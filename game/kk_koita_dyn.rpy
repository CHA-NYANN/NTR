# Event dinamis Koita (K-D01, K-D05, K-D08, K-D09, K-D13, K-D16, K-D18, K-D19,
# K-D20, K-D21). Memperdalam thread kesadaran -> keruntuhan -> pemulihan yang
# sudah dimulai di kk_koita_y1/y2/y3. Cabang gelap ditulis sebagai KONSEKUENSI
# dan KARAKTER saja: tanpa metode, tanpa cara memfitnah. Gerbang rute eksplisit
# (BL/Koita-Success) dan jalur yang mengandaikan Force on-screen tidak dibuka.
# Nilai adalah setelan prototipe; semantik mengikuti Alur_Cabang/Event_Koita.

init 1 python:
    def kk_koita_collapse(delta):
        store.runtuh_koita = max(0, min(100, runtuh_koita + delta))
    def kk_koita_aware(delta):
        store.koita_sadar = max(0, min(100, koita_sadar + delta))
    def kk_koita_orbit(delta):
        store.orbit_koita = max(0, orbit_koita + delta)
    def kk_koita_guilt(delta):
        pts.setdefault("rasa_bersalah_koita", 0)
        kk_adj("rasa_bersalah_koita", delta)

# --- Intel / kesadaran ---------------------------------------------------
# ┌─ PANDUAN CERITA · K-D01 · Draf yang Tertinggal
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : Koita meninggalkan naskahnya
# │ INTI    : A baca semua / B baca sebagian / C kembalikan tanpa membaca
# │ AKHIRAN : pilihan "Kutip kalimat drafnya" terbuka; intel tentang kesadaran Koita
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K_D01:
    call kk_scene_enter("koita", "Gedung Sastra · Draf tertinggal")
    nar "Map Koita tersisa di meja setelah ia dipanggil keluar. Sebuah gelas menahan halaman teratas; baris terakhir yang terlihat berhenti pada kata tetapi."
    nar "Tokoh di dalamnya sedang duduk menunggu orang yang tidak datang. Di pinggir halaman ada pertanyaan dengan tulisan lebih kecil: kalau dia tidak tahu ditunggu, siapa yang bersalah?"
    call kk_family_menu("K-D01", ["Baca semua.", "Baca sebagian lalu tutup.", "Kembalikan tanpa membaca."])
    if _return == "A":
        nar "Kau membaca sampai halaman terakhir. Tokohnya berganti pekerjaan dan tempat tinggal, tetapi setiap bab membawanya kembali ke kursi yang sama."
        nar "Aku tahu ada yang mengambil tempatku. Kalimat itu muncul dua kali; pada kemunculan kedua, kata mengambil dicoret lalu ditulis kembali."
        koita "Kamu membaca?"
        nar "Koita sudah berdiri di ambang. Kau tidak tahu sejak halaman mana ia melihatmu."
        koita "Itu masih draf. Jangan kutip bagian yang bahkan belum kupahami sendiri."
        nar "Namun kalimat itu sudah melekat dalam ingatanmu, lengkap dengan coretannya."
    elif _return == "B":
        nar "Kau membaca halaman pertama, cukup jauh untuk menemukan kemarahan di balik kesedihan tokohnya. Lalu kau menutup map tersebut."
        koita "Oh, kamu menemukan naskahku. Kupikir kubawa tadi."
        nar "Ia menyimpannya lebih cepat daripada biasanya. Kau belum mengetahui siapa yang ditunggu tokohnya, tetapi kini tahu Koita tidak lagi menulis penantian sebagai sesuatu yang manis."
    else:
        nar "Kau menutup map tanpa meneruskan baris yang terlihat. Ketika Koita kembali, kau menyerahkannya dengan gelas yang tadi menahan halaman."
        koita "Makasih. Aku harus mulai ingat membawa barang sendiri."
        nar "Ia menepuk sampul map, tersenyum malu. Isi naskah tetap menjadi sesuatu yang hanya bisa kauketahui jika ia bersedia memperlihatkannya."
    return

# ┌─ PANDUAN CERITA · K-D05 · Senyum yang Berhenti
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : koita_sadar ≥ 50
# │ INTI    : A Sapa / B pura-pura tidak lihat / C catat
# │ AKHIRAN : Trust atau intel
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K_D05:
    call kk_scene_enter("koita", "Gedung Sastra · Sudut lorong")
    nar "Pintu klub menutup setelah teman-temannya keluar. Senyum Koita tidak meredup pelan; senyum itu lenyap sekaligus, seperti gerakan yang sudah selesai dikerjakan."
    nar "Ia bersandar pada dinding dan menekan pangkal hidung. Untuk beberapa saat tidak ada versi dirinya yang sedang disiapkan untuk orang lain."
    call kk_family_menu("K-D05", ["Sapa dan tarik dia kembali ke keramaian.", "Pura-pura tidak melihat.", "Catat diam-diam kapan ini terjadi."])
    if _return == "A":
        nar "Kau memanggil namanya dan mengajak menyusul yang lain. Koita menegakkan tubuh, tetapi kau sudah cukup dekat untuk melihat matanya lelah."
        koita "Oh, kamu. Aku cuma... capek sedikit."
        nar "Ia mulai tersenyum lagi. Kau mengatakan ia tidak perlu bercerita kalau belum mau."
        koita "Boleh jalan pelan? Aku belum siap kalau harus langsung ramai lagi."
    elif _return == "B":
        nar "Kau mengalihkan langkah sebelum ia melihatmu. Dari balik sudut kau mendengar botol minuman dibuka, lalu satu tarikan napas panjang."
        nar "Ketika akhirnya Koita menyusul kelompok, ia membawa lelucon yang membuat mereka tertawa. Tidak ada yang bertanya mengapa ia tertinggal."
    else:
        nar "Kau mengingat jam, tempat, dan siapa yang baru saja pergi. Ada pola yang mulai berulang: kelelahan paling jelas muncul setelah ia berhasil membuat semua orang percaya dirinya baik-baik saja."
        nar "Keterangan itu bisa menjelaskan perilakunya. Juga bisa menjadi sesuatu yang kelak kaupakai untuk menekannya. Di ujung lorong, Koita belum tahu dirinya sedang kauubah menjadi catatan."
    return

# ┌─ PANDUAN CERITA · K-D08 · Ponsel Pemain di Meja
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : pemain meninggalkan ponsel
# │ INTI    : A Saat pemain kembali: hadapi / B jelaskan / C pura-pura tidak tahu
# │ AKHIRAN : koita_sadar +25; manuver balik dimulai lebih awal
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K_D08:
    call kk_scene_enter("koita", "Rumah Amamiya · Meja makan")
    nar "Kau kembali ke meja makan tepat saat Koita menarik tangannya dari dekat ponselmu. Layar yang kauingat masih menyala kini mulai meredup."
    koita "Ada pesan masuk. Aku lihat namanya, terus... aku membaca yang muncul."
    nar "Ia menggeser ponsel kepadamu. Pengakuannya berhenti sebelum menjelaskan berapa lama ia melihat dan bagian mana yang membuatnya diam."
    koita "Beberapa orang di situ kukenal. Sepertinya ada banyak hal yang kalian bicarakan tanpa aku."
    call kk_family_menu("K-D08", ["Hadapi: tanya apa yang ia baca.", "Jelaskan seperlunya lalu alihkan.", "Pura-pura tidak tahu ia membacanya."])
    if _return == "A":
        nar "Kau menanyakan dengan tegas apa yang ia baca. Koita menyebut pesan yang terlihat, lalu membalas pertanyaanmu dengan pertanyaan lain."
        koita "Kenapa kalian membicarakan aku seperti itu?"
        nar "Kau mengingatkan bahwa ponsel itu milikmu. Ia mengangguk, wajahnya menegang."
        koita "Iya. Aku salah membaca. Tapi sekarang aku tahu ada sesuatu yang perlu kutanyakan sendiri kepada mereka."
    elif _return == "B":
        nar "Kau memberi konteks secukupnya, membedakan bagian yang bisa kaujelaskan dari percakapan yang juga milik orang lain."
        koita "Jadi aku kehilangan bagian sebelumnya. Iya, mungkin."
        nar "Ia menerima pergantian topik yang kautawarkan. Namun ketika nama yang sama muncul dalam pembicaraan berikutnya, ia mendengarkan jauh lebih saksama daripada tadi."
    else:
        nar "Kau mengambil ponsel dan bertanya apakah airnya sudah mendidih, seolah tidak melihat apa pun. Koita menjawab dengan nada yang sama datarnya."
        koita "Sudah. Aku matikan dulu."
        nar "Punggungnya menghadapmu ketika ia menuang air. Pembicaraan yang kalian hindari tetap hadir di meja, mengambil tempat lebih luas daripada ponsel yang sudah kausimpan."
    return

# ┌─ PANDUAN CERITA · K-D09 · Foto Ayah
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : setelah K16-A
# │ INTI    : A Dengarkan / B bandingkan dengan dirimu / C alihkan
# │ AKHIRAN : akar sifat menggantung; rasa_bersalah_koita +
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K_D09:
    call kk_scene_enter("koita", "Rumah Amamiya · Malam")
    nar "Foto itu mulai lengket pada plastik album. Koita mengangkat sudutnya perlahan: seorang pria berjongkok di samping anak kecil yang memegang mainan dengan dua tangan."
    koita "Ayah kandungku. Sebelum meninggal. Aku ingat mainannya lebih jelas daripada suaranya. Itu bikin aku merasa bersalah kadang-kadang."
    nar "Ia tidak menghadapmu ketika berbicara. Ada hal yang rupanya lebih mudah dikatakan kepada foto."
    koita "Dulu kalau Ibu keluar, aku bertanya kapan pulang terus. Bahkan setelah punya keluarga lagi. Aku takut kalau nggak bertanya, orang bisa lupa ada aku."
    call kk_family_menu("K-D09", ["Dengarkan tanpa menilai.", "Bandingkan dengan dirimu sendiri.", "Alihkan ke hal lain."])
    if _return == "A":
        nar "Kau mendengarkan kisah yang tidak tersusun rapi: sepatu di pintu, makanan yang mendadak terlalu banyak, orang dewasa yang mengatakan kuat padanya sambil menangis."
        koita "Aku tahu mereka yang sekarang nggak bersalah atas itu. Nagisa bukan Ibu. Teman-temanku bukan orang yang harus menebus masa kecilku."
        nar "Ia menyentuh pinggir foto."
        koita "Tapi setiap mereka mau pergi, aku mendadak pandai mencari alasan supaya ditunda. Itu yang perlu kuhentikan, ya. Bukan menghapus rasa takutnya dulu baru mencoba."
    elif _return == "B":
        nar "Kau bercerita tentang kesepianmu sendiri, cukup untuk membuatnya tahu ia tidak sedang mengungkapkan sesuatu yang mustahil dimengerti."
        koita "Kamu juga pernah menunggu suara pintu?"
        nar "Pertanyaannya membuat pembicaraan melambat. Pengalaman kalian tidak persis sama, tetapi malam ini ia tidak perlu menerjemahkan setiap kata."
        koita "Aku senang kamu bilang. Tapi kalau nanti aku mulai menganggap kamu wajib tinggal karena pernah bilang begitu... tegur aku."
    else:
        nar "Kau mengalihkan pembicaraan ke album berikutnya. Koita mengikuti arah jarimu, mengucapkan nama orang-orang di foto keluarga yang lebih baru."
        koita "Yang itu Daisuke. Rambutnya masih banyak waktu itu."
        nar "Leluconnya berhasil mengisi ruang. Foto ayah kandungnya ia kembalikan ke plastik sebelum sempat merampungkan satu kenangan terakhir."
        nar "Sesudah album ditutup, ia meminta maaf karena sudah membuat suasana berat. Kau tahu bukan hanya suasana yang baru saja ia simpan kembali."
    return

# --- Keruntuhan (konsekuensi saja, tanpa metode) -------------------------
# ┌─ PANDUAN CERITA · K-D13 · Nama yang Dicoret
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : orbit_koita ≤ 2
# │ INTI    : A Lihat diam-diam / B ambil daftarnya / C tulis namamu sendiri di sana
# │ AKHIRAN : runtuh_koita +; pemain tahu siapa yang tersisa
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K_D13:
    call kk_scene_enter("koita", "Gedung Sastra · Daftar yang memudar")
    nar "Koita menulis tanggal di samping sebuah nama, lalu mencoretnya. Ada nama yang dicoret dua kali; garis pertama rupanya pernah ia batalkan."
    nar "Buku itu terbuka di antara piring yang belum disentuh dan ponsel tanpa notifikasi. Ia menggerakkan pena di udara sebelum memutuskan baris berikutnya."
    call kk_family_menu("K-D13", ["Lihat diam-diam siapa yang tersisa.", "Ambil daftar itu dari tangannya.", "Tulis namamu sendiri di sana."])
    if _return == "A":
        nar "Dari tempatmu berdiri kau melihat satu nama yang masih bersih. Di sampingnya tertulis tanda tanya yang digambar berkali-kali sampai kertasnya berbulu."
        nar "Kau mengingat nama itu. Yang tidak kauketahui adalah apakah Koita sedang mencatat orang yang mencintainya, orang yang bisa ia hubungi, atau orang terakhir yang belum sempat mengatakan pergi."
        nar "Ia menutup buku sebelum kau bisa mencari jawabannya."
    elif _return == "B":
        nar "Kau mengambil buku dari dekat tangannya. Koita meraih pergelanganmu, lalu segera melepasnya sendiri."
        koita "Kembalikan. Itu bukan daftar yang boleh kamu periksa."
        nar "Ia mengulurkan telapak tangan. Kau melihat betapa keras ia berusaha agar suaranya tidak meninggi."
        koita "Atau ambil saja. Kamu sudah tahu yang di dalamnya, kan? Kalian selalu tahu lebih dulu daripada aku."
        nar "Ia mendorong piring menjauh. Mengambil buku itu tidak membuat ia berhenti menghitung; kini ia hanya tak lagi melakukannya di hadapanmu."
    else:
        nar "Kau menambahkan namamu pada baris kosong. Koita menatap tulisan itu, lalu wajahmu."
        koita "Kamu tahu daftar ini tentang apa?"
        nar "Kau mengatakan ia boleh menghubungimu. Tidak ada janji bahwa kau akan selalu bisa datang, tetapi ada tawaran yang bisa ia tanyakan lagi."
        koita "Kalau begitu aku nggak akan mencoretnya cuma karena suatu hari kamu terlambat membalas."
        nar "Ia meletakkan pena. Untuk sementara, tak ada nama berikutnya yang ia periksa."
    return

# ┌─ PANDUAN CERITA · K-D16 · Pengakuan yang Disengaja
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : pemain memutuskan memberi tahu Koita semuanya
# │ INTI    : A ceritakan dengan tenang / B dengan mengejek / C tunjukkan buktinya
# │ AKHIRAN : runtuh_koita +20 sampai +40; Koita runtuh atau berbalik melawan (E-KO-10, E-KO-20)
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K_D16:
    call kk_scene_enter("koita", "Gedung Sastra · Ruang kosong")
    nar "Ruang kelas sudah kosong. Koita hendak merapikan kursi ketika kau mengatakan ada hal yang selama ini sengaja kausembunyikan darinya. Ia melepaskan sandaran kursi perlahan."
    koita "Semuanya? Jangan mulai dengan kata semuanya kalau nanti kamu menyisakan bagian yang paling penting."
    nar "Ia memilih kursi dekat pintu. Kau melihat keputusan itu, lalu memulai pengakuanmu."
    call kk_family_menu("K-D16", ["Ceritakan dengan tenang, sejujurnya.", "Katakan sambil mengejek kekalahannya.", "Tunjukkan bukti yang kaukumpulkan."])
    if _return == "A":
        nar "Kau menjelaskan perbuatanmu tanpa menyebutnya takdir, tanpa mengubah akibatnya menjadi bukti bahwa Sistem terlalu kuat untuk dilawan. Koita beberapa kali memintamu mengulang tanggal."
        koita "Waktu itu aku masih cerita ke kamu. Aku minta saran."
        nar "Ia menekan telapak tangan pada lutut, menahan gemetarnya."
        koita "Ada bagian yang memang salahku. Aku nggak mau memakai ini supaya semua kesalahanku hilang. Tapi kamu... kamu mendengarkan sambil melakukan itu."
        nar "Kejelasan memberinya bentuk untuk kemarahan. Kejelasan itu tidak membuatnya lebih mudah bernapas."
    elif _return == "B":
        nar "Kau menceritakannya sebagai kemenangan, menunggu setiap fakta membuat wajahnya semakin jatuh. Koita tidak lagi bertanya setelah kalimat ketigamu."
        koita "Sudah cukup."
        nar "Kau masih ingin menyelesaikan. Ia berdiri, memberi jarak antara kursi kalian."
        koita "Kamu mau aku menangis di sini supaya ceritamu terasa selesai? Aku nggak akan memberimu itu."
        nar "Ia pergi dengan langkah kaku. Kau belum tahu apakah diamnya akan menjadi pengasingan atau kesaksian, tetapi sejak saat itu ia tidak lagi menganggapmu orang yang bisa diajak menyelesaikan apa pun."
    else:
        nar "Kau memperlihatkan bukti yang selama ini kausimpan. Koita memeriksa satu per satu, tidak mau membiarkan penjelasanmu menjadi satu-satunya cara membacanya."
        koita "Kamu menyimpan ini seperti laporan. Buat siapa?"
        nar "Ada gambar yang ia lewati terlalu cepat, lalu ia minta dibuka kembali. Rasa ingin tahu melawan tubuhnya sendiri yang ingin berhenti melihat."
        koita "Aku perlu mengingat mana yang benar-benar terlihat di sini dan mana yang cuma kamu bilang. Aku nggak akan menyerahkan bagian itu kepadamu juga."
    return

# ┌─ PANDUAN CERITA · K-D18 · Draf Terakhir
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : runtuh_koita ≥ 60
# │ INTI    : A Selamatkan filenya / B biarkan / C baca halaman terakhirnya
# │ AKHIRAN : dibiarkan: ambisi_menulis nol; halaman terakhir berisi nama-nama heroine
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K_D18:
    call kk_scene_enter("koita", "Gedung Sastra · Layar yang kosong")
    nar "Nama-nama berkas memenuhi layar laptop Koita: versi pertama, revisi, revisi sungguhan, revisi terakhir yang ternyata diikuti enam versi lain. Ia memilih semuanya."
    koita "Aku baca lagi semalam. Semua tokohnya ingin dicintai. Bahkan waktu aku merasa sedang menulis tentang hal lain."
    nar "Ia tertawa tanpa suara, lalu menarik jendela penghapusan ke tengah layar."
    koita "Aku capek mendengarkan diriku sendiri."
    call kk_family_menu("K-D18", ["Selamatkan filenya diam-diam.", "Biarkan ia menghapusnya.", "Baca dulu halaman terakhirnya."])
    if _return == "A":
        nar "Ketika ia beranjak mengambil air, kau menyelamatkan salinan naskahnya. Ia kembali dan menghapus versi yang masih terlihat di depannya."
        koita "Sudah. Ternyata cepat."
        nar "Kau belum mengatakan ada salinan lain. Menyimpannya tidak mengembalikan keinginannya menulis; kelak kau tetap harus memutuskan bagaimana mengakui bahwa kau mengambil keputusan itu tanpa bertanya."
        nar "Namun bertahun-tahun kerjanya tidak lagi bergantung pada satu malam terburuk untuk tetap ada."
    elif _return == "B":
        nar "Kau tidak menghentikannya. Koita menyelesaikan penghapusan, lalu membuka folder kosong itu sekali lagi seolah ingin memastikan ia benar-benar sanggup melakukannya."
        koita "Sekarang nggak ada yang perlu kuselesaikan."
        nar "Ia menutup laptop. Kelegaan yang diharapkannya tidak datang. Malam itu ia tidak membicarakan buku, ide cerita, atau penerbit; besoknya pun tidak."
        nar "Yang hilang bukan hanya berkas. Ia mulai menanggalkan nama penulis dari cara memperkenalkan dirinya."
    else:
        nar "Kau meminta membaca halaman terakhir sebelum ia memutuskan. Koita ragu, lalu membuka satu berkas yang tidak memiliki judul."
        nar "Isinya nama-nama orang yang pernah dekat dengannya. Di bawahnya tertulis: aku tidak ingat kapan mereka pergi."
        koita "Aku ingat mereka mulai menyapa beda. Aku ingat berhenti dapat pesan. Tapi waktu itu aku selalu punya alasan yang membuat semuanya kelihatan sementara."
        nar "Ia memandang daftar itu lama."
        koita "Mungkin yang harus kutulis berikutnya bukan kenapa mereka pergi. Mungkin kapan aku berhenti mendengar. Aku belum tahu sanggup atau nggak."
    return

# --- Pemulihan / belok dari keruntuhan -----------------------------------
# ┌─ PANDUAN CERITA · K-D19 · Telepon Yoshie
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : runtuh_koita ≥ 60
# │ INTI    : A Jujur / B bohong / C minta ia pulang
# │ AKHIRAN : Yoshie pulang: penopang, belok ke E-KO-07; bohong: runtuh berlanjut
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K_D19:
    call kk_scene_enter("koita", "Rumah Amamiya · Telepon larut")
    nar "Yoshie menelepon dari tempat dengan siang yang belum selesai. Di rumah Amamiya, lampu dapur sudah menjadi satu-satunya lampu menyala."
    "Yoshie" "Koita selalu bilang cuma lelah. Dulu kalau lelah dia malah cerita panjang. Sekarang pesanku dijawab satu kata. Kamu tahu keadaannya?"
    nar "Di lantai atas tidak ada bunyi. Kau menatap tangga sambil memilih seberapa banyak kebenaran yang akan sampai ke ibunya."
    call kk_family_menu("K-D19", ["Jujur soal keadaannya.", "Katakan semua baik-baik saja.", "Minta ia pulang sekarang."])
    if _return == "A":
        nar "Kau menceritakan perubahan yang bisa kauamati: kuliah yang ditinggalkan, makan yang tak teratur, tulisan yang tidak disentuh. Kau membedakannya dari hal-hal yang hanya kauduga."
        "Yoshie" "Aku seharusnya bertanya lebih banyak. Bukan cuma apa dia sudah makan."
        nar "Ia terdiam, kemudian mulai membicarakan kepulangan dengan seseorang di dekatnya."
        "Yoshie" "Terima kasih sudah jujur. Aku pulang. Dan aku akan bicara dengannya tanpa meminta dia membuatku merasa jadi ibu yang baik dulu."
    elif _return == "B":
        nar "Kau mengatakan Koita hanya sibuk. Yoshie menghela napas lega, menanyakan kabar kuliahmu, lalu meminta kau menyampaikan bahwa ia menelepon."
        "Yoshie" "Bilang jangan lupa makan. Aku kirim uang tambahan besok."
        nar "Uang itu akan datang. Orang yang mengirimkannya tetap mengira rumah tersebut masih menampung seorang putra yang hanya kelelahan sementara."
        nar "Sesudah panggilan selesai, kesunyian di tangga tidak berubah. Sekarang kau ikut menjaga alasan yang membuat tak seorang pun naik untuk bertanya."
    else:
        nar "Kau memintanya pulang secepatnya. Tidak memakai kata mungkin, tidak mengecilkan keadaan agar ia tidak khawatir."
        "Yoshie" "Baik. Aku cari penerbangan. Daisuke akan bantu urus di sini."
        nar "Suaranya bergetar, tetapi pertanyaan berikutnya praktis: siapa yang sudah tahu, siapa yang bisa menemani, apakah Koita bersedia menerima teleponnya malam ini."
        "Yoshie" "Kamu nggak perlu menanggung ini sendirian sampai aku tiba. Kita cari orang di dekatnya juga. Aku akan tetap bisa dihubungi."
    return

# ┌─ PANDUAN CERITA · K-D20 · Matsuda Mengetuk
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : runtuh_koita ≥ 70; Matsuda sekutu Koita
# │ INTI    : A Halangi / B biarkan / C ikut
# │ AKHIRAN : pemulihan: belok dari E-KO-16 ke E-KO-07
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K_D20:
    call kk_scene_enter("koita", "Gedung Sastra · Ketukan di pintu")
    nar "Matsuda datang tanpa membawa naskah atau alasan rapat klub. Ia mengetuk sampai Koita menjawab, kemudian berdiri cukup jauh dari ambang agar pintu bisa dibuka lebar."
    "Matsuda" "Aku sudah tanya ruang konseling. Sato bisa ketemu. Kamu nggak perlu menyiapkan cerita yang runtut."
    koita "Aku bahkan nggak tahu harus mulai dari apa."
    "Matsuda" "Bilang itu juga boleh. Aku bisa antar sampai pintu."
    call kk_family_menu("K-D20", ["Halangi, katakan Koita baik-baik saja.", "Biarkan Matsuda membawanya.", "Ikut mengantar mereka."])
    if _return == "A":
        nar "Kau menyela, mengatakan Koita baik-baik saja dan hanya perlu istirahat. Matsuda tidak menatapmu; ia masih menunggu jawaban orang di ambang pintu."
        "Matsuda" "Aku ingin dengar dari dia."
        nar "Tetapi Koita sudah menangkap jalan termudah untuk mengakhiri percakapan. Ia mengangguk pada ucapanmu dan meminta maaf karena membuat khawatir."
        nar "Matsuda meninggalkan cara menghubunginya sebelum pergi. Pintu tertutup, dan keheningan yang kaupertahankan kembali memenuhi kamar."
    elif _return == "B":
        nar "Kau bergeser memberi jalan. Matsuda menunggu Koita mengambil jaket, tidak mengomentari berapa lama waktu yang ia perlukan."
        koita "Satu kali dulu. Aku nggak janji bisa cerita."
        "Matsuda" "Aku dengar. Satu kali dulu."
        nar "Koita keluar dengan langkah ragu. Kali ini seseorang mendampinginya tanpa meminta ia menjadi ceria sebagai bayaran atas kehadiran itu."
    else:
        nar "Kau menawarkan ikut sampai ruang tunggu. Koita memeriksa wajahmu, lalu mengangguk."
        koita "Tapi nanti di dalam aku sendiri. Ada hal yang mungkin belum bisa kukatakan di depan kalian."
        nar "Kau menyetujuinya. Di perjalanan kalian membicarakan jalan yang paling teduh, hal kecil yang tidak memerlukan Koita menjelaskan seluruh hidupnya."
        nar "Di depan ruang konseling ia berhenti, menarik napas, lalu mengetuk atas kemauannya sendiri. Kalian menunggu di luar."
    return

# ┌─ PANDUAN CERITA · K-D21 · Satu yang Tidak Ikut Percaya
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : framing_koita terpasang (06_Chiasa.md §14)
# │ INTI    : A Terima dukungan itu / B tolak karena malu / C minta mereka diam saja
# │ AKHIRAN : menerima: runtuh_koita −15, dan orang itu bisa menjadi saksi yang meruntuhkan framing; menolak: makin sendirian; minta diam: tertunda, bukan dihapus
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K_D21:
    call kk_scene_enter("koita", "Gedung Sastra · Yang tidak ikut")
    nar "Seseorang yang mengenal Koita sejak sebelum rumor itu datang menghampirinya di koridor. Orang itu tidak berkata bahwa Koita mustahil berbuat salah. Ia mengatakan ada bagian tuduhan yang bertentangan dengan apa yang diketahuinya sendiri."
    nar "Koita mendengarkan dengan wajah tertunduk. Setelah berhari-hari dicari hanya untuk dimintai penjelasan, tawaran untuk didengarkan justru membuatnya sulit menjawab."
    koita "Kamu tahu orang akan bilang apa kalau kelihatan bicara denganku?"
    call kk_family_menu("K-D21", ["Terima dukungan itu.", "Tolak karena malu.", "Minta mereka diam saja."])
    if _return == "A":
        nar "Dukungan itu diterima. Koita duduk di bangku koridor, mempersilakan orang tersebut menyelesaikan apa yang ingin dikatakannya."
        koita "Aku nggak minta kamu membelaku untuk hal yang nggak kamu tahu. Kalau ada yang memang kamu lihat... tolong jangan biarkan mereka menggantinya dengan cerita lain."
        nar "Ia menangis setelah kalimatnya selesai, berusaha menghapus air mata sebelum orang lewat. Pendampingnya tetap duduk. Kini ada ingatan lain yang tak sepenuhnya berada dalam kendali fitnah."
    elif _return == "B":
        koita "Jangan. Nanti kamu ikut kena. Aku nggak sanggup melihat satu orang lagi menyesal mengenalku."
        nar "Ia menolak sebelum dukungan itu sempat mengambil bentuk. Orang tersebut memberi cara menghubunginya dan mengatakan tawarannya tidak kedaluwarsa sore ini."
        nar "Koita menyimpan nomor itu, tetapi tetap pergi sendirian. Malu membuatnya menganggap kehadirannya sendiri sebagai ancaman bagi orang yang masih mau mendekat."
    else:
        nar "Koita meminta agar orang itu tidak bicara dulu. Ia ingin satu hari tanpa melihat namanya menjadi perdebatan baru."
        koita "Aku tahu mungkin itu membantu. Aku cuma... belum sanggup menghadapi semua orang lagi."
        nar "Permintaannya didengar, tetapi apa yang diketahui saksi tidak berubah. Dukungan itu menunggu kesempatan lain; sementara itu versi yang sudah beredar tetap menjadi versi yang paling mudah ditemukan orang."
    return

init 1 python:
    # Intel / kesadaran
    _hook("K-D01-A", lambda: (kk_flag("kutipan_draf_koita"), kk_koita_aware(5)))
    _hook("K-D01-B", lambda: kk_koita_aware(2))
    _hook("K-D05-A", lambda: kk_rel("koita","trust",4))
    _hook("K-D05-C", lambda: (kk_flag("pola_koita_dicatat"), kk_koita_aware(3)))
    _hook("K-D08-A", lambda: (kk_koita_aware(25), kk_flag("koita_manuver_balik")))
    _hook("K-D08-B", lambda: kk_koita_aware(10))
    _hook("K-D08-C", lambda: (kk_koita_aware(25), kk_koita_suspect(8)))
    _hook("K-D09-A", lambda: (kk_rel("koita","trust",5), kk_koita_guilt(6)))
    _hook("K-D09-B", lambda: (kk_rel("koita","intim",4), kk_flag("koita_merasa_dekat")))
    _hook("K-D09-C", lambda: kk_koita_guilt(3))
    # Keruntuhan (konsekuensi)
    _hook("K-D13-A", lambda: (kk_koita_collapse(8), kk_flag("sisa_orbit_diketahui")))
    _hook("K-D13-B", lambda: kk_koita_collapse(12))
    _hook("K-D13-C", lambda: (kk_koita_collapse(5), kk_koita_orbit(1)))
    _hook("K-D16-A", lambda: (kk_koita_collapse(20), kk_flag("koita_diberi_tahu")))
    _hook("K-D16-B", lambda: (kk_koita_collapse(40), kk_flag("koita_berbalik")))
    _hook("K-D16-C", lambda: (kk_koita_collapse(30), kk_flag("koita_diberi_tahu")))
    _hook("K-D18-A", lambda: kk_flag("naskah_koita_diselamatkan"))
    _hook("K-D18-B", lambda: (kk_adj("ambisi_menulis_koita",-100), kk_koita_collapse(10)))
    _hook("K-D18-C", lambda: kk_koita_guilt(8))
    # Pemulihan / belok
    _hook("K-D19-A", lambda: (kk_flag("yoshie_pulang"), kk_koita_collapse(-15)))
    _hook("K-D19-B", lambda: kk_koita_collapse(5))
    _hook("K-D19-C", lambda: (kk_flag("yoshie_pulang"), kk_koita_collapse(-20)))
    _hook("K-D20-A", lambda: kk_koita_collapse(6))
    _hook("K-D20-B", lambda: (kk_koita_collapse(-20), kk_flag("koita_ke_konselor")))
    _hook("K-D20-C", lambda: (kk_koita_collapse(-25), kk_flag("koita_ke_konselor")))
    _hook("K-D21-A", lambda: (kk_koita_collapse(-15), kk_flag("saksi_koita_berdiri")))
    _hook("K-D21-B", lambda: kk_koita_collapse(8))
    _hook("K-D21-C", lambda: kk_flag("saksi_koita_tertunda"))
