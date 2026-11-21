# Grand Bab M01b (Revisi 1 — Diperpanjang & Dimainkan Penuh Tanpa Skip) — Host Chiasa (`H01` → `S01` → `Mi01`)

## 1. `H01` — *Perpustakaan Sains* (`game/kk_harumi.rpy`)
```renpy
label kkscene_H01:
    call kk_scene_enter("harumi", "Perpustakaan sains")
    if kk_host == "chiasa":
        nar "Di luar jendela kaca lebar lantai dua Gedung Sains & Lab, puncak-puncak pohon sakura bergoyang diterpa angin April sementara suara tawa rombongan Hanami terdengar samar dari kejauhan. Namun di dalam ruang baca ini, suasana nyaris sunyi sepenuhnya."
        nar "Hanya terdengar dengung halus pendingin ruangan, bau kertas buku referensi yang kering, sesekali bunyi halaman dibalik, serta goresan pelan ujung pensil mekanik di atas kertas."
        nar "Kau melangkah pelan menyusuri lorong di antara rak-rak tinggi untuk mencari buku referensi teori warna dan komposisi optik yang kebetulan tersimpan di bagian arsip lintas bidang. Begitu melewati deretan rak paling ujung dekat jendela sudut, langkahmu terhenti."
        nar "Di meja baca yang paling dekat dengan cahaya pagi pucat itu, seorang mahasiswi duduk sendirian menghadap buku teks tebal terbuka. Rambut abu-abunya yang agak panjang diikat satu menyamping hingga menjuntai rapi ke depan bahu kiri. Ia mengenakan kardigan abu-abu sederhana di atas kemeja putih bersih."
        nar "Kujo Harumi—mahasiswi tahun kedua yang kau kenal sepintas dari Koita dan cerita kelompok belajar SMA mereka. Di dalam manga, orang sering mengira ia sedingin mesin karena bicaranya selalu datar dan singkat, padahal ia sebenarnya hanya sangat lugas."
        nar "Satu jari tangan kirinya menahan tepi halaman buku agar tidak menutup, sementara tangan kanannya berulang kali menuliskan deretan angka dan tanda panah kecil pada buku catatan bersampul hitam di sebelahnya. Setiap beberapa detik, ia menaikkan bingkai kacamatanya dengan ujung jari tengah tanpa sedikit pun mengalihkan pandangan dari kertas."
        nar "Tepat di sampingnya, sebuah kursi kayu tampak sedikit tertarik keluar dari kolong meja—entah bekas seseorang yang baru saja beranjak pergi, atau ruang kosong yang memang dibiarkan terbuka."
        nar "Belum sempat kau memutuskan apakah akan langsung berbelok ke rak di belakangnya, mata biru tua di balik kacamata itu naik sekilas menangkap bayanganmu yang berdiri di ujung meja."
        harumi "Amamiya-san, bukan?"
        nar "Suaranya pelan, datar, dan terjaga rapi menyesuaikan keheningan ruang baca—sama sekali tidak terdengar kesal karena terganggu."
        harumi "Kalau kamu mencari buku referensi yang sedang kubuka ini, masih ada satu salinan lagi di rak baris ketiga sebelah kiri. Tapi kalau kamu sedang mencari tempat duduk... kursi di sebelahku ini belum dipakai siapa-siapa."
    call kk_family_menu("H01", ["Tarik kursi dan duduk di sampingnya.", "\"Sedang mengerjakan soal apa?\"", "Lewati mejanya agar ia bisa membaca dengan tenang."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau mengangguk singkat, lalu menarik kursi kayu di sebelahnya dengan sangat pelan agar kakinya tidak berdecit di atas lantai linoleum. Kau meletakkan tas kainmu di pangkuan dan duduk menghadap meja yang sama."
            chiasa "Terima kasih, Kujo-senpai. Di luar sedang agak terlalu ramai buat membaca dengan tenang, jadi aku numpang duduk sebentar di sini."
            nar "Harumi menoleh sekilas ke arah jendela kaca yang memperlihatkan kerumunan mahasiswa di taman bawah, lalu kembali menatap mejanya dengan ekspresi datar yang nyaris menyerupai humor kering."
            harumi "Benar. Keramaian di bawah pohon sakura menghasilkan terlalu banyak kebisingan akustik untuk membaca atau menghitung. Di sudut ini tingkat gangguannya jauh lebih rendah."
            nar "Tanpa perlu diminta, ia mendorong buku teks tebal di depannya beberapa sentimeter ke tengah meja agar sudut halamannya tidak tertutup bayangan lengannya, lalu merapikan kotak pensil dan penghapusnya sejajar di tepi atas."
            harumi "Kalau kamu mau melihat referensi di sini atau butuh ruang lebih lebar di sisi kanan, bukunya bisa kugeser ke tengah seperti ini."
            nar "Alih-alih langsung menenggelamkan wajahnya kembali ke deretan rumus, Harumi diam sejenak—menunggu dengan sabar sampai kau selesai mengeluarkan buku catatanmu dan menemukan posisi duduk yang nyaman."
            chiasa "Maaf kalau kehadiranku malah memecah konsentrasi Kujo-senpai."
            harumi "Tidak. Konsentrasiku tidak serapuh itu."
            nar "Ia membetulkan letak kacamatanya dengan gerakan jari yang tenang, lalu menoleh setengah badan kepadamu dengan sorot mata biru tua yang lurus dan jujur."
            harumi "Aku juga tidak keberatan dijeda kalau kamu sedang kesulitan mencari buku atau ingin menanyakan sesuatu. Aku hanya perlu diberi tahu secara langsung kalau memang ada pertanyaan—soalnya aku sering gagal membaca ekspresi orang yang sebenarnya ingin bicara."
            chiasa "Begitu, ya... baik, kalau ada yang ingin kutanyakan nanti pasti langsung kubilang, Senpai."
            harumi "Bagus. Itu jauh lebih efisien daripada sama-sama menebak."
            nar "Harumi mengangguk tipis seolah kesepakatan sederhana itu sudah cukup jelas dan menenangkan baginya, lalu kembali menurunkan pandangan ke deretan perhitungannya. Keheningan yang turun di antara kalian berdua kini terasa jauh lebih hangat dan akrab daripada basa-basi perkenalan yang biasanya diucapkan orang di kampus."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Alih-alih langsung duduk, kau berhenti di ujung meja dan mencondongkan badan sedikit sambil melirik barisan persamaan, tanda panah koreksi, serta grafik kecil yang digambar sangat rapi di buku catatan hitamnya."
            chiasa "Permisi, Kujo-senpai. Kelihatannya sejak tadi Kujo-senpai mengulang baris perhitungan yang sama berkali-kali—sedang mengerjakan soal apa?"
            nar "Ujung pensil mekanik Harumi terhenti tepat di atas sebuah angka. Ia tidak langsung menjawab, melainkan menatap baris terakhir tulisannya selama beberapa detik penuh sambil mengangkat sedikit telunjuk tangan kirinya memberi isyarat."
            harumi "Sebentar. Aku masih memeriksa bagian akhir jawabannya."
            nar "Caranya memintamu menunggu sama sekali tidak terasa angkuh atau seperti ingin memamerkan kepandaian. Kau memperhatikan bibirnya bergerak menggumamkan dua perbandingan angka tanpa suara, lalu ia mencoret satu baris kecil di pinggir kertas dan menuliskan angka pembanding baru dengan hati-hati—jelas ia hanya tidak mau menjelaskan sebuah kesimpulan sebelum ia sendiri yakin kebenarannya."
            nar "Sepuluh detik kemudian, ia menghela napas tipis yang nyaris tak terdengar, meletakkan pensil mekaniknya sejajar tepi buku, membetulkan kacamata, lalu memutar buku catatan hitamnya sembilan puluh derajat menghadap ke arahmu."
            harumi "Sudah. Ada satu variabel pada contoh soal di buku ini yang hasilnya tidak konsisten dengan grafiknya, jadi aku mengujinya ulang dari awal. Bagian mana yang ingin kamu tahu dulu, Amamiya-san?"
            chiasa "Grafik lengkung kecil di pojok bawah itu kelihatannya menarik—kalau tidak merepotkan Kujo-senpai."
            harumi "Tidak merepotkan. Untung kamu langsung menunjuk bagiannya—aku sering mulai menjelaskan terlalu jauh dari teori dasar kalau tidak ditanya secara spesifik."
            nar "Ia menarik kursi kosong di sebelahnya beberapa sentimeter lebih dekat agar kau bisa duduk atau membungkuk melihat dengan nyaman, lalu menunjuk garis kurva itu dengan ujung belakang pensilnya."
            harumi "Coba lihat titik tekukan di tengah ini. Bayangkan seperti gradasi cahaya pada permukaan melengkung—kalau nilai di baris sebelumnya berubah tiba-tiba, garisnya seharusnya patah tajam di sini. Di buku teks tercetak mulus karena penyuntingnya membulatkan angka terlalu cepat."
            chiasa "Oh... pantas saja tadi Kujo-senpai sampai menghitung ulang di kertas terpisah. Padahal kalau dilihat sepintas, garis di buku kelihatan benar-benar saja."
            nar "Harumi mengerjap sesaat mendengar tanggapanmu, seolah tidak menyangka kau benar-benar mengikuti penjelasannya sampai ke titik itu alih-alih sekadar mengangguk sopan."
            harumi "...Ya, persis seperti itu. Pengamatanmu cepat juga, Amamiya-san. Kalau kamu mau melihat dua halaman berikutnya, silakan duduk saja."
            nar "Untuk pertama kalinya sejak kau masuk ruang baca ini, sudut bibir Harumi tampak sedikit lebih rileks saat ia menggeser kursi untukmu."
    else:
        if kk_host == "chiasa":
            nar "Kau menatap sekilas lembaran perhitungan yang terbentang rapi di atas meja, lalu memutuskan tidak memecah ketenangan belajarnya pagi ini. Kau tersenyum tipis dan membungkuk kecil dengan sopan."
            chiasa "Terima kasih tawarannya, Kujo-senpai. Aku cuma lewat mau mengambil buku di rak belakang saja—tidak enak kalau sampai mengganggu waktu bacanya."
            nar "Harumi mempertahankan tatapannya padamu selama satu detik penuh, seolah benar-benar ingin memastikan kau tidak sedang menolak karena sungkan atau bingung mencari rak."
            harumi "Kamu yakin tidak butuh petunjuk letak raknya?"
            chiasa "Iya, tadi aku sudah lihat denahnya di dekat pintu masuk. Permisi, Kujo-senpai."
            harumi "Baiklah. Rak arsip lintas bidang ada di lorong sebelah kanan."
            nar "Ia mengangguk singkat dengan sopan. Kau melanjutkan langkah melewati mejanya menuju deretan rak belakang yang teduh."
            nar "Ketika beberapa menit kemudian kau mengambil buku dan sempat melirik dari ujung lorong, Harumi sudah kembali menundukkan kepala dengan satu jari menahan halaman buku teksnya. Kursi kayu di sebelahnya tetap tertarik sedikit keluar dalam keadaan kosong—sebuah kesempatan percakapan yang jelas tidak akan pernah ia panggil kembali dengan suara keras di tengah perpustakaan."
```

## 2. `S01` — *Papan Shogi di Taman* (`game/kk_spring.rpy`)
```renpy
label kkscene_S01:
    call kk_scene_enter("shiori", "Hanami · Taman Kampus")
    if kk_host == "chiasa":
        nar "Agak menjauh dari area rumput tengah tempat puluhan mahasiswa menggelar terpal piknik Hanami, sisi barat Taman Kampus terasa jauh lebih teduh dan lengang. Angin April masih terus menggugurkan kelopak sakura pucat ke atas jalan setapak batu dan bangku-bangku di bawah pohon tua."
        nar "Saat kau berjalan santai menyusuri jalur itu untuk mencari udara segar sejenak, bunyi 'klak' yang jernih dan mantap dari kayu yang beradu menarik perhatianmu."
        nar "Di sebuah meja batu teduh di pinggir taman, duduk seorang mahasiswi yang bahkan di tengah acara piknik kampus pun tampak seperti berada di ruang tersendiri. Rambut putih keperakannya ditata rapi dengan bagian atas menyilang bervolume dan gelombang panjang yang jatuh anggun ke depan melewati bahu. Pakaian semi-formalnya terlihat halus dan mahal, tetapi sama sekali tidak berlebihan."
        nar "Saionji Shiori—putri tunggal keluarga konglomerat yang di kampus dijuluki Ratu Fakultas. Kau belum pernah berbicara dengannya sebelumnya, dan hanya mengenal reputasinya dari ingatanmu membaca manga: bukan tipe gadis dingin yang angkuh, melainkan seseorang yang selalu ramah, sopan, namun senyumnya hampir mustahil dibaca."
        nar "Di hadapannya terbentang sebuah papan shogi kayu lipat. Dengan jari-jari rampingnya, Shiori mengangkat satu bidak kayu, meletakkannya di petak tengah dengan bunyi tajam, menatap formasi itu selama beberapa detik, lalu dengan tenang memutar seluruh papan seratus delapan puluh derajat agar ia dapat menakar posisi yang sama dari sisi lawan."
        nar "Tepat ketika ia hendak menggerakkan bidak berikutnya, sehelai kelopak sakura melayang turun dan mendarat persis di antara dua garis petak. Shiori tidak meniupnya begitu saja; ia menjepit kelopak merah muda itu dengan dua jari dan meletakkannya rapi di pinggir meja batu, seolah benda itu tamu tak diundang yang salah memilih kursi."
        nar "Tanpa tergesa sedikit pun, sepasang mata ungu amethyst-nya naik menatap ke arahmu. Senyum tipis yang ramah dan penuh percaya diri langsung tersungging di bibirnya."
        shiori "Selamat siang. Kalau kamu ingin duduk beristirahat di bangku ini, silakan saja—tempatnya masih cukup luas."
        nar "Ia sedikit memiringkan kepala, nada suaranya halus dan sopan, namun terasa seperti sedang menakar seberapa cepat kau akan bereaksi."
        shiori "Dan kalau kamu hendak bertanya mengapa ada orang yang bermain shogi sendirian di tengah keramaian Hanami, jawabannya sangat sederhana: karena sejauh ini belum ada yang duduk di seberang."
    call kk_family_menu("S01", ["Duduk di seberangnya dan tantang ia bermain.", "Berhenti sejenak dan amati langkah berikutnya.", "Beri salam singkat dan biarkan ia bermain sendiri."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau tidak gentar oleh senyum sopan yang terasa seperti saringan halus itu. Kau melangkah maju mendekati meja batu, meletakkan tas kainmu di samping bangku, lalu duduk tepat di seberang papan shogi kayu."
            chiasa "Kalau begitu, boleh aku yang mengisi sisi seberang, Saionji-senpai? Aku Amamiya Chiasa, mahasiswa tahun pertama."
            nar "Alis perak Shiori terangkat halus sepersekian milimeter mendengar kau langsung menyambut tantangannya alih-alih memberi alasan sopan untuk pergi. Senyum di wajahnya tidak melebar berlebihan, tetapi binar di mata ungu amethyst-nya langsung terasa jauh lebih hidup."
            shiori "Amamiya-san, ya. Baiklah—kalau begitu, sisi papan di depanmu itu resmi milikmu."
            nar "Ia membiarkanmu beberapa detik memeriksa susunan bidak yang tadi sedang ia mainkan sendiri, lalu dengan gerakan tangan yang tenang dan cekatan, ia mulai menarik kembali bidak-bidak kayu itu ke garis awal."
            chiasa "Tidak dilanjutkan dari posisi tadi saja, Senpai?"
            shiori "Tidak adil jika aku menyimpan keuntungan dari rencana yang sudah kubangun sendirian sebelum kamu duduk. Permainan yang layak dinikmati selalu dimulai dari garis yang sama."
            nar "Satu demi satu bidak terakhir mendarat rapi dengan bunyi kayu yang jernih. Shiori menautkan jari-jarinya sejenak di tepi meja batu, lalu memberi isyarat ringan ke arahmu."
            shiori "Silakan melangkah lebih dulu, Amamiya-san. Mari kita lihat apakah keputusan dudukmu hari ini akan membuat sore ini jadi menarik."
            nar "Kau mengamati barisan pion di depanmu, lalu menggerakkan satu pion pembuka di jalur tengah dengan bunyi kayu yang mantap. Tanpa ragu sedikit pun, tangan Shiori langsung membalas di sisi kanan—'klak'."
            shiori "Oh, pembukaan yang cukup lurus dan berani untuk orang yang tadi sempat berdiri diam mengamati. Kamu tidak memilih bermain aman?"
            chiasa "Kalau terlalu bertahan dari langkah pertama, rasanya malah cuma menunggu kalah dari Saionji-senpai."
            nar "Tawa kecil yang sangat halus lolos dari bibir Shiori, dan tatapan mata ungunya kini tertuju penuh kepadamu—tanda jelas bahwa namamu baru saja masuk ke daftar orang yang menarik perhatiannya di luar perkenalan singkat."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kau memilih tidak langsung menantangnya di wilayah yang jelas ia kuasai. Kau berhenti berdiri di sisi meja batu dengan tangan terlipat santai, menunduk mengamati formasi bidak kayu di atas papan."
            chiasa "Aku belum yakin sanggup mengimbangi Saionji-senpai. Boleh aku melihat beberapa langkah berikutnya saja dari sini?"
            shiori "Tentu. Penonton yang tenang tidak pernah mengganggu jalannya permainan."
            nar "Menyadari kau benar-benar mengikuti alurnya bukan sekadar melihat-lihat sambil lalu, Shiori sengaja memperlambat sedikit tempo gerakannya saat memindahkan dua bidak berikutnya, membiarkanmu melihat arah serangannya terbuka pelan."
            nar "Sambil menelusuri garis serong di atas papan kayu, matamu menangkap satu celah kecil di sisi kiri pertahanan yang tidak sengaja terbuka ketika ia mendorong bidak peraknya terlalu jauh ke depan."
            chiasa "Maaf menyela, Saionji-senpai—tapi kalau bidak perak itu maju ke petak tadi, bukannya jalur serong dari bidak gajah lawan di pojok kanan jadi terbuka langsung ke belakang?"
            nar "Jari-jari Shiori yang baru saja hendak mengangkat bidak balasan berhenti di udara. Ia tidak buru-buru membantah ataupun berpura-pura sudah memperhitungkannya. Sebaliknya, ia benar-benar menunduk, menelusuri garis diagonal dari pojok kanan ke baris belakang selama beberapa detik penuh."
            shiori "...Benar juga. Aku terlalu sibuk mempertahankan rencana seranganku sendiri sampai mengabaikan ancaman balasan dari jalur serong itu."
            nar "Ia mengembalikan bidak peraknya setengah petak ke posisi semula, lalu menoleh ke atas menatapmu dengan senyum tipis yang kali ini terasa jauh lebih tulus dan hangat daripada senyum sopannya tadi."
            shiori "Pengamatan yang tajam. Kalau kamu belum terburu-buru kembali ke keramaian, mau duduk sebentar dan melihat dua kemungkinan langkah berikutnya bersamaku? Aku penasaran jalur mana yang akan kamu pilih jika memegang sisi lawan."
            chiasa "Kalau cuma melihat kemungkinannya bersama, boleh saja, Senpai."
            nar "Kau duduk di sisi bangku batu, dan untuk pertama kalinya Shiori memutar papan sedikit miring ke arahmu agar kalian berdua bisa membedah variasi langkah di atas papan kayu yang sama."
    else:
        if kk_host == "chiasa":
            nar "Kau membalas senyum sopannya dengan anggukan ringan dan memilih tidak memecah keheningan di meja batu teduh itu."
            chiasa "Terima kasih tawarannya, Saionji-senpai. Tapi aku cuma lewat mencari angin sebentar—aku tidak mau mengganggu permainanmu."
            shiori "Begitu, ya. Terima kasih sudah menyapa. Selamat menikmati Hanami-nya juga."
            nar "Shiori mengangguk anggun tanpa sedikit pun raut kecewa ataupun berusaha menahan langkahmu. Senyum di bibirnya tetap sama tenangnya seperti saat kau pertama kali mendekat."
            nar "Kau berbalik dan melangkah kembali menuju jalan setapak yang dipenuhi guguran kelopak sakura. Belum lima langkah kau menjauh, bunyi 'klak' bidak kayu yang diletakkan di papan kembali terdengar mantap di belakangmu—tanda bahwa Shiori memiliki kesenangan sendiri yang tetap berjalan utuh tanpa perlu memintamu menjadi penonton."
```

## 3. `Mi01` — *Bento Hanami* (`game/kk_scenes.rpy`)
```renpy
label kkscene_Mi01:
    call kk_scene_enter("miyuki", "Taman Kampus")
    if kk_host == "chiasa":
        nar "Di bawah pohon sakura besar di bagian tengah Taman Kampus, aroma gurih telur dadar gulung hangat, ayam goreng renyah, dan kaldu rebusan mendadak menyeruak di antara bau rumput siang yang terkena sinar matahari."
        nar "Di atas selembar alas duduk yang terhampar rapi, Tachibana Miyuki—mahasiswi tahun ketiga yang kau kenal lewat Koita—tengah berlutut anggun melepas ikatan kain furoshiki krem yang membungkus sebuah kotak bento kayu bertingkat tiga."
        nar "Rambut hitam panjangnya yang lurus dan terurai tanpa hiasan bergoyang pelan ditiup angin. Mengenakan kardigan lembut di atas pakaian rapi, ia tampak begitu tenang dan keibuan—sampai sehelai kelopak sakura melayang jatuh tepat di tengah tutup kotak bento sebelum ia sempat mengangkatnya."
        nar "Miyuki menatap kelopak kecil itu, memajukan bibir sedikit, lalu meniupnya dengan raut wajah luar biasa serius seolah sedang menjalankan prosedur penting."
        "Mahasiswi di Sebelah" "Pfft—Tachibana-senpai serius banget sih cuma buat niup satu kelopak sakura!"
        nar "Tawa kecil dari mahasiswi di sebelah alasnya membuat Miyuki mengerjap kaget, lalu baru setelah kelopak itu melayang jatuh ke rumput, senyum lembut dan sedikit malu-malu ikut mengembang di wajahnya."
        nar "Tepat saat itulah mata biru sapphire-nya menoleh ke tepi jalan setapak dan menangkap sosokmu yang baru melintas. Ia langsung mengangkat tangan melambai pelan dengan kehangatan khasnya."
        miyuki "Ara, Chiasa-san? Pas sekali kamu lewat sini. Senpai lagi-lagi memasak terlalu banyak—kalimat itu mulai terdengar seperti kebiasaan buruk, ya. Kalau kamu belum makan siang, silakan duduk dan ikut makan bersama."
        nar "Kau melangkah mendekat ke tepi alas dan melihat isi kotak bento bertingkat tiga yang baru saja ia buka satu per satu. Setiap sekatnya ditata sangat rapi agar mudah dibagi: potongan tamagoyaki berwarna keemasan, karaage, bola nasi onigiri berbalut nori, sayur rebus warna-warni, hingga sekat kecil berisi lauk berbumbu merah. Bahkan di samping kotak sudah tertata rapi beberapa pasang sumpit sekali pakai, piring kertas, dan tisu basah yang jelas ia siapkan sebelum tahu siapa saja yang akan mampir."
        miyuki "Yang agak pedas Senpai pisahkan di pojok kanan sini ya, Chiasa-san. Jangan sampai Senpai merusak suasana Hanami pertamamu gara-gara salah ambil sambal."
    call kk_family_menu("Mi01", ["\"Tamagoyaki dan lauknya enak sekali, kelihatan dibuat dengan teliti.\"", "Bantu ia membawakan dan menata kotak bentonya yang berat.", "\"Maaf, Senpai, aku masih ada urusan lain.\""])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau melepas sepatu di pinggir rumput dan ikut duduk di tepi alas, menerima piring kertas serta sepasang sumpit yang disodorkan Miyuki. Kau mengambil sepotong tamagoyaki dan sedikit sayur rebus dari tingkat teratas, lalu mencicipinya perlahan."
            nar "Begitu gigitan pertama menyentuh lidah, kau langsung tahu ini bukan masakan asal jadi—lapisan telurnya tetap lembut dan berair kaldu meski sudah dibawa keluar ruangan, sementara manis gurihnya terasa sangat seimbang."
            chiasa "Tachibana-senpai, tamagoyaki sama sayur rebus ini enak sekali. Lapisannya lembut banget dan manis kaldunya pas—kelihatan sekali dibuat pelan-pelan dari pagi."
            nar "Miyuki mengerjap sesaat mendengar pujianmu yang begitu spesifik, bukan sekadar ucapan sopan 'enak' yang biasa dilontarkan orang sebelum menelan. Ia mencondongkan tubuhnya sedikit dengan mata biru sapphire yang tampak ingin memastikan."
            miyuki "Ara... benarkah kamu suka bagian itu? Kamu tidak sedang bilang begitu cuma karena sungkan sama Senpai, kan?"
            chiasa "Sungguh. Aku jarang makan tamagoyaki yang masih selembut ini walaupun sudah dibawa piknik."
            nar "Senyum anggun yang biasa ia pasang sebagai senior yang dewasa perlahan luruh menjadi tawa kecil yang terdengar jauh lebih ringan dan jujur."
            miyuki "Syukurlah... padahal bagian itu yang paling lama kubuat subuh tadi. Sempat hampir salah takar kaldu gara-gara masih mengantuk, lho. Senpai senang banget kamu menyadarinya, Chiasa-san."
            nar "Dengan wajah berbinar, ia segera menyumpitkan dua potongan tambahan beserta karaage dan meletakkannya ke piring kertasmu."
            chiasa "Eh—Tachibana-senpai, piringmu sendiri masih kosong lho dari tadi."
            nar "Gerakan sumpit Miyuki terhenti di udara. Ia menunduk melihat piring kertas bersih di depan lututnya sendiri, lalu mengedip bingung sebelum tertawa kecil."
            miyuki "Ara... benar juga, ya. Senpai terlalu sibuk membagi sampai lupa mengambil bagian sendiri."
            nar "Untuk beberapa detik di bawah guguran kelopak sakura itu, saat ia akhirnya mengambil sepotong tamagoyaki ke piringnya sendiri, senyumnya tampak jauh lebih muda daripada citra senior serba sempurna yang biasa ia perlihatkan di kampus."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Ketika dua mahasiswa lain mulai berdatangan di dekat pohon dan Miyuki hendak mengangkat tumpukan kotak bento bertingkat tiga itu untuk dipindahkan ke tengah alas yang lebih teduh dan rata, kau menangkap sesuatu yang luput dari orang lain: pergelangan tangan Miyuki sedikit menegang dan memerah menahan beban kotak kayu yang penuh sesak itu."
            nar "Tanpa menunggu ia kewalahan, kau langsung berjongkok di sampingnya dan menjulurkan kedua tangan menyangga bagian kotak terbawah."
            chiasa "Biar kubantu angkat bagian bawahnya, Tachibana-senpai. Kelihatannya berat sekali kalau dipindah sekaligus sendirian."
            nar "Bibir Miyuki sempat terbuka seolah hendak menolak secara otomatis—kebiasaan seseorang yang terlalu terbiasa memikul semuanya sendiri."
            miyuki "Eh, tidak usah repot-repot, Chiasa-san, Senpai bisa—"
            chiasa "Pergelangan tangan Senpai sudah agak merah dari tadi. Kita bawa berdua saja, lebih cepat dan tidak tumpah."
            nar "Miyuki terdiam sepersekian detik, melirik pergelangan tangannya sendiri lalu menimbang berat kotak kayu di pelukannya. Akhirnya ia menghela napas kecil yang lembut dan menyerahkan tingkat terbawah ke tanganmu."
            miyuki "Ara... ketahuan, ya. Terima kasih banyak, Chiasa-san. Aku selalu yakin sanggup membawa semuanya sendiri sampai baru sadar tanganku sudah terlanjur pegal."
            nar "Kalian berdua memindahkan kotak-kotak itu ke bagian alas yang rata di bawah bayangan dahan sakura. Begitu tutupnya dibuka kembali, kau ikut mengambil alih menata piring kertas dan membagikannya kepada dua mahasiswa yang baru duduk di pinggir agar Miyuki tidak lagi sibuk sendirian mengawasi semua orang."
            chiasa "Nah, sudah rapi. Sekarang Tachibana-senpai juga duduk dan makan dulu ya, nanti keburu dingin kena angin."
            miyuki "Iya... rasanya aneh juga ya, biasanya aku yang menyuruh orang lain makan duluan. Terima kasih sudah mengingatkan, Chiasa-san."
            nar "Dengan bahu yang tampak jauh lebih santai, Miyuki akhirnya benar-benar mengambil sumpitnya sendiri dan menikmati satu gigitan hangat sebelum angin siang mendinginkan masakannya."
    else:
        if kk_host == "chiasa":
            nar "Kau melirik sekilas arah gedung di belakang taman, lalu membungkuk sopan tanpa ikut melepas sepatu atau duduk di tepi alas pikniknya."
            chiasa "Terima kasih banyak tawarannya, Tachibana-senpai. Kelihatannya enak sekali, tapi aku masih ada urusan yang harus diselesaikan sebentar lagi, jadi aku permisi duluan."
            nar "Miyuki langsung mengangguk cepat dengan senyum lembut yang tampak begitu tenang dan terlatih. Tangannya segera menarik sedikit ujung kain furoshiki dan menggeser kotak bento ke dalam agar jalur langkahmu di tepi alas tetap lapang."
            miyuki "Oh, tentu saja, jangan sampai terlambat ya, Chiasa-san. Hati-hati di jalan. Kalau nanti urusannya cepat selesai dan masih lapar, boleh kok mampir lagi ke sini—makanannya masih banyak sekali."
            chiasa "Baik, Senpai. Terima kasih, permisi."
            nar "Kau mengangguk singkat lalu melangkah menjauh menyusuri jalan setapak yang dipenuhi kelopak sakura."
            nar "Ketika beberapa langkah kemudian kau sempat menoleh sekilas sebelum belokan pohon, kau melihat Miyuki sempat menunduk diam selama sepersekian detik memandangi tumpukan kotak bento tiga tingkat yang masih penuh itu—ada jeda sunyi yang sangat tipis di wajahnya, sebelum tangannya kembali bergerak cekatan dan senyum hangat yang sama kembali terpasang siap saat mahasiswa berikutnya melintas."
```
