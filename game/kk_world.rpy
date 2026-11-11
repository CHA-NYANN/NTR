# Kouseikan — navigasi dunia (Hybrid Location Navigation + Cinematic VN).
# Distrik → lokasi → KEHIDUPAN di lokasi: siapa yang ada, apa yang bisa dilakukan,
# dan peristiwa yang muncul karena konteks. Bukan eksplorasi top-down (✅ GDD 6A, 6L.6).
#
# Angka aktivitas, biaya, dan aturan kehadiran di file ini adalah 🟡 USULAN (GDD 6F/6D
# menyebut kategorinya tapi menyatakan nilainya "belum ditetapkan"). Mudah diedit di sini.
#
# Alur 7 langkah (arahan UX): pilih tujuan → waktu maju → state/NPC diproses →
# cek event memenuhi syarat → masuk VN bila ada → akibat diterapkan → kembali ke dunia.
#
# Jadwal NPC TIDAK ditandai ke pemain (✅ 6L.1/6L.7): layar tidak pernah bilang "ada
# event di sini". Satu-satunya petunjuk organik adalah kehadiran orang itu sendiri.

init -4 python:

    # ── Distrik & lokasi (data dari docs/Jadwal_Harian_NPC.md §2) ──
    KK_DISTRICTS = [
        ("d1", "Kampus Kouseikan", ["Gedung Sastra", "Gedung Ekonomi", "Gedung Sains & Lab",
            "Gedung Seni Rupa & Studio", "Gedung Arsitektur", "Gedung Kedokteran",
            "Perpustakaan Pusat", "Kantin Pusat", "Taman Kampus", "Asrama Putri",
            "Ruang BEM", "Pusat Konseling", "Kafe Komorebi"]),
        ("d2", "Hunian Biasa", ["Rumah Amamiya", "Rumah Sakurajima", "Kos Moeka", "Taman Lingkungan"]),
        ("d3", "Distrik Elite", ["Apartemen Yutaka", "Apartemen Miyuki", "Rumah Saionji", "Klub Catur"]),
        ("d4", "Pusat Kota", ["Mall", "Bioskop", "Karaoke / Arcade", "Restoran", "Studio Foto"]),
        ("d5", "Stasiun & Pasar", ["Stasiun Kouseikan-mae", "Toko Thrift", "Pasar Tradisional", "Bimbel"]),
        ("d6", "Medis", ["Rumah Sakit Tachibana", "Klinik"]),
        ("d7", "Alam & Pantai", ["Kuil", "Tepi Sungai", "Pantai", "Taman Besar", "Vila (Izu)"]),
    ]
    KK_DISTRICT_NAME = {d: n for d, n, _ in KK_DISTRICTS}
    KK_DISTRICT_LOCS = {d: l for d, n, l in KK_DISTRICTS}

    # ── Peta event milestone → (bulan, distrik, lokasi, pemicu) ──
    # pemicu "enter": muncul saat memasuki lokasi (peristiwa berkumpul).
    # pemicu = cid: muncul saat berbicara dengan karakter itu di sana.
    KK_MILESTONE_MAP = [
        ("N01", 1, "d1", "Gedung Arsitektur", "nagisa"),
        ("Mi01", 1, "d1", "Taman Kampus", "enter"),
        ("N03", 3, "d1", "Gedung Arsitektur", "nagisa"),
        ("Mi03", 4, "d6", "Rumah Sakit Tachibana", "miyuki"),
    ]

    def kk_pending_enter(distrik, lokasi):
        return [m[0] for m in KK_MILESTONE_MAP
                if m[4] == "enter" and m[1] == store.kk_bulan and m[2] == distrik
                and m[3] == lokasi and not kk_done(m[0])]

    def kk_pending_talk(cid, distrik, lokasi):
        return [m[0] for m in KK_MILESTONE_MAP
                if m[4] == cid and m[1] == store.kk_bulan and m[2] == distrik
                and m[3] == lokasi and not kk_done(m[0])]

    # ── Kehadiran NPC (jadwal, disederhanakan; 🟡) ──
    # lokasi → [(cid, {slot...})]. Hanya karakter yang bisa diajak bicara.
    KK_FREQ = {
        "Gedung Sastra":   [("koita", {0, 1})],
        "Kantin Pusat":    [("koita", {1}), ("moeka", {1})],
        "Perpustakaan Pusat": [("miyuki", {3, 4}), ("harumi", {3, 4})],
        "Gedung Kedokteran":  [("miyuki", {1, 2})],
        "Rumah Sakit Tachibana": [("miyuki", {2, 3})],
        "Gedung Sains & Lab": [("harumi", {1, 2})],
        "Gedung Arsitektur":  [("nagisa", {1, 2})],
        "Gedung Seni Rupa & Studio": [("chiasa", {1, 2})],
        "Klub Catur":      [("shiori", {2})],
        "Kafe Komorebi":   [("koita", {2, 3})],
        "Rumah Amamiya":   [("koita", {0, 3, 4}), ("chiasa", {0, 4})],
        "Asrama Putri":    [("harumi", {3, 4})],
        "Taman Kampus":    [("nagisa", {2})],
        "Taman Lingkungan": [("nagisa", {2, 5})],
        "Apartemen Yutaka": [("yutaka", {4, 5})],
    }

    def kk_present_here(distrik, lokasi):
        # Cache per (lokasi, waktu): stabil lintas redraw screen, hanya re-roll saat waktu berubah.
        stamp = (lokasi, store.kk_bulan, store.kk_hari_n, store.kk_slot)
        cache = getattr(store, "_present_cache", None)
        if cache and cache[0] == stamp:
            return cache[1]
        out = []
        for cid, slots in KK_FREQ.get(lokasi, []):
            if cid == store.kk_host:
                continue  # host = pemain, bukan NPC
            # jadwal berubah karena rute (contoh minimal)
            st = store.stage.get(cid, 0)
            here = store.kk_slot in slots
            if cid == "moeka" and st >= 3 and store.kk_slot in (1, 2):
                here = False  # menarik diri
            if cid == "nagisa" and st >= 3:
                here = True   # muncul di lokasimu
            # variasi acak (jadwal tidak tetap) — rollback-safe
            if here and renpy.random.random() < 0.12:
                here = False
            # jaminan: kalau ada event "talk" tertunda untuk dia di sini+sekarang, ia pasti ada
            if kk_pending_talk(cid, distrik, lokasi):
                here = True
            if here and cid not in out:
                out.append(cid)
        store._present_cache = (stamp, out)
        return out

    # ── Aktivitas sehari-hari (🟡 nilai usulan) ──
    def _ok_makan():   return store.saldo >= 800
    def _fn_makan():
        store.saldo -= 800
        kk_adj_body("lapar", -60); kk_adj_body("energi", 8)
    def _fn_kerja():
        store.saldo += 3000
        kk_adj_body("energi", -20); kk_adj_body("kebersihan", -6)
    def _fn_belajar():
        kk_adj_body("energi", -15); kk_adj("belajar", 5)
    def _fn_santai():
        kk_adj_body("energi", 12); kk_adj_body("stres_host", -10)

    KK_ACTS = {
        "makan":   {"label": "Makan", "desc": "¥800 · lapar hilang, energi naik", "ok": _ok_makan,
                    "fn": _fn_makan, "done": "Kau makan. Perutmu tenang.", "fail": "Saldo tidak cukup untuk makan di sini."},
        "kerja":   {"label": "Kerja paruh waktu", "desc": "+¥3.000 · menguras energi", "ok": lambda: True,
                    "fn": _fn_kerja, "done": "Shift selesai. ¥3.000 masuk ke saldomu.", "fail": ""},
        "belajar": {"label": "Belajar", "desc": "energi turun · nilai akademik naik", "ok": lambda: True,
                    "fn": _fn_belajar, "done": "Kau belajar beberapa jam. Kepalamu penuh.", "fail": ""},
        "santai":  {"label": "Bersantai", "desc": "energi naik · stres turun", "ok": lambda: True,
                    "fn": _fn_santai, "done": "Kau duduk sebentar, membiarkan waktu lewat.", "fail": ""},
    }
    KK_ACT_BY_LOC = {
        "Kantin Pusat": ["makan"], "Restoran": ["makan"], "Kafe Komorebi": ["makan", "kerja"],
        "Studio Foto": ["kerja"], "Perpustakaan Pusat": ["belajar"], "Bimbel": ["belajar"],
        "Asrama Putri": ["belajar"], "Taman Kampus": ["santai"], "Taman Lingkungan": ["santai"],
        "Tepi Sungai": ["santai"], "Pantai": ["santai"], "Taman Besar": ["santai"], "Kuil": ["santai"],
    }

    def kk_acts_at(lokasi):
        return [(a, KK_ACTS[a]) for a in KK_ACT_BY_LOC.get(lokasi, [])]


# ══════════════════════════════════════════════════════════════════════════
# LATAR lokasi (placeholder editorial — status jelas placeholder, bukan canon)
# ══════════════════════════════════════════════════════════════════════════
screen kk_place_bg(distrik, lokasi, tint=kk_accent):
    zorder -10
    add kk_ink2
    add Solid(tint + "26") xpos 0.60 xsize 0.40 ysize 1.0
    add Solid(tint + "66") pos (1150, 0) xysize (4, 1080)
    text lokasi.upper():
        xpos 0.97 xanchor 1.0 ypos 0.62 yanchor 0.5 size 100 bold True color (tint + "16")


# ══════════════════════════════════════════════════════════════════════════
# PETA DISTRIK
# ══════════════════════════════════════════════════════════════════════════
screen kk_world_district():
    tag kk_world
    use kk_place_bg("", "Kouseikan", kk_acc2)
    use kk_hud
    vbox:
        xpos kk_margin ypos 150 spacing 10
        $ mt = kk_month_tuple()
        text ("[mt[0]] · " + mt[2]) style "kk_caption"
        text "Ke mana kau pergi?" style "kk_heading"
        text ("Hari ke-" + str(kk_hari_n) + " · " + KK_SLOTS[kk_slot] + ". Berpindah distrik memakan waktu.") style "kk_caption"
        null height 10
        for did, dnama, locs in KK_DISTRICTS:
            button:
                style "kk_button" xysize (1360, 84) action Return(("go", did))
                hbox:
                    yalign .5 spacing 36
                    text dnama size 28 bold True xsize 440
                    text (str(len(locs)) + " lokasi") style "kk_caption" yalign .5
    vbox:
        pos (kk_margin, 980) spacing 6
        if kk_bulan < 36:
            use kk_link("Lewati waktu ke bulan depan  »", Return(("skip", None)), 520)
        use kk_link("Alat uji", Show("kk_debug_panel"), 520)

screen kk_debug_panel():
    modal True
    zorder 90
    key "game_menu" action Hide("kk_debug_panel")
    add Solid("#101b24ee")
    frame:
        align (.5, .5) xysize (860, 600) background Solid(kk_ink2) padding (48, 42)
        vbox:
            spacing 20
            text "Alat uji" style "kk_heading"
            text "Bukan bagian cerita. Untuk memeriksa konten, bukan untuk dimainkan normal." style "kk_caption" xmaximum 740
            null height 8
            use kk_link("Jelajah semua cabang (190 event)", [Hide("kk_debug_panel"), Jump("kk_debug_explore")], 740)
            use kk_link("Galeri ending (220, berisi spoiler)", [Hide("kk_debug_panel"), ShowMenu("kk_gallery")], 740)
            use kk_link("Lompat ke evaluasi (M36)", [Hide("kk_debug_panel"), Jump("kk_debug_eval")], 740)
            null height 10
            use kk_link("Tutup", Hide("kk_debug_panel"), 740)


# ══════════════════════════════════════════════════════════════════════════
# DAFTAR LOKASI dalam distrik
# ══════════════════════════════════════════════════════════════════════════
screen kk_world_location(distrik):
    tag kk_world
    use kk_place_bg(distrik, KK_DISTRICT_NAME[distrik], kk_acc2)
    use kk_hud
    vbox:
        xpos kk_margin ypos 150 spacing 10
        text "Distrik" style "kk_caption"
        text KK_DISTRICT_NAME[distrik] style "kk_heading"
        null height 8
        viewport:
            xysize (1360, 720) mousewheel True draggable renpy.variant("touch") scrollbars "vertical"
            vbox:
                spacing 8
                for lokasi in KK_DISTRICT_LOCS[distrik]:
                    button:
                        style "kk_button" xysize (1320, 76) action Return(lokasi)
                        text lokasi size 26 yalign .5
    fixed:
        pos (kk_margin, 980)
        use kk_link("‹ Kembali ke peta", Return("back"))


# ══════════════════════════════════════════════════════════════════════════
# DALAM LOKASI — siapa di sini, apa yang bisa dilakukan (inti mode navigasi)
# ══════════════════════════════════════════════════════════════════════════
screen kk_location_view(distrik, lokasi):
    tag kk_world
    $ present = kk_present_here(distrik, lokasi)
    $ acts = kk_acts_at(lokasi)
    use kk_place_bg(distrik, lokasi, kk_accent)
    use kk_hud
    # Identitas tempat (kiri)
    vbox:
        xpos kk_margin ypos 150 spacing 8 xsize 820
        text KK_DISTRICT_NAME[distrik] style "kk_caption"
        text lokasi style "kk_heading"
        add Solid(kk_accent) xysize (72, 4)
        null height 6
        text KK_LOC_AMBIENCE.get(lokasi, "Tempat biasa. Dunia tetap berjalan di tempat lain.") style "kk_caption" xmaximum 760

    # Siapa di sini + aktivitas (kanan)
    vbox:
        pos (980, 150) spacing 28 xsize 820
        vbox:
            spacing 10
            text "SIAPA DI SINI" size 20 color kk_dim font kk_mono
            if present:
                for cid in present:
                    $ meta = KK_CHARS[cid]
                    button:
                        style "kk_button" xysize (800, 78) action Return(("talk", cid))
                        hbox:
                            yalign .5 spacing 18
                            add Solid(meta["warna"]) xysize (10, 44) yalign .5
                            text meta["nama"] size 25 bold True yalign .5
            else:
                text "Tidak ada orang yang kau kenal di sini sekarang." style "kk_caption"
        vbox:
            spacing 10
            text "YANG BISA KAU LAKUKAN" size 20 color kk_dim font kk_mono
            for aid, a in acts:
                button:
                    style "kk_button" xysize (800, 72) action Return(("act", aid)) sensitive a["ok"]()
                    hbox:
                        yalign .5 spacing 16
                        text a["label"] size 24 bold True yalign .5 xsize 300
                        text a["desc"] style "kk_caption" yalign .5
            if not acts:
                text "Tidak ada aktivitas khusus di sini." style "kk_caption"
    fixed:
        pos (kk_margin, 980)
        use kk_link("‹ Pergi dari sini", Return(("leave", None)))


# ══════════════════════════════════════════════════════════════════════════
# ALUR navigasi dunia
# ══════════════════════════════════════════════════════════════════════════
label kk_world_loop:
    call screen kk_world_district
    $ _r = _return
    if _r[0] == "skip":
        $ _b = kk_next_month()
        scene black with fade
        $ _mt = kk_month_tuple()
        nar "Minggu-minggu berlalu. [_mt[0]] — [_mt[2]]."
        jump kk_world_loop
    $ _distrik = _r[1]
    $ kk_advance(1)   # (1-2) berpindah distrik memakan waktu; tubuh menanggung
    jump kk_loc_list

label kk_loc_list:
    call screen kk_world_location(_distrik)
    if _return == "back":
        jump kk_world_loop
    $ _lokasi = _return
    # (3-4) peristiwa berkumpul yang muncul begitu kau tiba
    $ _ent = kk_pending_enter(_distrik, _lokasi)
    if _ent:
        call kk_play_scene(_ent[0])
    jump kk_location_view_loop

label kk_location_view_loop:
    call screen kk_location_view(_distrik, _lokasi)
    $ _c = _return
    if _c[0] == "leave":
        jump kk_loc_list
    elif _c[0] == "talk":
        call kk_do_talk(_distrik, _lokasi, _c[1])
        jump kk_location_view_loop
    elif _c[0] == "act":
        call kk_do_activity(_lokasi, _c[1])
        jump kk_location_view_loop

label kk_do_talk(distrik, lokasi, cid):
    $ _p = kk_pending_talk(cid, distrik, lokasi)
    if _p:
        # (5-6) event kontekstual via orang yang tepat — akibat lewat hook, tidak diumumkan
        call kk_play_scene(_p[0])
    else:
        call kk_generic_talk(cid, KK_DISTRICT_NAME[distrik] + " · " + lokasi)
    return

# Obrolan ringan tanpa event: beberapa kata, tanpa pilihan abstrak.
# Sekadar hadir & bicara menumbuhkan kedekatan sedikit, diam-diam.
label kk_generic_talk(cid, loc):
    $ _name = KK_CHARS[cid]["nama"]
    $ _key = "ngobrol_%s_%d_%d_%d" % (cid, kk_bulan, kk_hari_n, kk_slot)
    if kk_has(_key):
        nar "Kalian sudah bicara tadi. [_name] kembali ke urusannya."
        return
    $ kk_flag(_key)
    $ kk_rel(cid, "intim", 1)
    call kk_scene_enter(cid, loc)
    $ renpy.say(getattr(store, cid), "Oh, kau. Sedang apa di sini?")
    nar "Kalian bertukar beberapa kata ringan. Tidak terjadi apa-apa yang istimewa — baru. (Dialog berkarakter untuk obrolan bebas menyusul.)"
    return

label kk_do_activity(lokasi, actid):
    $ a = KK_ACTS[actid]
    if not a["ok"]():
        nar "[a['fail']]"
        return
    call kk_scene_enter(kk_host, lokasi)
    $ a["fn"]()
    $ kk_advance(1)   # (2) aktivitas memakan waktu
    nar "[a['done']]"
    return

# Beat sinematis masuk adegan (reuse latar kk_set milik sistem visual bersama).
label kk_scene_enter(char, loc_label):
    show screen kk_set(char, loc_label)
    with Dissolve(0.4)
    return


# ══════════════════════════════════════════════════════════════════════════
# Alat uji — dipisah dari alur pemain, tidak dihapus.
# ══════════════════════════════════════════════════════════════════════════
label kk_debug_explore:
    call kk_explore_loop
    jump kk_world_loop

label kk_debug_eval:
    jump kk_evaluasi


# Ambience lokasi (🟡 placeholder singkat; hanya yang relevan di slice).
init -4 python:
    KK_LOC_AMBIENCE = {
        "Taman Kampus": "Sakura belum sepenuhnya gugur. Beberapa kelompok duduk di bawah pohon — hari Hanami.",
        "Gedung Arsitektur": "Bau kayu maket dan kertas potong. Studio di lantai atas masih ramai.",
        "Kafe Komorebi": "Aroma kopi dari gerbang depan kampus. Tempat paling mudah menemukan orang.",
        "Perpustakaan Pusat": "Sepi dan dingin. Beberapa mahasiswa tertidur di meja sendiri.",
        "Kantin Pusat": "Jam makan selalu padat. Koita biasanya ada di salah satu meja.",
        "Rumah Sakit Tachibana": "Bau antiseptik dan lampu neon. Koridor mahasiswa kedokteran di ujung lorong.",
        "Rumah Amamiya": "Rumah tempatmu — atau tempat yang harus kau anggap rumah sekarang.",
        "Klub Catur": "Jam dinding berdetak. Papan-papan tertata rapi menunggu lawan.",
    }
