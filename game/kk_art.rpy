# Draft editorial dari Event_Chiasa C05/C09 dan Alur_Cabang/06 §11–12.
# ┌─ PANDUAN CERITA · C05 · Miono Menelepon
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : editor meminta cover jilid baru.
# │ INTI    : A menolak halus / B menerima dan berlatih / C minta bantuan Karuha.
# │ AKHIRAN : curiga_mio; B bisa membuka kemampuan baru bertahap.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C05:
    call kk_scene_enter("chiasa", "Rumah Amamiya")
    nar "Di atas meja belajar kamarmu, buku sketsa bersampul hitam milik Chiasa masih terbuka di halaman latihan anatomi tangan yang belum selesai. Beberapa lembar kertas buram yang penuh goresan kaku hasil latihanmu sendiri tergeletak di samping penghapus uli dan rautan pensil."
    nar "Baru saja kamu meletakkan pensil mekanik dan hendak merenggangkan jari-jarimu yang pegal, ponsel di dekat tabung kuas bergetar panjang di atas permukaan meja kayu."
    play sound "audio/sfx/phone_vibrate.wav"
    nar "Layar ponsel menyala menampilkan nama pemanggil 'Higashiyama Miono (Redaksi Bunko)'."
    nar "Kamu menatap nama itu selama dua dering penuh. Selama beberapa bulan terakhir, kiriman royalti cetak ulang sebesar lima puluh ribu yen dari penerbit selalu masuk otomatis ke rekening tanpa menuntut gambar baru. Panggilan suara langsung dari editor jelas bukan sekadar pemberitahuan transfer bank."
    nar "Kamu menarik napas pendek, menggeser tombol hijau di layar, lalu menempelkan ponsel ke telinga."
    nar "Suara riuh redaksi penerbitan yang diselingi dering telepon meja dan ketukan papan ketik terdengar samar di latar belakang sebelum suara editor itu masuk dengan jernih."
    nar "Kamu menegakkan posisi dudukmu di kursi kayu dan menyiapkan nada bicara yang paling tenang agar tidak terdengar kaku."
    if kk_slot == 0:
        chiasa "Halo, selamat pagi, Miono-san."
    elif kk_slot == 1:
        chiasa "Halo, selamat siang, Miono-san."
    elif kk_slot == 2:
        chiasa "Halo, selamat sore, Miono-san."
    else:
        chiasa "Halo, selamat malam, Miono-san."
    "Miono" "Halo, Shena-sensei! Syukurlah langsung diangkat, aku takut tadi masih di dalam ruang studio kampus atau lagi istirahat. Gimana kuliah semester pertamanya di Kouseikan? Sudah mulai terbiasa sama tugas-tugas seni?"
    nar "Suara Miono di seberang telepon terdengar cerah, cepat, dan akrab seperti seorang editor yang sudah bekerja sama dengan pemilik tubuh ini sejak bangku SMA."
    chiasa "Sudah mulai terbiasa kok, Miono-san. Dosen-dosennya juga baik, cuma jam praktiknya aja yang lumayan panjang."
    "Miono" "Haha, anak studio memang begitu semua keluhannya. Apalagi semester awal biasanya disuruh latihan garis manual terus dari pagi sampai sore ya? Oh iya, Sensei, aku menelepon karena ada kabar bagus banget dari rapat redaksi terbaru. Naskah jilid keempat seri novel strategi yang Sensei pegang kemarin akhirnya sudah selesai ditulis!"
    chiasa "Jilid keempat... sudah selesai naskahnya ya, Miono-san?"
    "Miono" "Iya! Penulisnya baru kirim draf finalnya ke mejaku. Terus terang aja, hasil cetakan ulang jilid ketiga kemarin laris banget di toko buku, dan banyak pembaca yang menulis di kartu pos survei kalau mereka jatuh cinta sama ilustrasi sampul buatan Sensei."
    chiasa "Wah... syukurlah kalau pembaca suka sama buku ketiganya."
    "Miono" "Apalagi cara Sensei menggambar sorot mata tokoh utamanya waktu berdiri di benteng salju itu, lho. Garisnya tipis tapi suasananya dingin dan hidup banget. Bahkan beberapa pembaca sampai menyurati redaksi menanyakan apakah jilid keempat nanti masih pakai sudut pandang yang sama."
    nar "Pandanganmu turun menatap buku novel cetakan jilid ketiga yang berjajar rapi di rak atas meja belajarmu, lalu turun lagi ke kertas buram di depan tanganmu sendiri. Lingkaran proporsi wajah dan garis jari yang baru saja kamu buat sepuluh menit lalu tampak kaku dan patah-patah, terpisah jauh sekali dari tarikan garis halus milik Shena."
    chiasa "Waktu gambar adegan benteng salju di jilid ketiga itu memang lumayan lama mencari sudut bayangannya, Miono-san."
    "Miono" "Tapi hasil akhirnya sepadan banget sama kerja keras Sensei! Sampai sekarang poster promosinya masih dipajang di toko buku dekat stasiun pusat lho."
    chiasa "Syukurlah kalau pihak toko buku juga suka sama komposisi warnanya."
    "Miono" "Bukan cuma suka, bagian pemasaran bahkan bilang sampul jilid ketiga itu yang paling banyak menarik pembaca baru tahun ini."
    nar "Setiap pujian tulus yang dilontarkan Miono untuk kemahiran menggambar Chiasa yang asli justru membuat beban di balik penyamaranmu terasa semakin nyata."
    nar "Kamu menggeser ujung pensil mekanik di atas meja sambil memperhatikan deretan kuas cat air dan pena tinta milik Chiasa yang tertata rapi berdasarkan ukurannya."
    nar "Seluruh peralatan profesional di meja ini sudah lengkap, tetapi keterampilan bertahun-tahun yang pernah menghidupkan karakter-karakter novel tersebut tidak ikut berpindah ke jari-jarimu."
    "Miono" "Makanya kepala redaksi langsung minta aku hubungi Sensei hari ini buat mengamankan jadwal ilustrasi sampul sekaligus tiga gambar sisipan hitam-putih untuk jilid keempat. Di jilid ini ada adegan perundingan malam di ruang peta yang cocok sekali sama gaya bayangan khas Sensei."
    chiasa "Satu sampul warna penuh sama tiga ilustrasi sisipan hitam-putih ya, Miono-san..."
    "Miono" "Betul! Untuk tenggat pengumpulannya masih sekitar dua bulan lagi sih sebelum naik cetak. Honornya juga naik sedikit mengikuti angka cetak ulang jilid kemarin. Gimana menurut Sensei, jadwal kuliah bulan ini memungkinkan nggak buat ambil proyek jilid keempat?"
    chiasa "Naskah jilid keempatnya sendiri tebalnya masih sama seperti tiga buku sebelumnya, Miono-san?"
    "Miono" "Lebih tebal sekitar tiga puluh halaman karena ada babak pengepungan benteng di bagian akhir, makanya penulisnya semangat sekali ingin melihat sketsa tokohnya lebih awal."
    chiasa "Untuk jadwal pencetakannya berarti direncanakan terbit awal musim dingin nanti ya?"
    "Miono" "Iya, target rilisnya bulan Desember supaya pas masuk daftar katalog liburan akhir tahun toko buku utama."
    nar "Kamu melirik kalender meja kecil di samping kotak pensil warna sambil menghitung sisa minggu efektif sebelum ujian akhir semester kampus dimulai."
    nar "Menerima tawaran ini tanpa kemampuan menggambar yang setara dengan karya lama Chiasa jelas berisiko membuka penyamaranmu di hadapan pihak penerbit profesional."
    nar "Namun menolak proyek utama dari seri novel yang membesarkan nama pena Shena juga bukan keputusan ringan yang bisa berlalu tanpa pertanyaan dari redaksi."
    nar "Di seberang sambungan, terdengar bunyi klik pulpen Miono yang sudah siap mencatat jawabanmu di buku agendanya."
    call kk_family_menu("C05", ["\"Terima kasih banyak tawarannya, Miono-san, tapi untuk jilid baru ini kayaknya aku belum bisa ambil dulu.\"", "\"Baik, Miono-san, aku ambil proyeknya. Boleh minta tenggat sketsa kasarnya agak longgar?\"", "\"Boleh aku minta waktu sebentar? Ada teman studio yang pengin kuajak diskusi dulu.\""])
    if _return == "A":
        chiasa "Terima kasih banyak tawarannya, Miono-san. Aku senang banget dengar jilid sebelumnya laris dan disukai pembaca. Tapi jujur aja, untuk jilid keempat ini kayaknya aku belum bisa ambil proyeknya dulu."
        nar "Bunyi ketukan pulpen di seberang telepon langsung berhenti. Terdengar jeda hening selama dua detik sebelum Miono kembali bersuara dengan nada hati-hati."
        "Miono" "Eh... belum bisa ambil ya, Shena-sensei? Jadwal tugas studio di kampus lagi padat banget ya bulan ini?"
        chiasa "Iya, Miono-san. Tugas dasar semester awal ini banyak yang harus dikerjakan manual tiap hari, dan aku takut kalau kupaksakan ambil jadwal sampul sekarang, hasilnya malah nggak maksimal dan mengecewakan penulis maupun pembacanya."
        "Miono" "...Begitu ya. Jujur aja sayang sekali sih, soalnya penulisnya sudah berharap Sensei lagi yang pegang jilid ini. Kemarin beliau bahkan sempat bilang membayangkan adegan ruang petanya lewat goresan Sensei."
        chiasa "Maaf banget ya, Miono-san, jadi bikin tim redaksi harus repot cari ilustrator pengganti buat jilid ini."
        "Miono" "Nggak apa-apa, Sensei, bagian cari jadwal pengganti itu memang kerjaanku sebagai editor kok. Kalau memang jadwal kuliah tahun pertama lagi berat, aku nggak mungkin memaksa Sensei begadang sampai sakit. Lagian kualitas itu yang paling penting."
        chiasa "Terima kasih sudah mengerti, Miono-san."
        "Miono" "Tapi Sensei beneran nggak lagi mengalami kendala kesehatan atau cedera pergelangan tangan gara-gara tugas kampus kan? Soalnya waktu SMA dulu, sepadat apa pun jadwal ujian sekolah, Sensei selalu paling semangat kalau dikirimi naskah baru."
        chiasa "Tanganku sehat kok, Miono-san, sama sekali nggak ada cedera. Cuma penyesuaian ritme belajar di studio universitas ini memang jauh lebih menyita waktu daripada waktu masih SMA dulu."
        "Miono" "Syukurlah kalau bukan karena sakit. Soalnya beberapa ilustrator muda yang baru masuk kuliah seni kadang suka kelelahan fisik karena kaget sama beban tugas kanvas besar."
        chiasa "Iya, minggu ini saja ada dua tugas gambar bentuk dan komposisi warna yang harus dikerjakan langsung di ruang studio sampai sore."
        "Miono" "Pantas saja jadwalnya padat sekali. Kalau begitu untuk jilid keempat ini biar kubicarakan dulu sama kepala redaksi dan penulisnya supaya kami bisa mengatur solusi sementara."
        chiasa "Tolong sampaikan permohonan maafku juga ke penulisnya ya, Miono-san. Aku tetap berdoa semoga jilid keempatnya nanti laris di pasaran."
        "Miono" "Pasti kusampaikan salamnya, beliau pasti maklum kok karena tahu Sensei baru tahun pertama kuliah."
        nar "Terdengar bunyi lembaran buku agenda yang ditutup pelan dari seberang saluran telepon."
        "Miono" "Oh iya, tenang aja ya, untuk royalti cetak ulang dari jilid satu sampai tiga tetap ditransfer tiap bulan seperti biasa, hak ciptanya kan tetap di tangan Sensei. Nanti kalau jadwal studio kampus sudah lebih longgar dan Sensei sudah siap pegang proyek buku lagi, langsung hubungi nomor pribadiku aja!"
        chiasa "Baik, Miono-san. Nanti kalau tugas semester awal ini sudah lebih ringan dan tanganku sudah siap lagi buat jadwal penerbitan, pasti langsung kukabari."
        "Miono" "Kutunggu banget lho kabar baiknya, Sensei! Jangan sampai lupa istirahat dan tetap semangat kuliahnya ya."
        chiasa "Terima kasih banyak, Miono-san. Selamat melanjutkan rapatnya."
        "Miono" "Sama-sama, Shena-sensei! Kalau akhir bulan nanti ada cetakan contoh jilid ketiga tambahan dari gudang, nanti kukirimkan dua eksemplar ke alamat rumah seperti biasa ya."
        chiasa "Baik, Miono-san, nanti langsung kuterima di rumah. Selamat sore."
        nar "Kamu menunggu sampai nada sambungan benar-benar berakhir sebelum menurunkan ponsel dari telingamu."
        nar "Di luar jendela kamar, angin sore menggoyangkan dahan pohon halaman sambil membawa bunyi lonceng sepeda dari jalan depan gang."
        nar "Kamu menatap kembali lembar latihan anatomi tangan di atas meja yang tadi sempat membuat keningmu berkerut sepanjang jam belajar."
        nar "Menolak tawaran ilustrasi jilid keempat ini memang menyelamatkanmu dari tenggat waktu dua bulan ke depan yang mustahil kamu penuhi dengan kemampuanmu saat ini."
        nar "Namun kamu tahu bahwa selama uang royalti buku itu masih masuk ke rekening Chiasa, pihak redaksi akan tetap menganggap Shena aktif berkarya."
        nar "Cepat atau lambat, kamu tetap harus memutuskan apakah akan melatih tangan ini sampai mampu menggantikan goresan aslinya atau menutup nama pena itu selamanya."
        nar "Dari lantai bawah terdengar samar suara televisi ruang keluarga yang dinyalakan Koita, mengingatkanmu betapa tenangnya rutinitas rumah ini selama rahasiamu tetap terjaga."
        nar "Kamu menarik laci meja belajar dan menyimpan lembar-lembar kertas latihanmu yang masih kasar ke bagian paling bawah agar tidak terlihat jika sewaktu-waktu ada yang masuk ke kamar."
        nar "Meskipun kamu berhasil mengulur waktu tanpa menimbulkan kecurigaan besar hari ini, nama pena Shena tetap merupakan bagian dari hidup Chiasa yang tidak bisa selamanya kamu hindari."
        nar "Sambungan telepon terputus. Kamu meletakkan ponsel kembali ke samping tabung kuas dan menutup buku sketsa hitam itu perlahan. Penyamaranmu aman dari tenggat penerbit untuk musim ini, meski kamu tahu panggilan serupa cepat atau lambat akan datang lagi."
    elif _return == "B":
        chiasa "Baik, Miono-san, aku ambil proyek jilid keempatnya. Cuma karena hari-hari ini aku masih ada jadwal kelas studio yang padat di kampus, boleh aku minta tenggat buat pengiriman sketsa kasarnya agak dilonggarkan sedikit?"
        nar "Terdengar helaan napas lega yang panjang dari seberang telepon, disusul bunyi lembaran kertas agenda yang dibalik cepat."
        "Miono" "Wah, syukurlah Sensei bersedia! Aku tadi sudah deg-degan takut Sensei menolak gara-gara sibuk kuliah! Kalau soal jadwal sketsa kasar, tentu aja bisa kugeser mundur dua minggu dari jadwal standar, Sensei. Bagian tata letak sampul biar kukosongkan duluan di percetakan."
        chiasa "Kalau ada waktu tambahan dua minggu untuk sketsa awal, aku punya cukup ruang buat menata komposisi tokohnya, Miono-san."
        "Miono" "Sip, sudah kucatat rapi di jadwal redaksi! Sebentar lagi kukirimkan ringkasan bab penting jilid keempat beserta catatan adegan untuk tiga ilustrasi sisipannya lewat surel ya. Ada satu tokoh panglima baru yang perlu dirancang kostumnya juga, Sensei baca-baca santai aja dulu sambil cari ide."
        chiasa "Panglima barunya perempuan atau laki-laki, Miono-san? Ada ciri khusus dari penulisnya?"
        "Miono" "Laki-laki muda, rambut perak pendek, pakai mantel perwira berkerah tinggi tanpa lencana. Katanya penulisnya ingin ekspresinya terlihat tenang tapi matanya tajam waktu menatap peta perang."
        chiasa "Untuk palet warna sampul utamanya nanti apakah masih memakai nuansa biru malam dan abu-abu salju seperti jilid ketiga?"
        "Miono" "Nah, buat jilid keempat ini penulisnya menyarankan ada sedikit pantulan cahaya obor kuning hangat dari sisi kiri bawah supaya kontras sama warna perak rambut tokoh barunya."
        chiasa "Pantulan cahaya obor dari kiri bawah di atas warna dingin ya... baik, akan kucoba atur gradasi cahayanya di draf awal nanti."
        "Miono" "Wah, membayangkannya saja sudah keren sekali! Untuk tiga ilustrasi sisipan hitam-putihnya nanti cukup fokus di ekspresi setengah badan sama detail lipatan jubahnya saja kok, Sensei, nggak perlu latar ruangan yang terlalu rumit."
        chiasa "Mengerti, Miono-san. Penjelasan itu sangat membantu buat membagi waktu pengerjaanku."
        "Miono" "Kalau di tengah jalan waktu menyusun sketsa kasar ada deskripsi naskah yang terasa kurang jelas, langsung kirim pesan saja ke aku kapan pun ya, Sensei."
        chiasa "Baik, langsung kuperiksa surel lengkapnya begitu masuk. Terima kasih banyak kelonggaran waktunya, Miono-san."
        "Miono" "Aku dan tim redaksi yang berterima kasih, Shena-sensei! Penulisnya pasti senang banget dengar kabar ini. Sampai ketemu di kiriman draf pertama ya, semangat kuliahnya!"
        chiasa "Terima kasih, Miono-san."
        nar "Begitu panggilan berakhir, kamar yang tadinya tenang mendadak terasa jauh lebih sempit. Di layar ponselmu, pesan konfirmasi jadwal dan tautan ringkasan naskah dari Miono langsung masuk hanya berselang satu menit."
        nar "Kamu membuka berkas catatan redaksi itu di layar ponsel dan membacanya pelan dari baris pertama sampai terakhir, lalu menatap pensil mekanik di tanganmu. Tidak ada jalan mundur setelah mengiyakan kontrak ini."
        nar "Kamu mengambil map arsip dari rak bawah meja belajar yang menyimpan draf-draf sketsa asli Chiasa untuk jilid pertama hingga ketiga."
        nar "Lembar demi lembar kertas kalkir penuh catatan anatomi dan uji coba bayangan pensil milik pemilik asli tubuh ini kamu bentangkan berjejer di bawah lampu baca."
        chiasa "{i}Cara dia menarik garis bayangan di lipatan mantel selalu dimulai dari lekuk siku bagian dalam... kalau aku melatih urutan tarikannya dua jam setiap malam, setidaknya proporsi dasarnya bisa kuikuti.{/i}"
        nar "Kamu menyalakan lampu meja pada tingkat paling terang dan menyiapkan rautan pensil di sudut kanan papan gambar."
        nar "Kamu menyingkirkan kertas buram yang tadi penuh coretan ragu, menarik satu lembar kertas gambar baru dari laci meja, lalu membuka halaman-halaman lama buku sketsa Chiasa di sampingnya sebagai acuan. Garis demi garis proporsi wajah, kerah mantel, dan lipatan tangan mulai kamu latih ulang dari dasar."
        nar "Pada lembar latihan pertama, tarikan garis rahang dan arah lipatan jubah perwira yang kamu buat masih tampak miring dan terlalu tebal di bagian siku."
        nar "Kamu menghapus bagian yang kaku tersebut dengan penghapus uli secara perlahan, lalu mengulang tarikan garisnya dari bahu atas sambil mengikuti ritme goresan tipis di buku catatan lama Chiasa."
        nar "Di halaman belakang buku sketsa hitam itu, kamu menemukan catatan kecil tulisan tangan Chiasa tentang rumus pembagian bayangan wajah saat terkena sumber cahaya dari sudut bawah."
        chiasa "{i}Untung sekali dia punya kebiasaan menulis catatan langkah pewarnaan dan sudut jatuhnya bayangan di pinggir halaman sketsa... ini bisa jadi panduan utamaku.{/i}"
        nar "Kamu menyalin ulang diagram pencahayaan obor tersebut ke kertas latihan kedua, menandai bagian mana dari kerah mantel tinggi itu yang harus dibiarkan terang dan bagian mana yang harus diarsir gelap."
        nar "Meski gerakan jari-jarimu belum seluwes pemilik asli tubuh ini, kerangka dasar untuk sketsa panglima berambut perak itu perlahan mulai terbentuk di atas meja belajarmu."
        nar "Kamu menarik penggaris lengkung dari dalam laci untuk membantu merapikan garis pinggiran meja peta perang yang menjadi latar utama ilustrasi sisipan pertama."
        nar "Setiap kali goresan pensilmu terasa mulai melenceng dari proporsi aslinya, kamu berhenti sejenak dan mencocokkannya kembali dengan lembar referensi lama milik Chiasa."
        nar "Ketekunan mengulang garis dasar itu perlahan mengurangi rasa panik yang tadi sempat muncul saat menerima telepon dari Miono."
        nar "Di sudut bawah kertas latihan, kamu menuliskan jadwal target harian selama dua minggu ke depan agar draf kasar ini siap dikirim tepat waktu."
        nar "Dari luar pintu kamar yang tertutup, suara langkah kaki Koita di lorong lantai dua terdengar lewat menuju ruang tengah."
        koita "Chi-chan, makan malamnya sudah siap di meja bawah ya! Jangan keasyikan gambar sampai lupa turun!"
        chiasa "Iya, Ko-nii! Aku bereskan pensil sebentar terus langsung turun!"
        nar "Kamu menyusun lembar-lembar latihan itu ke dalam map arsip dengan rapi sebelum bangkit keluar dari kamar untuk makan malam."
    else:
        chiasa "Terima kasih banyak tawarannya, Miono-san. Tapi sebelum aku kasih kepastian sanggup atau nggaknya, boleh aku minta waktu satu atau dua hari dulu? Kebetulan ada teman dekat di studio kampus yang mau kuajak diskusi soal pembagian waktu latihan sama jadwal tugasku bulan ini."
        "Miono" "Oh, mau mencocokkan jadwal sama teman studio dulu ya? Boleh banget kok, Shena-sensei. Rapat penetapan kontrak ilustratornya baru dikunci hari Jumat sore, jadi Sensei masih punya waktu buat menghitung jadwal dengan tenang."
        chiasa "Syukurlah kalau masih sempat. Sebelum hari Jumat pasti langsung kukabari keputusannya, Miono-san."
        "Miono" "Oke, kutunggu kabarnya ya, Sensei. Jangan terlalu diporsir tenaganya di kampus!"
        chiasa "Baik, terima kasih, Miono-san."
        nar "Setelah menutup telepon dari Miono, kamu tidak meletakkan ponselmu. Kamu membuka aplikasi pesan singkat dan mencari nama kontak Ishikawa Karuha yang sejak awal semester selalu duduk satu meja studio denganmu."
        nar "Kamu mengetik pesan dengan jujur tanpa berusaha terdengar seperti ilustrator mahir, menanyakan apakah besok sehabis kelas praktik studio Karuha langsung pulang dan apakah ia bersedia mengajarimu proporsi serta tarikan garis dasar dari awal."
        play sound "audio/sfx/phone_buzz.wav"
        nar "Kurang dari satu menit kemudian, ponsel di tanganmu bergetar berturut-turut menampilkan balasan antusias dari Karuha."
        "Pesan Karuha" "Eh, Chiasa tiba-tiba minta diajari proporsi garis dasar? Nggak salah kirim pesan kan ini? Hahaha!"
        "Pesan Karuha" "Kamu lagi mau ubah gaya gambar buat tugas semester ini ya? Atau habis kena koreksi dosen kemarin?"
        nar "Kamu mengetik balasan singkat bahwa akhir-akhir ini tarikan garis tanganmu terasa kaku dan kamu benar-benar ingin mengulang dari dasar tanpa terburu-buru."
        play sound "audio/sfx/phone_buzz.wav"
        "Pesan Karuha" "Kalau kamu serius mau latihan ulang bareng, aku kosong kok besok habis kelas studio! Kita pakai meja pojok dekat jendela aja sampai studio tutup, nanti kubawakan buku panduan anatomiku sama pensil arang sekalian."
        "Pesan Karuha" "Jangan lupa bawa penghapus uli yang masih bersih ya, besok kita mulai dari bentuk kubus sama tangan dulu!"
        nar "Kamu mengetik balasan lagi untuk menanyakan apakah kamu juga boleh membawa contoh gambar karakter bergaya ilustrasi novel untuk dipelajari struktur bayangannya."
        play sound "audio/sfx/phone_buzz.wav"
        "Pesan Karuha" "Boleh banget! Bawa saja semua contoh referensi yang mau kamu bedah, aku malah senang kalau kita sekalian latihan bedah garis ilustrasi buku!"
        "Pesan Karuha" "Pokoknya besok sore siapkan tenaga ya, aku nggak bakal kasih kamu pulang sebelum garis sketsa tanganmu lemas lagi kayak dulu!"
        nar "Membaca antusiasme tulus dari sahabat sejurusanmu itu membuat beban di pundakmu terasa jauh lebih ringan daripada saat pertama kali mengangkat telepon tadi."
        nar "Setidaknya dengan berlatih secara terbuka di bawah bimbingan teman studio yang memahami teknik dasar, kamu tidak harus meraba-raba sendirian di dalam kamar."
        nar "Kamu memilih tiga lembar fotokopi ilustrasi lama dari map arsip meja belajar tanpa menyertakan lembar kontrak berlabel nama pena Shena."
        nar "Kamu membalas ucapan terima kasih singkat, lalu menyimpan ponsel ke atas meja dan memasukkan buku sketsa kosong ke dalam tas kuliahmu untuk latihan besok bersama Karuha."
        nar "Setelah merapikan deretan pensil gambar berdasarkan ketebalan grafitnya ke dalam kotak kaleng, kamu menutup map referensi tersebut dan memasukkannya ke kompartemen utama tas."
        nar "Dari balik pintu kamar, suara langkah Koita yang naik ke lantai dua terdengar berhenti sebentar untuk mengingatkanmu turun makan malam sebelum sayur sup di dapur mendingin."
        chiasa "Iya, Ko-nii, sebentar lagi aku turun setelah merapikan meja belajar!"
        koita "Oke, kutunggu di meja makan ya, tadi aku bikin sup tahu hangat kesukaanmu!"
        chiasa "Wah, asyik! Tunggu dua menit lagi aku turun, Ko-nii!"
        nar "Kamu memeriksa sekali lagi isi tas kuliahmu untuk memastikan buku sketsa kosong, penghapus uli, dan tiga lembar fotokopi referensi sudah tersimpan aman di dalamnya."
        nar "Cahaya lampu jalan di depan rumah Amamiya tampak bersinar tenang menembus kaca jendela kamar yang separuh tertutup tirai."
        nar "Kamu menyadari bahwa mempelajari ulang keterampilan menggambar milik Chiasa dari nol bersama Karuha akan membutuhkan kesabaran ekstra setiap sore di studio."
        nar "Namun langkah jujur untuk berlatih dari dasar itu memberikan pijakan yang jauh lebih kokoh dibandingkan terus bersembunyi dari panggilan redaksi."
        nar "Kamu mematikan lampu baca meja dengan perasaan yang jauh lebih terarah, siap memulai latihan garis dari awal di studio kampus esok hari."
    return

# ┌─ PANDUAN CERITA · C09 · Buku Sketsa Kosong
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : pemain tidak bisa menggambar sebaik asli.
# │ INTI    : A latihan keras / B menyewa pihak lain / C berhenti.
# │ AKHIRAN : royalti ¥50.000 tetap masuk (), tetapi tawaran proyek dari Miono bisa gagal.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C09:
    call kk_scene_enter("chiasa", "Rumah Amamiya")
    if kk_slot >= 3:
        nar "Lampu meja belajar kuning hangat menyinari sudut kamarmu di lantai dua Rumah Amamiya. Dari balik jendela yang sedikit terbuka, udara musim panas bulan Juli masuk pelan bersama dengung serangga malam dari pekarangan tetangga."
    else:
        nar "Cahaya terik awal Juli menyelinap melewati tirai tipis kamarmu di lantai dua Rumah Amamiya. Suara tonggeret musim panas bergema dari deretan pohon halaman luar, sementara kipas angin kecil di pojok ruangan berputar lirih."
    nar "Di rak kayu tepat di atas meja belajar, tiga jilid novel ringan bertema strategi perang berjajar rapi dengan nama pena Shena tercetak kecil mengilap di punggung bukunya. Tepat di bawahnya, buku sketsa lama bersampul hitam milik Chiasa terbuka lebar di atas permukaan meja."
    nar "Halaman sebelah kiri dipenuhi sketsa pensil tangan Koita yang sedang menahan cangkir teh hangat. Tarikan garisnya ringan dan hidup sekali, mulai dari lengkungan buku jari, bayangan lipatan lengan kaus, sampai cara ibu jarinya menyentuh pegangan porselen, seolah tangan yang menggambarnya mengenal setiap lekuk itu tanpa perlu menatap lama."
    nar "Tepat di halaman sebelah kanan, percobaanmu meniru posisi tangan dan cangkir yang sama tampak kaku dan datar. Ruas jemarinya terlalu rata, sambungan pergelangannya patah-patah, dan permukaan kertas di sekitarnya sudah mulai berserabut tipis karena terlalu sering kamu hapus."
    nar "Di samping tempat pensil, layar ponselmu menyala menampilkan dua gelembung pesan terbaru dari Higashiyama Miono yang baru saja masuk sejam lalu."
    "Pesan Miono" "Halo, Shena-sensei! Kabar baik dari rapat cetak kemarin, cetakan ulang jilid sebelumnya baru saja lolos percetakan lagi, jadi royalti lima puluh ribu yen per bulan tetap meluncur otomatis seperti biasa ya."
    "Pesan Miono" "Oh iya, menjelang libur musim panas bulan Juli ini redaksi sedang menyusun daftar proyek paruh kedua, dan cukup banyak kartu pos pembaca menanyakan ilustrasi baru Sensei. Kalau Sensei sudah punya sketsa kasar atau waktu luang buat pegang sampul baru, kabari aku ya!"
    chiasa "{i}Aku mewarisi wajahnya, kamarnya, sandi ponselnya, sampai rekening royaltinya... tapi kepekaan tangan yang bikin gambar di halaman kiri ini bernapas sama sekali nggak ikut bangun bersamaku.{/i}"
    nar "Tepat ketika kamu mengencangkan genggaman pada pensil mekanikmu, ketukan pelan dua kali terdengar di pintu kamar sebelum kepala Koita melongok masuk membawa nampan kecil berisi dua gelas teh jelai dingin dan mangkuk kecil potongan melon."
    koita "Chi-chan, lagi sibuk banget ya? Aku bikin teh dingin sama potong melon di bawah, sekalian kubawain ke atas biar kamarmu nggak terlalu gerah."
    chiasa "Masuk aja, Ko-nii. Taruh di pojok kanan meja ya biar embunnya nggak kena kertas."
    nar "Koita melangkah masuk mengenakan kaus santai rumahannya, meletakkan gelas berembun dan mangkuk kecil itu dengan hati-hati di sisi kanan meja. Pandangannya sempat jatuh ke buku sketsa hitam yang terbuka lebar di depanmu, lalu sudut bibirnya terangkat lembut."
    koita "Eh, gambar yang di halaman kiri itu... tanganku waktu kita minum teh di beranda musim gugur tahun lalu ya? Pantas dulu kamu nyuruh aku duduk diam pegang cangkir sampai pergelanganku pegal. Masih kamu simpan rapi ternyata."
    chiasa "Iya, baru ketemu lagi pas aku buka bagian depan bukunya."
    koita "Aku masih ingat banget sore itu. Kamu cuma butuh sepuluh menit buat bikin bayangan buku jarinya kelihatan sejelas itu sambil masih sempat ngejek aku nggak boleh gerak sedikit pun. Jujur aja aku selalu kagum sih sama tanganmu, Chi-chan."
    chiasa "{i}Sepuluh menit sambil bercanda... sementara aku barusan menghabiskan hampir setengah jam dan hasilnya masih kaku kayak tangan boneka kayu.{/i}"
    nar "Tatapan Koita bergeser sesaat ke halaman sebelah kanan yang penuh bekas hapusan, serbuk karet halus, dan garis yang masih tampak ragu. Ia tidak menertawakan maupun melontarkan komentar aneh, hanya mengerutkan kening sedikit penuh perhatian."
    koita "Tugas ujian studio tahun kedua bulan Juli lagi berat banget ya, Chi-chan? Kemarin waktu ketemu Karuha di gerbang kampus, dia juga bilang dosen anatomi semester ini lagi ketat banget kasih nilai. Atau... Miono-san lagi menanyakan jadwal proyek sampul baru lagi?"
    chiasa "Nggak sampai ditekan kok, Ko-nii. Cuma belakangan aku ngerasa tarikan tanganku agak kaku aja pas lagi capek, jadi lagi coba ngerapiin ulang bentuk dasarnya dari awal."
    koita "Oh, wajar sih kalau lagi pekan ujian. Tadi pagi Ayah juga sempat kirim pesan dari tempat liputan nanyain pameran semester ini, katanya dia selalu senang lihat perkembangan garis gambar kamu."
    chiasa "{i}Ayahnya sendiri juga masih mengingat Chiasa lewat garis-garis di buku ini...{/i}"
    chiasa "Nanti kubalas pesan Ayah kalau latihanku sudah kelar ya, Ko-nii."
    koita "Jangan dipaksakan sampai pergelangan tanganmu keram ya, ingat dulu kamu pernah sampai dikompres gara-gara lembur terlalu lama. Kalau mau istirahat, makan buahnya dulu, atau mau cerita soal kerjaan dari Miono-san, aku masih baca buku di ruang bawah."
    chiasa "Iya, makasih banyak teh dingin sama melonnya, Ko-nii."
    koita "Sama-sama, semangat ya latihannya."
    nar "Koita mengangguk hangat lalu melangkah keluar dan menutup pintu kamar perlahan. Keheningan musim panas langsung kembali mengisi ruangan, menyisakan dirimu berhadapan dengan dua halaman buku sketsa yang terasa seperti milik dua orang asing serta pesan Miono yang masih menunggu balasan di layar."
    nar "Tetesan embun dari dinding gelas teh jelai dingin perlahan mengalir turun membasahi tatakan kayu kecil di sudut kanan mejamu."
    nar "Di atas rak buku, punggung tiga jilid novel strategi yang memuat nama Shena tampak seolah mengingatkanmu pada reputasi besar yang telah dibangun oleh pemilik tubuh ini."
    nar "Setiap bulan, kiriman royalti lima puluh ribu yen dari cetakan ulang buku-buku tersebut tetap masuk ke rekening tanpa menuntut gambar baru."
    nar "Akan tetapi, tawaran proyek paruh kedua dari Higashiyama Miono jelas tidak bisa dijawab hanya dengan mengandalkan arsip sketsa lama selamanya."
    nar "Jika kamu memaksakan diri mengirim ilustrasi baru dengan kondisi tarikan garis yang masih kaku seperti halaman sebelah kanan, editor sekaliber Miono pasti akan langsung menyadari perbedaannya."
    nar "Sementara itu, bayangan wajah hangat Koita dan pesan dari Daisuke tadi menunjukkan betapa eratnya bakat menggambar ini terikat dengan identitas Amamiya Chiasa di mata keluarganya."
    nar "Kamu mengangkat tangan kananmu di bawah sorot lampu belajar dan memperhatikan jemari lentik yang masih belum sepenuhnya terbiasa mengikuti perintah pikiranmu."
    nar "Ada tiga jalan berbeda yang kini terbentang di hadapanmu untuk menyikapi warisan nama pena Shena ini."
    nar "Kamu bisa mulai membangun kemampuan menggambarmu sendiri dari bentuk dasar yang paling jujur tanpa terus dihantui perbandingan dengan halaman lama."
    nar "Kamu juga bisa mencari jalan pintas dengan menyewa ilustrator lepas secara anonim di dunia maya demi menjaga nama Shena tetap memproduksi karya baru."
    nar "Atau kamu dapat menutup buku sketsa ini untuk sementara waktu dan meminta jeda resmi kepada pihak redaksi hingga pikiranmu lebih tenang."
    nar "Kipas angin di sudut kamar terus berputar pelan mengusir hawa gerah bulan Juli saat kamu kembali menatap layar ponselmu."
    nar "Di atas nampan kayu, potongan melon segar yang dibawakan Koita tampak berkilau terkena sorot lampu baca mejamu."
    nar "Kepercayaan tulus dari kakak tirimu dan editor penerbitmu menuntut jawaban yang tidak bisa kamu tunda lebih lama lagi."
    nar "Setiap pilihan yang kamu ambil sore ini akan menentukan masa depan nama pena Shena sepanjang paruh kedua tahun ajaran."
    nar "Kamu menyentuh pinggiran sampul buku sketsa hitam itu sekali lagi sebelum mengunci tekadmu."
    nar "Bayangan pepohonan musim panas di luar jendela bergerak pelan seiring hembusan angin bulan Juli."
    nar "Kamu menatap lurus ke arah lembaran kertas gambar di depanmu tanpa keraguan lagi."
    nar "Dengan napas panjang yang teratur, kamu meletakkan tangan di tepi meja belajar untuk mengambil keputusan."
    call kk_family_menu("C09", ["Singkirkan halaman lama, mulai lagi dengan latihan sendiri.", "Cari ilustrator lain untuk mengerjakannya diam-diam.", "Tutup bukunya dulu untuk hari ini."])
    if _return == "A":
        nar "Kamu menarik napas perlahan, mengambil selembar kertas gambar polos, lalu meletakkannya tepat menutupi sketsa tangan Koita di halaman kiri supaya matamu berhenti terus-terusan membandingkan diri dengan bayangan kemampuan pemilik tubuh lama."
        chiasa "{i}Kalau aku terus mencoba meniru garis dari ingatan otot yang nggak pernah kupunya, sampai kapan pun tanganku cuma bakal gemetar ragu di atas kertas.{/i}"
        nar "Kamu membalik ke lembaran bersih di bagian belakang buku sketsa, memilih pensil 2B yang baru diraut, lalu menggeser gelas teh jelai dingin dari Koita ke sebelah kirimu sebagai benda nyata yang benar-benar ada di depan matamu."
        nar "Kamu menyingkirkan niat menggambar jari rumit sekaligus dan mulai dari dasar yang paling sederhana. Silinder gelas, elips tipis permukaan es yang mulai mencair, lalu kerangka balok telapak tangan kirimu sendiri yang kamu angkat sejajar lampu meja."
        chiasa "Oke... percobaan pertama, proporsi ibu jarinya masih kepanjangan dan sudut pergelangannya terlalu miring."
        nar "Kamu menghapusnya perlahan dengan penghapus uli, menurunkan bahumu yang sejak tadi naik tegang, lalu mengingat cara Karuha mengatur tumpuan siku di meja studio agar tarikan garis tidak terputus-putus di tengah jalan."
        nar "Pada percobaan kedua, kerangka telapak mulai terlihat masuk akal, meski ruas jari manisnya masih sedikit terlalu tipis. Kamu membiarkan sketsa kedua itu tetap di kertas tanpa dihapus, lalu langsung mengulang di sisi paling kanan halaman."
        chiasa "Satu kali lagi... tarik dari bahu, tahan pergelangan, jangan ragu di lengkungan buku jarinya."
        nar "Kamu juga menggambar ulang gelas teh jelai di samping telapak tangan itu, mengukur ulang sudut miring bibir gelas dengan ujung pensil agar elipsnya sejajar."
        chiasa "Nah... elips bibir gelasnya akhirnya nggak penyok ke kanan lagi. Sedikit lebih masuk akal sekarang."
        nar "Hampir satu jam berlalu ditemani suara gesekan grafit dan serbuk penghapus yang menumpuk di pinggir meja. Pergelangan tanganmu mulai pegal, dan hasilnya jelas masih terpisah jauh dari keluwesan ilustrasi cetak yang terpajang di rak atas."
        nar "Akan tetapi, saat kamu menjauhkan wajahmu sejengkal dan menatap sketsa tangan ketiga di ujung kanan kertas, garis luarnya tidak lagi terputus ragu. Lengkungan jemarinya berdiri utuh dengan bobot yang jauh lebih mantap daripada sejam lalu."
        nar "Kamu mengambil ponsel, membuka ruang obrolan Miono, lalu mengetik balasan yang jujur tanpa berjanji berlebihan."
        "Pesan Chiasa" "Maaf, Miono-san, bulan Juli ini aku masih fokus penuh buat ujian semester tahun kedua sekaligus merapikan ulang latihan dasarku di studio. Kalau tanganku sudah benar-benar siap untuk jadwal penerbitan baru, nanti langsung kukabari ya."
        nar "Tidak sampai tiga menit, ponselmu bergetar halus menampilkan balasan cepat Miono."
        "Pesan Miono" "Siap banget, Shena-sensei! Sama sekali nggak usah buru-buru kok, kuliah sama kesehatan tangan tetap nomor satu. Kabari aja kapan pun Sensei sudah merasa pas lagi!"
        "Pesan Chiasa" "Terima kasih banyak pengertiannya, Miono-san."
        nar "Jawaban hangat dari Miono membuat beban tenggat komersial yang sejak tadi menekan pundakmu langsung terangkat sepenuhnya."
        nar "Kamu menarik kembali buku sketsa bersampul hitam itu ke tengah meja dan memperhatikan tiga tahapan gambar tangan yang baru saja kamu selesaikan."
        nar "Goresan pensil 2B pada gambar ketiga memang memiliki karakter yang sedikit lebih tegas dan konstruktif dibandingkan gaya almarhumah Chiasa yang serba mengalir."
        nar "Meskipun berbeda, garis itu tidak lagi tampak seperti tiruan yang gagal, melainkan langkah awal dari gaya gambarmu sendiri yang jujur."
        nar "Kamu menuliskan tanggal hari ini dengan huruf kecil di sudut bawah halaman tersebut sebagai penanda dimulainya latihan mandiri tahun keduamu."
        nar "Serpihan penghapus uli yang berserakan di sekitar tatakan gelas kamu kumpulkan dengan hati-hati lalu kamu buang ke keranjang sampah samping meja."
        nar "Berlatih secara bertahap dari anatomi dasar memang membutuhkan kesabaran ekstra, namun cara ini membuatmu tidak perlu berbohong kepada siapa pun di kemudian hari."
        nar "Ketika Karuha atau dosen studio memeriksa buku latihanmu minggu depan, kamu dapat mempertanggungjawabkan setiap tarikan garisnya dengan kepala tegak."
        nar "Suara derik tonggeret dari pepohonan halaman luar terdengar semakin tenang seiring udara bulan Juli yang beranjak lebih sejuk."
        nar "Kamu merapikan pensil-pensil kayumu ke dalam wadah sesuai tingkat ketebalan grafitnya agar siap dipakai kembali esok hari."
        nar "Rasa manis dari potongan melon dingin yang dibawakan Koita menyegarkan tenggorokanmu setelah satu jam penuh berkonsentrasi di depan kertas."
        nar "Dari balik pintu kamar yang tertutup, suara televisi ruang keluarga di lantai bawah terdengar sayup-sayup menghadirkan suasana rumah yang damai."
        nar "Kamu menutup buku sketsa itu dengan hati-hati setelah memastikan goresan pensil pada halaman latihan barumu tidak tercoreng."
        nar "Langkah kecil yang kamu mulai dari konstruksi silinder dan kerangka tangan hari ini telah membebaskanmu dari bayang-bayang rasa takut."
        nar "Esok hari di studio kampus, kamu siap kembali memegang pensil dengan ketenangan yang benar-benar milikmu sendiri."
        nar "Dengan perasaan yang jauh lebih mantap, kamu bersandar di kursi belajar sambil menikmati hasil latihan jujur pertamamu."
        nar "Kamu meletakkan ponsel, mengambil sepotong melon dingin yang tadi dibawakan Koita, lalu menyesap teh jelai sambil kembali memandangi halaman belakang buku sketsa itu. Untuk pertama kalinya hari ini, ada satu halaman di buku bersampul hitam milik Chiasa yang lahir sepenuhnya dari usahamu sendiri."
    elif _return == "B":
        nar "Kamu memandangi halaman penuh bekas hapusan itu selama beberapa detik, lalu meletakkan pensil mekanikmu ke atas meja dengan bunyi pelan. Melatih tangan dari dasar sampai menyamai standar ilustrator profesional memakan waktu berbulan-bulan, sementara redaksi dan pembaca di luar sana mengharapkan nama Shena tetap menghadirkan kualitas yang sama."
        chiasa "{i}Kalau standar yang dicari penerbit itu kualitas garisnya Shena, latihan biasa jelas nggak bakal sempat mengejar kalau proyek baru mendadak turun. Di forum daring pasti ada ilustrator lepas yang tarikan garisnya mendekati.{/i}"
        nar "Kamu menyalakan laptop di sudut meja belajar, membuka beberapa situs portofolio ilustrator lepas, lalu menyaring puluhan galeri satu per satu hingga menemukan satu akun anonim dengan garis tipis yang tajam serta pola bayangan dingin yang paling mendekati jilid-jilid novel milik Shena."
        nar "Kamu membuat akun pemesan baru terpisah tanpa memakai nama asli, nama pena, ataupun alamat surel kampus, lalu membuka jendela pesan langsung dengan ilustrator tersebut."
        "Pesan Chiasa" "Halo. Saya sedang mencari ilustrator lepas untuk mengerjakan satu ilustrasi penuh dan draf desain karakter bergaya garis tipis serta bayangan dingin seperti referensi potongan yang saya lampirkan. Apakah jadwal Anda masih tersedia bulan ini?"
        nar "Sambil menunggu, kamu menutup buku sketsa hitam di samping laptop agar halaman gambar tangan Koita tidak terus menatapmu. Kurang dari sepuluh menit, layar laptop berkedip menandakan balasan masuk."
        "Ilustrator Lepas" "Halo, kebetulan satu slot pengerjaan untuk pertengahan bulan ini baru saja kosong. Gaya bayangan pada contoh referensi Anda memang cukup dekat dengan tarikan biasa saya. Sebelum saya kirim rincian harga, ini untuk koleksi pribadi atau keperluan terbitan komersial?"
        nar "Jemari tanganmu sempat berhenti dua detik di atas papan ketik, sebelum kamu mengetik jawaban yang dingin dan ringkas."
        "Pesan Chiasa" "Untuk keperluan komersial terbatas. Saya membutuhkan kesepakatan lepas hak kredit penuh tanpa pencantuman nama Anda di publikasi, beserta klausul kerahasiaan total. Sebagai gantinya, saya bersedia membayar dua kali lipat dari tarif standar Anda dengan uang muka dikirim hari ini."
        "Ilustrator Lepas" "Dua kali tarif standar untuk kerja lepas kredit ya... terus terang jarang ada pemesan perorangan yang langsung menawarkan angka segitu. Selama sumber referensinya tidak melanggar hak cipta pihak lain dan pembayarannya jelas di muka, saya bersedia menerima."
        "Pesan Chiasa" "Semua rincian komposisi, pose, serta palet warna akan saya kirim lewat tautan tertutup, dan tolong jangan pernah mengunggah draf kasar maupun potongan gambarnya ke portofolio atau media sosial mana pun."
        "Ilustrator Lepas" "Baik, saya paham penuh aturannya dan biasa bekerja dengan kontrak kerahasiaan. Apakah berkas akhirnya ingin dikirim dalam bentuk lapisan terpisah atau gambar akhir menyatu saja?"
        "Pesan Chiasa" "Kirimkan dalam bentuk lapisan terpisah beserta versi akhir resolusi cetak, tanpa menyisipkan catatan nama di metadata berkasnya."
        "Ilustrator Lepas" "Siap, akan saya bersihkan seluruh metadatanya. Begitu bukti transfer uang muka masuk, sketsa awal akan saya kirimkan dalam lima hari."
        nar "Kamu mengirimkan arahan komposisi kasar tanpa sekalipun menyebut nama penerbit, nama Miono, ataupun nama pena Shena, lalu membuka perbankan daring dan mentransfer uang muka dari rekening simpananmu."
        nar "Begitu tanda terima transfer selesai di layar, bahumu sempat turun sedikit lega karena beban di atas meja akhirnya memiliki jalan pintas yang nyata. Akan tetapi, tepat ketika layar ponselmu menyala lagi menampilkan notifikasi lama dari Higashiyama Miono dan terdengar suara langkah santai Koita melintas di lantai bawah, rasa dingin yang asing merayap naik ke tengkukmu."
        chiasa "{i}Membayar keahlian orang lain memang kerja sama yang sah secara transaksi... tapi kalau suatu hari Miono-san, Karuha, atau siapa pun melihat gambarnya dan menanyakan satu pertanyaan sederhana tentang siapa yang sebenarnya menggambar ini, aku bahkan nggak siap menyebut namanya.{/i}"
        nar "Kamu segera menghapus riwayat peramban dan menutup jendela perbankan daring di laptopmu agar tidak meninggalkan jejak jika Koita sewaktu-waktu masuk ke kamar."
        nar "Di ruang obrolan Higashiyama Miono, kamu mengetik pesan singkat bahwa draf kasar untuk proyek paruh kedua akan segera kamu kirimkan dalam waktu dekat."
        nar "Miono langsung membalas dengan deretan stiker antusias yang memuji semangat kerja Shena-sensei di tengah padatnya jadwal kuliah musim panas."
        nar "Pujian tulus yang muncul di layar ponsel itu justru terasa mengganjal ketika kamu melirik buku sketsa hitam yang tertutup rapat di samping siku kirimu."
        nar "Dengan menyerahkan pembuatan ilustrasi tersebut kepada pihak ketiga, kamu memang berhasil mempertahankan citra profesional Shena di mata penerbit."
        nar "Namun pada saat yang sama, kamu baru saja menambahkan satu lapisan kebohongan baru yang harus terus kamu jaga kerahasiaannya setiap bulan."
        nar "Saldo rekening tabungan yang berkurang cukup besar untuk membayar tarif dua kali lipat tadi menjadi harga nyata dari jalan pintas yang kamu ambil."
        nar "Jika suatu saat nanti pihak redaksi mengundangmu hadir dalam rapat tatap muka dan memintamu membuat sketsa revisi di tempat, kamu tidak akan punya tempat bersembunyi."
        nar "Kamu mematikan layar laptopmu perlahan hingga pantulan wajahmu yang tegang di permukaan kaca gelap itu menghilang."
        nar "Potongan melon di dalam mangkuk kecil pemberian Koita tampak sudah mulai hangat karena belum sempat kamu sentuh sejak tadi."
        nar "Kamu menyesap sisa teh jelai yang esnya telah mencair seluruhnya sambil menatap tiga jilid novel strategi di rak atas meja belajar."
        nar "Dalam lima hari ke depan, sketsa pesanan dari ilustrator anonim itu akan masuk ke kotak surat elektronik rahasiamu."
        nar "Kamu harus menyiapkan alasan yang rapi bila sewaktu-waktu Miono menanyakan detail perubahan tipis pada goresan sampul barunya nanti."
        nar "Buku sketsa hitam di atas meja kamu masukkan ke dalam laci paling bawah agar tidak terlihat oleh Koita saat ia masuk mengambil nampan."
        nar "Jalan pintas yang kamu beli dengan uang tabungan itu kini mengikatmu pada sandiwara yang tidak boleh meleset sedikit pun."
        nar "Keheningan kamar lantai dua Rumah Amamiya sore itu terasa menyimpan rahasia yang jauh lebih berisik daripada suara serangga musim panas di luar jendela."
    else:
        nar "Kamu menatap garis-garis kaku di halaman kanan itu sekali lagi, meletakkan pensil mekanikmu kembali ke dalam wadah kayu di sudut meja, lalu menutup sampul hitam tebal buku sketsa tersebut perlahan."
        chiasa "{i}Percuma dipaksakan sekarang. Makin lama aku duduk memandangi perbandingan dua halaman itu, kepalaku malah makin buntu.{/i}"
        nar "Kamu meraih ponsel dari samping gelas teh, membuka ruang obrolan Higashiyama Miono, lalu mengetik balasan yang sopan dan tenang."
        "Pesan Chiasa" "Halo, Miono-san, terima kasih banyak kabarnya soal cetakan ulang kemarin. Untuk paruh kedua tahun ini, karena jadwal ujian semester dan kegiatan tahun kedua di kampus cukup padat, aku memutuskan beristirahat dulu dari seluruh tawaran proyek ilustrasi baru ya."
        nar "Beberapa menit kemudian, ponselmu bergetar pendek menampilkan balasan ramah dari Miono."
        "Pesan Miono" "Siap, Shena-sensei! Sama sekali nggak apa-apa kok, kuliah dan waktu istirahat tetap nomor satu. Tenang saja, royalti cetak ulang dari jilid sebelumnya tetap masuk tiap bulan seperti biasa tanpa syarat apa pun."
        "Pesan Miono" "Cuma... kalau suatu saat nanti Sensei kangen menggambar sampul lagi atau punya sketsa iseng yang ingin ditunjukkan, pintu redaksi dan para pembaca masih selalu nungguin karya baru Sensei ya!"
        nar "Kamu meletakkan ponsel menghadap ke bawah di atas meja, lalu mengangkat gelas teh jelai dingin pemberian Koita dan meminumnya perlahan sampai embun di dinding kaca membasahi ujung jarimu. Di sebelah buku sketsa, buku catatan teori sejarah seni yang besok hendak kamu baca ulang bersama Karuha masih menunggu dibuka."
        chiasa "{i}Ujian tulis teori masih bisa kukejar pakai kepalaku sendiri. Urusan menggambar biar kupikirkan lagi nanti kalau kepalaku sudah lebih dingin.{/i}"
        nar "Dari lantai bawah terdengar suara santai Koita memanggil ke arah tangga."
        koita "Chi-chan! Aku baru mau potong sisa semangka dingin dari kulkas buat camilan, kamu mau turun istirahat sebentar nggak?"
        chiasa "Iya, sebentar lagi aku turun, Ko-nii!"
        nar "Kamu menggeser buku sketsa bersampul hitam itu ke tepi rak bawah meja belajar agar tidak terus menyita pikiranmu sepanjang pekan ujian."
        nar "Sebagai gantinya, kamu menarik buku catatan teori sejarah seni dan menaruhnya tepat di tengah meja di bawah sorot lampu baca."
        nar "Menolak tawaran proyek baru dari Miono untuk sementara waktu memang menghentikan peluang pemasukan tambahan dari sampul paruh kedua."
        nar "Meski demikian, royalti lima puluh ribu yen dari cetakan ulang jilid lama yang tetap mengalir setiap bulan sudah lebih dari cukup untuk kebutuhan harianmu."
        nar "Keputusan untuk berhenti memaksakan diri hari ini menghindarkanmu dari risiko mengirim karya buruk yang dapat menghancurkan reputasi Shena."
        nar "Kamu membersihkan sisa serbuk penghapus dari permukaan kayu meja belajar menggunakan saputangan kecil hingga kembali rapi."
        nar "Di lantai bawah, terdengar suara Koita yang sedang menyiapkan piring buah di dapur sambil bersenandung ringan."
        nar "Kehangatan rumah ini memberikan tempat berlindung yang aman selagi kamu mengatur ulang prioritas hidupmu di tahun kedua kuliah."
        nar "Kamu menghabiskan potongan melon terakhir di mangkuk kecilmu lalu mengangkat nampan gelas kosong itu dengan kedua tangan."
        nar "Meskipun persoalan kemampuan menggambar ini belum benar-benar terselesaikan, kamu telah membeli waktu istirahat yang jujur tanpa menambah kebohongan baru."
        nar "Kamu mematikan kipas angin kecil di pojok ruangan sebelum melangkah menuju pintu kamar untuk turun ke ruang keluarga."
        nar "Higashiyama Miono pun telah menerima keputusan jedamu dengan lapang dada tanpa memberikan tekanan tenggat sedikit pun."
        nar "Sepanjang pekan ujian bulan Juli ini, kamu dapat memusatkan seluruh tenagamu pada mata kuliah studio dan teori bersama Karuha."
        nar "Nampan berisi gelas kosong dan mangkuk buah itu kamu bawa dengan langkah ringan menuruni anak tangga kayu Rumah Amamiya."
        nar "Udara sore yang hangat menyambutmu dari arah ruang makan tempat Koita sudah menunggu dengan potongan semangka dingin."
        nar "Sebelum bangkit dari kursi kayu itu, pandanganmu sempat terhenti pada tiga jilid novel strategi bersampul mengilap di rak atas yang berdiri rapi dengan nama Shena tercetak jelas di punggungnya. Menutup buku sketsa hari ini memberimu ruang bernapas yang tenang tanpa memaksamu membuktikan apa pun, meski kamu tahu suatu hari nanti seseorang pasti akan meminta melihat proses gambar barumu secara langsung."
    return

init 1 python:
    def kk_take_cover_project():
        kk_flag("proyek_mio_diterima")
        pts.setdefault("shena_risiko",20)
        kk_adj("shena_risiko",10)

    def kk_practice_sketch(place):
        if not kk_can_sketch(place):
            return
        kk_adj("kemampuan_gambar", 1 if kk_kelelahan_tier()[1] >= 2 else 3)
        pts.setdefault("shena_risiko",20)
        kk_adj("shena_risiko",-1)
        kk_minutes(60)

    _hook("C05-B", kk_take_cover_project)
    _hook("C05-C", lambda: kk_flag("haruka_dimintai_bantuan"))
    _hook("C09-A", lambda: kk_adj("kemampuan_gambar",5))
    def kk_commission_secret():
        kk_flag("ilustrasi_dikerjakan_orang_lain")
        pts.setdefault("shena_risiko",20)
        kk_adj("shena_risiko",10)

    _hook("C09-B", kk_commission_secret)

# ┌─ PANDUAN CERITA · C-D03 · Tangan yang Gemetar
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Chiasa
# │ AWALAN  : Chiasa host; berlatih saat Sangat Lelah
# │ INTI    : A berhenti dan tidur / B paksa sampai pagi / C minta Karuha mengajar
# │ AKHIRAN : kemampuan_gambar hanya naik sedikit saat lelah; tubuh menanggung
# └─ tulis / perbaiki dialog di bawah ──
label kk_draw_at_home:
    if not kk_can_sketch(_lokasi):
        return
    if kk_shaking_hands():
        nar "Lampu meja belajar menyinari kertas sketsa yang sudah penuh bekas hapus sampai permukaannya mulai berbulu. Ujung pensil mekanik di tangan kananmu bergetar halus begitu menyentuh kertas, meski pergelangan tanganmu sudah ditekan rapat ke tepi meja kayu."
        nar "Kamu menarik satu garis rahang lagi, lalu berhenti di tengah lengkungan. Kepalamu terasa berat dan kosong sekaligus sampai kamu lupa ke arah mana bayangan bahu itu tadi hendak ditarik."
        chiasa "{i}Ayolah... cuma satu lengkungan bahu. Kenapa jari-jariku nggak mau ikut gerak lurus sih...{/i}"
        nar "Pintu kamar diketuk pelan dua kali dari lorong sebelum suara Koita terdengar agak teredam."
        koita "Chi-chan? Lampu kamarmu masih nyala terang banget. Kamu belum mau istirahat? Tadi waktu pulang wajahmu sudah kelihatan pucat lho."
        chiasa "Bentar lagi, Ko-nii. Aku cuma mau beresin satu halaman sketsa ini dulu biar nggak kepikiran."
        koita "Jangan dipaksakan sampai ketiduran di meja ya. Kalau butuh teh hangat atau mau berhenti, aku masih di ruang bawah sebentar."
        nar "Langkah Koita menjauh pelan di lorong. Kamu kembali menatap kertas di depanmu. Rasa kesal datang lebih cepat daripada rasa kantuk saat kamu sadar tubuh ini sudah kehabisan tenaga untuk menuruti tuntutan yang kamu bebankan sejak tadi."
        call kk_family_menu("C-D03", ["Letakkan pensil dan beristirahat.", "Teruskan sampai pagi.", "Singkirkan kertasnya dan minta Karuha mengajarimu."])
        if _return == "A":
            nar "Kamu menatap goresan terakhir yang miring itu selama dua detik, lalu menjatuhkan pensil mekanik ke samping penghapus uli sebelum ujungnya kembali menggores kertas."
            chiasa "{i}...Cukup buat hari ini. Kalau kupaksakan juga hasilnya cuma bakal bikin aku makin kesal besok.{/i}"
            nar "Kamu membuka pintu kamar sedikit dan memanggil ke arah tangga."
            chiasa "Ko-nii, nggak jadi begadang. Aku mau langsung tidur aja."
            koita "Nah, gitu dong! Syukurlah kamu dengerin badan sendiri. Sudah makan malam tadi kan? Minum air dulu sebelum tidur ya, Chi-chan."
            chiasa "Iya, Ko-nii. Selamat malam."
            koita "Selamat malam. Besok pagi kubangunkan agak siangan kalau kuliahmu nggak terlalu pagi."
            nar "Kamu menutup pintu dan mematikan lampu meja. Berhenti di tengah halaman kosong sempat terasa seperti kekalahan kecil, sampai bahumu perlahan mengendur di atas kasur dan kamu sadar tubuh ini juga bagian dari hidup yang sedang kamu tanggung."
            call kk_rest_home
            return
        elif _return == "B":
            $ kk_adj("kemampuan_gambar",1)
            $ kk_minutes((6 - kk_slot)*240 - kk_minute)
            chiasa "{i}Sedikit lagi. Kalau sekarang berhenti, besok tanganku bakal kaku lagi dari awal...{/i}"
            nar "Kamu memutar ulang lembar kertas buram, mengulang bentuk tangan dan garis bahu puluhan kali di bawah lampu kuning yang terasa makin menyilaukan mata. Jam dinding berdetak melewati tengah malam tanpa terasa, menyisakan serbuk penghapus berserakan di seluruh sudut meja."
            nar "Ketika cahaya pucat pagi akhirnya merembes melewati celah tirai, kelopak matamu terasa perih dan lehermu kaku. Kamu harus mencondongkan wajah dekat sekali ke kertas hanya untuk membedakan garis mana yang sedikit membaik dari coretan kabur hasil kantuk."
            nar "Dari lantai bawah terdengar bunyi panci sup dan langkah Koita di dapur. Beberapa menit kemudian, pintu kamarmu terbuka perlahan."
            koita "Chi-chan, sarapannya sudah... lho? Kamu beneran nggak tidur semalaman?"
            chiasa "Eh... aku cuma keasyikan latihan garis, Ko-nii. Tadi tinggal sedikit lagi selesai."
            koita "Ya ampun, Chi-chan, lihat kantung matamu itu! Pensilnya bahkan masih nempel di jari. Sudah, sekarang cuci muka dulu, terus turun makan yang hangat. Buku sketsanya jangan disentuh dulu hari ini."
            chiasa "Iya... maaf bikin kamu khawatir, Ko-nii."
            nar "Kamu tetap duduk beberapa detik setelah Koita keluar, menatap tumpukan kertas buram yang terasa dingin. Malam panjang yang baru saja kamu habiskan memang meninggalkan sedikit perbaikan garis, tetapi belum juga mengubah tanganmu menjadi milik Shena."
            return
        else:
            $ kk_flag("haruka_dimintai_bantuan")
            $ kk_minutes(5)
            nar "Kamu menggeser buku sketsa itu menjauh ke pinggir meja, lalu meraih ponselmu yang tergeletak di samping kotak pensil. Daripada terus bertengkar dengan kertas kosong sendirian, kamu membuka ruang obrolan Ishikawa Karuha dan mengetik pesan singkat yang jujur."
            chiasa "Karuha, maaf mengganggu malam-malam. Tanganku lagi kaku banget waktu latihan sketsa di rumah sampai buntu total. Besok atau lain waktu kalau kamu senggang di studio, boleh nggak kamu ajarin aku lagi dari tarikan garis dasar?"
            nar "Kamu mengirim pesan itu tanpa berusaha menyembunyikan bahwa kemampuanmu sedang jatuh jauh. Beberapa puluh detik kemudian, layar ponselmu menyala dengan getaran pendek."
            play sound "audio/sfx/phone_buzz.wav"
            "Pesan Karuha" "Eh, kamu masih melek jam segini sambil latihan? Tanganmu gemetar karena capek banget kali, Chiasa!"
            "Pesan Karuha" "Boleh banget dong, tentu aja aku mau ajarin! Tapi syarat pertama dari guru dadakanmu sekarang satu aja, tutup bukunya, cuci muka, terus langsung tidur!"
            chiasa "Siap, Sensei. Bukunya sudah kugeserin kok dari depan mataku."
            play sound "audio/sfx/phone_buzz.wav"
            "Pesan Karuha" "Bagus! Nanti kalau kita ketemu di studio sore, bawa aja sketsa yang bikin kamu buntu malam ini. Kita bedah pelan-pelan bareng, nggak usah dikebut sendirian kayak mau dikejar tenggat penerbitan."
            chiasa "Makasih banyak ya, Karuha. Selamat istirahat."
            nar "Kamu meletakkan ponsel dengan napas jauh lebih lapang. Kamu meminta dia mengajarimu dari bawah tanpa menyuruhnya mengambil alih gambar atas namamu, dan ternyata pelajaran pertamanya dimulai dari berhenti sebelum rasa kesal pada diri sendiri menguasai seluruh meja kerja."
            return
    $ kk_practice_sketch(_lokasi)
    nar "Kamu meraut ujung pensil kayu, menarik napas tenang, lalu menyisihkan satu jam penuh untuk melatih bentuk dasar kubus, lengkungan bahu, dan proporsi jari di atas lembaran kertas baru."
    chiasa "{i}Yang bagian ibu jari tadi masih terlalu kaku... nah, kalau sudut pergelangannya digeser sedikit begini, arahnya lebih masuk akal.{/i}"
    nar "Kamu menandai lengkungan yang masih ragu dengan lingkaran tipis dan menulis tanggal hari ini di pojok kanan atas halaman. Perkembangannya memang masih kecil. Meski begitu, catatan tanggal itu membuat setiap garis terasa nyata sebagai milikmu sendiri yang boleh tumbuh dari awal."
    return

# ┌─ PANDUAN CERITA · C-D07 · Pesan Miono Jam Sebelas
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Chiasa
# │ AWALAN  : Chiasa host; ada proyek
# │ INTI    : A mengaku tidak sanggup / B minta perpanjangan / C sewa ilustrator / D begadang
# │ AKHIRAN : menyewa = kebohongan baru yang bisa ditemukan Shiori; begadang = tubuh dan kemampuan
# └─ tulis / perbaiki dialog di bawah ──
label kk_mio_deadline:
    if not kk_mio_message():
        return
    play sound "audio/sfx/phone_buzz.wav"
    nar "Jarum jam dinding di kamarmu baru saja menyentuh angka sebelas malam ketika ponsel di sebelah buku sketsa bergetar singkat. Nama Higashiyama Miono muncul di layar notifikasi."
    "Pesan Miono" "Selamat malam, Shena-sensei. Maaf mengirim pesan selarut ini. Saya cuma ingin menanyakan perkembangan sketsa kasar sampul jilid keempat sesuai jadwal redaksi minggu ini. Apakah sudah ada bagian yang bisa saya periksa besok pagi?"
    nar "Tidak ada tanda seru ataupun nada mendesak dalam pesan itu. Kesopanan Miono yang rapi justru menekan dadamu lebih berat. Di pihaknya ada tim tata letak, penulis novel, dan jadwal percetakan yang menunggu, sementara di atas mejamu tergeletak lembaran sketsa kaku yang bahkan kamu sendiri ragu memotretnya."
    chiasa "{i}Sudah jam sebelas malam... Miono-san pasti baru selesai lembur merapikan jadwal cetak.{/i}"
    nar "Kamu menatap kursor balasan yang berkedip pelan di layar ponsel, menimbang kejujuran macam apa yang sanggup kamu tanggung malam ini."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Akui bahwa kamu kesulitan mengerjakannya.", "Minta waktu tambahan.", "Cari ilustrator lain untuk menyelesaikannya.", "Buka sketsanya dan lanjutkan sampai pagi."])]
    call screen kk_choice_panel(_rows, "Pesan Miono")
    $ kk_record_choice("C-D07", _return)
    if _return == "A":
        chiasa "Selamat malam, Miono-san. Maaf banget aku harus jujur malam ini. Aku benar-benar lagi kesulitan menuntaskan sketsa sampulnya, dan hasil yang ada di mejaku sekarang jauh di bawah standar yang kujanjikan."
        nar "Jari-jarimu sempat dingin setelah menekan tombol kirim. Indikator mengetik di sisi Miono muncul, hilang sebentar, lalu muncul lagi sebelum dua balasan masuk berurutan."
        play sound "audio/sfx/phone_buzz.wav"
        "Pesan Miono" "Terima kasih sudah jujur lebih awal daripada mendadak menghilang pas hari cetak, Sensei. Boleh saya tahu bagian mana yang paling membuat macet sekarang? Komposisi latarnya atau ekspresi tokoh panglimanya?"
        chiasa "Dua-duanya masih terasa kaku banget, Miono-san. Proporsi gerak tangannya nggak keluar seperti yang kubayangkan waktu baca naskahnya."
        play sound "audio/sfx/phone_buzz.wav"
        "Pesan Miono" "Baik, saya catat dulu ya. Besok sore bisa kirim foto sketsa paling mentahnya saja ke surel saya? Nanti kita cek bareng bagian mana yang bisa disederhanakan komposisinya, atau apakah kita perlu menjadwalkan ulang tenggat tim desain."
        chiasa "Bisa, Miono-san. Maaf sekali lagi sudah bikin jadwal redaksi terganggu."
        "Pesan Miono" "Yang penting sekarang masalahnya sudah ditaruh di atas meja jadi bisa kita cari jalan keluarnya bareng. Istirahat dulu malam ini ya, Sensei."
        nar "Kamu menaruh ponsel dengan helaan napas panjang. Masalahnya belum hilang, tetapi setidaknya kini berada di antara dua orang yang saling bicara alih-alih terus berputar menyesakkan di dalam kepalamu sendiri."
    elif _return == "B":
        chiasa "Selamat malam, Miono-san. Maaf sekali, sketsa kasarnya belum siap dikirim besok pagi karena beberapa bagian masih kurombak ulang. Boleh aku minta perpanjangan waktu sekitar lima hari sampai satu minggu?"
        nar "Pesan itu langsung terbaca, tetapi tidak ada balasan selama hampir dua menit penuh. Kamu memandangi layar yang redup, baru benar-benar menyadari bahwa tambahan waktu yang kamu minta berarti Miono harus menegosiasikan ulang jadwal desainer sampul dan percetakan."
        play sound "audio/sfx/phone_buzz.wav"
        "Pesan Miono" "Saya baru cek kalender produksi dengan kepala redaksi untuk cadangan cetak bulan depan. Kalau mundur maksimal enam hari dari besok, masih bisa saya geserkan slot tata letaknya, Sensei."
        "Pesan Miono" "Cuma setelah tanggal itu sudah masuk kunci percetakan, jadi saya benar-benar butuh draf komposisi paling lambat hari keenam ya, Sensei. Masih memungkinkan?"
        chiasa "Iya, Miono-san. Terima kasih banyak sudah bantu menggeser jadwalnya. Dalam enam hari ini kupastikan draf komposisinya sudah rapi dan langsung kukirim."
        "Pesan Miono" "Baik, saya pegang janjinya ya, Sensei. Kalau di tengah jalan ada kendala lagi, kabari lebih cepat biar saya sempat atur ulang dari pihak redaksi."
        nar "Kamu membaca ulang pesan terakhir Miono sampai habis tanpa mencari pembelaan diri. Enam hari terasa seperti ruang bernapas yang rapuh sekaligus hitungan mundur yang sangat nyata."
    elif _return == "C":
        chiasa "{i}Kalau kuminta orang lain yang lebih mahir buat meneruskan draf kasar ini... nggak, Miono-san cukup dapat file rapi sesuai jadwal.{/i}"
        nar "Kamu membalas pesan Miono dengan kalimat singkat bahwa sketsa masih dalam tahap penyempurnaan akhir dan akan dikirim dalam dua hari, lalu segera beralih ke forum pekerja lepas ilustrasi yang sempat kamu tandai."
        nar "Kamu mengirim pesan pribadi ke salah satu ilustrator lepas yang gayanya paling mendekati arsiran tipis Shena, menawarkan bayaran penuh untuk merapikan draf sampul dalam waktu singkat."
        play sound "audio/sfx/phone_buzz.wav"
        "Ilustrator Lepas" "Halo, saya sudah lihat contoh komposisi dan kisaran honornya. Dengan referensi gaya arsir yang diminta, saya sanggup selesaikan dalam tiga hari kalau naskah ringkasnya dikirim malam ini."
        chiasa "Bagus banget. Honornya bisa langsung kutransfer setengah di muka malam ini juga."
        play sound "audio/sfx/phone_buzz.wav"
        "Ilustrator Lepas" "Siap, sebelum kita mulai, saya mau pastikan dulu soal kontraknya. Nanti nama saya dicantumkan sebagai asisten kredit di halaman hak cipta penerbit, atau ini sifatnya pengalihan hak penuh tanpa kredit?"
        nar "Jari-jarimu membeku di atas layar. Kamu mengetik balasan kaku bahwa proyek ini bersifat tertutup tanpa pencantuman nama tambahan, dan langsung mentransfer uang muka begitu pihak sana mengiyakan."
        nar "Ada kelegaan dingin melihat jadwal tampak terselamatkan, tetapi kamu sadar betul bahwa setiap bantuan yang dibeli di atas kebisuan hanya menambah satu orang lagi yang kelak bisa merasa diperalat."
    else:
        $ kk_adj("kemampuan_gambar",1 if kk_kelelahan_tier()[1] >= 2 else 3)
        $ kk_minutes((6 - kk_slot)*240 - kk_minute)
        chiasa "Selamat malam, Miono-san. Sketsanya tinggal tahap perapian akhir malam ini, besok pagi sekitar jam tujuh pasti sudah masuk ke surel Miono-san."
        play sound "audio/sfx/phone_buzz.wav"
        "Pesan Miono" "Eh, tidak usah begadang sampai sakit ya, Sensei! Siang pun masih sempat kok kalau memang perlu istirahat."
        chiasa "Nggak apa-apa, Miono-san, memang tinggal sedikit lagi biar alurnya nggak terputus."
        nar "Kamu mematikan dering ponsel, menarik lampu meja lebih rendah, dan memaksa matamu tetap terbuka menghadapi komposisi panglima di atas peta perang. Pensil berganti pulpen gambar, penghapus habis setengah batang, dan teh dingin di gelas sudah tak lagi bersisa."
        nar "Ketika langit di luar jendela mulai membiru pucat dan suara burung pagi terdengar samar, akhirnya ada satu lembar sketsa kasar yang cukup utuh untuk difoto dan dikirimkan ke alamat surel redaksi."
        chiasa "{i}...Terkirim. Akhirnya kekirim juga.{/i}"
        nar "Kamu menyandarkan dahi ke tepi meja, terlalu letih untuk merasakan lega. Pesan balasan terima kasih dari Miono mungkin akan datang beberapa jam lagi, diikuti permintaan revisi tahap berikutnya yang tidak akan menjadi lebih ringan hanya karena malam ini berhasil kamu habiskan tanpa tidur."
        return
    $ kk_minutes(5)
    return

init 1 python:
    _hook("C-D07-A", lambda: kk_flag("mio_tahu_kesulitan"))
    _hook("C-D07-B", lambda: kk_flag("perpanjangan_diminta"))
    _hook("C-D07-C", kk_commission_secret)

# ┌─ PANDUAN CERITA · C-D02 · Dua Sketsa Berdampingan
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Chiasa
# │ AWALAN  : Chiasa host; shena_risiko ≥ 40
# │ INTI    : A Jujur / B beri alasan / C minta Karuha mengajar
# │ AKHIRAN : rahasia Shena dibagi, atau curiga naik
# └─ tulis / perbaiki dialog di bawah ──
label kk_show_portfolio:
    if not kk_art_studio_open(_lokasi):
        return
    if kk_comparison_due():
        nar "Cahaya sore dari jendela tinggi Gedung Seni Rupa memanjang di atas meja kayu studio yang mulai sepi. Ishikawa Karuha tidak langsung memberi komentar ketika kamu menyerahkan map tugasmu."
        nar "Sebaliknya, ia mengeluarkan selembar salinan sketsa lama Chiasa dari map referensi klub dan meratakannya persis di sebelah lembar gambar yang baru kamu kerjakan minggu ini."
        "Karuha" "Chiasa, bentar deh. Coba kamu lihat dua lembar ini sebelahan."
        chiasa "Eh... itu kan sketsa lama dari semester awal waktu aku baru masuk studio?"
        "Karuha" "Iya, dan aku nggak lagi bilang gambarmu sekarang jelek atau menurun lho ya. Cuma... cara tanganmu nyari bentuk di lembar baru ini beda total dari lembar yang kiri."
        nar "Karuha mengetuk pelan sudut bahu dan tarikan jari pada sketsa lama dengan ujung pensil tumpulnya. Tatapannya jernih, penuh rasa ingin tahu yang tulus, dan justru karena ia sangat hafal kebiasaan gambar Chiasa, alasan klise apa pun mendadak terasa tipis sekali."
        "Karuha" "Dulu kamu selalu mulai dari satu garis siluet panjang tanpa angkat pensil, terus baru isi bayangan. Di sini, semua bentuknya kamu bangun dari kotak kecil dan garis pendek yang diulang berkali-kali. Ada sesuatu yang lagi terjadi ya sama kamu, Chiasa?"
        call kk_family_menu("C-D02", ["Ceritakan terus terang kenapa sketsa itu berbeda.", "Beri alasan untuk perbedaan itu.", "Minta ia mengajarimu membuat garis itu lagi."])
        if _return == "A":
            chiasa "...Karuha, tolong jangan potong dulu ya kalau aku bilang sesuatu yang terdengar aneh. Kamu pernah dengar nama ilustrator Shena di novel strategi itu?"
            "Karuha" "Shena? Pernah banget dong! Aku malah punya dua jilid bukunya di rak asrama. Tunggu... garis siluet tipis itu... jangan bilang selama ini..."
            chiasa "Iya, nama pena itu punyaku. Tapi belakangan ini tanganku beneran nggak sanggup lagi ngejar standar gambar lama itu. Rasanya ada jarak gede banget antara nama yang dikenal pembaca sama kemampuanku yang sekarang, dan aku nggak mau terus-terusan bohong di depan kamu."
            nar "Karuha terdiam cukup lama sambil menatap kedua lembar kertas itu bergantian. Ia tidak lantas menyebutmu palsu, tidak pula terburu-buru menawarkan diri membereskan pekerjaanmu."
            "Karuha" "Wah... jujur aja aku kaget banget dengarnya. Pantas aja akhir-akhir ini kamu kelihatan tertekan banget tiap kali orang muji gambarmu."
            chiasa "Kamu marah ya karena aku baru cerita sekarang?"
            "Karuha" "Nggak marah kok. Aku cuma bingung mau bantu dari mana kalau nggak tahu batasnya. Sekarang aku tanya satu hal aja deh, Chiasa. Tanpa bawa-bawa nama Shena atau gambar lama itu, bagian mana yang sekarang beneran sanggup kamu kerjakan sendiri?"
            chiasa "...Konstruksi bentuk dasar sama latihan ulang dari nol. Pelan, tapi itu yang sekarang bisa kulakukan."
            "Karuha" "Oke. Kalau begitu kita pegang itu dulu, dan soal nama penamu nggak bakal kubocorkan ke siapa-siapa di kampus. Janji."
            nar "Pertanyaan Karuha terasa menohok di bagian yang paling kamu takuti. Meski begitu, untuk pertama kalinya kamu merasa punya tempat pijakan yang jujur di ruang studio ini."
        elif _return == "B":
            chiasa "Oh, itu... akhir-akhir ini pergelangan tanganku sering pegal gara-gara kebanyakan tugas, Karuha. Jadi aku lagi coba ganti metode latihan pakai garis pendek biar nggak cepat capek."
            nar "Alasan itu terdengar cukup rapi dan masuk akal bila didengar sepintas. Karuha tidak langsung membantah, tetapi ia juga tidak langsung mengangguk puas."
            "Karuha" "Pergelangan tangan ya... padahal tekanan arsir di lembar barumu ini malah kelihatan lebih keras dibanding yang lama lho, Chiasa. Kalau lagi pegal, biasanya orang justru makin ringan nekan pensilnya."
            chiasa "Mungkin karena aku belum terbiasa aja sama posisi pegang pensil yang baru, jadi tenaganya masih suka kelebihan."
            "Karuha" "...Hm, gitu ya. Aku tadi nanya bukan buat nyari salahmu kok, beneran cuma pengin bantu kalau kamu lagi buntu."
            chiasa "Iya, aku tahu kok, Karuha. Makasih ya sudah perhatiin detail banget."
            nar "Karuha tersenyum tipis lalu mengembalikan map referensinya perlahan, membiarkan alasanmu tetap tergeletak di atas meja, berdampingan dengan dua lembar gambar yang diam-diam tidak sepenuhnya mendukung kata-katamu."
        else:
            chiasa "Karuha... jujur aja, aku nggak tahu kenapa akhir-akhir ini tanganku nggak bisa lagi narik garis sehalus yang kiri. Kalau aku minta kamu ajarin aku dari bagian paling dasar lagi, mulai dari garis panjang sama proporsi, kamu mau nggak?"
            nar "Karuha berkedip pelan, lalu raut tegang di wajahnya melunak seketika. Ia menggeser dua sketsa pembanding itu ke pinggir dan menarik selembar kertas karton putih yang masih bersih ke tengah meja."
            "Karuha" "Boleh banget, Chiasa. Tapi aku mau tanya satu hal dulu sebelum kita mulai. Kamu beneran siap nggak kalau selama latihan aku koreksi langsung tanpa banding-bandingin hasilmu sama gambar lama di sebelah itu?"
            chiasa "Iya, aku justru penginnya begitu. Anggap aja aku lagi mulai belajar ulang dari langkah pertama."
            "Karuha" "Sepakat kalau begitu! Sini, geser kursimu lebih dekat. Pertama-tama lemesin bahumu dulu, jangan cuma gerakin jari waktu bikin garis lengkung. Coba ikutin gerak tanganku di udara dulu tiga kali."
            chiasa "Kayak begini? Eh, bahunya ikut turun sedikit ya?"
            "Karuha" "Nah, bener! Sekarang sentuhin pensilnya tipis aja ke kertas. Jangan takut salah, kertas latihan kita masih banyak di lemari belakang."
            nar "Menjadi murid di depan teman yang sebelumnya mengagumi karya lama Chiasa sempat membuat telingamu panas. Meski begitu, rasa lega yang mengalir saat pensilmu mulai meluncur lebih lepas terasa jauh lebih besar."
    else:
        nar "Cahaya sore jatuh miring di meja studio. Karuha membentangkan lembar latihan yang kamu bawa dari rumah, lalu memiringkan kepala sambil memeriksa setiap sudut gambar dengan teliti tanpa membandingkannya dengan karya lama mana pun."
        "Karuha" "Hei, lihat bagian lipatan kain sama sudut dagu yang ini deh, Chiasa! Garismu jauh lebih konsisten dibanding minggu lalu lho."
        chiasa "Beneran? Padahal bagian bayangan di lehernya masih agak ragu tadi waktu kuarsir."
        "Karuha" "Iya, bagian lehernya memang masih agak malu-malu nekan pensilnya. Coba di sini kamu kasih satu garis tegas buat misahin dagu sama bayangan, nanti volumenya langsung kerasa."
        chiasa "Oh, di sebelah sini ya? Bentar, kucatat dulu di pinggir kertas biar nggak lupa pas latihan di rumah."
        "Karuha" "Catat sekalian arah datang cahayanya ya. Enak deh ngobrolin proses gambar yang beneran lagi dikerjain di depan mata begini, rasanya jadi ikut semangat ngerjain tugasku sendiri."
        nar "Kamu menulis catatan koreksi kecil di tepi kertas dengan pensilmu, menikmati obrolan jujur tentang pekerjaan yang benar-benar lahir dari tanganmu sendiri."
    if kk_has("haruka_dimintai_bantuan") or kk_get("kemampuan_gambar") >= 30:
        $ kk_adj("kemampuan_gambar",3)
        $ pts.setdefault("shena_risiko",20)
        $ kk_adj("shena_risiko",-1)
    $ kk_minutes(60)
    return

# ┌─ PANDUAN CERITA · C11 · Pameran Kecil dan Shiori
# │ LOKASI  : Kampus Kouseikan · Gedung Seni Rupa & Studio
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : Shiori datang ke pameran; ia pembaca Shena.
# │ INTI    : A mengaku / B pura-pura tidak tahu / C beri tanda tangan.
# │ AKHIRAN : jembatan ke Shiori atau perangkap (Rute Revenge jika kebohongan).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C11:
    call kk_scene_enter("shiori","Pameran seni · Studio")
    nar "Cahaya sore akhir pekan bulan November masuk miring melalui deretan jendela tinggi ruang galeri lantai dua Gedung Seni Rupa. Aroma kertas cetak, cat akrilik yang sudah kering, serta teh hangat dari meja tamu bercampur pelan bersama dengung obrolan para pengunjung."
    nar "Deretan panel putih berdiri sejajar memamerkan karya akhir pekan mahasiswa Seni Rupa dan Desain. Di dekat pintu masuk, Ishikawa Karuha sibuk merapikan tumpukan katalog tipis sambil menyapa beberapa pengunjung yang baru naik dari tangga utama."
    "Karuha" "Chiasa, barisan pengunjung sore mulai agak melonggar nih. Tadi lumayan banyak yang berhenti lama di depan panel tengahmu lho."
    chiasa "Yang sebelah kiri itu kan arsip lama yang diminta dosen buat dipajang bareng sketsa baruku, Karuha. Aku malah agak deg-degan tiap ada yang memperhatikan terlalu dekat."
    "Karuha" "Santai aja, komentarnya bagus-bagus semua kok. Aku turun sebentar ambil tambahan brosur di ruang cetak ya, tolong jaga meja buku tamu sama sudut panel tengah sebentar."
    chiasa "Siap, Karuha. Ambil pelan-pelan aja, di atas sini sudah aman kok."
    nar "Kamu merapikan pita hitam yang mengikat rambut cokelat gelapmu setengah ke atas, memeriksa pena di meja buku tamu yang sempat miring, lalu melangkah mendekati panel tengah tempat karyamu digantung. Di sana terpasang ilustrasi studi karakter berlatar jendela ruang baca dari arsip lama Chiasa, berdampingan dengan satu lembar sketsa tanganmu sendiri."
    nar "Dua pengunjung dari fakultas lain sempat berhenti di depan panel itu, membaca kartu judul kecil bertuliskan nama Amamiya Chiasa, lalu berbisik-bisik pelan sebelum bergeser ke lukisan cat minyak di sudut kanan."
    "Pengunjung Pameran" "Goresan bayangan di jendela yang kiri rapi banget ya. Berasa kayak ilustrasi sampul novel yang sering dipajang di toko buku stasiun."
    "Teman Pengunjung" "Iya, padahal baru tingkat dua kan yang bikin? Ayo lihat panel instalasi kain di ujung sana juga."
    nar "Begitu keduanya menjauh, satu sosok yang sangat tidak kamu sangka akan muncul di pameran kecil fakultas seni melangkah tenang melewati ambang pintu galeri."
    nar "Saionji Shiori mengenakan mantel warna gading potong rapi di atas gaun gelap sederhana. Rambut putih keperakan panjang bergelombangnya berhiasan jepit mutiara ungu-emas tampak kontras di bawah sorot lampu galeri yang hangat."
    nar "Ia berjalan santai tanpa memancing perhatian kerumunan, melewati tiga panel pertama dengan tatapan sopan, lalu berhenti cukup lama tepat di depan panel gambarmu. Ia tidak langsung menoleh mencari siapa penjaga ruangannya; matanya menyusuri sudut garis tinta dan komposisi ruang dengan ketelitian penuh."
    nar "Kamu sempat mengira ia hanya melintas mampir melihat kegiatan Festival Seni. Namun ketika langkah kakimu berbunyi pelan mendekati sisi panel, Shiori sama sekali tidak memanggil pengunjung lain ataupun memperlihatkan ekspresi terkejut."
    shiori "Selamat sore, Amamiya-san. Panelmu lumayan ramai dikerumuni orang dari tadi."
    chiasa "Eh, Saionji-senpai?! Tumben banget Senpai mampir sampai ke galeri Fakultas Seni akhir pekan begini."
    shiori "Kebetulan rapat evaluasi klub catur di gedung sebelah baru selesai. Kudengar jurusanmu buka pameran, jadi sekalian saja aku mampir melihat-lihat."
    nar "Ia mencondongkan tubuh sedikit mendekati kaca pelindung ilustrasi tinta di sisi kiri panelmu, membiarkan tatapan matanya yang jernih berhenti lama pada sosok yang berdiri menyamping dekat bingkai jendela."
    shiori "Boleh aku tanya sedikit soal gambar yang di sebelah kiri ini, Amamiya-san?"
    chiasa "Boleh dong, Senpai. Bagian mana yang bikin Senpai penasaran?"
    shiori "Tarikan garis tipis di bahunya... dan cara bayangan jendelanya memotong separuh wajah tokohnya tanpa menyembunyikan arah matanya."
    nar "Jemari Shiori terangkat pelan, tidak menyentuh kaca, hanya berhenti beberapa sentimeter di depan sudut bawah gambar. Saat ia menoleh kembali kepadamu, senyum tipis yang tenang dan menyelidik sudah terpasang rapi di wajahnya."
    shiori "Goresan ini mengingatkanku pada ilustrasi Shena. Aku punya semua jilid bukunya di kamar, Amamiya-san. Jadi aku hafal lebih dari sekadar gambar sampulnya."
    if kk_has("haruka_tahu_shena"):
        chiasa "{i}Karuha pasti menjaga rahasia itu dengan rapat... berarti Shiori benar-benar mengenalinya murni dari satu lembar karya di dinding pameran ini.{/i}"
    else:
        chiasa "{i}Ia langsung mengenali goresan Shena hanya dari satu lembar karya arsip di dinding pameran... Padahal nama pena itu bahkan tidak pernah tertulis di katalog kampus.{/i}"
    nar "Kamu merasakan detak jantungmu naik satu ketukan. Shiori membuka tas tangannya setengah jengkal, dan dari celah bagian dalamnya terlihat punggung sebuah novel strategi ringan yang ujung kertasnya sudah agak lembut karena sering dibaca."
    shiori "Di halaman seratus empat puluh jilid kedua, waktu tokoh ahli strateginya menunggu surat balasan di dekat jendela perpustakaan..."
    shiori "Sudut miring arsiran bayangannya persis sama dengan gambar yang tergantung di depan kita sekarang."
    chiasa "Uwah... Senpai sampai hafal nomor halaman ilustrasinya segala?!"
    shiori "Fufu... Kalau satu gambar bisa menjelaskan isi hati tokohnya lebih tajam daripada dua halaman tulisan, wajar kan kalau pembacanya ingat?"
    nar "Ia menutup kembali tas tangannya dengan gerakan pelan yang tidak mengintimidasi. Tidak ada satu pun pengunjung lain berdiri di dekat panel kalian saat ini; rasa ingin tahu Shiori diberikan seluruhnya kepadamu lebih dulu."
    shiori "Di kartu pameran ini cuma tertulis nama Amamiya Chiasa. Aku tidak berniat menyebar gosip di galeri, makanya aku tanya langsung ke orangnya."
    shiori "Kemiripan garis ini cuma kebetulan... atau aku memang sedang berdiri di depan Shena?"
    nar "Cahaya matahari sore bulan November yang masuk menembus jendela tinggi galeri memantul lembut di atas permukaan kaca bingkai ilustrasimu."
    nar "Di ujung ruangan sebelah utara, beberapa pengunjung masih tampak berbincang pelan mengamati lukisan cat minyak tanpa memperhatikan sudut panel tengah kalian."
    nar "Cara Shiori mengajukan pertanyaannya dengan suara rendah membuktikan bahwa ia benar-benar menghormati privasi sang ilustrator."
    nar "Ia tidak membawa buku itu untuk memojokkanmu di depan umum, melainkan karena ia sungguh-sungguh mengagumi karya yang selama ini menemaninya di sela kesibukan kuliah."
    nar "Namun pada saat yang sama, ketajaman pengamatannya sebagai pemain catur terbaik di kampus membuat alasan setengah matang pasti akan langsung terbaca olehnya."
    nar "Jika kamu mengakui identitas Shena secara jujur kepadanya, kamu akan membagikan rahasia terbesar Chiasa kepada seseorang yang paling menghargai kejujuran."
    nar "Sebaliknya, jika kamu memilih menyangkal dan berpura-pura tidak tahu, Shiori mungkin akan tetap bersikap sopan sambil mencatat kebohonganmu di dalam ingatannya."
    nar "Atau kamu bahkan bisa melangkah lebih berani dengan langsung menawarkan tanda tangan pada jilid novel yang sedang ia bawa di dalam tasnya."
    nar "Shiori berdiri tenang dengan postur anggun di samping panel putihmu, menunggu jawaban yang akan kamu pilih tanpa sedikit pun mendesak."
    nar "Aroma teh hangat dari sudut meja penerima tamu berembus tipis melewati lorong antarpanel galeri yang mulai lengang."
    nar "Di balik ketenangan wajahnya, kamu tahu Shiori telah menyusun seluruh bukti visual dari jilid bukunya sebelum menghampirimu sore ini."
    nar "Kejernihan tatapannya tidak menyisakan ruang bagi keraguan yang berlarut-larut di depan lukisan jendela tersebut."
    nar "Kamu merapikan letak jemarimu di sisi rok sambil memantapkan pilihan kalimat yang akan kamu sampaikan kepadanya."
    nar "Kamu menatap bergantian antara bingkai ilustrasi jendela tersebut dan wajah tenang Shiori sebelum akhirnya membuka suara."
    call kk_family_menu("C11", ["\"Iya, Saionji-senpai. Nama pena Shena itu memang punyaku.\"", "\"Shena? Aku cuma pernah dengar sekilas, tapi itu bukan aku, Senpai.\"", "\"Kalau Senpai bawa bukunya hari ini, mau kutandatangani sekarang sekalian?\""])
    if _return == "A":
        nar "Kamu menatap balik sorot mata Shiori selama dua ketukan, menimbang betapa sia-sianya menyusun alasan tipis di depan seseorang yang bahkan menghafal arah arsiran halaman seratus empat puluh."
        chiasa "...Iya, Senpai. Nama pena Shena itu memang punyaku."
        nar "Kamu menurunkan suaramu sedikit sambil melirik cepat ke arah pintu tangga yang masih sepi."
        chiasa "Tapi tolong banget jangan bocorin ke siapa-siapa di kampus ya, Senpai. Anak-anak studio aja hampir nggak ada yang tahu."
        chiasa "Lagian jujur aja... belakangan ini gaya gambarku lagi berubah banyak, belum tentu masih sebagus arsip lama yang dipajang ini."
        nar "Alis Shiori terangkat sangat tipis satu detik, lalu ekspresinya melunak menjadi ketertarikan yang jernih dan jauh lebih tulus daripada senyum sosialnya yang biasa."
        shiori "Fufu... Jadi benar kamu orangnya. Terima kasih sudah jujur tanpa berputar-putar mencari alasan, Amamiya-san."
        chiasa "Senpai nggak kaget atau kecewa tahu ilustrator aslinya cuma adik kelas biasa?"
        shiori "Untuk apa kecewa? Justru aku salut kamu tidak memamerkan nama penamu buat cari perhatian di kampus. Tenang saja, rahasiamu aman bersamaku."
        nar "Ia kembali menoleh ke arah ilustrasi di panel kaca sambil melipat tangan ringan di depan mantelnya."
        shiori "Mumpung masih senggang, boleh aku tanya satu hal soal komposisi gambarnya?"
        chiasa "Boleh banget, Senpai! Kebetulan Karuha lagi turun ambil brosur, jadi di sini lagi sepi. Mau tanya bagian mana?"
        shiori "Arah matanya. Di novelnya kan ditulis dia sedang menatap papan strategi di meja, tapi di gambarmu dia malah melihat keluar jendela. Kenapa kamu ubah arah pandangannya?"
        chiasa "Hmm... soalnya menurutku, orang yang tiap hari sibuk ngitung langkah orang lain itu justru paling gampang capek sama ruangan tempat dia duduk."
        chiasa "Kalau matanya ngelihat keluar jendela, rasanya dia lagi nyuri waktu satu detik buat dirinya sendiri."
        nar "Shiori terdiam sejenak mendengar jawabanmu. Sudut bibirnya terangkat lembut membentuk senyum tipis yang kali ini benar-benar sampai ke matanya."
        shiori "...Jawaban yang menarik sekali. Keputusan mampir ke galeri seni sore ini ternyata sangat tepat."
        chiasa "Hehehe, kalau gitu kapan-kapan gantian aku yang nanya ya! Bagian mana dari novel strategi itu yang menurut pemain catur beneran paling nggak masuk akal?"
        shiori "Fufufu, dengan senang hati. Aku punya tiga catatan soal taktik pembukaan di bab keempat yang terlalu nekat, tapi lebih enak kita bahas sambil minum teh nanti."
        nar "Sebelum melangkah menuju pintu, Shiori sempat mampir ke meja buku tamu, menuliskan nama dan satu baris komentar singkat dengan tulisan tegak rapi, lalu menoleh sekali lagi kepadamu."
        shiori "Sampai bertemu lagi di ruang klub atau koridor kampus, Amamiya-san. Selamat atas pamerannya."
        chiasa "Terima kasih banyak sudah mampir sore ini, Saionji-senpai. Hati-hati di jalan."
        nar "Kamu melangkah mendekati meja buku tamu setelah sosok mantel gading Shiori menghilang di balik pintu galeri."
        nar "Pada baris paling bawah buku tamu tersebut, tertulis nama Saionji Shiori diikuti kalimat singkat yang memuji kedalaman komposisi jendela pada panel tengah."
        nar "Mengakui kebenaran tentang nama pena Shena tanpa kepura-puraan tadi telah membangun rasa saling menghormati yang sangat kuat di antara kalian."
        nar "Ia bahkan sama sekali tidak mempermasalahkan pengakuanmu bahwa gaya gambarmu belakangan ini sedang berubah dari karya arsip lama."
        nar "Bagi seorang pembaca yang jeli seperti Shiori, kejujuran sikapmu sore ini jauh lebih berharga daripada kesempurnaan teknis semata."
        nar "Suara langkah cepat dari arah tangga luar menandakan kembalinya Karuha yang membawa setumpuk brosur pameran dari ruang cetak."
        "Karuha" "Maaf agak lama, Chiasa! Mesin potong kertas di bawah tadi sempat macet sebentar."
        chiasa "Aman kok, Karuha. Pengunjung sore ini tertib semua."
        nar "Kamu tersenyum tenang sambil merapikan letak pena di samping buku tamu sebelum kembali menjaga panel karyamu."
        nar "Karuha menaruh tumpukan katalog baru itu di sudut meja sambil melirik tulisan tangan rapi di baris terakhir buku tamu."
        nar "Kesepakatan rahasia yang baru saja terjalin dengan Shiori membuat jadwal kunjunganmu ke ruang klub catur minggu depan terasa jauh lebih menarik."
        nar "Cahaya sore bulan November di luar jendela galeri perlahan meredup dengan tenang tanpa menyisakan beban kecemasan di dadamu."
        nar "Karuha kembali naik ke ruang galeri beberapa menit kemudian dan sempat terkejut melihat Ratu Fakultas Ekonomi baru saja keluar setelah berbincang santai berdua denganmu. Ketika pintu menutup pelan, jarak formal yang biasa Shiori pasang sudah berkurang satu langkah penuh."
    elif _return == "B":
        nar "Kamu menahan ekspresimu agar tetap ringan, menggeleng pelan sambil memasang senyum santai yang biasa kamu pakai untuk membelokkan pertanyaan merepotkan di studio."
        chiasa "Shena? Aku pernah lihat sampul bukunya sekilas di toko buku dekat stasiun sih, Senpai. Tapi itu jelas bukan aku kok, aku cuma kebetulan sering latihan niru gaya arsiran populer buat tugas kelas."
        nar "Shiori sama sekali tidak langsung menyela ataupun menaikkan alisnya. Ia memindahkan tatapannya dari wajahmu kembali ke kaca pelindung ilustrasi di dinding, mengamati sudut kertas selama beberapa detik yang terlalu sunyi."
        chiasa "Di kelas ilustrasi semester awal emang banyak yang suka latihan pakai gaya bayangan jendela kayak gitu, Senpai. Mungkin karena buku referensinya sama, jadi kelihatan mirip hehehe."
        shiori "Begitu, ya? Banyak mahasiswa tingkat satu yang kebetulan punya tekanan garis bahu dan lekukan jari kelingking yang sama persis sampai ke detail terkecilnya?"
        chiasa "Yah, kalau sering nyontoh dari buku panduan gambar yang sama, kadang hasilnya memang bisa mirip banget, sih."
        shiori "Menarik. Padahal kertas bertekstur kasar yang kamu pakai di bingkai kiri itu juga sama persis dengan kertas asli ilustrasi jilid ketiganya."
        chiasa "Paling kebetulan sama-sama beli di toko alat lukis depan stasiun aja, Senpai. Anak seni kan hampir semuanya belanja kertas di situ."
        nar "Pandangan mata Shiori yang tenang kembali bertemu matamu. Ia tidak berdebat di tengah ruang pameran yang mulai dimasuki dua pengunjung baru, juga tidak memaksamu menarik ucapanmu kembali."
        shiori "Kalau memang cuma hasil latihan buku panduan dan kebetulan kertasnya sama... maaf sudah membuatmu harus menjelaskan panjang lebar, Amamiya-san."
        chiasa "Nggak apa-apa kok, Senpai! Malah senang dengarnya kalau gambarku dibilang mirip ilustrator profesional."
        nar "Ia menunduk sekilas membaca ulang kartu nama di sudut bingkai, lalu merapikan tali tas tangannya dengan gerakan tenang yang sama sekali tidak menunjukkan kekesalan."
        shiori "Gambar yang di sebelahnya juga rapi. Kelihatannya akhir-akhir ini kamu sedang banyak mengubah cara menarik garis, ya."
        chiasa "I-iya, lagi banyak nyoba gaya baru semester ini biar nggak monoton."
        shiori "Semoga eksperimenmu lancar sampai pameran tutup. Terima kasih sudah menemani melihat-lihat, Amamiya-san. Aku permisi dulu."
        nar "Shiori membungkuk kecil dengan kesopanan sempurna lalu melangkah keluar dari ruang galeri tanpa menoleh sekali pun. Tepat saat ia menghilang di tangga, Karuha muncul membawa tumpukan brosur baru dengan kening berkerut penasaran."
        "Karuha" "Eh, barusan itu Saionji-senpai dari Ekonomi kan? Tumben banget datang ke galeri, tadi mukanya kelihatan serius banget pas membandingkan dua gambarmu..."
        chiasa "Cuma mampir lihat-lihat sebentar kok, Karuha. Katanya baru selesai rapat dari gedung sebelah."
        chiasa "{i}Dia nggak membantah sepatah kata pun... tapi sorot matanya waktu melirik dua gambarku bergantian tadi jelas sedang mencatat sesuatu.{/i}"
        "Karuha" "Oh, syukurlah kalau cuma lihat-lihat biasa. Kirain ada urusan panitia lintas fakultas yang belum beres."
        chiasa "Nggak ada kok. Sini kubantu susun brosur barunya di meja depan."
        nar "Kamu mengambil separuh tumpukan katalog cetak dari tangan Karuha dan menatanya di tepi meja kayu dekat pintu masuk dengan jemari yang terasa agak dingin."
        nar "Ketika kamu melirik halaman buku tamu yang terbuka di samping kotak brosur, Shiori tampak sama sekali tidak menuliskan namanya di sana sebelum pergi."
        nar "Penyangkalan yang kamu rangkai mengenai buku panduan menggambar dan kesamaan toko kertas tadi memang berhasil menghindari pengakuan langsung."
        nar "Akan tetapi, bagi seseorang yang terbiasa membaca tiga langkah lawan di atas papan catur, deretan kebetulan yang terlalu dipaksakan itu justru terdengar seperti konfirmasi."
        nar "Lebih dari itu, perhatian Shiori yang sempat beralih membandingkan gambar arsip di sebelah kiri dengan sketsa barumu di sebelah kanan meninggalkan celah kecurigaan yang baru."
        nar "Ia kini tidak hanya mencurigai bahwa Amamiya Chiasa menyembunyikan nama pena Shena, tetapi juga mulai bertanya-tanya mengapa tarikan garismu berubah drastis."
        nar "Kamu kembali berdiri di dekat panel tengah sambil merasakan suasana galeri yang mendadak tidak lagi senyaman setengah jam lalu."
        nar "Karuha masih sibuk merapikan barisan katalog di meja depan tanpa menyadari betapa tegangnya percakapan yang baru saja terjadi di dekat lukisanmu."
        nar "Di dalam buku catatan ingatan Shiori, penyangkalanmu sore ini telah menjadi satu bidak kebohongan yang sewaktu-waktu dapat ia gunakan untuk mengujimu."
        nar "Kamu menatap kaca bingkai ilustrasi jendela itu dengan perasaan waspada yang terus membayangi sisa jam pameran."
        nar "Kesopanan yang tetap ia berikan sepanjang percakapan sama sekali tidak membuat kebohonganmu terasa lebih ringan. Hal itu hanya berarti kejanggalannya belum dipersoalkan hari ini."
    else:
        nar "Daripada terjebak dalam jawaban defensif, kamu menarik sudut bibirmu sedikit dan membalas tatapan menyelidik Shiori dengan ketenangan yang setara."
        chiasa "Kalau Senpai sampai hafal halaman seratus empat puluh dan kebetulan bawa bukunya di tas... mau sekalian kutandatangani sekarang, kah?"
        chiasa "Asal tetap jadi rahasia kita berdua aja di kampus ya, Senpai."
        nar "Untuk seperempat ketukan, sorot mata Shiori melebar halus oleh kejutan yang jujur. Sedetik kemudian, ia melepaskan tawa pelan yang sangat jarang terdengar di koridor kampus."
        shiori "Fufufu... Tawaran yang berani sekali, Amamiya-san. Bukannya mengelak atau panik cari alasan, kamu malah langsung menawarkan tanda tangan di tengah pameran?"
        chiasa "Habis percuma juga ngeles di depan orang yang hafal arsiranku sampai ke sudut jendelanya, hehehe. Lagian aku senang kalau bukunya beneran dibaca, bukan cuma dipajang."
        nar "Shiori membuka tas tangannya lalu mengeluarkan novel strategi ringan itu bersama sebuah pulpen tinta hitam ramping bergagang perak. Ujung sampul kertasnya memang sudah melunak rapi oleh bekas lipatan jari pembaca setia."
        shiori "Kalau begitu, aku terima tawarannya dengan senang hati. Tolong tulis di halaman depan bagian dalam sini, ya."
        nar "Ia membuka halaman kosong tepat di balik sampul depan lalu meletakkannya di atas meja katalog kecil di samping panel agar kamu punya tumpuan yang rata."
        chiasa "Mau kutulis nama pena Shena aja, atau pakai pesan khusus juga buat Senpai?"
        shiori "Tulis nama pena Shena, lalu tulis juga namamu sendiri di bawahnya."
        shiori "Aku selalu lebih suka mengingat orang yang kutemui langsung di hadapanku daripada sekadar nama di sampul buku."
        chiasa "Eh, namaku sendiri juga? Nanti kalau bukunya dipinjam orang terus ketahuan gimana, Senpai?"
        shiori "Fufu, buku yang kusukai tidak pernah kupinjamkan ke siapa pun, Amamiya-san. Rahasiamu aman di rak kamarku."
        nar "Kamu mencoba dulu aliran tinta pulpen berat milik Shiori di sudut kertas catatan bekas supaya tidak bleber, lalu menarik napas kecil dan menuliskan nama pena Shena dengan huruf sederhana diikuti nama Amamiya Chiasa serta tanggal pameran bulan November tepat di bawahnya."
        nar "Shiori mencondongkan tubuh memperhatikan goresan tintanya mengering, lalu meniup tipis ujung kertas dan menutup buku itu kembali ke dalam tasnya dengan raut puas yang tenang."
        shiori "Terima kasih banyak, Amamiya-san. Rasanya aku berutang satu cangkir teh enak untuk membalas kenang-kenangan sore ini."
        chiasa "Boleh kutagih lain kali di ruang klub catur ya, Senpai? Sekalian aku mau dengar komentar Senpai soal strategi di bab keempat bukunya."
        shiori "Pintu ruang klub selalu terbuka kalau kamu datang membawa kejujuran sejelas hari ini. Aku siapkan teh darjeeling minggu depan, Amamiya-san."
        nar "Tepat saat Shiori berpamitan dan melangkah pergi dengan senyum ringan yang tidak lagi terasa seperti tembok sopan, Karuha muncul dari tangga sambil melongo pelan."
        "Karuha" "Wah, kamu akrab juga sama Saionji-senpai? Baru kali ini aku lihat dia keluar galeri sambil tersenyum sesantai itu."
        chiasa "Cuma kebetulan sama-sama suka buku yang sama kok, Karuha."
        "Karuha" "Buku apa tuh sampai bisa bikin Ratu Fakultas Ekonomi kelihatan ramah banget? Kasih tahu aku juga dong judulnya!"
        chiasa "Haha, buku strategi militer yang agak tebal, nanti kapan-kapan kuceritain kalau brosur pamerannya sudah selesai kita tata ya."
        nar "Karuha meletakkan tumpukan brosur baru di meja depan sambil masih menggeleng kagum melihat kepergian senior terkenal dari fakultas sebelah itu."
        nar "Keberanianmu menjawab pengamatan Shiori dengan tawaran tanda tangan langsung telah mengubah situasi yang tadinya genting menjadi ikatan rahasia yang eksklusif."
        nar "Mulai hari ini, novel strategi yang tersimpan di rak kamar pribadi Shiori memuat dua nama yang mengikat kepercayaan kalian berdua secara tertulis."
        nar "Pada saat yang sama, kamu sadar bahwa tanda tangan ganda itu adalah bukti fisik yang tidak akan pernah bisa kamu sangkal bila suatu saat kamu mengkhianati kepercayaannya."
        nar "Sinar matahari sore yang hangat menerangi ruang galeri lantai dua sementara para pengunjung baru mulai berdatangan dari arah tangga utama."
        nar "Kamu merapikan letak buku tamu di meja depan dengan senyum tenang yang jauh lebih percaya diri."
        nar "Janji minum teh darjeeling di ruang klub catur minggu depan menjadi awal dari hubungan baru yang berdiri di atas rasa saling percaya."
        nar "Di sampingmu, Karuha kembali bersemangat menyapa rombongan mahasiswa desain yang baru masuk untuk melihat pameran."
        nar "Sore akhir pekan di Gedung Seni Rupa itu berakhir dengan perasaan hangat karena rahasia terbesar Chiasa kini berada di tangan pembaca yang tepat."
        nar "Kamu menatap pintu galeri yang menutup pelan, menyadari satu pintu besar menuju Shiori baru saja terbuka lewat kejujuran yang berani."
    return

init 1 python:
    def kk_tell_haruka():
        kk_flag("haruka_tahu_shena")
        kk_adj("shena_risiko",-10)

    _hook("C-D02-A", kk_tell_haruka)
    _hook("C-D02-B", lambda: kk_adj("curiga_haruka",5))
    _hook("C-D02-C", lambda: kk_flag("haruka_dimintai_bantuan"))
    _hook("C11-A", lambda: kk_flag("shiori_tahu_shena"))
    _hook("C11-B", lambda: kk_adj("daftar_kebohongan_shiori",1))
    _hook("C11-C", lambda: kk_flag("shiori_tahu_shena"))
