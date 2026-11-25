# Event dinamis Shiori (S-D03, S-D07, S-D13, S-D14, S-D15, S-D16, S-D17).
# Melanjutkan arc "ujian & pembongkaran" Shiori (respek_shiori, marah_shiori,
# daftar_kebohongan_shiori) yang dibangun kk_shiori_early + kk_saionji (Codex).
# Shiori menguji kejujuran pemain lewat shogi dan jebakan sosial. Cabang gelap
# (menikmati honeytrap, menjual rahasia) ditulis sebagai KONSEKUENSI, tanpa
# metode. Nilai prototipe; mengikuti Event_Shiori. S-D06 (Tojo) & S-D10 (Ogawa)
# ditunda karena butuh antagonis yang belum ada.

init 1 python:
    def kk_shiori_read(delta):
        pts.setdefault("senyum_terbaca", 0)
        kk_adj("senyum_terbaca", delta)
    def kk_shiori_proof(delta):
        pts.setdefault("bukti_terkumpul", 0)
        kk_adj("bukti_terkumpul", delta)
    def kk_koita_anger(delta):
        pts.setdefault("marah_koita", 0)
        kk_adj("marah_koita", delta)

# ┌─ PANDUAN CERITA · S-D03 · Kekalahan yang Ia Rayakan
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : respek ≥ 60
# │ INTI    : A Rayakan bersama / B sombong / C minta tanding ulang
# │ AKHIRAN : E-SH-01 menguat
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S_D03:
    call kk_scene_enter("shiori", "Klub Catur · Papan selesai")
    nar "Shiori menatap posisi akhir, kemudian tertawa tanpa menutupinya dengan sindiran. Ia mengulurkan tangan untuk mengakui hasil, matanya masih kembali ke langkah yang membuatnya kalah."
    shiori "Aku ingin mengulang. Tapi sebelumnya, selamat. Kamu membuatku lupa bagaimana biasanya menjaga wajah saat orang lain senang menang dariku."
    call kk_family_menu("S-D03", ["Rayakan kekalahannya bersama-sama.", "Sombongkan kemenanganmu.", "Minta tanding ulang sekarang."])
    if _return == "A":
        shiori "Kau tidak menyombong. Itu yang membuatmu layak dilawan lagi."
        nar "Kalian merayakannya dengan minuman kecil, membahas permainan tanpa membuat salah seorang harus mengecilkan diri. Shiori mengakui bagian yang luput, lalu menanyakan apakah kau juga gugup pada titik yang sama."
    elif _return == "B":
        shiori "...Hm. Kemenangan membuat lidah sebagian orang berubah. Kucatat itu."
        nar "Kesombonganmu membuat pembicaraan tentang permainan berubah menjadi usahamu memastikan ia merasa lebih rendah. Ia menarik tangannya dari meja, tak lagi menawarkan pembacaan langkah yang semula ingin dibagi."
    else:
        shiori "Langsung lagi? Baik. Aku suka lawan yang tidak puas hanya dengan sekali menang."
        nar "Ia menyusun ulang bidak dengan semangat baru. Kemenanganmu memberi alasan untuk bertemu dalam keadaan setara, bukan mengambil satu hasil lalu pergi sebelum ia sempat menjawab dengan permainan berikutnya."
    return

# ┌─ PANDUAN CERITA · S-D07 · Kartu yang Ia Tunjukkan
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : marah[[koita] ≥ 40
# │ INTI    : A "Kau sudah tahu?" Akui / B sangkal / C tambahkan bukti
# │ AKHIRAN : menambahkan bukti mengalihkan sasaran ke Koita (E-SH-09)
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S_D07:
    call kk_scene_enter("shiori", "Klub Catur · Kartu di meja")
    nar "Shiori meletakkan dua keterangan berdampingan. Ia tidak membaca pesan pribadi keras-keras; yang ditunjukkan adalah bagaimana dua orang dapat menerima kepastian yang tampaknya hanya ditujukan kepada masing-masing."
    shiori "Aku melihat pola pada Koita. Ada yang benar-benar disakiti, bukan sekadar orang yang terlalu berharap. Kamu sudah mengetahui sebagian ini?"
    call kk_family_menu("S-D07", ["Akui kau sudah tahu.", "Sangkal kau tahu apa-apa.", "Tambahkan bukti yang kaumiliki."])
    if _return == "A":
        shiori "Setidaknya kau tidak berpura-pura. Lalu, kita apakan ini?"
        nar "Kau mengakui yang diketahui, termasuk kapan memilih diam. Shiori menanyakan siapa yang perlu diberi ruang bicara sebelum kalian menjadikan persoalan itu pertarungan tentang Koita."
    elif _return == "B":
        shiori "Baik. Aku belum tahu apakah kamu tidak tahu atau tidak mau mengatakan. Aku akan memeriksa perbedaannya sebelum menyimpulkan."
        nar "Penyangkalanmu tidak mengakhiri pertanyaan. Ia kini harus memasukkan kemungkinan bahwa orang yang berada di dekatnya juga sedang memilih versi yang paling melindungi diri."
    else:
        nar "Kau menambahkan keterangan yang dimiliki. Amarah Shiori mendapatkan lebih banyak bentuk, sampai rencana memintai tanggung jawab mulai mendekati keinginan membuat Koita kehilangan seluruh tempatnya."
        shiori "Aku tahu apa yang bisa dibuat terlihat sekarang. Yang perlu kupikirkan adalah apakah aku masih peduli pada akibat selain dia jatuh."
    return

# ┌─ PANDUAN CERITA · S-D13 · Rahasia Palsu
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : Trust Sedang
# │ INTI    : A Simpan / B ceritakan ke orang lain / C jual ke Meisa
# │ AKHIRAN : bila rahasia itu muncul di mana pun, ia tahu sumbernya; ujian gagal dan marah[[pemain] naik
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S_D13:
    call kk_scene_enter("shiori", "Klub Catur · Titipan kecil")
    nar "Shiori menceritakan sesuatu yang tampak pribadi dan meminta kau tidak meneruskannya. Tidak ada keadaan darurat atau orang yang keselamatannya bergantung pada penyebaran kabar itu. Hanya kepercayaan yang ia letakkan di antara kalian."
    shiori "Aku ingin cerita ini tetap di sini. Kalau kamu merasa tidak bisa menjaga, katakan sekarang. Aku lebih suka batas yang jelas daripada janji yang diberikan karena mudah."
    call kk_family_menu("S-D13", ["Simpan rahasia itu.", "Ceritakan pada orang lain.", "Jual informasinya ke Meisa."])
    if _return == "A":
        nar "Kau menyimpan cerita itu. Pada pertemuan berikutnya, Shiori tidak menagih bukti bahwa kau masih ingat. Ia mengajak bicara hal lain, sedikit lebih santai memberi ruang pada sesuatu yang tidak sepenuhnya dapat diawasi."
    elif _return == "B":
        nar "Kau meneruskan cerita. Ketika kabar kembali, Shiori mengungkap bahwa cerita tersebut tidak benar dan memang digunakan untuk menguji kepercayaan."
        shiori "Aku juga mengambil keputusan yang tidak jujur dengan menguji tanpa bilang. Itu bagianku. Bagianmu adalah menyebarkan sesuatu yang sudah kamujanjikan akan dijaga."
        nar "Tak satu pun pengakuan itu membuat percakapan menjadi lebih hangat."
    else:
        "Meisa" "Informasi menarik. Akan kupakai dengan bijak. ...Atau tidak."
        nar "Kabar palsu itu mendapat jalan keluar melalui transaksi yang kaupilih. Ketika Shiori mengetahui, ia tidak lagi perlu bertanya apakah kedekatanmu mempunyai harga yang dapat dibayar orang lain."
    return

# ┌─ PANDUAN CERITA · S-D14 · Kesempatan Kecil untuk Berkhianat
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : Trust Sedang; pemain sedang butuh sesuatu
# │ INTI    : A Ambil / B tolak / C ambil lalu mengaku
# │ AKHIRAN : menolak: respek +10; mengambil: ujian gagal, dan pemain tidak sadar sedang diuji
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S_D14:
    call kk_scene_enter("shiori", "Klub Catur · Kesempatan kecil")
    nar "Ada kesempatan mengambil keuntungan kecil yang akan membuat seseorang tanpa banyak pengaruh kehilangan bagiannya. Shiori berada cukup dekat untuk mengetahui apa yang kaupilih, cukup diam untuk membuatmu merasa keputusan itu hanya milikmu."
    nar "Kebutuhanmu nyata. Orang yang akan kehilangan juga nyata, meski tak hadir di meja untuk mengajukan keberatan."
    call kk_family_menu("S-D14", ["Ambil keuntungan itu.", "Tolak dan biarkan orang itu.", "Ambil, lalu mengaku padanya."])
    if _return == "A":
        nar "Kau mengambil keuntungan. Shiori tidak menghalangi, kemudian menanyakan apakah kau akan menjelaskan keputusan yang sama dengan begitu tenang di depan orang yang dirugikan."
        nar "Pertanyaan itu datang terlambat untuk mengubah yang telah dilakukan, tepat waktu untuk menunjukkan apa yang sedang dinilainya."
    elif _return == "B":
        shiori "Kau melewatkannya. ...Menarik. Tidak banyak yang menolak saat mengira tak ada yang melihat."
        nar "Kau mengatakan tidak perlu membuat pilihanmu terdengar luar biasa. Shiori tersenyum kecil, mengakui ia berharap menemukan sesuatu yang dapat dipercaya tanpa harus terus mengatur ujian."
    else:
        shiori "Kau ambil lalu mengaku? Itu... jujur dengan cara yang aneh. Tapi jujur."
        nar "Ia menanyakan bagaimana kerugian orang lain akan dibetulkan. Pengakuanmu mendapat tempat sebagai awal bertanggung jawab, bukan pembayaran yang otomatis membuat keuntungan tersebut layak tetap dimiliki."
    return

# ┌─ PANDUAN CERITA · S-D15 · Senyum Paling Manis
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : marah[[pemain] ≥ 60; pemain belum mengaku
# │ INTI    : A Nikmati / B amati isyaratnya / C mengaku semuanya sekarang
# │ AKHIRAN : menikmati dan membuka rahasia: E-SH-16. Membaca isyarat (butuh senyum_terbaca ≥ 70) membuka kesempatan mengaku
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S_D15:
    call kk_scene_enter("shiori", "Klub Catur · Senyum paling manis")
    nar "Shiori mulai menyediakan lebih banyak waktu. Ia mengajak berjalan, duduk dekat, dan mendengarkan jawabanmu dengan perhatian yang dulu harus diperoleh melalui pertandingan panjang."
    nar "Kehangatan itu menyenangkan. Yang ganjil adalah betapa setiap topik akhirnya kembali pada hal yang belum pernah kauterangkan dengan jelas."
    call kk_family_menu("S-D15", ["Nikmati kehangatan itu apa adanya.", "Amati isyarat di balik senyumnya.", "Mengaku semuanya sekarang juga."])
    if _return == "A":
        nar "Kau menerima kedekatan sebagai bukti telah memenangkan hatinya. Ceritamu menjadi lebih terbuka, bukan karena memilih bertanggung jawab, melainkan karena merasa tak lagi perlu takut pada penilaiannya."
        nar "Shiori mendengar. Senyumnya tidak memberitahumu bagian mana yang ditanggapi sebagai keintiman dan bagian mana yang sedang disimpan untuk sesuatu yang lain."
    elif _return == "B":
        shiori "...Kau memperhatikan, ya. Tidak semua orang sadar saat sedang dibaca."
        nar "Kau menanyakan perubahan itu tanpa menganggap senyumnya sebagai jawaban. Ia berhenti menyusun pertanyaan berikutnya, terpaksa mengakui bahwa keramahan belum berarti persoalan di antara kalian sudah selesai."
    else:
        shiori "Kau mengaku? Sekarang? ...Aku tidak menyangka kau yang bergerak lebih dulu."
        nar "Kau mengatakan yang disimpan sebelum ia sempat memancing bagian tersebut keluar. Untuk sesaat kedekatan yang dipakai mengatur keadaan kehilangan kendali atas percakapan. Ia harus mendengar jawaban yang datang atas keputusanmu sendiri."
    return

# ┌─ PANDUAN CERITA · S-D16 · Langkah yang Terlalu Cepat
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : senyum_terbaca ≥ 40; sedang bertanding
# │ INTI    : A Tanya "ada apa?" / B pura-pura tidak sadar / C balas dengan langkah lambat
# │ AKHIRAN : bertanya tepat waktu: senyum_terbaca +10, dan ia sedikit terkejut
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S_D16:
    call kk_scene_enter("shiori", "Klub Catur · Langkah cepat")
    nar "Shiori menggerakkan bidak sebelum kau selesai menaruh milikmu. Tak sampai melanggar giliran, tetapi cukup tergesa untuk seseorang yang biasanya menikmati waktu berpikir. Ia tersenyum dengan wajah yang sama, lalu melakukan hal itu lagi."
    call kk_family_menu("S-D16", ["Tanya 'ada apa?' tepat waktu.", "Pura-pura tidak menyadarinya.", "Balas dengan langkah yang sengaja lambat."])
    if _return == "A":
        shiori "Kau menyadarinya secepat itu? ...Ternyata aku yang sedang terbaca sekarang."
        nar "Ia mengaku sedang memikirkan urusan lain dan menanyakan apakah boleh berhenti. Untuk sekali ini mengakui tidak dapat memusatkan diri terasa lebih dekat daripada mencoba mempertahankan permainan yang sempurna."
    elif _return == "B":
        nar "Kau berpura-pura tak melihat. Shiori terus bermain sampai satu kesalahan membuatnya harus mengakui pikirannya tidak berada di sana. Ia tidak bercerita lebih jauh, mengembalikan jarak yang tadi hampir terbuka."
    else:
        nar "Langkah lambatmu memberinya waktu. Ia menata ulang wajahnya sebelum kau sempat membaca lebih jauh."
        shiori "Terima kasih tidak mendesak. Aku tahu kamu menyadarinya. Aku akan bicara kalau sudah dapat menamainya dengan benar."
    return

# ┌─ PANDUAN CERITA · S-D17 · Papan yang Dibalik
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : bukti_terkumpul ≥ 50, atau pemain hampir menang
# │ INTI    : A Menyerah / B balas dengan langkah jujur yang tak terduga / C tertawa bersamanya
# │ AKHIRAN : menyerah: E-SH-03 atau E-SH-15; langkah jujur yang tak terduga: respek +15, satu-satunya pintu kembali setelah S18
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S_D17:
    call kk_scene_enter("shiori", "Klub Catur · Papan yang dibalik")
    shiori "Sebelum kau pikir kau menang—"
    nar "Shiori memutar papan tanpa menjatuhkan bidaknya, menunjukkan posisi dari sisi yang selama ini sengaja kauabaikan. Lalu ia meletakkan keterangan yang membuat keunggulanmu di luar permainan tidak lagi tampak aman."
    call kk_family_menu("S-D17", ["Menyerah dengan tenang.", "Balas dengan langkah jujur yang tak terduga.", "Tertawa bersamanya."])
    if _return == "A":
        shiori "Menyerah begitu saja? ...Sayang. Kukira kau punya satu langkah lagi."
        nar "Kau tidak memberi pembelaan baru. Ia kini harus menentukan apakah ingin mengakhiri pertarungan atau mempertahankan kuasa dengan membiarkanmu tetap takut. Keputusan itu bukan lagi sesuatu yang bisa disalahkan pada keenggananmu mengaku."
    elif _return == "B":
        shiori "Langkah itu... tidak kuperhitungkan. Jujur, dan justru karena itu tak terbaca. Mungkin masih ada jalan untukmu."
        nar "Kau membuka bagian yang akan merugikanmu sebelum ia memintanya, bersedia mempertanggungjawabkan kepada orang yang terkena akibat. Shiori memeriksa keputusan itu dengan hati-hati; satu langkah tidak menghapus masa lalu, tetapi bisa membuatnya berhenti mengulang perkiraan yang sama tentangmu."
    else:
        shiori "Kau tertawa? Di saat seperti ini? ...Baiklah. Aku ikut tertawa, sekali ini."
        nar "Tawa itu tidak membatalkan yang tersimpan di meja. Namun sesaat kalian melihat betapa letihnya terus membayangkan hidup sebagai pertarungan yang hanya boleh selesai ketika seseorang hancur."
    return

init 1 python:
    _hook("S-D03-A", lambda: (kk_adj("respek_shiori",8), kk_flag("shiori_kekalahan_dirayakan")))
    _hook("S-D03-B", lambda: kk_adj("respek_shiori",-5))
    _hook("S-D03-C", lambda: kk_adj("respek_shiori",4))
    _hook("S-D07-A", lambda: kk_rel("shiori","trust",5))
    _hook("S-D07-B", lambda: (kk_adj("daftar_kebohongan_shiori",1), kk_adj("marah_shiori",5)))
    _hook("S-D07-C", lambda: (kk_koita_anger(20), kk_flag("shiori_sasaran_koita")))
    _hook("S-D13-A", lambda: (kk_rel("shiori","trust",4), kk_flag("ujian_rahasia_lulus")))
    _hook("S-D13-B", lambda: (kk_adj("marah_shiori",15), kk_flag("ujian_rahasia_gagal")))
    _hook("S-D13-C", lambda: (kk_adj("marah_shiori",20), kk_flag("rahasia_dijual_mei")))
    _hook("S-D14-A", lambda: (kk_adj("marah_shiori",10), kk_flag("ujian_khianat_gagal")))
    _hook("S-D14-B", lambda: (kk_adj("respek_shiori",10), kk_flag("ujian_khianat_lulus")))
    _hook("S-D14-C", lambda: kk_adj("respek_shiori",4))
    _hook("S-D15-A", lambda: (kk_flag("shiori_senyum_dinikmati"), kk_adj("marah_shiori",5)))
    _hook("S-D15-B", lambda: kk_shiori_read(10))
    _hook("S-D15-C", lambda: (kk_adj("daftar_kebohongan_shiori",-1), kk_flag("shiori_pemain_mengaku")))
    _hook("S-D16-A", lambda: kk_shiori_read(10))
    _hook("S-D16-C", lambda: kk_rel("shiori","trust",2))
    _hook("S-D17-A", lambda: kk_flag("shiori_pemain_menyerah"))
    _hook("S-D17-B", lambda: (kk_adj("respek_shiori",15), kk_flag("shiori_langkah_jujur")))
    _hook("S-D17-C", lambda: kk_rel("shiori","intim",4))
