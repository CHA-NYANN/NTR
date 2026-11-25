# Draft adegan dari Event_Shiori dan Alur_Cabang/05. kk_family_menu mencatat pilihan satu kali.
# ┌─ PANDUAN CERITA · S07 · Natal Keluarga Saionji
# │ LOKASI  : Distrik Elite · Rumah Saionji
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : makan malam keluarga.
# │ INTI    : A diundang / B tidak / C mengirim hadiah.
# │ AKHIRAN : hub besar #3; keluarga mengenal pemain.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S07:
    call kk_scene_enter("shiori", "Natal di rumah Saionji")
    if kk_host == "chiasa":
        nar "Kediaman keluarga Saionji di distrik elite malam itu tampak teduh di balik pagar tanaman pangkas dan lampu taman berwarna kuning lembut. Ketika Kuroiwa membukakan pintu kayu besar di serambi depan untukmu yang mampir mengembalikan buku strategi pinjaman sebelum libur akhir tahun, suasana di dalam rumah sama sekali jauh dari kesan jamuan mewah keluarga konglomerat."
        nar "Tidak ada deretan pelayan berjas ataupun musik pesta. Sebaliknya, dari arah ruang makan di ujung lorong parket, tercium wangi sup krim jagung yang baru diangkat dari kompor, roti panggang mentega, dan ayam panggang herba."
        nar "Dari balik pintu ruang makan yang terbuka separuh, terdengar suara berat ayah Shiori, Saionji Shigeru, yang sedang mengangkat kursi kayu tambahan, disusul suara lembut ibunya, Saionji Akane."
        "Ibu Shiori" "Ayah, kursinya jangan ditarik dulu. Tamunya Shiori kan baru sampai di pintu depan, jangan bikin anaknya merasa dipaksa masuk kalau dia memang cuma mau mampir sebentar."
        "Ayah Shiori" "Lho, di luar kan anginnya dingin sekali. Masa teman Shiori datang malam Natal cuma disuruh berdiri di serambi? Supnya juga masih satu panci penuh di kompor."
        "Ibu Shiori" "Iya, tapi biar Shiori sendiri yang menawari dengan sopan di depan dulu. Ayah duduk aja sini merapikan serbetnya."
        nar "Shiori yang berdiri di hadapanmu mengenakan kardigan rajut putih keperakan di atas blus rumahan hanya menggeleng kecil mendengar percakapan kedua orang tuanya yang bocor sampai ke pintu depan. Ia menerima buku dari tanganmu, lalu menatapmu dengan senyum tipisnya."
        shiori "Maaf ya, Amamiya-san, suara mereka terdengar sampai ke sini. Tapi seperti yang baru saja kamu dengar sendiri, kami memang baru mau mulai makan malam."
        chiasa "Aku yang nggak enak, Saionji-senpai. Harusnya aku balikin bukunya kemarin siang di kampus, malah datang tepat di jam makan malam keluarga."
        shiori "Sama sekali tidak mengganggu. Lagipula Kuroiwa sudah memastikan tidak ada tamu bisnis malam ini, jadi hanya kami bertiga di dalam. Kalau kamu belum punya janji makan malam di tempat lain, silakan masuk dan makan bersama kami."
        chiasa "Eh, Oji-san sama Oba-san beneran nggak keberatan?"
        shiori "Kamu dengar sendiri Ayahku hampir menarik kursi sampai ke lorong barusan. Ayah dan Ibu jauh lebih santai diajak mengobrol daripada reputasi nama Saionji yang sering dibicarakan orang di kampus. Biasanya, sih."
        chiasa "Wangi sup jagungnya memang bikin lapar dari depan pintu sih, Senpai."
        shiori "Sup jagung itu resep andalan Ibu setiap malam tanggal dua puluh empat Desember."
        nar "Shiori menatapmu dengan tenang di bawah lampu serambi yang hangat sambil menunggu keputusanmu."
    else:
        nar "Kediaman keluarga Saionji di distrik elite malam itu tampak tenang di balik pagar tanaman pangkas dan pendar lampu taman berwarna kuning hangat. Ketika Kuroiwa membukakan pintu kayu besar di serambi depan untukmu yang mampir mengembalikan buku catatan strategi pinjaman sebelum libur akhir tahun, pemandangan di dalam rumah sama sekali tidak menyerupai pesta resmi keluarga konglomerat yang pernah disinggung orang tuamu."
        nar "Tidak ada deretan tamu berjas atau iringan musik kaku. Sebaliknya, dari arah ruang makan di ujung lorong kayu, tercium aroma sup krim jagung yang baru matang, roti panggang mentega, dan ayam panggang herba."
        nar "Dari balik pintu ruang makan yang terbuka separuh, terdengar suara berat ayah Shiori, Saionji Shigeru, yang sedang menggeser kursi tambahan, disusul teguran lembut ibunya, Saionji Akane."
        "Ibu Shiori" "Ayah, jangan keburu menarik kursinya dulu. Teman Shiori kan baru sampai di depan pintu, nanti anaknya malah sungkan dan merasa dipaksa masuk kalau memang cuma mau mampir sebentar."
        "Ayah Shiori" "Lho, di luar angin malam Natal dingin sekali. Masa tamu Shiori datang jauh-jauh cuma dibiarkan berdiri di serambi depan? Sup jagungnya juga masih banyak di panci."
        "Ibu Shiori" "Iya, tapi biar Shiori yang mempersilakan sendiri dengan tenang. Ayah bantu tata piring rotinya dulu sini."
        nar "Shiori yang berdiri di hadapanmu mengenakan kardigan rajut putih keperakan di atas blus rumahan menghela napas kecil mendengar percakapan kedua orang tuanya yang terdengar jelas sampai ke genkan. Ia menerima buku dari tanganmu, lalu menatapmu dengan senyum tipis."
        shiori "Maaf, Kisaragi-san, suara mereka memang agak sulit ditahan kalau sudah soal tamu. Tapi seperti yang baru saja kamu dengar sendiri, kami memang baru mau mulai makan malam."
        yutaka "Aku yang jadi nggak enak, Saionji-san. Harusnya buku ini kubalikin kemarin siang di fakultas, malah datang tepat di jam makan malam keluargamu."
        shiori "Tidak mengganggu sama sekali. Lagipula malam ini tidak ada satu pun acara formal, hanya kami bertiga di meja makan. Kalau kamu belum punya janji makan malam di tempat lain, silakan masuk."
        yutaka "Oji-san sama Oba-san beneran nggak keberatan aku ikut makan mendadak?"
        shiori "Kamu dengar sendiri Ayahku hampir mengangkat kursi ke depan pintu tadi. Ayah dan Ibu jauh lebih mudah diajak mengobrol daripada reputasi nama Saionji yang sering dibicarakan orang di luar sana. Biasanya, sih."
    call kk_family_menu("S07", ["\"Terima kasih. Kalau tidak merepotkan, aku ikut makan malam bersama.\"", "\"Selamat Natal untuk keluarga di rumah ya. Aku langsung pamit saja.\"", "\"Aku tidak bisa lama-lama, tapi aku bawa bingkisan kecil ini buat keluargamu.\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Terima kasih, Saionji-senpai. Kalau memang nggak merepotkan Oji-san dan Oba-san, aku ikut makan malam bersama."
            shiori "Kalau begitu silakan lepas mantelmu di sini. Biar kugantungkan di lemari depan, sandal tamunya ada di sebelah kanan."
            nar "Kamu melepas sepatu dan mantel tebalmu di genkan, lalu mengikuti Shiori masuk ke ruang makan yang hangat oleh lampu gantung kaca berwarna gading. Begitu melihatmu masuk, Saionji Akane langsung meletakkan sendok sup besar dan menyambutmu dengan senyum ramah, sementara Shigeru menarik kursi kayu tepat di sebelah Shiori."
            "Ibu Shiori" "Selamat malam, Amamiya Chiasa-san, benar kan? Shiori beberapa kali menyebut namamu waktu kami minum teh minggu lalu. Ayo duduk, tanganmu pasti dingin habis jalan dari stasiun."
            chiasa "Selamat malam, Oba-san, Oji-san. Maaf saya datang mendadak malam Natal begini."
            "Ayah Shiori" "Justru menyenangkan kalau ada teman Shiori yang mampir. Rumah sebesar ini kalau malam Natal cuma diisi kami bertiga rasanya sepi sekali. Sini, piring supnya sudah hangat."
            nar "Saat makan malam dimulai, suasana di meja itu terasa mengejutkan karena begitu mirip dengan keluarga biasa yang hangat. Tidak ada satu pun pertanyaan tentang pekerjaan orang tuamu atau relasi keluarga."
            "Ayah Shiori" "Chiasa-san, kalau di klub catur kampus Shiori suka kasih keringanan ke lawan barunya nggak? Soalnya sore tadi Ayahnya sendiri aja dikalahkan tiga babak berturut-turut tanpa dikasih ampun sedikit pun di malam Natal!"
            shiori "Ayah sendiri yang lupa menutup jalur diagonal gajahnya di langkah kedua belas. Kalau kubiarkan begitu saja, Ayah malah akan protes karena merasa diremehkan."
            "Ayah Shiori" "Haha, dengar sendiri kan jawabannya? Padahal aku cuma minta satu kemenangan biar makan malam terasa lebih manis."
            chiasa "Di kampus juga Saionji-senpai mainnya selalu tenang banget kok, Oji-san. Tapi habis selesai babak pasti langsung dikasih tahu salah langkahnya di mana. Oh ya, sup jagungnya enak sekali, Oba-san. Manisnya pas dan hangat di tenggorokan."
            "Ibu Shiori" "Syukurlah kalau cocok di lidahmu, Chiasa-san. Masih banyak di panci kalau mau tambah nanti. Ngomong-ngomong, kalau di kampus Shiori tidak terlalu galak atau menyendiri kan? Kadang Ibu khawatir kalau dia terlalu lama di ruang klub catur, teman-teman seangkatannya jadi segan mengajak mengobrol, apalagi waktu acara fakultas kemarin..."
            nar "Pertanyaan beruntun dari ibunya yang penuh perhatian membuatmu sempat terdiam sambil memegang sendok, bingung harus menjawab seberapa jauh. Di sebelahmu, Shiori meletakkan gelas airnya dengan bunyi pelan sambil menahan senyum geli."
            shiori "Ibu, tahan dulu pertanyaannya. Amamiya-san baru selesai makan setengah mangkuk supnya. Kalau Ibu bertanya terus dengan nada serius begitu, nanti dia mengira sedang ikut wawancara yayasan beasiswa Ibu."
            "Ibu Shiori" "Eh? Ya ampun, maafkan Oba-san ya, Chiasa-san. Oba-san cuma senang akhirnya ada teman kampus Shiori yang mampir makan ke rumah."
            chiasa "Nggak apa-apa kok, Oba-san. Di kampus Saionji-senpai baik banget sama saya, malah sering bantu ngasih sudut pandang tiap saya lagi bingung."
            "Ayah Shiori" "Haha, kamu dengar sendiri kan, Bu? Anak kita baik-baik saja di sana. Sudah, biarkan Chiasa-san makan ayam panggangnya dulu sebelum dingin."
            shiori "Ambil roti panggang menteganya juga, Amamiya-san. Ini paling enak dimakan selagi masih renyah dicelup ke sup."
            chiasa "Iya, terima kasih, Senpai."
            "Ayah Shiori" "Habis makan utama ini masih ada puding karamel hangat yang disiapkan di dapur lho, Chiasa-san, jadi jangan buru-buru kenyang dulu."
            chiasa "Wah, saya suka sekali puding karamel, Oji-san!"
            "Ibu Shiori" "Syukurlah, tadi Oba-san sempat ragu mau bikin kue tar atau puding hangat untuk malam sedingin ini."
            shiori "Pilihan Ibu tepat sekali malam ini."
            nar "Shiori melirikmu dari sudut matanya dengan senyum tipis yang hangat dan jauh lebih rileks daripada wajah tenangnya di kampus. Sisa malam di ruang makan itu mengalir santai ditemani cerita ringan dan teh hangat setelah hidangan utama selesai."
        else:
            yutaka "Terima kasih, Saionji-san. Kalau memang nggak merepotkan Oji-san dan Oba-san, aku ikut makan malam bersama deh."
            shiori "Kalau begitu silakan lepas mantelmu di sini. Biar kutaruh di gantungan depan, sandal tamunya sudah disiapkan di sebelah kanan."
            nar "Kamu melepas sepatu dan mantelmu di genkan, lalu mengikuti Shiori masuk ke ruang makan yang hangat oleh cahaya lampu gantung kaca berwarna gading. Begitu kamu muncul di ambang pintu, Saionji Akane langsung menggeser piring sup untuk menyiapkan tempatmu sambil tersenyum ramah, sementara Shigeru menarik kursi kayu di samping Shiori."
            "Ibu Shiori" "Selamat malam, Kisaragi Yutaka-san, benar kan? Shiori sempat menyebut namamu minggu lalu saat bercerita soal teman satu fakultas yang suka berdiskusi di klub catur. Ayo duduk, supnya baru saja dituang."
            yutaka "Selamat malam, Oba-san, Oji-san. Maaf saya datang mendadak malam Natal begini."
            "Ayah Shiori" "Justru kami yang senang ada tamu malam ini. Rumah sebesar ini kalau cuma makan bertiga rasanya terlalu hening. Duduklah, jangan sungkan."
            nar "Selama makan malam berlangsung, tidak ada satu pun pertanyaan tentang perusahaan keluarga Kisaragi ataupun relasi bisnis yang selama ini kamu duga bakal keluar dari meja orang berada."
            "Ayah Shiori" "Ngomong-ngomong, Kisaragi-san, kalau di ruang klub catur Shiori mainnya sekejam di rumah nggak? Masa sore tadi Ayahnya sendiri dikalahkan tiga babak berturut-turut tanpa dikasih keringanan sedikit pun di malam Natal."
            shiori "Ayah sendiri yang membiarkan jalur gajahnya terbuka di langkah kedua belas. Kalau aku pura-pura tidak melihat, Ayah malah akan tahu dan protes."
            "Ayah Shiori" "Haha, selalu saja punya alasan logis. Kamu sendiri sering menang lawan dia di kampus, Kisaragi-san?"
            yutaka "Jujur saja, Oji-san, buat bikin Saionji-san mikir lebih dari tiga puluh detik di satu langkah aja sudah lumayan berat. Tapi asyik buat latihan baca arah lawan. Oh ya, sup jagungnya enak sekali, Oba-san. Hangat banget buat malam sedingin ini."
            "Ibu Shiori" "Syukurlah kalau kamu suka, Kisaragi-san, nanti tambah lagi ya. Omong-omong, kalau di kelas Ekonomi Shiori tidak terlalu jaga jarak sama teman-teman seangkatannya kan? Oba-san kadang kepikiran kalau dia terlalu sibuk di ruang klub sampai jarang makan siang bareng yang lain, padahal..."
            nar "Rentetan pertanyaan tulus dari Akane membuatmu sedikit kikuk di atas kursi sambil memegang sendok, tidak terbiasa menghadapi keramahan orang tua yang langsung akrab seperti ini. Melihat ekspresimu, Shiori menurunkan gelas airnya dengan bunyi pelan sembari menahan senyum geli."
            shiori "Ibu, pelan-pelan dulu pertanyaannya. Kisaragi-san bahkan belum sempat menyentuh ayam panggangnya. Kalau Ibu terus bertanya serinci itu, nanti dia malah merasa sedang menghadapi rapat evaluasi yayasan Ibu."
            "Ibu Shiori" "Eh? Ya ampun, maaf ya, Kisaragi-san. Oba-san cuma kelewat senang akhirnya Shiori membawa teman satu fakultas makan malam di rumah."
            yutaka "Nggak apa-apa kok, Oba-san. Di kampus Saionji-san memang paling sering bikin lawan tandingnya mikir keras, tapi dia baik banget sama saya."
            "Ayah Shiori" "Haha, dengar sendiri kan, Bu? Ayo, Kisaragi-san, habiskan dulu ayam panggangnya sebelum dingin."
            shiori "Ambil roti panggang menteganya juga, Kisaragi-san. Enak dimakan selagi masih hangat dicelup ke sup."
            yutaka "Oke, makasih, Saionji-san."
            "Ayah Shiori" "Habis makan malam nanti jangan langsung pamit pulang ya, Kisaragi-san. Tadi kami sudah menyiapkan puding karamel hangat sama teh panggang di ruang duduk."
            yutaka "Terima kasih banyak, Oji-san. Dengan senang hati saya temani minum tehnya."
            "Ibu Shiori" "Jarang-jarang Shiori betah duduk lama di meja makan sambil senyum-senyum santai seperti malam ini."
            shiori "Ibu, kami hanya sedang menikmati makan malamnya dengan tenang."
            nar "Shiori melirikmu sekilas dari balik gelasnya dengan senyum tipis yang geli dan jauh lebih santai daripada biasanya di kampus. Obrolan meja makan berlanjut ringan tanpa beban hingga cangkir teh hangat selepas makan malam."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Terima kasih banyak tawarannya, Saionji-senpai, tapi aku nggak mau ganggu waktu makan malam keluarga Senpai. Di rumah juga sudah ada acara makan sendiri. Selamat Natal buat Senpai, Oji-san, dan Oba-san di dalam ya. Aku langsung pamit pulang aja."
            nar "Shiori sama sekali tidak memasang wajah kecewa atau mendesakmu masuk demi basa-basi. Ia merapikan posisi buku di pelukannya dan mengangguk tenang."
            shiori "Aku mengerti, kamu pasti juga sudah ditunggu di rumah. Akan kusampaikan salam Natalmu kepada Ayah dan Ibu di ruang makan. Mereka pasti akan bertanya kenapa tidak kutahan sebentar, tapi biar aku yang menjelaskan."
            chiasa "Haha, maaf ya jadi bikin Senpai harus menjelaskan ke Oji-san sama Oba-san, terus jadi berdiri di serambi dingin begini pas supnya baru dihidangkan."
            shiori "Tidak masalah sama sekali. Justru aku senang kamu menyempatkan mampir mengantar buku ini sendiri sebelum tahun baru, jadi catatannya bisa langsung kupakai selama liburan."
            nar "Ketika Kuroiwa membuka kembali pintu depan untukmu, udara malam menyapu masuk. Shiori melangkah setengah tapak mengantarmu sampai ke batas genkan."
            shiori "Lain kali kalau kamu lewat dekat sini atau ingin main satu babak lagi di rumah, mampir saja, Amamiya-san. Kamu tidak harus menunggu ada hari raya atau alasan mengembalikan buku dulu untuk diizinkan duduk makan di meja kami."
            chiasa "Terima kasih banyak, Saionji-senpai. Lain kali pasti kumanfaatkan tawarannya. Selamat malam."
            shiori "Selamat malam. Hati-hati di jalan, angin malam ini cukup dingin. Pastikan syalmu rapat sampai stasiun."
            chiasa "Iya, syalnya sudah kupakai rapat kok, Senpai. Salam hangat buat Oji-san dan Oba-san di meja makan."
            shiori "Pasti kusampaikan begitu aku masuk ke dalam. Sampai bertemu di kampus awal tahun nanti, Amamiya-san."
            nar "Kuroiwa mengangguk hormat dari samping pintu serambi sambil menyalakan lampu jalan taman depan agar langkahmu menuju gerbang terlihat terang."
            nar "Pintu kayu serambi tertutup pelan di belakangmu setelah kamu melangkah keluar ke jalan setapak taman yang tenang."
        else:
            yutaka "Terima kasih banyak tawarannya, Saionji-san, tapi aku nggak enak kalau mengganggu waktu makan malam keluargamu. Selamat Natal ya buat kamu, Oji-san, sama Oba-san di dalam. Aku langsung pamit aja."
            nar "Shiori tidak tampak tersinggung sedikit pun dan tidak memaksamu masuk demi sekadar sopan santun. Ia mendekap buku yang baru kamu kembalikan lalu mengangguk tenang."
            shiori "Baiklah, aku mengerti. Akan kusampaikan ucapan selamat Natalmu kepada Ayah dan Ibu di ruang makan. Ayah mungkin akan sedikit protes karena kursinya sudah telanjur ditarik, tapi biar aku yang menanganinya."
            yutaka "Haha, maaf ya malah bikin Oji-san kecewa dan bikin kamu berdiri di serambi pas supnya baru dihidangkan."
            shiori "Tidak masalah. Terima kasih sudah menyempatkan diri mengantar buku ini langsung sebelum libur panjang, catatannya memang mau kubaca ulang minggu depan."
            nar "Ketika Kuroiwa membukakan pintu kayu serambi untukmu, Shiori melangkah maju sedikit mengantarmu sampai tepi genkan."
            shiori "Lain kali kalau kamu sedang luang di sekitar sini, mampir saja, Kisaragi-san. Kamu tidak harus menunggu hari raya atau alasan mengembalikan buku dulu untuk diizinkan makan malam di rumah ini."
            yutaka "Oke, lain kali pasti kumanfaatkan tawarannya. Selamat malam, Saionji-san."
            shiori "Selamat malam. Hati-hati di jalan, angin malam ini cukup tajam."
            yutaka "Iya, salam buat kedua orang tuamu di dalam ya."
            shiori "Tentu. Sampai bertemu di fakultas setelah libur tahun baru nanti, Kisaragi-san."
            nar "Kuroiwa membungkuk sopan di dekat ambang pintu sambil memastikan lampu pagar depan menyala terang mengiringi langkahmu."
            nar "Kamu melangkah menuruni jalan setapak taman yang tenang sementara pintu kayu besar rumah Saionji menutup perlahan di belakangmu."
    else:
        if kk_host == "chiasa":
            nar "Kamu membuka tas selempangmu dan mengeluarkan sebuah kotak kaleng kecil berwarna hijau tua yang diikat pita krem, berisi daun teh panggang pilihan dari kedai tua dekat stasiun timur, lalu menyodorkannya dengan kedua tangan."
            chiasa "Maaf malam ini aku nggak bisa mampir makan, Saionji-senpai, soalnya di rumah sudah masak juga. Tapi aku bawa bingkisan teh ini buat Senpai sama keluarga di rumah. Selamat Natal ya."
            nar "Pandangan Shiori turun menatap kaleng teh tersebut. Ia meletakkan buku pinjamannya di atas meja konsol serambi terlebih dahulu agar bisa menerima kotak teh darimu dengan kedua tangan."
            shiori "Ini daun teh panggang dari kedai tua di seberang stasiun timur, kan? Wanginya khas sekali, bahkan masih terasa tipis dari luar kalengnya. Pilihan yang sangat cermat, Amamiya-san."
            chiasa "Syukurlah kalau Senpai kenal kedainya. Penjaga tokonya tadi bilang panggangan daun musim dingin yang ini paling enak diseduh habis makan makanan yang hangat atau berlemak."
            shiori "Ayahku sangat menyukai teh panggang dari kedai itu. Bahkan biasanya beliau menyimpan kaleng cadangannya sendiri di lemari ruang kerja supaya tidak tertukar. Biar kubawa langsung ke meja makan kami malam ini, tidak dicampur dengan tumpukan parsel di ruang depan."
            chiasa "Wah, untung banget ternyata cocok sama selera Oji-san."
            nar "Shiori memegang kaleng teh itu dengan hati-hati, lalu mengangkat wajah menatapmu lagi."
            shiori "Kalau begitu, ada pesan singkat yang ingin kamu titipkan untuk Ayah dan Ibu bersama teh ini? Aku ingin mereka menerimanya sebagai perhatian pribadimu sendiri supaya tidak tercampur dengan parsel formal dari rekan bisnis Ayah."
            chiasa "Bilang aja semoga Oji-san, Oba-san, dan Saionji-senpai suka tehnya buat diminum hangat-hangat sehabis makan malam Natal bersama, sambil istirahat dari urusan kerja dan kampus."
            shiori "Kalimat yang jujur dan tanpa embel-embel. Akan kusampaikan persis seperti yang kamu ucapkan barusan. Terima kasih banyak untuk perhatiannya malam ini, Amamiya-san."
            chiasa "Sama-sama, Senpai. Nanti kalau libur sudah selesai kita ketemu lagi di kampus ya. Aku pamit dulu, selamat malam."
            shiori "Selamat malam, Amamiya-san. Hati-hati di jalan pulang."
            chiasa "Jangan lupa langsung masuk ya, Senpai, di serambi sini udaranya mulai dingin."
            shiori "Aku masuk begitu kamu sampai di gerbang depan. Terima kasih sekali lagi untuk tehnya, Amamiya-san."
            nar "Aroma hangat sup jagung dari ruang makan kembali tercium samar saat Kuroiwa menahan daun pintu kayu untuk kepergianmu."
            nar "Shiori mengangguk anggun dengan senyum yang tampak lebih lembut daripada biasanya, lalu tetap berdiri di ambang serambi sampai kamu melewati gerbang halaman depan."
        else:
            nar "Kamu mengeluarkan sebuah kotak kaleng hijau tua berpita krem dari kantong kertas yang sejak tadi kamu bawa, berisi daun teh panggang pilihan dari kedai tua di dekat stasiun timur, lalu menyodorkannya dengan sopan."
            yutaka "Maaf malam ini aku nggak bisa ikut makan, Saionji-san. Tapi aku bawa bingkisan teh kecil ini buat kamu sama orang tuamu di rumah. Selamat Natal ya."
            nar "Tatapan Shiori turun mengamati kaleng teh di tanganmu. Ia meletakkan buku pinjamannya di atas meja konsol serambi terlebih dulu, lalu menerima kotak teh itu dengan kedua tangan."
            shiori "Daun teh panggang dari kedai tua di seberang stasiun timur, kan? Wanginya bahkan masih terasa tipis dari balik tutup kalengnya. Kamu tahu betul cara memilih hadiah yang tidak terasa dibuat-buat, Kisaragi-san."
            yutaka "Syukurlah kalau cocok. Pemilik kedainya tadi bilang panggangan musim dingin yang ini paling pas diseduh sehabis makan malam."
            shiori "Ayahku memang sangat menyukai teh dari kedai itu, bahkan punya kaleng simpanan khusus di ruang kerjanya. Biar kubawa langsung ke ruang makan kami sendiri, tidak kutaruh bersama tumpukan parsel akhir tahun di ruang depan."
            yutaka "Syukurlah kalau begitu, nggak sia-sia aku mampir ke gang stasiun timur tadi sore."
            nar "Shiori menimbang kaleng teh itu sejenak lalu mengangkat pandangannya kembali padamu."
            shiori "Ada pesan singkat yang ingin kamu titipkan bersama teh ini untuk Ayah dan Ibu? Aku ingin memastikan mereka mengenalinya sebagai niat pribadimu sendiri supaya tidak disamakan dengan bingkisan relasi bisnis di depan."
            yutaka "Sampaikan aja salam Natal dariku, semoga Oji-san, Oba-san, sama kamu bisa menikmati tehnya hangat-hangat habis makan malam nanti, sekalian istirahat sebelum tahun baru."
            shiori "Sederhana dan jelas. Akan kusampaikan tepat seperti itu. Terima kasih sudah menyempatkan mampir malam ini, Kisaragi-san."
            yutaka "Sama-sama, Saionji-san. Sampai ketemu habis libur ya. Aku pamit pulang dulu, selamat malam."
            shiori "Selamat malam, Kisaragi-san. Hati-hati di jalan."
            yutaka "Masuklah dulu, angin malamnya makin kencang kalau pintunya dibuka lama-lama."
            shiori "Aku akan masuk setelah kamu melewati pagar depan. Terima kasih untuk perhatianmu malam ini, Kisaragi-san."
            nar "Kuroiwa membukakan pintu serambi lebar-lebar sambil membungkuk sopan melepas kepergianmu menuju jalan utama Distrik Elite."
            nar "Shiori mengangguk dengan senyum tipis yang terasa jauh lebih santai daripada biasanya di kampus, lalu tetap berdiri di ambang pintu serambi hingga kamu melewati pagar halaman depan."
    return

# ┌─ PANDUAN CERITA · S-D08 · Teh dengan Ibu Saionji
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : setelah S07-A
# │ INTI    : A Jujur / B menyanjung / C membocorkan
# │ AKHIRAN : kehangatan keluarga; Shiori tahu apa yang dikatakan
# └─ tulis / perbaiki dialog di bawah ──
label kk_saionji_tea:
    nar "Di ruang duduk Rumah Saionji yang tenang dan beraroma kayu cemara, Akane, ibu Shiori, langsung mengenalimu dari makan malam Natal kemarin. Sambil menunggu Shiori menyelesaikan urusan sebentar di lantai atas, ia menuangkan dua cangkir teh hijau hangat dengan gerakan lembut."
    if kk_host == "chiasa":
        "Ibu Shiori" "Silakan diminum, Amamiya-san. Terima kasih sudah datang lagi. Di rumah, Shiori sering sekali duduk membaca sendirian. Aku tahu kadang-kadang dia memang menyukai ketenangan itu, tapi sebagai ibu aku cuma ingin tahu apakah di kampus dia punya teman yang sungguh-sungguh dia inginkan sendiri."
    else:
        "Ibu Shiori" "Silakan diminum, Kisaragi-san. Di rumah, Shiori sering memilih duduk sendirian di ruang baca. Aku mengerti dia memang butuh ketenangan, cuma kadang aku bertanya-tanya apakah di kampus ada teman yang sungguh dia sukai sendiri, lepas dari orang-orang yang mendekat karena merasa perlu menjaga hubungan baik dengan nama keluarga kami."
    nar "Suara Akane terdengar halus tanpa sedikit pun nada menginterogasi, hanya kekhawatiran jujur seorang ibu yang tahu betapa sering putrinya bersembunyi di balik kesopanan."
    call kk_family_menu("S-D08", ["Ceritakan apa yang kamu lihat tanpa menebak perasaannya.", "Katakan bahwa semua orang selalu ingin bersamanya.", "Ulangi obrolan pribadi kalian kepada ibunya."])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Kalau di klub catur, Saionji-senpai kelihatan paling lepas saat membahas langkah permainan sama obrolan santai setelah klub tutup, Oba-san. Tapi soal siapa yang paling bikin beliau nyaman, kurasa lebih tepat kalau Oba-san dengar langsung dari beliau sendiri."
        else:
            yutaka "Yang kulihat di kampus, Saionji-san paling santai waktu suasana ruang klub sudah sepi tanpa formalitas, Oba-san. Soal perasaannya yang lebih dalam, kayaknya aku nggak berhak nebak-nebak mewakilinya."
        "Ibu Shiori" "Terima kasih atas jawaban jujurnya. Benar juga ya, mungkin memang seharusnya aku sendiri yang belajar bertanya pelan-pelan padanya, tanpa meminta teman-temannya jadi juru bicara."
        nar "Wajah Akane tampak lebih lega ketika ia mengangkat cangkir tehnya. Saat Shiori turun beberapa menit kemudian, suasana ruang duduk terasa hangat dan bersih."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Tenang aja, Oba-san! Di kampus semua orang kagum banget sama Saionji-senpai dan selalu pengin duduk dekat beliau kok."
        else:
            yutaka "Oba-san nggak perlu khawatir, di kampus Saionji-san sangat dihormati dan banyak sekali orang yang selalu ingin berada di lingkaran pergaulannya."
        nar "Akane tersenyum sopan sambil menundukkan pandangan sekilas ke cangkir tehnya."
        "Ibu Shiori" "Begitu ya... banyak yang ingin mendekatinya. Kalau begitu, apakah menurutmu Shiori sendiri tampak senang berada di tengah mereka semua?"
        nar "Pertanyaan lembut itu langsung membuat pujianmu terasa hampa dan belum sedikit pun menyentuh hal yang sebenarnya ia khawatirkan."
    else:
        nar "Demi menunjukkan bahwa kamu cukup dekat dengan Shiori, kamu mulai mengulang isi percakapan pribadi yang pernah Shiori bagikan kepadamu di klub catur tentang tekanan keluarga dan rasa lelahnya. Belum selesai kalimatmu, Akane meletakkan cangkir tehnya perlahan ke atas tatakan keramik."
        "Ibu Shiori" "Maaf menyela. Aku memang ingin tahu apakah Shiori baik-baik saja di kampus, tapi aku sama sekali nggak memintamu menyerahkan rahasia yang dia percayakan kepadamu. Hal seperti itu jauh lebih baik dia sendiri yang memilih menceritakannya kepadaku."
        nar "Baru saat keheningan turun di antara kalian, kamu benar-benar sadar bahwa cerita yang baru saja kamu pakai untuk mencari simpati itu sejak awal bukan milikmu untuk dibagikan."
    return

# ┌─ PANDUAN CERITA · S09 · Tawaran Persahabatan
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia meminta teman sejati.
# │ INTI    : A terima / B tolak / C manfaatkan.
# │ AKHIRAN : shiori_kepercayaan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S09:
    call kk_scene_enter("shiori","Klub Catur")
    if kk_host == "chiasa":
        nar "Satu per satu anggota Klub Catur lainnya berpamitan meninggalkan ruangan hingga hanya menyisakan kamu dan Saionji Shiori di meja kayu dekat jendela. Pertandingan latihan di antara kalian baru saja berakhir dengan langkah menteri putih Shiori yang menutup seluruh jalan keluar rajamu."
        chiasa "Yah, kalah lagi deh... Padahal tadi aku udah yakin banget pertahanan di sisi kiriku aman, Senpai."
        shiori "Fufu, langkah bentengmu di giliran kedua puluh sebenarnya sudah cukup bagus, Amamiya-san."
        shiori "Kamu cuma sedikit lengah waktu membiarkan jalur diagonal tengahnya terbuka."
        chiasa "Susah banget baca tiga langkah ke depan kalau lawannya Senpai..."
        nar "Shiori mulai memungut bidak-bidak kayu dari atas papan lalu memasukkannya ke dalam kotak beludru satu per satu sebelum percakapan benar-benar selesai. Gerakan tangannya yang biasanya rapi dan cepat perlahan melambat. Tepat ketika hanya tersisa dua bidak raja di atas papan, jemarinya berhenti mengetuk pelan tepi kotak kayu."
        nar "Ia menatap dua bidak terakhir itu cukup lama, seolah sedang menimbang sebuah pertanyaan yang sama sekali tidak bisa diuji dengan membaca tiga langkah lawan. Ketika ia akhirnya mengangkat wajah menatapmu, senyum sopan seragam yang biasa ia kenakan di depan kerumunan sudah tidak ada di sana."
        shiori "Amamiya-san, boleh aku tanya satu hal di luar urusan catur?"
        chiasa "Boleh dong, Senpai. Mau tanya apa?"
        shiori "Selama ini, hampir setiap orang yang duduk di depanku selalu datang membawa maksud tertentu."
        shiori "Ada yang mengincar nama keluargaku, ada yang mengharapkan koneksi bisnis, atau sekadar ingin pamer bisa mengalahkanku."
        nar "Shiori meletakkan kedua tangannya tenang di atas meja, sorot matanya menatapmu jernih tanpa sedikit pun nada menyindir."
        shiori "Kalau suatu hari aku datang menemuimu cuma sebagai orang biasa—tanpa catur, tanpa undangan pesta, dan tanpa keuntungan apa pun..."
        shiori "Apa kamu masih mau duduk mengobrol denganku seperti ini?"
        nar "Di luar jendela ruang klub, bayangan pepohonan kampus bergoyang pelan diterpa angin sore sementara Shiori menunggu jawabanmu dalam keheningan."
        nar "Pertanyaan sederhana itu memperlihatkan sisi rapuh seorang pewaris keluarga besar yang selama ini selalu dikelilingi oleh kepentingan orang lain."
        nar "Dua bidak raja yang masih tertinggal di atas petak papan kayu tampak seolah menandai batas antara permainan strategi dan ketulusan hati."
        nar "Kamu menatap wajah Shiori yang kali ini sama sekali tidak berlindung di balik senyum formal seorang ketua klub."
    else:
        nar "Satu per satu anggota Klub Catur lainnya berpamitan meninggalkan ruangan hingga hanya menyisakan kamu dan Saionji Shiori di meja kayu dekat jendela. Pertandingan latihan di antara kalian baru saja berakhir setelah pertukaran kuda di tengah papan membuka jalan bagi menteri putih Shiori menutup seluruh langkah rajamu."
        yutaka "Yah, kalah lagi. Padahal kupikir pertukaran kudaku di tengah tadi udah cukup buat nahan seranganmu, Saionji-san."
        shiori "Fufu, langkahmu di giliran kedelapan belas sebenarnya lumayan berani, Kisaragi-san."
        shiori "Sayangnya kamu terlalu cepat membuka barisan pion di sayap kanan."
        yutaka "Selalu aja ketahuan celahnya dua langkah sebelum aku sadar sendiri."
        nar "Shiori mulai memungut bidak-bidak kayu dari atas papan lalu memasukkannya ke dalam kotak beludru satu per satu sebelum percakapan selesai. Gerakan tangannya yang biasanya rapi dan cepat perlahan melambat. Tepat ketika hanya tersisa dua bidak raja di atas papan, jemarinya berhenti mengetuk pelan tepi kotak penyimpanan."
        nar "Ia memandangi dua bidak terakhir itu cukup lama, seolah sedang menimbang sebuah pertanyaan yang tidak bisa diuji dengan membaca tiga langkah lawan. Ketika ia akhirnya mengangkat wajah menatapmu, senyum sopan seragam yang biasa ia kenakan di depan kerumunan sudah lenyap dari bibirnya."
        shiori "Kisaragi-san, boleh aku tanya sesuatu di luar papan catur?"
        yutaka "Boleh aja. Ada apa?"
        shiori "Kamu sendiri berasal dari keluarga pebisnis, jadi kurasa kamu paham rasanya. Selama ini, hampir semua orang yang mendekatiku selalu punya sesuatu yang ingin mereka tukarkan."
        shiori "Entah itu nama besar Saionji, undangan jamuan relasi, atau sekadar gengsi mengalahkanku."
        nar "Shiori meletakkan kedua tangannya tenang di atas meja, tatapan matanya menatapmu jernih tanpa sedikit pun nada menyindir."
        shiori "Kalau suatu hari aku datang menemuimu cuma sebagai orang biasa yang tidak membawa urusan catur maupun keuntungan bisnis apa pun..."
        shiori "Apakah kamu masih mau duduk di sini bersamaku?"
        nar "Keheningan ruang Klub Catur sore itu membuat setiap kata yang diucapkan Shiori terdengar begitu jujur tanpa lapisan strategi sedikit pun."
        nar "Ia tidak sedang menguji langkah lawan di atas papan, melainkan sedang mencari tahu apakah ada satu ruang aman tempat ia bisa melepas beban marganya."
        nar "Dua bidak raja yang tersisa di tengah papan catur itu tampak menandai titik penentu dalam hubungan pertemanan kalian di luar urusan keluarga."
        nar "Kamu memperhatikan sorot mata Shiori yang menunggu jawabanmu dengan kesungguhan yang jarang sekali ia perlihatkan kepada siapa pun."
    call kk_family_menu("S09", ["\"Tutup aja papannya sekarang. Nggak usah buru-buru pulang, duduk sini dan cerita apa aja.\"", "\"Jujur aja, aku lebih nyaman kalau kita tetap ketemu sebatas buat main catur aja.\"", "\"Tentu aja aku mau jadi temanmu. Ngomong-ngomong, boleh kenalin aku ke relasi keluargamu nanti?\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Tutup aja papannya sekarang, Senpai. Dari awal aku ke sini juga bukan gara-gara undangan pesta atau nama keluarga Senpai, kok."
            chiasa "Kalau Senpai belum buru-buru pulang, duduk aja di sini. Kita ngobrol santai tanpa perlu mikirin langkah apa-apa."
            nar "Kamu mendorong papan catur sedikit ke tepi meja lalu menggeser kursimu agar lebih santai. Shiori terdiam sepersekian detik melihat betapa tanpa ragunya kamu menjawab. Perlahan, sebuah senyum kecil yang jauh lebih tulus muncul di sudut bibirnya."
            nar "Ia memasukkan dua bidak terakhir ke kotak beludru, mengaitkan kunci kuningan kotaknya, lalu menarik kursinya kembali mendekat ke meja."
            shiori "Fufu... Terima kasih sudah menjawab tanpa berputar-putar, Amamiya-san. Kalau begitu, boleh aku mencoba sesuatu yang jarang kulakukan?"
            chiasa "Mencoba apa tuh, Senpai?"
            shiori "Aku ingin cerita hal-hal remeh dari hariku. Kalau kamu mulai bosan, langsung potong saja ya. Aku sedang belajar berhenti menebak-nebak isi kepala orang."
            chiasa "Siap! Ayo cerita aja, memangnya hari ini ada kejadian apa di fakultas Senpai?"
            nar "Shiori tertawa pelan, suara tawa yang jauh lebih ringan daripada biasanya, lalu menuangkan sisa teh hangat ke dua cangkir."
            shiori "Tadi ada rapat pengurus akademik hampir dua jam penuh. Dan coba tebak apa yang paling lama diperdebatkan oleh sepuluh mahasiswa terbaik di ruangan itu?"
            chiasa "Hmm... anggaran seminar?"
            shiori "Ukuran huruf dan warna bingkai untuk papan pengumuman semester depan."
            shiori "Aku sampai harus menahan diri keras-keras supaya tidak menyarankan kami lempar koin saja."
            chiasa "Hahaha! Dua jam cuma buat bahas ukuran huruf?! Pantas aja Senpai kelihatan capek banget tadi."
            shiori "Belum selesai. Kemarin waktu pulang kampus, Kuroiwa tiba-tiba mampir beli dua dorayaki hangat dari kedai pinggir jalan."
            shiori "Waktu menyodorkannya di mobil, mukanya kaku sekali bilang itu prosedur uji kualitas jajanan lokal. Padahal aku tahu dia cuma khawatir karena aku belum sempat makan siang."
            chiasa "Uwah, Kuroiwa-san manis banget... Biarpun mukanya kelihatan galak, ternyata perhatian banget ya."
            shiori "Fufu, memang begitu orangnya. Oh iya, belakangan ini aku juga lagi baca ulang novel ringan strategi militer tiap bosan baca buku ekonomi."
            shiori "Ilustrasi sampulnya rapi dan berkarakter sekali. Kapan-kapan mau kupinjamkan?"
            chiasa "Eh... novel strategi? Bagian mana yang paling Senpai suka dari gambarnya?"
            shiori "Garis ekspresi karakternya tegas tanpa terlihat berlebihan. Kenapa? Kamu baca seri itu juga?"
            chiasa "A-aku cuma pernah lihat sampulnya di toko buku dekat stasiun kok, Senpai! Kapan-kapan boleh banget dipinjam hehehe."
            shiori "Baik, nanti kubawakan jilid pertamanya. Sekarang giliranmu, ada kejadian lucu apa di studio seni minggu ini?"
            chiasa "Tadi pagi ada temanku yang lupa nutup botol cat biru, terus tumpah pas banget ke atas sepatu putihnya sendiri sebelum penilaian!"
            shiori "Fufufu, itu jelas jauh lebih menegangkan daripada rapat papan pengumuman kami. Lalu sepatunya tetap dipakai waktu penilaian?"
            chiasa "Dipakai dong, Senpai! Malah dibilang ke dosennya kalau itu bagian dari konsep lukisannya."
            shiori "Solusi yang nekat tapi cerdas. Aku suka cara berpikir anak fakultasmu."
            chiasa "Lain kali kalau Senpai habis rapat panjang yang membosankan lagi di gedung fakultas, langsung mampir aja ke sini atau kabari aku."
            shiori "Pasti akan kukabari, Amamiya-san. Rasanya menyenangkan sekali punya seseorang yang bisa diajak menertawakan rapat papan pengumuman."
            nar "Cahaya sore di luar jendela perlahan berubah kemerahan sementara cangkir teh di meja kalian sudah kosong seluruhnya."
            nar "Tanpa perlu menghitung untung rugi maupun langkah pembuka, sebuah persahabatan yang tulus telah terbentuk di antara kalian berdua sore itu."
            nar "Shiori bahkan sempat tertawa kecil ketika menceritakan kembali betapa seriusnya Kuroiwa saat memilih kedai jajanan tradisional di perjalanan pulang."
            nar "Kamu mendengarkan setiap ceritanya dengan santai hingga lampu koridor gedung klub mulai dinyalakan oleh petugas kampus."
            nar "Kalian tetap tinggal di ruangan itu jauh setelah jam klub berakhir, menemukan bahwa pembicaraan biasa tanpa taruhan apa pun ternyata bisa menjadi sesuatu yang ingin ditunggu."
        else:
            yutaka "Tutup aja papannya sekarang, Saionji-san. Kamu tahu sendiri kan aku paling malas sama urusan bisnis keluarga. Kalau kamu belum buru-buru dijemput, duduk aja dulu di sini, kita ngobrol santai."
            nar "Kamu mendorong papan catur sedikit ke tepi meja lalu menyandarkan punggungmu dengan santai. Shiori terdiam sepersekian detik melihat betapa tanpa ragunya kamu menjawab. Perlahan, sebuah senyum kecil yang jauh lebih tulus muncul di sudut bibirnya."
            nar "Ia memasukkan dua bidak terakhir ke kotak beludru, mengaitkan kunci kuningan kotaknya, lalu menarik kursinya kembali mendekat ke meja."
            shiori "Fufu... Terima kasih sudah menjawab lurus begitu, Kisaragi-san. Kalau begitu, aku ingin mencoba sesuatu yang jarang kulakukan."
            yutaka "Mencoba apa memangnya?"
            shiori "Aku ingin cerita hal-hal remeh dari hariku. Kalau kamu mulai bosan, langsung bilang saja. Aku sedang belajar berhenti menebak pikiran orang terus-menerus."
            yutaka "Boleh banget. Memangnya tadi ada kejadian apa di gedung fakultas kita?"
            nar "Shiori tertawa pelan, suara tawa yang jauh lebih ringan daripada biasanya, lalu menuangkan sisa teh hangat ke dua cangkir."
            shiori "Tadi ada rapat pengurus akademik hampir dua jam. Coba tebak apa yang paling lama diperdebatkan oleh sepuluh mahasiswa terbaik di ruangan itu?"
            yutaka "Pembagian dana klub?"
            shiori "Ukuran huruf dan warna bingkai untuk papan pengumuman semester depan."
            shiori "Aku sampai hampir menyarankan mereka lempar koin saja supaya cepat selesai."
            yutaka "Hahaha, khas banget pengurus fakultas kita. Dua jam habis cuma buat ributin ukuran huruf?"
            shiori "Belum selesai. Kemarin waktu pulang, Kuroiwa diam-diam mampir beli dua dorayaki hangat dari kedai pinggir jalan."
            shiori "Waktu menyerahkannya di mobil, mukanya serius sekali bilang itu prosedur uji kualitas jajanan lokal. Padahal jelas-jelas dia cuma khawatir karena aku telat makan siang."
            yutaka "Haha, Kuroiwa-san ternyata ada sisi lucunya juga ya kalau lagi nggak jaga pintu."
            shiori "Fufu, memang begitu orangnya. Oh iya, belakangan ini juga aku suka baca novel ringan strategi tiap penat baca jurnal ekonomi. Agak kekanak-kanakan mungkin, tapi lumayan seru."
            yutaka "Santai aja kali. Aku juga pusing kalau tiap hari cuma lihat kurva pasar. Eh, kalau di kelasku tadi, teman sebangkuku panik seharian gara-gara ngira tugas makalah dikumpulin hari ini, padahal baru bulan depan."
            shiori "Ara, lalu kamu langsung kasih tahu dia atau kamu biarkan dulu?"
            yutaka "Kubiarkan panik dua menit dulu biar kapok nggak baca silabus, baru kukasih tahu."
            shiori "Fufufu, kejam juga kamu, Kisaragi-san... Tapi adil. Setidaknya bulan depan dia bakal rajin baca pengumuman."
            yutaka "Nah, bener kan? Ternyata kalau lagi nggak di depan papan catur, komentar keringmu malah makin lucu."
            shiori "Anggap saja itu bonus karena kamu setuju menemaniku duduk tanpa agenda hari ini."
            yutaka "Kapan pun kamu butuh tempat istirahat dari rapat pengurus yang kaku begitu, panggil aja aku ke ruang klub ini."
            shiori "Akan kuingat janji itu, Kisaragi-san. Jangan mengeluh kalau nanti aku benar-benar sering mengajakmu mengobrol kosong setelah jam kuliah."
            nar "Langit sore di luar jendela mulai meredup saat kalian berdua merapikan cangkir teh yang telah kosong di atas nampan kayu."
            nar "Bagi Shiori, sore ini menjadi bukti nyata bahwa ada seseorang di kampus ini yang bersedia menemaninya tanpa menuntut imbalan apa pun."
            nar "Ia menyusun kembali cangkir porselen ke atas baki dengan raut wajah yang tampak jauh lebih segar dibandingkan saat pertandingan baru selesai tadi."
            nar "Kamu menemaninya merapikan meja hingga lampu lorong gedung mulai menyala menandai berakhirnya jam kegiatan mahasiswa."
            nar "Kalian tetap tinggal di ruangan itu jauh setelah jam klub berakhir, menemukan bahwa pembicaraan biasa tanpa taruhan apa pun ternyata bisa menjadi sesuatu yang ingin ditunggu."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kamu terdiam sebentar menatap dua bidak kayu di tangan Shiori, lalu menjawab dengan nada tenang tanpa berusaha memperhalus maksudmu dengan janji kosong."
            chiasa "Maaf ya, Saionji-senpai. Kalau boleh jujur, aku lebih nyaman kalau kita tetap ketemu sebatas buat main catur di ruang klub ini aja."
            chiasa "Aku nggak terlalu pintar menjaga hubungan pertemanan yang terlalu dekat."
            nar "Tidak ada amarah atau sindiran tajam yang keluar dari wajah Shiori. Ia menatap kotak beludru yang tadi hampir dibiarkannya terbuka sebagai alasan untuk tinggal lebih lama, lalu meletakkan kedua bidak raja itu dengan rapi ke tempatnya dan mengunci kait kuningan kotaknya hingga berbunyi pelan."
            shiori "Terima kasih sudah menjawab dengan jelas, Amamiya-san."
            shiori "Jauh lebih baik mendengar batas yang tegas hari ini daripada melihat seseorang mengiyakan karena sungkan, lalu menjauh diam-diam bulan depan."
            chiasa "Aku nggak bermaksud bikin suasana jadi canggung, Senpai. Aku tetap suka latihan catur di sini, kok."
            shiori "Kamu tidak melakukan kesalahan apa pun. Terus terang, aku memang sedikit kecewa."
            shiori "Tapi anggap saja itu sekadar pengakuan singkat. Sama sekali tidak kumaksudkan supaya kamu mengubah jawabanmu."
            nar "Senyum sopan yang rapi kembali terpasang di bibir Shiori. Ia memasukkan kotak catur ke lemari penyimpanan, mengambil tas selempangnya, lalu mengangguk halus kepadamu."
            shiori "Kalau begitu, sampai jumpa di jadwal latihan berikutnya, Amamiya-san. Aku permisi dulu."
            chiasa "Iya, hati-hati di jalan, Senpai."
            nar "Kamu duduk sendirian selama beberapa saat di ruang klub yang hening sambil memandangi cangkir teh yang masih tersisa separuh."
            nar "Ketulusanmu menolak dengan jujur memang tidak melukai harga dirinya, namun kesempatan untuk mengenalnya lebih dekat telah berakhir di meja ini."
            nar "Suara langkah sepatunya di koridor luar perlahan menjauh hingga tidak lagi terdengar dari balik pintu kayu."
            nar "Pintu ruang klub menutup lembut di belakangnya, menyisakan papan catur yang terlipat rapi di atas meja kayu."
        else:
            nar "Kamu terdiam sebentar menatap dua bidak kayu di tangan Shiori, lalu menjawab dengan nada tenang tanpa berusaha memperhalus maksudmu dengan janji kosong."
            yutaka "Jujur aja, Saionji-san. Aku rasa aku lebih nyaman kalau kita tetap ketemu sebatas buat main catur di ruang klub ini aja."
            yutaka "Aku kurang cocok kalau harus masuk terlalu jauh ke lingkaran pertemanan pribadi."
            nar "Tidak ada amarah atau sindiran tajam yang muncul di wajah Shiori. Ia menatap kotak beludru yang tadi hampir dibiarkannya terbuka sebagai alasan untuk tinggal lebih lama, lalu meletakkan kedua bidak raja itu dengan rapi ke tempatnya dan mengunci kait kuningan kotaknya hingga berbunyi pelan."
            shiori "Terima kasih sudah menjawab dengan jelas, Kisaragi-san."
            shiori "Jauh lebih baik mendengar batas yang tegas hari ini daripada melihat seseorang mengiyakan karena sopan, lalu menghindar diam-diam bulan depan."
            yutaka "Aku nggak bermaksud bikin suasana jadi nggak enak. Buat tanding catur, aku tetap senang datang ke sini."
            shiori "Kamu tidak melakukan kesalahan apa pun. Terus terang, aku memang sedikit kecewa."
            shiori "Tapi anggap saja itu sekadar pengakuan singkat. Sama sekali tidak kumaksudkan supaya kamu mengubah jawabanmu."
            nar "Senyum sopan yang rapi kembali terpasang di bibir Shiori. Ia menyimpan kotak catur ke lemari, mengambil tas selempangnya, lalu mengangguk halus kepadamu."
            shiori "Kalau begitu, sampai jumpa di jadwal latihan berikutnya, Kisaragi-san. Aku permisi dulu."
            yutaka "Oke. Hati-hati di jalan, Saionji-san."
            nar "Kamu memperhatikan punggungnya yang melangkah tegak keluar dari ruangan tanpa sedikit pun menoleh ke belakang."
            nar "Penolakan yang jujur setidaknya menjaga rasa hormat di antara kalian berdua meskipun batas hubungan kalian kini telah terkunci rapat."
            nar "Keheningan sore kembali memenuhi ruang Klub Catur begitu langkah kakinya menghilang di ujung lorong gedung."
            nar "Pintu ruang klub menutup lembut di belakangnya, menyisakan papan catur yang terlipat rapi di atas meja kayu."
    else:
        if kk_host == "chiasa":
            chiasa "Tentu aja aku mau jadi teman Saionji-senpai! Lagian kita kan sudah sering ngobrol di sini."
            chiasa "Oh iya, mumpung Senpai bahas soal kenalan tadi, kapan-kapan boleh nggak kenalin aku ke kolektor atau kurator galeri yang sering datang ke acara keluarga Saionji? Pasti berguna banget buat portofolioku nanti."
            nar "Tepat pada detik kalimatmu selesai, senyum tenang yang tadi begitu jernih di wajah Shiori kembali mengeras menjadi lengkungan sopan yang seragam dan tidak terbaca. Jari-jarinya yang memegang dua bidak raja berhenti sesaat sebelum ia meletakkannya rapi ke dalam kotak."
            shiori "Oh... jadi memang ada orang lain yang ingin kamu temui rupanya, Amamiya-san."
            chiasa "Eh, maksudku kan sekalian aja kalau memang ada acara terbuka, Senpai. Aku tetap senang kok main catur bareng Senpai."
            shiori "Tentu saja. Silakan jelaskan saja jenis kurator atau galeri seperti apa yang sedang kamu incar."
            shiori "Galeri seni kontemporer atau ruang pameran ilustrasi komersial? Aku akan mendengarkannya sampai selesai."
            nar "Ia menyimak seluruh penjelasanmu dengan sikap sangat sopan, mengangguk di tempat yang tepat, lalu menyebutkan dua nama pameran seni terbuka yang biasa disponsori relasi bisnis keluarganya agar kamu bisa mengirim lamaran sendiri."
            chiasa "Wah, makasih banyak infonya, Senpai! Habis ini Senpai mau langsung pulang atau masih mau minum teh sebentar?"
            shiori "Informasi acaranya sudah kusebutkan semua. Silakan dipakai bila memang perlu."
            shiori "Karena waktunya sudah lewat, aku permisi duluan, Amamiya-san."
            chiasa "Eh... iya. Terima kasih banyak ya, Senpai."
            nar "Ia mengunci kotak penyimpanan bidak catur dengan bunyi klik yang tegas sebelum memasukkannya kembali ke rak lemari klub."
            nar "Di matanya, permintaanmu barusan telah menempatkanmu di barisan yang sama dengan orang-orang yang hanya mendekatinya demi koneksi keluarga."
            nar "Kamu hanya bisa menatap pintu ruangan yang tertutup sambil menyadari bahwa kepercayaan pribadi Shiori tidak bisa lagi kamu raih dengan mudah."
            nar "Shiori sudah berdiri merapikan kursi dan meraih tasnya. Keramahan formalnya tetap utuh sampai pintu ruang klub tertutup, tetapi tawaran persahabatan yang beberapa menit lalu baru saja ia buka kini lenyap sepenuhnya dan tidak lagi ia ulang dalam bentuk apa pun."
        else:
            yutaka "Tentu aja aku mau jadi temanmu, Saionji-san. Lagian kita kan juga satu fakultas."
            yutaka "Oh iya, mumpung kamu menyinggung soal lingkaran kenalan tadi, kapan-kapan boleh nggak kenalin aku ke eksekutif divisi logistik di acara keluarga Saionji? Orang tuaku bilang kenalan di sana bakal berguna buat jalur distribusiku nanti."
            nar "Tepat pada detik kalimatmu selesai, sorot tenang yang tadi begitu jernih di wajah Shiori kembali mengeras menjadi lengkungan sopan yang seragam dan tidak terbaca. Jari-jarinya yang memegang dua bidak raja berhenti sesaat sebelum ia meletakkannya rapi ke dalam kotak."
            shiori "Oh... jadi memang ada orang lain yang ingin kamu temui rupanya, Kisaragi-san."
            yutaka "Maksudku kan sekalian aja kalau memang ada acara bisnis terbuka. Aku tetap senang kok duduk ngobrol sama kamu."
            shiori "Tentu saja. Silakan sebutkan saja bidang distribusi atau nama divisi mana yang sedang dicari keluargamu."
            shiori "Logistik maritim atau jaringan ritel domestik? Aku akan mendengarkannya sampai selesai."
            nar "Ia menyimak seluruh penjelasanmu dengan kesopanan sempurna, mengangguk di tempat yang tepat, lalu menyebutkan dua jadwal forum ekonomi terbuka yang biasa dihadiri mitra perusahaan keluarganya agar kamu bisa mengurus pendaftarannya sendiri."
            yutaka "Makasih infonya, Saionji-san. Oh ya, tehnya masih ada tuh, kamu belum buru-buru kan?"
            shiori "Jadwal forumnya sudah kusebutkan semua. Silakan dipakai bila memang perlu."
            shiori "Karena waktunya sudah lewat, aku permisi duluan, Kisaragi-san."
            yutaka "Oke... makasih waktunya, Saionji-san."
            nar "Ia menutup pengait kuningan kotak catur itu dengan gerakan jari yang rapi lalu menyimpannya kembali ke dalam lemari kayu."
            nar "Permintaan koneksi bisnis yang kamu selipkan barusan langsung membuktikan kekhawatirannya bahwa hampir semua orang mendekatinya dengan tujuan tersembunyi."
            nar "Meskipun kamu mendapatkan informasi forum yang kamu tanyakan, pintu menuju kepercayaan tulus Shiori telah tertutup rapat sore itu."
            nar "Shiori berdiri merapikan kursi dan mengambil tasnya. Keramahan formalnya tetap utuh sampai pintu ruang klub tertutup, tetapi tawaran persahabatan yang beberapa menit lalu baru saja ia ulurkan kini lenyap sepenuhnya dan tidak lagi ia ulang dalam bentuk apa pun."
    return

# ┌─ PANDUAN CERITA · S-D04 · Pertanyaan Jebakan
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : daftar_kebohongan ≥ 1
# │ INTI    : A Jujur sekarang / B bohong lebih rapi / C alihkan
# │ AKHIRAN : jujur sekarang lebih murah; bohong yang ketahuan belakangan dihitung dua kali
# └─ tulis / perbaiki dialog di bawah ──
label kk_shiori_question:
    nar "Suasana di sekitar kalian sedang cukup lengang ketika Shiori menutup buku catatannya perlahan dan menoleh penuh ke arahmu. Tatapannya tenang tanpa sedikit pun nada menuduh, persis cara seseorang mengetuk pintu sebelum benar-benar membukanya."
    if any(c["ev"] == "C11" and c["key"] == "B" for c in choices_log):
        shiori "Amamiya-san, waktu kita melihat ilustrasi sampul di pameran kemarin, kamu sempat kelihatan seperti hendak mengatakan sesuatu tentang Shena lalu berhenti. Apa aku salah baca situasi?"
    else:
        if kk_host == "chiasa":
            shiori "Amamiya-san, aku masih memikirkan ceritamu kemarin. Ada bagian yang sepertinya sengaja belum kamu ceritakan sampai tuntas?"
        else:
            shiori "Kisaragi-san, aku sempat mengingat ulang penjelasanmu kemarin. Ada bagian yang belum kamu ceritakan secara utuh?"
    nar "Pertanyaannya sama sekali tidak membocorkan seberapa banyak yang sebenarnya sudah ia ketahui. Ia sedang memberimu satu kesempatan bersih untuk meluruskan bagian yang sempat kamu simpan tanpa perlu lebih dulu menggelar bukti di atas meja."
    call kk_family_menu("S-D04", ["Ceritakan bagian yang sengaja kamu lewatkan.", "Susun alasan lain agar ceritamu terdengar cocok.", "Balik bertanya tentang buku yang ia baca."])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "...Maaf, Saionji-senpai. Kemarin aku memang menahan sebagian ceritanya karena panik takut bakal jadi masalah besar. Ini bagian yang sebenarnya belum kubilang..."
        else:
            yutaka "...Jujur saja, Saionji-san, kemarin memang ada bagian yang sengaja nggak kusebut karena kupikir lebih aman disimpan sendiri. Begini kenyataannya..."
        nar "Kamu menjelaskan bagian yang sempat tertahan itu dengan terbuka. Shiori mendengarkan tanpa memotong, lalu mengangguk tipis."
        shiori "Aku senang mendengarnya langsung darimu sendiri sebelum kita harus ribut mencari bukti. Aku belum bisa langsung bilang seluruh keraguanku selesai hari ini, tapi kesediaanmu bicara lebih dulu memberiku alasan kuat untuk tetap duduk di percakapan ini."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Nggak ada yang kusembunyikan kok, Saionji-senpai. Kemarin aku cuma agak salah ingat urutan waktunya aja karena lagi banyak tugas studio."
        else:
            yutaka "Nggak ada bagian yang terlewat kok, Saionji-san. Mungkin kemarin kalimatku aja yang kurang runtut jadi kedengaran janggal."
        nar "Shiori menatap matamu lurus selama dua detik, lalu mengulang satu kalimat alasanmu barusan dengan susunan kata yang persis sama."
        shiori "Baik. Aku sengaja mengulangnya supaya aku bisa mengingat jawabanmu dengan sangat akurat. Jadi kalau suatu hari kita perlu membahas ini lagi, kita nggak usah berdebat soal kata apa yang sebenarnya kamu pakai."
    else:
        if kk_host == "chiasa":
            chiasa "Oh iya, ngomong-ngomong buku yang lagi Saionji-senpai pegang itu novel strategi jilid barunya ya? Sudah sampai bab mana?"
        else:
            yutaka "Ngomong-ngomong, buku yang dari tadi kamu bawa itu kayaknya tebal banget, Saionji-san. Itu bacaan kuliah atau novel?"
        nar "Shiori menjawab pertanyaanmu tentang bukunya dengan sangat sopan dan terperinci selama beberapa kalimat, lalu menutup kembali sampulnya."
        shiori "Ceritanya memang menarik. Tapi perlu kamu tahu, pertanyaanku yang pertama tadi belum hilang hanya karena aku bersedia mengikuti sopan santunmu mengganti topik."
    return

# ┌─ PANDUAN CERITA · S14 · Natal Kedua: Senyum yang Sama
# │ LOKASI  : Distrik Elite · Rumah Saionji
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia tidak marah dan tidak menjauh; ia tersenyum persis seperti biasa.
# │ INTI    : A minta maaf / B menyalahkan / C menghindar.
# │ AKHIRAN : stage 3.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S14:
    call kk_scene_enter("shiori","Natal kedua di rumah Saionji")
    if kk_host == "chiasa":
        nar "Udara malam dua puluh empat Desember di Distrik Elite terasa jauh lebih tenang dan dingin dibandingkan kawasan stasiun yang ramai oleh lampu belanja. Deretan lampu taman berwarna emas hangat menyala teratur di balik pagar besi tinggi Rumah Saionji, memantul tipis pada embun beku di daun cemara."
        nar "Kamu menenteng sekotak kecil kue kering jahe berpita merah marun sambil menekan tombol interkom di sisi gerbang. Tidak sampai setengah menit, daun gerbang besi bergeser perlahan tanpa suara keras, dan Kuroiwa berdiri menyambutmu dengan mantel hitam rapi serta payung terlipat di tangannya."
        "Kuroiwa" "Selamat malam, Amamiya-san. Terima kasih sudah datang di malam yang dingin seperti ini. Mari saya antarkan langsung menuju serambi utama."
        chiasa "Selamat malam, Kuroiwa-san. Maaf merepotkan di malam Natal begini. Saionji-senpai sudah di ruang tamu?"
        nar "Langkah kalian berdua menimbulkan bunyi halus di atas kerikil halaman yang dingin oleh embun Desember. Kamu sempat menoleh singkat pada Kuroiwa yang memegang payung lipat dengan sangat rapi di sisi tubuhnya."
        chiasa "Belakangan ini Kuroiwa-san sibuk mengantar Saionji-senpai ke banyak acara akhir tahun ya?"
        "Kuroiwa" "Justru sebaliknya, Amamiya-san. Sepanjang bulan Desember ini Nona Shiori membatalkan hampir semua undangan resital musik dan lebih banyak menghabiskan sore dengan membaca berkas di ruang belajar."
        nar "Kamu melangkah di sampingnya menyusuri jalan batu halaman yang bersih. Untuk sesaat, kamu menangkap sesuatu yang tidak biasa pada pengawal keluarga Saionji itu. Langkahnya tetap tenang dan sikapnya tetap nyaris tanpa cela, tetapi matanya melirik ke arah jendela ruang duduk lantai satu dengan sorot resah yang amat samar."
        "Kuroiwa" "Nona Shiori sudah menyeduh teh sendiri sejak satu jam yang lalu sambil menata papan catur di ruang duduk, Amamiya-san."
        "Kuroiwa" "Jika saya boleh menyampaikan satu pesan kecil sebelum kita sampai di pintu... sepanjang minggu ini Nona Shiori sama sekali tidak pernah meninggikan suara ataupun tampak kesal di rumah. Justru ketenangan yang serapi itu yang membuat saya sedikit khawatir. Tolong pilih kata-kata Anda dengan cermat malam ini."
        chiasa "Kuroiwa-san... maksudnya Saionji-senpai masih menyimpan soal bulan kemarin ya?"
        "Kuroiwa" "Bukan wewenang saya menilai isi pikiran Nona, Amamiya-san. Saya hanya tahu beliau tidak pernah melupakan urutan langkah yang sudah sempat dicatat."
        nar "Sebelum kamu sempat bertanya lebih jauh, pintu kayu berat serambi utama terbuka lebar memancarkan cahaya hangat, aroma kayu manis panggang, dan musik piano pelan dari ruang makan keluarga. Ibu Shiori melangkah keluar menyambutmu dengan senyum tulus dan hangat khas keluarga Saionji."
        "Ibu Shiori" "Ya ampun, Amamiya-san! Selamat Natal! Ayo cepat masuk, pipimu sampai merah kena angin Desember di luar. Terima kasih banyak ya sudah mau mampir menemani Shiori malam ini."
        chiasa "Selamat Natal, Oba-san. Ini saya bawa sedikit kue kering buat keluarga di rumah, maaf cuma bingkisan sederhana."
        "Ibu Shiori" "Aduh, repot-repot segala! Pitanya juga dibungkus rapi sekali, pasti kue jahenya enak buat teman minum teh nanti. Di rumahmu Koita-kun yang memasak makan malam Natal tahun ini?"
        chiasa "Iya, Oba-san, Ko-nii sudah mulai memanggang ayam dari sore tadi sebelum saya berangkat ke sini."
        "Ibu Shiori" "Wah, rajin sekali kakakmu itu! Suamiku masih menerima telepon dari kerabat di Kyoto di ruang kerja, nanti sebentar lagi juga bergabung di ruang makan buat makan malam panggang bersama. Oh iya, kudengar dari Shiori bulan kemarin pameran Fakultas Seni Rupa ramai sekali ya? Orang tuamu juga sehat di rumah?"
        chiasa "Puji syukur sehat semua, Oba-san. Pamerannya juga berjalan lancar kok bulan kemarin."
        "Ibu Shiori" "Bagus sekali kalau begitu! Ini sandal rumah berlapis wol biar kakimu cepat hangat. Syal merah marun yang kamu pakai juga cocok sekali dengan warna matamu. Sudah, cepat lepas mantelmu biar Kuroiwa bantu gantungkan, Shiori sudah menunggumu di ruang duduk sebelah taman belakang."
        nar "Kamu mengenakan sandal rumah yang lembut itu sambil mengucapkan terima kasih. Keramahan tulus ibu Shiori terasa begitu hangat dan wajar, persis seperti rumah keluarga yang sungguh-sungguh menyayangi putri mereka dan menyambut teman-temannya tanpa sikap angkuh sedikit pun."
        nar "Di ambang pintu ruang duduk yang bersebelahan dengan beranda kaca, Saionji Shiori sudah berdiri menyambut kedatanganmu. Ia mengenakan gaun musim dingin berlengan panjang berwarna plum tua yang sangat rapi. Rambut putih keperakannya yang panjang bergelombang berhiasan mutiara ungu-emas tersusun anggun membingkai wajahnya."
        nar "Yang paling membuat jantungmu berdegup pelan adalah ekspresinya. Ia sama sekali tidak memasang wajah marah, dingin, ataupun menjauh. Di bibirnya terpasang senyum lembut yang persis sama dengan senyum yang kamu bawa dalam begitu banyak kenangan baik sepanjang dua tahun ini."
        if kk_has("shiori_teman_dipercaya"):
            shiori "Dulu kamu mau duduk denganku bahkan setelah ruang Klub Catur tutup dan lorong gedung sudah gelap, Amamiya-san. Malam ini juga masih ada satu kursi kosong di depan papan."
        else:
            shiori "Masuklah sebentar, Amamiya-san. Di luar dingin sekali, tidak baik berdiri terlalu lama di serambi."
        chiasa "Terima kasih, Saionji-senpai. Selamat Natal ya."
        shiori "Selamat Natal juga, Amamiya-san. Ibu, aku ajak Amamiya-san duduk sebentar di ruang duduk dulu ya sebelum makan malam keluarga dimulai."
        "Ibu Shiori" "Iya, silakan, Shiori. Ibu siapkan dulu piring buah dan kue dari Amamiya-san di ruang makan. Santai saja ya, Amamiya-san, anggap seperti rumah sendiri."
        nar "Keluarganya tetap sehangat dan sesantun dulu. Hanya jarak pribadi Shiori saat memersilakanmu masuk yang terasa jauh lebih rapi, seolah setiap celah kedekatan di antara kalian kini tidak lagi terbuka secara alami dan harus sengaja ia berikan satu per satu."
        nar "Di dalam ruang duduk yang diterangi perapian kecil, papan catur kayu di atas meja bundar sudah terisi penuh dengan bidak yang tertata rapi pada posisi awal. Di sebelahnya tersedia dua cangkir teh earl grey yang mengepul harum, dua piring kecil biskuit kayu manis, serta satu buah buku catatan tipis bersampul biru tua yang tertutup tenang di bawah tatakan porselen."
        if kk_has("shiori_menemukan_kebohongan_shena"):
            nar "Tepat di samping buku catatan itu terselip sebuah pembatas kertas penerbit novel yang sama dengan yang pernah ia bawa ke ruang Klub Catur bulan November kemarin. Shiori menyentuh tepi pembatas kertas itu satu detik sambil menuangkan teh, seolah mengingatkanmu dengan sangat halus tanpa perlu menyebut satu nama pun."
        nar "Saat kamu duduk di kursi seberangnya, pandanganmu sempat jatuh sekilas pada deretan bidak putih dan hitam yang masih berdiri utuh tanpa satu pun langkah dimulai. Shiori langsung menangkap arah tatapanmu dan tersenyum ringan."
        shiori "Jangan khawatir, aku tidak sedang menantangmu bertanding malam ini, Amamiya-san. Aku hanya suka melihat posisi pembukaan yang masih utuh. Dalam permainan klasik, kadang dua pemain sengaja duduk cukup lama di depan papan yang rapi sekadar untuk melihat siapa yang akhirnya memilih langkah jujur duluan."
        chiasa "Saionji-senpai memang selalu bisa menyambungkan apa saja ke papan catur ya..."
        shiori "Fufu, kebiasaan lama memang susah hilang. Silakan diminum tehnya selagi hangat, Amamiya-san. Aku pakai daun earl grey yang biasa kita minum waktu latihan sore di klub. Ambil juga biskuit kayu manisnya, Ibu baru memanggangnya satu jam lalu."
        nar "Ia menggeser piring kecil biskuit porselen itu sedikit lebih dekat ke arah sikumu sambil menuangkan cairan teh keemasan yang harum. Tidak ada satu pun tetes berceceran di atas taplak renda."
        chiasa "Terima kasih, Saionji-senpai. Minggu terakhir sebelum kampus libur kemarin suasana lorong klub sudah sepi banget ya."
        shiori "Memang sepi sekali, cocok buat membereskan catatan akhir tahun. Bagaimana persiapan liburan Natal di rumahmu bersama Koita-kun?"
        chiasa "Lumayan hangat kok, Senpai. Di rumah kami bikin masakan sederhana sama menata pohon Natal kecil."
        shiori "Syukurlah. Keluarga memang selalu jadi tempat pulang paling nyaman di akhir tahun."
        nar "Kamu sempat melirik keluar kaca beranda tempat lampu taman keemasan menyinari rumpun kamelia musim dingin yang daunnya tertutup embun tipis."
        chiasa "Taman belakang rumah Senpai malam ini kelihatan tenang banget ya di bawah lampu."
        shiori "Memang selalu begitu setiap akhir Desember, Amamiya-san. Hening, rapi, dan tidak ada satu pun daun yang bergeser tanpa terlihat dari ruang duduk ini."
        nar "Kalimat ringan itu meluncur halus sekali tanpa nada mengancam, tetapi seketika membuat hangat cangkir porselen di telapak tanganmu terasa berkurang separuh."
        nar "Ia duduk tegak di kursi seberangmu, kedua tangannya terlipat anggun di atas lutut. Tatapan mata ungu ametisnya sangat tenang, begitu ramah dan tak terburu-buru sampai justru membuat udara di sekitar perapian terasa setipis kaca."
        shiori "Aku senang kamu datang memenuhi undangan Ibu malam ini, Amamiya-san. Kamu sendiri bagaimana? Setelah pertemuan terakhir kita di ruang klub bulan lalu, apa ada sesuatu yang ingin kamu sampaikan mumpung kita sedang duduk berdua sebelum makan malam?"
        chiasa "{i}Ia tidak marah. Ia tidak menyindir. Ia tersenyum persis seperti biasa dan meletakkan seluruh pilihan di depanku seolah langkah berikutnya sepenuhnya milikku.{/i}"
        call kk_family_menu("S14", ["\"Aku datang untuk minta maaf soal jawabanku bulan lalu, Saionji-senpai.\"", "\"Aku tahu aku salah, tapi cara Senpai menekan kemarin juga bikin keadaan makin sulit.\"", "\"Nggak ada hal berat kok, Senpai. Aku cuma mau mengucapkan selamat Natal.\""])
        if _return == "A":
            nar "Kamu meletakkan cangkir tehmu kembali ke tatakan porselen dengan pelan, menarik napas dalam di bawah tatapan ungu ametisnya yang tenang, lalu menundukkan kepala dengan sungguh-sungguh."
            chiasa "Ada, Saionji-senpai. Aku datang malam ini karena aku mau minta maaf secara langsung soal jawabanku di ruang klub bulan kemarin."
            nar "Senyum sopan Shiori tidak berubah sedikit pun, tetapi ujung jarinya berhenti mengetuk pegangan cangkir. Ia memiringkan kepalanya sedikit menyimak."
            shiori "Aku dengar, Amamiya-san. Terima kasih sudah mau datang mengucapkannya sendiri."
            chiasa "Aku tahu waktu itu keadaannya memang serba rumit dan aku keburu panik di depan Senpai..."
            shiori "Sebentar, Amamiya-san."
            nar "Suaranya lembut sekali, nyaris tanpa nada teguran, tetapi langsung menghentikan kalimatmu tepat di tengah jalan."
            shiori "Kalau kamu sungguh-sungguh datang untuk meminta maaf, jangan merangkum semuanya sebagai keadaan yang rumit. Aku ingin dengar kamu menyebut bagian spesifik mana yang kamu sesali dari keputusanmu sendiri."
            nar "Kamu terdiam dua detik merasakan betapa tepatnya sasaran ucapannya. Kamu mengangkat wajahmu menatap mata Shiori lurus tanpa mencari alasan pelindung lagi."
            if kk_has("shiori_menemukan_kebohongan_shena"):
                chiasa "Aku menyesal karena waktu di pameran dan di ruang klub aku sengaja berbohong soal Shena dan catatan arsip pameran, Saionji-senpai. Aku memilih melindungi egoku sendiri dan meremehkan kepercayaan yang sudah Senpai kasih."
            else:
                chiasa "Aku menyesal karena aku sengaja membelokkan cerita dan menghindar waktu Senpai sudah memberi ruang bicara baik-baik di ruang klub. Aku membiarkan rasa takutku mengalahkan kejujuran ke Senpai."
            chiasa "Aku nggak berharap satu permintaan maaf malam ini langsung bikin semuanya balik seperti dulu. Aku cuma nggak mau melewati malam Natal dengan pura-pura bulan kemarin nggak pernah terjadi."
            nar "Shiori mendengarkan seluruh kalimatmu dari awal sampai akhir tanpa memotong. Untuk sesaat, sorot tenang di matanya yang selama beberapa minggu terakhir terasa tertutup rapi tampak sedikit bergeser, memberi ruang kecil untuk menimbang kejujuranmu."
            shiori "Baik. Aku mencatat perbedaan antara orang yang sekadar ingin segera dimaafkan dengan orang yang mau mengakui langkah kelirunya satu per satu."
            shiori "Satu pertanyaan terakhir sebelum kita masuk ke ruang makan, Amamiya-san. Jika bulan depan ada orang lain di kampus yang kembali menanyakan versi lama ceritamu itu, apa yang akan kamu lakukan?"
            chiasa "Aku nggak bakal mengulang alasan palsu yang sama lagi, Senpai. Kalau aku memang belum sanggup cerita ke mereka, aku bakal bilang aku nggak mau membahasnya, atau aku luruskan bagian yang keliru tanpa mengarang cerita baru."
            nar "Shiori menatap matamu lama sekali, lalu mengulurkan satu jari rampingnya ke papan catur di tengah meja dan menggeser satu bidak pion putih maju satu petak kecil dengan bunyi ketukan kayu yang halus."
            chiasa "Kenapa Senpai memajukan pion putih satu petak?"
            shiori "Dalam catur, putih melangkah pertama hanya ketika kedua pemain sepakat masih mau duduk di meja yang sama, Amamiya-san. Kalau aku sudah selesai denganmu, papan ini sudah kusimpan kembali ke dalam kotaknya sejak awal."
            shiori "Aku tidak akan mengatakan urusan kita sudah selesai malam ini, Amamiya-san. Beberapa hal masih perlu kulihat sendiri buktinya lewat tindakanmu di bulan-bulan berikutnya, terutama saat kampus ramai lagi bulan Januari dan orang-orang mulai kembali bertanya."
            chiasa "Aku mengerti, Saionji-senpai. Aku nggak bakal minta Senpai langsung percaya malam ini juga, dan aku bakal pegang janjiku pas masuk semester baru nanti."
            shiori "Bagus kalau kita sepakat di bagian itu. Sekarang habiskan tehmu dulu, lalu mari kita masuk ke ruang makan. Ibu pasti sudah menyiapkan potongan pai apel hangat untukmu."
            nar "Ia bangkit dengan gerak anggun, membiarkan satu pion putih yang baru saja maju itu berdiri di papan sebagai tanda bahwa percakapan di antara kalian belum dimatikan sepenuhnya. Senyumnya kini tidak sehangat tahun lalu, tetapi setidaknya kamu akhirnya menginjak tanah yang jujur di hadapannya."
            nar "Begitu pintu ruang makan dibuka, cahaya lilin panjang dan aroma pai apel hangat langsung menyambut kalian. Ibu Shiori menoleh dengan wajah berseri mempersilakan kamu duduk di sebelah Shiori."
            "Ibu Shiori" "Nah, ini dia dua anak rajin kita! Ayo duduk dulu, sup labunya baru saja diangkat dari dapur."
            shiori "Terima kasih, Ibu. Amamiya-san, silakan duduk duluan."
            nar "Shiori menarik pelan kursi kayu berlapis beludru di sebelah tempat duduknya sendiri untukmu sebelum sempat pelayan rumah mendekat. Saat kamu duduk, ia menunduk seperempat kepala cukup dekat agar suaranya hanya terdengar olehmu di sela denting sendok sup."
            shiori "Nikmati pai apel buatan Ibu malam ini, Amamiya-san. Setidaknya malam ini kamu sudah memilih berbicara jauh lebih jujur daripada saat di ruang klub kemarin."
            chiasa "...Terima kasih, Saionji-senpai."
            nar "Tak lama kemudian, ayah Shiori melangkah masuk dari ruang kerja sambil menyapa ramah dari ujung meja panjang, lalu menuangkan sari buah hangat ke setiap gelas dengan tawa tenang yang langsung mengisi seluruh ruang makan."
            "Ayah Shiori" "Selamat Natal, Amamiya-san. Terima kasih sudah datang meramaikan meja kami malam ini."
            chiasa "Selamat Natal, Oji-san. Terima kasih banyak sudah mengundang saya."
            nar "Saat kalian duduk berdampingan di ruang makan yang hangat itu, kamu sadar pintu di antara kalian masih belum terbuka lebar, sementara satu ujian panjang baru saja dimulai dari kejujuranmu malam ini."
        elif _return == "B":
            nar "Kamu menatap buku catatan biru tua di samping tatakan teh itu, merasakan ketegangan sepanjang sebulan terakhir menumpuk di tenggorokanmu, lalu memutuskan untuk tidak menanggung seluruh kesalahan sendirian."
            chiasa "Jujur saja, Saionji-senpai... aku tahu jawabanku bulan lalu nggak rapi. Tapi cara Senpai mengumpulkan catatan diam-diam lalu langsung menyodorkannya di ruang klub yang tertutup juga bikin keadaan jadi jauh lebih sulit buat bicara jujur."
            chiasa "Kalau Senpai memang menganggapku teman, harusnya Senpai tahu ditekan kayak terdakwa di depan meja catur itu bikin siapa pun refleks bertahan diri."
            nar "Suasana ruang duduk langsung menegang setipis benang. Meski begitu, Shiori sama sekali tidak mengerutkan kening ataupun menaikkan suaranya. Ia mendengarkan kalimatmu sampai selesai dengan kedua tangan masih terlipat rapi di pangkuan."
            shiori "Menarik sekali sudut pandangmu, Amamiya-san. Boleh aku mengajukan satu pertanyaan kecil untuk memastikan aku tidak salah menangkap maksudmu?"
            chiasa "Silakan, Senpai."
            shiori "Kamu menyebut caraku bertanya membuat keadaan menjadi sulit. Aku ingin tahu, apakah kesulitan itu kamu pakai untuk menjelaskan alasanmu gugup, atau kamu pakai untuk membatalkan tanggung jawabmu atas cerita yang tidak benar?"
            chiasa "Aku nggak bilang aku nggak salah, Senpai! Maksudku dua belah pihak sama-sama bikin situasinya makin rumit."
            shiori "Aku bisa saja punya bagian salah karena terlalu teliti menyimpan catatan dan terlalu menuntut kejujuran dari orang yang kupercaya, Amamiya-san."
            shiori "Akan tetapi, kesalahan caraku bertanya sama sekali tidak membuat dua cerita yang saling bertentangan mendadak berubah menjadi sama-sama benar."
            nar "Kalimat itu jatuh dengan kejernihan dingin yang membuatmu kehilangan kata balasan. Di luar jendela kaca, bayangan Kuroiwa tampak melintas singkat memeriksa pintu taman sebelum kembali ke posnya."
            nar "Kamu melirik buku catatan biru tua di samping tatakan porselen itu, tidak sanggup lagi menahan pertanyaan yang sejak tadi berputar di kepalamu."
            chiasa "Saionji-senpai... catatan yang Senpai kumpulkan di buku biru itu, apa Senpai sudah menunjukkannya ke orang lain di kampus atau ke Miono?"
            nar "Shiori mengangkat pandangan mata ungu ametisnya dengan senyum tipis yang tenang sekali. Ujung jarinya menyentuh sampul biru itu tanpa sedikit pun ketergesaan."
            shiori "Aku belum menunjukkan apa pun kepada siapa pun, Amamiya-san. Dalam catur, pemain yang ceroboh selalu terburu-buru mengeluarkan bidak terkuatnya sebelum seluruh petak di papan terisi lengkap."
            chiasa "Jadi Senpai mengundangku datang ke rumah malam Natal ini cuma buat menguji reaksiku di depan buku catatan itu?"
            nar "Shiori menggeleng sangat halus dengan senyum yang sama ramahnya seperti saat menyambutmu di teras tadi."
            shiori "Sama sekali tidak, Amamiya-san. Ibu memang sungguh-sungguh senang mengundang teman dekatku ke meja makan Natal. Lagipula aku tidak perlu repot menguji seseorang yang sudah menjelaskan posisinya sendiri dengan sejelas tadi."
            nar "Api kecil di perapian berderak halus memantulkan cahaya keemasan di mata ungu ametisnya. Kamu langsung menyadari betapa mustahilnya menggoyahkan ketenangan Shiori begitu ia sudah memutuskan menempatkanmu di seberang papan."
            chiasa "{i}Ia sama sekali tidak terpancing marah... justru setiap kali aku mencoba membela diri, aku seperti baru saja menyerahkan satu bidak lagi ke tangannya.{/i}"
            nar "Shiori menyesap teh earl grey miliknya satu teguk tenang, lalu meletakkan cangkirnya kembali tepat di tengah tatakan tanpa menimbulkan bunyi."
            shiori "Terima kasih sudah mengatakan isi pikiranmu dengan terang-terangan malam ini. Setidaknya sekarang aku tahu persis di mana kamu meletakkan batas tanggung jawabmu sendiri."
            chiasa "Saionji-senpai... kamu nggak berniat membicarakan ini lebih panjang?"
            shiori "Malam Natal adalah malam keluarga, tidak sopan jika kita membuat Ibu menunggu terlalu lama di ruang makan karena debat yang sudah jelas arahnya. Mari kita pindah ke meja makan sebentar supaya kue jahemu bisa dicicipi Ibu."
            nar "Di ruang makan yang hangat oleh cahaya lilin, Ibu Shiori kembali bercerita ceria tentang rencana Tahun Baru mereka sambil memotong pai apel. Di sampingmu, Shiori tertawa lembut menanggapi cerita ibunya seolah ruang duduk lima menit lalu tidak pernah ada."
            "Ibu Shiori" "Amamiya-san mau tambah potongan pai apel satu lagi? Masih hangat lho baru keluar dari oven."
            chiasa "Terima kasih banyak, Oba-san, tapi porsi yang tadi sudah cukup banget buat saya."
            shiori "Benar, Ibu, tadi di ruang duduk Amamiya-san juga sudah mencicipi teh earl grey dan biskuit kayu manis. Nanti kekenyangan sebelum pulang."
            nar "Ia tersenyum persis seperti ketika menyambutmu di serambi tadi. Tidak ada sedikit pun retakan pada sopan santunnya, tetapi kamu merasakan dinginnya musim dingin yang sesungguhnya baru saja turun menutup ruang duduk itu."
            chiasa "{i}Senyumnya nggak berubah satu milimeter pun... tapi rasanya aku baru saja mengonfirmasi semua kesimpulan terburuk yang sudah ia tulis di dalam buku catatan birunya.{/i}"
            nar "Satu jam kemudian di serambi depan, Kuroiwa menyerahkan mantelmu dalam keheningan yang begitu canggung lalu mengiringimu keluar melewati halaman batu yang membeku."
            "Kuroiwa" "Hati-hati di jalan pulang, Amamiya-san. Udara malam ini makin turun suhunya."
            chiasa "Terima kasih, Kuroiwa-san. Permisi."
            nar "Sepanjang sisa kunjungan itu, percakapan di ruang makan berjalan seramah jamuan resmi tanpa celah. Namun saat gerbang besi Rumah Saionji akhirnya menutup di belakangmu, kamu tahu babak percakapan baik-baik dengan Shiori baru saja bergeser ke fase yang jauh lebih berbahaya."
        else:
            nar "Kamu menatap senyum rapi Shiori yang tidak memberi petunjuk sedikit pun tentang isi buku catatan biru di sebelahnya, lalu memutuskan untuk tidak membuka luka lama di malam Natal."
            chiasa "Nggak ada hal berat yang perlu dibahas kok, Saionji-senpai. Aku datang malam ini cuma mau mengucapkan selamat Natal ke Senpai sama keluarga, sekalian mengantar kue jahe tadi."
            nar "Shiori menatap matamu dua detik penuh. Tidak ada raut kecewa ataupun sinis melintas di wajahnya; sudut bibirnya justru terangkat dengan keluwesan sempurna seorang tuan rumah yang terlatih."
            shiori "Begitu, ya. Terima kasih banyak atas perhatianmu, Amamiya-san. Ibu pasti senang sekali tahu kamu masih menyempatkan datang di tengah jadwal liburan akhir tahun."
            chiasa "Cuaca bulan Desember ini memang dingin banget ya, Senpai. Di stasiun tadi lampu-lampu hiasannya sudah ramai banget."
            shiori "Benar. Semalam Kuroiwa juga bilang jalan utama Distrik Elite sempat padat oleh rombongan keluarga yang mencari kue Natal."
            nar "Kamu menyesap teh earl grey yang terasa hangat dan harum di tenggorokan, mencoba meyakinkan dirimu sendiri bahwa mungkin memang lebih baik melewati malam ini dengan damai. Namun setiap jeda tiga detik di antara obrolan cuaca dan liburan, kehadiran buku catatan biru di meja samping terasa semakin berat."
            shiori "Bagaimana proyek tugas akhir semester di Fakultas Seni Rupa? Kudengar tahun kedua biasanya mulai banyak tenggat penilaian studio."
            chiasa "Lumayan padat, Senpai, tapi untungnya semua sketsa dasarku sudah sempat kukumpulkan sebelum libur."
            shiori "Dan Koita-kun juga sehat selama musim dingin ini? Aku belum sempat menyapanya lagi sejak rapat kegiatan kampus bulan lalu."
            chiasa "Ko-nii sehat kok, Senpai. Dia juga tadi sempat titip salam selamat Natal buat Senpai."
            shiori "Baguslah. Sampaikan salam balikku kepadanya. Jaga kesehatanmu baik-baik selama liburan ini, Amamiya-san. Jangan sampai kelelahan saat semester baru mulai Januari nanti."
            chiasa "Perapian di ruang duduk ini hangat banget ya, Senpai, sampai lupa di luar angin Desembernya sedingin itu."
            shiori "Rumah kayu tua memang bisa tetap hangat sepanjang musim dingin, Amamiya-san, selama semua jendelanya ditutup rapat dan tidak ada celah yang dibiarkan terbuka sembarangan."
            nar "Kamu sempat terdiam menelan ludah mendengar perumpamaan halus yang jatuh begitu ringan di antara denting kecil sendok porselen. Tepat saat keheningan itu mulai terasa terlalu panjang, suara ketukan ceria terdengar dari pintu ruang duduk."
            nar "Tak lama kemudian, Ibu Shiori mengetuk bingkai pintu ruang duduk dengan ceria mengundang kalian berdua bergabung ke ruang makan. Shiori menemanimu duduk di meja panjang, menuangkan teh hangat, dan memuji rasa kue jahe bawaanmu dengan kehangatan yang tepat untuk seorang tamu kehormatan."
            "Ibu Shiori" "Wah, manisnya cocok sekali, Amamiya-san! Nanti sebelum pulang bawa satu kaleng daun teh Ceylon ini buat orang tuamu di rumah ya, anggap saja balasan dari Ibu. Shiori itu biasanya jarang sekali mengajak teman dari kampus mampir ke rumah pas malam Natal, jadi Ibu senang sekali melihat kalian tetap akrab sampai tahun kedua ini."
            shiori "Tentu saja, Ibu. Amamiya-san selalu jadi teman mengobrol yang menarik di kampus."
            chiasa "Terima kasih banyak, Oba-san. Saya jadi merasa merepotkan sekali. Saya senang sekali bisa ikut makan malam di sini."
            "Ibu Shiori" "Jangan sungkan! Rumah ini selalu senang kalau teman dekat Shiori datang berkunjung. Sampaikan juga salam Natal kami untuk keluarga Amamiya ya."
            chiasa "Pasti saya sampaikan, Oba-san."
            nar "Satu jam kemudian, Shiori sendiri yang mengantarmu sampai serambi depan tempat Kuroiwa sudah siap membukakan gerbang besi. Angin malam Desember langsung menyambutmu di luar pintu."
            shiori "Hati-hati di jalan pulang, Amamiya-san. Jangan lupa pegang kaleng teh dari Ibu baik-baik. Sekali lagi, selamat Natal."
            chiasa "Selamat Natal juga, Saionji-senpai. Permisi."
            nar "Saat kamu melangkah keluar melewati gerbang besi, Kuroiwa menunduk hormat membukakan jalan sambil sempat mengarahkan tatapan khawatir sekali lagi dari wajah Shiori yang tersenyum tenang ke arah punggungmu."
            nar "Kamu memeluk kaleng teh Ceylon pemberian Ibu Shiori di depan dadamu sambil berjalan menyusuri trotoar sunyi Distrik Elite. Semakin hangat dan tulus sambutan keluarganya tadi, semakin dingin terasa keberadaan buku catatan biru yang tak tersentuh di meja ruang duduk itu."
            nar "Kamu berbalik sejenak di pinggir jalan batu. Shiori masih berdiri tenang di bawah lampu serambi dengan senyum yang sama persis seperti ketika kamu datang, tidak kurang dan tidak lebih satu garis pun."
            chiasa "{i}Kami melewati seluruh malam tanpa satu pun suara keras... tapi justru karena tidak ada satu pun hal yang dibahas, jarak di belakang senyumnya terasa makin mustahil ditebak.{/i}"
            nar "Kalian melewati malam Natal dengan sangat sopan tanpa satu pun langkah mendekati persoalan yang belum selesai. Di balik pintu yang perlahan menutup, permainan yang sempat berhenti di bulan November kini berjalan terus tanpa perlu melibatkanmu lagi."
    else:
        if kk_has("shiori_teman_dipercaya"):
            shiori "Dulu kau mau duduk denganku bahkan setelah klub tutup. Malam ini juga ada kursi kosong."
        else:
            shiori "Masuklah sebentar. Di luar dingin."
        nar "Ia menyambut dengan senyum yang kaubawa dalam banyak kenangan baik. Keluarganya tetap hangat; hanya jarak pribadi Shiori yang terasa lebih rapi, seolah setiap celah kini harus sengaja diberikan."
        call kk_family_menu("S14", ["Minta maaf atas jawabanmu waktu itu.", "Katakan bahwa ia juga ikut membuat keadaan sulit.", "Ucapkan selamat Natal tanpa membahasnya."])
        if _return == "A":
            shiori "Aku dengar. Terima kasih sudah datang."
            nar "Ia meminta kau menyebut bagian yang disesali, bukan merangkum semuanya sebagai keadaan yang rumit. Setelah mendengar, ia mengajak masuk tanpa mengatakan urusan kalian sudah selesai."
        elif _return == "B":
            nar "Kau mengatakan ia juga membuat keadaan sulit. Shiori mendengarkan, kemudian menanyakan apakah kesulitan itu dipakai untuk menjelaskan atau membatalkan tanggung jawabmu."
            shiori "Aku bisa punya bagian salah. Itu tidak membuat dua cerita yang bertentangan mendadak sama-sama benar."
        else:
            nar "Kau mengucapkan selamat Natal dan menghindari persoalan lama. Shiori membalas ucapanmu dengan hangat yang cukup untuk tamu. Kalian melewati malam tanpa satu pun langkah mendekati yang belum selesai."
    return

# ┌─ PANDUAN CERITA · S15 · Hatsumode: Doa untuk Siapa
# │ LOKASI  : Alam & Pantai · Kuil
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia berdoa.
# │ INTI    : A tanya / B tidak / C ikut.
# │ AKHIRAN : petunjuk.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S15:
    call kk_scene_enter("shiori","Kuil saat Tahun Baru")
    nar "Shiori memberi jalan kepada keluarga yang membawa anak kecil. Ia mengamati tangan orang tua yang menahan agar anak itu tidak jatuh, lalu lama tidak bergerak meski antrean di depan sudah kosong."
    call kk_family_menu("S15", ["Tanya untuk siapa ia akan berdoa.", "Biarkan ia berdoa sendiri.", "Berdiri di sampingnya dan ikut berdoa."])
    if _return == "A":
        shiori "Untuk seseorang yang jawabannya masih kutunggu."
        nar "Ia tidak menyebut nama. Ketika kau menanyakan hasil yang diharapkan, ia mengatakan ingin jawaban yang benar, lalu mengakui dirinya juga bisa takut pada kebenaran tersebut."
    elif _return == "B":
        nar "Kau memberi ruang untuk doanya sendiri. Shiori menunduk, menutup mata, dan kembali dengan wajah yang tidak perlu menjelaskan seluruh isinya kepadamu."
    else:
        nar "Kalian baru membuka mata setelah bunyi lonceng berhenti."
        shiori "Aku biasanya lebih percaya usaha daripada doa. Hari ini aku ingin membiarkan ada satu keinginan yang tidak harus kubuktikan dapat kukendalikan."
    return

# ┌─ PANDUAN CERITA · S16 · Valentine: Papan Kosong
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia tidak menjawab.
# │ INTI    : A datang / B tunggu / C abaikan.
# │ AKHIRAN : stage 3.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S16:
    call kk_scene_enter("shiori","Klub Catur saat Valentine")
    if kk_has("shiori_mendengar_maaf"):
        nar "Saat Natal ia mendengarkan permintaan maafmu. Hari ini kursi di seberangnya kosong lagi."
    if kk_has("shiori_doa_ditanya"):
        nar "Kau teringat jawabannya di kuil. Kini Shiori duduk di depan papan tanpa satu bidak pun."
    else:
        nar "Biasanya Shiori sudah menata bidak sebelum siapa pun datang. Hari ini papannya kosong."
    call kk_family_menu("S16", ["Hampiri kursi di seberangnya.", "Tunggu di pintu sampai ia bicara.", "Terus berjalan menuju festival."])
    if _return == "A":
        nar "Kau duduk dan menanyakan apakah ia ingin berbicara. Shiori tersenyum, lalu menggeleng. Kali ini ia tidak memberikan permainan sebagai jalan memutar menuju hal yang belum bersedia disebut."
        nar "Kau tinggal sampai bel berbunyi. Tidak semua jarak dapat diselesaikan dengan keberanian mendekat sekali."
    elif _return == "B":
        nar "Kau menunggu di pintu. Shiori mengetahui kehadiranmu tetapi tidak memanggil. Setelah bel, ia membereskan kotak tanpa pernah mengisi papan."
        nar "Penantianmu mendapat bentuk, belum mendapat jawaban. Ia belum memilih membiarkanmu masuk lebih jauh dari tempat yang kautentukan sendiri."
    else:
        nar "Kau terus berjalan. Shiori melihatmu lewat dan kembali pada papan kosong. Hari yang biasa dipakai orang lain meminta kepastian kalian lewati tanpa mengucapkan apa pun."
    return

# ┌─ PANDUAN CERITA · S13 · Penemuan
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia menemukan kebohongan pemain atau pengkhianatan pada orang yang ia pedulikan.
# │ INTI    : A mengaku / B menyangkal / C lari.
# │ AKHIRAN : gerbang Rute Revenge (stage 2).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S13:
    call kk_scene_enter("shiori","Klub Catur")
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Lampu gantung berbingkai kuningan di ruang Klub Catur memancarkan cahaya hangat di atas deretan papan kayu yang sudah dirapikan. Di luar jendela kaca gelap bulan November, lampu jalan Distrik Elite berkilau sunyi."
        else:
            nar "Cahaya bulan November masuk tenang melalui tirai tipis ruang Klub Catur yang lengang. Aroma teh hitam seduhan baru bercampur wangi kayu papan catur yang baru dilap memenuhi ruangan."
        nar "Begitu kamu melangkah masuk memenuhi pesan singkat Shiori, seorang anggota tingkat satu sedang mengunci lemari papan cadangan di sudut ruangan dan segera membungkuk sopan kepada Shiori."
        "Anggota Klub" "Semua catatan latihan minggu ini sudah saya rapikan ke laci, Saionji-senpai. Daftar pasangan tanding minggu depan juga sudah saya tempel di papan pengumuman."
        shiori "Terima kasih bantuannya. Pastikan papan nomor tiga dan lima diganti kain pelapisnya sebelum pertandingan hari Rabu. Hati-hati di jalan pulang."
        "Anggota Klub" "Siap, Saionji-senpai! Permisi, Amamiya-san."
        chiasa "Hati-hati di jalan ya."
        nar "Pintu kayu menutup perlahan di belakang mahasiswa itu, meninggalkan kesunyian yang sangat teratur di dalam ruang klub. Saionji Shiori duduk tegak di kursi ujung meja dekat jendela dengan rambut putih keperakan bergelombang berhiasan mutiara ungu-emas tersusun rapi."
        nar "Dari balik kaca jendela lantai dua, siluet mobil sedan gelap yang biasa dikemudikan Kuroiwa tampak terparkir tenang di tepi halaman luar. Detik jam dinding kayu di ruang klub terdengar begitu jelas di tengah ruangan yang kosong."
        nar "Di hadapannya tidak ada papan permainan yang sedang dibuka. Di atas taplak meja hanya tergeletak sebuah map biru tua tertutup, teko porselen hangat, dua cangkir teh darjeeling, serta satu papan kayu kecil di meja samping yang masih menyisakan dua bidak hitam berdiri sendirian."
        chiasa "Selamat datangnya rapi banget, Saionji-senpai. Tumben manggil ke ruang klub tanpa menyiapkan papan catur di meja utama dulu."
        shiori "Silakan duduk, Amamiya-san. Teh darjeelingnya baru saja kuseduh tiga menit lalu, masih hangat."
        nar "Kamu menarik kursi di seberangnya sambil merapikan syal tipis di bahumu. Shiori menuangkan teh ke cangkirmu dengan gerakan yang begitu tenang hingga tidak satu pun tetes berbunyi keras. Senyum sopannya terpasang tepat seperti biasanya."
        shiori "Bagaimana tanggapan pengunjung di Gedung Seni Rupa sepanjang Festival Seni minggu ini? Kudengar pameran fakultasmu ramai sekali."
        chiasa "Lumayan ramai, Senpai. Banyak anak jurusan lain ikut mampir lihat panel ilustrasi sama instalasi kain."
        shiori "Baguslah. Minumlah tehnya dulu, Amamiya-san. Daun darjeeling ini paling terasa aromanya sebelum uapnya menghilang."
        nar "Kamu mengangkat cangkir porselen itu dan menyesapnya satu teguk kecil. Kehangatan teh di kerongkongan sama sekali tidak mengurangi ketegangan yang menempel halus di antara kalian."
        chiasa "Enak sekali tehnya, Senpai. Wanginya ringan."
        shiori "Syukurlah kalau cocok. Aku sengaja menyeduh daun teh yang ringan supaya kita bisa ngobrol dengan kepala dingin."
        shiori "Dalam catur, Amamiya-san, niat lawan jarang kelihatan dari langkah pertama. Tapi kalau ada dua langkahnya sendiri yang saling bertabrakan... di situlah semuanya terbaca."
        chiasa "Eh? Hari ini kita langsung masuk ke teori catur, Senpai?"
        shiori "Fufu, anggap saja kelanjutan dari obrolan kita kemarin. Kamu mau aku yang buka catatanku duluan, atau kamu yang mulai cerita sendiri?"
        chiasa "Senpai sebutin aja langsung bagian mana yang bikin Senpai manggil aku ke sini."
        nar "Begitu cangkir teh diletakkan rapi di hadapanmu, ia meletakkan ujung jarinya ringan di atas map biru tua tersebut."
        if any(c["ev"] == "C11" and c["key"] == "B" for c in choices_log):
            nar "Ia menggeser sebuah buku novel strategi ringan yang penanda kertasnya mencuat di bagian kolofon dan bab ketiga keluar dari samping map biru, meletakkannya sejajar di tengah meja."
            shiori "Waktu di pameran Gedung Seni Rupa kemarin, kamu bilang tidak kenal siapa itu Shena. Kamu bahkan menyebut gambarmu cuma hasil latihan meniru buku panduan."
            shiori "Aku sudah memeriksa ulang kolofon penerbit dan arsip pameran Fakultas Seni tahun lalu. Kenapa waktu itu kamu berbohong padaku, Amamiya-san?"
        else:
            nar "Ia memutar map biru tua itu sedikit ke tengah meja tanpa langsung membukanya, membiarkan tatapan matanya berhenti tenang pada wajahmu."
            shiori "Belakangan ini aku mencocokkan beberapa cerita yang kamu sampaikan padaku dengan fakta yang kutemukan sendiri di kampus."
            shiori "Sayangnya, ada beberapa bagian yang sama sekali tidak sinkron. Sebelum aku mengambil kesimpulan sendiri, aku ingin dengar penjelasannya langsung darimu."
        if kk_has("shiori_alasan_kedua"):
            shiori "Penjelasan tambahan yang kamu berikan sesudah pameran kemarin pun ternyata tidak selaras dengan alasanmu yang pertama."
        chiasa "{i}Ia tidak menuduh sambil berteriak. Ia justru menyodorkan ruang terbuka supaya aku memilih sendiri apakah mau berhenti berbohong sekarang atau melangkah lebih jauh.{/i}"
        nar "Shiori tidak menatapmu seolah ia sudah mengetahui seluruh isi kepalamu ataupun sedang menikmati ketegangan ini. Ia tetap tenang, memberi ruang penuh bagi jawabanmu sehingga kebohongan berikutnya benar-benar menjadi pilihan sadar di depan matanya."
        shiori "Aku sudah pernah mengatakan sebelumnya, Amamiya-san. Aku tidak keberatan kalau seseorang punya rahasia yang belum ingin ia bagi. Yang tidak kusukai adalah dibuat tersenyum mengikuti cerita yang sengaja direkayasa di depanku."
        shiori "Sekarang kita hanya berdua di ruang ini. Ceritakan kepadaku apa yang sebenarnya terjadi."
        call kk_family_menu("S13", ["\"Baik, Saionji-senpai. Aku cerita terus terang bagian yang kusembunyikan.\"", "\"Ceritaku masih sama seperti kemarin, Senpai. Memang cuma kebetulan.\"", "Bereskan barangmu dan pergi dari ruang klub."])
        if _return == "A":
            nar "Kamu menatap cangkir teh yang masih mengepul tipis di depanmu selama dua detik, lalu meletakkan kedua tanganmu di tepi meja dan menarik napas panjang."
            chiasa "...Baik, Saionji-senpai. Aku berhenti berputar-putar. Aku bakal cerita terus terang bagian yang selama ini kusembunyikan dari Senpai."
            if any(c["ev"] == "C11" and c["key"] == "B" for c in choices_log):
                chiasa "Waktu di pameran kecil itu aku memang berbohong. Nama pena Shena itu benar punyaku, dan ilustrasi jendela itu memang arsip lama dari tanganku sendiri."
                chiasa "Aku panik waktu Senpai langsung menebak di tengah galeri karena belakangan ini gambarku sendiri lagi jauh menurun dari kualitas jilid sebelumnya. Aku takut kalau orang-orang tahu terus berekspektasi tinggi, atau sampai tersebar di kampus."
            else:
                chiasa "Beberapa detail yang kubilang sebelumnya memang sengaja kututup-tutupi dan kubelokkan supaya posisiku kelihatan lebih rapi di depan Senpai. Faktanya ada bagian yang keliru dan sengaja nggak kusebutkan waktu itu."
                chiasa "Aku nggak minta Senpai langsung percaya begitu saja cuma dari permintaanku. Senpai boleh periksa langsung urutan kejadiannya sama catatan yang ada di map Senpai."
            nar "Kamu menjelaskan rincian yang sebenarnya secara runtut, menyebutkan bagian mana saja yang dulu kamu belokkan dan fakta konkret apa yang bisa ia periksa sendiri tanpa meminta pembelaan ataupun janji dimaafkan seketika."
            nar "Shiori menyimak tanpa memotong satu kalimat pun. Raut wajahnya tidak mendadak melunak menjadi hangat, tetapi jemarinya yang tadi berada di tepi map biru kini membuka halaman pertama perlahan alih-alih menutupnya."
            shiori "Baik. Aku mendengarkan seluruhnya, dan aku akan mengingat apa yang kamu katakan hari ini sama cermatnya dengan catatan kemarin."
            shiori "Satu hal yang membuatku penasaran, Amamiya-san. Kenapa waktu itu kamu tidak cukup bilang saja bahwa kamu belum siap membahasnya, alih-alih membuat cerita baru?"
            chiasa "Karena aku pengecut dan mengira kalau aku menyangkal cukup cepat, Senpai bakal langsung melewatkannya. Aku takut gagal memenuhi bayangan orang-orang di sekitarku kalau kenyataannya terbuka."
            shiori "Mengakui rasa takut jauh lebih mudah kuhormati daripada memasang keyakinan palsu di depan wajahku, Amamiya-san."
            shiori "Kecewa tentu masih ada. Kepercayaan tidak langsung utuh lagi hanya karena satu pengakuan terlambat. Tapi setidaknya hari ini kamu berhenti memperlakukanku seperti penonton yang mudah diarahkan."
            nar "Ia meneguk teh hitamnya sekali, membaca ulang dua baris catatan di halaman pertama map biru, lalu menatapmu kembali dengan ketajaman yang jauh lebih jernih."
            shiori "Karena kamu sudah memilih bicara terbuka, aku akan mengajukan pertanyaan lanjutannya langsung sekarang. Apakah ada orang lain di kampus yang kamu minta ikut menutupi cerita ini, atau ini murni keputusanmu sendiri?"
            chiasa "Murni keputusanku sendiri, Saionji-senpai. Nggak ada satu orang pun yang kuminta ikut berbohong buat melindungiku."
            shiori "Baik. Jawabanmu bisa kuperiksa, dan itu lebih berguna daripada seratus permintaan maaf. Mari kita bahas sisanya pelan-pelan sambil minum teh."
            chiasa "Iya, Senpai. Aku siap mendengarkan bagian mana lagi yang perlu kuluruskan."
            nar "Ketegangan di ruang Klub Catur belum hilang sepenuhnya. Meski begitu, map biru di depan Shiori tetap terbuka untuk dibahas bersama alih-alih berubah menjadi berkas penuntutan sepihak."
        elif _return == "B":
            nar "Kamu menahan gemetar tipis di ujung jarimu, menegakkan bahu, lalu memilih mempertahankan versi cerita yang sejak awal kamu bangun."
            chiasa "Aku ngerti kenapa Saionji-senpai merasa ada yang aneh. Tapi ceritaku memang masih sama seperti kemarin, Senpai. Nggak ada yang kusembunyikan, semua kesamaan yang Senpai temukan itu murni kebetulan aja."
            nar "Shiori tidak langsung membalas. Ia membuka map biru di depannya satu inci, memperlihatkan selembar salinan catatan tanggal dan perbandingan tanda tangan di kartu kunjungan, lalu terdiam penuh memberi kesempatan terakhir."
            shiori "Satu bagian ini secara faktual mustahil terjadi bersamaan dengan alasanmu kemarin, Amamiya-san. Bahkan catatan arsip pameran, tanggal cetak jilid, dan tarikan huruf di halaman ini jelas saling bertentangan dengan kalimatmu barusan."
            shiori "Aku tanya sekali lagi saja. Kamu yakin tetap ingin mempertahankan jawaban yang sama?"
            chiasa "Iya, Senpai. Mungkin catatan sumber yang Senpai baca juga ada bagian yang kurang lengkap atau salah cetak, soalnya dari sisiku memang begitu kejadiannya."
            nar "Dua detik sunyi lewat di ruang klub. Shiori sempat melirik sekilas jarum jam dinding kayu di atas lemari papan sebelum mengalihkan tatapannya kembali kepadamu. Begitu jelas kamu lebih memilih menumpuk penyangkalan baru daripada menjawab kontradiksi yang ia tunjukkan, ia berhenti mendesak sepenuhnya."
            nar "Ia merapikan kertas di dalam map biru tua itu dengan jari yang sangat tenang, menutup sampulnya rapat, lalu kembali memasang senyum sopan yang nyaris identik dengan senyumnya saat pertama kali menyapamu di kampus."
            shiori "Begitu, ya. Kalau memang itu jawaban finalmu, aku tidak akan menyita waktumu lebih lama lagi di sini. Kuroiwa juga sudah menunggu di bawah."
            chiasa "Jadi masalahnya sudah jelas sekarang kan, Saionji-senpai?"
            shiori "Sudah sangat jelas, Amamiya-san. Aku sudah mendengar jawabanmu sampai selesai."
            shiori "Sekarang aku akan mencari kebenaran yang tidak lagi bergantung pada kesediaanmu untuk mengatakan yang sebenarnya."
            chiasa "Maksud Senpai apa?"
            shiori "Persis seperti bunyi kalimatnya, Amamiya-san. Selamat beristirahat, semoga sisa Festival Seni minggu ini berjalan lancar."
            chiasa "Permisi, Saionji-senpai."
            chiasa "{i}Senyumnya sama sekali nggak berubah dari lima menit lalu... tapi udara di ruangan ini mendadak terasa sedingin kaca.{/i}"
            nar "Shiori mengangkat cangkir tehnya dengan gerakan anggun yang tenang. Ia tidak mengusirmu, tidak pula menaikkan nada bicaranya. Justru ketenangannya yang tanpa cela menegaskan bahwa babak perundingan di antara kalian baru saja selesai."
        else:
            nar "Kamu menatap map biru tertutup di tengah meja, lalu memutuskan tidak memberikan satu pun jawaban tambahan yang bisa ia pakai untuk menjebakmu lebih dalam. Kamu meraih tali tasmu dan beranjak berdiri."
            chiasa "Maaf, Saionji-senpai. Aku datang ke sini kupikir buat ngobrol santai atau main catur. Aku nggak siap diinterogasi kayak begini. Aku lagi ada urusan lain di rumah, jadi aku permisi duluan."
            nar "Kamu mulai memasukkan buku catatan dan syalmu ke dalam tas dengan cepat. Di seberang meja, Shiori tetap duduk tegak tanpa sedikit pun berusaha menahan lenganmu ataupun menaikkan suaranya."
            nar "Dengan satu jari rampingnya, ia menggeser bidak raja hitam di papan kayu samping ke kotak kosong di tepi papan sebelum menoleh tenang ke arahmu."
            shiori "Kamu bebas keluar dari pintu itu sekarang juga, Amamiya-san. Aku tidak pernah menahan seseorang di ruang klub di luar kemauannya."
            chiasa "Terima kasih pengertiannya, Senpai."
            nar "Tepat saat tanganmu sudah menyentuh gagang pintu kayu, suara jernih Shiori terdengar tenang memotong kesunyian ruangan di belakang punggungmu."
            shiori "Satu hal saja sebelum kamu menutup pintu. Jangan pernah menyebut kepergianmu hari ini sebagai bukti bahwa persoalannya tidak layak dibahas."
            chiasa "Aku nggak bilang begitu, Senpai. Aku cuma nggak merasa harus terus duduk di ruangan ini."
            shiori "Baik. Berarti diam dan pergi adalah langkah yang kamu pilih di giliranmu hari ini. Aku akan mencatatnya dengan rapi di dalam map ini."
            chiasa "Terserah Senpai mau mencatat apa di situ."
            nar "Jemarimu sempat tertahan setengah detik di gagang dingin pintu sambil menimbang apakah lebih aman berbalik sekarang. Namun begitu mendengar bunyi pelan map biru dibuka di belakangmu, kamu langsung menekan gagang pintu dan melangkah keluar."
            chiasa "{i}Ia sama sekali tidak terlihat panik atau marah melihatku pergi... justru itu yang bikin tengkukku dingin.{/i}"
            nar "Kamu tidak menoleh lagi dan segera melangkah keluar menyusuri koridor Distrik Elite yang terasa semakin dingin. Saat kamu berhenti setengah detik di dekat tangga, tidak terdengar suara pintu dibuka ataupun langkah kaki mengejar di belakangmu."
            nar "Di balik pintu ruang klub yang sudah menutup rapat, Shiori tetap duduk sendirian di samping map biru yang kini tidak lagi membutuhkan kerja samamu untuk dibuka sampai halaman terakhir."
    else:
        if kk_slot >= 3:
            nar "Lampu gantung berbingkai kuningan di ruang Klub Catur memancarkan cahaya hangat di atas deretan papan kayu yang sudah dirapikan. Di luar jendela kaca gelap bulan November, lampu jalan Distrik Elite berkilau sunyi."
        else:
            nar "Cahaya bulan November masuk tenang melalui tirai tipis ruang Klub Catur yang lengang. Aroma teh hitam seduhan baru bercampur wangi kayu papan catur yang baru dilap memenuhi ruangan."
        nar "Begitu kamu melangkah masuk memenuhi pesan singkat Shiori, seorang anggota tingkat satu sedang mengunci lemari papan cadangan di sudut ruangan dan segera membungkuk sopan kepada Shiori."
        "Anggota Klub" "Semua catatan latihan minggu ini sudah saya rapikan ke laci, Saionji-senpai. Daftar pasangan tanding minggu depan juga sudah saya tempel di papan pengumuman."
        shiori "Terima kasih bantuannya. Pastikan papan nomor tiga dan lima diganti kain pelapisnya sebelum pertandingan hari Rabu. Hati-hati di jalan pulang."
        "Anggota Klub" "Siap, Saionji-senpai! Permisi, Kisaragi-senpai."
        yutaka "Hati-hati di jalan."
        nar "Pintu kayu menutup perlahan di belakang mahasiswa itu, meninggalkan kesunyian yang sangat teratur di dalam ruang klub. Saionji Shiori duduk tegak di kursi ujung meja dekat jendela dengan rambut putih keperakan bergelombang berhiasan mutiara ungu-emas tersusun rapi."
        nar "Dari balik kaca jendela lantai dua, siluet mobil sedan gelap yang biasa dikemudikan Kuroiwa tampak terparkir tenang di tepi halaman luar. Detik jam dinding kayu di ruang klub terdengar begitu jelas di tengah ruangan yang kosong."
        nar "Di hadapannya tidak ada papan permainan yang sedang dibuka. Di atas taplak meja hanya tergeletak sebuah map biru tua tertutup, teko porselen hangat, dua cangkir teh darjeeling, serta satu papan kayu kecil di meja samping yang masih menyisakan dua bidak hitam berdiri sendirian."
        yutaka "Pemandangan yang nggak biasa, Saionji-san. Tumben manggil teman sefakultas ke ruang klub tanpa menyiapkan papan catur di meja utama dulu."
        shiori "Silakan duduk, Kisaragi-san. Teh darjeelingnya baru saja kuseduh tiga menit lalu, masih hangat."
        nar "Kamu menarik kursi di seberangnya sambil menyampirkan mantel gelapmu ke sandaran kursi. Shiori menuangkan teh ke cangkirmu dengan gerakan yang begitu tenang hingga tidak satu pun tetes berbunyi keras. Senyum sopannya terpasang tepat seperti biasanya."
        shiori "Bagaimana urusan rekap dana Festival Seni dari bagian panitia Ekonomi minggu ini? Kudengar jadwalku dan jadwal panitiamu sama-sama padat."
        yutaka "Lumayan padat, tapi semua nota sudah mulai rapi kok. Anak-anak panitia juga sudah kebagian jadwal jaga masing-masing."
        shiori "Baguslah. Minumlah tehnya dulu, Kisaragi-san. Daun darjeeling ini paling terasa aromanya sebelum uapnya menghilang."
        nar "Kamu mengangkat cangkir porselen itu dan menyesapnya satu teguk kecil. Kehangatan teh di kerongkongan sama sekali tidak mengurangi ketegangan yang menempel halus di antara kalian."
        yutaka "Rasanya ringan sekali. Selera tehmu memang selalu konsisten."
        shiori "Terima kasih. Aku sengaja memilih daun yang tidak terlalu pahit supaya kita bisa bicara dengan kepala jernih."
        nar "Kamu sempat melirik meja samping tempat jam catur kayu masih mati terlipat di sebelah dua bidak hitam. Tidak ada tanda-tanda pertemuan ini bakal berakhir dengan pertandingan ringan."
        shiori "Kita berdua sama-sama tumbuh di lingkungan keluarga yang terbiasa menyembunyikan separuh kebenaran di balik kesopanan rapi, Kisaragi-san. Justru karena itu aku paling malas membuang waktu berputar-putar di meja ini."
        yutaka "Pembukaan yang cukup tajam, Saionji-san."
        shiori "Dalam permainan catur, kita jarang tahu niat lawan hanya dari satu langkah pertama. Biasanya niat sebenarnya baru terlihat ketika dua langkah yang seharusnya saling menguatkan ternyata saling bertabrakan di papan."
        yutaka "Kamu lebih suka aku menebak dulu, atau kamu langsung memaparkan apa yang baru kamu cek?"
        shiori "Kalau kamu mempersilakan, aku akan langsung masuk ke intinya."
        nar "Begitu cangkir teh diletakkan rapi di hadapanmu, ia meletakkan ujung jarinya ringan di atas map biru tua tersebut."
        if any(c["ev"] == "C11" and c["key"] == "B" for c in choices_log):
            shiori "Di pameran itu kamu bilang tidak mengenal Shena. Aku sudah membaca bukunya. Mengapa kamu mengatakan itu, Kisaragi-san?"
        else:
            nar "Ia memutar map biru tua itu sedikit ke tengah meja tanpa langsung membukanya, membiarkan mata ungu ametisnya berhenti tenang pada wajahmu."
            shiori "Belakangan ini aku menyusun ulang beberapa catatan obrolan kita di Ekonomi maupun klub, lalu mencocokkannya dengan beberapa fakta yang kutemukan sendiri di kampus, Kisaragi-san."
            shiori "Ada beberapa bagian penting yang tidak cocok antara cerita yang kamu sampaikan padaku dan kenyataan yang kutemukan. Sebelum aku menyimpulkan sendiri, aku ingin mendengarnya langsung darimu."
        if kk_has("shiori_alasan_kedua"):
            shiori "Penjelasan tambahan yang kamu berikan setelah pertemuan terakhir kita pun ternyata tidak selaras dengan alasanmu yang pertama."
        yutaka "{i}Ia tidak menuduh sambil menaikkan suara. Ia justru menyodorkan ruang terbuka supaya aku memilih sendiri apakah mau berhenti berbohong sekarang atau melangkah lebih jauh.{/i}"
        nar "Shiori tidak menatapmu seolah ia sudah mengetahui seluruh isi kepalamu ataupun sedang menikmati ketegangan ini. Ia tetap tenang, memberi ruang penuh bagi jawabanmu sehingga kebohongan berikutnya benar-benar menjadi pilihan sadar di depan matanya."
        shiori "Aku sudah pernah mengatakan sebelumnya, Kisaragi-san. Aku tidak keberatan kalau sesama penyandang nama keluarga besar punya hal-hal pribadi yang belum ingin ia bagi. Yang tidak kusukai adalah dibuat tersenyum mengikuti cerita yang sengaja direkayasa di depanku."
        shiori "Sekarang kita hanya berdua di ruang ini. Ceritakan kepadaku apa yang sebenarnya terjadi."
        call kk_family_menu("S13", ["\"Baik, Saionji-san. Aku cerita terus terang bagian yang kusembunyikan.\"", "\"Ceritaku masih sama seperti kemarin, Saionji-san. Memang cuma kebetulan.\"", "Bereskan barangmu dan pergi dari ruang klub."])
        if _return == "A":
            nar "Kamu menatap cangkir teh yang masih mengepul tipis di depanmu selama dua detik, lalu meletakkan kedua tanganmu di tepi meja dan menarik napas panjang."
            yutaka "...Baik, Saionji-san. Aku berhenti bersembunyi di balik jawaban santai. Aku bakal cerita terus terang bagian yang selama ini kusembunyikan darimu."
            yutaka "Beberapa detail yang kubilang sebelumnya memang sengaja kututup-tutupi dan kubelokkan supaya posisiku kelihatan lebih rapi di depanmu. Faktanya ada bagian yang keliru dan sengaja nggak kusebutkan waktu itu."
            yutaka "Aku nggak minta kamu langsung percaya begitu saja cuma dari ucapanku sekarang. Kamu boleh periksa langsung urutan waktunya dengan catatan yang ada di dalam map biru itu."
            nar "Kamu menjelaskan rincian yang sebenarnya secara runtut, menyebutkan bagian mana saja yang dulu kamu belokkan dan fakta konkret apa yang bisa ia periksa sendiri tanpa berlindung di balik nama keluarga Kisaragi ataupun janji dimaafkan seketika."
            nar "Shiori menyimak tanpa memotong satu kalimat pun. Raut wajahnya tidak mendadak melunak menjadi hangat, tetapi jemarinya yang tadi berada di tepi map biru kini membuka halaman pertama perlahan alih-alih menutupnya."
            shiori "Baik. Aku mendengarkan seluruhnya, dan aku akan mengingat apa yang kamu katakan hari ini sama cermatnya dengan catatan kemarin."
            shiori "Satu hal yang membuatku penasaran, Kisaragi-san. Kenapa waktu itu kamu tidak cukup bilang saja bahwa kamu belum siap membahasnya, alih-alih membuat cerita baru?"
            yutaka "Karena aku terbiasa memakai candaan dan jawaban mulus buat menutupi bagian yang berantakan. Aku sempat mengira kalau aku mengelak cukup cepat, kamu bakal langsung melewatkannya."
            shiori "Mengakui salah langkah jauh lebih mudah kuhormati daripada memasang keyakinan palsu di depan wajahku, Kisaragi-san."
            shiori "Kecewa tentu masih ada. Kepercayaan tidak langsung utuh lagi hanya karena satu pengakuan terlambat. Tapi setidaknya hari ini kamu berhenti memperlakukanku seperti penonton yang mudah diarahkan."
            nar "Ia meneguk teh hitamnya sekali, membaca ulang dua baris catatan di halaman pertama map biru, lalu menatapmu kembali dengan ketajaman yang jauh lebih jernih."
            shiori "Karena kamu sudah memilih bicara terbuka, aku akan mengajukan pertanyaan lanjutannya langsung sekarang. Apakah Amamiya-san atau orang lain di lingkaranmu ikut mengetahui bagian yang kamu tutup-tutupi ini?"
            yutaka "Nggak. Ini murni keputusanku sendiri, Saionji-san. Nggak ada satu orang pun yang kuminta ikut berbohong buat melindungiku."
            shiori "Dan kalau aku mengecek langsung bagian jadwal panitia Ekonomi dari bulan lalu, semua angka yang baru kamu sebutkan akan cocok?"
            yutaka "Cocok. Kamu boleh mengeceknya sendiri kapan pun kamu mau."
            shiori "Baik. Jawabanmu bisa kuperiksa, dan itu lebih berguna daripada seratus permintaan maaf. Mari kita bahas sisanya pelan-pelan sambil minum teh."
            yutaka "Iya. Aku siap mendengarkan bagian mana lagi yang perlu kuluruskan."
            nar "Ketegangan di ruang Klub Catur belum hilang sepenuhnya. Meski begitu, map biru di depan Shiori tetap terbuka untuk dibahas bersama alih-alih berubah menjadi berkas penuntutan sepihak."
        elif _return == "B":
            nar "Kamu menjaga ketenangan wajahmu tetap rata, menyandarkan bahu pelan, lalu memilih mempertahankan versi cerita yang sejak awal kamu bangun."
            yutaka "Aku mengerti kenapa kamu merasa ada bagian yang janggal, Saionji-san. Tapi ceritaku memang masih sama seperti kemarin. Nggak ada yang kusembunyikan, semua kesamaan yang kamu temukan itu murni kebetulan saja."
            nar "Shiori tidak langsung membalas. Ia membuka map biru di depannya satu inci, memperlihatkan selembar salinan catatan tanggal dan rincian kejadian yang sangat spesifik, lalu terdiam penuh memberi kesempatan terakhir."
            shiori "Satu bagian ini secara faktual mustahil terjadi bersamaan dengan alasanmu kemarin, Kisaragi-san. Bahkan catatan waktu di daftar panitia Ekonomi dan keterangan di halaman ini jelas saling bertentangan dengan kalimatmu barusan."
            shiori "Aku tanya sekali lagi saja. Kamu yakin tetap ingin mempertahankan jawaban yang sama?"
            yutaka "Iya. Mungkin catatan sumber yang kamu pegang juga ada bagian yang terpotong atau keliru tanggalnya, soalnya dari sisiku memang begitu kejadiannya."
            nar "Dua detik sunyi lewat di ruang klub. Shiori sempat melirik sekilas jarum jam dinding kayu di atas lemari papan sebelum mengalihkan tatapannya kembali kepadamu. Begitu jelas kamu lebih memilih menumpuk penyangkalan baru daripada menjawab kontradiksi yang ia tunjukkan, ia berhenti mendesak sepenuhnya."
            nar "Ia merapikan kertas di dalam map biru tua itu dengan jari yang sangat tenang, menutup sampulnya rapat, lalu kembali memasang senyum sopan yang nyaris identik dengan senyumnya saat pertama kali menyapamu di kelas Ekonomi."
            shiori "Begitu, ya. Kalau memang itu jawaban finalmu, aku tidak akan menyita waktumu lebih lama lagi di sini. Kuroiwa juga sudah menunggu di bawah."
            yutaka "Jadi masalahnya sudah jelas sekarang kan, Saionji-san?"
            shiori "Sudah sangat jelas, Kisaragi-san. Aku sudah mendengar jawabanmu sampai selesai."
            shiori "Sekarang aku akan mencari kebenaran yang tidak lagi bergantung pada kesediaanmu untuk mengatakan yang sebenarnya."
            yutaka "Maksudmu apa?"
            shiori "Persis seperti bunyi kalimatnya, Kisaragi-san. Selamat beristirahat, semoga sisa kegiatan Festival Seni minggu ini berjalan lancar."
            yutaka "Kalau begitu aku permisi dulu, Saionji-san."
            shiori "Hati-hati di jalan pulang."
            yutaka "{i}Senyumnya sama sekali nggak berubah dari lima menit lalu... tapi udara di ruangan ini mendadak terasa sedingin kaca.{/i}"
            nar "Shiori mengangkat cangkir tehnya dengan gerakan anggun yang tenang. Ia tidak mengusirmu, tidak pula menaikkan nada bicaranya. Justru ketenangannya yang tanpa cela menegaskan bahwa babak perundingan di antara kalian baru saja selesai."
        else:
            nar "Kamu menatap map biru tertutup di tengah meja, lalu memutuskan tidak memberikan satu pun jawaban tambahan yang bisa ia pakai untuk menjebakmu lebih dalam. Kamu menyampirkan mantelmu ke lengan dan beranjak berdiri."
            yutaka "Maaf, Saionji-san. Aku datang ke sini kupikir buat ngobrol santai atau main satu partai catur. Aku nggak siap duduk buat diinterogasi kayak begini. Aku masih ada urusan lain di apartemen, jadi aku permisi duluan."
            nar "Kamu mulai memasukkan buku catatanmu ke dalam tas dengan cepat lalu mengenakan mantel gelapmu sambil tetap menjaga ekspresi tenang. Di seberang meja, Shiori tetap duduk tegak tanpa sedikit pun berusaha menahan langkahmu ataupun menaikkan suaranya."
            nar "Dengan satu jari rampingnya, ia menggeser bidak raja hitam di papan kayu samping ke kotak kosong di tepi papan sebelum menoleh tenang ke arahmu."
            shiori "Kamu bebas keluar dari pintu itu sekarang juga, Kisaragi-san. Aku tidak pernah menahan seseorang di ruang klub di luar kemauannya."
            yutaka "Terima kasih pengertiannya."
            nar "Tepat saat tanganmu sudah menyentuh gagang pintu kayu, suara jernih Shiori terdengar tenang memotong kesunyian ruangan di belakang punggungmu."
            shiori "Satu hal saja sebelum kamu menutup pintu. Jangan pernah menyebut kepergianmu hari ini sebagai bukti bahwa persoalannya tidak layak dibahas."
            yutaka "Aku nggak bilang begitu. Aku cuma nggak merasa harus terus duduk di ruangan ini."
            shiori "Baik. Berarti diam dan pergi adalah langkah yang kamu pilih di giliranmu hari ini. Aku akan mencatatnya dengan rapi di dalam map ini."
            yutaka "Terserah kamu mau mencatat apa di situ, Saionji-san."
            shiori "Silakan, Kisaragi-san. Hati-hati di jalan."
            nar "Jemarimu sempat tertahan setengah detik di gagang dingin pintu sambil menimbang apakah lebih aman berbalik sekarang. Namun begitu mendengar bunyi pelan map biru dibuka di belakangmu, kamu langsung menekan gagang pintu dan melangkah keluar."
            nar "Udara koridor Distrik Elite langsung menyambutmu dengan dingin yang tajam, menyisakan gema langkah sepatumu sendiri yang terlalu nyaring."
            yutaka "{i}Ia sama sekali tidak terlihat panik atau marah melihatku pergi... justru itu yang bikin tengkukku dingin.{/i}"
            nar "Kamu tidak menoleh lagi dan segera melangkah keluar menyusuri koridor Distrik Elite yang terasa semakin sunyi. Saat kamu berhenti setengah detik di dekat tangga, tidak terdengar suara pintu dibuka ataupun langkah kaki mengejar di belakangmu."
            nar "Di balik pintu ruang klub yang sudah menutup rapat, Shiori tetap duduk sendirian di samping map biru yang kini tidak lagi membutuhkan kerja samamu untuk dibuka sampai halaman terakhir."
    return

# ┌─ PANDUAN CERITA · S17 · Keputusan Warisan
# │ LOKASI  : Distrik Elite · Rumah Saionji
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia memutuskan masa depan.
# │ INTI    : A dukung / B ganggu.
# │ AKHIRAN : karier.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S17:
    call kk_scene_enter("shiori","Rumah Saionji")
    if kk_has("shiori_teh_rahasia"):
        shiori "Ibu memberitahuku apa yang kauceritakan saat minum teh. Kali ini biar aku yang bicara."
    elif kk_has("shiori_teh_jujur"):
        shiori "Ibu bilang kau menyuruhnya bertanya padaku. Kemarin akhirnya kami duduk dan bicara."
    elif kk_has("shiori_teh_sanjung"):
        shiori "Rupanya Ibu mengira aku tak pernah sendirian di kampus. Aku sudah bicara dengannya."
    shiori "Orang tuaku ingin tahu peran apa yang kuinginkan di perusahaan. Mereka memberi ruang memilih. Aku tidak mau menjawab asal terdengar mampu lalu menjalani sesuatu yang sebenarnya tidak kupahami."
    nar "Ia menunjukkan rencana dengan bagian yang belum pasti tetap terlihat. Kepercayaan keluarga membuatnya berani meminta waktu, bukan menutup semua keraguan dengan ambisi."
    call kk_family_menu("S17", ["Dengarkan sampai ia selesai menyampaikan rencananya.", "Potong penjelasannya dan ajukan rencanamu sendiri."])
    if _return == "A":
        nar "Kau mendengar sampai selesai, lalu bertanya pada bagian yang belum jelas. Shiori mengubah satu kesimpulan setelah pembicaraan, senang karena didukung tidak harus berarti seluruh pikirannya disetujui."
        shiori "Terima kasih. Aku ingin punya orang yang bisa berkata belum cukup jelas tanpa takut kehilangan tempat di dekatku."
    else:
        shiori "Tunggu. Aku belum selesai."
        nar "Kau menyisipkan rencanamu sebelum ia menyelesaikan miliknya. Shiori menghentikan penjelasan dan meminta kembali ruang yang baru saja dipercayakan kepadamu."
    return

init 1 python:
    def kk_saionji_dinner():
        kk_npc_rel["hari_natal_saionji"] = kk_elapsed_days

    def kk_shiori_early_truth():
        kk_adj("daftar_kebohongan_shiori",-1)
        kk_adj("ujian_lulus_shiori",1)
        if any(c["ev"] == "C11" and c["key"] == "B" for c in choices_log):
            kk_flag("shiori_tahu_shena")

    def kk_shiori_winter():
        kk_stage("shiori",max(3,stage.get("shiori",0)))

    def kk_shiori_admission():
        small = kk_get("daftar_kebohongan_shiori") == 1 and not kk_has("shiori_alasan_kedua")
        kk_adj("daftar_kebohongan_shiori",-1)
        if not small:
            kk_shiori_revenge()

    def kk_shiori_revenge():
        kk_stage("shiori",max(2,stage.get("shiori",0)))
        if kk_has("shiori_alasan_kedua"):
            kk_adj("daftar_kebohongan_shiori",2)
        if kk_host == "chiasa" and any(c["ev"] == "C11" and c["key"] == "B" for c in choices_log):
            kk_flag("shiori_menemukan_kebohongan_shena")

    _hook("S07-A",kk_saionji_dinner)
    _hook("S-D08-A",lambda: kk_flag("shiori_teh_jujur"))
    _hook("S-D08-B",lambda: kk_flag("shiori_teh_sanjung"))
    _hook("S-D08-C",lambda: kk_flag("shiori_teh_rahasia"))
    def kk_shiori_friendship():
        kk_flag("shiori_teman_dipercaya")
        kk_rel("shiori","trust",5)

    _hook("S09-A",kk_shiori_friendship)
    _hook("S09-C",lambda: kk_rel("shiori","trust",-5))
    _hook("S-D04-A",kk_shiori_early_truth)
    _hook("S-D04-B",lambda: kk_flag("shiori_alasan_kedua"))
    _hook("S14-A",lambda: (kk_shiori_winter(),kk_flag("shiori_mendengar_maaf")))
    _hook("S14-B",kk_shiori_winter)
    _hook("S14-C",kk_shiori_winter)
    _hook("S15-A",lambda: kk_flag("shiori_doa_ditanya"))
    _hook("S16-A",kk_shiori_winter)
    _hook("S16-B",kk_shiori_winter)
    _hook("S16-C",kk_shiori_winter)
    _hook("S13-A",kk_shiori_admission)
    _hook("S13-B",kk_shiori_revenge)
    _hook("S13-C",kk_shiori_revenge)
    _hook("S17-A",lambda: kk_flag("shiori_warisan_didukung"))

# ┌─ PANDUAN CERITA · S-D09 · Papan yang Ditinggalkan
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : tahap 3
# │ INTI    : A Lanjutkan dengan satu langkah / B bereskan / C tinggalkan
# │ AKHIRAN : langkah balasan bisa menjadi pengakuan; S20 datang lebih awal
# └─ tulis / perbaiki dialog di bawah ──
label kk_inspect_board(place):
    if not kk_unfinished_board(place):
        return
    nar "Papan yang ditinggalkan Shiori mengulang posisi yang pernah dibahas bersama. Ada jawaban yang saat itu tidak kauambil karena risikonya, bukan karena tak melihatnya. Kini bidak itu menunggu tanpa pemiliknya berada di hadapanmu."
    call kk_family_menu("S-D09", ["Balas dengan langkah yang dulu urung kaumainkan.", "Masukkan bidak ke dalam kotaknya.", "Biarkan papan tetap seperti itu."])
    if _return == "A":
        nar "Kau membiarkan bidak itu di petaknya yang baru. Kali ini Shiori bisa melihat jawabanmu ketika ia kembali."
        nar "Itu belum percakapan yang lengkap. Setidaknya kau memilih meninggalkan sesuatu yang bisa dibaca sebagai tanggung jawab atas langkahmu sendiri, alih-alih menunggu semua pertanyaan dimulai olehnya."
    elif _return == "B":
        nar "Kau memasukkan bidak ke kotak, memutuskan pertandingan yang belum selesai tidak perlu diteruskan. Ketika kembali, Shiori akan menemukan meja rapi dan satu cara berbicara yang tidak lagi tersedia."
    else:
        nar "Kau membiarkan papan tetap seperti itu. Posisi tersebut tidak memburuk, tidak pula mendapatkan jawaban. Waktu yang berjalan di luar papan tidak tunduk pada kesabaran kayu-kayu kecil di atasnya."
    $ kk_minutes(10)
    return

# ┌─ PANDUAN CERITA · S18 · Hujan Terakhir: Pengumpulan Bukti
# │ LOKASI  : Distrik Elite · Rumah Saionji
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia mengumpulkan.
# │ INTI    : A hapus bukti / B perbaiki / C tidak peduli.
# │ AKHIRAN : stage 4; titik tanpa balik setelah ini hanya ending Distorted/Bad.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S18:
    call kk_scene_enter("shiori","Rumah Saionji saat hujan")
    if kk_has("shiori_langkah_balasan"):
        shiori "Aku lihat langkah yang kautinggalkan di klub. Sekarang aku ingin mendengar jawabanmu sendiri."
    else:
        shiori "Aku ingin mendengar jawabanmu sebelum aku meneruskan ini."
    nar "Map di meja berisi catatan yang bisa mengubah cara orang lain membaca perbuatanmu. Shiori menutupnya, mengatakan masih memberi kesempatan meluruskan kepada pihak yang dirugikan, lalu keluar sebentar menemui keluarganya."
    call kk_family_menu("S18", ["Masuk tanpa izin untuk menghapus catatan itu.", "Luruskan ceritamu kepada orang yang ikut dirugikan.", "Biarkan catatan itu dan pulang."])
    if _return == "A":
        "Kuroiwa" "Anda tidak diizinkan masuk ke ruangan ini."
        nar "Ia menghentikanmu sebelum berkas itu hilang. Sekarang ia juga tahu apa yang hendak kaulakukan."
        nar "Shiori kembali setelah dipanggil. Ia tidak tampak terkejut oleh niatmu, tetapi kecewanya terlihat pada jeda sebelum ia menanyakan apakah masih ada penjelasan yang hendak kaupertahankan."
    elif _return == "B":
        if kk_has("shiori_menemukan_kebohongan_shena"):
            nar "Kau menelepon Miono sendiri. Kau menceritakan apa yang sebenarnya kaukatakan tentang Shena, tanpa meminta Shiori menutupinya."
        else:
            nar "Kau menghubungi orang yang dirugikan dan meluruskan ceritamu, kali ini atas namamu sendiri."
        nar "Kau tidak meminta Shiori menanggung malu atau amarah yang muncul dari koreksi itu. Ia mendengar cukup banyak untuk mengetahui bahwa kali ini ada akibat yang bersedia kauhadapi tanpa lebih dahulu mencari cara agar tampak menang."
    else:
        nar "Kau pulang tanpa menanggapi. Map tetap di meja dan kesempatan terakhir untuk menjelaskan sendiri tidak otomatis ikut pulang bersamamu."
        nar "Di luar, hujan tidak cukup deras untuk menahanmu. Kau tidak punya kebetulan yang dapat disalahkan atas keputusan pergi."
    return

init 1 python:
    def kk_shiori_files():
        kk_stage("shiori",max(4,stage.get("shiori",0)))

    def kk_shiori_intrusion():
        kk_shiori_files()
        kk_flag("saionji_masuk_tanpa_izin")

    _hook("S18-A",kk_shiori_intrusion)
    _hook("S18-B",lambda: kk_flag("shiori_koreksi_disampaikan"))
    _hook("S18-C",kk_shiori_files)
    _hook("S-D09-A",lambda: kk_flag("shiori_langkah_balasan"))
