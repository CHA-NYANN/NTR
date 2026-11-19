# Chiasa host, menjaga penyamaran (C02, C03, C04, C08). Paralel dengan rute Yutaka:
# tingkah yang meleset dari Chiasa asli menaikkan kecurigaan. Event host (fire saat masuk lokasi).
# Variabel curiga_* mengikuti Event_Chiasa; angka adalah setelan prototipe.
# ┌─ PANDUAN CERITA · C02 · "Ko-nii?"
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : sarapan bersama Koita.
# │ INTI    : A memanggil "Ko-nii" natural / B memanggil nama / C menggoda seperti Chiasa asli.
# │ AKHIRAN : B memicu curiga Koita; C menaikkan Jealousy Koita.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C02:
    call kk_scene_enter("chiasa", "Rumah Amamiya")
    nar "Aroma kaldu miso dan roti panggang yang baru diangkat dari pemanggang memenuhi ruang makan keluarga Amamiya. Koita meletakkan dua piring berisi telur mata sapi di atas meja kayu, lalu menoleh setengah badan ke arah teko di dekat kompor."
    koita "Tehnya mau kubuatkan seperti biasa sekalian?"
    nar "Pertanyaan ringan itu membuatmu terdiam sepersekian detik. Kau sama sekali tidak tahu 'seperti biasa' versi Chiasa itu teh hijau tawar, teh hitam, atau teh dengan gula—sampai kau melihat tangan Koita sudah lebih dulu meraih cangkir keramik kuning bermotif kucing dan menjatuhkan satu dadu gula ke dalamnya."
    nar "Ia bertanya hanya karena kebiasaan, bukan karena tidak tahu. Kini ia berdiri menunggu jawabanmu sambil menuangkan air panas."
    nar "Ketika kau membacanya di layar ponsel dulu, sebutan manja Chiasa untuk kakaknya hanyalah deretan huruf cetak di balon dialog. Sekarang, di meja makan yang jaraknya tak sampai dua meter ini, panggilan itu harus keluar dari kerongkonganmu sendiri tanpa terdengar seperti orang asing yang sedang menghafal naskah."
    call kk_family_menu("C02", ["Panggil 'Ko-nii' dengan natural.", "Panggil namanya saja.", "Goda ia seperti Chiasa asli biasanya."])
    if _return == "A":
        nar "Kau menarik napas pendek tanpa suara, melemaskan bahu, lalu membiarkan pita suara tubuh ini melantunkan nada yang paling sering diucapkannya."
        chiasa "Iya, makasih ya, Ko-nii. Kayak biasa aja."
        nar "Gerakan tangan Koita yang sedang mengaduk cangkir tidak terhenti sedikit pun. Ia menaruh teh hangat itu di dekat tangan kananmu sambil tersenyum lega, melepas celemeknya, lalu duduk di kursi seberang."
        koita "Pagi, Chiasa. Tumben sudah rapi jam segini. Biasanya hari pertama semester pun kau masih harus kugedor sampai tiga kali baru mau lepas dari guling."
        chiasa "Hari pertama kuliah kan beda sama SMA, Ko-nii. Kalau aku telat di hari orientasi, nanti kesannya buruk."
        koita "Haha, tumben bijak. Ngomong-ngomong, Ibu kirim pesan lagi subuh tadi. Katanya lauk di kotak plastik biru harus dihabiskan hari ini biar nggak basi di kulkas."
        nar "Kau mengangguk sambil menyumpit sepotong telur, diam-diam mencatat setiap petunjuk kecil yang ia berikan secara cuma-cuma—mulai dari letak kotak makan di kulkas, kebiasaan bangun tidur pemilik tubuh ini, hingga jam keberangkatan kalian ke stasiun."
        koita "Nanti gedung Fakultas Seni Rupa agak jauh di sayap barat kampus. Kalau kau bingung jalannya habis acara pembukaan, tunggu saja di dekat kantin utama, ya."
        chiasa "Iya, gampang. Ko-nii nggak usah terlalu khawatir begitu."
        nar "Panggilan itu diterima begitu mulus sampai kau justru merasa semakin ganjil. Koita terus bercerita santai tentang jadwal kuliah Sastranya sambil mengunyah roti, sama sekali tidak menyadari bahwa gadis di seberang mejanya sedang memunguti serpihan informasi dari percakapan biasa demi bertahan hidup sebagai adiknya."
    elif _return == "B":
        nar "Lidahmu terasa kelu untuk meniru nada manja yang biasa dipakai pemilik tubuh ini. Sebelum kau sempat menimbang dampaknya, kalimat yang keluar dari bibirmu justru terdengar datar dan lugas."
        chiasa "Iya, tolong. Makasih, Koita."
        nar "Bunyi kucuran teh dari moncong teko mendadak berhenti. Tangan Koita terpaku di udara selama dua detik penuh sebelum ia menoleh perlahan ke arahmu dengan kening berkerut."
        koita "...'Koita'? Tumben sekali. Sejak kapan kau memanggilku pakai nama langsung begitu?"
        nar "Ia mengeluarkan tawa pendek yang terdengar canggung, menaruh cangkir kuning itu ke atas meja, lalu menatapmu seolah sedang menunggu kelanjutan dari sebuah lelucon."
        nar "Jemari tangan kananmu refleks bergerak menyentuh ujung pita hitam di rambutmu. Kau baru menyadari betapa fatalnya satu kata itu ketika seluruh kedekatan di dalam rumah ini dibangun dari cara Chiasa menyebut namanya."
        chiasa "A-ah, itu... aku kan mulai hari ini sudah jadi mahasiswi, bukan anak SMA lagi. Cuma pengin coba kedengaran lebih dewasa saja."
        koita "Apaan sih, malah kedengaran dingin kayak orang asing tahu nggak? Kupikir kau bangun tidur langsung marah gara-gara sesuatu."
        nar "Koita mencoba mencairkan suasana dengan senyum tipis sambil duduk di kursinya, tetapi caranya menatapmu saat mengambil sumpit tidak lagi sesantai tadi."
        koita "Kalau kau lagi nggak enak badan atau kepikiran soal kampus baru, bilang saja lho, Chi-chan."
        chiasa "Nggak kok, aku cuma masih setengah mengantuk. Maaf ya, Ko-nii."
        nar "Meski kau buru-buru meralat panggilanmu dan menyendok sup miso, keheningan tipis sudah telanjur turun di antara piring kalian. Sekali saja kau terpeleset keluar dari peran Chiasa, orang yang tinggal satu atap denganmu ini adalah orang pertama yang akan merasakan retakannya."
    else:
        nar "Daripada terlihat kaku karena takut salah bicara, kau memilih bersembunyi di balik sifat asli Chiasa yang paling mencolok. Kau meletakkan kedua siku di atas meja, menopang dagu dengan telapak tangan, lalu memiringkan kepala sambil tersenyum jahil."
        chiasa "Mau dong, Ko-nii~. Tumben pagi-pagi pelayanannya ekstra manis begini. Jangan-jangan Ko-nii ada maunya ya?"
        nar "Bahu Koita tersentak kecil hingga teh di cangkir nyaris tumpah ke tatakan. Ia buru-buru menaruh cangkir itu di depanmu sambil berdeham, telinganya memerah tipis dengan cara yang menunjukkan betapa seringnya ia tak berkutik menghadapi godaan semacam ini."
        koita "Hei, jangan iseng pagi-pagi. Aku kan cuma nyiapin sarapan biar kau nggak telat di hari pertama kuliah."
        chiasa "Masa cuma karena itu? Bukan gara-gara Ko-nii takut mulai hari ini adikmu yang manis bakal sibuk dilirik cowok-cowok dan senior di Fakultas Seni?"
        nar "Tangan Koita yang hendak mengambil roti panggang terhenti di udara. Senyum canggung di wajahnya surut sedikit, digantikan kerutan samar di sela alisnya yang jarang ia tunjukkan."
        koita "...Di jurusan seni kan memang banyak orang yang nyentrik. Kalau ada senior atau cowok seangkatan yang aneh-aneh dan sok akrab, kau harus langsung bilang ke aku. Jangan gampang ikut ajakan orang."
        chiasa "Wah, posesifnya keluar. Tenang saja, Ko-nii."
        nar "Merasa umpanmu sudah cukup untuk menutup kegugupan sekaligus menakar batas reaksinya, kau langsung menegakkan dudukmu kembali dan meraih sumpit untuk memakan telur—mengakhiri godaan itu jauh lebih cepat daripada kebiasaan Chiasa yang asli."
        nar "Perubahan mendadak dari senyum menggoda ke wajah tenang itu membuat Koita terdiam. Ia tidak langsung menyentuh sarapannya, melainkan menatap wajahmu lebih lama dengan sorot mata yang belum sepenuhnya tenang antara kesal karena candaanmu soal pria lain dan bingung melihatmu berhenti begitu saja."
    return

# ┌─ PANDUAN CERITA · C03 · Tanzaku Chiasa
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Tanabata; Chiasa menulis tanzaku (apa pun).
# │ INTI    : A menulis harapan baru / B menyalin harapan asli / C tidak menulis.
# │ AKHIRAN : harapan_pemain; C membuat Haruka bertanya.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C03:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Tanabata")
    nar "Tanzaku menunggu di dekat alat gambar. Kau mengetahui harapan yang biasanya ditulis Chiasa, cukup untuk menyalinnya tanpa berpikir. Justru itu yang membuat pensil tertahan."
    nar "Di luar, Koita menanyakan apakah kertasnya sudah selesai. Kau masih harus menentukan apakah satu keinginan dalam hidup pinjaman ini boleh benar-benar menjadi milikmu."
    call kk_family_menu("C03", ["Tulis harapan baru, milikmu sendiri.", "Salin harapan aslinya persis.", "Biarkan tanzaku itu kosong."])
    if _return == "A":
        nar "Kau menulis harapanmu sendiri, dengan kalimat yang tidak berusaha menyenangkan bayangan tentang siapa Chiasa seharusnya. Kertas itu terasa terlalu kecil untuk menjelaskan perbedaan, cukup luas untuk memulainya."
    elif _return == "B":
        nar "Kau menyalin harapan lama. Koita mengenalinya dan tersenyum, mengira masih melihat adiknya yang sama."
        nar "Kau mendapat keamanan dari rasa percaya itu, bersama ketidaknyamanan bahwa kelegaan seseorang baru saja dibeli dengan mengulangi keinginan yang belum tentu hidup di dalam dirimu."
    else:
        "Haruka" "Tidak menulis? Tidak biasanya kau melewatkan ini."
        nar "Kau membiarkan kosong daripada menyampaikan sesuatu yang tak dapat diakui. Haruka menawarkan pensil lain, mengira masalahnya ada pada alat. Perhatian kecilnya membuat keputusan tidak menjawab terasa lebih terlihat."
    return

# ┌─ PANDUAN CERITA · C04 · "Nacchan-oneechan"
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Nagisa di festival; Chiasa kecil biasa memanggil begitu.
# │ INTI    : A pakai julukan / B pakai nama biasa / C menantang Nagisa.
# │ AKHIRAN : A membangkitkan kenangan; B dingin; C memperkuat rivalitas.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C04:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Festival")
    nar "Nagisa membetulkan tali tas di depan stan festival. Kau mengingat Chiasa kecil pernah memanggilnya Nacchan-oneechan, sebuah kedekatan yang kemudian terkubur oleh rivalitas."
    nar "Panggilan lama itu tersedia dalam pengetahuanmu. Belum jelas apakah mengucapkannya sekarang akan menjadi kebohongan tentang masa lalu atau tawaran hubungan yang baru."
    call kk_family_menu("C04", ["Pakai julukan lama itu.", "Panggil namanya biasa saja.", "Tantang Nagisa dengan sikap dingin."])
    if _return == "A":
        nagisa "...Lama tidak kudengar panggilan itu. Kau masih ingat, ya."
        nar "Ia menurunkan suara, lupa sesaat pada kebiasaan mencari celah untuk membalas. Kau melihat seseorang yang ternyata masih menunggu bagian lama kedekatan itu disebut tanpa ejekan."
    elif _return == "B":
        nagisa "Oh. Kukira kita lebih dekat dari itu."
        nar "Ia segera menambahkan bahwa nama biasa tentu boleh dipakai. Namun langkahnya lebih cepat ketika kalian mulai berjalan lagi, memberi jarak pada harapan kecil yang terlanjur terlihat."
    else:
        nagisa "Begitu caramu sekarang? Baik, aku terima."
        nar "Rivalitas memberimu peran yang mudah ditiru: sindir, balas, jangan mengalah. Di baliknya ada dua perempuan yang mulai sulit mengingat kapan terakhir kali berbicara tanpa mempertahankan tempat di dekat orang lain."
    return

# ┌─ PANDUAN CERITA · C08 · Haruka Curiga
# │ LOKASI  : Kampus Kouseikan · Gedung Seni Rupa & Studio
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : gambar sketsa pemain berubah gaya.
# │ INTI    : A kerjakan lagi dari nol / B beralasan "stres" / C mengaku sebagian.
# │ AKHIRAN : curiga_haruka; risiko rahasia Shena terbongkar.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C08:
    call kk_scene_enter("chiasa", "Gedung Seni Rupa & Studio")
    nar "Haruka menaruh gambar lama dan sketsa barumu di dekat cahaya. Ia tidak menunjuk hasil yang buruk lebih dahulu, melainkan keputusan kecil yang dahulu dibuat Chiasa tanpa berpikir."
    "Haruka" "Bukan cuma kualitas. Caramu mencari bentuknya berbeda. Kamu sedang mencoba sesuatu, atau kesulitan yang belum ingin kamu ceritakan?"
    call kk_family_menu("C08", ["Kerjakan ulang dari nol agar cocok dengan gaya lama.", "Beralasan kau sedang stres.", "Akui sebagian bahwa kau sedang mencoba hal baru."])
    if _return == "A":
        nar "Kau mengulang dari awal, memeriksa contoh sampai sebagian garis tampak lebih dekat dengan kebiasaan lama. Haruka mengangguk, tetapi melihat kerja keras yang sebelumnya tak perlu terlihat untuk hasil serupa."
        "Haruka" "Lebih mendekati. Kamu boleh bilang jika butuh waktu. Aku tidak ingin kamu mengira harus menyembunyikan setiap kesulitan agar tetap dianggap Chiasa."
    elif _return == "B":
        "Haruka" "Stres... mungkin. Tapi garis tidak biasanya berbohong."
        nar "Ia tidak menolak alasanmu, hanya menanyakan apa yang dapat dibantu. Kebohongan pendek itu kini memerlukan jawaban yang harus cukup meyakinkan untuk kepedulian seseorang yang tidak sedang mencari kesalahan."
    else:
        "Haruka" "Hal baru, ya. Akan kuperhatikan ke mana arahnya."
        nar "Kau mengakui sebagian perubahan tanpa membuka seluruh identitasmu. Haruka memberi ruang untuk mencoba, tetapi meminta jangan menjanjikan hasil profesional sebelum kau sendiri tahu kemampuan yang ada sekarang."
    return

init 1 python:
    _hook("C02-A", lambda: kk_suspect("koita", -3))
    _hook("C02-B", lambda: kk_suspect("koita", 8))
    _hook("C02-C", lambda: kk_rel("koita","jeal",5))
    _hook("C03-A", lambda: kk_flag("harapan_pemain_baru"))
    _hook("C03-C", lambda: kk_suspect("haruka", 5))
    _hook("C04-A", lambda: kk_rel("nagisa","intim",3))
    _hook("C04-B", lambda: kk_rel("nagisa","trust",-3))
    _hook("C04-C", lambda: kk_rel("nagisa","jeal",4))
    _hook("C08-A", lambda: kk_suspect("haruka", -3))
    _hook("C08-B", lambda: kk_suspect("haruka", 6))
    _hook("C08-C", lambda: (kk_suspect("haruka", 3), kk_flag("shena_hampir_terbongkar")))
