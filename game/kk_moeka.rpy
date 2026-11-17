# Arc Moeka (Mo03-Mo12, Mo26): wakil kelas dari keluarga miskin dengan tiga adik
# dan ayah sakit; tekanan finansial/akademik, gerbang awal fotografer Kuga, dan
# jendela intervensi menjelang krisis. Ditulis sebagai KARAKTER dan KONSEKUENSI;
# eksploitasi/krisis hanya akibatnya yang dicatat, tanpa metode. Penempatan di
# Kantin Pusat adalah prototipe reachability (🟡); locale naratif ada di dialog.
# Efek menggerakkan stres_moeka, stage[moeka], beban_keluarga. Event_Moeka.

init 1 python:
    def kk_moeka_burden(delta):
        pts.setdefault("beban_keluarga", 0)
        kk_adj("beban_keluarga", delta)
    def kk_moeka_stage(n):
        kk_stage("moeka", max(n, stage.get("moeka", 0)))

# ┌─ PANDUAN CERITA · Mo03 · Janji yang Terlupa
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia lupa janji dengan pemain.
# │ INTI    : A marah / B maklum / C bantu mengatur jadwal.
# │ AKHIRAN : Trust; B/C mengurangi stres.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo03:
    call kk_scene_enter("moeka", "Kantin Pusat · Janji terlupa")
    nar "Moeka datang ketika minumanmu sudah dingin. Ia masih memakai kartu panitia, satu peniti menahan ujung bajunya yang terlepas, dan ponselnya berbunyi sebelum ia sempat duduk."
    moeka "Maaf! Rapat molor, adikku telepon, terus aku ingat janji kita tepat waktu yang paling nggak berguna. Kamu sudah menunggu lama, ya. Aku nggak mau bilang sebentar kalau jelas bukan."
    call kk_family_menu("Mo03", ["Marah karena ia melupakan janji.", "Maklum; ia jelas kewalahan.", "Bantu ia menyusun jadwalnya."])
    if _return == "A":
        moeka "Kau benar. Aku pantas dimarahi. ...Maaf sekali lagi."
        nar "Ia membiarkan keluhanmu selesai tanpa membela diri. Namun setelahnya ia mencoba membuat suasana ramai dengan cerita yang terlalu cepat, seolah harus melunasi waktu yang hilang dengan menjadi lebih menyenangkan."
    elif _return == "B":
        moeka "Kau tidak marah? ...Terima kasih. Hari ini akhirnya ada yang tidak menuntut."
        nar "Kau mengatakan keterlambatan tetap merepotkan, tetapi bisa dibicarakan tanpa membuat seluruh dirinya menjadi masalah. Moeka berhenti tertawa, lalu meminta duduk lima menit sebelum memulai lagi."
    else:
        moeka "Kau mau bantu mengatur ini semua? ...Aku hampir lupa rasanya ditolong."
        nar "Kalian memeriksa kalender yang berisi dua janji pada jam sama dan satu tugas tanpa tanggal. Moeka menentukan mana yang bisa ditolak; kau membantu mencatat, tidak mengambil alih seluruh harinya."
        moeka "Kalau aku salah jadwal lagi, ingatkan. Tapi jangan sampai kamu yang harus hidup di dalam ponselku."
    return

# ┌─ PANDUAN CERITA · Mo04 · Pingsan Karena Lupa Makan
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : di vila.
# │ INTI    : A rawat / B panggil Miyuki / C abaikan.
# │ AKHIRAN : intimasi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo04:
    call kk_scene_enter("moeka", "Dapur vila · Pingsan")
    nar "Moeka berhenti bicara di tengah lelucon, meraih tepi meja, lalu jatuh sebelum selesai mengatakan hanya pusing. Makanan yang sejak siang ia tawarkan kepada semua orang ternyata belum sempat disentuhnya sendiri."
    nar "Belakangan ia mengaku mengurangi makan agar uang cukup dikirim ke rumah. Pengakuan itu disertai senyum malu, seolah sedang membahas siasat hemat yang sedikit kelewatan."
    call kk_family_menu("Mo04", ["Rawat ia sendiri sampai pulih.", "Panggil Miyuki untuk memeriksanya.", "Abaikan; itu bukan urusanmu."])
    if _return == "A":
        moeka "Kau menjagaku? ...Jangan bilang siapa-siapa soal kenapa aku tidak makan. Tolong."
        nar "Kau memastikan ia mendapat bantuan yang diperlukan dan menemaninya sampai keadaan lebih stabil. Saat ia mulai menawarkan kembali membantu dapur, kau mengingatkan bahwa malam ini ia juga orang yang perlu diperhatikan."
        moeka "Aku takut kalau bilang alasannya, orang berhenti percaya aku bisa mengurus diri. Tapi ternyata aku memang belum mengurus yang ini dengan benar."
    elif _return == "B":
        nar "Kau memanggil Miyuki, yang segera membantu menilai kebutuhan pertolongan berikutnya. Ia tidak membiarkan status mahasiswanya menjadi alasan menunda bantuan jika keadaan membutuhkannya."
        moeka "Aku tahu kamu masih belajar. Maaf, aku tadi bercanda karena malu. Aku sebenarnya senang ada yang datang."
    else:
        nar "Kau tidak ikut menolong. Orang lain akhirnya mendekat, sementara Moeka mulai sadar dan buru-buru meminta maaf atas keributan yang dibuat tubuhnya."
        nar "Setelahnya ia merapikan rambut dan mencoba kembali tersenyum. Di dekatmu ia kini lebih cepat mengatakan sudah makan, menutup persoalan sebelum kau sempat bertanya."
    return

# ┌─ PANDUAN CERITA · Mo05 · Kabar dari Rumah
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ibu menelepon.
# │ INTI    : A dengarkan / B alihkan / C tanya langsung.
# │ AKHIRAN : membuka masalah keluarga.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo05:
    call kk_scene_enter("moeka", "Kantin Pusat · Kabar dari rumah")
    nar "Aya menelepon ketika Moeka sedang memilih kain untuk tugas. Tangannya berhenti pada warna cerah yang baru dipuji, lalu pindah memegang tas seolah mendadak harus bersiap pulang."
    moeka "Iya, Bu. Aku dengar. Jangan bilang ke adik-adik aku panik, ya. Aku pikirkan dulu."
    nar "Setelah panggilan selesai, ia menatap kain yang masih di tangan seakan lupa tadi hendak membuat apa."
    call kk_family_menu("Mo05", ["Dengarkan kalau ia mau cerita.", "Alihkan agar ia tak perlu menjelaskan.", "Tanya langsung ada apa."])
    if _return == "A":
        moeka "Ayahku... kondisinya tidak membaik. Dan biaya terus jalan. ...Maaf, kau tidak perlu dengar ini."
        nar "Kau menunggu setelah kalimat terakhir, memberi kesempatan ia membatalkan permintaan maafnya sendiri. Moeka akhirnya bercerita tentang tiga adik, pekerjaan ibunya, dan uang yang selalu terasa sudah punya tujuan sebelum diterima."
    elif _return == "B":
        moeka "...Terima kasih sudah tidak bertanya. Kadang itu yang kubutuhkan."
        nar "Kau mengalihkan pembicaraan tanpa memaksanya tampak ceria. Beberapa menit kemudian ia kembali memilih kain, kali ini meminta pendapatmu sungguhan. Masalahnya belum hilang, tetapi ia mendapat jeda yang tidak harus dibayar dengan penjelasan."
    else:
        moeka "Kau mau tahu? ...Baik. Mungkin lebih ringan kalau satu orang tahu."
        nar "Ia bercerita lebih jauh daripada rencana awal, sampai angka dan kebutuhan keluarganya memenuhi percakapan. Mendengarnya membuatmu memahami mengapa tawaran kerja yang tampak buruk dari luar tetap dapat terlihat seperti pintu baginya."
    return

# ┌─ PANDUAN CERITA · Mo06 · Kuga Renji: Tawaran Foto
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : fotografer menawarkan pekerjaan modeling.
# │ INTI    : A dukung / B halangi / C ikut menemani.
# │ AKHIRAN : gerbang awal Kuga.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo06:
    call kk_scene_enter("moeka", "Kantin Pusat · Tawaran Kuga")
    nar "Kuga Renji memuji pakaian hasil ubahan Moeka sebelum menawarkan sesi foto. Ia membicarakan bayaran lebih panjang daripada rincian pekerjaan, dan setiap angka membuat Moeka mengingat tagihan yang berbeda."
    "Kuga" "Kamu bisa membantu rumah sekaligus membangun portofolio. Sayang kalau kesempatan ini lewat hanya karena terlalu banyak ragu."
    moeka "Aku perlu rincian sesi dan hak atas fotonya dulu. Boleh kubawa untuk dibaca?"
    call kk_family_menu("Mo06", ["Dukung ia mengambil tawaran itu.", "Halangi; ada yang tidak beres pada Kuga.", "Ikut menemaninya ke sesi itu."])
    if _return == "A":
        nar "Kau mendukungnya mengambil tawaran. Moeka tersenyum lega, menerima pendapatmu sebagai tanda bahwa kekhawatirannya mungkin hanya terlalu besar."
        moeka "Oke. Aku coba. Semoga nanti bisa cerita ini awal yang bagus, ya."
        nar "Bayaran yang dijanjikan terasa nyata. Bagian pekerjaan yang belum terjelaskan masih harus ia hadapi ketika kegembiraan awal sudah lewat."
    elif _return == "B":
        moeka "Kau merasa begitu juga? ...Mungkin aku terlalu butuh uang sampai mengabaikan firasat."
        nar "Kau menunjukkan bagian tawaran yang belum jelas. Moeka menahan kecewa karena penghasilan itu berarti banyak, lalu meminta Kuga waktu untuk memeriksa sebelum menjawab."
    else:
        "Kuga" "Oh, kau bawa teman. ...Tidak masalah. Untuk sekarang."
        nar "Moeka meminta kehadiran pendamping disebutkan sejak awal. Ketika nada Kuga berubah, ia melihat sendiri sesuatu yang tidak sesuai dengan keramahan tawaran tadi."
        moeka "Aku ingin bekerja dengan jelas. Temanku bukan masalah kalau pekerjaannya memang sesuai yang dibicarakan."
    return

# ┌─ PANDUAN CERITA · Mo08 · Natal Moeka dan Adik
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia pulang ke rumah.
# │ INTI    : A ikut / B kirim hadiah / C tidak.
# │ AKHIRAN : hub besar #3.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo08:
    call kk_scene_enter("moeka", "Kantin Pusat · Menjelang Natal")
    nar "Moeka membagi daftar belanja menjadi tiga kolom kecil, satu untuk setiap adik. Kolom bagi dirinya tidak ada. Ia memperlihatkan sebuah pita murah yang bisa dipakai berulang kali dengan wajah bangga seorang penemu."
    moeka "Aku pulang buat Natal. Mereka bilang nggak perlu apa-apa, jadi tentu saja aku malah makin ingin bawa sesuatu. Aku tahu. Logikaku sedang cuti."
    call kk_family_menu("Mo08", ["Ikut pulang bersamanya.", "Kirim hadiah untuk adik-adiknya.", "Tidak terlibat."])
    if _return == "A":
        moeka "Kau mau ikut? Rumahku sempit dan ramai, tapi... mereka pasti senang ada tamu."
        nar "Kau ikut sebagai tamu yang bersedia membantu, bukan penyelamat yang memeriksa kekurangan rumah. Moeka mulai menceritakan kebiasaan adik-adiknya dan memberi peringatan bahwa semua akan bertanya banyak hal sekaligus."
    elif _return == "B":
        moeka "Kau mengirim hadiah? Mereka akan mengira aku yang beli—biar kubilang dari siapa sebenarnya."
        nar "Ia meminta ukuran dan jenisnya dibicarakan lebih dahulu agar tak ada anak yang merasa dilupakan. Setelah memastikan itu, kegembiraannya keluar tanpa perlu dibesar-besarkan untuk membuktikan terima kasih."
    else:
        nar "Kau tidak terlibat. Moeka menyelesaikan belanja sendiri, membawa tas yang lebih berat daripada barang untuk beberapa hari seharusnya."
        nar "Dari rumah ia mengirim foto adik-adiknya tertawa. Ia tidak ikut masuk bingkai karena sedang memegang kamera dan memastikan seluruh hasil usahanya tampak bahagia."
    return

# ┌─ PANDUAN CERITA · Mo09 · Hatsumode: Doa Ayah
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia berdoa untuk ayah.
# │ INTI    : A temani / B tanya / C abaikan.
# │ AKHIRAN : Intimasi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo09:
    call kk_scene_enter("moeka", "Kuil · Hatsumode")
    nar "Antrean kuil sudah berganti orang ketika Moeka masih berdiri dengan telapak tangan rapat. Sesudah menunduk ia kembali memejamkan mata, seolah ada satu permintaan yang belum berani disebut sampai selesai."
    call kk_family_menu("Mo09", ["Temani ia berdoa dalam diam.", "Tanya apa yang ia doakan.", "Abaikan dan tunggu di luar."])
    if _return == "A":
        moeka "Kau menunggu sampai aku selesai? ...Aku berdoa supaya ayah bertahan sampai aku lulus."
        nar "Ia malu karena doanya terdengar seperti menawar waktu. Kau membiarkannya mengatakan takut tanpa menjanjikan hasil yang tak bisa diketahui siapa pun."
        moeka "Aku cuma ingin dia sempat melihat aku berhasil dalam sesuatu yang bukan bertahan hari ini."
    elif _return == "B":
        moeka "Untuk ayah. Selalu untuk ayah. ...Kadang aku lupa mendoakan diriku sendiri."
        nar "Kau menanyakan apa yang ingin diminta untuk dirinya. Moeka tertawa, kemudian tak punya jawaban. Baru di anak tangga terakhir ia mengatakan ingin satu hari ketika seluruh keluarganya bisa makan tanpa menghitung yang harus dikurangi besok."
    else:
        nar "Kau menunggu di luar tanpa membahas doanya. Moeka menyusul dengan mata sedikit merah, lalu menawarkan memotretmu di gerbang agar pembicaraan tidak berbalik ke wajahnya."
    return

# ┌─ PANDUAN CERITA · Mo10 · Coklat untuk Tiga Adik
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia membuat coklat untuk adik.
# │ INTI    : A bantu / B beri uang / C tak peduli.
# │ AKHIRAN : pemain mengenal adik-adik.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo10:
    call kk_scene_enter("moeka", "Kantin Pusat · Coklat untuk adik")
    nar "Tiga bungkus coklat diberi tanda berbeda agar mudah dikenali adik-adiknya. Moeka menghitung ulang bahan yang tersisa, lalu membagi hiasan dengan ketelitian yang jarang terlihat pada jadwal pribadinya."
    moeka "Kalau yang ini dapat bintang dan yang itu nggak, kami akan mengadakan perundingan damai di rumah. Jadi semuanya harus punya bintang."
    call kk_family_menu("Mo10", ["Bantu ia membuat dan membungkusnya.", "Beri ia uang untuk bahan.", "Tak peduli dengan urusan adiknya."])
    if _return == "A":
        moeka "Kau ikut membungkus? Adik-adikku akan bertanya siapa yang bantu. ...Akan kuceritakan tentangmu."
        nar "Kalian menempelkan hiasan sambil ia bercerita. Nama adik-adiknya berhenti menjadi daftar kebutuhan dan mulai menjadi orang-orang dengan humor, kesukaan, dan pertengkaran kecil yang sangat dikenalnya."
    elif _return == "B":
        moeka "Uang? ...Aku tidak enak. Tapi untuk mereka, akan kuterima. Terima kasih."
        nar "Kau menjelaskan bantuan itu tidak menuntut balasan. Moeka tetap mencatat jumlahnya, belum mudah menerima bahwa ada pemberian yang tidak akan berubah menjadi tagihan saat ia berkata tidak nanti."
    else:
        nar "Kau membiarkannya menyelesaikan sendiri. Moeka berhenti bercerita tentang adik-adik setelah sadar perhatianmu sudah berpindah. Tiga bungkus itu tetap rapi saat selesai; tidak ada yang menunjukkan berapa lama ia duduk di sana."
    return

# ┌─ PANDUAN CERITA · Mo11 · Hujan Deras: Ponsel Mati
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia hilang kontak.
# │ INTI    : A cari / B tunggu / C abaikan.
# │ AKHIRAN : jendela intervensi #1; stage 1 (beban menumpuk).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo11:
    call kk_scene_enter("moeka", "Kantin Pusat · Ponsel mati")
    nar "Panggilan ke Moeka tidak tersambung sejak pagi. Ia tak muncul pada kegiatan yang biasanya justru dimintanya agar dimulai tepat waktu. Di luar, hujan membuat semua rencana mencari terasa lebih sulit."
    nar "Pesan terakhirnya hanya mengatakan akan menyusul. Kalimat yang biasa tidak cukup menenangkan ketika kabar lain juga mulai hilang."
    call kk_family_menu("Mo11", ["Cari ia sampai ketemu.", "Tunggu sampai ia muncul sendiri.", "Abaikan."])
    if _return == "A":
        moeka "Kau mencariku? Di tengah hujan begini? ...Kenapa? Aku bukan siapa-siapa yang penting."
        nar "Ponselnya mati dan harinya berantakan oleh urusan rumah. Kau menemukannya basah, terlalu letih untuk menyiapkan cerita lucu tentang itu."
        nar "Kau mengatakan ketidakhadirannya diketahui. Untuk beberapa saat ia tidak percaya bahwa seseorang boleh mencarinya tanpa sedang membutuhkan sesuatu darinya."
    elif _return == "B":
        nar "Kau menunggu sampai ia menghubungi. Kabar baru datang keesokan hari, disertai tawa tentang ponsel yang tidak bisa diandalkan. Moeka tidak menyebut berapa lama ia bingung harus pulang ke mana lebih dahulu."
    else:
        nar "Kau menganggapnya urusan biasa yang tidak perlu ditanyakan. Moeka kembali dengan penjelasan pendek dan segera mengambil tugas tambahan agar orang berhenti membahas ketidakhadirannya."
        nar "Hari yang buruk berlalu tanpa seorang pun mengetahui seberapa buruk rasanya dari dalam. Ia menyimpan pelajaran bahwa menghilang sedikit pun tampaknya tidak banyak mengubah kehidupan orang lain."
    return

# ┌─ PANDUAN CERITA · Mo12 · IPK Turun
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : nilai turun.
# │ INTI    : A bantu belajar / B beri uang / C tidak peduli.
# │ AKHIRAN : beasiswa mulai terancam.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo12:
    call kk_scene_enter("moeka", "Kantin Pusat · IPK turun")
    nar "Moeka menatap nilai lebih lama daripada pesan keluarga tentang uang. Dua masalah itu tidak bisa lagi diletakkan di laci yang berbeda: bekerja lebih banyak menggerus kuliah, kuliah yang jatuh mengancam satu hal yang membuatnya mampu tetap bekerja untuk rumah."
    moeka "Aku selalu bilang tinggal atur jadwal. Sekarang jamnya sudah habis. Kalau beasiswa hilang, aku nggak punya cadangan yang bisa dibuat dari semangat saja."
    call kk_family_menu("Mo12", ["Bantu ia belajar.", "Beri ia uang untuk meringankan beban.", "Tidak peduli."])
    if _return == "A":
        moeka "Kau mau menemaniku belajar? ...Mungkin masih ada jalan kalau tidak sendirian."
        nar "Kalian memulai dari satu tugas yang paling dekat tenggat, bukan menuntut seluruh semester diperbaiki malam itu. Ia berhenti menyebut dirinya bodoh ketika akhirnya berhasil menjelaskan bagian yang tadi tak dipahami."
    elif _return == "B":
        moeka "Uang lagi? ...Aku mulai merasa berutang padamu lebih dari yang bisa kubalas."
        nar "Bantuan itu mengurangi kebutuhan bekerja untuk sementara. Kau mengatakan ia tidak harus menukar kedekatan demi menerimanya, tetapi ia perlu waktu sebelum benar-benar percaya bahwa penolakan di masa depan tidak akan membuat uang ini disebut kembali."
    else:
        nar "Kau tidak menanggapi lebih jauh. Moeka menutup layar nilai dan mulai membicarakan pekerjaan berikutnya, sesuatu yang masih tampak dapat menghasilkan uang sekarang."
        nar "Makin sedikit ruang tersisa untuk hal yang baru akan runtuh beberapa bulan lagi. Ia terus berlari di antara keduanya, sendirian."
    return

# ┌─ PANDUAN CERITA · Mo26 · Natal Sunyi
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia sendirian.
# │ INTI    : A datang / B kirim pesan / C tidak ada.
# │ AKHIRAN : jendela #5.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo26:
    call kk_scene_enter("moeka", "Kantin Pusat · Natal sunyi")
    nar "Moeka mengirim foto lampu Natal di luar jendelanya tanpa ikut muncul. Ketika kautanya apakah sedang di rumah, jawabannya datang terlambat: masih di kos, belum tahu nanti."
    nar "Di meja ada makanan yang belum dibuka dan ponsel yang terus diperiksa. Malam itu ia tidak punya tenaga untuk membuat kesendirian terdengar seperti pilihan yang seru."
    call kk_family_menu("Mo26", ["Datang menemaninya langsung.", "Kirim pesan agar ia tahu ada yang ingat.", "Tidak melakukan apa pun."])
    if _return == "A":
        moeka "Kau datang? Di malam seperti ini? ...Aku hampir percaya tidak ada yang akan datang."
        nar "Kau tidak meminta ia segera senang. Kalian membuka makanan, menghubungi orang yang perlu tahu keadaannya, dan membiarkan malam berlangsung tanpa pertunjukan bahwa semua sudah baik."
    elif _return == "B":
        moeka "Pesanmu masuk. ...Satu pesan. Kadang satu saja cukup untuk melewati satu malam."
        nar "Kau menanggapi dengan sungguh-sungguh dan menanyakan siapa yang bisa menemaninya jika malam terasa makin berat. Ia menyebut Rina setelah ragu. Kabar singkat itu tidak menyelesaikan masalahnya, tetapi membuka jalan agar ia tidak hanya menunggu satu orang."
    else:
        nar "Kau tidak menghubungi. Foto lampu itu tetap menjadi pesan terakhir dari Moeka malam tersebut. Di kos, ia menaruh ponsel menghadap bawah lalu membaliknya lagi beberapa menit kemudian."
        nar "Tidak ada satu malam yang sendirian menjelaskan seluruh krisis. Malam ini menambah sesuatu pada tumpukan yang belum berhasil dibagikannya kepada orang lain."
    return

init 1 python:
    _hook("Mo03-A", lambda: kk_rel("moeka","trust",-2))
    _hook("Mo03-B", lambda: (kk_rel("moeka","trust",4), kk_adj("stres_moeka",-5)))
    _hook("Mo03-C", lambda: (kk_rel("moeka","trust",5), kk_adj("stres_moeka",-8)))
    _hook("Mo04-A", lambda: (kk_rel("moeka","intim",6), kk_flag("moeka_rahasia_lapar")))
    _hook("Mo04-B", lambda: kk_rel("moeka","trust",4))
    _hook("Mo04-C", lambda: (kk_adj("stres_moeka",8), kk_rel("moeka","trust",-4)))
    _hook("Mo05-A", lambda: (kk_flag("moeka_keluarga_diketahui"), kk_rel("moeka","intim",4)))
    _hook("Mo05-B", lambda: kk_rel("moeka","trust",4))
    _hook("Mo05-C", lambda: (kk_flag("moeka_keluarga_diketahui"), kk_moeka_burden(5)))
    _hook("Mo06-A", lambda: (kk_flag("kuga_jerat_mulai"), kk_adj("stres_moeka",-10)))
    _hook("Mo06-B", lambda: (kk_rel("moeka","trust",5), kk_flag("kuga_dihalangi")))
    _hook("Mo06-C", lambda: kk_flag("kuga_ditemani"))
    _hook("Mo08-A", lambda: (kk_rel("moeka","intim",6), kk_flag("moeka_adik_dikenal")))
    _hook("Mo08-B", lambda: kk_rel("moeka","aff",4))
    _hook("Mo08-C", lambda: kk_moeka_burden(8))
    _hook("Mo09-A", lambda: (kk_rel("moeka","intim",5), kk_flag("moeka_ayah_diketahui")))
    _hook("Mo09-B", lambda: (kk_rel("moeka","trust",4), kk_flag("moeka_ayah_diketahui")))
    _hook("Mo09-C", lambda: kk_rel("moeka","trust",-3))
    _hook("Mo10-A", lambda: (kk_rel("moeka","intim",5), kk_flag("moeka_adik_dikenal")))
    _hook("Mo10-B", lambda: kk_adj("stres_moeka",-6))
    _hook("Mo10-C", lambda: kk_rel("moeka","aff",-3))
    _hook("Mo11-A", lambda: (kk_rel("moeka","trust",6), kk_flag("moeka_intervensi_1")))
    _hook("Mo11-B", lambda: (kk_moeka_stage(1), kk_moeka_burden(6)))
    _hook("Mo11-C", lambda: (kk_moeka_stage(1), kk_moeka_burden(12)))
    _hook("Mo12-A", lambda: (kk_rel("moeka","trust",5), kk_adj("stres_moeka",-8)))
    _hook("Mo12-B", lambda: kk_adj("stres_moeka",-5))
    _hook("Mo12-C", lambda: (kk_adj("stres_moeka",12), kk_flag("beasiswa_terancam")))
    _hook("Mo26-A", lambda: (kk_rel("moeka","intim",8), kk_flag("moeka_ditemani_natal"), kk_adj("stres_moeka",-15)))
    _hook("Mo26-B", lambda: (kk_rel("moeka","trust",5), kk_flag("moeka_dikabari_natal")))
    _hook("Mo26-C", lambda: (kk_adj("stres_moeka",15), kk_flag("moeka_natal_sendiri")))
