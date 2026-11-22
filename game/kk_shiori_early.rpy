# Shiori awal (S03, S06, S08, S11, S12). Senyum yang tak terbaca; ia menilai diam-diam.
# Menyontek masuk daftar kebohongan (dibaca S13); menyebar rumor merusak reputasi.
# Efek mengikuti Event_Shiori dan Alur_Cabang/05; angka adalah setelan prototipe.
# ┌─ PANDUAN CERITA · S03 · Payung Hujan
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : dasar manga: ia dan Koita berbagi payung.
# │ INTI    : A intersep / B tawarkan payung kedua / C biarkan.
# │ AKHIRAN : menentukan ketertarikan Shiori pada Koita.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S03:
    call kk_scene_enter("shiori", "Klub Catur · Hujan")
    if kk_host == "chiasa":
        nar "Hujan deras menahan langkah beberapa mahasiswa di bawah kanopi pintu masuk gedung Klub Catur. Air mengalir kencang dari tepi atap, menciptakan tirai berkilau yang memisahkan teras batu dari jalan setapak menuju gerbang depan."
        nar "Di tengah teras itu, Saionji Shiori berdiri dengan postur tegak dan tenang. Rambut putih keperakannya yang ditata menyilang bervolume di atas dan jatuh bergelombang melewati bahu sama sekali tak tersentuh tempias hujan. Ia melirik layar ponselnya sekali lalu memasukkannya kembali ke tas kulitnya. Mobil jemputannya rupanya tertahan macet di jalan utama dan baru bisa menunggu di dekat gerbang depan."
        nar "Tepat saat kamu baru saja keluar dari lorong samping sambil menenteng payung lipatmu, Amamiya Koita muncul dari pintu utama. Ia sempat menengadah melihat derasnya air di teras, berhenti di samping Shiori, lalu membuka payung lipatnya dengan senyum hangat yang begitu otomatis."
        koita "Saionji-san? Kamu nggak bawa payung ya? Hujannya turun makin deras nih."
        shiori "Payungku tertinggal di mobil, Amamiya-san. Sopirku baru mengirim pesan kalau mobilnya tertahan di jalan utama dan menunggu di depan gerbang."
        koita "Wah, kalau menunggu di sini terus nanti malah tambah dingin. Pakai payungku saja bareng sampai gerbang depan, yuk. Kebetulan aku juga memang mau jalan ke arah depan."
        nar "Melihat adegan klise semacam itu berlangsung tepat di depan matamu membuatmu sempat terdiam di sisi kanopi. Shiori tidak langsung menolak ataupun tersipu. Ia menurunkan pandangannya ke payung lipat berukuran standar di tangan Koita, lalu melirik lebar bahu Koita sendiri sebelum menoleh dengan senyum sopan yang disisipi sindiran halus."
        shiori "Kamu sudah membayangkan adegan yang cukup manis, Amamiya-san. Tapi sepertinya kamu belum menghitung lebar payungnya. Kalau kita berjalan berdua di bawah itu, bukankah bahumu sendiri yang akan basah kuyup?"
        koita "Eh, haha, iya juga ya... tapi kalau cuma basah sedikit sih aku nggak masalah kok, jaketku cepat kering. Lagipula jaraknya ke gerbang depan nggak sampai lima menit jalan kaki. Yang penting Saionji-san nggak kehujanan."
        shiori "Menarik sekali caramu menimbang risiko yang seluruhnya kamu tanggung sendiri. Kamu selalu menawarkan bantuan secepat ini kepada siapa pun yang kehujanan?"
        koita "Yah, kalau kebetulan lihat orang kesulitan di depan mata, masa cuma kulewati begitu saja..."
        nar "Shiori tersenyum ringan, sebuah senyum tipis yang nyaris mustahil ditebak apakah sedang geli, menilai, atau sekadar sopan. Ia menerima kebaikan kecil itu dengan anggun tanpa terburu-buru memberinya label ketertarikan apa pun."
        nar "Tepat sebelum mereka sempat melangkah turun dari anak tangga teras, mata ungu ametis Shiori bergeser menangkap sosokmu yang berdiri beberapa langkah di sisi kanopi sambil menggenggam payung lipatmu sendiri."
        nar "Alis peraknya terangkat tipis. Tatapannya tenang, memberi ruang sekaligus menguji, seolah di atas papan permainan hari ini ia sengaja menunggu apakah kamu berniat melangkah maju dan ikut menentukan siapa yang berjalan dengan siapa di bawah hujan."
    else:
        nar "Hujan deras memaksa beberapa mahasiswa tertahan di bawah kanopi batu di depan gedung Klub Catur. Air tumpah deras dari tepi atap, membentuk tirai putih yang memisahkan teras dari jalan setapak menuju gerbang depan."
        nar "Di tengah teras itu, Saionji Shiori berdiri dengan postur tegak dan tenang. Rambut putih keperakannya yang ditata menyilang bervolume di atas dan jatuh bergelombang melewati bahu sama sekali tak tersentuh tempias hujan. Ia memeriksa layar ponselnya sekali lalu memasukkannya kembali ke tas kulitnya. Mobil jemputannya rupanya tertahan macet di jalan utama dan baru bisa menunggu di dekat gerbang depan."
        nar "Baru saja kamu melangkah keluar dari lorong samping sambil menenteng payung panjangmu yang masih tertutup, Koita muncul dari pintu utama di dekat Shiori. Ia menengadah sekilas melihat derasnya hujan, lalu tanpa ragu langsung membuka payung lipatnya dengan senyum ramah yang sudah seperti refleks otomatis setiap kali melihat orang kesulitan."
        koita "Saionji-san? Nggak bawa payung ya? Hujannya makin deras nih."
        shiori "Payungku tertinggal di dalam mobil, Amamiya-san. Sopirku baru mengabari kalau mobilnya tertahan di jalan utama dan menunggu di dekat gerbang."
        koita "Kalau nunggu di sini terus nanti keburu dingin, lho. Pakai payungku saja bareng sampai gerbang depan, yuk. Aku juga memang searah ke depan kok."
        nar "Kamu berhenti di sisi pilar kanopi, menyaksikan adegan klise yang nyaris seperti halaman manga itu berlangsung tepat di depan mata. Shiori tidak langsung mengangguk ataupun tersipu. Ia menurunkan tatapannya ke payung lipat berukuran standar di tangan Koita, lalu melirik lebar bahu Koita sendiri sebelum menoleh dengan senyum sopan yang disisipi sindiran halus."
        shiori "Kamu sudah membayangkan adegan yang cukup manis, Amamiya-san. Tapi sepertinya kamu belum menghitung lebar payungnya. Kalau kita berjalan berdua di bawah itu, bukankah bahumu sendiri yang akan basah kuyup?"
        koita "Eh, haha, iya juga sih... tapi kalau cuma basah sedikit aku nggak masalah kok, jaketku cepat kering. Jarak ke gerbang depan juga nggak jauh. Yang penting Saionji-san nggak kehujanan."
        shiori "Menarik sekali caramu menimbang kerugian kecil yang seluruhnya kamu tanggung sendiri. Kamu selalu menawarkan bantuan secepat ini kepada siapa pun?"
        koita "Yah, kalau kebetulan lihat orang ketahan hujan di depan mata, masa kutinggal begitu saja..."
        nar "Shiori tersenyum ringan, senyum tipis yang nyaris mustahil ditebak apakah sedang geli, menilai, atau sekadar sopan. Ia menerima kebaikan kecil itu dengan anggun tanpa terburu-buru memberinya label ketertarikan apa pun."
        nar "Tepat sebelum mereka sempat melangkah turun dari anak tangga teras, mata ungu ametisnya bergeser menangkap sosokmu yang berdiri beberapa langkah di sisi kanopi sambil menggenggam payung panjangmu."
        nar "Alis peraknya terangkat tipis. Tatapannya tenang dan tajam, jelas memberi ruang sekaligus menguji, seolah di atas papan permainan hari ini ia sengaja menunggu apakah sahabat Amamiya-san sendiri berniat melangkah masuk dan ikut menentukan siapa yang berjalan dengan siapa di bawah hujan."
    call kk_family_menu("S03", ["\"Tunggu, biar aku aja yang antar kamu ke gerbang.\"", "\"Pakai payung satu lagi ini aja biar nggak sempit-sempitan.\"", "Biarkan saja mereka berangkat berdua."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu tidak membiarkan momen itu lewat begitu saja. Kamu langsung melangkah maju mendekati tepi kanopi dan membuka payungmu sendiri dengan bunyi klik yang tegas, memotong jarak di antara Koita dan Shiori sebelum mereka sempat turun ke jalan setapak."
            chiasa "Kalau payung Ko-nii terlalu sempit buat berdua, biar aku saja yang antar Saionji-senpai ke gerbang depan. Bahu kita sama-sama kecil, jadi lebih muat dan tidak ada yang harus basah."
            koita "Lho, Chi-chan? Tumben lewat gedung sini. Eh, nggak apa-apa kalau kamu yang antar? Tadi aku sudah keburu menawarkan..."
            chiasa "Nggak apa-apa, Ko-nii, aku juga memang mau keluar lewat gerbang depan kok."
            nar "Shiori sama sekali tidak langsung mengiyakan tawaranmu. Ia justru memandangmu dari ujung mata dengan senyum tipis yang penuh minat, seolah baru saja melihat seseorang menggerakkan bidak mendahului gilirannya."
            shiori "Oh? Kamu cepat sekali menengahi, Amamiya-san. Menarik sekali."
            nar "Ia melangkah setengah langkah mendekat ke arahmu, tetapi tetap berhenti tepat di batas kering kanopi. Sebelum masuk ke bawah payungmu, ia melontarkan satu pertanyaan sederhana dengan tatapan lurus yang sulit dihindari."
            shiori "Boleh aku tahu mengapa kamu menawarkan diri secepat itu? Apakah kamu memang searah denganku ke gerbang depan, atau ada alasan lain kamu tidak ingin kakakmu berjalan di bawah hujan bersamaku?"
            nar "Nada suaranya tetap lembut dan sopan, tetapi pertanyaannya setajam ujung bidak yang langsung mengincar celah pertahananmu. Di depan tatapan seperti itu, campur tanganmu harus segera mencari alasan yang terdengar masuk akal untuk diucapkan terang-terangan."
            chiasa "Aku memang mau ke arah gerbang depan, Saionji-senpai. Lagipula kalau Ko-nii kehujanan sampai masuk angin gara-gara memaksakan satu payung kecil, nanti di rumah aku juga yang repot mengurusnya."
            koita "Hei, aku nggak segampang itu masuk angin tahu, Chi-chan! Cuma jalan tiga menit doang!"
            chiasa "Bulan lalu waktu kehujanan sepuluh menit pulang kuliah, siapa yang paginya bersin-bersin minta dibikinkan bubur?"
            koita "Aduh... itu kan gara-gara malamnya lupa nutup jendela kamar..."
            nar "Shiori menatap kalian berdua selama dua detik penuh, menimbang kejujuran di balik kalimat itu, lalu sudut bibirnya melengkung sedikit lebih jelas."
            shiori "Alasan yang sangat praktis dan cukup jujur. Baiklah, kalau begitu aku terima tawaranmu, Amamiya-san. Terima kasih atas niat baiknya juga, Amamiya-san."
            nar "Ia melangkah masuk ke bawah payungmu dengan anggun, menjaga jarak yang rapi untuk berbagi ruang teduh. Di belakang kalian, Koita hanya bisa berdiri di tepi kanopi sambil menggaruk tengkuknya dengan wajah bingung melihat rencana sederhananya mendadak diambil alih."
            koita "Eh... hati-hati jalannya ya, Chi-chan! Aku nyusul di belakang kalau hujannya agak kecil!"
            nar "Kalian menuruni anak tangga batu dan berjalan berdampingan menyusuri jalan setapak di bawah derai hujan yang memukul kain payung. Semakin jauh dari gedung, suara rintik hujan terdengar kian rapat, menyisakan ruang obrolan kecil di bawah kanopi payung kalian."
            shiori "Benar juga katamu, bahu kita sama-sama kecil jadi tidak ada yang kehujanan. Tapi kalau boleh jujur, Amamiya-san, ekspresi terkejut kakakmu di teras tadi lumayan menghibur."
            chiasa "Ko-nii memang sering terlalu cepat menawarkan bantuan sebelum berpikir panjang, Senpai. Kadang dia lupa mengukur kemampuannya sendiri."
            shiori "Dan kamu cukup cepat memotong jalurnya sebelum ia sempat melangkah turun dari tangga. Aku mulai paham kenapa suasana di sekitar kakakmu tidak pernah benar-benar membosankan."
            chiasa "Hati-hati depan situ ada genangan agak lebar, Senpai, geser sedikit ke kiri."
            shiori "Terima kasih. Nah, mobilku sudah terlihat di balik gerbang."
            nar "Di dekat gerbang depan tempat sebuah sedan hitam menyalakan lampu hazard, sopir berjas gelap segera turun membukakan pintu belakang. Shiori melangkah naik lalu menoleh sekali lagi dengan membungkuk kecil."
            shiori "Terima kasih sudah mengantar sampai sini, Amamiya-san. Sampai bertemu di kampus besok."
            nar "Pintu sedan menutup pelan, meninggalkanmu berdiri di bawah payung sambil menyadari senyum tipis Shiori tadi jelas mencatat langkah beranimu hari ini."
        else:
            nar "Kamu tidak membiarkan momen itu lewat begitu saja. Kamu langsung melangkah maju mendekati tepi anak tangga dan menekan tombol payung panjangmu hingga terbuka lebar dengan bunyi klik yang mantap, memotong jarak di antara Koita dan Shiori sebelum mereka sempat turun ke jalan setapak."
            yutaka "Payung lipatmu terlalu sempit buat berdua, Koita, bahu kirimu pasti basah semua sebelum setengah jalan. Biar aku saja yang antar Saionji-san ke gerbang depan, payungku jauh lebih lebar."
            koita "Lho, Yutaka? Tumben lewat gedung sini. Eh, nggak apa-apa kalau kamu yang antar? Tadi aku sudah keburu nawarin..."
            yutaka "Nggak apa-apa, aku juga memang mau ke arah jalan depan kok."
            nar "Shiori sama sekali tidak langsung menerima ataupun menolak. Ia memandangmu dari sudut matanya dengan senyum tipis yang penuh rasa ingin tahu, seolah baru saja melihat pemain lain mendadak ikut duduk di depan papan caturnya."
            shiori "Oh? Kamu cepat sekali menengahi, Kisaragi-san. Menarik sekali."
            nar "Ia melangkah setengah langkah ke arahmu, tetapi tetap berhenti tepat di batas kering kanopi. Sebelum melangkah masuk ke bawah payungmu, ia menatap matamu lurus-lurus dengan satu pertanyaan sederhana yang sulit dielakkan."
            shiori "Boleh aku tahu mengapa kamu menawarkan diri secepat itu? Apakah kamu memang searah denganku ke gerbang depan, atau ada alasan khusus kamu tidak ingin temanmu berjalan berdua denganku?"
            nar "Nada suaranya tetap ringan dan sopan, sementara pertanyaannya setajam langkah pembuka yang langsung menguji niatmu. Di depan tatapan seterang itu, campur tanganmu harus segera menemukan alasan yang terdengar masuk akal untuk diucapkan terang-terangan."
            yutaka "Aku memang searah ke gerbang depan, Saionji-san. Lagipula aku kenal Koita dari kecil. Kalau dia nekat kehujanan begini, besok pasti demam dan ujung-ujungnya aku juga yang kena repot mengantar catatan kuliahnya."
            koita "Hei, aku nggak selemah itu tahu, Yutaka! Cuma jalan tiga menit sampai gerbang!"
            yutaka "Bulan lalu waktu kena hujan sebentar pulang latihan, siapa yang kirim pesan tengah malam minta dibelikan obat flu?"
            koita "Aduh... itu kan kebetulan lagi kurang tidur saja..."
            nar "Shiori menimbang jawabanmu selama dua detik penuh dengan senyum yang tetap tak terbaca, lalu sudut bibirnya melengkung sedikit lebih jelas."
            shiori "Alasan yang cukup masuk akal, dan payungmu memang lebih luas. Baiklah, kalau begitu aku terima tawaranmu, Kisaragi-san. Terima kasih juga atas niat baiknya, Amamiya-san."
            nar "Ia melangkah masuk ke bawah payungmu dengan anggun, menjaga jarak yang rapi untuk berbagi ruang teduh. Di belakang kalian, Koita hanya bisa berdiri di tepi kanopi sambil menggaruk tengkuknya dengan wajah bingung melihat rencananya baru saja disela sahabatnya sendiri."
            koita "Eh... hati-hati jalannya ya! Aku tunggu hujan agak reda dikit baru nyusul!"
            nar "Kalian berjalan berdampingan menyusuri jalan setapak yang basah di bawah bunyi hujan yang menghantam kain payung panjangmu. Begitu menjauh dari teras gedung, Shiori melirik sekilas ke arahmu."
            shiori "Payungmu memang jauh lebih lega. Dan jujur saja, Kisaragi-san, ekspresi terkejut Amamiya-san di bawah kanopi tadi cukup menarik untuk dilihat."
            yutaka "Dia memang sering bertindak dulu baru mikir belakangnya. Sudah kebiasaan dari dulu."
            shiori "Sementara kamu jauh lebih cepat memotong langkahnya sebelum ia sempat berjalan jauh. Sepertinya kamu memang selalu mengamati sekitarmu lebih dekat daripada yang terlihat."
            yutaka "Hati-hati depan situ pavingnya agak miring dan tergenang, geser ke kanan dikit."
            shiori "Terima kasih. Mobilku sudah menunggu tepat di balik gerbang."
            nar "Di depan gerbang tempat sebuah sedan hitam berhenti menyalakan lampu hazard, sopir berjas gelap segera turun membukakan pintu. Shiori membungkuk anggun sebelum melangkah masuk."
            shiori "Terima kasih sudah mengantar, Kisaragi-san. Sampai bertemu di kampus."
            nar "Pintu mobil menutup rapi, meninggalkanmu berdiri di tepi gerbang sambil menyadari senyum tipis Shiori tadi jelas belum selesai menilai niatmu."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Alih-alih memaksa masuk di antara mereka secara terang-terangan, kamu melangkah maju dengan tenang dan menyodorkan payung lipatmu yang masih tergulung rapi langsung ke arah Shiori."
            chiasa "Saionji-senpai, pakai payungku saja supaya tidak usah berdesakan di bawah satu payung."
            koita "Eh, Chi-chan? Tumben lewat sini. Tunggu, kalau payungmu dipinjamkan, nanti kamu sendiri pulang pakai apa?"
            chiasa "Payungmu kan masih ada, Ko-nii. Aku bisa pulang bareng kamu sampai depan atau menunggu sebentar sampai hujannya agak reda. Kalau Saionji-senpai pegang payung sendiri, tidak ada satu pun yang bahunya basah."
            nar "Shiori menatap payung di tanganmu, lalu menatap wajahmu sejenak. Senyum tipis di bibirnya tampak benar-benar menghargai langkah yang bersih, efisien, dan tidak berlebihan itu."
            shiori "Sopan sekali, Amamiya-san. Aku mencatat itu, terima kasih banyak. Besok pasti kukembalikan dalam keadaan bersih dan kering."
            chiasa "Tidak usah buru-buru kok, Senpai, di rumah masih ada payung cadangan."
            nar "Ia menerima payung lipatmu dengan kedua tangan secara anggun, membukanya dengan satu gerakan halus, lalu menoleh ringan ke arah Koita dengan sorot mata yang tenang."
            shiori "Dengan begini, tidak ada yang harus kehujanan demi kesopanan. Nah, Amamiya-san, kalau kamu masih ingin berjalan ke arah gerbang depan, aku tidak keberatan. Sekarang itu sepenuhnya keputusanmu sendiri tanpa alasan berbagi payung."
            koita "Ah... iya, tentu! Aku juga memang searah ke depan kok. Eh, tapi Chi-chan ikut sekalian saja ya, payungku cukup buat kita berdua jalan pelan-pelan!"
            chiasa "Iya, ayo sekalian jalan ke gerbang, Ko-nii. Tapi pegang payungnya di tengah ya, jangan miring sebelah lagi."
            koita "Haha, siap! Aku nggak miring-miring kok kalau sama adik sendiri."
            shiori "Kalau begitu mari, sepertinya jalan setapak sebelah kanan lebih sedikit genangannya."
            nar "Kalian bertiga melangkah turun ke jalan setapak yang basah. Shiori berjalan tenang setengah langkah di depan di bawah payung lipatmu, sementara kamu dan Koita menyusul tepat di belakangnya."
            shiori "Ngomong-ngomong, payungmu ringan sekali, Amamiya-san. Gagangnya juga nyaman dipegang."
            chiasa "Aku memang pilih yang ringan supaya nggak berat di tas waktu bawa buku sketsa, Senpai."
            koita "Eh, itu sedan hitam di depan gerbang mobil jemputanmu, Saionji-san? Kelihatannya sudah dari tadi menyalakan lampu."
            shiori "Iya, itu mobilku. Terima kasih banyak untuk payungnya, Amamiya-san, dan terima kasih sudah berjalan bersama sampai depan."
            nar "Dengan hilangnya alasan berbagi satu payung, suasana yang tadinya nyaris terasa seperti adegan romantis mendadak kembali menjadi perjalanan biasa bertiga menuju gerbang depan, terpisah di bawah payung masing-masing tanpa jarak terlalu dekat yang bisa dipaksakan oleh hujan."
        else:
            nar "Alih-alih menyela secara terang-terangan, kamu melangkah maju dengan santai lalu menyodorkan payung panjangmu yang masih tergulung rapi langsung ke hadapan Shiori."
            yutaka "Pakai punyaku saja, Saionji-san, biar nggak perlu berdesakan di bawah satu payung kecil."
            koita "Eh, Yutaka? Tumben lewat sini. Terus kamu sendiri pulang pakai apa kalau payungmu dipinjamkan?"
            yutaka "Aku bisa nebeng payungmu sebentar sampai gerbang atau tunggu di sini sampai hujannya agak reda. Yang penting nggak ada satu pun yang bahunya basah cuma gara-gara payung kekecilan."
            nar "Shiori menatap gagang payung di tanganmu lalu melirik wajahmu sejenak. Senyum tipis di bibirnya tampak benar-benar menghargai langkah yang bersih, praktis, dan tidak memaksa itu."
            shiori "Sopan sekali, Kisaragi-san. Aku mencatat itu, terima kasih banyak. Besok pasti kukembalikan dalam keadaan bersih dan kering."
            yutaka "Santai saja, di apartemen masih ada payung lipat."
            nar "Ia menerima payung itu dengan kedua tangan secara anggun, membukanya dengan satu gerakan halus, lalu menoleh ringan ke arah Koita dengan sorot mata yang tenang."
            shiori "Nah, dengan begini tidak ada satu pun yang harus kehujanan demi kesopanan. Amamiya-san, kalau kamu masih ingin berjalan ke arah gerbang depan, aku tidak keberatan. Sekarang itu sepenuhnya keputusanmu sendiri tanpa alasan payung lagi."
            koita "Ah... iya! Aku memang searah ke depan kok. Ayo sekalian jalan bareng saja, Yutaka!"
            yutaka "Oke, tapi jangan miringkan payungmu terlalu ke kanan lagi, nanti malah bahuku yang basah."
            koita "Ya nggak mungkin lah aku biarin kamu basah, haha!"
            shiori "Hehe, kalau begitu mari, jalur sebelah kanan sepertinya lebih sedikit genangan."
            nar "Kalian bertiga melangkah turun menyusuri jalan setapak yang basah. Shiori berjalan anggun di bawah payung panjangmu, sementara kamu dan Koita berjalan bersebelahan di belakangnya sambil sesekali menghindari cipratan air."
            shiori "Payungmu lebar sekali, Kisaragi-san. Pilihan yang praktis untuk cuaca bulan Juni."
            yutaka "Biar tas sama sepatu nggak gampang kena tempias kalau anginnya miring."
            koita "Nah, itu mobil jemputanmu di depan gerbang kan, Saionji-san?"
            shiori "Betul. Terima kasih untuk payungnya, Kisaragi-san, dan terima kasih sudah menemani jalan sampai gerbang."
            nar "Dengan hilangnya alasan berbagi satu payung, momen yang tadi hampir berbelok ke arah romantis langsung kembali menjadi perjalanan pulang biasa bertiga, terpisah di bawah payung masing-masing tanpa jarak terlalu dekat yang dipaksakan oleh hujan."
    else:
        if kk_host == "chiasa":
            nar "Kamu memilih tetap berdiri diam di sisi kanopi tanpa ikut campur, membiarkan mereka berdua menyelesaikan percakapan mereka sendiri sambil menggenggam gagang payungmu yang masih tertutup."
            nar "Koita menanggapi sindiran Shiori dengan tawa kecil yang sedikit malu, lalu melangkah turun lebih dulu ke batas hujan sambil sengaja memiringkan gagang payungnya cukup jauh ke sisi kanan untuk melindungi bahu Shiori."
            koita "Ayo, Saionji-san, sebelah sini lebih lebar ruangnya. Jalannya agak pelan saja biar sepatumu nggak kena cipratan genangan."
            shiori "Kamu benar-benar memiringkannya sejauh itu, ya... lihat, bahu kirimu sudah mulai basah padahal kita baru melangkah tiga langkah."
            koita "Nggak apa-apa, cuma sampai gerbang depan kok. Jaketku juga cepat kering nanti begitu sampai rumah."
            shiori "Hujan sederas ini jarang sekali mau menunggu jaketmu kering, Amamiya-san. Kamu yakin tidak mau membetulkan pegangannya sedikit ke tengah?"
            koita "Kalau cuma kena hujan sedikit sih bukan kerugian besar, Saionji-san. Hati-hati, batu depan situ agak licin."
            shiori "Begitu. Kamu memang tipe orang yang tidak terlalu memikirkan kerugian kecil untuk diri sendiri, ya, Amamiya-san."
            koita "Haha, kalau dibilang begitu aku malah jadi malu. Tapi serius, bagian kanan sana banyak genangan, lebih aman agak ke dalam sini."
            shiori "Terima kasih sudah mengingatkan."
            nar "Dari bawah kanopi, kamu menyaksikan punggung mereka perlahan menjauh menyusuri jalan setapak yang basah. Suara tawa kikuk Koita dan jawaban tenang Shiori lama-lama tenggelam oleh derai hujan."
            nar "Sebelum mereka berbelok di dekat lampu gerbang depan, kamu sempat menangkap bagaimana Shiori melirik bahu jaket Koita yang mulai gelap tersiram air hujan, lalu melirik lagi ke arah payung yang masih miring ke sisinya."
            nar "Ia jelas menyadari perhatian yang sungguh-sungguh dilakukan di balik gerakan kecil itu, meski dari langkahnya yang tetap teratur dan bahunya yang tak sedikit pun mendekat lebih jauh dari yang diperlukan, ia belum memberinya arti lebih daripada kebaikan seorang kenalan."
            nar "Baru setelah lampu belakang sedan hitam di depan gerbang perlahan menjauh di balik tirai air, kamu menekan tombol payung lipatmu dan mulai melangkah turun sendiri ke jalan setapak."
        else:
            nar "Kamu memilih tetap bersandar tenang di dekat pilar kanopi sambil menyelipkan satu tangan ke saku celana, membiarkan mereka berdua menyelesaikan percakapan mereka sendiri tanpa ikut campur."
            nar "Koita menanggapi sindiran Shiori dengan tawa kecil yang sedikit kikuk, lalu melangkah turun lebih dulu ke batas hujan sambil memiringkan payungnya cukup jauh ke sisi kanan untuk melindungi bahu Shiori."
            koita "Ayo, Saionji-san, lewat sisi sini saja biar sepatumu nggak kena genangan."
            shiori "Kamu benar-benar memiringkannya sejauh itu, ya... bahu kirimu sudah mulai basah padahal kita baru melangkah tiga langkah."
            koita "Nggak apa-apa, cuma sampai gerbang depan kok. Jaketku juga cepat kering nanti begitu sampai rumah."
            shiori "Hujan sederas ini jarang mau menunggu jaketmu kering, Amamiya-san. Kamu yakin tidak mau sedikit menggeser gagangnya ke tengah?"
            koita "Kalau cuma kena hujan sedikit sih bukan kerugian besar, Saionji-san. Hati-hati, batu depan situ agak licin."
            shiori "Begitu. Kamu memang tidak terlalu menghitung kerugian kecil untuk diri sendiri, ya, Amamiya-san."
            koita "Haha, nggak sampai segitunya kok. Tapi serius, pinggir kanan sana ada kubangan, agak ke sini sedikit saja."
            shiori "Baik, terima kasih sudah mengingatkan."
            nar "Dari bawah kanopi, kamu memperhatikan punggung mereka perlahan menjauh di tengah tirai hujan. Suara canggung Koita dan balasan tenang Shiori perlahan hilang di balik gemuruh air yang jatuh dari atap."
            nar "Sebelum sosok mereka mencapai lampu gerbang depan, kamu sempat menangkap bagaimana Shiori melirik bahu jaket Koita yang mulai gelap tersiram air, lalu memandang lagi ke arah payung yang tetap miring melindunginya."
            nar "Ia jelas menyadari perhatian tulus yang sungguh-sungguh dilakukan di balik gerakan kecil itu, meski dari langkahnya yang tetap teratur dan jarak bahunya yang terjaga, ia belum memberinya arti lebih jauh daripada kebaikan seorang kenalan."
            nar "Baru setelah sedan hitam di depan gerbang mulai bergerak menjauh menembus hujan, kamu mendorong tombol payung panjangmu hingga terbuka lebar dan melangkah turun sendiri ke jalan setapak."
    return

# ┌─ PANDUAN CERITA · S06 · Turnamen Klub Catur
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia berpartisipasi.
# │ INTI    : A hadir / B ikut / C absen.
# │ AKHIRAN : Trust.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S06:
    call kk_scene_enter("shiori", "Klub Catur · Turnamen")
    if kk_host == "chiasa":
        nar "Ruang utama Klub Catur Distrik Elite hari itu dipenuhi tiga baris meja kayu panjang yang sudah dipasangi papan catur turnamen beserta jam digital di sisi kanan masing-masing. Udara di dalam ruangan terasa hening dan padat, hanya diselingi bunyi ketukan tombol jam, gesekan kain lengan kemeja, serta langkah kaki wasit klub yang berjalan pelan memeriksa papan."
        nar "Di depan papan pengumuman kayu dekat pintu masuk, Saionji Shiori berdiri memperhatikan bagan babak penyisihan yang baru ditempel panitia. Di antara para peserta yang sebagian besar tampak tegang menghafal pembukaan dari buku catatan kecil, Shiori berdiri tenang dengan kedua tangan terlipat ringan."
        nar "Di ruangan turnamen ini, marga Saionji tidak bisa membatalkan satu pun langkah keliru di atas enam puluh empat petak papan, dan dari cara matanya mempelajari daftar lawan, situasi yang murni bergantung pada kemampuan sendiri itu justru merupakan hal yang paling ia sukai."
        nar "Menyadari langkahmu berhenti di ambang pintu ruang turnamen, Shiori menoleh dan menunjuk kursi kayu kosong di samping meja panitia pendaftaran."
        if kk_slot == 0:
            shiori "Selamat pagi, Amamiya-san. Aku tidak menyangka kamu mampir ke gedung klub saat hari turnamen terbuka begini."
        elif kk_slot == 1:
            shiori "Selamat siang, Amamiya-san. Aku tidak menyangka kamu mampir ke gedung klub saat hari turnamen terbuka begini."
        elif kk_slot == 2:
            shiori "Selamat sore, Amamiya-san. Aku tidak menyangka kamu mampir ke gedung klub saat hari turnamen terbuka begini."
        else:
            shiori "Selamat malam, Amamiya-san. Aku tidak menyangka kamu mampir ke gedung klub saat babak turnamen terbuka begini."
        chiasa "Suasananya serius banget ya, Saionji-senpai. Aku sampai ragu mau masuk tadi takut suara sepatuku berisik."
        shiori "Saat jam pertandingan belum ditekan, kamu masih boleh bicara biasa kok. Sebentar lagi babak penyisihan dibuka, dan lawan pertamaku dari klub teknik sedang mengambil kartu meja di sebelah."
        chiasa "Senpai kelihatan tenang sekali, padahal peserta lain di pojok sana masih sibuk bolak-balik buku pembukaan."
        shiori "Menghafal lima menit sebelum jam ditekan jarang membantu kalau lawan keluar dari jalur buku. Jadi, apa yang membawamu ke sini hari ini? Mau duduk menonton, ikut menulis nama di bagan peserta, atau hanya kebetulan lewat? Ketiganya boleh, aku hanya ingin tahu lebih dulu sebelum terlanjur senang mengira kamu datang khusus untuk melihatku bertanding."
    else:
        nar "Ruang utama Klub Catur Distrik Elite hari itu dipenuhi tiga deret meja kayu panjang lengkap dengan papan turnamen dan jam catur digital. Keheningan ruangan terasa padat oleh konsentrasi para peserta, hanya diselingi bunyi klik tombol jam dan langkah pelan panitia yang mencatat hasil babak awal."
        nar "Di depan papan bagan pertandingan dekat meja panitia, Saionji Shiori berdiri memeriksa urutan lawannya dengan postur santai dan fokus. Di ruangan ini, nama besar Saionji Holdings sama sekali tidak berlaku untuk menyelamatkan bidak yang salah langkah, dan sorot mata ungunya tampak sangat menikmati aturan yang adil tersebut."
        nar "Begitu menangkap kehadiranmu di dekat pintu masuk, Shiori menoleh dan memberi isyarat halus ke arah kursi kosong di samping meja pendaftaran."
        if kk_slot == 0:
            shiori "Selamat pagi, Kisaragi-san. Tumben sekali kamu naik sampai ke ruang turnamen klub."
        elif kk_slot == 1:
            shiori "Selamat siang, Kisaragi-san. Tumben sekali kamu naik sampai ke ruang turnamen klub."
        elif kk_slot == 2:
            shiori "Selamat sore, Kisaragi-san. Tumben sekali kamu naik sampai ke ruang turnamen klub."
        else:
            shiori "Selamat malam, Kisaragi-san. Tumben sekali kamu naik sampai ke ruang turnamen klub."
        yutaka "Hening banget ruangannya, Saionji-san. Semua orang mukanya kayak lagi nunggu pengumuman sidang."
        shiori "Turnamen terbuka bulanan memang selalu seperti ini. Tidak ada yang ingin kehilangan konsentrasi sebelum langkah pembuka."
        yutaka "Kamu sendiri malah kelihatan santai banget di depan papan bagan begini."
        shiori "Di depan enam puluh empat petak ini, semua orang mulai dari posisi bidak yang sama persis. Itu justru ruangan paling tenang bagiku. Jadi, kamu datang ke sini untuk menonton, ikut mendaftar di slot terakhir, atau sekadar lewat? Aku bertanya lebih dulu supaya tidak salah menebak niatmu mampir."
    call kk_family_menu("S06", ["\"Aku sengaja datang buat nonton pertandinganmu kok.\"", "\"Masih ada kursi kosong di bagan? Aku ikut daftar main deh.\"", "\"Cuma mampir nyapa sebentar, habis ini masih ada urusan.\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Aku memang sengaja datang buat nonton pertandingan Saionji-senpai kok. Kalau aku duduk di deretan kursi penonton sebelah kiri sana, nggak mengganggu kan?"
            shiori "Tidak sama sekali. Tapi jangan terkejut kalau babak tengah nanti berjalan sangat lambat ya, Amamiya-san. Kadang satu langkah bisa memakan waktu sepuluh menit tanpa ada bidak yang bergeser."
            chiasa "Tenang aja, Senpai, aku betah kok duduk memperhatikan komposisi."
            nar "Kamu mengambil tempat duduk di barisan penonton sisi kiri yang menghadap langsung ke meja nomor satu. Ketika babak perempat final dimulai, pertandingan berjalan jauh lebih alot daripada perkiraan. Lawan Shiori yang merupakan senior klub bertahan sangat rapat di balik susunan pion ganda, memaksa permainan berlangsung hampir empat puluh menit."
            nar "Pada menit ketiga puluh, beberapa penonton di belakang sudah menguap dan keluar ruangan. Di meja satu, Shiori menatap papan selama tiga menit penuh tanpa menggerakkan jari, lalu perlahan meletakkan perwira kudanya di petak kanan yang jelas terancam pion lawan. Lawannya sempat terkejut sebelum memakan kuda itu, persis seperti umpan yang membuka garis tengah hingga rajanya terkunci sepuluh langkah kemudian."
            nar "Setelah menandatangani lembar hasil pertandingan dan berjabat tangan dengan lawannya, Shiori langsung melangkah menghampiri kursimu."
            shiori "Kamu benar-benar duduk di sini sampai langkah terakhir, Amamiya-san. Padahal kukira waktu masuk menit ketiga puluh tadi kamu sudah keluar mencari udara segar seperti penonton yang lain."
            chiasa "Mana mungkin aku keluar waktu lagi seru-serunya, Senpai. Apalagi waktu Senpai sengaja membiarkan perwira kuda di petak kanan itu dimakan lawan, aku sampai ikut menahan napas lihatnya."
            nar "Alis perak Shiori terangkat sedikit, dan senyum sopannya langsung berubah jauh lebih hidup. Ia menarik kursi kosong di sebelahmu lalu menunjuk papan meja satu yang belum dibereskan panitia."
            shiori "Kamu memperhatikan langkah kuda di giliran kesembilan belas itu? Jujur saja, sebelum melepas bidak itu aku sempat ragu hampir tiga menit. Menurutmu, kalau tadi kudanya kutarik mundur ke petak tengah untuk cari aman, apa yang akan dilakukan lawanku?"
            chiasa "Kelihatannya dia bakal langsung dorong bentengnya buat menutup baris tengah, Senpai. Justru karena Senpai biarkan kudanya diambil di kanan, perhatiannya jadi tersedot ke sana dan sisi rajanya malah lowong."
            shiori "...Bacaanmu tajam sekali. Kebanyakan orang yang menonton tadi hanya sibuk menghitung siapa yang memakan bidak lebih banyak sampai lupa melihat ruang kosong yang ditinggalkannya."
            chiasa "Soalnya tadi aku lihat gajah Senpai dari giliran sebelumnya sudah siap mengarah ke jalur itu."
            shiori "Pengamatan yang sangat bersih, Amamiya-san. Ayo ke ruang tunggu sebelah, kutraktir teh hangat sebelum babak semifinal dimulai."
            chiasa "Ayo, Senpai. Aku juga mau dengar strategi Senpai buat lawan berikutnya."
        else:
            yutaka "Sengaja datang buat nonton pertandinganmu lah, Saionji-san. Kalau aku duduk di kursi penonton pinggir sana boleh kan?"
            shiori "Silakan saja. Hanya saja kalau babak tengahnya nanti berjalan sangat lambat, usahakan jangan menguap terlalu lebar di dekat meja wasit, ya."
            yutaka "Tenang, aku nggak bakal ngantuk."
            nar "Kamu duduk di kursi kayu barisan penonton yang menghadap lurus ke meja unggulan pertama. Babak perempat final tersebut ternyata berjalan sangat lambat dan rapat. Lawan Shiori memasang pertahanan berlapis yang membuat setiap giliran memakan waktu berlama-lama di jam digital."
            nar "Mahasiswa lain yang tadinya menonton di dekat pintu perlahan bubar satu per satu, tetapi kamu tetap bertahan memperhatikan papan. Pada giliran kesembilan belas, Shiori diam cukup lama sebelum sengaja mendorong kudanya ke petak terbuka di sayap kanan. Begitu lawannya mengambil umpan itu, lajur tengah langsung runtuh sampai rajanya menyerah."
            nar "Begitu lembar skor selesai ditandatangani wasit, Shiori merapikan kursinya lalu berjalan langsung menghampirimu."
            shiori "Ternyata kamu sungguh bertahan duduk diam selama itu, Kisaragi-san. Hampir semua penonton biasa sudah keluar mencari angin waktu permainan melambat di menit kedua puluh tadi."
            yutaka "Sayang banget kalau keluar di tengah jalan. Bagian paling serunya kan justru waktu kamu sengaja mengorbankan kuda di sayap kanan itu."
            nar "Sorot mata ungu Shiori langsung menyala tertarik. Ia menarik kursi di sampingmu, duduk, lalu menoleh ke arah papan catur yang masih menyisakan posisi akhir pertandingan."
            shiori "Oh? Kamu membaca maksud langkah kuda itu juga? Padahal waktu jariku memegang bidaknya tadi, aku sempat bimbang cukup lama. Kalau menurutmu, seandainya tadi kudanya kutahan di petak tengah, apakah benteng lawanku akan tetap diam?"
            yutaka "Nggak mungkin diam, pasti langsung naik mengunci baris depanmu. Kalau kamu main aman di situ, justru langkahmu sendiri yang bakal kehabisan ruang."
            shiori "...Tepat seperti hitunganku. Menyenangkan sekali ada penonton yang benar-benar membaca papan alih-alih cuma menunggu siapa yang menang di akhir."
            yutaka "Kelihatan banget kok dari tadi kamu mengincar petak di belakang bentengnya."
            shiori "Mata yang jeli, Kisaragi-san. Ayo ke ruang sebelah sebentar, kutraktir teh sebelum babak berikutnya."
            yutaka "Boleh, sekalian lihat bagan lawanmu di semifinal."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Meja pendaftarannya belum ditutup kan, Saionji-senpai? Kalau masih ada satu slot kosong di bagan peserta, aku mau ikut daftar main sekalian."
            nar "Mata Shiori sedikit melebar, lalu senyum percaya diri yang tajam mengembang di bibirnya."
            shiori "Keputusan yang sangat menarik, Amamiya-san. Aku selalu lebih menyukai orang yang berani langsung duduk di balik papan daripada sekadar memberi komentar dari kursi penonton. Ayo, panitia masih membuka satu slot cadangan terakhir."
            nar "Kamu menuliskan namamu di meja panitia dan berhasil melewati babak pembuka melawan anggota tahun pertama. Di babak kedua, bagan undian langsung mempertemukanmu dengan Shiori di meja tengah."
            shiori "Ternyata kita langsung bertemu di babak kedua, Amamiya-san. Seperti biasa, di depan papan turnamen aku tidak akan memberikan keringanan."
            chiasa "Justru itu yang kucari, Saionji-senpai. Silakan mulai."
            nar "Begitu wasit menekan jam catur, gerakan Shiori mengalir tanpa sedikit pun rasa sungkan. Ia membuka serangan cepat dari sayap menteri, menekan ruang gerak perwiramu langkah demi langkah dengan ketelitian yang dingin."
            shiori "Kamu menarik kuda kembali ke baris kedua, Amamiya-san. Cukup berhati-hati."
            chiasa "Kalau kubiarkan di depan, pion Senpai langsung mendorongnya keluar."
            nar "Kamu berusaha keras menahan laju pionnya dan sempat mencuri satu gajahnya lewat jebakan silang di tengah papan. Alis perak Shiori terangkat tipis saat meletakkan gajahnya di pinggir papan."
            shiori "Jebakan silang yang bagus. Kalau begitu aku harus mempercepat tempo di sisi kanan."
            nar "Enam giliran kemudian, benteng dan menterinya tetap berhasil mengunci rajamu tanpa celah."
            shiori "Skakmat. Tapi serangan silangmu waktu mengambil gajahku di tengah tadi cukup mengejutkan, Amamiya-san."
            chiasa "Tetap aja baris belakangku jebol di akhir, Senpai. Aku sama sekali nggak sadar sejak kapan gajah kedua Senpai di pojok kiri itu sudah membidik petak rajaku."
            nar "Shiori sama sekali tidak memasang ekspresi menang yang angkuh. Dengan gerakan jari yang tenang, ia mengembalikan empat bidak ke posisi lima giliran sebelum permainan berakhir."
            shiori "Jalur diagonal gajahku itu sebenarnya masih tertutup rapat sampai giliran kedua puluh dua, Amamiya-san. Celahnya baru terbuka tepat ketika kamu memajukan pion tengah ini untuk memburu menteriku."
            chiasa "Ah... waktu aku dorong pion itu buat menyergap menteri Senpai ya?"
            shiori "Iya. Niat serangannya sudah bagus dan berani, hanya saja kamu jadi terlambat satu tempo untuk menarik bentengmu menjaga baris dasar. Kalau tadi kamu menahan pion itu satu giliran saja, aku yang harus memutar otak mencari jalan masuk."
            chiasa "Begitu ya... kelihatan jelas banget sekarang kalau diulang begini. Makasih banyak pelajarannya, Saionji-senpai."
            shiori "Sama-sama. Turnamen bulan depan ikut daftar lagi ya, aku ingin melihat seberapa jauh pertahanan tengahmu berkembang."
        else:
            yutaka "Meja pendaftarannya masih buka kan, Saionji-san? Kalau masih ada satu kursi kosong di bagan, aku ikut daftar main aja sekalian."
            nar "Senyum percaya diri yang tajam langsung muncul di wajah Shiori."
            shiori "Menantang langsung di turnamen resmi, ya, Kisaragi-san? Bagus, aku jauh lebih menghargai orang yang memilih turun ke papan daripada cuma berdiri menonton. Tulis namamu di meja panitia sekarang, masih tersisa satu slot."
            nar "Kamu mendaftarkan namamu dan berhasil memenangkan babak penyisihan pertama. Pada babak kedua, bagan pertandingan langsung menempatkanmu berhadapan dengan Shiori di meja utama."
            shiori "Kebetulan yang bagus, Kisaragi-san. Di meja resmi ini aku bermain dengan tenaga penuh ya."
            yutaka "Silakan, Saionji-san. Kalau kamu menahan langkah malah nggak seru."
            nar "Begitu jam digital ditekan, Shiori bermain tanpa sedikit pun menahan kekuatannya. Ia menekan dari sayap menteri dengan perhitungan yang rapat, memaksamu bertahan keras di setiap petak."
            shiori "Kamu tidak langsung memakan pion depanku di jalur kiri, Kisaragi-san."
            yutaka "Kelihatan terlalu gampang buat diambil, biasanya itu berarti kamu sudah menunggu di belakangnya."
            nar "Kamu sempat membalas dengan memotong jalur bentengnya di tengah papan, membuat Shiori berhenti dua puluh detik sebelum menyusun serangan balik. Lima giliran menjelang akhir, jepitan gajah dan menterinya tetap mengunci langkah rajamu."
            shiori "Skakmat. Pertahananmu di bagian tengah tadi lumayan alot untuk ditembus, Kisaragi-san."
            yutaka "Tetap aja kalah di ujung. Gajahmu yang di pojok kiri itu sejak kapan sudah mengincar petak belakang rajaku?"
            nar "Shiori tidak tersenyum meremehkan. Ia menggeser kembali beberapa bidak ke posisi empat langkah sebelum skakmat terjadi."
            shiori "Tepat sejak kamu memakan pion pinggirku di petak ini, Kisaragi-san. Langkahmu waktu itu cukup agresif dan hampir merusak susunanku, tapi gara-gara bentengmu bergeser satu petak ke samping, garis diagonal gajahku jadi terbuka lurus ke arah rajamu."
            yutaka "Oh... berarti pion pinggir yang kuburu tadi memang sengaja kamu pasang buat umpan ya?"
            shiori "Umpan yang baru bekerja kalau lawannya cukup berani untuk menyerang. Seandainya tadi kamu menggeser kuda lebih dulu sebelum memakan pion itu, justru posisiku yang akan kerepotan."
            yutaka "Rapi banget jebakanmu, Saionji-san. Kalau nggak kamu tunjukin barusan, mungkin sampai pulang aku masih bingung salah langkah di mana."
            shiori "Hehe, anggap saja itu bonus karena kamu sudah berani langsung mendaftar hari ini. Lain kali kalau ada turnamen terbuka lagi, pastikan namamu ada di daftar peserta ya."
    else:
        if kk_host == "chiasa":
            chiasa "Maaf ya, Saionji-senpai, aku cuma kebetulan lewat lorong depan terus lihat pintu klub terbuka, jadi mampir menyapa sebentar. Habis ini aku masih ada urusan tugas yang harus dibereskan."
            nar "Shiori mengangguk anggun, sama sekali tidak memperlihatkan kekecewaan maupun menahan langkahmu."
            shiori "Begitu ya. Terima kasih sudah menyempatkan berhenti untuk menyapa, Amamiya-san. Urusan tugas tentu harus didahulukan."
            chiasa "Semoga lancar dan menang turnamennya hari ini, Senpai. Aku permisi dulu."
            shiori "Terima kasih. Hati-hati di jalan, Amamiya-san."
            nar "Kamu melangkah keluar dari pintu ruang klub. Saat melewati jendela koridor, kamu melihat Shiori sudah kembali berbalik menghadap papan bagan pertandingan, memusatkan seluruh perhatiannya pada babak yang akan segera dimulai."
        else:
            yutaka "Aku cuma mampir menyapa sebentar kok waktu lihat pintu klub ramai, Saionji-san. Habis ini masih ada urusan lain yang harus kuurus, jadi belum bisa duduk menonton."
            nar "Shiori mengangguk sopan dengan raut wajah yang tetap tenang."
            shiori "Begitu. Terima kasih sudah menyempatkan mampir, Kisaragi-san. Jangan sampai urusanmu terlambat gara-gara berhenti di sini."
            yutaka "Semoga lancar pertandingannya hari ini. Aku duluan ya."
            shiori "Terima kasih. Hati-hati di jalan, Kisaragi-san."
            nar "Kamu berbalik meninggalkan ruang turnamen. Dari balik kaca pintu yang menutup, tampak Shiori sudah kembali menatap papan bagan pertandingan dengan fokus penuh."
    return

# ┌─ PANDUAN CERITA · S08 · Festival: Satu Tahun
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : peringatan perkenalan dengan Koita.
# │ INTI    : A hadir / B mengantisipasi / C mengganggu.
# │ AKHIRAN : dasar manga: ia mulai mencintai Koita.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S08:
    call kk_scene_enter("shiori", "Klub Catur")
    if kk_host == "chiasa":
        nar "Ruang Klub Catur hari itu jauh lebih lengang daripada biasanya karena sebagian besar anggota sedang tidak di tempat. Dari jendela lebar di sisi ruangan, terlihat beberapa panitia mahasiswa mulai memasang tiang spanduk untuk menyambut peringatan Festival Universitas yang tinggal sebentar lagi."
        nar "Di meja kayu dekat jendela, Saionji Shiori duduk sendirian di samping cangkir teh hitam yang tinggal separuh. Tidak ada papan pertandingan yang sedang dimainkan. Di depannya hanya tergeletak selembar brosur jadwal festival, sementara jemari tangan kanannya memutar-mutar pelan satu bidak kuda kayu."
        chiasa "Permisi, Saionji-senpai. Tumben ruang klub sepi banget, Senpai lagi ngecek jadwal turnamen buat festival ya?"
        nar "Shiori menoleh lalu mempersilakanmu duduk di kursi seberangnya dengan isyarat tangan yang anggun. Alis peraknya sedikit berkerut ketika matanya kembali jatuh pada deretan tanggal di brosur tersebut, seolah ia sedang agak kesal pada satu hal yang muncul di kepalanya sendiri."
        shiori "Silakan duduk, Amamiya-san. Sebenarnya aku sedang tidak memeriksa jadwal pertandingan. Aku hanya baru sadar saat membaca tanggal di brosur ini bahwa minggu ini tepat satu tahun sejak Festival Universitas tahun lalu."
        chiasa "Festival tahun lalu? Memangnya ada pertandingan penting waktu itu, Senpai?"
        shiori "Justru itu yang agak menjengkelkan. Aku bahkan tidak ingat jelas siapa lawan mainku di babak pertama tahun lalu. Aku malah ingat persis tanggal, cuaca sorenya, sampai sudut koridor tempat aku pertama kali berkenalan dengan kakakmu, Amamiya Koita."
        nar "Shiori meletakkan bidak kuda kayu itu ke atas brosur dengan bunyi pelan. Ada senyum tipis yang agak menyindir dirinya sendiri di sudut bibirnya."
        shiori "Waktu itu beberapa berkas rapat panitia jatuh berserakan di tengah keramaian lorong. Kakakmu langsung berjongkok membantu memungut lalu mengantar berkasnya sampai ke ruang panitia tanpa terlebih dahulu bertanya aku putri siapa atau marga apa yang kubawa. Secara rasional, puluhan mahasiswa lain juga bisa melakukan hal sederhana itu. Anehnya, dari sekian banyak orang yang kutemui setahun terakhir, ternyata aku tetap mengingat yang satu ini."
    else:
        nar "Ruang Klub Catur hari itu jauh lebih lengang daripada biasanya karena sebagian besar anggota sedang tidak di tempat. Dari jendela lebar di sisi ruangan, terlihat beberapa panitia mahasiswa mulai memasang tiang spanduk untuk menyambut peringatan Festival Universitas yang tinggal sebentar lagi."
        nar "Di meja kayu dekat jendela, Saionji Shiori duduk sendirian di samping cangkir teh hitam yang tinggal separuh. Tidak ada papan pertandingan yang sedang digelar. Di hadapannya hanya tergeletak selembar brosur jadwal festival, sementara jemari tangan kanannya memutar-mutar pelan satu bidak kuda kayu."
        yutaka "Permisi, Saionji-san. Tumben ruang klub sepi banget, lagi ngecek jadwal turnamen buat festival ya?"
        nar "Shiori menoleh lalu mempersilakanmu duduk di kursi seberangnya dengan isyarat tangan yang tenang. Alis peraknya sedikit berkerut ketika matanya kembali jatuh pada deretan tanggal di brosur tersebut, seolah ia sedang agak jengkel pada satu ingatan yang muncul begitu saja di kepalanya."
        shiori "Silakan duduk, Kisaragi-san. Sebenarnya aku sedang tidak memeriksa jadwal pertandingan. Aku hanya baru sadar saat melihat tanggal di brosur ini bahwa minggu ini tepat satu tahun sejak Festival Universitas tahun lalu."
        yutaka "Festival tahun lalu? Memangnya ada pertandingan penting waktu itu?"
        shiori "Justru itu yang agak menjengkelkan. Aku bahkan tidak ingat jelas siapa lawan mainku di babak pertama tahun lalu. Aku malah ingat persis tanggal, cuaca sorenya, sampai sudut koridor tempat aku pertama kali berkenalan dengan temanmu, Amamiya Koita."
        nar "Shiori meletakkan bidak kuda kayu itu ke atas brosur dengan bunyi pelan. Ada senyum tipis yang agak menyindir dirinya sendiri di sudut bibirnya."
        shiori "Waktu itu beberapa berkas rapat panitia jatuh berserakan di tengah lorong. Dia langsung berjongkok membantu memungut lalu mengantarnya sampai ke ruang panitia tanpa terlebih dahulu bertanya keluargaku siapa atau marga apa yang kubawa. Secara rasional, banyak orang lain juga bisa melakukan hal sederhana itu. Anehnya, dari sekian banyak orang yang kutemui setahun terakhir, ternyata aku tetap mengingat yang satu ini."
    call kk_family_menu("S08", ["\"Wajar kok kalau kejadian kayak gitu tetap diingat. Cerita aja kalau masih pengin bahas soal itu.\"", "Dengarkan pilihan katanya baik-baik dan ukur ke mana arah perasaannya sekarang.", "\"Cuma dibantuin pungut kertas segitu aja masa sampai diingat setahun penuh? Biasa aja kali.\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Wajar kok kalau momen kayak gitu tetap nempel di ingatan, Saionji-senpai. Selama ini kan orang-orang sering langsung mikirin nama keluarga Senpai duluan sebelum bicara. Kalau Senpai masih pengin cerita soal hari itu, aku dengerin kok."
            nar "Shiori menatapmu sejenak dengan mata ungu yang tenang, seolah memeriksa apakah ada nada menyindir atau rasa ingin bersaing di balik ucapanmu. Begitu melihat kamu hanya duduk mendengarkan dengan santai, bahunya tampak lebih rileks."
            shiori "Terima kasih sudah mau duduk menemani tanpa langsung mengubahnya jadi bahan ledekan, Amamiya-san. Aku memang tidak biasa mengakui hal yang tidak bisa dihitung dengan logika seperti ini."
            nar "Ia meraih teko porselen kecil di sudut meja dan menuangkan secangkir teh hitam hangat untukmu, lalu menyodorkannya pelan."
            shiori "Kalau dipikir lagi, mungkin aku terlalu lama terbiasa mengukur maksud orang dari langkah pembukanya. Jadi begitu ada seseorang yang berbuat baik tanpa motif jelas, kepalaku malah terus mencari tahu apakah ada sesuatu di baliknya."
            chiasa "Setelah setahun kenal Ko-nii, menurut Senpai gimana?"
            shiori "Harus kuakui kebaikan kakakmu itu konsisten. Hanya saja... ada satu keraguan yang masih membuatku menahan langkah. Aku memperhatikan cara ia memperlakukan teman-teman di sekelilingnya, dan kadar kehangatannya tampak begitu merata kepada hampir semua orang."
            chiasa "Maksud Senpai, susah dibedakan apakah dia memang menaruh perhatian khusus atau cuma bersikap baik ke semua orang?"
            shiori "Tepat sekali. Aku belum pernah bertanya langsung kepadanya apakah kebaikannya itu disertai kejelasan sikap atau memang sekadar kebiasaan agar tidak ada orang yang kecewa. Selama pertanyaan itu belum kujawab sendiri, aku lebih memilih duduk mengamati lebih dulu."
            chiasa "Tehnya enak, Senpai. Terima kasih sudah mau cerita sejujur itu."
            shiori "Sama-sama. Anggap saja hari ini kita sedang beristirahat dari papan catur sebentar."
            nar "Kalian terus berbincang santai di dekat jendela sambil menghabiskan teh hingga beberapa anggota klub mulai berdatangan membawa papan latihan."
        else:
            yutaka "Wajar kok kalau kejadian kayak gitu tetap diingat, Saionji-san. Orang-orang kan biasanya langsung mikirin nama keluargamu duluan sebelum ngomong apa-apa. Kalau masih pengin cerita soal hari itu, aku dengerin kok."
            nar "Shiori menatapmu sejenak dengan mata ungu yang tenang, seolah memeriksa apakah ada nada meledek atau niat memancing di balik ucapanmu. Begitu melihat kamu hanya duduk mendengarkan dengan santai, bahunya tampak lebih rileks."
            shiori "Terima kasih sudah mau duduk menemani tanpa langsung mengubahnya menjadi bahan candaan, Kisaragi-san. Aku memang tidak biasa mengakui hal yang tidak bisa diukur dengan logika seperti ini."
            nar "Ia meraih teko porselen kecil di sudut meja dan menuangkan secangkir teh hitam hangat untukmu, lalu menyodorkannya pelan."
            shiori "Mungkin aku terlalu lama terbiasa menilai maksud orang dari langkah pembukanya. Jadi begitu ada seseorang yang berbuat baik tanpa motif jelas, kepalaku malah terus mencari tahu apakah ada sesuatu di baliknya."
            yutaka "Setelah setahun kenal Koita, menurutmu dia gimana?"
            shiori "Harus kuakui kebaikannya konsisten. Hanya saja... ada satu keraguan yang masih membuatku menahan langkah. Aku memperhatikan cara ia memperlakukan orang-orang di sekelilingnya, dan kadar kehangatannya tampak begitu merata kepada hampir semua orang."
            yutaka "Kamu ragu apakah kebaikannya itu punya kejelasan sikap atau cuma kebiasaan biar nggak ada yang kecewa?"
            shiori "Tepat sekali. Aku belum pernah menanyakannya langsung kepadanya. Selama pertanyaan itu belum terjawab dengan jelas, aku lebih memilih duduk mengamati dari samping lebih dulu."
            yutaka "Tehnya pas banget. Makasih sudah mau cerita sejujur itu, Saionji-san."
            shiori "Sama-sama. Anggap saja hari ini kita sedang beristirahat dari strategi sebentar."
            nar "Kalian terus berbincang santai di dekat jendela sambil menghabiskan teh hingga beberapa anggota klub mulai berdatangan membawa papan latihan."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kamu tidak langsung memberi komentar panjang. Kamu duduk tegak di seberang meja, mengamati setiap pilihan kata Shiori, jeda napasnya, serta cara jarinya kembali menyentuh pangkal bidak kuda kayu di atas brosur festival."
            chiasa "Kedengarannya kejadian setahun lalu itu masih berkesan banget buat Saionji-senpai ya. Berarti di festival tahun ini Senpai juga berencana menyapa Ko-nii duluan kalau ketemu di stan acara?"
            nar "Shiori mengangkat pandangan menatapmu dengan senyum tipis yang sulit ditebak, lalu menyesap tehnya seteguk."
            shiori "Menarik sekali pertanyaanmu, Amamiya-san. Aku sama sekali belum menjanjikan perasaan apa pun, apalagi menyebut kata cinta yang terlalu cepat."
            chiasa "Aku cuma nanya aja kok, Senpai. Soalnya jarang banget dengar Saionji-senpai bahas seseorang selain soal strategi permainan."
            shiori "Memang jarang. Biasanya kemungkinan semacam ini langsung kupotong sejak awal dengan satu sindiran sopan supaya tidak mengganggu fokusku. Untuk yang satu ini, entah kenapa aku justru membiarkannya tetap berada di atas papan."
            nar "Kalimat itu jatuh dengan sangat jelas di telingamu. Gadis yang selama ini paling waspada dan menjaga jarak di seluruh kampus itu ternyata sudah mulai memberi ruang nyata bagi Koita, persis seperti arah cerita asli manga. Kamu mengangguk tenang menanggapi obrolannya tentang persiapan festival, sambil diam-diam menyusun perhitungan tentang bagaimana kamu akan menggunakan informasi ini sebelum semuanya berjalan terlalu jauh."
        else:
            nar "Kamu tidak buru-buru menanggapi panjang lebar. Kamu menyandarkan lengan di tepi meja, mendengarkan setiap pilihan kata Shiori, jeda napasnya, serta cara jemarinya kembali menyentuh bidak kuda kayu di atas brosur festival."
            yutaka "Kedengarannya kejadian setahun lalu itu masih berkesan banget ya, Saionji-san. Berarti di festival tahun ini kamu juga berencana nyapa Koita duluan kalau ketemu di stan acara?"
            nar "Shiori mengangkat pandangan menatapmu dengan senyum tipis yang sulit ditebak, lalu menyesap tehnya seteguk."
            shiori "Pertanyaan yang menarik, Kisaragi-san. Aku sama sekali belum menjanjikan perasaan apa pun, apalagi menyebut kata cinta yang terlalu tergesa-gesa."
            yutaka "Aku cuma tanya aja. Jarang banget dengar kamu bahas seseorang selain soal strategi permainan."
            shiori "Memang jarang. Biasanya kemungkinan semacam ini langsung kupotong sejak awal dengan satu sindiran sopan supaya tidak mengganggu fokusku. Untuk yang satu ini, entah kenapa aku justru membiarkannya tetap berada di atas papan."
            nar "Kalimat itu jatuh dengan sangat jelas di telingamu. Ia belum menjanjikan cinta, tetapi sudah memberi tempat bagi kemungkinan yang dahulu akan langsung ia tutup dengan sindiran. Mengetahui arah itu memberimu ruang untuk bertindak sebelum semuanya terlambat, sekaligus memaksamu menimbang bagaimana kamu akan menggunakan pengetahuan tersebut."
    else:
        if kk_host == "chiasa":
            nar "Kamu mendengus pelan sambil bersandar di sandaran kursi, memandang brosur festival di depan Shiori dengan nada enteng yang disengaja."
            chiasa "Cuma dibantuin pungut berkas yang jatuh di lorong aja masa sampai diingat tanggal sama cuacanya setahun penuh, Saionji-senpai? Ko-nii itu hampir tiap minggu bantu orang di kampus kayak gitu, jadi menurutku biasa aja kali, nggak ada yang spesial sampai perlu diperingati segala."
            nar "Jemari Shiori yang tadi memutar bidak kuda kayu seketika berhenti. Senyum sopan di bibirnya sama sekali tidak berubah, tetapi sorot mata ungunya langsung jatuh tajam dan dingin ke arahmu."
            shiori "...Begitu ya. Kucatat juga tanggapan yang satu ini, Amamiya-san."
            chiasa "Lho, aku kan cuma bilang fakta soal kebiasaan Ko-nii—"
            shiori "Kamu benar sekali. Rupanya aku terlalu banyak membuang waktumu dengan cerita pribadi yang tidak relevan."
            nar "Dengan satu gerakan bersih, Shiori memasukkan bidak kuda kayu itu ke dalam kotak penyimpanan, melipat brosur festival, lalu menarik berkas jadwal turnamen resmi ke hadapannya. Tepat saat itu pintu ruang klub dibuka oleh dua anggota tahun pertama."
            shiori "Pas sekali kalian sudah tiba. Mari kita periksa daftar bagan pertandingan untuk festival bulan depan. Amamiya-san, terima kasih sudah mampir sebentar hari ini."
            nar "Nadanya tetap sangat halus dan sopan sehingga dua anggota klub yang baru masuk tidak menyadari sedikit pun ketegangan di meja itu. Ruang pribadi yang tadi sempat dibuka sedikit oleh Shiori kini sudah tertutup rapat tanpa menyisakan celah bagimu."
        else:
            nar "Kamu mendengus pelan sambil bersandar di sandaran kursi, memandang brosur festival di depan Shiori dengan nada santai yang disengaja terdengar meremehkan."
            yutaka "Cuma dibantuin pungut berkas yang jatuh di lorong aja masa sampai diingat tanggal sama cuacanya setahun penuh, Saionji-san? Koita itu hampir tiap minggu bantu orang di kampus kayak gitu, biasa aja kali, nggak ada yang spesial sampai perlu diingat-ingat segala."
            nar "Jemari Shiori yang tadi memutar bidak kuda kayu seketika berhenti. Senyum sopan di bibirnya sama sekali tidak berubah, tetapi sorot mata ungunya langsung jatuh tajam dan dingin ke arahmu."
            shiori "...Begitu. Kucatat juga tanggapan yang satu ini, Kisaragi-san."
            yutaka "Lho, aku kan cuma bilang kebiasaan asli Koita di kampus—"
            shiori "Kamu benar sekali. Rupanya aku terlalu banyak membuang waktumu dengan cerita pribadi yang tidak relevan."
            nar "Dengan satu gerakan bersih, Shiori memasukkan bidak kuda kayu itu ke dalam kotak penyimpanan, melipat brosur festival, lalu menarik berkas jadwal turnamen resmi ke hadapannya. Tepat saat itu pintu ruang klub dibuka oleh dua anggota tahun pertama."
            shiori "Pas sekali kalian sudah tiba. Mari kita periksa daftar bagan pertandingan untuk festival bulan depan. Kisaragi-san, terima kasih sudah mampir hari ini."
            nar "Nadanya tetap sangat halus sehingga dua anggota klub yang baru masuk tidak menyadari sedikit pun ketegangan di meja itu, sementara ruang pribadi yang tadi sempat dibuka sedikit oleh Shiori kini sudah tertutup rapat tanpa menyisakan celah bagimu."
    return

# ┌─ PANDUAN CERITA · S11 · Peringkat Pertama
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ujian.
# │ INTI    : A kompetisi / B bantu / C menyontek.
# │ AKHIRAN : C masuk daftar.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S11:
    call kk_scene_enter("shiori", "Klub Catur")
    nar "Shiori menelusuri hasil ujian, berhenti pada satu kesalahan yang membuat peringkat pertamanya belum aman. Ia tidak mengatakan penilaiannya keliru; ia ingin tahu bagian mana yang tak cukup baik dipersiapkan."
    shiori "Aku ingin menang karena pekerjaanku. Kau ingin bersaing atau membantu, keduanya akan kuterima. Tapi jangan kira aku mencari seseorang yang cukup sayang untuk memberiku kemenangan."
    call kk_family_menu("S11", ["Bersaing dengannya secara jujur.", "Bantu ia belajar.", "Tawarkan cara menyontek diam-diam."])
    if _return == "A":
        shiori "Bagus. Kalahkan aku dengan benar kalau bisa."
        nar "Kalian membandingkan persiapan tanpa saling memberikan jawaban yang seharusnya dikerjakan sendiri. Persaingan itu membuatnya lebih hidup daripada pujian panjang tentang betapa tentu ia akan menang."
    elif _return == "B":
        shiori "Berdua ternyata lebih cepat. Terima kasih."
        nar "Ia menerima bantuanmu pada bagian yang belum dikuasai dan menawarkan keahliannya untuk bagian lain. Pada meja itu, membutuhkan seseorang tidak mengharuskannya berpura-pura tidak pernah salah."
    else:
        shiori "...Kau menawarkan itu. Aku akan mengingatnya."
        nar "Kau menawarkan kecurangan sebagai bantuan. Shiori menutup bahan belajar sebelum membalas dengan senyum tipis."
        shiori "Yang menarik, kau mengira aku ingin menang lebih besar daripada ingin dapat mempercayai caraku menang. Itu informasi penting tentangmu."
    return

# ┌─ PANDUAN CERITA · S12 · Rumor tentang Shiori
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : Mei menulis.
# │ INTI    : A bantu bantah / B diam / C menyebar.
# │ AKHIRAN : reputasi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S12:
    call kk_scene_enter("shiori", "Klub Catur")
    nar "Tulisan Mei menyebut kedekatan dan prestasi Shiori dengan cara yang membuat nama keluarganya menjadi jawaban bagi semua hal. Shiori membaca sampai selesai, lalu mengembalikan ponsel."
    shiori "Ia cukup cermat membicarakan orang yang dikenal semua orang, dan cukup ceroboh untuk mengira itu sama dengan mengenalku."
    call kk_family_menu("S12", ["Bantu bantah tulisan itu.", "Diamkan saja.", "Ikut menyebarkan tulisan itu."])
    if _return == "A":
        shiori "Kau membelaku tanpa kuminta. Itu... tidak biasa."
        nar "Kau membantah yang tidak berdasar tanpa menambahkan pujian yang juga tidak dapat diperiksa. Shiori menanyakan apakah kau tak takut dianggap sedang mencari muka, lalu tampak senang ketika jawabanmu tidak berusaha membuatnya berutang."
    elif _return == "B":
        nar "Kau tidak berkomentar. Shiori tetap bersikap biasa di hadapan orang lain. Ketika kalian sendiri, ia menanyakan apakah kau tidak tahu harus berkata apa atau sungguh percaya pada tulisan itu. Ia masih memberi kesempatan bertanya sebelum menyimpulkan."
    else:
        nar "Kau ikut menyebarkan. Shiori mengetahui bahwa namamu hadir dalam perjalanan kabar itu. Pada pertemuan berikutnya ia menyapamu sopan, menanyakan apakah tulisannya cukup menghibur."
        nar "Ia tidak membutuhkan suara keras untuk membuatmu sadar ada bagian yang tidak lagi dianggap gurauan."
    return

init 1 python:
    _hook("S03-A", lambda: kk_adj("respek_shiori",3))
    _hook("S03-B", lambda: kk_adj("respek_shiori",5))
    _hook("S06-A", lambda: (kk_rel("shiori","trust",4), kk_adj("respek_shiori",3)))
    _hook("S06-B", lambda: (kk_rel("shiori","trust",5), kk_adj("respek_shiori",5)))
    _hook("S06-C", lambda: kk_adj("respek_shiori",-3))
    _hook("S08-A", lambda: kk_rel("shiori","trust",5))
    _hook("S08-B", lambda: kk_flag("shiori_cinta_koita_dikenal"))
    _hook("S08-C", lambda: (kk_adj("marah_shiori",5), kk_adj("respek_shiori",-5)))
    _hook("S11-A", lambda: kk_adj("respek_shiori",5))
    _hook("S11-B", lambda: (kk_rel("shiori","trust",4), kk_adj("respek_shiori",3)))
    _hook("S11-C", lambda: kk_adj("daftar_kebohongan_shiori",1))
    _hook("S12-A", lambda: (kk_rel("shiori","trust",6), kk_adj("respek_shiori",5)))
    _hook("S12-B", lambda: kk_adj("marah_shiori",3))
    _hook("S12-C", lambda: (kk_adj("marah_shiori",10), kk_flag("shiori_rumor_disebar")))
