# Naskah penghubung draft editorial; sumber Event_Nagisa, Alur_Cabang/02
# dan Sistem_Cabang_dan_Poin §1. Tidak ditampilkan sebagai teks desain.
# ┌─ PANDUAN CERITA · N04 · Gagal Mengaku Lagi
# │ LOKASI  : Alam & Pantai · Tepi Sungai
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : kembang api; ia mau mengaku pada Koita dan gagal.
# │ INTI    : A hibur / B dorong mengaku / C menyela.
# │ AKHIRAN : C membuat Nagisa marah tapi juga lega.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N04:
    call kk_scene_enter("nagisa", "Tepi Sungai · Kembang api")
    play sound "audio/sfx/fireworks.wav"
    if kk_host == "chiasa":
        nar "Di tepi tanggul rumput yang menghadap langsung ke permukaan sungai, pantulan kembang api berpendar seperti pecahan cahaya emas dan biru di atas air yang gelap. Suara sorak penonton dari sisi jembatan terdengar bercampur dengan dentuman demi dentuman di langit malam Agustus."
        nar "Kalian duduk di atas alas kain biru di lereng rumput yang agak lengang. Beberapa langkah di sebelahmu, Sakurajima Nagisa duduk memeluk kedua lututnya. Dari samping, kamu melihat jelas bagaimana bahunya menegang, kedua tangannya meremas ujung lengan yukata bermotif bunga krisannya, dan bibirnya terbuka lalu tertutup lagi setiap kali menunggu jeda singkat di antara dua ledakan besar."
        koita "Wah, yang warna hijau barusan mekarnya lebar banget ya! Nagisa-chan, dari tempatmu ketutupan pohon nggak? Chi-chan juga kelihatan jelas kan?"
        chiasa "Jelas banget kok, Ko-nii, dari sini malah nggak kena dorong orang lewat."
        nagisa "Nggak kok, kelihatan jelas dari sini."
        nar "Suara Nagisa terdengar sedikit lebih kaku dari biasanya. Kamu melihatnya sempat melirik ke arahmu sekali sebelum kembali memusatkan pandangannya ke punggung Koita. Begitu langit malam hening selama dua detik setelah satu bunga api raksasa meredup, ia akhirnya menarik napas cepat dan menoleh ke arah Koita."
        nagisa "Ko-kun... dengar sebentar, sebenarnya dari dulu aku sudah lama mau bilang kalau..."
        nar "Koita langsung menoleh dengan wajah ramah penuh perhatian. Tepat di saat mata mereka bertemu di bawah sisa cahaya langit, keberanian Nagisa tampak menciut seketika. Suaranya tertahan di tenggorokan, dan pada detik yang sama, rentetan kembang api beruntun meledak menggelegar di atas sungai hingga menelan habis sisa ucapannya."
        koita "Apa, Nagisa-chan? Maaf, suaramu ketutup ledakan kembang api barusan! Kamu mau pindah duduk lihat dari sebelah sana yang lebih dekat pagar sungai?"
        nagisa "...Bukan apa-apa! Nggak jadi!"
        koita "Eh? Beneran nggak apa-apa? Kalau di sini kena asap, kita bisa geser sedikit kok."
        nagisa "Aku bilang nggak jadi ya nggak jadi, Ko-kun! Lihat ke langit saja sana!"
        koita "Oh... oke, oke, maaf kalau salah dengar."
        nar "Nagisa langsung membuang muka ke arah sungai dan kembali duduk tegak dengan kaku. Di atas pangkuannya, jari-jarinya terus meremas kain lengan yukata dengan keras meskipun Koita sudah kembali menengadah memandangi langit."
        nar "Pantulan cahaya merah dari bunga api berikutnya menyinari pipi Nagisa yang memanas karena malu pada dirinya sendiri."
        nar "Kamu yang duduk hanya berjarak satu rentangan tangan darinya dapat mendengar helaan napas pendek yang ia tahan di sela keriuhan penonton di sekitar tanggul."
        nar "Di tengah jeda sebelum peluncuran babak berikutnya dimulai, kamu tahu sikap yang kamu ambil detik ini akan menentukan apakah kegagalan kecilnya malam ini berakhir begitu saja atau berbelok ke arah lain."
    else:
        nar "Di tepi tanggul rumput yang menghadap langsung ke permukaan sungai, pantulan kembang api berpendar seperti pecahan cahaya emas dan biru di atas air yang gelap. Suara sorak penonton dari arah jembatan bercampur dengan dentuman demi dentuman di langit malam Agustus."
        nar "Kalian menggelar alas kain biru di lereng rumput yang agak tinggi. Di sampingmu, Sakurajima Nagisa duduk memeluk lutut dengan bahu menegang. Dari sudut matamu, kamu melihat jelas kedua tangannya meremas ujung lengan yukatanya sementara ia terus memperhatikan Koita dan menunggu jeda sunyi di antara dua peluncuran kembang api."
        koita "Yang barusan tinggi banget naiknya! Nagisa-chan, dari posisimu ketutupan asap nggak? Yutaka, kelihatan jelas kan?"
        yutaka "Jelas. Arah anginnya ke seberang sungai, jadi asapnya nggak turun ke sini."
        nagisa "Nggak, masih jelas kok."
        nar "Jawabannya keluar kaku dan pendek. Begitu langit hening selama dua detik, Nagisa menarik napas pendek lalu mencondongkan badan menoleh ke arah Koita yang duduk agak di depan."
        nagisa "Ko-kun... dengar dulu, sebenarnya aku sudah lama pengin bilang soal..."
        nar "Koita langsung menoleh dengan senyum ramahnya. Tepat saat tatapan mereka beradu, keberanian Nagisa langsung menyusut. Suaranya mengecil di ujung lidah, dan pada detik yang sama, rangkaian kembang api besar meledak beruntun di langit atas sungai, menenggelamkan sisa kalimatnya."
        koita "Kenapa, Nagisa-chan? Suaramu ketutup kembang api barusan! Kamu mau pindah lihat dari bagian bawah yang lebih dekat air?"
        nagisa "...Bukan! Nggak jadi ngomong!"
        koita "Lho, kok malah marah? Tadi beneran nggak kedengaran sama sekali lho."
        nagisa "Sudah lupakan saja, lihat kembang apinya sana!"
        koita "Iya deh, maaf..."
        nar "Ia kembali duduk tegak dengan wajah memaling ke arah sungai. Di atas pangkuannya, jari-jarinya masih mencengkeram kain lengan yukata erat-erat meski Koita sudah kembali menengadah ke langit."
        nar "Bias cahaya biru dan perak dari langit sungai memantul di matanya yang meredup kesal karena lagi-lagi membiarkan nyalinya runtuh di detik terakhir."
        nar "Koita sendiri tampak benar-benar mengira Nagisa hanya sedang mengeluhkan posisi duduk, sama sekali tidak menyadari ketegangan yang baru saja meletup di sampingnya."
        nar "Menyaksikan kebuntuan yang berulang di depan matamu itu, kamu menimbang apakah akan menemaninya menenangkan diri, membuka jalan agar mereka bicara berdua, atau justru memotong kesempatannya sekalian."
    call kk_family_menu("N04", ["Tetap di sampingnya.", "Beri dia kesempatan bicara berdua dengan Koita.", "Panggil Koita sebelum Nagisa melanjutkan."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu tidak ikut menoleh ke arah Koita dan tidak pula menyinggung pengakuan yang baru saja kandas di tengah suara ledakan itu. Kamu hanya bergeser duduk tenang di samping Nagisa, membiarkan bahu kalian sejajar sambil menyodorkan sebotol teh jelai dingin yang baru kamu keluarkan dari tasmu."
            chiasa "Minum dulu, Nagisa-senpai. Udara di tepi sungai malam ini lumayan gerah."
            nar "Nagisa melirikmu dua kali dari sudut matanya, awalnya tampak waspada seolah takut kamu akan menanyakan apa yang baru saja ia bisikkan kepada Koita. Ketika ia melihatmu hanya duduk tenang menemaninya tanpa senyum menggoda sedikit pun, bahunya yang kaku perlahan turun. Ia menerima botol dingin itu."
            nagisa "...Bodoh sekali aku barusan, ya."
            chiasa "Nggak ada yang bilang Senpai bodoh kok."
            nagisa "Padahal aku sudah latihan menyusun kalimatnya dari kemarin malam di depan cermin kamar. Di dalam kepalaku, semuanya hening sampai kalimatku selesai kuucapkan. Tapi begitu di dunia nyata... ternyata bahkan sebelum suara kembang apinya meledak pun, lidahku sendiri yang sudah keburu kaku duluan."
            chiasa "Mengubah hubungan yang sudah jalan bertahun-tahun sejak kecil itu memang menakutkan, Senpai. Wajar kalau nggak bisa langsung keluar dalam satu tarikan napas."
            nagisa "Kamu dengar kalimatku yang kepotong tadi ya, Chiasa?"
            chiasa "Cuma bagian depannya saja kok, sisanya ketutup suara kembang api. Lagipula kalau Senpai belum siap malam ini, nggak usah dipaksa harus selesai sekarang."
            nagisa "Huh... padahal setiap kali musim panas lewat, rasanya aku selalu bilang ke diriku sendiri 'tahun depan pasti bisa'. Tahu-tahu sekarang kita sudah kuliah, dan di sekitar Ko-kun makin banyak orang yang luar biasa."
            chiasa "Senpai sendiri juga selalu ada di sebelahnya sejak dulu, nggak usah mengecilkan diri sendiri begitu."
            nagisa "Aneh banget ya aku malah dihibur sama kamu di tepi sungai begini... padahal biasanya kita berdua paling sering debat hal nggak penting."
            chiasa "Sekali-sekali akur di bawah kembang api nggak ada salahnya kan, Senpai? Minum dulu tehnya biar tenang."
            nar "Nagisa membuka tutup botol, menyesap teh dingin itu pelan, lalu menempelkan dinding botol yang berembun ke pipinya yang masih agak memerah. Remasan tangannya pada lengan yukata akhirnya terlepas."
            nagisa "...Terima kasih ya sudah duduk diam di sebelahku dan nggak nanya macam-macam, Chiasa. Sungguh, kalau kamu tadi ikutan nanya tadi aku mau ngomong apa, aku mungkin sudah lari pulang dari tanggul ini."
            chiasa "Aku duduk di sini saja sampai babak kembang apinya selesai, Senpai."
            nagisa "Iya, jangan pindah ke mana-mana dulu. Lihat tuh, kembang api bentuk bunga krisan besarnya baru mau diluncurkan dari tongkang tengah sungai."
            chiasa "Warnanya bagus sekali kalau memantul di permukaan air sungai yang gelap begitu."
            nagisa "Hehe, iya... setidaknya malam ini pemandangan kembang apinya nggak gagal kayak nyaliku tadi."
            chiasa "Simpan saja sisa tenagamu buat menikmati malam ini dulu, Senpai."
            nagisa "Iya. Nanti waktu turun dari tanggul kita mampir beli permen apel di stan bawah bareng-bareng ya, Chiasa."
            nar "Ia menggeser duduknya sedikit lebih rapat di atas alas kain biru sambil menyandarkan sikunya di lutut, membiarkan keheningan hangat di antara kalian meredakan sisa detak jantungnya yang sempat memburu."
            nar "Kalian kembali memandangi pantulan warna emas di permukaan sungai berdampingan, membiarkan malam musim panas itu lewat tanpa ada satu pun tuntutan."
        else:
            nar "Kamu tidak melontarkan ledekan dan tidak pula mengungkit kalimatnya yang baru saja terputus di tengah ledakan. Kamu hanya duduk tenang di sampingnya dengan satu lutut ditekuk, lalu menggeser sebotol teh dingin dari kantong plastik ke dekat tangannya."
            yutaka "Minum dulu, Nagisa. Tenggorokanmu pasti kering dari tadi di tengah keramaian begini."
            nar "Nagisa melirikmu dua atau tiga kali dengan sudut mata yang siap membela diri, seolah menunggu sindiran keluar dari mulutmu. Ketika ia menyadari kamu benar-benar hanya menemaninya duduk diam malam ini, ketegangan di pundaknya perlahan mereda dan ia mengambil botol tersebut."
            nagisa "...Payah banget ya aku barusan."
            yutaka "Nggak ada yang bilang kamu payah, Nagisa."
            nagisa "Aku sudah latihan kalimatnya berkali-kali di kamar dari kemarin. Di kepalaku, semua orang diam mendengarkan sampai kalimatku selesai. Tapi pas sudah duduk di depannya... ternyata bahkan sebelum kembang apinya bunyi pun, nyaliku sendiri yang sudah ciut duluan."
            yutaka "Namanya juga mau ngomongin hal yang sudah kamu simpan bertahun-tahun. Wajar kalau lidahmu mendadak kelu waktu orangnya langsung menoleh."
            nagisa "Jadi kamu tadi dengar aku mau ngomong apa ke Ko-kun?"
            yutaka "Dengar sedikit, tapi itu urusanmu sama dia. Kalau malam ini rasanya belum sanggup, nggak usah terlalu keras menyalahkan diri sendiri."
            nagisa "Setiap kali festival musim panas selesai, aku selalu bilang dalam hati tahun depan pasti berani. Eh, tahu-tahu sekarang sudah masuk kuliah, dan di sekitar Ko-kun makin banyak orang yang lebih tenang dan dewasa daripada aku."
            yutaka "Kamu nggak perlu jadi orang lain buat didengarkan, Nagisa. Waktunya juga masih panjang, nggak usah panik kayak dunia berhenti malam ini."
            nagisa "Tumben banget omonganmu kedengaran dewasa malam ini, Yutaka..."
            yutaka "Sekali-sekali boleh lah. Minum dulu tehmu."
            nar "Ia membuka tutup botol minuman dingin itu dan meneguknya pelan, lalu menyandarkan kedua tangannya di atas lutut dengan napas yang jauh lebih teratur."
            nagisa "...Makasih ya sudah duduk di sini tanpa ngeledek aku, Yutaka. Serius, rasanya kepalaku agak lebih tenang sekarang."
            yutaka "Santai saja. Lihat tuh, babak penutupnya sudah mulai naik dari perahu peluncur di tengah sungai."
            nagisa "Oh, iya! Yang rentetan warna emas beruntun itu kan babak terakhirnya!"
            yutaka "Makanya tonton saja dulu langitnya, urusan pusingnya dipikir besok lagi."
            nagisa "Hehe, bener juga. Habis ini temani aku beli yakisoba di stan dekat jembatan ya, tiba-tiba perutku lapar lagi habis tegang dari sore."
            yutaka "Siap, nanti kita mampir sebelum pulang."
            nar "Nagisa mengangguk kecil dengan senyum yang jauh lebih lepas. Kalian kembali menatap cahaya yang mekar bertubi-tubi di atas sungai dalam diam yang nyaman."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Melihat Nagisa yang masih tampak menyesal karena kehilangan momennya barusan, kamu bangkit berdiri dari alas kain, menepuk pelan bahu Koita untuk menarik perhatiannya dari langit, lalu mencondongkan badan sedikit."
            chiasa "Ko-nii, aku mau naik ke deretan stan di atas tanggul sebentar ya buat beli minuman dingin sama kakigori. Tadi kelihatannya Nagisa-senpai ada hal penting yang mau dibicarakan berdua sama kamu sebelum acara kembang apinya selesai."
            nar "Nagisa langsung mendongak memelototimu dengan mata biru membulat dan wajah memerah sampai ke telinga, separuh kesal karena tiba-tiba didorong ke tengah panggung, separuh gugup karena kini ia tidak punya alasan lagi untuk mundur."
            nagisa "H-hei, Chiasa! Jangan ngarang cerita seenaknya sendiri dong! Aku tadi nggak bilang mau ngomong berdua..."
            chiasa "Antrean minuman di atas lumayan panjang kok, Nagisa-senpai, jadi aku bakal agak lama balik ke sininya. Santai saja ngobrolnya."
            koita "Oh? Tadi memang ada yang mau kamu omongin serius ya, Nagisa-chan? Pantas suaramu tadi kedengaran agak tegang. Sini, sekarang lagi jeda peluncuran babak kedua kok, suaranya sudah nggak berisik."
            chiasa "Aku naik duluan ya, Ko-nii, Nagisa-senpai."
            nar "Sebelum Nagisa sempat menarik ujung yukatamu untuk menahanmu pergi, Koita sudah memutar tubuhnya menghadap Nagisa sepenuhnya dengan raut wajah tenang yang siap mendengarkan. Nagisa menelan ludah, meremas kain di atas lututnya sekali, lalu mengangkat dagunya menatap Koita."
            nagisa "...Iya, Ko-kun. Tunggu sebentar, yang mau kubilang tadi memang bukan soal pindah tempat duduk. Kalau babak kembang api yang ini selesai dan orang-orang mulai jalan turun, aku mau bicara sebentar sama kamu."
            koita "Oke, Nagisa-chan. Aku nggak bakal ke mana-mana, nanti kita jalan belakangan habis kembang apinya selesai ya."
            nagisa "Awas kalau kamu lupa atau malah sibuk ngobrol sama yang lain!"
            koita "Nggak bakal lupa, janji. Aku duduk di sini terus kok sampai peluncurannya habis."
            nar "Saat kamu merapikan lipatan yukatamu dan berbalik menuju jalur tangga tanggul, Nagisa sempat menoleh singkat ke arahmu dengan sorot mata yang mencampurkan rasa gugup dan ucapan terima kasih yang tertahan."
            nar "Kamu melangkah menaiki tangga batu tanggul menuju keramaian stan festival tanpa menoleh ke belakang lagi, memberikan ruang penuh yang sudah begitu lama tertunda di antara mereka berdua."
        else:
            nar "Melihat Nagisa yang masih menggigit bibirnya karena menyesal kehilangan kesempatan barusan, kamu langsung bangkit berdiri, menepuk bahu Koita, lalu menunjuk ke arah deretan stan pedagang di atas tanggul."
            yutaka "Koita, aku mau naik ke stan atas sebentar beli minum dingin. Tadi kelihatannya Nagisa ada urusan penting yang mau dibicarakan berdua sama kamu."
            nar "Nagisa langsung mendongak menatapmu tajam dengan wajah memerah padam, marah karena tiba-tiba dipaksa maju tanpa persiapan, sekaligus gentar karena kesempatan kedua berarti ia harus berhadapan langsung dengan jawabannya."
            nagisa "H-hei, Yutaka! Jangan bicara sembarangan! Siapa yang bilang ada urusan penting..."
            yutaka "Aku mau sekalian antre yakisoba di ujung atas, jadi bakal lama baliknya. Ngobrol saja dulu kalian berdua."
            koita "Eh? Tadi yang ketutup suara ledakan itu memang hal serius ya, Nagisa-chan? Sekarang lagi jeda pengisian kembang api kok, aku bisa dengar jelas."
            yutaka "Duluan ke atas ya."
            nar "Sebelum Nagisa sempat berdiri untuk mengejarmu, Koita sudah bergeser menghadapnya penuh dengan tatapan fokus. Nagisa menarik napas pendek, menegakkan punggungnya, lalu menatap mata Koita."
            nagisa "...Iya, Ko-kun. Yang tadi itu memang nggak ada hubungannya sama tempat duduk. Nanti begitu kembang api penutupnya selesai dan kerumunannya mulai agak sepi, ada yang mau kubicarakan sebentar sama kamu."
            koita "Iya, Nagisa-chan. Aku janji dengerin sampai selesai nanti."
            nagisa "Jangan sampai keburu pergi duluan!"
            koita "Iya, aku tunggu di sini sama kamu sampai semua orang bubar."
            nar "Ketika kamu melangkah meninggalkan tepi alas kain, Nagisa sempat melirik ke arah punggungmu dengan wajah merah padam, menyadari bahwa dorongan mendadakmu barusan telah memaksanya berhenti menunda-nunda lagi."
            nar "Kamu melangkah menaiki lereng tanggul menuju deretan lampion stan tanpa menoleh lagi, memastikan malam ini tidak ada gangguan luar yang bisa menghalangi mereka berbicara."
    else:
        if kk_host == "chiasa":
            nar "Tepat ketika jeda hening berikutnya tiba dan Nagisa kembali menarik napas dalam seolah hendak mencoba mengulangi kalimatnya kepada Koita, kamu lebih dulu bangkit berdiri dan menarik ujung lengan yukata Koita."
            chiasa "Ko-nii, temani aku ke stan di belakang jembatan sebentar yuk! Tadi kantong minuman sama camilan yang kita beli ketinggalan di bangku dekat deretan lampion, berat kalau kuangkat sendiri."
            koita "Eh, ketinggalan di sana? Wah, ayo cepat kita ambil sebelum dibereskan panitia! Tunggu sebentar di sini ya, Nagisa-chan, aku bantu Chi-chan ambil barang sebentar terus langsung balik sebelum penutup!"
            nar "Koita langsung berdiri dan bersiap mengikuti langkahmu tanpa menyadari sedikit pun bahwa ada sebuah pengakuan besar yang baru saja kamu potong tepat di depannya. Baru saja Koita melangkah dua tapak lebih dulu ke tangga tanggul, suara rendah dan tajam dari atas alas kain menghentikan langkahmu."
            nagisa "Kamu sengaja melakukan itu barusan, Chiasa?"
            nar "Kamu menoleh perlahan ke bawah. Tatapan mata biru Nagisa menyala tajam menatap wajahmu di bawah pendar cahaya lampion, tetapi ketika pandanganmu turun ke pangkuannya, kamu melihat kedua tangannya yang sejak tadi meremas erat kain yukata kini justru perlahan mengendur."
            chiasa "Sengaja apa maksudnya, Nagisa-senpai? Kantong minuman kita memang masih tertinggal di bangku belakang kok, aku butuh Ko-nii buat bantu bawa."
            nagisa "...Jangan pura-pura bodoh. Kamu jelas-jelas lihat aku baru narik napas mau ngomong sama Ko-kun tadi."
            chiasa "Oh, tadi Senpai mau lanjut ngomong ya? Kirain sudah nggak jadi kayak yang Senpai bilang keras-keras barusan."
            nagisa "...Dasar."
            chiasa "Kalau Senpai memang sudah siap bicara, nanti waktu kami balik bawa minuman juga masih ada waktu sebelum pulang kok."
            nagisa "Diamlah, nggak usah sok ngatur waktuku."
            koita "Chi-chan! Ayo buruan, nanti keburu macet di tangga!"
            chiasa "Sebentar, Ko-nii! Kalau begitu kami ambil barang dulu ya, Nagisa-senpai."
            nar "Nagisa menggigit bibir bawahnya dan memalingkan wajah ke arah sungai tanpa membalas lebih jauh. Di raut wajahnya, rasa marah karena kalimatnya dipotong paksa dan rasa lega karena malam ini ia tidak jadi mempertaruhkan hubungannya dengan Koita tampak begitu rapat hingga ia tidak mampu menahanmu pergi."
        else:
            nar "Tepat ketika jeda sunyi di langit kembali turun dan Nagisa menarik napas panjang hendak mencoba mengulang pengakuannya, kamu lebih dulu bangkit berdiri dan menepuk pundak Koita."
            yutaka "Koita, ikut aku ke stan belakang sebentar. Kantong minuman sama makanan ringan yang kita beli tadi masih ketinggalan di meja dekat tiang lampion, repot kalau kubawa sendiri semuanya."
            koita "Lho, ketinggalan di meja sana? Ayo cepat kita ambil sebelum hilang! Nagisa-chan, tunggu di alas sini sebentar ya, aku bantu Yutaka angkat minuman terus langsung balik!"
            nar "Koita segera bangkit dan melangkah mendahuluimu menuju tangga tanggul, sama sekali tidak peka bahwa ada kalimat penting yang baru saja terpotong oleh ajakanmu. Tepat sebelum kamu ikut melangkah menyusulnya, suara rendah yang tertahan memanggilmu dari atas alas kain."
            nagisa "Kamu sengaja memotongku barusan, Yutaka?"
            nar "Kamu menoleh ke samping. Sorot mata biru Nagisa menatapmu tajam penuh kemarahan, sementara jemari tangannya yang sejak tadi mencengkeram kain yukata sampai kusut kini justru perlahan terlepas lemas di atas lututnya."
            yutaka "Sengaja gimana? Kantong minumannya memang masih di meja belakang, kamu bisa lihat sendiri nanti kalau kami bawa ke sini."
            nagisa "...Kamu tahu persis aku lagi ngumpulin nyali buat bicara sama Ko-kun barusan."
            yutaka "Tadi kamu sendiri yang teriak bilang nggak jadi ngomong. Kalau kamu kelihatan setegang orang mau loncat ke sungai begitu, mana mungkin kubiarkan."
            nagisa "...Dasar menyebalkan."
            yutaka "Kalau kamu beneran mau bicara tanpa gemetaran, tunggu kepala sama napasmu tenang dulu."
            nagisa "Aku nggak gemetaran tahu! Sudah sana pergi!"
            koita "Yutaka! Ayo, tangganya mulai padat nih!"
            yutaka "Iya, sebentar. Jaga alasnya ya, Nagisa."
            nar "Nagisa menggigit bibirnya dan membuang pandangannya ke arah pantulan air sungai. Kemarahan karena dihalangi dan kelegaan diam-diam karena ia punya alasan untuk menunda pengakuannya malam ini tampak jelas di wajahnya saat kamu berbalik menyusul Koita."
    return

# ┌─ PANDUAN CERITA · N06 · Fuuto Menawarkan Bantuan
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : Mochizuki membantu maket.
# │ INTI    : A dukung / B halangi / C cemburu.
# │ AKHIRAN : stage 2 (kelekatan) bila B/C.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N06:
    call kk_scene_enter("nagisa", "Studio Arsitektur")
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Malam itu kamu mampir ke lantai dua Gedung Arsitektur untuk mengembalikan penggaris siku milik Nagisa yang sempat terbawa di mapmu kemarin. Dari ambang pintu ruang studio yang terbuka separuh, lampu meja menyala terang diiringi suara gesekan karton dan percakapan tenang di dekat meja kerja tengah."
        else:
            nar "Kamu mampir ke lantai dua Gedung Arsitektur untuk mengembalikan penggaris siku milik Nagisa yang sempat terbawa di mapmu kemarin. Dari ambang pintu ruang studio yang terbuka separuh, terdengar suara gesekan karton dan percakapan tenang di dekat meja kerja tengah."
        nar "Di sana, Sakurajima Nagisa sedang membungkuk memeriksa sambungan maket gedung bertingkat dari karton putih tebal. Di seberang mejanya, seorang mahasiswa laki-laki berkacamata dengan rambut hitam agak berantakan dan kemeja flanel yang lengannya digulung tampak berdiri menahan sisi dinding maket tersebut dengan kedua tangan agar tidak bergeser."
        nar "Keduanya berbicara dengan kalimat pendek-pendek yang sudah terbiasa saling mengisi, layaknya rekan studio yang sudah beberapa kali melewati lembur bersama."
        "Fuuto" "Sisi dinding yang sebelah timur ini kutahan dari luar dulu biar nggak melengkung ya. Kamu cek kerataan sudut bawahnya dulu aja, Sakurajima-san."
        nagisa "Oke, tahan sebentar di situ ya, Mochizuki. Bagian siku bawahnya tadi lem kayunya kurang rata sedikit, mau kutambah pakai ujung tusuk gigi."
        "Fuuto" "Iya, santai aja, nggak pegal kok. Kalau posisinya kurang rapat setengah milimeter bilang ya, nanti kudorong pelan dari sini."
        nar "Baru ketika kamu mengetuk daun pintu kayu yang terbuka itu dua kali, Nagisa dan mahasiswa berkacamata tersebut menoleh bersamaan ke arah pintu."
        chiasa "Permisi, Nagisa-senpai. Lagi sibuk banget ngerjain maket ya? Aku mau balikin penggaris siku yang kemarin."
        nagisa "Oh, Chiasa! Masuk aja, pintunya memang nggak dikunci kok. Ini kami baru aja selesai pasang rangka dinding maket kelompok yang tadi hampir miring. Kenalin dulu, ini Mochizuki, teman satu kelas studioku."
        "Fuuto" "Halo, Amamiya-san. Aku Mochizuki Fuuto. Maaf ya meja tengahnya lagi penuh potongan karton begini."
        if "N03" in kk_missed:
            nagisa "Waktu maketku kena tampias hujan deras beberapa bulan lalu itu, Mochizuki juga yang kebetulan masih di kampus dan bantu aku bawain papan karton pengganti dari koperasi ke studio."
        chiasa "Oh, salam kenal, Mochizuki-senpai. Aku Amamiya Chiasa dari gedung sebelah."
        "Fuuto" "Tentu, Sakurajima-san beberapa kali sempat cerita soal kamu di studio."
        nar "Fuuto tersenyum agak malu-malu dan mengangguk sopan kepadamu, sementara kedua tangannya tetap setia menahan tegak lembaran dinding maket itu supaya lem yang baru dioleskan Nagisa tidak bergeser."
    else:
        if kk_slot >= 3:
            nar "Malam itu kamu melangkah naik ke Studio Arsitektur untuk melihat apakah Nagisa masih lembur dan mau pulang bareng ke arah stasiun. Dari celah pintu studio yang terbuka di bawah lampu neon panjang, kamu melihat Nagisa sedang menunduk serius di depan meja kerjanya yang dipenuhi potongan karton maket berwarna putih."
        else:
            nar "Kamu melangkah naik ke Studio Arsitektur untuk melihat apakah Nagisa sudah selesai kuliah dan mau pulang bareng ke arah stasiun. Dari celah pintu studio yang terbuka, kamu melihat Nagisa sedang menunduk serius di depan meja kerjanya yang dipenuhi potongan karton maket berwarna putih."
        nar "Ia tidak bekerja sendirian. Di sisi seberang meja, seorang mahasiswa berkacamata berambut hitam agak acak-acakan berdiri dengan sabar menahan salah satu sudut dinding maket agar tetap tegak lurus. Cara mereka berdua membagi tugas terdengar sangat kompak dan tenang."
        "Fuuto" "Bagian dinding timur ini kutahan dulu ya biar nggak goyang. Kamu periksa aja dulu sambungan sudut bawahnya, Sakurajima-san."
        nagisa "Sip, tahan sebentar ya, Mochizuki. Lem di pojok bawahnya tadi agak kurang merata, mau kutambal sedikit pakai pinset."
        "Fuuto" "Iya, nggak usah buru-buru. Kalau kurang lurus bilang aja, nanti kugeser pelan."
        nar "Ketika kamu mengetuk kusen pintu studio, barulah keduanya mengangkat kepala menoleh ke arahmu."
        yutaka "Masih lembur maket, Nagisa? Kirain jam segini sudah beres."
        nagisa "Eh, Yutaka. Masuk aja. Ini tinggal nunggu lem rangka dinding utamanya kering kok, tadi hampir aja miring sebelah. Kenalin, ini Mochizuki, teman sekelasku di sini."
        "Fuuto" "Halo, Kisaragi-san. Aku Mochizuki Fuuto. Maaf mejanya lagi berantakan banget."
        if "N03" in kk_missed:
            nagisa "Waktu tugas maketku rusak kena hujan deras di studio dulu, Mochizuki ini juga yang kebetulan lewat dan bantu bawain bahan karton baru ke sini."
        yutaka "Oh, salam kenal, Mochizuki. Aku Kisaragi Yutaka."
        "Fuuto" "Salam kenal juga, Kisaragi-san. Sakurajima-san lumayan sering menyebut namamu waktu kita istirahat."
        nar "Fuuto mengangguk sopan dengan senyum canggung khas orang pemalu, sementara jari-jarinya tetap menahan dinding karton maket itu dengan stabil agar pekerjaan Nagisa tidak terganggu."
    call kk_family_menu("N06", ["\"Lanjutin dulu aja, aku tunggu di dekat jendela biar nggak ganggu.\"", "\"Sini biar aku aja yang gantiin nahan bagian ini.\"", "\"Kalau lagi butuh bantuan begini, sebenarnya aku pengin kamu minta tolong ke aku juga.\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Lanjutin dulu aja sampai lemnya kering, Nagisa-senpai, Mochizuki-senpai. Penggarisnya kutaruh di kotak alat pinggir sini ya, aku duduk nunggu di kursi dekat jendela biar nggak ganggu tangan kalian."
            nagisa "Beneran nggak apa-apa nunggu sebentar, Chiasa? Paling tinggal tiga menit lagi kok sampai lemnya mengikat."
            chiasa "Nggak apa-apa, aku juga lagi santai kok hari ini."
            nar "Kamu menarik kursi di dekat jendela dan membiarkan mereka menyelesaikan pemasangan dinding maket tersebut. Dari tempat dudukmu, kamu bisa mendengar bagaimana Nagisa berbicara dengan nada yang jauh lebih tenang dan tanpa gengsi saat bekerja dengan teman sekelasnya itu."
            nagisa "Mochizuki, tolong dorong bagian atas kirinya sekitar dua milimeter ke dalam dong, masih agak renggang sedikit dari garis alasnya."
            "Fuuto" "Begini sudah pas belum? Aku tekan pelan dari siku bawahnya juga ya supaya nempel rata."
            nagisa "Nah, pas banget! Akhirnya berdiri tegak lurus juga! Terima kasih banyak ya, Mochizuki, sekarang sudah boleh dilepas kok tangannya."
            "Fuuto" "Coba kucek sekali lagi dari sisi samping... iya, sudah kuat menempel. Syukurlah nggak jadi bongkar ulang."
            nar "Nagisa tersenyum lebar penuh kelegaan kepada Fuuto, sama sekali tidak menoleh untuk memeriksa reaksimu di dekat jendela."
            "Fuuto" "Kalau begitu aku balik beresin meja gambarku di baris belakang dulu ya, Sakurajima-san. Permisi, Amamiya-san."
            chiasa "Iya, terima kasih, Mochizuki-senpai."
            nar "Setelah Fuuto kembali ke mejanya di ujung ruangan, Nagisa baru melambai memanggilmu mendekat ke meja tengah."
            nagisa "Chiasa, sini lihat deh! Rapi banget kan sambungan dindingnya sekarang? Kalau tadi Mochizuki nggak bantu nahanin dari seberang, pasti sudah miring lagi."
            chiasa "Rapi banget, Senpai. Kalian berdua kelihatan sudah kompak banget kerjanya."
            nagisa "Iya, dia orangnya sabar sekali kalau diajak ngecek ukuran milimeter begini. Enak diajak kerja bareng."
            chiasa "Kalau begitu penggaris sikunya sudah kutaruh di kotak alat Senpai ya, aku balik ke gedung sebelah dulu."
            nagisa "Oke, makasih banyak sudah repot-repot mengantar ke lantai dua ya, Chiasa!"
            nar "Nagisa mengangguk puas sambil membersihkan sisa lem di ujung pinsetnya dengan tisu, tampak sangat nyaman dengan rekan sekelasnya itu."
        else:
            yutaka "Beresin dulu aja sampai lemnya nempel kuat, Nagisa, Mochizuki. Aku duduk nunggu di bangku dekat jendela sana ya biar nggak ngalangin lampu meja kalian."
            nagisa "Oke, tunggu sebentar ya, Yutaka. Paling tiga menit lagi sudah kering kok lemnya."
            yutaka "Santai, aku nggak buru-buru."
            nar "Kamu menepi ke bangku dekat jendela dan memperhatikan keduanya menyelesaikan pekerjaan itu tanpa menyela. Dari sana terlihat jelas betapa lancarnya mereka berdua bekerja sama tanpa ada perdebatan kecil sedikit pun."
            nagisa "Mochizuki, geser ujung atasnya dua milimeter ke kiri dong, tadi agak miring sedikit waktu kutekan."
            "Fuuto" "Segini cukup, Sakurajima-san? Kutahan bagian bawahnya sebentar ya biar nggak geser lagi."
            nagisa "Sip, lurus sempurna! Makasih banyak ya, Mochizuki, sudah boleh dilepas kok sekarang."
            "Fuuto" "Kuperiksa sudut belakangnya sekali lagi... aman, sudah lurus. Untung langsung kencang lemnya."
            nar "Nagisa tersenyum cerah ke arah Fuuto dengan wajah lega, tidak sedikit pun melirik ke arahmu untuk mengecek reaksimu."
            "Fuuto" "Aku balik ke mejaku di belakang dulu ya, Sakurajima-san. Permisi, Kisaragi-san."
            yutaka "Iya, duluan aja, Mochizuki."
            nar "Begitu Fuuto berjalan kembali ke meja kerjanya sendiri, Nagisa langsung memanggilmu mendekat sambil menunjuk bangunan miniatur tersebut."
            nagisa "Yutaka, sini lihat! Tegak banget kan dinding timurnya sekarang? Untung tadi ada Mochizuki di studio, jadi nggak perlu kubongkar dari awal."
            yutaka "Iya, rapi banget sambungannya. Kompak juga kalian berdua."
            nagisa "Dia memang paling telaten di kelas kami kalau soal menahan rangka maket begini. Nggak gampang capek tangannya."
            yutaka "Kalau maketmu sudah selesai dipasang, berarti kita bisa langsung turun pulang sekarang?"
            nagisa "Tunggu dua menit aku tutup botol lem sama beresin pisau cutter ini dulu ya!"
            nar "Nagisa tersenyum senang sambil mulai memasukkan pisau cutter dan penggarisnya ke dalam kotak alat."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kamu tidak menepi ke bangku jendela. Kamu langsung melangkah ke sisi meja tempat Fuuto berdiri dan menatap dinding karton yang sedang ia pegangi."
            chiasa "Mochizuki-senpai kan pasti punya tugas maket sendiri yang harus diberesin di meja belakang. Sini, biar aku aja yang gantiin nahan sisi dinding yang ini, supaya Senpai bisa lanjut ngerjain tugas Senpai sendiri."
            nar "Fuuto mengerjap kaget di balik kacamatanya, lalu tetap tidak langsung melepaskan tangannya dari maket tersebut. Ia menoleh menatap Nagisa terlebih dahulu, menyerahkan keputusan sepenuhnya kepada Nagisa tentang siapa yang ia inginkan membantu di mejanya."
            "Fuuto" "Sebenarnya tugasku sendiri sudah hampir selesai kok, aku nggak keberatan nunggu sampai lemnya kering, Sakurajima-san. Tapi kalau memang mau digantikan..."
            nagisa "Eh? Chiasa mau bantu? Sebenarnya kalau kamu mau bantu, masih ada potongan atap di sebelah kanan itu sih. Tapi... ya sudah deh, kamu gantiin tahan sisi dinding timur ini sebentar ya."
            nar "Begitu mendengar persetujuan Nagisa, Fuuto mengangguk tenang dan menggeser jari-jarinya satu per satu secara hati-hati saat kedua tanganmu mengambil alih menahan dinding karton tersebut."
            "Fuuto" "Tekan bagian tengahnya pelan aja ya, Amamiya-san. Kalau nanti butuh bantuan potong bagian lain, panggil aja ya, Sakurajima-san. Aku ke meja belakang dulu."
            nagisa "Oke, makasih banyak ya, Mochizuki!"
            nar "Setelah Fuuto menyingkir kembali ke mejanya, Nagisa menunduk merapikan sisa lem di sudut bawah sambil melirik tanganmu dengan senyum kecil yang berusaha ia sembunyikan."
            nagisa "Tumben banget kamu langsung maju ngambil alih kerjaan orang, Chiasa. Tahan yang lurus lho ya, jangan sampai goyang!"
            chiasa "Iya, ini sudah kutahan lurus kok, Nagisa-senpai. Tangan kiriku nggak gerak sama sekali."
            nagisa "Bagus. Tunggu dua menit lagi sampai lemnya bening, habis itu baru bantu aku cek bagian atapnya."
            chiasa "Bagian atapnya pakai karton abu-abu yang sudah dipotong di sudut meja itu ya, Senpai?"
            nagisa "Iya, yang itu. Nanti tinggal kita pasang lis pinggirannya saja."
            nar "Meskipun mulutnya tetap memberi instruksi cerewet soal posisi jari, rona tipis di pipi Nagisa menunjukkan ia cukup senang melihatmu berebut ingin membantunya."
        else:
            nar "Alih-alih duduk menunggu di pinggir, kamu langsung melangkah menghampiri sisi meja tempat Fuuto berdiri dan menunjuk dinding karton yang sedang ia tahan."
            yutaka "Mochizuki pasti masih ada kerjaan maket sendiri kan di meja belakang? Sini biar aku aja yang gantiin nahan bagian dinding ini, biar kamu nggak keteteran sama tugasmu sendiri."
            nar "Fuuto tidak langsung menarik tangannya. Ia melirik ke arah Nagisa lebih dulu dengan tenang, memastikan apakah Nagisa memang ingin berganti orang atau tidak."
            "Fuuto" "Punyaku tinggal tahap akhir kok, Sakurajima-san, aku nggak masalah nahanin ini sebentar lagi. Tapi kalau temanmu mau gantian..."
            nagisa "Eh? Kalau kamu mau ikut bantu, sebenarnya masih ada bagian tangga di sebelah sana sih, Yutaka. Tapi... ya sudah, sini kamu tahan dinding yang ini dulu aja sampai kering."
            nar "Setelah Nagisa mengiyakan, barulah Fuuto melepaskan tumpuan jarinya perlahan-lahan begitu tanganmu menggantikan posisinya menahan karton tersebut."
            "Fuuto" "Jangan ditekan terlalu keras ke dalam ya, Kisaragi-san. Kalau butuh apa-apa lagi panggil aja di belakang ya, Sakurajima-san."
            nagisa "Siap, makasih banyak tadi, Mochizuki!"
            nar "Begitu Fuuto kembali ke meja kerjanya di baris belakang, Nagisa melirik ke arahmu sambil menahan senyum tipis di sudut bibirnya."
            nagisa "Tumben banget seorang Kisaragi Yutaka rajin nawarin diri sampai nyuruh orang minggir. Pegang yang stabil ya, kalau sampai miring setengah milimeter aja kamu yang harus potong ulang!"
            yutaka "Tenang aja, tanganku stabil kok. Nggak bakal miring."
            nagisa "Tunggu dua menit lagi sampai lemnya kencang, habis itu sekalian bantu aku rapikan potongan tangga di sebelah kanan."
            yutaka "Potongan anak tangga kecil yang berjejer di atas tatakan kertas biru itu kan?"
            nagisa "Iya, nanti tinggal ditempel satu-satu pakai ujung pinset."
            nar "Ia kembali menunduk memeriksa sambungan lem dengan pinsetnya, tampak jelas merasa senang karena kamu tidak rela membiarkan orang lain yang membantunya."
    else:
        if kk_host == "chiasa":
            nar "Kamu berhenti tepat di pinggir meja kerja itu, menatap tangan Fuuto yang menahan maket, lalu menatap Nagisa dengan raut wajah serius tanpa basa-basi."
            chiasa "Nagisa-senpai... kalau Senpai lagi repot butuh bantuan ngerjain maket kayak begini, sebenarnya aku pengin Senpai minta tolongnya ke aku juga."
            nar "Pinset besi di tangan Nagisa langsung berhenti bergerak. Di seberang meja, Fuuto ikut mengerjap canggung merasakan perubahan suasana yang begitu mendadak di antara kalian berdua."
            nagisa "H-hah?! Kamu tiba-tiba ngomong apa sih di depan orang, Chiasa?!"
            chiasa "Aku serius, Senpai. Gedung sebelah sama gedung ini kan dekat banget, kalau Senpai kirim pesan minta bantuan tahanin maket atau potong karton, aku kan bisa langsung lari ke sini."
            nar "Wajah Nagisa langsung memerah sampai ke cuping telinganya. Fuuto yang peka membaca situasi segera memeriksa sudut karton di bawah jarinya lalu berdeham pelan."
            "Fuuto" "Ehm... Sakurajima-san, kayaknya lem di dinding timur ini sudah cukup kering dan kuat kok. Aku balik ke mejaku di belakang dulu ya. Permisi, Amamiya-san."
            nar "Fuuto melepas tangannya dengan sopan lalu melangkah cepat kembali ke mejanya sendiri. Begitu tinggal kalian berdua di meja tengah, Nagisa langsung membuang muka sedikit sambil merapikan penggarisnya dengan gerakan gugup."
            nagisa "K-kenapa kamu nggak pernah bilang dari kemarin-kemarin coba?! Aku kan mikirnya kamu sibuk sama tugas lukismu sendiri, jadi mana berani aku ganggu nyuruh-nyuruh ke sini."
            chiasa "Makanya sekarang kubilang nggak bakal ganggu. Kalau Senpai butuh sepasang tangan tambahan, kirim pesan aja ke aku."
            nagisa "Huh, ngomongnya gampang sekali... ya sudah, pegang kata-katamu sendiri ya."
            chiasa "Pasti. Jadi bagian mana lagi yang belum selesai sekarang, Senpai?"
            nagisa "...Nih, tolong potongin kertas karton tipis buat bingkai jendela yang sudah kugarisin pensil ini. Awas ya kalau potongannya miring!"
            chiasa "Siap, kukerjakan serapi mungkin."
            nagisa "Kalau tanganmu pegal waktu menekan cutter-nya, berhenti dulu sebentar biar garisnya nggak melenceng."
            chiasa "Tenang saja, Senpai, aku sudah biasa memotong kertas tebal buat alas kanvas di studio."
            nar "Nagisa menggeser lampu belajar mejanya sedikit ke arahmu supaya garis pensil di atas karton putih itu terlihat lebih jelas."
            nar "Ia menyodorkan lembaran karton dan pisau cutter cadangan kepadamu dengan pipi yang masih bersemu merah, dan sepanjang setengah jam berikutnya ia jauh lebih sering melirik ke arah tanganmu daripada memeriksa maketnya sendiri."
        else:
            nar "Kamu berdiri di tepi meja kerja itu, melirik maket yang sedang dikerjakan berdua tersebut, lalu menatap Nagisa lurus-lurus tanpa nada bercanda sedikit pun."
            yutaka "Kalau kamu lagi kerepotan butuh bantuan ngerjain maket kayak gini, sebenarnya aku pengin kamu minta tolongnya ke aku juga, Nagisa."
            nar "Tangan Nagisa yang sedang memegang pinset langsung membeku. Di seberang meja, Fuuto ikut mengerjap kikuk melihat tatapanmu yang begitu serius ke arah Nagisa."
            nagisa "H-hah?! Apaan sih kamu tiba-tiba ngomong gitu di studio, Yutaka?!"
            yutaka "Aku serius. Dari gedung kuliahku ke sini kan nggak sampai lima menit jalan kaki. Kalau kamu butuh orang buat bantu nahan maket atau lembur potong bahan, tinggal telepon atau kirim pesan aja ke aku."
            nar "Rona merah langsung menjalar naik ke pipi dan telinga Nagisa. Fuuto yang langsung menangkap suasana pribadi di meja itu segera menarik tangannya perlahan dari dinding maket yang sudah berdiri kokoh."
            "Fuuto" "Ehm... lem bagian dinding ini kayaknya sudah kering sempurna kok, Sakurajima-san. Aku kembali ke meja kerjaku di belakang dulu ya. Permisi, Kisaragi-san."
            nar "Setelah Fuuto menyingkir dengan sopan ke ujung ruangan, Nagisa langsung mendengus pelan sambil menghindari kontak mata langsung denganmu."
            nagisa "Kenapa baru ngomong sekarang coba? Selama ini kan aku mikir kamu paling malas kalau disuruh berurusan sama kerjaan tangan yang ribet begini, makanya aku nggak enak minta tolong."
            yutaka "Kalau kamu yang minta tolong ya nggak bakal kutolak. Lain kali panggil aku duluan."
            nagisa "Iya, iya, nggak usah diulang-ulang keras-keras di ruangan begini! Sekarang bagian mana yang mau kamu bantu?"
            yutaka "Kasih aja yang paling lama dikerjakan."
            nagisa "...Nih, tolong iris bagian lis jendela yang sudah kutandain pakai pensil ini. Ikutin penggaris besinya yang bener, jangan sampai melenceng!"
            yutaka "Beres, serahkan padaku."
            nagisa "Pakai alas potong hijau yang di sebelah kanan itu supaya mata pisau cutter-nya nggak cepat tumpul kena meja kayu."
            yutaka "Siap, alas potongnya sudah kupasang di bawah karton."
            nar "Nagisa menarik kursi kayu cadangan ke tepat di sebelah kursinya sendiri agar kamu tidak perlu membungkuk terlalu lama saat memotong."
            nar "Nagisa menyerahkan lembaran karton dan cutter cadangan itu dengan wajah yang masih merah, dan sepanjang tiga puluh menit berikutnya di meja studio, pandangannya berkali-kali mencuri lihat ke arahmu."
    return

# ┌─ PANDUAN CERITA · N-D01 · Rematch Jam Dua
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Sakurajima Nagisa
# │ AWALAN  : Larut atau Dini Hari; Aff Sedang
# │ INTI    : A Main sampai pagi / B tidur / C biarkan ia menang
# │ AKHIRAN : Intim + dan utang tidur; menang tipis yang jujur menaikkan gengsi; ketahuan mengalah menurunkannya
# └─ tulis / perbaiki dialog di bawah ──
label kk_phone_rematch:
    if not kk_phone_event():
        return
    $ _msg = KK_DYN_BY_ID["N-D01"]
    play sound "audio/sfx/phone_buzz.wav"
    nar "Menjelang pukul dua dini hari, layar ponselmu menyala dua kali berturut-turut di tengah kamar yang gelap. Pesan pertama datang dari Nagisa membawa tautan ruang permainan daring, lalu tiga detik kemudian pesan kedua menyusul karena ia tampaknya mengira pesan pertama tidak masuk."
    if kk_host == "chiasa":
        "Pesan Nagisa" "Chiasa, masih melek kan? Satu ronde lagi aja. Aku baru sadar di mana letak salahku pas tanding kemarin, kali ini jangan kabur duluan sebelum kubalas."
        chiasa "Jam dua pagi masih nyari tanding ulang, Nagisa-senpai? Kamu belum tidur dari tadi?"
        play sound "audio/sfx/phone_buzz.wav"
        "Pesan Nagisa" "Habis beresin gambar, terus kepikiran skor kemarin jadi nggak bisa merem! Cepat masuk ruangnya, aku sudah siapkan kursinya nih."
    else:
        "Pesan Nagisa" "Yutaka, masih melek kan? Satu pertandingan lagi sekarang. Aku baru sadar salah langkahku kemarin di mana, jangan kabur dulu sebelum kubuktikan."
        yutaka "Ini jam dua pagi lho, Nagisa. Kamu serius nggak bisa tidur cuma gara-gara mikirin skor pertandingan kemarin?"
        play sound "audio/sfx/phone_buzz.wav"
        "Pesan Nagisa" "Berisik! Habis beresin tugas gambar terus kepikiran, jadinya kesel sendiri! Cepat buka aplikasinya, ruangnya sudah kubuka."
    $ _opts = [(caption, Return(i), False) for i, caption in enumerate(_msg["choices"])]
    call screen kk_choice_panel(_opts, "Pesan dari Nagisa")
    $ _reply = _return
    if kk_record_choice("N-D01", ("A","B","C")[_reply]):
        if _reply == 1:
            if kk_host == "chiasa":
                chiasa "Maaf ya, Nagisa-senpai, mataku sudah berat banget buat melek lagi. Besok aja ya tanding ulangnya, kamu juga cepat istirahat."
                "Pesan Nagisa" "Tch... ya sudah, besok! Tapi jangan jadikan alasan tidur buat kabur dari tantangan ulangku ya, Chiasa."
                "Pesan Nagisa" "Selamat malam. Besok siang nggak ada alasan lagi."
            else:
                yutaka "Besok aja ya, Nagisa. Kalau kuladeni sekarang, besok pagi aku pasti ketiduran di kelas. Kamu juga cepat tidur."
                "Pesan Nagisa" "Ya sudah, besok! Jangan coba-coba menyebut tidur sebagai strategi buat menghindari kekalahanmu ya, Yutaka."
                "Pesan Nagisa" "Selamat malam. Jangan telat bangun."
            nar "Gurauan singkat itu langsung diikuti ucapan selamat malam yang lebih pendek dan lembut. Kamu mematikan layar ponsel sebelum tubuhmu harus membayar harga begadang yang terlalu mahal."
        else:
            if _reply == 2:
                nar "Kamu masuk ke ruang permainan dan sengaja memperlambat refleks beberapa detik di babak penentuan agar serangan terakhir Nagisa masuk dengan mulus. Layar langsung menampilkan kemenangan untuk akunnya, tetapi ruang obrolan suara di headset justru hening dua detik."
                if kk_host == "chiasa":
                    nagisa "Tunggu dulu, Chiasa. Kamu barusan sengaja kalah ya? Pertahananmu di pojok kiri biasanya nggak selonggar itu. Aku nggak minta dikasih hadiah kemenangan!"
                    chiasa "Eh, ketahuan ya? Habisnya sudah malam banget, aku kira kalau kamu menang sekali bisa langsung lega terus tidur."
                    nagisa "Mana ada lega kalau dikasih begitu! Ulang lagi sekarang, main yang benar sampai selesai! Nggak usah pakai rasa kasihan segala!"
                else:
                    nagisa "Hei, Yutaka. Kamu barusan sengaja mengalah ya? Cara mainmu beda banget sama kemarin, tadi kamu jelas-jelas bisa blokir langkahku. Aku nggak minta dikasih menang!"
                    yutaka "Ketahuan juga ya. Kupikir kalau rondenya cepat beres kamu bisa langsung istirahat."
                    nagisa "Enak aja! Menang hasil dikasih begini malah bikin makin nggak bisa tidur! Mulai ulang sekarang, kali ini jangan berani-berani nahan tangan lagi!"
                nar "Kemenangan palsu yang tadi kamu berikan demi cepat mengakhiri malam justru membuatnya menuntut tanding ulang ronde demi ronde hingga langit di luar jendela mulai membiru pucat."
            else:
                nar "Kamu menegakkan duduk, memasang headset, dan meladeni setiap serangannya dengan serius hingga skor saling kejar sampai menit terakhir. Saat poin kemenangan akhirnya jatuh tipis ke sisimu, suara protes Nagisa langsung meledak pelan di balik mikrofon."
                if kk_host == "chiasa":
                    nagisa "Argh, tipis banget! Satu detik lagi padahal seranganku masuk! Jangan besar kepala dulu ya, Chiasa, ulang satu ronde lagi!"
                    chiasa "Tadi bilangnya cuma satu ronde lho, Nagisa-senpai. Tapi boleh deh, ayo satu lagi."
                    nagisa "Hahaha, iya, iya, aku lupa! Tapi ronde ini serius bakal kubalikkan!"
                else:
                    nagisa "Argh, beda tipis banget! Tadi satu langkah lagi padahal kena! Menang tipis jangan besar kepala ya, Yutaka. Ulang!"
                    yutaka "Katanya tadi cuma satu pertandingan, Nagisa. Tapi kalau kamu masih penasaran, ayo kuladeni lagi."
                    nagisa "Hahaha, diam deh! Ronde ini nggak bakal kulepas lagi!"
                nar "Satu pertandingan meluas menjadi lima ronde beruntun. Di sela omelan dan adu strategi, terdengar tawa lepas Nagisa yang jarang muncul pada siang hari di kampus. Ketika kalian akhirnya sepakat berhenti, fajar sudah dekat dan rasa kantuk datang bersama keakraban baru."
            $ kk_minutes((6 - kk_slot) * 240 - kk_minute)
    return

init python:
    KK_DYN_BY_ID = {event["id"]: event for event in KK_EVENTS_DYN}

    def kk_can_sketch(place):
        return kk_host == "chiasa" and place == "Rumah Amamiya" and kk_slot in (3,4,5)

    def kk_art_studio_open(place):
        return (kk_host == "chiasa" and place == "Gedung Seni Rupa & Studio"
                and kk_slot == 2 and kk_date().weekday() < 5
                and (kk_has("haruka_dimintai_bantuan") or kk_get("kemampuan_gambar") >= 30
                     or kk_comparison_due()))

    def kk_comparison_due():
        return kk_host == "chiasa" and kk_get("shena_risiko",20) >= 40 and not kk_done("C-D02")

    def kk_shaking_hands():
        return kk_host == "chiasa" and kk_kelelahan_tier()[1] >= 2 and not kk_done("C-D03")

    def kk_father_visit(place):
        return (kk_host == "yutaka" and place == "Apartemen Yutaka" and kk_slot == 3
                and kk_family_bond() < 40 and not kk_done("Y-D03"))

    def kk_mother_message():
        return (kk_host == "yutaka" and kk_slot == 3 and kk_family_bond() >= 40
                and not kk_done("Y-D08") and "Y-D08" not in kk_missed)

    def kk_phone_event():
        return (not kk_done("N-D01") and "N-D01" not in kk_missed and
                kk_slot in (4,5) and kk_rel_get("nagisa","aff") >= 25)

    def kk_can_skip():
        return not kk_graduated and (kk_elapsed_days >= 7 or kk_has("q01_complete"))

    def kk_skip_week():
        if not kk_can_skip():
            return
        if any(p[0] == kk_elapsed_days for p in kk_promises.values()):
            return
        for day in range(7):
            kk_new_day()
            if (kk_graduated or kk_is_hanami_date() or (kk_bulan, kk_hari_n) in ((2,3),(5,9))
                    or any(p[0] == kk_elapsed_days for p in kk_promises.values())):
                break
        store.kk_slot = 0
        store.kk_minute = 0

    def kk_is_hanami_date():
        return kk_bulan == 1 and kk_hari_n in (19,20)

    def kk_mio_message():
        return (kk_host == "chiasa" and kk_has("proyek_mio_diterima")
                and not kk_done("C-D07") and "C-D07" not in kk_missed
                and kk_slot == 4 and 60 <= kk_minute < 120)

    def kk_incoming_messages():
        # One ordering for awake play and bedside phone modes.
        return [(cid, eid, label) for cid, eid, label, ready in (
            ("nagisa", "N-D01", "kk_phone_rematch", kk_phone_event),
            ("miyuki", "Mi-D01", "kk_pudding", kk_pudding_message),
            ("ibu_kisaragi", "Y-D08", "kk_message_kisaragi", kk_mother_message),
            ("mio", "C-D07", "kk_mio_deadline", kk_mio_message),
        ) if ready()]

    def kk_sleep(minutes=480):
        # Wake on the same simulated clock used by the phone, including midnight.
        slept = 0
        message = None
        while slept < minutes and not kk_graduated:
            for cid, eid, label in kk_incoming_messages():
                if kk_phone_mode == "siaga" or (kk_phone_mode == "normal" and cid in kk_priority_contacts):
                    message = cid
                    break
                if eid not in kk_missed:
                    store.kk_missed.append(eid)
            if message:
                break
            step = min(minutes - slept, 60 - kk_minute % 60)
            kk_minutes(step, sleeping=True)
            slept += step
        energy, store.kk_rest_energy_minutes = divmod(kk_rest_energy_minutes + slept, 40)
        debt, store.kk_rest_debt_minutes = divmod(kk_rest_debt_minutes + slept, 60)
        kk_adj_body("energi", energy)
        kk_adj_body("utang_tidur", -debt)
        return message

    def kk_moeka_ending():
        # Rute Moeka: digerbang flag distingtif (krisis/Kuga/pemulihan/donor).
        if kk_has("force_moeka"):
            return "E-MO-11"
        if kk_has("moeka_kehilangan"):
            return "E-MO-04"
        if kk_has("moeka_donor_didampingi"):
            return "E-MO-13"
        if kk_has("moeka_selamat"):
            if (kk_has("moeka_intervensi_1") and kk_get("andalan_moeka",0) >= 40
                    and not kk_has("force_pernah")):
                return "E-MO-01"
            if kk_get("topeng_moeka",0) >= 70 and kk_get("andalan_moeka",0) >= 50:
                return "E-MO-03"
            if kk_has("beasiswa_terancam") and not kk_has("moeka_beasiswa_dibantu"):
                return "E-MO-02"
            if not kk_has("moeka_intervensi_1") and kk_has("rina_sekutu"):
                return "E-MO-12"
            return "E-MO-06" if kk_has("rina_sekutu") else "E-MO-05"
        if kk_has("kuga_kontrak_terikat"):
            return "E-MO-07"
        if kk_has("moeka_ayah_meninggal"):
            return "E-MO-10"
        if kk_has("moeka_jalan_keluar") or kk_has("moeka_kerja_aman"):
            return "E-MO-08" if kk_has("rina_sekutu") else "E-MO-09"
        return None

    def kk_shiori_route_ending():
        # Rute Shiori endgame: digerbang flag distingtif skakmat/sekutu/Tojo/Shena.
        if kk_has("force_shiori_pelaku"):
            return "E-SH-11"
        if (kk_get("respek_shiori",0) >= 80 and kk_rel_get("shiori","trust") >= 80
                and kk_has("shiori_langkah_jujur") and not kk_has("force_pernah")):
            return "E-SH-01"
        if kk_has("shiori_sekutu_akhir"):
            return "E-SH-06"
        if kk_has("shiori_sekutu_musuh") and (kk_has("bukti_kuga_terkumpul") or kk_has("ogawa_dihentikan")):
            return "E-SH-10"
        if kk_has("shena_terbongkar") and kk_get("respek_shiori",0) >= 70:
            return "E-SH-14"
        if kk_has("shena_diakui_chiasa") and kk_get("respek_shiori",0) >= 70:
            return "E-SH-12"
        if kk_has("shiori_cinta_koita_dikenal") and kk_has("koita_pilih_shiori"):
            return "E-SH-05"
        if kk_has("shiori_pemain_mengaku"):
            return "E-SH-03"
        if kk_has("shiori_skakmat_dibalas"):
            return "E-SH-02"
        if kk_has("shiori_skakmat_menyerah"):
            return "E-SH-15"
        if kk_has("shiori_senyum_dinikmati"):
            return "E-SH-16"
        if kk_has("shiori_sasaran_koita"):
            return "E-SH-09"
        if stage.get("shiori",0) >= 5 and not kk_has("shiori_sekutu_akhir"):
            return "E-SH-04"
        if kk_has("tojo_bidak"):
            return "E-SH-08"
        return None

    def kk_koita_route_ending():
        # Rute Koita: pilihan K26 + keruntuhan -> pemulihan + manuver balik.
        if kk_has("koita_pilih_chiasa") or kk_has("koita_success_tuntas"):
            return "E-KO-06"
        if kk_has("koita_pilih_miyuki"):
            return "E-KO-01"
        if kk_has("koita_pilih_nagisa"):
            return "E-KO-02"
        if kk_has("koita_pilih_harumi"):
            return "E-KO-03"
        if kk_has("koita_pilih_moeka"):
            return "E-KO-04"
        if kk_has("koita_pilih_shiori_"):
            return "E-KO-05"
        if kk_has("koita_dituduh_chiasa") and runtuh_koita >= 80:
            return "E-KO-21"
        if kk_has("koita_menyaksikan_force") and kk_rel_get("koita","trust") >= 40:
            return "E-KO-19"
        if kk_has("koita_tahu_pelaku") and not runtuh_koita >= 70:
            return "E-KO-14"
        if kk_has("koita_tahu_naskah_percaya"):
            return "E-KO-13"
        if kk_has("koita_berbalik"):
            return "E-KO-10"
        if kk_has("koita_rapat_dibalik") and orbit_koita <= 0:
            return "E-KO-17"
        if kk_has("plot_armor_padam") and orbit_koita <= 0:
            return "E-KO-18" if kk_has("koita_tahu_naskah_percaya") else "E-KO-16"
        if kk_has("naskah_koita_disabotase") or kk_has("koita_runtuh_tahun3"):
            return "E-KO-15"
        if runtuh_koita >= 70:
            if kk_has("koita_ke_konselor") or kk_has("yoshie_pulang"):
                return "E-KO-07"
            if kk_has("naskah_koita_diselamatkan"):
                return "E-KO-11"
            return "E-KO-09"
        if kk_has("saksi_koita_berdiri"):
            return "E-KO-20"
        if kk_has("koita_pergi_didukung"):
            return "E-KO-12"
        if kk_has("koita_pola_tak_terbongkar") and kk_bulan >= 36:
            return "E-KO-08"
        return None

    def kk_bl_ending():
        # Rute BL (Koita x Yutaka): digerbang koita_arah_bl + pilihan B6 (non-eksplisit).
        if not kk_has("koita_arah_bl"):
            return None
        if kk_has("bl_b6_memilih"):
            if kk_has("bl_keluarga_menerima"):
                return "E-BL-06"
            if kk_has("bl_keluarga_menolak"):
                return "E-BL-07"
            if kk_has("bl_disembunyikan"):
                return "E-BL-05"
            return "E-BL-01"
        if kk_has("bl_b6_menolak"):
            return "E-BL-02"
        if kk_has("bl_b6_lari"):
            return "E-BL-08" if kk_has("bl_tanpa_kehangatan") else "E-BL-03"
        if kk_has("bl_semua_mundur"):
            return "E-BL-04"
        return None

    def kk_yutaka_route_ending():
        # Rute Yutaka-NPC mengejar Chiasa: digerbang yutaka_harap + flag pengakuan.
        if kk_has("yutaka_memperalat_ketahuan"):
            return "E-YU-05"
        if kk_has("yutaka_bela_koita"):
            return "E-YU-06"
        if kk_has("yutaka_ditanggapi") and kk_has("chiasa_menerima_yutaka"):
            return "E-YU-01"
        if kk_has("chiasa_jujur_yutaka"):
            return "E-YU-04"
        if kk_has("yutaka_ditolak_candaan") or kk_has("chiasa_menolak_gantung"):
            return "E-YU-03"
        if kk_has("yutaka_mundur_koita"):
            return "E-YU-02"
        if kk_has("keluarga_kisaragi_menekan") and not kk_has("chiasa_hadir_m31"):
            return "E-YU-07"
        if kk_has("chiasa_menolak_konsisten"):
            return "E-YU-08"
        return None

    def kk_chiasa_route_ending():
        # Rute Chiasa (host Chiasa / Female Route): digerbang flag rute.
        if kk_has("force_chiasa"):
            return "E-CH-09"
        if kk_has("chiasa_dipakai_menyakiti_ketahuan"):
            return "E-CH-11"
        if kk_has("koita_success_tuntas"):
            if kk_has("keluarga_menerima_success"):
                return "E-CH-02"
            if kk_has("keluarga_menolak_keras"):
                return "E-CH-04"
            if kk_has("koita_kembali_pola"):
                return "E-CH-05"
            return "E-CH-03"
        if kk_has("rute_bl_berhasil") and not kk_has("chiasa_didekati"):
            return "E-CH-08" if kk_has("yutaka_jujur_chiasa") else "E-CH-07"
        if kk_has("chiasa_yutaka_menerima"):
            return "E-CH-01"
        if kk_has("chiasa_fokus_seni"):
            return "E-CH-06"
        if kk_has("chiasa_adik_kembali"):
            return "E-CH-10"
        return None

    def kk_force_ending():
        # Ending KONSEKUENSI Force: hanya memilih kode akibat yang dicatat flag;
        # teks berasal dari katalog. Tidak ada metode. Digerbang force_pernah.
        if not kk_has("force_pernah"):
            return None
        if kk_has("force_pembalikan_terbongkar"):
            return "E-FO-15"
        if kk_has("force_disaksikan_koita"):
            if kk_has("korban_melapor") or kk_rel_get("koita","trust") >= 60:
                return "E-FO-11"
            if kk_has("koita_diam_takut"):
                return "E-FO-14"
            return "E-FO-13"
        if kk_has("force_kejahatan_berantai"):
            return "E-FO-09"
        if kk_has("force_dilaporkan") or kk_has("bukti_force_kuat"):
            return "E-FO-01"
        if kk_has("force_bukti_kampus"):
            return "E-FO-02"
        if kk_has("force_pelaku_mengaku"):
            return "E-FO-04"
        if kk_has("force_pelaku_lari"):
            return "E-FO-05"
        if kk_has("force_kerabat_tahu"):
            return "E-FO-06"
        if kk_has("force_saksi_memeras"):
            return "E-FO-07"
        if kk_has("force_kasus_dibuka"):
            return "E-FO-08"
        if kk_has("force_korban_terikat"):
            return "E-FO-12"
        if kk_has("force_ringan"):
            return "E-FO-10"
        if kk_has("force_bersih"):
            return "E-FO-03"
        return None

    def kk_npc_ending():
        # Ending NPC: digerbang flag arc/romansa NPC spesifik (banyak dorman).
        if kk_has("penyusup_ogawa"):
            return "E-NPC-27" if kk_has("penyamaran_terlalu_lama") else "E-NPC-26"
        if kk_has("romansa_sena"):
            return "E-NPC-01"
        if kk_has("sena_disakiti_pemain"):
            return "E-NPC-02"
        if kk_has("romansa_rina") and kk_has("moeka_selamat"):
            return "E-NPC-03"
        if kk_has("rina_tak_memaafkan") or (kk_has("moeka_kehilangan") and kk_has("rina_sekutu")):
            return "E-NPC-04"
        if kk_has("romansa_haruka"):
            return "E-NPC-05"
        if kk_has("haruka_tahu_shena"):
            return "E-NPC-06"
        if kk_has("romansa_ayane"):
            return "E-NPC-07"
        if kk_has("ayane_tahu_manipulasi"):
            return "E-NPC-08"
        if kk_has("romansa_mei"):
            return "E-NPC-09"
        if kk_has("mei_dibayar") or kk_has("mei_dibuang"):
            return "E-NPC-10"
        if kk_has("romansa_mio"):
            return "E-NPC-11"
        if kk_has("mio_kontrak_putus"):
            return "E-NPC-12"
        if kk_has("romansa_haruto"):
            return "E-NPC-13"
        if kk_has("haruto_sekutu"):
            return "E-NPC-14"
        if kk_has("romansa_matsuda"):
            return "E-NPC-15"
        if kk_has("matsuda_membongkar"):
            return "E-NPC-16"
        if kk_has("romansa_daichi"):
            return "E-NPC-17"
        if kk_has("romansa_yuuto"):
            return "E-NPC-18"
        if kk_has("romansa_tojo"):
            return "E-NPC-19"
        if kk_has("skandal_omiai_takeru"):
            return "E-NPC-20"
        if kk_has("kerja_tetap_kafe"):
            return "E-NPC-21"
        if kk_has("sato_dikejar_romantis"):
            return "E-NPC-22"
        if kk_has("sato_kyoko_terlibat") or kk_has("konseling_host_rutin"):
            return "E-NPC-23"
        if kk_has("kuroiwa_percaya_penuh") or kk_get("kuroiwa_percaya",0) >= 70:
            return "E-NPC-24"
        if kk_has("hanabusa_dibantu"):
            return "E-NPC-25"
        return None

    def kk_cross_ending():
        # Ending lintas (harem/komposit): digerbang flag/komposit distingtif.
        if kk_has("ntr_sempurna"):
            return "E-X-14"
        if kk_has("rute_yandere_nagisa") and kk_has("shiori_revenge_pemain"):
            return "E-X-12"
        if kk_has("dua_tragedi_distorsi"):
            return "E-X-09"
        if kk_has("mei_terbit_semua"):
            return "E-X-10"
        if kk_has("harem_terbongkar_serentak"):
            return "E-X-01"
        if kk_has("domino_shiori"):
            return "E-X-03"
        if kk_has("harem_terbuka_disepakati"):
            return "E-X-02"
        if kk_has("sistem_dibuka_semua_m35"):
            return "E-X-08"
        if kk_has("melawan_naskah_bersama"):
            return "E-X-07"
        if kk_has("pesta_amamiya_pulih"):
            return "E-X-11"
        if kk_has("semua_bebas_mandiri"):
            return "E-X-06"
        if kk_has("tubuh_dibayar_tiga") or kk_has("menyelamatkan_tiga_distorsi"):
            return "E-X-13"
        if kk_has("kursi_kosong_wisuda") or (orbit_koita <= 0 and kk_has("semua_lepas_koita")):
            return "E-X-05"
        if kk_has("moeka_kehilangan"):
            return "E-X-04"
        return None

    def kk_epilogue():
        result = [kk_resolve_ending()]
        if result == ["E-SI-05"] and (kk_done_kindness()):
            result = ["E-SI-13"]
        # Katalog §1: jangan menggambarkan karier host masa depan setelah kematian.
        miyuki = kk_miyuki_ending()
        nagisa = kk_nagisa_ending()
        partners = int(miyuki in ("E-MI-05","E-MI-13","E-MI-01")) + int(nagisa == "E-NA-01")
        harumi = kk_harumi_ending()
        partners += int(harumi == "E-HA-01")
        if partners:
            result.append("E-HP-02" if partners > 1 else "E-HP-01")
        elif kk_has("ditinggalkan_semua"):
            result.append("E-HP-04")
        elif kk_has("mengejar_tapi_kosong"):
            result.append("E-HP-03")
        elif not any(kk_has(f) for f in ("romansa_dimulai","chiasa_yutaka_saja")):
            result.append("E-HP-05")
        if kk_has("pengakuan_terlambat"):
            result.append("E-HP-06")
        if kk_has("patah_hati_diterima"):
            result.append("E-HP-07")
        if kk_host == "chiasa" and kk_has("shiori_menemukan_kebohongan_shena"):
            result.append("E-SH-13")
        elif kk_has("shiori_warisan_didukung") and stage.get("shiori",0) < 2 and not kk_has("force_shiori"):
            result.append("E-SH-07")
        if nagisa:
            result.append(nagisa)
        if miyuki:
            result.append(miyuki)
        if harumi:
            result.append(harumi)
        for _fn in (kk_moeka_ending, kk_shiori_route_ending, kk_koita_route_ending,
                    kk_bl_ending, kk_yutaka_route_ending, kk_chiasa_route_ending,
                    kk_force_ending, kk_npc_ending, kk_cross_ending):
            _e = _fn()
            if _e and _e not in result:
                result.append(_e)
        if result[0] in ("E-SI-01","E-SI-02","E-SI-03","E-SI-18"):
            if kk_host == "chiasa" and partners:
                result.append("E-CF-01")
            if kk_host == "yutaka" and kk_has("job_family") and kk_family_bond() >= 60:
                result.append("E-YH-01")
            elif kk_yutaka_relation_ending():
                result.append(kk_yutaka_relation_ending())
            elif kk_host == "yutaka" and kk_has("job_outside"):
                result.append("E-YH-02")
            elif kk_host == "yutaka" and kk_has("intern_abroad"):
                result.append("E-YH-06")
            elif kk_host == "chiasa" and kk_get("kemampuan_gambar") >= 80:
                result.append("E-CF-08")
            elif kk_host == "chiasa" and "E-HP-05" in result:
                result.append("E-CF-10")
        # --- E-CF / E-YH tambahan: digerbang flag rute distingtif (dorman di happy-path) ---
        if kk_has("koita_success_tuntas"):
            if kk_has("keluarga_menerima_success"):
                result.append("E-CF-02")
            elif kk_has("keluarga_memisahkan"):
                result.append("E-CF-04")
            elif kk_has("koita_kembali_pola"):
                result.append("E-CF-05")
            else:
                result.append("E-CF-03")
        if kk_has("chiasa_yutaka_bersama"):
            result.append("E-CF-06")
        if kk_has("shena_terbongkar_bohong"):
            result.append("E-CF-07")
        if kk_has("amamiya_retak"):
            result.append("E-CF-09")
        if kk_has("yuri_terbongkar_banyak"):
            result.append("E-CF-11")
        if kk_has("framing_bertahan") and kk_get("nurani_chiasa",0) < 70:
            result.append("E-CF-12")
        if kk_has("framing_dicabut_sendiri") and kk_get("nurani_chiasa",0) >= 70:
            result.append("E-CF-13")
        if kk_has("kisaragi_dicoret"):
            result.append("E-YH-04")
        if kk_has("ketahuan_bukan_yutaka") or kk_get("curiga_identitas",0) >= 80:
            result.append("E-YH-05")
        if kk_has("daichi_penagih"):
            result.append("E-YH-07")
        return result

    def kk_done_kindness():
        return any((c["ev"],c["key"]) in (("Mi03","A"),("N03","A")) for c in choices_log)


    def kk_pudding_message():
        return (kk_slot == 4 and kk_minute >= 60 and kk_minute < 120 and
                not kk_done("Mi-D01") and "Mi-D01" not in kk_missed and kk_rel_get("miyuki","trust") >= 25 and
                kk_get("dimanja_miyuki",10) >= 50)

    def kk_desk_event(place):
        home = "Apartemen Yutaka" if kk_host == "yutaka" else "Rumah Amamiya"
        if place != home:
            return None
        if kk_bulan == 34 and kk_has("haruto_lawan") and not kk_done("N23"):
            return "N23"
        if kk_has("koko_di_meja") and not kk_done("N-D09"):
            return "N-D09"
        return None

    def kk_can_sit_with_miyuki(place):
        return (place == "Perpustakaan Pusat" and kk_daily_place("miyuki") == place
                and kk_get("kelelahan_miyuki",35) >= 60 and not kk_done("Mi-D02"))

    def kk_unfinished_board(place):
        return (place == "Klub Catur" and stage.get("shiori",0) == 3
                and kk_daily_place("shiori") != place and not kk_done("S-D09"))

    def kk_social_event(cid, place):
        if kk_daily_place(cid) != place:
            return None
        if (cid == "shiori" and kk_get("daftar_kebohongan_shiori") >= 1
                and not kk_done("S-D04") and not kk_done("S13")):
            return "S-D04"
        if (cid == "shiori" and place == "Rumah Saionji" and not kk_done("S-D08")
                and kk_elapsed_days > kk_npc_rel.get("hari_natal_saionji", kk_elapsed_days)):
            return "S-D08"
        if cid == "shiori":
            if kk_get("bukti_terkumpul",0) >= 50 and not kk_done("S-D17"):
                return "S-D17"
            if kk_get("marah_shiori",0) >= 60 and not kk_done("S-D15"):
                return "S-D15"
            if kk_get("marah_koita",0) >= 40 and not kk_done("S-D07"):
                return "S-D07"
            if kk_get("senyum_terbaca",0) >= 40 and not kk_done("S-D16"):
                return "S-D16"
            if kk_get("respek_shiori",0) >= 60 and not kk_done("S-D03"):
                return "S-D03"
            if (kk_rel_get("shiori","trust") >= 30 and not kk_done("S-D14")
                    and not kk_done("S-D13")):
                return "S-D14"
            if kk_rel_get("shiori","trust") >= 30 and not kk_done("S-D13"):
                return "S-D13"
            # --- Batch dinamis Shiori tambahan ---
            if stage.get("shiori",0) >= 4 and not kk_done("S-D12"):
                return "S-D12"
            if (kk_has("ogawa_aktif") or kk_has("bukti_kuga_terkumpul")) and not kk_done("S-D10"):
                return "S-D10"
            if kk_has("tojo_aktif") and not kk_done("S-D06"):
                return "S-D06"
            if (kk_host == "chiasa" and not kk_done("S-D05")
                    and not kk_has("shiori_tahu_shena")
                    and (stage.get("shiori",0) >= 1 or kk_rel_get("shiori","trust") >= 25)
                    and (kk_done("C05") or kk_has("kesan_awal_C01_A") or kk_has("kesan_awal_C01_B")
                         or kk_done("C-D02") or kk_done("C-D03") or kk_done("C-D07"))):
                return "S-D05"
            if stage.get("shiori",0) >= 3 and not kk_done("S-D02"):
                return "S-D02"
            if kk_get("respek_shiori",0) >= 50 and kk_has("shiori_tahu_sistem") and not kk_done("S-D11"):
                return "S-D11"
            if kk_rel_get("shiori","trust") >= 25 and not kk_done("S-D01"):
                return "S-D01"
        if cid == "nagisa":
            if (stage.get("nagisa",0) >= 2 and kk_slot in (4,5)
                    and kk_rel_get("nagisa","aff") >= 30 and not kk_done("N-D04")):
                return "N-D04"
            if stage.get("nagisa",0) >= 4 and not kk_done("N-D09"):
                return "N-D09"
            if (place == "Taman Lingkungan" and kk_slot == 3 and not kk_done("N-D03")
                    and kk_npc_rel.get("hari_harapan_turun") == kk_elapsed_days):
                return "N-D03"
            if (not kk_done("N-D08") and kk_get("gengsi_nagisa",70) >= 60 and
                    any(c["ev"] == "N02" and c["key"] == "B" for c in choices_log)):
                return "N-D08"
            if kk_host == "chiasa" and stage.get("nagisa",0) >= 3 and not kk_done("N-D13"):
                return "N-D13"
            if kk_host == "chiasa" and kk_rel_get("nagisa","intim") >= 40 and not kk_done("N-D12"):
                return "N-D12"
            if (stage.get("nagisa",0) >= 3 and kk_get("kelekatan_nagisa",40) >= 70
                    and not kk_done("N-D06")):
                return "N-D06"
            if (kk_get("kelekatan_nagisa",40) >= 70 and kk_rel_get("nagisa","aff") >= 55
                    and stage.get("nagisa",0) <= 2 and not kk_done("N-D11")):
                return "N-D11"
            if kk_has("haruto_kenal") and kk_slot in (4,5) and not kk_done("N-D07"):
                return "N-D07"
            if kk_rel_get("nagisa","jeal") >= 50 and not kk_done("N-D05"):
                return "N-D05"
            if ("N-D01" in kk_missed and stage.get("nagisa",0) >= 3
                    and not kk_done("N-D10")):
                return "N-D10"
        if cid == "harumi":
            # --- Batch dinamis Harumi (jalur Ogawa + kejelasan/validasi) ---
            if (kk_get("kejelasan_harumi") >= 60 and kk_has("ogawa_aktif")
                    and kk_get("validasi_pemain",0) >= 40 and not kk_done("H-D08")):
                return "H-D08"
            if (kk_get("kejelasan_harumi") >= 50 and kk_rel_get("harumi","intim") >= 50
                    and not kk_done("H-D11")):
                return "H-D11"
            if kk_host == "chiasa" and stage.get("harumi",0) >= 2 and not kk_done("H-D12"):
                return "H-D12"
            if kk_has("ogawa_aktif") and kk_get("cengkeraman_ogawa",0) >= 40 and kk_slot in (4,5) and not kk_done("H-D03"):
                return "H-D03"
            if kk_has("ogawa_aktif") and stage.get("harumi",0) >= 4 and not kk_done("H-D06"):
                return "H-D06"
            if kk_has("ogawa_aktif") and stage.get("harumi",0) >= 3 and not kk_done("H-D09"):
                return "H-D09"
            if kk_has("ogawa_aktif") and not kk_done("H-D04"):
                return "H-D04"
            if kk_has("ogawa_aktif") and not kk_done("H-D02"):
                return "H-D02"
            if stage.get("harumi",0) >= 3 and kk_get("rumor_harumi",0) >= 20 and not kk_done("H-D10"):
                return "H-D10"
        if (cid == "harumi" and place == "Perpustakaan Pusat" and not kk_done("H-D07")
                and any(c["ev"] == "H10" and c["key"] == "A" for c in choices_log)):
            return "H-D07"
        if cid == "harumi" and place == "Asrama Putri" and kk_slot == 3 and not kk_done("H-D05"):
            if any(c["ev"] == "H03" and c["key"] == "C" for c in choices_log):
                return "H-D05"
        if cid == "harumi" and place == "Asrama Putri" and kk_slot == 4 and kk_minute >= 180:
            if kk_get("kejelasan_harumi") >= 30 and not kk_done("H-D01"):
                return "H-D01"
        if cid == "nagisa" and kk_slot == 1 and not kk_done("N-D02"):
            if kk_rel_get(cid,"aff") >= 55 and kk_get("gengsi_nagisa",70) >= 50:
                return "N-D02"
        if (cid == "miyuki" and kk_host == "chiasa" and kk_rel_get("miyuki","intim") >= 55
                and not kk_done("Mi-D13")):
            return "Mi-D13"
        if (cid == "miyuki" and place == "Rumah Sakit Tachibana" and kk_bulan == 25
                and kk_rel_get("miyuki","aff") >= 25 and not kk_done("Mi-D09")):
            return "Mi-D09"
        if (cid == "miyuki" and place == "Rumah Sakit Tachibana" and kk_bulan == 30
                and kk_hari_n == 14 and kk_slot in (3,4) and not kk_done("Mi-D11")):
            return "Mi-D11"
        if cid == "miyuki" and not kk_done("Mi-D12") and kk_miyuki_ready_to_refuse():
            return "Mi-D12"
        if cid == "miyuki" and kk_has("puji_pastry") and not kk_done("Mi-D03"):
            if kk_rel_get(cid,"aff") >= 55:
                return "Mi-D03"
        if (cid == "miyuki" and not kk_done("Mi-D04") and kk_hari == "Sabtu" and kk_slot == 4
                and kk_get("omiai_takeru") >= 40):
            return "Mi-D04"
        if (cid == "miyuki" and place == "Rumah Sakit Tachibana" and kk_slot == 5
                and kk_rel_get("miyuki","aff") >= 25
                and kk_get("luka_miyuki_diri",0) >= 50 and not kk_done("Mi-D05")):
            return "Mi-D05"
        if (cid == "miyuki" and place == "Rumah Sakit Tachibana" and kk_slot in (4,5)
                and kk_rel_get("miyuki","aff") >= 25
                and kk_get("kelelahan_miyuki",35) >= 85 and not kk_done("Mi-D10")):
            return "Mi-D10"
        if (cid == "miyuki" and place == "Kafe Komorebi" and kk_hari == "Sabtu"
                and kk_get("omiai_takeru") >= 40 and not kk_done("Mi-D07")):
            return "Mi-D07"
        if (cid == "miyuki" and place != "Rumah Sakit Tachibana"
                and body.get("kesehatan",100) <= 60
                and kk_rel_get("miyuki","aff") >= 25
                and stage.get("miyuki",0) <= 3 and not kk_done("Mi-D14")):
            return "Mi-D14"
        if (cid == "miyuki" and kk_slot in (4,5) and stage.get("miyuki",0) >= 3
                and kk_rel_get("miyuki","aff") >= 25
                and kk_get("luka_miyuki_diri",0) >= 40 and not kk_done("Mi-D06")):
            return "Mi-D06"
        if cid == "koita":
            if kk_slot == 5 and koita_sadar >= 25 and not kk_done("Mi-D08"):
                return "Mi-D08"
            # Fase keruntuhan -> pemulihan diperiksa lebih dulu agar tidak
            # terbayangi event intel awal yang belum dimainkan.
            if runtuh_koita >= 70 and not kk_done("K-D20"):
                return "K-D20"
            if runtuh_koita >= 60 and not kk_done("K-D18"):
                return "K-D18"
            if runtuh_koita >= 60 and not kk_done("K-D19"):
                return "K-D19"
            if (runtuh_koita >= 50 and kk_has("koita_rumor_didorong")
                    and not kk_done("K-D21")):
                return "K-D21"
            if koita_sadar >= 60 and not kk_done("K-D16"):
                return "K-D16"
            if orbit_koita <= 2 and not kk_done("K-D13"):
                return "K-D13"
            if koita_sadar >= 50 and not kk_done("K-D05"):
                return "K-D05"
            if kk_has("koita_akar_diketahui") and not kk_done("K-D09"):
                return "K-D09"
            if kk_bulan >= 13 and not kk_done("K-D08"):
                return "K-D08"
            if kk_bulan >= 5 and not kk_done("K-D01"):
                return "K-D01"
            # --- Batch tambahan K-D (gerbang mengikuti pemicu katalog) ---
            if kk_has("force_pernah") and not kk_done("K-D17"):
                return "K-D17"
            if kk_get("plot_armor_tekanan",0) >= 90 and orbit_koita <= 1 and not kk_done("K-D14"):
                return "K-D14"
            if kk_get("plot_armor_tekanan",0) >= 75 and not kk_done("K-D10"):
                return "K-D10"
            if koita_sadar >= 75 and kk_get("pilihan_koita_puncak",0) >= 80 and not kk_done("K-D11"):
                return "K-D11"
            if runtuh_koita >= 30 and orbit_koita <= 2 and not kk_done("K-D15"):
                return "K-D15"
            if kk_bulan >= 35 and not kk_done("K-D12"):
                return "K-D12"
            if kk_has("matsuda_sekutu") and not kk_done("K-D06"):
                return "K-D06"
            if kk_get("takut_ditinggal",0) >= 60 and not kk_done("K-D02"):
                return "K-D02"
            if kk_host == "yutaka" and kk_get("ikatan_bl",0) >= 50 and not kk_done("K-D07"):
                return "K-D07"
            if kk_host == "yutaka" and kk_bulan >= 8 and not kk_done("K-D03"):
                return "K-D03"
            if kk_bulan >= 20 and kk_has("koita_pola_dicurigai") and not kk_done("K-D04"):
                return "K-D04"
        if cid == "moeka":
            _mst = kk_get("stres_total",0)
            _mstage = stage.get("moeka",0)
            # Pemulihan / jendela intervensi diperiksa lebih dulu.
            if _mst < 40 and kk_rel_get("moeka","aff") >= 55 and not kk_done("Mo-D13"):
                return "Mo-D13"
            if _mstage >= 3 and (kk_rel_get("moeka","intim") >= 55 or kk_has("rina_memberi_tahu")) and not kk_done("Mo-D12"):
                return "Mo-D12"
            if _mstage >= 4 and not kk_done("Mo-D11"):
                return "Mo-D11"
            if kk_get("topeng_moeka",0) >= 70 and kk_slot in (4,5) and not kk_done("Mo-D10"):
                return "Mo-D10"
            if (kk_has("moeka_ayah_diketahui") and _mstage >= 3 and _mst >= 55
                    and not kk_done("Mo-D09")):
                return "Mo-D09"
            if _mstage >= 3 and _mst >= 55 and not kk_done("Mo-D08"):
                return "Mo-D08"
            if (kk_get("rina_curiga",0) >= 50 or kk_has("rina_sekutu")) and not kk_done("Mo-D07"):
                return "Mo-D07"
            if kk_get("kuga_tekanan",0) >= 40 and not kk_done("Mo-D05"):
                return "Mo-D05"
            if _mstage >= 2 and kk_rel_get("moeka","aff") >= 30 and not kk_done("Mo-D03"):
                return "Mo-D03"
            if _mstage >= 2 and kk_slot in (4,5) and _mst >= 60 and not kk_done("Mo-D02"):
                return "Mo-D02"
            if _mst >= 60 and kk_slot in (4,5) and not kk_done("Mo-D01"):
                return "Mo-D01"
            if kk_rel_get("moeka","intim") >= 40 and not kk_done("Mo-D04"):
                return "Mo-D04"
            if kk_bulan in (7,19,31) and _mst >= 50 and not kk_done("Mo-D06"):
                return "Mo-D06"
        # --- Event lintas-karakter (X-D) lewat tokoh yang tepat ---
        if cid == "moeka":
            if (kk_rel_get("nagisa","jeal") >= 60 and kk_get("stres_total",0) >= 60
                    and kk_slot in (4,5) and not kk_done("X-D01")):
                return "X-D01"
            if (kk_get("rina_curiga",0) >= 50 and kk_get("sena_curiga",0) >= 50
                    and not kk_done("X-D08")):
                return "X-D08"
            if kk_has("krisis_ganda") and not kk_done("X-D10"):
                return "X-D10"
        if cid == "miyuki":
            if (stage.get("moeka",0) >= 3 and kk_get("kelelahan_miyuki",35) < 60
                    and not kk_done("X-D02")):
                return "X-D02"
        if cid == "shiori":
            if (kk_has("ogawa_aktif") and kk_rel_get("harumi","trust") >= 40
                    and kk_rel_get("shiori","trust") >= 40 and not kk_done("X-D03")):
                return "X-D03"
        if cid == "koita":
            if koita_sadar >= 75 and not kk_done("X-D07"):
                return "X-D07"
            if kk_has("grup_sma_dibuka") and not kk_done("X-D11"):
                return "X-D11"
            if kk_has("mei_menulis") and not kk_done("X-D06"):
                return "X-D06"
            if (kk_get("haruto_curiga",0) >= 50 and kk_get("kuroiwa_percaya",0) >= 20
                    and not kk_done("X-D09")):
                return "X-D09"
            if kk_bulan == 14 and kk_hari_n == 14 and not kk_done("X-D04"):
                return "X-D04"
            if kk_kelelahan_tier()[1] >= 3 and not kk_done("X-D12"):
                return "X-D12"
        return None

    def kk_host_dyn(distrik, lokasi):
        # Event dinamis host (Chiasa/Yutaka) yang menyala saat memasuki lokasi
        # tertentu, sejajar dengan kk_father_visit. String eid tinggal di berkas ini
        # agar ikut terhitung connected. Semua di rumah host kecuali disebut lain.
        home = "Apartemen Yutaka" if kk_host == "yutaka" else "Rumah Amamiya"
        if (lokasi == home and kk_bulan in (9,21,33) and kk_hari_n in (24,25)
                and kk_slot in (3,4) and not kk_done("X-D05")):
            return "X-D05"
        if kk_host == "chiasa":
            if lokasi == home and kk_slot in (4,5) and not kk_done("C-D01"):
                return "C-D01"
            if kk_has("framing_koita"):
                if not kk_done("C-D13"):
                    return "C-D13"
                if not kk_done("C-D15"):
                    return "C-D15"
                if (kk_get("yutaka_harap",0) >= 40 or kk_get("nurani_chiasa",0) >= 20) and not kk_done("C-D14"):
                    return "C-D14"
            if lokasi == home and kk_has("koita_arah_bl") and not kk_done("C-D09"):
                return "C-D09"
            if lokasi == home and kk_has("koita_arah_bl") and not kk_done("C-D11"):
                return "C-D11"
            if lokasi == home and kk_get("yutaka_harap",0) >= 30 and kk_slot in (4,5) and not kk_done("C-D08"):
                return "C-D08"
            if lokasi == home and stage.get("nagisa",0) >= 2 and not kk_done("C-D06"):
                return "C-D06"
            if lokasi == home and kk_bulan in (9,21) and kk_hari_n in (24,25) and not kk_done("C-D10"):
                return "C-D10"
            if kk_bulan == 16 and kk_slot in (0,1) and not kk_done("C-D05"):
                return "C-D05"
            if (lokasi == home and max([kk_rel_get(h,"intim") for h in ("miyuki","nagisa","harumi","moeka","shiori")]) >= 50
                    and not kk_done("C-D12")):
                return "C-D12"
            if lokasi == home and kk_kelelahan_tier()[1] >= 2 and not kk_done("C-D04"):
                return "C-D04"
            # Yutaka sebagai NPC yang mengejar Chiasa (Female Route).
            if kk_get("yutaka_harap",0) >= 70 and not kk_done("Y-D11"):
                return "Y-D11"
            if kk_get("yutaka_harap",0) >= 50 and not kk_done("Y-D10"):
                return "Y-D10"
        if kk_host == "yutaka":
            if kk_hari_n == 25 and not kk_done("Y-D01"):
                return "Y-D01"
            if kk_bulan == 16 and not kk_done("Y-D05"):
                return "Y-D05"
            if lokasi == home and kk_rel_get("nagisa","aff") >= 40 and kk_slot in (4,5) and not kk_done("Y-D07"):
                return "Y-D07"
            if lokasi == home and kk_has("koita_arah_bl") and not kk_done("Y-D09"):
                return "Y-D09"
            if lokasi == home and kk_has("daichi_kenal") and not kk_done("Y-D04"):
                return "Y-D04"
            if kk_date().weekday() == 4 and kk_slot in (4,5) and not kk_done("Y-D06"):
                return "Y-D06"
            if kk_has("koita_arah_bl") and not kk_done("Y-D02"):
                return "Y-D02"
        return None

# Dua event dinamis berikut ditangani INLINE di fallback generik label ini
# (cari "if eid == \"N-D02\"" / "if eid == \"Mi-D03\"" di bawah), bukan di label sendiri:
# ┌─ PANDUAN CERITA · N-D02 · Bekal yang Tidak Diakui
# │ LOKASI  : (dinamis) · TERLIBAT: Sakurajima Nagisa
# │ AWALAN  : Aff ≥ 55; gengsi ≥ 50
# │ INTI    : A Puji di depan orang / B puji diam-diam / C kembalikan
# │ AKHIRAN : di depan orang: gengsi −, Aff +; diam-diam: Aff ++
# ├─ PANDUAN CERITA · Mi-D03 · Pastry dengan Nama
# │ LOKASI  : (dinamis) · TERLIBAT: Tachibana Miyuki (+ Koita bila di lokasi)
# │ AWALAN  : Aff ≥ 55; pemain pernah memuji pastry-nya
# │ INTI    : A Makan di depan Koita / B sembunyikan / C bagikan ke semua
# │ AKHIRAN : Koita mencatat; Nagisa cemburu bila melihat
# └─ tulis / perbaiki dialog di bawah ──
label kk_social_scene(eid):
    # Draft editorial dari pemicu dan pilihan katalog dinamis.
    if kk_done(eid):
        return
    $ kk_bgm_event(eid)
    if eid in KK_DYNX:
        # Batch dinamis tambahan: tiap eid punya label kkscene_<eid> sendiri.
        call expression ("kkscene_" + eid.replace("-","_"))
        $ kk_minutes(10)
        return
    if (eid.startswith("K-D") or eid in ("Mi-D05","Mi-D06","Mi-D07","Mi-D08","Mi-D10","Mi-D14")
            or eid in ("S-D03","S-D07","S-D13","S-D14","S-D15","S-D16","S-D17")):
        call expression ("kkscene_" + eid.replace("-","_"))
        $ kk_minutes(10)
        return
    if eid == "S-D04":
        call kk_shiori_question
        $ kk_minutes(10)
        return
    if eid == "S-D08":
        call kk_saionji_tea
        $ kk_minutes(10)
        return
    if eid == "Mi-D11":
        call kk_exam_eve
        return
    if eid == "Mi-D09":
        call kk_pediatric_patient
        $ kk_minutes(10)
        return
    if eid == "Mi-D12":
        call kk_miyuki_refuses
        $ kk_minutes(10)
        return
    if eid == "Mi-D04":
        call kk_overheard_call
        $ kk_minutes(10)
        return
    if eid == "N-D09":
        call kk_torn_koko
        $ kk_minutes(10)
        return
    if eid in ("N-D03","N-D08","N-D05","N-D06","N-D07","N-D10","N-D11","N-D12","N-D13"):
        call expression ("kkscene_" + eid.replace("-","_"))
        $ kk_minutes(10)
        return
    if eid == "H-D05":
        call kk_second_meal
        return
    if eid == "H-D07":
        call kk_kansai_letter
        $ kk_minutes(10)
        return
    if eid == "H-D01":
        call kk_dorm_tea
        return
    if eid == "N-D02":
        nar "Pada jam makan siang itu, Nagisa mengeluarkan dua kotak bekal dari tas kainnya lalu mendorong salah satunya ke depanmu dengan gerakan yang terlalu cepat untuk terlihat santai. Saat kamu melirik ke balik tutup beningnya, potongan telur gulung manis dan lauk pendamping di dalamnya terlalu tepat mengikuti seleramu untuk disebut kebetulan."
        if kk_host == "chiasa":
            chiasa "Eh? Ini buatku, Nagisa-senpai? Lauknya rapi banget sampai ada potongan wortel bentuk bunga segala."
            nagisa "Tadi pagi aku salah hitung takaran nasi sama lauk, Chiasa! Jangan lihat aku begitu dong. Orang kan bisa aja nggak sengaja bikin kelebihan satu porsi lengkap. Daripada mubazir, habiskan aja!"
        else:
            yutaka "Wah, kotak bekal tambahan ya? Lauknya kebetulan banget semua yang biasa kupesan di kantin, Nagisa."
            nagisa "Aku salah hitung takaran tadi pagi, Yutaka! Jangan pasang senyum begitu dong. Orang kan bisa aja salah hitung satu porsi lengkap. Daripada basi di tas, makan aja sana!"
        nar "Ia sudah menyiapkan pembelaan rapi bahkan sebelum kamu sempat membuka pengait kotak makannya."
    else:
        nar "Miyuki mengeluarkan sebuah kotak kue mungil dari tasnya lalu membuka tutupnya dengan gerakan hati-hati di meja. Di atas lapisan pastry cokelat yang mengilap, terukir tulisan namamu dari lelehan krim putih yang sedikit miring dan jelas ditulis langsung dengan tangannya."
        nar "Begitu menyadari beberapa mahasiswa lain melintas di dekat meja, Miyuki refleks mencondongkan tubuh untuk menutupi sebagian tutup kotak agar tidak langsung terbaca dari jauh."
        if kk_host == "chiasa":
            miyuki "Chiasa-chan pernah bilang suka pastry panggang yang kulitnya renyah kan? Jadi kali ini kubuatkan satu khusus buat Chiasa-chan biar nggak perlu dibagi-bagi. Maaf ya tulisannya agak miring, aku bisa bikin lapisan adonan rapi tapi ternyata menulis namamu jauh lebih bikin gugup."
            chiasa "Tachibana-senpai sampai nulis namaku sendiri di atas kuenya... kelihatan enak banget!"
        else:
            miyuki "Yutaka-kun pernah bilang suka pastry panggang yang kulitnya renyah kan? Jadi kali ini kubuatkan satu yang nggak perlu dibagi ke siapa-siapa. Tulisannya agak miring ya, aku biasa bikin lapisan rapi tapi ternyata menulis namamu di atas kue malah lebih susah."
            yutaka "Wah, ini beneran ditulis tangan sama Tachibana-senpai? Sayang banget rasanya kalau langsung dipotong."
    $ _row = KK_DYN_BY_ID[eid]
    $ _rows = [(caption, Return(key), False) for key, caption in zip("ABC", _row["choices"]) if not (eid == "Mi-D03" and key == "A" and kk_daily_place("koita") != _lokasi)]
    call screen kk_choice_panel(_rows, "Apa yang kamu lakukan?")
    $ _key = _return
    $ kk_record_choice(eid,_key)
    if eid == "Mi-D03":
        $ kk_pastry_witnessed(_key, _lokasi)
    if eid == "N-D02":
        if _key == "A":
            if kk_host == "chiasa":
                chiasa "Wah, ini enak banget lho, Nagisa-senpai! Telur gulungnya manis pas banget, jauh lebih enak daripada beli di luar!"
            else:
                yutaka "Serius nih, Nagisa, masakanmu enak banget! Bumbunya pas semua, kalau salah hitung bisa selezat ini aku nggak keberatan dapat tiap minggu."
            nagisa "Sst, pelankan suaramu! Meja sebelah jadi pada noleh ke sini tahu!"
            nar "Telinga Nagisa memerah cepat sambil melirik sekitar, tetapi tangannya tetap ikut menggeser kotak bekalmu agar lebih nyaman dijangkau sumpit. Protesnya atas perhatian orang lain ternyata kalah jauh oleh keinginannya melihat kamu menyuap habis."
            nagisa "Sudah, makan aja yang benar, nggak usah pakai teriak-teriak muji segala..."
        elif _key == "B":
            if kk_host == "chiasa":
                chiasa "Enak banget, Nagisa-senpai... makasih banyak ya sudah repot-repot buatin sampai seenak ini."
            else:
                yutaka "Jujur aja, ini enak banget, Nagisa. Makasih ya sudah buatin bekal serapi ini buatku."
            nar "Kamu memujinya dengan suara rendah yang hanya terdengar di meja kalian berdua. Bahu Nagisa yang tadi menegang perlahan turun, dan senyum kecil sempat lolos sebelum ia cepat-cepat menunduk."
            nagisa "...Kalau memang suka, habiskan sampai bersih ya. Biar nanti aku tahu porsinya kebanyakan atau kurang."
            nar "Ia terhenti sepersekian detik saat sadar kalimatnya barusan menyiratkan akan ada bekal-bekal berikutnya. Kamu memilih tidak menggodanya, memberi ruang aman agar perhatian yang baru berani ia tunjukkan tidak perlu ia tarik lagi."
        else:
            if kk_host == "chiasa":
                chiasa "Maaf ya, Nagisa-senpai, tadi aku sudah sempat beli roti sebelum ke sini, jadi kayaknya nggak bakal habis. Kubalikin dulu ya biar nggak mubazir."
            else:
                yutaka "Maaf ya, Nagisa, perutku masih kenyang banget habis makan tadi. Lebih baik kamu simpan aja atau bawa pulang biar nggak kebuang."
            nar "Nagisa mengambil kotak itu kembali dan menutup pengait plastiknya dengan bunyi klik yang sedikit terlalu keras."
            nagisa "Oh, iya. Nggak apa-apa kok. Aku kan cuma menawarkan daripada tersisa."
            nar "Kotak bekal itu langsung masuk kembali ke dalam tas kainnya. Detik berikutnya ia segera mengalihkan obrolan ke jadwal kelas siang, menyembunyikan berapa lama ia tadi pagi berdiri di dapur menata isi kotak tersebut."
    else:
        if _key == "A":
            nar "Kamu membiarkan tutup kotak terbuka jelas di atas meja tepat saat Koita melangkah mendekat sambil membawa minuman. Pandangan Koita langsung tertuju pada ukiran namamu di atas kue, lalu naik menatap Miyuki sedikit lebih lama dari biasanya."
            koita "Wah, kelihatannya enak banget tuh. Ada tulisan namanya segala... Miyuki-senpai bikin khusus ya?"
            miyuki "Iya, Koita-kun. Kali ini memang kubuat khusus."
            if kk_host == "chiasa":
                chiasa "Makasih ya, Tachibana-senpai, aku makan sekarang mumpung kulitnya masih renyah!"
                koita "Haha, enak banget tuh Chi-chan dapat perlakuan khusus dari Senpai."
            else:
                yutaka "Enak banget lho, Koita. Kulitnya masih renyah persis kayak yang kubilang kemarin."
                koita "...Iya, kelihatan banget niat bikinnya. Selamat makan, Yutaka."
            nar "Miyuki menjawab dengan suara lembut tanpa berusaha menyebutnya sisa adonan atau kebetulan. Koita mengangguk pelan, baru benar-benar menangkap bahwa perhatian Miyuki kini tidak lagi hanya berputar di sekitar dirinya."
        elif _key == "B":
            nar "Kamu buru-buru merapatkan tutup kotak dan memasukkannya ke dalam tas sebelum tulisan namamu sempat dibaca mahasiswa lain di meja sebelah. Miyuki memperhatikan gerakan tanganmu dengan raut tenang yang agak sulit ditebak."
            if kk_host == "chiasa":
                chiasa "Biar kusimpan dulu buat kumakan pelan-pelan di rumah ya, Tachibana-senpai, sayang kalau dimakan buru-buru di sini."
            else:
                yutaka "Kusimpan dulu ya, Tachibana-senpai, biar nanti bisa kunikmati tenang di apartemen tanpa diganggu keramaian."
            miyuki "Baiklah... makan nanti ya kalau sudah santai. Aku ingin tahu rasanya cocok atau nggak di lidahmu."
            nar "Ia tidak mempertanyakan keputusanmu di depan umum, meski kamu sadar ia belum sepenuhnya yakin apakah kamu ingin menjaga momen pribadi atau justru canggung mengakui kedekatan kalian."
        else:
            if kk_host == "chiasa":
                chiasa "Kelihatannya gede banget buat kumakan sendiri, Tachibana-senpai. Boleh kubagi sekalian ke teman-teman meja sebelah biar pada ikut nyicipin enaknya buatan Senpai?"
            else:
                yutaka "Porsinya lumayan besar nih, Tachibana-senpai. Gimana kalau kita potong terus bagi ke yang lain sekalian biar ramai?"
            nar "Kamu memotong pastry itu di tempat. Pisau plastik membelah tepat di tengah ukiran namamu hingga huruf-huruf krim itu terpisah menjadi potongan biasa di atas piring kertas."
            miyuki "Oh... dibagi ke semuanya ya. Iya, tentu saja boleh. Semoga potongannya cukup."
            nar "Miyuki ikut membantu menyodorkan piring kecil dengan senyum terlatih sebelum sempat menimbang apakah ia sebenarnya kecewa. Bagi orang-orang di meja itu hanyalah camilan manis, sedangkan bagi Miyuki perhatian yang semula ia tulis khusus untuk satu nama kini harus ia relakan menjadi milik semua orang."
    $ kk_minutes(10)
    return

# ┌─ PANDUAN CERITA · Mi-D01 · Permintaan Kecil
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Tachibana Miyuki
# │ AWALAN  : dimanja ≥ 50; Trust Sedang
# │ INTI    : A Belikan dan temani / B belikan lalu pergi / C tolak / D tertawakan
# │ AKHIRAN : dimanja +10 / +5 / −5 / −10; Intim
# └─ tulis / perbaiki dialog di bawah ──
label kk_pudding:
    play sound "audio/sfx/phone_buzz.wav"
    nar "Menjelang pukul sebelas malam, ponselmu bergetar menampilkan satu pesan singkat dari Miyuki yang sekadar menanyakan apakah kamu masih bangun. Setelah kamu membuka ruang obrolan, tanda sedang mengetik sempat muncul lama lalu hilang kembali, sebelum akhirnya sebuah pesan yang tampak ditulis sangat hati-hati masuk."
    if kk_host == "chiasa":
        "Pesan Miyuki" "Chiasa-chan, maaf mengganggu malam-malam. Kalau kebetulan masih belum tidur dan lewat toko serba ada dekat sini, boleh nggak... sekali ini aja aku titip dibelikan puding karamel? Nggak usah kalau jauh atau sudah mau tidur ya."
        "Pesan Miyuki" "Nanti uangnya langsung kuganti kok. Aku cuma lagi kepengin sesuatu yang manis, tapi rasanya malas keluar sendirian jam segini. Beneran nggak apa-apa banget kalau nggak bisa ya, Chiasa-chan."
    else:
        "Pesan Miyuki" "Yutaka-kun, maaf mengganggu selarut ini. Kalau kebetulan kamu belum tidur dan lewat toko serba ada, boleh nggak... sekali ini aja aku titip puding karamel? Nggak harus sama sekali kalau jauh atau kamu sudah capek."
        "Pesan Miyuki" "Uangnya pasti langsung kuganti begitu sampai. Aku cuma lagi kepengin yang manis tapi nggak mau jalan keluar sendirian malam-malam. Sungguh nggak apa-apa kalau kamu nggak sempat ya."
    nar "Permintaan kecil itu tiba dibungkus begitu banyak jalan keluar untuk membatalkannya, seolah Miyuki sudah menyiapkan diri untuk mundur begitu kamu menunjukkan sedikit saja tanda keberatan."
    $ _rows = [(caption, Return(key), False) for key, caption in zip("ABCD",KK_DYN_BY_ID["Mi-D01"]["choices"])]
    call screen kk_choice_panel(_rows, "Balas pesan Miyuki")
    $ _key = _return
    $ kk_record_choice("Mi-D01", _key)
    if _key == "A":
        $ kk_rel("miyuki","intim",1)
        nar "Kamu langsung menyambar jaket, membeli dua cangkir puding karamel di toko serba ada yang masih terang, lalu mengantarkannya ke pintu apartemen Miyuki. Begitu pintu terbuka dan kamu menawarkan ikut duduk sebentar, Miyuki segera mengambil dua sendok dari dapur lalu tertawa kecil menyadari tangannya bergerak otomatis sebelum sempat bertanya apakah kamu mau."
        if kk_host == "chiasa":
            miyuki "Haha, ketahuan ya, Chiasa-chan? Aku bahkan sudah siapin dua sendok duluan sebelum nanya kamu mau makan juga apa nggak."
            chiasa "Kebetulan aku juga beli dua kok, Tachibana-senpai. Makanya nggak usah buru-buru, kita habiskan pelan-pelan aja."
            miyuki "...Sebenarnya malam ini aku memang nggak cuma kepengin pudingnya doang sih. Ternyata rasanya lega banget ya kalau boleh jujur bilang begitu."
        else:
            miyuki "Haha, ketahuan ya, Yutaka-kun? Tanganku sudah keburu ambil dua sendok padahal belum nanya kamu mau ikut makan atau nggak."
            yutaka "Tenang aja, aku memang sengaja beli dua cangkir kok, Tachibana-senpai. Jadi kita duduk santai aja sebentar."
            miyuki "...Sebenarnya malam ini aku nggak cuma pengin makan puding doang. Ternyata boleh ya bilang pengin ditemani tanpa harus cari alasan dulu."
        nar "Kalian menyendok puding pelan di meja kecil dapur. Malam itu Miyuki tidak sibuk menyiapkan camilan lain ataupun mencari topik serius demi membuat waktumu terasa berguna. Kehadiranmu cukup diterima apa adanya sebagai sesuatu yang ingin ia nikmati."
    elif _key == "B":
        nar "Kamu mampir membeli puding karamel dan mengantarkannya langsung ke depan pintu apartemen Miyuki, lalu menjelaskan dengan jujur bahwa kamu harus segera pulang karena besok ada urusan pagi."
        if kk_host == "chiasa":
            chiasa "Ini pudingnya, Tachibana-senpai. Maaf aku nggak bisa mampir lama ya, besok ada kelas pagi jadi harus langsung pulang."
            miyuki "Terima kasih banyak sudah jauh-jauh menyempatkan, Chiasa-chan! Justru aku senang kamu langsung bilang waktumu sampai sini saja, jadi aku nggak perlu nebak-nebak kapan aku mulai merepotkan."
        else:
            yutaka "Ini puding karamelnya, Tachibana-senpai. Maaf aku langsung balik ya, besok jadwal pagiku lumayan padat."
            miyuki "Terima kasih banyak sudah menyempatkan jalan ke sini, Yutaka-kun. Aku malah lega kamu bilang batasnya terus terang, jadi aku nggak terus merasa bersalah sudah menahanmu."
        nar "Miyuki melambaikan tangan hangat dari ambang pintu. Sepuluh menit setelah kamu berjalan menjauh, satu foto puding yang tutupnya baru dibuka masuk ke ponselmu disertai pesan singkat bahwa rasanya manis dan lezat sekali."
    elif _key == "C":
        if kk_host == "chiasa":
            chiasa "Maaf banget ya, Tachibana-senpai, malam ini aku sudah siap tidur dan di luar lagi dingin banget. Lain waktu aja ya."
        else:
            yutaka "Maaf ya, Tachibana-senpai, malam ini aku belum bisa keluar ke toko serba ada soalnya sudah mau istirahat."
        nar "Balasan Miyuki masuk kurang dari lima detik kemudian, terlalu cepat untuk menutupi rasa canggung karena telanjur meminta."
        "Pesan Miyuki" "Oh, baik, nggak apa-apa sama sekali! Maaf banget sudah kirim pesan mendadak selarut ini. Aku bikin teh hangat sendiri aja di dapur, selamat istirahat ya."
        nar "Setelah pesan itu tidak ada lagi lanjutan obrolan. Penolakanmu jelas wajar dan sah, tetapi kamu tahu Miyuki masih harus belajar agar satu permintaan yang tidak bisa dipenuhi tidak langsung ia catat sebagai bukti bahwa meminta sejak awal adalah kesalahan."
    else:
        if kk_host == "chiasa":
            chiasa "Haha, Tachibana-senpai yang biasanya paling dewasa ternyata jam sebelas malam bisa ngidam puding kayak anak kecil juga ya?"
        else:
            yutaka "Hahaha, serius nih Tachibana-senpai jam sebelas malam mendadak ngidam puding kayak anak kecil begitu?"
        nar "Indikator mengetik di sisi Miyuki muncul, menghilang beberapa detik, muncul kembali, lalu berhenti cukup lama sebelum akhirnya satu balasan pendek masuk."
        "Pesan Miyuki" "Maaf, lupakan saja pesan tadi ya. Aku tadi cuma bercanda kok. Selamat tidur."
        nar "Kamu tahu betul ia sama sekali tidak sedang bercanda saat mengetik permintaan pertamanya tadi. Kini ia terpaksa bersembunyi di balik dalih candaan agar tidak merasa telah mempermalukan dirinya sendiri, dan pada obrolan berikutnya ia pasti akan kembali sibuk menanyakan kabarmu lebih dulu agar tidak ada keinginan kecilnya yang telanjur keluar lagi."
    $ kk_minutes(15)
    return

