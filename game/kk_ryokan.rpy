# K02 "Kamar yang Tertukar" (M02, trip onsen/ryokan). Plot armor menaruh Koita
# sekamar dengan salah satu heroine; pemain bisa menggeser pembagian kamar.
# Pilihan manipulatif (termasuk sabotase) ditulis sebagai KONSEKUENSI + risiko,
# tanpa metode/cara. Lihat [[feedback-force-route-non-operational]].

# ┌─ PANDUAN CERITA · K02 · Kamar yang Tertukar
# │ LOKASI  : Taman luar ryokan
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : ryokan; plot armor menaruh Koita sekamar dengan satu heroine (ditentukan oleh siapa yang paling siap).
# │ INTI    : A tukar kamar tanpa ketahuan / B biarkan / C masuk sebagai "gangguan" / D sabotase pembagian kamar.
# │ AKHIRAN : A–C menggeser Jealousy; D memicu kecurigaan Fujisawa/Rina bila ketahuan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K02:
    call kk_scene_enter("koita", "Taman luar ryokan · Daftar kamar")
    if kk_host == "chiasa":
        nar "Sore hari di penginapan ryokan membawa aroma kayu cedar yang hangat, bau tatami segar, dan uap belerang tipis yang melayang dari arah pemandian air panas di belakang bangunan."
        play sound "audio/sfx/bamboo.wav"
        nar "Di luar pintu kaca geser yang terbuka sebagian, taman luar ryokan tampak tenang dengan kolam koi dan pancuran bambu yang sesekali berdenting pelan. Di dalam beranda berkaca, koper dan tas menginap milik rombongan mahasiswa masih berjajar rapat di atas lantai kayu yang mengilap."
        "Pengelola Ryokan" "Permisi semuanya. Sebelum kunci kamar dibagikan, silakan periksa dulu daftar pembagian kamar di meja ini ya. Saya ambilkan baki kuncinya di dalam sebentar."
        nar "Pengelola ryokan meletakkan sebuah papan klip kayu di atas meja rendah dekat jendela, lalu menyingkap tirai kain menuju ruang resepsionis. Rombongan mahasiswa segera merapat mengerubungi meja untuk mencari nama masing-masing."
        nar "Kau sendiri berdiri dua langkah di tepi pintu kaca sambil memegangi gagang tas jinjingmu, mengamati punggung para mahasiswa dari pinggir. Sebagai adik tiri Koita yang ikut dalam perjalanan ini, tidak ada yang merasa aneh melihatmu berdiri diam di sekitar rombongan."
        nar "Namun belum sampai semenit, keriuhan kecil di depan meja mendadak mereda di satu titik. Kau melangkah sedikit menyamping hingga bisa membaca lembaran kertas di papan klip itu."
        nar "Di baris kamar lantai dua paling ujung, nama Amamiya Koita tertulis bersebelahan dengan nama salah satu mahasiswi dari rombongan—sebuah kekeliruan penempatan yang memisahkan mereka dari kelompok masing-masing."
        nar "Mahasiswi yang namanya tertera di sebelah Koita langsung terdiam kaku. Ujung telinganya memerah, kedua tangannya mencengkeram tali tasnya erat-erat, bingung harus terus menatap kertas atau membuang pandangan ke lantai kayu."
        nar "Koita mencondongkan tubuh membaca ulang baris itu. Ekspresi kaget yang muncul di wajahnya tampak begitu polos dan wajar—kecuali satu detail kecil yang langsung tertangkap oleh matamu: sebelum kalimatnya keluar, sorot matanya sempat melirik cepat ke wajah mahasiswi itu untuk memeriksa reaksinya."
        koita "Eh... namaku tertulis di kamar itu juga? Mungkin pengelolanya salah hitung kapasitas supaya semua kebagian. Aku bisa langsung tanya ke resepsionis kalau kamu keberatan."
        "Mahasiswi" "T-tidak apa-apa kok! Lagipula... cuma semalam, kan? Nanti malah merepotkan pengelolanya kalau semua kamar harus dirombak lagi dari awal."
        nar "Jawaban itu meluncur terlalu cepat—terlalu buru-buru untuk terdengar santai. Di seberang meja, dua orang lain yang ikut mendengar langsung saling bertukar pandang, dan suasana di sekitar papan daftar mendadak terasa lebih sempit."
        nar "Koita mengusap tengkuknya pelan sambil tersenyum malu—senyum hangat yang datang sepersekian detik terlalu cepat, seolah kebetulan ini sepenuhnya terjadi di luar kuasanya."
        koita "Kalau kamu benar-benar nggak keberatan, ya sudah... nanti kita bisa minta tambahan penyekat saja."
        nar "Kau menatap pemandangan itu dengan rasa muak yang familier. Ini persis seperti bab klise paling basi di dalam manga harem: kesalahan pembagian kamar di ryokan onsen, ruang tertutup mendadak, dan alasan sempurna bagi Koita untuk berkata bahwa semuanya cuma tidak sengaja."
        nar "Pengelola ryokan belum kembali membawa baki gantungan kunci kayu. Papan daftar itu masih tergeletak terbuka di atas meja rendah, belum disahkan."
    else:
        nar "Sore hari di penginapan ryokan membawa aroma kayu cedar hangat, bau anyaman tatami baru, serta uap belerang tipis yang melayang dari pemandian air panas di bagian belakang bangunan."
        nar "Di balik pintu kaca geser yang terbuka sebagian, taman luar ryokan tampak tenang dengan kolam ikan koi, bebatuan berlumut, dan pancuran bambu yang sesekali berdenting pelan. Sementara itu, di dalam beranda berkaca, koper dan tas menginap rombongan masih berjajar rapat di atas lantai kayu yang mengilap."
        "Pengelola Ryokan" "Permisi semuanya. Sebelum kunci kamar dibagikan, silakan periksa dulu daftar pembagian kamar di meja ini ya. Saya ambilkan baki kuncinya di ruang dalam sebentar."
        nar "Pengelola ryokan meletakkan sebuah papan klip kayu di atas meja rendah dekat jendela, lalu menyingkap tirai kain menuju resepsionis. Rombongan mahasiswa langsung merapat mengerubungi meja mencari nama masing-masing."
        nar "Dengan kedua tangan terselip santai di saku jaket, kau berdiri menyandar ke bingkai pintu kaca sambil mengamati punggung para mahasiswa dari jarak dua langkah. Belum sampai semenit, suara obrolan ringan di sekitar papan daftar mendadak mereda di satu titik."
        nar "Kau melangkah mendekat dan melongok melewati bahu salah satu mahasiswa hingga bisa membaca lembaran kertas itu. Di baris kamar lantai dua paling ujung, nama Amamiya Koita tertulis bersebelahan dengan nama salah satu mahasiswi dari rombongan—sebuah kekeliruan penempatan yang memisahkan keduanya dari kelompok masing-masing."
        nar "Mahasiswi yang namanya tertera di samping Koita langsung terdiam kaku. Ujung telinganya memerah, kedua tangannya mencengkeram tali tas selempangnya erat-erat, bingung harus terus menatap daftar atau membuang pandangan ke lantai."
        nar "Koita mencondongkan tubuh membaca ulang baris itu. Ekspresi kaget yang muncul di wajahnya tampak begitu polos dan wajar—namun satu detail kecil tidak luput dari matamu: sebelum kalimatnya keluar, sorot mata Koita sempat melirik cepat ke wajah gadis itu untuk memeriksa reaksinya."
        koita "Eh... namaku tertulis di kamar itu juga? Mungkin pengelolanya salah hitung kapasitas supaya semua kebagian. Aku bisa langsung tanya ke resepsionis kalau kamu keberatan."
        "Mahasiswi" "T-tidak apa-apa kok! Lagipula... cuma semalam, kan? Nanti malah merepotkan pengelolanya kalau semua kamar harus dirombak lagi dari awal."
        nar "Jawaban itu meluncur terlalu cepat untuk terdengar santai. Di sisi seberang meja, dua orang lain yang ikut mendengar langsung bertukar pandang singkat, membuat udara di sekitar papan daftar mendadak terasa lebih sempit."
        nar "Koita mengusap tengkuknya pelan sambil tersenyum malu—senyum hangat yang datang sepersekian detik terlalu cepat, seolah kebetulan ini sepenuhnya terjadi di luar kuasanya."
        koita "Kalau kamu benar-benar nggak keberatan, ya sudah... nanti kita bisa minta tambahan penyekat saja."
        nar "Kau menatap pemandangan itu dari pinggir beranda. Masalah kecil, ruang tertutup mendadak, lalu alasan sempurna bagi semua orang untuk menyebutnya sekadar ketidaksengajaan. Pengelola ryokan belum kembali membawa baki gantungan kunci kayu, dan daftar di atas meja rendah itu belum disahkan."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Tukar kamar diam-diam, tanpa ada yang tahu.", "Biarkan pembagian apa adanya.", "Sisipkan dirimu sebagai 'yang kebetulan lewat'.", "Kacaukan pembagian kamar itu dari balik layar."])]
    call screen kk_choice_panel(_rows, "Daftar pembagian kamar")
    $ kk_record_choice("K02", _return)
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau memanfaatkan jeda singkat ketika sebagian rombongan menoleh ke arah teras untuk merapikan koper dan sandal dalam ruang. Tanpa menarik perhatian siapa pun dan tanpa mengumumkan campur tanganmu, kau memastikan susunan nama pada daftar kamar itu bergeser sebelum pengelola kembali."
            nar "Beberapa saat kemudian, tirai resepsionis tersibak. Pengelola ryokan melangkah keluar membawa baki kayu berisi deretan gantungan kunci bernomor, lalu mengambil papan klip dari meja dan mulai membacakan pembagian kamar dengan suara ramah dan mantap."
            "Pengelola Ryokan" "Baik, semuanya sudah lengkap ya. Untuk kamar lantai bawah sebelah timur, Amamiya Koita-san bersama rombongan putra yang lain. Lalu untuk kamar lantai dua..."
            nar "Suara pengelola terus mengalir tanpa keraguan sedikit pun, membacakan susunan baru itu seolah memang itulah keputusan yang sejak awal tercatat."
            nar "Di dekat meja, senyum ramah Koita sempat membeku sepersekian detik. Ia mengerjap, lalu melangkah maju menerima gantungan kunci kayu dari baki pengelola."
            koita "Oh... ternyata berubah, ya? Tadi kukira namaku di baris lantai dua. Iya, baik, terima kasih banyak."
            nar "Tepat di belakangnya, terdengar helaan napas lega yang tertahan dari beberapa anggota rombongan—bertabrakan langsung dengan bahu mahasiswi yang tadi berdiri di sebelah Koita. Gadis itu menerima kunci kamar putrinya dengan gerakan kaku, raut kecewa melintas jelas sebelum ia buru-buru menunduk."
            nar "Koita tidak langsung beranjak mengambil kopernya. Ia berdiri di tepi meja beberapa detik lebih lama, menatap daftar di tangan pengelola seolah berusaha mencocokkan baris nama yang baru saja dibacakan dengan apa yang jelas-jelas ia ingat lima menit lalu."
            nar "Tatapannya kemudian menyapu pelan seisi beranda—melewati beberapa wajah yang sibuk mengangkat tas, lalu berhenti sejenak pada sosokmu yang tetap tenang menyandar di bingkai pintu kaca."
            nar "Malam itu, saat rombongan berkumpul di ruang makan, orang-orang membicarakan pembagian kamar dengan nada terlalu ringan dan ceria—seolah berusaha menutupi ketegangan singkat yang sempat lewat sore tadi. Koita ikut tertawa seperti biasa, tetapi ketika ia lewat di sampingmu sambil membawa gelas teh, sorot matanya sempat singgah sekali lagi dengan tanda tanya yang tidak ia ucapkan."
            nar "Kau hanya membalasnya dengan wajah datar dan membiarkan semua orang menyebut perubahan kamar itu sebagai nasib."
        else:
            nar "Kau memanfaatkan jeda singkat ketika sebagian rombongan menoleh ke arah teras untuk memindahkan koper dan mengambil sandal dalam ruang. Tanpa menarik perhatian siapa pun dan tanpa mengumumkan campur tanganmu, kau memastikan susunan nama pada daftar kamar itu bergeser sebelum pengelola kembali."
            nar "Beberapa saat kemudian, tirai resepsionis tersibak. Pengelola ryokan melangkah keluar membawa baki kayu berisi deretan gantungan kunci bernomor, mengambil papan klip dari meja, lalu mulai membacakan susunan kamar dengan suara ramah dan pasti seolah memang itulah catatan yang sejak awal ia pegang."
            "Pengelola Ryokan" "Baik, semuanya sudah sesuai ya. Untuk kamar putra lantai bawah sebelah timur, Amamiya Koita-san dan Kisaragi Yutaka-san bersama yang lain. Lalu untuk kamar lantai dua..."
            nar "Di dekat meja, senyum ramah Koita sempat membeku sepersekian detik. Ia mengerjap bingung, lalu melangkah maju menerima gantungan kunci kayu kamar lantai bawah dari baki pengelola."
            koita "Oh... ternyata berubah, ya? Tadi kukira namaku tertulis di baris lantai dua. Iya, baik, terima kasih banyak."
            nar "Tepat di belakangnya, terdengar helaan napas lega yang tertahan dari beberapa anggota rombongan—bertabrakan langsung dengan bahu mahasiswi yang tadi berdiri di sebelah Koita. Gadis itu menerima kunci kamar putrinya dengan gerakan kaku, raut kecewa melintas jelas di wajahnya sebelum ia buru-buru menunduk."
            nar "Koita tidak langsung beranjak mengambil kopernya. Ia berdiri di tepi meja beberapa detik lebih lama, memandangi daftar di tangan pengelola seolah berusaha mencocokkan apa yang baru dibacakan dengan susunan yang jelas-jelas ia ingat lima menit lalu."
            nar "Tatapannya kemudian menyapu pelan seisi beranda—melewati rombongan yang mulai mengangkat tas, lalu berhenti sejenak pada sosokmu yang tetap santai menyandar di bingkai pintu kaca sambil menimang kunci kamar kalian."
            yutaka "Ayo, Koita. Kopermu berat nggak? Sekamar lagi nih kita."
            koita "Eh—iya, sebentar. Aneh juga ya tadi, perasaan aku lihat namaku di lantai dua..."
            nar "Malam itu di ruang makan, orang-orang membicarakan pembagian kamar dengan nada terlalu ringan untuk menutupi ketegangan singkat sore tadi. Koita tetap mengobrol dan tertawa bersamamu seperti biasa, tetapi sesekali matanya masih menyimpan tanda tanya kecil yang tidak ia ucapkan—dan kau membiarkan mereka semua menyebutnya nasib."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kau memilih tidak menggerakkan satu jari pun ke arah meja daftar. Kedua tanganmu tetap memegangi tali tas jinjing sementara kau berdiri diam di pinggir pintu kaca, membiarkan alur yang sudah disiapkan naskah berjalan tanpa campur tanganmu."
            nar "Tidak lama kemudian, pengelola ryokan kembali membawa baki kayu berisi deretan gantungan kunci. Satu per satu nama dipanggil sesuai daftar yang tidak berubah sedikit pun."
            nar "Koita melangkah maju menerima gantungan kunci kayu untuk kamar lantai dua paling ujung. Sebelum beranjak menuju kopernya, ia menoleh sekali lagi kepada mahasiswi yang menjadi rekan sekamarnya dengan nada lembut yang penuh pertimbangan."
            koita "Kalau nanti sudah sampai atas ternyata terasa nggak nyaman, bilang saja ke aku ya. Kita masih bisa langsung turun dan tanyakan ke pengelola soal kamar cadangan."
            "Mahasiswi" "Sudah kubilang nggak apa-apa kok... lagipula nanti kita ketinggalan penjelasan soal jadwal makan malam. Ayo naik duluan."
            nar "Mahasiswi itu mengangkat tas menginapnya dengan cepat, wajahnya masih menyimpan rona merah tipis saat ia berjalan mendahului Koita menuju tangga kayu lantai dua. Koita tersenyum maklum, mengangkat kopernya, lalu menyusul di belakangnya."
            nar "Begitu punggung keduanya mulai menaiki anak tangga, suasana di beranda berkaca terasa sedikit terlalu sunyi. Beberapa mahasiswi lain yang sejak tadi berdiri di dekat rak sandal menatap arah tangga tanpa berkomentar."
            "Mahasiswi Lain" "Permisi, Bu Pengelola! Makan malamnya mulai jam enam pas atau setengah tujuh ya? Terus pemandian air panasnya buka sampai jam berapa?"
            nar "Pertanyaan itu meluncur dengan suara yang satu tingkat lebih keras dan kaku daripada yang diperlukan—cukup jelas terdengar seperti usaha memecah keheningan yang mendadak tidak enak."
            play sound "audio/sfx/bamboo.wav"
            nar "Kau menoleh kembali ke luar pintu kaca saat pancuran bambu di taman berdenting pelan. Malam ini, kedekatan yang disiapkan kebetulan itu sudah mendapat ruangnya sendiri. Apa yang akan terjadi di balik pintu geser lantai dua nanti adalah sesuatu yang tidak bisa dijawab oleh selembar daftar kamar."
        else:
            nar "Kau tetap memasukkan kedua tangan ke saku jaket dan tidak menyentuh papan daftar itu sedikit pun. Kau berdiri tenang di pinggir beranda, membiarkan alur yang sudah disiapkan kebetulan itu berjalan tanpa campur tanganmu."
            nar "Tidak lama kemudian, pengelola ryokan kembali membawa baki kayu berisi deretan gantungan kunci. Satu per satu nama dipanggil sesuai daftar yang tidak berubah sehuruf pun."
            nar "Koita melangkah maju menerima gantungan kunci kayu kamar lantai dua paling ujung. Sebelum beranjak menuju kopernya, ia menoleh sekali lagi kepada mahasiswi yang menjadi rekan sekamarnya dengan nada lembut penuh pertimbangan."
            koita "Kalau nanti sudah sampai di atas ternyata terasa nggak nyaman, bilang saja ke aku ya. Kita masih bisa langsung turun dan tanyakan ke pengelola soal kamar cadangan."
            "Mahasiswi" "Sudah kubilang nggak apa-apa kok... lagipula nanti kita ketinggalan penjelasan soal jam makan malam. Ayo naik dulu."
            nar "Mahasiswi itu mengangkat tas menginapnya cepat-cepat dengan rona merah tipis di pipi lalu melangkah mendahului menuju tangga kayu lantai dua. Koita tersenyum maklum, sempat melirikmu sekilas sambil mengangkat bahu kecil seolah berkata 'mau bagaimana lagi', lalu menyusul naik."
            nar "Begitu punggung keduanya menghilang di belokan tangga, suasana di beranda berkaca mendadak terasa sedikit terlalu sunyi. Beberapa mahasiswi lain yang berdiri di dekat rak sandal saling berpandangan tanpa bicara."
            "Mahasiswi Lain" "Permisi, Bu Pengelola! Makan malamnya mulai jam enam pas atau setengah tujuh ya? Terus pemandian air panasnya buka sampai jam berapa?"
            nar "Pertanyaan itu meluncur dengan suara yang satu tingkat lebih keras dan kaku daripada yang diperlukan—terdengar jelas seperti usaha memecah keheningan yang mendadak tidak enak."
            play sound "audio/sfx/bamboo.wav"
            nar "Kau menoleh ke taman luar saat pancuran bambu berdenting pelan. Kedekatan malam itu sudah mendapatkan panggung yang disiapkan untuknya; entah apa yang akan mereka lakukan di balik pintu geser lantai dua nanti, selembar daftar kamar jelas tidak bisa menjawabnya."
    elif _return == "C":
        if kk_host == "chiasa":
            nar "Sebelum Koita dan mahasiswi itu sempat mengunci kesepakatan canggung mereka, kau langsung melangkah maju dari tepi pintu kaca menuju meja daftar sambil menjinjing tasmu, seolah baru saja selesai memeriksa koper di beranda dan kebetulan ikut membaca papan klip."
            nar "Kau meletakkan tas jinjingmu tepat di tepi meja di samping papan daftar, mencondongkan badan sedikit di antara mereka berdua, lalu menunjuk baris kamar lantai dua dengan nada ringan namun jelas."
            chiasa "Lho, susunan kamar lantai dua masih ada yang bercampur begitu? Kebetulan tas kelompokku juga belum kebagian tempat di lantai bawah. Sekalian saja kita minta pengelola rapikan ulang sebelum kuncinya keluar, daripada nanti ada yang terpisah sendiri."
            nar "Koita mengerjap kaget melihatmu tiba-tiba masuk tepat ke tengah percakapan. Namun seperti biasa, refleks ramah dan keinginan menjaga semua orang tetap nyaman langsung mengambil alih wajahnya."
            koita "Eh, Chi-chan? Oh, iya juga sih... kalau memang ada yang belum kebagian tempat di bawah, sekalian kita atur ulang bareng-bareng saja. Jangan sampai ada yang nggak kebagian kamar yang pas."
            nar "Namun reaksi mahasiswi di sebelah Koita sama sekali tidak seramah itu. Rona malu-malu yang tadi menghiasi wajahnya langsung menyusut, berganti sorot mata yang jauh lebih waspada."
            nar "Ia menatapmu dengan cermat—mengamati posisimu yang kini berdiri persis memotong jarak antara dirinya dan Koita, lalu melirik tasmu yang sudah terlanjur mendarat di atas meja."
            "Mahasiswi" "Sebenarnya kami tadi sudah sepakat nggak mempermasalahkan kamar ini kok. Nggak perlu repot-repot merombak daftarnya segala."
            chiasa "Tidak repot juga. Pengelolanya sendiri yang tadi bilang suruh cek dulu sebelum kunci dibagikan, kan? Itu orangnya sudah keluar."
            nar "Tepat saat pengelola ryokan menyibak tirai membawa baki kunci, kau langsung mengangkat tangan menyapanya dan meminta penyesuaian kamar untuk rombongan putri agar tidak ada yang terpecah. Beberapa mahasiswi lain yang mendengar ikut merapat menyetujui."
            nar "Dalam hitungan detik, kesempatan berdua yang tadi nyaris terbentuk dengan begitu rapi langsung larut menjadi keramaian logistik yang berisik dan praktis. Koita ikut menggeser nama sambil tersenyum santai, sementara mahasiswi di sebelahnya perlahan mundur dua langkah dengan lengan terlipat di dada."
            nar "Ia tidak bisa memprotes alasanmu yang terdengar sepenuhnya wajar—tetapi tatapan dingin yang sempat ia lemparkan ke arahmu sebelum mengambil kunci kamar barunya menyisakan cemburu yang belum punya tempat untuk diucapkan."
        else:
            nar "Sebelum Koita dan mahasiswi itu selesai mengunci kesepakatan canggung mereka, kau langsung mengangkat tas menginapmu dan melangkah maju tepat ke samping meja daftar seolah sekadar mengecek pembagian kamar."
            nar "Kau menaruh tasmu di pinggir meja tepat di sebelah papan klip, lalu menepuk ringan bahu Koita sambil menunjuk baris kamar lantai dua dengan nada santai namun tak bisa diabaikan."
            yutaka "Lho, Koita, kamarmu kok malah nyasar ke lantai dua? Kebetulan barang bawaan anak-anak cowok tadi sebagian nitip di koperku sama kopermu. Sekalian saja kita rapikan ulang ke kamar bawah sebelum kuncinya keluar, biar nggak repot bolak-balik tangga malam-malam."
            nar "Koita mengerjap kaget melihatmu tiba-tiba masuk tepat ke tengah percakapan dengan alasan praktis yang sepenuhnya masuk akal. Seperti biasa, refleks ramah dan keinginan menjaga semua orang nyaman langsung mengambil alih wajahnya."
            koita "Oh, iya juga sih, Yutaka. Kalau begitu sekalian kita atur ulang bareng-bareng saja biar rapi. Jangan sampai ada yang nggak kebagian tempat yang pas."
            nar "Namun reaksi mahasiswi di sebelah Koita sama sekali tidak seramah itu. Rona malu-malu yang tadi menghiasi pipinya langsung menyusut, berganti sorot mata yang jauh lebih waspada."
            nar "Ia menatapmu dari atas ke bawah dengan lebih cermat—memperhatikan posisimu yang berdiri memotong jarak antara dirinya dan Koita, lalu melirik tas menginapmu yang sudah terlanjur mendarat di atas meja."
            "Mahasiswi" "Padahal kami tadi sudah sepakat nggak mempermasalahkan kamar ini kok. Nggak perlu sampai repot-repot menggeser daftar semuanya."
            yutaka "Nggak repot juga. Pengelolanya sendiri yang tadi minta kita cek sebelum kunci dibagikan, kan? Nah, itu orangnya sudah keluar."
            nar "Tepat saat pengelola ryokan menyibak tirai membawa baki kunci, kau langsung mengangkat tangan menyapanya dan meminta penyesuaian kamar putra-putri agar barang dan rombongan tidak terpecah. Beberapa anggota rombongan lain yang mendengar segera ikut merapat menyetujui."
            nar "Dalam hitungan detik, kesempatan berdua yang semula terasa pribadi langsung larut menjadi kesibukan logistik bersama yang bising. Koita ikut menggeser nama sambil tersenyum aman, sementara mahasiswi di sebelahnya mundur dua langkah dengan tangan terlipat di dada—menyimpan rasa kesal dan cemburu yang belum punya tempat untuk diucapkan."
    else:
        if kk_host == "chiasa":
            nar "Tanpa memperlihatkan keterlibatanmu secara terbuka, campur tanganmu dari balik layar membuat pembagian kamar yang masuk ke tangan pengelola menjadi tumpang-tindih tepat ketika baki gantungan kunci dibawa keluar."
            nar "Awalnya semua tampak berjalan biasa. Pengelola ryokan mulai menyerahkan tiga gantungan kunci pertama, lalu gerakannya tiba-tiba terhenti di baris tengah. Alisnya berkerut dalam saat membandingkan catatan di papan klip dengan nomor kunci yang tersisa di baki kayu."
            "Pengelola Ryokan" "Eh... maaf sekali, tunggu sebentar. Kenapa jumlah tamu di kamar dua ratus tiga jadi lebih satu, sementara ada dua nama yang tertulis ganda di lantai bawah dan lantai atas?"
            nar "Suara gumaman bingung langsung menyebar di seluruh beranda. Pengelola ryokan membungkuk cemas meminta maaf berkali-kali dan meminta seluruh mahasiswa mengembalikan dulu gantungan kunci kayu yang sudah terlanjur dibagikan agar bisa didata ulang dari nol."
            koita "Lho, kuncinya dikumpulkan lagi? Tadi punyaku juga sempat keluar di lantai dua..."
            nar "Koita ikut mengembalikan gantungan kunci kayunya dengan wajah bingung. Rencana kamar yang semula menyatukannya dengan mahasiswi itu otomatis bubar begitu saja di tengah keributan rombongan yang saling membandingkan ingatan."
            nar "Namun keributan itu tidak berhenti sebagai kesalahan teknis biasa. Tepat di samping meja resepsionis, Rina—sahabat dekat Moeka yang sejak tadi ikut mengecek daftar kamar—mencondongkan tubuh ke arah papan klip dengan kening berkerut tajam."
            "Rina" "Tunggu sebentar... aneh banget. Tadi waktu kubaca sebelum pengelolanya masuk ke dalam, susunannya belum sekacau ini. Namaku sendiri tadi nggak di baris ini. Ada yang mengubah daftarnya ya?"
            nar "Kalimat Rina membuat suara obrolan di sekitar meja mendadak turun beberapa tingkat. Beberapa kepala serentak menoleh ke arah papan klip, lalu saling melirik satu sama lain dengan rasa tidak nyaman."
            nar "Dari sisi rombongan, Fujisawa melangkah maju dengan langkah tenang namun tegas. Ia mengangkat satu tangan meminta semua orang berhenti berdebat, lalu berdiri di sebelah pengelola ryokan untuk membantu mencocokkan ulang daftar cadangan."
            "Fujisawa" "Semuanya tenang dulu, jangan ada yang pindah tempat sampai kita cocokkan satu-satu dengan daftar awal yang kubawa. Kalau memang ada yang berubah dalam lima menit terakhir, kita pasti kelihatan bagian mana yang bergeser."
            nar "Saat berkata demikian, sorot mata Fujisawa yang awas menyapu perlahan wajah orang-orang yang sejak tadi berdiri paling dekat dengan beranda dan meja daftar—termasuk melewati dirimu."
            nar "Tidak ada satu pun yang menyebut namamu malam itu, dan rencana kebetulan yang seharusnya menguntungkan Koita memang berhasil kau gagalkan total. Namun tatapan curiga Rina yang belum juga lepas dari papan daftar dan sikap teliti Fujisawa meninggalkan satu akibat yang tak bisa dihapus: malam ini mereka berdua tahu ada sesuatu yang tidak beres untuk diperiksa."
        else:
            nar "Tanpa menampakkan keterlibatanmu di depan umum, campur tanganmu dari balik layar membuat data pembagian kamar yang sampai ke tangan pengelola menjadi tumpang-tindih tepat saat pembagian kunci dimulai."
            nar "Awalnya semua tampak berjalan wajar. Pengelola ryokan baru saja menyerahkan tiga gantungan kunci pertama ketika gerakannya mendadak terhenti di baris tengah. Keningnya berkerut dalam membandingkan catatan di papan klip dengan nomor kunci yang tersisa di baki kayu."
            "Pengelola Ryokan" "Maaf sekali, tunggu sebentar... kenapa jumlah penghuni di kamar dua ratus tiga jadi lebih satu, sementara ada dua nama yang tertulis ganda di lantai bawah dan lantai atas?"
            nar "Gumaman bingung langsung menyebar ke seluruh beranda. Pengelola membungkuk cemas meminta maaf berkali-kali dan meminta seluruh gantungan kunci kayu yang sudah terlanjur dibagikan dikumpulkan kembali agar bisa didata ulang dari nol."
            koita "Lho, kuncinya dikumpulkan lagi? Tadi punyaku juga sempat keluar di lantai dua..."
            nar "Koita ikut menyerahkan kembali gantungan kunci kayunya dengan wajah bingung. Rencana kamar yang semula menyatukannya dengan mahasiswi itu langsung bubar begitu saja di tengah riuh rombongan yang saling membandingkan ingatan."
            nar "Namun keributan itu tidak berhenti sebagai kesalahan teknis biasa. Tepat di samping meja resepsionis, Rina mencondongkan badan membaca ulang papan klip dengan alis berkerut tajam."
            "Rina" "Tunggu sebentar... aneh banget. Tadi waktu kubaca sebelum pengelolanya masuk ke dalam, susunannya belum sekacau ini. Namaku sendiri tadi nggak di baris ini. Ada yang mengubah daftarnya ya?"
            nar "Kalimat Rina membuat suara obrolan di sekitar meja mendadak mereda beberapa tingkat. Beberapa kepala serentak menoleh ke arah papan klip, lalu saling melirik dengan rasa tidak nyaman."
            nar "Dari sisi rombongan, Fujisawa segera melangkah maju dengan langkah tenang namun tegas. Ia mengangkat satu tangan meminta semua orang berhenti berdebat, lalu berdiri di samping pengelola untuk mencocokkan ulang daftar cadangan."
            "Fujisawa" "Semuanya tenang dulu, jangan ada yang pindah tempat sampai kita cocokkan satu-satu dengan catatan awal yang kubawa. Kalau memang ada yang berubah dalam lima menit terakhir, kita pasti kelihatan bagian mana yang bergeser."
            nar "Sambil berbicara, sorot mata awas Fujisawa sempat menyapu perlahan wajah orang-orang yang sejak tadi berdiri paling dekat dengan beranda dan meja daftar—termasuk melewati dirimu."
            nar "Tidak ada yang langsung menyebut namamu malam itu, dan kebetulan yang seharusnya menguntungkan Koita memang berhasil kau gagalkan total. Namun tatapan curiga Rina yang belum juga lepas dari papan daftar dan ketelitian Fujisawa meninggalkan satu akibat nyata: malam ini ada dua orang yang tahu ada sesuatu yang tidak beres untuk diperiksa."
    return

init 1 python:
    _hook("K02-A", lambda: (kk_adj("cemburu_kamar",8), kk_koita_aware(3)))
    _hook("K02-B", lambda: None)
    _hook("K02-C", lambda: kk_adj("cemburu_kamar",6))
    _hook("K02-D", lambda: (kk_flag("kamar_disabotase"), kk_adj("rina_curiga",8), kk_suspect("fujisawa",10)))
