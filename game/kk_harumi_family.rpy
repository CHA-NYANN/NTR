# Alur hangat Harumi: teh awal (H02, H05) dan keluarga Kansai (H10, H-D07, H22).
# Efek mengikuti Alur_Cabang/03; nilai angka adalah setelan prototipe. Tanpa materi rute eksploitasi.
# ┌─ PANDUAN CERITA · H02 · Teh di Bawah Atap
# │ LOKASI  : Kampus Kouseikan · Gedung Sains & Lab
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : hujan; ia menyeduh teh untuk pemain.
# │ INTI    : A puji / B minta tambah / C kritik.
# │ AKHIRAN : Trust.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H02:
    call kk_scene_enter("harumi", "Gedung Sains & Lab · Hujan")
    nar "Harumi memeriksa arah hujan sebelum mengeluarkan termos. Ia menuang sedikit ke tutup, menunggu uapnya berkurang, lalu menyodorkannya kepadamu lebih dahulu."
    harumi "Belum akan berhenti dalam waktu dekat. Itu perkiraan, bukan hasil pengukuran. Tehnya lebih bisa dipercaya."
    call kk_family_menu("H02", ["Puji rasanya dengan jujur.", "Minta ditambah satu tutup lagi.", "Kritik tehnya terlalu pahit."])
    if _return == "A":
        harumi "Kau menyebut bagian yang tepat. Aku memang menakar daunnya lama."
        nar "Ia terlihat senang karena ketelitiannya diketahui tanpa harus diperlihatkan lewat catatan. Ketika kau mengembalikan tutup, ia memegangnya sesaat, menyadari kalian baru saja berbagi sesuatu yang baginya tidak sepenuhnya biasa."
    elif _return == "B":
        harumi "Masih ada. Habiskan sebelum hujannya berhenti."
        nar "Ia menuang lebih banyak, kemudian mengakui sengaja selalu membawa lebih dari satu porsi."
        harumi "Biasanya tidak ada yang bertanya untuk siapa sisanya. Hari ini jawabannya jadi jelas."
    else:
        nar "Harumi mencicipi dan mengatakan kepahitan itu memang bagian dari teh yang dipilih. Ia menerima bahwa kau tidak menyukainya, tetapi menutup termos lebih cepat."
        harumi "Lain kali aku tanya seleramu dulu. Aku terlalu cepat menganggap yang kusukai pasti menolong orang lain juga."
    return

# ┌─ PANDUAN CERITA · H05 · Reuni di Rumah Teh
# │ LOKASI  : Kampus Kouseikan · Kafe Komorebi
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : kelompok belajar.
# │ INTI    : A bantu penyajian / B pembicaraan masa depan / C membuka rahasia.
# │ AKHIRAN : gerbang pengecekan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H05:
    call kk_scene_enter("harumi", "Kafe Komorebi · Kelompok belajar")
    nar "Kelompok belajar di Komorebi selesai dengan kebiasaan lama: semua membawa jawaban pulang, Harumi masih memastikan tidak ada buku tertinggal. Ia hampir memanggil seseorang kembali, lalu hanya menanyakan apakah kau mau tinggal."
    harumi "Aku belum ingin percakapannya selesai. Itu alasan yang lebih tepat daripada masih menata cangkir. Tapi cangkirnya juga memang perlu ditata."
    call kk_family_menu("H05", ["Bantu ia menyajikan teh untuk yang tersisa.", "Tanyakan ke mana ia ingin melangkah setelah lulus.", "Pancing ia menceritakan hal yang jarang ia buka."])
    if _return == "A":
        harumi "Berdua lebih cepat. Terima kasih."
        nar "Kalian membagi pekerjaan, kemudian justru duduk lebih lama setelah selesai. Harumi tampak geli pada kenyataan bahwa pekerjaan yang dijadikan alasan sudah habis tetapi kau tetap berada di sana."
    elif _return == "B":
        harumi "Orang tuaku mengukur segalanya. Aku belum tahu caraku sendiri. Tapi aku ingin tahu."
        nar "Ia bercerita tentang menjadi profesor, bukan hanya sebagai puncak yang diharapkan keluarga tetapi keinginan untuk punya ruang bertanya dan membimbing."
        harumi "Aku ingin tahu apakah masih akan memilih itu kalau suatu hari mereka tidak bangga. Sejauh ini jawabannya iya. Itu membuatku lega."
    else:
        harumi "...Jarang ada yang bertanya soal itu. Mungkin lain kali."
        nar "Kau menyentuh cerita yang belum siap ia buka. Harumi memberikan batas singkat, lalu menanyakan hal lain agar penolakan kecil tersebut tidak harus mengakhiri kebersamaan."
        nar "Tetap duduk sesudahnya memberinya pengalaman bahwa belum mau bercerita tidak membuat seseorang otomatis pergi."
    return

# ┌─ PANDUAN CERITA · H10 · Pulang ke Kansai
# │ LOKASI  : Stasiun & Pasar · Stasiun Kouseikan-mae
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : orang tua Kujo dan Mizuhara.
# │ INTI    : A ikut / B tidak / C bercerita tentang Harumi.
# │ AKHIRAN : konteks keluarga.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H10:
    call kk_scene_enter("harumi", "Stasiun Kouseikan-mae")
    nar "Tiket Kansai terselip di buku Harumi. Ia telah merencanakan perjalanan, pertemuan keluarga, dan pembicaraan tentang studinya, tetapi menunda membalas pertanyaan ibunya tentang apakah ingin dijemput."
    harumi "Aku pulang akhir pekan ini. Bertemu orang tua. Mungkin akan lebih banyak bicara tentang riset daripada diriku sendiri. Aku belum tahu apakah itu karena mereka tidak bertanya, atau aku yang selalu lebih dahulu membawa nilai."
    call kk_family_menu("H10", ["Tawarkan ikut menemaninya pulang.", "Katakan sebaiknya ia pergi sendiri dulu.", "Ceritakan hal baik tentang Harumi yang bisa ia bawa pulang."])
    if _return == "A":
        harumi "Kau yakin? Orang tuaku akan menanyaimu seperti menguji hipotesis."
        nar "Kau mengatakan bersedia hadir tanpa menjawab atas namanya. Harumi akhirnya membalas pesan ibunya bahwa akan ada teman, lalu menyebut namamu dengan jelas."
        harumi "Aku ingin mereka mengenal bagian hidupku yang tidak bisa dijelaskan lewat transkrip. Itu termasuk kamu."
    elif _return == "B":
        harumi "Mungkin kau benar. Ini urusanku dengan mereka."
        nar "Ia menyimpan tiket dan mengatakan akan mencoba membicarakan sesuatu yang tidak berkaitan dengan prestasi. Ada kecewa kecil karena pergi sendiri, tetapi juga ruang untuk menentukan bagaimana ingin dikenal keluarganya."
    else:
        harumi "Kalau kau yang bilang begitu, barangkali aku bisa mengulanginya pada mereka."
        nar "Kau menyebut kesabarannya, humor kering yang mulai kaukenali, dan kepedulian kecil yang jarang ia hitung sebagai kelebihan. Harumi menolak satu pujian, lalu membiarkan yang lain tetap ada."
        harumi "Aku akan mencoba mengatakan itu tanpa menambahkan bahwa orang lain pasti lebih baik."
    return

# ┌─ PANDUAN CERITA · H22 · Natal Pulang
# │ LOKASI  : Stasiun & Pasar · Stasiun Kouseikan-mae
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : ia pulang ke Kansai.
# │ INTI    : A mengantar / B menelepon orang tua / C biarkan.
# │ AKHIRAN : keluarga.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H22:
    call kk_scene_enter("harumi", "Stasiun Kouseikan-mae · Natal")
    if kk_has("harumi_kansai_ikut"):
        harumi "Tahun lalu kau ikut sampai depan rumah. Kali ini aku pulang untuk Natal. Mereka menanyakanmu."
    else:
        harumi "Aku pulang untuk Natal. Entah kenapa, tahun ini rasanya bukan sekadar kewajiban."
    call kk_family_menu("H22", ["Antar ia sampai peron dan tunggu keretanya berangkat.", "Tawarkan menelepon orang tuanya untuk menitip salam.", "Ucapkan selamat jalan lalu biarkan ia pergi."])
    if _return == "A":
        harumi "Sampai keretanya hilang di tikungan, ya. Baik."
        nar "Kau menunggu di peron. Harumi memilih tempat dekat jendela, menaruh tas, lalu melambai sebelum kereta bergerak. Ia tidak perlu membuat perpisahan itu berguna agar boleh terasa berat."
    elif _return == "B":
        harumi "Mereka akan kaget. Tapi kurasa mereka akan senang."
        nar "Dengan izinnya kau menyampaikan salam dan waktu kedatangan. Ibunya bertanya apakah Harumi sudah makan sebelum menanyakan riset. Ia mendengar dari dekatmu, tersenyum pada urutan yang kali ini berbeda."
    else:
        nar "Ia melambai sekali sebelum naik. Tidak ada yang menemaninya sampai jendela, tetapi ia tetap mengirim kabar ketika sudah duduk."
        harumi "Aku akan sampai sore. Aku ingin pulang, ternyata. Menulis itu membuatku lebih yakin daripada menghitung alasan kenapa harus."
    return

# ┌─ PANDUAN CERITA · H-D07 · Surat dari Kansai
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kujo Harumi
# │ AWALAN  : setelah H10-A
# │ INTI    : A Bantu Harumi membalas / B bacakan / C abaikan
# │ AKHIRAN : orang_tua_kujo +
# └─ tulis / perbaiki dialog di bawah ──
label kk_kansai_letter:
    nar "Surat dari Kansai memuat kabar rumah, jadwal ayahnya, dan pertanyaan penelitian. Di akhir ada baris tentang teh yang masih tersisa sejak kunjungan kalian. Harumi membacanya berulang kali."
    harumi "Aku tahu beliau ingin kabar. Aku hanya tidak tahu apakah boleh menjawab bahwa aku lelah, bukan sedang mencapai sesuatu."
    call kk_family_menu("H-D07", ["Bantu ia menyusun balasan dengan kata-katanya sendiri.", "Bacakan suratnya keras-keras agar ia mendengarnya utuh.", "Sarankan ia mengabaikan surat itu saja."])
    if _return == "A":
        harumi "Jadi aku boleh menulis apa yang kurasakan, bukan hanya nilai dan jadwal."
        nar "Ia menulis satu paragraf yang tidak bisa dipindahkan ke laporan akademik. Sesudahnya ia membacanya kembali, tidak langsung menghapus bagian tentang ingin ditelepon tanpa membahas riset."
    elif _return == "B":
        harumi "Dibacakan begini, ada satu kalimat yang hampir terdengar seperti rindu."
        nar "Kau membaca tanpa menambahkan maksud yang tak tertulis. Harumi menunjuk baris tentang teh, lalu mengakui mungkin itu cara ibunya mengatakan masih mengingat kehadiran mereka di rumah."
        harumi "Aku bisa bertanya apakah memang itu maksudnya. Aku tidak perlu menentukan sendirian dari selembar surat."
    else:
        nar "Kau menyarankan mengabaikan. Harumi melipat surat dan menyimpannya kembali di buku. Balasan yang tidak segera dibuat akan semakin sulit dimulai karena ia merasa harus sekaligus meminta maaf atas keterlambatan."
    return

init 1 python:
    _hook("H02-A", lambda: kk_rel("harumi","trust",4))
    _hook("H02-B", lambda: (kk_rel("harumi","intim",3), kk_rel("harumi","trust",2)))
    _hook("H02-C", lambda: kk_rel("harumi","trust",-3))
    _hook("H05-A", lambda: kk_rel("harumi","trust",4))
    _hook("H05-B", lambda: (kk_rel("harumi","trust",3), kk_adj("orang_tua_kujo",5)))
    _hook("H05-C", lambda: (kk_rel("harumi","intim",4), kk_rel("harumi","trust",2)))
    _hook("H10-A", lambda: (kk_adj("orang_tua_kujo",15), kk_rel("harumi","trust",5), kk_flag("harumi_kansai_ikut")))
    _hook("H10-B", lambda: kk_rel("harumi","trust",2))
    _hook("H10-C", lambda: (kk_rel("harumi","trust",4), kk_adj("orang_tua_kujo",5)))
    _hook("H22-A", lambda: (kk_adj("orang_tua_kujo",10), kk_rel("harumi","trust",4)))
    _hook("H22-B", lambda: (kk_adj("orang_tua_kujo",10), kk_rel("harumi","trust",3)))
    _hook("H-D07-A", lambda: (kk_adj("orang_tua_kujo",10), kk_rel("harumi","trust",3), kk_flag("kujo_surat_dibalas")))
    _hook("H-D07-B", lambda: kk_adj("orang_tua_kujo",5))
    _hook("H-D07-C", lambda: kk_adj("orang_tua_kujo",-5))
