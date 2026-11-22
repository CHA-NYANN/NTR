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
    if kk_slot == 0:
        nar "Kamu menuruni tangga kayu rumah keluarga Amamiya dengan langkah pelan, secara otomatis melangkahi anak tangga kelima yang papannya agak berderit seperti ingatan otot yang tertinggal di tungkai kaki ini. Rasanya masih ganjil menyesuaikan diri dengan jangkauan langkah yang lebih pendek, ayunan rambut cokelat panjang yang terikat setengah dengan pita hitam di belakang kepala, serta udara pagi awal musim semi yang sejuk."
        nar "Begitu kamu melewati lorong pendek dan melangkah masuk ke ruang makan, aroma kaldu miso hangat, roti panggang yang baru menyembul dari pemanggang, dan wangi telur mata sapi langsung memenuhi udara. Cahaya matahari pagi jatuh miring melalui tirai tipis jendela dapur, menerangi meja makan kayu yang sudah tertata rapi untuk dua orang."
        nar "Di atas meja tergeletak dua piring lauk hangat, dua mangkuk sup miso yang masih mengepul tipis, sepiring irisan kubis renyah, serta kotak plastik biru berisi rebusan sayur kiriman ibu tiri mereka yang baru saja dikeluarkan dari kulkas."
    else:
        nar "Begitu kamu membuka pintu rumah keluarga Amamiya dan melepas sepatu di genkan, suasana tenang ruang dalam langsung menyambutmu. Kamu menata sepatumu sejajar di tepi rak kayu, lalu mengenakan sandal rumah yang terasa terlalu mungil setiap kali kakimu melangkah. Rasanya masih ganjil berjalan dengan langkah yang lebih pendek dan ayunan rambut cokelat panjang berpita hitam di dalam rumah yang seharusnya terasa akrab."
        nar "Saat kamu melangkah masuk ke ruang makan, lampu gantung kuning di atas meja sudah menyala lembut. Aroma kaldu miso hangat, tumis sayur, dan lauk rumahan yang baru saja dihangatkan langsung memenuhi udara. Meja makan kayu sudah tertata rapi untuk dua orang, lengkap dengan kotak plastik biru berisi lauk kiriman dari kulkas."
    nar "Di dekat meja dapur, seorang pemuda berambut hitam agak acak-acakan berdiri mengenakan celemek rumahan berwarna biru pudar di atas kaus abu-abu. Dialah Amamiya Koita, sang protagonis utama manga yang dulu hanya kamu lihat di balik panel gambar, kini berdiri nyata kurang dari dua meter di hadapanmu."
    nar "Ia meletakkan dua mangkuk nasi hangat di atas meja, menyeka kedua tangannya pada lap kain kecil, lalu menoleh setengah badan ke arah teko di dekat kompor sambil tersenyum ringan."
    if kk_slot == 0:
        koita "Sudah bangun? Bagus deh, baru saja matang semua. Semalam nggak begadang sampai lewat tengah malam lagi, kan? Tadi kulihat lampu kamarmu masih nyala lumayan lama."
        chiasa "Cuma beres-beres perlengkapan kuliah sedikit saja. Belum terlalu malam kok."
        koita "Syukurlah kalau begitu. Awal semester begini paling gampang kecapekan kalau jam tidurnya berantakan. Duduk dulu saja, Chi-chan, nanti supnya keburu dingin."
    else:
        koita "Oh, sudah pulang? Baru saja kubesarkan api buat hangatkan supnya, jadi masih panas semua. Hari ini gedung kampus ramai banget ya? Kamu kelihatan agak capek."
        chiasa "Lumayan ramai, jalannya dari stasiun juga agak jauh. Aku cuci tangan sebentar dulu."
        koita "Iya, santai saja. Duduk dulu kalau sudah selesai, biar langsung makan selagi masih hangat."
    nar "Kamu menarik kursi kayu di sisi kanan meja dan duduk dengan punggung sedikit tegak. Tanpa perlu banyak bicara, Koita kembali berbalik ke kompor, memeriksa api kecil di bawah teko air sambil mengobrol ringan seolah jeda hening di antara mereka tidak pernah ada."
    koita "Oh iya, barusan Ibu kirim pesan lagi dari luar kota bareng Ayah. Katanya lauk rebusan di kotak plastik biru rak tengah kulkas itu harus dihabiskan minggu ini biar nggak keburu basi. Aku sudah ambil sebagian buat hari ini, sisanya mungkin kita makan besok malam."
    chiasa "Ayah sama Ibu masih lama pulangnya?"
    koita "Katanya akhir pekan depan baru sempat balik sehari, itu pun masih tergantung jadwal rapat Ayah. Oh ya, Ibu juga nanya apakah tas kain barumu muat buat bawa buku sketsa besar, soalnya kemarin kamu sempat mengeluh resleting tas lamamu macet."
    nar "Sambil berbicara, tangan Koita bergerak begitu terbiasa di area dapur yang kecil ini. Ia membuka lemari piring di atas wastafel, meraih sebuah cangkir keramik kuning bermotif kucing, lalu menjatuhkan satu dadu gula ke dasarnya."
    koita "Tehnya mau kubuatkan seperti biasa sekalian? Airnya baru saja mendidih nih."
    nar "Kamu terdiam selama satu tarikan napas pendek menatap cangkir kuning di tangannya. Kamu sama sekali tidak tahu minuman 'seperti biasa' versi Chiasa itu teh hijau tawar, teh hitam, atau teh susu, sampai kamu melihat Koita menyobek satu kantong teh hitam aromatik dan mencelupkannya sebelum menuang air panas dari teko."
    nar "Ia bertanya begitu semata karena kebiasaan bertahun-tahun tinggal di bawah atap yang sama. Kini ia berdiri di depan kompor sambil memegangi pegangan teko, menoleh sekilas lewat bahunya menunggu sahutanmu."
    nar "Dulu, ketika kamu membaca manga ini di layar ponsel, panggilan manja Chiasa untuk kakak tirinya hanyalah deretan huruf cetak di dalam balon dialog yang lewat begitu saja. Sekarang, di ruang makan hangat yang jaraknya tak sampai dua meter ini, sebutan itu harus keluar dari kerongkonganmu sendiri tanpa terdengar seperti orang asing yang sedang menghafal naskah."
    call kk_family_menu("C02", ["\"Iya, makasih ya, Ko-nii. Kayak biasa aja.\"", "\"Iya, tolong. Makasih, Koita.\"", "\"Mau dong, Ko-nii~. Tumben manis banget.\""])
    if _return == "A":
        nar "Kamu menarik napas pendek tanpa suara, melemaskan bahu yang sempat menegang, lalu membiarkan pita suara tubuh ini melantunkan nada ringan yang paling sering diucapkannya."
        chiasa "Iya, makasih ya, Ko-nii. Kayak biasa aja."
        nar "Gerakan tangan Koita yang sedang mengaduk sendok kecil di dalam cangkir kuning itu tidak tersendat sedikit pun. Bunyi denting lembut logam menyentuh keramik berlanjut tenang, lalu ia berjalan menghampiri meja dan menaruh teh hangat tersebut di sisi kanan piringmu sambil tersenyum lega."
        koita "Oke, gulanya satu saja kan biar nggak terlalu manis? Hati-hati, masih agak panas."
        nar "Ia melepas simpul tali celemeknya di belakang pinggang, menggantungkannya di sandaran kursi sebelah, lalu duduk di kursi seberangmu. Kamu memperhatikan caranya merapatkan kedua tangan singkat sebelum mengambil sumpit, lalu cepat-cepat meniru gerakannya agar tidak tampak janggal."
        koita "Tumben banget hari ini nggak langsung mengeluh ngantuk atau pegal, Chi-chan. Gimana minggu-minggu awal di kampus? Sudah mulai hafal jalur ke gedung sayap barat?"
        chiasa "Lumayan kok, Ko-nii. Awal kuliah memang beda jauh sama waktu SMA dulu, ruangannya terpencar ke mana-mana, jadi aku lagi berusaha menyesuaikan ritme biar nggak keteteran."
        koita "Haha, tumben sekali adikku bicara bijak begitu. Biasanya baru hari ketiga sudah protes kakinya pegal gara-gara jalan dari gerbang depan sampai gedung studio."
        chiasa "Kalau protes terus juga nggak bikin gedungnya pindah lebih dekat, kan?"
        koita "Betul juga sih. Eh, ngomong-ngomong, teman sejurusanmu yang waktu orientasi langsung akrab itu siapa namanya... Ishikawa-san ya? Dia masih seramai di pesan kemarin?"
        nar "Kamu menyumpit sepotong lobak rebus dari kotak plastik biru untuk memberi jeda sedetik sambil menyusun jawaban aman dari potongan pesan ponsel yang sempat kamu lihat."
        chiasa "Iya, Haruka masih seheboh itu. Baru beberapa hari masuk, obrolannya sudah sampai ke rencana pameran akhir semester."
        koita "Bagus dong kalau kamu dapat teman yang ramai begitu. Soalnya kalau kamu lagi asyik menggambar, kadang suka lupa jam makan siang sendiri."
        nar "Kamu menelan suapanmu perlahan sambil diam-diam mencatat setiap petunjuk hidup sehari-hari yang baru saja ia serahkan secara cuma-cuma. Mulai dari letak kotak makan di kulkas, kebiasaan lupa makan pemilik tubuh ini, hingga seberapa akrab Koita dengan rutinitas kecil Chiasa."
        koita "Oh iya, kalau jadwal kuliah kita lagi barengan, bilang saja ya biar bisa jalan ke stasiun sama-sama. Tadi pagi juga Nagisa-chan sempat mengeluh di grup soal tugas awal yang langsung numpuk, sementara Yutaka katanya agak telat bangun. Kalau mereka lagi mampir ke kantin utama, kita bisa makan siang bareng sekalian."
        chiasa "Iya, gampang nanti kukabari lewat pesan kalau kelasku selesai barengan."
        koita "Kalau habis kelas kamu bawa papan gambar berat atau malas jalan sendirian dari ujung barat kampus, tunggu saja di dekat kantin utama atau telepon aku. Jadwal kelasku semester ini nggak terlalu padat kok, jadi aku masih sempat nyusul."
        chiasa "Santai saja, Ko-nii nggak usah terlalu khawatir begitu. Aku kan sudah mahasiswi sekarang, masa ke mana-mana masih harus dijemput terus."
        koita "Ya mau gimana lagi, tetap saja rasanya baru kemarin kamu masih minta dibantu bawa tas gambar waktu pulang hujan."
        nar "Ia tertawa pelan sambil menyendok sup misonya. Kamu ikut mengangkat cangkir keramik kuning bermotif kucing itu dan menyesap sedikit teh hitam hangat yang terasa manis tipis di lidah."
        chiasa "Tehnya pas kok, Ko-nii. Makasih ya."
        koita "Syukurlah. Habiskan juga rebusan dari Ibu itu, nanti kalau sampai bersisa di kulkas pas mereka pulang, aku yang kena omel duluan."
        chiasa "Iya, iya, ini juga lagi kumakan kok."
        nar "Panggilan itu diterima begitu mulus sampai ketegangan di pundakmu berangsur turun. Sepanjang sisa waktu makan, Koita terus bercerita santai tentang dosen pengantarnya yang suka keluar topik dan rencananya mampir ke toko buku bekas dekat stasiun, sementara kamu membalas seperlunya sambil memunguti serpihan informasi dari percakapan rumah tangga biasa."
        nar "Ketika kalian selesai makan dan kamu ikut mengangkat mangkuk kosongmu ke bak cuci piring, Koita hanya mengangguk ringan seolah tidak ada yang berubah sedikit pun di dalam rumah ini."
    elif _return == "B":
        nar "Lidahmu terasa kelu dan enggan memaksa tubuh ini mengucapkan panggilan semanja itu kepada protagonis manga yang paling tidak kamu sukai. Sebelum kamu sempat menimbang akibatnya, kalimat yang meluncur dari bibirmu justru terdengar datar dan lugas."
        chiasa "Iya, tolong. Makasih, Koita."
        nar "Bunyi kucuran air panas dari moncong teko mendadak berhenti. Tangan Koita tertahan di udara selama dua detik penuh sebelum ia meletakkan teko itu kembali ke atas kompor dengan bunyi logam pelan, lalu menoleh ke arahmu dengan kening berkerut."
        koita "...'Koita'? Tumben sekali. Sejak kapan kamu memanggilku pakai nama langsung begitu tanpa embel-embel kakak?"
        nar "Ia mengeluarkan tawa pendek yang terdengar canggung, mengambil cangkir kuning bermotif kucing itu dari meja dapur, lalu berjalan pelan menghampiri meja makan. Alih-alih langsung duduk, ia berdiri di samping kursimu sesaat setelah menaruh cangkir tersebut, menatap wajahmu seolah sedang menunggu kelanjutan dari sebuah lelucon."
        nar "Jemari tangan kananmu refleks terangkat menyentuh ujung pita hitam di rambutmu. Kamu baru menyadari betapa mencoloknya perubahan satu kata itu ketika seluruh keakraban di dalam rumah ini berdiri di atas cara Chiasa menyebut namanya."
        chiasa "A-ah, itu... aku kan sekarang sudah jadi mahasiswi, masa masih kayak anak SMA terus manggil manja begitu. Cuma pengin coba kedengaran lebih dewasa saja."
        koita "Apaan sih, bukannya terdengar dewasa, itu malah kedengaran dingin kayak orang asing tahu nggak?"
        nar "Ia menggaruk pelipisnya pelan, senyum canggungnya perlahan menyusut menjadi raut bingung yang tulus."
        koita "Kupikir tadi kamu lagi marah gara-gara aku salah ngomong sesuatu kemarin, atau gara-gara aku lupa membalas pesanmu. Ada sesuatu yang bikin kamu kesal, Chi-chan?"
        chiasa "Nggak ada kok. Sungguh, nggak ada hubungannya sama kamu."
        koita "Serius? Biasanya kalau kamu lagi kesal sama aku, kamu justru makin cerewet atau langsung menyindir di depan muka, nggak pernah tiba-tiba memanggil nama langsung dengan nada sedatar tadi."
        nar "Koita akhirnya melepas simpul celemeknya, menggantungkannya di sandaran kursi, lalu duduk di seberangmu. Ketika ia merapatkan tangan singkat dan meraih sumpit untuk menyendok sup miso, caranya menatapmu jelas tidak lagi sesantai beberapa menit lalu. Matanya sempat singgah mengamati raut wajahmu lebih lama setiap kali kamu menunduk."
        chiasa "Aku cuma masih agak capek menyesuaikan diri sama jadwal kampus baru saja. Ruangannya jauh-jauh, orang-orangnya juga baru semua."
        koita "...Kalau kamu lagi nggak enak badan, kurang tidur, atau ada yang bikin kamu nggak nyaman di lingkungan kampus baru, bilang saja ke aku lho, Chi-chan. Jangan dipendam sendiri sampai jadi kaku begini."
        nar "Melihat tatapan khawatir yang masih menempel di wajahnya, kamu tahu menahan jarak terlalu keras sekarang hanya akan membuatnya terus bertanya. Kamu menurunkan bahumu pelan, mengangkat sumpit, lalu memaksa nada suaramu kembali lebih lunak."
        chiasa "Iya, maaf ya, Ko-nii. Tadi memang cuma lagi agak linglung saja."
        nar "Begitu panggilan lama itu akhirnya keluar dari mulutmu, ketegangan di bahu Koita tampak sedikit mengendur. Ia mengembuskan napas pendek yang hampir mirip kelegaan, lalu menyendok nasi ke mangkuknya."
        koita "Syukurlah kalau cuma kecapekan. Kalau besok-besok kamu malas jalan sendirian ke stasiun atau butuh bantuan bawa barang studio, langsung bilang saja. Nggak perlu sungkan atau pura-pura sok dewasa mendadak begitu lagi."
        chiasa "Iya, ngerti kok."
        nar "Suasana makan kembali berjalan, tetapi keheningan di antara bunyi sumpit dan mangkuk terasa beberapa derajat lebih dingin daripada sebelumnya. Dua kali selama kalian makan, kamu menangkap pandangan Koita yang melirik singkat ke arahmu saat menuangkan teh untuk dirinya sendiri, seolah ia masih berusaha memastikan apakah adik tirinya benar-benar baik-baik saja."
        nar "Ketika kamu akhirnya membereskan piring dan beranjak dari meja, satu pelajaran penting sudah tertanam kuat di kepalamu. Sekali saja kamu terpeleset keluar dari peran Chiasa, orang yang tinggal satu atap denganmu ini akan menjadi yang pertama merasakannya."
    else:
        nar "Daripada terlihat kaku dan mencurigakan karena terlalu berhati-hati, kamu memutuskan bersembunyi tepat di balik sifat asli Chiasa yang paling mencolok. Kamu meletakkan kedua sikumu di atas meja makan, menopang dagu dengan kedua telapak tangan, lalu memiringkan kepala sedikit sambil menarik sudut bibirmu menjadi senyum jahil."
        chiasa "Mau dong, Ko-nii~. Tumben pelayanannya ekstra manis begini, sampai tehku langsung dibikinkan tanpa diminta. Jangan-jangan Ko-nii lagi ada maunya ya, atau lagi menyembunyikan sesuatu dariku?"
        nar "Bahu Koita tersentak kecil hingga teh panas di dalam cangkir kuning itu nyaris menyentuh bibir tatakan. Ia buru-buru melangkah ke meja dan menaruh cangkir itu di depanmu sambil berdeham, ujung telinganya memerah tipis dengan cara yang langsung memperlihatkan betapa seringnya ia tak berkutik menghadapi godaan semacam ini."
        koita "Hei, jangan mulai iseng begitu dong! Aku kan cuma nyiapin makan biar kamu nggak jajan roti minimarket terus di awal kuliah begini. Memangnya kakak sendiri nggak boleh baik sedikit?"
        chiasa "Boleh banget sih. Cuma kalau Ko-nii terlalu rajin begini, aku jadi curiga nih."
        nar "Koita melepas celemeknya dengan gerakan agak tergesa dan duduk di kursi seberang sambil menyambar sumpitnya."
        koita "Nggak ada yang kusembunyikan kok. Lagipula Ibu juga nitip pesan supaya kita makan yang benar selama mereka di luar kota."
        nar "Melihat reaksinya yang begitu mudah dibaca, kamu mendorong umpan itu selangkah lebih jauh untuk menakar seberapa besar pengaruh Chiasa atas kakak tirinya sekaligus menguji batas sikapnya."
        chiasa "Masa cuma karena pesan Ibu? Bukan gara-gara Ko-nii takut sekarang adikmu yang manis ini bakal sibuk dilirik cowok-cowok dan senior keren di gedung sayap barat, terus lupa makan bareng di rumah?"
        nar "Gerakan tangan Koita yang baru saja hendak mengambil sepotong telur goreng langsung melambat di tengah jalan. Senyum canggung yang tadi tersisa di wajahnya surut perlahan, digantikan kerutan samar di sela alisnya yang jarang sekali ia tunjukkan di depan orang lain."
        nar "Ia meletakkan sumpitnya di tepi piring, lalu menatapmu dari seberang meja dengan nada bicara yang mendadak turun lebih rendah dan serius."
        koita "...Di sayap barat kan memang banyak orang yang nyentrik dan suka asal akrab, Chi-chan. Apalagi kamu baru masuk tahun pertama, belum tahu karakter senior-senior di sana seperti apa."
        chiasa "Lho, kok jadi serius begitu mukanya?"
        koita "Aku serius. Kalau ada senior atau teman seangkatan yang aneh-aneh, mulai terlalu dekat, atau memaksa ngajak pergi setelah kelas, kamu harus langsung bilang ke aku. Jangan gampang ikut ajakan orang cuma karena nggak enak menolak."
        chiasa "Wah, kakak yang posesifnya keluar juga ternyata. Mau sekalian datang memeriksa teman-teman studio satu per satu kayak satpam kampus?"
        koita "Aku nggak bercanda, Chi-chan. Di kampus itu nggak semua orang ramah tanpa maksud."
        nar "Nada suara Koita terdengar begitu tulus hingga sempat membuatmu terhenti sepersekian detik. Di balik senyum mudahnya yang ramah kepada semua orang di luar sana, ternyata ada garis posesif yang cukup pekat setiap kali menyangkut adik tirinya sendiri."
        chiasa "Tenang saja, Ko-nii, aku tahu cara jaga diri kok. Lagipula kalau ada yang aneh, paling juga langsung kutinggal pulang."
        nar "Merasa umpanmu sudah lebih dari cukup untuk menutupi kegugupan sekaligus memancing batas reaksinya, kamu langsung menegakkan dudukmu, menurunkan kedua tangan dari dagu, menghapus senyum jahil itu bersih-bersih, lalu meraih sumpit untuk menyendok sup miso dengan tenang. Kamu memutus permainan godaan itu jauh lebih cepat daripada kebiasaan Chiasa yang asli."
        nar "Perpindahan mendadak dari senyum menggoda ke raut datar yang tenang itu membuat Koita terdiam di kursinya. Tangannya masih berhenti di dekat mangkuk nasi, matanya menatap wajahmu selama beberapa detik penuh seolah mencoba menebak apakah kamu masih bercanda atau benar-benar sudah bosan menggodanya."
        koita "...Eh? Sudah selesai ngeledeknya?"
        chiasa "Sudah. Supnya nanti keburu dingin kalau cuma dipakai ngobrol terus."
        koita "Oh... iya juga sih. Ayo makan dulu."
        nar "Ia akhirnya ikut mengangkat sumpit dan mulai makan sambil sesekali masih melirik singkat ke arahmu di sela kunyahan, tampak masih sedikit terganggu oleh seberapa cepat senyum jahil tadi menghilang dari matamu."
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
    nar "Di atas meja kayu di hadapanmu, di antara deretan buku sketsa, pena gambar, dan spidol warna milik pemilik tubuh ini, tergeletak selembar kertas tanzaku kuning pucat lengkap dengan seutas benang tipis. Di sebelahnya, terselip sebuah tanzaku lama dari tahun lalu yang rupanya pernah dipakai Chiasa sebagai pembatas halaman di buku sketsanya."
    nar "Kamu memandangi tulisan tangan rapi di kertas lama itu, berisi harapan pendek dan manis tentang ingin selalu berada di sisi kakak tirinya dan tidak pernah berubah. Kamu bahkan tidak perlu menebak-nebak, karena kalau ingin bermain aman, kamu tinggal menyalinnya persis seperti tahun-tahun sebelumnya."
    nar "Justru karena terlalu mudah untuk disalin itulah ujung spidol di tanganmu tertahan di atas kertas kosong."
    nar "Dari balik pintu kamar yang sedikit terbuka, suara langkah kaki di lorong terdengar mendekat, disusul ketukan pelan dua kali di daun pintu."
    koita "Chi-chan, tulisan di kertasmu sudah selesai belum? Dahan bambunya sudah kupasang di beranda bawah nih, Haruka-san juga baru mampir bantu merapikan tali-talinya."
    chiasa "Sebentar lagi, Ko-nii! Tunggu lima menit lagi aku turun!"
    koita "Oke, santai saja. Jangan kelamaan mikir permohonannya, nanti keburu gelap."
    nar "Langkah Koita kembali menjauh menuruni tangga kayu. Kamar itu kembali hening, menyisakan kertas tanzaku kosong yang menunggu di atas meja."
    nar "Tubuh ini pinjaman, nama ini pinjaman, bahkan kamar penuh alat gambar ini bukan milikmu. Kamu harus memutuskan apakah di tengah semua peran yang harus kamu jalani ini, satu harapan kecil di atas kertas tipis boleh benar-benar menjadi milikmu sendiri, atau sebaiknya tetap disembunyikan di balik bayangan Chiasa."
    call kk_family_menu("C03", ["Tulis harapan baru, milikmu sendiri.", "Salin harapan aslinya persis.", "Biarkan tanzaku itu kosong."])
    if _return == "A":
        nar "Kamu menutup buku sketsa lama itu perlahan, menyingkirkan kertas tanzaku tahun lalu dari pandanganmu, lalu menekan ujung pena ke permukaan kertas kuning yang masih bersih."
        nar "Tanpa berusaha meniru gaya bahasa manis ataupun memikirkan kalimat apa yang akan membuat Koita senang saat membacanya, kamu menuliskan satu baris pendek dengan maksudmu sendiri, 'Semoga aku bisa melewati semua ini dengan jalanku sendiri dan tetap hidup sampai akhir.'"
        nar "Tarikan garis hurufnya memang sedikit berbeda dibandingkan tulisan melengkung di buku catatan Chiasa, tetapi kalimat di depanmu itu sepenuhnya jujur mewakili dirimu."
        nar "Kamu mengikatkan benang tipis di lubang ujung kertas itu, lalu membawanya turun ke beranda belakang. Di sana, Koita dan Ishikawa Haruka sedang menggantung beberapa kertas warna-warni di dahan bambu kecil yang disandarkan di tiang teras."
        koita "Nah, akhirnya turun juga. Sini, gantung di dahan bagian atas biar nggak ketutupan daun... eh, tahun ini kamu nulis permohonan apa, Chi-chan? Boleh aku intip sedikit?"
        chiasa "Rahasia dong, Ko-nii. Kata orang kalau permohonan Tanabata dibaca keras-keras sebelum digantung, nanti malah nggak terkabul."
        "Haruka" "Benar kata Chiasa, Koita-san, jangan diintip begitu! Eh, tapi sekilas garis tulisan tanganmu hari ini kelihatan lebih tegas dan lurus ya, Chiasa? Biasanya hurufmu agak bulat-bulat lucu."
        chiasa "Aku tadi nulisnya sambil berdiri buru-buru waktu dipanggil Ko-nii, Haruka, makanya agak kaku sedikit."
        "Haruka" "Oh, pantas! Ayo gantung di sebelah punyaku yang warna merah muda ini biar berdampingan!"
        nar "Kamu mengikatkan kertas kuningmu di dahan samping kertas milik Haruka dengan simpul rapat. Koita tertawa kecil dan mengangkat kedua tangan tanda menyerah tidak jadi mengintip, sementara angin sore mulai mengayunkan kertas permohonan milikmu itu di antara dedaunan bambu."
    elif _return == "B":
        nar "Kamu menatap kertas tanzaku lama di samping buku sketsa selama beberapa detik, lalu menarik napas pendek. Bermain aman jauh lebih masuk akal daripada memancing pertanyaan yang tidak perlu di dalam rumah ini."
        nar "Dengan gerakan tangan yang hati-hati, kamu meniru bentuk huruf dan menyalin harapan lama Chiasa nyaris kata demi kata, menjaga nada manis tentang keinginan agar hari-hari bersama kakaknya tidak pernah berubah."
        nar "Ketika kamu turun ke beranda belakang dan mengangkat tangan untuk mengikatkannya di dahan bambu, Koita yang berdiri menahan pot di sebelahmu sempat membaca baris kalimat itu sebelum kertasnya terputar angin. Senyum hangat yang tampak sangat lega langsung merekah di wajahnya."
        koita "Haha... ternyata permohonanmu tahun ini masih sama persis kayak tahun lalu ya, Chi-chan. Nggak berubah sedikit pun."
        chiasa "Memangnya kenapa kalau sama? Kan memang itu yang paling gampang kepikiran waktu mau nulis."
        koita "Nggak apa-apa, justru aku senang sekali bacanya. Jujur saja, kadang setelah kamu masuk kuliah dan sibuk di studio, aku sempat kepikiran kalau kita berdua bakal makin jarang punya waktu ngobrol di rumah kayak dulu."
        "Haruka" "Wah, kalian berdua ini benar-benar kakak-adik yang akur sekali ya! Sampai permohonan Tanabata pun masih saling nyambung begitu."
        chiasa "Kita kan memang masih tinggal satu atap, Ko-nii. Nggak usah mikir yang aneh-aneh deh."
        koita "Iya juga sih... makasih ya, Chi-chan."
        nar "Koita menepuk puncak kepalamu dengan lembut sebelum berbalik membantu Haruka merapikan pita di dahan bawah. Penyamaranmu hari ini berjalan tanpa celah sedikit pun, meski kamu tahu kelegaan di wajah Koita barusan dibangun di atas kalimat masa lalu yang sama sekali bukan milikmu."
    else:
        nar "Ujung penamu berhenti beberapa milimeter di atas kertas kuning itu, lalu perlahan kamu menutup kembali tutup penanya dan meletakkannya ke atas meja. Menulis harapan palsu milik orang lain terasa memuakkan, sementara menulis rahasia aslimu di rumah ini terlalu berbahaya."
        nar "Kamu mengambil kertas tanzaku yang masih polos tanpa satu huruf pun itu, mengikatkan benangnya di lubang atas, lalu melangkah turun ke beranda belakang. Koita sedang sibuk menata ulang batu pemberat pot bambu di sudut teras, sehingga yang pertama kali memperhatikan kertas di tanganmu justru Haruka."
        "Haruka" "Eh, Chiasa? Kertas tanzakumu kok masih kosong melompong? Kamu belum nulis apa-apa?"
        nar "Suara Haruka tidak terdengar menuduh, melainkan penuh keheranan yang tulus. Ia melangkah mendekat sambil mengamati lembar kertas kuning polos yang baru saja hendak kamu ikatkan ke ranting."
        "Haruka" "Tumben sekali kamu biarkan kosong. Tahun lalu waktu di klub seni SMA saja kamu sampai minta dua lembar kertas tambahan gara-gara merasa susunan huruf permohonanmu kurang rapi. Pena di kamarmu habis tintanya ya? Ini, pakai spidol hitamku saja kalau mau nulis di sini."
        nar "Haruka menyodorkan spidol hitam tipisnya ke arahmu dengan senyum ramah, mengira masalahnya hanya soal alat tulis. Koita yang mendengar percakapan itu ikut berdiri dan menoleh dari dekat pot bambu."
        koita "Lho, beneran belum kamu tulis apa-apa, Chi-chan? Tadi di kamar lima menit ngapain saja?"
        chiasa "Ah... bukan karena tintanya habis kok, Haruka, Ko-nii. Cuma tahun ini aku lagi benar-benar nggak kepikiran mau nulis permintaan apa. Rasanya aneh saja kalau harus mengarang permohonan yang nggak beneran kupikirkan."
        "Haruka" "...Mengarang permohonan? Tumben banget kamu ngomong seserius itu soal Tanabata, Chiasa."
        koita "Kalau lagi belum kepikiran ya nggak apa-apa sih digantung polos begitu, anggap saja hiasan warna di bambunya."
        nar "Haruka menarik kembali spidolnya perlahan dan mengangguk sopan, tetapi tatapan matanya sempat bertahan mengamati wajahmu sedikit lebih lama, seolah sedang mencoba mencocokkan kalimat dinginmu barusan dengan sosok Chiasa yang selama ini ia kenal di studio."
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
    nar "Deretan lampion kertas merah dan putih memanjang di sepanjang jalan setapak menuju halaman kuil festival musim panas, memantulkan cahaya hangat di atas kerumunan pengunjung yang mengenakan yukata. Aroma manis permen kapas, saus takoyaki yang mendesis di atas pelat besi panas, dan seruan penjaga stan permainan ikan mas bercampur di udara malam Agustus."
    nar "Beberapa langkah di depan sebuah stan suvenir kayu, Sakurajima Nagisa berdiri sendirian sambil merapikan tali tas serut kainnya. Malam ini ia mengenakan yukata bermotif bunga cerah yang serasi dengan rambut pirang keemasannya yang diikat dua; gantungan kunci kelinci kecil yang biasa menempel di tas kuliahnya tampak dipindahkan ke tali tas festivalnya."
    nar "Ketika kamu melangkah mendekat, kamu teringat cerita Koita di ruang tamu tadi sore sebelum berangkat, bahwa sewaktu mereka masih duduk di sekolah dasar dulu, Chiasa selalu memegangi ujung lengan yukata Nagisa setiap kali diajak ke festival malam dan memanggilnya dengan sebutan 'Nacchan-oneechan'."
    nar "Panggilan masa kecil itu perlahan berhenti dipakai sejak mereka beranjak remaja dan mulai berdiri dalam ketegangan diam-diam untuk memperebutkan perhatian Koita."
    nar "Nagisa menoleh saat menyadari langkah terompah kayumu berhenti di sampingnya. Alisnya sedikit terangkat, dan postur siaga yang biasa ia pasang setiap kali berhadapan dengan Chiasa langsung terlihat di bahunya."
    nagisa "Oh, Chiasa. Kukira kamu masih jalan di belakang bareng Ko-kun sama yang lain. Pengunjungnya padat banget malam ini, kalau jalan terpisah di tikungan depan nanti susah nyarinya."
    nar "Sebutan lama 'Nacchan-oneechan' itu kini berada di ujung lidahmu. Kamu tahu satu panggilan saja dapat menggeser suasana di antara kalian malam ini, entah membangkitkan kembali sisi kakak perempuan dalam ingatan Nagisa, menjaga jarak formal, atau justru menyulut persaingan terbuka."
    call kk_family_menu("C04", ["\"Kalau begitu aku jalan di sebelahmu saja, Nacchan-oneechan.\"", "\"Iya, ramai banget, Nagisa-senpai. Ayo jalan bareng saja.\"", "\"Tenang saja, aku nggak gampang tersesat. Aku mau jalan di depan bareng Ko-nii.\""])
    if _return == "A":
        nar "Kamu tidak memasang senyum menyindir seperti yang biasa dilakukan Chiasa saat menggoda Nagisa di kampus. Dengan nada bicara yang tenang, ringan, dan bebas dari ejekan, kamu menatapnya sambil melangkah sejajar di sampingnya."
        chiasa "Kalau begitu aku jalan di sebelahmu saja supaya nggak terpisah di tengah kerumunan, Nacchan-oneechan."
        nar "Seketika, gerakan tangan Nagisa yang sedang mengencangkan tali tas serutnya berhenti. Mata biru cerahnya mengerjap dua kali dengan raut terkejut yang sama sekali tidak sempat ia tutupi."
        nagisa "...Eh? Tunggu sebentar, barusan kamu manggil aku apa?"
        chiasa "Nacchan-oneechan. Kenapa? Aneh ya kalau kupanggil begitu lagi waktu kita jalan di festival kayak dulu?"
        nar "Selama beberapa detik, seluruh sikap defensif dan kebiasaan mencari celah perdebatan langsung luruh dari wajah Nagisa. Rona merah tipis merambat naik ke telinganya, dan ketika ia kembali membuka suara, nadanya terdengar jauh lebih lembut."
        nagisa "...Sudah lama sekali aku nggak dengar kamu manggil begitu. Kupikir kamu sudah lupa total, atau sudah gengsi memakainya sejak kita masuk SMA."
        chiasa "Mana mungkin lupa. Dulu kan waktu aku masih pendek, aku yang paling sering narik-narik ujung lengan yukatamu di depan stan permen apel biar nggak tertinggal di belakang."
        nagisa "Iya, sampai jahitan lengan yukata kesayanganku waktu itu hampir melar sebelah gara-gara kamu tarik terus... dasar anak nakal."
        nar "Sudut bibir Nagisa melengkung membentuk senyum kecil yang hangat tanpa sedikit pun kesan galak. Ia menggeser langkahnya setengah tapak lebih dekat ke sisimu sambil menoleh ke arah deretan tangga kuil yang terang oleh lampion."
        nagisa "Ya sudah, ayo jalan di sebelahku sampai ke pelataran atas. Awas jangan sampai lepas terus hilang lagi di kerumunan kayak waktu kecil, Chi-chan."
        chiasa "Hehe, iya, aku jalan persis di sampingmu kok."
        nar "Di tengah riuh rendah pengunjung festival malam itu, satu panggilan lama barusan berhasil meruntuhkan tembok persaingan Nagisa, mengembalikan sejenak kehangatan dua gadis yang pernah tumbuh besar bersama."
    elif _return == "B":
        nar "Kamu memutuskan tidak menggunakan panggilan masa kecil yang kenangannya bukan milikmu. Kamu mengangguk singkat dengan senyum sopan yang terjaga."
        chiasa "Iya, malam ini ramai sekali, Nagisa-senpai. Ayo kita jalan bareng saja supaya nggak terpisah dari rombongan."
        nar "Tampak jeda singkat di raut wajah Nagisa. Kelopak matanya berkedip pelan, seolah di tengah suasana lampion festival yang persis seperti masa kecil mereka dulu, ia sempat tanpa sadar menantikan sapaan yang lebih akrab daripada panggilan senior kampus."
        nagisa "...Oh. 'Nagisa-senpai', ya. Kukira kalau lagi di festival luar kampus begini, kita nggak sekaku itu."
        chiasa "Eh... maksudku kan sekarang di kampus kita sudah beda angkatan, jadi biar tetap sopan saja di depan orang banyak."
        nar "Nagisa segera mengibaskan satu tangannya di depan dada, berusaha menutupi rasa kecewa kecil yang sempat terlintas di matanya."
        nagisa "Nggak apa-apa kok! Memang sudah seharusnya panggil begitu kan kalau sudah kuliah. Ayo cepat jalan, nanti kita kehabisan tempat bagus buat lihat kembang api di atas."
        chiasa "Iya, ayo."
        nar "Ia langsung berbalik menghadap jalan setapak dan melangkah lebih dulu di antara deretan stan makanan, mempertahankan jarak dua langkah yang sopan dan rapi di depanmu sepanjang perjalanan menuju kuil."
    else:
        nar "Daripada berpura-pura akrab atau bersikap sopan yang kaku, kamu membiarkan sudut bibirmu terangkat tipis, memasang senyum menantang yang sangat sesuai dengan peran rival yang selama ini selalu diwaspadai Nagisa."
        chiasa "Tenang saja, Nagisa-senpai, aku bukan anak kecil lagi yang gampang tersesat di festival. Lagipula aku memang sengaja jalan cepat ke depan supaya nanti bisa berdiri berdua bareng Ko-nii waktu kembang apinya mulai."
        nar "Kedua alis Nagisa langsung menukik tajam. Ketegangan yang tadinya hanya samar di pundaknya seketika mengeras penuh, dan sorot mata birunya menatapmu tanpa berkedip."
        nagisa "Oh... jadi malam ini kamu mau main terang-terangan begitu ya, Chiasa? Nggak pakai alasan minta ditemani kayak dulu lagi?"
        chiasa "Aku kan cuma ngomong jujur dari awal. Kalau Senpai mau jalan santai lihat-lihat suvenir di belakang sendirian, silakan saja."
        nagisa "Enak saja! Siapa juga yang mau tertinggal di belakang! Lihat saja nanti siapa yang bakal duduk di sebelahnya waktu di tanggul sungai!"
        nar "Ia langsung memutar tumitnya dan melangkah cepat sejajar di sampingmu dengan dagu terangkat, sama sekali tidak sudi membiarkanmu mendahuluinya barang setengah langkah pun."
        nar "Persaingan terbuka ternyata memberimu topeng yang sangat mudah dimainkan di hadapan Nagisa. Selama kamu terus memancing sifat keras kepalanya, ia tidak akan pernah sempat mencurigai bahwa orang di dalam tubuh Chiasa telah berganti."
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
