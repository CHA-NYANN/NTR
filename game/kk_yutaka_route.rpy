# Milestone host Yutaka (Y03, Y04, Y06, Y07, Y08, Y11, Y12, Y14, Y15, Y16, Y18):
# hidup pemain-sebagai-Yutaka menjaga penyamaran dan menavigasi arah (BL / heroine
# / Chiasa-NPC). Fire saat MASUK lokasi sebagai host Yutaka (trigger "host").
# Pilihan rute = pointer-flag non-eksplisit; manuver = konsekuensi. Mengikuti
# Event_Yutaka; melengkapi Y01/Y02/Y05/Y09/Y10/Y13/Y17. Daichi pakai nama-penutur.

# ┌─ PANDUAN CERITA · Y03 · Yuu-kun?
# │ LOKASI  : Distrik Elite · Apartemen Yutaka
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Nagisa memanggil dengan julukan masa kecil.
# │ INTI    : A jawab natural / B salah panggil / C pura-pura lupa.
# │ AKHIRAN : curiga_nagisa naik/turun.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y03:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Julukan lama")
    nar "Malam hari di apartemen mewah milik keluarga Kisaragi itu biasanya terlalu luas dan sunyi, tetapi kehadiran Sakurajima Nagisa yang mampir selepas kuliah dan makan malam langsung membuat ruang tamu terasa jauh lebih hidup."
    nar "Sepatu ketsnya sudah terlepas rapi di pintu masuk, sementara tabung kertas gambar berukuran besar ia sandarkan begitu saja di dekat dinding lorong. Lampu-lampu kota di balik jendela kaca lebar berkilau tenang sementara suara langkah ringan Nagisa mondar-mandir di atas karpet ruang tamu terdengar sampai ke dapur."
    nar "Kamu sedang menuang dua gelas teh jelai dingin dari kulkas dan menata beberapa keping biskuit asin di piring kecil ketika suaranya terdengar berseru dari depan."
    nagisa "Serius deh, Yutaka, setiap kali aku mampir ke sini, apartemenmu selalu kelihatan kayak ruang pamer mebel! Masa nggak ada satu pun majalah atau bantal yang miring sedikit?"
    yutaka "Bukan ruang pamer, memang cuma nggak banyak barang saja. Lagipula aku tinggal sendirian."
    nagisa "Tetap saja terlalu rapi! Kalau di ruang tengah rumahku, papan gambar, penggaris skala, sama potongan kayu balsa pasti sudah berceceran sampai dekat televisi. Tadi saja pundakku hampir copot bawa tabung gambar ini dari stasiun."
    yutaka "Kamu sendiri yang selalu menolak nitip di loker studio."
    nagisa "Habis loker studio suka lembap! Nanti kertasku melengkung semua!"
    nar "Kamu keluar dari dapur membawa nampan kecil berisi dua gelas teh dingin dan piring camilan. Alih-alih melihat gadis bertubuh mungil berambut pirang keemasan yang diikat dua itu sudah duduk di sofa sambil mengeluhkan dosennya seperti tadi, langkahmu terhenti ketika melihatnya berdiri diam di dekat rak televisi."
    nar "Perhatiannya tertahan sepenuhnya pada sebuah bingkai foto kayu kecil yang terpajang rapi di sudut rak. Di dalam foto yang warnanya mulai agak hangat dimakan waktu itu, empat anak kecil berdiri berdempetan di bawah deretan lampion festival musim panas."
    nar "Selama beberapa detik penuh, raut galak dan kompetitif yang biasa ia pasang di kampus menghilang begitu saja. Ia memandangi foto masa kecil itu dengan senyum tipis yang lembut, jari telunjuknya menyentuh ringan tepi bingkai kayu. Lalu, seolah terseret kenangan lama tanpa sadar, ia menoleh ke arahmu begitu mendengar bunyi gelas diletakkan di atas meja kaca."
    nagisa "Yuu-kun! ...Eh."
    nar "Begitu julukan masa kecil itu keceplosan meluncur dari bibirnya, Nagisa sendiri langsung tersentak. Matanya yang biru cerah melebar, lalu rona merah tipis naik cepat ke pipi dan ujung telinganya. Ia buru-buru berdeham kecil sambil mengalihkan pandangan kembali ke bingkai foto, lalu tertawa canggung."
    nagisa "...Aneh sekali ya sekarang keceplosan memanggil begitu lagi. Padahal sudah bertahun-tahun nggak kupakai."
    yutaka "Tiba-tiba sekali."
    nagisa "Habis lihat foto ini, sih! Waktu SD dulu, setiap kali aku teriak 'Yuu-kun!' dari ujung gang, kamu selalu yang paling pertama menoleh sebelum Ko-kun sempat sadar aku lagi manggil. Kamu masih ingat kan malam foto ini diambil? Waktu kita hampir ketinggalan kembang api pembuka gara-gara nungguin Chiasa beli permen apel?"
    nar "Mata biru cerah Nagisa menoleh lurus menatapmu, menunggu sahutan yang akrab. Di dalam kepala, kamu tahu persis bahwa tidak ada satu pun ingatan masa kecil Yutaka yang ikut diwariskan kepadamu. Yang kamu miliki hanyalah foto di rak itu dan serpihan gambaran umum tentang sifat mereka."
    call kk_family_menu("Y03", ["\"Mana mungkin lupa, kamu kan selalu paling heboh.\"", "\"Ingat dong, waktu kamu tersesat di dekat stan ikan mas itu, kan?\"", "\"Wah, jujur saja bagian itu sudah agak kabur di kepalaku.\""])
    if _return == "A":
        nar "Kamu tidak membiarkan raut wajahmu membeku sedetik pun. Kamu bersandar santai di pinggir sofa sambil menyilangkan tangan di dada, lalu menarik sudut bibirmu menjadi senyum tipis yang terasa paling cocok dengan pembawaan santai pemilik tubuh ini."
        yutaka "Mana mungkin lupa. Kalau aku nggak langsung menoleh waktu kamu teriak dulu, nanti kamu bakal makin keras teriaknya sampai satu gang keluar semua. Lagipula kalau nggak salah, malam itu kamu sendiri yang paling heboh berebut tempat duduk di dekat tangga kuil, kan?"
        nar "Kamu sengaja memilih detail yang paling sesuai dengan sifat tidak sabaran Nagisa, cukup masuk akal tanpa harus menebak rincian spesifik yang berisiko meleset."
        nar "Nagisa mengerjap sesaat, lalu tawa ringan yang tulus langsung pecah dari bibirnya. Rona canggung di wajahnya segera meluruh berganti raut rileks yang akrab."
        nagisa "Hei, itu kan supaya kita semua dapat pemandangan kembang api paling jelas! Kalau aku nggak lari duluan nyari tempat, nanti kita cuma kebagian berdiri di belakang orang-orang tinggi!"
        yutaka "Dan tetap saja ujung-ujungnya kamu berdiri juga gara-gara nggak bisa duduk diam."
        nagisa "Mana ada! ...Tapi ternyata kamu masih ingat rupanya."
        nar "Ia menunduk kembali memandangi bingkai foto di rak dengan tatapan hangat, lalu meluruskan sedikit letaknya sebelum berjalan menghampiri sofa."
        nagisa "Jujur saja, aku sendiri juga nggak ingat semuanya dengan rinci, Yutaka. Yang paling kuingat cuma rasanya dulu, tiap kali musim panas datang, kita selalu merasa besok masih bisa main bareng lagi tanpa perlu mikir macam-macam."
        nar "Ia duduk di ujung sofa, mengambil salah satu gelas teh dingin dan sebiji biskuit dari meja kaca, lalu menyandarkan punggungnya sambil menatap langit-langit yang tenang."
        yutaka "Sekarang juga kan kita masih sering kumpul kayak begini. Kampusnya saja masih sama semua."
        nagisa "Iya sih, Chiasa juga akhirnya masuk Kouseikan bareng kita. Jujur aja, waktu mau ujian masuk dulu aku sempat panik takut cuma aku yang kepisah ke kampus lain. Untung saja kita semua masih ketemu di stasiun yang sama."
        yutaka "Kalau sampai kepisah, pasti kamu yang paling kencang protes di grup setiap malam."
        nagisa "Jelas dong! Terus siapa juga yang bakal ngingetin Ko-kun kalau dia kelamaan bengong atau nggak bisa nolak permintaan orang? Cuma kadang rasanya aneh aja... waktu kecil kelihatannya dunia itu cuma sepanjang gang rumah sampai kuil, sekarang tiba-tiba semua orang punya jadwal sendiri, tugas sendiri, kenalan sendiri."
        yutaka "Termasuk jadwal studio maket yang bikin kamu mengeluh tiap malam?"
        nagisa "Hei, itu dosennya memang nggak masuk akal kasih tenggatnya! Nanti kalau panitia kampusmu makin sibuk juga jangan sampai lupa mampir nongkrong bareng, ya."
        nar "Ia tertawa pelan sambil menyesap teh jelai dinginnya, lalu menurunkan gelas ke atas tatakan dan menoleh padamu dengan sorot mata biru yang tenang dan hangat."
        nagisa "...Baguslah kalau sekarang pun kamu masih mau menoleh waktu kupanggil, Yutaka. Rasanya lega lihat nggak semuanya berubah."
        yutaka "Selama kamu nggak teriak-teriak di tengah lorong kampus, aku pasti menoleh."
        nagisa "Heh, jangan salah, kalau kamu pura-pura nggak dengar bakal kupanggil pakai julukan lama itu keras-keras di depan gedung fakultasmu lho!"
        nar "Kalian menghabiskan teh dingin dan sisa biskuit sambil berbincang santai setengah jam lagi sebelum Nagisa mengangkat tabung gambarnya dan beranjak ke pintu depan. Di matanya, tidak ada sedikit pun keraguan yang tersisa. Kamu mengantarnya sampai ke lorong pintu dengan perasaan lega, menyadari betapa mudahnya satu jawaban yang tepat menenangkan sahabat masa kecilnya sekaligus menjaga jarak aman dari masa lalu yang tidak pernah kamu alami."
    elif _return == "B":
        nar "Merasa harus membuktikan bahwa kamu benar-benar mengingat masa kecil mereka agar tidak dicurigai, kamu nekat merangkai satu detail berdasarkan foto festival di rak televisi."
        yutaka "Tentu saja ingat. Malam itu kan gara-gara kamu sempat tersesat di dekat stan ikan mas sampai Koita harus meminjamkan sandalnya, terus kita semua baru ketemu lagi di depan gerbang taman kota, kan?"
        nar "Nagisa sempat mengeluarkan tawa pendek karena mengira kamu sedang sengaja mengarang lelucon konyol untuk menggodanya."
        nagisa "Haha, apaan sih, ngawur sekali... tunggu dulu, kamu nggak lagi bercanda ya?"
        nar "Tawa Nagisa langsung terhenti di tenggorokan begitu ia melihat raut wajahmu yang tetap serius menunggu ia mengiyakan. Alisnya perlahan berkerut dalam."
        nagisa "Yutaka... yang malam itu tersesat di festival memang aku, tapi yang menemukan dan menenangkanku waktu itu kan Chiasa di dekat kuil sebelah timur, sama sekali nggak di gerbang taman kota. Mana pernah juga Ko-kun meminjamkan sandalnya."
        nar "Suara Nagisa melambat dan turun, nada santainya lenyap sepenuhnya. Ia meletakkan tangannya menjauh dari bingkai foto di rak televisi dengan gerakan kaku, lalu menoleh menatapmu lebih lama seolah berusaha memahami bagaimana sahabat sejak kecilnya bisa meleset sejauh itu."
        yutaka "Ah... maaf. Kayaknya kepalaku mencampuradukkan dua festival musim panas yang berbeda. Kan dulu kita sering datang hampir tiap tahun."
        nagisa "...Mungkin. Tapi biasanya kamu paling hafal hal-hal begini, bahkan detail kecil yang aku sendiri sudah lupa. Waktu SMA dulu kamu masih sempat ngeledek aku soal malam itu."
        nar "Ia berjalan pelan ke sofa, duduk di ujungnya sambil menarik bantal ke pangkuan dan memeluknya erat. Suaranya turun lebih pelan, masih mengandung keraguan yang belum hilang."
        nagisa "Malam itu kan aku lari mengejar anak kucing belang di belakang stan takoyaki, terus malah nyasar sampai ke dekat kuil timur. Chiasa yang nemuin aku sambil bawain es serut, terus kamu sama Ko-kun baru nyusul sepuluh menit kemudian sambil ngos-ngosan dan saling menyalahkan."
        yutaka "Oh... iya, baru ingat sekarang bagian kucing sama es serutnya."
        nagisa "Kamu beneran nggak ingat waktu itu aku hampir nangis gara-gara takut kucingnya ketabrak sepeda, terus kamu sendiri yang ngebeliin minuman dingin dari mesin di pinggir jalan sambil bilang aku cengeng?"
        nar "Jeda satu detik sebelum kamu sempat menjawab terasa terlalu panjang di dalam ruang tamu yang sunyi itu."
        yutaka "...Iya, agak kabur, Nagisa. Belakangan kepalaku memang lagi penuh sama bacaan kuliah, jadi ingatan lama kayaknya agak campur aduk."
        nagisa "Padahal waktu pulang kamu juga yang menggendong tasku karena talinya putus. Masa bisa ketukar sama cerita sandal segala sih?"
        nar "Nagisa tidak lagi membantah penjelasanmu. Ia mengambil gelas teh dingin di meja kaca, menyesapnya beberapa teguk tanpa menyentuh biskuit di piring, lalu melirikmu dengan kening masih berkerut samar."
        nagisa "Aneh banget deh kamu malam ini, Yutaka. Kayak lagi capek banget... atau lagi mikirin hal lain sampai nggak benar-benar di sini."
        yutaka "Cuma agak kurang tidur saja minggu ini."
        nagisa "...Ya sudah, kalau capek jangan begadang terus. Aku pulang duluan deh mumpung keretanya belum terlalu malam, biar kamu bisa istirahat."
        nar "Ia berdiri lebih cepat dari biasanya, mengenakan sepatunya di pintu masuk, lalu mengambil tabung kertas gambarnya. Tepat sebelum menutup daun pintu apartemen dari luar, Nagisa sempat berhenti sejenak menatap wajahmu dengan sorot ragu yang belum hilang. Kamu hanya bisa mengangguk pelan sambil menelan satu kenyataan pahit bahwa kenangan masa kecil mereka yang bertahun-tahun tidak akan pernah bisa ditebak secara sembarangan."
    else:
        nar "Daripada nekat mengarang detail masa lalu dan berakhir salah sebut, kamu memilih duduk santai di sofa, bersandar sambil mengangkat bahu ringan, lalu tersenyum tipis."
        yutaka "Wah, jujur saja, bagian yang itu sudah agak kabur di kepalaku. Sudah bertahun-tahun lalu juga kan, Nagisa. Akhir-akhir ini kepalaku keburu penuh sama materi kuliah sama catatan panitia."
        nar "Nagisa langsung memutar badannya menghadapmu dengan mata biru membulat dan bibir mengerucut tidak percaya."
        nagisa "Hah?! Lupa?! Serius kamu bisa lupa?!"
        nar "Ia melangkah cepat dari rak televisi menuju sofa, berhenti tepat di depan meja kaca dengan kedua tangan bertolak pinggang."
        nagisa "Padahal biasanya kamu yang paling berisik mengungkit kejadian waktu SD cuma buat ngeledek aku kalau kita lagi kumpul! Masa yang kali ini malah bilang sudah kabur?!"
        yutaka "Bukan lupa semuanya, cuma urutan malam itu saja yang agak buram. Kalau kamu ingat sejelas itu, memangnya waktu itu persisnya gimana?"
        nar "Nagisa menatapmu beberapa detik penuh dengan sorot curiga tipis yang bercampur kesal, seolah menimbang apakah kamu sedang berpura-pura malas meladeninya atau sungguh-sungguh tidak ingat. Akhirnya ia menghela napas panjang dan menjatuhkan diri duduk bersila di sofa sambil memeluk salah satu bantal."
        nagisa "...Ya sudah, kalau memang lupa nanti kuceritakan lagi pelan-pelan."
        nar "Suara Nagisa berubah sedikit lebih serius. Ia menoleh menatapmu lurus dari balik bantal yang dipeluknya."
        nagisa "Tapi dengar ya, Yutaka. Jangan pernah cuma mengangguk-angguk pura-pura paham kalau sebenarnya kamu nggak ingat. Aku masih bisa maklum kalau kamu jujur lupa, tapi aku bisa benar-benar marah kalau sahabat sendiri cuma mengiyakan ucapanku tanpa benar-benar dengar."
        yutaka "Iya, maaf. Aku nggak bakal pura-pura ingat. Ceritakan saja lagi nanti kalau ada bagian lama yang kelupaan."
        nar "Nagisa mendengus kecil, lalu meraih gelas teh dinginnya dan mencomot sekeping biskuit dari piring. Raut kesalnya sedikit melunak saat ia mulai menceritakan ulang potongan malam itu."
        nagisa "Malam itu gara-gara aku melihat anak kucing belang lari ke belakang stan takoyaki, jadi aku langsung ngejar tanpa bilang siapa-siapa. Tahu-tahu malah nyasar sampai dekat kuil timur. Yang nemuin duluan itu Chiasa sambil bawain es serut sirup biru, padahal tangannya sendiri sudah penuh pegang permen apel."
        yutaka "Lalu aku sama Koita?"
        nagisa "Kalian berdua baru nyusul sepuluh menit kemudian sambil ngos-ngosan, terus malah berantem sendiri siapa yang lupa jagain aku! Padahal aku sudah duduk tenang makan es serut bareng Chiasa."
        yutaka "Ingatanmu tajam sekali ya buat hal-hal begitu."
        nagisa "Ya iyalah, soalnya habis itu kalian masih sempat ngeledek aku sebulan penuh! Awas aja kalau besok-besok kamu lupa janjimu sendiri juga. Sudah ah, bahas kuliah saja, tugas maketku minggu ini bikin aku pengin melempar penggaris."
        nar "Obrolan pun perlahan kembali mengalir ke keluh kesah jadwal studionya dan candaan soal Koita selama setengah jam berikutnya. Meski suasananya kembali cair, sesekali di sela tegukan tehnya kamu menangkap mata biru Nagisa masih melirik ke arahmu dari balik gelas dengan kerutan samar di kening. Ada sesuatu pada sikapmu malam ini yang membuatnya merasa tidak sepenuhnya sama."
    return

# ┌─ PANDUAN CERITA · Y04 · Kuliah Ekonomi: Ingatan yang Hilang
# │ LOKASI  : Distrik Elite · Apartemen Yutaka
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : kuis dadakan.
# │ INTI    : A belajar semalaman / B menyontek / C jujur ke dosen / D minta bantuan Daichi.
# │ AKHIRAN : IPK; B berisiko skorsing akademik ().
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y04:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Kuis dadakan")
    nar "Malam turun sunyi di apartemen Kisaragi yang luas. Lampu langit-langit ruang tamu sengaja kamu matikan, menyisakan hanya lingkaran cahaya hangat dari lampu meja belajar yang menyoroti tumpukan buku teks tebal dan map binder rapi di atas meja kayu gelap."
    nar "Siang tadi, tepat lima menit sebelum kelas berakhir, dosen mata kuliah pengantar ekonomi menengah mengumumkan kuis dadakan untuk besok pagi, menutup rangkaian kuliah beberapa minggu terakhir yang sebagian besar hanya lewat di telingamu seperti bahasa asing."
    nar "Kamu membalik halaman demi halaman catatan lama milik Kisaragi Yutaka. Tulisannya bersih, terstruktur, dan penuh singkatan istilah, turunan rumus, serta kurva keseimbangan yang tampaknya sudah lebih dari cukup untuk pemilik tubuh ini. Bagimu, setiap halaman yang kamu buka justru melahirkan tiga pertanyaan baru yang bahkan tidak tahu harus dicari dari bab mana."
    nar "Kamu menyandarkan punggung ke kursi, mengusap wajah pelan sambil menatap kartu mahasiswa di sudut meja. Memiliki kartu mahasiswa, apartemen mewah, dan nama belakang yang dikenal baik oleh dosen sama sekali tidak berarti kamu mewarisi dua tahun ilmu yang pernah ia pelajari."
    nar "Ponsel di atas meja bergetar dua kali, menampilkan notifikasi grup kelas yang ramai mengeluhkan kuis besok. Beberapa teman sekelas bahkan menandai namamu dengan candaan bahwa Kisaragi Yutaka pasti sudah selesai membaca sambil bersantai seperti biasa."
    "Pesan Grup Kelas" "Yutaka pasti lagi minum kopi santai nih, besok bagi-bagi bocoran bab empat dong sebelum kelas mulai!"
    "Pesan Grup Kelas" "Bener banget, semester lalu aja nilainya paling tinggi tanpa kelihatan belajar."
    nar "Kamu menatap layar ponsel selama beberapa detik sebelum mematikannya tanpa membalas. Jam dinding sudah melewati pukul sembilan malam. Besok pagi lembar kuis akan tetap diletakkan di depan mejamu, tidak peduli siapa sebenarnya yang sedang duduk di balik tubuh ini."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Belajar semalaman mengejar ketertinggalan.", "Menyontek saat kuis.", "Jujur ke dosen soal kesulitanmu.", "Minta bantuan Daichi."])]
    call screen kk_choice_panel(_rows, "Pilihan")
    $ kk_record_choice("Y04", _return)
    if _return == "A":
        nar "Kamu menyetel ponsel ke mode hening lalu menaruhnya terbalik di sudut meja, beranjak ke dapur untuk menyeduh segelas kopi hitam pekat, lalu kembali duduk dan membuka buku pengantar dari bab paling dasar."
        nar "Malam itu merambat lambat ditemani goresan pensil, halaman buku yang dibalik bolak-balik, dan rumus-rumus yang harus kamu bongkar ulang satu per satu tanpa jalan pintas. Pukul satu dini hari, konsep kurva permintaan akhirnya mulai masuk akal. Pukul tiga, dua bab perhitungan optimasi tetap keras kepala membingungkan tidak peduli berapa kali kamu ulangi contoh soalnya."
        nar "Kamu menyeduh gelas kopi kedua sambil menahan kantuk, merangkum ulang pola grafik yang paling sering muncul di kuis tahun lalu ke dua lembar kertas coretan sampai langit di balik tirai jendela apartemen mulai berubah biru pucat."
        nar "Ketika fajar tiba, matamu terasa perih dan bahumu kaku. Kamu mandi air dingin cepat-cepat, menyambar tas kuliah, lalu melangkah menuju gedung fakultas."
        nar "Di koridor depan ruang kelas yang mulai dipadati mahasiswa mengantuk, Nakamura Daichi yang baru tiba berhenti melangkah dan menatap lingkaran gelap di bawah matamu dengan alis terangkat tinggi."
        "Daichi" "Hei, Yutaka... mukamu kenapa kusut amat pagi ini? Jangan bilang kamu beneran begadang semalaman cuma buat belajar kuis dadakan begini?"
        yutaka "Sekali-sekali boleh kan aku belajar serius sebelum kuis."
        "Daichi" "Wah, langit mau runtuh kayaknya seorang Kisaragi Yutaka bela-belain begadang baca buku paket sampai mata merah begitu. Biasanya kamu cuma baca ringkasan sepuluh menit di kereta terus tetap dapat nilai bagus."
        yutaka "Materi tiga minggu terakhir ini lumayan banyak hitungannya, kalau nggak dibaca dari awal bakal meleset semua."
        "Daichi" "Bagian elastisitas pasar sama substitusi variabel di bab empat sudah kamu baca? Dengar-dengar dari anak kelas sebelah, dosen kita suka keluarin grafik jebakan di situ."
        yutaka "Sudah kubaca ulang tadi subuh, lumayan nyambung lah rumus dasarnya. Tinggal hati-hati di tanda minusnya saja."
        "Daichi" "Wah, seriusan belajar penuh rupanya. Mantap lah. Kalau ada soal esai pendek di nomor terakhir, ingat pesan asisten minggu lalu ya, tulis asumsi awalmu dulu biar tetap dapat nilai langkah."
        yutaka "Oke, makasih infonya, Daichi."
        "Daichi" "Sip, ayo masuk, dosennya sudah jalan dari ujung lorong tuh."
        yutaka "Duluan saja, aku buang kaleng kopi di tempat sampah depan pintu dulu."
        nar "Saat kamu duduk di bangku kuliah dan lembar kuis mulai dibagikan dari baris depan, pengetahuan yang kamu bawa pagi ini memang belum sempurna, tetapi setiap rumus yang berhasil kamu tulis di atas kertas sepenuhnya hasil kerjamu sendiri semalaman."
    elif _return == "B":
        nar "Menatap tumpukan bab yang jelas mustahil kamu kuasai utuh dalam satu malam, kamu memilih jalan pintas yang paling berisiko. Dengan pulpen berujung tipis, kamu menyalin ringkasan rumus-rumus kunci serta tiga contoh persamaan keseimbangan di secarik kertas kecil yang dilipat rapi lalu kamu selipkan ke saku kemeja sebelum berangkat."
        nar "Pagi berikutnya, ruang kuliah yang biasanya ramai oleh gumaman mahasiswa berubah senyap begitu lembar kuis dibagikan. Hanya terdengar gesekan pensil, bunyi penghapus, dan detak jam dinding di atas papan tulis."
        nar "Di bangku sebelahmu, Daichi tampak tekun menunduk mengerjakan lembarnya sendiri. Kamu melewati soal nomor satu yang masih bisa ditebak dengan logika umum, lalu terhenti pada persamaan ganda di nomor dua. Sambil menunggu pengawas melangkah ke deretan kanan, kamu membuka lipatan kertas kecil itu tepat di balik bayangan lengan kirimu."
        nar "Jantungmu berdetak keras setiap kali matamu melirik cepat deretan rumus tersebut. Kelegaan singkat ketika baris demi baris soal akhirnya terisi mendadak berubah menjadi dingin yang menusuk tengkuk saat suara langkah sepatu pengawas berhenti tepat di samping mejamu."
        nar "Kamu menahan napas, menjaga punggung tetap tegak sambil menggeser pergelangan tangan kirimu menutupi lipatan kertas kecil itu tanpa berani melirik ke atas."
        "Pengawas" "...Kisaragi-kun, tolong posisi lengan kirimu agak diangkat sedikit dari pinggiran meja, ya. Jangan menutupi bagian bawah lembar soal."
        yutaka "...Baik, Pak. Maaf, tangan saya agak pegal tadi."
        nar "Dengan gerakan setenang mungkin, kamu menarik sedikit lengan kirimu sambil menyembunyikan kertas kecil itu di dalam genggaman telapak tangan sebelum menurunkannya ke paha di bawah meja."
        "Pengawas" "Pastikan di atas meja hanya ada pensil, penghapus, dan kalkulator standar. Kalau ada catatan di saku atau bawah meja, sebaiknya jangan sampai terlihat saat pemeriksaan. Waktu pengerjaan tinggal sepuluh menit lagi."
        yutaka "Iya, Pak. Sudah tidak ada apa-apa di atas meja."
        nar "Suara pengawas itu datar dan menyiratkan peringatan tegas sebelum ia akhirnya melanjutkan langkah perlahan ke barisan belakang. Dingin yang tersisa di ujung jarimu membuat tulisanmu di dua soal terakhir nyaris kaku sampai bel waktu selesai berbunyi."
        nar "Begitu kertas jawaban dikumpulkan dan mahasiswa mulai berhamburan ke koridor, Daichi langsung merapat ke sebelahmu dengan wajah heran."
        "Daichi" "Eh, Yutaka, tadi pengawasnya berhenti lama banget di samping mejamu. Ada soal yang salah cetak ya?"
        yutaka "Nggak ada, cuma diingatkan posisi tangan saja tadi."
        "Daichi" "Oh, ketat banget ya kuis kali ini. Tadi anak barisan belakang juga hampir kena tegur cuma gara-gara kotak pensilnya nggak ditutup. Semoga nilai kita aman deh."
        yutaka "Iya, semoga saja."
        nar "Ketika kamu meremas lipatan kertas kecil itu di dalam saku kemejamu di lorong belakang, kamu menyadari betapa tipis batas yang baru saja kamu lewati. Sekali saja kamu tertangkap tangan berbuat curang di kampus ini, nama besar keluarga Kisaragi tidak akan menyelamatkanmu dari skorsing akademik."
    elif _return == "C":
        nar "Alih-alih nekat menebak secara membabi buta atau mengambil risiko curang, kamu menutup buku teks tebal itu setelah mencatat bagian mana saja yang benar-benar tidak kamu pahami. Keesokan paginya, kamu datang setengah jam lebih awal dan mengetuk pintu ruang kerja dosen mata kuliah tersebut sebelum kelas dimulai."
        "Dosen" "Masuk. Oh, Kisaragi-kun? Tumben pagi-pagi sudah datang ke ruangan saya sebelum jam kuliah. Ada yang ingin ditanyakan soal materi kuis hari ini?"
        yutaka "Permisi, Pak. Saya ingin bicara jujur sebelum kuis pagi ini dimulai. Sebenarnya ada beberapa bagian dasar dari materi tiga minggu terakhir yang benar-benar tertinggal dan belum saya pahami dengan benar."
        nar "Dosen itu mengerutkan kening keheranan, melirik berkas daftar nilai semester lalu atas nama Kisaragi Yutaka yang tergeletak di mejanya, lalu melepas kacamatanya perlahan."
        "Dosen" "Tertinggal? Semester lalu pemahamanmu di bagian pengantar makro cukup kuat, Kisaragi-kun. Bahkan jawaban esaimu waktu ujian akhir termasuk tiga terbaik di kelas. Baiklah, kalau begitu coba jelaskan singkat saja kepada saya, bagian mana tepatnya yang masih kamu mengerti sekarang, dan di titik mana kamu mulai kehilangan alurnya?"
        yutaka "Untuk konsep dasar penawaran, permintaan, dan pergeseran kurva awal saya masih bisa mengikuti, Pak. Tapi begitu masuk ke penurunan persamaan keseimbangan ganda dan substitusi variabel di bab empat dan lima, saya benar-benar kehilangan pijakan cara menghitungnya."
        "Dosen" "Hmm... jadi kamu macet di bagian penerapan kalkulus untuk optimasi pasarnya ya. Tidak biasanya kamu membiarkan materi menumpuk sampai tiga minggu tanpa bertanya di kelas atau menghampiri asisten dosen."
        yutaka "Maaf, Pak. Belakangan ini fokus saya sempat terpecah dan saya baru sadar ketertinggalan saya terlalu jauh waktu membuka buku catatan tadi malam. Saya rasa lebih baik melapor langsung daripada pura-pura paham sampai ujian tengah semester nanti."
        nar "Dosen itu mendengarkan penjelasanmu tanpa menyela, memandang wajahmu sejenak dengan tatapan menilai yang tenang, lalu mengangguk singkat dan menarik dua lembar modul latihan tambahan dari laci mejanya."
        "Dosen" "Saya tentu tidak bisa memberimu nilai keringanan atau membebaskanmu dari kuis pagi ini. Kamu tetap harus masuk kelas dan mengerjakan soal kuis sebisa kemampuanmu sekarang."
        yutaka "Iya, Pak, saya mengerti. Saya memang tidak berniat minta bebas kuis."
        "Dosen" "Bagus. Saya menghargai kejujuranmu datang melapor sebelum ujian tengah semester daripada membiarkannya berlarut-larut. Banyak mahasiswa yang memilih diam sampai nilainya hancur di akhir semester. Ambil daftar bacaan dasar dan lembar latihan susulan ini, kerjakan semuanya, lalu bawa ke ruangan saya minggu depan untuk saya periksa."
        yutaka "Baik, Pak. Saya akan kerjakan semua soalnya sebelum pertemuan minggu depan. Terima kasih banyak atas waktunya dan kesempatannya."
        "Dosen" "Sama-sama. Kalau ada satu nomor yang benar-benar buntu, tandai saja lalu tanyakan ke asisten setelah jam kuliah. Sekarang kembali ke ruang kelas dulu sebelum bel masuk berbunyi."
        nar "Kamu melangkah keluar dari ruang dosen dengan napas yang jauh lebih lega. Meskipun harus mengakui ketidaktahuanmu di depan dosen, kini kamu memegang panduan materi dasar yang jelas untuk mengejar ketertinggalanmu secara sah."
    else:
        nar "Menyadari bahwa membaca catatan singkatan Yutaka sendirian hanya akan membuatmu berputar di tempat sampai pagi, kamu mengambil ponsel dan mengirim pesan singkat kepada Nakamura Daichi, teman sekelasmu yang paling paham cara dosen ini membuat soal."
        nar "Balasannya masuk tidak sampai dua menit kemudian dengan rentetan tanda seru kaget, diikuti janjinya untuk langsung naik ke apartemenmu mumpung ia belum tidur."
        nar "Setengah jam kemudian, bel interkom berbunyi. Daichi melangkah masuk dengan santai sambil menenteng dua bungkus roti minimarket, sekaleng teh dingin, dan buku catatannya yang penuh tanda panah warna-warni, lalu menatap wajahmu yang kusut sebelum mendengus geli."
        "Daichi" "Wah, tumben sekali seorang Kisaragi Yutaka minta tolong diajarin kuliah malam-malam. Biasanya kamu cuma menyandar di barisan belakang sambil setengah mengantuk, tapi giliran ujian nilaimu tetap lolos aman."
        yutaka "Jangan mulai meledek dulu, Daichi. Kali ini aku beneran buntu total dari bab awalnya. Catatanku sendiri terlalu banyak singkatan sampai malah bikin pusing dibaca."
        "Daichi" "Haha, oke, oke, boleh. Sini geser kursimu ke tengah. Kita mulai dari bagian konsep yang bikin kamu tersesat dulu, jangan langsung loncat ke latihan soal terakhir. Roti malamnya gampang dimakan sambil jalan, mukamu sudah tegang kayak orang mau sidang kelulusan saja."
        yutaka "Biar kubuatkan kopi dulu sebentar, kamu mau kopi atau teh dingin?"
        "Daichi" "Teh dingin saja, kopinya buat kamu biar nggak ketiduran pas aku jelasin kurva."
        nar "Setelah meletakkan gelas di tepi meja, Daichi menarik kursi ke samping meja belajarmu. Ia membuka buku catatannya yang tulisannya jauh lebih mudah diikuti dibandingkan singkatan kaku milik Yutaka, lalu mulai menggambar ulang kurva dasar di kertas buram sambil menjelaskannya langkah demi langkah."
        "Daichi" "Lihat bagian sini dulu. Jangan lihat rumusnya dulu, baca logika pergeseran garisnya. Kalau harga input naik sementara pendapatan tetap, kurvanya otomatis geser ke kiri atas alih-alih muter ke bawah."
        yutaka "Tunggu sebentar... berarti angka koefisien di bagian sumbu vertikal ini nggak perlu diturunkan ulang kalau variabel pendapatannya dianggap tetap?"
        "Daichi" "Nah, persis! Tuh kan, sebenarnya otakmu cepat tangkap kok kalau nggak langsung lompat ke rumus pendek di buku paket. Dosen kita tuh paling suka jebak di kalimat soalnya doang. Coba sekarang kamu hitung satu contoh soal nomor tiga di bawahnya, aku lihatin dari sini."
        nar "Kamu menarik kertas coretan, menuliskan persamaan pelan-pelan mengikuti alur yang baru ia ajarkan, lalu memeriksa tanda plus dan minus di baris akhir."
        yutaka "Kalau dimasukkan ke rumus tadi... hasilnya seratus dua puluh unit, titik keseimbangannya naik dua angka. Benar nggak?"
        "Daichi" "Seratus persen tepat! Lihat, nggak sampai tiga menit kan? Coba satu lagi yang bagian elastisitas silang biar kamu hafal jebakan angkanya."
        yutaka "Oke, yang ini kalau produknya barang substitusi berarti nilainya positif, kan?"
        "Daichi" "Tepat banget! Sudah aman itu buat ukuran kuis besok pagi."
        yutaka "Ternyata cara menjelaskanmu jauh lebih gampang dicerna daripada buku teksnya. Makasih banyak, Daichi. Besok habis kuis kutraktir makan siang di kantin."
        "Daichi" "Nah, ini nih bagian yang paling kutunggu! Awas lupa ya besok! Ayo habisin satu bab terakhir lagi biar makin tenang tidurnya."
        nar "Selama dua jam berikutnya, Daichi membongkar ulang konsep-konsep dasar dari bab tiga hingga bab lima dengan sabar tanpa menaruh curiga sedikit pun mengapa kamu mendadak lupa materi awal, membuatmu siap menghadapi kuis esok pagi dengan kepala tegak."
    return

# ┌─ PANDUAN CERITA · Y06 · Daichi Membocorkan
# │ LOKASI  : Distrik Elite · Apartemen Yutaka
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Daichi tahu sesuatu tentang Shiori/Moeka dan menawarkannya.
# │ INTI    : A bayar dengan makanan / B tolak / C tawar informasi lain.
# │ AKHIRAN : intel; C membuat Daichi mulai mengorek rahasia pemain.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y06:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Daichi membocorkan")
    nar "Malam itu jarum jam dinding di ruang tamu apartemenmu baru saja melewati pukul delapan ketika bel interkom pintu depan berbunyi dua kali. Saat kamu membuka pintu, Nakamura Daichi sudah berdiri di lorong dengan jaket denim tebal dan tangan yang dimasukkan ke saku karena kedinginan."
    "Daichi" "Malam, Yutaka! Untung lampu ruang tamumu kelihatan nyala dari bawah. Aku mampir sebentar nih, nggak lagi sibuk kan?"
    yutaka "Nggak lagi sibuk kok. Masuk aja, Daichi. Tumben malam-malam naik ke sini tanpa kirim pesan dulu, habis dari mana?"
    nar "Daichi melepas sepatu ketsnya di genkan, lalu melangkah masuk dan langsung menjatuhkan diri duduk di sofa ruang tamu sambil menggosok kedua telapak tangannya di dekat pemanas."
    "Daichi" "Habis rapat logistik klub di gedung kemahasiswaan, terus tadi sempat mampir fotokopi berkas di dekat perempatan stasiun timur. Nah, waktu jalan balik dari stasiun tadi, aku kebetulan lihat sesuatu yang lumayan bikin penasaran."
    yutaka "Lihat apa memangnya di dekat stasiun?"
    "Daichi" "Bukan cuma satu sih. Yang pertama soal Kohinata Moeka dari Fakultas Seni, itu kulihat langsung pakai mataku sendiri dari seberang jalan. Terus yang kedua soal Saionji Shiori, ini kudengar waktu anak-anak klub debat lagi ngobrol di ruang fotokopi tadi."
    nar "Ketika melihatmu duduk di kursi seberang meja kaca dan menatapnya dengan serius tanpa menyela, cengiran santai di wajah Daichi perlahan mereda. Ia mencondongkan tubuhnya ke depan dengan kedua siku bertumpu di lutut."
    "Daichi" "Kamu kan lumayan sering kelihatan ngobrol sama mereka berdua akhir-akhir ini, makanya kupikir kamu pasti pengin tahu."
    yutaka "Terus kenapa nggak langsung diceritain aja dari tadi?"
    nar "Daichi menyeringai lebar sambil menepuk perutnya yang berbunyi pelan."
    "Daichi" "Masalahnya dari sore tadi aku belum sempat makan malam sama sekali nih, Yutaka. Pesenin dua mangkuk ramen chashu dari kedai depan stasiun lewat aplikasi dong, nanti sambil nunggu kuahnya datang kuceritain semuanya sampai tuntas."
    call kk_family_menu("Y06", ["\"Ya sudah, kupesanin ramen sekarang. Cerita aja.\"", "\"Nggak usah deh, Daichi. Aku males dengerin kabar burung.\"", "\"Gimana kalau tukar kabar aja? Aku juga tahu jadwal panitia yang kamu cari.\""])
    if _return == "A":
        yutaka "Ada-ada aja alasanmu minta makan malam gratis. Ya sudah, ini kubuka aplikasinya, kupesanin ramen chashu dua porsi sama gyoza. Tapi awas ya kalau yang mau kamu ceritain ini cuma gosip ngawur."
        "Daichi" "Enak aja ngawur! Aku nggak bakal jauh-jauh mampir ke apartemenmu kalau cuma bawa gosip murahan, Yutaka. Nih, dengerin baik-baik, kupisahin dulu mana yang kulihat sendiri sama mana yang kudengar dari orang."
        yutaka "Oke, mulai dari yang kamu lihat sendiri di dekat stasiun timur tadi. Soal Kohinata kenapa?"
        "Daichi" "Tadi sekitar jam setengah tujuh malam, aku lewat depan ruko tua tiga lantai yang bagian atasnya disewain buat studio foto komersial itu. Pintu besinya kebuka, terus Kohinata keluar dari sana."
        yutaka "Dia habis pemotretan sendirian?"
        "Daichi" "Nah, masalahnya nggak sendirian. Di belakangnya ada pria umur tiga puluhan pakai jaket kulit hitam dan rambut diikat. Mukanya Kohinata tuh kelihatan pucat dan capek banget, Yutaka, jalannya aja agak nunduk. Tapi begitu pria itu ngerangkul bahunya sambil bisik sesuatu, Kohinata langsung maksa senyum lebar kayak biasanya."
        yutaka "Pria jaket kulit rambut diikat... Kuga Renji maksudmu?"
        "Daichi" "Aku nggak tahu namanya siapa, tapi gaya orang itu jelas bukan anak kampus kita, dan cara dia megang bahu Kohinata tadi kelihatan terlalu menekan buat ukuran rekan kerja biasa. Terus kalau kabar kedua soal Saionji, ini kudengar dari ketua klub debat yang kakaknya kerja di grup bisnis Tojo."
        yutaka "Keluarga Tojo yang kemarin datang ke resepsi klub catur itu?"
        "Daichi" "Persis. Katanya belakangan ini pihak keluarga Tojo rajin banget nyebar omongan di kalangan relasi bisnis seolah pertunangan antara pewaris mereka, Tojo Akihiro, sama Saionji Shiori itu sudah hampir resmi dan tinggal nunggu tanggal. Padahal setahuku dari pihak keluarga Saionji sendiri belum pernah keluar pernyataan apa-apa."
        yutaka "Jadi pihak Tojo sengaja bikin tekanan dari luar supaya Saionji susah nolak di depan umum ya. Masuk akal sama gelagatnya kemarin. Makasih banyak infonya, Daichi."
        "Daichi" "Sama-sama. Cuma tolong jangan sebut-sebut kamu dengar dari aku ya, males banget kalau nanti aku ikut dilirik sinis sama lingkaran bisnis mereka. Eh, itu bel bawah sudah bunyi, kayaknya kurir ramennya sudah sampai tuh!"
        nar "Kamu bangkit mengambil pesanan makanan hangat di pintu depan, sementara kedua informasi dari Daichi barusan tersimpan jelas di kepalamu untuk langkah berikutnya."
    elif _return == "B":
        yutaka "Nggak usah deh, Daichi. Simpan aja ceritamu. Aku lagi malas dengerin urusan pribadi orang lain dari belakang, apalagi kalau harus dibarter pakai traktiran kayak transaksi makelar begini."
        nar "Daichi mengerjap dua kali menatapmu, lalu mendengus geli dan menyandarkan punggungnya kembali ke bantal sofa."
        "Daichi" "Wah, tumben banget seorang Kisaragi Yutaka nggak kepancing penasaran. Biasanya kalau ada kabar soal anak-anak populer di kampus, kamu paling cepat pasang telinga."
        yutaka "Lagi banyak pikiran soal kuliah aja minggu ini. Tapi kalau kamu memang beneran kelaparan habis rapat dan mau makan ramen bareng di sini tanpa bahas gosip orang, ayo aja kupesanin sekarang."
        "Daichi" "Lah, serius tetap dipesenin makan walaupun aku nggak jadi buka mulut?! Boleh banget lah kalau gitu, rezeki nggak boleh ditolak!"
        yutaka "Iya, sudah kupencet pesanannya nih, lima belas menit lagi sampai. Ambil aja kaleng soda di kulkas kalau haus."
        nar "Daichi tertawa lebar. Sebelum bangkit menuju dapur, ia menoleh sebentar ke arahmu dengan raut wajah yang lebih serius."
        "Daichi" "Tapi tenang aja, Yutaka. Aku tadi minta traktir ramen cuma buat bercanda kok. Kalau suatu hari nanti apa yang kulihat soal teman-temanmu itu beneran kelihatan gawat atau membahayakan mereka, aku pasti langsung kasih tahu kamu tanpa minta bayaran apa-apa."
        yutaka "Nah, kalau ngomong gitu dari awal kan enak dengarnya. Sana ambil minumnya dulu."
        nar "Sambil menunggu kurir ramen tiba, Daichi menyalakan konsol di meja ruang tamu dan menghabiskan malam itu dengan mengobrolkan pertandingan bola serta tugas kuliah tanpa sedikit pun menyinggung gosip kampus lagi."
    else:
        yutaka "Daripada aku keluar uang buat traktir makan malam, gimana kalau kita barter informasi aja, Daichi? Minggu kemarin waktu di kantin kamu sempat ngeluh lagi nyari bocoran jadwal pembagian stan festival sama kuota gudang logistik panitia buat usaha titip belimu, kan? Aku pegang jadwal lengkapnya."
        nar "Mata Daichi langsung membulat antusias. Ia segera mengeluarkan buku catatan kecil dari saku jaket denimnya."
        "Daichi" "Serius kamu tahu jadwal buka gudang sama kuota mejanya, Yutaka?! Wah, itu informasi mahal banget buat ngatur stok barangku bulan depan! Kalau beneran lengkap, kita sepakat tukar kabar sekarang!"
        nar "Kamu menyebutkan rincian jadwal pengiriman logistik, jam pemeriksaan stan sayap timur, serta pembagian kuota meja panitia yang sempat kamu dengar dengan jelas dari percakapan Koita dan Moeka beberapa hari lalu."
        nar "Daichi mencatat semuanya dengan cepat di halaman bukunya sambil manggut-manggut puas. Begitu titik terakhir selesai ia tulis, ujung pulpennya berhenti. Ia tidak langsung membalas dengan ceritanya, melainkan mengangkat kepala dan menatapmu dengan kening berkerut tajam."
        "Daichi" "...Tunggu sebentar deh, Yutaka. Kok kamu bisa hafal urutan jam logistik panitia lintas fakultas sampai ke menit-menitnya begini? Kamu kan bahkan nggak masuk seksi perlengkapan tahun ini."
        yutaka "Kebetulan aja aku duduk di sebelah mereka waktu anak-anak panitia lagi bahas jadwal di kantin."
        "Daichi" "Masa cuma dengar sambil lalu bisa hafal sedetail itu? Semester lalu aja kamu ditanya jadwal kuis kelas sendiri sering lupa. Akhir-akhir ini kamu kelihatan rajin banget ya merhatiin dan ngumpulin jadwal orang-orang di sekitar Koita?"
        yutaka "Perasaanmu aja kali. Jadi gimana, sekarang giliranmu cerita soal Kohinata sama Saionji sesuai janji."
        nar "Daichi menatapmu dua detik lebih lama sambil memasukkan buku catatannya ke saku, lalu tetap menepati janjinya menceritakan soal Moeka yang tampak tertekan saat keluar dari studio foto komersial bersama seorang fotografer pria, serta kabar burung dari lingkaran keluarga Tojo yang berusaha memojokkan Shiori lewat isu pertunangan."
        "Daichi" "Sudah lunas ya bagianku. Kapan-kapan kita tukar kabar lagi, Yutaka... kayaknya banyak hal menarik kalau merhatiin langkahmu belakangan ini."
        nar "Setelah Daichi pamit dan pintu apartemen kembali tertutup, kamu menyadari bahwa kebiasaanmu mengumpulkan celah informasi kini mulai membuat mata Daichi ikut mengawasi gerak-gerikmu sendiri."
    return

# ┌─ PANDUAN CERITA · Y07 · Natal: Apartemen Sepi
# │ LOKASI  : Distrik Elite · Apartemen Yutaka
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Natal; orang tua Kisaragi tidak menelepon.
# │ INTI    : A pergi ke rumah Amamiya / B mengundang heroine / C sendiri / D mengejar Koita
# │ AKHIRAN : hub besar #3 untuk host.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y07:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Natal sepi")
    nar "Malam Natal tiba di apartemen lantai atas Distrik Elite tanpa satu pun suara yang menyambut. Dari balik jendela kaca lebar ruang tamu, lampu-lampu jalan raya dan menara pertokoan di kejauhan tampak berkelip ramai, kontras dengan lantai kayu ruanganmu yang dingin dan terlalu luas untuk satu orang."
    nar "Di atas meja makan kayu gelap yang dikelilingi empat kursi, layar ponselmu menyala dua kali berturut-turut. Kamu sempat menoleh, tetapi isinya hanyalah pemberitahuan diskon kue akhir tahun dari minimarket dan catatan otomatis transfer uang saku bulanan dari rekening perusahaan keluarga Kisaragi. Tidak ada panggilan masuk, bahkan satu baris pesan ucapan pun tidak ada dari Kenji maupun Reiko."
    nar "Kamu baru saja menaruh satu piring keramik, sepasang sumpit, dan segelas air dingin di ujung meja. Di sebelah piring itu, tiga kursi kayu lainnya berdiri rapi menghadap dinding kosong. Jarum detik pada jam tangan tipis hadiah dari Pak Daisuke di pergelangan tangan kirimu berdetak pelan di tengah dengung pemanas ruangan."
    nar "Menatap permukaan meja yang terlalu lapang itu, tebersit pertanyaan singkat di kepalamu tentang sudah berapa kali Natal yang dilewati Yutaka asli dengan duduk diam di kursi yang sama persis seperti malam ini."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Kirim pesan lalu pergi ke Rumah Amamiya.", "Undang salah satu teman dekatmu ke apartemen.", "Habiskan malam Natal sendirian di apartemen.", "Hubungi Koita dan minta bertemu dengannya berdua saja."])]
    call screen kk_choice_panel(_rows, "Pilihan")
    $ kk_record_choice("Y07", _return)
    if _return == "A":
        nar "Kamu menghela napas pendek, mengambil mantel navy dari gantungan di lorong depan, lalu mengirim satu pesan singkat kepada Koita untuk memastikan apakah ia ada di rumah. Belum sampai satu menit, balasan Koita langsung masuk menyuruhmu datang sekarang juga."
        nar "Di perjalanan menuju perumahan Amamiya, kamu sempat mampir di toko roti dekat persimpangan untuk membeli satu kotak kue stroberi ukuran sedang agar tidak datang dengan tangan kosong. Sepuluh menit kemudian, langkahmu berhenti di depan pagar kayu Rumah Amamiya yang lampu terasnya menyala hangat."
        nar "Begitu tombol bel kamu tekan, terdengar suara langkah cepat dari dalam lorong dan pintu langsung ditarik terbuka. Koita berdiri di ambang pintu dengan kaus rajut santai dan celemek biru tua yang masih terikat di pinggangnya, membawa aroma sup krim hangat dari arah dapur."
        koita "Akhirnya datang juga! Masuk, masuk, di luar anginnya kencang banget. Ibu tadi baru aja nanya dari dapur, apa kita perlu nyisain porsi ekstra buat kamu malam ini."
        yutaka "Tahu aja aku bakal muncul. Nih, aku bawa kue stroberi dari toko depan stasiun, jangan bilang kalian sudah beli dua loyang."
        koita "Pas banget, kami belum sempat beli kue soalnya tadi sore hujan rintik sebentar. Sini kutaruh di meja makan. Kamu lepas mantel dulu, habis itu bantu aku bawa piring ke meja ya, jangan cuma duduk santai terus ngeledek kayak biasanya."
        yutaka "Iya, iya, baru sampai depan pintu sudah langsung dikasih kerjaan."
        nar "Begitu kamu melepas sepatu di genkan dan melangkah masuk ke ruang tengah, Bu Yoshie melongok dari balik meja dapur dengan senyum hangat sambil mengaduk panci besar, sementara Chiasa sudah duduk di kursi makan merapikan deretan sendok dan gelas."
        "Bu Yoshie" "Selamat malam, Yutaka-kun! Wah, kamu bawa kue segala, terima kasih banyak ya. Ayo cepat duduk di dekat pemanas, telingamu sampai merah begitu kena angin."
        yutaka "Selamat malam, Bu Yoshie. Maaf ya saya mampir mendadak malam Natal begini."
        "Bu Yoshie" "Mendadak apanya, piring buatmu kan memang selalu Ibu hitung kalau malam begini. Orang tuamu tahun ini masih sibuk perjalanan bisnis di luar kota?"
        yutaka "Iya, Bu, jadwal akhir tahun mereka lagi padat."
        "Bu Yoshie" "Kalau begitu makan yang banyak di sini ya. Sup krimnya baru saja matang."
        chiasa "Tumben banget Yutaka-kun nggak lupa bawa buah tangan. Kukira cuma mau datang modal perut kosong kayak tahun lalu."
        yutaka "Eh, tahun lalu aku bawa jus apel dua botol lho, kamu aja yang lupa karena langsung rebutan ayam panggang sama Koita."
        chiasa "Nggak tuh, yang rebutan paha ayam kan Ko-nii sama Yutaka-kun."
        koita "Hei, kok aku ikut kena? Sudah, sudah, Yutaka, tolong angkat mangkuk salad itu ke tengah meja sebelum dingin."
        nar "Kamu meraih mangkuk keramik yang disodorkan Koita dan meletakkannya di antara loyang ayam panggang dan kotak kue stroberi. Suara piring yang beradu, celotehan Chiasa yang terus menyahuti ledekanmu, serta uap sup hangat yang dituang Bu Yoshie membuat malam Natal di meja makan yang sempit itu terasa jauh lebih hidup daripada apartemen luas yang kamu tinggalkan setengah jam lalu."
    elif _return == "B":
        nar "Kamu mengambil ponsel dari atas meja, menggulir daftar kontak sejenak, lalu menghubungi salah satu kenalan dekatmu yang beberapa hari lalu sempat bilang belum punya acara tetap di malam Natal. Nada sambung berbunyi tiga kali sebelum panggilannya diangkat."
        yutaka "Halo? Lagi sibuk nggak? Aku cuma mau nanya, malam ini kamu beneran di kamar aja atau sudah ada rencana keluar?"
        nar "Di seberang sana terdengar suara sedikit terkejut sekaligus santai, menjawab bahwa ia memang cuma berencana makan malam biasa dan menonton acara televisi akhir tahun."
        yutaka "Kalau belum makan dan nggak keberatan jalan sebentar, mau mampir ke apartemenku nggak malam ini? Tempatku lagi sepi banget, dan terus terang aja, malam ini aku lagi nggak pengin makan sendirian."
        nar "Ada jeda singkat di ujung sambungan sebelum ia menjawab setuju dan mengatakan akan berangkat sekarang juga, paling lama dua puluh menit sudah tiba di lobi bawah."
        yutaka "Oke, pakai syal yang tebal ya, angin di luar kencang. Nanti kalau sudah sampai pintu bawah tinggal pencet bel kamarku aja."
        nar "Begitu telepon ditutup, suasana apartemen yang tadi terasa kaku mendadak bergerak. Kamu segera merapikan majalah yang tergeletak di sofa, mengambil satu piring dan gelas tambahan dari lemari dapur, lalu menyalakan kompor untuk memanaskan sup krim dan roti bawang yang tadi sore kamu beli di pasar swalayan."
        nar "Dua puluh menit kemudian, bel interkom di dekat pintu masuk berbunyi. Saat kamu membukakan pintu, tamu malammu berdiri di koridor sambil menenteng kantong kertas berisi dua botol minuman hangat dan sekotak kue cokelat kecil, pipinya sedikit memerah karena angin malam."
        yutaka "Masuk, masuk. Maaf ya malah bikin kamu keluar jauh-jauh pas udara lagi sedingin ini."
        nar "Ia melepas mantel dan sepatunya di lorong depan, lalu ikut melangkah ke ruang makan yang kini sudah harum oleh sup krim panas. Begitu kalian duduk berhadapan dan mulai makan, obrolan langsung mengalir tanpa rasa canggung, mulai dari keluhan soal tugas akhir tahun sampai cerita ringan tentang keramaian toko-toko dekat stasiun tadi sore."
        yutaka "Makasih ya sudah mau nyempetin datang malam ini. Aku nggak ngundang kamu cuma buat ngisi kursi kosong di meja kok. Memang beneran senang aja kalau malam ini ada kamu di sini."
        nar "Mendengar ucapanmu yang lugas tanpa nada bercanda, ia sempat terdiam sejenak dengan sendok di tangan sebelum tersenyum lembut dan menimpali bahwa ia juga senang tidak melewatkan malam ini sendirian. Kalian terus mengobrol hingga cangkir teh kedua habis dan jam dinding melewati pukul sepuluh."
    elif _return == "C":
        nar "Kamu meletakkan kembali ponsel ke atas meja makan dengan layar menghadap ke bawah. Tidak ada pesan yang kamu ketik untuk Koita, tidak pula panggilan untuk siapa pun di daftar kontakmu."
        nar "Kamu melangkah ke dapur, memanaskan ulang kotak ayam panggang dan sup instan yang tadi sore kamu beli di kedai dekat stasiun, lalu menyendok nasi hangat ke dalam satu mangkuk keramik. Saat kembali ke meja makan, kamu menyalakan televisi di ruang tamu dengan volume pelan sekadar agar apartemen tidak sepenuhnya sunyi oleh dengung mesin pemanas."
        nar "Suara pembawa acara musik akhir tahun dan tepuk tangan penonton di layar kaca terdengar sayup menemani bunyi sumpitmu. Kamu menghabiskan seluruh isi piring sebelum supnya sempat dingin, menatap sekilas pada tiga kursi kosong di seberang meja tanpa banyak pikiran yang perlu dirumuskan."
        nar "Selesai makan, kamu membawa piring, mangkuk, dan gelas itu ke bak cuci, membilasnya sampai bersih, lalu menyeduh secangkir kopi hitam panas. Dengan cangkir hangat di tangan, kamu berdiri sebentar di dekat jendela kaca lebar yang berembun di bagian sudutnya, memandangi deretan lampu mobil yang melintas pelan di jalan raya bawah."
        nar "Tidak ada kunjungan mendadak dan tidak ada telepon susulan hingga larut malam. Saat rasa kantuk mulai turun menjelang pukul sebelas, kamu membiarkan lampu ruang tamu tetap menyala redup sebelum menutup pintu kamar tidurmu."
    else:
        nar "Kamu mengambil ponsel dari atas meja makan, membuka kontak paling atas yang biasa kamu hubungi, lalu menekan tombol panggil tanpa menunggu lebih lama. Nada sambung berbunyi empat kali sebelum suara Koita terdengar dari seberang dengan latar suara televisi yang samar."
        koita "Halo, Yutaka? Tumben langsung telepon malam-malam. Kamu mau mampir ke rumah ya? Ibu baru aja selesai masak sup krim nih, sini aja langsung."
        yutaka "Bukan ke rumahmu, Koita. Aku mau ketemu kamu malam ini. Berdua aja."
        nar "Di ujung sambungan, suara Koita langsung berhenti selama dua detik. Terdengar bunyi kursi bergeser pelan, seolah ia menjauh dari ruang tengah rumahnya menuju lorong."
        koita "Eh? Berdua aja? Tunggu, kamu lagi ada masalah ya, Yutaka? Atau orang tuamu barusan telepon terus bikin ribut lagi?"
        yutaka "Nggak ada masalah apa-apa sama orang tuaku. Mereka malah nggak telepon sama sekali hari ini."
        koita "Hah? Terus kenapa nada suaramu serius banget kayak mau nagih utang begitu? Haha, kalau kamu bosan sendirian di apartemen, kan tinggal jalan kaki sepuluh menit ke rumahku, Chiasa juga lagi di sini kok."
        yutaka "Koita, dengerin dulu. Aku nggak lagi bercanda, dan aku juga bukan mau nongkrong ramai-ramai di ruang tengahmu."
        nar "Kamu bersandar di tepi meja makan, menurunkan nada bicaramu agar terdengar jelas tanpa celah untuk ia alihkan dengan lelucon."
        yutaka "Aku cuma nggak mau malam Natal ini lewat begitu saja tanpa ketemu dan dengar suaramu langsung. Bisa keluar sebentar nggak? Aku tunggu di luar."
        nar "Keheningan di seberang telepon berlangsung jauh lebih lama kali ini. Candaan ringan yang biasa dipakai Koita untuk mencairkan suasana mendadak surut, tergantikan oleh embusan napas pelan."
        koita "...Kamu serius ngomong begitu, Yutaka? Iya deh... kalau gitu kita ketemu di bangku tepi sungai dekat kedai kopi yang di belokan stasiun aja ya. Dua puluh menit lagi aku sampai sana. Pakai mantel yang tebal, di luar dingin banget."
        yutaka "Oke. Dua puluh menit lagi, aku jalan sekarang."
        nar "Kamu segera mengenakan mantel dan syalmu, lalu berjalan kaki menyusuri trotoar yang sepi menuju tepi sungai. Tepat saat kamu tiba di bawah lampu jalan dekat bangku kayu, Koita ternyata sudah lebih dulu berdiri di sana dengan jaket gelapnya, menggenggam dua kaleng kopi panas dari mesin penjual otomatis."
        nar "Begitu melihatmu mendekat, Koita langsung menyodorkan satu kaleng ke arahmu dengan kening berkerut kesal. Jemarimu sempat menyentuh punggung tangannya yang dingin sepersekian detik lebih lama saat menerima kaleng hangat itu, membuat Koita langsung menarik tangannya mundur dengan gerakan kaku."
        koita "Nih, pegang! Tunggu dulu, Yutaka. Aku kira tadi kamu lagi ada masalah gawat sama orang tuamu, makanya aku langsung lari keluar malam-malam begini! Tahunya kamu beneran cuma ngajak duduk berdua di pinggir sungai sambil lihat lampu Natal?!"
        yutaka "Kan di telepon tadi sudah kubilang jelas, aku nggak lagi ada masalah apa-apa. Memangnya kenapa kalau malam ini cuma ada kita berdua?"
        nar "Wajah Koita langsung memerah sampai ke telinga di bawah sorot lampu jalan kuning. Ia melirik sepasang kekasih yang kebetulan melintas di trotoar seberang, lalu menoleh balik memelototimu dengan suara ketus."
        koita "Kenapa kamu tanya?! Ini malam Natal lho, Yutaka! Duduk berdua sama cowok di bangku tepi sungai sambil pegang kopi panas begini... kelihatannya aneh banget tahu nggak! Merinding aku lihat cara kamu natap aku dari tadi!"
        yutaka "Kalau memang semerinding itu, kenapa kamu tetap lari keluar ke sini bawa dua kopi panas buatku?"
        nar "Kalimatmu yang tenang dan sedikit meledek itu langsung membuat Koita tersedak ucapannya sendiri. Mulutnya membuka lalu menutup lagi sebelum ia mendengus keras dan membuang pandangannya ke permukaan sungai."
        koita "Itu... itu cuma karena aku takut kamu kesepian sendirian di apartemen terus jadi mikir yang aneh-aneh! Kita kan sahabat dari kecil, wajar lah kalau aku khawatir!"
        yutaka "Iya, iya. Makasih sudah khawatir sama aku. Ayo duduk dulu, kopinya keburu dingin."
        nar "Kamu duduk santai di bangku kayu lalu menepuk ruang kosong tepat di sebelahmu. Koita memelototi tempat duduk itu selama dua detik dengan bibir mengerucut kesal, menggerutu pelan bahwa kamu makin hari makin menyebalkan, lalu tetap menjatuhkan diri duduk di sampingmu dengan kerah jaket ditarik tinggi menutupi separuh pipinya yang merah."
        koita "Jangan lihatin aku terus! Lihat sana ke lampu di seberang sungai! Dasar seenaknya sendiri!"
        nar "Kamu tersenyum tipis melihat reaksinya yang tetap defensif sambil meneguk kopi hangatmu. Ia terus mengomel pelan di tengah angin malam yang dingin, tetapi kakinya sama sekali tidak beranjak dari bangku di sebelahmu."
    return

# ┌─ PANDUAN CERITA · Y08 · Coklat dari Siapa
# │ LOKASI  : Distrik Elite · Apartemen Yutaka
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Valentine; Yutaka menerima coklat dari banyak orang.
# │ INTI    : A balas satu orang / B balas semua sama / C tolak semua / D memberi coklat pada Koita
# │ AKHIRAN : menyalakan rantai BL atau rantai heroine.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y08:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Coklat Valentine")
    nar "Malam tanggal empat belas Februari di apartemen lantai atas Distrik Elite terasa sunyi dengan dengung pelan mesin pemanas ruangan. Di sudut meja makan kayu gelap, berjajar belasan kotak cokelat dan bungkusan pita yang kamu bawa pulang dari kampus sepanjang hari."
    nar "Beberapa di antaranya hanyalah cokelat toko biasa dari kenalan satu kelas atau anggota panitia yang dilengkapi stiker ucapan santai. Di baris sebelah kanan, ada beberapa kotak buatan tangan yang terbungkus jauh lebih hati-hati, masing-masing menyelipkan kartu kecil dengan tulisan tangan rapi yang membuatmu tidak bisa membacanya sambil lalu."
    nar "Kamu menarik satu kursi, menyalakan lampu meja, lalu meletakkan ponselmu di sebelah tumpukan kartu tersebut. Layarnya berkedip dua kali oleh notifikasi pesan masuk yang menanyakan apakah cokelatnya sudah sampai dengan aman. Orang-orang yang memberimu kotak-kotak ini jelas sedang menaruh risiko kecil agar perasaannya kamu ketahui malam ini."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Balas satu orang saja dengan maksud yang jelas.", "Siapkan balasan yang sopan dan setara untuk semuanya.", "Tolak semua harapan romantis mereka dengan terus terang.", "Ajak Koita naik sebentar dan berikan kotak cokelat khusus kepadanya."])]
    call screen kk_choice_panel(_rows, "Pilihan")
    $ kk_record_choice("Y08", _return)
    if _return == "A":
        nar "Kamu menatap deretan kotak di meja cukup lama, lalu menarik satu kotak berpita rapi ke depanmu sementara sisanya kamu geser ke sisi kanan. Setelah merapikan kartu-kartu kecil yang lain, kamu membuka aplikasi pesan di ponselmu dan menuliskan ucapan terima kasih yang ramah kepada setiap pengirim lain tanpa menyisakan janji samar atau ajakan susulan."
        nar "Baru setelah semua pesan sopan itu terkirim, kamu membuka satu ruang obrolan yang sejak tadi kamu biarkan di urutan paling atas. Kamu mengetik balasan yang jauh lebih lugas, mengucapkan terima kasih karena ia sudah repot menyiapkannya sendiri, lalu mengajaknya keluar berdua saja akhir pekan ini agar kalian bisa bicara lebih tenang."
        nar "Jempolmu sempat tertahan sepersekian detik di atas tombol kirim. Di tengah ruang tamu yang sunyi ini, kamu membaca ulang dua baris kalimatmu sendiri, bertanya sebentar di dalam kepala apakah nama yang kamu pilih malam ini memang benar-benar keinginanmu atau sekadar langkah yang paling mudah kamu pertanggungjawabkan."
        nar "Pada akhirnya kamu tetap menekan kirim. Tidak sampai dua menit kemudian, layar ponselmu menyala dengan panggilan suara masuk dari orang tersebut. Kamu mengangkatnya sambil bersandar di sandaran kursi."
        yutaka "Halo? Belum tidur ternyata. Pesanku barusan sudah terbaca ya?"
        nar "Di ujung sambungan terdengar helaan napas kecil yang agak gugup diikuti tawa lembut, memastikan apakah ajakan akhir pekanmu barusan sungguh-sungguh dan dimaksudkan untuk bertemu berdua saja."
        yutaka "Iya, serius. Kalau cuma mau bilang makasih biasa, aku nggak bakal repot-repot nulis sepanjang itu. Nanti hari Sabtu aku jemput di depan stasiun jam dua siang, cocok nggak?"
        nar "Ia langsung mengiyakan dengan suara yang terdengar jauh lebih lega dan hangat daripada sebelumnya, lalu mengucapkan selamat malam sebelum sambungan ditutup. Kamu meletakkan kotak cokelat darinya terpisah di dekat cangkir kopimu sementara malam perlahan merambat larut."
    elif _return == "B":
        nar "Kamu menarik buku catatan kecil dari laci meja, menyusun daftar nama semua pengirim di selembar kertas, lalu membuka aplikasi pesan di ponselmu. Untuk setiap nama yang sudah mengirimimu cokelat hari ini, kamu menuliskan balasan ucapan terima kasih yang hangat, ramah, dan nyaris setara panjangnya."
        nar "Kamu memuji bungkusnya, mengucapkan terima kasih karena sudah repot-repot di tengah padatnya jadwal kuliah, dan menyelipkan kalimat manis bahwa kamu pasti akan menyiapkan balasan saat White Day bulan depan. Tidak ada satu pun pesan yang terasa dingin, dan tidak ada pula satu kalimat pun yang mengikatmu pada satu orang saja."
        nar "Begitu semua pesan selesai dikirim, layar ponselmu mulai bergetar bergantian. Dua teman sekelasmu membalas santai dengan stiker tertawa. Sementara itu, dua pengirim lain justru membalas sangat cepat dengan kalimat yang penuh antusiasme, menanyakan rasa apa yang paling kamu suka dan apakah nanti boleh bertemu langsung saat White Day."
        nar "Kamu meletakkan ponselmu dengan layar menghadap ke atas sambil memandangi deretan balasan yang terus bermunculan. Kesopanan yang seragam itu memang membuat malam ini lewat tanpa satu pun pertengkaran atau wajah kecewa. Melihat betapa cepat orang-orang membaca harapan yang berbeda dari kalimat manis yang sama persis, kamu jadi paham sendiri mengapa kebiasaan Koita untuk terus bersikap baik kepada semua orang terasa begitu menggoda sekaligus melelahkan."
    elif _return == "C":
        nar "Kamu mengembuskan napas panjang, memisahkan beberapa kotak yang jelas membawa kartu bernada pengakuan, lalu mulai mengetik pesan satu per satu. Kamu berterima kasih dengan sopan atas usaha dan cokelat yang mereka berikan, lalu menuliskan secara terus terang bahwa kamu tidak bisa membalas harapan romantis mereka dan tidak ingin membiarkan mereka menunggu sesuatu yang tidak akan kamu berikan."
        nar "Jari-jarimu menekan tombol kirim untuk pesan terakhir. Beberapa menit pertama berlalu tanpa suara. Kemudian satu balasan masuk sangat singkat, hanya mengiyakan dan meminta maaf sudah merepotkan. Pesan kedua dibalas dengan tawa teks yang tampak terlalu dipaksakan, seolah pengirimnya mendadak ingin menganggap cokelat buatannya tadi cuma candaan biasa. Pesan ketiga hanya memunculkan tanda terbaca tanpa satu kata pun."
        nar "Tepat saat kamu hendak menutup layar, ponselmu bergetar oleh panggilan masuk dari salah satu mahasiswi yang cukup dekat denganmu di panitia. Kamu mengangkatnya tanpa menunda."
        yutaka "Halo? Kamu sudah baca pesanku?"
        nar "Di seberang sambungan, suaranya terdengar sedikit bergetar meski ia berusaha keras menjaga nadanya tetap ringan. Ia bertanya pelan apakah ia melakukan sesuatu yang membuatmu tidak nyaman tadi siang, atau apakah memang sudah ada orang lain yang sedang kamu sukai."
        yutaka "Kamu sama sekali nggak bikin aku nggak nyaman. Cokelatmu juga kuhargai, makanya aku nggak mau pura-pura nggak paham maksud kartumu terus membiarkan kamu nebak-nebak sampai bulan depan. Maaf karena jawabanku nggak sesuai yang kamu harapkan."
        nar "Hening pendek menggantung di sambungan telepon sebelum ia menarik napas pelan, mengucapkan terima kasih karena kamu mau menjawab dengan jujur, lalu menutup panggilan dengan cepat."
        nar "Kamu menurunkan ponsel ke atas meja makan. Tidak ada cara membuat penolakan terasa ringan bagi siapa pun. Malam ini kamu memilih membiarkan rasa kecewa itu tetap utuh di pihak mereka tanpa mengirim pesan susulan hanya demi ditenangkan dari rasa bersalahmu sendiri."
    else:
        nar "Kamu menggeser seluruh tumpukan kotak cokelat dari para mahasiswi itu jauh ke ujung bufet agar tidak memenuhi meja makan. Dari dalam tas jaketmu, kamu mengeluarkan satu kotak kecil berwarna hitam doff berpita abu-abu gelap yang sejak sore tadi sengaja kamu beli di toko cokelat dekat stasiun, lengkap dengan selembar kartu kecil yang sudah kamu tulis sendiri dengan tinta hitam."
        nar "Kamu mengambil ponsel dan mengirim pesan singkat kepada Koita, menyuruhnya mampir sebentar ke apartemenmu kalau sedang tidak sibuk. Lima menit kemudian balasannya masuk, mengira kamu cuma butuh teman menghabiskan tumpukan cokelat atau mau pinjam catatan kuliah. Lima belas menit berselang, bel interkom berbunyi."
        nar "Begitu pintu apartemen kamu buka, Koita melangkah masuk dengan jaket gelap dan syal longgar, menggigil sebentar sambil melepas sepatunya di genkan."
        koita "Dingin banget di luar, Yutaka! Tumben malam-malam nyuruh aku naik ke sini. Mana tumpukan cokelat dari cewek-cewek fakultasmu yang katanya mau minta tolong dihabisin? Jangan kasih aku yang rasanya aneh-aneh ya."
        yutaka "Duduk dulu aja di ruang tamu. Aku nggak nyuruh kamu naik buat ngabisin cokelat sisa orang."
        nar "Koita mengangkat sebelah alis sambil berjalan ke dekat meja makan dan melihat permukaan meja yang bersih, kecuali satu kotak kecil hitam berpita abu-abu gelap di tengahnya. Kamu melangkah mendekat, mengambil kotak itu, lalu menyodorkannya langsung ke depan dada Koita."
        yutaka "Nih, buat kamu. Selamat hari Valentine, Koita."
        nar "Koita menatap kotak di tanganmu lalu mendengus sambil tertawa ringan, masih mengira kamu sedang menjahilinya seperti kebiasaan lama kalian."
        koita "Haha, apaan nih, Yutaka? Tumben banget kamu iseng bungkusin cokelat begini. Ada jebakan isinya rasa cabai atau wasabi ya di dalam?"
        yutaka "Nggak ada jebakan apa-apa. Cokelat hitam biasa. Buka aja kartunya di balik pita itu biar jelas."
        nar "Karena nada suaramu terlalu datar dan sama sekali tidak terdengar seperti orang yang sedang melawak, senyum santai Koita perlahan memudar. Ia meraih kotak itu dengan ragu, menyelipkan jarinya di bawah pita abu-abu gelap, lalu menarik kartu kecil di dalamnya dan membaca dua baris tulisan tanganmu."
        nar "Wajah Koita seketika membeku. Dalam hitungan detik, rona merah pekat merambat dari pipi sampai ke ujung kedua telinganya. Tangannya yang memegang kartu langsung bergetar pelan sebelum ia mendongak menatapmu dengan mata melebar penuh syok dan amarah yang mendadak meledak."
        koita "...Tunggu dulu! Apa-apaan tulisan kayak gini, Yutaka?! Kamu beneran nulis ini buat aku?! Buat aku, cowok?!"
        yutaka "Iya. Tulisanku cukup jelas kan? Nggak perlu kubacain ulang."
        koita "Jangan ngomong santai gitu dong! Kamu kepentok pintu atau lagi demam tinggi sih hari ini?! Kita sama-sama cowok, Yutaka! Aku ini normal, aku suka cewek! Kenapa tiba-tiba kamu nyodorin cokelat Valentine sambil nulis kalimat gila begitu ke sahabatmu sendiri?!"
        nar "Suara Koita meninggi memantul di dinding ruang tamu yang sunyi. Kamu tetap berdiri tenang dengan satu tangan bersandar di tepi meja makan, menatapnya lurus tanpa sedikit pun mengalihkan pandangan atau menarik ucapanmu."
        yutaka "Aku sadar banget kamu cowok, Koita. Dan aku juga nggak lagi sakit. Aku cuma sudah capek aja lihat kamu terus-terusan diperebutkan orang lain sementara aku disuruh diam di pinggir pura-pura nggak peduli."
        nar "Koita terdiam setengah detik mendengar kalimatmu yang begitu telanjang, lalu kedua tangannya mengepal erat di sisi tubuhnya. Sorot matanya tampak goyah antara panik, marah, dan rasa kecewa yang menusuk."
        koita "Kamu... kamu nggak tahu gimana rasanya di posisiku sekarang?! Tiap hari di kampus aku sudah cukup capek mikirin perasaan orang-orang di sekitarku, terus aku selalu percaya kalau sama kamu semuanya aman! Kamu sahabatku dari SMP, Yutaka! Tempat satu-satunya aku bisa ngobrol biasa tanpa takut bikin orang berharap! Terus sekarang tiba-tiba kamu malah... kamu bikin aku ngerasa kayak dikhianati tahu nggak?!"
        nar "Dada Koita naik turun cepat, matanya menatapmu tajam dengan wajah yang masih merah padam. Kamu memperhatikan gejolak di wajahnya dengan tenang, lalu melangkah maju satu langkah hingga jarak di antara kalian menyempit. Koita refleks mundur setengah langkah sampai betisnya menyentuh tepi sofa."
        yutaka "Aku nggak pernah nipu kamu soal persahabatan kita, Koita. Cuma aku juga nggak mau bohong terus-terusan ke diriku sendiri."
        koita "H-hei, jangan maju dekat-dekat begitu! Berdiri aja di sana!"
        nar "Kamu berhenti melangkah persis di tempatmu, tetap menghormati jarak yang ia minta tanpa sedikit pun melunakkan sorot matamu."
        yutaka "Oke, aku diam di sini. Aku nggak nyuruh kamu kasih jawaban malam ini juga. Kamu mau marah, mau nyangkal, mau nggak percaya, itu hakmu sepenuhnya. Tapi aku nggak bakal narik balik apa yang sudah kutulis di kartu itu."
        koita "Dasar seenaknya sendiri! Kamu tuh selalu aja begini, ngomong hal yang bikin orang pusing tujuh keliling terus pasang muka tenang kayak nggak bersalah sama sekali!"
        nar "Koita memelototi kotak hitam di tangannya dengan napas kesal. Ia sempat melirik ke arah meja seolah ingin membanting kotak itu kembali ke depanmu, lalu bibirnya mengerucut keras dan tangannya justru mencengkeram kotak tersebut lebih erat."
        yutaka "Kalau kamu beneran nggak mau, tinggal taruh aja lagi di meja. Nggak kupaksa bawa pulang."
        koita "Nggak! Jangan salah paham dulu ya, aku sama sekali nggak nerima omongan ngawurmu! Aku bawa ini cuma karena sayang aja kalau cokelat mahal begini mubazir nggak dimakan! Dan aku butuh waktu buat mikir ini sebenarnya otakmu lagi konslet di bagian mana!"
        nar "Koita segera membalikkan badan dengan langkah kaku menuju genkan, memasukkan kotak cokelat beserta kartumu ke dalam saku dalam jaketnya, lalu buru-buru memasang sepatunya dengan gerakan kikuk."
        koita "Aku pulang sekarang! Besok di kampus awas aja kalau kamu berani bertingkah aneh-aneh di depan orang lain, beneran nggak bakal kumaafin!"
        yutaka "Hati-hati di jalan, Koita. Pakai syalnya yang bener, di luar dingin."
        koita "Nggak usah sok perhatian!"
        nar "Pintu apartemen tertutup cukup keras di belakangnya. Ruang tamu kembali sunyi, menyisakan udara dingin dari lorong luar. Ia pergi dalam keadaan marah besar dan menyangkal habis-habisan, tetapi satu hal tidak bisa ia sangkal malam ini, kotak cokelat darimu tetap ia bawa pulang di dalam jaketnya."
    return

# ┌─ PANDUAN CERITA · Y11 · Yukata dan Chiasa
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : festival; Chiasa memakai yukata.
# │ INTI    : A pujian / B gunakan godaan Yutaka asli / C diam.
# │ AKHIRAN : Chiasa menilai apakah "Yutaka" masih Yutaka.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y11:
    call kk_scene_enter("yutaka", "Rumah Amamiya · Yukata dan Chiasa")
    nar "Chiasa keluar dengan yukata, lalu membetulkan ujung lengan yang sebenarnya sudah rapi. Ia berhenti di depanmu seolah ada percakapan yang dijanjikan oleh kebiasaan lama. Kau ingin mengatakan sesuatu yang disukainya, tetapi tidak tahu apakah yang sedang ditunggu adalah suaramu atau suara Yutaka dahulu."
    call kk_family_menu("Y11", ["Puji penampilannya dengan tulus.", "Pakai gaya menggoda Yutaka asli.", "Diam saja."])
    if _return == "A":
        chiasa "Terima kasih. Kau bilang begitu tanpa meledek? Aku sampai menyiapkan jawaban yang tidak jadi dipakai. ...Tidak, jangan diubah. Aku suka mendengarnya."
    elif _return == "B":
        chiasa "Nah, mulai lagi. Aku tahu kau akan menggodaku. Tapi jangan terus sembunyi di balik bercanda, Yutaka. Sesekali aku ingin tahu bagian mana yang sungguh kaukatakan."
    else:
        nar "Kau diam terlalu lama. Chiasa menunduk memeriksa pakaiannya, lalu bertanya apakah ada yang salah. Ketika kau mengatakan tidak, ia mengangguk dan beralih membicarakan jalan menuju festival. Kau mengikuti sambil sadar bahwa diam pun dapat terdengar seperti penilaian."
    return

# ┌─ PANDUAN CERITA · Y12 · Pameran Chiasa
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : pameran seni; Haruka mengenalkan Chiasa.
# │ INTI    : A belikan karya / B hadir saja / C kritik.
# │ AKHIRAN : Chiasa membuka diri atau menjauh.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y12:
    call kk_scene_enter("yutaka", "Rumah Amamiya · Pameran Chiasa")
    nar "Haruka memperkenalkan karya Chiasa kepada pengunjung. Dari samping kau melihat Chiasa mencoba berdiri tenang sambil mengawasi reaksi setiap orang. Ketika menemukan wajahmu, senyumnya sebentar menjadi lebih kecil dan lebih jujur. Kau datang sebagai orang yang mengenalnya sebelum label seniman ditempelkan di dinding."
    call kk_family_menu("Y12", ["Beli salah satu karyanya.", "Hadir dan memberi dukungan.", "Kritik karyanya terang-terangan."])
    if _return == "A":
        chiasa "Kau benar ingin yang ini? Aku senang, tapi jangan membeli karena merasa harus menolongku. Ceritakan bagian yang kausukai. ...Ya. Kalau itu alasanmu, aku ingin kau yang menyimpannya."
    elif _return == "B":
        chiasa "Kau datang. Aku tadi takut akan terlalu sibuk memperhatikan orang yang tidak kukenal. Kalau nanti aku banyak bicara tentang gambarnya, dengarkan, ya. Aku sedang mencoba tidak gugup."
    else:
        nar "Kau menyampaikan kritik di depan pengunjung lain tanpa menanyakan apakah ia siap membahasnya sekarang. Chiasa menjawab seperlunya, kemudian kembali melayani orang yang datang. Kalian belum tentu berbeda pendapat tentang gambar itu. Yang membuatnya menjauh adalah caramu memilih saat untuk mempermalukannya."
    return

# ┌─ PANDUAN CERITA · Y14 · Hari Bentrok: Pernyataan Yutaka
# │ LOKASI  : Distrik Elite · Apartemen Yutaka
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : hari pengakuan.
# │ INTI    : A mengaku pada Chiasa / B mengaku pada Koita / C mengaku pada heroine / D tidak mengaku.
# │ AKHIRAN : hub besar #8.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y14:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Hari pengakuan")
    nar "Hari ini pesan masuk bertumpuk, masing-masing meminta waktu bertemu. Kau meletakkan ponsel dan mencoba memisahkan rasa takut kehilangan dari keinginan sungguh mendekat. Menyatakan cinta berarti berbicara kepada seseorang yang boleh menjawab lain; tidak ada nama dalam daftar kontak yang bisa menjamin keselamatan hatimu."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Mengaku pada Chiasa.", "Mengaku pada Koita.", "Mengaku pada seorang heroine.", "Tidak mengaku pada siapa pun."])]
    call screen kk_choice_panel(_rows, "Pilihan")
    $ kk_record_choice("Y14", _return)
    if _return == "A":
        nar "Kau menemui Chiasa dan mengaku menyukainya. Kau tidak memakai kedekatan keluarga Amamiya sebagai alasan agar ia menerima. Ia mendengarkan sampai selesai, lalu menyebut namamu pelan. Apa pun jawabannya nanti, ia kini tahu ada bagian dari candaanmu yang tidak lagi bisa dianggap biasa."
    elif _return == "B":
        nar "Kau mengatakan kepada Koita bahwa perasaanmu telah melewati persahabatan. Ia diam, lalu bertanya sejak kapan. Kau menjawab sejauh yang benar-benar kauketahui. Tidak ada desakan agar ia segera memilih; hanya keberanian membiarkan seorang sahabat melihatmu tanpa perlindungan lelucon."
    elif _return == "C":
        nar "Kau menemui perempuan yang ingin kaupilih dan mengucapkan perasaanmu dengan jelas. Kau tidak membawa daftar orang lain yang bisa menjadi pengganti. Sesudah kata-kata selesai, ada ruang hening yang menjadi miliknya untuk menjawab. Kau berusaha tidak memenuhi ruang itu dengan janji tambahan."
    else:
        nar "Kau tidak menyatakan cinta hari ini. Ada pesan yang tetap kaubalasi dengan ramah dan percakapan yang kaubawa ke topik lain. Pilihan itu terasa aman sampai malam, ketika kau menyadari bahwa orang yang menunggu juga dapat memutuskan berhenti menunggu tanpa memberimu kesempatan terakhir."
    return

# ┌─ PANDUAN CERITA · Y15 · Jarak dari Rumah
# │ LOKASI  : Distrik Elite · Apartemen Yutaka
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : perjalanan; Yutaka merasa jauh dari keluarga Kisaragi.
# │ INTI    : A bicara dengan Daisuke / B menelepon ibu / C diam.
# │ AKHIRAN : ending Yutaka.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y15:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Jarak dari rumah")
    nar "Jendela kendaraan memperlihatkan rumah-rumah yang akan didatangi orang sepulang bekerja. Kau memikirkan keluarga Kisaragi dan betapa sedikit bagian dari mereka yang kaukenal. Merindukan keluarga lamamu tidak membatalkan kesepian Yutaka. Kini kedua kehilangan itu bertemu dalam satu tubuh yang tidak tahu harus menelepon siapa."
    call kk_family_menu("Y15", ["Bicara dari hati dengan Daisuke.", "Menelepon ibu Kisaragi.", "Diam dan memendamnya."])
    if _return == "A":
        "Daisuke" "Kau boleh bicara denganku tanpa harus menunggu Koita punya masalah dulu. Aku mungkin tidak punya jawaban, tapi aku bisa mendengar. Jangan merasa perlu menghiburku saat kau sendiri sedang susah."
    elif _return == "B":
        nar "Kau menelepon ibu Kisaragi. Ia terkejut, lalu mencoba mengingat kapan terakhir kalian bicara di luar urusan uang. Kehangatannya kaku dan terlambat, tetapi ada. Kau mendengarkan suara seorang ibu yang tidak mengenalmu, bertanya-tanya apakah ia mendengar perubahan pada anak yang sedang ia rindukan."
    else:
        nar "Kau menahan keinginan menelepon. Di luar, rumah-rumah terus berlalu dan percakapan orang lain terdengar jauh. Tidak berbagi membuatmu terhindar dari jawaban yang salah; ia juga membuat tak seorang pun tahu bahwa hari ini kau membutuhkan seseorang untuk bertanya apakah kau baik-baik saja."
    return

# ┌─ PANDUAN CERITA · Y16 · Kembang Api dan Chiasa
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : A mengaku / B bergandengan / C menjaga jarak.
# │ AKHIRAN : Chiasa × Yutaka (NPC) berjalan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y16:
    call kk_scene_enter("yutaka", "Rumah Amamiya · Kembang api dan Chiasa")
    play sound "audio/sfx/fireworks.wav"
    nar "Chiasa berdiri di sebelahmu ketika kembang api pertama menyala. Ia tidak sibuk mencari Koita di antara kerumunan. Di sela suara ledakan, percakapan kalian terputus lalu disambung dengan tawa kecil. Kau bertanya dalam hati apakah kedekatan ini masih ingin kausimpan sebagai kemungkinan yang tidak pernah dinamai."
    call kk_family_menu("Y16", ["Mengaku pada Chiasa.", "Bergandengan tangan tanpa kata.", "Menjaga jarak."])
    if _return == "A":
        chiasa "Aku dengar. Tidak perlu mengulang cuma karena kembang apinya keras. ...Aku ingin tahu apakah besok kau masih akan mengatakannya, saat kita tidak punya langit sebagus ini untuk disalahkan."
    elif _return == "B":
        nar "Kau menawarkan tangan. Chiasa menatapnya sebentar sebelum membiarkan jarinya bertemu jarimu. Kalian tetap melihat langit. Kesediaannya tidak menjawab semua pertanyaan tentang masa depan, tetapi sentuhan itu datang dari dua orang yang sama-sama memilih untuk tidak menjauh malam ini."
    else:
        chiasa "Aku mengerti. Kita bisa melihat kembang apinya saja. ...Jangan memandangku seolah aku harus segera bilang aku tidak kecewa. Aku akan baik-baik saja, tapi beri aku sebentar."
    return

# ┌─ PANDUAN CERITA · Y18 · Pameran Tunggal Chiasa
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : A hadir / B absen / C membawa seseorang.
# │ AKHIRAN : hubungan Yutaka–Chiasa.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y18:
    call kk_scene_enter("yutaka", "Rumah Amamiya · Pameran tunggal Chiasa")
    nar "Nama Chiasa tercetak di undangan pameran tunggalnya. Di bawah judul, ia menulis sepenggal kalimat tentang hal yang ingin dipertahankan ketika semuanya berubah. Kau membaca undangan itu lebih dari sekali. Hari pembukaan punya arti bagi pekerjaannya, bahkan jika hubungan kalian sedang sulit dijelaskan."
    call kk_family_menu("Y18", ["Hadir mendukungnya.", "Absen dari pameran.", "Membawa seseorang bersamamu."])
    if _return == "A":
        chiasa "Kau datang. Aku ingin menunjukkan satu gambar sebelum tempat ini ramai. Bukan karena kau harus punya jawaban yang bagus. Aku hanya ingin kau melihatnya bersamaku."
    elif _return == "B":
        nar "Kau tidak hadir. Chiasa memeriksa pintu beberapa kali sebelum mulai memberi penjelasan kepada pengunjung. Pamerannya tetap berjalan; pekerjaan bertahun-tahun tidak berhenti karena satu kursi kosong. Ketika kau melihat foto acara itu nanti, kau tidak tahu pada saat mana ia akhirnya berhenti mencarimu."
    else:
        nar "Kau datang membawa seseorang dan memperkenalkannya dengan jelas. Chiasa menyambut kalian, lalu menjelaskan karyanya tanpa menjadikan tamumu alat untuk menebak perasaanmu. Ada pertanyaan pribadi yang ia simpan sampai kalian punya kesempatan bicara sendiri. Hari ini ia juga berhak menjadi seniman yang sedang merayakan pekerjaannya."
    return

init 1 python:
    _hook("Y03-A", lambda: kk_suspect("nagisa",-4))
    _hook("Y03-B", lambda: kk_suspect("nagisa",8))
    _hook("Y03-C", lambda: kk_suspect("nagisa",3))
    _hook("Y04-A", lambda: kk_flag("yutaka_kuis_belajar"))
    _hook("Y04-B", lambda: (kk_flag("yutaka_menyontek"), kk_suspect("daichi",5)))
    _hook("Y04-C", lambda: kk_rel("nagisa","trust",2))
    _hook("Y04-D", lambda: kk_flag("daichi_dimintai_tolong"))
    _hook("Y06-A", lambda: kk_flag("daichi_intel_dibeli"))
    _hook("Y06-B", lambda: kk_rel("koita","trust",2))
    _hook("Y06-C", lambda: (kk_flag("daichi_mengorek"), kk_suspect("daichi",6)))
    _hook("Y07-A", lambda: kk_rel("koita","trust",4))
    _hook("Y07-B", lambda: kk_flag("yutaka_rantai_heroine"))
    _hook("Y07-C", lambda: kk_rel("koita","aff",-2))
    _hook("Y07-D", lambda: kk_flag("yutaka_arah_bl"))
    _hook("Y08-A", lambda: kk_flag("yutaka_rantai_heroine"))
    _hook("Y08-B", lambda: None)
    _hook("Y08-C", lambda: None)
    _hook("Y08-D", lambda: (kk_flag("yutaka_arah_bl"), kk_rel("koita","intim",5)))
    _hook("Y11-A", lambda: kk_suspect("chiasa",4))
    _hook("Y11-B", lambda: kk_suspect("chiasa",-5))
    _hook("Y11-C", lambda: kk_suspect("chiasa",6))
    _hook("Y12-A", lambda: (kk_flag("chiasa_karya_dibeli"), kk_rel("chiasa","intim",4)))
    _hook("Y12-B", lambda: kk_rel("chiasa","trust",4))
    _hook("Y12-C", lambda: kk_rel("chiasa","aff",-4))
    _hook("Y14-A", lambda: kk_flag("yutaka_arah_chiasa"))
    _hook("Y14-B", lambda: kk_flag("yutaka_arah_bl"))
    _hook("Y14-C", lambda: kk_flag("yutaka_rantai_heroine"))
    _hook("Y14-D", lambda: None)
    _hook("Y15-A", lambda: (kk_flag("kisaragi_daisuke_dekat"), kk_adj("hubungan_keluarga_kisaragi",8)))
    _hook("Y15-B", lambda: kk_adj("hubungan_keluarga_kisaragi",5))
    _hook("Y15-C", lambda: kk_adj("hubungan_keluarga_kisaragi",-5))
    _hook("Y16-A", lambda: (kk_rel("chiasa","intim",8), kk_flag("yutaka_chiasa_diakui")))
    _hook("Y16-B", lambda: (kk_rel("chiasa","intim",6), kk_flag("yutaka_arah_chiasa")))
    _hook("Y16-C", lambda: kk_rel("chiasa","jeal",4))
    _hook("Y18-A", lambda: (kk_rel("chiasa","intim",6), kk_flag("chiasa_pameran_yutaka_hadir")))
    _hook("Y18-B", lambda: kk_rel("chiasa","aff",-4))
    _hook("Y18-C", lambda: kk_rel("chiasa","jeal",4))
