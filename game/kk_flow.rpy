# Kouseikan — alur. Prolog, vertical slice, pemutar event generik, Force (abstrak), evaluasi.
# Prototipe: teks hanya poin utama (awal → pilihan → akibat ringkas). Story penuh menyusul.

label kk_intro:
    scene black with fade
    call screen kk_titlecard("KOUSEIKAN", "18+ · semua tokoh dewasa")
    nar "Peron stasiun kereta bawah tanah sore itu pengap oleh udara lembap dan desakan orang-orang yang baru pulang kerja. Di tengah kebisingan itu, perhatianmu justru terpaku sepenuhnya pada layar ponsel di genggamanmu."
    nar "Di layar itu terpampang bab terbaru 'Kouseikan'—sebuah manga romansa kampus yang entah bagaimana selalu bertengger di peringkat teratas aplikasi bacaan mingguan."
    nar "Kau mendengus sinis sambil menggeser layar dengan ibu jari. Semakin jauh kau membacanya, semakin gatal rasanya ingin memaki di kolom komentar."
    nar "Bagaimana mungkin cerita sampah macam ini bisa begitu populer? Sejak bab pertama, alurnya jelas-jelas cuma mimpi basah pengarangnya yang dituangkan tanpa tahu malu."
    nar "Tokoh utamanya, Amamiya Koita, hanyalah mahasiswa sastra biasa yang modalnya cuma senyum ramah dan jawaban menggantung. Ia tidak pernah tegas menolak siapa pun dengan dalih 'tidak tega menyakiti', tetapi seluruh isi cerita memujanya seolah ia pria paling tulus di muka bumi."
    nar "Lebih parahnya lagi, gadis-gadis cantik di sekelilingnya dibuat jatuh cinta hanya karena kebaikan sepele, sementara sahabat dan orang-orang di sekitarnya direduksi menjadi figuran bodoh yang rela mengorbankan perasaan mereka demi kebahagiaan sang protagonis."
    nar "Jempolmu baru saja mengetik sepatah kalimat pedas di kolom ulasan ketika tiba-tiba jeritan melengking memecah keramaian peron."
    nar "Kau menoleh spontan dari layar ponsel. Beberapa langkah di sebelahmu, seorang anak kecil terlepas dari genggaman ibunya, terpeleset melewati garis kuning, dan jatuh tersungkur ke atas batu-batu rel."
    nar "Di ujung terowongan yang gelap, dua sorot lampu kereta ekspres sudah menyala menyilaukan. Klakson panjang meraung memekakkan telinga, disusul gemuruh roda besi yang membelah rel dengan kecepatan penuh."
    nar "Orang-orang di peron hanya menjerit kaku sambil menutup mulut—tidak ada satu pun yang berani bergerak. Panik menyergap dadamu lebih cepat daripada akal sehat; ponselmu terlepas jatuh ke lantai saat kakimu refleks melompat turun ke atas rel."
    nar "Kau merengkuh tubuh mungil yang gemetar itu dan mengangkatnya sekuat tenaga ke atas bibir peron, tepat saat beberapa tangan penumpang lain menarik kerah baju anak itu hingga selamat."
    nar "Anak itu lolos. Namun ketika kau bertumpu pada kedua tangan hendak memanjat naik, cahaya putih lampu kereta sudah menelan seluruh pandanganmu, diiringi derit rem darurat yang merobek gendang telinga."
    nar "Hantaman baja yang masif meremukkan tulang rusukmu dalam sekejap. Tubuhmu terlempar ringan seperti boneka kain sebelum dingin yang pekat menyergap."
    nar "Di detik terakhir sebelum kesadaranmu benar-benar padam, bukan rasa takut yang melintas di kepalamu, melainkan cibiran getir yang tak tertahankan."
    nar "Bisa-bisanya kau mati tertabrak kereta gara-gara menyelamatkan anak kecil—persis pembuka cerita fiksi pasaran yang belakangan ini bertebaran di mana-mana. Benar-benar klise. Menyebalkan sampai tarikan napas terakhir."
    nar "Lalu segalanya terputus menjadi hitam."
    nar "Tidak ada lagi raungan klakson atau teriakan penumpang. Tidak ada rasa sakit, tidak ada dinginnya lantai peron, bahkan tidak ada detak waktu. Kesadaranmu hanya mengapung tanpa bobot di dalam keheningan alam bawah sadar yang gelap gulita."
    nar "Entah berapa lama kau terombang-ambing di kehampaan itu, sampai perlahan-lahan kegelapan di hadapanmu mulai bergeser."
    nar "Dari balik bayangan pekat, dua buah tangan terulur menembus ruang hampa, berhenti tepat dalam jangkauanmu tanpa sepatah kata pun."
    nar "Di sebelah kiri, terulur tangan seorang pria—berjari panjang, rapi, dan terawat, namun menyiratkan kesepian dingin yang tertahan di buku-buku jarinya."
    nar "Di sebelah kanan, terulur tangan seorang wanita—ramping, lentik, dengan bekas kapalan tipis di ruas jari tengahnya, tampak anggun sekaligus keras kepala."
    nar "Kau sama sekali tidak tahu milik siapa kedua tangan itu, atau ke mana mereka akan menyeretmu pergi. Namun instingmu berbisik jelas: jika kau tidak ingin lenyap begitu saja setelah kematian konyol tadi, kau harus memilih salah satu dan menggenggamnya sekarang."
    call screen kk_route_select
    $ kk_host = _return
    $ kk_setup_state()
    call kk_prologue
    nar "Ikon wajah di layar kaca biru itu menyipitkan mata, lalu memunculkan barisan teks baru berwarna kuning menyala tepat di depan hidungmu."
    sistem "Dan karena aku tahu kau bakal malas bergerak kalau tidak dipecut, ini misi pembukamu: dalam tujuh hari ke depan, temui tiga orang yang dekat dengan Koita."
    sistem "Amati tabiat mereka, ajak bicara, dan cari tahu celah mana yang bisa kauungkit. Jangan coba-coba mengurung diri di kamar sampai tenggatnya habis—aku paling benci pemeran yang mogok kerja, dan kau sudah merasakan sendiri caraku memberi teguran."
    nar "Jendela kaca biru itu menutup dirinya paksa dengan bunyi dengung halus, meninggalkanmu bersama detak jantung yang masih memburu di tengah pagi tanggal tujuh April."
    jump kk_main

label kk_prologue:
    if kk_host == "yutaka":
        $ kk_mc_nama = "YUTAKA (kau)"
        show screen kk_set("yutaka", "Apartemen Mewah · Dini Hari")
        with fade
        nar "Begitu jemarimu menggenggam tangan pria itu, gravitasi mendadak berbalik. Sebuah tarikan kasar mengempaskan kesadaranmu jatuh menembus lorong gelap, seolah kau dilempar paksa ke dasar air."
        nar "Kau tersentak bangun dengan napas memburu. Kedua tanganmu refleks mencengkeram dada, bersiap merasakan tulang rusuk yang hancur dan darah hangat yang merembes."
        nar "Namun tidak ada luka. Yang tergenggam oleh jari-jarimu hanyalah kaus tidur berbahan katun lembut yang lembap oleh keringat dingin, membungkus bidang dada yang terasa rata, utuh, dan jauh lebih lebar dari yang kauingat."
        nar "Kau mengerjap pelan, mengatur napas sambil mengedarkan pandangan. Kau tidak sedang berbaring di aspal stasiun atau ruang gawat darurat, melainkan di atas ranjang berukuran besar di dalam kamar apartemen yang sangat luas dan sunyi."
        nar "Langit-langit beton ekspos yang tinggi, tirai jendela kaca yang menyisakan siluet gedung kota saat dini hari, serta dengung halus pendingin udara membuat keningmu berkerut dalam."
    else:
        $ kk_mc_nama = "CHIASA (kau)"
        show screen kk_set("chiasa", "Rumah Amamiya · Pagi")
        with fade
        nar "Begitu jemarimu menggenggam tangan wanita itu, gravitasi mendadak berbalik. Sebuah tarikan kasar mengempaskan kesadaranmu jatuh menembus lorong gelap, seolah kau dilempar paksa ke dasar air."
        nar "Kau tersentak bangun dengan napas memburu. Kedua tanganmu refleks mencengkeram dada, bersiap merasakan tulang rusuk yang remuk dihantam baja kereta."
        nar "Namun tidak ada rasa sakit maupun darah. Yang tersentuh oleh telapak tanganmu justru kain piyama yang lembut, lekuk tubuh yang terasa ringan dan asing, serta aroma sabun bunga yang menguar dari selimut hangat."
        nar "Saat kau menunduk dengan napas tersengal, beberapa helai rambut panjang berwarna gelap merosot melewati bahumu dan menggelitik pipi."
        nar "Kau mengerjap keras menatap sekeliling. Cahaya matahari pagi menembus tirai tipis sebuah kamar yang rapi, menerangi meja rias kayu, deretan kuas cat, dan peralatan gambar di sudut ruangan."
    nar "Belum sempat otakmu mencerna di mana kau berada, bunyi derik statis yang tajam tiba-tiba berdenging di dalam telingamu."
    nar "Udara kosong di depan wajahmu berkedip. Sebuah jendela kaca biru transparan membuka diri begitu saja di ruang pandangmu, menampilkan ikon wajah sederhana dari garis-garis cahaya yang menyunggingkan senyum miring."
    sistem "Bangun juga akhirnya. Kukira jiwamu ikut penyok tertabrak kereta tadi, Sampah Peron."
    nar "Suara itu bergema langsung di dalam tengkorakmu—bernada rendah, ceria secara dibuat-buat, dan terdengar begitu menyebalkan hingga kau refleks mengibaskan tangan untuk menepis layar biru itu."
    nar "Tanganmu menembus cahaya kaca itu seperti menyapu asap. Kau mundur merapat ke kepala ranjang dengan mata melebar."
    if kk_host == "yutaka":
        yutaka "Suara apa itu—?! Siapa yang bicara?!"
        nar "Kau tertegun setengah detik mendengar suara bariton yang keluar dari tenggorokanmu sendiri, sebelum rasa jengkel mengalahkan keterkejutanmu."
        yutaka "Hei! Kau dengar aku, kan?! Proyektor macam apa ini—keluar dan tunjukkan wajahmu!"
    else:
        chiasa "Suara apa itu—?! Siapa yang memasang layar ini?!"
        nar "Kau tertegun setengah detik mendengar suara perempuan yang jernih dan ringan keluar dari tenggorokanmu sendiri, sebelum rasa marah mengalahkan keterkejutanmu."
        chiasa "Hei! Jangan bersembunyi di balik layar konyol itu—keluar dan jelaskan apa yang kaulakukan padaku!"
    nar "Ikon garis wajah di layar biru itu memutar matanya dengan gerakan patah-patah yang mengejek. Detik berikutnya, sengatan nyeri seperti jarum listrik menusuk pelipismu hingga kau meringis memegangi kepala."
    sistem "Berisik sekali. Itu barusan bukti kecil supaya kau tidak buang-buang waktuku dengan mengira ini mimpi atau halusinasi rumah sakit."
    sistem "Tubuh lamamu sudah jadi daging giling di atas rel kereta, Tuan Rumah. Yang kaupakai bernapas sekarang adalah tubuh pinjaman dariku—dan pemilik aslinya sudah tidak ada lagi di dalam sana."
    if kk_host == "yutaka":
        yutaka "Tubuh pinjaman...? Kau pikir aku bakal percaya begitu saja pada ocehan benda mencurigakan di kepalaku?!"
        nar "Tepat saat kau menggeram kesal, ponsel pintar di atas nakas sebelah ranjang bergetar singkat, menyalakan layar yang menampilkan pengingat pagi beserta nama kontak 'Koita', sementara di meja tamu tampak sebuah dompet kulit dan pintu kamar mandi yang sedikit terbuka."
    else:
        chiasa "Tubuh pinjaman...? Kau pikir aku bakal percaya begitu saja pada klaim gila dari suara di kepalaku?!"
        nar "Tepat saat kau mendesis kesal, dari lantai bawah rumah ini terdengar bunyi piring beradu dan langkah kaki seseorang di dapur, sementara di sekeliling kamarmu tampak cermin meja rias, buku sketsa yang terbuka, serta sebuah ponsel yang sedang diisi dayanya di nakas."
    sistem "Tidak percaya? Silakan saja periksa sendiri kamar ini. Kau punya kaki, mata, dan barang-barang pemilik tubuh itu di dekatmu, kan? Cari tahu sendiri kau sedang menjadi siapa sekarang, sebelum kita bicara soal harga sewa nyawamu."
    call kk_first_morning
    nar "Tepat ketika kau masih berusaha menelan kenyataan gila tentang identitas barumu, jendela kaca biru itu kembali meluncur turun di depan wajahmu."
    nar "Ikon wajah di layarnya membentuk tepuk tangan lambat yang sarat ejekan."
    sistem "Selamat atas pencerahannya, Tuan Rumah. Ekspresi terkejutmu barusan benar-benar layak dijadikan pembuka pagi."
    if kk_host == "yutaka":
        yutaka "Kau... kau sengaja memasukkanku ke dalam manga sampah yang baru kubaca sebelum mati?! Sebagai Kisaragi Yutaka pula?! Apa maumu sebenarnya, brengsek?!"
    else:
        chiasa "Kau... kau sengaja memasukkanku ke dalam manga sampah yang baru kuhina sebelum mati?! Di tubuh Amamiya Chiasa pula?! Otakmu sudah miring, hah?!"
    sistem "Justru karena kau begitu membenci manga ini, kau adalah kandidat paling cocok untukku. Panggil aku Sistem—dan mulai detik ini, kontrakmu resmi aktif."
    sistem "Aturannya sangat sederhana: kau punya waktu tiga tahun sampai Amamiya Koita lulus kuliah untuk menyimpangkan takdir romantisnya sejauh mungkin dari jalur asli."
    sistem "Evaluasinya hanya dilakukan satu kali, tepat saat ia menerima ijazah wisuda. Kalau sampai hari itu skenario romansa sang protagonis masih berjalan mulus... jantung barumu akan kubuat berhenti berdetak di tempat."
    if kk_host == "yutaka":
        yutaka "Jangan bercanda! Kenapa aku harus ikut campur mengurus urusan ranjang dan percintaan si protagonis naif itu pakai taruhan nyawa segala?!"
    else:
        chiasa "Jangan gila! Kenapa nyawaku harus digantungkan pada urusan cinta kakak tiri menyebalkan itu?!"
    nar "Layar biru itu berkedip merah selama sepersekian detik, memancarkan tekanan dingin yang membuat tengkukmu meremang."
    sistem "Karena hidup keduamu adalah milikku. Bagaimana caramu merusak takdirnya, siapa yang kaurangkul atau kauhancurkan, dan seperti apa kepribadianmu di balik topeng tubuh itu? Bukan urusanku menebaknya sekarang."
    sistem "Simpan keluhan moralmu, Tuan Rumah. Aku akan menilai siapa kau sebenarnya dari apa yang kaulakukan, bukan dari seberapa keras kau memakiku."
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
    if kk_host == "yutaka":
        $ _actions = ["Bongkar isi dompet dan ponselnya.", "Hampiri cermin kamar mandi untuk memastikan.", "Langsung telepon Koita sekarang juga.", "Duduk membisu menuntut penjelasan."]
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
            nar "Kau menyibak selimut dan menurunkan kaki dari ranjang. Langkah pertamamu terasa ganjil karena tungkai yang lebih panjang dari biasanya, namun kau memaksakan diri berjalan ke meja kaca di tengah ruang tamu."
            nar "Jika suara di kepalamu tadi tidak berbohong soal tubuh pinjaman, maka dompet kulit hitam dan ponsel yang tergeletak di sana adalah petunjuk paling nyata."
            nar "Kau menyambar dompet itu dan membukanya. Di balik deretan kartu debit prioritas dan uang tunai, terselip selembar kartu tanda mahasiswa bertuliskan 'Universitas Kouseikan — Fakultas Ekonomi dan Bisnis'."
            yutaka "...Universitas Kouseikan? Tunggu dulu, kenapa nama kampusnya terdengar tidak asing?"
            nar "Keningmu berkerut. Kau menarik kartu itu keluar, memperhatikan pasfoto seorang pemuda berambut gelap agak berantakan dengan tatapan santai, lalu membaca nama yang tercetak di sebelahnya: Kisaragi Yutaka."
            nar "Saat kau meraih ponsel di atas meja, kaca layarnya yang masih gelap memantulkan wajahmu sendiri—garis rahang yang sama, rambut yang sama, dan mata yang persis dengan foto di kartu tersebut."
            nar "Potongan ingatan tentang halaman manga yang baru kubaca di peron stasiun tadi mendadak menyambung di kepalamu."
            yutaka "Ahhh...?! Tunggu—wajah ini kan Kisaragi Yutaka?! Sahabat kaya si protagonis di manga 'Kouseikan'?!"
            nar "Dengan napas tercekat, kau menempelkan ibu jari ke pemindai ponsel hingga kuncinya terbuka. Aplikasi bank di layar menampilkan angka yang membuatmu terbelalak: saldo yang bisa kaugunakan hari ini [_balance], lengkap dengan catatan transfer otomatis seratus lima puluh ribu yen dari orang tuanya."
            nar "Kau menggulir ke aplikasi pesan. Ada pesan singkat yang dingin dari 'Kisaragi Reiko' tanpa sapaan ibu, obrolan grup yang ramah, serta satu draf pesan yang belum terkirim di ruang obrolan 'Amamiya Chiasa' yang mengajak gadis itu makan berdua."
            nar "Kau menelan ludah menatap layar itu. Kau benar-benar terlempar ke tubuh si sahabat figuran yang kesepian—dan seluruh kekayaan di rekening ini sama sekali tidak memberimu ingatan tentang cara menjadi orang yang mereka kenal."
        elif _opening_key == "B":
            nar "Kau menolak memercayai klaim bahwa tubuh aslimu sudah hancur sebelum melihatnya dengan mata kepalamu sendiri. Dengan langkah yang masih agak goyah, kau bangkit dari kasur dan mendorong pintu kamar mandi dalam."
            nar "Jarimu meraba dinding keramik dan menekan sakelar. Lampu putih di atas wastafel menyala terang, langsung memantulkan sosok seorang pria muda di cermin."
            nar "Kau membeku di depan wastafel. Pria di balik kaca itu memiliki bekas lipatan bantal di pipi kirinya, napas yang memburu, dan sorot mata penuh ketakutan. Saat kau mengangkat tangan menyentuh dagu, pantulan itu melakukan gerakan yang persis sama."
            yutaka "Wajah orang lain... Aku benar-benar ada di tubuh orang lain."
            nar "Kau mencondongkan badan lebih dekat ke cermin, mengamati potongan rambut hitamnya yang modis namun berantakan serta garis wajahnya yang tampan. Semakin lama kau menatapnya, semakin kuat rasa ganjil yang menggelitik ingatanmu."
            yutaka "Tunggu sebentar... kenapa wajah ini kelihatan familier sekali? Aku yakin pernah melihat proporsi wajah dan gaya rambut seperti ini..."
            nar "Matamu melirik jaket almamater yang tergantung di balik pintu kamar mandi dengan bordir nama 'Kouseikan — Kisaragi', lalu kembali menatap cermin. Seketika, gambar-gambar dari layar ponselmu di stasiun kereta tadi menghantam ingatanmu."
            yutaka "Ahhh!! Wajah ini kan... Kisaragi Yutaka?!"
            nar "Kau mencengkeram pinggiran wastafel hingga buku jarimu memutih. Ini wajah sahabat masa kecil Amamiya Koita dari manga 'Kouseikan'—sosok pria santai yang selalu berdiri setengah langkah di belakang sang protagonis sambil memendam cinta sendirian pada adik tiri Koita, Chiasa!"
            nar "Di cermin, pori-pori kulit yang berkeringat dingin dan detak nadi di lehermu yang memburu—hal-hal kecil yang tidak pernah digambar pengarangnya—membuat kenyataan ini terasa mengerikan."
        elif _opening_key == "C":
            nar "Pandanganmu terpaku pada ponsel di nakas yang baru saja bergetar. Nama 'Koita' yang muncul di layar pengingat itu membuat dadamu terasa dingin—terlalu kebetulan jika dibandingkan dengan nama tokoh manga yang baru saja kaumaki di stasiun."
            nar "Kau meraih ponsel itu dari kabel pengisi daya. Sebelum kau menyentuh tombol apa pun, permukaan kaca hitamnya memantulkan wajah seorang pemuda asing dengan rambut agak berantakan."
            nar "Pemindai wajah otomatis membuka kunci layar, langsung menampilkan halaman kontak dengan profil pemilik ponsel di bagian paling atas: 'Kisaragi Yutaka — Universitas Kouseikan'."
            yutaka "Kouseikan...? Kisaragi Yutaka...? Tunggu dulu..."
            nar "Kau membandingkan pantulan wajahmu di sudut layar dengan foto profil itu, dan seketika darahmu terasa berdesir hebat."
            yutaka "Ahhh...?! Wajah ini kan—Kisaragi Yutaka?! Sahabat karib Amamiya Koita di manga tadi?!"
            nar "Seolah didorong kepanikan untuk membuktikan bahwa ini cuma lelucon gila, ibu jarimu langsung menekan tombol panggil pada nama 'Koita' di bawahnya."
            nar "Nada sambung baru berdering satu kali ketika panggilan itu diangkat dari seberang, bahkan sebelum kau sempat menyiapkan alasan."
            koita "Halo, Yutaka? Tumben bangun pagi-pagi begini. Kita tetap jadi berangkat kuliah bareng dari depan stasiun, kan?"
            nar "Suara itu terdengar begitu nyata—ramah, sedikit mengantuk, dan penuh keakraban tanpa curiga. Mendengar protagonis manga itu berbicara langsung di telingamu membuat lidahmu kelu."
            yutaka "A-ah... soal itu, kepalaku agak pusing pagi ini. Nanti kukabari lagi sebentar ya, Koita."
            koita "Eh, kau nggak apa-apa? Jangan dipaksa kalau belum enak badan. Kabari saja nanti, ya."
            nar "Sambungan terputus. Kau menurunkan ponsel perlahan dengan napas tertahan; bukan hanya dunia ini benar-benar nyata, tetapi Koita juga memercayai setiap kata dari mulut tubuh ini tanpa keraguan sedikit pun."
        else:
            nar "Kau meremas seprai kasur kuat-kuat dan menolak beranjak satu langkah pun. Enak saja suara sialan itu menyuruhmu jalan-jalan memeriksa kamar setelah menculik kesadaranmu ke tempat asing."
            nar "Namun saat kau mendongak hendak memaki layar biru itu lagi, tatapanmu tanpa sengaja menangkap pantulan dirimu di cermin lemari pakaian yang berseberangan dengan ranjang, tepat di sebelah rak televisi yang memajang foto masa kecil empat sekawan di festival."
            nar "Kau menghentikan napas, menyipitkan mata menatap pemuda di cermin dan gadis kecil berpita hitam di dalam bingkai foto tersebut."
            yutaka "Tunggu dulu... potret festival itu... dan wajah pria di cermin itu..."
            nar "Ingatan tentang bab-bab manga yang baru kaucibir di peron stasiun berkelebat cepat di kepalamu."
            yutaka "Ahhh?! Tunggu—wajah ini kan Kisaragi Yutaka dari manga 'Kouseikan'?!"
            nar "Menyadari kau dilempar ke dalam tubuh pemeran pembantu kaya yang kesepian di apartemen seluas ini membuat amarahmu langsung meledak ke arah ruang kosong di depan ranjang."
            yutaka "Hei, keluar lagi kau! Kau pikir lucu memasukkanku ke tubuh figuran manga sampah?! Kembalikan aku sekarang juga, pengecut!"
            nar "Udara di depan wajahmu berkedip tajam. Alih-alih menjawab dengan sopan, dengung frekuensi tinggi mendadak menghantam telingamu, disusul rasa ngilu yang buas di belakang mata hingga kau terbungkuk memegangi kening."
            yutaka "Argh—sialan! Hentikan!"
            sistem "Menuntut pelayanan sambil berteriak seolah kau pelanggan raja di restoran? Nyalimu lumayan juga, Tuan Rumah, sayang sekali otakmu tertinggal di bawah roda kereta."
            nar "Rasa sakit itu dicabut seketika, menyisakan napasmu yang terengah-engah di atas kasur dengan keringat dingin membasahi tengkuk."
            yutaka "Hah... hah... dasar psikopat sakit jiwa! Kau memungutku cuma buat dijadikan bahan tontonanmu?!"
            sistem "Aku lebih suka disebut sutradara yang murah hati. Mesin pendingin apartemen mewah ini masih menyala, kota di balik jendela itu terus berjalan, dan kau masih hidup. Jadi berhentilah merengek sebelum kutambah dosis perkenalannya."
    else:
        if _opening_key == "A":
            nar "Kau menyibak selimut dan menurunkan kaki ke atas karpet kamar. Begitu berdiri, keseimbanganmu sempat goyah; titik berat tubuh ini terasa jauh lebih ringan dan pendek, sementara helai-helai rambut panjang bergeser lembut di sepanjang punggungmu."
            nar "Dengan perasaan waswas, kau melangkah mendekati meja rias kayu di sudut kamar dan berdiri tepat di hadapan cerminnya."
            nar "Dari balik kaca, seorang gadis cantik berwajah oval menatapmu balik dengan mata kuning keemasan yang melebar kaku. Rambut cokelat gelapnya jatuh sepunggung dalam potongan berlapis, poni menyampingnya membingkai dahi, dan separuh rambut atasnya terikat rapi dengan pita hitam."
            chiasa "...Siapa gadis ini? Tunggu... mata keemasan dan rambut cokelat gelap dengan pita hitam..."
            nar "Saat kau menghela napas gugup, tangan kananmu bergerak sendiri karena refleks otot—naik ke belakang kepala untuk merapikan simpul pita hitam itu, lalu menyentuh anting kecil dan kalung tipis di leher."
            nar "Gerakan khas itu langsung memicu ingatanmu tentang ilustrasi sampul manga yang baru saja kubaca di peron stasiun."
            chiasa "Ahhh!! Wajah ini kan... Amamiya Chiasa?!"
            nar "Kau menutup mulutmu dengan kedua tangan, terperanjat mendengar suara jernih dan sedikit manja yang keluar dari kerongkonganmu. Tidak salah lagi: ini Amamiya Chiasa, adik tiri tanpa hubungan darah di manga 'Kouseikan' yang diam-diam terobsesi pada kakaknya sendiri!"
            nar "Pandanganmu beralih cepat ke meja belajar di sebelah cermin. Sebuah buku sketsa tebal untuk kuliah Seni Rupa tergeletak terbuka, memamerkan gambar-gambar anatomi dan ilustrasi karakter yang sangat hidup dengan tanda tangan pena 'Shena' di sudut bawah."
            chiasa "Kalau refleks tubuhnya masih tertinggal di tanganku... jangan-jangan keahlian menggambarnya juga masih ada?"
            nar "Kau menarik kursi dan memungut pensil mekanik. Jemari lentikmu langsung mengapit batang pensil di lekukan yang tepat, tetapi begitu kau mencoba menarik garis di sudut kertas yang kosong, goresannya justru miring, kaku, dan patah saat kautekan."
            nar "Kau menatap serbuk grafit itu dengan tengkuk dingin. Tangan ini memang tangan Chiasa, tetapi bakat melukis yang menjadi kebanggaannya sama sekali tidak ikut diwariskan kepadamu."
        elif _opening_key == "B":
            nar "Kau menggeser tubuh ke tepi kasur dan meraih ponsel pintar yang masih terhubung ke pengisi daya di nakas. Jika kau ingin tahu di kamar siapa kau terbangun, benda ini pasti menyimpan jawabannya."
            nar "Saat kau mengangkat ponsel itu ke depan wajah, permukaan layarnya yang hitam memantulkan sepasang mata kuning keemasan dan rambut cokelat gelap berpita hitam—dan detik berikutnya, sensor pemindai wajah langsung membuka kunci layar tanpa meminta sandi."
            nar "Kau mengerjap menatap halaman utama ponsel itu. Di sudut atas aplikasi kampus dan galeri foto, tertulis jelas identitas pemiliknya: 'Amamiya Chiasa — Fakultas Seni Rupa dan Desain'."
            chiasa "Amamiya...? Tunggu sebentar, marga Amamiya dengan mata kuning dan pita hitam..."
            nar "Ingatan tentang bab manga yang baru saja kaucibir di stasiun kereta langsung menyambar kepalamu."
            chiasa "Ahhh...?! Wajah ini kan—Amamiya Chiasa?! Adik tiri si protagonis di manga 'Kouseikan'?!"
            nar "Dengan jari gemetar, kau membuka aplikasi di dalamnya satu per satu. Aplikasi bank mencatat saldo empat ratus ribu yen dari uang saku dan royalti pasif ilustrasi novel ringan atas nama pena 'Shena', sementara surel editornya memastikan belum ada kewajiban gambar baru."
            nar "Di aplikasi pesan, ada obrolan heboh dari teman sejurusan bernama Haruka yang mengagumi karya 'Shena-sensei', serta pesan semalam dari ibu tirinya, Amamiya Yoshie, yang menanyakan kabar dari luar kota."
            nar "Namun ruang obrolan yang disematkan paling atas hanya satu: 'Ko-nii'. Saat kau membukanya, ratusan pesan manja dan godaan setengah serius dari Chiasa kepada kakak tirinya memenuhi layar—begitu intim hingga membacanya terasa seperti mengintip surat rahasia."
            koita "Chiasa? Kau sudah bangun? Sarapannya sebentar lagi dingin, lho!"
            nar "Suara panggilan laki-laki dari lantai bawah membuat bahumu tersentak. Sebelum kau sempat mengetik balasan apa pun, pita suaramu refleks menyahut dengan nada manja yang membuatmu bergidik sendiri."
            chiasa "I-iya, Ko-nii! Sebentar lagi aku turun!"
        elif _opening_key == "C":
            nar "Daripada terkurung di kamar bersama suara sinting di kepalamu, kau menyibak selimut dan melangkah cepat menuju pintu untuk memeriksa siapa yang sedang beraktivitas di lantai bawah."
            nar "Namun tepat saat kau hendak memutar kenop pintu, langkahmu terhenti di depan cermin panjang yang menempel di dinding samping lemari."
            nar "Dari balik kaca, seorang gadis bertubuh mungil dengan mata kuning keemasan dan rambut cokelat gelap sepunggung yang diikat pita hitam menatapmu balik dengan wajah pucat."
            chiasa "Tunggu dulu... wajah gadis ini... kenapa rasanya aku baru saja melihatnya?"
            nar "Jari tanganmu tanpa sadar terangkat menyentuh pita hitam di rambutmu, sementara matamu menangkap papan nama kayu bergambar kuas lukis di pintu kamar yang bertuliskan 'Chiasa'."
            chiasa "Ahhh!! Wajah ini kan... Amamiya Chiasa?! Adik tiri dari manga 'Kouseikan' yang baru kubaca di stasiun tadi?!"
            nar "Belum sempat keterkejutan itu reda, aroma roti panggang dan sup miso hangat dari bawah menarik langkahmu keluar kamar. Anehnya, kakimu menuruni tangga kayu dengan sangat hafal, otomatis melangkahi anak tangga kelima yang agak berderit."
            nar "Di ruang makan lantai bawah, kotak lauk kiriman dari Yoshie tampak tergeletak di meja, dan tepat di seberangnya, Amamiya Koita berdiri mengenakan celemek sambil mengangkat wajah dan tersenyum ramah."
            koita "Pagi, Chi-chan. Cepat duduk, makan selagi hangat sebelum dingin. Tumben kau turun sebelum kupanggil dua kali."
            nar "Wajah itu persis seperti protagonis manga yang selalu membuatmu kesal, kini bernapas nyata di hadapanmu. Kau menarik kursi sambil berusaha mengendalikan ekspresimu."
            chiasa "P-pagi, Ko-nii... aku cuma kebetulan bangun lebih awal."
            koita "Haha, gugup karena hari pertama kuliah di Seni Rupa, ya? Nih, makan dulu telur gulungnya."
            nar "Koita menggeser piring ke depanmu tanpa sedikit pun curiga pada caramu memperhatikan kursimu sendiri. Menjadi Chiasa di rumah ini berarti harus duduk berhadapan dengan pria yang merasa paling mengenalmu, sementara salah bicara sedikit saja bisa membongkar semuanya."
        else:
            nar "Kau duduk membeku di tepi ranjang, mencengkeram ujung selimut dan menolak beranjak. Sebelum kau sudi menggerakkan satu jari pun di kamar ini, entitas kurang ajar yang menyeretmu ke sini harus memberikan jawaban."
            nar "Saat kau memutar pandangan dengan kesal ke sekeliling kamar, matamu menangkap pantulan dirimu sendiri di cermin meja rias tepat di seberang kasur, berdampingan dengan jadwal kuliah Seni Rupa, buku sketsa terbuka, dan nampan pita hitam cadangan."
            nar "Kau terdiam sejenak, menyipitkan mata melihat mata kuning keemasan dan rambut cokelat gelap half-up berpita hitam di kaca tersebut."
            chiasa "Tunggu sebentar... mahasiswi tahun pertama seni rupa... pita hitam... dan wajah itu..."
            nar "Ingatan tentang bab manga yang baru kaucibir habis-habisan di peron stasiun langsung menghantam benakmu."
            chiasa "Ahhh...?! Jangan bercanda—wajah ini kan Amamiya Chiasa dari manga 'Kouseikan'?!"
            nar "Menyadari kau dilempar masuk ke tubuh si adik tiri posesif di cerita harem yang paling kaubenci membuat emosimu langsung meledak ke arah ruang kosong di depan kasur."
            chiasa "Hei, keluar kau! Kau pikir lucu memasukkanku ke tubuh karakter manga sampah ini?! Kembalikan aku ke tubuhku sekarang juga, pengecut!"
            nar "Udara di depan wajahmu berkedip tajam. Ikon wajah di layar kaca biru itu melebarkan senyum miringnya, lalu detik berikutnya sengatan ngilu yang brutal menghantam pangkal lehermu hingga kau terbungkuk di atas kasur sambil memekik tertahan."
            chiasa "Akh—! Sialan, hentikan!"
            sistem "Berteriak menuntut ganti rugi seolah kau sedang memarahi kasir toko? Menggemaskan sekali, Tuan Rumah. Sayangnya kau bukan pelanggan di sini—kau cuma rongsokan peron yang kupungut."
            nar "Sengatan itu berhenti seketika, menyisakan napasmu yang memburu dan keringat dingin di pelipis, sementara dari lantai bawah terdengar bunyi piring dan langkah kaki di dapur."
            chiasa "Hah... hah... dasar psikopat sakit jiwa! Kau memaksaku masuk ke tubuh gadis ini cuma buat tontonanmu?!"
            sistem "Anggap saja aku penonton setia yang bosan melihat alur cerita yang lurus. Pemilik asli kamar ini sudah tidak ada, dan kakak kesayangannya sedang menyiapkan sarapan di bawah—jadi simpan tenagamu untuk berakting."
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
    scene black with Dissolve(0.7)
    call screen kk_titlecard("…")
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
    sistem "Mari kita hitung. Apa yang sudah kau ubah dari takdirnya?"
    $ _slides = kk_epilogue()
    $ _slide = 0
    while _slide < len(_slides):
        call kk_show_ending(_slides[_slide])
        $ _slide += 1
    return

label kk_show_ending(code):
    $ _e = kk_ending_data(code)
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