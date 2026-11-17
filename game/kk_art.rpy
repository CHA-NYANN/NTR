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
    nar "Nama Mio muncul tepat ketika kau sedang mencari alasan untuk menutup buku sketsa. Editor itu menyapamu sebagai Shena, hangat dan tanpa keraguan. Ia membicarakan jilid berikutnya, tokoh yang akan muncul di sampul, dan kesan sunyi yang dulu berhasil kautangkap. Semua pujian itu ditujukan kepada tangan yang sedang kaupakai, tetapi bukan kepada kemampuanmu."
    call kk_family_menu("C05", ["Ucapkan terima kasih dan tolak dengan halus.", "Ambil proyeknya dan siapkan waktu untuk berlatih.", "Katakan kau perlu mendiskusikannya dengan Haruka."])
    if _return == "A":
        nar "Kau berterima kasih dan menolak pekerjaan baru. Mio terdiam, lalu menanyakan apakah kau perlu jeda lebih panjang. Tidak ada ancaman untuk mencabut royalti karya lama. Ketika telepon ditutup, kau merasakan kehilangan yang aneh: melepaskan kesempatan milik orang lain tetap terasa seperti gagal menjadi seseorang."
    elif _return == "B":
        nar "Kau menerima. Mio terdengar lega, dan kelegaannya membuat janji itu semakin berat. Sesudah telepon ditutup, kau membuka halaman latihan, bukan contoh sampul. Kau harus memulai dari garis yang sanggup kautarik hari ini, meskipun orang di ujung telepon mengira ia baru berbicara dengan ilustrator berpengalaman."
    else:
        nar "Kau meminta waktu untuk membicarakannya dengan Haruka. Mio setuju menunggu kepastian; ia belum menganggap pekerjaan itu selesai hanya karena namamu tercantum. Dalam pesan kepada Haruka, kau menulis bahwa ada hal yang tidak bisa lagi kauberesi sendirian. Kali ini bantuan harus berarti lebih dari seseorang yang menyembunyikan kekuranganmu."
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
