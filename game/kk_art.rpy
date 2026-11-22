# Draft editorial dari Event_Chiasa C05/C09 dan Alur_Cabang/06 §11–12.
# ┌─ PANDUAN CERITA · C05 · Mio Menelepon
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : editor meminta cover jilid baru.
# │ INTI    : A menolak halus / B menerima dan berlatih / C minta bantuan Haruka.
# │ AKHIRAN : curiga_mio; B bisa membuka kemampuan baru bertahap.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C05:
    call kk_scene_enter("chiasa", "Rumah Amamiya")
    nar "Di atas meja belajar kamarmu, buku sketsa bersampul hitam milik Chiasa masih terbuka di halaman latihan anatomi tangan yang belum selesai. Beberapa lembar kertas buram yang penuh goresan kaku hasil latihanmu sendiri tergeletak di samping penghapus uli."
    nar "Baru saja kamu meletakkan pensil mekanik dan hendak merenggangkan jari-jarimu yang pegal, ponsel di dekat tabung kuas bergetar panjang di atas permukaan meja kayu."
    play sound "audio/sfx/phone_vibrate.wav"
    nar "Layar ponsel menyala menampilkan nama pemanggil 'Higashiyama Mio (Redaksi Bunko)'."
    nar "Kamu menatap nama itu selama dua dering penuh. Selama beberapa bulan terakhir, kiriman royalti cetak ulang sebesar lima puluh ribu yen dari penerbit selalu masuk otomatis ke rekening tanpa menuntut gambar baru. Panggilan telepon langsung di siang hari jelas bukan sekadar pemberitahuan transfer bank."
    nar "Kamu menarik napas pendek, menggeser tombol hijau di layar, lalu menempelkan ponsel ke telinga."
    chiasa "Halo, selamat siang, Mio-san."
    "Mio" "Halo, Shena-sensei! Syukurlah langsung diangkat, aku takut tadi masih di dalam ruang studio kampus. Gimana kuliah semester pertamanya di Kouseikan? Sudah mulai terbiasa sama tugas-tugas jurusan seni?"
    nar "Suara Mio di seberang telepon terdengar cerah, cepat, dan akrab seperti seorang editor yang sudah bekerja sama dengan pemilik tubuh ini sejak bangku SMA."
    chiasa "Sudah mulai terbiasa kok, Mio-san. Dosen-dosennya juga baik, cuma jam praktiknya aja yang lumayan panjang."
    "Mio" "Haha, anak seni rupa memang begitu semua keluhannya. Oh iya, Sensei, aku menelepon hari ini karena ada kabar bagus banget dari rapat redaksi pagi tadi. Naskah jilid keempat seri novel strategi yang Sensei pegang kemarin akhirnya sudah selesai ditulis!"
    chiasa "Jilid keempat... sudah selesai naskahnya ya, Mio-san?"
    "Mio" "Iya! Penulisnya kemarin malam baru kirim draf finalnya ke mejaku. Terus terang aja, hasil cetakan ulang jilid ketiga kemarin laris banget di toko buku, dan banyak pembaca yang nulis di kartu pos survei kalau mereka jatuh cinta sama ilustrasi sampul buatan Sensei."
    chiasa "Wah... syukurlah kalau pembaca suka."
    "Mio" "Apalagi cara Sensei menggambar sorot mata tokoh utamanya waktu berdiri di benteng salju itu, lho. Garisnya tipis tapi suasananya dingin dan hidup banget. Makanya kepala redaksi langsung minta aku hubungi Sensei hari ini buat mengamankan jadwal ilustrasi sampul sekaligus tiga gambar sisipan hitam-putih untuk jilid keempat."
    nar "Pandanganmu turun menatap kertas latihan di meja belajarmu sendiri. Lingkaran proporsi wajah dan garis jari yang baru saja kamu buat sepuluh menit lalu tampak kaku dan patah-patah, terpisah jauh sekali dari goresan halus di cetakan sampul novel yang dipajang di rak buku kamar ini."
    "Mio" "Untuk tenggat pengumpulannya masih sekitar dua bulan lagi sih sebelum naik cetak. Gimana menurut Sensei, jadwal kuliah bulan ini memungkinkan nggak buat ambil proyek jilid keempat?"
    nar "Di seberang sambungan, terdengar bunyi klik pulpen Mio yang sudah siap mencatat jawabanmu di buku agendanya."
    call kk_family_menu("C05", ["\"Terima kasih banyak tawarannya, Mio-san, tapi untuk jilid baru ini kayaknya aku belum bisa ambil dulu.\"", "\"Baik, Mio-san, aku ambil proyeknya. Boleh minta tenggat sketsa kasarnya agak longgar?\"", "\"Boleh aku minta waktu sebentar? Ada teman studio yang pengin kuajak diskusi dulu.\""])
    if _return == "A":
        chiasa "Terima kasih banyak tawarannya, Mio-san. Aku senang banget dengar jilid sebelumnya laris. Tapi jujur aja, untuk jilid keempat ini kayaknya aku belum bisa ambil proyeknya dulu."
        nar "Bunyi ketukan pulpen di seberang telepon langsung berhenti. Terdengar jeda hening selama dua detik sebelum Mio kembali bersuara dengan nada hati-hati."
        "Mio" "Eh... belum bisa ambil ya, Shena-sensei? Jadwal tugas studio di kampus lagi padat banget ya bulan ini?"
        chiasa "Iya, Mio-san. Tugas dasar semester awal ini banyak yang harus dikerjakan manual tiap sore, dan aku takut kalau kupaksakan ambil jadwal sampul sekarang, hasilnya malah nggak maksimal dan mengecewakan penulisnya."
        "Mio" "...Begitu ya. Jujur aja sayang banget sih, soalnya penulisnya sudah berharap Sensei lagi yang pegang jilid ini. Tapi kalau memang jadwal kuliah tahun pertama lagi berat, aku nggak mungkin maksa Sensei begadang sampai sakit."
        chiasa "Maaf banget ya, Mio-san, jadi bikin tim redaksi harus repot cari ilustrator pengganti buat jilid ini."
        "Mio" "Nggak apa-apa, Sensei, bagian cari jadwal pengganti itu memang kerjaanku sebagai editor kok. Yang penting Sensei beresin dulu adaptasi kuliahnya di kampus. Oh iya, tenang aja, untuk royalti cetak ulang dari jilid satu sampai tiga tetap ditransfer tiap bulan seperti biasa ya, hak ciptanya kan tetap di tangan Sensei."
        chiasa "Terima kasih banyak pengertiannya, Mio-san."
        "Mio" "Sama-sama. Nanti kalau jadwal studio kampus sudah lebih longgar dan Sensei sudah siap pegang proyek buku lagi, langsung hubungi nomor pribadiku aja ya!"
        nar "Sambungan telepon terputus. Kamu meletakkan ponsel kembali ke samping tabung kuas dan menutup buku sketsa hitam itu perlahan, mengamankan penyamaranmu dari tenggat penerbit setidaknya untuk musim ini."
    elif _return == "B":
        chiasa "Baik, Mio-san, aku ambil proyek jilid keempatnya. Cuma karena sore hari aku masih ada jadwal kelas studio di kampus, boleh aku minta tenggat buat pengiriman sketsa kasarnya agak dilonggarkan sedikit?"
        nar "Terdengar helaan napas lega yang panjang dari seberang telepon, disusul bunyi lembaran kertas agenda yang dibalik cepat."
        "Mio" "Wah, syukurlah Sensei bersedia! Kalau soal jadwal sketsa kasar, tentu aja bisa kugeser mundur dua minggu dari jadwal standar, Sensei. Bagian tata letak sampul biar kukosongkan duluan di percetakan."
        chiasa "Kalau ada waktu tambahan dua minggu untuk sketsa awal, harusnya cukup kok, Mio-san."
        "Mio" "Sip, sudah kucatat di jadwal redaksi! Nanti malam sekitar jam tujuh kukirimkan ringkasan bab penting jilid keempat beserta catatan adegan untuk tiga ilustrasi sisipannya lewat surel ya. Sensei baca-baca santai aja dulu sambil cari ide komposisinya."
        chiasa "Baik, nanti malam langsung kuperiksa surelnya. Terima kasih ya, Mio-san."
        "Mio" "Aku dan tim redaksi yang berterima kasih, Shena-sensei! Sampai ketemu di kiriman draf pertama ya, semangat kuliahnya!"
        nar "Begitu panggilan berakhir, kamar yang tadinya tenang mendadak terasa jauh lebih sempit. Di layar ponselmu, pesan konfirmasi jadwal dari Mio langsung masuk hanya berselang satu menit."
        nar "Kamu menyingkirkan kertas buram yang tadi penuh coretan ragu, menarik satu lembar kertas gambar baru dari laci meja, lalu membuka halaman-halaman lama buku sketsa Chiasa sebagai acuan. Dengan pensil mekanik di tangan, kamu mulai melatih ulang tarikan garis anatomi dan lipatan pakaian satu per satu dari dasar."
    else:
        chiasa "Terima kasih banyak tawarannya, Mio-san. Tapi sebelum aku kasih kepastian sanggup atau nggaknya, boleh aku minta waktu satu atau dua hari dulu? Kebetulan ada teman dekat di studio kampus yang mau kuajak diskusi soal pembagian waktu latihan sama jadwal tugasku bulan ini."
        "Mio" "Oh, mau mencocokkan jadwal sama teman studio dulu ya? Boleh banget kok, Shena-sensei. Rapat penetapan kontrak ilustratornya baru dikunci hari Jumat sore, jadi Sensei masih punya waktu buat hitung jadwal dengan tenang."
        chiasa "Syukurlah kalau masih sempat. Sebelum hari Jumat pasti langsung kukabari keputusannya, Mio-san."
        "Mio" "Oke, kutunggu kabarnya ya, Sensei. Jangan terlalu diporsir tenaganya di kampus!"
        nar "Setelah menutup telepon dari Mio, kamu tidak meletakkan ponselmu. Kamu membuka aplikasi pesan singkat dan mencari nama kontak Ishikawa Haruka yang sejak awal semester selalu duduk satu meja studio denganmu."
        nar "Kamu mengetik pesan dengan jujur tanpa berusaha terdengar seperti ilustrator mahir, menanyakan apakah besok sore sehabis kelas praktik studio Haruka langsung pulang dan apakah ia bersedia mengajarimu proporsi serta tarikan garis dasar dari awal."
        play sound "audio/sfx/phone_buzz.wav"
        nar "Kurang dari satu menit kemudian, ponsel di tanganmu bergetar oleh balasan antusias dari Haruka yang heran kamu tiba-tiba minta diajari gambar dasar, tetapi ia langsung mengiyakan dan mengajakmu memakai meja pojok studio sampai jam tutup besok."
        nar "Kamu menyimpan ponsel ke atas meja dan menyiapkan buku sketsa kosong ke dalam tas kuliahmu untuk latihan besok sore."
    return

# ┌─ PANDUAN CERITA · C09 · Buku Sketsa Kosong
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : pemain tidak bisa menggambar sebaik asli.
# │ INTI    : A latihan keras / B menyewa pihak lain / C berhenti.
# │ AKHIRAN : royalti ¥50.000 tetap masuk (), tetapi tawaran proyek dari Mio bisa gagal.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C09:
    call kk_scene_enter("chiasa", "Rumah Amamiya")
    nar "Buku sketsa lama terbuka pada gambar tangan Koita. Bahkan cara jari itu menahan cangkir terasa dikenal oleh orang yang menggambarnya. Di halaman sebelah, percobaanmu tampak kaku. Kau memiliki wajah Chiasa, sandi ponselnya, dan meja kerjanya; kepekaan yang membuat gambar itu hidup tidak ikut bangun bersamamu."
    call kk_family_menu("C09", ["Mulai lagi dengan latihan sendiri.", "Cari orang lain untuk mengerjakannya.", "Tutup bukunya untuk hari ini."])
    if _return == "A":
        nar "Kau mengambil halaman baru dan berlatih bentuk sederhana. Hasilnya tidak tiba-tiba bagus. Menjelang akhir, kau bisa menunjukkan satu garis yang lebih mantap daripada sebelumnya. Untuk pertama kalinya hari ini, ada sesuatu di buku Chiasa yang sungguh dikerjakan olehmu, tanpa meminjam pujian masa lalunya."
    elif _return == "B":
        nar "Kau mencari orang yang sanggup menyelesaikan pekerjaan itu. Membayar keahlian seseorang dapat menjadi kerja sama yang sah, tetapi kau belum siap menyebut namanya kepada orang yang memesan karya Shena. Di sela kelegaan karena pekerjaan mungkin selesai, tumbuh ketakutan terhadap pertanyaan sederhana: siapa yang membuat gambar ini?"
    else:
        nar "Kau menutup buku. Sore terus berjalan tanpa memaksamu membuktikan apa pun. Namun sampul yang sudah terbit tetap memakai nama Shena, dan suatu hari seseorang akan meminta melihat proses gambar baru. Berhenti hari ini memberimu ruang bernapas; ia belum menjawab bagaimana kau akan hidup dengan nama yang diwariskan itu."
    return

init 1 python:
    def kk_take_cover_project():
        kk_flag("proyek_mio_diterima")
        pts.setdefault("shena_risiko",20)
        kk_adj("shena_risiko",10)

    def kk_practice_sketch(place):
        if not kk_can_sketch(place):
            return
        kk_adj("kemampuan_gambar", 1 if kk_kelelahan_tier()[1] >= 2 else 3)
        pts.setdefault("shena_risiko",20)
        kk_adj("shena_risiko",-1)
        kk_minutes(60)

    _hook("C05-B", kk_take_cover_project)
    _hook("C05-C", lambda: kk_flag("haruka_dimintai_bantuan"))
    _hook("C09-A", lambda: kk_adj("kemampuan_gambar",5))
    def kk_commission_secret():
        kk_flag("ilustrasi_dikerjakan_orang_lain")
        pts.setdefault("shena_risiko",20)
        kk_adj("shena_risiko",10)

    _hook("C09-B", kk_commission_secret)

# ┌─ PANDUAN CERITA · C-D03 · Tangan yang Gemetar
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Chiasa
# │ AWALAN  : Chiasa host; berlatih saat Sangat Lelah
# │ INTI    : A berhenti dan tidur / B paksa sampai pagi / C minta Haruka mengajar
# │ AKHIRAN : kemampuan_gambar hanya naik sedikit saat lelah; tubuh menanggung
# └─ tulis / perbaiki dialog di bawah ──
label kk_draw_at_home:
    if not kk_can_sketch(_lokasi):
        return
    if kk_shaking_hands():
        nar "Pensil bergetar meskipun kau sudah menahan pergelangan. Di antara dua garis, kau lupa bentuk yang hendak dibuat. Kemarahan datang lebih cepat daripada rasa kantuk: tubuh ini tidak mau lagi menuruti janji yang kaubuat atas namanya."
        call kk_family_menu("C-D03", ["Letakkan pensil dan beristirahat.", "Teruskan sampai pagi.", "Singkirkan kertasnya dan minta Haruka mengajarimu."])
        if _return == "A":
            nar "Kau meletakkan pensil sebelum ujungnya kembali menyentuh kertas. Berhenti terasa seperti kalah sampai kau menyadari bahwa tubuh ini juga bagian dari hidup yang sedang kautanggung."
            call kk_rest_home
            return
        elif _return == "B":
            $ kk_adj("kemampuan_gambar",1)
            $ kk_minutes((6 - kk_slot)*240 - kk_minute)
            nar "Pagi datang tanpa kemenangan. Beberapa bagian memang membaik, tetapi kau harus mendekatkan wajah untuk membedakannya dari coretan yang dibuat ketika pikiranmu mulai kabur. Ketika terdengar orang menyiapkan sarapan, rasa malu membuatmu tetap duduk. Malam yang panjang belum mengubahmu menjadi Shena."
            return
        else:
            $ kk_flag("haruka_dimintai_bantuan")
            $ kk_minutes(5)
            nar "Kau menulis kepada Haruka bahwa tanganmu gemetar dan latihanmu buntu. Pesan itu tidak meminta ia mengerjakan gambar atas namamu. Kau meminta dia mengajarimu, bahkan jika pelajaran pertama ternyata hanya berhenti sebelum kebencian pada diri sendiri mengambil alih seluruh meja kerja."
            return
    $ kk_practice_sketch(_lokasi)
    nar "Satu jam latihan memberimu halaman yang penuh koreksi. Kau menandai lengkung yang belum benar dan tanggal hari ini. Perkembangannya kecil, tetapi tanggal itu membuatnya nyata: keterampilanmu punya awal, dan awal itu boleh berbeda dari riwayat Chiasa."
    return

# ┌─ PANDUAN CERITA · C-D07 · Pesan Mio Jam Sebelas
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Chiasa
# │ AWALAN  : Chiasa host; ada proyek
# │ INTI    : A mengaku tidak sanggup / B minta perpanjangan / C sewa ilustrator / D begadang
# │ AKHIRAN : menyewa = kebohongan baru yang bisa ditemukan Shiori; begadang = tubuh dan kemampuan
# └─ tulis / perbaiki dialog di bawah ──
label kk_mio_deadline:
    if not kk_mio_message():
        return
    nar "Pukul sebelas, Mio mengirim pesan singkat menanyakan sketsa yang dijanjikan. Tidak ada tanda seru. Kesopanannya justru membuatmu merasa lebih bersalah; di pihaknya ada jadwal kerja dan orang lain yang menunggu, sementara di mejamu masih ada gambar yang takut kautunjukkan."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Akui bahwa kau kesulitan mengerjakannya.", "Minta waktu tambahan.", "Cari ilustrator lain untuk menyelesaikannya.", "Buka sketsanya dan lanjutkan sampai pagi."])]
    call screen kk_choice_panel(_rows, "Pesan Mio")
    $ kk_record_choice("C-D07", _return)
    if _return == "A":
        nar "Kau mengakui bahwa hasilmu belum memenuhi yang dijanjikan. Mio menanyakan apa yang sudah selesai dan apa yang masih mungkin dilakukan. Jawabannya praktis, tetapi tidak kejam. Masalah itu kini nyata di antara dua orang, tidak lagi hanya berputar di kepalamu."
    elif _return == "B":
        nar "Kau meminta perpanjangan dan mengakui pekerjaan belum siap. Mio tidak langsung menjawab. Kau menatap layar, baru memahami bahwa waktu tambahan yang diminta darinya juga akan diambil dari orang lain. Begitu jawabannya datang, kau membacanya sampai akhir sebelum mencoba membela diri."
    elif _return == "C":
        nar "Kau menghubungi ilustrator lain. Percakapan tentang pekerjaan terasa menenangkan sampai ia bertanya bagaimana kredit akan ditulis. Kau belum menjawab dengan jujur kepada Mio, dan setiap bantuan yang disepakati di atas kebisuan itu menambah orang yang kelak bisa merasa diperalat."
    else:
        $ kk_adj("kemampuan_gambar",1 if kk_kelelahan_tier()[1] >= 2 else 3)
        $ kk_minutes((6 - kk_slot)*240 - kk_minute)
        nar "Ketika langit terang, ada bagian yang akhirnya bisa kautunjukkan. Kau juga terlalu lelah untuk merasa lega. Janji berikutnya tidak akan menjadi lebih mudah hanya karena malam ini berhasil kauhabiskan tanpa tidur; pikiran itu menunggu bersama pesan Mio di layar."
        return
    $ kk_minutes(5)
    return

init 1 python:
    _hook("C-D07-A", lambda: kk_flag("mio_tahu_kesulitan"))
    _hook("C-D07-B", lambda: kk_flag("perpanjangan_diminta"))
    _hook("C-D07-C", kk_commission_secret)

# ┌─ PANDUAN CERITA · C-D02 · Dua Sketsa Berdampingan
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Chiasa
# │ AWALAN  : Chiasa host; shena_risiko ≥ 40
# │ INTI    : A Jujur / B beri alasan / C minta Haruka mengajar
# │ AKHIRAN : rahasia Shena dibagi, atau curiga naik
# └─ tulis / perbaiki dialog di bawah ──
label kk_show_portfolio:
    if not kk_art_studio_open(_lokasi):
        return
    if kk_comparison_due():
        nar "Haruka meratakan dua sketsa di meja. Ia tidak menuduhmu menurun; ia bertanya mengapa cara tanganmu mencari bentuk menjadi begitu berbeda. Perhatiannya tidak berhenti pada hasil buruk. Justru karena ia mengenal pekerjaanmu, alasan biasa terdengar semakin tipis."
        call kk_family_menu("C-D02", ["Ceritakan terus terang kenapa sketsa itu berbeda.", "Beri alasan untuk perbedaan itu.", "Minta ia mengajarimu membuat garis itu lagi."])
        if _return == "A":
            nar "Kau mengakui jarak antara nama Shena dan kemampuan yang kaumiliki sekarang. Haruka tidak buru-buru menyebutmu palsu atau menawarkan menyelesaikan semuanya. Ia bertanya apa yang sanggup kaulakukan sendiri. Pertanyaan itu menyakitkan, tetapi memberimu tempat untuk mulai menjawab dengan benar."
        elif _return == "B":
            nar "Kau memberi alasan yang terdengar masuk akal jika didengar sekali. Haruka memandang gambar itu lebih lama, lalu berkata bahwa ia bertanya karena ingin membantu. Ia membiarkan alasanmu tetap berada di meja, berdampingan dengan dua lembar yang tidak sepenuhnya mendukungnya."
        else:
            nar "Kau meminta dia mengajarimu dari bagian yang paling dasar. Haruka menggeser kertas kosong dan bertanya apakah kau siap dikoreksi tanpa dibandingkan terus dengan gambar lama. Kau mengangguk. Menjadi murid di depan orang yang dulu mengagumi pekerjaanmu terasa memalukan sekaligus melegakan."
    else:
        nar "Haruka menilai halaman yang kaubawa tanpa meminta ia menyerupai karya lama. Ia menunjukkan bagian yang sudah konsisten dan bagian yang masih ragu. Kau mencatat koreksinya di tepi kertas, menikmati percakapan tentang pekerjaan yang benar-benar ada di depan kalian."
    if kk_has("haruka_dimintai_bantuan") or kk_get("kemampuan_gambar") >= 30:
        $ kk_adj("kemampuan_gambar",3)
        $ pts.setdefault("shena_risiko",20)
        $ kk_adj("shena_risiko",-1)
    $ kk_minutes(60)
    return

# ┌─ PANDUAN CERITA · C11 · Pameran Kecil dan Shiori
# │ LOKASI  : Kampus Kouseikan · Gedung Seni Rupa & Studio
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : Shiori datang ke pameran; ia pembaca Shena.
# │ INTI    : A mengaku / B pura-pura tidak tahu / C beri tanda tangan.
# │ AKHIRAN : jembatan ke Shiori atau perangkap (Rute Revenge jika kebohongan).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C11:
    call kk_scene_enter("shiori","Pameran seni · Studio")
    nar "Di pameran kecil itu, Shiori berhenti lebih lama di depan satu gambar. Ia tidak memanggil orang lain ketika melihatmu mendekat; rasa ingin tahunya diberikan kepadamu lebih dulu, bukan kepada penonton."
    shiori "Garis ini mengingatkanku pada ilustrasi Shena. Aku punya bukunya. Bukan hanya sampulnya yang kuingat."
    call kk_family_menu("C11", ["Akui bahwa kau yang memakai nama Shena.", "Pura-pura tidak mengenal nama itu.", "Tawarkan membubuhkan tanda tangan."])
    if _return == "A":
        shiori "Jadi kau Shena. Terima kasih sudah memberitahuku sendiri. Aku ingin bertanya tentang gambarnya, kalau kau bersedia; aku tidak sedang meminta kau menjadi tokoh dalam buku itu."
    elif _return == "B":
        nar "Kau menyangkal mengenal nama itu. Shiori menatap karya di dinding, kemudian wajahmu. Ia tidak berdebat di tengah pameran. Kesopanan yang tetap ia berikan membuat kebohonganmu tidak terasa lebih ringan, hanya belum dipersoalkan."
    else:
        shiori "Di halaman ini, kalau boleh. Tulis namamu juga. Aku suka mengingat siapa yang kutemui, bukan cuma nama yang tercetak di sampul."
    return

init 1 python:
    def kk_tell_haruka():
        kk_flag("haruka_tahu_shena")
        kk_adj("shena_risiko",-10)

    _hook("C-D02-A", kk_tell_haruka)
    _hook("C-D02-B", lambda: kk_adj("curiga_haruka",5))
    _hook("C-D02-C", lambda: kk_flag("haruka_dimintai_bantuan"))
    _hook("C11-A", lambda: kk_flag("shiori_tahu_shena"))
    _hook("C11-B", lambda: kk_adj("daftar_kebohongan_shiori",1))
    _hook("C11-C", lambda: kk_flag("shiori_tahu_shena"))
