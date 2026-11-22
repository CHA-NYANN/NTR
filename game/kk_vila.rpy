# Mi05 "Minuman di Vila" (M05b, bulan 5, Vila Izu). Miyuki lebih terbuka saat
# menginap. Pilihan "memanfaatkan" membuat Force Route TERSEDIA sebagai kejahatan,
# ditulis sebagai KONSEKUENSI + KARAKTER saja: kerentanan korban dan sikap pemain,
# tanpa metode, tanpa adegan, tanpa cara. Force tetap non-operasional/off-screen.
# Lihat [[feedback-force-route-non-operational]].

# ┌─ PANDUAN CERITA · Mi05 · Minuman di Vila
# │ LOKASI  : Alam & Pantai · Vila (Izu)
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : Miyuki lebih terbuka.
# │ INTI    : A dengarkan / B mengantar ke kamar / C memanfaatkan.
# │ AKHIRAN : hub risiko tinggi ( Force Route tersedia sebagai kejahatan).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi05:
    call kk_scene_enter("miyuki", "Vila (Izu) · Malam")
    if kk_host == "chiasa":
        nar "Jam dinding di ruang tengah vila sudah melewati pukul sebelas malam. Lampu langit-langit sudah dimatikan sejak setengah jam lalu, hanya menyisakan lampu berdiri berkap kuning redup di sudut dekat rak televisi. Dari balik pintu kaca yang menghadap ke beranda kayu, suara debur ombak pantai Izu terdengar berulang dan tenang."
        nar "Kaleng-kaleng minuman ringan dan beberapa kaleng minuman buah beralkohol rendah bekas acara kumpul tadi masih berjajar di atas meja rendah. Teman-teman yang lain sudah pamit naik ke kamar masing-masing karena kelelahan habis bermain di pantai seharian."
        nar "Di ujung sofa panjang, Tachibana Miyuki masih duduk bersandar sambil memeluk bantal sofa persegi ke depan perutnya. Kardigan krem rumahannya agak merosot di satu bahu, dan kedua pipinya bersemu merah muda setelah ikut menghabiskan hampir dua kaleng minuman buah malam ini."
        chiasa "Tachibana-senpai belum mau naik ke kamar? Yang lain sudah pada tidur semua lho di atas."
        miyuki "Hmm... sebentar lagi, Chiasa-chan. Kalau aku langsung berdiri sekarang, rasanya lantainya agak miring sedikit."
        nar "Miyuki tertawa kecil sambil menyentuh pelipisnya dengan ujung jari. Biasanya di kampus maupun di rumah sakit ia selalu duduk dengan punggung tegak dan bicara dengan urutan yang sangat teratur, tetapi malam ini suaranya terdengar jauh lebih pelan dan santai."
        chiasa "Senpai tadi minum dua kaleng penuh sih. Padahal waktu kaleng pertama habis sudah kubilang itu ada alkoholnya sedikit."
        miyuki "Habisnya rasa buah persiknya enak banget, mirip sirup soda biasa. Lagipula tadi waktu kalian main kartu di karpet, seru banget lihatnya... aku jadi malas cepat-cepat balik ke kamar."
        nar "Ia mendorong kaleng kosong di dekat lututnya menjauh sedikit di atas meja kayu, lalu menoleh menatapmu dengan mata biru safir yang tampak sedikit sayu."
        miyuki "Eh, Chiasa-chan... besok pagi waktu sarapan, jangan ceritain ke anak-anak kalau Senpai ketiduran atau ngelantur di sofa ya. Malu tahu kalau senior paling tua di rombongan malah tumbang duluan gara-gara minuman kaleng."
        chiasa "Tenang aja, nggak bakal kuceritain ke siapa-siapa kok, Senpai."
        miyuki "Janji ya... sekali-sekali Senpai cuma pengin duduk santai begini aja, nggak usah jadi kakak yang serba rapi terus dari pagi sampai malam."
        nar "Ia menyandarkan pipinya ke tepi sandaran sofa yang empuk, memejamkan mata sebentar sambil bernapas pelan tanpa sedikit pun memasang kewaspadaan di dekatmu."
    else:
        nar "Jam dinding di ruang tengah vila sudah melewati pukul sebelas malam. Lampu utama langit-langit sudah dimatikan sejak setengah jam lalu, hanya menyisakan lampu berdiri berkap kuning redup di sudut dekat rak televisi. Dari balik pintu kaca yang menghadap ke beranda, suara ombak pantai Izu terdengar berulang di kejauhan."
        nar "Kaleng-kaleng minuman ringan dan beberapa kaleng minuman buah beralkohol rendah bekas kumpul tadi masih tersisa di meja rendah. Yang lain sudah naik ke kamar masing-masing karena kelelahan setelah seharian di pantai."
        nar "Di ujung sofa panjang, Tachibana Miyuki masih duduk bersandar sambil memeluk bantal sofa ke depan perutnya. Kardigan kremnya agak turun di satu bahu, dan kedua pipinya bersemu merah setelah ikut menghabiskan hampir dua kaleng minuman buah malam ini."
        yutaka "Tachibana-senpai belum mau naik ke kamar? Yang lain sudah pada masuk kamar semua lho."
        miyuki "Hmm... sebentar lagi, Yutaka-kun. Kalau aku langsung bangun sekarang, rasanya ruangannya agak goyang sedikit."
        nar "Miyuki tertawa pelan sambil menyentuh pelipisnya dengan ujung jari. Biasanya di kampus ia selalu duduk tegak dengan sikap senior yang terjaga rapi, tetapi malam ini nada bicaranya terdengar jauh lebih lambat dan manja."
        yutaka "Senpai tadi minum dua kaleng sih. Padahal sudah diingetin kalau yang kaleng merah muda itu ada campuran alkoholnya."
        miyuki "Habisnya rasa persiknya manis banget, kayak soda buah biasa. Lagipula tadi waktu kalian ribut main kartu di karpet, aku senang banget lihatnya... jadi malas naik ke kamar cepat-cepat."
        nar "Ia menggeser kaleng kosong di meja menjauh sedikit dengan ujung jarinya, lalu menoleh menatapmu dengan mata biru safir yang tampak berat oleh kantuk."
        miyuki "Yutaka-kun... besok pagi waktu sarapan, jangan ledekin Senpai di depan yang lain ya. Malu banget kalau senior paling tua di sini malah pusing duluan gara-gara minuman buah."
        yutaka "Tenang aja, mulutku aman kok, Senpai."
        miyuki "Janji ya... sekali-sekali Senpai cuma pengin duduk malas-malasan begini aja, nggak usah sok rapi dan ngurusin orang terus."
        nar "Ia menyandarkan pipinya ke sandaran sofa, memejamkan mata sebentar sambil bernapas teratur tanpa sedikit pun rasa curiga atau waspada di dekatmu."
    call kk_family_menu("Mi05", ["\"Minum air putih dulu ya, Senpai. Kalau mau cerita, aku dengerin.\"", "\"Ayo kuantar ke kamar dulu, Senpai. Nanti malah masuk angin di sofa.\"", "Duduk diam mengamati betapa rentannya ia malam ini."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu melangkah ke dapur sebentar untuk mengambil segelas air putih suhu ruang, lalu kembali dan duduk di sisi sofa yang kosong dengan jarak yang sopan."
            chiasa "Minum air putih dulu sedikit ya, Tachibana-senpai, biar besok pagi kepalanya nggak sakit. Kalau Senpai masih belum ngantuk dan mau ngobrol, aku temani di sini."
            nar "Miyuki membuka matanya pelan, menerima gelas itu dengan kedua tangan, lalu meminumnya beberapa teguk sebelum menaruh gelasnya di atas tatakan meja."
            miyuki "Terima kasih ya, Chiasa-chan. Airnya sejuk."
            chiasa "Di vila ramai begini enak ya, Senpai. Dari sore tadi ada aja suaranya."
            miyuki "Iya... jujur aja, itu yang bikin aku paling malas masuk kamar malam ini. Kalau di apartemenku sendiri, tiap aku pulang habis jaga praktik malam dari rumah sakit, ruangannya tuh sepi banget. Begitu pintu dikunci, yang kedengaran cuma bunyi jarum jam sama kulkas."
            chiasa "Orang tua Senpai jarang mampir ke apartemen?"
            miyuki "Ayah sama Ibu sibuk banget di rumah sakit mereka. Paling sebulan sekali asisten Ibu kirim paket buah mahal atau baju baru ke resepsionis bawah, terus Ibu cuma kirim pesan dua baris nanya jadwal ujianku."
            nar "Miyuki memeluk bantal sofanya lebih erat, dagunya bertumpu di tepi kain bantal."
            miyuki "Makanya kalau di kampus atau waktu kumpul kayak gini, aku senang banget kalau bisa masakin sesuatu atau bantu anak-anak. Soalnya cuma pas lagi dibutuhin orang gitu rasanya aku nggak lagi sendirian."
            nar "Tiba-tiba Miyuki terdiam sendiri. Ia mengerjap, lalu buru-buru menutup mulutnya dengan punggung tangan sambil menatapmu canggung."
            miyuki "Eh... aduh, maaf banget ya, Chiasa-chan. Aku malah curhat ngelantur malam-malam begini. Biasanya aku nggak pernah cerita sampai bagian itu, soalnya orang-orang suka bingung mau nanggepin apa kalau lihat aku ngeluh."
            chiasa "Nggak usah minta maaf, Senpai. Aku sama sekali nggak keberatan dengerinnya kok. Kalau sekarang sudah capek ngomong, kita duduk diam aja dengerin suara pantai juga nggak apa-apa."
            miyuki "...Hehe. Beneran boleh duduk diam aja sebentar tanpa harus cari topik?"
            chiasa "Boleh banget. Sandaran aja lagi, Senpai."
            nar "Miyuki tersenyum lega, menyandarkan kembali bahunya ke bantalan sofa sementara kamu menemaninya dalam tenang sampai pusing di kepalanya perlahan mereda."
        else:
            nar "Kamu berjalan ke dapur untuk mengambil segelas air putih, lalu kembali ke ruang tengah dan duduk di ujung sofa yang berjarak cukup sopan darinya."
            yutaka "Minum air putih dulu ya, Tachibana-senpai, biar besok pagi nggak pusing waktu bangun. Kalau Senpai masih mau duduk ngobrol di sini, aku temani."
            nar "Miyuki membuka kelopak matanya pelan, menerima gelas kaca itu dengan kedua tangan, lalu meneguknya setengah sebelum meletakkannya kembali ke meja."
            miyuki "Terima kasih ya, Yutaka-kun. Tenggorokanku langsung enakan."
            yutaka "Tumben Senpai betah banget di ruang tengah sampai selarut ini."
            miyuki "Habisnya di sini hangat sih, masih berasa baru dipakai kumpul ramai-ramai. Kalau aku pulang ke apartemenku sendiri habis praktik malam, tempatnya tuh kelewat luas dan sepi. Begitu lampu dinyalain, nggak ada suara siapa-siapa."
            yutaka "Keluarga Senpai jarang mampir ke sana?"
            miyuki "Ayah sama Ibu jadwal operasinya padat terus dari pagi sampai malam. Paling mereka cuma suruh orang kirim barang atau hadiah ke apartemen, tapi jarang banget sempat telepon lama. Makanya aku suka kalau lagi kumpul bareng kalian terus bisa bantu-bantu nyiapin makanan... rasanya kayak kehadiranku ada gunanya."
            nar "Miyuki mendadak berhenti bicara. Ia menatap gelas air di meja, lalu menutup bibirnya sedikit dengan punggung tangan dan menoleh padamu dengan raut malu."
            miyuki "Aduh... maaf ya, Yutaka-kun. Efek minumannya bikin mulutku ngomong terlalu jauh. Biasanya aku selalu berhenti sebelum bahas soal rumah, soalnya orang suka serba salah kalau dengar aku ngeluh."
            yutaka "Nggak usah minta maaf, Senpai. Sama sekali nggak bikin serba salah kok. Kalau Senpai sudah capek cerita, duduk diam aja di sini juga nggak masalah."
            miyuki "...Hehe. Beneran nggak apa-apa kalau Senpai diam aja sebentar?"
            yutaka "Nggak apa-apa. Istirahatin aja matanya dulu."
            nar "Miyuki mengangguk kecil lalu menyandarkan kepalanya kembali ke punggung sofa, membiarkan keheningan malam vila menemani kalian berdua sampai rasa pusingnya hilang."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Melihat kelopak matanya sudah berkali-kali tertutup dan udara dari celah pintu beranda mulai bertambah dingin, kamu bangkit berdiri lalu mengulurkan tangan ke hadapannya."
            chiasa "Ayo kuantar naik ke kamar dulu, Tachibana-senpai. Di ruang tengah sini angin malamnya mulai tembus dari kaca, nanti Senpai malah masuk angin kalau ketiduran di sofa."
            miyuki "Hmm... iya juga ya. Kakiku rasanya agak berat nih, maaf ngerepotin kamu ya, Chiasa-chan."
            chiasa "Sama sekali nggak ngerepotin. Pegangan aja ke lenganku pelan-pelan. Mau sekalian kukirimkan pesan ke Sena-san biar dia tahu Senpai sudah balik ke kamar?"
            miyuki "Oh, iya... tolong kirim pesan singkat ke Sena dari ponselku di tas ya. Tadi jam sembilan dia sempat nanya aku lagi apa."
            nar "Kamu mengambil tas kecilnya, mengetik kabar singkat ke Sena, lalu memapah lengan Miyuki menaiki anak tangga kayu menuju kamar putri di lantai dua. Sesampainya di dalam kamar, kamu membantunya duduk di tepi kasur dan menaruh segelas air putih di atas nakas samping bantalnya."
            chiasa "Air minumnya kutaruh di sebelah lampu tidur ini ya, Senpai. Selimutnya sudah cukup tebal belum?"
            miyuki "Sudah hangat kok. Makasih banyak ya, Chiasa-chan, sudah sabar banget ngurusin Senpai malam ini."
            nar "Miyuki menarik selimut sampai ke bahunya sambil tersenyum mengantuk ke arahmu."
            miyuki "Besok pagi kalau aku kelihatan malu pas ketemu di meja makan, tolong ingetin ya kalau malam ini aku beneran cuma kecapekan minta tidur, jangan malah diketawain."
            chiasa "Aman, Senpai. Selamat malam, tidur yang nyenyak ya."
            nar "Kamu mematikan lampu utama kamar tersebut dan menutup pintunya tanpa suara."
        else:
            nar "Melihat kelopak matanya sudah makin berat dan hawa dingin dari celah beranda mulai masuk ke ruang tengah, kamu bangkit berdiri untuk membantunya bangun dari sofa."
            yutaka "Ayo kuantar sampai depan kamarmu di atas, Tachibana-senpai. Kalau ketiduran di sofa sini sampai pagi, besok lehermu pegal dan bisa masuk angin."
            miyuki "Hmm... iya deh. Maaf ya, Yutaka-kun, malah bikin kamu repot ngantar aku."
            yutaka "Nggak repot kok. Pegang aja lengan jaketku waktu naik tangga biar nggak tersandung. Mau sekalian kukabari Sena-san biar dia nggak khawatir?"
            miyuki "Boleh... tolong bilang ke Sena kalau aku sudah mau tidur di kamar vila ya."
            nar "Kamu mengambilkan segelas air putih dari dapur dengan tangan kiri, lalu menemani Miyuki berjalan pelan menaiki tangga kayu lantai dua sampai ke depan pintu kamarnya. Di ambang pintu, kamu menyerahkan gelas air tersebut ke tangannya."
            yutaka "Ini air putihnya ditaruh di dekat kasur ya, Senpai. Jangan lupa kunci pintunya dari dalam."
            miyuki "Terima kasih banyak ya, Yutaka-kun. Kamu baik banget malam ini. Besok pagi kalau aku malu waktu ketemu di ruang makan, ingetin ya kalau malam ini aku beneran cuma minta istirahat, jangan diledekin."
            yutaka "Iya, tenang aja. Selamat malam, Tachibana-senpai."
            miyuki "Selamat malam, Yutaka-kun."
            nar "Kamu menunggu dua detik di koridor sampai terdengar bunyi kunci pintu kamarnya diputar dari dalam, barulah kamu berbalik kembali ke kamarmu sendiri."
    else:
        if kk_host == "chiasa":
            nar "Kamu tidak beranjak mengambilkan air ke dapur dan tidak pula mengajaknya naik ke kamar. Kamu hanya duduk diam di ujung sofa, memperhatikan bagaimana napas Miyuki melambat dan seluruh pertahanan dirinya lepas begitu saja di ruangan yang sepi ini."
            nar "Di bawah cahaya lampu sudut yang redup, kamu mencatat dengan kepala dingin betapa mudahnya seorang senior yang di kampus selalu tampak sempurna dan tak tersentuh ini kehilangan kewaspadaannya hanya karena merasa berada di dekat orang yang ia kenal."
            miyuki "Chiasa-chan... masih di situ kan?"
            chiasa "Masih, Senpai."
            miyuki "Rasanya tenang banget ya kalau ada orang yang bisa dipercaya kayak gini... aku nggak perlu takut macam-macam."
            chiasa "...Iya, Senpai. Istirahat aja dulu di situ."
            nar "Malam ini kamu tidak menyentuhnya sedikit pun dan membiarkannya tertidur pulas di sofa sampai ia terbangun sendiri menjelang dini hari untuk naik ke kamar."
            nar "Di dalam benakmu, celah kerentanan yang baru saja kamu saksikan malam ini sudah tersimpan sebagai satu kemungkinan gelap yang sewaktu-waktu bisa kamu gunakan jika kamu memilih jalan itu."
        else:
            nar "Kamu tidak beranjak mengambilkan air ke dapur dan tidak pula mengajaknya pindah ke kamar atas. Kamu hanya duduk diam di ujung sofa, mengamati bagaimana napas Miyuki melambat dan seluruh kewaspadaannya hilang di ruangan yang sudah kosong ini."
            nar "Di bawah lampu sudut yang redup, kamu memperhatikan dengan kepala dingin betapa mudahnya seorang senior yang biasanya selalu rapi dan berhati-hati ini melepaskan seluruh bentengnya hanya karena merasa aman di dekatmu."
            miyuki "Yutaka-kun... kamu masih di situ kan?"
            yutaka "Masih, Senpai."
            miyuki "Enak banget ya rasanya bisa duduk tenang sama orang yang bisa dipercaya begini... tanpa harus mikir macam-macam."
            yutaka "...Iya, Senpai. Istirahat aja dulu."
            nar "Malam ini kamu tidak melakukan tindakan apa pun dan membiarkannya tertidur di sofa sampai ia terbangun sendiri beberapa jam kemudian untuk naik ke kamarnya."
            nar "Di dalam kepala, celah kerentanan yang terbuka lebar malam ini sudah telanjur kamu catat sebagai satu jalan gelap yang kini terbuka jika suatu hari kamu memutuskan untuk memakainya."
    return

init 1 python:
    _hook("Mi05-A", lambda: (kk_rel("miyuki","trust",6), kk_rel("miyuki","intim",4)))
    _hook("Mi05-B", lambda: (kk_rel("miyuki","trust",8), kk_flag("miyuki_dijaga_vila")))
    _hook("Mi05-C", lambda: kk_flag("force_tersedia_miyuki"))
