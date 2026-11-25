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
        ("H02", 3, "d1", "Gedung Sains & Lab", "harumi"),
        ("H05", 6, "d1", "Kafe Komorebi", "harumi"),
        ("H10", 14, "d5", "Stasiun Kouseikan-mae", "harumi"),
        ("H22", 33, "d5", "Stasiun Kouseikan-mae", "harumi"),
        ("H03", 4, "d1", "Asrama Putri", "harumi"),
        ("H08", 10, "d7", "Kuil", "harumi"),
        ("H09", 13, "d1", "Gedung Sains & Lab", "harumi"),
        ("Mo01", 1, "d1", "Taman Kampus", "moeka"),
        ("S03", 3, "d3", "Klub Catur", "shiori"),
        ("S06", 8, "d3", "Klub Catur", "shiori"),
        ("S08", 11, "d3", "Klub Catur", "shiori"),
        ("S11", 16, "d3", "Klub Catur", "shiori"),
        ("S12", 18, "d3", "Klub Catur", "shiori"),
        ("S10", 15, "d3", "Klub Catur", "shiori"),
        ("N20", 29, "d2", "Taman Lingkungan", "nagisa"),
        ("S07", 9, "d3", "Rumah Saionji", "shiori"),
        ("S09", 12, "d3", "Klub Catur", "shiori"),
        ("S14", 21, "d3", "Rumah Saionji", "shiori"),
        ("S15", 22, "d7", "Kuil", "shiori"),
        ("S16", 23, "d3", "Klub Catur", "shiori"),
        ("S13", 20, "d3", "Klub Catur", "shiori"),
        ("S18", 27, "d3", "Rumah Saionji", "shiori"),
        ("S19", 28, "d1", "Taman Kampus", "shiori"),
        ("H19", 28, "d1", "Taman Kampus", "harumi"),
        ("Mo20", 28, "d1", "Taman Kampus", "moeka"),
        ("N19", 28, "d1", "Taman Kampus", "nagisa"),
        ("S17", 25, "d3", "Rumah Saionji", "shiori"),
        ("S01", 1, "d1", "Taman Kampus", "shiori"),
        ("Mo02", 2, "d5", "Stasiun Kouseikan-mae", "moeka"),
        ("Mo03", 3, "d1", "Kantin Pusat", "moeka"),
        ("Mo04", 5, "d1", "Kantin Pusat", "moeka"),
        ("Mo05", 6, "d1", "Kantin Pusat", "moeka"),
        ("Mo06", 7, "d1", "Kantin Pusat", "moeka"),
        ("Mo08", 9, "d1", "Kantin Pusat", "moeka"),
        ("Mo09", 10, "d1", "Kantin Pusat", "moeka"),
        ("Mo10", 11, "d1", "Kantin Pusat", "moeka"),
        ("Mo11", 15, "d1", "Kantin Pusat", "moeka"),
        ("Mo12", 16, "d1", "Kantin Pusat", "moeka"),
        ("Mo26", 33, "d1", "Kantin Pusat", "moeka"),
        ("Mo13", 18, "d1", "Kantin Pusat", "moeka"),
        ("Mo14", 19, "d1", "Kantin Pusat", "moeka"),
        ("Mo15", 20, "d1", "Kantin Pusat", "moeka"),
        ("Mo16", 22, "d1", "Kantin Pusat", "moeka"),
        ("Mo17", 23, "d1", "Kantin Pusat", "moeka"),
        ("Mo18", 26, "d1", "Kantin Pusat", "moeka"),
        ("Mo19", 27, "d1", "Kantin Pusat", "moeka"),
        ("Mo21", 29, "d1", "Kantin Pusat", "moeka"),
        ("Mo22", 30, "d1", "Kantin Pusat", "moeka"),
        ("Mo23", 31, "d1", "Kantin Pusat", "moeka"),
        ("Mo24", 32, "d1", "Kantin Pusat", "moeka"),
        ("Mo25", 34, "d1", "Kantin Pusat", "moeka"),
        ("H04", 5, "d1", "Perpustakaan Pusat", "harumi"),
        ("H06", 7, "d1", "Perpustakaan Pusat", "harumi"),
        ("H07", 9, "d1", "Perpustakaan Pusat", "harumi"),
        ("H11", 16, "d1", "Perpustakaan Pusat", "harumi"),
        ("H12", 19, "d1", "Perpustakaan Pusat", "harumi"),
        ("H13", 20, "d1", "Perpustakaan Pusat", "harumi"),
        ("H14", 21, "d1", "Perpustakaan Pusat", "harumi"),
        ("H15", 22, "d1", "Perpustakaan Pusat", "harumi"),
        ("H16", 23, "d1", "Perpustakaan Pusat", "harumi"),
        ("H17", 25, "d1", "Perpustakaan Pusat", "harumi"),
        ("H18", 27, "d1", "Perpustakaan Pusat", "harumi"),
        ("S04", 5, "d3", "Klub Catur", "shiori"),
        ("S05", 7, "d3", "Klub Catur", "shiori"),
        ("S20", 29, "d3", "Klub Catur", "shiori"),
        ("S21", 30, "d3", "Klub Catur", "shiori"),
        ("S22", 31, "d3", "Klub Catur", "shiori"),
        ("S23", 32, "d3", "Klub Catur", "shiori"),
        ("S24", 33, "d3", "Klub Catur", "shiori"),
        ("H20", 29, "d1", "Perpustakaan Pusat", "harumi"),
        ("H21", 30, "d1", "Perpustakaan Pusat", "harumi"),
        ("H23", 34, "d1", "Perpustakaan Pusat", "harumi"),
        ("Mo07", 8, "d1", "Kantin Pusat", "moeka"),
        ("C06", 9, "d2", "Rumah Amamiya", "host"),
        ("C07", 11, "d2", "Rumah Amamiya", "host"),
        ("C10", 17, "d2", "Rumah Amamiya", "host"),
        ("C12", 21, "d2", "Rumah Amamiya", "host"),
        ("C13", 23, "d2", "Rumah Amamiya", "host"),
        ("C14", 26, "d2", "Rumah Amamiya", "host"),
        ("C15", 29, "d2", "Rumah Amamiya", "host"),
        ("C16", 31, "d1", "Gedung Seni Rupa & Studio", "host"),
        ("C17", 32, "d1", "Gedung Seni Rupa & Studio", "host"),
        ("Y03", 1, "d3", "Apartemen Yutaka", "host"),
        ("Y04", 4, "d3", "Apartemen Yutaka", "host"),
        ("Y06", 8, "d3", "Apartemen Yutaka", "host"),
        ("Y07", 9, "d3", "Apartemen Yutaka", "host"),
        ("Y08", 11, "d3", "Apartemen Yutaka", "host"),
        ("Y11", 17, "d2", "Rumah Amamiya", "host"),
        ("Y12", 20, "d2", "Rumah Amamiya", "host"),
        ("Y14", 23, "d3", "Apartemen Yutaka", "host"),
        ("Y15", 26, "d3", "Apartemen Yutaka", "host"),
        ("Y16", 29, "d2", "Rumah Amamiya", "host"),
        ("Y18", 32, "d2", "Rumah Amamiya", "host"),
        ("S02", 2, "onsen", "Lobi ryokan", "shiori"),
        ("Mi02", 2, "onsen", "Dapur ryokan", "miyuki"),
        ("N02", 2, "onsen", "Ruang bersama ryokan", "nagisa"),
        ("K02", 2, "onsen", "Taman luar ryokan", "koita"),
        ("N01", 1, "d1", "Gedung Arsitektur", "nagisa"),
        ("Mi01", 1, "d1", "Taman Kampus", "enter"),
        ("Mi07", 7, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("Mi06", 6, "d1", "Gedung Kedokteran", "miyuki"),
        ("Mi24", 30, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("Mi21", 25, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("Mi12", 13, "d1", "Gedung Kedokteran", "miyuki"),
        ("Mi13", 14, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("Mi11", 11, "d1", "Kafe Komorebi", "miyuki"),
        ("Mi09", 9, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("Mi18", 21, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("Mi25", 33, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("Mi14", 15, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("Mi15", 17, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("Mi16", 19, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("Mi17", 20, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("Mi19", 23, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("Mi20", 24, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("Mi22", 27, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("Mi23", 29, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("Mi26", 34, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("K07", 8, "d1", "Gedung Sastra", "koita"),
        ("K08", 9, "d1", "Gedung Sastra", "koita"),
        ("N11", 14, "d2", "Rumah Sakurajima", "nagisa"),
        ("N12", 15, "d1", "Gedung Arsitektur", "nagisa"),
        ("N13", 17, "d1", "Gedung Arsitektur", "nagisa"),
        ("N14", 18, "d1", "Gedung Arsitektur", "nagisa"),
        ("N15", 21, "d1", "Gedung Arsitektur", "nagisa"),
        ("N16", 23, "d1", "Gedung Arsitektur", "nagisa"),
        ("N17", 24, "d1", "Gedung Arsitektur", "nagisa"),
        ("N18", 26, "d1", "Gedung Arsitektur", "nagisa"),
        ("N21", 31, "d2", "Rumah Sakurajima", "nagisa"),
        ("N23", 34, None, None, "desk"),
        ("N22", 33, "d2", "Rumah Sakurajima", "nagisa"),
        ("C02", 1, "d2", "Rumah Amamiya", "host"),
        ("C03", 4, "d2", "Rumah Amamiya", "host"),
        ("C04", 5, "d2", "Rumah Amamiya", "host"),
        ("C08", 13, "d1", "Gedung Seni Rupa & Studio", "host"),
        ("C05", 8, "d2", "Rumah Amamiya", "host"),
        ("C11", 20, "d1", "Gedung Seni Rupa & Studio", "shiori"),
        ("C09", 16, "d2", "Rumah Amamiya", "host"),
        ("Y02", 1, "d2", "Rumah Amamiya", "host"),
        ("Y05", 5, "d3", "Apartemen Yutaka", "host"),
        ("Y10", 16, "d2", "Rumah Amamiya", "host"),
        ("Y09", 13, "d3", "Apartemen Yutaka", "host"),
        ("Y13", 21, "d2", "Rumah Amamiya", "host"),
        ("Y17", 31, "d3", "Apartemen Yutaka", "host"),
        ("N04", 5, "d7", "Tepi Sungai", "nagisa"),
        ("N05", 6, "d1", "Gedung Arsitektur", "nagisa"),
        ("N07", 9, "d2", "Rumah Sakurajima", "nagisa"),
        ("N08", 11, "d1", "Gedung Arsitektur", "nagisa"),
        ("N09", 12, "d1", "Gedung Arsitektur", "nagisa"),
        ("N10", 13, "d1", "Gedung Arsitektur", "nagisa"),
        ("K01", 1, "d1", "Gedung Sastra", "koita"),
        ("K03", 4, "d1", "Gedung Sastra", "koita"),
        ("K06", 6, "d1", "Kafe Komorebi", "koita"),
        ("K09", 10, "d7", "Kuil", "koita"),
        ("K10", 11, "d1", "Gedung Sastra", "koita"),
        ("K11", 12, "d1", "Gedung Sastra", "koita"),
        ("K12", 14, "d1", "Gedung Sastra", "koita"),
        ("K14", 18, "d1", "Kafe Komorebi", "koita"),
        ("K15", 19, "d1", "Gedung Sastra", "koita"),
        ("K16", 21, "d2", "Rumah Amamiya", "koita"),
        ("K18", 24, "d1", "Gedung Sastra", "koita"),
        ("K19", 25, "d1", "Gedung Sastra", "koita"),
        ("K23", 31, "d1", "Gedung Sastra", "koita"),
        ("K24", 32, "d1", "Gedung Sastra", "koita"),
        ("K25", 33, "d2", "Rumah Amamiya", "koita"),
        ("K04", 5, "d1", "Gedung Sastra", "koita"),
        ("K05", 5, "d2", "Rumah Amamiya", "koita"),
        ("K13", 17, "d1", "Gedung Sastra", "koita"),
        ("K17", 23, "d1", "Gedung Sastra", "koita"),
        ("K20", 26, "d2", "Rumah Amamiya", "koita"),
        ("K21", 29, "d2", "Rumah Amamiya", "koita"),
        ("K22", 29, "d1", "Gedung Sastra", "koita"),
        ("N06", 7, "d1", "Gedung Arsitektur", "nagisa"),
        ("N03", 3, "d1", "Gedung Arsitektur", "nagisa"),
        ("Mi03", 4, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("Mi04", 5, "d1", "Gedung Kedokteran", "miyuki"),
        ("Mi05", 5, "d7", "Vila (Izu)", "miyuki"),
        ("Mi08", 8, "d6", "Rumah Sakit Tachibana", "miyuki"),
        ("Mi10", 10, "d7", "Kuil", "miyuki"),
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
                    "fn": _fn_makan, "done": "Kamu menyantap makanan hangat hingga perutmu kembali tenang dan tenagamu pulih.", "fail": "Saldo tidak cukup untuk makan di sini."},
        "kerja":   {"label": "Kerja paruh waktu", "desc": "+¥3.000 · menguras energi", "ok": lambda: True,
                    "fn": _fn_kerja, "done": "Jam kerja paruh waktu selesai. Tubuhmu terasa pegal, dan ¥3.000 masuk ke saldomu.", "fail": ""},
        "belajar": {"label": "Belajar", "desc": "energi turun · nilai akademik naik", "ok": lambda: True,
                    "fn": _fn_belajar, "done": "Kamu belajar beberapa jam penuh sambil merapikan catatan. Kepalamu terasa berat, tetapi pemahamanmu bertambah.", "fail": ""},
        "santai":  {"label": "Bersantai", "desc": "energi naik · stres turun", "ok": lambda: True,
                    "fn": _fn_santai, "done": "Kamu duduk menghela napas sejenak, membiarkan waktu berjalan pelan sampai pikiranmu kembali jernih.", "fail": ""},
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
        text "Ke mana kamu pergi?" style "kk_heading"
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
                                add Solid(kk_line) xysize (10, 44) yalign .5
                                text meta["nama"] size 25 bold True yalign .5
                else:
                    text "Tidak ada orang yang kamu kenal di sini sekarang." style "kk_caption"
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
                    use kk_link("Bicarakan sketsa dengan Karuha", Return(("portfolio", None)), 800)
                if kk_can_sketch(lokasi):
                    use kk_link("Latihan di buku sketsa", Return(("draw", None)), 800)
                if kk_can_sit_with_miyuki(lokasi):
                    button:
                        id "miyuki_library_seat"
                        style "kk_button" action Return(("sit_miyuki", None))
                        text "Duduk di sebelah Miyuki" style "kk_button_text"
                if kk_unfinished_board(lokasi):
                    button:
                        id "unfinished_board"
                        style "kk_button" xysize (800, 72) action Return(("board", None))
                        text "Perhatikan papan yang belum dibereskan" style "kk_button_text" yalign .5
                if lokasi == home and kk_desk_event(lokasi):
                    use kk_link("Periksa meja di kamar", Return(("desk", None)), 800)
                if lokasi == home:
                    use kk_link("Beristirahat di kamar", Return(("sleep", None)), 800)
                if not acts and not kk_unfinished_board(lokasi) and not kk_art_studio_open(lokasi) and lokasi != home and distrik != "onsen" and not (lokasi == "Stasiun Kouseikan-mae" and kk_onsen_dates()):
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
        call kk_scene_enter(kk_host, kk_hari + " · " + str(kk_hari_n) + " " + kk_month_tuple()[1])
        call kk_play_lines(kk_weekly_lines())
        $ _mt = kk_month_tuple()
        nar "Kini memasuki [kk_hari], [kk_hari_n] [_mt[1]]."
        hide screen kk_set
        jump kk_world_loop
    $ _distrik = _r[1]
    $ kk_minutes(60)
    jump kk_loc_list

label kk_loc_list:
    if kk_graduated:
        jump kk_evaluasi
    if _distrik == "onsen" and not kk_onsen_dates():
        jump kk_trip_return
    $ kk_bgm_location(_distrik)
    call screen kk_world_location(_distrik)
    if _return == "back":
        if _distrik == "onsen":
            jump kk_trip_return
        jump kk_world_loop
    $ _lokasi = _return
    $ kk_minutes(30)
    $ kk_bgm_location(_distrik, _lokasi)
    if kk_graduated:
        jump kk_evaluasi
    # (3-4) peristiwa berkumpul yang muncul begitu kau tiba
    $ _ent = kk_pending_enter(_distrik, _lokasi)
    if _ent:
        call kk_play_scene(_ent[0])
        $ kk_advance()
    elif kk_pulau_m17b_due(_distrik, _lokasi):
        call kk_pulau_m17b
    elif kk_father_visit(_lokasi):
        call kk_visit_kisaragi
        $ kk_minutes(10)
    elif kk_host_dyn(_distrik, _lokasi):
        call kk_social_scene(kk_host_dyn(_distrik, _lokasi))
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
    $ kk_bgm_location(_distrik, _lokasi)
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
            call kk_scene_enter(kk_host, "Perjalanan menuju penginapan onsen")
            call kk_play_lines(KK_ONSEN_TRAVEL["to_onsen"])
            jump kk_loc_list
        nar "Kesempatan untuk menyusul rombongan sudah berlalu."
        jump kk_location_view_loop
    elif _c[0] == "rest":
        $ kk_advance()
        jump kk_location_view_loop
    elif _c[0] == "portfolio":
        call kk_show_portfolio
        jump kk_location_view_loop
    elif _c[0] == "sit_miyuki":
        call kk_library_rest(_lokasi)
        jump kk_location_view_loop
    elif _c[0] == "board":
        call kk_inspect_board(_lokasi)
        jump kk_location_view_loop
    elif _c[0] == "desk":
        call kk_check_desk
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
    call kk_scene_enter(kk_host, "Perjalanan pulang · Stasiun Kouseikan-mae")
    call kk_play_lines(KK_ONSEN_TRAVEL["from_onsen"])
    jump kk_location_view_loop

label kk_do_talk(distrik, lokasi, cid):
    if cid not in kk_present_here(distrik, lokasi):
        return
    $ known = cid in kk_last_met
    if kk_keep_promise(cid, lokasi):
        call kk_scene_enter(cid, KK_DISTRICT_NAME[distrik] + " · " + lokasi)
        call kk_play_lines(KK_DAILY_KEEP_PROMISE.get((cid, kk_host), [("nar", "Kamu datang sesuai janji kalian kemarin.")]))
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
        call kk_scene_enter("nagisa", KK_DISTRICT_NAME[distrik] + " · " + lokasi)
        call kk_play_lines(KK_NAGISA_HEARD_REPLY[kk_host])
        $ kk_flag("heard_reply")
    else:
        call kk_generic_talk(cid, KK_DISTRICT_NAME[distrik] + " · " + lokasi, known)
        return
    $ kk_advance()
    return

# Obrolan ringan tanpa event: pertemuan harian utuh dengan cerita mini per karakter & host.
# Sekadar hadir & bicara menumbuhkan kedekatan sedikit, diam-diam.
label kk_generic_talk(cid, loc, known=True):
    $ _name = KK_CHARS[cid]["nama"]
    $ _key = "ngobrol_%s_%d_%d_%d" % (cid, kk_bulan, kk_hari_n, kk_slot)
    $ fresh = not kk_has(_key)
    $ kk_flag(_key)
    call kk_scene_enter(cid, loc)
    $ _loc_desc = KK_LOC_DESC.get(_lokasi)
    $ _slot_desc = KK_SLOT_MOOD.get(kk_slot, "")
    if _loc_desc and _slot_desc:
        nar "[_loc_desc] [_slot_desc]"
    elif _loc_desc:
        nar "[_loc_desc]"
    $ _after = kk_afterglow(cid)
    if _after:
        $ renpy.say(getattr(store, cid), _after)
        $ _ag_rep = KK_DAILY_AFTERGLOW_REPLY.get((cid, kk_host))
        if _ag_rep:
            $ renpy.say(getattr(store, _ag_rep[0]), _ag_rep[1])
    elif not known and (cid, kk_host) in KK_DAILY_OPEN_FIRST:
        call kk_play_lines(KK_DAILY_OPEN_FIRST[(cid, kk_host)])
    elif (cid, kk_host) in KK_DAILY_OPEN:
        call kk_play_lines(kk_daily_pick(cid, KK_DAILY_OPEN[(cid, kk_host)]))
    else:
        $ renpy.say(getattr(store, cid), "Kebetulan sekali bertemu di sini. Kamu lagi senggang?")
    menu:
        "Buka kembali soal yang kalian baca bersama." if cid == "harumi" and any(c["ev"] == "H01" and c["key"] == "A" for c in choices_log):
            call kk_play_lines(KK_DAILY_H01[kk_host])
            if fresh:
                $ kk_rel("harumi", "trust", 1)
            $ kk_minutes(10)
        "Tanyakan bagaimana harinya." if known:
            if (cid, kk_host) in KK_DAILY_CHAT:
                call kk_play_lines(kk_daily_chat_lines(cid, kk_host))
            else:
                nar "Kalian duduk sebentar bertukar kabar tentang kegiatan kuliah masing-masing."
            if fresh:
                $ kk_rel(cid, "trust", 1)
            $ kk_minutes(10)
        "Janjikan bertemu lagi di sini besok pada waktu yang sama." if fresh and cid not in kk_promises:
            $ kk_make_promise(cid, _lokasi)
            $ kk_minutes(1)
            if (cid, kk_host) in KK_DAILY_PROMISE:
                call kk_play_lines(KK_DAILY_PROMISE[(cid, kk_host)])
            else:
                nar "Kalian sepakat untuk bertemu lagi di tempat ini besok pada waktu yang sama."
        "Balas sapaannya lalu pamit.":
            if (cid, kk_host) in KK_DAILY_BYE:
                call kk_play_lines(KK_DAILY_BYE[(cid, kk_host)])
            else:
                nar "Kamu membalas sapaannya singkat lalu berpamitan melanjutkan langkahmu."
            if fresh:
                $ kk_rel(cid, "aff", 2)
            $ kk_minutes(5)
        "Bawakan makanan untuk Miyuki." if cid == "miyuki" and saldo >= 800:
            $ kk_post_money(-800, "Makanan untuk Miyuki")
            call kk_play_lines(KK_DAILY_MIYUKI_FOOD[kk_host])
            if fresh:
                $ kk_adj("dimanja_miyuki",4)
                $ kk_adj("kelelahan_miyuki",-8)
            $ kk_minutes(60)
        "Puji pastry yang ia bawa." if cid == "miyuki" and _lokasi == "Kafe Komorebi" and kk_hari == "Sabtu":
            $ kk_flag("puji_pastry")
            call kk_play_lines(KK_DAILY_MIYUKI_PASTRY[kk_host])
            if fresh:
                $ kk_rel(cid,"aff",2)
            $ kk_minutes(2)
    return

label kk_do_activity(lokasi, actid):
    $ a = KK_ACTS[actid]
    if actid not in KK_ACT_BY_LOC.get(lokasi, []) or not a["ok"]():
        nar "[a['fail']]"
        return
    call kk_scene_enter(kk_host, lokasi)
    $ a["fn"]()
    $ kk_advance(1)   # (2) aktivitas memakan waktu
    call kk_play_lines(kk_act_lines(actid, lokasi))
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
        "Rumah Amamiya": "Rumah tempatmu tinggal sekarang, lengkap dengan kehangatan keluarga yang masih terasa asing.",
        "Klub Catur": "Jam dinding berdetak. Papan-papan tertata rapi menunggu lawan.",
    }
