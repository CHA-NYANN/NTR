# Milestone host Yutaka (Y03, Y04, Y06, Y07, Y08, Y11, Y12, Y14, Y15, Y16, Y18):
# hidup pemain-sebagai-Yutaka menjaga penyamaran dan menavigasi arah (BL / heroine
# / Chiasa-NPC). Fire saat MASUK lokasi sebagai host Yutaka (trigger "host").
# Pilihan rute = pointer-flag non-eksplisit; manuver = konsekuensi. Mengikuti
# Event_Yutaka; melengkapi Y01/Y02/Y05/Y09/Y10/Y13/Y17. Daichi pakai nama-penutur.

# ┌─ PANDUAN CERITA · Y03 · Yuu-kun?
# │ LOKASI  : Distrik Elite · Apartemen Yutaka
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Nagisa memanggil dengan julukan masa kecil.
# │ INTI    : A jawab natural / B salah panggil / C pura-pura lupa.
# │ AKHIRAN : curiga_nagisa naik/turun.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y03:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Julukan lama")
    nar "Sore hari di apartemen mewah milik keluarga Kisaragi itu biasanya terlalu sunyi, tetapi kehadiran Sakurajima Nagisa yang mampir seusai kelas langsung membuat ruang tamu terasa jauh lebih hidup."
    nar "Kau baru saja keluar dari dapur membawa dua gelas teh dingin ketika melihat gadis bertubuh mungil berambut pirang keemasan twin-tail itu berdiri di dekat rak televisi. Alih-alih langsung duduk di sofa, perhatiannya tertahan pada bingkai foto lama empat sekawan di festival musim panas yang terpajang di sana."
    nar "Untuk beberapa detik, raut galak dan kompetitif yang biasa ia pasang di kampus menghilang sepenuhnya. Ia memandangi foto masa kecil itu dengan senyum tipis yang lembut—lalu, seolah terseret kenangan lama tanpa sadar, ia menoleh ke arahmu begitu mendengar bunyi gelas diletakkan di atas meja kaca."
    nagisa "Yuu-kun! ...Eh—"
    nar "Begitu julukan masa kecil itu keceplosan meluncur dari bibirnya, Nagisa sendiri langsung tersentak. Rona merah tipis naik ke ujung telinganya; ia buru-buru berdeham kecil sambil menyentuh bingkai foto di rak dengan jari telunjuknya, lalu tertawa canggung."
    nagisa "...Aneh banget, ya, sekarang keceplosan memanggil begitu lagi. Padahal waktu SD dulu, setiap kali aku teriak 'Yuu-kun!' dari ujung gang, kau selalu yang paling pertama menoleh sebelum Koita sempat sadar. Kau masih ingat kan waktu kita hampir ketinggalan kembang api gara-gara nungguin Chiasa beli permen apel?"
    nar "Mata biru cerah Nagisa menoleh lurus menatapmu, menunggu sahutan. Di dalam kepala, kau tahu persis bahwa tidak ada satu pun ingatan masa kecil Yutaka yang ikut diwariskan kepadamu—yang kaumiliki hanyalah foto di rak itu dan serpihan informasi umum dari manga."
    call kk_family_menu("Y03", ["\"Mana mungkin lupa, kau kan selalu paling heboh.\"", "\"Ingat dong, waktu kau tersesat di dekat stan ikan mas itu, kan?\"", "\"Wah, jujur saja bagian itu sudah agak kabur di kepalaku.\""])
    if _return == "A":
        nar "Kau tidak membiarkan raut wajahmu membeku sedetik pun. Kau bersandar santai di pinggir sofa sambil menyilangkan tangan, lalu menarik sudut bibirmu menjadi senyum tipis yang terasa paling cocok dengan pembawaan santai pemilik tubuh ini."
        yutaka "Mana mungkin lupa. Kalau aku nggak langsung menoleh waktu kau teriak dulu, nanti kau bakal makin keras teriaknya sampai satu gang keluar semua. Lagipula kalau nggak salah, waktu itu kau sendiri yang paling heboh berebut tempat duduk di dekat tangga kuil, kan?"
        nar "Kau sengaja memilih detail yang paling sesuai dengan sifat keras kepala Nagisa—cukup masuk akal tanpa harus menebak hal spesifik yang berisiko meleset."
        nar "Nagisa mengerjap sesaat, lalu tawa ringan yang tulus langsung pecah dari bibirnya. Wajahnya tampak jauh lebih rileks."
        nagisa "Hei, itu kan supaya kita semua dapat pemandangan kembang api paling jelas! ...Masih ingat rupanya."
        nar "Ia menunduk kembali memandangi bingkai foto di tangannya dengan tatapan hangat, lalu meletakkannya kembali dengan rapi di atas rak televisi."
        nagisa "Jujur saja, aku sendiri juga tidak ingat semuanya dengan tepat. Yang paling kuingat cuma rasanya dulu—kita selalu merasa besok masih bisa main bareng lagi tanpa perlu mikir macam-macam."
        nar "Ia berjalan menghampiri sofa, mengambil salah satu gelas teh dingin dari meja kaca, lalu menatapmu sebentar dengan sorot mata yang tenang."
        nagisa "...Baguslah kalau sekarang pun kau masih mau menoleh, Yutaka."
        nar "Di matanya, tidak ada sedikit pun keraguan tersisa. Kau mengangguk pelan sambil meneguk tehmu, menyadari betapa mudahnya satu jawaban tepat menenangkan kecurigaan sahabat masa kecilnya."
    elif _return == "B":
        nar "Merasa harus membuktikan bahwa kau benar-benar mengingat masa kecil mereka agar tidak dicurigai, kau nekat merangkai satu detail berdasarkan foto festival di rak televisi."
        yutaka "Tentu saja ingat. Waktu itu kan gara-gara kau sempat tersesat di dekat stan ikan mas sampai Koita harus meminjamkan sandalnya dan kita semua baru ketemu lagi di depan gerbang taman kota, kan?"
        nar "Nagisa sempat mengeluarkan tawa pendek karena mengira kau sedang sengaja mengarang lelucon untuk menggodanya."
        nagisa "Haha, apaan sih, ngawur banget—tunggu dulu... kau nggak lagi bercanda ya?"
        nar "Tawa Nagisa langsung terhenti di tenggorokan begitu ia melihat raut wajahmu yang tetap serius menunggu ia mengiyakan. Alisnya perlahan berkerut dalam."
        nagisa "Yutaka... yang waktu itu tersesat di festival memang aku, tapi yang menemukan dan menenangkanku kan Chiasa—dan itu di dekat kuil sebelah timur, bukan di gerbang taman kota. Mana pernah juga Koita meminjamkan sandalnya."
        nar "Suara Nagisa melambat dan turun, nada santainya lenyap sepenuhnya. Ia meletakkan kembali bingkai foto itu ke rak televisi dengan gerakan kaku, lalu menoleh menatapmu lebih lama seolah berusaha memahami bagaimana sahabat sejak TK-nya bisa meleset sejauh itu."
        yutaka "Ah... maaf. Kayaknya kepalaku mencampuradukkan dua festival yang berbeda."
        nagisa "...Mungkin. Tapi biasanya kau paling hafal hal-hal begini, bahkan hal yang aku sendiri sudah lupa."
        nar "Ia duduk di ujung sofa dan mulai menceritakan ulang kejadian sebenarnya dengan nada pelan. Kau hanya bisa mengangguk mengikuti alurnya sambil menyadari satu kenyataan pahit: masa lalu mereka yang bertahun-tahun tidak bisa dipelajari atau ditebak seperti soal ujian."
    else:
        nar "Daripada nekat mengarang detail masa lalu dan berakhir salah sebut, kau memilih bersandar santai di sofa, mengangkat bahu ringan, lalu tersenyum tipis mengejek diri sendiri."
        yutaka "Wah, jujur saja, bagian yang itu sudah agak kabur di kepalaku. Sudah bertahun-tahun lalu juga kan, Nagisa—akhir-akhir ini kepalaku keburu penuh sama materi Ekonomi."
        nar "Nagisa langsung memutar badannya menghadapmu dengan mata biru membulat dan bibir mengerucut tidak percaya."
        nagisa "Hah?! Lupa?! Serius kau bisa lupa?! Padahal biasanya kau yang paling berisik mengungkit kejadian waktu SD cuma buat ngeledek aku kalau kita lagi kumpul!"
        nar "Ia menatapmu beberapa detik dengan sorot curiga tipis yang bercampur kesal, lalu menghela napas panjang dan menjatuhkan diri duduk di sofa sambil memeluk salah satu bantal."
        nagisa "...Ya sudah, kalau memang lupa nanti kuceritakan lagi pelan-pelan. Tapi dengar ya, Yutaka—jangan pernah cuma mengangguk-angguk pura-pura paham kalau sebenarnya kau nggak ingat. Aku bisa benar-benar kesal kalau sahabat sendiri cuma iyain aku tanpa benar-benar dengar."
        yutaka "Iya, maaf. Ceritakan saja lagi nanti."
        nar "Nagisa mendengus kecil lalu meraih gelas teh dinginnya. Meski ia akhirnya kembali mengobrol tentang jadwal kuliah Arsitekturnya, sesekali matanya masih melirik ke arahmu dari balik gelas dengan kerutan samar di kening—merasa ada sesuatu pada sikapmu hari ini yang tidak sepenuhnya sama."
    return

# ┌─ PANDUAN CERITA · Y04 · Kuliah Ekonomi: Ingatan yang Hilang
# │ LOKASI  : Distrik Elite · Apartemen Yutaka
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : kuis dadakan.
# │ INTI    : A belajar semalaman / B menyontek / C jujur ke dosen / D minta bantuan Daichi.
# │ AKHIRAN : IPK; B berisiko skorsing akademik ().
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y04:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Kuis dadakan")
    nar "Malam turun sunyi di apartemen Kisaragi yang luas. Hanya cahaya lampu meja belajar yang menyala, menyoroti tumpukan buku teks tebal dan map binder rapi yang terhampar di atas meja kayu gelap di hadapanmu."
    nar "Siang tadi, dosen mata kuliah inti mengumumkan kuis dadakan untuk besok pagi—menutup rangkaian kuliah beberapa minggu terakhir yang sebagian besar hanya lewat di telingamu seperti bahasa asing."
    nar "Kau membalik halaman demi halaman catatan lama milik Kisaragi Yutaka. Tulisannya bersih, terstruktur, dan penuh singkatan istilah serta kurva perhitungan yang tampaknya sudah lebih dari cukup untuk pemilik tubuh ini. Namun bagimu, setiap halaman yang kaubuka justru melahirkan tiga pertanyaan baru yang tidak tahu harus dijawab dari mana."
    nar "Kau menyandarkan punggung ke kursi, mengusap wajah pelan sambil menatap kartu mahasiswa di sudut meja. Punya kartu mahasiswa, apartemen mewah, dan nama belakang yang dikenal dosen sama sekali tidak berarti kau mewarisi dua tahun ilmu yang pernah ia pelajari."
    nar "Jam dinding sudah melewati pukul sembilan malam. Besok pagi lembar kuis akan tetap diletakkan di depan mejamu, peduli setan siapa sebenarnya yang sedang duduk di balik tubuh ini."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Belajar semalaman mengejar ketertinggalan.", "Menyontek saat kuis.", "Jujur ke dosen soal kesulitanmu.", "Minta bantuan Daichi."])]
    call screen kk_choice_panel(_rows, "Pilihan")
    $ kk_record_choice("Y04", _return)
    if _return == "A":
        nar "Kau menarik napas panjang, beranjak ke dapur untuk menyeduh segelas kopi hitam pekat, lalu kembali duduk dan membuka buku pengantar dari bab paling dasar."
        nar "Malam itu berjalan lambat ditemani goresan pensil, halaman buku yang dibalik bolak-balik, dan rumus-rumus yang harus kaubongkar ulang satu per satu tanpa jalan pintas. Beberapa konsep akhirnya mulai masuk akal menjelang pukul dua pagi; beberapa halaman lainnya tetap keras kepala membingungkan tidak peduli berapa kali kaubaca ulang."
        nar "Ketika cahaya pucat fajar mulai menyelinap di sela tirai jendela apartemen, matamu terasa perih dan bahumu kaku. Namun saat kau mengemasi tas dan melangkah keluar menuju kampus, kau membawa pengetahuan yang terbatas—tetapi sepenuhnya milikmu sendiri."
        nar "Nilai yang keluar nanti akan mengukur kerja kerasmu malam ini, bukan reputasi orang lain yang namanya tercetak di atas lembar jawaban."
    elif _return == "B":
        nar "Melihat tumpukan bab yang mustahil kaukuasai dalam satu malam, kau mengambil jalan pintas. Kau menuliskan ringkasan rumus-rumus kunci dengan huruf sangat kecil di secarik kertas lipat yang kauselipkan di saku kemeja sebelum berangkat ke kelas."
        nar "Saat kuis dimulai di ruang kuliah yang sunyi, jantungmu berdetak keras setiap kali kertas kecil itu kauintip cepat di bawah tepi meja. Kelegaan singkat ketika baris demi baris jawaban akhirnya terisi mendadak berubah menjadi dingin yang menusuk tengkuk saat langkah sepatu pengawas berhenti tepat di samping mejamu selama beberapa detik yang terasa seperti selamanya."
        nar "Ia memang tidak langsung menegurmu di tempat dan hanya melanjutkan langkah ke barisan belakang—tetapi tatapan sekilasnya sebelum beranjak sudah cukup membuat tanganmu nyaris kaku sampai bel waktu selesai berbunyi."
        nar "Saat lembar jawaban akhirnya dikumpulkan, kau sadar yang tergeletak di tumpukan depan bukan lagi sekadar materi yang tidak kaumengerti: ada pelanggaran nyata yang sewaktu-waktu bisa menuntut pertanggungjawabanmu, dan kekayaan keluarga Kisaragi tidak akan menghapusnya."
    elif _return == "C":
        nar "Alih-alih nekat menebak membabi buta atau mengambil risiko curang, keesokan paginya kau datang lebih awal dan menemui dosen mata kuliah tersebut langsung di ruangannya sebelum kuis dimulai."
        yutaka "Permisi, Pak. Saya ingin bicara jujur sebelum kuis hari ini—ada beberapa bagian dasar dari materi beberapa minggu terakhir yang benar-benar tertinggal dan belum saya pahami dengan benar."
        nar "Dosen itu sempat mengerutkan kening keheranan melirik daftar nilai lama atas nama Kisaragi Yutaka, lalu melepas kacamatanya dan menatapmu lurus-lurus. Ia tidak menjanjikan nilai aman ataupun kemudahan khusus; sebaliknya, ia langsung menanyakan bagian mana tepatnya yang benar-benar kau mengerti sekarang."
        nar "Menjawab pertanyaan itu dengan jujur terasa cukup memalukan untuk seorang mahasiswa tahun kedua. Namun setelah mendengarkan jawabanmu tanpa menyela, dosen itu menuliskan daftar bacaan dasar serta tugas susulan yang harus kaukerjakan jika ingin mengejar ketertinggalan."
        nar "Kau keluar dari ruangan itu dengan napas lega yang agak perih—setidaknya kini kau tidak lagi berpura-pura tahu, dan kau tahu persis dari mana harus mulai belajar."
    else:
        nar "Menyadari membaca catatan singkatan Yutaka sendirian hanya akan membuatmu berputar di tempat, kau mengambil ponsel dan mengirim pesan singkat kepada Daichi, teman sekelasmu yang paling paham ritme dosen ini."
        nar "Setengah jam kemudian, Daichi sudah duduk di ruang makan apartemenmu sambil meletakkan dua bungkus roti minimarket dan buku catatannya yang penuh tanda panah warna-warni. Ia menatap wajahmu yang kusut lalu mendengus geli."
        "Daichi" "Wah, tumben banget seorang Kisaragi Yutaka minta tolong soal kuliah. Biasanya kau cuma tidur di barisan belakang tapi pas ujian nilaimu tetap aman."
        yutaka "Jangan mulai mengejek dulu. Kali ini aku beneran mentok dari bab awalnya."
        "Daichi" "Haha, oke, oke—boleh. Kita mulai dari bagian yang bikin kau tersesat, bukan dari soal terakhir. Makan siangnya belakangan saja; mukamu sudah kayak orang mau sidang."
        nar "Sepanjang dua jam berikutnya, Daichi membongkar ulang konsep-konsep dasar itu dengan bahasa manusia biasa yang jauh lebih mudah dicerna daripada singkatan kaku di buku Yutaka."
        nar "Tidak ada pertanyaan aneh darinya soal kenapa kau mendadak lupa materi dasar—hanya seorang teman sekelas yang sabar mengulang penjelasan sampai kau akhirnya benar-benar mengangguk paham."
    return

# ┌─ PANDUAN CERITA · Y06 · Daichi Membocorkan
# │ LOKASI  : Distrik Elite · Apartemen Yutaka
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Daichi tahu sesuatu tentang Shiori/Moeka dan menawarkannya.
# │ INTI    : A bayar dengan makanan / B tolak / C tawar informasi lain.
# │ AKHIRAN : intel; C membuat Daichi mulai mengorek rahasia pemain.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y06:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Daichi membocorkan")
    nar "Daichi datang dengan wajah orang yang mempunyai alasan untuk ditraktir. Ia berhenti bercanda ketika melihat kau benar-benar memperhatikan, lalu menurunkan suara. Cerita tentang orang lain mendadak terdengar seperti sesuatu yang bisa mengubah hubungan, bukan sekadar mengisi waktu makan."
    "Daichi" "Aku dengar sesuatu soal Saionji, juga soal Moeka. Belum semuanya jelas. Kalau kau mau dengar, traktir aku makan. ...Jangan pasang muka begitu, aku juga perlu makan untuk mengingat."
    call kk_family_menu("Y06", ["Bayar dengan mentraktir makan.", "Tolak; kau tak mau berutang padanya.", "Tawar dengan informasi lain."])
    if _return == "A":
        "Daichi" "Baik. Tapi bedakan yang kulihat sendiri dan yang kudengar dari orang. Aku tidak mau besok namaku dipakai untuk menghakimi mereka berdasarkan cerita setengah matang."
    elif _return == "B":
        "Daichi" "Ya sudah. Aku tidak akan memaksamu mendengar. Tapi kalau itu menyangkut keselamatan orang, nanti tetap kuberi tahu. Tidak semuanya pantas ditahan demi makan gratis."
    else:
        nar "Kau menawarkan cerita lain sebagai ganti. Daichi mendengarkan, lalu bertanya bagaimana kau tahu bagian yang tidak banyak dibicarakan itu. Perhatian yang semula tertuju kepada orang lain beralih kepadamu. Kau mendapati harga percakapan ini ternyata bukan sekadar isi informasi yang diserahkan."
    return

# ┌─ PANDUAN CERITA · Y07 · Natal: Apartemen Sepi
# │ LOKASI  : Distrik Elite · Apartemen Yutaka
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Natal; orang tua Kisaragi tidak menelepon.
# │ INTI    : A pergi ke rumah Amamiya / B mengundang heroine / C sendiri / D mengejar Koita
# │ AKHIRAN : hub besar #3 untuk host.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y07:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Natal sepi")
    nar "Natal datang bersama pemberitahuan toko dan pesan promosi. Dari orang tua Kisaragi belum ada panggilan. Kau menaruh satu piring di meja makan yang cukup untuk beberapa orang, lalu memandangi kursi-kursi kosong. Untuk pertama kalinya, kau bertanya seberapa sering Yutaka asli duduk tepat di tempatmu sekarang."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Pergi ke Rumah Amamiya.", "Mengundang seorang heroine.", "Habiskan sendirian.", "Mengejar Koita."])]
    call screen kk_choice_panel(_rows, "Pilihan")
    $ kk_record_choice("Y07", _return)
    if _return == "A":
        koita "Kau datang! Ibu tadi bertanya apa kita perlu menyisakan makanan untukmu. Masuklah. Kau bisa bantu bawa piring, supaya tidak cuma duduk dan mengejekku seperti biasanya."
    elif _return == "B":
        nar "Kau mengundang seseorang yang dekat denganmu dan menjelaskan bahwa malam ini kau ingin ditemani. Ketika ia bersedia datang, kau membersihkan meja dan menyiapkan dua gelas. Kau tidak menyebutnya pengganti keluarga. Kehadirannya punya arti sendiri, dan ia berhak tahu bahwa kau senang ia memilih berada di sini."
    elif _return == "C":
        nar "Kau memilih tinggal sendiri. Makanan dimakan sebelum dingin, lampu ruang tamu tetap menyala. Ada kesedihan yang tidak langsung berubah menjadi keputusan romantis. Menjelang tidur, kau menyadari bahwa menginginkan rumah tidak selalu berarti tahu siapa yang ingin kauajak membangunnya."
    else:
        nar "Kau menghubungi Koita dan mengatakan ingin bertemu dengannya, khusus dengannya. Ia menanyakan apakah ada masalah. Kau menjawab bahwa kau hanya ingin malam ini tidak berlalu tanpa mendengar suaranya. Di ujung telepon, gurauannya mereda; ia memberimu waktu dan tempat untuk datang."
    return

# ┌─ PANDUAN CERITA · Y08 · Coklat dari Siapa
# │ LOKASI  : Distrik Elite · Apartemen Yutaka
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Valentine; Yutaka menerima coklat dari banyak orang.
# │ INTI    : A balas satu orang / B balas semua sama / C tolak semua / D memberi coklat pada Koita
# │ AKHIRAN : menyalakan rantai BL atau rantai heroine.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y08:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Coklat Valentine")
    nar "Kotak-kotak cokelat memenuhi sudut meja. Ada yang disertai pesan ringan, ada yang ditulis begitu hati-hati hingga kau takut membacanya sembarangan. Orang-orang itu tidak sedang menawarkan hadiah yang bisa dinilai satu per satu. Masing-masing telah mengambil risiko untuk diketahui perasaannya."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Balas satu orang saja.", "Balas semua dengan setara.", "Tolak semua.", "Beri coklat pada Koita."])]
    call screen kk_choice_panel(_rows, "Pilihan")
    $ kk_record_choice("Y08", _return)
    if _return == "A":
        nar "Kau memilih membalas satu orang dengan maksud yang jelas. Ucapan terima kasih kepada yang lain tetap perlu ditulis tanpa janji samar. Sebelum menekan kirim, kau membaca ulang balasan itu: apakah ini benar keinginanmu, atau hanya pilihan yang paling mudah dipertanggungjawabkan?"
    elif _return == "B":
        nar "Kau menyiapkan balasan setara bagi semua pengirim. Kesopanan itu menyelamatkanmu dari memilih hari ini, tetapi tidak menjamin setiap orang akan membacanya dengan arti yang sama. Kau merasakan betapa mudah kebaikan dipakai untuk menunda percakapan yang sebenarnya sedang ditunggu."
    elif _return == "C":
        nar "Kau mengucapkan terima kasih lalu menjelaskan bahwa kau tidak dapat membalas harapan romantis mereka. Beberapa jawaban datang singkat, satu belum dibalas. Tidak ada cara membuat penolakan sama sekali tidak sakit. Kau membiarkan mereka kecewa tanpa meminta ditenangkan karena telah merasa bersalah."
    else:
        koita "Untukku? ...Tunggu, kau serius atau sedang menunggu aku salah tingkah? Kalau serius, bilang begitu. Aku mungkin perlu waktu memikirkan jawabannya, tapi aku tidak mau menertawakan sesuatu yang penting bagimu."
    return

# ┌─ PANDUAN CERITA · Y11 · Yukata dan Chiasa
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : festival; Chiasa memakai yukata.
# │ INTI    : A pujian / B gunakan godaan Yutaka asli / C diam.
# │ AKHIRAN : Chiasa menilai apakah "Yutaka" masih Yutaka.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y11:
    call kk_scene_enter("yutaka", "Rumah Amamiya · Yukata dan Chiasa")
    nar "Chiasa keluar dengan yukata, lalu membetulkan ujung lengan yang sebenarnya sudah rapi. Ia berhenti di depanmu seolah ada percakapan yang dijanjikan oleh kebiasaan lama. Kau ingin mengatakan sesuatu yang disukainya, tetapi tidak tahu apakah yang sedang ditunggu adalah suaramu atau suara Yutaka dahulu."
    call kk_family_menu("Y11", ["Puji penampilannya dengan tulus.", "Pakai gaya menggoda Yutaka asli.", "Diam saja."])
    if _return == "A":
        chiasa "Terima kasih. Kau bilang begitu tanpa meledek? Aku sampai menyiapkan jawaban yang tidak jadi dipakai. ...Tidak, jangan diubah. Aku suka mendengarnya."
    elif _return == "B":
        chiasa "Nah, mulai lagi. Aku tahu kau akan menggodaku. Tapi jangan terus sembunyi di balik bercanda, Yutaka. Sesekali aku ingin tahu bagian mana yang sungguh kaukatakan."
    else:
        nar "Kau diam terlalu lama. Chiasa menunduk memeriksa pakaiannya, lalu bertanya apakah ada yang salah. Ketika kau mengatakan tidak, ia mengangguk dan beralih membicarakan jalan menuju festival. Kau mengikuti sambil sadar bahwa diam pun dapat terdengar seperti penilaian."
    return

# ┌─ PANDUAN CERITA · Y12 · Pameran Chiasa
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : pameran seni; Haruka mengenalkan Chiasa.
# │ INTI    : A belikan karya / B hadir saja / C kritik.
# │ AKHIRAN : Chiasa membuka diri atau menjauh.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y12:
    call kk_scene_enter("yutaka", "Rumah Amamiya · Pameran Chiasa")
    nar "Haruka memperkenalkan karya Chiasa kepada pengunjung. Dari samping kau melihat Chiasa mencoba berdiri tenang sambil mengawasi reaksi setiap orang. Ketika menemukan wajahmu, senyumnya sebentar menjadi lebih kecil dan lebih jujur. Kau datang sebagai orang yang mengenalnya sebelum label seniman ditempelkan di dinding."
    call kk_family_menu("Y12", ["Beli salah satu karyanya.", "Hadir dan memberi dukungan.", "Kritik karyanya terang-terangan."])
    if _return == "A":
        chiasa "Kau benar ingin yang ini? Aku senang, tapi jangan membeli karena merasa harus menolongku. Ceritakan bagian yang kausukai. ...Ya. Kalau itu alasanmu, aku ingin kau yang menyimpannya."
    elif _return == "B":
        chiasa "Kau datang. Aku tadi takut akan terlalu sibuk memperhatikan orang yang tidak kukenal. Kalau nanti aku banyak bicara tentang gambarnya, dengarkan, ya. Aku sedang mencoba tidak gugup."
    else:
        nar "Kau menyampaikan kritik di depan pengunjung lain tanpa menanyakan apakah ia siap membahasnya sekarang. Chiasa menjawab seperlunya, kemudian kembali melayani orang yang datang. Kalian belum tentu berbeda pendapat tentang gambar itu. Yang membuatnya menjauh adalah caramu memilih saat untuk mempermalukannya."
    return

# ┌─ PANDUAN CERITA · Y14 · Hari Bentrok: Pernyataan Yutaka
# │ LOKASI  : Distrik Elite · Apartemen Yutaka
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : hari pengakuan.
# │ INTI    : A mengaku pada Chiasa / B mengaku pada Koita / C mengaku pada heroine / D tidak mengaku.
# │ AKHIRAN : hub besar #8.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y14:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Hari pengakuan")
    nar "Hari ini pesan masuk bertumpuk, masing-masing meminta waktu bertemu. Kau meletakkan ponsel dan mencoba memisahkan rasa takut kehilangan dari keinginan sungguh mendekat. Menyatakan cinta berarti berbicara kepada seseorang yang boleh menjawab lain; tidak ada nama dalam daftar kontak yang bisa menjamin keselamatan hatimu."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Mengaku pada Chiasa.", "Mengaku pada Koita.", "Mengaku pada seorang heroine.", "Tidak mengaku pada siapa pun."])]
    call screen kk_choice_panel(_rows, "Pilihan")
    $ kk_record_choice("Y14", _return)
    if _return == "A":
        nar "Kau menemui Chiasa dan mengaku menyukainya. Kau tidak memakai kedekatan keluarga Amamiya sebagai alasan agar ia menerima. Ia mendengarkan sampai selesai, lalu menyebut namamu pelan. Apa pun jawabannya nanti, ia kini tahu ada bagian dari candaanmu yang tidak lagi bisa dianggap biasa."
    elif _return == "B":
        nar "Kau mengatakan kepada Koita bahwa perasaanmu telah melewati persahabatan. Ia diam, lalu bertanya sejak kapan. Kau menjawab sejauh yang benar-benar kauketahui. Tidak ada desakan agar ia segera memilih; hanya keberanian membiarkan seorang sahabat melihatmu tanpa perlindungan lelucon."
    elif _return == "C":
        nar "Kau menemui perempuan yang ingin kaupilih dan mengucapkan perasaanmu dengan jelas. Kau tidak membawa daftar orang lain yang bisa menjadi pengganti. Sesudah kata-kata selesai, ada ruang hening yang menjadi miliknya untuk menjawab. Kau berusaha tidak memenuhi ruang itu dengan janji tambahan."
    else:
        nar "Kau tidak menyatakan cinta hari ini. Ada pesan yang tetap kaubalasi dengan ramah dan percakapan yang kaubawa ke topik lain. Pilihan itu terasa aman sampai malam, ketika kau menyadari bahwa orang yang menunggu juga dapat memutuskan berhenti menunggu tanpa memberimu kesempatan terakhir."
    return

# ┌─ PANDUAN CERITA · Y15 · Jarak dari Rumah
# │ LOKASI  : Distrik Elite · Apartemen Yutaka
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : perjalanan; Yutaka merasa jauh dari keluarga Kisaragi.
# │ INTI    : A bicara dengan Daisuke / B menelepon ibu / C diam.
# │ AKHIRAN : ending Yutaka.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y15:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Jarak dari rumah")
    nar "Jendela kendaraan memperlihatkan rumah-rumah yang akan didatangi orang sepulang bekerja. Kau memikirkan keluarga Kisaragi dan betapa sedikit bagian dari mereka yang kaukenal. Merindukan keluarga lamamu tidak membatalkan kesepian Yutaka. Kini kedua kehilangan itu bertemu dalam satu tubuh yang tidak tahu harus menelepon siapa."
    call kk_family_menu("Y15", ["Bicara dari hati dengan Daisuke.", "Menelepon ibu Kisaragi.", "Diam dan memendamnya."])
    if _return == "A":
        "Daisuke" "Kau boleh bicara denganku tanpa harus menunggu Koita punya masalah dulu. Aku mungkin tidak punya jawaban, tapi aku bisa mendengar. Jangan merasa perlu menghiburku saat kau sendiri sedang susah."
    elif _return == "B":
        nar "Kau menelepon ibu Kisaragi. Ia terkejut, lalu mencoba mengingat kapan terakhir kalian bicara di luar urusan uang. Kehangatannya kaku dan terlambat, tetapi ada. Kau mendengarkan suara seorang ibu yang tidak mengenalmu, bertanya-tanya apakah ia mendengar perubahan pada anak yang sedang ia rindukan."
    else:
        nar "Kau menahan keinginan menelepon. Di luar, rumah-rumah terus berlalu dan percakapan orang lain terdengar jauh. Tidak berbagi membuatmu terhindar dari jawaban yang salah; ia juga membuat tak seorang pun tahu bahwa hari ini kau membutuhkan seseorang untuk bertanya apakah kau baik-baik saja."
    return

# ┌─ PANDUAN CERITA · Y16 · Kembang Api dan Chiasa
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : A mengaku / B bergandengan / C menjaga jarak.
# │ AKHIRAN : Chiasa × Yutaka (NPC) berjalan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y16:
    call kk_scene_enter("yutaka", "Rumah Amamiya · Kembang api dan Chiasa")
    play sound "audio/sfx/fireworks.wav"
    nar "Chiasa berdiri di sebelahmu ketika kembang api pertama menyala. Ia tidak sibuk mencari Koita di antara kerumunan. Di sela suara ledakan, percakapan kalian terputus lalu disambung dengan tawa kecil. Kau bertanya dalam hati apakah kedekatan ini masih ingin kausimpan sebagai kemungkinan yang tidak pernah dinamai."
    call kk_family_menu("Y16", ["Mengaku pada Chiasa.", "Bergandengan tangan tanpa kata.", "Menjaga jarak."])
    if _return == "A":
        chiasa "Aku dengar. Tidak perlu mengulang cuma karena kembang apinya keras. ...Aku ingin tahu apakah besok kau masih akan mengatakannya, saat kita tidak punya langit sebagus ini untuk disalahkan."
    elif _return == "B":
        nar "Kau menawarkan tangan. Chiasa menatapnya sebentar sebelum membiarkan jarinya bertemu jarimu. Kalian tetap melihat langit. Kesediaannya tidak menjawab semua pertanyaan tentang masa depan, tetapi sentuhan itu datang dari dua orang yang sama-sama memilih untuk tidak menjauh malam ini."
    else:
        chiasa "Aku mengerti. Kita bisa melihat kembang apinya saja. ...Jangan memandangku seolah aku harus segera bilang aku tidak kecewa. Aku akan baik-baik saja, tapi beri aku sebentar."
    return

# ┌─ PANDUAN CERITA · Y18 · Pameran Tunggal Chiasa
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : A hadir / B absen / C membawa seseorang.
# │ AKHIRAN : hubungan Yutaka–Chiasa.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y18:
    call kk_scene_enter("yutaka", "Rumah Amamiya · Pameran tunggal Chiasa")
    nar "Nama Chiasa tercetak di undangan pameran tunggalnya. Di bawah judul, ia menulis sepenggal kalimat tentang hal yang ingin dipertahankan ketika semuanya berubah. Kau membaca undangan itu lebih dari sekali. Hari pembukaan punya arti bagi pekerjaannya, bahkan jika hubungan kalian sedang sulit dijelaskan."
    call kk_family_menu("Y18", ["Hadir mendukungnya.", "Absen dari pameran.", "Membawa seseorang bersamamu."])
    if _return == "A":
        chiasa "Kau datang. Aku ingin menunjukkan satu gambar sebelum tempat ini ramai. Bukan karena kau harus punya jawaban yang bagus. Aku hanya ingin kau melihatnya bersamaku."
    elif _return == "B":
        nar "Kau tidak hadir. Chiasa memeriksa pintu beberapa kali sebelum mulai memberi penjelasan kepada pengunjung. Pamerannya tetap berjalan; pekerjaan bertahun-tahun tidak berhenti karena satu kursi kosong. Ketika kau melihat foto acara itu nanti, kau tidak tahu pada saat mana ia akhirnya berhenti mencarimu."
    else:
        nar "Kau datang membawa seseorang dan memperkenalkannya dengan jelas. Chiasa menyambut kalian, lalu menjelaskan karyanya tanpa menjadikan tamumu alat untuk menebak perasaanmu. Ada pertanyaan pribadi yang ia simpan sampai kalian punya kesempatan bicara sendiri. Hari ini ia juga berhak menjadi seniman yang sedang merayakan pekerjaannya."
    return

init 1 python:
    _hook("Y03-A", lambda: kk_suspect("nagisa",-4))
    _hook("Y03-B", lambda: kk_suspect("nagisa",8))
    _hook("Y03-C", lambda: kk_suspect("nagisa",3))
    _hook("Y04-A", lambda: kk_flag("yutaka_kuis_belajar"))
    _hook("Y04-B", lambda: (kk_flag("yutaka_menyontek"), kk_suspect("daichi",5)))
    _hook("Y04-C", lambda: kk_rel("nagisa","trust",2))
    _hook("Y04-D", lambda: kk_flag("daichi_dimintai_tolong"))
    _hook("Y06-A", lambda: kk_flag("daichi_intel_dibeli"))
    _hook("Y06-B", lambda: kk_rel("koita","trust",2))
    _hook("Y06-C", lambda: (kk_flag("daichi_mengorek"), kk_suspect("daichi",6)))
    _hook("Y07-A", lambda: kk_rel("koita","trust",4))
    _hook("Y07-B", lambda: kk_flag("yutaka_rantai_heroine"))
    _hook("Y07-C", lambda: kk_rel("koita","aff",-2))
    _hook("Y07-D", lambda: kk_flag("yutaka_arah_bl"))
    _hook("Y08-A", lambda: kk_flag("yutaka_rantai_heroine"))
    _hook("Y08-B", lambda: None)
    _hook("Y08-C", lambda: None)
    _hook("Y08-D", lambda: (kk_flag("yutaka_arah_bl"), kk_rel("koita","intim",5)))
    _hook("Y11-A", lambda: kk_suspect("chiasa",4))
    _hook("Y11-B", lambda: kk_suspect("chiasa",-5))
    _hook("Y11-C", lambda: kk_suspect("chiasa",6))
    _hook("Y12-A", lambda: (kk_flag("chiasa_karya_dibeli"), kk_rel("chiasa","intim",4)))
    _hook("Y12-B", lambda: kk_rel("chiasa","trust",4))
    _hook("Y12-C", lambda: kk_rel("chiasa","aff",-4))
    _hook("Y14-A", lambda: kk_flag("yutaka_arah_chiasa"))
    _hook("Y14-B", lambda: kk_flag("yutaka_arah_bl"))
    _hook("Y14-C", lambda: kk_flag("yutaka_rantai_heroine"))
    _hook("Y14-D", lambda: None)
    _hook("Y15-A", lambda: (kk_flag("kisaragi_daisuke_dekat"), kk_adj("hubungan_keluarga_kisaragi",8)))
    _hook("Y15-B", lambda: kk_adj("hubungan_keluarga_kisaragi",5))
    _hook("Y15-C", lambda: kk_adj("hubungan_keluarga_kisaragi",-5))
    _hook("Y16-A", lambda: (kk_rel("chiasa","intim",8), kk_flag("yutaka_chiasa_diakui")))
    _hook("Y16-B", lambda: (kk_rel("chiasa","intim",6), kk_flag("yutaka_arah_chiasa")))
    _hook("Y16-C", lambda: kk_rel("chiasa","jeal",4))
    _hook("Y18-A", lambda: (kk_rel("chiasa","intim",6), kk_flag("chiasa_pameran_yutaka_hadir")))
    _hook("Y18-B", lambda: kk_rel("chiasa","aff",-4))
    _hook("Y18-C", lambda: kk_rel("chiasa","jeal",4))
