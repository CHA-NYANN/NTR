# Miyuki awal (Mi04, Mi08, Mi10). Menyambung jalur pemulihan (Sato Kyoko) dan
# kerentanan yang dibaca arc klinik/CBT. Efek mengikuti Event_Miyuki dan Alur_Cabang/01.
# ┌─ PANDUAN CERITA · Mi04 · Tali Obi
# │ LOKASI  : Kampus Kouseikan · Gedung Kedokteran
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : kesulitan memakai yukata.
# │ INTI    : A bantu / B panggil Sena / C goda.
# │ AKHIRAN : intimasi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi04:
    call kk_scene_enter("miyuki", "Gedung Kedokteran")
    if kk_host == "chiasa":
        nar "Di dalam ruang ganti kecil yang dipinjam sebelum berangkat ke festival musim panas, aroma samar parfum bunga dan kayu kipas lipat memenuhi ruangan. Di depan cermin tinggi, Tachibana Miyuki berdiri membelakangi kaca sambil memegang kedua ujung tali obi berwarna merah anggur di punggungnya."
        nar "Yukata biru tua bermotif bunga tipis yang ia kenakan tampak sangat serasi dengan rambut hitam lurus panjangnya—tetapi begitu ia mencoba menoleh lewat bahu untuk mengencangkan simpul di belakang pinggangnya, lipatan kain tebal itu kembali melorot pelan dan terlepas."
        nar "Miyuki menghela napas panjang dengan bahu sedikit turun, menatap bayangannya sendiri di cermin dengan ekspresi kalah yang jarang sekali terlihat di depan umum."
        miyuki "Ara... aku bisa menghafal ratusan halaman buku anatomi tanpa keliru satu saraf pun. Ternyata kain sepanjang ini punya rencananya sendiri."
        nar "Dari balik pintu ruang ganti, suara teman-teman rombongan di lorong mulai memanggil menanyakan apakah kalian sudah siap berangkat. Seketika punggung Miyuki kembali tegak; ia menyahut dengan suara lembut dan tenang khas senior yang selalu serba beres."
        miyuki "Iya, sebentar lagi kami keluar kok! Tunggu lima menit ya!"
        nar "Begitu suara di lorong menjauh, ia langsung menoleh ke arahmu yang sudah selesai bersiap, kedua matanya yang biru sapphire memandangmu dengan senyum kikuk yang jujur meminta tolong."
        miyuki "Chiasa-chan... boleh minta tolong sebentar? Sepertinya aku sudah kalah lima kali dari tali obi ini."
    else:
        nar "Miyuki berdiri membelakangi cermin dengan dua ujung obi di tangan. Ia mencoba melihat simpulnya melalui bahu, lalu mendesah ketika kain itu kembali melorot."
        miyuki "Aku bisa menghafal halaman-halaman anatomi. Ternyata kain sepanjang ini punya rencana sendiri."
        nar "Di luar ruang ganti, rombongan mulai memanggil. Ia menjawab sebentar lagi dengan suara senpai yang sangat meyakinkan, lalu menatapmu meminta tolong."
    call kk_family_menu("Mi04", ["Bantu rapikan talinya dengan hati-hati.", "Panggil Sena untuk membantunya.", "Goda kecanggungannya."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau melangkah mendekat ke belakangnya, namun tetap berhenti setengah langkah untuk memastikan ia nyaman sebelum tanganmu menyentuh kainnya."
            chiasa "Boleh kubantu rapikan dari belakang, Tachibana-senpai? Sini biar kupegang ujungnya."
            nar "Miyuki mengangguk lega, lalu mengumpulkan rambut hitam panjangnya ke satu sisi bahu dengan kedua tangan agar punggung yukatanya terlihat jelas."
            miyuki "Terima kasih, Chiasa-chan. Tolong jangan terlalu kencang ya—aku masih ingin mencicipi semua takoyaki dan es serut yang tadi kita lewati di depan stan."
            chiasa "Tenang saja, nggak bakal bikin sesak. Begini sudah pas?"
            nar "Kau merapikan lipatan kain tebal itu perlahan, menarik kedua ujungnya hingga simpul pitanya duduk tegak dan rapi di tengah punggungnya, lalu mengecek sekali lagi apakah ikatannya nyaman saat ia menarik napas."
            nar "Ketika kau selesai dan menarik tanganmu, Miyuki memutar badan sedikit memeriksa bayangannya di cermin—tetapi ia tidak langsung melangkah menjauh. Ia tetap berdiri cukup dekat darimu sesaat lebih lama sambil tersenyum lembut tanpa sedikit pun topeng senior yang serba sempurna."
            miyuki "Wah, rapi sekali... terima kasih banyak, Chiasa-chan. Ternyata Senpai boleh ya nggak pandai satu hal di depanmu."
            chiasa "Tentu saja boleh, Senpai. Semua orang pasti ada bagian yang repot dikerjakan sendiri."
            nar "Ia tertawa kecil yang tulus dan hangat sebelum meraih tas serutnya untuk berangkat bersama."
        else:
            nar "Kau menanyakan apakah boleh membantu sebelum mendekat. Miyuki mengangguk dan mengangkat rambut agar kainnya terlihat."
            miyuki "Jangan terlalu kencang. Aku masih ingin makan semua yang tadi kulihat di stan."
            nar "Kau merapikannya perlahan sambil meminta ia memeriksa kenyamanannya. Sesudah selesai, ia tetap berdiri dekat sesaat lebih lama."
            miyuki "Terima kasih. Senpai boleh nggak pandai satu hal di depanmu, ya."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Merasa seseorang yang benar-benar ahli mengikat obi akan jauh lebih cepat daripada tebakanmu sendiri, kau melangkah ke pintu ruang ganti dan memanggil sahabat dekat Miyuki yang sedang menunggu di lorong."
            chiasa "Sena-san, tolong sebentar ke sini—Tachibana-senpai butuh bantuan merapikan obinya."
            nar "Pintu langsung terbuka lebar. Sena melangkah masuk, langsung berhenti sejenak menahan tawa begitu melihat simpul kain yang nyaris terpasang terbalik di punggung Miyuki, lalu segera mengambil alih dengan tangan cekatan."
            "Sena" "Astaga, Miyuki... lain kali minta tolong sebelum lima kali membongkar sendiri, boleh nggak? Lipatannya sampai kusut begini."
            miyuki "Aku kan ingin mencoba sendiri dulu, Sena. Lima kali itu masih masuk hitungan berusaha, tahu."
            "Sena" "Iya deh, calon dokter yang nggak mau kalah sama kain. Nah, tahan napas sedikit—beres!"
            nar "Dalam kurang dari dua menit, simpul pita obi itu sudah duduk sempurna. Ketika kalian melangkah keluar menuju lorong tempat rombongan menunggu, Miyuki sempat menoleh kepadamu dengan rona malu tipis yang justru terlihat manis."
            miyuki "Terima kasih ya sudah manggil Sena, Chiasa-chan. Agak malu sih ketahuan berantakan begitu... tapi lega juga ternyata aku nggak harus selalu membereskan semuanya sendiri dulu sebelum boleh ikut menikmati festival."
        else:
            nar "Kau memanggil Sena. Ia datang, menahan tawa ketika melihat simpul yang nyaris terbalik, lalu mengambil alih dengan cekatan."
            "Sena" "Lain kali minta tolong sebelum lima kali membongkar, boleh?"
            miyuki "Aku ingin mencoba sendiri dulu. Lima kali itu masih mencoba."
            nar "Ketika keluar, Miyuki berterima kasih kepadamu. Wajahnya sedikit malu, tetapi ia tidak lagi harus membuktikan bisa menyelesaikan semuanya sendiri sebelum menikmati festival."
    else:
        if kk_host == "chiasa":
            nar "Melihat senior Kedokteran yang biasanya selalu tenang, anggun, dan serba bisa itu ternyata dibuat kewalahan oleh sehelai kain panjang, senyum jahil langsung muncul di bibirmu."
            chiasa "Wah, ternyata Tachibana-senpai yang biasanya paling tenang di kampus bisa kalah juga sama tali obi, ya?"
            nar "Miyuki langsung menoleh dari cermin sambil menggembungkan pipinya sedikit—ekspresi merajuk yang sangat jarang ia perlihatkan—tetapi sedetik kemudian ia sendiri hampir tertawa melihat bayangannya di kaca."
            miyuki "Ih, Chiasa-chan jahat banget malah ngeledek! Jangan mengganggu konsentrasiku ya—aku ini sedang bernegosiasi serius dengan obi."
            chiasa "Kalau negosiasinya gagal lagi nanti kembang apinya keburu selesai lho, Senpai."
            miyuki "Nggak akan! Lihat saja kali ini pasti jadi!"
            nar "Entah karena leluconmu berhasil mencairkan ketegangannya, tangannya kini bergerak jauh lebih santai saat kembali melipat kain itu. Ketika suara rombongan di luar kembali memanggil, Miyuki tidak lagi buru-buru membuat alasan sempurna."
            miyuki "Tunggu sebentar lagi ya! Kali ini sungguhan... mungkin!"
            nar "Tawa ringan kalian berdua terdengar sampai ke luar pintu, membuat persiapan festival malam itu terasa jauh lebih hangat daripada biasanya."
        else:
            nar "Kau menggoda senpai yang biasanya begitu tenang kini dikalahkan oleh sehelai kain. Miyuki menggembungkan pipi, lalu hampir tertawa pada bayangannya sendiri."
            miyuki "Jangan mengganggu konsentrasiku. Aku sedang bernegosiasi dengan obi."
            nar "Ia mencoba lagi, kali ini tidak terlalu tegang. Saat rombongan memanggil, ia menyuruh mereka menunggu tanpa membuat alasan tambahan."
            miyuki "Sebentar lagi. Kali ini sungguhan. Mungkin."
    return

# ┌─ PANDUAN CERITA · Mi08 · Sena dan Psikolog
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : Sena memperkenalkan Sato Kyoko.
# │ INTI    : A dukung konsultasi / B tolak / C abaikan.
# │ AKHIRAN : membuka jalur pemulihan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi08:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana")
    nar "Miyuki mengeluarkan kartu kontak Sato Kyoko dari sela buku, lalu mengembalikannya sebelum kau selesai membaca. Sena telah memberikannya tiga hari lalu. Bekas lipatan di sudutnya menunjukkan kartu itu sering dibuka."
    miyuki "Katanya aku boleh datang sebelum semuanya benar-benar buruk. Tapi aku membayangkan duduk di sana dan nggak punya alasan yang cukup."
    nar "Ia menyebut kelelahan sebagai kesibukan biasa, sulit tidur sebagai akibat kopi, dan keinginan menangis sebagai hal yang nanti akan lewat. Setiap penjelasan membuatnya tampak semakin letih."
    call kk_family_menu("Mi08", ["Dukung ia mencoba berkonsultasi.", "Katakan ia tidak butuh itu.", "Abaikan topik itu."])
    if _return == "A":
        nar "Kau mengatakan ia tidak perlu menunggu keadaan memburuk agar boleh membicarakannya. Miyuki mengeluarkan kartu itu lagi."
        miyuki "Aku bisa membuat janji sendiri. Mungkin aku cuma perlu mendengar bahwa itu nggak berlebihan."
        nar "Ia menyimpan nomor Sato ke ponsel, tidak lagi di antara halaman yang mudah dilupakan."
        miyuki "Kalau aku gugup nanti, boleh mengabarimu sesudahnya? Bukan untuk minta dinilai berhasil atau nggak. Cuma kabar."
    elif _return == "B":
        nar "Kau mengatakan ia tidak membutuhkan konsultasi. Miyuki tersenyum lega dengan cepat, terlalu cepat untuk keraguan yang sudah ia bawa berhari-hari."
        miyuki "Iya. Aku cuma perlu mengatur waktu lebih baik."
        nar "Kartu itu kembali ke buku. Kini saat kelelahan datang, ia juga punya suaramu untuk membantu menjelaskan bahwa meminta bantuan akan menjadi sesuatu yang berlebihan."
    else:
        nar "Kau menanyakan jadwal praktik berikutnya. Miyuki menjawab dengan lancar; percakapan tentang hal yang harus dikerjakan selalu lebih mudah daripada hal yang sedang dirasakan."
        nar "Ia tidak mengeluarkan kartu itu lagi. Saat berpisah, ia justru menanyakan apakah kau sudah makan, mengembalikan dirinya pada peran yang tidak membuat siapa pun menunggu jawaban sulit."
    return

# ┌─ PANDUAN CERITA · Mi10 · Omikuji Miyuki
# │ LOKASI  : Alam & Pantai · Kuil
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : ramalan "kesendirian".
# │ INTI    : A hibur / B tertawa / C ambil kesempatan.
# │ AKHIRAN : kerentanan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi10:
    call kk_scene_enter("miyuki", "Kuil · Tahun Baru")
    nar "Miyuki membaca omikuji dalam hati. Ketika seorang teman menanyakan hasilnya, ia menyebut kesehatan dan studi, menyimpan satu bagian sampai kalian tertinggal di dekat bangku kuil."
    miyuki "Kesendirian. Kata yang dipakainya itu. Padahal jadwalku penuh orang setiap hari."
    nar "Ia tertawa kecil, lalu mengaku ada malam ketika tak tahu siapa yang bisa ditelepon tanpa lebih dahulu menyiapkan alasan."
    call kk_family_menu("Mi10", ["Hibur dan temani ia sebentar.", "Tertawakan ramalan yang kebetulan itu.", "Manfaatkan saat ia rapuh."])
    if _return == "A":
        nar "Kau menawarkan duduk sebentar. Miyuki semula hendak menolak karena rombongan menunggu, lalu memeriksa ponsel dan menyampaikan bahwa kalian akan menyusul."
        miyuki "Aku nggak perlu cerita yang menyenangkan dulu supaya boleh ditemani?"
        nar "Ia mengucapkannya seperti gurauan, tetapi menunggu jawaban dengan sungguh-sungguh. Sesudah itu kertas ramalannya dilipat tanpa dibaca ulang."
    elif _return == "B":
        nar "Kau menertawakan ketepatan ramalan umum itu. Miyuki ikut menyebut bahwa semua orang pasti pernah merasa sepi."
        miyuki "Iya. Senpai terlalu mudah terbawa suasana."
        nar "Ia berjalan lebih dahulu untuk menyusul kelompok. Dari samping ia tampak kembali tenang, hanya kertas di tangannya yang makin kecil karena terus dilipat."
    else:
        nar "Kau menerima pengakuannya sebagai kesempatan membuat dirimu tampak satu-satunya orang yang bisa memahami. Miyuki mendekat pada kepastian yang kautawarkan, terlalu lelah untuk memeriksa harga yang menyertainya."
        miyuki "Kalau nanti aku menelepon tanpa alasan penting, kamu benar-benar nggak keberatan?"
        nar "Kau membiarkannya berharap lebih banyak daripada yang sungguh ingin kauberikan. Ketika ia tersenyum lagi, kelegaan itu sudah mulai terikat pada persetujuanmu."
    return

init 1 python:
    def kk_miyuki_hurt_self(delta):
        pts.setdefault("luka_miyuki_diri",15)
        kk_adj("luka_miyuki_diri",delta)

    _hook("Mi04-A", lambda: kk_rel("miyuki","intim",4))
    _hook("Mi04-C", lambda: kk_rel("miyuki","intim",2))
    _hook("Mi08-A", lambda: (kk_flag("miyuki_sato_dikenal"), kk_miyuki_hurt_self(-5)))
    _hook("Mi08-B", lambda: kk_rel("miyuki","trust",-3))
    _hook("Mi10-A", lambda: kk_rel("miyuki","trust",5))
    _hook("Mi10-C", lambda: (kk_miyuki_hurt_self(8), kk_flag("miyuki_disandari")))
