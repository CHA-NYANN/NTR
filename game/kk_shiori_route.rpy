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
        nar "Jarum jam dinding mendekati pukul sebelas malam ketika lantai bawah vila mulai hening. Lampu ruang makan sudah dipadamkan, menyisakan garis cahaya kuning hangat yang keluar dari celah pintu geser ruang tatami kecil di sisi timur beserta bunyi ketukan kayu yang jatuh teratur."
        nar "Saat kamu melongok dari balik pintu geser, Saionji Shiori tampak duduk bersimpuh seorang diri di atas bantal tatami menghadap papan shogi kayu. Ia mengenakan kardigan malam berwarna ungu gelap di atas pakaian santainya, dengan rambut putih keperakan yang jatuh rapi melewati bahu."
        nar "Ia baru saja menarik mundur dua bidak kayu ke petak sebelumnya, menatap sudut papan selama beberapa detik, lalu tersenyum tipis seorang diri."
        chiasa "Senpai belum tidur juga? Masih main shogi sendirian jam segini?"
        shiori "Selamat malam, Amamiya-san. Aku tidak sedang main babak baru, kok. Cuma menyusun ulang pertandingan di ruang klub kemarin sore."
        chiasa "Eh, Senpai sampai bawa papan shogi sendiri dari rumah ke vila pantai?"
        shiori "Fufu, bukan. Kebetulan papan ini memang punya pengelola vila, disimpan di lemari sudut itu. Bidaknya agak enteng sih, tapi lumayan enak dipakai."
        chiasa "Memangnya pertandingan kemarin di klub ada yang salah, Senpai? Bukannya Senpai menang?"
        shiori "Tadi waktu baru mau tidur di atas, tiba-tiba aku kepikiran langkahku di giliran ketiga puluh delapan. Aku terlalu cepat memajukan benteng."
        shiori "Biarpun menang karena lawan tidak sadar, langkah keliru tetap saja langkah keliru."
        chiasa "Padahal kemarin kan Senpai udah capek kuliah seharian sebelum ke klub."
        shiori "Mudah saja kalau mau menyalahkan rasa lelah. Tapi waktu memegang bidak itu kemarin, kepalaku sadar penuh kok. Aku paling tidak suka membela kesalahanku sendiri dengan alasan lunak."
        nar "Dengan gerakan jari yang cekatan dan terlatih, Shiori merapikan kembali seluruh bidak kayu itu ke dalam dua barisan awal yang berhadapan, lalu melirik bantal duduk kosong di seberang mejanya."
        shiori "Mumpung kamu belum ngantuk dan turun ke sini, mau main satu babak, Amamiya-san? Atau kamu sebenarnya cuma mampir karena sungkan langsung balik ke kamar?"
    else:
        nar "Mendekati pukul sebelas malam, lantai bawah vila sudah sepi setelah rombongan lain naik ke kamar masing-masing. Hanya cahaya lampu kuning dari ruang tatami samping yang masih menyala, diselingi bunyi ketukan jernih bidak kayu di atas papan."
        nar "Ketika kamu melongok melewati ambang pintu geser, Saionji Shiori sedang duduk sendirian di depan papan shogi. Ia baru saja memundurkan dua bidak kayu, menatap posisinya beberapa detik, lalu tersenyum tipis pada dirinya sendiri."
        yutaka "Belum tidur, Saionji-san? Jam segini masih betah aja ngutak-atik papan shogi?"
        shiori "Selamat malam, Kisaragi-san. Tadi aku mendadak kepikiran pertandingan di klub kemarin sore, jadi turun sebentar ke sini."
        yutaka "Lengkap juga fasilitas vila pantai ini sampai ada papan shogi."
        shiori "Disimpan di lemari dinding sebelah sana. Kemarin waktu giliran ketiga puluh delapan, langkahku di sayap kanan lumayan ceroboh."
        yutaka "Padahal di pertandingan itu kan kamu tetap menang."
        shiori "Menang karena lawan luput melihat celah bukan alasan buat membiarkan langkah buruk lewat begitu saja."
        shiori "Kalau mau beralasan capek kuliah sih gampang, tapi kemarin aku melakukannya dalam kondisi sadar penuh. Aku tidak suka membiasakan diri mencari alasan seperti itu."
        nar "Ia mengumpulkan bidak-bidak kayu itu dan menyusunnya kembali ke garis awal dengan gerakan rapi, lalu menatap bantal duduk kosong di seberangnya."
        shiori "Fufu, masih sanggup main satu babak malam ini, Kisaragi-san? Atau kamu sebenarnya sudah mengantuk?"
    call kk_family_menu("S04", ["\"Aku belum ngantuk kok. Ayo main, tapi kita batasi sampai tengah malam ya.\"", "Bermain fokus penuh untuk mengalahkannya secara jujur.", "Intip catatan strategi di ponselmu saat ia lengah."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu melangkah masuk ke ruang tatami dan duduk bersimpuh di atas bantal seberang papan shogi."
            chiasa "Aku belum ngantuk kok, Saionji-senpai. Ayo main satu babak, tapi kita batasi sampai tengah malam ya supaya besok pagi nggak bangun kesiangan."
            shiori "Syarat yang sangat masuk akal. Aku pegang janji waktunya. Silakan ambil langkah pembukanya, Amamiya-san."
            nar "Ruang tatami yang sunyi segera diisi bunyi ketukan kayu yang teratur. Kamu menggerakkan pion depan dengan tempo tenang, dan Shiori membalas tanpa tergesa-gesa. Ketika memasuki pertengahan babak, ia memajukan bidak perak untuk mengunci jalur sayap kananmu."
            chiasa "Wah, baru saja kupikir jalur kanan sudah aman, Senpai langsung menutupnya rapat sekali."
            shiori "Kamu membiarkan petak di sebelah kudamu kosong terlalu lama, Amamiya-san. Coba lihat barisan tengahmu, masih ada satu jalur tarik mundur yang cukup rapi."
            chiasa "Oh, yang ini ya? Kalau kugeser bidak emas ke sini berarti pertahanan kiriku tetap rapat."
            shiori "Pilihan yang tenang. Aku senang melihatmu tidak langsung panik waktu ditekan di pinggir papan."
            nar "Sambil menunggu giliran berikutnya, Shiori menuangkan sedikit teh panggang hangat dari termos kecil di samping meja ke dua cangkir rendah. Permainan terus berjalan akrab tanpa tekanan jam turnamen hingga jarum jam dinding di sudut ruangan tepat menyentuh angka dua belas malam."
            nar "Begitu mendengar bunyi detak jam yang samar, Shiori meletakkan bidak peraknya di petak pertahanan lalu mengangkat tangan memberi isyarat jeda."
            shiori "Sudah tepat tengah malam sesuai kesepakatan kita tadi. Ternyata kamu benar-benar tahan fokus sampai selarut ini ya, Amamiya-san. Kebanyakan orang kalau menemaniku bermain malam-malam sudah bolak-balik melirik jam sejak dua puluh menit pertama."
            chiasa "Habisnya lihat cara Senpai menutup celah di baris tengah tadi seru sekali, jadi nggak terasa waktunya jalan."
            shiori "Kalau begitu kita hentikan babaknya di posisi imbang ini. Aku jauh lebih menghargai lawan yang tahu kapan harus berhenti sesuai janjinya daripada orang yang memaksakan diri begadang hanya demi terlihat menyenangkan di depanku."
            chiasa "Sini, kubantu masukkan bidaknya ke kotak kayu, Senpai."
            shiori "Terima kasih, Amamiya-san. Besok pagi di kereta pulang kita masih bisa menyambung obrolan tanpa mata mengantuk."
            nar "Kalian berdua merapikan bidak-bidak shogi itu kembali ke dalam kotaknya, mematikan lampu ruang tatami, lalu naik bersama ke lantai dua yang sudah sunyi."
        else:
            nar "Kamu melangkah masuk ke ruang tatami dan duduk bersila di bantal seberang meja rendah tersebut."
            yutaka "Belum ngantuk kok, Saionji-san. Ayo main satu babak, tapi kita patok batas waktunya sampai tengah malam ya biar besok pagi nggak pusing."
            shiori "Kesepakatan yang adil. Silakan jalan duluan, Kisaragi-san."
            nar "Ketukan bidak kayu segera mengisi keheningan malam di bawah lampu kuning ruang tatami. Tidak ada yang bermain terburu-buru. Di tengah babak, Shiori memutar barisan perwiranya ke sayap kiri, memaksamu mengatur ulang pertahanan."
            yutaka "Cepat sekali kamu memindah beban serangan ke sisi kiri, Saionji-san. Tadi kukira kamu mau menembus dari tengah."
            shiori "Bagian tengahmu terlalu rapat untuk ditembus langsung, Kisaragi-san. Lebih efisien memancing bidak emasmu bergeser sedikit ke pinggir."
            yutaka "Berarti kalau kutukar pion di sini dulu, gerak bentengmu ikut tertahan kan?"
            shiori "Betul. Kamu membacanya dengan tenang tanpa terpancing terburu-buru."
            nar "Di sela giliran, Shiori menyodorkan cangkir teh hangat dari termos kecil di sebelah meja. Permainan mengalir santai sampai jarum jam dinding tepat menunjuk pukul dua belas malam. Shiori segera meletakkan bidak terakhirnya di sisi raja lalu merapikan duduknya."
            shiori "Sudah tepat tengah malam. Waktunya habis di pertengahan babak. Kamu benar-benar bertahan fokus sampai selarut ini ya, Kisaragi-san. Jarang ada teman kampus yang mau menemaniku di depan papan tanpa melirik jam setiap sepuluh menit."
            yutaka "Soalnya lihat cara kamu memutar pertahanan di sayap kiri tadi lumayan bikin penasaran."
            shiori "Kalau begitu kita akhiri malam ini di sini. Sudah waktunya istirahat, dan aku selalu lebih menyukai lawan bicara yang jujur menjaga batas waktunya daripada yang memaksakan diri sampai pagi hanya untuk menyenangkanku."
            yutaka "Oke, biar kubantu beresin bidak bagian sini ke kotaknya."
            shiori "Terima kasih, Kisaragi-san. Permainan yang sangat menyenangkan malam ini."
            nar "Kalian membereskan seluruh bidak kayu itu ke dalam kotak penyimpanan, memadamkan lampu ruangan, lalu kembali ke kamar masing-masing."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kamu duduk tegak di seberang meja rendah dan memusatkan seluruh perhatianmu pada susunan bidak kayu di depan mata. Sejak langkah pembuka, kamu menjaga baris pertahananmu tetap rapat sambil menunggu Shiori mengambil inisiatif serangan."
            shiori "Hmm... pembukaan pertahananmu malam ini jauh lebih rapi daripada waktu kita latihan ringan dulu, Amamiya-san. Kamu sedang bermain serius rupanya."
            chiasa "Sekali-sekali aku juga pengin lihat seberapa jauh aku bisa mengimbangi Saionji-senpai tanpa minta kelonggaran."
            shiori "Kalau begitu aku juga tidak akan menahan langkahku."
            nar "Memasuki pertengahan babak, Shiori mendorong perwira kudanya cukup jauh di sisi kanan untuk membongkar bentengmu. Serangan agresif itu menyisakan satu petak kosong di depan barisan tengahnya. Tanpa membuang satu giliran pun, kamu langsung menjatuhkan bidak gajah cadanganmu tepat ke jantung pertahanannya."
            shiori "Oh... kamu menunggu kudaku naik ke baris keempat baru menjatuhkan gajah di situ."
            chiasa "Soalnya kalau kuturunkan satu giliran lebih awal, Senpai masih sempat menutup pakai bidak emas."
            nar "Empat langkah ketat menyusul dengan bunyi ketukan kayu yang makin cepat, sampai akhirnya bidak terakhirmu mendarat bersih mengunci sudut raja lawan."
            chiasa "Skakmat, Saionji-senpai."
            nar "Shiori terdiam menatap papan selama tiga detik penuh. Matanya menyusuri kembali petak-petak di sekeliling rajanya untuk memeriksa apakah masih ada jalur lolos, lalu ia mengangkat wajah dengan sorot mata ungu yang berbinar terang."
            shiori "...Skakmat yang sangat bersih. Kamu benar-benar mengalahkanku malam ini, Amamiya-san. Bagus sekali. Aku paling tidak tahan kalau harus menang melawan orang yang menahan kemampuannya."
            chiasa "Jantungku juga berdebar kencang tadi, Senpai. Kalau Senpai sempat tarik mundur bidak emasnya satu langkah aja tadi, pertahanan kiriku yang bakal jebol duluan."
            nar "Shiori mencondongkan tubuhnya sedikit ke atas papan, menunjuk petak tempat ia memajukan kudanya tadi sambil tertawa kecil."
            shiori "Lucunya, justru langkah serangan kuda yang paling kuyakini bakal menembus baris belakangmu tadi yang malah membuka pintu masuk untuk gajahmu. Coba kita mundurkan empat langkah sebentar. Sejak giliran ke berapa kamu sudah menyiapkan umpan di petak tengah itu?"
            chiasa "Sejak tiga giliran sebelumnya, waktu Senpai menggeser benteng ke jalur pinggir."
            shiori "Berarti kamu sudah membacanya sejak awal pertukaran bidak tadi. Menarik sekali. Ayo kita bedah langkah itu lima menit lagi sebelum naik ke kamar."
            chiasa "Ayo, Senpai. Aku juga penasaran kalau tadi Senpai balik menyerang dari kiri jadinya gimana."
            shiori "Kalau aku memaksa masuk dari sisi kiri tadi, bentengmu yang masih diam di pojok bawah justru bakal langsung menguasai lajur tengah."
            chiasa "Wah, cepat sekali Senpai menghitung cabang langkahnya di luar kepala."
            nar "Kalian berdua memundurkan beberapa bidak kayu di atas papan dan mendiskusikan variasi langkah tersebut dengan hangat sebelum akhirnya merapikan meja ruang tatami."
        else:
            nar "Kamu duduk bersila di seberang papan dan langsung bermain dengan fokus penuh sejak giliran pertama. Kamu membiarkan Shiori menekan lebih dulu dari sayap kanan, sambil perlahan mengumpulkan bidak cadangan di tanganmu."
            shiori "Pembukaanmu malam ini jauh lebih disiplin, Kisaragi-san. Kelihatannya kamu tidak berniat sekadar menemani."
            yutaka "Kalau main setengah-setengah lawan kamu kan percuma, Saionji-san. Sekalian aja kuhabiskan fokusku di papan ini."
            shiori "Bagus. Kalau begitu aku juga bermain dengan kecepatan penuh."
            nar "Di pertengahan permainan, Shiori mendorong bentengnya terlalu dalam untuk mengepung sisi rajamu, meninggalkan satu celah sempit di jalur diagonal tengah. Kamu langsung memanfaatkan giliran itu dengan menjatuhkan bidak gajah tepat di titik buta pertahanannya."
            shiori "Begitu rupanya... kamu sengaja membiarkan bentengku masuk sedalam itu supaya jalur diagonalnya terbuka."
            yutaka "Satu-satunya cara biar rajamu nggak sempat geser ke samping."
            nar "Beberapa pertukaran cepat terjadi sebelum bidak penutupmu jatuh di atas papan dengan bunyi klik yang tegas."
            yutaka "Skakmat, Saionji-san."
            nar "Shiori menatap papan shogi itu tanpa berkedip selama beberapa detik, memeriksa ulang setiap petak di sekitar rajanya, sebelum akhirnya mendongak menatapmu dengan sorot mata yang berbinar hidup."
            shiori "...Luar biasa bersih. Kamu sungguh mengalahkanku tanpa celah malam ini, Kisaragi-san. Aku senang sekali, karena tidak ada yang lebih membosankan daripada lawan yang diam-diam mengalah."
            yutaka "Tipis sekali itu tadi. Kalau serangan bentengmu di sisi kiriku tadi nggak kupotong pakai gajah, dua langkah lagi pasti aku yang kalah."
            nar "Shiori mencondongkan badan ke arah papan, menyentuh bidak bentengnya sendiri yang terlalu maju tadi lalu tertawa pelan."
            shiori "Justru langkah benteng yang paling kuandalkan untuk menutup pergerakanmu tadi yang malah jadi titik runtuhnya pertahananku sendiri. Coba kita tarik mundur tiga giliran. Sejak kapan kamu sengaja mengosongkan petak tengah itu buat memancing bentengku naik?"
            yutaka "Sejak kamu makan pionku di baris keempat tadi. Kelihatan kalau kamu lagi buru-buru mau buka jalur kanan."
            shiori "Bacaan yang tajam. Ayo kita ulas posisi tengah ini sebentar sebelum tidur, aku belum rela naik ke kamar sebelum paham penuh jebakanmu barusan."
            yutaka "Boleh, tapi cuma lima menit ya sebelum kita sama-sama ketiduran di tatami."
            shiori "Lima menit sudah lebih dari cukup untuk membongkar tiga langkah terakhirmu itu, Kisaragi-san."
            yutaka "Silakan, coba tunjukkan kalau memang masih ada celah buat rajamu lolos tadi."
            nar "Shiori menggeser kembali empat bidak kayu ke posisi tengah dan mengulas jalannya permainan bersama-sama dengan antusiasme tulus yang jarang ia perlihatkan di kampus."
    else:
        if kk_host == "chiasa":
            nar "Ketika permainan memasuki babak tengah dan susunan bidak Shiori mulai mengepung sisi kirimu rapat-rapat, kamu tahu kamu akan kalah jika terus mengandalkan hitunganmu sendiri."
            shiori "Posisi sayap kirimu mulai sempit, Amamiya-san. Tunggu sebentar, aku ambilkan teh hangat di meja samping dulu supaya tenggorokan tidak kering sambil kamu memikirkan langkah berikutnya."
            chiasa "Iya, silakan, Senpai."
            nar "Tepat saat Shiori memutar tubuhnya untuk meraih teko teh di meja samping dan menuang air hangat ke cangkirnya, kamu diam-diam menyalakan layar ponsel yang tergeletak di atas pangkuanmu. Kamu mengintip diagram penyelesaian shogi dari aplikasi strategi yang tadi sempat kamu buka, lalu menghafal tiga urutan langkah jitu tersebut sebelum layar mati."
            nar "Begitu Shiori kembali duduk, kamu langsung mengorbankan bidak perak di pojok kiri lalu mendorong rentetan serangan yang sama sekali berbeda dari gaya bermainmu sejak awal. Lima giliran sesudahnya, barisan pertahanan Shiori runtuh."
            chiasa "Ah... masuk juga akhirnya. Skakmat, Saionji-senpai."
            nar "Shiori tidak langsung menyentuh bidaknya. Ia menatap rangkaian langkah di sudut kiri papan itu selama beberapa detik dengan raut wajah yang tetap tenang, lalu mengangkat pandangannya dan tersenyum sopan."
            shiori "Selamat atas kemenangannya, Amamiya-san. Akhir permainan yang sangat tidak terduga."
            chiasa "Hehe, makasih, Senpai. Tadi di tengah jalan aku cuma kebetulan nemu celahnya aja kok, lagi beruntung."
            shiori "Kebetulan dan keberuntungan, ya? Boleh aku menanyakan satu hal teknis?"
            chiasa "Eh, boleh aja, Senpai. Bagian mana?"
            shiori "Pada giliran kedua puluh empat tadi, tepat waktu aku berpaling menuang teh, mengapa kamu tiba-tiba mengorbankan bidak perak di pojok kiri? Padahal dari langkah pertama sampai langkah kedua puluh, seluruh pola permainanmu adalah bertahan rapat, jauh berbeda dari kombinasi buku klasik tingkat lanjut pada lima langkah terakhirmu."
            chiasa "A-ah... yang di pojok kiri itu tadi cuma nebak aja kok, Senpai. Aku pikir daripada kejepit terus, siapa tahu bisa buka jalan di belakang."
            shiori "...Begitu. Tebakan mendadak yang persis sama dengan urutan buku panduan tingkat lanjut, bahkan sampai jeda pion pendukungnya."
            chiasa "Mungkin kebetulan aja pernah kebaca sekilas dulu, Senpai..."
            shiori "Tentu saja. Kebetulan memang hal yang menarik."
            chiasa "Kalau begitu... aku bantu bereskan bidaknya sekarang ya, Senpai, sudah lewat tengah malam juga."
            shiori "Tidak usah, Amamiya-san. Biar aku sendiri yang merapikan papan ini, kamu boleh naik lebih dulu ke kamar atas."
            chiasa "Eh, beneran nggak apa-apa ditinggal bereskan sendiri, Senpai?"
            shiori "Tidak masalah sama sekali. Selamat beristirahat, Amamiya-san."
            nar "Shiori sama sekali tidak meninggikan suara ataupun menuduhmu melirik ponsel. Ia mulai memasukkan bidak-bidak kayu itu ke dalam kotaknya satu per satu, sementara senyum sopan di bibirnya tetap terpasang tanpa berubah sedikit pun sampai kamu pamit keluar dari ruang tatami."
        else:
            nar "Saat permainan memasuki pertengahan babak dan tekanan bidak Shiori mulai mengunci ruang gerakmu di kedua sisi, kamu sadar posisimu sudah hampir mustahil diselamatkan dengan cara biasa."
            shiori "Langkahmu di sisi kiri hampir tertutup rapat, Kisaragi-san. Sebentar, aku tuangkan teh hangat dari nampan sebelah dulu selagi kamu mempertimbangkan giliran berikutnya."
            yutaka "Oke, santai saja, Saionji-san."
            nar "Ketika Shiori menoleh ke samping untuk mengambil teko teh hangat, kamu melirik cepat layar ponsel yang tersembunyi di dekat lipatan lututmu, membaca urutan langkah balasan dari catatan strategi yang sudah terbuka di sana, lalu segera memadamkan layarnya kembali."
            nar "Begitu Shiori kembali menghadap papan, kamu langsung mendorong serangan tajam di pojok kiri yang membalik arah permainan sepenuhnya. Lima giliran kemudian, pertahanan raja Shiori jebol."
            yutaka "Menang juga akhirnya. Skakmat, Saionji-san."
            nar "Shiori menatap susunan akhir di atas papan kayu itu selama beberapa detik. Wajahnya tidak menunjukkan keterkejutan yang berlebihan. Ia hanya memiringkan kepalanya sedikit lalu tersenyum sopan seperti biasa."
            shiori "Selamat, Kisaragi-san. Perubahan ritme permainan yang sangat mengejutkan di akhir babak."
            yutaka "Makasih, Saionji-san. Tadi aku cuma lagi beruntung aja tiba-tiba lihat jalannya."
            shiori "Beruntung, ya? Kalau begitu boleh aku bertanya satu hal?"
            yutaka "Tanya apa?"
            shiori "Pada langkah kedua puluh empat tepat waktu aku sedang menuang teh tadi, kenapa kamu tiba-tiba mendorong bidak di pojok kiri dengan pola buku profesional? Padahal sepanjang dua puluh langkah sebelumnya, arah seranganmu sama sekali tidak menyiapkan formasi ke sana."
            yutaka "Ah... itu tadi cuma spekulasi aja daripada kejepit terus di tengah, kebetulan tembus."
            shiori "...Begitu. Spekulasi sesaat yang sangat presisi, sampai ke urutan pion penutupnya."
            yutaka "Namanya juga lagi tepat saja instingnya malam ini."
            shiori "Memang menakjubkan sekali insting seperti itu."
            yutaka "Sini kubantu masukkan bidaknya ke kotak kayu sebelum kita naik ke kamar."
            shiori "Tidak perlu repot, Kisaragi-san. Aku biasa merapikan urutan bidaknya sendiri sebelum menutup papan, jadi silakan naik beristirahat lebih dulu."
            yutaka "Oke, kalau begitu aku naik duluan ya. Selamat malam, Saionji-san."
            shiori "Selamat malam, Kisaragi-san."
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
        nar "Aula resepsi di lantai atas gedung Klub Catur Distrik Elite terang oleh lampu gantung kristal dan denting halus gelas minuman para tamu undangan. Kamu datang menemani Shiori yang sejak berangkat sudah mengatakan hanya ingin hadir sebentar untuk memenuhi undangan tahunan pengurus klub dan para donatur."
        chiasa "Ramai sekali ya tamunya, Saionji-senpai. Hampir semua yang di meja tengah kelihatannya dari kalangan perusahaan."
        shiori "Begitulah acara ramah tamah donatur klub setiap tahun, Amamiya-san. Mereka datang membawa kartu nama, saling memuji perkembangan turnamen, lalu membicarakan kerja sama di luar catur."
        chiasa "Senpai kelihatan sudah hafal betul alur acaranya."
        shiori "Sejak SMA aku sudah ikut menghadiri jamuan serupa bersama keluargaku. Kita cukup menyapa ketua klub, mengambil segelas teh dingin di tepi ruangan, lalu pamit setelah tiga puluh menit."
        chiasa "Rencana yang rapi sekali. Kalau begitu biar kuambilkan teh dinginnya sekalian, Senpai mau yang tawar atau pakai perasan lemon?"
        shiori "Yang tawar saja, terima kasih."
        nar "Baru saja kalian berdua menepi ke dekat meja minuman dingin setelah menyapa ketua klub, seorang pemuda bertubuh jangkung dengan setelan jas biru gelap berpotongan mahal dan rambut disisir rapi melangkah membelah kerumunan menuju tempat kalian berdiri. Begitu pemuda itu mendekat, beberapa tamu dewasa di meja sebelah langsung memelankan suara mereka dan melirik ke arah Shiori dengan tatapan penuh arti."
        "Tojo" "Selamat malam, Saionji-san. Senang sekali akhirnya melihat Anda turun ke aula resepsi."
        shiori "Selamat malam, Tojo-san. Saya tidak menyangka Anda juga meluangkan waktu menghadiri acara ramah tamah klub catur universitas."
        "Tojo" "Tentu saja saya hadir. Apalagi setelah ayah saya memberi tahu bahwa Saionji Holdings juga ikut menjadi penyokong utama turnamen tahun ini. Dua keluarga kita memang selalu punya banyak agenda bersama untuk dibicarakan lebih dekat, kan?"
        shiori "Urusan sponsor turnamen sepenuhnya ditangani bagian humas kantor ayah saya dan pengurus klub, Tojo-san. Saya hadir malam ini hanya sebagai anggota aktif klub."
        "Tojo" "Haha, rendah hati sekali seperti biasa. Tetap saja, para tamu di ruangan ini semua tahu siapa Anda."
        nar "Tojo Akihiro berbicara dengan nada ramah yang terlalu santai, gaya seseorang yang lingkungan sosialnya sudah begitu sering memasangkan namanya dengan keluarga Saionji hingga ia menganggap kedekatan mereka sebagai kesepakatan yang sudah selesai. Di sampingmu, Shiori hanya membalas dengan senyum formal yang datar."
        nar "Kamu tahu kedua orang tua Shiori di rumah tidak pernah memaksanya menerima perjodohan bisnis mana pun. Meski begitu, tatapan para relasi perusahaan yang mengelilingi meja jamuan membuat setiap kata penolakan di ruangan ini langsung menjadi tontonan banyak pasang mata."
        nar "Tojo kemudian menggeser pandangannya kepadamu, memperhatikan pakaianmu sekilas dari atas ke bawah sebelum tersenyum tipis."
        "Tojo" "...Dan gadis di sebelahmu ini siapa, Saionji-san? Adik kelas dari kampus?"
        shiori "Perkenalkan, ini Amamiya Chiasa-san, rekan saya dari Universitas Kouseikan."
        "Tojo" "Oh, mahasiswi tahun pertama rupanya. Maaf kalau saya menyela obrolan kalian ya, Amamiya-san. Boleh saya pinjam Saionji-san sebentar ke meja tengah? Ada beberapa direktur dari Tojo Group yang sejak tadi sudah menunggu ingin menyapa beliau secara langsung."
    else:
        nar "Aula resepsi lantai atas Klub Catur Distrik Elite dipenuhi tamu berjas rapi dan percakapan sopan para penyokong klub di bawah lampu gantung yang terang. Kamu datang menemani Shiori yang sejak berangkat dari kampus tadi hanya berniat mampir setengah jam untuk menghormati undangan pengurus."
        yutaka "Suasananya jauh lebih kaku daripada ruang tanding di lantai bawah ya, Saionji-san."
        shiori "Karena separuh tamu di sini datang untuk membicarakan sponsor daripada langkah pembukaan catur, Kisaragi-san. Di lantai bawah tidak ada orang yang bertanya perusahaan mana yang membiayai papan caturnya."
        yutaka "Bener juga. Jadi kita cukup bertahan berapa lama di atas sini?"
        shiori "Tiga puluh menit sudah cukup sopan. Kita ambil minuman sebentar, sapa ketua klub, lalu bisa segera pulang."
        yutaka "Kedengarannya rencana yang sangat aman. Mau kuambilkan teh dingin atau air mineral?"
        shiori "Teh dingin tawar saja, terima kasih."
        nar "Ketika kalian berdua baru saja mengambil gelas minuman di dekat meja jamuan samping, seorang pria muda berusia sekitar dua puluh empat tahun dengan setelan jas gelap mahal dan rambut tersisir klimis berjalan lurus menghampiri Shiori. Beberapa tamu di sekitar langsung menghentikan obrolan mereka dan memperhatikan keduanya dengan senyum penuh spekulasi."
        "Tojo" "Selamat malam, Saionji-san. Kebetulan yang sangat menyenangkan kita bisa bertemu lagi di resepsi ini."
        shiori "Selamat malam, Tojo-san. Saya tidak menduga Anda juga hadir di acara klub catur kampus."
        "Tojo" "Mustahil saya lewatkan kalau keluarga Saionji ikut menjadi sponsor utamanya. Lagipula, orang tua saya selalu bilang kita berdua harus lebih sering tampil dan berbincang di acara seperti ini, kan?"
        shiori "Sponsor klub diurus langsung oleh bagian humas perusahaan ayah saya, Tojo-san. Kehadiran saya malam ini murni sebagai anggota klub."
        "Tojo" "Ah, jangan terlalu formal begitu, Saionji-san. Semua relasi di aula ini toh tahu hubungan baik keluarga kita."
        nar "Tojo Akihiro mengucapkannya dengan kepercayaan diri seseorang yang merasa dukungan gosip lingkungan bisnis sudah cukup untuk menempatkan Shiori di sisinya. Shiori sendiri hanya mempertahankan senyum sopannya tanpa mengiyakan kalimat tersebut."
        nar "Meskipun ayah dan ibu Shiori tidak pernah menekan putrinya soal pasangan, suasana aula yang penuh kolega bisnis membuat ruang gerak Shiori di dekat meja itu terasa sengaja disempitkan."
        nar "Tojo lalu menoleh ke arahmu, menakar setelanmu sekilas dengan senyum miring yang terbungkus kesopanan dan terasa merendahkan."
        "Tojo" "...Ngomong-ngomong, siapa temanmu ini, Saionji-san? Mahasiswa satu angkatan?"
        shiori "Ini Kisaragi Yutaka-san, teman seangkatan saya di Fakultas Ekonomi dan Bisnis."
        "Tojo" "Ah, teman kuliah rupanya. Maaf ya, Kisaragi-kun, boleh saya pinjam Saionji-san sebentar ke bagian depan? Ada beberapa kolega senior dari Tojo Group yang sudah menunggu ingin berbicara dengan beliau."
    call kk_family_menu("S05", ["\"Maaf, Tojo-san, kebetulan dia sudah lebih dulu janji bahas jadwal catur sama saya.\"", "\"Silakan dilanjutkan dulu, aku tunggu di dekat meja minuman ya.\"", "\"Wah, Tojo Group yang pegang proyek properti itu ya? Boleh kenalan lebih dekat?\""])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu tidak melangkah mundur seperti yang diharapkan Tojo. Sebaliknya, kamu bergeser setengah langkah lebih dekat ke samping Shiori dan menatap pria itu dengan senyum sopan yang tenang."
            chiasa "Maaf sekali, Tojo-san. Kebetulan sepuluh menit yang lalu Saionji-senpai sudah lebih dulu berjanji mau membahas susunan jadwal tanding klub catur minggu depan bersama saya di ruang sebelah. Waktunya agak mepet karena sebentar lagi kami harus pulang."
            nar "Senyum di wajah Tojo sempat tertahan. Alisnya terangkat tipis karena tidak terbiasa permintaannya dipotong begitu saja oleh seorang mahasiswi tahun pertama di depan para tamu."
            "Tojo" "Jadwal tanding catur kampus? Saya rasa urusan jadwal kegiatan mahasiswa bisa dibicarakan besok di kampus, sedangkan para direktur di meja depan..."
            shiori "Amamiya-san benar, Tojo-san. Saya memang sudah menyepakati janji lebih dulu dengannya sebelum Anda menghampiri meja ini, dan saya tidak terbiasa membatalkan janji yang sudah saya buat lebih awal. Tolong sampaikan salam hormat saya kepada rekan-rekan Anda di meja depan."
            nar "Begitu kamu membuka alasan di depan umum, Shiori langsung menguncinya dengan tata krama yang sama sekali tidak bisa dibantah Tojo tanpa membuat dirinya sendiri terlihat memaksa. Rahang Tojo mengeras sesaat, lalu ia mengangguk kaku dan berbalik meninggalkan kalian."
            "Tojo" "Baiklah kalau begitu. Lain kali semoga jadwal kita lebih cocok, Saionji-san."
            nar "Setelah punggung pria berjas itu hilang di balik kerumunan tamu tengah, Shiori menoleh kepadamu. Sorot matanya memancarkan rasa geli yang tulus."
            shiori "Fufu... Kamu langsung pasang badan di depanku barusan, Amamiya-san. Berani sekali."
            shiori "Biasanya orang-orang di ruangan ini langsung menyingkir begitu mendengar marga Tojo disebut."
            chiasa "Habis cara dia ngajak tadi maksa banget sih, Senpai. Eh, aku tadi nggak lancang kan ikut nyela?"
            shiori "Sama sekali tidak. Sebenarnya aku bisa saja memotongnya sendiri, tapi kalau aku yang menolak tanpa alasan orang ketiga, bisik-bisik di aula ini bakal panjang."
            shiori "Jujur saja, menyenangkan rasanya malam ini tidak harus menghadapi mereka sendirian."
            chiasa "Hehehe, syukurlah. Kalau gitu ayo kita pindah ke ruang sebelah sekarang biar alasan jadwal catur tadi kelihatan beneran!"
            shiori "Langkah penutup yang rapi. Ayo."
            chiasa "Di ruang sebelah juga jauh lebih tenang buat ngabisin teh dingin kita sebelum pulang."
            shiori "Setuju. Di sana juga ada papan catur kayu kalau kamu mau lihat satu teka-teki pembukaan sebentar."
            nar "Shiori melangkah berdampingan denganmu meninggalkan aula resepsi yang bising dengan senyum ringan yang tampak jauh lebih santai."
        else:
            nar "Kamu tidak bergeser menyingkir seperti yang diinginkan Tojo. Kamu justru melangkah setengah tapak lebih dekat ke sisi Shiori dan membalas tatapan pria itu dengan senyum santai yang tegas."
            yutaka "Maaf nih, Tojo-san, tapi kebetulan Saionji-san sudah lebih dulu janji sama saya buat ngerapiin jadwal tanding klub di ruang panitia. Waktunya agak mepet soalnya sebentar lagi kami sudah mau pamit."
            nar "Alis Tojo langsung terangkat tipis. Jelas sekali ia tidak terbiasa dihalangi secara terbuka oleh mahasiswa di acara yang disponsori perusahaannya."
            "Tojo" "Jadwal pertandingan fakultas? Bukankah urusan kampus seperti itu bisa kalian bahas besok siang? Rekan-rekan bisnis di meja depan itu..."
            shiori "Kisaragi-san benar, Tojo-san. Saya sudah berjanji lebih dulu dengannya hari ini, dan saya tidak suka membatalkan janji yang sudah dibuat lebih awal. Tolong sampaikan salam saya untuk rekan-rekan Anda."
            nar "Karena kamu sudah lebih dulu membuka celah alasan, Shiori langsung menutup pembicaraan itu dengan sangat halus hingga Tojo tidak punya ruang untuk mendesak lagi di depan orang banyak. Pria itu mengangguk kaku dengan senyum tertahan."
            "Tojo" "Baiklah. Selamat melanjutkan urusan kampus kalian kalau begitu."
            nar "Begitu Tojo menjauh ke meja tengah, Shiori menoleh ke arahmu dengan senyum tipis yang tampak benar-benar terhibur."
            shiori "Fufu, kamu langsung memotong jalannya barusan, Kisaragi-san. Cukup berani juga. Dia tidak terbiasa mendengar penolakan dari mahasiswa."
            yutaka "Habis cara dia minta izin tadi udah kayak ngasih perintah aja. Aku nggak kelewatan kan barusan?"
            shiori "Tidak sama sekali. Kalau kamu tidak membuka alasan jadwal tadi, aku pasti harus buang waktu lima belas menit lagi buat meladeni basa-basinya di depan para tamu."
            shiori "Lega rasanya ada rekan yang sigap di sebelahku."
            yutaka "Ayo sekalian geser ke ruang panitia sebelah biar nggak disamperin gelombang kedua dari meja tengah."
            shiori "Saran yang cerdas. Mari."
            yutaka "Habis minum teh dingin di ruang sebelah, kita bisa langsung turun lewat tangga samping tanpa harus muter balik ke aula ini lagi."
            shiori "Kamu bahkan sudah memetakan jalur keluarnya. Efisien sekali, Kisaragi-san."
            nar "Shiori membawa gelas teh dinginnya dan berjalan sejajar di sampingmu menuju pintu samping dengan raut wajah yang tampak jauh lebih tenang."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Merasa percakapan antar keluarga konglomerat itu bukan wilayah yang perlu kamu campuri, kamu mengangguk sopan kepada Tojo lalu melangkah mundur dua tapak ke samping meja jamuan."
            chiasa "Silakan dilanjutkan dulu obrolannya, Saionji-senpai. Aku tunggu sambil ambil minum di meja ujung sana ya."
            nar "Wajah Tojo langsung tampak puas melihatmu menyingkir tanpa perlawanan. Dari jarak beberapa langkah di dekat meja kudapan, kamu masih bisa mendengar percakapan mereka dengan cukup jelas."
            "Tojo" "Nah, akhirnya kita bisa bicara tanpa gangguan, Saionji-san. Hari Sabtu akhir bulan ini keluarga saya mengadakan jamuan makan malam tertutup di hotel pusat. Ayah saya dan para kolega sudah menanyakan kapan Anda akan hadir bersama saya."
            shiori "Saya menghargai undangan keluarga Anda, Tojo-san. Hanya saja jadwal kuliah dan agenda persiapan turnamen klub saya sudah terisi penuh sampai akhir bulan depan."
            "Tojo" "Ayolah, Saionji-san, kegiatan klub mahasiswa kan bisa ditinggal satu malam. Kita berdua sama-sama tahu hubungan antara keluarga kita jauh lebih penting untuk diprioritaskan sekarang."
            shiori "Ayah dan Ibu saya di rumah tidak pernah meminta saya meninggalkan tanggung jawab studi demi jamuan makan malam bisnis, Tojo-san. Kalau tidak ada lagi urusan terkait acara klub, saya permisi kembali ke teman saya."
            nar "Tojo terdiam kaku menerima penolakan dingin yang diucapkan dengan tata krama tanpa cela itu, sebelum akhirnya mengangguk singkat dan pergi. Saat Shiori berjalan kembali menghampirimu di meja minuman, ekspresi wajahnya sudah kembali tenang seperti semula."
            chiasa "Sudah selesai ngobrolnya, Saionji-senpai?"
            shiori "Sudah selesai. Kamu langsung melangkah mundur tadi waktu dia menyuruhmu pergi. Keputusan yang sangat wajar sih, karena itu memang bukan urusanmu."
            chiasa "Aku cuma takut salah bicara kalau ikut campur urusan relasi keluarga Senpai."
            shiori "Aku mengerti kok, Amamiya-san. Tidak ada yang salah dengan menjaga diri sendiri. Hanya saja... aku memang punya kebiasaan selalu mencatat siapa yang memilih diam dan menyingkir ketika melihatku sedang disudutkan."
            chiasa "Maaf ya, Senpai..."
            shiori "Tidak perlu minta maaf. Kita bisa pulang sekarang kalau kamu sudah selesai minum."
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
            yutaka "Maaf kalau sikapku tadi terkesan membiarkanmu sendirian."
            shiori "Tidak masalah, aku memang terbiasa mengurusnya sendiri. Ayo kita pamit ke ketua klub sekarang."
            nar "Suaranya sama sekali tidak terdengar marah atau menyindir keras. Ia tetap menemanimu sampai acara selesai dengan sopan santun yang utuh, tetapi ada dinding kaca tipis yang kini berdiri jelas di antara kalian."
    else:
        if kk_host == "chiasa":
            nar "Begitu mendengar nama besar Tojo Group disebut langsung oleh pewarisnya, kamu justru memasang senyum paling ramahmu dan melangkah setengah tapak ke depan untuk menyapanya dengan antusias."
            chiasa "Wah, tunggu sebentar... Tojo-san ini dari Tojo Group yang membawahi jaringan galeri seni dan properti di distrik pusat itu ya? Kebetulan saya suka sekali baca liputan pameran di gedung milik perusahaan Anda. Senang sekali bisa berkenalan langsung!"
            nar "Tojo yang tadinya hendak mengajak Shiori pergi langsung menoleh kembali kepadamu dengan senyum bangga karena namanya dikenali."
            "Tojo" "Oh? Kamu mengikuti proyek galeri kami rupanya? Selera pengamatanmu bagus juga, Amamiya-san. Kebetulan bulan depan kami memang sedang menyiapkan pembukaan pameran instalasi modern di lobi menara baru kami."
            chiasa "Serius, Tojo-san? Wah, kalau ada kesempatan, saya pengin banget bisa datang melihat kurasi pamerannya dari dekat."
            "Tojo" "Tentu saja bisa. Ini kartu nama pribadiku, hubungi saja nomor sekretarisku minggu depan nanti biar namamu dimasukkan ke daftar tamu undangan."
            chiasa "Terima kasih banyak, Tojo-san!"
            nar "Selama kamu bertukar basa-basi dan menerima kartu nama tersebut, Shiori berdiri diam sempurna di sebelahmu, memperhatikan setiap perubahan nada bicaramu sejak detik pertama tanpa berkedip. Tak lama kemudian, seorang kolega memanggil Tojo dari meja tengah sehingga ia berpamitan pergi. Begitu Tojo berbalik, senyum di bibir Shiori langsung menipis tajam."
            chiasa "Lumayan banget ya, Saionji-senpai. Selain dapat kenalan buat lihat pameran galeri, aku juga sekalian bantu mengalihkan perhatian dia supaya nggak terus-terusan mendesak Senpai ke meja depan tadi."
            shiori "Kalau sejak awal tujuanmu datang ke acara ini memang untuk mencari koneksi dengan Tojo-san, kamu cukup mengatakannya terus terang kepadaku, Amamiya-san."
            chiasa "Eh? Bukan gitu maksudku, Senpai, aku tadi kan sekalian mau bantu memecah suasana..."
            shiori "Tolong jangan menggunakan posisi tidak nyamanku sebagai batu loncatan untuk kepentinganmu sendiri, lalu membungkusnya seolah kamu sedang menolongku. Aku sudah melihat ratusan orang memakai cara persis seperti itu di ruang resepsi keluarga sejak aku masih kecil."
            chiasa "Saionji-senpai, dengar dulu..."
            shiori "Waktuku di acara ini sudah selesai, Amamiya-san. Silakan lanjutkan menikmati resepsinya sendiri kalau masih ada relasi yang ingin kamu temui."
            chiasa "Aku ikut keluar bareng Senpai saja kalau begitu..."
            shiori "Tidak perlu, sopir keluargaku sudah menunggu di lobi bawah. Selamat malam, Amamiya-san."
            nar "Shiori meletakkan gelas teh dinginnya yang belum tersentuh di atas baki pelayan yang melintas, lalu melangkah lurus menuju pintu keluar aula."
            nar "Suara Shiori tetap rendah, lembut, dan sangat sopan di telinga orang yang lewat. Setiap katanya jatuh sedingin es hingga kamu tidak mampu melanjutkan alasanmu lagi."
        else:
            nar "Mendengar nama Tojo Group disebut langsung oleh pewarisnya, kamu justru mengeluarkan senyum paling luwesmu dan melangkah maju mengulurkan tangan lebih dulu kepada pria itu."
            yutaka "Tunggu sebentar, Tojo-san ini dari jajaran manajemen Tojo Group yang pegang proyek pengembangan properti pusat kota itu kan? Kelompok diskusi kuliah saya baru saja membedah laporan ekspansi perusahaan Anda minggu lalu. Suatu kehormatan bisa kenal langsung."
            nar "Sikap Tojo yang tadinya ingin mengusirmu langsung berubah hangat karena merasa disanjung di depan Shiori. Ia menyambut jabatan tanganmu dengan dada membusung."
            "Tojo" "Oh? Mahasiswa Kouseikan yang mengikuti proyek properti kami rupanya? Mata bisnismu boleh juga, Kisaragi-kun. Bulan depan divisi pengembangan kami mengadakan seminar tertutup untuk mahasiswa terpilih dan investor muda."
            yutaka "Wah, kalau diperbolehkan hadir, saya tertarik sekali buat ikut menyimak langsung di forum itu, Tojo-san."
            "Tojo" "Mudah itu. Ini kartu namaku, kirimkan saja pesan ke staf kantorku minggu depan, nanti kupastikan namamu masuk daftar peserta."
            yutaka "Terima kasih banyak kesempatannya, Tojo-san."
            nar "Di sampingmu, Shiori berdiri hening sambil mengamati caramu menyimpan kartu nama Tojo ke dalam saku jas tanpa berkedip sedikit pun. Beberapa detik kemudian, seorang direktur memanggil Tojo ke meja utama sehingga ia pamit menyingkir. Begitu Tojo menjauh, senyum di wajah Shiori berubah sangat tipis."
            yutaka "Hasil yang lumayan kan, Saionji-san? Aku dapat akses seminar bisnis, sekaligus tadi berhasil mengulur waktu supaya kamu nggak jadi diseret ke meja kolega mereka."
            shiori "Kalau kamu memang membutuhkan perkenalan dengan pihak Tojo Group, seharusnya kamu meminta langsung kepadaku sejak awal, Kisaragi-san."
            yutaka "Lho, aku kan tadi sekalian bantu memecah perhatiannya dari kamu..."
            shiori "Jangan memanfaatkan situasi ketika aku sedang terdesak sebagai pintu masuk untuk urusan pribadimu, lalu menyebutnya sebagai bantuan untukku. Sejak kecil aku sudah terlalu hafal dengan orang-orang yang mendekat memakai dalih seperti itu."
            yutaka "Saionji-san, tunggu sebentar..."
            shiori "Urusanku di aula ini sudah cukup, Kisaragi-san. Silakan tinggal lebih lama jika masih ada kolega bisnis yang ingin kamu sapa."
            yutaka "Biar kuantar sampai ke lobi bawah dulu, Saionji-san."
            shiori "Tidak usah repot, mobil jemputanku sudah siap di depan pintu utama. Selamat malam, Kisaragi-san."
            nar "Ia menaruh kembali gelas minumannya ke atas meja samping dengan gerakan rapi, lalu berbalik dan berjalan meninggalkan aula tanpa menoleh lagi."
            nar "Nada bicara Shiori tetap halus dan tidak menarik perhatian tamu di meja sebelah, tetapi ketajamannya langsung menutup seluruh ruang percakapan kalian."
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
