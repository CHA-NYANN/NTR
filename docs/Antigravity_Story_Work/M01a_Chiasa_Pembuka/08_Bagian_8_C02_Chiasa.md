# Bagian 8 — `C02` (*"Ko-nii?"*) · Host Chiasa (M01a)

Target File: `game/kk_chiasa_host.rpy` (`label kkscene_C02`)

```renpy
label kkscene_C02:
    call kk_scene_enter("chiasa", "Rumah Amamiya")
    nar "Kau menuruni tangga kayu rumah keluarga Amamiya yang berderit pelan di bawah pijakan kakimu. Rasanya masih ganjil merasakan langkah yang lebih pendek, ayunan rambut cokelat panjang yang terikat setengah dengan pita hitam di belakang kepala, serta udara pagi 7 April yang sejuk menyapu pergelangan kakimu."
    nar "Begitu kau melangkah masuk ke ruang makan, aroma kaldu miso hangat, roti panggang yang baru menyembul dari pemanggang, dan wangi telur mata sapi langsung memenuhi udara. Cahaya matahari pagi jatuh miring melalui tirai tipis jendela dapur, menerangi meja makan kayu yang sudah tertata rapi."
    nar "Di dekat meja dapur, seorang pemuda berambut hitam agak acak-acakan dengan satu helai rambut mencuat di puncak kepalanya berdiri mengenakan celemek rumahan di atas kaus abu-abu. Amamiya Koita—sang MC manga harem yang selama ini hanya kau lihat di balik panel hitam-putih."
    nar "Ia meletakkan dua piring berisi telur mata sapi dan roti panggang beserta dua mangkuk sup miso di atas meja, lalu menoleh setengah badan ke arah teko di dekat kompor sambil tersenyum hangat—senyum yang tampak begitu tulus dan biasa-biasa saja."
    koita "Sudah bangun? Bagus deh, pas banget baru matang. Duduk dulu saja—tehnya mau kubuatkan seperti biasa sekalian?"
    nar "Kau menarik kursi kayu dan duduk, tetapi pertanyaan ringan itu membuatmu terdiam sepersekian detik. Kau sama sekali tidak tahu 'seperti biasa' versi Chiasa itu teh hijau tawar, teh hitam, atau teh susu—sampai kau melihat tangan Koita sendiri sudah lebih dulu meraih cangkir keramik kuning bermotif kucing dari rak piring dan menjatuhkan satu dadu gula ke dalamnya."
    nar "Ia bertanya hanya karena kebiasaan bertahun-tahun, bukan karena ia tidak tahu. Kini ia berdiri di depan kompor sambil menuangkan air panas dari teko, menunggu jawabanmu."
    nar "Dulu, ketika kau membaca manga ini di layar ponsel, panggilan manja Chiasa untuk kakak tirinya hanyalah deretan huruf cetak di dalam balon dialog yang lewat dalam sedetik. Sekarang, di ruang makan yang jaraknya tak sampai dua meter ini, sebutan itu harus keluar dari kerongkonganmu sendiri tanpa terdengar seperti orang asing yang sedang menghafal naskah."
    call kk_family_menu("C02", ["Panggil 'Ko-nii' dengan natural.", "Panggil namanya saja.", "Goda ia seperti Chiasa asli biasanya."])
    if _return == "A":
        nar "Kau menarik napas pendek tanpa suara, melemaskan bahu yang sempat menegang, lalu membiarkan pita suara tubuh ini melantunkan nada ringan yang paling sering diucapkannya."
        chiasa "Iya, makasih ya, Ko-nii. Kayak biasa aja."
        nar "Gerakan tangan Koita yang sedang mengaduk sendok di cangkir kuning itu tidak terhenti sedikit pun. Ia berjalan menghampiri meja, menaruh teh hangat tersebut di sisi kanan piringmu sambil tersenyum lega, lalu melepas tali celemeknya dan menggantungkannya di sandaran kursi."
        koita "Pagi, Chiasa. Tumben banget hari ini sudah rapi dan turun tepat waktu. Biasanya hari pertama semester pun kau masih harus kugedor sampai tiga kali baru mau lepas dari guling."
        chiasa "Hari pertama kuliah kan beda sama SMA, Ko-nii. Kalau aku telat di hari orientasi fakultas, nanti kesannya buruk."
        koita "Haha, tumben bijak. Ngomong-ngomong, Ibu kirim pesan lagi subuh tadi sebelum berangkat sama Ayah. Katanya lauk di kotak plastik biru di rak tengah kulkas harus dihabiskan hari ini biar nggak keburu basi."
        nar "Koita duduk di kursi seberang, merapatkan kedua tangannya singkat sebelum mengambil sumpit. Kau ikut meraih sumpitmu dan menyumpit sepotong telur, diam-diam mencatat setiap petunjuk hidup sehari-hari yang baru saja ia serahkan secara cuma-cuma—letak kotak makan di kulkas, kebiasaan bangun tidur pemilik tubuh ini, hingga posisi orang tua mereka yang sedang bepergian."
        koita "Oh iya, nanti kita berangkat bareng sampai stasiun seperti biasa, kan? Gedung Fakultas Seni Rupa agak jauh di sayap barat kampus, jadi lumayan makan waktu kalau jalan santai."
        chiasa "Iya, nanti aku siap sebentar lagi habis makan."
        koita "Kalau habis acara pembukaan kau masih bingung cari ruang studio atau malas jalan sendirian, tunggu saja di dekat kantin utama atau kirim pesan ke aku. Jam kuliah Sastraku hari ini cuma sampai siang kok."
        chiasa "Gampang. Ko-nii nggak usah terlalu khawatir begitu."
        nar "Panggilan itu diterima begitu mulus sampai kau justru merasa semakin ganjil. Koita terus bercerita santai tentang jadwal kelas dan rencana mampir ke toko buku bekas sambil mengunyah roti panggangnya—sama sekali tidak menyadari bahwa gadis di seberang mejanya sedang memunguti serpihan informasi dari percakapan biasa demi bertahan hidup di dalam tubuh adiknya."
    elif _return == "B":
        nar "Lidahmu terasa kelu dan enggan memaksa tubuh ini mengucapkan panggilan semanja itu kepada MC manga yang paling tidak kau sukai. Sebelum kau sempat menimbang akibatnya, kalimat yang meluncur dari bibirmu justru terdengar datar dan lugas."
        chiasa "Iya, tolong. Makasih, Koita."
        nar "Bunyi kucuran air panas dari moncong teko mendadak terhenti. Tangan Koita membeku di udara selama dua detik penuh sebelum ia meletakkan teko itu kembali ke atas kompor dan menoleh perlahan ke arahmu dengan kening berkerut."
        koita "...'Koita'? Tumben sekali. Sejak kapan kau memanggilku pakai nama langsung begitu?"
        nar "Ia mengeluarkan tawa pendek yang terdengar canggung, mengambil cangkir kuning bermotif kucing itu, lalu berjalan ke meja dan menaruhnya di sebelah piringmu sambil menatap wajahmu seolah sedang menunggu kelanjutan dari sebuah lelucon pagi."
        nar "Jemari tangan kananmu refleks terangkat menyentuh ujung pita hitam di rambutmu. Kau baru menyadari betapa fatalnya satu kata itu ketika seluruh kedekatan di dalam rumah ini rupanya berdiri di atas cara Chiasa menyebut namanya."
        chiasa "A-ah, itu... aku kan mulai hari ini sudah jadi mahasiswi, bukan anak SMA lagi. Cuma pengin coba kedengaran lebih dewasa saja."
        koita "Apaan sih, bukannya terdengar dewasa, itu malah kedengaran dingin kayak orang asing tahu nggak? Kupikir tadi kau bangun tidur langsung marah gara-gara sesuatu."
        nar "Koita melepas celemeknya dan duduk di kursi seberang sambil mencoba tersenyum tipis. Namun ketika ia meraih sumpit dan mulai menyendok sup miso, caranya menatapmu jelas tidak lagi sesantai beberapa menit lalu—matanya sempat singgah di wajahmu dua kali lebih lama."
        koita "Kalau kau lagi nggak enak badan, kurang tidur, atau kepikiran soal kampus baru, bilang saja ke aku lho, Chi-chan. Jangan dipendam sendiri."
        chiasa "Nggak kok, sungguh. Cuma masih agak setengah mengantuk saja tadi. Maaf ya, Ko-nii."
        nar "Begitu kau buru-buru meralat panggilanmu dan menunduk menyendok sup miso, bahu Koita baru tampak sedikit mengendur. Meski ia mengangguk dan kembali menyantap rotinya, keheningan tipis sudah telanjur turun di antara piring kalian."
        nar "Satu pelajaran penting langsung tertanam di kepalamu pagi ini: sekali saja kau terpeleset keluar dari peran Chiasa, orang yang tinggal satu atap denganmu ini adalah orang pertama yang akan merasakan retakannya."
    else:
        nar "Daripada terlihat kaku dan mencurigakan karena terlalu berhati-hati, kau memutuskan bersembunyi tepat di balik sifat asli Chiasa yang paling mencolok. Kau meletakkan kedua sikumu di atas meja makan, menopang dagu dengan kedua telapak tangan, lalu memiringkan kepala sedikit sambil menarik sudut bibirmu menjadi senyum jahil."
        chiasa "Mau dong, Ko-nii~. Tumben pagi-pagi pelayanannya ekstra manis begini. Jangan-jangan Ko-nii lagi ada maunya ya?"
        nar "Bahu Koita tersentak kecil hingga teh panas di dalam cangkir kuning itu nyaris menyentuh bibir tatakan. Ia buru-buru melangkah ke meja dan menaruh cangkir itu di depanmu sambil berdeham, ujung telinganya memerah tipis dengan cara yang langsung memperlihatkan betapa seringnya ia tak berkutik menghadapi godaan semacam ini."
        koita "Hei, jangan iseng pagi-pagi begini dong. Aku kan cuma nyiapin sarapan biar kau nggak telat di hari pertama kuliah."
        nar "Melihat reaksinya yang begitu mudah dibaca, kau mendorong umpan itu selangkah lebih jauh untuk menakar seberapa jauh kendali Chiasa atas kakak tirinya."
        chiasa "Masa cuma karena itu? Bukan gara-gara Ko-nii takut mulai hari ini adikmu yang manis bakal sibuk dilirik cowok-cowok dan senior di Fakultas Seni?"
        nar "Tangan Koita yang baru saja hendak mengambil potongan roti panggang dari piringnya langsung terhenti di udara. Senyum canggung yang tadi tersisa di wajahnya surut sedikit, digantikan kerutan samar di sela alisnya yang jarang sekali ia tunjukkan."
        nar "Ia menarik tangannya kembali dari roti, lalu menatapmu dari seberang meja dengan nada bicara yang mendadak lebih rendah dan serius."
        koita "...Di jurusan seni kan memang banyak orang yang nyentrik dan suka asal akrab. Kalau ada senior atau cowok seangkatan yang aneh-aneh dan mulai terlalu dekat, kau harus langsung bilang ke aku. Jangan gampang ikut ajakan orang cuma karena nggak enak menolak."
        chiasa "Wah, posesifnya keluar juga. Tenang saja, Ko-nii."
        nar "Merasa umpanmu sudah lebih dari cukup untuk menutupi kegugupan sekaligus memancing batas reaksinya, kau langsung menegakkan dudukmu, menjatuhkan senyum jahilmu sepenuhnya, lalu meraih sumpit untuk memakan telur mata sapi dengan tenang—mengakhiri godaan itu jauh lebih cepat daripada kebiasaan Chiasa yang asli."
        nar "Perpindahan mendadak dari senyum menggoda ke wajah datar yang tenang itu membuat Koita terdiam di kursinya. Ia tidak langsung menyentuh sarapannya, melainkan menatap wajahmu beberapa detik lebih lama dengan sorot mata yang belum sepenuhnya tenang—terjebak di antara rasa kesal yang baru saja terpancing soal pria lain, dan kebingungan melihatmu berhenti secepat itu."
    return
```
