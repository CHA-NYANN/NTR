# Milestone utama Miyuki tahun 2-3 (Mi14-Mi23, Mi26): arc "Rute Masokis" —
# Miyuki menormalisasi menyalahkan diri dan penyerahan emosional di bawah tekanan
# supervisor/karier/keluarga. DITULIS sebagai KONSEKUENSI dan KARAKTER: pilihan
# "manfaatkan" dicatat singkat tanpa metode; opsi pemulihan (Sena/Sato Kyoko)
# selalu tersedia. Bukan Force. Efek menggerakkan stage[miyuki], luka_miyuki_diri,
# omiai_takeru, dan bendera pemulihan. Nilai prototipe; mengikuti Event_Miyuki.

init 1 python:
    def kk_miyuki_stage(n):
        kk_stage("miyuki", max(n, stage.get("miyuki", 0)))

# ┌─ PANDUAN CERITA · Mi14 · Hujan di Bangsal
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : ia dimarahi supervisor.
# │ INTI    : A hibur / B bela / C kritik Miyuki.
# │ AKHIRAN : stage 2 (dimarahi = diperhatikan).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi14:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana · Hujan di bangsal")
    nar "Hujan memukul kaca koridor ketika Miyuki keluar dari bangsal. Ia masih membawa lembar catatan yang tadi ditepuk supervisor dengan jari, cukup keras sampai pasien ikut berhenti bicara."
    miyuki "Ada yang harus kubetulkan. Beliau benar soal itu."
    nar "Ia menerangkan kesalahan pekerjaannya dengan jelas, lalu buru-buru menerangkan mengapa dipermalukan di depan orang lain mungkin juga wajar."
    miyuki "Setidaknya beliau memperhatikan. Lebih buruk kalau aku sudah dianggap nggak layak ditegur, kan?"
    call kk_family_menu("Mi14", ["Hibur ia; ia tidak pantas diperlakukan begitu.", "Bela ia langsung ke supervisor.", "Ikut mengkritik kinerjanya."])
    if _return == "A":
        nar "Kau memisahkan hal yang perlu diperbaiki dari cara orang memperlakukannya. Miyuki menatap lembar catatan, seolah dua hal itu baru pertama kali boleh berbeda."
        miyuki "Aku bisa salah dan tetap nggak pantas dipermalukan?"
        nar "Kau mengangguk. Ia duduk di bangku, membiarkan pertanyaan tersebut tinggal lebih lama daripada alasan untuk membantahnya."
    elif _return == "B":
        nar "Kau menyampaikan keberatan langsung kepada supervisor tentang teguran di depan pasien. Jawabannya singkat dan kaku; ia meminta urusan pendidikan tidak dibahas di koridor."
        miyuki "Aku takut besok jadi lebih sulit. Tapi aku juga... senang ada yang merasa itu nggak semestinya."
        nar "Ia meminta kau memberinya ruang untuk menangani pekerjaan yang perlu dikoreksi. Kali ini permintaannya sendiri kaudengarkan."
    else:
        nar "Kau ikut mengkritik kinerjanya sebelum ia sempat menenangkan diri. Miyuki mengangguk pada setiap kalimat, bahkan ketika kau membahas hal yang tidak kaulihat sendiri."
        miyuki "Iya. Aku akan lebih teliti. Jangan kecewa dulu."
        nar "Ia terdengar lega karena tahu apa yang harus dilakukan untuk mempertahankan perhatianmu. Luka dari bangsal mendapatkan suara kedua yang bisa ia bawa pulang."
    return

# ┌─ PANDUAN CERITA · Mi15 · Minta Maaf Berlebihan
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : ia meminta maaf untuk hal sepele.
# │ INTI    : A tegur halus / B biarkan / C manfaatkan.
# │ AKHIRAN : stage 3 (normalisasi).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi15:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana · Permintaan maaf")
    nar "Mesin minuman menelan uang tanpa mengeluarkan apa pun. Sebelum kau selesai mengeluh, Miyuki sudah meraih dompetnya."
    miyuki "Maaf, harusnya tadi kuajak ke mesin sebelah. Aku nggak tahu yang ini rusak. Maaf, ya."
    nar "Ia menyebut tiga hal yang seharusnya dilakukan, tak satu pun masuk akal untuk menjadi tanggung jawabnya. Kau melihat jemarinya gemetar saat mencari uang pengganti."
    call kk_family_menu("Mi15", ["Tegur halus bahwa ia tak perlu minta maaf.", "Biarkan saja.", "Manfaatkan kebiasaannya itu."])
    if _return == "A":
        nar "Kau memintanya menyimpan dompet dan menyebut bahwa mesin rusak bukan kesalahannya. Miyuki terdiam di tengah permintaan maaf berikutnya."
        miyuki "Aku bahkan belum mikir. Kata itu langsung keluar."
        nar "Ia mencoba mengatakan kesal kepada mesin, lalu tertawa canggung pada betapa asingnya hal itu terasa."
        miyuki "Aku boleh ikut kesal tanpa harus membereskan perasaan semua orang dulu, ya."
    elif _return == "B":
        nar "Kau membiarkan ia membayar minuman pengganti. Miyuki menyerahkannya dengan senyum yang baru muncul setelah kau menerima."
        miyuki "Nah. Sekarang sudah beres."
        nar "Baginya persoalan selesai karena kau tidak lagi tampak kecewa. Kebiasaan yang barusan mendapat pembenaran akan datang lebih cepat pada kesempatan berikutnya."
    else:
        nar "Kau membiarkan rasa bersalahnya menutup urusan lain yang sebenarnya bukan tanggung jawabnya. Miyuki menyanggupi sebelum sempat memeriksa jadwalnya sendiri."
        miyuki "Bisa. Nanti aku atur. Jangan khawatir."
        nar "Ia mencatat permintaanmu di antara waktu praktik dan belajarnya. Satu baris baru masuk tanpa ada baris lama yang dikeluarkan. Kau mendapat bantuan; ia mendapat alasan tambahan untuk takut gagal."
    return

# ┌─ PANDUAN CERITA · Mi16 · Kesalahan di Bangsal
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : kesalahan klinis kecil; teguran keras.
# │ INTI    : A hibur / B tegas / C dingin / D bawa ke Sena/Sato.
# │ AKHIRAN : gerbang Rute Masokis (stage 4); D membuka jalur pemulihan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi16:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana · Kesalahan di bangsal")
    nar "Kesalahan pencatatan itu sudah dikoreksi sebelum berdampak pada pasien. Miyuki masih membahasnya sejam kemudian, mengulang setiap teguran seperti daftar bukti tentang dirinya."
    miyuki "Kalau aku pantas berada di sini, hal seperti itu harusnya nggak terjadi."
    nar "Saat kau mengingatkan bahwa ia telah memperbaikinya, ia menggeleng. Yang sedang ia usahakan rupanya bukan memahami kejadian, melainkan menemukan hukuman yang cukup besar untuk mengakhirinya."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Hibur dan yakinkan ia cukup.", "Tegas: ia harus berhenti merendah.", "Bersikap dingin padanya.", "Bawa ia ke Sena atau Sato Kyoko."])]
    call screen kk_choice_panel(_rows, "Sesudah teguran")
    $ kk_record_choice("Mi16", _return)
    if _return == "A":
        nar "Kau mengatakan bahwa ia tidak perlu merangkum dirinya dari satu kesalahan. Miyuki mencoba mendengar, tetapi wajahnya tetap tegang."
        miyuki "Aku ingin percaya. Setiap mendengar cukup, aku malah mencari bagian yang belum kamu lihat."
        nar "Ia tidak langsung tenang. Namun ia berhenti menambahkan tuduhan baru sambil duduk di sampingmu."
    elif _return == "B":
        nar "Kau menyuruhnya berhenti merendahkan diri. Maksudmu tegas; di telinganya kalimat itu masuk sebagai hal lain yang baru saja gagal ia lakukan dengan benar."
        miyuki "Aku mencoba. Maaf kalau melelahkan didengar."
        nar "Ia mengatur wajahnya kembali. Pembicaraan berhenti lebih cepat daripada rasa bersalahnya, dan ia berterima kasih karena mengira itulah yang kauharapkan."
    elif _return == "C":
        nar "Kau menarik perhatianmu ketika ia sedang mencarinya. Miyuki justru mulai menawarkan lebih banyak penjelasan, lebih banyak bantuan, apa saja yang mungkin membuatmu kembali melihat."
        miyuki "Bilang apa yang harus kubetulkan. Kalau kamu diam, aku nggak tahu kapan boleh berhenti merasa salah."
        nar "Kedekatan di antara kalian mengencang dengan cara yang buruk: ketenangannya mulai tergantung pada kapan kau bersedia mengakhiri hukuman yang tidak pernah jelas."
    else:
        nar "Kau menawarkan bertemu Sena atau Sato. Miyuki hampir menolak, lalu memandang catatannya sendiri yang penuh pengulangan."
        miyuki "Aku capek mendengar suara ini di kepalaku. Aku mau mencoba bicara."
        "Sena" "Kita cari waktu yang bisa. Kamu nggak perlu menjelaskan semuanya sekaligus."
        nar "Miyuki menutup buku. Untuk sementara, kegagalannya tidak lagi menjadi satu-satunya hal yang dibicarakan tentang dirinya."
    return

# ┌─ PANDUAN CERITA · Mi17 · Pingsan di Pameran
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : kelelahan ekstrem.
# │ INTI    : A bawa ke UGD / B diam / C manfaatkan.
# │ AKHIRAN : Sena menegur pemain.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi17:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana · Pingsan")
    nar "Miyuki masih meminta tamu pameran kesehatan menunggu sebentar ketika lututnya kehilangan tenaga. Map terlepas dari tangannya; kertas meluncur lebih jauh daripada tubuh yang jatuh di belakang meja."
    nar "Suara ruangan terasa mendadak jauh. Kau berada paling dekat ketika namanya dipanggil tanpa jawaban."
    call kk_family_menu("Mi17", ["Bawa ia ke UGD segera.", "Diam dan tunggu ia sadar sendiri.", "Manfaatkan keadaannya."])
    if _return == "A":
        nar "Kau memanggil petugas dan memastikan ia mendapat pertolongan di UGD. Sena tiba ketika Miyuki sudah diperiksa."
        "Sena" "Aku akan bantu urusan jadwal. Tolong jangan biarkan dia mengira harus kembali kerja setelah bilang sudah enakan."
        miyuki "Pamerannya..."
        "Sena" "Ada orang lain di sana. Sekarang kamu di sini dulu."
        nar "Miyuki memejamkan mata. Kalimat bahwa orang lain dapat menggantikannya tampak menakutkan dan menenangkan sekaligus."
    elif _return == "B":
        nar "Kau menunggu sampai ia siuman. Orang lain akhirnya memanggil bantuan, sementara Miyuki mencoba duduk sebelum benar-benar memahami apa yang terjadi."
        miyuki "Aku merepotkan semua orang lagi. Maaf."
        nar "Ia meminta maaf kepada orang yang memungut kertas, petugas yang datang, dan kepadamu. Tidak ada yang menghentikan urutannya cukup cepat untuk membuat ia merasa jatuh sakit boleh berarti hal lain selain gagal."
    else:
        nar "Kau memakai kelemahannya untuk menuntut sesuatu saat ia bahkan belum pulih dari kebingungan. Sena mendengar dan segera memutus percakapan."
        "Sena" "Mundur. Dia perlu pertolongan, bukan permintaanmu."
        nar "Miyuki mencoba menjelaskan bahwa ia tidak keberatan. Suaranya terlalu lemah untuk menyamarkan ketakutan membuatmu kecewa. Sena tetap memanggil petugas dan tidak lagi membiarkanmu berada sendirian dengannya."
    return

# ┌─ PANDUAN CERITA · Mi19 · Valentine Dingin
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : ia memberi coklat tanpa senyum.
# │ INTI    : A terima / B kembalikan / C tanyakan.
# │ AKHIRAN : pola menguat.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi19:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana · Valentine")
    nar "Kotak coklat itu dibungkus sempurna. Miyuki menyerahkannya di koridor rumah sakit, menyebut kapan sebaiknya dimakan dan bagaimana menyimpannya, lalu berdiri menunggu penilaian."
    miyuki "Aku membuatnya tadi malam. Kalau kurang manis, bilang. Aku masih punya bahan."
    nar "Tidak ada nada jahil atau kebanggaan kecil yang biasa mengikuti hasil dapurnya. Ia terdengar seperti sedang menyerahkan tugas yang harus diperiksa."
    call kk_family_menu("Mi19", ["Terima apa adanya.", "Kembalikan dan minta ia memberinya dengan tulus.", "Tanyakan kenapa ia tak tersenyum."])
    if _return == "A":
        nar "Kau menerima kotak itu dan mengucapkan terima kasih. Miyuki mengangguk, lega karena tidak perlu membuatnya ulang."
        miyuki "Sudah cukup? Baik. Aku senang kalau kamu nggak kecewa."
        nar "Ia baru menyadari pilihan katanya setelah mengucapkannya. Namun ketika dipanggil kembali ke dalam, ia segera pergi, meninggalkan rasa getir yang tidak berasal dari coklat."
    elif _return == "B":
        nar "Kau mengembalikan kotaknya dan mengatakan tidak ingin ia memberimu sesuatu sebagai pembayaran agar tetap disukai. Miyuki menatap pita yang sudah begitu hati-hati dibuatnya."
        miyuki "Aku tadi mengira kamu minta kubuat lebih bagus. Ternyata kamu bertanya aku ingin memberi atau nggak."
        nar "Ia menarik kotak itu ke dada."
        miyuki "Boleh kusimpan dulu? Aku ingin tahu jawabannya sebelum memberimu lagi."
    else:
        nar "Kau menanyakan keadaannya, bukan meminta ia tersenyum untukmu. Miyuki sempat mengatakan baik-baik saja, lalu berhenti di tengah kalimat."
        miyuki "Aku bangun tadi dan yang kupikirkan cuma jangan lupa. Bukan siapa yang ingin kubuat senang."
        nar "Kotak itu terasa berat di tanganmu. Ia meminta duduk sebentar sebelum kembali ke bangsal, dan kali ini membiarkanmu melihat bahwa ia belum punya jawaban."
    return

# ┌─ PANDUAN CERITA · Mi20 · Audit Pribadi
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : ia mengevaluasi hidupnya.
# │ INTI    : A dukung / B abaikan / C bawa ke Sato.
# │ AKHIRAN : titik pemulihan terakhir sebelum Tahun 3.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi20:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana · Audit pribadi")
    nar "Miyuki membuat dua daftar. Yang pertama berjudul harus. Yang kedua hanya punya satu baris, ditulis lalu dicoret hingga sulit dibaca."
    miyuki "Aku mencoba menulis yang kuinginkan. Setiap kali muncul sesuatu, aku langsung teringat siapa yang akan kecewa."
    nar "Ia menunjuk pediatri sebagai satu hal yang masih terasa miliknya, kemudian menutup bagian keluarga dengan telapak tangan."
    miyuki "Kalau baru sekarang bertanya tentang hidupku sendiri, apa sudah terlalu terlambat?"
    call kk_family_menu("Mi20", ["Dukung ia mengambil kembali pilihannya.", "Abaikan; biarkan ia memutuskan sendiri.", "Bawa ia ke Sato Kyoko untuk membicarakannya."])
    if _return == "A":
        nar "Kau mendukungnya tanpa mengisi daftar kosong itu dengan keinginanmu. Miyuki menunggu saran, lalu menyadari kau sedang membiarkan ia sendiri yang menulis."
        miyuki "Aku ingin satu malam tanpa menjawab telepon keluarga. Aku ingin tidur sebelum merasa pantas tidur."
        nar "Dua kalimat masuk ke daftar. Tidak mengubah seluruh hidupnya, tetapi keduanya tidak dicoret."
    elif _return == "B":
        nar "Kau mengatakan keputusan itu miliknya, lalu membiarkan pembicaraan berhenti tanpa menanyakan bantuan apa yang diperlukan. Miyuki mengangguk seperti menerima pekerjaan tambahan."
        miyuki "Iya. Aku harus bisa memutuskan sendiri."
        nar "Ia menutup daftar kedua dan kembali memeriksa jadwal. Ketidakmampuannya memilih kini terasa seperti kekurangan baru yang juga harus ia tanggung sendirian."
    else:
        nar "Kau menawarkan membicarakannya dengan Sato. Miyuki membawa kedua daftar itu ke pertemuan, bahkan bagian yang menurutnya memalukan."
        "Sato Kyoko" "Kita bisa mulai dari apa yang terjadi saat kamu hendak mencoret sebuah keinginan. Tidak perlu memutuskan seluruh masa depan hari ini."
        nar "Miyuki menarik tangannya dari daftar yang ditutupi. Untuk sekali ini bagian yang sulit tidak harus dirapikan sebelum boleh dilihat seseorang."
    return

# ┌─ PANDUAN CERITA · Mi22 · Pola Menetap
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : stage 5: dinamika dominasi–penyerahan emosional (tersirat).
# │ INTI    : A lanjutkan / B hentikan / C bawa ke Sena/Sato.
# │ AKHIRAN : A bisa membuat pola permanen setelah 1 semester; C membuka pemulihan sebagian.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi22:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana · Pola yang menetap")
    nar "Miyuki meminta izin sebelum memilih minumannya sendiri. Ia mengatakannya begitu biasa hingga penjaga kantin menjawab lebih dahulu, mengira pertanyaan itu untuknya."
    miyuki "Aku cuma ingin memastikan kamu nggak keberatan. Kalau kamu memilihkan, aku lebih tenang."
    nar "Pola itu kini hidup di dalam hal-hal kecil. Ia menunggu arahan, kau terbiasa memberi, dan kata nyaman mulai dipakai setiap kali seseorang bertanya apakah ia masih punya keinginan sendiri."
    call kk_family_menu("Mi22", ["Lanjutkan pola ini.", "Hentikan sebelum menetap.", "Bawa ia ke Sena atau Sato Kyoko."])
    if _return == "A":
        nar "Kau memilihkan dan menerima kelegaan di wajahnya sebagai pembenaran. Miyuki menyimpan pilihan yang berbeda sebelum sempat mengucapkannya."
        miyuki "Begini lebih mudah. Aku nggak perlu takut salah."
        nar "Semester itu berlalu dengan semakin sedikit perbedaan yang terlihat. Ia menjadi sangat pandai memperkirakan kehendakmu; orang lain menyebutnya pengertian. Dirinya sendiri makin sulit ditemukan di antara tebakan-tebakan tersebut."
    elif _return == "B":
        nar "Kau menolak meneruskan kebiasaan itu dan mengatakan ia tidak perlu membuat pilihan yang menyenangkanmu. Miyuki justru tampak ketakutan."
        miyuki "Kalau aku nggak tahu apa yang kumau hari ini, kamu tetap mau duduk denganku?"
        nar "Kau tetap di tempat. Ia memilih minuman setelah cukup lama, lalu mengubah pesanannya satu kali tanpa meminta maaf. Gerakan kecil itu belum pemulihan penuh, tetapi pola yang lama akhirnya bertemu gangguan."
    else:
        nar "Kau mengusulkan bantuan di luar hubungan kalian. Sena mendengarkan sebelum mengatakan bahwa keduanya memerlukan jarak untuk melihat kebiasaan yang telah terasa terlalu biasa."
        "Sena" "Aku bisa menemani Miyuki menghubungi Sato. Kamu perlu memberi ruang, termasuk saat itu membuatmu nggak nyaman."
        nar "Miyuki menanyakan siapa yang akan menentukan pertemuan. Sena menjawab bahwa ia sendiri boleh ikut menentukannya. Pertanyaan berikutnya datang lebih lambat, tetapi mulai terdengar seperti keinginan."
    return

# ┌─ PANDUAN CERITA · Mi23 · Yukata Tanpa Senyum
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : ia hadir tanpa ekspresi.
# │ INTI    : A hibur / B manfaatkan / C tinggalkan.
# │ AKHIRAN : Sena memutus hubungan jika pemain memanfaatkan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi23:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana · Yukata tanpa senyum")
    nar "Sena menemani Miyuki keluar setelah jadwal terakhir agar ia sempat pergi ke festival. Yukatanya indah, tetapi ia menatap lampion seperti orang yang sedang mencoba mengingat alasan datang."
    miyuki "Aku sudah berganti pakaian. Harusnya habis ini rasanya berbeda, ya."
    nar "Ia menyadari wajahmu, lalu cepat-cepat meminta maaf karena tidak tampak senang. Bahkan malam libur hampir berubah menjadi ujian lain yang harus ia luluskan."
    call kk_family_menu("Mi23", ["Hibur dan temani ia malam itu.", "Manfaatkan keadaannya.", "Tinggalkan ia sendiri."])
    if _return == "A":
        nar "Kau mengatakan ia tidak harus menikmati seluruh festival agar boleh berada di sana. Kalian memilih tempat duduk yang jauh dari pengeras suara."
        miyuki "Aku boleh bilang mau pulang nanti? Meski baru sebentar?"
        nar "Kau menyetujuinya. Justru setelah mendapat jalan untuk pergi, ia sanggup memperhatikan warna lampion dan mulai bercerita tentang yukata yang dipinjamkan Sena."
    elif _return == "B":
        nar "Kau memperlakukan kepatuhannya sebagai kesempatan menekan, membiarkan ia membayar suasana hatimu dengan tenaganya yang hampir habis. Sena kembali sebelum percakapan selesai."
        "Sena" "Miyuki, ikut aku dulu. Kamu nggak berutang malam yang menyenangkan kepada siapa pun."
        nar "Sesudah mendengar apa yang terjadi, Sena menutup jalanmu untuk mendekat melalui dirinya. Senyum sopan yang selama ini ia berikan kepadamu tidak muncul lagi."
    else:
        nar "Kau pergi setelah mengatakan ada urusan. Miyuki mengangguk dan melambaikan tangan, berusaha membuat perpisahan itu semudah mungkin untukmu."
        nar "Ia tetap duduk dengan yukata rapi, memandang orang lewat. Ketika Sena menemuinya lagi, ia berkata belum lama menunggu, padahal minuman di tangannya sudah hangat."
        miyuki "Aku mungkin memang belum cocok pergi bersenang-senang."
    return

# ┌─ PANDUAN CERITA · Mi26 · Ujian Akhir dan Sena
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : Sena berdiri di sisi pemain atau melawan.
# │ INTI    : A minta bantuan Sena / B hindari / C konfrontasi.
# │ AKHIRAN : aliansi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi26:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana · Ujian akhir")
    nar "Sena membawa salinan jadwal akhir dan daftar barang yang sering dilupakan Miyuki ketika gugup. Ia berhenti berbicara begitu melihatmu di koridor."
    "Sena" "Aku mau memastikan dia punya waktu makan dan tidur. Kalau kamu datang untuk menambah sesuatu yang harus ia tanggung, sekarang bukan waktunya."
    nar "Miyuki berada beberapa langkah di belakangnya, cukup dekat untuk mendengar. Ia tidak boleh lagi dijadikan alasan oleh dua orang yang saling berebut hak paling memahami."
    call kk_family_menu("Mi26", ["Minta bantuan Sena.", "Hindari Sena.", "Konfrontasi Sena."])
    if _return == "A":
        nar "Kau meminta bantuan dengan tugas yang jelas, bukan meminta Sena menjamin bahwa kehadiranmu baik untuk Miyuki. Ia memeriksa apakah Miyuki menginginkan rencana itu."
        miyuki "Aku mau. Asal kalau aku bilang cukup, kita berhenti."
        "Sena" "Baik. Kita bantu sesuai itu. Demi dia."
        nar "Kerja sama kalian dimulai dari persetujuan Miyuki, tanpa perlu menghapus apa yang Sena ingat tentangmu."
    elif _return == "B":
        nar "Kau memilih menghindari Sena. Ia tidak mengejar, kembali menyerahkan jadwal kepada Miyuki dan membicarakan hal-hal yang tetap perlu diselesaikan."
        nar "Kau kehilangan kesempatan mengetahui bagian yang tak pernah Miyuki ceritakan kepadamu. Persiapan itu berjalan juga, dengan pintu yang kini harus diketuk melalui Miyuki sendiri."
    else:
        nar "Kau mempertanyakan hak Sena menghalangi. Ia mendengarkan tanpa mundur, lalu menoleh ketika Miyuki hendak meminta maaf untuk kalian berdua."
        "Sena" "Bukan salahmu. Jangan ambil ini juga."
        nar "Barulah ia menjawabmu."
        "Sena" "Aku akan berdiri di pihak yang membuat dia lebih aman, termasuk kalau itu membuatmu marah. Kamu baru saja menunjukkan kenapa aku perlu tegas."
    return

init 1 python:
    _hook("Mi14-A", lambda: (kk_rel("miyuki","trust",5), kk_miyuki_stage(2)))
    _hook("Mi14-B", lambda: (kk_rel("miyuki","aff",4), kk_miyuki_stage(2)))
    _hook("Mi14-C", lambda: (kk_miyuki_hurt_self(8), kk_miyuki_stage(2)))
    _hook("Mi15-A", lambda: kk_rel("miyuki","trust",4))
    _hook("Mi15-B", lambda: kk_miyuki_stage(3))
    _hook("Mi15-C", lambda: (kk_miyuki_hurt_self(10), kk_miyuki_stage(3), kk_flag("miyuki_rasa_salah_dimanfaatkan")))
    _hook("Mi16-A", lambda: kk_rel("miyuki","trust",4))
    _hook("Mi16-B", lambda: kk_rel("miyuki","aff",-3))
    _hook("Mi16-C", lambda: (kk_miyuki_hurt_self(12), kk_miyuki_stage(4), kk_flag("rute_masokis_miyuki")))
    _hook("Mi16-D", lambda: (kk_miyuki_hurt_self(-10), kk_flag("miyuki_sato_dikenal")))
    _hook("Mi17-A", lambda: (kk_rel("miyuki","trust",5), kk_adj("kelelahan_miyuki",-20)))
    _hook("Mi17-B", lambda: kk_miyuki_hurt_self(6))
    _hook("Mi17-C", lambda: (kk_miyuki_hurt_self(10), kk_flag("sena_memutus")))
    _hook("Mi19-A", lambda: kk_flag("miyuki_pola_valentine"))
    _hook("Mi19-B", lambda: kk_rel("miyuki","aff",3))
    _hook("Mi19-C", lambda: kk_rel("miyuki","trust",4))
    _hook("Mi20-A", lambda: (kk_rel("miyuki","trust",6), kk_flag("miyuki_ambil_pilihan")))
    _hook("Mi20-C", lambda: (kk_miyuki_hurt_self(-8), kk_flag("miyuki_sato_dikenal")))
    _hook("Mi22-A", lambda: (kk_miyuki_stage(5), kk_flag("pola_masokis_permanen")))
    _hook("Mi22-B", lambda: (kk_miyuki_hurt_self(-12), kk_flag("pola_dihentikan")))
    _hook("Mi22-C", lambda: (kk_miyuki_hurt_self(-10), kk_flag("miyuki_sato_dikenal")))
    _hook("Mi23-A", lambda: kk_rel("miyuki","intim",5))
    _hook("Mi23-B", lambda: (kk_miyuki_hurt_self(12), kk_flag("sena_memutus")))
    _hook("Mi23-C", lambda: kk_rel("miyuki","trust",-5))
    _hook("Mi26-A", lambda: kk_flag("sena_sekutu"))
    _hook("Mi26-B", lambda: kk_rel("miyuki","trust",-2))
    _hook("Mi26-C", lambda: kk_flag("sena_lawan"))
