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
        nar "Hujan sore yang deras menahan langkah beberapa mahasiswa di bawah kanopi pintu masuk gedung Klub Catur. Air mengalir kencang dari tepi atap, menciptakan tirai berkilau yang memisahkan teras batu dari jalan setapak menuju gerbang depan."
        nar "Di tengah teras itu, Saionji Shiori berdiri dengan postur tegak dan tenang. Rambut putih keperakannya yang ditata menyilang bervolume di atas dan jatuh bergelombang melewati bahu sama sekali tak tersentuh tempias hujan. Ia melirik layar ponselnya sekali lalu memasukkannya kembali ke tas—mobil jemputannya rupanya tertahan macet di jalan utama dan baru bisa menunggu di dekat gerbang depan."
        nar "Tepat saat kau baru saja keluar dari lorong samping sambil menenteng payung lipatmu, Amamiya Koita muncul dari pintu utama, berhenti di samping Shiori, lalu membuka payung lipatnya dengan senyum hangat yang begitu otomatis."
        koita "Saionji-san, hujannya lumayan deras—kalau menunggu di sini terus nanti malah tambah sore dan dingin. Pakai payungku saja bareng sampai gerbang depan, yuk."
        nar "Melihat adegan klise semacam itu berlangsung tepat di depan matamu membuatmu sempat terdiam di sisi kanopi. Shiori tidak langsung menolak ataupun tersipu. Ia menurunkan pandangannya ke payung lipat berukuran standar di tangan Koita, lalu melirik lebar bahu Koita sendiri sebelum menoleh dengan senyum sopan yang disisipi sindiran halus."
        shiori "Kamu sudah membayangkan adegan yang cukup manis, Amamiya-san. Tapi sepertinya kamu belum menghitung lebar payungnya—kalau kita berjalan berdua di bawah itu, bukankah bahumu sendiri yang akan basah kuyup?"
        koita "Eh—haha, iya juga ya... tapi kalau cuma basah sedikit sih aku nggak masalah kok, yang penting Saionji-san nggak kehujanan sampai ke gerbang."
        nar "Shiori tersenyum ringan—senyum tipis yang nyaris mustahil ditebak apakah sedang geli, menilai, atau sekadar sopan. Ia menerima kebaikan kecil itu dengan anggun tanpa terburu-buru memberinya label ketertarikan apa pun."
        nar "Namun tepat sebelum mereka sempat melangkah turun dari anak tangga teras, mata ungu amethyst Shiori bergeser menangkap sosokmu yang berdiri beberapa langkah di sisi kanopi sambil menggenggam payung lipatmu sendiri."
        nar "Alis peraknya terangkat tipis sepersekian sentimeter. Tatapannya tenang, memberi ruang sekaligus menguji—seolah di atas papan permainan sore ini, ia sengaja menunggu apakah kau berniat melangkah maju dan ikut menentukan siapa yang berjalan dengan siapa di bawah hujan."
    else:
        nar "Hujan sore yang deras memaksa beberapa mahasiswa tertahan di bawah kanopi batu di depan gedung Klub Catur. Air tumpah deras dari tepi atap, membentuk tirai putih yang memisahkan teras dari jalan setapak menuju gerbang depan."
        nar "Di tengah teras itu, Saionji Shiori berdiri dengan postur tegak dan tenang. Rambut putih keperakannya yang ditata menyilang bervolume di atas dan jatuh bergelombang melewati bahu sama sekali tak tersentuh tempias hujan. Ia memeriksa layar ponselnya sekali lalu memasukkannya kembali ke tas—mobil jemputannya rupanya tertahan macet di jalan utama dan baru bisa menunggu di dekat gerbang depan."
        nar "Baru saja kau melangkah keluar dari lorong samping sambil menenteng payung panjangmu yang masih tertutup, Koita muncul dari pintu utama di dekat Shiori. Tanpa ragu sedikit pun, sahabat masa kecilmu itu langsung membuka payung lipatnya dengan senyum ramah yang sudah seperti refleks otomatis setiap kali melihat orang kesulitan."
        koita "Saionji-san, hujannya makin deras nih—kalau nunggu di sini terus nanti keburu gelap dan dingin. Pakai payungku saja bareng sampai gerbang depan, yuk."
        nar "Kau berhenti di sisi pilar kanopi, menyaksikan adegan klise yang nyaris seperti halaman manga itu berlangsung tepat di depan mata. Shiori tidak langsung mengangguk ataupun tersipu; ia menurunkan tatapannya ke payung lipat berukuran standar di tangan Koita, lalu melirik lebar bahu Koita sendiri sebelum menoleh dengan senyum sopan yang disisipi sindiran halus."
        shiori "Kamu sudah membayangkan adegan yang cukup manis, Amamiya-san. Tapi sepertinya kamu belum menghitung lebar payungnya—kalau kita berjalan berdua di bawah itu, bukankah bahumu sendiri yang akan basah kuyup?"
        koita "Eh—haha, iya juga sih... tapi kalau cuma basah sedikit aku nggak masalah kok, yang penting Saionji-san nggak kehujanan sampai ke gerbang."
        nar "Shiori tersenyum ringan—senyum tipis yang nyaris mustahil ditebak apakah sedang geli, menilai, atau sekadar sopan. Ia menerima kebaikan kecil itu dengan anggun tanpa terburu-buru memberinya label ketertarikan apa pun."
        nar "Namun tepat sebelum mereka sempat melangkah turun dari anak tangga teras, mata ungu amethyst-nya bergeser menangkap sosokmu yang berdiri beberapa langkah di sisi kanopi sambil menggenggam payung panjangmu."
        nar "Alis peraknya terangkat tipis sepersekian sentimeter. Tatapannya tenang namun tajam, jelas memberi ruang sekaligus menguji—seolah di atas papan permainan sore ini, ia sengaja menunggu apakah sahabat Amamiya-san sendiri berniat melangkah masuk dan ikut menentukan siapa yang berjalan dengan siapa di bawah hujan."
    call kk_family_menu("S03", ["Sela dan tawarkan mengantarnya sendiri.", "Tawarkan payung kedua untuk mereka.", "Biarkan saja mereka berangkat berdua."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau tidak membiarkan momen itu lewat begitu saja. Kau langsung melangkah maju mendekati tepi kanopi dan membuka payungmu sendiri dengan bunyi klik yang tegas, memotong jarak di antara Koita dan Shiori sebelum mereka sempat turun ke jalan setapak."
            chiasa "Kalau payung Ko-nii terlalu sempit buat berdua, biar aku saja yang antar Saionji-senpai ke gerbang depan. Bahu kita sama-sama kecil, jadi lebih muat dan tidak ada yang harus basah."
            koita "Lho, Chi-chan? Tumben lewat gedung sini—eh, nggak apa-apa kalau kau yang antar? Tadi aku sudah keburu menawarkan..."
            nar "Panggilan 'Chi-chan' dari Koita terdengar refleks seperti biasa, sementara Shiori sama sekali tidak langsung mengiyakan tawaranmu. Ia justru memandangmu dari ujung mata dengan senyum tipis yang penuh minat, seolah baru saja melihat seseorang menggerakkan bidak mendahului gilirannya."
            shiori "Oh? Kamu cepat sekali menengahi, Amamiya-san. Menarik sekali."
            nar "Ia melangkah setengah langkah mendekat ke arahmu, tetapi tetap berhenti tepat di batas kering kanopi. Sebelum masuk ke bawah payungmu, ia melontarkan satu pertanyaan sederhana dengan tatapan lurus yang sulit dihindari."
            shiori "Boleh aku tahu mengapa kamu menawarkan diri secepat itu? Apakah kamu memang searah denganku ke gerbang depan, atau ada alasan lain kamu tidak ingin kakakmu berjalan di bawah hujan bersamaku?"
            nar "Nada suaranya tetap lembut dan sopan, tetapi pertanyaannya setajam ujung bidak yang langsung mengincar celah pertahananmu. Di depan tatapan seperti itu, campur tanganmu harus segera mencari alasan yang terdengar masuk akal untuk diucapkan terang-terangan."
            chiasa "Aku memang mau ke arah gerbang depan, Saionji-senpai. Lagipula kalau Ko-nii kehujanan sampai masuk angin gara-gara sok kuat, nanti di rumah aku juga yang repot mengurusnya."
            koita "Hei, aku nggak segampang itu masuk angin tahu!"
            nar "Shiori menatapmu selama dua detik penuh, menimbang kejujuran di balik kalimat itu, lalu sudut bibirnya melengkung sedikit lebih jelas."
            shiori "Alasan yang sangat praktis—dan cukup jujur. Baiklah, kalau begitu aku terima tawaranmu, Amamiya-san. Terima kasih atas niat baiknya juga, Amamiya-san."
            nar "Ia melangkah masuk ke bawah payungmu dengan anggun, menjaga jarak yang pas namun cukup dekat untuk berbagi ruang teduh. Di belakang kalian, Koita hanya bisa berdiri di tepi kanopi sambil menggaruk tengkuknya dengan wajah bingung melihat rencana sederhananya mendadak diambil alih."
        else:
            nar "Kau tidak membiarkan momen itu lewat begitu saja. Kau langsung melangkah maju mendekati tepi anak tangga dan menekan tombol payung panjangmu hingga terbuka lebar dengan bunyi klik yang mantap, memotong jarak di antara Koita dan Shiori sebelum mereka sempat turun ke jalan setapak."
            yutaka "Payung lipatmu terlalu sempit buat berdua, Koita—bahu kirimu pasti basah semua sebelum setengah jalan. Biar aku saja yang antar Saionji-san ke gerbang depan, payungku jauh lebih lebar."
            koita "Lho, Yutaka? Tumben lewat gedung sini—eh, nggak apa-apa kalau kau yang antar? Tadi aku sudah keburu nawarin..."
            nar "Shiori sama sekali tidak langsung menerima ataupun menolak. Ia memandangmu dari sudut matanya dengan senyum tipis yang penuh rasa ingin tahu, seolah baru saja melihat pemain lain mendadak ikut duduk di depan papan caturnya."
            shiori "Oh? Kamu cepat sekali menengahi, Kisaragi-san. Menarik sekali."
            nar "Ia melangkah setengah langkah ke arahmu, tetapi tetap berhenti tepat di batas kering kanopi. Sebelum melangkah masuk ke bawah payungmu, ia menatap matamu lurus-lurus dengan satu pertanyaan sederhana yang sulit dielakkan."
            shiori "Boleh aku tahu mengapa kamu menawarkan diri secepat itu? Apakah kamu memang searah denganku ke gerbang depan, atau ada alasan khusus kamu tidak ingin temanmu berjalan berdua denganku?"
            nar "Nada suaranya tetap ringan dan sopan, namun pertanyaannya setajam langkah pembuka yang langsung menguji niatmu. Di depan tatapan seterang itu, campur tanganmu harus segera menemukan alasan yang terdengar masuk akal untuk diucapkan terang-terangan."
            yutaka "Aku memang searah ke gerbang depan, Saionji-san. Lagipula aku kenal Koita dari kecil—kalau dia nekat kehujanan begini, besok pasti demam dan ujung-ujungnya aku juga yang kena repot."
            koita "Hei, aku nggak selemah itu tahu, Yutaka!"
            nar "Shiori menimbang jawabanmu selama dua detik penuh dengan senyum yang tetap tak terbaca, lalu sudut bibirnya melengkung sedikit lebih jelas."
            shiori "Alasan yang cukup masuk akal—dan payungmu memang lebih luas. Baiklah, kalau begitu aku terima tawaranmu, Kisaragi-san. Terima kasih juga atas niat baiknya, Amamiya-san."
            nar "Ia melangkah masuk ke bawah payungmu dengan anggun, menjaga jarak yang rapi namun cukup dekat untuk berbagi ruang teduh. Di belakang kalian, Koita hanya bisa berdiri di tepi kanopi sambil menggaruk tengkuknya dengan wajah bingung melihat rencananya baru saja disela sahabatnya sendiri."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Alih-alih memaksa masuk di antara mereka secara terang-terangan, kau melangkah maju dengan tenang dan menyodorkan payung lipatmu yang masih tergulung rapi langsung ke arah Shiori."
            chiasa "Saionji-senpai, pakai payungku saja supaya tidak usah berdesakan di bawah satu payung."
            koita "Eh—Chi-chan, nanti kamu sendiri pulang pakai apa?"
            chiasa "Payungmu kan masih ada, Ko-nii. Aku bisa pulang bareng kamu atau menunggu sebentar sampai hujannya agak reda. Kalau Saionji-senpai pegang payung sendiri, tidak ada satu pun yang bahunya basah."
            nar "Shiori menatap payung di tanganmu, lalu menatap wajahmu sejenak. Senyum tipis di bibirnya tampak benar-benar menghargai langkah yang bersih, efisien, dan tidak berlebihan itu."
            shiori "Sopan sekali, Amamiya-san. Aku mencatat itu—terima kasih banyak. Besok pasti kukembalikan dalam keadaan bersih dan kering."
            nar "Ia menerima payung lipatmu dengan kedua tangan secara anggun, membukanya dengan satu gerakan halus, lalu menoleh ringan ke arah Koita dengan sorot mata yang tenang."
            shiori "Dengan begini, tidak ada yang harus kehujanan demi kesopanan. Nah, Amamiya-san—kalau kamu masih ingin berjalan ke arah gerbang depan, aku tidak keberatan. Tapi sekarang sepenuhnya keputusanmu sendiri, bukan karena aku butuh payung."
            koita "Ah... iya, tentu! Aku juga memang searah ke depan kok—eh, tapi Chi-chan nanti ikut sekalian saja ya!"
            nar "Dengan hilangnya alasan 'berbagi satu payung', suasana yang tadinya nyaris terasa seperti adegan romantis mendadak kembali menjadi perjalanan sore biasa. Mereka memang tetap berjalan ke arah gerbang yang sama, tetapi terpisah di bawah payung masing-masing tanpa jarak terlalu dekat yang bisa dipaksakan oleh hujan."
        else:
            nar "Alih-alih menyela secara terang-terangan, kau melangkah maju dengan santai lalu menyodorkan payung panjangmu yang masih tergulung rapi langsung ke hadapan Shiori."
            yutaka "Pakai punyaku saja, Saionji-san, biar nggak perlu berdesakan di bawah satu payung kecil."
            koita "Eh—Yutaka, terus kau sendiri pulang pakai apa?"
            yutaka "Aku bisa nebeng payungmu atau tunggu sebentar di sini sampai hujannya agak reda. Yang penting nggak ada satu pun yang bahunya basah cuma gara-gara payung kekecilan."
            nar "Shiori menatap gagang payung di tanganmu lalu melirik wajahmu sejenak. Senyum tipis di bibirnya tampak benar-benar menghargai langkah yang bersih, praktis, dan tidak memaksa itu."
            shiori "Sopan sekali, Kisaragi-san. Aku mencatat itu—terima kasih banyak. Besok pasti kukembalikan dalam keadaan bersih dan kering."
            nar "Ia menerima payung itu dengan kedua tangan secara anggun, membukanya dengan satu gerakan halus, lalu menoleh ringan ke arah Koita dengan sorot mata yang tenang."
            shiori "Nah, dengan begini tidak ada satu pun yang harus kehujanan demi kesopanan. Amamiya-san, kalau kamu masih ingin berjalan ke arah gerbang depan, aku tidak keberatan—tapi sekarang sepenuhnya keputusanmu sendiri, bukan karena aku butuh payung."
            koita "Ah... iya! Aku memang searah ke depan kok—ayo sekalian saja, Yutaka!"
            nar "Dengan hilangnya alasan 'berbagi satu payung', momen yang tadi hampir berbelok ke arah romantis langsung kembali menjadi perjalanan pulang biasa—terpisah di bawah payung masing-masing, tanpa jarak terlalu dekat yang dipaksakan oleh hujan."
    else:
        if kk_host == "chiasa":
            nar "Kau memilih tetap berdiri diam di sisi kanopi tanpa ikut campur, membiarkan mereka berdua menyelesaikan percakapan mereka sendiri sambil menggenggam gagang payungmu yang masih tertutup."
            nar "Koita menanggapi sindiran Shiori dengan tawa kecil yang sedikit malu, lalu melangkah turun lebih dulu ke batas hujan sambil sengaja memiringkan gagang payungnya cukup jauh ke sisi kanan untuk melindungi bahu Shiori."
            koita "Ayo, Saionji-san, sebelah sini lebih lebar ruangnya. Jalannya agak pelan saja biar sepatumu nggak kena cipratan genangan."
            shiori "Kamu benar-benar memiringkannya sejauh itu, ya... lihat, bahu kirimu sudah mulai basah padahal kita baru melangkah tiga langkah."
            koita "Nggak apa-apa, cuma sampai gerbang depan kok. Jaketku juga cepat kering."
            shiori "Begitu. Kamu memang tipe orang yang tidak terlalu memikirkan kerugian kecil untuk diri sendiri, ya, Amamiya-san."
            nar "Dari bawah kanopi, kau melihat punggung mereka perlahan menjauh menyusuri jalan setapak yang basah. Kau sempat menangkap bagaimana Shiori melirik bahu jaket Koita yang mulai gelap terkena air hujan."
            nar "Ia jelas menyadari perhatian yang sungguh-sungguh dilakukan di balik gerakan kecil itu—meski dari langkahnya yang tetap teratur dan bahunya yang tak sedikit pun mendekat lebih jauh dari perlu, ia belum memberinya arti lebih daripada kebaikan seorang kenalan."
        else:
            nar "Kau memilih tetap bersandar tenang di dekat pilar kanopi sambil menyelipkan satu tangan ke saku celana, membiarkan mereka berdua menyelesaikan percakapan mereka sendiri tanpa ikut campur."
            nar "Koita menanggapi sindiran Shiori dengan tawa kecil yang sedikit kikuk, lalu melangkah turun lebih dulu ke batas hujan sambil memiringkan payungnya cukup jauh ke sisi kanan untuk melindungi bahu Shiori."
            koita "Ayo, Saionji-san, lewat sisi sini saja biar sepatumu nggak kena genangan."
            shiori "Kamu benar-benar memiringkannya sejauh itu, ya... bahu kirimu sudah mulai basah padahal kita baru melangkah tiga langkah."
            koita "Nggak apa-apa, cuma sampai gerbang depan kok. Jaketku cepat kering."
            shiori "Begitu. Kamu memang tidak terlalu menghitung kerugian kecil untuk diri sendiri, ya, Amamiya-san."
            nar "Dari bawah kanopi, kau memperhatikan punggung mereka perlahan menjauh di tengah tirai hujan. Kau sempat menangkap bagaimana Shiori melirik bahu jaket Koita yang mulai gelap tersiram air."
            nar "Ia jelas menyadari perhatian tulus yang sungguh-sungguh dilakukan di balik gerakan kecil itu—meski dari langkahnya yang tetap teratur dan jarak bahunya yang terjaga, ia belum memberinya arti lebih jauh daripada kebaikan seorang kenalan."
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
    nar "Shiori memeriksa jadwal turnamen dan menawarkan kursi dengan gerakan yang sama seperti menyambut lawan. Di sini nama keluarganya tidak dapat memindahkan bidak setelah langkah yang buruk. Ia tampak menikmati itu."
    shiori "Kau menonton, bertanding, atau hanya lewat? Ketiganya boleh. Aku hanya ingin tahu sebelum terlanjur senang melihatmu duduk."
    call kk_family_menu("S06", ["Hadir dan dukung permainannya.", "Ikut bertanding melawannya.", "Lewat saja tanpa menonton."])
    if _return == "A":
        shiori "Kau tetap sampai babak terakhir. Tidak banyak yang begitu."
        nar "Kau menunggu bahkan ketika permainan menjadi lambat. Sesudahnya Shiori mengajak membahas satu keputusan yang diragukannya, memberi tempat pada pendapatmu meski tidak datang sebagai peserta."
    elif _return == "B":
        shiori "Berani. Aku suka lawan yang mau duduk di seberangku."
        nar "Pertandingannya menuntut seluruh perhatianmu. Shiori tidak mengurangi keseriusan untuk tampak ramah, dan setelah selesai ia menjelaskan satu langkahnya tanpa membuat penjelasan itu terdengar seperti belas kasihan."
    else:
        nar "Kau melanjutkan langkah. Shiori mengucapkan selamat jalan dan kembali ke jadwal. Pertandingan akan tetap berarti baginya tanpa penonton yang sedang tidak ingin hadir."
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
    nar "Shiori mengingat tanggal pertemuan dengan Koita lebih tepat daripada rincian sebuah kemenangan. Ia tampak sedikit jengkel pada fakta bahwa ingatan itu datang tanpa diminta."
    shiori "Setahun sejak festival itu. Aku ingat dia menawarkan bantuan tanpa lebih dahulu bertanya keluargaku siapa. Banyak orang bisa melakukan itu. Ternyata aku tetap mengingat yang satu ini."
    call kk_family_menu("S08", ["Temani ia memperingatinya dengan tenang.", "Antisipasi ke mana perasaannya mengarah.", "Ganggu peringatan kecil itu."])
    if _return == "A":
        shiori "Terima kasih sudah menemani. Aku tidak biasa mengakui hal seperti ini."
        nar "Kau mendengarkan tanpa mengubah perasaannya menjadi tantangan untuk direbut. Shiori berbicara lebih jauh, termasuk keraguannya tentang apakah kebaikan Koita disertai kejelasan yang belum pernah ia tanyakan."
    elif _return == "B":
        nar "Kau memperhatikan pilihan katanya. Ia belum menjanjikan cinta, tetapi sudah memberi tempat bagi kemungkinan yang dahulu akan ditutup dengan sindiran. Mengetahui arah itu memberi kesempatan bertindak sebelum terlambat, juga tanggung jawab atas bagaimana kau akan memakai pengetahuan tersebut."
    else:
        shiori "...Begitu. Kucatat juga yang satu ini."
        nar "Gangguanmu membuatnya berhenti bercerita. Ia mengembalikan percakapan ke jadwal festival, cukup sopan untuk tidak menegur di depan orang lain dan cukup jelas untuk menunjukkan bahwa ruang pribadi tadi sudah ditutup."
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
