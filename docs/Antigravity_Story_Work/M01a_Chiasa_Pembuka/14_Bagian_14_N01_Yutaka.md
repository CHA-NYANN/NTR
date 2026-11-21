# Bagian 14 — `N01` (*Tabrakan di Koridor*) · Host Yutaka (Penutup M01a Yutaka)

Target File: `game/kk_scenes.rpy` (`label kkscene_N01`, blok `else:` untuk Host Yutaka)

```renpy
    # --- Pembukaan (Host Yutaka) ---
    else:
        nar "Sinar matahari siang masuk melalui jendela-jendela tinggi di koridor lantai satu Gedung Arsitektur. Udara di sepanjang lorong itu membawa aroma samar lem kayu, kertas kalkir, dan debu kapur dari ruang studio maket di ujung lantai."
        nar "Kau baru saja memotong jalan lewat gedung ini menuju jalur penghubung utama dengan kedua tangan terselip di saku jaket. Karena koridor sedang agak lengang di antara pergantian jam kuliah, kau berjalan santai mendekati tikungan dekat papan pengumuman."
        nar "Namun tepat sebelum kau melewati sudut dinding, suara langkah sepatu kets yang tergesa terdengar dari balik belokan—bercampur bunyi ketukan tombol yang cepat dan gugup."
        nar "Kau tidak sempat menghindar. Sudut keras sebuah map gambar besar langsung menghantam bahu kirimu."
        yutaka "Waduh—!"
        nar "Tubuhmu yang lebih tinggi hanya bergeser setengah langkah, tetapi sosok mungil yang menabrakmu justru terhuyung mundur cukup jauh. Rambut pirang keemasan panjang yang diikat twin-tail berayun keras saat ia berusaha menjaga keseimbangan."
        nar "Tali tas selempang berhias gantungan kunci kelinci kecil di bahunya melorot ke siku. Kotak karton tipis berisi maket rumah kecil yang tadi ia jepit di bawah lengan kirinya langsung terlepas dan mendarat miring di dekat ujung sepatumu, disusul gulungan kertas gambar dan penggaris skala besi yang jatuh berdenting nyaring di lantai keramik."
        nar "Pada saat yang sama, sebuah konsol genggam hitam yang sejak tadi ia mainkan di tangan kanannya ikut terlempar ke udara."
        nar "Yang membuatmu melongo sepersekian detik adalah reaksinya: alih-alih menahan kotak maket atau gulungan tugasnya, Sakurajima Nagisa justru langsung menukik ke bawah dengan refleks luar biasa cepat—nyaris membenturkan satu lutut ke keramik hanya demi menyambar konsol genggam itu dengan kedua tangan sebelum layarnya menyentuh lantai."
        nagisa "Dapat! Fiuh—hampir saja..."
        nar "Begitu yakin konsolnya selamat tanpa goresan, barulah Nagisa mendongak dengan mata biru cerah yang langsung menyala galak—sebelum raut wajahnya sedikit tersentak saat mengenali wajahmu."
        nagisa "Hei! Kalau jalan di tikungan lihat-lihat dong—eh, Yutaka?!"
        nar "Kau menggosok bahu kirimu sambil menatap sahabat masa kecil pemilik tubuh ini yang masih berjongkok memeluk konsolnya di tengah barang-barang yang berserakan."
        yutaka "Harusnya kalimat itu aku yang bilang, Nagisa. Dari tadi kau sendiri yang jalan sambil menunduk menatap layar game, kan?"
        nar "Wajah Nagisa langsung menegang. Ia buru-buru menggeser lututnya untuk meraih gulungan kertas gambar di dekat kaki sambil menggerutu cepat."
        nagisa "I-iya, aku tahu aku juga salah lihat! Tapi aku tadi sudah hampir berhenti di tikungan kok, cuma kau saja yang muncul terlalu mendadak!"
        nar "Ketika ia memindahkan konsol ke tangan kiri untuk memungut penggaris skala, layar konsol yang belum sempat dimatikan itu miring tepat ke arah pandanganmu. Di tengah layar yang masih menyala terang, terpampang tulisan merah besar 'YOU LOSE' bersama skor kekalahan telak."
        nar "Kau tidak bisa menahan alis yang terangkat sedikit. Nagisa langsung menangkap arah tatapanmu, dan ibu jarinya panik menekan tombol daya hingga layar itu padam seketika."
        yutaka "...Kalah lagi?"
        nar "Rona merah langsung naik ke pipi dan ujung telinga Nagisa. Ia mendongak dengan sorot mata kompetitif yang langsung tersulut dalam hitungan detik."
        nagisa "Tadi itu cuma gara-gara sinyalnya jelek di dalam gedung beton begini! Lagipula aku kan mainnya sambil jalan bawa maket! Kalau kau mau komentar atau ngetawain, jangan cuma berdiri sok keren di situ—lawan aku dulu!"

    # --- Pilihan A (Host Yutaka) ---
        else:
            nar "Kau ikut berjongkok di lantai koridor. Kau meraih kotak karton maket yang mendarat miring dekat ujung sepatumu dengan hati-hati, mengintip ke dalam untuk memastikan atap miniatur dari kayu balsa itu tidak ada yang patah."
            yutaka "Untung jatuhnya ketahan map tadi. Atapnya masih utuh semua."
            nar "Kau menyodorkan kotak maket itu kepada Nagisa, lalu meraih penggaris skala besi yang tergeletak di samping dinding. Dalam hati kau tahu betul bahwa kau sama sekali tidak mewarisi keahlian bermain game milik Yutaka yang asli—namun menolak tantangan Nagisa terang-terangan justru akan terasa ganjil baginya."
            yutaka "Soal tantanganmu tadi—boleh saja. Kapan dan di mana? Asal kalau nanti kalah lagi, jangan salahkan sinyal koridor ya, Nagisa."
            nar "Kedua mata biru Nagisa langsung menyala. Raut kesal di wajahnya seketika berganti seringai bersemangat yang sama sekali tidak cocok dengan orang yang baru saja mengomel soal tabrakan."
            nagisa "Nah, gitu dong! Jangan kira rekor menangmu kemarin bakal terus lanjut hari ini!"
            nar "Ia menyelipkan konsolnya ke saku jaket, memeluk kotak maket dengan satu tangan, lalu langsung menentukan waktu dengan nada tidak sabar."
            nagisa "Hari ini aku masih ada kelas studio sampai jam empat, jadi habis itu kita ketemu di ruang santai lantai dua atau kafe dekat gerbang selatan—jam lima pas! Awas ya kalau kau kabur setelah bikin janji!"
            nar "Saat kau menyerahkan penggaris skala besi kepadanya, Nagisa mengambil penggaris itu lalu menodongkannya singkat ke arahmu dengan wajah serius."
            nagisa "Dan satu lagi—jangan pernah sok-sokan mengalah cuma supaya aku senang. Aku tahu kau jago, tapi kalau kau main setengah hati, itu jauh lebih menyebalkan daripada kalah telak. Mengerti?"
            yutaka "Iya, tenang saja. Aku tidak bakal mengalah."
            nar "Kau menyerahkan gulungan gambar terakhir dari lantai. Nagisa menerimanya, menunduk memeriksa kotak maketnya sekali lagi, lalu bangkit berdiri. Begitu kalian sama-sama berdiri, nada suaranya turun sedikit—tidak lagi melengking galak, meski pandangannya tetap melengos ke samping."
            nagisa "...Makasih ya, Yutaka, sudah bantu mungut dan ngecek maketku. Sampai ketemu jam lima—jangan telat!"
            nar "Ucapan terima kasih itu terdengar cukup jelas untuk ditangkap di lorong yang sepi. Ia memeluk semua barangnya kembali lalu melangkah cepat menjauh dengan twin-tail pirangnya yang terayun-ayun."

    # --- Pilihan B (Host Yutaka) ---
        else:
            nar "Kau melirik sekilas jam tangan di pergelangan kirimu, lalu memutuskan tidak meladeni tantangan game-nya. Kau berjongkok singkat, memungut kotak maket dan penggaris skala besi yang jatuh paling dekat dengan kakimu, lalu menyerahkannya langsung ke tangan Nagisa sambil berdiri kembali."
            yutaka "Maaf ya, Nagisa, tadi aku juga jalan agak cepat di belokan. Aku nggak sempat bahas soal tanding sekarang—kelas berikutnya mulai sebentar lagi, jadi aku harus buru-buru."
            nar "Mulut Nagisa yang sudah sempat terbuka hendak menyambung omelannya mendadak terkatup rapat. Ia menatap raut wajahmu yang memang benar-benar datar dan terburu-buru—sama sekali tidak terpancing oleh tantangannya seperti biasa."
            nar "Bahu Nagisa sedikit mengendur. Ia menerima kotak maket dan penggaris dari tanganmu, merapikan gulungan gambar ke pelukannya, lalu bergeser merapat ke dinding koridor supaya jalanmu lapang."
            nagisa "Oh... begitu. Ya sudah, kalau memang buru-buru pergi saja dulu. Jalan hati-hati di tikungan."
            nar "Ia menunduk merapikan tali tasnya yang berhias gantungan kunci kelinci, lalu menambahkan dengan gumaman pelan yang masih terdengar seperti gengsi khasnya."
            nagisa "Kalau nanti kau nabrak orang lagi di sini, bilang saja koridor gedung ini yang desainnya salah."
            yutaka "Iya. Hati-hati juga, Nagisa."
            nar "Kau mengangguk singkat lalu melangkah melewati belokan. Namun beberapa langkah kemudian, ketika kau sempat menoleh sekilas dari ujung lorong, kau melihat Nagisa belum langsung beranjak—ia justru membungkuk lagi memeriksa lantai keramik di bekas tempatmu berdiri tadi, memastikan tidak ada barang atau catatan milikmu yang ikut terjatuh dan tertinggal."

    # --- Pilihan C (Host Yutaka) ---
        else:
            nar "Kau ikut berjongkok memungut gulungan gambar yang menggelinding paling jauh dekat dinding dan meletakkan kotak maketnya di atas map plastik agar tidak kotor. Namun sebelum menyerahkan gulungan terakhir itu, kau melirik konsol genggam hitam di pelukan Nagisa, lalu menatapnya dengan senyum jahil."
            yutaka "Harus kuakui, refleksmu barusan luar biasa cepat, Nagisa. Gulungan gambar dan kotak maket dibiarkan jatuh berantakan ke lantai, tapi konsolnya langsung disambar pakai dua tangan sebelum menyentuh keramik. Rupanya game jauh lebih penting daripada tabrakan dan tugas kuliah, ya?"
            nar "Seketika rona merah padam langsung naik dari leher hingga ke pipi Nagisa. Ia refleks mendekap konsol yang layarnya sudah gelap itu erat-erat ke dadanya dengan kedua tangan, matanya melebar panik."
            nagisa "B-bukan begitu! Jangan asal menyimpulkan dong! Yang ini kalau jatuh layarnya bisa retak, terus biaya servisnya mahal tahu nggak?!"
            yutaka "Jadi kalau maketnya yang patah tidak apa-apa?"
            nagisa "Bukan nggak apa-apa! Kalau kertas gambar sama maket kan bisa—ya, gambar sama maket juga bisa rusak dan bikin aku begadang lagi sih, tapi tetap beda! Sudah, jangan bantu argumenmu sendiri!"
            nar "Menyadari pembelaannya sendiri malah berantakan dan menguatkan ucapanmu, Nagisa mendengus keras. Namun alih-alih benar-benar marah, sudut bibirnya justru berkedut hingga keluar tawa pendek yang setengah kesal dan setengah malu."
            nar "Ia menyambar gulungan gambar terakhir dari tanganmu dengan gerakan cepat, lalu bangkit berdiri sambil memeluk map, kotak maket, dan konsolnya sekaligus dengan agak kikuk."
            nagisa "Menyebalkan banget sih kau hari ini, Yutaka! Pokoknya aku nggak mau tahu—nanti waktu kita ketemu lagi, kau tetap harus lawan aku satu ronde biar nggak cuma bisa ngeledek doang!"
            yutaka "Boleh. Asal waktu itu konsolnya jangan sampai terlempar lagi sebelum pertandingan mulai."
            nagisa "Berisik! Sudah sana, aku mau masuk studio sebelum dosennya datang!"
            nar "Ia membalikkan badan dan melangkah cepat menjauh menyusuri koridor dengan telinga yang masih memerah. Tantangan bertanding yang tadinya ia lontarkan demi menjaga gengsi kini terdengar jauh lebih mirip alasan untuk bertemu lagi."
```
