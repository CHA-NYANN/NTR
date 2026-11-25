# Event netral tambahan: S10 (Kuroiwa menjemput Shiori) dan N20 (kembang api terakhir).
# Efek mengikuti Event_Shiori dan Event_Nagisa; angka adalah setelan prototipe.
# ┌─ PANDUAN CERITA · S10 · Hujan Deras: Kuroiwa Menjemput
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia dijemput.
# │ INTI    : A ikut / B tolak.
# │ AKHIRAN : Kuroiwa mencatat.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S10:
    call kk_scene_enter("shiori", "Klub Catur · Hujan deras")
    play sound "audio/sfx/rain.wav"
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Hujan deras bulan Juni turun seperti tirai kaca di depan serambi batu Klub Catur. Cahaya lampu teras dan sorot lampu depan mobil yang melintas di jalan utama memantul panjang di atas permukaan aspal yang basah dan gelap."
        else:
            nar "Langit musim hujan bulan Juni menggelap kelabu di atas serambi batu Klub Catur. Derasnya air yang jatuh dari tepi atap bergema menimpa paving halaman, menyebarkan hawa dingin yang langsung merembes melewati kemeja."
        nar "Kamu berdiri di tepi anak tangga serambi sambil menatap gerbang jalan raya dengan kening sedikit berkerut. Hari ini kamu lupa membawa payung lipat, dan di kepalamu baru saja terlintas rencana nekat menjadikan map plastik sketsa di dalam tasmu sebagai pelindung kepala untuk berlari menuju halte bus terdekat."
        nar "Tepat ketika kamu hendak mengangkat tas ke atas kepala, sebuah sedan hitam mengilap meluncur pelan memasuki halaman dan berhenti mulus di depan tangga. Pintunya terbuka dengan bunyi tenang, lalu Kuroiwa Genzo melangkah turun mengenakan jas hitam rapi dan sarung tangan putih sambil langsung membentangkan payung hitam berukuran besar."
        nar "Di sampingmu, Saionji Shiori merapikan pita ungu di kerah blazernya, rambut putih keperakan panjangnya yang ditata bervolume dengan hiasan mutiara tampak tetap rapi meski udara luar lembap. Sebelum melangkah ke bawah payung yang dipegang Kuroiwa, sorot mata Shiori yang tenang sempat melirik tas di tanganmu lalu berhenti."
        shiori "Amamiya-san. Jangan bilang kamu berniat memakai tas kanvas dan buku gambar itu buat payung menerobos hujan sederas ini."
        chiasa "Eh, ketahuan ya, Senpai? Habis halte bus di depan kan cuma lima menit kalau lari, kupikir paling cuma basah di bahu dikit hehehe..."
        shiori "Dengan hujan selebat ini, belum sampai tikungan pertama juga sepatumu sudah kebanjiran dan kertas gambarmu rusak semua."
        nar "Kuroiwa berdiri tegak beberapa langkah di depan anak tangga, payung hitamnya tetap stabil melindungi area pintu mobil sementara tatapannya yang tenang dan tajam sempat singgah sebentar pada dirimu."
        shiori "Ikut mobilku saja, Amamiya-san. Kursi belakang kebetulan kosong dan jalan kita searah."
        shiori "Kamu tidak perlu menganggapnya utang budi. Tapi kalau kamu memang lebih nyaman pulang sendiri, aku juga tidak akan memaksa."
        chiasa "{i}Caranya menawarkan tumpangan benar-benar nggak bikin terbebani... tapi jelas kalau aku naik mobil keluarga Saionji, Kuroiwa-san bakal langsung mencatat wajah dan alamat rumahku.{/i}"
        nar "Angin sore yang basah berembus pelan melewati pilar batu serambi dan membawa aroma tanah hujan dari taman halaman klub."
        nar "Kuroiwa tetap berdiri tanpa bergerak sedikit pun di samping pintu penumpang yang terbuka, menunjukkan disiplin seorang kepala pelayan keluarga besar."
        nar "Tawaran Shiori terdengar begitu tulus dan menghormati pilihanmu tanpa sedikit pun nada merendahkan."
        nar "Kamu memperhatikan pintu sedan hitam yang terbuka hangat itu sambil menimbang apakah kamu akan menerima tumpangannya atau menjaga jarak."
        nar "Shiori menunggumu dengan tenang di tepi serambi, sementara air hujan terus bergemuruh jatuh di ujung payung hitam yang dipegang Kuroiwa."
    else:
        if kk_slot >= 3:
            nar "Hujan deras bulan Juni turun rapat di depan serambi batu Klub Catur. Cahaya lampu teras dan sorot lampu depan mobil di jalan utama memantul panjang di atas permukaan aspal yang gelap dan basah."
        else:
            nar "Langit musim hujan bulan Juni menggelap kelabu di atas serambi batu Klub Catur. Gemuruh air hujan yang jatuh dari tepi atap bergema menimpa halaman batu, membawa embusan udara dingin yang langsung merembes melewati kemeja."
        nar "Kamu berdiri di tepi anak tangga serambi sambil menatap gerbang jalan raya dengan kening berkerut. Hari ini kamu tidak membawa payung, dan kamu baru saja menimbang-nimbang apakah tas kulitmu cukup lebar dijadikan pelindung kepala untuk berlari cepat ke jalan utama mencari taksi."
        nar "Tepat saat kamu mulai menarik kerah jaketmu ke atas, sebuah sedan hitam mengilap meluncur pelan memasuki halaman dan berhenti mulus di depan tangga. Pintu pengemudi terbuka dengan tenang, lalu Kuroiwa Genzo turun mengenakan jas hitam rapi dan sarung tangan putih sambil membentangkan payung hitam berukuran besar."
        nar "Di sebelahmu, Saionji Shiori merapikan pita ungu di kerah blazernya, rambut putih keperakan panjangnya yang ditata bervolume dengan hiasan mutiara tampak tetap rapi meski udara luar lembap. Sebelum melangkah turun ke bawah payung yang dipegang Kuroiwa, tatapan mata Shiori yang jernih sempat melirik tas di tanganmu lalu berhenti."
        shiori "Kisaragi-san. Jangan bilang kamu sedang menghitung peluang menyelamatkan jaketmu dengan lari menerobos hujan sederas ini."
        yutaka "Ketahuan, ya? Jalan raya di depan kan cuma tiga menit lari, kupikir paling basah dikit sebelum dapat taksi."
        shiori "Dengan curah hujan setebal ini, belum sampai gerbang depan pun sepatumu sudah penuh air dan catatan di tasmu basah semua."
        nar "Kuroiwa berdiri tegak beberapa langkah di bawah anak tangga, payung hitamnya tetap stabil melindungi pintu penumpang sementara tatapannya yang tenang dan tajam sempat singgah menilai sosokmu."
        shiori "Ikut mobilku saja sampai Distrik Elite, Kisaragi-san. Kursi belakang masih kosong dan rute kita searah."
        shiori "Ini bukan utang budi keluarga yang perlu kamu balas nanti. Tapi kalau kamu lebih suka pulang sendiri, aku juga tidak keberatan."
        yutaka "{i}Cara menawarkannya benar-benar bersih tanpa basa-basi politik keluarga... tapi jelas kalau aku naik sedan Saionji, Kuroiwa-san bakal langsung mencatat nama dan alamat apartemenku.{/i}"
        nar "Embusan angin musim hujan membawa tempias halus ke ujung anak tangga batu tempat kalian berdua berdiri berdampingan."
        nar "Di bawah payung hitam yang kokoh, Kuroiwa menunggu keputusan nona mudanya dengan postur tubuh yang tegak dan penuh kewaspadaan."
        nar "Kalimat Shiori yang lugas memberikan kebebasan penuh bagimu untuk menerima atau menolak tanpa harus memikirkan beban basa-basi."
        nar "Kamu menatap kabin belakang sedan yang tampak hangat itu sambil mempertimbangkan konsekuensi dari masuk ke dalam lingkaran pengawasan Kuroiwa."
        nar "Shiori menunggumu dengan tenang di tepi serambi, sementara air hujan terus bergemuruh jatuh di tepi payung hitam yang dipegang Kuroiwa."
    menu:
        "\"Kalau nggak merepotkan, boleh aku ikut menumpang pulang?\"":
            $ kk_record_choice("S10", "A")
            if kk_host == "chiasa":
                nar "Kamu menurunkan tas yang tadi hampir kamu angkat ke atas kepala, lalu tersenyum sopan mengangguk ke arah Shiori."
                chiasa "Kalau memang nggak merepotkan dan kebetulan searah, boleh aku ikut menumpang sampai dekat pertigaan rumahku, Saionji-senpai?"
                shiori "Tentu. Sebelum masuk, aku perlu menyampaikan satu hal supaya kamu tidak terkejut. Kuroiwa-san punya kebiasaan mencatat siapa saja yang ikut di mobil ini. Tidak apa-apa, memang aku sendiri yang memintanya mengantarmu."
                chiasa "Oh, aku paham kok, Senpai, memang sudah tugas beliau menjaga keamanan."
                nar "Kuroiwa melangkah maju setengah tapak agar payung besar itu menaungi kalian berdua sekaligus. Ia membungkuk singkat dengan sikap profesional yang dingin sekaligus sangat sopan."
                "Kuroiwa" "Selamat bertemu kembali, Amamiya-san. Silakan masuk lebih dulu agar tidak terkena tempias angin. Mohon arahkan alamat tujuan Anda setelah pintu tertutup."
                chiasa "Terima kasih banyak, Kuroiwa-san. Maaf jadi merepotkan di tengah hujan begini."
                "Kuroiwa" "Sama sekali tidak merepotkan. Saya hanya menjalankan arahan Ojou-sama."
                nar "Begitu kalian duduk di kursi belakang yang hangat dan pintu tertutup rapat meredam gemuruh hujan, kabin sedan terasa sangat sunyi dan nyaman. Kamu menyebutkan patokan jalan menuju daerah Rumah Amamiya, dan Kuroiwa mengangguk sekali di balik kemudi sebelum menjalankan mobil dengan sangat halus."
                shiori "Kuroiwa-san, tolong nyalakan penghangat sedikit saja, jaket Amamiya-san agak lembap terkena cipratan angin di serambi tadi."
                "Kuroiwa" "Baik, Ojou-sama."
                nar "Shiori menyandarkan punggungnya dengan rileks, menoleh ke arah jendela yang dialiri butiran hujan, lalu mulai membuka percakapan ringan yang jauh berbeda dari nada tegasnya di depan papan catur."
                shiori "Musim hujan bulan Juni selalu bikin halaman buku cepat bergelombang karena udara lembap. Tadi pagi saja satu bab novel yang kubaca harus kutindih buku kamus dulu supaya pinggirannya rata kembali."
                chiasa "Eh, Saionji-senpai lagi baca novel apa memangnya belakangan ini?"
                shiori "Novel ringan bertema strategi perang dan diplomasi kerajaan yang tempo hari sempat kusinggung di klub. Jilid terbarunya baru keluar bulan lalu, dan detail gambar baju zirahnya di sampul luar biasa rapi. Kalau tidak salah nama ilustratornya Shena."
                chiasa "{i}Gawat... jantungku hampir berhenti! Jangan sampai ekspresiku kelihatan aneh di kaca spion...{/i}"
                chiasa "Oh... aku pernah lihat bukunya di rak toko buku dekat stasiun! Kelihatannya seru ya alurnya."
                shiori "Iya, penulisnya jarang memakai kebetulan murah. Oh iya, dekat pertigaan menuju rumahmu ada toko kecil yang menjual dorayaki hangat, kan? Kuroiwa-san pernah membelikannya untukku sekali waktu pulang rapat."
                "Kuroiwa" "Kacang merahnya tidak terlalu manis, Amamiya-san. Cocok dimakan selagi hujan."
                chiasa "Haha, nanti kapan-kapan kucoba mampir beli deh kalau lewat sana."
                shiori "Jangan kaget kalau Kuroiwa-san tiba-tiba hafal jalan tikus di sekitar distrik ini. Beliau memang sudah bekerja bersama keluargaku sejak aku masih duduk di bangku sekolah dasar."
                "Kuroiwa" "Mengetahui rute tercepat dan memastikan keamanan teman Ojou-sama sudah menjadi bagian dari tanggung jawab saya."
                chiasa "Pantasan cara menyetirnya halus banget walaupun jalanannya lagi tergenang air hujan di mana-mana."
                shiori "Begitulah. Di dalam mobil ini aku jarang sekali bisa mengobrol soal novel atau makanan pinggir jalan, jadi perjalanan sore ini terasa cukup menyenangkan."
                nar "Ketika sedan hitam itu akhirnya melambat di dekat pertigaan menuju Rumah Amamiya, Kuroiwa segera turun lebih dulu untuk membukakan pintu dengan payungnya."
                nar "Shiori melambaikan tangan kecil dari balik kursi belakang sambil mengingatkanmu agar segera mengeringkan rambut setibanya di rumah."
                nar "Kamu membungkuk sopan mengucapkan terima kasih kepada Shiori dan Kuroiwa sebelum melangkah masuk ke jalan pemukiman yang sudah mulai reda hujannya."
                nar "Perjalanan singkat di dalam sedan keluarga Saionji itu memperlihatkan betapa nyamannya Shiori ketika berada di dekat seseorang yang tidak menuntut apa-apa darinya."
                nar "Pada saat yang sama, kamu sadar bahwa kepala pelayan setia keluarga Saionji kini telah mengenal wajah serta lingkungan tempat tinggalmu dengan sangat jelas."
                nar "Cahaya lampu jalan memantul di atas aspal basah sementara sedan hitam itu berputar halus kembali menuju jalan raya utama."
                nar "Kamu merapikan tas kanvas di bahumu dengan hati-hati agar buku sketsa di dalamnya tetap kering sampai tiba di pintu rumah."
                nar "Di sepanjang jalan yang basah, kamu melihat Shiori benar-benar menikmati percakapan biasa yang tidak memerlukan papan catur, panggung formal, ataupun agenda rumit. Sesekali kamu menangkap lirikan tenang Kuroiwa melalui spion tengah yang memperhatikan betapa rileksnya bahu nona mudanya saat mengobrol bersamamu, mencatat namamu dengan rapi dalam ingatannya."
            else:
                nar "Kamu melepaskan cengkeraman pada kerah jaketmu, lalu mengangguk tenang dengan senyum sopan ke arah Shiori."
                yutaka "Kalau memang nggak merepotkan dan kebetulan searah, boleh aku ikut menumpang sampai depan gerbang gedung apartemenku, Saionji-san?"
                shiori "Tentu. Sebelum masuk, aku perlu memberitahu satu hal supaya kamu tidak heran nanti. Kuroiwa-san selalu mencatat siapa saja yang ikut di dalam mobil ini. Tidak apa-apa, memang aku sendiri yang memintanya mengantarmu."
                yutaka "Paham kok, wajar banget buat standar keamanan keluarga Saionji."
                nar "Kuroiwa melangkah maju setengah tapak agar payung hitam besar itu menaungi kalian berdua sekaligus. Ia membungkuk singkat dengan sikap profesional yang dingin sekaligus sangat tertib."
                "Kuroiwa" "Selamat bertemu kembali, Kisaragi-san. Silakan masuk lebih dulu agar tidak terkena tempias angin. Mohon arahkan pintu masuk gedung apartemen Anda setelah pintu tertutup."
                yutaka "Terima kasih banyak, Kuroiwa-san. Maaf jadi ikut merepotkan di tengah hujan begini."
                "Kuroiwa" "Sama sekali tidak merepotkan. Saya hanya menjalankan arahan Ojou-sama."
                nar "Begitu kalian duduk di kursi belakang yang hangat dan pintu tertutup rapat meredam gemuruh hujan, kabin sedan terasa hening dan nyaman. Kamu menyebutkan arah blok apartemenmu, dan Kuroiwa mengangguk sekali di balik kemudi sebelum melajukan mobil dengan sangat halus."
                shiori "Kuroiwa-san, tolong naikkan suhu penghangat sedikit saja, bahu jaket Kisaragi-san agak lembap terkena angin di serambi tadi."
                "Kuroiwa" "Baik, Ojou-sama."
                nar "Shiori menyandarkan punggungnya dengan rileks, menoleh ke arah kaca jendela yang dialiri butiran air, lalu memulai percakapan biasa yang sama sekali terlepas dari urusan nama keluarga ataupun pertandingan catur."
                shiori "Musim hujan bulan Juni selalu membuat halaman buku catatan cepat bergelombang karena udara lembap. Tadi pagi saja buku referensi akhir permainan yang kubaca harus kutindih kamus tebal dulu supaya pinggirannya rata kembali."
                yutaka "Sama, buku di meja apartemenku juga sering melengkung tiap bulan Juni. Biasanya kamu suka baca buku strategi apa selain catatan catur, Saionji-san?"
                shiori "Belakangan aku sedang mengikuti satu seri novel ringan tentang strategi perang dan diplomasi kerajaan. Penulisnya rapi, jarang memakai kebetulan murah untuk menyelamatkan tokohnya. Oh iya, dekat bundaran sebelum jalan masuk apartemenmu ada kedai kecil yang menjual dorayaki hangat, kan? Kuroiwa-san pernah membelikannya sekali sepulang rapat."
                "Kuroiwa" "Isian kacang merahnya tidak terlalu manis, Kisaragi-san. Cukup pas menemani teh hangat selagi hujan."
                yutaka "Haha, padahal aku sering lewat situ tapi belum pernah mampir. Nanti kapan-kapan kucoba deh."
                shiori "Kuroiwa-san memang selalu hafal sudut-sudut jalan di Distrik Elite melebihi peta navigasi mana pun karena sudah mengawal keluargaku sejak aku kecil."
                "Kuroiwa" "Memastikan perjalanan Ojou-sama dan rekan beliau berlangsung aman adalah prioritas utama saya setiap hari."
                yutaka "Cara bawanya juga tenang banget biarpun hujan di jalan raya lagi deras-derasnya."
                shiori "Biasanya perjalanan pulangku hanya diisi laporan jadwal harian, jadi bisa mengobrol santai soal buku dan kedai kue seperti ini rasanya cukup menyegarkan."
                nar "Begitu sedan hitam tersebut berhenti tepat di bawah kanopi lobi gedung apartemenmu, Kuroiwa segera turun membukakan pintu penumpang dengan sopan."
                nar "Shiori mengangguk hangat dari dalam kabin belakang sambil berpesan agar kamu beristirahat dengan baik malam ini."
                nar "Kamu menyampaikan ucapan terima kasih kepada Shiori dan Kuroiwa sebelum melangkah masuk ke lobi marmer apartemenmu yang kering."
                nar "Keakraban yang mengalir alami di sepanjang perjalanan tadi membuktikan bahwa Shiori semakin mempercayai keberadaanmu di luar ruang klub."
                nar "Di sisi lain, kamu tahu bahwa setiap detail alamat serta sikapmu sore ini telah tersimpan rapi di dalam catatan kepala pengawal keluarga Saionji."
                nar "Lampu belakang sedan hitam itu tampak memantul di permukaan jalan Distrik Elite yang basah saat mobil tersebut kembali melaju tenang."
                nar "Kamu menekan tombol lift menuju lantai atas apartemenmu sambil mengingat betapa ringannya tawa Shiori di dalam kabin tadi."
                nar "Sepanjang jalan basah menuju Distrik Elite, kamu melihat Shiori sungguh-sungguh menikmati percakapan biasa yang tidak memerlukan panggung sosial, rencana rumit, ataupun perhitungan timbal balik. Sesekali kamu menangkap lirikan tenang Kuroiwa melalui kaca spion tengah yang memperhatikan betapa santainya bahu nona mudanya saat mengobrol bersamamu, mencatat namamu dengan cermat dalam ingatannya."
        "\"Terima kasih tawarannya, tapi aku pulang sendiri aja nggak apa-apa.\"":
            $ kk_record_choice("S10", "B")
            if kk_host == "chiasa":
                nar "Kamu menggeleng halus sambil tersenyum berterima kasih, merapatkan tas sketsamu ke dada di bawah atap serambi."
                chiasa "Terima kasih banyak tawarannya, Saionji-senpai, tapi aku pulang sendiri aja nggak apa-apa kok. Lagian rumahku agak masuk ke gang pemukiman, nanti malah bikin rute mobil Kuroiwa-san jadi mutar jauh di tengah macet hujan."
                nar "Shiori tidak terlihat tersinggung ataupun mendesakmu untuk berubah pikiran. Ia hanya mengangguk tenang menerima keputusanmu."
                shiori "Baik, aku mengerti. Hati-hati di jalan kalau begitu, Amamiya-san. Jangan nekat berlari dengan tas di atas kepala sampai pulang membawa demam."
                chiasa "Iya, Senpai, aku tunggu sepuluh menit di teras ini dulu sampai hujannya agak tipis, baru jalan ke halte bus."
                shiori "Kalau kamu berniat memesan taksi lewat aplikasi, kami bisa menunggu lima menit di pinggir halaman ini sampai mobilmu tiba supaya kamu tidak berdiri sendirian di serambi."
                "Kuroiwa" "Saya juga menyimpan payung lipat cadangan polos di bagasi bila Amamiya-san berkenan meminjamnya."
                chiasa "Wah, beneran nggak perlu repot-repot, Saionji-senpai, Kuroiwa-san! Sebentar lagi biasanya hujannya turun jadi gerimis kok, aku aman banget menunggu di sini."
                shiori "Kalau kamu sudah yakin, aku tidak akan memaksa. Sampai bertemu lagi di latihan klub berikutnya, Amamiya-san."
                nar "Shiori mengangguk sopan sekali, lalu melangkah masuk ke dalam mobil di bawah payung yang dipegang Kuroiwa. Kuroiwa membungkuk singkat ke arahmu sebelum menutup pintu dan masuk ke kursi pengemudi."
                nar "Sedan hitam itu bergerak meninggalkan halaman batu Klub Catur dengan laju yang tenang tanpa memercikkan genangan air ke arah serambi."
                nar "Tak lama berselang, curah hujan di luar mulai mereda menjadi rintik-rintik halus seperti yang kamu perkirakan tadi."
                nar "Sikap Shiori yang menghormati penolakanmu tanpa rasa tersinggung membuktikan bahwa ia benar-benar memandangmu sebagai teman yang setara."
                nar "Kamu merapikan letak tali tas kanvas di bahumu lalu menuruni anak tangga batu menuju halte bus dengan langkah yang ringan."
                nar "Di sepanjang trotoar menuju halte, udara sore pascahujan terasa segar dan bersih dari hiruk-pikuk kendaraan."
                nar "Dengan memilih pulang sendiri hari ini, kamu berhasil menjaga batas privasimu dari catatan pengawasan keluarga Saionji tanpa merusak hubungan baik dengan Shiori."
                nar "Bus kota yang menuju arah pemukimanmu tampak mendekat dari ujung jalan tepat ketika kamu tiba di bawah atap halte."
                nar "Ketika lampu merah belakang sedan itu perlahan menjauh menembus tirai hujan, kamu menyadari kelegaan kecil yang aneh. Kepedulian Shiori benar-benar berhenti tepat di garis batas yang kamu pilih, tanpa berubah menjadi desakan yang memaksa diterima demi menjaga harga dirinya."
            else:
                nar "Kamu menggeleng santai sambil tersenyum berterima kasih, merapatkan tas kulitmu di bawah naungan atap serambi."
                yutaka "Terima kasih banyak tawarannya, Saionji-san, tapi aku pulang sendiri aja nggak apa-apa. Jalur menuju apartemenku biasanya macet total tiap hujan deras begini, nanti malah bikin perjalanan pulangmu ikut tertahan."
                nar "Shiori sama sekali tidak tampak tersinggung ataupun memaksa. Ia hanya mengangguk tenang menerima batas pilihanmu."
                shiori "Baik, aku mengerti. Hati-hati di jalan kalau begitu, Kisaragi-san. Jangan benar-benar nekat berlari dengan tas di atas kepala sampai pulang membawa demam."
                yutaka "Tenang aja, aku tunggu sepuluh menit di serambi ini dulu sampai hujannya turun jadi gerimis, baru pesan taksi atau jalan ke jalan utama."
                shiori "Kalau kamu hendak memesan taksi sekarang, kami bisa menunggu lima menit di tepi halaman ini sampai mobilnya tiba supaya kamu tidak berdiri sendiri menunggu di luar."
                "Kuroiwa" "Saya juga membawa payung lipat cadangan polos di bagasi apabila Kisaragi-san berkenan meminjamnya."
                yutaka "Beneran nggak usah repot-repot, Saionji-san, Kuroiwa-san. Hujan bulan Juni biasanya cepat reda sebentar lagi, aku aman banget di sini."
                shiori "Kalau kamu sudah yakin, aku tidak akan memaksa. Sampai bertemu lagi di pertemuan klub berikutnya, Kisaragi-san."
                nar "Shiori mengangguk sopan sekali, lalu melangkah masuk ke dalam sedan di bawah payung besar yang dipegang Kuroiwa. Kuroiwa membungkuk singkat ke arahmu sebelum menutup pintu dan kembali ke kursi kemudi."
                nar "Mobil keluarga Saionji itu meluncur keluar melewati gerbang halaman dengan halus tanpa menyisakan kesan kaku di antara kalian."
                nar "Beberapa menit kemudian, deru hujan di atas atap serambi mulai menyusut menjadi gerimis tipis yang menyejukkan udara sore."
                nar "Cara Shiori menerima keputusanmu tanpa sedikit pun memaksakan kebaikannya membuat rasa hormat di antara kalian tetap terjaga dengan bersih."
                nar "Kamu mengeluarkan ponsel dari saku jaket untuk memesan taksi sambil menikmati udara sejuk di teras batu yang lengang."
                nar "Menolak tumpangan itu dengan sopan menghindarkanmu dari sorotan langsung Kuroiwa sekaligus membuktikan kepada Shiori bahwa kamu tidak mengejar fasilitas keluarganya."
                nar "Tak lama kemudian, sebuah taksi kosong berhenti di depan gerbang batu halaman klub sesuai titik jemput yang kamu pesan."
                nar "Kamu melangkah turun dari serambi dengan tenang untuk kembali ke apartemenmu di Distrik Elite."
                nar "Udara petang bulan Juni yang basah terasa segar saat kamu membuka pintu penumpang taksi tersebut."
                nar "Keputusan sederhana di teras klub catur tadi menjaga hubunganmu dengan Shiori tetap berada di atas pijakan yang bersih dan mandiri."
                nar "Saat sorot lampu merah belakang mobil itu perlahan menghilang di balik tirai hujan, kamu merasa lega melihat kepedulian Shiori berhenti tepat di tempat yang kamu pilih, tanpa berubah menjadi tuntutan agar diterima demi menjaga harga dirinya."
    return

# ┌─ PANDUAN CERITA · N20 · Kembang Api Terakhir
# │ LOKASI  : Hunian Biasa · Taman Lingkungan
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : ia menarik pemain pergi.
# │ INTI    : A ikut / B tolak / C ajak bicara.
# │ AKHIRAN : hub #10.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N20:
    call kk_scene_enter("nagisa", "Taman Lingkungan · Kembang api")
    nar "Nagisa menyentuh lenganmu ketika orang-orang mulai bergerak menuju tepi sungai. Ada jalan lebih sepi di dekat taman, cukup terang untuk dilewati tetapi jauh dari rombongan."
    nagisa "Ikut sebentar? Aku ingin melihat yang terakhir tanpa harus mendengar semua orang bicara. Kamu boleh bilang nggak. Aku sedang mencoba bertanya sebelum menarik."
    nar "Ia melepaskan lenganmu sesudah mengatakan itu. Kesungguhan gerakan kecil tersebut lebih jelas daripada kalimat yang masih terdengar ketus."
    call kk_family_menu("N20", ["Ikut dengannya menjauh dari keramaian.", "Tolak dan tetap di keramaian.", "Ajak ia bicara alih-alih pergi."])
    if _return == "A":
        play sound "audio/sfx/fireworks.wav"
        nar "Kau ikut. Kalian menemukan tempat di mana ledakan masih terdengar utuh dan orang lain tidak cukup dekat untuk mendengar setiap kata."
        nagisa "Terima kasih. Aku tahu harus belajar bisa sendiri. Tapi malam ini aku senang kamu mau."
        nar "Ia tidak langsung meminta janji tentang festival berikutnya. Untuk beberapa menit, kebersamaan boleh berhenti sebagai sesuatu yang sedang terjadi."
    elif _return == "B":
        nar "Kau memilih tetap di keramaian. Nagisa melihat jalan sepi itu, lalu orang-orang yang ada di dekatmu."
        nagisa "Baik. Aku juga mungkin tetap di sini. Bukan buat mengawasi. Aku cuma... belum ingin pergi sendirian."
        nar "Ia menjaga jarak, tetapi matanya beberapa kali kembali mencarimu. Penolakan yang kecil masih terasa besar di dalam ketakutan yang belum selesai."
    else:
        nar "Kau mengajaknya bicara di tempat kalian berdiri, menanyakan mengapa perlu membawa kalian menjauh. Nagisa hendak marah, lalu mengakui ia ingin merasa punya waktumu tanpa bersaing dengan wajah lain."
        nagisa "Aku tahu itu mulai terdengar seperti harus selalu dipilih. Aku nggak mau jadi orang yang cuma bisa tenang kalau yang lain hilang."
        play sound "audio/sfx/fireworks.wav"
        nar "Kembang api terakhir membuat kalian berhenti. Sesudahnya, pembicaraan yang belum selesai tetap boleh dilanjutkan."
    return

init 1 python:
    _hook("S10-A", lambda: (kk_adj("respek_shiori",3), kk_flag("kuroiwa_mencatat")))
    _hook("S10-B", lambda: kk_rel("shiori","trust",3))
    _hook("N20-A", lambda: (kk_rel("nagisa","intim",4), kk_adj("kelekatan_nagisa",5)))
    _hook("N20-B", lambda: kk_rel("nagisa","jeal",4))
    _hook("N20-C", lambda: kk_rel("nagisa","trust",4))
