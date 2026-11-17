# Hari-hari kecil Miyuki: puding larut malam (Mi-D01) dan pastry bernama (Mi-D03).
# Efek mengikuti Alur_Cabang/01 baris Mi-D01 dan Mi-D03; kalimat adalah draf editorial.
# Besar kenaikan cemburu Nagisa (+5) adalah setelan prototipe.
init 1 python:
    KK_AFTERGLOW = (
        ("pudding_ditemani", "miyuki", "Soal puding malam itu. Terima kasih sudah duduk menemaniku. Aku tidak biasa meminta, dan ternyata tidak seburuk yang kukira."),
        ("pudding_diantar", "miyuki", "Pudingnya sampai dengan baik. Terima kasih sudah repot, walau hanya sebentar."),
        ("pudding_ditolak", "miyuki", "Soal puding itu, tidak apa-apa. Aku memang tidak seharusnya meminta selarut itu."),
        ("pudding_ditertawakan", "miyuki", "Aku masih ingat balasanmu malam itu. Lain kali aku akan berpikir dua kali sebelum meminta apa pun."),
        ("telepon_diabaikan", "miyuki", "Kau pasti mendengar telepon Ibu malam itu. Terima kasih sudah tidak membahasnya, walau aku tahu kau mendengarnya."),
        ("telepon_ditanya", "miyuki", "Terima kasih sudah bertanya setelah telepon itu, bukan saat Ibu masih bicara. Aku sedang mencari kata-katanya."),
        ("kenal_sayuri", "miyuki", "Ibu bilang kau sopan sekali di telepon. Sejak itu beliau agak lebih tenang soal aku. Sedikit saja."),
        ("koita_mencatat_pastry", "koita", "Pastry dengan namamu kemarin. Aku cuma memperhatikan. Miyuki kelihatannya bersungguh-sungguh."),
        ("nagisa_lihat_pastry", "nagisa", "Pastry itu ada namamu, kan? Aku cuma kebetulan lewat. Jangan salah paham."),
    )

    def kk_afterglow(cid):
        # Satu kalimat tindak lanjut per pilihan, muncul sekali pada obrolan berikutnya.
        for flag, who, line in KK_AFTERGLOW:
            if who == cid and kk_has(flag) and not kk_has("sudah_" + flag):
                kk_flag("sudah_" + flag)
                return line
        return None

    def kk_pastry_witnessed(key, place):
        # Nagisa hanya cemburu bila ia memang berada di tempat yang sama dan pastry itu terlihat.
        if key not in ("A", "C") or kk_daily_place("nagisa") != place:
            return False
        kk_rel("nagisa", "jeal", 5)
        kk_flag("nagisa_lihat_pastry")
        return True

    _hook("Mi-D01-A", lambda: (kk_adj("dimanja_miyuki", 10), kk_flag("pudding_ditemani")))
    _hook("Mi-D01-B", lambda: (kk_adj("dimanja_miyuki", 5), kk_flag("pudding_diantar")))
    _hook("Mi-D01-C", lambda: (kk_adj("dimanja_miyuki", -5), kk_flag("pudding_ditolak")))
    _hook("Mi-D01-D", lambda: (kk_adj("dimanja_miyuki", -10), kk_flag("pudding_ditertawakan"), kk_adj("luka_miyuki_pemain",5)))
    _hook("Mi-D03-A", lambda: kk_flag("koita_mencatat_pastry"))
    _hook("Mi-D03-B", lambda: kk_flag("pastry_disembunyikan"))
    _hook("Mi-D03-C", lambda: kk_flag("pastry_dibagikan"))

    # Mi-D04: nilai omiai mengikuti arah yang tertulis; angkanya adalah setelan prototipe.
    _hook("Mi-D04-A", lambda: (kk_adj("omiai_takeru", 3), kk_flag("telepon_diabaikan")))
    _hook("Mi-D04-B", lambda: (kk_rel("miyuki","trust", 5), kk_flag("telepon_ditanya")))
    _hook("Mi-D04-C", lambda: (kk_adj("omiai_takeru", -10), kk_rel("miyuki","trust", 3), kk_flag("kenal_sayuri")))

# ┌─ PANDUAN CERITA · Mi-D04 · Telepon Ibu yang Terdengar
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Tachibana Miyuki
# │ AWALAN  : pemain bersamanya Sabtu malam; omiai_takeru ≥ 40
# │ INTI    : A Pura-pura tidak dengar / B tanya setelahnya / C minta bicara dengan ibunya
# │ AKHIRAN : omiai_takeru ±; Trust; bicara dengan ibunya membuka hubungan pemain dengan keluarga Tachibana
# └─ tulis / perbaiki dialog di bawah ──
label kk_overheard_call:
    nar "Ponsel Miyuki berbunyi di meja saat kalian selesai makan. Ia menyentuh tombol yang salah, dan suara ibunya terdengar jelas sebelum ia sempat mematikan pengeras."
    "Ibu Miyuki" "Hayase akan datang Sabtu depan. Jangan buat jadwal lain. Kami sudah menyesuaikan semuanya."
    miyuki "Bu, aku belum bilang bisa. Jadwal rumah sakit—"
    nar "Ia berhenti ketika suara di seberang kembali berbicara. Punggungnya menegang, tangannya merapikan sendok yang sudah lurus."
    $ _rows = [(caption, Return(key), False) for key, caption in zip("ABC", KK_DYN_BY_ID["Mi-D04"]["choices"])]
    call screen kk_choice_panel(_rows, "Apa yang kau lakukan?")
    $ _key = _return
    $ kk_record_choice("Mi-D04", _key)
    if _key == "A":
        nar "Kau memandangi cangkir, memberi kesan bahwa tidak ada yang terdengar. Miyuki mengucapkan iya pada tanggal yang akhirnya ditetapkan."
        miyuki "Maaf, telepon keluarga. Tehnya masih hangat?"
        nar "Ia melanjutkan malam seolah percakapan itu hanya urusan kecil. Di kalendernya, Sabtu depan kini sudah dimiliki orang lain."
    elif _key == "B":
        nar "Kau menunggu sampai panggilan selesai sebelum bertanya. Miyuki menaruh ponsel jauh dari tangannya, seperti benda itu masih bisa menyela."
        miyuki "Takeru. Orang yang dipilih Ibu. Bukan aku. Aku bahkan belum diminta menjawab dengan sungguh-sungguh."
        nar "Ia menyebutnya untuk pertama kali tanpa tersenyum agar terdengar tidak terlalu serius. Malam itu ia tidak memerlukan kau menyelesaikannya, hanya tidak menganggap semuanya sudah disetujui."
    else:
        nar "Kau meminta izin Miyuki untuk berbicara kepada ibunya. Ia mengangguk setelah ragu, lalu memperkenalkanmu sebelum menyerahkan ponsel."
        "Ibu Miyuki" "Jadi kau temannya. Saya belum tahu ada tamu malam ini."
        nar "Kau memperkenalkan diri dan mengingatkan bahwa jadwal Miyuki perlu dibicarakan dengannya. Kesopanan di seberang menjadi lebih dingin, tetapi kini kau bukan lagi nama yang bisa dianggap tidak ada."
        miyuki "Aku takut tadi. Tapi terima kasih sudah menunggu aku mengizinkan. Aku ingin tetap ikut menentukan apa yang dikatakan."
    return

# ┌─ PANDUAN CERITA · Mi11 · Kue untuk Semua
# │ LOKASI  : Kampus Kouseikan · Kafe Komorebi
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : ia membuat terlalu banyak.
# │ INTI    : A makan bersama / B bantu bagikan / C minta khusus.
# │ AKHIRAN : gerbang cinta pemain.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi11:
    call kk_scene_enter("miyuki","Kafe Komorebi")
    nar "Kotak kue ketiga membuat meja Komorebi nyaris tak punya tempat untuk minuman. Miyuki menyebutnya salah hitung, tetapi semua porsinya rapi, seolah sejak awal ia sudah membayangkan akan ada banyak orang yang memerlukan dirinya."
    miyuki "Tinggal satu loyang. Kalau kubawa pulang, Sena pasti tanya aku sebenarnya membuat untuk berapa orang. Aku juga belum punya jawaban yang bagus."
    nar "Ia mengambil pisau lagi sebelum sempat mencicipi satu potong."
    call kk_family_menu("Mi11", ["Tarik kursi dan makan bersamanya.", "Bantu bagikan kue selagi masih hangat.", "Minta satu kue khusus untukmu."])
    if _return == "A":
        nar "Kau menarik kursi dan menyiapkan piring untuknya juga. Miyuki semula memilih potongan paling rapi untukmu, lalu berhenti ketika kau menanyakan yang ia inginkan sendiri."
        miyuki "Pinggirnya. Yang agak kecokelatan. Biasanya bagian itu kusimpan terakhir."
        nar "Kalian makan sebelum ia beranjak membagikan yang lain. Ia menilai hasilnya dengan gembira kecil yang sempat hilang di antara kesibukan melayani."
    elif _return == "B":
        nar "Kau membantu menawarkan kue ke meja yang bersedia menerima. Tidak semua orang mau; kau mengatakan tidak apa-apa tanpa meminta Miyuki membuat rasa lain."
        miyuki "Aku selalu mengira kalau ada yang menolak, berarti aku harus membetulkan sesuatu."
        nar "Ia akhirnya duduk dan makan bagiannya. Menolak satu potong kue ternyata tidak harus berarti menolak orang yang membuatnya."
    else:
        nar "Kau meminta satu yang ia pilih khusus untukmu. Miyuki menahan senyum, berpura-pura memeriksa seluruh loyang dengan sangat serius."
        miyuki "Kalau khusus, ada syarat. Makan denganku. Jangan cuma dibawa pergi lalu bilang enak lewat pesan."
        nar "Ia mengambil potongan yang lapisannya paling utuh dan satu lagi untuk dirinya. Kali ini ia berani meminta bagian kecil dari waktumu sebagai keinginan, bukan menyamarkannya sebagai pelayanan."
    return

# ┌─ PANDUAN CERITA · Mi-D12 · Ia Memilih Dirinya
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Tachibana Miyuki
# │ AWALAN  : dimanja ≥ 70; semua luka < 30; Trust ≥ 70
# │ INTI    : A Dukung / B goda / C bilang itu berkat pemain
# │ AKHIRAN : omiai_takeru −30; E-MI-01 dan E-MI-02 menguat
# └─ tulis / perbaiki dialog di bawah ──
label kk_miyuki_refuses:
    nar "Miyuki memperlihatkan kalender. Satu Sabtu yang biasanya sudah penuh coretan keluarga kini kosong, bukan karena ia lupa menuliskan sesuatu."
    miyuki "Ibu menelepon soal Hayase. Aku bilang tidak mau bertemu untuk omiai lagi. Bukan karena sibuk. Aku sengaja tidak memakai jadwal sebagai alasan."
    nar "Ia masih menggenggam ponsel, ibu jarinya mengusap bagian samping yang sama berulang kali."
    miyuki "Ibu diam lama. Aku hampir bilang mungkin bulan depan. Tapi aku menunggu sampai beliau menjawab."
    call kk_family_menu("Mi-D12", ["Dukung keputusan Miyuki.", "Goda dia soal berani membantah ibunya.", "Katakan kau yang membuatnya berani."])
    if _return == "A":
        nar "Kau mendukung keputusan itu dan menanyakan apa yang ia perlukan sekarang. Miyuki berpikir, lalu meminta minum dan waktu untuk tidak membicarakan Hayase."
        miyuki "Kalau Ibu bertanya lagi, aku mau menjawab sendiri. Tapi hari ini aku ingin merasakan bahwa Sabtu itu boleh kosong."
        nar "Ia meletakkan ponsel. Sesudah beberapa menit tangannya berhenti mencari benda tersebut setiap kali ada suara."
    elif _return == "B":
        nar "Kau menggoda keberaniannya membantah keluarga. Miyuki sempat tertawa, lalu mengangkat tangan agar kau melihat getarnya."
        miyuki "Aku memang gemetar. Ini bukan karena mendadak jadi orang berani. Aku cuma tetap bilang tidak meskipun takut."
        nar "Ia menunggu sampai kau mendengarnya dengan serius sebelum ikut tertawa lagi."
    else:
        nar "Kau menyebut keberanian itu sebagai hasil pengaruhmu. Miyuki memandangmu sebentar, kali ini tidak buru-buru membalas dengan terima kasih."
        miyuki "Kamu sudah membantuku. Aku nggak menyangkal. Tapi tadi aku yang bicara. Aku ingin boleh menyimpan bagian itu sebagai milikku."
        nar "Kalimatnya lembut, tetapi tidak ditarik kembali ketika suasana menjadi canggung."
    return

init 1 python:
    def kk_miyuki_ready_to_refuse():
        return (kk_get("dimanja_miyuki",10) >= 70 and kk_rel_get("miyuki","trust") >= 70
                and kk_get("luka_miyuki_pemain",0) < 30 and kk_get("luka_miyuki_koita",10) < 30
                and kk_get("luka_miyuki_diri",15) < 30)

    _hook("Mi11-A",lambda: kk_adj("dimanja_miyuki",5))
    _hook("Mi11-B",lambda: kk_adj("dimanja_miyuki",5))
    _hook("Mi11-C",lambda: kk_rel("miyuki","intim",2))
    for response in "ABC":
        _hook("Mi-D12-" + response,lambda: kk_adj("omiai_takeru",-30))

# ┌─ PANDUAN CERITA · Mi12 · Tahun Keempat
# │ LOKASI  : Kampus Kouseikan · Gedung Kedokteran
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : klinik dimulai.
# │ INTI    : A bantu belajar / B ganggu / C jarak.
# │ AKHIRAN : stage 2 dimulai.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi12:
    call kk_scene_enter("miyuki","Gedung Kedokteran")
    nar "Miyuki menempelkan jadwal klinik pada halaman depan catatan. Tulisan kecil memenuhi ruang yang dahulu cukup untuk satu minggu kuliah biasa. Ia melihatmu membaca dan cepat-cepat mengatakan masih bisa diatur."
    miyuki "Besok mulai. Aku senang, sungguh. Aku juga takut tiba di sana dan lupa semua yang pernah kupelajari."
    nar "Ia menunjukkan satu jawaban yang ditandai pembimbing, lalu tiga halaman yang hendak diulang sebelum tidur."
    call kk_family_menu("Mi12", ["Bantu ia mengulang bahan belajarnya.", "Ajak ia meninggalkan catatannya sebentar.", "Beri ia ruang untuk belajar sendiri."])
    if _return == "A":
        nar "Kau menutup kolom jawaban dan membacakan soal. Miyuki sempat salah, mengulang alasannya, lalu menemukan bagian yang perlu diperbaiki."
        miyuki "Jangan kasih petunjuk dulu. Aku mau tahu letak lupanya."
        nar "Belajar bersama membuat rasa takutnya punya batas yang bisa dikerjakan: satu pertanyaan, satu pembahasan, kemudian berhenti pada jam yang disepakati."
    elif _return == "B":
        nar "Kau mengajaknya meninggalkan catatan. Miyuki mengikuti beberapa langkah, lalu berkali-kali melihat tasnya."
        miyuki "Aku mau istirahat, tapi belum ingin pergi lama. Besok benar-benar mulai."
        nar "Ajakanmu bisa menjadi jeda, bisa juga gangguan. Malam itu ia kesulitan menikmati apa pun sebelum tahu kapan akan diizinkan kembali menyiapkan dirinya."
    else:
        nar "Kau memberi ruang belajar dan menanyakan apakah ada barang yang perlu diambilkan sebelum pergi. Miyuki menggeleng, lalu menyebut air minum dengan malu-malu."
        miyuki "Terima kasih. Aku akan kabari kalau sudah selesai. Bukan minta ditemani terus, cuma... aku ingin ada yang tahu."
        nar "Ia membuka kembali catatan. Kesibukannya baru dimulai; kedekatan kalian kini harus belajar menghormati waktu yang tidak selalu bisa dibagi."
    return

# ┌─ PANDUAN CERITA · Mi13 · Telepon Ibu
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : tekanan dari orang tua.
# │ INTI    : A dengarkan / B tegur ibunya / C alihkan.
# │ AKHIRAN : kelelahan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi13:
    call kk_scene_enter("miyuki","Rumah Sakit Tachibana")
    nar "Panggilan ibunya masuk tepat saat Miyuki duduk untuk makan. Ia menjawab karena takut ada keadaan penting. Suara yang terdengar justru membicarakan undangan keluarga, prestasi anak kenalan, dan mengapa ia jarang pulang."
    miyuki "Ibu, aku masih di rumah sakit. Makan malamku baru... iya, aku dengar."
    nar "Ia menurunkan sendok. Nasi di kotak terbuka kehilangan hangat selama ia mengucapkan paham berulang kali."
    call kk_family_menu("Mi13", ["Tunggu dan dengarkan setelah ia selesai.", "Minta ibunya memberi Miyuki waktu istirahat.", "Alihkan pembicaraan setelah ia menutup telepon."])
    if _return == "A":
        nar "Kau menunggu, lalu bertanya apakah ia ingin membicarakannya. Miyuki menyandarkan punggung pada kursi."
        miyuki "Aku ingin suatu hari ditelepon cuma karena Ibu ingin mendengar suaraku. Bukan mengecek apakah hidupku sudah sesuai rencana."
        nar "Ia menatap makanannya, malu karena kalimat itu terdengar seperti keluhan seorang anak. Kau tetap mendengarkan sampai ia tidak perlu mengecilkannya lagi."
    elif _return == "B":
        nar "Kau meminta ibunya memberi Miyuki waktu makan dan istirahat. Hening singkat menyusul sebelum jawaban sopan yang jelas tidak menyukai campur tanganmu."
        miyuki "Terima kasih. Tapi nanti aku yang harus melanjutkan pembicaraan ini. Aku ingin kamu tahu kenapa kadang aku takut dibela di depan Ibu."
        nar "Ia akhirnya bisa makan, tetapi ponselnya tetap diletakkan menghadap atas."
    else:
        nar "Kau mengganti topik sesudah telepon ditutup. Miyuki mengikutinya dengan mudah, bahkan menyisipkan satu godaan agar kau yakin suasana kembali ringan."
        nar "Namun makanannya tidak banyak berkurang. Ketika waktunya kembali ke dalam, ia merapikan kotak itu sambil meminta maaf karena makan terlalu lama."
    return

# ┌─ PANDUAN CERITA · Mi-D02 · Tertidur di Bahu
# │ LOKASI  : (dinamis — muncul dari kondisi) · TERLIBAT: Tachibana Miyuki
# │ AWALAN  : kelelahan ≥ 60; pemain duduk di dekatnya
# │ INTI    : A Biarkan sampai bangun (dua jam lewat) / B bangunkan / C foto / D pindahkan ke ruang jaga
# │ AKHIRAN : Intim +, kelelahan −5; foto bisa sampai ke Mei
# └─ tulis / perbaiki dialog di bawah ──
label kk_library_rest(place):
    if not kk_can_sit_with_miyuki(place):
        return
    nar "Miyuki membaca paragraf yang sama tiga kali. Pada bacaan keempat, jarinya tidak lagi mengikuti baris. Ia menutup mata sambil tetap menahan buku agar tampak masih bekerja."
    miyuki "Kalau aku istirahat sebentar, tolong jaga bukuku. Sebentar saja."
    nar "Tak lama kepalanya bersandar di bahumu. Napasnya berubah teratur sebelum ia sempat menyadari jarak kalian."
    menu:
        "Tetap duduk sampai ia terbangun.":
            $ kk_record_choice("Mi-D02","A")
            $ kk_minutes(120)
            nar "Kau tetap duduk, mengubah posisi sesedikit mungkin. Suara halaman dan langkah orang berganti di sekitar kalian; untuk sementara, Miyuki tidak menjawab siapa pun."
            miyuki "Dua jam? Aku ingin marah karena nggak dibangunkan, tapi... aku sudah lama nggak bangun tanpa langsung merasa pusing."
            nar "Ia meminta maaf soal bahumu, lalu berhenti ketika kau mengatakan keputusan tinggal adalah keputusanmu."
        "Bangunkan ia dengan pelan.":
            $ kk_record_choice("Mi-D02","B")
            $ kk_minutes(5)
            nar "Kau memanggil pelan sampai ia membuka mata. Miyuki menegakkan tubuh terlalu cepat, mencari jam sebelum mencari wajahmu."
            miyuki "Aku tertidur, ya. Maaf. Aku harus cari tempat istirahat yang benar."
            nar "Ia mengusap pipi, malu tetapi mulai mengakui bahwa memaksa satu paragraf lagi tidak akan menolongnya."
        "Ambil foto saat ia tertidur.":
            $ kk_record_choice("Mi-D02","C")
            $ kk_flag("foto_miyuki_tertidur")
            $ kk_minutes(5)
            nar "Foto itu tersimpan di ponselmu ketika Miyuki belum bisa memutuskan apakah ia ingin dilihat seperti itu. Wajah yang tertidur membuatnya tampak jauh lebih muda dan tidak terlindungi."
            nar "Kau bisa menyebutnya kenangan manis. Jika gambar itu sampai ke tangan orang lain, Miyuki tetap yang harus menghadapi tatapan dan pertanyaan tentang sesuatu yang tidak pernah ia setujui untuk dibagikan."
        "Bantu ia beristirahat di ruang jaga.":
            $ kk_record_choice("Mi-D02","D")
            $ kk_minutes(15)
            nar "Kau membangunkannya cukup untuk menawarkan ruang jaga, lalu membawakan bukunya ketika ia bersedia pindah. Miyuki berjalan dengan mata berat, berhenti sekali untuk memastikan tidak ada barang tertinggal."
            miyuki "Tolong ingatkan aku kalau nanti bilang masih bisa lanjut. Aku barusan bahkan lupa halaman yang kubaca."
            nar "Di ruang jaga ia akhirnya berbaring. Kali ini istirahat tidak perlu disamarkan sebagai kegiatan belajar."
    return

init 1 python:
    def kk_begin_miyuki_clinic():
        kk_stage("miyuki",max(2,stage.get("miyuki",0)))

    def kk_study_with_miyuki():
        kk_begin_miyuki_clinic()
        kk_rel("miyuki","trust",3)
        kk_change_medical_career(5)

    def kk_miyuki_nap():
        kk_adj("kelelahan_miyuki",-5)
        kk_rel("miyuki","intim",2)

    _hook("Mi12-A",kk_study_with_miyuki)
    _hook("Mi12-B",kk_begin_miyuki_clinic)
    _hook("Mi12-C",kk_begin_miyuki_clinic)
    for response in "ABC":
        _hook("Mi13-" + response,lambda: kk_adj("kelelahan_miyuki",8))
    _hook("Mi-D02-A",kk_miyuki_nap)
    _hook("Mi-D02-D",kk_miyuki_nap)

# ┌─ PANDUAN CERITA · Mi06 · Rencana Masa Depan
# │ LOKASI  : Kampus Kouseikan · Gedung Kedokteran
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : ia bercerita tentang pediatri.
# │ INTI    : A dukung / B remehkan / C tanyakan Koita.
# │ AKHIRAN : Trust.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi06:
    call kk_scene_enter("miyuki","Gedung Kedokteran")
    nar "Miyuki berhenti di depan gambar buatan anak-anak yang dipajang dekat gedung kuliah. Ia menunjuk seekor kucing berkaki enam dan tersenyum tanpa perlu memeriksa apakah kau ikut tersenyum."
    miyuki "Aku suka saat anak akhirnya bertanya sendiri. Kadang semua orang dewasa sudah memberi jawaban sebelum dia tahu boleh bertanya apa."
    miyuki "Aku ingin masuk pediatri. Bukan karena kupikir akan selalu menyenangkan. Justru karena banyak yang perlu didengar sebelum bisa ditolong."
    call kk_family_menu("Mi06", ["Tanya apa lagi yang membuatnya ingin bekerja dengan anak-anak.", "Katakan cita-cita itu kedengarannya terlalu sederhana.", "Tanya apa Koita sudah tahu rencananya."])
    if _return == "A":
        miyuki "Kamu sungguh mau dengar? Kalau begitu jalan pelan sedikit. Aku bisa panjang sekali kalau mulai soal ini."
        nar "Ia bercerita tentang ketakutan anak yang tidak dianggap serius, tentang keluarga yang juga perlu penjelasan, dan tentang betapa ia ingin belajar mendengarkan tanpa buru-buru merasa paling tahu."
        nar "Kali ini kelelahannya tidak lenyap, tetapi ada keinginan miliknya sendiri yang cukup terang untuk terlihat di baliknya."
    elif _return == "B":
        miyuki "Kedengarannya sederhana karena aku belum menjelaskan pekerjaannya. Tapi keinginanku bukan hal kecil bagiku."
        nar "Ia berhenti bercerita. Saat kalian berjalan lagi, ia membahas tugas kuliah yang tidak mengharuskan ia menyerahkan sesuatu yang begitu pribadi untuk dinilai."
    else:
        miyuki "Belum. Aku tadi sedang bercerita kepadamu."
        nar "Senyumnya kembali, lebih tipis. Koita tetap penting baginya, tetapi memasukkan namanya ke setiap keinginan membuat Miyuki mendadak merasa cita-citanya sendiri perlu persetujuan seseorang yang tidak sedang berada di sana."
    return

# ┌─ PANDUAN CERITA · Mi21 · Rotasi Klinik
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : cabang spesialis.
# │ INTI    : A bantu / B ganggu.
# │ AKHIRAN : karier.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi21:
    call kk_scene_enter("miyuki","Rotasi pediatri · Rumah Sakit Tachibana")
    if kk_has("miyuki_cita_didengar"):
        miyuki "Ingat yang kuceritakan waktu kita jalan dari gedung kuliah? Minggu ini aku akhirnya masuk bangsal anak."
    else:
        miyuki "Aku baru dapat jadwal bangsal anak. Aku harus berangkat sebentar lagi."
    nar "Beberapa lembar jadwal jatuh saat Miyuki meraih tas. Ia berjongkok untuk mengambilnya sambil tetap menoleh ke jam. Di saku jasnya terselip pulpen dengan hiasan kecil yang mungkin disukai pasien anak."
    call kk_family_menu("Mi21", ["Bantu susun jadwalnya agar ia bisa segera masuk.", "Tahan dia sebentar untuk urusanmu sendiri."])
    if _return == "A":
        nar "Kau menyusun jadwal menurut penjelasannya dan menyerahkan lembar kuning paling atas. Miyuki memeriksa sekali, kemudian mengembuskan napas lega."
        miyuki "Terima kasih. Aku ingin masuk dengan kepala yang nggak masih sibuk mencari kertas."
        nar "Ia berangkat tepat waktu. Sebelum pintu menutup, ia sempat menoleh dan berjanji bercerita saat jeda, jika tenaganya cukup."
    else:
        nar "Kau menahannya untuk urusanmu. Miyuki mencoba mendengar, tetapi setiap menit membuat tangannya bergerak menuju tas."
        miyuki "Aku harus masuk sekarang. Bisa kita lanjut nanti?"
        nar "Ia akhirnya berani memotong. Meski begitu, sisa gugup dan rasa bersalah ikut dibawa ke dalam, menutupi sebagian kegembiraan yang tadi ingin ia bagi."
    return

# ┌─ PANDUAN CERITA · Mi-D09 · Pasien Kecil
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Tachibana Miyuki
# │ AWALAN  : rotasi pediatri Tahun 3; Aff Sedang
# │ INTI    : A Datang ke RS / B telepon / C tidak bisa datang
# │ AKHIRAN : didukung: luka[[diri] −, karier +; ia merasa dibutuhkan dengan cara yang sehat
# └─ tulis / perbaiki dialog di bawah ──
label kk_pediatric_patient:
    nar "Pesan Miyuki lebih pendek daripada biasanya. Ia tidak menyebut nama atau detail pribadi pasien, hanya mengatakan seorang anak yang selama ini menyapanya di pintu sedang memburuk."
    miyuki "Aku tahu aku bukan orang yang bisa menjanjikan semuanya baik. Tadi aku hampir mengatakannya kepada keluarganya karena nggak tahan melihat mereka takut."
    miyuki "Sena menggantikanku sebentar. Aku perlu beberapa menit untuk mengingat bahwa sedih bukan berarti aku gagal bekerja."
    call kk_family_menu("Mi-D09", ["Temani Miyuki di ruang tunggu rumah sakit.", "Telepon dia saat jeda berikutnya.", "Katakan kau tidak bisa menemaninya."])
    if _return == "A":
        nar "Kau datang ke ruang tunggu dan duduk tanpa meminta penjelasan yang bukan hakmu. Miyuki bercerita tentang perasaannya sendiri, tentang betapa ingin ia memberi jawaban ketika yang tersedia hanya ketidakpastian."
        miyuki "Terima kasih. Aku nggak butuh kamu bilang aku pasti bisa menyelamatkan semua orang. Aku cuma ingin kembali ke sana tanpa harus berbohong agar terdengar kuat."
    elif _return == "B":
        nar "Saat jeda berikutnya kau menelepon. Miyuki mengangkatnya."
        miyuki "Aku cuma ingin ada yang mendengar. Sebentar saja."
        nar "Kau tetap di telepon sementara ia menyusun napas dan kata-kata. Ketika namanya dipanggil, ia mengatakan sudah lebih siap kembali."
        miyuki "Aku masih takut. Tapi bukan berarti harus menjauh dari pekerjaan yang kuinginkan. Nanti aku kabari kalau sudah ada waktu."
    else:
        miyuki "Baik. Terima kasih sudah menjawab. Aku akan kembali ke dalam."
        nar "Ia menutup panggilan sebelum kau sempat mencari kalimat tambahan. Kemudian ada pesan bahwa ia akan bicara dengan Sena saat bisa. Ia tetap memerlukan seseorang untuk mendengar, sekalipun malam itu bukan dirimu."
    return

init 1 python:
    def kk_change_medical_career(delta):
        pts.setdefault("karier_miyuki",70)
        kk_adj("karier_miyuki",delta)

    def kk_support_pediatrics():
        kk_rel("miyuki","trust",5)
        kk_flag("miyuki_cita_didengar")

    def kk_support_patient_shift():
        pts.setdefault("luka_miyuki_diri",15)
        kk_adj("luka_miyuki_diri",-5)
        kk_change_medical_career(5)

    _hook("Mi06-A",kk_support_pediatrics)
    _hook("Mi06-B",lambda: kk_rel("miyuki","trust",-5))
    _hook("Mi21-A",lambda: kk_change_medical_career(5))
    _hook("Mi21-B",lambda: kk_change_medical_career(-5))
    _hook("Mi-D09-A",kk_support_patient_shift)
    _hook("Mi-D09-B",kk_support_patient_shift)

# ┌─ PANDUAN CERITA · Mi-D11 · Malam Sebelum CBT
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Tachibana Miyuki
# │ AWALAN  : minggu M30
# │ INTI    : A temani belajar semalaman (tubuh pemain) / B bawakan makanan lalu pulang / C tidak datang
# │ AKHIRAN : hasil Mi24 bergeser
# └─ tulis / perbaiki dialog di bawah ──
label kk_exam_eve:
    nar "Miyuki menandai soal yang salah sampai halaman itu dipenuhi warna. Ketika kau datang, ia sudah mengulang materi yang sama meski bisa menjawabnya tanpa melihat."
    miyuki "Kalau buku kututup, rasanya ada satu halaman yang akan membuat besok gagal. Aku tahu itu nggak masuk akal. Mengetahuinya belum membuat tanganku bisa berhenti."
    menu:
        "Temani ia mengulang soal sampai pagi.":
            $ kk_record_choice("Mi-D11","A")
            $ kk_minutes((6-kk_slot)*240-kk_minute)
            nar "Kalian mengulang soal sampai suara kendaraan pagi mulai terdengar. Sesekali Miyuki mampu menjelaskan dengan jernih, lalu lupa hal sederhana karena terlalu lelah."
            miyuki "Kita sudah sampai pagi, ya. Terima kasih menemani. Aku senang nggak sendirian, tapi tubuhmu juga pasti capek."
            nar "Buku akhirnya ditutup. Keberanian yang didapat dari kehadiranmu harus berbagi tempat dengan kantuk yang tidak bisa dinegosiasikan."
        "Bawakan makan malam dan beri ia waktu untuk istirahat." if saldo >= 800:
            $ kk_record_choice("Mi-D11","B")
            $ kk_post_money(-800,"Makan sebelum CBT")
            $ kk_adj("kelelahan_miyuki",-8)
            $ kk_minutes(30)
            nar "Kau meninggalkan makan malam dan mengucapkan selamat beristirahat. Miyuki sempat mengajakmu tinggal, lalu mengakui bahwa ajakan itu juga cara menunda menutup buku."
            miyuki "Aku makan sekarang. Setelah itu aku coba tidur. Tolong jangan tanya sudah belajar berapa halaman lagi kalau aku mengirim kabar."
        "Ucapkan semoga lancar lalu pulang.":
            $ kk_record_choice("Mi-D11","C")
            $ kk_minutes(5)
            nar "Kau mengucapkan semoga lancar dan pulang. Miyuki mengantarmu sampai pintu, berterima kasih dengan suara yang sengaja dibuat ringan."
            nar "Sebelum pintu menutup, ia kembali melihat meja. Buku itu masih terbuka pada halaman yang sama; malam yang tersisa harus ia atur tanpa kehadiranmu."
    return

init python:
    def kk_record_cbt_result():
        if kk_has("cbt_miyuki_lulus") or kk_has("cbt_miyuki_gagal"):
            return
        risks = int(kk_get("karier_miyuki",70) < 40) + int(kk_get("kelelahan_miyuki",35) >= 75)
        helped = any(c["ev"] == "Mi-D11" and c["key"] in ("A","B") for c in choices_log)
        kk_flag("cbt_miyuki_lulus" if risks <= int(helped) else "cbt_miyuki_gagal")

# ┌─ PANDUAN CERITA · Mi24 · Hasil CBT
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : hasil ujian.
# │ INTI    : A rayakan / B hibur / C abaikan.
# │ AKHIRAN : karier.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi24:
    call kk_scene_enter("miyuki","Hasil ujian · Rumah Sakit Tachibana")
    if kk_has("cbt_miyuki_lulus"):
        miyuki "Aku membaca daftarnya dua kali. Terus minta Sena baca juga. Namaku memang ada. Aku lulus."
        nar "Ia tertawa sambil menutup mulut, kemudian menangis sebelum sempat mengatakan tidak apa-apa. Tubuhnya rupanya baru mengizinkan seluruh ketakutan yang ditahan selama ini keluar."
    else:
        miyuki "Aku belum lulus. Aku sudah baca penjelasannya. Ada yang bisa diurus besok. Hari ini aku ingin duduk sebentar sebelum harus mengatakan ke keluarga."
        nar "Ia melipat lembar pengumuman sampai namanya tidak terlihat. Kertas itu tidak seberat perasaan yang membuat tangannya sulit diletakkan tenang."
    menu:
        "Ajak ia merayakannya." if kk_has("cbt_miyuki_lulus"):
            $ kk_record_choice("Mi24","A")
            miyuki "Ayo. Aku ingin pesan kue yang nggak kubuat sendiri. Dan nggak perlu memilih yang murah hanya karena merasa harus rendah hati."
            nar "Ia tertawa lagi, lebih lega. Perayaan itu tetap kecil, tetapi untuk sekali ini semua orang di meja duduk karena ingin merayakan sesuatu miliknya."
        "Duduk bersamanya dan dengarkan.":
            $ kk_record_choice("Mi24","B")
            nar "Kau duduk dan membiarkan ia menentukan apa yang ingin diceritakan. Miyuki berbicara tentang takut menelepon rumah, tentang hal yang dipelajari, tentang betapa lelahnya menunggu hasil yang dianggap bisa merangkum dirinya."
            miyuki "Terima kasih sudah nggak buru-buru menyuruhku merasa sesuatu. Aku ingin tahu dulu sebenarnya aku merasa apa."
        "Beri ia ruang dan pamit.":
            $ kk_record_choice("Mi24","C")
            nar "Kau memberi ruang dan pamit. Miyuki memasukkan kertas ke tas, lalu duduk sekali lagi setelah sempat hendak berdiri."
            nar "Hasil itu tetap harus dibawa pulang, dibicarakan, dan ditempatkan di dalam masa depan yang belum selesai. Kau tidak berada di sampingnya saat ia memulai percakapan berikutnya."
    return
