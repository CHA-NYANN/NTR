# Event dinamis Nagisa (N-D05, N-D06, N-D07, N-D10, N-D11, N-D12, N-D13).
# Arc kelekatan/posesif Nagisa yang HANGAT sampai menekan, memakai variabel
# yang sudah ada (kelekatan_nagisa, gengsi_nagisa, jeal, stage, haruto_kenal).
# Gerbang yandere keras (N14-N18) TIDAK dibuka. Cabang posesif ditulis sebagai
# konsekuensi dan karakter. Nilai adalah setelan prototipe; mengikuti Event_Nagisa.

init 1 python:
    def kk_haruto_suspect(delta):
        pts.setdefault("haruto_curiga", 0)
        kk_adj("haruto_curiga", delta)

# --- 3 pilihan (kk_family_menu) ------------------------------------------
# ┌─ PANDUAN CERITA · N-D06 · Kunci Cadangan
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Sakurajima Nagisa
# │ AWALAN  : tahap ≥ 3; kelekatan ≥ 75
# │ INTI    : A Beri / B tolak / C beri kunci palsu
# │ AKHIRAN : memberi: N23 dan kunjungan malam datang lebih awal; kunci palsu ketahuan: luka_bohong +30
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N_D06:
    call kk_scene_enter("nagisa", "Rumah Amamiya · Ambang pintu")
    nar "Nagisa masih berdiri di ambang meskipun barang yang dibawanya sudah diserahkan. Ia menunjuk gantungan kunci di dekat pintu, lalu menyebut tiga keadaan darurat yang belum pernah terjadi."
    nagisa "Kalau ada kunci cadangan untukku, lebih praktis. Kamu sakit, lupa barang, atau nggak dengar bel... aku bisa bantu."
    nar "Ia mengatakannya seperti usul rumah tangga biasa. Tangan yang menunggu di dekat tas menunjukkan betapa penting jawabanmu baginya."
    call kk_family_menu("N-D06", ["Beri ia kunci cadangan.", "Tolak dengan baik.", "Beri kunci yang tidak benar-benar cocok."])
    if _return == "A":
        nar "Kau menyerahkan kunci dan mulai membicarakan kapan ia boleh memakainya. Nagisa lebih dahulu tersenyum, mengusap permukaan logam dengan ibu jari."
        nagisa "Aku akan jaga. Sekarang kalau kamu diam, aku bisa memastikan sendiri kamu nggak kenapa-kenapa."
        nar "Kau baru memberikan akses ke sebuah rumah. Dalam pikirannya, akses itu juga menjanjikan jawaban untuk kecemasan yang belum tentu berkaitan dengan pintu."
    elif _return == "B":
        nar "Kau menolak dengan baik dan mengatakan kedatangan tetap perlu disepakati. Nagisa membetulkan tali tas sebelum menjawab."
        nagisa "Oh. Iya. Aku cuma menawarkan bantuan."
        nar "Ia memaksakan tawa lalu berpamitan lebih cepat. Batasmu masuk akal; untuk saat ini ia masih mendengarnya sebagai ukuran seberapa jauh dirinya boleh dianggap dekat."
    else:
        nar "Kau menyerahkan kunci yang tidak cocok. Nagisa menerimanya dengan wajah lega, mempercayai bahwa kau baru saja memberinya tempat yang lebih pasti dalam hidupmu."
        nagisa "Terima kasih. Aku nggak akan sembarangan."
        nar "Suatu hari logam itu akan gagal memutar pintu. Yang terbuka saat itu bukan rumahmu, melainkan kenyataan bahwa batas yang tidak berani kauucapkan telah diganti dengan kebohongan yang bisa ia pegang."
    return

# ┌─ PANDUAN CERITA · N-D07 · Haruto di Depan Rumah
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Sakurajima Nagisa
# │ AWALAN  : haruto_curiga ≥ 50; pemain di D2 malam hari
# │ INTI    : A Jujur / B bohong / C ajak minum
# │ AKHIRAN : Haruto bercerita masa kecil Nagisa; ia menjadi sekutu atau lawan
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N_D07:
    call kk_scene_enter("nagisa", "Depan Rumah Amamiya · Larut")
    nar "Haruto melonggarkan dasi saat melihatmu di depan rumah Amamiya. Ia semula melambaikan tangan, kemudian berhenti ketika menyadari jam dan wajahmu yang tidak sepenuhnya santai."
    "Haruto" "Aku baru pulang lembur. Kamu sendiri ada urusan apa malam-malam? Ini menyangkut Nagisa?"
    nar "Suaranya tenang, tetapi ia tidak melanjutkan langkah sebelum mendapat jawaban."
    call kk_family_menu("N-D07", ["Jujur kenapa kau ada di sini.", "Karang alasan.", "Ajak ia bicara sambil minum."])
    if _return == "A":
        nar "Kau menjelaskan alasanmu dan membatasi cerita pada hal yang benar-benar kauketahui. Haruto mendengarkan, lalu menanyakan apakah Nagisa tahu kalian membicarakannya."
        "Haruto" "Aku ingin bantu, bukan membuat dia merasa semua orang bersekutu menentukan hidupnya. Terima kasih sudah terus terang. Kalau ada yang perlu dibicarakan dengannya, aku akan bicara sendiri."
        nar "Ia memberikan nomor yang bisa dihubungi. Kepeduliannya kini punya jalan untuk sampai kepadamu tanpa melalui dugaan."
    elif _return == "B":
        nar "Kau mengarang alasan. Haruto mengangguk, lalu mengulangi satu detail yang tidak sesuai dengan apa yang baru kaukatakan."
        "Haruto" "Oh. Begitu. Aku salah dengar mungkin."
        nar "Ia tidak mendebat di jalan. Justru kesopanannya terasa kurang menenangkan ketika ia kemudian menanyakan kapan terakhir kali Nagisa pulang dalam keadaan baik."
    else:
        nar "Kau mengajaknya membeli minum dan bicara. Haruto memilih sesuatu tanpa alkohol, mengatakan masih perlu bekerja esok pagi."
        "Haruto" "Dulu Nagisa kalau kalah main akan marah, lalu menyiapkan tempat supaya kami main lagi. Dia sulit bilang ingin ditemani. Tapi itu nggak berarti orang lain harus mengalah terus agar dia tenang."
        nar "Ia tidak sedang membenarkan adiknya. Ia memberimu bagian masa lalu yang mungkin membantu mendengar kebutuhan di balik suaranya, tanpa harus mengikuti semua tuntutannya."
    return

# ┌─ PANDUAN CERITA · N-D11 · Ruang di Gambar Kerja
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Sakurajima Nagisa
# │ AWALAN  : studio ≥ 70; Aff ≥ 55; tahap ≤ 2
# │ INTI    : A Tanya maksudnya / B pura-pura tidak paham / C tambahkan sesuatu ke gambarnya
# │ AKHIRAN : pengakuan lewat arsitektur; E-NA-01 menguat
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N_D11:
    call kk_scene_enter("nagisa", "Studio Arsitektur · Gambar kerja")
    nar "Nama ruang di denah Nagisa biasanya praktis: tidur, kerja, makan. Satu ruangan pada gambar terbaru justru diberi namamu, dengan catatan tentang cahaya sore dan tempat menyimpan barang yang kausering bawa."
    nagisa "Itu cuma latihan membayangkan penghuni. Kalau penghuninya jelas, lebih mudah mendesain. Jangan langsung memasang wajah begitu."
    call kk_family_menu("N-D11", ["Tanya apa maksud ruangan itu.", "Pura-pura tidak paham.", "Tambahkan sesuatu ke gambarnya."])
    if _return == "A":
        nar "Kau menanyakan mengapa memilihmu sebagai penghuni. Nagisa menatap ujung penggaris, lalu mengaku ia ingin kau punya ruang yang tidak harus dipinjam dari siapa pun."
        nagisa "Kalau nanti ada kamu, aku ingin tahu kamu suka tempatnya. Bukan cuma bilang bagus karena aku yang bikin."
        nar "Kalimat itu lebih dekat pada pengakuan daripada pembahasan tugas. Ia membiarkanmu melihat denah sampai selesai."
    elif _return == "B":
        nar "Kau berpura-pura mengira namamu hanya contoh acak. Nagisa menunggu, memberi satu kesempatan lagi dengan menunjukkan catatan yang sangat khusus tentangmu."
        nagisa "Iya. Contoh saja."
        nar "Ia menutup denah ketika kau tetap menghindar. Pada pembicaraan berikutnya ia hanya menunjukkan bagian yang tidak memiliki nama penghuni."
    else:
        nar "Kau meminta izin menambahkan catatan kecil, lalu menandai tempat duduk dekat jendela. Nagisa bertanya mengapa memilih sisi itu."
        nar "Kau mengatakan dari sana bisa melihat meja kerjanya tanpa menghalangi. Ia menunduk cukup lama sebelum mengambil pensil kembali."
        nagisa "Kalau begitu jalannya harus lebih lebar. Biar kalau aku mengantuk, nggak menabrak kursimu."
        nar "Ia mulai merancang kebiasaan kalian bersama tanpa sekali pun menyebut semua ini hanya contoh lagi."
    return

# ┌─ PANDUAN CERITA · N-D12 · Nacchan-oneechan
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Sakurajima Nagisa
# │ AWALAN  : Chiasa host; momen emosional
# │ INTI    : A Pakai dengan sungguh-sungguh / B bercanda / C tidak
# │ AKHIRAN : E-NA-10 menguat, atau gengsi tersinggung
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N_D12:
    call kk_scene_enter("nagisa", "Taman Lingkungan · Senja")
    nar "Nagisa berhenti dekat ayunan yang kini terlalu kecil untuk kalian. Ia mengingat Chiasa kecil yang dahulu berlari menyusul sambil memanggilnya Nacchan-oneechan."
    nagisa "Kamu berhenti memanggil begitu setelah kita makin sering bertengkar. Aku bilang lega nggak dianggap tua lagi. Sebenarnya... aku ingat harinya."
    nar "Angin menggerakkan ayunan kosong. Ia menatap rantainya, memberimu ruang untuk menentukan apa yang ingin kauambil dari masa lalu."
    call kk_family_menu("N-D12", ["Pakai panggilan itu dengan sungguh-sungguh.", "Pakai sambil bercanda.", "Jangan pakai."])
    if _return == "A":
        chiasa "Nacchan-oneechan. Aku masih ingat."
        nar "Nagisa menoleh tanpa sempat menyiapkan wajah marah. Panggilan itu terdengar berbeda di antara dua perempuan yang telah tumbuh dan pernah menjadi saingan."
        nagisa "Jangan cuma dipakai karena aku tadi sedih. Aku ingin dengar lagi kalau kamu memang ingin mengatakannya."
        nar "Kau mengangguk. Untuk sementara, kelembutan tidak perlu disembunyikan sebagai kekalahan."
    elif _return == "B":
        nar "Kau menirukan panggilan kecil itu dengan nada bercanda. Nagisa sempat tersenyum refleks, lalu menyadari kau sedang menampilkan masa lalu sebagai sesuatu yang lucu."
        nagisa "Jangan begitu. Aku baru saja bilang itu penting."
        nar "Ia beranjak dari ayunan. Kalian tetap bisa berjalan bersama, tetapi bagian pembicaraan yang tadi terbuka kini ditutup dengan keluhan tentang angin."
    else:
        nar "Kau tidak menggunakan panggilan itu. Nagisa menunggu, kemudian menendang kerikil kecil dengan ujung sepatu."
        nagisa "Nggak apa-apa. Kita memang sudah bukan anak kecil."
        nar "Ia mengatakannya sebagai kesimpulan yang wajar. Di perjalanan pulang, ia memanggilmu Chiasa dengan jelas, seperti mengingatkan dirinya bahwa kedekatan lama tidak bisa diminta kembali hanya karena dirindukan."
    return

# ┌─ PANDUAN CERITA · N-D13 · Jendela Seberang
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Sakurajima Nagisa
# │ AWALAN  : Chiasa host; tahap ≥ 3
# │ INTI    : A Lambaikan tangan / B tutup tirai / C keluar menemuinya
# │ AKHIRAN : kelekatan bergeser; pengawasan menjadi terbuka
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N_D13:
    call kk_scene_enter("nagisa", "Rumah Amamiya · Jendela seberang")
    nar "Kau melihat gerakan di jendela seberang ketika hendak mematikan lampu. Nagisa berdiri di balik kaca, cukup terang untuk dikenali. Ia tidak mengalihkan pandangan saat tahu sudah terlihat."
    nar "Ponselmu diam. Kehadirannya di sana terasa seperti pertanyaan yang menuntut jawaban tanpa perlu diketuk atau dikirim."
    call kk_family_menu("N-D13", ["Lambaikan tangan padanya.", "Tutup tirai.", "Keluar dan temui ia langsung."])
    if _return == "A":
        nar "Kau melambaikan tangan. Nagisa membalas, kemudian mengangkat ponsel dan mengirim pertanyaan apakah kau akan tidur."
        nar "Kalian bertukar kabar singkat. Ia tampak lega setelah mendapat jawaban, tetapi tidak segera meninggalkan jendela. Kehangatan sapaan itu juga sedang mengajarinya bahwa menunggu di sana akan membuatmu menjawab."
    elif _return == "B":
        nar "Kau menutup tirai. Cahaya dari seberang masih terlihat di sela kain ketika kamarmu sendiri sudah gelap."
        nar "Kau berhak menutup malam tanpa disaksikan. Di tempat lain, Nagisa menghadapi batas itu sendirian, menatap sesuatu yang tidak lagi bisa dipakai untuk memastikan keberadaanmu."
    else:
        nar "Kau menghubunginya untuk bertemu di luar, lalu menunggu di tempat terang dekat rumah. Nagisa datang dengan jaket yang dikenakan terburu-buru."
        nagisa "Aku cuma lihat apakah kamu masih bangun."
        nar "Kau mengatakan lebih baik bertanya daripada mengawasi. Ia hendak membantah, kemudian melihat kembali dua jendela di atas kalian."
        nagisa "Kedengarannya buruk kalau disebut begitu. Tapi... iya, aku tadi menunggu kamu terlihat."
        nar "Untuk pertama kalinya kebiasaan itu dibicarakan langsung, tidak lagi bisa bersembunyi sepenuhnya di dalam sapaan tetangga."
    return

# --- 4 pilihan (panel manual) --------------------------------------------
# ┌─ PANDUAN CERITA · N-D05 · Tangkapan Layar
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Sakurajima Nagisa
# │ AWALAN  : jeal[[x] ≥ 60; pemain mengunggah foto bersama x
# │ INTI    : A Jelaskan jujur / B bohong / C abaikan / D blokir
# │ AKHIRAN : jujur: Trust +; bohong: luka_bohong bila ketahuan; blokir: eskalasi
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N_D05:
    call kk_scene_enter("nagisa", "Ponsel · Tangkapan layar")
    nar "Nagisa mengirim kembali foto yang baru kauunggah. Ia telah memperbesarnya pada bagian bahumu yang berdekatan dengan seseorang. Di bawah gambar hanya ada satu tanda tanya, kemudian pertanyaan lain: kenapa aku baru tahu dari sini?"
    nar "Belum ada janji yang secara jelas kaulanggar dalam gambar itu. Namun ia menunggu penjelasan seolah setiap kedekatanmu perlu lebih dahulu melewati dirinya."
    python:
        _caps = ["Jelaskan apa adanya.", "Buat alasan yang tidak benar.", "Abaikan pesannya.", "Blokir dan diamkan."]
        _rows = [(cap, Return(key), False) for key, cap in zip("ABCD", _caps)]
    call screen kk_choice_panel(_rows, "Balas Nagisa")
    $ _key = _return
    $ kk_family_choice("N-D05", _key)
    if _key == "A":
        nar "Kau menjelaskan keadaan apa adanya, termasuk bagian yang mungkin tidak ia sukai. Nagisa membaca cukup lama sebelum menjawab."
        nagisa "Aku cemburu. Iya. Tapi terima kasih nggak membuat alasan yang nanti berubah lagi."
        nar "Ia masih bertanya satu hal. Kali ini pertanyaannya mengakui bahwa ia sedang ingin memahami, bukan sudah mengetahui sesuatu yang harus kauakui."
    elif _key == "B":
        nar "Kau membuat alasan yang tidak benar. Balasan oke datang hampir langsung, disusul keheningan yang tidak memberitahumu apakah ia tenang atau sedang memeriksa."
        nar "Kau telah menyelesaikan percakapan malam ini dengan memberinya versi yang mudah diterima. Jika versi tersebut retak, gambar yang semula hanya memicu cemburu akan menjadi pengingat sebuah kebohongan yang memang kaupilih."
    elif _key == "C":
        nar "Kau membaca tanpa menjawab. Nagisa mengirim satu pesan lagi, lebih singkat, lalu menghapusnya."
        nar "Jam terus bergerak di atas percakapan yang tak selesai. Diam tidak memberi hak kepadanya untuk menuntut, tetapi juga tidak memberi penjelasan yang kauselama ini biarkan ia harapkan. Dalam ruang kosong itu ia mulai menyusun jawaban yang paling ditakutinya."
    else:
        nar "Kau memblokir percakapan. Untukmu layar berhenti bergetar; untuk Nagisa, satu saluran memastikan keberadaanmu tiba-tiba hilang."
        nar "Keesokan hari ia menunggu di tempat kalian biasa bertemu, terlalu pagi, dengan wajah yang menunjukkan ia belum tidur. Batas digital itu telah dijawab dengan kedatangan yang tidak kauundang."
    $ kk_minutes(5)
    return

# ┌─ PANDUAN CERITA · N-D10 · Pesan Ketiga Puluh Tujuh
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Sakurajima Nagisa
# │ AWALAN  : tahap ≥ 3; pemain tidur dengan mode Senyap
# │ INTI    : A Telepon langsung / B balas singkat / C jelaskan mode senyap / D marah
# │ AKHIRAN : tahap naik atau turun; contoh tubuh dan ponsel yang menjadi cabang
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N_D10:
    call kk_scene_enter("nagisa", "Pagi · 37 pesan")
    nar "Ponselmu berada dalam mode senyap semalaman. Saat dibuka, tiga puluh tujuh pesan Nagisa menunggu: pertanyaan ringan, kekhawatiran, tuduhan, permintaan maaf, lalu satu kalimat menjelang pagi bahwa ia hanya ingin tahu kau masih ada."
    nar "Kau membaca urutannya sambil baru mulai terjaga. Ia telah melewati seluruh malam yang tidak kaudengar."
    python:
        _caps = ["Telepon dia langsung.", "Balas singkat saja.", "Jelaskan soal mode senyap.", "Marah karena berlebihan."]
        _rows = [(cap, Return(key), False) for key, cap in zip("ABCD", _caps)]
    call screen kk_choice_panel(_rows, "Tanggapi Nagisa")
    $ _key = _return
    $ kk_family_choice("N-D10", _key)
    if _key == "A":
        nar "Kau menelepon. Nagisa menjawab sebelum nada pertama selesai, kemudian diam cukup lama sampai terdengar ia sedang menahan tangis."
        nagisa "Aku kira terjadi sesuatu. Terus aku marah karena berpikir kamu sengaja. Aku tahu, itu berantakan."
        nar "Suaramu menenangkannya cepat. Kelegaan itu mendekatkan kalian, sekaligus menunjukkan betapa seluruh malamnya sudah digantungkan pada satu jawaban darimu."
    elif _key == "B":
        nar "Kau membalas bahwa tadi tidur. Tanda mengetik muncul, hilang, muncul lagi. Akhirnya ia hanya mengatakan baik."
        nar "Kabar bahwa kau aman tiba tanpa jawaban untuk ketakutan yang sudah tumbuh semalaman. Nagisa membaca ulang balasan pendek itu, mencoba memutuskan apakah nadanya dingin atau dirinya saja yang terlalu jauh menafsirkan."
    elif _key == "C":
        nar "Kau menjelaskan mode senyap dan kebutuhan tidur tanpa terus memeriksa layar. Nagisa meminta diberi tahu setiap kali, lalu berhenti ketika kau mengatakan tidak selalu bisa membuat pemberitahuan untuk hal biasa."
        nagisa "Iya. Aku perlu belajar nggak menjadikan setiap diam sebagai tanda buruk. Aku belum bisa langsung, tapi aku dengar."
        nar "Kalian membicarakan kapan menghubungi orang lain jika benar-benar ada keadaan darurat. Untuk pagi ini, kekhawatiran mendapat bentuk yang lebih kecil daripada tuntutan agar kau selalu tersedia."
    else:
        nar "Kau memarahinya karena pesan yang berlebihan. Nagisa meminta maaf beberapa kali, lalu mendadak berhenti."
        nar "Hari itu tidak ada satu pesan pun darinya. Pada pertemuan berikutnya ia tersenyum cepat dan mengatakan sudah mengerti. Yang berubah jelas adalah jumlah pesan; kau belum tahu apakah ketakutannya benar-benar berkurang atau hanya menemukan tempat bersembunyi yang tak lagi mengganggu layarmu."
    $ kk_minutes(5)
    return

init 1 python:
    # N-D05 cemburu
    _hook("N-D05-A", lambda: kk_rel("nagisa","trust",6))
    _hook("N-D05-B", lambda: (kk_adj("luka_bohong",10), kk_flag("nagisa_dibohongi")))
    _hook("N-D05-C", lambda: kk_rel("nagisa","jeal",8))
    _hook("N-D05-D", lambda: (kk_rel("nagisa","jeal",15), kk_adj("kelekatan_nagisa",-10)))
    # N-D06 kunci cadangan
    _hook("N-D06-A", lambda: (kk_flag("nagisa_punya_kunci"), kk_adj("kelekatan_nagisa",8)))
    _hook("N-D06-B", lambda: kk_rel("nagisa","trust",-4))
    _hook("N-D06-C", lambda: kk_flag("nagisa_kunci_palsu"))
    # N-D07 Haruto
    _hook("N-D07-A", lambda: (kk_flag("haruto_sekutu"), kk_haruto_suspect(-5)))
    _hook("N-D07-B", lambda: kk_haruto_suspect(10))
    _hook("N-D07-C", lambda: (kk_flag("haruto_sekutu"), kk_rel("nagisa","trust",3)))
    # N-D10 pesan menumpuk
    _hook("N-D10-A", lambda: (kk_rel("nagisa","intim",4), kk_adj("kelekatan_nagisa",5)))
    _hook("N-D10-B", lambda: kk_rel("nagisa","jeal",4))
    _hook("N-D10-C", lambda: kk_rel("nagisa","trust",5))
    _hook("N-D10-D", lambda: (kk_rel("nagisa","fear",8), kk_adj("kelekatan_nagisa",-6)))
    # N-D11 denah
    _hook("N-D11-A", lambda: (kk_rel("nagisa","intim",6), kk_flag("pengakuan_arsitektur")))
    _hook("N-D11-B", lambda: kk_rel("nagisa","trust",-3))
    _hook("N-D11-C", lambda: kk_rel("nagisa","intim",4))
    # N-D12 panggilan masa kecil
    _hook("N-D12-A", lambda: (kk_rel("nagisa","intim",5), kk_flag("nacchan_dipakai")))
    _hook("N-D12-B", lambda: kk_rel("nagisa","jeal",4))
    _hook("N-D12-C", lambda: kk_rel("nagisa","trust",-3))
    # N-D13 jendela
    _hook("N-D13-A", lambda: kk_adj("kelekatan_nagisa",5))
    _hook("N-D13-B", lambda: kk_rel("nagisa","jeal",6))
    _hook("N-D13-C", lambda: (kk_rel("nagisa","intim",5), kk_flag("pengawasan_terbuka")))
