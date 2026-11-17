# Shiori awal (S03, S06, S08, S11, S12). Senyum yang tak terbaca; ia menilai diam-diam.
# Menyontek masuk daftar kebohongan (dibaca S13); menyebar rumor merusak reputasi.
# Efek mengikuti Event_Shiori dan Alur_Cabang/05; angka adalah setelan prototipe.
# ┌─ PANDUAN CERITA · S03 · Payung Hujan
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : dasar manga: ia dan Koita berbagi payung.
# │ INTI    : A intersep / B tawarkan payung kedua / C biarkan.
# │ AKHIRAN : menentukan ketertarikan Shiori pada Koita.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S03:
    call kk_scene_enter("shiori", "Klub Catur · Hujan")
    nar "Hujan menahan Shiori di depan klub. Koita membuka payung dan menawarkan berjalan ke gerbang bersama, lalu tampak bingung ketika ia menanyakan apakah ia sendiri akan kebasahan."
    shiori "Kau sudah membayangkan adegan yang baik, Amamiya. Belum menghitung lebar payungnya."
    nar "Ia tersenyum, menerima kebaikan kecil itu tanpa terburu-buru menamainya ketertarikan. Ketika melihatmu, ia mengangkat alis sedikit, menunggu apakah kau ingin ikut menentukan siapa berjalan dengan siapa."
    call kk_family_menu("S03", ["Sela dan tawarkan mengantarnya sendiri.", "Tawarkan payung kedua untuk mereka berdua.", "Biarkan saja mereka berdua."])
    if _return == "A":
        shiori "Oh? Kau cepat sekali menengahi. Menarik."
        nar "Kau menawarkan mengantarnya sendiri. Shiori menanyakan mengapa sebelum mengubah rencana. Di depan pertanyaan yang sederhana itu, campur tanganmu harus mencari alasan yang dapat diucapkan terang-terangan."
    elif _return == "B":
        shiori "Sopan sekali. Aku mencatat itu."
        nar "Payung kedua membuat tak seorang pun perlu berjalan terlalu dekat agar tetap kering. Shiori berterima kasih dan membiarkan Koita memutuskan sendiri apakah masih ingin berjalan ke arah yang sama."
    else:
        nar "Kau membiarkan mereka berangkat. Koita mendengarkan sindirannya dengan tawa malu, lalu memiringkan payung lebih jauh untuk melindungi bahunya. Shiori menyadari gerakan itu, tetapi belum memberinya arti lebih daripada perhatian yang sungguh dilakukan."
    return

# ┌─ PANDUAN CERITA · S06 · Turnamen Klub Catur
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia berpartisipasi.
# │ INTI    : A hadir / B ikut / C absen.
# │ AKHIRAN : Trust.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S06:
    call kk_scene_enter("shiori", "Klub Catur · Turnamen")
    nar "Shiori memeriksa jadwal turnamen dan menawarkan kursi dengan gerakan yang sama seperti menyambut lawan. Di sini nama keluarganya tidak dapat memindahkan bidak setelah langkah yang buruk. Ia tampak menikmati itu."
    shiori "Kau menonton, bertanding, atau hanya lewat? Ketiganya boleh. Aku hanya ingin tahu sebelum terlanjur senang melihatmu duduk."
    call kk_family_menu("S06", ["Hadir dan dukung permainannya.", "Ikut bertanding melawannya.", "Lewat saja tanpa menonton."])
    if _return == "A":
        shiori "Kau tetap sampai babak terakhir. Tidak banyak yang begitu."
        nar "Kau menunggu bahkan ketika permainan menjadi lambat. Sesudahnya Shiori mengajak membahas satu keputusan yang diragukannya, memberi tempat pada pendapatmu meski tidak datang sebagai peserta."
    elif _return == "B":
        shiori "Berani. Aku suka lawan yang mau duduk di seberangku."
        nar "Pertandingannya menuntut seluruh perhatianmu. Shiori tidak mengurangi keseriusan untuk tampak ramah, dan setelah selesai ia menjelaskan satu langkahnya tanpa membuat penjelasan itu terdengar seperti belas kasihan."
    else:
        nar "Kau melanjutkan langkah. Shiori mengucapkan selamat jalan dan kembali ke jadwal. Pertandingan akan tetap berarti baginya tanpa penonton yang sedang tidak ingin hadir."
    return

# ┌─ PANDUAN CERITA · S08 · Festival: Satu Tahun
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : peringatan perkenalan dengan Koita.
# │ INTI    : A hadir / B mengantisipasi / C mengganggu.
# │ AKHIRAN : dasar manga: ia mulai mencintai Koita.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S08:
    call kk_scene_enter("shiori", "Klub Catur")
    nar "Shiori mengingat tanggal pertemuan dengan Koita lebih tepat daripada rincian sebuah kemenangan. Ia tampak sedikit jengkel pada fakta bahwa ingatan itu datang tanpa diminta."
    shiori "Setahun sejak festival itu. Aku ingat dia menawarkan bantuan tanpa lebih dahulu bertanya keluargaku siapa. Banyak orang bisa melakukan itu. Ternyata aku tetap mengingat yang satu ini."
    call kk_family_menu("S08", ["Temani ia memperingatinya dengan tenang.", "Antisipasi ke mana perasaannya mengarah.", "Ganggu peringatan kecil itu."])
    if _return == "A":
        shiori "Terima kasih sudah menemani. Aku tidak biasa mengakui hal seperti ini."
        nar "Kau mendengarkan tanpa mengubah perasaannya menjadi tantangan untuk direbut. Shiori berbicara lebih jauh, termasuk keraguannya tentang apakah kebaikan Koita disertai kejelasan yang belum pernah ia tanyakan."
    elif _return == "B":
        nar "Kau memperhatikan pilihan katanya. Ia belum menjanjikan cinta, tetapi sudah memberi tempat bagi kemungkinan yang dahulu akan ditutup dengan sindiran. Mengetahui arah itu memberi kesempatan bertindak sebelum terlambat, juga tanggung jawab atas bagaimana kau akan memakai pengetahuan tersebut."
    else:
        shiori "...Begitu. Kucatat juga yang satu ini."
        nar "Gangguanmu membuatnya berhenti bercerita. Ia mengembalikan percakapan ke jadwal festival, cukup sopan untuk tidak menegur di depan orang lain dan cukup jelas untuk menunjukkan bahwa ruang pribadi tadi sudah ditutup."
    return

# ┌─ PANDUAN CERITA · S11 · Peringkat Pertama
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ujian.
# │ INTI    : A kompetisi / B bantu / C menyontek.
# │ AKHIRAN : C masuk daftar.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S11:
    call kk_scene_enter("shiori", "Klub Catur")
    nar "Shiori menelusuri hasil ujian, berhenti pada satu kesalahan yang membuat peringkat pertamanya belum aman. Ia tidak mengatakan penilaiannya keliru; ia ingin tahu bagian mana yang tak cukup baik dipersiapkan."
    shiori "Aku ingin menang karena pekerjaanku. Kau ingin bersaing atau membantu, keduanya akan kuterima. Tapi jangan kira aku mencari seseorang yang cukup sayang untuk memberiku kemenangan."
    call kk_family_menu("S11", ["Bersaing dengannya secara jujur.", "Bantu ia belajar.", "Tawarkan cara menyontek diam-diam."])
    if _return == "A":
        shiori "Bagus. Kalahkan aku dengan benar kalau bisa."
        nar "Kalian membandingkan persiapan tanpa saling memberikan jawaban yang seharusnya dikerjakan sendiri. Persaingan itu membuatnya lebih hidup daripada pujian panjang tentang betapa tentu ia akan menang."
    elif _return == "B":
        shiori "Berdua ternyata lebih cepat. Terima kasih."
        nar "Ia menerima bantuanmu pada bagian yang belum dikuasai dan menawarkan keahliannya untuk bagian lain. Pada meja itu, membutuhkan seseorang tidak mengharuskannya berpura-pura tidak pernah salah."
    else:
        shiori "...Kau menawarkan itu. Aku akan mengingatnya."
        nar "Kau menawarkan kecurangan sebagai bantuan. Shiori menutup bahan belajar sebelum membalas dengan senyum tipis."
        shiori "Yang menarik, kau mengira aku ingin menang lebih besar daripada ingin dapat mempercayai caraku menang. Itu informasi penting tentangmu."
    return

# ┌─ PANDUAN CERITA · S12 · Rumor tentang Shiori
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : Mei menulis.
# │ INTI    : A bantu bantah / B diam / C menyebar.
# │ AKHIRAN : reputasi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S12:
    call kk_scene_enter("shiori", "Klub Catur")
    nar "Tulisan Mei menyebut kedekatan dan prestasi Shiori dengan cara yang membuat nama keluarganya menjadi jawaban bagi semua hal. Shiori membaca sampai selesai, lalu mengembalikan ponsel."
    shiori "Ia cukup cermat membicarakan orang yang dikenal semua orang, dan cukup ceroboh untuk mengira itu sama dengan mengenalku."
    call kk_family_menu("S12", ["Bantu bantah tulisan itu.", "Diamkan saja.", "Ikut menyebarkan tulisan itu."])
    if _return == "A":
        shiori "Kau membelaku tanpa kuminta. Itu... tidak biasa."
        nar "Kau membantah yang tidak berdasar tanpa menambahkan pujian yang juga tidak dapat diperiksa. Shiori menanyakan apakah kau tak takut dianggap sedang mencari muka, lalu tampak senang ketika jawabanmu tidak berusaha membuatnya berutang."
    elif _return == "B":
        nar "Kau tidak berkomentar. Shiori tetap bersikap biasa di hadapan orang lain. Ketika kalian sendiri, ia menanyakan apakah kau tidak tahu harus berkata apa atau sungguh percaya pada tulisan itu. Ia masih memberi kesempatan bertanya sebelum menyimpulkan."
    else:
        nar "Kau ikut menyebarkan. Shiori mengetahui bahwa namamu hadir dalam perjalanan kabar itu. Pada pertemuan berikutnya ia menyapamu sopan, menanyakan apakah tulisannya cukup menghibur."
        nar "Ia tidak membutuhkan suara keras untuk membuatmu sadar ada bagian yang tidak lagi dianggap gurauan."
    return

init 1 python:
    _hook("S03-A", lambda: kk_adj("respek_shiori",3))
    _hook("S03-B", lambda: kk_adj("respek_shiori",5))
    _hook("S06-A", lambda: (kk_rel("shiori","trust",4), kk_adj("respek_shiori",3)))
    _hook("S06-B", lambda: (kk_rel("shiori","trust",5), kk_adj("respek_shiori",5)))
    _hook("S06-C", lambda: kk_adj("respek_shiori",-3))
    _hook("S08-A", lambda: kk_rel("shiori","trust",5))
    _hook("S08-B", lambda: kk_flag("shiori_cinta_koita_dikenal"))
    _hook("S08-C", lambda: (kk_adj("marah_shiori",5), kk_adj("respek_shiori",-5)))
    _hook("S11-A", lambda: kk_adj("respek_shiori",5))
    _hook("S11-B", lambda: (kk_rel("shiori","trust",4), kk_adj("respek_shiori",3)))
    _hook("S11-C", lambda: kk_adj("daftar_kebohongan_shiori",1))
    _hook("S12-A", lambda: (kk_rel("shiori","trust",6), kk_adj("respek_shiori",5)))
    _hook("S12-B", lambda: kk_adj("marah_shiori",3))
    _hook("S12-C", lambda: (kk_adj("marah_shiori",10), kk_flag("shiori_rumor_disebar")))
