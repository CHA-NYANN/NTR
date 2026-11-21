# Alur hangat Harumi: teh awal (H02, H05) dan keluarga Kansai (H10, H-D07, H22).
# Efek mengikuti Alur_Cabang/03; nilai angka adalah setelan prototipe. Tanpa materi rute eksploitasi.
# ┌─ PANDUAN CERITA · H02 · Teh di Bawah Atap
# │ LOKASI  : Kampus Kouseikan · Gedung Sains & Lab
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : hujan; ia menyeduh teh untuk pemain.
# │ INTI    : A puji / B minta tambah / C kritik.
# │ AKHIRAN : Trust.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H02:
    call kk_scene_enter("harumi", "Gedung Sains & Lab · Hujan")
    if kk_host == "chiasa":
        nar "Hujan deras pertengahan Juni turun tanpa peringatan di atas halaman Gedung Sains & Lab. Dalam hitungan detik, langit yang tadinya hanya mendung kelabu berubah gelap, dan tirai air yang rapat menghantam paving batu hingga memercikkan kabut dingin ke teras beton."
        nar "Kau terpaksa berlari kecil masuk ke bawah atap lorong depan gedung, menyeka beberapa tetes air dari lengan bajumu sambil memeluk tas kain agar tidak terkena tempias. Payung lipatmu rupanya tertinggal di rumah pagi tadi."
        nar "Tidak jauh darimu, berdiri tenang di bawah naungan atap yang sama, ada Kujo Harumi. Rambut abu-abu panjangnya yang diikat menyamping di atas bahu tetap rapi tanpa sehelai pun basah, kemeja putih dan kardigan abu-abu sederhananya dikancingkan rapi menahan angin lembap, dan sebuah buku catatan kecil tampak menyembul dari saku luar tasnya."
        nar "Harumi sempat menoleh sekilas menyadari kehadiranmu, mengangguk sopan, lalu kembali menatap garis hujan yang jatuh lurus dari talang atap. Ia mengamati arah angin dan kepekatan awan selama beberapa detik sambil membetulkan letak kacamatanya dengan ujung jari."
        harumi "Anginnya datang dari barat daya. Awan di atas bukit belakang masih tebal."
        chiasa "Yah... berarti hujannya masih bakal lama, ya, Kujo-senpai?"
        harumi "Kemungkinan besar belum akan berhenti dalam waktu dekat. Itu perkiraan berdasarkan pengamatan biasa, bukan hasil pengukuran."
        nar "Tanpa terburu-buru, Harumi menurunkan tas kainnya, mengeluarkan sebuah termos baja ramping berwarna perak buram, lalu memutar tutupnya yang sekaligus berfungsi sebagai cangkir kecil."
        nar "Ia menuangkan teh hangat berwarna keemasan jernih ke dalam tutup termos itu, mengangkatnya sedikit untuk memeriksa uap tipis yang naik, lalu menunggu beberapa detik sampai panasnya tidak lagi terlalu menyengat sebelum melangkah mendekat dan menyodorkannya kepadamu lebih dahulu."
        harumi "Amamiya-san, pegang dulu sebelum tanganmu dingin. Perkiraan cuacaku mungkin bisa meleset, tapi teh ini jauh lebih bisa dipercaya."
        nar "Aroma daun teh panggang yang lembut, bersih, dan hangat langsung naik menyapa hidungmu—begitu kontras dengan bau tanah basah dan udara dingin yang mengepung teras gedung."
    else:
        nar "Hujan deras pertengahan Juni turun tanpa aba-aba di atas halaman Gedung Sains & Lab. Langit yang lima menit lalu hanya kelabu mendadak gelap, dan tirai air yang rapat langsung menghantam paving batu hingga memercikkan kabut dingin ke seluruh teras."
        nar "Kau terpaksa berlari menerobos beberapa meter terakhir sebelum berhenti di bawah naungan atap beton teras depan, menepuk-nepuk bahu jaket yang sedikit lembap sambil menyelipkan kedua tangan ke saku celana menahan angin dingin."
        nar "Di sebelahmu, beberapa langkah dari garis tempias, Kujo Harumi berdiri tenang dengan postur tegak. Rambut abu-abu panjangnya yang diikat menyamping di atas bahu tetap rapi tanpa setetes pun air, kemeja putih dan kardigan abu-abu sederhananya terkancing rapi, dan sebuah buku catatan kecil tampak menyembul dari saku luar tas kainnya."
        nar "Kalian sama-sama tahu satu sama lain sejak dulu, tetapi jarang sekali benar-benar mengobrol berdua di luar urusan belajar. Menyadari kehadiranmu, Harumi menoleh sekilas dan mengangguk kecil dengan sopan sebelum kembali menatap awan tebal di atas atap gedung seberang."
        harumi "Kisaragi-kun. Kamu tidak membawa payung?"
        yutaka "Tadi pagi langitnya masih cerah, mana kutahu sore bakal turun sederas ini. Kelihatannya masih lama, ya, Kujo-san?"
        nar "Harumi membetulkan letak kacamatanya dengan ujung jari, mengamati arah miring rintik hujan selama dua detik."
        harumi "Arah anginnya dari barat daya dan awannya masih rapat. Belum akan berhenti dalam waktu dekat. Itu perkiraan biasa, bukan hasil pengukuran."
        nar "Tanpa banyak basa-basi, Harumi menurunkan tas kainnya, mengeluarkan termos baja ramping berwarna perak buram, lalu memutar tutupnya yang merangkap cangkir kecil."
        nar "Ia menuangkan teh hangat berwarna keemasan jernih ke dalam tutup itu, mengamati uap tipis yang naik selama beberapa detik sampai panasnya cukup aman diminum, lalu melangkah mendekat dan menyodorkannya kepadamu lebih dahulu."
        harumi "Ini—pegang dulu sebelum kedinginan. Perkiraan cuacaku bisa saja meleset, tapi teh ini lebih bisa dipercaya."
        nar "Aroma daun teh panggang yang bersih, lembut, dan hangat langsung menyapu udara lembap di antara kalian."
    call kk_family_menu("H02", ["\"Harum banget, suhu sama rasanya pas sekali.\"", "\"Enak banget—boleh minta tambah satu tutup lagi?\"", "\"Maaf, agak terlalu pahit buat seleraku.\""])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau menerima tutup termos hangat itu dengan kedua telapak tangan, membiarkan hawa panasnya merambat ke jari-jarimu yang sempat kedinginan oleh angin hujan, lalu menyesapnya pelan."
            nar "Rasanya bersih dan seimbang—tidak sepat berlebihan, tidak hambar, dengan aroma daun teh panggang yang tertinggal lama di tenggorokan."
            chiasa "Wah... harum sekali, Kujo-senpai. Pahitnya lembut dan suhu seduhannya pas banget—langsung bikin badan hangat."
            nar "Harumi mengerjap pelan di balik kacamatanya. Sudut bibirnya tidak melengkung lebar, tetapi sorot matanya yang biru tua tampak melembut dengan ekspresi puas yang tenang."
            harumi "Kamu menyebut bagian yang tepat, Amamiya-san. Aku memang menakar berat daun dan menunggu suhu airnya turun sedikit lebih lama pagi tadi supaya aroma akhirnya tidak ikut rusak."
            chiasa "Pantas saja rasanya beda jauh sama teh botol dari mesin penjual di lorong."
            harumi "Di mesin penjual suhunya dijaga terlalu tinggi dan terlalu lama disimpan, jadi senyawanya cepat berubah dan rasanya jadi datar. Menyeduh sendiri jauh lebih konsisten."
            nar "Ia terdiam sejenak, membetulkan letak kacamatanya lagi dengan gerakan kecil yang nyaris tak kentara."
            harumi "Biasanya orang hanya bilang 'panas' atau 'enak' lalu selesai. Jarang ada yang memperhatikan suhu dan aromanya terpisah."
            chiasa "Soalnya memang terasa banget bedanya, Senpai. Kelihatan kalau diseduh dengan teliti."
            nar "Harumi tampak tulus senang karena ketelitiannya dikenali tanpa ia harus menunjukkannya lewat catatan atau rumus. Ketika kau menghabiskan tegukan terakhir dan mengembalikan tutup termos itu kepadanya, jari-jari Harumi sempat menahannya beberapa detik sambil menatap permukaan cangkir kecil tersebut."
            nar "Baru saat itu ia tampak menyadari bahwa kalian baru saja berbagi satu tutup termos hangat di bawah derai hujan—sesuatu yang baginya terasa sedikit di luar kebiasaan, namun tidak membuatnya ingin mundur."
            harumi "...Kalau nanti hujannya masih lama, bilang saja. Masih cukup untuk satu putaran lagi."
        else:
            nar "Kau menerima tutup termos hangat itu, merasakan panasnya langsung meresap ke telapak tangan yang dingin, lalu menyesapnya perlahan. Rasanya ternyata jauh lebih bersih dan seimbang daripada teh kaleng atau botolan mana pun yang biasa kaubeli di minimarket."
            yutaka "Wah, serius—ini harum banget, Kujo-san. Suhu sama rasanya pas sekali, nggak sepat tapi aromanya tetap kuat di tenggorokan."
            nar "Harumi mengerjap pelan di balik kacamatanya. Raut wajahnya tetap datar seperti biasa, tetapi ada kilatan puas yang lembut di sorot matanya yang biru tua."
            harumi "Kamu menyebut bagian yang tepat, Kisaragi-kun. Aku memang menakar berat daunnya cukup lama pagi tadi dan menurunkan suhu airnya sedikit sebelum menyeduh supaya aroma akhirnya tidak terbakar."
            yutaka "Pantas rasanya beda jauh sama teh botolan dari mesin penjual."
            harumi "Di mesin penjual suhunya dipanaskan terlalu lama, jadi profil rasanya cepat rusak dan jadi datar. Menyeduh sendiri jauh lebih terkontrol."
            nar "Ia membetulkan letak kacamatanya dengan gerakan tipis, tampak tulus senang karena ketelitiannya dikenali tanpa ia harus memamerkannya lewat catatan atau angka."
            harumi "Jarang ada yang langsung memperhatikan keseimbangan suhu dan aromanya. Biasanya orang cuma bilang 'panas' atau 'enak' lalu selesai."
            yutaka "Soalnya memang terasa banget bedanya. Kelihatan kalau yang bikin nggak asal tuang."
            nar "Ketika kau menghabiskan tegukan terakhir dan mengembalikan tutup termos itu kepadanya, jari-jari Harumi sempat menahannya beberapa detik sambil menatap permukaan cangkir kecil tersebut."
            nar "Tampak jelas ia baru menyadari bahwa kalian berdua baru saja berbagi satu tutup termos hangat di bawah hujan—sesuatu yang baginya tidak sepenuhnya biasa, meski sama sekali tidak membuatnya ingin menjauh."
            harumi "...Kalau hujan belum reda sepuluh menit lagi, masih cukup untuk putaran kedua."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Karena hawa hujan di teras memang dingin, teh hangat itu terasa luar biasa menolong. Kau menyesapnya sampai habis lebih cepat dari yang kaukira, lalu menatap termos baja di tangan Harumi dengan senyum polos."
            chiasa "Enak sekali, Kujo-senpai—sampai nggak kerasa langsung habis. Kalau masih ada, boleh aku minta tambah satu tutup lagi?"
            nar "Harumi tidak ragu sedikit pun. Ia mengambil kembali tutup termos itu dari tanganmu, membuka katup tuangnya, lalu mengisi cangkir kecil itu kali ini jauh lebih penuh daripada porsi pertama sebelum mengembalikannya padamu."
            harumi "Masih ada banyak. Habiskan saja sebelum hujannya berhenti."
            chiasa "Eh, tunggu—kalau kutambah lagi nanti Kujo-senpai sendiri kebagian sedikit dong?"
            harumi "Tidak perlu khawatir. Aku sengaja selalu menyeduh dan membawa lebih dari satu porsi setiap kali mengisi termos di asrama."
            nar "Kau menerima tutup termos kedua itu dengan kedua tangan, merasakan hangatnya kembali memenuhi telapakmu. Harumi berdiri diam di sampingmu sambil menatap tirai air yang mengguyur halaman beton."
            chiasa "Memangnya Senpai selalu minum sebanyak itu di kampus, atau memang jaga-jaga kalau ketemu teman?"
            nar "Harumi menoleh sedikit ke arahmu. Di balik kacamatanya, sorot matanya datar seperti biasa, tetapi kalimat yang keluar sesudahnya terasa begitu jujur dan hangat."
            harumi "Awalnya hanya kebiasaan karena teko di dapur asrama ukurannya tanggung. Tapi... biasanya tidak ada yang pernah bertanya untuk siapa sisa teh di dalam termosku. Hari ini jawabannya jadi jelas."
            chiasa "Kalau begitu aku terima dengan senang hati, Senpai. Terima kasih."
            harumi "Sama-sama, Amamiya-san. Minumlah pelan-pelan, suhunya masih cukup tinggi."
            nar "Kau menggenggam tutup termos hangat itu erat-erat di bawah derai hujan, membiarkan keheningan nyaman di teras Gedung Sains mengisi sisa waktu tunggu kalian berdua."
        else:
            nar "Angin hujan yang dingin di teras membuat teh hangat itu habis jauh lebih cepat daripada rencanamu. Kau menurunkan tutup termos yang sudah kosong itu lalu menatap termos baja di tangan Harumi tanpa sungkan."
            yutaka "Enak banget, Kujo-san—sampai nggak kerasa langsung habis. Kalau masih ada, boleh minta tambah satu tutup lagi?"
            nar "Harumi tidak terlihat keberatan sedikit pun. Ia mengambil tutup termos itu dari tanganmu, membuka katup tuangnya, lalu mengisinya kali ini jauh lebih penuh daripada porsi pertama sebelum mengembalikannya padamu."
            harumi "Masih ada banyak. Habiskan saja sebelum hujannya berhenti."
            yutaka "Nggak apa-apa nih? Nanti bagianmu sendiri habis."
            harumi "Tidak perlu khawatir. Aku sengaja selalu menyeduh dan membawa lebih dari satu porsi setiap pagi."
            nar "Kau menerima tutup termos hangat itu sambil menatap halaman beton yang masih diguyur air deras. Harumi berdiri sejajar di sampingmu, memandang garis hujan dengan tatapan datar yang tenang."
            yutaka "Rajin juga ya, selalu bawa cadangan sebanyak itu. Memangnya sering minum bareng orang lain di lab?"
            nar "Harumi menoleh sedikit ke arahmu. Suaranya tetap datar tanpa hiasan, tetapi kalimat yang keluar sesudahnya terasa begitu jujur dan hangat."
            harumi "Jarang. Awalnya cuma karena ukuran teko di dapur asrama memang lebih besar dari satu gelas. Tapi... biasanya tidak ada yang pernah bertanya untuk siapa sisanya. Hari ini jawabannya jadi jelas."
            yutaka "Kalau begitu, aku terima dengan senang hati. Terima kasih banyak, Kujo-san."
            harumi "Sama-sama, Kisaragi-kun. Pelan-pelan saja minumnya, suhunya masih cukup tinggi."
            nar "Untuk beberapa menit berikutnya, kalian hanya berdiri berdampingan di bawah atap beton, ditemani suara hujan dan uap teh hangat tanpa perlu memaksakan percakapan."
    else:
        if kk_host == "chiasa":
            nar "Kau menyesap sedikit teh dari tutup termos itu. Uapnya memang menghangatkan, tetapi begitu rasa pahit daun teh yang pekat dan sepat menyentuh lidahmu, keningmu refleks sedikit berkerut."
            chiasa "Terima kasih, Kujo-senpai, hangat sih... tapi maaf, buat seleraku ini agak terlalu pahit."
            nar "Harumi menerima kembali tutup termos itu tanpa menunjukkan raut tersinggung atau marah. Ia menatap permukaan tehnya sejenak, lalu mencicipi sedikit sisa di pinggir tutup itu untuk memeriksa sendiri."
            harumi "Hmm. Kepahitan di ujungnya memang karakter dari jenis daun teh yang kupilih pagi ini, ditambah waktu seduh tiga menit penuh. Wajar kalau tidak semua orang menyukainya."
            nar "Meski nadanya tetap tenang dan rasional seperti sedang mencatat hasil percobaan, gerakannya saat mengosongkan sedikit sisa tetes dan memutar kembali tutup termos baja itu terasa sedikit lebih cepat daripada biasanya."
            nar "Ia memasukkan termosnya kembali ke dalam tas kain dan menarik ritsletingnya hingga tertutup rapi."
            harumi "Lain kali aku tanya seleramu dulu sebelum menawarkan, Amamiya-san. Aku terlalu cepat menganggap sesuatu yang kusukai pasti bisa menolong orang lain juga."
            chiasa "Eh, bukan begitu maksudku, Senpai—aku tetap menghargai tawarannya, sungguh. Cuma lidahku memang nggak kuat yang terlalu pahit."
            harumi "Aku mengerti. Secara objektif tidak ada yang salah dengan preferensi rasa. Tidak apa-apa."
            nar "Ia membetulkan letak kacamatanya sekali, lalu kembali memandang lurus ke arah hujan yang turun deras di halaman. Tidak ada pertengkaran atau kata-kata tajam, tetapi jarak sopan yang rapi di antara kalian berdua terasa kembali terpasang tepat di bawah atap yang sama."
        else:
            nar "Kau menyesap sedikit teh dari tutup termos itu. Hangatnya memang terasa di tenggorokan, tetapi rasa pahit daun teh yang pekat dan sepat langsung menyentuh lidah hingga keningmu refleks berkerut."
            yutaka "Makasih, Kujo-san, lumayan bikin hangat... tapi jujur saja, buat seleraku ini agak terlalu pahit."
            nar "Harumi mengambil kembali tutup termos itu tanpa menunjukkan raut tersinggung atau marah. Ia menatap permukaannya sejenak, lalu mencicipi sedikit sisa di pinggir tutup itu untuk memeriksa sendiri sebelum mengangguk singkat."
            harumi "Kepahitan di ujungnya memang karakter daun teh yang kupilih pagi ini, ditambah waktu seduh tiga menit penuh. Wajar kalau tidak cocok di lidah semua orang."
            nar "Meski ucapannya tetap tenang dan objektif seperti sedang mengevaluasi hasil pengamatan, caranya memutar kembali tutup termos dan memasukkannya ke dalam tas kain terasa sedikit lebih cepat daripada saat ia mengeluarkannya tadi."
            harumi "Lain kali aku tanya seleramu dulu, Kisaragi-kun. Aku terlalu cepat menganggap sesuatu yang kusukai pasti bisa menolong orang lain juga."
            yutaka "Bukan gitu maksudku—aku tetap menghargai tawarannya kok, sungguh. Cuma lidahku memang nggak terlalu kuat yang pahit."
            harumi "Aku paham. Secara objektif preferensi rasa bukan sesuatu yang perlu diperdebatkan. Tidak apa-apa."
            nar "Ia membetulkan kacamatanya sekali lalu kembali menatap lurus ke arah hujan di halaman. Tidak ada suasana bermusuhan, tetapi jarak sopan yang rapi di antara kalian berdua terasa kembali menutup rapat di bawah atap yang sama."
    return

# ┌─ PANDUAN CERITA · H05 · Reuni di Rumah Teh
# │ LOKASI  : Kampus Kouseikan · Kafe Komorebi
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : kelompok belajar.
# │ INTI    : A bantu penyajian / B pembicaraan masa depan / C membuka rahasia.
# │ AKHIRAN : gerbang pengecekan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H05:
    call kk_scene_enter("harumi", "Kafe Komorebi · Kelompok belajar")
    nar "Kelompok belajar di Komorebi selesai dengan kebiasaan lama: semua membawa jawaban pulang, Harumi masih memastikan tidak ada buku tertinggal. Ia hampir memanggil seseorang kembali, lalu hanya menanyakan apakah kau mau tinggal."
    harumi "Aku belum ingin percakapannya selesai. Itu alasan yang lebih tepat daripada masih menata cangkir. Tapi cangkirnya juga memang perlu ditata."
    call kk_family_menu("H05", ["Bantu ia menyajikan teh untuk yang tersisa.", "Tanyakan ke mana ia ingin melangkah setelah lulus.", "Pancing ia menceritakan hal yang jarang ia buka."])
    if _return == "A":
        harumi "Berdua lebih cepat. Terima kasih."
        nar "Kalian membagi pekerjaan, kemudian justru duduk lebih lama setelah selesai. Harumi tampak geli pada kenyataan bahwa pekerjaan yang dijadikan alasan sudah habis tetapi kau tetap berada di sana."
    elif _return == "B":
        harumi "Orang tuaku mengukur segalanya. Aku belum tahu caraku sendiri. Tapi aku ingin tahu."
        nar "Ia bercerita tentang menjadi profesor, bukan hanya sebagai puncak yang diharapkan keluarga tetapi keinginan untuk punya ruang bertanya dan membimbing."
        harumi "Aku ingin tahu apakah masih akan memilih itu kalau suatu hari mereka tidak bangga. Sejauh ini jawabannya iya. Itu membuatku lega."
    else:
        harumi "...Jarang ada yang bertanya soal itu. Mungkin lain kali."
        nar "Kau menyentuh cerita yang belum siap ia buka. Harumi memberikan batas singkat, lalu menanyakan hal lain agar penolakan kecil tersebut tidak harus mengakhiri kebersamaan."
        nar "Tetap duduk sesudahnya memberinya pengalaman bahwa belum mau bercerita tidak membuat seseorang otomatis pergi."
    return

# ┌─ PANDUAN CERITA · H10 · Pulang ke Kansai
# │ LOKASI  : Stasiun & Pasar · Stasiun Kouseikan-mae
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : orang tua Kujo dan Mizuhara.
# │ INTI    : A ikut / B tidak / C bercerita tentang Harumi.
# │ AKHIRAN : konteks keluarga.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H10:
    call kk_scene_enter("harumi", "Stasiun Kouseikan-mae")
    nar "Tiket Kansai terselip di buku Harumi. Ia telah merencanakan perjalanan, pertemuan keluarga, dan pembicaraan tentang studinya, tetapi menunda membalas pertanyaan ibunya tentang apakah ingin dijemput."
    harumi "Aku pulang akhir pekan ini. Bertemu orang tua. Mungkin akan lebih banyak bicara tentang riset daripada diriku sendiri. Aku belum tahu apakah itu karena mereka tidak bertanya, atau aku yang selalu lebih dahulu membawa nilai."
    call kk_family_menu("H10", ["Tawarkan ikut menemaninya pulang.", "Katakan sebaiknya ia pergi sendiri dulu.", "Ceritakan hal baik tentang Harumi yang bisa ia bawa pulang."])
    if _return == "A":
        harumi "Kau yakin? Orang tuaku akan menanyaimu seperti menguji hipotesis."
        nar "Kau mengatakan bersedia hadir tanpa menjawab atas namanya. Harumi akhirnya membalas pesan ibunya bahwa akan ada teman, lalu menyebut namamu dengan jelas."
        harumi "Aku ingin mereka mengenal bagian hidupku yang tidak bisa dijelaskan lewat transkrip. Itu termasuk kamu."
    elif _return == "B":
        harumi "Mungkin kau benar. Ini urusanku dengan mereka."
        nar "Ia menyimpan tiket dan mengatakan akan mencoba membicarakan sesuatu yang tidak berkaitan dengan prestasi. Ada kecewa kecil karena pergi sendiri, tetapi juga ruang untuk menentukan bagaimana ingin dikenal keluarganya."
    else:
        harumi "Kalau kau yang bilang begitu, barangkali aku bisa mengulanginya pada mereka."
        nar "Kau menyebut kesabarannya, humor kering yang mulai kaukenali, dan kepedulian kecil yang jarang ia hitung sebagai kelebihan. Harumi menolak satu pujian, lalu membiarkan yang lain tetap ada."
        harumi "Aku akan mencoba mengatakan itu tanpa menambahkan bahwa orang lain pasti lebih baik."
    return

# ┌─ PANDUAN CERITA · H22 · Natal Pulang
# │ LOKASI  : Stasiun & Pasar · Stasiun Kouseikan-mae
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : ia pulang ke Kansai.
# │ INTI    : A mengantar / B menelepon orang tua / C biarkan.
# │ AKHIRAN : keluarga.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H22:
    call kk_scene_enter("harumi", "Stasiun Kouseikan-mae · Natal")
    if kk_has("harumi_kansai_ikut"):
        harumi "Tahun lalu kau ikut sampai depan rumah. Kali ini aku pulang untuk Natal. Mereka menanyakanmu."
    else:
        harumi "Aku pulang untuk Natal. Entah kenapa, tahun ini rasanya bukan sekadar kewajiban."
    call kk_family_menu("H22", ["Antar ia sampai peron dan tunggu keretanya berangkat.", "Tawarkan menelepon orang tuanya untuk menitip salam.", "Ucapkan selamat jalan lalu biarkan ia pergi."])
    if _return == "A":
        harumi "Sampai keretanya hilang di tikungan, ya. Baik."
        nar "Kau menunggu di peron. Harumi memilih tempat dekat jendela, menaruh tas, lalu melambai sebelum kereta bergerak. Ia tidak perlu membuat perpisahan itu berguna agar boleh terasa berat."
    elif _return == "B":
        harumi "Mereka akan kaget. Tapi kurasa mereka akan senang."
        nar "Dengan izinnya kau menyampaikan salam dan waktu kedatangan. Ibunya bertanya apakah Harumi sudah makan sebelum menanyakan riset. Ia mendengar dari dekatmu, tersenyum pada urutan yang kali ini berbeda."
    else:
        nar "Ia melambai sekali sebelum naik. Tidak ada yang menemaninya sampai jendela, tetapi ia tetap mengirim kabar ketika sudah duduk."
        harumi "Aku akan sampai sore. Aku ingin pulang, ternyata. Menulis itu membuatku lebih yakin daripada menghitung alasan kenapa harus."
    return

# ┌─ PANDUAN CERITA · H-D07 · Surat dari Kansai
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kujo Harumi
# │ AWALAN  : setelah H10-A
# │ INTI    : A Bantu Harumi membalas / B bacakan / C abaikan
# │ AKHIRAN : orang_tua_kujo +
# └─ tulis / perbaiki dialog di bawah ──
label kk_kansai_letter:
    nar "Surat dari Kansai memuat kabar rumah, jadwal ayahnya, dan pertanyaan penelitian. Di akhir ada baris tentang teh yang masih tersisa sejak kunjungan kalian. Harumi membacanya berulang kali."
    harumi "Aku tahu beliau ingin kabar. Aku hanya tidak tahu apakah boleh menjawab bahwa aku lelah, bukan sedang mencapai sesuatu."
    call kk_family_menu("H-D07", ["Bantu ia menyusun balasan dengan kata-katanya sendiri.", "Bacakan suratnya keras-keras agar ia mendengarnya utuh.", "Sarankan ia mengabaikan surat itu saja."])
    if _return == "A":
        harumi "Jadi aku boleh menulis apa yang kurasakan, bukan hanya nilai dan jadwal."
        nar "Ia menulis satu paragraf yang tidak bisa dipindahkan ke laporan akademik. Sesudahnya ia membacanya kembali, tidak langsung menghapus bagian tentang ingin ditelepon tanpa membahas riset."
    elif _return == "B":
        harumi "Dibacakan begini, ada satu kalimat yang hampir terdengar seperti rindu."
        nar "Kau membaca tanpa menambahkan maksud yang tak tertulis. Harumi menunjuk baris tentang teh, lalu mengakui mungkin itu cara ibunya mengatakan masih mengingat kehadiran mereka di rumah."
        harumi "Aku bisa bertanya apakah memang itu maksudnya. Aku tidak perlu menentukan sendirian dari selembar surat."
    else:
        nar "Kau menyarankan mengabaikan. Harumi melipat surat dan menyimpannya kembali di buku. Balasan yang tidak segera dibuat akan semakin sulit dimulai karena ia merasa harus sekaligus meminta maaf atas keterlambatan."
    return

init 1 python:
    _hook("H02-A", lambda: kk_rel("harumi","trust",4))
    _hook("H02-B", lambda: (kk_rel("harumi","intim",3), kk_rel("harumi","trust",2)))
    _hook("H02-C", lambda: kk_rel("harumi","trust",-3))
    _hook("H05-A", lambda: kk_rel("harumi","trust",4))
    _hook("H05-B", lambda: (kk_rel("harumi","trust",3), kk_adj("orang_tua_kujo",5)))
    _hook("H05-C", lambda: (kk_rel("harumi","intim",4), kk_rel("harumi","trust",2)))
    _hook("H10-A", lambda: (kk_adj("orang_tua_kujo",15), kk_rel("harumi","trust",5), kk_flag("harumi_kansai_ikut")))
    _hook("H10-B", lambda: kk_rel("harumi","trust",2))
    _hook("H10-C", lambda: (kk_rel("harumi","trust",4), kk_adj("orang_tua_kujo",5)))
    _hook("H22-A", lambda: (kk_adj("orang_tua_kujo",10), kk_rel("harumi","trust",4)))
    _hook("H22-B", lambda: (kk_adj("orang_tua_kujo",10), kk_rel("harumi","trust",3)))
    _hook("H-D07-A", lambda: (kk_adj("orang_tua_kujo",10), kk_rel("harumi","trust",3), kk_flag("kujo_surat_dibalas")))
    _hook("H-D07-B", lambda: kk_adj("orang_tua_kujo",5))
    _hook("H-D07-C", lambda: kk_adj("orang_tua_kujo",-5))
