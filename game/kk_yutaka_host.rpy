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
    nar "Menyusuri kawasan hunian biasa yang tenang ini terasa seperti berjalan di atas peta yang tergambar di balik kulitmu sendiri. Kamu melewati mesin penjual minuman di tikungan jalan, pagar tanaman yang baru dipangkas, dan papan pengumuman warga, hingga akhirnya langkah kakimu berhenti dengan sendirinya tepat di depan sebuah rumah dua lantai yang hangat dan terawat dengan papan nama keramik bertuliskan 'Amamiya' di samping kotak surat."
    nar "Ada kejanggalan aneh yang merambat pelan di dadamu. Tubuh Kisaragi Yutaka mengenali setiap belokan gang dan jarak menuju rumah ini tanpa perlu kamu membuka peta di ponsel, seolah tungkai panjangnya sudah ratusan kali menapakinya, sementara dirimu di dalam kepala ini tidak memiliki satu pun ingatan tentang tempat ini."
    nar "Kamu sempat memeriksa riwayat obrolan di ponsel Yutaka sebelum keluar dari apartemen. Dari potongan pesan lama dan awal manga yang sempat kamu baca, kamu hanya tahu Yutaka sangat sering mampir dan ikut makan di sini. Tidak ada satu pun petunjuk apakah ia biasa langsung membuka pintu tanpa kabar, mengetuk dulu dari teras, atau mengirim pesan sebelum datang."
    nar "Dari balik jendela lantai satu yang sedikit terbuka di balik tirai tipis, terdengar samar suara televisi, aroma kuah kari hangat yang kaya bawang bombai dan rempah mengepul keluar dari dapur, lalu suara percakapan ringan yang terdengar akrab."
    chiasa "Ko-nii, apinya jangan kebesaran, nanti bagian bawah pancinya lengket lagi kayak bulan lalu!"
    koita "Haha, iya, iya, ini juga lagi diaduk terus kok! Kamu tolong siapkan acar lobaknya di mangkuk kecil saja, Chi-chan."
    chiasa "Sudah kusiapkan dari tadi. Tinggal tunggu karinya mengental saja. Oh ya, wortelnya sudah empuk belum?"
    koita "Coba kucicip dulu sedikit... nah, sudah pas empuknya. Sebentar lagi bisa dimatikan kompornya."
    nar "Kamu berdiri diam di depan pagar kayu rendah, mendengarkan bunyi sendok sayur menyentuh tepi panci dari dalam rumah. Kehangatan rumah tangga yang begitu sederhana itu terasa sangat jauh berbeda dari apartemen mewahmu yang selalu sunyi, sekaligus terasa seperti ruangan kaca yang rapuh."
    nar "Satu langkah salah di ambang pintu saja sudah cukup untuk membuat kedua orang di dalam sana sadar bahwa sosok yang berdiri di teras mereka bukan lagi sahabat lama yang mereka kenal."
    call kk_family_menu("Y02", ["Bunyikan bel dan bersikap sopan.", "Masuk saja seolah rumah sendiri.", "Kabari dulu sebelum datang."])
    if _return == "A":
        nar "Kamu menarik napas pelan, memutuskan untuk mengikuti tata krama bertamu paling aman daripada menebak-nebak kebiasaan pemilik tubuh ini. Kamu mendorong pagar kayu yang tidak dikunci, melangkah melintasi teras batu, lalu menekan tombol bel di samping kusen pintu masuk."
        nar "Suara denting lembut terdengar dari dalam rumah. Beberapa detik kemudian, suara langkah sandal mendekat ke lorong depan, kunci selot diputar dari dalam, dan daun pintu kayu itu terbuka."
        nar "Amamiya Chiasa berdiri di ambang pintu mengenakan kaus rumahan lengan panjang dan rok santai. Rambut cokelat gelapnya terikat setengah dengan pita hitam, dan sepasang mata kuning keemasannya mengerjap sesaat melihat sosokmu sebelum sudut bibirnya melengkung tipis."
        chiasa "Oh, Yutaka-kun? Tumben sekali pakai pencet bel segala. Biasanya kalau pagarnya nggak dikunci kamu langsung ketuk pintu depan sambil manggil-manggil dari luar."
        yutaka "Tadi dengar kalian lagi sibuk di dapur, takutnya nggak kedengaran kalau cuma diketuk pelan."
        chiasa "Bisa aja alasannya. Kamu sudah makan belum? Jangan bilang dari tadi cuma minum kopi doang di apartemen."
        yutaka "Belum sempat makan, kebetulan lewat sekitar sini jadi mampir sebentar. Nggak mengganggu, kan?"
        chiasa "Mana mungkin mengganggu. Ayo masuk, Ko-nii lagi di dapur nyiapin kari, porsinya kayaknya cukup buat satu blok."
        nar "Kamu mengikuti kebiasaan bertamu yang wajar dengan menunggu Chiasa bergeser sedikit memberi jalan, mengucapkan salam singkat, lalu melepas sepatumu dan menatanya rapi menghadap pintu di atas lantai genkan sebelum mengenakan sandal tamu yang ia sodorkan."
        nar "Begitu kamu melangkah mengikuti Chiasa ke ruang makan yang hangat, ruang tamu di sebelahnya tampak hidup oleh tumpukan majalah, bantal duduk, dan beberapa buku sketsa di sudut meja rendah. Dari arah kompor, suara Koita terdengar ceria tanpa perlu menoleh penuh."
        koita "Eh, Yutaka ya? Pas sekali, aku masak kari agak banyak hari ini! Ambil gelas sendiri di rak atas sebelah kiri seperti biasa ya, tanganku masih pegang sendok sayur!"
        nar "Kamu menangkap petunjuk kecil itu dengan cepat. Tanpa tampak ragu, kamu berjalan ke lemari dapur sebelah kiri, membuka pintunya, lalu mengambil tiga gelas kaca dan sebotol air teh dingin dari meja dapur."
        yutaka "Iya, terima kasih, Koita. Sini sekalian kubantu bawa piring sama sendoknya ke meja."
        nar "Chiasa yang baru saja menaruh mangkuk kecil acar merah di atas meja makan menoleh ke arahmu dengan sebelah alis terangkat jahil."
        chiasa "Wah, tumben rajin banget hari ini, Yutaka-kun. Biasanya baru masuk genkan langsung meluncur duduk manis di depan televisi sambil nunggu dipanggil makan."
        yutaka "Sekali-sekali bantu tuan rumah kan nggak ada salahnya. Lagipula aku kan datang menumpang makan."
        koita "Haha, biarkan saja, Chi-chan. Kalau Yutaka lagi rajin begini kan tugasku berkurang. Gimana minggu awal kuliahmu, Yutaka? Tadi pagi Nagisa sempat mengeluh panjang lebar di grup soal dosennya."
        yutaka "Lumayan padat. Materi semester ini langsung ngebut dari hari pertama, jadi lumayan bikin kepala panas."
        chiasa "Kalau begitu makan yang banyak biar nggak makin pusing. Ini punyamu, kuahnya kuberi agak banyak seperti biasa."
        nar "Chiasa menggeser sepiring nasi hangat bersiram kuah kari kental dengan potongan kentang dan wortel ke hadapanmu. Koita segera mematikan kompor, melepas celemeknya, lalu ikut duduk di seberang meja sambil menuangkan air teh dingin dari botol yang kamu bawa."
        koita "Eh, ngomong-ngomong, kemarin aku coba campuran bubuk kari baru yang disarankan di minimarket. Gimana rasanya, kepedasan nggak?"
        nar "Kamu menyendok suapan pertama nasi beserta kuah karinya. Hangat rempahnya langsung menyebar di lidah, gurih dan tidak terlalu tajam."
        yutaka "Enak kok, bumbunya lebih terasa daripada yang biasa. Pedasnya juga nggak berlebihan."
        koita "Nah, dengar tuh, Chi-chan! Tadi kamu sempat ragu gara-gara bau bawangnya terlalu tajam."
        chiasa "Habis tadi kamu sempat hampir lupa mengecilkan api kompor, Ko-nii. Untung aku langsung teriak dari ruang tengah. Ngomong-ngomong, Yutaka-kun, minggu ini kamu nggak terlalu sibuk urus panitia kampus?"
        yutaka "Belum terlalu ramai, paling baru rapat pembagian tugas awal saja."
        koita "Syukurlah kalau belum keteteran. Nanti kalau kamu malas masak atau bosan makan sendirian di apartemen, langsung mampir saja ke sini kayak biasa. Ibu juga sempat berpesan sebelum dinas supaya aku nggak membiarkanmu makan mi instan terus."
        yutaka "Iya, terima kasih, Koita. Nanti kubantu bereskan piringnya habis makan."
        chiasa "Beneran nih mau bantu cuci piring? Awas nanti cuma bilang doang terus kabur pulang."
        yutaka "Nggak kabur kok, tenang saja."
        nar "Tawa ringan mereka memenuhi ruang makan kecil yang hangat itu. Saat kamu menyendok kari bersama mereka dan sesekali menimpali obrolan ringan soal jadwal kampus, penerimaan yang begitu alami dan tanpa curiga membuat langkah pertamamu di rumah keluarga Amamiya berjalan mulus."
    elif _return == "B":
        nar "Kamu menduga sahabat sejak kecil yang hampir setiap minggu makan di sini pasti sudah terbiasa langsung masuk tanpa banyak basa-basi. Kamu membuka pagar kayu, melangkah naik ke teras, lalu langsung meraih gagang pintu depan dan menekannya ke bawah dengan mantap seolah memiliki hak penuh untuk membukanya."
        nar "Gagang pintu berbunyi klik keras, sementara daun pintu itu terkunci rapat dari dalam. Gerakan tanganmu yang terlalu percaya diri membentur kayu yang sama sekali tidak bergeming."
        nar "Tepat ketika kamu masih memegangi gagang pintu dengan kening berkerut, bunyi kunci selot di balik pintu berputar cepat dan daun pintu terbuka ke dalam."
        nar "Amamiya Chiasa berdiri tepat di hadapanmu. Langkahnya terhenti mendadak begitu mata kuning keemasannya menangkap posisi tanganmu yang masih menggantung di gagang pintu, lalu naik perlahan menatap wajahmu dengan sorot tajam."
        chiasa "...Yutaka-kun? Kamu barusan mau langsung buka pintu masuk tanpa pencet bel atau mengetuk dulu?"
        nar "Kamu refleks menarik tanganmu turun ke sisi jaket. Tidak ada kunci cadangan di sakumu, karena Yutaka asli memang tidak pernah punya kunci rumah ini, dan tidak ada ingatan masa lalu yang bisa menyelamatkan jawabanmu sekarang."
        yutaka "A-ah... kupikir tadi pintunya nggak dikunci. Aku dengar suara kalian dari dalam, jadi..."
        chiasa "Kalaupun nggak dikunci, sejak kapan kamu masuk ke rumah ini tanpa mengetuk atau memanggil dari luar dulu? Kamu kan bukan penghuni rumah ini, dan kamu juga nggak punya kunci di sini."
        nar "Nada suara Chiasa tidak meninggi sedikit pun, tetapi justru ketenangannya yang dingin itu membuat tengkukmu menegang. Matanya bertahan menatap wajahmu selama dua detik penuh, seolah sedang mencoba membaca apa yang terasa janggal dari sikapmu."
        yutaka "Iya, salahku. Tadi kepalaku lagi agak melamun di jalan."
        chiasa "Melamun sampai lupa caranya bertamu? Padahal selama ini kamu termasuk orang yang paling rapi soal sopan santun kalau masuk rumah orang, Yutaka-kun."
        nar "Sebelum keheningan di ambang pintu itu semakin menekan, suara Koita terdengar menyela dari lorong ruang makan sambil berjalan mendekat membawa lap tangan di bahunya."
        koita "Lho, ada apa, Chi-chan? Kok pintunya dibuka tapi nggak ada yang masuk... oh, Yutaka! Ayo masuk, jangan berdiri terus di luar, anginnya lumayan kencang. Kebetulan aku baru selesai masak kari."
        yutaka "Iya... maaf sudah bikin kaget tadi, Chiasa."
        chiasa "...Lain kali ketuk dulu kayak biasa, Yutaka-kun."
        nar "Chiasa akhirnya menggeser tubuhnya setengah langkah untuk memberimu jalan. Ketika kamu melangkah melewati ambang pintu untuk melepas sepatu di genkan, tatapan mata keemasan Chiasa masih mengikutimu dari samping."
        nar "Beberapa menit kemudian, kamu duduk di meja makan menghadapi sepiring kari hangat bersama mereka. Koita mencoba menjaga suasana tetap santai sambil menyendok nasi dan bercerita tentang jadwal kelas awalnya, sementara Chiasa duduk di seberangmu dengan punggung tegak, mengaduk tehnya pelan tanpa banyak tersenyum."
        koita "Kari hari ini lumayan enak kan, Yutaka? Tadi aku pakai campuran rempah baru. Kebetulan porsinya banyak, jadi makan saja yang kenyang."
        yutaka "Iya, enak kok, Koita. Makasih sudah dikasih makan."
        chiasa "Tadi kamu habis dari mana sih, Yutaka-kun, sampai bisa melamun begitu di depan pagar rumah kami?"
        nar "Suara Chiasa terdengar ringan di permukaan, tetapi kedua matanya menatap lurus ke arahmu tanpa berkedip sedikit pun."
        yutaka "Cuma habis jalan kaki dari arah kampus. Materi kuliah minggu ini lumayan banyak, jadi agak kelelahan."
        chiasa "Oh... dari kampus. Biasanya kalau kamu lagi kecapekan habis kuliah, kamu justru kirim pesan dulu nanya kami lagi di rumah atau nggak, biar nggak capek jalan sia-sia kalau rumahnya kosong."
        yutaka "Tadi ponselku keburu masuk saku jaket dan aku sekalian lewat gang sini."
        koita "Wah, pantas saja. Jangan terlalu diporsir, Yutaka, nanti tumbang lagi kayak waktu musim dingin kemarin. Kalau lagi pusing banget sama tugas, istirahat saja dulu di sini sebentar."
        chiasa "Atau ada masalah di apartemenmu, Yutaka-kun? Tadi caramu pegang gagang pintu depan itu kelihatan benar-benar seperti nggak sadar kalau kamu sedang berdiri di depan rumah orang lain."
        yutaka "Nggak ada masalah apa-apa kok, Chiasa. Murni salah tingkah karena kurang tidur saja."
        chiasa "...Begitu, ya. Semoga memang cuma kurang tidur saja."
        nar "Chiasa tersenyum tipis yang sama sekali tidak menyentuh matanya, lalu kembali menyendok karinya dengan tenang. Sisa makan malam itu berjalan jauh lebih sunyi. Kamu menghabiskan piringmu dengan hati-hati dan berpamitan tidak terlalu lama setelahnya, sadar betul bahwa tatapan mata keemasan gadis itu sama sekali belum kembali hangat."
    else:
        nar "Kamu memilih berhenti dua langkah sebelum pagar kayu. Daripada menebak-nebak kebiasaan pemilik tubuh ini dan mengambil risiko salah langkah di depan pintu, kamu mengeluarkan ponsel dari saku jaket dan membuka ruang obrolan dengan Koita."
        nar "Kamu mengetik pesan singkat menanyakan apakah mereka sedang di rumah dan apakah kamu boleh mampir sebentar, lalu menekan tombol kirim."
        play sound "audio/sfx/phone_buzz.wav"
        nar "Tidak sampai setengah menit, ponsel di tanganmu bergetar ringan. Balasan Koita masuk dengan nada santai yang terasa begitu alami. Ia bilang mereka sedang di rumah memasak kari, lalu tanpa sungkan langsung menitip dibelikan sebotol besar teh oolong dingin di minimarket ujung gang, lengkap dengan tambahan pesan kedua."
        nar "Pesan susulan itu berbunyi, 'Kalau di etalase masih ada puding karamel dua buah, sekalian ambil buat Chi-chan ya! Uangnya langsung kuganti begitu kamu sampai.'"
        nar "Melihat permintaan sederhana yang begitu santai itu, bahumu yang sejak tadi menegang perlahan turun. Tidak ada yang luar biasa atau kaku dari kedatanganmu bagi mereka."
        nar "Kamu membalas singkat 'Oke, sebentar lagi sampai', lalu berbalik berjalan ke minimarket terang di ujung jalan. Di dalam pendingin, kamu mengambil sebotol besar teh oolong yang permukaannya berembun dingin serta dua wadah kecil puding karamel, membayarnya di kasir, lalu berjalan kembali ke Rumah Amamiya dan menekan bel pintu."
        nar "Tidak lama berselang, pintu kayu terbuka. Amamiya Chiasa sudah berdiri di ambang pintu dengan senyum tipis seolah memang sudah menunggu kedatanganmu. Ia langsung melirik kantong plastik di tanganmu dan mengulurkan kedua tangannya menyambut."
        chiasa "Pas sekali, Ko-nii baru saja mematikan kompor. Wah, beli tehnya yang dingin lagi... eh, kamu beneran nemu puding karamelnya? Biasanya jam segini sudah habis lho di minimarket depan."
        yutaka "Tadi tinggal dua terakhir di rak paling belakang. Untung masih sempat kuambil."
        chiasa "Wah, beruntung banget. Makasih ya, Yutaka-kun. Ayo masuk, sepatumu taruh di sebelah kiri saja, sandalnya sudah kusiapkan."
        yutaka "Sama-sama. Maaf mendadak mampir begini."
        chiasa "Tumben sekali pakai acara minta maaf segala. Masuk gih, nanti karinya keburu dingin."
        nar "Kamu melepas sepatu di genkan yang hangat, mengenakan sandal tamu, lalu melangkah masuk menuju ruang makan. Dari balik meja dapur, Koita melambai sambil menata tiga piring kari mengepul dan menunjuk ke arah kulkas."
        koita "Yutaka! Uang teh sama pudingnya sudah kutaruh di atas kulkas ya, jangan lupa diambil!"
        yutaka "Nggak usah diganti, Koita, anggap saja oleh-oleh mampir sekalian numpang makan."
        koita "Lho, jangan begitu dong, setiap kali mampir kamu selalu bilang begitu. Nanti aku yang nggak enak."
        chiasa "Kalau Yutaka-kun sudah bilang begitu, terima saja, Ko-nii. Sebagai gantinya porsi karinya kasih daging paling banyak hari ini."
        koita "Haha, baiklah, adil juga. Duduk, Yutaka, gelasnya sudah kusiapkan di meja."
        nar "Kamu menuangkan teh oolong dingin ke tiga gelas kaca dan duduk di kursi yang sudah disiapkan. Kalian mulai menyantap kari hangat sambil berbincang santai soal minggu pertama semester baru dan rencana kumpul akhir pekan."
        chiasa "Oh ya, Yutaka-kun, tadi waktu kamu kirim pesan dulu baru datang, terus langsung mau titipan Ko-nii juga, rasanya kamu jadi jauh lebih tenang daripada biasanya. Lagi ada kabar bagus di kampus?"
        yutaka "Nggak ada kabar khusus, cuma lagi ingin mampir tanpa bikin repot saja."
        koita "Bagus dong, Chi-chan, berarti kita juga jadi lebih sering dapat puding dingin."
        chiasa "Heh, yang itu memang paling benar sih."
        nar "Selesai makan dan membereskan piring bersama ke bak cuci, Chiasa membuka tutup wadah puding karamel dengan sendok kecil dan menyodorkan satu lagi kepadamu, memaksa kamu ikut menghabiskan sisanya bersama teh dingin. Ketika kamu akhirnya mengenakan sepatu kembali di genkan dan melangkah keluar ke udara malam yang sejuk, kepastian kecil tentang bagaimana mereka menyambut kedatanganmu memberi rasa tenang yang tidak pernah kamu temukan di apartemen mewahmu yang sunyi."
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
    if kk_slot >= 3:
        nar "Malam hari yang santai di ruang tamu apartemenmu. Tirai jendela kaca lebar dibiarkan terbuka menampakkan lampu kota, sementara cahaya layar televisi menerangi karpet tempat Sakurajima Nagisa duduk bersila dengan semangat penuh."
    else:
        nar "Ruang tamu apartemenmu terasa sejuk oleh pendingin ruangan yang berembus pelan. Sakurajima Nagisa sudah duduk bersila di atas karpet tepat di depan layar televisi lebar, memegang pengendali konsol dengan semangat penuh sementara dua kaleng soda dingin dan semangkuk keripik berdiri di atas meja kaca."
    nar "Ia memilih sebuah permainan tarung kompetitif yang memang sudah terpasang rapi di konsol milik Yutaka. Sambil menekan tombol dengan cepat untuk mengatur jumlah ronde, batas waktu, dan arena, Nagisa berceloteh percaya diri, sepenuhnya yakin bahwa orang di sebelahnya hafal setiap kombinasi tombol jauh lebih baik daripada dirinya."
    nagisa "Kali ini nggak ada ampun, Yutaka! Kemarin malam aku sudah latihan kombo karakter ini sampai jari kram. Lihat saja, rekor menang beruntunmu bakal putus hari ini!"
    yutaka "Yakin sekali nih? Biasanya baru dua ronde kamu sudah teriak minta ulang dari awal sambil nyalahin tombol stiknya."
    nagisa "Itu kan minggu lalu! Hari ini beda! Aku sudah nonton rekaman turnamennya juga biar hafal cara mematahkan serangan sudutmu yang menyebalkan itu!"
    yutaka "Wah, sampai belajar dari rekaman segala. Serius banget."
    nagisa "Jelas dong! Mana bisa aku kalah terus dari kamu sampai lulus kuliah! Kalau aku menang hari ini, nanti di kantin kamu wajib traktir aku es krim!"
    yutaka "Tahu-tahu sudah pasang taruhan segala."
    nar "Di layar televisi, daftar papan skor menampilkan nama akun Kisaragi Yutaka bertengger sendirian di puncak dengan rasio kemenangan yang nyaris mustahil. Kamu meraih pengendali kedua di tanganmu."
    nar "Jari-jarimu memang langsung menemukan posisi alami di atas tombol arah dan pemicu bahu, sebuah refleks otot sederhana milik tubuh ini. Begitu layar pemilihan karakter terbuka dengan puluhan jurus dan hitungan jeda yang ketat, kepalamu benar-benar kosong karena insting bermain kelas profesional yang membuat Yutaka tak terkalahkan sama sekali tidak ikut diwariskan kepadamu."
    nagisa "Ayo, cepat pilih karakter utamamu! Jangan bilang kamu mau pakai karakter acak lagi buat ngeledek aku!"
    call kk_family_menu("Y05", ["Pura-pura mengalah agar terlihat wajar.", "Kalah terang-terangan saja.", "Minta waktu latihan dulu."])
    if _return == "A":
        nar "Daripada terlihat canggung dan kebingungan menekan tombol dasar, kamu memilih bersembunyi di balik citra santai Yutaka. Kamu bersandar ke belakang sambil menopang pengendali agak miring, sesekali melempar komentar ringan sambil sengaja membiarkan celah pertahananmu terbuka lebar."
        yutaka "Santai saja, Nagisa. Kalau aku main serius dari ronde pertama, nanti kamu malah ngambek dan nggak mau tanding lagi."
        nagisa "Siapa juga yang ngambek?! Jangan meremehkan aku, rasakan ini!"
        nar "Begitu aba-aba ronde muncul, Nagisa langsung menekan tombol bertubi-tubi dengan mata terpaku ke layar. Kamu menggerakkan karaktermu seadanya, menahan satu pukulan lalu sengaja membiarkan serangan beruntunnya masuk penuh."
        nagisa "Nah, kena! Terus masuk lagi... selesai!"
        nar "Layar menampilkan tulisan kemenangan besar untuknya. Alih-alih bersorak puas dan mengangkat kedua tangan seperti biasanya, Nagisa justru menurunkan pengendalinya perlahan ke atas karpet dan menoleh menatapmu dengan kening berkerut tajam."
        nagisa "...Tunggu. Kamu barusan sengaja mengalah, ya?"
        yutaka "Eh, maksudmu? Kombonya tadi memang masuk telak kok, aku nggak sempat menangkis."
        nagisa "Jangan bohong, Yutaka. Aku tahu persis rasanya menang beneran sama dikasih menang. Karaktermu tadi diam saja pas aku buka celah sebesar itu. Aku memang pengin ngalahin kamu, tapi aku nggak butuh menang yang dibungkus hadiah kasihan kayak begini."
        yutaka "Oke, oke, maaf kalau kelihatan begitu. Aku cuma mau lihat dulu seberapa jauh hasil latihanmu semalam sebelum ikut naik tempo."
        nagisa "Alasan banget... tapi memang tadi kombo baruku keluar mulus semua kan?"
        yutaka "Mulus kok. Lumayan jauh bedanya sama minggu lalu, perpindahan tombol tendangan bawahnya juga jauh lebih rapat."
        nar "Ia menghela napas pendek, raut kesalnya sedikit melunak meski sorot kompetitif di mata birunya tetap menyala tajam."
        nagisa "...Sudah, ronde berikutnya jangan terlalu sibuk menjaga perasaanku. Main biasa saja, biar kalau aku kalah lagi aku tahu salahku di mana. Ayo tekan ulang!"
        yutaka "Siap, ronde kedua aku nggak kasih celah gratis lagi."
        nagisa "Awas kalau kamu sengaja berhenti pencet tombol lagi, kulempar bantal sofa ini ya!"
        nar "Kamu mengangguk pelan sambil menekan tombol siap, diam-diam merasa lega karena setidaknya ia mengira kecanggungan tanganmu barusan hanyalah bentuk mengalah yang berlebihan alih-alih ketidaktahuan yang sesungguhnya."
    elif _return == "B":
        nar "Kamu memutuskan tidak repot-repot bersandiwara. Kamu memilih karakter yang tampak paling sering dipakai di daftar favorit Yutaka, lalu berusaha bertahan sebisa mungkin mengikuti ritme layar yang bergerak terlalu cepat."
        nar "Hasilnya telak dan sama sekali tidak rapi. Kamu salah menekan tombol menangkis menjadi lompat dua kali berturut-turut, gagal membaca serangan bawah Nagisa, dan kalah tanpa mampu membalas satu rangkaian kombo pun dalam waktu kurang dari setengah menit."
        nagisa "Bagus! Kena! Akhirnya aku bisa ngalahin..."
        nar "Seruan kemenangan Nagisa mendadak terpotong di tengah kalimat. Matanya tertahan pada tayangan ulang singkat di layar, lalu bergeser turun melihat jari-jarimu yang masih meraba-raba tombol bahu pengendali. Senyum lebarnya langsung lenyap seketika."
        nagisa "...Tunggu dulu. Kok bisa semudah itu?"
        nar "Ia meletakkan pengendalinya di atas meja kaca, lalu memutar badan penuh menghadapmu. Seluruh nada riuh dan ceria dari semenit lalu hilang, digantikan tatapan biru yang tajam sekaligus khawatir."
        nagisa "Yutaka... itu tadi jelas aneh. Kamu kelihatan benar-benar nggak tahu harus melakukan apa di tombolnya. Bahkan gerakan tangkis dasar yang biasanya kamu lakukan sambil tutup mata pun tadi nggak keluar sama sekali."
        yutaka "Ah... tanganku lagi kaku saja hari ini, sudah agak lama nggak pegang konsol ini."
        nagisa "Kamu baru main minggu lalu sama aku sebelum kuis! Waktu itu kamu masih menghajar karakterku tiga ronde berturut-turut sambil makan keripik dan mengobrol soal dosen! Jangan ngeles, aku nggak lagi mengejek, Yuu-kun. Serius. Akhir-akhir ini sebenarnya ada apa sama kamu?"
        yutaka "Nggak ada apa-apa, Nagisa. Sungguh, aku cuma lagi kurang tidur dan nggak fokus saja hari ini."
        nagisa "Kurang tidur nggak bikin orang lupa letak tombol tangkis di konsolnya sendiri, Yutaka..."
        yutaka "Beneran cuma lagi pusing sama urusan kuliah saja."
        nagisa "...Kalau kamu lagi ada masalah di rumah atau sama orang tuamu, jangan cuma dipendam sendiri sambil bilang nggak ada apa-apa. Kamu tahu kan kamu masih bisa cerita ke aku atau Ko-kun."
        yutaka "Iya, aku tahu. Nggak usah dipikirkan sampai sejauh itu, aku baik-baik saja."
        nagisa "Ya sudah, nggak usah lanjut main dulu deh kalau kepalamu lagi nggak enak. Minum sodanya saja dulu."
        nar "Panggilan masa kecil 'Yuu-kun' yang lolos begitu tulus dari bibirnya membuat dadamu terasa sedikit dingin. Ia akhirnya meraih kaleng sodanya dan mematikannya ke layar menu utama tanpa mengajak tanding ulang. Tidak ada amarah di matanya, hanya kebingungan yang jujur dari sahabat sejak kecil yang mulai menyadari ada jurang besar antara orang di hadapannya dengan Yutaka yang selama ini ia kenal."
    else:
        nar "Sebelum menekan tombol siap bertanding, kamu menghentikan kursor di layar menu, menurunkan pengendali sedikit, lalu menoleh menatap Nagisa dengan nada terus terang."
        yutaka "Tunggu sebentar, Nagisa. Kasih aku lima menit di mode latihan dulu. Tanganku terasa kaku sekali hari ini, susunan tombolnya perlu kuingat ulang sebentar."
        nar "Mata biru Nagisa langsung membulat tidak percaya, bibirnya sempat terbuka beberapa detik sebelum ia mendengus kaget."
        nagisa "Hah?! Minta latihan dulu? Seorang Kisaragi Yutaka minta pemanasan sebelum lawan aku?! Biasanya kamu yang paling berisik nyuruh aku pemanasan sambil ngeledek!"
        yutaka "Hari ini giliranku yang perlu pemanasan. Kalau aku kalah konyol gara-gara salah pencet tombol, kamu sendiri juga bakal nggak puas kan?"
        nagisa "Ya... benar juga sih. Aku maunya menang pas kamu benar-benar siap, supaya kamu nggak punya alasan buat ngeles habis itu."
        nar "Nagisa memandangmu sejenak dengan alis sedikit terangkat, tampak agak heran tetapi tidak menaruh curiga berlebihan. Ia akhirnya mengibaskan tangannya dan menekan tombol pindah ke mode latihan di layar."
        nagisa "...Ya sudah, ambil lima menitmu. Aku paling malas kalau lawannya cuma panik menjaga reputasi terus nanti cari-cari alasan kalau kalah."
        yutaka "Makasih. Jangan intip layar pas aku cek daftar gerakan."
        nagisa "Siapa juga yang mau ngintip gerakan dasar! Buruan deh, aku ambil es batu sama gelas di dapur dulu."
        nar "Begitu Nagisa melangkah ke dapur, kamu langsung membuka menu daftar gerakan dan memanfaatkan lima menit penuh itu untuk benar-benar menghafal tombol tangkis, menghindar, dan serangan dasar di layar hingga jarimu mulai menangkap iramanya."
        nar "Saat Nagisa kembali membawa dua gelas dingin berisi soda berdesis dan pertandingan sungguhan akhirnya dimulai, pertarungan berjalan jauh lebih sengit. Kamu menangkis beberapa serangan pembukanya dan sempat membalas dua kali di tengah ronde sebelum ia akhirnya menembus pertahananmu di detik terakhir."
        nagisa "Ha! Kena juga akhirnya! Gila, barusan tipis banget tahu nggak! Jantungku hampir copot pas kamu tangkis tendangan lompatku tadi!"
        yutaka "Lumayan juga latihanmu kemarin malam, Nagisa. Kalau tadi nggak sempat pemanasan, mungkin aku sudah kalah dalam dua puluh detik."
        nagisa "Jelas dong! Ayo satu ronde lagi, jangan mau kalah! Sekarang skor masih satu nol, kita main sampai tiga kemenangan!"
        yutaka "Oke, ayo lanjut."
        nar "Kamu tetap tidak sehebat pemilik tubuh aslinya, tetapi lima menit latihan barusan sudah cukup memberinya pertandingan sengit yang masuk akal tanpa sedikit pun merusak penyamaranmu."
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
