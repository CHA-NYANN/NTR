# Kouseikan — alur. Prolog, vertical slice, pemutar event generik, Force (abstrak), evaluasi.
# Prototipe: teks hanya poin utama (awal → pilihan → akibat ringkas). Story penuh menyusul.

label kk_intro:
    scene black with fade
    call screen kk_titlecard("KOUSEIKAN", "18+ · semua tokoh dewasa")
    $ kk_bgm("platform", level=0.56)
    play story_crowd "audio/sfx/platform_crowd.wav" fadein 0.6
    nar "Peron stasiun kereta bawah tanah sore itu pengap oleh udara lembap dan desakan orang-orang yang baru pulang kerja. Di tengah kebisingan itu, perhatianmu justru terpaku sepenuhnya pada layar ponsel di genggamanmu."
    nar "Di layar itu terpampang bab terbaru 'Kouseikan'—sebuah manga romansa kampus yang entah bagaimana selalu bertengger di peringkat teratas aplikasi bacaan mingguan."
    nar "Kau mendengus sinis sambil menggeser layar dengan ibu jari. Semakin jauh kau membacanya, semakin gatal rasanya ingin memaki di kolom komentar."
    nar "Bagaimana mungkin cerita sampah macam ini bisa begitu populer? Sejak bab pertama, alurnya jelas-jelas cuma mimpi basah authornya yang dituangkan tanpa tahu malu."
    nar "Tokoh utamanya, Amamiya Koita, hanyalah mahasiswa sastra biasa yang modalnya cuma senyum ramah dan jawaban menggantung. Ia tidak pernah tegas menolak siapa pun dengan dalih 'tidak tega menyakiti', tetapi seluruh isi cerita memujanya seolah ia pria paling tulus di muka bumi."
    nar "Lebih parahnya lagi, gadis-gadis cantik di sekelilingnya dibuat jatuh cinta hanya karena kebaikan sepele, sementara keluarga, sahabat dan orang-orang di sekitarnya direduksi menjadi figuran bodoh yang rela mengorbankan perasaan mereka demi kebahagiaan sang protagonis."
    $ kk_bgm("tension", fade=0.3, level=0.46)
    play story_crowd "audio/sfx/platform_panic.wav" fadeout 0.2
    nar "Jempolmu baru saja mengetik sepatah kalimat pedas di kolom ulasan ketika tiba-tiba jeritan melengking memecah keramaian peron."
    nar "Kau menoleh spontan dari layar ponsel. Beberapa langkah di sebelahmu, seorang anak kecil terlepas dari genggaman ibunya, terpeleset melewati garis kuning, dan jatuh tersungkur ke atas batu-batu rel."
    play story_rail "audio/sfx/train_rail.wav" fadein 0.8
    play story_train "audio/sfx/train_horn.wav"
    nar "Di ujung terowongan yang gelap, dua sorot lampu kereta ekspres sudah menyala menyilaukan. Klakson panjang meraung memekakkan telinga, disusul gemuruh roda besi yang membelah rel dengan kecepatan penuh."
    play sound "audio/sfx/phone_drop.wav"
    nar "Orang-orang di peron hanya menjerit kaku sambil menutup mulut—tidak ada satu pun yang berani bergerak. Panik menyergap dadamu lebih cepat daripada akal sehat; ponselmu terlepas jatuh ke lantai saat kakimu refleks melompat turun ke atas rel."
    nar "Kau merengkuh tubuh mungil yang gemetar itu dan mengangkatnya sekuat tenaga ke atas bibir peron, tepat saat beberapa tangan penumpang lain menarik kerah baju anak itu hingga selamat."
    play story_train "audio/sfx/train_brake.wav"
    nar "Anak itu lolos. Namun ketika kau bertumpu pada kedua tangan hendak memanjat naik, cahaya putih lampu kereta sudah menelan seluruh pandanganmu, diiringi derit rem darurat yang merobek gendang telinga."
    play sound "audio/sfx/train_impact.wav"
    stop story_train fadeout 0.15
    stop story_crowd fadeout 0.18
    stop story_rail fadeout 0.4
    nar "Hantaman baja yang masif meremukkan tulang rusukmu dalam sekejap. Tubuhmu terlempar ringan seperti boneka kain sebelum dingin yang pekat menyergap."
    nar "Di detik terakhir sebelum kesadaranmu benar-benar padam, bukan rasa takut yang melintas di kepalamu, melainkan cibiran getir yang tak bisa di tahan."
    nar "Bisa-bisanya kau mati tertabrak kereta gara-gara menyelamatkan anak kecil—persis pembuka cerita fiksi pasaran yang belakangan ini bertebaran di mana-mana. Benar-benar klise. Menyebalkan. Kenapa segalanya terasa sangat menyebalkan sampai akhir?"
    stop music fadeout 0.3
    nar "Lalu segalanya terputus menjadi hitam."
    nar "Tidak ada lagi raungan klakson atau teriakan penumpang. Tidak ada rasa sakit, tidak ada dinginnya lantai peron, bahkan tidak ada detak waktu. Kesadaranmu hanya mengapung tanpa bobot di dalam keheningan alam bawah sadar yang gelap gulita."
    $ kk_bgm("system")
    nar "Entah berapa lama kau terombang-ambing di kehampaan itu, sampai perlahan-lahan kegelapan di hadapanmu mulai bergeser."
    nar "Dari balik bayangan pekat, dua buah tangan terulur menembus ruang hampa, berhenti tepat dalam jangkauanmu tanpa sepatah kata pun."
    nar "Di sebelah kiri, terulur tangan seorang pria—berjari panjang, rapi, dan terawat."
    nar "Di sebelah kanan, terulur tangan seorang wanita—ramping, lentik, dengan bekas kapalan tipis di ruas jari tengahnya."
    nar "Kau sama sekali tidak tahu milik siapa kedua tangan itu, atau ke mana mereka akan menyeretmu pergi. Namun instingmu berbisik jelas: jika kau tidak ingin lenyap begitu saja setelah kematian konyol tadi, kau harus memilih salah satu dan menggenggamnya sekarang."
    call screen kk_route_select
    $ kk_host = _return
    $ kk_setup_state()
    call kk_prologue
    nar "Ikon wajah di layar kaca biru itu menyipitkan mata, lalu memunculkan barisan teks baru berwarna kuning menyala tepat di depan hidungmu."
    sistem "( ` v ´ )b Dan karena aku tahu kau bakal malas bergerak kalau tidak dipecut, ini misi pembukamu: dalam tujuh hari ke depan, temui tiga orang yang dekat dengan Koita."
    sistem "Amati tabiat mereka, ajak bicara, dan cari tahu celah mana yang bisa kauungkit. Jangan coba-coba mengurung diri di kamar sampai tenggatnya habis—aku paling benci pemeran yang mogok kerja, dan kau sudah merasakan sendiri caraku memberi teguran~ (^_~)-*"
    play sound "audio/sfx/system_close.wav"
    nar "Jendela kaca biru itu menutup dirinya paksa dengan bunyi dengung halus, meninggalkanmu bersama detak jantung yang masih memburu di tengah pagi tanggal tujuh April."
    jump kk_main

label kk_prologue:
    $ kk_bgm(kk_host)
    if kk_host == "yutaka":
        $ kk_mc_nama = "YUTAKA (kau)"
        show screen kk_set("yutaka", "Apartemen Mewah · Dini Hari")
        with fade
        nar "Begitu jemarimu menggenggam tangan pria itu di dalam kehampaan, gravitasi mendadak berbalik arah. Sebuah sentakan keras merenggut kesadaranmu turun menembus lorong gelap yang pengap, seolah tubuhmu diikat batu dan dilempar paksa ke dasar air yang tak bertepi."
        nar "Gema derit rem baja dan raungan klakson kereta ekspres masih memekakkan telinga batinmu ketika kau tersentak bangun dengan tarikan napas panjang yang memburu."
        nar "Kedua tanganmu refleks mencengkeram bagian tengah dadamu kuat-kuat. Otot-ototmu menegang hebat, bersiap menyambut rasa ngilu dari tulang rusuk yang remuk dihantam moncong lokomotif serta rembesan darah panas di atas batu rel."
        nar "Namun rasa sakit yang kauantisipasi itu tidak pernah datang. Tidak ada tulang yang patah, tidak ada bau amis besi dari darah yang tumpah, dan tidak ada dinginnya kerikil peron kereta bawah tanah di punggungmu."
        nar "Yang tergenggam oleh jari-jarimu yang panjang justru permukaan kaus tidur berbahan katun lembut yang lembap oleh keringat dingin, membungkus bidang dada yang terasa rata, utuh, berotot ramping, dan jauh lebih lebar dari ukuran tubuh yang kauingat."
        nar "Dari lipatan selimut linen berwarna abu-abu gelap yang menutup pinggangmu, menguar aroma deterjen bersih yang sejuk bercampur samar dengan wangi kayu cedar."
        nar "Kau mengerjap keras berkali-kali, mengatur tarikan napas yang masih tersengal di kerongkongan sambil mengedarkan pandangan ke sekeliling ruangan."
        nar "Kau tidak sedang berbaring di aspal stasiun maupun di atas brankar ruang gawat darurat, melainkan di atas ranjang berukuran besar di dalam sebuah kamar apartemen modern yang sangat luas, rapi, dan sunyi senyap."
        nar "Langit-langit beton ekspos yang tinggi, tirai jendela kaca setinggi dinding yang menyisakan siluet gedung-gedung kota saat dini hari, serta dengung halus mesin pendingin udara di tengah keheningan yang terasa terlalu hampa untuk satu orang membuat keningmu berkerut dalam."
        nar "Setiap detail di ruangan mewah yang dingin ini terasa begitu nyata—dan kau yakin belum pernah menginjakkan kaki di tempat seperti ini seumur hidupmu."
    else:
        $ kk_mc_nama = "CHIASA (kau)"
        show screen kk_set("chiasa", "Rumah Amamiya · Pagi")
        with fade
        nar "Begitu jemarimu menggenggam tangan wanita itu di dalam kehampaan, gravitasi mendadak berbalik arah. Sebuah sentakan keras merenggut kesadaranmu turun menembus lorong gelap yang pengap, seolah tubuhmu diikat batu dan dilempar paksa ke dasar air yang tak bertepi."
        nar "Gema derit rem baja dan raungan klakson kereta ekspres masih memekakkan telinga batinmu ketika kau tersentak bangun dengan tarikan napas panjang yang memburu."
        nar "Kedua tanganmu refleks mencengkeram bagian tengah dadamu kuat-kuat. Otot-ototmu menegang hebat, bersiap menyambut rasa ngilu dari tulang rusuk yang remuk dihantam moncong lokomotif serta rembesan darah panas di atas batu rel."
        nar "Namun rasa sakit yang kauantisipasi itu tidak pernah datang. Tidak ada tulang yang patah, tidak ada bau amis besi dari darah yang tumpah, dan tidak ada dinginnya kerikil peron kereta bawah tanah di punggungmu."
        nar "Yang tersentuh oleh telapak tanganmu justru permukaan kain piyama katun yang halus dan kering, membungkus lekuk dada serta tulang rusuk yang terasa utuh, ringan, dan sama sekali bukan ukuran tubuhmu sendiri."
        nar "Dadanya naik-turun dengan irama napas yang pendek dan cepat. Dari lipatan selimut tebal yang menutup pinggangmu, menguar aroma sabun mandi berwangi bunga lembut yang bercampur samar dengan bau kayu pinus serta cat akrilik kering."
        nar "Saat kau menunduk dengan napas yang masih tersengal-sengal di kerongkongan, beberapa helai rambut panjang berwarna cokelat gelap merosot melewati bahumu, menyapu tulang selangka dan menggelitik kulit pipimu yang dingin oleh keringat."
        nar "Kau mengerjap keras berkali-kali, memaksa mata yang terasa perih oleh cahaya untuk mengenali ruang di sekelilingmu."
        nar "Sinar matahari pagi awal musim semi menembus tirai tipis berwarna gading di jendela sebelah kanan, membiaskan debu-debu halus yang melayang di atas lantai kayu dan karpet rajut bundar."
        nar "Kamar ini tertata rapi namun penuh dengan jejak kesibukan seseorang: sebuah meja rias kayu berdiri di sudut dekat lemari, bersebelahan dengan meja belajar lebar yang dipenuhi tabung kuas, deretan botol tinta gambar, kaleng pensil, serta papan sketsa kayu."
        nar "Setiap sudut ruangan ini berteriak bahwa tempat ini milik seorang gadis muda—dan kau sama sekali tidak pernah menginjakkan kaki di dalamnya seumur hidupmu."
    $ kk_bgm("system")
    play sound "audio/sfx/system_open.wav"
    nar "Belum sempat otakmu yang masih pening merangkai satu pun penjelasan masuk akal, bunyi derik statis seperti radio rusak tiba-tiba menyambar langsung di dalam rongga telingamu."
    nar "Udara kosong sekitar setengah meter di depan wajahmu bergetar dan berkedip dua kali. Tanpa proyektor maupun layar fisik, sebuah jendela kaca biru transparan membuka diri begitu saja di ruang pandangmu, menampilkan deretan teks dan emotikon garis cahaya neon yang menyunggingkan senyum miring."
    sistem "( ´ v ` )/ Bangun juga akhirnya~ Kukira jiwamu ikut penyok terlindas roda kereta tadi, Sampah Peron."
    nar "Suara itu tidak datang dari arah pintu maupun jendela, melainkan bergema langsung di balik tulang tengkorakmu—bernada rendah, ceria secara dibuat-buat, dan sarat dengan nada mengejek yang membuat darahmu mendidih seketika."
    nar "Kau refleks mengayunkan tangan kananmu ke depan untuk menepis panel cahaya itu jauh-jauh dari wajahmu."
    nar "Namun jemarimu hanya menembus bidang kaca biru itu seperti membelah kepulan asap dingin. Kau tersentak mundur hingga punggungmu menghantam sandaran kepala ranjang dengan mata melebar."
    if kk_host == "yutaka":
        yutaka "Suara apa itu—?! Siapa yang bicara di dalam kamarku?!"
        nar "Kalimat itu terputus di ujung lidahmu sendiri. Kau membeku selama satu detak jantung penuh, meraba pangkal tenggorokanmu yang bergetar."
        nar "Suara yang baru saja memantul di dinding beton kamar ini adalah suara bariton seorang pria muda—rendah, jernih, terdengar berwibawa secara alami meski sedang serak oleh kepanikanmu, namun jelas bukan warna suaramu sendiri."
        yutaka "Suaraku... tunggu, kenapa suaraku terdengar seperti orang lain?! Hei! Proyektor macam apa ini—keluar dan tunjukkan wajahmu!"
    else:
        chiasa "Suara apa itu—?! Siapa yang memasang layar ini di depanku?!"
        nar "Kalimat itu terputus di ujung lidahmu sendiri. Kau membeku selama satu detak jantung penuh, meraba pangkal tenggorokanmu yang terasa ramping dan asing."
        nar "Suara yang baru saja memantul di dinding kamar ini adalah suara seorang perempuan muda—jernih, ringan, sedikit bernada tinggi di ujung kalimat, namun tetap tajam oleh kepanikanmu."
        chiasa "Suaraku... tunggu, kenapa suaraku berubah seperti ini?! Hei! Jangan bersembunyi di balik layar konyol itu—keluar dan jelaskan apa yang kaulakukan padaku!"
    nar "Ikon emotikon di layar biru itu memutar kedua matanya dengan animasi patah-patah yang tampak sengaja dibuat untuk memancing emosi. Detik berikutnya, sengatan nyeri setajam jarum listrik bertegangan tinggi menusuk lurus ke balik pelipismu hingga kau terpekik dan mencengkeram kepala dengan kedua tangan."
    sistem "(¬_¬ ) Berisik sekali. Itu barusan bukti kecil supaya kau tidak membuang waktuku yang berharga dengan mengira ini cuma mimpi buruk atau efek obat bius di ruang gawat darurat."
    sistem "Tubuh lamamu sudah selesai jadi daging giling di atas rel stasiun, Manusia (´• v •`). Yang sedang kaupakai menghirup oksigen sekarang adalah tubuh pinjaman dariku—dan kesadaran pemilik aslinya sudah tidak ada lagi di dalam sana~"
    if kk_host == "yutaka":
        yutaka "Tubuh pinjaman...? Pemilik aslinya sudah tidak ada?! Kau pikir aku bakal menelan ocehan gila dari benda mencurigakan di kepalaku?!"
        nar "Denyut ngilu di pelipismu perlahan mereda, menyisakan napasmu yang memburu kasar di tengah keheningan apartemen yang terlalu luas itu."
        play sound "audio/sfx/phone_vibrate.wav"
        nar "Tepat saat kau menggeram kesal, ponsel pintar di atas nakas sebelah ranjang—tepat di samping sebuah jam tangan tipis bertali kulit yang tampak sering dipakai—bergetar panjang berulang-ulang, menyalakan layar panggilan masuk dengan nama kontak 'Koita' yang terus berkedip."
        nar "Sementara itu, beberapa langkah di seberang ranjang, tampak sebuah dompet kulit hitam di atas meja kaca ruang tamu serta pintu kamar mandi dalam yang sedikit terbuka, seolah menantangmu untuk membuktikan sendiri klaim suara tersebut."
    else:
        chiasa "Tubuh pinjaman...? Pemilik aslinya sudah tidak ada?! Kau pikir aku bakal menelan klaim sinting dari suara tak jelas di kepalaku?!"
        nar "Denyut ngilu di pelipismu perlahan mereda, menyisakan napasmu yang memburu kasar di sela gigi yang terkatup rapat."
        play sound "audio/sfx/ceramic.wav"
        nar "Tepat pada saat keheningan kamar itu kembali turun, dari lantai bawah rumah ini terdengar bunyi denting piring keramik yang beradu dengan permukaan meja, disusul desis air mendidih dari teko dan langkah kaki seseorang yang berjalan tenang di dapur."
        nar "Di dalam kamarmu sendiri, pantulan samar dari cermin meja rias di sudut ruangan, buku sketsa tebal yang terbuka di meja belajar, serta sebuah ponsel pintar yang terhubung ke kabel pengisi daya di atas nakas seolah menantangmu untuk membuktikan sendiri ucapan suara tersebut."
    sistem "(¬v¬) Tidak percaya? Silakan saja periksa sendiri kamar ini. Kau punya kaki, mata, dan barang-barang pemilik tubuh itu di dekatmu, kan? Cari tahu sendiri kau sedang menjadi siapa sekarang, sebelum kita bicara soal harga sewa nyawamu~ (^_~)-*"
    call kk_first_morning
    $ kk_bgm("system")
    nar "Tepat ketika kau masih berusaha menelan kenyataan gila tentang identitas barumu dan siapa saja orang yang tinggal di sekelilingmu, udara kosong di depan wajahmu kembali bergetar."
    play sound "audio/sfx/system_open.wav"
    nar "Jendela kaca biru itu meluncur turun untuk kedua kalinya, menampilkan emotikon garis yang membentuk gerakan tepuk tangan lambat yang sarat ejekan."
    sistem "(*^v^*)// Selamat atas pencerahannya, Manusia~ Ekspresi terkejutmu barusan benar-benar layak dijadikan pembuka pagi."
    if kk_host == "yutaka":
        yutaka "Kau... kau sengaja memasukkanku ke dalam manga sampah yang baru kubaca sebelum mati?! Sebagai Kisaragi Yutaka pula?! Apa maumu sebenarnya, brengsek?!"
    else:
        chiasa "Kau... kau sengaja memasukkanku ke dalam manga sampah yang baru kuhina sebelum mati?! Di tubuh Amamiya Chiasa pula?! Otakmu sudah miring, hah?!"
    sistem "( ´ w ` )/ Justru karena kau begitu membenci manga ini dari ujung rambut sampai ujung kaki, kau adalah kandidat paling cocok untukku. Panggil aku Sistem—dan mulai detik ini, kontrak sewa nyawamu resmi aktif."
    sistem "Aturan mainnya sangat sederhana: kau punya waktu tiga tahun penuh sampai Amamiya Koita lulus kuliah untuk menyimpangkan takdir romantisnya sejauh mungkin dari jalur asli manga ini."
    sistem "Evaluasinya hanya dilakukan satu kali, tepat pada hari ia naik ke panggung aula untuk menerima ijazah wisuda (´• v •`). Kalau sampai detik itu skenario romansa sang protagonis masih berjalan mulus... jantung pinjaman di dadamu itu akan kubuat berhenti berdetak di tempat~"
    if kk_host == "yutaka":
        yutaka "Jangan bercanda! Kenapa aku harus ikut campur mengurus urusan ranjang dan percintaan si protagonis naif itu pakai taruhan nyawa segala?!"
    else:
        chiasa "Jangan gila! Kenapa nyawaku harus digantungkan pada urusan cinta kakak tiri menyebalkan itu?!"
    nar "Layar biru transparan itu mendadak berkedip merah menyala selama sepersekian detik, memancarkan gelombang tekanan dingin yang membuat bulu kuduk di tengkukmu berdiri."
    sistem "(¬_¬ ) Karena hidup keduamu adalah milikku. Bagaimana caramu merusak takdirnya, siapa yang kaurangkul atau kauhancurkan, dan seperti apa wajah aslimu di balik topeng tubuh itu? Bukan urusanku menebaknya sekarang."
    sistem "Simpan keluhan moralmu, Manusia ( ´ v ` )~. Aku akan menilai siapa kau sebenarnya dari apa yang kaulakukan selama tiga tahun ini, bukan dari seberapa keras kau memakiku di kamar."
    return

# Draft editorial. Karakter/Event_Chiasa C01 dan Event_Yutaka Y01.
# ┌─ PANDUAN CERITA · Y01 · Terbangun di Apartemen Mewah  (dipakai bila host = Yutaka)
# │ LOKASI  : Apartemen Yutaka (prolog) · TERLIBAT: Kisaragi Yutaka (+ Koita bila relevan)
# │ AWALAN  : pagi 7 April; prolog — pemain baru sadar ada di tubuh host.
# │ INTI    : A periksa dompet & ponsel / B periksa cermin / C hubungi Koita / D tunggu notifikasi Sistem.
# │ AKHIRAN : membentuk kesan_awal; A memberi tahu saldo.
# ├─ PANDUAN CERITA · C01 · Terbangun di Kamar Chiasa   (dipakai bila host = Chiasa)
# │ LOKASI  : Rumah Amamiya (prolog) · TERLIBAT: Amamiya Chiasa (+ Koita bila relevan)
# │ AWALAN  : pagi 7 April; prolog.
# │ INTI    : A cek cermin & buku sketsa / B cek ponsel / C turun sarapan / D menunggu Sistem.
# │ AKHIRAN : kesan_awal; A mengungkap pita & ciri visual.
# └─ tulis / perbaiki dialog di bawah ──
label kk_first_morning:
    $ _opening = "Y01" if kk_host == "yutaka" else "C01"
    if kk_done(_opening):
        return
    $ kk_bgm(kk_host)
    if kk_host == "yutaka":
        $ _actions = ["Bongkar isi dompet dan ponselnya.", "Hampiri cermin kamar mandi untuk memastikan.", "Angkat telepon masuk dari Koita sekarang juga.", "Duduk membisu menuntut penjelasan."]
    else:
        $ _actions = ["Hampiri cermin dan periksa meja belajarnya.", "Bongkar isi ponsel di sebelah kasur.", "Nekat keluar kamar dan turun ke bawah.", "Duduk membisu menuntut penjelasan."]
    $ _rows = [(caption, Return(key), False) for key, caption in zip("ABCD", _actions)]
    call screen kk_choice_panel(_rows, "Di situasi gila ini, apa langkah pertamamu?")
    $ _opening_key = _return
    $ kk_record_choice(_opening, _opening_key)
    $ kk_flag("kesan_awal_" + _opening + "_" + _opening_key)
    if kk_host == "yutaka":
        if _opening_key == "A":
            $ _balance = "¥{:,}".format(saldo)
            nar "Kau menyibak selimut linen itu ke samping dan menurunkan kedua telapak kakimu ke atas lantai parket kayu yang dingin. Begitu kau bertumpu untuk berdiri tegak, titik berat tubuh ini terasa begitu ganjil."
            nar "Tungkai kakimu terasa jauh lebih panjang dengan jangkauan langkah yang lebar, sementara postur tubuhmu yang menjulang tinggi membuat sudut pandangmu terhadap perabotan kamar terasa berbeda dari biasanya."
            nar "Sambil menahan napas yang masih terasa berat di dada, kau memaksakan diri melangkah melewati karpet ruang tengah menuju meja kaca rendah, tempat sebuah dompet kulit hitam berdesain minimalis namun berkelas tergeletak berdampingan dengan sebuah ponsel pintar."
            nar "Jika suara kurang ajar di kepalamu tadi tidak berbohong soal tubuh pinjaman, maka kedua benda pribadi di atas meja itu adalah petunjuk paling nyata tentang siapa pemilik apartemen ini."
            nar "Kau menyambar dompet kulit tersebut dan membuka lipatannya. Di balik deretan kartu debit prioritas berlogo bank swasta besar dan lembaran uang tunai sepuluh ribu yen yang tersusun rapi tanpa lipatan, terselip selembar kartu tanda mahasiswa bertuliskan 'Universitas Kouseikan — Fakultas Ekonomi dan Bisnis'."
            yutaka "...Universitas Kouseikan? Tunggu dulu, kenapa nama kampusnya terdengar tidak asing di telingaku?"
            nar "Keningmu berkerut dalam. Kau menarik kartu mahasiswa itu keluar dari slot kulitnya, mengamati pasfoto seorang pemuda tampan berusia dua puluh tahun berambut hitam pekat dengan potongan two-block modern dan sorot mata abu-abu gelap yang tampak santai, lalu membaca nama yang tercetak tegas di sebelahnya: Kisaragi Yutaka."
            nar "Saat tanganmu yang lain meraih ponsel pintar di atas meja kaca, permukaan layarnya yang masih gelap memantulkan bayangan wajahmu sendiri—garis rahang tegas yang sama, potongan rambut hitam agak berantakan yang sama, dan sepasang mata abu-abu gelap yang persis dengan foto di kartu tersebut."
            nar "Potongan ingatan tentang halaman-halaman manga yang baru saja kaucibir di peron stasiun kereta bawah tanah tadi mendadak menyambung di kepalamu seperti kepingan teka-teki."
            yutaka "Ahhh...?! Tunggu—jangan bercanda! Wajah dan nama ini kan... Kisaragi Yutaka?! Sahabat kaya si protagonis di manga 'Kouseikan'?!"
            nar "Dengan napas tercekat di kerongkongan, kau menempelkan ibu jari tangan kananmu ke pemindai ponsel hingga kuncinya langsung terbuka tanpa hambatan."
            nar "Kau membuka aplikasi perbankan digital yang berada di halaman depan. Angka yang terpampang di layar membuat matamu terbelalak: saldo aktif yang bisa kaugunakan hari ini mencapai [_balance], lengkap dengan catatan transfer otomatis bulanan sebesar seratus lima puluh ribu yen dari rekening atas nama 'Kisaragi Kenji' tanpa sepatah pesan pribadi pun."
            nar "Jempolmu menggulir cepat ke aplikasi pesan singkat. Di urutan bawah, tampak ruang obrolan dengan 'Kisaragi Reiko' yang hanya berisi kalimat satu arah yang dingin dari bulan lalu tanpa sapaan seorang ibu: 'Transfer bulan ini sudah masuk. Jangan membuat masalah di kampus.'"
            nar "Di atasnya, ada obrolan grup empat sekawan masa kecil yang ramai membahas hari pertama semester baru, pesan dari teman sefakultas bernama Nakamura Daichi, serta ruang obrolan dengan Sakurajima Nagisa yang penuh keluhan gadis itu soal Koita."
            nar "Namun, ruang obrolan yang paling menyita perhatianmu berada di urutan teratas: 'Amamiya Chiasa'. Saat kau membukanya, di dalam kolom ketiknya masih tersimpan satu draf pesan yang diketik semalam oleh Yutaka asli tetapi tidak pernah berani dikirim—mengajak adik tiri Koita itu makan siang berdua setelah acara orientasi."
            nar "Kau menelan ludah menatap cahaya layar ponsel di tengah ruang tamu yang terlalu luas dan sunyi ini. Kau benar-benar terlempar ke dalam tubuh sang sahabat figuran yang kesepian—dan seluruh kekayaan di rekening ini sama sekali tidak memberimu ingatan tentang bagaimana cara menjadi pemuda yang mereka kenal."
        elif _opening_key == "B":
            nar "Kau menolak memercayai klaim gila bahwa tubuh aslimu sudah hancur di bawah roda kereta sebelum melihat buktinya dengan mata kepalamu sendiri."
            nar "Dengan langkah yang masih agak canggung karena ukuran tungkai yang terasa jauh lebih panjang dan tinggi, kau bangkit dari tepi kasur, melintasi lantai kayu kamar tidur, dan mendorong pintu kamar mandi dalam yang sedikit terbuka."
            nar "Jari-jarimu yang panjang meraba dinding marmer dingin di dekat kusen pintu lalu menekan sakelar. Lampu putih di atas cermin wastafel lebar langsung menyala terang, memantulkan sosok seorang pria muda dengan jelas."
            nar "Kau membeku di depan wastafel porselen itu."
            nar "Pria berusia sekitar dua puluh tahun di balik kaca tersebut memiliki postur tinggi ramping yang atletis di balik kaus tidur berwarna biru tua, bekas lipatan bantal tipis di pipi kirinya, dada yang naik-turun oleh napas yang memburu, serta sepasang mata abu-abu gelap yang melebar penuh ketegangan."
            nar "Saat kau mengangkat tangan kananmu yang gemetar untuk menyentuh dagu dan garis rahangmu sendiri, pemuda di dalam cermin itu melakukan gerakan yang persis sama pada detik yang sama."
            yutaka "Wajah orang lain... Aku benar-benar berada di dalam tubuh orang lain."
            nar "Suara bariton yang memantul di dinding keramik kamar mandi itu membuat tengkukmu semakin dingin. Kau mencondongkan tubuh lebih dekat ke permukaan cermin, mengamati potongan rambut hitam pekat bergaya two-block modern yang poninya jatuh agak berantakan di dahi, serta struktur wajahnya yang tampan dan terawat."
            nar "Semakin lama kau menatap pantulan mata abu-abu gelap itu, semakin kuat rasa ganjil yang menggelitik ingatanmu."
            yutaka "Tunggu sebentar... kenapa wajah ini kelihatan familier sekali? Aku yakin baru saja melihat proporsi wajah dan gaya rambut seperti ini..."
            nar "Ekor matamu melirik jaket almamater yang tergantung rapi di balik pintu kamar mandi dengan bordir nama 'Universitas Kouseikan — Kisaragi', lalu turun ke tepi meja wastafel tempat sebuah jam tangan tipis bertali kulit tergeletak, sebelum kembali menatap wajah di cermin."
            nar "Seketika, gambar-gambar dari layar ponselmu di peron stasiun kereta bawah tanah tadi menghantam ingatanmu dengan kejelasan yang mengerikan."
            yutaka "Ahhh!! Tunggu—wajah ini kan... Kisaragi Yutaka?!"
            nar "Kau mencengkeram pinggiran wastafel marmer itu kuat-kuat hingga buku-buku jarimu memutih. Tidak salah lagi: ini adalah Kisaragi Yutaka, sahabat masa kecil Amamiya Koita dari manga 'Kouseikan'!"
            nar "Dari seluruh orang di dunia komik yang baru saja kauhina itu, kau justru terlempar masuk ke tubuh si sahabat kaya yang selalu tampil santai dan jahil di permukaan, namun selalu berdiri setengah langkah di belakang sang protagonis sambil memendam cinta sendirian pada adik tiri Koita, Amamiya Chiasa!"
            nar "Di dalam cermin yang terang benderang itu, bulir keringat dingin yang merembes di pori-pori pelipis serta denyut pembuluh nadi di lehermu yang memburu kencang—hal-hal nyata yang tidak pernah digambar oleh pengarangnya di atas kertas—membuat kenyataan bahwa kau kini menghuni tubuhnya terasa begitu mencekam."
        elif _opening_key == "C":
            play sound "audio/sfx/phone_vibrate.wav"
            nar "Pandanganmu terpaku pada ponsel pintar di atas nakas sebelah ranjang yang masih terus bergetar panjang, bergeser tipis di atas permukaan kayu seiring dering getarannya."
            nar "Nama 'Koita' yang berkedip-kedip di layar panggilan masuk itu membuat dadamu terasa dingin—terlalu ganjil dan terlalu kebetulan jika dibandingkan dengan nama protagonis manga yang baru saja kaucibir habis-habisan di peron stasiun."
            nar "Dengan jantung yang berdegup kencang, kau menggeser tubuh ke tepi kasur dan menyambar ponsel itu dari kabel pengisi dayanya."
            nar "Sebelum jemarimu sempat menyentuh tombol jawab maupun tolak, bagian kaca layar di sekitar foto kontak memantulkan bayangan seorang pemuda asing berwajah tampan dengan rambut hitam pekat agak berantakan dan sepasang mata abu-abu gelap."
            nar "Pada saat yang sama, sensor pemindai wajah otomatis mengenali pemilik tubuh ini dan membuka bilah informasi profil di sudut atas layar kunci: 'Kisaragi Yutaka — Tahun Kedua, Universitas Kouseikan'."
            yutaka "Universitas Kouseikan...? Kisaragi Yutaka...? Tunggu dulu..."
            nar "Kau membandingkan pantulan wajahmu sendiri di permukaan kaca ponsel itu dengan nama yang tertera di layar, dan seketika darah di seluruh tubuhmu terasa berdesir hebat."
            yutaka "Ahhh...?! Jangan gila—wajah ini kan Kisaragi Yutaka?! Sahabat karib Amamiya Koita di manga 'Kouseikan' tadi?!"
            nar "Itu berarti orang yang saat ini sedang meneleponmu di seberang sana adalah sang protagonis utama, Amamiya Koita sendiri!"
            nar "Getaran panggilan masuk di telapak tanganmu hampir berhenti karena terlalu lama dibiarkan. Didorong kepanikan sekaligus dorongan untuk membuktikan apakah dunia ini benar-benar hidup atau sekadar ilusi, ibu jarimu refleks menggeser ikon hijau di layar untuk mengangkat panggilan tersebut."
            nar "Bahkan sebelum kau sempat menarik napas untuk menyiapkan sepatah alasan pun, suara seorang pemuda langsung terdengar jernih dari balik pengeras telinga."
            koita "Halo, Yutaka? Tumben lama sekali angkat teleponnya, kau baru bangun ya? Kita tetap jadi berangkat kuliah bareng dari depan stasiun pagi ini, kan?"
            nar "Suara itu terdengar begitu nyata—ramah, hangat, sedikit terburu-buru khas mahasiswa di pagi hari pertama semester, dan penuh keakraban seseorang yang sudah mengenal pemilik tubuh ini sejak kecil tanpa menaruh curiga sedikit pun."
            nar "Mendengar tokoh manga yang beberapa menit lalu hanya berupa balon teks dua dimensi kini berbicara langsung di telingamu membuat lidahmu mendadak kelu."
            yutaka "A-ah... soal itu, kepalaku agak pusing waktu bangun barusan. Kau berangkat duluan saja, nanti kukabari lagi kalau sudah di kampus ya, Koita."
            koita "Eh, kau nggak apa-apa? Tumben sekali kau mengeluh pusing pagi-pagi. Jangan dipaksa kalau memang belum enak badan, ya. Nanti absen kelas pagi biar kutanyakan ke anak-anak fakultasmu kalau berpapasan. Kabari aku kalau butuh sesuatu."
            nar "Sambungan telepon itu terputus dengan bunyi klik halus. Kau menurunkan ponsel dari telingamu perlahan-lahan dengan napas tertahan; bukan hanya dunia manga ini benar-benar nyata, tetapi Amamiya Koita juga memercayai setiap patah kata yang keluar dari mulut tubuh ini tanpa keraguan sedikit pun."
        else:
            nar "Kau meremas seprai linen kasur itu kuat-kuat hingga buku-buku jarimu memutih dan menolak beranjak satu langkah pun dari tempat tidur."
            nar "Enak saja suara sialan itu menyuruhmu jalan-jalan memeriksa kamar seperti pesuruh setelah menculik kesadaranmu ke tempat asing. Di atas nakas sebelahmu, getaran telepon masuk di layar ponsel akhirnya berhenti sendiri, menyisakan notifikasi panggilan tak terjawab yang meredup."
            nar "Namun tepat saat kau mendongak hendak memaki ruang kosong di depan ranjang lagi, tatapanmu tanpa sengaja menangkap pantulan dirimu sendiri di cermin pintu lemari pakaian besar yang berseberangan langsung dengan kasur."
            nar "Di dalam cermin itu, tampak seorang pemuda bertubuh tinggi ramping dengan rambut hitam pekat bergaya two-block yang agak berantakan dan sepasang mata abu-abu gelap yang menatap lurus ke arahmu—tepat di sebelah rak televisi yang memajang bingkai foto masa kecil empat sekawan di festival musim panas."
            nar "Kau menghentikan napas sejenak, menyipitkan mata memperhatikan pemuda di dalam cermin, lalu beralih menatap sosok anak laki-laki dan gadis kecil berpita hitam di dalam bingkai foto tersebut."
            yutaka "Tunggu dulu... potret empat anak di festival itu... jam tangan di nakas itu... dan wajah pria di cermin itu..."
            nar "Ingatan tentang bab-bab manga yang baru saja kaucibir habis-habisan di peron stasiun kereta bawah tanah berkelebat cepat di kepalamu."
            yutaka "Ahhh...?! Tunggu—jangan bercanda! Wajah ini kan Kisaragi Yutaka dari manga 'Kouseikan'?!"
            nar "Menyadari kau dilempar masuk ke dalam tubuh si sahabat kaya yang kesepian—figuran yang di sepanjang cerita hanya dijadikan tempat curhat sementara cintanya pada adik tiri sang protagonis tak pernah terbalas—membuat amarahmu langsung meledak ke arah ruang kosong di depan kasur."
            yutaka "Hei, keluar lagi kau! Kau pikir lucu memasukkanku ke tubuh figuran manga sampah ini?! Kembalikan aku ke tubuhku sekarang juga, pengecut!"
            nar "Udara kosong di depan wajahmu berkedip tajam. Emotikon garis di layar kaca biru itu melebarkan senyum miringnya, lalu detik berikutnya dengung frekuensi tinggi mendadak menghantam gendang telingamu, disusul rasa ngilu yang buas di belakang bola mata hingga kau terbungkuk di atas kasur sambil mencengkeram kening."
            yutaka "Argh—sialan! Hentikan!"
            sistem "(¬_¬\") Menuntut pelayanan sambil berteriak seolah kau pelanggan raja di restoran bintang lima? Nyalimu lumayan juga, Manusia, sayang sekali otakmu tertinggal di bawah roda kereta~"
            nar "Sengatan ngilu itu dicabut seketika, menyisakan napasmu yang terengah-engah di atas kasur dengan keringat dingin membasahi tengkuk dan pelipis."
            yutaka "Hah... hah... dasar psikopat sakit jiwa! Kau memungutku ke apartemen ini cuma buat dijadikan bahan tontonanmu?!"
            sistem "( ´ v ` )~ Aku lebih suka disebut sutradara yang murah hati. Mesin pendingin apartemen mewah ini masih menyala, saldo bankmu masih penuh, kota di balik jendela itu terus berjalan, dan kau masih hidup. Jadi berhentilah merengek sebelum kutambah dosis perkenalannya, ya~"
    else:
        if _opening_key == "A":
            nar "Kau menyibak selimut hangat itu ke samping dan menurunkan kedua telapak kakimu ke atas karpet rajut di samping ranjang. Serat benangnya terasa lembut di bawah kulit telapak kaki yang mungil, namun begitu kau bertumpu untuk berdiri tegak, tubuhmu langsung oleng setengah langkah."
            nar "Kau buru-buru menahan pinggiran kasur dengan telapak tangan. Titik berat tubuh ini terasa ganjil—jauh lebih pendek, lebih ringan, dengan tulang bahu yang sempit dan lekuk pinggang yang membuat setiap ayunan langkah terasa asing."
            nar "Setiap kali kau bergerak, massa rambut panjang di punggungmu ikut bergeser lembut menyapu kain piyama di sekitar belikat."
            nar "Sambil menahan napas yang masih terasa dingin di pangkal tenggorokan, kau melangkah pelan menghampiri meja rias kayu di sudut kamar, lalu berhenti tepat di hadapan cermin lonjongnya."
            nar "Kau terpaku menatap sosok di balik kaca itu."
            nar "Seorang gadis muda berusia sekitar sembilan belas tahun sedang menatapmu balik dengan wajah oval yang pucat dan sepasang mata kuning keemasan yang melebar kaku."
            nar "Bulu matanya lentik, membingkai iris keemasan yang tampak berkilau tertimpa sinar matahari pagi. Rambutnya yang berwarna cokelat gelap jatuh sepunggung dalam potongan berlapis yang sedikit bergelombang di ujungnya, dengan poni menyamping yang menyapu kening dan separuh rambut bagian atas yang terikat rapi menggunakan pita hitam."
            nar "Saat kau mengangkat tangan untuk meraba pipimu sendiri, gadis di dalam cermin itu melakukan gerakan yang persis sama pada detik yang sama."
            chiasa "...Siapa gadis ini? Wajah ini... mata kuning keemasan... rambut cokelat gelap dengan pita hitam..."
            nar "Suara jernih yang meluncur dari bibirmu sendiri membuat tengkukmu merinding. Ketika kau menghela napas gugup dan mencoba menenangkan debar jantungmu, tangan kananmu mendadak bergerak sendiri tanpa perintah otakmu."
            nar "Jari-jari lentik itu terangkat ke belakang kepala, meraba simpul pita hitam di rambutmu untuk memastikan ikatannya masih kencang, lalu turun menyentuh anting mungil di daun telinga dan rantai kalung tipis yang melingkar di lekuk tulang selangka."
            nar "Gerakan refleks itu begitu luwes dan terbiasa—sebuah kebiasaan bawah sadar pemilik tubuh ini ketika sedang gugup. Dan tepat pada detik jemarimu menyentuh simpul pita hitam itu, ingatan tentang ilustrasi sampul berwarna yang baru saja kaulihat di layar ponselmu sebelum tewas di peron stasiun menghantam kepalamu seperti palu."
            chiasa "Ahhh!! Tunggu—jangan bercanda! Wajah dan pita hitam ini kan... Amamiya Chiasa?!"
            nar "Kau refleks membekap mulutmu sendiri dengan kedua telapak tangan, mundur setengah langkah dari meja rias hingga betismu menyentuh kursi kayu."
            nar "Tidak salah lagi. Proporsi wajah ini, sorot mata keemasan yang biasanya digambar menyipit jahil itu, hingga pita hitam khas di rambutnya—semuanya adalah ciri visual Amamiya Chiasa dari manga romansa kampus 'Kouseikan' yang baru saja kaumaki habis-habisan beberapa menit sebelum tertabrak kereta!"
            nar "Dari sekian banyak orang di dunia fiksi itu, kau justru dilempar masuk ke dalam tubuh si adik tiri tanpa hubungan darah yang tinggal satu atap dengan sang protagonis, Amamiya Koita, dan diam-diam memendam obsesi romantis pada kakak tirinya sendiri!"
            nar "Dengan dada yang masih bergemuruh, pandanganmu beralih cepat ke meja belajar lebar tepat di sebelah meja rias."
            nar "Di atas permukaan kayu yang bersih dari debu itu, tergeletak jadwal orientasi mahasiswa baru bertuliskan 'Universitas Kouseikan — Fakultas Seni Rupa dan Desain', bersebelahan dengan deretan pena gambar teknik, penghapus uli, serta sebuah buku sketsa tebal bersampul hitam yang sedang terbuka."
            nar "Kau melangkah mendekat dan menunduk menatap halaman buku sketsa tersebut. Di atas kertas bertekstur halus itu, terpampang gambar rancangan anatomi dan ilustrasi karakter novel ringan yang luar biasa hidup—garis-garisnya bersih, tegas, penuh percaya diri, dengan arsiran bayangan yang halus dan tanda tangan pena mungil bertuliskan 'Shena' di sudut kanan bawah."
            nar "Di samping buku sketsa itu, terselip pula selembar contoh sampul cetakan novel ringan strategi populer yang mencantumkan nama ilustrator yang sama."
            nar "Kau menatap bekas kapalan tipis di ruas jari tengah tangan kananmu, lalu teringat bagaimana tangan ini tadi bergerak sendiri merapikan pita rambut."
            chiasa "Tunggu dulu... kalau refleks otot tubuhnya masih tertinggal di tanganku... jangan-jangan keahlian menggambarnya sebagai 'Shena' juga masih bisa kupakai?"
            nar "Didorong secercah harapan untuk menemukan pegangan di tubuh asing ini, kau menarik kursi meja belajar, duduk tergesa-gesa, dan memungut sebatang pensil mekanik logam dari samping buku sketsa."
            nar "Begitu batang pensil itu menyentuh telapak tanganmu, jemari lentik Chiasa secara otomatis mengapitnya pada sudut dan lekukan ruas jari yang paling ideal."
            nar "Napasmu tertahan. Kau menempelkan ujung timah grafit itu ke sudut halaman kosong di sebelah sketsa karakter tadi, lalu mencoba menarik satu garis lengkung sederhana untuk meniru lekuk rahang yang ada di sebelahnya."
            nar "Goresan yang muncul di atas kertas justru miring, gemetar, dan kaku seperti coretan anak sekolah dasar yang memegang pensil dengan tangan kiri."
            chiasa "Eh...? Kok begini? Tunggu, sekali lagi—"
            nar "Kau menggigit bibir bawahmu, menekan batang pensil itu lebih keras untuk memaksa pergelangan tanganmu menurut, lalu menggoreskan garis kedua dan ketiga dengan terburu-buru."
            nar "Krak."
            nar "Ujung grafit tipis itu patah berkeping-keping di atas kertas, meninggalkan noda serbuk hitam yang kotor dan garis patah yang menyedihkan tepat di sebelah ilustrasi indah peninggalan Chiasa asli."
            nar "Pensil mekanik itu terlepas dari jemarimu dan menggelinding pelan di atas meja kayu. Kau menatap telapak tanganmu yang gemetar dengan keringat dingin merembes di punggung."
            nar "Otot-otot tubuh ini memang masih mengingat cara mengapit pensil dan merapikan pita rambut. Namun mata, kepekaan ruang, dan bakat melukis bertahun-tahun yang membuat nama 'Shena' dikagumi orang-orang telah lenyap tanpa sisa bersama jiwa pemilik aslinya."
        elif _opening_key == "B":
            nar "Kau menggeser tubuhmu yang terasa ringan dan asing itu ke tepi kasur, lalu menjulurkan tangan meraih ponsel pintar bersarung krem-hitam yang sedang terhubung ke kabel pengisi daya di atas nakas kayu."
            nar "Jika suara kurang ajar di kepalamu tadi tidak berbohong tentang tubuh pinjaman, maka benda pribadi yang paling sering disentuh pemilik kamar ini pasti menyimpan seluruh identitasnya."
            nar "Kau mencabut kabel pengisi dayanya dengan jari yang sedikit gemetar. Saat kau mengangkat ponsel itu ke depan wajahmu, permukaan kaca layarnya yang masih gelap memantulkan bayangan sepasang mata kuning keemasan yang bulat melebar, poni menyamping, serta rambut cokelat gelap yang diikat pita hitam."
            nar "Detik berikutnya, layar ponsel menyala otomatis. Ikon gembok kecil di bagian atas layar langsung terbuka hanya dengan memindai wajah yang sedang kaupakai—sama sekali tidak memberimu kesempatan untuk terhalang oleh kata sandi."
            nar "Kau mengerjap pelan menatap halaman utama yang tertata rapi dengan folder-folder kuliah dan aplikasi gambar. Di bilah pengingat paling atas, terpampang kartu identitas digital mahasiswa baru: 'Amamiya Chiasa — Tahun Pertama, Fakultas Seni Rupa dan Desain, Universitas Kouseikan'."
            chiasa "Universitas Kouseikan...? Amamiya Chiasa...? Tunggu sebentar, marga Amamiya dengan mata keemasan dan pita hitam di jurusan Seni Rupa..."
            nar "Napasmu tercekat di kerongkongan. Potongan adegan dan sampul manga yang baru saja kaucibir habis-habisan di peron stasiun kereta bawah tanah tadi langsung menyambar ingatanmu."
            chiasa "Ahhh...?! Jangan gila—wajah ini kan Amamiya Chiasa?! Adik tiri si protagonis di manga 'Kouseikan'?!"
            nar "Jantungmu berdegup kencang menghantam rongga dada yang sempit ini. Kau benar-benar dilempar masuk ke dalam manga harem yang paling kaubenci, dan parahnya lagi, kau menghuni tubuh adik tiri tanpa hubungan darah yang tinggal serumah dengan Amamiya Koita!"
            nar "Dengan ujung jari yang terasa dingin, kau membuka aplikasi di dalam ponsel itu satu per satu untuk memeriksa seberapa dalam hidup gadis ini harus kautanggung."
            nar "Aplikasi perbankan digital menampilkan saldo akhir sebesar empat ratus ribu yen—gabungan dari kiriman uang saku bulanan lima puluh ribu yen dari ayahnya, Amamiya Daisuke, serta transfer royalti pasif lima puluh ribu yen per bulan dari penerbit novel ringan atas nama pena 'Shena'."
            nar "Kau beralih membuka aplikasi surel. Pesan terbaru di kotak masuk berasal dari seorang editor bernama Higashiyama Mio yang menyapamu dengan sebutan 'Shena-sensei', mengucapkan selamat masuk kuliah, dan memastikan bahwa royalti cetakan ulang tetap berjalan tanpa kewajiban proyek ilustrasi baru untuk saat ini, meski ia berharap bisa segera mendiskusikan sampul jilid berikutnya."
            nar "Ketika kau berpindah ke aplikasi pesan singkat, deretan notifikasi langsung menyambut matamu. Di urutan bawah, ada pesan semalam dari ibu tirinya, Amamiya Yoshie, yang menanyakan kabar dari luar kota dan mengingatkan dengan nada lembut agar Chiasa serta Koita menghabiskan lauk di kotak plastik biru dan tidak hanya makan roti tawar."
            nar "Di atasnya, ada belasan pesan beruntun penuh tanda seru dari kontak teman sejurusan bernama 'Ishikawa Haruka' yang meributkan jadwal studio minggu pertama sekaligus memuja-muja goresan ilustrasi terbaru 'Shena-sensei'—tanpa sedikit pun menyadari bahwa gadis yang dikiriminya pesan adalah sang ilustrator itu sendiri."
            nar "Namun, ruang obrolan yang disematkan paling atas dengan tanda bintang khusus hanyalah satu nama kontak: 'Ko-nii'."
            nar "Ibu jarimu menyentuh ruang obrolan itu dengan ragu. Begitu terbuka, ratusan gelembung pesan dari minggu-minggu sebelumnya langsung memenuhi layar—penuh dengan sapaan manja berakhiran tanda gelombang, keluhan pura-pura minta dijemput di depan stasiun, godaan setengah serius yang menanyakan Koita sedang bersama gadis mana, hingga foto sketsa tangan Koita yang dikirim lewat tengah malam."
            nar "Setiap baris kalimat yang diketik Chiasa asli begitu intim, posesif, dan sarat dengan pengakuan cinta terselubung yang dibungkus candaan adik perempuan, hingga membacanya saja membuat bulu kudukmu meremang seperti sedang membongkar buku harian terlarang milik orang lain."
            nar "Ibu jarimu menggantung kaku di atas papan ketik layar. Bagaimana mungkin kau bisa meniru cara bicara semanja dan seakrab ini kepada pria yang bahkan belum pernah kautemui secara langsung?!"
            koita "Chiasa? Kau sudah bangun, kan? Sarapannya sebentar lagi dingin, lho!"
            nar "Seruan suara laki-laki yang hangat dan akrab dari lantai bawah rumah itu mendadak menembus pintu kamar, membuat kedua bahumu tersentak keras hingga ponsel di tanganmu nyaris terlepas."
            nar "Kau menoleh panik ke arah pintu kamar yang tertutup, lalu kembali melirik tulisan 'Ko-nii' yang terpampang di puncak layar ponselmu. Selama sepersekian detik, mulutmu membuka untuk membalas panggilan itu sesuai nama di layar—tetapi lidahmu mendadak kelu dan menolak mengeluarkan sebutan manja tersebut."
            nar "Kau menelan ludah dengan kerongkongan kering, lalu buru-buru mengunci layar ponsel dan menyahut sekenanya tanpa sanggup menyematkan panggilan kakak itu di ujung kalimatmu."
            chiasa "I-iya! Aku sudah bangun... sebentar lagi aku turun!"
            nar "Suaramu terdengar sedikit tercekat di kalimat terakhir. Dari lantai bawah tidak ada kecurigaan yang langsung membalas, hanya bunyi langkah kaki yang kembali bergerak di dapur—namun kau tahu persis bahwa begitu kau membuka pintu kamar itu dan duduk di meja makan nanti, kau tidak bisa lagi menghindar dari keharusan memanggilnya secara langsung."
        elif _opening_key == "C":
            nar "Daripada terus terkurung di dalam kamar asing bersama suara sinting yang berbisik di dalam tengkorakmu, kau menyibak selimut dengan gerakan cepat dan melangkah menuju pintu kamar untuk memeriksa langsung siapa yang sedang beraktivitas di lantai bawah."
            nar "Namun tepat ketika jemarimu baru saja menyentuh kenop pintu kayu, langkahmu mendadak terhenti di depan cermin panjang yang menempel di dinding samping lemari pakaian."
            nar "Dari balik permukaan kaca itu, seorang gadis bertubuh mungil dan ramping menatapmu balik dengan wajah oval yang pucat, sepasang mata kuning keemasan yang melebar kaku, serta rambut cokelat gelap sepunggung yang separuh bagian atasnya terikat rapi menggunakan pita hitam."
            chiasa "Tunggu dulu... wajah gadis ini... kenapa rasanya aku baru saja melihatnya beberapa menit lalu?"
            nar "Saat kau menahan napas karena gugup, jari-jari tangan kananmu tanpa sadar terangkat menyentuh simpul pita hitam di belakang kepala dan anting mungil di daun telingamu—sementara ekor matamu menangkap papan nama kayu kecil bergambar kuas lukis di pintu kamar yang bertuliskan 'Chiasa'."
            nar "Potongan ciri visual itu langsung menyambung dengan halaman manga yang baru saja kaucibir di peron stasiun kereta bawah tanah sebelum kematianmu."
            chiasa "Ahhh!! Tunggu—jangan bercanda! Wajah ini kan... Amamiya Chiasa?! Adik tiri dari manga 'Kouseikan' yang baru kubaca di stasiun tadi?!"
            nar "Kau membekap mulutmu sendiri dengan telapak tangan yang dingin. Dari seluruh tokoh yang ada di cerita romansa kampus itu, kau justru terlempar masuk ke tubuh si adik tiri tanpa hubungan darah yang tinggal satu atap dengan sang protagonis utama!"
            nar "Belum sempat keterkejutan di dadamu mereda, aroma kaldu sup miso hangat, roti panggang, dan telur goreng dari lantai bawah menarik langkahmu keluar dari kamar."
            nar "Anehnya, begitu telapak kakimu menapak di deretan tangga kayu menuju lantai satu, otot-otot tungkai tubuh ini melangkah turun dengan sangat hafal—bahkan secara otomatis melangkahi anak tangga kelima yang kayunya agak berderit tanpa perlu kauperhatikan."
            nar "Begitu kau tiba di ambang ruang makan lantai bawah yang terang oleh sinar matahari pagi, tampak sebuah kotak plastik biru berisi lauk kiriman dari Amamiya Yoshie tergeletak di atas meja kayu."
            nar "Dan tepat di seberang meja itu, Amamiya Koita berdiri mengenakan celemek di atas kaus rumahnya, sedang meletakkan piring sarapan sambil mengangkat wajah dan menyunggingkan senyum ramah tanpa pertahanan."
            koita "Pagi, Chi-chan. Cepat duduk, makan selagi hangat sebelum dingin. Tumben sekali kau sudah turun sebelum kupanggil dua kali."
            nar "Kau terpaku di ambang pintu ruang makan. Wajah ramah dengan potongan rambut hitam agak berantakan yang tadi hanya berupa gambar dua dimensi yang membuatmu muak di layar ponsel, kini berdiri nyata, bernapas, dan menatapmu dengan akrab dari jarak beberapa langkah."
            nar "Kau tahu dari halaman manga bahwa Chiasa asli selalu menyapanya dengan panggilan manja 'Ko-nii'. Namun di hadapan orangnya langsung, lidahmu mendadak tercekat menolak mengeluarkan sebutan itu."
            chiasa "P-pagi... aku cuma kebetulan bangun lebih awal. A-aku mau cuci muka sebentar sebelum duduk."
            koita "Haha, gugup karena hari pertama kuliah di Seni Rupa, ya? Jangan lama-lama, nanti telur mata sapinya keburu dingin."
            nar "Koita berbalik kembali ke arah kompor tanpa sedikit pun curiga pada caramu berdiri kaku di ambang ruangan. Menjadi Chiasa di rumah ini berarti harus duduk berhadapan setiap hari dengan pria yang merasa paling mengenalmu—sementara salah bicara sedikit saja di meja makan nanti bisa langsung membongkar semuanya."
        else:
            nar "Kau duduk membeku di tepi ranjang, mencengkeram ujung selimut kuat-kuat hingga buku-buku jarimu yang lentik memutih, dan menolak beranjak satu langkah pun."
            nar "Enak saja suara kurang ajar itu menyuruhmu berkeliling memeriksa kamar seperti pesuruh setelah menculik kesadaranmu ke tempat asing. Sebelum kau sudi menggerakkan satu jari pun, entitas yang menyeretmu ke sini harus memberikan jawaban."
            nar "Namun saat kau memutar pandangan dengan kesal ke sekeliling kamar untuk mencari celah, matamu tanpa sengaja menangkap pantulan dirimu sendiri di cermin meja rias yang berseberangan langsung dengan kasur."
            nar "Di samping cermin itu, tampak jadwal kuliah tahun pertama Fakultas Seni Rupa dan Desain, buku sketsa tebal yang terbuka dengan tanda tangan pena 'Shena', serta nampan kayu kecil berisi pita hitam cadangan."
            nar "Kau menghentikan napas sejenak, menyipitkan mata menatap gadis berwajah oval dengan mata kuning keemasan dan rambut cokelat gelap half-up berpita hitam di balik kaca cermin tersebut."
            chiasa "Tunggu sebentar... mahasiswi tahun pertama Seni Rupa... pita hitam... mata keemasan... dan wajah itu..."
            nar "Ingatan tentang bab-bab manga yang baru saja kaucibir habis-habisan di peron stasiun kereta bawah tanah langsung menyambar kepalamu."
            chiasa "Ahhh...?! Jangan bercanda—wajah ini kan Amamiya Chiasa dari manga 'Kouseikan'?!"
            nar "Menyadari kau dilempar masuk ke dalam tubuh si adik tiri posesif tanpa hubungan darah di cerita harem yang paling kaubenci membuat amarahmu langsung meledak ke arah ruang kosong di depan kasur."
            chiasa "Hei, keluar lagi kau! Kau pikir lucu memasukkanku ke tubuh karakter manga sampah ini?! Kembalikan aku ke tubuhku sekarang juga, pengecut!"
            nar "Udara di depan wajahmu berkedip tajam. Emotikon garis di layar kaca biru itu melebarkan senyum miringnya, lalu detik berikutnya sengatan ngilu yang jauh lebih brutal menghantam pangkal lehermu hingga kau terbungkuk di atas kasur sambil memekik tertahan."
            chiasa "Akh—! Sialan, hentikan!"
            sistem "(¬_¬\") Berteriak menuntut ganti rugi seolah kau sedang memarahi kasir toko? Menggemaskan sekali, Manusia. Sayangnya kau bukan pelanggan di sini—kau cuma rongsokan peron yang kupungut~"
            nar "Sengatan listrik itu dicabut seketika, menyisakan napasmu yang terengah-engah di atas seprai dan keringat dingin yang membasahi pelipis, sementara dari lantai bawah terdengar bunyi piring beradu dan langkah kaki yang tenang di dapur."
            chiasa "Hah... hah... dasar psikopat sakit jiwa! Kau memaksaku masuk ke tubuh gadis ini cuma buat bahan tontonanmu?!"
            sistem "( ´ v ` )~ Anggap saja aku penonton setia yang bosan melihat alur cerita yang lurus. Pemilik asli kamar ini sudah tidak ada, dan kakak kesayangannya sedang menyiapkan sarapan di bawah—jadi simpan tenagamu untuk berakting, ya~"
    return

label kk_main:
    # M01 — Hari Pertama + Hanami. Dunia dibuka; pemain menemukan N01/Mi01 sendiri
    # dengan berjalan ke lokasinya (Gedung Arsitektur, Taman Kampus) — tidak dipaksa.
    $ kk_bulan = 1
    $ kk_slot = 1
    show screen kk_set("koita", "Kampus Kouseikan · Hari Pertama")
    with fade
    nar "Hari pertama semester musim semi di Universitas Kouseikan dibuka dengan guguran kelopak sakura di sepanjang gerbang utama. Di sudut kantin yang ramai, teman-teman Koita sudah mengelilingi mejanya seperti adegan pembuka yang kaukenal."
    nar "Inilah dunia manga yang harus kaubelokkan demi bertahan hidup. Ke mana kau pergi hari ini, dan kapan kau mulai bergerak, sepenuhnya adalah milikmu."
    jump kk_world_loop

label kk_explore_loop:
    if not (config.developer and kk_debug_tools):
        return
    call screen kk_explorer
    if _return == "back":
        return
    call kk_event(_return)
    jump kk_explore_loop

# Pemutar event generik dari data autogenerated.
# reveal=True (Alat Uji/Explorer): tampilkan ringkasan efek mekanik untuk pengujian.
# reveal=False (ditemukan lewat navigasi dunia): akibat HANYA terasa lewat perilaku
# NPC/Status nanti — tidak diucapkan di sini (konsisten dgn arahan: jangan ungkap
# hasil pilihan sebelum konsekuensinya benar-benar terjadi).
label kk_event(evid, reveal=True):
    $ ev = KK_EV_BY_ID.get(evid)
    if ev is None:
        nar "(Event [evid] belum ada datanya.)"
        return
    $ kk_bgm_event(evid)
    $ _char = _char_of(ev["id"])
    show screen kk_set(_char, ev["month"] + " · " + ev["title"])
    with Dissolve(0.4)
    if reveal:
        nar "{size=20}{color=#8d877f}[ev['id']] · [ev['month']]{/color}{/size}\n[ev['title']]"
    else:
        nar "[ev['title']]"
    if ev["trigger"]:
        nar "[ev['trigger']]"
    if ev["choices"]:
        call screen kk_choices(ev)
        $ key = _return
        $ _new_choice = kk_record_choice(ev["id"], key)
        $ _fk = ev["id"] + "-" + key
        if _new_choice and _fk in KK_FORCE_CHOICES:
            call kk_force(KK_FORCE_CHOICES[_fk])
        if reveal and ev["effect"]:
            nar "{color=#8d877f}→ Efek (ringkas): [ev['effect']]{/color}"
    else:
        if reveal:
            nar "{color=#8d877f}(Resolusi event ini ditentukan oleh flag terkumpul — menuju ending.){/color}"
    return

# Force: non-operasional. Adegan TIDAK ditampilkan (lihat docs/09 §2).
label kk_force(victim):
    stop music fadeout 0.5
    scene black with Dissolve(0.7)
    call screen kk_titlecard("…")
    $ kk_bgm("aftermath")
    $ kk_force_consequences(victim)
    sistem "Tercatat."
    nar "Adegan dilewati. Yang ditampilkan: akibat pada korban. Lapor atau diam ditentukan wataknya; konsekuensi hukum, sosial, akademik, dan psikologis berjalan terpisah."
    nar "{color=#8d877f}(Tidak ada romansa dengan pelaku. Jalur ini punya harga.){/color}"
    return

label kk_evaluasi:
    scene black with fade
    show screen kk_set("koita", "Wisuda")
    with dissolve
    nar "Tiga tahun telah berlalu. Di atas panggung aula kelulusan Universitas Kouseikan, Amamiya Koita maju menerima ijazahnya. Detik itu juga, kontrakmu jatuh tempo."
    play sound "audio/sfx/system_open.wav"
    sistem "Mari kita hitung. Apa yang sudah kau ubah dari takdirnya?"
    $ _slides = kk_epilogue()
    $ _slide = 0
    while _slide < len(_slides):
        call kk_show_ending(_slides[_slide])
        $ _slide += 1
    return

label kk_show_ending(code):
    $ _e = kk_ending_data(code)
    $ kk_bgm_ending(_e["type"])
    if code == "E-NA-07":
        if kk_has("haruto_sekutu"):
            $ _e = dict(_e, body="Haruto menelepon lagi. Kali ini yang terdengar lebih dulu justru suara Nagisa dari dapur. Ia sudah pulang. Besok kakaknya akan menemani sesi terapi pertamanya. Untuk urusan kampus, mereka punya waktu membicarakannya nanti.")
        else:
            $ _e = dict(_e, body="Di meja makan keluarga Sakurajima ada tempat untuk Nagisa lagi. Sepulang dari sesi terapi, ia duduk di sana dengan sketsa setengah jadi. Ibunya menggeser teko agar kertas itu bisa dibentangkan.")
    elif code == "E-MI-02":
        $ _e = dict(_e, body="Miyuki menaruh kursi kecil di dekat mejanya. Ketika orang tua pasien mulai menjawab, ia menunggu sebentar. Anak di kursi itu punya pertanyaannya sendiri. Miyuki meletakkan penanya dan mendengarkan.")
    elif code == "E-SH-13":
        $ _e = dict(_e, body="Di pameran dulu, Shiori bertanya sebagai pembaca. Kini Mio menerima pertanyaan yang sama, bersama salinan jawabanmu. Kali berikutnya kalian duduk membahas sampul, buku itu masih tertutup. Yang ingin Mio dengar lebih dulu adalah ceritamu tentang Shena.")
    elif code == "E-SH-07":
        $ _e = dict(_e, body="Shiori menutup map bertuliskan nama Tojo. Pertunangan itu sudah ia batalkan sendiri. Map berikutnya berisi rencana kerjanya. Kali ini, ketika ayahnya bertanya dari mana mereka harus mulai, Shiori membukanya di halaman yang ia pilih.")
    elif code == "E-CF-01":
        $ _e = dict(_e, body="Kunci rumah baru itu ada dua. Saat kalian pulang membawa dus terakhir, kau mendengar ia bertanya dari dapur di mana cangkir-cangkir disimpan. Kau belum tahu. Kalian membuka dus satu demi satu, bersama-sama.")
    scene black with fade
    call screen kk_ending_card(_e)
    return
