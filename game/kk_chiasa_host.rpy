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
    nar "Kau menuruni tangga kayu rumah keluarga Amamiya yang berderit pelan di bawah pijakan kakimu. Rasanya masih ganjil merasakan langkah yang lebih pendek, ayunan rambut cokelat panjang yang terikat setengah dengan pita hitam di belakang kepala, serta udara pagi 7 April yang sejuk menyapu pergelangan kakimu."
    nar "Begitu kau melangkah masuk ke ruang makan, aroma kaldu miso hangat, roti panggang yang baru menyembul dari pemanggang, dan wangi telur mata sapi langsung memenuhi udara. Cahaya matahari pagi jatuh miring melalui tirai tipis jendela dapur, menerangi meja makan kayu yang sudah tertata rapi."
    nar "Di dekat meja dapur, seorang pemuda berambut hitam agak acak-acakan dengan satu helai rambut mencuat di puncak kepalanya berdiri mengenakan celemek rumahan di atas kaus abu-abu. Amamiya Koita—sang protagonis manga harem yang selama ini hanya kau lihat di balik panel hitam-putih."
    nar "Ia meletakkan dua piring berisi telur mata sapi dan roti panggang beserta dua mangkuk sup miso di atas meja, lalu menoleh setengah badan ke arah teko di dekat kompor sambil tersenyum hangat—senyum yang tampak begitu tulus dan biasa-biasa saja."
    koita "Sudah bangun? Bagus deh, pas banget baru matang. Duduk dulu saja—tehnya mau kubuatkan seperti biasa sekalian?"
    nar "Kau menarik kursi kayu dan duduk, tetapi pertanyaan ringan itu membuatmu terdiam sepersekian detik. Kau sama sekali tidak tahu 'seperti biasa' versi Chiasa itu teh hijau tawar, teh hitam, atau teh susu—sampai kau melihat tangan Koita sendiri sudah lebih dulu meraih cangkir keramik kuning bermotif kucing dari rak piring dan menjatuhkan satu dadu gula ke dalamnya."
    nar "Ia bertanya hanya karena kebiasaan bertahun-tahun, bukan karena ia tidak tahu. Kini ia berdiri di depan kompor sambil menuangkan air panas dari teko, menunggu jawabanmu."
    nar "Dulu, ketika kau membaca manga ini di layar ponsel, panggilan manja Chiasa untuk kakak tirinya hanyalah deretan huruf cetak di dalam balon dialog yang lewat dalam sedetik. Sekarang, di ruang makan yang jaraknya tak sampai dua meter ini, sebutan itu harus keluar dari kerongkonganmu sendiri tanpa terdengar seperti orang asing yang sedang menghafal naskah."
    call kk_family_menu("C02", ["\"Iya, makasih ya, Ko-nii. Kayak biasa aja.\"", "\"Iya, tolong. Makasih, Koita.\"", "\"Mau dong, Ko-nii~. Tumben pagi-pagi manis banget.\""])
    if _return == "A":
        nar "Kau menarik napas pendek tanpa suara, melemaskan bahu yang sempat menegang, lalu membiarkan pita suara tubuh ini melantunkan nada ringan yang paling sering diucapkannya."
        chiasa "Iya, makasih ya, Ko-nii. Kayak biasa aja."
        nar "Gerakan tangan Koita yang sedang mengaduk sendok di cangkir kuning itu tidak terhenti sedikit pun. Ia berjalan menghampiri meja, menaruh teh hangat tersebut di sisi kanan piringmu sambil tersenyum lega, lalu melepas tali celemeknya dan menggantungkannya di sandaran kursi."
        koita "Pagi, Chi-chan. Tumben banget hari ini sudah rapi dan turun tepat waktu. Biasanya hari pertama semester pun kau masih harus kugedor sampai tiga kali baru mau lepas dari guling."
        chiasa "Hari pertama kuliah kan beda sama SMA, Ko-nii. Kalau aku telat di hari orientasi fakultas, nanti kesannya buruk."
        koita "Haha, tumben bijak. Ngomong-ngomong, Ibu kirim pesan lagi subuh tadi sebelum berangkat sama Ayah. Katanya lauk di kotak plastik biru di rak tengah kulkas harus dihabiskan hari ini biar nggak keburu basi."
        nar "Koita duduk di kursi seberang, merapatkan kedua tangannya singkat sebelum mengambil sumpit. Kau ikut meraih sumpitmu dan menyumpit sepotong telur, diam-diam mencatat setiap petunjuk hidup sehari-hari yang baru saja ia serahkan secara cuma-cuma—letak kotak makan di kulkas, kebiasaan bangun tidur pemilik tubuh ini, hingga posisi orang tua mereka yang sedang bepergian."
        koita "Oh iya, nanti kita berangkat bareng sampai stasiun seperti biasa, kan? Gedung Fakultas Seni Rupa agak jauh di sayap barat kampus, jadi lumayan makan waktu kalau jalan santai."
        chiasa "Iya, nanti aku siap sebentar lagi habis makan."
        koita "Kalau habis acara pembukaan kau masih bingung cari ruang studio atau malas jalan sendirian, tunggu saja di dekat kantin utama atau kirim pesan ke aku. Jam kuliah Sastraku hari ini cuma sampai siang kok."
        chiasa "Gampang. Ko-nii nggak usah terlalu khawatir begitu."
        nar "Panggilan itu diterima begitu mulus sampai kau justru merasa semakin ganjil. Koita terus bercerita santai tentang jadwal kelas dan rencana mampir ke toko buku bekas sambil mengunyah roti panggangnya—sama sekali tidak menyadari bahwa gadis di seberang mejanya sedang memunguti serpihan informasi dari percakapan biasa demi bertahan hidup di dalam tubuh adiknya."
    elif _return == "B":
        nar "Lidahmu terasa kelu dan enggan memaksa tubuh ini mengucapkan panggilan semanja itu kepada protagonis manga yang paling tidak kau sukai. Sebelum kau sempat menimbang akibatnya, kalimat yang meluncur dari bibirmu justru terdengar datar dan lugas."
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

# ┌─ PANDUAN CERITA · C03 · Tanzaku Chiasa
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Tanabata; Chiasa menulis tanzaku (apa pun).
# │ INTI    : A menulis harapan baru / B menyalin harapan asli / C tidak menulis.
# │ AKHIRAN : harapan_pemain; C membuat Haruka bertanya.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C03:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Tanabata")
    nar "Sore awal Juli yang hangat di rumah keluarga Amamiya. Jendela kamarmu terbuka separuh, membiarkan suara serangga musim panas dari pekarangan dan embusan angin tipis menggoyangkan tirai putih di samping meja belajar."
    nar "Di atas meja kayu di hadapanmu—di antara deretan buku sketsa, pena drawing, dan spidol warna milik pemilik tubuh ini yang nyaris tak pernah kausentuh—tergeletak selembar kertas tanzaku kuning pucat lengkap dengan seutas benang tipis. Di bawahnya, terselip sebuah tanzaku lama dari tahun lalu yang rupanya pernah dipakai Chiasa sebagai pembatas halaman di buku sketsanya."
    nar "Kau memandangi tulisan tangan rapi di kertas lama itu: sebuah harapan pendek dan manis tentang ingin selalu tinggal di sisi kakak tirinya dan tidak pernah berubah. Kau bahkan tidak perlu menebak-nebak—kalau kau mau aman, kau tinggal menyalinnya persis seperti tahun-tahun sebelumnya."
    nar "Justru karena terlalu mudah untuk disalin itulah ujung pensil di tanganmu tertahan di atas kertas kosong."
    nar "Dari balik pintu kamar yang sedikit terbuka, suara langkah di lorong terdengar mendekat, disusul ketukan pelan dua kali."
    koita "Chi-chan, kertasmu sudah selesai belum? Cabang bambunya sudah kutaruh di beranda bawah, Haruka juga baru datang bantu menata tali-talinya."
    chiasa "Sebentar lagi, Ko-nii! Tunggu lima menit!"
    koita "Oke, santai saja. Jangan kelamaan mikir, nanti keburu gelap."
    nar "Langkah Koita kembali menjauh menuruni tangga kayu. Ruangan kembali sunyi, menyisakan kertas tanzaku kosong yang menatapmu balik di atas meja."
    nar "Tubuh ini pinjaman, nama ini pinjaman, bahkan kamar penuh alat gambar ini bukan milikmu. Kau masih harus memutuskan apakah di tengah semua peran yang harus kau jalani ini, satu harapan kecil di atas kertas tipis boleh benar-benar menjadi milikmu sendiri—atau sebaiknya tetap dikubur di balik bayangan Chiasa."
    call kk_family_menu("C03", ["Tulis harapan baru, milikmu sendiri.", "Salin harapan aslinya persis.", "Biarkan tanzaku itu kosong."])
    if _return == "A":
        nar "Kau menutup buku sketsa lama itu perlahan, menyingkirkan kertas tanzaku tahun lalu dari pandanganmu, lalu menekan ujung pensil ke permukaan kertas kuning yang masih bersih."
        nar "Tanpa berusaha meniru gaya bahasa manis ataupun memikirkan kalimat apa yang akan membuat Koita tersenyum, kau menuliskan satu baris pendek dengan tulisanmu sendiri: semoga aku bisa melewati semua ini dengan caraku sendiri, dan tetap utuh sampai akhir."
        nar "Garis hurufnya memang sedikit kaku dibandingkan tulisan rapi di buku catatan Chiasa, tetapi untuk pertama kalinya sejak bangun di dunia ini, kalimat di depanmu tidak terasa seperti naskah hafalan."
        nar "Kau mengikat benang tipis di ujung kertas itu, lalu turun ke beranda belakang. Di sana, Koita dan Haruka sedang menggantung beberapa kertas warna-warni di dahan bambu kecil yang ditaruh di sudut teras."
        koita "Nah, akhirnya turun juga. Sini, gantung di dahan atas biar nggak ketutupan punya orang lain—eh, boleh lihat kamu nulis apa, Chi-chan?"
        chiasa "Rahasia dong, Ko-nii. Kalau dibaca orang duluan, nanti nggak terkabul."
        nar "Kau langsung mengikat kertasmu di dahan samping dengan cepat sambil tersenyum ringan. Koita tertawa kecil dan mengangkat kedua tangan menyerah, sementara Haruka di sebelahnya hanya tersenyum tipis melihat tingkah kalian."
        nar "Saat angin sore kembali bertiup dan membuat kertas kuning itu berayun pelan di antara daun bambu, kau tahu selembar kertas kecil terlalu sempit untuk menjelaskan siapa dirimu sebenarnya—tetapi cukup luas untuk mulai mengakui bahwa kau ada di sini."
    elif _return == "B":
        nar "Kau menatap kertas tanzaku lama di samping buku sketsa selama dua detik, lalu menarik napas pendek. Bermain aman jauh lebih masuk akal daripada memancing pertanyaan yang tidak perlu di dalam rumah sendiri."
        nar "Dengan gerakan hati-hati, kau menyalin harapan lama Chiasa nyaris kata demi kata—menjaga nada manis dan keinginan untuk tetap seperti ini agar tidak ada satu pun yang merasa ganjil."
        nar "Ketika kau turun ke beranda belakang dan menggantungkannya di dahan bambu, Koita yang berdiri di sebelahmu sempat melirik sekilas sebelum kertas itu terlipat angin. Senyum hangat yang begitu lega langsung merekah di wajahnya."
        koita "Haha... ternyata tahun ini masih mirip yang dulu, ya, Chi-chan. Nggak berubah sama sekali."
        chiasa "Memangnya kenapa kalau mirip? Kan memang itu yang kepikiran."
        koita "Nggak apa-apa, justru aku senang. Kadang-kadang setelah masuk kuliah, aku takut kita berdua jadi makin jarang punya waktu bareng di rumah."
        nar "Ia menepuk puncak kepalamu ringan sebelum berbalik membantu Haruka merapikan pita di dahan bawah."
        nar "Kau mendapatkan rasa aman yang kaucari—tidak ada kecurigaan, tidak ada celah, penyamaranmu utuh sempurna. Namun saat menatap kertas kuning yang berayun pelan di dahan bambu itu, ada rasa hambar yang mengganjal di dada: kelegaan seseorang baru saja kaubeli dengan mengulang sebuah keinginan yang sama sekali tidak hidup di dalam dirimu."
    else:
        nar "Ujung pensilmu berhenti beberapa milimeter di atas kertas kuning itu, lalu perlahan kau meletakkannya kembali ke atas meja. Menulis harapan milik orang lain terasa seperti kebohongan yang tidak perlu, sementara menulis harapanmu sendiri di rumah ini terasa terlalu jujur."
        nar "Kau mengambil kertas tanzaku yang masih kosong itu, mengikat benangnya seadanya, lalu melangkah turun ke beranda belakang. Koita sedang sibuk menata ulang posisi pot bambu di sudut teras, sehingga yang pertama menyadari kertas di tanganmu justru Haruka."
        "Haruka" "Eh—Chiasa? Kertasmu masih kosong? Tidak menulis apa-apa?"
        nar "Suaranya tidak menuduh, hanya penuh keheranan yang tulus. Ia melangkah mendekat sambil menatap kertas polos di jari-jarimu."
        "Haruka" "Tidak biasanya kamu melewatkan ini. Tahun lalu kamu bahkan sampai menghabiskan dua lembar karena merasa tulisannya kurang rapi. Pensilmu di atas tumpul atau habis isinya? Ini, pakai spidolku saja kalau mau."
        nar "Haruka menyodorkan spidol hitam tipis ke arahmu dengan senyum ramah, mengira masalahnya sekadar alat tulis. Koita yang mendengar obrolan itu ikut menoleh dari dekat pot bambu."
        koita "Lho, beneran belum ditulis, Chi-chan?"
        chiasa "Ah... nggak kok, bukan soal pensilnya. Cuma tahun ini aku lagi nggak kepikiran mau minta apa-apa saja. Rasanya nggak perlu dipaksakan kalau memang belum ada."
        "Haruka" "...Begitu ya."
        nar "Haruka menarik kembali spidolnya perlahan, mengangguk sopan—tetapi tatapannya sempat tertahan di wajahmu satu detik lebih lama dari biasanya, seolah sedang mencoba mencocokkan jawaban datar barusan dengan Chiasa yang selama ini ia kenal."
        nar "Justru karena perhatian kecilnya yang begitu tulus, keputusanmu untuk tidak menulis apa-apa malah terasa jauh lebih mencolok daripada yang kau kira."
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
    nar "Lampion kertas merah dan putih berjajar sepanjang jalan menuju halaman kuil festival musim panas, memantulkan cahaya hangat di atas kerumunan pengunjung yang mengenakan yukata. Bau manis permen kapas, saus takoyaki yang dipanggang di atas pelat besi, dan suara teriakan penjaga stan ikan mas bercampur dalam udara malam Agustus yang gerah."
    nar "Beberapa langkah di depan sebuah stan suvenir kayu, Sakurajima Nagisa berdiri sambil membetulkan tali tas serut kainnya. Malam ini ia mengenakan yukata bernuansa cerah yang kontras dengan twin-tail pirang keemasannya; gantungan kunci kelinci kecil yang biasa menempel di tas kuliahnya ikut ia pindahkan ke pegangan tas festival."
    nar "Ketika kau berjalan mendekat, kau teringat selintas ucapan Koita di rumah tadi sore sambil tertawa kecil saat melihat foto lama di ruang tamu—bahwa dulu sewaktu kecil, Chiasa selalu menempel di lengan yukata Nagisa setiap kali festival tiba dan memanggilnya 'Nacchan-oneechan'."
    nar "Kedekatan itu rupanya pelan-pelan terkubur seiring mereka tumbuh besar dan mulai berdiri di sisi yang saling menjaga jarak, bahkan bersaing diam-diam di sekitar Koita."
    nar "Nagisa menoleh saat menyadari langkahmu berhenti di sampingnya. Alisnya sedikit terangkat, ekspresi siaga yang biasa ia pasang di depanmu langsung muncul hampir tanpa sadar."
    nagisa "Oh, Chiasa. Kirain kamu masih di belakang bareng yang lain. Ramai banget ya malam ini—kalau jalan kepisah nanti susah nyarinya."
    nar "Panggilan lama 'Nacchan-oneechan' itu kini ada di ujung lidahmu. Kau sendiri tidak benar-benar memiliki kenangan masa kecil tersebut; belum jelas apakah mengucapkannya sekarang akan menjadi kebohongan yang manis tentang masa lalu, atau justru tawaran jujur untuk memulai kedekatan yang baru."
    call kk_family_menu("C04", ["Pakai julukan lama itu.", "Panggil namanya biasa saja.", "Tantang Nagisa dengan sikap dingin."])
    if _return == "A":
        nar "Kau tidak memasang senyum jahil seperti biasanya. Dengan nada ringan yang justru terasa tenang dan tanpa ejekan, kau memiringkan kepala sedikit sambil menatapnya."
        chiasa "Kalau begitu aku jalan di sebelahmu saja supaya nggak kepisah di kerumunan, Nacchan-oneechan."
        nar "Seketika, gerakan tangan Nagisa yang sedang merapikan tali tas serutnya langsung berhenti total. Mata biru cerahnya mengerjap dua kali dengan raut kaget yang sama sekali tak sempat ia sembunyikan."
        nagisa "...Eh? Tunggu—barusan kamu manggil apa?"
        chiasa "Nacchan-oneechan. Kenapa? Aneh ya kalau kupanggil begitu lagi di festival?"
        nar "Untuk beberapa detik, seluruh sikap defensif dan kebiasaan mencari celah untuk membalas sindiran mendadak lenyap dari wajah Nagisa. Rona merah tipis merambat ke ujung telinganya, dan ketika ia akhirnya berbicara lagi, suaranya turun jauh lebih pelan daripada biasanya."
        nagisa "...Lama banget nggak kudengar panggilan itu. Kupikir kamu sudah lupa—atau sudah malas memakainya sejak kita masuk SMA."
        chiasa "Masa lupa. Dulu kan aku yang paling sering narik lengan yukatamu biar nggak ketinggalan."
        nagisa "Iya, sampai lengan yukataku melar sebelah... dasar."
        nar "Bibirnya melengkung menjadi senyum kecil yang hangat dan jauh dari kesan galak. Ia menggeser langkahnya setengah tapak lebih dekat ke sisimu sambil melirik deretan stan di depan."
        nagisa "Ya sudah, ayo jalan duluan ke stan dekat tangga kuil. Jangan sampai hilang lagi di kerumunan, Chi-chan."
        nar "Di tengah riuh lampion malam itu, kau melihat sisi Nagisa yang jarang sekali terlihat—seseorang yang ternyata selama ini masih menunggu potongan lama kedekatan itu disebut kembali tanpa sedikit pun ejekan."
    elif _return == "B":
        nar "Kau memutuskan tidak memakai panggilan masa kecil yang kenangannya bahkan bukan milikmu. Kau mengangguk singkat dengan senyum sopan yang terjaga."
        chiasa "Iya, ramai banget, Nagisa-senpai. Ayo jalan bareng saja supaya nggak kepisah dari rombongan."
        nar "Ada jeda sepersekian detik di wajah Nagisa. Matanya sempat berkedip kecil—seolah di antara cahaya lampion festival yang sama seperti tahun-tahun dulu, ia sempat tanpa sadar mengharapkan sesuatu yang sedikit lebih akrab dari sekadar sapaan formal."
        nagisa "...Oh. 'Nagisa-senpai', ya. Kukira di luar kampus begini kita lebih dekat dari itu."
        chiasa "Eh—maksudku biar sopan saja di depan orang banyak."
        nar "Nagisa segera mengibaskan satu tangannya cepat-cepat, berusaha menutupi kecewa kecil yang tadi sempat terlanjur terlihat."
        nagisa "Nggak apa-apa kok! Tentu saja boleh panggil biasa begitu, memang itu kan yang benar. Ayo, nanti kita ketinggalan tempat bagus buat nonton kembang api."
        nar "Ia langsung berbalik dan melangkah lebih cepat menyusuri jalan setapak di antara stan-stan makanan, menjaga jarak dua langkah di depanmu—seolah memberi pagar yang rapi bagi harapan kecil yang baru saja ia tarik kembali."
    else:
        nar "Daripada berpura-pura akrab atau bersikap sopan yang kaku, kau membiarkan sudut bibirmu terangkat tipis—senyum dingin yang terasa sangat cocok dengan peran rival yang selama ini ia waspadai."
        chiasa "Tenang saja, Nagisa-senpai, aku nggak gampang tersesat kok. Lagipula aku memang sengaja jalan di depan supaya nggak ketinggalan sama Ko-nii nanti."
        nar "Alis Nagisa langsung menukik tajam. Ketegangan yang tadi hanya samar di bahunya seketika mengeras penuh, dan sorot matanya yang biru cerah menyala menatapmu lurus-lurus."
        nagisa "Oh... begitu caramu sekarang? Langsung terang-terangan ya. Baik, aku terima."
        chiasa "Aku cuma bilang kenyataannya. Kalau Senpai mau jalan pelan-pelan di belakang, silakan saja."
        nagisa "Siapa juga yang mau jalan pelan-pelan! Lihat saja siapa yang sampai duluan di tepi sungai!"
        nar "Ia langsung memutar tumit dan berjalan cepat di sisimu dengan langkah yang sama sekali tidak mau kalah. Rivalitas ternyata memberimu peran yang paling mudah ditiru di dunia ini: sindir, balas, jangan pernah mengalah."
        nar "Namun di balik langkah cepat dan kalimat tajam yang saling kalian lempar di bawah lampion merah itu, ada sesuatu yang terasa dingin—dua perempuan yang mulai lupa kapan terakhir kali mereka bisa berbicara tanpa harus mempertahankan tempat di dekat orang lain."
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
