# Arc Shiori endgame (S04, S05, S20-S24): dari pertandingan shogi dan kemunculan
# pewaris Tojo, menuju klimaks "penghancuran" tempat Shiori membalas kebohongan
# yang ia deteksi. Ditulis sebagai KARAKTER dan KONSEKUENSI (shogi sebagai metafora
# strategi sosial); manuver balasnya dicatat sebagai akibat, bukan panduan. Jalur
# jujur/mengaku/bersekutu tersedia. Penempatan Klub Catur prototipe; Tojo pakai
# nama-penutur. Mengikuti Event_Shiori; melengkapi S07/S09/S13-S19 (Codex) + S-D.

# ┌─ PANDUAN CERITA · S04 · Pertandingan Malam di Vila
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia bermain shogi sampai larut.
# │ INTI    : A temani / B menang jujur / C menyontek.
# │ AKHIRAN : C masuk daftar kebohongan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S04:
    call kk_scene_enter("shiori", "Klub Catur · Pertandingan malam vila")
    if kk_host == "chiasa":
        nar "Jarum jam dinding sudah melewati pukul sebelas malam ketika lantai bawah vila mulai hening. Lampu ruang makan sudah dipadamkan, menyisakan garis cahaya kuning hangat yang keluar dari celah pintu geser ruang tatami kecil di sisi timur beserta bunyi ketukan kayu yang jatuh teratur."
        nar "Saat kamu melongok dari balik pintu geser, Saionji Shiori tampak duduk bersimpuh seorang diri di atas bantal tatami menghadap papan shogi kayu. Ia mengenakan kardigan malam berwarna ungu gelap di atas pakaian santainya, dengan rambut putih keperakan yang jatuh rapi melewati bahu."
        nar "Ia baru saja menarik mundur dua bidak kayu ke petak sebelumnya, menatap sudut papan selama beberapa detik, lalu tersenyum tipis seorang diri."
        chiasa "Saionji-senpai belum tidur juga? Masih main shogi sendirian jam segini?"
        shiori "Selamat malam, Amamiya-san. Aku tidak sedang bermain babak baru kok. Aku hanya sedang menyusun ulang pertandingan waktu di ruang klub kemarin sore."
        chiasa "Memangnya ada yang keliru sama pertandingan kemarin, Senpai?"
        shiori "Tadi waktu aku baru mau tidur di kamar atas, tiba-tiba aku teringat langkahku di giliran ketiga puluh delapan kemarin. Aku mendorong bidak bentengku satu petak terlalu cepat. Aku bisa saja mencari alasan bahwa kemarin aku sedang lelah sehabis kuliah, tapi kenyataannya waktu memegang bidak itu kemarin, kepalaku sadar penuh."
        nar "Dengan gerakan jari yang cekatan dan terlatih, Shiori merapikan kembali seluruh bidak kayu itu ke dalam dua barisan awal yang berhadapan, lalu melirik bantal duduk kosong di seberang mejanya."
        shiori "Mumpung kamu belum mengantuk dan turun ke sini, bagaimana kalau kita main satu babak, Amamiya-san? Atau kamu sebenarnya sudah mau tidur, hanya terlalu sopan untuk langsung berbalik?"
    else:
        nar "Lewat pukul sebelas malam, lantai bawah vila sudah sepi setelah rombongan lain naik ke kamar masing-masing. Hanya cahaya lampu kuning dari ruang tatami samping yang masih menyala, diselingi bunyi ketukan jernih bidak kayu di atas papan."
        nar "Ketika kamu melongok melewati ambang pintu geser, Saionji Shiori sedang duduk sendirian di depan papan shogi. Ia baru saja memundurkan dua bidak kayu, menatap posisinya beberapa detik, lalu tersenyum tipis pada dirinya sendiri."
        yutaka "Belum tidur, Saionji-san? Masih betah aja mengutak-atik papan shogi jam segini?"
        shiori "Selamat malam, Kisaragi-san. Aku baru saja teringat pertandingan di klub kemarin sore. Di giliran ketiga puluh delapan waktu itu, aku melakukan langkah yang cukup ceroboh di sayap kanan."
        yutaka "Padahal kemarin kan kamu tetap menang di babak itu."
        shiori "Menang karena lawan tidak melihat celahku bukanlah alasan untuk membiarkan langkah buruk itu lewat begitu saja. Mudah saja kalau mau menyalahkan kelelahan kuliah, tapi kemarin aku melakukannya dalam keadaan sadar penuh."
        nar "Ia mengumpulkan bidak-bidak kayu itu dan menyusunnya kembali ke garis awal dengan gerakan rapi, lalu menatap bantal duduk kosong di seberangnya."
        shiori "Masih sanggup bermain satu babak denganku malam ini, Kisaragi-san? Atau kamu sebenarnya sudah mengantuk dan cuma sungkan menolak?"
    call kk_family_menu("S04", ["\"Aku belum ngantuk kok. Ayo main, tapi kita batasi sampai tengah malam ya.\"", "Bermain fokus penuh untuk mengalahkannya secara jujur.", "Intip catatan strategi di ponselmu saat ia lengah."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu melangkah masuk ke ruang tatami dan duduk bersimpuh di atas bantal seberang papan shogi."
            chiasa "Aku belum ngantuk kok, Saionji-senpai. Ayo main satu babak, tapi kita batasi sampai jam setengah satu malam aja ya supaya besok pagi nggak bangun kesiangan."
            shiori "Syarat yang sangat masuk akal. Silakan ambil langkah pembukanya, Amamiya-san."
            nar "Selama hampir satu jam berikutnya, keheningan ruang tatami itu diisi bunyi ketukan bidak kayu dan percakapan pendek setiap kali salah satu dari kalian memindahkan perwira di tengah papan. Kamu tidak terburu-buru menyerang, dan Shiori pun menikmati ritme permainan yang tenang tanpa tekanan jam turnamen."
            nar "Tepat ketika jarum jam dinding di sudut ruangan menunjuk pukul setengah satu lewat lima menit, Shiori meletakkan bidak peraknya di petak pertahanan, lalu mengangkat tangan memberi isyarat jeda."
            shiori "Sudah lewat tengah malam seperti kesepakatan kita tadi. Ternyata kamu benar-benar tahan fokus sampai selarut ini ya, Amamiya-san. Kebanyakan orang kalau menemaniku bermain malam-malam sudah bolak-balik melirik jam sejak tiga puluh menit pertama."
            chiasa "Habisnya lihat cara Senpai nutup celah di baris tengah tadi seru banget, jadi nggak kerasa jamnya jalan."
            shiori "Kalau begitu kita hentikan babaknya di posisi imbang ini. Aku jauh lebih menghargai lawan yang tahu kapan harus berhenti sesuai janjinya daripada orang yang memaksakan diri begadang hanya demi terlihat menyenangkan di depanku."
            chiasa "Sini, kubantu masukkan bidaknya ke kotak kayu, Senpai."
            nar "Kalian berdua merapikan bidak-bidak shogi itu kembali ke dalam kotaknya, mematikan lampu ruang tatami, lalu naik bersama ke lantai dua yang sudah sunyi."
        else:
            nar "Kamu melangkah masuk ke ruang tatami dan duduk bersila di bantal seberang meja rendah tersebut."
            yutaka "Belum ngantuk kok, Saionji-san. Ayo main satu babak, tapi kita patok batas waktunya sampai jam setengah satu aja ya biar besok pagi nggak pusing."
            shiori "Kesepakatan yang adil. Silakan jalan duluan, Kisaragi-san."
            nar "Hampir satu jam berikutnya berjalan tenang di bawah lampu kuning ruang tatami. Tidak ada yang bermain terburu-buru; setiap kali ada pertukaran bidak yang rumit di tengah papan, kalian sempat bertukar dua-tiga kalimat ringan sebelum melanjutkan giliran."
            nar "Begitu jarum jam dinding menyentuh pukul setengah satu malam, Shiori meletakkan bidak terakhirnya di sisi raja lalu merapikan duduknya."
            shiori "Waktunya habis tepat di pertengahan babak. Kamu benar-benar bertahan fokus sampai selarut ini ya, Kisaragi-san. Jarang ada teman kampus yang mau menemaniku di depan papan tanpa melirik jam setiap sepuluh menit."
            yutaka "Soalnya lihat cara kamu memutar pertahanan di sayap kiri tadi lumayan bikin penasaran."
            shiori "Kalau begitu kita akhiri malam ini di sini. Sudah waktunya istirahat, dan aku selalu lebih menyukai lawan bicara yang jujur menjaga batas waktunya daripada yang memaksakan diri sampai pagi hanya untuk menyenangkanku."
            yutaka "Oke, biar kubantu beresin bidak bagian sini ke kotaknya."
            nar "Kalian membereskan seluruh bidak kayu itu ke dalam kotak penyimpanan, memadamkan lampu ruangan, lalu kembali ke kamar masing-masing."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kamu duduk tegak di seberang meja rendah dan memusatkan seluruh perhatianmu pada susunan bidak kayu di depan mata. Sejak langkah pembuka, kamu menjaga baris pertahananmu tetap rapat sambil menunggu Shiori mengambil inisiatif serangan."
            nar "Memasuki pertengahan babak, Shiori mendorong perwira kudanya cukup jauh di sisi kanan untuk membongkar bentengmu. Serangan agresif itu menyisakan satu petak kosong di depan barisan tengahnya. Tanpa membuang satu giliran pun, kamu langsung menjatuhkan bidak gajah cadanganmu tepat ke jantung pertahanannya."
            nar "Empat langkah kemudian, bidak terakhirmu mendarat dengan bunyi ketukan kayu yang bersih."
            chiasa "Skakmat, Saionji-senpai."
            nar "Shiori terdiam menatap papan selama tiga detik penuh. Matanya menyusuri kembali petak-petak di sekeliling rajanya untuk memeriksa apakah masih ada jalur lolos, lalu ia mengangkat wajah dengan sorot mata ungu yang berbinar terang."
            shiori "...Skakmat yang sangat bersih. Kamu benar-benar mengalahkanku malam ini, Amamiya-san. Bagus sekali. Aku paling tidak tahan kalau harus menang melawan orang yang menahan kemampuannya."
            chiasa "Jantungku juga deg-degan tadi, Senpai. Kalau Senpai sempat tarik mundur bidak emasnya satu langkah aja tadi, pertahanan kiriku yang bakal jebol duluan."
            nar "Shiori mencondongkan tubuhnya sedikit ke atas papan, menunjuk petak tempat ia memajukan kudanya tadi sambil tertawa kecil."
            shiori "Lucunya, justru langkah serangan kuda yang paling kuyakini bakal menembus baris belakangmu tadi yang malah membuka pintu masuk untuk gajahmu. Coba kita mundurkan empat langkah sebentar. Sejak giliran ke berapa kamu sudah menyiapkan umpan di petak tengah itu?"
            chiasa "Sejak tiga giliran sebelumnya, waktu Senpai geser benteng ke jalur pinggir."
            shiori "Berarti kamu sudah membacanya sejak awal pertukaran bidak tadi. Menarik sekali. Ayo kita bedah langkah itu lima menit lagi sebelum naik ke kamar."
        else:
            nar "Kamu duduk bersila di seberang papan dan langsung bermain dengan fokus penuh sejak giliran pertama. Kamu membiarkan Shiori menekan lebih dulu dari sayap kanan, sambil perlahan mengumpulkan bidak cadangan di tanganmu."
            nar "Di pertengahan permainan, Shiori mendorong bentengnya terlalu dalam untuk mengepung sisi rajamu, meninggalkan satu celah sempit di jalur diagonal tengah. Kamu langsung memanfaatkan giliran itu dengan menjatuhkan bidak gajah tepat di titik buta pertahanannya dan memaksa rajanya terdesak ke pinggir."
            nar "Bidak penutupmu jatuh di atas papan dengan bunyi klik yang tegas."
            yutaka "Skakmat, Saionji-san."
            nar "Shiori menatap papan shogi itu tanpa berkedip selama beberapa detik, memeriksa ulang setiap petak di sekitar rajanya, sebelum akhirnya mendongak menatapmu dengan mata ungu yang berbinar hidup."
            shiori "...Luar biasa bersih. Kamu sungguh mengalahkanku tanpa celah malam ini, Kisaragi-san. Aku senang sekali, karena tidak ada yang lebih membosankan daripada lawan yang diam-diam mengalah."
            yutaka "Tipis banget itu tadi. Kalau serangan bentengmu di sisi kiriku tadi nggak kupotong pakai gajah, dua langkah lagi pasti aku yang kalah."
            nar "Shiori mencondongkan badan ke arah papan, menyentuh bidak bentengnya sendiri yang terlalu maju tadi lalu tertawa pelan."
            shiori "Justru langkah benteng yang paling kuandalkan untuk menutup pergerakanmu tadi yang malah jadi titik runtuhnya pertahananku sendiri. Coba kita tarik mundur tiga giliran. Sejak kapan kamu sengaja mengosongkan petak tengah itu buat memancing bentengku naik?"
            yutaka "Sejak kamu makan pionku di baris keempat tadi. Kelihatan kalau kamu lagi buru-buru mau buka jalur kanan."
            shiori "Bacaan yang tajam. Ayo kita ulas posisi tengah ini sebentar sebelum tidur, aku belum rela naik ke kamar sebelum paham penuh jebakanmu barusan."
    else:
        if kk_host == "chiasa":
            nar "Ketika permainan memasuki babak tengah dan susunan bidak Shiori mulai mengepung sisi kirimu rapat-rapat, kamu tahu kamu akan kalah jika terus mengandalkan hitunganmu sendiri."
            nar "Tepat saat Shiori memutar tubuhnya untuk meraih teko teh di meja samping dan menuang air hangat ke cangkirnya, kamu diam-diam menyalakan layar ponsel yang tergeletak di atas pangkuanmu, mengintip diagram penyelesaian shogi dari aplikasi strategi yang tadi sempat kamu buka, lalu menyalin tiga urutan langkah jitu tersebut ke atas papan."
            nar "Lima giliran sesudahnya, barisan pertahanan Shiori runtuh oleh kombinasi serangan yang sama sekali berbeda dari gaya bermainmu di awal."
            chiasa "Ah... masuk juga akhirnya. Skakmat, Saionji-senpai."
            nar "Shiori tidak langsung menyentuh bidaknya. Ia menatap rangkaian langkah di sudut kiri papan itu selama beberapa detik dengan raut wajah yang tetap tenang, lalu mengangkat pandangannya dan tersenyum sopan."
            shiori "Selamat atas kemenangannya, Amamiya-san. Akhir permainan yang sangat tidak terduga."
            chiasa "Hehe, makasih, Senpai. Tadi di tengah jalan aku cuma kebetulan nemu celahnya aja kok, lagi beruntung."
            shiori "Kebetulan dan keberuntungan, ya? Boleh aku menanyakan satu hal teknis? Pada giliran kedua puluh empat tadi, waktu aku pergi menuang teh, mengapa kamu tiba-tiba mengorbankan bidak perak di pojok kiri? Padahal dari langkah pertama sampai langkah kedua puluh, seluruh pola permainanmu adalah bertahan rapat, jauh berbeda dari pembukaan buku klasik pada lima langkah terakhirmu."
            chiasa "A-ah... yang di pojok kiri itu tadi cuma nebak aja kok, Senpai, siapa tahu bisa buka jalan di belakang."
            shiori "...Begitu. Tebakan mendadak yang persis sama dengan urutan buku panduan tingkat lanjut."
            nar "Shiori sama sekali tidak meninggikan suara ataupun menuduhmu melirik ponsel. Ia mulai memasukkan bidak-bidak kayu itu ke dalam kotaknya satu per satu, sementara senyum sopan di bibirnya tetap terpasang tanpa berubah sedikit pun sampai kamu pamit keluar dari ruang tatami."
        else:
            nar "Saat permainan memasuki pertengahan babak dan tekanan bidak Shiori mulai mengunci ruang gerakmu di kedua sisi, kamu sadar posisimu sudah hampir mustahil diselamatkan dengan cara biasa."
            nar "Ketika Shiori menoleh ke samping untuk mengambil teko teh hangat dari atas nampan, kamu melirik cepat layar ponsel yang tersembunyi di dekat lipatan lututmu, membaca urutan langkah balasan dari catatan strategi yang sudah terbuka di sana, lalu memindahkan bidakmu mengikuti pola tersebut."
            nar "Lima giliran kemudian, pertahanan raja Shiori jebol oleh rangkaian langkah yang berbalik tajam."
            yutaka "Menang juga akhirnya. Skakmat, Saionji-san."
            nar "Shiori menatap susunan akhir di atas papan kayu itu selama beberapa detik. Wajahnya tidak menunjukkan keterkejutan yang berlebihan; ia hanya memiringkan kepalanya sedikit lalu tersenyum sopan seperti biasa."
            shiori "Selamat, Kisaragi-san. Perubahan ritme permainan yang sangat mengejutkan di akhir babak."
            yutaka "Makasih, Saionji-san. Tadi aku cuma lagi hoki aja tiba-tiba lihat jalannya."
            shiori "Hoki, ya? Kalau begitu boleh aku bertanya satu hal? Pada langkah kedua puluh empat waktu aku sedang menuang teh tadi, kenapa kamu tiba-tiba mendorong bidak di pojok kiri dengan pola buku profesional? Padahal sepanjang dua puluh langkah sebelumnya, arah seranganmu sama sekali tidak menyiapkan formasi ke sana."
            yutaka "Ah... itu tadi cuma spekulasi aja daripada kejepit terus di tengah, kebetulan tembus."
            shiori "...Begitu. Spekulasi sesaat yang sangat presisi."
            nar "Ia tidak mendebat alasanmu lebih jauh dan langsung merapikan bidak-bidak kayu ke dalam kotak penyimpanan. Senyum sopan yang tidak berubah sedikit pun di wajahnya saat mengucapkan selamat malam membuat udara ruang tatami itu terasa jauh lebih dingin ketika kamu melangkah keluar."
    return

# ┌─ PANDUAN CERITA · S05 · Tojo Akihiro di Pesta
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : pewaris Tojo mendekatinya.
# │ INTI    : A lindungi / B abaikan / C manfaatkan.
# │ AKHIRAN : tojo_aktif.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S05:
    call kk_scene_enter("shiori", "Klub Catur · Tojo di pesta")
    if kk_host == "chiasa":
        nar "Aula resepsi di lantai atas gedung Klub Catur Distrik Elite malam itu terang oleh lampu gantung dan denting halus gelas minuman para tamu undangan. Kamu datang menemani Shiori yang sejak sore tadi sudah mengatakan hanya ingin hadir sebentar untuk memenuhi undangan tahunan pengurus klub dan para donatur."
        nar "Baru saja kalian berdua menepi ke dekat meja minuman dingin setelah menyapa ketua klub, seorang pemuda bertubuh jangkung dengan setelan jas biru gelap berpotongan mahal dan rambut disisir rapi melangkah membelah kerumunan menuju tempat kalian berdiri. Begitu pemuda itu mendekat, beberapa tamu dewasa di meja sebelah langsung memelankan suara mereka dan melirik ke arah Shiori dengan tatapan penuh arti."
        "Tojo" "Selamat malam, Saionji-san. Senang sekali akhirnya melihat Anda turun ke aula resepsi malam ini."
        shiori "Selamat malam, Tojo-san. Saya tidak menyangka Anda juga meluangkan waktu menghadiri acara ramah tamah klub catur universitas."
        "Tojo" "Tentu saja saya hadir. Apalagi setelah ayah saya memberi tahu bahwa Saionji Holdings juga ikut menjadi penyokong utama turnamen tahun ini. Dua keluarga kita memang selalu punya banyak agenda bersama untuk dibicarakan lebih dekat, bukan?"
        nar "Tojo Akihiro berbicara dengan nada ramah yang terlalu santai, gaya seseorang yang lingkungan sosialnya sudah begitu sering memasangkan namanya dengan keluarga Saionji hingga ia menganggap kedekatan mereka sebagai kesepakatan yang sudah selesai. Di sampingmu, Shiori hanya membalas dengan senyum formal yang datar."
        nar "Kamu tahu kedua orang tua Shiori di rumah tidak pernah memaksanya menerima perjodohan bisnis mana pun. Meski begitu, tatapan para relasi perusahaan yang mengelilingi meja jamuan membuat setiap kata penolakan di ruangan ini langsung menjadi tontonan banyak pasang mata."
        nar "Tojo kemudian menggeser pandangannya kepadamu, memperhatikan pakaianmu sekilas dari atas ke bawah sebelum tersenyum tipis."
        "Tojo" "...Dan gadis di sebelahmu ini siapa, Saionji-san? Adik kelas dari kampus?"
        shiori "Perkenalkan, ini Amamiya Chiasa-san, rekan saya dari Universitas Kouseikan."
        "Tojo" "Oh, mahasiswi tahun pertama rupanya. Maaf kalau saya menyela obrolan kalian ya, Amamiya-san. Boleh saya pinjam Saionji-san sebentar ke meja tengah? Ada beberapa direktur dari Tojo Group yang sejak tadi sudah menunggu ingin menyapa beliau secara langsung."
    else:
        nar "Aula resepsi lantai atas Klub Catur Distrik Elite malam itu dipenuhi tamu berjas rapi dan percakapan sopan para penyokong klub. Kamu datang menemani Shiori yang sejak berangkat dari kampus tadi hanya berniat mampir setengah jam untuk menghormati undangan pengurus."
        nar "Ketika kalian berdua baru saja mengambil gelas minuman di dekat meja jamuan samping, seorang pria muda berusia sekitar dua puluh empat tahun dengan setelan jas gelap mahal dan rambut tersisir klimis berjalan lurus menghampiri Shiori. Beberapa tamu di sekitar langsung menghentikan obrolan mereka dan memperhatikan keduanya dengan senyum penuh spekulasi."
        "Tojo" "Selamat malam, Saionji-san. Kebetulan yang sangat menyenangkan kita bisa bertemu lagi di resepsi malam ini."
        shiori "Selamat malam, Tojo-san. Saya tidak menduga Anda juga hadir di acara klub catur kampus."
        "Tojo" "Mustahil saya lewatkan kalau keluarga Saionji ikut menjadi sponsor utamanya. Lagipula, orang tua saya selalu bilang kita berdua harus lebih sering tampil dan berbincang di acara seperti ini, kan?"
        nar "Tojo Akihiro mengucapkannya dengan kepercayaan diri seseorang yang merasa dukungan gosip lingkungan bisnis sudah cukup untuk menempatkan Shiori di sisinya. Shiori sendiri hanya mempertahankan senyum sopannya tanpa mengiyakan kalimat tersebut."
        nar "Meskipun ayah dan ibu Shiori tidak pernah menekan putrinya soal pasangan, suasana aula yang penuh kolega bisnis membuat ruang gerak Shiori di dekat meja itu terasa sengaja disempitkan."
        nar "Tojo lalu menoleh ke arahmu, menakar setelanmu sekilas dengan senyum miring yang terbungkus kesopanan dan terasa merendahkan."
        "Tojo" "...Ngomong-ngomong, siapa temanmu ini, Saionji-san? Mahasiswa satu jurusan?"
        shiori "Ini Kisaragi Yutaka-san, teman seangkatan saya di Fakultas Ekonomi dan Bisnis."
        "Tojo" "Ah, teman kuliah rupanya. Maaf ya, Kisaragi-kun, boleh saya pinjam Saionji-san sebentar ke bagian depan? Ada beberapa kolega senior dari Tojo Group yang sudah menunggu ingin berbicara dengan beliau."
    call kk_family_menu("S05", ["\"Maaf, Tojo-san, kebetulan dia sudah lebih dulu janji bahas jadwal catur sama saya.\"", "\"Silakan dilanjutkan dulu, aku tunggu di dekat meja minuman ya.\"", "\"Wah, Tojo Group yang pegang proyek properti itu ya? Boleh kenalan lebih dekat?\""])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu tidak melangkah mundur seperti yang diharapkan Tojo. Sebaliknya, kamu bergeser setengah langkah lebih dekat ke samping Shiori dan menatap pria itu dengan senyum sopan yang tenang."
            chiasa "Maaf sekali, Tojo-san. Kebetulan sepuluh menit yang lalu Saionji-senpai sudah lebih dulu berjanji mau membahas susunan jadwal tanding klub catur minggu depan bersama saya di ruang sebelah. Waktunya agak mepet karena sebentar lagi kami harus pulang."
            nar "Senyum di wajah Tojo sempat tertahan. Alisnya terangkat tipis karena tidak terbiasa permintaannya dipotong begitu saja oleh seorang mahasiswi tahun pertama di depan para tamu."
            "Tojo" "Jadwal tanding catur kampus? Saya rasa urusan jadwal kegiatan mahasiswa bisa dibicarakan besok di kampus, sedangkan para direktur di meja depan—"
            shiori "Amamiya-san benar, Tojo-san. Saya memang sudah menyepakati janji lebih dulu dengannya sebelum Anda menghampiri meja ini, dan saya tidak terbiasa membatalkan janji yang sudah saya buat lebih awal. Tolong sampaikan salam hormat saya kepada rekan-rekan Anda di meja depan."
            nar "Begitu kamu membuka alasan di depan umum, Shiori langsung menguncinya dengan tata krama yang sama sekali tidak bisa dibantah Tojo tanpa membuat dirinya sendiri terlihat memaksa. Rahang Tojo mengeras sesaat, lalu ia mengangguk kaku dan berbalik meninggalkan kalian."
            nar "Setelah punggung pria berjas itu hilang di balik kerumunan tamu tengah, Shiori menoleh kepadamu. Sorot mata ungunya memancarkan rasa geli yang tulus."
            shiori "Kamu langsung pasang badan di depanku barusan, Amamiya-san. Berani sekali. Orang-orang di ruangan ini biasanya langsung menyingkir begitu mendengar nama Tojo Group disebut."
            chiasa "Habisnya cara dia ngajak tadi kayak nggak ngasih pilihan buat nolak, Saionji-senpai. Aku tadi nggak lancang kan ikut nyela?"
            shiori "Sama sekali tidak lancang. Sebenarnya aku bisa saja memotongnya sendiri, tapi kalau aku yang menolak langsung tanpa alasan pihak ketiga, bisik-bisik di ruangan ini bakal panjang sekali. Jujur saja, menyenangkan rasanya malam ini tidak harus menghadapi satu aula sendirian."
        else:
            nar "Kamu tidak bergeser menyingkir seperti yang diinginkan Tojo. Kamu justru melangkah setengah tapak lebih dekat ke sisi Shiori dan membalas tatapan pria itu dengan senyum santai yang tegas."
            yutaka "Maaf nih, Tojo-san, tapi kebetulan Saionji-san sudah lebih dulu punya janji sama saya buat merapikan jadwal pertandingan catur fakultas malam ini di ruang panitia. Waktunya agak sempit soalnya sebentar lagi kami sudah mau pamit."
            nar "Alis Tojo langsung terangkat tipis. Jelas sekali ia tidak terbiasa dihalangi secara terbuka oleh mahasiswa di acara yang disponsori perusahaannya."
            "Tojo" "Jadwal pertandingan fakultas? Bukankah urusan kampus seperti itu bisa kalian bahas besok siang? Rekan-rekan bisnis di meja depan itu—"
            shiori "Kisaragi-san mengatakan yang sebenarnya, Tojo-san. Saya sudah lebih dulu berjanji menyelesaikan urusan klub dengannya malam ini, dan tidak sopan rasanya kalau saya meninggalkan janji yang sudah dibuat lebih awal. Tolong sampaikan permohonan maaf dan salam saya kepada rekan-rekan Anda."
            nar "Karena kamu sudah lebih dulu membuka celah alasan, Shiori langsung menutup pembicaraan itu dengan sangat halus hingga Tojo tidak punya ruang untuk mendesak lagi di depan orang banyak. Pria itu mengangguk kaku dengan senyum tertahan, lalu melangkah pergi."
            nar "Begitu Tojo menjauh ke meja tengah, Shiori menoleh ke arahmu dengan senyum tipis yang tampak benar-benar terhibur."
            shiori "Kamu langsung berdiri memotong jalurnya barusan, Kisaragi-san. Langkah yang cukup berani. Tojo tidak terbiasa mendengar kata tidak dari mahasiswa."
            yutaka "Habisnya cara dia minta izin tadi terdengar kayak perintah yang nggak boleh ditolak, Saionji-san. Aku nggak kelewatan kan barusan?"
            shiori "Tidak sama sekali. Aku memang bisa menolaknya sendiri, tapi kalau kamu tidak membuka alasan jadwal tadi, aku harus menghabiskan lima belas menit lagi untuk meladeni basa-basinya di depan para tamu. Lega rasanya malam ini ada rekan yang sigap di sebelahku."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Merasa percakapan antar keluarga konglomerat itu bukan wilayah yang perlu kamu campuri, kamu mengangguk sopan kepada Tojo lalu melangkah mundur dua tapak ke samping meja jamuan."
            chiasa "Silakan dilanjutkan dulu obrolannya, Saionji-senpai. Aku tunggu sambil ambil minum di meja ujung sana ya."
            nar "Wajah Tojo langsung tampak puas melihatmu menyingkir tanpa perlawanan. Dari jarak beberapa langkah di dekat meja kudapan, kamu masih bisa mendengar percakapan mereka dengan cukup jelas."
            "Tojo" "Nah, akhirnya kita bisa bicara tanpa gangguan, Saionji-san. Hari Sabtu akhir bulan ini keluarga saya mengadakan jamuan makan malam tertutup di hotel pusat. Ayah saya dan para kolega sudah menanyakan kapan Anda akan hadir bersama saya."
            shiori "Saya menghargai undangan keluarga Anda, Tojo-san. Hanya saja jadwal kuliah dan agenda persiapan turnamen klub saya sudah terisi penuh sampai akhir bulan depan."
            "Tojo" "Ayolah, Saionji-san, kegiatan klub mahasiswa kan bisa ditinggal satu malam. Kita berdua sama-sama tahu hubungan antara keluarga kita jauh lebih penting untuk diprioritaskan sekarang."
            shiori "Ayah dan Ibu saya di rumah tidak pernah meminta saya meninggalkan tanggung jawab studi demi jamuan makan malam bisnis, Tojo-san. Kalau tidak ada lagi urusan terkait acara klub malam ini, saya permisi kembali ke teman saya."
            nar "Tojo terdiam kaku menerima penolakan dingin yang diucapkan dengan tata krama tanpa cela itu, sebelum akhirnya mengangguk singkat dan pergi. Saat Shiori berjalan kembali menghampirimu di meja minuman, ekspresi wajahnya sudah kembali tenang seperti semula."
            chiasa "Sudah selesai ngobrolnya, Saionji-senpai?"
            shiori "Sudah selesai. Kamu langsung melangkah mundur tadi waktu dia menyuruhmu pergi. Keputusan yang sangat wajar sih, karena itu memang bukan urusanmu."
            chiasa "Aku cuma takut salah ngomong kalau ikut campur urusan relasi keluarga Senpai."
            shiori "Aku mengerti kok, Amamiya-san. Hanya saja... aku memang punya kebiasaan selalu mencatat siapa yang memilih diam dan menyingkir ketika melihatku sedang disudutkan."
            nar "Shiori mengangkat gelas teh dinginnya dan menyesapnya pelan tanpa sedikit pun nada marah. Ia tetap mengobrol sopan denganmu sampai kalian keluar dari gedung klub, sambil memasang kembali batas jarak dengan sangat rapi."
        else:
            nar "Merasa urusan tarik-menarik antar keluarga bisnis besar itu bukan tempatmu untuk ikut campur, kamu mengangguk singkat kepada Tojo lalu mundur beberapa langkah menuju ujung meja minuman."
            yutaka "Silakan dilanjutkan dulu, Saionji-san. Aku tunggu di dekat meja sana ya."
            nar "Tojo tersenyum puas begitu melihatmu langsung menyingkir. Dari tempatmu berdiri beberapa meter di samping meja jamuan, suara percakapan mereka masih terdengar di sela riuh ruangan."
            "Tojo" "Akhirnya kita bisa bicara leluasa, Saionji-san. Akhir pekan depan orang tua saya mengadakan jamuan makan malam keluarga di restoran utama kami. Banyak relasi yang sudah menunggu kehadiran Anda di sana."
            shiori "Terima kasih atas undangannya, Tojo-san. Sayangnya jadwal kuliah dan turnamen resmi klub catur saya sudah padat sampai bulan depan."
            "Tojo" "Turnamen klub kampus kan bisa diwakilkan ke anggota lain, Saionji-san. Bukankah kita sama-sama paham acara mana yang lebih bernilai bagi masa depan kedua keluarga?"
            shiori "Orang tua saya tidak pernah menganggap komitmen saya di kampus sebagai hal yang bisa ditinggalkan demi jamuan bisnis, Tojo-san. Jika pembicaraan kita sudah selesai, saya permisi kembali ke teman saya."
            nar "Tojo tampak menahan kekesalannya selama dua detik sebelum mengangguk dingin dan berbalik pergi. Ketika Shiori melangkah kembali ke tempatmu berdiri, raut wajahnya tampak datar dan tak terusik."
            yutaka "Sudah beres urusannya sama dia, Saionji-san?"
            shiori "Sudah. Tadi kamu langsung menyingkir begitu dia meminta ruang. Langkah yang rasional sih, mengingat ini memang bukan masalahmu."
            yutaka "Aku cuma nggak mau sembarangan nyela urusan relasi keluargamu."
            shiori "Aku paham alasanmu, Kisaragi-san. Hanya saja... aku selalu mengingat dengan jelas siapa orang yang memilih mundur dan diam saat melihatku sedang terdesak di sudut."
            nar "Suaranya sama sekali tidak terdengar marah atau menyindir keras. Ia tetap menemanimu sampai acara selesai dengan sopan santun yang utuh, tetapi ada dinding kaca tipis yang kini berdiri jelas di antara kalian."
    else:
        if kk_host == "chiasa":
            nar "Begitu mendengar nama besar Tojo Group disebut langsung oleh pewarisnya, kamu justru memasang senyum paling ramahmu dan melangkah setengah tapak ke depan untuk menyapanya dengan antusias."
            chiasa "Wah, tunggu sebentar... Tojo-san ini dari Tojo Group yang membawahi jaringan galeri seni dan properti di distrik pusat itu ya? Kebetulan saya mahasiswi Fakultas Seni Rupa, saya sering banget baca liputan pameran di gedung milik perusahaan Anda. Senang sekali bisa berkenalan langsung!"
            nar "Tojo yang tadinya hendak mengajak Shiori pergi langsung menoleh kembali kepadamu dengan senyum bangga karena namanya dikenali."
            "Tojo" "Oh? Kamu mahasiswi Seni Rupa yang mengikuti proyek galeri kami rupanya? Selera pengamatanmu bagus juga, Amamiya-san. Kebetulan bulan depan kami memang sedang menyiapkan pembukaan pameran instalasi modern di lobi menara baru kami."
            chiasa "Serius, Tojo-san? Wah, kalau ada kesempatan, saya pengin banget bisa datang melihat kurasi pamerannya dari dekat."
            "Tojo" "Tentu saja bisa. Ini kartu nama pribadiku, hubungi saja nomor sekretarisku minggu depan nanti biar namamu dimasukkan ke daftar tamu undangan."
            chiasa "Terima kasih banyak, Tojo-san!"
            nar "Selama kamu bertukar basa-basi dan menerima kartu nama tersebut, Shiori berdiri diam sempurna di sebelahmu, memperhatikan setiap perubahan nada bicaramu sejak detik pertama tanpa berkedip. Tak lama kemudian, seorang kolega memanggil Tojo dari meja tengah sehingga ia berpamitan pergi. Begitu Tojo berbalik, senyum di bibir Shiori langsung menipis tajam."
            chiasa "Lumayan banget ya, Saionji-senpai. Selain dapat kenalan buat lihat pameran galeri, aku juga sekalian bantu ngalihin perhatian dia supaya nggak terus-terusan mendesak Senpai ke meja depan tadi."
            shiori "Kalau sejak awal tujuanmu datang ke acara ini memang untuk mencari koneksi dengan Tojo-san, kamu cukup mengatakannya terus terang kepadaku, Amamiya-san."
            chiasa "Eh? Bukan gitu maksudku, Senpai, aku tadi kan sekalian mau bantu memecah suasana—"
            shiori "Tolong jangan menggunakan posisi tidak nyamanku sebagai batu loncatan untuk kepentinganmu sendiri, lalu membungkusnya seolah kamu sedang menolongku. Aku sudah melihat ratusan orang memakai cara persis seperti itu di ruang resepsi keluarga sejak aku masih kecil."
            nar "Suara Shiori tetap rendah, lembut, dan sangat sopan di telinga orang yang lewat. Setiap katanya jatuh sedingin es hingga kamu tidak mampu melanjutkan alasanmu lagi."
        else:
            nar "Mendengar nama Tojo Group disebut langsung oleh pewarisnya, kamu justru mengeluarkan senyum paling luwesmu dan melangkah maju mengulurkan tangan lebih dulu kepada pria itu."
            yutaka "Tunggu sebentar, Tojo-san ini dari jajaran manajemen Tojo Group yang pegang proyek pengembangan properti pusat kota itu kan? Kebetulan saya mahasiswa Ekonomi dan Bisnis, kelompok diskusi kami baru saja membedah laporan ekspansi perusahaan Anda minggu lalu. Suatu kehormatan bisa kenal langsung."
            nar "Sikap Tojo yang tadinya ingin mengusirmu langsung berubah hangat karena merasa disanjung di depan Shiori. Ia menyambut jabatan tanganmu dengan dada membusung."
            "Tojo" "Oh? Mahasiswa Ekonomi Kouseikan yang mengikuti proyek properti kami rupanya? Mata bisnismu boleh juga, Kisaragi-kun. Bulan depan divisi pengembangan kami mengadakan seminar tertutup untuk mahasiswa terpilih dan investor muda."
            yutaka "Wah, kalau diperbolehkan hadir, saya tertarik sekali buat ikut menyimak langsung di forum itu, Tojo-san."
            "Tojo" "Mudah itu. Ini kartu namaku, kirimkan saja pesan ke staf kantorku minggu depan, nanti kupastikan namamu masuk daftar peserta."
            yutaka "Terima kasih banyak kesempatannya, Tojo-san."
            nar "Di sampingmu, Shiori berdiri hening sambil mengamati caramu menyimpan kartu nama Tojo ke dalam saku jas tanpa berkedip sedikit pun. Beberapa detik kemudian, seorang direktur memanggil Tojo ke meja utama sehingga ia pamit menyingkir. Begitu Tojo menjauh, senyum di wajah Shiori berubah sangat tipis."
            yutaka "Hasil yang lumayan kan, Saionji-san? Aku dapat akses seminar bisnis, sekaligus tadi berhasil ngulur waktu supaya kamu nggak jadi diseret ke meja kolega mereka."
            shiori "Kalau kamu memang membutuhkan perkenalan dengan pihak Tojo Group, seharusnya kamu meminta langsung kepadaku sejak awal, Kisaragi-san."
            yutaka "Lho, aku kan tadi sekalian bantu memecah perhatiannya dari kamu—"
            shiori "Jangan memanfaatkan situasi ketika aku sedang terdesak sebagai pintu masuk untuk urusan pribadimu, lalu menyebutnya sebagai bantuan untukku. Sejak kecil aku sudah terlalu hafal dengan orang-orang yang mendekat memakai dalih seperti itu."
            nar "Nada bicara Shiori tetap halus dan tidak menarik perhatian tamu di meja sebelah, tetapi ketajamannya langsung menutup seluruh ruang percakapan kalian malam itu."
    return

# ┌─ PANDUAN CERITA · S20 · Permainan Terakhir
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : shogi di vila.
# │ INTI    : A bertanding / B mengalah / C menolak.
# │ AKHIRAN : pesan tersirat.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S20:
    call kk_scene_enter("shiori", "Klub Catur · Permainan terakhir")
    nar "Shiori menyiapkan papan tanpa memulai. Yang berbeda adalah cara ia menunggu sampai kau benar-benar melihatnya."
    shiori "Satu pertandingan lagi. Aku ingin tahu apakah kita masih bisa saling mendengar. Kalau ada pesan yang tidak sampai lewat permainan, kita bicara sesudahnya."
    call kk_family_menu("S20", ["Bertanding sungguh-sungguh.", "Sengaja mengalah untuk membaca niatnya.", "Menolak bermain."])
    if _return == "A":
        shiori "Kau menjawab dengan permainan penuh. ...Pesanku sampai, dan kau membalas setara."
        nar "Kalian mengambil risiko yang dapat dibaca. Sesudahnya ia menyebut satu hal tentang hubungan kalian yang belum berani dikatakan sebelum pertandingan. Papan menjadi pembuka percakapan, bukan penggantinya."
    elif _return == "B":
        shiori "Kau mengalah? ...Kau pikir aku tidak akan sadar? Jangan hina aku dengan kemenangan murahan."
        nar "Ia menolak melanjutkan seolah hasil itu nyata. Keinginanmu membaca dirinya sambil menyembunyikan keseriusan sendiri terasa lebih merendahkan daripada kekalahan."
    else:
        nar "Kau menolak. Shiori menerima dan memasukkan bidak tanpa membanting."
        shiori "Baik. Aku tidak akan menyebutnya kesalahan karena menginginkan jawaban lain. Tapi malam ini aku juga tidak ingin mencari cara memulai pembicaraan lagi."
    return

# ┌─ PANDUAN CERITA · S21 · Pengumuman: Tojo
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : Tojo diumumkan sebagai calon tunangan.
# │ INTI    : A halangi / B dukung / C manfaatkan.
# │ AKHIRAN : Shiori memakai Tojo sebagai bidak.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S21:
    call kk_scene_enter("shiori", "Klub Catur · Pengumuman Tojo")
    nar "Tojo diumumkan sebagai calon tunangan dalam lingkungan yang terlalu cepat menyebut rencana sosial sebagai akhir bahagia. Shiori bisa membatalkannya dengan dukungan keluarga, tetapi justru mempertimbangkan manfaat mempertahankannya."
    shiori "Jangan kasihan. Aku punya pilihan. Yang sulit adalah memastikan aku tidak memilih sesuatu yang melukaiku hanya karena dapat kupakai melukai orang lain."
    call kk_family_menu("S21", ["Halangi pertunangan itu.", "Dukung langkahnya memakai Tojo.", "Manfaatkan situasi untuk dirimu."])
    if _return == "A":
        shiori "Kau mau menghalanginya untukku? ...Hati-hati. Menolong Saionji ada harganya."
        nar "Kau menanyakan apakah ia ingin berhenti sebelum bertindak. Shiori mengakui ada bagian rencana yang hanya dipertahankan agar ia tidak harus mengatakan betapa kecewanya."
    elif _return == "B":
        shiori "Kau mendukungku memainkan ini? ...Baik. Kita lihat siapa yang jadi raja di akhir papan."
        nar "Dukunganmu memudahkan ia membicarakan orang sebagai alat. Tojo memperoleh pengumuman; Shiori memperoleh akses. Keinginan benar-benar mengenal tidak lagi dianggap perlu."
    else:
        nar "Kau mencari keuntungan bagi dirimu. Shiori mendengarkan, lalu menanyakan apakah satu pun bagian rencanamu mempertimbangkan kehendaknya."
        nar "Ia tidak perlu melarangmu bergerak untuk mulai memperlakukanmu sebagai pihak yang harus diantisipasi."
    return

# ┌─ PANDUAN CERITA · S22 · Penghancuran Dimulai
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia bergerak.
# │ INTI    : A melawan / B mengaku / C lari.
# │ AKHIRAN : stage 5.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S22:
    call kk_scene_enter("shiori", "Klub Catur · Penghancuran dimulai")
    nar "Shiori meletakkan catatan peristiwa di meja, tidak cukup dekat untuk kauambil. Ada bagian yang segera kaukenali dan bagian yang menunjukkan selama ini ia jauh lebih banyak mendengar daripada yang terlihat."
    shiori "Aku meminta penjelasan. Beberapa kali. Sekarang aku berhenti menganggap menunggu sebagai kewajiban agar kamu tetap sempat menyusun cerita yang lebih nyaman."
    call kk_family_menu("S22", ["Melawan langkahnya.", "Mengaku semua yang kausembunyikan.", "Lari dari konfrontasi."])
    if _return == "A":
        shiori "Kau melawan? Bagus. Permainan yang menyerah terlalu dini membosankan."
        nar "Kau membantah dan mempertahankan tempatmu. Shiori tidak menjawab setiap serangan, cukup menunjukkan satu kontradiksi yang membuat pembelaan berikutnya sulit dimulai. Percakapan kini dibentuk keinginan menang, bukan pulih."
    elif _return == "B":
        shiori "Kau mengaku sekarang, saat sudah terdesak? ...Setidaknya itu langkah jujur yang pertama."
        nar "Ia meminta keterangan konkret, bukan janji semua akan baik. Kau menyebut perbuatan dan akibatnya, menanggung jeda ketika ia perlu berhenti mendengar. Kerusakan belum batal; satu kebohongan baru berhenti ditambahkan."
    else:
        nar "Kau pergi sebelum selesai. Shiori tidak menghalangi atau mengejar. Sesudahnya, kesempatan menjelaskan tidak lagi datang melalui undangan pribadi darinya."
        nar "Orang lain kini dapat menanyakan hal yang selama ini ia coba dengar langsung. Tak semuanya akan memberi kesabaran yang sama."
    return

# ┌─ PANDUAN CERITA · S23 · Turnamen Akhir
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia menang.
# │ INTI    : A hadir / B gagal / C mengganggu.
# │ AKHIRAN : reputasi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S23:
    call kk_scene_enter("shiori", "Klub Catur · Turnamen akhir")
    nar "Shiori melaju ke babak akhir turnamen. Keluarganya mengirim kabar bangga tanpa menjanjikan bahwa hasilnya akan menentukan nilai dirinya. Ia membacanya, tersenyum, lalu memusatkan diri pada permainan yang memang ingin dimenangkan."
    call kk_family_menu("S23", ["Hadir mendukungnya.", "Biarkan ia gagal tanpa dukungan.", "Ganggu konsentrasinya."])
    if _return == "A":
        shiori "Kamu datang. Aku senang. Itu tidak menjamin aku menang, tentu saja. Tapi aku ingin kamu melihat saat aku mencoba sungguh-sungguh."
        nar "Kau tetap menonton pada bagian lambat, tidak hanya datang untuk tepuk tangan. Sesudahnya ia menghampiri dengan satu keputusan yang ingin dibahas, lebih senang mendapat pendapatmu daripada pujian yang tidak memerhatikan permainan."
    elif _return == "B":
        nar "Tanpa satu wajah yang ia percaya di antara penonton, permainannya kehilangan satu derajat ketajaman."
        nar "Ia perlu waktu mengembalikan perhatian pada papan. Ketidakhadiranmu tidak boleh dijadikan penjelasan seluruh hasil, tetapi ia tetap merasakan kehilangan kecil di tempat yang semula berharap akan terisi."
    else:
        nar "Gangguanmu menarik perhatian petugas. Shiori menunggu persoalan ditangani sebelum melanjutkan, menahan marah yang tak ingin dibawa ke keputusan berikutnya."
        nar "Ia tetap menang. Sesudahnya, tidak ada keramahan pribadi yang bisa kaupanggil untuk mengecilkan perbuatan tersebut sebagai gurauan."
    return

# ┌─ PANDUAN CERITA · S24 · Natal: Skakmat
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : puncaknya.
# │ INTI    : A menyerah / B membalas / C menjadi sekutu.
# │ AKHIRAN : menentukan ending.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S24:
    call kk_scene_enter("shiori", "Klub Catur · Natal, skakmat")
    nar "Pada malam Natal itu Shiori tidak menyiapkan papan. Ia membicarakan akibat yang sudah bergerak dan bagian terakhir yang masih dapat diputuskan. Senyumnya tenang, matanya letih."
    shiori "Aku bisa terus menyebutnya permainan. Tetapi ada orang yang harus menjalani akibat sesudah kita selesai bicara. Jadi jawab sebagai dirimu sendiri. Apa yang kamu lakukan sekarang?"
    call kk_family_menu("S24", ["Menyerah dan terima kekalahan.", "Membalas dengan langkah terakhir.", "Ulurkan tangan untuk menjadi sekutu."])
    if _return == "A":
        shiori "Kau menyerah dengan tenang. ...Mungkin itu bentuk kejujuran yang paling akhir."
        nar "Kau menerima kekalahan tanpa memintanya menghiburmu. Shiori berhenti menjelaskan langkah berikutnya, seolah tak lagi perlu memastikan kau memahami siapa yang mengendalikan keadaan."
    elif _return == "B":
        shiori "Kau masih punya satu langkah? ...Tunjukkan. Aku ingin tahu apakah kau sepadan sampai akhir."
        nar "Kau membalas dengan keputusan yang bersedia diakui di depan pihak lain. Shiori memeriksa akibatnya sebelum menjawab. Pertarungan belum selesai, tetapi kali ini ia tidak bisa menutupinya sebagai kebohongan yang sama."
    else:
        shiori "Bersekutu? Setelah semua ini? ...Anehnya, itu langkah yang tidak kuperhitungkan. Dan justru karena itu, aku tertarik."
        nar "Ia tidak langsung menerima tanganmu. Ia menanyakan syarat, kebenaran yang masih disimpan, dan siapa yang dirugikan jika kalian hanya mencari musuh baru untuk melupakan urusan lama."
        nar "Kemungkinan kerja sama muncul di antara jawaban itu. Tak ada janji bahwa luka harus dilupakan agar kalian boleh berhenti menambahnya."
    return

init 1 python:
    _hook("S04-A", lambda: kk_adj("respek_shiori",5))
    _hook("S04-B", lambda: kk_adj("respek_shiori",8))
    _hook("S04-C", lambda: (kk_adj("daftar_kebohongan_shiori",1), kk_adj("marah_shiori",5)))
    _hook("S05-A", lambda: (kk_rel("shiori","trust",5), kk_flag("tojo_aktif"), kk_flag("shiori_dilindungi_tojo")))
    _hook("S05-B", lambda: (kk_flag("tojo_aktif"), kk_rel("shiori","trust",-3)))
    _hook("S05-C", lambda: (kk_flag("tojo_aktif"), kk_adj("marah_shiori",8)))
    _hook("S20-A", lambda: (kk_adj("respek_shiori",8), kk_flag("shiori_pesan_dibalas")))
    _hook("S20-B", lambda: (kk_adj("marah_shiori",10), kk_adj("respek_shiori",-8)))
    _hook("S20-C", lambda: kk_rel("shiori","trust",-5))
    _hook("S21-A", lambda: (kk_rel("shiori","trust",6), kk_flag("tojo_dihalangi")))
    _hook("S21-B", lambda: (kk_adj("respek_shiori",6), kk_flag("tojo_bidak")))
    _hook("S21-C", lambda: (kk_adj("marah_shiori",6), kk_flag("pemain_pakai_tojo")))
    _hook("S22-A", lambda: (kk_stage("shiori", max(5, stage.get("shiori",0))), kk_flag("shiori_dilawan")))
    _hook("S22-B", lambda: (kk_adj("daftar_kebohongan_shiori",-2), kk_flag("pemain_mengaku_terdesak")))
    _hook("S22-C", lambda: (kk_stage("shiori", max(5, stage.get("shiori",0))), kk_adj("marah_shiori",10)))
    _hook("S23-A", lambda: (kk_adj("respek_shiori",6), kk_flag("shiori_turnamen_didukung")))
    _hook("S23-B", lambda: kk_rel("shiori","aff",-4))
    _hook("S23-C", lambda: (kk_adj("marah_shiori",8), kk_adj("daftar_kebohongan_shiori",1)))
    _hook("S24-A", lambda: kk_flag("shiori_skakmat_menyerah"))
    _hook("S24-B", lambda: (kk_adj("respek_shiori",10), kk_flag("shiori_skakmat_dibalas")))
    _hook("S24-C", lambda: (kk_rel("shiori","intim",6), kk_flag("shiori_sekutu_akhir")))
