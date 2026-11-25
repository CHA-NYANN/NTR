# Bagian 1 (ACC) — Pembuka `kk_prologue` & `C01` (Paruh 1: Cabang A & Cabang B)

- **Alur:** `M01a` Host Chiasa (`C01` → `C02` → `K01` → `N01`)
- **File Target:** `game/kk_flow.rpy` (`kk_intro` sampai `call screen kk_route_select` menggunakan versi yang diperbaiki langsung oleh pengguna; setelah memilih tangan, masuk ke pembuka `label kk_prologue` host Chiasa & `label kk_first_morning` Cabang A dan B di bawah ini).
- **Status:** **ACC (Disetujui)**

---

## Teks Naskah Ren'Py (Bagian 1 — Disetujui)

```renpy
# [Di dalam label kk_prologue — game/kk_flow.rpy]
    else:
        $ kk_mc_nama = "CHIASA (kau)"
        show screen kk_set("chiasa", "Rumah Amamiya · Pagi")
        with fade
        nar "Begitu jemarimu menggenggam tangan wanita itu di dalam kehampaan, gravitasi mendadak berbalik arah. Sebuah sentakan keras merenggut kesadaranmu turun menembus lorong gelap yang pengap, seolah tubuhmu diikat batu dan dilempar paksa ke dasar air yang tak bertepi."
        nar "Gema derit rem baja dan raungan klakson kereta ekspres masih memekakkan telinga batinmu ketika kau tersentak bangun dengan tarikan napas panjang yang memburu."
        nar "Kedua tanganmu refleks mencengkeram bagian tengah dadamu kuat-kuat. Otot-ototmu menegang hebat, bersiap menyambut rasa ngilu dari tulang rusuk yang remuk dihantam moncong lokomotif serta rembesan darah panas di atas batu rel."
        nar "Rasa sakit yang kamu antisipasi itu sama sekali tidak datang. Dadamu terasa utuh dan hangat, jauh dari dinginnya kerikil peron kereta bawah tanah."
        nar "Yang tersentuh oleh telapak tanganmu justru permukaan kain piyama katun yang halus dan kering, membungkus lekuk dada serta tulang rusuk yang terasa utuh, ringan, dan sama sekali bukan ukuran tubuhmu sendiri."
        nar "Dadanya naik-turun dengan irama napas yang pendek dan cepat. Dari lipatan selimut tebal yang menutup pinggangmu, menguar aroma sabun mandi berwangi bunga lembut yang bercampur samar dengan bau kayu pinus serta cat akrilik kering."
        nar "Saat kau menunduk dengan napas yang masih tersengal-sengal di kerongkongan, beberapa helai rambut panjang berwarna cokelat gelap merosot melewati bahumu, menyapu tulang selangka dan menggelitik kulit pipimu yang dingin oleh keringat."
        nar "Kau mengerjap keras berkali-kali, memaksa mata yang terasa perih oleh cahaya untuk mengenali ruang di sekelilingmu."
        nar "Sinar matahari pagi awal musim semi menembus tirai tipis berwarna gading di jendela sebelah kanan, membiaskan debu-debu halus yang melayang di atas lantai kayu dan karpet rajut bundar."
        nar "Kamar ini tertata rapi namun penuh dengan jejak kesibukan seseorang: sebuah meja rias kayu berdiri di sudut dekat lemari, bersebelahan dengan meja belajar lebar yang dipenuhi tabung kuas, deretan botol tinta gambar, kaleng pensil, serta papan sketsa kayu."
        nar "Setiap sudut ruangan ini berteriak bahwa tempat ini milik seorang gadis muda—dan kau sama sekali tidak pernah menginjakkan kaki di dalamnya seumur hidupmu."
    nar "Belum sempat otakmu yang masih pening merangkai satu pun penjelasan masuk akal, bunyi derik statis seperti radio rusak tiba-tiba menyambar langsung di dalam rongga telingamu."
    nar "Udara kosong sekitar setengah meter di depan wajahmu bergetar dan berkedip dua kali. Tanpa proyektor maupun layar fisik, sebuah jendela kaca biru transparan membuka diri begitu saja di ruang pandangmu, menampilkan deretan teks dan emotikon garis cahaya neon yang menyunggingkan senyum miring."
    sistem "( ´ v ` )/ Bangun juga akhirnya~ Kukira jiwamu ikut penyok terlindas roda kereta tadi, Sampah Peron."
    nar "Suara itu tidak datang dari arah pintu maupun jendela, melainkan bergema langsung di balik tulang tengkorakmu—bernada rendah, ceria secara dibuat-buat, dan sarat dengan nada mengejek yang membuat darahmu mendidih seketika."
    nar "Kau refleks mengayunkan tangan kananmu ke depan untuk menepis panel cahaya itu jauh-jauh dari wajahmu."
    nar "Namun jemarimu hanya menembus bidang kaca biru itu seperti membelah kepulan asap dingin. Kau tersentak mundur hingga punggungmu menghantam sandaran kepala ranjang dengan mata melebar."
    if kk_host == "yutaka":
        yutaka "Suara apa itu—?! Siapa yang bicara?!"
        nar "Kau tertegun setengah detik mendengar suara bariton yang keluar dari tenggorokanmu sendiri, sebelum rasa jengkel mengalahkan keterkejutanmu."
        yutaka "Hei! Kau dengar aku, kan?! Proyektor macam apa ini—keluar dan tunjukkan wajahmu!"
    else:
        chiasa "Suara apa itu—?! Siapa yang memasang layar ini di depanku?!"
        nar "Kalimat itu terputus di ujung lidahmu sendiri. Kau membeku selama satu detak jantung penuh, meraba pangkal tenggorokanmu yang terasa ramping dan asing."
        nar "Suara yang baru saja memantul di dinding kamar ini adalah suara seorang perempuan muda—jernih, ringan, sedikit bernada tinggi di ujung kalimat, namun tetap tajam oleh kepanikanmu."
        chiasa "Suaraku... tunggu, kenapa suaraku berubah seperti ini?! Hei! Jangan bersembunyi di balik layar konyol itu—keluar dan jelaskan apa yang kaulakukan padaku!"
    nar "Ikon emotikon di layar biru itu memutar kedua matanya dengan animasi patah-patah yang tampak sengaja dibuat untuk memancing emosi. Detik berikutnya, sengatan nyeri setajam jarum listrik bertegangan tinggi menusuk lurus ke balik pelipismu hingga kau terpekik dan mencengkeram kepala dengan kedua tangan."
    sistem "(¬_¬ ) Berisik sekali. Itu barusan bukti kecil supaya kau tidak membuang waktuku yang berharga dengan mengira ini cuma mimpi buruk atau efek obat bius di ruang gawat darurat."
    sistem "Tubuh lamamu sudah selesai jadi daging giling di atas rel stasiun, Manusia (´• v •`). Yang sedang kaupakai menghirup oksigen sekarang adalah tubuh pinjaman dariku—dan kesadaran pemilik aslinya sudah tidak ada lagi di dalam sana~"
    if kk_host == "yutaka":
        yutaka "Tubuh pinjaman...? Kau pikir aku bakal percaya begitu saja pada ocehan benda mencurigakan di kepalaku?!"
        nar "Tepat saat kau menggeram kesal, ponsel pintar di atas nakas sebelah ranjang bergetar singkat, menyalakan layar yang menampilkan pengingat pagi beserta nama kontak 'Koita', sementara di meja tamu tampak sebuah dompet kulit dan pintu kamar mandi yang sedikit terbuka."
    else:
        chiasa "Tubuh pinjaman...? Pemilik aslinya sudah tidak ada?! Kau pikir aku bakal menelan klaim sinting dari suara tak jelas di kepalaku?!"
        nar "Denyut ngilu di pelipismu perlahan mereda, menyisakan napasmu yang memburu kasar di sela gigi yang terkatup rapat."
        nar "Tepat pada saat keheningan kamar itu kembali turun, dari lantai bawah rumah ini terdengar bunyi denting piring keramik yang beradu dengan permukaan meja, disusul desis air mendidih dari teko dan langkah kaki seseorang yang berjalan tenang di dapur."
        nar "Di dalam kamarmu sendiri, pantulan samar dari cermin meja rias di sudut ruangan, buku sketsa tebal yang terbuka di meja belajar, serta sebuah ponsel pintar yang terhubung ke kabel pengisi daya di atas nakas seolah menantangmu untuk membuktikan sendiri ucapan suara tersebut."
    sistem "(¬v¬) Tidak percaya? Silakan saja periksa sendiri kamar ini. Kau punya kaki, mata, dan barang-barang pemilik tubuh itu di dekatmu, kan? Cari tahu sendiri kau sedang menjadi siapa sekarang, sebelum kita bicara soal harga sewa nyawamu~ (^_~)-*"
    call kk_first_morning

# [Di dalam label kk_first_morning (C01 Cabang A & Cabang B) — game/kk_flow.rpy]
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
            chiasa "Tunggu sebentar... Universitas Kouseikan, mata kuning keemasan, marga Amamiya, ditambah pita hitam di meja rias itu... pantas aja tadi waktu rambutnya masih terurai bangun tidur aku nggak langsung ngeh! Jangan bercanda, aku beneran di tubuh adik tirinya si MC... Amamiya Chiasa?!"
            nar "Kamu refleks membekap mulutmu sendiri dengan kedua telapak tangan, mundur setengah langkah dari meja hingga betismu menyentuh kursi kayu."
            nar "Dari sekian banyak orang di dunia fiksi itu, kamu justru dilempar masuk ke dalam tubuh si adik tiri tanpa hubungan darah yang tinggal satu atap dengan sang MC, Amamiya Koita, dan diam-diam memendam obsesi romantis pada kakak tirinya sendiri!"
            nar "Kamu menunduk menatap halaman buku sketsa yang masih terbuka di meja belajar. Di atas kertas bertekstur halus itu, terpampang gambar rancangan anatomi dan ilustrasi karakter novel ringan yang luar biasa hidup. Garis-garisnya bersih, tegas, dengan arsiran bayangan yang halus dan tanda tangan pena mungil bertuliskan 'Shena' di sudut kanan bawah."
            nar "Di samping buku sketsa itu, terselip pula selembar contoh sampul cetakan novel ringan strategi populer yang mencantumkan nama ilustrator yang sama."
            nar "Kamu menatap bekas kapalan tipis di ruas jari tengah tangan kananmu, lalu kembali melihat kualitas ilustrasi profesional di atas meja. Perutmu mendadak terasa dingin."
            chiasa "Seni Rupa... dan dia ilustrator sungguhan pakai nama pena 'Shena'? Tunggu dulu... kalau nanti aku masuk kelas studio atau ada tugas gambar, terus aku harus gimana?"
            nar "Tanganmu sempat menyentuh pinggiran buku sketsa yang masih terbuka itu, lalu menariknya kembali dengan gugup. Di kepalamu sekarang bahkan belum sempat terbayang apakah tubuh ini masih menyimpan bakat pemilik aslinya atau tidak, karena satu-satunya yang terasa nyata hanyalah fakta bahwa kamu baru saja dilempar ke tengah hidup seseorang yang jauh lebih rumit daripada yang pernah kamu baca di manga."
        elif _opening_key == "B":
            nar "Kamu menggeser tubuhmu yang terasa ringan dan asing itu ke tepi kasur, lalu menjulurkan tangan meraih ponsel pintar bersarung krem-hitam yang sedang terhubung ke kabel pengisi daya di atas nakas kayu."
            nar "Jika suara kurang ajar di kepalamu tadi tidak berbohong tentang tubuh pinjaman, maka benda pribadi yang paling sering disentuh pemilik kamar ini pasti menyimpan seluruh identitasnya."
            nar "Kamu mencabut kabel pengisi dayanya dengan jari yang sedikit gemetar. Saat kamu mengangkat ponsel itu ke depan wajahmu, permukaan kaca layarnya yang masih gelap memantulkan bayangan sepasang mata kuning keemasan yang bulat melebar dengan rambut cokelat gelap panjang yang terurai kusut bekas tidur."
            nar "Kamu sama sekali tidak mengenali gadis berambut terurai di pantulan kaca tersebut. Detik berikutnya, layar ponsel menyala otomatis. Ikon gembok kecil di bagian atas layar langsung terbuka hanya dengan memindai wajah yang sedang kamu pakai, sama sekali tidak memberimu kesempatan untuk terhalang oleh kata sandi."
            nar "Kamu mengerjap pelan menatap halaman utama yang tertata rapi dengan folder-folder kuliah dan aplikasi gambar. Di bilah pengingat paling atas, terpampang kartu identitas digital mahasiswa baru bertuliskan 'Tahun Pertama, Fakultas Seni Rupa dan Desain, Universitas Kouseikan' dengan marga 'Amamiya' di bawah fotonya."
            nar "Tatapanmu sempat terangkat melirik sehelai pita hitam yang tergeletak rapi di atas nampan meja rias di sudut kamar, lalu kembali ke layar ponsel. Barulah saat seluruh petunjuk itu bertautan, potongan sampul manga yang baru saja kamu cibir habis-habisan di peron kereta bawah tanah menyambar ingatanmu."
            chiasa "Tunggu sebentar... Universitas Kouseikan, marga Amamiya, mata kuning keemasan, terus pita hitam yang ditaruh di meja rias sana... pantas aja tadi di pantulan layar nggak langsung sadar karena rambutnya masih terurai tanpa pita! Jangan gila, ini kan Amamiya Chiasa?! Adik tiri si MC di manga 'Kouseikan'?!"
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
```
