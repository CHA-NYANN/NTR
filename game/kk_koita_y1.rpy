# Lapisan kesadaran Koita, Tahun 1 (K01, K03, K06, K09, K10, K11).
# Koita adalah aktor yang membalas (NPC mandiri). Event observasional: pemain membaca pola,
# Koita mulai merasa diperhatikan. Efek mengikuti Event_Koita; angka adalah setelan prototipe.
# Gerbang rute BL/Koita-Success (K04-D, K10-A) TIDAK dibangun di sini.
# ┌─ PANDUAN CERITA · K01 · Senyum yang Terlalu Cepat
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : kantin hari pertama; Koita menyapa tiga heroine dengan tiga kalimat berbeda.
# │ INTI    : A amati dan catat polanya / B tegur terang-terangan / C abaikan.
# │ AKHIRAN : A membuka pola_koita_dikenal (intel); B membuat Koita waspada ringan; C tidak ada.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K01:
    call kk_scene_enter("koita", "Gedung Sastra")
    if kk_host == "chiasa":
        nar "Jam makan siang di kantin dekat Gedung Sastra penuh dengan riuh rendah mahasiswa yang baru selesai mengikuti kelas dan sesi pengenalan hari pertama. Aroma kari hangat, kuah udon, serta bunyi baki plastik yang diletakkan di atas meja panjang bercampur di bawah cahaya matahari siang yang masuk melalui jendela kaca tinggi."
        nar "Baru saja selesai dari acara orientasi di sayap barat, kau melangkah menyusuri lorong meja sambil memegangi nampan makan siangmu. Dua langkah sebelum mencapai barisan kursi dekat jendela, langkahmu melambat ketika melihat sosok Amamiya Koita sudah duduk di sana—dan sebuah pertunjukan kecil sedang berlangsung tepat di depan matamu."
        nar "Di sebelah meja, Sakurajima Nagisa baru saja tiba sambil menyeimbangkan nampan makan siang dan gulungan kertas gambar di ketiaknya. Tanpa diminta, Koita langsung menahan sandaran kursi kosong di sebelahnya dengan lutut agar tidak bergeser sambil merapikan tasnya sendiri supaya Nagisa bisa meletakkan nampan dengan mudah."
        nar "Namun belum sempat Koita benar-benar duduk, matanya sudah menangkap sosok Tachibana Miyuki yang melintas di lorong sambil memeluk map plastik dan segelas kopi dari mesin penjual otomatis. Koita langsung mengangkat satu tangan dan melambai dengan senyum hangat."
        koita "Miyuki-senpai, sudah makan siang? Jangan minum kopi lagi dong, ya. Kemarin katanya perut Senpai agak nggak enak habis jaga praktikum."
        nar "Langkah anggun Miyuki terhenti di tepi meja. Mahasiswi tahun ketiga Kedokteran itu mengedip pelan, lalu tersenyum lembut yang tampak tulus tersentuh."
        miyuki "Ara, Koita-kun masih ingat hal sekecil itu? Senpai jadi terharu lho. Baiklah, setelah mengantar map ini ke ruang dosen, Senpai janji beli roti dulu sebelum lanjut."
        nar "Di samping Koita, ujung alis Nagisa langsung berkedut tipis mendengar nada hangat itu. Ia meletakkan sumpit kayunya di atas nampan dengan bunyi yang sedikit lebih keras dari biasanya."
        nagisa "Kalau ingatanmu soal orang lain memang sehebat itu, harusnya kau juga ingat janjimu mengembalikan buku catatanku yang kaupinjam minggu lalu, Ko-kun."
        nar "Koita sama sekali tidak tampak kikuk. Ia memutar tubuhnya menghadap Nagisa sepenuhnya, menepuk tas selempangnya, lalu menurunkan suaranya menjadi nada lembut yang seolah hanya ditujukan untuk mereka berdua."
        koita "Ada di tas kok, sudah kubawa dari pagi. Sengaja kutaruh di sini supaya aku punya alasan buat duduk dan makan siang bareng kamu hari ini, Nagisa-chan."
        nar "Rona merah tipis langsung naik ke pipi Nagisa. Ia mendengus pelan dan membuang muka ke arah jendela, tetapi tangannya tetap menggeser tasnya sedikit ke samping untuk memberi Koita ruang duduk yang lega."
        nar "Tepat di belakang Miyuki, Kujo Harumi melintas pelan sambil mendekap sebuah buku sampul tebal. Sebelum Harumi sempat hanya mengangguk singkat dan berlalu, Koita sudah lebih dulu mengangkat buku saku yang tadi sempat ia jadikan alas tepi nampan di meja, memperlihatkan sampulnya."
        koita "Harumi-san! Aku sudah baca novel rekomendasi darimu kemarin malam. Bagian akhirnya bikin kepikiran terus—nanti kalau ada waktu luang, tolong jelaskan sudut pandangmu soal bab terakhirnya, ya. Aku mau dengar pendapatmu dulu sebelum baca ulasan lain."
        nar "Langkah Harumi melambat. Sorot matanya yang tadinya datar sedikit melunak, memancarkan binar kecil seseorang yang merasa pendapatnya sungguh-sungguh dinantikan."
        harumi "...Baiklah, Amamiya-kun. Kalau kamu memang sudah selesai membacanya sampai akhir, nanti aku bisa jelaskan di perpustakaan atau kafe."
        nar "Kau berdiri diam di pinggir lorong memegangi nampanmu, menyaksikan seluruh rangkaian itu dalam waktu kurang dari dua menit. Tiga gadis, tiga cara berbeda untuk membuat masing-masing dari mereka merasa diingat dan ditunggu."
        nar "Dan satu detail kecil langsung menusuk matamu: setiap kali Koita melontarkan kalimat-kalimat manis itu, senyum hangatnya selalu tiba sepersekian detik lebih cepat daripada jawaban lawan bicaranya—seolah ia sedang memeriksa apakah kehangatannya berhasil mengena."
    else:
        nar "Jam makan siang di kantin dekat Gedung Sastra penuh dengan suara mahasiswa yang baru bubar dari kelas pagi. Aroma kari hangat, kuah udon, dan bunyi baki plastik yang diletakkan di meja panjang bercampur di bawah sinar matahari yang masuk dari jendela kaca tinggi."
        nar "Baru saja selesai dari mata kuliah Ekonomi pagi, kau melangkah menyusuri lorong meja sambil membawa nampan makan siangmu. Beberapa langkah sebelum mencapai meja panjang dekat jendela, langkahmu melambat ketika melihat sahabat masa kecil pemilik tubuh ini—Amamiya Koita—sedang menjalankan pertunjukan klasiknya tepat di depan matamu."
        nar "Di samping meja, Sakurajima Nagisa baru saja tiba sambil menyeimbangkan nampan makan siang dan gulungan kertas gambar di ketiaknya. Tanpa perlu diminta, Koita langsung menahan sandaran kursi kosong di sebelahnya dengan lutut sambil menggeser tasnya sendiri agar Nagisa bisa meletakkan nampan dengan mudah."
        nar "Namun belum sempat Koita benar-benar duduk, matanya sudah menangkap sosok Tachibana Miyuki yang melintas di lorong sambil memeluk map plastik dan segelas kopi dari mesin penjual otomatis. Koita segera mengangkat tangan melambai dengan senyum hangat."
        koita "Miyuki-senpai, sudah makan siang? Jangan minum kopi lagi dong, ya. Kemarin katanya perut Senpai agak nggak enak habis jaga praktikum."
        nar "Langkah anggun Miyuki terhenti di tepi meja. Mahasiswi tahun ketiga Kedokteran itu mengedip pelan, lalu tersenyum lembut yang tampak sungguh-sungguh tersentuh."
        miyuki "Ara, Koita-kun masih ingat hal sekecil itu? Senpai jadi terharu lho. Baiklah, setelah mengantar map ini ke ruang dosen, Senpai janji beli roti dulu sebelum lanjut."
        nar "Di sebelah Koita, ujung alis Nagisa langsung berkedut tipis mendengar nada hangat itu. Ia meletakkan sumpit kayunya di atas nampan dengan bunyi agak keras."
        nagisa "Kalau ingatanmu soal orang lain memang sehebat itu, harusnya kau juga ingat janjimu mengembalikan buku catatanku yang kaupinjam minggu lalu, Ko-kun."
        nar "Koita sama sekali tidak tampak gugup. Ia memutar tubuhnya menghadap Nagisa, menepuk tas selempangnya, lalu menurunkan suaranya menjadi nada lembut yang seolah hanya ditujukan untuk mereka berdua."
        koita "Ada di tas kok, sudah kubawa dari pagi. Sengaja kutaruh di sini supaya aku punya alasan buat duduk dan makan siang bareng kamu hari ini, Nagisa-chan."
        nar "Rona merah tipis langsung naik ke pipi Nagisa. Ia mendengus pelan dan membuang muka ke arah jendela, tetapi tangannya tetap menggeser tasnya sedikit ke samping untuk memberi Koita ruang duduk."
        nar "Tepat di belakang Miyuki, Kujo Harumi melintas pelan sambil mendekap sebuah buku sampul tebal. Sebelum Harumi sempat hanya mengangguk singkat dan berlalu, Koita sudah lebih dulu mengangkat buku saku yang tadi sempat ia jadikan alas tepi nampan, memperlihatkan sampulnya."
        koita "Harumi-san! Aku sudah baca novel rekomendasi darimu kemarin malam. Bagian akhirnya bikin kepikiran terus—nanti kalau ada waktu luang, tolong jelaskan sudut pandangmu soal bab terakhirnya, ya. Aku mau dengar pendapatmu dulu sebelum baca ulasan lain."
        nar "Langkah Harumi melambat. Sorot matanya yang tadinya datar sedikit melunak, memancarkan binar kecil seseorang yang merasa pendapatnya dinantikan."
        harumi "...Baiklah, Amamiya-kun. Kalau kamu memang sudah selesai membacanya sampai akhir, nanti aku bisa jelaskan di perpustakaan atau kafe."
        nar "Kau berdiri diam di tepi lorong memegangi nampanmu, menyaksikan semuanya berlangsung kurang dari dua menit. Tiga gadis, tiga cara berbeda untuk membuat masing-masing dari mereka merasa diingat dan ditunggu."
        nar "Dan satu detail kecil tidak luput dari pengamatanmu: setiap kali Koita melontarkan kalimat manis itu, senyum hangatnya selalu tiba sepersekian detik lebih cepat daripada jawaban mereka—seolah ia sedang memeriksa apakah kehangatannya berhasil mengena."
    call kk_family_menu("K01", ["Amati dan catat polanya diam-diam.", "\"Itu namanya ramah, atau sengaja pilih kasih biar semua menunggu?\"", "Abaikan saja dan langsung ikut duduk."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau menahan diri untuk tidak langsung melangkah maju atau menyela. Kau berdiri diam di dekat tiang kantin selama beberapa detik lagi, memetakan setiap detail cara kerja Koita di kepalamu."
            nar "Kau memperhatikan siapa yang ia tatap ketika menyebut kata 'nanti' kepada Harumi—tidak ada hari, jam, atau tempat yang benar-benar dikunci. Kepada Miyuki, ia menawarkan kepedulian yang manis tanpa harus ikut menemaninya pergi. Dan kepada Nagisa, satu kalimat menggoda yang terdengar pribadi sudah cukup memadamkan rasa kesalnya."
            nar "Tidak ada satu pun komitmen nyata yang keluar dari mulutnya, tetapi ketiga gadis itu menerima potongan kecil dari perhatian dan masa depannya."
            nar "Baru ketika Miyuki melangkah pergi membawa map dan Harumi berjalan menuju rak pengembalian baki, tatapan Koita akhirnya menangkap sosokmu yang berdiri diam memegang nampan di pinggir lorong."
            koita "Lho, Chi-chan? Dari tadi berdiri di situ saja? Kenapa nggak langsung panggil—mau duduk bareng di sini juga?"
            nar "Mendengar panggilan masa kecil 'Chi-chan' itu keluar begitu akrab di tengah kantin masih meninggalkan rasa ganjil di tenggorokanmu, mengingat tubuh ini bukan milikmu yang sebenarnya."
            nar "Bahkan sebelum kau sempat mengangguk, Koita sudah lebih dulu menggeser kursi kosong di seberangnya dengan satu tangan sambil tersenyum ramah. Di sebelahnya, Nagisa menoleh sekilas ke arahmu sambil meletakkan gelas airnya."
            nagisa "Oh, acara pengenalan Fakultas Seni sudah selesai, Chiasa?"
            chiasa "Baru saja selesai. Aku ikut duduk di sini, ya."
            nar "Kau berjalan mendekat dan meletakkan nampanmu di meja. Saat kau duduk, satu catatan penting sudah terkunci rapi di benakmu: keramahan Koita memang nyata—tetapi sama nyatanya dengan betapa cepat matanya memeriksa apakah keramahan itu berhasil menahan orang-orang di sekelilingnya."
        else:
            nar "Kau menahan langkah di dekat tiang kantin selama beberapa detik lagi, memetakan cara kerja sang protagonis di dalam kepalamu tanpa menarik perhatian."
            nar "Kau memperhatikan siapa yang ia tatap ketika menyebut kata 'nanti' kepada Kujo-san—tidak ada hari, jam, atau tempat yang benar-benar disepakati. Kepada Miyuki-senpai, ia menawarkan kepedulian hangat tanpa harus ikut menemaninya. Dan kepada Nagisa, satu kalimat manis yang terdengar pribadi langsung meredam kekesalannya."
            nar "Tidak ada satu pun janji konkret yang keluar dari mulutnya, tetapi masing-masing dari mereka pergi atau duduk dengan membawa sepotong kecil dari masa depannya."
            nar "Baru ketika Miyuki-senpai melangkah pergi membawa map dan Kujo-san berjalan menjauh, tatapan Koita akhirnya menangkap sosokmu yang berdiri diam memegangi nampan."
            koita "Lho, Yutaka? Tumben diam saja di situ—mau duduk bareng di sini juga?"
            nar "Bahkan sebelum kau sempat menjawab, Koita sudah lebih dulu menggeser kursi kosong di seberangnya dengan satu tangan sambil tersenyum ramah. Nagisa di sebelahnya ikut menoleh sekilas."
            nagisa "Kelasmu baru selesai juga, Yutaka?"
            yutaka "Baru saja. Aku ikut duduk sini."
            nar "Kau melangkah mendekat dan menaruh nampanmu. Saat kau duduk, satu hal sudah terkunci rapi di kepalamu: keramahan Koita memang nyata—begitu pula betapa cepat matanya memeriksa apakah keramahan itu berhasil bekerja."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kau tidak membiarkan pertunjukan kecil itu berlalu begitu saja. Kau melangkah maju mendekati meja panjang, meletakkan nampan makan siangmu di pinggir kayu dengan bunyi yang cukup jelas untuk menarik perhatian, lalu menatap Koita lurus-lurus sebelum Miyuki dan Harumi sempat menjauh."
            chiasa "Hebat juga, ya. Dalam waktu kurang dari dua menit, semua orang kebagian jatah perhatian khusus masing-masing—tapi tidak ada satu pun yang jelas kapan waktunya. Itu namanya ramah, atau sengaja pilih kasih supaya semua tetap menunggu?"
            nar "Seketika, obrolan hangat di sekitar meja itu terhenti total. Miyuki yang baru hendak membalikkan badan ikut terdiam dengan map masih di pelukannya, sementara Harumi menunduk sedikit menatap sampul bukunya dengan wajah canggung."
            nar "Senyum hangat di wajah Koita mengendur sepersekian detik. Ia berkedip kaget, lalu menggaruk pelipisnya pelan sambil tertawa pendek yang berusaha terdengar ringan."
            koita "Eh, pilih kasih? Maksudmu apa sih, Chi-chan? Aku kan cuma ingat hal-hal kecil tentang teman-teman sendiri. Masa menanyakan kabar Senpai atau bahas buku sama Harumi-san dianggap aneh? Kamu juga begitu ke teman-temanmu, kan?"
            nar "Sebelum kau sempat membalas, Nagisa yang duduk di sebelah Koita langsung menoleh ke arahmu dengan kening berkerut dan nada membela yang muncul begitu saja."
            nagisa "Memangnya hal sepele begini harus diributkan di tengah kantin? Ko-kun kan dari dulu memang begitu orangnya kalau sama teman."
            miyuki "Ara, tidak perlu tegang begitu. Kalau begitu Senpai duluan ya, nanti terlambat mengantar map ke ruang dosen."
            nar "Miyuki tersenyum halus untuk meredakan suasana lalu melangkah pergi, diikuti Harumi yang mengangguk pelan sebelum cepat-cepat menjauh dari meja."
            nar "Koita tertawa kecil untuk mencairkan sisa kecanggungan dan menggeserkan kursi kosong untukmu seolah tidak ada yang berubah. Namun sepanjang sisa jam makan siang itu, kau merasakan betul pergeserannya: setiap kali ada kenalan lewat di lorong kantin, tatapan Koita sempat melirik ke arahmu terlebih dahulu sebelum ia memutuskan bagaimana cara menyapa mereka."
        else:
            nar "Kau tidak membiarkan tontonan itu lewat begitu saja. Kau melangkah mendekati meja panjang, meletakkan nampan makan siangmu di pinggir meja dengan bunyi yang cukup keras untuk memotong obrolan, lalu menatap sahabat masa kecil pemilik tubuh ini lurus-lurus sebelum Miyuki-senpai dan Kujo-san sempat pergi."
            yutaka "Santai amat bagi-bagi janji kosongnya, Koita. Kurang dari dua menit, semua kebagian 'nanti' masing-masing—tapi satu jadwal pun nggak ada yang jelas. Itu namanya ramah, atau memang sengaja pilih kasih biar semuanya terus menunggu?"
            nar "Seketika, percakapan ringan di meja itu berhenti total. Miyuki-senpai yang baru hendak berbalik terhenti dengan map di pelukannya, sementara Kujo-san menunduk kaku menatap sampul bukunya."
            nar "Senyum hangat di wajah Koita surut sepersekian detik. Ia mengerjap, lalu menggaruk tengkuknya dengan tawa pendek yang berusaha terdengar santai."
            koita "Pilih kasih? Maksudmu apa sih, Yutaka? Aku kan cuma ingat hal-hal kecil tentang teman-teman sendiri. Masa menanyakan kabar Miyuki-senpai atau bahas buku sama Harumi-san dianggap aneh? Kau juga begitu ke teman-temanmu, kan?"
            nar "Sebelum kau sempat menimpali, Nagisa yang duduk di sebelah Koita langsung menoleh ke arahmu dengan kening berkerut dan nada membela yang refleks muncul."
            nagisa "Memangnya hal begini harus diributkan di tengah kantin, Yutaka? Ko-kun kan dari dulu memang begitu orangnya kalau sama teman."
            miyuki "Ara, jangan tegang begitu. Kalau begitu Senpai duluan ya, Koita-kun, Yutaka-kun—nanti terlambat mengantar map."
            nar "Miyuki-senpai tersenyum halus untuk meredakan keadaan lalu melangkah pergi, disusul Kujo-san yang mengangguk singkat sebelum cepat-cepat menjauh dari meja."
            nar "Koita tertawa kecil untuk mencairkan suasana dan menarikkan kursi untukmu seolah semuanya biasa saja. Namun sejak saat itu, setiap kali ada kenalan lewat di dekat meja kalian, kau menangkap betul sorot matanya yang sempat melirik ke arahmu terlebih dahulu sebelum ia menyapa orang lain."
    else:
        if kk_host == "chiasa":
            nar "Kau memutuskan tidak membuang tenaga mengomentari kebiasaan lama sang protagonis di hari pertama kuliah. Kau melangkah santai mendekati meja panjang, menarik kursi kosong di ujung yang tidak mengganggu siapa pun, lalu meletakkan nampan makan siangmu sambil menyapa biasa."
            chiasa "Meja ini ramai juga. Aku ikut duduk di ujung sini ya—jam istirahat Fakultas Seni lumayan mepet, habis ini masih ada pengarahan ruang studio."
            nar "Koita langsung menyambut topik aman itu dengan mudah dan tampak lega. Ia menggeser tempat sumpit ke arahmu sambil menanyakan bagaimana kesan gedung Fakultas Seni Rupa di sayap barat."
            koita "Oh, sudah selesai sesi pembukaannya? Gedung sayap barat lumayan jauh kan kalau jalan kaki dari gerbang depan? Kalau nanti kelasmu selesai sore, kabari saja ya."
            nar "Tanpa ada gesekan tambahan, kerumunan kecil di sekitar meja itu perlahan terurai dengan sendirinya. Miyuki tersenyum pamit dan melanjutkan langkahnya sambil memeluk map menuju ruang dosen, Harumi menyimpan kembali bukunya ke dalam tas kanvas dan mengangguk pelan sebelum pergi, sementara Nagisa membuka buku catatan yang akhirnya dikeluarkan Koita dari tasnya."
            nar "Masing-masing dari mereka pergi atau melanjutkan siang membawa potongan percakapan yang terasa utuh dan menyenangkan di kepala mereka sendiri—sangat berbeda dari keseluruhan gambaran yang baru saja kaudengar dan kausaksikan dari pinggir lorong."
        else:
            nar "Kau memutuskan tidak perlu repot-repot mengomentari kebiasaan lama sang protagonis siang ini. Kau melangkah santai mendekati meja panjang, menarik kursi kosong di ujung, lalu meletakkan nampan makan siangmu sambil membuka obrolan biasa."
            yutaka "Meja ini ramai juga. Aku ikut duduk di sini ya—kelas pagi tadi lumayan bikin pusing, habis ini masih ada kelas siang."
            nar "Koita langsung menyambut topik aman itu dengan mudah dan tampak lega. Ia menggeser wadah sumpit ke arahmu sambil tertawa kecil."
            koita "Baru hari pertama sudah mengeluh pusing? Dosenmu semester ini galak banget ya? Kalau butuh tempat tenang buat baca catatan, nanti ikut ke perpustakaan saja."
            nar "Tanpa ada gesekan apa pun, lingkaran kecil di meja itu perlahan bubar dengan sendirinya. Miyuki-senpai tersenyum pamit dan melanjutkan langkah membawa map, Kujo-san menyimpan kembali bukunya ke dalam tas kanvas lalu mengangguk singkat sebelum pergi, sementara Nagisa membuka buku catatan yang akhirnya dikeluarkan Koita dari tasnya."
            nar "Masing-masing dari mereka pergi atau melanjutkan siang membawa potongan percakapan yang terasa utuh dan menyenangkan di kepala mereka sendiri—jauh berbeda dari keseluruhan gambaran yang baru saja kaudengar dari pinggir lorong."
    return

# ┌─ PANDUAN CERITA · K03 · Tanzaku Koita
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : aula Tanabata; tanzaku Koita: "semoga semuanya tetap seperti ini".
# │ INTI    : A baca diam-diam / B tukar dengan tanzaku lain / C tulis balasan di sebelahnya.
# │ AKHIRAN : A memberi ketakutan_koita; B bisa menjadi sabotase kecil; C membuat Koita merasa "dilihat".
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K03:
    call kk_scene_enter("koita", "Gedung Sastra · Tanabata")
    if kk_host == "chiasa":
        nar "Menjelang sore di awal Juli, selasar utama Gedung Sastra dipenuhi deretan pot bambu tinggi yang dipasang panitia mahasiswa untuk perayaan Tanabata. Ratusan lembar kertas tanzaku warna-warni bergantung di setiap dahan, berdesir pelan setiap kali angin panas musim panas bertiup masuk dari pintu lobi."
        nar "Saat kau mampir ke gedung ini selepas kelas sore, kau melihat Koita berdiri sendirian di depan salah satu dahan bambu bagian tengah. Di atas meja panjang di belakangnya, spidol-spidol warna dan tumpukan kertas kosong berserakan."
        nar "Kau melangkah mendekat dan sempat melirik beberapa tanzaku milik mahasiswa lain yang tergantung di sekitar sana. Harapan mereka hampir semuanya tegas dan mengarah ke depan: 'Lolos ujian semester', 'Diterima magang', 'Berani menyatakan cinta bulan ini'."
        nar "Berbeda dari semua itu, selembar kertas biru muda yang baru saja diikat Koita tepat setinggi pandangan mata hanya memuat satu baris kalimat pendek."
        nar "Semoga semuanya tetap seperti ini."
        nar "Ketika matamu turun sedikit ke bagian bawah tulisan itu, kau melihat bekas beberapa huruf yang dicoret tebal berkali-kali dengan spidol hitam. Coretannya nyaris menutup seluruh kata, tetapi dari lengkungan huruf depannya, kau masih bisa membedakan awal kata 'jangan' sebelum ia memutuskan menutup sisanya."
        nar "Menyadari kehadiranmu di sampingnya, Koita menoleh lalu menyunggingkan senyum kecil yang sedikit kikuk sambil menggaruk pelipisnya."
        koita "Eh, Chi-chan? Tumben main sampai Gedung Sastra. Punyaku nggak ambisius banget, ya... yang lain semua minta masa depan. Aku malah minta hari ini diperpanjang."
        nar "Nadanya terdengar ringan seperti gurauan biasa, tetapi matanya sempat melirik kembali kertas biru muda itu sebelum kembali menatapmu."
    else:
        nar "Menjelang sore di awal Juli, selasar utama Gedung Sastra dipenuhi deretan pot bambu tinggi yang dipasang panitia mahasiswa untuk perayaan Tanabata. Ratusan lembar kertas tanzaku warna-warni bergantung di setiap dahan, berdesir pelan setiap kali angin hangat musim panas masuk dari pintu lobi."
        nar "Saat kau mampir ke Gedung Sastra selepas kelas untuk mencari Koita, kau melihatnya berdiri sendirian di depan salah satu dahan bambu bagian tengah. Di meja panjang di belakangnya, spidol-spidol warna dan tumpukan kertas kosong masih berserakan."
        nar "Sambil berjalan mendekat dengan tangan di saku celana, matamu sempat menyapu tanzaku milik mahasiswa lain di sekitar sana. Harapan mereka nyaris semuanya tegas dan menghadap ke depan: 'Lolos ujian', 'Dapat magang', 'Berani menyatakan cinta bulan ini'."
        nar "Kontras dengan semuanya, selembar kertas biru muda yang baru saja diikat Koita tepat setinggi pandangan mata hanya berisi satu baris kalimat sederhana."
        nar "Semoga semuanya tetap seperti ini."
        nar "Di bawah baris itu, ada bekas beberapa huruf yang dicoret tebal berkali-kali dengan spidol hitam. Coretannya memang rapat, tetapi dari lengkungan huruf depannya, kau masih bisa membedakan awal kata 'jangan' sebelum ia memutuskan menutup sisanya."
        nar "Menyadari langkahmu berhenti di sampingnya, Koita menoleh lalu menyunggingkan senyum kecil yang agak kikuk sambil menggaruk tengkuknya."
        koita "Eh, Yutaka? Tumben mampir sampai Gedung Sastra. Punyaku nggak ambisius banget, ya... yang lain semua minta masa depan. Aku malah minta hari ini diperpanjang."
        nar "Ia mengucapkannya dengan nada ringan seolah sedang menertawakan diri sendiri, tetapi matanya sempat melirik kembali kertas biru muda itu sebelum kembali menatapmu."
    call kk_family_menu("K03", ["Baca diam-diam lalu tinggalkan.", "Tukar diam-diam dengan tanzaku lain.", "Tulis balasan di tanzaku sebelahnya."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau tidak menanyakan kata apa yang tadi ia coret, dan kau juga tidak menggoda kalimatnya seperti kebiasaan Chiasa. Kau hanya membaca baris itu sekali lagi dalam diam, lalu mengangguk kecil."
            chiasa "Nggak masalah kok, Ko-nii. Harapan orang kan memang beda-beda. Aku duluan ke kantin ya, tadi janji beli minum."
            nar "Senyum lega langsung kembali utuh di wajah Koita. Ia melambai santai dan berbalik menuju meja spidol untuk mengembalikan pena yang tadi ia pakai."
            koita "Oke, nanti pulang bareng, ya!"
            nar "Kau berbalik melangkah beberapa meter menuju koridor, tetapi tepat sebelum berbelok di pilar lobi, kau sempat menoleh sekilas ke belakang."
            nar "Di depan dahan bambu itu, Koita ternyata tidak langsung pergi. Ia kembali melangkah mendekati kertas biru mudanya, memegang ujung talinya dengan kedua jari, lalu mengencangkan simpulnya sekali lagi dengan sangat hati-hati—padahal angin yang masuk ke dalam selasar nyaris tak cukup kencang untuk menjatuhkan sehelai kertas pun."
            nar "Kau melanjutkan langkah sambil menyimpan pemandangan itu rapat-rapat di kepalamu. Gerakan kecil barusan jauh lebih jujur daripada kalimat manis mana pun: seseorang yang harus memastikan permintaannya terikat cukup kuat sebelum berani meninggalkannya."
        else:
            nar "Kau tidak mengomentari kalimatnya, tidak mengejeknya seperti kebiasaan Yutaka, dan tidak menanyakan huruf apa yang ia coret di bawahnya. Kau hanya mengangguk singkat lalu mengangkat satu tangan."
            yutaka "Terserah kau lah, Koita. Harapan orang kan memang beda-beda. Aku duluan ke depan ya, mau beli minum."
            nar "Senyum lega langsung kembali utuh di wajah Koita. Ia mengangguk santai lalu berbalik menuju meja panjang untuk mengembalikan spidol yang tadi ia pakai."
            koita "Oke, nanti ketemu di depan gerbang!"
            nar "Kau melangkah pergi menyusuri selasar, tetapi tepat sebelum berbelok di balik pilar lobi, kau sempat melirik sekilas ke belakang."
            nar "Di depan dahan bambu itu, Koita ternyata tidak langsung beranjak. Ia berjalan balik mendekati kertas biru mudanya, memegang ujung benangnya dengan kedua jari, lalu mengencangkan simpulnya sekali lagi dengan teliti—padahal tidak ada angin yang cukup kencang di dalam ruangan untuk menjatuhkannya."
            nar "Kau menyimpan pemandangan itu dalam diam. Gerakan kecil barusan tertinggal jauh lebih jelas di kepalamu daripada kalimatnya: seseorang yang harus memeriksa apakah permintaannya sudah cukup aman sebelum berani ditinggalkan."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Begitu Koita berbalik menuju meja panjang untuk mengembalikan spidol dan membuang sobekan benang, kau bergerak cepat tanpa bersuara."
            nar "Dengan dua jari, kau melepas simpul longgar kertas biru mudanya dari dahan tengah yang mencolok, lalu menukarnya persis dengan sebuah tanzaku hijau milik entah siapa dari dahan paling bawah yang agak tertutup daun."
            nar "Keinginannya tidak hilang dan tidak kaurusak—hanya saja kini tidak lagi tergantung di tempat yang paling mudah dilihat mata. Tepat saat kau sudah kembali berdiri santai satu langkah di samping, Koita berjalan balik."
            koita "Nah, sudah beres—eh? Tunggu sebentar."
            nar "Langkahnya langsung terhenti di depan dahan tengah. Senyum santainya lenyap dalam sedetik saat matanya mendapati kertas hijau yang bukan miliknya."
            koita "Tadi jelas-jelas aku menggantungnya di dahan ini... ke mana, ya? ...Ah, ketemu."
            nar "Ia membungkuk agak rendah menyibak daun bambu di dahan bawah, menatap tulisan tangannya sendiri selama dua detik penuh dengan kening berkerut tipis."
            nar "Ia sama sekali tidak menuduhmu ataupun bertanya apakah angin yang menerbangkannya. Tanpa suara, ia melepas kembali kertas biru mudanya dan memindahkannya lagi ke dahan tengah dengan simpul yang jauh lebih rapat."
            koita "...Aneh, padahal tadi perasaan sudah kuikat di atas sini."
            nar "Selesai mengikatnya, mata Koita menyapu seluruh selasar Gedung Sastra—sekilas, tenang, namun jauh lebih waspada. Usikan sekecil itu rupanya sudah cukup membuatnya sadar bahwa ada sesuatu di sekitarnya yang tidak lagi diam di tempat."
        else:
            nar "Begitu Koita membelakangimu menuju meja panjang untuk mengembalikan spidol dan membuang sisa benang, tanganmu bergerak cepat tanpa menimbulkan suara."
            nar "Kau melepas simpul longgar kertas biru mudanya dari dahan tengah yang mencolok, lalu menukarnya dengan sebuah tanzaku hijau dari dahan paling bawah yang agak tertutup daun. Keinginannya tetap ada—hanya tidak lagi mudah terlihat oleh siapa pun yang lewat."
            nar "Tepat ketika kau kembali berdiri santai dengan tangan di saku celana, Koita melangkah balik."
            koita "Nah, beres—eh? Tunggu dulu."
            nar "Langkahnya langsung berhenti di depan dahan tengah. Senyum santainya lenyap dalam sedetik saat melihat kertas hijau yang bukan miliknya."
            koita "Tadi aku menggantungnya di sini... ke mana, ya? ...Ah, ketemu."
            nar "Ia membungkuk membaca tulisannya sendiri di dahan bawah selama dua detik dengan kening berkerut tipis. Tanpa bertanya kepadamu ataupun orang di sekitar, ia melepas kembali kertas biru mudanya lalu mengikatnya ulang di dahan tengah dengan simpul jauh lebih kencang."
            koita "...Aneh juga, perasaan tadi sudah kuikat rapi di sini."
            nar "Begitu selesai, tatapannya sempat menyapu selasar di sekeliling kalian dengan ketenangan yang sedikit berubah waspada. Usikan sekecil itu rupanya sudah cukup membuatnya mulai memeriksa sekitar."
    else:
        if kk_host == "chiasa":
            nar "Kau menatap kertas biru mudanya selama beberapa detik, lalu berjalan ke meja panjang di belakang kalian, mengambil selembar tanzaku putih kosong dan sebuah spidol hitam."
            nar "Di atas meja itu, kau menuliskan satu kalimat sederhana dengan huruf yang jelas: 'Kalau ada yang berubah, semoga kita berani membicarakannya.'"
            nar "Kau kembali ke dahan bambu dan mengikat kertas putih itu persis di sebelah kertas biru muda milik Koita, sehingga kedua tepi kertasnya hampir bersentuhan setiap kali angin bertiup."
            nar "Koita yang sejak tadi memperhatikanmu mendadak terdiam. Ia condong sedikit ke depan untuk membaca tulisanmu, senyum terlatih yang biasa menempel di wajahnya perlahan surut."
            koita "...Itu balasan buat aku, Chi-chan?"
            nar "Sebelum kau sempat menjawab ya atau tidak, ia membacanya sekali lagi dari awal sampai akhir. Untuk beberapa detik yang hening di tengah selasar, ekspresinya tampak jauh lebih rapuh dan jujur daripada biasanya."
            koita "Aku... biasanya selalu menganggap kalau semua orang diam, berarti semuanya masih baik-baik saja. Nggak ada yang marah, nggak ada yang pergi."
            chiasa "Diam nggak selalu berarti baik-baik saja, Ko-nii."
            koita "Iya, ya... mungkin selama ini cuma aku saja yang nggak pernah berani bertanya."
            nar "Ia mengembuskan napas pelan sambil menatap dua lembar kertas yang tergantung berdampingan itu. Kalian berdiri di bawah dua keinginan yang sama sekali tidak menjanjikan hal yang sama—dan kali ini, Koita tidak mencoba menyentuh atau memindahkan salah satunya."
        else:
            nar "Kau memandangi kertas biru mudanya sejenak, lalu melangkah ke meja panjang di belakang kalian untuk mengambil selembar tanzaku putih kosong dan spidol hitam."
            nar "Tanpa bertele-tele, kau menuliskan satu kalimat lugas dengan huruf yang jelas: 'Kalau ada yang berubah, semoga kita berani membicarakannya.'"
            nar "Kau kembali ke dahan bambu dan mengikat kertas putih itu persis di sebelah kertas biru muda milik Koita. Begitu selesai, Koita yang sejak tadi memperhatikan gerakanmu langsung condong sedikit membaca tulisan itu. Senyum santai yang biasa terpasang di wajahnya perlahan surut."
            koita "...Itu balasan buat aku, Yutaka?"
            nar "Sebelum kau sempat mengiyakan, ia membacanya sekali lagi dari awal sampai akhir. Untuk beberapa detik yang sunyi di tengah selasar, seluruh sikap ringan yang biasa ia pakai menutupi diri tampak luruh."
            koita "Aku biasanya selalu menganggap diam itu berarti semuanya masih baik-baik saja. Nggak ada yang berubah, nggak ada yang pergi."
            yutaka "Diam nggak pernah otomatis berarti aman, Koita."
            koita "...Iya, ya. Padahal mungkin selama ini cuma aku saja yang nggak pernah berani bertanya."
            nar "Ia menghela napas pelan sambil menatap dua lembar kertas yang tergantung berdampingan itu. Kalian berdiri di bawah dua keinginan yang sama sekali tidak menjanjikan hal yang sama—dan Koita tidak memindahkan salah satunya."
    return

# ┌─ PANDUAN CERITA · K06 · Foto Reuni
# │ LOKASI  : Kampus Kouseikan · Kafe Komorebi
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : Koita meminta foto kelompok; ia berdiri di tengah.
# │ INTI    : A ambil foto / B ikut berfoto dan geser posisi / C ganti fotografer.
# │ AKHIRAN : foto menjadi bukti digital () tentang siapa dekat siapa.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K06:
    call kk_scene_enter("koita", "Kafe Komorebi")
    nar "Cangkir di Komorebi sudah dikumpulkan, tetapi tak seorang pun ingin menjadi yang pertama mengatakan pulang. Koita mengambil ponselnya."
    koita "Foto dulu, yuk. Sudah lama nggak lengkap begini."
    nar "Ia berdiri di tengah tanpa perlu diminta. Nagisa bergerak ke satu sisinya; Miyuki ragu sepersekian detik di sisi lain. Harumi mundur agar tidak menutupi papan menu, lalu nyaris keluar bingkai."
    koita "Harumi, dekat sedikit. Nggak usah sejauh itu."
    nar "Ia mengucapkannya sambil menoleh kepada Miyuki, memastikan sang senpai masih tersenyum."
    call kk_family_menu("K06", ["Ambilkan fotonya dari luar bingkai.", "Ikut berfoto dan geser posisimu.", "Minta orang lain yang memotret."])
    if _return == "A":
        nar "Kau mundur sampai semua masuk layar. Hitungan ketiga menangkap tangan yang hampir menyentuh, bahu yang menegang, dan senyum yang tiba tepat pada waktunya."
        koita "Kirim ke grup, ya. Jangan pilih yang aku merem."
        nar "Kau menyimpan foto aslinya. Di layar, jarak beberapa sentimeter terlihat remeh. Kau ingat siapa yang bersusah payah mempertahankannya."
    elif _return == "B":
        nar "Kau meminta ruang di tengah dan menyelipkan diri ke dalam kelompok. Koita bergeser, membuat seluruh susunan ikut berubah."
        nagisa "Eh, tunggu. Kalau begitu tasku keinjak."
        koita "Kita geser semua saja. Pelan-pelan."
        nar "Foto akhirnya lebih berantakan dan lebih hidup. Saat memeriksa hasilnya, Koita memperbesar gambar sekali, melihat tempatmu berdiri, lalu mengecilkannya lagi."
    else:
        nar "Kau meminta bantuan pelayan dan bergabung di ujung. Ia mengarahkan semua orang merapat; kini posisi kalian ditentukan oleh orang yang hanya ingin segera selesai memotret."
        koita "Satu lagi, boleh? Yang tadi kayaknya aku belum siap."
        nar "Pada foto kedua ia sudah tersenyum. Ketika kedua gambar masuk grup, orang-orang memilih versi yang berbeda sebagai favorit."
    return

# ┌─ PANDUAN CERITA · K09 · Omikuji Koita
# │ LOKASI  : Alam & Pantai · Kuil
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : kuil; ia menarik ramalan "pilihanmu akan datang".
# │ INTI    : A tanyakan / B tertawakan / C ancam.
# │ AKHIRAN : mulai tumbuh rasa takut; kunci K15.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K09:
    call kk_scene_enter("koita", "Kuil · Tahun Baru")
    nar "Jari Koita kedinginan ketika membuka omikuji. Ia membacakan bagian studi dan kesehatan dengan nada pembawa acara, lalu berhenti pada bagian hubungan."
    koita "Pilihanmu akan datang. Jangan mengira diam menghentikan waktu."
    nar "Ia membalik kertas, mencari kelanjutan yang bisa membuat kalimat itu terdengar lucu. Bagian belakang kosong."
    koita "Agak galak untuk ramalan Tahun Baru, ya. Aku bahkan belum merasa harus memilih."
    call kk_family_menu("K09", ["Tanyakan pilihan apa yang ia maksud.", "Tertawakan ramalan yang samar itu.", "Katakan ia tak perlu memikirkannya."])
    if _return == "A":
        koita "Entah. Itu masalahnya. Begitu dibaca, aku langsung kepikiran beberapa orang. Kalau benar-benar nggak ada pilihan, harusnya aku nggak kepikiran siapa-siapa, kan?"
        nar "Ia menghangatkan jari dengan napas, tetapi kertas itu tetap terbuka."
        koita "Aku takut salah memilih. Tapi mungkin selama ini orang lain yang menanggung ketakutanku."
    elif _return == "B":
        nar "Kau tertawa dan mengatakan kalimat itu bisa berlaku untuk memilih makan siang. Koita ikut tertawa, kali ini sedikit terlambat."
        koita "Benar. Kalau begitu aku pilih mi. Selesai, takdir sudah dipenuhi."
        nar "Ia melipat kertas dengan rapi, jauh lebih rapi daripada leluconnya memerlukan. Ketika kalian turun dari kuil, ia masih meraba saku tempat menyimpannya."
    else:
        nar "Kau mengatakan ia tak perlu membiarkan selembar ramalan mengatur hidupnya. Koita mengangguk cepat."
        koita "Iya. Aku nggak perlu memikirkannya sekarang."
        nar "Penekanan pada sekarang terdengar seperti batas waktu yang baru ia tetapkan sendiri. Ia menyimpan kertas itu, tidak mengikatnya pada tempat ramalan buruk."
    return

# ┌─ PANDUAN CERITA · K10 · Coklat yang Tidak Habis
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : Valentine; Koita menerima banyak coklat.
# │ INTI    : A pemain memberi coklat / B amati siapa yang tidak memberi / C bantu menghabiskan.
# │ AKHIRAN : gerbang BL/Koita Success. Male: A membuka rantai BL. Female: A membuka jalur Chiasa × Koita.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K10:
    call kk_scene_enter("koita", "Gedung Sastra · Valentine")
    nar "Pita merah, stiker toko, kotak kecil yang sudutnya penyok karena dibawa di dalam tas. Hadiah Valentine menutupi separuh meja Koita. Ia memindahkan semuanya dengan hati-hati agar tak terlihat sedang menyusun peringkat."
    koita "Aku harus ingat yang mana dari siapa. Tahun lalu salah mengucapkan terima kasih, malu sekali."
    nar "Ia tersenyum, tetapi sesekali matanya mencari pintu. Jumlah di meja ternyata belum cukup menjawab siapa yang masih akan datang."
    call kk_family_menu("K10", ["Beri ia satu coklat darimu juga.", "Amati siapa yang justru tidak memberi.", "Bantu ia menghabiskan yang menumpuk."])
    if _return == "A":
        nar "Kau meletakkan hadiahmu di depannya. Koita baru mengulurkan tangan ketika kau menyebut bahwa ini memang untuknya."
        koita "Dari kamu juga? Aku nggak tahu kamu... menyiapkan."
        nar "Ia hampir menyebutnya kejutan dari teman, lalu berhenti sebelum kata terakhir keluar."
        koita "Boleh kubuka nanti? Sendiri. Aku mau membacanya tanpa orang lain melihat dulu."
        nar "Hadiahmu ia taruh di dalam tas, terpisah dari tumpukan meja. Itu belum sebuah jawaban, tetapi kali ini ia tidak buru-buru mengubah pertanyaannya."
    elif _return == "B":
        nar "Kau mengamati orang yang melambai lalu lewat, orang yang memilih pintu lain, dan orang yang membawa bingkisan tetapi menyimpannya lagi. Tidak semua ketidakhadiran berarti hal yang sama."
        koita "Kamu lihat seseorang di luar?"
        nar "Ia berusaha bertanya ringan. Kau mulai mengenali bahwa bagian terpenting dari mejanya justru tempat kosong yang hanya ia lihat sendiri."
    else:
        nar "Koita memisahkan kotak yang boleh dibagi dari kotak dengan pesan pribadi. Kali ini kau menunggu ia yang membukanya sebelum mengambil."
        koita "Yang ini banyak. Katanya memang buat ramai-ramai."
        nar "Kalian makan sambil membicarakan kuliah. Setelah beberapa menit, ia berhenti menghadap pintu."
        koita "Aku suka begini. Nggak perlu menebak apa artinya."
        nar "Ia mengucapkannya dengan lega yang membuat tumpukan hadiah di antara kalian terasa sedikit lebih berat."
    return

# ┌─ PANDUAN CERITA · K11 · Hadiah yang Sama
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : White Day; Koita membalas semua dengan hadiah yang sama.
# │ INTI    : A kritik / B bantu ganti / C biarkan.
# │ AKHIRAN : heroine sadar mereka "disamakan"; menaikkan kecurigaan antar heroine.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K11:
    call kk_scene_enter("koita", "Gedung Sastra · White Day")
    nar "Koita mengeluarkan kantong-kantong White Day dari tas belanja. Semua berpita sama. Semua berisi biskuit yang sama, bahkan kartu kecilnya memiliki kalimat cetak yang sama."
    koita "Kupikir kalau ada yang lebih mahal, nanti malah nggak enak. Jadi kubuat adil."
    nar "Ia mengatakannya sebelum ada yang bertanya. Di dekat pintu, dua penerima membandingkan kantong mereka, lalu berhenti tersenyum pada saat yang hampir bersamaan."
    call kk_family_menu("K11", ["Kritik bahwa menyamakan semua orang itu ceroboh.", "Bantu ia mengganti beberapa dengan yang berbeda.", "Biarkan saja."])
    if _return == "A":
        nar "Kau mengingatkan bahwa sebagian hadiah sebelumnya adalah pengakuan, bukan kewajiban bertukar makanan. Balasan seragam membiarkan semua pertanyaan itu tetap terbuka."
        koita "Kalau kubedakan, mereka tahu aku..."
        nar "Ia berhenti. Kalimat yang tak diselesaikannya menjelaskan lebih banyak daripada pembelaan tentang keadilan."
        koita "Aku takut ada yang sedih. Tapi aku juga takut ada yang berhenti memberiku hadiah. Itu jelek, ya."
    elif _return == "B":
        nar "Kau membantu memisahkan beberapa kantong dan menyarankan tambahan yang sesuai dengan penerimanya. Koita menyambut bantuan itu dengan lega."
        koita "Yang ini dia suka. Aku ingat. Terus yang ini... iya, lebih cocok."
        nar "Hadiahnya kini tampak lebih pribadi. Pertanyaan tentang apa yang sebenarnya ia balas belum terjawab, hanya mendapatkan bungkus yang lebih meyakinkan."
        nar "Ketika ia berterima kasih, kau menyadari betapa mudah perhatian yang cermat dipakai untuk menunda kejujuran."
    else:
        nar "Kau membiarkannya membagikan seluruh kantong. Ucapan terima kasih tetap terdengar sopan, tetapi tidak semua penerima menunggu untuk berbicara lebih lama."
        koita "Mereka nggak suka biskuitnya, ya?"
        nar "Dari seberang ruangan terdengar kalimat pelan: oh, kamu juga dapat yang ini. Koita mendengarnya. Ia menunduk merapikan tas belanja yang sudah kosong."
    return

init 1 python:
    def kk_koita_fear(delta):
        pts.setdefault("ketakutan_koita",0)
        kk_adj("ketakutan_koita",delta)
    def kk_koita_suspect(delta):
        pts.setdefault("koita_curiga_1",0)
        kk_adj("koita_curiga_1",delta)

    _hook("K01-A", lambda: kk_flag("pola_koita_dikenal"))
    _hook("K01-B", lambda: kk_koita_suspect(5))
    _hook("K03-A", lambda: kk_koita_fear(5))
    _hook("K03-C", lambda: (kk_flag("koita_merasa_dilihat"), kk_koita_fear(3)))
    _hook("K06-A", lambda: kk_flag("foto_bukti_koita"))
    _hook("K09-A", lambda: kk_koita_fear(8))
    _hook("K09-B", lambda: kk_koita_fear(3))
    _hook("K10-A", lambda: kk_rel("koita","aff",2))
    _hook("K10-B", lambda: kk_flag("pola_koita_dikenal"))
    _hook("K11-A", lambda: kk_koita_suspect(8))
    _hook("K11-C", lambda: kk_koita_suspect(10))
