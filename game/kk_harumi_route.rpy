# Arc Harumi-Ogawa (H04, H06, H07, H11-H18): Harumi yang brilian tapi naif secara
# sosial perlahan dijerat advisor senior Ogawa (eksploitasi akademik/finansial).
# Ditulis sebagai KONSEKUENSI dan KARAKTER: cengkeraman Ogawa dan uang gelap hanya
# AKIBATNYA yang tampak; metode grooming/pemerasan TIDAK ditulis. Jalur protektif
# (lapor/bela/bersaksi) tersedia di tiap simpul. Penempatan Perpustakaan Pusat
# prototipe reachability. Speaker Ogawa/Ogiwara/Mizuhara pakai nama-penutur.

init 1 python:
    def kk_ogawa_grip(delta):
        pts.setdefault("cengkeraman_ogawa", 0)
        kk_adj("cengkeraman_ogawa", delta)
    def kk_harumi_validate(delta):
        pts.setdefault("validasi_pemain", 0)
        kk_adj("validasi_pemain", delta)
    def kk_harumi_stage(n):
        kk_stage("harumi", max(n, stage.get("harumi", 0)))

# ┌─ PANDUAN CERITA · H04 · Teh Malam di Vila
# │ LOKASI  : Kampus Kouseikan · Perpustakaan Pusat
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : ia menyendiri.
# │ INTI    : A temani / B ajak bicara / C tinggalkan.
# │ AKHIRAN : Intimasi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H04:
    call kk_scene_enter("harumi", "Perpustakaan Pusat · Teh malam")
    nar "Harumi membawa teh ke sudut vila yang paling jauh dari televisi. Catatan di lututnya tidak memuat rumus: ia mencoba mengingat percakapan siang tadi dan mengapa satu jawaban terasa menyenangkan sementara jawaban lain tidak."
    harumi "Aku punya perasaan tentangnya. Yang sulit adalah tahu namanya sebelum sudah lewat. Kalau aku diam, bukan berarti tidak ada apa-apa."
    call kk_family_menu("H04", ["Minum bersama dalam diam.", "Tanya apa yang ia catat.", "Ceritakan tentang dirimu."])
    if _return == "A":
        harumi "Kau tidak keberatan diam bersamaku? ...Variabel yang menyenangkan. Jarang ada."
        nar "Ia menutup catatan setelah kau duduk. Untuk beberapa menit, tidak semua keheningan harus diolah menjadi pertanyaan yang perlu dijawab."
        harumi "Aku tidak sedang bosan. Itu perlu kukatakan supaya kamu tidak pergi karena salah menyimpulkan."
    elif _return == "B":
        harumi "Aku mencatat kapan seseorang merasa nyaman. Untukmu, datanya... tidak biasa."
        nar "Kau bertanya apakah ia sudah menanyakan langsung kepada orangnya. Harumi menatap pena di tangan, lalu mengakui ia berharap pencatatan bisa menghindarkannya dari kemungkinan bertanya sesuatu yang memalukan."
        harumi "Mungkin aku bisa mulai dari sekarang. Kamu ingin duduk denganku, atau hanya mengambil teh? Keduanya boleh."
    else:
        harumi "Kau berbagi lebih dulu? Itu bukan transaksi. ...Aku perlu waktu memahami kenapa itu terasa hangat."
        nar "Ia mendengarkan ceritamu tanpa menyiapkan contoh yang sepadan untuk dibalas. Sesudahnya ia mengatakan ada bagian yang ingin dipikirkan lagi, lalu meminta izin bertanya lain kali."
    return

# ┌─ PANDUAN CERITA · H06 · Ogawa Masato Muncul
# │ LOKASI  : Kampus Kouseikan · Perpustakaan Pusat
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : senior lab menawarkan "bimbingan".
# │ INTI    : A dukung / B curiga / C peringatkan.
# │ AKHIRAN : ogawa_aktif.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H06:
    call kk_scene_enter("harumi", "Perpustakaan Pusat · Ogawa muncul")
    nar "Ogawa Masato datang ketika Harumi sedang membereskan referensi. Ia mengenal penelitiannya cukup baik untuk menyebut bagian yang paling sering luput dari pujian orang lain. Harumi menegakkan punggung, terkejut sekaligus senang."
    "Ogawa" "Kalau mau berkembang lebih cepat, kita bisa bicara di luar jadwal biasa. Bakat seperti ini perlu perhatian khusus."
    harumi "Saya perlu tahu bentuk bimbingannya. Saya belum bisa menyesuaikan semua jadwal."
    nar "Pertanyaannya jelas. Jawaban Ogawa jauh lebih sibuk membicarakan kepercayaan."
    call kk_family_menu("H06", ["Dukung; mungkin ini peluang baik.", "Curiga pada Ogawa.", "Peringatkan Harumi terang-terangan."])
    if _return == "A":
        nar "Kau mendukung kesempatan tersebut. Harumi menerima dukunganmu sebagai alasan tambahan untuk mengabaikan bagian tawaran yang belum terjelaskan."
        harumi "Baik. Saya akan mencoba. Nanti saya siapkan catatan yang diperlukan."
        nar "Ogawa memberi waktu pertemuan, lalu beranjak sebelum pertanyaan tentang batas bimbingan kembali muncul."
    elif _return == "B":
        nar "Kau menyebut jawaban yang belum diberikan, bukan menebak seluruh niatnya dari senyum. Harumi melihat tawaran itu lagi."
        harumi "Benar. Aku bertanya tentang pekerjaan, dia menjawab tentang kepercayaan. Aku bisa meminta penjelasan tanpa harus memutuskan sekarang apakah dia orang baik."
        nar "Ia menyimpan pesan Ogawa, kini sebagai sesuatu yang perlu diperiksa, bukan sekadar kehormatan yang harus diterima."
    else:
        nar "Kau memperingatkan agar ia tidak menerima syarat yang kabur demi pujian atau rekomendasi. Harumi mendengar, lalu memintamu menjelaskan bagian yang bisa ia nilai sendiri."
        harumi "Aku percaya kamu khawatir. Aku juga ingin belajar mengenali alasannya, supaya tidak hanya memindahkan seluruh keputusan dari dia kepadamu."
    return

# ┌─ PANDUAN CERITA · H07 · Natal di Laboratorium
# │ LOKASI  : Kampus Kouseikan · Perpustakaan Pusat
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : ia menghabiskan Natal di lab.
# │ INTI    : A datang / B kirim makanan / C abaikan.
# │ AKHIRAN : hub besar #3.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H07:
    call kk_scene_enter("harumi", "Perpustakaan Pusat · Natal di lab")
    nar "Ucapan selamat Natal Harumi disertai foto catatan pengamatan, bukan pohon atau makan malam. Ia punya pekerjaan di laboratorium dan telah menyusun jam agar tidak perlu memikirkan apakah ingin berada di tempat lain."
    harumi "Eksperimen tidak mengikuti hari libur. Aku masih di sini sampai nanti. Itu jawaban jadwalku. Jawaban tentang apakah ingin sendiri... belum kutanyakan ke diriku."
    call kk_family_menu("H07", ["Datang menemaninya di lab.", "Kirim makanan ke lab.", "Abaikan."])
    if _return == "A":
        harumi "Kau datang? Di hari ketika semua orang memilih tempat lain? ...Datanya menyimpang, dan aku senang."
        nar "Kau menunggu di area yang boleh dimasuki, tidak mengganggu pekerjaan yang harus diselesaikan. Saat jeda ia keluar dengan dua cangkir dan cerita yang ternyata tak seluruhnya tentang riset."
        harumi "Aku menyiapkan cangkir kedua setelah tahu kamu menuju sini. Rasanya berbeda dari menyiapkan karena mungkin ada orang."
    elif _return == "B":
        harumi "Makanan hangat di tengah malam begini... Terima kasih. Aku akan makan sebelum dingin."
        nar "Ia mengirim kabar setelah makan, menjelaskan bagian yang disukainya dengan ketelitian yang membuat ucapan terima kasih terasa sangat pribadi. Tidak lama kemudian ia mengingatkan agar kau juga makan."
    else:
        nar "Tidak ada kabar darimu. Harumi menyelesaikan jadwalnya, makan sesuatu yang tersisa, lalu mematikan lampu yang tidak lagi diperlukan."
        nar "Ia menyebut malam itu sesuai perkiraan dalam catatannya. Pada baris berikutnya ada satu kata yang ditulis lebih kecil, belum berani dijadikan kesimpulan: kecewa."
    return

# ┌─ PANDUAN CERITA · H11 · Beasiswa Luar Negeri Dibuka
# │ LOKASI  : Kampus Kouseikan · Perpustakaan Pusat
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : peluang sekaligus tekanan.
# │ INTI    : A dukung / B minta tetap / C manfaatkan.
# │ AKHIRAN : stage 2 (salah baca validasi).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H11:
    call kk_scene_enter("harumi", "Perpustakaan Pusat · Beasiswa luar negeri")
    nar "Persyaratan beasiswa tersebar di meja Harumi bersama salinan hasil riset. Ia sudah memeriksa dokumen, bahasa, dan tenggat. Satu bagian yang belum jelas justru datang dari orang yang menawarkan membuat semuanya lebih mudah."
    harumi "Ogawa mengatakan hanya dia yang bisa menjamin rekomendasiku. Di pengumuman tidak tertulis begitu. Aku merasa perlu berterima kasih dan takut pada saat yang sama."
    call kk_family_menu("H11", ["Dukung ia mengejar peluang itu sendiri.", "Minta ia tetap, tapi jujur soal alasanmu.", "Manfaatkan ketergantungannya padamu."])
    if _return == "A":
        harumi "Mengejarnya tanpa bergantung pada satu orang... ya. Aku akan coba jalur yang lebih bersih."
        nar "Kau membantunya memisahkan persyaratan resmi dari klaim pribadi. Harumi mencoret kata hanya dari catatannya sendiri."
        harumi "Aku masih bisa membutuhkan bantuan. Itu tidak sama dengan seseorang boleh menentukan seluruh syaratnya."
    elif _return == "B":
        harumi "Kau ingin aku tetap? ...Katakan itu sebagai dirimu, bukan sebagai saran. Maka aku akan mempertimbangkannya."
        nar "Ia menunggu alasan pribadimu selesai, tidak mengubahnya menjadi penilaian akademik. Keinginanmu kini ikut masuk dalam pertimbangannya, berat karena ia mulai sangat menghargai persetujuanmu."
    else:
        nar "Kau memanfaatkan keinginannya mendapat dukungan, membuat perhatianmu seolah bergantung pada pilihan yang menguntungkanmu. Harumi mencoba menyesuaikan rencana sebelum memeriksa apakah ia sungguh menginginkannya."
        harumi "Kalau begitu aku ubah yang ini. Setelah itu... kamu masih mau membantu, kan?"
    return

# ┌─ PANDUAN CERITA · H12 · Variabel Sosial
# │ LOKASI  : Kampus Kouseikan · Perpustakaan Pusat
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : ia mencoba "eksperimen" interaksi.
# │ INTI    : A hentikan / B ikut / C manfaatkan.
# │ AKHIRAN : stage 3–4 (eksperimen, transaksional awal).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H12:
    call kk_scene_enter("harumi", "Perpustakaan Pusat · Variabel sosial")
    nar "Harumi menunjukkan catatan tentang bantuan dan balasan. Hal yang semula dicatat untuk memahami hubungan kini berubah menjadi daftar harga yang harus dipenuhi sebelum ia berhak meminta perhatian."
    harumi "Ogawa bilang semua kedekatan punya pertukaran. Aku mencari sesuatu yang bisa kuberikan supaya tidak salah berharap. Tapi semakin jelas pertukarannya, semakin sedikit aku tahu apakah mereka ingin mengenalku."
    call kk_family_menu("H12", ["Hentikan sebelum ia percaya itu.", "Ikut dalam eksperimennya.", "Manfaatkan kerangka itu."])
    if _return == "A":
        harumi "Kau bilang kedekatan bukan transaksi? ...Itu bertentangan dengan yang Ogawa ajarkan. Aku perlu memikirkannya ulang."
        nar "Kau menanyakan apakah ia boleh menolak tanpa kehilangan seluruh rasa hormat. Harumi berhenti pada pertanyaan tersebut, lalu menyadari kolom penolakan tidak pernah dibuat dalam tabelnya."
        harumi "Aku menghapus pilihan itu sebelum mulai mengamati. Pantas hasilnya selalu mengarah ke hal yang sama."
    elif _return == "B":
        nar "Kau mengikuti kerangkanya dan membicarakan kedekatan sebagai pertukaran yang perlu diseimbangkan. Harumi tampak lega menemukan orang lain yang bersedia menyebutnya masuk akal."
        nar "Ia menambahkan kolom baru. Semakin rapi modelnya, semakin sulit baginya menerima perhatian yang tidak menuntut sesuatu untuk dibayar kembali."
    else:
        nar "Kau mengambil keuntungan dari aturan yang baru ia percayai. Harumi menyetujui sesuatu dengan kalimat yang terdengar seperti penyelesaian kewajiban, bukan keinginan."
        harumi "Kalau begitu sekarang sudah setara? Aku masih boleh datang ketika butuh bicara?"
        nar "Kau mendengar rasa takut di balik hitungannya dan tetap menerima hasil yang menguntungkanmu."
    return

# ┌─ PANDUAN CERITA · H13 · Dana Lab Dibekukan
# │ LOKASI  : Kampus Kouseikan · Perpustakaan Pusat
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : Ogawa menawarkan solusi.
# │ INTI    : A bantu mencari dana / B laporkan Ogawa / C diam / D manfaatkan.
# │ AKHIRAN : gerbang rute (stage 5).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H13:
    call kk_scene_enter("harumi", "Perpustakaan Pusat · Dana lab dibekukan")
    nar "Pemberitahuan pembekuan dana membuat Harumi membuka semua rencana kerjanya sekaligus. Ogawa sudah menawarkan jalan pribadi, dengan syarat yang tak tercantum pada satu pun dokumen penelitian."
    harumi "Aku ingin menolak. Lalu aku memikirkan semua yang akan berhenti jika dana itu tidak datang. Aku sedang mencoba tahu apakah takut membuatku melihat sesuatu sebagai satu-satunya jalan padahal bukan."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Bantu ia cari dana yang bersih.", "Laporkan Ogawa ke pihak yang berwenang.", "Diam saja.", "Manfaatkan situasi untuk kepentinganmu."])]
    call screen kk_choice_panel(_rows, "Pilihan Harumi")
    $ kk_record_choice("H13", _return)
    if _return == "A":
        harumi "Jalur pendanaan resmi, hibah mahasiswa... akan kucoba. Lebih lambat, tapi tidak mengikatku pada siapa pun."
        nar "Kalian membuat daftar bantuan yang dapat ditanyakan secara terbuka. Ia harus menyesuaikan target penelitian dan menerima kemungkinan terlambat, tetapi tak lagi harus menerima satu tawaran hanya karena datang pada saat paling menakutkan."
    elif _return == "B":
        harumi "Melaporkannya? ...Aku takut, tapi kalau kau bersamaku, aku akan bersaksi apa yang kulihat."
        nar "Kau menawarkan mendampingi, membiarkan Harumi menentukan bagian yang hendak disampaikan. Ia mengumpulkan pesan dan dokumen yang memang dimilikinya, tidak lagi menganggap rasa tidak nyaman sebagai sesuatu yang harus dibuktikan lewat pengorbanan baru."
    elif _return == "C":
        nar "Kau diam. Harumi kembali memeriksa angka, mencoba membuat harga tawaran itu tampak lebih kecil dibanding kehilangan yang ditakutinya."
        harumi "Aku bisa menjalaninya sementara. Sampai risetnya aman."
        nar "Keputusan itu memberinya dana dan mengambil lebih banyak ruang hidup daripada yang dapat diakui dalam laporan. Sementara tidak memiliki tanggal berakhir yang jelas."
    else:
        nar "Kau membiarkan tekanan dana memberi jalan bagi kepentinganmu sendiri. Harumi menerima bantuan yang membawa syarat lain, seolah setiap pintu yang tersedia harus dibuka dengan menyerahkan bagian dirinya."
        nar "Pekerjaan mungkin bergerak kembali. Itu tidak membuat pilihan yang dibatasi ketakutan menjadi persetujuan bebas terhadap semua yang ingin kauambil darinya."
    return

# ┌─ PANDUAN CERITA · H14 · Natal: Undangan Diskusi
# │ LOKASI  : Kampus Kouseikan · Perpustakaan Pusat
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : Ogawa mengundang.
# │ INTI    : A larang / B temani / C biarkan.
# │ AKHIRAN : stage 6.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H14:
    call kk_scene_enter("harumi", "Perpustakaan Pusat · Undangan diskusi")
    nar "Undangan Ogawa tidak menyebut agenda, hanya malam Natal dan permintaan agar Harumi datang sendiri. Ia membandingkannya dengan jadwal akademik yang sudah kosong pada jam itu."
    harumi "Aku tidak ingin pergi. Bagian itu sudah jelas sekarang. Yang belum jelas adalah kenapa aku merasa tidak boleh memakai alasan tersebut."
    call kk_family_menu("H14", ["Larang ia pergi sendiri.", "Temani ia ke pertemuan itu.", "Biarkan ia pergi sendiri."])
    if _return == "A":
        harumi "Kau melarangku keras sekali. ...Baik. Aku percaya reaksimu lebih dari ketidakmampuanku membaca ini."
        nar "Ia membatalkan kehadiran malam itu. Setelahnya ia meminta kalian membicarakan bagaimana ia dapat mempertahankan keputusan serupa tanpa harus menunggu seseorang melarang."
        harumi "Aku ingin bisa mengatakan tidak atas namaku sendiri juga."
    elif _return == "B":
        harumi "Kau ikut? Maka itu bukan lagi berdua. ...Entah kenapa aku bisa bernapas lebih lega."
        nar "Ketika rencana pendampingan disampaikan, sambutan Ogawa berubah. Harumi memperhatikan perubahan itu, kini punya sesuatu yang nyata untuk dibandingkan dengan klaim bahwa pertemuan tersebut hanya urusan riset."
    else:
        nar "Ia pergi sendiri meski tadi sudah mengatakan tidak ingin. Sesudah pertemuan ia kembali dengan jawaban yang lebih pendek dan rencana yang semakin banyak menyebut persetujuan Ogawa."
        harumi "Sudah selesai. Aku belum ingin membicarakannya."
        nar "Undangan berikutnya tidak lagi terasa seperti sesuatu yang dapat ditolak. Malam itu bertambah panjang di dalam kebiasaan yang dibawanya pulang."
    return

# ┌─ PANDUAN CERITA · H15 · Uang yang Tidak Jelas
# │ LOKASI  : Kampus Kouseikan · Perpustakaan Pusat
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : saldo bertambah.
# │ INTI    : A tanya langsung / B selidiki / C abaikan.
# │ AKHIRAN : Ogiwara curiga.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H15:
    call kk_scene_enter("harumi", "Perpustakaan Pusat · Uang tidak jelas")
    nar "Harumi memeriksa uang masuk yang tidak tercantum dalam pendanaan resmi. Pesan Ogawa menyebut jangan terlalu banyak berpikir. Justru kalimat itu membuatnya terus membuka percakapan yang sama."
    harumi "Aku tidak meminta ini. Tapi sekarang dia bicara seolah aku sudah menerima sesuatu darinya. Aku ingin tahu kapan diam mulai dianggap sebagai perjanjian."
    call kk_family_menu("H15", ["Minta ia tanya langsung asal uang itu.", "Selidiki diam-diam asal dana itu.", "Abaikan."])
    if _return == "A":
        harumi "Menanyakannya langsung? ...Ya. Lebih baik tahu bentuk ikatannya daripada pura-pura tidak ada."
        nar "Ia meminta keterangan yang jelas tanpa menambahkan ucapan terima kasih untuk sesuatu yang belum dipahami. Menunggu balasan membuatnya gelisah, tetapi kali ini pertanyaannya tetap ia biarkan terkirim."
    elif _return == "B":
        nar "Kau membantu memeriksa keterangan yang tersedia tanpa menyebarkannya menjadi gosip. Ogiwara mulai melihat hubungan antara perubahan Harumi dan pertemuan yang semakin sering mengambil waktunya."
        "Ogiwara" "Saya tidak ingin menuduh dari angka saja. Saya ingin memastikan dia punya tempat untuk mengatakan kalau ada yang tidak beres."
    else:
        nar "Kau membiarkannya. Harumi menyimpan sebagian dana tanpa membelanjakan, seolah tidak menyentuhnya cukup untuk menahan seluruh akibat."
        nar "Namun setiap pesan Ogawa kini membawa sesuatu yang tidak disebut terang-terangan: ingatan bahwa uang telah diterima. Kegelisahan yang tidak dibicarakan semakin mudah ia tafsirkan sebagai utang."
    return

# ┌─ PANDUAN CERITA · H16 · Valentine: Data Lain
# │ LOKASI  : Kampus Kouseikan · Perpustakaan Pusat
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : ia membawa hadiah dari orang lain.
# │ INTI    : A terima / B tegur / C manfaatkan.
# │ AKHIRAN : Hub #8.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H16:
    call kk_scene_enter("harumi", "Perpustakaan Pusat · Valentine, data lain")
    nar "Hadiah Ogawa tersimpan dalam kotak yang terlalu mahal untuk dibawa santai. Harumi meletakkannya di antara kalian seolah meminta benda itu ikut menjelaskan dirinya."
    harumi "Dia menyebut apresiasi. Aku ingin menerimanya sebagai itu saja. Tapi setiap kali aku mencoba menolak permintaan berikutnya, kotak ini seperti ikut berada dalam percakapan."
    call kk_family_menu("H16", ["Terima kenyataannya dan bicarakan jujur.", "Tegur ia soal menerima itu.", "Manfaatkan kecemburuan sebagai alat."])
    if _return == "A":
        harumi "Kau tidak marah, tapi ingin aku mengerti bentuknya. ...Baik. Akan kutimbang ulang apa arti hadiah ini."
        nar "Kalian membicarakan haknya menolak tanpa menjadikan hadiah sebagai tagihan. Harumi menutup kotak dengan lebih pasti, mulai membedakan rasa senang diperhatikan dari ketakutan terhadap syarat yang menyusul."
    elif _return == "B":
        harumi "Kau menegurku. ...Mungkin aku memang keliru membaca 'apresiasi' yang punya pamrih."
        nar "Ia menarik kotak menjauh, malu karena percakapan kembali terasa seperti pemeriksaan keputusan yang salah. Pengaruh Ogawa sedikit berkurang, tetapi kedekatan kalian ikut kehilangan kehangatan yang semula ingin ia cari."
    else:
        nar "Kau mengubah hadiah tersebut menjadi alasan menuntut bukti bahwa dirimu lebih penting. Harumi mencoba mencari balasan yang cukup untuk menghapus kecemburuanmu."
        harumi "Kalau aku lakukan itu, kamu tidak lagi menganggap aku memilih dia?"
        nar "Ia kembali diminta membayar kedekatan, kali ini oleh orang yang dapat melihat betapa mudahnya ia terjebak di dalam pertanyaan itu."
    return

# ┌─ PANDUAN CERITA · H17 · Ogiwara Menegur
# │ LOKASI  : Kampus Kouseikan · Perpustakaan Pusat
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : pengelola asrama memanggil.
# │ INTI    : A dukung teguran / B bela Harumi / C tutupi.
# │ AKHIRAN : titik tanpa balik tanpa Mizuhara/Ogiwara.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H17:
    call kk_scene_enter("harumi", "Perpustakaan Pusat · Ogiwara menegur")
    nar "Ogiwara mengundang kalian bicara di ruang pengelola asrama. Ia menutup pintu dari kebisingan koridor, lalu menjelaskan bahwa Harumi boleh meminta pendamping lain atau menghentikan pembicaraan sementara."
    "Ogiwara" "Ada perubahan yang membuat saya khawatir. Saya tidak ingin menganggapnya pelanggaran sebelum tahu apakah ada orang yang sedang menekanmu. Uang dan pertemuan itu perlu dijelaskan dengan aman."
    harumi "Saya takut kalau bicara, semuanya dianggap pilihan saya sendiri lalu selesai."
    call kk_family_menu("H17", ["Dukung teguran Ogiwara.", "Bela Harumi dan jelaskan keadaannya.", "Tutupi keadaan sebenarnya."])
    if _return == "A":
        "Ogiwara" "Terima kasih. Dengan kesaksianmu, kita bisa menghentikan ini lewat jalur yang benar."
        nar "Kau mendukung perlunya keadaan itu ditangani. Harumi sempat menunduk seperti sedang dimarahi, lalu Ogiwara mengingatkan bahwa meminta penjelasan tidak berarti menjadikannya pihak yang harus menanggung semuanya."
    elif _return == "B":
        "Ogiwara" "Kau membelanya tanpa menutupi faktanya. Itu yang kuperlukan—melindunginya, bukan Ogawa."
        nar "Harumi mulai menjelaskan satu pertemuan, lalu berhenti untuk menanyakan siapa yang akan mendengar keterangannya. Kali ini pertanyaan tentang kendali atas ceritanya sendiri diberi jawaban, bukan dianggap penghambat."
    else:
        nar "Kau menutupi keadaan dan memberi penjelasan yang membuat semua perubahan terdengar biasa. Harumi melihatmu menjawab lebih lancar daripada dirinya sendiri."
        harumi "Kalau begitu... memang tidak ada yang perlu dibicarakan?"
        nar "Pintu bantuan yang sempat terbuka menjadi lebih sempit. Ogiwara tetap khawatir, tetapi kini harus menembus kisah yang kaubangun bersama keengganan Harumi menganggap dirinya layak ditolong."
    return

# ┌─ PANDUAN CERITA · H18 · Mizuhara Memanggil
# │ LOKASI  : Kampus Kouseikan · Perpustakaan Pusat
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : rapat tertutup.
# │ INTI    : A bersaksi / B menutup / C menantang.
# │ AKHIRAN : jalur hukum akademik.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H18:
    call kk_scene_enter("harumi", "Perpustakaan Pusat · Mizuhara memanggil")
    nar "Mizuhara menjelaskan tujuan pertemuan sebelum menanyakan satu pun peristiwa. Catatan diperiksa, siapa yang akan mengakses keterangan disebutkan, dan Harumi diberi kesempatan meminta jeda."
    "Mizuhara" "Yang kami perlukan adalah yang Anda ketahui. Tidak perlu membuat cerita terasa lengkap dengan dugaan. Kami sedang memeriksa tindakan Ogawa dan tanggung jawab lingkungan akademik atasnya."
    nar "Harumi meletakkan kedua tangan di meja, berusaha berhenti menyembunyikan gemetarnya."
    call kk_family_menu("H18", ["Bersaksi apa yang kau lihat.", "Menutup dan tidak bersaksi.", "Menantang kewenangan rapat itu."])
    if _return == "A":
        "Mizuhara" "Kesaksian Anda tercatat. Proses akademik akan berjalan, dan Kujo-san akan dilindungi selama itu."
        nar "Kau menyampaikan yang dilihat dan didengar, mengoreksi bagian yang ternyata hanya kausimpulkan. Harumi menatapmu saat kau mengakui keterbatasan ingatan tanpa menjadikannya alasan membatalkan seluruh cerita."
        harumi "Aku juga mau menambahkan. Ada hal yang belum pernah kukatakan karena kukira sudah terlambat untuk menjelaskan."
    elif _return == "B":
        nar "Kau memilih tidak bersaksi. Pertanyaan itu ditutup setelah cukup jelas tak ada keterangan tambahan yang bersedia kauberikan."
        nar "Harumi merapikan halaman yang semula hendak ditunjukkannya dengan dukunganmu. Yang belum cukup untuk melindunginya tetap belum cukup, sementara Ogawa masih punya ruang untuk melanjutkan versi yang paling menguntungkan dirinya."
    else:
        "Mizuhara" "Anda menantang prosedur ini? ...Saya catat keberatan Anda. Tapi fakta tetap akan diperiksa."
        nar "Kau menghabiskan waktu mempertanyakan kewenangan pertemuan. Harumi menatap jam, lalu meminta kesempatan bicara sebelum namanya kembali tenggelam dalam pertarungan orang-orang yang mengaku sedang membahas kepentingannya."
    return

init 1 python:
    _hook("H04-A", lambda: kk_rel("harumi","intim",4))
    _hook("H04-B", lambda: (kk_rel("harumi","trust",4), kk_adj("kejelasan_harumi",5)))
    _hook("H04-C", lambda: (kk_rel("harumi","intim",5), kk_harumi_validate(5)))
    _hook("H06-A", lambda: (kk_flag("ogawa_aktif"), kk_ogawa_grip(10)))
    _hook("H06-B", lambda: (kk_flag("ogawa_aktif"), kk_rel("harumi","trust",5)))
    _hook("H06-C", lambda: (kk_flag("ogawa_aktif"), kk_ogawa_grip(-8), kk_flag("harumi_diperingatkan")))
    _hook("H07-A", lambda: (kk_rel("harumi","intim",6), kk_adj("kejelasan_harumi",5)))
    _hook("H07-B", lambda: kk_rel("harumi","trust",4))
    _hook("H07-C", lambda: kk_rel("harumi","aff",-3))
    _hook("H11-A", lambda: (kk_rel("harumi","trust",5), kk_ogawa_grip(-6)))
    _hook("H11-B", lambda: (kk_harumi_validate(6), kk_harumi_stage(2)))
    _hook("H11-C", lambda: (kk_harumi_stage(2), kk_flag("harumi_dimanfaatkan")))
    _hook("H12-A", lambda: (kk_adj("kejelasan_harumi",8), kk_flag("harumi_eksperimen_dihentikan")))
    _hook("H12-B", lambda: kk_harumi_stage(3))
    _hook("H12-C", lambda: (kk_harumi_stage(4), kk_flag("harumi_dimanfaatkan")))
    _hook("H13-A", lambda: (kk_ogawa_grip(-10), kk_flag("harumi_dana_bersih")))
    _hook("H13-B", lambda: (kk_flag("ogawa_dilaporkan"), kk_rel("harumi","trust",6)))
    _hook("H13-C", lambda: (kk_ogawa_grip(15), kk_harumi_stage(5)))
    _hook("H13-D", lambda: (kk_ogawa_grip(10), kk_harumi_stage(5), kk_flag("harumi_dimanfaatkan")))
    _hook("H14-A", lambda: (kk_ogawa_grip(-12), kk_flag("harumi_dilarang_sendiri")))
    _hook("H14-B", lambda: (kk_rel("harumi","intim",6), kk_ogawa_grip(-8)))
    _hook("H14-C", lambda: (kk_ogawa_grip(18), kk_harumi_stage(6)))
    _hook("H15-A", lambda: (kk_rel("harumi","trust",5), kk_flag("uang_ogawa_ditanya")))
    _hook("H15-B", lambda: (kk_flag("ogiwara_curiga"), kk_flag("uang_ogawa_diselidiki")))
    _hook("H15-C", lambda: (kk_ogawa_grip(10), kk_flag("uang_ogawa_diabaikan")))
    _hook("H16-A", lambda: (kk_rel("harumi","trust",4), kk_adj("kejelasan_harumi",5)))
    _hook("H16-B", lambda: (kk_rel("harumi","aff",-2), kk_ogawa_grip(-5)))
    _hook("H16-C", lambda: kk_flag("harumi_dimanfaatkan"))
    _hook("H17-A", lambda: (kk_flag("ogiwara_sekutu"), kk_ogawa_grip(-12)))
    _hook("H17-B", lambda: (kk_flag("ogiwara_sekutu"), kk_rel("harumi","trust",6), kk_ogawa_grip(-10)))
    _hook("H17-C", lambda: (kk_ogawa_grip(15), kk_flag("harumi_titik_tanpa_balik")))
    _hook("H18-A", lambda: (kk_flag("ogawa_dihentikan"), kk_ogawa_grip(-30), kk_rel("harumi","trust",8)))
    _hook("H18-B", lambda: (kk_ogawa_grip(12), kk_flag("ogawa_lolos")))
    _hook("H18-C", lambda: kk_flag("mizuhara_ditantang"))
