# Koita Tahun 3 (K18, K19, K23, K24, K25). Tagihan: ia harus memilih.
# Gerbang rute BL (Male) dan Koita Success (Female) di K17/K22 TIDAK dibangun di sini.
# Efek mengikuti Event_Koita; angka adalah setelan prototipe.
# ┌─ PANDUAN CERITA · K18 · Daftar Orang yang Kupilih
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : Koita menulis daftar nama.
# │ INTI    : A baca / B hapus satu nama / C tambahkan namamu.
# │ AKHIRAN : mengubah target ending Koita.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K18:
    call kk_scene_enter("koita", "Gedung Sastra")
    nar "Buku catatan Koita terbuka pada halaman yang tidak menyerupai draf. Nama-nama tersusun di kiri, lalu potongan kalimat di kanan: perlu bicara, belum tahu, jangan lewat pesan."
    koita "Sebentar. Ini bukan buat klub."
    nar "Ia menutup buku, tetapi dipanggil seorang dosen sebelum sempat memasukkannya ke tas. Buku itu tertinggal di meja dengan pena sebagai pembatas."
    call kk_family_menu("K18", ["Curi baca daftar itu diam-diam.", "Hapus satu nama saat ia lengah.", "Tuliskan namamu di daftar itu."])
    if _return == "A":
        nar "Kau membuka halaman tersebut. Ada nama yang dilingkari, ada yang dicoret, tetapi keterangannya tidak membentuk peringkat sesederhana yang kaubayangkan. Di samping satu nama tertulis: minta maaf tanpa minta kembali."
        nar "Kau mengingat semuanya, lalu mengembalikan pena ke tempatnya. Koita kembali tanpa sadar ada orang lain yang kini mengetahui peta percakapan yang belum berani ia mulai."
    elif _return == "B":
        nar "Kau menghapus satu nama saat ia tidak melihat. Bekas tulisannya tetap samar pada kertas, tetapi baris yang semula penuh kini tampak kosong."
        koita "Aku tadi menulis apa di sini?"
        nar "Ia bertanya kepada dirinya sendiri ketika kembali. Ia memeriksa halaman sebelum dan sesudahnya, lalu menatap pena."
        nar "Orang yang namanya kauhapus tetap ada di luar buku. Yang baru kaurusak adalah keyakinan Koita bahwa catatannya sendiri bisa dipercaya."
    else:
        nar "Kau menuliskan namamu pada baris terakhir dan membiarkan buku itu terbuka. Koita membaca tambahan tersebut, lalu menatapmu."
        koita "Kamu bahkan nggak tanya ini daftar apa."
        nar "Kau mengatakan namamu perlu ada dalam percakapan yang akan ia selesaikan. Ia menutup buku perlahan."
        koita "Iya. Tentang kita juga ada yang harus kubicarakan. Aku nggak akan pura-pura nggak melihatnya."
    return

# ┌─ PANDUAN CERITA · K19 · Skripsi: Tokoh yang Tidak Memilih
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : A bantu / B beri masukan jujur / C sabotase
# │ AKHIRAN : A/B membuat Koita menulis lebih jujur (trust naik); C merusak
# │           kepercayaannya (trust turun, fear naik).
# │ KOREKSI : urutan B/C di katalog asli tertukar dibanding implementasi —
# │           kode & hook sudah benar memakai urutan B=jujur/C=sabotase di atas.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K19:
    call kk_scene_enter("koita", "Gedung Sastra")
    nar "Judul sementara skripsi Koita lebih panjang daripada satu baris. Subjeknya jauh lebih sederhana: tokoh yang terus menunda keputusan dan membuat cerita bergerak di tempat."
    koita "Dosen pembimbing bilang argumenku terlalu melindungi tokohnya. Aku bilang itu usaha memahami. Beliau tanya kenapa yang lain nggak kupahami juga."
    nar "Ia menggeser draf kepadamu. Bagian yang banyak ditandai justru bagian yang paling lancar ia tulis."
    koita "Aku bisa ganti topik. Tapi kalau alasannya cuma karena ini terlalu dekat... aku akan tahu sendiri."
    call kk_family_menu("K19", ["Bantu ia menyusun argumennya.", "Beri masukan jujur meski pahit.", "Diam-diam rusak arah tulisannya."])
    if _return == "A":
        nar "Kau membantunya memisahkan niat tokoh, tindakannya, dan akibat terhadap orang lain. Koita mulai menemukan bahwa ketiganya tidak harus menghasilkan penilaian yang sama."
        koita "Dia bisa takut ditinggal dan tetap bertanggung jawab atas caranya menahan orang. Aku selalu menulis seolah harus pilih salah satu."
        nar "Kalian menandai bagian yang perlu dikerjakan ulang. Malam itu tugasnya bertambah, tetapi untuk pertama kalinya ia tahu apa yang harus dilakukan selain membela paragraf lama."
    elif _return == "B":
        nar "Kau mengatakan draf itu memperlakukan ketidaktegasan tokohnya sebagai penderitaan paling besar, sementara orang yang menunggu hanya disebut sebagai sumber tekanan. Koita memandang halaman yang kaumaksud."
        koita "Aku marah waktu dengar tadi. Berarti kamu menyentuh bagian yang memang sedang kusembunyikan."
        nar "Ia meminta contoh kedua, kemudian ketiga. Tidak semuanya langsung ia setujui, tetapi ia menulis catatan tanpa memintamu memperhalusnya."
        koita "Aku akan perbaiki argumennya. Bukan cuma mengganti kata yang kedengaran egois."
    else:
        nar "Kau memberinya arahan yang justru menjauhkan tulisan dari pertanyaan utamanya. Koita mengikuti karena mengira kau bersedia membantu pada bagian yang paling sulit ia lihat sendiri."
        nar "Semakin ia merevisi, semakin rapuh hubungan antara bukti dan kesimpulannya. Ketika ia bertanya mengapa naskahnya terasa makin asing, kau masih bisa menyebutnya bagian dari proses."
        koita "Aku tadi paham apa yang mau kutulis. Sekarang bahkan kalimat pembukanya terasa bohong."
        nar "Ia menutup laptop lebih awal. Keraguan yang kausisipkan ikut pulang bersamanya."
    return

# ┌─ PANDUAN CERITA · K23 · Tawaran dari Penerbit
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : A dukung ia pergi / B minta tinggal / C ikut.
# │ AKHIRAN : arah karier Koita.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K23:
    call kk_scene_enter("koita", "Gedung Sastra")
    nar "Koita mencetak surel penerbit meskipun sudah membacanya berkali-kali di ponsel. Tanggal mulai magang diberi garis, alamat kota lain dilingkari."
    koita "Pekerjaannya mungkin lebih banyak urus naskah orang. Gajinya juga nggak besar. Tapi mereka betulan menawarkan. Bukan cuma bilang kapan-kapan kirim tulisan."
    nar "Ia menatap kertas itu dengan gembira yang belum berani ia pertahankan."
    koita "Aku harus menjawab. Sebagian diriku ingin pergi. Sebagian lagi langsung menghitung siapa yang akan berhenti menghubungiku kalau aku jauh."
    call kk_family_menu("K23", ["Dukung ia mengambil kesempatan itu.", "Minta ia tetap tinggal.", "Tawarkan ikut bersamanya."])
    if _return == "A":
        nar "Kau mendukung keinginannya mencoba, lalu membicarakan biaya, tempat tinggal, dan pekerjaan yang sungguh ditawarkan. Koita tampak lebih tenang ketika mimpinya boleh dibahas sebagai urusan nyata."
        koita "Jadi aku boleh pergi tanpa berarti aku membuang semua yang di sini."
        nar "Ia membuka halaman untuk membalas surel."
        koita "Kalau nanti sepi, itu bukan otomatis tanda aku salah, ya. Aku harus memberi diriku waktu."
    elif _return == "B":
        nar "Kau memintanya tinggal. Wajah Koita langsung mencari sesuatu yang bisa disebut alasan cukup kuat."
        koita "Kalau aku tetap di sini, kamu ingin apa yang berubah?"
        nar "Pertanyaan itu menggantung. Ia ingin diyakinkan bahwa melewatkan kesempatan akan dibalas dengan kedekatan yang lebih pasti, tetapi belum berani memintanya terus terang."
        nar "Surel itu ia lipat kembali. Untuk sementara, ia menunda jawaban kepada penerbit demi menunggu jawaban darimu."
    else:
        nar "Kau menawarkan ikut. Koita tertawa kaget, lalu berhenti ketika menyadari kau sungguh membicarakan kemungkinan itu."
        koita "Kita harus hitung semuanya. Tempat tinggal, kerjaanmu juga. Aku nggak mau bilang iya cuma karena senang nggak harus sendirian."
        nar "Ia mengambil kertas kosong. Di bagian atas ia menulis dua nama, lalu membuat dua kolom kebutuhan yang tidak selalu sama."
        koita "Boleh kita mulai dari rencana, bukan janji dulu? Aku ingin ini masuk akal untukmu juga."
    return

# ┌─ PANDUAN CERITA · K24 · Pidato Klub
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : A hadir / B absen / C mengganggu.
# │ AKHIRAN : publik melihat siapa dekat dengan siapa.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K24:
    call kk_scene_enter("koita", "Gedung Sastra")
    nar "Kursi acara perpisahan klub disusun oleh mahasiswa baru yang belum hafal nama angkatan Koita. Di podium kecil, mikrofon mengeluarkan dengung setiap kali disentuh."
    koita "Aku mendapat bagian bicara terakhir. Kalau aku lupa berhenti, jangan tepuk tangan dulu. Nanti kukira masih menarik."
    nar "Ia mencoba bercanda, lalu menanyakan dengan lebih pelan apakah kau akan hadir. Tidak menyisipkan alasan bahwa semua orang pasti datang."
    call kk_family_menu("K24", ["Hadir dan dengarkan pidatonya.", "Lewatkan acaranya.", "Ganggu jalannya pidato."])
    if _return == "A":
        nar "Kau duduk di antara anggota lain. Koita melihatmu sebelum mulai, lalu memaksa dirinya membagikan pandangan ke seluruh ruangan."
        koita "Aku banyak belajar di sini. Sebagian karena dibantu, sebagian karena akhirnya ada yang mau bilang tulisanku belum jujur."
        nar "Ia beberapa kali kehilangan tempat membaca, tetapi menyelesaikannya. Seusai acara ia menghampirimu tanpa menunggu dipanggil."
        koita "Makasih sudah mendengar. Aku sadar kamu ada di sana. Aku juga berusaha sadar yang lain ada."
    elif _return == "B":
        nar "Kau tidak menghadiri acaranya. Belakangan sebuah foto dikirim ke grup: Koita di podium, satu kursi kosong di baris yang semula kautahu disiapkan untukmu."
        nar "Pidato tetap selesai. Anggota baru bertepuk tangan, panitia membagikan makanan, dan orang-orang membawa pulang kenangan yang tidak membutuhkan kehadiranmu untuk terjadi."
        nar "Koita hanya mengirim satu pesan pendek bahwa acaranya sudah lewat. Ia tidak bertanya kenapa kau tidak datang."
    else:
        nar "Kau memotong pidatonya ketika ruangan sedang hening. Beberapa orang menoleh, bingung apakah itu bagian dari acara. Koita kehilangan baris yang hendak dibaca."
        "Matsuda" "Biarkan dia selesai. Kalau ada urusan, bicarakan sesudahnya."
        nar "Koita mencoba melanjutkan, tetapi tangannya cukup gemetar hingga kertas di mikrofon terdengar berisik. Acara tidak lagi bisa kembali seperti semula."
        nar "Di luar ruangan, orang-orang membicarakan kedekatan kalian dalam bentuk yang berbeda dari yang kauinginkan: siapa yang memberi seseorang hak mempermalukan orang lain di hari perpisahannya?"
    return

# ┌─ PANDUAN CERITA · K25 · Natal Sendirian
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : A datang / B kirim orang lain / C biarkan.
# │ AKHIRAN : ending Koita "Sendiri" jika tak ada yang datang.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K25:
    call kk_scene_enter("koita", "Rumah Amamiya · Natal")
    nar "Pesan Koita datang setelah toko kue dekat stasiun mulai menurunkan harga. Foto ruang keluarganya memperlihatkan televisi menyala dan meja yang hanya punya satu piring."
    koita "Aku di rumah. Tadi hampir beli kue besar karena kebiasaan. Untung kasirnya tanya untuk berapa orang."
    nar "Ia menyusulkan pesan bahwa kau tidak perlu membatalkan rencana. Setelah itu tidak ada lagi tulisan yang muncul."
    call kk_family_menu("K25", ["Datang dan temani ia malam ini.", "Kirim orang lain untuk menemaninya.", "Biarkan ia sendirian malam itu."])
    if _return == "A":
        nar "Koita membuka pintu sebelum kau sempat menekan bel kedua kali. Ia sudah memakai sandal, seolah tadi masih mempertimbangkan pergi ke mana saja."
        koita "Kamu betulan datang. Aku nggak tahu harus menyiapkan apa."
        nar "Kau mengatakan tidak perlu menjadikan malam ini acara besar. Kalian menghangatkan makanan yang ada dan menonton bagian akhir film yang tak seorang pun melihat awalnya."
        koita "Aku senang. Boleh aku bilang senang tanpa langsung merasa harus membuatmu senang juga?"
        nar "Malam itu cukup panjang untuk membiarkan pertanyaan tersebut mendapat jawaban."
    elif _return == "B":
        nar "Kau menghubungi seseorang yang bersedia menemani, lalu memberi tahu Koita siapa yang akan datang. Ia membaca pesanmu lebih lama daripada biasanya."
        koita "Baik. Makasih sudah menghubungi. Aku siapkan piring lagi."
        nar "Tamu itu datang dengan rencananya sendiri yang sudah disisihkan. Koita sempat melihat ke pintu setelah menyambutnya, lalu sadar orang di hadapannya layak mendapat perhatian yang utuh."
        nar "Ia mematikan ponsel dan bertanya tentang perjalanan tamunya. Malam itu bukan malam yang ia bayangkan, tetapi tidak harus menjadi malam yang dibuang."
    else:
        nar "Kau membiarkan pesan itu tanpa tawaran datang. Di rumah Amamiya, Koita mengecilkan volume televisi ketika suara tawa di dalamnya mulai terasa mengganggu."
        nar "Ia makan dari piring yang sama seperti di foto, mencucinya, lalu menaruh kembali kotak kue kecil di lemari es. Tidak ada bel yang berbunyi."
        koita "Selamat Natal. Semoga malammu menyenangkan."
        nar "Pesan terakhir itu ia kirim tanpa pertanyaan. Lampu ruang keluarga padam lebih dahulu daripada lampu kamarnya."
    return

init 1 python:
    _hook("K18-A", lambda: kk_flag("koita_daftar_dibaca"))
    _hook("K18-B", lambda: (kk_flag("koita_nama_dihapus"), kk_koita_fear(6)))
    _hook("K18-C", lambda: kk_flag("koita_nama_pemain_ditulis"))
    _hook("K19-A", lambda: (kk_rel("koita","trust",5), kk_flag("koita_skripsi_jujur")))
    _hook("K19-B", lambda: (kk_rel("koita","trust",3), kk_flag("koita_skripsi_jujur")))
    _hook("K19-C", lambda: (kk_rel("koita","trust",-6), kk_koita_fear(5)))
    _hook("K23-A", lambda: kk_flag("koita_penerbit_pergi"))
    _hook("K23-B", lambda: kk_flag("koita_penerbit_tinggal"))
    _hook("K23-C", lambda: (kk_rel("koita","trust",4), kk_flag("koita_penerbit_ikut")))
    _hook("K24-A", lambda: (kk_rel("koita","trust",4), kk_flag("koita_pidato_dihadiri")))
    _hook("K24-C", lambda: (kk_koita_fear(8), kk_flag("koita_pidato_diganggu")))
    _hook("K25-A", lambda: (kk_rel("koita","trust",6), kk_flag("koita_natal_ditemani")))
    _hook("K25-B", lambda: kk_flag("koita_natal_wakil"))
    _hook("K25-C", lambda: (kk_koita_fear(10), kk_flag("koita_sendiri")))
