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
        nar "Kamu terpaksa berlari kecil masuk ke bawah atap lorong depan gedung, menyeka beberapa tetes air dari lengan bajumu sambil memeluk tas kain agar buku sketsamu tidak terkena tempias. Payung lipatmu rupanya tertinggal di rak dekat pintu rumah pagi tadi."
        nar "Tidak jauh darimu, berdiri tenang di bawah naungan atap yang sama, ada Kujo Harumi. Rambut abu-abu panjangnya yang diikat menyamping di atas bahu tetap rapi tanpa sehelai pun basah, kemeja putih dan kardigan abu-abu sederhananya dikancingkan rapi menahan angin lembap, dan sebuah buku catatan kecil menyembul dari saku luar tasnya."
        nar "Harumi sempat menoleh sekilas menyadari kehadiranmu, mengangguk sopan, lalu kembali menatap garis hujan yang jatuh lurus dari talang atap. Ia mengamati arah angin dan kepekatan awan selama beberapa detik sambil membetulkan letak kacamatanya dengan ujung jari."
        harumi "Amamiya-san. Kamu kehujanan di halaman depan tadi?"
        chiasa "Cuma kena sedikit di lengan baju, Kujo-senpai. Payung lipatku ketinggalan di rumah gara-gara pagi tadi langitnya cerah banget, nggak ada tanda mendung sama sekali."
        harumi "Prakiraan cuaca pagi ini memang hanya mencatat peluang hujan tiga puluh persen untuk siang hari. Angin laut bergerak masuk lebih cepat dari perkiraan."
        chiasa "Kujo-senpai selalu cek prakiraan cuaca sebelum berangkat?"
        harumi "Sudah kebiasaan. Apalagi kalau hari itu aku membawa berkas catatan laboratorium yang tidak boleh lembap."
        nar "Ia kembali menoleh ke halaman luar, menatap puncak pepohonan di tepi lapangan yang mulai miring ditiup embusan angin."
        harumi "Anginnya datang dari barat daya. Awan di atas bukit belakang masih sangat tebal."
        chiasa "Yah... berarti hujannya masih bakal lama reda ya, Kujo-senpai?"
        harumi "Kemungkinan besar belum akan berhenti dalam tiga puluh menit ke depan. Itu cuma perkiraan dari pengamatan cuaca biasa tanpa alat ukur."
        chiasa "Kalau begitu aku ikut berteduh di sini dulu deh. Kujo-senpai juga baru keluar dari laboratorium dan mau pulang ke asrama?"
        harumi "Iya, baru selesai merapikan hasil pengamatan kelas siang. Aku membawa payung lipat, tapi dengan angin sekencang ini, memaksa jalan sekarang cuma akan membuat bagian bawah rok dan tas buku basah percuma."
        chiasa "Bener juga, jalan setapak depan sana saja sudah mulai tergenang."
        nar "Tanpa terburu-buru, Harumi menurunkan tas kainnya, mengeluarkan sebuah termos baja ramping berwarna perak buram, lalu memutar tutupnya yang sekaligus berfungsi sebagai cangkir kecil."
        nar "Ia menuangkan teh hangat berwarna keemasan jernih ke dalam tutup termos itu, mengangkatnya sedikit untuk memeriksa uap tipis yang naik, lalu menunggu beberapa detik sampai panasnya tidak lagi terlalu menyengat sebelum melangkah mendekat dan menyodorkannya kepadamu lebih dahulu."
        harumi "Amamiya-san, pegang dulu sebelum tanganmu dingin. Ujung lengan bajumu tadi kena tempias kan? Perkiraan cuacaku mungkin bisa meleset beberapa menit, tapi suhu teh ini jauh lebih bisa dipercaya."
        nar "Aroma daun teh panggang yang lembut, bersih, dan hangat langsung naik menyapa hidungmu, begitu kontras dengan bau tanah basah dan udara dingin yang mengepung teras gedung."
    else:
        nar "Hujan deras pertengahan Juni turun tanpa aba-aba di atas halaman Gedung Sains & Lab. Langit yang lima menit lalu hanya kelabu mendadak gelap, dan tirai air yang rapat langsung menghantam paving batu hingga memercikkan kabut dingin ke seluruh teras."
        nar "Kamu terpaksa berlari menerobos beberapa meter terakhir sebelum berhenti di bawah naungan atap beton teras depan, menepuk-nepuk bahu jaket yang sedikit lembap sambil menyelipkan kedua tangan ke saku celana menahan angin dingin."
        nar "Di sebelahmu, beberapa langkah dari garis tempias, Kujo Harumi berdiri tenang dengan postur tegak. Rambut abu-abu panjangnya yang diikat menyamping di atas bahu tetap rapi tanpa setetes pun air, kemeja putih dan kardigan abu-abu sederhananya terkancing rapi, dan sebuah buku catatan kecil menyembul dari saku luar tas kainnya."
        nar "Menyadari kehadiranmu, Harumi menoleh sekilas dan mengangguk kecil dengan sopan sebelum kembali menatap awan tebal di atas atap gedung seberang."
        harumi "Kisaragi-kun. Kamu tidak membawa payung hari ini?"
        yutaka "Tadi pagi langitnya masih cerah banget waktu berangkat, mana kutahu bakal turun sederas ini. Kelihatannya masih lama redanya ya, Kujo-san?"
        harumi "Prakiraan pagi tadi memang cuma menyebut kemungkinan gerimis ringan. Perubahan tekanan angin di dekat bukit sering membuat hujan datang mendadak di bulan Juni."
        yutaka "Kamu baru kelar kelas praktikum di dalam?"
        harumi "Iya, baru selesai mencocokkan catatan laporan bersama asisten laboratorium."
        nar "Harumi membetulkan letak kacamatanya dengan ujung jari, mengamati arah miring rintik hujan selama beberapa detik."
        harumi "Arah anginnya dari barat daya dan lapisan awannya masih rapat. Kemungkinan belum akan berhenti dalam setengah jam ke depan. Itu sekadar perkiraan pengamatan biasa tanpa alat."
        yutaka "Kamu sendiri bawa payung, kan? Nggak langsung jalan saja balik ke asrama?"
        harumi "Bawa. Tapi dengan angin miring seperti sekarang, berjalan melintasi lapangan terbuka cuma akan membuat sisi tas dan buku catatan ikut basah. Menunggu di sini jauh lebih masuk akal."
        yutaka "Masuk akal sih. Melihat genangan di tangga depan situ saja aku langsung malas melangkah."
        nar "Tanpa banyak basa-basi, Harumi menurunkan tas kainnya, mengeluarkan termos baja ramping berwarna perak buram, lalu memutar tutupnya yang merangkap sebagai cangkir kecil."
        nar "Ia menuangkan teh hangat berwarna keemasan jernih ke dalam tutup itu, mengamati uap tipis yang naik selama beberapa detik sampai panasnya cukup aman diminum, lalu melangkah mendekat dan menyodorkannya kepadamu lebih dahulu."
        harumi "Ini, pegang dulu sebelum tanganmu kedinginan. Bahu jaketmu tadi sempat kena hujan kan? Perkiraan cuacaku bisa saja meleset, tapi teh ini jauh lebih bisa dipercaya."
        nar "Aroma daun teh panggang yang bersih, lembut, dan hangat langsung menyapu udara lembap di antara kalian."
    call kk_family_menu("H02", ["\"Harum banget, suhu sama rasanya pas sekali.\"", "\"Enak banget, boleh minta tambah satu tutup lagi?\"", "\"Maaf, agak terlalu pahit buat seleraku.\""])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu menerima tutup termos hangat itu dengan kedua telapak tangan, membiarkan hawa panasnya merambat ke jari-jarimu yang sempat kedinginan oleh angin hujan, lalu menyesapnya pelan."
            nar "Rasanya bersih dan seimbang, tidak sepat berlebihan dan tidak hambar, dengan aroma daun teh panggang yang tertinggal nyaman di tenggorokan."
            chiasa "Wah... harum sekali, Kujo-senpai. Pahitnya lembut dan suhu seduhannya pas sekali di lidah, langsung bikin badan hangat."
            nar "Harumi mengerjap pelan di balik kacamatanya. Sudut bibirnya tidak melengkung lebar, tetapi sorot matanya yang biru tua tampak melembut dengan ekspresi puas yang tenang."
            harumi "Kamu memperhatikan bagian yang tepat, Amamiya-san. Aku memang menakar berat daun tehnya dengan timbangan kecil pagi tadi dan menunggu suhu airnya turun ke delapan puluh derajat sebelum menyeduh supaya aroma akhirnya tidak ikut terbakar."
            chiasa "Sampai ditimbang dan diukur suhunya segala pagi-pagi, Senpai?"
            harumi "Kalau sudah terbiasa, tidak sampai lima menit kok. Air yang baru mendidih langsung dituang ke cangkir perantara dulu supaya turun sekitar dua puluh derajat, baru dituang ke daun tehnya."
            chiasa "Pantas saja rasanya beda jauh sama teh botol hangat dari mesin penjual otomatis di lorong kampus. Ini jenis teh panggang apa, Senpai?"
            harumi "Teh batang panggang. Kafeinnya sedikit lebih rendah dan lebih ramah untuk lambung kalau aku harus berada di laboratorium sampai lewat jam makan. Di mesin penjual otomatis suhunya dijaga terlalu tinggi selama berjam-jam, jadi senyawa taninnya berubah dan rasanya menjadi datar. Menyeduh sendiri dari daun kering jauh lebih konsisten."
            chiasa "Wah, dengar penjelasannya saja jadi kerasa banget bedanya. Padahal di rumahku sendiri aku biasanya cuma celup kantong teh terus langsung tuang air panas dari ketel."
            harumi "Metode itu praktis kalau sedang terburu-buru. Tapi kalau suatu hari kamu ingin istirahat sebentar di tengah tugas gambar yang padat, mencoba menunggu air turun suhunya sebentar memberi hasil yang cukup menyenangkan."
            nar "Ia terdiam sejenak, membetulkan letak kacamatanya lagi dengan gerakan kecil."
            harumi "Biasanya kalau aku menawari orang lain, mereka hanya bilang 'panas' atau 'enak' lalu selesai. Jarang ada yang memperhatikan suhu dan aromanya secara terpisah seperti kamu barusan."
            chiasa "Soalnya memang terasa sekali bedanya, Senpai. Kelihatan kalau yang menyeduh benar-benar teliti."
            nar "Kalian berdiri berdampingan beberapa menit lagi menikmati suara hujan yang mulai sedikit melambat. Ketika kamu menghabiskan tegukan terakhir dan mengembalikan tutup termos itu kepadanya, jari-jari Harumi sempat menahannya beberapa detik sambil menatap tepi cangkir kecil tersebut. Tampak jelas ia baru menyadari bahwa kalian berdua baru saja berbagi satu tutup termos yang sama di bawah derai hujan, sebuah kedekatan kecil yang sama sekali tidak membuatnya keberatan."
            harumi "...Kalau lima belas menit lagi hujannya masih belum reda, bilang saja. Isi termosnya masih cukup untuk satu cangkir lagi, Amamiya-san."
            chiasa "Terima kasih banyak, Kujo-senpai. Kalau begitu aku ikut menunggu hujan agak reda di sini bareng Senpai ya."
            harumi "Iya. Berdiri berdua di teras memang membuat waktu tunggu terasa lebih pendek."
        else:
            nar "Kamu menerima tutup termos hangat itu, merasakan panasnya langsung meresap ke telapak tangan yang dingin, lalu menyesapnya perlahan. Rasanya ternyata jauh lebih bersih dan seimbang daripada teh kaleng atau botolan mana pun yang biasa kamu beli di minimarket."
            yutaka "Wah, serius, ini harum sekali, Kujo-san. Suhu sama takaran rasanya pas banget, nggak sepat di lidah tapi wangi daun tehnya tetap terasa jelas."
            nar "Harumi mengerjap pelan di balik kacamatanya. Raut wajahnya tetap tenang seperti biasa, tetapi ada kilatan puas yang lembut di sorot matanya yang biru tua."
            harumi "Kamu menyebut bagian yang tepat, Kisaragi-kun. Aku memang menakar berat daunnya cukup teliti pagi tadi dan menurunkan suhu air mendidihnya sebentar sebelum menyeduh supaya aroma akhirnya tidak rusak."
            yutaka "Pagi-pagi kamu sempat menimbang daun teh dan menurunkan suhu air segala? Niat banget."
            harumi "Kalau sudah jadi rutinitas sebelum berangkat kuliah, tidak sampai lima menit kok. Air mendidih cukup dipindahkan sebentar ke teko keramik supaya suhunya turun, baru dituang ke daunnya."
            yutaka "Pantas rasanya jauh di atas teh hangat botolan dari mesin penjual di pojok gedung. Ini jenis teh apa, Kujo-san?"
            harumi "Teh batang panggang. Kandungan kafeinnya lebih ringan dan tidak mudah mengganggu perut saat jam praktikum panjang. Di mesin penjual suhunya dipanaskan terus-menerus terlalu lama, jadi profil rasanya cepat rusak dan menjadi datar. Menyeduh sendiri dengan takaran waktu tiga menit jauh lebih terkontrol."
            yutaka "Pantas saja di apartemen aku bikin teh celup sering terasa aneh, ternyata langsung kucelup pakai air mendidih terus kutinggal kelamaan."
            harumi "Itu kesalahan paling umum. Lain kali tunggu sekitar dua menit setelah ketel berbunyi sebelum menuang airnya, rasanya akan jauh lebih halus."
            nar "Ia membetulkan letak kacamatanya dengan gerakan tipis, tampak tulus senang karena ketelitiannya dikenali tanpa ia harus memamerkannya lewat angka atau catatan."
            harumi "Jarang ada yang langsung memperhatikan keseimbangan suhu dan aromanya. Biasanya orang cuma bilang 'lumayan buat penghangat' lalu selesai."
            yutaka "Soalnya memang terasa jelas bedanya di tenggorokan. Kelihatan kalau yang bikin nggak asal tuang air panas."
            nar "Kalian berdiri sejajar beberapa menit lagi memandangi halaman yang basah. Ketika kamu menghabiskan tegukan terakhir dan mengembalikan tutup termos itu kepadanya, jari-jari Harumi sempat menahannya beberapa detik sambil menatap permukaan cangkir kecil tersebut. Ia tampak baru menyadari bahwa kalian baru saja berbagi satu tutup termos di bawah naungan teras, dan hal itu sama sekali tidak membuatnya mengambil jarak."
            harumi "...Kalau hujannya belum reda sepuluh menit lagi, masih cukup untuk putaran kedua, Kisaragi-kun."
            yutaka "Siap, makasih banyak, Kujo-san. Lumayan jadi nggak terlalu kesal kejebak hujan begini."
            harumi "Iya. Menunggu cuaca reda bersama orang lain memang terasa lebih masuk akal daripada berdiri sendiri."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Karena hawa hujan di teras beton memang cukup dingin, teh hangat itu terasa sangat menolong. Kamu menyesapnya sampai habis lebih cepat dari perkiraanmu, lalu menatap termos baja di tangan Harumi dengan senyum jujur."
            chiasa "Enak sekali, Kujo-senpai, sampai nggak terasa tahu-tahu sudah habis. Kalau masih ada isinya, boleh aku minta tambah satu tutup lagi?"
            nar "Harumi tidak ragu sedikit pun. Ia menerima kembali tutup termos itu dari tanganmu, membuka katup tuangnya, lalu mengisi cangkir kecil itu kali ini jauh lebih penuh daripada tuangan pertama sebelum menyodorkannya kembali kepadamu."
            harumi "Silakan. Masih ada cukup banyak di dalam. Habiskan saja selagi uapnya masih hangat."
            chiasa "Eh, tunggu sebentar, kalau kutambah penuh begini nanti Kujo-senpai sendiri kebagian sedikit dong?"
            harumi "Tidak perlu khawatir, Amamiya-san. Aku sengaja selalu menyeduh dan membawa lebih dari satu porsi setiap kali mengisi termos di dapur asrama pagi hari."
            nar "Kamu menerima tutup termos kedua itu dengan kedua tangan, merasakan hangatnya kembali memenuhi telapakmu. Di halaman luar, dua mahasiswa berlari melintasi genangan sambil memegang payung yang hampir terbalik ditiup angin, membuatmu sedikit tersenyum."
            chiasa "Untung kita nggak nekat lari kayak mereka tadi ya, Senpai. Payungnya sampai melengkung ke atas begitu."
            harumi "Mereka mengambil jalur paling terbuka di tengah halaman. Kalau memutar lewat selasar samping perpustakaan, terpaan anginnya berkurang lebih dari setengah."
            chiasa "Oh ya, memangnya Senpai selalu minum sebanyak itu sendirian di laboratorium, atau memang sengaja bawa lebih buat jaga-jaga kalau ketemu teman?"
            nar "Harumi menoleh sedikit ke arahmu. Di balik lensa kacamatanya, sorot matanya tenang seperti biasa, tetapi kalimat yang keluar sesudahnya terdengar sangat tulus."
            harumi "Awalnya hanya kebiasaan praktis karena teko saring di dapur asrama ukurannya tanggung kalau cuma diisi satu gelas. Sisa seduhannya sayang kalau dibuang, jadi sekalian kumasukkan semua ke termos."
            chiasa "Terus biasanya sisa porsinya diminum sore hari?"
            harumi "Kadang sampai malam pun masih tersisa. Sebenarnya... biasanya tidak ada yang pernah bertanya untuk siapa sisa teh di dalam termosku. Hari ini jawabannya jadi jelas."
            chiasa "Kalau begitu aku terima porsi keduanya dengan senang hati, Senpai. Terima kasih banyak ya."
            harumi "Sama-sama, Amamiya-san. Minumlah pelan-pelan, bagian tengah termos biasanya suhunya masih agak tinggi."
            chiasa "Nanti kalau hujannya sudah tinggal gerimis, aku mampir beli biskuit di koperasi buat balas tehnya ya, Senpai."
            harumi "Tidak perlu membalas. Cukup tunggu sampai hujannya benar-benar aman untuk jalan pulang, nanti baju dan buku sketsamu malah basah."
            chiasa "Baik, Senpai. Memang paling enak berdiri di sini dulu sambil pegang teh hangat."
            nar "Kamu menggenggam tutup termos hangat itu di bawah derai hujan, menikmati ketenangan yang terasa jauh lebih akrab di teras Gedung Sains bersama Harumi."
        else:
            nar "Angin hujan yang dingin di teras membuat teh hangat itu habis jauh lebih cepat daripada rencanamu. Kamu menurunkan tutup termos yang sudah kosong itu lalu menatap termos baja di tangan Harumi tanpa sungkan."
            yutaka "Enak banget tehnya, Kujo-san, sampai nggak kerasa langsung habis sekali teguk. Kalau masih ada sisa, boleh minta tambah satu tutup lagi?"
            nar "Harumi tidak terlihat keberatan sedikit pun. Ia mengambil tutup termos itu dari tanganmu, menekan katup tuangnya, lalu mengisinya kali ini jauh lebih penuh daripada porsi pertama sebelum mengembalikannya kepadamu."
            harumi "Masih ada banyak di dalam. Habiskan saja sebelum hujannya berhenti."
            yutaka "Beneran nggak apa-apa nih? Nanti bagian buat kamu minum sendiri di jalan malah habis."
            harumi "Tidak perlu khawatir. Aku memang selalu menyeduh dan membawa lebih dari satu porsi setiap pagi dari asrama."
            nar "Kamu menerima tutup termos hangat itu sambil memandangi halaman beton yang masih diguyur air deras. Di seberang sana, dua mahasiswa berlari menerobos genangan dengan payung miring yang nyaris terbalik oleh angin."
            yutaka "Untung tadi kita milih berteduh di sini. Payung yang di ujung sana hampir patah tuh kena angin."
            harumi "Mereka memilih jalur tengah yang tidak terlindung bangunan. Padahal lewat koridor samping perpustakaan hanya lebih jauh dua menit."
            yutaka "Rajin juga ya kamu, selalu bawa cadangan teh sebanyak itu. Memangnya sering bagi-bagi teh bareng anak-anak di laboratorium?"
            nar "Harumi menoleh sedikit ke arahmu. Nada suaranya tetap tenang tanpa dibuat-buat, tetapi jawabannya terdengar begitu jujur."
            harumi "Jarang sekali. Awalnya cuma karena ukuran teko seduhku memang lebih besar dari takaran satu gelas, dan rasanya mubazir kalau sisanya dibuang begitu saja."
            yutaka "Terus biasanya kamu habiskan sendiri sampai malam?"
            harumi "Kadang tidak habis juga. Selama ini tidak pernah ada yang bertanya untuk siapa sisa teh di dalam termosku. Hari ini jawabannya jadi jelas."
            yutaka "Kalau begitu, jatah sisanya kuterima dengan senang hati. Lain kali gantian aku yang traktir kopi atau camilan di kantin ya, Kujo-san."
            harumi "Tidak perlu dihitung sebagai utang, Kisaragi-kun. Pelan-pelan saja minumnya, bagian bawah termos suhunya masih cukup panas."
            yutaka "Bukan soal utang kok, sekadar traktir balik biar adil. Wah, hujannya mulai agak kecil sedikit tuh."
            harumi "Tunggu lima menit lagi saja supaya genangan di tangga surut dulu."
            nar "Selama beberapa menit berikutnya, kalian berdiri berdampingan di bawah atap beton, ditemani suara guyuran hujan dan uap teh hangat yang menenangkan."
    else:
        if kk_host == "chiasa":
            nar "Kamu menyesap sedikit teh dari tutup termos itu. Uapnya memang menghangatkan mulut, tetapi begitu rasa pahit daun teh yang pekat dan sepat menyentuh lidahmu, keningmu refleks sedikit berkerut."
            chiasa "Terima kasih banyak, Kujo-senpai, hangat sih di tenggorokan... tapi maaf, buat lidahku seduhan ini agak terlalu pahit."
            nar "Harumi menerima kembali tutup termos itu darimu tanpa menunjukkan raut tersinggung atau marah. Ia menatap permukaan teh yang tersisa sejenak, lalu mencicipi sedikit dari sisi tutupnya untuk memeriksa sendiri."
            harumi "Hmm. Kepahitan di akhir kecapan ini memang karakter dari jenis daun teh panggang tua yang kupilih pagi tadi, ditambah waktu seduh tiga menit penuh. Wajar kalau tidak semua orang cocok dengan rasanya."
            chiasa "Mungkin karena aku biasanya minum teh melati atau teh susu yang lebih ringan, Senpai."
            harumi "Masuk akal. Perbedaan tingkat panggangan daun sangat memengaruhi rasa akhirnya di lidah."
            nar "Meskipun nadanya tetap tenang dan rasional seperti sedang mengevaluasi hasil percobaan laboratorium, gerakannya saat mengosongkan sisa tetesan teh ke saluran air teras dan memutar kembali tutup termos baja itu tampak sedikit lebih cepat daripada biasanya."
            nar "Ia memasukkan termosnya kembali ke dalam tas kain dan menarik ritsletingnya hingga tertutup rapat."
            harumi "Lain kali aku akan menanyakan seleramu dulu sebelum langsung menyodorkannya, Amamiya-san. Aku terlalu cepat menyimpulkan bahwa sesuatu yang menurutku pas pasti nyaman juga bagi orang lain."
            chiasa "Eh, jangan salah paham, Senpai! Maksudku tidak begitu. Aku tetap senang dan menghargai tawarannya kok, sungguh. Cuma lidahku saja yang memang kurang biasa minum teh pekat tanpa gula."
            harumi "Aku mengerti kok. Secara objektif tidak ada yang salah dengan perbedaan sensitivitas rasa. Kamu tidak perlu merasa bersalah."
            chiasa "Tetap saja, aku jadi nggak enak karena tidak kuhabiskan..."
            harumi "Sungguh tidak masalah. Lebih baik kamu jujur daripada memaksa menelan minuman yang tidak kamu sukai."
            chiasa "Makasih ya, Kujo-senpai, tadi sudah repot-repot menuangkan."
            harumi "Sama-sama. Sepertinya anginnya mulai melemah sedikit, mungkin sepuluh menit lagi sudah cukup aman untuk jalan."
            nar "Ia membetulkan letak kacamatanya sekali, lalu kembali memandang lurus ke arah hujan yang turun deras di halaman. Tidak ada kata-kata tajam di antara kalian, tetapi batas sopan yang formal terasa kembali terpasang rapi di bawah atap teras itu."
        else:
            nar "Kamu menyesap sedikit teh dari tutup termos itu. Hangatnya memang terasa di tenggorokan, tetapi rasa pahit daun teh yang pekat dan sepat langsung menyentuh lidah hingga keningmu refleks berkerut."
            yutaka "Makasih, Kujo-san, lumayan bikin hangat... tapi kalau boleh jujur, buat seleraku ini seduhannya agak terlalu pahit."
            nar "Harumi mengambil kembali tutup termos itu tanpa menunjukkan raut tersinggung. Ia menatap permukaannya sejenak, lalu mencicipi sedikit sisa teh di pinggir tutup itu untuk memastikan sendiri sebelum mengangguk singkat."
            harumi "Kepahitan di ujungnya memang karakter daun teh yang kupilih pagi ini, ditambah waktu ekstraksi tiga menit penuh. Wajar kalau tidak cocok di lidah semua orang."
            yutaka "Kayaknya lidahku saja yang kebanyakan minum kopi susu sama teh botolan manis."
            harumi "Kalau terbiasa dengan minuman bergula, teh seduh murni tanpa campuran memang akan terasa jauh lebih tajam."
            nar "Meski ucapannya tetap tenang dan objektif seperti sedang membaca catatan praktikum, caranya memutar kembali tutup termos baja dan memasukkannya ke dalam tas kain terasa sedikit lebih ringkas daripada saat ia mengeluarkannya tadi."
            harumi "Lain kali aku tanya preferensimu dulu sebelum menawari, Kisaragi-kun. Aku terlalu cepat menganggap takaran yang kusukai pasti cocok untuk menolong orang lain juga."
            yutaka "Eh, jangan salah paham dulu, aku tetap berterima kasih banget sudah dikasih minum hangat. Cuma lidahku saja yang kurang biasa sama teh pekat."
            harumi "Aku paham. Secara objektif selera rasa memang berbeda-beda dan sama sekali bukan hal yang perlu diperdebatkan. Tidak apa-apa."
            yutaka "Iya... maaf ya jadi nggak kuhabiskan."
            harumi "Tidak masalah. Lebih baik langsung bilang terus terang daripada memaksa menghabiskannya demi kesopanan. Sepertinya arah anginnya mulai melambat sedikit, sebentar lagi mungkin sudah bisa jalan."
            yutaka "Iya, hujannya mulai kelihatan lebih tipis."
            nar "Ia membetulkan kacamatanya sekali lalu kembali menatap lurus ke arah hujan di halaman. Tidak ada suasana permusuhan, tetapi jarak formal yang sopan di antara kalian berdua terasa kembali menutup rapat."
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
    if kk_host == "chiasa":
        nar "Kelompok belajar sore di Kafe Komorebi akhirnya bubar dengan pola yang sama seperti minggu-minggu sebelumnya. Begitu soal terakhir selesai dibahas, teman-teman yang lain segera memasukkan catatan ke dalam tas dan berpamitan satu per satu sambil membawa lembar jawaban yang sudah lengkap."
        nar "Lonceng kecil di atas pintu kafe berdenting beberapa kali sampai ruang sudut itu akhirnya kembali lengang. Hanya Kujo Harumi yang masih berdiri memutari meja kayu panjang tersebut, menunduk memeriksa deretan kursi dan kolong meja untuk memastikan tidak ada pulpen, penghapus, atau buku catatan milik siapa pun yang tertinggal."
        chiasa "Semua barang anak-anak sudah terbawa lengkap, Kujo-senpai?"
        harumi "Sudah, Amamiya-san. Tadi hanya ada satu lembar kertas buram di bawah kursi pojok sana, tapi isinya cuma coretan rumus awal yang salah hitung. Sudah kubuang ke tempat sampah."
        nar "Kamu baru saja hendak menyampirkan tali tas ke bahumu ketika melihat Harumi sempat melangkah setengah tapak ke arah pintu kaca kafe. Tatapannya tertuju ke luar jendela mengikuti punggung Koita dan teman-teman yang baru saja berjalan menjauh di trotoar, seperti baru teringat hendak memanggil seseorang. Tangannya tidak jadi terangkat; ia berhenti, lalu berbalik menoleh kepadamu."
        harumi "Amamiya-san, apakah sore ini kamu sedang buru-buru harus pulang ke rumah?"
        chiasa "Nggak buru-buru kok, Kujo-senpai. Di rumah sore ini juga nggak ada jadwal apa-apa. Memangnya kenapa, Senpai?"
        nar "Harumi membetulkan letak kacamatanya dengan dua jari. Ekspresinya tetap tenang dan datar seperti biasa, tetapi kalimat yang keluar berikutnya justru terdengar sangat polos dan jujur."
        harumi "Aku sebenarnya belum ingin obrolan sore ini selesai. Itu alasan yang jauh lebih jujur daripada aku berdalih masih harus menata cangkir-cangkir kosong di meja ini."
        chiasa "Hehe, Kujo-senpai jujur sekali kalau bicara."
        harumi "Tapi cangkir-cangkir bekasnya memang tetap perlu dikumpulkan ke satu tepi dulu sebelum pelayan kafenya datang membersihkan. Kalau dibiarkan menyebar begini kelihatannya terlalu berantakan."
        nar "Di tengah meja kayu itu masih tersisa satu teko keramik berisi teh melati hangat yang baru berkurang separuh, lengkap dengan dua cangkir bersih yang tadi belum sempat terpakai."
    else:
        nar "Kelompok belajar sore di Kafe Komorebi bubar dengan pola yang sama seperti biasanya. Begitu soal latihan terakhir selesai disimpulkan, anggota kelompok yang lain langsung merapikan buku masing-masing dan berpamitan satu per satu."
        nar "Lonceng pintu kafe berdenting beberapa kali hingga sudut meja panjang itu kembali sepi. Hanya Kujo Harumi yang masih berdiri memutari barisan kursi, menunduk memeriksa kolong meja supaya tidak ada buku catatan atau alat tulis milik teman-teman yang tertinggal."
        yutaka "Nggak ada barang anak-anak yang ketinggalan kan, Kujo-san? Tadi kulihat kayaknya semua sudah masuk tas masing-masing."
        harumi "Sudah aman semuanya, Kisaragi-kun. Tadi cuma ada satu kertas coretan soal yang jatuh di bawah kursi ujung, dan sudah kubuang karena tidak terpakai."
        nar "Kamu baru saja hendak menyampirkan tali tas ke bahu ketika melihat Harumi sempat melangkah setengah tapak ke arah pintu kaca depan. Pandangannya mengikuti rombongan Koita yang baru berjalan menjauh di luar trotoar, seperti hampir hendak memanggil salah satu dari mereka kembali. Ia mengurungkan niatnya, berhenti di tempat, lalu berbalik menoleh kepadamu."
        harumi "Kisaragi-kun, apakah kamu sedang buru-buru harus segera pulang sore ini?"
        yutaka "Nggak juga sih. Di apartemenku juga lagi nggak ada jadwal apa-apa sampai malam. Kenapa memangnya, Kujo-san?"
        nar "Harumi membetulkan letak kacamatanya dengan dua jari. Wajahnya tetap tenang dan datar, tetapi kalimat berikutnya meluncur tanpa sedikit pun basa-basi."
        harumi "Aku sebenarnya belum ingin waktu ngobrolnya selesai begitu saja. Itu alasan yang lebih akurat daripada aku beralasan masih harus merapikan cangkir-cangkir kosong di meja ini."
        yutaka "Jujur banget ya kamu kalau ngomong, Kujo-san."
        harumi "Tapi cangkir dan piring bekasnya memang tetap harus ditumpuk rapi dulu sebelum pelayannya ke sini. Meja sebesar ini tidak enak dilihat kalau ditinggal berantakan."
        nar "Di ujung meja masih tersisa satu teko keramik teh melati yang baru diminum setengahnya, beserta dua cangkir bersih yang belum sempat dipakai sejak sore."
    call kk_family_menu("H05", ["\"Sini kubantu beresin cangkir sekalian tuang teh buat kita berdua.\"", "\"Habis lulus nanti, kamu rencananya mau lanjut ke mana?\"", "\"Ada nggak sih hal pribadi di luar kampus yang belum pernah kamu ceritain?\""])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu menurunkan kembali tasmu ke atas kursi, lalu melangkah meraih baki kayu kosong yang terletak di ujung meja."
            chiasa "Sini kubantu bereskan cangkir-cangkir kotornya ke baki, Kujo-senpai. Sekalian nanti aku tuangkan sisa teh melatinya buat kita berdua, mumpung tekonya masih hangat."
            harumi "Dikerjakan berdua memang jauh lebih efisien. Terima kasih, Amamiya-san. Hati-hati waktu mengangkat tekonya, bagian pangkal gagangnya tadi agak licin."
            nar "Kalian membagi tugas dengan tenang tanpa perlu banyak aba-aba. Harumi mengumpulkan piring-piring kecil bekas camilan dan sendok pengaduk ke atas baki kayu, sementara kamu mengelap sedikit tetesan air di meja dengan tisu lalu menuangkan teh melati yang masih mengepul ke dalam dua cangkir bersih."
            nar "Setelah meletakkan baki berisi peralatan kotor dengan rapi di sudut meja luar agar mudah diambil pelayan, kamu tidak langsung berdiri mengambil tasmu. Kamu justru menarik kursi kayu tepat di seberang Harumi, duduk bersandar santai, dan menggeser satu cangkir teh hangat ke hadapannya."
            chiasa "Nah, mejanya sudah rapi semua. Silakan diminum tehnya, Senpai."
            nar "Harumi ikut menarik kursinya dan duduk perlahan. Ia menatap baki yang sudah tertata rapi di ujung meja, lalu menatapmu balik dengan sudut bibir yang sedikit terangkat."
            harumi "Pekerjaan merapikan meja yang tadi kujadikan alasan sudah selesai kurang dari tiga menit, tapi kamu masih tetap duduk di sini."
            chiasa "Kan tadi Kujo-senpai sendiri yang bilang alasan sebenarnya karena belum pengin obrolannya selesai. Lagian sayang sekali kalau teh melati sewangi ini dibiarkan dingin tanpa diminum."
            harumi "...Evaluasi yang tepat. Aku tidak punya bantahan kalau kamu mengutip kalimatku sendiri."
            nar "Ia mengangkat cangkirnya dan menyesap teh melati itu perlahan, lalu melirik papan menu kecil yang berdiri di samping kotak tisu."
            harumi "Kalau begitu, izinkan aku memesan sepotong kue bolu teh hijau untuk kita bagi berdua sebagai teman minum tehnya. Anggap saja pembagian upah karena kamu sudah membantu merapikan meja."
            chiasa "Wah, kalau ditraktir kue bolu di sini sih aku jelas nggak bakal menolak, Senpai."
            harumi "Kesepakatan tercapai. Tunggu sebentar, aku panggilkan pelayannya."
            nar "Pertemuan yang tadinya nyaris bubar begitu saja akhirnya memanjang menjadi waktu santai yang hangat, tanpa ada lagi yang perlu mencari-cari alasan formal untuk tetap duduk bersama."
        else:
            nar "Kamu menaruh tasmu kembali ke atas kursi sebelah, lalu langsung meraih baki kayu kosong di sudut meja."
            yutaka "Sini kubantu kumpulin cangkir-cangkir bekasnya, Kujo-san. Sekalian kutuangkan sisa teh hangat di teko itu buat kita berdua, sayang kalau ditinggal."
            harumi "Dikerjakan berdua memang lebih cepat selesai. Terima kasih, Kisaragi-kun. Hati-hati waktu menuang tekonya, tutup keramiknya agak longgar."
            nar "Kalian membagi pekerjaan tanpa perlu banyak instruksi. Harumi menyusun piring-piring kecil dan sendok bekas ke atas baki kayu, sementara kamu menahan tutup teko dan menuangkan teh melati yang masih mengepulkan uap harum ke dalam dua cangkir bersih. Dalam waktu singkat, meja panjang itu sudah kembali bersih dan lapang."
            nar "Begitu baki kotor disisihkan ke tepi meja, kamu tidak langsung berdiri mengambil tas. Kamu justru menarik kursi di seberang Harumi, duduk dengan santai, lalu mendorong satu cangkir hangat ke depannya."
            yutaka "Beres semua. Diminum dulu tehnya, Kujo-san, mumpung masih hangat."
            nar "Harumi ikut duduk di kursinya. Ia melirik baki yang sudah beres di ujung meja, lalu menatapmu dengan sudut bibir yang sedikit terangkat geli."
            harumi "Pekerjaan merapikan cangkir yang kujadikan alasan tadi sudah habis semua, tapi kamu ternyata masih duduk di sini."
            yutaka "Kan tadi kamu sendiri yang bilang alasan aslinya gara-gara belum pengin obrolannya selesai. Masa setelah mejanya bersih aku malah langsung kabur."
            harumi "...Benar juga. Argumenmu sangat konsisten kali ini."
            nar "Ia menyesap tehnya pelan, lalu melirik daftar menu makanan penutup di samping tempat tisu."
            harumi "Karena kamu sudah membantu membereskan meja dan menemaniku duduk lebih lama, biar kupesankan satu porsi kue keju panggang untuk kita makan berdua. Jangan menolak, ini bentuk timbal balik yang adil."
            yutaka "Wah, kalau ditawari traktiran kue di Komorebi sih mana mungkin aku nolak, Kujo-san."
            harumi "Bagus. Sebentar, aku panggil pelayannya dulu."
            nar "Sore yang tadinya hampir berakhir di depan pintu kafe itu pun berlanjut dengan obrolan ringan yang nyaman tanpa perlu alasan tambahan."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kamu menarik kursi dan duduk kembali di seberangnya, menuangkan teh melati hangat ke kedua cangkir bersih, lalu menangkupkan kedua telapak tanganmu di sisi cangkir keramik."
            chiasa "Ngomong-ngomong, Kujo-senpai kan kelihatan selalu serius dan terarah sekali setiap kali bahas materi kuliah atau praktikum laboratorium. Setelah lulus sarjana nanti, Senpai rencananya mau lanjut ke mana?"
            nar "Harumi ikut duduk di kursinya dan menerima cangkir hangat darimu. Ia memandangi uap tipis yang naik dari permukaan teh beberapa detik sebelum menjawab."
            harumi "Melanjutkan ke program pascasarjana sampai doktoral, lalu mengabdi di universitas sebagai peneliti dan profesor. Itu jalur yang sudah kurencanakan sejak sekolah menengah."
            chiasa "Wah, jadi profesor universitas? Keren sekali! Orang tua Senpai di rumah pasti mendukung penuh ya kalau dengar rencana sebesar itu?"
            nar "Mendengar pertanyaanmu tentang orang tuanya, jari Harumi yang sedang memegang gagang cangkir tampak berhenti sesaat. Ia tersenyum tipis yang tampak agak datar."
            harumi "Orang tuaku di rumah... mereka adalah tipe pendidik yang mengukur hampir segala hal di dunia ini lewat angka, nilai ujian, dan peringkat resmi, Amamiya-san. Sejak kecil aku sudah sangat terlatih membaca jawaban atau pilihan hidup seperti apa yang akan membuat mereka mengangguk puas."
            chiasa "Berarti... rencana Senpai buat lanjut sampai jadi profesor itu awalnya karena tuntutan mereka juga?"
            harumi "Dua tahun lalu aku sempat cukup lama terjebak memikirkan pertanyaan itu. Aku tidak yakin apakah aku sungguh-sungguh menginginkan jalur akademik, atau aku hanya memilihnya karena gelar profesor adalah puncak pencapaian yang paling mereka anggap layak di keluarga kami."
            chiasa "Terus kalau sekarang gimana perasaan Senpai sendiri?"
            nar "Harumi mengangkat wajahnya, menatapmu lurus dengan sorot mata biru tua yang jernih dari balik kacamatanya."
            harumi "Setelah menjalaninya sendiri di kampus ini, sekarang aku mulai tahu bedanya. Aku ternyata memang menyukai proses mencari tahu sesuatu secara mendalam, menguji hipotesis pelan-pelan di laboratorium, dan membantu menjelaskan materi kepada teman-teman yang sedang kesulitan seperti di kelompok belajar tadi. Bukan semata-mata demi nama gelarnya."
            chiasa "Bagian itu kelihatan jelas kok, Senpai. Setiap kali Senpai mengajari kami yang dari jurusan lain, Senpai sabar sekali menjelaskannya dari dasar."
            harumi "Terima kasih, Amamiya-san. Beberapa bulan lalu aku sempat mengajukan satu pertanyaan uji kepada diriku sendiri, seandainya suatu hari nanti kedua orang tuaku tidak lagi merasa bangga atau tidak menyetujui bidang riset pilihanku, apakah aku masih tetap ingin menempuh jalan ini? Sejauh ini jawabannya tetap iya. Dan menyadari hal itu membuatku merasa jauh lebih lega."
            chiasa "Aku senang dengarnya, Kujo-senpai. Berarti sekarang itu sudah benar-benar jadi cita-cita milik Senpai sendiri."
            nar "Harumi mengangguk pelan lalu menyesap teh hangatnya. Bahunya yang biasanya selalu tegak dan kaku tampak jauh lebih rileks saat berbagi cerita itu denganmu."
        else:
            nar "Kamu kembali duduk di kursi seberangnya, menuangkan sisa teh melati hangat ke dalam dua cangkir bersih, lalu menyandarkan siku dengan santai di tepi meja."
            yutaka "Ngomong-ngomong, Kujo-san, aku sering perhatikan kamu kayaknya paling fokus kalau sudah urusan riset dan akademik. Habis lulus sarjana nanti, kamu rencananya mau langsung kerja atau lanjut ke mana?"
            nar "Harumi ikut duduk dan menarik cangkir teh yang kamu tuangkan ke hadapannya. Ia menatap uap tipis dari permukaan teh itu selama beberapa detik sebelum menjawab."
            harumi "Lanjut ke sekolah pascasarjana, mengambil gelar doktor, lalu bekerja di universitas sebagai profesor riset. Dari dulu jalur rencanaku memang selalu mengarah ke sana."
            yutaka "Langsung target jadi profesor ya. Orang tuamu di rumah pasti bangga sekali punya anak yang jalurnya sudah selurus itu."
            nar "Jari Harumi berhenti memutar gagang cangkir keramiknya. Ia menyunggingkan senyum tipis yang tidak benar-benar sampai ke matanya."
            harumi "Keluargaku mengukur hampir seluruh kehidupan lewat indikator yang bisa dihitung, Kisaragi-kun. Nilai rapor, peringkat nasional, jumlah publikasi ilmiah. Sejak kecil aku tumbuh dengan mempelajari standar ukuran mereka terlebih dahulu sebelum sempat mengenali caraku sendiri menilai sesuatu."
            yutaka "Jadi awalnya target jadi profesor itu gara-gara mengikuti standar orang tuamu?"
            harumi "Dulu aku sempat cukup lama meragukan diriku sendiri soal itu. Aku bertanya-tanya apakah aku mengejar jalur akademik karena keinginanku sendiri, atau hanya karena itu satu-satunya jawaban yang pasti mendapat persetujuan penuh di meja makan rumah."
            yutaka "Terus setelah kuliah di sini, kamu sudah nemu jawabannya?"
            nar "Harumi mengangkat pandangannya dan menatapmu lurus dari balik lensa kacamatanya."
            harumi "Sekarang aku sudah bisa memisahkan keduanya. Aku sadar bahwa aku memang menikmati ruang untuk mengamati, meneliti sesuatu tanpa tergesa-gesa, dan membimbing orang lain memahami konsep yang rumit. Kepuasanku ada pada proses belajarnya sendiri."
            yutaka "Itu kelihatan banget sih tiap kali kamu dengan sabar ngajarin kita-kita yang otaknya sering buntu waktu belajar kelompok."
            harumi "Beberapa waktu lalu aku sempat menguji diriku dengan satu pertanyaan. Kalau suatu hari nanti orang tuaku kecewa atau tidak lagi bangga pada jalur penelitian yang kupilih, apakah aku masih tetap akan mengambil jalan ini? Sejauh ini jawabanku tetap iya. Dan kepastian itu membuat beban di kepalaku jauh lebih ringan."
            yutaka "Bagus sekali kalau begitu, Kujo-san. Berarti kamu benar-benar jalan buat masa depanmu sendiri, jauh di luar sekadar memenuhi daftar angka orang tuamu."
            nar "Harumi mengangguk pelan dengan raut wajah yang tampak jauh lebih teduh saat ia mengangkat cangkir tehnya."
    else:
        if kk_host == "chiasa":
            nar "Kamu duduk kembali di kursi seberangnya, menuangkan teh ke cangkir kalian, lalu menopang dagu dengan satu tangan sambil menatapnya penuh rasa ingin tahu."
            chiasa "Kujo-senpai kan selama ini di kampus jarang sekali cerita soal hal-hal di luar urusan kuliah, buku, atau laboratorium. Sebenarnya ada nggak sih hal pribadi yang Senpai simpan rapat-rapat dan belum pernah diceritakan ke siapa pun di sini?"
            nar "Gerakan tangan Harumi yang baru saja hendak meraih cangkir tehnya langsung terhenti. Ia terdiam sejenak, menatapmu dengan tenang dari balik kacamatanya, lalu menggeleng pelan."
            harumi "...Jarang sekali ada orang yang langsung menanyakan hal seperti itu tepat di depan wajahku, Amamiya-san."
            chiasa "Eh, maaf, Kujo-senpai! Pertanyaanku barusan terlalu lancang dan melewati batas ya?"
            harumi "Tidak, aku sama sekali tidak merasa tersinggung. Kalau harus menjawab dengan jujur, tentu saja ada beberapa hal tentang diriku dan keluargaku yang belum pernah kuceritakan di kampus ini. Tapi sepertinya belum waktunya kuceritakan sekarang. Mungkin di lain kesempatan."
            chiasa "Oh, begitu. Iya, nggak apa-apa kok, Senpai, aku sama sekali nggak memaksa."
            nar "Meskipun ia memasang batas yang tegas bahwa ia belum siap membuka urusan pribadinya hari ini, suasana di meja kalian tidak berubah menjadi dingin. Harumi menyesap tehnya sedikit, meletakkan cangkirnya kembali dengan rapi, lalu menatapmu dengan rasa ingin tahu yang seimbang."
            harumi "Kalau kamu sendiri bagaimana, Amamiya-san? Minggu ini di studio Fakultas Seni Rupa apakah ada tugas lukis atau proyek yang sedang membuatmu kesulitan?"
            chiasa "Lumayan ada sih, Senpai. Minggu depan ada tenggat pengumpulan sketsa ruang terbuka, tapi sampai hari ini aku masih bingung menentukan sudut lokasi mana yang pencahayaannya paling bagus."
            harumi "Kalau kamu mencari sudut dengan kontras bayangan yang tenang dan tidak banyak orang lalu-lalang, balkon baca di lantai tiga perpustakaan utama biasanya kosong setelah pukul empat sore. Cahaya matahari barat yang masuk lewat jendela tingginya sangat jelas garisnya."
            chiasa "Wah, aku belum pernah naik sampai ke balkon lantai tiga perpustakaan sore-sore. Besok sehabis kelas bakal kucoba bawa buku sketsaku ke sana. Terima kasih sarannya, Senpai!"
            nar "Kamu tetap duduk menemani obrolannya sampai teh melati di dalam teko habis tak bersisa. Penolakan halusnya tadi sama sekali tidak memutus percakapan, melainkan menandai sebuah pintu yang kelak baru akan ia buka jika kepercayaan di antara kalian sudah cukup dalam."
        else:
            nar "Kamu duduk kembali di seberangnya setelah menuangkan teh ke kedua cangkir, lalu menopang dagu sambil memancingnya dengan nada bicara santai."
            yutaka "Kujo-san kan kalau lagi kumpul bareng jarang sekali bahas urusan di luar materi kuliah, buku bacaan, atau jadwal lab. Sebenarnya ada nggak sih rahasia atau urusan pribadi yang selama ini kamu simpan sendiri dan belum pernah kamu ceritakan ke siapa-siapa?"
            nar "Gerakan tangan Harumi di dekat cangkir keramiknya berhenti sejenak. Ia menatapmu dengan sorot mata tenang dari balik kacamatanya, lalu menggeleng perlahan."
            harumi "...Jarang ada orang yang bertanya langsung ke inti seperti itu tanpa pembuka, Kisaragi-kun."
            yutaka "Eh, terlalu kelewat batas ya pertanyaanku barusan? Maaf kalau kesannya mengorek-ngorek."
            harumi "Tidak, aku tidak tersinggung kok. Kalau dijawab secara faktual, memang ada beberapa hal pribadi yang belum pernah kubicarakan dengan siapa pun di sini. Hanya saja belum saatnya kuceritakan sore ini. Mungkin lain kali."
            yutaka "Oke, santai saja. Aku nggak bakal memaksa kalau kamu memang belum mau cerita."
            nar "Harumi menetapkan batasnya dengan lugas tanpa membuat suasana meja menjadi kaku. Ia menyesap teh hangatnya satu kali, lalu langsung mengalihkan pembicaraan dengan menanyakan kabarmu secara tulus."
            harumi "Kalau dari pihakmu sendiri bagaimana, Kisaragi-kun? Mata kuliah statistik ekonomi yang kamu keluhkan minggu lalu apakah materinya sudah lebih bisa diikuti?"
            yutaka "Wah, jangan ditanya yang itu. Kemarin saja waktu dosennya nurunin rumus distribusi di papan tulis, aku sudah hampir menyerah di baris ketiga."
            harumi "Bagian penurunan rumus awalnya memang sering dilompati di buku teks ekonomi. Kalau minggu depan kamu masih bingung waktu mengerjakan lembar latihannya, bawa saja buku catatanmu ke sini. Aku bisa bantu jelaskan langkah dasarnya."
            yutaka "Serius kamu mau bantu ngajarin bagian itu? Wah, tertolong banget aku kalau begitu, Kujo-san."
            nar "Kalian berdua melanjutkan obrolan sore itu hingga teh di dalam teko habis. Meskipun pintu menuju rahasia pribadinya belum terbuka hari ini, kesediaannya untuk tetap duduk dan berbincang denganmu menunjukkan bahwa ia menghargai kehadiranmu."
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
