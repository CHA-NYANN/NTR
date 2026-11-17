# Event dinamis Koita lanjutan (K-D02/03/04/06/07/10/11/12/14/15/17).
# Melanjutkan thread kesadaran -> keruntuhan + gerbang rute (BL/Success) sebagai
# POINTER non-eksplisit, dan K-D17 (Koita menemukan akibat Force) ditulis sebagai
# KONSEKUENSI + KARAKTER saja: tanpa metode, tanpa adegan, tanpa cara memfitnah.
# Lihat [[feedback-force-route-non-operational]].

# ┌─ PANDUAN CERITA · K-D02 · Jalan Pulang yang Diperpanjang
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : takut_ditinggal ≥ 60
# │ INTI    : A Temani / B tanya kenapa / C biarkan
# │ AKHIRAN : Koita bicara soal rumah; benih BL (Y) atau Koita Success (C)
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K_D02:
    call kk_scene_enter("koita", "Jalan pulang · Rute jauh")
    nar "Di persimpangan kedua, Koita kembali mengambil arah yang menjauhi rumah. Ia menunjuk toko yang sudah tutup, mengatakan pernah membeli buku di sana, lalu kehabisan cerita sebelum kalian melewati etalasenya."
    koita "Lewat sungai juga bisa, ya. Memang agak jauh. Tapi belum malam-malam banget."
    nar "Ia melihat layar ponsel. Tidak mengetik apa pun. Ketika kau memperlambat langkah, ia ikut melambat tanpa menoleh."
    koita "Dulu aku suka rumah kosong. Bisa main sampai pagi, nggak ada yang menegur. Sekarang suara kulkas saja kedengaran sampai kamarku."
    nar "Lampu penyeberangan berganti hijau. Koita tidak segera bergerak."
    call kk_family_menu("K-D02", ["Temani ia berjalan.", "Tanyakan kenapa.", "Biarkan ia sendiri."])
    if _return == "A":
        nar "Kau mengambil sisi jalan yang sama dengannya. Tidak bertanya sampai kapan; untuk sementara, kalian hanya berjalan."
        koita "Kamu nggak ada urusan? Kalau ada, bilang. Aku tadi hampir pura-pura nggak tahu supaya kamu terus ikut."
        nar "Pengakuan itu membuatnya salah tingkah. Ia memasukkan ponsel ke saku."
        koita "Aku nggak butuh keliling sekota, kok. Sampai lampu berikutnya saja. Habis itu... kita lihat."
        nar "Ketika kalian mencapai lampu berikutnya, ia yang lebih dahulu bertanya apakah kau lelah."
    elif _return == "B":
        koita "Kalau aku pulang dan nggak ada siapa-siapa, rasanya semua orang sudah punya kehidupan yang nggak butuh aku."
        nar "Ia buru-buru menggeleng, seolah ingin menarik kembali kalimatnya sebelum terdengar seperti tuntutan."
        koita "Aku tahu mereka boleh sibuk. Chiasa juga bukan penjaga rumah. Aku tahu. Cuma... tahu dan nggak takut itu beda, ya."
        nar "Kau membiarkan jawabannya tetap menjadi jawaban, tanpa menjanjikan bahwa seseorang akan selalu menunggu."
        koita "Mungkin aku harus belajar pulang meskipun nggak ada yang menyuruh."
    else:
        nar "Kau berhenti di persimpangan. Koita masih berjalan dua langkah sebelum sadar suara sepatumu tidak menyusul."
        koita "Oh. Kamu lewat sana, ya. Iya, hati-hati."
        nar "Ia tersenyum terlalu cepat. Dari tempatmu, kau melihatnya mengambil ponsel lagi, menggulir daftar percakapan, kemudian mematikan layarnya."
        nar "Kali ini ia menyeberang ke arah rumah, tetapi berjalan lebih lambat daripada sebelumnya."
    return

# ┌─ PANDUAN CERITA · K-D03 · Uang untuk Hadiah
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : Male Route
# │ INTI    : A Beri / B tolak / C tanya untuk siapa
# │ AKHIRAN : intel pilihan_koita[[x]
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K_D03:
    call kk_scene_enter("koita", "Apartemen · Permintaan ganjil")
    nar "Koita menunjukkan dua benda dalam keranjang belanja daring: sebuah hadiah dan bungkus yang harganya hampir seperempat hadiah itu. Jarinya menutupi nama penerima pada catatan pesanan."
    koita "Menurutmu bungkus yang ini terlalu niat? Aku mau kelihatan serius, tapi nggak mau bikin dia merasa harus jawab sesuatu."
    yutaka "Kalau kamu memang serius, bukannya wajar dia ingin tahu maksudmu?"
    nar "Koita mengunci layar. Sesudah jeda yang kurang nyaman, ia menanyakan uang."
    koita "Boleh bantu bayar sebagian? Bukan pinjaman, sih. Aku belum tahu kapan bisa ganti. Kalau nggak bisa, bilang saja."
    call kk_family_menu("K-D03", ["Berikan uangnya.", "Tolak dengan halus.", "Tanya hadiah itu untuk siapa."])
    if _return == "A":
        nar "Kau memberikan uang yang dimintanya. Koita menghitung sekali, lalu menyimpannya tanpa lagi membicarakan bungkus."
        koita "Makasih, Yutaka. Aku tahu ini agak keterlaluan."
        yutaka "Hadiah darimu tetap harus kamu yang menjelaskan maksudnya. Aku cuma membantu uangnya."
        koita "Iya. Aku nggak akan pakai namamu kalau dia bertanya."
        nar "Ia membuka pesanan kembali. Kali ini ia memilih kotak untuk menulis pesan, bukan pilihan hiasan."
    elif _return == "B":
        yutaka "Maaf, uangku sudah ada keperluannya. Aku nggak bisa."
        koita "Oh. Iya, tentu. Aku cuma tanya."
        nar "Ia menutup keranjang terlalu cepat, seolah barang-barang itu bisa melihat penolakannya."
        koita "Aku pikir kalau hadiahnya cukup bagus... ya, sudahlah. Aku cari yang sesuai uangku saja."
        nar "Kalimatnya berakhir kecil. Kau tak tahu apakah yang terasa ditolak baginya adalah permintaan uang atau keberanian yang baru ia kumpulkan."
    else:
        yutaka "Sebelum soal uang, ini untuk siapa? Kamu bicara seperti dia akan tahu maksudmu dari kertas kado."
        nar "Koita membuka layar lagi dan memperlihatkan nama pada catatan pesanan. Ia menyebut alasan yang sangat khusus: sesuatu yang pernah diinginkan orang itu, dalam percakapan yang ternyata ia ingat."
        koita "Aku ingat hal begini. Terus aku mengira itu sudah cukup sebagai jawaban."
        yutaka "Mengingat dan menjawab kan beda."
        koita "Iya. Kayaknya itu bagian yang selama ini sengaja kulewati."
    return

# ┌─ PANDUAN CERITA · K-D04 · Dua Pesan yang Sama
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : pemain melihat ponsel dua heroine
# │ INTI    : A Simpan tangkapan layar / B hadapi Koita / C abaikan
# │ AKHIRAN : bukti pola; pola_publik naik bila disebar
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K_D04:
    call kk_scene_enter("koita", "Layar ponsel · Dua pesan")
    nar "Kedua pesan itu diperlihatkan kepadamu dalam percakapan terpisah. Masing-masing penerima tersenyum saat sampai pada kalimat terakhir. Masing-masing mengira kalimat tersebut hanya ditujukan kepadanya."
    nar "Besok kalau capek, cari aku dulu, ya. Aku paling senang kalau kamu yang datang."
    nar "Bahkan letak komanya sama. Kau ingat Koita menunggu balasan dengan senyum malu-malu; sekarang sulit membayangkan senyum itu hanya terjadi sekali."
    call kk_family_menu("K-D04", ["Simpan tangkapan layar.", "Hadapi Koita langsung.", "Abaikan, bukan urusanmu."])
    if _return == "A":
        nar "Kau menyimpan tangkapan layar yang telah diperlihatkan kepadamu. Di ukuran kecil, kedua gambar itu tampak seperti salinan satu percakapan. Nama di atasnya yang membuat perbedaannya tak bisa diabaikan."
        nar "Tak ada janji eksklusif tertulis di sana. Ada dua orang yang dibimbing menuju kesimpulan yang sama, dan seseorang yang menerima kehangatan dari keduanya."
        nar "Kau belum menyebarkannya. Menyimpan pola bukan berarti sudah mengetahui seluruh cerita, tetapi sekarang kau tidak perlu mengandalkan ingatan saja."
    elif _return == "B":
        koita "Aku memang sering bilang begitu. Itu cara ngomongku. Masa perhatian harus beda kalimat ke setiap orang?"
        nar "Ia terdengar tersinggung sebelum kau selesai menjelaskan mengapa kedua penerima menganggap pesan itu istimewa."
        koita "Mereka bilang begitu? Dua-duanya?"
        nar "Tangannya naik ke tengkuk. Untuk beberapa detik ia kehilangan alasan yang biasa muncul dengan lancar."
        koita "Aku nggak bermaksud bikin mereka salah paham. Tapi... aku juga nggak pernah membetulkan, ya."
    else:
        nar "Kau mengembalikan pembicaraan ke topik semula. Senyum di hadapanmu tetap utuh karena orang itu belum tahu ada pesan kembar."
        nar "Nanti, ketika Koita menyapa dari ujung koridor, kau masih bisa membalas seperti biasa. Yang terasa ganjil justru betapa mudahnya."
        nar "Tak ada yang berubah hari ini bagi dua penerima pesan itu. Keraguanmu tinggal bersamamu."
    return

# ┌─ PANDUAN CERITA · K-D06 · Debat di Klub Sastra
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : Matsuda sekutu (K07-A)
# │ INTI    : A Dukung Matsuda / B bela Koita / C tetap diam
# │ AKHIRAN : pola_publik ±
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K_D06:
    call kk_scene_enter("koita", "Klub Sastra · Debat")
    nar "Matsuda tidak mengembalikan lembar cerpen Koita setelah sesi baca. Ia menunjuk satu paragraf ketika anggota lain sudah mulai membereskan tas."
    "Matsuda" "Tokohmu bilang dia nggak pernah menjanjikan apa-apa. Terus narator menyebut perempuan yang menunggunya terlalu menuntut. Kenapa cuma dia yang diberi hak menjelaskan?"
    koita "Karena sudut pandangnya dari dia. Tokoh yang salah juga boleh punya cerita, kan?"
    "Matsuda" "Boleh. Aku bertanya kenapa ceritanya selalu membenarkan dia."
    nar "Tas-tas berhenti dibereskan. Koita menatapmu sekilas; biasanya pada titik ini seseorang akan membantu mengubah ketegangan menjadi lelucon."
    call kk_family_menu("K-D06", ["Dukung Matsuda.", "Bela Koita.", "Tetap diam."])
    if _return == "A":
        nar "Kau menunjuk bagian ketika perempuan itu meminta kepastian. Tak ada tuntutan agar cintanya dibalas, hanya permintaan agar ia tak terus diminta menunggu."
        "Matsuda" "Itu. Dia minta jawaban, bukan hadiah karena bersabar."
        koita "Aku bisa menulis ulang bagian itu."
        nar "Tak seorang pun menuduh Koita secara langsung. Namun ia menarik lembar cerpennya lebih dekat, seperti melindungi sesuatu yang jauh lebih pribadi."
    elif _return == "B":
        nar "Kau membela hak Koita menulis tokoh yang tidak menyenangkan. Beberapa anggota mengangguk, lega mendapat jalan keluar dari pembicaraan yang mulai terasa pribadi."
        koita "Iya. Itu maksudku. Makasih."
        "Matsuda" "Hak menulisnya nggak sedang kucabut. Aku sedang membaca akibat dari cara dia menulis."
        nar "Tetapi waktunya sudah lewat. Seseorang mengusulkan membeli minuman, dan Koita berdiri di dekatmu ketika kelompok mulai beranjak."
        koita "Tadi kupikir kamu juga akan ikut menyerang. Syukurlah."
    else:
        nar "Kau tetap duduk. Matsuda menunggu sebentar, lalu menyerahkan lembar cerpen itu langsung kepada Koita."
        "Matsuda" "Pikirkan saja. Aku sudah menuliskan catatanku."
        koita "Iya. Nanti kubaca."
        nar "Pembicaraan berikutnya tentang jadwal klub. Koita ikut menjawab dengan nada biasa, tetapi kertas Matsuda tidak ia masukkan bersama catatan anggota lain."
    return

# ┌─ PANDUAN CERITA · K-D07 · Pelukan di Stasiun
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : Male Route; ikatan_bl ≥ 50
# │ INTI    : A Balas / B tahan jarak / C bercanda
# │ AKHIRAN : rantai BL maju atau tertahan
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K_D07:
    call kk_scene_enter("koita", "Stasiun · Setelah menjemput")
    nar "Pintu pemeriksaan tiket baru saja lewat di belakangmu ketika Koita menarikmu ke dalam pelukan. Ranselmu tersangkut pada lengannya; ia tidak segera melepas."
    yutaka "Koita? Keretanya cuma telat. Aku tadi sudah kirim pesan."
    koita "Iya. Kubaca. Aku tahu."
    nar "Jawaban itu tidak menjelaskan mengapa ia masih memelukmu. Ketika orang lewat menyenggol bahunya, ia bergeser agar kalian tidak menghalangi jalan, tetapi tetap dekat."
    koita "Aku senang kamu datang. Cuma itu yang tadi kepikiran."
    call kk_family_menu("K-D07", ["Balas pelukannya.", "Jaga jarak dengan canggung.", "Cairkan dengan bercanda."])
    if _return == "A":
        nar "Kau meletakkan tangan di punggungnya. Koita menarik napas yang terasa tertahan sejak tadi."
        yutaka "Aku di sini. Kamu boleh lepas kalau sudah mau."
        koita "Kalau belum mau?"
        yutaka "Bilang. Jangan pura-pura cuma salam biasa."
        nar "Ia tertawa kecil di bahumu, lalu mengangguk. Saat akhirnya menjauh, wajahnya lebih merah daripada yang bisa dijelaskan oleh udara stasiun."
        koita "Belum tadi. Sekarang... ayo makan dulu. Aku mau kamu ikut."
    elif _return == "B":
        nar "Kau menahan bahunya dengan lembut dan memberi jarak. Koita segera melepas, terlalu cepat meminta maaf."
        yutaka "Aku kaget. Aku butuh waktu."
        koita "Iya, tentu. Aku tadi nggak mikir. Maaf."
        nar "Ia mengambil satu langkah ke samping agar kalian bisa berjalan berdampingan. Tangan yang tadi memelukmu kini sibuk membetulkan tali tas yang sebenarnya sudah lurus."
        nar "Kalian membicarakan keterlambatan kereta. Tak satu pun benar-benar ingin membicarakan kereta."
    else:
        yutaka "Kalau tiap pulang dapat sambutan begini, nanti aku sengaja naik kereta yang paling lambat."
        koita "Jangan. Aku bisa tambah tua di depan gerbang tiket."
        nar "Tawanya kali ini lepas. Ia mundur, membiarkanmu membetulkan tas."
        koita "Tapi serius. Makasih sudah ngasih kabar. Aku tahu itu hal kecil. Buatku... ternyata nggak kecil."
        nar "Kalian berjalan menuju deretan kedai. Bahunya beberapa kali menyentuh bahumu; ia tidak lagi menggunakan keramaian sebagai alasan."
    return

# ┌─ PANDUAN CERITA · K-D10 · Kebetulan yang Gagal Tiga Kali
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : plot_armor_tekanan ≥ 75
# │ INTI    : A " Tertawakan / B akui sebagian / C ceritakan Sistem
# │ AKHIRAN : koita_sadar +; jalur E-KO-13
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K_D10:
    call kk_scene_enter("koita", "Kafe · Tiga kegagalan")
    nar "Koita mencoret tiga jam di sudut struk kafe. Satu karena orang yang ditunggu sudah pulang, satu karena kursi di sebelahnya terisi, satu karena hujan reda sebelum ia sempat menawarkan payung."
    koita "Aku tahu kedengarannya bodoh kalau diurut begini. Tapi biasanya aku nggak perlu mengurutkannya. Biasanya semuanya... pas."
    nar "Ia menatap ujung pena, tampak malu oleh keganjilan yang baru saja ia akui."
    koita "Aku nggak mengatakan mereka wajib memilih aku. Aku cuma merasa ada yang berubah sebelum mereka sempat memilih. Dan kamu selalu kelihatan sudah tahu."
    call kk_family_menu("K-D10", ["Tertawakan kecurigaannya.", "Akui sebagian.", "Ceritakan soal Sistem."])
    if _return == "A":
        nar "Kau tertawa dan menyebut tiga kebetulan yang gagal itu hal biasa. Koita ikut tersenyum, lalu menutup struk dengan telapak tangannya."
        koita "Iya, ya. Orang juga punya jadwal sendiri. Aku tahu itu."
        nar "Namun ia tidak membuang struk tersebut. Ia melipatnya dua kali dan memasukkannya ke dompet."
        koita "Kamu ketawa sebelum aku selesai cerita. Bagian mana yang sebenarnya lucu?"
        nar "Ia tidak mendesak jawaban. Justru itu yang membuat pertanyaannya tetap terasa setelah topik berganti."
    elif _return == "B":
        nar "Kau mengakui telah mengambil beberapa kesempatan yang dulu mungkin menjadi miliknya, tetapi menahan penjelasan tentang Sistem."
        koita "Jadi kamu sengaja?"
        nar "Ia memandangmu lama, mencoba memisahkan pengakuanmu dari bagian yang masih kausimpan."
        koita "Aku lebih suka kamu bilang begitu daripada bilang aku kebanyakan mikir. Tapi ada yang belum kamu katakan, kan?"
        nar "Kopinya mendingin di antara kalian. Koita tak lagi bersedia menyebut semua perubahan itu kebetulan."
    else:
        nar "Kau menjelaskan Sistem, tugasnya, dan bagaimana kedekatan orang-orang di sekitar Koita dijadikan sesuatu yang dapat dinilai. Makin jauh penjelasanmu, makin sedikit ekspresi yang tersisa di wajahnya."
        koita "Aku nggak tahu apakah aku percaya. Tapi kalau itu benar... selama ini kamu melihat kami sebagai apa?"
        nar "Ia memutar cangkir, lalu menjauhkannya tanpa minum."
        koita "Dan kalau dulu aku selalu dapat kesempatan yang terlalu bagus, apa itu juga dibuatkan untukku?"
        nar "Pertanyaan berikutnya keluar lebih pelan."
        koita "Yang kurasakan ke mereka, yang mereka rasakan ke aku... bagian mana yang masih bisa kami sebut milik sendiri?"
    return

# ┌─ PANDUAN CERITA · K-D11 · Pilihan Lebih Awal
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : pilihan_koita[[x] ≥ 80; koita_sadar ≥ 75
# │ INTI    : A Dukung / B halangi / C diam
# │ AKHIRAN : belok besar bagi heroine itu
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K_D11:
    call kk_scene_enter("koita", "Gedung Sastra · Pilihan lebih awal")
    nar "Koita memintamu berhenti di bordes, jauh dari teman-teman yang turun menuju kantin. Ia menyebut satu nama dengan suara yang tidak dibuat ringan."
    koita "Aku mau bilang padanya. Hari ini kalau dia bersedia ketemu."
    nar "Ia menunjukkan pesan yang belum dikirim: permintaan waktu, tanpa alasan darurat dan tanpa umpan tentang kabar buruk."
    koita "Aku belum tentu dapat jawaban yang kuinginkan. Tapi aku nggak mau menunggu sampai dia memilih orang lain baru merasa punya keberanian."
    call kk_family_menu("K-D11", ["Dukung keputusannya.", "Halangi dulu.", "Diam saja."])
    if _return == "A":
        nar "Kau mendukungnya dan mengingatkan bahwa pengakuan itu juga harus mengakhiri harapan palsu yang ia pelihara di tempat lain."
        koita "Aku tahu. Yang itu malah lebih kutakuti. Aku nggak bisa lagi memakai alasan belum mengerti perasaanku."
        nar "Ia membaca pesannya sekali lagi, lalu mengirim."
        koita "Kalau dia bilang tidak, aku tetap harus bicara dengan yang lain, ya."
        nar "Untuk pertama kalinya, ia terdengar memahami bahwa memilih seseorang bukan sekadar kesempatan mendapatkan sesuatu."
    elif _return == "B":
        nar "Kau memintanya menunggu. Koita menurunkan ponsel, menatapmu tanpa senyum yang biasa ia pakai untuk menutup keberatan."
        koita "Waktu aku nggak memilih, itu salah. Sekarang aku mau memilih, kamu bilang jangan dulu. Aku harus menunggu apa?"
        nar "Pesan itu tetap belum terkirim. Ia menguncinya, tetapi tidak memasukkan ponsel ke saku."
        koita "Aku akan mendengar alasanmu. Tapi jangan menyebut ini demi kebaikanku kalau sebenarnya kamu takut kehilangan kesempatanmu sendiri."
    else:
        nar "Kau tidak menghalangi maupun menyemangati. Koita mengangguk kecil, seolah jawabanmu memang cukup sampai di situ."
        koita "Aku tadi berharap kamu bilang ini benar. Biar kalau gagal, rasanya bukan cuma aku yang salah menilai."
        nar "Ia menatap pesan yang belum dikirim."
        koita "Tapi itu bukan urusanmu untuk menjamin, ya."
        nar "Ia beranjak dari bordes dengan ponsel di tangan. Apa pun yang akan terjadi berikutnya, ia tidak lagi bisa menyebutnya sekadar mengikuti saranmu."
    return

# ┌─ PANDUAN CERITA · K-D12 · Gladi Resik Pidato
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : menjelang M36
# │ INTI    : A Jujur / B memuji / C menulis ulang untuknya
# │ AKHIRAN : nada epilog Koita berubah
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K_D12:
    call kk_scene_enter("koita", "Gladi resik pidato wisuda")
    nar "Mikrofon aula masih mati. Koita mencoba dua paragraf pidatonya ke ruangan kosong, kemudian turun dari podium dan menyerahkan naskah kepadamu."
    koita "Bagian tentang orang yang datang dan mengubah hidup kita... terlalu jelas, ya?"
    nar "Paragraf itu indah. Hampir semua akibat buruk di dalamnya dijelaskan sebagai pelajaran berharga bagi orang yang berpidato. Orang lain hanya disebut sebagai mereka yang pernah hadir."
    koita "Jujur saja. Aku nggak mau terdengar seolah sudah mengerti semuanya cuma karena bisa membuat kalimat yang rapi."
    call kk_family_menu("K-D12", ["Beri pendapat jujur.", "Puji saja agar ia tenang.", "Tawarkan menulis ulang untuknya."])
    if _return == "A":
        nar "Kau mengatakan bahwa orang yang pernah disakitinya tidak harus berterima kasih karena penderitaan mereka membuatnya dewasa. Koita membaca paragraf itu lagi sampai ke tanda titik."
        koita "Aku menulis ini sambil membayangkan semua orang memaafkanku di akhir pidato. Ketahuan, ya."
        nar "Ia mencoret satu kalimat, kemudian satu lagi."
        koita "Mungkin aku cukup bilang ada hal yang belum selesai. Permintaan maaf yang sungguhan harus kusampaikan ke orangnya, bukan ke aula."
        nar "Ketika ia kembali mencoba, kalimatnya lebih pendek dan suaranya beberapa kali tersandung. Kau bisa mengenali orang yang sedang bicara."
    elif _return == "B":
        nar "Kau memuji irama dan pilihan katanya. Koita mengembuskan napas, segera kembali ke paragraf yang tadi ia ragukan."
        koita "Aku takut terlalu sok bijak. Kalau kamu bilang bagus, mungkin aman."
        nar "Ia memberi tanda pada tempat untuk berhenti dan menarik napas. Sekarang ia tahu cara membacakannya agar terdengar tulus."
        nar "Pertanyaan tentang apa yang belum ia katakan hilang di antara latihan intonasi dan cara memegang mikrofon."
    else:
        nar "Kau mengambil pena dan mengganti paragraf yang paling sulit ia selesaikan. Koita mengikuti gerak tulisanmu, sesekali meminta penjelasan sebuah kata."
        koita "Kalau aku yang bilang ini, kamu percaya?"
        nar "Ia mencoba membacanya. Terdengar lebih baik: lebih tenang, lebih lengkap, dengan pengakuan yang sebelumnya tak mampu ia susun."
        koita "Bagus. Tapi nanti kalau ada yang bertanya maksudku... aku harus bisa menjawab sendiri, ya."
        nar "Ia menuliskan catatan kecil di pinggir naskahmu. Kata-katanya belum menjadi miliknya hanya karena ia akan membacakannya."
    return

# ┌─ PANDUAN CERITA · K-D14 · Kebetulan yang Tidak Datang Lagi
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : plot_armor_tekanan ≥ 90; orbit_koita ≤ 1
# │ INTI    : A Datangi dia / B biarkan / C kirim heroine yang tersisa
# │ AKHIRAN : plot armor padam; jalur E-KO-18
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K_D14:
    call kk_scene_enter("koita", "Tempat kebetulan · Yang kosong")
    nar "Minuman kedua di meja Koita sudah tak lagi berembun. Ia memesan rasa yang biasa disukai seseorang, lalu baru teringat bahwa hari ini mereka tidak punya janji."
    koita "Dulu aku duduk di sini sebentar, terus pasti ada yang lewat. Sampai kupikir tempat ini memang ramai."
    nar "Tempat itu memang ramai. Orang-orang membeli minuman, mencari uang kecil, bertemu teman. Tidak satu pun berbelok ke mejanya."
    koita "Aku kayak sedang menunggu namaku dipanggil. Padahal nggak ada yang bilang akan datang."
    call kk_family_menu("K-D14", ["Datangi dia.", "Biarkan ia menunggu.", "Kirim orang lain yang tersisa."])
    if _return == "A":
        nar "Kau mendekat dan menanyakan apakah kursinya kosong. Koita mengangguk, lalu tersadar dan menggeser minuman kedua."
        koita "Ini sudah dingin. Eh, maksudku... bukan berarti kamu harus ambil yang sudah kupesan. Kamu mau apa?"
        nar "Pertanyaan sederhana itu tampak memerlukan usaha. Ia baru saja berhenti menganggap orang yang datang akan pas dengan tempat yang disiapkannya."
        koita "Makasih sudah duduk. Aku nggak mau bohong, tadinya aku mengharapkan orang lain. Tapi aku senang kamu di sini."
    elif _return == "B":
        nar "Kau lewat tanpa mendatanginya. Melalui kaca, kau masih bisa melihat Koita setiap kali arus pejalan kaki memberi celah."
        nar "Ia menunggu sampai petugas mengambil kursi dari meja sebelah. Barulah ia berdiri, membawa dua minuman yang salah satunya belum disentuh."
        nar "Tidak ada hujan mendadak, tidak ada seseorang yang tersandung ke pelukannya. Koita harus menentukan sendiri ke mana pergi setelah tempat itu tutup."
    else:
        nar "Kau menghubungi seseorang yang masih dekat dengannya dan menyampaikan bahwa Koita sedang sendirian di sana. Kau tidak menjanjikan akan ada pengakuan atau kabar istimewa."
        nar "Ketika orang itu datang, Koita berdiri terlalu cepat. Lalu ia melihat siapa yang benar-benar ada di hadapannya."
        koita "Oh. Maaf, aku tadi melamun. Duduk, kalau mau."
        nar "Mereka mulai berbicara. Sesekali mata Koita masih mengarah ke pintu, dan orang di depannya cukup dekat untuk menyadari itu."
    return

# ┌─ PANDUAN CERITA · K-D15 · Dari Seberang Jalan
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : heroine yang dulu di orbit Koita sedang bersama pemain di tempat umum
# │ INTI    : A Pamer / B pura-pura tidak lihat / C hampiri dan jelaskan
# │ AKHIRAN : runtuh_koita +15 / +5 / ±; pamer menaikkan Fear dan rumor
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K_D15:
    call kk_scene_enter("koita", "Seberang jalan")
    nar "Kantong belanja di tangan Koita berayun sekali, kemudian diam. Ia berhenti di seberang jalan, tepat saat pendampingmu sedang menceritakan sesuatu yang membuatmu tertawa."
    nar "Kau bertemu pandang dengannya sebelum sempat berpura-pura tidak melihat. Pendampingmu mengikuti arah matamu. Suasana yang semula ringan berubah, bukan karena siapa pun telah mengatakan sesuatu."
    call kk_family_menu("K-D15", ["Pamerkan kedekatan itu.", "Pura-pura tidak melihat.", "Hampiri dan jelaskan."])
    if _return == "A":
        nar "Kau mendekatkan tubuh dengan gerak yang sengaja bisa dilihat dari seberang. Pendampingmu sempat kaku; ia mengerti bahwa perhatianmu sedang tertuju pada reaksi orang lain."
        nar "Koita mencoba tersenyum. Ia mengangkat tangan setengah, lalu menurunkannya ketika menyadari sapaan tidak sedang ditawarkan."
        nar "Ia pergi sebelum lampu berganti. Di sampingmu, cerita tadi tidak dilanjutkan. Kemesraan yang kaupamerkan meninggalkan rasa dipakai pada orang yang masih berdiri bersamamu."
    elif _return == "B":
        nar "Kau kembali menatap pendampingmu, menanyakan kelanjutan ceritanya dengan nada sedikit terlalu cerah. Ia menjawab, tetapi matanya sekali lagi bergerak ke seberang."
        nar "Koita tidak memanggil. Ketika lampu berganti, ia membiarkan rombongan pertama menyeberang tanpa ikut."
        nar "Sesudah beberapa langkah kau menoleh. Ia sudah tidak berada di tempat tadi; kau tidak tahu apakah ia pulang atau hanya mencari jalan yang tidak melewati kalian."
    else:
        nar "Kau meminta waktu kepada pendampingmu sebelum menyeberang. Koita membetulkan pegangan kantong, berusaha menyiapkan wajah biasa."
        koita "Kamu nggak perlu menjelaskan semuanya ke aku. Aku nggak punya hak melarang."
        nar "Kau mengatakan hubungan itu nyata dan bukan pertunjukan untuk melukainya. Ia mendengar tanpa memotong."
        koita "Aku tahu. Itu yang sakit. Kalian bisa bahagia tanpa sedang melakukan sesuatu kepadaku."
        nar "Ia menarik napas dan menanyakan apakah orang yang menunggu di seberang akan canggung jika ia menyapa. Kali ini ia membiarkan jawabannya menentukan langkahnya."
    return

# ┌─ PANDUAN CERITA · K-D17 · Yang Ia Temukan Setelahnya
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : Koita mengetahui Force setelah kejadian, bukan menyaksikan
# │ INTI    : A Pemain ada di sana: sangkal / B diam / C mengaku
# │ AKHIRAN : rasa bersalah Koita; bukti; jalur E-KO-19 atau E-KO-20
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K_D17:
    call kk_scene_enter("koita", "Setelahnya")
    nar "Koita tiba setelah kejadian. Orang yang ditemukannya meminta jarak sebelum ia sempat mengulurkan tangan. Ia berhenti, menurunkan tangannya, dan menanyakan siapa yang boleh dihubungi."
    koita "Aku di sini. Aku nggak akan menyentuh kalau kamu nggak mau. Kita bisa panggil orang yang kamu percaya."
    nar "Lalu ia melihatmu. Sesaat wajahnya bergerak menuju rasa lega yang biasa muncul saat bertemu orang dekat. Rasa itu hilang ketika ia melihat reaksi orang di belakangnya."
    koita "Kenapa kamu ada di sini? Apa yang kamu lakukan?"
    nar "Pertanyaannya rendah dan terputus. Ia tetap berdiri di antara kalian, tidak menghalangi jalan keluar orang yang sedang berusaha ia lindungi."
    call kk_family_menu("K-D17", ["Sangkal semuanya.", "Diam.", "Mengaku padanya."])
    if _return == "A":
        nar "Kau menyangkal keterlibatanmu. Koita menatapmu lama; kau mengenali dorongan lama di wajahnya, keinginan agar orang yang dikenalnya ternyata tetap baik."
        koita "Aku dengar kamu. Tapi aku nggak akan meminta dia membuktikan apa pun kepadamu sekarang."
        nar "Ia berpaling untuk menanyakan lagi siapa yang ingin dihubungi. Penyangkalanmu tidak membuatnya memberikan jalan untuk mendekat."
        nar "Belakangan ia akan memikirkan semua tanda yang pernah ia abaikan. Malam ini rasa bersalah itu belum punya nama, hanya membuat tangannya gemetar saat mencari nomor bantuan yang diminta."
    elif _return == "B":
        nar "Kau tidak menjawab. Koita menunggu cukup lama hingga terdengar napas seseorang yang berusaha tenang di belakangnya."
        koita "Kalau kamu nggak mau bicara, aku tetap akan ingat kamu ada di sini. Dan aku akan mengatakan apa yang kulihat, bukan menebak sisanya."
        nar "Keheninganmu bukan pengakuan yang bisa menjelaskan seluruh kejadian. Namun itu menjadi bagian dari ingatan Koita yang tak bisa lagi ia rapikan menjadi salah paham biasa."
        nar "Ia menyingkirkan keinginannya menanyaimu lebih jauh. Orang yang perlu ia dengarkan saat ini bukan dirimu."
    else:
        nar "Kau mengakui perbuatanmu. Koita tidak segera membalas. Rahangnya mengeras, dan untuk sesaat tangannya mengepal sebelum ia membukanya lagi."
        koita "Jangan minta aku memahami alasanmu sekarang. Jangan mendekat."
        nar "Ia meminta orang yang dapat dipercaya datang menemani korban. Saat berbicara, suaranya hampir tidak terdengar seperti suara yang kaukenal."
        koita "Aku bisa menemani kalau dia mau. Aku bisa mengatakan yang kuketahui. Aku nggak bisa menghapus ini cuma karena kita pernah dekat."
        nar "Sesudahnya ia akan membenci dirinya karena pernah mempercayaimu. Tetapi ia tidak menjadikan perasaan itu alasan untuk mengambil keputusan atas nama korban, atau meminta korban menenangkannya."
    return

init 1 python:
    _hook("K-D02-A", lambda: (kk_rel("koita","trust",4), kk_adj("takut_ditinggal",-6)))
    _hook("K-D02-B", lambda: (kk_koita_aware(4), kk_adj("takut_ditinggal",-4)))
    _hook("K-D02-C", lambda: kk_adj("takut_ditinggal",6))
    _hook("K-D03-A", lambda: (kk_flag("koita_hadiah_diberi"), kk_adj("pilihan_koita_puncak",8)))
    _hook("K-D03-B", lambda: kk_koita_collapse(5))
    _hook("K-D03-C", lambda: kk_adj("pilihan_koita_puncak",10))
    _hook("K-D04-A", lambda: (kk_flag("koita_pola_dicurigai"), kk_flag("bukti_pola_koita")))
    _hook("K-D04-B", lambda: (kk_koita_aware(6), kk_flag("koita_pola_dicurigai")))
    _hook("K-D04-C", lambda: None)
    _hook("K-D06-A", lambda: (kk_adj("pola_publik_koita",10), kk_koita_collapse(5)))
    _hook("K-D06-B", lambda: (kk_rel("koita","trust",5), kk_adj("pola_publik_koita",-5)))
    _hook("K-D06-C", lambda: None)
    _hook("K-D07-A", lambda: (kk_adj("ikatan_bl",10), kk_flag("koita_arah_bl")))
    _hook("K-D07-B", lambda: kk_adj("ikatan_bl",-5))
    _hook("K-D07-C", lambda: kk_rel("koita","aff",3))
    _hook("K-D10-A", lambda: kk_koita_aware(5))
    _hook("K-D10-B", lambda: kk_koita_aware(10))
    _hook("K-D10-C", lambda: (kk_koita_aware(20), kk_flag("koita_tahu_sistem")))
    _hook("K-D11-A", lambda: (kk_flag("koita_memilih_awal"), kk_adj("pilihan_koita_puncak",10)))
    _hook("K-D11-B", lambda: kk_koita_collapse(5))
    _hook("K-D11-C", lambda: kk_koita_aware(4))
    _hook("K-D12-A", lambda: (kk_rel("koita","trust",6), kk_flag("pidato_koita_jujur")))
    _hook("K-D12-B", lambda: kk_rel("koita","aff",3))
    _hook("K-D12-C", lambda: kk_flag("pidato_koita_ditulis_pemain"))
    _hook("K-D14-A", lambda: (kk_rel("koita","trust",5), kk_koita_collapse(5)))
    _hook("K-D14-B", lambda: (kk_koita_collapse(15), kk_flag("plot_armor_padam")))
    _hook("K-D14-C", lambda: kk_koita_collapse(8))
    _hook("K-D15-A", lambda: (kk_koita_collapse(15), kk_rel("koita","fear",8)))
    _hook("K-D15-B", lambda: kk_koita_collapse(5))
    _hook("K-D15-C", lambda: (kk_rel("koita","trust",3), kk_koita_collapse(3)))
    _hook("K-D17-A", lambda: (kk_koita_guilt(10), kk_flag("koita_curiga_pelaku")))
    _hook("K-D17-B", lambda: (kk_koita_guilt(15), kk_flag("bukti_diam_koita")))
    _hook("K-D17-C", lambda: (kk_koita_collapse(20), kk_flag("koita_tahu_pelaku")))
