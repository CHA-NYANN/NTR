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
    nar "Miyuki berdiri membelakangi cermin dengan dua ujung obi di tangan. Ia mencoba melihat simpulnya melalui bahu, lalu mendesah ketika kain itu kembali melorot."
    miyuki "Aku bisa menghafal halaman-halaman anatomi. Ternyata kain sepanjang ini punya rencana sendiri."
    nar "Di luar ruang ganti, rombongan mulai memanggil. Ia menjawab sebentar lagi dengan suara senpai yang sangat meyakinkan, lalu menatapmu meminta tolong."
    call kk_family_menu("Mi04", ["Bantu rapikan talinya dengan hati-hati.", "Panggil Sena untuk membantunya.", "Goda kecanggungannya."])
    if _return == "A":
        nar "Kau menanyakan apakah boleh membantu sebelum mendekat. Miyuki mengangguk dan mengangkat rambut agar kainnya terlihat."
        miyuki "Jangan terlalu kencang. Aku masih ingin makan semua yang tadi kulihat di stan."
        nar "Kau merapikannya perlahan sambil meminta ia memeriksa kenyamanannya. Sesudah selesai, ia tetap berdiri dekat sesaat lebih lama."
        miyuki "Terima kasih. Senpai boleh nggak pandai satu hal di depanmu, ya."
    elif _return == "B":
        nar "Kau memanggil Sena. Ia datang, menahan tawa ketika melihat simpul yang nyaris terbalik, lalu mengambil alih dengan cekatan."
        "Sena" "Lain kali minta tolong sebelum lima kali membongkar, boleh?"
        miyuki "Aku ingin mencoba sendiri dulu. Lima kali itu masih mencoba."
        nar "Ketika keluar, Miyuki berterima kasih kepadamu. Wajahnya sedikit malu, tetapi ia tidak lagi harus membuktikan bisa menyelesaikan semuanya sendiri sebelum menikmati festival."
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
