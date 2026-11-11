# Kouseikan — state model. Semua angka tersembunyi dari pemain (✅ 6C.4).
# Prototipe: struktur penuh, nilai awal dari dokumen desain.

default kk_host = ""              # "yutaka" (Male) / "chiasa" (Female)

# kesan_awal (✅ GDD 6Q.2): kepribadian TIDAK dipilih di menu — ia terbentuk dari
# pilihan dan tindakan nyata sepanjang main. Ini cuma penghitung kecenderungan,
# dibaca pasif di Status, tidak pernah ditanyakan ke pemain.
default kk_persona = {"ramah":0, "dingin":0, "genit":0, "agresif":0, "manipulatif":0}

# Waktu
default kk_bulan = 1             # 1..36 (M01..M36)
default kk_slot = 0             # index ke KK_SLOTS
default kk_hari = "Senin"
default kk_hari_n = 1           # hari ke-berapa dalam bulan (overflow slot)
default _present_cache = None   # cache kehadiran NPC per-waktu (stabil lintas redraw)

# Sumber daya tubuh host (lihat Sistem_Waktu_Bebas_dan_Kondisi_Fisik.md)
default body = {}
# Hubungan 5 dimensi per karakter: {"koita": {"aff":..,"trust":..,"intim":..,"jeal":..,"fear":..}}
default rel = {}
# Poin kondisi karakter & dunia (kelelahan, stres, kecurigaan, dll) — generik by name
default pts = {}
# Tahap rute: {"miyuki":0,...}
default stage = {}
# Flag (himpunan nama)
default flags = []
# Log pilihan untuk resolver ending
default choices_log = []

# Variabel Sistem & global
default saldo = 0
default deviasi = 0
default orbit_koita = 5
default runtuh_koita = 0
default trust_koita = 60
default koita_sadar = 0
default sikap_sistem = {"patuh":0,"bangkang":0,"tipu":0,"selidik":0}
default peringatan_1 = False
default peringatan_final = False
default koita_bebas_naskah = False

# Konstanta
define KK_SLOTS = ["PAGI", "SIANG", "SORE", "MALAM", "LARUT", "DINI HARI"]

# Tulang punggung 36 bulan (ringkas dari Milestone_3_Tahun.md)
init -5 python:
    KK_BACKBONE = [
        ("M01","Apr T1","Hari Pertama + Hanami","Kontrak"),
        ("M02","Mei","Golden Week: Onsen","Kontrak"),
        ("M03","Jun","Tsuyu: Hujan Bersama","Kontrak"),
        ("M04","Jul","Tanabata + Ujian 1","Kontrak"),
        ("M05","Agu","Natsu Matsuri + Vila Pantai","Kontrak"),
        ("M06","Sep","Tsukimi + Reuni","Kontrak"),
        ("M07","Okt","Pesaing Muncul","Kontrak"),
        ("M08","Nov","Momiji + Festival Klub","Kontrak"),
        ("M09","Des","Malam Natal","Kontrak"),
        ("M10","Jan","Hatsumode + Ujian 2","Kontrak"),
        ("M11","Feb","Festival Dingin + Valentine","Kontrak"),
        ("M12","Mar","White Day + Audit 1","Kontrak"),
        ("M13","Apr T2","Adik Tingkat Baru","Retak"),
        ("M14","Mei","Golden Week: Kansai","Retak"),
        ("M15","Jun","Tsuyu: Hujan Deras","Retak"),
        ("M16","Jul","Tanabata 2 + Ujian","Retak"),
        ("M17","Agu","Natsu Matsuri 2 + Pulau","Retak"),
        ("M18","Sep","Tsukimi: Sidang Rumor","Retak"),
        ("M19","Okt","Koita Menyadari","Retak"),
        ("M20","Nov","Festival Seni + Pameran","Retak"),
        ("M21","Des","Natal Kedua","Retak"),
        ("M22","Jan","Hatsumode 2 + Ujian","Retak"),
        ("M23","Feb","Pengakuan Bentrok","Retak"),
        ("M24","Mar","White Day + Audit 2","Retak"),
        ("M25","Apr T3","Skripsi + Shukatsu","Tagihan"),
        ("M26","Mei","Perjalanan Perpisahan","Tagihan"),
        ("M27","Jun","Tsuyu Terakhir","Tagihan"),
        ("M28","Jul","Tanabata 3 + Ujian","Tagihan"),
        ("M29","Agu","Gasshuku Terakhir","Tagihan"),
        ("M30","Sep","Tsukimi: Pengumuman","Tagihan"),
        ("M31","Okt","Pilihan Karier","Tagihan"),
        ("M32","Nov","Festival Akhir + Pameran Tunggal","Tagihan"),
        ("M33","Des","Natal Terakhir + Peringatan Final","Tagihan"),
        ("M34","Jan","Malam Tanpa Balasan + Ujian","Tagihan"),
        ("M35","Feb","Festival Dingin Terakhir","Tagihan"),
        ("M36","Mar","White Day, Wisuda, Evaluasi","Tagihan"),
    ]

    # Heroine & karakter inti (id, nama tampil, fakultas singkat, warna aksen rute)
    # tag = fakultas/identitas netral (BUKAN nama rute — jangan membocorkan arah cerita).
    KK_CHARS = {
        "koita":  {"nama":"Amamiya Koita",    "tag":"Sastra & Humaniora",  "warna":"#6366f1"},
        "miyuki": {"nama":"Tachibana Miyuki",  "tag":"Kedokteran",          "warna":"#c0607a"},
        "nagisa": {"nama":"Sakurajima Nagisa", "tag":"Arsitektur",          "warna":"#d9a441"},
        "harumi": {"nama":"Kujo Harumi",       "tag":"Sains",               "warna":"#4aa3a0"},
        "moeka":  {"nama":"Kohinata Moeka",     "tag":"Seni Rupa & Desain",  "warna":"#5a8fd0"},
        "shiori": {"nama":"Saionji Shiori",    "tag":"Ekonomi & Bisnis",    "warna":"#9c7bd0"},
        "chiasa": {"nama":"Amamiya Chiasa",    "tag":"Seni Rupa",           "warna":"#d9a441"},
        "yutaka": {"nama":"Kisaragi Yutaka",   "tag":"Ekonomi & Bisnis",    "warna":"#4a7bf0"},
    }
