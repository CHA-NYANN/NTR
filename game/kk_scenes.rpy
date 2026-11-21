# Kouseikan — adegan naratif untuk event yang benar-benar dimainkan (vertical slice).
# Rangkuman cerita yang mengalir + pilihan yang muncul dari adegan, BUKAN poin desain
# atau menu nada abstrak. Pilihan tidak mengungkap ke mana arahnya.
#
# Event lain (yang hanya muncul di Alat Uji) tetap pakai pemutar generik kk_event.

# Dispatcher: pakai adegan tulisan tangan bila ada; kalau tidak, pemutar generik ringkas.
label kk_play_scene(evid):
    if kk_done(evid):
        return
    if renpy.has_label("kkscene_" + evid):
        call expression ("kkscene_" + evid)
    else:
        call kk_event(evid, reveal=False)
    return

# ── N01 · Tabrakan di Koridor (Nagisa, Gedung Arsitektur) ──
# ┌─ PANDUAN CERITA · N01 · Tabrakan di Koridor
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : tumbukan di fakultas arsitektur; ia menantang main game.
# │ INTI    : A terima / B tolak / C goda.
# │ AKHIRAN : A membuka rivalitas ringan. (Female: risiko "Nacchan-oneechan".)
# └─ tulis / perbaiki dialog di bawah ──
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
        chiasa "Seharusnya kalimat itu aku yang bilang, Nagisa-senpai. Dari tadi kau sendiri yang jalan di tikungan sambil menunduk menatap layar game, kan?"
        nar "Wajah Nagisa langsung menegang. Ia buru-buru bangkit setengah berjongkok untuk meraih gulungan kertas gambar di dekat lututnya sambil menggerutu cepat."
        nagisa "I-iya, aku tahu aku juga salah lihat! Tapi aku tadi sudah hampir berhenti di tikungan kok, cuma kau saja yang muncul terlalu mendadak!"
        nar "Saat ia memindahkan konsol ke tangan kiri untuk memungut penggaris skala, layar konsol yang belum sempat dimatikan itu miring tepat ke arah pandanganmu. Di tengah layar yang masih menyala terang, terpampang tulisan merah besar 'YOU LOSE' disertai skor kekalahan telak."
        nar "Kau tidak bisa menahan alis yang terangkat sedikit. Nagisa langsung menyadari arah tatapanmu, dan ibu jarinya panik menekan tombol daya hingga layar itu padam seketika."
        chiasa "...Kalah lagi?"
        nar "Rona merah langsung menjalar ke pipi dan ujung telinga Nagisa. Ia mendongak dengan sorot mata kompetitif yang tersulut dalam hitungan detik."
        nagisa "Tadi itu cuma gara-gara sinyalnya jelek di dalam gedung beton begini! Lagipula aku kan mainnya sambil jalan bawa maket! Kalau kau mau komentar atau ngetawain, jangan cuma berdiri di situ—lawan aku dulu!"
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
    call kk_family_menu("N01", ["Angkat kotak maketnya dan terima tantangannya.", "Minta maaf singkat—kau sedang buru-buru.", "\"Wah, game lebih penting daripada tugas dan tabrakan, ya?\""])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Alih-alih ikut terpancing kesal, kau ikut berjongkok di lantai koridor. Kau meraih kotak karton maket yang mendarat miring dekat ujung sepatumu dengan hati-hati, mengintip ke dalam untuk memeriksa atap miniatur dari kayu balsa di dalamnya."
            chiasa "Untung jatuhnya miring kena map tadi, jadi bagian atapnya tidak ada yang patah atau lepas lemnya."
            nar "Kau menyodorkan kotak maket itu kepada Nagisa, lalu menjulurkan tangan mengambil penggaris skala besi yang tergeletak di samping dinding. Begitu tangan Nagisa menyambut kotak maket tersebut, kau menatapnya lurus dengan senyum tenang."
            chiasa "Dan soal tantanganmu barusan—boleh saja. Kapan dan di mana? Asal kalau nanti kalah lagi, kau tidak menyalahkan sinyal koridor atau meja yang goyang ya, Nagisa-senpai."
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
        else:
            nar "Kau ikut berjongkok di lantai koridor. Kau meraih kotak karton maket yang mendarat miring dekat ujung sepatumu dengan hati-hati, mengintip ke dalam untuk memastikan atap miniatur dari kayu balsa itu tidak ada yang patah."
            yutaka "Tenang, jatuhnya ketahan map tadi. Atapnya masih utuh semua."
            nar "Kau menyodorkan kotak maket itu kepada Nagisa, lalu meraih penggaris skala besi di samping dinding. Dalam hati kau langsung teringat satu masalah kecil: Yutaka yang asli terkenal jago main game, sedangkan kau sama sekali tidak mewarisi refleks jarinya—tapi justru terasa menarik melihat seberapa jauh kau bisa meladeni sahabat masa kecilnya ini."
            yutaka "Boleh saja kalau mau tanding, Nagisa. Kapan dan di mana? Tapi kalau nanti aku agak berkarat atau kau yang kalah lagi, jangan salahkan sinyal koridor ya."
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
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kau melirik sekilas jam di layar ponselmu, lalu memutuskan tidak meladeni tantangan game-nya. Kau berjongkok singkat, memungut kotak maket dan penggaris skala besi yang jatuh paling dekat dengan kakimu, lalu menyodorkannya langsung ke tangan Nagisa sambil berdiri kembali."
            chiasa "Maaf ya, Nagisa-senpai, tadi aku juga jalan terlalu cepat di belokan. Aku nggak sempat bahas soal game sekarang—pengarahan studio di sayap barat mulai sepuluh menit lagi, jadi aku harus buru-buru."
            nar "Mulut Nagisa yang sudah sempat terbuka hendak menyambung omelan dan tantangan tadi mendadak terkatup rapat. Ia menatap raut wajahmu yang memang benar-benar tenang, datar, dan sedang terburu-buru—sama sekali tidak menunjukkan minat untuk berdebat dengannya."
            nar "Ada jeda canggung sepersekian detik di antara kalian berdua. Dari foto masa kecil dan cara Nagisa berbicara, kau bisa merasakan bahwa mereka dulu pernah cukup akrab sebelum jarak halus tumbuh di antara keduanya—dan sikap dinginmu barusan jelas terasa seperti batas yang sengaja kau pasang."
            nar "Bahu Nagisa sedikit mengendur. Ia menerima kotak maket dan penggaris dari tanganmu, merapikan gulungan kertas ke pelukannya, lalu bergeser merapat ke dinding koridor agar jalur lewatmu lapang."
            nagisa "Oh... begitu. Ya sudah, kalau memang buru-buru pergi saja dulu. Jalan hati-hati di tikungan."
            nar "Ia menunduk merapikan tali tasnya yang berhias gantungan kunci kelinci, lalu menambahkan dengan gumaman pelan yang masih terdengar seperti gengsi khasnya."
            nagisa "Kalau nanti kau nabrak orang lagi di gedung ini, bilang saja desain koridor Arsitektur yang terlalu sempit."
            chiasa "Iya. Hati-hati juga di studio, Nagisa-senpai."
            nar "Kau mengangguk singkat lalu melangkah melewati tikungan. Namun beberapa langkah kemudian, ketika kau sempat menoleh sekilas sebelum keluar dari lorong, kau melihat Nagisa belum juga beranjak—ia justru membungkuk lagi memeriksa lantai keramik di bekas tempatmu berdiri tadi, seolah ingin memastikan tidak ada catatan, pena, atau barang kecil milikmu yang ikut terjatuh dan tertinggal."
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
    else:
        if kk_host == "chiasa":
            nar "Kau ikut berjongkok untuk memungut gulungan gambar yang menggelinding paling jauh dekat dinding serta meletakkan kotak maketnya di atas map plastik agar tidak kotor. Namun sebelum menyerahkan gulungan terakhir itu, kau melirik konsol genggam hitam di pelukan Nagisa, lalu menatap wajahnya dengan senyum miring penuh godaan."
            chiasa "Jujur saja, refleksmu barusan keren sekali lho, Nagisa-senpai. Gulungan tugas gambar dan kotak maketmu dibiarkan jatuh berantakan ke lantai, tapi konsolnya langsung disambar dengan dua tangan sebelum sempat menyentuh keramik. Rupanya di Fakultas Arsitektur, game jauh lebih penting daripada tabrakan dan tugas kuliah, ya?"
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
        else:
            nar "Kau ikut berjongkok memungut gulungan gambar yang menggelinding paling jauh dekat dinding dan meletakkan kotak maketnya di atas map plastik agar tidak kotor. Sambil berdiri lagi, kau melirik konsol genggam hitam di pelukan Nagisa dengan senyum jahil yang blak-blakan."
            yutaka "Gaya menukikmu barusan sudah kayak tayangan ulang turnamen esports, Nagisa. Gulungan tugas dan maket dibiarkan terbang ke mana-mana, tapi konsol langsung disambar dua tangan sebelum nyentuh lantai. Prioritas yang sangat jujur."
            nar "Seketika rona merah padam langsung naik dari leher hingga ke pipi Nagisa. Ia refleks mendekap konsol yang layarnya sudah gelap itu erat-erat ke dadanya, lalu meninju pelan bahu lenganmu dengan wajah panik."
            nagisa "B-berisik! Jangan asal menyimpulkan dong! Yang ini kalau jatuh layarnya bisa retak, terus biaya servisnya mahal tahu nggak?!"
            yutaka "Oh, jadi kalau maketnya yang patah lebih murah?"
            nagisa "Bukan begitu! Kalau kertas gambar sama maket kan bisa—ya, maket juga bisa rusak dan bikin aku begadang lagi sih, tapi tetap beda! Sudah, jangan tambah-tambahin argumenmu sendiri!"
            nar "Menyadari pembelaannya sendiri malah berantakan dan menguatkan ucapanmu, Nagisa mendengus keras. Namun alih-alih benar-benar marah, sudut bibirnya justru berkedut hingga keluar tawa pendek yang setengah kesal dan setengah malu."
            nar "Ia menyambar gulungan gambar terakhir dari tanganmu dengan gerakan cepat, lalu bangkit berdiri sambil memeluk map, kotak maket, dan konsolnya sekaligus dengan agak kikuk."
            nagisa "Menyebalkan banget sih kau hari ini, Yutaka! Pokoknya aku nggak mau tahu—nanti waktu kita ketemu lagi, kau tetap harus lawan aku satu ronde biar nggak cuma bisa ngeledek doang!"
            yutaka "Boleh. Asal waktu itu konsolnya jangan sampai terlempar lagi sebelum pertandingan mulai."
            nagisa "Berisik! Sudah sana, aku mau masuk studio sebelum dosennya datang!"
            nar "Ia membalikkan badan dan melangkah cepat menjauh menyusuri koridor dengan telinga yang masih memerah. Tantangan bertanding yang tadinya ia lontarkan demi menjaga gengsi kini terdengar jauh lebih mirip alasan untuk bertemu lagi."
    return

# ── Mi01 · Bento Hanami (Miyuki, Taman Kampus) ──
# ┌─ PANDUAN CERITA · Mi01 · Bento Hanami
# │ LOKASI  : Kampus Kouseikan · Taman Kampus
# │ TERLIBAT: (saat masuk) (+ Koita bila relevan)
# │ AWALAN  : Miyuki membawa bento besar.
# │ INTI    : A puji / B bantu bawa / C abaikan.
# │ AKHIRAN : A/B membuka akses sisi hangat.
# └─ tulis / perbaiki dialog di bawah ──
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
        miyuki "Ara, Chiasa-chan? Pas sekali kamu lewat sini. Senpai lagi-lagi memasak terlalu banyak—kalimat itu mulai terdengar seperti kebiasaan buruk, ya. Kalau kamu belum makan siang, silakan duduk dan ikut makan bersama."
        nar "Panggilan akrab 'Chiasa-chan' itu sempat membuatmu terdiam sepersekian detik—terdengar begitu hangat dan tulus, meski jauh di dalam kepala kau tetap sadar bahwa kehangatan itu sebenarnya ditujukan kepada pemilik asli tubuh ini."
        nar "Kau melangkah mendekat ke tepi alas dan melihat isi kotak bento bertingkat tiga yang baru saja ia buka satu per satu. Setiap sekatnya ditata sangat rapi agar mudah dibagi: potongan tamagoyaki berwarna keemasan, karaage, bola nasi onigiri berbalut nori, sayur rebus warna-warni, hingga sekat kecil berisi lauk berbumbu merah. Bahkan di samping kotak sudah tertata rapi beberapa pasang sumpit sekali pakai, piring kertas, dan tisu basah yang jelas ia siapkan sebelum tahu siapa saja yang akan mampir."
        miyuki "Yang agak pedas Senpai pisahkan di pojok kanan sini ya, Chiasa-chan. Jangan sampai Senpai merusak suasana Hanami pertamamu gara-gara salah ambil sambal."
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
            miyuki "Syukurlah... padahal bagian itu yang paling lama kubuat subuh tadi. Sempat hampir salah takar kaldu gara-gara masih mengantuk, lho. Senpai senang banget kamu menyadarinya, Chiasa-chan."
            nar "Dengan wajah berbinar, ia segera menyumpitkan dua potongan tambahan beserta karaage dan meletakkannya ke piring kertasmu."
            chiasa "Eh—Tachibana-senpai, piringmu sendiri masih kosong lho dari tadi."
            nar "Gerakan sumpit Miyuki terhenti di udara. Ia menunduk melihat piring kertas bersih di depan lututnya sendiri, lalu mengedip bingung sebelum tertawa kecil."
            miyuki "Ara... benar juga, ya. Senpai terlalu sibuk membagi sampai lupa mengambil bagian sendiri."
            nar "Untuk beberapa detik di bawah guguran kelopak sakura itu, saat ia akhirnya mengambil sepotong tamagoyaki ke piringnya sendiri, senyumnya tampak jauh lebih muda daripada citra senior serba sempurna yang biasa ia perlihatkan di kampus."
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
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Ketika dua mahasiswa lain mulai berdatangan di dekat pohon dan Miyuki hendak mengangkat tumpukan kotak bento bertingkat tiga itu untuk dipindahkan ke tengah alas yang lebih teduh dan rata, kau menangkap sesuatu yang luput dari orang lain: pergelangan tangan Miyuki sedikit menegang dan memerah menahan beban kotak kayu yang penuh sesak itu."
            nar "Tanpa menunggu ia kewalahan, kau langsung berjongkok di sampingnya dan menjulurkan kedua tangan menyangga bagian kotak terbawah."
            chiasa "Biar kubantu angkat bagian bawahnya, Tachibana-senpai. Kelihatannya berat sekali kalau dipindah sekaligus sendirian."
            nar "Bibir Miyuki sempat terbuka seolah hendak menolak secara otomatis—kebiasaan seseorang yang terlalu terbiasa memikul semuanya sendiri."
            miyuki "Eh, tidak usah repot-repot, Chiasa-chan, Senpai bisa—"
            chiasa "Pergelangan tangan Senpai sudah agak merah dari tadi. Kita bawa berdua saja, lebih cepat dan tidak tumpah."
            nar "Miyuki terdiam sepersekian detik, melirik pergelangan tangannya sendiri lalu menimbang berat kotak kayu di pelukannya. Akhirnya ia menghela napas kecil yang lembut dan menyerahkan tingkat terbawah ke tanganmu."
            miyuki "Ara... ketahuan, ya. Terima kasih banyak, Chiasa-chan. Aku selalu yakin sanggup membawa semuanya sendiri sampai baru sadar tanganku sudah terlanjur pegal."
            nar "Kalian berdua memindahkan kotak-kotak itu ke bagian alas yang rata di bawah bayangan dahan sakura. Begitu tutupnya dibuka kembali, kau ikut mengambil alih menata piring kertas dan membagikannya kepada dua mahasiswa yang baru duduk di pinggir agar Miyuki tidak lagi sibuk sendirian mengawasi semua orang."
            chiasa "Nah, sudah rapi. Sekarang Tachibana-senpai juga duduk dan makan dulu ya, nanti keburu dingin kena angin."
            miyuki "Iya... rasanya aneh juga ya, biasanya aku yang menyuruh orang lain makan duluan. Terima kasih sudah mengingatkan, Chiasa-chan."
            nar "Dengan bahu yang tampak jauh lebih santai, Miyuki akhirnya benar-benar mengambil sumpitnya sendiri dan menikmati satu gigitan hangat sebelum angin siang mendinginkan masakannya."
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
    else:
        if kk_host == "chiasa":
            nar "Kau melirik sekilas arah gedung di belakang taman, lalu membungkuk sopan tanpa ikut melepas sepatu atau duduk di tepi alas pikniknya."
            chiasa "Terima kasih banyak tawarannya, Tachibana-senpai. Kelihatannya enak sekali, tapi aku masih ada urusan yang harus diselesaikan sebentar lagi, jadi aku permisi duluan."
            nar "Miyuki langsung mengangguk cepat dengan senyum lembut yang tampak begitu tenang dan terlatih. Tangannya segera menarik sedikit ujung kain furoshiki dan menggeser kotak bento ke dalam agar jalur langkahmu di tepi alas tetap lapang."
            miyuki "Oh, tentu saja, jangan sampai terlambat ya, Chiasa-chan. Hati-hati di jalan. Kalau nanti urusannya cepat selesai dan masih lapar, boleh kok mampir lagi ke sini—makanannya masih banyak sekali."
            chiasa "Baik, Senpai. Terima kasih, permisi."
            nar "Kau mengangguk singkat lalu melangkah menjauh menyusuri jalan setapak yang dipenuhi kelopak sakura."
            nar "Ketika beberapa langkah kemudian kau sempat menoleh sekilas sebelum belokan pohon, kau melihat Miyuki sempat menunduk diam selama sepersekian detik memandangi tumpukan kotak bento tiga tingkat yang masih penuh itu—ada jeda sunyi yang sangat tipis di wajahnya, sebelum tangannya kembali bergerak cekatan dan senyum hangat yang sama kembali terpasang siap saat mahasiswa berikutnya melintas."
        else:
            nar "Kau melirik sekilas jam tangan di pergelangan kirimu, lalu mengangguk sopan tanpa ikut duduk di tepi alas pikniknya."
            yutaka "Terima kasih tawarannya, Tachibana-senpai. Tapi aku masih ada urusan lain sebentar lagi, jadi aku permisi duluan."
            nar "Miyuki mengangguk cepat dengan senyum lembut yang sudah begitu terlatih, lalu menarik sedikit ujung kain furoshiki dan menggeser kotak bento ke dalam agar jalanmu di tepi alas tetap lapang."
            miyuki "Oh, tentu saja, jangan sampai terlambat ya, Yutaka-kun. Hati-hati di jalan. Kalau nanti sempat, masih boleh mampir lagi ke sini kok."
            yutaka "Baik, Senpai. Permisi."
            nar "Kau mengangguk singkat dan melangkah menjauh menyusuri jalan setapak. Ketika sempat menoleh sekilas sebelum belokan pohon, kau melihat Miyuki menunduk sebentar memandangi kotak bento yang masih penuh itu—ada jeda sunyi sepersekian detik sebelum tangannya kembali bergerak cekatan dan senyum hangatnya terpasang siap untuk orang berikutnya."
    return

# ── N03 · Maket Hujan (Nagisa, Gedung Arsitektur, M03) ──
# ┌─ PANDUAN CERITA · N03 · Maket Hujan
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : maket rusak karena hujan.
# │ INTI    : A bantu semalaman / B belikan baru / C tertawakan.
# │ AKHIRAN : stage 1 (rasa terima kasih) pada A.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N03:
    call kk_scene_enter("nagisa", "Gedung Arsitektur")
    if kk_host == "chiasa":
        nar "Hujan deras sore menjelang malam mengguyur Gedung Arsitektur disertai angin kencang yang menampar kaca-kaca koridor. Lorong lantai dua sudah hampir sepi; hanya dengung lampu neon putih dan bau lembap lantai basah yang menemani langkahmu saat kau melintas hendak mencari tempat berteduh."
        nar "Tiba-tiba, suara daun pintu ruang studio yang didorong keras—lalu diikuti keheningan panjang yang terasa ganjil—membuat langkahmu terhenti. Kau melongok dari ambang pintu yang terbuka separuh."
        nar "Jendela besar di sisi kanan ruang studio rupanya lupa ditutup rapat oleh penghuni sebelumnya. Angin hujan menerobos masuk tanpa ampun, membasahi lantai dan separuh meja kerja di dekatnya—tepat di atas maket tugas besar milik Sakurajima Nagisa yang sudah ia kerjakan berminggu-minggu."
        nar "Satu sudut bangunan miniatur rumah dari kayu balsa dan karton tebal itu basah kuyup. Dinding luarnya melengkung tak beraturan, potongan tangga kecil di sisi kiri miring terlepas, dan sambungan lem dasarnya mengelupas lembek di atas genangan tipis."
        nar "Di depan meja kerja itu, Nagisa berdiri mematung dengan kedua tangan mengepal erat di sisi tubuh. Tasnya dengan gantungan kunci imut tergeletak miring di kursi belakangnya. Rahangnya mengeras kaku, twin-tail pirang keemasannya sedikit lembap oleh tempias angin, dan matanya yang biru cerah memerah tipis—tetapi ia jelas-jelas menolak menjatuhkan satu tetes air mata pun di depan siapa pun."
        if any(c["ev"] == "N01" and c["key"] == "A" for c in choices_log):
            nagisa "Kalau kau ke sini mau menagih tanding game lagi, kau harus tunggu dulu, Chiasa. Lihat sendiri maketku."
        nar "Ia menarik napas dalam-dalam yang sempat bergetar di ujungnya, lalu meraih sekotak tisu dari sudut meja dan mulai menyeka genangan air di samping papan alas dengan gerakan cepat yang dipaksakan tetap tenang."
        chiasa "Nagisa-senpai... ini—separuh sisi kanannya kena hujan semua."
        nagisa "...Tidak apa-apa. Masih bisa diselamatkan. Bagian rangkanya belum patah semua kok."
        nar "Suaranya terdengar datar dan terlalu kencang, seperti seseorang yang sedang berusaha meyakinkan dirinya sendiri agar tidak langsung ambruk."
        nagisa "Aku tinggal bongkar yang melengkung ini, potong ulang, terus lem lagi dari awal. Semalaman. Lagi."
    else:
        nar "Hujan deras sore menjelang malam menghantam kaca-kaca koridor Gedung Arsitektur disertai embusan angin kencang. Lorong lantai dua sudah hampir kosong; hanya dengung lampu neon putih dan bau lembap lantai basah yang menemani langkahmu saat kau melintas untuk mengecek apakah Nagisa masih lembur di ruang studio."
        nar "Tiba-tiba, suara daun pintu ruang studio yang didorong terbuka—lalu diikuti keheningan panjang yang terasa ganjil—membuat langkahmu berhenti. Kau melongok dari ambang pintu yang terbuka separuh."
        nar "Jendela besar di sisi kanan ruang studio rupanya lupa ditutup rapat oleh penghuni sebelumnya. Angin hujan menerobos masuk tanpa ampun, membasahi lantai dan separuh meja kerja di dekatnya—tepat di atas maket tugas besar milik Sakurajima Nagisa yang sudah ia kerjakan berminggu-minggu."
        nar "Satu sudut bangunan miniatur rumah dari kayu balsa dan karton tebal itu basah kuyup. Dinding luarnya melengkung tak beraturan, potongan tangga kecil di sisi kiri miring terlepas, dan sambungan lem dasarnya mengelupas lembek di atas genangan tipis."
        nar "Di depan meja kerja itu, Nagisa berdiri mematung dengan kedua tangan mengepal erat di sisi tubuh. Tasnya dengan gantungan kunci imut tergeletak miring di kursi belakangnya. Rahangnya mengeras kaku, twin-tail pirang keemasannya sedikit lembap terkena tempias angin, dan matanya yang biru cerah memerah tipis—tetapi ia jelas-jelas menolak menjatuhkan satu tetes air mata pun di depan siapa pun."
        if any(c["ev"] == "N01" and c["key"] == "A" for c in choices_log):
            nagisa "Kalau kau ke sini mau menagih tanding game lagi, kau harus tunggu dulu, Yutaka. Lihat sendiri maketku."
        nar "Ia menarik napas dalam-dalam yang sempat bergetar di ujungnya, lalu meraih segenggam tisu dari sudut meja dan mulai menyeka air di pinggir papan alas dengan gerakan cepat yang dipaksakan tetap datar."
        yutaka "Nagisa... parah juga. Separuh sisi kanannya kena hujan semua."
        nagisa "...Tidak apa-apa. Masih bisa diselamatkan. Rangka utamanya belum patah semua kok."
        nar "Suaranya terdengar kaku dan terlalu tegas, seperti seseorang yang sedang mati-matian menahan diri agar tidak langsung runtuh."
        nagisa "Aku tinggal bongkar yang melengkung ini, potong ulang, terus lem lagi dari awal. Semalaman. Lagi."
    call kk_family_menu("N03", ["Tutup jendelanya dan bantu memperbaiki sampai pagi.", "Tawarkan membelikan bahan maket pengganti.", "Tertawakan nasib sialnya."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau tidak banyak bertanya lagi. Kau langsung melangkah masuk, menarik daun jendela studio yang terbuka lebar sambil menahan embusan angin hujan, lalu mengunci grendelnya rapat-rapat agar tak ada lagi air yang masuk."
            nar "Setelah meletakkan tasmu di atas kursi kosong dan menggulung ujung lengan bajumu sedikit, kau berjalan ke seberang meja kerja."
            chiasa "Bagian mana yang bisa kubantu kerjakan tanpa mengganggu rancangan aslimu, Nagisa-senpai?"
            nar "Mulut Nagisa sempat terbuka hendak menolak secara otomatis—refleks gengsinya yang tidak mau terlihat lemah atau bergantung pada siapa pun. Namun ketika matanya kembali jatuh pada sudut maket yang basah dan melengkung terlalu luas untuk dikejar sendirian sebelum pengumpulan, bahunya turun sedikit."
            nagisa "...Kau nggak bakal bisa pegang bagian atap atau sambungan miringnya. Nanti malah makin berantakan kalau salah sudut."
            chiasa "Makanya kasih aku bagian yang lurus-lurus saja. Memotong karton atau membersihkan papan alas aku masih sanggup."
            nar "Nagisa menatapmu sejenak, lalu menghela napas pendek dan menggeser satu cutting mat cadangan serta penggaris besi ke hadapanmu."
            nagisa "Bagian papan dasar sama dinding lurus sisi kiri. Potongannya harus pas rata di garis pensil ini, jangan miring satu milimeter pun. Bagian atap jangan disentuh dulu, aku yang urus sendiri."
            chiasa "Siap. Kasih aku cutter cadangannya juga, Senpai."
            nar "Malam itu berlalu pelan di bawah dengung lampu neon studio dan suara hujan yang terus mengguyur atap gedung. Tidak ada musik atau obrolan panjang—hanya bunyi pisau cutter mengiris karton di atas alas potong, bau lem kayu yang tajam, dan koreksi ukuran singkat dari Nagisa setiap kali potonganmu perlu dirapikan."
            nagisa "Tunggu—yang sisi ini kelebihan setengah milimeter, Chiasa. Ampelas sedikit ujungnya biar nanti masuknya nggak maksa."
            chiasa "Oke, sebentar... begini sudah rata?"
            nagisa "Iya, pas. ...Lumayan rapi juga tanganmu."
            nar "Di pinggir meja, dua kaleng teh hangat yang sempat kau ambil dari mesin penjual otomatis lantai bawah lama dibiarkan mendingin tanpa sempat disentuh lagi. Jam demi jam bergeser hingga hujan di luar akhirnya mereda menjadi tetesan pelan dari talang."
            nar "Menjelang subuh, saat langit di balik jendela studio mulai berubah biru pucat dan dinding pengganti terakhir akhirnya menempel kokoh di tempatnya, Nagisa meletakkan pinset besinya lalu menoleh menatapmu dengan mata lelah."
            nagisa "Chiasa... tanganmu sudah merah begitu. Capek banget, ya? Sudah, taruh dulu cutternya—berhenti lima menit bareng aku. Kalau dipaksakan nanti malah kena jari."
            nar "Ia menarik kursi, bersandar sambil menggeser satu kaleng teh yang sudah dingin ke dekatmu, lalu membukanya sendiri dengan bunyi klik yang nyaring di ruangan sunyi. Setelah beberapa detik hening yang terasa nyaman, suaranya terdengar jauh lebih pelan daripada biasanya."
            nagisa "...Terima kasih ya. Aku tahu malam ini kamu bisa saja langsung pulang dan tidur enak di rumah. Aku cuma... belum tahu cara bilang terima kasih tanpa terdengar seperti sedang pidato."
            chiasa "Tidak usah pakai pidato, Senpai. Yang penting maketnya sempat berdiri lagi sebelum pagi."
            nar "Nagisa mendengus kecil—kali ini disertai senyum lelah yang tulus dan tanpa sedikit pun pertahanan—sebelum kalian berdua kembali menatap bangunan kecil yang akhirnya kembali utuh di atas meja kerja."
        else:
            nar "Kau tidak membuang waktu berbasa-basi. Kau langsung melangkah masuk, menarik daun jendela studio yang terbuka lebar melawan embusan angin hujan, lalu mengunci grendelnya rapat-rapat agar tak ada lagi air yang masuk."
            nar "Kau melempar tasmu ke kursi kosong, menggulung lengan kemejamu sampai siku, lalu berjalan ke seberang meja kerja."
            yutaka "Bagian mana yang bisa kupegang tanpa merusak rancanganmu, Nagisa?"
            nar "Nagisa refleks membuka mulut hendak mengusirmu—kebiasaan gengsinya yang paling keras kepala setiap kali merasa lemah di depan orang lain. Namun begitu pandangannya kembali jatuh ke sudut maket yang basah dan melengkung terlalu lebar untuk dikerjakan dua tangan saja dalam semalam, bahunya sedikit meluruh."
            nagisa "...Jangan sentuh bagian atap atau sambungan miringnya. Tanganmu pasti kasar, nanti malah patah semua."
            yutaka "Ya sudah, kasih aku bagian yang lurus-lurus saja. Potong karton sama bersihin papan dasar masih sanggup lah."
            nar "Ia menatapmu sejenak, menghela napas pendek, lalu menggeser satu cutting mat cadangan, penggaris besi, dan cutter ke depanmu."
            nagisa "Bagian papan dasar sama dinding lurus sisi kiri. Potongannya harus pas rata di garis pensil ini, jangan miring satu milimeter pun. Atap jangan disentuh dulu, aku yang urus sendiri."
            yutaka "Beres. Mulai sekarang saja biar keburu."
            nar "Malam merambat pelan di bawah dengung lampu neon studio dan derai hujan di luar kaca. Tidak ada candaan panjang seperti biasa—hanya suara pisau cutter mengiris karton tebal, bau lem kayu yang menyengat, dan teguran pendek dari Nagisa setiap kali potonganmu perlu dirapikan."
            nagisa "Heh, Yutaka—ujung yang ini miring setengah milimeter. Ratakan lagi pakai ampelas sebelum dilem."
            yutaka "Iya, iya, bawel amat... begini sudah lurus?"
            nagisa "Nah, pas. ...Ternyata kau bisa teliti juga kalau nggak lagi males."
            nar "Di pinggir meja, dua kaleng kopi hangat yang sempat kaubeli dari mesin penjual di lantai bawah lama dibiarkan dingin tanpa tersentuh lagi. Jam demi jam bergeser hingga hujan di luar mereda menjadi tetesan pelan dari talang."
            nar "Menjelang pagi, saat langit di balik jendela mulai berubah biru pucat dan dinding pengganti terakhir akhirnya berdiri kokoh di tempatnya, Nagisa meletakkan pinset besinya lalu menoleh menatapmu dengan mata lelah."
            nagisa "Yutaka... tanganmu sudah merah begitu. Capek banget, ya? Sudah, taruh dulu cutternya. Berhenti lima menit bareng aku sebelum jarimu kena pisau."
            nar "Ia menarik kursi, bersandar di sampingmu sambil menggeser satu kaleng kopi yang sudah dingin ke dekatmu lalu membuka kalengnya sendiri dengan bunyi klik nyaring. Setelah beberapa detik hening yang nyaman, suaranya terdengar jauh lebih pelan daripada biasanya."
            nagisa "...Terima kasih ya. Aku tahu malam ini kamu bisa saja langsung pulang ke apartemen dan tidur nyenyak. Aku cuma... nggak tahu cara bilang terima kasih tanpa terdengar kayak lagi pidato."
            yutaka "Nggak usah pidato segala. Yang penting maketmu selamat sebelum jam pengumpulan."
            nar "Nagisa mendengus kecil disertai senyum lelah yang jujur—tanpa sedikit pun tembok gengsi yang biasa ia pasang—sebelum kalian berdua kembali menatap bangunan miniatur yang akhirnya utuh lagi di atas meja."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kau melangkah masuk menutup dan mengunci jendela studio lebih dulu agar angin hujan berhenti masuk, lalu melirik tumpukan lembaran kayu balsa dan karton cadangan di samping meja yang jelas tinggal beberapa potongan kecil."
            chiasa "Bahan cadanganmu nggak bakal cukup buat mengganti seluruh sisi yang basah, Nagisa-senpai. Toko alat seni di dekat stasiun masih buka satu jam lagi—biar kubelikan papan balsa sama karton baru yang dibutuhkan sekarang."
            nar "Seketika alis Nagisa menukik tajam. Ia mendongak dengan wajah tegang, tersinggung seolah kau baru saja mencoba menyelesaikan seluruh kerja kerasnya dengan uang begitu saja."
            nagisa "Hah?! Jangan seenaknya—aku nggak butuh dikasihani! Ini tugas kuliahku, aku bisa beli sendiri!"
            chiasa "Bukan kasihan, Senpai. Coba lihat jam sekarang—kalau kamu sendiri yang lari ke stasiun di tengah hujan deras begini, waktumu bakal habis di jalan hampir satu jam."
            nar "Kau berdiri tenang di seberang meja tanpa meninggikan suara sedikit pun."
            chiasa "Aku nggak bisa mengerjakan rancangan atapmu, tapi aku bisa bantu beli bahannya sekarang supaya kamu bisa langsung fokus membongkar bagian yang rusak dan membersihkan papan dasarnya. Itu saja."
            nar "Nagisa terdiam dua detik penuh, menatap wajahmu yang datar dan praktis tanpa sedikit pun nada merendahkan. Perlahan, ketegangan di bahunya surut saat ia menyadari kau sama sekali tidak sedang mencoba membeli keberhasilannya."
            nagisa "...Tch. Ya sudah, memang benar waktuku nggak cukup kalau bolak-balik sendiri."
            nar "Ia merobek selembar kertas dari buku sketsanya, lalu menuliskan daftar bahan dengan huruf yang cepat, tegas, dan rapi."
            nagisa "Kalau begitu, beli jenis dan ketebalan yang persis sama dengan yang kutulis di sini. Jangan beli yang lebih mahal cuma karena kasihan. Ini proyek kuliah, bukan sumbangan."
            chiasa "Paham. Aku bakal cari yang persis sama."
            nar "Ia menyodorkan kertas catatan itu kepadamu, ujung telinganya sedikit memerah karena gengsi yang masih tersisa."
            nagisa "Nanti struknya simpan, bakal kuganti semua begitu selesai. ...Hati-hati di jalan, hujannya masih deras. Makasih ya, Chiasa."
            nar "Menerima bantuan jelas masih membuatnya canggung, tetapi malam itu ia tidak lagi memandang tawaranmu sebagai ancaman bagi harga dirinya—melainkan sekadar bantuan praktis dari seseorang yang menghormati pekerjaannya."
        else:
            nar "Kau melangkah masuk, menutup dan mengunci jendela studio lebih dulu agar angin hujan berhenti masuk, lalu melirik tumpukan sisa kayu balsa dan karton di sudut meja yang jelas tinggal beberapa potongan kecil."
            yutaka "Bahan cadanganmu sudah habis, Nagisa. Toko alat seni dekat stasiun masih buka sekitar sejam lagi—biar aku yang lari beli papan balsa sama karton penggantinya sekarang."
            nar "Seketika alis Nagisa menukik tajam. Ia mendongak dengan wajah tegang dan tersinggung, seolah mengira kau hendak menyelesaikan seluruh kerja kerasnya dengan dompet begitu saja."
            nagisa "Hah?! Jangan seenaknya, Yutaka—aku nggak butuh dikasihani! Ini tugasku, aku bisa beli bahanku sendiri!"
            yutaka "Siapa juga yang mengasihani? Lihat jam di dinding—kalau kamu sendiri yang bolak-balik ke stasiun di tengah badai begini, waktumu kebuang hampir sejam di jalan."
            nar "Kau menatapnya datar dan praktis tanpa sedikit pun nada bercanda ataupun merendahkan."
            yutaka "Aku nggak bisa bikin rancangan atapmu, jadi satu-satunya hal berguna yang bisa kulakukan ya lari beli bahannya sekarang supaya kamu bisa langsung fokus membongkar bagian yang basah dan membersihkan papan dasarnya. Itu saja."
            nar "Nagisa terdiam dua detik penuh, menatap wajahmu sebelum menyadari kau sama sekali tidak sedang menawarkan membeli keberhasilannya. Ketegangan di bahunya perlahan turun."
            nagisa "...Tch. Ya sudah, memang benar waktuku nggak cukup kalau jalan sendiri."
            nar "Ia merobek selembar kertas dari buku sketsanya, lalu menuliskan jenis kayu balsa, ketebalan karton, serta jumlah lembar yang persis ia butuhkan dengan tulisan cepat dan rapi."
            nagisa "Kalau begitu beli jenis dan ketebalan yang persis sama dengan yang kutulis ini. Jangan beli yang lebih mahal cuma karena kasihan. Ini proyek kuliah, bukan sumbangan."
            yutaka "Iya, ngerti. Aku cari yang persis sama."
            nar "Ia menyodorkan catatan itu kepadamu sambil sedikit memalingkan wajah, ujung telinganya memerah tipis oleh gengsi yang masih tersisa."
            nagisa "Struknya simpan, nanti kuganti semua begitu selesai. ...Hati-hati di jalan, hujannya masih deras. Makasih, Yutaka."
            nar "Menerima bantuan jelas masih membuatnya canggung, tetapi malam itu uang tidak lagi terasa seperti musuh harga dirinya—melainkan sekadar bantuan praktis dari seseorang yang menghormati pekerjaannya."
    else:
        if kk_host == "chiasa":
            nar "Melihat bangunan miniatur yang berantakan basah di depan jendela yang lupa ditutup itu—setelah segala keseriusan yang biasanya Nagisa tunjukkan—tawa pendek yang kering lolos begitu saja dari bibirmu."
            chiasa "Serius, Nagisa-senpai? Kerja berminggu-minggu hancur cuma gara-gara jendela studio lupa ditutup? Sial banget nasibmu hari ini."
            nar "Suara tawamu menggantung canggung di ruangan studio yang dingin. Seketika, seluruh kepanikan, geram, dan emosi yang tadi menahan mata Nagisa langsung padam."
            nar "Ia tidak berteriak, tidak memaki, dan tidak meledak seperti biasanya. Ia mengangkat wajah menatapmu selama dua detik penuh dengan raut wajah yang berubah menjadi sangat tenang—tenang yang dingin dan terasa asing."
            nar "Perlahan, ia meletakkan tisu basah di tangannya ke atas meja, kembali menunduk memandangi maketnya yang rusak, lalu berbicara dengan suara rendah yang datar."
            nagisa "Keluar, Chiasa. Aku nggak sedang mencari penonton untuk hari terburukku."
            chiasa "Eh, tunggu—jangan salah paham, aku cuma bercanda buat mencairkan suasana—"
            nagisa "Keluar sekarang."
            nar "Tidak ada nada tinggi, tidak ada getar emosi—hanya batas tegas yang langsung ditutup rapat. Ia sama sekali tidak kembali menyentuh maketnya ataupun menoleh kepadamu; ia hanya berdiri mematung di depan meja, menunggu sampai kakimu benar-benar melangkah mundur melewati ambang pintu."
            nar "Begitu kau mundur ke koridor yang lengang, langkah Nagisa terdengar mendekat. Daun pintu kayu studio itu ditarik dan ditutup rapat tepat di hadapanmu—mengunci ruang itu sebelum kau sempat mengubah tawa tadi menjadi gurauan yang katanya tidak bermaksud melukai."
        else:
            nar "Melihat bangunan miniatur yang berantakan basah tepat di depan jendela yang lupa dikunci itu—setelah segala keseriusan yang biasanya Nagisa tunjukkan—tawa pendek yang kering lolos begitu saja dari tenggorokanmu."
            yutaka "Serius, Nagisa? Kerja berminggu-minggu hancur cuma gara-gara jendela studio lupa ditutup? Sial banget nasibmu hari ini."
            nar "Tawamu menggantung hambar di ruangan studio yang dingin. Jika biasanya ejekan semacam itu langsung dibalas teriakan keras dan omelan panjang darinya, kali ini yang terjadi justru sebaliknya—seluruh kepanikan dan geram di mata Nagisa mendadak padam."
            nar "Ia mengangkat wajah menatapmu selama dua detik penuh dengan raut wajah yang berubah sangat tenang—tenang yang dingin dan terasa asing—lalu meletakkan tisu basah di tangannya ke atas meja dan kembali menunduk ke arah maketnya."
            nagisa "Keluar, Yutaka. Aku nggak sedang mencari penonton untuk hari terburukku."
            yutaka "Hei, tunggu—aku cuma bercanda biar suasananya nggak terlalu tegang—"
            nagisa "Keluar sekarang."
            nar "Suaranya datar tanpa sedikit pun getar emosi, menutup batas rapat-rapat. Ia tidak kembali menyentuh maketnya ataupun menoleh lagi; ia hanya berdiri mematung di depan meja, menunggu sampai kakimu benar-benar bergerak mundur melewati ambang pintu."
            nar "Begitu kau mundur ke koridor yang lengang, langkahnya terdengar mendekat dan daun pintu kayu studio itu langsung ditarik lalu ditutup rapat tepat di hadapanmu—sebelum kau sempat mengubah tawa tadi menjadi gurauan yang katanya tidak dimaksudkan melukai."
    return

# ── Mi03 · Perpustakaan Medis Malam (Miyuki, RS Tachibana, M04) ──
# ┌─ PANDUAN CERITA · Mi03 · Perpustakaan Medis Malam
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : Miyuki belajar sampai larut.
# │ INTI    : A bawakan makanan / B paksa pulang / C temani diam.
# │ AKHIRAN : stage 1 (kelelahan); sena_curiga mulai.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi03:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana")
    if kk_host == "chiasa":
        nar "Sudah lewat tengah malam. Separuh lampu neon di ruang baca perpustakaan medis Rumah Sakit Tachibana sudah dimatikan, meninggalkan deretan rak buku tinggi yang tenggelam dalam bayangan dan hanya satu lingkaran cahaya lampu meja hangat di sudut ruangan."
        nar "Di bawah cahaya lampu meja itu, Tachibana Miyuki masih duduk tegak dikelilingi tumpukan buku anatomi tebal dan lembar catatan penuh stabilo. Jas dokter putihnya masih tersampir di bahu di atas atasan ungu gelapnya, sementara rambut hitam lurus panjangnya jatuh menyentuh tepi halaman yang terbuka."
        nar "Ia begitu larut sampai sama sekali tidak menyadari langkah pelanmu menyusuri lorong rak—baru ketika bayanganmu jatuh di pinggir meja dan kau cukup dekat untuk melihat betapa pucat wajahnya serta lingkar lelah tipis di bawah mata biru sapphire-nya, ia tersentak kecil dan mendongak."
        miyuki "Ara... Chiasa-chan? Jam berapa sekarang? Ah, tidak apa-apa kok. Sedikit lagi selesai. Bab ini saja."
        if any(c["ev"] == "Mi01" and c["key"] == "B" for c in choices_log):
            miyuki "Kamu lagi, Chiasa-chan. Kotak bento waktu di halaman kampus juga kamu yang bantu bawakan, ya? Kebetulan sekali ketemu di jam begini."
        nar "Senyum lembut khas senior yang selalu menenangkan orang lain langsung terpasang di bibirnya—tetapi dari tumpukan pembatas kertas warna-warni yang sudah ia lewati dan ujung jarinya yang sedikit dingin saat menahan halaman, kelihatannya ia sudah mengucapkan kalimat 'bab ini saja' entah berapa kali malam ini."
    else:
        nar "Sudah lewat tengah malam. Separuh lampu neon di ruang baca perpustakaan medis Rumah Sakit Tachibana sudah dimatikan, meninggalkan deretan rak buku tinggi dalam bayangan dan hanya satu lingkaran cahaya lampu meja hangat di sudut ruangan."
        nar "Di bawah cahaya itu, Tachibana Miyuki masih duduk tegak dikelilingi tumpukan buku anatomi tebal dan lembar catatan penuh coretan stabilo. Jas dokter putihnya masih tersampir di bahu di atas atasan ungu gelapnya, dan rambut hitam panjangnya jatuh menyentuh tepi halaman yang terbuka."
        nar "Ia begitu tenggelam sampai sama sekali tidak menyadari langkahmu menyusuri lorong rak—baru ketika kau berhenti di tepi mejanya dan melihat sendiri betapa pucat wajahnya serta bayangan lelah tipis di bawah mata biru sapphire-nya, ia tersentak kecil dan mendongak."
        miyuki "Ara... Yutaka-kun? Tumben sekali mampir ke sini jam segini. Jam berapa sekarang? Ah, tidak apa-apa kok. Sedikit lagi. Bab ini saja."
        if any(c["ev"] == "Mi01" and c["key"] == "B" for c in choices_log):
            miyuki "Kamu lagi, Yutaka-kun. Kotak bento waktu di halaman kampus juga kamu yang bantu bawakan, ya? Kebetulan sekali ketemu di jam begini."
        nar "Senyum lembut khas senior yang selalu menenangkan orang lain langsung terpasang rapi di bibirnya—tetapi melihat tumpukan pembatas kertas yang sudah ia lewati dan ujung jarinya yang dingin menahan halaman, kelihatannya ia sudah mengucapkan 'bab ini saja' entah berapa kali malam ini."
    call kk_family_menu("Mi03", ["Bawakan sesuatu untuk ia makan, diam-diam temani.", "Tegas: tutup bukunya, suruh ia pulang.", "Duduk diam di sebelahnya tanpa bicara."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau tidak langsung mendebat atau menyuruhnya berhenti. Sebaliknya, kau mengeluarkan bungkusan kecil yang sempat kaubeli dari minimarket depan rumah sakit—sebuah onigiri terbungkus rapi yang bisa dimakan tanpa mengotori kertas, serta sebotol teh jelai hangat—lalu meletakkannya perlahan di sisi kiri meja yang kosong."
            chiasa "Tachibana-senpai belum makan malam, kan? Ini nggak bakal bikin buku anatomimu kotor. Makan dulu sedikit sebelum lanjut."
            nar "Miyuki menatap bungkusan onigiri itu, lalu mengalihkan pandangannya ke jam dinding di atas pintu ruang baca. Barulah saat itu ia tampak benar-benar menyadari sudah berapa jam berlalu sejak terakhir kali ia menyentuh makanan."
            miyuki "Ah... sudah jam setengah satu, ya. Aku tadi rencananya mau berhenti sebelum lapar. Ternyata aku melewatkan rasa laparnya juga."
            nar "Tawa kecil yang keluar dari bibirnya terdengar lelah sekaligus sedikit malu. Ia meletakkan stabilonya, menutup buku anatomi tebal di hadapannya dengan rapi, lalu membuka bungkus onigiri itu pelan."
            chiasa "Nggak usah buru-buru, Senpai. Aku temani sebentar di sini."
            miyuki "Terima kasih banyak, Chiasa-chan. Padahal biasanya aku yang cerewet mengingatkan orang lain supaya jangan telat makan... ketahuan begini jadi malu sendiri."
            nar "Kalian makan dan minum dalam keheningan yang tenang di bawah lampu meja. Beberapa menit kemudian, ketika ia akhirnya kembali membuka buku catatannya untuk merapikan halaman terakhir, ia tidak lagi memaksakan senyum segar atau berpura-pura masih bertenaga hanya agar kau tidak khawatir."
        else:
            nar "Kau tidak membuang waktu menceramahinya. Kau mengeluarkan kantong kecil dari minimarket depan rumah sakit—sebuah roti lapis terbungkus rapi yang bisa dimakan tanpa mengotori kertas dan sebotol teh hangat—lalu menaruhnya pelan di sisi meja yang kosong."
            yutaka "Tachibana-senpai belum makan malam, kan? Ini bersih kok, nggak bakal ngotorin buku anatomimu. Makan dulu sebelum lanjut."
            nar "Miyuki menatap bungkusan itu, lalu melirik jam dinding di atas pintu ruang baca. Barulah saat itu ia tampak sadar sudah berapa jam berlalu sejak terakhir kali ia makan."
            miyuki "Ah... sudah lewat tengah malam begini, ya. Aku tadi rencananya mau berhenti sebelum lapar. Ternyata aku melewatkan laparnya juga."
            nar "Ia tertawa pelan—tawa yang terdengar lelah sekaligus sedikit malu—lalu meletakkan stabilonya dan menutup buku anatomi tebal di hadapannya selama kalian makan bersama dalam sunyi."
            miyuki "Terima kasih, Yutaka-kun. Biasanya aku yang cerewet mengingatkan orang lain supaya jangan telat makan... ketahuan begini jadi malu sendiri."
            yutaka "Nggak usah dipikirin, habiskan saja dulu."
            nar "Beberapa menit kemudian, ketika ia akhirnya kembali membuka bukunya untuk merapikan halaman terakhir, ia tidak lagi berpura-pura masih segar hanya agar kau tidak khawatir."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kau menatap wajahnya yang sudah sepucat kertas buku di depannya, lalu memutuskan tidak membiarkannya memaksakan diri lagi. Kau mengulurkan tangan, meletakkan pembatas kertas di halaman yang sedang ia baca, lalu menutup buku anatomi tebal itu dengan bunyi gedebuk pelan."
            chiasa "Sudah cukup untuk malam ini, Tachibana-senpai. Sudah lewat tengah malam dan wajah Senpai pucat sekali. Ayo bereskan tas dan pulang istirahat sekarang."
            nar "Tangan Miyuki refleks bergerak menahan sampul buku itu selama sepersekian detik, seolah hendak membukanya lagi. Namun begitu melihat tatapanmu yang tidak bergeser, jari-jarinya perlahan melemas dan jatuh kembali ke permukaan meja."
            nar "Untuk sesaat ia menunduk menatap sampul buku tersebut. Ketika ia berbicara lagi, nada suaranya jauh lebih pelan daripada biasanya—tidak marah, tetapi menyisakan luka kecil yang jujur."
            miyuki "Aku tahu kamu khawatir, Chiasa-chan... terima kasih. Tapi lain kali bilang dulu ya sebelum langsung menutup bukunya."
            chiasa "Eh—maaf, Senpai, aku terlalu tiba-tiba ya?"
            miyuki "Bukan salahmu kok. Cuma... kalau ditutup mendadak begitu, aku jadi merasa seperti sedang ditegur karena belum cukup pandai menjaga diriku sendiri."
            chiasa "Bukan begitu maksudku, Senpai. Aku cuma nggak mau Senpai sampai tumbang sendirian di perpustakaan."
            nar "Miyuki menghela napas lembut dan mengangguk kecil, lalu mulai memasukkan buku-buku tebalnya ke dalam tas dengan gerakan yang lebih lambat namun teratur."
            miyuki "Iya, aku mengerti. Ayo pulang, Chiasa-chan—nanti kamu juga kemalaman kalau terlalu lama di sini."
            nar "Kalian meninggalkan ruang baca yang sunyi itu berdampingan, membawa pulang satu percakapan kecil yang agak canggung namun ternyata bisa berlangsung jujur tanpa membatalkan rasa peduli."
        else:
            nar "Kau melirik wajahnya yang sudah sepucat kertas di bawah lampu meja, lalu langsung mengulurkan tangan, menyelipkan pembatas buku di halamannya, dan menutup buku anatomi tebal itu dengan bunyi pelan yang tegas."
            yutaka "Sudah cukup, Tachibana-senpai. Sudah lewat tengah malam dan mukamu pucat sekali. Bereskan tasmu, pulang istirahat sekarang."
            nar "Tangan Miyuki refleks menahan sampul buku itu sepersekian detik, lalu perlahan melemas dan jatuh kembali ke meja. Untuk beberapa detik ia hanya menatap sampul buku tersebut dengan bahu sedikit turun."
            miyuki "Aku tahu kamu khawatir, Yutaka-kun... terima kasih. Tapi lain kali bilang dulu sebelum langsung menutupnya."
            yutaka "Maaf, terlalu mendadak ya?"
            miyuki "Bukan salahmu kok. Cuma... kalau ditutup begitu saja, aku jadi merasa seperti sedang ditegur karena belum cukup pandai menjaga diriku sendiri."
            yutaka "Bukan mau menegur, Senpai. Aku cuma nggak mau dengar kabar kau tumbang sendirian di perpustakaan."
            nar "Miyuki menghela napas pelan lalu mulai mengemasi buku dan stabilonya ke dalam tas. Kalian melangkah keluar dari perpustakaan medis yang sunyi itu berdampingan, membawa satu percakapan sulit yang ternyata bisa berlangsung jujur tanpa membatalkan kepedulian."
    else:
        if kk_host == "chiasa":
            nar "Kau tidak menceramahi ataupun menyentuh buku-bukunya. Kau menarik kursi kosong di sebelah mejanya dengan sangat pelan agar tidak menimbulkan bunyi berisik, duduk tenang, lalu mengeluarkan buku catatan kecilmu sendiri dari dalam tas."
            chiasa "Lanjutkan saja bab terakhirnya, Tachibana-senpai. Aku cuma mau duduk sebentar di sini baca catatanku sendiri, nggak usah dipikirkan."
            nar "Miyuki mengerjap agak terkejut. Selama beberapa menit berikutnya, kau bisa merasakan lirikannya dua atau tiga kali ke arahmu—seolah ia sedang memastikan bahwa kehadiranmu di sebelahnya tidak sedang menuntutnya untuk segera menjadi senior yang ramah, menghibur, atau membuatkan teh."
            nar "Ketika ia melihatmu benar-benar hanya duduk tenang membalik halaman tanpa sedikit pun menekan, ketegangan di bahunya perlahan surut. Suaranya terdengar pelan di bawah dengung pendingin ruangan—sepenuhnya tanpa nada menggoda seperti biasanya."
            miyuki "Chiasa-chan... kamu nggak harus tinggal sampai aku selesai, lho."
            chiasa "Nggak apa-apa, aku belum ngantuk juga."
            miyuki "...Kalau begitu, jangan pergi dulu, ya. Sebentar saja."
            nar "Permintaan kecil itu keluar begitu polos dan tanpa topeng. Beberapa menit kemudian, bahkan sebelum bab yang tadi ia sebut benar-benar selesai, Miyuki meletakkan penanya, menyandarkan punggungnya penuh ke sandaran kursi, dan memejamkan mata sejenak—akhirnya membiarkan dirinya terlihat lelah di sebelah seseorang yang tidak menuntut apa-apa darinya."
        else:
            nar "Kau tidak menyuruhnya berhenti ataupun menyentuh bukunya. Kau menarik kursi di sebelahnya perlahan, duduk bersandar santai, lalu mengeluarkan buku bacaanmu sendiri dari dalam tas."
            yutaka "Lanjutkan saja babmu, Tachibana-senpai. Aku cuma numpang duduk sebentar baca catatanku sendiri, nggak usah dipikirin."
            nar "Miyuki mengerjap agak terkejut. Selama beberapa menit berikutnya, ia melirik ke arahmu dua atau tiga kali, seolah memastikan kehadiranmu tidak sedang menuntutnya untuk segera bersikap ramah atau menghiburmu."
            nar "Ketika ia melihatmu benar-benar hanya duduk diam membaca tanpa sedikit pun menekan, bahunya perlahan meluruh. Suaranya terdengar pelan di ruang baca yang sunyi—sepenuhnya tanpa nada menggoda seperti biasanya."
            miyuki "Yutaka-kun... kamu nggak harus tinggal sampai aku selesai, lho."
            yutaka "Santai saja, aku juga belum ngantuk."
            miyuki "...Kalau begitu, jangan pergi dulu. Sebentar saja."
            nar "Permintaan itu keluar polos tanpa topeng. Beberapa menit kemudian, bahkan sebelum babnya selesai, ia meletakkan penanya, menyandarkan punggungnya penuh ke kursi, dan memejamkan mata sejenak—akhirnya membiarkan dirinya terlihat lelah di samping seseorang yang tidak menuntut apa pun darinya."
    return
