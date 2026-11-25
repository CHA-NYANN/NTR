# Milestone host Chiasa (C06, C07, C10, C12-C17): hidup pemain-sebagai-Chiasa dan
# navigasi arah (yuri / Koita Success / Yutaka). Fire saat MASUK lokasi sebagai
# host Chiasa (trigger "host"). Pilihan yang membuka arah rute disambung sebagai
# POINTER-RUTE (bendera + teks terkendali), bukan adegan eksplisit. Mengikuti
# Event_Chiasa; melengkapi C02-C05/C08/C09 (kk_chiasa_host.rpy).

# ┌─ PANDUAN CERITA · C06 · Natal Rumah Amamiya
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : A di rumah bersama Koita / B mengundang heroine / C pergi ke Nagisa/yuri / D sendirian.
# │ AKHIRAN : hub besar #3.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C06:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Natal")
    nar "Udara akhir Desember di luar jendela Rumah Amamiya terasa menggigit, meninggalkan lapisan embun tipis di sudut kaca ruang makan. Di dalam rumah, pemanas ruangan di dekat sofa berdengung pelan, menyebarkan hawa hangat yang bercampur dengan wangi mentega, bawang bombai tumis, dan kaldu sup krim dari arah dapur."
    nar "Daisuke dan Yoshie masih berada di Sapporo untuk urusan pemotretan majalah akhir tahun, sehingga meja makan kayu malam ini hanya ditata untuk dua orang. Di tengah taplak kotak-kotak, tergeletak sebuah kotak kue bolu stroberi ukuran kecil dari toko roti dekat stasiun, berdampingan dengan rangkaian lampu hias mungil yang tadi kamu sangkutkan di tepi bufet."
    nar "Koita berdiri di depan kompor sambil mengaduk panci sup dengan sendok kayu. Begitu api kompor dimatikan, ia melepas celemek biru tuanya, menyeka tangan dengan handuk gantung, lalu menoleh ke arahmu yang baru saja turun dari lantai dua."
    koita "Pas banget kamu turun, Chi-chan. Sup krimnya baru matang, ayam panggang yang kubeli di kedai depan stasiun juga sudah kupanasin di oven."
    chiasa "Harum banget sampai ke tangga atas, Ko-nii. Kirain Ko-nii cuma beli lauk jadi semua tadi sore."
    koita "Kalau malam Natal cuma makan lauk kotak dari minimarket kan sedih banget. Tadi aku sampai ngiris bawang bombai dua biji sambil mata pedas gara-gara lupa nyalain penyedot asap."
    chiasa "Haha, pantesan tadi pas aku lewat depan pintu kamar kayak dengar suara Ko-nii bersin dua kali dari bawah."
    koita "Eh, kedengaran sampai lantai dua? Itu gara-gara mericanya kebanyakan sedikit pas kutuang. Tenang aja, sudah kucicipi kok, rasanya aman dan nggak keasinan."
    chiasa "Ayah sama Ibu tadi ada kirim kabar lagi dari Sapporo, Ko-nii?"
    koita "Baru sejam lalu Ibu kirim pesan. Katanya salju di sana turun makin tebal sampai Ayah ngeluh tas kameranya basah semua. Ibu juga sempat nanya kita berdua makan apa malam ini di rumah, terus titip pesan jangan sampai tidur terlalu larut."
    nar "Koita menarik dua kursi kayu di meja makan, lalu berhenti sejenak saat melihatmu masih memegang ponsel di tangan sambil berdiri di dekat ujung bufet."
    koita "Eh, tapi aku belum nanya dari siang tadi. Malam ini kamu nggak ada janji keluar sama Karuha atau teman-teman fakultasmu, kan? Biasanya anak tahun pertama suka bikin acara kumpul-kumpul malam Natal di dekat stasiun."
    chiasa "Anak-anak studio memang sempat ngajak jalan lihat lampu hias ke dekat stasiun sih tadi siang."
    koita "Oh, gitu... jadi malam ini kamu mau makan di rumah, atau sudah punya rencana sendiri?"
    nar "Koita bertanya dengan nada ringan sambil memegang gagang teko teh hangat, menunggu kepastian apakah kursi di seberangnya malam ini akan terisi atau tidak."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["\"Malam ini aku di rumah aja kok, makan malam bareng Ko-nii.\"", "\"Sebenarnya aku mau ngundang teman ke rumah malam ini, nggak apa-apa kan?\"", "\"Aku mau keluar sebentar, mampir ke tempat Nagisa-senpai.\"", "\"Aku lagi pengin istirahat sendiri di kamar malam ini. Makan duluan aja.\""])]
    call screen kk_choice_panel(_rows, "Pilihan")
    $ kk_record_choice("C06", _return)
    if _return == "A":
        nar "Kamu mematikan layar ponselmu, menaruhnya di atas bufet samping rangkaian lampu hias, lalu melangkah ke meja makan."
        chiasa "Malam ini aku di rumah aja kok, makan malam bareng Ko-nii. Di luar anginnya dingin banget, malas juga kalau harus desak-desakan di stasiun cuma buat lihat pohon lampu."
        nar "Sudut bibir Koita langsung terangkat lega. Ia meletakkan teko teh di atas tatakan kayu, lalu kembali ke dapur untuk mengambil dua mangkuk keramik putih."
        koita "Syukurlah. Jujur aja, tadi aku sempat mikir kalau kamu tiba-tiba pergi, aku bakal bingung ngabisin sup satu panci sama kue stroberi itu sendirian sampai besok lusa."
        chiasa "Lagian sayang kan kalau sup yang bikin mata Ko-nii pedas tadi sampai dingin nggak ada yang makan. Sini mangkuknya, biar aku yang tuang supnya. Ko-nii keluarkan ayam panggangnya aja dari oven."
        koita "Oke, hati-hati panas ya gagang pancinya. Sendok sayurnya kutaruh di pinggir kompor sebelah kanan."
        nar "Kamu menyendok sup krim yang masih mengepul tebal ke dalam dua mangkuk, memastikan potongan wortel dan kentang di dasar panci terbagi rata, sementara Koita memakai sarung tangan kain untuk mengeluarkan loyang berisi potongan paha ayam panggang kecokelatan. Setelah piring salad dan gelas teh tersusun di meja, kalian berdua duduk berhadapan."
        koita "Selamat makan, Chi-chan."
        chiasa "Selamat makan, Ko-nii."
        nar "Kamu meniup sendok pertama pelan lalu mencicipinya. Kuahnya gurih dan hangat, dengan potongan kentang yang empuk tanpa hancur."
        chiasa "Eh, enak beneran lho ini, Ko-nii. Lebih kental dari yang biasanya Ibu bikin kalau lagi buru-buru."
        koita "Tuh kan, kubilang juga apa. Tadi menteganya kutumis pelan pakai api kecil sesuai catatan resep yang Ibu tempel di kulkas. Ayamnya juga masih renyah tuh kulitnya."
        chiasa "Ko-nii kalau lagi dipuji masakannya, mukanya langsung kelihatan bangga banget lho."
        koita "Lho, wajar dong. Jarang-jarang aku masak sendiri nggak pakai kejadian panci gosong."
        nar "Tawa ringan di ruang makan itu pelan-pelan melunakkan hawa dingin yang menempel di balik kaca jendela. Setelah menghabiskan separuh mangkuk sup dan sepotong ayam panggang, Koita menarik kotak kue putih di tengah meja dan mulai melepas simpul pita merahnya."
        koita "Ngomong-ngomong, lihat kotak kue stroberi dari toko depan stasiun ini, aku jadi ingat waktu kita baru tahun pertama tinggal serumah dulu. Kamu ingat nggak waktu kamu masih kelas empat SD?"
        chiasa "Waktu Natal pertama kita sekeluarga?"
        koita "Iya. Waktu itu kamu ngotot banget nggak mau masuk kamar sampai jam dua belas malam. Katanya mau pergokin Ayah sama Ibu waktu naruh kado di dekat televisi, sekalian ngecek beneran ada kakek janggut putih masuk lewat balkon atau nggak."
        chiasa "Masa sih aku bilang lewat balkon? Rumah kita kan nggak punya cerobong asap."
        koita "Justru itu alasanmu dulu! Kamu duduk di karpet ruang tengah sambil meluk bantal sofa, matamu sudah merah banget nahan ngantuk. Terus ujung lengan sweterku kamu pegangin kencang supaya aku nggak boleh tidur duluan."
        chiasa "Terus aku beneran kuat melek sampai tengah malam?"
        koita "Mana ada! Belum juga jam sebelas, kepalamu sudah jatuh miring ke lututku sambil masih gumam soal pita kado. Waktu kugendong naik ke kamar atas, padahal tinggi kita dulu belum beda jauh, tanganku sampai gemetar di anak tangga terakhir."
        chiasa "Haha, maaf ya Ko-nii. Pasti berat banget dulu."
        koita "Bukan cuma berat, besok paginya aku malah kamu marahin seharian gara-gara kamu kira aku sengaja sekongkol sama Ayah nggak mau bangunin kamu. Sampai makan puding siang pun kamu masih cemberut."
        chiasa "Ya ampun, kecilku galak banget ternyata."
        nar "Koita tertawa kecil sambil memotong bolu stroberi itu menjadi empat bagian, lalu memindahkan satu potongan besar dengan buah stroberi paling merah ke piring kecil di depanmu."
        koita "Sekarang tahu-tahu kamu sudah kuliah aja, sudah sibuk bolak-balik studio sampai sore terus. Kalau Natal tahun ini, ada yang lagi kamu pengin atau bikin kamu capek nggak, Chi-chan?"
        chiasa "Nggak ada barang yang aneh-aneh kok, Ko-nii. Cuma akhir-akhir ini rasanya banyak banget hal di kampus yang muter terus di kepala. Tugas studio, orang-orang di sekitar kita, jadwal semester depan... jadi malam ini bisa duduk makan sup panas di rumah tanpa harus mikirin apa-apa aja sudah lega banget."
        koita "Kalau ada tugas studio yang berat atau ada urusan di kampus yang bikin kepalamu penuh, jangan dipendam sendirian terus lho. Rumah ini tempat pulang, jangan cuma dijadikan tempat numpang tidur. Makan dulu kuenya mumpung krimnya belum lumer."
        chiasa "Iya, ini dimakan kok. Eh, potongan punya Ko-nii stroberinya jatuh miring ke pinggir piring tuh."
        koita "Biarin aja, rasanya tetap sama di perut. Habis ini jangan rebutan cuci piring ya, aku yang nyabunin terus kamu yang bilas."
        chiasa "Sip, asal air hangatnya dinyalain dulu biar tangan nggak beku."
        koita "Pastilah kunyalakan keran air hangatnya, masa malam Natal bikin jari adik sendiri beku di bak cuci."
        chiasa "Habis cuci piring nanti kita tonton acara musik akhir tahun di ruang tengah sebentar ya, Ko-nii."
        koita "Boleh, sambil kita habiskan sisa teh hangat di teko."
        nar "Koita bangkit mengumpulkan mangkuk sup yang sudah kosong dengan senyum tenang yang memenuhi ruang makan rumah Amamiya."
        nar "Kamu menyuap potongan kue bolu yang lembut itu sambil mendengarkan Koita mengoceh santai soal jadwal libur toko buku dekat kampus dan daftar novel yang mau ia baca selama akhir tahun. Lampu hias mungil di atas bufet terus berpendar tenang sampai piring kalian bersih."
    elif _return == "B":
        nar "Kamu melirik jam dinding ruang tengah yang baru melewati pukul tujuh malam, lalu menatap Koita yang masih berdiri di samping meja."
        chiasa "Sebenarnya aku baru aja janjian mau ngundang teman dari kampus ke rumah malam ini, Ko-nii. Nggak apa-apa kan kalau kami pakai ruang tengah sama meja rendah di sana?"
        nar "Koita yang baru saja mengangkat sendok sayur dari panci menghentikan gerakannya. Ia menoleh dengan alis sedikit terangkat."
        koita "Ngundang teman ke rumah? Malam Natal begini?"
        chiasa "Iya. Dia lagi nggak pulang ke rumah orang tuanya malam ini, terus kebetulan juga belum ada acara. Jadi kuajak mampir makan kue sama minum teh hangat sebentar di sini biar nggak sendirian."
        koita "Tumben banget, Chi-chan. Biasanya kalau malam hari raya begini kamu paling malas kalau ada tamu datang ke rumah. Siapa, anak Fakultas Seni juga?"
        chiasa "Kenalan dekat dari kampus kok. Ko-nii nggak keberatan kan kalau ruang tengahnya kupakai sebentar?"
        koita "Nggak keberatan sih, rumah ini kan rumahmu juga. Cuma aku agak kaget aja dengar kamu ngajak orang mampir mendadak."
        nar "Koita melirik panci sup krim dan loyang ayam panggang di atas kompor, lalu mengambil satu nampan kayu besar dari rak samping serta mengecek rak sandal tamu di dekat lorong depan."
        koita "Sandal tamunya sudah kupastikan bersih dua pasang di rak bawah. Kalau gitu, biar kalian leluasa ngobrolnya tanpa canggung ada kakak cowok mondar-mandir, aku ambil porsiku ke nampan terus makan di kamar atas aja ya."
        chiasa "Lho, beneran nggak apa-apa Ko-nii makan di atas? Maaf banget malah bikin Ko-nii ngungsi ke kamar sendiri."
        koita "Santai aja, aku juga lagi mau lanjut baca novel tebal yang dari minggu lalu belum kelar. Sup sisanya kubiarin di panci dengan api mati, nanti kalau temanmu sudah datang tinggal dipanasin dua menit. Kuenya juga belum kubuka sama sekali kok, potong aja duluan sama temanmu."
        chiasa "Makasih ya, Ko-nii. Nanti kue sisanya kutaruh di kulkas buat Ko-nii juga."
        koita "Iya, gampang. Kalau butuh cangkir teh buat tamu, ambil yang warna putih polos di lemari kedua ya, jangan pakai muk retak punya aku."
        chiasa "Iya, hafal kok. Selamat makan malam, Ko-nii."
        nar "Tidak lama setelah langkah kaki Koita menghilang di tangga lantai dua, bel pintu depan berbunyi dua kali. Kamu bergegas ke lorong depan dan membuka pintu. Udara malam yang dingin berembus masuk bersama sosok gadis yang kamu undang, yang berdiri di teras sambil merapatkan syal di lehernya."
        chiasa "Masuk, masuk. Di luar dingin banget ya anginnya? Untung nggak sampai turun salju basah."
        nar "Ia melepas sepatu dan mantelnya di genkan sambil menggosok kedua telapak tangannya yang kemerahan karena udara malam, lalu memakai sandal tamu yang sudah kamu siapkan dan mengikutimu masuk ke ruang tengah."
        chiasa "Duduk di karpet dekat pemanas itu aja, aku sudah nyalain dari setengah jam lalu biar hangat. Sini bantal duduknya, tunggu sebentar ya, aku panasin sup krim sama seduh teh dulu di dapur."
        nar "Tak lama kemudian kamu kembali dari dapur membawa nampan berisi dua mangkuk sup krim panas yang mengepul, dua cangkir teh putih, serta kotak kue stroberi yang baru dibuka pitanya. Begitu kalian duduk bersebelahan di meja rendah ruang tengah, aroma mentega dan teh hangat segera mengusir sisa hawa dingin dari luar."
        chiasa "Rumah lagi sepi soalnya Ayah sama Ibu lagi kerja di Sapporo, terus Ko-nii sudah naik ke kamarnya di lantai atas. Jadi santai aja, nggak usah jaim, anggap kayak di kamar sendiri."
        nar "Tamu di sebelahmu tersenyum lega melihat suasana ruang tengah yang hangat dan tenang, lalu mencicipi sendok pertama sup krim buatan Koita sambil memuji rasanya yang gurih."
        chiasa "Haha, nanti kusampaikan ke Ko-nii kalau supnya dipuji, bisa langsung besar kepala dia besok pagi. Oh ya, tadi pas jalan dari stasiun ke sini jalanannya masih seramai sore tadi nggak?"
        nar "Ia bercerita pelan soal deretan toko roti dekat stasiun yang antreannya memanjang sampai ke trotoar dan pasangan-pasangan yang berfoto di bawah lampu jalan, sesekali tertawa kecil setiap kali mengomentari keramaian yang justru membuat tubuh makin kedinginan."
        chiasa "Pantesan aku malas banget keluar ke pusat kota malam ini. Lebih enak di sini kan, nggak perlu antre, bisa makan kue stroberi sambil kaki dekat pemanas. Mau potongan yang stroberinya besar nggak? Buat tamu bagian paling bagus dong."
        nar "Kamu memotong kue bolu stroberi dan menggeser piring kecil ke hadapannya. Percakapan kalian mengalir alami tanpa sedikit pun rasa terburu-buru, berpindah dari keluhan soal tugas akhir tahun yang menumpuk, kebiasaan aneh di rumah masing-masing saat libur sekolah dulu, sampai hal-hal kecil yang ingin dilakukan awal Januari nanti."
        chiasa "Kalau nanti sudah lewat jam sembilan dan kamu masih malas pulang kena angin dingin, nggak usah buru-buru kok. Tehnya masih setengah teko lagi, kita habisin pelan-pelan aja di sini."
        nar "Tamu di sebelahmu mengangguk senang sambil merapatkan bantal duduknya ke dekat meja rendah yang hangat oleh pemanas ruangan."
        nar "Dari lantai dua sama sekali tidak terdengar langkah kaki Koita yang turun mengganggu, memberi kalian ruang penuh untuk menikmati sisa kue malam itu."
        nar "Kamu menuangkan sisa teh hangat dari teko ke dalam kedua cangkir putih kalian sambil mendengarkan cerita tamumu tentang rencana libur tahun barunya."
        nar "Di bawah cahaya lampu hias mungil dari atas bufet, malam Natal di ruang tengah itu berjalan hangat dan akrab tanpa satu pun gangguan dari lantai atas."
    elif _return == "C":
        nar "Kamu berjalan ke gantungan pakaian di dekat lorong masuk, mengambil mantel tebal dan syal rajutmu, lalu kembali ke ruang makan untuk mengambil kotak biskuit cokelat yang masih tersegel di sudut meja."
        chiasa "Maaf ya, Ko-nii. Aku mau keluar sebentar malam ini, mau mampir ke rumah Nagisa-senpai."
        nar "Koita yang baru saja menaruh dua mangkuk sup di atas meja langsung menatapmu heran dengan sendok sayur masih di tangannya."
        koita "Ke rumah Nagisa-chan? Sekarang? Memangnya Nagisa-chan ngadain acara kumpul-kumpul di rumahnya malam ini?"
        chiasa "Nggak ada acara apa-apa sih. Tadi aku dengar orang tuanya sama Haru nii-san lagi keluar semua malam ini, jadi dia sendirian di rumah. Makanya aku mau mampir bawain camilan sebentar."
        koita "Tumben banget kamu kepikiran nyamperin Nagisa-chan sendirian malam Natal begini, Chi-chan. Biasanya kalau ketemu di kampus aja kalian masih suka saling sindir dulu sebelum ngobrol normal."
        chiasa "Sesekali akur kan nggak ada salahnya, Ko-nii. Lagian Ko-nii nggak perlu ikut repot, makan malam duluan aja di sini biar supnya nggak keburu dingin."
        koita "Lho, kamu nggak makan sup dulu setengah mangkuk biar perutmu hangat di jalan?"
        chiasa "Nanti aja di sana atau pas pulang. Kalau aku berangkat terlalu malam nanti malah kemalaman ketuk pintu rumahnya."
        koita "Oh... ya sudah, hati-hati di jalan ya. Pakai sarung tanganmu, di luar anginnya kencang. Kalau sudah mau pulang terus jalanannya sepi, kirim pesan aja biar kujemput di belokan."
        chiasa "Iya, aman kok cuma tiga blok. Aku pergi dulu ya, Ko-nii."
        nar "Kamu melangkah keluar menembus jalanan perumahan yang dingin. Lampu-lampu teras tetangga memantul di atas aspal kering sepanjang tiga blok menuju kediaman keluarga Sakurajima. Begitu sampai di depan pagar kayunya, kamu menekan tombol bel di samping pintu."
        nar "Beberapa detik kemudian, suara langkah cepat terdengar dari dalam dan kunci pintu diputar terbuka. Nagisa muncul mengenakan kaus lengan panjang yang dilapisi kardigan rajut krem tebal, dengan rambut pirang kembarnya yang digerai longgar di bahu. Begitu melihat siapa yang berdiri di teras, matanya langsung melebar."
        nagisa "Chiasa?! Kamu ngapain berdiri di depan pintu rumahku malam-malam begini?"
        nar "Nagisa refleks menjulurkan kepalanya sedikit melewati bahumu untuk melihat ke arah pagar jalanan yang kosong, lalu menoleh ke kanan dan kiri sebelum kembali menatapmu dengan kening berkerut."
        nagisa "...Tunggu dulu. Kamu beneran datang sendirian? Nggak bareng Ko-kun?"
        chiasa "Sendirian lah, Nagisa-senpai. Memangnya kalau aku jalan ke rumah Senpai harus selalu pakai pengawalan Ko-nii? Ini aku bawa biskuit cokelat hangat, tanganku sudah beku nih, aku nggak disuruh masuk?"
        nagisa "Y-ya masuk aja! Siapa juga yang nyuruh kamu berdiri terus di luar, nanti kalau kamu flu malah aku yang disalahin Ko-kun!"
        nar "Nagisa bergeser membuka pintu lebih lebar. Setelah kamu melepas sepatu dan mantel di genkan, ia mengajakmu naik ke kamarnya di lantai dua karena ruang tamu di bawah terlalu luas dan dingin untuk duduk berdua."
        nar "Begitu pintu kamar dibuka, Nagisa buru-buru melangkah mendahuluimu, memindahkan tumpukan gulungan kertas kalkir, penggaris skala, dan kotak pensil warna dari atas kursi serta karpet ke pinggir lemari. Di sudut kasurnya yang rapi, boneka kelinci putihnya duduk bersandar di dekat bantal."
        nagisa "Maaf agak berantakan, tadi sore aku baru beresin revisi sketsa tugas studio. Duduk di dekat meja bundar situ aja, pemanasnya baru kunyalain lima menit lalu."
        chiasa "Kamar Senpai hangat kok, wangi kayu pensil sama pelembut baju. Orang rumah beneran lagi pada keluar semua ya?"
        nagisa "Iya, Ayah sama Ibu makan malam di rumah kenalan lama mereka, Onii-chan masih kejebak lembur acara akhir tahun kantornya. Makanya tadi pas bel bunyi aku kaget setengah mati. Kukira kurir paket salah alamat atau tetangga mau pinjam sesuatu."
        nar "Ia duduk di tepi karpet dekat meja bundar sambil memeluk bantal kecil di pangkuannya, masih menatapmu dengan tatapan setengah curiga dan setengah salah tingkah."
        nagisa "Jujur deh, Chiasa. Tumben banget kamu ke sini malam Natal nggak pakai acara nyindir atau pamer lagi makan malam berdua di rumah Amamiya. Ada maunya apa sih? Jangan bilang kamu mau minta bantuan tugas?"
        chiasa "Nggak ada tugas apa-apa kok, Nagisa-senpai. Tadi pas di rumah aku kepikiran Senpai pasti lagi sendirian di sini, terus aku juga beneran pengin ngobrol sama Senpai tanpa bahas Ko-nii atau urusan kampus. Emang aneh banget ya?"
        nar "Ujung telinga Nagisa langsung memerah di sela rambut pirangnya yang tergerai. Ia memalingkan wajah sedikit ke arah lemari buku sambil berdeham kaku."
        nagisa "...Nggak aneh sih. Cuma nggak biasa aja dengar kamu ngomong lurus tanpa sindiran begitu. Bikin kaget tahu nggak."
        chiasa "Berarti mulai sekarang harus kubiasain ya, biar Senpai nggak kaget terus?"
        nagisa "H-hei, jangan mulai ngeledek lagi! Tunggu sebentar di sini, jangan buka kotak biskuitnya duluan, aku turun bikin cokelat panas dua cangkir ke dapur!"
        chiasa "Jangan lama-lama ya, Senpai! Kalau ada marshmallow boleh juga tuh!"
        nagisa "Banyak maunya banget sih tamu satu ini!"
        nar "Meski menggerutu, langkah kaki Nagisa menuruni tangga terdengar jauh lebih ringan daripada saat membuka pintu tadi. Tidak sampai lima menit, ia kembali masuk membawa nampan kayu berisi dua cangkir cokelat panas yang mengepul tebal, lengkap dengan dua butir marshmallow putih mengapung di atas masing-masing cangkir."
        chiasa "Wah, beneran ada marshmallow-nya! Makasih, Nagisa-senpai."
        nagisa "Kebetulan aja ada sisa di rak atas dapur, jangan geer dulu. Sini buka biskuitnya, aku mau lihat rasa apa yang kamu bawa."
        nar "Kamu membuka segel kotak biskuit cokelat itu dan meletakkannya di tengah meja bundar. Sambil meniup cokelat panas yang manis, obrolan kalian mengalir tanpa kecanggungan sedikit pun, mulai dari acara musik televisi akhir tahun yang terdengar sayup dari lantai bawah, dosen studio yang hobi mengubah tenggat di detik terakhir, sampai kebiasaan tidur larut saat mengerjakan tugas."
        chiasa "Tapi jujur aja nih, Senpai. Tadi sebelum aku pencet bel, rumah ini sepi banget ya?"
        nar "Nagisa terdiam sebentar, menatap pusaran cokelat di cangkirnya dengan kedua telapak tangan melingkari keramik hangat itu. Suaranya turun lebih pelan daripada biasanya."
        nagisa "...Lumayan sih. Tadinya aku mikir mau cepat-cepat tidur jam sembilan aja biar malamnya cepat lewat. Tapi... ya, untung juga tadi kamu nggak jadi malas jalan kaki ke sini."
        chiasa "Kalau gitu tahun depan kalau rumah Senpai sepi lagi, nggak usah nunggu aku nebak. Kirim pesan aja langsung, nanti kubawain biskuit dua kotak."
        nagisa "Hmph, lihat nanti aja deh. Nih, ambil biskuitnya lagi, mumpung cokelatmu belum dingin."
        nar "Di kamar lantai dua yang hangat itu, tawa pelan kalian berdua mengisi sisa malam hingga jarum jam di dinding melewati tengah malam."
    else:
        nar "Kamu menggeleng pelan sambil tetap berdiri di dekat anak tangga, tidak melangkah mendekati kursi makan yang sudah ditarik Koita."
        chiasa "Maaf ya, Ko-nii. Malam ini aku lagi pengin istirahat sendiri aja di kamar. Ko-nii makan duluan aja, nggak usah nungguin aku."
        nar "Tangan Koita yang masih memegangi sandaran kursi kayu perlahan turun. Senyum santai di wajahnya surut ketika matanya jatuh pada dua mangkuk sup krim yang sudah telanjur mengepul di atas meja."
        koita "Lho, kok gitu, Chi-chan? Kamu nggak enak badan? Atau tadi di kampus ada teman yang bikin kesal?"
        chiasa "Nggak sakit kok, di kampus juga nggak ada kejadian apa-apa. Cuma kepalaku rasanya agak penuh aja, lagi pengin diam di kamar malam ini."
        koita "Tapi ini kan malam Natal, Chi-chan. Masa kamu nggak makan malam sama sekali? Kalau kamu malas duduk di bawah sini, biar kuambilin nampan terus kubawain semangkuk sup sama ayam panggang ke kamarmu di atas ya? Aku taruh depan pintu aja kalau kamu nggak mau diganggu."
        chiasa "Beneran nggak usah repot-repot, Ko-nii. Perutku juga belum lapar. Aku cuma mau seduh susu hangat satu muk terus langsung istirahat."
        nar "Koita terdiam beberapa detik di samping meja makan. Ia melirik kotak kue stroberi yang masih terikat pita merah di tengah taplak kotak-kotak, lalu menghela napas pendek."
        koita "...Akhir-akhir ini kadang aku ngerasa kamu kayak sengaja ambil jarak di rumah, Chi-chan. Aku tahu kamu sudah kuliah dan butuh ruang sendiri, tapi kalau aku ada salah ngomong atau bikin kamu nggak nyaman, bilang aja terus terang lho."
        chiasa "Nggak ada yang salah sama Ko-nii kok. Beneran. Aku cuma lagi butuh waktu sendirian buat nenangin kepala aja. Selamat malam ya, Ko-nii."
        koita "...Iya deh, aku nggak maksa. Kalau nanti tengah malam kamu kebangun terus lapar, supnya masih ada di panci dan kuenya kusimpan di rak tengah kulkas ya. Tinggal ambil aja kapan pun mau."
        chiasa "Makasih, Ko-nii. Jangan lupa matiin pemanas bawah kalau sudah selesai makan."
        koita "Iya, nanti kupastikan mati semua sebelum aku naik ke kamar."
        nar "Koita duduk perlahan di kursinya seorang diri dan mulai menyendok sup krim yang sudah mulai turun uap panasnya."
        nar "Di atas meja makan itu, piring kedua yang tadinya sudah disiapkan untukmu tampak tetap bersih di samping kotak kue yang belum disentuh."
        nar "Kamu melangkah sebentar ke dapur untuk memanaskan satu muk susu tawar di microwave. Selama tiga puluh detik menunggu bunyi denting, tidak ada satu pun dari kalian yang menambah kalimat; hanya dengung pelan pemanas ruangan dan bunyi sendok Koita yang merapikan piring di meja."
        nar "Begitu susu hangat di tangan, kamu berjalan menaiki tangga kayu dan menutup pintu kamarmu di lantai dua, meninggalkan Koita duduk seorang diri di ruang makan bawah yang terasa terlalu sunyi."
        nar "Di dalam kamar, kamu mematikan lampu langit-langit dan hanya menyalakan lampu baca kecil di sudut meja belajar. Sambil menyesap susu hangat di tepi kasur dan memandangi embun di kaca jendela, malam itu akhirnya berjalan tenang tanpa ada satu pun tatapan di rumah ini yang menuntutmu bersandiwara."
    return

# ┌─ PANDUAN CERITA · C07 · Coklat untuk Banyak Orang
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Valentine.
# │ INTI    : A coklat untuk Koita / B untuk heroine tertentu / C untuk Yutaka / D tidak memberi.
# │ AKHIRAN : gerbang jalur yuri/Koita Success/Yutaka.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C07:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Valentine")
    nar "Malam di dapur Rumah Amamiya terasa hangat oleh aroma cokelat hitam leleh, mentega, dan parutan kulit jeruk manis. Pemanas ruangan di ruang tengah berdengung pelan sementara angin dingin pertengahan Februari sesekali mengetuk kaca jendela belakang."
    nar "Di atas meja makan kayu yang sudah kamu alasi kertas minyak, berjajar potongan cokelat ganache yang baru selesai kamu dinginkan, dua gulung pita satin berwarna cokelat tua dan krem, sebuah kotak karton polos ukuran sedang, serta setumpuk kartu ucapan kecil yang seluruhnya masih kosong."
    nar "Kamu mencicipi satu remah pinggiran di ujung loyang untuk memastikan rasa pahit cokelat dan segarnya kulit jeruk tidak berlebihan, lalu melepas celemek dan duduk di kursi sambil memandangi kotak yang sudah tertata rapi di hadapanmu. Belum ada satu nama pun yang kamu tulis di atas kartu kertas itu. Selama berbulan-bulan tinggal di dunia ini, kamu sudah menyaksikan berkali-kali betapa mudahnya satu hadiah kecil berubah menjadi harapan yang rumit kalau maksud di baliknya sengaja dibiarkan samar."
    nar "Dari lantai atas terdengar samar bunyi pintu kamar dibuka lalu langkah kaki Koita melintas menuju kamar mandi sebelum kembali masuk. Tubuh Amamiya Chiasa memang menyimpan kebiasaan lama untuk selalu menyiapkan cokelat setiap pertengahan Februari, tetapi malam ini kamu sendiri yang menentukan ke tangan siapa kotak di meja ini akan sampai."
    nar "Di dalam laci bufet dapur, kamu sempat melihat buku catatan resep lama milik Chiasa yang halaman tengahnya penuh coretan takaran gula kesukaan kakaknya dari tahun ke tahun."
    nar "Namun resep cokelat hitam dengan parutan kulit jeruk yang baru saja kamu selesaikan di atas meja ini adalah takaran yang kamu pilih sendiri sore tadi."
    nar "Cahaya lampu gantung ruang makan memantul lembut di atas permukaan pita satin yang masih tergulung rapi di samping gunting."
    nar "Kamu mengambil pena tinta hitam di dekat tumpukan kartu ucapan kosong sambil menimbang langkah mana yang ingin kamu kunci pada malam tanggal empat belas Februari ini."
    nar "Jam dinding di ruang tengah berdetak teratur melewati pukul sembilan malam sementara uap teh hangat di sudut meja perlahan menipis."
    nar "Setiap potong cokelat yang tersusun di dalam kotak karton polos itu telah kamu siapkan dengan tanganmu sendiri dari tahap melelehkan bahan hingga menata kemasannya."
    nar "Di dalam rumah yang tenang ini, tidak ada seorang pun yang memaksamu mengikuti kebiasaan lama pemilik tubuh ini."
    nar "Sebuah kartu kecil dapat menjadi awal dari pengakuan yang sungguh-sungguh, atau justru tetap kosong tanpa mengikat siapa pun."
    nar "Kamu merapikan letak kotak karton tersebut di tengah alas kertas minyak sambil menatap ujung pena di jarimu."
    nar "Kini hanya tersisa satu keputusan terakhir mengenai siapa yang berhak menerima kartu ucapan di samping kotak tersebut."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Tulis nama Koita dan berikan kotak cokelat ini padanya.", "Tulis pesan untuk perempuan yang kamu sukai dan temui dia.", "Bawa kotak cokelat ini untuk diberikan kepada Yutaka.", "Biarkan tanpa nama dan simpan untuk dimakan sendiri saja."])]
    call screen kk_choice_panel(_rows, "Pilihan")
    $ kk_record_choice("C07", _return)
    if _return == "A":
        nar "Kamu menarik satu lembar kartu krem kosong, mengambil pena tinta hitam, lalu menuliskan beberapa baris kalimat pendek dengan tulisan yang rapi tanpa embel-embel candaan. Setelah menyelipkan kartu itu di dalam tutup kotak dan mengikat pita cokelat tuanya hingga kencang, kamu mengangkat kotak itu dan berjalan menuju ruang tengah."
        nar "Tidak lama kemudian, langkah kaki Koita terdengar menuruni tangga kayu sambil membawa gelas kosong untuk diisi air di dapur. Begitu melihatmu berdiri di dekat meja makan dengan kotak cokelat berpita rapi di kedua tangan, langkahnya melambat."
        koita "Lho, Chi-chan belum tidur? Wah, pantesan bau cokelat sama kulit jeruknya naik sampai ke tangga atas dari tadi. Kamu bikin sendiri itu?"
        chiasa "Iya, baru aja beres didinginin sama dibungkus. Tadi sempat kucicipi pinggirannya biar nggak terlalu pahit. Nih, buat Ko-nii."
        nar "Kamu melangkah maju dan menyodorkan kotak karton krem itu langsung ke hadapannya. Koita menatap kotak tersebut dengan mata agak melebar sebelum menerimanya dengan kedua tangan."
        koita "Buat aku? Makasih banyak, Chi-chan! Wah, seperti biasa adikku memang paling rajin kalau sudah tanggal empat belas..."
        nar "Kalimat santai Koita terhenti sendiri di tengah jalan. Ia melihat raut wajahmu yang tenang dan tidak melontarkan godaan jahil seperti biasanya, lalu pandangannya turun ke pita satin yang diikat terlalu teliti dan ujung kartu kertas yang menyembul rapi dari balik tutup kotak."
        koita "...Sebentar, Chi-chan. Kenapa kamu lihatin aku serius banget begitu?"
        chiasa "Soalnya aku nggak mau Ko-nii asal nerima sambil mikir ini cuma cokelat kewajiban tahunan dari adik ke kakak. Di dalamnya ada kartu yang kutulis sendiri. Aku mau Ko-nii baca baik-baik."
        nar "Koita terdiam cukup lama di depan meja makan. Jarinya yang memegangi sisi kotak tampak sedikit menegang. Ia sempat melirik ke arah gelas kosong di meja dapur, seolah naluri lamanya baru saja mencari alasan ringan untuk mengalihkan suasana, lalu mengurungkannya."
        koita "Jujur aja, barusan aku hampir otomatis bilang makasih buat cokelat adiknya, Chi-chan. Kalau aku ngomong gitu terus ketawa, semuanya langsung beres dan nggak ada yang perlu repot dipikirin."
        chiasa "Terus kenapa Ko-nii nggak jadi ngomong begitu?"
        koita "Karena aku lihat matamu sekarang. Kamu nggak lagi bercanda, kan? Aku mau tahu maksudmu yang sebenarnya, jangan sampai aku sok memutuskan sendiri artinya sebelum benar-benar mendengar dari kamu."
        chiasa "Bagus deh kalau Ko-nii akhirnya nggak langsung kabur pakai candaan. Aku nggak minta Ko-nii kasih jawaban malam ini juga kok. Cuma mulai hari ini, aku nggak mau Ko-nii pura-pura nggak dengar setiap kali aku ngomong serius."
        koita "...Sudah berapa lama kamu mikirin hal kayak gini sendirian, Chi-chan?"
        chiasa "Cukup lama sampai aku capek lihat Ko-nii selalu sembunyi di balik kalimat kakak-adik tiap ada hal yang agak susah dijawab."
        koita "Hah... kena telak banget kalimatmu malam ini. Rasanya jantungku malah jadi deg-degan sendiri padahal ini di ruang makan rumah kita."
        chiasa "Ya sudah, jangan sampai gelas minumnya lupa diisi nanti haus tengah malam. Kuenya juga jangan ditaruh di dekat pemanas biar cokelatnya nggak lumer."
        koita "Iya, bakal kujaga baik-baik kok."
        nar "Koita tersenyum tipis yang sedikit canggung lalu mengangguk pelan. Alih-alih menaruh kotak cokelatmu di atas bufet ruang tengah bersama camilan rumah lainnya, ia membawanya terpisah dengan kedua tangan menuju anak tangga."
        koita "Biar kubawa ke kamar dan kubaca kartunya pelan-pelan di atas ya, Chi-chan. Makasih banyak buat cokelatnya. Selamat malam."
        chiasa "Selamat malam, Ko-nii."
        koita "Jangan lupa matikan kompor sama lampu dapur sebelum kamu naik tidur juga ya."
        chiasa "Iya, ini tinggal kurapikan kertas minyaknya sebentar terus aku langsung naik."
        nar "Kamu memperhatikan punggung Koita yang melangkah menaiki anak tangga kayu dengan gerakan yang jauh lebih perlahan daripada saat ia turun membawa gelas tadi."
        nar "Kotak karton berpita cokelat tua di tangannya tampak dipegang erat seolah ia khawatir simpul pitanya bergeser sedikit saja."
        nar "Kamu melipat kertas minyak yang tersisa di atas meja makan dan memasukkannya ke tempat sampah dapur dengan perasaan yang tenang."
        nar "Dengan memotong kebiasaannya bersembunyi di balik candaan kakak-beradik sejak awal, kamu telah memaksanya menghadapi isi kartu itu secara utuh."
        nar "Dari lantai dua terdengar bunyi pintu kamar Koita yang ditutup perlahan tanpa suara langkah tambahan lagi."
        nar "Kamu menuangkan segelas air hangat dari ketel dapur untuk dirimu sendiri sambil menatap tangga kayu yang kini lengang."
        nar "Keheningan di ruang makan malam ini tidak lagi terasa seperti rutinitas biasa, melainkan awal dari perubahan yang tidak bisa lagi ia abaikan."
        nar "Kamu mematikan lampu dapur satu per satu sebelum melangkah naik menuju kamarmu sendiri di lantai atas."
        nar "Setengah jalan menaiki tangga kayu, ia sempat berhenti satu detik dan menoleh sekilas ke arahmu sebelum melanjutkan langkah ke lantai dua. Belum ada jawaban pasti malam ini, tetapi untuk pertama kalinya ia tidak lari dari pertanyaan yang kamu letakkan di depannya."
    elif _return == "B":
        nar "Kamu menarik satu lembar kartu ucapan kosong dan menggenggam pena tinta hitam cukup lama sebelum mulai menulis. Kamu tidak menuliskan kalimat basa-basi yang bisa disalahpahami sebagai sekadar tukar-menukar camilan Valentine antar mahasiswi. Kamu menuliskan dengan kalimat pendek dan jujur bahwa kamu memang sengaja membuatnya khusus untuknya."
        nar "Setelah mengikat pita krem di sekeliling kotak dan memasukkannya ke dalam kantong kertas kecil, kamu mengambil ponsel lalu mengirim pesan kepadanya, menanyakan apakah ia masih terjaga dan bersedia bertemu sebentar di dekat kedai minuman hangat dekat stasiun. Kurang dari lima menit kemudian, balasannya masuk mengiyakan."
        nar "Kamu mengenakan mantel dan syal rajut, menyelinap keluar rumah menembus udara malam Februari yang dingin, lalu berjalan cepat menyusuri trotoar yang mulai sepi. Di bawah lampu jalan depan kedai yang hangat, sosok perempuan yang kamu tunggu sudah berdiri sambil menggosok kedua telapak tangannya."
        chiasa "Maaf ya ngajak keluar malam-malam pas anginnya lagi dingin banget begini. Tanganmu sampai merah begitu, tunggu sebentar, aku beliin minuman hangat dulu dari loket depan situ ya?"
        nar "Ia menggeleng cepat dengan senyum lembut dan menjawab bahwa ia baru saja sampai dua menit lalu dan memang belum mengantuk, lalu melirik kantong kertas yang sejak tadi kamu dekap di depan mantelmu."
        chiasa "Tetap aja, pegang gelas hangat dulu biar nggak beku. Nah, ini satu buat kamu... terus sebenarnya ada satu hal lagi yang mau kukasih langsung malam ini."
        nar "Setelah ia menggenggam cangkir kertas hangat dengan satu tangan, kamu mengeluarkan kotak berpita krem dari dalam kantong kertas dan menyerahkannya dengan kedua tangan. Ia menerimanya sambil tertawa kecil, awalnya mengira kamu hanya sedang membagi kelebihan cokelat buatan rumah seperti yang biasa dilakukan teman-teman kuliah."
        chiasa "Ini kubikin sendiri tadi di rumah, ada sedikit parutan kulit jeruk biar nggak terlalu manis. Oh ya... di balik pitanya ada kartu kecil. Nggak usah langsung dijawab sekarang kok, aku cuma mau kamu baca sendiri nanti."
        nar "Ia sempat tertegun mendengar nada bicaramu yang tidak sedang bercanda. Dengan hati-hati ia menarik kartu kecil di balik pita, membacanya di bawah cahaya kuning lampu kedai, dan senyum sopan di wajahnya perlahan berhenti. Pipinya sedikit merona saat ia kembali mengangkat pandangannya ke arahmu."
        chiasa "Aku tahu kedengarannya agak mendadak, dan kamu sama sekali nggak wajib membalas apa-apa malam ini. Aku cuma nggak mau kasih hadiah manis terus membiarkan kamu nebak-nebak sendiri maksudku apa."
        nar "Ia menunduk menatap kartu di tangannya selama beberapa detik sebelum memasukkannya kembali ke dalam kotak dengan sangat hati-hati, lalu menyimpannya ke dalam tas selempangnya."
        chiasa "Eh, jangan sampai cokelatnya kegencet buku catatan di dalam tas ya, tadi krim ganachenya lumayan lembut."
        nar "Kalimat ringanmu membuat ketegangan di bahunya langsung melonggar; ia tertawa pelan sambil memindahkan letak kotak itu ke ruang tas yang paling lapang."
        chiasa "Kalau kamu sudah kedinginan di sini, ayo jalan pelan-pelan bareng ke arah persimpangan. Sekalian kuantar sampai dekat lampu jalan besar biar aman. Minumannya dihabisin di jalan aja mumpung masih panas."
        nar "Ia mengangguk dengan pipi yang masih bersemu merah muda di balik syal wolnya, lalu melangkah rapat di sampingmu meninggalkan cahaya lampu kedai."
        nar "Sepanjang jalan menuju persimpangan utama, ia sesekali menyentuh sisi tas selempangnya untuk memastikan kotak cokelat pemberianmu tetap tersimpan tegak di dalam sana."
        chiasa "Nanti kalau sudah sampai di rumah dan sudah dicicipi cokelatnya, kirim pesan ke aku ya, aku pengin tahu rasa jeruknya pas atau nggak di lidahmu."
        nar "Ia tersenyum hangat dan berjanji akan langsung menghubungimu begitu tiba di kamarnya malam ini."
        nar "Angin malam pertengahan Februari masih berembus dingin di sepanjang trotoar, tetapi langkah kaki kalian berdua terasa jauh lebih ringan dan searah."
        nar "Tidak ada lagi keraguan tentang bagaimana perasaanmu akan dibaca olehnya setelah kartu tulisan tangan itu berpindah ke genggamannya."
        nar "Lampu-lampu jalan perumahan memantulkan bayangan kalian berdua yang berjalan berdampingan di atas aspal kering yang dingin."
        nar "Ketika tiba di persimpangan dekat rumahnya, ia sempat berhenti sejenak untuk melambaikan tangan dengan senyum yang masih tampak tersipu."
        nar "Kamu membalas lambaian tangannya sebelum berbalik melangkah pulang menuju rumah Amamiya dengan hati yang terasa hangat."
        nar "Udara dingin bulan Februari tidak lagi terasa menusuk saat kamu membuka kembali pintu pagar rumahmu."
        nar "Dengan suara yang jauh lebih pelan dan hangat daripada sebelumnya, ia mengucapkan terima kasih karena kamu mau mengatakannya dengan jelas, lalu melangkah sejajar di sampingmu menyusuri trotoar yang tenang sebelum kalian berpisah pulang ke rumah masing-masing."
    elif _return == "C":
        nar "Kamu menarik kartu ucapan berwarna gading, menuliskan nama Yutaka-kun di bagian atas diikuti dua baris kalimat pendek yang jujur dan tidak bertele-tele, lalu menyelipkannya rapi di bawah simpul pita cokelat tua. Selesai memasukkan kotak itu ke kantong kertas kecil, kamu mengirim pesan ke Yutaka menanyakan apakah ia ada di apartemen malam ini."
        nar "Belum sampai dua menit, ponselmu bergetar oleh balasan singkatnya yang mengatakan ia baru selesai mandi dan sedang di ruang tamu, bertanya balik ada urusan penting apa malam-malam. Kamu menjawab akan mampir sebentar ke depan lobi apartemennya dalam lima belas menit."
        nar "Kamu mengenakan mantel tebal dan baru saja hendak memasang sepatu di lorong depan ketika pintu tangga lantai dua berderit. Koita melongok dari atas pegangan tangga dengan rambut agak berantakan."
        koita "Eh, Chi-chan? Sudah malam begini mau ke mana pakai mantel tebal segala?"
        chiasa "Mau keluar sebentar aja, Ko-nii. Mau mampir ke tempat Yutaka-kun buat kasih cokelat Valentine."
        nar "Koita terdiam di anak tangga atas. Pandangannya turun ke kantong kertas kecil berpita di tanganmu, lalu kembali ke wajahmu dengan senyum yang terasa sedikit melambat."
        koita "Oh... buat Yutaka? Tumben banget kamu sampai jalan kaki jauh ke Distrik Elite malam-malam. Biasanya kan tinggal kasih besok di kampus pas ketemu."
        chiasa "Mumpung cokelatnya baru matang aja kok, Ko-nii. Lagian aku memang mau ngasih langsung hari ini. Aku pergi sebentar ya, nggak lama."
        koita "...Iya, hati-hati di jalan ya. Pakai sarung tanganmu, kalau pulang kemalaman kabari aku biar kujemput di persimpangan."
        chiasa "Siap, Ko-nii."
        nar "Kamu melangkah keluar menembus angin dingin Februari menuju Distrik Elite. Tepat saat kamu tiba di halaman depan gedung apartemen yang berpenerangan hangat, pintu kaca lobi didorong terbuka dan Yutaka keluar mengenakan jaket navy di atas kaus rumahan dengan ekspresi setengah penasaran."
        yutaka "Seriusan kamu jalan kaki ke sini malam-malam, Chiasa? Anginnya dingin banget lho. Ada urusan mendadak soal Koita, atau rumah lagi kehabisan sesuatu?"
        chiasa "Nggak ada urusan soal Ko-nii kok, Yutaka-kun. Rumah juga aman. Aku ke sini memang khusus buat ketemu Yutaka-kun."
        nar "Kamu mengangkat kantong kertas kecil itu lalu mengeluarkan kotak cokelat berpita cokelat tua dan menyodorkannya ke depan dadanya."
        chiasa "Selamat hari Valentine, Yutaka-kun. Ini kubikin sendiri tadi di rumah, pakai cokelat hitam sama sedikit kulit jeruk biar nggak terlalu manis."
        nar "Yutaka mengerjap, raut jahil yang tadinya siap melontarkan ledekan langsung lenyap. Ia meraih kotak itu dengan kedua tangannya, memegangnya hati-hati seolah benda itu jauh lebih berat daripada sekotak cokelat biasa."
        yutaka "...Buat aku? Beneran buat aku, Chiasa? Ini nggak ketukar sama kotak yang harusnya buat orang lain?"
        chiasa "Nggak mungkin ketukar lah, namamu kutulis jelas di kartunya kok."
        yutaka "Boleh kubuka sekarang kartunya?"
        chiasa "Buka aja sekarang nggak apa-apa."
        nar "Di bawah lampu lobi yang terang, Yutaka menarik kartu gading dari selipan pita tanpa menertawakan kegugupanmu sedikit pun. Kamu memperhatikan mata abu-abu gelapnya menyusuri dua baris tulisan tanganmu. Senyum santai khas teman masa kecil yang biasa ia kenakan perlahan berubah menjadi tatapan yang jauh lebih serius."
        yutaka "...Chiasa. Kamu sadar kan kalau nulis kalimat kayak gini di kartu Valentine, aku nggak bakal bisa anggap ini cuma cokelat kewajiban dari adiknya Koita?"
        chiasa "Iya, aku sadar kok. Makanya aku nulisnya jelas begitu dan nganterin sendiri malam ini."
        yutaka "Jujur aja, aku baru pertama kali sampai kehabisan bahan ledekan di depanmu begini. Tadi kukira kamu cuma mau nitip sesuatu buat besok."
        chiasa "Kalau cuma nitip barang, mana mau aku jalan kaki nembus angin Februari sampai ke Distrik Elite, Yutaka-kun."
        yutaka "Haha... iya juga sih. Kena skakmat aku malam ini."
        nar "Yutaka mengembuskan napas pelan sambil tersenyum tipis, kali ini tanpa sedikit pun nada bercanda di suaranya. Ia memasukkan kotak itu hati-hati ke saku bagian dalam jaketnya, lalu melirik kedua tanganmu yang memerah karena angin."
        yutaka "Tanganmu sudah dingin banget begitu. Tunggu sebentar di sini ya, jangan langsung pulang jalan kaki sendirian. Aku ambil kunci sama dompet dulu di dalam, habis itu kita beli minuman hangat di kedai pojok jalan sekalian kuantar kamu sampai depan rumah."
        chiasa "Nggak merepotkan, Yutaka-kun? Tadi katanya baru selesai mandi."
        yutaka "Sama sekali nggak. Lagian kalau kubiarkan kamu jalan balik sendirian malam-malam begini, besok aku bisa diomelin Koita... dan aku sendiri juga nggak tenang. Tunggu dua menit."
        chiasa "Oke, aku tunggu di sini ya. Jangan lupa pakai syal, rambutmu masih agak lembap tuh."
        yutaka "Siap, bawel juga ternyata."
        nar "Tidak sampai dua menit kemudian, Yutaka sudah kembali keluar melewati pintu kaca lobi dengan syal abu-abu melilit lehernya dan dua kaleng teh susu panas di tangannya."
        yutaka "Nih, pegang satu buat ngangetin jari-jarimu sepanjang jalan pulang. Ayo, aku antar sampai depan pagar rumahmu."
        chiasa "Makasih banyak, Yutaka-kun. Hangat banget kalengnya."
        yutaka "Jangan lupa nanti kalau aku sudah selesai habisin cokelatnya, bagian kamu yang harus siap-siap nunggu balasan dariku bulan depan."
        chiasa "Hehe, bakal kutunggu tanggal empat belas Maret nanti."
        nar "Kalian berdua berjalan berdampingan menyusuri trotoar Distrik Elite yang tenang sambil berbagi kehangatan kaleng minuman di tengah udara malam."
        yutaka "Ngomong-ngomong, kulit jeruk yang kamu pakai di cokelat tadi wangi banget, dari luar kotaknya saja sudah kecium tipis."
        chiasa "Tadi kuparut sendiri dari jeruk segar yang ada di keranjang dapur supaya aromanya nggak hilang."
        yutaka "Pantas saja wanginya beda sama cokelat toko. Nanti sampai kamar langsung kucicipi sambil minum kopi hangat."
        chiasa "Jangan minum kopi terlalu malam nanti kamu malah susah tidur, Yutaka-kun."
        yutaka "Haha, kalau susah tidur gara-gara habis dapat cokelat darimu sih kayaknya nggak masalah."
        nar "Tawa pelan Yutaka di sepanjang perjalanan mengantarmu pulang membuat jarak antara Distrik Elite dan perumahan Amamiya terasa jauh lebih singkat malam ini."
        nar "Yutaka berbalik masuk ke lobi dengan langkah cepat, meninggalkan angin malam yang entah mengapa terasa jauh lebih ringan saat kamu menunggunya di depan pintu kaca."
    else:
        nar "Kamu memandangi deretan kartu ucapan yang masih kosong itu cukup lama, lalu meletakkan kembali pena tinta hitam ke samping kotak. Tidak ada satu nama pun yang terasa perlu kamu tulis malam ini."
        nar "Kamu melepas gulungan pita satin dan menyingkirkannya ke laci meja, membuka kembali penutup kotak, lalu berjalan ke dapur untuk menyeduh secangkir teh hitam hangat. Sisa potongan cokelat ganache yang dingin di atas kertas minyak kamu pindahkan ke piring keramik kecil, mengambil garpu kue, lalu duduk santai di ruang makan."
        nar "Rasa cokelat hitam yang sedikit pahit berpadu dengan parutan kulit jeruk terasa seimbang di lidah. Tak lama kemudian, Koita turun dari lantai dua mengenakan kaus longgar untuk mengambil air minum di kulkas. Ia melirik piring cokelat di depanmu sambil menaikkan alis."
        koita "Lho, Chi-chan? Bikin cokelat banyak begitu, nggak dibungkus buat dikasih ke teman-teman fakultas besok?"
        chiasa "Nggak ah, Ko-nii. Tadi cuma lagi pengin nyoba resep baru aja buat dimakan sendiri sambil santai habis tugas selesai."
        koita "Hahaha, dasar. Tumben banget bikin ganache segala cuma buat camilan tengah malam. Boleh minta cicip satu potongan pinggirannya nggak? Wangi jeruknya enak banget tuh."
        chiasa "Ambil aja yang di ujung loyang situ, bentuknya agak miring gara-gara pisauku kurang hangat tadi."
        nar "Koita mengambil satu potongan kecil, mengunyahnya sebentar, lalu matanya langsung melebar senang."
        koita "Wah, lumayan pas manisnya, nggak bikin enek sama sekali! Ini kalau kamu bungkus rapi terus jual di bazar kampus pasti langsung ludes lho, Chi-chan."
        chiasa "Malas ah, bikin satu loyang aja dapur sudah berantakan begini. Mending dimakan sendiri sambil minum teh hangat."
        koita "Bener juga sih. Eh, kalau Ibu pulang besok terus lihat dapur bau cokelat tapi kuenya sudah habis separuh, pasti langsung nanya siapa yang bikin."
        chiasa "Biarin aja, tinggal bilang Ko-nii ikut bantu ngabisin pinggirannya."
        koita "Hahaha, siap! Kapan-kapan kalau bikin lagi sisain buatku ya. Aku naik ke kamar dulu, jangan begadang terlalu malam."
        chiasa "Iya, selamat malam, Ko-nii."
        nar "Kamu mengambil satu potong cokelat ganache lagi dari piring keramik sambil memperhatikan uap tipis yang naik dari cangkir teh hitammu."
        nar "Di luar jendela dapur, angin malam Februari terdengar berdesir pelan melewati dahan pohon halaman belakang rumah Amamiya."
        nar "Memilih untuk tidak mengikatkan perasaan pada siapa pun malam ini memberimu ruang bernapas yang sepenuhnya bebas dari ekspektasi orang lain."
        nar "Setelah cangkir tehmu kosong, kamu membilas piring dan cangkir tersebut di bak cuci dengan air hangat hingga bersih."
        nar "Sisa cokelat di atas loyang kamu simpan rapi ke dalam wadah tertutup di rak tengah kulkas untuk teman minum teh esok sore."
        nar "Kamu mematikan lampu ruang makan dan naik ke lantai dua dengan pikiran yang jernih tanpa beban."
        nar "Suasana rumah yang hening di tengah malam musim dingin memberikan ketenangan yang jarang kamu rasakan di tengah kesibukan kampus."
        nar "Tidak ada pesan mendadak yang harus kamu tunggu balasannya di layar ponsel, dan tidak ada pula janji manis yang harus kamu jaga."
        nar "Kamu menutup pintu kamarmu dengan pelan dan bersiap beristirahat menyambut hari kuliah esok pagi."
        nar "Setelah langkah Koita menjauh di tangga atas, rumah kembali senyap. Kamu menyesap teh hitammu sampai tandas sambil menghabiskan potongan cokelat di piring, membiarkan malam Valentine berlalu tenang tanpa satu pun janji atau harapan baru yang harus kamu pertanggungjawabkan esok pagi."
    return

# ┌─ PANDUAN CERITA · C10 · Rival di Yukata
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Nagisa di festival kedua.
# │ INTI    : A damai / B tantang / C goda.
# │ AKHIRAN : kebangkitan rivalitas atau kedamaian.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C10:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Rival di yukata")
    nar "Udara malam Agustus masih menyimpan hangat aspal ketika kamu melangkah keluar dari gang Rumah Amamiya menuju jalan festival yang baru menyala. Deretan lampion kertas menggantung rendah di atas kerumunan, memantulkan cahaya jingga pada rambut cokelat gelapmu yang terikat pita hitam dan motif krisan putih di yukata biru malammu."
    nar "Aroma saus yakisoba dan cumi bakar segera menyambut dari tikungan pertama. Di belakang wajan besi yang mengepul, seorang pria berikat kepala handuk membalik mi dengan spatula logam."
    "Penjual Yakisoba" "Ayo, masih panas! Yukata baru jangan sampai bau asap dulu, mampir sebentar beli minuman dingin!"
    nar "Kamu baru saja menepi dekat tiang lampion untuk membetulkan tali sandal kayumu ketika suara ketukan geta lain berhenti tepat dua langkah di depanmu. Pita hitam-pink di kedua ujung twin-tail pirang itu langsung mudah dikenali bahkan di tengah keramaian."
    nar "Nagisa berdiri memegang kipas kertas lipat dengan yukata biru pucat bermotif kembang api kecil dan obi merah muda. Matanya yang biru cerah menyapu yukatamu dari kerah hingga lipatan bawah secara cepat, lalu segera naik lagi dengan kecepatan defensif."
    nagisa "Tumben banget kerah yukatamu nggak kebalik, biasanya kamu terburu-buru keluar rumah."
    chiasa "Baru ketemu tiga detik langsung memeriksa kerah, Nagisa-senpai?"
    nagisa "Jangan salah paham, ya. Aku nggak lagi membandingkan yukata kita. Cuma kebetulan lewat dan lihat pita obimu kelihatan agak miring sedikit."
    nar "Kamu menunduk memeriksa simpul obimu sendiri yang sebenarnya rapi tanpa lipatan meleset, lalu mengangkat wajah kembali menatapnya."
    chiasa "Rapi kok, Nagisa-senpai. Justru kipas di tanganmu kayaknya digenggam kencang banget dari tadi, takut terbang kena angin?"
    nar "Nagisa mendengus kecil dan langsung mengendurkan jarinya di gagang kipas. Di dalam tubuh ini, kamu bisa membayangkan betul bagaimana Chiasa yang asli akan membalas tatapan barusan. Satu sindiran ringan tentang siapa yang paling dulu dicari Koita, lalu seluruh malam akan habis untuk menghitung siapa yang tampak lebih unggul."
    chiasa "{i}Gaya lama mereka memang selalu muter di situ. Baru ketemu dua menit di mulut jalan festival, suasananya sudah kayak mau masuk arena tanding.{/i}"
    nar "Melihatmu diam sejenak dan tidak langsung melempar balasan tajam, alis Nagisa sedikit terangkat. Ia mengetuk-ngetukkan kipas kertas ke telapak tangannya, menatapmu dengan campuran curiga dan bersiap."
    nagisa "Kok diam? Tumben banget nggak langsung nyindir soal warna yukataku atau nanya aku mau ketemu siapa malam ini."
    chiasa "Lagi mikir aja. Rasanya sayang kalau baru keluar rumah sudah capek duluan."
    nagisa "Hmph. Ya sudah, jelas-jelas aja sekalian. Kita mau mulai berdebat dari sekarang, atau menunggu sampai semua stan tutup? Aku cuma tanya supaya bisa mengatur waktu."
    nar "Dari ujung jalan utama di belakang punggung Nagisa, bunyi tabuhan taiko festival terdengar berdentum berirama mengiringi tawa anak-anak yang berlarian membawa balon air."
    nar "Cahaya lampion kertas berwarna merah dan jingga bergoyang lembut ditiup angin malam Agustus, menerangi motif kembang api kecil pada kain yukata biru pucat Nagisa."
    nar "Meskipun mulutnya langsung menantangmu menentukan jadwal berdebat, kamu melihat jemarinya sempat merapikan letak obi merah mudanya dengan sedikit gugup."
    nar "Sejak tahun pertama mereka saling mengenal di sekitar Koita, pertemuan di malam festival musim panas memang selalu menjadi ajang adu gengsi yang tak tertulis."
    nar "Nagisa sudah menyiapkan seluruh pertahanan dirinya sejak keluar dari rumah karena mengira kamu akan langsung menyerangnya dengan sindiran seperti tahun lalu."
    nar "Padahal di balik tatapan birunya yang waspada, ia tampak datang sendirian ke mulut gang ini sebelum bergabung dengan kerumunan di jalan utama."
    nar "Aroma manis apel karamel dan jagung bakar berembus melewati tempat kalian berdiri di dekat tiang lampion kayu."
    nar "Beberapa rombongan mahasiswa beryukata tampak melintas sambil bercanda riang menuju deretan stan permainan di sisi kuil."
    nar "Kamu memperhatikan ujung sandal kayu Nagisa yang mengetuk pelan permukaan aspal seolah sedang menunggu aba-aba darimu."
    nar "Malam festival tahun kedua ini bisa kamu jalani dengan mengajak gencatan senjata yang santai agar kalian berdua bisa menikmati jajanan tanpa ketegangan."
    nar "Kamu juga bisa meladeni tantangan klasiknya untuk menghidupkan kembali persaingan lama yang sudah sangat ia hafal luar kepala."
    nar "Atau kamu dapat mematahkan seluruh kuda-kuda pertahanannya sekaligus dengan satu pujian tulus yang sama sekali tidak pernah ia duga dari bibir Chiasa."
    nar "Nagisa kembali membuka kipas kertas lipatnya setengah bagian sambil mengangkat dagu menunggu jawabanmu."
    nar "Suara pengumuman panitia festival dari pengeras suara di dekat gerbang kuil terdengar menyemarakkan langit malam yang cerah."
    nar "Lampion-lampion kertas di atas kepala kalian memancarkan warna hangat yang menenangkan suasana di mulut gang itu."
    nar "Kamu mengatur posisi berdirimu di atas sandal kayu agar lebih nyaman sebelum menanggapi ucapannya."
    nar "Kamu tersenyum tipis di bawah pendar cahaya lampion sebelum memilih kalimat yang akan membuka malam festival kalian."
    call kk_family_menu("C10", ["\"Bagaimana kalau kita damai dulu malam ini, Nagisa-senpai?\"", "\"Kenapa harus menunggu stan tutup? Mulai sekarang juga boleh.\"", "\"Nagisa-senpai manis banget pakai yukata itu, sayang kalau dipakai cemberut.\""])
    if _return == "A":
        chiasa "Bagaimana kalau kita damai dulu malam ini, Nagisa-senpai? Sandal kayu ini bikin kakiku pegal kalau harus dipakai berdiri sambil adu mulut sebelum makan apa-apa."
        nar "Nagisa berkedip cepat, gagang kipas di tangannya berhenti bergerak. Ia memicingkan mata, seolah memeriksa apakah ada sindiran tersembunyi di balik wajah santaimu."
        nagisa "Damai? Tiba-tiba begini? Kamu lagi nyiapin jebakan apa, Chiasa? Jangan bilang kamu mau bikin aku lengah lalu kabur duluan ke tempat lain."
        chiasa "Serius, nggak ada rencana apa-apa. Perutku beneran lapar, dan bau takoyaki dari stan sebelah sudah bikin pusing dari tadi."
        nar "Ia menatapmu dua detik lagi, lalu mendengus pelan sambil menutup kipas kertasnya dengan bunyi ringan."
        nagisa "...Baik. Untuk malam ini, aku turunkan pedangku. Tapi cuma sampai lampion terakhir dimatikan, ya. Jangan kira aku bakal terus-terusan lunak begini."
        chiasa "Sepakat. Kalau gitu kita cari makan dulu sebelum antreannya makin panjang."
        nar "Langkah kalian di beberapa meter pertama masih terasa sedikit kaku. Kalian berhenti di depan stan takoyaki yang dijaga seorang paman ramah bercelemek biru tua. Ia menaburkan serpihan ikan kering tinggi-tinggi dengan gaya pamer sambil nyaris menjatuhkan satu bola takoyaki ke kotak uangnya sendiri."
        "Penjual Takoyaki" "Waduh, hampir jadi bonus spesial! Ini buat dua adik-kakak manis, kuahnya kupilih yang paling kental ya!"
        nagisa "Kami... ah, terima kasih, Oji-san."
        nar "Begitu kalian menepi membawa wadah kertas masing-masing, kamu melirik paman yang masih panik mengelap meja kasirnya."
        chiasa "Kalau takoyaki tadi beneran jatuh ke kotak uang, itu dihitung dapat kembalian ekstra atau disuruh ganti rugi, ya?"
        nar "Nagisa yang baru meniup tusuk giginya langsung terbahak pendek sebelum sempat menahan diri. Begitu sadar suaranya keluar lepas, ia cepat-cepat menutup mulut dengan punggung tangan sambil melotot salah tingkah."
        nagisa "Jangan ngomong aneh-aneh waktu aku lagi pegang makanan panas! ...Tadi aku nggak ketawa, ya. Cuma keselek bau saus."
        chiasa "Iya deh, keselek saus. Habis ini mau es serut rasa apa? Aku biasanya pilih lemon."
        nagisa "Melon lebih enak, lemon terlalu asam buat lidahmu nanti. Sini, di ujung sana stannya lebih sepi."
        nar "Kalian tiba di depan stan es serut kecil berhias bendera kertas biru. Penjaga stan menyerut balok es dengan cepat lalu menyiramkan sirup hijau terang dan kuning pucat ke dua gelas plastik bening."
        "Penjual Es Serut" "Silakan, satu melon satu lemon! Hati-hati ngilu kalau dimakan terlalu cepat!"
        nagisa "Lihat, sirup melon warnanya jauh lebih bagus daripada kuning pucat begitu. Coba sini, aku mau cek seberapa asam lemonnya."
        nar "Ia menyendok sedikit es serut dari gelasmu, memasukkannya ke mulut, lalu langsung mengernyitkan seluruh wajah sampai matanya menyipit rapat."
        nagisa "Asem banget! Gimana kamu bisa makan ini sambil muka datar begitu?!"
        chiasa "Sudah kubilang rasanya segar. Mau tukar satu sendok melon biar adil?"
        nagisa "Ambil aja sedikit dari pinggir, jangan habisin bagian yang banyak sirupnya!"
        chiasa "Pelit banget sih, Senpai, padahal tadi siapa yang langsung nyendok es lemonku duluan."
        nagisa "Tadi itu kan prosedur pemeriksaan rasa, bukan minta! Sudah, buruan ambil satu sendok sebelum esnya mencair jadi air gula!"
        nar "Kamu menyendok sedikit es serut hijau beraroma melon manis dari pinggir gelasnya dan mencicipi dinginnya yang langsung menyegarkan langit-langit mulut."
        nar "Kalian berdua berjalan berdampingan dengan langkah yang jauh lebih santai menyusuri deretan stan lampion menuju bangku taman di dekat pelataran kuil."
        nar "Tanpa adanya keharusan untuk saling mengalahkan, Nagisa ternyata merupakan teman jalan yang sangat seru dan penuh perhatian pada hal-hal kecil."
        nar "Ia bahkan sempat mengingatkanmu agar mengangkat sedikit ujung bawah yukata biru malammu saat melewati genangan air di dekat stan minuman dingin."
        nar "Di sepanjang jalur festival yang ramai, beberapa kenalan kampus yang berpapasan sempat menoleh heran melihat kalian berdua tertawa bersama sambil berbagi jajanan."
        nar "Biasanya setiap kali Chiasa dan Nagisa berada di satu acara yang sama, udara di sekitar mereka selalu dipenuhi adu sindiran yang membuat orang lain sungkan mendekat."
        nar "Malam ini, gencatan senjata yang kamu tawarkan di awal pertemuan telah membuka ruang pertemanan baru yang hangat di antara kalian berdua."
        nar "Nagisa menghabiskan sisa es serut melonnya dengan wajah puas sambil mengipas-ngipas pelan lehernya menggunakan kipas kertas lipat."
        nar "Angin malam bulan Agustus berembus sejuk dari arah pepohonan kuil membawa gema musik festival yang meriah."
        nar "Kalian terus melangkah melihat-lihat stan topeng dan permen kapas tanpa ada satu pun yang terburu-buru ingin mengakhiri malam."
        nar "Nagisa bahkan sempat menunjuk satu gantungan kunci berbentuk kelinci putih di stan suvenir dengan mata yang berbinar senang."
        nar "Kedamaian sederhana yang kalian bangun malam ini terasa jauh lebih menyenangkan daripada seribu perdebatan lama."
        nar "Kamu berjalan di sebelahnya sambil menikmati sisa es serut lemon yang segar di tanganmu."
        nar "Nama Koita tidak muncul satu kali pun sepanjang deretan lampion itu. Nagisa berjalan sejajar di sampingmu sambil mengomentari stan demi stan, suaranya jauh lebih ringan dibandingkan saat kalian baru berpapasan tadi."
    elif _return == "B":
        chiasa "Kenapa harus menunggu stan tutup? Mulai sekarang juga boleh, Nagisa-senpai. Sayang banget kalau sudah dandan rapi begini lalu cuma lewat begitu saja."
        nar "Dagu Nagisa langsung terangkat. Kilat kompetitif yang akrab segera menyala di matanya yang biru cerah, menyapu sisa ragu yang tadi sempat muncul."
        nagisa "Oh, begitu caramu? Bagus. Aku memang lebih suka lawan yang nggak pura-pura mengalah di depan mataku."
        chiasa "Lagipula, pita di twin-tail itu kelihatan dipasangkan sengaja biar serasi sama obinya, ya? Butuh berapa lama di depan cermin sebelum keluar rumah?"
        nagisa "H-hei! Itu cuma... cuma kebetulan warnanya cocok! Daripada kamu yang sengaja pilih yukata warna gelap supaya kelihatan lebih dewasa di depan Ko-kun!"
        chiasa "Warna gelap itu gampang nggak kelihatan kotor kalau kena saus yakisoba. Beda sama warna cerah yang kalau kecipratan dikit langsung panik."
        nagisa "Aku nggak bakal kecipratan! Sini, kalau kamu memang segitu percaya dirinya, kita buktikan di stan depan sana!"
        nar "Nagisa berbalik cepat dan menunjuk deretan kolam plastik bercahaya di stan tangkap ikan mas. Penjaga stan yang melihat semangat kalian langsung terkekeh sambil menyodorkan dua jaring kertas tipis beserta mangkuk plastik."
        "Penjual Stan" "Wah, kelihatannya serius banget nih! Dua ratus yen sekali main, yang dapat paling banyak boleh pilih kantong motif khusus!"
        nagisa "Awas saja kalau jaringmu robek duluan sebelum dapat satu ekor, Chiasa."
        chiasa "Kita lihat saja siapa yang terlalu bersemangat sampai langsung menyendok airnya."
        nar "Baru lima detik jaring masuk ke air, Nagisa mengejar ikan mas oranye terbesar di sudut kolam. Kertas tipisnya langsung robek lebar di tengah gerakan, membuat percikan kecil mengenai ujung lengan yukatanya."
        nagisa "Argh! Kertasnya tipis banget! Ini pasti curang!"
        nar "Kamu menggeser jaringmu perlahan menyusuri pinggir kolam dan mengangkat dua ikan kecil berturut-turut ke dalam mangkuk plastik, lalu melirik Nagisa dengan senyum tipis."
        chiasa "Dua lawan nol. Sudah cukup, atau mau atur waktu buat ronde kedua?"
        nagisa "Sekali lagi! Oji-san, tambah dua jaring lagi! Jangan kira kamu menang cuma karena dapat dua ekor kecil yang nggak lari!"
        nar "Kamu ikut tertawa pendek dan meletakkan koin tambahan di nampan kayu. Pada ronde kedua, Nagisa mencondongkan badan dengan wajah sangat serius, memasukkan jaringnya miring perlahan dari tepi kolam hingga berhasil mengangkat satu ikan tutul kecil."
        nagisa "Dapat! Lihat tuh, aku cuma butuh pemanasan di ronde pertama!"
        chiasa "Tetap dua lawan satu, Nagisa-senpai. Jaring keduaku belum robek juga."
        nar "Begitu jaring keduamu ikut robek saat mengejar ikan hitam kecil, Nagisa langsung berdiri menegakkan punggung dan menunjuk stan lempar gelang di seberang jalan."
        nagisa "Seri nggak dihitung selesai! Ayo ke stan lempar gelang sekarang, yang kalah traktir jagung bakar!"
        chiasa "Boleh. Siap-siap buka dompet ya."
        nagisa "Kamu tuh yang harusnya siapin uang koin buat bayarin jagung bakarku! Jangan mimpi aku bakal kalah di stan lempar gelang!"
        chiasa "Hati-hati lho, Senpai, kalau terlalu napsu melempar kayak waktu ngejar ikan mas tadi, gelangnya malah mental keluar meja semua."
        nar "Nagisa mendengus menantang sambil melangkah cepat menyeberangi jalur pejalan kaki menuju stan lempar gelang rotan yang diterangi lampu bohlam kuning."
        nar "Di depan meja sasaran yang berjajar hadiah boneka kecil dan kotak permen, kalian kembali beradu skor lemparan dengan sorot mata penuh konsentrasi."
        nar "Setiap kali gelang rotanmu berhasil mendarat tipis di dekat hadiah utama, Nagisa langsung menahan napas dan berusaha melempar lebih akurat di giliran berikutnya."
        nar "Suasana kompetitif yang menyala di antara kalian berdua membuat penjaga stan dan beberapa pengunjung di sebelah ikut menonton dengan seru."
        nar "Pada akhirnya skor kalian tetap berakhir tipis dan kalian berjalan bersama menuju stan jagung bakar sambil terus berdebat siapa yang lemparannya paling rapi."
        nar "Aroma mentega dan kecap manis yang terbakar di atas arang panas memenuhi udara malam saat kalian menunggu dua tusuk jagung matang."
        nar "Meskipun perdebatan sepanjang malam itu terdengar ramai dan hidup, pola hubungan kalian kembali terkunci pada rel persaingan lama sebagai dua rival."
        nar "Tidak ada ruang bagi percakapan yang lebih lembut karena baik kamu maupun Nagisa sama-sama sibuk menjaga gengsi agar tidak terlihat mengalah."
        nar "Nagisa menerima tusuk jagung bakarnya sambil masih melirikmu dengan dagu terangkat, siap membalas setiap komentar yang keluar dari mulutmu."
        nar "Malam festival bulan Agustus itu berlalu dengan riuh di bawah deretan lampion, menyisakan semangat tanding yang belum juga padam."
        nar "Kamu menggigit jagung bakar hangat di tanganmu sambil melayani setiap tantangan kecil yang ia lempar di sepanjang jalan."
        nar "Beberapa pengunjung di sekitar stan permainan tampak tertawa melihat semangat kalian berdua yang tidak mau kalah satu sama lain."
        nar "Rivalitas lama antara Chiasa dan Nagisa kembali berdiri utuh seperti tahun-tahun sebelumnya di tengah gemerlap malam musim panas."
        nar "Ketajaman lama di antara kalian menyala cepat, akrab dan memicu adrenalin seperti permainan yang aturannya sudah kalian hafal luar kepala. Di balik serunya tawa bersaing itu, kamu bisa merasakan jarak tipis yang kembali mengeras, seolah malam ini tetap harus berakhir dengan satu pemenang dan satu pihak yang tampak kurang."
    else:
        chiasa "Nagisa-senpai manis banget pakai yukata itu, sayang kalau dipakai cemberut. Aku nggak niat berdebat malam ini."
        nar "Nagisa membeku di tengah tarikan napas. Kipas kertas di tangannya berhenti beberapa senti dari dagunya, sementara matanya membesar menatapmu."
        nagisa "H-hei! Jangan menggodaku di tempat ramai begini! Kamu lagi sakit atau kepalamu kepentok pintu sebelum keluar?"
        chiasa "Serius. Warna biru mudanya cocok banget sama rambut dan pitamu. Dari tadi di deretan jalan ini, Nagisa-senpai yang paling kelihatan rapi."
        nar "Kamu melangkah setengah tapak lebih dekat di bawah cahaya lampion jingga, tidak menyebut nama Koita ataupun membandingkannya dengan siapa pun di keramaian itu. Wajah Nagisa memerah cepat sampai ke ujung telinganya yang beranting pita pink."
        nagisa "Kamu... kamu pasti cuma mau bikin aku lengah! Iya kan? Supaya aku lupa mau bilang apa lalu kamu bisa ketawa sendiri!"
        chiasa "Kalau aku mau bikin kamu lengah, buat apa? Aku cuma bilang yang memang kelihatan dari tadi. Memangnya nggak boleh memuji?"
        nagisa "Bukannya nggak boleh. Cuma biasanya kamu nggak pernah ngomong begitu tanpa ada embel-embel di belakangnya!"
        nar "Dua pengunjung festival yang lewat di samping kalian melirik sekilas sambil tersenyum melihat pipi Nagisa yang merah padam. Nagisa langsung membuka kipas kertasnya lebar-lebar untuk menutupi separuh wajahnya."
        nagisa "Dasar menyebalkan. Jangan berdiri terus di bawah lampu paling terang sambil masang muka polos begitu."
        chiasa "Kalau begitu kita pindah ke tempat yang agak teduh? Di dekat stan kakigori lampunya lebih lembut."
        nar "Nagisa menggerutu pelan dari balik kipas, lalu tiba-tiba menjepit ujung lengan yukatamu dengan dua jari dan menarikmu melangkah maju mendahului kerumunan."
        nagisa "Sudah, ayo jalan! Kalau berdiri terus di sini, mukaku kelihatan aneh. ...Dan jangan diulangin lagi kalimat tadi di depan stan makanan."
        chiasa "Tangannya Nagisa-senpai hangat banget ya megang lengan bajuku."
        nagisa "I-itu karena di sebelah sana ada genangan air dari kotak es! Aku cuma nggak mau sandalmu terpeleset lalu aku repot!"
        nar "Kamu melirik jalan aspal kering di depan kalian sambil menahan senyum tipis."
        chiasa "Aspalnya kering semua kok dari ujung ke ujung."
        nagisa "Chiasa! Sudah, diam dan jalan aja!"
        chiasa "Haha, iya, iya, aku diam nih. Tapi pelan-pelan dikit jalannya, Senpai, sandal kayuku nggak bisa dipakai ngebut."
        nagisa "M-makanya jangan ngomong yang bikin orang salah tingkah terus dari tadi!"
        nar "Nagisa segera memelankan langkah sandalnya agar kembali sejajar dengan ritme jalanmu tanpa melepaskan cekalan dua jarinya dari ujung lengan yukatamu."
        nar "Pujian tulus yang kamu lontarkan tanpa embel-embel persaingan tadi telah meruntuhkan seluruh tembok pertahanan yang ia siapkan sejak dari rumah."
        nar "Di bawah cahaya lampion yang agak teduh dekat deretan stan kakigori, warna merah di kedua pipi Nagisa masih tampak jelas di balik kipas kertasnya."
        nar "Ia tidak lagi menyebut soal jadwal berdebat ataupun berusaha mencari-cari celah pada lipatan obi yukatamu seperti saat pertama kali berpapasan."
        nar "Ketika kalian berhenti memesan dua mangkuk es serut di stan sudut yang tenang, Nagisa bahkan memilihkan meja kayu yang jauh dari kerumunan agar kalian bisa duduk berdua."
        nar "Setiap kali tatapan mata kalian tidak sengaja bertemu di atas meja, ia langsung buru-buru memalingkan wajah sambil menggerutu pelan untuk menutupi debarannya."
        nar "Cara barumu memperlakukannya malam ini telah mengubah posisi Chiasa di dalam pikiran Nagisa dari sekadar saingan lama menjadi seseorang yang membuat hatinya berdebar."
        nar "Angin malam festival berembus lembut menggoyangkan pita hitam-pink pada kuncir kembarnya sementara ia menyendok es serutnya dengan gerakan salah tingkah."
        nar "Kamu menikmati suasana malam Agustus yang hangat itu sambil memperhatikan betapa manisnya reaksi Nagisa saat kehilangan seluruh alasan untuk memusuhimu."
        nar "Sepanjang sisa perjalanan menyusuri jalan festival, ia terus berjalan rapat di sisimu dengan keakraban baru yang terasa begitu berbeda."
        nar "Cahaya lampion yang memantul di anting pita merah mudanya membuat rona hangat di pipinya terlihat semakin jelas."
        nar "Ia bahkan membagi separuh apel karamel yang baru dibelinya kepadamu tanpa mengomel panjang lebar seperti biasanya."
        nar "Malam festival kedua ini telah membuka lembaran baru yang jauh lebih lembut di antara kalian berdua."
        nar "Meski suaranya naik satu oktaf, jemarinya tetap tidak melepaskan ujung lengan yukatamu selama beberapa langkah panjang. Ia berjalan sedikit di depan dengan bahu tegang, berusaha menyembunyikan wajahnya yang masih hangat di balik cahaya lampion."
    return

# ┌─ PANDUAN CERITA · C12 · Orang Tua Pulang
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Daisuke dan Yoshie pulang di Natal.
# │ INTI    : A menyambut / B menghindar / C membuka rahasia.
# │ AKHIRAN : gerbang Koita Success (tahap 3).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C12:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Orang tua pulang")
    nar "Udara malam Natal bulan Desember menempel dingin di kaca jendela ruang keluarga Rumah Amamiya. Di atas meja makan sudah terbentang taplak kotak-kotak hangat, dua piring ayam panggang sederhana buatan Koita, serta sebuah pohon cemara mungil berlampu kuning yang baru kalian keluarkan dari lemari bawah tangga."
    nar "Baru saja kamu hendak mengambil gelas kaca dari rak dapur, suara deru mobil taksi melambat dan berhenti tepat di depan pagar kayu. Bunyi pintu mobil ditutup dua kali disusul roda koper berat menggilas jalan masuk langsung membuat Koita menoleh cepat dari depan kompor."
    koita "Eh? Kita nggak lagi pesan kiriman apa pun malam ini kan, Chi-chan?"
    chiasa "Nggak ada paket datang kok, Ko-nii. Jangan-jangan..."
    nar "Belum sempat kamu menyelesaikan kalimat, bel pintu berbunyi pendek diikuti suara kunci yang sangat akrab diputar dari luar. Daun pintu depan terayun lebar membawa angin dingin bulan Desember bersama dua koper kain besar dan aroma kopi bandara."
    "Daisuke" "Kami pulang! Wah, pas sekali rumah masih hangat dan bau masakan sampai ke teras depan."
    "Yoshie" "Selamat malam, Koita-kun, Chiasa-chan! Maaf ya Ibu sama Ayah sengaja tidak mengabari jam pesawatnya supaya bisa jadi kejutan Natal untuk kalian."
    koita "Ayah?! Ibu?! Beneran pulang ke rumah buat Natal tahun ini?! Tadi di pesan terakhir bilang pemotretan majalah di luar negeri baru beres akhir bulan!"
    "Daisuke" "Editornya mempercepat tenggat cetak edisi musim dingin, jadi jadwal pulang kami maju seminggu. Lagipula masa dua Natal berturut-turut kami cuma muncul lewat layar video."
    nar "Amamiya Daisuke meletakkan tas kamera kanvas tuanya di dekat rak sepatu sambil tertawa renyah. Rambutnya yang diikat pendek sedikit berantakan oleh angin malam, dan jaket kanvas tebalnya masih dingin oleh embun luar."
    nar "Di sampingnya, Amamiya Yoshie melepas mantel wol berwarna krem dengan senyum hangat yang langsung memenuhi lorong masuk yang biasanya hanya dihuni langkah kaki kalian berdua."
    chiasa "Selamat pulang, Ayah, Ibu... kaget banget, beneran nggak menyangka kalian sudah berdiri di depan pintu."
    "Yoshie" "Aduh, lihat wajah terkejutnya Chiasa-chan, manis sekali! Sini, Ibu bawa kue kering mentega sama teh bunga dari kota terakhir tempat Ayah memotret kemarin. Koita-kun, tolong bantu Ayah angkat koper yang biru ke koridor dulu ya."
    koita "Siap, Ibu! Wah, berat banget ini, isinya batu atau buku semua, Ayah?"
    "Daisuke" "Isinya lensa cadangan sama dua kardus kecil cokelat buat anak-anak di rumah. Jangan sampai jatuh ya, Koita."
    nar "Ruang masuk yang biasanya terasa lapang mendadak penuh oleh koper, kantong kertas oleh-oleh, dan tawa akrab keluarga yang belum pernah benar-benar kamu alami sendiri sebelumnya."
    nar "Yoshie segera membuka tas tangan kainnya dan mengeluarkan sehelai syal wol kotak-kotak abu-abu untuk Koita serta sebuah buku sketsa bersampul linen tipis untukmu, lalu menyerahkannya dengan mata berbinar."
    "Yoshie" "Ini buat Koita-kun supaya lehernya nggak kedinginan waktu pulang kuliah malam, dan buku sketsa kertas kapas ini Ibu beli khusus di toko buku kecil dekat alun-alun buat Chiasa-chan."
    koita "Wah, bahannya lembut banget, Ibu! Kebetulan syal lamaku ujungnya sudah mulai berbulu semua."
    chiasa "Kertasnya tebal sekali, Ibu... terima kasih banyak ya, pasti enak banget buat latihan arang sama tinta."
    nar "Di samping mereka, Daisuke sempat melirik rak sepatu lorong sambil melepas tali sepatu botnya, memperhatikan payung lipat dan sepatu kanvasmu yang tertata rapi di sudut."
    "Daisuke" "Rumahnya kelihatan rapi banget, Koita. Teman-teman seni rupa Chiasa atau anak klubnya belakangan sering mampir main ke sini nggak?"
    koita "Sesekali Yutaka sama teman kampus suka mampir sebentar kok, Ayah. Tapi memang belakangan Chi-chan sendiri rajin banget membereskan ruang tamu sebelum tidur."
    nar "Begitu mereka berpindah ke ruang tamu, Daisuke membuka ritsleting tas kameranya dan mengeluarkan sebuah kotak kaleng tipis berisi pensil arang berbungkus kertas cokelat dengan stiker toko seni asing, lalu menyodorkannya kepadamu bersama selembar foto cetak hitam-putih berukuran kartu pos."
    "Daisuke" "Ini buat kamu, Chiasa. Kemarin waktu memotret stasiun tua yang atap kacanya tertutup salju tipis, Ayah langsung ingat lukisan jendela yang dulu suka kamu bikin di kamar atas. Katanya arang merek ini lembut banget buat bikin bayangan abu-abu."
    chiasa "Wah... foto stasiunnya bagus banget, Ayah. Garis bayangan tiangnya rapi sekali. Terima kasih banyak ya buat pensil arangnya."
    nar "Kamu menerima kotak kaleng itu dengan kedua tangan dan sedikit menundukkan kepala secara sopan. Yoshie yang sedang membuka pita kotak kue kering langsung menghentikan tangannya dan menatapmu sambil tersenyum heran."
    "Yoshie" "Eh? Tumben banget Chiasa-chan menerima oleh-oleh Ayah sambil bilang terima kasih serapi itu pakai dua tangan. Biasanya kalau Ayah pulang dari luar negeri kamu langsung merampas kotak cokelat duluan sambil protes kenapa nggak dibelikan film polaroid."
    chiasa "Ah... habis kaget aja lihat kalian datang mendadak, Ibu. Belum sempat kepikiran mau protes atau minta oleh-oleh apa."
    "Yoshie" "Ibu juga lihat pita rambut hitammu masih sama seperti dulu ya, Chiasa-chan. Cuma entah kenapa pembawaanmu sekarang kelihatan jauh lebih tenang dan kalem. Padahal waktu panggilan video musim panas kemarin kamu masih sempat cemberut soal cuaca panas."
    "Daisuke" "Hahaha, wajar lah kalau anak kuliah tahun kedua mulai sedikit jaga sikap, Ibu. Eh, Koita, sup krim di dapur aman kan? Ayah lapar banget habis duduk sembilan jam di pesawat."
    koita "Bentar lagi mendidih kok, Ayah! Aku balik ke dapur dulu cek panci biar nggak gosong, sekalian kutambahin porsi ayam panggangnya buat Ayah sama Ibu!"
    "Yoshie" "Biar Ibu bantu siapkan piring besar di meja makan ya, Koita-kun. Eh, gelas keramik kesukaan Ayah masih ditaruh di rak atas sebelah kanan kan?"
    koita "Masih di situ kok, Ibu! Tapi hati-hati, kemarin aku geser sedikit ke belakang soalnya ada gelas baru dari Chi-chan."
    nar "Koita melangkah cepat kembali ke dapur sambil tertawa kecil, meninggalkan bunyi sendok sayur dan uap sup hangat dari balik sekat kayu. Yoshie ikut menyusul meletakkan bungkusan kue kering dan teh bunga di meja makan."
    nar "Di tengah ruang tamu yang diterangi lampu kuning hangat, Daisuke belum langsung melangkah ke meja. Ia menggantung jaket kanvasnya di sandaran kursi, menepuk debu perjalanan dari lengan kemeja flanelnya, lalu memutar badan menghadapmu dengan tenang."
    nar "Tidak ada sedikit pun sorot marah ataupun curiga yang tajam di matanya. Justru cara pandangnya yang terbiasa membaca rincian kecil lewat lensa kamera berhenti lama di wajahmu, memperhatikan bagaimana bahumu berdiri tegak, caramu memegangi kotak pensil arang di depan dada, serta jeda napasmu sebelum menjawab."
    nar "Mereka pulang membawa hadiah kecil dan seluruh pengetahuan bertahun-tahun tentang Amamiya Chiasa yang tidak tersimpan di buku harian, catatan ponsel, ataupun lemari mana pun yang bisa kamu pelajari sebelum membuka mulut."
    "Daisuke" "Chiasa... kemari sebentar, biar Ayah lihat baik-baik."
    chiasa "Kenapa, Ayah? Ada yang aneh sama mukaku?"
    "Daisuke" "Nggak ada yang aneh, cuma... kamu kelihatan berbeda sekali sejak terakhir kali kita duduk satu ruangan. Lebih dewasa, mungkin. Cara kamu berdiri dan menatap balik waktu bicara sekarang terasa jauh lebih tenang dari Chiasa yang dulu suka langsung mencela lelucon Ayah."
    "Yoshie" "Benar juga kata Ayah, Chiasa-chan. Tadi waktu pintu dibuka, Ibu sempat merasa kamu kelihatan sedikit menahan jarak. Kamu nggak lagi capek banget gara-gara tugas kuliah atau pameran seni bulan kemarin kan?"
    chiasa "{i}Mereka tidak menuduh apa-apa. Mereka cuma menatap anak yang mereka besarkan dari kecil dan langsung menangkap ada sesuatu yang bergeser.{/i}"
    "Daisuke" "Ayah tahu mata seorang fotografer kadang terlalu cerewet soal hal kecil. Tapi kamu baik-baik saja kan selama Ayah sama Ibu pergi, Chiasa? Cerita dong, gimana rasanya tahun keduamu di kampus?"
    nar "Lampu pohon Natal kecil memantulkan kilau tipis di mata kuning keemasanmu. Di belakang sekat dapur, Koita masih mengaduk sup sambil sesekali melirik ke arah ruang tamu. Kamu sadar detik ini adalah pilihan antara mempertahankan peran yang mereka kenal, mundur dari tatapan mereka, atau meruntuhkan seluruh topeng penyamaranmu di hadapan orang tua tubuh ini."
    call kk_family_menu("C12", ["Sambut mereka dengan hangat seperti biasa.", "Hindari tatapan mereka dengan alasan mengurus barang.", "Buka rahasia siapa dirimu sebenarnya dan apa yang berubah."])
    if _return == "A":
        nar "Kamu menelan gugup yang sempat menyempitkan tenggorokanmu, melangkah maju mendekati Daisuke, lalu menarik senyum lembut yang paling hangat yang sanggup kamu berikan malam ini."
        chiasa "Aku baik-baik saja kok, Ayah, Ibu. Mungkin karena sudah dua tahun kuliah dan sering mengurus persiapan pameran sendiri di kampus, jadi terbawa agak lebih tenang aja. Selamat pulang ya, rumah beneran terasa beda begitu kalian berdua ada."
        nar "Kamu menyentuh ringan lengan sweter Yoshie dan membantunya merapikan kotak kue kering ke atas meja makan. Bahu Yoshie yang sempat tegang langsung meluruh hangat, sementara matanya berkaca-kaca tipis di bawah lampu ruang makan."
        "Yoshie" "Anak kami benar-benar sudah besar ya, Ayah... Entah kenapa Ibu tiba-tiba ingin menangis mendengarnya."
        "Daisuke" "Haha, sudah jangan nangis sebelum supnya keluar, Ibu. Nanti Chiasa malah bingung harus menenangkan siapa duluan."
        koita "Nah, sup krim sama ayam panggangnya sudah siap! Ayo duduk semua sebelum keburu dingin!"
        nar "Koita datang membawa panci keramik hangat dan meletakkannya di tengah meja makan, lalu menoleh kepadamu dengan senyum lega yang tulus melihatmu menyambut kepulangan orang tua kalian dengan begitu hangat."
        koita "Tuh kan, Ayah, Ibu, aku nggak bohong waktu di telepon bilang Chi-chan makin rajin dan dewasa di rumah. Belakangan dia bahkan nggak sering ngomel soal cucian piring lagi."
        chiasa "Hei, kalau Ko-nii naruh piring kotor di bak sampai besok pagi lagi, tetap bakal kuomeli kok."
        "Daisuke" "Nah, kalau nada menyindir kakaknya yang barusan baru terdengar persis kayak Chiasa yang biasa."
        nar "Tawa hangat pecah di sekeliling meja makan. Yoshie segera menyendokkan porsi sup hangat ke mangkukmu sambil memperhatikan piringmu dengan penuh perhatian."
        "Yoshie" "Kamu makannya tetap teratur kan, Chiasa-chan? Tidurmu juga jangan sampai lewat jam dua malam terus gara-gara menggambar, nanti matamu gampang lelah. Dulu waktu SMP saja kalau sudah keasyikan mewarnai sampai lupa makan malam."
        chiasa "Sudah jauh lebih teratur kok, Ibu. Ko-nii juga sering ngingetin kalau aku kelamaan melek di kamar."
        "Yoshie" "Syukurlah. Ingat nggak, Koita-kun, Natal pertama waktu Ibu sama kamu pindah ke rumah ini? Kalian berdua diam-diam mencolek krim kue Natal sebelum Ayah selesai memotret, lalu pas ketahuan Chiasa langsung menunjuk hidungmu padahal ujung jarinya sendiri belepotan gula."
        koita "Hahaha, iya banget, Ibu! Waktu itu aku sampai bengong dituduh duluan, padahal krim di pipi Chi-chan jelas banget kelihatan!"
        chiasa "Aduh, jangan dibahas lagi dong waktu kecil itu... bikin malu aja."
        nar "Kamu ikut tertawa pelan menyembunyikan denyut aneh di dadamu karena tidak satu pun potongan kenangan krim kue itu benar-benar ada di kepalamu. Di seberang meja, Daisuke mengeluarkan selembar kontak cetak foto kecil dari saku kemejanya dan menggesernya ke dekat piringmu."
        "Daisuke" "Oh iya, soal proyek gambarmu... masih lancar kan? Kalau editornya mulai terlalu menekan jadwal seperti musim gugur tahun lalu, kamu boleh bilang terus terang ke Ayah. Jangan dipikul sendirian cuma karena kamu pakai nama pena."
        chiasa "{i}Ayah benar-benar tahu soal nama pena Shena... dan ia menanyakannya dengan nada biasa seorang ayah yang menjaga putrinya.{/i}"
        chiasa "Masih bisa kuatur pelan-pelan kok, Ayah. Sekarang aku lagi banyak latihan teknik dasar lagi bareng teman studio biar tanganku nggak gampang kaku. Foto komposisi jalanan yang Ayah tunjukkan ini juga bagus banget buat referensi perspektif."
        "Daisuke" "Benar? Ambil saja lembar cetaknya kalau mau ditempel di dinding kamarmu. Ingat pesan Ayah ya, gambar yang paling bagus itu selalu lahir dari garis yang masih kamu sukai sendiri alih-alih sekadar selesai paling cepat buat mengejar cetak."
        chiasa "Iya, Ayah. Aku bakal ingat itu."
        nar "Koita beranjak sebentar ke kulkas mengambil sebotol sari apel bersoda yang sudah ia dinginkan sejak sore, lalu menuangkannya ke empat gelas kaca bening di atas meja."
        koita "Mumpung kita berempat akhirnya duduk lengkap di meja makan pas malam Natal, ayo bersulang dulu dong! Selamat pulang, Ayah, Ibu! Selamat Natal!"
        "Daisuke" "Selamat Natal semuanya! Terima kasih sudah menjaga rumah dengan baik selama kami pergi!"
        "Yoshie" "Selamat Natal, anak-anak. Oh iya, Chiasa-chan, teman-teman dekatmu di kampus seperti Sakurajima-san sama Tachibana-san sehat semua kan? Kalau liburan ini mereka senggang, ajak saja mampir makan kue di rumah."
        chiasa "Iya, Ibu, mereka sehat semua kok. Nanti kalau jadwal liburan mereka cocok, aku coba ajak mampir."
        "Yoshie" "Oh iya, Yutaka-kun juga sehat kan? Besok atau lusa undang dia mampir makan di rumah ya, Koita-kun, Chiasa-chan. Ayah sama Ibu juga bawa oleh-oleh biji kopi panggang kesukaannya."
        koita "Pasti, Ibu! Besok kukabari Yutaka biar langsung mampir, pasti dia senang banget dengar Ayah sama Ibu pulang."
        nar "Sepanjang makan malam Natal itu, obrolan tentang perjalanan Daisuke, cerita terjemahan Yoshie, dan kegiatan kampus Koita mengalir tanpa jeda canggung. Koita sesekali menggeser potongan roti hangat ke piringmu sambil bertukar pandangan akrab denganmu."
        nar "Dari luar, semuanya tampak seperti foto keluarga yang paling utuh. Namun di balik setiap jawaban hangat yang berhasil kamu susun, kamu merasakan dingin yang aneh di ujung jari."
        chiasa "{i}Mereka sedang menyayangi putri mereka yang sebenarnya sudah tidak ada di kursi ini. Semakin hangat mereka menatapku, semakin berat rasanya memakai kehangatan itu sebagai tameng penyamaranku.{/i}"
        nar "Kamu menerima setiap perhatian itu dengan rasa takut yang tidak terlihat dari luar. Malam Natal berjalan penuh tawa dan lampu hangat, sementara kamu sadar menyembunyikan jati dirimu di tengah orang-orang yang begitu tulus mengenal pemilik asli tubuh ini justru akan semakin sulit mulai malam ini."
    elif _return == "B":
        nar "Kamu segera mengalihkan pandangan dari mata tajam Daisuke ke arah dua koper besar di lorong masuk, berusaha menjaga jarak aman supaya tidak ada satu pun pertanyaan pribadi sempat memanjang."
        chiasa "Ah... aku cuma agak capek aja minggu ini, Ayah, Ibu. Biar aku bantu bereskan tas oleh-oleh sama menyiapkan handuk bersih buat mandi dulu ya, pasti kalian pegal habis duduk lama di pesawat."
        nar "Kamu bergegas membungkuk mengambil dua kantong kertas oleh-oleh dari lantai dan melangkah menjauh menuju lorong dapur sebelum Daisuke sempat melangkah lebih dekat."
        "Yoshie" "Eh, Chiasa-chan, tidak usah buru-buru begitu, tasnya nanti saja dibereskan habis makan..."
        chiasa "Nggak apa-apa, Ibu, biar lorongnya nggak sempit. Aku sekalian ambilkan teh hangat di dapur."
        nar "Kamu bersembunyi di balik sekat dapur, menyibukkan kedua tanganmu menyusun cangkir dan merapikan handuk lipat sementara bunyi obrolan pelan terdengar dari ruang tamu. Saat kamu membuka lemari atas hendak mencari teko keramik biru tua milik Yoshie, tanganmu meraba rak yang salah selama beberapa detik."
        nar "Di samping kompor, Koita yang baru mematikan api langsung memperhatikan gerakan tanganmu dengan kening berkerut heran."
        koita "Chi-chan? Teko teh bunga Ibu kan dari dulu selalu disimpan di laci bawah sebelah rak bumbu, nggak pernah ditaruh di lemari atas. Terus kamu kenapa langsung lari ke dapur begitu? Ayah sama Ibu baru datang lima menit, biasanya kamu yang paling duluan duduk bongkar koper."
        chiasa "Aku lupa Ko-nii naruhnya di bawah... lagipula aku cuma pengin cepat beresin meja biar mereka bisa langsung makan. Jangan ribut, nanti kedengaran di depan."
        nar "Koita tidak langsung menjawab. Sorot matanya bertahan lama di wajahmu, memperhatikan bagaimana jemarimu mencengkeram pegangan teko terlalu erat padahal air di dalamnya sudah hangat."
        koita "...Kamu beneran nggak lagi menghindari sesuatu kan, Chi-chan? Soalnya dari tadi pas Ayah bicara, kamu sama sekali nggak berani menatap mata Ayah lebih dari sedetik. Bahkan kaleng kue mentega kesukaanmu dari Ibu tadi kamu letakkan begitu saja di meja tanpa dibuka sedikit pun."
        chiasa "Aku cuma lagi nggak lapar kue manis sebelum makan malam, Ko-nii. Sudah ah, jangan kebanyakan mikir aneh-aneh."
        nar "Koita terdiam menatapmu sambil mematikan keran air di wastafel. Kerutan tipis di antara kedua alisnya tidak menghilang sedikit pun."
        nar "Sebelum kamu sempat menepis pertanyaan Koita, langkah kaki pelan terdengar mendekat ke ambang pintu dapur. Daisuke berdiri di sana tanpa membawa kamera, kedua tangannya terselip tenang di saku celana kanvasnya."
        "Daisuke" "Koita, Ibu minta tolong cek kotak kue di meja depan sebentar, katanya pitanya agak kusut dan pisau rotinya belum keluar."
        koita "Oh... iya, Ayah. Bentar ya, Chi-chan."
        nar "Koita melangkah keluar sambil sempat menoleh sekali lagi ke belakang dengan tatapan penuh tanda tanya yang jelas belum terjawab. Begitu tinggal kamu dan Daisuke di dekat ambang dapur, sang ayah sama sekali tidak meninggikan suara ataupun memaksamu berbalik."
        "Daisuke" "Ayah nggak bakal memaksa kamu duduk di ruang tamu kalau kamu memang lagi butuh ruang sendiri, Chiasa."
        chiasa "Maaf, Ayah... aku nggak bermaksud bikin suasana kepulangan kalian jadi aneh."
        "Daisuke" "Nggak ada yang perlu diminta maaf. Ayah cuma mau tanya satu hal pelan-pelan. Ada sesuatu yang bikin kamu nggak nyaman berada di rumah ini belakangan? Atau ada masalah sama Koita dan teman-teman kampusmu?"
        chiasa "Nggak ada kok, Ayah. Ko-nii baik banget di rumah, kuliah juga jalan biasa saja."
        "Daisuke" "Begitu ya. Soalnya sejak pintu dibuka tadi, cara kamu menghindari tatapan Ayah sama Ibu kelihatan kayak orang yang takut salah bicara di rumah sendiri. Padahal dulu kalau ada yang nggak kamu suka, kamu paling cepat bicara terus terang."
        nar "Kalimat itu meluncur begitu tenang dan penuh kepedulian hingga jauh lebih sulit ditolak daripada tuduhan keras yang bisa kamu bantah. Daisuke menepuk pelan bingkai pintu kayu di sampingnya lalu tersenyum tipis."
        "Daisuke" "Kalau kamu belum mau cerita malam ini, nggak apa-apa. Makan dulu saja pelan-pelan. Tapi ingat, rumah ini tetap tempatmu pulang, kamu nggak perlu pasang tameng di depan Ayah."
        nar "Daisuke kembali melangkah ke ruang makan, membiarkanmu berdiri sendirian beberapa detik di dapur yang hangat oleh uap sup."
        chiasa "{i}Bukan cuma Ayah yang menangkap ada yang janggal... tatapan Ko-nii tadi jelas sudah menyambungkan sikap menghindarku malam ini dengan semua keanehan yang ia curigai sejak Oktober.{/i}"
        nar "Ketika kamu akhirnya membawa nampan teh ke meja makan, Yoshie segera menyambutmu dengan senyum lembut dan menyendokkan potongan ayam panggang paling hangat ke piringmu supaya suasana tetap nyaman."
        "Yoshie" "Duduk di sini, Chiasa-chan. Kalau capek, habis makan nanti langsung istirahat saja ya, biar Koita-kun sama Ayah yang membereskan piring."
        koita "Iya, biar aku aja yang cuci piring malam ini. Chi-chan kelihatannya lagi banyak pikiran banget."
        chiasa "Terima kasih, Ibu, Ko-nii."
        nar "Percakapan kembali berjalan sopan di sekitar meja Natal. Namun setiap kali kamu mengangkat sendok, kamu merasakan tatapan Koita di seberang meja memperhatikan setiap gerak kecilmu dengan kewaspadaan sunyi yang kini jauh lebih tajam daripada sebelumnya."
        nar "Saat makan malam akhirnya selesai dan kamu naik ke kamar membawa kotak pensil arang pemberian Daisuke, kamu meletakkannya perlahan di tepi meja belajar tanpa langsung membukanya."
        chiasa "{i}Malam ini aku memang berhasil menghindari pertanyaan Ayah... tapi di bawah sana, Ko-nii pasti sedang menyusun ulang semua kepingan janggal yang baru saja kutinggalkan.{/i}"
    else:
        nar "Kamu menatap wajah hangat Daisuke dan Yoshie yang sedang menunggumu menjawab, lalu menyadari bahwa satu lagi kebohongan rapi malam ini hanya akan membuat ruang di rumah ini terasa semakin mencekik."
        nar "Kamu menarik napas panjang, meletakkan kotak pensil arang dan foto stasiun bersalju itu kembali ke atas meja dengan hati-hati, lalu menatap mata Daisuke lurus tanpa sedikit pun bersembunyi."
        chiasa "Ayah... Ibu... tolong duduk sebentar di ruang tamu ya. Ada sesuatu yang sudah terlalu lama kupendam, dan aku nggak sanggup lagi pura-pura semuanya cuma karena aku makin dewasa."
        nar "Nada suaramu yang mendadak serius langsung menghentikan gerak tangan Yoshie di atas kotak kue kering. Daisuke mengernyit pelan, lalu menarik kursi untuk istrinya sebelum duduk tegak di hadapanmu."
        "Daisuke" "Bicaralah pelan-pelan, Chiasa. Ayah dengar."
        "Yoshie" "Ada masalah besar di kampus, Chiasa-chan? Atau soal proyek ilustrasimu? Kalau ada orang yang menyulitkanmu, katakan saja."
        chiasa "Ini jauh lebih besar dari soal kuliah atau gambar, Ibu. Ini tentang siapa aku sebenarnya di depan kalian sekarang."
        nar "Kamu merapatkan kedua tanganmu di atas pangkuan yang terasa dingin, lalu mulai berbicara jujur tentang hal yang tidak pernah bisa dijelaskan sebagai perubahan biasa. Kamu menceritakan keterasinganmu terhadap kenangan masa kecil di rumah ini, tanganmu yang tidak lagi mewarisi kemampuan menggambar lama milik Shena, serta kenyataan pahit bahwa kesadaran yang kini hidup di tubuh ini sudah tidak sama lagi dengan putri yang mereka besarkan sejak kecil."
        nar "Di tengah kalimatmu, bunyi langkah Koita yang hendak membawa piring sup terhenti kaku di ambang sekat dapur. Ia hanya berdiri diam di sana, memegangi lap kain dengan wajah pucat tertegun mendengar kejujuran yang melampaui segala dugaan."
        "Daisuke" "Sebentar, Chiasa... berhenti dulu satu detik. Biar Ayah tarik napas dan mencerna kalimatmu."
        nar "Daisuke menurunkan kedua tangannya ke lutut, keningnya berkerut dalam seperti seseorang yang sedang memaksa akal sehatnya menerima sesuatu yang mustahil. Tidak ada kemarahan yang meledak, hanya keterkejutan berat yang membuat seluruh ruangan sunyi."
        "Daisuke" "Kamu mengatakan... kebiasaan menggambarmu hilang, banyak ingatan lama kita tidak terasa seperti milikmu, dan selama lebih dari setahun ini kamu berusaha hidup memakai nama Chiasa di rumah ini?"
        chiasa "Iya, Ayah. Aku tahu kedengarannya mustahil dan nggak masuk akal. Aku nggak minta kalian langsung percaya malam ini juga. Aku cuma nggak sanggup lagi terus menjawab pertanyaan tentang masa kecil yang sebenarnya nggak pernah kujalani, apalagi menipu orang-orang yang benar-benar menyayangi Chiasa."
        "Daisuke" "Lalu... selama setahun lebih ini, setiap kali kamu menelepon kami atau duduk makan di meja ini, apakah semuanya cuma kamu lakukan karena takut ketahuan?"
        chiasa "Awalnya aku memang cuma takut ketahuan dan bingung harus berbuat apa, Ayah. Tapi makin lama aku tinggal di sini, melihat sendiri betapa tulusnya Ayah, Ibu, dan Ko-nii menjaga rumah ini... rasa takutku berubah jadi rasa bersalah yang makin berat setiap hari."
        nar "Kamu juga membuka perasaan rumitmu menjalani hari-hari bersama Koita di rumah ini, betapa kamu takut setiap kedekatan yang tumbuh justru berdiri di atas rahasia yang disembunyikan."
        nar "Air mata akhirnya jatuh perlahan di pipi Yoshie. Jemarinya gemetar di atas taplak meja kotak-kotak itu, dan suaranya nyaris pecah saat mengajukan pertanyaan yang paling sulit untuk dijawab."
        "Yoshie" "Aku belum tahu apa yang harus kupercaya tentang cerita yang begitu aneh ini... kepalaku masih berputar mendengarnya. Lalu... Chiasa kami yang dulu, apakah kamu tahu di mana dia sekarang?"
        chiasa "...Aku nggak tahu, Ibu. Aku juga nggak tahu kenapa aku bisa terbangun di sini, dan aku nggak mau mengarang cerita manis cuma supaya Ibu nggak menangis."
        nar "Tangisan Yoshie sempat tertahan dalam satu tarikan napas pendek. Meski demikian, tangannya tidak menarik diri dari meja; mata lembutnya tetap menatap lekat wajah anak yang selama ini ia rawat."
        "Yoshie" "Aku melihat sendiri kamu gemetar sekarang, dan aku dengar kamu akhirnya memilih berhenti berbohong. Jadi aku ingin mendengar sampai selesai. Jangan menjanjikan jawaban yang tidak kamu punya cuma supaya kami tenang."
        "Daisuke" "Ibu benar. Kalau ada bagian yang memang nggak kamu tahu atau nggak bisa kamu jelaskan, bilang saja nggak tahu. Malam ini masih panjang, kita bicara pelan-pelan tanpa ada yang buru-buru menutup pintu."
        nar "Dari ambang pintu dapur, Koita melangkah masuk dengan langkah pelan dan wajah yang masih syok tetapi penuh kesungguhan. Ia meletakkan piring supnya ke meja, lalu berdiri di samping kursi Yoshie menatapmu dengan mata hitam yang akhirnya mengerti mengapa begitu banyak hal terasa berbeda sepanjang tahun ini."
        koita "Chi-chan... jadi soal cara gambarmu yang mendadak berubah sejak tahun pertama, kebiasaan kecilmu yang kadang lupa letak barang di rumah, sampai caramu menatapku di bulan Oktober kemarin... semua itu gara-gara beban sebesar ini yang kamu simpan sendirian setiap hari?"
        chiasa "Iya, Ko-nii... maaf aku baru berani bicara sekarang. Maaf sudah bikin Ko-nii bingung sepanjang tahun ini."
        koita "Aku masih kaget banget buat langsung mencerna semuanya malam ini, Chi-chan. Tapi kalau kamu beneran menanggung rahasia kayak begini sendirian di rumah selama setahun lebih... pantas saja kadang kamu kelihatan seperti nggak pernah bisa tidur tenang."
        "Daisuke" "Duduklah, Koita. Matikan dulu kompornya biar aman. Malam ini kita tidak pura-pura semuanya baik-baik saja dulu. Kita dengar semuanya dari awal."
        nar "Yoshie bangkit pelan sebentar mengambil teko teh hangat yang baru diseduh, lalu menuangkannya ke cangkir di depanmu sebelum menyentuh punggung tanganmu yang masih dingin seperti es."
        "Yoshie" "Minum sedikit dulu ya supaya tanganmu tidak terus gemetar. Kamu tidak perlu terburu-buru menjelaskan dalam satu tarikan napas."
        chiasa "Terima kasih, Ibu... maaf malam Natal kalian jadi berantakan begini gara-gara aku."
        "Daisuke" "Jangan minta maaf karena akhirnya memilih jujur, Chiasa. Justru kalau kamu terus diam sambil menyiksa diri sendirian di rumah ini, Ayah sama Ibu baru benar-benar merasa gagal menjaga rumah."
        koita "Iya, Chi-chan. Aku butuh waktu buat mencerna semuanya, tapi setidaknya mulai malam ini kamu nggak sendirian lagi memikul rahasia itu di kamar atas."
        nar "Kamu mengangguk pelan dengan mata memanas, menggenggam cangkir teh hangat di antara kedua telapak tanganmu saat jam dinding ruang tamu berdentang pelan menandai lewatnya pukul sepuluh malam."
        nar "Udara Natal di ruang keluarga tidak lagi sehangat lima belas menit lalu, dan masa depan hubunganmu dengan keluarga Amamiya kini penuh tanda tanya yang belum punya jawaban pasti. Namun untuk pertama kalinya sejak kamu terbangun di dunia ini, kamu tidak lagi duduk di bawah atap ini sendirian di balik topeng."
    return

# ┌─ PANDUAN CERITA · C13 · Hari Bentrok: Chiasa
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : hari pengakuan.
# │ INTI    : A mengaku pada Koita / B mengaku pada heroine / C mengaku pada Yutaka / D tidak mengaku.
# │ AKHIRAN : hub besar #8.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C13:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Hari pengakuan")
    nar "Permintaan bertemu datang di antara rencana orang-orang lain menyatakan perasaan. Kau tidak dapat mengatur agar setiap jawaban melindungi semua kedekatan sekaligus."
    nar "Yang dapat dipilih adalah berhenti memakai wajah Chiasa sebagai alasan bahwa kedekatanmu pasti sudah dimengerti tanpa perlu dikatakan."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Mengaku pada Koita.", "Mengaku pada seorang heroine.", "Mengaku pada Yutaka.", "Tidak mengaku pada siapa pun."])]
    call screen kk_choice_panel(_rows, "Pilihan")
    $ kk_record_choice("C13", _return)
    if _return == "A":
        chiasa "Aku ingin kamu mendengar ini tanpa menjawab hanya sebagai kakak. Aku menyukaimu. Aku juga tahu kamu boleh merasa berbeda."
        nar "Koita menatapmu lama, kemudian mengatakan ingin menjawab setelah benar-benar memikirkan seluruh yang ada di antara kalian. Kali ini penundaan itu diberi alasan dan batas percakapan berikutnya, bukan dibiarkan menjadi nanti yang tak berujung."
    elif _return == "B":
        nar "Kau mengucapkan perasaan kepada perempuan yang selama ini dicari dalam percakapan dan alasan kecil untuk bertemu. Sesudah kalimat itu selesai, kau memberi ruang mendengar jawabannya tanpa mencoba menyelamatkan diri dengan menyebutnya gurauan."
    elif _return == "C":
        chiasa "Aku ingin mengenalmu dengan cara yang bukan cuma teman Koita. Ini bukan permintaan agar kamu menolongku melupakan siapa pun."
        yutaka "Aku dengar. Aku juga ingin membicarakan perasaanku dengan jujur. Duduk sebentar, ya. Jangan kita lewati ini sambil pura-pura buru-buru."
    else:
        nar "Kau tidak mengaku hari itu. Orang lain tetap mengambil keputusan, tak menunggu sampai dirimu siap memilih arah. Saat malam berakhir, kebebasan menunda datang bersama kemungkinan beberapa kesempatan tak akan tersedia dengan cara yang sama lagi."
    return

# ┌─ PANDUAN CERITA · C14 · Perjalanan Perpisahan
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : A menghabiskan waktu dengan Koita / B dengan Nagisa / C dengan heroine lain.
# │ AKHIRAN : mempersempit jalur.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C14:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Perjalanan perpisahan")
    nar "Rencana perjalanan perpisahan terhampar dengan terlalu banyak tempat untuk satu hari. Teman-teman mulai membagi rombongan. Kau melihat bagaimana memilih pendamping berarti memberikan waktu yang tak dapat dibagikan utuh kepada semua orang."
    call kk_family_menu("C14", ["Bersama Koita.", "Bersama Nagisa.", "Bersama heroine lain."])
    if _return == "A":
        koita "Perjalanan berdua? ...Baik. Rasanya sudah lama kita tidak bicara sungguh-sungguh."
        nar "Kalian membicarakan tujuan yang sama-sama diinginkan, bukan hanya mengulang tempat masa kecil. Di sepanjang jalan Koita bertanya tentang rencana setelah pulang, belajar mengenal seseorang yang selama ini terlalu mudah dianggap sudah diketahui."
    elif _return == "B":
        nagisa "Kau memilihku untuk perjalanan ini? ...Jangan membuatku berharap kalau kau tidak serius."
        nar "Kau menjelaskan bahwa ingin waktunya, bukan reaksinya terhadap Koita. Nagisa menerima, lalu mulai mengusulkan tempat yang disukai dengan antusiasme yang makin sulit ia samarkan."
    else:
        nar "Kau menyisihkan hari untuk perempuan lain yang telah menjadi dekat. Percakapan tentang barang bawaan perlahan berpindah ke hari-hari yang ingin dijalani setelah perjalanan, membuat kebersamaan itu terasa lebih nyata daripada satu pengecualian menjelang perpisahan."
    return

# ┌─ PANDUAN CERITA · C15 · Kembang Api dan Nagisa
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : A mengaku / B bergandeng / C menjaga jarak.
# │ AKHIRAN : jalur yuri Nagisa.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C15:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Kembang api dan Nagisa")
    nar "Nagisa berdiri di sampingmu saat keramaian mulai menghitung waktu pertunjukan terakhir. Ia berkali-kali hampir mengatakan sesuatu, lalu memandangi langit sebelum sempat memilih kata. Kali ini keheningan juga menjadi pertanyaan untukmu."
    call kk_family_menu("C15", ["Mengaku pada Nagisa.", "Bergandengan tangan tanpa kata.", "Menjaga jarak."])
    if _return == "A":
        nagisa "Kamu mengatakannya sekarang? Dasar... aku sudah menyiapkan cara pura-pura nggak menunggu."
        nar "Kau memastikan ia tidak harus menerima hanya karena momen terlihat sempurna. Nagisa menatapmu kembali."
        nagisa "Aku tahu aku boleh menolak. Aku justru sedang ingin bilang iya. Dengar sampai selesai, bodoh."
    elif _return == "B":
        nar "Kau menawarkan tangan, membiarkan Nagisa memilih mendekat. Ia menautkan jari dengan wajah merah, lalu menggenggam lebih erat saat ledakan pertama menyala."
        nagisa "Nanti kita bicara juga, ya. Aku senang begini, tapi nggak mau harus menerjemahkan semuanya dari tangan terus."
    else:
        nagisa "...Begitu. Ya sudah. Kembang apinya bagus, kan? Anggap saja aku tidak berharap apa-apa."
        nar "Jarak yang kaujaga terasa jelas meski kalian berdiri dekat. Nagisa kembali melihat langit dan membiarkan tangan di samping tubuhnya tetap kosong. Ia belum bisa mengakui kecewa tanpa mencoba menghapus harapan yang sempat terlihat."
    return

# ┌─ PANDUAN CERITA · C16 · Cover vs Skripsi
# │ LOKASI  : Kampus Kouseikan · Gedung Seni Rupa & Studio
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : A fokus kuliah / B fokus proyek / C berhenti.
# │ AKHIRAN : karier Chiasa.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C16:
    call kk_scene_enter("chiasa", "Gedung Seni Rupa & Studio · Cover vs skripsi")
    nar "Tenggat karya akademik dan proyek Miono saling menutup ruang di kalender. Kau sudah memindahkan waktu tidur dua kali tanpa menemukan jam tambahan. Nama Shena menjanjikan penghasilan; nama Chiasa tetap harus menyelesaikan kelulusannya."
    call kk_family_menu("C16", ["Fokus pada kuliah.", "Fokus pada proyek ilustrasi.", "Berhenti dari keduanya."])
    if _return == "A":
        nar "Kau memprioritaskan kuliah dan memberitahu Miono sebelum pekerjaan lain ikut terhambat. Kesempatan itu hilang, tetapi keputusan yang jelas memberi waktu mengerjakan sesuatu tanpa sekaligus takut pada dua orang yang menunggu."
    elif _return == "B":
        nar "Kau menerima proyek dan membicarakan penyesuaian akademik yang perlu dihadapi. Pekerjaan seni mendapat ruang nyata, bukan sekadar dilakukan di sisa tenaga. Kelulusan kini harus menanggung akibat waktu yang memang dipindahkan."
    else:
        nar "Kau menghentikan keduanya untuk sekarang. Kabar itu harus disampaikan kepada orang-orang yang sudah menunggu, dan kelegaan awal segera bertemu ruang kosong yang belum mempunyai rencana pengganti."
        nar "Berhenti dapat menjadi pilihan yang perlu. Ia tetap meminta tanggung jawab atas pekerjaan yang telah dijanjikan dan kehidupan yang akan dijalani sesudahnya."
    return

# ┌─ PANDUAN CERITA · C17 · Pameran Tunggal
# │ LOKASI  : Kampus Kouseikan · Gedung Seni Rupa & Studio
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : A hadir sendiri / B mengundang seseorang / C membatalkan.
# │ AKHIRAN : publik melihat siapa dekat dengan siapa.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C17:
    call kk_scene_enter("chiasa", "Gedung Seni Rupa & Studio · Pameran tunggal")
    nar "Karya-karya di ruang pamer memperlihatkan garis yang kaukenal dari latihan, kegagalan, dan keputusan sulit yang akhirnya tidak dibuang. Di dekat pintu ada daftar undangan yang belum seluruhnya dikirim."
    call kk_family_menu("C17", ["Hadir sendiri saja.", "Mengundang seseorang yang berarti.", "Membatalkan pameran."])
    if _return == "A":
        nar "Kau hadir sendiri dan menjawab pertanyaan pengunjung dengan nama yang kini harus ditanggung melalui pekerjaanmu. Ada bangga dan sepi pada saat yang sama. Tak satu pun membuat pilihan itu kurang sah."
    elif _return == "B":
        nar "Kau mengundang orang yang berarti dengan jelas, menanyakan apakah bersedia hadir tanpa harus menjadi bagian dari pertunjukan kedekatan. Saat ia datang, tatapan pengunjung tidak sepenting kenyataan bahwa ia mengenali beberapa garis yang pernah dilihat sebelum menjadi karya jadi."
    else:
        nar "Kau membatalkan pameran dan menghubungi pihak yang sudah bersiap. Karya-karya kembali dibungkus, belum mendapat kesempatan dibaca orang lain."
        nar "Ruangan kosong tidak menilaimu. Orang-orang yang waktunya berubah tetap berhak mendapat penjelasan, dan kau harus memulai dari percakapan itu sebelum menanyakan apakah suatu hari siap mencoba lagi."
    return

init 1 python:
    _hook("C06-A", lambda: kk_rel("koita","trust",4))
    _hook("C06-B", lambda: kk_flag("chiasa_arah_yuri"))
    _hook("C06-C", lambda: kk_rel("nagisa","intim",4))
    _hook("C06-D", lambda: kk_rel("koita","aff",-2))
    _hook("C07-A", lambda: (kk_rel("koita","intim",4), kk_flag("chiasa_arah_success")))
    _hook("C07-B", lambda: kk_flag("chiasa_arah_yuri"))
    _hook("C07-C", lambda: (kk_flag("chiasa_arah_yutaka"), kk_suspect("koita",3)))
    _hook("C07-D", lambda: None)
    _hook("C10-A", lambda: kk_rel("nagisa","trust",4))
    _hook("C10-B", lambda: kk_rel("nagisa","jeal",5))
    _hook("C10-C", lambda: (kk_rel("nagisa","intim",4), kk_flag("chiasa_arah_yuri")))
    _hook("C12-A", lambda: kk_rel("koita","aff",4))
    _hook("C12-B", lambda: kk_suspect("koita",8))
    _hook("C12-C", lambda: (kk_flag("chiasa_arah_success"), kk_flag("chiasa_rahasia_dibuka")))
    _hook("C13-A", lambda: kk_flag("chiasa_arah_success"))
    _hook("C13-B", lambda: kk_flag("chiasa_arah_yuri"))
    _hook("C13-C", lambda: kk_flag("chiasa_arah_yutaka"))
    _hook("C13-D", lambda: None)
    _hook("C14-A", lambda: (kk_rel("koita","intim",4), kk_flag("chiasa_arah_success")))
    _hook("C14-B", lambda: (kk_rel("nagisa","intim",4), kk_flag("chiasa_arah_yuri")))
    _hook("C14-C", lambda: kk_flag("chiasa_jalur_sempit"))
    _hook("C15-A", lambda: (kk_rel("nagisa","intim",8), kk_flag("chiasa_nagisa_diakui")))
    _hook("C15-B", lambda: (kk_rel("nagisa","intim",6), kk_flag("chiasa_arah_yuri")))
    _hook("C15-C", lambda: kk_rel("nagisa","jeal",5))
    _hook("C16-A", lambda: kk_flag("chiasa_fokus_kuliah"))
    _hook("C16-B", lambda: (kk_adj("kemampuan_gambar",10), kk_flag("chiasa_fokus_proyek")))
    _hook("C16-C", lambda: kk_flag("chiasa_berhenti_seni"))
    _hook("C17-A", lambda: kk_flag("chiasa_pameran_sendiri"))
    _hook("C17-B", lambda: kk_flag("chiasa_pameran_berdua"))
    _hook("C17-C", lambda: kk_flag("chiasa_pameran_batal"))
