# Event dinamis Harumi (H-D02/03/04/06/08/09/10/11/12) — jalur Ogawa (eksploitasi
# advisor) + poros kejelasan/validasi. Eksploitasi ditulis sebagai konsekuensi dan
# karakter; tanpa metode. H-D11 berpusat pada persetujuan, non-eksplisit.

# ┌─ PANDUAN CERITA · H-D02 · Lembar Pengamatan
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kujo Harumi
# │ AWALAN  : jalur H12
# │ INTI    : A Koreksi datanya dengan jujur / B tertawa / C pakai datanya
# │ AKHIRAN : kejelasan ±; validasi[[pemain]
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H_D02:
    call kk_scene_enter("harumi", "Gedung Sains & Lab · Lembar pengamatan")
    nar "Harumi menyodorkan tabel. Kolom-kolomnya mencatat reaksimu: kapan kau tersenyum, berapa lama kau menatap, apa yang membuatmu diam."
    harumi "Aku tersenyum ketika gugup. Mungkin orang lain juga begitu. Tapi kalau setiap tanda bisa berarti dua hal, aku tidak tahu kapan boleh percaya kesimpulanku. Apakah aku salah mencatatmu?"
    call kk_family_menu("H-D02", ["Koreksi datanya dengan jujur.", "Tertawakan metodenya.", "Manfaatkan: biarkan ia salah membaca."])
    if _return == "A":
        nar "Kau menjelaskan arti tindakanmu sendiri, termasuk yang tidak sesuai harapannya. Harumi menandai bagian yang ternyata ia simpulkan tanpa bertanya."
        harumi "Aku tidak bisa menjadikan lama tatapan sebagai persetujuan. Aku tahu itu secara teori. Aneh sekali saat perasaanku sendiri yang membuatku melewatinya."
        nar "Ia menambahkan satu pertanyaan langsung pada catatan berikutnya, memberi tempat bagi jawaban yang belum bisa diketahui dari pengamatan saja."
    elif _return == "B":
        harumi "Aku tahu kelihatannya berlebihan. Tapi aku sungguh berusaha memahami, bukan membuat pertunjukan."
        nar "Ia menarik tabel dari dekatmu. Tawa itu tidak membuatnya berhenti mengamati; hanya membuatnya lebih jarang memperlihatkan cara ia mencari pemahaman."
    else:
        nar "Kau membiarkan kekeliruannya ketika kesimpulan itu memberimu keuntungan. Harumi menganggap diammu sebagai konfirmasi dan menulis ulang batas yang semula hendak dipertahankannya."
        harumi "Jadi aku boleh menganggap kamu menginginkan itu. Baik."
        nar "Kepastian yang ia pinjam darimu bertumpu pada bagian yang sengaja tidak kauluruskan."
    return

# ┌─ PANDUAN CERITA · H-D03 · Pintu Lab Jam Sebelas
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kujo Harumi
# │ AWALAN  : cengkeraman_ogawa ≥ 40; pemain lewat lab saat Larut
# │ INTI    : A Ketuk / B catat jam keluar / C pergi / D panggil satpam
# │ AKHIRAN : bukti +; risiko konfrontasi
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H_D03:
    call kk_scene_enter("harumi", "Gedung Sains & Lab · Jam sebelas malam")
    nar "Pukul sebelas, lampu lab masih menyala. Dari balik pintu tertutup terdengar Ogawa menyebut kepercayaan, lalu jawaban Harumi yang terlalu pelan untuk dipahami dari koridor."
    nar "Kau tidak mengetahui seluruh yang berlangsung di dalam. Yang jelas, jadwal kerja sudah lewat dan Harumi belum keluar seperti yang tadi direncanakan."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", KK_DYN_BY_ID["H-D03"]["choices"])]
    call screen kk_choice_panel(_rows, "Pintu lab jam sebelas")
    $ kk_record_choice("H-D03", _return)
    if _return == "A":
        play sound "audio/sfx/door_knock.wav"
        nar "Kau mengetuk dan menanyakan Harumi. Ogawa membuka pintu dengan senyum yang segera membicarakan kesibukan riset."
        harumi "Aku mendengar ketukan. Aku ingin keluar sebentar."
        nar "Ia mengatakan itu sebelum diberi penjelasan mengapa sebaiknya tetap tinggal. Kehadiranmu membuat jeda yang tadi tidak berani ia minta menjadi mungkin."
    elif _return == "B":
        nar "Kau menunggu dan mengingat kapan pintu dibuka serta siapa yang keluar. Catatan itu tidak menjelaskan apa yang terjadi di ruangan, tetapi dapat menguatkan urutan waktu jika Harumi kelak memerlukannya."
        nar "Ia berjalan dengan pandangan tertunduk. Kau kini punya satu kepastian kecil, dan banyak hal lain yang belum berhak disebut fakta."
    elif _return == "C":
        nar "Kau melanjutkan langkah. Pembicaraan di balik pintu tidak berhenti ketika suara sepatumu menjauh."
        nar "Nanti, saat Harumi mengatakan malamnya hanya dipakai bekerja, kau akan punya ingatan tentang koridor dan pilihan untuk tidak mengetuk. Ingatan itu belum cukup menjelaskan apa yang tak kaulihat."
    else:
        nar "Kau memanggil petugas untuk memeriksa ruangan yang masih digunakan. Pertanyaan tentang jadwal dan izin membuat Ogawa membuka pintu lebih lebar."
        harumi "Saya sudah ingin pulang. Barang saya tinggal diambil."
        nar "Petugas menunggu sementara ia membereskan. Kehadiran pihak lain tidak menyelesaikan hubungan kuasa itu, tetapi malam ini memberi Harumi jalan keluar yang tidak harus ia pertahankan sendirian."
    return

# ┌─ PANDUAN CERITA · H-D04 · Tawaran Ogawa
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kujo Harumi
# │ AWALAN  : Ogawa mengenal pemain
# │ INTI    : A Tolak / B pura-pura menerima / C laporkan
# │ AKHIRAN : pura-pura menerima membuka jalur penyusup (E-NPC-26 atau E-NPC-27)
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H_D04:
    call kk_scene_enter("harumi", "Koridor Sains · Tawaran")
    nar "Ogawa menyapamu setelah Harumi dipanggil ke ruangan lain. Ia membicarakan bakatnya dengan nada akrab, kemudian mulai membahas bagaimana kalian bisa mempermudah pilihan-pilihannya."
    "Ogawa" "Kau dekat dengannya. Kalau kita saling memahami, banyak hal tidak perlu dibuat sulit. Aku bisa menghargai kerja sama."
    nar "Harumi tidak berada di sana untuk mendengar dirinya diperlakukan sebagai urusan antara dua orang."
    call kk_family_menu("H-D04", ["Tolak tegas.", "Pura-pura menerima untuk menyusup.", "Laporkan tawaran ini."])
    if _return == "A":
        "Ogawa" "Sayang sekali. Kupikir kau orang yang realistis."
        nar "Kau menolak tanpa tertawa untuk melunakkan jawaban. Ogawa segera menyebut tawarannya disalahpahami, tetapi tak lagi mengulangnya. Kau telah kehilangan keramahan yang ternyata memang punya syarat."
    elif _return == "B":
        nar "Kau berpura-pura menyetujui. Ogawa mengendur, memperlakukanmu sebagai orang yang bisa diajak bicara dengan cara berbeda."
        nar "Kini ada kesempatan mengetahui lebih banyak dan risiko ikut mendapatkan keuntungan yang membuat penolakan semakin sulit. Niat menyusup tidak akan menghapus akibat jika kau mulai menikmati tempat di sisinya."
    else:
        nar "Kau menyampaikan tawaran yang didengar kepada pihak yang dapat menanganinya, membedakan perkataannya dari dugaanmu tentang maksud di baliknya."
        nar "Ogawa kehilangan kemudahan berbicara seolah semua orang akan menerima bahasa yang sama. Harumi belum mengetahui seluruh persoalannya, tetapi sesuatu di sekitarnya akhirnya mulai diperiksa dari luar."
    return

# ┌─ PANDUAN CERITA · H-D06 · Taksi Jam Lima
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kujo Harumi
# │ AWALAN  : tahap ≥ 4; pemain begadang di dekat asrama
# │ INTI    : A Sapa / B ikuti / C pura-pura tidak lihat / D foto
# │ AKHIRAN : bukti, atau bahan pemerasan; Trust
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H_D06:
    call kk_scene_enter("harumi", "Dekat asrama · Taksi jam lima")
    nar "Taksi berhenti sebelum pukul lima selesai disebut radio penjaga. Harumi turun dengan tas dipeluk dekat dada dan pakaian yang kauingat dari kemarin. Ia menunggu kendaraan pergi sebelum berjalan menuju asrama."
    nar "Kau tidak tahu dari mana ia pulang. Rasa ingin tahu mudah sekali menyamar sebagai hak mengetahui ketika seseorang yang dekat tampak menyimpan sesuatu."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", KK_DYN_BY_ID["H-D06"]["choices"])]
    call screen kk_choice_panel(_rows, "Taksi jam lima")
    $ kk_record_choice("H-D06", _return)
    if _return == "A":
        harumi "Kau... di sini? Jangan tanya. Tolong, kali ini saja, jangan tanya."
        nar "Kau menanyakan apakah ia memerlukan bantuan untuk sampai dengan aman, bukan meminta cerita malamnya. Harumi mengangguk kecil pada tawaran membawa barang sampai pintu."
        harumi "Aku belum bisa menjelaskan. Terima kasih kalau itu tidak membuatmu memutuskan semuanya sendiri tentangku."
    elif _return == "B":
        nar "Kau mengikutinya tanpa menyapa. Harumi masuk melalui pintu samping dan berhenti lama sebelum menemui pengelola. Kau mengingat waktu serta tempat, belum mengetahui alasan di balik gerakannya."
        nar "Jika catatan itu kelak membantunya, ia tetap berhak bertanya mengapa kau memilih mengawasi pada pagi ia begitu membutuhkan rasa aman."
    elif _return == "C":
        nar "Kau berpaling dan membiarkan ia masuk. Harumi tidak melihatmu, tidak perlu menjelaskan diri sebelum berhasil mencapai kamarnya."
        nar "Di ponselmu percakapan terakhir masih tentang pekerjaan biasa. Kini ada jarak antara yang ia katakan dan yang kaulihat, sebuah jarak yang belum memilih sendiri akan menjadi kehati-hatian atau tuduhan."
    else:
        nar "Kau memotretnya tanpa bertanya. Cahaya pagi menunjukkan letih, tas, dan jam kedatangan; tidak satu pun dapat menjelaskan seluruh malam yang dilewati."
        nar "Gambar itu dapat kaupakai sebagai tekanan justru karena orang mudah mengisinya dengan dugaan. Harumi masih berjalan menuju kamar, belum tahu rasa amannya baru saja diperkecil menjadi berkas yang kausimpan."
    return

# ┌─ PANDUAN CERITA · H-D08 · Hipotesis Ditolak
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kujo Harumi
# │ AWALAN  : kejelasan ≥ 60; validasi[[ogawa] ≥ 40
# │ INTI    : A Dukung keputusannya / B ragukan / C ajak ke Mizuhara
# │ AKHIRAN : cengkeraman_ogawa −30; belok besar
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H_D08:
    call kk_scene_enter("harumi", "Gedung Sains & Lab · Hipotesis ditolak")
    harumi "Aku membaca ulang pertemuan-pertemuan kami. Setiap kali aku menolak, dia membuatku takut kehilangan sesuatu yang penting. Setiap kali menurut, syarat berikutnya bertambah. Aku ingin berhenti menamakannya bimbingan."
    nar "Ia mengatakan memanfaatkan dengan jeda panjang. Kata itu mengubah kenangan yang semula berusaha disimpan sebagai kesempatan istimewa."
    call kk_family_menu("H-D08", ["Dukung keputusannya menjauh.", "Ragukan kesimpulannya.", "Ajak ia menemui Mizuhara."])
    if _return == "A":
        harumi "Kau setuju. ...Kalau begitu, aku akan menarik diri dari bimbingannya. Hipotesis yang salah harus dibuang."
        nar "Kau mendukung tanpa menuntut ia segera tenang. Harumi menyusun pemberitahuan singkat, lalu menanyakan siapa yang bisa mendampingi jika keputusannya dihalangi. Kali ini ia menyiapkan dukungan, bukan balasan untuk membuat Ogawa tetap senang."
    elif _return == "B":
        harumi "Kau pikir aku salah baca? ...Mungkin. Aku memang buruk soal ini. Aku akan uji lagi."
        nar "Ia membuka kembali catatan yang tadi akhirnya ditutup. Keraguanmu tidak mengembalikan kuasa Ogawa sepenuhnya, tetapi cukup untuk membuatnya menunda mempercayai penilaian yang telah susah payah dibentuk sendiri."
    else:
        nar "Kau menemaninya menghadap Mizuhara dan membiarkan ia menjelaskan sendiri sebelum menambahkan yang kaulihat. Harumi beberapa kali berhenti, tetapi tidak diminta mengulang sampai terdengar lebih tenang."
        "Mizuhara" "Kita hentikan akses yang membuatmu tertekan dan atur dukungannya. Kamu tidak perlu kembali ke situ untuk membuktikan bahwa keberatanmu sungguh-sungguh."
    return

# ┌─ PANDUAN CERITA · H-D09 · Celah di Jadwal
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kujo Harumi
# │ AWALAN  : ia menghilang dua malam seminggu
# │ INTI    : A tanya / B ikuti / C tanya Ogiwara
# │ AKHIRAN : H15 terbuka lebih awal
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H_D09:
    call kk_scene_enter("harumi", "Perpustakaan Pusat · Celah jadwal")
    nar "Dua malam pada jadwal Harumi tidak lagi diberi nama. Di tempat lain ia masih menuliskan hal sekecil mengembalikan buku. Kekosongan yang begitu teratur tampak lebih disengaja daripada catatan yang terlupa."
    call kk_family_menu("H-D09", ["Tanyakan langsung padanya.", "Ikuti diam-diam malam nanti.", "Tanya Ogiwara, teman labnya."])
    if _return == "A":
        harumi "Dua malam itu? ...Itu urusan bimbingan. Aku tidak mencatatnya karena... karena aku tidak ingin mencatatnya."
        nar "Kau menanyakan apakah ia ingin ditemani membicarakan alasannya, dan menerima ketika ia belum sanggup. Harumi tidak langsung bercerita, tetapi ia menyimpan pertanyaanmu sebagai sesuatu yang boleh dijawab nanti."
    elif _return == "B":
        nar "Kau mengikuti pada malam berikutnya dan melihat hubungan antara ruang kosong itu dengan pertemuan Ogawa. Harumi tidak tahu kau berada di sana."
        nar "Informasi yang diperoleh dapat membuka persoalan uang lebih awal. Cara memperolehnya tetap menyisakan pertanyaan tentang apakah ia akan merasa didampingi atau kembali kehilangan kendali ketika mengetahuinya."
    else:
        "Ogiwara" "Saya pengelola asrama. Saya melihat jam pulangnya berubah, dan dia menyebut pertemuan dengan Ogawa. Saya belum tahu semuanya. Yang ingin saya pastikan, dia tidak takut mencari bantuan di sini."
        nar "Kau mendapat pengamatan lain yang sejalan, tanpa menjadikannya keterangan tentang sesuatu yang tidak disaksikan Ogiwara sendiri."
    return

# ┌─ PANDUAN CERITA · H-D10 · Permintaan Komentar
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kujo Harumi
# │ AWALAN  : rumor tentang Harumi; Mei menghubungi pemain
# │ INTI    : A bantah / B diam / C beri informasi
# │ AKHIRAN : reputasi Harumi; Mei mendapat bahan
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H_D10:
    call kk_scene_enter("harumi", "Permintaan komentar")
    "Mei" "Aku menulis soal Kujo dan Ogawa. Ada orang bilang dia mendapat perlakuan khusus. Kamu mengenalnya. Satu komentar saja?"
    nar "Kau mendengar kata khusus yang selama ini dipakai Ogawa kini muncul sebagai tuduhan terhadap Harumi. Satu kalimat darimu akan mudah dipindahkan ke percakapan yang tidak lagi bisa kaudengar."
    call kk_family_menu("H-D10", ["Bantah rumornya.", "Diam, jangan beri apa pun.", "Beri informasi yang kau tahu."])
    if _return == "A":
        nar "Kau membantah anggapan yang tidak berdasar dan menolak menjadikan hidup pribadi Harumi bahan hiburan. Mei meminta sesuatu yang lebih tajam; kau tetap pada hal yang benar-benar dapat dikatakan."
        nar "Rumor tidak hilang seluruhnya, tetapi tidak mendapat dukungan yang diharapkan dari orang dekat."
    elif _return == "B":
        "Mei" "Tidak mau bicara? Ya sudah. Diammu juga sejenis jawaban, tahu."
        nar "Kau tidak memberi bahan. Mei pergi membawa kecenderungannya sendiri untuk menafsirkan. Menolak berkomentar tidak otomatis menghentikan orang lain menulis, dan Harumi tetap harus hidup di tengah cerita yang sedang bergerak tanpa dirinya."
    else:
        nar "Kau memberinya informasi yang diketahui. Mei memilih bagian yang paling menarik, tidak selalu bagian yang paling perlu dipahami."
        nar "Saat kabar itu kembali ke lingkungan Harumi, yang hilang justru konteks ketakutan dan kuasa. Ia harus menghadapi tatapan tentang percakapan yang tidak pernah ia setujui untuk dibagikan."
    return

# ┌─ PANDUAN CERITA · H-D11 · Pelajaran yang Ia Minta
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kujo Harumi
# │ AWALAN  : kejelasan ≥ 50; Intim ≥ 50
# │ INTI    : A Jelaskan dengan kata / B ajak kencan biasa / C manfaatkan permintaan itu / D tolak dengan lembut
# │ AKHIRAN : memanfaatkan: validasi[[pemain] naik ke arah Distorted; kencan biasa: E-HA-01 menguat
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H_D11:
    call kk_scene_enter("harumi", "Asrama Putri · Pelajaran yang ia minta")
    harumi "Aku ingin membicarakan cinta. Aku bisa mencari definisi. Yang tidak kupahami adalah bagaimana orang tahu mereka boleh meminta lebih dekat, atau boleh berhenti. Aku memilih bertanya kepadamu. Itu bukan berarti aku menyetujui semua jawaban sebelum mendengarnya."
    nar "Ia tampak canggung mengatakan bagian terakhir, lalu terlihat lebih lega setelah berhasil."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", KK_DYN_BY_ID["H-D11"]["choices"])]
    call screen kk_choice_panel(_rows, "Ia meminta diajari")
    $ kk_record_choice("H-D11", _return)
    if _return == "A":
        nar "Kau membicarakan keinginan, kepercayaan, dan hak mengubah pikiran, tanpa berpura-pura ada rumus yang menjamin semua hubungan berhasil. Harumi beberapa kali bertanya ulang."
        harumi "Jadi bertanya bukan gagal memahami. Justru itu cara agar aku tidak memutuskan untuk orang lain. Aku bisa mulai dari sana."
    elif _return == "B":
        nar "Kau mengajaknya berkencan tanpa menjadikannya pelajaran yang harus diikuti dengan benar. Harumi menanyakan tempat, waktu, dan apakah ia boleh menyebut jika ingin pulang lebih awal."
        harumi "Baik. Aku ingin mencoba. Bukan mengerjakan tugas cinta. Aku ingin menghabiskan waktu denganmu."
    elif _return == "C":
        nar "Kau memakai kepercayaannya untuk menentukan apa yang seharusnya ia berikan sebagai bukti cinta. Harumi berusaha mengikuti, mengira ketidaknyamanannya hanya bagian yang belum dipahami."
        harumi "Kalau aku belum ingin, itu berarti aku belum cukup menyukaimu?"
        nar "Pertanyaannya memberimu kesempatan berhenti. Kau tetap membiarkan jawaban yang menguntungkanmu menjadi ukuran bagi perasaannya."
    else:
        nar "Kau menolak peran yang tidak bisa kaujalani, menjelaskan bahwa penolakan itu tidak membuat pertanyaannya salah. Harumi diam, lalu mengangguk."
        harumi "Aku kecewa. Tapi aku senang kamu mengatakannya sebelum berpura-pura tahu. Aku masih boleh mencari jawaban dengan cara lain."
    return

# ┌─ PANDUAN CERITA · H-D12 · Poster Riset
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kujo Harumi
# │ AWALAN  : Chiasa host; kolaborasi berjalan
# │ INTI    : A Tampilkan nama berdua / B anonim / C batal
# │ AKHIRAN : E-HA-13 menguat
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H_D12:
    call kk_scene_enter("harumi", "Rumah Amamiya · Poster riset")
    nar "Chiasa mengilustrasikan poster riset Harumi. Keduanya berdiri memandangi hasilnya—sebuah kolaborasi yang jarang terjadi."
    harumi "Gambarmu membuat orang mau mendekat sebelum membaca. Aku menjelaskan idenya, tapi kamu membuat orang ingin tahu. Bagaimana kita menuliskan nama? Aku tidak mau bagian kerjamu menghilang."
    call kk_family_menu("H-D12", ["Tampilkan nama kalian berdua.", "Buat anonim saja.", "Batalkan kolaborasinya."])
    if _return == "A":
        harumi "Dua nama berdampingan. ...Entah kenapa itu membuatku lega. Seperti aku tidak sendirian mengerjakan ini."
        nar "Chiasa memeriksa ukurannya agar setara. Harumi tersenyum ketika melihat hasil akhir, lalu bertanya apakah mereka boleh mengerjakan sesuatu lagi setelah acara ini selesai."
    elif _return == "B":
        harumi "Anonim? ...Baik. Mungkin karyanya yang bicara, bukan namanya."
        nar "Ia menyetujui, tetapi memastikan keputusan itu tidak dimaksudkan untuk menghapus hubungan kalian di depan orang lain. Setelah mendengar jawabanmu, ia menyimpan versi kerja dengan nama keduanya sebagai pengingat siapa yang benar-benar berada di meja ini."
    else:
        nar "Kau membatalkan kolaborasi. Harumi menanyakan apa yang boleh tetap digunakan dan menerima batas yang kaupasang, meski melihat kembali gambar itu dengan jelas kecewa."
        harumi "Aku akan cari cara lain. Terima kasih untuk bagian yang sudah kamu kerjakan. Aku memang berharap ini selesai bersama."
    return

init 1 python:
    _hook("H-D02-A", lambda: (kk_adj("kejelasan_harumi",8), kk_rel("harumi","trust",4)))
    _hook("H-D02-B", lambda: kk_adj("kejelasan_harumi",-4))
    _hook("H-D02-C", lambda: (kk_harumi_validate(8), kk_flag("harumi_dimanfaatkan")))
    _hook("H-D03-A", lambda: (kk_ogawa_grip(-5), kk_rel("harumi","trust",4)))
    _hook("H-D03-B", lambda: kk_flag("bukti_ogawa_terkumpul"))
    _hook("H-D03-C", lambda: kk_ogawa_grip(5))
    _hook("H-D03-D", lambda: (kk_ogawa_grip(-10), kk_flag("ogawa_terganggu")))
    _hook("H-D04-A", lambda: (kk_ogawa_grip(-8), kk_flag("harumi_dilindungi")))
    _hook("H-D04-B", lambda: (kk_flag("penyusup_ogawa"), kk_flag("bukti_ogawa_terkumpul")))
    _hook("H-D04-C", lambda: (kk_ogawa_grip(-12), kk_flag("ogawa_dilaporkan")))
    _hook("H-D06-A", lambda: kk_rel("harumi","trust",4))
    _hook("H-D06-B", lambda: kk_flag("bukti_ogawa_terkumpul"))
    _hook("H-D06-C", lambda: None)
    _hook("H-D06-D", lambda: (kk_flag("bahan_pemerasan_harumi"), kk_rel("harumi","trust",-5)))
    _hook("H-D08-A", lambda: (kk_ogawa_grip(-30), kk_flag("harumi_menjauh_ogawa")))
    _hook("H-D08-B", lambda: kk_adj("kejelasan_harumi",-5))
    _hook("H-D08-C", lambda: (kk_ogawa_grip(-30), kk_flag("ogawa_dihentikan")))
    _hook("H-D09-A", lambda: (kk_rel("harumi","trust",3), kk_flag("harumi_celah_ditanya")))
    _hook("H-D09-B", lambda: (kk_flag("bukti_ogawa_terkumpul"), kk_flag("harumi_h15_dini")))
    _hook("H-D09-C", lambda: kk_flag("ogiwara_bersaksi"))
    _hook("H-D10-A", lambda: (kk_adj("rumor_harumi",-10), kk_rel("harumi","trust",4)))
    _hook("H-D10-B", lambda: kk_adj("rumor_harumi",5))
    _hook("H-D10-C", lambda: (kk_adj("rumor_harumi",15), kk_flag("mei_dapat_bahan")))
    _hook("H-D11-A", lambda: (kk_adj("kejelasan_harumi",10), kk_flag("harumi_dibantu_menamai_emosi")))
    _hook("H-D11-B", lambda: (kk_rel("harumi","aff",6), kk_flag("harumi_kencan_biasa")))
    _hook("H-D11-C", lambda: (kk_harumi_validate(15), kk_flag("harumi_dimanfaatkan"), kk_flag("harumi_titik_tanpa_balik")))
    _hook("H-D11-D", lambda: kk_rel("harumi","trust",5))
    _hook("H-D12-A", lambda: (kk_rel("harumi","intim",5), kk_flag("harumi_chiasa_kolaborasi")))
    _hook("H-D12-B", lambda: kk_rel("harumi","aff",3))
    _hook("H-D12-C", lambda: kk_rel("harumi","trust",-3))
