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
            chiasa "Ngomong-ngomong, buku catatan hitam ini memang selalu Senpai bawa ke mana-mana sejak semester satu ya?"
            harumi "Iya. Dulu waktu baru masuk universitas, kakakku menyarankan aku membawa satu buku kecil supaya aku tidak kewalahan mengingat percakapan di luar materi praktikum."
            chiasa "Saran yang rapi sekali, cocok banget sama gaya berpikir Senpai yang teratur."
            nar "Harumi mengusap sampul buku catatan hitamnya dengan senyum tipis sebelum akhirnya menuangkan teh hangat ke dalam cangkirmu."
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
            yutaka "Lagipula kalau kamu langsung bertanya begitu, kamu jadi menghemat banyak halaman buku catatan buat materi laboratorium."
            harumi "Benar juga. Halaman belakang buku ini sebenarnya sudah hampir penuh oleh catatan percakapan bulan lalu."
            nar "Harumi menutup buku catatan hitamnya dengan raut wajah yang tampak jauh lebih tenang, lalu mengangkat teko keramik untuk mengisi cangkir teh di hadapanmu."
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
            nar "Harumi menyesap teh hijau panggangnya perlahan sambil sesekali melirik ke arahmu dengan sorot mata yang terasa jauh lebih akrab dibandingkan tadi sore."
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
            nar "Harumi merapatkan kedua tangannya pada cangkir keramik hangat itu sambil menikmati sisa malam yang tenang bersamamu di serambi baca."
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
        if kk_slot >= 3:
            nar "Lantai dua Perpustakaan Pusat malam itu terasa tenang di bawah pendar lampu baca meja. Kamu duduk menemani Harumi yang sejak setengah jam lalu sibuk menyalin data pembanding dari tiga jurnal kimia organik untuk lampiran laporan praktikumnya."
        else:
            nar "Lantai dua Perpustakaan Pusat hari itu cukup tenang. Kamu duduk di meja baca dekat jendela besar menemani Harumi yang sejak setengah jam lalu sibuk menyalin data pembanding dari tiga jurnal kimia organik untuk lampiran laporan praktikumnya."
        chiasa "Tiga jurnal tebal itu selesai semua hari ini, Kujo-senpai?"
        harumi "Tinggal satu tabel pembanding lagi, Amamiya-san. Aku perlu memastikan batas galat suhu ruang di pengukuran kemarin tidak keluar dari rentang jurnal acuan."
        chiasa "Teliti banget sampai dihitung ulang ke angka di belakang koma segala."
        harumi "Di reaksi katalis, selisih setengah derajat saja bisa mengubah hasil kurvanya."
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
        "Ogawa" "Ah, urusan administrasi seperti itu gampang sekali diatur belakangan. Prof. Mizuhara akhir-akhir ini sibuk sekali dengan rapat komite fakultas, jadi beliau biasanya menyerahkan urusan pembinaan junior di laboratorium kepadaku."
        harumi "Tapi untuk pemakaian ruang instrumen di luar jadwal kelas kan tetap butuh lembar persetujuan tertulis..."
        "Ogawa" "Di dunia riset tingkat lanjut, hal paling mendasar itu rasa saling percaya antara peneliti senior dan juniornya dulu, Kujo-san. Kalau kita sudah cocok bekerja berdua, akses ke instrumen utama maupun surat rekomendasi untukmu nanti tinggal mengikuti."
        nar "Ogawa mengeluarkan ponsel dari saku jasnya, melirik layar sebentar, lalu kembali tersenyum tenang kepada Harumi."
        "Ogawa" "Nanti malam kukirimkan jadwal kosongku untuk akhir pekan ini lewat pesan pribadi ya, Kujo-san. Kamu pikirkan saja dulu."
        nar "Pria itu hanya mengangguk sekilas tanpa menatapmu, lalu melangkah pergi menyusuri lorong rak buku. Setelah langkah sepatunya menghilang di tangga turun, Harumi memandang map plastiknya sejenak lalu menoleh kepadamu."
        harumi "Amamiya-san, barusan itu Ogawa Masato, kandidat doktor senior di laboratorium kimia kami. Menurut pengamatanmu, apakah tawaran bimbingan di luar jam resmi seperti tadi itu prosedur yang wajar di universitas?"
        chiasa "Memangnya selama ini di laboratorium kimia pernah ada senior doktoral yang mengadakan bimbingan pribadi tanpa lewat pengumuman dosen, Senpai?"
        harumi "Sepengetahuanku selama tiga semester di sini, seluruh jadwal asisten maupun pembagian kelompok riset selalu ditempel resmi di papan pengumuman ruang profesor."
        nar "Harumi membalik halaman buku catatan kecilnya yang masih kosong, bersiap mendengarkan penilaianmu dengan saksama."
    else:
        if kk_slot >= 3:
            nar "Lantai dua Perpustakaan Pusat malam itu cukup lengang di bawah sorot lampu meja baca. Kamu duduk di seberang Harumi sambil mengerjakan rangkuman kuliahmu sendiri, sementara Harumi dengan teliti menyalin tabel dari tumpukan jurnal kimia organik ke lembar data risetnya."
        else:
            nar "Lantai dua Perpustakaan Pusat hari itu cukup lengang. Kamu duduk di seberang Harumi sambil mengerjakan rangkuman kuliahmu sendiri, sementara Harumi dengan teliti menyalin tabel dari tumpukan jurnal kimia organik ke lembar data risetnya."
        yutaka "Dari tadi angka di tabel ketiga itu kamu periksa ulang terus ya, Kujo-san?"
        harumi "Iya, Kisaragi-kun. Aku sedang mencocokkan koreksi suhu ruang dari percobaan kemarin dengan jurnal pembanding ini supaya datanya tidak meleset."
        yutaka "Telaten banget sampai diperiksa satu per satu."
        harumi "Kalau langkah awal saja meleset sedikit, analisis akhirnya jadi tidak bisa dipakai."
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
        "Ogawa" "Hal-hal teknis semacam itu bisa diatur kapan saja belakangan. Prof. Mizuhara bulan ini padat sekali jadwal rapatnya, jadi beliau percaya penuh padaku untuk menyeleksi junior yang berbakat di lab."
        harumi "Namun biasanya untuk jadwal tambahan di luar praktikum tetap ada formulir yang ditandatangani profesor..."
        "Ogawa" "Dalam kelompok riset, yang paling menentukan itu hubungan saling percaya antara senior dan juniornya lebih dulu, Kujo-san. Kalau kita sudah bisa bekerja sama dengan fleksibel, urusan akses data laboratorium dan rekomendasi akademikmu pasti kupastikan aman."
        nar "Ia memeriksa jam tangan peraknya sekilas, lalu tersenyum lagi kepada Harumi."
        "Ogawa" "Nanti malam kukirimkan waktu dan tempat pertemuannya lewat pesan ya, Kujo-san. Silakan dipertimbangkan dulu."
        nar "Ogawa berbalik tanpa menyapamu dan berjalan meninggalkan ruang baca. Begitu punggung berjas putih itu hilang di balik deretan rak, Harumi menoleh ke arahmu dengan kening sedikit berkerut."
        harumi "Kisaragi-kun, pria tadi itu Ogawa Masato, kandidat doktor yang membantu mengawasi laboratorium kami. Menurutmu, apakah ajakan bimbingan khusus di luar jadwal seperti barusan itu hal yang lazim?"
        yutaka "Memangnya selama kamu ikut praktikum di laboratorium itu, pernah ada asisten doktoral yang ngajak bimbingan tertutup tanpa surat tugas profesor?"
        harumi "Belum pernah. Biasanya setiap pembagian sub-proyek riset selalu diumumkan resmi dalam rapat mingguan laboratorium."
        nar "Harumi memegang pena di atas buku catatannya, menunggu pendapatmu sebelum memutuskan cara membalas pesan senior tersebut."
    call kk_family_menu("H06", ["\"Kelihatannya dia beneran merhatiin risetmu, mungkin itu peluang bagus.\"", "\"Tadi kamu nanya soal kerjaan, tapi dia malah muter ke soal kepercayaan.\"", "\"Jangan terima syarat yang kabur begitu cuma gara-gara dipuji atau dijanjikan rekomendasi.\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Kelihatannya dia beneran merhatiin detail tabel riset Kujo-senpai sih tadi. Kalau memang seorang kandidat doktor mau bantu Senpai masuk ke proyek publikasi jurnal lebih cepat, mungkin itu peluang yang bagus buat dicoba."
            nar "Harumi menunduk memandangi map plastik berisi tabel katalisnya. Keraguan kecil yang tadi sempat muncul di keningnya perlahan mereda setelah mendengar pendapatmu."
            harumi "Benar juga. Selama ini di laboratorium jarang ada senpai yang mau memeriksa lembar koreksi galat milik mahasiswa tahun kedua sampai serinci itu."
            chiasa "Mungkin dia memang lagi cari asisten yang seteliti Senpai buat risetnya."
            harumi "Jika dilihat dari kebutuhan riset, analisis itu cukup masuk akal. Kalau tujuannya untuk meningkatkan efisiensi penelitian dan peluang publikasi, rasanya tidak ada alasan untuk menolak sebelum mencobanya sekali."
            chiasa "Berarti Senpai mau coba ikut bimbingannya kalau nanti malam dia kirim pesan?"
            harumi "Iya. Nanti kusiapkan buku data mentahku dan grafik perbandingannya sebelum dia menghubungi, supaya waktunya tidak terbuang sia-sia."
            chiasa "Kalau jadwal bimbingannya sampai lewat jam tutup gedung laboratorium, jangan lupa kabari teman satu lab yang lain ya, Senpai."
            harumi "Saran yang baik, Amamiya-san. Aku memang selalu mencatat jam keluar masuk laboratorium di buku log pintu depan."
            chiasa "Kalau begitu aku bantu kembalikan tiga jurnal tebal ini ke rak referensi bagian belakang dulu ya, Senpai."
            harumi "Terima kasih banyak, Amamiya-san. Itu sangat menghemat waktuku."
            nar "Harumi memasukkan mapnya ke dalam tas dengan gerakan rapi. Pesan dari Ogawa yang masuk kemudian berisi ajakan bertemu di luar jam operasional laboratorium, dan karena tidak ada lagi yang mempertanyakan syaratnya, Harumi menyetujui jadwal pertama tersebut."
        else:
            yutaka "Kelihatannya dia beneran paham dan merhatiin hasil hitunganmu sih, Kujo-san. Kalau kandidat doktor di labmu sendiri yang nawarin jalan buat masuk proyek publikasi semester depan, mungkin itu kesempatan bagus buat kariermu."
            nar "Harumi menatap map datanya sejenak, lalu mengangguk pelan. Tanggapan positifmu barusan membuatnya menepikan kejanggalan kecil dari jawaban Ogawa tadi."
            harumi "Masuk akal. Memang tidak setiap hari ada peneliti tingkat doktoral yang bersedia meluangkan waktunya memeriksa draf mahasiswa tahun kedua."
            yutaka "Mungkin dia memang butuh orang yang teliti buat membantu proyek jurnalnya."
            harumi "Kalau dilihat dari sisi efisiensi tim riset, tawaran itu cukup logis. Sepertinya layak dicoba satu kali untuk melihat arah diskusinya."
            yutaka "Jadi kalau nanti malam dia kirim jadwalnya, kamu mau ambil?"
            harumi "Iya, aku akan mencobanya lebih dulu. Nanti kusiapkan salinan tabel pengamatanku supaya diskusinya berjalan efektif."
            yutaka "Pastikan saja pertemuan pertamanya tetap dilakukan di ruang laboratorium kampus yang ada petugas jaganya."
            harumi "Tentu, Kisaragi-kun. Aku tidak punya alasan untuk membawa data praktikum keluar dari gedung fakultas."
            yutaka "Sini jurnal-jurnal tebalnya kubantu kembalikan ke troli buku perpustakaan sebelum kita turun."
            harumi "Terima kasih, Kisaragi-kun. Kita bisa langsung turun setelah ini."
            nar "Harumi merapikan bukunya ke dalam tas. Tak lama kemudian, Ogawa mengirimkan jam pertemuan pertama di luar jadwal resmi laboratorium, membuka langkah awal bimbingan tanpa pernah menjawab pertanyaan soal izin Prof. Mizuhara."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Aku memang nggak paham soal aturan laboratorium kimia sih, Kujo-senpai. Cuma tadi waktu dengar kalian ngobrol dari seberang meja, ada satu hal yang kedengaran agak ganjil di telingaku."
            harumi "Bagian mana yang terdengar ganjil, Amamiya-san?"
            chiasa "Tadi kan Senpai nanya tiga hal yang jelas banget soal pekerjaan, mulai dari bentuk bimbingannya gimana, lokasinya di mana, sama apakah Prof. Mizuhara tahu. Tapi Ogawa-senpai itu nggak jawab satu pun dari tiga pertanyaan tadi, malah muter balik bahas soal rasa saling percaya sama janji rekomendasi."
            nar "Jari Harumi berhenti di atas penutup mapnya. Ia terdiam beberapa detik, memutar ulang kalimat demi kalimat yang baru saja diucapkan Ogawa di dalam kepalanya."
            harumi "...Pengamatanmu tepat sekali. Aku mengajukan pertanyaan tentang parameter teknis dan prosedur resmi, tetapi dia menjawabnya dengan variabel abstrak soal kepercayaan pribadi. Secara logika, jawaban itu sama sekali tidak menjawab pertanyaanku."
            chiasa "Apalagi cara dia langsung menyingkirkan nama Prof. Mizuhara dengan alasan administrasi gampang diatur belakangan. Di kampus kan justru izin dosen pembimbing itu langkah pertama."
            harumi "Benar. Aku sendiri lupa memeriksa ketidaksesuaian itu karena telanjur senang tabel ketigaku dibaca dengan teliti."
            chiasa "Aku nggak bilang dia pasti berniat buruk sih, Senpai. Tapi sebelum Senpai iyain ajakannya, lebih aman kalau Senpai minta dia tulis jelas dulu jadwal dan izin dosennya."
            harumi "Setuju. Kalau bimbingan itu memang kegiatan akademik yang wajar, seharusnya dia tidak keberatan memberikan rincian tertulis dan menyertakan persetujuan Prof. Mizuhara. Aku tidak perlu langsung menuduhnya orang jahat, tapi aku wajib memeriksa kejelasannya dulu. Terima kasih sudah memperhatikan celah itu, Amamiya-san."
            chiasa "Sama-sama, Senpai. Kadang orang yang duduk di luar percakapan memang lebih gampang menyadari kalau arah obrolannya dibelokkan."
            harumi "Persis seperti fungsi pengamat independen dalam eksperimen. Nanti malam ketika dia mengirim pesan, aku akan langsung membalas dengan daftar tiga pertanyaan teknis tadi."
            chiasa "Kalau dia masih mengelak juga waktu ditanya lewat pesan tertulis, berarti Senpai sudah punya bukti jelas buat menolak."
            harumi "Metode penyaringan yang sangat bersih dan rapi, Amamiya-san."
            nar "Harumi membuka buku catatan kecilnya dan menuliskan tiga poin verifikasi yang harus dijawab Ogawa sebelum ia bersedia datang ke pertemuan mana pun."
        else:
            yutaka "Aku memang bukan anak laboratorium sains sih, Kujo-san. Tapi dari caranya menjawab pertanyaanmu barusan, ada bagian yang kelihatan nggak beres menurutku."
            harumi "Bagian mana yang tidak beres menurutmu, Kisaragi-kun?"
            yutaka "Coba kamu ingat-ingat lagi. Kamu tanya tiga hal yang sangat teknis, yaitu bentuk bimbingannya apa, jadwalnya kapan, dan apakah Prof. Mizuhara tahu. Dia sama sekali nggak menjawab satu pun dari ketiganya, malah langsung ngeles bahas rasa saling percaya sama iming-iming akses lab."
            nar "Harumi terdiam di kursinya. Ujung jarinya mengetuk pelan permukaan map plastik sambil menimbang ulang struktur percakapan barusan."
            harumi "...Kamu benar. Aku menanyakan prosedur kerja yang konkret, sedangkan dia mengalihkan jawaban ke tuntutan kepercayaan personal. Kedua hal itu tidak nyambung."
            yutaka "Ditambah lagi dia buru-buru menyebut izin Prof. Mizuhara itu urusan belakangan. Padahal di lingkungan kampus, proyek resmi jelas harus lewat persetujuan profesornya lebih dulu."
            harumi "Betul sekali. Tadi perhatianku sempat terpecah karena pujiannya tentang koreksi suhu di tabel ketiga."
            yutaka "Aku nggak langsung nuduh dia mau berbuat jahat juga sih. Cuma kalau bimbingannya memang bersih, harusnya dia nggak perlu ngeles waktu kamu bawa-bawa nama dosen pembimbingmu."
            harumi "Iya. Aku bisa membalas pesannya nanti dengan meminta rincian agenda tertulis serta konfirmasi ke Prof. Mizuhara lebih dulu, tanpa perlu buru-buru menyimpulkan niatnya sekarang. Terima kasih sudah menangkap ketidaksinkronan itu, Kisaragi-kun."
            yutaka "Sama-sama. Orang kalau lagi dipuji hasil kerjanya memang wajar kalau lengah sebentar."
            harumi "Untung kamu duduk di seberang meja dan menyimak struktur kalimatnya secara objektif."
            yutaka "Nanti kalau balasan pesannya masih muter-muter nggak jelas, tinggal kamu abaikan saja ajakannya."
            harumi "Tentu. Tanpa parameter prosedur yang sah, aku tidak akan meluangkan waktu untuk sesi di luar jadwal."
            nar "Harumi mencatat poin tersebut di buku sakunya, mengubah tawaran yang tadinya tampak seperti pujian membanggakan menjadi sesuatu yang harus diuji ulang."
    else:
        if kk_host == "chiasa":
            chiasa "Kujo-senpai, jujur aja aku sama sekali nggak suka lihat gelagat Ogawa-senpai tadi. Tolong jangan mau terima ajakan ketemu di luar jam lab yang syaratnya kabur begitu, cuma gara-gara dia muji tabel Senpai atau janjiin surat rekomendasi."
            nar "Nada suaramu yang serius dan tegas membuat Harumi menatapmu lekat-lekat. Ia tidak tampak marah sama sekali. Ia hanya membetulkan letak kacamatanya dan mendengarkan dengan penuh perhatian."
            harumi "Kamu memperingatkanku dengan sangat tegas, Amamiya-san. Aku percaya kekhawatiranmu itu tulus."
            chiasa "Habisnya kelihatan banget dia sengaja nutupin soal Prof. Mizuhara tadi, Senpai. Ditambah lagi dari tadi dia berdiri memayungi mejamu dan sama sekali nggak menganggap ada orang lain duduk di sini."
            harumi "Poin soal Prof. Mizuhara dan sikapnya itu memang ganjil. Tapi... boleh aku minta satu hal padamu? Tolong jabarkan urutan tanda-tanda yang membuatmu langsung curiga padanya barusan. Aku ingin mempelajari polanya supaya bisa mengenalinya sendiri tanpa cuma memindahkan kepatuhanku dari Ogawa-senpai ke perintahmu."
            chiasa "Iya, Senpai, permintaan yang bagus banget. Pertama, dia buka obrolan pakai pujian yang sangat spesifik soal bagian tabel yang bikin Senpai bangga, supaya pertahanan Senpai langsung turun."
            harumi "Validasi awal untuk menurunkan kewaspadaan. Lalu yang kedua?"
            chiasa "Kedua, waktu Senpai minta kejelasan aturan dan nama dosen pembimbing, dia anggap itu cuma urusan sepele yang bisa diatur belakangan. Dan ketiga, dia langsung mengaitkan kesediaan Senpai menuruti kemauannya secara pribadi dengan akses alat serta rekomendasi masa depan."
            harumi "...Pujian spesifik, pengaburan prosedur resmi, lalu mengikat masa depan akademik pada kepatuhan pribadi. Kalau diuraikan menjadi tiga tahap seperti itu, polanya terlihat sangat berbahaya."
            chiasa "Nah, makanya kalau semua syaratnya belum tertulis resmi di papan laboratorium dan disetujui profesornya, jangan pernah mau ketemu sendirian, Senpai."
            harumi "Aku mengerti sepenuhnya sekarang. Besok aku juga akan menanyakan langsung ke Prof. Mizuhara soal proyek itu. Terima kasih sudah mengajariku cara membaca tandanya, Amamiya-san."
            chiasa "Aku senang bisa bantu Senpai menyusun daftar tandanya. Jangan lupa simpan catatan tiga pola tadi di buku hitam Senpai ya."
            harumi "Sudah kutulis di halaman paling depan barusan. Mulai sekarang aku akan memakai tiga indikator ini setiap kali ada tawaran serupa."
            nar "Harumi menutup buku catatan hitamnya dengan bunyi pelan yang mantap, lalu merapikan map praktikumnya untuk bersiap meninggalkan perpustakaan bersamamu."
        else:
            yutaka "Kujo-san, terus terang aja aku nggak suka cara senpai labmu itu ngomong tadi. Jangan sampai kamu mau diajak ketemuan di luar jam resmi dengan syarat kabur begitu cuma gara-gara dia muji risetmu atau bawa-bawa janji rekomendasi."
            nar "Mendengar peringatanmu yang tanpa tedeng aling-aling, Harumi menatapmu serius dari balik kacamatanya."
            harumi "Nada bicaramu tegas sekali, Kisaragi-kun. Aku tahu kamu mengatakan itu karena mengkhawatirkanku."
            yutaka "Habisnya gelagat orang itu waktu kamu sebut nama Prof. Mizuhara tadi jelas banget lagi cari celah. Caranya berdiri membatasi mejamu seolah aku nggak ada di sini juga sudah cukup bikin risih."
            harumi "Soal dia menghindari nama Prof. Mizuhara itu memang ganjil. Tapi... tolong jelaskan kepadaku bagian mana saja dari ucapannya tadi yang menjadi indikator bahaya menurutmu. Aku ingin belajar memahami polanya sendiri, supaya aku tidak cuma memindahkan ketergantungan keputusanku dari dia kepadamu."
            yutaka "Permintaan yang adil. Pertama, dia masuk pakai pujian yang sangat spesifik soal kerja kerasmu di tabel ketiga, supaya kamu langsung merasa cuma dia yang paham bakatmu."
            harumi "Memberikan pengakuan spesifik untuk membangun kepercayaan cepat. Lalu indikator keduanya?"
            yutaka "Kedua, begitu kamu minta batas yang jelas soal lokasi, jam, dan izin dosen pembimbing, dia langsung meremehkan itu sebagai urusan teknis belakangan. Dan ketiga, dia langsung menggantungkan akses alat lab sama rekomendasi publikasimu pada seberapa patuh kamu ikut cara kerjanya di luar jadwal."
            harumi "...Ketika dipecah menjadi tiga variabel seperti itu, struktur manipulasinya langsung kelihatan sangat jelas. Kalau bimbingannya memang resmi, rekomendasi tidak mungkin dijadikan alat tawar-menawar pribadi."
            yutaka "Persis. Jadi kalau dia nggak berani bicara di depan Prof. Mizuhara, jangan pernah diladeni."
            harumi "Paham. Besok aku akan memastikan langsung prosedurnya ke Prof. Mizuhara. Sekarang aku tahu persis apa yang harus kuperiksa. Terima kasih banyak, Kisaragi-kun."
            yutaka "Baguslah kalau tiga indikator tadi masuk akal buatmu. Jangan lupa kunci juga meja kerjamu di lab supaya draf hitunganmu nggak diambil orang sembarangan lagi."
            harumi "Benar, tadi itu kelalaianku meninggalkan draf di atas meja timbang. Besok pagi akan selalu kukunci di laci sebelum ke perpustakaan."
            nar "Harumi memasukkan buku catatan hitam dan map praktikumnya ke dalam tas dengan raut wajah tenang yang kini jauh lebih waspada."
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
        chiasa "Kujo-senpai belum pulang juga? Tadi kulihat foto yang Senpai kirim di grup, semua orang pamer foto kue stroberi sama lampu jalan, cuma Senpai yang balas pakai foto tabel angka. Habis dari perpustakaan ini Senpai masih mau balik ke gedung laboratorium?"
        nar "Harumi menaikkan letak kacamatanya dengan ujung telunjuk, lalu memasukkan penggaris logam ke dalam saku mapnya dengan gerakan teratur."
        harumi "Amamiya-san. Aku mengirim foto itu karena sedang memeriksa perubahan stabilitas suhu pada jam keempat, jadi benda terdekat di depan kameraku memang tabel pengamatan. Aku cuma mampir dua puluh menit ke perpustakaan buat mencocokkan tabel indeks bias dari jurnal lama."
        chiasa "Hari ini kan sudah mulai libur Natal, Senpai. Memangnya sampel di laboratorium nggak bisa ditinggal dulu terus dilanjutin habis tahun baru aja?"
        harumi "Reaksi kimia tidak membaca kalender akademik, Amamiya-san. Sampel katalis yang sedang kupantau butuh pencatatan suhu setiap dua jam sekali. Kalau pemanas inkubatornya kumatikan sekarang, seluruh larutan yang sudah kutumbuhkan sejak hari Selasa harus diulang dari nol. Jadi jadwalku masih berjalan sampai pukul sepuluh malam nanti."
        chiasa "Sampai jam sepuluh malam? Di Gedung Sains sendirian gitu?"
        harumi "Petugas keamanan gedung masih berjaga di pos lantai satu, dan lampu lorong utama tetap menyala. Hanya saja anggota lab yang lain memang sudah izin pulang sejak tadi. Itu jawaban berdasarkan jadwal kerjaku."
        nar "Harumi memeluk kedua jilid buku referensi itu ke dadanya. Pandangannya turun sejenak ke sampul buku catatan hitamnya sebelum kembali menatapmu."
        harumi "Kalau pertanyaan apakah aku memang lebih suka berada di laboratorium sendirian daripada di tempat lain hari ini... bagian itu sengaja tidak kutanyakan ke diriku sendiri. Kalau terlalu dipikirkan, biasanya konsentrasiku saat membaca angka ukur malah terganggu."
        chiasa "Jadi selama ini Senpai sengaja menyibukkan diri dengan jadwal pengukuran supaya nggak sempat merasa sepi?"
        harumi "Metode itu cukup efektif selama tiga semester terakhir, Amamiya-san."
    else:
        nar "Menjelang libur Natal, lantai dua Perpustakaan Pusat tampak jauh lebih lengang daripada biasanya. Hanya tersisa beberapa mahasiswa di meja dekat tangga yang sesekali berbisik membahas rencana makan malam dan belanja di sekitar stasiun."
        nar "Di sudut tenang dekat deretan rak jurnal kimia, Kujo Harumi sedang membereskan dua buku referensi tebal bersama buku catatan pengamatannya yang bersampul hitam. Baru lima belas menit lalu, saat grup pesan singkat teman-teman angkatan penuh dengan foto pohon Natal dan kue kafe, Harumi membalas ucapan selamat Natal hanya dengan mengirim foto lembar tabel pencatatan suhu larutan dari laboratorium."
        yutaka "Di grup dari tadi orang-orang kirim foto kue sama lampu jalan, cuma kamu yang balas pakai foto tabel suhu larutan, Kujo-san. Habis dari perpustakaan ini kamu masih mau balik ke gedung lab?"
        nar "Harumi membetulkan letak kacamatanya dengan ujung jari telunjuk, lalu memasukkan penggaris logam kecil ke dalam map plastiknya dengan rapi."
        harumi "Kisaragi-kun. Aku mengirim foto itu karena kebetulan sedang mengecek stabilitas suhu di jam keempat, jadi objek terdekat di mejaku memang lembar tabel itu. Aku hanya mampir sebentar ke sini buat mencocokkan kurva indeks bias di jurnal lama."
        yutaka "Ini sudah masuk libur Natal lho. Memangnya sampelnya nggak bisa dihentikan dulu terus dilanjut habis tahun baru?"
        harumi "Reaksi kimia tidak membaca kalender libur kampus, Kisaragi-kun. Sampel katalis yang sedang kuamati perlu dicatat suhunya setiap dua jam sekali."
        harumi "Kalau pemanas inkubatornya kumatikan hari ini, larutan yang sudah kutumbuhkan sejak Selasa lalu bakal gagal semua. Jadi jadwalku masih berjalan sampai pukul sepuluh malam nanti."
        yutaka "Sampai jam sepuluh malam? Di gedung yang sudah kosong sendirian begitu?"
        harumi "Petugas keamanan masih berjaga di lantai bawah, tapi anggota lab yang lain memang sudah izin pulang semua. Itu jawaban berdasarkan jadwalku."
        nar "Harumi memeluk kedua buku referensinya ke dada. Matanya sempat turun sebentar ke sampul buku catatan hitamnya sebelum kembali menatapmu."
        harumi "Kalau pertanyaan tentang apakah aku memang ingin menghabiskan hari Natal sendirian di laboratorium... bagian itu sengaja belum kutanyakan ke diriku sendiri. Kalau dipikirkan sekarang, biasanya akurasi pembacaan angkaku malah turun."
        yutaka "Berarti kamu sengaja pasang jadwal eksperimen rapat-rapat supaya nggak sempat memikirkan libur akhir tahun?"
        harumi "Secara praktis, kesibukan laboratorium memang selalu berhasil mengalihkan pikiran dari suasana luar, Kisaragi-kun."
    call kk_family_menu("H07", ["\"Kalau boleh, aku ikut ke gedung lab ya. Aku tunggu di ruang baca luar sampai selesai.\"", "\"Jangan lupa makan malam. Nanti kukirim makanan hangat ke depan gedung lab ya.\"", "\"Oh, masih lanjut praktikum ya. Ya sudah, semangat ya di lab.\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Kalau boleh, aku ikut jalan ke gedung laboratorium sekarang ya, Kujo-senpai. Aku nggak bakal masuk ke ruang reaksi kok, aku duduk nunggu di ruang baca luar aja sambil gambar sketsa sampai jadwal pengamatan Senpai selesai."
            nar "Harumi terdiam di samping meja kayu. Selama beberapa detik ia menatapmu dari balik lensa kacamatanya, seolah sedang memeriksa apakah kalimatmu barusan hanya basa-basi."
            harumi "Kamu mau ikut ke Gedung Sains hari ini, Amamiya-san? Di luar udaranya sudah dingin, dan hampir semua mahasiswa lain memilih pergi ke tempat yang ramai di sekitar stasiun."
            chiasa "Tempat yang terlalu ramai malah bikin cepat pusing, Senpai. Lagian di ruang baca luar lab kan ada pemanas sama sofa, enak buat duduk gambar tanpa ada yang lalu-lalang. Nanti tiap Senpai selesai catat suhu, kita bisa ngobrol sebentar."
            harumi "...Keputusanmu sama sekali tidak ada di dalam perkiraan awalku hari ini. Tapi harus kuakui, penyimpangan data yang ini membuatku senang."
            if kk_slot >= 2:
                nar "Kalian berdua berjalan menyeberangi pelataran kampus yang mulai temaram menuju Gedung Sains. Sesampainya di lantai dua, kamu duduk di sofa ruang istirahat tepat di sebelah dinding kaca laboratorium sambil membuka buku sketsa, sementara Harumi mengenakan jas lab putihnya di dalam dan memeriksa deretan tabung inkubator."
            else:
                nar "Kalian berdua berjalan menyeberangi pelataran kampus yang berangin di bawah langit Desember yang pucat menuju Gedung Sains. Sesampainya di lantai dua, kamu duduk di sofa ruang istirahat tepat di sebelah dinding kaca laboratorium sambil membuka buku sketsa, sementara Harumi mengenakan jas lab putihnya di dalam dan memeriksa deretan tabung inkubator."
            nar "Sekitar empat puluh lima menit kemudian, pintu geser laboratorium terbuka. Harumi melangkah keluar setelah melepas sarung tangan lateksnya, membawa nampan logam berisi teko kecil dan dua cangkir keramik putih yang mengepulkan aroma teh panggang."
            harumi "Siklus pencatatan ketujuh sudah selesai dan suhunya stabil. Masih ada waktu jeda satu jam lebih sebelum pembacaan terakhir. Silakan diminum, Amamiya-san. Aku menyeduhnya tepat tiga menit."
            chiasa "Wah, harum banget tehnya. Makasih banyak, Kujo-senpai. Di ruang istirahat lab memang selalu sedia dua cangkir begini?"
            harumi "Sebenarnya di lemari penyimpanan ada enam cangkir. Biasanya aku hanya mencuci dan mengeluarkan satu cangkir untukku sendiri, atau sesekali menaruh satu cangkir cadangan di baki karena berpikir mungkin ada asisten lab yang kebetulan lembur."
            nar "Harumi duduk di kursi sebelahmu, meletakkan cangkirnya dengan hati-hati, lalu menoleh menatapmu."
            harumi "Tapi tadi waktu kita baru sampai di sini, aku langsung mencuci dua cangkir sekaligus karena sudah tahu kamu benar-benar duduk menunggu di luar. Ternyata menyiapkan cangkir kedua karena kepastian itu rasanya jauh lebih hangat daripada menyiapkan karena kemungkinan."
            chiasa "Hehe, kalau gitu kapan-kapan kalau Senpai lembur lagi, siapkan dua cangkir aja dari awal."
            harumi "Akan kupertimbangkan sebagai prosedur tetap. Ngomong-ngomong, dari balik kaca tadi kulihat pensilmu bergerak terus. Gambar apa yang sedang kamu buat di buku sketsamu?"
            nar "Kamu memutar buku sketsamu ke arahnya, memperlihatkan arsir pensil deretan tabung kaca, lampu meja laboratorium, dan siluet Harumi yang sedang membungkuk mencatat di balik jendela."
            harumi "Menarik sekali. Sudut pantulan cahaya di permukaan tabung ukurnya sangat akurat... meskipun skala meniskus cairan di gambar tabung sebelah kiri terlalu cekung dua milimeter dari aslinya."
            chiasa "Haha, maaf, Senpai! Mataku nggak seteliti lensa laboratorium."
            harumi "Tidak, aku memujimu. Jarang sekali ada orang yang duduk mengamati ruang lab selama hampir satu jam tanpa mengeluh bosan. Di rumah orang tuaku di Kansai pun, suasana akhir tahun biasanya terasa mirip seperti ini... sangat tenang dan teratur."
            chiasa "Oh ya? Orang tua Kujo-senpai di Kansai biasanya merayakan akhir tahun gimana?"
            harumi "Ayah dan Ibu sama-sama akademisi. Jadi makan malam akhir tahun di rumah kami sering kali berakhir menjadi diskusi makalah terbaru sambil minum teh hijau, dengan nada suara sopan yang tidak pernah naik. Semuanya tertata rapi, sampai kadang aku sendiri lupa bagaimana caranya mengobrol tanpa harus menyiapkan argumen."
            chiasa "Kalau duduk minum teh di sofa sini bareng aku, Senpai nggak perlu nyiapin argumen apa-apa kok. Kita ngobrol ngalor-ngidul aja."
            harumi "...Iya. Ternyata mengobrol tanpa daftar topik di ruang baca begini jauh lebih mudah dari yang kubayangkan."
            chiasa "Tehnya juga masih hangat kan? Kutuangin setengah cangkir lagi ya, Senpai."
            harumi "Boleh, terima kasih, Amamiya-san. Malam ini berjalan jauh lebih cepat dari hitungan awalku."
            chiasa "Nanti waktu pencatatan suhu terakhir jam sepuluh selesai, kita pulang bareng naik taksi atau bus depan gerbang ya, Senpai."
            harumi "Setuju. Pulang bersama setelah praktikum malam selesai ternyata terdengar jauh lebih menyenangkan daripada berjalan ke halte sendirian."
            nar "Harumi menyesap teh panggang hangatnya sambil memperhatikan detail arsir bayangan pada buku sketsamu dengan sorot mata yang tenang."
            nar "Obrolan kalian mengalir tenang ditemani aroma teh panggang dan uap pemanas ruangan, sampai jam pengamatan terakhir Harumi tiba tanpa terasa."
        else:
            yutaka "Kalau nggak mengganggu kerjamu, aku ikut jalan ke Gedung Sains aja sekalian, Kujo-san. Tenang, aku nggak bakal masuk ruang reaksi kok. Aku duduk di ruang istirahat luar aja sambil baca bahan kuliahku sampai kamu selesai."
            nar "Harumi berhenti melangkah di samping meja. Ia menatapmu beberapa detik dari balik lensa kacamatanya untuk memastikan kamu tidak sedang bergurau."
            harumi "Kamu mau ikut menemani di Gedung Sains hari ini, Kisaragi-kun? Padahal hampir semua orang memilih pergi ke pusat kota atau acara makan malam."
            yutaka "Malas juga kalau harus desak-desakan di dekat stasiun. Lagian di ruang istirahat depan lab kan pemanasnya hangat dan tenang, cocok buat baca. Nanti pas jam jedamu, kita bisa ngobrol sebentar biar nggak terlalu sunyi."
            harumi "...Tindakanmu benar-benar menyimpang dari perkiraan awalku hari ini. Tapi harus kuakui, penyimpangan yang ini membuatku senang."
            if kk_slot >= 2:
                nar "Kalian berdua melintasi pelataran kampus yang mulai temaram dan berangin menuju Gedung Sains. Di lantai dua, kamu duduk di sofa ruang baca luar sambil membuka catatan yang kamu bawa, membiarkan Harumi bekerja tenang di balik dinding kaca laboratorium dengan jas putih dan sarung tangan lateksnya."
            else:
                nar "Kalian berdua melintasi pelataran kampus yang berangin di bawah langit Desember pucat menuju Gedung Sains. Di lantai dua, kamu duduk di sofa ruang baca luar sambil membuka catatan yang kamu bawa, membiarkan Harumi bekerja tenang di balik dinding kaca laboratorium dengan jas putih dan sarung tangan lateksnya."
            nar "Empat puluh lima menit kemudian, pintu geser lab dibuka. Harumi keluar membawa nampan logam berisi teko porselen dan dua cangkir keramik putih yang mengepulkan aroma teh panggang."
            harumi "Pencatatan ketujuh sudah beres dan grafik suhunya stabil. Masih ada jeda lebih dari satu jam sebelum pembacaan terakhir. Silakan diminum, Kisaragi-kun. Aku menyeduhnya tepat tiga menit."
            yutaka "Wanginya enak banget, Kujo-san. Makasih. Memangnya di ruang lab ini selalu sedia dua cangkir di atas baki?"
            harumi "Di lemari penyimpanan ada enam cangkir. Biasanya aku hanya mencuci satu untukku sendiri, atau kadang menaruh satu cangkir cadangan sekadar berjaga-jaga kalau ada asisten lab yang kebetulan lembur."
            nar "Harumi mengambil tempat di kursi sebelahmu, meletakkan cangkirnya dengan gerakan terukur, lalu menoleh kepadamu."
            harumi "Tapi begitu kita tiba tadi, aku langsung mencuci dua cangkir sekaligus karena tahu kamu benar-benar menunggu di sini. Ternyata menyiapkan cangkir kedua karena kepastian rasanya berbeda jauh daripada menyiapkan hanya karena kemungkinan ada orang."
            yutaka "Kalau begitu lain kali kamu harus lembur lagi, kabari aja dari awal biar prosedur dua cangkirnya langsung jalan."
            harumi "Akan kucatat sebagai kebiasaan baru yang efisien. Omong-omong, dari balik kaca tadi kulihat kamu menulis beberapa catatan pinggir di buku cetak itu. Bahan mata kuliah semester depan?"
            yutaka "Cuma rangkuman soal teori pilihan konsumen yang kemarin sempat bikin pusing di kelas. Sekalian nyicil baca mumpung suasananya tenang begini."
            harumi "Cara orang mengambil keputusan tidak rasional saat sedang tertekan memang menarik untuk dibaca. Di rumah orang tuaku di Kansai dulu, pembicaraan akhir tahun di meja makan juga sering mengarah ke hal-hal analitis seperti ini."
            yutaka "Orang tuamu di Kansai dua-duanya dosen atau peneliti ya?"
            harumi "Iya. Jadi setiap libur akhir tahun, meja makan kami lebih mirip ruang seminar kecil yang sopan. Tidak ada yang bertengkar, semuanya terdengar rapi dan masuk akal, tapi selesai makan masing-masing langsung kembali ke ruang kerja sendiri."
            yutaka "Agak mirip suasana di rumah orang tuaku juga sih, cuma di tempatku lebih sering kosong sekalian. Berarti sore sampai malam ini kita impas ya, sama-sama kabur dari meja makan yang terlalu kaku."
            nar "Harumi terdiam sepersekian detik, lalu tersenyum tipis yang membuat wajahnya tampak jauh lebih hangat daripada di ruang kelas."
            harumi "...Perbandingan yang cukup tepat, Kisaragi-kun. Kalau begitu, sebelum jam pengamatan terakhirku tiba, biar kutuang lagi tehnya mumpung masih panas."
            yutaka "Boleh. Jujur aja, duduk di ruang baca lab begini ternyata jauh lebih enak daripada ikut ramai-ramai di dekat stasiun."
            harumi "Kalau kamu tidak keberatan dengan bau samar larutan dari balik kaca, kamu boleh mampir kapan saja saat aku lembur lagi."
            yutaka "Nanti begitu pembacaan terakhirmu jam sepuluh selesai, aku antar kamu sampai halte bus depan gerbang utama."
            harumi "Terima kasih, Kisaragi-kun. Kehadiranmu malam ini membuat siklus pengamatan empat jam terasa sangat singkat."
            nar "Harumi menuangkan sisa teh panggang hangat dari teko porselen ke dalam kedua cangkir kalian dengan senyum tipis yang tulus."
            nar "Obrolan kalian mengalir tenang di sofa ruang baca luar hingga alarm pengukur waktu di dalam laboratorium berbunyi tanpa terasa."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Kalau harus bolak-balik mantau sampel sampai jam sepuluh malam, biasanya Kujo-senpai suka lupa makan malam kan? Nanti kukirim paket makanan hangat ke lobi Gedung Sains ya, biar Senpai nggak cuma ganjal perut pakai biskuit."
            nar "Harumi membetulkan letak kacamatanya, lalu sudut bibirnya yang biasanya lurus tampak melengkung tipis."
            harumi "Ingatanmu soal kebiasaan burukku saat bekerja cukup akurat, Amamiya-san. Tadi aku memang hanya membawa satu bungkus roti gandum dingin di tas, dan niatnya cuma mau menyeduh air panas dari ketel lab."
            chiasa "Tuh kan, ketebak banget! Masa libur Natal cuma makan roti gandum dingin di ruangan kosong. Aku minta kedai bento dekat gerbang depan antar paket nasi hangat sama sup miso ke lobi Gedung Sains ya. Kira-kira jam tujuh malam pas sama jeda pencatatan Senpai nggak?"
            harumi "Pukul tujuh lewat lima menit adalah jeda tepat setelah pembacaan sampel kedelapan. Aku akan turun ke pintu lobi lantai satu tepat waktu supaya makanannya tidak tertahan di pos satpam dan keburu dingin. Terima kasih banyak, Amamiya-san."
            chiasa "Sama-sama, Senpai. Awas lho kalau sampai kelewatan jam makannya gara-gara keasyikan lihat angka suhu."
            harumi "Akan kupasang pengingat di jam tanganku. Oh ya, Amamiya-san... di kedai dekat gerbang itu, biasanya menu kroket dagingnya tidak terlalu berminyak kan?"
            chiasa "Aman kok, Senpai, kering dan renyah. Nanti kupesanin yang sup misonya banyak tahu sama rumput lautnya."
            harumi "Kalau begitu, terima kasih sebelumnya."
            nar "Malam harinya tepat pukul tujuh lewat seperempat, ponselmu bergetar di meja kamar. Sebuah pesan masuk dari Harumi, dilampiri foto kotak bento kayu berisi nasi hangat, kroket daging, dan mangkuk sup miso yang sudah ditata rapi di meja ruang istirahat laboratorium."
            nar "Di bawah foto tersebut, Harumi menuliskan laporan panjang yang sangat khas dirinya. Ia mencatat bahwa makanannya sudah diterima pukul 19.04, suhu sup misonya masih sekitar enam puluh derajat saat dibuka, lapisan tepung kroketnya masih renyah, dan porsi karbohidratnya sangat ideal untuk menjaga fokus sampai pukul sepuluh nanti."
            nar "Baru saja kamu tersenyum membaca ulasan makanan bergaya laporan praktikum itu, satu pesan pendek masuk lagi darinya mengingatkan agar kamu juga tidak lupa makan malam yang hangat di rumah, ditutup ucapan selamat malam Natal."
            nar "Kamu membalas pesan tersebut dengan mengatakan bahwa kamu baru saja selesai makan malam dan memintanya berhati-hati saat pulang dari gedung laboratorium pukul sepuluh nanti."
            nar "Tidak sampai satu menit, Harumi mengirimkan tanda centang konfirmasi bahwa ia sudah memesan taksi stasiun untuk jam kepulangannya agar tidak berjalan sendirian di jalan gelap."
            nar "Perhatian sederhana lewat sekotak makanan hangat itu berhasil menemani jam lemburnya tanpa mengganggu ritme penelitian yang sedang ia jaga."
        else:
            yutaka "Kalau kamu harus mantau inkubator sampai jam sepuluh malam, ujung-ujungnya kamu pasti lupa makan malam lagi kan, Kujo-san? Nanti kukirim makanan hangat ke lobi Gedung Sains ya, jangan cuma ganjal perut pakai roti dingin."
            nar "Harumi menaikkan kacamatanya perlahan, sementara sudut bibirnya terangkat tipis."
            harumi "Tebakanmu soal isi tasku agak terlalu tepat, Kisaragi-kun. Tadi aku memang cuma beli satu bungkus roti kacang merah di minimarket sebelum masuk perpustakaan."
            yutaka "Sudah kuduga. Masa libur Natal makan malam cuma pakai roti minimarket di lorong lab yang dingin. Nanti sekitar jam tujuh malam aku minta kedai dekat gerbang depan antar paket nasi hangat sama sup miso ke lobi Gedung Sains. Jam segitu pas sama waktu jeda labmu nggak?"
            harumi "Pukul tujuh lewat lima menit adalah jeda tepat sesudah pencatatan kedelapan. Aku akan turun ke pintu lobi tepat waktu supaya makanannya langsung kuambil sebelum dingin. Terima kasih banyak, Kisaragi-kun."
            yutaka "Sama-sama. Awas kalau sampai dibiarkan dingin gara-gara keasyikan lihat grafik."
            harumi "Tidak akan. Aku sudah menyetel alarm pengingat di ponsel. Oh ya, Kisaragi-kun... di kedai gerbang depan, menu daging panggang saus jahenya tidak terlalu pedas kan?"
            yutaka "Nggak pedas kok, cuma hangat jahe biar enak di tenggorokan. Nanti sekalian kuminta tambah sup miso panas."
            harumi "Komposisi yang sangat tepat. Terima kasih sebelumnya."
            nar "Malam harinya pukul tujuh lewat dua puluh, ponselmu berdenting di atas meja. Satu pesan masuk dari Harumi disertai foto kotak makan hangat berisi nasi, daging panggang saus jahe, dan semangkuk sup miso yang tertata rapi di meja ruang istirahat laboratorium."
            nar "Di bawah foto itu, Harumi mengetik laporan yang begitu rinci khas gayanya. Ia menuliskan makanannya diterima pukul 19.03, suhu sup misonya masih hangat saat dibuka, rasa jahenya cukup kuat mengusir hawa dingin koridor, dan porsinya ideal untuk mempertahankan fokus sampai pukul sepuluh nanti."
            nar "Tak sampai semenit setelah kamu membaca pesan itu, satu balasan singkat menyusul lagi mengingatkan agar kamu juga tidak lupa makan malam yang layak di apartemen, disertai ucapan selamat malam Natal."
            nar "Kamu mengetik balasan singkat untuk mengingatkannya agar langsung pulang begitu pencatatan pukul sepuluh malam selesai."
            nar "Harumi membalas bahwa ia sudah mencatat jadwal bus terakhir di depan gerbang utama dan mengucapkan terima kasih sekali lagi atas makan malamnya."
            nar "Kotak makan hangat di ruang istirahat laboratorium itu menjadi penanda kecil bahwa malam Natalnya tahun ini tidak sepenuhnya berlalu dalam kesunyian."
    else:
        if kk_host == "chiasa":
            chiasa "Oh, masih harus lanjut mantau sampel sampai malam ya, Kujo-senpai. Repot juga ternyata riset kimia. Ya sudah, semangat ya di laboratoriumnya. Aku pulang duluan."
            nar "Harumi sempat terdiam setengah detik, bibirnya bergerak tipis seolah hendak menambahkan satu kalimat lagi, lalu ia menaikkan kacamatanya dan mengangguk sopan."
            harumi "Iya. Terima kasih, Amamiya-san. Hati-hati di jalan pulang, udara di luar sudah turun."
            chiasa "Iya, Senpai. Sampai ketemu habis libur ya."
            nar "Harumi mengangguk tenang, lalu berbalik menuju lorong tangga turun sambil mendekap kedua buku referensinya. Kamu melangkah keluar dari Perpustakaan Pusat menuju arah gerbang tanpa menoleh lagi."
            nar "Sepanjang sisa hari hingga larut malam tidak ada pesan baru di antara kalian. Di lantai dua Gedung Sains yang lengang, Harumi menyelesaikan seluruh siklus pencatatan suhunya tepat sesuai jadwal, memakan roti gandum dingin dari tasnya di ruang istirahat yang kosong, lalu mematikan lampu laboratorium satu per satu tepat pukul sepuluh malam."
            nar "Suara langkah sepatunya bergema sendirian di sepanjang koridor lantai dua yang gelap saat ia mengunci pintu ruang instrumen dan menyerahkan kunci cadangan ke pos penjaga bawah."
            nar "Angin malam Desember berembus dingin di halte depan kampus ketika ia duduk menunggu bus terakhir sambil memangku tas kerjanya dalam diam."
            nar "Tidak ada keluhan yang ia kirimkan ke grup pesan singkat, karena ia selalu menganggap ketahanan bekerja sendirian sebagai bagian dari kewajibannya."
            nar "Sebelum menutup buku catatan hitamnya, ia menuliskan kesimpulan bahwa seluruh parameter reaksi hari itu berjalan sesuai perhitungan awal. Di sudut paling bawah halaman kertas, terselip satu kata pendek yang ia tulis dengan ukuran huruf jauh lebih kecil di luar tabel pengamatan, yaitu kata kecewa."
        else:
            yutaka "Oh, masih lanjut mantau sampel sampai malam ya, Kujo-san. Lumayan ketat juga jadwal labmu. Ya sudah, semangat deh di labnya. Aku balik duluan ya."
            nar "Harumi sempat berhenti setengah detik sambil memegang tepi buku catatannya seperti hendak mengucapkan sesuatu, sebelum akhirnya membetulkan letak kacamatanya dan mengangguk tenang."
            harumi "Iya. Terima kasih, Kisaragi-kun. Hati-hati di jalan, angin di luar cukup dingin."
            yutaka "Sip, sampai ketemu habis liburan."
            nar "Harumi mengangguk sopan lalu berbalik melangkah ke arah tangga turun sambil mendekap buku-buku referensinya. Kamu melangkah keluar dari Perpustakaan Pusat tanpa menoleh kembali."
            nar "Sepanjang sisa hari hingga malam tidak ada satu pun pesan masuk darimu. Di lantai dua Gedung Sains yang sepi, Harumi menyelesaikan seluruh pencatatan suhunya tepat sesuai jadwal, menghabiskan roti dingin yang tersisa di tasnya di ruang istirahat kosong, lalu mematikan lampu laboratorium satu per satu tepat pukul sepuluh."
            nar "Lorong Gedung Sains yang panjang hanya menyisakan bunyi ketukan sepatunya sendiri saat ia turun menyerahkan buku log malam kepada petugas keamanan di lobi."
            nar "Di perjalanan pulang menaiki kereta malam yang lengang, ia hanya duduk memandangi pantulan jendela kaca sambil merapikan catatan waktunya."
            nar "Bagi Harumi yang jarang meminta ditemani secara langsung, perpisahan singkat di perpustakaan tadi sudah cukup menjadi jawaban atas pertanyaannya sendiri."
            nar "Di buku catatan hitamnya, ia menuliskan kesimpulan bahwa jalannya pengamatan hari itu sesuai perkiraan awal. Hanya saja di baris paling bawah halaman, terselip satu kata yang ditulis jauh lebih kecil dan belum berani ia masukkan ke kolom kesimpulan, yaitu kata kecewa."
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
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Lampu meja baca lantai dua Perpustakaan Pusat memancarkan cahaya kuning tenang di antara lorong rak jurnal sains yang hampir kosong. Di luar jendela kaca lebar, langit malam bulan Juli tampak gelap pekat dengan sesekali kilatan lampu kereta komuter melintas di kejauhan."
        else:
            nar "Cahaya matahari awal Juli yang terik disaring rapi oleh tirai vertikal lantai dua Perpustakaan Pusat. Di antara rak jurnal sains yang hening, embusan pendingin ruangan membawa bau kertas tua dan tinta cetakan, sementara di lantai bawah mahasiswa sibuk mengejar salinan bahan ujian."
        nar "Kamu melangkah menuju meja sudut dekat jendela sambil memeluk buku catatan teori senimu serta dua botol kecil teh hijau tawar dingin yang baru saja kamu beli dari mesin minuman di lobi bawah. Di meja sudut itu, Kujo Harumi duduk tegak mengenakan kemeja putih berbalut kardigan abu-abu tipis, rambut abu-abu peraknya dikepang ke samping dengan jepit mawar merah kecil seperti biasa."
        nar "Di hadapannya terbentang selebaran resmi pembukaan program beasiswa riset dan pascasarjana luar negeri dari universitas mitra di Eropa, kamus bahasa Inggris akademik tebal, daftar jadwal ujian bahasa, serta map bening berisi salinan data uji katalisnya."
        nar "Kamu baru saja menaruh salah satu botol teh hijau dingin di sudut meja yang jauh dari lembaran kertas ketika derap langkah sepatu yang teratur berhenti di ujung lorong rak. Ogawa Masato, kandidat doktor dari laboratorium kimia berjas rapi, melangkah mendekat sambil memasang senyum tenang yang terukur."
        "Ogawa" "Kebetulan sekali bertemu di sini, Kujo-san. Kelihatannya kamu sudah mulai mencetak rincian berkas program beasiswa luar negeri itu ya."
        nar "Punggung Harumi langsung menegak sedikit lebih kaku di kursinya. Ia menutup setengah halaman buku catatan hitamnya dan mengangguk sopan."
        harumi "Selamat bertemu, Ogawa-senpai. Saya sedang memeriksa syarat transkrip, skor bahasa, dan jadwal tenggat pengumpulannya terlebih dahulu."
        "Ogawa" "Bagus sekali, kalau persiapanmu secepat ini peluangnya jauh lebih terbuka. Jangan lupa pesan saya kemarin selepas rapat laboratorium ya, Kujo-san. Komite seleksi di universitas mitra itu sangat mengandalkan jalur rekomendasi langsung antarpeneliti yang sudah mereka kenal."
        nar "Kamu duduk pelan di seberang Harumi sambil membuka buku catatanmu, memperhatikan bagaimana pria itu berdiri agak condong ke sisi kursi Harumi dan sama sekali tidak melirik maupun menyapamu sepanjang berbicara."
        "Ogawa" "Kebetulan hanya saya di tim kita yang masih terhubung langsung dengan asisten profesor penguji di sana dan tahu persis format rekomendasi yang mereka cari. Kalau kamu mau datang ke sesi diskusi pribadi saya minggu ini, saya bisa bantu menyusun kerangka berkasmu dari awal supaya rekomendasimu terjamin lolos."
        harumi "Terima kasih atas perhatiannya, Ogawa-senpai. Saya masih perlu memeriksa beberapa ketentuan resmi di selebaran ini lebih dulu sebelum memastikan jadwal."
        "Ogawa" "Tentu, pikirkan baik-baik saja. Cuma jangan terlalu lama menunda, tenggat gelombang pertamanya ketat dan sayang sekali kalau kesempatan sebesar ini lewat begitu saja karena salah langkah di surat rekomendasi. Saya duluan kembali ke laboratorium ya."
        nar "Ogawa mengangguk sopan sekali kepada Harumi tanpa sedikit pun menoleh ke arahmu, lalu melangkah pergi hingga suara sepatunya menghilang di tangga turun."
        nar "Begitu lorong kembali sunyi, kamu memutar tutup botol tehmu dan menggeser botol kedua sedikit lebih dekat ke tangan Harumi."
        chiasa "Minum dulu, Kujo-senpai. Bahu Senpai langsung tegang banget sejak Ogawa-senpai berdiri di samping meja barusan."
        nar "Harumi meraih botol dingin itu dengan kedua tangan, membetulkan letak kacamata tipisnya perlahan, lalu mengembuskan napas pendek yang terdengar berat."
        harumi "Terima kasih, Amamiya-san. Teh tawar memang paling membantu menenangkan pikiran."
        harumi "Transkrip nilai sampai semester ini, skor bahasa Inggris, jadwal tes, sampai kerangka topik katalis yang kuteliti sudah kuperiksa semua. Semuanya masih dalam batas realistis untuk kukejar."
        nar "Tatapanmu jatuh ke halaman pertama selebaran resmi yang terbuka di meja. Hampir seluruh baris persyaratan sudah ditandai rapi dengan stabilo biru muda memakai penggaris, kecuali satu bagian kecil mengenai surat rekomendasi yang dilingkari pensil berulang kali hingga kertasnya berbekas kusut."
        chiasa "Kalau syarat akademiknya sudah aman semua, berarti yang bikin Kujo-senpai bimbang dari tadi cuma ucapan Ogawa-senpai soal surat rekomendasi tadi ya?"
        nar "Harumi membalik halaman kedua selebaran resmi itu menghadap kepadamu lalu menunjuk satu paragraf pendek di tengah halaman."
        harumi "Lihat sendiri, Amamiya-san. Di pengumuman resmi universitas sama sekali tidak tertulis bahwa rekomendasi harus melewati satu asisten peneliti tertentu. Syarat tertulisnya hanya dua surat rekomendasi dari dosen tetap atau kepala laboratorium."
        chiasa "Tertulisnya jelas banget cuma dosen tetap atau kepala laboratorium kok, Senpai."
        harumi "Aku tahu ada yang tidak cocok antara pengumuman resmi ini dengan perkataan Ogawa-senpai. Aku bahkan sudah menuliskan kata 'hanya' itu di catatanku kemarin untuk kuperiksa ulang."
        harumi "Tapi setiap kali mendengar caranya berbicara setenang barusan, aku merasa harus berterima kasih atas bantuannya... sekaligus takut kalau menolak, peluang yang sejak lama kurencanakan bakal langsung tertutup."
        chiasa "{i}Ogawa lagi... persis seperti caranya menarik kendali di lab. Peluang terbesar Kujo-senpai sekarang sengaja dibungkus jadi ketergantungan ke satu orang.{/i}"
        nar "Harumi menatapmu lurus dari balik lensa kacamatanya, kedua tangannya bertumpu rapi di tepi map berkas masa depannya sambil menunggu tanggapanmu."
    else:
        if kk_slot >= 3:
            nar "Lampu meja baca lantai dua Perpustakaan Pusat memancarkan cahaya kuning tenang di antara deretan rak jurnal sains yang lengang. Di luar jendela kaca lebar, langit malam bulan Juli terhampar gelap dengan sesekali kilatan lampu kereta komuter yang melintas di kejauhan."
        else:
            nar "Cahaya terik awal Juli disaring rapi oleh tirai vertikal lantai dua Perpustakaan Pusat. Di antara deretan rak jurnal sains yang sepi, embusan pendingin ruangan membawa aroma kertas tua dan tinta cetakan, sementara di lantai bawah mahasiswa lalu-lalang mengejar salinan bahan ujian."
        nar "Kamu melangkah menuju meja sudut dekat jendela sambil menenteng map catatan ekonomi makromu serta dua botol kecil teh oolong tawar dingin yang baru saja kamu beli dari mesin minuman di lobi bawah. Di meja sudut itu, Kujo Harumi duduk tegak mengenakan kemeja putih berbalut kardigan abu-abu tipis, rambut abu-abu peraknya dikepang samping dengan jepit mawar merah kecil seperti biasa."
        nar "Di hadapannya tersebar selebaran resmi pembukaan program beasiswa riset dan pascasarjana luar negeri dari universitas mitra di Eropa, kamus bahasa Inggris akademik tebal, jadwal tes kecakapan bahasa, serta map bening berisi salinan data uji katalisnya."
        nar "Kamu baru saja meletakkan salah satu botol teh oolong dingin di sudut meja yang jauh dari kertas ketika langkah sepatu yang teratur berhenti di ujung lorong rak. Ogawa Masato, kandidat doktor dari laboratorium kimia berjas rapi, melangkah mendekat sambil memasang senyum tenang yang terukur."
        "Ogawa" "Kebetulan sekali bertemu di sini, Kujo-san. Kelihatannya kamu sudah mulai mencetak rincian berkas program beasiswa luar negeri itu ya."
        nar "Punggung Harumi langsung menegak sedikit lebih kaku di kursinya. Ia menutup setengah halaman buku catatannya dan mengangguk sopan."
        harumi "Selamat bertemu, Ogawa-senpai. Saya sedang memeriksa syarat transkrip, skor bahasa, dan jadwal tenggat pengumpulannya dulu."
        "Ogawa" "Bagus, kalau persiapanmu secepat ini peluangnya jauh lebih terbuka. Jangan lupa pesan saya kemarin selepas rapat laboratorium ya, Kujo-san. Komite seleksi di universitas mitra itu sangat mengandalkan jalur rekomendasi langsung antarpeneliti yang sudah mereka kenal."
        nar "Kamu duduk di seberang Harumi sambil membuka map ekonomimu, mengamati bagaimana pria itu berdiri agak condong ke sisi kursi Harumi dan sama sekali tidak melirik maupun menyapamu sepanjang berbicara."
        "Ogawa" "Kebetulan hanya saya di tim kita yang masih terhubung langsung dengan asisten profesor penguji di sana dan tahu persis format rekomendasi yang mereka cari. Kalau kamu mau datang ke sesi diskusi pribadi saya minggu ini, saya bisa bantu menyusun kerangka berkasmu dari awal supaya rekomendasimu terjamin lolos."
        harumi "Terima kasih atas perhatiannya, Ogawa-senpai. Saya masih perlu memeriksa beberapa ketentuan resmi di selebaran ini terlebih dahulu sebelum memastikan jadwal."
        "Ogawa" "Tentu, pikirkan baik-baik saja. Cuma jangan terlalu lama menunda, tenggat gelombang pertamanya ketat dan sayang sekali kalau kesempatan sebesar ini lewat begitu saja karena salah langkah di surat rekomendasi. Saya duluan kembali ke laboratorium ya."
        nar "Ogawa mengangguk sopan sekali kepada Harumi tanpa sedikit pun menoleh ke arahmu, lalu melangkah pergi hingga suara sepatunya menghilang di tangga turun."
        nar "Begitu lorong kembali sunyi, kamu membuka tutup botol teh oolongmu lalu menggeser botol kedua sedikit lebih dekat ke tangan Harumi."
        yutaka "Minum dulu, Kujo-san. Wajahmu kelihatan tegang banget sejak pria tadi berdiri di samping mejamu."
        nar "Harumi meraih botol dingin itu dengan kedua tangan, membetulkan letak kacamata tipisnya perlahan, lalu mengembuskan napas pendek yang terdengar berat."
        harumi "Terima kasih, Kisaragi-kun. Teh tawar memang paling membantu untuk menenangkan pikiran."
        harumi "Transkrip nilai sampai semester ini, skor bahasa Inggris, jadwal tes, sampai topik katalis yang kuteliti sudah kuperiksa semua. Semuanya masih realistis untuk kukejar."
        nar "Tatapanmu turun ke halaman pertama selebaran resmi yang terbuka di meja. Hampir seluruh baris persyaratan sudah ditandai rapi dengan stabilo biru muda memakai penggaris, kecuali satu bagian kecil mengenai surat rekomendasi yang dilingkari pensil berulang kali sampai kertasnya kusut."
        yutaka "Kalau semua syarat nilaimu sudah aman, berarti satu-satunya yang bikin kamu bimbang dari tadi cuma bagian yang barusan disebut Ogawa itu?"
        nar "Harumi memutar halaman kedua selebaran resmi itu menghadap kepadamu dan menunjuk satu paragraf pendek di tengah halaman."
        harumi "Lihat sendiri, Kisaragi-kun. Di pengumuman resmi universitas sama sekali tidak tertulis bahwa surat rekomendasi harus melalui satu asisten peneliti tertentu. Syarat tertulisnya hanya dua surat rekomendasi dari dosen tetap atau kepala laboratorium."
        yutaka "Jelas banget tertulisnya cuma dosen tetap atau kepala lab."
        harumi "Aku tahu ada yang tidak cocok antara pengumuman resmi ini dengan perkataan Ogawa-senpai. Aku bahkan sudah menuliskan kata 'hanya' itu di catatanku kemarin untuk kuperiksa ulang."
        harumi "Tapi setiap kali mendengar caranya berbicara setenang barusan, aku justru merasa wajib berterima kasih atas bantuannya... sekaligus takut kalau menolak, peluang yang sejak lama kurencanakan bakal langsung tertutup."
        yutaka "{i}Taktik perantara yang klasik banget... bikin pintu resmi kelihatan sempit supaya dia bisa berdiri di depan gemboknya dan bikin Kujo-san percaya cuma dia satu-satunya kunci.{/i}"
        nar "Harumi memandangmu lurus dari balik lensa kacamatanya, kedua tangannya bertumpu rapi di tepi map berkas masa depannya sambil menunggu tanggapanmu."
    call kk_family_menu("H11", ["\"Jangan tergantung pada satu orang. Kejar beasiswanya lewat jalur resminya sendiri.\"", "\"Jujur aja, aku belum rela kalau sampai pergi jauh. Ini murni keinginanku sendiri.\"", "Arahkan rencananya agar bergantung pada dukungan dan persetujuanmu."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu menarik selebaran itu sedikit lebih dekat, membaca tuntas baris demi baris ketentuan surat rekomendasi resmi, lalu mengetuk pelan paragraf keempat tersebut dengan ujung jarimu."
            chiasa "Kujo-senpai, coba baca ulang baris yang barusan Senpai tunjuk sendiri deh. Di sini tertulis jelas syaratnya dua surat rekomendasi dari dosen tetap atau kepala laboratorium, kayak Prof. Mizuhara. Nama Ogawa-senpai bahkan nggak muncul di syarat wajib mana pun."
            harumi "Di selebarannya memang tertulis begitu, Amamiya-san. Tapi bagaimana kalau panitia di universitas mitra benar-benar memberi bobot lebih besar pada komunikasi tidak resmi yang disebut Ogawa-senpai barusan?"
            chiasa "Coba kita bandingkan pelan-pelan deh, Senpai. Antara kandidat doktor berusia dua puluh sembilan tahun yang belum jadi dosen tetap sama Prof. Mizuhara yang memimpin laboratorium sekaligus rutin menerbitkan jurnal internasional, siapa yang tanda tangannya jauh lebih dihormati profesor di Eropa?"
            nar "Harumi terdiam dua detik, matanya sedikit melebar di balik kacamata ketika perbandingan sederhana itu langsung meruntuhkan keraguannya."
            harumi "...Jelas Prof. Mizuhara. Beliau punya rekam jejak publikasi internasional jauh lebih panjang dan merupakan kepala laboratorium resmi tempat penelitianku terdaftar."
            chiasa "Betul, Senpai! Ditambah lagi aku lihat sendiri sikap Ogawa-senpai di samping meja tadi. Kalau dia beneran tulus mau bantu junior labnya, harusnya dia ngomong terbuka di depan Prof. Mizuhara waktu rapat."
            chiasa "Dia nggak perlu menunggumu sendirian, mengabaikan orang di depan meja, terus menakut-nakutimu pakai kata 'hanya saya' supaya Senpai datang ke sesi pribadinya."
            nar "Embusan napas panjang yang terdengar sangat lega akhirnya keluar dari bibir Harumi. Ia membuka buku catatan hitam kecilnya pada halaman catatan rapat kemarin, meraih pulpen hitamnya, lalu menarik satu garis lurus mantap mencoret kata 'hanya' yang sebelumnya sempat ia tuliskan."
            harumi "Argumenmu tajam sekali, Amamiya-san. Aku sempat terkecoh karena terlalu sibuk menghitung kemungkinan gagal sampai lupa menguji kebenaran kata 'hanya' itu sendiri."
            harumi "Mengejar beasiswa ini lewat jalur bersih tanpa menggantungkan seluruh pintu ke satu orang jelas jauh lebih masuk akal."
            chiasa "Nah, biar langsung jelas dan nggak kepikiran lagi, langkah pertama Senpai besok mau mulai dari mana?"
            harumi "Besok selepas kelas pagi aku akan langsung menghadap ke ruang kerja Prof. Mizuhara membawa selebaran ini untuk menanyakan prosedur rekomendasi resmi sekaligus meminta arahan beliau soal surat kedua dari ketua jurusan, tanpa perantara siapa pun."
            chiasa "Langkah yang rapi banget, Senpai! Nanti habis pekan ujian ini selesai, kalau Senpai butuh bantuan merapikan tata letak diagram poster riset atau sekadar bantu cek daftar tenggat berkasnya, ajak aku aja ya."
            harumi "Terima kasih banyak, Amamiya-san. Aku baru sungguh-sungguh memahami bedanya hari ini. Aku memang masih boleh membutuhkan bantuan orang lain untuk hal-hal tertentu, dan itu sama sekali tidak sama dengan membiarkan satu orang menentukan seluruh syarat hidupku."
            nar "Sorot mata abu-kebiruan Harumi di balik kacamatanya kembali jernih dan mantap. Ia mulai menuliskan jadwal janji temu resmi dengan Prof. Mizuhara di sudut kalendernya dengan gerakan pena yang tidak lagi ragu sedikit pun."
        else:
            nar "Kamu menarik selebaran itu sedikit lebih dekat ke arahmu, membaca tuntas baris demi baris syarat surat rekomendasi dan alur pendaftaran resmi, lalu mengetuk kertas itu dua kali dengan punggung jari telunjukmu."
            yutaka "Kujo-san, di dunia bisnis maupun kampus, begitu ada perantara yang sengaja membuat pintu resmi kelihatan sempit lalu mengklaim akses cuma lewat dirinya, tujuannya jelas mau mengunci ketergantunganmu. Lihat baris keempat brosur ini. Syarat resminya dua dosen tetap atau kepala laboratorium. Nama Ogawa sama sekali nggak tercantum di daftar mana pun."
            harumi "Secara administratif tertulis memang begitu, Kisaragi-kun. Tapi bagaimana kalau panitia di universitas mitra benar-benar memberi bobot lebih besar pada komunikasi tidak resmi yang disebut Ogawa-senpai tadi?"
            yutaka "Coba kamu uji pakai logika objektifmu sendiri deh. Antara kandidat doktor berusia dua puluh sembilan tahun yang bahkan belum jadi dosen tetap dengan Prof. Mizuhara yang memimpin laboratorium sekaligus rutin menerbitkan jurnal internasional, siapa yang tanda tangannya jauh lebih dihormati profesor di Eropa?"
            nar "Harumi terdiam dua detik, matanya sedikit melebar ketika perbandingan sederhana itu langsung meruntuhkan celah ketakutannya."
            harumi "...Jelas Prof. Mizuhara. Beliau punya rekam jejak publikasi internasional jauh lebih panjang dan merupakan kepala laboratorium resmi tempat penelitianku terdaftar."
            yutaka "Persis. Dan satu lagi yang tadi kulihat langsung dari sikapnya barusan. Kalau Ogawa beneran punya kenalan bersih di luar negeri dan tulus ingin menolong junior labnya, dia tinggal ngomong terbuka di ruang rapat di depan Prof. Mizuhara. Dia nggak perlu menunggumu sendirian, mengabaikan teman di sebelahmu, lalu menakut-nakutimu dengan kata 'hanya saya' supaya kamu datang ke sesi pribadinya."
            nar "Embusan napas panjang yang akhirnya terdengar sangat lega keluar dari bibir Harumi. Ia membuka buku catatan hitam kecilnya pada halaman catatan rapat kemarin, meraih pulpen hitamnya, lalu menarik satu garis lurus mantap mencoret kata 'hanya' yang sebelumnya sempat ia tuliskan."
            harumi "Analisismu sangat jernih, Kisaragi-kun. Aku sempat terkecoh karena terlalu sibuk menghitung kemungkinan gagal sampai lupa menguji kebenaran kata 'hanya' itu sendiri. Mengejar beasiswa ini lewat jalur bersih tanpa bergantung pada satu orang jelas pilihan yang jauh lebih sehat."
            yutaka "Nah, biar langsung konkret dan nggak kepikiran lagi, langkah pertamamu besok mau mulai dari mana?"
            harumi "Besok selepas jam kuliah pertama aku akan langsung menghadap ke ruang kerja Prof. Mizuhara membawa selebaran ini untuk menanyakan prosedur rekomendasi resmi sekaligus meminta arahan beliau soal surat kedua dari ketua jurusan, tanpa perantara siapa pun."
            yutaka "Langkah yang rapi banget. Coba sekalian catat batas tanggal tes bahasa Inggrisnya di bagian depan biar nggak tabrakan sama jadwal lab bulan depan."
            harumi "Sudah kucatat di kalender saku. Dan... Kisaragi-kun, terima kasih banyak sudah membantuku memisahkan persyaratan dokumen dari klaim pribadi barusan."
            yutaka "Santai aja. Nanti begitu pekan ujian ini kelar, kalau kamu butuh lawan bicara buat latihan wawancara bahasa Inggris atau ngecek kejelasan abstrak risetmu buat pembaca awam, tinggal kabari aku."
            harumi "Baik, dengan senang hati. Aku baru sungguh-sungguh mengerti bedanya hari ini. Aku tetap boleh membutuhkan bantuan orang lain untuk hal-hal tertentu, dan itu sama sekali tidak sama dengan mengizinkan satu orang menentukan seluruh syarat masa depanku."
            nar "Sorot mata abu-kebiruan Harumi di balik kacamatanya kembali bersih dan mantap. Ia mulai menuliskan jadwal janji temu resmi dengan Prof. Mizuhara di sudut kalendernya dengan gerakan pena yang tidak lagi ragu sedikit pun."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Alih-alih menunjuk paragraf persyaratan ataupun membahas klaim Ogawa, kamu meletakkan pensilmu di atas buku catatan, terdiam cukup lama memandangi lambang universitas Eropa di sudut atas brosur, lalu mengangkat wajah menatap Harumi lurus-lurus."
            chiasa "Kujo-senpai... aku tahu banget peluang ini besar buat masa depan Senpai, dan secara akademik Senpai jelas sanggup lolos lewat jalur resmi tanpa campur tangan Ogawa sedikit pun. Tapi kalau boleh jujur banget sekali ini, aku belum rela kalau Senpai sampai pergi jauh ke luar negeri secepat ini."
            nar "Harumi langsung membeku di kursinya. Ujung jari di tangan kanannya berhenti bergerak di atas kertas brosur, sementara matanya melebar tipis di balik kacamata seolah sedang menghadapi satu variabel besar yang tidak pernah ada di dalam daftar catatannya."
            harumi "...Tunggu sebentar, Amamiya-san. Kamu barusan sungguh-sungguh memintaku tetap tinggal di sini?"
            chiasa "Iya, Senpai. Aku nggak lagi kasih saran karier ataupun meragukan kesiapan riset Senpai sedikit pun. Ini murni keinginanku sendiri sebagai Chiasa."
            nar "Kamu mencondongkan bahu sedikit di atas meja agar suara pelanmu terdengar jelas di kesunyian lantai dua perpustakaan."
            chiasa "Sejak kita makin sering duduk satu meja, minum teh bareng, dan ngobrol panjang begini, aku baru sadar kehadiran Kujo-senpai beneran berarti buatku. Aku jujur belum siap kalau tahun depan kursi di seberang meja ini mendadak kosong gara-gara Senpai pindah ke belahan dunia lain."
            nar "Keheningan yang sangat pekat turun di meja sudut perpustakaan itu. Alih-alih langsung menepis ucapanmu dengan daftar alasan rasional tentang peringkat universitas seperti kebiasaannya, Harumi menatapmu lekat-lekat selama beberapa detik untuk memastikan kesungguhan di balik setiap katamu."
            harumi "Tolong pastikan satu hal dulu, Amamiya-san. Kalimat tadi murni kamu sampaikan sebagai keinginan dirimu sendiri, tanpa dibungkus sebagai saran sopan atau kekhawatiran apakah aku sanggup bertahan hidup sendiri di luar negeri?"
            chiasa "Sama sekali nggak ada keraguan soal kemampuan Senpai. Aku tahu Senpai sanggup bertahan di mana aja. Aku cuma egois dan jujur bilang aku sendiri yang pengin Senpai tetap di sini lebih lama."
            nar "Rona merah samar perlahan naik ke pangkal telinga Harumi. Ia membetulkan letak kacamatanya dengan gerakan jauh lebih lambat daripada biasanya, lalu menunduk memandangi lembaran brosur yang sejak dua minggu lalu ia tandai rapi dengan stabilo biru."
            harumi "...Kalau kamu menyampaikannya sejujur itu sebagai dirimu sendiri, maka aku tidak bisa menyingkirkannya begitu saja dari perhitunganku. Aku akan sungguh-sungguh mempertimbangkannya, Amamiya-san."
            chiasa "Aku nggak memaksa Senpai langsung jawab hari ini kok. Aku cuma nggak mau pura-pura santai soal kepergian Senpai padahal aslinya aku keberatan."
            harumi "Aku mengerti. Rasanya aneh sekaligus berat sekali... seluruh syarat objektif, daftar laboratorium mitra, sampai keuntungan akademik di brosur ini sudah kuhitung matang selama dua minggu, tetapi satu keinginan pribadimu barusan langsung menggeser seluruh bobot timbangannya."
            nar "Harumi merapikan lembaran brosur dan menutup map berkas katalisnya pelan tanpa lagi melingkari tanggal batas pengiriman gelombang pertama. Kamu melihat dengan sangat jelas bagaimana keinginan dan persetujuanmu kini mulai masuk terlampau jauh ke dalam cara ia menakar nilai keputusannya sendiri."
        else:
            nar "Kamu meletakkan pulpenmu pelan di atas map ekonomi, terdiam cukup lama memandangi lambang universitas Eropa di sudut atas brosur, lalu mengangkat pandangan menatap Harumi lurus tanpa sedikit pun nada jahil seperti kebiasaanmu."
            yutaka "Kujo-san, terus terang aja. Kalau ngomongin soal kemampuan, kamu jelas sanggup lolos beasiswa itu lewat jalur resmi tanpa perlu campur tangan Ogawa sedikit pun. Tapi kalau aku boleh jujur sekali ini, aku belum rela melihat kamu pergi jauh ke luar negeri secepat ini."
            nar "Harumi langsung membeku di kursinya. Jari-jarinya yang tadi menyentuh pinggiran brosur terhenti kaku, sementara matanya di balik lensa kacamata melebar tipis seolah sedang menghadapi satu variabel besar yang tidak pernah ada di dalam daftar catatannya."
            harumi "...Kisaragi-kun. Kamu barusan sungguh-sungguh memintaku tetap tinggal di sini?"
            yutaka "Iya. Aku nggak lagi kasih nasihat akademik ataupun meragukan kesiapan risetmu sedikit pun. Itu murni keinginanku sendiri sebagai Kisaragi Yutaka."
            nar "Kamu mencondongkan bahu sedikit di atas meja agar suara pelanmu terdengar sangat jelas di kesunyian perpustakaan."
            yutaka "Sejak kita makin sering duduk satu meja, bahas catatan, dan ngobrol panjang begini, aku baru sadar kehadiranmu di sini benar-benar penting buatku. Aku jujur belum siap kalau tahun depan bangku di seberang meja ini tiba-tiba kosong karena kamu pindah ke belahan dunia lain."
            nar "Keheningan yang sangat pekat turun di sudut lantai dua itu. Alih-alih langsung menepis ucapanmu dengan daftar alasan objektif tentang peringkat riset atau masa depan karier seperti kebiasaannya, Harumi menatap wajahmu lama sekali untuk memeriksa kesungguhan di balik setiap kata yang baru saja kamu ucapkan."
            harumi "Tolong pastikan satu hal dulu, Kisaragi-kun. Kalimat tadi murni kamu sampaikan sebagai keinginan dirimu sendiri, tanpa dibungkus sebagai saran sopan atau keraguan apakah aku sanggup bertahan hidup sendiri di luar negeri?"
            yutaka "Sama sekali nggak ada keraguan soal kemampuanmu, Kujo-san. Aku tahu kamu sanggup bertahan di mana aja. Aku cuma egois dan jujur bilang aku sendiri yang ingin kamu tetap di sini lebih lama."
            nar "Rona merah samar perlahan naik ke pangkal telinga Harumi. Ia membetulkan letak kacamatanya dengan gerakan jauh lebih pelan daripada biasanya, lalu menunduk memandangi lembaran brosur yang sejak dua minggu lalu ia tandai rapi dengan stabilo biru."
            harumi "...Kalau kamu menyampaikannya sejujur itu sebagai dirimu sendiri, aku tidak bisa menyingkirkannya begitu saja dari perhitunganku. Aku akan sungguh-sungguh mempertimbangkannya, Kisaragi-kun."
            yutaka "Aku nggak memaksa kamu langsung mengambil keputusan hari ini kok. Aku cuma nggak mau pura-pura santai soal kepergianmu padahal aslinya aku keberatan."
            harumi "Aku paham. Rasanya asing sekaligus berat sekali... seluruh syarat objektif, daftar laboratorium mitra, sampai keuntungan akademik di brosur ini sudah kuhitung matang selama dua minggu, tetapi satu keinginan pribadimu barusan langsung menggeser seluruh bobot timbangannya."
            nar "Harumi merapikan lembaran brosur dan menutup map berkas katalisnya pelan tanpa lagi melingkari tanggal batas pengiriman gelombang pertama. Kamu menyaksikan dengan sangat jelas bagaimana keinginan dan persetujuanmu kini mulai masuk terlampau dalam ke dalam cara ia menakar nilai keputusannya sendiri."
    else:
        if kk_host == "chiasa":
            nar "Melihat kebimbangan di wajah Harumi yang terjepit antara takut kehilangan dukungan dan besarnya taruhan beasiswa itu, kamu menyandarkan kedua siku di tepi meja lalu menurunkan nada bicaramu hingga terdengar hangat sekaligus menyimpan tekanan halus."
            chiasa "Jujur aja ya, Kujo-senpai, lingkungan laboratorium di luar negeri itu jauh lebih keras dan politik akademiknya jauh lebih licin kalau Senpai nekat berangkat tanpa pegangan yang aman. Di kampus sini aja Senpai masih sering bingung membaca manuver halus orang kayak Ogawa-senpai barusan."
            nar "Bahu Harumi langsung sedikit menegang mendengar kalimat itu. Ia mengerjap pelan menatapmu dari balik lensa kacamatanya."
            harumi "Menurut penilaian Amamiya-san... aku belum cukup siap untuk menghadapi lingkungan riset di sana sendirian?"
            chiasa "Aku nggak bilang nilai atau kemampuan riset Senpai kurang, cuma membaca niat orang itu nggak ada rumusnya di buku teks. Selama Senpai tetap di sini, menunda dulu pendaftaran jauh itu, dan membicarakan langkah besar Senpai denganku lebih dulu, aku selalu siap bantu Senpai menghadapi tekanan di lab maupun urusan lainnya."
            nar "Kamu diam setengah detik, membiarkan keheningan menekan meja agar kalimat berikutnya jatuh tepat di tengah kecemasannya."
            chiasa "Tapi kalau Senpai tetap maksain mengejar gelombang luar negeri sekarang dan mengabaikan pertimbanganku, terus terang aku juga nggak yakin bakal punya banyak waktu lagi buat terus nemenin atau bantu urusan Senpai di sini."
            nar "Keheningan dingin menggantung di atas meja sudut perpustakaan. Harumi menatap lembar persyaratan beasiswa di hadapannya dengan jemari sedikit gemetar di tepi kertas mengilap itu. Ia sama sekali tidak sempat bertanya kepada dirinya sendiri apakah ia sungguh-sungguh ingin melepas rencana gelombang pertama; yang segera ia tangkap adalah bahwa dukungan dan kehadiranmu hanya bertahan selama ia memilih jalan yang kamu setujui."
            nar "Dengan tarikan pensil yang cepat dan terlalu kaku, Harumi membuka buku agendanya lalu mencoret tanggal pendaftaran gelombang pertama bulan ini hingga bekas grafitnya tebal."
            harumi "Kalau begitu... aku ubah bagian ini dulu. Aku tunda pendaftarannya dan kusesuaikan jadwal risetku dengan rencana di kampus seperti yang Amamiya-san sarankan tadi."
            nar "Ia mendongak menatapmu dengan sorot mata abu-kebiruan penuh harap yang tampak rapuh sekaligus cemas."
            harumi "Setelah aku mengubah rencananya seperti ini... Amamiya-san masih tetap mau membantu dan meluangkan waktu duduk bersamaku di sini, kan?"
            chiasa "Tentu aja, Senpai. Kan jauh lebih tenang dan aman kalau kita jalan bareng mengikuti rencana yang sudah sama-sama disepakati."
            harumi "...Baik. Terima kasih, Amamiya-san. Aku langsung menyesuaikan daftar tugasku hari ini juga."
            nar "Harumi mengembuskan napas lega yang tipis lalu memasukkan selebaran beasiswanya ke bagian paling bawah tasnya. Ia mulai menukar arah hidupnya sendiri sebelum sempat memeriksa apakah ia sungguh-sungguh menginginkannya."
        else:
            nar "Melihat kebimbangan Harumi yang terimpit antara takut kehilangan dukungan dan besarnya pertaruhan beasiswa itu, kamu menyandarkan kedua lengan di tepi meja lalu menurunkan suaramu dengan nada tenang yang terdengar logis sekaligus menyimpan syarat dingin."
            yutaka "Realistis aja, Kujo-san. Lingkungan laboratorium luar negeri itu jauh lebih keras dan politik akademiknya jauh lebih licin kalau kamu nekat melangkah tanpa pegangan yang aman. Di kampus sini aja kamu masih sering kesusahan membaca manuver halus orang kayak Ogawa barusan."
            nar "Pundak Harumi langsung sedikit menegang mendengar kalimat itu. Ia mengerjap pelan menatapmu dari balik lensa kacamatanya."
            harumi "Menurut penilaian Kisaragi-kun... aku belum cukup siap untuk menghadapi lingkungan riset di sana sendirian?"
            yutaka "Aku nggak bilang nilai atau kemampuan hitungmu kurang, cuma membaca niat orang itu nggak ada rumusnya di buku teks. Selama kamu tetap di sini, menunda dulu pendaftaran jauh itu, dan membicarakan langkah besarmu denganku lebih dulu, aku selalu siap bantu memantau urusan lab maupun menghadapi tekanan Ogawa buatmu."
            nar "Kamu diam setengah detik, membiarkan keheningan menekan meja agar kalimat berikutnya jatuh tepat di tengah kecemasannya."
            yutaka "Tapi kalau kamu tetap memaksakan diri mengejar gelombang luar negeri sekarang dan mengabaikan pertimbanganku, terus terang aku juga nggak bakal punya banyak waktu lagi buat terus membantu atau mendampingi urusanmu di sini."
            nar "Keheningan kaku turun di atas meja sudut perpustakaan. Harumi menatap brosur beasiswa di hadapannya dengan jemari sedikit gemetar di tepi kertas mengilap itu. Ia sama sekali tidak sempat menanyakan kepada dirinya sendiri apakah ia sungguh-sungguh ingin melepas rencana gelombang pertama; yang langsung ia tangkap adalah bahwa dukungan dan perhatianmu hanya bertahan selama ia memilih arah yang kamu setujui."
            nar "Dengan tarikan pensil yang cepat dan terlalu kaku, Harumi membuka buku agendanya lalu mencoret jadwal pendaftaran gelombang pertama bulan ini hingga bekas grafitnya tebal."
            harumi "Kalau begitu... aku ubah bagian ini dulu. Aku tunda pendaftarannya dan kusesuaikan jadwal risetku dengan rencana di kampus seperti yang kamu sarankan tadi."
            nar "Ia mengangkat wajah menatapmu dengan sorot mata abu-kebiruan penuh harap yang tampak rapuh sekaligus cemas."
            harumi "Setelah aku mengubah rencanaku seperti ini... Kisaragi-kun masih tetap mau membantu dan meluangkan waktu duduk bersamaku di sini, kan?"
            yutaka "Tentu. Jauh lebih aman kalau kita jalan mengikuti rencana yang sudah jelas dan sama-sama kita sepakati."
            harumi "...Baik. Terima kasih, Kisaragi-kun. Aku langsung menyesuaikan daftar tugasku hari ini juga."
            nar "Harumi mengembuskan napas lega yang tipis lalu memasukkan selebaran beasiswanya ke bagian paling bawah tasnya. Ia mulai menukar arah masa depannya sendiri sebelum sempat memeriksa apakah ia sungguh-sungguh menginginkannya."
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
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Lampu baca meja sudut di lantai dua Perpustakaan Pusat memancarkan cahaya putih lembut di antara rak-rak jurnal yang sunyi. Di luar kaca besar, angin bulan Oktober menggerakkan bayangan daun di halaman kampus."
        else:
            nar "Cahaya bulan Oktober mengalir tenang melalui jendela kaca tinggi Perpustakaan Pusat. Di meja sudut lantai dua yang hanya diisi bunyi lembaran kertas dibalik dan dengung pelan pendingin ruangan, kamu meletakkan dua gelas kertas teh panggang hangat."
        nar "Harumi duduk tegak mengenakan kardigan abu-abu tipis dengan rambut abu-abu perak panjang berkepang samping dan sanggul kecil berhiasan jepit mawar merah. Di depan sikunya terbuka buku catatan saku presisi yang biasa ia pakai mencatat data kimia, sementara di sisi kirinya tersusun map kolaborasi poster riset kalian."
        nar "Ia mengangkat gelas kertas teh panggang yang baru kamu letakkan, merasakan hangat dinding gelasnya sejenak di telapak tangan sebelum mengangguk pelan."
        harumi "Terima kasih untuk teh panggangnya, Amamiya-san. Suhunya sekitar tujuh puluh lima derajat, masih cukup layak untuk mesin minuman lantai bawah. Ini salinan koreksi skala grafik untuk poster riset kita yang kemarin kamu titipkan."
        chiasa "Cepat sekali beresnya, Kujo-senpai. Makasih ya, bagian label sumbu sebelah kirinya juga sudah Senpai tandai?"
        harumi "Sudah. Aku menempelkan tiga catatan kecil di sudutnya agar kamu tidak perlu mengulang ukuran huruf dua kali. Jarak antarhuruf pada judul tabelnya memang sedikit terlalu rapat bagi mata penguji di baris belakang."
        chiasa "Hehe, selalu teliti sampai ke jarak huruf segala ya, Senpai."
        harumi "Kejelasan visual menghemat empat puluh persen pertanyaan ulang saat sesi tanya jawab. Secara efisiensi, itu cukup menguntungkan."
        nar "Saat Harumi menggeser map poster itu ke hadapanmu, kamu melihat bekas noda tinta hitam tipis di sisi jari telunjuk kanannya, tanda bahwa ia sudah menggaris halaman cukup lama sejak tadi. Tepat di samping sikunya, buku catatan sakunya masih terbuka lebar."
        nar "Halaman itu sama sekali kosong dari rumus katalis; di atasnya justru tergambar tiga garis kolom rapi bertinta hitam halus."
        chiasa "Tunggu dulu, Kujo-senpai... itu bukan tabel data laboratorium kan? Kok judul kolomnya ada bantuan yang diberikan, balasan yang diterima, sama syarat akses?"
        nar "Harumi membetulkan letak kacamata bingkai tipisnya dengan satu jari. Ia tidak buru-buru menutup buku itu ataupun terlihat malu, justru memutarnya pelan menghadap ke arahmu agar kamu bisa membaca seluruh isinya dengan jelas."
        nar "Di dalam tiga kolom tersebut tertulis catatan yang membuat dadamu terasa dingin. Baris pertama menuliskan menyusun ulang lampiran data untuk Ogawa berpasangan dengan akses ruang spektrometer setelah jam kuliah. Baris di bawahnya menuliskan menemani diskusi tambahan senior lab berpasangan dengan nama tetap masuk daftar publikasi."
        nar "Di baris ketiga tertulis lagi meminjamkan catatan kuliah penuh berpasangan dengan tetap diajak masuk obrolan kelompok belajar."
        chiasa "Sampai urusan menemani diskusi tambahan sama meminjamkan catatan kuliah juga Senpai masukkan ke tabel pertukaran..."
        nar "Harumi membalik mundur satu halaman sebelumnya, memperlihatkan catatan kecil yang jauh lebih sederhana sebelum seluruhnya berubah menjadi kolom berpagar garis kaku."
        harumi "Bulan lalu aku masih mencatat bantuan kecil di asrama dan perpustakaan sebagai titik referensi awal. Setelah berdiskusi panjang dengan Ogawa minggu lalu, aku memindahkan semuanya ke dalam tiga kolom ini."
        chiasa "Kenapa setiap barisnya harus diberi angka balasan begini, Kujo-senpai?"
        harumi "Awalnya aku mulai mencatat ini untuk memahami pola interaksi manusia yang selama ini sering terlewat olehku, Amamiya-san. Seperti mencatat perubahan suhu di ruang reaksi agar tidak ada variabel yang meledak di luar perhitungan."
        chiasa "Tapi lama-kelamaan catatan Senpai berubah jadi kayak daftar harga yang harus dibayar dulu sebelum boleh dekat sama orang..."
        harumi "Ogawa menjelaskan kepadaku bahwa semua kedekatan pada dasarnya memiliki pertukaran. Menurutnya, tidak ada perhatian yang benar-benar gratis, dan menganggap orang lain peduli tanpa syarat hanya membuat kita salah menghitung lalu berakhir kecewa."
        harumi "Ia bilang rasa bingungku saat membaca perasaan orang lain terjadi karena aku terus mengira interaksi sosial berjalan tanpa kontrak tertulis."
        if kk_has("harumi_dimanfaatkan"):
            harumi "Belakangan aku juga melihat sendiri bahwa setiap kali seseorang menawarkan bantuan atau waktu kepadaku, selalu ada jadwal atau syarat tertentu yang ikut menyertainya."
        nar "Mata abu-kebiruan Harumi turun menatap deretan garis hitam yang baru ia tambah dengan penggaris logam kecil. Kalung lambang atom di lehernya berkilau tipis saat ia mengembuskan napas pelan."
        harumi "Aku mencoba memperlakukannya sebagai eksperimen sosial. Aku mencari hal konkret yang bisa kuberikan lebih dulu supaya aku punya hak meminta perhatian tanpa salah berharap."
        chiasa "Terus... setelah Senpai mencatat semuanya serapi ini dan membayar tiap barisnya, apakah Senpai merasa lebih tenang?"
        harumi "Justru di situ anomali datanya, Amamiya-san. Semakin jelas daftar pertukarannya dan semakin tepat aku membayarnya, semakin sedikit aku tahu apakah orang-orang itu benar-benar ingin mengenalku."
        chiasa "{i}Ia membungkus rasa takut ditolak memakai tabel dan aturan yang ditanamkan Ogawa, seolah kalau semua hal diberi harga sejak awal, ia tidak akan pernah dikecewakan lagi.{/i}"
        call kk_family_menu("H12", ["\"Hentikan eksperimen itu, Kujo-senpai. Kedekatan nggak berjalan pakai daftar harga.\"", "\"Kalau menurut Senpai cara ini masuk akal, ayo kita uji variabel pertukarannya bareng.\"", "\"Kalau semua memang perlu imbal balik, kebetulan ada hal yang bisa Senpai bantu untukku sekarang.\""])
        if _return == "A":
            nar "Kamu meletakkan dua jarimu pelan di pinggir halaman buku catatan itu agar pena Harumi berhenti bergerak, lalu menatapnya lurus."
            chiasa "Hentikan eksperimen itu sebelum Senpai benar-benar memercayainya, Kujo-senpai. Kedekatan antara dua orang sama sekali nggak berjalan seperti transaksi yang dibilang Ogawa."
            nar "Harumi berkedip pelan di balik kacamatanya, keningnya berkerut menimbang sanggahanmu dengan keseriusan penuh."
            harumi "Kamu mengatakan kedekatan tidak bertumpu pada pertukaran? ...Pernyataan itu bertentangan langsung dengan seluruh argumen yang Ogawa ajarkan kepadaku beberapa minggu ini. Secara praktis, bukankah setiap orang memberi waktu dan tenaga karena mengharapkan timbal balik?"
            chiasa "Waktu Kujo-senpai menyeduhkan teh hangat buat teman-teman di asrama dulu, atau waktu aku datang membawakan teh panggang dan menemani Senpai di meja sudut ini, memangnya kita pernah menaruh nota tagihan di antara kita?"
            harumi "Itu... aku memang tidak mencatat biayanya waktu itu, tapi di dalam kepalaku aku tetap berpikir suatu saat harus membalas dengan nilai setara. Kalau tidak ada nilai tukar yang terukur, dari mana aku tahu kapan kehadiranku mulai mengganggu orang lain?"
            chiasa "Dari jawaban jujur orang itu sendiri, Kujo-senpai. Di hubungan yang sehat, orang boleh bilang sedang capek atau menolak tanpa langsung dianggap memutus segalanya."
            chiasa "Sekarang coba Senpai lihat sendiri tiga kolom di buku catatan itu. Kalau suatu hari Kujo-senpai bilang nggak mau, atau bilang hari ini nggak sanggup menemani diskusi tambahan, di kolom mana kamu tetap berhak dihormati?"
            nar "Seluruh gerak tangan Harumi berhenti seketika. Mata abu-kebiruannya menyapu pelan dari judul kolom paling kiri ke kolom kanan, lalu turun menyusuri seluruh baris kosong di bawahnya."
            harumi "...Di sini tidak ada kolom untuk penolakan."
            chiasa "Iya. Di aturan buatan Ogawa, satu-satunya cara supaya Senpai tetap dianggap berharga adalah dengan terus menyetujui syaratnya. Itu jebakan, Senpai."
            nar "Pandangan Harumi tertahan sejenak pada baris pertama yang menyebut nama Ogawa. Alisnya sedikit mengernyit ketika sebuah ingatan konkret rupanya baru saja tersambung di kepalanya."
            harumi "Minggu lalu ketika aku mengatakan lelah dan ingin pulang lebih awal ke asrama, Ogawa tidak memarahiku. Ia hanya mengingatkan pelan soal jadwal penggunaan alat dan surat rekomendasi."
            chiasa "Nah, itu persis buktinya. Ia nggak pernah kasih Senpai ruang aman buat menolak. Bandingkan sama Prof. Mizuhara atau Ogiwara-san di asrama, memangnya mereka pernah menagih balasan setiap kali mereka membantu Senpai?"
            harumi "...Tidak pernah. Ogiwara-san bahkan sering menyimpan teh tambahan di dapur asrama tanpa mencatat siapa yang meminumnya."
            chiasa "Karena perhatian yang tulus memang nggak punya buku tagihan, Senpai."
            nar "Harumi menatap lembaran tintanya selama beberapa detik yang hening. Pelan sekali, ia membuka tutup penanya lalu menarik satu garis miring panjang yang tegas menembus seluruh kolom daftar harga itu."
            harumi "Aku menghapus pilihan untuk menolak bahkan sebelum eksperimennya dimulai. Pantas seluruh hasil pengamatanku selalu mengarah ke kesimpulan yang sama."
            chiasa "Sekarang tutup dulu buku catatannya, Kujo-senpai. Minum teh panggangnya mumpung masih hangat."
            harumi "...Berarti sekarang aku boleh duduk di sini meminum teh bersamamu tanpa perlu menambahkan koreksi poster tambahan sebagai imbalan?"
            chiasa "Nggak ada tagihan apa-apa di meja ini, Kujo-senpai. Minum saja dengan tenang."
            nar "Harumi menatap gelas teh panggangnya sejenak, lalu sudut bibirnya terangkat sangat tipis membentuk senyum canggung yang jarang tampak di wajahnya."
            harumi "Data yang aneh... tapi untuk pertama kalinya dalam dua minggu, kepalaku terasa jauh lebih ringan tanpa harus menghitung apa pun."
            harumi "Terima kasih sudah menghentikan perhitunganku sebelum berubah menjadi kebiasaan, Amamiya-san. Aku perlu memikirkan ulang semua yang Ogawa katakan kepadaku."
            nar "Untuk pertama kalinya hari itu, bahu Harumi turun pelan saat ia membalik buku catatannya ke halaman kosong dan mengangkat gelas teh hangat di hadapannya."
        elif _return == "B":
            nar "Kamu memandangi tabel rapi di buku catatan itu beberapa detik lalu mengangguk tenang, ikut masuk ke dalam kerangka eksperimen yang baru saja ia bangun."
            chiasa "Sebenarnya aku bisa paham kenapa Kujo-senpai bikin tabel seperti ini. Kalau pertukarannya jelas dan seimbang dari awal, memang lebih kecil kemungkinan ada pihak yang merasa dimanfaatkan atau salah paham."
            nar "Kilat lega yang jarang terlihat langsung melintas di mata abu-kebiruan Harumi. Ia menegakkan duduknya sedikit dan membetulkan letak kacamatanya dengan antusiasme tenang."
            harumi "Kamu setuju bahwa model ini masuk akal, Amamiya-san? Aku sempat mengira orang di luar bidang sains akan menganggap pencatatan seperti ini terlalu dingin dan kaku."
            chiasa "Nggak kok, justru rapi dan gampang dicek. Kalau Senpai mau mengujinya sekarang, anggap saja bantuanku merapikan tata letak poster risetmu kita tukar dengan waktu Senpai memeriksa catatan referensi esai seniku minggu depan. Jadi kita berdua impas."
            nar "Harumi langsung menoleh kembali ke bukunya dengan ekspresi serius yang tampak lega, mengambil penggaris logam kecil, lalu menarik satu garis vertikal baru yang sangat lurus di sisi kanan halaman."
            harumi "Menarik. Variabelnya bisa diukur jelas dalam satuan jam dan keluaran kerja. Jika aku menambahkan kolom keempat untuk verifikasi keseimbangan, tingkat salah harap bisa ditekan mendekati nol."
            nar "Ia melirik arloji tipis di pergelangan tangannya lalu mencatat menit mulai percakapan kalian hari ini sebagai sampel kontrol di tepi atas kertas."
            nar "Ia menuliskan angka estimasi dua jam desain poster sejajar dengan dua jam penyuntingan esai di baris baru, lalu membacakannya pelan untuk memastikan kamu menyetujui rasionya."
            harumi "Rasio satu banding satu dengan cakupan tugas tertulis seperti ini terasa cukup seimbang untukmu, Amamiya-san? Jika kamu setuju, tolong bubuhkan inisial kecil di tepi kolom keempat sebagai rekan uji terkontrol."
            chiasa "Boleh, sini penanya. Cukup seimbang kok, Kujo-senpai. Dengan begitu Senpai juga nggak perlu terus menebak-nebak isi kepala orang lain kan?"
            nar "Begitu kamu menuliskan inisialmu di tepi halaman, Harumi membubuhkan tanda centang kecil yang sangat rapi di sampingnya, lalu memutar buku catatan itu kembali menghadap dirinya sendiri."
            harumi "Benar. Dengan persetujuan tertulis di kedua pihak, tingkat ketidakpastiannya turun drastis. Berarti di laboratorium nanti, aku juga hanya perlu merapikan rasio pertukaran bersama Ogawa agar seluruh angkanya tetap setimbang."
            chiasa "Kujo-senpai mau menerapkan format empat kolom ini ke catatan laboratorium juga?"
            harumi "Tentu. Kalau Ogawa melihat bahwa aku mampu mengukur kontribusi dan balasan secara transparan, koordinasi riset kami pasti berjalan jauh lebih teratur."
            chiasa "Bagus deh kalau Senpai jadi merasa jauh lebih tenang sekarang."
            harumi "Ya. Selama aku menjaga catatan empat kolom ini tetap seimbang, aku tidak perlu takut menerima perhatian yang tidak sanggup kubayar kembali."
            nar "Ia merapikan tutup penanya dengan raut puas yang tipis. Semakin rapi model yang ia susun di kertas itu, semakin sulit pula baginya kelak menerima perhatian tulus yang tidak menuntut sesuatu untuk dibayar kembali."
        else:
            nar "Kamu menatap kolom-kolom hitam di buku catatan Harumi sejenak, lalu menyandarkan siku di meja dengan nada tenang yang langsung menerima aturan barunya."
            chiasa "Kalau Kujo-senpai memang merasa lebih tenang memakai aturan pertukaran yang jelas, biar kita hitung secara adil sekalian hari ini."
            harumi "Maksudmu mengenai catatan interaksi kita berdua, Amamiya-san?"
            chiasa "Iya. Belakangan aku cukup sering meluangkan waktu mendengarkan masalah labmu, menemanimu saat Ogawa menekan soal beasiswa, dan membantumu mencari referensi di sini. Supaya perhitungannya setara, minggu ini aku butuh Senpai mengosongkan dua malam untuk membantu merapikan seluruh berkas dan menemani jadwal yang kuatur."
            nar "Pena di antara jemari Harumi berhenti tepat di atas kertas. Ia menunduk menghitung cepat dengan suara lirih seperti sedang membaca neraca reaksi."
            harumi "Empat puluh menit mendengarkan masalah laboratorium bulan lalu, ditambah satu jam pencarian referensi dan dua gelas teh hari ini... secara proporsional, menukar dengan dua malam penuh memang masih masuk dalam batas wajar."
            nar "Ia membuka lembaran kalender jadwal labnya sendiri di bagian belakang buku, menatap baris-baris padat di sana, lalu mencoret pelan jadwal bacaan tesis pribadi dan waktu istirahat hari Rabunya tanpa sedikit pun nada protes."
            harumi "Dua malam penuh berarti aku harus menggeser jam membaca jurnal tambahanku sampai lewat tengah malam, tapi aku bisa membawa laptopku supaya perapian berkasmu selesai lebih cepat."
            chiasa "Nggak keberatan memindahkan jam istirahat hari Rabumu?"
            harumi "Kelelahan fisik masih bisa diukur dengan tambahan kopi. Kehilangan satu-satunya tempat bicara yang dapat dipercaya jauh lebih sulit dihitung risikonya."
            chiasa "Oh iya, kalau hari Sabtu nanti ada berkas pameran fakultas yang perlu dirapikan mendadak, Senpai juga bisa kuhubungi kan?"
            nar "Tanpa mengangkat mata dari bukunya, Harumi langsung menulis kata siaga di kotak hari Sabtu dengan tinta hitam yang kaku."
            harumi "Baik. Hari Rabu, Jumat setelah praktikum, dan hari Sabtu aku akan menyelesaikan semua yang kamu tentukan."
            nar "Kalimat persetujuannya meluncur datar seperti tanda tangan di atas surat kewajiban, jauh dari kelegaan seseorang yang sedang memilih dengan bebas. Ia menuliskan syaratmu rapi di baris kosong, lalu menatapmu melewati bingkai kacamatanya dengan getar kecil yang nyaris tak terdengar."
            harumi "Kalau aku sudah memenuhi seluruh bagian ini... berarti catatan kita sekarang sudah setara? Aku masih boleh datang ke mejamu ketika aku butuh bicara, Amamiya-san?"
            chiasa "Tentu saja, Kujo-senpai. Selama kita sama-sama menepati bagian masing-masing, pintuku selalu terbuka."
            harumi "...Baik. Aku mengerti ketentuannya. Terima kasih sudah menjelaskan angkanya secara terang-terangan."
            chiasa "{i}Ia menyetujui seluruh syaratku tanpa menawar satu jam pun, semata demi memastikan dirinya tetap punya izin untuk duduk di meja ini.{/i}"
            nar "Kamu mendengar jelas rasa takut ditinggalkan yang bersembunyi di balik suara terukurnya, dan kamu tetap menutup obrolan dengan mengambil keuntungan penuh dari aturan yang baru saja ia percayai."
    else:
        if kk_slot >= 3:
            nar "Lampu baca meja sudut di lantai dua Perpustakaan Pusat memancarkan cahaya putih lembut di antara rak-rak jurnal yang sunyi. Di luar kaca besar, angin bulan Oktober menggerakkan bayangan daun di halaman kampus."
        else:
            nar "Cahaya bulan Oktober mengalir tenang melalui jendela kaca tinggi Perpustakaan Pusat. Di meja sudut lantai dua yang hanya diisi bunyi lembaran kertas dibalik dan dengung pelan pendingin ruangan, kamu meletakkan dua gelas kertas teh panggang hangat."
        nar "Harumi duduk tegak mengenakan kardigan abu-abu tipis dengan rambut abu-abu perak panjang berkepang samping dan sanggul kecil berhiasan jepit mawar merah. Di depan sikunya terbuka buku catatan saku presisi yang biasa ia pakai mencatat data kimia, sementara di sisi kirinya tersusun map kolaborasi data statistik lintas fakultas kalian."
        nar "Ia mengangkat gelas kertas teh panggang yang baru kamu letakkan, merasakan hangat dinding gelasnya sejenak di telapak tangan sebelum mengangguk pelan."
        harumi "Terima kasih untuk teh panggangnya, Kisaragi-kun. Suhunya sekitar tujuh puluh lima derajat, masih cukup layak untuk mesin minuman lantai bawah. Ini salinan koreksi tabel regresi untuk bahan seminar lintas fakultas yang kemarin kamu titipkan."
        yutaka "Cepat sekali beresnya, Kujo-san. Bagian galat baku di lampiran kedua juga sudah kamu tandai?"
        harumi "Sudah. Aku menempelkan tiga catatan kecil di sudutnya agar kamu tidak perlu mengulang hitungan desimal dua kali. Pembulatan terlalu awal di tabel pertama tadi sedikit menggeser angka ujungnya."
        yutaka "Selalu teliti sampai angka belakang koma ya."
        harumi "Kejelasan data menghemat empat puluh persen pertanyaan ulang saat sesi diskusi. Secara efisiensi, itu cukup menguntungkan."
        nar "Saat Harumi menggeser map kertas itu ke hadapanmu, kamu melihat bekas noda tinta hitam tipis di sisi jari telunjuk kanannya, tanda bahwa ia sudah menggaris halaman cukup lama sejak tadi. Tepat di samping sikunya, buku catatan sakunya masih terbuka lebar."
        nar "Halaman itu sama sekali kosong dari rumus katalis; di atasnya justru tergambar tiga garis kolom rapi bertinta hitam halus."
        yutaka "Tunggu dulu, Kujo-san... itu bukan catatan eksperimen laboratorium kan? Kok judul kolomnya ada bantuan yang diberikan, balasan yang diterima, sama syarat akses?"
        nar "Harumi membetulkan letak kacamata bingkai tipisnya dengan satu jari. Ia tidak buru-buru menutup buku itu ataupun terlihat malu, justru memutarnya pelan menghadap ke arahmu agar kamu bisa membaca seluruh isinya dengan jelas."
        nar "Di dalam tiga kolom tersebut tertulis catatan yang membuat dadamu terasa dingin karena terlalu mirip dengan buku hitung relasi di rumah keluargamu sendiri. Baris pertama menuliskan menyusun ulang lampiran data untuk Ogawa berpasangan dengan akses ruang spektrometer setelah jam kuliah. Baris di bawahnya menuliskan menemani diskusi tambahan senior lab berpasangan dengan nama tetap masuk daftar publikasi."
        nar "Di baris ketiga tertulis lagi meminjamkan catatan kuliah penuh berpasangan dengan tetap diajak masuk obrolan kelompok belajar."
        yutaka "Sampai urusan menemani diskusi tambahan sama meminjamkan catatan kuliah juga kamu masukkan ke tabel pertukaran?"
        nar "Harumi membalik mundur satu halaman sebelumnya, memperlihatkan catatan kecil yang jauh lebih sederhana sebelum seluruhnya berubah menjadi kolom berpagar garis kaku."
        harumi "Bulan lalu aku masih mencatat bantuan kecil di asrama dan perpustakaan sebagai titik referensi awal. Setelah berdiskusi panjang dengan Ogawa minggu lalu, aku memindahkan semuanya ke dalam tiga kolom ini."
        yutaka "Kenapa setiap barisnya harus diberi angka balasan begini, Kujo-san?"
        harumi "Awalnya aku mulai mencatat ini untuk memahami pola interaksi manusia yang selama ini sering terlewat olehku, Kisaragi-kun. Seperti mencatat perubahan suhu di ruang reaksi agar tidak ada variabel yang meledak di luar perhitungan."
        yutaka "Tapi lama-kelamaan catatanmu berubah jadi daftar harga yang harus dibayar dulu sebelum boleh dekat sama orang."
        harumi "Ogawa menjelaskan kepadaku bahwa semua kedekatan pada dasarnya memiliki pertukaran. Menurutnya, tidak ada perhatian yang benar-benar gratis, dan menganggap orang lain peduli tanpa syarat hanya membuat kita salah menghitung lalu berakhir kecewa."
        harumi "Ia bilang rasa bingungku saat membaca perasaan orang lain terjadi karena aku terus mengira interaksi sosial berjalan tanpa kontrak tertulis."
        if kk_has("harumi_dimanfaatkan"):
            harumi "Belakangan aku juga melihat sendiri bahwa setiap kali seseorang menawarkan bantuan atau waktu kepadaku, selalu ada jadwal atau syarat tertentu yang ikut menyertainya."
        nar "Mata abu-kebiruan Harumi turun menatap deretan garis hitam yang baru ia tambah dengan penggaris logam kecil. Kalung lambang atom di lehernya berkilau tipis saat ia mengembuskan napas pelan."
        harumi "Aku mencoba memperlakukannya sebagai eksperimen sosial. Aku mencari hal konkret yang bisa kuberikan lebih dulu supaya aku punya hak meminta perhatian tanpa salah berharap."
        yutaka "Terus... setelah kamu mencatat semuanya serapi ini dan membayar tiap barisnya, kamu merasa lebih tenang?"
        harumi "Justru di situ anomali datanya, Kisaragi-kun. Semakin jelas daftar pertukarannya dan semakin tepat aku membayarnya, semakin sedikit aku tahu apakah orang-orang itu benar-benar ingin mengenalku."
        yutaka "{i}Ia membungkus rasa takut ditolak memakai tabel dan aturan yang ditanamkan Ogawa, seolah kalau semua hal diberi harga sejak awal, ia tidak akan pernah dikecewakan lagi.{/i}"
        call kk_family_menu("H12", ["\"Hentikan eksperimen itu, Kujo-san. Kedekatan nggak berjalan pakai daftar harga.\"", "\"Kalau menurutmu cara ini masuk akal, ayo kita uji variabel pertukarannya bareng.\"", "\"Kalau semua memang perlu imbal balik, kebetulan ada hal yang bisa kamu bantu untukku sekarang.\""])
        if _return == "A":
            nar "Kamu meletakkan dua jarimu pelan di pinggir halaman buku catatan itu agar pena Harumi berhenti bergerak, lalu menatapnya lurus dengan sorot mata abu-abu gelap yang serius."
            yutaka "Hentikan eksperimen itu sebelum kamu benar-benar memercayainya, Kujo-san. Aku tumbuh di keluarga yang menghitung hampir seluruh relasi manusia memakai timbal balik dan daftar utang. Justru karena aku tahu bentuk aslinya, aku berani bilang Ogawa sedang memasang jebakan."
            nar "Harumi berkedip pelan di balik kacamatanya, keningnya berkerut menimbang sanggahanmu dengan keseriusan penuh."
            harumi "Kamu mengatakan kedekatan tidak bertumpu pada pertukaran? ...Pernyataan itu bertentangan langsung dengan seluruh argumen yang Ogawa ajarkan kepadaku beberapa minggu ini. Secara praktis, bukankah setiap orang memberi waktu dan tenaga karena mengharapkan timbal balik?"
            yutaka "Waktu dulu kamu mengajari kelompok belajar SMA kita, atau waktu aku datang membawakan teh panggang dan duduk di meja sudut ini, memangnya kita pernah menaruh nota tagihan di antara kita?"
            harumi "Itu... aku memang tidak mencatat biayanya waktu itu, tapi di dalam kepalaku aku tetap berpikir suatu saat harus membalas dengan nilai setara. Kalau tidak ada nilai tukar yang terukur, dari mana aku tahu kapan kehadiranku mulai mengganggu orang lain?"
            yutaka "Dari jawaban jujur orang itu sendiri, Kujo-san. Di hubungan yang sehat, orang boleh bilang sedang capek atau menolak tanpa langsung dianggap memutus segalanya."
            yutaka "Sekarang coba lihat sendiri tiga kolom di buku catatanmu itu. Kalau suatu hari kamu bilang nggak mau, atau bilang hari ini nggak sanggup menemani diskusi tambahan, di kolom mana kamu tetap berhak dihormati?"
            nar "Seluruh gerak tangan Harumi berhenti seketika. Mata abu-kebiruannya menyapu pelan dari judul kolom paling kiri ke kolom kanan, lalu turun menyusuri seluruh baris kosong di bawahnya."
            harumi "...Di sini tidak ada kolom untuk penolakan."
            yutaka "Tepat. Di aturan buatan Ogawa, satu-satunya cara supaya kamu tetap dianggap berharga adalah dengan terus menyetujui syaratnya."
            nar "Pandangan Harumi tertahan sejenak pada baris pertama yang menyebut nama Ogawa. Alisnya sedikit mengernyit ketika sebuah ingatan konkret rupanya baru saja tersambung di kepalanya."
            harumi "Minggu lalu ketika aku mengatakan lelah dan ingin pulang lebih awal ke asrama, Ogawa tidak memarahiku. Ia hanya mengingatkan pelan soal jadwal penggunaan alat dan surat rekomendasi."
            yutaka "Itu persis buktinya. Ia nggak pernah memberimu ruang aman buat menolak. Bandingkan sama Prof. Mizuhara atau Ogiwara-san di asrama, memangnya mereka pernah menagih balasan setiap kali mereka membantumu?"
            harumi "...Tidak pernah. Ogiwara-san bahkan sering menyimpan teh tambahan di dapur asrama tanpa mencatat siapa yang meminumnya."
            yutaka "Karena perhatian yang tulus memang nggak punya buku tagihan, Kujo-san."
            nar "Harumi menatap lembaran tintanya selama beberapa detik yang hening. Pelan sekali, ia membuka tutup penanya lalu menarik satu garis miring panjang yang tegas menembus seluruh kolom daftar harga itu."
            harumi "Aku menghapus pilihan untuk menolak bahkan sebelum eksperimennya dimulai. Pantas seluruh hasil pengamatanku selalu mengarah ke kesimpulan yang sama."
            yutaka "Sekarang tutup dulu buku catatannya. Minum teh panggangnya mumpung masih hangat."
            harumi "...Berarti sekarang aku boleh duduk di sini meminum teh bersamamu tanpa perlu menambahkan koreksi lampiran tambahan sebagai imbalan?"
            yutaka "Nggak ada tagihan apa-apa di meja ini, Kujo-san. Minum saja dengan tenang."
            nar "Harumi menatap gelas teh panggangnya sejenak, lalu sudut bibirnya terangkat sangat tipis membentuk senyum canggung yang jarang tampak di wajahnya."
            harumi "Data yang aneh... tapi untuk pertama kalinya dalam dua minggu, kepalaku terasa jauh lebih ringan tanpa harus menghitung apa pun."
            harumi "Terima kasih sudah menghentikan perhitunganku sebelum berubah menjadi kebiasaan, Kisaragi-kun. Aku perlu memikirkan ulang semua yang Ogawa katakan kepadaku."
            nar "Untuk pertama kalinya hari itu, bahu Harumi turun pelan saat ia membalik buku catatannya ke halaman kosong dan mengangkat gelas teh hangat di hadapannya."
        elif _return == "B":
            nar "Kamu memandangi tabel rapi di buku catatan itu beberapa detik lalu mengangguk tenang, ikut masuk ke dalam kerangka eksperimen yang baru saja ia bangun."
            yutaka "Sebenarnya aku paham kenapa kamu membuat tabel seperti ini, Kujo-san. Di Ekonomi sendiri, kalau pertukarannya jelas dan terukur dari awal, memang lebih kecil kemungkinan ada pihak yang merasa dirugikan atau salah paham."
            nar "Kilat lega yang jarang terlihat langsung melintas di mata abu-kebiruan Harumi. Ia menegakkan duduknya sedikit dan membetulkan letak kacamatanya dengan antusiasme tenang."
            harumi "Kamu setuju bahwa model ini masuk akal, Kisaragi-kun? Aku sempat mengira orang lain akan menganggap pencatatan seperti ini terlalu dingin dan kaku."
            yutaka "Justru rapi dan gampang diverifikasi. Kalau mau diuji sekarang, anggap saja waktumu memeriksa tabel regresi tadi kita tukar dengan dua jam waktuku membantu menyunting bagian tinjauan pustaka bahasa Inggrismu minggu depan. Jadi kita berdua impas."
            nar "Harumi langsung menoleh kembali ke bukunya dengan ekspresi serius yang tampak lega, mengambil penggaris logam kecil, lalu menarik satu garis vertikal baru yang sangat lurus di sisi kanan halaman."
            harumi "Menarik. Variabelnya bisa diukur jelas dalam satuan jam dan keluaran kerja. Jika aku menambahkan kolom keempat untuk verifikasi keseimbangan, tingkat salah harap bisa ditekan mendekati nol."
            nar "Ia melirik arloji tipis di pergelangan tangannya lalu mencatat menit mulai percakapan kalian hari ini sebagai sampel kontrol di tepi atas kertas."
            nar "Ia menuliskan angka estimasi dua jam pengecekan statistik sejajar dengan dua jam penyuntingan naskah di baris baru, lalu membacakannya pelan untuk memastikan kamu menyetujui rasionya."
            harumi "Rasio satu banding satu dengan cakupan tugas tertulis seperti ini terasa cukup seimbang untukmu, Kisaragi-kun? Jika kamu setuju, tolong bubuhkan inisial kecil di tepi kolom keempat sebagai rekan uji terkontrol."
            yutaka "Boleh, sini penanya. Cukup seimbang kok, Kujo-san. Dengan begitu kamu juga nggak perlu terus menebak-nebak isi kepala orang lain kan?"
            nar "Begitu kamu menuliskan inisialmu di tepi halaman, Harumi membubuhkan tanda centang kecil yang sangat rapi di sampingnya, lalu memutar buku catatan itu kembali menghadap dirinya sendiri."
            harumi "Benar. Dengan persetujuan tertulis di kedua pihak, tingkat ketidakpastiannya turun drastis. Berarti di laboratorium nanti, aku juga hanya perlu merapikan rasio pertukaran bersama Ogawa agar seluruh angkanya tetap setimbang."
            yutaka "Kamu mau menerapkan format empat kolom ini ke catatan laboratorium juga?"
            harumi "Tentu. Kalau Ogawa melihat bahwa aku mampu mengukur kontribusi dan balasan secara transparan, koordinasi riset kami pasti berjalan jauh lebih teratur."
            yutaka "Bagus lah kalau kamu jadi merasa jauh lebih tenang sekarang."
            harumi "Ya. Selama aku menjaga catatan empat kolom ini tetap seimbang, aku tidak perlu takut menerima perhatian yang tidak sanggup kubayar kembali."
            nar "Ia merapikan tutup penanya dengan raut puas yang tipis. Semakin rapi model yang ia susun di kertas itu, semakin sulit pula baginya kelak menerima perhatian tulus yang tidak menuntut sesuatu untuk dibayar kembali."
        else:
            nar "Kamu menatap kolom-kolom hitam di buku catatan Harumi sejenak, lalu menyandarkan lengan yang melingkari jam tangan tali kulit di atas meja dengan nada tenang yang langsung menerima aturan barunya."
            yutaka "Kalau kamu memang merasa lebih tenang memakai aturan pertukaran yang jelas, biar kita hitung secara adil sekalian hari ini, Kujo-san."
            harumi "Maksudmu mengenai catatan interaksi kita berdua, Kisaragi-kun?"
            yutaka "Iya. Belakangan aku cukup sering meluangkan waktu mendengarkan masalah labmu, membantumu membedah syarat beasiswa waktu Ogawa menekan, dan menemanimu mencari referensi di sini. Supaya perhitungannya setara, minggu ini aku butuh kamu mengosongkan dua malam untuk membantu merapikan seluruh data seminar dan menemani jadwal yang kuatur."
            nar "Pena di antara jemari Harumi berhenti tepat di atas kertas. Ia menunduk menghitung cepat dengan suara lirih seperti sedang membaca neraca reaksi."
            harumi "Empat puluh menit mendengarkan masalah laboratorium bulan lalu, ditambah satu jam pencarian referensi dan dua gelas teh hari ini... secara proporsional, menukar dengan dua malam penuh memang masih masuk dalam batas wajar."
            nar "Ia membuka lembaran kalender jadwal labnya sendiri di bagian belakang buku, menatap baris-baris padat di sana, lalu mencoret pelan jadwal bacaan tesis pribadi dan waktu istirahat hari Rabunya tanpa sedikit pun nada protes."
            harumi "Dua malam penuh berarti aku harus menggeser jam membaca jurnal tambahanku sampai lewat tengah malam, tapi aku bisa membawa laptopku supaya pengolahan datamu selesai lebih cepat."
            yutaka "Nggak keberatan memindahkan jam istirahat hari Rabumu?"
            harumi "Kelelahan fisik masih bisa diukur dengan tambahan kopi. Kehilangan satu-satunya tempat bicara yang dapat dipercaya jauh lebih sulit dihitung risikonya."
            yutaka "Oh iya, kalau hari Sabtu nanti ada berkas panitia yang perlu dirapikan mendadak, kamu juga bisa kuhubungi kan?"
            nar "Tanpa mengangkat mata dari bukunya, Harumi langsung menulis kata siaga di kotak hari Sabtu dengan tinta hitam yang kaku."
            harumi "Baik. Hari Rabu, Jumat setelah praktikum, dan hari Sabtu aku akan menyelesaikan semua yang kamu tentukan."
            nar "Kalimat persetujuannya meluncur datar seperti tanda tangan di atas surat kewajiban, jauh dari kelegaan seseorang yang sedang memilih dengan bebas. Ia menuliskan syaratmu rapi di baris kosong, lalu menatapmu melewati bingkai kacamatanya dengan getar kecil yang nyaris tak terdengar."
            harumi "Kalau aku sudah memenuhi seluruh bagian ini... berarti catatan kita sekarang sudah setara? Aku masih boleh datang ke mejamu ketika aku butuh bicara, Kisaragi-kun?"
            yutaka "Tentu saja, Kujo-san. Selama kita sama-sama menepati bagian masing-masing, pintuku selalu terbuka."
            harumi "...Baik. Aku mengerti ketentuannya. Terima kasih sudah menjelaskan angkanya secara terang-terangan."
            yutaka "{i}Ia menyetujui seluruh syaratku tanpa menawar satu jam pun, semata demi memastikan dirinya tetap punya izin untuk duduk di meja ini.{/i}"
            nar "Kamu mendengar jelas rasa takut ditinggalkan yang bersembunyi di balik suara terukurnya, dan kamu tetap menutup obrolan dengan mengambil keuntungan penuh dari aturan yang baru saja ia percayai."
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
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Lampu baca meja sudut lantai dua Perpustakaan Pusat menyala putih dingin di antara rak jurnal sains yang sepi. Angin bulan November mengetuk kaca jendela tinggi di luar sementara suara kipas pendingin terdengar samar."
        else:
            nar "Cahaya bulan November jatuh pucat melalui jendela kaca tinggi Perpustakaan Pusat. Di meja sudut lantai dua yang jauh dari keramaian stan Festival Seni di luar gedung, deretan buku referensi kimia tersusun setengah terbuka mengelilingi satu lembar pemberitahuan resmi."
        nar "Harumi duduk kaku mengenakan kardigan abu-abu tipis dengan rambut abu-abu perak panjang berkepang samping dan sanggul kecil berhiasan jepit mawar merah. Di depan sikunya terbentang hampir seluruh rencana kerja penelitian, daftar pemesanan reagen, serta jadwal pemakaian alat spektrometer."
        nar "Tepat ketika kamu menghampiri meja sambil membawa dua botol teh hangat dan salinan draf tata letak grafik riset yang sempat kalian bahas, seorang asisten senior dari jurusan Sains berhenti singkat di tepi meja sambil memeluk map plastik."
        "Asisten Lab" "Kujo-san, barusan staf administrasi lab bilang kalau alokasi dana pengganti reagenmu belum masuk sebelum akhir bulan, slot alat spektrometer untuk bulan Desember bakal langsung dialihkan ke kelompok uji lain ya."
        harumi "Aku mengerti. Terima kasih sudah mengabari lebih awal."
        "Asisten Lab" "Kalau kamu mau minta tanda tangan pinjam cadangan bahan dari proyek bimbingan Ogawa-san, katanya dia masih ada di ruang dokumen lantai tiga sampai jam tutup."
        harumi "Akan kupertimbangkan dulu. Terima kasih."
        nar "Asisten itu mengangguk singkat lalu melangkah menjauh melewati rak jurnal. Begitu suaranya hilang, mata abu-kebiruan Harumi turun kembali menatap lembar surat pembekuan dana di tengah meja. Jemarinya merapikan sudut kertas yang sudah terlipat tajam."
        chiasa "Kujo-senpai... surat yang barusan dibilang itu pemberitahuan pembekuan dana sub-proyek riset Senpai?"
        harumi "Ya, Amamiya-san. Mulai minggu ini seluruh pencairan dana hibah untuk sub-proyek katalisku dibekukan sementara sampai audit anggaran fakultas selesai semester depan."
        chiasa "Lho, bukannya data uji Senpai tinggal dua tahap lagi buat dikirim ke seminar musim dingin?"
        harumi "Benar. Kalau aku tidak membeli reagen pembanding sebelum akhir bulan November, seluruh sampel yang sudah kukerjakan sejak bulan Juni rusak dan harus diulang dari titik nol."
        chiasa "Prof. Mizuhara nggak bisa dimintai tanda tangan darurat buat cairin cadangan jurusan, Senpai?"
        harumi "Prof. Mizuhara sedang menghadiri simposium di Osaka sampai akhir minggu depan. Justru karena beliau sedang di luar kota, surat pembekuan ini datang di waktu paling buruk."
        nar "Ia mengembuskan napas pendek lalu membetulkan letak kacamata bingkai tipisnya dengan gerakan yang lebih kaku dari biasanya. Kalung lambang atom di lehernya berkilau redup ketika ia meraih ponselnya dan menggesernya ke tengah meja."
        nar "Di layar ponsel yang menyala itu terpampang rentetan pesan dari Ogawa Masato yang dikirim setengah jam sebelumnya."
        "Pesan Ogawa" "Kujo-san, aku sudah dengar soal pembekuan anggaranmu. Sayang sekali kalau risetmu berhenti di tengah jalan. Aku bisa talangi biaya reagennya lewat jalur dana pribadiku dulu."
        "Pesan Ogawa" "Nanti kita bahas rinciannya berdua di luar jam kampus saja biar lebih leluasa. Soal kompensasi dan urusan evaluasi proyek ke depan tidak perlu ditulis di berkas resmi fakultas."
        chiasa "Senpai... kalimat terakhirnya itu aneh banget. Kenapa dia minta bahas di luar jam kampus terus syaratnya nggak boleh ditulis di berkas resmi?"
        harumi "Aku tahu bagian mana yang tidak wajar, Amamiya-san. Aku sudah membaca pesan itu enam kali berturut-turut."
        if kk_has("harumi_eksperimen_dihentikan"):
            harumi "Sejak pembicaraan kita bulan lalu, aku sadar betul bahwa di setiap tawaran Ogawa tidak pernah ada pilihan untuk menolak. Aku tahu seharusnya aku langsung membalas tidak."
        else:
            harumi "Di setiap dokumen hibah resmi selalu ada aturan transparan dan batas kewajiban tertulis. Tawaran pribadi Ogawa sengaja menghilangkan semua batas itu supaya syaratnya hanya ditentukan oleh dirinya sendiri."
        nar "Harumi memandangi tabel anggaran dan kalender tenggat di samping ponselnya. Kedua bahunya tampak kaku menahan ketegangan yang berusaha keras ia hitung seperti persamaan kimia."
        harumi "Aku ingin menolak. Lalu lima detik kemudian aku memikirkan semua sampel yang akan rusak, rekomendasi pascasarjana yang tertunda, dan dua tahun kerja di laboratorium yang berhenti begitu saja jika dana itu tidak datang."
        harumi "Aku sedang mencoba mencari tahu apakah rasa takut sedang memanipulasi cara berpikirku sampai aku mengira tawaran Ogawa adalah satu-satunya jalan keluar yang tersedia."
        chiasa "{i}Ia sudah melihat jebakannya dengan mata terbuka lebar, tapi kepanikan soal risetnya hampir mendorongnya masuk sendiri.{/i}"
        $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["\"Kita cari jalur dana resmi sama hibah mahasiswa bareng, Senpai. Jangan sentuh uang pribadi Ogawa.\"", "\"Kita laporkan pesan sama syarat nggak resmi Ogawa ini ke Prof. Mizuhara dan pihak kampus, Senpai.\"", "Diam saja dan biarkan ia menimbang sendiri.", "Manfaatkan kepanikannya untuk mengikatnya ke syaratmu sendiri."])]
        call screen kk_choice_panel(_rows, "Pilihan Harumi")
        $ kk_record_choice("H13", _return)
        if _return == "A":
            nar "Kamu membalikkan ponsel Harumi perlahan ke permukaan meja supaya pesan Ogawa tidak terus menyita pandangannya, lalu menarik selembar kertas kosong ke tengah meja."
            chiasa "Jangan terima sepeser pun uang pribadi Ogawa, Kujo-senpai. Kalau dana lab lagi beku, ayo kita cari jalur pendanaan resmi sama hibah penelitian mahasiswa bareng sekarang."
            harumi "Hibah mahasiswa tingkat sarjana dan dana darurat jurusan... tenggat pencairannya jauh lebih lambat dari jadwal spektrometer akhir bulan ini, Amamiya-san. Penelitianku hampir pasti mundur minimal satu atau dua bulan."
            chiasa "Mundur satu atau dua bulan itu artinya riset Senpai tetap hidup dan utuh punya Senpai sendiri. Kalau menerima syarat gelap Ogawa, yang hilang bisa jauh lebih besar daripada satu slot alat."
            nar "Harumi menatap kertas kosong di hadapannya selama beberapa detik, lalu pandangannya perlahan kembali jernih. Ia meraih penanya dan menarik buku panduan beasiswa penelitian dari tasnya."
            harumi "Kamu benar. Terlambat masih bisa dihitung dan disesuaikan ulang skalanya. Terikat pada syarat yang tidak pernah tertulis justru memiliki risiko tak terukur."
            chiasa "Nah, coba kita tulis bareng dari yang paling mungkin dulu. Ada dana penelitian kecil fakultas, hibah asosiasi alumni sains, sama kemungkinan mengirim surel langsung ke Prof. Mizuhara di Osaka supaya slot spektrometer bisa ditunda sementara."
            harumi "Jika aku memperkecil volume sampel uji menjadi setengahnya, biaya reagen tahap pertama juga turun empat puluh persen. Aku bisa mengirim draf penyesuaian ke Prof. Mizuhara lewat surel begitu selesai dari sini."
            chiasa "Bagus banget, Senpai! Bagian grafik proposal sama lampiran presentasinya biar kubantu rapikan minggu ini supaya pengajuannya bisa cepat masuk."
            harumi "...Jalur pendanaan resmi memang lebih lambat dan merepotkan, Amamiya-san. Tapi setidaknya aku tidak perlu berutang ruang hidupku pada siapa pun."
            chiasa "Sini, minum teh hangatnya dulu sambil kita susun daftar kontaknya satu per satu. Nggak perlu buru-buru membalas pesan Ogawa."
            harumi "Baik. Aku bahkan bisa membalasnya singkat saja bahwa aku akan menempuh jalur hibah jurusan."
            nar "Harumi membalik lembar surat pembekuan dana itu ke bawah tumpukan lalu mulai menulis daftar pintu resmi yang bisa diketuk dengan tangan yang jauh lebih tenang."
        elif _return == "B":
            nar "Kamu menunjuk dua baris pesan terakhir di layar ponsel Harumi dengan nada tegas, membuat Harumi mengangkat wajah menatap mata kuning keemasanmu lurus."
            chiasa "Kujo-senpai, ini sudah jauh melewati urusan dana lab. Ogawa sengaja memanfaatkan pembekuan anggaran buat memancing pertemuan tertutup pakai syarat nggak resmi. Ayo kita laporkan dia ke Prof. Mizuhara dan komite etik kampus."
            nar "Jari Harumi yang menyentuh pinggir ponsel sempat menegang pelan. Sorot matanya meredup bimbang sejenak."
            harumi "Melaporkan Ogawa secara resmi... ia kandidat doktor senior yang memegang banyak jaringan pengelola alat di gedung Sains, Amamiya-san. Kalau laporanku dianggap berlebihan atau kurang bukti, posisiku di laboratorium bisa langsung dipersulit."
            chiasa "Justru karena dia mengandalkan jabatannya buat bikin Senpai takut bicara, dia bakal terus mengulang cara ini kalau dibiarkan. Aku nggak bakal menyuruh Senpai jalan sendirian, aku ikut mendampingi sampai ruang Prof. Mizuhara begitu beliau balik dari Osaka."
            chiasa "Dan Senpai sendiri yang menentukan bagian mana aja yang siap disampaikan nanti. Nggak ada yang memaksamu membuka hal yang belum mau kamu bahas."
            harumi "Kamu bahkan bukan mahasiswa Fakultas Sains, Amamiya-san... kamu yakin mau ikut terseret ke urusan internal laboratoriumku?"
            chiasa "Urutan pesan sejelas ini nggak cuma urusan laboratorium, Senpai. Nggak ada orang yang seharusnya menghadapi tekanan kayak begini sendirian."
            nar "Keheningan pendek menyelimuti sudut perpustakaan. Harumi memandangi pesan di layarnya sekali lagi, lalu bahunya tegak kembali perlahan."
            harumi "...Aku takut, Amamiya-san. Jujur saja, menghadapi konflik formal seperti ini adalah hal yang paling tidak bisa kuhitung hasilnya. Tapi kalau kamu bersamaku di sana, aku bersedia bersaksi tentang semua yang kulihat dan kuterima."
            chiasa "Bagus, Senpai. Sebelum Ogawa sempat menarik atau menghapus pesannya, ambil tangkapan layarnya dulu sekarang, sekalian kumpulkan jadwal lab dan riwayat surel lama yang pernah dia kirim."
            nar "Harumi mengangguk mantap. Ia segera menyimpan tangkapan layar percakapan itu ke folder cadangan, lalu mengambil dua lembar catatan jadwal laboratorium yang pernah dicoret Ogawa sebelumnya dari dalam map."
            harumi "Aku juga masih menyimpan salinan surat pembekuan dana dan catatan jam perubahan alat dari bulan lalu. Semuanya fakta yang dapat diperiksa."
            chiasa "Kita kirim permintaan jadwal menghadap ke sekretariat Prof. Mizuhara sama komite etik hari ini juga, biar semuanya tercatat resmi tanpa lewat perantara siapa pun."
            harumi "Baik. Untuk pertama kalinya aku tidak merasa harus menukar rasa tidak nyamanku dengan pengorbanan baru hanya demi membuktikan bahwa sesuatu memang keliru."
            nar "Ia merapikan seluruh bukti itu ke dalam satu map plastik bening. Rasa takutnya belum lenyap sepenuhnya, tetapi kini ia berhenti berdiri sendirian di hadapan tekanan Ogawa."
        elif _return == "C":
            nar "Kamu menatap layar ponsel Harumi dan deretan angka anggaran di meja tanpa sepatah kata pun. Kamu menyandarkan bahumu ke kursi dan membiarkan keheningan penuh menggantung di antara kalian."
            harumi "Amamiya-san... menurutmu bagaimana? Kalau aku menolak, semua kerja enam bulan terakhir benar-benar terhenti."
            chiasa "Itu keputusan riset Senpai sendiri. Aku kan anak Seni, kurang paham seberapa penting jadwal alat di lab Sains."
            nar "Sorot harap tipis yang tadi sempat singgah di mata abu-kebiruan Harumi padam seketika. Ia mengangguk kecil seperti baru menerima konfirmasi bahwa seluruh beban itu memang harus ia hitung sendiri dari awal hingga akhir."
            harumi "...Benar juga. Ini variabel penelitianku sendiri. Tidak adil kalau aku mengharapkan orang lain memikul keputusan biayanya."
            nar "Ia kembali menunduk memeriksa lembar pesanan reagen, mencoret angka demi angka sambil terus membandingkan kehilangan risetnya dengan kalimat kabur di layar ponsel Ogawa."
            chiasa "Senpai jadi mau balas pesannya?"
            harumi "Kalau aku hanya menerima pinjaman dana ini sementara sampai tahap pengukuran spektrometer bulan Desember selesai, mungkin dampaknya masih bisa kukendalikan."
            harumi "Aku bisa menjalaninya sementara. Sampai risetnya aman."
            nar "Jari-jarinya mengetik balasan singkat menyetujui pertemuan tertutup Ogawa lalu menekan tombol kirim dengan gerakan kaku. Tidak sampai setengah menit kemudian, layar ponsel itu menyala kembali membawa balasan cepat."
            "Pesan Ogawa" "Keputusan bijak, Kujo-san. Datanglah besok habis jam praktikum ke restoran di dekat stasiun selatan, aku sudah memesan ruang pribadi supaya kita bisa bicara tenang."
            nar "Harumi membaca satu baris pesan itu tanpa ekspresi, lalu langsung membalikkan layar ponselnya ke permukaan meja."
            harumi "Maaf sudah menyita waktumu di tengah persiapan Festival Seni, Amamiya-san. Aku harus segera ke ruang dokumen sebelum jam tutup."
            chiasa "{i}Kata sementara yang barusan ia sebut bahkan tidak punya tanggal berakhir yang jelas...{/i}"
            nar "Ia membereskan seluruh rencana kerjanya dengan terburu-buru lalu melangkah pergi. Keputusan yang lahir dari keheninganmu itu mungkin menyelamatkan reagennya minggu ini, sambil membuka pintu jauh lebih lebar bagi kendali Ogawa atas hidupnya."
        else:
            nar "Kamu memandangi wajah pucat Harumi dan rentetan pesan Ogawa di atas meja selama dua detik yang sunyi. Alih-alih menutup jebakan itu, kamu justru mencondongkan tubuh pelan mendekatinya."
            chiasa "Kujo-senpai nggak usah terima tawaran mencurigakan dari Ogawa. Kebetulan aku punya simpanan dana pribadi dari proyek ilustrasiku yang bisa kucairkan minggu ini buat membantu menutup sebagian bahan awalmu."
            nar "Mata abu-kebiruan Harumi langsung terangkat cepat menatapmu dengan keterkejutan bercampur rasa lega yang rapuh."
            harumi "Kamu serius mau menalangi biaya reagenku, Amamiya-san? Itu jumlahnya tidak kecil... bagaimana aku harus mengembalikannya?"
            chiasa "Aku nggak minta dibayar pakai uang dalam waktu dekat kok, Senpai. Cuma karena aku membantu mengeluarkanmu dari jebakan Ogawa, wajar kan kalau aku minta syarat yang jelas juga di antara kita?"
            harumi "Syarat seperti apa yang kamu maksud?"
            chiasa "Mulai bulan ini sampai semester selesai, kapan pun aku butuh waktu, bantuan riset, atau kehadiran Kujo-senpai buat jadwal yang kuatur di luar lab, Senpai harus mendahulukan aku dulu sebelum orang lain. Termasuk kalau ada urusan sama Ko-nii atau kelompok lain."
            nar "Jemari Harumi berhenti di pinggir surat pembekuan dana. Kacamata tipisnya memantulkan lampu baca saat ia menimbang kalimatmu dalam diam yang dingin dan kaku."
            harumi "...Kalau aku menerima bantuanmu, berarti aku menukar ikatan dengan Ogawa menjadi ketergantungan penuh pada syaratmu, Amamiya-san."
            chiasa "Setidaknya aku bilang terang-terangan di depan meja sekarang, Senpai. Tinggal pilih mau berhenti riset besok, masuk ke pertemuan tertutup Ogawa, atau menerima jalanku."
            harumi "Dan kalau suatu hari jadwalmu bertabrakan dengan jam istirahat atau janjiku di asrama bersama Ogiwara-san?"
            chiasa "Berarti Senpai menggeser jadwal lain itu dulu sesuai kesepakatan kita."
            nar "Keheningan panjang menekan bahu Harumi hingga ia perlahan memejamkan mata satu detik. Ketika ia kembali menatapmu, tidak ada kelegaan sedikit pun di wajahnya."
            harumi "...Baik. Kirimkan daftar jadwal yang kamu inginkan. Aku akan memenuhinya supaya risetku bisa tetap berjalan bulan ini."
            chiasa "Sepakat kalau begitu, Kujo-senpai. Besok kusiapkan bagian awal dananya."
            nar "Harumi menuliskan namamu di pojok buku catatannya dengan garis tinta lurus yang dingin. Risetnya mungkin akan bergerak kembali minggu depan, sementara ruang kebebasannya baru saja berpindah tangan lewat ketakutan yang kamu manfaatkan."
    else:
        if kk_slot >= 3:
            nar "Lampu baca meja sudut lantai dua Perpustakaan Pusat menyala putih dingin di antara rak jurnal sains yang sepi. Angin bulan November mengetuk kaca jendela tinggi di luar sementara suara kipas pendingin terdengar samar."
        else:
            nar "Cahaya bulan November jatuh pucat melalui jendela kaca tinggi Perpustakaan Pusat. Di meja sudut lantai dua yang jauh dari keramaian stan Festival Seni di luar gedung, deretan buku referensi kimia tersusun setengah terbuka mengelilingi satu lembar pemberitahuan resmi."
        nar "Harumi duduk kaku mengenakan kardigan abu-abu tipis dengan rambut abu-abu perak panjang berkepang samping dan sanggul kecil berhiasan jepit mawar merah. Di depan sikunya terbentang hampir seluruh rencana kerja penelitian, daftar pemesanan reagen, serta jadwal pemakaian alat spektrometer."
        nar "Tepat ketika kamu menghampiri meja sambil membawa dua gelas kertas teh panggang hangat dan map koreksi data seminar lintas fakultas, seorang asisten senior dari jurusan Sains berhenti singkat di tepi meja sambil memeluk map plastik."
        "Asisten Lab" "Kujo-san, barusan staf administrasi lab bilang kalau alokasi dana pengganti reagenmu belum masuk sebelum akhir bulan, slot alat spektrometer untuk bulan Desember bakal langsung dialihkan ke kelompok uji lain ya."
        harumi "Aku mengerti. Terima kasih sudah mengabari lebih awal."
        "Asisten Lab" "Kalau kamu mau minta tanda tangan pinjam cadangan bahan dari proyek bimbingan Ogawa-san, katanya dia masih ada di ruang dokumen lantai tiga sampai jam tutup."
        harumi "Akan kupertimbangkan dulu. Terima kasih."
        nar "Asisten itu mengangguk singkat lalu melangkah menjauh melewati rak jurnal. Begitu suaranya hilang, mata abu-kebiruan Harumi turun kembali menatap lembar surat pembekuan dana di tengah meja. Jemarinya merapikan sudut kertas yang sudah terlipat tajam."
        yutaka "Kujo-san... surat di tengah meja itu pemberitahuan pembekuan dana sub-proyek risetmu?"
        harumi "Ya, Kisaragi-kun. Mulai minggu ini seluruh pencairan dana hibah untuk sub-proyek katalisku dibekukan sementara sampai audit anggaran fakultas selesai semester depan."
        yutaka "Bukannya data ujimu tinggal dua tahap lagi sebelum dikirim ke seminar musim dingin?"
        harumi "Benar. Kalau aku tidak membeli reagen pembanding sebelum akhir bulan November, seluruh sampel yang sudah kukerjakan sejak bulan Juni rusak dan harus diulang dari titik nol."
        yutaka "Prof. Mizuhara nggak bisa dimintai persetujuan darurat buat mencairkan cadangan anggaran jurusan?"
        harumi "Prof. Mizuhara sedang menghadiri simposium di Osaka sampai akhir minggu depan. Justru karena beliau sedang di luar kota, surat pembekuan ini datang di waktu paling buruk."
        nar "Ia mengembuskan napas pendek lalu membetulkan letak kacamata bingkai tipisnya dengan gerakan yang lebih kaku dari biasanya. Kalung lambang atom di lehernya berkilau redup ketika ia meraih ponselnya dan menggesernya ke tengah meja."
        nar "Di layar ponsel yang menyala itu terpampang rentetan pesan dari Ogawa Masato yang dikirim setengah jam sebelumnya."
        "Pesan Ogawa" "Kujo-san, aku sudah dengar soal pembekuan anggaranmu. Sayang sekali kalau risetmu berhenti di tengah jalan. Aku bisa talangi biaya reagennya lewat jalur dana pribadiku dulu."
        "Pesan Ogawa" "Nanti kita bahas rinciannya berdua di luar jam kampus saja biar lebih leluasa. Soal kompensasi dan urusan evaluasi proyek ke depan tidak perlu ditulis di berkas resmi fakultas."
        yutaka "Kalimat terakhirnya itu mencurigakan sekali, Kujo-san. Di bisnis maupun kampus, orang yang minta bahas kesepakatan uang di luar jam kerja tanpa catatan resmi selalu sedang menyiapkan jebakan."
        harumi "Aku tahu bagian mana yang tidak wajar, Kisaragi-kun. Aku sudah membaca pesan itu enam kali berturut-turut."
        if kk_has("harumi_eksperimen_dihentikan"):
            harumi "Sejak pembicaraan kita bulan lalu, aku sadar betul bahwa di setiap tawaran Ogawa tidak pernah ada pilihan untuk menolak. Aku tahu seharusnya aku langsung membalas tidak."
        else:
            harumi "Di setiap dokumen hibah resmi selalu ada aturan transparan dan batas kewajiban tertulis. Tawaran pribadi Ogawa sengaja menghilangkan semua batas itu supaya syaratnya hanya ditentukan oleh dirinya sendiri."
        nar "Harumi memandangi tabel anggaran dan kalender tenggat di samping ponselnya. Kedua bahunya tampak kaku menahan ketegangan yang berusaha keras ia hitung seperti persamaan kimia."
        harumi "Aku ingin menolak. Lalu lima detik kemudian aku memikirkan semua sampel yang akan rusak, rekomendasi pascasarjana yang tertunda, dan dua tahun kerja di laboratorium yang berhenti begitu saja jika dana itu tidak datang."
        harumi "Aku sedang mencoba mencari tahu apakah rasa takut sedang memanipulasi cara berpikirku sampai aku mengira tawaran Ogawa adalah satu-satunya jalan keluar yang tersedia."
        yutaka "{i}Ia sudah melihat jebakannya dengan mata terbuka lebar, tapi kepanikan soal risetnya hampir mendorongnya masuk sendiri.{/i}"
        $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["\"Kita cari jalur dana resmi sama hibah mahasiswa bareng, Kujo-san. Jangan sentuh uang pribadi Ogawa.\"", "\"Kita laporkan pesan sama syarat nggak resmi Ogawa ini ke Prof. Mizuhara dan pihak kampus, Kujo-san.\"", "Diam saja dan biarkan ia menimbang sendiri.", "Manfaatkan kepanikannya untuk mengikatnya ke syaratmu sendiri."])]
        call screen kk_choice_panel(_rows, "Pilihan Harumi")
        $ kk_record_choice("H13", _return)
        if _return == "A":
            nar "Kamu membalikkan ponsel Harumi perlahan ke permukaan meja supaya pesan Ogawa tidak terus menyita pandangannya, lalu menarik selembar kertas kosong ke tengah meja."
            yutaka "Jangan terima sepeser pun uang pribadi Ogawa, Kujo-san. Kalau dana lab lagi beku, ayo kita bedah ulang jalur pendanaan resmi sama hibah penelitian mahasiswa bareng sekarang."
            harumi "Hibah mahasiswa tingkat sarjana dan dana darurat jurusan... tenggat pencairannya jauh lebih lambat dari jadwal spektrometer akhir bulan ini, Kisaragi-kun. Penelitianku hampir pasti mundur minimal satu atau dua bulan."
            yutaka "Mundur satu atau dua bulan artinya risetmu tetap utuh milikmu sendiri. Kalau menerima syarat gelap Ogawa, ongkos yang harus kamu bayar bakal jauh lebih besar daripada satu slot alat."
            nar "Harumi menatap kertas kosong di hadapannya selama beberapa detik, lalu pandangannya perlahan kembali jernih. Ia meraih penanya dan menarik buku panduan beasiswa penelitian dari tasnya."
            harumi "Kamu benar. Terlambat masih bisa dihitung dan disesuaikan ulang skalanya. Terikat pada syarat yang tidak pernah tertulis justru memiliki risiko tak terukur."
            yutaka "Coba kita petakan dari pintu paling realistis dulu. Ada dana penelitian kecil fakultas, hibah asosiasi alumni sains, sama opsi kirim surel langsung ke Prof. Mizuhara di Osaka supaya slot spektrometer ditunda sementara."
            harumi "Jika aku memperkecil volume sampel uji menjadi setengahnya, biaya reagen tahap pertama juga turun empat puluh persen. Aku bisa mengirim draf penyesuaian ke Prof. Mizuhara lewat surel begitu selesai dari sini."
            yutaka "Perhitungan yang rapi. Bagian proyeksi anggaran proposalnya biar kubantu susunkan format resminya minggu ini supaya pengajuannya langsung lolos verifikasi administrasi."
            harumi "...Jalur pendanaan resmi memang lebih lambat dan merepotkan, Kisaragi-kun. Tapi setidaknya aku tidak perlu berutang ruang hidupku pada siapa pun."
            yutaka "Sini, minum teh panggangnya dulu sambil kita susun daftar kontaknya satu per satu. Nggak perlu terburu-buru membalas pesan Ogawa."
            harumi "Baik. Aku bahkan bisa membalasnya singkat saja bahwa aku akan menempuh jalur hibah jurusan."
            nar "Harumi membalik lembar surat pembekuan dana itu ke bawah tumpukan lalu mulai menulis daftar pintu resmi yang bisa diketuk dengan tangan yang jauh lebih tenang."
        elif _return == "B":
            nar "Kamu menunjuk dua baris pesan terakhir di layar ponsel Harumi dengan nada datar yang tegas, membuat Harumi mengangkat wajah menatap mata abu-abu gelapmu lurus."
            yutaka "Kujo-san, ini sudah jauh melewati urusan dana lab. Ogawa sengaja memanfaatkan pembekuan anggaran buat memancing pertemuan tertutup pakai syarat nggak resmi. Ayo kita laporkan dia ke Prof. Mizuhara dan komite etik kampus."
            nar "Jari Harumi yang menyentuh pinggir ponsel sempat menegang pelan. Sorot matanya meredup bimbang sejenak."
            harumi "Melaporkan Ogawa secara resmi... ia kandidat doktor senior yang memegang banyak jaringan pengelola alat di gedung Sains, Kisaragi-kun. Kalau laporanku dianggap berlebihan atau kurang bukti, posisiku di laboratorium bisa langsung dipersulit."
            yutaka "Justru karena dia mengandalkan jabatannya buat bikin kamu takut bicara, dia bakal terus mengulang cara ini kalau dibiarkan. Aku nggak menyuruh kamu jalan sendirian, aku ikut mendampingi sampai ruang Prof. Mizuhara begitu beliau balik dari Osaka."
            yutaka "Dan kamu sendiri yang menentukan bagian mana saja yang siap disampaikan nanti. Nggak ada satu orang pun yang berhak memaksamu membuka hal di luar batasmu."
            harumi "Kamu bahkan berasal dari Fakultas Ekonomi, Kisaragi-kun... kamu yakin mau ikut terseret ke gesekan internal laboratorium Sains?"
            yutaka "Tekanan jabatan sejelas ini bukan cuma urusan satu lab, Kujo-san. Nggak ada orang yang seharusnya menghadapi pemerasan halus begini sendirian."
            nar "Keheningan pendek menyelimuti sudut perpustakaan. Harumi memandangi pesan di layarnya sekali lagi, lalu bahunya tegak kembali perlahan."
            harumi "...Aku takut, Kisaragi-kun. Jujur saja, menghadapi konflik formal seperti ini adalah hal yang paling tidak bisa kuhitung hasilnya. Tapi kalau kamu bersamaku di sana, aku bersedia bersaksi tentang semua yang kulihat dan kuterima."
            yutaka "Bagus. Sebelum Ogawa sempat menarik atau menghapus pesannya, ambil tangkapan layarnya dulu sekarang, sekalian kumpulkan jadwal lab dan riwayat surel lama yang pernah dia kirim."
            nar "Harumi mengangguk mantap. Ia segera menyimpan tangkapan layar percakapan itu ke folder cadangan, lalu mengambil dua lembar catatan jadwal laboratorium yang pernah dicoret Ogawa sebelumnya dari dalam map."
            harumi "Aku juga masih menyimpan salinan surat pembekuan dana dan catatan jam perubahan alat dari bulan lalu. Semuanya fakta yang dapat diperiksa."
            yutaka "Kita kirim permintaan jadwal menghadap ke sekretariat Prof. Mizuhara sama komite etik hari ini juga, biar semuanya tercatat resmi tanpa lewat perantara siapa pun."
            harumi "Baik. Untuk pertama kalinya aku tidak merasa harus menukar rasa tidak nyamanku dengan pengorbanan baru hanya demi membuktikan bahwa sesuatu memang keliru."
            nar "Ia merapikan seluruh bukti itu ke dalam satu map plastik bening. Rasa takutnya belum lenyap sepenuhnya, tetapi kini ia berhenti berdiri sendirian di hadapan tekanan Ogawa."
        elif _return == "C":
            nar "Kamu menatap layar ponsel Harumi dan deretan angka anggaran di meja tanpa sepatah kata pun. Kamu menyandarkan bahumu ke kursi dan membiarkan keheningan penuh menggantung di antara kalian."
            harumi "Kisaragi-kun... menurutmu bagaimana? Kalau aku menolak, semua kerja enam bulan terakhir benar-benar terhenti."
            yutaka "Itu keputusan risetmu sendiri, Kujo-san. Aku anak Ekonomi, kurang etis kalau aku ikut menentukan seberapa penting jadwal alat di lab Sains."
            nar "Sorot harap tipis yang tadi sempat singgah di mata abu-kebiruan Harumi padam seketika. Ia mengangguk kecil seperti baru menerima konfirmasi bahwa seluruh beban itu memang harus ia hitung sendiri dari awal hingga akhir."
            harumi "...Benar juga. Ini variabel penelitianku sendiri. Tidak adil kalau aku mengharapkan orang lain memikul keputusan biayanya."
            nar "Ia kembali menunduk memeriksa lembar pesanan reagen, mencoret angka demi angka sambil terus membandingkan kehilangan risetnya dengan kalimat kabur di layar ponsel Ogawa."
            yutaka "Kamu jadi mau membalas pesannya?"
            harumi "Kalau aku hanya menerima pinjaman dana ini sementara sampai tahap pengukuran spektrometer bulan Desember selesai, mungkin dampaknya masih bisa kukendalikan."
            harumi "Aku bisa menjalaninya sementara. Sampai risetnya aman."
            nar "Jari-jarinya mengetik balasan singkat menyetujui pertemuan tertutup Ogawa lalu menekan tombol kirim dengan gerakan kaku. Tidak sampai setengah menit kemudian, layar ponsel itu menyala kembali membawa balasan cepat."
            "Pesan Ogawa" "Keputusan bijak, Kujo-san. Datanglah besok habis jam praktikum ke restoran di dekat stasiun selatan, aku sudah memesan ruang pribadi supaya kita bisa bicara tenang."
            nar "Harumi membaca satu baris pesan itu tanpa ekspresi, lalu langsung membalikkan layar ponselnya ke permukaan meja."
            harumi "Maaf sudah menyita waktumu di tengah persiapan Festival Seni, Kisaragi-kun. Aku harus segera ke ruang dokumen sebelum jam tutup."
            yutaka "{i}Kata sementara yang barusan ia sebut bahkan tidak punya tanggal berakhir yang jelas...{/i}"
            nar "Ia membereskan seluruh rencana kerjanya dengan terburu-buru lalu melangkah pergi. Keputusan yang lahir dari keheninganmu itu mungkin menyelamatkan reagennya minggu ini, sambil membuka pintu jauh lebih lebar bagi kendali Ogawa atas hidupnya."
        else:
            nar "Kamu memandangi wajah pucat Harumi dan rentetan pesan Ogawa di atas meja selama dua detik yang sunyi. Alih-alih menutup jebakan itu, kamu menyandarkan lengan yang melingkari jam tangan tali kulit di atas meja dengan ketenangan dingin yang terlalu akrab dari lingkungan keluarga Kisaragi."
            yutaka "Kamu nggak usah terima tawaran mencurigakan dari Ogawa, Kujo-san. Kebetulan rekening pribadiku cukup longgar buat menalangi biaya reagen tahap awalmu minggu ini juga."
            nar "Mata abu-kebiruan Harumi langsung terangkat cepat menatapmu dengan keterkejutan bercampur rasa lega yang rapuh."
            harumi "Kamu serius mau menalangi biaya reagenku, Kisaragi-kun? Itu jumlahnya tidak kecil... bagaimana aku harus mengembalikannya?"
            yutaka "Aku nggak minta kamu mencicil uangnya dalam waktu dekat. Cuma karena aku mengeluarkanmu dari posisi terpojok di depan Ogawa, wajar kan kalau aku minta syarat yang jelas juga di antara kita?"
            harumi "Syarat seperti apa yang kamu maksud?"
            yutaka "Mulai bulan ini sampai semester selesai, kapan pun aku butuh waktu, pengolahan data, atau kehadiranmu buat jadwal yang kuatur di luar lab, kamu harus mendahulukan aku dulu sebelum orang lain. Termasuk kalau ada urusan sama Koita atau kelompok lain."
            nar "Jemari Harumi berhenti di pinggir surat pembekuan dana. Kacamata tipisnya memantulkan lampu baca saat ia menimbang kalimatmu dalam diam yang dingin dan kaku."
            harumi "...Kalau aku menerima bantuanmu, berarti aku menukar ikatan dengan Ogawa menjadi ketergantungan penuh pada syaratmu, Kisaragi-kun."
            yutaka "Setidaknya aku menaruh angkanya terbuka di atas meja sekarang, Kujo-san. Tinggal pilih mau berhenti riset besok, masuk ke pertemuan tertutup Ogawa, atau menerima jalanku."
            harumi "Dan kalau suatu hari jadwalmu bertabrakan dengan jam istirahat atau janjiku di asrama bersama Ogiwara-san?"
            yutaka "Berarti kamu menggeser jadwal lain itu dulu sesuai kesepakatan kita."
            nar "Keheningan panjang menekan bahu Harumi hingga ia perlahan memejamkan mata satu detik. Ketika ia kembali menatapmu, tidak ada kelegaan sedikit pun di wajahnya."
            harumi "...Baik. Kirimkan daftar jadwal yang kamu inginkan. Aku akan memenuhinya supaya risetku bisa tetap berjalan bulan ini."
            yutaka "Sepakat kalau begitu, Kujo-san. Besok kusiapkan transfer bagian awal dananya."
            nar "Harumi menuliskan namamu di pojok buku catatannya dengan garis tinta lurus yang dingin. Risetnya mungkin akan bergerak kembali minggu depan, sementara ruang kebebasannya baru saja berpindah tangan lewat ketakutan yang kamu manfaatkan."
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
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Lampu baca di lantai dua Perpustakaan Pusat menyala putih terang di atas deretan meja kosong menjelang libur Natal bulan Desember. Angin musim dingin mengetuk kaca jendela besar di samping rak jurnal kimia, membawa hening yang jauh lebih lengang dari biasanya."
        else:
            nar "Cahaya musim dingin bulan Desember mengalir pucat melalui jendela kaca tinggi Perpustakaan Pusat yang hampir kosong menjelang libur Natal. Aroma kertas lama bercampur dingin udara pemanas ruangan menyelimuti barisan meja sudut."
        nar "Dua mahasiswi di meja depan baru saja membereskan tumpukan buku catatan mereka sambil membungkus syal wol tebal ke leher, lalu melambaikan tangan pelan ke arah meja Harumi sebelum melangkah menuju tangga."
        "Mahasiswi Perpustakaan" "Kujo-san belum pulang juga? Gedung sains besok sudah mulai tutup libur Natal lho. Selamat Natal ya, duluan!"
        harumi "Terima kasih. Selamat Natal juga."
        "Teman Mahasiswi" "Hati-hati kalau pulang kemalaman, angin di depan gerbang dingin banget!"
        nar "Begitu langkah keduanya menghilang di ujung rak dan lantai dua benar-benar sunyi, kamu menghampiri meja sudut sambil membawa dua kaleng teh hangat dari mesin minuman lantai bawah."
        nar "Harumi duduk tegak mengenakan kardigan abu-abu tipis di atas kemeja putih rapi. Rambut abu-abu perak panjangnya yang berkepang samping dan bersanggul kecil berhiasan jepit mawar merah tampak sangat rapi, sementara kalung lambang atom di lehernya memantulkan cahaya redup lampu baca."
        nar "Kamu menarik kursi di hadapannya dengan pelan agar tidak memecah kesunyian lantai dua. Anehnya, termos baja ringan yang biasa ia buka di sebelah buku catatan masih tersimpan rapat di dalam tasnya, dan satu pun buku teks kimia tidak terlihat terbuka di meja."
        nar "Di atas meja di hadapannya hanya ada tiga benda yang diletakkan sejajar persis seperti sedang dibandingkan dalam percobaan, kalender jadwal resmi kampus yang sudah dicoret kosong untuk libur tanggal dua puluh empat Desember, buku catatan sakunya yang terbuka di halaman daftar tanggal, dan layar ponselnya yang menyala tenang."
        chiasa "Kujo-senpai, ini teh hangatnya biar tangannya nggak kaku kedinginan. Sudah berapa lama Senpai duduk di sini? Tumben banget buku kimianya nggak dikeluarkan sama sekali, cuma memandangi kalender sama layar ponsel begitu."
        harumi "Sekitar lima puluh menit, Amamiya-san. Aku berniat merapikan ulang grafik analisis terakhir sebelum perpustakaan tutup, tetapi pikiranku terus terhenti pada satu pesan ini."
        nar "Saat kamu meletakkan kaleng teh hangat itu di dekat telapak tangannya, jari Harumi terasa begitu dingin meski pemanas udara perpustakaan menyala cukup hangat. Ia mengangkat pandangan mata abu-kebiruannya di balik kacamata bingkai tipis, lalu memutar ponselnya perlahan ke arahmu supaya kamu bisa membaca deretan pesan yang baru masuk satu jam lalu."
        "Pesan Ogawa" "Kujo-san, mumpung jadwal perkuliahan sudah kosong saat malam Natal besok, saya ingin mengundangmu untuk sesi diskusi lanjutan di restoran dekat stasiun timur pukul tujuh malam."
        "Pesan Ogawa" "Tidak perlu membawa berkas berat atau mengajak orang lain, datanglah sendiri saja supaya kita bisa membahas kelanjutan posisimu di proyek riset dengan suasana yang lebih tenang."
        chiasa "Senpai... ini undangan diskusi apaan? Nggak ada agenda rapat, nggak ada daftar materi riset, terus minta datang sendirian tepat di malam Natal?"
        nar "Harumi menarik selembar surat edaran cetak bercap Fakultas Sains dari map beningnya dan meletakkannya tepat di samping ponsel itu."
        harumi "Aku sudah mengecek papan pengumuman Fakultas Sains dan jadwal resmi gedung laboratorium, Amamiya-san. Seluruh ruangan riset, termasuk sekretariat Prof. Mizuhara, libur total sejak tanggal dua puluh empat sampai awal Januari. Tidak ada jadwal evaluasi praktikum pada tanggal itu."
        nar "Ia menggeser buku catatan sakunya ke dekat sikumu. Di halaman itu tertulis tiga baris catatan tanggal pesan Ogawa sepanjang sebulan terakhir, semuanya ditandai dengan rapi memakai pena biru tipis."
        harumi "Awal bulan ia meminta bimbingan tambahan setelah kelas dengan menulis bahwa ia sudah meluangkan waktu pribadinya demi penelitianku. Minggu lalu ia meminta diskusi di kafe dekat stasiun dengan alasan laboratorium sedang dibersihkan."
        harumi "Sekarang ia meminta pertemuan berdua di restoran pada malam Natal tanpa membawa satu pun berkas, sambil lagi-lagi menyinggung kelanjutan posisiku di proyek riset."
        chiasa "Lihat polanya aja sudah jelas banget, Senpai. Setiap kali dia minta ketemu di luar kampus, dia selalu menyelipkan kalimat seolah dia sudah berkorban banyak biar Senpai merasa berutang budi."
        nar "Harumi membalik satu halaman lebih awal di buku catatan sakunya, menatap deretan tanggal dari semester lalu sambil mengerutkan kening tipis."
        harumi "Saat tahun pertama dulu, aku memang sering kesulitan membedakan kritik akademik yang keras dengan tekanan pribadi. Tetapi cara Prof. Mizuhara berbicara selalu datar, jelas agendanya, dan tidak pernah berubah manis lalu dingin dalam satu hari."
        chiasa "Coba Senpai ingat satu hal paling jujur saja. Begitu pesan undangan malam Natal dari Ogawa-san masuk di layar ponsel satu jam lalu, apa yang pertama kali Senpai rasakan di dada?"
        harumi "Dada terasa menyempit dan tenggorokanku langsung kering, Amamiya-san. Aku sampai menutup layar ponsel dua kali sebelum berani membacanya sampai baris terakhir."
        chiasa "Nah, reaksi badan Senpai sendiri sebenarnya sudah kasih peringatan dari detik pertama."
        if kk_has("ogawa_dilaporkan"):
            harumi "Setelah laporan kita bulan lalu masuk ke komite, proses pemeriksaan administratif belum mengeluarkan keputusan resmi. Kemarin Ogawa berpapasan denganku di lorong dan menyebut undangan ini sekadar untuk meluruskan kesalahpahaman agar tidak merusak suasana laboratorium."
        elif kk_has("harumi_dana_bersih"):
            harumi "Meski aku sudah mengajukan jalur hibah mahasiswa bulan kemarin, Ogawa tetap menuliskan bahwa tanda tangan evaluasi praktikum semester ini masih melewati mejanya."
        else:
            harumi "Sejak urusan pembekuan dana bulan lalu, setiap kali aku bertanya soal jadwal evaluasi laboratorium, ia selalu mengarahkannya ke pertemuan di luar jam kampus seperti ini."
        chiasa "Oh iya, tadi aku sempat papasan sebentar sama Ogiwara-san dekat lobi asrama, katanya penghuni asrama yang nggak pulang kampung mau bikin makan malam panci hangat pas malam Natal. Kujo-senpai sudah jawab ikut belum?"
        harumi "Belum, Amamiya-san. Pesan dari Ogiwara-san masih terbuka di bawah pesan Ogawa. Aku belum berani mengiyakan makan malam asrama karena pesan undangan ini membuat kepalaku langsung macet."
        nar "Kamu memperhatikan ujung jari telunjuk Harumi mengetuk pinggir kalender kertas dengan irama cepat yang tidak biasa. Ia tidak tampak bingung lagi mengenai kejanggalan pesan tersebut."
        chiasa "Berarti Kujo-senpai sendiri sebenarnya sudah tahu jelas kalau pertemuan itu nggak ada hubungannya sama jadwal riset resmi kan?"
        harumi "Ya. Secara logika, tidak ada alasan ilmiah mengapa evaluasi data harus dilakukan berdua di restoran pada malam Natal tanpa satu pun berkas."
        nar "Harumi menarik napas pendek lalu membetulkan letak kacamatanya dengan jemari yang dingin. Tatapannya turun kembali ke layar ponsel."
        harumi "Aku tidak ingin pergi, Amamiya-san. Bagian itu sudah sangat jelas sekarang di dalam kepalaku. Aku benar-benar tidak ingin duduk di meja itu berdua dengannya."
        chiasa "Kalau Senpai sudah jelas nggak ingin pergi, kenapa pesannya belum langsung dibalas tolak aja?"
        harumi "Justru itu anomali yang belum bisa kupecahkan... Yang belum jelas adalah kenapa setiap kali aku mengetik kata maaf saya tidak bisa hadir, tanganku langsung berhenti karena merasa aku tidak boleh memakai alasan tidak ingin."
        harumi "Di kepalaku selalu muncul perhitungan bahwa kalau aku menolak hanya karena tidak nyaman, ia akan menganggapku tidak kooperatif, tidak menghargai senior, dan berhak mencabut akses laboratoriumku nanti."
        chiasa "{i}Ogawa berhasil menanamkan rasa bersalah di kepalanya sampai keinginan sederhana untuk menolak pun terasa seperti pelanggaran disiplin.{/i}"
        call kk_family_menu("H14", ["\"Jangan pergi sendiri ke pertemuan itu, Kujo-senpai. Aku melarang Senpai datang.\"", "\"Kalau Senpai tetap harus ketemu dia, biar aku ikut menemani sampai selesai.\"", "\"Kalau Senpai merasa itu penting buat urusan lab, terserah Senpai saja.\""])
        if _return == "A":
            nar "Kamu meletakkan telapak tanganmu dengan mantap di samping ponsel Harumi dan menatap mata abu-kebiruannya lurus tanpa sedikit pun memberi celah keraguan."
            chiasa "Jangan pergi, Kujo-senpai. Aku melarang Senpai datang ke pertemuan malam Natal itu sendirian."
            nar "Harumi tersentak sangat halus, kelopak matanya berkedip dua kali mendengar ketegasan yang sama sekali tidak dibungkus basa-basi sopan."
            harumi "Kamu melarangku keras sekali, Amamiya-san..."
            chiasa "Iya, aku melarang keras. Lihat faktanya sendiri deh, Senpai. Kampus libur resmi, nggak ada agenda, nggak ada peserta lain, dan Senpai sendiri baru bilang dengan mulut sendiri kalau Senpai nggak ingin pergi. Itu sudah lebih dari cukup buat bilang tidak."
            nar "Harumi terdiam cukup lama memandangi wajahmu yang serius. Ketegangan di antara kedua alisnya perlahan mulai mengendur."
            harumi "...Baik. Untuk malam Natal kali ini, aku memercayai reaksimu lebih daripada ketidakmampuanku membaca niat orang lain."
            chiasa "Kalau begitu sekarang langsung balas pesannya di sini, jangan ditunda sampai pulang ke asrama biar kepalamu nggak terus muter-muter lagi."
            nar "Harumi mengambil ponselnya, mengetik beberapa kalimat pendek, lalu menunjukkannya kepadamu sebelum menekan tombol kirim."
            harumi "Permisi, Ogawa-san. Karena seluruh agenda laboratorium resmi sudah tutup selama libur Natal, saya tidak dapat menghadiri pertemuan pribadi di luar kampus. Pembahasan riset akan saya lanjutkan di ruang lab saat kampus buka kembali. Terima kasih."
            chiasa "Rapi, sopan, dan nggak membuka celah buat dinegosiasi. Kirim aja sekarang, Senpai."
            nar "Begitu tombol kirim ditekan, status pesan langsung berubah terbaca dalam kurang dari satu menit. Layar ponsel bergetar pendek memunculkan balasan cepat yang terasa dingin."
            "Pesan Ogawa" "Sangat disayangkan, Kujo-san. Saya sudah repot menyiapkan waktu di tengah libur demi membantu kelancaran risetmu. Semoga keputusanmu tidak membuat koordinasi kita Januari nanti terasa kaku."
            nar "Jari Harumi langsung menegang melihat kalimat terakhir itu. Secara refleks ibu jarinya langsung bergerak ke kolom ketik untuk menuliskan permintaan maaf tambahan, membuatmu segera menyentuh lembut punggung tangannya di atas meja."
            chiasa "Eh, stop dulu, Senpai! Jangan balas minta maaf lagi! Lihat baik-baik isi pesannya barusan!"
            chiasa "Begitu Senpai bilang tidak secara resmi, dia langsung melempar ancaman halus soal bulan Januari. Mana ada senior yang beneran niat bantu riset merajuk begitu cuma gara-gara mahasiswa menolak makan malam pribadi saat hari libur?"
            harumi "...Tanganku tadi otomatis mau mengetik maaf padahal aku tidak melakukan kesalahan prosedur apa pun. Reaksinya justru memverifikasi hipotesismu secara akurat. Jika tujuannya murni akademik, balasan sopanku seharusnya diterima tanpa masalah."
            nar "Harumi menarik tangannya dari layar, meletakkan ponselnya dalam posisi terbalik di atas meja, lalu mengembuskan napas panjang yang akhirnya terdengar lega. Ia membuka halaman bersih buku catatan sakunya."
            harumi "Amamiya-san... terima kasih sudah menahanku tadi. Tapi setelah ini, boleh kita bicarakan bersama bagaimana caranya aku bisa mempertahankan keputusan serupa di lain hari tanpa harus menunggu seseorang melarangku lebih dulu?"
            chiasa "Tentu saja boleh, Senpai. Kita mulai dari satu aturan paling dasar dulu, ketidaknyamanan Senpai itu data yang sah dan nggak perlu dihapus. Ayo sekalian kita tulis dua contoh kalimat penolakan pendek di bukumu biar kalau dia kirim pesan lagi, Senpai tinggal pakai."
            harumi "Ketidaknyamanan adalah data yang sah... baik, akan kucatat itu di halaman paling depan. Lalu di bawahnya aku tulis batasan pertemuan hanya di gedung kampus pada jam resmi. Aku ingin suatu hari nanti bisa mengatakan tidak atas namaku sendiri juga."
            chiasa "Coba kita latihan sebentar ya, Senpai. Misal nanti bulan Januari pas kampus buka, Ogawa-san nyindir di lorong bilang koordinasi kalian jadi kaku gara-gara Natal kemarin, Senpai mau jawab apa?"
            nar "Harumi menatap catatan barunya selama dua detik, lalu mengangkat wajahnya dengan sorot mata abu-kebiruan yang jauh lebih jernih."
            harumi "Saya akan menjawab bahwa saya selalu siap berkoordinasi di ruang laboratorium pada jam kerja Prof. Mizuhara, serta meminta daftar agenda tertulis sebelum pertemuan dimulai."
            chiasa "Nah, tepat sasaran banget! Sopan, resmi, nggak ada celah buat dia memutar balik fakta kalau Senpai nggak kooperatif."
            chiasa "Satu latihan lagi ya, Senpai. Gimana kalau pas kampus buka nanti dia sengaja mencegat Senpai di koridor dekat ruang ganti lab waktu ruangan lagi sepi?"
            harumi "Aku tidak akan berhenti berbicara sendirian di lorong sepi. Aku akan mengatakan bahwa aku sedang ditunggu rekan laboratorium atau langsung berjalan menuju meja sekretariat Prof. Mizuhara."
            chiasa "Sempurna banget, Senpai! Begitu cara bicaranya sudah siap di kepala, nanti Senpai nggak bakal gampang kaget kalau dia tiba-tiba muncul."
            harumi "Sebentar, boleh aku membacakan kalimat catatanku sekali lagi dengan suara pelan? Aku ingin memastikan lidahku sendiri terbiasa mengucapkannya."
            chiasa "Silakan, Senpai. Aku dengar."
            harumi "Saya hanya melaksanakan diskusi riset di ruang laboratorium pada jam resmi Prof. Mizuhara. Untuk pertemuan di luar agenda kampus, saya tidak dapat hadir."
            nar "Harumi mengerjap tipis begitu kalimat itu selesai diucapkannya di udara yang sunyi, tampak terkejut sendiri oleh betapa stabil nadanya terdengar."
            harumi "Ternyata menyusunnya sebagai prosedur standar lalu mengucapkannya keras-keras jauh lebih mudah daripada terus menebak apakah dia akan tersinggung atau tidak."
            chiasa "Nah, sekarang mumpung ponselnya di situ, balas juga pesan Ogiwara-san buat makan malam panci hangat di asrama ya, Senpai."
            harumi "Ya. Aku akan bilang aku ikut membantu memotong sayuran. Aku jauh lebih senang berada di ruang makan asrama daripada menebak maksud orang lain."
            nar "Jari Harumi bergerak mengetik balasan untuk Ogiwara-san dengan jauh lebih ringan. Tidak sampai satu menit, balasan antusias dari pengelola asrama muncul di layar membuat bahu Harumi turun lega."
            nar "Kamu membuka kaleng teh hangat dan menyodorkannya ke dekat tangannya. Harumi meraih kaleng itu dengan kedua telapak tangannya yang mulai kembali hangat, lalu menyesapnya pelan sambil tersenyum amat tipis ke arah jendela kaca perpustakaan."
            chiasa "Tehnya masih hangat kan, Senpai?"
            harumi "Masih hangat sekali. Terima kasih, Amamiya-san."
            chiasa "Nanti begitu masuk kampus awal Januari, kita tetap ketemu rutin di meja ini ya, Senpai. Sekalian ngecek progres grafik presentasi sama lihat perkembangan catatan batasan Senpai."
            harumi "Ya, aku akan menandai jadwal pertemuan resmi kita di buku saku sekarang juga. Ogiwara-san baru membalas memintaku datang pukul enam untuk membantu menyiapkan kaldu panci hangat. Rasanya jauh lebih tenang punya rencana yang jelas."
            nar "Di sudut perpustakaan yang tenang, Harumi mencatat kalimat batasannya sendiri dengan garis pena yang jauh lebih tegak dan mantap."
        elif _return == "B":
            nar "Kamu menatap layar ponsel Harumi sejenak, lalu menyandarkan tangan di tepi meja dengan nada tenang yang langsung mematahkan rencana pertemuan berdua Ogawa."
            chiasa "Kalau Kujo-senpai merasa belum sanggup membatalkan mentah-mentah karena urusan evaluasi lab, biar aku ikut menemani Senpai datang ke pertemuan itu."
            nar "Mata abu-kebiruan Harumi langsung terangkat cepat menatap wajahmu, sorot gelisah yang sejak tadi menggantung di wajahnya seketika mencair."
            harumi "Kamu mau ikut bersamaku di malam Natal, Amamiya-san? Berarti pertemuan itu bukan lagi berdua... Entah kenapa begitu kamu mengatakan itu, dadaku langsung bisa bernapas jauh lebih lega."
            chiasa "Jelas dong. Katanya kan mau bahas kelanjutan proyek riset, sementara aku juga ikut bantu bikin tata letak grafik presentasi riset Senpai kemarin. Jadi wajar banget kalau aku ikut duduk di sana."
            harumi "Tapi di pesannya tadi ia menulis tidak perlu mengajak orang lain... kalau aku bilang kamu ikut, kira-kira bagaimana cara menyusun kalimatnya supaya tidak terdengar seperti aku mencari masalah?"
            chiasa "Justru itu cara paling cepat buat menguji apakah ini beneran diskusi riset atau bukan, Senpai. Tulis saja dengan sopan kalau aku ikut mendampingi karena sekaligus membahas penyesuaian grafik presentasi, terus sekalian tanya data apa yang perlu kita bawa."
            nar "Harumi mengangguk mengerti. Dengan jari yang kini jauh lebih tenang karena tidak lagi sendirian, ia mengetik pesan konfirmasi yang sangat teratur bahwa adik tingkat kolaborator poster risetnya, Amamiya Chiasa, akan ikut menemani ke restoran stasiun timur dan meminta daftar materi yang perlu dicetak."
            nar "Pesan itu langsung terbaca. Tidak seperti biasanya yang membalas ramah dalam beberapa detik, indikator mengetik di sisi Ogawa sempat muncul beberapa detik lalu padam tanpa hasil."
            nar "Dua menit berlalu dalam keheningan yang terasa panjang di lantai dua perpustakaan. Harumi mengetuk pelan tutup penanya di atas buku catatan sambil menatap layar ponsel tanpa berkedip."
            chiasa "Sudah dua kali indikator mengetiknya muncul terus hilang, Senpai. Kelihatan banget dia lagi bingung cari alasan."
            harumi "Secara pola waktu respons, biasanya ia membalas kurang dari tiga puluh detik setiap kali topiknya hanya melibatkan kami berdua."
            harumi "Jujur saja, Amamiya-san... di sudut kecil kepalaku, sebagian diriku masih sedikit berharap ia membalas mempersilakan kamu ikut datang. Soalnya jauh lebih melelahkan mengakui bahwa seseorang yang selama ini membimbing praktikumku memang sengaja berbohong sejak awal."
            chiasa "Aku paham rasanya nggak enak, Senpai. Tapi jauh lebih aman tahu sekarang sebelum Senpai duduk sendirian di restoran luar kampus."
            nar "Baru saja Harumi selesai menghitung, layar ponsel menyala lagi membawa satu balasan kering yang nadanya berubah seratus delapan puluh derajat."
            "Pesan Ogawa" "Oh, kalau kamu mengajak mahasiswa dari fakultas lain, rasanya tidak efektif membahas detail internal laboratorium di restoran. Tidak usah repot datang malam Natal nanti. Kita batalkan saja, urusan evaluasimu akan saya tinjau sendiri nanti."
            nar "Keheningan pendek turun di meja sudut perpustakaan. Harumi menatap layar ponselnya lama sekali, lalu menggeser ke atas dan ke bawah membaca ulang perbandingan antara pesan pertama yang penuh kehangatan dan pesan kedua yang langsung menutup pintu seketika begitu nama orang ketiga muncul."
            chiasa "Nah, Kujo-senpai lihat sendiri sekarang kan? Begitu tahu Senpai nggak datang sendirian, mendadak pembahasannya jadi tidak efektif dan langsung dibatalkan total."
            harumi "...Ya. Selisih waktu balasnya dua menit empat belas detik, jauh di luar kebiasaannya. Di pesan pertama ia menyebut tidak perlu membawa berkas apa pun. Di pesan kedua ia tiba-tiba beralasan bahasannya terlalu internal sehingga tidak boleh ada orang lain."
            harumi "Kedua pernyataan itu saling bertentangan secara langsung. Untuk pertama kalinya aku punya bukti pengamatan langsung yang bisa dibandingkan dengan seluruh klaimnya bahwa semua ini cuma demi kebaikan risetku."
            chiasa "Sekarang tangkap layar dua pesan yang berurutan itu buat arsip Senpai ya, sekalian catat jam kirimnya di buku saku. Dan karena malam Natalnya sekarang sudah bebas dari undangan aneh itu, gimana kalau Senpai ikut makan malam hangat di asrama bareng Ogiwara-san atau mampir minum teh sama aku?"
            nar "Harumi langsung menyimpan kedua tangkapan layar ke dalam folder arsip khusus di ponselnya, menamai berkasnya berdasarkan tanggal, lalu menulis ringkasan waktu balasan dua menit empat belas detik itu di bawah catatan penanya dengan tangan yang jauh lebih mantap."
            harumi "Selesai. Melihat hipotesis keraguanku terbukti langsung oleh tanggapannya sendiri justru terasa jauh lebih lega daripada terus-terusan menyalahkan perasaanku sendiri."
            chiasa "Apalagi sekarang Senpai punya catatan jam sama tangkapan layar utuh. Kalau Januari nanti dia coba memutar cerita ke Prof. Mizuhara atau orang lab lain, Senpai punya bukti tertulis yang nggak bisa dibantah."
            harumi "Benar. Data objektif jauh lebih kuat daripada dugaan yang cuma berputar di kepalaku. Untuk pertama kalinya aku merasa posisi berdiriku punya pijakan yang jelas."
            chiasa "Sekarang beban di bahu Senpai kelihatan jauh lebih ringan lho. Ayo bereskan bukunya pelan-pelan."
            harumi "Aku akan mengabari Ogiwara-san sebentar lagi supaya namaku tetap masuk daftar makan malam asrama. Tapi sebelum kita pulang... bolehkah aku duduk minum teh hangat bersamamu lebih lama di sini, Amamiya-san? Kalau sempat, nanti di jalan menuju asrama kita mampir sebentar ke toko roti dekat gerbang."
            chiasa "Tentu saja boleh, Senpai. Sekalian kita beli potongan kue stroberi hangat biar suasana Natalnya beneran terasa."
            harumi "Terima kasih sudah berdiri di sebelahku hari ini. Aku tidak lagi merasa seperti sedang menebak bayangan sendirian."
            nar "Kalian membereskan tumpukan catatan dan kalender resmi kampus bersama-sama sebelum melangkah keluar menuju lobi perpustakaan. Harumi tersenyum tipis sekali sambil menyimpan ponselnya ke saku kardigan. Satu selubung kepalsuan Ogawa baru saja runtuh tepat di depan matanya sendiri."
        else:
            nar "Kamu mengendurkan bahu, menatap kembali kaleng teh hangat di tanganmu, lalu memilih tidak ikut campur menentukan apa yang harus dilakukan Harumi."
            chiasa "Kalau menurut Kujo-senpai pertemuan itu masih berhubungan sama nasib evaluasi laboratorium Senpai bulan depan, ya terserah Senpai saja. Aku nggak berani melarang kalau ujung-ujungnya malah bikin proyek Senpai terhambat."
            nar "Harumi terdiam dua detik mendengar jawabanmu yang datar dan menjaga jarak. Sorot harap tipis yang tadi sempat ia gantungkan padamu perlahan padam."
            harumi "...Benar juga. Kamu tidak bertanggung jawab atas penilaian laboratoriumku. Mungkin aku saja yang terlalu emosional membaca satu undangan biasa."
            chiasa "Ya sudah, nanti kabari aja kalau sudah selesai ya, Senpai."
            nar "Meski beberapa menit sebelumnya ia baru saja mengatakan dengan sangat jelas bahwa dirinya tidak ingin pergi, Harumi akhirnya menunduk dan mengetik pesan singkat menyetujui datang sendiri pada malam Natal. Di bawah layar ponselnya, pesan dari Ogiwara-san tentang makan malam asrama dibiarkannya tertutup tanpa balasan."
            harumi "Baiklah, aku sudah mengirim konfirmasi kehadiran. Maaf sudah membuang waktumu di perpustakaan dengan urusan pribadiku. Aku permisi kembali ke asrama dulu untuk merapikan catatan sebelum hari libur."
            nar "Ia merapikan kalender kosong dan bukunya ke dalam tas tanpa menatapmu lagi, meninggalkan kaleng teh hangat yang tadi kamu belikan tetap tertutup utuh di sudut meja. Langkahnya menyusuri barisan rak jurnal tampak terlalu kaku dan cepat."
            nar "Beberapa hari setelah malam Natal berlalu, kamu sempat berpapasan singkat dengan Ogiwara-san di dekat gerbang asrama yang bertanya dengan nada cemas mengapa Harumi melewatkan makan malam Natal asrama dan baru pulang jauh larut malam tanpa menyentuh makan malamnya."
            nar "Ketika kamu akhirnya kembali bertemu Harumi di meja sudut Perpustakaan Pusat yang sama, ada perubahan dingin yang langsung terasa bahkan sebelum ia duduk."
            nar "Ia datang membawa buku referensi tebal, tetapi tidak lagi membuka buku catatan sakunya di samping sikumu seperti biasa. Bahunya tertutup mantel lebih rapat, dan matanya lebih sering menghindar ke halaman buku."
            nar "Kamu juga menyadari buku catatan sakunya yang biasanya selalu terselip di saku kardigan sudah tidak terlihat; di atas meja hanya ada map jadwal laboratorium baru dengan inisial tanda tangan Ogawa di pojok atas."
            chiasa "Kujo-senpai... kemarin Ogiwara-san bilang Senpai nggak ikut makan malam Natal di asrama. Bagaimana hasil diskusi riset waktu malam Natal kemarin? Lancar?"
            harumi "Sudah selesai. Aku belum ingin membicarakannya."
            chiasa "Ini aku sempat beli teh hangat kaleng lagi buat Senpai biar tangannya nggak kedinginan."
            harumi "Terima kasih, tapi simpan saja untukmu, Amamiya-san. Ogawa-san mengingatkan agar aku tidak membawa minuman manis ke area koridor laboratorium."
            chiasa "Tapi jadwal evaluasi untuk bulan Januari aman kan? Kita masih jadi melanjutkan koreksi grafik presentasi minggu depan?"
            harumi "Soal jadwal presentasi dan penggunaan waktuku di luar laboratorium, aku harus menanyakan persetujuan Ogawa-san dulu sebelum bisa memberi kepastian kepadamu, Amamiya-san."
            nar "Belum sempat kamu bertanya lebih jauh, ponsel di atas meja bergetar satu kali memunculkan nama Ogawa yang menanyakan posisi Harumi. Tanpa jeda ragu sedikit pun, Harumi langsung melirik jam tangannya lalu mengetik balasan cepat."
            harumi "Maaf, aku harus segera pindah ke gedung sains sekarang. Ogawa-san memintaku mampir sebentar untuk membahas evaluasi pribadi sebelum pintu gedung ditutup. Pembahasan grafik kita tunda sampai ada kabar darinya."
            chiasa "Eh, tunggu sebentar, Senpai... rancangan tata letak poster riset yang kemarin kita kerjakan bareng gimana? Kan tinggal penyesuaian warna tabel sedikit lagi."
            harumi "Ogawa-san sudah membantu merapikan ulang seluruh kerangka presentasiku kemarin, jadi katanya aku tidak perlu merepotkan mahasiswa dari fakultas lain lagi."
            chiasa "Senpai, mau kutemani jalan sekalian balik ke arah asrama habis itu? Ogiwara-san kemarin kelihatan agak khawatir lho."
            harumi "Tidak perlu, Amamiya-san. Aku sudah biasa pulang sendiri. Permisi."
            nar "Setiap jawabannya kini jatuh pendek, rata, dan berjarak. Dua kali dalam lima menit percakapan singkat itu, ia kembali menyebut nama dan persetujuan Ogawa seolah seluruh kalendernya tidak lagi ia pegang sendiri."
            nar "Bahkan pekerjaan kolaborasi kecil yang dulu ia banggakan dengan mata berbinar kini diserahkan begitu saja tanpa perlawanan. Kamu hanya bisa memandangi punggung Harumi yang memeluk tas bukunya erat-erat saat melangkah menjauh menyusuri koridor musim dingin, tampak jauh lebih kecil dan tertutup dibandingkan sebulan lalu."
            chiasa "{i}Setelah malam Natal itu, undangan berikutnya tidak lagi terasa seperti sesuatu yang bisa ia tolak... dan aku membiarkannya berjalan sendirian masuk ke pintu itu.{/i}"
            nar "Malam Natal itu sudah lewat di kalender, tetapi dingin dan kepatuhan diam-diam yang ia bawa pulang kini terus memanjang di dalam setiap kebiasaannya."
    else:
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
