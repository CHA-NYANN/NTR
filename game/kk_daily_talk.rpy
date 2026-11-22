# Kouseikan — pembuka pertemuan peta, opsi interaksi harian, aktivitas 4 jam, & transisi waktu.
# Cerita obrolan panjang (KK_DAILY_CHAT) disimpan terpisah di game/kk_daily_stories.rpy.
# Seluruh mekanik, variabel relasi, jadwal, dan flag tetap diatur di kk_world.rpy & kk_life.rpy.

init -2 python:
    KK_LOC_DESC = {
        "Gedung Sastra": "Lorong lantai satu Gedung Sastra berbau samar kertas tua dan buku catatan, dengan suara langkah mahasiswa yang sesekali lewat menuju ruang baca.",
        "Gedung Ekonomi": "Koridor kaca Gedung Ekonomi tampak bersih dan lapang, dipenuhi suara obrolan ringan mahasiswa tentang tugas kelas dan diskusi kelompok.",
        "Gedung Sains & Lab": "Di depan ruang baca dan laboratorium Gedung Sains, suasana terasa hening oleh dengung halus pendingin ruangan dan aroma tipis larutan kimia.",
        "Gedung Seni Rupa & Studio": "Aroma cat akrilik, kertas gambar, dan serutan pensil tercium samar dari balik pintu studio Gedung Seni Rupa yang terbuka separuh.",
        "Gedung Arsitektur": "Dari ruang studio Gedung Arsitektur tercium bau kayu balsa dan lem maket, disertai bunyi penggaris besi yang sesekali beradu di atas meja gambar.",
        "Gedung Kedokteran": "Koridor Gedung Kedokteran tampak terang dan rapi, terasa jauh lebih tenang dibandingkan gedung fakultas lain di sekitarnya.",
        "Perpustakaan Pusat": "Di dalam Perpustakaan Pusat, deretan rak tinggi meredam suara kota di luar menjadi kesunyian yang sejuk dan tertib.",
        "Kantin Pusat": "Kantin Pusat dipenuhi aroma kuah hangat, kopi mesin, serta dengung percakapan mahasiswa yang silih berganti keluar masuk.",
        "Taman Kampus": "Angin sepoi-sepoi melintas di sepanjang jalan setapak Taman Kampus yang dinaungi deretan pepohonan rindang.",
        "Asrama Putri": "Area ruang tamu depan Asrama Putri terasa tenang dan tertata rapi dengan deretan kotak surat kayu di dinding samping.",
        "Ruang BEM": "Di sekitar Ruang BEM, papan jadwal kegiatan kampus penuh oleh catatan tempel warna-warni dan lembaran proposal acara.",
        "Pusat Konseling": "Selasar depan Pusat Konseling sunyi dan berjendela lebar, memberi kesan tempat yang terpisah dari keramaian kampus.",
        "Kafe Komorebi": "Lonceng kecil di pintu Kafe Komorebi berdenting pelan di tengah aroma kopi sangrai dan kue panggang hangat yang menyambut dari balik konter.",
        "Rumah Amamiya": "Ruang tengah Rumah Amamiya terasa akrab dan hangat, diterangi cahaya lampu ruang makan di samping deretan cangkir teh di meja.",
        "Rumah Sakurajima": "Beranda dan ruang tamu Rumah Sakurajima yang hangat dipenuhi kesan rumah keluarga yang ramai serta rak pajangan kecil di sudut dinding.",
        "Kos Moeka": "Lorong depan bangunan kos sederhana itu tenang, dengan deretan sepeda mahasiswa yang terparkir rapat di bawah tangga besi.",
        "Taman Lingkungan": "Bangku kayu di pinggir Taman Lingkungan menghadap jalur jalan kaki yang tenang, jauh dari bisingnya jalan raya utama.",
        "Apartemen Yutaka": "Ruang tamu apartemen lantai atas di Distrik Elite tampak luas, minimalis, dan senyap di balik jendela kaca setinggi dinding.",
        "Apartemen Miyuki": "Lobi kecil dan koridor Apartemen Miyuki terasa bersih dan tenang, berbau samar pewangi ruangan yang lembut.",
        "Rumah Saionji": "Halaman depan dan ruang terima tamu kediaman Saionji tampak anggun serta terjaga sunyi di balik pagar batu yang rapi.",
        "Klub Catur": "Di dalam ruang Klub Catur, papan-papan kayu tertata simetris di atas meja panjang diiringi detak jarum jam dinding yang teratur.",
        "Stasiun Kouseikan-mae": "Pelataran depan Stasiun Kouseikan-mae dipenuhi lalu-lalang penumpang serta suara pengumuman kereta yang terdengar samar dari peron.",
        "Toko Thrift": "Rak-rak pakaian bekas dan kain gulung memenuhi ruangan kecil Toko Thrift yang hangat oleh lampu gantung kuning.",
        "Studio Foto": "Area tunggu Studio Foto dipenuhi gulungan latar kain, koper lampu, dan bau samar kopi instan dari sudut ruangan.",
        "Rumah Sakit Tachibana": "Koridor lantai bawah Rumah Sakit Tachibana terang oleh lampu putih bersih dan aroma antiseptik yang khas.",
        "Kuil": "Tangga batu menuju halaman Kuil terasa teduh oleh pepohonan tua dan bunyi lonceng doa yang sesekali berdenting pelan.",
        "Tepi Sungai": "Angin sejuk bertiup pelan di sepanjang tanggul Tepi Sungai, memantulkan cahaya langit di permukaan air yang mengalir tenang.",
        "Lobi ryokan": "Lobi kayu ryokan beraroma tikar tatami baru dan teh panggang hangat yang disajikan bagi para tamu.",
        "Dapur ryokan": "Dari sudut dapur ryokan tercium wangi kaldu hangat dan uap panci yang mengepul pelan.",
        "Ruang bersama ryokan": "Ruang bersama berlantai tatami terasa lapang dan santai dengan meja rendah kayu di tengah ruangan.",
        "Taman luar ryokan": "Jalan setapak batu di taman luar ryokan dikelilingi rumpun bambu dan suara gemericik air pancuran kayu.",
    }

    KK_SLOT_MOOD = {
        0: "Cahaya pagi yang masih miring menerpa dinding dan lantai, membawa udara sejuk awal hari yang belum terlalu bising.",
        1: "Matahari tengah hari terasa terang di balik kaca jendela, sementara arus aktivitas di luar sedang berada di puncaknya.",
        2: "Cahaya sore mulai condong keemasan, membuat bayangan meja dan bangku memanjang pelan seiring jam kuliah berangsur usai.",
        3: "Lampu-lampu ruangan sudah menyala hangat melawan gelapnya langit malam di balik kaca jendela.",
        4: "Suasana larut malam terasa jauh lebih hening, hanya menyisakan dengung halus lampu dan langkah sesekali di kejauhan.",
        5: "Udara dini hari terasa dingin dan sunyi, seolah sebagian besar kota masih tertidur lelap.",
    }

    def kk_daily_pick(cid, pool):
        idx = (kk_elapsed_days + kk_slot + sum(ord(ch) for ch in cid)) % len(pool)
        return pool[idx]

    def kk_daily_chat_lines(cid, host):
        if cid == "koita" and host == "yutaka" and kk_has("yutaka_arah_bl"):
            pool = KK_DAILY_CHAT_KOITA_BL + KK_DAILY_CHAT[(cid, host)]
            return kk_daily_pick(cid, pool)
        pool = list(KK_DAILY_CHAT[(cid, host)])
        if cid == "moeka" and (kk_done("Mo08") or kk_done("Mo10")):
            pool.append(KK_DAILY_CHAT_MOEKA_SIBLINGS[host])
        if cid == "miyuki" and kk_done("Mi06"):
            pool.append(KK_DAILY_CHAT_MIYUKI_PEDIATRI[host])
        return kk_daily_pick(cid, pool)

    def kk_weekly_lines():
        m_mod = ((kk_bulan - 1) % 12) + 1
        if m_mod in (1, 2):
            season = "spring"
        elif m_mod in (3, 4, 5):
            season = "summer"
        elif m_mod in (6, 7, 8):
            season = "autumn"
        elif m_mod in (9, 10, 11):
            season = "winter"
        else:
            season = "late_winter"
        pool = KK_WEEKLY_LIFE[(kk_host, season)]
        return pool[(kk_elapsed_days // 7) % len(pool)]

    def kk_act_lines(actid, lokasi):
        by_loc = KK_ACT_SCENES.get(actid, {})
        pool = by_loc.get((lokasi, kk_host)) or by_loc.get(lokasi) or KK_ACT_DEFAULT.get(actid)
        if not pool:
            return [("nar", KK_ACTS[actid]["done"])]
        return pool[(kk_elapsed_days + kk_slot) % len(pool)]

    def kk_wake_lines():
        slot_key = "day" if kk_slot in (0, 1, 2) else "night"
        pool = KK_REST_WAKE[(kk_host, slot_key)]
        return pool[(kk_elapsed_days + kk_slot) % len(pool)]

    # Pembuka saat pertama kali mengobrol santai di peta (known == False)
    KK_DAILY_OPEN_FIRST = {
        ("koita", "chiasa"): [
            ("nar", "Koita berdiri di tepi ruangan sambil mendekap dua buku catatan tebal dan sebuah botol termos kecil. Begitu melihatmu berjalan menghampiri, senyum ramahnya langsung mengembang tanpa sedikit pun rasa curiga."),
            ("koita", "Eh, Chi-chan? Kebetulan banget ketemu di sini. Jadwal kelasmu barusan sudah selesai ya?"),
            ("chiasa", "Iya, baru aja keluar, Ko-nii. Ko-nii sendiri lagi nunggu seseorang di sini atau cuma sekadar mampir?"),
            ("koita", "Nggak nunggu siapa-siapa kok. Tadi habis mampir ambil fotokopi bahan bacaan, terus sekalian duduk sebentar sambil meluruskan kaki."),
            ("nar", "Panggilan 'Chi-chan' yang meluncur begitu ringan dari mulutnya kembali mengingatkanmu bahwa di mata Koita, sosok di dalam tubuh ini adalah adik tiri yang sudah bertahun-tahun tinggal satu atap dengannya."),
            ("koita", "Tumben banget kamu langsung nyamperin tanpa ngeledek aku duluan, Chi-chan. Lagi capek gara-gara harus keliling gedung kampus yang luas ya?"),
            ("chiasa", "Lumayan juga sih jalannya, Ko-nii. Lagi malas ngeledek aja hari ini."),
            ("koita", "Haha, ya sudah, mumpung ketemu, duduk sebentar di sini yuk kalau kamu nggak lagi buru-buru ke tempat lain."),
        ],
        ("koita", "yutaka"): [
            ("nar", "Koita sedang merapikan tumpukan catatan dan pembatas kertas di tangannya. Begitu menyadari kehadiranmu di dekatnya, ia langsung mengangkat tangan menyapa dengan senyum akrab khas sahabat sejak kecil."),
            ("koita", "Lho, Yutaka? Tumben banget kamu kelihatan rajin keliling sampai ke sini. Lagi jeda kosong atau baru keluar dari ruang kuliah?"),
            ("yutaka", "Baru keluar kelas. Kebetulan aja lewat sini terus lihat kamu berdiri sendirian sambil megang tumpukan kertas."),
            ("koita", "Haha, kirain kamu sengaja nyamperin mau minta traktir kopi kaleng lagi kayak minggu lalu. Tunggu sebentar... kamu kelihatan agak beda ya hari ini."),
            ("yutaka", "Beda di mananya?"),
            ("koita", "Biasanya kalau papasan begini kamu langsung nyeletuk soal rambutku yang berantakan atau soal tugas yang belum kukerjain. Hari ini kamu kelihatan lebih tenang gitu."),
            ("yutaka", "Lagi malas cari gara-gara aja hari ini. Sekalian cari tempat duduk yang nggak terlalu berisik."),
            ("koita", "Boleh juga. Mumpung aku juga belum harus pindah ruangan, duduk bentar di sini aja kalau kamu lagi luang."),
        ],
        ("miyuki", "chiasa"): [
            ("nar", "Tachibana Miyuki tampak sedang merapikan map catatan medis tebal yang penuh penanda kertas pastel di pelukannya. Saat langkahmu mendekat, ia berhenti sejenak lalu menyapamu dengan senyum lembut."),
            ("miyuki", "Ara, Chiasa-chan? Kebetulan sekali bisa berpapasan di sini. Bagaimana ritme kuliahmu sejauh ini?"),
            ("chiasa", "Halo, Tachibana-senpai. Masih menyesuaikan diri sama jadwal sama jarak antar gedungnya, tapi sejauh ini masih bisa diikuti kok."),
            ("miyuki", "Syukurlah kalau begitu. Masa awal masuk kuliah memang paling melelahkan karena semuanya serba baru dan ruangannya tersebar cukup jauh."),
            ("nar", "Ia merapikan sedikit ujung lengan sweternya lalu menatapmu dengan sorot penuh perhatian yang tulus, membuatmu langsung paham mengapa mahasiswa lain begitu menghormatinya."),
            ("miyuki", "Jangan sampai lupa makan teratur di sela pindah ruangan ya, Chiasa-chan. Kadang kalau terlalu fokus di kelas baru, orang baru sadar lapar pas hari sudah hampir habis."),
            ("chiasa", "Makasih, Tachibana-senpai. Senpai sendiri kelihatannya bawa catatan tebal banget hari ini."),
            ("miyuki", "Haha, ini sudah jadi bawaan wajib sehari-hari. Kebetulan aku baru selesai merapikan satu bab dan memang sedang ingin istirahat sebentar."),
        ],
        ("miyuki", "yutaka"): [
            ("nar", "Tachibana Miyuki baru saja menutup buku catatannya yang penuh pembatas kertas berwarna. Melihatmu melangkah mendekat, ia mengangguk sopan dengan senyum tenang."),
            ("miyuki", "Eh, Yutaka-kun? Kebetulan sekali bisa ketemu di sini. Tidak sedang berjalan bersama Koita-kun hari ini?"),
            ("yutaka", "Halo, Tachibana-senpai. Jadwal kelasku hari ini beda jam sama Koita, jadi kebetulan jalan sendiri dulu."),
            ("miyuki", "Begitu ya. Kalian berdua biasanya hampir selalu terlihat lewat bersama di sekitar gerbang atau kantin. Rasanya agak jarang melihatmu berjalan santai sendirian."),
            ("yutaka", "Sesekali enak juga jalan tanpa dengerin Koita bingung milih tempat makan, Senpai. Senpai sendiri kelihatan selalu bawa tumpukan catatan ke mana-mana ya."),
            ("miyuki", "Sudah kebiasaan dari tahun pertama sih, Yutaka-kun, supaya bisa langsung dibaca kalau ada jeda sepuluh menit. Tapi sekarang aku memang lagi berhenti membaca sebentar kok."),
            ("nar", "Miyuki meletakkan map tebalnya ke kursi kosong di sampingnya, mempersilakanmu berhenti sejenak jika kamu masih punya waktu."),
        ],
        ("nagisa", "chiasa"): [
            ("nar", "Sakurajima Nagisa sedang memeriksa gulungan kertas sketsa bangunan dengan kening agak berkerut. Begitu melihatmu berhenti di dekatnya, ia langsung menegakkan punggung dengan sikap yang sedikit waspada."),
            ("nagisa", "Eh, Chiasa? Tumben banget kamu mampir sampai ke area sini. Lagi nyari Ko-kun ya? Kalau kamu nyari dia, dia nggak ada di sekitar sini kok."),
            ("chiasa", "Aku nggak lagi nyari Ko-nii kok, Nagisa-senpai. Cuma kebetulan lewat terus lihat Senpai lagi berdiri di sini."),
            ("nagisa", "H-hmph, begitu ya. Kirain kamu sengaja keliling buat ngecek kakakmu lagi ngobrol sama siapa."),
            ("nar", "Nada awalnya terdengar ketus khas kebiasaan saling menyindir yang dulu sering terjadi antara Chiasa asli dan Nagisa. Namun begitu melihatmu tidak membalas dengan pancingan jahil, bahu Nagisa perlahan turun."),
            ("chiasa", "Kelihatannya Senpai habis berkutat sama gambar denah lama banget. Nggak capek berdiri terus?"),
            ("nagisa", "Lumayan pegal sih tanganku dari tadi megang penggaris besi. Ya sudah, kalau kamu lagi nggak buru-buru ke tempat lain, duduk sebentar di sini juga nggak apa-apa kok."),
        ],
        ("nagisa", "yutaka"): [
            ("nar", "Sakurajima Nagisa tampak sedang memasukkan gulungan kertas gambar ke dalam tabung plastiknya sambil sedikit cemberut. Begitu melihatmu mendekat, ia langsung mendengus pelan dengan gaya akrab teman masa kecil."),
            ("nagisa", "Lho, Yutaka? Tumben banget kamu kelihatan jalan santai ke sini tanpa bikin heboh duluan. Lagi nggak ada kelas ya?"),
            ("yutaka", "Baru kelar kelas. Lihat alismu sudah hampir nyambung dari jauh, kupikir kamu lagi perang sama tugas gambar lagi."),
            ("nagisa", "Enak aja alisku nyambung! Ini cuma capek mikirin revisi ukuran dari dosen tahu nggak! Kamu tuh dari dulu selalu aja mulai obrolan pakai ledekan."),
            ("yutaka", "Bercanda. Kelihatan kok kamu butuh berhenti sebentar sebelum mata kamu makin panas lihat garis lurus."),
            ("nagisa", "Hmph, ya memang sih. Syukurlah kamu lewat, kepalaku memang lagi butuh istirahat lima menit sebelum lanjut kerja lagi."),
            ("nar", "Nagisa menyandarkan tabung gambarnya di tepi bangku lalu melirikmu, memberi isyarat agar kamu ikut duduk sebentar."),
        ],
        ("harumi", "chiasa"): [
            ("nar", "Kujo Harumi sedang menunduk membaca buku referensi tebal sambil mencatat beberapa baris pendek di buku sakunya. Ketika langkahmu berhenti di dekatnya, ia mengangkat kepala dengan tatapan tenang dan jernih."),
            ("harumi", "Oh, Amamiya-san. Adiknya Amamiya-kun yang baru masuk tahun ini, benar?"),
            ("chiasa", "Iya, benar, Kujo-senpai. Maaf ya kalau aku mengganggu Senpai yang lagi serius baca."),
            ("harumi", "Tidak mengganggu sama sekali. Aku memang baru saja menyelesaikan satu subbab dan menjadwalkan jeda lima menit untuk mengistirahatkan mata."),
            ("nar", "Ia menyelipkan pembatas kertas putih polos ke dalam buku lalu meletakkannya rapi sejajar dengan tepi meja, seolah bahkan waktu istirahatnya pun ditata dengan terukur."),
            ("chiasa", "Kujo-senpai selalu bawa buku saku buat mencatat ke mana-mana ya?"),
            ("harumi", "Benar. Memindahkan ide dari kepala ke kertas mengosongkan memori kerja sehingga lebih mudah berkonsentrasi. Apakah ada hal tertentu yang ingin kamu tanyakan, atau kamu sekadar sedang berkeliling?"),
        ],
        ("harumi", "yutaka"): [
            ("nar", "Kujo Harumi sedang menutup buku referensi tebalnya sambil menyelipkan pembatas kertas dengan gerakan sangat teratur. Begitu melihatmu mendekat, ia mengangguk singkat dengan raut tenang."),
            ("harumi", "Kisaragi-kun. Kebetulan bertemu di sini. Apakah ada urusan dengan catatan kuliah atau kamu sekadar lewat?"),
            ("yutaka", "Kebetulan lewat aja, Kujo-san. Kelihatannya kamu lagi serius banget dari tadi, maaf kalau memotong fokusmu."),
            ("harumi", "Kamu tidak memotong apa pun. Aku baru menyelesaikan ringkasan satu bab dan memang menjadwalkan jeda singkat sekarang."),
            ("nar", "Ia menaruh penanya tepat sejajar di sisi buku catatan, lalu menatapmu dengan sorot tenang tanpa basa-basi berlebih."),
            ("harumi", "Jarang sekali kita berpapasan di luar diskusi kelompok belajar dulu atau lorong kampus. Kalau kamu punya waktu beberapa menit, silakan saja duduk."),
        ],
        ("moeka", "chiasa"): [
            ("nar", "Kohinata Moeka sedang membolak-balik buku sketsa kecil penuh potongan kain warna-warni ketika ekor matanya menangkap sosokmu. Senyum cerahnya langsung mengembang lebar sambil melambaikan tangan."),
            ("moeka", "Eh, Chimian! Ya ampun, pas banget ketemu di sini! Kamu lagi jeda kelas ya?"),
            ("nar", "Panggilan 'Chimian' yang meluncur begitu santai itu sempat membuatmu terhenti sepersekian detik karena terasa agak asing di telinga, meski jelas merupakan julukan akrab yang sudah biasa dipakai Moeka."),
            ("chiasa", "Halo, Moemoe-senpai. Iya, baru aja keluar kelas. Senpai kelihatan bersemangat banget hari ini."),
            ("moeka", "Harus dong! Kalau mukanya ditekuk terus nanti ide desain bajunya ikut kabur semua. Eh, tunggu, kamu hari ini kelihatan agak kalem dari biasanya ya? Lagi capek mikirin jadwal kuliah baru?"),
            ("chiasa", "Nggak capek banget kok, cuma lagi pengin jalan santai sebentar aja."),
            ("moeka", "Pas banget kalau begitu! Duduk sini sebentar yuk, aku juga baru selesai nyusun contoh kombinasi warna di bukuku."),
        ],
        ("moeka", "yutaka"): [
            ("nar", "Kohinata Moeka baru saja memasukkan ponsel ke saku jaketnya saat melihatmu berjalan mendekat. Ia langsung tersenyum cerah sambil melambaikan kedua tangannya."),
            ("moeka", "Lho, Yutayuta! Tumben banget kita papasan di sini pas lagi nggak ada rapat atau urusan panitia!"),
            ("nar", "Mendengar julukan 'Yutayuta' meluncur begitu ringan membuatmu sempat mengerjap sesaat sebelum ikut tersenyum tipis."),
            ("yutaka", "Halo, Kohinata. Energimu kayaknya nggak pernah habis ya padahal jadwal kampus lagi padat."),
            ("moeka", "Haha, kalau nggak dibawa senang nanti malah cepat pusing sendiri! Kamu sendiri kok kelihatan agak tenang hari ini, biasanya begitu ketemu langsung ngeledek tasku yang penuh pernak-pernik."),
            ("yutaka", "Hari ini lagi malas ngeledek. Kebetulan lewat aja terus lihat kamu di sini."),
            ("moeka", "Wah, langka banget! Kalau kamu lagi nggak buru-buru, duduk sebentar yuk ngobrol santai."),
        ],
        ("shiori", "chiasa"): [
            ("nar", "Saionji Shiori sedang memeriksa buku catatan bersampul kulit gelap sambil meneguk teh dari cangkirnya. Begitu kamu menghampiri, ia mengangkat wajah dan menatapmu dengan senyum sopan yang tenang."),
            ("shiori", "Selamat bertemu, Amamiya-san. Kalau ingatanku tidak keliru, kamu adik dari Amamiya Koita yang tahun ini masuk Fakultas Seni Rupa, benar?"),
            ("chiasa", "Iya, betul, Saionji-senpai. Maaf kalau aku datang menyapa tiba-tiba begini."),
            ("shiori", "Sama sekali tidak mengganggu. Aku memang sedang mengambil jeda sebentar sebelum kegiatan berikutnya."),
            ("nar", "Sorot mata ungunya mengamati sikapmu selama dua detik penuh dengan ketenangan yang sulit ditebak, lalu sudut bibirnya melengkung tipis."),
            ("shiori", "Menarik juga. Jarang sekali mahasiswa tahun pertama datang menyapa lebih dulu tanpa terlihat kaku atau sibuk mencari alasan. Silakan duduk sebentar kalau kamu punya waktu."),
        ],
        ("shiori", "yutaka"): [
            ("nar", "Saionji Shiori sedang merapikan lembaran catatan kuliah ekonominya saat melihatmu berhenti di dekat meja. Ia menoleh dengan senyum tipis yang sopan dan terukur."),
            ("shiori", "Selamat bertemu, Kisaragi-san. Kita satu angkatan di fakultas yang sama, meskipun rasanya ini pertama kalinya kita benar-benar berbicara di luar ruang kuliah."),
            ("yutaka", "Halo, Saionji-san. Maaf kalau mengganggu waktumu, kebetulan aja lewat sini terus lihat kamu."),
            ("shiori", "Tidak masalah. Aku baru selesai merangkum catatan mata kuliah minggu ini dan memang belum berniat langsung beranjak."),
            ("nar", "Mata ungunya menatapmu singkat seolah mengukur mengapa seorang Kisaragi Yutaka mendadak berhenti untuk menyapa, sebelum ia mempersilakanmu dengan isyarat tangan yang anggun."),
            ("shiori", "Silakan saja kalau kamu punya beberapa menit untuk bertukar kata."),
        ],
        ("chiasa", "yutaka"): [
            ("nar", "Amamiya Chiasa sedang merapikan buku sketsa dan kotak pensilnya sambil membetulkan pita hitam di rambutnya. Begitu melihatmu berjalan mendekat, mata keemasannya menyipit jahil."),
            ("chiasa", "Wah, tumben banget Yutaka-kun kelihatan keliling di sini sendirian tanpa ngekor di belakang Ko-nii."),
            ("yutaka", "Enak aja ngekor. Aku kan juga punya jadwal sama urusan sendiri di kampus, Chiasa."),
            ("chiasa", "Haha, iya deh, percaya. Tapi tunggu... cara kamu jawab tadi kedengarannya agak lebih kalem dari biasanya deh. Nggak lagi sakit kan, Yutaka-kun?"),
            ("yutaka", "Sehat kok, cuma lagi malas debat panjang aja hari ini."),
            ("chiasa", "Heh, langka banget. Ya sudah, kebetulan aku baru aja mau istirahat sebentar, temani ngobrol dulu nggak apa-apa kan?"),
        ],
        ("yutaka", "chiasa"): [
            ("nar", "Kisaragi Yutaka tampak bersandar santai sambil memutar kaleng minuman dingin di tangannya. Begitu melihatmu mendekat, ia mengangkat sebelah alis dengan senyum ringan khas teman masa kecil."),
            ("yutaka", "Eh, Chiasa? Tumben jalan sendirian ke sini, nggak lagi nempel sama Koita atau ngumpul bareng anak-anak jurusanmu?"),
            ("chiasa", "Baru aja pisah di depan gedung tadi, Yutaka-kun. Yutaka-kun sendiri kelihatan santai banget di sini."),
            ("yutaka", "Lagi nunggu jeda jam kuliah lewat aja daripada duduk melamun di koridor. Eh, kamu hari ini kelihatan nggak seberisik biasanya ya?"),
            ("chiasa", "Memangnya biasanya aku seberisik apa sih, Yutaka-kun?"),
            ("yutaka", "Haha, bercanda. Kebetulan kamu lewat, jadi nggak terlalu bosan duduk sendirian di sini."),
        ],
    }

    # 3 variasi pembuka yang lebih panjang & hidup saat sudah kenal (known == True)
    KK_DAILY_OPEN = {
        ("koita", "chiasa"): [
            [
                ("nar", "Koita duduk sambil membolak-balik buku bacaan sastra yang pinggirannya penuh tempelan kertas penanda. Begitu melihatmu datang, ia langsung menutup bukunya dan menepuk kursi di sebelah."),
                ("koita", "Eh, Chi-chan! Pas banget kamu lewat sini. Aku baru aja kepikiran mau berhenti baca sebentar."),
                ("chiasa", "Kelihatannya serius banget baca buku tebal itu, Ko-nii. Lagi nyiapin bahan diskusi kelas ya?"),
                ("koita", "Iya, minggu ini ada dua bab panjang yang harus kubandingkan, mataku sudah mulai lelah lihat huruf kecil semua. Sini duduk dulu kalau kamu nggak lagi dikejar waktu."),
                ("chiasa", "Kebetulan aku juga lagi santai sebentar kok, Ko-nii."),
                ("koita", "Sip, jadi ada teman ngobrol sambil ngelurusin punggung."),
            ],
            [
                ("nar", "Kamu melihat Koita sedang merapikan setumpuk lembar fotokopi yang beberapa sudutnya agak terlipat sambil menyesap minuman hangat dari botol termos kecilnya. Saat kamu menyapa, ia buru-buru memindahkan tasnya dari kursi sebelah."),
                ("koita", "Lho, Chi-chan? Sini duduk dulu, kamu kelihatan habis jalan cukup jauh dari gedung sebelah."),
                ("chiasa", "Lumayan sih, Ko-nii. Tadi sempat muter cari beberapa barang dulu sebelum lewat ke sini."),
                ("koita", "Wah, jangan terlalu diforsir keliling terus ya. Minum dulu aja biar nggak kehausan."),
                ("nar", "Koita menuangkan sedikit teh hangat dari termosnya ke cangkir tutupnya dan menggesernya ke dekatmu dengan kebiasaan telatennya."),
                ("chiasa", "Makasih, Ko-nii. Pas banget lagi pengin minum yang hangat."),
            ],
            [
                ("nar", "Koita menoleh tepat saat langkahmu mendekat, lalu tertawa kecil sambil memasukkan ponselnya kembali ke saku jaket."),
                ("koita", "Kebetulan banget, Chi-chan! Tadi aku baru aja mau ngetik pesan nanya kamu lagi ada di sekitar mana."),
                ("chiasa", "Memangnya ada urusan mendadak apa di rumah atau di kampus, Ko-nii?"),
                ("koita", "Nggak ada hal mendadak kok, cuma penasaran aja jadwalku hari ini kebetulan kosong bareng kamu atau nggak. Eh, ternyata malah langsung ketemu di sini."),
                ("chiasa", "Kebetulan jadwalku hari ini memang agak longgar sedikit."),
                ("koita", "Asyik deh kalau begitu. Istirahat sebentar di sini yuk sebelum lanjut kegiatan lagi."),
            ],
        ],
        ("koita", "yutaka"): [
            [
                ("nar", "Koita tampak sedang membaca catatan kuliahnya sambil mengetuk-ngetukkan ujung pena ke permukaan meja. Begitu melihatmu datang, ia langsung menyengir ramah dan melambai singkat."),
                ("koita", "Eh, Yutaka! Tumben banget kamu kelihatan segar hari ini. Lagi jeda kelas juga?"),
                ("yutaka", "Iya, baru keluar dari ruangan. Kamu dari tadi duduk sendirian aja di sini?"),
                ("koita", "Baru sepuluh menit lalu kok, teman-teman kelasku tadi pada duluan ke gedung sebelah. Pas banget kamu muncul jadi nggak bengong sendirian."),
                ("yutaka", "Biar nggak ketiduran di atas buku catatanmu juga kan."),
                ("koita", "Haha, ketahuan aja. Sini duduk dulu, Yutaka."),
            ],
            [
                ("nar", "Koita baru saja menutup ritsleting tas selempangnya ketika mendengar langkahmu mendekat. Ia menoleh sambil tertawa ringan."),
                ("koita", "Wah, pas banget kamu muncul, Yutaka. Aku baru aja bosan banget duduk sendiri sambil nunggu jeda jadwal berikutnya."),
                ("yutaka", "Kirain jadwalmu hari ini penuh terus sampai nggak sempat duduk tenang."),
                ("koita", "Hari ini lumayan longgar sedikit, dosen kelas terakhirku memajukan jam bimbingan ke minggu depan. Akhirnya bisa bernapas juga tanpa dikejar tenggat."),
                ("yutaka", "Lumayan tuh buat istirahat sebentar. Kamu nggak mau cari minum dulu?"),
                ("koita", "Sudah bawa air di tas kok. Duduk aja dulu di sini bentar."),
            ],
            [
                ("nar", "Kamu mendapati Koita tengah memandangi selembar daftar buku dengan dahi agak berkerut. Saat kamu menyapa, ia langsung melipat kertas itu dan tersenyum lega."),
                ("koita", "Lho, Yutaka? Kebetulan banget ketemu di sini. Kamu habis dari gedung fakultasmu ya?"),
                ("yutaka", "Iya, sekalian jalan cari angin bentar daripada duduk ngantuk di koridor."),
                ("koita", "Cocok banget, aku juga baru selesai nyusun daftar bacaan buat makalah minggu depan. Kepalaku sudah penuh banget lihat judul buku semua."),
                ("yutaka", "Makanya simpan dulu kertasnya, ngobrol biasa aja sebentar."),
                ("koita", "Siap, ide bagus tuh."),
            ],
        ],
        ("miyuki", "chiasa"): [
            [
                ("nar", "Tachibana Miyuki tampak sedang merapikan map catatan medisnya dengan gerakan yang sangat teratur. Begitu melihatmu mendekat, senyum lembutnya langsung terbit."),
                ("miyuki", "Ara, Chiasa-chan. Senang sekali bisa ketemu lagi di sini. Kamu baru selesai kelas?"),
                ("chiasa", "Iya, Tachibana-senpai. Senpai sendiri kelihatannya baru selesai baca catatan yang tebal banget itu."),
                ("miyuki", "Haha, lumayan bikin pundak pegal sih dari tadi menunduk terus. Kebetulan kamu lewat, jadi aku punya alasan yang bagus buat berhenti sejenak."),
                ("chiasa", "Syukurlah kalau aku datang di waktu yang pas buat bikin Senpai istirahat."),
                ("miyuki", "Selalu pas kok kalau Chiasa-chan yang mampir. Duduklah sebentar."),
            ],
            [
                ("nar", "Miyuki sedang menuang teh hangat dari termos kecilnya ke cangkir tutup saat menyadari kehadiranmu. Aroma teh chamomile yang lembut langsung tercium samar."),
                ("miyuki", "Chiasa-chan, kebetulan sekali. Kamu sudah sempat makan atau minum sesuatu belum hari ini?"),
                ("chiasa", "Sudah kok, Senpai. Justru Senpai yang biasanya terlalu sibuk sampai lupa jam istirahat sendiri."),
                ("miyuki", "Wah, ketahuan lagi ya kebiasaanku. Tenang saja, hari ini aku benar-benar menyempatkan duduk minum teh hangat dulu."),
                ("chiasa", "Wanginya enak banget, teh herbal ya, Senpai?"),
                ("miyuki", "Iya, biar tenggorokan dan bahu agak lebih rileks. Kalau nggak buru-buru, duduk sini sebentar yuk."),
            ],
            [
                ("nar", "Di tengah kesibukannya menandai jadwal di buku agenda bersampul krem, Miyuki mengangkat kepala dan tersenyum lega melihatmu."),
                ("miyuki", "Halo, Chiasa-chan. Tumben wajahmu kelihatan agak santai hari ini, jadwal tugasnya sudah aman?"),
                ("chiasa", "Sebagian besar sudah beres, Senpai. Jadi hari ini sempat jalan-jalan sebentar cari suasana."),
                ("miyuki", "Bagus sekali. Menjaga ritme supaya nggak terlalu terburu-buru itu penting banget, meskipun aku sendiri kadang masih kesulitan melakukannya."),
                ("chiasa", "Kalau gitu sekarang gantian Senpai yang ikut santai sebentar bareng aku."),
                ("miyuki", "Haha, baiklah. Aku ikut ajakanmu kali ini."),
            ],
        ],
        ("miyuki", "yutaka"): [
            [
                ("nar", "Tachibana Miyuki sedang menutup buku catatan tebalnya saat melihatmu melangkah mendekat. Senyum lembut langsung menghiasi wajahnya."),
                ("miyuki", "Ara, Yutaka-kun. Kebetulan sekali bisa ketemu di sini. Kamu lagi jeda kuliah?"),
                ("yutaka", "Iya, Tachibana-senpai. Kelihatannya tumpukan catatan Senpai hari ini nggak kalah tinggi dari kemarin."),
                ("miyuki", "Haha, memang rasanya nggak pernah berkurang ya tiap semester. Kebetulan kamu datang, jadi aku punya alasan buat berhenti membaca sebentar."),
                ("yutaka", "Kalau nggak ada yang nyamperin, Senpai pasti bakal terus baca sampai lupa jam lagi kan."),
                ("miyuki", "Ketahuan juga ya. Sini duduk sebentar kalau jadwalmu masih longgar, Yutaka-kun."),
            ],
            [
                ("nar", "Miyuki baru saja meletakkan cangkir teh hangatnya ketika melihatmu datang. Aroma tipis teh herbal melayang di sekitar meja."),
                ("miyuki", "Halo, Yutaka-kun. Kelihatannya kamu nggak lagi buru-buru mengejar jadwal hari ini."),
                ("yutaka", "Lagi cukup luang kok, Senpai. Senpai sendiri kelihatan akhirnya sempat minum teh juga."),
                ("miyuki", "Iya, tadi sempat diingatkan teman juga supaya nggak terus-terusan menatap catatan. Ternyata duduk tenang lima menit aja lumayan mengembalikan tenaga."),
                ("yutaka", "Memang harus sering-sering begitu, Senpai."),
                ("miyuki", "Makasih sudah ikut mengingatkan, Yutaka-kun. Temani aku duduk sebentar yuk."),
            ],
            [
                ("nar", "Kamu menemukan Miyuki sedang merapikan pembatas buku di dalam tasnya. Ia mendongak dengan senyum hangat begitu kamu menyapa."),
                ("miyuki", "Eh, Yutaka-kun? Tumben ketemu di sini hari ini. Ada urusan di sekitar sini atau sekadar lewat?"),
                ("yutaka", "Cuma lewat cari suasana baru aja, Senpai. Eh, malah ketemu Senpai di sini."),
                ("miyuki", "Pas sekali kalau begitu. Aku juga baru saja selesai membereskan ringkasanku dan sedang malas langsung pindah tempat."),
                ("yutaka", "Kalau gitu aku ikut duduk sebentar di sini nggak mengganggu kan?"),
                ("miyuki", "Sama sekali nggak mengganggu, justru aku senang ada teman mengobrol."),
            ],
        ],
        ("nagisa", "chiasa"): [
            [
                ("nar", "Sakurajima Nagisa sedang mengetuk-ngetukkan pensil mekaniknya ke tepi buku sketsa sambil memandangi denah garis tipis. Begitu melihatmu datang, bahunya sempat menegang kecil lalu perlahan melunak."),
                ("nagisa", "Oh, Chiasa. Kebetulan banget kamu lewat sini. Lagi nggak buru-buru balik ke gedung fakultasmu kan?"),
                ("chiasa", "Lagi kosong kok, Nagisa-senpai. Kelihatannya Senpai lagi serius banget sama gambar denahnya."),
                ("nagisa", "Yah, kalau nggak dicek dari sekarang nanti ukurannya meleset semua pas mulai dipotong. Tapi mataku memang sudah mulai lelah lihat garis milimeter dari tadi."),
                ("chiasa", "Istirahat sebentar aja dulu, Senpai, nanti malah makin salah ukur."),
                ("nagisa", "Hmph, ya sudah deh. Mumpung ada kamu, aku taruh pensilnya dulu sebentar."),
            ],
            [
                ("nar", "Nagisa tampak baru saja merapikan gulungan kertas ke dalam tabung gambar besar. Melihatmu menyapa, ia mendengus kecil dengan raut yang tetap ramah."),
                ("nagisa", "Eh, Chiasa? Tumben banget nggak kelihatan bawa tas kanvas besar itu."),
                ("chiasa", "Lagi kutitip di loker kampus, Senpai. Berat banget bahuku kalau dibawa keliling terus."),
                ("nagisa", "Haha, pantesan langkahmu kelihatan enteng banget tadi. Kalau aku malah nggak bisa lepas dari tabung gambar ini tiap hari."),
                ("chiasa", "Kelihatannya memang berat banget sih. Sini taruh dulu di bangku biar bahu Senpai nggak pegal."),
                ("nagisa", "Oke, makasih. Kebetulan aku juga lagi pengin duduk sebentar."),
            ],
            [
                ("nar", "Kamu mendapati Nagisa sedang menggosok pergelangan tangannya yang pegal sambil memegang botol minum dingin. Ia menoleh cepat begitu mendengar langkahmu."),
                ("nagisa", "Lho, Chiasa? Kamu habis dari mana tadi?"),
                ("chiasa", "Cuma keliling aja sambil cari angin, Nagisa-senpai. Tangan Senpai pegal ya habis potong maket?"),
                ("nagisa", "Dikit doang kok! Habis motong papan karton tebal kebanyakan dari tadi, pisau potongku sampai agak tumpul di tengah jalan."),
                ("chiasa", "Aduh, hati-hati lho kalau pisaunya tumpul, malah lebih gampang meleset."),
                ("nagisa", "Iya, sudah kuganti mata pisaunya kok! Ya sudah, duduk bentar di sini yuk."),
            ],
        ],
        ("nagisa", "yutaka"): [
            [
                ("nar", "Sakurajima Nagisa sedang melipat lembar cetak denah dengan kening berkerut dalam. Begitu kamu menghampiri, ia langsung menghela napas lega."),
                ("nagisa", "Eh, Yutaka? Pas banget kamu muncul. Kepalaku rasanya mau meledak lihat garis ukuran dari tadi."),
                ("yutaka", "Makanya sekali-kali berhenti dulu jangan dipelototin terus, Nagisa."),
                ("nagisa", "Iya, iya, tahu kok! Tapi kalau nggak kukerjain sekarang, besok pasti numpuk lagi sama tugas struktur."),
                ("yutaka", "Istirahat sepuluh menit nggak bakal bikin maketmu roboh kok."),
                ("nagisa", "Hmph, cerewet. Tapi ya sudah, mumpung kamu ada di sini, aku berhenti sebentar deh."),
            ],
            [
                ("nar", "Nagisa menoleh dengan senyum kecil yang segera berubah jadi ekspresi ketus main-main begitu melihat gaya jalanmu yang santai."),
                ("nagisa", "Enak banget ya kelihatannya anak ekonomi, jam segini sudah bisa jalan santai sambil masukin tangan ke saku."),
                ("yutaka", "Jangan salah, tugasku juga banyak kok. Cuma kebetulan aja aku pintar nyari jeda istirahat."),
                ("nagisa", "Bilang aja kamu memang paling jago nyari alasan buat santai! Tapi ya sudahlah, lihat kamu jalan santai gitu bikin aku ikut sadar aku terlalu tegang dari tadi."),
                ("yutaka", "Nah, akhirnya ngaku juga. Duduk dulu sebentar, Nagisa."),
                ("nagisa", "Oke, lima menit aja ya."),
            ],
            [
                ("nar", "Kamu melihat Nagisa baru saja membeli minuman dingin dan duduk memegangi botolnya sambil menatap kosong ke depan. Saat kamu mendekat, ia melambai singkat."),
                ("nagisa", "Oh, Yutaka! Tumben banget kita ketemu di sini tanpa janjian dulu."),
                ("yutaka", "Kebetulan lagi lewat terus lihat rambut pirangmu dari jauh."),
                ("nagisa", "Heh, nggak usah pakai alasan lihat rambut segala! Tapi pas banget sih kamu lewat, lagi pengin ngobrol biasa aja biar otakku dingin sedikit."),
                ("yutaka", "Kalau begitu aku ikut duduk di sebelah ya."),
                ("nagisa", "Silakan, mumpung kursinya masih kosong."),
            ],
        ],
        ("harumi", "chiasa"): [
            [
                ("nar", "Kujo Harumi sedang mencatat angka-angka rapi di buku catatan berkotaknya dengan tulisan seragam. Begitu mendengar langkahmu, ia mengangkat kepala dan mengangguk pelan."),
                ("harumi", "Amamiya-san. Kebetulan bertemu lagi di sini."),
                ("chiasa", "Halo, Kujo-senpai. Lagi ngerjain laporan percobaan lagi ya?"),
                ("harumi", "Baru saja selesai merapikan tabel datanya. Secara jadwal, aku punya waktu luang sekitar sepuluh menit sebelum kegiatan berikutnya."),
                ("chiasa", "Syukurlah, berarti aku nggak mengganggu waktu fokus Senpai ya."),
                ("harumi", "Tidak sama sekali. Silakan duduk kalau kamu ingin berbicara sebentar."),
            ],
            [
                ("nar", "Harumi menutup buku referensi tipis yang sedang ia baca dan menyimpannya rapi di sebelah gelas airnya. Tatapannya tertuju padamu dengan tenang."),
                ("harumi", "Selamat bertemu, Amamiya-san. Jadwal kelasmu hari ini sudah selesai?"),
                ("chiasa", "Sudah selesai sebagian, Kujo-senpai. Cuma lagi jalan santai sebentar biar nggak penat di dalam ruangan."),
                ("harumi", "Langkah yang masuk akal. Mengambil jeda pendek di antara dua blok konsentrasi memang terbukti meningkatkan daya ingat serta menurunkan kelelahan mata."),
                ("chiasa", "Senpai selalu punya penjelasan yang masuk akal banget ya bahkan buat jalan-jalan santai."),
                ("harumi", "Haha, mungkin itu sudah jadi kebiasaan. Duduklah sebentar, Amamiya-san."),
            ],
            [
                ("nar", "Kamu mendapati Harumi tengah memandangi selembar grafik kecil di atas meja sambil sedikit mengerutkan kening. Saat kamu menyapa, kerutan itu perlahan mereda."),
                ("harumi", "Oh, Amamiya-san. Kebetulan sekali kamu lewat."),
                ("chiasa", "Lagi ada angka atau grafik yang bikin bingung, Senpai?"),
                ("harumi", "Bukan bingung, hanya menemukan satu penyimpangan kecil yang cukup menarik untuk dicek ulang nanti di laboratorium."),
                ("chiasa", "Oh, syukurlah kalau bukan masalah besar."),
                ("harumi", "Tidak mendesak sekarang. Aku justru senang ada yang mengajak bicara supaya kepalaku bisa lepas sebentar dari grafik ini."),
            ],
        ],
        ("harumi", "yutaka"): [
            [
                ("nar", "Kujo Harumi sedang memeriksa catatan rapi di buku sakunya. Ketika kamu menyapa, ia mendongak dengan ekspresi tenang dan meletakkan penanya sejajar di tepi kertas."),
                ("harumi", "Kisaragi-kun. Kebetulan bertemu lagi di sini."),
                ("yutaka", "Halo, Kujo-san. Lagi meriksa data praktikum lagi?"),
                ("harumi", "Baru saja selesai mengecek ulang angkanya. Kebetulan aku sedang mengambil jeda sepuluh menit sekarang."),
                ("yutaka", "Pas banget kalau gitu, aku nggak merasa bersalah mengganggu jadwalmu."),
                ("harumi", "Kamu tidak perlu merasa begitu. Duduk saja kalau kamu sedang luang."),
            ],
            [
                ("nar", "Harumi menutup buku referensinya dengan bunyi pelan lalu menoleh ke arahmu dengan sorot jernih."),
                ("harumi", "Selamat bertemu, Kisaragi-kun. Kelihatannya jadwalmu hari ini tidak terlalu padat."),
                ("yutaka", "Lumayan longgar sih dibanding kemarin. Kamu sendiri kelihatan nggak pernah lepas dari buku catatan ke mana-mana."),
                ("harumi", "Mencatat langsung lebih efisien daripada mengandalkan ingatan jangka pendek yang mudah terdistorsi. Tapi untuk beberapa menit ke depan, aku bisa menyimpannya dulu."),
                ("yutaka", "Lumayan langka lihat kamu nutup buku sebelum diminta."),
                ("harumi", "Bahkan jadwal paling padat pun butuh jeda agar tidak rusak, Kisaragi-kun."),
            ],
            [
                ("nar", "Kamu melihat Harumi duduk tenang sambil memutar gelas airnya pelan. Begitu menyadari kehadiranmu, ia mengangguk sopan."),
                ("harumi", "Oh, Kisaragi-kun. Kebetulan kamu lewat di sini."),
                ("yutaka", "Lagi istirahat sebentar, Kujo-san? Kelihatannya tadi sempat mikirin sesuatu."),
                ("harumi", "Benar. Konsentrasi penuh lebih dari sembilan puluh menit biasanya mulai menurunkan ketelitian, jadi aku sengaja berhenti sebentar."),
                ("yutaka", "Kalau gitu aku ikut duduk sebentar di sini ya biar sekalian istirahat juga."),
                ("harumi", "Silakan saja."),
            ],
        ],
        ("moeka", "chiasa"): [
            [
                ("nar", "Kohinata Moeka sedang memilah beberapa gulung benang dan potongan pita di tas kain besarnya. Begitu melihatmu mendekat, mata birunya langsung berbinar cerah."),
                ("moeka", "Eh, Chimian! Pas banget kamu datang! Aku baru aja pusing milih kombinasi warna sendiri dari tadi!"),
                ("chiasa", "Haha, semangat banget sih, Moemoe-senpai. Lagi nyiapin konsep desain baru buat kelas ya?"),
                ("moeka", "Iya nih, tapi rasanya mataku sudah mulai ketukar antara warna krem sama gading gara-gara dilihat terus! Istirahat dulu deh mumpung ketemu kamu!"),
                ("chiasa", "Boleh banget, Senpai, taruh dulu contoh kainnya."),
                ("moeka", "Siap! Ngobrol sebentar yuk biar otakku segar lagi!"),
            ],
            [
                ("nar", "Moeka melambaikan tangan tinggi-tinggi dari tempatnya duduk sambil merapikan poninya yang sedikit tergerai."),
                ("moeka", "Chimian! Sini, sini! Tumben banget kita ketemu pas jam santai begini!"),
                ("chiasa", "Halo, Moemoe-senpai. Kelihatannya Senpai habis jalan jauh banget bawa tas kain penuh begitu."),
                ("moeka", "Lumayan! Tadi muter dulu ke dua tempat buat cek bahan. Tapi begitu lihat wajah yang familier langsung nggak berasa capeknya kok!"),
                ("chiasa", "Senpai memang selalu ceria banget ya kalau ketemu."),
                ("moeka", "Hehe, duduk sini sebentar yuk kalau kamu nggak lagi dikejar jadwal!"),
            ],
            [
                ("nar", "Kamu mendapati Moeka tengah tersenyum kecil memandangi buku catatan penuh tempelan contoh kain. Saat kamu memanggilnya, ia langsung mengangkat wajah dengan raut ceria."),
                ("moeka", "Lho, Chimian! Panjang umur banget, barusan aku lagi lihat potongan warna hangat yang kupikir cocok banget sama gaya kamu!"),
                ("chiasa", "Wah, warna apa tuh, Senpai?"),
                ("moeka", "Warna cokelat karamel agak keemasan, pasti masuk banget sama warna rambut sama pita hitammu!"),
                ("chiasa", "Wah, mata desainer memang beda ya langsung kepikiran warna."),
                ("moeka", "Haha, duduk dulu yuk kalau lagi nggak buru-buru!"),
            ],
        ],
        ("moeka", "yutaka"): [
            [
                ("nar", "Kohinata Moeka sedang membolak-balik buku catatan penuh stiker warna-warni saat melihatmu mendekat. Senyum ramainya langsung terbit."),
                ("moeka", "Eh, Yutayuta! Tumben banget ketemu di sini! Lagi cari kopi atau lagi kabur dari kelas yang membosankan nih?"),
                ("yutaka", "Mana ada kabur dari kelas, Kohinata. Kelasku memang sudah selesai dari tadi."),
                ("moeka", "Haha, bercanda kok! Tapi muka santaimu tuh memang selalu bikin orang mengira kamu lagi bolos!"),
                ("yutaka", "Enak aja. Kamu sendiri kelihatan lagi nggak buru-buru hari ini."),
                ("moeka", "Pas banget aku baru selesai beresin catatanku. Duduk sebentar yuk ngobrol!"),
            ],
            [
                ("nar", "Moeka langsung melambaikan tangan dengan antusias ketika kamu melangkah masuk ke pandangannya."),
                ("moeka", "Yutayuta! Kebetulan banget ketemu di sini! Kelihatannya kamu lagi nggak buru-buru ya?"),
                ("yutaka", "Lagi cukup santai kok. Kamu sendiri nggak lagi dikejar rapat kegiatan kampus?"),
                ("moeka", "Hari ini aman, bebas rapat! Rasanya lega banget sampai pengin ngobrol panjang lebar tanpa mikirin proposal."),
                ("yutaka", "Jarangnya kamu nggak bawa tumpukan formulir ke mana-mana."),
                ("moeka", "Iya kan! Makanya duduk sini bentar yuk mumpung aku lagi bebas!"),
            ],
            [
                ("nar", "Kamu melihat Moeka sedang merapikan kantong kain penuh peralatan jahit kecil di pangkuannya. Begitu kamu menyapa, ia langsung tertawa ringan."),
                ("moeka", "Wah, pas banget Yutayuta lewat! Coba lihat, mukaku kelihatan capek banget nggak hari ini?"),
                ("yutaka", "Nggak juga, masih seberisik biasanya kok."),
                ("moeka", "Ih, jahat banget jawabannya! Padahal aku sudah berharap dibilang rajin banget hari ini!"),
                ("yutaka", "Iya deh, kelihatan rajin banget sampai bawa kotak jahit ke mana-mana."),
                ("moeka", "Haha, nah gitu dong! Duduk sini sebentar yuk."),
            ],
        ],
        ("shiori", "chiasa"): [
            [
                ("nar", "Saionji Shiori sedang menutup buku catatannya dengan gerakan anggun ketika melihatmu menghampiri. Senyum tipis yang tenang muncul di bibirnya."),
                ("shiori", "Selamat bertemu lagi, Amamiya-san. Kebetulan sekali waktu kita bertemu cukup serasi hari ini."),
                ("chiasa", "Halo, Saionji-senpai. Senpai lagi santai sebentar sebelum kegiatan berikutnya?"),
                ("shiori", "Betul. Aku baru saja menyelesaikan bacaanku untuk sesi ini dan belum ingin langsung beranjak."),
                ("chiasa", "Boleh aku ikut duduk sebentar di sini, Senpai?"),
                ("shiori", "Silakan saja, Amamiya-san. Kehadiranmu cukup menenangkan suasana."),
            ],
            [
                ("nar", "Shiori sedang memutar pelan cangkir porselen di depannya saat menyadari langkahmu. Mata ungunya menatapmu dengan sorot penasaran yang ramah."),
                ("shiori", "Oh, Amamiya-san. Kelihatannya jadwal studiomu hari ini memberimu sedikit ruang bernapas."),
                ("chiasa", "Lumayan, Saionji-senpai. Jadi sempat keliling sebentar biar nggak bosan di dalam ruangan terus."),
                ("shiori", "Pilihan yang bagus. Ruang gerak pikiran kadang memang perlu mengganti pemandangan agar tidak terasa sempit."),
                ("chiasa", "Senpai sendiri kelihatan selalu tenang di mana pun tempatnya."),
                ("shiori", "Hanya kebiasaan menjaga tempo saja. Silakan duduk sebentar kalau kamu punya waktu."),
            ],
            [
                ("nar", "Kamu mendapati Shiori tengah membaca catatan strategi di buku sakunya. Begitu kamu menyapa, ia menyelipkan pembatas pita sutra dan menoleh."),
                ("shiori", "Selamat bertemu, Amamiya-san. Tumben kamu muncul di sini dengan langkah sesantai itu."),
                ("chiasa", "Lagi nggak ada tenggat mendadak hari ini, Senpai. Rasanya lega banget."),
                ("shiori", "Hari yang tidak dikejar tenggat memang selalu terasa terlalu singkat. Mari manfaatkan beberapa menit ini dengan tenang."),
                ("chiasa", "Dengan senang hati, Saionji-senpai."),
            ],
        ],
        ("shiori", "yutaka"): [
            [
                ("nar", "Saionji Shiori sedang merapikan berkas tipis di atas meja saat melihatmu datang. Ia menoleh dengan senyum sopan yang terukur."),
                ("shiori", "Selamat bertemu lagi, Kisaragi-san. Kelihatannya kita punya jeda jadwal yang berdekatan hari ini."),
                ("yutaka", "Halo, Saionji-san. Baru kelar urusan fakultas juga ya?"),
                ("shiori", "Baru saja selesai merapikan beberapa catatan kuliah. Silakan duduk sebentar kalau kamu tidak sedang ditunggu siapa-siapa."),
                ("yutaka", "Nggak ditunggu siapa-siapa kok. Lumayan juga duduk sebentar di sini."),
                ("shiori", "Bagus kalau begitu."),
            ],
            [
                ("nar", "Shiori memutar pelan cangkir tehnya sambil menatapmu yang baru melangkah mendekat."),
                ("shiori", "Oh, Kisaragi-san. Tidak biasanya kamu terlihat santai di tempat setenang ini."),
                ("yutaka", "Sesekali butuh tempat yang nggak terlalu berisik juga, Saionji-san. Di kantin kadang kepalaku ikut pusing."),
                ("shiori", "Pendapat yang sulit kubantah. Kebetulan aku juga sedang mengambil jeda beberapa menit dari bacaanku."),
                ("yutaka", "Kalau begitu aku ikut istirahat sebentar di sini ya."),
                ("shiori", "Silakan saja, Kisaragi-san."),
            ],
            [
                ("nar", "Kamu melihat Shiori sedang menutup buku catatan bersampul gelapnya. Begitu kamu menyapa, ia mengangguk halus."),
                ("shiori", "Selamat bertemu, Kisaragi-san. Apakah ada hal menarik yang terjadi di kelasmu hari ini?"),
                ("yutaka", "Lumayan bikin ngantuk sih, makanya begitu bel selesai aku langsung keluar cari udara segar."),
                ("shiori", "Haha, jawaban yang cukup jujur. Setidaknya kamu tidak berpura-pura menyimak setiap kata dosen seperti sebagian mahasiswa di baris depan."),
                ("yutaka", "Wah, tajam juga pengamatanmu."),
                ("shiori", "Duduk saja sebentar kalau kamu punya waktu."),
            ],
        ],
        ("chiasa", "yutaka"): [
            [
                ("nar", "Amamiya Chiasa baru saja memasukkan papan sketsanya ke dalam tas kanvas. Begitu melihatmu mendekat, ia tersenyum tipis sambil memiringkan kepala."),
                ("chiasa", "Eh, Yutaka-kun? Kebetulan banget ketemu di sini. Lagi bolos jam baca ya?"),
                ("yutaka", "Enak aja bolos, kelasku memang sudah selesai dari tadi, Chiasa."),
                ("chiasa", "Haha, iya deh, percaya. Tapi tiap kali ketemu kamu mukamu tuh selalu kelihatan terlalu santai kayak nggak punya beban tugas."),
                ("yutaka", "Itu cuma karena aku nggak panik di depan orang aja."),
                ("chiasa", "Heh, sok keren banget. Ya sudah, mumpung ketemu, istirahat sebentar di sini nggak apa-apa kan?"),
            ],
            [
                ("nar", "Chiasa sedang membetulkan simpul pita hitam di rambutnya ketika ekor matanya menangkap sosokmu. Ia langsung melambai kecil."),
                ("chiasa", "Lho, Yutaka-kun? Tumben banget jalannya santai begini, nggak lagi buru-buru pulang ke apartemen?"),
                ("yutaka", "Nggak buru-buru kok. Apartemenku juga nggak bakal lari ke mana-mana. Kamu sendiri habis dari studio ya?"),
                ("chiasa", "Iya, tanganku sampai pegal banget habis pegang kuas sama pensil berjam-jam. Baru aja mau cari tempat duduk."),
                ("yutaka", "Pas banget kalau gitu, istirahat dulu sebentar di sini."),
                ("chiasa", "Sip, temani ngobrol bentar ya."),
            ],
            [
                ("nar", "Kamu mendapati Chiasa sedang memeriksa isi tas kecilnya sambil sedikit cemberut. Begitu melihatmu datang, ekspresinya langsung mencair."),
                ("chiasa", "Oh, Yutaka-kun! Pas banget, tadi aku hampir lupa kalau jadwal kuliahku hari ini sudah selesai semua dan malah nyari buku buat kelas besok."),
                ("yutaka", "Sampai lupa jadwal sendiri, kebanyakan begadang ngerjain gambar ya kamu?"),
                ("chiasa", "Bukan begadang kok, cuma kemarin terlalu fokus sedikit sampai lupa lihat jam!"),
                ("yutaka", "Itu sama aja namanya begadang, Chiasa. Duduk dulu sana."),
                ("chiasa", "Iya, iya, bawel banget sih."),
            ],
        ],
        ("yutaka", "chiasa"): [
            [
                ("nar", "Kisaragi Yutaka sedang bersandar santai sambil memeriksa jam tangan tipis di pergelangan tangannya. Begitu melihatmu datang, senyum jahil tipis muncul di wajahnya."),
                ("yutaka", "Eh, Chiasa? Pas banget lewat sini. Kelihatannya kamu baru bebas dari kelas ya?"),
                ("chiasa", "Iya, Yutaka-kun, baru aja beres. Yutaka-kun sendiri lagi nungguin seseorang di sini?"),
                ("yutaka", "Nggak nunggu siapa-siapa kok, cuma lagi malas langsung balik ke apartemen yang sepi banget."),
                ("chiasa", "Pantas kelihatan santai banget bersandar di situ."),
                ("yutaka", "Kebetulan kamu lewat, jadi ada alasan bagus buat nggak langsung pulang. Duduk bentar yuk."),
            ],
            [
                ("nar", "Yutaka menoleh begitu mendengar langkahmu, lalu mengangkat botol minuman dinginnya sebagai sapaan singkat."),
                ("yutaka", "Halo, Chiasa. Tumben nggak kelihatan bawa gulungan kertas gambar segede tabung bazoka itu."),
                ("chiasa", "Ih, itu kan tabung sketsa biasa, Yutaka-kun! Hari ini lagi kutitip di loker kampus soalnya berat."),
                ("yutaka", "Pantesan jalannya kelihatan lebih enteng. Kalau terus-terusan bawa barang seberat itu nanti bahumu malah pegal semua."),
                ("chiasa", "Tumben perhatian, biasanya cuma ngeledek."),
                ("yutaka", "Haha, sekali-kali kan boleh. Duduk bentar aja di sini kalau kamu lagi luang."),
            ],
            [
                ("nar", "Kamu melihat Yutaka sedang duduk santai sambil memandangi lalu-lalang orang di kejauhan. Begitu kamu menyapa, sorot matanya langsung melunak."),
                ("yutaka", "Lho, Chiasa? Kebetulan banget kita ketemu di sini hari ini."),
                ("chiasa", "Iya, kebetulan lewat aja. Yutaka-kun kelihatan agak capek hari ini?"),
                ("yutaka", "Cuma ngantuk dikit gara-gara kuliah tadi kepanjangan dan suara dosennya datar banget kayak suara kipas angin."),
                ("chiasa", "Haha, kejam banget perumpamaannya."),
                ("yutaka", "Tapi beneran bikin ngantuk kok. Ngobrol sebentar sama kamu lumayan biar melek lagi."),
            ],
        ],
    }

    # Dialog saat memilih "Janjikan bertemu lagi di sini besok pada waktu yang sama."
    KK_DAILY_PROMISE = {
        ("koita", "chiasa"): [
            ("chiasa", "Ko-nii, besok di jam yang sama ketemu lagi di sini yuk? Biar bisa ngobrol lebih santai tanpa buru-buru."),
            ("nar", "Koita tersenyum lebar sambil mengeluarkan ponselnya sebentar untuk melihat jadwal kuliahnya esok hari."),
            ("koita", "Besok di sini lagi? Boleh banget, Chi-chan! Kebetulan jadwalku besok juga lewat area sini dan nggak ada rapat mendadak."),
            ("chiasa", "Oke, kucatat ya. Jangan sampai lupa gara-gara keasyikan baca buku di ruang baca."),
            ("koita", "Haha, mana mungkin lupa kalau sudah janji sama kamu. Kalau aku sampai duluan, nanti sekalian kubeliin minuman hangat deh."),
            ("chiasa", "Asyik, aku tunggu kalau gitu. Sampai besok, Ko-nii."),
            ("nar", "Kalian sepakat untuk bertemu kembali di tempat ini esok hari pada waktu yang sama."),
        ],
        ("koita", "yutaka"): [
            ("yutaka", "Besok jam segini ketemu lagi di sini gimana, Koita? Sekalian istirahat bareng sebelum lanjut kegiatan."),
            ("nar", "Koita mengangguk cepat sambil memeriksa catatan jadwal di layar ponselnya."),
            ("koita", "Oke, boleh aja, Yutaka! Kebetulan besok di jam segini kelasku juga baru selesai."),
            ("yutaka", "Sip, awas jangan ketiduran atau keasyikan nolongin orang fotokopi sampai lupa waktu."),
            ("koita", "Hahaha, tenang aja, langsung kupasang pengingat di ponsel biar nggak meleset semenit pun. Sampai ketemu besok di sini ya."),
            ("nar", "Kalian sepakat untuk bertemu kembali di tempat ini esok hari pada waktu yang sama."),
        ],
        ("miyuki", "chiasa"): [
            ("chiasa", "Tachibana-senpai, besok di jam yang sama ketemu di sini lagi yuk kalau Senpai lagi luang."),
            ("nar", "Miyuki membuka buku agenda bersampul kremnya, menelusuri jadwal hari esok dengan jari telunjuknya, lalu mengangkat wajah dengan senyum hangat."),
            ("miyuki", "Boleh sekali, Chiasa-chan. Besok aku punya jeda sekitar tiga puluh menit di jam ini, jadi aku bisa datang tepat waktu."),
            ("chiasa", "Kalau tiba-tiba jadwal praktik Senpai molor nggak apa-apa kok, jangan sampai dipaksa buru-buru."),
            ("miyuki", "Nggak kok, aku justru senang rasanya punya janji kecil yang bisa kutunggu besok. Sampai jumpa besok ya, Chiasa-chan."),
            ("nar", "Kalian sepakat untuk bertemu kembali di tempat ini esok hari pada waktu yang sama."),
        ],
        ("miyuki", "yutaka"): [
            ("yutaka", "Besok di jam yang sama kita ketemu lagi di sini gimana, Tachibana-senpai?"),
            ("nar", "Miyuki memeriksa halaman agenda kecilnya lalu tersenyum lembut ke arahmu."),
            ("miyuki", "Tentu saja, Yutaka-kun. Besok aku usahakan menyelesaikan catatanku sedikit lebih awal supaya bisa duduk santai di sini."),
            ("yutaka", "Santai aja, Senpai, jangan sampai terburu-buru di jalan."),
            ("miyuki", "Terima kasih ya. Senang sekali bisa bikin janji sederhana seperti ini. Sampai jumpa besok."),
            ("nar", "Kalian sepakat untuk bertemu kembali di tempat ini esok hari pada waktu yang sama."),
        ],
        ("nagisa", "chiasa"): [
            ("chiasa", "Nagisa-senpai, besok di jam yang sama ketemu lagi di sini ya."),
            ("nar", "Nagisa mengerjap sesaat dengan pipi agak memerah karena kaget diajak janjian secara langsung, lalu buru-buru berdeham."),
            ("nagisa", "Eh, besok? Ya sudah deh, kebetulan aku juga memang lewat sini kok habis dari studio!"),
            ("chiasa", "Siap, aku datang tepat waktu kok, Senpai."),
            ("nagisa", "Bagus! Awas aja kalau kamu sendiri yang telat terus bikin aku berdiri sendirian kayak orang bingung!"),
            ("chiasa", "Haha, janji nggak telat."),
            ("nar", "Kalian sepakat untuk bertemu kembali di tempat ini esok hari pada waktu yang sama."),
        ],
        ("nagisa", "yutaka"): [
            ("yutaka", "Besok jam segini ketemu lagi di sini yuk, Nagisa."),
            ("nar", "Nagisa melirikmu sebentar lalu mendengus pelan sambil menahan senyum kecil."),
            ("nagisa", "Hmph, ya sudah, kebetulan jadwalku besok juga lewat sini kok. Awas ya kalau kamu sendiri yang lupa terus bikin aku nunggu!"),
            ("yutaka", "Tenang aja, kalau sudah bilang besok ya aku pasti datang."),
            ("nagisa", "Oke, kupegang omonganmu ya. Sampai ketemu besok, Yutaka!"),
            ("nar", "Kalian sepakat untuk bertemu kembali di tempat ini esok hari pada waktu yang sama."),
        ],
        ("harumi", "chiasa"): [
            ("chiasa", "Kujo-senpai, besok di waktu yang sama bisa ketemu di sini lagi?"),
            ("nar", "Harumi membuka buku agenda sakunya dan memeriksa kolom hari esok dengan teliti sebelum menuliskan satu tanda kecil dengan pena."),
            ("harumi", "Ya, besok pada jam ini aku bebas dari pengawasan reaksi di laboratorium. Baik, aku akan hadir tepat waktu, Amamiya-san."),
            ("chiasa", "Terima kasih, Senpai. Aku juga nggak bakal telat."),
            ("harumi", "Bagus. Sampai bertemu besok di tempat yang sama."),
            ("nar", "Kalian sepakat untuk bertemu kembali di tempat ini esok hari pada waktu yang sama."),
        ],
        ("harumi", "yutaka"): [
            ("yutaka", "Kujo-san, besok di jam yang sama ketemu di sini lagi gimana?"),
            ("nar", "Harumi membuka buku agenda sakunya sebentar lalu menandai jam tersebut dengan tulisan rapi."),
            ("harumi", "Besok aku tidak ada jadwal mendesak pada jam ini. Baik, aku akan datang tepat waktu, Kisaragi-kun."),
            ("yutaka", "Sip, aku usahakan sampai lima menit lebih awal biar nggak meleset."),
            ("harumi", "Ketepatan waktu selalu dihargai. Sampai bertemu besok."),
            ("nar", "Kalian sepakat untuk bertemu kembali di tempat ini esok hari pada waktu yang sama."),
        ],
        ("moeka", "chiasa"): [
            ("chiasa", "Moemoe-senpai, besok jam segini ketemu lagi di sini yuk!"),
            ("nar", "Mata biru Moeka langsung berbinar senang. Ia segera mengeluarkan ponselnya dan mengetik cepat."),
            ("moeka", "Asyik! Boleh banget, Chimian! Tunggu bentar, aku langsung pasang pengingat pakai bunyi alarm di ponsel sekarang biar nggak kelewatan."),
            ("chiasa", "Haha, sampai pasang alarm segala, Senpai."),
            ("moeka", "Wajib dong! Nggak mau bikin kamu nunggu sendirian besok. Sampai ketemu besok ya, Chimian!"),
            ("nar", "Kalian sepakat untuk bertemu kembali di tempat ini esok hari pada waktu yang sama."),
        ],
        ("moeka", "yutaka"): [
            ("yutaka", "Kohinata, besok jam segini ketemu lagi di sini gimana?"),
            ("nar", "Moeka menyeringai lebar lalu langsung mengeluarkan ponselnya untuk mencatat pengingat."),
            ("moeka", "Oke banget, Yutayuta! Langsung kupasang pengingat di ponsel biar nggak lupa di tengah jalan."),
            ("yutaka", "Sip, jangan sampai salah baca hari atau jam ya besok."),
            ("moeka", "Tenang aja, besok aku datang paling duluan! Sampai ketemu besok!"),
            ("nar", "Kalian sepakat untuk bertemu kembali di tempat ini esok hari pada waktu yang sama."),
        ],
        ("shiori", "chiasa"): [
            ("chiasa", "Saionji-senpai, besok di waktu yang sama boleh kita ketemu lagi di sini?"),
            ("nar", "Shiori menatapmu sejenak dengan senyum tipis yang tenang, lalu membuka buku saku kulit gelapnya untuk mencatat singkat."),
            ("shiori", "Baik, Amamiya-san. Aku akan menyisihkan waktu besok pada jam yang sama."),
            ("chiasa", "Terima kasih, Senpai. Aku datang tepat waktu besok."),
            ("shiori", "Aku menantikan percakapan kita selanjutnya. Sampai besok."),
            ("nar", "Kalian sepakat untuk bertemu kembali di tempat ini esok hari pada waktu yang sama."),
        ],
        ("shiori", "yutaka"): [
            ("yutaka", "Saionji-san, besok di jam yang sama ketemu lagi di sini gimana?"),
            ("nar", "Shiori mengangguk halus sambil mencatatnya dengan pena tipis di buku saku kulit gelapnya."),
            ("shiori", "Baik, Kisaragi-san. Akan kucatat dalam jadwalku besok. Pastikan kamu tidak datang terlambat."),
            ("yutaka", "Tenang aja, aku pasti datang tepat waktu."),
            ("shiori", "Kalau begitu sampai bertemu besok."),
            ("nar", "Kalian sepakat untuk bertemu kembali di tempat ini esok hari pada waktu yang sama."),
        ],
        ("chiasa", "yutaka"): [
            ("yutaka", "Chiasa, besok jam segini ketemu lagi di sini yuk."),
            ("nar", "Chiasa mengerjap sedikit lalu tersenyum jahil sambil memiringkan kepala."),
            ("chiasa", "Wah, tumben banget Yutaka-kun ngajak janjian duluan. Oke deh, kebetulan besok aku juga lewat sini."),
            ("yutaka", "Sip, sampai ketemu besok di sini."),
            ("chiasa", "Jangan sampai lupa terus bikin aku nunggu sendirian ya, Yutaka-kun!"),
            ("nar", "Kalian sepakat untuk bertemu kembali di tempat ini esok hari pada waktu yang sama."),
        ],
        ("yutaka", "chiasa"): [
            ("chiasa", "Yutaka-kun, besok di jam yang sama ketemu lagi di sini yuk."),
            ("nar", "Yutaka tersenyum tipis yang santai lalu mengangguk ringan."),
            ("yutaka", "Boleh aja, Chiasa. Kebetulan jadwalku besok juga longgar di jam segini."),
            ("chiasa", "Oke, aku pegang janjinya ya. Jangan lupa."),
            ("yutaka", "Siap, mana mungkin lupa. Sampai ketemu besok di sini."),
            ("nar", "Kalian sepakat untuk bertemu kembali di tempat ini esok hari pada waktu yang sama."),
        ],
    }

    # Sapaan saat janji bertemu ditepati di kk_do_talk
    KK_DAILY_KEEP_PROMISE = {
        ("koita", "chiasa"): [
            ("nar", "Kamu tiba di lokasi tepat sesuai janji kalian kemarin. Koita sudah berdiri menunggumu sambil menenteng dua botol minuman dan langsung tersenyum lega."),
            ("koita", "Wah, kamu beneran datang tepat waktu, Chi-chan! Aku juga baru sampai dua menit lalu kok."),
            ("chiasa", "Kan sudah janji kemarin, Ko-nii. Wah, sampai beliin minuman segala?"),
            ("koita", "Biar nggak haus sambil ngobrol. Ayo duduk dulu."),
        ],
        ("koita", "yutaka"): [
            ("nar", "Kamu tiba di lokasi tepat sesuai janji kalian kemarin. Koita langsung mengangkat tangan menyapa dengan wajah cerah."),
            ("koita", "Tepat waktu banget, Yutaka! Kupikir kamu bakal telat lima menit kayak biasanya."),
            ("yutaka", "Sekali-kali buktiin kalau aku juga bisa tepat waktu dong."),
            ("koita", "Haha, mantap deh. Sini duduk dulu."),
        ],
        ("miyuki", "chiasa"): [
            ("nar", "Kamu datang sesuai janji kemarin. Senyum hangat Miyuki langsung mengembang begitu melihat sosokmu mendekat."),
            ("miyuki", "Terima kasih sudah datang sesuai janji, Chiasa-chan. Aku senang sekali melihatmu hari ini."),
            ("chiasa", "Maaf nggak bikin Senpai nunggu terlalu lama kan?"),
            ("miyuki", "Sama sekali tidak, aku baru saja duduk kok. Rasanya lega melihatmu menepati janji kecil ini."),
        ],
        ("miyuki", "yutaka"): [
            ("nar", "Kamu datang sesuai janji kemarin. Miyuki segera menutup bukunya dan tersenyum lembut menyambutmu."),
            ("miyuki", "Terima kasih sudah menepati janji hari ini, Yutaka-kun. Duduklah dulu."),
            ("yutaka", "Maaf kalau bikin Senpai nunggu."),
            ("miyuki", "Tidak kok, kamu datang tepat waktu sekali. Aku senang kamu ingat."),
        ],
        ("nagisa", "chiasa"): [
            ("nar", "Kamu datang sesuai janji kalian kemarin. Nagisa sempat pura-pura sibuk melihat layar ponselnya, lalu menoleh cepat dengan wajah sedikit lega."),
            ("nagisa", "Akhirnya datang juga. Aku nggak nunggu lama kok, baru aja sampai semenit lalu!"),
            ("chiasa", "Syukurlah kalau gitu, Nagisa-senpai. Maaf kalau sempat nunggu sebentar."),
            ("nagisa", "Nggak apa-apa! Yang penting kamu beneran datang sesuai omonganmu kemarin."),
        ],
        ("nagisa", "yutaka"): [
            ("nar", "Kamu tiba tepat waktu sesuai janji kemarin. Nagisa langsung menurunkan bahunya yang tadi agak tegang."),
            ("nagisa", "Tumben banget kamu datang tepat waktu, Yutaka. Oke deh, kuhargai usahamu hari ini."),
            ("yutaka", "Sudah kubilang kemarin aku nggak bakal lupa kan."),
            ("nagisa", "Hmph, iya deh, kali ini kamu lulus."),
        ],
        ("harumi", "chiasa"): [
            ("nar", "Kamu tiba sesuai waktu yang disepakati kemarin. Harumi melirik jam tangannya sekilas lalu mengangguk puas."),
            ("harumi", "Tepat waktu, Amamiya-san. Aku menghargai orang yang menepati jadwal yang sudah disepakati."),
            ("chiasa", "Senang dengarnya, Kujo-senpai."),
            ("harumi", "Silakan duduk, aku juga baru tiba tiga menit yang lalu."),
        ],
        ("harumi", "yutaka"): [
            ("nar", "Kamu tiba sesuai waktu yang disepakati kemarin. Harumi memeriksa arlojinya sekilas lalu mengangguk tenang."),
            ("harumi", "Tepat waktu, Kisaragi-kun. Menepati janji sekecil ini membuat penilaianku terhadap ketepatan waktumu meningkat."),
            ("yutaka", "Syukurlah kalau lulus penilaianmu, Kujo-san."),
            ("harumi", "Ya, kamu lulus hari ini. Duduklah dulu."),
        ],
        ("moeka", "chiasa"): [
            ("nar", "Kamu datang sesuai janji kemarin. Moeka yang sudah menunggu sambil menggoyangkan kaki langsung melambai antusias."),
            ("moeka", "Chimian! Kamu beneran datang sesuai janji! Senang banget rasanya ditungguin dan disamperin begini!"),
            ("chiasa", "Iya dong, kan sudah sepakat kemarin, Moemoe-senpai. Senpai nggak nunggu kepanasan atau kedinginan kan?"),
            ("moeka", "Nggak sama sekali! Aku baru duduk dua menit lalu kok!"),
        ],
        ("moeka", "yutaka"): [
            ("nar", "Kamu datang sesuai janji kemarin. Moeka langsung menyeringai lebar dan melambaikan tangannya."),
            ("moeka", "Yutayuta! Tepat waktu banget! Makasih ya sudah nggak lupa sama janji kita kemarin!"),
            ("yutaka", "Sama-sama, Kohinata. Kamu juga datang cepat banget ternyata."),
            ("moeka", "Haha, alarm ponselku ampuh banget tadi!"),
        ],
        ("shiori", "chiasa"): [
            ("nar", "Kamu tiba sesuai janji kemarin. Shiori mengangkat cangkirnya sedikit sambil tersenyum tipis yang tulus."),
            ("shiori", "Tepat sesuai waktu yang kita sepakati, Amamiya-san. Menepati janji kecil selalu menjadi pertanda yang baik."),
            ("chiasa", "Terima kasih sudah menunggu, Saionji-senpai."),
            ("shiori", "Tidak lama sama sekali. Silakan duduk."),
        ],
        ("shiori", "yutaka"): [
            ("nar", "Kamu tiba sesuai janji kemarin. Shiori menutup buku catatannya dengan senyum tipis yang tenang."),
            ("shiori", "Tepat waktu, Kisaragi-san. Rupanya kamu memang memegang kata-katamu sendiri."),
            ("yutaka", "Tentu aja, Saionji-san. Kalau sudah bilang datang ya aku datang."),
            ("shiori", "Sikap yang menyenangkan. Silakan duduk."),
        ],
        ("chiasa", "yutaka"): [
            ("nar", "Kamu datang tepat waktu sesuai janji kalian kemarin. Chiasa langsung tersenyum jahil sambil melangkah mendekat."),
            ("chiasa", "Wah, Yutaka-kun beneran datang tepat waktu! Kukira bakal lupa di jalan."),
            ("yutaka", "Nggak bakal lupa kalau sudah janji sama kamu, Chiasa."),
            ("chiasa", "Heh, bagus deh. Ayo duduk sebentar."),
        ],
        ("yutaka", "chiasa"): [
            ("nar", "Kamu tiba sesuai janji kemarin. Yutaka berdiri tegak dari sandarannya dan tersenyum santai."),
            ("yutaka", "Tepat waktu juga kamu, Chiasa. Baru aja aku sampai beberapa menit lalu."),
            ("chiasa", "Syukurlah nggak telat, Yutaka-kun."),
            ("yutaka", "Nggak kok, malah pas banget."),
        ],
    }

    # Dialog saat memilih "Balas sapaannya lalu pamit."
    KK_DAILY_BYE = {
        ("koita", "chiasa"): [
            ("chiasa", "Maaf ya, Ko-nii, aku cuma mampir nyapa sebentar soalnya masih ada urusan yang harus diberesin dulu. Duluan ya!"),
            ("koita", "Oh, oke, Chi-chan! Jangan buru-buru di jalan, nanti kita ketemu lagi di rumah ya."),
            ("chiasa", "Iya, sampai nanti, Ko-nii."),
            ("nar", "Koita melambaikan tangan dengan senyum hangat sebelum kembali menekuni buku catatannya."),
        ],
        ("koita", "yutaka"): [
            ("yutaka", "Oke deh, aku cuma mampir nyapa sebentar, masih ada urusan lain yang harus kukejar. Duluan ya, Koita."),
            ("koita", "Sip, semangat ya, Yutaka! Kabari aja lewat pesan kalau nanti lagi senggang mau makan bareng."),
            ("yutaka", "Oke, nanti kukabari. Duluan."),
            ("nar", "Koita mengangguk ramah sambil kembali merapikan barang-barangnya di meja."),
        ],
        ("miyuki", "chiasa"): [
            ("chiasa", "Aku pamit duluan ya, Tachibana-senpai. Jangan lupa istirahat di sela baca catatan!"),
            ("miyuki", "Iya, terima kasih sudah mampir menyapa, Chiasa-chan. Hati-hati di jalan ya."),
            ("chiasa", "Sampai ketemu lagi, Senpai."),
            ("nar", "Miyuki tersenyum lembut sambil mengantarmu dengan pandangan sebelum kembali membuka bukunya."),
        ],
        ("miyuki", "yutaka"): [
            ("yutaka", "Aku jalan duluan ya, Tachibana-senpai. Jangan sampai lupa makan ya nanti."),
            ("miyuki", "Haha, siap, Yutaka-kun. Terima kasih sudah menyapa dan mengingatkan. Hati-hati di jalan ya."),
            ("yutaka", "Sampai jumpa lagi, Senpai."),
            ("nar", "Miyuki melambaikan tangan pelan lalu kembali merapikan tumpukan catatannya."),
        ],
        ("nagisa", "chiasa"): [
            ("chiasa", "Ya sudah, aku nggak ganggu lama-lama ya, Nagisa-senpai. Semangat ngerjain tugasnya!"),
            ("nagisa", "Iya, makasih, Chiasa! Kamu juga jangan lupa jaga kesehatan."),
            ("chiasa", "Oke, duluan ya, Senpai."),
            ("nar", "Nagisa melambai singkat sebelum kembali menunduk menghadap pekerjaannya."),
        ],
        ("nagisa", "yutaka"): [
            ("yutaka", "Oke deh, nggak kuganggu lagi biar tugasmu cepat kelar. Duluan ya, Nagisa."),
            ("nagisa", "Iya, sana pergi! Tapi makasih sudah mampir nyapa tadi, Yutaka."),
            ("yutaka", "Santai. Semangat ya."),
            ("nar", "Nagisa mengibaskan tangannya sambil menahan senyum tipis lalu kembali sibuk dengan alat gambarnya."),
        ],
        ("harumi", "chiasa"): [
            ("chiasa", "Kalau gitu aku pamit dulu ya, Kujo-senpai, biar Senpai bisa lanjut fokus."),
            ("harumi", "Baik, Amamiya-san. Terima kasih sudah menyapa. Semoga kegiatanmu hari ini berjalan lancar."),
            ("chiasa", "Terima kasih, Senpai. Permisi."),
            ("nar", "Harumi mengangguk sopan lalu kembali membuka halaman buku catatannya."),
        ],
        ("harumi", "yutaka"): [
            ("yutaka", "Aku pamit duluan ya, Kujo-san. Jangan terlalu capek di lab."),
            ("harumi", "Baik, Kisaragi-kun. Terima kasih sudah mampir. Sampai bertemu di kesempatan berikutnya."),
            ("yutaka", "Sampai jumpa, Kujo-san."),
            ("nar", "Harumi menundukkan kepala sedikit sebelum kembali menatap lembaran datanya."),
        ],
        ("moeka", "chiasa"): [
            ("chiasa", "Aku pamit duluan ya, Moemoe-senpai! Nanti kita ngobrol lagi kalau lagi luang."),
            ("moeka", "Oke, Chimian! Semangat terus ya, hati-hati di jalan, dadah!"),
            ("chiasa", "Dadah, Senpai!"),
            ("nar", "Moeka melambaikan kedua tangannya dengan ceria sebelum kembali sibuk dengan barang-barangnya."),
        ],
        ("moeka", "yutaka"): [
            ("yutaka", "Duluan ya, Kohinata. Semangat beresin tugas desainnya."),
            ("moeka", "Sip, makasih ya, Yutayuta! Hati-hati di jalan, sampai ketemu lagi!"),
            ("yutaka", "Iya, sampai ketemu lagi."),
            ("nar", "Moeka tersenyum cerah sambil melambai lalu kembali membolak-balik buku sketsanya."),
        ],
        ("shiori", "chiasa"): [
            ("chiasa", "Kalau begitu aku pamit duluan ya, Saionji-senpai. Terima kasih waktunya."),
            ("shiori", "Sama-sama, Amamiya-san. Semoga sisa harimu menyenangkan. Sampai jumpa lagi."),
            ("chiasa", "Permisi, Senpai."),
            ("nar", "Shiori tersenyum halus dan mengangguk sopan saat kamu beranjak pergi."),
        ],
        ("shiori", "yutaka"): [
            ("yutaka", "Aku jalan duluan ya, Saionji-san. Sampai ketemu lagi di kampus."),
            ("shiori", "Baik, Kisaragi-san. Sampai bertemu kembali di kesempatan berikutnya."),
            ("yutaka", "Duluan ya."),
            ("nar", "Shiori mengangguk anggun sebelum kembali menyesap tehnya dengan tenang."),
        ],
        ("chiasa", "yutaka"): [
            ("yutaka", "Duluan ya, Chiasa. Jangan sampai pulangnya kemalaman."),
            ("chiasa", "Iya, tenang aja, Yutaka-kun! Hati-hati di jalan juga ya."),
            ("yutaka", "Sampai ketemu lagi."),
            ("nar", "Chiasa melambaikan tangan sambil tersenyum ringan sebelum kembali merapikan tas kanvasnya."),
        ],
        ("yutaka", "chiasa"): [
            ("chiasa", "Aku pamit duluan ya, Yutaka-kun, masih ada yang harus kucari."),
            ("yutaka", "Oke, Chiasa. Hati-hati di jalan, kabari aja kalau butuh apa-apa."),
            ("chiasa", "Iya, makasih, Yutaka-kun."),
            ("nar", "Yutaka mengangkat tangannya singkat dengan senyum santai saat kamu melangkah pergi."),
        ],
    }

    # Dialog khusus untuk opsi Harumi (H01-A)
    KK_DAILY_H01 = {
        "chiasa": [
            ("chiasa", "Kujo-senpai, soal bagian pembahasan dari buku yang pernah kita baca bareng dulu itu, boleh aku tanya lagi dari langkah awalnya? Kemarin aku sempat kepikiran bagian logikanya."),
            ("nar", "Mata Harumi langsung tampak sedikit lebih cerah mendengar kamu masih mengingat rincian bacaan kalian sebelumnya. Ia membuka halaman kosong buku sakunya dan mengambil pena tinta tipis."),
            ("harumi", "Tentu saja, Amamiya-san. Mari kita periksa lagi dari langkah pertama. Inti kesalahan yang sering terjadi ada pada asumsi variabel awalnya yang dianggap tetap padahal lingkungannya berubah."),
            ("nar", "Ia menggambar dua garis sumbu kecil dengan gerakan tangan sangat stabil, lalu menunjuk titik potongnya menggunakan ujung pena."),
            ("chiasa", "Oh, berarti begitu suhu atau kondisinya berubah sedikit aja, seluruh garis perhitungannya langsung ikut bergeser ya?"),
            ("harumi", "Tepat sekali. Banyak mahasiswa langsung memasukkan angka ke rumus akhir tanpa memeriksa batas syarat di awal. Pemahamanmu jauh lebih cepat daripada yang kubayangkan."),
            ("chiasa", "Soalnya penjelasan Kujo-senpai rapi banget, jadi gampang kebayang urutannya."),
            ("harumi", "Terima kasih. Kalau kamu masih penasaran dengan bagian lanjutannya, lain kali aku bisa membawa buku referensi pendukungnya."),
            ("chiasa", "Boleh banget, Senpai. Terima kasih sudah mau jelasin ulang."),
            ("nar", "Kalian menghabiskan sepuluh menit membedah ulang catatan tersebut dengan tenang sebelum Harumi menutup penanya dengan raut puas."),
        ],
        "yutaka": [
            ("yutaka", "Kujo-san, soal pembahasan dari buku yang dulu sempat kita baca bareng, boleh kita lihat lagi dari langkah pertamanya? Ada satu bagian yang masih bikin aku penasaran."),
            ("nar", "Sorot mata Harumi tampak sedikit melunak begitu menyadari kamu masih mengingat detail bacaan kalian. Ia segera membuka buku catatan kecilnya dan menyiapkan pena."),
            ("harumi", "Tentu, Kisaragi-kun. Mari kita periksa dari langkah pertama. Bagian yang paling sering membuat orang keliru adalah menganggap variabel pengiringnya selalu konstan."),
            ("nar", "Ia menggambar dua kurva pembanding kecil di halaman berkotak buku sakunya dengan sangat presisi."),
            ("yutaka", "Jadi begitu satu faktor di awal bergeser, hasil akhirnya langsung melenceng jauh ya? Mirip banget sama model keseimbangan di kelasku."),
            ("harumi", "Perbandingan yang cukup tepat. Di ilmu alam maupun ekonomi, asumsi awal yang keliru selalu membesarkan kesalahan di ujung perhitungan."),
            ("yutaka", "Pantesan kemarin waktu aku mikirin ulang kok rasanya ada langkah yang loncat. Sekarang baru nyambung."),
            ("harumi", "Senang sekali bisa mendiskusikannya dengan seseorang yang benar-benar menyimak sampai tuntas, Kisaragi-kun."),
            ("yutaka", "Makasih sudah mau ngulang penjelasannya, Kujo-san."),
            ("nar", "Selama sepuluh menit berikutnya kalian mengurai ulang kerangka soal itu bersama hingga Harumi menutup catatannya dengan anggukan puas."),
        ],
    }

    # Dialog khusus opsi "Bawakan makanan untuk Miyuki."
    KK_DAILY_MIYUKI_FOOD = {
        "chiasa": [
            ("chiasa", "Tachibana-senpai, kebetulan tadi aku mampir beli roti lapis hangat sama teh madu di kedai depan. Aku beli dua porsi, makan dulu yuk sebelum Senpai lanjut baca lagi."),
            ("nar", "Kamu meletakkan kantong kertas hangat berisi roti lapis isi telur lembut dan botol teh di depan Miyuki. Gerakan tangannya di atas buku catatan langsung berhenti, matanya sedikit melebar kaget."),
            ("miyuki", "Eh, Chiasa-chan? Kamu sengaja membelikan ini buatku? Aduh, nggak usah repot-repot begitu, sebentar biar kuganti uangnya ya..."),
            ("nar", "Miyuki sudah hendak membuka ritsleting tasnya untuk mengambil dompet, tetapi kamu segera menahan pelan dengan gelengan kepala."),
            ("chiasa", "Nggak usah diganti kok, Senpai! Anggap aja ganti jajan soalnya Senpai kan sering banget mikirin orang lain. Ayo dimakan mumpung rotinya masih hangat."),
            ("nar", "Miyuki menatap kantong kertas hangat itu beberapa detik dengan senyum lembut yang tampak jauh lebih santai dari biasanya, lalu menutup buku tebalnya dan menarik dompetnya kembali."),
            ("miyuki", "Kalau begitu kuterima dengan senang hati. Terima kasih banyak ya, Chiasa-chan. Jujur saja, perutku memang sudah mulai kosong dari tadi tapi aku terlalu malas turun cari makan sendirian."),
            ("chiasa", "Tuh kan, ketahuan belum sempat makan. Ayo dimakan pelan-pelan bareng aku."),
            ("miyuki", "Hmm, rotinya lembut sekali, masih hangat pula. Rasanya jauh lebih enak kalau dimakan berdua begini ya."),
            ("nar", "Kalian duduk berdampingan menghabiskan makanan hangat tersebut sambil berbincang ringan tentang keseharian kampus hampir satu jam penuh. Raut lelah di sekitar mata Miyuki tampak mereda cukup banyak saat ia akhirnya selesai makan."),
        ],
        "yutaka": [
            ("yutaka", "Tachibana-senpai, tadi kebetulan aku beli roti lapis hangat sama teh madu lebih satu di kedai depan. Nih, makan dulu sebelum lanjut baca lagi."),
            ("nar", "Kamu meletakkan kantong kertas hangat berisi roti lapis dan botol teh di hadapan Miyuki. Tangannya berhenti di atas pena, lalu ia menatapmu dengan mata agak melebar."),
            ("miyuki", "Ara, Yutaka-kun? Kamu repot-repot membelikan makan buatku? Tunggu, biar kuganti dulu uangnya ya..."),
            ("nar", "Kamu segera menggeleng tenang sambil menggeser botol teh madu itu lebih dekat ke tangannya."),
            ("yutaka", "Nggak perlu diganti, Senpai. Sekali-kali gantian dong, biasanya kan Senpai terus yang repot mikirin orang lain. Ayo dimakan mumpung masih hangat."),
            ("nar", "Miyuki terdiam sebentar, lalu sebuah senyum hangat yang terasa jauh lebih ringan muncul di bibirnya. Ia menutup map catatannya dan membuka bungkus roti lapis tersebut."),
            ("miyuki", "Baiklah, kalau begitu kuterima tanpa sungkan ya. Terima kasih banyak, Yutaka-kun. Ternyata enak juga rasanya dibawakan makan tanpa harus meminta duluan."),
            ("yutaka", "Nah, gitu dong. Makan yang tenang dulu, bukunya nggak bakal lari ke mana-mana."),
            ("miyuki", "Enak sekali rotinya. Apalagi teh madunya pas banget buat tenggorokan."),
            ("nar", "Kalian duduk mengobrol santai sambil menghabiskan makanan hangat itu hampir satu jam penuh hingga bahu Miyuki tampak jauh lebih rileks daripada saat kamu baru tiba."),
        ],
    }

    # Dialog khusus opsi "Puji pastry yang ia bawa." (Kafe Komorebi · Sabtu)
    KK_DAILY_MIYUKI_PASTRY = {
        "chiasa": [
            ("nar", "Di meja sebelah cangkir teh Miyuki tergeletak sebuah kotak kue kecil yang baru terbuka sebagian, menebarkan aroma mentega panggang dan vanila yang harum. Miyuki menaruh satu potong kecil di atas serbet bersih lalu menyodorkannya kepadamu."),
            ("miyuki", "Kebetulan aku bawa sedikit dari apartemen. Kalau Chiasa-chan mau, cicipin satu potong dong, aku ingin dengar pendapat jujurmu."),
            ("nar", "Kamu mengambil gigitan pertama. Kulit pastry itu langsung pecah renyah di mulut, diikuti lembutnya krim vanila yang sama sekali tidak terasa berat."),
            ("chiasa", "Wah, lapisan pastry buatan Tachibana-senpai hari ini renyah banget! Manis krimnya juga pas, nggak bikin enek sama sekali. Beneran enak banget, Senpai!"),
            ("nar", "Pipi Miyuki langsung merona lembut mendengar pujianmu yang begitu spesifik. Ia tersenyum senang sambil menatap sisa potongan di dalam kotak."),
            ("miyuki", "Syukurlah kalau Chiasa-chan suka! Tadi aku sempat khawatir lipatan menteganya kurang mengembang waktu masuk oven. Rupanya kamu suka yang rasa vanila ringan seperti ini ya?"),
            ("chiasa", "Suka banget, Senpai! Rasanya cocok banget diminum bareng teh hangat di Komorebi."),
            ("miyuki", "Akan kuingat baik-baik selera Chiasa-chan. Lain kali aku ingin coba membuatkan satu yang lebih spesial lagi."),
            ("nar", "Miyuki menutup kembali kotak kecilnya dengan raut gembira yang tulus, tampak jelas menyimpan pujianmu baik-baik."),
        ],
        "yutaka": [
            ("nar", "Di samping cangkir teh Miyuki tergeletak sebuah kotak kue kecil yang baru terbuka sebagian, menebarkan aroma mentega panggang dan vanila yang lembut. Miyuki meletakkan satu potong kecil di piring kertas lalu menyodorkannya kepadamu."),
            ("miyuki", "Kebetulan tadi aku memanggang sedikit di apartemen. Kalau Yutaka-kun nggak keberatan, cicipin satu potong ya, aku ingin tahu rasanya menurutmu."),
            ("nar", "Kamu mencicipinya pelan. Tekstur kulit luarnya renyah dengan wangi mentega yang bersih, berpadu manis tipis krim di bagian dalam."),
            ("yutaka", "Wah, lapisan pastry buatan Tachibana-senpai hari ini renyah banget. Manisnya juga pas, nggak berlebihan sampai nutupin wangi menteganya. Serius enak banget, Senpai."),
            ("nar", "Senyum lebar yang tulus langsung merekah di wajah Miyuki mendengar komentar lugasmu. Ia menatap kotak kuenya dengan mata berbinar senang."),
            ("miyuki", "Benarkah enak menurutmu, Yutaka-kun? Tadi aku sempat ragu apakah takaran gulanya terlalu tipis untuk seleramu. Rupanya kamu memang suka rasa yang ringan seperti ini ya."),
            ("yutaka", "Iya, yang kayak gini justru bisa kumakan beberapa potong sekaligus tanpa terasa enek."),
            ("miyuki", "Kucatat baik-baik di kepalaku ya. Lain kali aku ingin mencoba memanggang satu yang khusus sesuai seleramu."),
            ("nar", "Miyuki merapikan kembali kotak kue kecil itu dengan senyum hangat yang bertahan lama."),
        ],
    }

    KK_DAILY_AFTERGLOW_REPLY = {
        ("miyuki", "chiasa"): ("chiasa", "Sama-sama, Tachibana-senpai. Aku senang dengarnya kalau Senpai merasa lebih tenang sekarang."),
        ("miyuki", "yutaka"): ("yutaka", "Santai aja, Tachibana-senpai. Aku nggak masalah kok soal itu."),
        ("koita", "chiasa"): ("chiasa", "Wah, tajam juga mata Ko-nii merhatiin hal kayak gitu."),
        ("koita", "yutaka"): ("yutaka", "Perasaanmu aja kali terlalu banyak mikir, Koita."),
        ("nagisa", "chiasa"): ("chiasa", "Iya deh, iya, aku nggak salah paham kok, Nagisa-senpai."),
        ("nagisa", "yutaka"): ("yutaka", "Iya, kebetulan lewat ya, Nagisa. Percaya kok."),
    }

    KK_NAGISA_HEARD_REPLY = {
        "chiasa": [
            ("nar", "Kamu menemukan Nagisa duduk diam memandangi kedua tangannya yang terlipat di atas meja. Tidak ada tawa atau nada ketus seperti biasanya saat ia akhirnya mengangkat pandangan menatapmu."),
            ("nagisa", "...Dia akhirnya jawab pesanku, Chiasa."),
            ("chiasa", "Ko-nii? Apa yang dia bilang, Nagisa-senpai?"),
            ("nagisa", "Dia bilang kita teman masa kecil. Seperti itu saja. Sopan banget, rapi banget, sampai aku bahkan nggak tahu bagian mana yang boleh kusebut menyakitkan."),
            ("chiasa", "Senpai nggak harus pura-pura kuat di depanku sekarang kok."),
            ("nagisa", "...Aku nggak nangis. Aku cuma perlu duduk diam sebentar sampai kepalaku beres mikirin semuanya. Makasih sudah dengerin tanpa ngeledek, Chiasa."),
            ("nar", "Nagisa menunduk menatap meja dengan bahu sedikit bergetar, lalu menarik napas panjang sebelum kembali menutup perasaannya pelan-pelan."),
        ],
        "yutaka": [
            ("nar", "Kamu menemukan Nagisa duduk diam memandangi kedua tangannya yang terlipat di atas meja. Begitu kamu berhenti di sebelahnya, ia tidak melontarkan ledekan seperti biasanya."),
            ("nagisa", "...Koita akhirnya jawab aku, Yutaka."),
            ("yutaka", "Dia bilang apa, Nagisa?"),
            ("nagisa", "Dia bilang kita teman masa kecil. Seperti itu saja. Nadanya lembut banget, sopan banget, sampai aku sendiri bingung kenapa dadaku sesak banget dengarnya."),
            ("yutaka", "Kamu nggak perlu buru-buru pura-pura semuanya baik-baik aja sekarang."),
            ("nagisa", "...Aku nggak bakal nangis di sini. Aku cuma perlu duduk tenang sebentar biar kepalaku nggak penuh. Makasih sudah dengerin tanpa ngeledek, Yutaka."),
            ("nar", "Nagisa menarik napas pelan sambil menggenggam ujung lengan bajunya erat-erat, mencoba menelan jawaban yang selama bertahun-tahun paling ia takutkan."),
        ],
    }

    # Adegan aktivitas harian 4 jam (membuat waktu 1 slot terasa benar-benar dijalani)
    KK_ACT_SCENES = {
        "makan": {
            "Kantin Pusat": [
                [
                    ("nar", "Kamu mengantre di depan konter makanan hangat Kantin Pusat, mengambil seporsi nasi kari katsu bersama semangkuk sup miso yang masih mengepul, lalu mencari bangku kosong di dekat jendela kaca."),
                    ("nar", "Di meja-meja sekitar, mahasiswa dari berbagai fakultas ramai membicarakan tugas kelas, rencana akhir pekan, dan gosip kecil kampus. Suasana bising yang wajar itu justru membuatmu merasa sedikit lebih membumi di dunia ini."),
                    ("nar", "Kamu menyantap seluruh hidangan pelan-pelan hingga tandas, lalu duduk menghabiskan teh jelai dingin sambil meluruskan kaki. Perutmu kembali tenang dan tenagamu terasa pulih."),
                ],
                [
                    ("nar", "Kamu memilih menu harian berupa ikan panggang, nasi hangat, dan tumis bayam di Kantin Pusat. Petugas konter menyodorkan nampan dengan senyum ramah yang terburu-buru."),
                    ("nar", "Sambil makan di meja panjang pojok ruangan, kamu memperhatikan arus mahasiswa yang datang dan pergi membawa buku catatan serta tas studio. Beberapa menit yang tenang tanpa dikejar percakapan berat terasa menyegarkan."),
                    ("nar", "Setelah mengembalikan nampan ke rak cucian, rasa laparmu hilang sepenuhnya dan tubuhmu kembali siap melanjutkan hari."),
                ],
            ],
            "Kafe Komorebi": [
                [
                    ("nar", "Begitu lonceng pintu Kafe Komorebi berdenting, aroma kopi sangrai dan roti panggang mentega langsung menyambutmu. Kamu memilih kursi di dekat meja konter kayu."),
                    ("Ito Shinji", "Selamat datang. Hari ini mau roti panggang telur hangat sama kopi, atau teh hitam seperti kemarin?"),
                    ("nar", "Pemilik kafe itu menyajikan pesananmu dengan gerakan tenang yang sudah sangat terlatih. Kamu makan pelan sambil mendengarkan musik akustik pelan yang mengalun dari sudut ruangan."),
                    ("nar", "Kehangatan kopi dan roti yang renyah membuat perutmu tenang sekaligus meredakan sisa penat di kepalamu."),
                ],
                [
                    ("nar", "Kamu duduk di meja dekat jendela Kafe Komorebi dan memesan seporsi pasta rumahan beserta segelas teh es. Dari balik konter, Ito Shinji mengangguk tenang dan mulai menyiapkan hidangan."),
                    ("nar", "Sambil makan, kamu memandangi pejalan kaki yang melintas di depan gerbang kampus di balik tirai tipis. Waktu mengalir pelan tanpa terasa terburu-buru."),
                    ("Ito Shinji", "Pelan-pelan saja makannya, masih banyak waktu sebelum jam berikutnya."),
                    ("nar", "Kamu menghabiskan makananmu sampai bersih dan meninggalkan meja dengan tubuh yang terasa jauh lebih bugar."),
                ],
            ],
            "Restoran": [
                [
                    ("nar", "Kamu melangkah masuk ke sebuah restoran kecil di Pusat Kota dan memilih meja sudut yang cukup tenang. Pelayan membawakan handuk hangat dan buku menu bergambar rapi."),
                    ("nar", "Sepuluh menit kemudian, seporsi nasi daging panggang saus jahe hangat tiba bersama sup panas. Kamu menyantapnya tanpa tergesa sambil mendengarkan denting piring samar dari arah dapur."),
                    ("nar", "Istirahat makan yang layak kali ini benar-benar mengisi ulang tenagamu untuk sisa hari."),
                ],
            ],
        },
        "kerja": {
            "Kafe Komorebi": [
                [
                    ("nar", "Kamu mengikat celemek kain gelap di belakang konter Kafe Komorebi dan langsung membantu Ito Shinji menyiapkan cangkir bersih serta menata kue di etalase kaca."),
                    ("Ito Shinji", "Hari ini pengunjung lumayan ramai di jam jeda kuliah. Tolong bantu antar pesanan meja tiga dan lima, sisanya biar saya yang seduh di sini."),
                    ("nar", "Selama beberapa jam berikutnya, lonceng pintu terus berdenting hampir tanpa henti. Kamu mencatat pesanan, mengantar nampan kopi panas, mengelap meja yang baru ditinggalkan pelanggan, hingga akhirnya arus tamu mulai mereda."),
                    ("Ito Shinji", "Kerja bagus hari ini. Ini upahmu, sekalian bawa pulang sisa roti panggang satu bungkus kalau mau."),
                    ("nar", "Bahu dan kakimu terasa cukup pegal, tetapi lembaran upah sebesar ¥3.000 masuk rapi ke saldomu."),
                ],
                [
                    ("nar", "Kamu memulai giliran kerja paruh waktu di Kafe Komorebi dengan menggiling biji kopi segar dan menyusun gelas es di rak bawah konter."),
                    ("nar", "Menjelang pertengahan jam kerja, dua rombongan mahasiswa datang sekaligus dan membuat suasana kafe mendadak sibuk. Dengan arahan singkat yang tenang dari Ito Shinji, seluruh pesanan berhasil keluar tanpa satu pun yang keliru."),
                    ("Ito Shinji", "Kamu makin cepat tangkap alurnya sekarang. Terima kasih bantuannya hari ini."),
                    ("nar", "Setelah melepas celemek dan mencuci tangan, kamu menerima upah ¥3.000 dengan napas lega meski tenagamu cukup terkuras."),
                ],
            ],
            "Studio Foto": [
                [
                    ("nar", "Kamu melapor di meja depan Studio Foto di Pusat Kota dan langsung diminta membantu kru menata gulungan layar latar belakang serta menggeser kaki lampu studio."),
                    ("Kru Studio", "Tolong bantu rapikan kabel di sebelah kanan itu dan pastikan nggak ada yang melintang di jalur model ya. Habis sesi ini kita bereskan reflektornya."),
                    ("nar", "Beberapa jam berlalu di tengah bunyi jepretan kamera beruntun, arahan pencahayaan, serta bau samar kopi instan di sudut ruang kru. Begitu sesi selesai dan seluruh peralatan masuk kembali ke koper kerasnya, bahumu terasa lumayan pegal."),
                    ("nar", "Koordinator studio menyerahkan amplop upah sebesar ¥3.000 sambil mengucapkan terima kasih sebelum kamu melangkah keluar."),
                ],
            ],
        },
        "belajar": {
            "Perpustakaan Pusat": [
                [
                    ("nar", "Kamu memilih meja baca di baris belakang lantai dua Perpustakaan Pusat, membuka buku catatan kuliah, lalu mulai merangkum bab-bab yang kemarin sempat tertinggal."),
                    ("nar", "Di tengah kesunyian yang hanya diisi bunyi halaman kertas dibalik dan goresan pensil mahasiswa di meja sebelah, fokusmu perlahan menyatu. Satu per satu konsep yang tadinya terasa asing mulai tersusun masuk akal di kepalamu."),
                    ("nar", "Ketika kamu akhirnya menutup buku dan meregangkan leher, beberapa jam sudah berlalu tanpa terasa. Kepalamu agak berat, tetapi catatanmu kini jauh lebih siap untuk ujian mendatang."),
                ],
                [
                    ("nar", "Kamu mengambil dua buku referensi dari rak tinggi Perpustakaan Pusat lalu duduk di meja dekat jendela lebar."),
                    ("nar", "Kamu membandingkan definisi, menuliskan ulang poin-poin inti dengan bahasamu sendiri, dan menandai bagian yang perlu ditanyakan di kelas berikutnya. Sesekali kamu mengistirahatkan mata menatap pepohonan di luar kaca sebelum kembali menunduk."),
                    ("nar", "Selesai mengembalikan buku ke troli petugas, tubuhmu terasa agak lelah, tetapi penguasaan materimu bertambah mantap."),
                ],
            ],
            "Bimbel": [
                [
                    ("nar", "Kamu duduk di ruang belajar tenang di Bimbel dekat stasiun, mengeluarkan bundelan latihan soal dan mulai mengerjakannya satu per satu dengan penunjuk waktu di samping meja."),
                    ("nar", "Beberapa soal sempat membuatmu berhenti lama mengulang perhitungan dari baris pertama sampai akhirnya menemukan letak kekeliruannya. Begitu jawaban akhirnya cocok dengan lembar kunci, rasa lega kecil muncul di dadamu."),
                    ("nar", "Setelah merapikan seluruh berkas latihan ke dalam tas, kepalamu terasa penuh tetapi pemahaman materimu meningkat nyata."),
                ],
            ],
            "Asrama Putri": [
                [
                    ("nar", "Kamu duduk di ruang baca kecil lantai bawah Asrama Putri yang tenang, menyusun catatan kuliah di atas meja kayu sambil mengulang materi minggu ini halaman demi halaman."),
                    ("nar", "Tanpa gangguan suara ramai dari luar, kamu berhasil menyelesaikan seluruh ringkasan yang sempat tertunda. Saat merapikan pena dan bangkit berdiri, matamu terasa agak penat tetapi pikiranmu jauh lebih teratur."),
                ],
            ],
        },
        "santai": {
            "Taman Kampus": [
                [
                    ("nar", "Kamu duduk di bangku kayu di bawah pohon rindang Taman Kampus sambil meluruskan kaki. Daun-daun bergoyang pelan diterpa angin, mematahkan cahaya matahari menjadi bintik-bintik terang di jalur setapak."),
                    ("nar", "Beberapa mahasiswa berjalan melintas sambil tertawa membahas kegiatan klub, sementara seekor kucing kampus melangkah santai menyeberangi rumput lalu meringkuk di bawah semak."),
                    ("nar", "Untuk beberapa jam kamu membiarkan pikiranmu lepas dari semua perhitungan rumit dan kontrak Sistem. Saat bangkit berdiri, bahumu terasa jauh lebih ringan."),
                ],
            ],
            "Taman Lingkungan": [
                [
                    ("nar", "Kamu duduk sendirian di bangku kayu Taman Lingkungan yang tenang, mendengarkan suara samar anak-anak bermain di ujung jalan serta desiran angin di antara pagar tanaman warga."),
                    ("nar", "Udara perumahan yang damai itu membuat detak pikiranmu melambat. Setelah cukup lama beristirahat sambil memandangi langit, kepalamu terasa jauh lebih jernih."),
                ],
            ],
            "Tepi Sungai": [
                [
                    ("nar", "Kamu bersandar di pagar besi Tepi Sungai sambil memandangi riak air yang memantulkan cahaya langit. Di jalur lari bawah tanggul, beberapa warga melintas pelan mengajak anjing berjalan."),
                    ("nar", "Angin sungai yang sejuk menyapu wajahmu dan mengurai ketegangan di pundak. Waktu terasa berjalan lebih pelan di sini, memberimu ruang bernapas yang jarang kamu dapatkan di tengah kesibukan kampus."),
                ],
            ],
            "Pantai": [
                [
                    ("nar", "Kamu berjalan pelan menyusuri tepian berbatu di dekat Pantai lalu duduk menghadap laut terbuka. Suara ombak yang datang dan surut berulang kali membentuk irama yang langsung menenangkan kepala."),
                    ("nar", "Bau garam laut dan angin kencang yang menyapu rambutmu membuat seluruh keruwetan jadwal kampus terasa jauh sekali. Kamu duduk di sana cukup lama sampai tenagamu pulih kembali."),
                ],
            ],
            "Taman Besar": [
                [
                    ("nar", "Kamu menyusuri jalan setapak teduh di Taman Besar lalu berhenti di bangku dekat kolam kecil. Permukaan air beriak setiap kali daun gugur menyentuhnya."),
                    ("nar", "Tanpa harus menjaga sikap di depan siapa pun, kamu membiarkan pikiranmu kosong sejenak hingga ketegangan di lehermu mereda."),
                ],
            ],
            "Kuil": [
                [
                    ("nar", "Kamu menaiki tangga batu Kuil pelan-pelan dan berhenti di halaman teduh di bawah bayangan pohon cedar tua. Suasana di atas sini jauh lebih hening dibandingkan jalanan kota di bawah."),
                    ("nar", "Kamu berdiri sejenak mendengarkan gemerisik dedaunan dan bunyi lonceng angin yang samar. Ketenangan sederhana di tempat ini membuat napasmu kembali teratur dan pikiranmu jernih."),
                ],
            ],
        },
    }

    KK_ACT_DEFAULT = {
        "makan": [[("nar", "Kamu duduk menikmati hidangan hangat tanpa terburu-buru hingga rasa laparmu hilang dan tenagamu kembali pulih.")]],
        "kerja": [[("nar", "Beberapa jam kerja paruh waktu berlalu cukup sibuk. Tubuhmu terasa pegal saat selesai, dan upah sebesar ¥3.000 masuk ke saldomu.")]],
        "belajar": [[("nar", "Kamu memusatkan pikiran pada tumpukan catatan kuliah selama beberapa jam penuh hingga pemahamanmu bertambah jelas.")]],
        "santai": [[("nar", "Kamu mengambil waktu duduk tenang tanpa memikirkan tenggat apa pun, membiarkan napas dan kepalamu kembali segar.")]],
    }

    # Vignette transisi saat "Lanjutkan rutinitas mingguan" (7 hari berlalu dengan terasa hidup!)
    KK_WEEKLY_LIFE = {
        ("chiasa", "spring"): [
            [
                ("nar", "Satu minggu penuh berlalu di tengah sisa angin musim semi yang sejuk. Pagi hari di Rumah Amamiya diisi bunyi ketel air mendidih di dapur, langkah kaki Koita yang selalu hampir telat mencari kaus kaki di lorong bawah, serta obrolan ringan sambil sarapan roti panggang."),
                ("nar", "Di kampus, kelas-kelas awal di Fakultas Seni Rupa mulai menuntut tugas dasar satu demi satu. Kamu belajar menyimak instruksi dosen dengan hati-hati sambil menjaga jarak wajar di depan teman-teman sejurusan agar tidak memancing pertanyaan yang belum bisa kamu jawab."),
                ("nar", "Di sela jam kosong, kamu beberapa kali berpapasan singkat dengan wajah-wajah familier di koridor maupun depan gerbang, bertukar sapa singkat sebelum kembali ke rutinitas masing-masing. Tanpa terasa, satu pekan baru pun tiba."),
            ],
            [
                ("nar", "Hari demi hari sepanjang pekan ini berjalan dengan irama mahasiswa tahun pertama yang mulai terasa akrab. Kelopak bunga yang tersisa di sepanjang jalan menuju Stasiun Kouseikan-mae perlahan berganti menjadi daun hijau muda yang segar."),
                ("nar", "Sepulang kuliah, kamu menyempatkan diri mampir ke toko kelontong bersama bahan masak sederhana, lalu duduk di meja belajar lantai dua menata ulang catatan kuliahmu sambil mendengarkan suara televisi samar dari ruang tengah."),
                ("nar", "Sesekali layar ponselmu menyala oleh pesan singkat dari Bu Yoshie atau obrolan grup kelas. Begitu kamu membalik halaman kalender meja, tujuh hari sudah berlalu dengan tenang."),
            ],
        ],
        ("chiasa", "summer"): [
            [
                ("nar", "Pekan ini diwarnai udara lembap dan terik matahari musim panas yang mulai terasa menyengat di pelataran Universitas Kouseikan. Suara serangga musim panas terdengar nyaring dari deretan pohon di tepi Taman Kampus setiap kali kamu berjalan berpindah gedung."),
                ("nar", "Di rumah, kipas angin di ruang makan berputar pelan menemani gelas-gelas teh jelai dingin yang selalu disiapkan Koita di dalam kulkas. Tugas studio dan persiapan menjelang jeda semester membuat bahumu cukup sering terasa pegal di penghujung hari."),
                ("nar", "Di antara hujan sore yang turun tiba-tiba dan cahaya matahari yang cepat kembali menyilaukan, satu minggu lagi terlewati dalam kalender tiga tahunmu."),
            ],
            [
                ("nar", "Tujuh hari terakhir berjalan di bawah langit biru cerah musim panas. Hampir setiap siang, antrean di depan mesin penjual minuman dingin dekat gedung fakultas selalu lebih panjang daripada biasanya."),
                ("nar", "Kamu menjalani jadwal kuliah, membereskan tugas harian di ruang studio yang berpendingin udara, lalu pulang menyusuri trotoar yang masih memancarkan sisa panas aspal sambil menenteng tas kanvasmu."),
                ("nar", "Malam-malam di Rumah Amamiya berlalu tenang oleh percakapan singkat di meja makan dan bunyi halaman catatan yang dibalik sebelum tidur, hingga pekan berikutnya tiba."),
            ],
        ],
        ("chiasa", "autumn"): [
            [
                ("nar", "Angin musim gugur mulai bertiup lebih dingin sepanjang pekan ini, menggugurkan daun-daun kecokelatan di sepanjang jalan setapak Taman Kampus dan pelataran Gedung Sastra."),
                ("nar", "Kuliah semester baru kembali memadat. Kamu mulai mengenakan kardigan hangat setiap pagi saat berangkat menuju stasiun, mendengarkan deru kereta pagi sambil menyusun rencana langkahmu untuk minggu-minggu mendatang."),
                ("nar", "Sore hari kini datang jauh lebih cepat dengan langit jingga yang cepat meredup menjadi gelap. Sepulang dari kampus, aroma masakan hangat dari dapur Rumah Amamiya menjadi penanda berakhirnya satu minggu lagi."),
            ],
            [
                ("nar", "Satu minggu penuh berlalu di tengah cuaca musim gugur yang sejuk dan kering. Di sepanjang koridor kampus, bau kopi hangat dari gelas kertas mahasiswa mulai menggantikan minuman es musim panas."),
                ("nar", "Di sela jam kuliah dan kesibukan studio, kamu memperhatikan bagaimana orang-orang di sekeliling Koita menjalani rutinitas mereka masing-masing dengan ritme yang tampak biasa di permukaan. Tujuh hari terlipat rapi menuju pekan baru."),
            ],
        ],
        ("chiasa", "winter"): [
            [
                ("nar", "Udara dingin musim dingin menyelimuti seluruh pekan ini. Setiap pagi napasmu mengembun putih begitu melangkah keluar dari pintu pagar Rumah Amamiya sambil merapatkan syal rajut di lehermu."),
                ("nar", "Di kampus, mahasiswa berjalan lebih cepat dengan tangan tersembunyi di saku mantel, mencari kehangatan di Kantin Pusat atau ruang baca yang pemanasnya menyala terus-menerus."),
                ("nar", "Sepulang kuliah, lampu-lampu pertokoan dekat stasiun menyala lebih awal di tengah langit gelap. Kamu menghabiskan malam-malam yang dingin di dekat pemanas ruangan hingga satu minggu lagi berlalu."),
            ],
            [
                ("nar", "Tujuh hari di pertengahan musim dingin terasa berjalan cepat oleh tumpukan persiapan akhir semester dan udara beku yang mengetuk kaca jendela kamar."),
                ("nar", "Kamu menjalani kelas harian, menghangatkan jari dengan kaleng cokelat panas dari mesin otomatis, lalu pulang menuju lampu teras Rumah Amamiya yang menyala kuning hangat. Tanpa terasa, pekan baru kembali dimulai."),
            ],
        ],
        ("chiasa", "late_winter"): [
            [
                ("nar", "Angin dingin di penghujung tahun ajaran mulai sedikit melunak sepanjang pekan ini, membawa tanda samar bahwa musim semi baru tinggal menghitung minggu."),
                ("nar", "Suasana kampus terasa sedikit berubah oleh kesibukan evaluasi akhir semester dan mahasiswa tingkat akhir yang mulai mengurus berkas. Kamu menata ulang catatanmu dan mengevaluasi seluruh jejak yang sudah terjadi sepanjang tahun ini saat tujuh hari berlalu."),
            ],
        ],
        ("yutaka", "spring"): [
            [
                ("nar", "Satu minggu penuh berlalu di tengah angin awal musim semi yang sejuk. Pagi hari di apartemen lantai atasmu dimulai dalam keheningan yang rapi, hanya diisi suara mesin pemanas air dan cahaya matahari yang memantul di jendela kaca tinggi."),
                ("nar", "Di Gedung Ekonomi, kamu duduk di barisan tengah menyimak kuliah sambil menjaga sikap santai yang tidak terlalu mencolok agar teman-teman sefakultas termasuk Daichi tidak curiga pada ingatanmu yang kosong."),
                ("nar", "Di sela jadwal kuliah dan jam makan siang di kantin, kamu beberapa kali bertukar sapa dengan Koita, Nagisa, serta kenalan lainnya sebelum pulang kembali ke apartemen saat langit mulai gelap. Tujuh hari pun terlewati."),
            ],
            [
                ("nar", "Hari demi hari sepanjang pekan ini berjalan dengan ritme perkuliahan yang mulai bisa kamu baca. Jalanan dari Distrik Elite menuju Stasiun Kouseikan-mae dipenuhi kelopak bunga yang tersapu angin di tepi trotoar."),
                ("nar", "Sore hari kamu menyempatkan diri membaca ulang materi ekonomi di meja apartemen agar tidak tertinggal terlalu jauh, lalu memesan makan malam sederhana atau mampir sebentar ke kedai dekat stasiun. Tanpa terasa, pekan berikutnya tiba."),
            ],
        ],
        ("yutaka", "summer"): [
            [
                ("nar", "Pekan ini berjalan di bawah terik matahari musim panas yang menyilaukan kaca-kaca tinggi Gedung Ekonomi. Pendingin ruangan di ruang kuliah dan apartemen hampir tidak pernah berhenti berdengung."),
                ("nar", "Kamu menjalani rangkaian kelas, diskusi kelompok, dan jeda siang dengan kaleng kopi dingin di tangan sambil mengamati gerak-gerik orang-orang di sekitar Koita dari jarak wajar."),
                ("nar", "Menjelang akhir pekan, hujan deras musim panas sempat turun sesaat lalu meninggalkan bau aspal basah yang segar di udara malam. Satu minggu lagi berlalu dalam hitungan kontrakmu."),
            ],
            [
                ("nar", "Tujuh hari terakhir berlalu cepat oleh jadwal kuliah dan tugas kelompok yang mulai menumpuk menjelang pertengahan tahun. Suara serangga musim panas terdengar nyaring setiap kali kamu melintasi Taman Kampus."),
                ("nar", "Malam-malam di apartemenmu diisi suara siaran televisi pelan dan layar catatan kuliah di meja makan, sementara sesekali notifikasi pesan dari grup teman masa kecil menyala di ponselmu hingga pekan baru dimulai."),
            ],
        ],
        ("yutaka", "autumn"): [
            [
                ("nar", "Angin musim gugur mulai terasa dingin setiap pagi sepanjang pekan ini, membuatmu mulai mengenakan jaket navy kesayangan Yutaka setiap kali keluar dari lobi apartemen."),
                ("nar", "Di kampus, dedaunan di sepanjang jalur menuju Gedung Sastra mulai menguning dan berguguran. Kelas-kelas semester baru berjalan padat, diselingi obrolan singkat di kantin dan cangkir kopi panas di Kafe Komorebi."),
                ("nar", "Matahari terbenam lebih cepat di balik gedung-gedung kota yang terlihat dari jendela apartemenmu. Tanpa terasa, satu pekan penuh kembali terlewati."),
            ],
            [
                ("nar", "Satu minggu di tengah sejuknya musim gugur berjalan dengan irama yang teratur. Kamu mengurus tugas mata kuliah ekonomi, mengecek saldo rekening bulanan dari keluarga Kisaragi yang selalu masuk tanpa pesan pribadi, lalu menyusun ulang rencana langkahmu di kampus."),
                ("nar", "Waktu terus bergerak maju di balik keseharian yang tampak tenang, membawamu masuk ke pekan berikutnya."),
            ],
        ],
        ("yutaka", "winter"): [
            [
                ("nar", "Udara dingin musim dingin menusuk wajah setiap kali kamu keluar dari lobi apartemen menuju kampus sepanjang pekan ini. Lampu-lampu jalan raya di Distrik Elite menyala lebih awal di bawah langit sore yang cepat gelap."),
                ("nar", "Di dalam ruang kuliah dan perpustakaan, mahasiswa sibuk menyiapkan bahan ujian akhir sambil menghangatkan tangan pada botol minuman panas. Malam-malam di apartemenmu terasa semakin hening dengan pemanas ruangan yang menyala pelan."),
                ("nar", "Di sela rutinitas dingin yang teratur itu, tujuh hari berlalu membawa waktu mendekati titik balik berikutnya."),
            ],
            [
                ("nar", "Tujuh hari di pertengahan musim dingin berlalu oleh deretan kuliah, bacaan ekonomi yang menumpuk, serta perjalanan pulang menembus angin malam yang kencang."),
                ("nar", "Kamu sempat mampir membeli makan malam hangat di kedai dekat stasiun sebelum kembali ke ruang tamu yang senyap. Begitu layar kalender ponselmu berganti, satu minggu lagi sudah kamu lewati."),
            ],
        ],
        ("yutaka", "late_winter"): [
            [
                ("nar", "Angin tajam di penghujung tahun ajaran perlahan mulai berkurang sepanjang pekan ini. Di pelataran kampus, mahasiswa sibuk menyelesaikan evaluasi akhir semester sambil membicarakan rencana liburan dan tahun ajaran baru."),
                ("nar", "Kamu merapikan catatan di meja apartemen sambil menimbang seluruh perubahan yang sudah mulai bergeser di sekitar Koita sepanjang setahun ini. Tujuh hari berlalu dengan tenang menuju pekan baru."),
            ],
        ],
    }

    # Adegan bangun tidur di kk_rest.rpy
    KK_REST_WAKE = {
        ("chiasa", "day"): [
            [
                ("nar", "Cahaya terang dari balik tirai tipis kamar lantai dua Rumah Amamiya menyentuh kelopak matamu. Kamu mengerjap pelan, meregangkan bahu yang sempat kaku, lalu bangkit duduk di tepi ranjang."),
                ("nar", "Dari lantai bawah terdengar samar suara aktivitas rumah yang akrab. Setelah merapikan simpul pita hitam di rambutmu di depan cermin, tubuhmu terasa jauh lebih segar untuk kembali beraktivitas."),
            ],
            [
                ("nar", "Kamu membuka mata perlahan di kamarmu sambil mendengarkan kicau burung samar dari arah taman luar. Rasa kantuk yang tadi memberatkan kelopak matamu kini berangsur hilang."),
                ("nar", "Kamu menyibak selimut, merapikan baju di depan meja rias, dan kembali siap melangkah keluar kamar."),
            ],
        ],
        ("chiasa", "night"): [
            [
                ("nar", "Kamu membuka mata di dalam kamar Rumah Amamiya yang tenang dan remang oleh cahaya lampu jalan di luar tirai. Hening malam membuat detak jam dinding terdengar jelas."),
                ("nar", "Kamu duduk sebentar di tepi ranjang untuk mengumpulkan kesadaran penuh, lalu menyalakan lampu meja belajar dengan tubuh yang terasa lebih bugar."),
            ],
        ],
        ("yutaka", "day"): [
            [
                ("nar", "Sinar matahari yang menembus celah tirai panjang apartemen lantai atas membangunkanmu secara perlahan. Dengung halus mesin pendingin ruangan mengisi keheningan kamar yang luas itu."),
                ("nar", "Kamu bangkit duduk di tepi ranjang, mengusap wajah sekali, lalu mengenakan kembali jam tangan tipis di pergelangan kirimu. Tenagamu terasa cukup pulih untuk melanjutkan jadwal hari ini."),
            ],
            [
                ("nar", "Kamu membuka mata di kamar tidur apartemenmu yang tenang. Dari balik jendela kaca besar, langit kota tampak terang di atas deretan atap gedung Distrik Elite."),
                ("nar", "Setelah minum segelas air dingin di dapur untuk mengusir sisa kantuk, kamu kembali siap keluar apartemen."),
            ],
        ],
        ("yutaka", "night"): [
            [
                ("nar", "Kamu membuka mata di dalam kamar apartemen yang senyap. Lampu-lampu gedung di kejauhan berkelip tenang di balik jendela kaca setinggi dinding."),
                ("nar", "Kamu bangkit dari ranjang, menyalakan lampu ruang tamu yang temaram, dan menarik napas dalam dengan tubuh yang terasa jauh lebih ringan."),
            ],
        ],
    }

    KK_ONSEN_TRAVEL = {
        "to_onsen": [
            ("nar", "Kamu naik ke gerbong kereta lokal dari peron Stasiun Kouseikan-mae sambil membawa tas menginapmu. Begitu pintu menutup dan kereta mulai melaju, deretan gedung kota perlahan berganti menjadi perbukitan hijau dan sungai berbatu di balik jendela."),
            ("nar", "Selama hampir satu jam perjalanan, guncangan gerbong yang teratur dan udara pegunungan yang semakin sejuk membuat suasana benar-benar terasa lepas dari rutinitas kampus."),
            ("nar", "Akhirnya kereta berhenti di stasiun kecil bernuansa kayu, dan beberapa menit berjalan menanjak membawamu tiba di gerbang penginapan onsen yang menyambut dengan kepulan uap tipis dari arah taman belakang."),
        ],
        "from_onsen": [
            ("nar", "Kamu berpamitan meninggalkan halaman penginapan onsen sambil menenteng tas perjalananmu menuju stasiun kecil di kaki bukit. Aroma belerang tipis dan udara pegunungan yang dingin perlahan tertinggal di belakang."),
            ("nar", "Kereta lokal melaju mulus menuruni lereng kembali ke arah kota, mengembalikan deretan papan toko, kabel listrik, serta keramaian jalan raya ke balik jendela kaca."),
            ("nar", "Tidak lama kemudian pengumuman peron terdengar, dan kamu melangkah turun kembali ke Stasiun Kouseikan-mae dengan seluruh kesan dari perjalanan onsen yang masih melekat di kepalamu."),
        ],
    }

label kk_play_lines(lines):
    $ _kk_pl_i = 0
    while _kk_pl_i < len(lines):
        $ _kk_pl_spk, _kk_pl_txt = lines[_kk_pl_i]
        $ _kk_pl_i += 1
        $ _kk_pl_who = getattr(store, _kk_pl_spk, _kk_pl_spk)
        $ renpy.say(_kk_pl_who, _kk_pl_txt)
    return
