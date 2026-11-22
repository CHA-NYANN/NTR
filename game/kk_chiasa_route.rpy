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
    chiasa "Harum banget sampai ke tangga atas, Ko-nii. Kirain Ko-nii cuma beli lauk jadi."
    koita "Kalau malam Natal cuma makan lauk kotak dari minimarket kan sedih banget. Ibu juga tadi sore sempat kirim pesan, nanya kita berdua makan apa malam ini di rumah."
    nar "Koita menarik dua kursi kayu di meja makan, lalu berhenti sejenak saat melihatmu masih memegang ponsel di tangan."
    koita "Eh, tapi aku belum nanya dari siang tadi. Malam ini kamu nggak ada janji keluar sama Haruka atau teman-teman fakultasmu, kan? Biasanya anak tahun pertama suka bikin acara kumpul-kumpul malam Natal."
    chiasa "Anak-anak studio memang ada yang ngajak jalan ke dekat stasiun sih tadi siang."
    koita "Oh, gitu... jadi malam ini kamu mau makan di rumah, atau sudah punya rencana sendiri?"
    nar "Koita bertanya dengan nada ringan sambil memegang gagang teko teh hangat, menunggu kepastian apakah kursi di seberangnya malam ini akan terisi atau tidak."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["\"Malam ini aku di rumah aja kok, makan malam bareng Ko-nii.\"", "\"Sebenarnya aku mau ngundang teman ke rumah malam ini, nggak apa-apa kan?\"", "\"Aku mau keluar sebentar, mampir ke tempat Nagisa-senpai.\"", "\"Aku lagi pengin istirahat sendiri di kamar malam ini. Makan duluan aja.\""])]
    call screen kk_choice_panel(_rows, "Pilihan")
    $ kk_record_choice("C06", _return)
    if _return == "A":
        nar "Kamu mematikan layar ponselmu, menaruhnya di atas bufet samping rangkaian lampu hias, lalu melangkah ke meja makan."
        chiasa "Malam ini aku di rumah aja kok, makan malam bareng Ko-nii. Di luar anginnya dingin banget, malas juga kalau harus desak-desakan di stasiun."
        nar "Sudut bibir Koita langsung terangkat lega. Ia meletakkan teko teh di atas tatakan kayu, lalu kembali ke dapur untuk mengambil dua mangkuk keramik."
        koita "Syukurlah. Kalau kamu tiba-tiba pergi, aku bakal bingung ngabisin sup satu panci sama kue stroberi itu sendirian."
        chiasa "Sini mangkuknya, biar aku yang tuang supnya. Ko-nii keluarkan ayam panggangnya aja dari oven."
        koita "Oke, hati-hati panas ya gagang pancinya."
        nar "Kamu menyendok sup krim yang masih mengepul tebal ke dalam dua mangkuk, sementara Koita memakai sarung tangan kain untuk mengeluarkan loyang berisi potongan paha ayam panggang kecokelatan. Setelah semuanya tersusun di meja, kalian berdua duduk berhadapan."
        koita "Selamat makan, Chi-chan."
        chiasa "Selamat makan, Ko-nii."
        nar "Beberapa menit pertama diisi bunyi sendok yang beradu pelan dengan pinggiran mangkuk. Rasa sup krim buatan Koita gurih dan kental, dengan potongan kentang serta wortel yang empuk. Setelah menghabiskan setengah mangkuknya, Koita menarik kotak kue putih di tengah meja dan mulai melepas simpul pita merahnya."
        koita "Ngomong-ngomong, lihat kue stroberi ini aku jadi ingat waktu kita baru tahun pertama tinggal serumah dulu. Kamu ingat nggak waktu kamu masih kelas empat SD?"
        chiasa "Waktu Natal pertama kita?"
        koita "Iya. Waktu itu kamu ngotot banget nggak mau masuk kamar sampai jam dua belas malam. Katanya mau pergokin Ayah sama Ibu waktu naruh kado di dekat televisi."
        chiasa "Masa sih? Aku nggak ingat sampai segitunya."
        koita "Beneran. Kamu duduk di karpet sambil meluk bantal sofa, matamu sudah merah banget nahan ngantuk. Aku disuruh nemenin di sebelahmu, nggak boleh tidur duluan. Eh, belum juga jam sebelas, kepalamu sudah jatuh ke lututku."
        chiasa "Terus Ko-nii tinggalin aku tidur di karpet?"
        koita "Ya nggak lah. Aku gendong kamu ke kamar atas, padahal waktu itu badan kita belum beda jauh tingginya. Besok paginya aku malah dimarahin gara-gara kamu kira aku sengaja nggak bangunin pas Ayah pulang."
        nar "Koita tertawa kecil sambil memotong bolu stroberi itu menjadi empat bagian, lalu memindahkan satu potongan besar dengan buah stroberi paling merah ke piring kecil di depanmu."
        koita "Sekarang tahu-tahu kamu sudah kuliah aja. Kalau Natal tahun ini, ada yang lagi kamu pengin nggak, Chi-chan? Dari kemarin kulihat kamu sering pulang sore dari studio."
        chiasa "Nggak ada yang aneh-aneh kok, Ko-nii. Akhir-akhir ini banyak hal di kampus yang harus kupikirin, jadi malam ini bisa duduk makan sup panas di rumah tanpa dikejar apa-apa aja sudah enak banget."
        koita "Kalau ada tugas studio yang berat atau ada apa-apa di kampus, jangan dipendam sendiri lho. Makan dulu kuenya mumpung krimnya belum lumer."
        chiasa "Iya, ini dimakan kok. Potongan punya Ko-nii stroberinya jatuh miring tuh."
        koita "Biarin aja, rasanya tetap sama di perut."
        nar "Kamu menyuap potongan kue bolu yang lembut itu sambil mendengarkan Koita mengoceh soal jadwal libur toko buku dekat kampus, sementara lampu hias kecil di atas bufet terus berpendar tenang sampai piring kalian bersih."
    elif _return == "B":
        nar "Kamu melirik jam dinding ruang tengah yang baru melewati pukul tujuh malam, lalu menatap Koita."
        chiasa "Sebenarnya aku baru aja janjian mau ngundang teman dari kampus ke rumah malam ini, Ko-nii. Nggak apa-apa kan kalau kami pakai ruang tengah sama meja rendah di sana?"
        nar "Koita yang baru saja mengangkat sendok sayur dari panci menghentikan gerakannya. Ia menoleh dengan alis sedikit terangkat."
        koita "Ngundang teman ke rumah? Malam Natal begini?"
        chiasa "Iya. Dia lagi nggak pulang ke rumah orang tuanya malam ini, jadi kuajak mampir makan kue sama minum teh hangat sebentar di sini."
        koita "Tumben banget, Chi-chan. Biasanya kalau malam hari raya begini kamu paling malas kalau ada tamu datang ke rumah. Siapa, anak Fakultas Seni juga?"
        chiasa "Kenalan dekat dari kampus kok. Ko-nii nggak keberatan kan?"
        koita "Nggak keberatan sih, rumah ini kan rumahmu juga. Cuma aku agak kaget aja."
        nar "Koita melirik panci sup krim dan loyang ayam panggang di atas kompor, lalu mengambil satu nampan kayu besar dari rak samping."
        koita "Kalau gitu, biar kalian leluasa ngobrolnya, aku ambil porsiku ke nampan terus makan di kamar atas aja ya. Sup sisanya kubiarin di panci, nanti kalau temanmu sudah datang tinggal dipanasin sebentar. Kuenya juga belum kubuka kok."
        chiasa "Makasih ya, Ko-nii. Maaf malah bikin Ko-nii ngungsi ke kamar."
        koita "Santai aja, aku juga lagi mau lanjut baca novel yang kemarin belum tamat. Kalau butuh cangkir teh buat tamu, ambil yang warna putih di lemari kedua ya."
        nar "Tidak lama setelah langkah kaki Koita menghilang di tangga lantai dua, bel pintu depan berbunyi. Kamu bergegas ke lorong depan dan membuka pintu. Udara malam yang dingin berembus masuk bersama sosok gadis yang kamu undang, yang berdiri di teras sambil merapatkan syal di lehernya."
        chiasa "Masuk, masuk. Di luar dingin banget ya anginnya?"
        nar "Ia melepas sepatunya di genkan sambil menggosok kedua telapak tangannya yang kemerahan karena udara malam, lalu mengikutimu masuk ke ruang tengah."
        chiasa "Duduk di karpet dekat pemanas itu aja, aku sudah nyalain dari tadi. Tunggu sebentar ya, aku ambilkan sup krim hangat sama teh dari dapur."
        nar "Kamu kembali dari dapur membawa nampan berisi dua mangkuk sup krim panas, dua cangkir teh, serta kotak kue stroberi yang baru dibuka. Saat kalian duduk berdampingan di meja rendah ruang tengah, uap sup yang hangat segera mengusir sisa hawa dingin dari luar."
        chiasa "Rumah lagi sepi soalnya orang tua lagi kerja di luar kota, terus Ko-nii sudah di kamarnya di lantai atas. Jadi santai aja, anggap kayak di kamar kos sendiri."
        nar "Tamu di sebelahmu tersenyum lega melihat suasana rumah yang tenang, lalu mulai menyendok supnya sambil bercerita soal jalanan depan stasiun yang penuh lampu Natal. Kalian mengobrol ringan dari soal makanan, kebiasaan liburan waktu sekolah, sampai rencana tahun baru nanti tanpa sedikit pun gangguan dari lantai atas."
    elif _return == "C":
        nar "Kamu berjalan ke gantungan pakaian di dekat lorong masuk, mengambil mantel tebal dan syal rajutmu, lalu kembali ke ruang makan untuk mengambil kotak biskuit cokelat yang masih tersegel di sudut meja."
        chiasa "Maaf ya, Ko-nii. Aku mau keluar sebentar malam ini, mau mampir ke rumah Nagisa-senpai."
        nar "Koita yang baru saja menaruh dua mangkuk sup di atas meja langsung menatapmu heran."
        koita "Ke rumah Nagisa-chan? Sekarang? Memangnya Nagisa-chan ngadain acara di rumahnya malam ini?"
        chiasa "Nggak ada acara apa-apa sih. Tadi aku dengar orang tuanya sama Kak Haruto lagi keluar makan malam, jadi dia sendirian di rumah. Makanya aku mau mampir bawain camilan sebentar."
        koita "Tumben banget kamu kepikiran nyamperin Nagisa-chan sendirian malam Natal begini, Chi-chan. Biasanya kalau ketemu aja kalian suka debat dulu."
        chiasa "Sesekali kan nggak apa-apa. Ko-nii makan malam duluan aja ya, supnya nggak usah nungguin aku dingin."
        koita "Oh... ya sudah, hati-hati di jalan ya. Pakai sarung tanganmu, di luar anginnya kencang."
        nar "Kamu melangkah keluar menembus jalanan perumahan yang dingin. Lampu-lampu teras tetangga memantul di atas aspal kering sepanjang tiga blok menuju kediaman keluarga Sakurajima. Begitu sampai di depan pagar kayunya, kamu menekan tombol bel di samping pintu."
        nar "Beberapa detik kemudian, kunci pintu dibuka dari dalam. Nagisa muncul mengenakan kaus lengan panjang yang dilapisi kardigan rajut tebal, dengan rambut pirang kembarnya yang digerai longgar di bahu. Begitu melihat siapa yang berdiri di teras, matanya langsung melebar."
        nagisa "Chiasa?! Kamu ngapain berdiri di depan pintu rumahku malam-malam begini?"
        nar "Nagisa refleks menjulurkan kepalanya sedikit melewati bahumu untuk melihat ke arah pagar jalanan yang kosong, lalu kembali menatapmu dengan kening berkerut."
        nagisa "...Tunggu. Kamu beneran datang sendirian? Nggak bareng Ko-kun?"
        chiasa "Sendirian lah, Nagisa-senpai. Memangnya kalau aku jalan ke rumah Senpai harus selalu dikawal Ko-nii? Ini aku bawa biskuit cokelat hangat, aku nggak disuruh masuk nih?"
        nagisa "Y-ya masuk aja! Siapa juga yang nyuruh kamu berdiri terus di luar, nanti kalau kamu flu malah aku yang disalahin!"
        nar "Nagisa bergeser membuka pintu lebih lebar. Setelah kamu melepas sepatu di genkan, ia mengajakmu naik ke kamarnya di lantai dua karena ruang tamu di bawah terlalu besar untuk duduk berdua."
        nar "Begitu pintu kamar dibuka, Nagisa buru-buru melangkah mendahuluimu, memindahkan tumpukan gulungan kertas kalkir dan kotak pensil warna dari atas kursi serta karpet ke pinggir lemari."
        nagisa "Maaf agak berantakan, tadi sore aku baru beresin sketsa tugas studio. Duduk di dekat meja situ aja, pemanasnya baru kunyalain."
        chiasa "Kamar Senpai hangat kok. Orang rumah lagi pada keluar semua ya?"
        nagisa "Iya, Ayah sama Ibu makan malam di tempat teman lama mereka, Kak Haruto masih lembur acara kantornya. Makanya tadi pas bel bunyi aku kaget. Kukira kurir paket salah alamat."
        nar "Ia duduk di tepi karpet dekat meja bundar sambil memeluk bantal kecil, masih menatapmu dengan tatapan setengah curiga dan setengah salah tingkah."
        nagisa "Jujur deh, Chiasa. Tumben banget kamu ke sini malam Natal nggak pakai acara nyindir atau pamer lagi di rumah berdua. Ada apaan sih?"
        chiasa "Nggak ada apa-apa, Nagisa-senpai. Tadi di rumah aku mikir Senpai pasti lagi sendirian, terus aku juga lagi pengin ngobrol sama Senpai tanpa bahas Ko-nii atau urusan tugas. Emang aneh ya?"
        nar "Ujung telinga Nagisa langsung memerah di sela rambut pirangnya. Ia memalingkan wajah sedikit ke arah lemari buku sambil berdeham."
        nagisa "...Nggak aneh sih. Cuma nggak biasa aja dengar kamu ngomong lurus begitu. Tunggu sebentar di sini, jangan buka biskuitnya duluan, aku turun bikin cokelat panas dua cangkir ke dapur!"
        chiasa "Jangan lama-lama ya, Senpai!"
        nar "Tidak sampai lima menit, Nagisa kembali naik membawa nampan berisi dua cangkir cokelat panas yang mengepul. Kalian membuka kotak biskuit itu bersama di atas meja bundar, mengobrolkan tontonan televisi akhir tahun dan kehebohan kampus sampai jarum jam melewati tengah malam."
    else:
        nar "Kamu menggeleng pelan sambil tetap berdiri di dekat anak tangga, tidak melangkah mendekati kursi makan yang sudah ditarik Koita."
        chiasa "Maaf ya, Ko-nii. Malam ini aku lagi pengin istirahat sendiri aja di kamar. Ko-nii makan duluan aja, nggak usah nungguin aku."
        nar "Tangan Koita yang masih memegangi sandaran kursi kayu perlahan turun. Senyum di wajahnya surut ketika ia melihat dua mangkuk sup krim yang sudah terlanjur mengepul di atas meja."
        koita "Lho, kok gitu, Chi-chan? Kamu nggak enak badan? Atau tadi di kampus ada yang bikin kesal?"
        chiasa "Nggak sakit kok, cuma rasanya agak capek aja pengin diam di kamar malam ini."
        koita "Tapi ini kan malam Natal, Chi-chan. Masa kamu nggak makan malam sama sekali? Kalau kamu malas duduk di bawah, biar kuambilin nampan terus kubawain sup sama ayamnya ke kamarmu di atas ya?"
        chiasa "Beneran nggak usah, Ko-nii. Perutku belum lapar. Aku cuma mau seduh susu hangat satu muk terus langsung tidur."
        nar "Koita terdiam beberapa detik di samping meja makan. Ia melirik kotak kue stroberi yang masih terikat pita merah di tengah meja, lalu menghela napas pendek."
        koita "...Akhir-akhir ini kadang aku ngerasa kamu kayak sengaja ambil jarak di rumah, Chi-chan. Kalau aku ada salah ngomong atau bikin kamu nggak nyaman, bilang aja lho."
        chiasa "Nggak ada yang salah kok, Ko-nii. Aku cuma lagi butuh waktu sendiri aja. Selamat malam ya."
        koita "...Iya. Kalau nanti tengah malam kamu bangun terus lapar, supnya masih di panci dan kuenya kusimpan di rak tengah kulkas ya. Tinggal ambil aja."
        nar "Kamu mengambil satu muk susu hangat dari dapur, lalu berjalan menaiki tangga kayu dan menutup pintu kamarmu di lantai dua, meninggalkan Koita duduk seorang diri di ruang makan bawah yang terlalu sunyi."
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
    nar "Kamu melepas celemek lalu duduk di kursi sambil memandangi kotak cokelat yang sudah tertata rapi di hadapanmu. Belum ada satu nama pun yang kamu tulis di atas kartu kertas itu. Selama berbulan-bulan tinggal di dunia ini, kamu sudah menyaksikan berkali-kali betapa mudahnya satu hadiah kecil berubah menjadi harapan yang rumit kalau maksud di baliknya sengaja dibiarkan samar."
    nar "Dari lantai atas terdengar samar bunyi pintu kamar dibuka lalu langkah kaki Koita melintas menuju kamar mandi sebelum kembali masuk. Tubuh Amamiya Chiasa memang menyimpan kebiasaan lama untuk selalu menyiapkan cokelat setiap pertengahan Februari, tetapi malam ini kamu sendiri yang menentukan ke tangan siapa kotak di meja ini akan sampai."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Tulis nama Koita dan berikan kotak cokelat ini padanya.", "Tulis pesan untuk perempuan yang kamu sukai dan temui dia.", "Bawa kotak cokelat ini untuk diberikan kepada Yutaka.", "Biarkan tanpa nama dan simpan untuk dimakan sendiri saja."])]
    call screen kk_choice_panel(_rows, "Pilihan")
    $ kk_record_choice("C07", _return)
    if _return == "A":
        nar "Kamu menarik satu lembar kartu krem kosong, mengambil pena tinta hitam, lalu menuliskan beberapa baris kalimat pendek dengan tulisan yang rapi tanpa embel-embel candaan. Setelah menyelipkan kartu itu di dalam tutup kotak dan mengikat pita cokelat tuanya hingga kencang, kamu mengangkat kotak itu dan berjalan menuju ruang tengah."
        nar "Tidak lama kemudian, langkah kaki Koita terdengar menuruni tangga kayu sambil membawa gelas kosong untuk diisi air di dapur. Begitu melihatmu berdiri di dekat meja makan dengan kotak cokelat berpita rapi di kedua tangan, langkahnya melambat."
        koita "Lho, Chi-chan belum tidur? Wah, pantesan bau cokelatnya sampai ke tangga atas dari tadi. Kamu bikin sendiri itu?"
        chiasa "Iya, baru aja beres didinginin sama dibungkus. Nih, buat Ko-nii."
        nar "Kamu melangkah maju dan menyodorkan kotak karton krem itu langsung ke hadapannya. Koita menatap kotak tersebut dengan mata agak melebar sebelum menerimanya dengan kedua tangan."
        koita "Buat aku? Makasih banyak, Chi-chan! Wah, seperti biasa adikku memang paling rajin kalau sudah tanggal empat belas—"
        nar "Kalimat santai Koita terhenti sendiri di tengah jalan. Ia melihat raut wajahmu yang tenang dan tidak melontarkan godaan jahil seperti biasanya, lalu pandangannya turun ke pita satin yang diikat terlalu teliti dan ujung kartu kertas yang menyembul rapi dari balik tutup kotak."
        koita "...Sebentar, Chi-chan. Kenapa kamu lihatin aku serius banget begitu?"
        chiasa "Soalnya aku nggak mau Ko-nii asal nerima sambil mikir ini cuma cokelat kewajiban tahunan dari adik ke kakak. Di dalamnya ada kartu yang kutulis sendiri. Aku mau Ko-nii baca baik-baik."
        nar "Koita terdiam cukup lama di depan meja makan. Jarinya yang memegangi sisi kotak tampak sedikit menegang. Ia sempat melirik ke arah gelas kosong di meja dapur, seolah naluri lamanya baru saja mencari alasan ringan untuk mengalihkan suasana, lalu mengurungkannya."
        koita "Jujur aja, barusan aku hampir otomatis bilang makasih buat cokelat adiknya, Chi-chan. Kalau aku ngomong gitu, semuanya langsung beres dan nggak ada yang perlu repot dipikirin."
        chiasa "Terus kenapa nggak jadi ngomong begitu?"
        koita "Karena aku lihat matamu sekarang. Kamu nggak lagi bercanda, kan? Aku mau tahu maksudmu yang sebenarnya, jangan sampai aku sok memutuskan sendiri artinya sebelum benar-benar mendengar dari kamu."
        chiasa "Aku nggak minta Ko-nii kasih jawaban malam ini juga kok. Cuma mulai hari ini, aku nggak mau Ko-nii pura-pura nggak dengar setiap kali aku ngomong serius."
        nar "Koita mengangguk pelan. Alih-alih menaruh kotak cokelatmu di atas bufet ruang tengah bersama camilan rumah lainnya, ia membawanya terpisah dengan kedua tangan menuju anak tangga."
        koita "Biar kubawa ke kamar dan kubaca kartunya pelan-pelan di atas ya, Chi-chan. Makasih banyak buat cokelatnya. Selamat malam."
        chiasa "Selamat malam, Ko-nii."
        nar "Ia menaiki tangga dengan langkah yang lebih pelan dari biasanya. Belum ada jawaban pasti malam ini, tetapi untuk pertama kalinya ia tidak lari dari pertanyaan yang kamu letakkan di depannya."
    elif _return == "B":
        nar "Kamu menarik satu lembar kartu ucapan kosong dan menggenggam pena tinta hitam cukup lama sebelum mulai menulis. Kamu tidak menuliskan kalimat basa-basi yang bisa disalahpahami sebagai sekadar tukar-menukar camilan Valentine antar mahasiswi. Kamu menuliskan dengan kalimat pendek dan jujur bahwa kamu memang sengaja membuatnya khusus untuknya."
        nar "Setelah mengikat pita krem di sekeliling kotak dan memasukkannya ke dalam kantong kertas kecil, kamu mengambil ponsel lalu mengirim pesan kepadanya, menanyakan apakah ia masih terjaga dan bersedia bertemu sebentar di dekat kedai minuman hangat dekat stasiun. Kurang dari lima menit kemudian, balasannya masuk mengiyakan."
        nar "Kamu mengenakan mantel dan syal rajut, menyelinap keluar rumah menembus udara malam Februari yang dingin, lalu berjalan cepat menyusuri trotoar yang mulai sepi. Di bawah lampu jalan depan kedai yang hangat, sosok perempuan yang kamu tunggu sudah berdiri sambil menggosok kedua telapak tangannya."
        chiasa "Maaf ya ngajak keluar malam-malam pas anginnya lagi dingin banget begini."
        nar "Ia menggeleng dengan senyum lembut dan menjawab bahwa ia memang belum tidur, lalu melirik kantong kertas yang sejak tadi kamu dekap di depan mantelmu."
        chiasa "Ini... kebetulan tadi aku bikin cokelat sendiri di rumah. Aku pengin kasih langsung ke kamu malam ini."
        nar "Kamu mengeluarkan kotak berpita krem itu dan menyerahkannya dengan kedua tangan. Ia menerimanya sambil tertawa kecil, awalnya mengira kamu hanya sedang membagi kelebihan cokelat buatan rumah seperti yang biasa dilakukan teman-teman kuliah."
        chiasa "Di balik pitanya ada kartu kecil. Nggak usah langsung dijawab sekarang kok, aku cuma mau kamu baca sendiri nanti."
        nar "Ia sempat tertegun melihat nada bicaramu yang tidak sedang bercanda. Dengan hati-hati ia menarik kartu kecil di balik pita, membacanya di bawah cahaya kuning lampu kedai, dan senyum sopan di wajahnya perlahan berhenti. Pipinya sedikit merona saat ia kembali mengangkat pandangannya ke arahmu."
        chiasa "Aku tahu kedengarannya agak mendadak, dan kamu sama sekali nggak wajib membalas apa-apa malam ini. Aku cuma nggak mau kasih hadiah manis terus membiarkan kamu nebak-nebak sendiri maksudku apa."
        nar "Ia menunduk menatap kartu di tangannya selama beberapa detik sebelum memasukkannya kembali ke dalam kotak dengan sangat hati-hati, lalu menyimpannya ke dalam tas selempangnya."
        nar "Dengan suara yang lebih pelan dari sebelumnya, ia mengucapkan terima kasih karena kamu mau mengatakannya dengan jelas, lalu mengajakmu berjalan bersama sebentar ke arah persimpangan sebelum kalian berpisah pulang ke rumah masing-masing."
    elif _return == "C":
        nar "Kamu menarik kartu ucapan berwarna gading, menuliskan nama Yutaka-kun di bagian atas diikuti dua baris kalimat pendek yang jujur dan tidak bertele-tele, lalu menyelipkannya rapi di bawah simpul pita cokelat tua. Selesai memasukkan kotak itu ke kantong kertas kecil, kamu mengirim pesan ke Yutaka menanyakan apakah ia ada di apartemen malam ini."
        nar "Belum sampai dua menit, ponselmu bergetar oleh balasan singkatnya yang mengatakan ia baru selesai mandi dan sedang di ruang tamu, bertanya balik ada urusan penting apa malam-malam. Kamu menjawab akan mampir sebentar ke depan lobi apartemennya dalam lima belas menit."
        nar "Kamu mengenakan mantel tebal dan baru saja hendak memasang sepatu di lorong depan ketika pintu tangga lantai dua berderit. Koita melongok dari atas pegangan tangga dengan rambut agak berantakan."
        koita "Eh, Chi-chan? Sudah malam begini mau ke mana pakai mantel tebal segala?"
        chiasa "Mau keluar sebentar aja, Ko-nii. Mau mampir ke tempat Yutaka-kun buat kasih cokelat Valentine."
        nar "Koita terdiam di anak tangga atas. Pandangannya turun ke kantong kertas kecil berpita di tanganmu, lalu kembali ke wajahmu dengan senyum yang terasa sedikit melambat."
        koita "Oh... buat Yutaka? Tumben banget kamu sampai nyamperin langsung ke apartemennya malam-malam. Biasanya kan tinggal kasih besok di kampus."
        chiasa "Mumpung cokelatnya baru matang aja kok, Ko-nii. Aku pergi sebentar ya, nggak lama."
        koita "...Iya, hati-hati di jalan ya. Kalau pulang kemalaman kabari aku."
        nar "Kamu melangkah keluar menembus angin dingin Februari menuju Distrik Elite. Tepat saat kamu tiba di halaman depan gedung apartemen yang berpenerangan hangat, pintu kaca lobi didorong terbuka dan Yutaka keluar mengenakan jaket navy di atas kaus rumahan dengan ekspresi setengah penasaran."
        yutaka "Seriusan kamu jalan kaki ke sini malam-malam, Chiasa? Anginnya dingin banget lho. Ada urusan mendadak soal Koita?"
        chiasa "Nggak ada urusan soal Ko-nii kok, Yutaka-kun. Aku ke sini memang buat ketemu Yutaka-kun."
        nar "Kamu mengangkat kantong kertas kecil itu lalu mengeluarkan kotak cokelat berpita cokelat tua dan menyodorkannya ke depan dadanya."
        chiasa "Selamat hari Valentine, Yutaka-kun. Ini kubikin sendiri tadi di rumah."
        nar "Yutaka mengerjap, raut jahil yang tadinya siap melontarkan ledekan langsung lenyap. Ia meraih kotak itu dengan kedua tangannya, memegangnya hati-hati seolah benda itu jauh lebih berat daripada sekotak cokelat biasa."
        yutaka "...Buat aku? Beneran buat aku, Chiasa? Boleh kubuka sekarang kartunya?"
        chiasa "Buka aja sekarang nggak apa-apa."
        nar "Di bawah lampu lobi yang terang, Yutaka menarik kartu gading dari selipan pita tanpa menertawakan kegugupanmu sedikit pun. Kamu memperhatikan mata abu-abu gelapnya menyusuri dua baris tulisan tanganmu. Senyum santai khas teman masa kecil yang biasa ia kenakan perlahan berubah menjadi tatapan yang jauh lebih serius."
        yutaka "...Chiasa. Kamu sadar kan kalau nulis kalimat kayak gini di kartu Valentine, aku nggak bakal bisa anggap ini cuma cokelat kewajiban dari adiknya Koita?"
        chiasa "Iya, aku sadar kok. Makanya aku nulisnya jelas begitu dan nganterin sendiri malam ini."
        nar "Yutaka mengembuskan napas pelan sambil tersenyum tipis, kali ini tanpa sedikit pun nada bercanda di suaranya. Ia memasukkan kotak itu hati-hati ke saku bagian dalam jaketnya."
        yutaka "Tunggu sebentar di sini ya, jangan langsung pulang jalan kaki sendirian. Aku ambil kunci sama dompet dulu di dalam, habis itu kita beli minuman hangat di kedai pojok jalan sekalian kuantar kamu sampai depan rumah."
        chiasa "Nggak merepotkan, Yutaka-kun?"
        yutaka "Sama sekali nggak. Tunggu dua menit."
        nar "Yutaka berbalik masuk ke lobi dengan langkah cepat, meninggalkan angin malam yang entah mengapa terasa jauh lebih ringan saat kamu menunggunya di depan pintu kaca."
    else:
        nar "Kamu memandangi deretan kartu ucapan yang masih kosong itu cukup lama, lalu meletakkan kembali pena tinta hitam ke samping kotak. Tidak ada satu nama pun yang terasa perlu kamu tulis malam ini."
        nar "Kamu melepas gulungan pita satin dan menyingkirkannya ke laci meja, membuka kembali penutup kotak, lalu berjalan ke dapur untuk menyeduh secangkir teh hitam hangat. Sisa potongan cokelat ganache yang dingin di atas kertas minyak kamu pindahkan ke piring keramik kecil, mengambil garpu kue, lalu duduk santai di ruang makan."
        nar "Rasa cokelat hitam yang sedikit pahit berpadu dengan parutan kulit jeruk terasa seimbang di lidah. Tak lama kemudian, Koita turun dari lantai dua mengenakan kaus longgar untuk mengambil air minum di kulkas. Ia melirik piring cokelat di depanmu sambil menaikkan alis."
        koita "Lho, Chi-chan? Bikin cokelat banyak begitu, nggak dibungkus buat dikasih ke teman-teman fakultas besok?"
        chiasa "Nggak ah, Ko-nii. Tadi cuma lagi pengin nyoba resep baru aja buat dimakan sendiri sambil nonton televisi."
        koita "Hahaha, dasar. Boleh minta cicip satu potongan pinggirannya nggak? Kelihatannya enak banget tuh."
        chiasa "Ambil aja yang di ujung loyang situ, bentuknya agak miring."
        koita "Wah, lumayan pas manisnya, nggak bikin enek! Kapan-kapan bikin lagi ya, Chi-chan. Aku naik ke kamar dulu, jangan begadang."
        chiasa "Iya, selamat malam, Ko-nii."
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
    nar "Nagisa memeriksa yukatamu dengan pandangan cepat, lalu berkata tak sedang membandingkan. Kau mengenali cara lama Chiasa akan membalasnya: satu sindiran yang membuat seluruh malam kembali tentang siapa lebih dipilih."
    nagisa "Kita mau mulai berdebat dari sekarang, atau menunggu sampai semua stan tutup? Aku cuma tanya supaya bisa mengatur waktu."
    call kk_family_menu("C10", ["Tawarkan damai.", "Tantang balik rivalitasnya.", "Goda ia alih-alih bertengkar."])
    if _return == "A":
        nagisa "Damai? ...Baik. Untuk malam ini, aku turunkan pedangku."
        nar "Kalian menukar komentar tentang makanan alih-alih Koita. Pada mulanya terasa kaku, kemudian sebuah lelucon tentang penjaga stan membuat Nagisa tertawa sebelum sempat memikirkan apakah itu berarti kalah."
    elif _return == "B":
        nagisa "Begitu caramu? Bagus. Aku lebih suka lawan yang tidak mengalah."
        nar "Kalian kembali memakai ketajaman yang sudah hafal tempat melukai. Kegembiraan bersaing membuat jarak lama terasa akrab, meski keakraban itu semakin sulit dipisahkan dari kebutuhan membuat yang lain tampak kurang."
    else:
        nagisa "He—! Jangan menggodaku di tempat ramai begini. ...Dasar."
        nar "Godaanmu kali ini menyebutnya cantik tanpa membandingkan dengan siapa pun. Nagisa mencari balasan tajam, tak menemukannya cukup cepat, lalu mengajak berjalan agar tidak harus terus berdiri dengan wajah merah."
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
    nar "Koper Daisuke dan Yoshie memenuhi pintu masuk. Mereka membawa hadiah kecil dan pengetahuan tentang Chiasa yang tidak tersimpan dalam benda mana pun yang bisa kauperiksa sebelum menjawab."
    "Daisuke" "Chiasa. Kau tampak... berbeda. Lebih dewasa, mungkin. Kemari, biar kulihat baik-baik."
    call kk_family_menu("C12", ["Sambut mereka dengan hangat.", "Hindari tatapan mereka.", "Buka rahasia siapa dirimu sebenarnya."])
    if _return == "A":
        "Yoshie" "Anak kami sudah besar. ...Entah kenapa aku ingin menangis."
        nar "Kau menerima kehangatan dengan takut yang tidak terlihat dari luar. Daisuke menanyakan kabar gambar, Yoshie menanyakan tidur. Perhatian yang diberikan kepada seseorang yang mereka kenal terasa semakin sulit dipakai hanya sebagai perlindungan penyamaranmu."
    elif _return == "B":
        nar "Kau mengambil jarak dan menawarkan mengurus barang agar tak perlu menjawab terlalu lama. Daisuke memberi ruang, lalu bertanya dengan pelan apakah ada sesuatu yang membuatmu tidak nyaman berada di rumah."
        nar "Kecurigaannya datang melalui kepedulian, lebih sulit ditolak daripada tuduhan yang dapat dibantah."
    else:
        nar "Kau menceritakan siapa dirimu dan apa yang tidak bisa dijelaskan sebagai perubahan biasa. Daisuke meminta kau berhenti sejenak agar ia dapat memahami, sementara Yoshie tetap menatap wajah anak yang dikenalnya."
        "Yoshie" "Aku belum tahu apa yang harus kupercaya. Tapi aku ingin mendengar sampai selesai. Jangan menjanjikan jawaban yang tidak kamu punya hanya supaya kami tenang."
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
    nar "Tenggat karya akademik dan proyek Mio saling menutup ruang di kalender. Kau sudah memindahkan waktu tidur dua kali tanpa menemukan jam tambahan. Nama Shena menjanjikan penghasilan; nama Chiasa tetap harus menyelesaikan kelulusannya."
    call kk_family_menu("C16", ["Fokus pada kuliah.", "Fokus pada proyek ilustrasi.", "Berhenti dari keduanya."])
    if _return == "A":
        nar "Kau memprioritaskan kuliah dan memberitahu Mio sebelum pekerjaan lain ikut terhambat. Kesempatan itu hilang, tetapi keputusan yang jelas memberi waktu mengerjakan sesuatu tanpa sekaligus takut pada dua orang yang menunggu."
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
