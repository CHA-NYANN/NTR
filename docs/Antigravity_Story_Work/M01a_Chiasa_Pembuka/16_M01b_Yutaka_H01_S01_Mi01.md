# Grand Bab M01b — Host Yutaka (`H01` → `S01` → `Mi01`)
*(Melengkapi `Mo01` Host Yutaka yang sudah ACC sebelumnya)*

## 1. `H01` — *Perpustakaan Sains* (`game/kk_harumi.rpy`, blok `else:`)
```renpy
    # --- Pembukaan (Host Yutaka) ---
    else:
        nar "Di luar jendela kaca lebar lantai dua Gedung Sains & Lab, kelopak sakura berterbangan di atas keramaian Hanami yang terdengar samar seperti dengung jauh. Sebaliknya, di dalam ruang baca ini, udara terasa dingin, kering, dan nyaris sunyi sepenuhnya."
        nar "Kau masuk ke sini sekadar untuk menjauh sebentar dari bisingnya taman kampus sekaligus mencari buku referensi dasar yang mungkin bisa membantu menutupi banyak materi kuliah yang sama sekali tidak kauingat. Dengan kedua tangan masih terselip di saku jaket, langkahmu melambat di ujung lorong rak dekat jendela sudut."
        nar "Di meja baca paling pojok yang diterangi cahaya pagi pucat, duduk seorang mahasiswi berkacamata dengan rambut abu-abu agak panjang yang diikat satu menyamping hingga menjuntai ke depan bahu kirinya. Kardigan abu-abu di atas kemeja putihnya tampak serapi cara duduknya yang tegak."
        nar "Kujo Harumi—wajah yang sempat kaulihat di foto lama dan grup obrolan teman-teman Koita. Satu jari tangan kirinya menahan halaman buku teks tebal agar tidak menutup, sementara tangan kanannya berulang kali menggoreskan deretan perhitungan pada buku catatan kecil bersampul hitam di sebelahnya. Sesekali ia menaikkan bingkai kacamatanya dengan ujung jari tengah tanpa sedikit pun mengangkat pandangan."
        nar "Tepat di sebelah kursinya, sebuah kursi kayu lain tampak agak tertarik keluar dari kolong meja—tidak jelas apakah bekas seseorang yang baru saja beranjak, atau ruang yang memang dibiarkan terbuka."
        nar "Ketika kau berhenti dua langkah dari ujung meja, mata biru tua di balik kacamata itu naik sekilas menangkap bayanganmu."
        harumi "Kisaragi-kun?"
        nar "Suaranya datar, pelan, dan terjaga sesuai keheningan ruang baca—sama sekali tidak terdengar terkejut maupun terganggu."
        harumi "Kalau kamu mencari buku referensi yang sedang kubuka ini, masih ada satu salinan lagi di rak baris ketiga sebelah kiri. Kalau kamu sedang mencari tempat duduk... kursi di sebelahku ini belum dipakai."

    # --- Pilihan A (Host Yutaka) ---
        else:
            nar "Kau mengangguk santai, menarik kursi kayu di sebelahnya dengan pelan agar tidak menimbulkan bunyi gesekan, lalu duduk sambil meletakkan buku catatan tipis dan tasmu di samping kaki meja."
            yutaka "Makasih, Kujo-san. Di luar terlalu berisik buat baca tenang, jadi aku numpang duduk sebentar di sini."
            nar "Harumi melirik sekilas ke arah jendela kaca yang memperlihatkan kerumunan di bawah pohon sakura, lalu kembali menatap mejanya dengan wajah datar."
            harumi "Masuk akal. Tingkat kebisingan di taman siang ini memang tidak cocok untuk berkonsentrasi."
            nar "Tanpa diminta, ia menggeser buku teks tebal di hadapannya beberapa sentimeter ke tengah meja agar ruang di sisimu lebih lega, lalu merapikan penghapus dan kotak pensilnya sejajar di tepi atas."
            harumi "Kalau kamu mau ikut melihat atau butuh ruang menulis di sebelah kanan, bukunya bisa kugeser ke tengah seperti ini."
            nar "Ia benar-benar menunggu dengan tenang sampai kau selesai membuka catatanmu dan duduk nyaman, tidak langsung menenggelamkan wajahnya kembali ke bacaan."
            yutaka "Tidak apa-apa kalau aku di sini? Takutnya malah mengganggu."
            harumi "Tidak. Konsentrasiku tidak terganggu oleh orang yang duduk diam. Dulu waktu kelompok belajar juga kamu sering diam dulu sebelum bertanya."
            nar "Kalimat pendek itu memberimu satu petunjuk kecil tentang bagaimana pemilik asli tubuh ini biasanya bersikap di depan Harumi. Ia membetulkan letak kacamatanya, lalu menoleh setengah badan padamu."
            harumi "Aku juga tidak keberatan dijeda kalau ada yang mau ditanyakan, Kisaragi-kun. Hanya saja, katakan langsung kalau ada pertanyaan—aku kurang pandai menebak dari ekspresi wajah."
            yutaka "Oke, catat. Nanti pasti langsung kubilang kalau aku mentok."
            nar "Harumi mengangguk pelan seolah kesepakatan lurus itu sudah cukup jelas, lalu kembali menurunkan pandangannya ke kertas hitungannya. Cara kerjanya yang sabar dan tanpa basa-basi itu terasa jauh lebih hangat daripada perkenalan ramah yang dibuat-buat."

    # --- Pilihan B (Host Yutaka) ---
        else:
            nar "Kau tidak langsung duduk, melainkan berhenti di tepi meja sambil menumpukan sebelah tangan ringan di sandaran kursi kosong dan melirik deretan angka serta coretan koreksi di buku catatan hitamnya."
            yutaka "Dari tadi kelihatannya kau mengulang baris yang sama terus, Kujo-san. Lagi mengerjakan soal apa?"
            nar "Ujung pensil mekanik Harumi berhenti di atas kertas. Ia tidak langsung menoleh, melainkan menatap baris terakhir hitungannya selama beberapa detik penuh sambil mengangkat sedikit telunjuk tangan kirinya."
            harumi "Sebentar. Aku masih memeriksa bagian akhir jawabannya."
            nar "Caranya memintamu menunggu sama sekali tidak terasa seperti orang yang sedang pamer kepandaian. Kau melihatnya mencoret satu angka pembulatan, menggumamkan perbandingan pelan tanpa suara, lalu menuliskan ulang hasil akhirnya—ia jelas tidak mau menjelaskan kesimpulan yang belum ia yakini sendiri."
            nar "Setelah memastikan angkanya cocok, ia meletakkan pensilnya sejajar tepi buku, membetulkan kacamata, lalu memutar buku catatannya menghadap ke arahmu agar mudah dibaca."
            harumi "Sudah selesai. Ada satu tabel tren di buku ini yang selisih datanya meleset dari rumus pengantarnya, jadi aku menghitung ulang untuk memastikan mana yang salah cetak. Bagian mana yang ingin kamu lihat dulu, Kisaragi-kun?"
            yutaka "Bagian selisih tabel yang kaucoret di tengah itu. Kenapa di bukunya malah kelihatan rata?"
            harumi "Untung kamu langsung menunjuk intinya—aku sering mulai menjelaskan terlalu jauh dari definisi awal kalau tidak ditanya spesifik."
            nar "Ia menunjuk dua kolom angka di kertasnya dengan ujung belakang pensil."
            harumi "Di kolom ketiga, penulisnya membuang angka di belakang koma sebelum mengalikannya ke baris bawah. Untuk contoh singkat mungkin kelihatan sepele, tapi kalau dipakai membaca tren jangka panjang, arah grafiknya langsung melenceng jauh."
            yutaka "Oh... berarti kalau cuma menghafal hasil akhirnya tanpa mengecek langkah tengahnya, pasti ikut salah semua."
            nar "Harumi mengedip pelan, seolah sedikit terkejut kau menangkap celah praktisnya secepat itu."
            harumi "...Benar. Kau menangkap polanya lebih cepat daripada dugaanku, Kisaragi-kun. Kalau mau duduk dan lihat bagian selanjutnya, silakan."

    # --- Pilihan C (Host Yutaka) ---
        else:
            nar "Kau melirik sekilas lembaran hitungan yang tersusun begitu rapi di depannya, lalu memutuskan tidak memotong konsentrasinya siang ini. Kau mengangkat satu tangan singkat sebagai isyarat sopan."
            yutaka "Makasih, Kujo-san. Aku cuma lewat mau cari buku di rak belakang saja—nggak usah terganggu."
            nar "Harumi menatapmu satu detik lebih lama, seolah benar-benar memeriksa apakah kau sedang butuh petunjuk atau memang berniat lewat saja."
            harumi "Baiklah. Kalau kamu mencari buku pengantar statistik atau referensi umum, letaknya di lorong kedua sebelah kanan."
            yutaka "Siap. Duluan ya."
            nar "Kau melanjutkan langkah menyusuri deretan rak tinggi. Beberapa menit kemudian saat kau melirik balik dari ujung lorong, Harumi sudah kembali menunduk menahan halaman bukunya dengan satu jari, sementara kursi kosong di sebelahnya tetap tidak tersentuh—kesempatan obrolan yang jelas tidak akan ia panggil ulang dengan suara keras di ruang baca."
```

## 2. `S01` — *Papan Shogi di Taman* (`game/kk_spring.rpy`, blok `else:`)
```renpy
    # --- Pembukaan (Host Yutaka) ---
    else:
        nar "Agak menjauh dari area rumput tengah yang dipenuhi terpal piknik Hanami, sisi barat Taman Kampus jauh lebih teduh dan sepi. Kau melangkah santai menyusuri jalan setapak batu dengan kedua tangan terselip di saku jaket, menikmati angin April yang menggugurkan kelopak sakura."
        nar "Bunyi 'klak' yang jernih dan mantap dari kayu yang beradu membuat langkahmu melambat di dekat sebuah meja batu di bawah pohon sakura tua."
        nar "Di bangku batu itu duduk seorang mahasiswi yang bahkan di tengah acara piknik kampus pun tampak seperti berada di ruangnya sendiri. Rambut putih keperakannya ditata rapi dengan bagian atas menyilang bervolume dan gelombang panjang yang jatuh anggun melewati bahu, berpadu dengan busana semi-formal yang tampak mahal namun tidak mencolok."
        nar "Saionji Shiori—nama yang beberapa kali kaudengar disebut mahasiswa di fakultas yang sama dengan julukan Ratu Fakultas. Meski satu angkatan, pemilik tubuh ini belum pernah berbicara dengannya, dan kau sendiri tidak tahu banyak soal dirinya."
        nar "Di hadapannya terbentang sebuah papan shogi kayu lipat. Dengan jari-jari rampingnya, Shiori menggerakkan satu bidak ke petak tengah, menatap susunan itu beberapa detik, lalu dengan tenang memutar seluruh papan seratus delapan puluh derajat untuk membaca posisi dari sudut pandang lawan."
        nar "Tepat ketika ia hendak mengangkat bidak berikutnya, sehelai kelopak sakura melayang turun dan jatuh di antara dua garis petak. Shiori menjepit kelopak merah muda itu dengan dua jari lalu meletakkannya rapi di pinggir meja batu, seolah benda itu tamu yang salah memilih kursi."
        nar "Tanpa tergesa sedikit pun, mata ungu amethyst-nya naik menatapmu dengan senyum tipis yang ramah, sopan, namun terasa seperti sedang menakar seberapa cepat kau bereaksi."
        shiori "Selamat siang, Kisaragi-san. Kalau kamu ingin duduk di bangku ini, silakan saja—tempatnya masih luas."
        nar "Kau sempat mengerjap pelan mendengar ia langsung menyebut nama keluargamu padahal kalian belum pernah bertegur sapa. Senyum percaya dirinya tetap terpasang tenang."
        shiori "Dan kalau kamu hendak bertanya mengapa ada orang bermain shogi sendirian di tengah Hanami, jawabannya cukup sederhana: karena belum ada yang duduk di seberang."

    # --- Pilihan A (Host Yutaka) ---
        else:
            nar "Kau mengeluarkan kedua tangan dari saku jaket, tersenyum tipis menerima sapaan yang terdengar seperti pancingan halus itu, lalu melangkah maju dan duduk tepat di seberang papan shogi."
            yutaka "Kalau memang belum ada lawan, boleh saja aku coba mengisi kursi di seberang, Saionji-san."
            nar "Alis perak Shiori terangkat halus sepersekian milimeter. Senyum sopannya tidak berubah lebar, tetapi kilatan di mata ungu amethyst-nya langsung terasa lebih tajam."
            shiori "Menarik. Kalau begitu, sisi papan di depanmu itu milikmu, Kisaragi-san."
            nar "Ia memberimu beberapa detik memeriksa posisi bidak yang sedang berlangsung, lalu dengan gerakan tangan yang terlatih dan tenang, ia mulai mengembalikan seluruh bidak kayu itu ke susunan awal."
            yutaka "Direset dari awal?"
            shiori "Tentu. Tidak adil kalau aku menyimpan keuntungan dari rencana yang sudah kubangun sendirian sebelum kamu duduk. Permainan yang sepadan harus dimulai dari garis yang sama."
            nar "Bidak terakhir mendarat dengan bunyi kayu yang jernih. Shiori menautkan jari-jarinya di tepi meja batu dan memberi isyarat ringan."
            shiori "Silakan melangkah lebih dulu, Kisaragi-san."
            nar "Alih-alih membuka jalur pion standar di sisi kanan yang biasa dipakai pemula, kau menggerakkan pion pinggir yang jarang disentuh di awal hanya untuk melihat bagaimana ia merespons. Tangan Shiori sempat berhenti setengah detik sebelum membalas—'klak'."
            shiori "Oh... pembukaan yang cukup tidak terduga. Kamu sengaja menguji apakah aku bermain berdasarkan hafalan buku?"
            yutaka "Cuma penasaran saja bagaimana Ratu Fakultas menanggapi langkah yang agak berantakan."
            nar "Tawa kecil yang sangat halus lolos dari bibir Shiori. Caranya menerima tantanganmu dengan kesungguhan penuh membuatmu langsung sadar bahwa sore ini tidak akan berakhir sekadar sebagai perkenalan singkat."

    # --- Pilihan B (Host Yutaka) ---
        else:
            nar "Kau memilih tidak langsung menantangnya. Kau berhenti di sisi meja batu dengan sebelah tangan masih di saku jaket, menunduk memperhatikan pola gerak bidak di atas papan kayu."
            yutaka "Belum tentu aku kuat menahan tiga puluh langkah melawanmu, Saionji-san. Aku lihat saja beberapa giliran berikutnya dari sini."
            shiori "Silakan. Penonton yang benar-benar memperhatikan selalu diterima."
            nar "Ia sedikit memperlambat tempo tangannya saat memindahkan dua bidak berikutnya agar alur serangannya mudah kauikuti. Sambil menatap jalur terbuka di sisi kiri papan, matamu menangkap satu celah balasan yang tercipta tepat saat ia mendorong bidak peraknya terlalu maju."
            yutaka "Tunggu—kalau bidak itu naik ke petak barusan, bukannya jalur serong dari pojok kanan langsung jebol sampai ke belakang?"
            nar "Tangan Shiori berhenti di udara. Alih-alih langsung menyangkal atau berpura-pura sudah tahu, ia menunduk memeriksa jalur yang kau tunjuk selama beberapa detik penuh."
            shiori "...Benar. Aku terlalu sibuk membela rencanaku sendiri sampai mengabaikan celah balasan dari sisi itu."
            nar "Ia menggeser mundur bidaknya sedikit, lalu mendongak menatapmu dengan senyum tipis yang kali ini terasa jauh lebih jujur daripada senyum sopannya di awal."
            shiori "Matamu cukup jeli, Kisaragi-san. Kalau belum terburu-buru, mau duduk sebentar dan melihat kemungkinan langkah berikutnya bersama?"
            yutaka "Boleh juga, mumpung masih santai."
            nar "Kau duduk di sisi bangku batu, dan Shiori memiringkan papan kayu itu sedikit ke arahmu agar kalian bisa membedah dua variasi balasan di atas papan yang sama."

    # --- Pilihan C (Host Yutaka) ---
        else:
            nar "Kau mengangguk sopan tanpa berniat mengganggu ketenangan sudut taman itu."
            yutaka "Makasih tawarannya, Saionji-san. Aku cuma lewat cari angin sebentar—lanjutkan saja permainanmu."
            shiori "Baiklah. Selamat menikmati Hanami-nya, Kisaragi-san."
            nar "Shiori mengangguk anggun tanpa sedikit pun raut kecewa. Begitu kau berbalik dan melangkah menjauh menyusuri jalan setapak, bunyi 'klak' bidak kayu kembali terdengar mantap di belakangmu—menegaskan bahwa ia punya kesenangan sendiri yang tetap berlangsung utuh tanpa perlu penonton."
```

## 3. `Mi01` — *Bento Hanami* (`game/kk_scenes.rpy`, blok `else:`)
```renpy
    # --- Pembukaan (Host Yutaka) ---
    else:
        nar "Di bawah pohon sakura besar di sisi tengah Taman Kampus, aroma gurih telur dadar gulung hangat, ayam goreng renyah, dan kaldu rebusan menyeruak di antara bau rumput siang."
        nar "Di atas selembar alas duduk yang terhampar rapi, Tachibana Miyuki—senior tahun ketiga yang wajahnya kaukenal dari lingkar pertemanan Koita—tengah berlutut anggun membuka ikatan kain furoshiki krem yang membungkus sebuah kotak bento kayu bertingkat tiga."
        nar "Rambut hitam panjangnya yang lurus dan terurai tanpa hiasan bergoyang pelan ditiup angin. Tepat sebelum ia mengangkat tutup tingkat teratas, sehelai kelopak sakura mendarat pas di tengah tutup kotak itu."
        nar "Miyuki menatap kelopak kecil itu, memajukan bibir sedikit, lalu meniupnya pergi dengan raut wajah luar biasa serius seolah sedang menjalankan tugas penting."
        "Mahasiswi di Sebelah" "Pfft—Tachibana-senpai serius banget sih cuma buat niup satu kelopak sakura!"
        nar "Tawa kecil dari mahasiswi di sebelah alasnya membuat Miyuki mengerjap kaget, lalu baru setelah kelopak itu melayang jatuh ke rumput, senyum lembut dan sedikit malu-malu ikut mengembang di wajahnya."
        nar "Saat mata biru sapphire-nya menoleh ke tepi jalan setapak dan menangkap sosokmu yang lewat, ia segera melambai lembut."
        miyuki "Ara, Yutaka-kun? Kebetulan sekali kamu lewat sini. Senpai lagi-lagi memasak terlalu banyak—kalimat itu mulai terdengar seperti kebiasaan buruk, ya. Kalau kamu belum makan siang, silakan duduk dan ikut makan."
        nar "Mendengar panggilan hangat 'Yutaka-kun' itu sempat membuatmu terdiam sepersekian detik—terasa begitu akrab dan tulus, meski jauh di dalam kepala kau tetap sadar bahwa kelembutan itu ditujukan kepada pemuda pemilik asli tubuh ini."
        nar "Kau melangkah mendekat dan melihat isi kotak bento bertingkat tiga yang baru ia buka satu per satu: potongan tamagoyaki keemasan, karaage, bola nasi onigiri berbalut nori, sayur rebus warna-warni, serta sekat kecil berisi lauk berbumbu merah. Bahkan di sampingnya sudah tertata rapi beberapa pasang sumpit cadangan, piring kertas, dan tisu basah sebelum ia tahu siapa saja yang akan duduk."
        miyuki "Yang agak pedas Senpai pisahkan di pojok kanan sini ya, Yutaka-kun. Jangan sampai Senpai merusak suasana Hanami-mu gara-gara salah ambil sambal."

    # --- Pilihan A (Host Yutaka) ---
        else:
            nar "Kau melepas sepatu di tepi rumput, duduk bersila di pinggir alas, lalu menerima piring kertas dan sumpit yang disodorkan Miyuki. Kau mengambil sepotong tamagoyaki serta sayur rebus dari tingkat teratas dan langsung mencicipinya."
            nar "Lapisan telurnya tetap lembut dan berair kaldu meski sudah dibawa keluar ruangan, sementara bumbunya pas tanpa rasa manis yang berlebihan."
            yutaka "Tachibana-senpai, tamagoyaki sama sayur rebus ini beneran enak. Teksturnya masih lembut dan bumbunya pas—kelihatan sekali bukan masakan buru-buru."
            nar "Miyuki mengerjap mendengar pujianmu yang blak-blakan namun spesifik itu. Ia sedikit mencondongkan tubuhnya sambil menatapmu dengan mata biru sapphire yang ingin memastikan."
            miyuki "Ara... benarkah? Kamu tidak sedang bilang begitu cuma buat bersikap sopan sama Senpai, kan, Yutaka-kun?"
            yutaka "Kalau nggak enak ya nggak bakal kupuji sedetail itu, Senpai. Serius, ini enak banget."
            nar "Senyum anggun yang biasa ia pasang perlahan luruh menjadi tawa kecil yang jauh lebih ringan dan tulus."
            miyuki "Syukurlah... padahal bagian itu yang paling lama kubuat subuh tadi sampai hampir salah takar kaldu. Senpai senang kamu menyadarinya."
            nar "Dengan wajah berbinar, ia langsung menyumpitkan beberapa potong karaage dan tamagoyaki tambahan ke piring kertasmu."
            yutaka "Sebentar, Tachibana-senpai—piringmu sendiri dari tadi masih kosong, lho. Jangan kasih semuanya ke orang lain."
            nar "Gerakan sumpit Miyuki terhenti di udara. Ia menunduk melihat piring kertas bersih di depan lututnya sendiri, lalu mengedip kikuk sebelum tertawa lepas."
            miyuki "Ara... benar juga, ya. Senpai terlalu asyik membagi sampai lupa makan sendiri."
            nar "Saat ia akhirnya menyumpit sepotong tamagoyaki ke piringnya sendiri di bawah guguran kelopak sakura, senyumnya tampak jauh lebih santai dan lebih muda daripada citra senior serba sempurna yang biasa ia tampilkan."

    # --- Pilihan B (Host Yutaka) ---
        else:
            nar "Ketika dua mahasiswa lain mulai merapat ke dekat pohon dan Miyuki hendak mengangkat tumpukan kotak bento bertingkat tiga itu untuk dipindahkan ke bagian alas yang lebih teduh dan rata, kau langsung melihat pergelangan tangannya sedikit menegang menahan beban kotak kayu penuh tersebut."
            nar "Tanpa banyak basa-basi, kau berjongkok di sampingnya dan langsung menyangga dua tingkat terbawah dengan kedua tanganmu."
            yutaka "Biar aku yang angkat bagian bawahnya, Tachibana-senpai. Berat banget itu kalau diangkat sendirian."
            nar "Bibir Miyuki refleks terbuka seolah hendak menolak secara otomatis."
            miyuki "Eh, tidak usah repot-repot, Yutaka-kun, Senpai bisa sendiri kok—"
            yutaka "Pergelangan tangan Senpai sudah mulai merah dari tadi. Kalau dipaksakan nanti malah tumpah semua. Sini, pegang tingkat atasnya saja."
            nar "Mendengar nada lugasmu, Miyuki terdiam sepersekian detik, menimbang berat kotak kayu di tangannya sendiri, lalu menghela napas kecil yang lembut dan menyerahkan bagian bawah itu kepadamu."
            miyuki "Ara... kalah argumen, ya. Terima kasih banyak, Yutaka-kun. Aku selalu yakin sanggup membawa semuanya sendiri sampai baru sadar tanganku sudah terlanjur pegal."
            nar "Kalian berdua memindahkan kotak-kotak itu ke tengah alas yang rata di bawah bayangan dahan sakura, lalu kau ikut membagikan piring kertas dan gelas minuman kepada mahasiswa di pinggir supaya Miyuki tidak harus sibuk sendirian mengawasi semua orang."
            yutaka "Beres. Sekarang giliran Tachibana-senpai duduk dan makan sebelum makanannya dingin kena angin."
            miyuki "Iya... rasanya menyenangkan juga sesekali tidak harus mengurus semuanya sendiri. Terima kasih ya, Yutaka-kun."
            nar "Dengan bahu yang tampak jauh lebih rileks, Miyuki akhirnya benar-benar mengambil sumpitnya sendiri dan menikmati satu gigitan hangat sebelum angin siang mendinginkan masakannya."

    # --- Pilihan C (Host Yutaka) ---
        else:
            nar "Kau melirik sekilas jam tangan di pergelangan kirimu, lalu mengangguk sopan tanpa ikut duduk di tepi alas pikniknya."
            yutaka "Terima kasih tawarannya, Tachibana-senpai. Tapi aku masih ada urusan lain sebentar lagi, jadi aku permisi duluan."
            nar "Miyuki mengangguk cepat dengan senyum lembut yang sudah begitu terlatih, lalu menarik sedikit ujung kain furoshiki dan menggeser kotak bento ke dalam agar jalanmu di tepi alas tetap lapang."
            miyuki "Oh, tentu saja, jangan sampai terlambat ya, Yutaka-kun. Hati-hati di jalan. Kalau nanti sempat, masih boleh mampir lagi ke sini kok."
            yutaka "Baik, Senpai. Permisi."
            nar "Kau mengangguk singkat dan melangkah menjauh menyusuri jalan setapak. Ketika sempat menoleh sekilas sebelum belokan pohon, kau melihat Miyuki menunduk sebentar memandangi kotak bento yang masih penuh itu—ada jeda sunyi sepersekian detik sebelum tangannya kembali bergerak cekatan dan senyum hangatnya terpasang siap untuk orang berikutnya."
```
