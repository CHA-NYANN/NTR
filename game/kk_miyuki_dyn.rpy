# Event dinamis Miyuki (Mi-D05, Mi-D06, Mi-D07, Mi-D08, Mi-D10, Mi-D14).
# Melanjutkan arc luka-diri/karier Miyuki (luka_miyuki_diri, kelelahan_miyuki,
# omiai_takeru) yang sudah ada. Beat perawatan ditulis sebagai pemulihan; cabang
# gelap (menuruti hukuman-diri, merekam diam-diam, menekan Koita) ditulis sebagai
# KONSEKUENSI dan KARAKTER saja, tanpa metode. Gerbang yuri (Mi-D13) tidak dibuka.
# Nilai prototipe; mengikuti Event_Miyuki. Sena & Sato Kyoko memakai nama-penutur.

# --- 3 pilihan ------------------------------------------------------------
# ┌─ PANDUAN CERITA · Mi-D05 · Tangga Darurat Jam Tiga
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Tachibana Miyuki
# │ AWALAN  : Tahun 3; jaga malam; luka[[diri] ≥ 50; pemain di RS saat Dini Hari
# │ INTI    : A Duduk di sebelahnya / B panggil Sena / C pergi diam-diam
# │ AKHIRAN : luka[[diri] −15 / Sena menjadi sekutu / tidak ada
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi_D05:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana · Tangga darurat")
    nar "Pintu tangga darurat menutup dengan desis pelan. Miyuki duduk di anak tangga paling bawah, dekat lantai, memegang teh yang belum dibuka. Jam di ponselnya menunjukkan lewat pukul tiga."
    miyuki "Aku tahu harus kembali sebentar lagi. Di sini nggak ada yang bertanya apa pun selama satu menit. Ternyata aku ingin sekali satu menit itu."
    nar "Ia bergeser ketika melihatmu, belum jelas sedang menawarkan tempat atau bersiap berdiri agar tak dianggap mengabaikan tugas."
    call kk_family_menu("Mi-D05", ["Duduk di sebelahnya tanpa banyak kata.", "Panggilkan Sena, rekannya.", "Pergi diam-diam agar ia sendiri."])
    if _return == "A":
        nar "Kau duduk dengan satu anak tangga di antara kalian. Miyuki menunggu pertanyaan, kemudian pelan-pelan melepaskan napas ketika tidak ada yang menuntut cerita."
        miyuki "Aku tadi merasa harus menjelaskan kenapa belum masuk. Padahal kamu bahkan belum bertanya."
        nar "Kau menunjukkan teh di tangannya. Ia membukanya setelah sadar sejak tadi hanya memegang."
        miyuki "Boleh sampai minuman ini habis? Setelah itu aku bisa pikirkan langkah berikutnya."
    elif _return == "B":
        nar "Kau memberi tahu Miyuki sebelum memanggil Sena. Ia sempat ingin menolak karena merasa merepotkan, lalu mengangguk kecil."
        "Sena" "Aku bisa duduk sebentar. Setelah itu kita lihat jadwalmu, ya. Jangan tambah tugas dulu."
        miyuki "Aku nggak tahu aku butuh apa."
        "Sena" "Kalau begitu kita mulai dari nggak sendirian di sini."
        nar "Miyuki menurunkan bahu. Ia tidak lagi harus menyusun alasan sempurna agar seseorang tetap tinggal."
    else:
        nar "Kau mundur sebelum ia melihatmu dengan jelas. Pintu kembali menutup, menyisakan bayangannya dalam celah kaca sempit."
        nar "Miyuki tetap duduk sampai teh di tangannya kehilangan dingin. Saat akhirnya masuk lagi, ia sudah menyiapkan jawaban bahwa tadi hanya mencari udara. Tidak ada orang yang mengetahui seberapa lama satu menitnya berubah menjadi penantian."
    return

# ┌─ PANDUAN CERITA · Mi-D10 · Resep yang Salah Tulis
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Tachibana Miyuki
# │ AWALAN  : kelelahan ≥ 85
# │ INTI    : A Paksa ia cuti / B bantu menyembunyikan / C laporkan ke pembimbing
# │ AKHIRAN : menyembunyikan lalu ketahuan: E-MI-06 menguat; cuti: E-MI-10 menguat
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi_D10:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana · Ruang resep")
    nar "Sena menahan lembar resep sebelum diserahkan untuk pemeriksaan berikutnya. Ada kesalahan pada tulisan Miyuki. Ia membacanya, mengoreksi, lalu membaca ulang seolah tidak mengenali gerakan tangannya sendiri."
    miyuki "Aku tahu yang benar. Aku bisa menjelaskan. Tadi tanganku..."
    "Sena" "Belum sampai ke pasien. Sekarang berhenti dulu. Kamu perlu didampingi pembimbing."
    nar "Miyuki tidak mendengar kelegaan pada kalimat pertama. Ia hanya mendengar bahwa sesuatu yang buruk hampir terjadi dan namanya ada di situ."
    call kk_family_menu("Mi-D10", ["Paksa ia mengambil cuti.", "Bantu ia menyembunyikannya.", "Laporkan ke pembimbing demi keselamatan pasien."])
    if _return == "A":
        nar "Kau bersikeras ia berhenti dan mengambil cuti, bukan kembali membuktikan diri pada jadwal berikutnya. Miyuki marah sebentar, lalu terlalu lelah untuk mempertahankan penyangkalan."
        miyuki "Aku takut kalau berhenti, aku nggak bisa kembali. Tapi kalau terus begini... aku juga takut."
        nar "Ia meminta Sena menemani membicarakan cuti. Keputusan itu tidak membuatnya langsung tenang, tetapi lembar berikutnya tidak lagi ia tangani dengan tangan yang gemetar."
    elif _return == "B":
        nar "Kau membantu mengecilkan kejadian itu menjadi sesuatu yang seolah tidak perlu dibicarakan lebih jauh. Miyuki menerima jalan keluar tersebut dengan lega yang segera berubah menjadi takut ketahuan."
        "Sena" "Ini tetap harus ditangani. Aku nggak akan menyebut kelelahan yang membahayakan pasien sebagai rahasia pribadi kalian."
        nar "Miyuki kini menanggung dua hal sekaligus: kesalahan yang hampir terjadi dan keputusan untuk mencoba menutupinya. Jadwal yang membuatnya kelelahan belum mendapatkan alasan yang jujur untuk berubah."
    else:
        nar "Kau menyampaikan kejadian kepada pembimbing, membatasi laporan pada apa yang benar-benar kauketahui. Miyuki tetap berada di sana ketika rencana tindak lanjut dibicarakan."
        miyuki "Aku malu sekali. Tapi aku nggak mau ada pasien yang menanggung karena aku takut malu."
        "Sena" "Kita urus jadwal dan pengawasannya. Kamu nggak perlu menyelesaikan ini dengan menghukum diri sendiri."
        nar "Miyuki mengangguk, kali ini pada rencana yang punya langkah berikutnya, bukan pada tuduhan bahwa dirinya selalu kurang."
    return

# ┌─ PANDUAN CERITA · Mi-D14 · Jaga untuk Pemain
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Tachibana Miyuki
# │ AWALAN  : pemain Ambruk atau sakit; tahap ≤ 3
# │ INTI    : A Terima / B tolak / C minta ia pulang tidur
# │ AKHIRAN : tahap ≤ 3: ia merasa dibutuhkan dengan sehat; tahap 4+: kelelahan naik
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi_D14:
    call kk_scene_enter("miyuki", "Kamar pemain · Demam")
    nar "Miyuki tiba dengan kantong makanan, air minum, dan pertanyaan yang memintamu menjawab jujur alih-alih mengatakan masih sanggup. Ia memeriksa apakah kau sudah mendapat pertolongan yang diperlukan, lalu menarik kursi mendekat."
    miyuki "Aku bisa tinggal sebentar. Jangan pakai tenaga untuk kelihatan sehat di depanku. Sayang sekali aktingmu jelek kalau demam."
    nar "Godaan itu lembut. Di bawahnya ada kekhawatiran yang tidak ia coba jadikan alasan mengambil alih seluruh kamarmu."
    call kk_family_menu("Mi-D14", ["Terima perawatannya.", "Tolak, suruh ia tidak repot.", "Minta ia pulang beristirahat."])
    if _return == "A":
        nar "Kau menerima bantuannya dan menyebut hal yang benar-benar diperlukan. Miyuki mengangguk, tampak senang tidak harus menebak."
        miyuki "Baik. Makan sedikit dulu, nanti istirahat. Kalau butuh diperiksa lagi, kita cari bantuan. Aku masih belajar, jadi jangan jadikan aku alasan menunda."
        nar "Ia menunggu sampai kau bisa beristirahat. Kehadirannya kali ini punya tugas yang jelas dan akhir yang boleh ia tentukan sendiri."
    elif _return == "B":
        nar "Kau menolak karena tidak ingin merepotkan. Miyuki menurunkan kantong yang baru diangkat, senyumnya mengecil."
        miyuki "Aku datang karena mau. Tapi kalau kamu nggak ingin ditemani, aku akan hormati."
        nar "Ia meninggalkan barang yang kaubersedia terima dan menanyakan siapa yang bisa kauhubungi jika keadaan berubah. Saat pergi ia tidak memaksa, meski penolakan itu masih terasa lebih pribadi baginya daripada maksudmu."
    else:
        nar "Kau melihat lelah di wajahnya dan memintanya pulang tidur. Miyuki hendak menawarkan satu jam lagi, kemudian berhenti."
        miyuki "Iya. Aku juga perlu istirahat. Kamu kabari kalau butuh bantuan lain, ya. Bukan harus dariku terus."
        nar "Kalian menyepakati kabar singkat besok. Ia pulang dengan tenang yang masih baru: seseorang menerima kepeduliannya tanpa meminta ia menghabiskan diri sebagai bukti."
    return

# --- 4 pilihan (panel manual) --------------------------------------------
# ┌─ PANDUAN CERITA · Mi-D06 · Teguran yang Ia Minta
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Tachibana Miyuki
# │ AWALAN  : tahap ≥ 3; luka[[pemain] ≥ 40
# │ INTI    : A Aku pantas." Tolak dengan lembut / B turuti / C alihkan / D bawa ke Sato
# │ AKHIRAN : persimpangan utama; lihat Sistem_Cabang_dan_Poin §5.3
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi_D06:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana · Lorong sepi")
    nar "Miyuki menunggu sampai lorong sepi sebelum memintamu tinggal. Ia menjelaskan kesalahan kecil yang tadi sudah selesai, lalu menanyakan apakah kau kecewa. Jawaban yang tidak terdengar cukup keras justru membuatnya gelisah."
    miyuki "Bilang saja aku bodoh. Kalau kamu yang mengatakannya, aku tahu harus menerima apa. Aku capek menunggu tanpa tahu kapan selesai."
    nar "Ia menatapmu dengan permintaan yang mengerikan justru karena terdengar begitu masuk akal baginya."
    python:
        _caps = ["Tolak dengan lembut; ia tidak pantas itu.", "Turuti permintaannya.", "Alihkan ke hal lain.", "Ajak ia menemui Sato Kyoko."]
        _rows = [(cap, Return(key), False) for key, cap in zip("ABCD", _caps)]
    call screen kk_choice_panel(_rows, "Tanggapi Miyuki")
    $ _key = _return
    $ kk_family_choice("Mi-D06", _key)
    if _key == "A":
        nar "Kau menolak merendahkannya, tetap tinggal ketika wajahnya berubah takut. Miyuki mengulang bahwa ia tidak keberatan, seolah sedang menawarkan syarat yang lebih mudah."
        miyuki "Kalau kamu nggak marah, bukan berarti kamu sudah nggak peduli?"
        nar "Kau menjawab pertanyaannya, tidak memenuhi permintaan yang melukainya. Ia terdiam lama. Menerima perhatian tanpa hukuman ternyata memerlukan keberanian yang belum ia punya seluruhnya."
    elif _key == "B":
        nar "Kau menuruti. Miyuki menunduk, lalu tampak lega ketika mendapatkan bentuk perhatian yang sudah ia pahami. Kelegaan itu tidak membuat apa yang baru terjadi menjadi sehat."
        miyuki "Terima kasih sudah jujur. Aku akan lebih baik."
        nar "Ia berterima kasih atas penghinaan. Sesudahnya ia lebih cepat mencari persetujuanmu, lebih sulit percaya pada keramahan yang tidak menuntut penebusan."
    elif _key == "C":
        nar "Kau mengalihkan topik ke makanan dan jadwal. Miyuki mengikuti, mengingat detail yang kausampaikan dengan perhatian berlebihan."
        miyuki "Baik. Jadi kita nggak membahasnya lagi?"
        nar "Ia tidak menanyakan karena sudah tenang. Ia sedang memastikan apakah pembicaraan yang belum selesai itu akan kembali pada saat yang tidak bisa ia duga."
    else:
        nar "Kau mengajaknya menemui Sato dan menunggu ia bersedia. Pada pertemuan itu, Miyuki mengulang permintaannya dengan malu yang hampir membuat kalimatnya tak terdengar."
        "Sato Kyoko" "Saat kamu meminta dimarahi, apa yang kamu harapkan berhenti sesudahnya? Kita bisa mulai dari situ."
        nar "Miyuki tidak langsung menjawab. Tetapi tidak seorang pun menghukumnya karena perlu waktu, dan itu menjadi pengalaman pertama yang bisa ia bawa pulang dari percakapan tersebut."
    $ kk_minutes(10)
    return

# ┌─ PANDUAN CERITA · Mi-D07 · Hayase di Kafe
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Tachibana Miyuki
# │ AWALAN  : omiai_takeru ≥ 40; pemain di Kafe Komorebi hari Sabtu
# │ INTI    : A Hadapi / B bersekutu / C pancing ia jujur / D rekam diam-diam
# │ AKHIRAN : Takeru bisa mengaku ia tidak mencintai Miyuki; rekaman menjadi bukti sekaligus risiko
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi_D07:
    call kk_scene_enter("miyuki", "Kafe Komorebi · Sabtu")
    nar "Takeru memilih meja Komorebi yang cukup jauh dari pintu. Ia belum memesan untukmu, tetapi sudah menyediakan kursi seolah pertemuan ini bagian jadwal yang akan kauikuti."
    "Takeru" "Kau dekat dengan Miyuki. Aku ingin tahu apakah kita bisa menghindari masalah yang tidak perlu."
    nar "Ia menyebut dua keluarga, hubungan lama, dan harapan orang tua sebelum sekali pun menyebut apa yang diinginkan Miyuki sendiri."
    python:
        _caps = ["Hadapi ia terus terang.", "Pura-pura bersekutu dengannya.", "Pancing ia bicara jujur.", "Rekam pembicaraan diam-diam."]
        _rows = [(cap, Return(key), False) for key, cap in zip("ABCD", _caps)]
    call screen kk_choice_panel(_rows, "Hadapi Takeru")
    $ _key = _return
    $ kk_family_choice("Mi-D07", _key)
    if _key == "A":
        nar "Kau menanyakan langsung apakah ia mencintai Miyuki. Takeru meletakkan sendok, tampak kesal karena percakapan yang dianggapnya praktis dibawa ke sana."
        "Takeru" "Tidak. Aku menghormatinya. Keluarga kami menganggap itu cukup untuk memulai."
        nar "Kau mengatakan Miyuki berhak menentukan apakah cukup. Ia memandang keluar, lalu mengakui bahwa pertanyaan itulah yang paling jarang diajukan dalam pertemuan keluarga."
    elif _key == "B":
        nar "Kau menampilkan sikap seolah bersedia bekerja sama. Takeru mengendur, membicarakan rencana keluarga sebagai urusan yang bisa kalian permudah berdua."
        "Takeru" "Bagus. Aku tidak ingin membuat keadaan sulit. Miyuki juga selalu berusaha memahami."
        nar "Ia tidak menyadari persetujuanmu hanya sandiwara. Di antara cangkir, kehidupan Miyuki kembali diperlakukan sebagai sesuatu yang bisa dibahas orang dekat tanpa perlu menghadirkannya."
    elif _key == "C":
        nar "Kau menanyakan apa yang akan ia pilih jika tidak perlu menjawab kepada keluarganya. Takeru lama tidak menyentuh kopi."
        "Takeru" "Aku juga ingin memilih sendiri. Tapi setiap kubilang begitu, mereka bertanya apakah aku punya alasan yang lebih baik."
        nar "Ia terdengar lebih muda ketika berhenti berbicara atas nama dua keluarga. Pengakuan itu memberinya tanggung jawab baru: ia tidak lagi bisa menganggap kepatuhan Miyuki sebagai bukti bahwa rencana tersebut baik bagi mereka berdua."
    else:
        nar "Pembicaraan itu tersimpan dalam rekaman tanpa sepengetahuannya. Takeru menyebut tidak mencintai Miyuki dan menganggap hubungan tersebut kepentingan keluarga."
        nar "Bukti kini ada di tanganmu, bersama persoalan baru tentang bagaimana ia diperoleh dan siapa yang berhak menentukan penggunaannya. Menyimpan suara seseorang tidak otomatis memberimu hak mengambil keputusan atas nama Miyuki."
    $ kk_minutes(10)
    return

# ┌─ PANDUAN CERITA · Mi-D08 · Rahasia di Konbini
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Tachibana Miyuki
# │ AWALAN  : Koita lelah atau mabuk; koita_sadar ≥ 25
# │ INTI    : A Simpan / B ceritakan ke Miyuki / C pakai untuk menekan Koita / D dorong Koita mengaku sendiri
# │ AKHIRAN : bendera rahasia_koita_sma; bila Koita mengaku sendiri, cinta_koita bisa +20 atau Miyuki justru kesal, tergantung tahapnya
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi_D08:
    call kk_scene_enter("koita", "Konbini · 03:00")
    nar "Lampu konbini membuat wajah Koita terlihat lebih pucat daripada biasanya. Ia belum menghabiskan air mineralnya ketika bercerita tentang kelompok belajar SMA dan senpai yang selalu terlihat lebih tahu harus berbuat apa."
    koita "Aku dulu suka Miyuki. Sungguh. Terus aku berpikir dia pantas dapat orang yang lebih... jelas. Lebih hebat."
    nar "Ia tertawa kecil, lelah dan kurang waspada."
    koita "Akhirnya aku jadi orang yang paling nggak jelas. Aku dekat terus, supaya nggak perlu tahu apakah dia akan menolak."
    python:
        _caps = ["Simpan untuk diri sendiri.", "Ceritakan pada Miyuki.", "Pakai untuk menekan Koita.", "Dorong Koita mengaku sendiri."]
        _rows = [(cap, Return(key), False) for key, cap in zip("ABCD", _caps)]
    call screen kk_choice_panel(_rows, "Apa yang kau lakukan dengan pengakuan itu?")
    $ _key = _return
    $ kk_family_choice("Mi-D08", _key)
    if _key == "A":
        nar "Kau menyimpan pengakuan itu. Koita melanjutkan kisah yang berpindah-pindah, tidak tahu kalimat mana yang akan kaubawa pulang."
        nar "Besok ia mungkin menganggap malam ini sekadar percakapan saat lelah. Kau tahu ada nama dari masa lalu yang masih memengaruhi cara ia menghindari keputusan hari ini."
    elif _key == "B":
        nar "Kau menceritakannya kepada Miyuki ketika ada waktu bicara. Ia mendengar tanpa senyum yang kaubayangkan akan muncul."
        miyuki "Aku ingin mendengar itu darinya. Dulu, atau sekarang. Bukan karena orang lain akhirnya membawakan kalimat yang dia simpan."
        nar "Ia berterima kasih atas kabarnya, tetapi meminta waktu sebelum membicarakan apa artinya. Perasaan masa lalu tidak otomatis menjawab luka penantian yang berlangsung sesudahnya."
    elif _key == "C":
        nar "Kau membuat Koita sadar pengakuannya bisa kaugunakan untuk mengatur langkahnya. Ia menegakkan tubuh, mabuk atau lelah tidak lagi cukup untuk menyembunyikan takut di wajahnya."
        koita "Aku cerita karena kukira kamu temanku."
        nar "Ia memegang botol sampai plastiknya berbunyi. Sesudah malam ini, setiap keinginan untuk bicara kepadamu akan disertai ingatan bahwa kejujuran pernah diubah menjadi alat menahan dirinya."
    else:
        nar "Kau mendorongnya mengatakannya sendiri ketika sudah cukup jernih untuk bertanggung jawab atas perkataannya. Bukan mengirim pesan tengah malam lalu menganggapnya selesai."
        koita "Aku juga harus menjelaskan kenapa selama ini diam. Itu bagian yang kutakuti."
        nar "Ia menutup botol dan menyimpan ponsel tanpa mengetik. Keberanian yang kausarankan tidak menjanjikan penerimaan; ia tetap harus datang dengan kemungkinan membuat Miyuki justru lebih marah."
    $ kk_minutes(10)
    return

init 1 python:
    # Mi-D05 tangga darurat (pemulihan)
    _hook("Mi-D05-A", lambda: (kk_miyuki_hurt_self(-15), kk_rel("miyuki","intim",4)))
    _hook("Mi-D05-B", lambda: kk_flag("sena_sekutu"))
    _hook("Mi-D05-C", lambda: kk_rel("miyuki","trust",-4))
    # Mi-D06 teguran yang ia minta (persimpangan)
    _hook("Mi-D06-A", lambda: (kk_rel("miyuki","trust",5), kk_flag("miyuki_ditolak_merendah")))
    _hook("Mi-D06-B", lambda: (kk_miyuki_hurt_self(12), kk_flag("miyuki_direndahkan")))
    _hook("Mi-D06-C", lambda: kk_rel("miyuki","trust",2))
    _hook("Mi-D06-D", lambda: (kk_miyuki_hurt_self(-10), kk_flag("miyuki_sato_dikenal")))
    # Mi-D07 Hayase di kafe
    _hook("Mi-D07-A", lambda: (kk_adj("omiai_takeru",-10), kk_flag("takeru_dihadapi")))
    _hook("Mi-D07-B", lambda: kk_flag("takeru_sekutu_palsu"))
    _hook("Mi-D07-C", lambda: (kk_adj("omiai_takeru",-15), kk_flag("takeru_mengaku")))
    _hook("Mi-D07-D", lambda: (kk_flag("rekaman_takeru"), kk_flag("takeru_mengaku")))
    # Mi-D08 rahasia konbini
    _hook("Mi-D08-A", lambda: kk_flag("rahasia_koita_sma"))
    _hook("Mi-D08-B", lambda: (kk_flag("rahasia_koita_sma"), kk_rel("miyuki","trust",-3)))
    _hook("Mi-D08-C", lambda: (kk_flag("rahasia_koita_sma"), kk_koita_fear(8)))
    _hook("Mi-D08-D", lambda: (kk_flag("rahasia_koita_sma"), kk_flag("koita_dorong_jujur")))
    # Mi-D10 resep salah tulis
    _hook("Mi-D10-A", lambda: (kk_adj("kelelahan_miyuki",-30), kk_flag("miyuki_cuti")))
    _hook("Mi-D10-B", lambda: kk_flag("resep_disembunyikan"))
    _hook("Mi-D10-C", lambda: (kk_rel("miyuki","trust",4), kk_flag("miyuki_dilaporkan_demi_pasien")))
    # Mi-D14 jaga untuk pemain
    _hook("Mi-D14-A", lambda: (kk_rel("miyuki","intim",5), kk_flag("miyuki_merawat_pemain")))
    _hook("Mi-D14-B", lambda: kk_rel("miyuki","trust",-2))
    _hook("Mi-D14-C", lambda: kk_rel("miyuki","trust",3))
