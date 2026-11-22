# Arc Moeka (Mo03-Mo12, Mo26): wakil kelas dari keluarga miskin dengan tiga adik
# dan ayah sakit; tekanan finansial/akademik, gerbang awal fotografer Kuga, dan
# jendela intervensi menjelang krisis. Ditulis sebagai KARAKTER dan KONSEKUENSI;
# eksploitasi/krisis hanya akibatnya yang dicatat, tanpa metode. Penempatan di
# Kantin Pusat adalah prototipe reachability (🟡); locale naratif ada di dialog.
# Efek menggerakkan stres_moeka, stage[moeka], beban_keluarga. Event_Moeka.

init 1 python:
    def kk_moeka_burden(delta):
        pts.setdefault("beban_keluarga", 0)
        kk_adj("beban_keluarga", delta)
    def kk_moeka_stage(n):
        kk_stage("moeka", max(n, stage.get("moeka", 0)))

# ┌─ PANDUAN CERITA · Mo03 · Janji yang Terlupa
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia lupa janji dengan pemain.
# │ INTI    : A marah / B maklum / C bantu mengatur jadwal.
# │ AKHIRAN : Trust; B/C mengurangi stres.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo03:
    call kk_scene_enter("moeka", "Kantin Pusat · Janji terlupa")
    if kk_host == "chiasa":
        nar "Hujan gerimis pertengahan Juni menempel di kaca jendela besar Kantin Pusat yang mulai lengang selepas jam makan siang. Bau samar kuah udon dan kopi dari mesin penjual otomatis masih menggantung di udara, sementara di luar, payung-payung mahasiswa melintas pelan di halaman yang basah."
        nar "Di atas meja kayu di hadapanmu, segelas teh hijau hangat yang kamu pesan hampir satu jam lalu sudah lama kehilangan uapnya. Ketika jari-jarimu menyentuh dinding gelasnya, yang tersisa hanyalah permukaan dingin yang lembap, sama sunyinya dengan layar ponselmu yang belum menampilkan satu pun balasan pesan."
        nar "Kamu sempat membuka ruang obrolan sekali lagi, membaca ulang pesan kemarin sore untuk memastikan hari, jam, dan tempat yang kalian sepakati memang benar di Kantin Pusat pukul satu. Tidak ada satu pun tanda pesan dibaca sejak sebelum tengah hari."
        nar "Kamu menghela napas pelan dan melirik jam dinding kantin yang jarum panjangnya hampir genap berputar satu putaran penuh sejak waktu janji kalian lewat. Baru saja kamu merapikan buku sketsa ke dalam tas dan menyampirkan talinya ke bahu, suara pintu kaca kantin yang didorong tergesa membuatmu menoleh."
        nar "Kohinata Moeka berlari kecil menyusuri sela-sela deretan meja dengan napas tersengal. Ujung rambut merah muda panjangnya yang bergelombang tampak lembap terkena tempias hujan, tali kartu panitia masih melingkar miring di kerahnya, dan di tepi bawah kardigan rajutnya yang berhias renda jahitan tangan, sebuah peniti perak kecil tersemat darurat untuk menahan keliman benang yang terlepas."
        nar "Sebelum ia sempat menarik kursi di hadapanmu, ponsel di dalam saku kardigannya kembali bergetar nyaring oleh rentetan pesan masuk. Ia merogoh sakunya, mematikan getaran itu tanpa sempat melirik layar, lalu menangkupkan kedua tangan di depan wajah dengan raut penuh rasa bersalah."
        moeka "Chimian! Aduh, maaf, aku benar-benar minta maaf sudah telat sejauh ini!"
        nar "Moeka menurunkan tas kanvas besarnya yang menggembung penuh gulungan kain contoh dan map kepanitiaan ke kursi sebelah, lalu menarik napas pendek-pendek untuk menenangkan dadanya yang masih naik turun."
        chiasa "Pelan-pelan dulu napasnya, Moemoe-senpai. Senpai habis lari dari gedung sebelah?"
        moeka "Iya, lari potong jalan lewat selasar belakang tadi. Rapat panitia festival molor hampir satu jam gara-gara divisi panggung mendadak minta rombak daftar perlengkapan, terus begitu aku baru keluar pintu ruang rapat, adikku telepon dari rumah nanyain jadwal obat Ayah. Aku baru sadar janji kita sudah lewat jauh waktu lihat jam di koridor."
        chiasa "Urusan rumah sudah beres ditelepon tadi?"
        moeka "Sudah, untung cuma salah paham soal jadwal minum obat malamnya saja... tapi gara-gara panik, aku lupa total kalau harus ketemu kamu jam satu."
        chiasa "Kardigan Senpai bagian bawahnya juga sempat tersangkut sesuatu ya? Ada peniti di pinggir rendanya."
        moeka "Eh? Oh, iya! Tadi kesangkut gagang kursi waktu buru-buru keluar ruang rapat, jadi kupasangin peniti dulu biar benangnya nggak makin ketarik."
        nar "Matanya yang biru cerah turun ke arah gelas teh di depanmu yang sudah tak beruap lagi. Senyum cerah yang biasanya selalu siap sedia di wajahnya langsung meredup."
        moeka "Kamu pasti sudah nunggu lama sekali di sini, ya... gelas tehmu sampai dingin begitu. Ponselku tadi kusetel hening di dasar tas selama rapat, jadi aku sama sekali nggak sempat kirim kabar kalau bakal telat. Aku benar-benar minta maaf ya, Chimian."
    else:
        nar "Hujan gerimis pertengahan Juni menempel tipis di kaca jendela besar Kantin Pusat yang mulai lengang selepas jam makan siang. Suara piring dicuci dari balik konter dapur terdengar samar, bercampur bunyi rintik air yang jatuh terus-menerus di saluran pembuangan luar."
        nar "Di atas meja kayu di hadapanmu, segelas kopi hitam dari mesin penjual otomatis yang kamu beli hampir satu jam lalu sudah lama kehilangan hangatnya. Dinding cangkir kertas itu terasa dingin di ujung jari, menyisakan lingkar embun tipis di permukaan kayu."
        nar "Kamu sempat memeriksa ulang pesan kemarin malam di layar ponsel, memastikan kamu tidak salah hari atau salah gedung. Pesan terakhirmu yang menanyakan posisinya setengah jam lalu bahkan belum terbaca."
        nar "Kamu menyandarkan punggung ke kursi sambil memutar ponsel pelan di atas meja. Baru saja kamu menghela napas, memasukkan ponsel ke saku celana, dan bersiap berdiri, daun pintu kaca kantin didorong tergesa dari luar."
        nar "Kohinata Moeka berlari kecil menyusuri lorong di antara meja-meja kosong dengan napas memburu. Ujung rambut merah muda panjangnya yang bergelombang basah terkena tempias hujan, tali tanda pengenal panitia masih miring di bahunya, dan di tepi bawah kardigannya yang berhias renda jahitan tangan, sebuah peniti perak kecil menahan keliman kain yang mulai terurai."
        nar "Sebelum ia sempat memegang sandaran kursi di seberangmu, ponsel di dalam saku kardigannya kembali bergetar keras oleh rentetan notifikasi masuk. Ia merogoh saku dengan satu tangan, menekan tombol samping untuk membungkam getarannya tanpa melihat layar, lalu menatapmu dengan wajah penuh penyesalan."
        moeka "Yutayuta! Aduh, maaf, aku benar-benar minta maaf sudah bikin kamu nunggu selama ini!"
        nar "Ia meletakkan tas kanvas beratnya yang penuh gulungan kain dan map kertas ke kursi sebelah, lalu menangkupkan kedua tangan di depan dagu sambil mengatur napasnya yang masih terengah."
        yutaka "Kamu lari dari gedung rapat sampai ke sini, Kohinata? Ujung rambutmu basah semua itu."
        moeka "Iya, tadi terobos gerimis sedikit di halaman tengah. Rapat panitia molor hampir satu jam gara-gara bagian panggung mendadak ganti daftar barang, terus pas aku baru keluar ruangan, adikku telepon dari rumah nanyain jadwal obat Ayah. Aku baru ingat janji kita waktu sudah lari turun tangga."
        yutaka "Urusan rumahmu sudah aman tadi?"
        moeka "Untung sudah, cuma perlu kuingatkan jadwal minum obat malamnya saja... tapi gara-gara panik, otakku langsung kosong dan lupa janji sama kamu."
        yutaka "Keliman kardiganmu juga sampai ditahan peniti begitu, habis kesangkut apa?"
        moeka "Oh, tadi kesangkut sudut meja ruang rapat waktu aku buru-buru berdiri. Untung di tas selalu ada peniti cadangan biar rendanya nggak sobek panjang."
        nar "Matanya yang biru cerah tertuju pada cangkir kopi dingin di depanmu, dan bahunya tampak turun karena malu."
        moeka "Kamu sudah duduk nunggu dari sejam lalu, ya... aku nggak bakal bisa beralasan cuma telat sebentar kalau kopimu saja sudah dingin begitu. Ponselku tadi kusetel hening di dalam tas waktu rapat, jadi aku sama sekali nggak sempat ngabarin. Maaf banget ya, Yutayuta."
    call kk_family_menu("Mo03", ["\"Aku sudah menunggu hampir sejam sampai minumanku dingin.\"", "\"Tidak apa-apa, tarik napas dulu saja.\"", "Tawarkan bantuan untuk menyusun ulang jadwal di ponselnya."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu tidak memaksakan senyum maklum untuk menutupi waktu yang sudah terbuang. Kamu menggeser pelan gelas teh yang sudah dingin itu beberapa sentimeter ke tengah meja, lalu menatap Moeka dengan nada bicara yang tenang tetapi tegas."
            chiasa "Aku memang sudah menunggu hampir satu jam di sini sampai minumanku dingin, Moemoe-senpai. Lima menit lagi tadi aku sudah mau pulang."
            nar "Moeka menarik kursi di seberangmu dan duduk perlahan. Kedua tangannya meremas tali tas kanvas di atas pangkuannya, sama sekali tidak mencoba memotong kalimatmu."
            chiasa "Kalau rapat panitianya molor atau ada telepon mendadak dari rumah, aku bisa mengerti kok. Urusan begitu memang nggak bisa ditebak. Tapi setidaknya kirim satu pesan singkat supaya aku tidak duduk menebak-nebak di sini tanpa kepastian."
            moeka "...Iya, kamu benar, Chimian. Aku nggak punya alasan buat membela diri. Harusnya waktu rapatnya lewat setengah jam tadi, aku izin keluar sebentar buat kirim pesan ke kamu. Aku salah total, maaf sekali lagi ya."
            chiasa "Lain kali jangan diulangi lagi, Senpai. Aku juga punya jadwal tugas studio yang harus kukerjakan sore ini, jadi satu jam itu lumayan terasa."
            moeka "Iya, aku janji lain kali pasti langsung kirim pesan duluan..."
            nar "Keheningan yang canggung sempat turun di atas meja selama beberapa detik, hanya diisi suara gerimis di kaca jendela. Kamu melihat jari-jari Moeka yang masih mencengkeram tali tasnya erat-erat. Tepat ketika kamu hendak membuka map catatanmu, ia mendadak mengangkat wajah dan memasang senyum lebar yang terdengar terlalu bersemangat."
            moeka "Eh, tapi ngomong-ngomong, Chimian! Tadi di ruang rapat sempat ada kejadian lucu lho. Waktu ketua panitia lagi serius banget jelasin denah panggung, kabel proyektornya kesenggol sampai gambarnya muter terbalik di papan tulis! Satu ruangan langsung heboh sendiri nahan ketawa, ahaha!"
            chiasa "Moemoe-senpai..."
            moeka "Terus tadi di lorong belakang juga ada kucing kampus yang ikut masuk berteduh sampai ngeong-ngeong minta makanan ke anak-anak divisi logistik! Lucu banget lho, Chimian!"
            chiasa "Senpai, kamu tidak perlu memaksa cerita hal lucu begitu sekarang."
            moeka "Oh iya! Di konter kantin sebelah sana katanya hari ini ada puding susu karamel baru yang cuma keluar sore hari. Biar aku yang beliin buat ganti tehmu yang sudah dingin itu ya! Tunggu di sini sebentar, aku lari beliin sekarang biar kamu nggak kesal lagi!"
            chiasa "Nggak usah lari beli puding segala, Senpai. Duduk saja dulu, kita selesaikan urusan catatan kita."
            moeka "Nggak apa-apa, cuma sebentar kok di konter depan situ! Sekalian aku mau beli air hangat buat tehmu, terus habis ini catatanmu langsung kubereskan secepat kilat! Mau roti isi sekalian nggak?"
            chiasa "Moemoe-senpai, aku serius, kamu nggak perlu menebusnya pakai traktiran. Duduk saja."
            moeka "Tapi aku nggak enak banget lihat gelas dingin itu! Sebentar saja ya, Chimian, janji nggak sampai dua menit!"
            nar "Ia sudah setengah berdiri dari kursinya, berbicara cepat dari satu kalimat ke kalimat lain dengan tawa nyaring yang dipaksakan di tengah kantin yang sepi. Semakin keras kamu menegurnya, semakin sibuk ia berusaha menambal kesalahannya dengan sikap ramah yang berlebihan, seolah satu jam yang hilang itu harus dibayar dengan seluruh tenaganya."
        else:
            nar "Kamu tidak repot-repot memasang senyum maklum atau melempar candaan untuk melunakkan suasana. Kamu mengetuk pelan sisi cangkir kopi dingin di hadapanmu dengan telunjuk, lalu menatap Moeka dengan nada bicara yang lugas."
            yutaka "Aku memang sudah duduk di sini hampir sejam sampai kopiku dingin, Kohinata. Kalau kamu telat dua menit lagi saja, aku sudah berdiri dan pulang tadi."
            nar "Moeka menarik kursi di seberangmu lalu duduk perlahan. Kedua tangannya menggenggam tali tas kanvasnya di atas lutut, kepalanya sedikit tertunduk menerima teguranmu tanpa menyela."
            yutaka "Rapat kepanitiaan molor atau ada telepon penting dari rumah itu hal yang biasa, aku nggak mempermasalahkan bagian itunya. Tapi mengetik satu baris pesan kan nggak sampai sepuluh detik. Jangan biarkan orang duduk menunggu tanpa kabar sama sekali."
            moeka "...Kamu benar, Yutayuta. Aku memang salah total hari ini. Harusnya waktu sadar rapatnya bakal molor panjang, aku keluar sebentar buat kirim kabar ke kamu. Nggak ada alasan buat ngeles, aku minta maaf."
            yutaka "Pastikan saja lain kali jangan kejadian lagi. Sore ini aku juga masih ada urusan lain."
            moeka "Iya, aku janji nggak bakal lupa ngabarin lagi..."
            nar "Suasana di meja kalian sempat hening dan kaku selama beberapa saat. Kamu sempat melihat buku-buku jarinya memutih karena terlalu kuat meremas tali tas. Baru saja kamu menarik buku catatan dari dalam tas, Moeka mendadak menegakkan punggungnya dan memasang senyum lebar yang terdengar terlalu riang."
            moeka "Eh, tapi tahu nggak sih, Yutayuta! Tadi di ruang rapat ada kejadian konyol banget lho! Waktu ketua lagi semangat presentasi anggaran, proyektornya mendadak mati terus layarnya malah nyangkut waktu mau digulung! Semua anak panitia langsung panik sendiri, ahaha!"
            yutaka "Kohinata..."
            moeka "Terus tadi pas aku lari lewat tangga belakang, ada kucing kampus ikut neduh di depan pintu logistik sambil ngeong kencang banget!"
            yutaka "Kamu nggak perlu maksain diri cerita macam-macam cuma buat nutupin canggung."
            moeka "Oh iya! Di konter depan hari ini ada kopi seduh panas sama roti melon yang baru keluar dari panggangan! Biar aku yang traktir buat ganti kopimu yang dingin ini ya! Tunggu sebentar di sini, aku lari beli sekarang biar suasana hatimu balik lagi!"
            yutaka "Nggak perlu beli roti segala, duduk saja dulu. Kita bereskan urusan kita sekarang."
            moeka "Cuma semenit kok ke konter situ, sekalian aku juga haus habis lari tadi! Habis itu daftar barangmu langsung kucatat rapi tanpa kurang satu pun! Kamu mau kopi susu atau hitam?"
            yutaka "Aku nggak minta traktiran, Kohinata."
            moeka "Aku yang nggak enak kalau lihat cangkir dingin itu terus! Sebentar banget, ya!"
            nar "Ia sudah setengah bangkit dari kursinya sambil tertawa sedikit terlalu keras untuk ruang kantin yang lengang. Alih-alih tenang setelah dimaafkan, teguranmu barusan tampak membuatnya merasa berutang untuk menjadi dua kali lebih ramai dan menyenangkan di depanmu."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kamu memperhatikan ujung jarinya yang masih sedikit gemetar memegang ponsel, peniti kecil yang menahan keliman kardigannya, serta napasnya yang belum sepenuhnya teratur. Alih-alih memperpanjang urusan waktu yang terbuang, kamu menghela napas pelan dan menggeser kotak tisu meja ke arahnya."
            chiasa "Terlambat hampir satu jam tanpa kabar memang bikin repot, Moemoe-senpai. Tapi kelihatan jelas hari ini Senpai lagi kewalahan sekali, ujung rambutmu saja masih basah begitu. Jadi jangan panik dulu, duduk dan tarik napas saja."
            nar "Moeka mengerjap pelan. Ketegangan di wajahnya yang tadi sudah bersiap menerima omelan perlahan mengendur saat ia meraih selembar tisu."
            moeka "Eh... Chimian beneran nggak marah?"
            chiasa "Kesal sedikit sih iya, soalnya tehku sudah telanjur dingin. Tapi kalau aku ikut-ikutan marah sekarang, Senpai kelihatannya malah makin pusing. Lain kali kalau mendadak ketahan rapat atau urusan rumah, cukup kirim satu kata saja biar aku tahu harus menunggu atau geser jam. Itu saja kok."
            nar "Moeka terdiam sejenak sambil menyeka ujung rambut merah mudanya yang lembap dengan tisu. Ketika ia menatapmu kembali, senyum riang yang biasa ia pasang di depan orang banyak sudah berganti menjadi raut lega yang jauh lebih tenang."
            moeka "...Terima kasih banyak ya, Chimian. Serius. Rasanya dari tadi pagi baru kali ini ada orang yang nggak langsung menuntut sesuatu begitu lihat mukaku."
            nar "Ia menarik kursi, duduk penuh, lalu menyandarkan punggungnya ke sandaran kayu sambil mengembuskan napas panjang."
            moeka "Dari jam delapan pagi tadi semua orang di kampus nanyain berkas dekorasi sudah beres belum, contoh kain panggung jadi dibeli atau nggak, terus barusan orang rumah juga telepon soal urusan Ayah... kepalaku rasanya baru berhenti berputar waktu kamu suruh duduk barusan."
            chiasa "Semua bagian itu Senpai pegang sendirian?"
            moeka "Nggak sendirian semua sih, tapi kalau aku nggak ikut ngecek langsung, takutnya nanti ada yang kelewat atau salah ukuran. Ujung-ujungnya semua pesan masuk ke ponselku duluan."
            chiasa "Sudah sempat makan siang belum dari pagi tadi, Senpai?"
            moeka "Tadi sempat makan roti kecil di koridor sebelum masuk ruang rapat, masih aman kok. Kalau begitu... boleh nggak, Chimian, aku minta waktu lima menit saja buat duduk diam dan minum air putih sebelum kita mulai bahas catatan? Lima menit saja, janji."
            chiasa "Iya, silakan saja, Moemoe-senpai. Aku juga masih santai kok, hujannya di luar juga belum reda."
            moeka "Hehe... kamu baik sekali sih, Chimian. Sebentar ya, aku minum dulu."
            nar "Moeka mengeluarkan botol air minum dari tas kanvasnya dan meneguknya perlahan. Selama beberapa menit berikutnya di tengah suara gerimis yang mengetuk kaca jendela kantin, ia duduk tenang di hadapanmu, membiarkan bahunya benar-benar turun tanpa perlu memaksakan tawa atau obrolan berisik."
            moeka "Aneh juga ya... biasanya kalau suasana hening begini, aku langsung refleks nyari bahan obrolan biar nggak canggung. Tapi duduk diam sama kamu barusan rasanya malah enak."
            chiasa "Kadang memang lebih butuh diam sebentar daripada terus bicara, Senpai."
            moeka "Iya... sekarang kepalaku sudah jauh lebih ringan. Ayo kita mulai bahas catatan yang kemarin, Chimian, maaf ya tadi sempat ketunda lama."
            nar "Rona hangat kembali perlahan ke pipinya. Dengan senyum yang jauh lebih tenang dan tidak tergesa, ia membuka buku catatannya di atas meja."
        else:
            nar "Kamu melirik peniti kecil yang menahan keliman kardigannya, tali kartu panitia yang masih miring di kerahnya, dan jari-jarinya yang menggenggam ponsel terlalu erat. Alih-alih menyindir, kamu menghela napas pelan lalu mendorong kursi di seberangmu sedikit dengan kaki agar ia bisa langsung duduk."
            yutaka "Duduk dulu, Kohinata. Terlambat sejam tanpa kabar memang merepotkan, tapi mukamu sekarang sudah kayak orang habis lari keliling lapangan kampus. Tarik napas dulu saja."
            nar "Moeka mengerjap kaget, jelas tidak menyangka kamu akan merespons dengan nada setenang itu. Ia menarik kursi dan duduk perlahan sambil menurunkan tas kanvas beratnya ke lantai."
            moeka "Eh... Yutayuta nggak marah? Nggak mau nyindir aku dulu kayak biasanya?"
            yutaka "Kesal sedikit sih iya, kopiku sudah dingin dari tadi. Tapi kalau sekarang aku ikut ngoceh, kepalamu kelihatannya malah makin pusing. Lain kali kalau ketahan rapat, tinggal ketik 'telat' atau 'geser jam' biar jelas. Nggak perlu sampai lari panik menerobos hujan begini."
            nar "Senyum gugup yang tadinya sudah siap ia pasang di bibir perlahan surut. Ia menyandarkan punggungnya penuh ke kursi kayu dan memejamkan mata sejenak sambil mengembuskan napas panjang."
            moeka "...Terima kasih ya, Yutayuta. Sungguh. Sejak pagi tadi rasanya baru sekarang ada orang yang nggak langsung menagih sesuatu dariku."
            yutaka "Memangnya dari pagi kamu ngurusin apa saja sampai kelihatan dikejar-kejar begitu?"
            moeka "Anak-anak panitia dari pagi ngejar daftar belanja kain, tugas studio minggu ini belum selesai kujahit, terus barusan rumah juga telepon soal urusan Ayah... kepalaku rasanya baru berhenti berdengung waktu duduk di sini."
            yutaka "Kerjaan panitia itu memangnya nggak ada orang lain yang bisa bagi tugas?"
            moeka "Ada sih, tapi kalau aku nggak ikut turun langsung ngecek, rasanya waswas takut ada yang salah ukuran atau telat datang. Akhirnya semua orang terbiasa lempar urusan ke aku duluan."
            yutaka "Sudah sempat makan siang belum?"
            moeka "Tadi sempat ganjal roti sebentar di luar ruang rapat. Boleh ya aku minta lima menit saja buat duduk diam dan minum air sebelum kita mulai? Lima menit saja, janji."
            yutaka "Ambil saja waktumu, hujannya juga masih turun. Aku belum mau ke mana-mana."
            nar "Ia mengangguk pelan, mengeluarkan botol air minum dari dalam tasnya, lalu meneguknya tanpa terburu-buru. Di tengah suara hujan tipis yang membasahi jendela kantin, Moeka akhirnya bisa duduk tenang tanpa merasa harus menghibur siapa pun."
            moeka "Aneh banget ya... biasanya kalau meja hening begini, aku langsung panik nyari topik biar orang nggak bosan. Tapi barusan duduk diam di depanmu malah bikin tenang."
            yutaka "Nggak semua waktu kosong harus diisi obrolan. Kalau napasmu sudah enak, baru kita mulai."
            moeka "Hehe, iya... sekarang sudah jauh lebih segar. Ayo kita bahas urusan kemarin, Yutayuta. Makasih ya sudah mau nunggu."
            nar "Dengan bahu yang kembali rileks, ia meraih buku catatannya dan mulai membuka halaman yang sudah ditandai sejak kemarin."
    else:
        if kk_host == "chiasa":
            nar "Kamu menggeser gelas teh dinginmu ke tepi meja, lalu mengetuk pelan permukaan kayu di depanmu sambil menunjuk ponsel yang masih digenggam Moeka."
            chiasa "Duduk dulu, Moemoe-senpai. Kalau jadwalnya sampai bertumpuk dan bikin lupa janji begini terus, nanti Senpai sendiri yang paling kewalahan. Coba buka kalender di ponsel Senpai sekarang, biar kubantu merapikannya."
            nar "Moeka tertegun menatapmu selama beberapa detik. Matanya yang biru cerah mengerjap pelan, seolah tidak menyangka akan ditawari bantuan praktis alih-alih dimarahi."
            moeka "Eh... Chimian beneran mau bantu beresin jadwal ponselku? Memangnya nggak merepotkan kamu?"
            chiasa "Justru lebih merepotkan kalau minggu depan jadwal Senpai tabrakan lagi terus kita sama-sama buang waktu. Sini, duduk di sebelahku biar gampang lihat layarnya."
            moeka "...Astaga, aku sampai lupa kapan terakhir kali ada yang nawarin bantu ngurusin hal begini duluan."
            nar "Ia mengangkat tasnya, pindah duduk ke kursi di sampingmu, lalu membuka kunci layar ponselnya dan meletakkannya di atas meja di antara kalian berdua."
            nar "Begitu aplikasi kalendernya terbuka, sumber kekacauan hariannya langsung terlihat jelas. Blok-blok catatan memenuhi setiap kotak tanggal tanpa jeda, mulai dari dua rapat kepanitiaan yang tertulis di jam yang sama pada hari Rabu depan, jadwal kerja paruh waktu sore yang menempel persis lima menit setelah kelas berakhir, sampai catatan tugas jahit studio tanpa tenggat hari yang jelas."
            chiasa "Lihat yang hari Rabu jam empat sore ini, Senpai. Rapat seksi dekorasi sama rapat anggaran kok ditaruh di jam yang persis sama? Senpai memang wajib datang ke dua-duanya?"
            moeka "Aduh, aku lupa kalau rapat anggaran kemarin digeser ke hari Rabu! Pantas saja waktu dilihat sekilas aku merasa hari Rabu penuh banget... Hmm, sebenarnya yang rapat dekorasi kan sudah ada Rina yang pegang daftar barangnya. Catatan ukuranku bisa kutitipkan ke Rina hari Selasa malam, jadi Rabu aku cukup hadir di rapat anggaran saja."
            chiasa "Kalau begitu yang dekorasi kuganti jadi pengingat titip catatan ke Rina hari Selasa jam tujuh malam, ya. Terus ini tugas studio yang cuma ditulis 'minggu ini', batas pengumpulan aslinya hari apa?"
            moeka "Hari Jumat jam tiga sore. Tapi kalau ditulis Jumat, aku suka baru ngebut Kamis tengah malam sambil minum kopi instan. Tulis Kamis sore saja deh di kalender biar aku nggak kelabakan di hari terakhir."
            chiasa "Oke, sudah kugeser ke Kamis sore. Sama lihat hari Selasa dan Kamis siang ini, kelas Senpai selesai jam dua belas lebih lima belas, terus jam setengah satu sudah masuk kerja paruh waktu?"
            moeka "Eh, iya, biasanya aku lari ke tempat kerja sambil beli roti di minimarket depan gerbang."
            chiasa "Mulai minggu ini, jeda antara kelas siang sama rapat atau kerja paruh waktu aku kasih blok khusus buat makan dan jalan, jangan diisi janji dadakan lagi."
            moeka "Haha, sampai jam makanku juga kamu kunci di kalender, Chimian?"
            chiasa "Biar nggak tumbang. Setiap rapat sama janji ketemu orang juga kupasangin alarm pengingat tiga puluh menit sebelumnya, supaya Senpai sempat kirim pesan kalau jadwal sebelumnya molor."
            nar "Selama lima belas menit berikutnya, kalian berdua menyisir jadwal dua minggu ke depan satu per satu. Kamu membantu mengetikkan jam dan merapikan urutan prioritasnya, tetapi selalu membiarkan Moeka yang memutuskan agenda mana yang harus ia geser atau lepaskan."
            nar "Ketika layar kalender itu akhirnya tampak bersih dan masuk akal untuk dijalani, Moeka menopang dagunya dengan kedua tangan sambil mengembuskan napas lega."
            moeka "Wah... baru kali ini layar kalenderku kelihatan punya sela buat bernapas. Makasih banyak ya, Chimian. Kalau nanti aku mulai salah atur jadwal lagi, tolong ingatkan ya, tapi jangan sampai kamu yang ikut repot ngurusin ponselku terus."
            chiasa "Tenang saja, Senpai. Aku cuma bakal mengingatkan kalau Senpai sudah kelihatan mulai numpuk-numpuk kerjaan lagi."
            moeka "Siap! Kalau begitu sekarang giliran aku fokus penuh sama catatan kita hari ini, ayo!"
            nar "Moeka tertawa kecil yang terdengar jauh lebih ringan daripada saat ia baru berlari masuk kantin tadi, lalu menyimpan ponselnya dengan tenang untuk memulai pembicaraan kalian."
        else:
            nar "Kamu menggeser cangkir kopi dinginmu ke pinggir meja, lalu mencondongkan badan sedikit sambil menunjuk ponsel yang masih berada di genggaman Moeka."
            yutaka "Duduk dulu, Kohinata. Kalau jadwalmu sampai tabrakan dan bikin lupa janji kayak hari ini terus, belum sampai ujian tengah semester kamu sudah tumbang duluan. Sini buka aplikasi kalender di ponselmu, kita bereskan sekarang."
            nar "Moeka mengerjap tertegun. Selama beberapa detik ia hanya menatapmu, seolah belum terbiasa ditawari bantuan langsung tanpa harus meminta."
            moeka "Serius, Yutayuta mau bantu ngatur jadwalku? Nggak ngerepotin kamu memangnya?"
            yutaka "Lebih ngerepotin kalau lain kali aku harus duduk bengong sejam lagi gara-gara jadwalmu tumpang tindih. Geser kursimu ke sini biar kelihatan layarnya."
            moeka "...Ya ampun, rasanya sudah lama sekali aku nggak ditolong duluan kayak begini."
            nar "Ia memindahkan kursinya agak merapat ke sisi mejamu, membuka kunci layar ponselnya, lalu meletakkannya di tengah agar kalian berdua bisa memeriksa daftar agendanya bersama."
            nar "Begitu tampilan mingguannya terbuka, kamu langsung melihat kenapa ia selalu tampak dikejar waktu. Hampir setiap hari dipenuhi catatan rapat panitia, jadwal kuliah studio, dan jam kerja paruh waktu yang saling berhimpitan tanpa jeda perjalanan, bahkan ada dua agenda berbeda yang tercatat di jam yang sama pada hari Rabu."
            yutaka "Lihat yang hari Rabu jam empat sore ini. Rapat dekorasi sama rapat anggaran ditaruh di jam yang persis sama. Kamu kan nggak bisa belah diri jadi dua, mana yang sebenarnya bisa diwakilkan?"
            moeka "Aduh, aku lupa total kalau rapat anggaran kemarin dimajuin ke Rabu! Hmm... kalau rapat dekorasi sebenarnya sudah ada Rina di sana. Catatan bahan bagianku bisa kutitipkan ke Rina hari Selasa malam, jadi Rabu aku cukup datang ke rapat anggaran."
            yutaka "Oke, yang rapat dekorasi kubuat jadi pengingat titip catatan ke Rina hari Selasa jam delapan malam. Terus catatan 'tugas studio minggu ini' yang nggak ada jamnya ini, batas kumpul aslinya kapan?"
            moeka "Jumat sore jam empat. Tapi tolong tulis Kamis malam saja deh, Yutayuta, biar aku nggak baru panik ngerjain pas Kamis tengah malam."
            yutaka "Beres, kupasang Kamis jam enam sore. Terus lihat hari Selasa sama Kamis ini, kelasmu keluar jam dua belas lewat seperempat, terus kerja paruh waktumu mepet banget habis itu. Kapan kamu makan siang?"
            moeka "Biasanya beli roti di jalan sambil lari ke halte..."
            yutaka "Di sela kelas siang sama rapatmu juga kublok kosong setengah jam buat makan, jangan kamu isi urusan dadakan lagi."
            moeka "Wah, galak juga ya pengatur jadwalnya sampai jam makan dikunci segala."
            yutaka "Biar kamu nggak pingsan di tengah rapat. Semua janji ketemu orang juga kunyalakan pengingatnya setengah jam sebelum mulai, jadi kalau rapat sebelumnya molor, kamu langsung ingat buat kirim pesan."
            nar "Selama lima belas menit berikutnya, kamu membantu merapikan blok-blok jadwal di ponselnya dan memberi jeda realistis antar kegiatan, sambil tetap membiarkan Moeka yang menentukan sendiri mana pekerjaan yang wajib ia pegang dan mana yang bisa ia kurangi."
            nar "Setelah seluruh jadwal dua minggu ke depan tertata rapi, Moeka menyandarkan punggungnya ke kursi sambil menatap layar ponselnya dengan napas lega."
            moeka "Fiuh... baru kali ini jadwalku kelihatan kayak jadwal manusia normal. Terima kasih banyak ya, Yutayuta. Kalau nanti aku mulai teledor lagi, tolong tegur saja, tapi jangan sampai kamu yang malah pusing ngurusin kalenderku."
            yutaka "Tenang saja, aku nggak serajin itu buat ngecek tiap hari. Yang penting lain kali kalau telat, kamu tahu harus ngabarin."
            moeka "Siap, mengerti! Sekarang ayo kita selesaikan urusan kita hari ini sebelum sore."
            nar "Ia tertawa pelan dengan bahu yang jauh lebih rileks daripada saat ia membuka pintu kantin tadi, lalu membuka buku catatannya untuk memulai urusan kalian yang sempat tertunda."
    return

# ┌─ PANDUAN CERITA · Mo04 · Pingsan Karena Lupa Makan
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : di vila.
# │ INTI    : A rawat / B panggil Miyuki / C abaikan.
# │ AKHIRAN : intimasi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo04:
    call kk_scene_enter("moeka", "Dapur vila · Pingsan")
    if kk_host == "chiasa":
        nar "Menjelang waktu makan malam di vila pantai, area dapur dipenuhi bunyi kuah mendidih dari panci besar, aroma kaldu sayur yang hangat, serta suara obrolan dari ruang tengah. Sejak rombongan tiba siang tadi, Moeka menjadi orang yang paling sibuk bergerak ke sana kemari tanpa pernah duduk diam."
        nar "Ia yang mengupas buah untuk camilan sore, mengantarkan nampan minuman dingin ke teras, lalu kembali lagi ke dapur untuk menyiapkan bumbu makan malam sambil terus berceloteh riang."
        chiasa "Moemoe-senpai, dari siang tadi Senpai belum duduk istirahat sekali pun lho. Biar aku saja yang mengaduk panci supnya, Senpai duduk dulu di ruang makan sana."
        moeka "Ih, nggak usah, Chimian! Aku malah senang kalau di dapur ramai-ramai begini. Lagian sup sayurnya tinggal tunggu lobaknya empuk sedikit lagi kok."
        chiasa "Tapi uap kompornya panas banget di sini. Keringat di pelipis Senpai sudah kelihatan."
        moeka "Biarin aja, anggap sekalian olahraga sore! Oh iya, tolong geser mangkuk saus wijennya sedikit ke sini dong! Tadi waktu kalian main di tepi pantai, aku sempat lihat kepiting kecil lari nyempil di bawah payung bawa remah roti, lucu sekali kayak..."
        nar "Kalimatnya mendadak terputus di udara. Sendok sayur kayu di tangan kanannya terlepas dan jatuh membentur pinggiran panci dengan suara nyaring, sementara jemarinya langsung mencengkeram tepi meja dapur erat-erat. Rona cerah di pipinya lenyap dalam sekejap menjadi pucat pasi."
        chiasa "Eh, Moemoe-senpai? Kenapa? Wajah Senpai pucat banget! Pegangan ke aku dulu!"
        moeka "Nggak... nggak apa-apa, Chimian, cuma agak gelap sedikit pemandanganku barusan... pusing sebentar doang kok, aku masih..."
        nar "Belum sempat ia menyelesaikan ucapannya, kedua lututnya kehilangan tumpuan. Tubuhnya langsung merosot jatuh ke lantai kayu dapur. Kamu segera maju menahan kedua bahunya agar kepalanya tidak membentur kaki meja."
        chiasa "Moemoe-senpai! Senpai, dengar suaraku nggak?!"
        nar "Tubuh Moeka terasa lemas dan dingin di pelukan lenganmu, dengan napas pendek yang berat. Saat matamu melirik ke sudut meja persiapan di belakangnya, kamu melihat sepiring nasi kecil dengan lauk telur gulung yang tadi siang disisihkan khusus untuk bagian makan siangnya masih tergeletak utuh di bawah tudung saji. Sejak pagi, ia sibuk memastikan semua orang di vila makan kenyang, sedangkan dirinya sendiri belum menyentuh makanan sama sekali."
    else:
        nar "Menjelang jam makan malam di vila pantai, ruang dapur dipenuhi kepulan uap dari panci kaldu, aroma tumisan bumbu, serta suara tawa rombongan yang bersantai di ruang tengah. Sejak tiba di vila siang tadi, Moeka hampir tidak pernah terlihat duduk diam barang sepuluh menit."
        nar "Ia yang memotong semangka untuk teman-teman di beranda, membereskan gelas-gelas kosong di meja ruang tamu, lalu langsung berdiri lagi di depan kompor untuk mengaduk sup makan malam sambil terus mengajakmu mengobrol."
        yutaka "Kamu dari siang tadi belum berhenti jalan mondar-mandir lho, Kohinata. Sini sendok sayurnya biar aku yang gantian ngaduk, kamu duduk sebentar di depan."
        moeka "Nggak usah, Yutayuta! Aku kuat kok, lagian kuahnya tinggal ditunggu mendidih sekali lagi terus dikasih garam sedikit."
        yutaka "Dapur ini panasnya kayak ruang uap, mukamu saja kelihatan agak lelah."
        moeka "Cuma kena asap panci aja kok! Eh, tolong oper mangkuk sausnya ke sebelah sini dong. Tadi waktu jalan di pinggir pantai aku sempat lihat kepiting kecil lari dikejar ombak sambil nyapit kerupuk, lucu sekali mirip..."
        nar "Suaranya tiba-tiba hilang di tengah kalimat. Tangan kanannya melepaskan sendok sayur hingga berdenting di tepi panci, lalu jari-jarinya mencengkeram pinggiran meja konter dapur sekuat tenaga. Wajahnya yang semenit lalu masih bersemangat mendadak pucat tanpa warna."
        yutaka "Hei, Kohinata? Mukamu pucat sekali, kamu kenapa?!"
        moeka "Nggak... cuma berkunang-kunang sedikit barusan, Yutayuta... pusing biasa kok, sebentar lagi juga..."
        nar "Sebelum kalimatnya selesai, tumpuan kakinya langsung goyah. Kamu refleks melangkah maju dan menangkap kedua lengannya tepat sebelum tubuhnya merosot menghantam lantai kayu dapur, lalu menahannya bersandar perlahan ke bawah."
        yutaka "Kohinata! Hei, buka matamu dulu!"
        nar "Telapak tangannya terasa sangat dingin dan napasnya terdengar dangkal. Ketika kamu menoleh ke sudut meja dapur di belakang tempatnya berdiri tadi, sepiring nasi dan lauk porsi kecil yang disisihkan untuk makan siangnya masih dingin dan belum tersentuh sedikit pun. Dari siang ia sibuk menyuruh semua orang makan, sementara perutnya sendiri dibiarkan kosong seharian."
    call kk_family_menu("Mo04", ["Rawat ia sendiri sampai pulih.", "Panggil Miyuki untuk memeriksanya.", "Abaikan; itu bukan urusanmu."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu segera mematikan api kompor yang paling dekat, lalu merangkul bahu Moeka dan memapahnya perlahan keluar dari dapur menuju sofa di ruang duduk samping yang lebih sejuk dan jauh dari kebisingan ruang tengah."
            chiasa "Pelan-pelan saja jalannya, Moemoe-senpai. Tumpukan berat badan Senpai ke bahuku, jangan dipaksa berdiri sendiri."
            moeka "...Maaf ya, Chimian, badanku kok rasanya berat sekali..."
            nar "Saat Nagisa sempat melongok dari ujung lorong ruang makan dengan wajah kaget, kamu segera memberi isyarat tenang."
            nagisa "Lho, Chiasa, Kohinata-san kenapa?"
            chiasa "Cuma agak kepanasan kena uap kompor di dapur, Nagisa-senpai. Biar kubaringkan dulu di ruang samping supaya kena angin, yang lain lanjutkan makan malam dulu aja biar ruangan ini nggak pengap."
            nar "Nagisa mengangguk paham lalu kembali mengawasi kompor di dapur. Setelah membaringkan Moeka dengan bantal menyangga kepala dan menyelimuti kakinya, kamu kembali sebentar ke dapur untuk menyendok semangkuk bubur nasi hangat serta membuat segelas teh manis hangat, lalu menaruhnya di meja kecil samping sofa."
            nar "Beberapa menit kemudian, kelopak mata Moeka bergerak pelan dan terbuka. Begitu melihatmu duduk berlutut di sisi sofa sambil memegang gelas hangat untuknya, ia langsung berusaha bangkit dengan wajah panik."
            moeka "Eh... Chimian? Aku kok di sofa? Aduh, maaf, aku tadi jatuh di dapur ya? Kamu yang jagain aku dari tadi?"
            chiasa "Jangan langsung duduk tegak dulu, Moemoe-senpai, nanti pusingnya balik lagi. Minum teh manis hangat ini dulu pelan-pelan."
            nar "Kamu membantu menyangga punggungnya sedikit agar ia bisa menyesap teh hangat itu dari tepi gelas. Moeka memegangi gelasnya dengan kedua tangan yang masih agak gemetar, lalu tertawa kecil yang terdengar serak."
            moeka "Malu sekali... baru juga dibilangin buat duduk, eh semenit kemudian langsung tumbang di depan panci."
            chiasa "Piring makan siang Senpai di pojok dapur tadi masih utuh sama sekali. Sebenarnya Senpai dari pagi belum makan apa-apa ya waktu berangkat ke vila?"
            moeka "Hehe... ketahuan ya, Chimian. Aku pikir tadi kalau cuma minum air putih sama mencicipi kuah sedikit sudah cukup kuat sampai malam."
            chiasa "Kenapa sampai nggak makan seharian begitu, Senpai? Di vila ini kan makanannya banyak sekali."
            moeka "Bukan gara-gara makanan di sini kok... cuma dua minggu terakhir ini aku memang lagi membiasakan porsi makan sehari sekali di kampus supaya sisa uang makanku bisa kukirim ke rumah akhir bulan ini. Jadi perutku kayaknya kaget, terus tadi di dapur udaranya panas sekali."
            chiasa "Ya ampun, Moemoe-senpai... menghemat uang pun jangan sampai mengorbankan badan sendiri sampai pingsan di depan kompor begitu. Kalau tadi kepalamu kena sudut meja gimana?"
            moeka "Iya, maaf, aku ceroboh sekali nggak mengukur tenaga sendiri... tapi Chimian, aku mohon sekali sama kamu. Tolong jangan cerita ke anak-anak yang lain soal alasan kenapa aku kurangi makan akhir-akhir ini, ya? Apalagi soal uang buat rumah. Tolong rahasiakan di antara kita berdua saja."
            chiasa "Tenang saja, Senpai, aku nggak bakal cerita ke siapa-siapa di luar ruangan ini. Tapi syaratnya sekarang Senpai harus habiskan bubur hangat di mangkuk ini sampai bersih."
            moeka "Semangkuk penuh ini? Nanti kalau kekenyangan..."
            chiasa "Nggak ada tawar-menawar, Senpai. Sendoknya kupegangkan atau mau suap sendiri?"
            moeka "Eh, aku suap sendiri aja! Iya, iya, kumakan sekarang kok."
            nar "Moeka menerima mangkuk bubur yang mengepul lembut di tanganmu, lalu menyuapinya perlahan-lahan. Setelah lebih dari setengah mangkuk tandas dan rona merah muda mulai kembali ke pipi serta bibirnya, ia meletakkan sendok di pinggir mangkuk. Kebiasaan lamanya langsung muncul lagi. Tangannya refleks menyingkap ujung selimut tipis di pangkuannya dan bersiap menurunkan kaki ke lantai."
            moeka "Nah, badanku sudah hangat lagi kok! Aku balik ke dapur sekarang ya, kasihan yang lain kalau harus mencuci panci sebanyak itu..."
            chiasa "Diam di sofa, Moemoe-senpai. Jangan berdiri."
            nar "Kamu menahan pelan bahunya hingga ia kembali terduduk bersandar di bantal sofa."
            chiasa "Malam ini gantian Senpai yang diurus dan dijaga di sini. Sekali-sekali biarkan orang lain yang membereskan dapur."
            nar "Gerakan Moeka terhenti. Ia menatap wajahmu beberapa detik dalam keheningan ruang samping, lalu akhirnya melepaskan pinggiran selimut dan menyandarkan kepalanya kembali ke bantal sofa dengan napas panjang."
            moeka "...Aku tuh paling takut kalau orang-orang tahu kondisiku, nanti mereka mikir aku bahkan nggak becus mengurus diriku sendiri. Tapi di depan kamu... kayaknya buat malam ini aku memang harus mengaku kalah dan istirahat, ya."
            chiasa "Iya, istirahat saja sampai makan malam di depan selesai. Aku temani di sini sampai Senpai benar-benar pulih."
            moeka "...Makasih banyak ya, Chimian. Teh manisnya pas banget rasanya."
        else:
            nar "Kamu segera mengecilkan api kompor di dekatnya, lalu merangkul pundak Moeka dan memapahnya perlahan menuju ruang duduk samping yang lebih sejuk dan tenang."
            yutaka "Pelan-pelan, jangan buru-buru melangkah. Tumpu saja di bahuku sampai sofa sebelah."
            moeka "...Maaf ya, Yutayuta, kakiku kok jadi lemas banget begini..."
            nar "Saat Koita sempat melongok dari ujung lorong ruang makan dengan wajah kaget, kamu segera memberi penjelasan singkat agar tidak terjadi kerumunan."
            koita "Lho, Yutaka, Moeka-chan kenapa? Perlu kupanggil yang lain?"
            yutaka "Cuma pusing kena uap panas di dapur. Aku baringkan dulu di ruang samping biar kena angin, tolong kamu bantu awasi kompornya dulu di belakang biar ruangan ini tetap sejuk."
            nar "Koita mengangguk cepat lalu berbalik ke dapur. Setelah membaringkan Moeka di sofa panjang dan menyelimuti kakinya, kamu kembali ke dapur sebentar untuk mengambil segelas teh manis hangat serta semangkuk bubur nasi hangat."
            nar "Tak lama setelah kamu duduk di kursi sebelah sofa, kelopak mata Moeka mengerjap pelan. Begitu menyadari dirinya terbaring dengan selimut dan melihatmu memegang gelas hangat di sampingnya, ia langsung terkesiap hendak bangun."
            moeka "Yutayuta...? Loh, aku kok pindah ke sini? Aduh, maaf sekali, tadi aku bikin heboh satu dapur ya?"
            yutaka "Tahan dulu kepalamu di bantal, jangan langsung bangun. Minum teh manis ini dulu pelan-pelan biar gula darahmu naik."
            nar "Kamu membantunya duduk setengah bersandar dan menyodorkan gelas hangat itu ke tangannya. Moeka menerima gelas tersebut dengan kedua telapak tangan, menyesapnya beberapa teguk, lalu mengeluarkan tawa pendek yang terdengar lemah."
            moeka "Malu-maluin sekali... baru saja kubilang kuat, langsung roboh di depan panci."
            yutaka "Piring jatah makan siangmu di pojok meja dapur tadi masih utuh belum disentuh. Kamu dari pagi waktu berangkat belum kemasukan nasi sama sekali, kan?"
            moeka "Hehe... matamu jeli sekali sih, Yutayuta. Tadi kupikir kalau cuma ganjal air minum sebentar masih kuat sampai jam makan malam."
            yutaka "Makanan di vila sebanyak itu, kenapa malah kamu lewati dari siang?"
            moeka "Bukan karena nggak mau makan masakan di sini... cuma dua minggu belakangan aku memang lagi membiasakan hemat uang makan di kampus biar kiriman ke rumah bulan ini nggak kurang. Jadinya perutku sudah keburu kaget dan nggak biasa makan siang, terus tadi kena uap panas kompor langsung gelap semua."
            yutaka "Hemat ya hemat, Kohinata, tapi kalau sampai tumbang di depan kompor panas begitu namanya nekat. Kalau tadi aku nggak berdiri tepat di belakangmu, kepalamu sudah terbentur lantai kayu."
            moeka "Iya, salahku, maaf sudah bikin kamu panik... tapi Yutayuta, tolong sekali ya. Jangan bilang ke siapa-siapa di vila ini kenapa aku sampai nggak makan dari pagi. Soal kiriman rumah itu... cukup kamu saja yang tahu, ya?"
            yutaka "Mulutku terkunci, tenang saja. Tapi gantinya, bubur hangat di mangkuk ini harus kamu habiskan sekarang di depanku."
            moeka "Sebanyak ini? Kalau cuma setengah mangkuk dulu boleh?"
            yutaka "Jangan ditawar. Makan pelan-pelan, aku nggak bakal pergi sebelum mangkuknya hampir kosong."
            moeka "...Iya deh, iya, kumakan sekarang."
            nar "Moeka menatap mangkuk bubur yang kamu sodorkan, lalu mengangguk kecil. Ia mulai menyuap bubur hangat itu perlahan-lahan di bawah pengawasanmu. Setelah lebih dari separuh mangkuk habis dan warna pucat di wajahnya mulai berganti hangat, tangannya sudah otomatis bergerak menyingkap selimut hendak turun dari sofa."
            moeka "Oke, tenagaku sudah balik kok! Aku ke dapur sekarang ya, nggak enak kalau cucian piring sama panci ditinggal ke anak-anak yang lain..."
            yutaka "Duduk diam di situ, Kohinata. Jangan coba-coba berdiri."
            nar "Kamu menahan tepi sandaran sofa di dekat bahunya, membuatnya urung menurunkan kaki ke lantai."
            yutaka "Malam ini gantian kamu yang dijaga. Biarkan saja urusan dapur dipegang yang lain."
            nar "Moeka terdiam menatapmu selama beberapa detik, lalu akhirnya menurunkan kembali tangannya dan menyandarkan kepala ke bantal sofa dengan helaan napas panjang."
            moeka "...Selama ini aku paling takut kalau kelihatan lemah begini, orang-orang bakal mikir aku nggak becus mengurus diri sendiri. Tapi buat malam ini... kayaknya aku memang harus nurut kata kamu dulu, ya."
            yutaka "Nah, begitu. Habiskan sisa tehmu terus pejamkan mata sebentar, aku tungguin di kursi sini."
            moeka "...Makasih ya, Yutayuta."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Menyadari tubuh Moeka sangat dingin dan lemas, kamu menahan bahunya agar tetap bersandar aman di lantai dapur, lalu segera berseru memanggil Tachibana Miyuki yang sedang berada di ruang tengah."
            chiasa "Tachibana-senpai! Tolong ke dapur sebentar, Moemoe-senpai tiba-tiba pusing terus jatuh lemas!"
            nar "Kurang dari sepuluh detik, Miyuki sudah melangkah cepat masuk ke dapur tanpa kehilangan ketenangannya. Ia langsung berlutut di sisi Moeka dan memberi isyarat kepada yang lain agar tidak berkerumun di ambang pintu dapur."
            miyuki "Semuanya tolong tetap di ruang tengah dulu ya supaya udaranya nggak pengap. Chiasa-chan, tolong bukakan jendela samping sedikit supaya angin masuk, lalu ambilkan segelas air hangat dengan dua sendok gula. Moeka-chan, bisa dengar suara Senpai?"
            chiasa "Baik, Senpai! Jendelanya sudah kubuka, ini air gulanya!"
            nar "Miyuki memeriksa denyut pergelangan tangan Moeka sambil melihat jam tangannya, lalu menempelkan punggung tangan ke dahi serta pipi gadis itu. Ketika kelopak mata Moeka mulai mengerjap terbuka, kamu membantu Miyuki memapahnya pindah ke sofa ruang samping yang lebih tenang."
            moeka "Ehm... Miyumiyu-senpai? Chimian? Maaf banget, aku bikin repot semua orang ya..."
            miyuki "Jangan dipikirkan dulu soal repot, Moeka-chan. Denyut nadimu agak lemah dan ujung jari-jarimu dingin sekali. Ada rasa mual atau nyeri dada nggak?"
            moeka "Nggak ada kok, Senpai, cuma kepalaku masih agak ringan sedikit."
            miyuki "Bagus kalau nggak mual. Sekarang jawab jujur sama Senpai, hari ini kamu terakhir kali makan jam berapa?"
            moeka "Ehm... tadi pagi cuma sempat minum teh hangat di kamar, Miyumiyu-senpai. Aku cuma lagi hemat sedikit biar uang buat rumah bulan ini cukup... nggak parah kok, sungguh, nggak usah dibawa ke klinik atau rumah sakit segala ya, nanti malah keluar biaya lagi."
            chiasa "Piring makan siangnya di pojok meja dapur juga masih utuh, Senpai. Dari berangkat tadi Moemoe-senpai belum makan nasi sama sekali."
            miyuki "Minum air gula hangat dari Chiasa-chan ini dulu pelan-pelan sampai habis. Senpai nggak akan langsung bawa ke klinik kalau kondisimu membaik. Tapi kalau dalam lima belas menit pandanganmu masih berkunang-kunang dan keringat dinginnya belum berhenti, kita tetap harus periksa ke dokter jaga dekat sini. Soal kesehatan nggak boleh ditawar pakai alasan hemat, mengerti?"
            nar "Moeka yang tadinya sudah bersiap melempar candaan untuk mencairkan suasana langsung terdiam melihat tatapan lembut Miyuki yang sama sekali tidak bisa dibantah."
            moeka "...Iya, Miyumiyu-senpai. Maaf ya sudah bikin kalian berdua cemas. Tadi aku mau bercanda soalnya malu sekali ketahuan jatuh gara-gara belum makan. Aslinya aku lega sekali kalian langsung datang menolongku."
            chiasa "Jangan ditahan-tahan lagi kalau lapar, Moemoe-senpai. Sebentar ya, aku ambilkan bubur hangat dari dapur sama bantal tambahan supaya Senpai bisa langsung istirahat di sini."
            miyuki "Benar kata Chiasa-chan. Malam ini Moeka-chan bebas tugas dari urusan dapur, fokus habiskan buburnya lalu tidur lebih awal ya. Lima belas menit lagi Senpai cek nadimu sekali lagi."
            moeka "Hehe... iya, siap, Dokter. Terima kasih banyak ya, Chimian, Miyumiyu-senpai."
        else:
            nar "Melihat wajah Moeka yang pucat pasi dengan keringat dingin di pelipisnya, kamu menahan punggungnya agar tetap aman bersandar, lalu segera berseru memanggil Tachibana Miyuki di ruang tengah."
            yutaka "Tachibana-senpai! Tolong ke dapur sekarang, Kohinata barusan pusing terus roboh!"
            nar "Miyuki segera bergegas masuk ke dapur dengan langkah tenang dan cekatan. Ia langsung berlutut di samping Moeka dan meminta mahasiswa lain yang sempat melongok di pintu untuk tetap di ruang tengah agar sirkulasi udara tidak pengap."
            miyuki "Yang lain tolong beri ruang udara dulu ya. Yutaka-kun, tolong bukakan jendela samping dan ambilkan air hangat yang dicampur gula agak banyak, lalu bantu Senpai pindahkan Moeka-chan ke sofa ruang sebelah kalau dia sudah mulai merespons. Moeka-chan, dengar suara Senpai?"
            yutaka "Siap, Senpai. Ini air gulanya sudah kubuatkan."
            nar "Miyuki memeriksa nadi di pergelangan tangan Moeka serta suhu tubuhnya dengan teliti. Begitu Moeka mulai membuka mata dan mengerang pelan, kamu membantunya memapah Moeka menuju sofa panjang di ruang duduk samping."
            moeka "Aduh... Miyumiyu-senpai, Yutayuta? Maaf ya, aku malah bikin heboh..."
            miyuki "Nggak usah minta maaf dulu, atur napasmu pelan-pelan. Tanganmu dingin sekali dan tekanan darahmu kelihatannya turun karena perut kosong, Moeka-chan. Ada rasa mual atau sesak nggak?"
            moeka "Nggak mual kok, Senpai, cuma tadi pandanganku sempat gelap semua."
            miyuki "Syukurlah kalau begitu. Sekarang jujur sama Senpai, kamu terakhir makan nasi kapan?"
            moeka "Hehe... tadi malam, Miyumiyu-senpai. Siang tadi aku sengaja lewat makan biar hemat uang saku buat kiriman rumah... tapi aku sudah nggak apa-apa kok, sungguh nggak perlu dibawa ke klinik malam-malam begini, sayang biayanya."
            yutaka "Piring makan siang jatahnya di pojok dapur tadi bahkan belum dibuka tudungnya, Senpai."
            miyuki "Minum air gula hangat yang dibuatkan Yutaka-kun ini dulu sedikit demi sedikit. Senpai masih mahasiswa kedokteran, jadi Senpai nggak boleh ambil risiko menebak-nebak. Kalau sepuluh menit setelah minum ini dan makan bubur kepalamu masih pusing saat duduk, kita tetap pergi ke klinik terdekat malam ini juga."
            nar "Moeka sempat hendak membalas dengan tawa ringannya, tetapi melihat raut serius di wajah Miyuki dan tatapanmu yang ikut mengawasi di sisi sofa, ia akhirnya mengangguk patuh."
            moeka "...Maaf ya, Yutayuta, Miyumiyu-senpai. Aku tadi ngeles sambil bercanda soalnya malu sekali pingsan gara-gara lapar. Sebenarnya aku senang kok kalian berdua langsung sigap mengurus aku."
            yutaka "Makanya jangan aneh-aneh nahan lapar seharian. Tunggu di sini, aku ambilkan semangkuk bubur hangat dari dapur sama selimut tambahan buatmu."
            miyuki "Iya, malam ini urusan makan malam dan cuci piring biar yang lain saja yang pegang. Moeka-chan cukup makan bubur lalu istirahat penuh, sebentar lagi Senpai periksa lagi kondisimu."
            moeka "Iya... terima kasih banyak ya, Yutayuta, Miyumiyu-senpai."
    else:
        if kk_host == "chiasa":
            nar "Kamu mundur setengah langkah dari meja dapur setelah bunyi jatuhnya Moeka mengundang perhatian beberapa anggota rombongan dari ruang tengah. Koita dan Nagisa segera berlari masuk ke dapur, memapah Moeka duduk ke kursi ruang makan, lalu memberinya air minum."
            koita "Moeka-chan, pelan-pelan saja duduknya. Ini minum dulu, mukamu pucat sekali."
            nagisa "Makanya jangan berdiri terus di depan kompor panas dari tadi!"
            nar "Kamu memilih tidak ikut mengerubungi kursinya dan tetap berdiri di dekat meja dapur melanjutkan merapikan peralatan masak. Tak lama kemudian, Moeka mulai membuka mata. Begitu menyadari beberapa teman sedang menatapnya dengan cemas, ia langsung menegakkan punggung dan menangkupkan kedua tangan di depan wajah."
            moeka "Aduh, maaf semuanya! Aku bikin kaget ya? Beneran nggak apa-apa kok, tadi siang cuma agak kepanasan waktu jalan di pantai terus lupa minum air putih!"
            nar "Ia merapikan poni rambut merah mudanya dengan jemari yang masih tampak sedikit gemetar, lalu langsung memasang kembali senyum cerahnya seolah tidak terjadi apa-apa. Beberapa menit kemudian ia bahkan bersikeras tetap duduk di meja makan bersama rombongan."
            nar "Sepanjang sisa malam itu di vila, setiap kali kamu berpapasan dengannya di lorong atau di dekat meja makan, Moeka selalu menoleh lebih dulu dan berbicara cepat sebelum kamu sempat membuka mulut."
            moeka "Eh, Chimian! Tadi aku sudah makan nasi dua mangkuk penuh kok di meja depan, sumpah! Lauk sup sayurnya enak banget, kan?"
            chiasa "Oh... iya, Moemoe-senpai. Syukurlah kalau sudah makan."
            moeka "Sekarang tenagaku sudah pulih seratus persen, jadi kamu sama sekali nggak perlu khawatir atau nanya-nanya lagi ya! Tadi tuh murni cuma efek angin pantai aja kok!"
            chiasa "Baik, Senpai. Jangan dipaksakan lagi ya malam ini."
            moeka "Tenang aja! Aku mau bantu angkat piring kotor ke dapur dulu ya, dah!"
            nar "Ia tersenyum lebar lalu cepat-cepat melangkah melewatimu menuju dapur, menutup rapat celah percakapan apa pun tentang kejadian tadi."
        else:
            nar "Begitu suara gaduh di dapur membuat beberapa orang dari ruang tengah berlari masuk untuk menolong, kamu melepaskan peganganmu di lengan Moeka dan memilih mundur ke samping agar mereka yang mengurusnya."
            koita "Moeka-chan, pegangan ke sini pelan-pelan. Kita duduk dulu di kursi makan, biar kuambilkan air hangat."
            nagisa "Kamu sih dari siang nggak pernah mau duduk, makanya langsung lemas begini!"
            nar "Mereka memapah Moeka duduk di kursi ruang makan dan memberinya air hangat. Beberapa menit kemudian, saat kesadarannya pulih dan ia melihat banyak mata menatapnya khawatir, Moeka langsung duduk tegak sambil melambaikan kedua tangan di depan dada."
            moeka "Aduh, maaf semuanya sudah bikin panik! Aku beneran nggak apa-apa kok, tadi cuma agak kepanasan waktu lari-lari di pantai siang tadi!"
            nar "Ia menyibakkan poni rambut merah mudanya dengan jari yang masih sedikit gemetar, lalu segera memaksakan tawa riang seperti biasa untuk membubarkan kerumunan."
            nar "Sepanjang sisa malam di vila, setiap kali kamu kebetulan berpapasan dengannya di koridor atau ruang tengah, Moeka selalu menyapamu lebih dulu dengan nada suara yang sengaja dibuat lantang."
            moeka "Eh, Yutayuta! Tadi aku sudah habis makan malam porsi besar kok bareng anak-anak di depan, sumpah! Sup sayurnya tadi mantap banget, kan?"
            yutaka "Oh... baguslah kalau kamu sudah makan."
            moeka "Sekarang sudah sehat total, jadi kamu nggak usah mikirin kejadian di dapur tadi ya! Murni cuma kecapekan main di pantai aja kok!"
            yutaka "Ya sudah, jangan sampai tumbang lagi."
            moeka "Sip! Aku mau ke belakang bantu beresin gelas dulu ya!"
            nar "Ia melemparkan senyum lebar lalu bergegas berjalan melewatimu, memastikan tidak ada ruang sedikit pun bagimu untuk menanyakan alasan mengapa ia tumbang tadi."
    return

# ┌─ PANDUAN CERITA · Mo05 · Kabar dari Rumah
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ibu menelepon.
# │ INTI    : A dengarkan / B alihkan / C tanya langsung.
# │ AKHIRAN : membuka masalah keluarga.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo05:
    call kk_scene_enter("moeka", "Kantin Pusat · Kabar dari rumah")
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Kantin Pusat malam itu sudah jauh lebih lengang di bawah lampu langit-langit yang terang. Di meja pojok dekat jendela gelap, Moeka membentangkan beberapa lembar kain perca berwarna cerah di samping buku sketsa desainnya, lengkap dengan deretan kancing contoh dan gunting benang kecil yang tertata di atas saputangan."
        else:
            nar "Kantin Pusat saat itu sudah melewati jam sibuk. Di meja pojok dekat jendela terang, Moeka membentangkan beberapa lembar kain perca berwarna cerah di samping buku sketsa desainnya, lengkap dengan deretan kancing contoh dan gunting benang kecil yang tertata di atas saputangan."
        moeka "Chimian, kebetulan banget kamu lewat sini! Coba lihat perpaduan warna ini deh. Menurutmu kalau bagian kerah luarnya kupakaiin kain kuning pastel ini, kelihatan terlalu mencolok nggak?"
        chiasa "Sebentar, coba diangkat sedikit biar kelihatan serat kainnya, Moemoe-senpai."
        nar "Moeka segera mengangkat potongan kain kuning lembut itu dan menempelkannya di dekat bahunya sendiri sambil memiringkan kepala."
        moeka "Nah, gimana kalau begini? Aku pengin hasil akhirnya kelihatan segar dan hidup, nggak pucat. Soalnya waktu evaluasi bulan lalu, dosen pembimbing bilang pilihan warna karyaku masih terlalu cari aman."
        chiasa "Bagus kok, Senpai. Kuningnya lembut, jadi kalau dipadukan sama bahan polos warna krem atau putih gading di bagian bawahnya, pasti kelihatan bersih dan cerah."
        moeka "Beneran cocok ya? Asyik! Kancing contoh yang mana nih yang paling pas menurutmu, yang kancing kayu cokelat muda atau kancing bungkus krem?"
        chiasa "Yang kancing bungkus krem kelihatan lebih halus, cocok sama potongan kerah di sketsa Senpai."
        moeka "Kalau Chimian saja sudah bilang masuk warnanya, berarti pilihanku kali ini nggak meleset. Habis ini aku tinggal mampir beli benang jahit yang senada terus..."
        nar "Kalimatnya terputus oleh getaran ponsel di samping buku sketsanya. Layar ponsel itu menyala menampilkan satu nama kontak singkat bertuliskan 'Ibu'."
        nar "Sorot mata Moeka yang tadi berbinar membicarakan pola kerah langsung meredup. Ia menurunkan potongan kain kuning itu perlahan ke atas meja, sementara raut wajahnya berubah tegang."
        moeka "Eh, maaf sebentar ya, Chimian. Ibuku telepon dari rumah."
        chiasa "Iya, silakan diangkat dulu saja, Senpai."
        nar "Moeka meraih ponselnya dan menekan tombol terima. Tangan kirinya yang bebas tampak refleks bergerak mencengkeram tali tas kanvasnya di kursi sebelah, seolah tubuhnya bersiap apabila sewaktu-waktu ia harus segera berlari mengejar kereta pulang."
        moeka "Halo, Bu? Iya, aku masih di kantin kampus, baru selesai urusan studio. Kenapa, Bu? Ayah demam lagi?"
        nar "Ia terdiam cukup lama mendengarkan suara ibunya dari seberang saluran. Rahangnya perlahan mengeras, dan punggungnya tampak kaku."
        moeka "...Iya, Bu, aku dengar kok. Tebusan obat barunya naik segitu banyak? Iya... jangan bilang ke Ren sama adik-adik dulu kalau biayanya kurang ya, Bu, nanti mereka malah kepikiran di sekolah. Biar bagian yang minggu ini aku coba carikan dulu dari sini. Iya, besok malam aku telepon Ibu lagi. Ibu juga jangan sampai telat makan."
        nar "Panggilan itu berakhir. Moeka meletakkan ponselnya perlahan di atas meja dengan layar menghadap ke bawah. Selama beberapa detik ia tetap terdiam tanpa menoleh kepadamu, tatapannya kosong jatuh pada potongan kain kuning pastel di depan tangannya."
    else:
        if kk_slot >= 3:
            nar "Kantin Pusat malam itu sudah mulai lengang di bawah cahaya lampu ruang yang terang. Saat kamu melintas membawa sekaleng kopi hangat dari mesin penjual otomatis, Moeka melambai dari meja pojok tempat ia sedang menggelar potongan-potongan kain perca warna-warni."
        else:
            nar "Kantin Pusat saat itu sudah mulai lengang. Saat kamu melintas membawa sekaleng kopi hangat dari mesin penjual otomatis, Moeka melambai dari meja pojok dekat jendela tempat ia sedang menggelar potongan-potongan kain perca warna-warni."
        moeka "Yutayuta! Kebetulan lewat sini! Mampir duduk sebentar dong, aku lagi butuh pendapat mata orang luar biar penilaianku nggak berat sebelah!"
        yutaka "Baru juga mampir sudah dibilang orang luar, Kohinata. Lagi milih bahan buat tugas apa ini?"
        moeka "Buat tugas rancangan busana musim panas! Nih, coba kamu bandingkan kain kuning pastel ini sama yang biru muda. Kalau kupakai buat aksen kerah dan manset lengan, menurutmu yang kuning terlalu terang nggak?"
        nar "Ia mengangkat lembaran kain kuning itu ke arah cahaya lampu di atas meja, menatapmu dengan mata berbinar penuh semangat."
        yutaka "Nggak terlalu terang kok. Justru kelihatan lebih hidup yang kuning daripada yang biru pucat itu. Lebih cocok sama gaya rancanganmu biasanya."
        moeka "Tuh kan, dugaanku bener! Terus buat kancingnya enakan pakai kancing kayu cokelat muda ini atau yang bening?"
        yutaka "Yang kayu cokelat muda lebih kelihatan hangat kontrasnya."
        moeka "Mantap! Kalau gitu aku kunci pakai warna kuning sama kancing kayu ini saja! Habis ini tinggal beli benangnya terus aku bisa mulai potong polanya..."
        nar "Ucapannya langsung terhenti ketika ponsel di sebelah buku sketsanya bergetar panjang. Layarnya menyala memperlihatkan nama kontak 'Ibu'."
        nar "Gerakan tangan Moeka yang sedang melipat kain kuning itu melambat hingga berhenti. Senyum lebar di wajahnya surut dalam hitungan detik, berganti dengan kerutan cemas di keningnya."
        moeka "Maaf, sebentar ya, Yutayuta. Ibuku telepon dari rumah."
        yutaka "Iya, angkat saja dulu."
        nar "Moeka mengangkat ponsel ke telinganya. Tanpa ia sadari, tangan kirinya yang berada di atas meja bergeser mencengkeram tali tas kanvasnya erat-erat, seperti seseorang yang setiap saat harus siap bergegas pulang."
        moeka "Halo, Bu? Iya, aku masih di kampus. Ada apa, Bu? Hasil kontrol Ayah tadi pagi gimana?"
        nar "Ia terdiam cukup lama mendengarkan penjelasan dari seberang telepon. Bahunya tampak menegang di balik kardigan rajutnya."
        moeka "...Iya, Bu, aku dengar. Jadi resep obat tambahannya nggak masuk tanggungan penuh ya... Iya, tolong jangan kasih tahu Ren sama adik-adik dulu soal tagihan itu ya, Bu, biar mereka fokus ujian sekolah saja. Nanti kekurangannya coba kupikirkan dari sini. Besok aku kabari Ibu lagi. Ibu jangan terlalu diporsir kerjanya."
        nar "Setelah sambungan terputus, Moeka menaruh ponselnya kembali ke meja dengan gerakan pelan. Ia belum juga mengangkat wajah ke arahmu, pandangannya tertahan pada lembaran kain kuning di depannya seolah baru saja lupa apa yang sedang ia kerjakan semenit lalu."
    call kk_family_menu("Mo05", ["\"Kalau mau cerita, aku dengerin kok. Kalau belum mau juga santai aja.\"", "\"Eh, kalau kain kuning ini dipaduin sama putih polos kayaknya lebih masuk deh.\"", "\"Ada masalah serius di rumah? Kalau lagi pusing, bilang aja ada apa.\""])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu tidak langsung memberondongnya dengan pertanyaan. Kamu hanya menggeser botol air mineral dingin yang belum dibuka dari nampanmu ke dekat tangannya, lalu duduk tenang menunggunya mengatur napas."
            chiasa "Kalau Moemoe-senpai mau cerita soal telepon barusan, aku siap dengerin kok. Tapi kalau Senpai belum pengin bicara juga nggak apa-apa, kita duduk tenang saja dulu di sini."
            nar "Moeka menatap botol air di depannya selama beberapa detik. Cengkeraman jemarinya pada tali tas kanvas perlahan mengendur, lalu ia mengembuskan napas panjang."
            moeka "Ayahku... kondisi kesehatannya belum membaik juga, Chimian. Dari bulan lalu dokter spesialisnya bilang dosis obat hariannya harus ditambah, sementara jadwal pemeriksaan rutinnya tetap harus jalan dua minggu sekali."
            chiasa "Ayah Senpai dirawat di rumah sakit?"
            moeka "Sekarang rawat jalan di rumah, soalnya kalau opname terus biayanya jauh lebih berat lagi. Tapi obat tambahannya itu sebagian nggak ditanggung asuransi, dan barusan Ibu bilang uang buku cetak sama iuran kegiatan sekolah ketiga adikku jatuh temponya barengan minggu ini."
            nar "Suaranya sempat bergetar tipis di ujung kalimat. Ia buru-buru menarik sudut bibirnya membentuk senyum kecil untuk menutupi nada bicaranya."
            moeka "...Eh, aduh, maaf ya, Chimian. Aku malah curhat masalah keluarga berat-berat begini. Harusnya kamu nggak perlu ikut dengar urusan dapur rumahku, nanti harimu malah jadi ikut suram."
            chiasa "Sama sekali nggak suram kok, Senpai. Jangan minta maaf terus. Kalau dengan diceritakan bisa bikin beban di kepala Senpai berkurang sedikit, lanjutkan saja."
            nar "Melihatmu tetap duduk tenang mendengarkan tanpa rasa risih, Moeka berhenti memaksakan senyumnya dan menyandarkan punggung ke kursi."
            moeka "Adikku di rumah ada tiga orang. Ren baru masuk SMA tahun ini, Sora masih SMP, terus si bungsu Hinata masih kelas empat SD. Sejak Ayah jatuh sakit dan nggak bisa kerja di bengkel lagi, Ibu ambil dua pekerjaan sekaligus. Pagi sampai siang di dapur toko roti, terus sorenya lanjut bersih-bersih gedung kantor dekat stasiun."
            chiasa "Ibu Senpai kerja dua tempat setiap hari? Pasti berat sekali..."
            moeka "Berat banget. Makanya aku di sini juga ambil shift kerja paruh waktu hampir setiap pulang kuliah supaya bisa rutin kirim uang ke rumah tiap bulan. Cuma kadang rasanya... setiap kali gajiku baru masuk rekening, uangnya sudah langsung habis dibagi ke pos tagihan bahkan sebelum sempat kulihat saldonya."
            chiasa "Pantas saja setiap ada jadwal kosong, Senpai hampir selalu langsung buru-buru ke tempat kerja."
            moeka "Kadang aku iri lihat mahasiswa lain yang kalau akhir bulan cuma pusing mikirin mau beli baju baru atau nongkrong di kafe mana. Aku cuma pengin ngerasain satu bulan saja bangun pagi tanpa langsung menghitung sisa uang di kepala."
            chiasa "Moemoe-senpai sudah berjuang keras sekali menjaga keluarga Senpai sambil tetap kuliah dan mempertahankan nilai beasiswa di sini. Senpai hebat sekali bisa bertahan sejauh ini."
            moeka "Belum cukup hebat kalau bulan ini masih kurang, Chimian... tapi terima kasih banyak ya sudah mau dengerin tanpa menghakimi. Rasanya dadaku yang tadi sesak waktu tutup telepon jadi jauh lebih longgar sekarang."
            nar "Moeka mengusap cepat sudut matanya dengan ujung jari, membuka botol air yang kamu berikan, lalu meminumnya beberapa teguk sebelum kembali merapikan potongan kainnya dengan napas yang lebih teratur."
        else:
            nar "Kamu tidak langsung menodongnya dengan pertanyaan. Kamu hanya menyandarkan punggung ke sandaran kursi dan menggeser kaleng minuman dingin tambahan yang tadi kamu beli ke dekat buku sketsanya."
            yutaka "Kalau kamu mau cerita soal kabar dari rumah tadi, aku dengerin kok, Kohinata. Kalau lagi malas bahas juga santai saja, nggak usah dipaksa."
            nar "Moeka memandangi kaleng minuman itu beberapa saat. Tangan kirinya yang tadi mencengkeram tali tas kanvas perlahan terlepas, dan bahunya turun mengikuti helaan napas panjang."
            moeka "Ayahku... penyakitnya belum ada tanda-tanda membaik, Yutayuta. Bulan ini dokter nambah resep obat baru yang biayanya lumayan tinggi, belum termasuk jadwal kontrol rutinnya."
            yutaka "Ayahmu sudah lama sakitnya?"
            moeka "Sudah hampir dua tahun sakit kronis, jadi sama sekali nggak bisa kerja di bengkel lagi. Terus barusan Ibu telepon dari rumah, bilang tagihan obat barunya datang barengan sama jadwal bayar buku dan seragam sekolah adik-adikku minggu ini."
            nar "Nada suaranya sempat merendah di akhir kalimat, sebelum ia cepat-cepat memaksakan senyum tipis di bibirnya."
            moeka "...Maaf ya, Yutayuta, aku malah mengeluh urusan rumah tangga yang suram begini ke kamu. Padahal tadi aku manggil kamu ke sini cuma mau nanya warna kain."
            yutaka "Nggak usah minta maaf. Aku juga lagi nggak buru-buru ke mana-mana habis ini. Kalau mau dikeluarin sekalian biar nggak sumpek di kepala, cerita saja."
            nar "Sikapmu yang tenang dan tidak memandangnya dengan tatapan kasihan membuat Moeka tampak lebih berani melanjutkan bicaranya."
            moeka "Di rumah masih ada tiga adikku yang sekolah semua. Ren baru masuk SMA, Sora masih SMP, dan si bungsu Hinata kelas empat SD. Sekarang Ibu kerja di dua tempat dari pagi sampai malam, di toko roti sama jadi petugas kebersihan kantor. Aku sendiri ambil kerja paruh waktu tiap habis kuliah supaya bisa bantu kirim uang bulanan."
            yutaka "Pantas saja belakangan ini begitu jam kuliah selesai kamu selalu langsung menghilang buru-buru dari kampus."
            moeka "Hehe, kelihatan sekali ya? Masalahnya, sekeras apa pun aku ambil jam lembur paruh waktu di toko, uangnya rasanya selalu sudah habis terpakai bahkan sebelum mampir ke rekening. Kadang aku cuma pengin ngerasain satu bulan saja bangun tidur tanpa harus langsung menghitung kurang berapa puluh ribu yen lagi buat minggu depan."
            yutaka "Kamu sudah menanggung beban sebesar itu sendirian sambil tetap jaga nilai beasiswa di kampus, Kohinata. Wajar kalau sesekali kamu merasa capek."
            moeka "...Terima kasih ya sudah mau dengerin tanpa ceramahin aku, Yutayuta. Rasanya kepalaku yang tadi tegang waktu dengar suara Ibu jadi agak entengan sekarang."
            nar "Ia mengusap sudut matanya cepat sebelum ada air mata yang sempat jatuh, lalu menarik napas panjang dan membuka kaleng minuman yang kamu sodorkan."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Melihat rahangnya yang mengatup rapat dan jemarinya yang menahan pinggiran meja, kamu tahu ia sedang berusaha keras agar tidak runtuh di tengah ruang kantin yang terbuka. Kamu memutuskan tidak menanyakan sepatah kata pun tentang isi panggilan telepon itu."
            nar "Sebagai gantinya, kamu mengambil potongan kain kuning pastel dan kain putih gading dari atas meja, lalu menyejajarkan keduanya dengan raut serius."
            chiasa "Eh, Moemoe-senpai, aku baru perhatikan lagi seratnya. Kalau kuning pastel ini dipadukan sama kain putih polos yang agak tebal ini, kayaknya jauh lebih masuk deh daripada pakai biru muda. Kalau pakai biru muda, nanti waktu kena lampu ruang pameran warnanya malah kalah."
            nar "Moeka mengerjap pelan menatap kedua potongan kain di tanganmu. Selama beberapa detik ia terdiam, lalu ketegangan di pundaknya perlahan mereda dan seulas senyum kecil yang tulus muncul di bibirnya."
            moeka "...Kamu sengaja banget nggak nanya apa-apa soal teleponku barusan ya, Chimian?"
            chiasa "Nanya apa memangnya? Kan dari tadi kita lagi diskusi soal kombinasi warna buat tugas desain Senpai."
            moeka "Hehe... terima kasih banyak ya, Chimian. Sungguh. Kadang kalau habis terima telepon dari rumah begitu, hal yang paling kubutuhkan memang cuma tetap duduk normal tanpa harus menjelaskan semuanya dari awal."
            chiasa "Santai saja, Senpai. Minum dulu airnya, habis itu kita cocokkan ukuran kancingnya sekalian."
            nar "Moeka mengangguk, menyesap air dari botol minumnya, lalu kembali meraih buku sketsa dan pensil warnanya. Beberapa menit kemudian, suaranya sudah kembali tenang saat mendiskusikan potongan pola bersamamu."
            moeka "Menurutmu kalau bagian manset lengannya kubuat agak lebar sedikit terus dipasang kancing bungkus warna krem, kelihatan rapi nggak?"
            chiasa "Kelihatan rapi dan klasik, Senpai. Cocok sama bentuk kerah yang Senpai gambar di halaman sebelah ini. Apalagi kalau jahitan tepinya dikasih benang kuning senada."
            moeka "Wah, iya benar! Ide benang kuning di tepi manset itu cakep sekali! Coba kugambar ulang detail lengannya sekarang selagi ingat."
            chiasa "Nah, sekalian tandai ukuran kain yang perlu dibeli biar besok nggak kurang."
            nar "Beban dari telepon ibunya tadi tentu belum lenyap dari pikirannya, tetapi setidaknya ia memperoleh jeda bernapas yang tenang di sampingmu tanpa merasa dipaksa membuka lukanya."
        else:
            nar "Melihat punggungnya yang masih kaku dan tatapannya yang tertuju ke permukaan meja, kamu tahu ia sedang menahan diri agar tidak tumbang di tempat umum. Kamu memilih tidak menyinggung sedikit pun soal telepon barusan."
            nar "Kamu justru meraih potongan kain kuning pastel dan biru muda di atas meja, lalu memegang keduanya berdampingan sambil mengerutkan kening dengan gaya menilai yang serius."
            yutaka "Eh, Kohinata, kalau kupikir-pikir lagi, kain kuning ini bakal jauh lebih bagus kalau dipasangkan sama bahan putih polos atau krem sekalian. Kalau biru muda ketemu kuning terang begini, nanti baju rancanganmu malah kelihatan kayak seragam pegawai toko kue."
            nar "Moeka terdiam menatapmu selama dua detik, lalu keningnya yang tadi berkerut tegang perlahan melunak. Senyum kecil yang tampak sungguh-sungguh lega terbit di sudut bibirnya."
            moeka "...Kamu sengaja nggak nanya soal telepon ibuku barusan ya, Yutayuta?"
            yutaka "Memangnya aku harus nanya? Tadi kan kamu manggil aku ke meja ini buat minta pendapat soal warna kain."
            moeka "Hehe... makasih banyak ya sudah nggak nanya-nanya. Kadang memang itu yang paling kubutuhkan waktu kepalaku lagi penuh, nggak harus buru-buru menjelaskan semuanya."
            yutaka "Santai saja. Jadi gimana, mau tetap mirip seragam toko kue atau ganti pakai kombinasi putih polos?"
            moeka "Enak saja seragam toko kue! Iya, iya, pakai bahan putih tulang saja buat bagian dasarnya biar kelihatan elegan."
            nar "Ia menghela napas panjang yang lebih ringan, lalu kembali menarik buku sketsa dan deretan kancing contohnya ke tengah meja."
            moeka "Kalau bagian kerahnya kubuat agak tegak sedikit terus kupasang kancing kayu warna cokelat muda ini, menurutmu aneh nggak?"
            yutaka "Nggak aneh, malah kelihatan rapi kontrasnya sama warna kuning tadi. Pakai yang itu saja, sekalian saku depannya jangan dibuat terlalu besar."
            moeka "Boleh juga mata orang luar satu ini! Sini kutandai dulu di pinggir sketsanya sebelum lupa."
            nar "Meski urusan dari telepon tadi belum selesai, di meja kantin itu Moeka bisa kembali fokus pada gambarnya tanpa terus-menerus dihantui rasa cemas."
    else:
        if kk_host == "chiasa":
            nar "Kamu mencondongkan badan sedikit melewati hamparan kain perca di meja dan menatap wajahnya secara langsung."
            chiasa "Ada masalah serius di rumah ya, Moemoe-senpai? Dari waktu angkat telepon tadi raut wajah Senpai langsung berubah pucat. Kalau memang lagi ada yang bikin pusing, cerita saja ke aku ada apa."
            nar "Moeka tampak terkejut mendengar pertanyaanmu yang langsung menuju sasaran. Ia menatapmu diam selama beberapa detik, menimbang apakah harus mengelak dengan candaan seperti biasa, sebelum akhirnya mengembuskan napas panjang."
            moeka "Kamu beneran mau tahu, Chimian? Nggak takut malah jadi ikut pusing dengar urusan keluargaku?"
            chiasa "Cerita saja, Senpai. Jauh lebih baik dibagi daripada Senpai pendam sendirian sambil pura-pura ketawa terus."
            moeka "...Ya sudah deh. Mungkin memang lebih ringan kalau setidaknya ada satu orang di kampus ini yang tahu kondisiku sebenarnya."
            nar "Begitu pertahanannya terbuka, cerita yang selama ini ia simpan rapat di balik sikap cerianya mengalir keluar dengan rinci."
            moeka "Ayahku sudah hampir dua tahun sakit kronis di rumah dan sama sekali nggak bisa bekerja lagi. Ibuku sekarang kerja di dua tempat dari pagi buta sampai malam, sementara tiga adikku, Ren, Sora, sama Hinata, masih sekolah semua di SMA, SMP, dan SD. Tadi Ibu telepon ngabarin kalau harga tebusan obat baru Ayah bulan ini naik tinggi, padahal minggu ini juga harus bayar buku sekolah adik-adik."
            chiasa "Tiga adik masih sekolah semua... berarti selama ini uang kerja paruh waktu Senpai dipakai buat menutup biaya rumah juga?"
            moeka "Iya. Buat bantu bayar obat Ayah, tagihan listrik rumah, sama uang sekolah adik-adikku, di luar uang sewa kamarku sendiri di sini. Belum lagi syarat nilai IPK beasiswaku di kampus ini nggak boleh turun sedikit pun, soalnya kalau beasiswaku sampai dicabut, kuliahku langsung selesai saat itu juga."
            nar "Jari-jari Moeka mengetuk pelan pinggiran buku sketsanya, tatapannya menerawang ke arah kaca jendela."
            moeka "Makanya akhir-akhir ini, jujur saja sama kamu, Chimian... kalau ada tawaran kerja tambahan yang bisa menghasilkan uang tunai cepat dalam jumlah lumayan, aku langsung tergoda buat ambil. Kepalaku sudah terlalu penuh sama angka tagihan sampai kadang nggak sempat mikir terlalu panjang."
            chiasa "Aku mengerti Senpai lagi terdesak sekali bulan ini, tapi jangan sampai Senpai ambil pekerjaan yang nggak jelas atau berbahaya ya. Kalau ada tawaran apa-apa, cek dulu baik-baik, minimal kasih tahu aku atau teman lain."
            moeka "Iya, aku tahu kok harus hati-hati... cuma masalahnya tagihan obat minggu depan nggak bisa disuruh menunggu aku dapat kerjaan yang santai."
            nar "Mendengar rincian beban keuangan yang menghimpit keluarganya setiap bulan membuatmu mengerti bahwa dalam kondisi terdesak seperti itu, tawaran pekerjaan berbayaran tinggi yang mencurigakan sekalipun akan tampak sangat menggiurkan di mata Moeka."
        else:
            nar "Kamu meletakkan kaleng kopimu di atas meja kayu dan menatap mata Moeka lurus-lurus."
            yutaka "Ada masalah berat di rumah, Kohinata? Mukamu langsung berubah total begitu dengar telepon dari ibumu barusan. Kalau lagi pusing soal sesuatu, bilang saja terus terang ada apa."
            nar "Moeka tampak terkesiap mendengar pertanyaanmu yang langsung menembak ke inti persoalan. Ia menatapmu diam beberapa detik, lalu akhirnya menurunkan bahunya dan menghela napas panjang."
            moeka "Kamu beneran mau dengar, Yutayuta? Nggak takut malah jadi kecipratan repot dengar cerita suram?"
            yutaka "Kalau cuma mendengarkan teman cerita mah nggak ada repotnya. Daripada kamu tahan sendiri sampai mukamu kaku begitu, keluarkan saja."
            moeka "...Ya sudah. Mungkin memang lebih mending kalau setidaknya ada satu orang di kampus yang tahu keadaanku sebenarnya."
            nar "Begitu ia memutuskan untuk jujur, kalimat demi kalimat yang selama ini ia tutupi rapat di balik tawa ramainya mengalir keluar tanpa ditahan lagi."
            moeka "Ayahku sakit kronis di rumah dan sudah lama nggak bisa cari nafkah. Ibuku sekarang banting tulang kerja di dua tempat sehari, sementara tiga adikku, Ren, Sora, sama Hinata, masih sekolah semua. Barusan Ibu telepon bilang biaya tebus obat baru Ayah bulan ini naik jauh dari perkiraan, padahal minggu ini jadwal bayar uang buku adik-adikku juga jatuh tempo."
            yutaka "Tiga adik masih sekolah semua? Berarti kerja paruh waktu yang kamu ambil tiap habis kelas itu buat dikirim ke rumah?"
            moeka "Iya, hampir semuanya kukirim pulang buat nutupin biaya obat sama kebutuhan adik-adik, sisanya baru buat bertahan hidup di sini. Sementara di kampus aku juga harus mati-matian jaga nilai supaya beasiswa penuhku nggak dicabut."
            nar "Ia mengetuk-ngetukkan ujung jarinya ke sampul buku sketsa, pandangannya jatuh pada lembaran kain yang belum sempat ia gunting."
            moeka "Jujur saja, Yutayuta, belakangan ini setiap kali lihat angka tagihan yang masuk, kalau ada tawaran kerjaan sampingan yang bayarannya besar dan cepat cair, aku langsung kepikiran mau sambar saja. Rasanya sudah nggak punya kemewahan buat pilih-pilih kerjaan terlalu lama."
            yutaka "Aku paham kondisi rumahmu lagi berat banget, Kohinata. Tapi justru waktu lagi kepepet begitu kamu harus ekstra waspada, jangan sampai masuk perangkap orang yang memanfaatkan keadaanmu. Kalau ada tawaran aneh-aneh, tanya dulu ke aku."
            moeka "Iya, di kepalaku aku ngerti soal itu... cuma kalau sudah ditagih tenggat waktu minggu depan, rasanya pusing sekali harus cari tambahan dari mana lagi."
            nar "Penjelasan terbuka tentang himpitan biaya keluarganya itu memberi gambaran yang sangat jelas bagimu. Dengan tekanan sebesar itu di pundaknya, Moeka berada tepat di posisi yang paling rawan terhadap tawaran uang cepat dari pihak mana pun."
    return

# ┌─ PANDUAN CERITA · Mo06 · Kuga Renji: Tawaran Foto
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : fotografer menawarkan pekerjaan modeling.
# │ INTI    : A dukung / B halangi / C ikut menemani.
# │ AKHIRAN : gerbang awal Kuga.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo06:
    call kk_scene_enter("moeka", "Kantin Pusat · Tawaran Kuga")
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Kantin Pusat malam itu masih cukup ramai oleh mahasiswa yang mencari makan malam selepas jam studio. Kamu dan Moeka duduk di meja tengah sambil memeriksa sketsa pakaian untuk tugas jahitnya di bawah lampu ruang yang terang."
        else:
            nar "Kantin Pusat hari itu cukup ramai oleh mahasiswa yang baru keluar dari kelas. Kamu dan Moeka baru saja menyelesaikan makan sambil memeriksa sketsa pakaian untuk tugas jahitnya di meja tengah."
        moeka "Lihat deh, Chimian, keliman renda di kerah jaket denim yang kemarin kubawa dari toko barang bekas akhirnya jadi juga! Semalam aku baru kelar jahit kancing terakhirnya jam satu pagi."
        chiasa "Rapi banget jahitannya, Moemoe-senpai. Dari dekat malah nggak kelihatan kalau awalnya itu jaket bekas."
        moeka "Hehe, lumayan buat hemat beli bahan tugas minggu depan kan? Rencananya..."
        nar "Kalimat Moeka terhenti ketika seorang pria jangkung berjaket kulit hitam berhenti tepat di samping meja kalian. Pria itu berusia sekitar awal tiga puluhan dengan rambut agak gondrong yang diikat rapi ke belakang dan kamera berlensa besar yang tergantung di bahunya. Tatapannya tertuju pada jaket denim berhias tambalan renda buatan tangan yang dikenakan Moeka, lalu ia tersenyum ramah."
        "Kuga" "Permisi, maaf mengganggu waktunya sebentar. Jaket denim yang kamu pakai itu hasil modifikasi jahitan sendiri, ya? Sambungan renda di kerah dan lengannya rapi sekali. Jarang ada mahasiswa yang berani memadukan tekstur kasar dan renda halus seperti itu."
        moeka "Eh? Iya, ini memang kurombak sendiri dari jaket bekas. Terima kasih banyak, Mas... eh, Pak?"
        "Kuga" "Panggil Kuga saja. Kuga Renji. Aku fotografer busana lepas untuk beberapa majalah dan katalog independen."
        nar "Ia mengeluarkan selembar kartu nama berdesain minimalis hitam-putih dari saku jaketnya dan meletakkannya di atas meja kayu. Moeka mengambil kartu itu dengan kedua tangan, dan matanya langsung melebar saat membaca deretan nama rubrik mode di bagian bawahnya."
        chiasa "Fotografer majalah mode, Moemoe-senpai?"
        "Kuga" "Beberapa proyek buku katalog dan merek pakaian lokal di pusat kota. Kebetulan minggu depan studionya sedang mencari model wajah baru dengan gaya busana jalanan yang segar dan alami. Waktu lihat kamu duduk di sini tadi, pembawaan dan gaya berpakaianmu langsung cocok sekali dengan konsep yang kami cari."
        moeka "Aku... ditawari jadi model foto? Serius, Kuga-san? Tapi aku ini mahasiswi tata busana, sama sekali belum pernah ikut pemotretan profesional di depan kamera."
        "Kuga" "Justru itu nilai tambahnya. Model dari agensi besar sering kali posenya sudah terlalu kaku dan seragam. Kami butuh ekspresi mahasiswa yang benar-benar hidup. Untuk satu sesi pemotretan selama setengah hari di akhir pekan nanti, bayaran bersihnya sebesar ini."
        nar "Kuga menyebutkan satu nominal uang tunai dengan nada bicara yang sangat ringan, lalu menambahkan bahwa akan ada bonus lipat dua apabila hasil fotonya terpilih untuk seri katalog bulan berikutnya. Kamu melihat kelopak mata Moeka langsung berkedip cepat. Jumlah uang untuk setengah hari itu sudah cukup untuk melunasi seluruh tagihan obat ayahnya dan iuran sekolah adik-adiknya bulan ini."
        moeka "Sebanyak itu... buat pemotretan setengah hari saja?"
        "Kuga" "Bayarannya langsung cair tunai selesai pemotretan hari itu juga. Selain bisa dapat penghasilan cepat, nama dan karya modifikasi pakaianmu juga bisa ikut dicantumkan buat portofolio kuliahmu. Sayang sekali kalau kesempatan emas begini terlewat cuma karena kamu terlalu lama ragu."
        nar "Meski kalimatnya terdengar sangat meyakinkan, kamu menangkap satu kejanggalan yang mencolok. Sejak awal membuka pembicaraan, Kuga terus-menerus menekankan soal bayaran tunai yang besar dan rasa takut kehilangan kesempatan, tetapi belum sekalipun menyebutkan alamat studio, nama merek kliennya, daftar kru di lokasi, maupun batas penggunaan hak cipta foto tersebut."
        moeka "Ehm... tawaran dan angkanya memang menarik sekali, Kuga-san. Tapi sebelum aku bilang iya, aku perlu tahu dulu rincian konsep sesinya, lokasi studionya di mana, sama ketetapan hak pakai fotonya nanti seperti apa. Boleh aku minta draf kontrak tertulisnya dulu buat kubaca?"
        "Kuga" "Tentu saja, draf standarnya nanti bisa kukirim lewat pesan. Cuma slot jadwal studionya minggu ini sangat padat dan ada dua kandidat lain yang juga sedang antre, jadi aku butuh kepastian awalmu hari ini kalau memang berminat."
        nar "Kuga tersenyum sopan sekali lagi, lalu pamit menepi sebentar ke dekat mesin penjual kopi di sudut kantin untuk memberi waktu Moeka mengambil keputusan. Begitu pria itu melangkah menjauh, Moeka langsung menoleh kepadamu dengan jari-jari yang masih menggenggam erat kartu nama tersebut."
        moeka "Chimian... jujur, menurutmu aku harus gimana? Bayaran setengah harinya besar sekali, bisa langsung nutup semua kekurangan uang rumahku minggu ini..."
    else:
        if kk_slot >= 3:
            nar "Kantin Pusat malam itu masih cukup hidup oleh mahasiswa yang makan selepas jam studio. Kamu duduk semeja dengan Moeka sambil mendengarkan ceritanya soal bahan tugas menjahit di bawah sorot lampu ruangan."
        else:
            nar "Kantin Pusat hari itu cukup padat oleh mahasiswa yang sedang makan dan beristirahat di sela kuliah. Kamu duduk semeja dengan Moeka sambil mendengarkan ceritanya soal bahan tugas menjahit."
        moeka "Nih, lihat deh, Yutayuta! Jaket denim rombakanku akhirnya jadi juga. Semalam sampai jam satu pagi aku pasang renda putih di bagian kerah sama ujung lengannya."
        yutaka "Rapi juga jahitannya, Kohinata. Kalau nggak bilang dari toko bekas, orang pasti ngira itu beli baru di butik."
        moeka "Hehe, yang penting hemat biaya bahan kan? Rencananya besok mau kupakai buat..."
        nar "Kalimatnya terpotong ketika seorang pria jangkung berjaket kulit hitam dengan kamera profesional tersampir di bahu berhenti di sisi meja kalian. Pria berusia awal tiga puluhan dengan rambut diikat rapi ke belakang itu memperhatikan jaket denim berhias renda buatan tangan Moeka, lalu menyunggingkan senyum santai."
        "Kuga" "Permisi, maaf menyela obrolannya sebentar. Jaket denim yang kamu pakai itu hasil rombakan tangan sendiri, ya? Pola sambungan rendanya berani dan rapi sekali. Jarang aku lihat mahasiswi yang punya selera padu padan sekuat ini."
        moeka "Eh? Iya, ini memang kujahit ulang sendiri dari jaket toko barang bekas. Terima kasih, Mas... eh, Pak?"
        "Kuga" "Panggil Kuga saja. Kuga Renji. Aku fotografer mode lepas."
        nar "Ia mengeluarkan kartu nama berwarna hitam dop dari saku jaketnya dan menaruhnya di atas meja. Moeka menerima kartu itu dengan kedua tangan, dan matanya langsung membulat saat melihat beberapa nama publikasi mode independen yang tercetak di bagian bawah kartu."
        yutaka "Fotografer mode sungguhan, Kohinata?"
        "Kuga" "Aku banyak memegang proyek katalog independen dan merek pakaian lokal. Kebetulan minggu depan aku sedang mencari model baru untuk konsep gaya jalanan yang natural. Begitu lihat kamu di meja ini tadi, gayamu langsung pas dengan karakter visual yang kucari."
        moeka "Aku disuruh jadi model pemotretan? Serius, Kuga-san? Tapi aku sama sekali nggak punya pengalaman jadi model di depan kamera profesional."
        "Kuga" "Justru karena belum pernah masuk agensi itu ekspresimu masih segar dan nggak kaku. Kamu cukup tampil natural memakai gaya pakaianmu sendiri. Untuk satu sesi singkat setengah hari minggu depan, bayaran pokoknya segini."
        nar "Kuga menyebutkan satu angka nominal dengan nada enteng, lalu menambahkan iming-iming bonus tambahan jika fotonya dipakai untuk seri katalog lanjutan. Kamu memperhatikan mata Moeka langsung membesar. Angka sebesar itu jelas langsung terhubung di kepalanya dengan tagihan obat ayahnya dan biaya sekolah ketiga adiknya yang sedang jatuh tempo."
        moeka "Sebesar itu... cuma buat sesi setengah hari?"
        "Kuga" "Uangnya langsung dibayar tunai begitu sesi foto selesai, tanpa potongan agensi. Kamu bisa bereskan kebutuhanmu sekaligus punya portofolio nyata di dunia mode. Kesempatan langka seperti ini jarang datang dua kali kalau kamu kebanyakan mikir."
        nar "Satu hal langsung terasa ganjil di telingamu. Pria ini berbicara sangat panjang lebar soal uang tunai cepat dan mendesak Moeka agar takut kehilangan peluang, tetapi sama sekali belum menjelaskan di mana letak studionya, siapa klien pemilik mereknya, bagaimana pakaian yang akan dikenakan di sesi kedua, serta ke mana saja foto-foto itu akan diedarkan."
        moeka "Ehm... terima kasih banyak atas tawarannya, Kuga-san. Tapi aku tetap perlu tahu rincian sesi pemotretannya dulu, alamat studionya, sama batas hak edar fotonya nanti gimana. Boleh aku baca lembaran kontrak resminya dulu?"
        "Kuga" "Rinciannya gampang, nanti kukirim lewat pesan singkat. Tapi karena jadwal sewa studionya sudah mepet dan masih ada kandidat lain yang siap masuk kalau kamu ragu, aku butuh jawaban kesediaanmu sekarang sebelum aku keluar dari kampus ini."
        nar "Kuga tersenyum ramah lalu melangkah menepi ke dekat deretan mesin penjual minuman otomatis agar Moeka bisa berunding sebentar. Begitu Kuga menjauh beberapa meter, Moeka langsung mencondongkan tubuh ke arahmu sambil memegangi kartu nama itu erat-erat."
        moeka "Yutayuta... menurutmu gimana? Angka bayarannya besar banget buat kerja setengah hari, tagihan rumahku minggu ini bisa langsung lunas semua kalau aku ambil..."
    call kk_family_menu("Mo06", ["\"Kalau bayarannya jelas dan bisa jadi portofolio, coba aja dulu.\"", "\"Tahan dulu, cara dia nawarin kerjaan tanpa rincian kontrak itu nggak beres.\"", "\"Kalau kamu mau coba, biar aku ikut nemenin ke sesi fotonya nanti.\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Kalau memang bayaran tunainya jelas segitu dan sekalian bisa dipakai buat portofolio desainmu, coba ambil saja dulu, Moemoe-senpai. Jarang-jarang kan ada fotografer majalah yang langsung tertarik sama hasil jahitan tangan Senpai."
            nar "Wajah Moeka yang tadinya masih menyimpan keraguan langsung tampak lega. Ia mengembuskan napas panjang, seolah dukunganmu barusan menjadi pembenaran yang ia butuhkan untuk menepiskan rasa waswasnya."
            moeka "Iya juga ya, Chimian... mungkin tadi aku saja yang terlalu curigaan gara-gara belum pernah ditawari kerjaan model. Lagian kartu namanya juga lengkap ada nomor telepon dan alamat surat elektroniknya kok."
            chiasa "Iya, yang penting nanti waktu draf rinciannya dikirim lewat pesan, Senpai baca dulu pelan-pelan sebelum hari pemotretannya."
            moeka "Sip! Kalau begitu aku samperin Kuga-san sekarang buat kasih nomor kontakku ya. Doakan semoga ini beneran jadi jalan keluar yang bagus buat bulan ini ya, Chimian!"
            nar "Moeka bangkit dari kursinya dan menghampiri Kuga di dekat mesin kopi. Dari tempat dudukmu, kamu mendengar potongan percakapan mereka."
            moeka "Kuga-san, aku bersedia ambil slot minggu depan. Ini nomor ponselku, tolong kirimkan rincian kontraknya ya."
            "Kuga" "Keputusan yang cerdas, Kohinata-san. Nanti malam kukirimkan jam dan lokasinya. Kamu tidak akan menyesal mengambil peluang ini."
            nar "Kuga tersenyum puas, menyimpan nomor ponsel Moeka, lalu menepuk ringan bahu gadis itu sebelum berpamitan keluar dari kantin. Saat Moeka kembali duduk di mejamu sambil menatap pesan konfirmasi yang baru masuk ke layar ponselnya, bayangan uang tunai yang dijanjikan itu tampak sudah menutupi seluruh rincian kontrak yang sejak awal belum terjawab."
        else:
            yutaka "Kalau bayarannya memang sebesar itu dan bisa sekalian jadi portofolio buat kuliahmu, coba ambil saja dulu, Kohinata. Lumayan kan setengah hari kerja bisa langsung nutup kebutuhan rumahmu bulan ini."
            nar "Ketegangan di bahu Moeka langsung turun. Ia tersenyum lebar penuh kelegaan, menjadikan perkataanmu sebagai alasan kuat untuk mengabaikan keraguan kecil di benaknya."
            moeka "Iya ya, Yutayuta... mungkin aku saja yang tadi terlalu banyak mikir buruk. Orang kartu namanya juga kelihatan rapi dan profesional begini kok."
            yutaka "Asal nanti waktu dia kirim pesan soal jadwal dan ketentuannya, tetap kamu periksa baik-baik sebelum berangkat ke studionya."
            moeka "Pasti! Aku ke sana sebentar ya buat kasih nomor kontakku ke Kuga-san. Semoga saja habis sesi minggu depan aku bisa traktir kamu kopi beneran buat kabar baiknya!"
            nar "Moeka segera berdiri menghampiri Kuga di dekat mesin minuman untuk menyepakati jadwal."
            moeka "Kuga-san, aku mau ambil jadwal minggu depan. Ini nomorku, nanti tolong langsung kirimkan rincian sesinya ya."
            "Kuga" "Pilihan tepat, Kohinata-san. Nanti malam kukirimkan alamat studionya. Sampai bertemu akhir pekan nanti."
            nar "Kuga menyambutnya dengan senyum tipis yang tampak sangat puas sebelum melangkah keluar dari pintu kantin. Ketika Moeka kembali ke meja sambil memandangi kartu nama di tangannya dengan mata berbinar, janji bayaran cepat itu sudah berdiri di depan mata, sementara seluruh syarat kerja yang belum sempat dijelaskan masih tertinggal di belakang."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Tahan dulu, Moemoe-senpai. Jangan langsung kasih nomor ponselmu ke dia. Jujur saja, aku merasa cara dia menawarkan pekerjaan barusan sama sekali nggak beres."
            moeka "Eh? Nggak beres gimana maksudmu, Chimian? Dia kan fotografer katalog..."
            chiasa "Coba Senpai ingat-ingat lagi kalimatnya dari awal tadi. Dia bicara panjang lebar soal uang tunai besar yang langsung cair hari itu juga, terus nakut-nakutin Senpai soal kehilangan kesempatan dan ada kandidat lain yang antre. Tapi giliran Senpai tanya hal paling dasar soal alamat studio, konsep pakaian, dan hak edar foto, dia malah mengelak bilang nanti dikirim lewat pesan dan memaksa minta jawaban sekarang juga."
            nar "Moeka terdiam di kursinya. Pandangannya turun menatap kartu nama hitam-putih di tangannya, dan jemarinya perlahan meremas tepi kertas tebal itu."
            moeka "...Kamu menyadari bagian itu juga ya, Chimian? Jujur... waktu dia bilang draf kontraknya baru bisa dikirim nanti tapi jawabannya harus sekarang, di dalam hati aku juga sempat ngerasa ada yang janggal. Cuma begitu dia sebut angka bayarannya, kepalaku langsung penuh sama bayangan tagihan obat Ayah sampai aku hampir pura-pura nggak lihat kejanggalan itu."
            chiasa "Aku mengerti banget Senpai lagi butuh uang minggu ini. Tapi fotografer profesional yang beneran punya studio resmi nggak akan keberatan kasih draf kontrak tertulis dan waktu berpikir satu atau dua hari. Kalau belum apa-apa sudah mendesak begini, risikonya terlalu bahaya buat Senpai."
            nar "Raut kecewa sempat melintas di mata biru Moeka karena bayangan uang cepat itu harus dilepaskan. Beberapa detik kemudian ia menarik napas dalam dan mengangguk mantap."
            moeka "Iya... kamu benar sekali, Chimian. Kalau aku sampai kenapa-kenapa gara-gara nekat ambil kerjaan gelap, Ibu sama adik-adikku di rumah justru bakal jauh lebih hancur. Biar kutolak tawaran mendadaknya sekarang."
            nar "Moeka bangkit berdiri dan berjalan tegas menghampiri Kuga di dekat mesin kopi."
            moeka "Maaf, Kuga-san, setelah kupikir lagi aku nggak bisa menerima tawaran pemotretan ataupun memberikan nomor pribadiku tanpa membaca dokumen kontrak resmi dan detail merek kliennya lebih dulu."
            "Kuga" "...Begitu ya. Kalau memang takut mengambil kesempatan, silakan saja. Kandidat lain masih banyak yang lebih cekatan."
            nar "Dari kursimu, kamu melihat senyum ramah di wajah Kuga langsung memudar menjadi ekspresi datar yang dingin. Ia sempat melirik tajam ke arahmu yang duduk di meja tengah, lalu berbalik meninggalkan kantin tanpa mengucapkan sepatah kata pamit pun."
            moeka "Aduh... jantungku berdebar kencang banget, Chimian. Tapi lihat wajahnya barusan berubah drastis begitu kutolak? Untung sekali kamu nahan aku tadi."
        else:
            yutaka "Tahan dulu, Kohinata. Jangan kasih nomor kontakmu ke orang itu. Cara dia menawarkan pekerjaan dari awal tadi sudah penuh tanda bahaya."
            moeka "Eh? Tanda bahaya gimana maksudmu, Yutayuta?"
            yutaka "Perhatikan polanya barusan. Dia sengaja mengumpan kamu pakai angka bayaran tunai yang nggak masuk akal buat ukuran model pemula, terus langsung menekan kamu pakai alasan jadwal mepet dan ada kandidat lain supaya kamu panik. Tapi waktu kamu minta hak paling wajar kayak draf kontrak, lokasi studio, dan batas hak pakai foto, dia nggak bisa tunjukkan satu pun sekarang."
            nar "Moeka tertegun di tempat duduknya. Matanya turun menatap kartu nama di telapak tangannya, lalu ia menghela napas panjang dengan bahu sedikit gemetar."
            moeka "...Kamu juga langsung ngerasa itu aneh ya, Yutayuta? Sebenarnya waktu dia ngotot minta jawaban sebelum keluar kantin tadi, firasatku juga sudah nggak enak. Tapi gara-gara kepalaku dari kemarin pusing mikirin tagihan rumah yang jatuh tempo minggu ini, aku hampir saja menutup mata dan langsung bilang iya."
            yutaka "Orang yang berniat memeras atau menjebak mahasiswa memang selalu mengincar mereka yang lagi kepepet butuh uang cepat, Kohinata. Kalau pekerjaannya memang bersih dan profesional, dia nggak bakal takut kasih kamu draf kontrak resmi buat dibawa pulang dan dipelajari dulu."
            nar "Moeka menggigit bibir bawahnya, menahan rasa kecewa karena harus melepas bayangan uang sebesar itu, sebelum akhirnya mengangguk tegas."
            moeka "Kamu benar, Yutayuta. Untung ada kamu di sebelahku hari ini. Kalau aku sendirian tadi, aku pasti sudah termakan omongannya. Tunggu sebentar, aku tolak dia sekarang."
            nar "Moeka berdiri dan menghampiri Kuga di dekat mesin minuman."
            moeka "Maaf, Kuga-san. Aku harus menolak. Aku nggak bisa kasih komitmen ataupun nomor pribadiku kalau belum ada draf kontrak resmi dari agensi atau kliennya."
            "Kuga" "...Baiklah. Terserah kamu saja kalau mau membuang tawaran bagus begini."
            nar "Senyum santai di wajah Kuga langsung mengeras. Pria itu melirik dingin ke arahmu yang sedang mengawasinya dari meja makan, memasukkan kembali tangannya ke saku jaket kulit, lalu melangkah keluar dari kantin tanpa menoleh lagi."
            moeka "Hhh... lihat kan cara matanya langsung berubah dingin begitu kutolak? Terima kasih banyak ya, Yutayuta."
    else:
        if kk_host == "chiasa":
            chiasa "Kalau Moemoe-senpai memang mau mencoba peluang ini karena butuh bayarannya, ambil saja, tapi ada satu syarat. Biar aku ikut menemani Senpai ke lokasi studionya waktu pemotretan nanti."
            moeka "Eh? Chimian mau ikut nemenin aku sampai ke studionya? Memangnya nggak mengganggu waktu akhir pekanmu?"
            chiasa "Sama sekali nggak mengganggu, Senpai. Aku juga bisa sekalian lihat proses penataan cahaya di studio foto. Dan yang paling penting, jauh lebih aman kalau Senpai datang ke tempat orang baru itu nggak sendirian."
            nar "Wajah Moeka langsung tampak jauh lebih tenang dan bersemangat. Ketika Kuga berjalan kembali ke meja kalian sambil memegang gelas kopi kertasnya untuk menagih jawaban, Moeka langsung menyampaikan syarat tersebut dengan tegas."
            moeka "Kuga-san, aku bersedia mencoba sesi pemotretan minggu depan, dengan syarat draf kontraknya dikirim hari ini dan temanku ini ikut menemaniku di dalam studio selama sesi berlangsung. Dia juga bisa sekalian bantu merapikan pakaian ganti dan barang-barangku di lokasi."
            nar "Tangan Kuga yang sedang memegang gelas kopi kertas tampak berhenti sesaat. Senyum ramahnya masih terpasang di bibir, tetapi sorot matanya sedikit menyipit saat melirik ke arahmu, dan nada suaranya turun lebih datar."
            "Kuga" "Oh... kamu mau bawa teman masuk ke lokasi. Sebenarnya studio kami agak sempit, tapi baiklah. Tidak masalah untuk sesi pertama ini, selama temanmu duduk tenang di pojok dan tidak mengganggu kerja kru saat pengambilan gambar."
            nar "Penekanan pada kata 'untuk sesi pertama ini' jatuh begitu saja di tengah meja. Moeka langsung menangkap perubahan nada bicara pria tersebut. Senyum polos di wajahnya meredup sedikit, digantikan sikap yang jauh lebih waspada."
            moeka "Tenang saja, Kuga-san, Chimian nggak akan mengganggu jalannya pemotretan kok. Aku cuma ingin semuanya berjalan jelas dan aman sesuai yang kita bicarakan di awal. Kehadiran satu teman kan bukan masalah kalau pekerjaannya memang pemotretan katalog biasa."
            "Kuga" "Tentu. Nanti malam kukirimkan alamat studio dan jam kumpulnya lewat pesan. Sampai ketemu minggu depan."
            nar "Begitu Kuga berbalik dan melangkah keluar dari pintu kaca kantin, Moeka mengembuskan napas panjang yang tertahan di dadanya sambil menoleh kepadamu."
            moeka "Chimian... untung sekali tadi kamu langsung bilang mau ikut menemaniku. Lihat sendiri kan cara dia menatap kamu dan perubahan nada suaranya waktu tahu aku nggak bakal datang sendirian? Sekarang aku jadi tahu kalau aku harus benar-benar waspada sama orang itu."
            chiasa "Iya, Senpai. Nanti begitu draf kontrak dan alamatnya masuk ke pesanmu, langsung teruskan ke ponselku juga ya biar kita periksa sama-sama."
            moeka "Pasti langsung kukirim ke kamu begitu masuk!"
        else:
            yutaka "Kalau kamu memang mau mencoba tawaran ini karena butuh biayanya, silakan ambil, Kohinata. Tapi ada syaratnya. Waktu hari pemotretannya nanti, aku ikut mengantar dan menemani kamu di dalam studionya sampai selesai."
            moeka "Serius, Yutayuta? Kamu mau luangin waktu akhir pekanmu buat nemenin aku di studio foto?"
            yutaka "Bisa diatur jadwalnya. Aku nggak tenang kalau membiarkan kamu datang sendirian ke studio tertutup milik fotografer lepas yang baru pertama kali kita temui di kantin."
            nar "Raut tegang di wajah Moeka langsung mencair. Saat Kuga melangkah kembali ke meja kalian sambil membawa kopi kaleng untuk meminta kepastian, Moeka langsung mengangkat wajah dan menetapkan syarat itu di awal."
            moeka "Kuga-san, aku mau ambil jadwal sesi minggu depan, tapi draf kontraknya harus dikirim hari ini dan temanku ini akan ikut menemaniku di lokasi studio selama pemotretan berlangsung. Dia sekalian bantu membawakan tas perlengkapan dan pakaian gantiku."
            nar "Kuga melirikmu yang duduk menyandar di samping Moeka. Senyum santai di wajah pria itu sedikit mengeras di bagian rahang, dan suaranya terdengar lebih dingin dibandingkan saat ia menawarkan uang beberapa menit lalu."
            "Kuga" "Bawa teman laki-laki ke studio, ya... Biasanya kami membatasi orang luar di ruang pemotretan. Tapi baiklah, tidak masalah untuk sesi perkenalan ini. Asal temanmu tahu aturan dan tidak mencampuri arahan kru di lapangan."
            nar "Mendengar tambahan kata 'untuk sesi perkenalan ini' dengan nada ketus tersebut, sorot mata Moeka langsung berubah awas. Senyum sungkannya hilang, berganti tatapan lurus yang tenang ke arah Kuga."
            moeka "Tenang saja, Kuga-san, Yutayuta nggak bakal mengganggu kerja fotografer kok. Aku cuma ingin bekerja secara profesional dan transparan. Membawa satu pendamping kan sama sekali bukan halangan kalau memang pemotretannya sesuai dengan konsep katalog yang Anda jelaskan tadi."
            "Kuga" "Tentu saja. Nanti malam kukirimkan lokasi studio dan rincian waktunya ke nomor ponselmu."
            nar "Setelah Kuga berbalik dan berjalan meninggalkan Kantin Pusat, Moeka mengembuskan napas panjang sambil menoleh ke arahmu dengan ekspresi bersyukur."
            moeka "Terima kasih banyak ya, Yutayuta. Gara-gara kamu pasang badan bilang mau ikut tadi, topeng ramahnya langsung kelihatan retak sedikit barusan. Kalau kamu nggak ikut, aku nggak tahu bakal seberbahaya apa datang ke tempatnya sendirian."
            yutaka "Makanya, nanti begitu dia kirim alamat studio dan draf kontraknya, langsung kirim salinannya ke ponselku juga. Kita cek dulu tempatnya beneran studio resmi atau bukan."
            moeka "Siap, begitu pesannya masuk langsung kuteruskan ke kamu."
    return

# ┌─ PANDUAN CERITA · Mo08 · Natal Moeka dan Adik
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia pulang ke rumah.
# │ INTI    : A ikut / B kirim hadiah / C tidak.
# │ AKHIRAN : hub besar #3.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo08:
    call kk_scene_enter("moeka", "Kantin Pusat · Menjelang Natal")
    if kk_host == "chiasa":
        nar "Kantin Pusat menjelang libur akhir tahun sudah tidak sesesak hari kuliah biasa. Di salah satu meja panjang dekat jendela, sebuah tas jinjing kain yang menggembung penuh pakaian ganti diletakkan di kursi, sementara di atas meja kayu berjajar tiga kantong kertas cokelat ukuran sedang."
        nar "Moeka duduk membungkuk di depan ketiga kantong itu dengan gunting kecil, benang jahit, dan buku catatan saku yang terbuka lebar. Di halaman buku itu, kamu melihat coretan daftar belanja yang dibagi rapi menjadi tiga kolom untuk ketiga adiknya, Ren, Sora, dan Hinata, lengkap dengan hitungan harga diskon sampai ke angka satuan yen. Sama sekali tidak ada kolom keempat untuk keperluannya sendiri."
        nar "Begitu menyadari langkahmu mendekat ke mejanya, Moeka langsung mengangkat sepotong pita satin merah murah yang ujungnya baru saja ia lipat berlapis-lapis dan ia kunci dengan dua tusukan benang hingga berbentuk bintang."
        moeka "Chimian! Sini duduk dulu, lihat deh hasil karyaku barusan. Keren nggak pita bintangnya?"
        chiasa "Rapi banget lipatannya, Moemoe-senpai. Itu dijahit tangan dari pita gulungan biasa?"
        moeka "Iya dong! Kalau beli pita bintang tempel yang sudah jadi di toko suvenir kan mahal, satu bijinya bisa seratus lima puluh yen sendiri. Kalau beli pita gulungan polos terus kulipat pakai simpul geser begini, selain hemat, nanti pas bungkusnya dibuka, pitanya nggak bakal kusut dan masih bisa dipakai buat ikat rambut si Hinata!"
        chiasa "Senpai pintar banget ngakalinya. Berarti habis ini langsung berangkat pulang ke rumah ya?"
        moeka "Iya, naik kereta komuter sejam dari stasiun depan. Padahal kemarin malam waktu teleponan, mereka bertiga sudah kompak banget bilang, 'Kakak nggak usah beli kado apa-apa, langsung pulang aja.' Dasar akunya aja yang keras kepala, dibilang nggak usah malah makin gatal pengin bawa sesuatu."
        nar "Moeka tertawa kecil sambil memasukkan sepasang sarung tangan rajut ke kantong pertama, buku komik bekas yang masih mulus ke kantong kedua, dan kotak krayon warna ke kantong ketiga."
        moeka "Aku tahu sih uang sakuku bulan ini harusnya diirit buat bayar bahan studio semester depan. Tapi kalau pulang tangan kosong pas Natal tuh rasanya kayak ada yang kurang. Tiap sudah urusan adik-adik, hitung-hitungan logikaku langsung libur duluan."
    else:
        nar "Kantin Pusat menjelang libur akhir tahun terasa jauh lebih lengang dibandingkan hari kuliah biasa. Di salah satu meja kayu dekat jendela besar, sebuah tas jinjing kain yang penuh sesak oleh pakaian ganti diletakkan di atas kursi, sementara tiga kantong kertas cokelat berjajar rapi di permukaan meja."
        nar "Moeka duduk agak membungkuk menghadapi ketiga kantong itu dengan gunting lipat, benang jahit, serta buku saku yang terbuka. Sekilas melirik catatannya dari dekat, kamu melihat daftar belanjanya dibagi rapi menjadi tiga kolom untuk ketiga adiknya, Ren, Sora, dan Hinata, lengkap dengan catatan harga diskon sampai satuan yen. Tidak ada satu baris pun yang disisihkan untuk dirinya sendiri."
        nar "Saat kamu berjalan mendekat sambil menenteng kaleng kopi hangat dari mesin otomatis, Moeka langsung mendongak dan mengangkat sepotong pita satin merah murah yang ujungnya baru ia bentuk menyerupai bintang menggunakan dua tusukan benang."
        moeka "Yutayuta! Sini duduk bentar, lihat deh hasil jahitanku barusan. Keren nggak pita bintangnya?"
        nar "Mendengar julukan akrab itu meluncur begitu saja dari mulutnya masih sempat terasa sedikit ganjil di telingamu, tetapi kamu segera menarik kursi di seberangnya dan melirik pita di jemarinya."
        yutaka "Rapi juga lipatannya, Kohinata. Itu bikin sendiri dari pita gulungan biasa?"
        moeka "Iya dong! Kalau beli pita bintang tempel yang sudah jadi di toko suvenir, satu bijinya bisa seratus lima puluh yen sendiri. Kalau beli gulungan polos terus kulipat pakai simpul geser begini, selain jauh lebih murah, nanti begitu bungkusnya dibuka, pitanya nggak bakal sobek dan masih bisa dipakai buat ikat rambut si Hinata!"
        yutaka "Wah, perhitunganmu malah lebih ketat dari waktu kita jadi panitia bagian dana festival dulu. Jadi habis ini kamu langsung naik kereta pulang ke rumah?"
        moeka "Iya, kereta komuter sejam dari stasiun depan. Padahal kemarin malam waktu teleponan, mereka bertiga sudah kompak banget bilang, 'Kakak nggak usah beli apa-apa, langsung pulang aja.' Tapi dasar akunya aja yang keras kepala, dibilang nggak usah malah makin gatal pengin bawa sesuatu."
        nar "Moeka tertawa ringan sambil menyelipkan sepasang sarung tangan rajut ke kantong pertama, buku komik bekas yang masih bersih ke kantong kedua, dan kotak krayon warna ke kantong ketiga."
        moeka "Aku tahu sih uang sakuku bulan ini sebenarnya harus dihemat buat bahan tugas studio semester depan. Cuma kalau pulang ke rumah tangan kosong pas Natal tuh rasanya kayak ada yang kurang. Begitu urusan adik-adik, logikaku langsung ambil cuti duluan."
    call kk_family_menu("Mo08", ["\"Kalau nggak keberatan, boleh aku ikut ke rumahmu sekalian bantu bawa barang?\"", "\"Tunggu sebentar, aku juga mau nitip hadiah kecil buat adik-adikmu.\"", "\"Hati-hati di jalan ya. Salam aja buat orang rumah.\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Kantongnya banyak banget ditambah tas baju segede itu, Moemoe-senpai. Kalau Senpai nggak keberatan, boleh aku ikut main ke rumah Senpai hari ini? Sekalian aku bantu bawain barang-barang ini sampai sana."
            nar "Jari Moeka yang sedang merapikan ujung pita merah terhenti. Ia menatapmu dengan mata biru cerahnya yang membulat, lalu melirik tas pakaiannya sendiri."
            moeka "Eh? Chimian serius mau ikut ke rumahku? Rumahku di kota satelit lho, naik keretanya aja sejam penuh, terus rumahnya juga sempit dan berisik banget sama anak kecil!"
            chiasa "Aku lagi luang kok hari ini, Senpai. Di rumah juga orang tuaku lagi di luar kota. Lagian aku penasaran pengin ketemu adik-adik yang sering Senpai ceritain."
            nar "Raut kaget di wajah Moeka perlahan berganti menjadi senyum hangat yang membuat matanya menyipit senang."
            moeka "Wah... kalau kamu beneran nggak keberatan sama rumahku yang seadanya, mereka pasti girang setengah mati kedatangan tamu cantik dari kampus. Sini, Chimian bawa dua kantong kertas yang ringan ini aja, tas bajunya biar aku yang cangklong."
            nar "Sepanjang perjalanan di dalam gerbong kereta komuter yang melaju keluar pusat kota, kalian duduk berdampingan sambil memangku kantong kado. Moeka tampak begitu bersemangat menjelaskan profil satu per satu penghuni rumahnya sebelum kalian tiba."
            moeka "Nanti kalau sudah sampai pintu depan, siap-siap aja ya, Chimian. Si Hinata yang umur delapan tahun itu paling nggak bisa lihat kakak perempuan, pasti langsung nempel minta lihat isi tasmu. Kalau Sora yang kelas satu SMP lagi fase sok keren, tapi aslinya paling kepo."
            chiasa "Kalau yang paling besar, Ren-kun ya?"
            moeka "Iya, Ren sudah kelas satu SMA. Dia paling pendiam mirip Ayah, tapi kalau aku pulang bawa barang berat, dia selalu yang paling pertama lari keluar ambil tas dari tanganku. Pokoknya kalau mereka bertiga mulai nanya sepuluh hal berbarengan, colek aja lenganku ya!"
            nar "Begitu kalian turun di stasiun kota satelit dan berjalan sepuluh menit menyusuri gang perumahan sederhana, pintu geser rumah keluarga Kohinata langsung terbuka bahkan sebelum Moeka sempat mengetuk. Persis seperti ucapannya, seorang gadis kecil berlari memeluk pinggang Moeka, disusul dua remaja laki-laki yang langsung mengambil alih tas pakaian serta mempersilakanmu masuk dengan sopan ke ruang tamu yang hangat oleh aroma rebusan makan malam."
        else:
            yutaka "Tas bajumu sudah hampir meledak gitu ditambah tiga kantong kado, Kohinata. Kalau nggak keberatan, boleh aku ikut ke rumahmu hari ini? Sekalian aku bantu bawain barang-barang ini sampai sana."
            nar "Moeka langsung berhenti merapikan pita merahnya dan menatapmu dengan mata biru yang melebar, lalu melirik tas kainnya yang menggembung."
            moeka "Hah? Yutayuta serius mau ikut pulang ke rumahku? Rumahku di kota satelit lho, naik keretanya sejam penuh, terus rumahnya juga kecil dan berisik banget, jauh banget bedanya sama apartemenmu!"
            yutaka "Memangnya aku lagi nyari hotel bintang lima? Hari ini aku lagi luang, nggak ada acara apa-apa. Lagian kalau kamu paksa angkat sendiri tas seberat itu naik turun tangga stasiun, bahumu bisa pegal sampai tahun baru."
            nar "Wajah kaget Moeka berubah menjadi senyum lebar yang tulus. Ia menghela napas kecil lalu menggeser tas pakaian berat itu ke arahmu."
            moeka "Kalau kamu beneran nggak keberatan sama rumahku yang sempit dan ramai... adik-adikku pasti senang banget kedatangan tamu tinggi kayak kamu. Nih, kamu angkat tas kain ini sama satu kantong yang paling berat ya, sisanya biar aku yang pegang!"
            yutaka "Sini, ringan begini mah gampang."
            nar "Sepanjang satu jam perjalanan di dalam kereta komuter yang bergerak keluar dari pusat kota, kalian duduk bersebelahan dengan barang bawaan di pangkuan dan di kaki. Moeka berbicara cepat penuh semangat untuk membekalimu sebelum sampai di depan pintu rumahnya."
            moeka "Dengar dulu ya, Yutayuta, nanti begitu pintu dibuka, kamu jangan kaget kalau langsung diserbu. Si Hinata yang umur delapan tahun itu suka heboh sendiri kalau lihat orang tinggi, pasti bakal nanya kamu atlet basket atau bukan. Terus Sora yang kelas satu SMP lagi sok-sok tenang, tapi begitu kamu nyebut komik atau game, langsung nggak berhenti ngobrol."
            yutaka "Kalau adikmu yang paling besar, si Ren?"
            moeka "Ren sudah kelas satu SMA. Dia paling pendiam mirip Ayah, jarang banyak ngomong, tapi dia yang paling cepat sigap bantuin urusan rumah. Oh ya, jangan kaget juga kalau mereka bertiga nanti nanya macem-macem berbarengan ya, anggap aja lagi wawancara dadakan."
            nar "Setelah turun di stasiun kota satelit dan berjalan kaki sepuluh menit menyusuri gang perumahan yang tenang, pintu geser rumah keluarga Kohinata langsung ditarik terbuka sebelum Moeka sempat mengetuk. Seorang gadis kecil langsung menghambur memeluk Moeka lalu mendongak takjub melihat tinggi badanmu, sementara dua adik laki-lakinya menyapa sopan dan mengambil alih kantong belanjaan sebelum mengajakmu masuk ke ruang tamu yang hangat oleh aroma sup rebusan."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Tunggu sebentar ya, Moemoe-senpai, jangan diikat mati dulu kantong kertasnya. Aku juga mau nitip hadiah kecil buat adik-adik Senpai di rumah."
            nar "Kamu membuka ritsleting tas kuliahmu, lalu mengeluarkan tiga kotak biskuit cokelat bergambar pohon Natal serta satu pak buku sketsa saku dan pulpen warna yang tadi kamu beli di toko koperasi kampus."
            moeka "Lho, Chimian?! Kok kamu malah keluarin hadiah segala buat mereka? Jangan dong, aku cerita tadi bukan buat minta dibeliin barang!"
            chiasa "Aku tahu kok, Senpai. Ini memang kebetulan tadi kubeli di koperasi, harganya juga nggak mahal. Kemarin kan Senpai pernah cerita si bungsu suka gambar terus yang cowok suka ngemil. Anggap aja salam kenal dariku buat Natal."
            nar "Moeka menatap tiga kotak biskuit dan buku sketsa di atas meja itu beberapa saat. Ia menghela napas pelan, lalu tersenyum lembut tanpa lagi berusaha mendorong barang itu kembali padamu."
            moeka "Ya ampun... kamu baik banget sih, Chimian. Kalau kubawa pulang begini, mereka bertiga pasti ngira aku yang borong semuanya. Pokoknya nanti pas buka kado di ruang tamu, bakal kubilang keras-keras kalau ini dari Chimian, adik tingkat kakak yang paling pengertian di fakultas."
            chiasa "Bilang aja dari teman kampus, Senpai. Eh, itu biskuitnya ada tiga rasa beda lho, ada stroberi, kacang panggang, sama cokelat hitam. Mending dimasukin ke kantong masing-masing dari sekarang biar nggak ketukar."
            moeka "Nah, itu krusial banget! Kalau sampai salah bagi rasa, bisa debat panjang sampai tahun baru mereka. Sebentar, yang stroberi jelas buat Hinata, yang kacang buat Sora soalnya dia suka yang gurih, terus yang cokelat hitam buat Ren."
            nar "Dengan gerakan teliti, Moeka membuka kembali simpul geser pita bintangnya, menyelipkan kotak biskuit dan buku sketsa darimu ke dalam masing-masing kantong kertas, lalu mengikatnya kembali sampai rapi."
            moeka "Lihat deh, kantongnya sekarang jadi penuh sampai ke atas. Makasih banyak ya, Chimian. Nanti malam kalau mereka sudah buka bungkusnya, aku kirimin fotonya ke kamu!"
        else:
            yutaka "Tunggu sebentar, Kohinata, jangan diikat dulu kantongnya. Aku juga mau nitip hadiah kecil buat ketiga adikmu di rumah."
            moeka "Eh? Tunggu dulu, Yutayuta! Nggak usah repot-repot begitu dong, aku cerita tadi bukan kode minta dibeliin kado buat mereka lho!"
            yutaka "Santai aja, aku nggak lagi mau beli barang mahal yang bikin kamu nggak enak. Tapi biar nggak salah pilih dan nggak ada yang merasa kebagian lebih sedikit, mending kita obrolin dulu dari sekarang. Adik-adikmu sukanya camilan rasa apa sama lagi butuh alat tulis apa?"
            nar "Moeka menatapmu beberapa detik, seolah baru menyadari bahwa kamu tidak asal menyodorkan barang mahal tanpa peduli siapa penerimanya. Sikap sungkannya perlahan surut, digantikan senyum ringan."
            moeka "Kalau kamu tanya begitu... ya sudah, daripada nanti kamu asal beli yang kebesaran atau nggak dimakan. Kalau buat Ren yang sudah SMA, dia suka cokelat hitam pahit sama buku catatan polos buat sekolah. Sora suka biskuit kacang yang gurih, terus Hinata paling senang biskuit stroberi sama spidol warna."
            yutaka "Oke, pas banget, di koperasi sebelah kantin semuanya ada. Tunggu sini lima menit ya, aku turun beli sebentar."
            nar "Tak lama kemudian kamu kembali ke meja dengan tiga paket kecil yang ukurannya sengaja kamu samakan agar tidak memicu protes di rumah, yaitu satu kotak cokelat hitam dan buku catatan polos, satu kotak biskuit kacang, serta satu kotak biskuit stroberi dengan set spidol warna."
            moeka "Wah, kamu beneran nyamain ukuran kotaknya segala ya! Kalau kutaruh di dalam kantong begini, mereka pasti langsung ngira aku yang borong semuanya. Nggak mau tahu, nanti waktu buka kado di ruang tamu bakal kubilang keras-keras kalau ini titipan dari Yutayuta, teman seangkatanku di kampus."
            yutaka "Bilang aja dari teman seangkatanmu, nggak perlu pakai embel-embel aneh. Masukin ke kantongnya sekarang biar nggak ketukar pas di kereta."
            nar "Moeka membuka simpul geser pita merahnya satu per satu, menyelipkan tiap paket ke kantong yang tepat sambil memastikan tidak ada yang tertindih, lalu mengikat ulang pita bintangnya dengan rapi."
            moeka "Nah, sekarang kantongnya jadi padat dan rapi banget. Makasih banyak ya, Yutayuta. Nanti malam waktu mereka buka bungkusnya, aku kirimin fotonya!"
    else:
        if kk_host == "chiasa":
            chiasa "Pita bintangnya beneran rapi kok, Moemoe-senpai. Hati-hati di jalan ya nanti naik keretanya, salam aja buat Ibu, Ayah, sama adik-adik di rumah."
            moeka "Siap, Chimian! Nanti kusampaikan salamnya. Selamat Natal juga ya buat kamu sama Kocchi di rumah, jangan lupa makan yang enak malam ini!"
            chiasa "Iya, Senpai. Aku duluan ke kelas studio ya."
            nar "Kamu melambai singkat lalu melangkah keluar dari Kantin Pusat. Saat melewati jendela kaca luar kantin, kamu sempat melihat Moeka masih duduk sendirian merapikan potongan sisa benang di meja, sebelum akhirnya menyampirkan tas pakaian yang berat ke bahu kirinya dan mengangkat ketiga kantong belanjaan itu sekaligus dengan kedua tangan."
            nar "Malam harinya sekitar pukul sembilan, ponselmu berdenting menerima satu pesan bergambar dari Moeka. Di layar tampak tiga anak dengan usia berbeda sedang duduk berdempetan di atas tikar ruang tamu sederhana, masing-masing memamerkan kado mereka sambil tertawa lebar."
            nar "Di bawah foto itu tertera pesan singkat bahwa ia akhirnya sampai rumah dengan selamat dan mereka bertiga sangat senang dengan kadonya, disertai ucapan selamat Natal untukmu. Moeka sendiri tidak tampak di dalam foto itu karena dialah yang berdiri di balik kamera ponsel, memastikan kebahagiaan seluruh isi rumahnya terekam utuh."
        else:
            yutaka "Pita bintangnya beneran rapi kok, Kohinata. Hati-hati di jalan naik keretanya ya, salam buat orang tua sama adik-adikmu di rumah."
            moeka "Siap, Yutayuta! Nanti kusampaikan salamnya ke mereka. Selamat Natal juga ya, jangan lupa makan enak malam ini, jangan cuma nongkrong di apartemen terus!"
            yutaka "Iya, aman. Aku duluan ya."
            nar "Kamu mengangguk singkat lalu melangkah keluar dari Kantin Pusat. Saat berjalan melewati jendela kaca panjang di luar kantin, kamu sempat melihat Moeka membereskan gunting dan potongan benang ke dalam tas kecilnya, lalu menyampirkan tas pakaian yang terlalu berat itu ke bahunya dan mengangkat ketiga kantong kertas sekaligus dengan kedua tangan."
            nar "Malam harinya sekitar pukul sembilan, ponselmu bergetar menerima sebuah kiriman foto dari Moeka. Di layar tampak ketiga adiknya duduk berdempetan di atas tikar ruang tamu sederhana sambil mengangkat hadiah masing-masing dengan tawa lepas."
            nar "Di bawah foto itu tertulis pesan singkat bahwa ia sudah sampai rumah dengan selamat dan ketiga adiknya ribut kesenangan dengan kadonya, diikuti ucapan selamat Natal untukmu. Tidak ada sosok Moeka di dalam bingkai foto itu karena ia sendiri yang memegang kamera dari belakang, memastikan seluruh isi rumahnya terlihat bahagia."
    return

# ┌─ PANDUAN CERITA · Mo09 · Hatsumode: Doa Ayah
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia berdoa untuk ayah.
# │ INTI    : A temani / B tanya / C abaikan.
# │ AKHIRAN : Intimasi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo09:
    call kk_scene_enter("moeka", "Kuil · Hatsumode")
    if kk_host == "chiasa":
        nar "Halaman kuil pada hari-hari awal Januari dipenuhi suara koin yang jatuh beradu ke dalam kotak kayu persembahan, tepukan tangan yang sahut-menyahut, serta kepulan asap dupa yang terbawa angin dingin. Kamu dan Moeka baru saja menyelesaikan giliran berdiri di depan altar utama."
        nar "Pengunjung di sebelah kanan dan kirimu sudah dua kali berganti barisan, sementara Moeka belum juga beranjak dari tempatnya. Ia sudah melempar koin lima yen, menunduk dua kali, dan menepukkan tangan seperti tata cara biasanya. Selesai menunduk terakhir, ia kembali merapatkan kedua telapak tangannya di depan dada dan memejamkan mata lebih lama."
        nar "Syal rajut merah mudanya sedikit tersingkap oleh angin, memperlihatkan rahangnya yang menegang pelan. Di keramaian kuil yang riuh, sosoknya yang biasanya paling ramai berbicara itu justru tampak sangat sunyi, seperti sedang menggenggam satu permohonan yang bahkan tidak berani ia selesaikan dengan cepat."
    else:
        nar "Halaman kuil pada awal Januari terasa riuh oleh bunyi koin yang berjatuhan ke kotak persembahan kayu, suara tepukan tangan yang bersahutan, dan kepulan asap dupa yang terbawa angin dingin. Kamu dan Moeka baru saja menyelesaikan giliran berdiri di depan altar utama."
        nar "Antrean pengunjung di sebelah kanan dan kiri sudah berganti dua gelombang, sementara Moeka masih belum beranjak dari posisinya. Ia sudah melempar koin lima yen, membungkuk dua kali, dan menepuk tangan seperti biasa. Sesudah membungkuk terakhir, ia kembali merapatkan kedua telapak tangannya dan memejamkan mata jauh lebih lama."
        nar "Angin dingin menggoyang ujung syal rajut merah mudanya, menampakkan garis rahangnya yang kaku. Di tengah suasana kuil yang ramai, gadis yang biasanya paling heboh bercerita di kampus itu berdiri sangat diam, seolah ada satu permohonan yang tidak sanggup ia akhiri begitu saja."
    call kk_family_menu("Mo09", ["Berdiri tenang di sampingnya sampai ia selesai berdoa.", "\"Lama banget doanya... tadi kamu minta apa aja?\"", "Menyingkir duluan ke luar antrean dan menunggu di dekat gerbang."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu tidak memanggil namanya ataupun menyentuh lengannya. Kamu cukup bergeser setengah langkah agar tidak menghalangi orang di belakang, lalu tetap berdiri tenang di sampingnya sambil membiarkan bunyi lonceng kuil dan langkah pengunjung berlalu di sekitar kalian."
            nar "Hampir satu menit kemudian, Moeka akhirnya menurunkan kedua tangannya yang memerah karena dingin, membuka mata perlahan, lalu menunduk sekali lagi sebelum berbalik. Begitu melihatmu masih berdiri persis di sisinya, bahunya sedikit tersentak."
            moeka "Lho, Chimian... kamu masih nungguin aku di sini sampai selesai? Kirain kamu sudah jalan duluan ke arah stan jimat tadi."
            chiasa "Nggak kok, Moemoe-senpai. Di sana juga masih ramai, mending jalan bareng aja turunnya."
            nar "Kalian berdua melangkah menepi menuju deretan bangku kayu di bawah pohon cedar tua, sedikit jauh dari antrean utama. Kamu mengeluarkan penghangat tangan saku cadangan dari tasmu dan menyodorkannya, yang langsung diterima Moeka dengan kedua tangan."
            moeka "Makasih ya, Chimian. Maaf banget tadi aku berdiri lama banget di depan kotak kayu sampai bikin kamu ikut kedinginan."
            chiasa "Nggak apa-apa, Senpai. Kelihatannya memang ada yang lagi penting banget."
            nar "Moeka menunduk menatap bungkus penghangat di telapak tangannya. Senyum cerianya yang biasa ia pasang di kampus tidak langsung muncul; sebagai gantinya, ia mengembuskan napas pendek yang berubah jadi kabut putih tipis."
            moeka "...Aku tadi berdoa supaya Ayah bisa bertahan. Setidaknya sampai aku lulus kuliah."
            nar "Ia tertawa pelan dengan nada agak malu pada ucapannya sendiri, seolah merasa bersalah karena doanya terdengar seperti sedang tawar-menawar soal waktu."
            moeka "Kedengarannya aneh ya, berdoa pakai batas waktu begitu. Soalnya dari kemarin jadwal cuci darahnya mulai bikin badannya makin sering lemas, dan Ibu nggak pernah mau bilang terus terang kalau kondisi Ayah lagi turun."
            chiasa "Nggak aneh kok, Senpai. Wajar banget kalau Senpai takut."
            moeka "Aku nggak minta keajaiban yang muluk-muluk atau tiba-tiba kaya mendadak. Aku cuma pengin... suatu hari nanti Ayah sempat duduk melihat aku berhasil bikin sesuatu yang bikin dia bangga. Sesuatu yang beneran hasil karyaku sendiri, jauh lebih dari sekadar bertahan hidup dari bulan ke bulan kayak sekarang."
            chiasa "Senpai sudah kerja keras banget dari kemarin. Kalau lagi capek atau kepikiran kayak tadi, nggak usah selalu buru-buru ketawa buat nutupin di depanku ya."
            nar "Moeka mengangguk pelan tanpa membalas dengan candaan seperti biasa. Kalian duduk berdampingan di bangku kayu itu beberapa menit lagi sambil menikmati angin yang mulai reda sebelum akhirnya turun membeli minuman hangat."
        else:
            nar "Kamu tidak menyela ataupun menarik perhatiannya. Kamu hanya bergeser setengah langkah ke pinggir agar orang di belakang tetap bisa lewat, memasukkan kedua tangan ke saku mantel, lalu menunggu dalam diam sampai ia selesai."
            nar "Hampir semenit kemudian, Moeka baru menurunkan kedua tangannya yang memerah karena angin, membuka mata pelan, lalu membungkuk sekali lagi sebelum berbalik. Melihatmu masih berdiri tepat di sebelahnya, ia tampak agak kaget."
            moeka "Eh, Yutayuta... kamu beneran nungguin aku di sini sampai beres? Kirain kamu sudah kabur duluan ke dekat stan jajanan di bawah."
            yutaka "Ngapain kabur duluan, di bawah juga antreannya penuh. Ayo minggir ke bangku sebelah pohon sana dulu, tanganmu sudah merah banget tuh kena angin."
            nar "Kalian berjalan menepi ke bangku kayu di bawah pohon cedar yang lebih tenang. Kamu sempat mampir sebentar ke mesin penjual otomatis di sisi tangga dan menyodorkan sekaleng teh susu panas ke tangan Moeka."
            moeka "Wah, makasih ya, Yutayuta. Maaf banget tadi aku berdiri lama banget di depan kotak saisen sampai bikin kamu ikut kena angin."
            yutaka "Santai aja, Kohinata. Kelihatannya memang ada yang lagi kamu pikirin serius tadi."
            nar "Moeka memegangi kaleng hangat itu dengan kedua telapak tangannya. Tidak ada nada bercanda seperti biasanya di kampus; ia menatap uap tipis napasnya sendiri beberapa saat sebelum akhirnya bicara pelan."
            moeka "...Aku tadi berdoa supaya Ayah bisa bertahan. Setidaknya sampai aku lulus kuliah."
            nar "Ia menarik tawa pendek yang terdengar sedikit malu, seperti merasa salah karena permohonannya terdengar seperti sedang menawar batas waktu."
            moeka "Aneh banget ya, berdoa sampai pakai batas waktu segala. Habisnya belakangan jadwal cuci darahnya bikin kondisi Ayah makin sering drop, sementara Ibu nggak pernah mau ngaku jujur setiap kali aku telepon nanya kabar."
            yutaka "Nggak aneh kok. Wajar aja kalau kamu takut."
            moeka "Aku nggak minta hal yang muluk-muluk, beneran. Aku cuma pengin Ayah sempat melihat aku berhasil dalam sesuatu yang bukan sekadar bertahan hidup hari ini aja."
            yutaka "Aku memang nggak bisa janji soal hasil apa pun yang belum terjadi. Tapi kalau lagi capek mikirin semua itu sendirian, nggak usah selalu maksa ketawa paling keras di depanku."
            nar "Moeka mengangguk kecil tanpa melontarkan balasan jahil seperti biasanya. Kalian duduk tenang menghabiskan minuman hangat di bangku kayu itu sampai angin dingin berangsur mereda."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Begitu Moeka akhirnya menurunkan tangannya dan melangkah keluar dari barisan depan altar, kamu segera menghampirinya saat kalian mulai berjalan menyusuri jalan setapak samping menuju tangga turun."
            chiasa "Lama banget tadi doanya, Moemoe-senpai. Antrean di sebelah aja sampai ganti dua kali. Tadi Senpai minta apa aja sih?"
            nar "Moeka sempat mengedipkan mata agak kaget, lalu tersenyum kecil sambil memasukkan kedua tangannya ke dalam saku mantel."
            moeka "Ketahuan lama banget ya? Hehe, maaf deh bikin kamu nunggu. Tadi aku berdoa buat Ayah. Tiap awal tahun selalu buat Ayah, biar pengobatannya lancar dan badannya kuat terus."
            chiasa "Buat Ibu sama adik-adik juga?"
            moeka "Iya dong, buat Ibu biar nggak jatuh sakit gara-gara kerja dobel, terus buat Ren, Sora, sama Hinata biar sekolahnya lancar. Eh, ngomong-ngomong... sekarang baru sadar nih aku."
            chiasa "Sadar apa, Senpai?"
            moeka "Dari tadi aku berdiri hampir dua menit di depan altar, tapi aku sama sekali lupa mendoakan sesuatu buat diriku sendiri."
            chiasa "Lho, serius? Kalau sekarang Senpai boleh tambah satu doa lagi khusus buat Moemoe-senpai sendiri, Senpai mau minta apa?"
            nar "Moeka langsung tertawa ringan, seperti hendak menjawab sesuatu yang bercanda soal baju atau nilai kuliah, tetapi tawanya berhenti di tengah jalan. Ia menatap ujung sepatu botnya sendiri saat kalian mulai menuruni anak tangga batu kuil satu per satu."
            moeka "Hmm... apa ya? Kok malah susah banget nyari jawabannya..."
            nar "Kamu tidak menyela dan membiarkannya berpikir sepanjang turunan tangga yang agak curam. Baru ketika kaki kalian menginjak anak tangga paling bawah di dekat gerbang kayu, Moeka menoleh ke arahmu dengan raut wajah yang lebih tenang."
            moeka "Kalau boleh minta satu hal aja buat diriku sendiri tahun ini... aku pengin ada satu hari di mana aku, Ayah, Ibu, sama ketiga adikku bisa duduk makan malam bareng sampai kenyang, tanpa satu pun dari kami harus diam-diam mikirin pengeluaran apa yang besok mesti dikurangi."
            chiasa "Semoga tahun ini beneran ada hari kayak gitu ya, Moemoe-senpai."
            moeka "Amiin! Makasih ya, Chimian, sudah nanya begitu. Rasanya agak plong juga akhirnya disebut keras-keras."
        else:
            nar "Begitu Moeka akhirnya membuka mata dan keluar dari barisan depan altar, kamu melangkah sejajar di sampingnya menyusuri jalan setapak menuju tangga turun."
            yutaka "Lama banget doanya, Kohinata. Antrean kanan kirimu sampai sudah ganti dua kali. Tadi kamu minta apa aja?"
            nar "Moeka mengerjap sebentar lalu tersenyum tipis sambil memasukkan kedua tangannya yang dingin ke saku mantel."
            moeka "Kelihatan lama banget ya? Hehe, maaf deh. Tadi aku berdoa buat Ayah. Tiap tahun baru selalu buat Ayah duluan, supaya cuci darahnya lancar dan badannya kuat terus."
            yutaka "Terus buat Ibu sama adik-adikmu juga?"
            moeka "Iya, jelas dong. Buat Ibu biar nggak tumbang gara-gara kerja dua tempat, sama buat Ren, Sora, dan Hinata biar sekolahnya aman. Eh... tunggu deh, Yutayuta. Aku baru sadar sekarang."
            yutaka "Sadar apa?"
            moeka "Hampir dua menit aku berdiri merem di depan altar tadi, tapi aku sama sekali lupa minta satu hal pun buat diriku sendiri."
            yutaka "Serius? Kalau sekarang kamu boleh nambah satu permintaan khusus buat Kohinata Moeka sendiri, kamu mau minta apa?"
            nar "Moeka sempat tertawa pendek seperti mau melontarkan jawaban iseng soal belanja kain atau nilai kuliah, tetapi kalimatnya terputus sendiri. Ia menunduk melihat langkah kakinya saat kalian menuruni deretan anak tangga batu kuil."
            moeka "Eh... apa ya? Kok malah bingung banget pas ditanya begitu..."
            nar "Kamu tidak mendesaknya dan membiarkannya diam sepanjang tangga turun. Baru ketika sepatu kalian menginjak anak tangga paling bawah di dekat gerbang kayu, Moeka menoleh menatapmu dengan nada yang lebih pelan."
            moeka "Kalau boleh minta satu hal aja buat diriku sendiri... aku pengin ada satu hari di mana seluruh keluargaku bisa duduk makan bareng tanpa satu pun dari kami harus diam-diam menghitung pengeluaran apa yang harus dikurangi besok."
            yutaka "Semoga tahun ini kesampaian ya, Kohinata."
            moeka "Iya, semoga aja! Makasih ya, Yutayuta, gara-gara kamu tanya barusan, rasanya agak lega juga akhirnya diucapkan."
    else:
        if kk_host == "chiasa":
            nar "Kamu memutuskan tidak menunggu di tengah arus antrean yang makin padat. Setelah memastikan Moeka masih memejamkan mata, kamu melangkah keluar barisan lebih dulu, menyusuri pelataran berkerikil hingga berdiri di samping pilar gerbang torii merah sambil melihat-lihat deretan stan jimat di pinggir jalan."
            nar "Sekitar lima menit kemudian, suara langkah cepat terdengar dari arah tangga atas. Moeka menghampirimu sambil menggosok kedua pipinya dengan punggung tangan. Ujung hidung dan kelopak matanya tampak agak memerah, meski sulit dipastikan apakah itu murni karena angin dingin atau hal lain."
            moeka "Chimian! Maaf ya aku lama banget di atas tadi, antreannya padat banget terus aku sempat betulin tali syal segala."
            chiasa "Nggak apa-apa, Moemoe-senpai. Aku baru sebentar kok di sini."
            nar "Kamu tidak menanyakan apa yang ia doakan tadi. Melihatmu tidak menyinggung soal itu, Moeka langsung mengeluarkan ponselnya dari saku mantel dan mengangkatnya tinggi-tinggi dengan senyum cerah yang segera terpasang rapi kembali."
            moeka "Eh, pencahayaan di bawah gerbang torii ini bagus banget lho! Sini, Chimian berdiri agak ke tengah dekat lentera kertas itu, biar aku fotoin buat kenang-kenangan Hatsumode tahun pertama kamu di kampus!"
            chiasa "Eh? Senpai nggak mau ikut difoto juga?"
            moeka "Nanti aja gampang, wajahku lagi merah kena angin nanti kelihatan kuyu di kamera. Ayo senyum dulu, satu, dua..."
            nar "Bunyi jepretan kamera ponsel mengalihkan seluruh perhatian kalian ke layar pratinjau foto. Moeka berceloteh cepat mengomentari hasil jepretan dan deretan jajanan di luar gerbang, menjaga obrolan tetap ramai agar tidak sekali pun berbalik menyentuh apa yang ia simpan di depan altar tadi."
        else:
            nar "Kamu memilih keluar dari barisan antrean yang makin padat lebih dulu. Meninggalkan Moeka yang masih memejamkan mata di depan altar, kamu menyusuri halaman kerikil lalu berdiri menunggu di dekat pilar gerbang torii merah sambil memperhatikan deretan stan jimat."
            nar "Lima menit kemudian, Moeka berjalan cepat menyusul dari arah tangga atas sambil menyeka sudut pipinya dengan punggung tangan. Mata dan ujung hidungnya terlihat agak merah karena angin dingin atau hal lain yang tidak kamu tanyakan."
            moeka "Yutayuta! Maaf ya aku lama banget di atas tadi, antreannya padat banget terus syalku sempat nyangkut segala!"
            yutaka "Nggak apa-apa, aku juga baru sebentar di bawah sini."
            nar "Karena kamu sama sekali tidak membahas doanya tadi, Moeka langsung merogoh ponsel dari saku mantel dan mengangkatnya dengan senyum cerah yang kembali utuh."
            moeka "Eh, mumpung cahayanya bagus banget di dekat gerbang merah ini, sini deh kubikinin foto Hatsumode! Tapi kamu mundur dua langkah ya, Yutayuta, badanmu ketinggian nanti atas gerbangnya nggak masuk frame!"
            yutaka "Kamu nggak sekalian ikut foto aja?"
            moeka "Nanti aja ah, mukaku lagi merah kena angin nanti kelihatan jelek di layar. Ayo siap, jangan pasang muka datar gitu dong, senyum dikit!"
            nar "Suara jepretan kamera segera memindahkan arah pembicaraan ke layar ponsel. Moeka terus mengomentari hasil foto dan jajanan kuil sepanjang jalan keluar, memastikan percakapan tidak pernah berbalik ke wajahnya sendiri."
    return

# ┌─ PANDUAN CERITA · Mo10 · Coklat untuk Tiga Adik
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia membuat coklat untuk adik.
# │ INTI    : A bantu / B beri uang / C tak peduli.
# │ AKHIRAN : pemain mengenal adik-adik.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo10:
    call kk_scene_enter("moeka", "Kantin Pusat · Coklat untuk adik")
    if kk_host == "chiasa":
        nar "Kantin Pusat menjelang pertengahan Februari dipenuhi aroma kopi hangat dan obrolan mahasiswa yang sibuk membicarakan hadiah Valentine. Di meja panjang dekat jendela yang lebih tenang, Moeka menggelar saputangan kain bersih di atas permukaan kayu, lalu menata tiga plastik bungkus cokelat buatan tangan, gunting lipat, pinset kecil, selotip bermotif, dan selembar stiker bintang berwarna emas."
        nar "Ketiga bungkus cokelat itu sudah ia pisahkan dengan pita warna berbeda supaya tidak tertukar. Bungkus pertama berikat pita biru gelap berisi cokelat hitam dengan taburan kacang almond, bungkus kedua berpita hijau cerah berisi cokelat susu renyah, sedangkan bungkus ketiga berpita merah muda berisi cokelat stroberi dengan butiran gula warna-warni."
        nar "Kamu duduk di seberangnya sambil meletakkan tas kanvasmu dan memperhatikan bagaimana Moeka menghitung ulang sisa taburan gula lalu membagi stiker bintang satu per satu dengan pinset. Ketelitian yang ia tunjukkan di depan meja itu jauh sekali berbeda dari kebiasaan cerobohnya saat mengatur jadwal pribadinya sendiri."
        chiasa "Serius banget sampai pakai pinset segala, Moemoe-senpai. Itu cokelat buat teman-teman satu jurusan atau buat anggota panitia?"
        nar "Moeka mendongak lalu tertawa cerah sambil mengangkat selembar stiker bintang emas di ujung pinsetnya."
        moeka "Bukan buat anak kampus, Chimian! Tiga bungkus ini khusus buat adik-adikku di rumah. Tunggu sebentar ya, aku lagi ngepasin biar tiap bungkus dapat persis tiga stiker bintang sama rata."
        chiasa "Sampai harus dihitung persis tiga biji begitu, Senpai?"
        moeka "Wajib banget! Kamu nggak kebayang ributnya kalau nanti bungkus yang satu dapat bintang empat terus yang lain cuma dapat dua, atau ada satu yang nggak kebagian bintang sama sekali. Bisa-bisa ruang tamu rumahku langsung berubah jadi sidang perundingan damai sampai malam. Jadi semuanya wajib dapat bintang yang sama persis!"
        nar "Ia menempelkan satu bintang emas ke bungkus pita merah muda sambil tersenyum geli, sementara di sampingnya masih tersisa satu gulung pita, beberapa kotak mika tipis yang belum dilipat, serta kartu nama kosong yang belum ditulis."
    else:
        nar "Kantin Pusat menjelang pertengahan Februari dipenuhi obrolan mahasiswa soal hadiah Valentine dan aroma kopi panas dari sudut konter. Di meja panjang dekat jendela yang agak sepi, Moeka menggelar saputangan kain bersih lalu menata tiga plastik bungkus cokelat buatan tangan, gunting lipat, pinset kecil, selotip bermotif, serta selembar stiker bintang berwarna emas."
        nar "Tiga bungkus itu diberi pita warna berbeda supaya tidak tertukar. Yang pertama berpita biru gelap berisi cokelat hitam bertabur kacang almond, yang kedua berpita hijau cerah berisi cokelat susu renyah, dan yang ketiga berpita merah muda berisi cokelat stroberi dengan butiran gula warna-warni."
        nar "Kamu menarik kursi di seberangnya sambil meletakkan botol teh dinginmu, memperhatikan bagaimana Moeka menghitung sisa taburan gula dan menempelkan stiker bintang satu per satu menggunakan pinset dengan ketelitian yang jarang sekali tampak saat ia mengurus jadwal pribadinya sendiri."
        yutaka "Serius amat sampai pakai pinset segala, Kohinata. Itu pesanan panitia atau kamu lagi mau buka lapak cokelat di kantin?"
        nar "Moeka mendongak lalu tertawa cerah sambil mengangkat selembar stiker bintang emas di ujung pinsetnya."
        moeka "Bukan buat anak kampus, Yutayuta! Tiga bungkus ini khusus buat adik-adikku di rumah. Bentar ya, jangan goyangin mejanya dulu, aku lagi ngepasin biar tiap bungkus dapat persis tiga stiker bintang sama rata."
        yutaka "Sampai harus dihitung persis tiga biji begitu?"
        moeka "Wajib banget! Kamu nggak kebayang hebohnya kalau bungkus yang satu dapat bintang empat terus yang lain cuma dapat dua, atau ada satu yang nggak kebagian bintang sama sekali. Bisa-bisa ruang tamu rumahku langsung berubah jadi meja perundingan damai sampai malam. Jadi semuanya wajib dapat bintang yang sama persis!"
        nar "Ia menempelkan satu bintang emas ke bungkus pita merah muda sambil tersenyum geli, sementara di sampingnya masih tersisa gulungan pita, beberapa kotak mika tipis yang belum dilipat, serta tiga kartu nama kosong."
    call kk_family_menu("Mo10", ["\"Sini aku bantu lipat kotak sama tempelin stikernya, biar cepat selesai.\"", "\"Ini pakai dulu uangku buat tambah beli bahan cokelat sama kotak yang lebih bagus.\"", "\"Oh, sibuk bikin buat adik-adik ya. Aku nggak ganggu deh.\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Kotak mikanya masih belum dilipat semua tuh, Moemoe-senpai. Sini aku bantu lipat kotak sama ikat pitanya sekalian, mumpung tanganku lagi nganggur."
            nar "Mata biru Moeka langsung berbinar kaget. Ia buru-buru menggeser kursi di sebelahnya dan mendorong gunting serta gulungan pita ke depanmu."
            moeka "Eh, serius Chimian mau ikut bantu bungkusin? Asyik! Nanti begitu mereka terima cokelatnya di rumah, mereka pasti langsung curiga nanya siapa yang bikin lipatan pita serapi ini. Soalnya mereka tahu banget kalau aku bikin simpul sering miring. Bakal kuceritain panjang lebar tentang kamu di depan mereka!"
            chiasa "Haha, bilang aja dibantuin adik tingkat. Eh, ngomong-ngomong, pita biru gelap yang isinya cokelat hitam almond ini buat Ren-kun ya?"
            moeka "Tepat banget! Ren itu kan sudah kelas satu SMA, gayanya sok dewasa banget kalau di depan orang. Tiap kutanya mau dibikinin cokelat apa, jawabannya selalu, 'Kak, nggak usah repot bikin buat aku, aku bisa beli sendiri.' Padahal tiap aku pulang bawa cokelat hitam pahit, punyanya yang paling duluan ludes sampai remahnya nggak bersisa!"
            chiasa "Dia diam-diam kerja paruh waktu juga ya, Senpai?"
            moeka "Iya, anak itu keras kepala banget. Kadang kami sampai agak adu mulut gara-gara dia ngotot nyuruh aku berhenti kirim uang ke rumah. Tapi begitu tahu aku capek, dia juga yang paling sigap bikinin teh hangat di dapur."
            nar "Kamu melipat kotak mika kedua sambil menyimak, lalu menyelipkan bungkus pita hijau cerah berisi cokelat susu ke dalamnya."
            chiasa "Kalau yang pita hijau ini jelas buat Sora-kun ya?"
            moeka "Ketahuan banget ya? Sora yang kelas satu SMP itu persis banget pelawak keluarga, hobi main bola sampai kaus kakinya sering bolong. Paling usil juga di rumah. Kamu tahu nggak, tiap bulan Februari begini begitu aku buka pintu rumah bawa kantong cokelat, dia pasti langsung teriak dari ruang tengah, 'Kak Moeka! Pacar kakak yang mana kali ini?!' Padahal aku aja nggak punya pacar!"
            chiasa "Wah, rame banget ya jadinya kalau kalian lagi kumpul di ruang tamu."
            moeka "Berisik setengah mati! Nah, kalau yang pita merah muda bertabur gula warna ini jelas buat si bungsu, Hinata. Dia umur delapan tahun, agak pemalu kalau baru ketemu orang asing, tapi kalau sama aku nempel terus minta dikepang rambutnya."
            chiasa "Kayaknya dia suka gambar juga ya?"
            moeka "Suka banget! Kemarin dia gambar aku pakai krayon warna pink terang banget terus ditempel di pintu kulkas pakai magnet. Makanya bungkus punya Hinata harus yang paling lucu dan pitanya nggak boleh kusut!"
            nar "Kalian berdua terus mengobrol sambil menempel sisa stiker bintang emas dan menuliskan nama di masing-masing kartu kecil sampai seluruh kotak selesai terbungkus rapi. Di antara potongan pita dan sisa kertas di atas meja, ketiga adik Moeka kini terasa begitu hidup lewat seluruh lelucon, gengsi, dan kehebohan kecil yang baru saja ia ceritakan kepadamu."
        else:
            yutaka "Kotak mikanya masih numpuk belum dilipat semua tuh. Sini kubantu lipat kotak sama potong pitanya, mumpung tanganku lagi nganggur."
            nar "Mata biru Moeka langsung membulat kaget, lalu ia menyeringai lebar dan menggeser gunting lipat beserta tumpukan kotak mika ke hadapanmu."
            moeka "Wah, seorang Kisaragi Yutaka beneran mau ikut duduk ngelipat kotak pita di kantin? Boleh banget! Nanti begitu adik-adikku terima cokelatnya di rumah, mereka pasti langsung curiga nanya siapa yang bantuin bikin lipatan serapi ini. Bakal kuceritain panjang lebar tentang kamu di depan mereka!"
            yutaka "Nggak usah dilebih-lebihkan ceritanya. Jadi yang pita biru gelap isi cokelat hitam almond ini punya adikmu yang paling tua, Ren?"
            moeka "Tepat banget! Ren itu kan sudah kelas satu SMA, gayanya sok dewasa banget kalau di depan orang. Tiap kutanya mau dibikinin cokelat apa, jawabannya selalu, 'Kak, nggak usah repot bikin buat aku, aku bisa beli sendiri.' Padahal tiap aku pulang bawa cokelat hitam pahit, punyanya yang paling duluan habis sampai nggak bersisa!"
            yutaka "Tipikal anak SMA yang gengsinya tinggi ya. Dia masih kerja paruh waktu juga?"
            moeka "Iya, keras kepala setengah mati. Kadang kami sampai agak adu mulut gara-gara dia ngotot nyuruh aku berhenti kirim uang ke rumah. Tapi begitu lihat aku pulang capek, dia juga yang paling cepat nyeduhin teh hangat di dapur."
            nar "Kamu melipat kotak mika kedua lalu menyelipkan bungkus pita hijau cerah berisi cokelat susu ke dalamnya."
            yutaka "Kalau yang pita hijau ini berarti punya Sora ya?"
            moeka "Ketahuan ya? Sora yang kelas satu SMP itu persis pelawak keluarga, hobi main bola sampai sepatunya cepat jebol dan paling usil di rumah. Kamu tahu nggak, tiap pertengahan Februari begitu aku buka pintu rumah bawa kantong cokelat, dia pasti langsung teriak dari ruang tengah, 'Kak Moeka! Pacar kakak yang mana kali ini?!' Padahal aku aja nggak punya pacar!"
            yutaka "Hahaha, pantesan rumahmu kedengarannya nggak pernah sepi."
            moeka "Berisik banget! Nah, kalau yang pita merah muda bertabur gula warna ini jelas buat si bungsu, Hinata. Dia umur delapan tahun, agak pemalu kalau baru ketemu orang asing, tapi kalau sama aku nempel terus minta dikepang rambutnya."
            yutaka "Dia yang suka gambar terus ditempel di kulkas itu?"
            moeka "Lho, kamu masih ingat?! Kemarin dia gambar aku pakai krayon pink terang banget terus ditempel di pintu kulkas pakai magnet. Makanya kotak punya Hinata harus paling rapi dan pitanya nggak boleh miring sedikit pun!"
            nar "Kalian berdua terus mengobrol santai sambil menempel sisa stiker bintang emas dan melengkapi tiap kotak sampai rapi. Di antara potongan pita di atas meja, ketiga adik Moeka berhenti menjadi sekadar daftar tanggungan di kepalamu dan berubah menjadi sosok-sosok nyata dengan humor, gengsi, dan pertengkaran kecil yang sangat dikenalnya."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kamu melirik kotak mika tipis yang beberapa sudutnya sudah agak penyok karena bahan murah serta sisa cokelat di kantong plastik yang tinggal sedikit. Tanpa banyak basa-basi, kamu membuka dompetmu, mengambil beberapa lembar uang kertas, lalu meletakkannya rapi di tepi buku catatan Moeka."
            chiasa "Moemoe-senpai, pakai uang ini dulu ya buat beli tambahan bahan cokelat sama kotak bungkus yang lebih tebal di toko depan stasiun. Sekalian buat beli camilan lain buat dibawa pulang ke rumah."
            nar "Gerakan pinset di tangan Moeka langsung berhenti. Ia menatap lembaran uang di atas meja selama beberapa detik, lalu mengangkat wajahnya menatapmu dengan senyum ceria yang mendadak mengempis."
            moeka "Eh... Chimian? Tunggu dulu, kenapa kamu tiba-tiba ngeluarin uang segala? Aku cerita soal adik-adikku tadi sama sekali nggak bermaksud minta dikasihani atau minta dibayarin lho!"
            chiasa "Aku tahu kok, Senpai. Aku juga nggak lagi mengasihani Senpai. Kebetulan uang royaltiku bulan ini masih banyak sisa, dan aku tahu akhir bulan begini ongkos kereta pulang plus bahan tugas studio pasti lagi mepet banget."
            moeka "Tetap aja, Chimian... ini jumlahnya nggak sedikit. Aku nggak enak banget nerima uang cuma-cuma dari adik tingkat sendiri."
            chiasa "Ini bukan pinjaman ya, Senpai. Nggak usah dicicil balik dan nggak ada syarat apa-apa. Anggap aja aku ikut patungan beliin hadiah Valentine buat Ren-kun, Sora-kun, sama Hinata-chan."
            nar "Moeka terdiam menatap lembaran uang di mejanya, lalu melirik ketiga bungkus cokelat sederhana yang sudah ia susun. Bahunya turun pelan saat ia akhirnya menghela napas panjang."
            moeka "...Maaf ya aku jadi kedengaran galak barusan. Jujur, harga diriku agak kesentil sedikit waktu lihat uang di atas meja. Tapi kalau dipikir buat beli bahan tambahan sama buah segar buat Ayah dan adik-adik di rumah, aku nggak boleh egois nolak bantuan tulusmu. Terima kasih banyak ya, Chimian."
            chiasa "Sama-sama, Senpai. Jangan dipikirin jadi beban ya."
            nar "Moeka mengangguk sambil tersenyum lembut dan memasukkan uang itu ke dalam amplop kecil di tasnya. Meski kamu sudah menegaskan bahwa bantuan itu sama sekali tidak menuntut balasan, kamu sempat melihat ia membuka halaman paling belakang buku saku kecilnya lalu menuliskan angka nominal pemberianmu dengan pena, masih belum terbiasa percaya bahwa ada kebaikan yang tidak akan berubah menjadi tagihan di kemudian hari."
        else:
            nar "Kamu melirik kotak mika tipis yang beberapa sudutnya sudah penyok serta bahan cokelat di kantong plastik yang tinggal sedikit. Tanpa bertele-tele, kamu mengeluarkan dompet dari saku jaket, mengambil beberapa lembar uang kertas, lalu meletakkannya rapi di samping buku catatan Moeka."
            yutaka "Nih, Kohinata. Pakai dulu uang ini buat beli tambahan bahan cokelat sama kotak yang lebih tebal di toko depan stasiun. Sisanya beliin buah atau camilan sekalian buat dibawa pulang ke rumah."
            nar "Gerakan pinset di tangan Moeka seketika berhenti. Ia menatap lembaran uang di atas meja cukup lama, lalu mendongak menatapmu dengan senyum cerah yang mendadak surut."
            moeka "Eh... Yutayuta? Tunggu dulu, kenapa kamu tiba-tiba naruh uang di meja? Aku cerita soal adik-adikku tadi sama sekali nggak bermaksud mancing biar dikasihani atau dibayarin lho!"
            yutaka "Aku juga nggak lagi mengasihani kamu. Uang bulanan dari orang tuaku masih banyak sisa di rekening, dan aku tahu akhir bulan begini ongkos kereta pulang plus bahan tugasmu lagi mepet."
            moeka "Tetap aja, Yutayuta... ini jumlahnya lumayan besar. Aku nggak enak banget nerima uang cuma-cuma begini."
            yutaka "Ini bukan pinjaman, nggak ada bunga, dan nggak ada syarat apa-apa di belakangnya. Anggap aja aku ikut patungan beliin hadiah buat Ren, Sora, sama Hinata."
            nar "Moeka terdiam memandangi lembaran uang itu, lalu melirik ketiga bungkus cokelat sederhana yang baru ia susun. Bahunya turun pelan bersama embusan napas panjang."
            moeka "...Maaf ya tadi nadaku sempat agak ketus. Jujur, aku agak kaget aja lihat uang ditaruh langsung di depan mata. Tapi kalau buat beli bahan tambahan sama buah segar buat Ayah dan adik-adik di rumah, aku nggak boleh keras kepala nolak niat baikmu. Terima kasih banyak ya, Yutayuta."
            yutaka "Santai aja. Nggak usah dipikir jadi utang."
            nar "Moeka mengangguk sambil tersenyum lembut dan menyimpan uang itu ke dalam amplop kecil di tasnya. Meskipun kamu sudah menegaskan bantuan itu tidak menuntut balasan, kamu tetap melihat ia membuka halaman paling belakang buku saku kecilnya lalu mencatat angkanya dengan pena, belum mudah percaya bahwa ada pemberian yang tidak akan berubah menjadi tagihan saat ia berkata tidak nanti."
    else:
        if kk_host == "chiasa":
            chiasa "Oh, ribet juga ya urusan bungkusin cokelat buat tiga anak sekaligus. Ya sudah, aku nggak ganggu deh, aku mau sekalian ngecek catatan buat kelas besok dulu."
            nar "Kamu menunduk membuka ponselmu dan mulai menggulir halaman jadwal kuliah di layar sambil menyeruput minuman dinginmu tanpa lagi melihat ke arah deretan stiker bintang di depan Moeka."
            moeka "Haha, iya sih, emang agak ribet. Soalnya si Sora itu dari dulu paling jeli kalau soal ukuran bungkusan, kemarin aja waktu aku pulang bawa—"
            chiasa "Hmm, gitu ya."
            nar "Ucapan Moeka melambat di tengah kalimat saat ia menyadari pandanganmu sama sekali tidak terangkat dari layar ponsel. Senyum ramainya sedikit surut, lalu ia buru-buru mengangguk sendiri dan kembali menundukkan kepala ke atas saputangan kainnya."
            moeka "Eh, maaf ya, Chimian! Aku malah ngoceh panjang soal adik-adikku padahal kamu lagi sibuk ngecek tugas. Lanjutin aja urusanmu, aku beresin ini diam-diam kok."
            chiasa "Oke, semangat ya, Senpai."
            nar "Dua puluh menit berikutnya berjalan dalam keheningan yang hanya diisi bunyi gunting memotong pita dan plastik yang dilipat. Moeka tidak lagi menyebut satu pun nama adiknya sampai kamu bangkit berpamitan menuju ruang kuliah."
            nar "Ketika kamu melangkah menjauh dari meja sudut itu, ketiga bungkus cokelat sudah selesai tersusun sangat rapi dengan tiga stiker bintang emas di tiap sisinya, tanpa ada sedikit pun jejak di wajah ceria Moeka yang menunjukkan betapa lama ia duduk menyelesaikan semuanya seorang diri."
        else:
            yutaka "Oh, sibuk bikin buat tiga adik sekaligus ya. Ribet juga kedengarannya. Ya sudah, aku nggak ganggu deh, aku mau sekalian cek pesan tugas kelompokku dulu."
            nar "Kamu bersandar di kursi, membuka layar ponselmu, dan mulai menggulir pesan kuliah sambil meneguk teh dingin tanpa lagi menatap deretan stiker bintang di hadapan Moeka."
            moeka "Haha, iya sih, lumayan ribet. Soalnya si Sora itu dari dulu paling cerewet kalau soal ukuran bungkusan, kemarin aja waktu aku pulang bawa—"
            yutaka "Hmm, begitu ya."
            nar "Kalimat Moeka melambat lalu berhenti sendiri begitu ia melihat matamu sama sekali tidak beranjak dari layar ponsel. Senyum ramainya sedikit mengempis, kemudian ia mengangguk cepat dan kembali menunduk ke atas saputangan kainnya."
            moeka "Eh, maaf ya, Yutayuta! Aku malah ngoceh panjang soal adik-adikku padahal kamu lagi sibuk cek pesan tugas. Lanjutin aja urusanmu, aku beresin ini diam-diam kok."
            yutaka "Oke, duluan ya."
            nar "Menit-menit berikutnya berlalu dalam senyap yang hanya diisi suara gunting memotong pita dan gemerisik plastik bening. Moeka tidak lagi menyebut satu pun nama adiknya sampai kamu bangkit meninggalkan meja sudut itu, sementara ketiga bungkus cokelatnya tetap selesai tersusun sangat rapi tanpa sedikit pun jejak yang menunjukkan berapa lama ia duduk di sana sendirian."
    return

# ┌─ PANDUAN CERITA · Mo11 · Hujan Deras: Ponsel Mati
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia hilang kontak.
# │ INTI    : A cari / B tunggu / C abaikan.
# │ AKHIRAN : jendela intervensi #1; stage 1 (beban menumpuk).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo11:
    call kk_scene_enter("moeka", "Kantin Pusat · Ponsel mati")
    play sound "audio/sfx/rain.wav"
    nar "Panggilan ke Moeka tidak tersambung sejak pagi. Ia tak muncul pada kegiatan yang biasanya justru dimintanya agar dimulai tepat waktu. Di luar, hujan membuat semua rencana mencari terasa lebih sulit."
    nar "Pesan terakhirnya hanya mengatakan akan menyusul. Kalimat yang biasa tidak cukup menenangkan ketika kabar lain juga mulai hilang."
    call kk_family_menu("Mo11", ["Cari ia sampai ketemu.", "Tunggu sampai ia muncul sendiri.", "Abaikan."])
    if _return == "A":
        moeka "Kau mencariku? Di tengah hujan begini? ...Kenapa? Aku bukan siapa-siapa yang penting."
        nar "Ponselnya mati dan harinya berantakan oleh urusan rumah. Kau menemukannya basah, terlalu letih untuk menyiapkan cerita lucu tentang itu."
        nar "Kau mengatakan ketidakhadirannya diketahui. Untuk beberapa saat ia tidak percaya bahwa seseorang boleh mencarinya tanpa sedang membutuhkan sesuatu darinya."
    elif _return == "B":
        nar "Kau menunggu sampai ia menghubungi. Kabar baru datang keesokan hari, disertai tawa tentang ponsel yang tidak bisa diandalkan. Moeka tidak menyebut berapa lama ia bingung harus pulang ke mana lebih dahulu."
    else:
        nar "Kau menganggapnya urusan biasa yang tidak perlu ditanyakan. Moeka kembali dengan penjelasan pendek dan segera mengambil tugas tambahan agar orang berhenti membahas ketidakhadirannya."
        nar "Hari yang buruk berlalu tanpa seorang pun mengetahui seberapa buruk rasanya dari dalam. Ia menyimpan pelajaran bahwa menghilang sedikit pun tampaknya tidak banyak mengubah kehidupan orang lain."
    return

# ┌─ PANDUAN CERITA · Mo12 · IPK Turun
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : nilai turun.
# │ INTI    : A bantu belajar / B beri uang / C tidak peduli.
# │ AKHIRAN : beasiswa mulai terancam.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo12:
    call kk_scene_enter("moeka", "Kantin Pusat · IPK turun")
    nar "Moeka menatap nilai lebih lama daripada pesan keluarga tentang uang. Dua masalah itu tidak bisa lagi diletakkan di laci yang berbeda: bekerja lebih banyak menggerus kuliah, kuliah yang jatuh mengancam satu hal yang membuatnya mampu tetap bekerja untuk rumah."
    moeka "Aku selalu bilang tinggal atur jadwal. Sekarang jamnya sudah habis. Kalau beasiswa hilang, aku nggak punya cadangan yang bisa dibuat dari semangat saja."
    call kk_family_menu("Mo12", ["Bantu ia belajar.", "Beri ia uang untuk meringankan beban.", "Tidak peduli."])
    if _return == "A":
        moeka "Kau mau menemaniku belajar? ...Mungkin masih ada jalan kalau tidak sendirian."
        nar "Kalian memulai dari satu tugas yang paling dekat tenggat, bukan menuntut seluruh semester diperbaiki malam itu. Ia berhenti menyebut dirinya bodoh ketika akhirnya berhasil menjelaskan bagian yang tadi tak dipahami."
    elif _return == "B":
        moeka "Uang lagi? ...Aku mulai merasa berutang padamu lebih dari yang bisa kubalas."
        nar "Bantuan itu mengurangi kebutuhan bekerja untuk sementara. Kau mengatakan ia tidak harus menukar kedekatan demi menerimanya, tetapi ia perlu waktu sebelum benar-benar percaya bahwa penolakan di masa depan tidak akan membuat uang ini disebut kembali."
    else:
        nar "Kau tidak menanggapi lebih jauh. Moeka menutup layar nilai dan mulai membicarakan pekerjaan berikutnya, sesuatu yang masih tampak dapat menghasilkan uang sekarang."
        nar "Makin sedikit ruang tersisa untuk hal yang baru akan runtuh beberapa bulan lagi. Ia terus berlari di antara keduanya, sendirian."
    return

# ┌─ PANDUAN CERITA · Mo26 · Natal Sunyi
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia sendirian.
# │ INTI    : A datang / B kirim pesan / C tidak ada.
# │ AKHIRAN : jendela #5.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo26:
    call kk_scene_enter("moeka", "Kantin Pusat · Natal sunyi")
    nar "Moeka mengirim foto lampu Natal di luar jendelanya tanpa ikut muncul. Ketika kautanya apakah sedang di rumah, jawabannya datang terlambat: masih di kos, belum tahu nanti."
    nar "Di meja ada makanan yang belum dibuka dan ponsel yang terus diperiksa. Malam itu ia tidak punya tenaga untuk membuat kesendirian terdengar seperti pilihan yang seru."
    call kk_family_menu("Mo26", ["Datang menemaninya langsung.", "Kirim pesan agar ia tahu ada yang ingat.", "Tidak melakukan apa pun."])
    if _return == "A":
        moeka "Kau datang? Di malam seperti ini? ...Aku hampir percaya tidak ada yang akan datang."
        nar "Kau tidak meminta ia segera senang. Kalian membuka makanan, menghubungi orang yang perlu tahu keadaannya, dan membiarkan malam berlangsung tanpa pertunjukan bahwa semua sudah baik."
    elif _return == "B":
        moeka "Pesanmu masuk. ...Satu pesan. Kadang satu saja cukup untuk melewati satu malam."
        nar "Kau menanggapi dengan sungguh-sungguh dan menanyakan siapa yang bisa menemaninya jika malam terasa makin berat. Ia menyebut Rina setelah ragu. Kabar singkat itu tidak menyelesaikan masalahnya, tetapi membuka jalan agar ia tidak hanya menunggu satu orang."
    else:
        nar "Kau tidak menghubungi. Foto lampu itu tetap menjadi pesan terakhir dari Moeka malam tersebut. Di kos, ia menaruh ponsel menghadap bawah lalu membaliknya lagi beberapa menit kemudian."
        nar "Tidak ada satu malam yang sendirian menjelaskan seluruh krisis. Malam ini menambah sesuatu pada tumpukan yang belum berhasil dibagikannya kepada orang lain."
    return

init 1 python:
    _hook("Mo03-A", lambda: kk_rel("moeka","trust",-2))
    _hook("Mo03-B", lambda: (kk_rel("moeka","trust",4), kk_adj("stres_moeka",-5)))
    _hook("Mo03-C", lambda: (kk_rel("moeka","trust",5), kk_adj("stres_moeka",-8)))
    _hook("Mo04-A", lambda: (kk_rel("moeka","intim",6), kk_flag("moeka_rahasia_lapar")))
    _hook("Mo04-B", lambda: kk_rel("moeka","trust",4))
    _hook("Mo04-C", lambda: (kk_adj("stres_moeka",8), kk_rel("moeka","trust",-4)))
    _hook("Mo05-A", lambda: (kk_flag("moeka_keluarga_diketahui"), kk_rel("moeka","intim",4)))
    _hook("Mo05-B", lambda: kk_rel("moeka","trust",4))
    _hook("Mo05-C", lambda: (kk_flag("moeka_keluarga_diketahui"), kk_moeka_burden(5)))
    _hook("Mo06-A", lambda: (kk_flag("kuga_jerat_mulai"), kk_adj("stres_moeka",-10)))
    _hook("Mo06-B", lambda: (kk_rel("moeka","trust",5), kk_flag("kuga_dihalangi")))
    _hook("Mo06-C", lambda: kk_flag("kuga_ditemani"))
    _hook("Mo08-A", lambda: (kk_rel("moeka","intim",6), kk_flag("moeka_adik_dikenal")))
    _hook("Mo08-B", lambda: kk_rel("moeka","aff",4))
    _hook("Mo08-C", lambda: kk_moeka_burden(8))
    _hook("Mo09-A", lambda: (kk_rel("moeka","intim",5), kk_flag("moeka_ayah_diketahui")))
    _hook("Mo09-B", lambda: (kk_rel("moeka","trust",4), kk_flag("moeka_ayah_diketahui")))
    _hook("Mo09-C", lambda: kk_rel("moeka","trust",-3))
    _hook("Mo10-A", lambda: (kk_rel("moeka","intim",5), kk_flag("moeka_adik_dikenal")))
    _hook("Mo10-B", lambda: kk_adj("stres_moeka",-6))
    _hook("Mo10-C", lambda: kk_rel("moeka","aff",-3))
    _hook("Mo11-A", lambda: (kk_rel("moeka","trust",6), kk_flag("moeka_intervensi_1")))
    _hook("Mo11-B", lambda: (kk_moeka_stage(1), kk_moeka_burden(6)))
    _hook("Mo11-C", lambda: (kk_moeka_stage(1), kk_moeka_burden(12)))
    _hook("Mo12-A", lambda: (kk_rel("moeka","trust",5), kk_adj("stres_moeka",-8)))
    _hook("Mo12-B", lambda: kk_adj("stres_moeka",-5))
    _hook("Mo12-C", lambda: (kk_adj("stres_moeka",12), kk_flag("beasiswa_terancam")))
    _hook("Mo26-A", lambda: (kk_rel("moeka","intim",8), kk_flag("moeka_ditemani_natal"), kk_adj("stres_moeka",-15)))
    _hook("Mo26-B", lambda: (kk_rel("moeka","trust",5), kk_flag("moeka_dikabari_natal")))
    _hook("Mo26-C", lambda: (kk_adj("stres_moeka",15), kk_flag("moeka_natal_sendiri")))
