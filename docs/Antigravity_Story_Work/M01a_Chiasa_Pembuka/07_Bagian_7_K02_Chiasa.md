# Bagian 7 — `K02` (*Kamar yang Tertukar*) · Host Chiasa

Target File: `game/kk_ryokan.rpy` (`label kkscene_K02`, blok `if kk_host == "chiasa":`)

```renpy
label kkscene_K02:
    call kk_scene_enter("koita", "Taman luar ryokan · Daftar kamar")
    if kk_host == "chiasa":
        nar "Sore hari di penginapan ryokan membawa aroma kayu cedar yang hangat, bau tatami segar, dan uap belerang tipis yang melayang dari arah pemandian air panas di belakang bangunan."
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
        ...
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
            nar "Kau menoleh kembali ke luar pintu kaca saat pancuran bambu di taman berdenting pelan. Malam ini, kedekatan yang disiapkan kebetulan itu sudah mendapat ruangnya sendiri. Apa yang akan terjadi di balik pintu geser lantai dua nanti adalah sesuatu yang tidak bisa dijawab oleh selembar daftar kamar."
    elif _return == "C":
        if kk_host == "chiasa":
            nar "Sebelum Koita dan mahasiswi itu sempat mengunci kesepakatan canggung mereka, kau langsung melangkah maju dari tepi pintu kaca menuju meja daftar sambil menjinjing tasmu, seolah baru saja selesai memeriksa koper di beranda dan kebetulan ikut membaca papan klip."
            nar "Kau meletakkan tas jinjingmu tepat di tepi meja di samping papan daftar, mencondongkan badan sedikit di antara mereka berdua, lalu menunjuk baris kamar lantai dua dengan nada ringan namun jelas."
            chiasa "Lho, susunan kamar lantai dua masih ada yang bercampur begitu? Kebetulan tas kelompokku juga belum kebagian tempat di lantai bawah. Sekalian saja kita minta pengelola rapikan ulang sebelum kuncinya keluar, daripada nanti ada yang terpisah sendiri."
            nar "Koita mengerjap kaget melihatmu tiba-tiba masuk tepat ke tengah percakapan. Namun seperti biasa, refleks ramah dan keinginan menjaga semua orang tetap nyaman langsung mengambil alih wajahnya."
            koita "Eh, Chiasa? Oh, iya juga sih... kalau memang ada yang belum kebagian tempat di bawah, sekalian kita atur ulang bareng-bareng saja. Jangan sampai ada yang nggak kebagian kamar yang pas."
            nar "Namun reaksi mahasiswi di sebelah Koita sama sekali tidak seramah itu. Rona malu-malu yang tadi menghiasi wajahnya langsung menyusut, berganti sorot mata yang jauh lebih waspada."
            nar "Ia menatapmu dengan cermat—mengamati posisimu yang kini berdiri persis memotong jarak antara dirinya dan Koita, lalu melirik tasmu yang sudah terlanjur mendarat di atas meja."
            "Mahasiswi" "Sebenarnya kami tadi sudah sepakat nggak mempermasalahkan kamar ini kok. Nggak perlu repot-repot merombak daftarnya segala."
            chiasa "Tidak repot juga. Pengelolanya sendiri yang tadi bilang suruh cek dulu sebelum kunci dibagikan, kan? Itu orangnya sudah keluar."
            nar "Tepat saat pengelola ryokan menyibak tirai membawa baki kunci, kau langsung mengangkat tangan menyapanya dan meminta penyesuaian kamar untuk rombongan putri agar tidak ada yang terpecah. Beberapa mahasiswi lain yang mendengar ikut merapat menyetujui."
            nar "Dalam hitungan detik, kesempatan berdua yang tadi nyaris terbentuk dengan begitu rapi langsung larut menjadi keramaian logistik yang berisik dan praktis. Koita ikut menggeser nama sambil tersenyum santai, sementara mahasiswi di sebelahnya perlahan mundur dua langkah dengan lengan terlipat di dada."
            nar "Ia tidak bisa memprotes alasanmu yang terdengar sepenuhnya wajar—tetapi tatapan dingin yang sempat ia lemparkan ke arahmu sebelum mengambil kunci kamar barunya menyisakan cemburu yang belum punya tempat untuk diucapkan."
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
```
