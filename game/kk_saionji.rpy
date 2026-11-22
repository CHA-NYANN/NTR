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
        "Ayah Shiori" "Lho, di luar kan anginnya dingin sekali. Masa teman Shiori datang malam Natal cuma disuruh berdiri di serambi?"
        nar "Shiori yang berdiri di hadapanmu mengenakan kardigan rajut putih keperakan di atas blus rumahan hanya menggeleng kecil mendengar percakapan kedua orang tuanya yang bocor sampai ke pintu depan. Ia menerima buku dari tanganmu, lalu menatapmu dengan senyum tipisnya."
        shiori "Maaf ya, Amamiya-san, suara mereka terdengar sampai ke sini. Tapi seperti yang baru saja kamu dengar sendiri, kami memang baru mau mulai makan malam."
        chiasa "Aku yang nggak enak, Saionji-senpai. Harusnya aku balikin bukunya kemarin siang di kampus, malah ganggu jam makan malam keluarga."
        shiori "Sama sekali tidak mengganggu. Kalau kamu belum punya janji makan malam di tempat lain, silakan masuk dan makan bersama kami. Ayah dan Ibu jauh lebih santai diajak mengobrol daripada reputasi nama Saionji yang sering dibicarakan orang di kampus. Biasanya, sih."
    else:
        nar "Kediaman keluarga Saionji di distrik elite malam itu tampak tenang di balik pagar tanaman pangkas dan pendar lampu taman berwarna kuning hangat. Ketika Kuroiwa membukakan pintu kayu besar di serambi depan untukmu yang mampir mengembalikan buku catatan strategi pinjaman sebelum libur akhir tahun, pemandangan di dalam rumah sama sekali tidak menyerupai pesta resmi keluarga konglomerat yang pernah disinggung orang tuamu."
        nar "Tidak ada deretan tamu berjas atau iringan musik kaku. Sebaliknya, dari arah ruang makan di ujung lorong kayu, tercium aroma sup krim jagung yang baru matang, roti panggang mentega, dan ayam panggang herba."
        nar "Dari balik pintu ruang makan yang terbuka separuh, terdengar suara berat ayah Shiori, Saionji Shigeru, yang sedang menggeser kursi tambahan, disusul teguran lembut ibunya, Saionji Akane."
        "Ibu Shiori" "Ayah, jangan keburu menarik kursinya dulu. Teman Shiori kan baru sampai di depan pintu, nanti anaknya malah sungkan dan merasa dipaksa masuk kalau memang cuma mau mampir sebentar."
        "Ayah Shiori" "Lho, di luar angin malam Natal dingin sekali. Masa tamu Shiori datang jauh-jauh cuma dibiarkan berdiri di serambi depan?"
        nar "Shiori yang berdiri di hadapanmu mengenakan kardigan rajut putih keperakan di atas blus rumahan menghela napas kecil mendengar percakapan kedua orang tuanya yang terdengar jelas sampai ke genkan. Ia menerima buku dari tanganmu, lalu menatapmu dengan senyum tipis."
        shiori "Maaf, Kisaragi-san, suara mereka memang agak sulit ditahan kalau sudah soal tamu. Tapi seperti yang baru saja kamu dengar sendiri, kami memang baru mau mulai makan malam."
        yutaka "Aku yang jadi nggak enak, Saionji-san. Harusnya buku ini kubalikin kemarin siang di fakultas, malah datang pas jam makan malam keluargamu."
        shiori "Tidak mengganggu sama sekali. Kalau kamu belum punya janji makan malam di tempat lain, silakan masuk. Ayah dan Ibu jauh lebih mudah diajak mengobrol daripada reputasi nama Saionji yang sering dibicarakan orang di luar sana. Biasanya, sih."
    call kk_family_menu("S07", ["\"Terima kasih. Kalau tidak merepotkan, aku ikut makan malam bersama.\"", "\"Selamat Natal untuk keluarga di rumah ya. Aku langsung pamit saja.\"", "\"Aku tidak bisa lama-lama, tapi aku bawa bingkisan kecil ini buat keluargamu.\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Terima kasih, Saionji-senpai. Kalau memang nggak merepotkan Paman dan Bibi, aku ikut makan malam bersama."
            shiori "Kalau begitu silakan lepas mantelmu di sini. Biar kugantungkan di lemari depan."
            nar "Kamu melepas sepatu dan mantel tebalmu di genkan, lalu mengikuti Shiori masuk ke ruang makan yang hangat oleh lampu gantung kaca berwarna gading. Begitu melihatmu masuk, Saionji Akane langsung meletakkan sendok sup besar dan menyambutmu dengan senyum ramah, sementara Shigeru menarik kursi kayu tepat di sebelah Shiori."
            "Ibu Shiori" "Selamat malam, Amamiya Chiasa-san, benar kan? Shiori beberapa kali menyebut namamu waktu kami minum teh minggu lalu. Ayo duduk, tanganmu pasti dingin habis jalan dari stasiun."
            chiasa "Selamat malam, Bibi, Paman. Maaf saya datang mendadak malam Natal begini."
            "Ayah Shiori" "Justru menyenangkan kalau ada teman Shiori yang mampir. Rumah sebesar ini kalau malam Natal cuma diisi kami bertiga rasanya sepi sekali. Sini, piring supnya sudah hangat."
            nar "Saat makan malam dimulai, suasana di meja itu terasa mengejutkan karena begitu mirip dengan keluarga biasa yang hangat. Tidak ada satu pun pertanyaan tentang pekerjaan orang tuamu atau relasi keluarga. Shigeru menceritakan betapa ia baru saja dikalahkan Shiori tiga babak catur berturut-turut sore tadi, sementara Akane menanyakan makanan apa yang paling kamu sukai di kantin kampus."
            chiasa "Sup jagungnya enak sekali, Bibi. Manisnya pas dan hangat di tenggorokan."
            "Ibu Shiori" "Syukurlah kalau cocok di lidahmu, Chiasa-san. Ngomong-ngomong, kalau di kampus Shiori tidak terlalu galak atau menyendiri kan? Kadang Ibu khawatir kalau dia terlalu lama di ruang klub catur, teman-teman seangkatannya jadi segan mengajak mengobrol, apalagi waktu acara fakultas kemarin..."
            nar "Pertanyaan beruntun dari ibunya yang penuh perhatian membuatmu sempat terdiam sambil memegang sendok, bingung harus menjawab seberapa jauh. Di sebelahmu, Shiori meletakkan gelas airnya dengan bunyi pelan sambil menahan senyum geli."
            shiori "Ibu, tahan dulu pertanyaannya. Amamiya-san baru selesai makan setengah mangkuk supnya. Kalau Ibu bertanya terus dengan nada serius begitu, nanti dia mengira sedang ikut wawancara yayasan beasiswa Ibu."
            "Ibu Shiori" "Eh? Ya ampun, maafkan Bibi ya, Chiasa-san. Bibi cuma senang akhirnya ada teman kampus Shiori yang mampir makan ke rumah."
            chiasa "Nggak apa-apa kok, Bibi. Di kampus Saionji-senpai baik banget sama saya."
            "Ayah Shiori" "Haha, kamu dengar sendiri kan, Bu? Sudah, biarkan Chiasa-san makan ayam panggangnya dulu sebelum dingin."
            nar "Shiori melirikmu dari sudut matanya dengan senyum tipis yang hangat, lalu menggeser piring roti mentega lebih dekat ke jangkauanmu sementara obrolan meja makan kembali mengalir santai."
        else:
            yutaka "Terima kasih, Saionji-san. Kalau memang nggak merepotkan Paman dan Bibi, aku ikut makan malam bersama deh."
            shiori "Kalau begitu silakan lepas mantelmu di sini. Biar kutaruh di gantungan depan."
            nar "Kamu melepas sepatu dan mantelmu di genkan, lalu mengikuti Shiori masuk ke ruang makan yang hangat oleh cahaya lampu gantung kaca berwarna gading. Begitu kamu muncul di ambang pintu, Saionji Akane langsung menggeser piring sup untuk menyiapkan tempatmu sambil tersenyum ramah, sementara Shigeru menarik kursi kayu di samping Shiori."
            "Ibu Shiori" "Selamat malam, Kisaragi Yutaka-san, benar kan? Shiori sempat menyebut namamu minggu lalu saat bercerita soal teman satu fakultas yang suka berdiskusi di klub catur. Ayo duduk, supnya baru saja dituang."
            yutaka "Selamat malam, Bibi, Paman. Maaf saya datang mendadak malam Natal begini."
            "Ayah Shiori" "Justru kami yang senang ada tamu malam ini. Rumah sebesar ini kalau cuma makan bertiga rasanya terlalu hening. Duduklah, jangan sungkan."
            nar "Selama makan malam berlangsung, tidak ada satu pun pertanyaan tentang perusahaan keluarga Kisaragi ataupun relasi bisnis yang selama ini kamu duga bakal keluar dari meja orang berada. Shigeru bercerita sambil tertawa kecil tentang tiga kekalahan catur beruntun dari putrinya sore tadi, sementara Akane menanyakan mata kuliah yang paling kamu sukai serta jajanan kantin favoritmu."
            yutaka "Sup jagungnya enak sekali, Bibi. Hangat banget pas buat malam sedingin ini."
            "Ibu Shiori" "Syukurlah kalau kamu suka, Kisaragi-san. Omong-omong, kalau di kelas Ekonomi Shiori tidak terlalu jaga jarak sama teman-teman seangkatannya kan? Bibi kadang kepikiran kalau dia terlalu sibuk di ruang klub sampai jarang makan siang bareng yang lain, padahal..."
            nar "Rentetan pertanyaan tulus dari Akane membuatmu sedikit kikuk di atas kursi sambil memegang sendok, tidak terbiasa menghadapi keramahan orang tua yang langsung akrab seperti ini. Melihat ekspresimu, Shiori menurunkan gelas airnya dengan bunyi pelan sembari menahan senyum geli."
            shiori "Ibu, pelan-pelan dulu pertanyaannya. Kisaragi-san bahkan belum sempat menyentuh ayam panggangnya. Kalau Ibu terus bertanya serinci itu, nanti dia malah merasa sedang menghadapi rapat evaluasi yayasan Ibu."
            "Ibu Shiori" "Eh? Ya ampun, maaf ya, Kisaragi-san. Bibi cuma kelewat senang akhirnya Shiori membawa teman satu fakultas makan malam di rumah."
            yutaka "Nggak apa-apa kok, Bibi. Di kampus Saionji-san memang paling sering bikin lawan tandingnya mikir keras, tapi dia baik banget sama saya."
            "Ayah Shiori" "Haha, dengar sendiri kan, Bu? Ayo, Kisaragi-san, habiskan dulu ayam panggangnya sebelum dingin."
            nar "Shiori melirikmu sekilas dari balik gelasnya dengan senyum tipis yang geli, lalu menggeser piring roti panggang mentega lebih dekat ke depanmu sementara obrolan santai meja makan berlanjut tanpa beban."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Terima kasih banyak tawarannya, Saionji-senpai, tapi aku nggak mau ganggu waktu makan malam keluarga Senpai. Selamat Natal buat Senpai, Paman, dan Bibi di rumah ya. Aku langsung pamit pulang aja."
            nar "Shiori sama sekali tidak memasang wajah kecewa atau mendesakmu masuk demi basa-basi. Ia merapikan posisi buku di pelukannya dan mengangguk tenang."
            shiori "Aku mengerti, kamu pasti juga sudah ditunggu di rumah. Akan kusampaikan salam Natalmu kepada Ayah dan Ibu di ruang makan."
            chiasa "Maaf ya jadi bikin Senpai keluar ke serambi pas baru mau makan."
            shiori "Tidak masalah sama sekali. Justru aku senang kamu menyempatkan mampir mengantar buku ini sendiri sebelum tahun baru."
            nar "Ketika Kuroiwa membuka kembali pintu depan untukmu, Shiori melangkah setengah tapak mengantarmu sampai ke batas genkan."
            shiori "Lain kali kalau kamu lewat dekat sini atau ingin main satu babak lagi di rumah, mampir saja, Amamiya-san. Kamu tidak harus menunggu ada hari raya atau alasan mengembalikan buku dulu untuk diizinkan duduk makan di meja kami."
            chiasa "Terima kasih, Saionji-senpai. Selamat malam."
            shiori "Selamat malam. Hati-hati di jalan, angin malam ini cukup dingin."
            nar "Pintu kayu serambi tertutup pelan di belakangmu setelah kamu melangkah keluar ke jalan setapak taman yang tenang."
        else:
            yutaka "Terima kasih banyak tawarannya, Saionji-san, tapi aku nggak enak kalau mengganggu waktu makan malam keluargamu. Selamat Natal ya buat kamu, Paman, sama Bibi di dalam. Aku langsung pamit aja."
            nar "Shiori tidak tampak tersinggung sedikit pun dan tidak memaksamu masuk demi sekadar sopan santun. Ia mendekap buku yang baru kamu kembalikan lalu mengangguk tenang."
            shiori "Baiklah, aku mengerti. Akan kusampaikan ucapan selamat Natalmu kepada Ayah dan Ibu di ruang makan."
            yutaka "Maaf ya jadi bikin kamu berdiri di serambi pas supnya baru dihidangkan."
            shiori "Tidak masalah. Terima kasih sudah menyempatkan diri mengantar buku ini langsung sebelum libur panjang."
            nar "Ketika Kuroiwa membukakan pintu kayu serambi untukmu, Shiori melangkah maju sedikit mengantarmu sampai tepi genkan."
            shiori "Lain kali kalau kamu sedang luang di sekitar sini, mampir saja, Kisaragi-san. Kamu tidak harus menunggu hari raya atau alasan mengembalikan buku dulu untuk diizinkan makan malam di rumah ini."
            yutaka "Oke, lain kali pasti kumanfaatkan tawarannya. Selamat malam, Saionji-san."
            shiori "Selamat malam. Hati-hati di jalan, angin malam ini cukup tajam."
            nar "Kamu melangkah menuruni jalan setapak taman yang tenang sementara pintu kayu besar rumah Saionji menutup perlahan di belakangmu."
    else:
        if kk_host == "chiasa":
            nar "Kamu membuka tas selempangmu dan mengeluarkan sebuah kotak kaleng kecil berwarna hijau tua yang diikat pita krem, berisi daun teh panggang pilihan dari kedai tua dekat stasiun timur, lalu menyodorkannya dengan kedua tangan."
            chiasa "Maaf malam ini aku nggak bisa mampir makan, Saionji-senpai, soalnya di rumah sudah masak juga. Tapi aku bawa bingkisan teh ini buat Senpai sama keluarga di rumah. Selamat Natal ya."
            nar "Mata ungu Shiori turun menatap kaleng teh tersebut. Ia meletakkan buku pinjamannya di atas meja konsol serambi terlebih dahulu agar bisa menerima kotak teh darimu dengan kedua tangan."
            shiori "Ini daun teh panggang dari kedai tua di seberang stasiun timur, bukan? Wanginya khas sekali, bahkan dari luar kalengnya. Pilihan yang sangat cermat, Amamiya-san."
            chiasa "Syukurlah kalau Senpai kenal kedainya. Penjaga tokonya tadi bilang teh ini enak diseduh habis makan makanan yang berlemak atau bersantan."
            shiori "Ayahku sangat menyukai teh panggang dari kedai itu. Biar kubawa langsung ke meja makan kami, tidak dicampur dengan tumpukan parsel di ruang depan."
            nar "Shiori memegang kaleng teh itu dengan hati-hati, lalu menatapmu lagi."
            shiori "Kalau begitu, ada pesan singkat yang ingin kamu titipkan untuk Ayah dan Ibu bersama teh ini? Aku ingin mereka menerimanya sebagai perhatian pribadimu sendiri supaya tidak tercampur dengan parsel formal dari rekan bisnis Ayah."
            chiasa "Bilang aja semoga Paman, Bibi, dan Saionji-senpai suka tehnya buat diminum hangat-hangat sehabis makan malam Natal bersama."
            shiori "Kalimat yang jujur dan tanpa embel-embel. Akan kusampaikan persis seperti yang kamu ucapkan barusan. Terima kasih banyak untuk perhatiannya malam ini, Amamiya-san."
            chiasa "Sama-sama, Senpai. Aku pamit dulu ya, selamat malam."
            nar "Shiori mengangguk anggun dengan senyum yang tampak lebih lembut daripada biasanya, lalu tetap berdiri di ambang serambi sampai kamu melewati gerbang halaman depan."
        else:
            nar "Kamu mengeluarkan sebuah kotak kaleng hijau tua berpita krem dari kantong kertas yang sejak tadi kamu bawa, berisi daun teh panggang pilihan dari kedai tua di dekat stasiun timur, lalu menyodorkannya dengan sopan."
            yutaka "Maaf malam ini aku nggak bisa ikut makan, Saionji-san. Tapi aku bawa bingkisan teh kecil ini buat kamu sama orang tuamu di rumah. Selamat Natal ya."
            nar "Tatapan ungu Shiori turun mengamati kaleng teh di tanganmu. Ia meletakkan buku pinjamannya di atas meja konsol serambi terlebih dulu, lalu menerima kotak teh itu dengan kedua tangan."
            shiori "Daun teh panggang dari kedai tua di seberang stasiun timur, bukan? Wanginya bahkan masih terasa tipis dari balik tutup kalengnya. Kamu tahu betul cara memilih hadiah yang tidak terasa dibuat-buat, Kisaragi-san."
            yutaka "Syukurlah kalau cocok. Pemilik kedainya tadi bilang teh panggang yang ini paling pas diseduh sehabis makan malam."
            shiori "Ayahku memang sangat menyukai teh dari kedai itu. Biar kubawa langsung ke ruang makan kami sendiri, tidak kutaruh bersama tumpukan parsel akhir tahun di ruang depan."
            nar "Shiori menimbang kaleng teh itu sejenak lalu mengangkat pandangannya kembali padamu."
            shiori "Ada pesan singkat yang ingin kamu titipkan bersama teh ini untuk Ayah dan Ibu? Aku ingin memastikan mereka mengenalinya sebagai niat pribadimu sendiri supaya tidak disamakan dengan bingkisan relasi bisnis di depan."
            yutaka "Sampaikan aja salam Natal dariku, semoga Paman, Bibi, sama kamu bisa menikmati tehnya hangat-hangat habis makan malam nanti."
            shiori "Sederhana dan jelas. Akan kusampaikan tepat seperti itu. Terima kasih sudah menyempatkan mampir malam ini, Kisaragi-san."
            yutaka "Sama-sama, Saionji-san. Aku pamit pulang dulu ya, selamat malam."
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
    nar "Ibu Shiori mengenalimu dari meja makan malam Natal. Ia menuangkan dua cangkir teh."
    "Ibu Shiori" "Di rumah ia sering duduk sendiri. Aku tahu dia menyukainya kadang-kadang. Aku hanya ingin tahu apakah di kampus dia punya teman yang memang diinginkan, bukan orang yang merasa harus dekat."
    call kk_family_menu("S-D08", ["Ceritakan apa yang kaulihat tanpa menebak perasaannya.", "Katakan bahwa semua orang selalu ingin bersamanya.", "Ulangi obrolan pribadi kalian kepada ibunya."])
    if _return == "A":
        "Ibu Shiori" "Terima kasih. Mungkin aku harus bertanya sendiri padanya."
        nar "Kau menceritakan yang kaulihat tanpa menebak seluruh perasaan Shiori. Ibunya tampak lega, lalu meminta agar kau tidak merasa perlu menjadi juru bicara putrinya pada pertemuan berikutnya."
    elif _return == "B":
        nar "Kau menyanjung seolah semua orang selalu ingin bersamanya. Ibunya tersenyum sopan, tetapi menanyakan apakah Shiori sendiri senang berada di tengah mereka. Pujianmu ternyata belum menjawab hal yang dikhawatirkannya."
    else:
        nar "Ibu Shiori meletakkan cangkirnya. Baru sekarang kau sadar itu cerita Shiori untukmu."
        "Ibu Shiori" "Aku ingin mengenal kabarnya. Aku tidak memintamu menyerahkan kepercayaan yang diberikan kepadamu. Yang ini lebih baik dia sendiri yang menceritakan."
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
        chiasa "Yah, kalah lagi deh. Padahal tadi aku sudah yakin pertahanan di sisi kiriku aman, Saionji-senpai."
        shiori "Langkah bentengmu di giliran kedua puluh sebenarnya sudah cukup bagus, Amamiya-san. Kamu hanya sedikit lengah saat membiarkan diagonal tengah terbuka."
        nar "Shiori mulai memungut bidak-bidak kayu dari atas papan lalu memasukkannya ke dalam kotak beludru satu per satu sebelum percakapan benar-benar selesai. Gerakan tangannya yang biasanya rapi dan cepat perlahan melambat. Tepat ketika hanya tersisa dua bidak raja di atas papan, jemarinya berhenti mengetuk pelan tepi kotak kayu."
        nar "Ia menatap dua bidak terakhir itu cukup lama, seolah sedang menimbang sebuah pertanyaan yang sama sekali tidak bisa diuji dengan membaca tiga langkah lawan. Ketika ia akhirnya mengangkat wajah menatapmu, senyum sopan seragam yang biasa ia kenakan di depan kerumunan sudah tidak ada di sana."
        shiori "Amamiya-san, boleh aku bertanya satu hal di luar papan catur?"
        chiasa "Boleh kok, Senpai. Ada apa?"
        shiori "Selama bertahun-tahun, hampir setiap orang yang duduk di hadapanku selalu datang membawa sesuatu yang ingin mereka minta atau tukarkan. Ada yang menginginkan nama keluargaku, ada yang menginginkan undangan acara bisnis, ada pula yang sekadar ingin membuktikan bisa mengalahkanku di papan."
        nar "Shiori meletakkan kedua tangannya tenang di atas meja, mata ungunya menatapmu jernih tanpa sedikit pun nada menyindir."
        shiori "Kalau suatu hari aku datang menemuimu tanpa papan catur, tanpa undangan pesta, dan tanpa satu pun keuntungan yang bisa kuberikan kepadamu... apakah kamu masih mau duduk di sini bersamaku? Aku tahu pertanyaan ini terdengar terlalu bersungguh-sungguh. Memang aku sedang bersungguh-sungguh sekarang."
    else:
        nar "Satu per satu anggota Klub Catur lainnya berpamitan meninggalkan ruangan hingga hanya menyisakan kamu dan Saionji Shiori di meja kayu dekat jendela. Pertandingan latihan di antara kalian baru saja berakhir setelah pertukaran kuda di tengah papan membuka jalan bagi menteri putih Shiori menutup seluruh langkah rajamu."
        yutaka "Kalah lagi. Padahal kupikir tadi pertukaran kudaku di tengah papan sudah cukup buat nahan seranganmu, Saionji-san."
        shiori "Langkahmu di giliran kedelapan belas sebenarnya lumayan berani, Kisaragi-san. Kamu hanya sedikit terlalu cepat membuka barisan bidak di sayap kanan."
        nar "Shiori mulai memungut bidak-bidak kayu dari atas papan lalu memasukkannya ke dalam kotak beludru satu per satu sebelum percakapan selesai. Gerakan tangannya yang biasanya rapi dan cepat perlahan melambat. Tepat ketika hanya tersisa dua bidak raja di atas papan, jemarinya berhenti mengetuk pelan tepi kotak penyimpanan."
        nar "Ia memandangi dua bidak terakhir itu cukup lama, seolah sedang menimbang sebuah pertanyaan yang tidak bisa diuji dengan membaca tiga langkah lawan. Ketika ia akhirnya mengangkat wajah menatapmu, senyum sopan seragam yang biasa ia kenakan di depan kerumunan sudah lenyap dari bibirnya."
        shiori "Kisaragi-san, boleh aku bertanya satu hal di luar papan catur?"
        yutaka "Boleh aja. Ada apa?"
        shiori "Sebagai mahasiswa dari keluarga yang punya perusahaan sendiri di fakultas yang sama, kurasa kamu juga cukup paham. Selama bertahun-tahun, hampir setiap orang yang duduk di hadapanku selalu datang membawa sesuatu yang ingin mereka minta atau tukarkan. Ada yang menginginkan nama keluargaku, ada yang menginginkan undangan acara bisnis, ada pula yang sekadar ingin membuktikan bisa mengalahkanku di papan."
        nar "Shiori meletakkan kedua tangannya tenang di atas meja, mata ungunya menatapmu jernih tanpa sedikit pun nada menyindir."
        shiori "Kalau suatu hari aku datang menemuimu tanpa papan catur, tanpa undangan pesta, dan tanpa satu pun keuntungan yang bisa kuberikan kepadamu... apakah kamu masih mau duduk di sini bersamaku? Aku tahu itu terdengar terlalu bersungguh-sungguh. Memang aku sedang bersungguh-sungguh sekarang."
    call kk_family_menu("S09", ["\"Tutup aja papannya sekarang. Nggak usah buru-buru pulang, duduk sini dan cerita apa aja.\"", "\"Jujur aja, aku lebih nyaman kalau kita tetap ketemu sebatas buat main catur aja.\"", "\"Tentu aja aku mau jadi temanmu. Ngomong-ngomong, boleh kenalin aku ke relasi keluargamu nanti?\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Tutup aja papannya sekarang, Saionji-senpai. Sejak awal aku datang ke ruangan ini juga bukan karena undangan pesta atau nama keluarga Senpai kok. Kalau Senpai belum buru-buru pulang, duduk aja di sini, kita ngobrol biasa tanpa perlu mikirin langkah apa-apa."
            nar "Kamu mendorong papan catur sedikit ke tepi meja lalu menggeser kursimu agar lebih santai. Shiori terdiam sepersekian detik melihat betapa tanpa ragunya kamu menjawab. Perlahan, sebuah senyum kecil yang jauh lebih tulus muncul di sudut bibirnya."
            nar "Ia memasukkan dua bidak terakhir ke kotak beludru, mengaitkan kunci kuningan kotaknya, lalu menarik kursinya kembali mendekat ke meja."
            shiori "Baik. Terima kasih sudah menjawab tanpa berputar-putar, Amamiya-san. Kalau begitu, aku ingin mencoba sesuatu yang jarang sekali kulakukan."
            chiasa "Mencoba apa, Senpai?"
            shiori "Aku ingin bercerita tentang hal-hal yang sama sekali membosankan dari hariku. Dan kalau kamu mulai bosan mendengarkannya, kamu boleh langsung bilang. Aku ingin belajar berhenti menebak-nebak isi pikiran orang di depanku terus-menerus."
            chiasa "Sepakat! Ayo cerita aja, memangnya hari ini ada kejadian membosankan apa di fakultas Senpai?"
            nar "Shiori tertawa pelan, suara tawa yang jauh lebih ringan daripada biasanya, lalu menuangkan sisa teh hangat ke dua cangkir."
            shiori "Tadi ada rapat pengurus akademik hampir dua jam penuh, dan tebak apa yang paling lama diperdebatkan oleh sepuluh mahasiswa terbaik di ruangan itu. Ukuran huruf dan warna bingkai untuk papan pengumuman semester depan. Aku sampai harus menahan diri keras-keras supaya tidak menyarankan kami melempar koin saja."
            chiasa "Haha, dua jam cuma buat bahas ukuran huruf papan pengumuman? Pantas aja Senpai kelihatan capek tadi."
            shiori "Belum selesai. Kemarin sepulang dari kampus, Kuroiwa diam-diam mampir membeli dua potong dorayaki hangat dari kedai kecil di pinggir jalan, lalu menyodorkannya kepadaku di dalam mobil sambil bersikeras dengan wajah kaku bahwa itu adalah prosedur uji kualitas makanan jajanan lokal, padahal aku tahu betul ia cuma melihatku melewatkan makan."
            chiasa "Wah, Pak Kuroiwa ternyata perhatian banget ya meskipun mukanya selalu kelihatan serius."
            shiori "Memang begitu orangnya. Oh iya, belakangan ini juga aku sedang membaca ulang satu seri novel ringan bergenre strategi militer setiap kali penat membaca buku ekonomi. Ilustrasi sampul dan karakternya sangat rapi dan berkarakter. Kalau kamu sempat, suatu hari aku ingin meminjamkannya padamu."
            chiasa "Eh... novel strategi? Kapan-kapan boleh banget aku lihat, Senpai."
            nar "Kamu ikut menceritakan kesibukan kelas seni serta beberapa tingkah konyol di rumahmu, dan Shiori mendengarkan dengan tenang sambil sesekali menimpali dengan komentar kering yang justru membuat kalian berdua tertawa. Kalian tetap tinggal di ruangan itu jauh setelah jam klub berakhir, menemukan bahwa pembicaraan biasa tanpa taruhan apa pun ternyata bisa menjadi sesuatu yang ingin ditunggu."
        else:
            yutaka "Tutup aja papannya sekarang, Saionji-san. Kamu kan tahu sendiri aku paling malas sama acara bisnis keluarga segala macam. Sejak awal aku duduk di sini jelas bukan buat nyari undangan pesta. Kalau kamu belum buru-buru dijemput, duduk aja dulu di sini, kita ngobrol santai tanpa perlu mikirin strategi apa-apa."
            nar "Kamu mendorong papan catur sedikit ke tepi meja lalu menyandarkan punggungmu dengan santai. Shiori terdiam sepersekian detik melihat betapa tanpa ragunya kamu menjawab. Perlahan, sebuah senyum kecil yang jauh lebih tulus muncul di sudut bibirnya."
            nar "Ia memasukkan dua bidak terakhir ke kotak beludru, mengaitkan kunci kuningan kotaknya, lalu menarik kursinya kembali mendekat ke meja."
            shiori "Baik. Terima kasih sudah menjawab tanpa berputar-putar, Kisaragi-san. Kalau begitu, aku ingin mencoba sesuatu yang jarang sekali kulakukan."
            yutaka "Mencoba apa memangnya?"
            shiori "Aku ingin bercerita tentang hal-hal yang sama sekali membosankan dari hariku. Dan kalau kamu mulai bosan mendengarkannya, kamu boleh langsung bilang. Aku ingin belajar berhenti menebak-nebak isi pikiran orang di depanku terus-menerus."
            yutaka "Boleh banget. Ayo cerita aja, memangnya tadi ada kejadian membosankan apa di gedung fakultas kita?"
            nar "Shiori tertawa pelan, suara tawa yang jauh lebih ringan daripada biasanya, lalu menuangkan sisa teh hangat ke dua cangkir."
            shiori "Tadi ada rapat pengurus akademik hampir dua jam penuh, dan tebak apa yang paling lama diperdebatkan oleh sepuluh mahasiswa terbaik di ruangan itu. Ukuran huruf dan warna bingkai untuk papan pengumuman semester depan. Aku sampai harus menahan diri keras-keras supaya tidak menyarankan kami melempar koin saja."
            yutaka "Hahaha, khas banget anak-anak pengurus fakultas kita. Dua jam cuma buat berdebat soal ukuran huruf papan pengumuman?"
            shiori "Belum selesai. Kemarin sepulang dari kampus, Kuroiwa diam-diam mampir membeli dua potong dorayaki hangat dari kedai kecil di pinggir jalan, lalu menyodorkannya kepadaku di dalam mobil sambil bersikeras dengan wajah kaku bahwa itu adalah prosedur uji kualitas makanan jajanan lokal, padahal aku tahu betul ia cuma melihatku melewatkan makan."
            yutaka "Pak Kuroiwa ternyata asyik juga ya kalau lagi di luar urusan jaga pintu."
            shiori "Memang begitu orangnya. Oh iya, belakangan ini juga aku sering membaca satu seri novel ringan strategi setiap kali penat membaca jurnal ekonomi. Mungkin terdengar kekanak-kanakan, tapi alur pikirannya lumayan menghibur."
            nar "Kamu ikut menimpali dengan cerita ringan soal teman-teman kelasmu yang selalu panik menjelang tugas akhir, dan Shiori mendengarkan sambil sesekali melempar komentar kering yang membuat kalian berdua tertawa. Kalian tetap tinggal di ruangan itu jauh setelah jam klub berakhir, menemukan bahwa pembicaraan biasa tanpa taruhan apa pun ternyata bisa menjadi sesuatu yang ingin ditunggu."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kamu terdiam sebentar menatap dua bidak kayu di tangan Shiori, lalu menjawab dengan nada tenang tanpa berusaha memperhalus maksudmu dengan janji kosong."
            chiasa "Maaf ya, Saionji-senpai. Kalau boleh jujur, aku rasa aku jauh lebih nyaman kalau kita tetap ketemu sebatas buat main catur di ruang klub ini aja. Aku nggak terlalu pintar mengurus hubungan pertemanan yang terlalu dekat."
            nar "Tidak ada amarah atau sindiran tajam yang keluar dari wajah Shiori. Ia menatap kotak beludru yang tadi hampir dibiarkannya terbuka sebagai alasan untuk tinggal lebih lama, lalu meletakkan kedua bidak raja itu dengan rapi ke tempatnya dan mengunci kait kuningan kotaknya hingga berbunyi pelan."
            shiori "Terima kasih sudah menjawab dengan jelas, Amamiya-san. Jauh lebih baik mendengar batas yang tegas hari ini daripada melihat seseorang mengiyakan karena sungkan lalu menjauh diam-diam bulan depan."
            chiasa "Aku nggak bermaksud bikin suasana jadi canggung, Senpai."
            shiori "Kamu tidak melakukan kesalahan apa pun. Terus terang, aku sedikit kecewa. Tapi anggap saja itu sekadar pengakuan singkat, sama sekali tidak kumaksudkan supaya kamu mengubah jawabanmu."
            nar "Senyum sopan yang rapi kembali terpasang di bibir Shiori. Ia memasukkan kotak catur ke lemari penyimpanan, mengambil tas selempangnya, lalu mengangguk halus kepadamu."
            shiori "Kalau begitu sampai jumpa di jadwal latihan berikutnya, Amamiya-san. Permisi dulu."
            nar "Pintu ruang klub menutup lembut di belakangnya, menyisakan papan catur yang terlipat rapi di atas meja kayu."
        else:
            nar "Kamu terdiam sebentar menatap dua bidak kayu di tangan Shiori, lalu menjawab dengan nada tenang tanpa berusaha memperhalus maksudmu dengan janji kosong."
            yutaka "Jujur aja, Saionji-san, aku rasa aku lebih nyaman kalau kita tetap ketemu sebatas buat main catur di ruang klub ini aja. Aku nggak terlalu cocok masuk terlalu jauh ke lingkaran pertemanan pribadi."
            nar "Tidak ada amarah atau sindiran tajam yang muncul di wajah Shiori. Ia menatap kotak beludru yang tadi hampir dibiarkannya terbuka sebagai alasan untuk tinggal lebih lama, lalu meletakkan kedua bidak raja itu dengan rapi ke tempatnya dan mengunci kait kuningan kotaknya hingga berbunyi pelan."
            shiori "Terima kasih sudah menjawab dengan jelas, Kisaragi-san. Jauh lebih baik mendengar batas yang tegas hari ini daripada melihat seseorang mengiyakan karena sopan lalu menghindar diam-diam bulan depan."
            yutaka "Aku nggak bermaksud bikin suasana jadi nggak enak."
            shiori "Kamu tidak melakukan kesalahan apa pun. Terus terang, aku sedikit kecewa. Tapi anggap saja itu sekadar pengakuan singkat, sama sekali tidak kumaksudkan supaya kamu mengubah jawabanmu."
            nar "Senyum sopan yang rapi kembali terpasang di bibir Shiori. Ia menyimpan kotak catur ke lemari, mengambil tas selempangnya, lalu mengangguk halus kepadamu."
            shiori "Kalau begitu sampai jumpa di jadwal latihan berikutnya, Kisaragi-san. Permisi dulu."
            nar "Pintu ruang klub menutup lembut di belakangnya, menyisakan papan catur yang terlipat rapi di atas meja kayu."
    else:
        if kk_host == "chiasa":
            chiasa "Tentu aja aku mau jadi teman Saionji-senpai! Lagian kita kan sudah sering ngobrol di sini. Oh iya, mumpung Senpai lagi bahas soal lingkaran kenalan tadi, kapan-kapan boleh nggak Senpai kenalin aku ke beberapa kolektor atau kurator galeri seni yang sering hadir di acara keluarga Saionji? Pasti berguna banget buat portofolioku ke depannya."
            nar "Tepat pada detik kalimatmu selesai, senyum tenang yang tadi begitu jernih di wajah Shiori kembali mengeras menjadi lengkungan sopan yang seragam dan tidak terbaca. Jari-jarinya yang memegang dua bidak raja berhenti sesaat sebelum ia meletakkannya rapi ke dalam kotak."
            shiori "Oh... jadi memang ada orang lain yang ingin kamu temui rupanya, Amamiya-san."
            chiasa "Eh, maksudku kan sekalian aja kalau memang ada acara terbuka, Senpai. Aku tetap senang kok main catur bareng Senpai."
            shiori "Tentu saja. Silakan jelaskan saja jenis kurator atau galeri seperti apa yang sedang kamu incar. Aku akan mendengarkannya sampai selesai."
            nar "Ia menyimak seluruh penjelasanmu dengan sikap sangat sopan, mengangguk di tempat yang tepat, bahkan menyebutkan dua nama pameran seni terbuka yang biasa disponsori relasi bisnis keluarganya agar kamu bisa mengirim lamaran sendiri. Namun saat kamu mencoba mengembalikan obrolan ke hal-hal ringan di luar urusan itu, Shiori sudah berdiri merapikan kursi dan mengambil tasnya."
            shiori "Informasi acaranya sudah kusebutkan semua, silakan dipakai bila memang perlu. Karena waktunya sudah lewat, aku permisi duluan, Amamiya-san."
            nar "Keramahan formalnya tetap utuh sampai pintu ruang klub tertutup, tetapi tawaran persahabatan yang beberapa menit lalu baru saja ia buka kini lenyap sepenuhnya dan tidak lagi ia ulang dalam bentuk apa pun."
        else:
            yutaka "Tentu aja aku mau jadi temanmu, Saionji-san. Lagian kita kan juga satu fakultas. Oh iya, mumpung kamu lagi menyinggung soal lingkaran kenalan tadi, kapan-kapan boleh nggak kenalin aku ke beberapa eksekutif divisi logistik atau relasi bisnis di acara keluarga Saionji? Orang tuaku sempat bilang kenalan di sana bakal berguna banget buat jalur distribusiku nanti."
            nar "Tepat pada detik kalimatmu selesai, sorot tenang yang tadi begitu jernih di wajah Shiori kembali mengeras menjadi lengkungan sopan yang seragam dan tidak terbaca. Jari-jarinya yang memegang dua bidak raja berhenti sesaat sebelum ia meletakkannya rapi ke dalam kotak."
            shiori "Oh... jadi memang ada orang lain yang ingin kamu temui rupanya, Kisaragi-san."
            yutaka "Maksudku kan sekalian aja kalau memang ada acara bisnis terbuka. Aku tetap senang kok duduk ngobrol sama kamu."
            shiori "Tentu saja. Silakan sebutkan saja bidang distribusi atau nama divisi mana yang sedang dicari keluargamu. Aku akan mendengarkannya sampai selesai."
            nar "Ia menyimak seluruh penjelasanmu dengan kesopanan sempurna, mengangguk di tempat yang tepat, bahkan menyebutkan dua jadwal forum ekonomi terbuka yang biasa dihadiri mitra perusahaan keluarganya agar kamu bisa mengurus pendaftarannya sendiri. Namun saat kamu mencoba mengembalikan percakapan ke topik santai, Shiori sudah berdiri merapikan kursi dan mengambil tasnya."
            shiori "Jadwal forumnya sudah kusebutkan semua, silakan dipakai bila memang perlu. Karena waktunya sudah lewat, aku permisi duluan, Kisaragi-san."
            nar "Keramahan formalnya tetap utuh sampai pintu ruang klub tertutup, tetapi tawaran persahabatan yang beberapa menit lalu baru saja ia ulurkan kini lenyap sepenuhnya dan tidak lagi ia ulang dalam bentuk apa pun."
    return

# ┌─ PANDUAN CERITA · S-D04 · Pertanyaan Jebakan
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : daftar_kebohongan ≥ 1
# │ INTI    : A Jujur sekarang / B bohong lebih rapi / C alihkan
# │ AKHIRAN : jujur sekarang lebih murah; bohong yang ketahuan belakangan dihitung dua kali
# └─ tulis / perbaiki dialog di bawah ──
label kk_shiori_question:
    if any(c["ev"] == "C11" and c["key"] == "B" for c in choices_log):
        shiori "Waktu kita melihat ilustrasi sampul itu, kau seperti hendak mengatakan sesuatu tentang Shena. Apa aku salah ingat?"
    else:
        shiori "Aku masih memikirkan ceritamu kemarin. Ada bagian yang belum kauceritakan?"
    nar "Pertanyaannya tidak memastikan apa yang sudah diketahui. Ia memberimu satu kesempatan mengatakan bagian yang sengaja disimpan tanpa lebih dahulu perlu ditunjukkan buktinya."
    call kk_family_menu("S-D04", ["Ceritakan bagian yang sengaja kaulewatkan.", "Susun alasan lain agar ceritamu terdengar cocok.", "Balik bertanya tentang buku yang ia baca."])
    if _return == "A":
        shiori "Aku senang mendengarnya darimu sendiri."
        nar "Ia menanyakan akibat yang belum dipahami, tidak langsung menjanjikan percaya. Namun kesediaanmu bicara sebelum didesak memberinya alasan untuk tetap berada dalam percakapan."
    elif _return == "B":
        nar "Shiori mengulang satu kalimatmu persis seperti yang baru saja kauucapkan."
        shiori "Baik. Aku ingin memastikan mengingat jawabanmu dengan benar. Supaya nanti kita tidak perlu berdebat tentang kata yang sebenarnya dipakai."
    else:
        nar "Kau menanyakan buku yang dibaca. Shiori menjawab secukupnya, lalu mengatakan pertanyaannya tadi belum hilang hanya karena ia bersedia sopan mengenai topik lain."
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
    if any(c["ev"] == "C11" and c["key"] == "B" for c in choices_log):
        shiori "Di pameran itu kau bilang tidak mengenal Shena. Aku sudah membaca bukunya. Mengapa kau mengatakan itu?"
    else:
        shiori "Ada yang tidak cocok antara ceritamu dan yang kutemukan. Aku ingin mendengarnya darimu."
    if kk_has("shiori_alasan_kedua"):
        shiori "Yang itu pun berbeda dari penjelasanmu sesudah pameran."
    nar "Ia tidak menatap seperti sudah mengetahui seluruh isi kepalamu. Justru ruang untuk jawaban yang masih diberikannya membuat kebohongan berikutnya menjadi pilihan yang jelas."
    call kk_family_menu("S13", ["Ceritakan terus terang apa yang kausembunyikan.", "Tetap pada ceritamu semula.", "Bereskan barangmu dan pergi."])
    if _return == "A":
        shiori "Baik. Aku akan mengingat apa yang kaukatakan hari ini juga."
        nar "Kau memberikan penjelasan yang dapat diperiksa, bukan sekadar meminta dipercaya. Shiori tidak langsung tenang, tetapi ia mengajukan pertanyaan berikutnya alih-alih menutup map."
    elif _return == "B":
        nar "Kau bertahan pada cerita lama. Shiori menyebut satu perbedaan, menunggu, lalu berhenti ketika jelas kau memilih menambah penyangkalan daripada menanggapi."
        shiori "Aku sudah mendengar jawabanmu. Sekarang aku akan mencari yang tidak bergantung pada kesediaanmu mengatakan benar."
    else:
        nar "Kau membereskan barang dan pergi. Shiori tidak memaksamu tinggal, hanya meminta jangan menyebut kepergian itu bukti bahwa persoalannya memang tidak layak dibahas."
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
            nar "Kau menelepon Mio sendiri. Kau menceritakan apa yang sebenarnya kaukatakan tentang Shena, tanpa meminta Shiori menutupinya."
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
