# Naskah penghubung draft editorial; sumber Event_Nagisa, Alur_Cabang/02
# dan Sistem_Cabang_dan_Poin §1. Tidak ditampilkan sebagai teks desain.
label kkscene_N04:
    call kk_scene_enter("nagisa", "Tepi Sungai · Kembang api")
    nar "Nagisa menunggu Koita menoleh. Ketika ia akhirnya membuka mulut, kembang api menelan suaranya."
    nagisa "Sudahlah. Dia bahkan tidak dengar."
    menu:
        "Tetap di sampingnya.":
            $ kk_record_choice("N04","A")
            nagisa "Jangan pasang muka kasihan begitu. ...Tapi duduklah."
        "Beri dia kesempatan bicara berdua dengan Koita.":
            $ kk_record_choice("N04","B")
            nagisa "Koita, sebentar saja. Ada yang mau kukatakan."
        "Panggil Koita sebelum Nagisa melanjutkan.":
            $ kk_record_choice("N04","C")
            nar "Nagisa memelototimu. Tangannya perlahan berhenti meremas lengan yukatanya."
    return

label kkscene_N06:
    call kk_scene_enter("nagisa", "Studio Arsitektur")
    nar "Mochizuki menahan sisi maket agar Nagisa bisa merekatkan sambungannya."
    if "N03" in kk_missed:
        nagisa "Yang waktu hujan itu juga dia yang bantu."
    menu:
        "Beri mereka ruang untuk bekerja.":
            $ kk_record_choice("N06","A")
            nagisa "Nah, yang ini sudah lurus."
        "Tawarkan mengambil alih pekerjaan Mochizuki.":
            $ kk_record_choice("N06","B")
            nagisa "Kau juga mau bantu?"
        "Akui bahwa kau ingin dia meminta bantuanmu.":
            $ kk_record_choice("N06","C")
            nagisa "Kenapa tidak bilang sejak tadi?"
    return

label kk_phone_rematch:
    if not kk_phone_event():
        return
    $ _msg = KK_DYN_BY_ID["N-D01"]
    nagisa "Masih bangun? Satu pertandingan lagi. Kali ini jangan kabur."
    $ _opts = [(caption, Return(i), False) for i, caption in enumerate(_msg["choices"])]
    call screen kk_choice_panel(_opts, "Pesan dari Nagisa")
    $ _reply = _return
    if kk_record_choice("N-D01", ("A","B","C")[_reply]):
        if _reply == 1:
            nagisa "Ya sudah. Besok saja."
        else:
            if _reply == 2:
                nagisa "Kau sengaja kalah, ya?"
            else:
                nagisa "Menang tipis begitu jangan besar kepala."
            $ kk_minutes((6 - kk_slot) * 240 - kk_minute)
    return

init python:
    KK_DYN_BY_ID = {event["id"]: event for event in KK_EVENTS_DYN}

    def kk_phone_event():
        return (not kk_done("N-D01") and
                kk_slot in (4,5) and kk_rel_get("nagisa","aff") >= 25)

    def kk_can_skip():
        return not kk_graduated and (kk_elapsed_days >= 7 or kk_has("q01_complete"))

    def kk_skip_week():
        if not kk_can_skip():
            return
        for day in range(7):
            kk_new_day()
            if kk_graduated or kk_is_hanami_date() or (kk_bulan, kk_hari_n) == (5,9):
                break
        store.kk_slot = 0
        store.kk_minute = 0

    def kk_is_hanami_date():
        return kk_bulan == 1 and kk_hari_n in (19,20)

    def kk_sleep():
        # Dua slot empat jam. Pulihkan beban energi per slot dan utang satu malam.
        before = body.get("energi",100)
        debt = body.get("utang_tidur",0)
        kk_minutes(480, sleeping=True)
        store.body["energi"] = min(100, before + 12)
        store.body["utang_tidur"] = max(0,debt - 8)

    def kk_epilogue():
        result = [kk_resolve_ending()]
        if result == ["E-SI-05"] and (kk_done_kindness()):
            result = ["E-SI-13"]
        # Katalog §1: jangan menggambarkan karier host masa depan setelah kematian.
        miyuki = kk_miyuki_ending()
        nagisa = kk_nagisa_ending()
        partners = int(miyuki in ("E-MI-05","E-MI-13","E-MI-01")) + int(nagisa == "E-NA-01")
        if partners:
            result.append("E-HP-02" if partners > 1 else "E-HP-01")
        elif not any(kk_has(f) for f in ("romansa_dimulai","chiasa_yutaka_saja")):
            result.append("E-HP-05")
        if nagisa:
            result.append(nagisa)
        if miyuki:
            result.append(miyuki)
        if result[0] in ("E-SI-01","E-SI-02","E-SI-03","E-SI-18"):
            if kk_host == "yutaka" and kk_has("job_outside"):
                result.append("E-YH-02")
            elif kk_host == "yutaka" and kk_has("intern_abroad"):
                result.append("E-YH-06")
            elif kk_host == "chiasa" and "E-HP-05" in result:
                result.append("E-CF-10")
        return result

    def kk_done_kindness():
        return any((c["ev"],c["key"]) in (("Mi03","A"),("N03","A")) for c in choices_log)


    def kk_pudding_message():
        return (kk_slot == 4 and kk_minute >= 60 and kk_minute < 120 and
                not kk_done("Mi-D01") and kk_rel_get("miyuki","trust") >= 25 and
                kk_get("dimanja_miyuki",10) >= 50)

    def kk_social_event(cid, place):
        if kk_daily_place(cid) != place:
            return None
        if cid == "nagisa" and kk_slot == 1 and not kk_done("N-D02"):
            if kk_rel_get(cid,"aff") >= 55 and kk_get("gengsi_nagisa",70) >= 50:
                return "N-D02"
        if cid == "miyuki" and kk_has("puji_pastry") and not kk_done("Mi-D03"):
            if kk_rel_get(cid,"aff") >= 55:
                return "Mi-D03"
        return None

label kk_social_scene(eid):
    # Draft editorial dari pemicu dan pilihan katalog dinamis.
    if kk_done(eid):
        return
    if eid == "N-D02":
        nagisa "Ini bukan khusus buatmu. Kebetulan saja aku bawa satu lebih."
    else:
        miyuki "Kau pernah bilang suka pastry-ku. Lihat, kali ini ada namamu."
    $ _row = KK_DYN_BY_ID[eid]
    $ _rows = [(caption, Return(key), False) for key, caption in zip("ABC", _row["choices"]) if not (eid == "Mi-D03" and key == "A" and kk_daily_place("koita") != _lokasi)]
    call screen kk_choice_panel(_rows, "Apa yang kau lakukan?")
    $ _key = _return
    $ kk_record_choice(eid,_key)
    if eid == "N-D02":
        if _key == "A":
            nagisa "Pelankan suaramu! Orang-orang jadi lihat ke sini."
        elif _key == "B":
            nagisa "...Kalau kau suka, habiskan."
        else:
            nar "Ia mengambil kembali bekal itu."
    else:
        if _key == "A":
            nar "Koita memperhatikan tulisan pada pastry itu."
        elif _key == "B":
            nar "Kau menyimpannya sebelum orang lain melihat tulisan itu."
        else:
            nar "Kau membagi pastry itu di tempat."
    $ kk_minutes(10)
    return

label kk_pudding:
    miyuki "Maaf, sudah malam. Kalau kau lewat konbini, boleh titip puding? Sekali ini saja."
    $ _rows = [(caption, Return(key), False) for key, caption in zip("ABCD",KK_DYN_BY_ID["Mi-D01"]["choices"])]
    call screen kk_choice_panel(_rows, "Balas pesan Miyuki")
    $ _key = _return
    $ kk_record_choice("Mi-D01", _key)
    if _key == "A":
        $ kk_rel("miyuki","intim",1)
        miyuki "Kau masih mau duduk denganku? Terima kasih."
    elif _key == "B":
        miyuki "Terima kasih. Hati-hati pulang."
    else:
        miyuki "...Oh. Baiklah."
    $ kk_minutes(15)
    return

