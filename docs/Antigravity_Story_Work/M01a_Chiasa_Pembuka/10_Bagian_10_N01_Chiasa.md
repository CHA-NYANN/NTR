# Bagian 10 (Revisi 1 — Alur Dialog Nyambung & Lebih Detail) — `N01` (*Tabrakan di Koridor*) · Host Chiasa

Target File: `game/kk_scenes.rpy` (`label kkscene_N01`, blok `if kk_host == "chiasa":`)

```renpy
label kkscene_N01:
    call kk_scene_enter("nagisa", "Gedung Arsitektur")
    if kk_host == "chiasa":
        nar "Sinar matahari siang menembus deretan jendela tinggi di koridor lantai satu Gedung Arsitektur. Udara di sepanjang lorong itu membawa aroma samar lem kayu, kertas kalkir, dan serbuk gergaji halus dari ruang studio maket di ujung lantai."
        nar "Kau baru saja memotong jalan lewat gedung ini dari arah Gedung Seni Rupa menuju jalur penghubung utama sambil menyampirkan tas jinjing kain di bahu. Karena koridor sedang agak lengang setelah jam kelas berganti, kau melangkah santai mendekati tikungan dekat papan pengumuman."
        nar "Namun sebelum kau sempat menginjak ubin belokan, suara langkah sepatu kets yang berjalan cepat terdengar dari sisi lain dinding—diiringi bunyi ketukan tombol yang cepat dan gugup."
        nar "Kau tidak sempat menghindar. Sudut keras sebuah map gambar besar langsung menghantam bahu kirimu."
        chiasa "Aw—!"
        nar "Kau terdorong mundur setengah langkah menahan keseimbangan. Di depanmu, seorang gadis bertubuh mungil dengan rambut pirang keemasan panjang yang diikat twin-tail ikut terhuyung ke belakang."
        nar "Tali tas selempang berhias gantungan kunci kelinci kecil di bahunya melorot ke siku. Kotak karton tipis berisi maket rumah kecil yang tadi ia jepit di bawah lengan kirinya langsung terlepas dan mendarat miring di dekat ujung sepatumu, disusul gulungan kertas gambar dan penggaris skala besi yang jatuh berdenting nyaring di lantai keramik."
        nar "Sementara itu, sebuah konsol genggam hitam yang sejak tadi ia mainkan dengan tangan kanannya ikut terlempar dari genggamannya."
        nar "Yang membuatmu melongo sepersekian detik adalah reaksinya: alih-alih menahan kotak maket atau gulungan tugas kuliahnya, Sakurajima Nagisa justru langsung menukik ke bawah dengan refleks luar biasa cepat—nyaris membenturkan satu lutut ke lantai keramik hanya demi menyambar konsol genggam itu dengan kedua tangan sebelum layarnya menyentuh lantai."
        nagisa "Dapat! Fiuh—hampir saja..."
        nar "Begitu yakin konsolnya aman tanpa goresan, barulah Nagisa mendongak dengan mata biru cerah yang langsung menyala galak—sebelum raut wajahnya sedikit tersentak saat mengenali wajahmu."
        nagisa "Hei! Kalau lewat tikungan itu lihat jalan dong—eh, Chiasa?!"
        nar "Kau mengusap bahu kirimu yang sedikit nyeri, lalu menatap Nagisa yang masih berjongkok memeluk konsolnya di tengah barang-barangnya yang berserakan."
        chiasa "Seharusnya kalimat itu aku yang bilang, Nagisa. Dari tadi kau sendiri yang jalan di tikungan sambil menunduk menatap layar game, kan?"
        nar "Wajah Nagisa langsung menegang. Ia buru-buru bangkit setengah berjongkok untuk meraih gulungan kertas gambar di dekat lututnya sambil menggerutu cepat."
        nagisa "I-iya, aku tahu aku juga salah lihat! Tapi aku tadi sudah hampir berhenti di tikungan kok, cuma kau saja yang muncul terlalu mendadak!"
        nar "Saat ia memindahkan konsol ke tangan kiri untuk memungut penggaris skala, layar konsol yang belum sempat dimatikan itu miring tepat ke arah pandanganmu. Di tengah layar yang masih menyala terang, terpampang tulisan merah besar 'YOU LOSE' disertai skor kekalahan telak."
        nar "Kau tidak bisa menahan alis yang terangkat sedikit. Nagisa langsung menyadari arah tatapanmu, dan ibu jarinya panik menekan tombol daya hingga layar itu padam seketika."
        chiasa "...Kalah lagi?"
        nar "Rona merah langsung menjalar ke pipi dan ujung telinga Nagisa. Ia mendongak dengan sorot mata kompetitif yang tersulut dalam hitungan detik."
        nagisa "Tadi itu cuma gara-gara sinyalnya jelek di dalam gedung beton begini! Lagipula aku kan mainnya sambil jalan bawa maket! Kalau kau mau komentar atau ngetawain, jangan cuma berdiri di situ—lawan aku dulu!"
    else:
        ...
    call kk_family_menu("N01", ["Angkat maketnya, lalu balas tantangannya.", "Minta maaf singkat, kau sedang buru-buru.", "Goda dia soal game yang lebih penting dari tabrakan."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Alih-alih ikut terpancing kesal, kau ikut berjongkok di lantai koridor. Kau meraih kotak karton maket yang mendarat miring dekat ujung sepatumu dengan hati-hati, mengintip ke dalam untuk memeriksa atap miniatur dari kayu balsa di dalamnya."
            chiasa "Untung jatuhnya miring kena map tadi, jadi bagian atapnya tidak ada yang patah atau lepas lemnya."
            nar "Kau menyodorkan kotak maket itu kepada Nagisa, lalu menjulurkan tangan mengambil penggaris skala besi yang tergeletak di samping dinding. Begitu tangan Nagisa menyambut kotak maket tersebut, kau menatapnya lurus dengan senyum tenang."
            chiasa "Dan soal tantanganmu barusan—boleh saja. Kapan dan di mana? Asal kalau nanti kalah lagi, kau tidak menyalahkan sinyal koridor atau meja yang goyang ya, Nagisa."
            nar "Kedua mata biru Nagisa langsung melebar, lalu raut defensif di wajahnya berubah menjadi seringai penuh semangat kompetitif yang sama sekali tidak cocok dengan orang yang semenit lalu baru saja mengomel soal tabrakan."
            nagisa "Oh, berani juga ya kau terima langsung! Jangan kira aku bakal kalah cuma gara-gara kau lihat layar barusan!"
            nar "Ia segera menyelipkan konsol ke saku jaketnya, memeluk kotak maket dengan satu tangan, lalu menyebut jadwal dengan nada yang terdengar terlalu bersemangat."
            nagisa "Hari ini aku masih ada kelas studio sampai jam empat, jadi habis itu kita ketemu di kafe dekat gerbang selatan atau ruang santai lantai dua—jam lima pas! Awas ya kalau kau kabur setelah bikin janji!"
            nar "Saat kau menyerahkan penggaris skala besi dan gulungan gambar terakhir kepadanya, Nagisa mengambil penggaris itu lalu mengacungkannya singkat ke arahmu dengan wajah serius."
            nagisa "Dan satu syarat lagi: jangan pernah sok-sokan mengalah cuma supaya aku senang atau biar cepat selesai. Kalau kau main setengah hati, itu jauh lebih menyebalkan daripada kalah beneran. Mengerti?"
            chiasa "Siapa juga yang berniat mengalah. Aku datang jam lima."
            nar "Nagisa menerima gulungan gambar terakhir dari tanganmu, menunduk sekali lagi memeriksa kotak maketnya yang masih utuh sempurna, lalu bangkit berdiri. Saat kalian sudah sama-sama berdiri di koridor, nada suaranya turun sedikit—tidak lagi melengking galak, meski wajahnya tetap membuang pandang ke samping."
            nagisa "...Makasih ya, sudah bantu mungut dan ngecek maketku. Sampai ketemu nanti sore—jangan telat!"
            nar "Ucapan terima kasih itu terdengar cukup jelas untuk ditangkap di lorong yang sepi. Ia memeluk semua barangnya kembali, lalu melangkah cepat menjauh dengan twin-tail pirangnya yang terayun-ayun penuh energi."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kau melirik sekilas jam di layar ponselmu, lalu memutuskan tidak meladeni tantangan game-nya. Kau berjongkok singkat, memungut kotak maket dan penggaris skala besi yang jatuh paling dekat dengan kakimu, lalu menyodorkannya langsung ke tangan Nagisa sambil berdiri kembali."
            chiasa "Maaf ya, Nagisa, tadi aku juga jalan terlalu cepat di belokan. Aku nggak sempat bahas soal game sekarang—pengarahan studio di sayap barat mulai sepuluh menit lagi, jadi aku harus buru-buru."
            nar "Mulut Nagisa yang sudah sempat terbuka hendak menyambung omelan dan tantangan tadi mendadak terkatup rapat. Ia menatap raut wajahmu yang memang benar-benar tenang, datar, dan sedang terburu-buru—sama sekali tidak menunjukkan minat untuk berdebat dengannya."
            nar "Ada jeda canggung sepersekian detik di antara kalian berdua. Di dalam manga, Nagisa dan Chiasa dulunya teman masa kecil yang akrab sebelum jarak halus tumbuh di antara mereka—dan sikap dinginmu barusan jelas terasa seperti batas yang sengaja kau pasang."
            nar "Bahu Nagisa sedikit mengendur. Ia menerima kotak maket dan penggaris dari tanganmu, merapikan gulungan kertas ke pelukannya, lalu bergeser merapat ke dinding koridor agar jalur lewatmu lapang."
            nagisa "Oh... begitu. Ya sudah, kalau memang buru-buru pergi saja dulu. Jalan hati-hati di tikungan."
            nar "Ia menunduk merapikan tali tasnya yang berhias gantungan kunci kelinci, lalu menambahkan dengan gumaman pelan yang masih terdengar seperti gengsi khasnya."
            nagisa "Kalau nanti kau nabrak orang lagi di gedung ini, bilang saja desain koridor Arsitektur yang terlalu sempit."
            chiasa "Iya. Hati-hati juga di studio, Nagisa."
            nar "Kau mengangguk singkat lalu melangkah melewati tikungan. Namun beberapa langkah kemudian, ketika kau sempat menoleh sekilas sebelum keluar dari lorong, kau melihat Nagisa belum juga beranjak—ia justru membungkuk lagi memeriksa lantai keramik di bekas tempatmu berdiri tadi, seolah ingin memastikan tidak ada catatan, pena, atau barang kecil milikmu yang ikut terjatuh dan tertinggal."
    else:
        if kk_host == "chiasa":
            nar "Kau ikut berjongkok untuk memungut gulungan gambar yang menggelinding paling jauh dekat dinding serta meletakkan kotak maketnya di atas map plastik agar tidak kotor. Namun sebelum menyerahkan gulungan terakhir itu, kau melirik konsol genggam hitam di pelukan Nagisa, lalu menatap wajahnya dengan senyum miring penuh godaan."
            chiasa "Jujur saja, refleksmu barusan keren sekali lho, Nagisa. Gulungan tugas gambar dan kotak maketmu dibiarkan jatuh berantakan ke lantai, tapi konsolnya langsung disambar dengan dua tangan sebelum sempat menyentuh keramik. Rupanya di Fakultas Arsitektur, game jauh lebih penting daripada tabrakan dan tugas kuliah, ya?"
            nar "Seketika rona merah padam langsung naik dari leher hingga ke pipi Nagisa. Ia refleks mendekap konsol yang layarnya sudah gelap itu erat-erat ke dadanya dengan kedua tangan, matanya melebar panik."
            nagisa "B-bukan begitu! Jangan asal menyimpulkan dong! Yang ini kalau jatuh layarnya bisa retak, terus biaya servisnya mahal tahu nggak?!"
            chiasa "Jadi kalau maketnya yang patah tidak masalah?"
            nagisa "Bukan nggak masalah! Kalau kertas gambar sama maket kan bisa—ya, maket juga bisa rusak dan bikin aku begadang lagi sih, tapi tetap beda! Sudah, jangan tambah-tambahin argumenmu sendiri!"
            nar "Menyadari kalimat pembelaannya sendiri malah makin berantakan dan membuktikan ucapanmu, Nagisa mendengus keras. Namun alih-alih benar-benar marah, sudut bibirnya justru berkedut hingga keluar tawa pendek yang setengah kesal dan setengah malu."
            nar "Ia menyambar gulungan gambar terakhir dari tanganmu dengan gerakan cepat, lalu bangkit berdiri sambil memeluk map, kotak maket, dan konsolnya sekaligus dengan agak kikuk."
            nagisa "Menyebalkan banget sih kau hari ini, Chiasa! Pokoknya aku nggak mau tahu—kapan-kapan waktu kita ketemu lagi, kau tetap harus lawan aku satu ronde biar kau tahu rasanya kalah!"
            chiasa "Boleh saja. Asal waktu itu konsolnya jangan sampai terlempar lagi sebelum pertandingan mulai."
            nagisa "Berisik! Sudah sana, aku mau masuk studio sebelum dosennya datang!"
            nar "Ia membalikkan badan dan melangkah cepat menjauh menyusuri koridor dengan telinga yang masih memerah. Tantangan bertanding yang tadinya ia lontarkan demi menjaga gengsi kini terdengar jauh lebih mirip alasan untuk bertemu lagi."
```
