# Stub berkomentar untuk node keputusan akhir M35/M36 (data-only).
# TIDAK terjadwal di KK_MILESTONE_MAP (hasilnya ditarik resolver akumulatif).
# Ini hanya TEMPAT untukmu menulis adegan penutup bila suatu saat ingin
# menjadikannya adegan eksplisit. Label dibiarkan tak dipanggil = aman.

# ┌─ PANDUAN CERITA · K26 · Pilihan Terakhir Koita
# │ LOKASI  : —
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : (node keputusan / penutup — tak ada menu)
# │ AKHIRAN : ending Koita: Dipilih / Sendiri / Tetap Menggantung / Hancur.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K26:
    call kk_scene_enter("koita", "Gedung Sastra · Selesai kuliah")
    nar "Koita mengeluarkan isi lokernya satu per satu. Buku pinjaman, tiket yang tak jadi dipakai, selembar catatan dengan tulisan tangan orang lain. Benda-benda kecil yang dulu mudah ia simpan tanpa memikirkan siapa yang menunggu jawabannya."
    koita "Aku sempat mau mengajak semuanya makan. Biar hari terakhir kuliah terasa seperti dulu."
    nar "Ia meratakan tiket itu di telapak tangan. Lipatannya sudah putih."
    koita "Terus aku sadar, aku sudah menyiapkan kalimat kalau ada yang nggak datang. Aku akan bilang mereka sibuk. Seolah aku nggak perlu bertanya kenapa."
    nar "Di luar, seseorang menyeret kursi. Suaranya panjang dan kasar di koridor yang mulai kosong."
    koita "Aku nggak tahu jawaban mereka nanti. Ada yang mungkin bahkan nggak mau membaca pesanku."
    koita "Tapi aku tahu apa yang harus berhenti kulakukan. Aku nggak bisa terus meminta orang tinggal sambil menyembunyikan tempat mereka dalam hidupku."
    nar "Ia meletakkan buku pinjaman terpisah dari barang miliknya. Satu nama di satu buku; satu urusan yang harus ia selesaikan dengan orang yang tepat."
    koita "Kalau aku bilang sayang, aku harus berani bilang sayang yang seperti apa. Kalau aku cuma takut sendirian... aku harus mengaku itu juga."
    nar "Koita menutup loker. Tangannya tertahan sesaat pada pintunya, menunggu sesuatu yang tidak datang dari dalam. Lalu ia mengambil tasnya sendiri."
    return

# ┌─ PANDUAN CERITA · Mi27 · Pilihan Miyuki
# │ LOKASI  : —
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : keputusan akhir. *Efek:* ending Miyuki.
# │ INTI    : (node keputusan / penutup — tak ada menu)
# │ AKHIRAN : — (kosong di katalog; bebas karang)
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi27:
    call kk_scene_enter("miyuki", "Apartemen Miyuki · Menjelang pagi")
    nar "Timer dapur berbunyi ketika Miyuki sedang duduk. Biasanya ia sudah berdiri sebelum bunyi kedua. Kali ini ia membiarkannya selesai, lalu mengangkat wajah dari kedua tangannya."
    miyuki "Kuenya aman. Ovennya sudah mati otomatis. Aku cuma... ingin duduk sampai benar-benar ingin bangun."
    nar "Di meja ada daftar kegiatan esok hari. Hampir semua baris diawali nama orang lain."
    miyuki "Lucu, ya. Aku bisa bertanya ke pasien kecil di mana yang sakit. Ke diriku sendiri, pertanyaannya selalu: masih sanggup berapa lama?"
    nar "Ia menarik kertas itu mendekat, tetapi tidak merobeknya. Ada tanggung jawab yang tetap nyata; ada kebiasaan yang selama ini menyamar sebagai tanggung jawab."
    miyuki "Aku tetap ingin merawat orang. Aku juga masih bisa menginginkan seseorang. Dua hal itu nggak perlu membuatku terus meminta izin untuk lelah."
    miyuki "Jawaban yang akan kuberi mungkin mengecewakan orang. Aku takut itu. Jangan kira karena aku bisa mengucapkannya, tanganku sudah berhenti gemetar."
    nar "Ia menyelipkan tangan ke bawah lengan kardigannya. Senyumnya muncul sebentar, kecil dan letih."
    miyuki "Tapi kali ini aku mau mendengar jawabanku sendiri sampai selesai. Jangan buru-buru menenangkanku sebelum aku selesai bicara, ya."
    nar "Aroma kue memenuhi apartemen. Miyuki bangkit setelah beberapa saat, mengambil satu piring untuk dirinya, lalu duduk kembali."
    return

# ┌─ PANDUAN CERITA · N24 · Pilihan Nagisa
# │ LOKASI  : —
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : keputusan akhir. *Efek:* ending Nagisa.
# │ INTI    : (node keputusan / penutup — tak ada menu)
# │ AKHIRAN : — (kosong di katalog; bebas karang)
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N24:
    call kk_scene_enter("nagisa", "Bangku dekat taman · Sore")
    nar "Satu telinga Koko keluar dari tas Nagisa. Ia mendorongnya masuk, lalu berubah pikiran dan membiarkannya terlihat."
    nagisa "Jangan lihat begitu. Aku bawa karena tadi beres-beres. Bukan karena mau menjadikan boneka saksi sidang."
    nar "Ia mencoba tertawa. Tak ada yang perlu kauucapkan untuk membuat tawa itu berhenti."
    nagisa "Dulu aku pikir, kalau aku paling lama mengenalnya, aku pasti paling mengerti. Terus kalau aku paling mengerti, dia pasti akan memilihku."
    nagisa "Aku bahkan marah pada orang yang nggak pernah tahu ada perlombaan di kepalaku."
    nar "Ibu jarinya mengusap jahitan lama di telinga Koko. Ia hafal bagian yang pernah lepas dan bagian yang diperbaikinya sendiri."
    nagisa "Kenangannya tetap punyaku. Aku nggak mau pura-pura semuanya jelek supaya lebih gampang pergi. Tapi kenangan juga nggak bisa menjawab untuk orang yang hidup sekarang."
    nar "Dari taman terdengar anak kecil memanggil temannya pulang. Nagisa menoleh, menunggu suara itu menjauh."
    nagisa "Apa pun yang nanti kupilih, aku harus bisa mengatakannya tanpa mengancam siapa pun akan kehilangan aku. Dan aku harus bisa mendengar jawaban yang nggak kusuka."
    nagisa "Susah. Aku tahu. Makanya jangan pasang wajah seolah aku baru saja lulus. Aku baru mau mulai."
    nar "Ia menggeser tas agar ada tempat di bangku. Kali ini ia menanyakan apakah kau mau duduk sebelum menyuruhmu mendekat."
    return

# ┌─ PANDUAN CERITA · H24 · Pilihan Harumi
# │ LOKASI  : —
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : keputusan akhir. *Efek:* ending Harumi.
# │ INTI    : (node keputusan / penutup — tak ada menu)
# │ AKHIRAN : — (kosong di katalog; bebas karang)
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H24:
    call kk_scene_enter("harumi", "Perpustakaan · Meja terakhir")
    nar "Harumi menghapus judul sebuah kolom sampai kertasnya menipis. Kolom-kolom lain penuh tanggal, percakapan, dan panah yang hanya bisa ia baca sendiri."
    harumi "Ini bukan tabel penilaian kalian. Awalnya aku mencatat supaya tidak salah mengingat. Lalu... aku mulai menggunakannya supaya tidak perlu memutuskan."
    nar "Penghapusnya berhenti di atas satu kata: aman."
    harumi "Aku memasukkan diam sebagai persetujuan. Kesediaanku membantu sebagai kewajiban berikutnya. Kalau hasilnya menyakitkan, aku mencari kesalahan pada pencatatannya."
    harumi "Metodenya buruk. Aku tahu itu sekarang. Mengetahuinya tidak otomatis membuatku berani."
    nar "Ia melipat kertas tersebut. Sudutnya tidak tepat bertemu; untuk sekali ini ia tidak membetulkannya."
    harumi "Aku ingin menjawab sebagai diriku sendiri. Bukan sebagai orang yang paling mudah diminta memahami."
    harumi "Mungkin aku akan kehilangan hubungan karena jawaban itu. Mungkin justru itu syarat agar hubungan tersebut menjadi nyata. Aku belum bisa membuktikannya."
    nar "Buku di depan Harumi masih terbuka. Ia menyelipkan catatannya sebagai pembatas, bukan sebagai kesimpulan."
    harumi "Kalau nanti suaraku terlalu kecil, minta aku mengulang. Jangan menebak. Aku sedang belajar berhenti membiarkan orang lain mengisi bagian yang tidak kuucapkan."
    return

# ┌─ PANDUAN CERITA · S25 · Pilihan Shiori
# │ LOKASI  : —
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : keputusan akhir. *Efek:* ending Shiori.
# │ INTI    : (node keputusan / penutup — tak ada menu)
# │ AKHIRAN : — (kosong di katalog; bebas karang)
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S25:
    call kk_scene_enter("shiori", "Kediaman Saionji · Ruang tamu")
    nar "Shiori membalik kartu nama di meja sehingga sisi putihnya menghadap atas. Di ruangan ini, bahkan tamu yang sudah pergi masih sering dianggap punya suara."
    shiori "Aku sudah menerima cukup banyak nasihat tentang keputusan yang menguntungkan. Menarik sekali betapa jarang mereka bertanya siapa yang akan menjalani akibatnya."
    nar "Ia meluruskan punggung ketika pintu koridor tertutup. Sikap itu terbentuk jauh sebelum kau mengenalnya."
    shiori "Jangan salah paham. Aku juga pernah memperlakukan orang seperti angka dalam perhitungan. Menjadi sasaran kepentingan orang lain tidak membuat perbuatanku sendiri otomatis benar."
    shiori "Ada jawaban yang ingin kuberikan karena tulus. Ada yang terasa memuaskan karena akan melukai seseorang. Hari ini aku harus membedakannya."
    nar "Ia memindahkan kartu nama itu ke tepi meja, menyisakan ruang kosong di depannya."
    shiori "Aku tidak menjanjikan pilihan yang membuat semua orang tenang. Aku menjanjikan keputusan yang bersedia kuakui sebagai milikku. Termasuk kalau kelak aku menyesal."
    nar "Untuk beberapa saat ia tidak tampak hendak menambahkan apa pun. Keheningan di antara kalian kehilangan sifatnya sebagai ujian."
    shiori "Kau boleh tidak sepakat. Aku akan mendengarnya. Tetapi jangan menjawab atas namaku hanya karena kau menganggap dirimu lebih tahu cara menyelamatkanku."
    nar "Shiori meraih cangkirnya. Tehnya sudah dingin; ia meminumnya tanpa memanggil siapa pun untuk mengganti."
    return

# ┌─ PANDUAN CERITA · C18 · Pilihan Chiasa
# │ LOKASI  : —
# │ TERLIBAT: Amamiya Chiasa (+ Koita bila relevan)
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : (node keputusan / penutup — tak ada menu)
# │ AKHIRAN : lolos atau gagal evaluasi; ending Chiasa (Koita Success / Yutaka / Yuri / mandiri).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C18:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Pintu depan")
    nar "Chiasa menghitung kunci pada gantungan di pintu. Kunci rumah, kunci sepeda, satu kunci kecil yang sudah tak jelas membuka apa. Ia masih mengingat siapa yang dahulu memintanya menyimpan masing-masing."
    chiasa "Kalau hafal kebiasaan seseorang, gampang sekali merasa punya hak atas hidupnya. Aku tahu jam pulangnya. Aku tahu cangkir favoritnya. Masa aku bisa salah tentang perasaannya?"
    nar "Pertanyaan itu diucapkan pelan, hampir manis. Ia mendengar sendiri apa yang ganjil di dalamnya."
    chiasa "Bisa, ternyata. Orang bisa tetap pulang ke rumah yang sama sambil ingin pergi jauh darimu."
    nar "Ia melepaskan gantungan dari jarinya sebelum bekas lingkarannya semakin dalam."
    chiasa "Aku belum tahu bagaimana menjelaskan semuanya. Ada hal yang kurasakan sendiri, ada hal yang seolah didorong dari tempat lain. Tapi akibatnya terjadi di sini. Pada orang yang benar-benar mengenalku."
    chiasa "Aku ingin sesuatu karena aku menginginkannya. Kedengarannya sederhana. Selama ini aku lebih sibuk memastikan sesuatu itu tidak bisa meninggalkanku."
    nar "Chiasa mengembalikan kunci ke kait. Kedua tangannya kini kosong."
    chiasa "Aku akan memberi jawaban. Dan kalau orang yang kutuju berkata tidak... aku harus membiarkan kalimatnya selesai."
    nar "Ia membuka pintu secukupnya untuk keluar, lalu menoleh sekali ke ruang keluarga. Kali ini ia tidak meminta kau menjanjikan bahwa segala sesuatu akan tetap sama saat ia pulang."
    return

# ┌─ PANDUAN CERITA · Y19 · Jawaban
# │ LOKASI  : —
# │ TERLIBAT: Kisaragi Yutaka (+ Koita bila relevan)
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : (node keputusan / penutup — tak ada menu)
# │ AKHIRAN : ending Yutaka (lihat Kisaragi_Yutaka.md bagian 11).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y19:
    call kk_scene_enter("yutaka", "Stasiun · Sebelum keberangkatan")
    nar "Yutaka salah membeli dua minuman yang sama. Ia memandang tombol mesin, lalu kaleng di tangannya, seolah baru sadar kebiasaan bisa bergerak lebih cepat dari pikiran."
    yutaka "Biasanya kuberikan satu ke orang yang bareng aku. Tadi aku bahkan nggak bertanya kamu mau apa."
    nar "Ia meletakkan kaleng kedua di bangku, tidak langsung menyodorkannya."
    yutaka "Aku sering bilang terserah, yang penting semua senang. Kadang itu memang karena aku senang melihat mereka senang. Kadang karena aku takut kalau keinginanku bikin repot."
    yutaka "Terus ada hal-hal yang tetap kulakukan, tetap kupilih, meskipun setelahnya aku ingin bilang aku cuma terbawa."
    nar "Pengumuman kereta memotong pembicaraan. Ia menunggu hingga nama stasiun terakhir selesai dibacakan."
    yutaka "Aku nggak mau memakai kata baik untuk menutupi itu. Jawabanku nanti harus bisa kutanggung setelah hari ini lewat."
    yutaka "Kalau ada yang mau tinggal, aku mau tahu dia tinggal karena mau. Kalau dia pergi, aku nggak mau menjadikan semua yang pernah kuberikan sebagai tagihan."
    nar "Ia menatap jalur kereta, lalu kembali padamu. Wajahnya masih hangat; kehangatan itu kini disertai kesungguhan yang sulit kauabaikan."
    yutaka "Jadi dengarkan aku sekali ini, ya. Aku akan bilang apa yang sebenarnya kuinginkan."
    return

# ┌─ PANDUAN CERITA · K27 · Wisuda
# │ LOKASI  : —
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : (node keputusan / penutup — tak ada menu)
# │ AKHIRAN : epilog; evaluasi Sistem.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K27:
    call kk_scene_enter("koita", "Kouseikan · Hari wisuda")
    nar "Jubah wisuda membuat semua orang sibuk dengan hal kecil: kerah yang terlipat, tali yang tidak rata, topi yang terus miring. Koita beberapa kali mengangkat tangan untuk membantu, lalu bertanya lebih dahulu."
    koita "Boleh kubetulkan? Talinya tersangkut."
    nar "Kampus masih sama. Jalan menuju kantin, pintu klub sastra, bangku tempat seseorang pernah menunggu terlalu lama. Hari ini semuanya menjadi latar foto yang kelak bisa dipotong sesuka pemiliknya."
    koita "Aku dulu yakin kita pasti berfoto lengkap di sini. Sampai sudah memikirkan siapa berdiri di mana."
    nar "Ia mengusap tengkuk, menatap orang-orang yang berkumpul dalam kelompok berbeda. Tak semua jarak di antara mereka bisa dijelaskan oleh kamera."
    koita "Ternyata lulus bareng nggak berarti selesai dengan cara yang sama."
    nar "Di sudut kesadaranmu, kau menunggu penilaian Sistem. Selama ini angka selalu tampak siap memberi arti pada sesuatu yang baru saja terjadi. Namun orang-orang di halaman tidak berhenti bergerak untuk menunggu hasilnya."
    koita "Aku mau mengembalikan ini dulu. Sudah kelamaan kubawa."
    nar "Koita menunjukkan sebuah buku, lalu berjalan menuju pemiliknya. Percakapan mereka tak terdengar dari tempatmu. Ia tidak menoleh untuk memastikan kau menyaksikan."
    nar "Seseorang memanggil nama untuk foto berikutnya. Kau merapikan pakaianmu sendiri, menyadari bahwa apa pun putusan yang muncul nanti, hari esok tetap akan meminta jawaban dari orang yang kini berdiri di dalam tubuh ini."
    return
