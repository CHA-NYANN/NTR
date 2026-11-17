# Arc Shiori endgame (S04, S05, S20-S24): dari pertandingan shogi dan kemunculan
# pewaris Tojo, menuju klimaks "penghancuran" tempat Shiori membalas kebohongan
# yang ia deteksi. Ditulis sebagai KARAKTER dan KONSEKUENSI (shogi sebagai metafora
# strategi sosial); manuver balasnya dicatat sebagai akibat, bukan panduan. Jalur
# jujur/mengaku/bersekutu tersedia. Penempatan Klub Catur prototipe; Tojo pakai
# nama-penutur. Mengikuti Event_Shiori; melengkapi S07/S09/S13-S19 (Codex) + S-D.

# ┌─ PANDUAN CERITA · S04 · Pertandingan Malam di Vila
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia bermain shogi sampai larut.
# │ INTI    : A temani / B menang jujur / C menyontek.
# │ AKHIRAN : C masuk daftar kebohongan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S04:
    call kk_scene_enter("shiori", "Klub Catur · Pertandingan malam vila")
    nar "Shiori menyusun ulang posisi terakhir di vila ketika orang lain sudah mulai tidur. Ia menemukan kesalahan sendiri dan tampak lebih tertarik daripada kesal."
    shiori "Aku bisa menyalahkan lelah. Tapi langkah buruknya tetap kulakukan dalam keadaan sadar. Kau masih mau bermain, atau sudah terlalu mengantuk untuk menolak dengan sopan?"
    call kk_family_menu("S04", ["Temani ia bermain sampai puas.", "Menang dengan jujur.", "Menang dengan menyontek langkah."])
    if _return == "A":
        shiori "Kau bertahan sampai selarut ini? ...Tidak banyak yang mau. Aku mengingatnya."
        nar "Kalian bermain sampai menyepakati batas waktu. Ketika tiba saat berhenti, Shiori tidak memperlakukan kebutuhan tidur sebagai kekalahan. Ia menghargai pertandingan yang sungguh dipilih, bukan ketahanan untuk terus menyenangkan dirinya."
    elif _return == "B":
        shiori "Kau mengalahkanku bersih. ...Bagus. Aku benci menang melawan orang yang mengalah."
        nar "Ia meminta melihat titik yang terlewat, lalu tertawa ketika menyadari justru keputusan paling diyakininya membuka jalan bagimu. Kalah membuatnya ingin mengenal cara pikirmu, bukan merendahkanmu agar hasilnya terasa lebih kecil."
    else:
        nar "Kau curang dan mendapatkan kemenangan. Shiori mengucapkan selamat, kemudian meminta penjelasan satu keputusan yang tidak sesuai pola permainanmu."
        nar "Ia belum menuduh. Namun jawabanmu kini harus hidup bersama ingatannya tentang kejadian, dan senyum penutupnya tidak menghapus selisih di antara keduanya."
    return

# ┌─ PANDUAN CERITA · S05 · Tojo Akihiro di Pesta
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : pewaris Tojo mendekatinya.
# │ INTI    : A lindungi / B abaikan / C manfaatkan.
# │ AKHIRAN : tojo_aktif.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S05:
    call kk_scene_enter("shiori", "Klub Catur · Tojo di pesta")
    nar "Tojo Akihiro mendekati Shiori di pesta dengan kemudahan seseorang yang lingkungannya telah sering membicarakan kecocokan dua keluarga. Shiori menyambut sopan tanpa memberikan persetujuan yang dianggap sudah disiapkan."
    nar "Orang tuanya tidak memaksanya menerima. Tekanan datang dari kerumunan yang memperlakukan kemungkinan sebagai sesuatu yang tinggal menunggu diumumkan."
    "Tojo" "Saionji-san. Keluarga kita punya banyak hal untuk dibicarakan. ...Dan temanmu ini siapa?"
    call kk_family_menu("S05", ["Lindungi Shiori dari pendekatan Tojo.", "Abaikan; itu urusan keluarganya.", "Manfaatkan kehadiran Tojo untuk keuntunganmu."])
    if _return == "A":
        shiori "Kau berdiri di antara kami? ...Berani. Tojo tidak terbiasa dihalangi."
        nar "Kau membuka ruang agar Shiori dapat mengakhiri percakapan sendiri. Ia tidak berpura-pura tak mampu menolak, tetapi lega tidak harus menghadapi seluruh acara sendirian."
    elif _return == "B":
        shiori "Kau mundur. Masuk akal. ...Tapi aku mencatat siapa yang tetap diam saat aku terdesak."
        nar "Ia mengakhiri percakapan dengan Tojo tanpa bantuanmu. Setelahnya ia tidak menghukum kepergianmu dengan keributan, hanya lebih jelas tentang bagian hidup yang belum ingin dibagikan kepadamu."
    else:
        nar "Kau memakai situasi itu untuk membuka akses bagi dirimu. Shiori melihat nadamu menjadi lebih ramah saat pembicaraan menyentuh koneksi dan keuntungan."
        shiori "Kalau ingin dikenalkan, tanyakan kepadaku. Jangan gunakan ketidaknyamananku sebagai pintu masuk lalu menyebutnya membantu."
    return

# ┌─ PANDUAN CERITA · S20 · Permainan Terakhir
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : shogi di vila.
# │ INTI    : A bertanding / B mengalah / C menolak.
# │ AKHIRAN : pesan tersirat.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S20:
    call kk_scene_enter("shiori", "Klub Catur · Permainan terakhir")
    nar "Shiori menyiapkan papan tanpa memulai. Yang berbeda adalah cara ia menunggu sampai kau benar-benar melihatnya."
    shiori "Satu pertandingan lagi. Aku ingin tahu apakah kita masih bisa saling mendengar. Kalau ada pesan yang tidak sampai lewat permainan, kita bicara sesudahnya."
    call kk_family_menu("S20", ["Bertanding sungguh-sungguh.", "Sengaja mengalah untuk membaca niatnya.", "Menolak bermain."])
    if _return == "A":
        shiori "Kau menjawab dengan permainan penuh. ...Pesanku sampai, dan kau membalas setara."
        nar "Kalian mengambil risiko yang dapat dibaca. Sesudahnya ia menyebut satu hal tentang hubungan kalian yang belum berani dikatakan sebelum pertandingan. Papan menjadi pembuka percakapan, bukan penggantinya."
    elif _return == "B":
        shiori "Kau mengalah? ...Kau pikir aku tidak akan sadar? Jangan hina aku dengan kemenangan murahan."
        nar "Ia menolak melanjutkan seolah hasil itu nyata. Keinginanmu membaca dirinya sambil menyembunyikan keseriusan sendiri terasa lebih merendahkan daripada kekalahan."
    else:
        nar "Kau menolak. Shiori menerima dan memasukkan bidak tanpa membanting."
        shiori "Baik. Aku tidak akan menyebutnya kesalahan karena menginginkan jawaban lain. Tapi malam ini aku juga tidak ingin mencari cara memulai pembicaraan lagi."
    return

# ┌─ PANDUAN CERITA · S21 · Pengumuman: Tojo
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : Tojo diumumkan sebagai calon tunangan.
# │ INTI    : A halangi / B dukung / C manfaatkan.
# │ AKHIRAN : Shiori memakai Tojo sebagai bidak.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S21:
    call kk_scene_enter("shiori", "Klub Catur · Pengumuman Tojo")
    nar "Tojo diumumkan sebagai calon tunangan dalam lingkungan yang terlalu cepat menyebut rencana sosial sebagai akhir bahagia. Shiori bisa membatalkannya dengan dukungan keluarga, tetapi justru mempertimbangkan manfaat mempertahankannya."
    shiori "Jangan kasihan. Aku punya pilihan. Yang sulit adalah memastikan aku tidak memilih sesuatu yang melukaiku hanya karena dapat kupakai melukai orang lain."
    call kk_family_menu("S21", ["Halangi pertunangan itu.", "Dukung langkahnya memakai Tojo.", "Manfaatkan situasi untuk dirimu."])
    if _return == "A":
        shiori "Kau mau menghalanginya untukku? ...Hati-hati. Menolong Saionji ada harganya."
        nar "Kau menanyakan apakah ia ingin berhenti sebelum bertindak. Shiori mengakui ada bagian rencana yang hanya dipertahankan agar ia tidak harus mengatakan betapa kecewanya."
    elif _return == "B":
        shiori "Kau mendukungku memainkan ini? ...Baik. Kita lihat siapa yang jadi raja di akhir papan."
        nar "Dukunganmu memudahkan ia membicarakan orang sebagai alat. Tojo memperoleh pengumuman; Shiori memperoleh akses. Keinginan benar-benar mengenal tidak lagi dianggap perlu."
    else:
        nar "Kau mencari keuntungan bagi dirimu. Shiori mendengarkan, lalu menanyakan apakah satu pun bagian rencanamu mempertimbangkan kehendaknya."
        nar "Ia tidak perlu melarangmu bergerak untuk mulai memperlakukanmu sebagai pihak yang harus diantisipasi."
    return

# ┌─ PANDUAN CERITA · S22 · Penghancuran Dimulai
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia bergerak.
# │ INTI    : A melawan / B mengaku / C lari.
# │ AKHIRAN : stage 5.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S22:
    call kk_scene_enter("shiori", "Klub Catur · Penghancuran dimulai")
    nar "Shiori meletakkan catatan peristiwa di meja, tidak cukup dekat untuk kauambil. Ada bagian yang segera kaukenali dan bagian yang menunjukkan selama ini ia jauh lebih banyak mendengar daripada yang terlihat."
    shiori "Aku meminta penjelasan. Beberapa kali. Sekarang aku berhenti menganggap menunggu sebagai kewajiban agar kamu tetap sempat menyusun cerita yang lebih nyaman."
    call kk_family_menu("S22", ["Melawan langkahnya.", "Mengaku semua yang kausembunyikan.", "Lari dari konfrontasi."])
    if _return == "A":
        shiori "Kau melawan? Bagus. Permainan yang menyerah terlalu dini membosankan."
        nar "Kau membantah dan mempertahankan tempatmu. Shiori tidak menjawab setiap serangan, cukup menunjukkan satu kontradiksi yang membuat pembelaan berikutnya sulit dimulai. Percakapan kini dibentuk keinginan menang, bukan pulih."
    elif _return == "B":
        shiori "Kau mengaku sekarang, saat sudah terdesak? ...Setidaknya itu langkah jujur yang pertama."
        nar "Ia meminta keterangan konkret, bukan janji semua akan baik. Kau menyebut perbuatan dan akibatnya, menanggung jeda ketika ia perlu berhenti mendengar. Kerusakan belum batal; satu kebohongan baru berhenti ditambahkan."
    else:
        nar "Kau pergi sebelum selesai. Shiori tidak menghalangi atau mengejar. Sesudahnya, kesempatan menjelaskan tidak lagi datang melalui undangan pribadi darinya."
        nar "Orang lain kini dapat menanyakan hal yang selama ini ia coba dengar langsung. Tak semuanya akan memberi kesabaran yang sama."
    return

# ┌─ PANDUAN CERITA · S23 · Turnamen Akhir
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia menang.
# │ INTI    : A hadir / B gagal / C mengganggu.
# │ AKHIRAN : reputasi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S23:
    call kk_scene_enter("shiori", "Klub Catur · Turnamen akhir")
    nar "Shiori melaju ke babak akhir turnamen. Keluarganya mengirim kabar bangga tanpa menjanjikan bahwa hasilnya akan menentukan nilai dirinya. Ia membacanya, tersenyum, lalu memusatkan diri pada permainan yang memang ingin dimenangkan."
    call kk_family_menu("S23", ["Hadir mendukungnya.", "Biarkan ia gagal tanpa dukungan.", "Ganggu konsentrasinya."])
    if _return == "A":
        shiori "Kamu datang. Aku senang. Itu tidak menjamin aku menang, tentu saja. Tapi aku ingin kamu melihat saat aku mencoba sungguh-sungguh."
        nar "Kau tetap menonton pada bagian lambat, tidak hanya datang untuk tepuk tangan. Sesudahnya ia menghampiri dengan satu keputusan yang ingin dibahas, lebih senang mendapat pendapatmu daripada pujian yang tidak memerhatikan permainan."
    elif _return == "B":
        nar "Tanpa satu wajah yang ia percaya di antara penonton, permainannya kehilangan satu derajat ketajaman."
        nar "Ia perlu waktu mengembalikan perhatian pada papan. Ketidakhadiranmu tidak boleh dijadikan penjelasan seluruh hasil, tetapi ia tetap merasakan kehilangan kecil di tempat yang semula berharap akan terisi."
    else:
        nar "Gangguanmu menarik perhatian petugas. Shiori menunggu persoalan ditangani sebelum melanjutkan, menahan marah yang tak ingin dibawa ke keputusan berikutnya."
        nar "Ia tetap menang. Sesudahnya, tidak ada keramahan pribadi yang bisa kaupanggil untuk mengecilkan perbuatan tersebut sebagai gurauan."
    return

# ┌─ PANDUAN CERITA · S24 · Natal: Skakmat
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : puncaknya.
# │ INTI    : A menyerah / B membalas / C menjadi sekutu.
# │ AKHIRAN : menentukan ending.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S24:
    call kk_scene_enter("shiori", "Klub Catur · Natal, skakmat")
    nar "Pada malam Natal itu Shiori tidak menyiapkan papan. Ia membicarakan akibat yang sudah bergerak dan bagian terakhir yang masih dapat diputuskan. Senyumnya tenang, matanya letih."
    shiori "Aku bisa terus menyebutnya permainan. Tetapi ada orang yang harus menjalani akibat sesudah kita selesai bicara. Jadi jawab sebagai dirimu sendiri. Apa yang kamu lakukan sekarang?"
    call kk_family_menu("S24", ["Menyerah dan terima kekalahan.", "Membalas dengan langkah terakhir.", "Ulurkan tangan untuk menjadi sekutu."])
    if _return == "A":
        shiori "Kau menyerah dengan tenang. ...Mungkin itu bentuk kejujuran yang paling akhir."
        nar "Kau menerima kekalahan tanpa memintanya menghiburmu. Shiori berhenti menjelaskan langkah berikutnya, seolah tak lagi perlu memastikan kau memahami siapa yang mengendalikan keadaan."
    elif _return == "B":
        shiori "Kau masih punya satu langkah? ...Tunjukkan. Aku ingin tahu apakah kau sepadan sampai akhir."
        nar "Kau membalas dengan keputusan yang bersedia diakui di depan pihak lain. Shiori memeriksa akibatnya sebelum menjawab. Pertarungan belum selesai, tetapi kali ini ia tidak bisa menutupinya sebagai kebohongan yang sama."
    else:
        shiori "Bersekutu? Setelah semua ini? ...Anehnya, itu langkah yang tidak kuperhitungkan. Dan justru karena itu, aku tertarik."
        nar "Ia tidak langsung menerima tanganmu. Ia menanyakan syarat, kebenaran yang masih disimpan, dan siapa yang dirugikan jika kalian hanya mencari musuh baru untuk melupakan urusan lama."
        nar "Kemungkinan kerja sama muncul di antara jawaban itu. Tak ada janji bahwa luka harus dilupakan agar kalian boleh berhenti menambahnya."
    return

init 1 python:
    _hook("S04-A", lambda: kk_adj("respek_shiori",5))
    _hook("S04-B", lambda: kk_adj("respek_shiori",8))
    _hook("S04-C", lambda: (kk_adj("daftar_kebohongan_shiori",1), kk_adj("marah_shiori",5)))
    _hook("S05-A", lambda: (kk_rel("shiori","trust",5), kk_flag("tojo_aktif"), kk_flag("shiori_dilindungi_tojo")))
    _hook("S05-B", lambda: (kk_flag("tojo_aktif"), kk_rel("shiori","trust",-3)))
    _hook("S05-C", lambda: (kk_flag("tojo_aktif"), kk_adj("marah_shiori",8)))
    _hook("S20-A", lambda: (kk_adj("respek_shiori",8), kk_flag("shiori_pesan_dibalas")))
    _hook("S20-B", lambda: (kk_adj("marah_shiori",10), kk_adj("respek_shiori",-8)))
    _hook("S20-C", lambda: kk_rel("shiori","trust",-5))
    _hook("S21-A", lambda: (kk_rel("shiori","trust",6), kk_flag("tojo_dihalangi")))
    _hook("S21-B", lambda: (kk_adj("respek_shiori",6), kk_flag("tojo_bidak")))
    _hook("S21-C", lambda: (kk_adj("marah_shiori",6), kk_flag("pemain_pakai_tojo")))
    _hook("S22-A", lambda: (kk_stage("shiori", max(5, stage.get("shiori",0))), kk_flag("shiori_dilawan")))
    _hook("S22-B", lambda: (kk_adj("daftar_kebohongan_shiori",-2), kk_flag("pemain_mengaku_terdesak")))
    _hook("S22-C", lambda: (kk_stage("shiori", max(5, stage.get("shiori",0))), kk_adj("marah_shiori",10)))
    _hook("S23-A", lambda: (kk_adj("respek_shiori",6), kk_flag("shiori_turnamen_didukung")))
    _hook("S23-B", lambda: kk_rel("shiori","aff",-4))
    _hook("S23-C", lambda: (kk_adj("marah_shiori",8), kk_adj("daftar_kebohongan_shiori",1)))
    _hook("S24-A", lambda: kk_flag("shiori_skakmat_menyerah"))
    _hook("S24-B", lambda: (kk_adj("respek_shiori",10), kk_flag("shiori_skakmat_dibalas")))
    _hook("S24-C", lambda: (kk_rel("shiori","intim",6), kk_flag("shiori_sekutu_akhir")))
