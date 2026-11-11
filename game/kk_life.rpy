# Kalender relatif: epoch teknis yang cocok dengan Senin 7 April (Milestone §1).
# Epoch bukan penetapan tahun cerita. Hanya nilai sederhana disimpan dalam save.
default kk_minute = 0
default kk_calendar_version = 0
default kk_world_seed = 0
default kk_elapsed_days = 0
default kk_graduated = False
default kk_missed = []
default kk_due = {}
default kk_promises = {}
default kk_npc_rel = {}
default kk_last_met = {}
define kk_debug_tools = False

init python:
    import calendar
    import datetime
    import hashlib

    def kk_date():
        index = 3 + kk_bulan - 1
        year, month = 2025 + index // 12, index % 12 + 1
        return datetime.date(year, month, min(kk_hari_n, calendar.monthrange(year, month)[1]))

    def kk_sync_calendar():
        store.kk_hari = ("Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu")[kk_date().weekday()]

    def kk_upgrade_world():
        if kk_calendar_version:
            return
        # Save lama menghitung hari dari 1, dan dapat melewati akhir bulan.
        old_day = max(1, kk_hari_n)
        store.kk_hari_n = 1
        d = min(kk_date() + datetime.timedelta(days=old_day - 1 + (6 if kk_bulan == 1 else 0)),
                datetime.date(2028, 3, 31))
        store.kk_bulan = (d.year - 2025) * 12 + d.month - 3
        store.kk_hari_n = d.day
        store.kk_elapsed_days = (d - datetime.date(2025,4,7)).days
        store.kk_world_seed = renpy.random.randint(1, 2147483647)
        if not kk_rel_base:
            store.kk_rel_base = {cid: dict(values) for cid, values in rel.items()}
        store.kk_calendar_version = 1
        kk_sync_calendar()

    def kk_new_day():
        if kk_bulan == 36 and kk_hari_n == 31:
            store.kk_graduated = True
            return
        old_month = kk_bulan
        d = kk_date() + datetime.timedelta(days=1)
        store.kk_bulan = (d.year - 2025) * 12 + d.month - 3
        store.kk_hari_n = d.day
        store.kk_elapsed_days += 1
        kk_sync_calendar()
        for cid, (day, slot, place) in list(kk_promises.items()):
            if day < kk_elapsed_days:
                del store.kk_promises[cid]
                if not kk_schedule_away(cid, day, slot):
                    kk_rel(cid, "trust", -3)
        for eid, month, district, loc, trigger in KK_MILESTONE_MAP:
            if old_month == month and kk_bulan != month and not kk_done(eid) and eid not in kk_missed:
                store.kk_missed.append(eid)
        if old_month != kk_bulan and kk_bulan >= 7:
            kk_adj("omiai_takeru", 3)
            if old_month in (9,21) and not kk_done("Mi09" if old_month == 9 else "Mi18"):
                kk_adj("omiai_takeru", 5)
            if old_month == 33 and not kk_done("Mi25") and kk_get("omiai_takeru") >= 90:
                kk_flag("hayase_engaged")
        if old_month == 3 and kk_bulan == 4 and "N03" in kk_missed:
            store.kk_npc_rel["yuuto_nagisa_studio"] = "membantu maket"
        if kk_bulan == 1:
            for eid, deadline in (("N01",7), ("Mi01",20)):
                if d.day > deadline and not kk_done(eid) and eid not in kk_missed:
                    store.kk_missed.append(eid)
        if kk_due.get("koita_reply", float("inf")) <= kk_elapsed_days:
            del store.kk_due["koita_reply"]
            kk_flag("nagisa_koita_ditolak")
            store.kk_npc_rel["nagisa_koita"] = "goyah"
            store.kk_npc_rel["harapan_koita"] = min(44, kk_npc_rel.get("harapan_koita",70))
        if kk_elapsed_days == 7 and not kk_has("q01_complete"):
            kk_flag("q01_expired")
        if kk_elapsed_days % 7 == 0:
            for cid in rel:
                for dim, step in (("jeal",2),("fear",1)):
                    base = kk_rel_base.get(cid, {}).get(dim, 0)
                    excess = kk_rel_get(cid, dim) - base
                    if excess > 0:
                        kk_rel(cid, dim, -min(excess, step))
                if kk_elapsed_days - kk_last_met.get(cid, 0) >= 14:
                    kk_rel(cid, "aff", -1)
                    kk_rel(cid, "intim", -1)
            if kk_bulan >= 13:
                kk_adj("kelelahan_miyuki", 3)

    # Alur_Cabang/14: trust kecil saat berjanji, lebih besar ketika ditepati.
    def kk_make_promise(cid, place):
        if cid in kk_promises or kk_graduated:
            return False
        store.kk_promises[cid] = (kk_elapsed_days + 1, kk_slot, place)
        kk_rel(cid, "trust", 1)
        return True

    def kk_keep_promise(cid, place):
        if kk_promises.get(cid) != (kk_elapsed_days, kk_slot, place):
            return False
        del store.kk_promises[cid]
        kk_rel(cid, "trust", 3)
        return True

    def kk_contact(cid):
        store.kk_last_met[cid] = kk_elapsed_days
        if kk_elapsed_days < 7 and cid in ("miyuki","nagisa","harumi","moeka","shiori"):
            kk_flag("q01_met_" + cid)
            if sum(f.startswith("q01_met_") for f in flags) >= 3:
                kk_flag("q01_complete")

    def kk_record_choice(eid, key):
        if kk_done(eid):
            return False
        kk_log(eid, key)
        if _char_of(eid) != kk_host:
            kk_contact(_char_of(eid))
        kk_run_hook(eid, key)
        return True

    def kk_is_hanami():
        return kk_bulan == 1 and kk_hari_n in (19,20) and kk_slot in (1,2)

    def kk_window(eid):
        if eid in ("N22","Mi09","Mi18","Mi25"):
            return kk_hari_n in (24,25) and (eid != "Mi25" or kk_get("omiai_takeru") >= 70)
        if eid == "N01":
            return kk_hari_n == 7 and kk_slot in (1,2)
        if eid == "Mi01":
            return kk_is_hanami()
        if eid == "Mi03":
            return kk_slot == 4
        if eid == "N04":
            return kk_hari_n == 9 and kk_slot == 3
        return True

    def kk_planned_place(cid):
        # Jadwal verbal tanpa lokasi tertentu menghasilkan None.
        week = kk_date().weekday()
        slot = kk_slot
        if kk_is_hanami() and cid in ("miyuki","moeka","shiori","nagisa","harumi","koita","chiasa"):
            return "Taman Kampus"
        if cid == "nagisa" and kk_bulan == 5 and kk_hari_n == 9 and slot == 3:
            return "Tepi Sungai"
        if cid == "miyuki" and kk_bulan in (4,16,28) and slot == 4 and week < 5:
            return "Rumah Sakit Tachibana"
        if cid == "miyuki" and kk_bulan in (9,21,33) and kk_hari_n in (24,25) and slot == 3:
            return "Rumah Sakit Tachibana"
        if cid == "nagisa" and kk_bulan == 33 and kk_hari_n in (24,25) and slot == 3:
            return "Rumah Sakurajima"
        if cid == "moeka" and stage.get(cid,0) >= 3 and slot in (1,2):
            return None
        if cid == "miyuki" and stage.get(cid,0) >= 2 and slot in (3,4):
            return "Rumah Sakit Tachibana"
        if week >= 5:
            weekend = {
                "nagisa": ("Rumah Sakurajima", None, None, "Rumah Sakurajima", "Rumah Sakurajima", "Rumah Sakurajima"),
                "miyuki": ("Apartemen Miyuki", "Rumah Sakit Tachibana", "Kafe Komorebi", None, "Apartemen Miyuki", "Apartemen Miyuki"),
                "shiori": ("Rumah Saionji", "Klub Catur", None, "Rumah Saionji", "Rumah Saionji", "Rumah Saionji"),
                "harumi": ("Perpustakaan Pusat","Perpustakaan Pusat","Gedung Sains & Lab","Asrama Putri","Asrama Putri","Asrama Putri"),
                "moeka": ("Toko Thrift", "Studio Foto", None, None, "Kos Moeka", "Kos Moeka"),
                "chiasa": (None, "Toko Thrift", "Kafe Komorebi", None, "Rumah Amamiya", "Rumah Amamiya"),
                "koita": ("Kafe Komorebi", None, "Kafe Komorebi", None, "Rumah Amamiya","Rumah Amamiya"),
                "yutaka": ("Apartemen Yutaka",None,None,None,"Apartemen Yutaka","Apartemen Yutaka"),
            }
            if week == 6:
                return {"nagisa":"Rumah Sakurajima","miyuki":"Apartemen Miyuki","koita":"Rumah Amamiya",
                        "harumi":"Asrama Putri","shiori":"Rumah Saionji","chiasa":"Rumah Amamiya"}.get(cid) if slot >= 3 else None
            return weekend[cid][slot]
        if cid == "koita" and slot == 1 and week in (1,3):
            return "Perpustakaan Pusat"
        locations = [loc for loc, people in KK_FREQ.items()
                     if any(who == cid and slot in slots for who, slots in people)]
        if not locations:
            return None
        return locations[(kk_elapsed_days + slot) % len(locations)]

    def kk_schedule_away(cid, day, slot):
        data = ("%d/%d/%d/%s" % (kk_world_seed, day, slot, cid)).encode("ascii")
        rates = {"shiori":5, "harumi":8, "miyuki":10, "koita":12, "nagisa":15,
                 "yutaka":20, "chiasa":20, "moeka":30}
        return int.from_bytes(hashlib.sha256(data).digest()[:4], "big") % 100 < rates[cid]

    def kk_daily_place(cid):
        if cid == kk_host or kk_schedule_away(cid, kk_elapsed_days, kk_slot):
            return None
        promise = kk_promises.get(cid)
        if promise and promise[:2] == (kk_elapsed_days, kk_slot):
            return promise[2]
        return kk_planned_place(cid)

default kk_rel_base = {}


label after_load:
    $ kk_upgrade_world()
    return
