# Hari-hari kecil Miyuki: puding larut malam (Mi-D01) dan pastry bernama (Mi-D03).
# Efek mengikuti Alur_Cabang/01 baris Mi-D01 dan Mi-D03; kalimat adalah draf editorial.
# Besar kenaikan cemburu Nagisa (+5) adalah setelan prototipe.
init 1 python:
    KK_AFTERGLOW = (
        ("pudding_ditemani", "miyuki", "Soal puding malam itu, terima kasih banyak sudah duduk menemaniku ya. Aku memang jarang meminta tolong, dan ternyata rasanya nggak seburuk yang kubayangkan."),
        ("pudding_diantar", "miyuki", "Pudingnya kemarin enak sekali. Terima kasih ya sudah repot-repot mengantarkannya walau cuma sebentar."),
        ("pudding_ditolak", "miyuki", "Soal pesan puding malam itu, nggak apa-apa kok. Aku memang nggak seharusnya meminta hal seperti itu selarut itu."),
        ("pudding_ditertawakan", "miyuki", "Aku masih ingat balasanmu malam itu. Lain kali aku akan berpikir dua kali sebelum merepotkanmu dengan permintaan apa pun."),
        ("telepon_diabaikan", "miyuki", "Kamu pasti dengar suara telepon Ibu malam itu. Terima kasih sudah nggak membahasnya, walau aku tahu kamu mendengarnya."),
        ("telepon_ditanya", "miyuki", "Terima kasih sudah menunggu sampai telepon Ibu selesai baru bertanya. Waktu itu aku memang masih mencari kata-kata yang pas."),
        ("kenal_sayuri", "miyuki", "Ibu bilang kamu sopan sekali waktu bicara di telepon kemarin. Sejak itu beliau kelihatan agak lebih tenang soal aku. Sedikit saja sih."),
        ("koita_mencatat_pastry", "koita", "Pastry yang ada namamu kemarin itu... aku cuma sempat memperhatikan. Tachibana-senpai kelihatannya sungguh-sungguh banget waktu bikinnya."),
        ("nagisa_lihat_pastry", "nagisa", "Pastry kemarin itu beneran ada namamu kan? Aku cuma kebetulan lihat waktu lewat kok, jangan salah paham!"),
    )

    def kk_afterglow(cid):
        # Satu kalimat tindak lanjut per pilihan, muncul sekali pada obrolan berikutnya.
        for flag, who, line in KK_AFTERGLOW:
            if who == cid and kk_has(flag) and not kk_has("sudah_" + flag):
                kk_flag("sudah_" + flag)
                return line
        return None

    def kk_pastry_witnessed(key, place):
        # Nagisa hanya cemburu bila ia memang berada di tempat yang sama dan pastry itu terlihat.
        if key not in ("A", "C") or kk_daily_place("nagisa") != place:
            return False
        kk_rel("nagisa", "jeal", 5)
        kk_flag("nagisa_lihat_pastry")
        return True

    _hook("Mi-D01-A", lambda: (kk_adj("dimanja_miyuki", 10), kk_flag("pudding_ditemani")))
    _hook("Mi-D01-B", lambda: (kk_adj("dimanja_miyuki", 5), kk_flag("pudding_diantar")))
    _hook("Mi-D01-C", lambda: (kk_adj("dimanja_miyuki", -5), kk_flag("pudding_ditolak")))
    _hook("Mi-D01-D", lambda: (kk_adj("dimanja_miyuki", -10), kk_flag("pudding_ditertawakan"), kk_adj("luka_miyuki_pemain",5)))
    _hook("Mi-D03-A", lambda: kk_flag("koita_mencatat_pastry"))
    _hook("Mi-D03-B", lambda: kk_flag("pastry_disembunyikan"))
    _hook("Mi-D03-C", lambda: kk_flag("pastry_dibagikan"))

    # Mi-D04: nilai omiai mengikuti arah yang tertulis; angkanya adalah setelan prototipe.
    _hook("Mi-D04-A", lambda: (kk_adj("omiai_takeru", 3), kk_flag("telepon_diabaikan")))
    _hook("Mi-D04-B", lambda: (kk_rel("miyuki","trust", 5), kk_flag("telepon_ditanya")))
    _hook("Mi-D04-C", lambda: (kk_adj("omiai_takeru", -10), kk_rel("miyuki","trust", 3), kk_flag("kenal_sayuri")))

# ┌─ PANDUAN CERITA · Mi-D04 · Telepon Ibu yang Terdengar
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Tachibana Miyuki
# │ AWALAN  : pemain bersamanya Sabtu malam; omiai_takeru ≥ 40
# │ INTI    : A Pura-pura tidak dengar / B tanya setelahnya / C minta bicara dengan ibunya
# │ AKHIRAN : omiai_takeru ±; Trust; bicara dengan ibunya membuka hubungan pemain dengan keluarga Tachibana
# └─ tulis / perbaiki dialog di bawah ──
label kk_overheard_call:
    play sound "audio/sfx/phone_vibrate.wav"
    nar "Malam Sabtu yang tadinya hangat mendadak terpotong bunyi getar ponsel Miyuki di atas meja makan. Tangannya yang hendak mengangkat telepon malah tidak sengaja menyentuh tombol pengeras suara, membuat suara tegas Sayuri di seberang langsung terdengar jernih sebelum Miyuki sempat mematikannya."
    "Ibu Miyuki" "Keluarga Hayase sudah memastikan Tatsuru akan datang Sabtu depan. Jangan buat jadwal apa pun di luar itu, Ibu sudah menyusun semuanya dengan rapi."
    miyuki "Bu, tunggu sebentar, aku belum bilang bisa ikut. Jadwal piket klinik minggu depan masih padat..."
    nar "Kalimat Miyuki langsung terpotong oleh suara ibunya yang terus berbicara cepat di seberang sambungan. Punggung Miyuki menegang kaku, sementara tangan kirinya terus merapikan sendok logam di pinggir piring yang sebenarnya sudah sangat lurus."
    $ _rows = [(caption, Return(key), False) for key, caption in zip("ABC", KK_DYN_BY_ID["Mi-D04"]["choices"])]
    call screen kk_choice_panel(_rows, "Apa yang kamu lakukan?")
    $ _key = _return
    $ kk_record_choice("Mi-D04", _key)
    if _key == "A":
        nar "Kamu menunduk memandangi permukaan cangkir tehmu, bersikap seolah suara keras dari ponsel tadi sama sekali tidak masuk ke telingamu. Setelah menelan ludah pelan, Miyuki akhirnya mengucapkan kata iya pada tanggal yang baru saja diputuskan sepihak oleh ibunya."
        miyuki "...Maaf ya, tadi ada telepon urusan keluarga sebentar. Tehnya masih hangat?"
        if kk_host == "chiasa":
            chiasa "Masih hangat kok, Tachibana-senpai. Nggak apa-apa, pelan-pelan aja minumnya."
        else:
            yutaka "Masih hangat, Tachibana-senpai. Nggak usah buru-buru."
        nar "Ia melanjutkan makan malam dengan senyum sopan seolah percakapan tadi hanyalah pengingat jadwal biasa, padahal di kalendernya hari Sabtu depan baru saja diambil alih orang lain."
    elif _key == "B":
        nar "Kamu duduk tenang tanpa menyela hingga panggilan itu benar-benar berakhir. Begitu sambungan terputus, Miyuki meletakkan ponselnya agak jauh ke tepi meja, seakan benda itu masih sanggup mendesaknya bicara."
        if kk_host == "chiasa":
            chiasa "Tachibana-senpai... maaf tadi nggak sengaja kedengaran. Yang barusan ditelepon itu soal pertemuan sama Hayase Tatsuru lagi ya?"
        else:
            yutaka "Maaf tadi sempat kedengaran, Tachibana-senpai. Ibu Senpai barusan mengatur jadwal pertemuan sama Hayase lagi ya?"
        miyuki "...Iya. Tatsuru. Orang yang dipilih Ibu buat masa depanku, padahal aku sendiri bahkan belum pernah ditanya dengan sungguh-sungguh apakah aku mau atau nggak."
        if kk_host == "chiasa":
            chiasa "Senpai nggak harus langsung mengiyakan kalau memang belum mau, kan?"
        else:
            yutaka "Kalau jadwalnya bahkan belum dibicarakan sama Senpai, wajar banget kalau Senpai merasa keberatan."
        nar "Untuk pertama kalinya Miyuki menyebut nama itu tanpa memasang senyum penenang demi mengecilkan masalahnya. Malam ini ia tidak memintamu membereskan urusan keluarganya, cukup ada seseorang yang tidak langsung menganggap semuanya sudah disetujui."
    else:
        if kk_host == "chiasa":
            chiasa "Tachibana-senpai... kalau Senpai mengizinkan, boleh nggak aku ikut bicara sebentar sama Ibu Senpai? Cuma buat bilang malam ini Senpai lagi sama aku dan jadwal minggu depan masih padat."
        else:
            yutaka "Tachibana-senpai, kalau Senpai izinkan, boleh aku bicara sebentar ke Ibu Senpai? Supaya beliau tahu Senpai juga punya jadwal dan teman di kampus yang perlu dihormati."
        nar "Miyuki sempat terdiam ragu dengan mata melebar, lalu mengangguk pelan. Ia menyebut namamu singkat ke telepon sebelum menyerahkan ponselnya ke tanganmu."
        "Ibu Miyuki" "Oh, jadi kamu temannya Miyuki. Saya belum diberi tahu ada tamu bersamanya malam ini."
        if kk_host == "chiasa":
            chiasa "Selamat malam, Tachibana-san. Saya Amamiya Chiasa, adik tingkat Tachibana-senpai di kampus. Maaf lancang menyela, tapi akhir-akhir ini Tachibana-senpai capek sekali mengejar jadwal praktik, jadi mungkin rencana Sabtu depan lebih baik dibicarakan pelan-pelan dulu bersama beliau."
        else:
            yutaka "Selamat malam, Tachibana-san. Saya Kisaragi Yutaka, kenalan Tachibana-senpai di kampus. Maaf menyela sebentar, tapi jadwal kampus dan klinik Tachibana-senpai minggu depan cukup berat, sebaiknya rencana Sabtu depan dipastikan langsung sesuai kesediaan beliau dulu."
        "Ibu Miyuki" "...Begitu ya. Baik, nanti saya bicarakan lagi dengan Miyuki. Terima kasih atas perhatiannya."
        nar "Kesopanan di seberang sambungan berubah jauh lebih dingin sebelum panggilan ditutup, tetapi kini namamu tidak lagi bisa dianggap tidak ada di hadapan keluarga Tachibana."
        miyuki "Jujur aja jantungku sempat mau copot tadi... tapi terima kasih ya sudah minta izinku dulu sebelum ambil ponselnya. Aku tetap pengin ikut menentukan apa yang disampaikan ke Ibu."
    return

# ┌─ PANDUAN CERITA · Mi11 · Kue untuk Semua
# │ LOKASI  : Kampus Kouseikan · Kafe Komorebi
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : ia membuat terlalu banyak.
# │ INTI    : A makan bersama / B bantu bagikan / C minta khusus.
# │ AKHIRAN : gerbang cinta pemain.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi11:
    call kk_scene_enter("miyuki","Kafe Komorebi")
    if kk_host == "chiasa":
        nar "Kafe Komorebi di pertengahan Februari terasa hangat oleh aroma kopi sangrai dan wangi manis kue cokelat panggang yang baru dibuka dari kotak. Di meja pojok dekat jendela, di hadapan Tachibana Miyuki sudah berjajar tiga kotak kue ukuran besar hingga cangkir tehnya sendiri hampir tidak kebagian tempat di permukaan meja kayu."
        nar "Di balik meja konter, pemilik kafe, Ito Shinpei, hanya melirik sekilas sambil mengelap gelas dengan senyum tenang yang sudah sangat hafal dengan kebiasaan pelanggan tetapnya ini."
        "Ito" "Selamat datang, Chiasa-san. Tolong bantu habiskan ya, dari tadi meja sudut itu sudah lebih harum dari dapur saya sendiri."
        chiasa "Haha, siap, Ito-san. Tachibana-senpai, ini beneran Senpai panggang sendiri semuanya? Meja Komorebi sampai penuh begini."
        nar "Miyuki tertawa kecil sambil merapikan tumpukan piring kertas dan serbet yang ikut ia bawa dari apartemen."
        miyuki "Ara, ketahuan ya, Chiasa-chan. Tadi di apartemen aku salah hitung takaran adonan waktu mulai memanggang, jadinya malah dapat tiga loyang sekaligus. Dua kotak tadi sebagian sudah kubagi ke teman sekelas sama perawat jaga di klinik, tinggal satu loyang besar ini."
        nar "Ia menyebutnya salah hitung takaran. Meski begitu, setiap potongannya di dalam kotak sudah diiris seragam dan dihias krim cokelat dengan rapi, seolah sejak awal memanggang ia sudah membayangkan akan ada sangat banyak orang yang membutuhkannya hari ini."
        miyuki "Kalau loyang terakhir ini kubawa pulang lagi ke apartemen, Yuina pasti langsung menginterogasi aku sebenarnya bikin kue buat berapa puluh orang. Masalahnya, aku sendiri juga belum punya jawaban yang bagus buat Yuina."
        nar "Baru saja selesai bicara, Miyuki sudah kembali meraih pisau kue untuk memotong barisan berikutnya agar siap dibagikan. Di depan kursinya sendiri bahkan belum ada satu piring pun, dan ia sama sekali belum mencicipi secuil pun kue buatannya sendiri."
        nar "Kebiasaannya mendahulukan semua orang di sekitarnya membuat ia bahkan tidak sadar bahwa teh hangat di cangkirnya sendiri mulai mendingin."
        nar "Kamu memperhatikan gerak tangannya yang cekatan menata kotak kertas sambil menimbang cara menghentikan kesibukannya itu sejenak."
    else:
        nar "Kafe Komorebi di pertengahan Februari terasa hangat oleh aroma kopi sangrai dan wangi manis kue cokelat panggang yang baru dibuka dari kotak. Di meja pojok dekat jendela, di hadapan Tachibana Miyuki berjajar tiga kotak kue ukuran besar hingga cangkir tehnya sendiri hampir tidak kebagian ruang di permukaan meja kayu."
        nar "Di balik meja konter, pemilik kafe, Ito Shinpei, melirik sekilas sambil mengelap gelas dengan senyum tenang yang sudah sangat hafal dengan kebiasaan pelanggan tetapnya ini."
        "Ito" "Selamat datang, Yutaka-san. Kebetulan sekali kamu datang, meja pojok itu dari tadi sudah seperti cabang toko kue."
        yutaka "Haha, kelihatan banget dari pintu, Ito-san. Tachibana-senpai, ini beneran Senpai panggang sendiri semuanya? Meja Komorebi sampai penuh begini, cangkir kopiku nanti ditaruh di mana?"
        nar "Miyuki tertawa kecil sambil merapikan tumpukan piring kertas dan serbet yang ikut ia bawa dari apartemen."
        miyuki "Ara, ketahuan ya, Yutaka-kun. Tadi di apartemen aku salah hitung takaran adonan waktu mulai memanggang, jadinya malah dapat tiga loyang sekaligus. Dua kotak tadi sebagian sudah kubagi ke teman sekelas sama perawat jaga di klinik, tinggal satu loyang besar ini."
        nar "Ia menyebutnya salah hitung takaran. Meski begitu, setiap potongannya di dalam kotak sudah diiris seragam dan dihias krim cokelat dengan rapi, seolah sejak awal memanggang ia sudah membayangkan akan ada sangat banyak orang yang membutuhkannya hari ini."
        miyuki "Kalau loyang terakhir ini kubawa pulang lagi ke apartemen, Yuina pasti langsung nanya aku sebenarnya bikin kue buat berapa puluh orang. Masalahnya, aku sendiri juga belum punya jawaban yang bagus buat Yuina."
        nar "Baru saja selesai bicara, Miyuki sudah kembali meraih pisau kue untuk memotong barisan berikutnya agar siap dibagikan. Di depan kursinya sendiri bahkan belum ada satu piring pun, dan ia sama sekali belum mencicipi secuil pun kue buatannya sendiri."
        nar "Kesibukannya menyiapkan porsi untuk orang lain membuat cangkir teh hangat di samping sikunya sendiri terabaikan sejak tadi."
        nar "Kamu menatap deretan piring kertas bersih yang sudah ia siapkan di tepi meja sambil memikirkan cara terbaik untuk meresponsnya."
    call kk_family_menu("Mi11", ["\"Taruh dulu pisaunya, Senpai. Duduk sini, kita makan kuenya bareng dulu.\"", "\"Sini aku bantu tawarin ke meja-meja sebelah mumpung kuenya masih hangat.\"", "\"Aku nggak mau potongan sisa bagi-bagi. Pilih satu potongan khusus buatku dong, Senpai.\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Taruh dulu pisaunya, Tachibana-senpai. Sebelum Senpai sibuk mikirin mau kasih ke siapa lagi, duduk dulu di sini. Kita makan kuenya bareng sekarang, Senpai sendiri kan belum nyicipin sama sekali dari tadi."
            nar "Kamu menarik kursi di sebelahnya lalu mengambil dua piring kecil dan dua garpu kue dari nampan yang tadi disiapkan Ito Shinpei. Miyuki sempat terdiam kaget mendengar ajakanmu, lalu tersenyum lembut dan segera mengambil satu potongan bagian tengah yang paling rapi dan utuh untuk ditaruh di piringmu."
            miyuki "Nah, ini buat Chiasa-chan. Bagian tengahnya paling lembut."
            chiasa "Terus buat Senpai sendiri mau potongan yang mana? Jangan bilang nanti aja ya."
            nar "Gerakan tangan Miyuki yang tadi sudah hendak meletakkan pisau kue terhenti. Ia mengerjap pelan menatap loyang di depannya, seolah sudah lama sekali tidak ada yang menanyakan potongan mana yang paling ia inginkan sendiri."
            miyuki "Kalau buatku sendiri... sebenarnya aku paling suka bagian pinggirnya, Chiasa-chan. Yang pinggirannya agak kering dan kecokelatan kena panas loyang."
            chiasa "Lho, kirain Senpai suka bagian tengah yang banyak krimnya."
            miyuki "Justru bagian pinggir itu wanginya paling keluar. Biasanya bagian itu selalu kusimpan paling terakhir setelah semua orang selesai makan, soalnya bentuknya kurang rapi kalau dikasih ke orang lain."
            chiasa "Kalau gitu hari ini bagian pinggirnya dimakan duluan ya, Senpai. Sini piringnya."
            nar "Kamu memotong bagian sudut yang kecokelatan itu, memindahkannya ke piring Miyuki, lalu menyodorkan garpu ke tangannya. Kalian duduk berdampingan menikmati kue bersama sebelum ia memikirkan tamu atau teman lainnya. Begitu gigitan pertama masuk ke mulutnya, senyum senang yang ringan langsung merekah di wajah Miyuki."
            miyuki "Eh... ternyata pinggirannya renyah banget kali ini! Tadi aku coba ganti bubuk kakaonya pakai jenis yang tanpa gula tambahan, terus kukasih sejumput garam halus."
            chiasa "Pantesan rasa cokelatnya dalam banget dan nggak bikin enek, Senpai. Cocok banget diminum bareng teh hitamnya Ito-san."
            miyuki "Syukurlah kalau pas di lidahmu! Kemarin waktu nyoba resep pertama rasanya agak terlalu manis kalau dimakan bareng teh hangat begini."
            chiasa "Kalau Senpai makan duluan kayak gini kan langsung ketahuan enaknya, nggak cuma dengar kata orang lain."
            miyuki "Haha, benar juga ya, Chiasa-chan. Ternyata duduk makan potongan kesukaanku sendiri sebelum kotak ini dibagikan rasanya jauh lebih menyenangkan."
            chiasa "Sisanya yang di piring Senpai habisin pelan-pelan aja, jangan buru-buru bangun buat bungkusin kotak lagi."
            miyuki "Iya, aku habiskan dulu sama teh hangat ini. Rasanya sudah lama sekali aku tidak duduk santai menikmati kue buatanku sendiri di jam segini."
            nar "Ito Shinpei dari balik konter mengantarkan teko kecil berisi tambahan air panas tanpa mengganggu obrolan hangat di meja sudut kalian."
            nar "Miyuki menyesap tehnya dengan bahu yang tampak jauh lebih rileks, menikmati jeda sore yang kali ini benar-benar ia gunakan untuk menyenangkan dirinya sendiri."
        else:
            yutaka "Taruh dulu pisaunya, Tachibana-senpai. Sebelum Senpai sibuk mikirin mau kasih ke siapa lagi, duduk dulu di sini. Kita makan kuenya bareng sekarang, Senpai sendiri kan belum nyicipin sama sekali dari tadi."
            nar "Kamu menarik kursi di seberangnya lalu mengambil dua piring kecil dan dua garpu kue dari nampan di dekat konter. Miyuki sempat terdiam kaget mendengar ucapanmu, lalu tersenyum lembut dan langsung mengambil satu potongan bagian tengah yang paling rapi dan utuh untuk diletakkan di piringmu."
            miyuki "Nah, ini buat Yutaka-kun. Bagian tengahnya paling lembut."
            yutaka "Terus buat Senpai sendiri mau potongan yang mana? Jangan bilang nanti aja."
            nar "Tangan Miyuki yang hendak meletakkan pisau kue langsung terhenti. Ia mengerjap pelan memandangi loyang di hadapannya, seolah sudah lama sekali tidak ada yang menanyakan bagian mana yang paling ia inginkan sendiri."
            miyuki "Kalau buatku sendiri... sebenarnya aku paling suka bagian pinggirnya, Yutaka-kun. Yang pinggirannya agak kering dan kecokelatan kena panas loyang."
            yutaka "Kirain Senpai suka bagian tengah yang banyak krimnya."
            miyuki "Justru bagian pinggir itu aromanya paling keluar. Biasanya bagian itu selalu kusimpan paling terakhir setelah semua orang selesai makan, soalnya bentuknya kurang rapi kalau dikasih ke orang lain."
            yutaka "Kalau gitu hari ini bagian pinggirnya dimakan duluan aja, Senpai. Sini piringnya."
            nar "Kamu memotong bagian sudut yang kecokelatan itu, memindahkannya ke piring Miyuki, lalu menyodorkan garpu ke tangannya. Kalian duduk menikmati kue bersama sebelum ia beranjak memikirkan orang lain. Begitu gigitan pertama masuk ke mulutnya, sorot mata Miyuki langsung berbinar puas."
            miyuki "Wah... pinggirannya beneran renyah! Kali ini aku ganti pakai bubuk kakao murni tanpa gula tambahan sama sedikit garam halus supaya nggak terlalu manis."
            yutaka "Beneran terasa bedanya, Senpai. Rasa pahit cokelatnya masuk banget kalau ditemani kopi hitam."
            miyuki "Syukurlah berhasil! Resep sebelumnya agak terlalu berat di lidah kalau dimakan lebih dari satu potong."
            yutaka "Nah, makan duluan begini jauh lebih bener daripada nunggu sisa paling akhir terus."
            miyuki "Haha, iya juga ya, Yutaka-kun. Rasanya jadi ingat lagi kenapa dulu aku suka memanggang kue di waktu luang."
            yutaka "Habiskan dulu satu piring itu sampai tuntas, urusan bungkus sisa loyangnya belakangan aja."
            miyuki "Siap, Yutaka-kun. Aku nikmati dulu kue sama teh hangatku sore ini."
            nar "Cahaya matahari sore yang masuk melewati jendela Kafe Komorebi menyinari meja kayu tempat kalian berdua menikmati kudapan dengan tenang."
            nar "Untuk pertama kalinya dalam beberapa minggu terakhir, Miyuki duduk menikmati hasil karyanya sendiri tanpa terburu-buru melayani kebutuhan orang lain."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Mumpung kuenya masih hangat dan harum banget, sini aku bantu tawarin ke pelanggan di meja-meja sebelah ya, Tachibana-senpai. Sayang banget kalau sampai dingin di kotak."
            miyuki "Eh, boleh memangnya kita bagi-bagi di kafe? Biar kutanya dulu ke Ito-san."
            "Ito" "Silakan saja, Miyuki-san. Ini piring kayu bersihnya kalau mau dipakai."
            nar "Kalian menata beberapa potongan kue lalu berjalan pelan menghampiri tiga meja pelanggan lain di dalam kafe. Dua meja mahasiswa langsung menerima dengan wajah cerah sambil memuji aroma cokelatnya. Saat kalian mendekati meja paling pojok dekat rak majalah, seorang mahasiswa berkacamata yang sibuk mengetik di laptopnya mengangkat tangan sopan."
            "Pelanggan Kafe" "Wah, terima kasih banyak tawarannya, tapi maaf saya baru saja selesai makan dan sedang mengurangi makanan manis."
            nar "Di sebelahmu, senyum ramah Miyuki langsung menegang tipis. Sebelum ia sempat membungkuk meminta maaf terlalu dalam atau menawarkan membikinkan rasa lain, kamu segera menyahut santai."
            chiasa "Oh, nggak apa-apa banget kok! Maaf sudah mengganggu waktunya, selamat melanjutkan kerjanya."
            nar "Kamu menuntun pelan lengan Miyuki kembali ke meja sudut kalian."
            chiasa "Sudah, nggak apa-apa kok, Senpai. Orangnya tadi bilang baru kelar makan aja, jadi memang lagi kenyang."
            nar "Miyuki duduk kembali sambil memandangi potongan kue yang tersisa di piring saji kayu. Dahinya masih sedikit berkerut."
            miyuki "Tadi aku sempat kepikiran... apa bau cokelatnya terlalu pekat ya, Chiasa-chan? Harusnya tadi aku bikin versi yang rasanya lebih ringan kayak teh hijau supaya semua orang bisa makan."
            chiasa "Kuenya sudah enak banget kok, Senpai. Orang menolak satu potong kue itu cuma karena perutnya lagi kenyang, sama sekali nggak ada hubungannya sama kesalahan Senpai."
            nar "Miyuki terdiam menatap piring di tangannya beberapa detik, lalu mengembuskan napas pendek dengan tawa kecil yang agak lelah."
            miyuki "Lucu ya... dari dulu aku selalu mengira kalau ada seseorang yang menolak sesuatu yang kusiapkan, artinya aku harus segera membetulkan sesuatu dari diriku supaya mereka mau menerima lagi."
            chiasa "Sekarang gantian Senpai yang duduk makan bagiannya sendiri ya. Nih, tehnya keburu dingin."
            miyuki "Iya, Chiasa-chan. Makasih ya tadi sudah cepat bantuin jawab di depan meja pojok."
            chiasa "Sama-sama, Senpai. Yuk makan bareng."
            nar "Kamu menuangkan teh hangat dari teko kecil ke dalam cangkir Miyuki lalu menggeser piring kuenya agar lebih dekat ke hadapannya."
            nar "Dua meja mahasiswa yang tadi menerima potongan kue tampak melambaikan tangan sambil mengucapkan terima kasih saat mereka beranjak menuju kasir."
            nar "Kalimat sederhana darimu tadi berhasil menahan kebiasaan lama Miyuki yang selalu menyalahkan dirinya sendiri setiap kali menghadapi penolakan kecil."
            nar "Miyuki mengangguk pelan, mengambil garpu kue, lalu akhirnya mencicipi potongan kuenya sendiri dengan raut wajah yang jauh lebih tenang."
        else:
            yutaka "Mumpung kuenya masih hangat dan harum, sini kubantu tawarin ke meja-meja sebelah ya, Tachibana-senpai. Sayang kalau keburu dingin di kotak."
            miyuki "Eh, boleh memangnya kita bagi-bagi di kafe? Biar kutanya dulu ke Ito-san."
            "Ito" "Tentu saja boleh, Miyuki-san. Pakai piring kayu yang ini saja."
            nar "Kalian menata beberapa potongan kue lalu berjalan pelan menghampiri tiga meja pelanggan lain di dalam kafe. Dua meja mahasiswa langsung menerima dengan wajah senang sambil memuji aroma cokelatnya. Saat kalian mendekati meja pojok dekat rak majalah, seorang mahasiswa berkacamata yang sibuk mengetik di laptop mengangkat tangan sopan."
            "Pelanggan Kafe" "Terima kasih tawarannya, tapi maaf saya baru saja makan berat dan sedang menghindari yang manis-manis."
            nar "Di sebelahmu, senyum ramah Miyuki langsung menegang tipis. Sebelum ia sempat membungkuk meminta maaf terlalu dalam atau menawarkan membuat rasa lain, kamu segera menyahut santai."
            yutaka "Nggak masalah sama sekali. Maaf ganggu sebentar, silakan lanjut."
            nar "Kamu mengajak Miyuki kembali ke meja sudut kalian."
            yutaka "Sudah, santai aja, Senpai. Orangnya cuma baru kelar makan, jadi memang lagi kenyang aja."
            nar "Miyuki duduk kembali sambil memandangi sisa potongan kue di piring saji kayu. Dahinya masih sedikit berkerut."
            miyuki "Tadi aku sempat kepikiran... apa aroma cokelatnya terlalu pekat ya, Yutaka-kun? Harusnya tadi aku bikin versi teh hijau juga supaya semua orang bisa makan."
            yutaka "Kuenya sudah enak banget kok, Senpai. Orang menolak satu potong kue itu ya cuma karena perutnya penuh, sama sekali nggak berarti ada yang salah dari kuenya atau dari Senpai."
            nar "Miyuki terdiam menatap piring di tangannya beberapa detik, lalu mengembuskan napas pendek dengan tawa kecil yang agak lelah."
            miyuki "Aneh ya... dari dulu aku selalu mengira kalau ada yang menolak sesuatu yang kusiapkan, berarti aku harus cepat-cepat membetulkan sesuatu dari diriku supaya mereka mau menerima lagi."
            yutaka "Sekarang giliran Senpai duduk makan bagiannya sendiri. Nih, tehnya keburu dingin."
            miyuki "Iya, Yutaka-kun. Terima kasih ya tadi langsung bantuin nutup percakapan di meja pojok."
            yutaka "Santai aja, Senpai. Ayo makan."
            nar "Kamu menggeser piring kecil berisi potongan sudut kue cokelat itu ke depan Miyuki sambil mengambil cangkir kopimu sendiri."
            nar "Beberapa pelanggan di meja tengah tampak menikmati kue pemberian tadi dengan lahap sambil berbincang santai di bawah lampu kafe yang teduh."
            nar "Ketegangan halus di bahu Miyuki perlahan mencair setelah ia menyadari bahwa penolakan biasa tidak pernah mengurangi nilai kebaikannya."
            nar "Miyuki mengangguk pelan, mengambil garpu kue, lalu akhirnya mencicipi potongan kuenya sendiri dengan raut wajah yang jauh lebih tenang."
    else:
        if kk_host == "chiasa":
            chiasa "Tachibana-senpai, aku nggak mau potongan acak dari sisa yang mau dibagi-bagi ke orang lain ya. Pilih satu potongan khusus buatku dong."
            nar "Tangan Miyuki berhenti di atas gagang pisau kue. Ia menoleh menatapmu sambil menahan senyum jahil yang lembut, lalu berpura-pura mencondongkan tubuh untuk memeriksa seluruh permukaan loyang dengan keseriusan seperti dokter yang sedang memilih tindakan paling penting."
            miyuki "Ara... Chiasa-chan minta potongan khusus pilihan Senpai sendiri ya? Boleh banget dong. Tapi kalau mau yang khusus, ada satu syarat yang harus kamu setujui dulu."
            chiasa "Wah, pakai syarat segala. Syaratnya apa, Senpai?"
            miyuki "Kamu harus duduk di sini dan makan kuenya bareng Senpai sekarang juga sampai habis. Jangan cuma dibungkus dibawa pulang ke rumah terus nanti malam baru kirim pesan bilang kuenya enak."
            chiasa "Cuma itu syaratnya? Gampang banget, aku setuju."
            nar "Miyuki tersenyum lebar, lalu mengiris satu potongan tengah yang lapisan cokelat dan krimnya paling utuh untuk diletakkan di depanmu. Setelah itu, ia memotong satu bagian lagi yang sama rapinya untuk dirinya sendiri dan menaruhnya di piring sebelah."
            miyuki "Nah, ini potongan paling bagus di seluruh loyang hari ini. Dan karena kamu sudah setuju sama syaratnya, setengah jam ke depan waktumu jadi milik Senpai dulu ya, Chiasa-chan. Nggak boleh buru-buru lihat jam."
            chiasa "Siap, Tachibana-senpai. Selamat makan."
            miyuki "Enak nggak? Jangan langsung muji karena nggak enak sama Senpai lho."
            chiasa "Lembut banget krimnya, terus cokelatnya nggak terlalu manis. Beneran beda rasanya kalau dimakan bareng di sini."
            miyuki "Haha, senang dengernya. Kalau begitu ayo santai dulu, tehnya baru kuseduh."
            chiasa "Kapan-kapan kalau Senpai bikin kue lagi, langsung sisihkan dua potong kayak gini dari awal ya."
            miyuki "Janji, Chiasa-chan. Lain kali dua potong terbaiknya langsung kusimpan sebelum loyangnya kubuka buat orang lain."
            nar "Ia meletakkan pisau pemotong kue ke tepi nampan dan menutup kembali kotak kue besar itu agar tidak lagi menyita perhatiannya."
            nar "Suasana meja pojok Kafe Komorebi terasa begitu akrab sementara kalian berdua menikmati teh hangat dan kue cokelat tanpa gangguan."
            nar "Miyuki menyuap potongan kuenya dengan tatapan mata yang berbinar hangat dan tulus. Kali ini ia berhenti menyembunyikan keinginannya di balik alasan melayani orang lain dan terang-terangan meminta sebagian kecil waktumu untuk duduk bersamanya."
        else:
            yutaka "Tachibana-senpai, aku nggak mau potongan sisa bagi-bagi ya. Pilih satu potongan khusus buatku dong."
            nar "Tangan Miyuki berhenti di atas gagang pisau kue. Ia menoleh menatapmu sambil menahan senyum lembut yang sedikit jahil, lalu berpura-pura mencondongkan tubuh untuk memeriksa seluruh permukaan loyang dengan keseriusan yang dibuat-buat."
            miyuki "Ara... Yutaka-kun minta potongan khusus pilihan Senpai sendiri ya? Boleh banget. Tapi kalau mau yang khusus, ada satu syarat yang harus kamu setujui dulu."
            yutaka "Pakai syarat segala nih? Apa syaratnya, Senpai?"
            miyuki "Kamu harus duduk di sini dan makan kuenya bareng Senpai sekarang juga. Jangan cuma dibungkus dibawa pulang ke apartemen terus nanti malam baru kirim pesan bilang kuenya enak."
            yutaka "Cuma itu? Gampang banget, aku setuju."
            nar "Miyuki tersenyum lebar, lalu mengiris satu potongan tengah yang lapisan cokelat dan krimnya paling utuh untuk diletakkan di depanmu. Setelah itu, ia memotong satu bagian lagi yang sama rapinya untuk dirinya sendiri dan menaruhnya di piring sebelah."
            miyuki "Nah, ini potongan paling bagus di seluruh loyang hari ini. Dan karena kamu sudah sepakat sama syaratnya, setengah jam ke depan waktumu jadi milik Senpai dulu ya, Yutaka-kun. Nggak boleh buru-buru lihat jam tangan."
            yutaka "Siap, Tachibana-senpai. Selamat makan."
            miyuki "Gimana rasanya? Bilang terus terang aja kalau kemanisan ya."
            yutaka "Pas banget kok, pahit cokelatnya masih kerasa. Jauh lebih enak daripada kue toko."
            miyuki "Syukurlah. Kalau begitu kita habiskan pelan-pelan bareng kopinya ya."
            yutaka "Lain kali kalau Senpai panggang kue lagi, langsung pisahin dua potong terbaik dari awal buat meja kita."
            miyuki "Tentu saja, Yutaka-kun. Lain kali aku tidak akan menunggu sisa loyang lagi kalau mau makan kue berdua denganmu."
            nar "Ia menggeser kotak loyang besar itu ke sisi meja agar ruang di antara cangkir kalian terasa lebih lapang dan leluasa."
            nar "Percakapan ringan mengenai kegiatan kampus mengalir dengan hangat diiringi alunan musik akustik pelan dari pengeras suara Kafe Komorebi."
            nar "Miyuki menyuap potongan kuenya dengan sorot mata yang memancarkan kelegaan hangat. Kali ini ia berani meminta sebagian kecil waktumu secara langsung sebagai keinginannya sendiri tanpa menyamarkannya di balik alasan melayani orang lain."
    return

# ┌─ PANDUAN CERITA · Mi-D12 · Ia Memilih Dirinya
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Tachibana Miyuki
# │ AWALAN  : dimanja ≥ 70; semua luka < 30; Trust ≥ 70
# │ INTI    : A Dukung / B goda / C bilang itu berkat pemain
# │ AKHIRAN : omiai_takeru −30; E-MI-01 dan E-MI-02 menguat
# └─ tulis / perbaiki dialog di bawah ──
label kk_miyuki_refuses:
    nar "Miyuki memperlihatkan kalender. Satu Sabtu yang biasanya sudah penuh coretan keluarga kini kosong, bukan karena ia lupa menuliskan sesuatu."
    miyuki "Ibu menelepon soal Hayase. Aku bilang tidak mau bertemu untuk omiai lagi. Bukan karena sibuk. Aku sengaja tidak memakai jadwal sebagai alasan."
    nar "Ia masih menggenggam ponsel, ibu jarinya mengusap bagian samping yang sama berulang kali."
    miyuki "Ibu diam lama. Aku hampir bilang mungkin bulan depan. Tapi aku menunggu sampai beliau menjawab."
    call kk_family_menu("Mi-D12", ["Dukung keputusan Miyuki.", "Goda dia soal berani membantah ibunya.", "Katakan kau yang membuatnya berani."])
    if _return == "A":
        nar "Kau mendukung keputusan itu dan menanyakan apa yang ia perlukan sekarang. Miyuki berpikir, lalu meminta minum dan waktu untuk tidak membicarakan Hayase."
        miyuki "Kalau Ibu bertanya lagi, aku mau menjawab sendiri. Tapi hari ini aku ingin merasakan bahwa Sabtu itu boleh kosong."
        nar "Ia meletakkan ponsel. Sesudah beberapa menit tangannya berhenti mencari benda tersebut setiap kali ada suara."
    elif _return == "B":
        nar "Kau menggoda keberaniannya membantah keluarga. Miyuki sempat tertawa, lalu mengangkat tangan agar kau melihat getarnya."
        miyuki "Aku memang gemetar. Ini bukan karena mendadak jadi orang berani. Aku cuma tetap bilang tidak meskipun takut."
        nar "Ia menunggu sampai kau mendengarnya dengan serius sebelum ikut tertawa lagi."
    else:
        nar "Kau menyebut keberanian itu sebagai hasil pengaruhmu. Miyuki memandangmu sebentar, kali ini tidak buru-buru membalas dengan terima kasih."
        miyuki "Kamu sudah membantuku. Aku nggak menyangkal. Tapi tadi aku yang bicara. Aku ingin boleh menyimpan bagian itu sebagai milikku."
        nar "Kalimatnya lembut, tetapi tidak ditarik kembali ketika suasana menjadi canggung."
    return

init 1 python:
    def kk_miyuki_ready_to_refuse():
        return (kk_get("dimanja_miyuki",10) >= 70 and kk_rel_get("miyuki","trust") >= 70
                and kk_get("luka_miyuki_pemain",0) < 30 and kk_get("luka_miyuki_koita",10) < 30
                and kk_get("luka_miyuki_diri",15) < 30)

    _hook("Mi11-A",lambda: kk_adj("dimanja_miyuki",5))
    _hook("Mi11-B",lambda: kk_adj("dimanja_miyuki",5))
    _hook("Mi11-C",lambda: kk_rel("miyuki","intim",2))
    for response in "ABC":
        _hook("Mi-D12-" + response,lambda: kk_adj("omiai_takeru",-30))

# ┌─ PANDUAN CERITA · Mi12 · Tahun Keempat
# │ LOKASI  : Kampus Kouseikan · Gedung Kedokteran
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : klinik dimulai.
# │ INTI    : A bantu belajar / B ganggu / C jarak.
# │ AKHIRAN : stage 2 dimulai.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi12:
    call kk_scene_enter("miyuki","Gedung Kedokteran")
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Lampu koridor lantai dua Gedung Kedokteran menyala terang di tengah suasana malam awal April yang sunyi. Di dalam ruang belajar kecil yang pintunya terbuka separuh, bau kertas buku referensi tebal bercampur dengan aroma samar cairan pembersih ruang praktik."
        elif kk_slot == 2:
            nar "Cahaya sore awal musim semi masuk miring melalui jendela tinggi ruang belajar lantai dua Gedung Kedokteran. Sebagian besar mahasiswa lain sudah meninggalkan ruangan, menyisakan suasana tenang yang beraroma buku teks tebal dan teh hangat dari termos."
        else:
            nar "Ruang belajar lantai dua Gedung Kedokteran masih lengang di bawah cahaya siang awal musim semi. Hanya suara lembaran kertas dibalik dan bunyi jam dinding yang terdengar menemani aroma buku teks medis yang memenuhi rak."
        nar "Tachibana Miyuki duduk di meja panjang dekat jendela dengan jas dokter putih yang tampak baru disetrika rapi di atas atasan gelapnya. Rambut hitam panjangnya yang lurus terurai jatuh melewati bahu ketika ia menunduk merapikan potongan selotip transparan di sampul dalam buku catatan tebalnya, sementara stetoskopnya terlipat rapi di samping kotak pensil."
        nar "Begitu mendengar langkahmu mendekat, Miyuki mengangkat wajahnya. Mata cokelat kemerahannya langsung menyambutmu dengan senyum lembut yang akrab."
        miyuki "Ara, Chiasa-chan? Tumben mampir sampai ke lantai dua Gedung Kedokteran. Kelas tahun keduamu sudah selesai?"
        chiasa "Baru aja selesai, Tachibana-senpai. Tadi kebetulan lewat halaman sebelah, terus ingat minggu ini Senpai mulai masuk jadwal baru tahun keempat. Lagi nempelin jadwal ya?"
        nar "Kamu mencondongkan badan sedikit melihat selembar kertas yang baru saja direkatkan Miyuki di halaman depan buku catatannya. Kotak-kotak hari dari Senin sampai Jumat penuh sesak dengan tulisan tangan kecil berisi jadwal rotasi klinik, sesi jaga observasi, dan rapat evaluasi kasus yang memenuhi ruang yang dahulu cukup untuk satu minggu kuliah biasa."
        nar "Menyadari matamu tertahan cukup lama pada jadwal padat itu, Miyuki langsung tersenyum cerah dan menepuk sampul bukunya pelan."
        miyuki "Haha, kelihatannya memang agak penuh ya? Tenang aja, masih bisa diatur kok, Chiasa-chan. Sebagian cuma jam pengenalan bangsal sama pengamatan senpai aja buat minggu pertama."
        chiasa "Tapi jam istirahat siangnya aja kelihatan mepet banget lho, Senpai. Jujur aja, gimana rasanya mau mulai praktik klinik besok?"
        nar "Mendengar pertanyaan langsungmu, senyum terlatih di bibir Miyuki pelan-pelan melunak. Ia meletakkan gulungan selotip di pinggir meja, lalu mengusap tepi lembar jadwalnya dengan ibu jari."
        miyuki "...Besok benar-benar mulai. Aku senang sekali, sungguh, akhirnya langkahku menuju bagian anak mulai nyata. Cuma di saat yang sama, aku juga takut banget begitu besok pagi melangkah masuk ke bangsal dan ditanya dokter pembimbing, kepalaku malah mendadak kosong terus lupa semua yang kupelajari tiga tahun ini."
        nar "Ia membuka halaman tengah catatannya, memperlihatkan satu lembar studi kasus yang bagian pinggirnya penuh koreksi tinta merah dari dosen pembimbing, diikuti tiga halaman ringkasan gejala dan prosedur pemeriksaan yang sudah ditandai dengan pembatas kertas warna-warni."
        miyuki "Tadi waktu simulasi kelas, aku sempat kelewat satu pertanyaan riwayat alergi obat di sini. Jadi sebelum pulang hari ini, aku mau mengulang tiga halaman ini sekali lagi biar besok nggak gugup."
        chiasa "{i}Biasanya dia selalu kelihatan paling tenang di antara semuanya... baru kali ini aku lihat tangannya sempat berhenti begini cuma gara-gara tiga halaman catatan.{/i}"
    else:
        if kk_slot >= 3:
            nar "Koridor lantai dua Gedung Kedokteran terasa sunyi di bawah sorot lampu putih panjang malam awal April. Dari pintu ruang belajar yang terbuka separuh, tercium bau kertas buku referensi tebal bercampur aroma tipis cairan pembersih ruang praktik."
        elif kk_slot == 2:
            nar "Cahaya sore awal musim semi masuk miring melalui jendela kaca tinggi ruang belajar lantai dua Gedung Kedokteran. Sebagian besar mahasiswa sudah pulang, menyisakan suasana tenang beraroma buku teks tebal dan teh hangat dari termos."
        else:
            nar "Ruang belajar lantai dua Gedung Kedokteran masih cukup lengang di bawah cahaya siang awal April. Hanya bunyi halaman buku dibalik dan detak pelan jam dinding yang terdengar menemani deretan rak buku referensi medis."
        nar "Di meja panjang dekat jendela, Tachibana Miyuki duduk mengenakan jas dokter putih rapi di atas atasan gelapnya, dengan stetoskop terlipat di sebelah kotak alat tulis. Rambut hitam panjangnya yang lurus terurai jatuh melewati bahu ketika ia menunduk meratakan potongan selotip transparan di sampul dalam buku catatan tebalnya."
        nar "Begitu melihat bayanganmu berhenti di dekat mejanya, Miyuki menoleh dan mengangkat wajah. Mata cokelat kemerahannya menyambutmu dengan senyum lembut yang akrab."
        miyuki "Ara, Yutaka-kun? Tumben mampir sampai ke lantai dua Gedung Kedokteran. Kuliah tahun ketigamu sudah selesai?"
        yutaka "Baru selesai tadi, Tachibana-senpai. Kebetulan lewat halaman sebelah, terus ingat minggu ini Senpai resmi masuk tahun keempat. Lagi nempelin jadwal baru ya?"
        nar "Kamu mencondongkan badan sedikit melihat selembar kertas yang baru direkatkan di bagian depan catatannya. Kotak hari dari Senin sampai Jumat penuh oleh tulisan kecil berisi rotasi klinik, jam observasi bangsal, hingga rapat evaluasi yang memenuhi ruang yang dahulu cukup untuk satu minggu kuliah biasa."
        yutaka "Itu jadwal klinik atau jadwal piket pabrik, Senpai? Jam istirahat siangnya aja hampir nggak kelihatan."
        nar "Mendengar komentarmu, Miyuki tertawa kecil sambil cepat-cepat menepuk sampul bukunya seperti kebiasaannya meredam kekhawatiran orang lain."
        miyuki "Haha, kelihatannya memang agak padat ya? Tenang aja, masih bisa diatur kok, Yutaka-kun. Minggu pertama sebagian masih pengenalan bangsal sama pengamatan senpai aja."
        yutaka "Jangan langsung pasang senyum aman begitu dong, Senpai. Jujur aja, gimana rasanya mau mulai turun ke klinik besok?"
        nar "Senyum terlatih Miyuki perlahan melunak. Ia meletakkan gulungan selotip di samping buku, lalu mengusap tepi lembar jadwal itu dengan ibu jarinya."
        miyuki "...Besok benar-benar mulai. Aku senang, sungguh, akhirnya langkahku ke bagian anak mulai jalan beneran. Cuma di sisi lain, aku juga takut banget begitu besok masuk bangsal terus ditanya dokter pembimbing, kepalaku malah mendadak kosong dan lupa semua yang sudah kupelajari tiga tahun ini."
        nar "Ia membalik catatannya ke bagian tengah, memperlihatkan satu jawaban studi kasus yang diberi koreksi tinta merah pembimbing, disusul tiga halaman ringkasan prosedur pemeriksaan yang sudah ditandai dengan pembatas warna-warni."
        miyuki "Tadi waktu latihan kelas, aku sempat salah urutan tanya riwayat obat pasien anak di sini. Jadi sebelum pulang hari ini, aku mau mengulang tiga halaman ini sekali lagi biar besok lebih tenang."
        yutaka "{i}Biasanya dia selalu kelihatan paling dewasa dan paling siap ngurusin semua orang... melihat dia ragu begini baru kerasa seberapa berat beban tahun keempat itu.{/i}"
    call kk_family_menu("Mi12", ["\"Sini aku bantu bacain soalnya, Senpai. Kita ulang bareng tiga halaman ini dulu.\"", "\"Tutup dulu catatannya sebentar yuk, Senpai. Kita jalan keluar cari angin dulu biar kepalanya nggak penuh.\"", "\"Kalau begitu aku nggak ganggu jam belajarnya ya, Senpai. Ada yang perlu kuambilkan dulu sebelum aku pergi?\""])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu menarik kursi kayu di sebelahnya, meletakkan tas kainmu di pangkuan, lalu mengulurkan tangan meminta buku catatan yang terbuka itu."
            chiasa "Sini aku bantu bacain soalnya ya, Tachibana-senpai. Aku memang nggak paham istilah kedokterannya sih, tapi kalau cuma nutupin kolom jawaban terus ngecek cocok atau nggaknya sama catatan Senpai, aku bisa banget."
            nar "Miyuki mengerjap kaget sebentar, lalu tawa lembut lolos dari bibirnya saat ia menyerahkan buku catatan tebal itu kepadamu."
            miyuki "Wah, itu justru paling membantu, Chiasa-chan! Kalau kubaca sendiri, mataku sering nggak sengaja langsung melirik bagian jawabannya duluan. Boleh kita mulai dari halaman yang ada tanda merahnya?"
            chiasa "Siap. Kita pasang batas waktu empat puluh menit aja ya biar Senpai masih sempat istirahat sebelum pulang. Oke, pertanyaan pertama di sini tertulis pasien anak usia enam tahun datang dengan demam tinggi hari ketiga. Langkah pemeriksaan awal yang nggak boleh dilewati sebelum kasih obat apa aja?"
            miyuki "Pertama periksa tanda dehidrasi sama frekuensi napasnya, lalu tanyakan riwayat obat yang sudah diminum di rumah serta alergi obat sebelumnya. Setelah itu cek ruam di kulit sama kondisi tenggorokan."
            chiasa "Wah, lancar banget! Persis sama semua poin yang digarisbawahi di sini. Lanjut nomor dua ya, Senpai. Kalau di catatan keluhan ada muntah berulang dan anak mulai lemas, urutan prioritas tindakan pertama yang dicoret merah pembimbing kemarin apa?"
            nar "Miyuki menarik napas pendek dan menyebutkan dua prosedur pertama dengan cepat, lalu jeda di langkah ketiga dan menyebut urutan tes laboratorium sebelum stabilisasi cairan. Kamu melirik baris bertinta merah di kertas, baru saja hendak membisikkan kata pertama sebagai petunjuk ketika tangan Miyuki terangkat halus menahan pergelangan tanganmu."
            miyuki "Sebentar, Chiasa-chan, jangan kasih petunjuk dulu ya. Aku mau cari sendiri di mana letak lupaku."
            nar "Ia memejamkan mata sebentar, mengetukkan telunjuknya pelan di tepi meja sambil mengulang kondisi pasien dari awal dengan suara pelan."
            miyuki "...Oh! Anak lemas disertai muntah berulang, berarti cek tanda syok dan jalur cairan dulu sebelum hal lain. Tadi aku langsung lompat ke daftar tes darah karena panik melihat poin berikutnya."
            chiasa "Nah, bener banget, Senpai! Persis sama catatan tinta merah di sini!"
            miyuki "Haha, akhirnya ketemu juga celah salahnya. Kalau cuma kubaca ulang dalam hati tadi, pasti aku bakal langsung lewat lagi di bagian itu."
            nar "Kalian meneruskan tanya jawab itu lembar demi lembar sampai seluruh tiga halaman tuntas dibahas, lalu menutup buku tepat ketika jarum jam dinding menyentuh batas waktu yang telah disepakati."
            miyuki "Terima kasih banyak ya, Chiasa-chan. Aneh ya, tadi rasanya besok kayak tembok besar yang bikin takut. Setelah dibedah satu per satu bareng kamu begini, rasanya jadi jauh lebih tenang."
            chiasa "Besok pasti lancar kok, Tachibana-senpai. Sekarang yuk beresin bukunya, jangan lupa makan yang bener habis ini."
            nar "Miyuki mengangguk dengan bahu yang tampak jauh lebih ringan, memasukkan buku catatannya ke tas tanpa lagi menatap jadwal kliniknya dengan cemas."
        else:
            nar "Kamu menarik kursi kayu di seberangnya, menaruh tas selempangmu di lantai, lalu mengulurkan tangan meminta buku catatan itu dengan santai."
            yutaka "Sini bukunya, Tachibana-senpai. Aku memang nggak paham istilah medisnya, tapi kalau cuma nutupin kolom jawaban, bacain soalnya satu-satu, terus nyocokin sama kunci catatan sambil jaga waktu pakai jam tanganku, aku lumayan jago."
            nar "Miyuki berkedip sejenak, lalu senyum lega yang ringan mengembang di wajahnya saat ia menyerahkan buku tebal itu ke tanganmu."
            miyuki "Wah, itu justru paling kubutuhkan sekarang, Yutaka-kun. Kalau kubaca sendirian, mataku selalu refleks melirik baris jawabannya duluan. Mulai dari halaman pertama yang ada tinta merahnya ya?"
            yutaka "Siap. Kita sepakati empat puluh menit penuh ya, habis itu berhenti biar Senpai masih sempat istirahat sebelum pulang. Soal pertama, anak usia lima tahun datang dengan batuk parah dan napas cepat sejak kemarin sore. Poin pemeriksaan awal yang wajib dicek di menit pertama apa aja?"
            miyuki "Cek laju pernapasan, tarikan dinding dada, sama saturasi oksigennya dulu. Baru setelah itu dengarkan suara napas pakai stetoskop dan tanyakan riwayat asma atau alergi ke orang tuanya."
            yutaka "Tepat semua sesuai garis bawah di sini. Lanjut kasus kedua yang kena tanda merah pembimbing kemarin. Kalau hasil tanya orang tua ternyata anak sempat diberi obat penurun panas dewasa di rumah, langkah pengecekan prioritas yang dicatat di baris ketiga apa?"
            nar "Miyuki menjawab langkah penghitungan berat badan dengan cepat, lalu tersendat satu detik dan langsung menyebut observasi suhu sebelum memastikan takaran dosis yang sudah masuk serta rentang waktunya. Begitu kamu hendak membuka mulut memberi satu kata pancingan, Miyuki cepat mengangkat tangan menahan lengan jaketmu."
            miyuki "Jangan kasih petunjuk dulu, Yutaka-kun. Biar aku cari sendiri letak lupaku."
            nar "Ia menunduk, mengetuk permukaan meja pelan dengan ujung jarinya sambil menyusun ulang urutan logika kasusnya tanpa suara."
            miyuki "...Oh, benar! Harus pastikan dulu jenis kandungan obat, total miligram yang masuk, sama jam terakhir diminum sebelum menentukan observasi lanjutan. Tadi aku kelewat langsung lompat ke langkah belakang gara-gara buru-buru."
            yutaka "Nah, cocok persis sama coretan merah pembimbingmu di sini."
            miyuki "Syukurlah ketemu juga celahnya. Kalau cuma kubaca ulang dalam hati, pasti bagian itu bakal kulompati lagi besok."
            nar "Kalian menyelesaikan seluruh tiga halaman satu pertanyaan demi satu pembahasan tanpa terburu-buru, hingga jam tangan kulit di pergelangan kirimu tepat menandai empat puluh menit dan kamu menutup bukunya."
            yutaka "Waktu habis, Senpai. Tiga halaman sudah beres semua, sisanya tinggal tidur yang cukup."
            miyuki "Terima kasih banyak ya, Yutaka-kun. Tadi ketakutanku kayak meluas ke mana-mana, tapi setelah dipecah jadi soal satu per satu bareng kamu begini, akhirnya terasa lebih bisa dihadapi."
            yutaka "Besok pasti lancar, Senpai. Yuk beresin mejanya."
            nar "Bahu Miyuki turun jauh lebih santai saat ia merapikan alat tulis dan memasukkan bukunya ke dalam tas."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Melihat kelopak mata Miyuki yang mulai tampak berat di bawah cahaya ruang belajar, kamu menutup perlahan tepi buku catatannya dan tersenyum mengajak."
            chiasa "Tutup dulu catatannya sebentar yuk, Tachibana-senpai. Kalau kepala terus diisi hafalan tanpa berhenti, nanti besok pagi malah makin gampang lupa semua. Kita jalan keluar sebentar ke mesin minuman depan taman biar cari angin."
            nar "Miyuki sempat melirik tiga halaman berpenanda di hadapannya dengan ragu, lalu langsung mengangguk ramah seperti kebiasaannya setiap kali seseorang mengajaknya."
            miyuki "Oh... iya juga ya. Aku memang sudah duduk di kursi ini hampir dua jam tanpa berdiri. Sebentar ya, Chiasa-chan, kubawa tasku dulu."
            nar "Kalian melangkah keluar dari ruang belajar menuju selasar terbuka di samping Gedung Kedokteran dan membeli dua kaleng teh hangat dari mesin penjual otomatis."
            chiasa "Tadi di gedung sebelah, dosen baru kelas semester ini sampai bawa penggaris sendiri cuma buat ngecek jarak meja anak-anak lho, Senpai. Satu ruangan sampai nggak berani geser kursi sedikit pun."
            miyuki "Haha, wah, teliti sekali ya dosennya... pasti suasana kelasnya langsung sunyi."
            nar "Meski Miyuki menyahut dengan senyum sopan, baru dua puluh langkah menjauh dari pintu gedung, matanya sudah kembali menoleh ke arah tas jinjing di lengannya, lalu turun memeriksa jam tangan kecil di pergelangan kirinya."
            chiasa "Tachibana-senpai? Dari tadi Senpai lihat jam tangan terus. Lagi mikirin tiga halaman catatan tadi ya?"
            nar "Langkah Miyuki melambat di depan bangku kayu dekat taman. Ia menggenggam kaleng teh hangatnya dengan kedua tangan, lalu menoleh kepadamu dengan raut agak bersalah."
            miyuki "Maaf banget ya, Chiasa-chan, aku jadi kelihatan nggak fokus dengerin ceritamu... sebenarnya aku mau istirahat, tapi hatiku belum bisa tenang kalau pergi terlalu lama. Besok benar-benar hari pertama klinik dimulai."
            chiasa "Oh... maaf ya, Senpai, aku malah narik Senpai keluar pas lagi butuh persiapan."
            miyuki "Nggak kok, sama sekali bukan salahmu! Teh hangat ini beneran enak, dan aku senang banget kamu mampir ngajak ngobrol. Cuma kalau boleh, setelah teh ini habis, aku balik sebentar lagi ke atas buat menyelesaikan satu halaman terakhir ya?"
            chiasa "Iya, tentu aja boleh, Senpai. Yuk kita balik pelan-pelan biar Senpai nggak kepikiran terus."
            nar "Kalian berjalan kembali ke ruang belajar beberapa menit kemudian. Meski Miyuki berkali-kali mengucapkan terima kasih atas teh hangatnya, kamu bisa melihat sepanjang waktu istirahat singkat tadi pikirannya tetap tertinggal di atas meja belajar, menghitung menit yang terpakai sebelum ia diizinkan kembali menyiapkan dirinya."
        else:
            nar "Melihat kening Miyuki yang mulai tegang menatap deretan tulisan kecil itu, kamu mengetuk pelan tepi mejanya dan menyodorkan ajakan santai."
            yutaka "Tutup dulu bukunya sebentar yuk, Tachibana-senpai. Kalau kepala terus dipaksa menghafal tanpa jeda, nanti malah makin susah masuk. Kita turun sebentar beli kopi atau teh hangat di mesin depan taman biar kena angin luar."
            nar "Miyuki melirik tiga halaman berpenanda di depannya selama satu detik dengan ragu, lalu tetap mengangguk lembut karena enggan menolak ajakanmu."
            miyuki "Iya juga sih... aku sudah duduk di sini hampir dua jam tanpa istirahat. Tunggu sebentar ya, Yutaka-kun, kuambil tasku dulu."
            nar "Kalian berjalan keluar menuju selasar terbuka samping gedung dan mengambil dua kaleng minuman hangat dari mesin penjual otomatis."
            yutaka "Tadi waktu aku lewat kantin utama, anak-anak panitia orientasi kampus sampai rebutan meja gara-gara mahasiswa baru penuh banget. Tahun lalu nggak seramai ini deh rasanya."
            miyuki "Haha, iya ya, tahun ini jumlah mahasiswa barunya memang kelihatan lebih banyak..."
            nar "Meski ia menyahut dengan senyum ramah, baru beberapa puluh langkah meninggalkan pintu gedung, pandangan Miyuki sudah tiga kali turun melirik tas jinjing berisi buku catatannya dan mengecek jarum jam di pergelangan tangannya."
            yutaka "Tachibana-senpai nggak beneran tenang di luar sini, kan? Dari tadi matamu balik terus ke tas sama jam tangan."
            nar "Langkah Miyuki langsung berhenti di tepi bangku kayu dekat taman. Ia memegangi kaleng teh hangatnya dengan kedua tangan, menatapmu dengan raut agak bersalah."
            miyuki "Ketahuan ya... maaf banget, Yutaka-kun. Aku sebenarnya pengin istirahat bareng kamu, tapi belum bisa tenang kalau pergi terlalu lama. Besok benar-benar hari pertama klinik dimulai."
            yutaka "Oke, salahku juga langsung narik Senpai keluar pas lagi butuh persiapan. Nggak usah sungkan, ayo balik ke atas sekarang aja biar kepalamu tenang."
            miyuki "Maaf ya jadi memotong waktumu, tapi terima kasih banyak buat teh hangatnya, Yutaka-kun."
            nar "Kamu berjalan mengantarnya kembali ke ruang belajar. Niatmu memberi jeda singkat memang diterima dengan sopan, sementara terlihat jelas di matanya bahwa sepanjang menit di luar tadi ia justru kesulitan menikmati apa pun sebelum tahu kapan ia boleh kembali membuka catatannya."
    else:
        if kk_host == "chiasa":
            nar "Kamu melirik tumpukan buku tebal dan tiga halaman bertanda warna-warni itu, lalu memilih tidak menyita waktu persiapannya menjelang hari penting besok. Kamu merapikan tali tas kainmu di bahu sambil tersenyum tenang."
            chiasa "Kalau begitu aku nggak mau ganggu konsentrasi Senpai lebih lama lagi ya. Besok hari pertama yang penting banget. Sebelum aku pergi, ada barang atau minuman yang perlu kuambilkan dulu dari bawah?"
            nar "Refleks pertama Miyuki langsung menggeleng halus sambil mengangkat satu tangan."
            miyuki "Eh, nggak usah repot-repot, Chiasa-chan. Aku nggak butuh apa-apa kok, sungguh."
            nar "Kamu tidak langsung berbalik pergi. Kamu menunggu dua detik dengan santai sambil melirik botol plastik kosong yang sejak tadi tergeletak di sisi kanan kotak pensilnya. Melihat pandanganmu, Miyuki akhirnya terhenti, rona tipis muncul di pipinya, lalu ia tertawa kecil malu-malu."
            miyuki "...Sebenarnya tenggorokanku agak kering dari tadi siang. Kalau memang kamu lewat tangga depan mesin penjual otomatis, boleh aku titip sebotol air mineral biasa aja? Ini uangnya..."
            chiasa "Simpan aja uangnya, Senpai, cuma air mineral kok. Tunggu dua menit ya, aku turun sebentar."
            nar "Kamu bergegas turun ke lantai satu, membeli sebotol air mineral dingin dari mesin penjual otomatis, lalu kembali meletakkannya perlahan di sisi kanan mejanya agar tidak mengganggu ruang geraknya."
            miyuki "Terima kasih banyak, Chiasa-chan. Maaf jadi merepotkan padahal kamu sudah mau pulang."
            chiasa "Sama sekali nggak repot kok. Semangat buat hari pertama klinik besok ya, Tachibana-senpai."
            nar "Miyuki melingkarkan jemarinya di sekeliling botol dingin itu, menatapmu dengan sorot mata cokelat kemerahan yang hangat dan sedikit ragu."
            miyuki "Chiasa-chan... besok kalau jadwal praktik hari pertamaku sudah selesai, boleh ya aku kirim pesan kasih kabar? Nggak perlu kamu selalu luangkan waktu atau langsung balas kok, aku cuma ingin ada seseorang yang tahu hariku berjalan seperti apa."
            chiasa "Boleh banget dong, Senpai. Kapan pun selesai, kirim pesan aja, pasti kubaca kok."
            miyuki "Hehe, terima kasih ya. Hati-hati di jalan pulang."
            nar "Kamu melambai pelan dan melangkah keluar ruang belajar. Menoleh sekali melalui kaca pintu, kamu melihat Miyuki sudah membuka kembali catatannya dengan tenang, menapaki hari-hari sibuk tahun keempat di mana waktu berdua kini harus berbagi tempat dengan jadwal yang semakin padat."
        else:
            nar "Kamu melirik tiga halaman berpenanda itu lalu memutuskan menghormati waktu persiapannya menjelang hari penting besok. Kamu merapikan tali tas selempangmu di bahu sambil tersenyum ringan."
            yutaka "Kalau gitu aku nggak ganggu jam belajarmu ya, Tachibana-senpai. Sebelum aku turun, ada barang atau minuman yang perlu kuambilkan dulu dari lantai bawah?"
            nar "Refleks pertama Miyuki segera menggeleng sambil mengangkat tangannya sopan."
            miyuki "Nggak usah repot-repot, Yutaka-kun. Aku baik-baik aja kok, sungguh."
            nar "Kamu tetap berdiri sebentar di pinggir meja, lalu mengangkat dagu singkat menunjuk ke arah botol plastik kosong yang sejak tadi berdiri di sebelah kotak pensilnya."
            yutaka "Botol di samping catatanmu sudah kosong melompong tuh, Senpai. Mau air mineral atau teh tawar?"
            nar "Miyuki terhenti, melirik botol kosongnya sendiri, lalu tersenyum malu-malu dengan rona tipis di kedua pipinya."
            miyuki "Ketahuan juga ya... sebenarnya tenggorokanku agak kering dari tadi. Kalau nggak merepotkan, air mineral biasa aja deh. Sebentar kuambilkan uangnya..."
            yutaka "Simpan aja uangnya, Senpai, cuma sebotol air. Tunggu dua menit ya."
            nar "Kamu turun cepat ke mesin penjual otomatis di dekat tangga lantai satu, lalu kembali menaruh sebotol air mineral dingin dengan pelan di sisi kanan meja tanpa memotong fokusnya."
            miyuki "Terima kasih banyak, Yutaka-kun. Maaf jadi bikin kamu bolak-balik tangga."
            yutaka "Santai aja. Semangat buat hari pertama klinik besok ya, Tachibana-senpai."
            nar "Miyuki menggenggam botol dingin itu dengan kedua tangannya, lalu menatapmu dengan mata cokelat kemerahan yang hangat."
            miyuki "Yutaka-kun... besok kalau hari pertama klinikku sudah selesai, aku kirim pesan kasih kabar ya? Nggak perlu kamu langsung balas atau luangkan waktu terus kok, aku cuma ingin ada seseorang yang tahu hariku sudah lewat."
            yutaka "Kirim aja kapan pun, Senpai. Kalau aku masih bangun pasti langsung kubalas."
            miyuki "Hehe, terima kasih. Hati-hati pulangnya, Yutaka-kun."
            nar "Kamu mengangkat satu tangan pamit lalu melangkah keluar ruang belajar. Dari balik kaca pintu, kamu melihat Miyuki sudah kembali membuka buku catatannya dengan tenang, memulai masa sibuk tahun keempat yang menuntut waktu kalian kini lebih pandai berbagi ruang."
    return

# ┌─ PANDUAN CERITA · Mi13 · Telepon Ibu
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : tekanan dari orang tua.
# │ INTI    : A dengarkan / B tegur ibunya / C alihkan.
# │ AKHIRAN : kelelahan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi13:
    call kk_scene_enter("miyuki","Rumah Sakit Tachibana")
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Kantin sudut di lantai satu Rumah Sakit Tachibana sudah hampir kosong di bawah sorot lampu putih yang agak redup. Hanya bunyi dengung pelan lemari pendingin minuman dan langkah jauh seorang perawat di koridor luar yang menemani suasana."
        elif kk_slot == 2:
            nar "Cahaya sore miring masuk melalui kaca lebar kantin sudut Rumah Sakit Tachibana yang mulai sepi. Sinar jingga tipis jatuh di atas meja plastik putih yang bersih, berbaur dengan aroma kaldu hangat dari dapur kantin yang bersiap tutup."
        else:
            nar "Di sudut tenang kantin Rumah Sakit Tachibana yang tidak terlalu padat, kamu memilih meja dekat jendela kaca yang menghadap taman kecil halaman depan. Obrolan pelan beberapa staf medis di meja seberang terdengar samar di kejauhan."
        nar "Kamu baru saja menaruh dua botol teh jelai hangat di atas meja ketika Tachibana Miyuki melangkah menghampiri sambil membawa kotak makan terbungkus kain krem. Jas dokter putihnya tampak agak kusut di bagian siku, stetoskop tersampir rapi di lehernya, dan lingkaran lelah tipis mulai tampak di bawah mata cokelat kemerahannya."
        miyuki "Maaf banget bikin kamu nunggu di bawah, Chiasa-chan. Tadi ada pasien anak di bangsal tiga yang agak rewel waktu pemeriksaan rutin, jadi aku baru bisa lepas sebentar sekarang."
        chiasa "Nggak apa-apa banget, Tachibana-senpai, aku juga baru duduk kok. Nih, teh jelai hangatnya. Gimana rotasi bangsal minggu ini, masih bikin kaki pegal terus?"
        nar "Miyuki duduk di seberangmu sambil mengembuskan napas lega pelan, lalu menyisir rambut hitam panjangnya yang lurus terurai melewati bahu jas dokternya."
        miyuki "Lumayan banget, Chiasa-chan. Rasanya tiap habis keliling lantai tiga, semua catatan istilah medis di kepalaku ikut berpencar ke mana-mana. Untung tadi pagi aku masih sempat bikin bekal telur gulung sama sayur rebus biar nggak makan roti kering terus."
        chiasa "Hebat banget masih sempat masak sendiri! Sekarang makan dulu yuk mumpung masih hangat, jeda istirahat Senpai cuma dua puluh menit kan?"
        miyuki "Iya, makasih banyak sudah mau mampir nemenin aku duduk sebentar, Chiasa-chan. Selamat makan ya."
        nar "Baru saja Miyuki membuka tutup kotak makan hangatnya, mengepulkan uap tipis dari nasi dan lauk rumahan di dalamnya, lalu mengangkat sendok dengan senyum yang akhirnya tampak benar-benar santai, ponsel di dekat botol tehnya bergetar keras di atas meja. Di layar menyala satu nama, Ibu."
        nar "Gerakan sendok Miyuki langsung terhenti di udara."
        chiasa "Tachibana-senpai? Mau makan beberapa suap dulu aja atau diangkat sekarang?"
        miyuki "Bentar ya, Chiasa-chan... takutnya ada urusan mendadak di rumah atau kabar penting dari Ayah di ruang operasi."
        nar "Miyuki menggeser tombol jawab dan menempelkan ponsel ke telinga kanannya. Akan tetapi, di dalam sudut kantin yang sunyi ini, suara anggun sekaligus tajam milik Tachibana Sayuri di seberang sambungan terdengar cukup jelas bahkan dari kursimu."
        "Ibu Miyuki" "Miyuki, kenapa pesan Ibu kemarin sore soal jamuan akhir bulan di hotel belum juga kamu balas? Keluarga rekanan Ayahmu sudah memastikan hadir semua. Ibu paling tidak suka kalau pihak rumah sakit sampai menunggu konfirmasi dari keluarga kita sendiri."
        miyuki "Ibu, maaf... dua hari ini jadwal rotasi bangsal padat sekali, aku baru sempat membuka ponsel di ruang istirahat..."
        "Ibu Miyuki" "Anak bungsu keluarga Morita saja yang baru tahun ketiga kedokteran sudah aktif mendampingi ayahnya di seminar rumah sakit mereka, sementara kamu yang sudah masuk tahun keempat malah sudah hampir tiga minggu belum juga pulang ke rumah."
        miyuki "Ibu, aku masih di rumah sakit habis keliling bangsal anak. Baru banget sempat duduk mau makan..."
        "Ibu Miyuki" "Justru karena kamu sudah masuk tahun keempat, jadwal harus diatur jauh lebih tertib daripada mahasiswa biasa, Miyuki. Semua ini demi masa depanmu sendiri nanti. Ibu sudah mengirim daftar tanggal makan malam keluarga ke pesanmu. Jangan buat Ibu harus mengingatkan dua kali."
        miyuki "...Iya, Ibu. Aku dengar. Nanti sepulang dari rumah sakit kuperiksa lagi jadwal jagaku lalu langsung kukabari."
        nar "Tangan Miyuki perlahan menurunkan sendok kembali ke pinggir kotak makannya. Punggungnya menegang tegak seperti sedang menerima teguran di depan penguji, dan sementara ia terus mengulang kalimat iya dan paham berkali-kali, uap hangat dari nasi serta telur gulung di kotak yang terbuka itu perlahan menghilang tanpa tersentuh."
        chiasa "{i}Baru sebulan mulai klinik dan dia sudah secapek ini... ibunya bahkan nggak sempat nanya sekali pun dia lagi capek atau sudah makan belum.{/i}"
    else:
        if kk_slot >= 3:
            nar "Sudut kantin di lantai satu Rumah Sakit Tachibana sudah hampir lengang di bawah pendar lampu putih yang tenang. Hanya bunyi dengung pelan lemari pendingin minuman dan langkah jauh seorang perawat di koridor luar yang memecah kesunyian."
        elif kk_slot == 2:
            nar "Cahaya sore condong masuk melewati jendela kaca lebar kantin sudut Rumah Sakit Tachibana yang mulai sepi. Sinar jingga tipis memantul di atas meja plastik putih yang bersih, berbaur dengan aroma kaldu hangat dari dapur kantin yang bersiap tutup."
        else:
            nar "Di sudut tenang kantin Rumah Sakit Tachibana yang tidak terlalu ramai, kamu memilih meja dekat jendela kaca yang menghadap taman kecil halaman depan. Suara obrolan pelan beberapa staf medis di meja seberang terdengar samar di kejauhan."
        nar "Kamu menaruh dua botol teh jelai hangat di atas meja tepat ketika Tachibana Miyuki melangkah menghampiri dengan membawa kotak makan berbalut kain krem. Jas dokter putihnya tampak agak kusut di bagian siku, stetoskop tersampir rapi di lehernya, dan di bawah mata cokelat kemerahannya mulai terlihat bayangan lelah tipis."
        miyuki "Maaf banget bikin kamu nunggu di bawah, Yutaka-kun. Tadi pasien anak di bangsal tiga sempat rewel waktu pemeriksaan rutin, jadi aku baru bisa lepas sebentar sekarang."
        yutaka "Santai aja, Tachibana-senpai, aku juga baru sampai kok. Nih, teh hangatnya. Gimana rotasi bangsal minggu ini, masih bikin kaki pegal terus?"
        nar "Miyuki duduk di seberangmu sambil mengembuskan napas lega pelan, lalu merapikan rambut hitam panjangnya yang lurus terurai melewati bahu jas dokternya."
        miyuki "Lumayan banget, Yutaka-kun. Rasanya tiap habis keliling lantai tiga, catatan istilah medis di kepalaku langsung ikut lari ke mana-mana. Untung tadi pagi aku sempat nyiapin bekal telur gulung sama sayur rebus biar nggak makan roti kering melulu."
        yutaka "Bagus dong, sekarang makan dulu mumpung masih hangat. Jeda istirahatmu cuma dua puluh menit kan?"
        miyuki "Iya, terima kasih banyak sudah mau mampir nemenin aku duduk sebentar, Yutaka-kun. Selamat makan ya."
        nar "Baru saja Miyuki membuka tutup kotak makan hangatnya, mengepulkan uap tipis dari nasi dan lauk rumahan di dalamnya, lalu mengangkat sendok dengan senyum yang akhirnya tampak benar-benar santai, ponsel di dekat botol tehnya bergetar nyaring di atas permukaan meja. Di layar menyala satu nama, Ibu."
        nar "Gerakan sendok Miyuki langsung membeku di udara."
        yutaka "Tachibana-senpai? Mau makan dulu aja beberapa suap atau mau diangkat sekarang?"
        miyuki "Sebentar ya, Yutaka-kun... takutnya ada urusan mendadak di rumah atau kabar penting dari Ayah di ruang operasi."
        nar "Miyuki mengusap tombol terima dan menempelkan ponsel ke telinga kanannya. Di sudut kantin yang sunyi ini, suara anggun sekaligus tajam milik Tachibana Sayuri di seberang sambungan terdengar cukup jelas bahkan dari kursimu."
        "Ibu Miyuki" "Miyuki, kenapa pesan Ibu kemarin sore mengenai jamuan akhir bulan di hotel belum juga kamu balas? Keluarga rekanan Ayahmu sudah memastikan hadir semua. Ibu paling tidak suka kalau pihak rumah sakit sampai menunggu konfirmasi dari keluarga kita sendiri."
        miyuki "Ibu, maaf... dua hari ini jadwal rotasi bangsal padat sekali, aku baru sempat membuka ponsel di ruang istirahat..."
        "Ibu Miyuki" "Putra bungsu keluarga Morita saja yang baru masuk tahun ketiga kedokteran sudah rutin mendampingi ayahnya di seminar rumah sakit mereka, sementara kamu yang sudah menginjak tahun keempat malah hampir tiga minggu belum juga pulang ke rumah."
        miyuki "Ibu, aku masih di rumah sakit habis keliling bangsal anak. Baru banget sempat duduk mau makan..."
        "Ibu Miyuki" "Justru karena kamu sudah masuk tahun keempat, jadwal harus diatur jauh lebih disiplin daripada mahasiswa biasa, Miyuki. Semua ini demi masa depanmu sendiri nanti. Ibu sudah mengirim daftar tanggal makan malam keluarga ke pesanmu. Jangan buat Ibu harus mengingatkan dua kali."
        miyuki "...Iya, Ibu. Aku dengar. Nanti sepulang dari rumah sakit kuperiksa lagi jadwal jagaku lalu langsung kukabari."
        nar "Jemari Miyuki perlahan menurunkan sendok kembali ke pinggir kotak makannya. Punggungnya menegak kaku seperti sedang menerima teguran di depan penguji, dan sementara ia terus mengulang kalimat iya dan paham berkali-kali, uap hangat dari nasi serta telur gulung di kotak yang terbuka itu perlahan menghilang tanpa sempat tersentuh."
        yutaka "{i}Nada halus tapi dingin yang dibungkus alasan demi masa depan... persis banget kayak gaya telepon rumah Kisaragi. Ibunya bahkan nggak nanya sekali pun dia lagi capek atau sudah makan belum.{/i}"
    call kk_family_menu("Mi13", ["Tunggu dengan tenang sampai telepon selesai, lalu tanyakan apakah ia mau cerita.", "Minta izin menyela di telepon dan katakan kepada ibunya agar memberi Miyuki waktu istirahat.", "Segera alihkan pembicaraan ke topik ringan setelah ia menutup telepon."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu memilih tidak memotong panggilan itu ataupun membuat situasi di telepon semakin menegangkan. Kamu duduk tenang di seberangnya, memutar tutup botol teh jelai hangat lalu menggesernya sedikit lebih dekat ke jangkauan tangan Miyuki sementara suara Sayuri terus mengalir selama tiga menit penuh."
            nar "Begitu layar ponselnya akhirnya padam, Miyuki menaruhnya pelan di samping baki. Untuk sesaat ia hanya memandangi layar hitam itu, lalu menyandarkan punggung ke sandaran kursi plastik dengan embusan napas panjang."
            chiasa "Tachibana-senpai nggak apa-apa? Kalau Senpai lagi pengin cerita soal telepon barusan, aku dengerin kok. Kalau mau minum dulu terus diam sebentar juga boleh banget."
            nar "Refleks pertamanya sempat mencoba menarik sudut bibir menjadi senyum senpai yang selalu terlihat rapi dan tenang."
            miyuki "Nggak apa-apa kok, Chiasa-chan, maaf ya jadi bikin suasana istirahat nggak enak. Cuma soal jadwal jamuan keluarga biasa aja, Ibu memang paling teliti kalau soal acara rekanan Ayah..."
            nar "Kamu tidak buru-buru mengiyakan topengnya ataupun mengalihkan topik. Kamu tetap duduk tenang menatapnya sampai Miyuki sadar ia tidak perlu berpura-pura kuat di meja ini. Perlahan, senyum tipis itu turun, dan kedua bahu Miyuki ikut meluruh."
            miyuki "...Sebenarnya, aku cuma ingin satu hari nanti ponselku berbunyi karena Ibu memang ingin mendengar suaraku. Hanya nanya aku lagi capek atau nggak di bangsal, atau hari ini sempat makan enak atau belum. Tidak langsung memeriksa apakah jadwal hidupku sudah berjalan sesuai rencana beliau."
            nar "Begitu kalimat pelan itu meluncur, mata cokelat kemerahan Miyuki langsung turun menatap kotak makannya yang sudah tidak lagi mengepulkan uap. Rona malu tipis merambat di pipinya."
            miyuki "Aduh... maaf ya, Chiasa-chan. Kedengarannya kayak keluhan anak kecil yang nggak tahu terima kasih banget ya? Padahal Ayah sama Ibu kan memang super sibuk mengurus rumah sakit dan selama ini selalu kasih fasilitas terbaik buatku..."
            chiasa "Sama sekali nggak kekanak-kanakan kok, Senpai. Pengin ditanyain kabar sama orang tua sendiri tanpa bahas jadwal jamuan atau perbandingan sama anak kenalan itu hal paling wajar di dunia."
            miyuki "Tapi kan beliau juga melakukan semua itu demi masa depanku..."
            chiasa "Mungkin iya, tapi tetap aja bikin sesak kan kalau tiap diangkat isinya cuma tagihan jadwal? Senpai nggak perlu langsung minta maaf cuma gara-gara jujur bilang capek."
            nar "Miyuki mengangkat wajah menatapmu cukup lama, lalu sorot matanya perlahan menghangat."
            miyuki "...Kamu tuh kelihatannya tenang banget ya, Chiasa-chan. Terima kasih sudah nggak buru-buru nyuruh aku semangat lagi."
            chiasa "Kalau lagi lelah ya memang boleh istirahat dulu, Senpai. Tadi di bangsal anak ada kejadian yang bikin pusing banget ya?"
            miyuki "Ada satu anak umur enam tahun yang takut banget disuntik, terus pembimbingku sempat menegur karena catatanku agak telat lima menit... rasanya hari ini agak panjang aja."
            nar "Kamu tidak memotong ataupun menceramahinya; kamu tetap duduk mendengarkan ketika ia pelan-pelan bercerita tentang betapa melelahkannya minggu pertama rotasi bangsal sampai ia akhirnya berhenti mengecilkan keluhannya sendiri, meneguk teh hangatmu, dan kembali mengangkat sendoknya untuk makan."
        else:
            nar "Kamu memilih tidak menyela panggilan itu ataupun memperkeruh suasana di ujung sambungan. Kamu duduk tenang di seberang meja, memutar tutup botol teh jelai hangat lalu menggesernya sedikit lebih dekat ke jangkauan tangan Miyuki sementara suara Sayuri terus mengalir selama tiga menit penuh."
            nar "Begitu layar ponselnya akhirnya padam, Miyuki meletakkannya perlahan di sisi baki. Untuk sesaat ia hanya memandangi layar hitam itu, lalu menyandarkan punggung ke kursi plastik sambil mengembuskan napas panjang."
            yutaka "Tachibana-senpai nggak apa-apa? Kalau Senpai pengin cerita soal telepon tadi, aku dengerin kok. Kalau mau minum dulu terus diam sebentar juga santai aja."
            nar "Kebiasaan lamanya sempat mendorong sudut bibirnya membentuk senyum senpai yang selalu terlihat rapi dan tenang."
            miyuki "Nggak apa-apa kok, Yutaka-kun, maaf jadi bikin suasana makan nggak enak ya. Cuma urusan jadwal jamuan keluarga biasa aja, Ibu memang paling teliti kalau soal acara rekanan Ayah..."
            nar "Kamu tidak langsung mengangguk menerima penjelasan itu, juga tidak buru-buru mengalihkan topik. Kamu hanya tetap duduk tenang di depannya sampai Miyuki sadar ia tidak perlu berpura-pura kuat di meja ini. Perlahan, senyum rapi itu meluruh, dan kedua bahunya ikut turun."
            miyuki "...Sebenarnya, aku cuma ingin satu hari nanti ponselku berbunyi karena Ibu memang ingin mendengar suaraku. Sekadar nanya aku lagi capek atau nggak di bangsal, atau hari ini sempat makan enak atau belum. Tidak langsung memeriksa apakah jadwal hidupku masih berjalan sesuai rencana beliau."
            nar "Begitu pengakuan pelan itu terlepas, mata cokelat kemerahan Miyuki langsung turun menatap kotak makannya yang sudah tidak lagi mengepulkan uap. Rona malu tipis merambat di pipinya."
            miyuki "Aduh... maaf ya, Yutaka-kun. Kedengarannya kayak keluhan anak kecil yang nggak tahu terima kasih banget ya? Padahal Ayah sama Ibu kan memang super sibuk mengurus rumah sakit dan selama ini selalu kasih semua fasilitas terbaik buatku..."
            yutaka "Nggak kekanak-kanakan sama sekali, Senpai. Pengin ditelepon orang tua sendiri buat ditanyain kabar tanpa embel-embel jadwal jamuan atau perbandingan sama anak kenalan itu hal paling normal di dunia."
            miyuki "Tapi kan beliau juga melakukan semua itu demi masa depanku..."
            yutaka "Mungkin iya, tapi tetap aja bikin sesak kan? Aku sendiri tahu persis gimana rasanya angkat telepon dari rumah yang isinya cuma pemeriksaan target bulanan. Jadi Senpai nggak perlu langsung minta maaf ke aku cuma gara-gara jujur bilang capek."
            nar "Miyuki mengangkat wajah menatapmu cukup lama, seolah baru menyadari bahwa di seberangnya duduk seseorang yang sungguh-sungguh mengerti jenis kelelahan yang ia simpan. Matanya perlahan menghangat."
            miyuki "...Kamu beneran jeli banget ya, Yutaka-kun. Terima kasih sudah nggak buru-buru nyuruh aku semangat lagi."
            yutaka "Kalau lagi lelah ya memang boleh lelah dulu. Terus tadi di bangsal anak ada kejadian yang bikin pusing banget?"
            miyuki "Ada satu anak umur enam tahun yang takut banget disuntik, terus pembimbingku ikut menegur karena catatanku agak telat lima menit... rasanya hari ini agak panjang aja."
            nar "Kamu tidak menyela ataupun memberinya nasihat berlebihan; kamu tetap duduk mendengarkan ketika Miyuki pelan-pelan bercerita tentang kelelahan minggu pertamanya di klinik, sampai ia berhenti mengecilkan perasaannya sendiri, meraih botol teh hangatmu, dan akhirnya mengangkat sendok untuk mulai makan."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Melihat nasi dan telur gulung di kotak Miyuki makin dingin sementara suara tajam di seberang belum juga memberinya ruang bernapas, kamu mencondongkan badan sedikit melintasi meja dan berbicara dengan nada sopan yang jelas tepat saat ada jeda napas di sambungan."
            chiasa "Maaf sekali menyela pembicaraannya, Tachibana-san. Saya Amamiya Chiasa, junior Tachibana-senpai dari Universitas Kouseikan. Kebetulan Tachibana-senpai baru saja keluar dari jam rotasi bangsal dan baru sempat duduk untuk makan. Boleh kiranya Tachibana-senpai diberi waktu sebentar dulu untuk makan dan beristirahat?"
            nar "Mata Miyuki melebar kaget menatapmu, tangannya refleks sedikit menarik ponsel menjauh dari telinga. Di seberang telepon langsung turun keheningan kaku selama beberapa detik penuh sebelum suara Tachibana Sayuri kembali terdengar, kali ini terlampau sopan sekaligus menegang dingin."
            "Ibu Miyuki" "...Oh, Amamiya-san rupanya. Terima kasih atas perhatiannya yang begitu sopan, tapi tentu saja saya paling memahami jadwal serta ketahanan putri saya sendiri."
            chiasa "Tentu, Tachibana-san. Saya hanya khawatir waktu istirahatnya habis sebelum sempat makan."
            "Ibu Miyuki" "Kami menghargai perhatian teman kuliahnya, Amamiya-san. Miyuki, Ibu tutup dulu sekarang supaya tidak mengganggu tamumu. Nanti begitu kamu selesai jaga, segera hubungi Ibu kembali tanpa ada yang memotong."
            miyuki "Iya, Ibu. Selamat melanjutkan aktivitas..."
            nar "Sambungan langsung terputus seketika dengan bunyi klik yang terasa nyaring di sudut kantin yang sunyi. Miyuki menurunkan ponselnya ke atas meja dengan jemari yang masih agak tegang, lalu menatapmu dengan campuran rasa terima kasih dan kecemasan yang jujur."
            miyuki "Terima kasih sudah mau membelaku barusan, Chiasa-chan. Aku tahu niatmu benar-benar tulus supaya aku bisa makan tenang sebelum naik ke bangsal lagi."
            chiasa "Maaf kalau tadi aku terlalu lancang langsung menyela, Senpai. Aku cuma nggak tega lihat bekalmu dibiarin dingin terus sementara ibumu nggak berhenti bicara."
            miyuki "Aku nggak marah sama sekali kok, sungguh. Cuma... nanti sepulang jaga tetap aku sendiri yang harus menelepon balik dan menjelaskan panjang lebar ke Ibu kenapa ada orang lain yang ikut berbicara di tengah panggilan keluarga."
            chiasa "...Maaf ya, Senpai, harusnya aku mikirin efek buntutnya dulu sebelum langsung maju bicara."
            miyuki "Jangan dipasang muka bersalah begitu dong, Chiasa-chan. Aku cuma ingin kamu tahu kenapa selama ini aku kadang takut kalau ada yang membelaku langsung di depan Ibu. Kadang diam sampai teleponnya selesai justru terasa lebih aman buatku."
            chiasa "Aku ngerti sekarang, Senpai. Lain kali aku tanya Senpai dulu. Sekarang habisin makannya mumpung jedanya belum habis."
            miyuki "Iya, mumpung masih sisa sepuluh menit, kumakan dulu ya."
            nar "Miyuki akhirnya mengangkat sendok dan mulai menyuap makannya dengan tenang, tetapi ponselnya tetap ia letakkan menghadap ke atas tepat di tepi baki, seolah siap siaga menyambut panggilan susulan kapan saja."
        else:
            nar "Melihat nasi dan telur gulung di hadapan Miyuki terus mendingin sementara suara di ujung sambungan belum juga memberinya celah bernapas, kamu mencondongkan bahu sedikit melintasi meja. Tepat ketika Sayuri mengambil jeda napas singkat, kamu berbicara dengan nada formal yang tenang dan jelas."
            yutaka "Maaf sekali menyela pembicaraannya, Tachibana-san. Saya Kisaragi Yutaka, junior Tachibana-senpai dari Universitas Kouseikan. Kebetulan Tachibana-senpai baru saja keluar dari jam rotasi bangsal dan baru sempat duduk untuk makan. Boleh kiranya Tachibana-senpai diberi waktu sebentar dulu untuk makan dan beristirahat?"
            nar "Mata Miyuki langsung melebar kaget menatapmu, tangannya refleks sedikit menarik ponsel menjauh dari telinga. Di seberang sambungan langsung turun keheningan kaku selama beberapa detik penuh. Ketika suara Tachibana Sayuri kembali terdengar, nadanya berubah terlampau sopan sekaligus menegang dingin."
            "Ibu Miyuki" "...Oh, Kisaragi-san rupanya. Putra keluarga Kisaragi, ya. Terima kasih atas perhatian Anda yang begitu sopan, tetapi tentu saja saya paling memahami jadwal serta ketahanan putri saya sendiri."
            yutaka "Tentu, Tachibana-san. Saya hanya khawatir waktu istirahatnya habis sebelum sempat makan."
            "Ibu Miyuki" "Kami sangat menghargai sopan santun Anda, Kisaragi-san. Miyuki, Ibu tutup dulu sekarang supaya tidak mengganggu tamu kuliahmu. Nanti begitu kamu selesai jaga, segera hubungi Ibu kembali tanpa ada yang memotong."
            miyuki "Iya, Ibu. Selamat melanjutkan aktivitas..."
            nar "Sambungan langsung diputus seketika dengan bunyi klik yang terasa keras di sudut kantin yang sunyi. Miyuki meletakkan ponselnya di tepi meja dengan jemari yang masih agak tegang, lalu mengangkat pandangan menatapmu dengan campuran rasa terima kasih dan kecemasan yang jujur."
            miyuki "Terima kasih sudah mau membelaku barusan, Yutaka-kun. Aku tahu niatmu benar-benar tulus supaya aku bisa makan dengan tenang sebelum masuk bangsal lagi."
            yutaka "Maaf kalau tadi aku kelewatan langsung menyela, Senpai. Aku cuma nggak tega lihat bekalmu dibiarin dingin terus sementara ibumu nggak berhenti ngomong."
            miyuki "Aku nggak marah sama sekali kok, sungguh. Cuma... nanti sepulang jaga tetap aku sendiri yang harus menelepon balik dan menghadapi pertanyaan panjang Ibu soal kenapa ada orang lain, apalagi putra keluarga Kisaragi, yang duduk menemaniku dan ikut bicara di tengah panggilan keluarga."
            yutaka "...Ibuku juga suka begitu tiap ada nama keluarga lain disebut. Salahku juga tadi nggak mikir sampai ke efek buntutnya buat kamu, Senpai."
            miyuki "Jangan dipasang muka bersalah begitu dong, Yutaka-kun. Aku cuma ingin kamu paham kenapa selama ini aku kadang takut kalau ada orang yang membelaku langsung di depan Ibu. Kadang diam sampai teleponnya selesai justru terasa lebih aman buatku."
            yutaka "Aku paham sekarang. Lain kali aku bakal tanya ke kamu dulu sebelum maju bicara. Sekarang habisin dulu mumpung jedamu belum habis."
            miyuki "Iya, mumpung masih sisa sepuluh menit, aku makan dulu ya."
            nar "Miyuki akhirnya mengangkat sendok dan mulai menyuap nasinya dengan tenang, tetapi ponselnya tetap ia biarkan tergeletak menghadap ke atas tepat di samping baki, seolah siap siaga menyambut panggilan susulan kapan saja."
    else:
        if kk_host == "chiasa":
            nar "Begitu panggilan ibunya akhirnya selesai dan Miyuki meletakkan ponsel dengan sorot mata redup, kamu berpikir membahas beban keluarga di tengah jeda singkat hanya akan semakin menguras tenaganya. Kamu segera menyodorkan topik ringan yang jauh dari rumah sakit maupun urusan rumah."
            chiasa "Oh iya, Tachibana-senpai! Kemarin waktu aku jalan pulang lewat dekat pintu timur stasiun, toko roti kecil di pojok gang yang dulu pernah Senpai bilang itu ternyata lagi keluarin menu tart stroberi musiman lho. Antreannya panjang banget sampai meluber ke trotoar depan!"
            nar "Miyuki berkedip satu kali, langsung menangkap usahamu mencairkan suasana. Dalam hitungan detik, senyum lembut seorang senpai kembali terpasang rapi tanpa cela di wajahnya."
            miyuki "Ah, toko roti kecil yang jendelanya kayu cokelat itu ya? Krim kocok mereka memang ringan sekali dan nggak bikin enek sih, pantas langsung diserbu begitu masuk musim stroberi. Jangan-jangan Chiasa-chan lagi kasih kode halus minta Senpai bikin versi rumahan akhir pekan depan nih?"
            chiasa "Haha, ketahuan ya? Tapi beneran kalau Senpai lagi santai aja dong, mana berani nodong kue waktu jadwal klinik lagi sepadat ini."
            miyuki "Tenang aja kok, kalau akhir pekan ada waktu kosong, memanggang tart di dapur apartemen justru bikin kepalaku jauh lebih segar daripada cuma membaca buku teks terus. Chiasa-chan lebih suka kulit bawahnya yang renyah pakai almon atau bolu yang agak lembut?"
            chiasa "Yang renyah pakai almon dong, Senpai, biar nggak terlalu manis!"
            miyuki "Dicatat deh. Tunggu kabar dari Senpai kalau jadwalku sudah agak longgar minggu depan ya."
            nar "Ia mengikutimu dengan sangat mulus, bahkan terus menyelipkan godaan halus agar kamu yakin suasana hatinya sudah kembali cerah. Akan tetapi, sepanjang sepuluh menit obrolan hangat itu mengalir, kamu sempat menangkap sendok di tangan Miyuki lebih sering sekadar mengaduk-aduk permukaan nasi yang dingin daripada benar-benar menyuapkannya ke mulut."
            nar "Ketika alarm kecil di jam tangannya berbunyi menandakan waktu istirahat habis dan ia harus kembali ke bangsal, isi kotak makannya nyaris belum berkurang setengah. Ia menutup kembali tutup plastik kotaknya dengan rapi, membungkusnya lagi dengan kain krem, lalu menatapmu sambil tersenyum tipis yang lelah."
            miyuki "Maaf ya, Chiasa-chan, makanku hari ini lambat sekali sampai malah menyita waktu mampirmu ke kantin. Aku balik ke lantai tiga dulu ya, hati-hati di jalan pulang."
            chiasa "Iya, Senpai... jaga kesehatan ya, jangan sampai telat makan lagi nanti."
            miyuki "Iya, terima kasih sudah mampir, Chiasa-chan."
            nar "Ia melangkah pergi meninggalkan sudut kantin sambil membawa kotak makan yang masih terasa berat di tangannya, kembali menyimpan seluruh kelelahannya di balik keramahan yang tak pernah goyah."
        else:
            nar "Begitu telepon ibunya akhirnya terputus dan Miyuki meletakkan ponsel dengan sorot mata redup, kamu menilai membahas beban keluarga di tengah jeda singkat hanya akan semakin menguras tenaganya. Kamu segera melempar topik ringan yang jauh dari rumah sakit ataupun urusan rumah."
            yutaka "Oh iya, Tachibana-senpai, kemarin waktu aku jalan pulang lewat dekat pintu timur stasiun, toko roti kecil di pojok gang yang dulu pernah Senpai bilang itu lagi keluarin menu tart stroberi musiman. Antreannya panjang banget sampai meluber ke trotoar depan."
            nar "Miyuki mengedip satu kali, langsung menangkap maksudmu mencairkan meja. Dalam hitungan detik, senyum lembut seorang senpai kembali terpasang rapi tanpa cela di wajahnya."
            miyuki "Ah, toko roti kecil yang jendelanya kayu cokelat itu ya? Krim kocok mereka memang ringan sekali dan nggak bikin enek sih, pantas langsung diserbu begitu masuk musim stroberi. Jangan-jangan Yutaka-kun lagi kasih kode halus minta Senpai buatkan versi rumahan akhir pekan depan nih?"
            yutaka "Haha, ketahuan ya? Tapi beneran kalau Senpai lagi luang aja dong. Mana berani aku nagih kue waktu jadwal klinik lagi sepadat ini."
            miyuki "Santai aja kok, kalau akhir pekan ada waktu kosong, memanggang tart di dapur apartemen justru bikin kepalaku jauh lebih segar daripada cuma membaca buku teks terus. Yutaka-kun lebih suka adonan dasar yang renyah pakai almon atau yang agak lembut?"
            yutaka "Yang renyah pakai almon jelas menang lah, biar nggak terlalu manis."
            miyuki "Dicatat deh. Tunggu aja kabar dari Senpai kalau jadwalku sudah agak longgar minggu depan ya."
            nar "Ia menyambut alihan topikmu dengan sangat mulus, bahkan terus menyelipkan godaan halus agar kamu yakin suasana hatinya sudah kembali cerah. Akan tetapi, sepanjang sepuluh menit obrolan hangat itu mengalir, kamu sempat menangkap sendok di tangan Miyuki lebih sering sekadar mengaduk-aduk permukaan nasi yang sudah mendingin daripada benar-benar menyuapkannya ke mulut."
            nar "Ketika alarm pelan di jam tangannya berbunyi menandakan waktu istirahat habis dan ia harus segera kembali ke bangsal, isi kotak makannya nyaris belum berkurang setengah. Ia menutup kembali tutup plastik kotaknya dengan rapi, membungkusnya lagi dengan kain krem, lalu menatapmu sambil tersenyum tipis yang lelah."
            miyuki "Maaf ya, Yutaka-kun, makanku hari ini lambat banget sampai malah menyita waktumu mampir ke kantin. Aku naik ke lantai tiga dulu ya, hati-hati di jalan pulang."
            yutaka "Iya, Senpai... jaga badan baik-baik ya, jangan sampai telat makan lagi nanti."
            miyuki "Iya, terima kasih sudah mampir, Yutaka-kun."
            nar "Ia melangkah meninggalkan sudut kantin sambil menenteng kotak makan yang masih terasa berat di tangannya, kembali menyimpan seluruh kelelahannya di balik keramahan yang terjaga rapi."
    return

# ┌─ PANDUAN CERITA · Mi-D02 · Tertidur di Bahu
# │ LOKASI  : (dinamis — muncul dari kondisi) · TERLIBAT: Tachibana Miyuki
# │ AWALAN  : kelelahan ≥ 60; pemain duduk di dekatnya
# │ INTI    : A Biarkan sampai bangun (dua jam lewat) / B bangunkan / C foto / D pindahkan ke ruang jaga
# │ AKHIRAN : Intim +, kelelahan −5; foto bisa sampai ke Meisa
# └─ tulis / perbaiki dialog di bawah ──
label kk_library_rest(place):
    if not kk_can_sit_with_miyuki(place):
        return
    nar "Di meja baca Perpustakaan Pusat yang lengang, Miyuki sudah membaca paragraf tebal yang sama tiga kali berturut-turut. Pada bacaan keempat, ujung jari telunjuknya berhenti menyusuri baris cetakan. Kelopak matanya perlahan menutup sementara tangannya masih memegangi tepi buku seolah tetap ingin tampak sedang belajar."
    if kk_host == "chiasa":
        chiasa "Tachibana-senpai? Mata Senpai sudah merah banget lho. Istirahat dulu sebentar nggak apa-apa kan?"
        miyuki "Hm... kalau aku merem lima menit aja, tolong jagain bukuku ya, Chiasa-chan. Sebentar aja kok..."
    else:
        yutaka "Tachibana-senpai, dari tadi halaman bukunya nggak pindah-pindah lho. Mending istirahat dulu sebentar daripada dipaksa baca."
        miyuki "Mm... kalau aku tutup mata lima menit, tolong jagain catatanku ya, Yutaka-kun. Sebentar aja..."
    nar "Belum sampai satu menit berselang, bahu Miyuki meluruh pelan lalu kepalanya bersandar ringan di bahumu. Napasnya segera berubah pelan dan teratur sebelum ia sempat menyadari seberapa dekat jarak kalian."
    menu:
        "Tetap duduk sampai ia terbangun.":
            $ kk_record_choice("Mi-D02","A")
            $ kk_minutes(120)
            nar "Kamu memilih tidak bergerak, menggeser napas dan posisi lengan sesedikit mungkin agar sandarannya tidak terganggu. Suara lembaran buku dibalik dan langkah mahasiswa lain silih berganti di lorong rak, sementara di sampingmu Miyuki akhirnya benar-benar lepas dari segala tuntutan selama dua jam penuh."
            nar "Ketika ia akhirnya mengerjap pelan dan menoleh ke jam dinding perpustakaan, wajahnya langsung memerah karena terkejut."
            if kk_host == "chiasa":
                miyuki "Eh... dua jam penuh?! Chiasa-chan, kenapa aku nggak dibangunkan dari tadi?! Bahumu pasti pegal banget ya!"
                chiasa "Nggak apa-apa kok, Tachibana-senpai, aku memang sengaja duduk tenang baca buku juga di sini. Tidurnya nyenyak kan?"
            else:
                miyuki "Dua jam?! Yutaka-kun, kenapa nggak membangunkanku?! Bahumu pasti kaku banget dari tadi!"
                yutaka "Santai aja, Tachibana-senpai, aku sendiri yang memilih tetap duduk di sini kok. Yang penting Senpai sempat tidur beneran."
            miyuki "...Aku tadi hampir mau marah karena nggak dibangunkan, tapi jujur aja... sudah lama banget aku nggak bangun tidur tanpa kepala langsung berdenyut pusing. Terima kasih ya."
        "Bangunkan ia dengan pelan.":
            $ kk_record_choice("Mi-D02","B")
            $ kk_minutes(5)
            if kk_host == "chiasa":
                chiasa "Tachibana-senpai... bangun pelan-pelan ya. Kalau tidur duduk begini nanti leher Senpai malah sakit semua."
            else:
                yutaka "Tachibana-senpai, bangun pelan-pelan dulu ya. Tidur miring di meja perpustakaan nanti lehernya malah kaku."
            nar "Miyuki langsung menegakkan tubuh terlalu cepat begitu membuka mata, pandangannya refleks melirik jam dinding lebih dulu sebelum menoleh ke arahmu."
            miyuki "Aduh, aku beneran ketiduran ya... maaf banget! Aku harus cari tempat istirahat yang benar deh, nggak mungkin lanjut baca dengan mata begini."
            nar "Ia mengusap pipinya dengan raut malu, tetapi untuk sekali ini ia tidak lagi memaksa dirinya menamatkan satu bab lagi dalam keadaan letih."
        "Ambil foto saat ia tertidur.":
            $ kk_record_choice("Mi-D02","C")
            $ kk_flag("foto_miyuki_tertidur")
            $ kk_minutes(5)
            nar "Kamu mengeluarkan ponsel secara diam-diam, mematikan suara rana, lalu memotret wajah Miyuki yang terlelap tenang di bahumu. Tanpa senyum senior yang selalu terjaga, raut wajahnya tampak jauh lebih muda dan rapuh."
            nar "Foto itu tersimpan rapi di galeri ponselmu tanpa pernah meminta persetujuannya. Kamu bisa saja menyebutnya kenangan kecil yang manis, tetapi bila gambar ini suatu hari jatuh ke tangan orang yang salah, Miyuki sendiri yang harus menanggung tatapan dan pertanyaan orang lain."
        "Bantu ia beristirahat di ruang jaga.":
            $ kk_record_choice("Mi-D02","D")
            $ kk_minutes(15)
            if kk_host == "chiasa":
                chiasa "Tachibana-senpai, bangun sebentar yuk. Aku bantu bawakan bukunya, kita pindah ke ruang istirahat klinik biar Senpai bisa rebahan beneran."
            else:
                yutaka "Tachibana-senpai, bangun sebentar ya. Sini tas sama bukunya kubawakan, kuantar ke ruang istirahat klinik supaya Senpai bisa rebahan layak."
            nar "Miyuki mengangguk pasrah dengan kelopak mata masih berat, melangkah pelan di sampingmu dan berhenti satu kali hanya untuk memastikan tidak ada alat tulis yang tertinggal di meja."
            miyuki "Lain kali tolong ingatkan aku lagi ya kalau aku ngotot masih bisa belajar... barusan aku bahkan lupa tadi sedang baca bab apa."
            nar "Begitu sampai di ruang istirahat yang tenang, ia akhirnya membaringkan diri tanpa lagi menyamarkan istirahat sebagai sesi belajar."
    return

init 1 python:
    def kk_begin_miyuki_clinic():
        kk_stage("miyuki",max(2,stage.get("miyuki",0)))

    def kk_study_with_miyuki():
        kk_begin_miyuki_clinic()
        kk_rel("miyuki","trust",3)
        kk_change_medical_career(5)

    def kk_miyuki_nap():
        kk_adj("kelelahan_miyuki",-5)
        kk_rel("miyuki","intim",2)

    _hook("Mi12-A",kk_study_with_miyuki)
    _hook("Mi12-B",kk_begin_miyuki_clinic)
    _hook("Mi12-C",kk_begin_miyuki_clinic)
    for response in "ABC":
        _hook("Mi13-" + response,lambda: kk_adj("kelelahan_miyuki",8))
    _hook("Mi-D02-A",kk_miyuki_nap)
    _hook("Mi-D02-D",kk_miyuki_nap)

# ┌─ PANDUAN CERITA · Mi06 · Rencana Masa Depan
# │ LOKASI  : Kampus Kouseikan · Gedung Kedokteran
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : ia bercerita tentang pediatri.
# │ INTI    : A dukung / B remehkan / C tanyakan Koita.
# │ AKHIRAN : Trust.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi06:
    call kk_scene_enter("miyuki","Gedung Kedokteran")
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Malam itu kamu berjalan beriringan dengan Tachibana Miyuki melewati koridor lantai dasar Gedung Kedokteran yang sudah lengang di bawah sorot lampu putih panjang. Di sepanjang dinding sebelah kiri menuju pintu lobi, terpasang papan pajangan berkaca lebar yang berisi jadwal seminar serta dokumentasi kegiatan mahasiswa."
        else:
            nar "Kamu berjalan beriringan dengan Tachibana Miyuki melewati koridor lantai dasar Gedung Kedokteran yang mulai lengang selepas jam kuliah berakhir. Di sepanjang dinding sebelah kiri menuju pintu lobi, terpasang papan pajangan berkaca panjang yang berisi jadwal seminar serta dokumentasi kegiatan mahasiswa."
        nar "Tepat di bagian tengah papan kaca itu, tertempel belasan kertas gambar penuh coretan krayon warna-warni hasil karya anak-anak dari acara kunjungan relawan di bangsal rumah sakit akhir pekan lalu."
        nar "Langkah Miyuki tiba-tiba melambat, lalu berhenti tepat di depan deretan gambar anak-anak tersebut. Ia menunjuk selembar kertas gambar di baris bawah yang memperlihatkan seekor kucing besar berwarna biru tua dengan enam kaki, mata bulat yang besar sebelah, dan kumis keriting yang lebih panjang daripada tubuhnya."
        nar "Tanpa menoleh untuk memeriksa apakah kamu ikut berhenti atau tidak, Miyuki tersenyum lepas seorang diri memandangi gambar krayon itu."
        chiasa "Lucu banget gambar kucingnya, Tachibana-senpai. Kakinya sampai ada enam begitu, terus kumisnya panjang sekali sampai melewati batas kertas."
        miyuki "Hehe, menggemaskan banget ya, Chiasa-chan? Yang menggambar ini pasien anak laki-laki umur enam tahun waktu acara menggambar bareng relawan hari Sabtu kemarin. Waktu kutanya kenapa kaki kucingnya ada enam, dia jawab dengan muka serius sekali."
        chiasa "Memangnya dia jawab kenapa, Senpai?"
        miyuki "Katanya, kalau kucing biasa kakinya cuma empat, nanti gampang ketangkap waktu dikejar dokter yang bawa jarum suntik. Jadi harus dikasih dua kaki cadangan biar larinya secepat kereta ekspres."
        chiasa "Haha, pintar banget anak umur enam tahun bisa kepikiran alasan kayak gitu. Terus Senpai bilang apa waktu dengar itu?"
        miyuki "Aku bilang kalau begitu kucingnya bakal jadi juara lari se-rumah sakit, tapi tetap harus mampir minum sirup stroberi dulu biar tenaganya nggak habis di tengah jalan. Eh, dia malah langsung tertawa keras sambil menambahkan satu kumis lagi di kertasnya."
        chiasa "Terus gambar bunga matahari besar di sampingnya itu buatan anak yang sama juga?"
        miyuki "Yang itu buatan adik kelas satu SD di ranjang sebelah. Katanya bunga matahari harus digambar tinggi sekali supaya bisa mengintip lewat jendela kamar rawat sampai lantai empat."
        chiasa "Manis sekali ceritanya, Senpai. Rasanya ruangan bangsalnya jadi kelihatan jauh lebih hangat begitu dengar cerita Senpai."
        miyuki "Padahal waktu hari pertama anak laki-laki itu masuk ruang rawat, dia takut banget sampai nggak mau lepas dari jaket ibunya. Aku selalu senang setiap kali lihat anak kecil akhirnya merasa cukup aman buat bercerita atau bercanda seperti itu. Soalnya sering kali orang dewasa di sekitar mereka sudah buru-buru menyuruh diam atau memberi jawaban sebelum anaknya sendiri tahu boleh bertanya apa."
        nar "Miyuki masih memandangi kertas gambar itu beberapa detik lagi, lalu kembali melangkah pelan di sampingmu menuju pintu kaca lobi dengan suara yang tenang dan mantap."
        miyuki "Nanti setelah lulus ujian negara dan selesai masa residensi awal, aku pengin mengambil spesialisasi pediatri, Chiasa-chan. Bukan karena aku membayangkan bekerja di bangsal anak itu bakal selalu lucu dan menyenangkan setiap hari. Justru karena anak-anak punya banyak sekali ketakutan yang harus didengarkan dengan sabar sebelum kita bisa benar-benar mengobati mereka."
    else:
        if kk_slot >= 3:
            nar "Malam itu kamu melangkah keluar menyusuri lobi lantai satu Gedung Kedokteran bersama Tachibana Miyuki di bawah cahaya lampu koridor yang bersih. Di dinding dekat pintu utama, terdapat papan pengumuman kaca berukuran lebar yang memajang laporan kegiatan bakti sosial mahasiswa."
        else:
            nar "Kamu melangkah keluar menyusuri lobi lantai satu Gedung Kedokteran bersama Tachibana Miyuki selepas jam kelas. Di dinding koridor dekat pintu utama, terdapat papan pengumuman kaca berukuran lebar yang memajang laporan kegiatan bakti sosial mahasiswa."
        nar "Di sudut tengah papan tersebut, berjajar kertas-kertas gambar penuh warna krayon buatan pasien anak-anak dari acara relawan rumah sakit minggu lalu."
        nar "Langkah kaki Miyuki melambat lalu terhenti di depan kaca pajangan itu. Ia menunjuk selembar kertas di pojok bawah yang bergambar seekor kucing biru berkaki enam dengan kumis mencuat lebar, lalu tersenyum hangat seorang diri tanpa menoleh dulu ke arahmu."
        yutaka "Kucing biru berkaki enam, Tachibana-senpai? Bebas banget ya imajinasi anak kecil."
        miyuki "Hehe, iya kan, Yutaka-kun? Yang menggambar ini anak umur enam tahun waktu kami mengadakan sesi bermain di bangsal anak hari Sabtu lalu. Waktu kutanya kenapa kakinya ditambah dua, jawabannya serius sekali."
        yutaka "Dia bilang kenapa memangnya, Senpai?"
        miyuki "Katanya supaya kucingnya punya gigi persneling tambahan buat kabur kalau dikejar dokter yang bawa suntikan. Padahal waktu pertama kali datang ke ruang periksa, anak itu menangis terus karena takut lihat jas putih."
        yutaka "Haha, ada-ada aja idenya. Terus Senpai balas apa?"
        miyuki "Aku bilang kalau kucingnya lari secepat kereta, nanti dia cepat haus, jadi harus tetap mampir ke bangsal buat minum obat rasa jeruk. Dia langsung nyengir lebar lalu mewarnai ekornya pakai krayon ungu."
        yutaka "Kalau gambar roket warna hijau di baris atasnya itu?"
        miyuki "Itu gambar anak perempuan kelas satu SD di ranjang seberang. Katanya roketnya mau dipakai menjemput kucing berkaki enam tadi kalau hujan turun."
        yutaka "Pandai sekali Senpai meladeni candaan mereka. Nggak heran anak-anak langsung cepat akrab."
        miyuki "Aku suka sekali momen waktu anak-anak akhirnya berani membuka suara dan bercerita jujur seperti itu. Kadang orang dewasa di sekeliling mereka terlalu sibuk menenangkan dengan kalimat cepat, sampai anaknya sendiri tidak sempat menjelaskan bagian mana yang sebenarnya membuat mereka takut."
        nar "Ia berdiri sejenak lagi menatap deretan gambar krayon itu, lalu kembali berjalan pelan di sebelahmu menuju pintu keluar gedung dengan nada bicara yang terdengar sangat yakin."
        miyuki "Nanti kalau aku sudah lulus, aku ingin masuk spesialisasi pediatri, Yutaka-kun. Bukan karena kupikir merawat anak-anak itu pekerjaan yang ringan atau manis terus. Justru karena di sana ada banyak sekali hal yang harus didengarkan pelan-pelan sebelum mereka bisa ditolong dengan benar."
    call kk_family_menu("Mi06", ["\"Keren banget, Senpai. Selain itu, apa lagi yang bikin Senpai yakin milih pediatri?\"", "\"Kedengarannya agak sederhana ya, Senpai?\"", "\"Koita sudah tahu rencana Senpai mau masuk pediatri ini?\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Keren banget tujuannya, Tachibana-senpai. Selain kejadian waktu acara relawan kemarin, apa lagi yang bikin Senpai yakin banget pengin ambil pediatri?"
            nar "Sorot mata Miyuki langsung berbinar hangat, tampak senang karena kamu menanyakan alasan di balik pilihannya secara sungguh-sungguh."
            miyuki "Kamu beneran mau dengar ceritanya, Chiasa-chan? Kalau begitu kita jalan agak pelan lewat jalur taman samping ya. Kalau sudah mulai bicara soal pediatri, Senpai suka lupa waktu."
            chiasa "Nggak apa-apa kok, Senpai, aku juga lagi nggak buru-buru pulang ke rumah. Cerita aja."
            nar "Sepanjang jalan setapak yang dinaungi pepohonan kamper menuju gerbang depan kampus, Miyuki berbicara dengan antusiasme yang jarang ia perlihatkan saat sedang membahas urusan keluarganya."
            miyuki "Waktu aku mulai ikut observasi klinik semester ini, aku sering lihat anak kecil yang gemetar waktu mau diperiksa, tapi dokter atau orang tuanya cuma bilang, 'Cuma sebentar kok, jangan cengeng.' Padahal buat anak sekecil itu, ketidaktahuan soal apa yang bakal dilakukan ke tubuh mereka itu jauh lebih menakutkan daripada rasa sakitnya sendiri."
            chiasa "Kalau dipikir-pikir iya juga ya, Senpai. Jangankan anak kecil, kita aja kalau tiba-tiba disuruh berbaring tanpa dijelasin mau diapain pasti panik."
            miyuki "Nah, persis itu! Cukup dengan menunjukkan stetoskopnya sebentar dan membiarkan mereka mendengarkan detak jantungnya sendiri, biasanya tangan mereka yang tegang langsung melonggar. Dan bukan cuma pasien anaknya saja yang butuh ditenangkan."
            chiasa "Orang tuanya juga ya, Senpai?"
            miyuki "Iya. Ibu atau ayah yang mengantar mereka sering datang ke rumah sakit dengan wajah pucat karena menyalahkan diri sendiri saat anaknya jatuh sakit. Aku ingin belajar jadi dokter anak yang bisa mendengarkan kecemasan orang tuanya juga tanpa menghakimi mereka."
            chiasa "Tapi jadwal jaga dan beban belajarnya pasti berat banget kan, Senpai?"
            miyuki "Berat banget, jujur aja. Kadang kalau habis baca buku teks patologi sampai tengah malam di apartemen, punggungku rasanya mau patah. Tapi setiap kali aku teringat wajah anak-anak di bangsal kemarin, aku selalu tahu jelas untuk apa aku masih bertahan belajar setiap malam."
            chiasa "Senpai pasti bakal jadi dokter anak yang hebat banget nanti. Anak-anak nggak bakal perlu gambar kucing kaki enam lagi buat kabur dari Senpai."
            miyuki "Haha, kalau mereka masih mau menggambar kucing kaki enam buat ditempel di dinding ruang periksaku, malah senang sekali aku menerimanya."
            chiasa "Kalau nanti ruang periksa Senpai sudah penuh tempelan gambar anak-anak, jangan lupa undang aku mampir lihat ya, Senpai."
            miyuki "Pasti! Nanti khusus buat Chiasa-chan kuberi tempat pajangan paling depan kalau mau menyumbang satu lukisan cat air buat ruang tunggunya."
            chiasa "Janji ya, Senpai! Nanti kugambarkan pemandangan taman bunga yang warnanya cerah supaya anak-anak nggak takut masuk ruang periksa."
            miyuki "Wah, janji itu bakal kutagih begitu aku resmi bertugas di bangsal anak nanti!"
            nar "Miyuki tertawa lepas sambil merapikan tali tas di bahunya, berjalan di sampingmu dengan langkah yang terasa jauh lebih ringan sampai kalian tiba di gerbang utama."
        else:
            yutaka "Pilihan yang keren, Tachibana-senpai. Selain cerita anak yang gambar kucing tadi, apa lagi yang bikin Senpai mantap banget memilih pediatri?"
            nar "Wajah Miyuki langsung tampak berbinar, terkejut sekaligus senang karena kamu tertarik mendengarkan pemikirannya lebih jauh."
            miyuki "Kamu sungguh ingin dengar, Yutaka-kun? Kalau begitu kita jalan santai lewat pelataran samping ya. Senpai bisa bicara panjang lebar kalau sudah ditanya soal ini."
            yutaka "Santai aja, Senpai. Jadwalku kosong kok habis ini."
            nar "Sambil berjalan pelan menyusuri trotoar kampus di bawah pepohonan kamper, Miyuki bercerita dengan nada suara yang hidup dan penuh keyakinan."
            miyuki "Selama ikut kegiatan observasi di rumah sakit, aku sering memperhatikan bagaimana ketakutan pasien anak-anak kadang dianggap remeh oleh orang dewasa. Mereka cuma disuruh diam supaya pemeriksaannya cepat selesai, padahal mereka menangis karena tidak mengerti alat apa yang sedang didekatkan ke mereka."
            yutaka "Masuk akal sih. Orang dewasa aja kadang tegang kalau masuk ruang tindakan tanpa dikasih penjelasan."
            miyuki "Betul sekali. Padahal cuma butuh satu menit untuk menjelaskan cara kerja stetoskop atau membiarkan mereka memegang ujungnya sebentar, suasana ruang periksa langsung berubah total. Belum lagi orang tua yang membawa anak mereka ke ruang gawat darurat malam-malam."
            yutaka "Orang tuanya biasanya malah lebih panik daripada anaknya ya?"
            miyuki "Sering kali jauh lebih panik dan merasa bersalah karena mengira mereka lalai menjaga anaknya. Aku ingin jadi dokter yang punya kesabaran untuk menjelaskan pelan-pelan kepada anak maupun orang tuanya, tanpa bersikap menggurui."
            yutaka "Kedengarannya butuh tenaga dan kesabaran ekstra setiap hari ya, Senpai."
            miyuki "Sangat menguras tenaga memang. Kadang kalau pulang praktik malam, rasanya aku sudah terlalu lelah bahkan untuk memasak makan malam sendiri. Tapi setiap kali aku mengingat tujuan itu, rasa lelahnya jadi punya arti yang jelas."
            yutaka "Bidang itu cocok banget sama pembawaan Senpai. Pasti banyak keluarga pasien yang bakal terbantu nanti."
            miyuki "Terima kasih, Yutaka-kun. Mendengar dukungan seperti itu bikin semangat belajarku malam ini naik lagi."
            yutaka "Kalau bulan depan ada acara bakti sosial lagi di bangsal anak dan butuh tenaga angkat-angkat perlengkapan gambar, kabari saja, Senpai."
            miyuki "Wah, beneran kamu mau bantu angkat kardus krayon sama kertas gambarnya? Nanti anak-anak di bangsal pasti senang kalau ada kakak mahasiswa baru yang ikut mampir."
            yutaka "Asal jangan disuruh ikut lomba gambar kucing berkaki enam saja, gambar tanganku kalah jauh sama anak umur enam tahun."
            miyuki "Hahaha, tenang saja, bagian menggambarnya biar anak-anak yang urus!"
            nar "Miyuki tertawa lembut sambil membetulkan letak tasnya. Meskipun jadwal kuliah tahun ketiganya masih menumpuk, wajahnya tampak sangat cerah saat berjalan bersamamu menuju stasiun."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Kedengarannya agak sederhana ya alasannya, Tachibana-senpai? Tadinya kukira Senpai bakal mengincar spesialisasi bedah utama atau manajemen rumah sakit besar seperti ayah dan ibu Senpai."
            nar "Langkah kaki Miyuki yang tadinya ringan langsung melambat setengah ketukan. Senyum lepas yang sejak di depan papan pajangan tadi menghiasi wajahnya perlahan surut, berganti kembali dengan senyum formal seorang senior yang menjaga jarak."
            miyuki "Kalau dari luar terdengar sederhana, mungkin karena aku belum menceritakan betapa rumitnya diagnosis klinis pada pasien anak yang belum bisa menjelaskan letak sakitnya sendiri, Chiasa-chan."
            chiasa "Eh... maaf, Senpai. Sama sekali nggak ada maksudku meremehkan atau bilang itu gampang kok, aku cuma kaget aja..."
            miyuki "Tidak apa-apa, Chiasa-chan. Di rumah pun orang tuaku sering mengatakan hal yang mirip, bahwa pediatri kurang bergengsi dibandingkan bedah mayor. Aku sudah cukup terbiasa mendengarnya."
            chiasa "Maaf ya, Senpai, ucapanku tadi kurang sopan. Aku beneran nggak bermaksud menyamakan sama pandangan itu."
            miyuki "Sudah, tidak usah dipikirkan lagi. Bagiku pribadi, pilihan ini sama sekali bukan hal yang kecil. Ayo kita percepat sedikit jalannya, angin di luar sudah mulai dingin. Kebetulan minggu ini jadwal praktikumku juga sedang padat, jadi aku harus mampir ke perpustakaan sebentar sebelum pulang."
            chiasa "Praktikum mata kuliah apa minggu ini, Senpai?"
            miyuki "Farmakologi klinis. Tenggat laporan penghitungan dosisnya hari Jumat besok, jadi malam ini aku masih harus merapikan beberapa tabel referensi."
            chiasa "Pasti butuh ketelitian tinggi sekali ya soal dosis obat."
            miyuki "Iya, salah satu angka desimal saja dampaknya sangat besar. Semangat juga buat tugas kampusmu minggu ini ya, Chiasa-chan."
            chiasa "Terima kasih, Senpai. Semangat beresin laporannya."
            miyuki "Terima kasih, Chiasa-chan. Hati-hati di jalan pulang nanti ya."
            nar "Miyuki mengangguk sopan di dekat persimpangan jalan menuju gedung perpustakaan sebelum berbelok memisahkan diri darimu."
            nar "Sepanjang sisa perjalanan menuju persimpangan gerbang, Miyuki tetap berbicara dengan sangat sopan, tetapi ia tidak lagi menyebut sepatah kata pun tentang cita-cita maupun pasien anak-anaknya."
        else:
            yutaka "Kedengarannya agak sederhana ya, Tachibana-senpai? Kukira mahasiswa peringkat atas dari keluarga Tachibana bakal langsung mengincar bedah mayor atau manajemen rumah sakit seperti orang tua Senpai."
            nar "Langkah Miyuki melambat sejenak. Senyum hangat yang tadi muncul di depan gambar krayon anak-anak perlahan memudar, digantikan ekspresi tenang dan rapi yang terasa berjarak."
            miyuki "Mungkin terdengar sederhana karena aku baru menceritakan bagian menyenangkannya saja, belum bagian betapa sulitnya menangani pasien anak dalam kondisi kritis yang belum mampu menggambarkan gejalanya sendiri, Yutaka-kun."
            yutaka "Ah, maaf. Sama sekali nggak ada maksudku bilang pediatri itu mudah kok, Senpai..."
            miyuki "Tidak apa-apa, aku cukup sering mendengar komentar seperti itu dari lingkungan rekan ayahku. Hanya saja, untukku pribadi, rencana ini sama sekali bukan pilihan yang remeh."
            yutaka "Maaf ya, Senpai. Tadi aku asal nyeletuk aja tanpa mikir panjang."
            miyuki "Sudah, lupakan saja. Ayo kita jalan lebih cepat sedikit, udaranya sudah mulai dingin. Minggu ini aku juga masih punya tumpukan laporan praktikum yang harus diselesaikan."
            yutaka "Laporan praktikum bagian apa minggu ini, Senpai?"
            miyuki "Farmakologi klinis. Hari Jumat pagi sudah harus dikumpulkan ke dokter pembimbing, jadi aku harus memeriksa ulang tabel interaksi obatnya malam ini."
            yutaka "Kedengarannya lumayan berat juga tabel hitungannya."
            miyuki "Cukup menyita waktu memang. Kalau begitu aku duluan ke arah perpustakaan ya, Yutaka-kun."
            yutaka "Semoga cepat beres ya laporannya, Senpai."
            miyuki "Terima kasih, Yutaka-kun. Hati-hati di jalan pulang."
            nar "Miyuki merapatkan map bukunya ke dada lalu berbelok menaiki tangga menuju gedung perpustakaan dengan langkah yang teratur."
            nar "Miyuki menutup rapat topik tentang rencana masa depannya dan hanya membicarakan urusan akademik umum sampai kalian berpisah di depan gerbang kampus."
    else:
        if kk_host == "chiasa":
            chiasa "Ngomong-ngomong, Ko-nii sudah tahu belum soal rencana Senpai mau masuk spesialisasi pediatri ini?"
            nar "Langkah Miyuki sempat tertahan setengah detik di atas ubin lobi. Ia menoleh ke arahmu, dan senyum lembutnya yang biasa kembali terpasang, hanya saja kali ini tampak sedikit lebih tipis."
            miyuki "Koita-kun? Belum, aku belum pernah cerita sedetail ini ke dia. Barusan kan aku memang sedang bercerita kepadamu, Chiasa-chan."
            chiasa "Oh... kirain Senpai sudah pernah bahas duluan sama Ko-nii waktu kalian ketemu di perpustakaan atau kafe. Biasanya kan kalau soal rencana masa depan, teman-teman suka cerita ke Ko-nii."
            miyuki "Nanti kalau kebetulan sedang mengobrol soal rencana lulus dan waktunya pas, mungkin aku akan cerita juga ke Koita-kun. Tapi keinginan masuk pediatri ini murni rencanaku sendiri kok, tidak ada hubungannya dengan siapa-siapa."
            chiasa "Iya, tentu aja itu rencana Senpai sendiri. Aku cuma penasaran aja barusan."
            miyuki "Tidak apa-apa, Chiasa-chan. Ayo kita keluar, angin di koridor sini agak dingin."
            chiasa "Oh iya, minggu ini jadwal praktikum Senpai padat banget nggak?"
            miyuki "Lumayan padat, ada dua laporan observasi yang harus kukumpulkan sebelum akhir minggu. Aku juga masih harus mampir ke toko buku dekat stasiun buat ambil buku referensi tambahan."
            chiasa "Kalau begitu aku nggak bakal menahan Senpai lama-lama di jalan."
            miyuki "Terima kasih pengertiannya, Chiasa-chan. Hati-hati waktu pulang ke rumah nanti ya."
            chiasa "Senpai juga hati-hati di jalan pulang dari toko buku nanti ya."
            miyuki "Iya, Chiasa-chan. Sampai ketemu di kampus besok."
            nar "Angin malam yang sejuk berembus melewati pelataran gedung fakultas saat kalian berjalan berdampingan menuju pintu gerbang depan."
            nar "Miyuki merapikan letak buku di pelukannya dan kembali melangkah lurus melewati pintu kaca lobi. Kalian masih bertukar obrolan ringan soal jadwal kuliah sampai ke dekat gerbang, tetapi keterbukaan hangat yang tadi sempat muncul di depan gambar kucing berkaki enam itu sudah kembali disimpan olehnya."
        else:
            yutaka "Ngomong-ngomong, Koita sudah tahu belum soal rencana Senpai mau ambil spesialisasi pediatri ini?"
            nar "Langkah Miyuki terhenti sepersekian detik sebelum mendorong pintu kaca lobi. Ia menoleh menatapmu dengan senyum sopan yang terasa sedikit menipis."
            miyuki "Koita-kun? Belum. Tadi kan yang berdiri melihat gambar anak-anak di papan itu aku sama kamu, Yutaka-kun, jadi aku bercerita ke kamu."
            yutaka "Oh... kukira Senpai sudah cerita lebih dulu ke Koita waktu kumpul kemarin."
            miyuki "Kalau nanti kebetulan ada pembicaraan soal rencana setelah lulus, mungkin aku akan cerita juga padanya. Tapi keputusan memilih pediatri ini sepenuhnya rencanaku sendiri sejak awal kuliah."
            yutaka "Iya, benar juga sih, Senpai. Aku cuma asal tanya aja tadi."
            miyuki "Tidak masalah. Ayo kita jalan ke arah gerbang, aku masih harus mampir beli bahan catatan di toko buku dekat stasiun."
            yutaka "Minggu ini jadwal praktikum Senpai lagi padat?"
            miyuki "Cukup padat, ada beberapa laporan yang tenggatnya jatuh akhir minggu ini. Selesai dari toko buku pun aku langsung harus pulang merapikan catatannya."
            yutaka "Semangat ya beresin laporannya, Senpai."
            miyuki "Terima kasih, Yutaka-kun. Hati-hati di jalan pulang."
            yutaka "Senpai juga hati-hati di jalan, jangan terlalu larut begadang kerjakan laporannya."
            miyuki "Iya, aku usahakan selesai sebelum tengah malam. Sampai besok, Yutaka-kun."
            yutaka "Kalau toko bukunya sudah ramai antrean kasirnya, jangan lupa sempatkan beli makan malam dulu di dekat stasiun, Senpai."
            miyuki "Hehe, iya, nanti aku mampir beli roti atau salad sebelum naik kereta. Terima kasih sudah mengingatkan, Yutaka-kun."
            nar "Lampu-lampu taman di sepanjang jalan setapak menuju gerbang kampus mulai menyala satu per satu di atas kepala kalian."
            nar "Miyuki kembali melangkah menuruni tangga teras gedung sambil menatap jalan setapak di depannya. Percakapan kalian tetap berlangsung sopan sampai di persimpangan gerbang, sementara suasana akrab yang tadi terbuka di depan papan pajangan sudah tidak kembali lagi."
    return

# ┌─ PANDUAN CERITA · Mi21 · Rotasi Klinik
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : cabang spesialis.
# │ INTI    : A bantu / B ganggu.
# │ AKHIRAN : karier.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi21:
    call kk_scene_enter("miyuki","Rotasi pediatri · Rumah Sakit Tachibana")
    if kk_has("miyuki_cita_didengar"):
        miyuki "Ingat yang kuceritakan waktu kita jalan dari gedung kuliah? Minggu ini aku akhirnya masuk bangsal anak."
    else:
        miyuki "Aku baru dapat jadwal bangsal anak. Aku harus berangkat sebentar lagi."
    nar "Beberapa lembar jadwal jatuh saat Miyuki meraih tas. Ia berjongkok untuk mengambilnya sambil tetap menoleh ke jam. Di saku jasnya terselip pulpen dengan hiasan kecil yang mungkin disukai pasien anak."
    call kk_family_menu("Mi21", ["Bantu susun jadwalnya agar ia bisa segera masuk.", "Tahan dia sebentar untuk urusanmu sendiri."])
    if _return == "A":
        nar "Kau menyusun jadwal menurut penjelasannya dan menyerahkan lembar kuning paling atas. Miyuki memeriksa sekali, kemudian mengembuskan napas lega."
        miyuki "Terima kasih. Aku ingin masuk dengan kepala yang nggak masih sibuk mencari kertas."
        nar "Ia berangkat tepat waktu. Sebelum pintu menutup, ia sempat menoleh dan berjanji bercerita saat jeda, jika tenaganya cukup."
    else:
        nar "Kau menahannya untuk urusanmu. Miyuki mencoba mendengar, tetapi setiap menit membuat tangannya bergerak menuju tas."
        miyuki "Aku harus masuk sekarang. Bisa kita lanjut nanti?"
        nar "Ia akhirnya berani memotong. Meski begitu, sisa gugup dan rasa bersalah ikut dibawa ke dalam, menutupi sebagian kegembiraan yang tadi ingin ia bagi."
    return

# ┌─ PANDUAN CERITA · Mi-D09 · Pasien Kecil
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Tachibana Miyuki
# │ AWALAN  : rotasi pediatri Tahun 3; Aff Sedang
# │ INTI    : A Datang ke RS / B telepon / C tidak bisa datang
# │ AKHIRAN : didukung: luka[[diri] −, karier +; ia merasa dibutuhkan dengan cara yang sehat
# └─ tulis / perbaiki dialog di bawah ──
label kk_pediatric_patient:
    nar "Pesan Miyuki lebih pendek daripada biasanya. Ia tidak menyebut nama atau detail pribadi pasien, hanya mengatakan seorang anak yang selama ini menyapanya di pintu sedang memburuk."
    miyuki "Aku tahu aku bukan orang yang bisa menjanjikan semuanya baik. Tadi aku hampir mengatakannya kepada keluarganya karena nggak tahan melihat mereka takut."
    miyuki "Yuina menggantikanku sebentar. Aku perlu beberapa menit untuk mengingat bahwa sedih bukan berarti aku gagal bekerja."
    call kk_family_menu("Mi-D09", ["Temani Miyuki di ruang tunggu rumah sakit.", "Telepon dia saat jeda berikutnya.", "Katakan kau tidak bisa menemaninya."])
    if _return == "A":
        nar "Kau datang ke ruang tunggu dan duduk tanpa meminta penjelasan yang bukan hakmu. Miyuki bercerita tentang perasaannya sendiri, tentang betapa ingin ia memberi jawaban ketika yang tersedia hanya ketidakpastian."
        miyuki "Terima kasih. Aku nggak butuh kamu bilang aku pasti bisa menyelamatkan semua orang. Aku cuma ingin kembali ke sana tanpa harus berbohong agar terdengar kuat."
    elif _return == "B":
        nar "Saat jeda berikutnya kau menelepon. Miyuki mengangkatnya."
        miyuki "Aku cuma ingin ada yang mendengar. Sebentar saja."
        nar "Kau tetap di telepon sementara ia menyusun napas dan kata-kata. Ketika namanya dipanggil, ia mengatakan sudah lebih siap kembali."
        miyuki "Aku masih takut. Tapi bukan berarti harus menjauh dari pekerjaan yang kuinginkan. Nanti aku kabari kalau sudah ada waktu."
    else:
        miyuki "Baik. Terima kasih sudah menjawab. Aku akan kembali ke dalam."
        nar "Ia menutup panggilan sebelum kau sempat mencari kalimat tambahan. Kemudian ada pesan bahwa ia akan bicara dengan Yuina saat bisa. Ia tetap memerlukan seseorang untuk mendengar, sekalipun malam itu bukan dirimu."
    return

init 1 python:
    def kk_change_medical_career(delta):
        pts.setdefault("karier_miyuki",70)
        kk_adj("karier_miyuki",delta)

    def kk_support_pediatrics():
        kk_rel("miyuki","trust",5)
        kk_flag("miyuki_cita_didengar")

    def kk_support_patient_shift():
        pts.setdefault("luka_miyuki_diri",15)
        kk_adj("luka_miyuki_diri",-5)
        kk_change_medical_career(5)

    _hook("Mi06-A",kk_support_pediatrics)
    _hook("Mi06-B",lambda: kk_rel("miyuki","trust",-5))
    _hook("Mi21-A",lambda: kk_change_medical_career(5))
    _hook("Mi21-B",lambda: kk_change_medical_career(-5))
    _hook("Mi-D09-A",kk_support_patient_shift)
    _hook("Mi-D09-B",kk_support_patient_shift)

# ┌─ PANDUAN CERITA · Mi-D11 · Malam Sebelum CBT
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Tachibana Miyuki
# │ AWALAN  : minggu M30
# │ INTI    : A temani belajar semalaman (tubuh pemain) / B bawakan makanan lalu pulang / C tidak datang
# │ AKHIRAN : hasil Mi24 bergeser
# └─ tulis / perbaiki dialog di bawah ──
label kk_exam_eve:
    nar "Miyuki menandai soal yang salah sampai halaman itu dipenuhi warna. Ketika kau datang, ia sudah mengulang materi yang sama meski bisa menjawabnya tanpa melihat."
    miyuki "Kalau buku kututup, rasanya ada satu halaman yang akan membuat besok gagal. Aku tahu itu nggak masuk akal. Mengetahuinya belum membuat tanganku bisa berhenti."
    menu:
        "Temani ia mengulang soal sampai pagi.":
            $ kk_record_choice("Mi-D11","A")
            $ kk_minutes((6-kk_slot)*240-kk_minute)
            nar "Kalian mengulang soal sampai suara kendaraan pagi mulai terdengar. Sesekali Miyuki mampu menjelaskan dengan jernih, lalu lupa hal sederhana karena terlalu lelah."
            miyuki "Kita sudah sampai pagi, ya. Terima kasih menemani. Aku senang nggak sendirian, tapi tubuhmu juga pasti capek."
            nar "Buku akhirnya ditutup. Keberanian yang didapat dari kehadiranmu harus berbagi tempat dengan kantuk yang tidak bisa dinegosiasikan."
        "Bawakan makan malam dan beri ia waktu untuk istirahat." if saldo >= 800:
            $ kk_record_choice("Mi-D11","B")
            $ kk_post_money(-800,"Makan sebelum CBT")
            $ kk_adj("kelelahan_miyuki",-8)
            $ kk_minutes(30)
            nar "Kau meninggalkan makan malam dan mengucapkan selamat beristirahat. Miyuki sempat mengajakmu tinggal, lalu mengakui bahwa ajakan itu juga cara menunda menutup buku."
            miyuki "Aku makan sekarang. Setelah itu aku coba tidur. Tolong jangan tanya sudah belajar berapa halaman lagi kalau aku mengirim kabar."
        "Ucapkan semoga lancar lalu pulang.":
            $ kk_record_choice("Mi-D11","C")
            $ kk_minutes(5)
            nar "Kau mengucapkan semoga lancar dan pulang. Miyuki mengantarmu sampai pintu, berterima kasih dengan suara yang sengaja dibuat ringan."
            nar "Sebelum pintu menutup, ia kembali melihat meja. Buku itu masih terbuka pada halaman yang sama; malam yang tersisa harus ia atur tanpa kehadiranmu."
    return

init python:
    def kk_record_cbt_result():
        if kk_has("cbt_miyuki_lulus") or kk_has("cbt_miyuki_gagal"):
            return
        risks = int(kk_get("karier_miyuki",70) < 40) + int(kk_get("kelelahan_miyuki",35) >= 75)
        helped = any(c["ev"] == "Mi-D11" and c["key"] in ("A","B") for c in choices_log)
        kk_flag("cbt_miyuki_lulus" if risks <= int(helped) else "cbt_miyuki_gagal")

# ┌─ PANDUAN CERITA · Mi24 · Hasil CBT
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : hasil ujian.
# │ INTI    : A rayakan / B hibur / C abaikan.
# │ AKHIRAN : karier.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi24:
    call kk_scene_enter("miyuki","Hasil ujian · Rumah Sakit Tachibana")
    if kk_has("cbt_miyuki_lulus"):
        miyuki "Aku membaca daftarnya dua kali. Terus minta Yuina baca juga. Namaku memang ada. Aku lulus."
        nar "Ia tertawa sambil menutup mulut, kemudian menangis sebelum sempat mengatakan tidak apa-apa. Tubuhnya rupanya baru mengizinkan seluruh ketakutan yang ditahan selama ini keluar."
    else:
        miyuki "Aku belum lulus. Aku sudah baca penjelasannya. Ada yang bisa diurus besok. Hari ini aku ingin duduk sebentar sebelum harus mengatakan ke keluarga."
        nar "Ia melipat lembar pengumuman sampai namanya tidak terlihat. Kertas itu tidak seberat perasaan yang membuat tangannya sulit diletakkan tenang."
    menu:
        "Ajak ia merayakannya." if kk_has("cbt_miyuki_lulus"):
            $ kk_record_choice("Mi24","A")
            miyuki "Ayo. Aku ingin pesan kue yang nggak kubuat sendiri. Dan nggak perlu memilih yang murah hanya karena merasa harus rendah hati."
            nar "Ia tertawa lagi, lebih lega. Perayaan itu tetap kecil, tetapi untuk sekali ini semua orang di meja duduk karena ingin merayakan sesuatu miliknya."
        "Duduk bersamanya dan dengarkan.":
            $ kk_record_choice("Mi24","B")
            nar "Kau duduk dan membiarkan ia menentukan apa yang ingin diceritakan. Miyuki berbicara tentang takut menelepon rumah, tentang hal yang dipelajari, tentang betapa lelahnya menunggu hasil yang dianggap bisa merangkum dirinya."
            miyuki "Terima kasih sudah nggak buru-buru menyuruhku merasa sesuatu. Aku ingin tahu dulu sebenarnya aku merasa apa."
        "Beri ia ruang dan pamit.":
            $ kk_record_choice("Mi24","C")
            nar "Kau memberi ruang dan pamit. Miyuki memasukkan kertas ke tas, lalu duduk sekali lagi setelah sempat hendak berdiri."
            nar "Hasil itu tetap harus dibawa pulang, dibicarakan, dan ditempatkan di dalam masa depan yang belum selesai. Kau tidak berada di sampingnya saat ia memulai percakapan berikutnya."
    return
