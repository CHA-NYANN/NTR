# Yutaka host, menjaga penyamaran (Y02, Y05, Y10). Pemain menghuni tubuh Yutaka;
# tingkah yang meleset dari Yutaka asli menaikkan kecurigaan. Event host (fire saat masuk lokasi).
# Variabel curiga_* mengikuti Event_Yutaka; angka adalah setelan prototipe.
init 1 python:
    def kk_suspect(who, delta):
        key = "curiga_" + who
        pts.setdefault(key, 0)
        kk_adj(key, delta)

# ┌─ PANDUAN CERITA · Y02 · Kunci yang Tidak Ada
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : kunjungan pertama ke rumah Amamiya.
# │ INTI    : A bunyikan bel dan sopan / B masuk seolah rumah sendiri / C mengabari dulu.
# │ AKHIRAN : B memicu curiga Chiasa/Koita (Yutaka asli tidak punya kunci cadangan ).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y02:
    call kk_scene_enter("yutaka", "Rumah Amamiya")
    nar "Sore hari di kawasan hunian biasa itu membawa cahaya jingga lembut yang menyapu deretan genteng rumah dan pagar kayu rendah di sepanjang gang. Di depan sebuah rumah dua lantai yang tampak hangat dan terawat dengan papan nama keramik bertuliskan 'Amamiya' di samping kotak surat, langkah kakimu berhenti dengan sendirinya."
    nar "Ada kejanggalan aneh yang merambat di dadamu. Tubuh Kisaragi Yutaka mengenali belokan gang dan jarak menuju rumah ini tanpa perlu kau membuka peta di ponsel, seolah kakinya sudah ratusan kali menapakinya—sementara dirimu di dalam kepala ini tidak memiliki satu pun ingatan tentang tempat ini."
    nar "Dari obrolan di ponsel Yutaka dan potongan awal cerita yang sempat kaubaca, kau hanya tahu Yutaka cukup sering mampir dan makan di sini. Namun tidak ada satu pun petunjuk apakah ia biasa langsung masuk tanpa kabar, atau tetap mengetuk dan menunggu seperti tamu."
    nar "Dari balik jendela lantai satu yang sedikit terbuka, terdengar samar suara televisi, aroma kuah kari hangat yang mengepul dari dapur, serta suara tawa ringan Koita disusul sahutan cepat Chiasa."
    nar "Kehangatan rumah tangga yang dari luar tampak begitu sederhana itu mendadak terasa seperti ruangan kaca yang rapuh—seolah satu langkah salah di ambang pintu saja sudah cukup untuk merusaknya dan membuat orang di dalam sadar bahwa sosok yang berdiri di teras mereka bukan lagi sahabat yang mereka kenal."
    call kk_family_menu("Y02", ["Bunyikan bel dan bersikap sopan.", "Masuk saja seolah rumah sendiri.", "Kabari dulu sebelum datang."])
    if _return == "A":
        nar "Kau menarik napas pelan, memutuskan untuk mengikuti tata krama bertamu paling aman daripada menebak-nebak kebiasaan pemilik tubuh ini. Kau mendorong pagar kayu yang tidak dikunci, melangkah melintasi teras batu, lalu menekan tombol bel di samping kusen pintu masuk."
        nar "Suara denting lembut terdengar dari dalam rumah. Beberapa detik kemudian, suara langkah sandal mendekat ke lorong depan, kunci selot diputar, dan daun pintu kayu itu terbuka."
        nar "Amamiya Chiasa berdiri di ambang pintu mengenakan pakaian rumah santai. Rambut cokelat gelapnya terikat setengah dengan pita hitam, dan sepasang mata kuning keemasannya mengerjap sesaat melihat sosokmu sebelum bibirnya melengkung tipis."
        chiasa "Oh, Yutaka-kun? Tumben sekali pakai pencet bel segala—biasanya kalau pagarnya nggak dikunci langsung ketuk pintu depan sambil teriak dari luar. Kau sudah makan belum?"
        yutaka "Belum. Kebetulan lewat sekitar sini, jadi mampir sebentar. Tidak mengganggu, kan?"
        chiasa "Mana mungkin mengganggu. Ayo masuk, Ko-nii lagi di dapur nyiapin makan malam."
        nar "Kau mengikuti kebiasaan bertamu yang wajar: menunggu Chiasa bergeser sedikit memberi jalan, mengucapkan salam singkat, lalu melepas sepatumu dan menatanya rapi menghadap pintu di atas lantai genkan sebelum mengenakan sandal tamu yang ia sodorkan."
        nar "Dari arah ruang makan di dalam, suara Koita terdengar ceria tanpa perlu menoleh penuh dari depan kompor."
        koita "Eh, Yutaka ya? Pas banget, aku masak kari agak banyak hari ini! Ambil gelas sendiri di rak atas seperti biasa ya, tanganku masih pegang sendok sayur!"
        yutaka "Iya, terima kasih, Koita."
        nar "Kau melangkah masuk ke ruang tamu yang hangat dan sedikit penuh oleh majalah serta buku sketsa di sudut meja, lalu berdiri sejenak menatap lemari dapur mencari rak gelas yang dimaksud. Penerimaan yang begitu ringan dan tanpa curiga itu terasa wajar bagi mereka, tetapi justru terasa nyaris menyakitkan di dadamu—kau baru saja dipersilakan melangkah masuk ke dalam kehidupan hangat seorang sahabat yang pemilik aslinya sudah tiada."
    elif _return == "B":
        nar "Kau menduga sahabat sejak kecil yang hampir setiap minggu makan di sini pasti sudah terbiasa langsung masuk tanpa banyak basa-basi. Kau membuka pagar kayu, melangkah naik ke teras, lalu langsung meraih gagang pintu depan dan menekannya ke bawah seolah memiliki hak penuh untuk membukanya."
        nar "Gagang pintu berbunyi klik keras—namun daun pintu itu terkunci rapat dari dalam. Gerakan tanganmu yang terlalu percaya diri membentur kayu yang sama sekali tidak bergeming."
        nar "Tepat ketika kau masih memegangi gagang pintu dengan kening berkerut, kunci selot di balik pintu berputar cepat dan daun pintu terbuka ke dalam."
        nar "Amamiya Chiasa berdiri tepat di hadapanmu. Langkahnya terhenti mendadak begitu mata kuning keemasannya menangkap posisi tanganmu yang masih menggantung di gagang pintu, lalu naik perlahan menatap wajahmu dengan sorot tajam yang langsung mendinginkan udara sore."
        chiasa "...Yutaka-kun? Kau barusan mau langsung buka pintu masuk tanpa pencet bel atau mengetuk dulu?"
        nar "Kau refleks menarik tanganmu turun ke sisi jaket. Tidak ada kunci cadangan di sakumu—karena Yutaka asli memang tidak pernah punya kunci rumah ini—dan tidak ada ingatan masa lalu yang bisa menyelamatkan jawabanmu sekarang."
        yutaka "A-ah... kupikir tadi pintunya nggak dikunci. Aku dengar suara kalian dari dalam, jadi..."
        chiasa "Kalaupun nggak dikunci, sejak kapan kau masuk ke rumah ini tanpa mengetuk atau memanggil dari luar dulu? Kau kan bukan penghuni rumah ini."
        nar "Nada suara Chiasa tidak meninggi sedikit pun, tetapi justru ketenangannya yang membuat tengkukmu terasa dingin. Matanya bertahan menatap wajahmu selama dua detik penuh, seolah sedang mencoba membaca apa yang terasa janggal dari sikapmu."
        nar "Sebelum keheningan itu semakin menekan, suara Koita terdengar menyela dari lorong ruang makan sambil berjalan mendekat membawa lap tangan."
        koita "Lho, ada apa, Chi-chan? Oh, Yutaka! Ayo masuk, jangan berdiri terus di luar—angin sore mulai dingin. Kebetulan aku baru selesai masak kari."
        yutaka "Iya... maaf sudah bikin kaget, Chiasa."
        nar "Chiasa akhirnya menggeser tubuhnya setengah langkah untuk memberimu jalan. Namun ketika kau melangkah melewati ambang pintu untuk melepas sepatu di genkan, tatapan mata keemasan Chiasa yang mengikutimu dari samping sama sekali belum kembali hangat."
    else:
        nar "Kau memilih berhenti dua langkah sebelum pagar kayu. Daripada menebak-nebak kebiasaan pemilik tubuh ini dan mengambil risiko salah langkah di depan pintu, kau mengeluarkan ponsel dari saku jaket dan membuka ruang obrolan dengan Koita."
        nar "Kau mengetik pesan singkat menanyakan apakah mereka sedang di rumah dan apakah kau boleh mampir sebentar, lalu menekan kirim."
        play sound "audio/sfx/phone_buzz.wav"
        nar "Tidak sampai setengah menit, ponsel di tanganmu bergetar ringan. Balasan Koita masuk dengan nada santai yang terasa begitu alami—ia bilang mereka sedang di rumah menyiapkan makan malam, lalu tanpa sungkan langsung menitip dibelikan sebotol besar teh oolong dingin di minimarket ujung gang, lengkap dengan janji mengganti uangnya begitu kau sampai."
        nar "Melihat permintaan sederhana itu, bahumu yang sejak tadi menegang perlahan turun. Tidak ada yang luar biasa dari kedatanganmu bagi mereka."
        nar "Kau berbalik sejenak ke minimarket di ujung jalan untuk membeli botol teh oolong dingin dan sekotak kecil camilan, lalu berjalan kembali ke Rumah Amamiya dan menekan bel pintu."
        nar "Begitu pintu kayu terbuka, Amamiya Chiasa sudah berdiri di ambang pintu dengan senyum tipis seolah memang sudah menunggu kedatanganmu. Ia langsung mengulurkan kedua tangannya mengambil kantong plastik belanjaan dari tanganmu."
        chiasa "Pas banget, Ko-nii baru saja mematikan kompor. Wah, beli tehnya yang dingin lagi—makasih ya, Yutaka-kun. Ayo masuk, sepatumu taruh di sebelah kiri saja."
        yutaka "Sama-sama. Maaf mendadak mampir sore-sore."
        chiasa "Tumben sekali pakai acara minta maaf segala. Masuk gih, nanti karinya keburu dingin."
        nar "Dari dalam ruang makan, Koita melambai sambil menata piring dan memanggilmu masuk. Saat kau melepas sepatu di genkan yang terang dan hangat itu, kepastian kecil tentang kapan orang mengharapkan kedatanganmu memberi rasa lega yang aneh—kehangatan sederhana yang tidak pernah bisa dibeli oleh apartemen mewahmu yang sunyi di distrik elite."
    return

# ┌─ PANDUAN CERITA · Y05 · Turnamen Game: Skill yang Hilang
# │ LOKASI  : Distrik Elite · Apartemen Yutaka
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Nagisa menantang main game; Yutaka asli pro, pemain tidak.
# │ INTI    : A pura-pura mengalah / B kalah terang-terangan / C latihan dulu.
# │ AKHIRAN : B memicu curiga ("Yutaka tidak pernah kalah").
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y05:
    call kk_scene_enter("yutaka", "Apartemen Yutaka")
    nar "Nagisa memilih permainan yang sudah tersimpan di konsolmu. Ia bicara sambil memasang pengaturan, percaya bahwa kau hafal lebih banyak daripada dirinya. Nama akun Yutaka tampak di antara catatan skor. Jari-jarimu mengenali cara memegang pengendali, tetapi keputusan cepat yang membuatnya hebat tidak ikut diwariskan."
    call kk_family_menu("Y05", ["Pura-pura mengalah agar terlihat wajar.", "Kalah terang-terangan saja.", "Minta waktu latihan dulu."])
    if _return == "A":
        nagisa "Kau mengalah, ya? Aku ingin menang, tapi bukan menang yang dibungkus kado begini. ...Sudah, ronde berikutnya jangan terlalu sibuk menjaga perasaanku."
    elif _return == "B":
        nagisa "Tunggu. Itu bukan salah tekan biasa. Kau kelihatan tidak tahu harus melakukan apa. Aku tidak sedang mengejek, Yuu-kun. Akhir-akhir ini ada apa?"
    else:
        nagisa "Minta latihan dulu? Biasanya kau yang menyuruhku pemanasan. ...Ya sudah. Aku mau tanding sama orang yang siap main, bukan orang yang panik menjaga reputasi."
    return

# ┌─ PANDUAN CERITA · Y10 · Jam Tangan Hadiah
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Yutaka menerima jam tangan dari Daisuke seperti tahun lalu.
# │ INTI    : A simpan / B pakai / C kembalikan.
# │ AKHIRAN : Daisuke menilai sikap.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y10:
    call kk_scene_enter("yutaka", "Rumah Amamiya")
    nar "Daisuke menyerahkan kotak jam tipis. Ia menyebut jam tahun lalu dan tertawa tentang betapa sering Yutaka memakainya. Kau baru memahami bahwa benda itu bukan hadiah mahal dari relasi keluarga; seseorang di rumah ini memperhatikan apa yang melekat di pergelangan seorang anak yang bukan anaknya."
    call kk_family_menu("Y10", ["Simpan dengan hati-hati dan berterima kasih.", "Pakai langsung di pergelanganmu.", "Kembalikan karena merasa terlalu berharga."])
    if _return == "A":
        nar "Kau mengucapkan terima kasih dan menyimpan kotaknya dengan hati-hati. Daisuke mengatakan hadiah itu untuk dipakai sesukamu, bukan untuk dipajang demi menyenangkan pemberi. Kau mengangguk, malu karena sempat menganggap percakapan ini sekadar ujian yang harus dilalui."
    elif _return == "B":
        nar "Kau memakainya, lalu mengangkat pergelangan untuk menunjukkan hasilnya. Daisuke tersenyum dan membetulkan letak kotak kosong di meja. Untuk sesaat ia tidak memeriksa apa pun tentang dirimu. Ia hanya tampak senang hadiah yang dipilihnya disukai."
    else:
        nar "Kau mengembalikan kotak itu karena merasa tak berhak menerima sesuatu seberharga ini. Daisuke menerimanya perlahan. Ia tidak tersinggung oleh kesopananmu, tetapi bertanya apakah ada yang membuatmu tidak nyaman di rumah mereka. Chiasa memandangmu, terkejut oleh jarak yang baru saja kauciptakan."
    return

init 1 python:
    _hook("Y02-A", lambda: kk_suspect("chiasa", -3))
    _hook("Y02-B", lambda: kk_suspect("chiasa", 10))
    _hook("Y05-A", lambda: kk_rel("nagisa","trust",2))
    _hook("Y05-B", lambda: kk_suspect("nagisa", 12))
    _hook("Y10-A", lambda: kk_flag("daisuke_setuju"))
    _hook("Y10-B", lambda: kk_flag("daisuke_setuju"))
    _hook("Y10-C", lambda: kk_suspect("chiasa", 5))
