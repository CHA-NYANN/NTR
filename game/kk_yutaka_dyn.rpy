# Event dinamis Yutaka host (Y-D01/02/04/05/06/07/09) + Yutaka-NPC pada rute Chiasa
# (Y-D10/Y-D11). Konsekuensi + karakter; intel/identitas/keluarga.

# ┌─ PANDUAN CERITA · Y-D01 · Notifikasi Saldo
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kisaragi Yutaka
# │ AWALAN  : tanggal uang saku
# │ INTI    : A Belanja / B simpan / C beri pada seseorang
# │ AKHIRAN : arah pemakaian uang
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y_D01:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Notifikasi saldo")
    play sound "audio/sfx/phone_buzz.wav"
    nar "Tanggal dua puluh lima. Ponselmu bergetar singkat menampilkan pemberitahuan otomatis dari aplikasi bank keluarga Kisaragi. Jumlah transfer bulanan yang masuk ke rekeningmu tampak sangat lapang dan datang tepat waktu tanpa meleset satu jam pun."
    nar "Orang tua Kisaragi bisa saja lupa menelepon berminggu-minggu, tetapi sistem transfer uang saku mereka tidak pernah terlambat. Tidak ada pesan tambahan ataupun petunjuk pemakaian yang menyertainya. Untuk kebutuhan apa pun bulan ini, kamu tidak perlu meminta izin siapa-siapa."
    play sound "audio/sfx/phone_buzz.wav"
    nar "Tepat ketika kamu masih memandangi deretan angka di layar, pesan singkat dari Koita masuk di jendela obrolan."
    "Pesan Koita" "Yutaka, nanti habis kuliah mau cari makan murah di kantin belakang nggak? Bulan ini aku habis beli buku referensi dua jilid, jadi dompetku agak menjerit nih, haha."
    yutaka "Wah, ketahuan banget baru habis belanja buku tebal ya. Nanti kukabari kalau jadwalku cocok, Koita."
    nar "Kamu menutup jendela pesan sambil membayangkan orang-orang di sekitarmu yang selalu menghitung receh di depan mesin tiket dan membandingkan harga makan siang. Kelonggaran hidup milik Yutaka terasa nyaman sekaligus sedikit hampa, seolah semua jawaban materi diberikan jauh sebelum ada yang sempat mendengar pertanyaanmu."
    call kk_family_menu("Y-D01", ["Belanja untuk dirimu.", "Simpan sebagian besar.", "Beri pada seseorang yang membutuhkan."])
    if _return == "A":
        nar "Kamu memutuskan menggunakan kelonggaran itu untuk berkeliling sebentar di distrik belanja elite dekat apartemen. Di sebuah toko perlengkapan rumah dan pakaian, matamu tertuju pada mantel hangat berpotongan rapi serta cangkir keramik yang sejak minggu lalu sempat kamu lirik."
        "Pegawai Toko" "Pilihan yang sangat bagus, Tuan. Bahannya ringan sekali untuk dipakai berangkat kuliah dan tahan angin. Apakah ingin langsung dicoba?"
        yutaka "Boleh, aku ambil yang warna abu gelap ini sama satu set cangkir di rak depan tadi ya."
        "Pegawai Toko" "Baik, akan segera kami bungkus rapi."
        nar "Saat membayar di kasir, kamu sempat menikmati sensasi betapa sedikit harga membatasi keinginanmu hari ini. Begitu kamu membawa kantong belanja itu pulang dan meletakkannya di kursi, apartemen luas itu ternyata masih sama sunyinya. Kenyamanan materi ini memang nyata, hanya saja tidak sanggup mengisi hal-hal sepi yang diam-diam kamu harapkan darinya."
    elif _return == "B":
        nar "Kamu membuka menu pemindahan dana di aplikasi bank, menyisihkan sebagian besar uang kiriman itu ke kantong tabungan terpisah, dan hanya menyisakan anggaran harian yang secukupnya di saldo utama."
        yutaka "{i}Uang segini lebih aman disimpan dulu. Masa depanku di tubuh ini belum jelas bakal berhenti di mana, jadi paling nggak pegangan darurat harus aman.{/i}"
        nar "Kamu mengetik balasan lagi ke Koita."
        yutaka "Eh, aku jadi ikut makan di kantin murah aja ya hari ini. Lagi mau latihan hemat bareng kamu."
        play sound "audio/sfx/phone_buzz.wav"
        "Pesan Koita" "Serius nih seorang Kisaragi mau ikutan hemat? Oke deh, nanti kupesankan meja paling pojok!"
        nar "Kamu mengunci layar ponsel setelah mengecek angka tabungan sekali lagi. Menyimpan uang memberi rasa aman yang bisa dihitung jelas di tengah begitu banyak hal di kampus ini yang masih samar arahnya."
    else:
        nar "Kamu teringat seorang rekan kerja paruh waktu tingkat bawah di kafe yang kemarin mengeluh pelan karena biaya buku praktik dan tagihan listrik bulanannya bentrok di minggu yang sama. Kamu mampir menemuinya sebentar sebelum jam kuliah berikutnya dengan amplop kecil berisi bantuan biaya buku."
        "Rekan Kafe" "Eh, Kisaragi-san? Ini serius buat bantu beli buku praktikku? Nggak usah deh, aku pasti lama banget baru sanggup bayar cicilannya balik..."
        yutaka "Tenang aja, ini nggak usah dianggap utang kok. Kebetulan uang bulananku bulan ini masih longgar banget, daripada nganggur lebih berguna buat buku kuliahmu."
        "Rekan Kafe" "Tapi kan nggak enak, Kisaragi-san... aku nggak punya apa-apa buat balas kebaikan sebanyak ini."
        yutaka "Kamu nggak perlu balas apa-apa, serius. Mau kamu terima atau nggak itu terserah kamu sepenuhnya, aku nggak bakal ungkit-ungkit lagi setelah hari ini."
        "Rekan Kafe" "...Terima kasih banyak, Kisaragi-san. Beneran nolong banget bulan ini."
        nar "Kamu mengangguk ringan dan pamit duluan. Uang itu bisa meringankan beban seseorang hari ini, dan kamu sengaja menjaga jarak agar rasa terima kasihnya tidak pernah berubah menjadi rasa berutang budi kepadamu."
    return

# ┌─ PANDUAN CERITA · Y-D02 · Teman Game yang Heran
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kisaragi Yutaka
# │ AWALAN  : Male Route
# │ INTI    : A teman online Yutaka asli: "kok mainmu beda?" Jujur sebagian / B beri alasan / C berhenti main
# │ AKHIRAN : curiga_identitas menyebar lewat dunia online
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y_D02:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Teman game")
    nar "Di antara suara permainan, teman lama Yutaka menanyakan mengapa kau berhenti mengambil keputusan yang dulu paling cepat kaulakukan. Ia mengulang satu candaan yang tidak kaupahami. Kau tertawa terlambat, dan hening di headset membuat kesalahan kecil itu terdengar jelas."
    "Hayase" "Mainmu beda sekali. Biasanya kau yang bilang aku harus tenang, sekarang kau seperti takut menyentuh tombol. Ini bukan soal menang. Kamu baik-baik saja?"
    call kk_family_menu("Y-D02", ["Jujur sebagian.", "Beri alasan masuk akal.", "Berhenti main bersamanya."])
    if _return == "A":
        nar "Kau mengakui ada banyak hal yang tidak bisa kaulakukan seperti dahulu. Temanmu menurunkan suara dan bertanya sejak kapan. Kau tidak membuka seluruh kebenaran, tetapi percakapan kini telah melewati alasan permainan. Di dunia yang hanya mengenal suaramu itu, seseorang mulai merasa kehilangan orang yang ia kenal."
    elif _return == "B":
        "Hayase" "Banyak pikiran, ya? Baik. Kita main santai saja. Kalau tidak mau main pun bilang; aku bisa tetap mengobrol tanpa menyuruhmu membuktikan skor lama."
    else:
        nar "Kau keluar dari permainan dan berhenti mengatur waktu bersama. Pesannya yang berikut masih ramah, lalu semakin jarang. Kau berhasil menghindari pertanyaan, dengan harga kehilangan seseorang yang mungkin bersedia mengenalmu lagi jika kau sanggup bertahan dalam percakapan itu."
    return

# ┌─ PANDUAN CERITA · Y-D04 · Kaichi Menginap
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kisaragi Yutaka
# │ AWALAN  : kenal Kaichi
# │ INTI    : A Jelaskan / B sembunyikan / C sogok
# │ AKHIRAN : daichi_tahu +
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y_D04:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Kaichi menginap")
    nar "Kaichi datang menginap dengan makanan dan cerita kampus, lalu menemukan catatan tentang orang-orang dekatmu di meja. Ia berhenti bercanda ketika melihat nama, waktu pertemuan, dan hal pribadi yang tampak seperti sedang dinilai. Kau mendadak melihat catatanmu melalui mata seorang tamu."
    "Kaichi" "Kau mencatat mereka seperti tugas penelitian? Aku tidak tahu maksudmu, tapi beberapa hal ini sepertinya bukan untuk dibaca siapa saja. Kenapa ada di mejamu?"
    call kk_family_menu("Y-D04", ["Jelaskan apa adanya.", "Sembunyikan catatannya.", "Sogok ia agar diam."])
    if _return == "A":
        nar "Kau menjelaskan apa yang sedang kaucatat dan mengakui bahwa orang-orang itu tidak tahu. Kaichi mendengar tanpa langsung memihak. Ia bertanya apakah kau sanggup mengatakan hal yang sama di depan mereka. Pertanyaan itu tidak membuatnya tahu semuanya, tetapi membuat alasanmu sendiri terdengar kurang kokoh."
    elif _return == "B":
        "Kaichi" "Aku sudah lihat namanya. Menutup buku tidak membuatku lupa. Kita bisa berhenti bicara sekarang, tapi jangan minta aku menganggap tidak ada yang aneh."
    else:
        nar "Kau menawarkan uang agar Kaichi tidak membicarakannya. Ia menerimanya, dan percakapan kalian menjadi terlalu sopan untuk disebut persahabatan seperti tadi. Kau mendapatkan kebisuan malam ini. Ia mendapatkan alasan untuk menanyakan berapa banyak hal lain yang sedang kaubayar supaya tetap tidak dibicarakan."
    return

# ┌─ PANDUAN CERITA · Y-D05 · Jam dari Daisuke
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kisaragi Yutaka
# │ AWALAN  : M16
# │ INTI    : A "Masih ingat jam yang tahun lalu?" Jawab yakin / B akui lupa / C alihkan
# │ AKHIRAN : curiga_identitas[[daisuke] ±
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y_D05:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Jam dari Daisuke")
    nar "Daisuke melihat pergelanganmu sebelum menyebut jam lama. Nada suaranya ringan, tetapi kau merasakan jurang antara keakraban yang ia tawarkan dan ingatan yang tidak bisa kauambil kembali. Hadiah itu pernah berarti bagi seseorang; sekarang kau harus menjawab tanpa mengetahui seluruh alasannya."
    "Daisuke" "Jam yang kuberikan tahun lalu masih ada? Aku ingat kau langsung memakainya. Waktu itu aku senang sekali, sampai Yoshie bilang aku lebih heboh daripada orang yang menerima hadiah."
    call kk_family_menu("Y-D05", ["Jawab dengan yakin.", "Akui lupa.", "Alihkan pembicaraan."])
    if _return == "A":
        "Daisuke" "Ya, yang itu. Senang kau masih menyimpannya. Benda begitu kadang cuma berguna karena kita ingat siapa yang ada bersama kita waktu menerimanya."
    elif _return == "B":
        "Daisuke" "Kau tidak ingat? ...Tidak apa-apa kalau detailnya lupa. Tapi akhir-akhir ini kau kelihatan menanggung sesuatu. Ada hal yang perlu kutahu?"
    else:
        "Daisuke" "Kita boleh bicara soal perjalanan dulu. Tapi kalau kau sedang menghindari sesuatu, jangan merasa harus terus begitu di depanku. Aku tidak sedang mengujimu dengan jam."
    return

# ┌─ PANDUAN CERITA · Y-D06 · Lidah yang Lepas di Kafe Bar
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kisaragi Yutaka
# │ AWALAN  : Jumat malam saat kerja
# │ INTI    : A Dengarkan / B rekam / C antar pulang
# │ AKHIRAN : intel untuk rute Miyuki atau Shiori
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y_D06:
    call kk_scene_enter("yutaka", "Kafe bar · Jumat malam")
    nar "Jumat malam di kafe bar tempatmu bekerja paruh waktu selalu dipenuhi denting gelas dan obrolan pelan di bawah lampu temaram. Ketika kamu sedang mengelap meja kosong di dekat sudut konter, suara tawa berat yang terlalu nyaring membuat tanganmu seketika berhenti bergerak."
    nar "Di bangku sudut, Tojo sedang bersandar santai dengan gelas ketiganya yang hampir tandas. Wajahnya memerah oleh alkohol, dan lidahnya terasa makin lepas ketika ia mengangkat gelas ke arahmu begitu mengenali seragam kerjamu."
    "Tojo" "Hei, anak Kisaragi, kebetulan banget ketemu di sini! Tuangin air dingin dong satu. Sumpah deh, malam ini kepalaku lagi enak banget habis makan malam sama perwakilan keluarga Saionji kemarin."
    yutaka "Ini air dinginnya, Tojo-san. Kelihatannya sudah minum lumayan banyak dari tadi."
    "Tojo" "Halah, baru segini doang kok. Eh, kamu sekampus sama Saionji Shiori kan? Lucu banget deh cewek itu, sampai sekarang masih ngira dia bisa terus-terusan mengulur keputusan keluarga pakai alasan kuliah sama klub catur."
    nar "Suara santai pengunjung di meja lain membuat nada pongah Tojo terdengar jauh lebih menjijikkan. Ia berbicara tentang masa depan Shiori dengan keyakinan orang yang terbiasa menganggap pilihan perempuan lain hanyalah bagian kecil dari rencananya."
    "Tojo" "Padahal orang tuanya sudah sepakat soal arah kerja sama kami. Cepat atau lambat dia juga bakal paham mana yang paling masuk akal buat nama keluarganya... lho, kamu kenapa diam aja sambil ngelihatin aku gitu? Jangan pasang tampang kayak aku ini penjahat dong!"
    call kk_family_menu("Y-D06", ["Dengarkan baik-baik.", "Rekam diam-diam.", "Antar ia pulang."])
    if _return == "A":
        yutaka "Nggak ada maksud apa-apa kok, Tojo-san. Aku cuma kaget aja dengar pembicaraan keluarganya sudah sejauh itu. Memangnya pihak keluarga Saionji sendiri sudah mutusin semuanya tanpa nunggu jawaban Saionji-san?"
        "Tojo" "Haha, kalau soal itu kan tinggal cara ngatur jadwal pertemuannya aja! Begitu ayahku teken jadwal makan malam berikutnya, dia mau menghindar ke mana lagi? Di kalangan kita, penolakan anak kuliah itu paling cuma bertahan satu semester."
        yutaka "Begitu ya... kedengarannya Tojo-san yakin sekali semuanya bakal jalan sesuai rencana."
        "Tojo" "Ya jelas lah! Orang yang pegang kunci perjanjian kan bukan cuma dia sendiri."
        nar "Kamu terus mengangguk datar sambil membersihkan meja di sebelahnya, memisahkan baik-baik mana kalimat pasti yang keluar dari mulut Tojo dan mana yang sekadar bualan mabuk. Semua keterangan itu memberimu alasan kuat untuk memperingatkan Shiori tanpa mengambil alih haknya mengambil keputusan."
    elif _return == "B":
        nar "Kamu menaruh lap di atas nampan, lalu dengan satu gerakan tenang di balik meja konter kamu menyalakan aplikasi perekam suara di ponselmu dan meletakkannya telungkup tepat di tepi baki minuman."
        yutaka "Minum dulu air putihnya, Tojo-san. Jadi tadi maksudmu rencana keluarga soal Saionji-san itu sebenarnya sudah mulai diatur dari belakang meja?"
        "Tojo" "Bukan dari belakang meja lah, namanya strategi bisnis! Kalau nunggu Saionji Shiori setuju dari hatinya, bisa-bisa sampai lulus juga nggak kelar. Yang penting kesepakatan orang tua dikunci dulu, nanti dia tinggal ikut arus aja."
        yutaka "...Kamu beneran bicara begitu tentang orang yang rencananya mau kamu dekati?"
        "Tojo" "Jangan naif banget lah, Kisaragi. Kamu kan juga lahir di keluarga bisnis, harusnya paham gimana cara dunia ini muter."
        nar "Beberapa menit kemudian, setelah Tojo membayar tagihan dan keluar dengan langkah agak sempoyongan, kamu menghentikan rekaman dan memutarnya pelan di ruang belakang. Suara mabuknya tidak terdengar sedikit pun berkuasa, hanya dingin dan penuh rasa berhak. Kini kamu memegang bukti nyata yang mungkin perlu diketahui Shiori."
    else:
        yutaka "Tojo-san, kayaknya malam ini sudah cukup minumnya. Jam tutup bar juga sebentar lagi, biar kubantu panggil taksi sampai depan biar pulangnya aman."
        "Tojo" "Wah, perhatian amat kamu, Kisaragi! Boleh deh, kepalaku memang agak muter sedikit nih... pegangin lenganku sebentar dong sampai trotoar."
        nar "Kamu mengambilkan mantelnya, membantu menopang bahunya keluar dari kafe bar, lalu memastikan sopir taksi mencatat alamat rumah Tojo dengan benar sebelum menutup pintu."
        "Tojo" "Makasih banyak ya, Yutaka! Ternyata kamu anak yang enak diajak kerja sama. Lain kali kalau butuh koneksi bisnis atau apa, kabari aku aja!"
        yutaka "Hati-hati di jalan, Tojo-san."
        nar "Taksi meluncur menjauh di jalanan basah. Membantu orang mabuk pulang dengan aman tidak berarti kamu menyetujui satu pun kalimatnya tentang Shiori. Meski begitu, besok pagi ia pasti akan jauh lebih mudah mengingat kebaikanmu malam ini daripada ucapannya sendiri yang lepas kendali."
    return

# ┌─ PANDUAN CERITA · Y-D07 · Nagisa Main Sampai Pagi
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kisaragi Yutaka
# │ AWALAN  : Aff Nagisa Sedang
# │ INTI    : A Biarkan tidur di sofa / B antar pulang / C suruh pulang
# │ AKHIRAN : rumor; kelekatan Nagisa
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y_D07:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Nagisa main sampai pagi")
    nar "Cahaya biru pucat menjelang fajar mulai merembes di celah tirai ruang tengah ketika suara layar hasil akhir permainan berhenti berdengung. Dua kaleng teh dingin kosong dan sebungkus keripik yang hampir habis tergeletak di atas meja rendah."
    nar "Nagisa meletakkan pengendali gim ke atas karpet lalu menguap panjang tanpa sempat menutup mulutnya dengan tangan. Begitu sadar kamu melihatnya, ia cepat-cepat menegakkan punggung seolah ingin mengembalikan suasana jadi adu gengsi seperti tiga jam lalu."
    nagisa "Tadi... aku bilang 'satu ronde lagi' berapa kali sih? Jangan dijawab ya, aku nggak mau dengar hitungannya."
    yutaka "Kalau nggak salah mulai dari jam setengah dua sampai sekarang sudah hampir sembilan kali, Nagisa. Tapi tenang, aku nggak bakal bilang kamu kalah tipis tiga kali berturut-turut kok."
    nagisa "Heh! Itu gara-gara mataku sudah mulai buram, tahu! Bukan karena kamu mendadak jago!"
    nar "Ia mengusap matanya pelan, bahunya yang tegang perlahan melorot bersandar ke bantal sofa. Kamu menoleh ke jam dinding dan sadar malam sudah benar-benar lewat tanpa salah seorang dari kalian berniat menyudahi obrolan."
    nagisa "...Yutaka. Boleh nggak aku numpang tidur di sofa sini sebentar aja sampai matahari agak naik? Jujur aja, aku sudah terlalu ngantuk buat pura-pura masih sanggup jalan pulang sekarang."
    call kk_family_menu("Y-D07", ["Biarkan ia tidur di sofa.", "Antar ia pulang.", "Suruh ia pulang sendiri."])
    if _return == "A":
        yutaka "Ya sudah, tidur aja di sofa sini. Tunggu sebentar, kuambilkan selimut bersih sama bantal cadangan dari lemari."
        nagisa "Beneran nggak merepotkan? Aku janji begitu bangun langsung bereskan selimutnya terus pulang."
        yutaka "Nggak merepotkan sama sekali. Tasmu taruh di kursi dekat pintu aja, kabel pengisi daya ada di sebelah meja TV kalau mau kasih kabar dulu ke rumah."
        nagisa "Iya, kukabari Ibu sama Onii-chan dulu biar nggak panik nyariin... makasih ya, Yutaka. Selamat tidur."
        nar "Tidak sampai lima menit setelah mengirim pesan ke rumahnya, napas Nagisa sudah terdengar tenang di balik selimut. Paginya, ketika ia keluar dari pintu apartemenmu dengan rambut masih agak kusut, seorang kenalan kampus yang kebetulan melintas di koridor sempat melirik panjang."
        nar "Kamu tahu betul rasa percaya yang Nagisa tunjukkan dengan tertidur pulas di sofamu jauh lebih sederhana daripada cerita macam-macam yang mungkin segera dibangun orang lain dari pemandangan pagi itu."
    elif _return == "B":
        yutaka "Daripada tidur di sofa yang sempit nanti badanmu malah sakit semua, sini kuantar pulang sekarang aja mumpung jalanan masih sepi. Aku ambil jaket dulu ya."
        nagisa "Eh, kamu mau antar aku pulang jam segini? Serius nggak apa-apa? Nanti kamu sendiri kapan tidurnya?"
        yutaka "Rumahmu nggak jauh-jauh amat kok, sekalian cari udara pagi. Ayo, nanti keburu matamu benar-benar nutup di sini."
        nar "Kalian berjalan berdampingan menyusuri trotoar yang masih basah oleh embun pagi. Langkah Nagisa sedikit melambat karena kantuk, dan sesekali ia bersandar tipis ke tasnya sendiri sambil menahan senyum."
        nagisa "Makasih ya, Yutaka. Aku tahu ini merepotkan banget... dan awas ya, kalau sampai aku hampir ketiduran sambil jalan begini, jangan berani-berani kamu jadikan bahan lelucon satu semester!"
        yutaka "Janji nggak bakal kubocorkan ke siapa-siapa. Yang penting kamu sampai kasurmu sendiri dengan aman."
        nar "Di depan gerbang Rumah Sakurajima, Nagisa melambai kecil dengan mata setengah terpejam sebelum masuk, meninggalkan rasa hangat yang tenang sepanjang perjalananmu kembali ke apartemen."
    else:
        yutaka "Maaf, Nagisa, kayaknya lebih baik kamu pulang sekarang aja deh. Sudah hampir pagi begini, nggak enak sama keluargamu juga kalau sampai ketahuan menginap di tempat laki-laki."
        nar "Raut kantuk di wajah Nagisa seketika menegang. Ia langsung menarik tasnya ke pangkuan dan berdiri lebih cepat dari yang diperlukan."
        nagisa "Oh... iya, bener juga. Harusnya kamu bilang dari tadi kalau memang nggak nyaman aku kelamaan di sini."
        yutaka "Bukan nggak nyaman, aku cuma mikirin omongan orang nanti..."
        nagisa "Nggak usah ikut berdiri, aku tahu jalan ke pintu kok. Makasih buat gimnya malam ini."
        nar "Suara pintu apartemen menutup pelan di belakangnya. Apartemen mendadak terasa terlalu luas dan terlalu dingin, meninggalkan dua gelas kosong di meja yang belum sempat dibereskan."
    return

# ┌─ PANDUAN CERITA · Y-D09 · Koita di Depan Pintu
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kisaragi Yutaka
# │ AWALAN  : Koita bertengkar atau ditinggal heroine
# │ INTI    : A Biarkan menginap / B dengarkan lalu antar pulang / C tolak
# │ AKHIRAN : benih BL atau persahabatan
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y_D09:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Jam satu pagi")
    nar "Koita berdiri di depan pintu pukul satu pagi. Rambutnya berantakan dan ia sudah menyiapkan senyum yang gagal muncul saat kau membukakan. Ia tidak membawa tas. Apa pun yang membuatnya datang tampaknya telah menghabiskan waktu lebih lama di kepalanya daripada perjalanan menuju apartemenmu."
    koita "Maaf datang tanpa kabar. Aku sudah coba menenangkan diri di jalan, tapi belum bisa pulang seperti ini. Boleh masuk sebentar? Aku tidak harus cerita semuanya sekarang, kan?"
    call kk_family_menu("Y-D09", ["Biarkan ia menginap.", "Dengarkan lalu antar pulang.", "Tolak dengan tegas."])
    if _return == "A":
        nar "Kau mempersilakannya tinggal dan menyiapkan tempat tidur. Koita duduk dekatmu sebelum akhirnya mulai bicara, sedikit demi sedikit. Kau tidak memakai kesedihannya untuk meminta jawaban romantis. Ketika ia tertidur, kau merasakan keinginan menjaganya sekaligus takut pada betapa besar arti keinginannya datang kepadamu."
    elif _return == "B":
        koita "Terima kasih sudah dengar. Aku masih sedih, tapi sekarang bisa pulang. ...Besok jangan merasa harus menganggap semuanya baik-baik saja. Tanya aku lagi, ya."
    else:
        play sound "audio/sfx/door_close.wav"
        nar "Kau mengatakan tidak bisa menerimanya malam ini. Koita mengangguk sebelum kau selesai menjelaskan, lalu meminta maaf sekali lagi. Setelah pintu tertutup, apartemen kembali tenang. Kau tidak tahu ke mana ia pergi berikutnya, dan ketidaktahuan itu tinggal lebih lama daripada alasanmu menolak."
    return

# ┌─ PANDUAN CERITA · Y-D10 · Menunggu di Stasiun
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kisaragi Yutaka
# │ AWALAN  : Female Route; yutaka_harap ≥ 50
# │ INTI    : A Jalan bersama / B terima tumpangan / C tolak
# │ AKHIRAN : yutaka_harap +
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y_D10:
    call kk_scene_enter("chiasa", "Stasiun · Yutaka menunggu")
    nar "Yutaka menunggu di luar stasiun setelah kelas malammu. Ia menoleh terlalu cepat ketika melihatmu, kemudian mencoba membuat pertemuan itu terdengar kebetulan. Di tangannya ada minuman yang belum dibuka. Kau bisa melihat ia sudah memikirkan beberapa kalimat dan kini lupa memilih salah satunya."
    yutaka "Baru selesai? Aku tadi di sekitar sini. ...Baik, itu tidak sepenuhnya benar. Aku menunggu. Kalau kau mau pulang sendiri, bilang saja."
    call kk_family_menu("Y-D10", ["Jalan bersama.", "Terima tumpangan.", "Tolak dengan sopan."])
    if _return == "A":
        nar "Kau memilih berjalan bersamanya. Yutaka menyesuaikan langkah dan menanyakan kelasmu tanpa berusaha membuat setiap jawaban menjadi godaan. Di persimpangan, ia bertanya apakah masih boleh menemani. Harapannya tumbuh justru karena kau memilih tetap berjalan, bukan karena ia berhasil menahanmu."
    elif _return == "B":
        nar "Kau menerima tawaran pulang bersamanya. Di kendaraan, percakapan terdengar lebih dekat karena tidak ada orang lain yang memotong. Yutaka mengingat tujuanmu dan tidak menambah perjalanan tanpa bertanya. Ketika sampai, ia tampak ingin malam berlangsung lebih lama, tetapi tetap membiarkanmu turun."
    else:
        yutaka "Baik, aku mengerti. Terima kasih sudah bilang terus terang. Kabari kalau nanti butuh sesuatu. ...Sampai ketemu di rumah Koita."
    return

# ┌─ PANDUAN CERITA · Y-D11 · Pengakuan Jumat Malam
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kisaragi Yutaka
# │ AWALAN  : Female Route; yutaka_harap ≥ 70
# │ INTI    : A Jawab sekarang / B tunda / C anggap candaan
# │ AKHIRAN : E-YU-01 atau E-YU-03 menguat
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y_D11:
    call kk_scene_enter("chiasa", "Kafe bar · Pengakuan Jumat malam")
    nar "Di kafe bar, Yutaka berhenti bercanda dan menaruh gelasnya jauh dari tangan. Alkohol telah membuat suaranya lebih berani, tetapi ia masih tampak takut pada jawabanmu. Kau menyadari percakapan ini perlu diingat lagi besok, ketika tidak ada minuman yang bisa dijadikan alasan."
    yutaka "Aku menyukaimu, Chiasa. Aku sudah terlalu sering bercanda sampai takut kau tidak akan percaya kalau aku serius. Kau boleh minta waktu. Aku cuma ingin malam ini kau tahu."
    call kk_family_menu("Y-D11", ["Jawab sekarang.", "Minta ia menundanya.", "Anggap candaan mabuk."])
    if _return == "A":
        nar "Kau menjawab bahwa perasaannya tidak hendak kauanggap permainan. Wajah Yutaka berubah sebelum ia sempat menutupinya dengan tawa. Kalian sepakat membicarakannya lagi saat sama-sama jernih. Yang lahir malam ini adalah kesediaan saling mendengar, bukan kewajiban memenuhi seluruh harapannya sekaligus."
    elif _return == "B":
        yutaka "Baik. Besok kita bicara lagi. Aku ingin kau menjawab orang yang benar-benar hadir, bukan cuma orang yang tadi minum terlalu banyak. Aku tidak akan marah karena kau meminta waktu."
    else:
        yutaka "Candaan... ya. Kalau itu yang ingin kaudengar. ...Maaf, aku perlu keluar sebentar. Tidak, kau tidak perlu ikut."
    return

init 1 python:
    _hook("Y-D01-A", lambda: kk_adj("uang_dibelanjakan",10))
    _hook("Y-D01-B", lambda: kk_adj("uang_disimpan",10))
    _hook("Y-D01-C", lambda: (kk_adj("uang_diberikan",10), kk_flag("pemain_dermawan")))
    _hook("Y-D02-A", lambda: (kk_adj("curiga_identitas",10), kk_flag("identitas_online_retak")))
    _hook("Y-D02-B", lambda: None)
    _hook("Y-D02-C", lambda: kk_flag("hayase_diputus"))
    _hook("Y-D04-A", lambda: (kk_adj("daichi_tahu",10), kk_flag("daichi_tahu_catatan")))
    _hook("Y-D04-B", lambda: kk_adj("daichi_tahu",3))
    _hook("Y-D04-C", lambda: (kk_adj("daichi_tahu",6), kk_flag("daichi_disogok")))
    _hook("Y-D05-A", lambda: kk_adj("curiga_daisuke",-5))
    _hook("Y-D05-B", lambda: kk_adj("curiga_daisuke",10))
    _hook("Y-D05-C", lambda: kk_adj("curiga_daisuke",4))
    _hook("Y-D06-A", lambda: (kk_flag("intel_tojo"), kk_adj("bukti_tojo",8)))
    _hook("Y-D06-B", lambda: (kk_flag("rekaman_tojo"), kk_adj("bukti_tojo",12)))
    _hook("Y-D06-C", lambda: kk_flag("tojo_berhutang_budi"))
    _hook("Y-D07-A", lambda: (kk_adj("kelekatan_nagisa",6), kk_flag("rumor_nagisa_menginap")))
    _hook("Y-D07-B", lambda: kk_rel("nagisa","trust",4))
    _hook("Y-D07-C", lambda: kk_rel("nagisa","aff",-3))
    _hook("Y-D09-A", lambda: (kk_adj("ikatan_bl",8), kk_flag("koita_arah_bl")))
    _hook("Y-D09-B", lambda: kk_rel("koita","trust",5))
    _hook("Y-D09-C", lambda: kk_koita_collapse(5))
    _hook("Y-D10-A", lambda: kk_adj("yutaka_harap",8))
    _hook("Y-D10-B", lambda: (kk_adj("yutaka_harap",10), kk_rel("chiasa","intim",3)))
    _hook("Y-D10-C", lambda: kk_adj("yutaka_harap",-5))
    _hook("Y-D11-A", lambda: (kk_flag("yutaka_ditanggapi"), kk_adj("yutaka_harap",10)))
    _hook("Y-D11-B", lambda: kk_adj("yutaka_harap",5))
    _hook("Y-D11-C", lambda: (kk_adj("yutaka_harap",-10), kk_flag("yutaka_ditolak_candaan")))
