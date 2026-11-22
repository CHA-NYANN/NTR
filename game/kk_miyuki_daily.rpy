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
    nar "Ponsel Miyuki berbunyi di meja saat kalian selesai makan. Ia menyentuh tombol yang salah, dan suara ibunya terdengar jelas sebelum ia sempat mematikan pengeras."
    "Ibu Miyuki" "Hayase akan datang Sabtu depan. Jangan buat jadwal lain. Kami sudah menyesuaikan semuanya."
    miyuki "Bu, aku belum bilang bisa. Jadwal rumah sakit—"
    nar "Ia berhenti ketika suara di seberang kembali berbicara. Punggungnya menegang, tangannya merapikan sendok yang sudah lurus."
    $ _rows = [(caption, Return(key), False) for key, caption in zip("ABC", KK_DYN_BY_ID["Mi-D04"]["choices"])]
    call screen kk_choice_panel(_rows, "Apa yang kau lakukan?")
    $ _key = _return
    $ kk_record_choice("Mi-D04", _key)
    if _key == "A":
        nar "Kau memandangi cangkir, memberi kesan bahwa tidak ada yang terdengar. Miyuki mengucapkan iya pada tanggal yang akhirnya ditetapkan."
        miyuki "Maaf, telepon keluarga. Tehnya masih hangat?"
        nar "Ia melanjutkan malam seolah percakapan itu hanya urusan kecil. Di kalendernya, Sabtu depan kini sudah dimiliki orang lain."
    elif _key == "B":
        nar "Kau menunggu sampai panggilan selesai sebelum bertanya. Miyuki menaruh ponsel jauh dari tangannya, seperti benda itu masih bisa menyela."
        miyuki "Takeru. Orang yang dipilih Ibu. Bukan aku. Aku bahkan belum diminta menjawab dengan sungguh-sungguh."
        nar "Ia menyebutnya untuk pertama kali tanpa tersenyum agar terdengar tidak terlalu serius. Malam itu ia tidak memerlukan kau menyelesaikannya, hanya tidak menganggap semuanya sudah disetujui."
    else:
        nar "Kau meminta izin Miyuki untuk berbicara kepada ibunya. Ia mengangguk setelah ragu, lalu memperkenalkanmu sebelum menyerahkan ponsel."
        "Ibu Miyuki" "Jadi kau temannya. Saya belum tahu ada tamu malam ini."
        nar "Kau memperkenalkan diri dan mengingatkan bahwa jadwal Miyuki perlu dibicarakan dengannya. Kesopanan di seberang menjadi lebih dingin, tetapi kini kau bukan lagi nama yang bisa dianggap tidak ada."
        miyuki "Aku takut tadi. Tapi terima kasih sudah menunggu aku mengizinkan. Aku ingin tetap ikut menentukan apa yang dikatakan."
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
        nar "Di balik meja konter, pemilik kafe, Ito Shinji, hanya melirik sekilas sambil mengelap gelas dengan senyum tenang yang sudah sangat hafal dengan kebiasaan pelanggan tetapnya ini. Kamu menghampiri meja pojok sambil membawa tasmu dan melirik tumpukan kotak kue tersebut dengan mata melebar."
        chiasa "Tachibana-senpai, ini beneran Senpai panggang sendiri semuanya? Meja Komorebi sampai penuh begini."
        nar "Miyuki tertawa kecil sambil merapikan tumpukan piring kertas dan serbet yang ikut ia bawa dari apartemen."
        miyuki "Ara, ketahuan ya, Chiasa-chan. Tadi di apartemen aku salah hitung takaran adonan waktu mulai memanggang, jadinya malah dapat tiga loyang sekaligus. Dua kotak tadi sebagian sudah kubagi ke teman sekelas sama perawat jaga di klinik, tinggal satu loyang besar ini."
        nar "Ia menyebutnya salah hitung takaran. Namun setiap potongannya di dalam kotak sudah diiris seragam dan dihias krim cokelat dengan rapi, seolah sejak awal memanggang ia sudah membayangkan akan ada sangat banyak orang yang membutuhkannya hari ini."
        miyuki "Kalau loyang terakhir ini kubawa pulang lagi ke apartemen, Sena pasti langsung menginterogasi aku sebenarnya bikin kue buat berapa puluh orang. Masalahnya, aku sendiri juga belum punya jawaban yang bagus buat Sena."
        nar "Baru saja selesai bicara, Miyuki sudah kembali meraih pisau kue untuk memotong barisan berikutnya agar siap dibagikan. Di depan kursinya sendiri bahkan belum ada satu piring pun, dan ia sama sekali belum mencicipi secuil pun kue buatannya sendiri."
    else:
        nar "Kafe Komorebi di pertengahan Februari terasa hangat oleh aroma kopi sangrai dan wangi manis kue cokelat panggang yang baru dibuka dari kotak. Di meja pojok dekat jendela, di hadapan Tachibana Miyuki berjajar tiga kotak kue ukuran besar hingga cangkir tehnya sendiri hampir tidak kebagian ruang di permukaan meja kayu."
        nar "Di balik meja konter, pemilik kafe, Ito Shinji, melirik sekilas sambil mengelap gelas dengan senyum tenang yang sudah sangat hafal dengan kebiasaan pelanggan tetapnya ini. Kamu melangkah menghampiri meja pojok sambil menaruh tasmu di kursi kosong dan menatap tumpukan kotak kue itu dengan alis terangkat."
        yutaka "Tachibana-senpai, ini beneran Senpai panggang sendiri semuanya? Meja Komorebi sampai penuh begini, cangkir kopiku nanti ditaruh di mana?"
        nar "Miyuki tertawa kecil sambil merapikan tumpukan piring kertas dan serbet yang ikut ia bawa dari apartemen."
        miyuki "Ara, ketahuan ya, Yutaka-kun. Tadi di apartemen aku salah hitung takaran adonan waktu mulai memanggang, jadinya malah dapat tiga loyang sekaligus. Dua kotak tadi sebagian sudah kubagi ke teman sekelas sama perawat jaga di klinik, tinggal satu loyang besar ini."
        nar "Ia menyebutnya salah hitung takaran. Namun setiap potongannya di dalam kotak sudah diiris seragam dan dihias krim cokelat dengan rapi, seolah sejak awal memanggang ia sudah membayangkan akan ada sangat banyak orang yang membutuhkannya hari ini."
        miyuki "Kalau loyang terakhir ini kubawa pulang lagi ke apartemen, Sena pasti langsung nanya aku sebenarnya bikin kue buat berapa puluh orang. Masalahnya, aku sendiri juga belum punya jawaban yang bagus buat Sena."
        nar "Baru saja selesai bicara, Miyuki sudah kembali meraih pisau kue untuk memotong barisan berikutnya agar siap dibagikan. Di depan kursinya sendiri bahkan belum ada satu piring pun, dan ia sama sekali belum mencicipi secuil pun kue buatannya sendiri."
    call kk_family_menu("Mi11", ["\"Taruh dulu pisaunya, Senpai. Duduk sini, kita makan kuenya bareng dulu.\"", "\"Sini aku bantu tawarin ke meja-meja sebelah mumpung kuenya masih hangat.\"", "\"Aku nggak mau potongan sisa bagi-bagi. Pilih satu potongan khusus buatku dong, Senpai.\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Taruh dulu pisaunya, Tachibana-senpai. Sebelum Senpai sibuk mikirin mau kasih ke siapa lagi, duduk dulu di sini. Kita makan kuenya bareng sekarang, Senpai sendiri kan belum nyicipin sama sekali dari tadi."
            nar "Kamu menarik kursi di sebelahnya lalu mengambil dua piring kecil dan dua garpu kue dari nampan yang tadi disiapkan Ito Shinji. Miyuki sempat terdiam kaget mendengar ajakanmu, lalu tersenyum lembut dan segera mengambil satu potongan bagian tengah yang paling rapi dan utuh untuk ditaruh di piringmu."
            miyuki "Nah, ini buat Chiasa-chan. Bagian tengahnya paling lembut."
            chiasa "Terus buat Senpai sendiri mau potongan yang mana? Jangan bilang nanti aja ya."
            nar "Gerakan tangan Miyuki yang tadi sudah hendak meletakkan pisau kue terhenti. Ia mengerjap pelan menatap loyang di depannya, seolah sudah lama sekali tidak ada yang menanyakan potongan mana yang paling ia inginkan sendiri."
            miyuki "Kalau buatku sendiri... sebenarnya aku paling suka bagian pinggirnya, Chiasa-chan. Yang pinggirannya agak kering dan kecokelatan kena panas loyang."
            chiasa "Lho, kirain Senpai suka bagian tengah yang banyak krimnya."
            miyuki "Justru bagian pinggir itu wanginya paling keluar. Biasanya bagian itu selalu kusimpan paling terakhir setelah semua orang selesai makan, soalnya bentuknya kurang rapi kalau dikasih ke orang lain."
            chiasa "Kalau gitu hari ini bagian pinggirnya dimakan duluan ya, Senpai. Sini piringnya."
            nar "Kamu memotong bagian sudut yang kecokelatan itu, memindahkannya ke piring Miyuki, lalu menyodorkan garpu ke tangannya. Kalian duduk berdampingan menikmati kue bersama sebelum ia memikirkan tamu atau teman lainnya. Begitu gigitan pertama masuk ke mulutnya, senyum senang yang ringan muncul di wajah Miyuki, dan ia mulai bercerita antusias tentang bagaimana ia mencoba mengganti jenis bubuk kakao supaya rasa manisnya cocok diminum bersama teh hitam."
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
            nar "Kamu memotong bagian sudut yang kecokelatan itu, memindahkannya ke piring Miyuki, lalu menyodorkan garpu ke tangannya. Kalian duduk menikmati kue bersama sebelum ia beranjak memikirkan orang lain. Begitu gigitan pertama masuk ke mulutnya, senyum gembira yang ringan muncul di wajah Miyuki, dan ia mulai menilai hasil panggangan barunya dengan antusiasme kecil yang sempat hilang di tengah kesibukannya melayani semua orang."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Mumpung kuenya masih hangat dan harum banget, sini aku bantu tawarin ke pelanggan di meja-meja sebelah ya, Tachibana-senpai. Sayang banget kalau sampai dingin di kotak."
            miyuki "Eh, boleh memangnya kita bagi-bagi di kafe? Biar kutanya dulu ke Pak Ito."
            nar "Dari balik meja konter, Ito Shinji mengangguk tenang sambil menyodorkan dua piring saji kayu bersih. Kalian menata beberapa potongan kue lalu berjalan pelan menghampiri tiga meja pelanggan lain di dalam kafe."
            nar "Dua meja mahasiswa langsung menerima dengan wajah cerah sambil memuji aroma cokelatnya. Saat kalian mendekati meja paling pojok dekat rak majalah, seorang mahasiswa berkacamata yang sibuk mengetik di laptopnya mengangkat tangan sopan dan menolak karena ia baru saja selesai makan dan sedang menghindari makanan manis."
            nar "Di sebelahmu, senyum ramah Miyuki langsung menegang tipis. Sebelum ia sempat membungkuk meminta maaf terlalu dalam atau menawarkan membikinkan rasa lain, kamu segera menyahut santai bahwa tidak masalah sama sekali, mengucapkan terima kasih, lalu menuntun lengan Miyuki kembali ke meja kalian."
            chiasa "Sudah, nggak apa-apa kok, Senpai. Orangnya tadi bilang baru kelar makan aja, jadi memang lagi kenyang."
            nar "Miyuki duduk kembali sambil memandangi potongan kue yang tersisa di piring saji kayu. Dahinya masih sedikit berkerut."
            miyuki "Tadi aku sempat kepikiran... apa bau cokelatnya terlalu pekat ya, Chiasa-chan? Harusnya tadi aku bikin versi yang rasanya lebih ringan kayak teh hijau supaya semua orang bisa makan."
            chiasa "Kuenya sudah enak banget kok, Senpai. Orang menolak satu potong kue itu cuma karena perutnya lagi kenyang, sama sekali nggak ada hubungannya sama kesalahan Senpai."
            nar "Miyuki terdiam menatap piring di tangannya beberapa detik, lalu mengembuskan napas pendek dengan tawa kecil yang agak lelah."
            miyuki "Lucu ya... dari dulu aku selalu mengira kalau ada seseorang yang menolak sesuatu yang kusiapkan, artinya aku harus segera membetulkan sesuatu dari diriku supaya mereka mau menerima lagi."
            chiasa "Sekarang gantian Senpai yang duduk makan bagiannya sendiri ya. Nih, tehnya keburu dingin."
            nar "Miyuki mengangguk pelan, mengambil garpu kue, lalu akhirnya mencicipi potongan kuenya sendiri dengan raut wajah yang jauh lebih tenang."
        else:
            yutaka "Mumpung kuenya masih hangat dan harum, sini kubantu tawarin ke meja-meja sebelah ya, Tachibana-senpai. Sayang kalau keburu dingin di kotak."
            miyuki "Eh, boleh memangnya kita bagi-bagi di kafe? Biar kutanya dulu ke Pak Ito."
            nar "Dari balik meja konter, Ito Shinji mengangguk tenang sambil menyodorkan dua piring saji kayu bersih. Kalian menata beberapa potongan kue lalu menghampiri tiga meja pelanggan lain di dalam kafe."
            nar "Dua meja mahasiswa langsung menerima dengan wajah senang sambil memuji aroma cokelatnya. Saat kalian mendekati meja pojok dekat rak majalah, seorang mahasiswa berkacamata yang sibuk mengetik di laptop mengangkat tangan sopan dan menolak karena ia baru saja selesai makan dan sedang menghindari makanan manis."
            nar "Di sebelahmu, senyum ramah Miyuki langsung menegang tipis. Sebelum ia sempat membungkuk meminta maaf terlalu dalam atau menawarkan membuat rasa lain, kamu segera menyahut santai bahwa tidak masalah sama sekali, mengucapkan terima kasih, lalu mengajak Miyuki kembali ke meja kalian."
            yutaka "Sudah, santai aja, Senpai. Orangnya cuma baru kelar makan, jadi memang lagi kenyang aja."
            nar "Miyuki duduk kembali sambil memandangi sisa potongan kue di piring saji kayu. Dahinya masih sedikit berkerut."
            miyuki "Tadi aku sempat kepikiran... apa aroma cokelatnya terlalu pekat ya, Yutaka-kun? Harusnya tadi aku bikin versi teh hijau juga supaya semua orang bisa makan."
            yutaka "Kuenya sudah enak banget kok, Senpai. Orang menolak satu potong kue itu ya cuma karena perutnya penuh, sama sekali nggak berarti ada yang salah dari kuenya atau dari Senpai."
            nar "Miyuki terdiam menatap piring di tangannya beberapa detik, lalu mengembuskan napas pendek dengan tawa kecil yang agak lelah."
            miyuki "Aneh ya... dari dulu aku selalu mengira kalau ada yang menolak sesuatu yang kusiapkan, berarti aku harus cepat-cepat membetulkan sesuatu dari diriku supaya mereka mau menerima lagi."
            yutaka "Sekarang giliran Senpai duduk makan bagiannya sendiri. Nih, tehnya keburu dingin."
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
            nar "Miyuki mengambil garpunya dan menyuap potongan kuenya dengan sorot mata biru safir yang hangat. Kali ini ia berhenti menyembunyikan keinginannya di balik alasan melayani orang lain dan terang-terangan meminta sebagian kecil waktumu untuk duduk bersamanya."
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
            nar "Miyuki mengambil garpunya dan menyuap potongan kuenya dengan sorot mata biru safir yang hangat. Kali ini ia berani meminta sebagian kecil waktumu secara langsung sebagai keinginannya sendiri tanpa menyamarkannya di balik alasan melayani orang lain."
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
    nar "Miyuki menempelkan jadwal klinik pada halaman depan catatan. Tulisan kecil memenuhi ruang yang dahulu cukup untuk satu minggu kuliah biasa. Ia melihatmu membaca dan cepat-cepat mengatakan masih bisa diatur."
    miyuki "Besok mulai. Aku senang, sungguh. Aku juga takut tiba di sana dan lupa semua yang pernah kupelajari."
    nar "Ia menunjukkan satu jawaban yang ditandai pembimbing, lalu tiga halaman yang hendak diulang sebelum tidur."
    call kk_family_menu("Mi12", ["Bantu ia mengulang bahan belajarnya.", "Ajak ia meninggalkan catatannya sebentar.", "Beri ia ruang untuk belajar sendiri."])
    if _return == "A":
        nar "Kau menutup kolom jawaban dan membacakan soal. Miyuki sempat salah, mengulang alasannya, lalu menemukan bagian yang perlu diperbaiki."
        miyuki "Jangan kasih petunjuk dulu. Aku mau tahu letak lupanya."
        nar "Belajar bersama membuat rasa takutnya punya batas yang bisa dikerjakan: satu pertanyaan, satu pembahasan, kemudian berhenti pada jam yang disepakati."
    elif _return == "B":
        nar "Kau mengajaknya meninggalkan catatan. Miyuki mengikuti beberapa langkah, lalu berkali-kali melihat tasnya."
        miyuki "Aku mau istirahat, tapi belum ingin pergi lama. Besok benar-benar mulai."
        nar "Ajakanmu bisa menjadi jeda, bisa juga gangguan. Malam itu ia kesulitan menikmati apa pun sebelum tahu kapan akan diizinkan kembali menyiapkan dirinya."
    else:
        nar "Kau memberi ruang belajar dan menanyakan apakah ada barang yang perlu diambilkan sebelum pergi. Miyuki menggeleng, lalu menyebut air minum dengan malu-malu."
        miyuki "Terima kasih. Aku akan kabari kalau sudah selesai. Bukan minta ditemani terus, cuma... aku ingin ada yang tahu."
        nar "Ia membuka kembali catatan. Kesibukannya baru dimulai; kedekatan kalian kini harus belajar menghormati waktu yang tidak selalu bisa dibagi."
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
    nar "Panggilan ibunya masuk tepat saat Miyuki duduk untuk makan. Ia menjawab karena takut ada keadaan penting. Suara yang terdengar justru membicarakan undangan keluarga, prestasi anak kenalan, dan mengapa ia jarang pulang."
    miyuki "Ibu, aku masih di rumah sakit. Makan malamku baru... iya, aku dengar."
    nar "Ia menurunkan sendok. Nasi di kotak terbuka kehilangan hangat selama ia mengucapkan paham berulang kali."
    call kk_family_menu("Mi13", ["Tunggu dan dengarkan setelah ia selesai.", "Minta ibunya memberi Miyuki waktu istirahat.", "Alihkan pembicaraan setelah ia menutup telepon."])
    if _return == "A":
        nar "Kau menunggu, lalu bertanya apakah ia ingin membicarakannya. Miyuki menyandarkan punggung pada kursi."
        miyuki "Aku ingin suatu hari ditelepon cuma karena Ibu ingin mendengar suaraku. Bukan mengecek apakah hidupku sudah sesuai rencana."
        nar "Ia menatap makanannya, malu karena kalimat itu terdengar seperti keluhan seorang anak. Kau tetap mendengarkan sampai ia tidak perlu mengecilkannya lagi."
    elif _return == "B":
        nar "Kau meminta ibunya memberi Miyuki waktu makan dan istirahat. Hening singkat menyusul sebelum jawaban sopan yang jelas tidak menyukai campur tanganmu."
        miyuki "Terima kasih. Tapi nanti aku yang harus melanjutkan pembicaraan ini. Aku ingin kamu tahu kenapa kadang aku takut dibela di depan Ibu."
        nar "Ia akhirnya bisa makan, tetapi ponselnya tetap diletakkan menghadap atas."
    else:
        nar "Kau mengganti topik sesudah telepon ditutup. Miyuki mengikutinya dengan mudah, bahkan menyisipkan satu godaan agar kau yakin suasana kembali ringan."
        nar "Namun makanannya tidak banyak berkurang. Ketika waktunya kembali ke dalam, ia merapikan kotak itu sambil meminta maaf karena makan terlalu lama."
    return

# ┌─ PANDUAN CERITA · Mi-D02 · Tertidur di Bahu
# │ LOKASI  : (dinamis — muncul dari kondisi) · TERLIBAT: Tachibana Miyuki
# │ AWALAN  : kelelahan ≥ 60; pemain duduk di dekatnya
# │ INTI    : A Biarkan sampai bangun (dua jam lewat) / B bangunkan / C foto / D pindahkan ke ruang jaga
# │ AKHIRAN : Intim +, kelelahan −5; foto bisa sampai ke Mei
# └─ tulis / perbaiki dialog di bawah ──
label kk_library_rest(place):
    if not kk_can_sit_with_miyuki(place):
        return
    nar "Miyuki membaca paragraf yang sama tiga kali. Pada bacaan keempat, jarinya tidak lagi mengikuti baris. Ia menutup mata sambil tetap menahan buku agar tampak masih bekerja."
    miyuki "Kalau aku istirahat sebentar, tolong jaga bukuku. Sebentar saja."
    nar "Tak lama kepalanya bersandar di bahumu. Napasnya berubah teratur sebelum ia sempat menyadari jarak kalian."
    menu:
        "Tetap duduk sampai ia terbangun.":
            $ kk_record_choice("Mi-D02","A")
            $ kk_minutes(120)
            nar "Kau tetap duduk, mengubah posisi sesedikit mungkin. Suara halaman dan langkah orang berganti di sekitar kalian; untuk sementara, Miyuki tidak menjawab siapa pun."
            miyuki "Dua jam? Aku ingin marah karena nggak dibangunkan, tapi... aku sudah lama nggak bangun tanpa langsung merasa pusing."
            nar "Ia meminta maaf soal bahumu, lalu berhenti ketika kau mengatakan keputusan tinggal adalah keputusanmu."
        "Bangunkan ia dengan pelan.":
            $ kk_record_choice("Mi-D02","B")
            $ kk_minutes(5)
            nar "Kau memanggil pelan sampai ia membuka mata. Miyuki menegakkan tubuh terlalu cepat, mencari jam sebelum mencari wajahmu."
            miyuki "Aku tertidur, ya. Maaf. Aku harus cari tempat istirahat yang benar."
            nar "Ia mengusap pipi, malu tetapi mulai mengakui bahwa memaksa satu paragraf lagi tidak akan menolongnya."
        "Ambil foto saat ia tertidur.":
            $ kk_record_choice("Mi-D02","C")
            $ kk_flag("foto_miyuki_tertidur")
            $ kk_minutes(5)
            nar "Foto itu tersimpan di ponselmu ketika Miyuki belum bisa memutuskan apakah ia ingin dilihat seperti itu. Wajah yang tertidur membuatnya tampak jauh lebih muda dan tidak terlindungi."
            nar "Kau bisa menyebutnya kenangan manis. Jika gambar itu sampai ke tangan orang lain, Miyuki tetap yang harus menghadapi tatapan dan pertanyaan tentang sesuatu yang tidak pernah ia setujui untuk dibagikan."
        "Bantu ia beristirahat di ruang jaga.":
            $ kk_record_choice("Mi-D02","D")
            $ kk_minutes(15)
            nar "Kau membangunkannya cukup untuk menawarkan ruang jaga, lalu membawakan bukunya ketika ia bersedia pindah. Miyuki berjalan dengan mata berat, berhenti sekali untuk memastikan tidak ada barang tertinggal."
            miyuki "Tolong ingatkan aku kalau nanti bilang masih bisa lanjut. Aku barusan bahkan lupa halaman yang kubaca."
            nar "Di ruang jaga ia akhirnya berbaring. Kali ini istirahat tidak perlu disamarkan sebagai kegiatan belajar."
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
        nar "Sore itu kamu berjalan beriringan dengan Tachibana Miyuki melewati koridor lantai dasar Gedung Kedokteran yang sudah mulai lengang selepas jam kuliah berakhir. Di sepanjang dinding sebelah kiri menuju pintu lobi, terpasang papan pajangan berkaca panjang yang berisi jadwal seminar serta dokumentasi kegiatan mahasiswa."
        nar "Tepat di bagian tengah papan kaca itu, tertempel belasan kertas gambar penuh coretan krayon warna-warni hasil karya anak-anak dari acara kunjungan relawan di bangsal rumah sakit akhir pekan lalu."
        nar "Langkah Miyuki tiba-tiba melambat, lalu berhenti tepat di depan deretan gambar anak-anak tersebut. Ia menunjuk selembar kertas gambar di baris bawah yang memperlihatkan seekor kucing besar berwarna biru tua dengan enam kaki, mata bulat yang besar sebelah, dan kumis keriting yang lebih panjang daripada tubuhnya."
        nar "Tanpa menoleh untuk memeriksa apakah kamu ikut berhenti atau tidak, Miyuki tersenyum lepas seorang diri memandangi gambar krayon itu."
        chiasa "Lucu banget gambar kucingnya, Tachibana-senpai. Kakinya sampai ada enam begitu, terus kumisnya panjang banget."
        miyuki "Hehe, menggemaskan banget ya, Chiasa-chan? Yang menggambar ini pasien anak laki-laki umur enam tahun waktu acara menggambar bareng relawan hari Sabtu kemarin. Waktu kutanya kenapa kaki kucingnya ada enam, dia jawab dengan muka serius banget."
        chiasa "Memangnya dia jawab kenapa, Senpai?"
        miyuki "Katanya, kalau kucing biasa kakinya cuma empat, nanti gampang ketangkap waktu dikejar dokter yang bawa jarum suntik. Jadi harus dikasih dua kaki cadangan biar larinya secepat kereta ekspres."
        chiasa "Haha, pintar banget anak umur enam tahun bisa kepikiran alasan kayak gitu."
        miyuki "Iya. Padahal waktu hari pertama dia masuk ruang rawat, dia takut banget sampai nggak mau lepas dari jaket ibunya. Aku selalu senang setiap kali lihat anak kecil akhirnya merasa cukup aman buat bercerita atau bercanda seperti itu. Soalnya sering kali orang dewasa di sekitar mereka sudah buru-buru menyuruh diam atau memberi jawaban sebelum anaknya sendiri tahu boleh bertanya apa."
        nar "Miyuki masih memandangi kertas gambar itu beberapa detik lagi, lalu kembali melangkah pelan di sampingmu menuju pintu kaca lobi dengan suara yang tenang dan mantap."
        miyuki "Nanti setelah lulus ujian negara dan selesai masa residensi awal, aku pengin mengambil spesialisasi pediatri, Chiasa-chan. Bukan karena aku membayangkan bekerja di bangsal anak itu bakal selalu lucu dan menyenangkan setiap hari. Justru karena anak-anak punya banyak sekali ketakutan yang harus didengarkan dengan sabar sebelum kita bisa benar-benar mengobati mereka."
    else:
        nar "Sore itu kamu melangkah keluar menyusuri lobi lantai satu Gedung Kedokteran bersama Tachibana Miyuki. Di dinding koridor dekat pintu utama, terdapat papan pengumuman kaca berukuran lebar yang memajang laporan kegiatan bakti sosial mahasiswa kedokteran."
        nar "Di sudut tengah papan tersebut, berjajar kertas-kertas gambar penuh warna krayon buatan pasien anak-anak dari acara relawan rumah sakit minggu lalu."
        nar "Langkah kaki Miyuki melambat lalu terhenti di depan kaca pajangan itu. Ia menunjuk selembar kertas di pojok bawah yang bergambar seekor kucing biru berkaki enam dengan kumis mencuat lebar, lalu tersenyum hangat seorang diri tanpa menoleh dulu ke arahmu."
        yutaka "Kucing biru berkaki enam, Tachibana-senpai? Bebas banget ya imajinasi anak kecil."
        miyuki "Hehe, iya kan, Yutaka-kun? Yang menggambar ini anak umur enam tahun waktu kami mengadakan sesi bermain di bangsal anak hari Sabtu lalu. Waktu kutanya kenapa kakinya ditambah dua, jawabannya serius sekali."
        yutaka "Dia bilang kenapa memangnya, Senpai?"
        miyuki "Katanya supaya kucingnya punya gigi persneling tambahan buat kabur kalau dikejar dokter yang bawa suntikan. Padahal waktu pertama kali datang ke ruang periksa, anak itu menangis terus karena takut lihat jas putih."
        yutaka "Haha, ada-ada aja idenya."
        miyuki "Aku suka sekali momen waktu anak-anak akhirnya berani membuka suara dan bercerita jujur seperti itu. Kadang orang dewasa di sekeliling mereka terlalu sibuk menenangkan dengan kalimat cepat, sampai anaknya sendiri tidak sempat menjelaskan bagian mana yang sebenarnya membuat mereka takut."
        nar "Ia berdiri sejenak lagi menatap deretan gambar krayon itu, lalu kembali berjalan pelan di sebelahmu menuju pintu keluar gedung dengan nada bicara yang terdengar sangat yakin."
        miyuki "Nanti kalau aku sudah lulus, aku ingin masuk spesialisasi pediatri, Yutaka-kun. Bukan karena kupikir merawat anak-anak itu pekerjaan yang ringan atau manis terus. Justru karena di sana ada banyak sekali hal yang harus didengarkan pelan-pelan sebelum mereka bisa ditolong dengan benar."
    call kk_family_menu("Mi06", ["\"Keren banget, Senpai. Selain itu, apa lagi yang bikin Senpai yakin milih pediatri?\"", "\"Kedengarannya agak sederhana ya, Senpai?\"", "\"Koita sudah tahu rencana Senpai mau masuk pediatri ini?\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Keren banget tujuannya, Tachibana-senpai. Selain kejadian waktu acara relawan kemarin, apa lagi yang bikin Senpai yakin banget pengin ambil pediatri?"
            nar "Mata biru safir Miyuki langsung berbinar hangat, tampak senang karena kamu menanyakan alasan di balik pilihannya secara sungguh-sungguh."
            miyuki "Kamu beneran mau dengar ceritanya, Chiasa-chan? Kalau begitu kita jalan agak pelan lewat jalur taman samping ya. Kalau sudah mulai bicara soal pediatri, Senpai suka lupa waktu."
            chiasa "Nggak apa-apa kok, Senpai, aku juga lagi nggak buru-buru pulang ke rumah. Cerita aja."
            nar "Sepanjang jalan setapak yang dinaungi pepohonan kamper menuju gerbang depan kampus, Miyuki berbicara dengan antusiasme yang jarang ia perlihatkan saat sedang membahas urusan keluarganya."
            miyuki "Waktu aku mulai ikut observasi klinik semester ini, aku sering lihat anak kecil yang gemetar waktu mau diperiksa, tapi dokter atau orang tuanya cuma bilang, 'Cuma sebentar kok, jangan cengeng.' Padahal buat anak sekecil itu, ketidaktahuan soal apa yang bakal dilakukan ke tubuh mereka itu jauh lebih menakutkan daripada rasa sakitnya sendiri."
            chiasa "Kalau dipikir-pikir iya juga ya, Senpai. Jangankan anak kecil, kita aja kalau tiba-tiba disuruh berbaring tanpa dijelasin mau diapain pasti panik."
            miyuki "Nah, persis itu! Dan bukan cuma pasien anaknya saja yang butuh ditenangkan. Ibu atau ayah yang mengantar mereka juga sering datang ke rumah sakit dengan wajah pucat karena menyalahkan diri sendiri saat anaknya jatuh sakit. Aku ingin belajar jadi dokter anak yang bisa mendengarkan kecemasan orang tuanya juga tanpa menghakimi mereka."
            chiasa "Tapi jadwal jaga dan beban belajarnya pasti berat banget kan, Senpai?"
            miyuki "Berat banget, jujur aja. Kadang kalau habis baca buku teks patologi sampai tengah malam di apartemen, punggungku rasanya mau patah. Tapi setiap kali aku teringat wajah anak-anak di bangsal kemarin, aku selalu tahu jelas untuk apa aku masih bertahan belajar setiap malam."
            chiasa "Senpai pasti bakal jadi dokter anak yang hebat banget nanti. Anak-anak nggak bakal perlu gambar kucing kaki enam lagi buat kabur dari Senpai."
            nar "Miyuki tertawa lepas sambil merapikan tali tas di bahunya, berjalan di sampingmu dengan langkah yang terasa jauh lebih ringan sampai kalian tiba di gerbang utama."
        else:
            yutaka "Pilihan yang keren, Tachibana-senpai. Selain cerita anak yang gambar kucing tadi, apa lagi yang bikin Senpai mantap banget memilih pediatri?"
            nar "Mata biru safir Miyuki langsung tampak berbinar, terkejut sekaligus senang karena kamu tertarik mendengarkan pemikirannya lebih jauh."
            miyuki "Kamu sungguh ingin dengar, Yutaka-kun? Kalau begitu kita jalan santai lewat pelataran samping ya. Senpai bisa bicara panjang lebar kalau sudah ditanya soal ini."
            yutaka "Santai aja, Senpai. Sore ini jadwalku kosong kok."
            nar "Sambil berjalan pelan menyusuri trotoar kampus yang mulai teduh, Miyuki bercerita dengan nada suara yang hidup dan penuh keyakinan."
            miyuki "Selama ikut kegiatan observasi di rumah sakit, aku sering memperhatikan bagaimana ketakutan pasien anak-anak kadang dianggap remeh oleh orang dewasa. Mereka cuma disuruh diam supaya pemeriksaannya cepat selesai, padahal mereka menangis karena tidak mengerti alat apa yang sedang didekatkan ke mereka."
            yutaka "Masuk akal sih. Orang dewasa aja kadang tegang kalau masuk ruang tindakan tanpa dikasih penjelasan."
            miyuki "Betul sekali. Belum lagi orang tua yang membawa anak mereka ke ruang gawat darurat malam-malam, mereka sering kali jauh lebih panik dan merasa bersalah. Aku ingin jadi dokter yang punya kesabaran untuk menjelaskan pelan-pelan kepada anak maupun orang tuanya, tanpa bersikap menggurui."
            yutaka "Kedengarannya butuh tenaga dan kesabaran ekstra setiap hari ya, Senpai."
            miyuki "Sangat menguras tenaga memang. Kadang kalau pulang praktik malam, rasanya aku sudah terlalu lelah bahkan untuk memasak makan malam sendiri. Tapi setiap kali aku mengingat tujuan itu, rasa lelahnya jadi punya arti yang jelas."
            yutaka "Bidang itu cocok banget sama pembawaan Senpai. Pasti banyak keluarga pasien yang bakal terbantu nanti."
            nar "Miyuki tertawa lembut sambil membetulkan letak tasnya. Meskipun jadwal kuliah tahun ketiganya masih menumpuk, sore ini wajahnya tampak sangat cerah saat berjalan bersamamu menuju stasiun."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Kedengarannya agak sederhana ya alasannya, Tachibana-senpai? Tadinya kukira Senpai bakal ngincar spesialisasi bedah utama atau manajemen rumah sakit besar seperti ayah dan ibu Senpai."
            nar "Langkah kaki Miyuki yang tadinya ringan langsung melambat setengah ketukan. Senyum lepas yang sejak di depan papan pajangan tadi menghiasi wajahnya perlahan surut, berganti kembali dengan senyum formal seorang senior yang menjaga jarak."
            miyuki "Kalau dari luar terdengar sederhana, mungkin karena aku belum menceritakan betapa rumitnya diagnosis klinis pada pasien anak yang belum bisa menjelaskan letak sakitnya sendiri, Chiasa-chan."
            chiasa "Eh... bukan maksudku meremehkan bilang itu gampang kok, Senpai, aku cuma kaget aja—"
            miyuki "Tidak apa-apa, Chiasa-chan. Di rumah pun orang tuaku sering mengatakan hal yang mirip, bahwa pediatri kurang bergengsi dibandingkan bedah. Tapi bagiku pribadi, pilihan ini sama sekali bukan hal yang kecil."
            chiasa "Maaf ya, Senpai, ucapanku tadi kurang sopan."
            miyuki "Sudah, tidak usah dipikirkan lagi. Ayo kita percepat sedikit jalannya, angin sorenya sudah mulai dingin. Kebetulan minggu ini jadwal praktikumku juga sedang padat, jadi aku harus mampir ke perpustakaan sebentar sebelum pulang."
            chiasa "Praktikum mata kuliah apa minggu ini, Senpai?"
            miyuki "Farmakologi klinis. Tenggat laporan penghitungan dosisnya hari Jumat besok, jadi malam ini aku masih harus merapikan beberapa tabel referensi."
            chiasa "Semangat ya beresin laporannya, Senpai."
            miyuki "Terima kasih, Chiasa-chan. Hati-hati di jalan pulang nanti ya."
            nar "Sepanjang sisa perjalanan menuju persimpangan gerbang, Miyuki tetap berbicara dengan sangat sopan, tetapi ia tidak lagi menyebut sepatah kata pun tentang cita-cita maupun pasien anak-anaknya."
        else:
            yutaka "Kedengarannya agak sederhana ya, Tachibana-senpai? Kukira mahasiswa peringkat atas dari keluarga Tachibana bakal langsung ngincar bedah mayor atau manajemen rumah sakit seperti orang tua Senpai."
            nar "Langkah Miyuki melambat sejenak. Senyum hangat yang tadi muncul di depan gambar krayon anak-anak perlahan memudar, digantikan ekspresi tenang dan rapi yang terasa berjarak."
            miyuki "Mungkin terdengar sederhana karena aku baru menceritakan bagian menyenangkannya saja, belum bagian betapa sulitnya menangani pasien anak dalam kondisi kritis, Yutaka-kun."
            yutaka "Ah, maaf, bukan maksudku bilang pediatri itu mudah kok, Senpai..."
            miyuki "Tidak apa-apa, aku cukup sering mendengar komentar seperti itu dari lingkungan rekan ayahku. Hanya saja, untukku pribadi, rencana ini sama sekali bukan pilihan yang remeh."
            yutaka "Maaf ya, Senpai. Tadi aku asal nyeletuk aja."
            miyuki "Sudah, lupakan saja. Ayo kita jalan lebih cepat sedikit, langitnya sudah mulai mendung. Minggu ini aku juga masih punya tumpukan laporan praktikum yang harus diselesaikan malam ini."
            yutaka "Laporan praktikum bagian apa minggu ini, Senpai?"
            miyuki "Farmakologi klinis. Hari Jumat pagi sudah harus dikumpulkan ke dokter pembimbing, jadi malam ini aku harus memeriksa ulang tabel interaksi obatnya."
            yutaka "Semoga cepat beres ya laporannya, Senpai."
            miyuki "Terima kasih, Yutaka-kun. Hati-hati di jalan pulang."
            nar "Miyuki menutup rapat topik tentang rencana masa depannya dan hanya membicarakan urusan akademik umum sampai kalian berpisah di depan gerbang kampus."
    else:
        if kk_host == "chiasa":
            chiasa "Ngomong-ngomong, Ko-nii sudah tahu belum soal rencana Senpai mau masuk spesialisasi pediatri ini?"
            nar "Langkah Miyuki sempat tertahan setengah detik di atas ubin lobi. Ia menoleh ke arahmu, dan senyum lembutnya yang biasa kembali terpasang, hanya saja kali ini tampak sedikit lebih tipis."
            miyuki "Koita-kun? Belum, aku belum pernah cerita sedetail ini ke dia. Barusan kan aku memang sedang bercerita kepadamu, Chiasa-chan."
            chiasa "Oh... kirain Senpai sudah pernah bahas duluan sama Ko-nii waktu kalian ketemu di perpustakaan atau kafe. Biasanya kan kalau soal rencana masa depan, teman-teman suka cerita ke Ko-nii."
            miyuki "Nanti kalau kebetulan sedang mengobrol soal rencana lulus dan waktunya pas, mungkin aku akan cerita juga ke Koita-kun. Tapi keinginan masuk pediatri ini murni rencanaku sendiri kok, tidak ada hubungannya dengan siapa-siapa."
            chiasa "Iya, tentu aja itu rencana Senpai sendiri."
            nar "Miyuki merapikan letak buku di pelukannya dan kembali melangkah lurus melewati pintu kaca lobi. Kalian masih bertukar obrolan ringan soal jadwal kuliah sampai ke dekat gerbang, tetapi keterbukaan hangat yang tadi sempat muncul di depan gambar kucing berkaki enam itu sudah kembali disimpan olehnya."
        else:
            yutaka "Ngomong-ngomong, Koita sudah tahu belum soal rencana Senpai mau ambil spesialisasi pediatri ini?"
            nar "Langkah Miyuki terhenti sepersekian detik sebelum mendorong pintu kaca lobi. Ia menoleh menatapmu dengan senyum sopan yang terasa sedikit menipis."
            miyuki "Koita-kun? Belum. Tadi kan yang berdiri melihat gambar anak-anak di papan itu aku sama kamu, Yutaka-kun, jadi aku bercerita ke kamu."
            yutaka "Oh... kukira Senpai sudah cerita lebih dulu ke Koita waktu ngumpul kemarin."
            miyuki "Kalau nanti kebetulan ada pembicaraan soal rencana setelah lulus, mungkin aku akan cerita juga padanya. Tapi keputusan memilih pediatri ini sepenuhnya rencanaku sendiri sejak awal kuliah."
            yutaka "Iya, benar juga sih, Senpai."
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
    miyuki "Sena menggantikanku sebentar. Aku perlu beberapa menit untuk mengingat bahwa sedih bukan berarti aku gagal bekerja."
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
        nar "Ia menutup panggilan sebelum kau sempat mencari kalimat tambahan. Kemudian ada pesan bahwa ia akan bicara dengan Sena saat bisa. Ia tetap memerlukan seseorang untuk mendengar, sekalipun malam itu bukan dirimu."
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
        miyuki "Aku membaca daftarnya dua kali. Terus minta Sena baca juga. Namaku memang ada. Aku lulus."
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
