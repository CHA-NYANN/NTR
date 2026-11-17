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
    nagisa "Yuu-kun! ...Aneh, ya, sekarang memanggil begitu. Dulu kau selalu menoleh duluan kalau aku meneriakkannya. Kau masih ingat?"
    call kk_family_menu("Y03", ["Jawab natural seolah memang ingat.", "Salah menyebut kenangannya.", "Pura-pura lupa sambil tersenyum."])
    if _return == "A":
        nagisa "Masih ingat rupanya. Aku juga tidak ingat semuanya dengan tepat. Yang kuingat, kita selalu merasa besok bisa main lagi. ...Baguslah kau masih mau menoleh."
    elif _return == "B":
        nar "Kau menyebut kenangan yang salah. Nagisa sempat tertawa, lalu berhenti ketika sadar kau sungguh mengiranya benar. Ia membetulkan satu nama dengan pelan. Kau mengikuti ceritanya sambil menyadari bahwa masa lalu mereka tidak bisa dipelajari seperti jawaban ujian."
    else:
        nagisa "Lupa? Kau biasanya paling berisik mengingatkan hal begitu. ...Ya sudah, nanti kuceritakan. Tapi jangan cuma mengangguk kalau sebenarnya tidak ingat. Aku bisa kesal karena itu."
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
    nar "Pengumuman kuis menyusul kuliah yang sebagian besar tidak kaupahami. Catatan lama Yutaka rapi dan penuh singkatan yang tampaknya cukup untuknya. Bagimu setiap halaman justru membuka pertanyaan baru. Punya kartu mahasiswa bukan berarti mewarisi tahun-tahun yang telah ia pelajari."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Belajar semalaman mengejar ketertinggalan.", "Menyontek saat kuis.", "Jujur ke dosen soal kesulitanmu.", "Minta bantuan Daichi."])]
    call screen kk_choice_panel(_rows, "Pilihan")
    $ kk_record_choice("Y04", _return)
    if _return == "A":
        nar "Kau menghabiskan malam mengejar dasar yang hilang. Ada soal yang akhirnya masuk akal, ada halaman yang tetap membingungkan. Saat berangkat, kau membawa pengetahuan yang terbatas tetapi milikmu sendiri. Nilai nanti akan mengukur pekerjaan malam ini, bukan reputasi orang yang namanya tertulis di lembar jawaban."
    elif _return == "B":
        nar "Kau menyontek. Kelegaan ketika jawaban terisi segera berubah menjadi takut saat pengawas berhenti di dekat mejamu. Di akhir kuis, lembar yang dikumpulkan bukan lagi sekadar hasil yang tidak kaumengerti: ada pelanggaran yang dapat menuntut pertanggungjawabanmu, dan kekayaan keluarga tidak menghapusnya."
    elif _return == "C":
        nar "Kau menemui dosen dan mengakui ada bagian dasar yang tertinggal. Ia tidak menjanjikan nilai aman, tetapi memberi kesempatan membahas kesulitan itu dan pekerjaan susulan yang harus kaujalani. Ditanya apa yang benar-benar kaupahami terasa memalukan; setidaknya kini kau tahu apa yang harus dipelajari."
    else:
        "Daichi" "Tumben minta tolong soal kuliah. Boleh. Kita mulai dari bagian yang membuatmu tersesat, bukan dari soal terakhir. Makan siangnya belakangan saja; mukamu sudah seperti orang mau sidang."
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
