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
    if kk_host == "chiasa":
        nar "Ruang tengah vila di lantai bawah masih ramai oleh suara acara kuis televisi dan tawa teman-teman yang sedang berebut camilan malam. Untuk mencari udara yang lebih sejuk, kamu melangkah memutar ke serambi baca di sudut belakang yang menghadap langsung ke halaman pohon pinus."
        nar "Di sana, di bawah lampu dinding berwarna kuning teduh, Kujo Harumi sudah duduk seorang diri di kursi rotan. Sebuah teko keramik kecil dan dua cangkir teh berdiri di atas meja bundar di sampingnya, sementara di pangkuannya terbuka buku catatan bersampul hitam yang biasa ia bawa ke laboratorium."
        nar "Ketika kamu melangkah mendekat, kamu sempat melihat halaman buku yang sedang ia tatap. Sama sekali tidak ada struktur molekul ataupun rumus reaksi kimia di sana. Halaman bergaris itu justru terisi beberapa baris kalimat pendek lengkap dengan jam pencatatan dan tanda tanya kecil di pinggirnya."
        chiasa "Kujo-senpai belum tidur? Jauh sekali duduknya sampai ke serambi belakang sini."
        harumi "Amamiya-san. Di ruang tengah tadi tingkat kebisingannya terlalu tinggi untuk menyusun catatan, jadi aku menyingkir ke sini."
        chiasa "Harum sekali tehnya. Senpai menyeduh teh hijau panggang sendiri dari dapur?"
        harumi "Iya, daun tehnya sudah tersedia di toples lemari dapur. Aku menyeduh satu teko kecil supaya tidak perlu bolak-balik."
        chiasa "Ngomong-ngomong, masih sempat-sempatnya ya Senpai menulis materi kuliah waktu lagi liburan di vila begini."
        harumi "Ini bukan materi kuliah. Aku sedang meninjau ulang beberapa percakapan kita waktu makan siang dan jalan di pantai tadi sore."
        nar "Harumi menaikkan letak kacamatanya dengan ujung jari telunjuk, lalu menatap halaman bukunya lagi dengan kening sedikit berkerut."
        chiasa "Percakapan kita tadi siang dicatat juga?"
        harumi "Waktu kita mengobrol di beranda tadi siang, ada satu kalimatmu yang membuat detak jantungku sedikit naik dan rasanya menyenangkan. Sebaliknya, beberapa kalimat dari orang lain sesudahnya terasa datar saja. Aku punya reaksi emosional terhadap hal itu, hanya saja aku sering terlambat mengenali apa nama perasaannya sampai momennya sudah lewat."
        chiasa "Jadi Senpai tulis waktunya di buku supaya nggak lupa kejadiannya?"
        harumi "Iya. Kalau aku diam cukup lama saat kita sedang mengobrol, itu bukan karena aku mengabaikanmu atau tidak punya perasaan apa-apa. Aku hanya sedang memprosesnya lebih lambat daripada orang lain."
    else:
        nar "Ruang tengah vila masih penuh oleh suara televisi dan obrolan teman-teman yang belum mau bubar. Untuk mengistirahatkan telinga sejenak, kamu berjalan menyusuri lorong samping menuju sudut baca dekat jendela belakang yang menghadap ke taman pinus vila."
        nar "Di kursi kayu dekat jendela, Kujo Harumi ternyata sudah duduk lebih dulu ditemani teko keramik kecil yang masih mengepul dan sebuah buku catatan hitam terbuka di pangkuannya."
        nar "Saat kamu berhenti di dekat mejanya, sekilas matamu menangkap isi halaman buku tersebut. Di sana sama sekali tidak terlihat deretan angka ataupun rumus kimia. Halaman itu justru berisi potongan kalimat percakapan dari tadi siang yang diberi nomor urut, jam kejadian, dan tanda tanya di tepinya."
        yutaka "Belum tidur, Kujo-san? Jauh amat mengungsinya sampai ke pojok belakang sini."
        harumi "Kisaragi-kun. Di ruang depan terlalu banyak suara yang bertumpuk, agak sulit dipakai berpikir dengan jernih."
        yutaka "Wangi teh panggangnya sampai ke lorong lho. Kamu bikin sendiri dari dapur?"
        harumi "Iya, kebetulan di rak dapur ada kaleng daun teh panggang. Satu teko kecil cukup buat menghangatkan badan sebelum tidur."
        yutaka "Lagi liburan di vila begini masih aja buka catatan kuliah?"
        harumi "Ini bukan catatan kuliah. Aku sedang memeriksa ulang urutan obrolan waktu kita di beranda tadi siang."
        nar "Harumi membetulkan posisi kacamatanya dengan ujung jari, lalu menatap lembar catatannya dengan raut wajah serius."
        yutaka "Obrolan santai kita tadi siang sampai kamu catat di buku?"
        harumi "Tadi siang ada satu tanggapanmu yang membuatku merasa cukup senang, sedangkan percakapan lain setelah itu biasa saja. Masalahnya, aku sering baru memahami apa yang sedang kurasakan beberapa jam setelah kejadiannya selesai. Jadi kalau saat berbicara denganmu aku terdiam lama, itu bukan karena aku tidak peduli."
        yutaka "Kamu sampai menulis jam kejadiannya segala di pinggir kertas itu?"
        harumi "Supaya konteksnya tidak tercampur. Aku hanya tidak ingin diamku disalahartikan sebagai rasa bosan."
    call kk_family_menu("H04", ["Minum bersama dalam diam.", "\"Memangnya apa yang lagi kamu catat di situ?\"", "Mulai bercerita duluan tentang dirimu."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu tidak mendesaknya membuka isi buku catatan itu. Kamu hanya menarik kursi rotan di sebelahnya, membalik cangkir cadangan yang masih tertelungkup di atas baki, lalu menuangkan teh hangat dari teko untuk dirimu sendiri."
            chiasa "Boleh kan aku ikut minta satu cangkir teh panggangnya, Kujo-senpai?"
            harumi "Tentu, memang sengaja kusiapkan dua cangkir kalau kebetulan ada yang lewat."
            nar "Kamu meniup permukaan teh yang masih panas lalu menyesapnya pelan sambil menyandarkan punggung menghadap deretan pohon pinus gelap di luar kaca."
            harumi "...Kamu tidak keberatan hanya duduk diam seperti ini, Amamiya-san?"
            chiasa "Nggak keberatan sama sekali kok, Kujo-senpai. Di ruang depan lagi heboh sekali rebutan kartu, duduk tenang di sini sambil dengar suara angin pohon pinus di luar jauh lebih enak."
            nar "Harumi menatapmu selama dua detik, lalu perlahan menutup buku catatan hitam di pangkuannya dan menyelipkan pena ke pinggir sampul."
            harumi "Kebanyakan orang langsung buru-buru mencari topik basa-basi kalau suasana hening lebih dari sepuluh detik. Aku sering bingung harus membalas apa waktu orang memaksa mengisi kekosongan. Aku senang kamu tidak merasa harus melakukan itu."
            chiasa "Kalau dipaksa cari bahan ngobrol terus kan malah capek, Senpai. Kadang duduk saja sambil minum hangat sudah cukup."
            harumi "Benar. Dan satu hal lagi sebagai klarifikasi di awal... kalau sebentar lagi aku hanya diam meminum tehku sampai habis, itu artinya aku sedang merasa nyaman duduk di sini. Jangan mengira aku bosan atau ingin kamu pergi."
            chiasa "Hehe, iya, aku paham kok, Senpai. Aku juga nggak bakal pergi dulu sampai tekonya habis."
            nar "Harumi mengangguk puas, lalu mengangkat cangkir keramik putihnya dan menyesap teh hangat itu perlahan. Ketika cangkir kalian sama-sama menyusut, kamu mengangkat teko untuk menuangkan seduhan kedua."
            harumi "Terima kasih, Amamiya-san. Suhu tehnya sekarang jauh lebih pas."
            chiasa "Sama-sama, Senpai."
            nar "Kalian berdua kembali menikmati keheningan serambi malam ditemani suara angin yang melewati dahan pinus sampai teko di meja kosong."
        else:
            nar "Kamu tidak mengintip lebih jauh ke dalam catatannya. Kamu menarik kursi kayu di sebelahnya, mengambil cangkir cadangan di samping teko, lalu menuangkan teh hangat untuk dirimu sendiri sambil menyandarkan punggung."
            yutaka "Ikut minta secangkir ya, Kujo-san. Lumayan buat menghangatkan tenggorokan."
            harumi "Silakan, Kisaragi-kun. Memang sudah kubawa dua cangkir dari dapur."
            nar "Kamu menyesap teh panggang hangat itu pelan sambil memandang bayangan dahan pohon yang bergerak di luar jendela."
            harumi "...Kamu tidak merasa canggung duduk diam tanpa mengobrol seperti ini, Kisaragi-kun?"
            yutaka "Nggak lah, Kujo-san. Telingaku baru aja panas dengar anak-anak teriak main kartu di depan, duduk tenang di sini jauh lebih mendingan."
            nar "Harumi memperhatikan wajahmu sejenak, lalu menutup buku catatan hitamnya dan meletakkan penanya di atas meja."
            harumi "Biasanya orang akan langsung gelisah dan melempar pertanyaan acak kalau lawan bicaranya diam. Jarang ada yang bisa duduk tenang tanpa menuntut percakapan."
            yutaka "Ngobrol kan nggak harus dipaksain terus setiap menit. Kalau lagi sama-sama capek, diam justru lebih santai."
            harumi "Aku setuju. Kalau begitu aku ingin memastikan satu hal dulu... selama aku duduk diam menghabiskan teh ini, aku sama sekali tidak sedang merasa bosan. Aku perlu mengatakan itu di awal supaya kamu tidak salah paham lalu beranjak pergi."
            yutaka "Siap, sudah kucatat di kepala. Aku juga nggak bakal ke mana-mana kok sampai tehnya habis."
            nar "Harumi mengangguk kecil, lalu mengangkat cangkirnya dan meminum tehnya pelan-pelan. Beberapa menit kemudian, saat cangkirnya tinggal sedikit, kamu menuangkan sisa teh dari teko ke cangkirnya lebih dulu sebelum mengisi punyamu."
            harumi "Terima kasih, Kisaragi-kun. Aroma teh panggangnya ternyata makin enak kalau diminum pelan."
            yutaka "Cocok sekali buat udara malam vila begini."
            nar "Sisa malam di serambi itu berlalu tanpa ketergesaan, hanya ditemani angin malam yang menggoyangkan dahan pinus di luar kaca."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kamu menggeser kursimu sedikit lebih dekat ke samping meja bundar dan melirik halaman yang masih terbuka di pangkuannya."
            chiasa "Memangnya kalimat mana yang lagi Kujo-senpai catat di halaman itu? Boleh aku tahu nggak?"
            nar "Ujung jari Harumi sempat menahan tepi halaman bukunya, lalu ia memiringkan buku itu sedikit agar kamu bisa melihat daftar singkat dengan tulisan tangan yang sangat rapi di dalamnya."
            harumi "Aku mencoba mencatat pola kapan seseorang merasa senang saat mengobrol denganku. Untuk anggota kelompok belajar yang lain, polanya cukup mudah ditebak. Kalau aku membantu menjelaskan rumus atau meminjamkan catatan, reaksi mereka selalu seragam."
            chiasa "Terus kalau soal obrolan kita tadi siang, kenapa banyak tanda tanyanya, Senpai?"
            harumi "Untuk beberapa percakapan denganmu belakangan ini, aku kesulitan menarik kesimpulan. Kadang kamu menanggapi dengan bercanda, kadang serius sekali, dan aku tidak yakin bagian mana yang tulus."
            chiasa "Eh, aku kelihatan susah ditebak ya? Padahal aku nggak bermaksud bikin Senpai bingung lho."
            harumi "Kamu tidak berbuat salah, Amamiya-san. Hanya saja kemampuan membaca isyarat sosialku memang kurang peka dibanding orang lain."
            chiasa "Kalau Senpai penasaran aku lagi nyaman atau nggak waktu ngobrol, kenapa nggak langsung ditanyakan ke akunya aja waktu itu?"
            nar "Harumi memutar batang penanya pelan di antara jari-jarinya sambil menunduk memandangi lembaran kertasnya."
            harumi "Tadinya kupikir kalau kuamati dan kucatat sendiri dulu, aku tidak perlu menanyakan hal canggung yang berisiko membuatmu merasa aneh. Tapi ternyata menulisnya sendirian di sini tidak menghasilkan jawaban pasti."
            nar "Ia mengangkat wajahnya dan menatapmu lurus dari balik lensa kacamatanya."
            harumi "Kalau begitu aku gunakan saranmu sekarang. Amamiya-san, malam ini kamu berjalan ke sudut belakang ini karena memang ingin duduk mengobrol denganku, atau hanya kebetulan lewat mau mengambil teh hangat? Dua-duanya boleh, aku hanya butuh data yang sebenarnya."
            chiasa "Tadinya memang mau cari tempat tenang jauh dari suara televisi. Tapi begitu lihat Kujo-senpai duduk sendiri di sini, aku mampir karena pengin menemani Senpai. Tehnya juga kelihatan enak sih."
            nar "Harumi terdiam sejenak seolah mencatat jawaban itu di kepalanya, lalu bahunya sedikit mengendur."
            harumi "...Berarti kombinasi keduanya, dengan prioritas ingin menemani. Terima kasih, Amamiya-san. Jawaban langsung seperti itu jauh lebih mudah kupahami daripada menebak dari nada suara. Silakan ambil cangkirnya, tehnya masih hangat."
            chiasa "Terima kasih, Senpai. Nah, kalau besok ada yang bikin bingung lagi, tanya langsung saja ya."
            harumi "Baik. Aku akan mencoba metode itu."
        else:
            nar "Kamu menarik kursi sedikit lebih dekat dan menunjuk buku catatan bersampul hitam di pangkuannya dengan dagu."
            yutaka "Memangnya bagian obrolan mana yang lagi kamu tulis sampai penuh tanda tanya begitu, Kujo-san? Boleh tahu nggak?"
            nar "Harumi ragu sejenak, lalu memiringkan bukunya sedikit ke arahmu hingga deretan catatan waktu yang sangat rapi terlihat di bawah lampu kuning."
            harumi "Aku mencatat indikator kapan lawan bicara merasa nyaman saat berbicara denganku. Untuk percakapan akademik di perpustakaan, variabelnya sangat jelas. Tapi untuk beberapa obrolan santai denganmu akhir-akhir ini, polanya sulit kubaca."
            yutaka "Sulit dibaca gimana? Perasaan aku kalau ngomong lumayan blak-blakan."
            harumi "Justru karena nada bicaramu sering terdengar santai untuk hal yang serius maupun hal yang sepele, aku tidak yakin kapan kamu benar-benar senang mengobrol denganku dan kapan kamu hanya sedang mengisi waktu luang."
            yutaka "Wah, berarti pembawaanku yang santai malah bikin kamu mikir keras ya?"
            harumi "Bukan salahmu, Kisaragi-kun. Aku memang selalu lebih lambat menangkap candaan halus dibanding teman-teman lain."
            yutaka "Kalau kamu penasaran soal itu, kenapa nggak langsung tanya ke orangnya aja daripada pusing bikin tabel sendiri di pojokan?"
            nar "Harumi merapatkan penanya ke buku, terdiam dua detik sambil memikirkan usulanmu."
            harumi "Aku mengira kalau kuanalisis sendiri dulu, aku bisa menghindari pertanyaan langsung yang membuat suasana jadi kaku. Tapi sepertinya metodenya memang kurang efektif."
            nar "Ia mendongak dan menatap matamu lurus-lurus dengan keseriusan penuh."
            harumi "Kalau begitu aku tanyakan langsung sekarang. Kisaragi-kun, malam ini kamu menghampiri mejaku karena memang ingin duduk bersamaku, atau cuma kebetulan lewat mencari minuman hangat? Kamu boleh jawab jujur, aku tidak akan tersinggung."
            yutaka "Awalnya memang mau cari angin biar telinga istirahat sebentar. Tapi begitu lihat kamu duduk sendirian di sini, aku mampir karena memang pengin ngobrol sama kamu. Sekalian minta tehnya satu cangkir."
            nar "Harumi mengedip sekali, lalu sudut bibirnya melengkung halus dengan lega."
            harumi "...Berarti niat utamanya memang ingin mengobrol denganku. Baiklah, data itu sangat jelas dan tidak membingungkan sama sekali. Silakan duduk, Kisaragi-kun, kubantu tuangkan tehnya."
            yutaka "Makasih, Kujo-san. Lain kali langsung tanya aja ya, nggak usah repot bikin catatan jam segala."
            harumi "Baik. Aku akan mengingat saranmu."
    else:
        if kk_host == "chiasa":
            nar "Kamu menarik kursi di sebelahnya dan menuang teh hangat ke cangkir cadangan, tanpa melirik sedikit pun ke arah buku catatan di pangkuannya."
            chiasa "Kujo-senpai, boleh nggak aku ikut menumpang duduk di sini sebentar? Jujur aja, kepalaku dari tadi agak penuh."
            harumi "Penuh karena perjalanan dari stasiun tadi?"
            chiasa "Bukan cuma perjalanannya sih. Seru banget memang main seharian di pantai sama anak-anak, terus malamnya kumpul di ruang tengah. Cuma kadang kalau dikelilingi suasana seramai itu terus dari pagi tanpa jeda, aku ngerasa tenagaku cepat banget habis. Harus terus ikut ketawa dan menanggapi obrolan padahal sebenarnya pengin diam lima menit aja."
            nar "Harumi yang tadinya masih memegang pena di atas kertas perlahan menurunkan tangannya. Ia menoleh menatapmu dengan alis sedikit terangkat."
            harumi "Kamu menceritakan perasaanmu duluan kepadaku, Amamiya-san? Padahal aku belum mengajukan pertanyaan satu pun."
            chiasa "Memangnya nggak boleh cerita duluan kalau belum ditanya, Kujo-senpai?"
            harumi "Bukan tidak boleh. Hanya saja, biasanya orang baru mau menceritakan hal pribadi kalau mereka ingin menuntutku bercerita balik, atau sedang mengharapkan pujian tertentu dariku."
            chiasa "Aku nggak minta Senpai cerita balik kok. Cuma lagi pengin berbagi cerita aja mumpung di sini tenang dan rasanya enak diajak bicara tanpa harus pasang wajah heboh."
            harumi "Percakapan yang tidak terasa seperti transaksi pertukaran data... rasanya agak asing, tapi justru menenangkan."
            nar "Harumi menutup buku catatannya dan meletakkannya di samping teko. Ia menangkupkan kedua tangannya di sekitar cangkir tehnya, menyimak dengan sungguh-sungguh."
            chiasa "Waktu baru masuk kuliah kemarin juga rasanya mirip begitu, Senpai. Semua orang kelihatan cepat banget akrab, sedangkan kadang aku cuma pengin cari satu bangku pojok yang sepi buat menarik napas sebentar sebelum lanjut kelas berikutnya."
            harumi "Aku mengerti bagian itu. Di laboratorium pun kadang aku sengaja tinggal dua puluh menit lebih lama setelah praktikum selesai, hanya supaya bisa merapikan alat tanpa harus menjawab pertanyaan siapa pun."
            chiasa "Wah, ternyata Kujo-senpai juga suka cari jam sepi kayak gitu ya."
            harumi "Tadi waktu kamu cerita soal rasa lelah di tengah keramaian, ada satu bagian yang mirip sekali dengan yang sering kurasakan di kampus. Besok pagi sebelum kita pulang dari vila, boleh aku menanyakan bagian itu lebih lanjut?"
            chiasa "Boleh banget, Kujo-senpai. Kapan aja Senpai mau bahas, sambil sarapan atau di kereta pulang juga boleh."
            harumi "Terima kasih, Amamiya-san. Malam ini aku mendapat bahan pemikiran yang sangat berharga."
        else:
            nar "Kamu duduk di kursi sebelahnya sambil memeluk cangkir teh hangat, tanpa mengorek apa yang sedang ia tulis di bukunya."
            yutaka "Numpang menepi di sini sebentar ya, Kujo-san. Kepala rasanya agak penuh habis ramai-ramai seharian."
            harumi "Kamu lelah karena jalan di pantai tadi?"
            yutaka "Bukan cuma capek fisik sih. Kumpul bareng rombongan dari pagi sampai malam itu memang seru, tapi ada titik tertentu waktu suara tawa sama obrolan di sekeliling malah bikin kepala pengin sepi sebentar. Enak aja rasanya bisa duduk di pojok sini tanpa harus terus pasang wajah santai dan menanggapi semua orang."
            nar "Harumi menurunkan penanya dari atas halaman kertas dan menatapmu dengan raut sedikit terkejut."
            harumi "Kamu bercerita duluan tentang dirimu, Kisaragi-kun? Padahal aku belum menanyakan apa-apa."
            yutaka "Kenapa memangnya? Nggak boleh cerita duluan?"
            harumi "Bukan tidak boleh. Selama ini kalau ada teman kampus yang tiba-tiba bercerita panjang kepadaku, biasanya ujung-ujungnya mereka ingin meminjam catatan atau menuntutku membuka cerita pribadiku sebagai gantinya."
            yutaka "Aku nggak lagi mau pinjam catatan ataupun nagih cerita balik kok. Cuma lagi pengin ngobrol santai aja mumpung di sini tenang."
            harumi "Obrolan yang tidak menuntut timbal balik langsung seperti itu... cukup jarang kualami. Rasanya hangat."
            nar "Ia menutup buku catatan hitamnya, menaruhnya ke atas meja, lalu memusatkan perhatiannya kepadamu."
            yutaka "Lagian sejak awal kuliah di Kouseikan, orang-orang sering mengira kalau aku selalu betah di tempat ramai. Padahal kadang duduk sendirian di teras sambil pegang minuman hangat itu jauh lebih menyegarkan kepala."
            harumi "Aku bisa memahami perasaan itu. Setelah praktikum selesai pun aku sering sengaja menunda pulang sepuluh menit di ruang alat supaya bisa membereskan catatan dalam sunyi."
            yutaka "Ternyata cara kita cari tempat istirahat mirip juga ya, Kujo-san."
            harumi "Ada satu kalimatmu tadi tentang rasa sepi di tengah keramaian yang masih ingin kupikirkan malam ini, Kisaragi-kun. Lain kali waktu kita bertemu di kampus, boleh aku bertanya soal itu lagi?"
            yutaka "Tentu aja boleh, Kujo-san. Tanya aja kapan pun."
            harumi "Baiklah. Terima kasih untuk malam ini, Kisaragi-kun."
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
    if kk_host == "chiasa":
        nar "Lantai dua Perpustakaan Pusat sore itu cukup tenang. Kamu sedang duduk di meja baca dekat jendela besar menemani Harumi yang sejak setengah jam lalu sibuk menyalin data pembanding dari tiga jurnal kimia organik untuk lampiran laporan praktikumnya."
        nar "Ketika Harumi mulai menyusun lembaran kertas grafiknya ke dalam map bening, langkah sepatu kulit yang teratur berhenti tepat di sisi meja kalian. Seorang pria akhir dua puluhan berjas laboratorium putih bersih dengan rambut hitam tersisir klimis berdiri di sana sambil tersenyum sopan."
        "Ogawa" "Kujo-san, masih di perpustakaan ternyata. Tadi waktu aku lewat ruang timbang di laboratorium, aku sempat membaca draf tabel katalis yang kamu tinggalkan di meja kerjamu."
        nar "Harumi langsung menegakkan duduknya dan merapikan letak kacamatanya."
        harumi "Ogawa-senpai? Maaf, tadi saya hanya meninggalkan meja sebentar untuk mencari referensi pembanding di sini, jadi drafnya belum sempat saya masukkan ke laci."
        "Ogawa" "Justru beruntung aku sempat membacanya. Koreksi batas galat pada tabel ketigamu itu sangat tajam, Kujo-san. Kebanyakan mahasiswa tahun kedua selalu mengabaikan fluktuasi suhu ruang pada tahap titrasi tersebut, bahkan beberapa asisten peneliti tahun keempat pun jarang menyadarinya."
        nar "Pujian yang langsung menunjuk detail perhitungan teknis itu jelas menyentuh bagian kerja keras Harumi yang jarang diperhatikan orang. Sorot mata Harumi di balik lensa kacamatanya tampak berbinar senang."
        harumi "...Terima kasih banyak, Ogawa-senpai. Saya memang mengulang pengukuran suhu ruangnya tiga kali kemarin sore karena kurva awalnya terlihat sedikit melenceng."
        "Ogawa" "Ketelitian seperti milikmu ini terlalu sayang kalau hanya dipakai mengerjakan modul praktikum standar kelas, Kujo-san. Kebetulan semester depan aku sedang menyiapkan sub-proyek publikasi mandiri. Kalau kamu ingin berkembang lebih cepat, kita bisa mengadakan sesi bimbingan khusus di luar jam laboratorium reguler. Biar aku yang membimbingmu secara pribadi."
        nar "Dari kursimu di seberang meja, kamu memperhatikan cara pria itu berdiri. Meskipun kata-katanya terdengar seperti senior yang murah hati, tubuhnya sedikit condong memayungi kursi Harumi dan ia sama sekali tidak menoleh ataupun menganggap kehadiranmu di meja yang sama."
        harumi "Saya sangat menghargai tawaran itu, Ogawa-senpai. Sebelum menyanggupi, saya perlu mengetahui rincian bentuk bimbingannya terlebih dahulu. Apakah sesi itu dilakukan di ruang laboratorium utama, pukul berapa jadwalnya, dan apakah sudah tercatat dalam daftar bimbingan Prof. Mizuhara?"
        "Ogawa" "Ah, urusan administrasi seperti itu gampang sekali diatur belakangan. Di dunia riset tingkat lanjut, hal paling mendasar itu rasa saling percaya antara peneliti senior dan juniornya dulu. Kalau kita sudah cocok bekerja berdua, akses ke instrumen utama maupun surat rekomendasi untukmu nanti tinggal mengikuti."
        nar "Ogawa mengeluarkan ponsel dari saku jasnya, melirik layar sebentar, lalu kembali tersenyum tenang kepada Harumi."
        "Ogawa" "Nanti malam kukirimkan jadwal kosongku untuk akhir pekan ini lewat pesan pribadi ya, Kujo-san. Kamu pikirkan saja dulu malam ini."
        nar "Pria itu hanya mengangguk sekilas tanpa menatapmu, lalu melangkah pergi menyusuri lorong rak buku. Setelah langkah sepatunya menghilang di tangga turun, Harumi memandang map plastiknya sejenak lalu menoleh kepadamu."
        harumi "Amamiya-san, barusan itu Ogawa Masato, kandidat doktor senior di laboratorium kimia kami. Menurut pengamatanmu, apakah tawaran bimbingan di luar jam resmi seperti tadi itu prosedur yang wajar di universitas?"
    else:
        nar "Lantai dua Perpustakaan Pusat sore itu cukup lengang. Kamu duduk di seberang Harumi sambil mengerjakan rangkuman kuliahmu sendiri, sementara Harumi dengan teliti menyalin tabel dari tumpukan jurnal kimia organik ke lembar data risetnya."
        nar "Tepat saat Harumi merapikan kertas terakhirnya ke dalam map, seorang pria berusia akhir dua puluhan dengan jas laboratorium putih rapi dan rambut hitam tersisir licin berhenti di samping meja kalian. Senyumnya tampak ramah dan sangat terukur."
        "Ogawa" "Kujo-san, ternyata kamu ada di sini. Tadi waktu di laboratorium aku sempat melihat draf perhitungan katalis yang kamu taruh di atas meja kerja."
        nar "Harumi segera menegakkan punggungnya, tampak sedikit terkejut."
        harumi "Ogawa-senpai? Maaf, tadi saya belum sempat menyimpannya ke dalam loker karena harus mengambil jurnal referensi ke perpustakaan."
        "Ogawa" "Justru bagus aku sempat melihatnya. Perhitungan koreksi margin galat di tabel ketigamu itu luar biasa rapi, Kujo-san. Mahasiswa tahun kedua biasanya tidak pernah memperhitungkan penyimpangan suhu ruang pada tahap tersebut, bahkan asisten lab pun sering kelewatan."
        nar "Mendengar bagian tersulit dari perhitungannya dikenali secara spesifik, mata Harumi sedikit melebar di balik kacamatanya dan raut wajahnya tampak senang."
        harumi "...Terima kasih, Ogawa-senpai. Kemarin saya memang mengulang pengukuran suhunya sampai tiga kali supaya datanya tidak bias."
        "Ogawa" "Kemampuan analisis sepertimu ini bakal terbuang percuma kalau cuma mengikuti jadwal praktikum biasa, Kujo-san. Kalau kamu mau melangkah lebih cepat dan ikut masuk ke proyek publikasi jurnal tahun depan, kita bisa adakan diskusi dan bimbingan khusus di luar jam laboratorium biasa. Aku bersedia membimbingmu langsung."
        nar "Kamu mengamati pria itu dari seberang meja. Nada suaranya halus layaknya senior teladan, tetapi sejak berhenti di meja tadi, tatapannya terus mengunci Harumi dan sama sekali mengabaikan keberadaanmu di depannya."
        harumi "Terima kasih atas tawarannya, Ogawa-senpai. Tapi untuk menyesuaikannya dengan jadwal studi saya, saya perlu tahu dulu prosedur bimbingannya seperti apa, di mana lokasinya, dan apakah kegiatan ini berada di bawah sepengetahuan Prof. Mizuhara."
        "Ogawa" "Hal-hal teknis semacam itu bisa diatur kapan saja belakangan. Dalam kelompok riset, yang paling menentukan itu hubungan saling percaya antara senior dan juniornya lebih dulu. Kalau kita sudah bisa bekerja sama dengan fleksibel, urusan akses data laboratorium dan rekomendasi akademikmu pasti kupastikan aman."
        nar "Ia memeriksa jam tangan peraknya sekilas, lalu tersenyum lagi kepada Harumi."
        "Ogawa" "Nanti malam kukirimkan waktu dan tempat pertemuannya lewat pesan ya, Kujo-san. Silakan dipertimbangkan dulu."
        nar "Ogawa berbalik tanpa menyapamu dan berjalan meninggalkan ruang baca. Begitu punggung berjas putih itu hilang di balik deretan rak, Harumi menoleh ke arahmu dengan kening sedikit berkerut."
        harumi "Kisaragi-kun, pria tadi itu Ogawa Masato, kandidat doktor yang membantu mengawasi laboratorium kami. Menurutmu, apakah ajakan bimbingan khusus di luar jadwal seperti barusan itu hal yang lazim?"
    call kk_family_menu("H06", ["\"Kelihatannya dia beneran merhatiin risetmu, mungkin itu peluang bagus.\"", "\"Tadi kamu nanya soal kerjaan, tapi dia malah muter ke soal kepercayaan.\"", "\"Jangan terima syarat yang kabur begitu cuma gara-gara dipuji atau dijanjikan rekomendasi.\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Kelihatannya dia beneran merhatiin detail tabel riset Kujo-senpai sih tadi. Kalau memang seorang kandidat doktor mau bantu Senpai masuk ke proyek publikasi jurnal lebih cepat, mungkin itu peluang yang bagus buat dicoba."
            nar "Harumi menunduk memandangi map plastik berisi tabel katalisnya. Keraguan kecil yang tadi sempat muncul di keningnya perlahan mereda setelah mendengar pendapatmu."
            harumi "Benar juga. Selama ini di laboratorium jarang ada senior yang mau memeriksa lembar koreksi galat milik mahasiswa tahun kedua sampai serinci itu."
            chiasa "Berarti Senpai mau coba ikut bimbingannya kalau nanti malam dia kirim pesan?"
            harumi "Iya. Kalau tujuannya untuk meningkatkan efisiensi riset dan peluang publikasi, rasanya tidak ada alasan untuk menolak sebelum mencobanya sekali. Nanti malam akan kusiapkan buku data mentahku sebelum dia menghubungi."
            nar "Harumi memasukkan mapnya ke dalam tas dengan gerakan rapi. Malam itu juga, pesan dari Ogawa masuk ke ponselnya berisi ajakan bertemu di luar jam operasional laboratorium, dan karena tidak ada lagi yang mempertanyakan syaratnya, Harumi langsung menyetujui jadwal pertama tersebut."
        else:
            yutaka "Kelihatannya dia beneran paham dan merhatiin hasil hitunganmu sih, Kujo-san. Kalau kandidat doktor di labmu sendiri yang nawarin jalan buat masuk proyek publikasi semester depan, mungkin itu kesempatan bagus buat kariermu."
            nar "Harumi menatap map datanya sejenak, lalu mengangguk pelan. Tanggapan positifmu barusan membuatnya menepikan kejanggalan kecil dari jawaban Ogawa tadi."
            harumi "Masuk akal. Memang tidak setiap hari ada peneliti tingkat doktoral yang bersedia meluangkan waktunya memeriksa draf mahasiswa tahun kedua."
            yutaka "Jadi kalau nanti malam dia kirim jadwalnya, kamu mau ambil?"
            harumi "Iya, aku akan mencobanya lebih dulu. Nanti di asrama kusiapkan salinan tabel pengamatanku supaya diskusinya berjalan efektif."
            nar "Harumi merapikan bukunya ke dalam tas. Malam harinya, Ogawa langsung mengirimkan jam pertemuan pertama di luar jadwal resmi laboratorium, membuka langkah awal bimbingan tanpa pernah menjawab pertanyaan soal izin Prof. Mizuhara."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Aku memang nggak paham soal aturan laboratorium kimia sih, Kujo-senpai. Cuma tadi waktu dengar kalian ngobrol dari seberang meja, ada satu hal yang kedengaran agak ganjil di telingaku."
            harumi "Bagian mana yang terdengar ganjil, Amamiya-san?"
            chiasa "Tadi kan Senpai nanya tiga hal yang jelas banget soal pekerjaan, mulai dari bentuk bimbingannya gimana, lokasinya di mana, sama apakah Prof. Mizuhara tahu. Tapi Ogawa-senpai itu nggak jawab satu pun dari tiga pertanyaan tadi, malah muter balik bahas soal rasa saling percaya sama janji rekomendasi."
            nar "Jari Harumi berhenti di atas penutup mapnya. Ia terdiam beberapa detik, memutar ulang kalimat demi kalimat yang baru saja diucapkan Ogawa di dalam kepalanya."
            harumi "...Pengamatanmu tepat sekali. Aku mengajukan pertanyaan tentang parameter teknis dan prosedur resmi, tetapi dia menjawabnya dengan variabel abstrak soal kepercayaan pribadi. Secara logika, jawaban itu sama sekali tidak menjawab pertanyaanku."
            chiasa "Aku nggak bilang dia pasti berniat buruk sih, Senpai. Tapi sebelum Senpai iyain ajakannya malam ini, lebih aman kalau Senpai minta dia tulis jelas dulu jadwal dan izin dosennya."
            harumi "Setuju. Kalau bimbingan itu memang kegiatan akademik yang wajar, seharusnya dia tidak keberatan memberikan rincian tertulis dan menyertakan persetujuan Prof. Mizuhara. Aku tidak perlu langsung menuduhnya orang jahat, tapi aku wajib memeriksa kejelasannya dulu. Terima kasih sudah memperhatikan celah itu, Amamiya-san."
            nar "Harumi membuka buku catatan kecilnya dan menuliskan tiga poin verifikasi yang harus dijawab Ogawa sebelum ia bersedia datang ke pertemuan mana pun."
        else:
            yutaka "Aku memang bukan anak laboratorium sains sih, Kujo-san. Tapi dari caranya menjawab pertanyaanmu barusan, ada bagian yang kelihatan nggak beres menurutku."
            harumi "Bagian mana yang tidak beres menurutmu, Kisaragi-kun?"
            yutaka "Coba kamu ingat-ingat lagi. Kamu tanya tiga hal yang sangat teknis, yaitu bentuk bimbingannya apa, jadwalnya kapan, dan apakah Prof. Mizuhara tahu. Dia sama sekali nggak menjawab satu pun dari ketiganya, malah langsung ngeles bahas rasa saling percaya sama iming-iming akses lab."
            nar "Harumi terdiam di kursinya. Ujung jarinya mengetuk pelan permukaan map plastik sambil menimbang ulang struktur percakapan barusan."
            harumi "...Kamu benar. Aku menanyakan prosedur kerja yang konkret, sedangkan dia mengalihkan jawaban ke tuntutan kepercayaan personal. Kedua hal itu tidak nyambung."
            yutaka "Aku nggak langsung nuduh dia mau berbuat jahat juga sih. Cuma kalau bimbingannya memang bersih, harusnya dia nggak perlu ngeles waktu kamu bawa-bawa nama dosen pembimbingmu."
            harumi "Iya. Aku bisa membalas pesannya nanti malam dengan meminta rincian agenda tertulis serta konfirmasi ke Prof. Mizuhara lebih dulu, tanpa perlu buru-buru menyimpulkan niatnya sekarang. Terima kasih sudah menangkap ketidaksinkronan itu, Kisaragi-kun."
            nar "Harumi mencatat poin tersebut di buku sakunya, mengubah tawaran yang tadinya tampak seperti pujian membanggakan menjadi sesuatu yang harus diuji ulang."
    else:
        if kk_host == "chiasa":
            chiasa "Kujo-senpai, jujur aja aku sama sekali nggak suka lihat gelagat Ogawa-senpai tadi. Tolong jangan mau terima ajakan ketemu di luar jam lab yang syaratnya kabur begitu, cuma gara-gara dia muji tabel Senpai atau janjiin surat rekomendasi."
            nar "Nada suaramu yang serius dan tegas membuat Harumi menatapmu lekat-lekat. Ia tidak tampak marah, melainkan membetulkan kacamatanya dan mendengarkan dengan penuh perhatian."
            harumi "Kamu memperingatkanku dengan sangat tegas, Amamiya-san. Aku percaya kekhawatiranmu itu tulus."
            chiasa "Habisnya kelihatan banget dia sengaja nutupin soal Prof. Mizuhara tadi, Senpai."
            harumi "Poin soal Prof. Mizuhara itu memang benar. Tapi... boleh aku minta satu hal padamu? Tolong jabarkan urutan tanda-tanda yang membuatmu langsung curiga padanya barusan. Aku ingin mempelajari polanya supaya bisa mengenalinya sendiri tanpa cuma memindahkan kepatuhanku dari Ogawa-senpai ke perintahmu."
            chiasa "Iya, Senpai, masuk akal kok. Pertama, dia buka obrolan pakai pujian yang sangat spesifik soal bagian tabel yang bikin Senpai bangga, supaya pertahanan Senpai langsung turun."
            harumi "Validasi awal untuk menurunkan kewaspadaan. Lalu yang kedua?"
            chiasa "Kedua, waktu Senpai minta kejelasan aturan dan nama dosen pembimbing, dia anggap itu cuma urusan sepele yang bisa diatur belakangan. Dan ketiga, dia langsung mengaitkan kesediaan Senpai menuruti kemauannya secara pribadi dengan akses alat serta rekomendasi masa depan."
            harumi "...Pujian spesifik, pengaburan prosedur resmi, lalu mengikat masa depan akademik pada kepatuhan pribadi. Kalau diuraikan menjadi tiga tahap seperti itu, polanya terlihat sangat berbahaya."
            chiasa "Nah, makanya kalau semua syaratnya belum tertulis resmi di papan laboratorium, jangan pernah mau ketemu sendirian, Senpai."
            harumi "Aku mengerti sepenuhnya sekarang. Terima kasih sudah mengajariku cara membaca tandanya, Amamiya-san."
        else:
            yutaka "Kujo-san, terus terang aja aku nggak suka cara senior labmu itu ngomong tadi. Jangan sampai kamu mau diajak ketemuan di luar jam resmi dengan syarat kabur begitu cuma gara-gara dia muji risetmu atau bawa-bawa janji rekomendasi."
            nar "Mendengar peringatanmu yang tanpa tedeng aling-aling, Harumi menatapmu serius dari balik kacamatanya."
            harumi "Nada bicaramu tegas sekali, Kisaragi-kun. Aku tahu kamu mengatakan itu karena mengkhawatirkanku."
            yutaka "Habisnya gelagat orang itu waktu kamu sebut nama Prof. Mizuhara tadi jelas banget lagi cari celah."
            harumi "Soal dia menghindari nama Prof. Mizuhara itu memang ganjil. Tapi... tolong jelaskan kepadaku bagian mana saja dari ucapannya tadi yang menjadi indikator bahaya menurutmu. Aku ingin belajar memahami polanya sendiri, supaya aku tidak cuma memindahkan ketergantungan keputusanku dari dia kepadamu."
            yutaka "Permintaan yang adil. Pertama, dia masuk pakai pujian yang super spesifik soal kerja kerasmu di tabel ketiga, supaya kamu langsung merasa cuma dia yang paham bakatmu."
            harumi "Memberikan pengakuan spesifik untuk membangun kepercayaan cepat. Lalu indikator keduanya?"
            yutaka "Kedua, begitu kamu minta batas yang jelas soal lokasi, jam, dan izin dosen pembimbing, dia langsung meremehkan itu sebagai urusan teknis belakangan. Dan ketiga, dia langsung menggantungkan akses alat lab sama rekomendasi publikasimu pada seberapa patuh kamu ikut cara kerjanya di luar jadwal."
            harumi "...Ketika dipecah menjadi tiga variabel seperti itu, struktur manipulasinya langsung kelihatan sangat jelas. Kalau bimbingannya memang resmi, rekomendasi tidak mungkin dijadikan alat tawar-menawar pribadi."
            yutaka "Persis. Jadi kalau dia nggak berani bicara di depan Prof. Mizuhara, jangan pernah diladeni."
            harumi "Paham. Sekarang aku tahu persis apa yang harus kuperiksa. Terima kasih banyak, Kisaragi-kun."
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
    if kk_host == "chiasa":
        nar "Menjelang libur Natal, lantai dua Perpustakaan Pusat sudah jauh lebih sepi daripada minggu ujian. Sebagian besar meja baca kayu kosong, sementara beberapa mahasiswa yang masih tersisa di dekat tangga sibuk berbisik membicarakan rencana makan malam atau pertukaran kado di pusat kota."
        nar "Di meja paling ujung dekat rak referensi kimia, Kujo Harumi berdiri sambil merapikan dua jilid buku tebal dan buku catatan pengamatannya yang bersampul hitam. Lima belas menit lalu, ketika grup pesan singkat ramai oleh kiriman foto pohon Natal dan kue dari kafe stasiun, Harumi membalas ucapan selamat Natal teman-temannya hanya dengan mengirim foto lembar tabel pencatatan suhu larutan dari laboratorium."
        chiasa "Kujo-senpai belum pulang juga? Tadi kulihat foto yang Senpai kirim di grup, habis dari perpustakaan ini Senpai masih mau balik ke gedung laboratorium?"
        nar "Harumi menaikkan letak kacamatanya dengan ujung telunjuk, lalu memasukkan penggaris logam ke dalam saku mapnya."
        harumi "Amamiya-san. Iya, aku cuma mampir dua puluh menit ke perpustakaan buat mencocokkan tabel indeks bias dari jurnal lama. Sampel katalis yang sedang kupantau di laboratorium butuh pencatatan suhu setiap dua jam sekali."
        chiasa "Hari ini kan sudah mulai libur Natal, Senpai. Memangnya nggak bisa dilanjutin habis tahun baru aja?"
        harumi "Reaksi kimia tidak membaca kalender akademik, Amamiya-san. Kalau pemanas inkubatornya kumatikan sekarang, seluruh larutan yang sudah kutumbuhkan sejak hari Selasa harus diulang dari nol. Jadi aku sudah menyusun jadwal pengamatan sampai pukul sepuluh malam nanti."
        chiasa "Sampai jam sepuluh malam? Sendirian di laboratorium?"
        harumi "Petugas keamanan gedung masih berjaga di pos lantai satu, tapi anggota lab yang lain memang sudah izin pulang sejak siang tadi. Itu jawaban berdasarkan jadwal kerjaku."
        nar "Harumi memeluk kedua jilid buku referensi itu ke dadanya. Pandangannya turun sejenak ke sampul buku catatan hitamnya."
        harumi "Kalau pertanyaan apakah aku memang lebih suka berada di laboratorium sendirian daripada di tempat lain malam ini... bagian itu sengaja tidak kutanyakan ke diriku sendiri. Kalau terlalu dipikirkan, biasanya konsentrasiku saat membaca angka ukur malah terganggu."
    else:
        nar "Menjelang libur Natal, lantai dua Perpustakaan Pusat tampak jauh lebih lengang daripada biasanya. Hanya tersisa beberapa mahasiswa di meja dekat tangga yang sesekali berbisik membahas rencana makan malam dan belanja di sekitar stasiun."
        nar "Di sudut tenang dekat deretan rak jurnal kimia, Kujo Harumi sedang membereskan dua buku referensi tebal bersama buku catatan pengamatannya yang bersampul hitam. Baru lima belas menit lalu, saat grup pesan singkat teman-teman angkatan penuh dengan foto pohon Natal dan kue kafe, Harumi membalas ucapan selamat Natal hanya dengan mengirim foto lembar tabel pencatatan suhu larutan dari laboratorium."
        yutaka "Di grup dari tadi orang-orang kirim foto kue sama lampu jalan, cuma kamu yang ngirim tabel suhu larutan, Kujo-san. Habis dari perpustakaan ini kamu masih mau balik ke gedung lab?"
        nar "Harumi membetulkan letak kacamatanya dengan ujung jari telunjuk, lalu memasukkan penggaris logam kecil ke dalam map plastiknya."
        harumi "Kisaragi-kun. Iya, aku cuma mampir sebentar ke sini buat mencocokkan kurva indeks bias di jurnal lama. Sampel katalis yang sedang kuamati di laboratorium perlu dicatat suhunya setiap dua jam sekali."
        yutaka "Ini sudah masuk libur Natal lho. Memangnya nggak bisa dihentikan dulu terus dilanjut habis tahun baru?"
        harumi "Reaksi kimia tidak membaca kalender libur kampus, Kisaragi-kun. Kalau pemanas inkubatornya kumatikan hari ini, seluruh larutan yang sudah kutumbuhkan sejak Selasa lalu bakal gagal dan harus diulang dari awal. Jadi jadwalku di laboratorium masih berjalan sampai pukul sepuluh malam nanti."
        yutaka "Sampai jam sepuluh malam? Di gedung yang sudah kosong sendirian begitu?"
        harumi "Petugas keamanan masih berjaga di lantai bawah, tapi anggota lab yang lain memang sudah izin pulang sejak siang. Itu jawaban berdasarkan jadwalku."
        nar "Harumi memeluk kedua buku referensinya ke dada. Matanya sempat turun sebentar ke sampul buku catatan hitamnya sebelum kembali menatapmu."
        harumi "Kalau pertanyaan tentang apakah aku memang ingin menghabiskan malam Natal sendirian di laboratorium... bagian itu sengaja belum kutanyakan ke diriku sendiri. Kalau dipikirkan sekarang, biasanya akurasi pembacaan angkaku malah turun."
    call kk_family_menu("H07", ["\"Kalau boleh, aku ikut ke gedung lab ya. Aku tunggu di ruang baca luar sampai selesai.\"", "\"Jangan lupa makan malam. Nanti kukirim makanan hangat ke depan gedung lab ya.\"", "\"Oh, masih lanjut praktikum ya. Ya sudah, semangat ya di lab.\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Kalau boleh, aku ikut jalan ke gedung laboratorium sekarang ya, Kujo-senpai. Aku nggak bakal masuk ke ruang reaksi kok, aku duduk nunggu di ruang baca luar aja sambil gambar sketsa sampai jadwal pengamatan Senpai selesai."
            nar "Harumi terdiam di samping meja kayu. Selama beberapa detik ia menatapmu dari balik lensa kacamatanya, seolah sedang memeriksa apakah kalimatmu barusan hanya basa-basi."
            harumi "Kamu mau ikut ke Gedung Sains malam ini, Amamiya-san? Di luar sudah mulai dingin, dan hampir semua mahasiswa lain memilih pergi ke tempat yang ramai."
            chiasa "Tempat yang terlalu ramai malah bikin cepat pusing, Senpai. Lagian di ruang baca luar lab kan ada pemanas sama sofa, enak buat duduk gambar. Nanti tiap Senpai selesai catat suhu, kita bisa ngobrol."
            harumi "...Keputusanmu sama sekali tidak ada di dalam perkiraan awalku hari ini. Tapi harus kuakui, penyimpangan data yang ini membuatku senang."
            nar "Kalian berdua berjalan menyeberangi pelataran kampus yang mulai gelap menuju Gedung Sains. Sesampainya di lantai dua, kamu duduk di sofa ruang istirahat tepat di sebelah dinding kaca laboratorium sambil membuka buku sketsa, sementara Harumi mengenakan jas lab putihnya di dalam dan memeriksa deretan tabung inkubator."
            nar "Sekitar empat puluh lima menit kemudian, pintu geser laboratorium terbuka. Harumi melangkah keluar setelah melepas sarung tangan lateksnya, membawa nampan logam berisi teko kecil dan dua cangkir keramik putih yang mengepulkan aroma teh panggang."
            harumi "Siklus pencatatan ketujuh sudah selesai dan suhunya stabil. Masih ada waktu jeda satu jam lebih sebelum pembacaan terakhir. Silakan diminum, Amamiya-san. Aku menyeduhnya tepat tiga menit."
            chiasa "Wah, harum banget tehnya. Makasih banyak, Kujo-senpai. Di ruang istirahat lab memang selalu sedia dua cangkir begini?"
            harumi "Sebenarnya di lemari penyimpanan ada enam cangkir. Biasanya aku hanya mencuci dan mengeluarkan satu cangkir untukku sendiri, atau sesekali menaruh satu cangkir cadangan di baki karena berpikir mungkin ada asisten lab yang kebetulan lembur."
            nar "Harumi duduk di kursi sebelahmu, meletakkan cangkirnya dengan hati-hati, lalu menoleh menatapmu."
            harumi "Tapi tadi waktu kita baru sampai di sini, aku langsung mencuci dua cangkir sekaligus karena sudah tahu kamu benar-benar duduk menunggu di luar. Ternyata menyiapkan cangkir kedua karena kepastian itu rasanya jauh lebih hangat daripada menyiapkan karena kemungkinan."
            chiasa "Hehe, kalau gitu kapan-kapan kalau Senpai lembur lagi, siapkan dua cangkir aja dari awal."
            harumi "Akan kupertimbangkan sebagai prosedur tetap. Ngomong-ngomong, gambar apa yang sedang kamu buat di buku sketsamu dari tadi?"
            nar "Kamu memperlihatkan sketsa deretan tabung kaca dan lampu meja laboratorium yang baru saja kamu arsir. Harumi mengamatinya dengan serius, mengomentari proporsi tabung ukurnya dengan jujur, lalu mulai bercerita tentang bagaimana suasana rumahnya di Kansai setiap akhir tahun hingga jadwal pengamatan terakhirnya tiba tanpa terasa."
        else:
            yutaka "Kalau nggak mengganggu kerjamu, aku ikut jalan ke Gedung Sains aja sekalian, Kujo-san. Tenang, aku nggak bakal masuk ruang reaksi kok. Aku duduk di ruang istirahat luar aja sambil baca bahan kuliahku sampai kamu selesai."
            nar "Harumi berhenti melangkah di samping meja. Ia menatapmu beberapa detik dari balik lensa kacamatanya untuk memastikan kamu tidak sedang bergurau."
            harumi "Kamu mau ikut menemani di Gedung Sains malam ini, Kisaragi-kun? Padahal hari ini semua orang memilih pergi ke pusat kota atau acara makan malam."
            yutaka "Malas juga kalau harus desak-desakan di dekat stasiun malam begini. Lagian di ruang istirahat depan lab kan pemanasnya hangat dan tenang. Nanti pas jam jedamu, kita bisa ngobrol sebentar biar nggak terlalu sunyi."
            harumi "...Tindakanmu benar-benar menyimpang dari perkiraan awalku hari ini. Tapi harus kuakui, penyimpangan yang ini membuatku senang."
            nar "Kalian berdua melintasi pelataran kampus yang berangin menuju Gedung Sains. Di lantai dua, kamu duduk di sofa ruang baca luar sambil membuka catatan yang kamu bawa, membiarkan Harumi bekerja tenang di balik dinding kaca laboratorium dengan jas putih dan sarung tangan lateksnya."
            nar "Empat puluh lima menit kemudian, pintu geser lab dibuka. Harumi keluar membawa nampan logam berisi teko porselen dan dua cangkir keramik putih yang mengepulkan aroma teh panggang."
            harumi "Pencatatan ketujuh sudah beres dan grafik suhunya stabil. Masih ada jeda lebih dari satu jam sebelum pembacaan terakhir. Silakan diminum, Kisaragi-kun. Aku menyeduhnya tepat tiga menit."
            yutaka "Wanginya enak banget, Kujo-san. Makasih. Memangnya di ruang lab ini selalu sedia dua cangkir di atas baki?"
            harumi "Di lemari penyimpanan ada enam cangkir. Biasanya aku hanya mencuci satu untukku sendiri, atau kadang menaruh satu cangkir cadangan sekadar berjaga-jaga kalau ada asisten lab yang kebetulan lembur."
            nar "Harumi mengambil tempat di kursi sebelahmu, meletakkan cangkirnya dengan gerakan terukur, lalu menoleh kepadamu."
            harumi "Tapi begitu kita tiba tadi, aku langsung mencuci dua cangkir sekaligus karena tahu kamu benar-benar menunggu di sini. Ternyata menyiapkan cangkir kedua karena kepastian rasanya berbeda jauh daripada menyiapkan hanya karena kemungkinan ada orang."
            yutaka "Kalau begitu lain kali kamu harus lembur lagi, kabari aja dari awal biar prosedur dua cangkirnya langsung jalan."
            harumi "Akan kucatat sebagai kebiasaan baru yang efisien. Omong-omong, catatan apa yang kamu baca di sofa tadi?"
            nar "Obrolan kalian mengalir jauh keluar dari urusan laboratorium. Setelah membahas sekilas bacaan kuliahmu, Harumi mulai bercerita tentang bagaimana kedua orang tuanya di Kansai merayakan akhir tahun yang hampir selalu berakhir dengan diskusi makalah di meja makan, sampai jam pengamatan terakhirnya tiba tanpa terasa."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Kalau harus bolak-balik mantau sampel sampai jam sepuluh malam, biasanya Kujo-senpai suka lupa makan malam kan? Nanti kukirim paket makanan hangat ke lobi Gedung Sains ya, biar Senpai nggak cuma ganjal perut pakai biskuit."
            nar "Harumi membetulkan letak kacamatanya, lalu sudut bibirnya yang biasanya lurus tampak melengkung tipis."
            harumi "Ingatanmu soal kebiasaan burukku saat bekerja cukup akurat, Amamiya-san. Tadi aku memang hanya membawa satu bungkus roti gandum di tas. Kalau kamu mau mengirim makanan... kira-kira pukul berapa sampai di lobi?"
            chiasa "Sekitar jam tujuh malam nanti aku minta kurir kedai dekat gerbang antar ke lobi Gedung Sains. Jam segitu pas sama jeda pencatatan Senpai nggak?"
            harumi "Pukul tujuh lewat lima menit adalah jeda tepat setelah pembacaan sampel kedelapan. Aku akan turun ke pintu lobi lantai satu tepat waktu supaya makanannya tidak tertahan di pos satpam dan keburu dingin. Terima kasih, Amamiya-san."
            chiasa "Sama-sama, Senpai. Jangan sampai kelewatan jam makannya ya."
            nar "Malam harinya tepat pukul tujuh lewat seperempat, ponselmu bergetar di meja kamar. Sebuah pesan masuk dari Harumi, dilampiri foto kotak bento kayu berisi nasi hangat, kroket daging, dan mangkuk sup miso yang sudah ditata rapi di meja ruang istirahat laboratorium."
            nar "Di bawah foto tersebut, Harumi menuliskan laporan panjang yang sangat khas dirinya, mengabarkan bahwa makanannya sudah diterima pukul 19.04, suhu supnya masih sekitar enam puluh derajat saat dibuka, lapisan tepung kroketnya masih renyah, dan porsi karbohidratnya sangat pas untuk menjaga fokus sampai pukul sepuluh nanti."
            nar "Baru saja kamu tersenyum membaca ulasan makanan bergaya laporan praktikum itu, satu pesan pendek masuk lagi darinya mengingatkan agar kamu juga tidak lupa makan malam yang hangat di rumah, ditutup ucapan selamat malam Natal."
        else:
            yutaka "Kalau kamu harus mantau inkubator sampai jam sepuluh malam, ujung-ujungnya kamu pasti lupa makan malam lagi kan, Kujo-san? Nanti kukirim makanan hangat ke lobi Gedung Sains ya, jangan cuma ganjal perut pakai roti dingin."
            nar "Harumi menaikkan kacamatanya perlahan, sementara sudut bibirnya terangkat tipis."
            harumi "Tebakanmu soal isi tasku agak terlalu tepat, Kisaragi-kun. Tadi aku memang cuma beli satu bungkus roti kacang merah di minimarket sebelum masuk perpustakaan. Kalau kamu benar-benar mau mengirim makanan, kira-kira pukul berapa diantar?"
            yutaka "Sekitar jam tujuh malam aku minta kedai dekat gerbang depan antar langsung ke lobi Gedung Sains. Jam segitu pas sama waktu jeda labmu nggak?"
            harumi "Pukul tujuh lewat lima menit adalah jeda tepat sesudah pencatatan kedelapan. Aku akan turun ke pintu lobi tepat waktu supaya makanannya langsung kuambil sebelum dingin. Terima kasih, Kisaragi-kun."
            yutaka "Sama-sama. Awas kalau sampai dibiarkan dingin gara-gara keasyikan lihat grafik."
            nar "Malam harinya pukul tujuh lewat dua puluh, ponselmu berdenting di atas meja. Satu pesan masuk dari Harumi disertai foto kotak makan hangat berisi nasi, daging panggang saus jahe, dan semangkuk sup miso yang tertata rapi di meja ruang istirahat laboratorium."
            nar "Di bawah foto itu, Harumi mengetik laporan yang begitu rinci khas gayanya, menyebutkan makanannya diterima pukul 19.03, suhu sup misonya masih hangat saat dibuka, rasa jahenya cukup kuat mengusir hawa dingin koridor, dan porsinya ideal untuk mempertahankan fokus sampai pukul sepuluh nanti."
            nar "Tak sampai semenit setelah kamu membaca pesan itu, satu balasan singkat menyusul lagi mengingatkan agar kamu juga tidak lupa makan malam yang layak di apartemen, disertai ucapan selamat malam Natal."
    else:
        if kk_host == "chiasa":
            chiasa "Oh, masih harus lanjut mantau sampel sampai malam ya, Kujo-senpai. Ya sudah, semangat ya di laboratoriumnya. Aku pulang duluan."
            harumi "Iya. Terima kasih, Amamiya-san. Hati-hati di jalan pulang, udara di luar sudah turun."
            nar "Harumi mengangguk sopan, lalu berbalik menuju lorong tangga turun sambil mendekap buku referensinya. Kamu melangkah keluar dari Perpustakaan Pusat menuju arah gerbang tanpa menoleh lagi."
            nar "Sepanjang sisa malam itu tidak ada pesan baru di antara kalian. Di lantai dua Gedung Sains yang lengang, Harumi menyelesaikan seluruh siklus pencatatan suhunya tepat sesuai jadwal, memakan roti lapis dingin dari tasnya di ruang istirahat yang kosong, lalu mematikan lampu laboratorium satu per satu tepat pukul sepuluh malam."
            nar "Sebelum menutup buku catatan hitamnya, ia menuliskan kesimpulan bahwa seluruh parameter reaksi malam itu berjalan sesuai perhitungan awal. Di sudut paling bawah halaman kertas, terselip satu kata pendek yang ia tulis dengan ukuran huruf jauh lebih kecil di luar tabel pengamatan, yaitu kata kecewa."
        else:
            yutaka "Oh, masih lanjut mantau sampel sampai malam ya, Kujo-san. Ya sudah, semangat deh di labnya. Aku balik duluan ya."
            harumi "Iya. Terima kasih, Kisaragi-kun. Hati-hati di jalan, angin di luar cukup dingin."
            nar "Harumi mengangguk tenang lalu berbalik melangkah ke arah tangga turun sambil mendekap buku-buku referensinya. Kamu melangkah keluar dari Perpustakaan Pusat tanpa menoleh kembali."
            nar "Sepanjang sisa malam itu tidak ada satu pun pesan masuk darimu. Di lantai dua Gedung Sains yang sepi, Harumi menyelesaikan seluruh pencatatan suhunya tepat sesuai jadwal, menghabiskan roti dingin yang tersisa di tasnya di ruang istirahat kosong, lalu mematikan lampu laboratorium satu per satu tepat pukul sepuluh."
            nar "Di buku catatan hitamnya, ia menuliskan kesimpulan bahwa jalannya pengamatan malam itu sesuai perkiraan awal. Hanya saja di baris paling bawah halaman, terselip satu kata yang ditulis jauh lebih kecil dan belum berani ia masukkan ke kolom kesimpulan, yaitu kata kecewa."
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
