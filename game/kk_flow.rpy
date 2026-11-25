# Kouseikan — alur. Prolog, vertical slice, pemutar event generik, Force (abstrak), evaluasi.
# Prototipe: teks hanya poin utama (awal → pilihan → akibat ringkas). Story penuh menyusul.

label kk_intro:
    scene black with fade
    call screen kk_titlecard("KOUSEIKAN", "18+ · semua tokoh dewasa")
    $ kk_bgm("platform", level=0.56)
    play story_crowd "audio/sfx/platform_crowd.wav" fadein 0.6
    nar "Peron stasiun kereta bawah tanah sore itu pengap oleh udara lembap dan desakan orang-orang yang baru pulang kerja. Di tengah kebisingan itu, perhatianmu justru terpaku sepenuhnya pada layar ponsel di genggamanmu."
    nar "Di layar itu terpampang bab terbaru 'Kouseikan', sebuah manga romansa kampus yang entah bagaimana selalu bertengger di peringkat teratas aplikasi bacaan mingguan."
    nar "Kamu mendengus sinis sambil menggeser layar dengan ibu jari. Semakin jauh kamu membacanya, semakin gatal rasanya ingin memaki di kolom komentar."
    nar "Bagaimana mungkin cerita sampah semacam ini bisa begitu populer? Sejak bab pertama, alurnya jelas-jelas hanya angan-angan murahan penulisnya yang dituangkan tanpa tahu malu."
    nar "Tokoh utamanya, Amamiya Koita, hanyalah mahasiswa sastra biasa yang modalnya cuma senyum ramah dan jawaban menggantung. Ia tidak pernah tegas menolak siapa pun dengan dalih 'tidak tega menyakiti', tetapi seluruh isi cerita memujanya seolah ia pria paling tulus di muka bumi."
    nar "Lebih parahnya lagi, gadis-gadis cantik di sekelilingnya dibuat jatuh cinta hanya karena kebaikan sepele, sementara keluarga, sahabat, dan orang-orang di sekitarnya direduksi menjadi figuran bodoh yang rela mengorbankan perasaan mereka demi kebahagiaan sang MC."
    $ kk_bgm("tension", fade=0.3, level=0.46)
    play story_crowd "audio/sfx/platform_panic.wav" fadeout 0.2
    nar "Ibu jarimu baru saja mengetik sepatah kalimat pedas di kolom ulasan ketika tiba-tiba jeritan melengking memecah keramaian peron."
    nar "Kamu menoleh spontan dari layar ponsel. Beberapa langkah di sebelahmu, seorang anak kecil terlepas dari genggaman ibunya, terpeleset melewati garis batas kuning, dan jatuh tersungkur ke atas batu-batu rel."
    play story_rail "audio/sfx/train_rail.wav" fadein 0.8
    play story_train "audio/sfx/train_horn.wav"
    nar "Di ujung terowongan yang gelap, dua sorot lampu kereta ekspres sudah menyala menyilaukan. Klakson panjang meraung memekakkan telinga, disusul gemuruh roda besi yang membelah rel dengan kecepatan penuh."
    play sound "audio/sfx/phone_drop.wav"
    nar "Orang-orang di peron hanya menjerit kaku sambil menutup mulut, tidak ada satu pun yang berani bergerak maju. Kepanikan menyergap dadamu lebih cepat daripada perhitungan akal sehat; ponselmu terlepas jatuh ke lantai saat kakimu refleks melompat turun ke atas rel."
    nar "Kamu merengkuh tubuh mungil yang gemetar itu dan mengangkatnya sekuat tenaga ke atas bibir peron, tepat saat beberapa tangan penumpang lain menarik kerah baju anak itu hingga selamat."
    play story_train "audio/sfx/train_brake.wav"
    nar "Anak itu lolos. Tepat ketika kamu bertumpu pada kedua tangan hendak memanjat naik, cahaya putih lampu kereta sudah menelan seluruh pandanganmu, diiringi derit rem darurat yang merobek gendang telinga."
    play sound "audio/sfx/train_impact.wav"
    stop story_train fadeout 0.15
    stop story_crowd fadeout 0.18
    stop story_rail fadeout 0.4
    nar "Hantaman baja yang masif meremukkan tulang rusukmu dalam sekejap. Tubuhmu terlempar ringan seperti boneka kain sebelum dingin yang pekat menyergap."
    nar "Pada detik terakhir sebelum kesadaranmu benar-benar padam, yang melintas di kepalamu hanyalah cibiran getir yang tidak bisa ditahan."
    nar "Bisa-bisanya kamu mati tertabrak kereta gara-gara menyelamatkan anak kecil, persis pembuka cerita fiksi pasaran yang belakangan ini bertebaran di mana-mana. Benar-benar klise dan menyebalkan sampai akhir."
    stop music fadeout 0.3
    nar "Lalu segalanya terputus menjadi hitam."
    nar "Raungan klakson, teriakan penumpang, dan rasa sakit dari peron lenyap begitu saja. Kesadaranmu hanya mengapung tanpa bobot di dalam kehampaan yang hening dan gelap gulita."
    $ kk_bgm("system")
    nar "Entah berapa lama kamu terombang-ambing di kehampaan itu, sampai perlahan-lahan kegelapan di hadapanmu mulai bergeser."
    nar "Dari balik bayangan pekat, dua buah tangan terulur menembus ruang hampa, berhenti tepat dalam jangkauanmu tanpa sepatah kata pun."
    nar "Di sebelah kiri, terulur tangan seorang pria yang berjari panjang, rapi, dan terawat."
    nar "Di sebelah kanan, terulur tangan seorang wanita yang ramping dan lentik, dengan bekas kapalan tipis di ruas jari tengahnya."
    nar "Kamu sama sekali tidak tahu milik siapa kedua tangan itu, atau ke mana mereka akan menyeretmu pergi. Instingmu berbisik jelas bahwa jika kamu tidak ingin lenyap begitu saja setelah kematian konyol tadi, kamu harus memilih salah satu dan menggenggamnya sekarang."
    call screen kk_route_select
    $ kk_host = _return
    $ kk_setup_state()
    call kk_prologue
    nar "Ikon wajah di layar kaca biru itu menyipitkan mata, lalu memunculkan barisan teks baru berwarna kuning menyala tepat di depan hidungmu."
    sistem "( ` v ´ )b Dan karena aku tahu kau bakal malas bergerak kalau tidak dipecut, ini misi pembukamu. Dalam tujuh hari ke depan, temui tiga orang yang dekat dengan Koita."
    sistem "Amati tabiat mereka, ajak bicara, dan cari tahu celah mana yang bisa kauungkit. Jangan coba-coba mengurung diri di kamar sampai tenggatnya habis. Aku paling benci pemeran yang mogok kerja, dan kau sudah merasakan sendiri caraku memberi teguran~ (^_~)-*"
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
        nar "Gema derit rem baja dan raungan klakson kereta ekspres masih memekakkan telinga batinmu ketika kamu tersentak bangun dengan tarikan napas panjang yang memburu."
        nar "Kedua tanganmu refleks mencengkeram bagian tengah dadamu kuat-kuat. Otot-ototmu menegang hebat, bersiap menyambut rasa ngilu dari tulang rusuk yang remuk dihantam moncong lokomotif serta rembesan darah panas di atas batu rel."
        nar "Rasa sakit yang kamu antisipasi itu sama sekali tidak datang. Dadamu terasa utuh dan hangat, jauh dari dinginnya kerikil peron kereta bawah tanah."
        nar "Yang tergenggam oleh jari-jarimu yang panjang justru permukaan kaus tidur berbahan katun lembut yang lembap oleh keringat dingin, membungkus bidang dada yang terasa rata, utuh, berotot ramping, dan jauh lebih lebar dari ukuran tubuh yang kamu ingat."
        nar "Dari lipatan selimut linen berwarna abu-abu gelap yang menutup pinggangmu, menguar aroma deterjen bersih yang sejuk bercampur samar dengan wangi kayu cedar."
        nar "Kamu mengerjap keras berkali-kali, mengatur tarikan napas yang masih tersengal di kerongkongan sambil mengedarkan pandangan ke sekeliling ruangan."
        nar "Kamu tidak sedang berbaring di aspal stasiun maupun di atas brankar ruang gawat darurat, melainkan di atas ranjang berukuran besar di dalam sebuah kamar apartemen modern yang sangat luas, rapi, dan sunyi senyap."
        nar "Langit-langit beton ekspos yang tinggi, tirai jendela kaca setinggi dinding yang menyisakan siluet gedung-gedung kota saat dini hari, serta dengung halus mesin pendingin udara di tengah keheningan yang terasa terlalu hampa untuk satu orang membuat keningmu berkerut dalam."
        nar "Setiap detail di ruangan mewah yang dingin ini terasa begitu nyata, dan kamu yakin belum pernah menginjakkan kaki di tempat seperti ini seumur hidupmu."
    else:
        $ kk_mc_nama = "CHIASA (kau)"
        show screen kk_set("chiasa", "Rumah Amamiya · Pagi")
        with fade
        nar "Begitu jemarimu menggenggam tangan wanita itu di dalam kehampaan, gravitasi mendadak berbalik arah. Sebuah sentakan keras merenggut kesadaranmu turun menembus lorong gelap yang pengap, seolah tubuhmu diikat batu dan dilempar paksa ke dasar air yang tak bertepi."
        nar "Gema derit rem baja dan raungan klakson kereta ekspres masih memekakkan telinga batinmu ketika kamu tersentak bangun dengan tarikan napas panjang yang memburu."
        nar "Kedua tanganmu refleks mencengkeram bagian tengah dadamu kuat-kuat. Otot-ototmu menegang hebat, bersiap menyambut rasa ngilu dari tulang rusuk yang remuk dihantam moncong lokomotif serta rembesan darah panas di atas batu rel."
        nar "Rasa sakit yang kamu antisipasi itu sama sekali tidak datang. Dadamu terasa utuh dan hangat, jauh dari dinginnya kerikil peron kereta bawah tanah."
        nar "Yang tersentuh oleh telapak tanganmu justru permukaan kain piyama katun yang halus dan kering, membungkus lekuk dada serta tulang rusuk yang terasa utuh, ringan, dan sama sekali bukan ukuran tubuhmu sendiri."
        nar "Dadamu naik turun dengan irama napas yang pendek dan cepat. Dari lipatan selimut tebal yang menutup pinggangmu, menguar aroma sabun mandi berwangi bunga lembut yang bercampur samar dengan bau kayu pinus serta cat akrilik kering."
        nar "Saat kamu menunduk dengan napas yang masih tersengal-sengal di kerongkongan, beberapa helai rambut panjang berwarna cokelat gelap merosot melewati bahumu, menyapu tulang selangka dan menggelitik kulit pipimu yang dingin oleh keringat."
        nar "Kamu mengerjap keras berkali-kali, memaksa mata yang terasa perih oleh cahaya untuk mengenali ruang di sekelilingmu."
        nar "Sinar matahari pagi awal musim semi menembus tirai tipis berwarna gading di jendela sebelah kanan, membiaskan debu-debu halus yang melayang di atas lantai kayu dan karpet rajut bundar."
        nar "Kamar ini tertata rapi sekaligus penuh dengan jejak kesibukan seseorang. Sebuah meja rias kayu berdiri di sudut dekat lemari, bersebelahan dengan meja belajar lebar yang dipenuhi tabung kuas, deretan botol tinta gambar, kaleng pensil, serta papan sketsa kayu."
        nar "Setiap sudut ruangan ini menunjukkan bahwa tempat ini milik seorang gadis muda, dan kamu sama sekali tidak pernah menginjakkan kaki di dalamnya seumur hidupmu."
    $ kk_bgm("system")
    play sound "audio/sfx/system_open.wav"
    nar "Belum sempat otakmu yang masih pening merangkai satu pun penjelasan masuk akal, bunyi derik statis seperti radio rusak tiba-tiba menyambar langsung di dalam rongga telingamu."
    nar "Udara kosong sekitar setengah meter di depan wajahmu bergetar dan berkedip dua kali. Tanpa proyektor maupun layar fisik, sebuah jendela kaca biru transparan membuka diri begitu saja di ruang pandangmu, menampilkan deretan teks dan emotikon garis cahaya neon yang menyunggingkan senyum miring."
    sistem "( ´ v ` )/ Bangun juga akhirnya~ Kukira jiwamu ikut penyok terlindas roda kereta tadi, Sampah Peron."
    nar "Suara itu tidak datang dari arah pintu maupun jendela, melainkan bergema langsung di balik tulang tengkorakmu, bernada rendah, ceria secara dibuat-buat, dan sarat dengan nada mengejek yang membuat darahmu mendidih seketika."
    nar "Kamu refleks mengayunkan tangan kananmu ke depan untuk menepis panel cahaya itu jauh-jauh dari wajahmu."
    nar "Jemarimu hanya menembus bidang kaca biru itu seperti membelah kepulan asap dingin. Kamu tersentak mundur hingga punggungmu menghantam sandaran kepala ranjang dengan mata melebar."
    if kk_host == "yutaka":
        yutaka "Suara apa itu?! Siapa yang bicara di dalam kamarku?!"
        nar "Kalimat itu terputus di ujung lidahmu sendiri. Kamu membeku selama satu detak jantung penuh, meraba pangkal tenggorokanmu yang bergetar."
        nar "Suara yang baru saja memantul di dinding beton kamar ini adalah suara bariton seorang pria muda, rendah, jernih, dan terdengar berwibawa secara alami meski sedang serak oleh kepanikanmu. Itu jelas bukan warna suaramu sendiri."
        yutaka "Suaraku... tunggu, kenapa suaraku terdengar seperti orang lain?! Hei! Proyektor macam apa ini, keluar dan tunjukkan wajahmu!"
    else:
        chiasa "Suara apa itu?! Siapa yang memasang layar ini di depanku?!"
        nar "Kalimat itu terputus di ujung lidahmu sendiri. Kamu membeku selama satu detak jantung penuh, meraba pangkal tenggorokanmu yang terasa ramping dan asing."
        nar "Suara yang baru saja memantul di dinding kamar ini adalah suara seorang perempuan muda, jernih, ringan, dan sedikit bernada tinggi di ujung kalimat karena kepanikanmu."
        chiasa "Suaraku... tunggu, kenapa suaraku berubah seperti ini?! Hei! Jangan bersembunyi di balik layar konyol itu, keluar dan jelaskan apa yang kamu lakukan padaku!"
    nar "Ikon emotikon di layar biru itu memutar kedua matanya dengan animasi patah-patah yang tampak sengaja dibuat untuk memancing emosi. Detik berikutnya, sengatan nyeri setajam jarum listrik bertegangan tinggi menusuk lurus ke balik pelipismu hingga kamu terpekik dan mencengkeram kepala dengan kedua tangan."
    sistem "(¬_¬ ) Berisik sekali. Itu barusan bukti kecil supaya kau tidak membuang waktuku yang berharga dengan mengira ini cuma mimpi buruk atau efek obat bius di ruang gawat darurat."
    sistem "Tubuh lamamu sudah selesai jadi daging giling di atas rel stasiun, Manusia (´• v •`). Yang sedang kaupakai menghirup oksigen sekarang adalah tubuh pinjaman dariku, dan kesadaran pemilik aslinya sudah tidak ada lagi di dalam sana~"
    if kk_host == "yutaka":
        yutaka "Tubuh pinjaman...? Pemilik aslinya sudah tidak ada?! Kamu pikir aku bakal menelan ocehan gila dari benda mencurigakan di kepalaku?!"
        nar "Denyut ngilu di pelipismu perlahan mereda, menyisakan napasmu yang memburu kasar di tengah keheningan apartemen yang terlalu luas itu."
        play sound "audio/sfx/phone_vibrate.wav"
        nar "Tepat saat kamu menggeram kesal, ponsel pintar di atas nakas sebelah ranjang, tepat di samping sebuah jam tangan tipis bertali kulit yang tampak sering dipakai, bergetar panjang berulang-ulang dan menyalakan layar panggilan masuk dengan nama kontak 'Koita' yang terus berkedip."
        nar "Sementara itu, beberapa langkah di seberang ranjang, tampak sebuah dompet kulit hitam di atas meja kaca ruang tamu serta pintu kamar mandi dalam yang sedikit terbuka, seolah menantangmu untuk membuktikan sendiri klaim suara tersebut."
    else:
        chiasa "Tubuh pinjaman...? Pemilik aslinya sudah tidak ada?! Kamu pikir aku bakal menelan klaim sinting dari suara nggak jelas di kepalaku?!"
        nar "Denyut ngilu di pelipismu perlahan mereda, menyisakan napasmu yang memburu kasar di sela gigi yang terkatup rapat."
        play sound "audio/sfx/ceramic.wav"
        nar "Tepat pada saat keheningan kamar itu kembali turun, dari lantai bawah rumah ini terdengar bunyi denting piring keramik yang beradu dengan permukaan meja, disusul desis air mendidih dari teko dan langkah kaki seseorang yang berjalan tenang di dapur."
        nar "Di dalam kamarmu sendiri, pantulan samar dari cermin meja rias di sudut ruangan, buku sketsa tebal yang terbuka di meja belajar, serta sebuah ponsel pintar yang terhubung ke kabel pengisi daya di atas nakas seolah menantangmu untuk membuktikan sendiri ucapan suara tersebut."
    sistem "(¬v¬) Tidak percaya? Silakan saja periksa sendiri kamar ini. Kau punya kaki, mata, dan barang-barang pemilik tubuh itu di dekatmu, kan? Cari tahu sendiri kau sedang menjadi siapa sekarang, sebelum kita bicara soal harga sewa nyawamu~ (^_~)-*"
    call kk_first_morning
    $ kk_bgm("system")
    nar "Tepat ketika kamu masih berusaha menelan kenyataan gila tentang identitas barumu dan siapa saja orang yang tinggal di sekelilingmu, udara kosong di depan wajahmu kembali bergetar."
    play sound "audio/sfx/system_open.wav"
    nar "Jendela kaca biru itu meluncur turun untuk kedua kalinya, menampilkan emotikon garis yang membentuk gerakan tepuk tangan lambat yang sarat ejekan."
    sistem "(*^v^*)// Selamat atas pencerahannya, Manusia~ Ekspresi terkejutmu barusan benar-benar layak dijadikan pembuka pagi."
    if kk_host == "yutaka":
        yutaka "Kamu... kamu sengaja memasukkanku ke dalam manga sampah yang baru kubaca sebelum mati?! Sebagai Kisaragi Yutaka pula?! Apa maumu sebenarnya, brengsek?!"
    else:
        chiasa "Kamu... kamu sengaja memasukkanku ke dalam manga sampah yang baru kuhina sebelum mati?! Di tubuh Amamiya Chiasa pula?! Otakmu sudah miring, hah?!"
    sistem "( ´ w ` )/ Justru karena kau begitu membenci manga ini dari ujung rambut sampai ujung kaki, kau adalah kandidat paling cocok untukku. Panggil aku Sistem, dan mulai detik ini, kontrak sewa nyawamu resmi aktif."
    sistem "Aturan mainnya sangat sederhana. Kau punya waktu tiga tahun penuh sampai Amamiya Koita lulus kuliah untuk menyimpangkan takdir romantisnya sejauh mungkin dari jalur asli manga ini."
    sistem "Evaluasinya hanya dilakukan satu kali, tepat pada hari ia naik ke panggung aula untuk menerima ijazah wisuda (´• v •`). Kalau sampai detik itu skenario romansa sang MC masih berjalan mulus... jantung pinjaman di dadamu itu akan kubuat berhenti berdetak di tempat~"
    if kk_host == "yutaka":
        yutaka "Jangan bercanda! Kenapa aku harus ikut campur mengurus urusan percintaan si MC naif itu pakai taruhan nyawa segala?!"
    else:
        chiasa "Jangan gila! Kenapa nyawaku harus digantungkan pada urusan cinta kakak tiri menyebalkan itu?!"
    nar "Layar biru transparan itu mendadak berkedip merah menyala sesaat, memancarkan gelombang tekanan dingin yang membuat bulu kuduk di tengkukmu berdiri."
    sistem "(¬_¬ ) Karena hidup keduamu adalah milikku. Bagaimana caramu merusak takdirnya, siapa yang kaurangkul atau kauhancurkan, dan seperti apa wajah aslimu di balik topeng tubuh itu? Bukan urusanku menebaknya sekarang."
    sistem "Simpan keluhan moralmu, Manusia ( ´ v ` )~. Aku akan menilai siapa kau sebenarnya dari apa yang kaulakukan selama tiga tahun ini. Berapa pun kerasnya kau memakiku di kamar ini, sama sekali tidak ada artinya."
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
            nar "Kamu menyibak selimut linen itu ke samping dan menurunkan kedua telapak kakimu ke atas lantai parket kayu yang dingin. Begitu kamu bertumpu untuk berdiri tegak, titik berat tubuh ini terasa begitu ganjil."
            nar "Tungkai kakimu terasa jauh lebih panjang dengan jangkauan langkah yang lebar, sementara postur tubuhmu yang menjulang tinggi membuat sudut pandangmu terhadap perabotan kamar terasa berbeda dari biasanya."
            nar "Sambil menahan napas yang masih terasa berat di dada, kamu memaksakan diri melangkah melewati karpet ruang tengah menuju meja kaca rendah, tempat sebuah dompet kulit hitam berdesain minimalis dan berkelas tergeletak berdampingan dengan sebuah ponsel pintar."
            nar "Jika suara kurang ajar di kepalamu tadi tidak berbohong soal tubuh pinjaman, maka kedua benda pribadi di atas meja itu adalah petunjuk paling nyata tentang siapa pemilik apartemen ini."
            nar "Kamu menyambar dompet kulit tersebut dan membuka lipatannya. Di balik deretan kartu debit prioritas berlogo bank swasta besar dan lembaran uang tunai sepuluh ribu yen yang tersusun rapi tanpa lipatan, terselip selembar kartu tanda mahasiswa bertuliskan 'Universitas Kouseikan, Fakultas Ekonomi dan Bisnis'."
            nar "Kamu menarik kartu mahasiswa itu keluar dari slot kulitnya, mengamati pasfoto seorang pemuda tampan berusia dua puluh tahun berambut hitam pekat dengan sorot mata abu-abu gelap yang tampak santai, lalu membaca nama yang tercetak tegas di sebelahnya."
            nar "Saat tanganmu yang lain meraih ponsel pintar di atas meja kaca, permukaan layarnya yang masih gelap memantulkan bayangan wajah asing yang persis sama dengan foto di kartu tersebut."
            yutaka "{i}Universitas Kouseikan...? Tunggu dulu, nama kampus ini persis judul manga yang baru kubaca di kereta tadi. Tapi wajah sama nama di kartu ini aku nggak langsung ingat siapa...{/i}"
            nar "Sebagai pembaca yang hanya sesekali membuka bab manga itu sambil menggerutu, kamu tidak hafal wajah setiap tokoh pendukungnya. Dengan kening berkerut dan napas tercekat, kamu menempelkan ibu jari tangan kananmu ke pemindai ponsel hingga kuncinya langsung terbuka tanpa hambatan."
            nar "Kamu membuka aplikasi perbankan digital yang berada di halaman depan. Angka yang terpampang di layar membuat matamu terbelalak karena saldo aktif yang bisa kamu gunakan hari ini mencapai [_balance], lengkap dengan catatan transfer otomatis bulanan sebesar seratus lima puluh ribu yen dari rekening atas nama 'Kisaragi Kenji' tanpa sepatah pesan pribadi pun."
            nar "Ibu jarimu menggulir cepat ke aplikasi pesan singkat. Di urutan bawah, tampak ruang obrolan dengan 'Kisaragi Reiko' yang hanya berisi kalimat satu arah yang dingin dari bulan lalu tanpa sapaan seorang ibu, 'Transfer bulan ini sudah masuk. Jangan membuat masalah di kampus.'"
            nar "Baru ketika matamu naik ke obrolan grup empat sekawan masa kecil yang berisi nama 'Amamiya Koita' dan 'Sakurajima Nagisa', lalu berhenti pada ruang obrolan paling atas bernama 'Amamiya Chiasa', kepingan ingatanmu akhirnya menyambung pelan."
            yutaka "{i}Tunggu... Amamiya Koita? Sakurajima Nagisa? Terus apartemen mewah sendirian dengan saldo sebanyak ini... oh, baru ingat sekarang! Dia sahabat kaya si MC yang jarang dapat sorotan utama di manga 'Kouseikan' itu... Kisaragi Yutaka!{/i}"
            nar "Di dalam kolom ketik ruang obrolan 'Amamiya Chiasa' yang terbuka di layar, masih tersimpan satu draf pesan yang diketik semalam oleh Yutaka asli tetapi tidak pernah berani dikirim, mengajak adik tiri Koita itu makan siang berdua setelah acara orientasi."
            nar "Kamu menelan ludah menatap cahaya layar ponsel di tengah ruang tamu yang terlalu luas dan sunyi ini. Pantas saja wajahnya tidak langsung melekat di kepalamu tadi. Kamu benar-benar terlempar ke dalam tubuh sang sahabat pendukung yang kesepian, dan seluruh kekayaan di rekening ini sama sekali tidak memberimu ingatan tentang bagaimana cara menjadi pemuda yang mereka kenal."
        elif _opening_key == "B":
            nar "Kamu menolak memercayai klaim gila bahwa tubuh aslimu sudah hancur di bawah roda kereta sebelum melihat buktinya dengan mata kepalamu sendiri."
            nar "Dengan langkah yang masih agak canggung karena ukuran tungkai yang terasa jauh lebih panjang dan tinggi, kamu bangkit dari tepi kasur, melintasi lantai kayu kamar tidur, dan mendorong pintu kamar mandi dalam yang sedikit terbuka."
            nar "Jari-jarimu yang panjang meraba dinding marmer dingin di dekat kusen pintu lalu menekan sakelar. Lampu putih di atas cermin wastafel lebar langsung menyala terang, memantulkan sosok seorang pria muda dengan jelas."
            nar "Kamu membeku di depan wastafel porselen itu."
            nar "Pria berusia sekitar dua puluh tahun di balik kaca tersebut memiliki postur tinggi ramping yang atletis di balik kaus tidur berwarna biru tua, bekas lipatan bantal tipis di pipi kirinya, dada yang naik turun oleh napas yang memburu, serta sepasang mata abu-abu gelap yang melebar penuh ketegangan."
            nar "Saat kamu mengangkat tangan kananmu yang gemetar untuk menyentuh dagu dan garis rahangmu sendiri, pemuda di dalam cermin itu melakukan gerakan yang persis sama pada detik yang sama."
            yutaka "Wajah orang lain... Aku benar-benar berada di dalam tubuh orang lain. Tapi siapa pria ini?"
            nar "Suara bariton yang memantul di dinding keramik kamar mandi itu membuat tengkukmu semakin dingin. Kamu mencondongkan tubuh lebih dekat ke permukaan cermin, mengamati potongan rambut hitam pekat yang poninya jatuh acak-acakan di dahi serta struktur wajah yang sama sekali tidak langsung memicu ingatan apa pun di kepalamu."
            nar "Ekor matamu lalu melirik jaket almamater yang tergantung rapi di balik pintu kamar mandi dengan bordir nama 'Universitas Kouseikan, Kisaragi'. Keningmu seketika berkerut dalam."
            yutaka "{i}Universitas Kouseikan...? Tunggu sebentar, itu kan nama kampus di manga yang baru kuhina di kereta tadi! Tapi marga Kisaragi... siapa pula tokoh bernama Kisaragi di cerita itu?{/i}"
            nar "Kamu keluar kembali ke kamar tidur dengan pikiran berpacu, lalu pandanganmu tertumbuk pada ponsel di nakas yang masih menampilkan panggilan masuk bernama 'Koita' tepat di sebelah rak televisi berisi bingkai foto masa kecil empat anak di festival musim panas."
            nar "Menyambungkan nama 'Koita', apartemen mewah yang kosong, dan marga 'Kisaragi' akhirnya membuka sudut ingatan samar yang hampir terlupakan dari bab-bab manga yang jarang kamu baca sampai tuntas."
            yutaka "{i}...Oh! Sialan, baru nyambung sekarang! Dia sahabat masa kecilnya Amamiya Koita yang tajir itu, Kisaragi Yutaka! Pantas aja tadi di cermin aku nggak langsung ngeh, di manganya dia memang bukan tokoh utama dan jarang dapat sorotan sendiri!{/i}"
            nar "Kamu mencengkeram sandaran kursi di dekat meja dengan buku-buku jari yang memutih. Dari seluruh orang di dunia komik yang baru saja kamu hina itu, kamu justru terlempar masuk ke tubuh si sahabat pendukung yang selalu berdiri setengah langkah di belakang sang MC dan jarang disorot, padahal diam-diam memendam perasaan sendirian."
            nar "Bulir keringat dingin yang merembes di pelipis serta denyut pembuluh nadi di lehermu yang memburu kencang membuat kenyataan bahwa kamu kini menghuni tubuhnya terasa begitu mencekam."
        elif _opening_key == "C":
            play sound "audio/sfx/phone_vibrate.wav"
            nar "Pandanganmu terpaku pada ponsel pintar di atas nakas sebelah ranjang yang masih terus bergetar panjang, bergeser tipis di atas permukaan kayu seiring dering getarannya."
            nar "Nama 'Koita' yang berkedip-kedip di layar panggilan masuk itu membuat dadamu terasa dingin, terlalu ganjil dan terlalu kebetulan jika dibandingkan dengan nama MC manga yang baru saja kamu cibir habis-habisan di peron stasiun."
            nar "Dengan jantung yang berdegup kencang, kamu menggeser tubuh ke tepi kasur dan menyambar ponsel itu dari kabel pengisi dayanya."
            nar "Sebelum jemarimu sempat menyentuh tombol jawab maupun tolak, bagian kaca layar di sekitar foto kontak memantulkan bayangan seorang pemuda asing berwajah tampan dengan rambut hitam pekat agak berantakan dan sepasang mata abu-abu gelap yang sama sekali tidak kamu kenali."
            nar "Pada saat yang sama, sensor pemindai wajah otomatis mengenali pemilik tubuh ini dan membuka bilah informasi profil di sudut atas layar kunci bertuliskan 'Tahun Kedua, Universitas Kouseikan' di bawah sebuah nama bermarga Kisaragi."
            yutaka "{i}Universitas Kouseikan...? Tunggu dulu, Kouseikan itu judul manga tadi kan? Tapi marga Kisaragi di layar kunci ini tokoh yang mana lagi...{/i}"
            nar "Kamu masih berusaha mengingat siapa pemilik nama itu di antara deretan tokoh manga yang jarang kamu ikuti detailnya ketika getaran panggilan masuk dari 'Koita' di telapak tanganmu hampir berhenti karena terlalu lama dibiarkan."
            nar "Didorong kepanikan sekaligus dorongan untuk membuktikan apakah dunia ini benar-benar hidup atau sekadar ilusi, ibu jarimu refleks menggeser ikon hijau di layar untuk mengangkat panggilan tersebut."
            nar "Bahkan sebelum kamu sempat menarik napas untuk menyiapkan sepatah alasan pun, suara seorang pemuda langsung terdengar jernih dari balik pengeras telinga."
            koita "Halo, Yutaka? Tumben lama sekali angkat teleponnya, kamu baru bangun ya? Kita tetap jadi berangkat kuliah bareng dari depan stasiun pagi ini, kan?"
            nar "Suara itu terdengar begitu nyata, ramah, hangat, sedikit terburu-buru khas mahasiswa di pagi hari pertama semester, dan penuh keakraban seseorang yang sudah mengenal pemilik tubuh ini sejak kecil tanpa menaruh curiga sedikit pun."
            nar "Mendengar suara Amamiya Koita sendiri berbicara seakrab itu langsung di telingamu membuat lidahmu mendadak kelu sekaligus menyalakan kepingan ingatan yang tadi terputus."
            yutaka "A-ah... soal itu, kepalaku agak pusing waktu baru bangun barusan. Kamu berangkat duluan saja ke kampus, nanti kukabari lagi kalau aku sudah di jalan ya, Koita."
            koita "Eh, kamu nggak apa-apa? Tumben sekali kamu mengeluh pusing pagi-pagi begini. Semalam begadang main gim lagi ya?"
            yutaka "Nggak... cuma kurang enak tidur saja semalam. Kamu jalan duluan saja biar nggak telat."
            koita "Jangan dipaksa berangkat kalau memang belum enak badan, ya. Nanti absen kelas pagi biar kutanyakan ke anak-anak fakultasmu kalau berpapasan di gerbang. Kabari aku kalau butuh dibawakan sesuatu."
            nar "Sambungan telepon itu terputus dengan bunyi klik halus. Kamu menurunkan ponsel dari telingamu perlahan-lahan dengan napas tertahan."
            yutaka "{i}...Oh. Baru ingat sekarang. Sahabat masa kecilnya Koita yang tinggal di apartemen mewah tapi di manga jarang dapat jatah adegan utama itu... ternyata namanya Kisaragi Yutaka.{/i}"
            nar "Dunia manga ini benar-benar nyata, dan Amamiya Koita baru saja memercayai setiap patah kata yang keluar dari mulut tubuh ini tanpa keraguan sedikit pun."
        else:
            nar "Kamu meremas seprai linen kasur itu kuat-kuat hingga buku-buku jarimu memutih dan menolak beranjak satu langkah pun dari tempat tidur."
            nar "Enak saja suara sialan itu menyuruhmu jalan-jalan memeriksa kamar seperti pesuruh setelah menculik kesadaranmu ke tempat asing. Di atas nakas sebelahmu, getaran telepon masuk dari 'Koita' di layar ponsel akhirnya berhenti sendiri, menyisakan notifikasi panggilan tak terjawab yang meredup."
            nar "Tepat saat kamu mendongak hendak memaki ruang kosong di depan ranjang lagi, tatapanmu tanpa sengaja menangkap pantulan dirimu sendiri di cermin pintu lemari pakaian besar yang berseberangan langsung dengan kasur."
            nar "Di dalam cermin itu, tampak seorang pemuda asing bertubuh tinggi ramping dengan rambut hitam pekat yang berantakan dan sepasang mata abu-abu gelap yang menatap lurus ke arahmu. Kamu menatap pantulan itu beberapa detik tanpa sedikit pun mengenalinya."
            nar "Baru ketika pandanganmu bergeser ke amplop bertuliskan 'Universitas Kouseikan' di atas meja, bingkai foto masa kecil empat anak di festival musim panas dekat televisi, serta panggilan tak terjawab bertuliskan 'Koita' di atas nakas, kepingan ingatan yang kabur itu pelan-pelan mulai tersusun."
            yutaka "{i}Tunggu dulu... Universitas Kouseikan... yang nelpon tadi namanya Koita... apartemen mewah sendirian, terus foto empat anak kecil di sebelah rak itu...{/i}"
            nar "Kamu memejamkan mata sejenak mengorek ingatan dari bab-bab manga yang hanya sesekali kamu baca sebelum akhirnya matamu melebar."
            yutaka "{i}...Oh! Sahabat kaya si MC yang jarang disorot itu?! Jangan bercanda, aku dilempar ke tubuh Kisaragi Yutaka dari manga 'Kouseikan'?!{/i}"
            nar "Menyadari kamu dilempar masuk ke dalam tubuh si sahabat pendukung yang kesepian di cerita harem yang paling kamu benci membuat amarahmu langsung meledak ke arah ruang kosong di depan kasur."
            yutaka "Hei, keluar lagi kamu! Kamu pikir lucu memasukkanku ke tubuh figuran manga sampah ini?! Kembalikan aku ke tubuhku sekarang juga, pengecut!"
            nar "Udara kosong di depan wajahmu berkedip tajam. Emotikon garis di layar kaca biru itu melebarkan senyum miringnya, lalu detik berikutnya dengung frekuensi tinggi mendadak menghantam gendang telingamu, disusul rasa ngilu yang buas di belakang bola mata hingga kamu terbungkuk di atas kasur sambil mencengkeram kening."
            yutaka "Argh, sialan! Hentikan!"
            sistem "(¬_¬\") Menuntut pelayanan sambil berteriak seolah kau pelanggan raja di restoran bintang lima? Nyalimu lumayan juga, Manusia, sayang sekali otakmu tertinggal di bawah roda kereta~"
            nar "Sengatan ngilu itu dicabut seketika, menyisakan napasmu yang terengah-engah di atas kasur dengan keringat dingin membasahi tengkuk dan pelipis."
            yutaka "Hah... hah... dasar psikopat sakit jiwa! Kamu memungutku ke apartemen ini cuma buat dijadikan bahan tontonanmu?!"
            sistem "( ´ v ` )~ Aku lebih suka disebut sutradara yang murah hati. Mesin pendingin apartemen mewah ini masih menyala, saldo bankmu masih penuh, kota di balik jendela itu terus berjalan, dan kau masih hidup. Jadi berhentilah merengek sebelum kutambah dosis perkenalannya, ya~"
    else:
        if _opening_key == "A":
            nar "Kamu menyibak selimut hangat itu ke samping dan menurunkan kedua telapak kakimu ke atas karpet rajut di samping ranjang. Serat benangnya terasa lembut di bawah kulit telapak kaki yang mungil, lalu begitu kamu bertumpu untuk berdiri tegak, tubuhmu langsung oleng setengah langkah."
            nar "Kamu buru-buru menahan pinggiran kasur dengan telapak tangan. Titik berat tubuh ini terasa ganjil, jauh lebih pendek dan lebih ringan, dengan tulang bahu yang sempit dan lekuk pinggang yang membuat setiap ayunan langkah terasa asing."
            nar "Setiap kali kamu bergerak, massa rambut panjang yang tergerai bebas di punggungmu ikut bergeser lembut menyapu kain piyama di sekitar belikat."
            nar "Sambil menahan napas yang masih terasa dingin di pangkal tenggorokan, kamu melangkah pelan menghampiri meja rias kayu di sudut kamar, lalu berhenti tepat di hadapan cermin lonjongnya."
            nar "Kamu terpaku menatap sosok di balik kaca itu."
            nar "Seorang gadis muda berusia sekitar sembilan belas tahun sedang menatapmu balik dengan wajah oval yang pucat dan sepasang mata kuning keemasan yang melebar kaku. Rambut cokelat gelapnya yang panjang sepunggung terurai agak berantakan bekas tidur tanpa ikatan apa pun, dengan poni menyamping yang sedikit kusut menutupi sebagian keningnya."
            nar "Saat kamu mengangkat tangan untuk meraba pipimu sendiri, gadis di dalam cermin itu melakukan gerakan yang persis sama pada detik yang sama."
            chiasa "...Siapa gadis ini? Rambut cokelat panjang, mata kuning keemasan... aku sama sekali nggak kenal wajah ini."
            nar "Suara jernih yang meluncur dari bibirmu sendiri membuat tengkukmu merinding. Tanpa riasan atau aksesoris khas apa pun, sosok bangun tidur di balik kaca itu hanya terlihat seperti mahasiswi asing yang membuat kepalamu semakin buntu."
            nar "Pandanganmu turun ke permukaan meja rias kayu di bawah cermin. Di atas sebuah nampan kecil di samping sisir rambut, tergeletak rapi sehelai pita hitam halus bersama sepasang anting mungil dan rantai kalung tipis."
            nar "Dengan dada yang masih bergemuruh bingung, kamu menoleh ke meja belajar lebar tepat di sebelah meja rias untuk mencari nama pemilik kamar ini."
            nar "Di atas permukaan kayu yang bersih dari debu itu, tergeletak amplop jadwal orientasi mahasiswa baru bertuliskan 'Universitas Kouseikan, Fakultas Seni Rupa dan Desain' dengan marga 'Amamiya' tercetak di bagian penerima, bersebelahan dengan deretan pena gambar teknik, penghapus uli, serta sebuah buku sketsa tebal bersampul hitam yang sedang terbuka."
            nar "Begitu matamu membaca tulisan kampus dan marga di amplop itu, lalu kembali melirik pita hitam di atas nampan meja rias serta wajah bermata keemasan di dalam cermin, potongan ingatan tentang halaman berwarna manga yang baru kamu baca di peron stasiun akhirnya menghantam kepalamu."
            chiasa "{i}Tunggu sebentar... Universitas Kouseikan, mata kuning keemasan, marga Amamiya, ditambah pita hitam di meja rias itu... pantas aja tadi waktu rambutnya masih terurai bangun tidur aku nggak langsung ngeh! Jangan bercanda, aku beneran di tubuh adik tirinya si MC... Amamiya Chiasa?!{/i}"
            nar "Kamu refleks membekap mulutmu sendiri dengan kedua telapak tangan, mundur setengah langkah dari meja hingga betismu menyentuh kursi kayu."
            nar "Dari sekian banyak orang di dunia fiksi itu, kamu justru dilempar masuk ke dalam tubuh si adik tiri tanpa hubungan darah yang tinggal satu atap dengan sang MC, Amamiya Koita, dan diam-diam memendam obsesi romantis pada kakak tirinya sendiri!"
            nar "Kamu menunduk menatap halaman buku sketsa yang masih terbuka di meja belajar. Di atas kertas bertekstur halus itu, terpampang gambar rancangan anatomi dan ilustrasi karakter novel ringan yang luar biasa hidup. Garis-garisnya bersih, tegas, dengan arsiran bayangan yang halus dan tanda tangan pena mungil bertuliskan 'Shena' di sudut kanan bawah."
            nar "Di samping buku sketsa itu, terselip pula selembar contoh sampul cetakan novel ringan strategi populer yang mencantumkan nama ilustrator yang sama."
            nar "Kamu menatap bekas kapalan tipis di ruas jari tengah tangan kananmu, lalu kembali melihat kualitas ilustrasi profesional di atas meja. Perutmu mendadak terasa dingin."
            chiasa "{i}Seni Rupa... dan dia ilustrator sungguhan pakai nama pena 'Shena'? Tunggu dulu... kalau nanti aku masuk kelas studio atau ada tugas gambar, terus aku harus gimana?{/i}"
            nar "Tanganmu sempat menyentuh pinggiran buku sketsa yang masih terbuka itu, lalu menariknya kembali dengan gugup. Di kepalamu sekarang bahkan belum sempat terbayang apakah tubuh ini masih menyimpan bakat pemilik aslinya atau tidak, karena satu-satunya yang terasa nyata hanyalah fakta bahwa kamu baru saja dilempar ke tengah hidup seseorang yang jauh lebih rumit daripada yang pernah kamu baca di manga."
        elif _opening_key == "B":
            nar "Kamu menggeser tubuhmu yang terasa ringan dan asing itu ke tepi kasur, lalu menjulurkan tangan meraih ponsel pintar bersarung krem-hitam yang sedang terhubung ke kabel pengisi daya di atas nakas kayu."
            nar "Jika suara kurang ajar di kepalamu tadi tidak berbohong tentang tubuh pinjaman, maka benda pribadi yang paling sering disentuh pemilik kamar ini pasti menyimpan seluruh identitasnya."
            nar "Kamu mencabut kabel pengisi dayanya dengan jari yang sedikit gemetar. Saat kamu mengangkat ponsel itu ke depan wajahmu, permukaan kaca layarnya yang masih gelap memantulkan bayangan sepasang mata kuning keemasan yang bulat melebar dengan rambut cokelat gelap panjang yang terurai kusut bekas tidur."
            nar "Kamu sama sekali tidak mengenali gadis berambut terurai di pantulan kaca tersebut. Detik berikutnya, layar ponsel menyala otomatis. Ikon gembok kecil di bagian atas layar langsung terbuka hanya dengan memindai wajah yang sedang kamu pakai, sama sekali tidak memberimu kesempatan untuk terhalang oleh kata sandi."
            nar "Kamu mengerjap pelan menatap halaman utama yang tertata rapi dengan folder-folder kuliah dan aplikasi gambar. Di bilah pengingat paling atas, terpampang kartu identitas digital mahasiswa baru bertuliskan 'Tahun Pertama, Fakultas Seni Rupa dan Desain, Universitas Kouseikan' dengan marga 'Amamiya' di bawah fotonya."
            nar "Tatapanmu sempat terangkat melirik sehelai pita hitam yang tergeletak rapi di atas nampan meja rias di sudut kamar, lalu kembali ke layar ponsel. Barulah saat seluruh petunjuk itu bertautan, potongan sampul manga yang baru saja kamu cibir habis-habisan di peron kereta bawah tanah menyambar ingatanmu."
            chiasa "{i}Tunggu sebentar... Universitas Kouseikan, marga Amamiya, mata kuning keemasan, terus pita hitam yang ditaruh di meja rias sana... pantas aja tadi di pantulan layar nggak langsung sadar karena rambutnya masih terurai tanpa pita! Jangan gila, ini kan Amamiya Chiasa?! Adik tiri si MC di manga 'Kouseikan'?!{/i}"
            nar "Jantungmu berdegup kencang menghantam rongga dada yang sempit ini. Kamu benar-benar dilempar masuk ke dalam manga harem yang paling kamu benci, dan parahnya lagi, kamu menghuni tubuh adik tiri tanpa hubungan darah yang tinggal serumah dengan Amamiya Koita!"
            nar "Dengan ujung jari yang terasa dingin, kamu membuka aplikasi di dalam ponsel itu satu per satu untuk memeriksa seberapa dalam hidup gadis ini harus kamu tanggung."
            nar "Aplikasi perbankan digital menampilkan saldo akhir sebesar empat ratus ribu yen, gabungan dari kiriman uang saku bulanan lima puluh ribu yen dari ayahnya, Amamiya Daisuke, serta transfer royalti pasif lima puluh ribu yen per bulan dari penerbit novel ringan atas nama pena 'Shena'."
            nar "Kamu beralih membuka aplikasi surat elektronik. Pesan terbaru di kotak masuk berasal dari seorang editor bernama Higashiyama Miono yang menyapamu dengan sebutan 'Shena-sensei', mengucapkan selamat masuk kuliah, dan memastikan bahwa royalti cetakan ulang tetap berjalan tanpa kewajiban proyek ilustrasi baru untuk saat ini, meski ia berharap bisa segera mendiskusikan sampul jilid berikutnya."
            nar "Ketika kamu berpindah ke aplikasi pesan singkat, deretan notifikasi langsung menyambut matamu. Di urutan bawah, ada pesan semalam dari ibu tirinya, Amamiya Yoshie, yang menanyakan kabar dari luar kota dan mengingatkan dengan nada lembut agar Chiasa serta Koita menghabiskan lauk di kotak plastik biru dan tidak hanya makan roti tawar."
            nar "Di atasnya, ada belasan pesan beruntun penuh tanda seru dari kontak teman sejurusan bernama 'Ishikawa Karuha' yang meributkan jadwal studio minggu pertama sekaligus memuja-muja goresan ilustrasi terbaru 'Shena-sensei', tanpa sedikit pun menyadari bahwa gadis yang dikiriminya pesan adalah sang ilustrator itu sendiri."
            nar "Ruang obrolan yang disematkan paling atas dengan tanda bintang khusus hanyalah satu nama kontak, 'Ko-nii'."
            nar "Ibu jarimu menyentuh ruang obrolan itu dengan ragu. Begitu terbuka, ratusan gelembung pesan dari minggu-minggu sebelumnya langsung memenuhi layar, penuh dengan sapaan manja, keluhan pura-pura minta dijemput di depan stasiun, godaan setengah serius yang menanyakan Koita sedang bersama gadis mana, hingga foto sketsa tangan Koita yang dikirim lewat tengah malam."
            nar "Setiap baris kalimat yang diketik Chiasa asli begitu intim, posesif, dan sarat dengan pengakuan cinta terselubung yang dibungkus candaan adik perempuan, hingga membacanya saja membuat bulu kudukmu meremang seperti sedang membongkar buku harian terlarang milik orang lain."
            nar "Ibu jarimu menggantung kaku di atas papan ketik layar. Bagaimana mungkin kamu bisa meniru cara bicara semanja dan seakrab ini kepada pria yang bahkan belum pernah kamu temui secara langsung?!"
            koita "Chiasa? Kamu sudah bangun, kan? Sarapannya sebentar lagi dingin, lho!"
            nar "Seruan suara laki-laki yang hangat dan akrab dari lantai bawah rumah itu mendadak menembus pintu kamar, membuat kedua bahumu tersentak keras hingga ponsel di tanganmu nyaris terlepas."
            nar "Kamu menoleh panik ke arah pintu kamar yang tertutup, lalu kembali melirik tulisan 'Ko-nii' yang terpampang di puncak layar ponselmu. Mulutmu sempat terbuka untuk membalas panggilan itu sesuai nama di layar, tetapi lidahmu mendadak kelu dan menolak mengeluarkan sebutan manja tersebut."
            nar "Kamu menelan ludah dengan kerongkongan kering, lalu buru-buru mengunci layar ponsel dan menyahut sekenanya tanpa sanggup menyematkan panggilan kakak itu di ujung kalimatmu."
            chiasa "I-iya! Aku sudah bangun... sebentar lagi aku turun!"
            nar "Suaramu terdengar sedikit tercekat di kalimat terakhir. Dari lantai bawah tidak ada kecurigaan yang langsung membalas, hanya bunyi langkah kaki yang kembali bergerak di dapur. Kamu tahu persis bahwa begitu kamu membuka pintu kamar itu dan duduk di meja makan nanti, kamu tidak bisa lagi menghindar dari keharusan memanggilnya secara langsung."
        elif _opening_key == "C":
            nar "Daripada terus terkurung di dalam kamar asing bersama suara sinting yang berbisik di dalam tengkorakmu, kamu menyibak selimut dengan gerakan cepat dan melangkah menuju pintu kamar untuk memeriksa langsung siapa yang sedang beraktivitas di lantai bawah."
            nar "Tepat ketika jemarimu baru saja menyentuh kenop pintu kayu, langkahmu mendadak terhenti di depan cermin panjang yang menempel di dinding samping lemari pakaian."
            nar "Dari balik permukaan kaca itu, seorang gadis bertubuh mungil dan ramping menatapmu balik dengan wajah oval yang pucat, sepasang mata kuning keemasan yang melebar kaku, serta rambut cokelat gelap sepunggung yang terurai agak berantakan bekas tidur."
            chiasa "{i}Wajah siapa ini...? Aku sama sekali nggak kenal gadis di cermin ini.{/i}"
            nar "Ekor matamu menangkap papan nama kayu kecil bergambar kuas lukis di pintu kamar yang bertuliskan 'Chiasa'. Nama itu terasa sedikit mengusik ingatanmu, tetapi tanpa ikatan rambut atau seragam apa pun, pikiranmu yang masih kacau belum sanggup mengaitkannya ke mana-mana."
            nar "Aroma kaldu sup miso hangat, roti panggang, dan telur goreng dari lantai bawah menarik langkahmu membuka pintu dan keluar dari kamar."
            nar "Anehnya, begitu telapak kakimu menapak di deretan tangga kayu menuju lantai satu, otot-otot tungkai tubuh ini melangkah turun dengan sangat hafal, bahkan secara otomatis melangkahi anak tangga kelima yang kayunya agak berderit tanpa perlu kamu perhatikan."
            nar "Begitu kamu tiba di ambang ruang makan lantai bawah yang terang oleh sinar matahari pagi, tampak sebuah kotak plastik biru berisi lauk kiriman di atas meja kayu."
            nar "Dan tepat di seberang meja itu, seorang pemuda berambut hitam agak berantakan berdiri mengenakan celemek di atas kaus rumahnya, sedang meletakkan piring sarapan sambil mengangkat wajah dan menyunggingkan senyum ramah tanpa pertahanan."
            koita "Pagi, Chi-chan. Rambutmu belum sempat diikat ya? Cepat duduk, makan selagi hangat sebelum dingin. Tumben sekali kamu sudah turun sebelum kupanggil dua kali."
            nar "Kamu terpaku di ambang pintu ruang makan. Wajah ramah dengan potongan rambut hitam acak-acakan yang tadi hanya berupa gambar dua dimensi yang membuatmu muak di layar ponsel, kini berdiri nyata, bernapas, dan memanggilmu dengan sebutan yang langsung menyalakan seluruh ingatanmu sekaligus."
            nar "Amamiya Koita. Itu jelas Amamiya Koita, sang MC manga 'Kouseikan'. Dan nama 'Chiasa' di pintu kamar lantai atas tadi berarti kamu benar-benar terlempar ke tubuh adik tiri tanpa hubungan darah yang tinggal satu atap dengannya!"
            nar "Kamu ingat dari halaman manga bahwa Chiasa asli selalu menyapanya dengan panggilan manja 'Ko-nii'. Di hadapan orangnya langsung, lidahmu mendadak tercekat menolak mengeluarkan sebutan itu."
            chiasa "P-pagi... aku cuma kebetulan bangun lebih awal. A-aku mau cuci muka sama rapikan rambut dulu sebentar di kamar mandi."
            koita "Haha, gugup karena hari pertama kuliah ya? Jangan lama-lama, nanti telur mata sapinya keburu dingin."
            chiasa "Iya... sebentar saja."
            nar "Koita berbalik kembali ke arah kompor tanpa sedikit pun curiga pada caramu berdiri kaku di ambang ruangan. Menjadi Chiasa di rumah ini berarti harus duduk berhadapan setiap hari dengan pria yang merasa paling mengenalmu, sementara salah bicara sedikit saja di meja makan nanti bisa langsung membongkar semuanya."
        else:
            nar "Kamu duduk membeku di tepi ranjang, mencengkeram ujung selimut kuat-kuat hingga buku-buku jarimu yang lentik memutih, dan menolak beranjak satu langkah pun."
            nar "Enak saja suara kurang ajar itu menyuruhmu berkeliling memeriksa kamar seperti pesuruh setelah menculik kesadaranmu ke tempat asing. Sebelum kamu sudi menggerakkan satu jari pun, entitas yang menyeretmu ke sini harus memberikan jawaban."
            nar "Saat kamu memutar pandangan dengan kesal ke sekeliling kamar untuk mencari celah, matamu tanpa sengaja menangkap pantulan dirimu sendiri di cermin meja rias yang berseberangan langsung dengan kasur."
            nar "Gadis pucat bermata kuning keemasan dengan rambut cokelat gelap tergerai berantakan di balik kaca itu tampak sama sekali asing bagimu. Kamu menyipitkan mata bingung, sebelum pandanganmu bergeser ke meja belajar di sebelahnya yang memajang amplop bertuliskan 'Universitas Kouseikan' bermarga 'Amamiya' serta nampan kayu berisi sehelai pita hitam rapi."
            chiasa "{i}Tunggu sebentar... Universitas Kouseikan, marga Amamiya, mata kuning keemasan, terus pita hitam yang ditaruh di nampan meja rias itu...{/i}"
            nar "Baru setelah menggabungkan nama di amplop dengan pita hitam di meja rias, ingatan tentang bab-bab manga yang baru saja kamu cibir habis-habisan di peron stasiun kereta bawah tanah menyambar kepalamu."
            chiasa "{i}Oh... pantas aja tadi waktu rambutnya masih terurai aku nggak langsung ngeh! Jangan bercanda, wajah ini kan Amamiya Chiasa dari manga 'Kouseikan'?!{/i}"
            nar "Menyadari kamu dilempar masuk ke dalam tubuh si adik tiri posesif tanpa hubungan darah di cerita harem yang paling kamu benci membuat amarahmu langsung meledak ke arah ruang kosong di depan kasur."
            chiasa "Hei, keluar lagi kamu! Kamu pikir lucu memasukkanku ke tubuh karakter manga sampah ini?! Kembalikan aku ke tubuhku sekarang juga, pengecut!"
            nar "Udara di depan wajahmu berkedip tajam. Emotikon garis di layar kaca biru itu melebarkan senyum miringnya, lalu detik berikutnya sengatan ngilu yang jauh lebih brutal menghantam pangkal lehermu hingga kamu terbungkuk di atas kasur sambil memekik tertahan."
            chiasa "Akh! Sialan, hentikan!"
            sistem "(¬_¬\") Berteriak menuntut ganti rugi seolah kau sedang memarahi kasir toko? Menggemaskan sekali, Manusia. Sayangnya kau bukan pelanggan di sini, kau cuma rongsokan peron yang kupungut~"
            nar "Sengatan listrik itu dicabut seketika, menyisakan napasmu yang terengah-engah di atas seprai dan keringat dingin yang membasahi pelipis, sementara dari lantai bawah terdengar bunyi piring beradu dan langkah kaki yang tenang di dapur."
            chiasa "Hah... hah... dasar psikopat sakit jiwa! Kamu memaksaku masuk ke tubuh gadis ini cuma buat bahan tontonanmu?!"
            sistem "( ´ v ` )~ Anggap saja aku penonton setia yang bosan melihat alur cerita yang lurus. Pemilik asli kamar ini sudah tidak ada, dan kakak kesayangannya sedang menyiapkan sarapan di bawah, jadi simpan tenagamu untuk berakting, ya~"
    return

label kk_main:
    # M01 — Hari Pertama + Hanami. Dunia dibuka; pemain menemukan N01/Mi01 sendiri
    # dengan berjalan ke lokasinya (Gedung Arsitektur, Taman Kampus) — tidak dipaksa.
    # Hari pertama diawali perjalanan/monolog adaptasi masing-masing host (dan
    # orientasi mahasiswa baru khusus Host Chiasa Tahun 1) sebelum peta bebas dibuka.
    $ kk_bulan = 1
    $ kk_slot = 0
    if kk_host == "chiasa":
        call kk_chiasa_orientation
    else:
        call kk_yutaka_commute
    $ kk_slot = 1
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
        $ _e = dict(_e, body="Di pameran dulu, Shiori bertanya sebagai pembaca. Kini Miono menerima pertanyaan yang sama, bersama salinan jawabanmu. Kali berikutnya kalian duduk membahas sampul, buku itu masih tertutup. Yang ingin Miono dengar lebih dulu adalah ceritamu tentang Shena.")
    elif code == "E-SH-07":
        $ _e = dict(_e, body="Shiori menutup map bertuliskan nama Tojo. Pertunangan itu sudah ia batalkan sendiri. Map berikutnya berisi rencana kerjanya. Kali ini, ketika ayahnya bertanya dari mana mereka harus mulai, Shiori membukanya di halaman yang ia pilih.")
    elif code == "E-CF-01":
        $ _e = dict(_e, body="Kunci rumah baru itu ada dua. Saat kalian pulang membawa dus terakhir, kau mendengar ia bertanya dari dapur di mana cangkir-cangkir disimpan. Kau belum tahu. Kalian membuka dus satu demi satu, bersama-sama.")
    scene black with fade
    call screen kk_ending_card(_e)
    return
