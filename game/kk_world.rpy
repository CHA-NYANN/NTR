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
    KK_DISTRICT_NAME["onsen"] = "Penginapan onsen"
    KK_DISTRICT_LOCS["onsen"] = ["Lobi ryokan", "Dapur ryokan", "Ruang bersama ryokan", "Taman luar ryokan"]
    KK_MILESTONE_MAP = [
        ("H01", 1, "d1", "Gedung Sains & Lab", "harumi"),
        ("H03", 4, "d1", "Asrama Putri", "harumi"),
        ("H08", 10, "d7", "Kuil", "harumi"),
        ("H09", 13, "d1", "Gedung Sains & Lab", "harumi"),
        ("Mo01", 1, "d1", "Taman Kampus", "moeka"),
        ("S01", 1, "d1", "Taman Kampus", "shiori"),
        ("Mo02", 2, "d5", "Stasiun Kouseikan-mae", "moeka"),
        ("S02", 2, "onsen", "Lobi ryokan", "shiori"),
        ("Mi02", 2, "onsen", "Dapur ryokan", "miyuki"),
        ("N02", 2, "onsen", "Ruang bersama ryokan", "nagisa"),
        ("N01", 1, "d1", "Gedung Arsitektur", "nagisa"),
        ("Mi01", 1, "d1", "Taman Kampus", "enter"),
        ("Mi07", 7, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("Mi09", 9, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("Mi18", 21, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("Mi25", 33, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("N22", 33, "d2", "Rumah Sakurajima", "nagisa"),
        ("C05", 8, "d2", "Rumah Amamiya", "host"),
        ("C11", 20, "d1", "Gedung Seni Rupa & Studio", "shiori"),
        ("C09", 16, "d2", "Rumah Amamiya", "host"),
        ("Y09", 13, "d3", "Apartemen Yutaka", "host"),
        ("Y13", 21, "d2", "Rumah Amamiya", "host"),
        ("Y17", 31, "d3", "Apartemen Yutaka", "host"),
        ("N04", 5, "d7", "Tepi Sungai", "nagisa"),
        ("N06", 7, "d1", "Gedung Arsitektur", "nagisa"),
        ("N03", 3, "d1", "Gedung Arsitektur", "nagisa"),
        ("Mi03", 4, "d6", "Rumah Sakit Tachibana", "miyuki"),
    ]

    def kk_pending_enter(distrik, lokasi):
        return [m[0] for m in KK_MILESTONE_MAP
                if ((m[4] == "enter" and kk_daily_place("miyuki") == lokasi) or
                    (m[4] == "host" and _char_of(m[0]) == kk_host)) and m[1] == store.kk_bulan and m[2] == distrik
                and m[3] == lokasi and kk_window(m[0]) and not kk_done(m[0]) and m[0] not in kk_missed]

    def kk_pending_talk(cid, distrik, lokasi):
        return [m[0] for m in KK_MILESTONE_MAP
                if m[4] == cid and kk_daily_place(cid) == lokasi and m[1] == store.kk_bulan and m[2] == distrik
                and m[3] == lokasi and kk_window(m[0]) and not kk_done(m[0]) and m[0] not in kk_missed]

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
        return [cid for cid in KK_CHARS if kk_daily_place(cid) == lokasi]

    # ── Aktivitas sehari-hari (🟡 nilai usulan) ──
    def _ok_makan():   return store.saldo >= 800
    def _fn_makan():
        kk_post_money(-800, "Makan")
        kk_adj_body("lapar", -60); kk_adj_body("energi", 8)
    def _fn_kerja():
        kk_post_money(3000, "Upah kerja paruh waktu")
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
        text (kk_hari + " · " + str(kk_hari_n) + " " + mt[1]) style "kk_caption"
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
        if kk_can_skip():
            use kk_link("Lanjutkan rutinitas mingguan", Return(("skip", None)), 520)
        if config.developer and kk_debug_tools:
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
        use kk_link("‹ Pulang ke stasiun" if distrik == "onsen" else "‹ Kembali ke peta", Return("back"))


# ══════════════════════════════════════════════════════════════════════════
# DALAM LOKASI — siapa di sini, apa yang bisa dilakukan (inti mode navigasi)
# ══════════════════════════════════════════════════════════════════════════
screen kk_location_view(distrik, lokasi):
    tag kk_world
    $ present = kk_present_here(distrik, lokasi)
    $ acts = kk_acts_at(lokasi)
    $ home = "Apartemen Yutaka" if kk_host == "yutaka" else "Rumah Amamiya"
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
    viewport:
        pos (980, 150) xysize (860, 780)
        mousewheel True draggable renpy.variant("touch") arrowkeys True scrollbars "vertical"
        vbox:
            spacing 28 xsize 820
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
                if lokasi == "Stasiun Kouseikan-mae" and kk_onsen_dates():
                    use kk_link("Berangkat ke penginapan onsen", Return(("travel", None)), 800)
                if distrik == "onsen":
                    use kk_link("Duduk sejenak di penginapan", Return(("rest", None)), 800)
                if kk_art_studio_open(lokasi):
                    use kk_link("Bicarakan sketsa dengan Haruka", Return(("portfolio", None)), 800)
                if kk_can_sketch(lokasi):
                    use kk_link("Latihan di buku sketsa", Return(("draw", None)), 800)
                if lokasi == home:
                    use kk_link("Beristirahat di kamar", Return(("sleep", None)), 800)
                if not acts and not kk_art_studio_open(lokasi) and lokasi != home and distrik != "onsen" and not (lokasi == "Stasiun Kouseikan-mae" and kk_onsen_dates()):
                    text "Tidak ada aktivitas khusus di sini." style "kk_caption"
    fixed:
        pos (kk_margin, 980)
        use kk_link("‹ Pergi dari sini", Return(("leave", None)))


# ══════════════════════════════════════════════════════════════════════════
# ALUR navigasi dunia
# ══════════════════════════════════════════════════════════════════════════
label kk_world_loop:
    $ kk_upgrade_world()
    if kk_graduated:
        jump kk_evaluasi
    call screen kk_world_district
    $ _r = _return
    if _r[0] == "skip":
        $ kk_skip_week()
        scene black with fade
        $ _mt = kk_month_tuple()
        nar "Rutinitasmu berlanjut. [kk_hari], [kk_hari_n] [_mt[1]]."
        jump kk_world_loop
    $ _distrik = _r[1]
    $ kk_minutes(60)
    jump kk_loc_list

label kk_loc_list:
    if kk_graduated:
        jump kk_evaluasi
    if _distrik == "onsen" and not kk_onsen_dates():
        jump kk_trip_return
    call screen kk_world_location(_distrik)
    if _return == "back":
        if _distrik == "onsen":
            jump kk_trip_return
        jump kk_world_loop
    $ _lokasi = _return
    $ kk_minutes(30)
    if kk_graduated:
        jump kk_evaluasi
    # (3-4) peristiwa berkumpul yang muncul begitu kau tiba
    $ _ent = kk_pending_enter(_distrik, _lokasi)
    if _ent:
        call kk_play_scene(_ent[0])
        $ kk_advance()
    elif kk_father_visit(_lokasi):
        call kk_visit_kisaragi
        $ kk_minutes(10)
    jump kk_location_view_loop

label kk_location_view_loop:
    $ kk_upgrade_world()
    if kk_graduated:
        jump kk_evaluasi
    if _distrik == "onsen" and not kk_onsen_dates():
        jump kk_trip_return
    $ _incoming = kk_incoming_messages()
    if _incoming:
        call expression _incoming[0][2]
        jump kk_location_view_loop
    call screen kk_location_view(_distrik, _lokasi)
    $ _c = _return
    if _c[0] == "leave":
        jump kk_loc_list
    elif _c[0] == "talk":
        call kk_do_talk(_distrik, _lokasi, _c[1])
        jump kk_location_view_loop
    elif _c[0] == "travel":
        $ kk_minutes(60)
        if kk_onsen_dates():
            $ _distrik = "onsen"
            nar "Kau menyusul rombongan ke penginapan."
            jump kk_loc_list
        nar "Kesempatan untuk menyusul rombongan sudah berlalu."
        jump kk_location_view_loop
    elif _c[0] == "rest":
        $ kk_advance()
        jump kk_location_view_loop
    elif _c[0] == "portfolio":
        call kk_show_portfolio
        jump kk_location_view_loop
    elif _c[0] == "draw":
        call kk_draw_at_home
        jump kk_location_view_loop
    elif _c[0] == "sleep":
        call kk_rest_home
        jump kk_location_view_loop
    elif _c[0] == "act":
        call kk_do_activity(_lokasi, _c[1])
        jump kk_location_view_loop

label kk_trip_return:
    $ _distrik = "d5"
    $ _lokasi = "Stasiun Kouseikan-mae"
    $ kk_minutes(60)
    nar "Kau kembali ke stasiun Kouseikan."
    jump kk_location_view_loop

label kk_do_talk(distrik, lokasi, cid):
    if cid not in kk_present_here(distrik, lokasi):
        return
    $ known = cid in kk_last_met
    if kk_keep_promise(cid, lokasi):
        nar "Kau datang seperti yang kalian janjikan."
    $ kk_contact(cid)
    $ _p = kk_pending_talk(cid, distrik, lokasi)
    if _p:
        # (5-6) event kontekstual via orang yang tepat — akibat lewat hook, tidak diumumkan
        call kk_play_scene(_p[0])
        if _p[0] == "N03" and any(c["ev"] == "N03" and c["key"] == "A" for c in choices_log):
            $ kk_minutes((6 - kk_slot) * 240 - kk_minute)
            return
    elif kk_social_event(cid, lokasi):
        call kk_social_scene(kk_social_event(cid, lokasi))
        return
    elif cid == "nagisa" and kk_has("nagisa_koita_ditolak") and not kk_has("heard_reply"):
        nagisa "Dia bilang kita teman masa kecil. Seperti itu saja."
        $ kk_flag("heard_reply")
    else:
        call kk_generic_talk(cid, KK_DISTRICT_NAME[distrik] + " · " + lokasi, known)
        return
    $ kk_advance()
    return

# Obrolan ringan tanpa event: beberapa kata, tanpa pilihan abstrak.
# Sekadar hadir & bicara menumbuhkan kedekatan sedikit, diam-diam.
label kk_generic_talk(cid, loc, known=True):
    $ _name = KK_CHARS[cid]["nama"]
    $ _key = "ngobrol_%s_%d_%d_%d" % (cid, kk_bulan, kk_hari_n, kk_slot)
    $ fresh = not kk_has(_key)
    $ kk_flag(_key)
    call kk_scene_enter(cid, loc)
    $ renpy.say(getattr(store, cid), "Oh, kau. Sedang apa di sini?")
    menu:
        "Buka kembali soal yang kalian baca bersama." if cid == "harumi" and any(c["ev"] == "H01" and c["key"] == "A" for c in choices_log):
            harumi "Mari kita periksa dari langkah pertama."
            if fresh:
                $ kk_rel("harumi", "trust", 1)
            $ kk_minutes(10)
        "Tanyakan bagaimana harinya." if known:
            if fresh:
                $ kk_rel(cid, "trust", 1)
            $ kk_minutes(10)
        "Janjikan bertemu lagi di sini besok pada waktu yang sama." if fresh and cid not in kk_promises:
            $ kk_make_promise(cid, _lokasi)
            $ kk_minutes(1)
            nar "Kalian sepakat bertemu lagi besok."
        "Balas sapaannya lalu pamit.":
            if fresh:
                $ kk_rel(cid, "aff", 2)
            $ kk_minutes(5)
        "Bawakan makanan untuk Miyuki." if cid == "miyuki" and saldo >= 800:
            $ kk_post_money(-800, "Makanan untuk Miyuki")
            if fresh:
                $ kk_adj("dimanja_miyuki",4)
                $ kk_adj("kelelahan_miyuki",-8)
            $ kk_minutes(60)
        "Puji pastry yang ia bawa." if cid == "miyuki" and _lokasi == "Kafe Komorebi" and kk_hari == "Sabtu":
            $ kk_flag("puji_pastry")
            if fresh:
                $ kk_rel(cid,"aff",2)
            $ kk_minutes(2)
    nar "Kalian bertukar beberapa kata ringan. Setelah itu ia kembali ke kegiatannya."
    return

label kk_do_activity(lokasi, actid):
    $ a = KK_ACTS[actid]
    if actid not in KK_ACT_BY_LOC.get(lokasi, []) or not a["ok"]():
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
    if not (config.developer and kk_debug_tools):
        jump kk_world_loop
    call kk_explore_loop
    jump kk_world_loop

label kk_debug_eval:
    if not (config.developer and kk_debug_tools):
        jump kk_world_loop
    jump kk_evaluasi


# Ambience lokasi (🟡 placeholder singkat; hanya yang relevan di slice).
init -4 python:
    KK_LOC_AMBIENCE = {
        "Taman Kampus": "Jalan setapak membelah taman di antara gedung-gedung kampus.",
        "Gedung Arsitektur": "Bau kayu maket dan kertas potong. Studio di lantai atas masih ramai.",
        "Kafe Komorebi": "Aroma kopi dari gerbang depan kampus. Tempat paling mudah menemukan orang.",
        "Perpustakaan Pusat": "Sepi dan dingin. Beberapa mahasiswa tertidur di meja sendiri.",
        "Kantin Pusat": "Jam makan selalu padat. Koita biasanya ada di salah satu meja.",
        "Rumah Sakit Tachibana": "Bau antiseptik dan lampu neon. Koridor mahasiswa kedokteran di ujung lorong.",
        "Rumah Amamiya": "Rumah tempatmu — atau tempat yang harus kau anggap rumah sekarang.",
        "Klub Catur": "Jam dinding berdetak. Papan-papan tertata rapi menunggu lawan.",
    }
