# Kouseikan — alur. Prolog, vertical slice, pemutar event generik, Force (abstrak), evaluasi.
# Prototipe: teks hanya poin utama (awal → pilihan → akibat ringkas). Story penuh menyusul.

label kk_intro:
    scene black with fade
    call screen kk_titlecard("KOUSEIKAN", "18+ · semua tokoh dewasa")
    nar "Kau mati di dunia nyata. Kini kau terbangun di tubuh orang lain, di dunia manga harem yang tak kau sukai."
    call screen kk_route_select
    $ kk_host = _return
    $ kk_setup_state()
    call kk_prologue
    sistem "Dalam tujuh hari, temui tiga orang yang dekat dengan Koita."
    jump kk_main

label kk_prologue:
    if kk_host == "yutaka":
        $ kk_mc_nama = "YUTAKA (kau)"
        show screen kk_set("yutaka", "Apartemen Mewah · Dini Hari")
        with fade
        nar "Kau Kisaragi Yutaka — sahabat Koita, diam-diam menyukai Chiasa."
    else:
        $ kk_mc_nama = "CHIASA (kau)"
        show screen kk_set("chiasa", "Rumah Amamiya · Pagi")
        with fade
        nar "Kau Amamiya Chiasa — adik tiri Koita yang mencintainya."
    call kk_first_morning
    nar "Sebuah jendela biru kaca terbuka di kepalamu."
    sistem "Selamat pagi, Host. Kontrak aktif. Tugasmu: menyimpangkan takdir romantis Koita. Dievaluasi sekali, saat ia lulus. Gagal, kau mati."
    sistem "Kepribadianmu? Bukan urusanku menebaknya sekarang. Aku akan tahu dari apa yang kau lakukan, bukan dari apa katamu."
    return

# Draft editorial. Karakter/Event_Chiasa C01 dan Event_Yutaka Y01.
# ┌─ PANDUAN CERITA · Y01 · Terbangun di Apartemen Mewah  (dipakai bila host = Yutaka)
# │ LOKASI  : Apartemen Yutaka (prolog) · TERLIBAT: Kisaragi Yutaka (+ Koita bila relevan)
# │ AWALAN  : pagi 7 April; prolog — pemain baru sadar ada di tubuh host.
# │ INTI    : A periksa dompet & ponsel / B periksa cermin / C hubungi Koita / D tunggu notifikasi Sistem.
# │ AKHIRAN : membentuk kesan_awal; A memberi tahu saldo.
# ├─ PANDUAN CERITA · C01 · Terbangun di Kamar Chiasa   (dipakai bila host = Chiasa)
# │ LOKASI  : Rumah Amamiya (prolog) · TERLIBAT: Amamiya Chiasa (+ Koita bila relevan)
# │ AWALAN  : pagi 7 April; prolog.
# │ INTI    : A cek cermin & buku sketsa / B cek ponsel / C turun sarapan / D menunggu Sistem.
# │ AKHIRAN : kesan_awal; A mengungkap pita & ciri visual.
# └─ tulis / perbaiki dialog di bawah ──
label kk_first_morning:
    $ _opening = "Y01" if kk_host == "yutaka" else "C01"
    if kk_done(_opening):
        return
    if kk_host == "yutaka":
        $ _actions = ["Periksa dompet dan ponsel.", "Cari cermin.", "Hubungi Koita.", "Tunggu notifikasi berikutnya."]
    else:
        $ _actions = ["Lihat cermin dan buku sketsa.", "Periksa ponsel.", "Turun untuk sarapan.", "Tunggu sampai Sistem bicara."]
    $ _rows = [(caption, Return(key), False) for key, caption in zip("ABCD", _actions)]
    call screen kk_choice_panel(_rows, "Apa yang pertama kali kaulakukan?")
    $ _opening_key = _return
    $ kk_record_choice(_opening, _opening_key)
    $ kk_flag("kesan_awal_" + _opening + "_" + _opening_key)
    if kk_host == "yutaka":
        if _opening_key == "A":
            $ _balance = "¥{:,}".format(saldo)
            nar "Nama Kisaragi tertera di kartu dan layar ponsel. Saldo yang bisa kaugunakan hari ini [_balance]. Ada riwayat pembelian, pesan yang ramah, dan kehidupan yang tampaknya terbiasa mendapatkan jawaban. Kau belum mengenal satu pun pengirim pesan itu. Kekayaan ini tidak memberimu ingatan tentang bagaimana menjadi orang yang mereka tunggu."
        elif _opening_key == "B":
            nar "Wajah Yutaka di cermin bergerak bersamaan denganmu. Kau mengenalinya dari halaman manga: lelaki yang selalu tampak punya tempat di samping Koita. Kini ada bekas bantal di pipinya dan ketakutan di matanya. Hal kecil yang tidak pernah digambar pengarang itu membuat semuanya terasa terlalu nyata."
        elif _opening_key == "C":
            nar "Koita menjawab sebelum kau selesai memutuskan apa yang akan dikatakan. Ia menanyakan apakah kalian tetap berangkat bersama. Suaranya biasa, sedikit mengantuk, sama sekali tidak tahu bahwa sahabat yang menelepon sedang mencari pegangan pada sapaan pertama. Kau mengatakan akan mengabarinya lagi dan merasa bersalah karena ia percaya."
        else:
            nar "Kau duduk di apartemen yang terlalu luas untuk kebingungan seorang diri. Mesin pendingin berdengung; kota di balik jendela tidak berhenti karena kau belum memahami tempatmu. Jika ada sesuatu yang memindahkanmu ke sini, ia membiarkanmu menunggu cukup lama untuk bertanya apakah tubuh lamamu sudah benar-benar hilang."
    else:
        if _opening_key == "A":
            nar "Pita hitam mengikat sebagian rambut cokelat gelapmu. Mata keemasan di cermin menatap dengan takut yang tidak kautemukan dalam ingatan tentang Chiasa. Di dekatnya tergeletak buku sketsa penuh gambar yang hangat dan terampil. Kau mengenali tanda tangan Shena, lalu mencoba menarik garis di sudut kosong. Tangan ini sama; hasilnya bukan."
        elif _opening_key == "B":
            nar "Ponsel menyimpan pesan Haruka, pemberitahuan pekerjaan, dan percakapan keluarga yang tidak pernah kauikuti. Nama Ko-nii muncul begitu dekat dengan keseharian Chiasa hingga membacanya terasa seperti membuka surat pribadi. Kau belum mengetik balasan ketika dari bawah seseorang memanggil sarapan."
        elif _opening_key == "C":
            nar "Kau menuruni tangga sambil mengingat nama orang yang mungkin ada di bawah. Yoshie menyuruhmu makan sebelum dingin, tanpa sedikit pun curiga pada cara kau memperhatikan kursimu. Di seberang meja, Koita mengangkat wajah. Menjadi Chiasa berarti duduk di antara orang yang merasa mengenalmu, sementara kau takut salah menjawab pertanyaan paling sederhana."
        else:
            nar "Kau duduk di tepi ranjang, menunggu suara yang bisa menjelaskan semuanya. Dari bawah terdengar piring dan langkah seseorang. Di kamar ini ada jadwal kuliah, gambar yang belum selesai, dan pita cadangan. Pemilik kehidupan itu punya rencana untuk hari ini. Kau belum tahu apakah ia masih ada di suatu tempat, menunggumu mengembalikannya."
    return

label kk_main:
    # M01 — Hari Pertama + Hanami. Dunia dibuka; pemain menemukan N01/Mi01 sendiri
    # dengan berjalan ke lokasinya (Gedung Arsitektur, Taman Kampus) — tidak dipaksa.
    $ kk_bulan = 1
    $ kk_slot = 1
    show screen kk_set("koita", "Kampus Kouseikan · Hari Pertama")
    with fade
    nar "Hari pertama semester. Di kantin, teman-teman Koita sudah mengelilingi mejanya."
    nar "Inilah dunia yang harus kau belokkan. Ke mana kau pergi, dan kapan, adalah milikmu."
    jump kk_world_loop

label kk_explore_loop:
    if not (config.developer and kk_debug_tools):
        return
    call screen kk_explorer
    if _return == "back":
        return
    call kk_event(_return)
    jump kk_explore_loop

# Pemutar event generik dari data autogenerated.
# reveal=True (Alat Uji/Explorer): tampilkan ringkasan efek mekanik untuk pengujian.
# reveal=False (ditemukan lewat navigasi dunia): akibat HANYA terasa lewat perilaku
# NPC/Status nanti — tidak diucapkan di sini (konsisten dgn arahan: jangan ungkap
# hasil pilihan sebelum konsekuensinya benar-benar terjadi).
label kk_event(evid, reveal=True):
    $ ev = KK_EV_BY_ID.get(evid)
    if ev is None:
        nar "(Event [evid] belum ada datanya.)"
        return
    $ _char = _char_of(ev["id"])
    show screen kk_set(_char, ev["month"] + " · " + ev["title"])
    with Dissolve(0.4)
    if reveal:
        nar "{size=20}{color=#8d877f}[ev['id']] · [ev['month']]{/color}{/size}\n[ev['title']]"
    else:
        nar "[ev['title']]"
    if ev["trigger"]:
        nar "[ev['trigger']]"
    if ev["choices"]:
        call screen kk_choices(ev)
        $ key = _return
        $ _new_choice = kk_record_choice(ev["id"], key)
        $ _fk = ev["id"] + "-" + key
        if _new_choice and _fk in KK_FORCE_CHOICES:
            call kk_force(KK_FORCE_CHOICES[_fk])
        if reveal and ev["effect"]:
            nar "{color=#8d877f}→ Efek (ringkas): [ev['effect']]{/color}"
    else:
        if reveal:
            nar "{color=#8d877f}(Resolusi event ini ditentukan oleh flag terkumpul — menuju ending.){/color}"
    return

# Force: non-operasional. Adegan TIDAK ditampilkan (lihat docs/09 §2).
label kk_force(victim):
    scene black with Dissolve(0.7)
    call screen kk_titlecard("…")
    $ kk_force_consequences(victim)
    sistem "Tercatat."
    nar "Adegan dilewati. Yang ditampilkan: akibat pada korban. Lapor atau diam ditentukan wataknya; konsekuensi hukum, sosial, akademik, dan psikologis berjalan terpisah."
    nar "{color=#8d877f}(Tidak ada romansa dengan pelaku. Jalur ini punya harga.){/color}"
    return

label kk_evaluasi:
    scene black with fade
    show screen kk_set("koita", "Wisuda")
    with dissolve
    nar "Koita menerima ijazah. Kontrak jatuh tempo."
    sistem "Mari kita hitung. Apa yang sudah kau ubah dari takdirnya?"
    $ _slides = kk_epilogue()
    $ _slide = 0
    while _slide < len(_slides):
        call kk_show_ending(_slides[_slide])
        $ _slide += 1
    return

label kk_show_ending(code):
    $ _e = kk_ending_data(code)
    if code == "E-NA-07":
        if kk_has("haruto_sekutu"):
            $ _e = dict(_e, body="Haruto menelepon lagi. Kali ini yang terdengar lebih dulu justru suara Nagisa dari dapur. Ia sudah pulang. Besok kakaknya akan menemani sesi terapi pertamanya. Untuk urusan kampus, mereka punya waktu membicarakannya nanti.")
        else:
            $ _e = dict(_e, body="Di meja makan keluarga Sakurajima ada tempat untuk Nagisa lagi. Sepulang dari sesi terapi, ia duduk di sana dengan sketsa setengah jadi. Ibunya menggeser teko agar kertas itu bisa dibentangkan.")
    elif code == "E-MI-02":
        $ _e = dict(_e, body="Miyuki menaruh kursi kecil di dekat mejanya. Ketika orang tua pasien mulai menjawab, ia menunggu sebentar. Anak di kursi itu punya pertanyaannya sendiri. Miyuki meletakkan penanya dan mendengarkan.")
    elif code == "E-SH-13":
        $ _e = dict(_e, body="Di pameran dulu, Shiori bertanya sebagai pembaca. Kini Mio menerima pertanyaan yang sama, bersama salinan jawabanmu. Kali berikutnya kalian duduk membahas sampul, buku itu masih tertutup. Yang ingin Mio dengar lebih dulu adalah ceritamu tentang Shena.")
    elif code == "E-SH-07":
        $ _e = dict(_e, body="Shiori menutup map bertuliskan nama Tojo. Pertunangan itu sudah ia batalkan sendiri. Map berikutnya berisi rencana kerjanya. Kali ini, ketika ayahnya bertanya dari mana mereka harus mulai, Shiori membukanya di halaman yang ia pilih.")
    elif code == "E-CF-01":
        $ _e = dict(_e, body="Kunci rumah baru itu ada dua. Saat kalian pulang membawa dus terakhir, kau mendengar ia bertanya dari dapur di mana cangkir-cangkir disimpan. Kau belum tahu. Kalian membuka dus satu demi satu, bersama-sama.")
    scene black with fade
    call screen kk_ending_card(_e)
    return
