# Miyuki awal (Mi04, Mi08, Mi10). Menyambung jalur pemulihan (Sato Kyoko) dan
# kerentanan yang dibaca arc klinik/CBT. Efek mengikuti Event_Miyuki dan Alur_Cabang/01.
# ┌─ PANDUAN CERITA · Mi04 · Tali Obi
# │ LOKASI  : Kampus Kouseikan · Gedung Kedokteran
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : kesulitan memakai yukata.
# │ INTI    : A bantu / B panggil Sena / C goda.
# │ AKHIRAN : intimasi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi04:
    call kk_scene_enter("miyuki", "Gedung Kedokteran")
    if kk_host == "chiasa":
        nar "Menjelang sore di dalam ruang ganti kecil Gedung Kedokteran yang dipinjam sebelum rombongan berangkat ke festival musim panas, cahaya matahari hangat masuk miring melewati tirai jendela. Aroma samar parfum bunga dan kayu kipas lipat memenuhi ruangan. Di depan cermin rias tinggi, Tachibana Miyuki berdiri membelakangi kaca sambil memegang kedua ujung kain obi berwarna merah anggur di punggungnya."
        nar "Yukata biru tua bermotif bunga tipis yang ia kenakan tampak sangat serasi dengan rambut hitam lurus panjangnya, tetapi begitu ia mencoba menoleh melewati bahu untuk mengencangkan simpul di belakang pinggangnya, lipatan kain tebal itu kembali melorot pelan dan terlepas."
        nar "Miyuki menghela napas panjang dengan bahu sedikit turun, menatap bayangannya sendiri di cermin dengan ekspresi menyerah yang jarang sekali terlihat di depan umum."
        miyuki "Ara... aku bisa menghafal ratusan halaman buku anatomi manusia tanpa keliru satu cabang saraf pun. Ternyata sehelai kain sabuk sepanjang ini punya kemauannya sendiri."
        chiasa "Tadi di depan cermin sudah dicoba lipat dari depan dulu, Tachibana-senpai?"
        miyuki "Sudah, Chiasa-chan. Waktu kulipat di depan kelihatannya rapi sekali, eh begitu kupuntir ke belakang, sayap pitanya langsung miring sebelah lagi."
        chiasa "Kain obinya memang agak licin ya, Senpai, apalagi yang model pita lebar begini."
        miyuki "Iya, baru aku beli bulan lalu buat festival tahun ini. Waktu dicoba bantu pakaikan sama penjaga tokonya kelihatannya gampang banget, ternyata begitu dicoba sendiri di cermin bikin tangan pegal semua."
        nar "Dari balik pintu kayu ruang ganti, suara teman-teman rombongan di lorong luar mulai memanggil untuk menanyakan apakah kalian berdua sudah siap berangkat. Seketika punggung Miyuki kembali tegak; ia menyahut dengan suara lembut dan tenang khas senior yang selalu serba siap."
        miyuki "Iya, sebentar lagi kami keluar kok! Tunggu lima menit lagi di lobi ya!"
        nar "Begitu langkah kaki di lorong luar menjauh, bahunya kembali turun dan ia menoleh ke arahmu yang sudah selesai merapikan pakaian. Sepasang matanya yang biru safir memandangmu dengan senyum kikuk yang jujur meminta pertolongan."
        miyuki "Chiasa-chan... boleh Senpai minta tolong sebentar? Sepertinya aku sudah kalah lima kali berturut-turut melawan tali obi ini."
    else:
        nar "Menjelang sore di lorong persiapan yang sepi di depan ruang ganti Gedung Kedokteran, cahaya matahari jatuh miring ke lantai keramik di dekat sebuah cermin dinding tinggi yang biasa dipakai mahasiswa merapikan jas laboratorium. Saat kamu datang menyusul untuk memeriksa apakah rombongan sudah siap berangkat ke festival musim panas, kamu mendapati Tachibana Miyuki berdiri seorang diri membelakangi cermin tersebut."
        nar "Ia sudah tampak anggun mengenakan yukata biru tua bermotif bunga tipis dengan rambut hitam panjangnya yang disampirkan ke satu sisi bahu, hanya saja kedua tangannya masih kesulitan menahan ujung kain obi merah anggur di punggungnya. Begitu ia mencoba menoleh lewat bahu untuk mengunci simpulnya, lipatan pita tebal itu kembali miring dan melorot pelan."
        nar "Miyuki mendesah panjang dengan bahu sedikit turun, menatap pantulan dirinya di kaca dengan raut kewalahan yang hampir tidak pernah ia perlihatkan di hadapan mahasiswa lain."
        miyuki "Ara... aku bisa menghafal ratusan halaman buku anatomi tanpa salah satu nama saraf pun. Ternyata mengikat kain sepanjang ini di belakang punggung jauh lebih rumit."
        yutaka "Dari tadi belum ketemu simpulnya, Tachibana-senpai?"
        miyuki "Hehe, ketahuan deh... waktu kulipat di depan perut kelihatannya rapi banget, tapi begitu kupuntir ke punggung, bentuk pitanya langsung miring dan longgar lagi."
        yutaka "Kainnya kelihatan cukup tebal dan licin juga sih."
        miyuki "Iya, baru kubeli bulan lalu buat festival tahun ini. Waktu dicontohkan penjaga tokonya kelihatannya cuma butuh tiga puluh detik, ternyata begitu praktik sendiri di sini malah bikin bahu pegal."
        nar "Dari ujung koridor dekat tangga lobi, suara rombongan yang sudah menunggu mulai terdengar memanggil. Seketika postur Miyuki kembali tegak; ia menyahut dengan nada suara lembut dan meyakinkan khas senior teladan yang selalu beres."
        miyuki "Iya, sebentar lagi kami turun menyusul kok! Tunggu lima menit lagi di bawah ya!"
        nar "Begitu suara di lobi mereda, ia menoleh ke arahmu yang berdiri beberapa langkah di lorong. Mata biru safirnya memandangmu dengan senyum canggung yang sungguh-sungguh meminta bantuan."
        miyuki "Yutaka-kun... kebetulan sekali kamu lewat sini. Boleh Senpai minta tolong sebentar? Sepertinya aku sudah kalah lima kali dari simpul obi ini."
    call kk_family_menu("Mi04", ["\"Boleh kubantu rapikan talinya dari belakang, Senpai?\"", "\"Sebentar ya, kupanggilkan Sena-san biar lebih rapi.\"", "\"Wah, ternyata Senpai yang biasanya paling tenang bisa kalah juga sama tali obi?\""])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu melangkah mendekat ke belakangnya, lalu berhenti setengah langkah untuk memastikan ia merasa nyaman sebelum tanganmu menyentuh kain sabuknya."
            chiasa "Boleh kubantu rapikan simpulnya dari belakang, Tachibana-senpai? Sini biar kupegang kedua ujung kainnya."
            nar "Miyuki mengangguk dengan raut wajah sangat lega, lalu mengangkat rambut hitam panjangnya ke depan dada dengan kedua tangan agar bagian punggung yukatanya terlihat jelas."
            miyuki "Terima kasih banyak, Chiasa-chan. Tolong jangan ditarik terlalu kencang ya bagian pinggangnya, soalnya nanti di sana Senpai masih ingin mencicipi takoyaki, apel karamel, sama es serut yang tadi kita bicarakan."
            chiasa "Hehe, tenang saja, Senpai, kupasang kencang di simpul luarnya saja supaya nggak melorot, tapi bagian perutnya tetap longgar buat bernapas. Coba tarik napas dulu, segini sudah pas belum?"
            miyuki "Hmm, pas sekali. Nggak sesak sama sekali waktu aku tarik napas."
            chiasa "Oke, sekarang tahan sebentar ya, aku lipat kedua sayap pitanya biar simetris sama garis punggung Senpai."
            nar "Kamu melipat kedua sayap kain merah anggur itu dengan teliti, menarik simpul tengahnya hingga duduk tegak dan seimbang di punggungnya, lalu menyelipkan tali penguncinya dengan rapi."
            chiasa "Selesai, Senpai. Coba lihat di cermin."
            nar "Ketika kamu menurunkan tanganmu, Miyuki memutar tubuhnya sedikit untuk memeriksa bayangan punggungnya di cermin, tetapi ia tidak langsung melangkah menjauh darimu. Ia justru menoleh dan berdiri cukup dekat di hadapanmu sambil tersenyum lembut tanpa sedikit pun topeng senior yang serba sempurna."
            miyuki "Wah, lipatan pitanya rapi sekali... jauh lebih cantik daripada kalau kuikat sendiri. Terima kasih banyak ya, Chiasa-chan. Ternyata rasanya menyenangkan juga ya kalau sesekali Senpai boleh nggak pandai satu hal di depanmu."
            chiasa "Tentu saja boleh, Senpai. Nggak ada orang yang harus bisa mengerjakan semuanya sendirian setiap waktu."
            miyuki "Di Fakultas Kedokteran, kalau ada satu detail kecil saja yang lepas, orang-orang langsung panik mengira ada masalah besar. Lama-lama aku jadi terbawa kebiasaan itu bahkan sampai urusan yukata."
            chiasa "Hari ini kan festival musim panas, Senpai. Nggak usah dibawa serius kayak ujian praktik di laboratorium, kalau ada yang miring tinggal minta tolong rapikan saja."
            miyuki "Hehe, benar juga. Kalau begitu, sebagai ucapan terima kasih, takoyaki pertama di festival nanti biar Senpai yang traktir ya. Yuk, kita ambil tas serut terus keluar sebelum yang lain curiga kenapa Senpai lama sekali."
            chiasa "Siap, ayo, Senpai."
            nar "Miyuki menurunkan rambut hitam panjangnya kembali melewati bahu, lalu berjalan keluar ruang ganti bersamamu dengan langkah yang jauh lebih ringan."
        else:
            nar "Kamu melangkah mendekat dengan tenang, lalu berhenti satu langkah di belakangnya untuk meminta izinnya lebih dahulu sebelum menyentuh kain obinya."
            yutaka "Boleh kubantu rapikan ikatannya dari belakang, Tachibana-senpai? Dulu aku sering diminta bantu nahan ujung simpul yukata di rumah, jadi kalau cuma merapikan lipatan luarnya aku masih bisa."
            nar "Miyuki mengangguk lega, lalu mengumpulkan rambut hitam lurus panjangnya ke depan bahu kiri agar punggungnya mudah dijangkau."
            miyuki "Terima kasih banyak, Yutaka-kun. Tolong jangan ditarik terlalu sesak ya, soalnya Senpai sudah mengincar jajanan di deretan stan festival nanti malam."
            yutaka "Tenang saja, Senpai, nggak bakal kubuat sesak. Coba tarik napas sebentar, ikatan dasarnya segini sudah nyaman?"
            miyuki "Iya, pas sekali. Sama sekali nggak menekan perut."
            yutaka "Tahan sebentar, aku rapikan lipatan sayap kanan kirinya biar duduk lurus di tengah."
            nar "Kamu merapikan lipatan pita tebal berwarna merah anggur itu dengan hati-hati, mengunci simpul tengahnya hingga duduk tegak dan seimbang di punggungnya, lalu merapikan kerutan kain yukata di bawahnya."
            yutaka "Sudah beres, Senpai. Coba cek di cermin."
            nar "Begitu kamu mundur setengah langkah, Miyuki memutar badan memeriksa cermin, lalu berbalik menghadapmu. Ia tetap berdiri cukup dekat darimu sesaat lebih lama sambil tersenyum hangat tanpa beban citra senior yang harus selalu sempurna."
            miyuki "Simpulnya rapi sekali... tanganmu cekatan juga ya. Terima kasih banyak, Yutaka-kun. Ternyata Senpai boleh ya sesekali kelihatan nggak becus mengurus satu hal di depan kamu."
            yutaka "Wajar lah, Senpai. Mengikat kain tebal di belakang punggung tanpa lihat itu memang susah kalau dikerjakan sendirian."
            miyuki "Di kampus semua orang terbiasa melihatku selalu siap sedia dan nggak pernah panik. Lama-lama aku sendiri jadi lupa kalau gagal mengikat pita yukata itu bukan kesalahan fatal."
            yutaka "Hari ini waktunya liburan festival, Senpai. Nggak usah tegang kayak lagi jadwal jaga rumah sakit, santai saja."
            miyuki "Hehe, kamu pintar sekali menghibur seniornya. Ayo kita turun sekarang, nanti di festival biar Senpai yang belikan minuman dingin sama jajanan pertama buatmu."
            yutaka "Boleh, kupegang janjinya ya, Senpai."
            nar "Ia tertawa kecil sambil menyampirkan tali tas serutnya ke pergelangan tangan, lalu melangkah turun menuju lobi bersamamu dengan langkah santai."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Menyadari bahwa tangan seseorang yang benar-benar terbiasa memakai yukata akan menghasilkan ikatan yang jauh lebih kuat dan rapi untuk dipakai berjalan sampai malam, kamu melangkah ke pintu ruang ganti dan memanggil sahabat seangkatan Miyuki yang sedang menunggu di koridor."
            chiasa "Sena-san! Maaf, boleh minta tolong masuk ke ruang ganti sebentar? Tachibana-senpai butuh bantuan merapikan ikatan obinya."
            nar "Pintu kayu langsung dibuka dari luar. Sena melangkah masuk, berhenti sejenak menahan tawa begitu melihat lipatan kain merah anggur yang nyaris terbalik di punggung Miyuki, lalu segera maju mengambil alih dengan gerakan tangan yang cekatan."
            "Sena" "Astaga, Miyuki... lain kali panggil aku sebelum kamu lima kali membongkar pasang sendiri sampai kainnya kusut begini, bisa nggak sih?"
            miyuki "Aku kan cuma ingin mencoba menyelesaikannya sendiri dulu, Sena. Lima kali percobaan itu masih masuk hitungan usaha yang wajar, tahu."
            "Sena" "Iya deh, mahasiswi teladan Fakultas Kedokteran yang gengsi minta bantuan bahkan sama selembar sabuk kain. Untung ada Chiasa-chan di sini yang langsung manggil aku. Nah, tahan napas sedikit... satu, dua, selesai!"
            miyuki "Wah, cepat banget! Kenapa kalau di tanganmu langsung rapi ya, Sena?"
            "Sena" "Soalnya aku nggak mencoba menghitung sudut lipatannya pakai rumus anatomi, Miyuki. Sudah, aku duluan turun tahan anak-anak di lobi ya, kalian cepat nyusul!"
            nar "Sena melambai santai lalu melangkah keluar lebih dulu. Ketika kalian berdua menyusul keluar dari ruang ganti menuju lobi tempat rombongan menunggu, Miyuki menyejajarkan langkahnya di sampingmu dan menoleh dengan rona malu tipis di pipinya."
            miyuki "Terima kasih ya sudah berinisiatif memanggilkan Sena tadi, Chiasa-chan. Jujur tadi agak malu sih ketahuan berantakan begitu... tapi ternyata lega juga rasanya sadar kalau aku nggak harus selalu membereskan semuanya sendirian dulu sebelum boleh ikut bersenang-senang."
            chiasa "Nggak perlu malu sama sekali, Senpai. Justru karena dibantu Sena-san, sekarang ikatan obinya rapi sekali dan kita nggak terlambat berangkat bareng rombongan."
            miyuki "Hehe, kamu benar. Ayo kita turun sama-sama!"
            nar "Langkahnya menuruni tangga lobi terasa jauh lebih santai dibandingkan ketegangan kecil yang tadi membelit bahunya di depan cermin."
        else:
            nar "Menyadari bahwa tangan seseorang yang memang ahli mengenakan yukata akan jauh lebih rapi dan nyaman bagi Miyuki, kamu menoleh ke ujung koridor lalu melangkah cepat memanggil sahabat dekatnya yang sedang mengobrol di dekat tangga."
            yutaka "Sena-san, maaf, bisa minta tolong ke depan cermin lorong sebentar? Tachibana-senpai lagi kesulitan mengikat obinya."
            nar "Sena langsung bergegas menghampiri cermin tersebut, dan seketika harus menahan tawa begitu melihat simpul kain di punggung Miyuki yang nyaris terpasang terbalik sebelum ia mengambil alih dengan terampil."
            "Sena" "Ya ampun, Miyuki... lain kali tolong panggil aku sebelum kamu bergulat lima kali sendiri sampai ujung kainnya lecek begini, boleh nggak?"
            miyuki "Aku kan cuma ingin berusaha mengikatnya sendiri dulu, Sena. Lima kali itu masih masuk batas mencoba."
            "Sena" "Iya deh, iya, tuan putri yang pantang menyerah. Untung Yutaka-kun langsung nyari aku tadi. Coba tegakkan punggungmu sebentar... nah, sudah rapi dan kencang!"
            miyuki "Lho, sudah jadi? Cepat sekali!"
            "Sena" "Iyalah, aku nggak terlalu ribet mikirin simetri lipatannya. Aku turun duluan ya jagain yang lain biar nggak ketinggalan bus, kalian cepat nyusul!"
            nar "Ketika kalian berjalan turun menyusul rombongan di lobi bawah, Miyuki melangkah di sebelahmu dan menoleh dengan wajah sedikit tersipu dan tampak jauh lebih santai."
            miyuki "Terima kasih ya sudah memanggilkan Sena buatku, Yutaka-kun. Sedikit malu sih ketahuan kesusahan begitu... tapi ternyata lega sekali rasanya tahu kalau aku nggak harus selalu membuktikan bisa menyelesaikan semuanya sendiri sebelum berangkat."
            yutaka "Nggak usah dipikirkan, Senpai. Semua orang juga tahu mengikat obi sendiri itu susah. Yang penting sekarang sudah rapi dan kita bisa langsung berangkat."
            miyuki "Hehe, iya. Ayo kita susul yang lain ke depan!"
            nar "Ia tersenyum ringan sambil merapikan ujung lengan yukatanya saat kalian melangkah bergabung dengan rombongan di lobi."
    else:
        if kk_host == "chiasa":
            nar "Melihat senior Kedokteran yang di kampus selalu tampak tenang, anggun, dan serba bisa itu ternyata dibuat kewalahan oleh sehelai kain sabuk, senyum jahil langsung terbit di bibirmu."
            chiasa "Wah, pemandangan langka nih. Ternyata Tachibana-senpai yang biasanya paling tenang dan sempurna di kampus bisa kalah telak juga sama sehelai tali obi, ya?"
            nar "Miyuki langsung menoleh dari cermin sambil menggembungkan pipinya sedikit, sebuah ekspresi merajuk yang hampir tidak pernah ia tunjukkan di depan orang lain, sebelum sedetik kemudian ia sendiri ikut tertawa melihat pantulan dirinya yang berantakan di kaca."
            miyuki "Ih, Chiasa-chan jahat sekali malah meledek seniornya yang lagi kesusahan! Jangan ganggu konsentrasiku dulu ya, aku ini sedang bernegosiasi serius dengan kain obi ini."
            chiasa "Kalau negosiasinya gagal terus sampai ronde keenam, nanti kita ketinggalan kereta ke lokasi festival lho, Senpai. Sini kubantu tahan lipatan tengahnya biar nggak merosot waktu Senpai tarik."
            miyuki "Eh, boleh! Tolong tahan bagian lipatan pitanya di sini sebentar ya... nah, kalau ada yang menahan di tengah begini ternyata langsung gampang dikunci!"
            chiasa "Tarik sedikit lagi ke kiri, Senpai, biar pas di tengah punggung."
            miyuki "Begini? Wah, iya, langsung lurus! Akhirnya menang juga di ronde keenam!"
            nar "Karena gurauanmu berhasil mencairkan ketegangannya, jemari Miyuki kini bergerak jauh lebih luwes saat merapikan ujung simpulnya. Ketika suara rombongan di lorong luar kembali memanggil menanyakan kabar, Miyuki tidak lagi buru-buru memasang alasan yang kaku."
            miyuki "Tunggu satu menit lagi ya semuanya! Kali ini beneran sudah selesai kok!"
            chiasa "Beneran kelihatan bagus sekali sekarang, Senpai."
            miyuki "Hehe, berkat asisten negosiasi yang agak usil tapi berguna. Ayo kita keluar!"
            nar "Tawa ringan kalian berdua terdengar hangat di dalam ruang ganti itu saat Miyuki meraih tas serutnya dan melangkah keluar bersamamu."
        else:
            nar "Melihat senior Kedokteran yang biasanya paling tenang dan serba terkendali itu ternyata dibuat kewalahan oleh sehelai kain sabuk, kamu bersandar santai di dinding lorong dengan senyum jahil."
            yutaka "Wah, jarang-jarang nih bisa lihat Tachibana-senpai kalah telak sama sehelai kain. Bukannya di kampus Senpai terkenal selalu bisa membereskan apa saja dengan tenang?"
            nar "Miyuki langsung menoleh lewat bahunya sambil menggembungkan pipinya sedikit, ekspresi merajuk yang sangat jarang terlihat darinya, sebelum akhirnya ia sendiri hampir tertawa melihat bayangannya di cermin."
            miyuki "Yutaka-kun jahat sekali bukannya menolong malah meledek! Jangan mengganggu konsentrasiku dulu ya, Senpai sedang bernegosiasi serius dengan obi ini."
            yutaka "Kalau negosiasinya buntu terus sampai malam, nanti kembang apinya keburu selesai sebelum kita sampai sungai, Senpai. Coba lipat dulu sayap kirinya, biar kutahan ujung bawahnya dari sini supaya nggak melorot waktu Senpai tarik."
            miyuki "Oh, ide bagus! Tolong tahan ujung yang ini sebentar ya, Yutaka-kun... nah, kalau ditahan satu jari begini ternyata langsung mengunci rapi!"
            yutaka "Geser sedikit ke kanan biar pitanya sejajar garis punggung, Senpai."
            miyuki "Begini? Wah, beneran langsung tegak! Menang juga akhirnya di percobaan keenam!"
            nar "Karena leluconmu berhasil menurunkan rasa gugupnya, tangan Miyuki kini bergerak jauh lebih santai saat merapikan pita obinya. Ketika suara rombongan dari lobi bawah kembali memanggil, ia menyahut dengan nada ceria tanpa perlu membuat alasan sempurna."
            miyuki "Iya, ini kami sudah selesai kok! Kami turun sekarang!"
            yutaka "Lumayan juga hasil kerja sama kita, Senpai."
            miyuki "Hehe, lain kali tolong bantu duluan baru meledek ya, Yutaka-kun. Ayo turun!"
            nar "Tawa ringan kalian berdua bergema di sepanjang lorong menuju tangga lobi, mencairkan seluruh kecanggungan sebelum keberangkatan ke festival dimulai."
    return

# ┌─ PANDUAN CERITA · Mi08 · Sena dan Psikolog
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : Sena memperkenalkan Sato Kyoko.
# │ INTI    : A dukung konsultasi / B tolak / C abaikan.
# │ AKHIRAN : membuka jalur pemulihan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi08:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana")
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Taman tengah Rumah Sakit Tachibana malam itu sudah sepi dari pengunjung rawat jalan. Lampu-lampu taman berbentuk bulat di sepanjang tepi kolam kecil menyala terang, memantulkan cahaya kekuningan ke permukaan air serta bangku kayu panjang tempat Tachibana Miyuki duduk merapikan tas kuliahnya."
        else:
            nar "Taman tengah Rumah Sakit Tachibana sore menjelang petang itu mulai sepi dari pengunjung rawat jalan. Lampu-lampu taman berbentuk bulat di sepanjang tepi kolam kecil baru saja menyala, memantulkan cahaya kekuningan ke atas bangku kayu panjang tempat Tachibana Miyuki duduk merapikan tas kuliahnya."
        chiasa "Sudah selesai giliran observasi hari ini, Tachibana-senpai? Wajah Senpai kelihatan agak pucat."
        miyuki "Baru saja selesai sepuluh menit lalu, Chiasa-chan. Tadi di bangsal sempat ada pasien masuk mendadak jadi jam istirahat kami mundur dua jam. Aku duduk sebentar di sini buat mengecek lembar jadwal besok sebelum naik kereta pulang."
        chiasa "Belum sempat makan apa-apa dari siang berarti? Di luar sini anginnya dingin lho, Senpai, tangan Senpai aja kelihatan merah."
        miyuki "Hehe, sebentar lagi kok, habis cek jadwal besok aku langsung jalan ke stasiun."
        nar "Saat Miyuki menarik buku catatan klinis tebal dari dalam tas untuk memeriksa jadwal besok pagi, selembar kartu nama berukuran kecil berwarna putih gading terselip keluar dari sela halaman dan jatuh tepat di atas roknya."
        nar "Sebelum Miyuki sempat mengambil dan menyelipkannya kembali ke dalam buku, matamu sudah menangkap cetakan huruf rapi di bagian tengah kartu tersebut yang bertuliskan 'Sato Kyoko, Konselor Klinis & Psikologi Medis'."
        chiasa "Kartu nama siapa itu tadi, Tachibana-senpai? Pinggiran kertasnya sampai lecek begitu kayak sering dipegang."
        nar "Gerakan tangan Miyuki yang hendak menutup buku catatannya melambat. Ia menatap sela halaman tempat kartu itu disimpan, lalu menariknya keluar setengah dan tersenyum tipis dengan raut wajah yang tampak sangat letih."
        miyuki "Ketahuan ya, Chiasa-chan... ini dikasih Sena tiga hari lalu waktu kami habis selesai jaga praktik. Katanya Sato-san ini konselor yang biasa mendampingi mahasiswa kedokteran sama dokter muda."
        chiasa "Sena-san yang menyuruh Senpai datang ke sana?"
        miyuki "Iya. Waktu itu aku ketiduran di meja perpustakaan sampai catatan pasienku jatuh semua, terus Sena langsung menyodorkan kartu ini ke tanganku. Dia bilang jangan tunggu sampai benar-benar tumbang baru cari tempat bicara."
        chiasa "Terus Senpai belum sempat menghubungi beliau dari tiga hari lalu?"
        miyuki "Dari tiga hari lalu kartu ini sudah kubuka-tutup terus tiap malam di kamar, nomornya bahkan sudah pernah kuketik di layar panggilan, tapi ujung-ujungnya selalu kuhapus lagi sebelum kupencet tombol telepon."
        chiasa "Kenapa ragu, Senpai? Takut jadwalnya bentrok sama jam kuliah?"
        miyuki "Bukan soal jadwalnya sih... aku cuma membayangkan kalau nanti aku beneran duduk di sofa ruangannya Sato-san, terus beliau nanya ada masalah apa, aku bingung harus jawab apa."
        nar "Ibu jari Miyuki mengusap sudut kartu nama yang sudah agak melengkung itu pelan-pelan."
        miyuki "Maksudku, mahasiswa tahun ketiga kedokteran kurang tidur kan hal yang wajar banget. Kalau belakangan ini aku sering kebangun jam tiga pagi terus susah napas, atau tiba-tiba pengin menangis sendiri waktu lagi mencuci piring di dapur apartemen... itu kan paling cuma gara-gara kebanyakan minum kopi sama capek ujian aja, kan?"
        nar "Setiap kali ia menambahkan alasan baru untuk mengecilkan apa yang ia rasakan, suaranya justru terdengar semakin habis tenaga."
    else:
        if kk_slot >= 3:
            nar "Taman dalam Rumah Sakit Tachibana malam itu sudah lengang setelah jam besuk berakhir. Lampu-lampu taman di sepanjang jalan setapak memantulkan cahaya hangat ke permukaan kolam serta bangku kayu tempat Tachibana Miyuki duduk sambil memangku buku catatan tebalnya."
        else:
            nar "Taman dalam Rumah Sakit Tachibana sore menjelang petang itu mulai lengang setelah jam besuk sore berakhir. Lampu-lampu taman di sepanjang jalan setapak baru saja dinyalakan, menyinari bangku kayu tempat Tachibana Miyuki duduk sambil memangku buku catatan tebalnya."
        yutaka "Baru selesai jadwal praktik hari ini, Tachibana-senpai? Kelihatannya capek banget."
        miyuki "Iya, baru selesai sepuluh menit lalu, Yutaka-kun. Tadi di bangsal ada kasus darurat masuk jadi waktu istirahat kami kegeser cukup jauh. Sebentar ya, aku lagi merapikan lembar rotasi besok supaya nggak ada yang tertinggal."
        yutaka "Berarti belum sempat makan dari tadi? Duduk lama-lama di taman dingin begini malah tambah lemas nanti, Senpai."
        miyuki "Hehe, sebentar lagi kok, habis beresin lembar ini aku langsung pulang."
        nar "Ketika ia membuka sampul bukunya untuk menyelipkan lembar jadwal rotasi, selembar kartu nama putih gading terlepas dari sela halaman dan jatuh ke atas pangkuannya. Sekilas kamu dapat membaca cetakan nama 'Sato Kyoko, Konselor Klinis & Psikologi Medis' di atasnya, tepat sebelum Miyuki buru-buru memasukkannya kembali."
        yutaka "Kartu nama siapa tadi itu, Tachibana-senpai? Ujung kertasnya sampai terlipat-lipat begitu."
        nar "Miyuki terdiam sejenak dengan tangan masih di atas buku, lalu menghela napas pelan dan menarik kartu itu keluar setengahnya lagi."
        miyuki "Mata kamu cepat juga ya, Yutaka-kun. Ini kartu kontak dari Sena, dikasih ke aku tiga hari lalu. Kenalan konselor yang biasa menangani mahasiswa kedokteran. Waktu itu aku ketiduran di ruang baca sampai hampir telat masuk kelas, jadi Sena langsung memaksa aku simpan nomornya."
        yutaka "Terus sudah Senpai coba hubungi orangnya?"
        miyuki "Belum. Dari kemarin cuma kuambil dari buku, kuketik nomornya di layar ponsel, kupandangi lima menit, terus kusimpan lagi. Habisnya setiap kali mau menekan tombol panggil, aku bingung sendiri nanti di sana mau bicara apa."
        yutaka "Bingung gimana maksudnya, Senpai?"
        miyuki "Ya masa aku datang ke konselor cuma buat mengeluh capek kuliah, Yutaka-kun? Anak kedokteran begadang kan sudah biasa. Kalau akhir-akhir ini aku sering kebangun tengah malam dengan dada sesak, atau tiba-tiba pengin menangis sendiri waktu baru sampai kamar apartemen... itu paling cuma efek kebanyakan minum kopi sama memikirkan nilai aja, kan?"
        nar "Ia mencoba tertawa kecil di ujung kalimatnya untuk membuat keluhannya terdengar ringan, tetapi raut wajahnya di bawah lampu taman justru terlihat semakin pucat dan lelah."
    call kk_family_menu("Mi08", ["\"Datang aja, Senpai. Nggak usah nunggu sampai tumbang dulu baru boleh cerita.\"", "\"Senpai cuma kecapekan sama jadwal padat aja kok, tidur cukup juga beres.\"", "\"Ngomong-ngomong, minggu depan Senpai jadwal jaganya mulai jam berapa?\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Datang aja temui Sato-san itu, Tachibana-senpai. Orang datang ke konselor kan nggak harus menunggu sampai pingsan atau gagal ujian dulu baru boleh cerita."
            miyuki "Tapi kalau ternyata waktu diperiksa aku cuma dibilang kurang istirahat biasa, nggak kelihatan manja banget ya, Chiasa-chan?"
            chiasa "Sama sekali nggak manja, Senpai. Kalau sudah sampai sering kebangun jam tiga pagi dengan dada sesak dan pengin menangis sendirian di dapur, itu jelas bukan cuma gara-gara kebanyakan minum kopi. Senpai sudah terlalu lama menahan semuanya sendirian."
            nar "Miyuki terdiam menatapmu selama beberapa detik. Jari-jarinya yang tadi meremas pinggiran buku perlahan mengendur, lalu ia menarik kartu kontak Sato Kyoko itu keluar sepenuhnya dari sela halaman."
            miyuki "...Iya ya. Dari kemarin di kepalaku tuh selalu ada suara yang bilang aku nggak boleh mengeluh soalnya orang lain juga capek. Ternyata dengar kamu bilang aku boleh datang ke sana rasanya bikin dadaku lega banget."
            chiasa "Sena-san pasti kasih kartu itu karena dia juga melihat Senpai sudah terlalu memaksa diri. Simpan nomornya di ponsel sekarang aja, Senpai, biar nanti nggak ragu lagi."
            nar "Miyuki mengangguk patuh. Ia mengeluarkan ponsel dari tasnya, mengetik deretan nomor telepon Sato Kyoko ke dalam daftar kontak, lalu menyelipkan kartu nama itu ke slot depan dompetnya."
            miyuki "Sudah kusimpan. Besok pagi jam kerja aku coba telepon buat bikin janji minggu ini. Eh, Chiasa-chan... kalau nanti habis keluar dari sesi pertamaku di sana aku masih agak gugup, boleh aku kirim pesan ke kamu nggak? Kamu nggak perlu bingung mau kasih saran apa kok, aku cuma pengin mengabari aja."
            chiasa "Boleh banget, Senpai. Kirim aja pesan kapan pun Senpai mau, pasti kubalas. Kalau mau mampir minum teh hangat habis dari sana juga bilang aja."
            miyuki "Hehe, teh hangat buatan kafe dekat stasiun ya? Aku pegang janjinya."
            chiasa "Siap, aku nggak bakal lupa."
            miyuki "Terima kasih banyak ya, Chiasa-chan. Ayo kita jalan ke depan, anginnya sudah mulai dingin."
        else:
            yutaka "Datang aja temui konselor itu, Tachibana-senpai. Nggak ada aturan harus menunggu sampai tumbang dulu baru boleh minta bantuan."
            miyuki "Tapi aku takut kelihatan manja kalau datang ke sana cuma gara-gara capek kuliah, Yutaka-kun..."
            yutaka "Nggak ada yang manja dari itu, Senpai. Kalau sudah sampai sering kebangun tengah malam dengan dada sesak terus pengin nangis sendiri di apartemen, itu jelas bukan sekadar efek kopi. Senpai aja yang selama ini terlalu keras memaksa diri sendiri."
            nar "Miyuki menatap wajahmu beberapa detik tanpa berkedip, lalu mengembuskan napas panjang. Ia menarik kartu nama Sato Kyoko itu keluar sepenuhnya dari sela buku catatannya."
            miyuki "...Jujur aja, dari kemarin aku takut kalau aku mengaku capek, orang-orang bakal kecewa sama aku. Tapi dengar kamu ngomong tegas begitu barusan, rasanya beban di kepalaku turun setengah."
            yutaka "Sena-san pasti ngasih kartu itu karena lihat Senpai sudah kelewat lelah. Masukin nomornya ke ponsel sekarang aja, Senpai, mumpung lagi ingat."
            nar "Miyuki mengangguk, mengeluarkan ponselnya dari saku jas, lalu mengetik nomor telepon Sato Kyoko ke daftar kontaknya dan menyimpan kartu fisik itu dengan rapi ke dalam dompet."
            miyuki "Sudah masuk kontaknya. Besok pagi waktu jam istirahat aku telepon buat atur jadwal konsultasi. Ngomong-ngomong, Yutaka-kun... kalau nanti sehabis dari tempat Sato-san aku masih merasa agak canggung, boleh aku kirim pesan singkat ke kamu? Nggak usah kasih solusi apa-apa kok, aku cuma pengin ada yang tahu aja."
            yutaka "Kirim aja kapan pun, Senpai. Pasti kubaca dan kubalas, atau kalau mau cari kopi hangat habis dari sana juga boleh."
            miyuki "Kopi hangat tanpa harus membahas jadwal praktik rumah sakit ya? Kedengarannya menyenangkan sekali."
            yutaka "Tentu, kita bahas hal lain aja."
            miyuki "Makasih banyak ya, Yutaka-kun. Rasanya malam ini aku bisa tidur lebih tenang."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Menurutku Tachibana-senpai cuma lagi kecapekan biasa gara-gara jadwal kuliah sama praktik yang menumpuk aja kok. Kalau akhir pekan ini Senpai kurangi minum kopi malam terus tidur yang cukup di apartemen, pasti minggu depan sudah segar lagi. Nggak perlu sampai repot datang ke konselor segala."
            nar "Miyuki mengerjap sesaat, lalu langsung tersenyum lega. Senyum itu muncul begitu cepat, seperti seseorang yang memang sedang mencari alasan untuk tidak perlu membuka hal yang membuatnya takut."
            miyuki "Iya kan, Chiasa-chan? Kamu juga mikirnya begitu ya? Sena aja kemarin yang terlalu cemas waktu lihat aku ketiduran di meja perpustakaan."
            chiasa "Iya, Senpai. Semua mahasiswa kalau lagi dekat jadwal ujian kan memang suka kurang tidur."
            miyuki "Benar banget. Aku cuma kurang disiplin mengatur jam istirahat aja dua minggu terakhir ini. Kalau jam tidurku sudah balik normal, sesak sama pusingnya juga pasti hilang sendiri."
            nar "Dengan gerakan cepat dan rapi, Miyuki mendorong kembali kartu nama Sato Kyoko itu jauh ke lipatan halaman paling belakang buku catatannya, lalu menutup sampul bukunya rapat-rapat."
            miyuki "Malam ini sampai apartemen Senpai mau langsung seduh teh chamomile terus tidur lebih awal deh. Terima kasih ya sudah dengerin keluhan recehku barusan, Chiasa-chan."
            chiasa "Istirahat yang cukup ya, Senpai."
            nar "Kamu ikut bangkit berjalan ke arah lobi depan, sementara kartu nama putih gading itu kini tersembunyi jauh di bagian belakang bukunya."
        else:
            yutaka "Menurutku Senpai cuma lagi kecapekan biasa gara-gara jadwal praktik yang padat aja kok. Kalau akhir pekan ini Senpai berhenti minum kopi malam terus tidur panjang di apartemen, minggu depan juga pasti segar lagi. Nggak perlu sampai repot ke konselor segala."
            nar "Miyuki mengerjap sesaat, lalu langsung menyambut ucapanmu dengan senyum lega yang terasa sedikit terlalu cepat untuk keraguan yang sudah ia simpan selama tiga hari."
            miyuki "Iya kan, Yutaka-kun? Aku juga mikirnya persis begitu dari kemarin. Sena aja yang kadang suka terlalu khawatir lihat aku belajar sampai malam."
            yutaka "Namanya juga mahasiswa tahun ketiga, wajar kalau lagi sibuk-sibuknya."
            miyuki "Betul. Aku cuma perlu merapikan lagi jadwal tidur sama makan malamku di apartemen. Kalau badanku sudah cukup istirahat, perasaan nggak enaknya pasti hilang sendiri."
            nar "Miyuki segera menyelipkan kembali kartu nama Sato Kyoko itu jauh ke bagian paling belakang buku catatannya, lalu menutup bukunya dan memasukkannya ke dalam tas."
            miyuki "Ya sudah, malam ini Senpai coba tidur sebelum jam sebelas deh. Makasih ya sudah menenangkan aku, Yutaka-kun."
            yutaka "Sama-sama, jangan lupa makan malam juga ya, Senpai."
            nar "Kalian beranjak meninggalkan taman dalam menuju pintu lobi utama, dengan kartu kontak itu tersimpan rapat di dasar buku tanpa sempat dicatat nomornya."
    else:
        if kk_host == "chiasa":
            chiasa "Ngomong-ngomong soal jadwal minggu depan, hari Senin nanti praktik observasi Senpai di rumah sakit mulai jam berapa? Masih satu kelompok sama Sena-san?"
            nar "Miyuki terdiam sepersekian detik melihatmu langsung mengalihkan pembicaraan dari kartu nama di tangannya. Tanpa berkata apa-apa lagi soal konselor itu, ia mendorong kartu tersebut masuk kembali ke sela buku dan memasang senyum seniornya yang tenang."
            miyuki "Oh, jadwal minggu depan ya? Masih jam delapan pagi kok di bangsal penyakit dalam, masih satu tim juga sama Sena. Hari Kamis sama Jumatnya kami ada pengumpulan laporan studi kasus."
            chiasa "Padat banget ya dari pagi sampai sore setiap hari."
            miyuki "Lumayan padat, tapi anak tahun ketiga memang sudah biasa begitu kok. Yang penting catatannya nggak ditunda sampai malam terakhir."
            nar "Ia menutup buku catatannya, merapikan tali tas ke bahunya, lalu bangkit berdiri dari bangku taman. Ketika kalian berjalan beriringan menuju pintu lobi depan untuk berpisah, justru Miyuki yang kembali menanyakan kabarmu dengan nada lembut seperti biasa."
            miyuki "Chiasa-chan sendiri nanti malam di rumah sudah ada makanan belum? Jangan telat makan malam ya, udara malam ini sudah mulai dingin soalnya."
            chiasa "Sudah ada bahan masakan di rumah kok, Senpai. Hati-hati di jalan pulang ya."
            miyuki "Iya, sampai ketemu lagi di kampus ya, Chiasa-chan."
            nar "Ia melambai sopan sebelum berbelok menuju arah stasiun, membawa kembali seluruh kelelahannya sendirian di balik senyum rapi yang tidak pernah retak."
        else:
            yutaka "Ngomong-ngomong soal jadwal rumah sakit, minggu depan giliran jaga praktik Senpai mulai jam berapa? Masih bareng kelompoknya Sena-san?"
            nar "Miyuki tertegun sejenak menyadari kamu sama sekali tidak menanggapi soal kartu nama di tangannya. Ia segera menyelipkan kembali kartu itu ke dalam sela halaman buku dan memasang senyum seniornya yang rapi seperti sediakala."
            miyuki "Oh, jadwal minggu depan ya? Masih masuk jam delapan pagi di bangsal observasi kok, masih bareng Sena juga. Hari Jumatnya kami harus mengumpulkan laporan evaluasi kasus ke dokter pembimbing."
            yutaka "Sibuk terus ya dari Senin sampai Jumat."
            miyuki "Iya, sudah rutinitas tahun ketiga kok. Selama semua berkasnya dirapikan lebih awal, masih bisa diatasi."
            nar "Ia memasukkan bukunya kembali ke dalam tas lalu bangkit berdiri dari bangku kayu. Saat kalian berjalan menuju pintu keluar lobi rumah sakit, justru Miyuki yang lebih dulu menoleh menanyakan keadaanmu dengan nada ramah."
            miyuki "Kamu sendiri sudah makan malam belum, Yutaka-kun? Jangan cuma beli makanan instan terus di apartemen ya, angin malam sudah mulai dingin soalnya."
            yutaka "Nanti aku mampir cari makan hangat dekat stasiun kok, Senpai. Hati-hati di jalan pulang."
            miyuki "Iya, duluan ya, Yutaka-kun."
            nar "Ia melambai tenang sebelum melangkah keluar dari pintu kaca lobi, kembali memikul seluruh kelelahannya sendiri di balik perhatian hangatnya kepada orang lain."
    return

# ┌─ PANDUAN CERITA · Mi10 · Omikuji Miyuki
# │ LOKASI  : Alam & Pantai · Kuil
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : ramalan "kesendirian".
# │ INTI    : A hibur / B tertawa / C ambil kesempatan.
# │ AKHIRAN : kerentanan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi10:
    call kk_scene_enter("miyuki", "Kuil · Tahun Baru")
    if kk_host == "chiasa":
        nar "Cahaya matahari awal Januari menembus sela dedaunan pohon cedar di halaman kuil, tetapi hembusan anginnya tetap dingin. Kamu dan Miyuki datang bersama beberapa kenalan kampus yang kini sudah berjalan agak jauh di depan menuju deretan kedai jajanan dekat gerbang utama."
        nar "Tadi di depan kotak omikuji, saat salah satu teman menanyakan isi ramalannya, Miyuki tersenyum tenang dan hanya membacakan bagian studi serta kesehatan yang cukup baik. Ia tidak langsung melipat kertas itu, melainkan memegangnya rapat-rapat hingga langkah kalian berdua tertinggal di dekat bangku kayu panjang di pinggir jalan setapak."
        chiasa "Tachibana-senpai dari tadi masih megangin kertas omikujinya terus. Ada bagian yang bikin Senpai kepikiran ya?"
        nar "Miyuki berhenti melangkah di samping bangku kayu, menoleh memastikan rombongan di depan sudah cukup jauh untuk tidak mendengar, lalu memperlihatkan satu baris di bagian bawah kertas kepadamu."
        miyuki "'Waspadai kesendirian yang kau tutup dengan kesibukan.' Kata yang mereka pakai di sini... kesendirian, Chiasa-chan."
        nar "Ia tertawa pendek sambil merapikan anak rambut hitamnya yang tertiup angin. Matanya terlihat lelah."
        miyuki "Lucu ya. Padahal jadwalku dari Senin sampai Minggu penuh orang terus. Di ruang kuliah ada teman seangkatan, di rumah sakit ada dokter dan perawat, di grup pesan juga selalu ada yang mengajak ngobrol atau minta tolong."
        chiasa "Tapi di kertas itu tetap kena ya, Senpai?"
        miyuki "Entahlah... mungkin gara-gara memang ada beberapa malam di apartemen ketika aku sudah selesai mandi, sudah beresin catatan, lalu megang ponsel lumayan lama tapi bingung harus telepon siapa. Rasanya aneh kalau menelepon orang tanpa lebih dulu menyiapkan alasan penting atau menanyakan kabar mereka duluan."
        nar "Miyuki menatap layar ponsel di tangan kirinya sebentar sebelum kembali melirikmu dengan senyum tipis."
    else:
        nar "Cahaya matahari awal Januari jatuh menembus sela pepohonan cedar di halaman kuil, tetapi hembusan anginnya tetap terasa tajam. Kamu dan Miyuki datang bersama beberapa kenalan kampus yang kini sudah berjalan cukup jauh di depan menuju deretan kedai jajanan dekat gerbang utama."
        nar "Tadi di depan kotak omikuji, ketika salah satu teman menanyakan isinya, Miyuki hanya tersenyum tenang dan membacakan bagian studi serta kesehatan yang cukup baik. Ia tidak langsung melipat kertas putih itu, melainkan memegangnya hingga langkah kalian berdua tertinggal di samping bangku kayu pinggir jalan setapak."
        yutaka "Dari tadi kertas omikujinya belum juga dilipat, Tachibana-senpai. Ada baris yang bikin kepikiran?"
        nar "Miyuki berhenti di dekat bangku kayu, melirik sebentar memastikan rombongan di depan terlalu jauh untuk mendengar, lalu menunjukkan satu baris di bagian bawah kertas kepadamu."
        miyuki "'Waspadai kesendirian yang kau tutup dengan kesibukan.' Kata yang mereka pakai di sini... kesendirian, Yutaka-kun."
        nar "Ia tertawa pelan sambil merapikan rambut hitam panjangnya yang ditiup angin, tetapi sorot matanya tampak letih."
        miyuki "Agak lucu ya. Padahal jadwalku penuh orang setiap hari. Di kampus ada kelas, di rumah sakit ada dokter dan perawat, di ponsel juga selalu ada pesan yang masuk."
        yutaka "Tapi kalimat itu tetap terasa kena?"
        miyuki "Entahlah... mungkin karena memang ada beberapa malam di apartemen ketika aku sudah selesai belajar, lalu memegangi ponsel cukup lama tapi bingung harus menelepon siapa. Rasanya aneh kalau menghubungi orang tanpa lebih dulu menyiapkan alasan penting."
        nar "Ucapan tentang apartemen yang terlalu sunyi itu terdengar begitu familier di telingamu. Miyuki memandang layar ponsel di tangan kirinya sebentar sebelum menoleh kembali padamu dengan senyum tipis."
    call kk_family_menu("Mi10", ["\"Duduk sebentar dulu di sini yuk, Senpai. Biar rombongan jalan duluan aja.\"", "\"Haha, ramalan kayak gitu cuma kebetulan aja kok. Semua orang juga pernah merasa sepi.\"", "\"Orang lain nggak bakal paham capeknya Senpai. Kalau butuh seseorang, cari aku saja.\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Duduk sebentar dulu di bangku sini yuk, Tachibana-senpai. Biar yang lain jalan duluan ke kedai jajanan, nanti kita tinggal nyusul pelan-pelan."
            nar "Miyuki sempat melirik ke arah punggung rombongan yang makin jauh dengan refleks seorang senior yang tidak ingin membuat orang lain menunggu."
            miyuki "Eh, nggak enak lho, Chiasa-chan, nanti mereka nyariin kita di bawah. Aku nggak apa-apa kok, ayo jalan lagi aja."
            chiasa "Lima menit aja, Senpai. Kakiku juga lumayan pegal habis antre lama di tangga atas tadi. Lagian nggak harus buru-buru kan?"
            nar "Mendengar alasan santaimu, Miyuki akhirnya mengalah. Ia mengeluarkan ponselnya, mengetik satu pesan singkat ke grup bahwa kalian berdua mampir beristirahat sebentar dan akan menyusul nanti, lalu ikut duduk di bangku kayu di sebelahmu."
            miyuki "Makasih ya, Chiasa-chan. Eh... tapi aku beneran nggak punya bahan obrolan yang seru atau lucu sekarang."
            chiasa "Memangnya harus selalu punya cerita seru dulu baru boleh duduk bareng, Senpai?"
            nar "Miyuki menatapmu sejenak. Nada suaranya yang tadi terdengar seperti bercanda pelan-pelan menjadi sungguh-sungguh."
            miyuki "Aku nggak perlu nyiapin cerita yang bikin orang lain senang dulu supaya boleh ditemani sebentar?"
            chiasa "Nggak perlu lah, Senpai. Duduk diam sambil minum hangat juga nggak ada salahnya."
            nar "Bibir Miyuki melengkung lembut. Tanpa membaca ulang tulisan di dalamnya, ia melipat kertas omikuji itu rapi-rapi, memasukkannya ke dalam tas selempangnya, lalu menyandarkan punggung ke sandaran bangku sambil menghirup udara dingin dengan tenang."
        else:
            yutaka "Duduk sebentar dulu di bangku sini yuk, Tachibana-senpai. Biar rombongan jalan duluan ke kedai jajanan, nanti kita tinggal nyusul."
            nar "Miyuki langsung melirik ke arah punggung teman-teman di depan dengan kebiasaan seorang senior yang tidak enak membuat orang lain menunggu."
            miyuki "Eh, nggak enak dong, Yutaka-kun, nanti mereka menunggu kita di bawah. Aku nggak apa-apa kok, ayo jalan lagi."
            yutaka "Lima menit doang, Senpai. Kakiku sendiri lumayan pegal habis antre lama di tangga atas tadi. Nggak harus selalu buru-buru kan?"
            nar "Mendengar alasan santaimu, Miyuki akhirnya berhenti menolak. Ia membuka ponselnya, mengirim pesan singkat ke grup bahwa kalian berdua akan menyusul sebentar lagi, lalu duduk di bangku kayu di sampingmu."
            miyuki "Terima kasih ya, Yutaka-kun. Tapi maaf, hari ini aku lagi nggak punya cerita seru atau topik lucu buat dibahas."
            yutaka "Memangnya harus punya topik seru dulu baru boleh duduk bareng, Senpai?"
            nar "Miyuki menoleh menatapmu. Nada kalimatnya terdengar seperti gurauan ringan, tetapi sorot matanya menunggu jawabanmu dengan sungguh-sungguh."
            miyuki "Jadi aku nggak perlu nyiapin cerita yang menyenangkan dulu supaya boleh ditemani sebentar?"
            yutaka "Nggak perlu. Duduk diam sebentar sambil kena angin juga nggak masalah."
            nar "Senyum lega yang lembut muncul di wajah Miyuki. Tanpa membaca ulang baris tulisannya, ia melipat kertas omikuji itu rapi dan memasukkannya ke dalam tas, lalu menyandarkan punggungnya dengan tenang di bangku kayu."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kamu tertawa ringan dan mengibaskan tangan sambil melangkah pelan di sampingnya."
            chiasa "Haha, ramalan omikuji kayak gitu cuma kebetulan aja kok, Tachibana-senpai. Semua orang kan pasti pernah ada malam-malam di mana mereka merasa sepi atau bingung mau ngehubungin siapa. Penulis kertasnya memang pintar bikin kalimat yang kerasa pas."
            nar "Miyuki terdiam sejenak, lalu senyum ramah khas senior yang biasa ia tunjukkan di depan banyak orang kembali terpasang rapi di wajahnya."
            miyuki "Ahaha... iya juga ya, Chiasa-chan. Masa gara-gara selembar kertas ramalan begitu aja Senpai langsung terbawa suasana terus curhat aneh-aneh begini. Malu-maluin banget."
            chiasa "Nggak apa-apa kok, Senpai, wajar lah awal tahun begini."
            miyuki "Ya sudah, ayo kita jalan agak cepat biar nggak ketinggalan sama rombongan di depan. Nanti mereka bingung nyariin kita di kedai jajanan."
            nar "Miyuki melangkah setengah langkah lebih dulu darimu menuruni jalan setapak menuju gerbang. Dari samping, pembawaannya sudah kembali tenang dan teratur seperti biasa, hanya saja jemarinya di samping mantel terus-menerus melipat kertas omikuji itu lagi dan lagi sampai bentuknya menjadi potongan persegi yang sangat kecil."
        else:
            nar "Kamu tertawa santai sambil melangkah pelan di sampingnya."
            yutaka "Haha, ramalan umum begitu cuma kebetulan aja kali, Tachibana-senpai. Semua orang kan pasti pernah ada malam-malam di mana mereka merasa sepi. Penulis kertasnya memang jago bikin kalimat yang gampang kerasa pas."
            nar "Miyuki terdiam sebentar, lalu senyum sopan khas senior yang biasa ia kenakan di kampus segera kembali terpasang rapi di wajahnya."
            miyuki "Ahaha... benar juga ya, Yutaka-kun. Senpai terlalu gampang terbawa suasana cuma gara-gara selembar kertas omikuji. Jadi agak malu sendiri."
            yutaka "Santai aja, Senpai, nggak usah dipikirin."
            miyuki "Ya sudah, ayo kita jalan lebih cepat supaya bisa nyusul yang lain di depan. Nanti mereka nyariin."
            nar "Miyuki berjalan sedikit mendahuluimu menuruni jalan setapak kuil. Dari samping, sikapnya terlihat kembali tenang dan rapi seperti biasanya, hanya saja jari-jarinya terus melipat kertas omikuji itu berulang kali hingga ukurannya menyusut makin kecil."
    else:
        if kk_host == "chiasa":
            nar "Kamu melangkah lebih dekat ke hadapan Miyuki, merendahkan suaramu agar terdengar begitu pasti di tengah angin kuil yang dingin."
            chiasa "Orang-orang di kampus atau di rumah sakit itu cuma mau lihat Tachibana-senpai yang selalu rapi dan bisa diandalkan. Mereka nggak bakal benar-benar paham seberapa capeknya Senpai sebenarnya."
            nar "Mata biru safir Miyuki menatapmu lekat-lekat, agak terkejut oleh ketajaman kalimatmu."
            chiasa "Jadi kalau suatu malam di apartemen Senpai merasa sepi lagi dan bingung mau telepon siapa, nggak usah mikir dua kali, cari dan telepon aku saja. Aku satu-satunya yang tahu sisi capeknya Senpai, jadi sama aku Senpai nggak perlu nyiapin alasan apa-apa."
            nar "Kamu mengucapkan janji sebesar itu dengan suara lembut dan mantap, menyadari betul betapa mudahnya seseorang yang sedang letih berpegang pada satu tempat yang menawarkan kepastian mutlak. Miyuki tidak menanyakan apa pun yang ada di balik tawaranmu; jari-jarinya yang dingin justru perlahan mengendur dari kertas omikuji itu."
            miyuki "...Kalau nanti suatu malam aku beneran meneleponmu tanpa alasan penting, cuma karena nggak sanggup diam sendirian di kamar... kamu beneran nggak keberatan, Chiasa-chan?"
            chiasa "Nggak bakal keberatan, Senpai. Kapan pun Senpai butuh, langsung hubungi aku saja."
            nar "Kamu membiarkan ia menaruh harapan jauh lebih besar daripada yang sungguh-sungguh berniat kamu penuhi tanpa syarat. Miyuki menarik napas panjang, lalu tersenyum lega menatapmu, seolah rasa tenangnya malam-malam mendatang baru saja ia titipkan sepenuhnya di tanganmu."
        else:
            nar "Kamu melangkah maju setengah tapak mendekati Miyuki lalu menurunkan suaramu pelan."
            yutaka "Orang-orang di kampus atau di rumah sakit itu cuma mau lihat Tachibana-senpai yang selalu kuat dan tersenyum rapi. Mereka nggak bakal benar-benar paham seberapa capeknya Senpai."
            nar "Miyuki menatapmu lekat-lekat, agak terkejut mendengar kalimatmu yang begitu langsung menyentuh titik lelahnya."
            yutaka "Jadi kalau suatu malam di apartemen kamu merasa sepi lagi dan bingung mau telepon siapa, nggak usah mikir panjang, hubungi aku saja. Sama aku, kamu nggak perlu repot nyiapin alasan apa-apa."
            nar "Kamu menawarkan kepastian itu dengan suara yang terdengar meyakinkan, tahu persis bahwa seseorang yang sedang selelah ini tidak akan sempat memeriksa harga di balik perhatian yang begitu mudah diberikan. Jemari Miyuki yang dingin perlahan melonggar dari pinggiran kertas ramalan."
            miyuki "...Kalau nanti aku benar-benar meneleponmu malam-malam tanpa alasan penting, cuma karena nggak kuat sendirian di apartemen... kamu sungguh nggak keberatan, Yutaka-kun?"
            yutaka "Nggak bakal keberatan, Senpai. Kapan pun kamu butuh, langsung telepon aku saja."
            nar "Kamu membiarkannya berharap jauh lebih banyak daripada yang sungguh-sungguh ingin kamu tanggung tanpa pamrih. Ketika Miyuki akhirnya tersenyum lega menatapmu, rasa tenangnya sudah mulai tertambat erat pada persetujuanmu."
    return

init 1 python:
    def kk_miyuki_hurt_self(delta):
        pts.setdefault("luka_miyuki_diri",15)
        kk_adj("luka_miyuki_diri",delta)

    _hook("Mi04-A", lambda: kk_rel("miyuki","intim",4))
    _hook("Mi04-C", lambda: kk_rel("miyuki","intim",2))
    _hook("Mi08-A", lambda: (kk_flag("miyuki_sato_dikenal"), kk_miyuki_hurt_self(-5)))
    _hook("Mi08-B", lambda: kk_rel("miyuki","trust",-3))
    _hook("Mi10-A", lambda: kk_rel("miyuki","trust",5))
    _hook("Mi10-C", lambda: (kk_miyuki_hurt_self(8), kk_flag("miyuki_disandari")))
