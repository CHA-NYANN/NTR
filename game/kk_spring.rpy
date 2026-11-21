# Draft editorial. Milestone_3_Tahun M01b/M02 dan Event_Moeka, Event_Shiori,
# Event_Nagisa, Event_Miyuki. Adegan memakai urutan pilihan dari katalog.
# ┌─ PANDUAN CERITA · Mo01 · Wakil yang Selalu Terlambat
# │ LOKASI  : Kampus Kouseikan · Taman Kampus
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : Moeka datang terlambat tapi memimpin acara.
# │ INTI    : A maklum / B tegur / C bantu.
# │ AKHIRAN : C membuka sisi kompeten.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo01:
    call kk_scene_enter("moeka", "Hanami · Taman Kampus")
    if kk_host == "chiasa":
        nar "Angin pertengahan April berembus hangat menyusuri jalan setapak Taman Kampus Kouseikan, menggoyangkan dahan-dahan sakura yang sedang mekar penuh hingga kelopak berwarna merah muda pucat berjatuhan pelan di atas rumput dan bangku kayu."
        nar "Di bawah naungan pepohonan dekat Gedung Seni Rupa, sekitar lima belas mahasiswa gabungan dari beberapa jurusan sudah berkumpul sejak tadi. Namun alih-alih suasana piknik yang meriah, yang terasa justru kecanggungan yang menggantung di udara."
        nar "Jam di layar ponselmu menunjukkan sudah lewat lima belas menit dari jadwal kumpul Hanami yang tertera di papan pengumuman fakultas. Dua mahasiswi tahun pertama yang berdiri tak jauh darimu mulai menggeser tumpuan kaki sambil memeluk kardus minuman yang tampak cukup berat."
        "Mahasiswi Tahun Pertama A" "Eh... ini sudah lewat seperempat jam, ya? Kita beneran belum boleh duduk dulu?"
        "Mahasiswi Tahun Pertama B" "Soalnya terpal pikniknya semua dibawa sama senpai koordinatornya. Aku juga nggak berani gelar apa-apa duluan kalau belum ada arahan..."
        nar "Beberapa langkah di sebelah mereka, seorang mahasiswa baru berkacamata berdiri agak terpisah dekat batang pohon kamper. Kedua tangannya mencengkeram tali kantong plastik berisi piring kertas dan sumpit dengan kaku, matanya berkali-kali melirik ke arah gerbang batu berharap ada sosok yang ia kenal."
        nar "Kau sendiri berdiri menyandar santai di pagar kayu rendah tepi jalan setapak sambil memeluk tas jinjing kain. Baru beberapa hari menjalani hidup di tubuh Amamiya Chiasa, kau belum hafal banyak hal soal orang-orang di kampus ini—bahkan dari manga yang cuma sempat kaubaca sepintas dulu, kau cuma samar-samar ingat ada seorang senior berambut merah muda yang sering terlambat."
        play sound "audio/sfx/footsteps.wav"
        nar "Belum sempat kau menebak apakah acara ini akan bubar sebelum dimulai, suara ketukan sepatu hak pendek yang berlari tergesa-gesa terdengar nyaring menghantam paving batu dari arah gerbang taman."
        moeka "Permisi! Awas, jalur darurat, kasih jalan sebentar—!"
        nar "Seorang gadis bertubuh semampai dengan rambut merah muda panjang bergelombang muncul dari tikungan jalan setapak sambil menahan tali kamera digital yang terayun liar di depan dadanya. Di bahu kirinya tergantung tas kanvas besar yang menggembung penuh sesak, sementara lengan kanannya mendekap dua gulungan terpal piknik biru yang ukurannya hampir setinggi bahunya sendiri."
        nar "Ia mengenakan kardigan rajut krem longgar bergaya gyaru yang dipadukan dengan rok lipit dan aksesori warna-warni. Bahkan dari jarak beberapa meter, kau bisa melihat detail jahitan renda tangan kecil yang rapi di ujung pergelangan kardigannya."
        nar "Kohinata Moeka mengerem langkahnya tepat di tepi hamparan rumput, menarik napas dalam-dalam sambil sedikit membungkuk agar gulungan terpal di lengannya tidak jatuh, lalu langsung mengangkat wajah dengan senyum lebar sebelum ada satu pun peserta yang sempat mengeluh."
        moeka "Semuanya, maaf banget aku telat! Kereta tadi sempat tertahan di stasiun sebelumnya, terus aku harus lari ambil terpal di ruang penyimpanan—tapi kalian boleh mengomel sepuasnya nanti setelah semuanya dapat tempat duduk, ya!"
        nar "Anehnya, kalimat permintaan maaf yang terdengar berisik dan santai itu bahkan belum benar-benar habis di udara ketika mata biru cerahnya sudah selesai memindai seluruh area taman dalam sekali sapuan."
        nar "Ia melihat arah jatuhnya sinar matahari siang, letak akar-akar pohon sakura yang menonjol, serta barang apa saja yang sedang dipegang oleh tiap kelompok mahasiswa."
        moeka "Oke, kita bereskan dalam satu menit! Kalian berdua yang pegang kardus minuman—tolong taruh di bawah bayangan pohon kamper sebelah kiri sana ya, biar tehnya nggak jadi hangat kena matahari langsung!"
        "Mahasiswi Tahun Pertama A" "Ah—iya, baik, Senpai!"
        moeka "Terus yang bawa piring kertas sama sumpit, letakkan dulu di atas bangku kayu panjang dekat pagar biar plastiknya nggak terbang ditiup angin! Nanti begitu terpalnya kebuka, baru kita pindahkan ke tengah!"
        nar "Suasana yang lima belas menit terakhir terasa beku dan canggung langsung berubah hidup. Para mahasiswa yang tadi hanya berdiri terpaku serentak mulai bergerak mengikuti arahannya tanpa ragu."
        nar "Sebelum melangkah ke tengah rumput, pandangan Moeka menangkap pemuda berkacamata yang sejak tadi berdiri menyendiri di dekat pohon kamper. Tanpa jeda sedikit pun, Moeka melambai kepadanya dengan nada akrab."
        moeka "Hei, Sato-kun yang kemarin ikut sesi pengenalan studio, kan? Jangan berdiri di pojokan sendirian dong! Bisa tolong pegangkan gulungan kantong sampah sama botol air buat pemberat sudut terpal nggak? Aku butuh bantuan orang yang teliti nih!"
        "Mahasiswa Tahun Pertama" "E-eh? Senpai ingat namaku? B-boleh, biar aku yang pegang!"
        nar "Wajah mahasiswa baru itu seketika berubah lega dan bersemangat. Ia bergegas melangkah masuk ke lingkaran rombongan untuk mengambil kantong sampah yang disodorkan salah satu panitia lain."
        nar "Hanya dalam waktu kurang dari setengah menit, tidak ada lagi satu pun orang yang kebingungan atau berdiri terasing. Baru setelah arus kerumunan mulai bergerak rapi, Moeka memutar tubuhnya untuk mencari celah melintas membawa dua gulungan terpal berat di lengannya—dan tatapannya langsung jatuh padamu di tepi jalan setapak."
        nar "Wajahnya yang sedikit bersemu karena berkeringat langsung merekah cerah. Ia melangkah cepat mendekatimu sambil memiringkan bahu agar gulungan terpalnya tidak menyenggol pagar."
        moeka "Eh, Chimian! Pas banget kau juga mampir ke Hanami gabungan! Maaf banget ya, senpai satu fakultasmu ini malah ngasih contoh buruk datang paling belakangan begini~"
        nar "'Chimian'... butuh sepersekian detik bagimu untuk mencerna bahwa julukan gyaru yang terdengar begitu akrab itu ditujukan kepada tubuh yang sedang kautempati sekarang."
    else:
        nar "Angin pertengahan April berembus hangat melewati jalan setapak Taman Kampus Kouseikan, menggugurkan kelopak-kelopak sakura pucat ke atas hamparan rumput dan bahu belasan mahasiswa yang sejak tadi berkumpul di dekat bangku kayu."
        nar "Kau melirik jam tangan di pergelangan kirimu—benda perak berdesain rapi yang terasa begitu alami melingkar di tubuh Kisaragi Yutaka—dan mendapati waktu sudah lewat lima belas menit dari jadwal kumpul Hanami gabungan."
        nar "Dengan kedua tangan dimasukkan santai ke saku jaket, kau berdiri menyandar ke tembok batu rendah di pinggir jalur taman sambil mengamati suasana. Sekitar lima belas mahasiswa, mayoritas anak tahun pertama dari berbagai fakultas, berdiri terpencar dengan raut wajah canggung."
        nar "Dua mahasiswi tahun pertama yang berdiri beberapa langkah darimu mulai mengganti posisi pegangan pada kardus berisi botol minuman yang tampak berat."
        "Mahasiswi Tahun Pertama A" "Aduh... tanganku mulai pegal. Ini beneran sudah lewat seperempat jam, kan? Kita belum boleh taruh dulu di rumput?"
        "Mahasiswi Tahun Pertama B" "Rumputnya masih agak lembap habis disiram pagi tadi. Terpalnya semua dibawa sama senpai koordinatornya, jadi mau nggak mau kita tunggu dulu..."
        nar "Agak terpisah dari mereka, seorang mahasiswa baru berkacamata berdiri kaku dekat batang pohon kamper sambil memeluk kantong plastik berisi piring kertas dan sumpit. Matanya bolak-balik melirik gerbang taman dengan gelisah."
        nar "Kau mengembuskan napas pelan. Baru beberapa hari menghuni tubuh Yutaka, banyak wajah dan nama di kampus ini masih asing bagimu. Dari grup obrolan panitia di ponsel Yutaka, kau cuma tahu koordinator acara siang ini bernama Kohinata Moeka—dan samar-samar mengingat sosok gyaru berambut merah muda dari beberapa bab awal yang pernah kaulirik."
        play sound "audio/sfx/footsteps.wav"
        nar "Belum sempat kau memutuskan apakah lebih baik pergi mencari kopi saja, suara ketukan sepatu hak pendek yang berlari kencang menghantam paving batu terdengar dari arah gerbang."
        moeka "Permisi! Awas, jalur darurat, kasih jalan sebentar—!"
        nar "Dari balik tikungan jalan setapak, muncul seorang gadis bertubuh semampai dengan rambut merah muda panjang bergelombang yang berantakan tertiup angin. Sebuah kamera digital terayun-ayun miring di depan dadanya, tas kanvas besar yang penuh sesak menggantung di bahu kiri, sementara lengan kanannya mendekap dua gulungan terpal piknik biru yang ukurannya hampir setinggi bahunya."
        nar "Ia mengenakan kardigan rajut krem bergaya gyaru dengan sentuhan renda jahitan tangan di pergelangan lengannya. Begitu sampai di tepi hamparan rumput, Kohinata Moeka mengerem langkahnya mendadak, menahan napas sejenak agar gulungan terpal di pelukannya tidak terlepas, lalu langsung mengangkat suara dengan nada ceria sebelum ada yang sempat menggerutu."
        moeka "Semuanya, maaf banget aku telat! Kereta tadi sempat tertahan di stasiun sebelumnya, terus aku harus lari ambil terpal dari ruang penyimpanan—tapi kalian boleh mengomel sepuasnya nanti setelah semuanya dapat tempat duduk, ya!"
        nar "Kalimat permintaan maaf itu bahkan belum selesai menggantung di udara ketika mata biru cerahnya sudah menyapu seluruh taman dalam sekali pandang—menakar arah cahaya matahari siang, letak akar pohon yang menonjol, serta barang bawaan di tangan setiap mahasiswa."
        moeka "Oke, kita bereskan dalam satu menit! Kalian berdua yang bawa kardus minuman—tolong taruh di bawah bayangan pohon kamper sebelah kiri sana ya, biar tehnya nggak jadi hangat kena matahari!"
        "Mahasiswi Tahun Pertama A" "Ah—iya, siap, Senpai!"
        moeka "Yang pegang kantong piring kertas sama sumpit, letakkan dulu di atas bangku panjang dekat pagar biar nggak diterbangkan angin! Nanti begitu terpalnya terhampar, baru kita pindahkan ke tengah!"
        nar "Hanya dalam hitungan detik, kebekuan yang sejak tadi menyelimuti taman langsung pecah. Para mahasiswa yang tadi berdiri canggung serentak bergerak mengikuti instruksinya tanpa ragu."
        nar "Sebelum melangkah ke tengah rumput, tatapan Moeka langsung menangkap mahasiswa baru berkacamata yang masih berdiri sendirian di dekat batang pohon kamper. Ia melambai lebar dengan suara akrab."
        moeka "Hei, Sato-kun yang kemarin ikut orientasi, kan? Jangan berdiri menyendiri di ujung sana dong! Bisa tolong pegangkan gulungan kantong sampah sama botol air buat pemberat sudut terpal nggak? Aku butuh bantuan orang yang teliti nih!"
        "Mahasiswa Tahun Pertama" "E-eh? Senpai hafal namaku? B-boleh, sini biar aku yang pegang!"
        nar "Wajah kaku pemuda itu seketika mencair penuh kelegaan, lalu ia bergegas masuk ke tengah rombongan. Dalam waktu kurang dari setengah menit, tidak ada lagi satu pun orang yang kebingungan."
        nar "Begitu alur kerumunan mulai bergerak teratur, Moeka memutar tubuhnya untuk mencari celah melintas di jalan setapak sambil menahan dua gulungan terpal berat di lengannya—dan pandangannya langsung tertumbuk padamu yang berdiri di dekat tembok rendah."
        nar "Alisnya terangkat sesaat, lalu wajahnya yang sedikit berkeringat langsung merekah dengan senyum usil khas teman satu kepanitiaan."
        moeka "Wah, panjang umur! Kisaragi Yutaka beneran datang ke Hanami gabungan, bukan cuma titip nama di daftar hadir? Maaf banget ya, Yutayuta, wakil panitiamu ini malah ngasih pertunjukan datang paling belakangan begini~"
        nar "'Yutayuta'... mendengar julukan seakrab itu dilemparkan begitu saja masih terasa ganjil di telingamu, seperti sedang dipanggil dengan nama panggilan milik orang lain yang jaketnya kebetulan kaupakai."
    call kk_family_menu("Mo01", ["Geser sedikit dan tahan dahan agar ia bisa lewat.", "\"Anak-anak tadi sudah menunggu lebih dari lima belas menit.\"", "Ambil gulungan terpalnya dan bantu membentangkan alas."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau memutuskan untuk tidak memperpanjang urusan saat tangannya sendiri jelas sedang penuh dan semua orang menunggu terpal itu dibuka. Tanpa melontarkan komentar apa pun, kau mundur selangkah ke tepi rumput dan mengangkat tangan kananmu untuk menahan dahan rendah pohon sakura yang menjuntai tepat di jalur kepala serta ujung gulungan terpal Moeka."
            nar "Moeka yang tadinya hendak menunduk terburu-buru sempat mengerjap kaget melihat dahan berbunga itu terangkat memberinya ruang lewat yang lega."
            moeka "Wah, penyelamat! Kalau nggak ditahan tadi, ujung terpalnya pasti sudah nyangkut dan rontokin kelopak ke rambutku semua. Makasih banyak ya, Chimian!"
            chiasa "Sama-sama, Moemoe-senpai. Urus bagian tengah dulu saja."
            moeka "Siap! Tunggu sebentar di situ ya, aku bereskan pembagian tempat anak-anak dulu baru aku balik lagi!"
            nar "Moeka mengedipkan sebelah mata dengan senyum lebar, lalu bergegas melewati jalan setapak menuju tanah lapang di bawah pohon sakura terbesar."
            nar "Dari tepi jalan setapak, kau tidak langsung pergi, melainkan memperhatikan bagaimana ia bekerja. Moeka menjatuhkan kedua gulungan terpal di rumput, berjongkok, dan langsung memanggil dua mahasiswa tahun pertama untuk menarik ujungnya berlawanan arah."
            moeka "Tarik pelan-pelan ke arah bangku sana—nah, tahan! Jangan terlalu mepet ke akar pohon yang menonjol itu, nanti kalau ada yang duduk malah sakit punggungnya!"
            nar "Ketika salah satu peserta hampir meletakkan kotak bento besar terlalu dekat ke pinggir jalur masuk terpal, Moeka langsung melompat ringan menghampirinya sambil tertawa."
            moeka "Eits, jangan taruh di pinggir situ dong! Nanti kalau keinjak kakiku yang jalannya nggak pakai rem ini, kita semua terpaksa makan nasi gepeng lho. Geser agak ke tengah sini biar yang duduk di ujung kanan juga gampang ambil!"
            nar "Tawa ringan langsung pecah dari kelompok mahasiswa baru itu. Lalu, saat melihat seorang mahasiswi bertubuh mungil masih berdiri ragu memeluk tasnya di tepi alas, Moeka menepuk ruang kosong di sebelah dua mahasiswi pembawa minuman tadi."
            moeka "Sini, duduk di sebelah mereka aja! Kalian sama-sama dari fakultas bahasa, kan? Pas banget, tadi mereka juga lagi bahas dosen mata kuliah pengantar yang katanya galak itu!"
            nar "Kau menyandarkan bahu ke pagar kayu, diam-diam merasa takjub. Di dalam manga, orang sering meremehkan Moeka sebagai sekadar gyaru berisik yang kerjanya cuma meramaikan suasana. Padahal kalau dilihat langsung seperti ini, setiap candaan dan gerakannya punya tujuan jelas—ia membaca canggungnya orang lain lebih cepat daripada siapa pun di taman ini."
            nar "Setelah seluruh rombongan duduk rapi di atas dua lembaran terpal biru dan suara obrolan mulai mengalir alami tanpa perlu dipandu lagi, Moeka berdiri, merenggangkan kedua bahunya yang tampak pegal, lalu berjalan kembali menghampirimu di tepi jalan setapak."
            nar "Ia berhenti di sebelahmu sambil mengipaskan telapak tangan ke lehernya. Napasnya kini jauh lebih teratur, meski rona hangat bekas berlari masih tersisa di pipinya."
            moeka "Fiuh... akhirnya semuanya duduk manis juga. Eh, Chimian, menurut mata anak jurusan ilustrasi gimana nih? Komposisi tempat duduknya sudah kelihatan seimbang belum, atau bagian pojok dekat semak sana masih terlalu sempit buat lewat?"
            nar "Kau menoleh mengamati hamparan terpal biru di depan kalian. Jalur tengah cukup lapang untuk orang berlalu-lalang mengambil minuman, sementara bayangan pohon menutupi hampir seluruh sisi yang ditempati para mahasiswa baru."
            chiasa "Bagian bawah pohon sebelah kanan sudah cukup lega kok, Moemoe-senpai. Jalur buat ambil minuman juga tidak terhalang, dan anak-anak tahun pertama yang tadi diam saja sekarang sudah kelihatan ikut mengobrol."
            moeka "Syukurlah kalau begitu~ Jujur aja, pas kereta tadi berhenti mendadak di tengah jalur, aku sempat panik setengah mati. Aku sudah membayangkan datang-datang anak-anak pada bubar atau malah pasang muka cemberut semua."
            nar "Moeka menghela napas kecil, lalu menoleh padamu dengan senyum yang terasa lebih lembut daripada saat ia berbicara di depan kerumunan tadi."
            moeka "Jadi begitu aku sampai terus lihat kau langsung minggir sambil tahanin dahan pohon buatku tanpa kasih tatapan menyalahkan, rasanya setengah panikku langsung hilang. Serius deh, itu ngebantu banget buat mentalku."
            chiasa "Moemoe-senpai sendiri kan langsung membereskan semuanya begitu datang."
            moeka "Tetap aja, nggak semua orang mau sabar nunggu aku bereskan dulu sebelum ngomel. Yuk, jangan berdiri terus di pinggir jalan setapak begini—duduk di sebelahku aja! Aku masih simpan minuman dingin di dalam tas, lumayan buat balas budi soal dahan sakura tadi."
            nar "Ia menarik pelan ujung lengan bajumu dengan akrab menuju sudut terpal yang masih teduh, tampak sungguh-sungguh menghargai ruang bernapas yang baru saja kau berikan kepadanya."
        else:
            nar "Kau memilih tidak menambah panjang daftar hal yang harus ia tangani saat kedua tangannya sedang penuh dan belasan mahasiswa baru menunggunya. Kau mengeluarkan satu tangan dari saku jaket, mundur selangkah ke tepi rumput, lalu mengangkat lenganmu untuk menahan dahan rendah pohon sakura yang menjuntai tepat di jalur ujung gulungan terpal Moeka."
            nar "Moeka yang tadinya hendak membungkuk buru-buru sempat mengerjap kaget melihat dahan berbunga itu terangkat tinggi melebihi kepalanya."
            moeka "Lho, tumben banget nih Kisaragi Yutaka jadi gentleman tanpa ngejek keterlambatanku duluan? Makasih ya, Yutayuta!"
            yutaka "Bereskan dulu yang di tengah sana. Soal ngejek bisa belakangan."
            moeka "Ahaha, nah gitu baru normal! Tunggu sebentar di situ ya, aku bereskan pembagian tempat duduk anak-anak dulu baru aku nyusul!"
            nar "Ia mengedipkan sebelah mata dengan senyum lebar, lalu bergegas melewati jalan setapak menuju hamparan rumput di bawah pohon sakura terbesar."
            nar "Dari tepi jalan setapak, kau melipat tangan di dada sambil mengamati cara kerjanya dengan rasa penasaran yang agak kering. Begitu menjatuhkan kedua gulungan terpal di rumput, Moeka langsung memanggil dua mahasiswa tahun pertama untuk menarik ujungnya, lalu cepat-cepat mencegat seorang mahasiswa senior yang mulai menggerutu soal keterlambatan."
            moeka "Aduh, maaf banget ya! Nanti bagian minuman dingin paling depan khusus buat kelompokmu deh, tapi sekarang bantu aku tahan ujung terpal sebelah sana dulu dong biar nggak terbang!"
            nar "Gerutuan pemuda itu langsung menguap jadi tawa canggung, dan detik berikutnya ia justru ikut berjongkok membantu. Kau tidak bisa menahan dengusan kecil—di balik reputasinya sebagai gyaru berisik, caranya memutar keluhan orang jadi tenaga kerja dalam sepuluh detik jelas bukan kebetulan."
            nar "Setelah seluruh rombongan duduk rapi di atas dua terpal biru dan obrolan mulai mengalir sendiri, Moeka berdiri, memutar bahunya yang tampak pegal, lalu berjalan santai menghampirimu sambil mengibaskan tangan ke lehernya."
            moeka "Fiuh... beres juga. Gimana penilaian sesama veteran panitia festival, Yutayuta? Masih layak dapat nilai lulus nggak penataanku hari ini?"
            yutaka "Lumayan. Apalagi trik memaksa orang yang mau protes jadi ikut pegang ujung terpal tadi."
            moeka "Ahaha, ketahuan deh! Jujur aja, pas kereta tadi berhenti mendadak di tengah jalur, aku sempat panik setengah mati. Kupikir sampai sini semua orang sudah pasang muka kesal."
            nar "Moeka menghela napas kecil, lalu menatapmu dengan senyum yang terasa lebih santai dan tidak dibuat-buat."
            moeka "Makanya pas lihat kau langsung kasih jalan sambil tahanin dahan pohon tanpa mulai ceramah dulu, rasanya setengah panikku langsung hilang. Makasih ya, Yutayuta."
            yutaka "Lagipula percuma juga mengomel sebelum terpalnya kebuka."
            moeka "Nah, itu baru logis! Yuk, jangan berdiri terus di pinggir kayak pengawas ujian—duduk di sebelahku aja, aku masih simpan teh dingin di tas buat bayaran dahan sakura tadi."
            nar "Ia menepuk ringan lengan jaketmu dengan akrab sambil menunjuk sudut terpal yang masih teduh."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kau tidak membalas senyum ramainya, dan juga tidak langsung menyingkir dari jalan setapak. Kau melirik sekilas ke arah dua mahasiswi yang tadi berdiri kepanasan memeluk kardus minuman serta mahasiswa berkacamata yang baru saja meletakkan kantong plastiknya, lalu kembali menatap Moeka dengan nada tenang namun lurus."
            chiasa "Acara memang langsung jalan begitu Moemoe-senpai datang. Tapi anak-anak tahun pertama di sebelah sana tadi sudah berdiri menunggu lebih dari lima belas menit di bawah matahari karena tidak ada yang berani membuka apa-apa duluan."
            nar "Langkah Moeka yang tadinya sudah siap melesat melewati jalan setapak langsung terhenti di tempat. Senyum cerah yang sejak tadi menempel rapat di wajahnya seperti topeng reflektif itu meredup dalam sepersekian detik."
            nar "Ia terdiam sejenak, lalu menoleh mengikuti arah pandanganmu ke kelompok mahasiswa tahun pertama yang sebagian sedang menyeka keringat di dahi mereka dengan tisu."
            nar "Kau sempat mengira ia akan tertawa canggung atau melempar candaan ringan untuk mencairkan suasana seperti yang biasa dilakukan karakter populer di manga. Namun tidak ada satu pun alasan klise yang keluar dari bibirnya."
            nar "Bahu Moeka turun sedikit. Kedua lengannya memeluk dua gulungan terpal biru itu lebih rapat ke dada, lalu ia menoleh kembali kepadamu dengan sorot mata biru yang jernih dan tampak sungguh-sungguh merasa bersalah."
            moeka "...Iya, kau benar. Aku nggak punya alasan buat membela diri soal itu."
            moeka "Maaf ya, Chimian. Dan maaf juga sudah bikin kalian semua berdiri kepanasan menunggu di sini tanpa kejelasan."
            nar "Nada suaranya turun satu oktaf—tidak lagi terdengar seperti pembawa acara yang berusaha menghibur kerumunan, melainkan suara seorang mahasiswi yang benar-benar menyadari kesalahannya."
            chiasa "Aku bilang begini bukan untuk menyudutkan Moemoe-senpai di depan yang lain. Cuma kalau memang terhambat di jalan, lebih baik kirim pesan singkat ke grup panitia atau tunjuk satu orang lebih dulu supaya yang sudah tiba tahu harus mulai dari mana."
            moeka "Iya... tadi waktu aku lari dari ruang penyimpanan bawa dua gulungan ini, ponselku jatuh tenggelam ke dasar tas kanvas. Aku pikir kalau aku lari cepat-cepat masih sempat sampai sebelum mereka selesai berkumpul, jadi aku nggak berhenti buat kirim pesan. Itu murni salah hitungku."
            nar "Moeka menghela napas pelan, lalu menatapmu dengan kesungguhan yang membuat sikapnya terasa jauh lebih dewasa daripada penampilannya yang penuh aksesori mencolok."
            moeka "Lain kali, kalau ada tanda-tanda telat lima menit saja, pasti langsung kukabari di grup dan kutunjuk satu panitia buat pegang komando sementara. Makasih ya, Chimian, sudah mau bilang langsung ke aku begini, bukan cuma dipendam."
            nar "Ia membungkuk kecil dengan sopan kepadamu sebelum akhirnya melangkah menuju tengah rumput."
            nar "Kau memperhatikan langkahnya dari tepi jalan setapak. Kali ini, Moeka tidak langsung melempar lelucon keras untuk menutupi keterlambatannya. Ia justru berjalan lebih dulu ke arah dua mahasiswi yang tadi memeluk kardus minuman."
            moeka "Hei, kalian berdua—maaf banget ya tadi jadi berdiri kepanasan lama gara-gara aku telat datang dan nggak ngabari dulu. Sini, biar aku yang bantu angkat kardusnya ke sini. Nanti begitu terpalnya kebuka, kalian duduk duluan di bagian paling teduh di bawah pohon itu, ya."
            "Mahasiswi Tahun Pertama A" "Eh, nggak apa-apa kok, Senpai! Kami juga nggak keberatan..."
            moeka "Nggak, salahku kok bikin kalian nunggu tanpa kabar. Kalau nanti haus duluan, langsung buka aja minumannya, nggak usah tunggu aba-aba dariku lagi, oke?"
            nar "Setelah memastikan keduanya mendapat tempat yang nyaman dan terpal tergelar rapi, Moeka bergerak membantu para peserta lain dengan tempo yang jauh lebih hati-hati—memeriksa apakah ada orang yang masih berdiri kebingungan atau menunggu jawaban darinya."
            nar "Saat semua orang akhirnya duduk di atas terpal, Moeka sempat mengangkat pandangan dari seberang rumput dan bertatapan singkat denganmu. Ia tidak membuang muka atau menunjukkan rasa kesal; ia justru mengangguk kecil dengan ekspresi yang lebih tenang dan sadar diri, sebelum kembali membagikan gelas kertas kepada rombongan."
        else:
            nar "Kau tidak ikut tertawa menanggapi godaannya. Kau tetap berdiri tenang di tempatmu, melirik sekilas ke arah dua mahasiswi yang tadi berdiri kepanasan memeluk kardus minuman serta mahasiswa berkacamata yang baru saja meletakkan kantong plastiknya, lalu kembali menatap Moeka dengan nada datar namun lugas."
            yutaka "Acara memang langsung jalan begitu kau datang, Kohinata. Tapi anak-anak tahun pertama di sebelah sana tadi sudah berdiri menunggu lebih dari lima belas menit di bawah matahari karena tidak ada yang berani memulai duluan."
            nar "Langkah Moeka yang tadinya siap melesat melewati jalan setapak langsung tertahan. Senyum usil yang sejak tadi menempel rapat di wajahnya meredup dalam sepersekian detik."
            nar "Ia tidak langsung membalas dengan candaan ataupun pembelaan. Ia menoleh mengikuti arah pandanganmu ke kelompok mahasiswa tahun pertama yang sebagian sedang menyeka pelipis mereka dengan tisu."
            nar "Bahu Moeka turun sedikit. Ia memeluk kedua gulungan terpal biru itu lebih rapat ke dada, lalu menoleh kembali kepadamu dengan mata biru yang jernih dan raut wajah yang sungguh-sungguh merasa bersalah."
            moeka "...Iya, kau benar, Yutayuta. Aku nggak ada pembelaan buat itu."
            moeka "Maaf sudah bikin kalian semua berdiri menunggu tanpa kejelasan."
            nar "Nada suaranya turun, kehilangan kesan berisik yang tadi ia pakai di depan kerumunan. Tidak ada tawa pengalihan sedikit pun—hanya pengakuan jujur yang terdengar jauh lebih dewasa daripada penampilannya yang mencolok."
            yutaka "Aku bilang begini bukan buat mempermalukanmu di depan anak baru. Cuma kalau memang terhambat di jalan, lebih baik kirim satu pesan singkat ke grup panitia atau tunjuk orang buat pegang sementara supaya yang sudah tiba tidak kebingungan."
            moeka "Iya... tadi waktu aku lari dari ruang penyimpanan bawa dua gulungan ini, ponselku jatuh tenggelam ke dasar tas kanvas. Aku terlalu yakin bisa sampai sebelum mereka selesai kumpul, jadi aku nggak berhenti buat kirim kabar. Itu murni salah hitungku."
            nar "Moeka menghela napas pelan, lalu menatapmu dengan kesungguhan yang tenang."
            moeka "Lain kali kalau ada tanda-tanda telat lima menit saja, pasti langsung kukabari lebih awal. Makasih ya, Yutayuta, sudah mau menegur langsung daripada cuma bercanda atau ngomongin di belakang."
            nar "Ia mengangguk kecil kepadamu sebelum melangkah menuju tengah rumput."
            nar "Dari tepi jalan setapak, kau mengamati bagaimana sikapnya langsung berubah. Alih-alih melempar lelucon keras untuk menutupi rasa canggung, Moeka berjalan lebih dulu menghampiri dua mahasiswi pembawa kardus minuman."
            moeka "Hei, kalian berdua—maaf banget ya tadi jadi berdiri kepanasan lama gara-gara aku telat datang dan nggak kasih kabar. Sini, biar aku yang bantu angkat kardusnya. Begitu terpalnya kebuka, kalian duduk duluan di bagian paling teduh sebelah dalam ini, ya."
            "Mahasiswi Tahun Pertama A" "Eh, nggak apa-apa kok, Senpai! Kami juga nggak keberatan..."
            moeka "Nggak, salahku kok bikin kalian nunggu tanpa kabar. Kalau haus duluan, langsung buka aja minumannya, nggak usah tunggu aba-aba dariku lagi, oke?"
            nar "Setelah keduanya duduk di tempat teduh dan kedua terpal tergelar rapi, Moeka bergerak menyusuri lingkaran peserta dengan tempo yang lebih hati-hati—memastikan tidak ada satu pun orang yang masih menunggu jawaban atau berdiri kebingungan."
            nar "Ketika seluruh rombongan akhirnya duduk, Moeka sempat mengangkat wajah dari seberang terpal dan bertatapan singkat denganmu. Tidak ada rasa kesal di sorot matanya; ia hanya mengangguk kecil dengan ekspresi yang lebih sadar dan tenang sebelum kembali membagikan gelas kertas."
    else:
        if kk_host == "chiasa":
            nar "Saat Moeka berbicara sambil membetulkan tali kamera yang merosot ke depan dadanya, salah satu gulungan terpal biru besar di lengan kanannya terlihat jelas mulai meluncur turun melewati lekuk sikunya. Sedetik lagi benda berat itu pasti jatuh menimpa sepatunya sendiri."
            nar "Tanpa menunggu ia meminta tolong, kau meletakkan tas jinjing kainmu di atas bangku kayu di sampingmu, lalu langsung melangkah maju menahan ujung gulungan terpal paling besar itu dan mengambil alihnya dari pelukan Moeka."
            moeka "Eh—Chimian?! Tunggu, berat lho itu! Nanti bajumu kotor kena debu gudang!"
            chiasa "Tidak seberat itu kok, Moemoe-senpai. Lagipula kalau jatuh tadi, nanti malah kena kameramu. Kita mau bentangkan dari sebelah mana dulu?"
            nar "Mata biru Moeka membulat sesaat karena terkejut, sebelum raut tegang tipis yang tersembunyi di balik senyumnya langsung luruh berganti kelegaan yang kentara."
            moeka "Wah, kau penyelamat hidupku hari ini! Kalau begitu, ikut aku ke tanah rumput yang rata di antara dua akar pohon sakura besar sebelah sana ya—kita bentangkan dari sana terus tarik memanjang ke arah bangku taman!"
            nar "Kau berjalan berdampingan dengannya ke titik yang ia tunjuk. Begitu sampai di tepi rumput, kau berjongkok dan melepas simpul tali rafia yang mengikat gulungan terpal itu, lalu memegang dua sudutnya sementara Moeka berjalan mundur perlahan membuka lipatan hingga lembaran plastik biru lebar itu terhampar di atas rumput."
            nar "Baru saja kalian meluruskannya, embusan angin April yang cukup kencang menyapu taman dan menerbangkan sudut kanan terpal hingga terlipat kembali ke tengah."
            moeka "Waduh, anginnya nakal banget! Chimian, tahan sudut yang di dekatmu sebentar—Sato-kun! Boleh tolong taruh dua botol air pemberat di pojok sebelah kiri sini?!"
            nar "Moeka cepat-cepat menindih tepi terpal dengan satu lututnya sambil merapikan lipatan, sementara kau menarik kencang ujung di sisimu dan menaruh tas kanvas besar milik Moeka di sudut agar lembaran itu tidak terangkat lagi. Sato segera berlari kecil meletakkan pemberat di sisi yang diminta."
            moeka "Sip, mantap! Sekarang kita buka terpal kedua di sebelahnya, tapi sisakan jarak sekitar dua langkah di tengah ya, Chimian."
            chiasa "Jangan dirapatkan sekalian, Senpai?"
            moeka "Jangan~ Kalau terlalu rapat, nanti orang yang mau jalan dari baris belakang ke kotak minuman harus melangkahi piring makanan atau malah nggak sengaja menginjak rok anak-anak cewek. Kalau ada lorong kecil di tengah, semua bisa keluar masuk dengan enak."
            nar "Dari jarak sedekat ini, kau bisa melihat dengan jelas bagaimana pikiran Moeka bekerja di balik gaya bicaranya yang lincah dan penuh canda. Sambil kalian menarik lembaran terpal kedua, ia menghitung jumlah mahasiswa dalam sekali pandang, lalu sedikit menyerongkan sudut terpal mengikuti jatuhnya bayangan dahan sakura."
            moeka "Nah, agak miring sedikit ke kanan biar bagian belakangnya nggak kepotong batang pohon besar ini. Jadi nggak ada satu pun yang terpaksa duduk terpisah di belakang pohon sendirian."
            chiasa "Rapi sekali hitungannya."
            moeka "Hehe, kalau soal beginian aku lumayan cerewet. Ayo semuanya, alasnya sudah siap! Sepatunya boleh dilepas di pinggir rumput sebelah luar ya, biar terpalnya nggak kotor kena tanah!"
            nar "Begitu aba-aba itu terdengar, para mahasiswa langsung berdatangan melepas sepatu, menata kotak bento, dan duduk berkelompok di atas kedua terpal yang baru kalian bentangkan. Dalam hitungan menit, suara tawa, obrolan perkenalan, dan bunyi kaleng minuman yang dibuka mulai memenuhi taman."
            nar "Moeka berdiri mengamati seluruh lingkaran itu beberapa detik lagi untuk memastikan tidak ada yang kekurangan gelas atau tempat duduk. Baru setelah semuanya benar-benar beres, ia menghela napas panjang dan menjatuhkan diri duduk bersila tepat di sebelahmu di pinggir terpal."
            nar "Ia melepas tali kamera dari lehernya, meletakkannya hati-hati di atas tas kanvas, lalu menyeka pelipisnya yang lembap dengan punggung tangan sebelum menoleh kepadamu dengan senyum miring penuh bangga."
            moeka "Nah, beres semuanya! Gimana? Jangan percaya ya, Chimian, kalau nanti di kampus ada yang bilang senpai-mu ini cuma bagian meramaikan acara doang. Aku juga lumayan jago lho bikin keramaian punya tempat duduk yang pas."
            chiasa "Kelihatan kok. Untuk ukuran orang yang datang terlambat, cara Moemoe-senpai membaca ruang, menyisakan lorong makanan, sampai mengatur biar tidak ada yang duduk terpisah tadi rapi sekali."
            moeka "Hehe, kebiasaan lama waktu masih jadi wakil ketua OSIS pas SMA dulu soalnya~ Susah hilang walaupun sekarang sudah jadi mahasiswi Seni yang kerjanya berantakan di studio jahit."
            nar "Tawanya kali ini terdengar berbeda—tidak setinggi atau sekeras saat ia menyapa kerumunan tadi, melainkan jauh lebih santai dan rendah. Ia merogoh tas kanvasnya, mengambil dua botol teh oolong dingin yang dinding plastiknya masih berembun, lalu menyodorkan satu kepadamu."
            moeka "Nih, buat asisten dadakan paling sigap hari ini. Tapi serius deh, Chimian... kalau tadi kau nggak langsung ambil gulungan terpal itu dari lenganku, mungkin aku sudah tersandung dan terguling duluan di depan anak-anak tahun pertama. Makasih banyak ya."
            chiasa "Sama-sama, Moemoe-senpai. Terima kasih tehnya."
            nar "Kau menerima botol dingin itu. Di bawah guguran kelopak sakura yang jatuh pelan menempel di sudut terpal biru, Moeka memutar tutup botolnya dan meneguk tehnya sambil menatap keramaian mahasiswa baru yang sedang tertawa—dan untuk beberapa detik yang tenang itu, senyum di wajahnya tampak jauh lebih jujur daripada topeng ceria yang biasa ia pasang di hadapan orang banyak."
        else:
            nar "Saat Moeka berbicara sambil membetulkan tali kamera yang merosot ke depan dadanya, salah satu gulungan terpal biru besar di lengan kanannya terlihat jelas mulai meluncur turun melewati lekuk sikunya. Sedetik lagi benda berat itu pasti jatuh menimpa sepatunya sendiri."
            nar "Tanpa banyak bicara, kau langsung mengeluarkan kedua tangan dari saku jaket, melangkah maju, dan mengangkat gulungan terpal yang paling besar itu keluar dari pelukan Moeka dengan mudah."
            moeka "Eh—Yutayuta?! Tunggu, itu penuh debu gudang lho, nanti jaket bagusmu kotor!"
            yutaka "Tinggal dikebas nanti. Daripada jatuh kena kameramu. Mau dibentangkan dari sebelah mana dulu?"
            nar "Mata biru Moeka membulat sesaat karena terkejut, sebelum raut tegang tipis yang tersembunyi di balik senyum usilnya langsung luruh berganti kelegaan yang kentara."
            moeka "Wah, tumben banget sigap tanpa diminta! Kalau begitu ikut aku ke tanah rumput yang rata di antara dua akar pohon sakura besar sebelah sana—kita bentangkan dari sana terus tarik memanjang ke arah bangku taman!"
            nar "Kau berjalan berdampingan dengannya menuju titik yang ia tunjuk. Begitu sampai, kau berjongkok melepas simpul tali rafia pengikat terpal, lalu menahan kedua sudutnya sementara Moeka berjalan mundur membuka gulungan hingga lembaran plastik biru lebar itu terhampar di atas rumput."
            nar "Baru saja kalian meluruskannya, embusan angin April yang cukup kencang menyapu taman dan menerbangkan sudut kanan terpal hingga terlipat kembali ke tengah."
            moeka "Waduh, anginnya nakal banget! Yutayuta, tahan ujung sebelah situ sebentar—Sato-kun! Boleh tolong taruh dua botol air pemberat di pojok sebelah kiri sini?!"
            nar "Moeka cepat-cepat menindih tepi terpal dengan satu lututnya sambil merapikan lipatan, sementara kau menarik kencang sudut di sisimu dan meletakkan tas kanvas besar milik Moeka di ujung agar lembaran itu tidak terangkat lagi. Sato segera berlari kecil menaruh pemberat di sisi yang diminta."
            moeka "Sip, beres satu! Sekarang kita buka terpal kedua di sebelahnya, tapi sisakan jarak sekitar dua langkah di tengah ya, Yutayuta."
            yutaka "Bukan dirapatkan sekalian?"
            moeka "Jangan~ Kalau dirapatkan, nanti orang dari baris belakang yang mau ambil minuman harus melangkahi piring makanan atau malah nggak sengaja menginjak rok anak-anak cewek. Kalau ada lorong kecil di tengah, semua bisa keluar masuk tanpa repot."
            nar "Dari jarak sedekat ini, kau bisa melihat dengan jelas bagaimana pikiran Moeka bekerja di balik gaya bicaranya yang lincah dan penuh canda. Sambil kalian menarik lembaran terpal kedua, ia menghitung jumlah mahasiswa dalam sekali pandang, lalu sedikit menyerongkan sudut terpal mengikuti jatuhnya bayangan dahan sakura."
            moeka "Nah, agak miring sedikit ke kanan biar bagian belakangnya nggak kepotong batang pohon besar ini. Jadi nggak ada satu pun yang terpaksa duduk terpisah di belakang pohon sendirian."
            yutaka "Rapi sekali hitungannya."
            moeka "Hehe, kalau urusan tata tempat aku memang lumayan cerewet. Ayo semuanya, alasnya sudah siap! Sepatunya boleh dilepas di pinggir rumput sebelah luar ya, biar terpalnya nggak kotor kena tanah!"
            nar "Begitu aba-aba itu terdengar, para mahasiswa langsung berdatangan melepas sepatu, menata kotak bento, dan duduk berkelompok di atas kedua terpal yang baru kalian bentangkan. Dalam hitungan menit, suara tawa, obrolan perkenalan, dan bunyi kaleng minuman yang dibuka mulai memenuhi taman."
            nar "Moeka berdiri mengamati seluruh lingkaran itu beberapa detik lagi untuk memastikan tidak ada yang kekurangan gelas atau tempat duduk. Baru setelah semuanya benar-benar beres, ia menghela napas panjang dan menjatuhkan diri duduk bersila tepat di sebelahmu di pinggir terpal."
            nar "Ia melepas tali kamera dari lehernya, meletakkannya hati-hati di atas tas kanvas, lalu menyeka pelipisnya yang lembap dengan punggung tangan sebelum menoleh kepadamu dengan senyum miring penuh bangga."
            moeka "Nah, beres semuanya! Gimana? Jangan percaya ya, Yutayuta, kalau nanti di kampus ada yang bilang aku cuma bagian meramaikan acara doang. Aku juga pandai lho bikin keramaian punya tempat duduk yang pas."
            yutaka "Kelihatan kok. Untuk ukuran orang yang datang terlambat, caramu membaca ruang, menyisakan lorong makanan, sampai memastikan tidak ada yang duduk terpisah tadi rapi sekali."
            moeka "Hehe, kebiasaan lama waktu masih jadi wakil ketua OSIS pas SMA dulu soalnya~ Susah hilang walaupun sekarang tiap hari lebih sering berantakan di studio jahit."
            nar "Tawanya kali ini terdengar berbeda—tidak setinggi atau sekeras saat ia menyapa kerumunan tadi. Dari jarak sedekat ini, di balik riasan matanya yang rapi, kau sempat menangkap bayangan lelah tipis yang jarang ia perlihatkan kepada orang lain. Ia merogoh tas kanvasnya, mengambil dua botol teh oolong dingin yang dinding plastiknya masih berembun, lalu menyodorkan satu kepadamu."
            moeka "Nih, buat rekan kerja dadakan paling bisa diandalkan hari ini. Serius deh, Yutayuta... kalau tadi kau nggak langsung ambil gulungan terpal itu dari lenganku, mungkin aku sudah tersandung duluan di depan anak-anak baru. Makasih banyak ya."
            yutaka "Lain kali kalau memang keberatan, tinggal minta tolong saja daripada memaksa bawa dua gulungan sekaligus. Terima kasih tehnya."
            nar "Moeka tertegun sepersekian detik mendengar ucapanmu yang blak-blakan itu, lalu tertawa pelan sambil membuka tutup botolnya sendiri—dan untuk beberapa detik yang tenang di bawah guguran sakura, rasa lega di wajahnya tampak begitu jujur."
    return

# ┌─ PANDUAN CERITA · S01 · Papan Shogi di Taman
# │ LOKASI  : Kampus Kouseikan · Taman Kampus
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia bermain sendiri.
# │ INTI    : A menantang / B mengamati / C lewat.
# │ AKHIRAN : A membuka rivalitas.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S01:
    call kk_scene_enter("shiori", "Hanami · Taman Kampus")
    if kk_host == "chiasa":
        nar "Agak menjauh dari area rumput tengah tempat puluhan mahasiswa menggelar terpal piknik Hanami, sisi barat Taman Kampus terasa jauh lebih teduh dan lengang. Angin April masih terus menggugurkan kelopak sakura pucat ke atas jalan setapak batu dan bangku-bangku di bawah pohon tua."
        nar "Saat kau berjalan santai menyusuri jalur itu untuk mencari udara segar sejenak, bunyi 'klak' yang jernih dan mantap dari kayu yang beradu menarik perhatianmu."
        nar "Di sebuah meja batu teduh di pinggir taman, duduk seorang mahasiswi yang bahkan di tengah acara piknik kampus pun tampak seperti berada di ruang tersendiri. Rambut putih keperakannya ditata rapi dengan bagian atas menyilang bervolume dan gelombang panjang yang jatuh anggun ke depan melewati bahu. Pakaian semi-formalnya terlihat halus dan mahal, tetapi sama sekali tidak berlebihan."
        nar "Saionji Shiori—nama yang sempat kaudengar disebut-sebut para mahasiswa dengan julukan Ratu Fakultas. Kau belum pernah berbicara dengannya dan tidak tahu banyak soal dirinya selain kesan pertama bahwa ia tampak sama sekali tidak terganggu oleh keramaian di sekelilingnya."
        nar "Di hadapannya terbentang sebuah papan shogi kayu lipat. Dengan jari-jari rampingnya, Shiori mengangkat satu bidak kayu, meletakkannya di petak tengah dengan bunyi tajam, menatap formasi itu selama beberapa detik, lalu dengan tenang memutar seluruh papan seratus delapan puluh derajat agar ia dapat menakar posisi yang sama dari sisi lawan."
        nar "Tepat ketika ia hendak menggerakkan bidak berikutnya, sehelai kelopak sakura melayang turun dan mendarat persis di antara dua garis petak. Shiori tidak meniupnya begitu saja; ia menjepit kelopak merah muda itu dengan dua jari dan meletakkannya rapi di pinggir meja batu, seolah benda itu tamu tak diundang yang salah memilih kursi."
        nar "Tanpa tergesa sedikit pun, sepasang mata ungu amethyst-nya naik menatap ke arahmu. Senyum tipis yang ramah dan penuh percaya diri langsung tersungging di bibirnya."
        shiori "Selamat siang. Kalau kamu ingin duduk beristirahat di bangku ini, silakan saja—tempatnya masih cukup luas."
        nar "Ia sedikit memiringkan kepala, nada suaranya halus dan sopan, namun terasa seperti sedang menakar seberapa cepat kau akan bereaksi."
        shiori "Dan kalau kamu hendak bertanya mengapa ada orang yang bermain shogi sendirian di tengah keramaian Hanami, jawabannya sangat sederhana: karena sejauh ini belum ada yang duduk di seberang."
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
    else:
        if kk_host == "chiasa":
            nar "Kau membalas senyum sopannya dengan anggukan ringan dan memilih tidak memecah keheningan di meja batu teduh itu."
            chiasa "Terima kasih tawarannya, Saionji-senpai. Tapi aku cuma lewat mencari angin sebentar—aku tidak mau mengganggu permainanmu."
            shiori "Begitu, ya. Terima kasih sudah menyapa. Selamat menikmati Hanami-nya juga."
            nar "Shiori mengangguk anggun tanpa sedikit pun raut kecewa ataupun berusaha menahan langkahmu. Senyum di bibirnya tetap sama tenangnya seperti saat kau pertama kali mendekat."
            nar "Kau berbalik dan melangkah kembali menuju jalan setapak yang dipenuhi guguran kelopak sakura. Belum lima langkah kau menjauh, bunyi 'klak' bidak kayu yang diletakkan di papan kembali terdengar mantap di belakangmu—tanda bahwa Shiori memiliki kesenangan sendiri yang tetap berjalan utuh tanpa perlu memintamu menjadi penonton."
        else:
            nar "Kau mengangguk sopan tanpa berniat mengganggu ketenangan sudut taman itu."
            yutaka "Makasih tawarannya, Saionji-san. Aku cuma lewat cari angin sebentar—lanjutkan saja permainanmu."
            shiori "Baiklah. Selamat menikmati Hanami-nya, Kisaragi-san."
            nar "Shiori mengangguk anggun tanpa sedikit pun raut kecewa. Begitu kau berbalik dan melangkah menjauh menyusuri jalan setapak, bunyi 'klak' bidak kayu kembali terdengar mantap di belakangmu—menegaskan bahwa ia punya kesenangan sendiri yang tetap berlangsung utuh tanpa perlu penonton."
    return

# ┌─ PANDUAN CERITA · Mo02 · Undian Onsen
# │ LOKASI  : Stasiun & Pasar · Stasiun Kouseikan-mae
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia memenangkan undian.
# │ INTI    : A ucapkan selamat / B iri / C bantu rencana.
# │ AKHIRAN : kedekatan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo02:
    call kk_scene_enter("moeka", "Stasiun Kouseikan-mae")
    if kk_host == "chiasa":
        nar "Sore hari di depan perbelanjaan dekat Stasiun Kouseikan-mae cukup ramai oleh mahasiswa dan warga sekitar yang baru pulang beraktivitas. Di dekat pintu kaca pusat perbelanjaan, sebuah stan undian belanja berhias pita warna-warni masih memutar lonceng kuningan setiap kali ada pembeli yang mendapat hadiah kecil."
        nar "Kau baru saja keluar dari gerbang tiket stasiun sambil menenteng tas kainmu ketika suara teriakan tertahan yang familiar membuat beberapa orang menoleh ke arah meja undian."
        nar "Di sana, Kohinata Moeka berdiri membeku sambil menggenggam selembar kupon hadiah bergambar pemandian air panas dengan kedua tangannya—seolah takut kertas itu mendadak berubah menjadi salah baca kalau ia berkedip terlalu lama. Di sampingnya, petugas stan baru saja berhenti membunyikan lonceng besar warna emas."
        nar "Begitu matanya yang biru cerah menangkap sosokmu yang berjalan melintas di trotoar, Moeka langsung berlari kecil menghampirimu sambil mengacungkan kertas undian itu hati-hati."
        moeka "Chimian! Chimian, tolong cubit pipiku sebentar—ini beneran tulisan hadiah utama paket perjalanan onsen buat rombongan, kan?! Aku nggak salah baca huruf kanjinya, kan?!"
        nar "Kau menunduk membaca tulisan tercetak tebal di kertas itu: kupon menginap rombongan di sebuah ryokan pemandian air panas, lengkap dengan kolom tanggal keberangkatan yang harus segera dikonfirmasi sebelum akhir bulan."
        chiasa "Beneran hadiah utama, Moemoe-senpai. Lengkap sama jatah kamar rombongannya."
        moeka "Menang! Seriusan aku menang?! Padahal tadi aku cuma ikut mutar roda undian gara-gara kupon belanja dari minimarket sama toko kain hampir habis masa berlakunya hari ini!"
        nar "Moeka tertawa kecil penuh semangat, lalu tawa itu melambat sepersekian detik saat ia menatap lembaran syarat dan tanggal di bagian bawah kupon. Alisnya sedikit berkerut antara senang dan cemas."
        moeka "Wah... sekarang kita beneran harus bikin rencana perjalanan, dong. Seru banget sih, tapi agak seram juga ya—soalnya rencananya harus benar-benar rapi biar nggak kacau pas hari-H."
        if any(c["ev"] == "Mo01" and c["key"] == "C" for c in choices_log):
            nar "Melihat caranya langsung memikirkan daftar peserta dan jadwal di tengah rasa kagetnya, kau teringat betul bagaimana ia mengatur kerumunan dan terpal saat piknik Hanami kemarin."
    else:
        nar "Sore hari di depan perbelanjaan dekat Stasiun Kouseikan-mae cukup padat oleh mahasiswa dan pekerja yang baru turun dari kereta. Di dekat pintu kaca mal kecil, sebuah stan undian belanja berhias pita warna-warni baru saja membunyikan lonceng emas besar berkali-kali."
        nar "Kau baru melangkah keluar dari gerbang tiket dengan kedua tangan terselip di saku jaket ketika melihat Kohinata Moeka berdiri membeku di samping meja undian. Kedua tangannya memegang erat selembar kupon hadiah bergambar pemandian air panas—seolah takut tulisan di kertas itu berubah jadi salah baca kalau ia menatapnya terlalu lama."
        nar "Begitu matanya yang biru cerah menangkap sosokmu di trotoar, Moeka langsung berlari kecil menghampirimu sambil mengangkat kupon itu setinggi dada."
        moeka "Yutayuta! Tolong baca keras-keras tulisan paling atas ini—ini beneran hadiah utama paket onsen rombongan, kan?! Aku nggak lagi halu gara-gara kurang tidur, kan?!"
        nar "Kau menunduk sekilas membaca cetakan tebal di kertas itu: kupon menginap rombongan di sebuah ryokan pemandian air panas lengkap dengan kolom tanggal yang perlu dipilih."
        yutaka "Beneran paket menginap rombongan, Kohinata. Bukan hadiah tisu."
        moeka "Menang! Seriusan menang?! Padahal aku tadinya cuma ikut mutar roda undian gara-gara kupon belanja dari minimarket sama toko kain hampir habis masa berlakunya hari ini!"
        nar "Tawa hebohnya melambat sepersekian detik saat ia melirik daftar syarat dan tanggal di bagian bawah kupon. Alisnya sedikit berkerut antara senang dan cemas."
        moeka "Waduh... berarti sekarang kita betulan harus bikin rencana perjalanan, ya. Seru sih, tapi agak seram juga—soalnya kalau rencananya nggak rapi, nanti malah berantakan pas hari-H."
        if any(c["ev"] == "Mo01" and c["key"] == "C" for c in choices_log):
            nar "Melihat caranya langsung memikirkan susunan rombongan di tengah rasa kagetnya, kau langsung teringat bagaimana ia mengatur terpal dan peserta saat piknik Hanami kemarin."
    call kk_family_menu("Mo02", ["\"Selamat! Nikmati dulu saja rasa senangnya.\"", "\"Wah, iri juga sih bisa seberuntung itu.\"", "Tawarkan bantuan untuk ikut memeriksa rencana perjalanannya."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau tersenyum dan memutuskan membiarkannya menikmati momen langka itu tanpa langsung membebaninya dengan urusan jadwal dan daftar nama."
            chiasa "Selamat, Moemoe-senpai! Urusan jadwal bisa dipikirkan nanti malam—sekarang nikmati dulu saja rasa senangnya."
            nar "Bahu Moeka yang sempat sedikit naik karena memikirkan teknis acara langsung mengendur. Ia menatap kembali tiket di tangannya, lalu tertawa lepas."
            moeka "Hehe... iya juga ya! Rasanya masih belum percaya banget. Tahu nggak, Chimian, tadi pagi waktu aku bereskan dompet, kupon struknya hampir ikut kubuang ke tempat sampah dekat mesin tiket lho."
            chiasa "Untung tidak jadi dibuang."
            moeka "Asli! Biasanya kalau urusan barang kecil begini aku selalu ceroboh dan berakhir nyesel sendiri. Tapi kali ini malah jadi tiket onsen! Rasanya kayak sekali-sekali semesta lagi baik banget sama aku~"
            nar "Ia menyelipkan kupon hadiah itu ke dalam map plastik kecil di tas kanvasnya dengan gerakan ekstra hati-hati—sangat berbeda dari kebiasaannya yang serba tergesa—lalu menoleh padamu dengan wajah berseri-seri."
            moeka "Nanti begitu tanggalnya ketemu, Chimian wajib ikut ya! Pokoknya nggak boleh absen!"
            nar "Melihat kegembiraannya yang begitu ringan tanpa sedikit pun beban tambahan, kau hanya mengangguk sambil tersenyum tipis."
        else:
            nar "Kau mengeluarkan senyum santai dan memilih tidak langsung menambah bebannya dengan urusan jadwal, daftar nama, ataupun pembagian ongkos."
            yutaka "Selamat, Kohinata. Urusan jadwal dan siapa saja yang ikut bisa dipikirkan nanti malam—sekarang nikmati dulu saja rasa menangnya."
            nar "Bahu Moeka yang sempat sedikit naik karena memikirkan teknis acara langsung turun lega. Ia menatap kembali kupon di kedua tangannya, lalu tertawa lepas sampai beberapa pejalan kaki di depan stasiun ikut menoleh tersenyum."
            moeka "Hehe... iya juga ya! Rasanya masih belum percaya banget. Tahu nggak, Yutayuta, tadi pagi waktu aku bereskan dompet di kamar, struk belanja buat undian ini hampir ikut kubuang ke tempat sampah dekat mesin tiket lho."
            yutaka "Untung nggak jadi dibuang. Kalau jadi dibuang terus baru sadar, bisa kepikiran seminggu tuh."
            moeka "Asli! Biasanya kalau urusan barang kecil begini aku selalu ceroboh dan berakhir nyesel belakangan. Tapi kali ini kesalahan kecil malah nggak kejadian! Rasanya kayak sekali-sekali semesta lagi baik banget sama aku~"
            nar "Ia membuka tas kanvasnya yang penuh sesak, mengambil map plastik bening kecil, lalu menyelipkan kupon hadiah itu ke dalamnya dengan gerakan ekstra hati-hati—sangat kontras dengan kebiasaannya yang serba tergesa."
            moeka "Pokoknya nanti begitu tanggalnya ketemu, Yutayuta wajib ikut ya! Nggak boleh kabur pakai alasan sibuk!"
            yutaka "Iya, kabari saja kalau sudah jelas tanggalnya."
            nar "Melihat kegembiraannya yang begitu ringan tanpa sedikit pun beban tambahan, kau hanya mengangguk sambil melihatnya melangkah riang menuju peron."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kau menatap kertas undian itu lalu melontarkan komentar jujur yang agak kering tanpa banyak berpikir."
            chiasa "Wah, iri juga sih. Aku bahkan tidak pernah dapat hadiah tisu dari undian belanja, tapi Moemoe-senpai malah langsung dapat paket menginap."
            nar "Senyum lebar di wajah Moeka surut sepersekian detik. Ia menurunkan sedikit kupon di tangannya, menunduk menatap kertas itu dengan ekspresi canggung, seolah mendadak ragu apakah kegembiraannya tadi terlihat berlebihan."
            moeka "Eh... kalau aku yang beneran berharap menang, biasanya malah meleset terus kok, Chimian. Ini beneran cuma kebetulan saja."
            chiasa "Tetap saja, itu keberuntungan besar."
            nar "Moeka diam sejenak sambil memutar sudut kertas di antara jari-jarinya, lalu mengangkat wajah kembali menatapmu dengan nada yang lebih pelan."
            moeka "Tapi... nanti Chimian juga ikut pergi dan menikmati onsen-nya bareng-bareng, kan? Aku nggak mau hadiah ini malah bikin kita jadi hitung-hitungan siapa yang lebih beruntung."
            chiasa "Iya, tentu saja. Maaf kalau tadi kedengaran sinis."
            nar "Ia mengangguk kecil dan kembali tersenyum, tetapi binar meluap-luap yang tadi memenuhi matanya tampak sudah jauh lebih tertahan saat ia menyimpan kupon itu ke dalam tas."
        else:
            nar "Kau menatap kupon hadiah di tangannya lalu melontarkan komentar jujur yang agak kering tanpa menyaring nadamu."
            yutaka "Jujur saja, agak iri juga. Aku yang bolak-balik belanja di sini nggak pernah dapat apa-apa selain permen, kau malah sekali putar langsung dapat paket onsen."
            nar "Senyum lebar di wajah Moeka langsung surut sepersekian detik. Ia menurunkan kedua tangannya perlahan dan menunduk menatap kertas undian itu dengan raut canggung, seolah mendadak ragu apakah kegembiraannya barusan terlihat berlebihan."
            moeka "Eh... kalau aku yang beneran berharap menang, biasanya malah meleset terus kok, Yutayuta. Ini beneran cuma kebetulan saja."
            yutaka "Tetap saja, itu keberuntungan yang jarang kejadian."
            nar "Moeka terdiam sejenak sambil memutar-mutar sudut kertas di antara jari-jarinya. Ketika ia mengangkat wajah menatapmu lagi, nada suaranya sudah turun jauh lebih pelan."
            moeka "Lagipula kamu juga bakal ikut pergi dan menikmati onsen-nya bareng-bareng, kan? Aku nggak ingin hadiah ini malah jadi alasan kita menghitung siapa yang lebih beruntung."
            yutaka "Iya, tentu saja. Maaf kalau tadi kedengaran sinis, cuma nyeletuk."
            nar "Ia mengangguk kecil dan kembali memasang senyum tipis, tetapi binar meluap-luap yang tadi memenuhi mata birunya sudah jauh lebih tertahan saat ia menyimpan kupon itu ke dalam tas."
    else:
        if kk_host == "chiasa":
            nar "Melihat raut cemas tipis di balik kegembiraan Moeka saat membaca tulisan syarat kecil di bagian bawah kertas, kau melangkah setengah langkah lebih dekat dan menunjuk bangku panjang di dekat taman kecil depan stasiun."
            chiasa "Kalau mau, kita duduk sebentar di bangku sana sambil mengecek syarat dan tanggalnya sekarang, Moemoe-senpai. Biar lebih jelas apa saja yang perlu disiapkan."
            nar "Mata biru Moeka langsung berbinar lega—jauh lebih tulus daripada tawa hebohnya semenit lalu."
            moeka "Boleh banget! Ayo! Chimian baca dari daftar syarat paling atas ya, nanti aku catat di ponsel siapa saja yang kira-kira bisa ikut dan tanggal mana yang nggak bentrok sama jadwal kuliah!"
            nar "Kalian duduk berdampingan di bangku kayu depan stasiun. Kau membacakan poin demi poin: batas akhir reservasi ryokan, jumlah kamar yang ditanggung kupon, serta biaya transportasi kereta dan makan tambahan yang tidak termasuk dalam hadiah."
            moeka "Oke, berarti kereta pulang-pergi kita patungan sendiri—untung nggak terlalu mahal kalau pakai tiket rombongan. Terus soal daftar peserta, nanti aku kabari di grup malam ini biar semua bisa konfirmasi sebelum Jumat."
            chiasa "Jangan lupa catat juga siapa yang punya alergi makanan sebelum telepon ryokan-nya, Senpai."
            moeka "Wah, iya juga! Hampir saja kelewat kalau nggak kauingatkan. Serius deh, Chimian, kalau mikir angkanya bareng begini rasanya langsung tenang banget—nggak kerasa kayak harus mengingat semuanya sendirian di kepalaku."
            nar "Ia menepuk buku catatan kecilnya dengan senyum puas yang hangat. Kegembiraannya kini terasa jauh lebih mantap karena bukan lagi beban yang harus ia pikul sendiri."
        else:
            nar "Melihat kening Moeka yang mulai berkerut kecil membaca deretan tulisan syarat di bagian bawah kupon, kau mengeluarkan tangan dari saku jaket dan menunjuk bangku panjang di dekat taman kecil depan stasiun."
            yutaka "Sini, kita duduk sebentar di bangku sana sambil mengecek syarat dan hitungan biayanya, Kohinata. Mumpung aku juga biasa pegang urusan dana kalau kepanitiaan, jadi lebih cepat beres."
            nar "Wajah Moeka langsung berseri lega—jauh lebih tulus dan tenang daripada tawa hebohnya semenit lalu."
            moeka "Boleh banget! Ayo! Yutayuta baca dari baris syarat paling atas ya, nanti aku catat di ponsel siapa saja yang kira-kira bisa ikut dan tanggal mana yang nggak bentrok!"
            nar "Kalian duduk berdampingan di bangku kayu di bawah lampu jalan yang mulai menyala. Kau membacakan poin demi poin: batas akhir reservasi ryokan, jumlah kamar yang ditanggung kupon, jam check-in, serta biaya kereta pulang-pergi dan makan tambahan di luar paket."
            moeka "Oke, berarti kereta pulang-pergi kita patungan sendiri—untung kalau pakai tiket rombongan potongannya lumayan, jadi masih aman banget di kantong. Nanti malam langsung kulempar ke grup biar semua konfirmasi sebelum Jumat."
            yutaka "Jangan lupa tanyakan juga ke ryokan-nya soal aturan pembatalan sama menu buat yang punya alergi makanan."
            moeka "Wah, iya juga! Hampir saja kelewat kalau nggak kauingatkan. Serius deh, Yutayuta—kalau angkanya sudah jelas dan ada yang bantu mengingat bareng begini, rasanya langsung tenang banget. Nggak kerasa kayak harus kupikul sendirian di kepalaku."
            nar "Ia menepuk buku catatan kecilnya dengan senyum puas yang hangat. Kegembiraannya kini berdiri di atas rencana nyata yang sanggup ia pegang."
    return

# ┌─ PANDUAN CERITA · S02 · Ruang Catur di Ryokan
# │ LOKASI  : Lobi ryokan
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : papan di lobi.
# │ INTI    : A bertanding / B sengaja kalah / C menang.
# │ AKHIRAN : B membuat ia jengkel.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S02:
    call kk_scene_enter("shiori", "Lobi ryokan")
    if kk_host == "chiasa":
        nar "Malam hari di lobi penginapan ryokan terasa jauh lebih tenang daripada ruang makan yang tadi penuh obrolan rombongan. Cahaya lampu kuning hangat dari lentera kertas memantul lembut di atas lantai kayu gelap, sementara suara air pancuran bambu di taman luar sesekali terdengar menembus pintu kaca."
        nar "Di sudut ruang tunggu yang menghadap ke taman, Saionji Shiori duduk anggun mengenakan yukata penginapan berwarna biru tua bermotif bunga halus. Rambut putih keperakannya yang panjang jatuh bergelombang melewati bahu saat ia menata barisan bidak kayu di atas papan catur klasik milik ryokan."
        nar "Begitu langkah sandalmu berhenti di dekat meja rendah itu, Shiori mengangkat wajah dan menatapmu dengan mata ungu amethyst serta senyum tipis yang tenang."
        if any(c["ev"] == "S01" and c["key"] == "A" for c in choices_log):
            shiori "Selamat malam, Amamiya-san. Kebetulan sekali—kali ini juga mau duduk di seberangku?"
        else:
            shiori "Selamat malam, Amamiya-san. Kebetulan papan catur di lobi ini sedang kosong. Kamu mau bermain satu babak?"
        nar "Ia meraih gelas teh hangat miliknya dan memindahkannya ke meja samping yang cukup jauh dari papan agar tidak tersenggol, lalu menautkan jari-jarinya dengan rapi di pangkuan."
        shiori "Lobi malam ini jauh lebih sunyi daripada taman waktu Hanami. Kamu mau permainan singkat sekadar mengisi waktu sebelum tidur, atau membiarkannya berlangsung penuh sampai selesai?"
        nar "Sorot matanya yang tenang terasa berbeda dari sekadar ajakan sopan—malam ini ia jelas punya cukup waktu luang untuk benar-benar ingin melihat bagaimana caramu berpikir."
    else:
        nar "Malam hari di lobi penginapan ryokan terasa jauh lebih tenang daripada ruang makan yang tadi ramai. Cahaya hangat lentera kertas memantul di atas lantai kayu gelap, sementara denting pancuran bambu dari taman luar terdengar samar di balik pintu kaca."
        nar "Di sudut ruang tunggu dekat jendela, Saionji Shiori duduk anggun mengenakan yukata penginapan biru tua bermotif bunga halus, rambut putih keperakannya jatuh bergelombang melewati bahu saat ia menata bidak-bidak kayu di atas papan catur klasik milik ryokan."
        nar "Ketika langkahmu berhenti di dekat meja rendah itu, Shiori mengangkat pandangan dengan mata ungu amethyst dan senyum tipis yang tenang."
        if any(c["ev"] == "S01" and c["key"] == "A" for c in choices_log):
            shiori "Selamat malam, Kisaragi-san. Kebetulan sekali—kali ini juga mau duduk di seberangku?"
        else:
            shiori "Selamat malam, Kisaragi-san. Papannya kebetulan sedang kosong. Kamu mau bermain satu babak?"
        nar "Ia memindahkan gelas teh hangatnya ke meja samping yang jauh dari papan agar tidak tersenggol, lalu menautkan jari-jarinya dengan rapi."
        shiori "Lobi ryokan jauh lebih sunyi daripada taman waktu Hanami. Kamu mau pertandingan singkat sekadar mengisi waktu, atau membiarkannya berlangsung sampai selesai?"
        nar "Malam ini ia jelas tidak sedang terburu-buru—sorot matanya menunjukkan rasa ingin tahu yang sungguh-sungguh terhadap caramu berpikir."
    call kk_family_menu("S02", ["\"Ayo main penuh saja sampai selesai.\"", "Bermain santai dan biarkan dia mengambil bidak pentingmu.", "Fokus penuh dan incar celah untuk menang."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau duduk bersila di bantal duduk seberang meja rendah, lalu menatap barisan bidak putih di hadapanmu dengan tatapan mantap."
            chiasa "Ayo main penuh saja, Saionji-senpai. Tanggung kalau cuma setengah jalan."
            shiori "Bagus. Jawaban seperti itu yang paling kusuka—aku ingin melihat langkahmu sendiri tanpa dipotong waktu."
            nar "Permainan dimulai dengan tempo yang pelan namun rapat. Setiap kali kau menggerakkan satu bidak, Shiori tidak pernah membalas secara asal; ia membaca arah tekananmu, menutup jalur tengah, lalu melempar jebakan kecil di sayap kanan yang memaksamu berpikir dua langkah lebih jauh."
            nar "Di pertengahan babak, kau mengambil satu keputusan berisiko dengan menukar kuda milikmu demi membuka garis serangan menteri. Alis perak Shiori terangkat tipis—pertandingan berlanjut sengit hingga akhirnya berakhir setelah lebih dari empat puluh langkah."
            nar "Begitu raja tumbang dan permainan selesai, Shiori tidak langsung merapikan papan. Ia menunjuk satu petak di tengah yang tadi sempat kaulepas."
            shiori "Amamiya-san, tadi di giliran kedua belas—mengapa kamu memilih mengorbankan kuda di petak ini padahal pertahanan kirimu masih bisa ditutup pion?"
            chiasa "Soalnya kalau kututup pakai pion, pergerakanku langsung terkunci sampai akhir. Lebih baik kupaksa papan terbuka sekalian meskipun berisiko."
            nar "Shiori menatap petak itu selama beberapa detik, lalu tersenyum pelan dengan binar puas yang jujur di matanya."
            shiori "...Menarik sekali. Aku tadi mengira sudah cukup memahami pola bermainmu, ternyata kamu lebih memilih ruang bergerak daripada keamanan semu. Jawabanmu barusan mengubah caraku membaca lawan malam ini."
            nar "Ia mengangkat gelas tehnya dan menyesap pelan, jelas menghargai keseriusanmu sepanjang babak."
        else:
            nar "Kau duduk bersila di bantal duduk seberang meja rendah, membetulkan letak lengan yukata gelapmu, lalu menatap barisan bidak putih di hadapanmu dengan santai namun fokus."
            yutaka "Main penuh saja sampai selesai, Saionji-san. Percuma main kalau dipotong di tengah jalan."
            shiori "Bagus. Jawaban seperti itu yang paling kusuka—aku ingin melihat langkahmu sendiri tanpa tergesa."
            nar "Permainan berjalan ketat sejak pembukaan. Setiap kali kau mendorong satu bidak, Shiori tidak pernah membalas secara mekanis; ia membaca arah tekananmu, menutup jalur tengah, lalu memasang jebakan halus di sayap kanan yang memaksamu mengubah rencana di tempat."
            nar "Di pertengahan babak, kau mengambil langkah berisiko dengan menukar perwira kuda milikmu demi memaksa jalur tengah terbuka. Alis perak Shiori terangkat tipis—pertandingan berlanjut sengit hingga akhirnya berakhir setelah lebih dari empat puluh langkah yang menguras perhatian."
            nar "Begitu raja tumbang, Shiori tidak langsung merapikan papan. Ia mengetuk ringan satu petak di tengah papan dengan ujung jarinya."
            shiori "Kisaragi-san, pada giliran tengah tadi—mengapa kamu memilih membuka jalur di sini padahal pertahanan rajamu sendiri sedang tipis?"
            yutaka "Soalnya kalau terus bertahan menunggu, pelan-pelan aku pasti kehabisan ruang gerak dan cuma menunda kekalahan. Lebih baik memaksa papan jadi berantakan sekalian biar peluangnya terbuka lagi."
            nar "Shiori menatap petak itu selama beberapa detik, lalu tersenyum pelan dengan binar puas yang jujur di mata ungunya."
            shiori "...Menarik sekali. Aku tadi mengira sudah cukup memahami gaya bermainmu, rupanya kamu lebih suka mengganggu ritme lawan daripada bersembunyi di balik pertahanan aman. Jawabanmu barusan mengubah caraku membaca lawan malam ini."
            nar "Ia mengangkat gelas tehnya dan menyesap pelan, jelas menghargai keseriusanmu sepanjang babak."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kau duduk di seberangnya dan memulai permainan, tetapi di pertengahan babak kau memilih tidak mempersulit suasana. Ketika menterimu sebenarnya bisa ditarik mundur ke petak aman, kau justru menggerakkan pion pinggir yang tidak penting dan membiarkan bidak berharga itu terbuka lebar di jalur serangannya."
            nar "Tangan Shiori sempat terangkat di atas papan—lalu berhenti mendadak di udara. Ia tidak mengambil menterimu."
            nar "Ia menarik tangannya kembali ke pangkuan, lalu menatapmu lurus-lurus dengan mata ungu amethyst yang mendadak kehilangan kehangatan sopannya."
            shiori "Amamiya-san. Kamu melihat jalur aman di petak sebelah kiri tadi, bukan? Jangan mengalah padaku."
            nar "Suaranya tetap rendah dan halus, namun ketajamannya langsung membuat suhu di lobi terasa turun beberapa derajat."
            chiasa "Ah... aku cuma pikir ini kan malam liburan, jadi tidak perlu dibuat terlalu tegang—"
            shiori "Apakah aku pernah mengatakan bahwa aku tidak sanggup kalah, atau bahwa aku membutuhkan kemenangan yang dibungkus rasa kasihan?"
            nar "Shiori mengembalikan satu bidaknya sendiri ke kotak kayu dengan bunyi pelan yang terasa jauh lebih dingin daripada kemarahan yang meledak-ledak."
            shiori "Kalau kamu tidak ingin bermain sungguhan, menolak sejak awal jauh lebih sopan daripada berpura-pura kalah demi menyenangkanku. Keramahan yang mengabaikan keinginan lawan bicara hanya terasa meremehkan."
            chiasa "...Maaf, Saionji-senpai. Itu memang salahku."
            nar "Ia mengangguk singkat dengan senyum tipis yang kini sepenuhnya tertutup seperti dinding kaca, lalu menutup papan catur itu sebelum permainan selesai."
        else:
            nar "Kau duduk di seberangnya dan memulai permainan, tetapi di pertengahan babak kau memilih mengendurkan tekanan. Ketika bidak pentingmu sebenarnya jelas-jelas bisa ditarik ke petak aman, kau justru menggerakkan pion pinggir dan membiarkan bidak itu terbuka di depan jalurnya."
            nar "Tangan Shiori terangkat di atas papan—lalu berhenti mendadak. Ia tidak mengambil bidakmu."
            nar "Ia menarik tangannya kembali ke pangkuan dan menatapmu lurus dengan mata ungu amethyst yang mendadak dingin."
            shiori "Kisaragi-san. Kamu melihat jalur aman di sebelah kiri tadi. Jangan mengalah padaku."
            yutaka "Ah... kupikir ini malam liburan, jadi nggak perlu dibuat terlalu tegang—"
            shiori "Apakah aku pernah mengatakan bahwa aku tidak sanggup kalah, atau butuh kemenangan yang sengaja disodorkan?"
            nar "Shiori mengembalikan satu bidaknya sendiri ke kotak kayu dengan bunyi pelan yang terasa jauh lebih dingin daripada kemarahan yang meledak-ledak."
            shiori "Kalau kamu tidak ingin bermain sungguhan, menolak sejak awal jauh lebih terhormat daripada mengalah demi menyenangkanku."
            yutaka "...Maaf, Saionji-san. Salahku."
            nar "Ia mengangguk singkat dengan senyum sopan yang kini terasa seperti tembok kaca, lalu menutup papan catur itu sebelum babak selesai."
    else:
        if kk_host == "chiasa":
            nar "Kau duduk di seberang meja rendah dan langsung memusatkan seluruh perhatianmu pada papan kayu. Tidak ada alasan untuk menahan diri; jika ia memang ingin melihat cara pikirmu, kau akan memberinya pertandingan yang paling tajam yang sanggup kauberikan."
            nar "Sepanjang dua puluh menit penuh, hanya bunyi 'klak' bidak kayu dan detak samar pancuran bambu di luar yang terdengar di lobi. Shiori membangun tekanan sistematis di sisi kanan, memaksamu bertahan rapat—sampai kau melihat satu celah kecil yang ia tinggalkan di baris belakang demi mempercepat serangannya."
            nar "Kau mendorong bentengmu menembus garis belakang, mengunci posisi rajanya dalam dua langkah tak terelakkan."
            chiasa "Skakmat, Saionji-senpai."
            nar "Shiori menatap papan selama tiga detik penuh. Tidak ada raut kesal, tidak ada alasan, dan tidak ada senyum palsu. Bibirnya justru melengkung naik menjadi senyum percaya diri yang tajam dan sangat hidup."
            shiori "Luar biasa. Kamu melihat celah di baris belakangku satu giliran lebih cepat daripada perkiraanku."
            nar "Tanpa sedikit pun ragu, kedua tangannya langsung bergerak cekatan mengumpulkan seluruh bidak dan menyusunnya kembali ke garis awal sebelum teh di gelas kalian sempat dingin."
            shiori "Aku mengaku kalah untuk babak ini, Amamiya-san. Bagaimana—mau satu babak lagi? Kali ini aku tidak akan membiarkan baris belakangku terbuka semudah itu."
            chiasa "Boleh saja, Senpai. Aku masih belum mengantuk."
            nar "Di lobi yang tenang itu, pujian paling tulus yang bisa keluar dari seorang Saionji Shiori malam ini hadir dalam bentuk bidak-bidak kayu yang langsung ia susun ulang untuk menantangmu lagi."
        else:
            nar "Kau duduk di seberang meja rendah dan memusatkan seluruh perhatianmu pada papan. Tidak ada alasan menahan diri; kalau ia memang ingin menguji cara pikirmu, kau akan membawanya sampai garis akhir."
            nar "Selama dua puluh menit penuh, hanya bunyi 'klak' bidak kayu dan denting pancuran bambu di luar yang terdengar di lobi. Shiori menekan dengan sistematis dari sayap kanan, memaksamu merapatkan pertahanan—hingga kau menangkap satu celah kecil yang ia tinggalkan di baris belakang demi mempercepat serangannya."
            nar "Kau langsung mendorong bentengmu menembus garis belakang dan mengunci rajanya dalam dua langkah."
            yutaka "Skakmat, Saionji-san."
            nar "Shiori menatap papan selama tiga detik penuh tanpa raut kesal ataupun alasan. Sebaliknya, senyum percaya diri yang tajam dan sangat hidup langsung muncul di bibirnya."
            shiori "Kau melihat celahnya satu giliran lebih cepat daripada hitunganku, Kisaragi-san."
            nar "Tanpa menunggu teh di gelas kalian dingin, kedua tangannya langsung bergerak cekatan menyusun ulang seluruh bidak ke garis awal."
            shiori "Aku mengaku kalah untuk babak ini. Bagaimana—satu lagi? Kali ini aku tidak akan membiarkan baris belakangku terbuka semudah itu."
            yutaka "Ayo saja, mumpung belum mengantuk."
            nar "Pujian paling tulus dari Saionji Shiori malam itu hadir dalam bentuk bidak-bidak kayu yang langsung ia susun kembali untuk menantangmu lagi."
    return

# ┌─ PANDUAN CERITA · Mi02 · Kue Percobaan Ketiga
# │ LOKASI  : Dapur ryokan
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : dapur ryokan; kue gagal.
# │ INTI    : A makan semuanya / B jujur / C bantu memperbaiki.
# │ AKHIRAN : C memicu sisi manja.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi02:
    call kk_scene_enter("miyuki", "Dapur ryokan")
    if kk_host == "chiasa":
        nar "Saat kau berjalan melewati lorong belakang ryokan untuk mengambil air minum malam, aroma manis mentega hangat dan vanila yang sedikit gosong tercium dari balik pintu dapur yang terbuka setengah."
        nar "Begitu melongok masuk, kau mendapati Tachibana Miyuki berdiri di depan meja saji mengenakan celemek putih di atas yukata tidurnya yang lengannya sudah diikat tali kain agar tidak kotor. Rambut hitam panjangnya diikat longgar ke belakang, dan di atas meja berjajar dua loyang kue hasil percobaan sebelumnya bersama mangkuk tepung."
        nar "Baru saja Miyuki membalik cetakan kue percobaan ketiga ke atas rak pendingin—dan tepat di depan mata kalian berdua, bagian tengah kue spons itu perlahan melesak turun membentuk cekungan yang agak menyedihkan."
        nar "Miyuki menatap kue itu dengan wajah serius yang begitu kontras, persis seperti seorang dokter yang baru saja melihat hasil percobaannya membantah seluruh teori terbaiknya."
        miyuki "Baiklah... bentuk memang bukan segalanya. Tapi kalau rasanya ikut melesak seperti bagian tengahnya, sepertinya Senpai perlu bicara serius dengan resep ini."
        nar "Ketika ia menoleh dan menyadari sosokmu berdiri di ambang pintu dapur, rona malu tipis langsung menyapu pipinya."
        miyuki "Ara, Chiasa-chan? Belum tidur ya? Maaf dapurnya jadi bau manis begini—tadi pengelola ryokan mengizinkan Senpai meminjam oven sebentar buat coba resep kue untuk sarapan besok, tapi... ya, hasilnya seperti yang kamu lihat."
        nar "Ia memotong sepotong kecil kue yang bentuknya miring itu, meletakkannya di piring keramik kecil bersama garpu, lalu menyodorkannya kepadamu dengan ekspresi sudah siap meminta maaf bahkan sebelum kau sempat mencicipinya."
        miyuki "Kalau Chiasa-chan tidak keberatan jadi juri dadakan... boleh bantu cicipi sedikit? Kalau tidak enak, langsung taruh saja ya."
    else:
        nar "Saat kau menyusuri lorong belakang ryokan malam-malam mencari mesin minuman dingin, aroma manis mentega hangat dan vanila yang agak gosong tercium dari balik pintu dapur yang terbuka setengah."
        nar "Begitu melongok masuk, kau mendapati Tachibana Miyuki berdiri di depan meja saji mengenakan celemek putih di atas yukata tidurnya, dengan rambut hitam panjang yang diikat longgar ke belakang. Di atas meja berjajar dua loyang hasil percobaan sebelumnya bersama mangkuk tepung."
        nar "Tepat di depan matamu, kue spons percobaan ketiganya baru saja keluar dari cetakan—dan perlahan bagian tengahnya melesak turun membentuk cekungan menyedihkan. Miyuki menatap kue itu dengan wajah serius yang begitu kontras, seolah sedang memeriksa pasien yang menolak seluruh teori terbaiknya."
        miyuki "Baiklah... bentuk memang bukan segalanya. Tapi kalau rasanya ikut melesak seperti ini, Senpai harus bicara serius dengan resepnya."
        nar "Ketika ia menoleh dan menyadari sosokmu berdiri di ambang pintu, rona malu tipis langsung naik ke pipinya."
        miyuki "Ara, Yutaka-kun? Belum tidur? Maaf dapurnya jadi bau manis begini—tadi pengelola mengizinkan Senpai meminjam oven sebentar buat coba resep kue sarapan besok, tapi hasilnya..."
        nar "Ia memotong sepotong kecil kue yang miring itu, menaruhnya di piring keramik kecil bersama garpu, lalu menyodorkannya kepadamu dengan ekspresi sudah siap meminta maaf bahkan sebelum kau sempat mencicipinya."
        miyuki "Kalau Yutaka-kun mau jadi juri dadakan... boleh cicipi sedikit? Kalau nggak enak, langsung taruh saja ya."
    call kk_family_menu("Mi02", ["Habiskan seluruh potongan kue yang ia sajikan.", "\"Bagian tengahnya agak padat, tapi pinggirnya enak kok.\"", "Gulung lengan bajumu dan tawarkan bantuan memperbaiki adonannya."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau menerima piring kecil itu, memotong satu gigitan dengan garpu, lalu mengunyahnya. Memang bagian tengahnya agak bantat dan terlalu padat, tetapi aroma mentega serta rasa manisnya sebenarnya masih sangat layak dimakan."
            nar "Tanpa banyak komentar, kau terus menyendok potongan kedua, ketiga, hingga piring kecil itu bersih tidak tersisa sedikit pun."
            chiasa "Habis. Rasanya tetap enak kok, Tachibana-senpai—manisnya pas buat camilan malam."
            nar "Miyuki mengerjap tak percaya melihat piring kosong di tanganmu, lalu tawa kaget yang lembut pecah dari bibirnya. Sebelum kau sempat melirik potongan berikutnya di rak pendingin, ia buru-buru mengambil garpu dari tanganmu sambil menggeleng geli."
            miyuki "Ara, tunggu dulu, Chiasa-chan! Satu gigitan buat penilaian itu sudah cukup—kamu tidak perlu memaksa menghabiskan semuanya cuma buat menghibur Senpai, nanti malah kekenyangan sebelum tidur."
            chiasa "Aku memang tidak memaksa, beneran enak."
            miyuki "Hehe... terima kasih banyak ya. Setidaknya sekarang Senpai tahu kegagalan percobaan ketiga ini masih punya satu penggemar setia."
            nar "Ia mengambil garpu bersih, mencicipi sedikit bagian tengah kuenya sendiri, lalu akhirnya ikut menertawakan bentuk cekung yang tadi membuatnya murung di depan oven."
        else:
            nar "Kau menerima piring kecil itu, memotong satu gigitan besar dengan garpu, lalu mengunyahnya. Memang bagian tengahnya agak padat dan bantat karena turun, tetapi aroma mentega hangat serta rasa manisnya masih sangat layak dimakan—bahkan pas untuk camilan tengah malam."
            nar "Tanpa banyak komentar, kau terus menyendok potongan kedua, ketiga, hingga piring keramik kecil itu bersih tidak tersisa sepotong pun."
            yutaka "Habis. Rasanya tetap enak kok, Tachibana-senpai—manisnya pas banget buat teman minum teh malam-malam begini."
            nar "Miyuki mengerjap tak percaya melihat piring kosong di tanganmu, lalu tawa kaget yang lembut pecah dari bibirnya. Sebelum kau sempat melirik potongan berikutnya di rak pendingin, ia cepat-cepat mengambil garpu dari tanganmu sambil menggeleng geli."
            miyuki "Ara, tunggu dulu, Yutaka-kun! Satu gigitan buat penilaian itu sudah cukup—kamu tidak perlu memaksa menghabiskan semuanya cuma buat menghibur Senpai, nanti malah kekenyangan sebelum tidur."
            yutaka "Nggak memaksa kok, beneran enak."
            miyuki "Hehe... terima kasih banyak ya. Setidaknya sekarang Senpai tahu kegagalan percobaan ketiga ini masih punya satu penggemar setia."
            nar "Ia mengambil garpu bersih, mencicipi sedikit bagian tengah kuenya sendiri, lalu akhirnya ikut menertawakan bentuk cekung yang tadi membuatnya murung di depan oven."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kau mencicipi satu gigitan dari bagian pinggir lalu satu gigitan kecil dari bagian tengah yang cekung, mengunyah pelan sebelum menjawab dengan jujur."
            chiasa "Kalau boleh jujur, Tachibana-senpai—bagian pinggirnya lembut dan wangi menteganya enak sekali. Tapi bagian tengah yang turun ini memang agak terlalu padat, kayak kurang mengembang waktu di oven."
            nar "Miyuki tidak tampak tersinggung sedikit pun. Ia mengambil garpu bersih, memotong sedikit dari bagian pinggir dan bagian tengah yang baru kau tunjuk, lalu mencicipinya sambil mengangguk pelan tanpa senyum yang dipaksakan."
            miyuki "Hmm... benar juga. Persis seperti yang kurasakan tadi. Suhu oven ryokan ini sepertinya agak terlalu panas di awal, jadi luarnya matang duluan sementara tengahnya belum sempat naik."
            nar "Ia menghela napas lega sambil menatapmu dengan sorot mata biru sapphire yang hangat."
            miyuki "Terima kasih sudah jujur, Chiasa-chan. Lega rasanya kalau kamu nggak merasa harus bilang 'sempurna' cuma karena Senpai yang membuatnya."
            nar "Ia meraih pulpen dan buku resep kecilnya di sudut meja, menuliskan catatan penyesuaian suhu dan waktu panggang di pinggir halaman—kali ini tanpa mencoret seluruh percobaannya sebagai kegagalan total."
        else:
            nar "Kau mencicipi satu gigitan dari bagian pinggir lalu satu gigitan kecil dari bagian tengah yang cekung, mengunyah pelan sebelum memberikan jawaban apa adanya."
            yutaka "Kalau mau jawaban jujur, Tachibana-senpai—bagian pinggirnya lembut dan wangi menteganya enak sekali. Tapi bagian tengahnya memang terlalu padat, kayak suhu oven di sini kepanasan di awal jadi bagian luarnya keburu matang sebelum tengahnya sempat naik."
            nar "Miyuki sama sekali tidak tampak tersinggung. Ia mengambil garpu bersih, memotong tepat di bagian pinggir dan bagian tengah yang baru kau tunjuk, lalu mencicipinya sambil mengangguk pelan tanpa senyum yang dipaksakan."
            miyuki "Hmm... benar juga. Persis seperti yang kurasakan tadi. Suhu oven ryokan ini memang jauh lebih panas daripada oven di apartemenku."
            nar "Ia menghela napas lega sambil menatapmu dengan sorot mata biru sapphire yang hangat."
            miyuki "Terima kasih sudah jujur, Yutaka-kun. Lega rasanya kalau kamu nggak merasa harus bilang 'sempurna' cuma karena Senpai yang membuatnya."
            nar "Ia meraih pulpen dan buku resep kecilnya di sudut meja, lalu menuliskan catatan penyesuaian suhu dan waktu panggang di tepi halaman—kali ini tanpa mencoret seluruh percobaannya sebagai kegagalan total."
    else:
        if kk_host == "chiasa":
            nar "Kau meletakkan piring kecil itu setelah satu gigitan, lalu langsung mengikat ujung lengan yukata-mu ke belakang dan melangkah masuk ke sisi meja saji."
            chiasa "Kalau masih ada bahan buat percobaan keempat, bagi tugas saja yuk, Tachibana-senpai. Biar aku yang bantu mengocok adonan atau menakar tepungnya."
            nar "Mata Miyuki membulat pelan melihat kesigapanmu. Untuk beberapa detik ia hanya menatapmu, lalu bahunya turun lega dan ia menggeser posisinya di depan meja agar kalian berdua punya ruang yang sama lapangnya."
            miyuki "Ara... kamu serius mau menemani Senpai begadang sedikit di dapur? Baiklah—kalau begitu Chiasa-chan pegang mangkuk yang ini, ya."
            nar "Ia menyodorkan mangkuk kaca dan pengocok telur kepadamu sambil tersenyum jahil yang jarang sekali terlihat di kampus."
            miyuki "Lagipula, kalau percobaan keempat ini ternyata gagal lagi, kali ini kita bisa menyalahkan kerja sama tim. Senpai suka rencana ini."
            chiasa "Jangan langsung pesimis dulu, Senpai. Telurnya dikocok sampai kaku, kan?"
            miyuki "Iyaa~ pelan-pelan saja, jangan sampai pegal. Kalau Chiasa-chan capek, nanti gantian sama Senpai, oke?"
            nar "Nada suaranya mendadak melunak jadi jauh lebih manja dan santai—sisi hangat yang tidak pernah keluar ketika semua orang di kampus hanya datang mengandalkannya. Percobaan keempat mungkin belum tentu langsung sempurna, tetapi malam ini ia tidak lagi berdiri sendirian di depan oven."
        else:
            nar "Kau meletakkan piring kecil itu setelah satu gigitan, lalu langsung menggulung lengan yukata-mu ke atas siku dan melangkah masuk ke samping meja saji."
            yutaka "Kalau bahannya masih ada buat percobaan keempat, bagi tugas saja, Tachibana-senpai. Urusan mengocok adonan yang bikin pegal biar aku yang pegang."
            nar "Mata biru sapphire Miyuki membulat pelan melihatmu langsung bergerak. Bahunya turun lega, lalu ia menggeser posisinya agar kalian sama-sama punya ruang di depan meja."
            miyuki "Ara... Yutaka-kun mau menemani Senpai begadang di dapur? Baiklah, mangkuk dan pengocoknya buat kamu ya."
            nar "Ia menyodorkan mangkuk kaca kepadamu sambil tersenyum jahil yang jarang sekali terlihat di kampus."
            miyuki "Lagipula kalau kali ini gagal lagi, kita bisa menyalahkan kerja sama tim. Senpai suka rencana ini."
            yutaka "Jangan langsung mikir gagal dulu, Senpai. Dikocok sampai kaku, kan?"
            miyuki "Iyaa~ pelan-pelan saja, nanti tangannya pegal lho. Kalau capek bilang ya, biar Senpai gantian~"
            nar "Suaranya melunak jadi jauh lebih santai dan manja—sisi hangat yang tidak pernah muncul saat semua orang hanya datang mengandalkannya. Percobaan keempat belum tentu langsung sempurna, tetapi malam ini ia tidak lagi berdiri sendirian di depan oven."
    return

# ┌─ PANDUAN CERITA · N02 · Rematch Malam Onsen
# │ LOKASI  : Ruang bersama ryokan
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : ia selalu meminta rematch.
# │ INTI    : A terus menang / B mengalah / C ajak tim.
# │ AKHIRAN : Trust.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N02:
    call kk_scene_enter("nagisa", "Ruang bersama ryokan · Malam")
    if kk_host == "chiasa":
        nar "Lewat pukul sepuluh malam, ruang bersama ryokan yang berkarpet tatami mulai sepi karena sebagian besar rombongan sudah kembali ke kamar masing-masing setelah berendam di onsen. Hanya cahaya layar televisi di sudut ruangan yang masih menyala terang."
        nar "Di depan layar itu, Sakurajima Nagisa duduk bersila mengenakan yukata penginapan, rambut pirang keemasannya yang biasanya diikat twin-tail kini masih agak lembap sehabis mandi dan diikat longgar di kiri-kanan. Dua stik pengendali konsol portabel yang disambungkan ke televisi tergeletak di antara kalian—dan di layar baru saja muncul tulisan 'GAME OVER' untuk kesekian kalinya."
        nar "Nagisa mengerutkan kening menatap layar sambil menekan tombol ulang dengan suara cepat, lalu mengoceh panjang lebar membedah kekalahannya sendiri memakai istilah frame, jeda serangan, dan arah menghindar."
        nagisa "Tunggu, tunggu! Barusan itu aku sudah pencet tangkis duluan, tapi jeda animasi seranganku belum selesai sepersekian detik! Jadi secara teknis aku nggak salah baca—cuma telat mencet tombolnya saja!"
        nar "Ketika kau hendak menguap pelan dan melirik jam dinding, Nagisa langsung menyambar lengan bajumu pelan sambil menyodorkan kembali stik pengendali ke pangkuanmu."
        nagisa "Hei, Chiasa, jangan tidur dulu! Aku baru saja paham timing tombol yang tadi. Kalau berhenti sekarang, besok pagi tanganku pasti lupa lagi—satu ronde lagi saja, ayo!"
    else:
        nar "Lewat pukul sepuluh malam, ruang bersama ryokan yang berkarpet tatami mulai sepi karena sebagian besar rombongan sudah kembali ke kamar masing-masing setelah berendam di onsen. Hanya cahaya layar televisi di sudut ruangan yang masih menyala terang."
        nar "Di depan layar itu, Sakurajima Nagisa duduk bersila mengenakan yukata penginapan, rambut pirang keemasannya yang masih agak lembap sehabis mandi diikat longgar di kiri-kanan. Dua stik pengendali konsol portabel yang disambungkan ke televisi tergeletak di antara kalian—dan tulisan 'GAME OVER' baru saja muncul lagi untuk kesekian kalinya."
        nar "Nagisa mengerutkan kening menatap layar sambil menekan tombol ulang dengan suara cepat, lalu mengoceh panjang lebar membedah kekalahannya sendiri memakai istilah frame, jeda serangan, dan arah menghindar."
        nagisa "Tunggu, tunggu! Barusan itu aku sudah pencet tangkis duluan, tapi jeda animasi seranganku belum selesai sepersekian detik! Jadi secara teknis aku nggak salah baca—cuma telat mencet tombolnya saja!"
        nar "Ketika kau hendak menguap pelan dan melirik jam dinding, Nagisa langsung menyambar lengan yukata-mu pelan sambil menyodorkan kembali stik pengendali ke pangkuanmu."
        nagisa "Hei, Yutaka, jangan tidur dulu! Aku baru saja paham timing tombol yang tadi! Kalau berhenti sekarang, besok pagi tanganku pasti lupa lagi—satu ronde lagi saja, ayo!"
    call kk_family_menu("N02", ["Ambil stiknya dan main dengan serius.", "Perlambat permainanmu supaya dia kebagian menang.", "\"Daripada terus beradu, mau coba main satu tim saja?\""])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau menerima stik pengendali itu, duduk kembali tegak di atas bantal tatami, dan memutuskan tidak menahan satu pun gerakanmu. Jika ia memang ingin mengukur batasnya sendiri, maka kau akan melawannya dengan sungguh-sungguh."
            chiasa "Oke, satu ronde lagi, Nagisa-senpai. Tapi aku main serius seperti tadi, ya."
            nagisa "Memang harus begitu! Awas kalau kau main-main!"
            nar "Pertandingan berlangsung cepat dan sengit. Ibu jari Nagisa bergerak heboh di atas tombol sambil sesekali memekik tertahan tiap kali serangannya hampir masuk. Kali ini bar darah karaktermu benar-benar terkuras hingga tersisa tipis—sebelum kau membaca lompatan terakhirnya dan menutup ronde dengan kemenangan tipis."
            nar "Nagisa mengembuskan napas keras lalu menjatuhkan punggungnya sedikit, tetapi alih-alih marah, matanya justru langsung menatap layar tayangan ulang dengan penuh semangat."
            nagisa "Hah... kalah lagi! Tapi jangan senyum dulu, Chiasa! Lihat bar darahmu barusan—aku makin dekat! Dan yang bikin aku kena tadi bukan kesalahan yang sama kayak ronde sebelumnya, kan?!"
            chiasa "Iya, tangkisanmu di tengah ronde tadi jauh lebih cepat daripada sebelumnya."
            nagisa "Tuh kan! Sebentar, minum dulu sana kalau tanganmu pegal—habis ini ronde penentuan!"
            nar "Ia menyodorkan botol minuman dingin di dekat meja kepadamu sambil menunggu dengan tidak sabar. Nada tantangannya masih sama kerasnya, tetapi sorot matanya kini jauh lebih lepas—ia tahu kau menghadapinya sebagai lawan sungguhan."
        else:
            nar "Kau mengambil stik pengendali itu, duduk kembali tegak di bantal tatami, dan memutuskan bermain sepenuh kemampuanmu tanpa menahan satu gerakan pun."
            yutaka "Oke, satu ronde lagi. Tapi aku nggak bakal nahan diri ya, Nagisa."
            nagisa "Memang itu yang kumau! Awas kalau kau main setengah hati!"
            nar "Pertandingan berlangsung cepat dan sengit. Ibu jari Nagisa bergerak heboh di atas tombol hingga bar darah karaktermu benar-benar tersisa tipis—sebelum kau membaca lompatan terakhirnya dan menutup ronde dengan kemenangan tipis."
            nar "Nagisa mengembuskan napas keras, tetapi alih-alih marah, matanya langsung menatap layar tayangan ulang dengan penuh semangat."
            nagisa "Hah... kalah lagi! Tapi jangan senyum dulu, Yutaka! Lihat bar darahmu barusan—aku makin dekat! Dan yang bikin aku kena tadi bukan kesalahan yang sama kayak ronde sebelumnya, kan?!"
            yutaka "Iya, tangkisanmu di tengah ronde tadi jauh lebih rapat daripada sebelumnya."
            nagisa "Tuh kan! Minum dulu sana kalau tanganmu pegal—habis ini ronde penentuan!"
            nar "Ia menyodorkan botol minuman dingin kepadamu sambil menunggu tidak sabar. Tantangannya keras, tetapi kini ia benar-benar percaya kau menganggapnya lawan yang layak dihadapi sungguhan."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Melihatnya sudah kalah berkali-kali padahal matanya masih menyala penuh ambisi, kau mengambil stik dan memutuskan mengendurkan sedikit tempomu. Di detik-detik terakhir ronde, ketika karakter Nagisa terbuka lebar untuk serangan balasan yang mudah, kau sengaja menahan ibu jarimu sepersekian detik dan membiarkan serangannya masuk duluan."
            nar "Tulisan 'PLAYER 2 WINS' menyala terang di layar televisi."
            nagisa "YES! Akhirnya menang juga—!"
            nar "Nagisa langsung mengangkat kedua tangannya tinggi-tinggi dengan senyum lebar—namun gerakannya mendadak berhenti di udara. Senyumnya perlahan luruh saat ia menatap tayangan ulang di layar dan mengingat kembali detik terakhir gerakan karaktermu."
            nar "Ia menurunkan kedua tangannya perlahan, lalu menoleh menatapmu dengan mata biru yang meredup kesal."
            nagisa "...Chiasa. Tadi karaktermu jelas-jelas bisa langsung menyerang balik waktu aku melompat. Kenapa kau tiba-tiba berhenti pencet tombol?"
            chiasa "Eh... jariku tadi agak telat saja—"
            nagisa "Jangan bohong. Dari tiga ronde sebelumnya kau nggak pernah telat di gerakan semudah itu."
            nar "Kemenangan di layar televisi mendadak terasa hambar dan tidak berarti. Nagisa meletakkan stiknya ke atas meja rendah dengan bunyi agak keras, lalu membuang muka ke samping—jelas jauh lebih kesal karena mengira kau merasa perlu melindunginya dari hal sekecil kekalahan dalam permainan."
            nagisa "Sudahlah, aku capek. Aku balik ke kamar duluan."
        else:
            nar "Melihatnya sudah kalah berkali-kali sementara jam makin larut, kau mengambil stik dan sengaja mengendurkan sedikit tempomu. Di detik terakhir ronde, ketika karakter Nagisa terbuka lebar untuk serangan balasan mudah, kau menahan ibu jarimu sepersekian detik dan membiarkan serangannya masuk duluan."
            nar "Tulisan 'PLAYER 2 WINS' menyala terang di layar televisi."
            nagisa "YES! Akhirnya aku menang dari Yutaka—!"
            nar "Nagisa mengangkat kedua tangannya tinggi-tinggi dengan senyum lebar—lalu gerakannya mendadak membeku di udara. Senyumnya luruh pelan saat ia mengingat gerakan karaktermu di detik terakhir."
            nar "Ia menurunkan kedua tangannya, lalu menoleh menatapmu dengan mata biru yang meredup kesal."
            nagisa "...Yutaka. Tadi kau jelas-jelas bisa langsung membalas waktu aku melompat. Kenapa kau tiba-tiba berhenti pencet tombol?"
            yutaka "Ah... jariku agak telat saja tadi—"
            nagisa "Jangan bohong. Aku tahu betul seberapa cepat reaksimu kalau lagi main. Kau sengaja mengalah, kan?"
            nar "Kemenangan di layar mendadak terasa tidak berarti. Nagisa menaruh stiknya ke atas meja rendah dengan bunyi agak keras, lalu membuang muka—jelas lebih kesal karena mengira kau merasa perlu melindunginya dari hal sekecil kekalahan dalam permainan."
            nagisa "Sudahlah, aku capek. Aku balik ke kamar duluan."
    else:
        if kk_host == "chiasa":
            nar "Alih-alih langsung menekan tombol tanding ulang satu lawan satu, kau menggeser menu di layar televisi ke mode kerja sama dua pemain melawan musuh komputer."
            chiasa "Daripada terus saling sikut satu lawan satu, mau coba main satu tim melawan bos tahap akhir saja, Nagisa-senpai?"
            nar "Nagisa langsung menyipitkan kedua matanya ke arahmu, mencoba menakar apakah tawaranmu itu cuma alasan halus supaya kau tidak perlu melawannya lagi. Setelah dua detik menimbang, ia mendengus kecil lalu menggeser bantal duduknya merapat ke sebelahmu."
            nagisa "Boleh juga. Tapi aku pegang sisi kiri dan garis depan! Dan dengar ya, Chiasa—kalau nanti aku teriak-teriak pas main, itu artinya aku ngasih informasi, bukan lagi marah!"
            chiasa "Siap, informasi diterima."
            nar "Begitu ronde kerja sama dimulai, ruang bersama yang tadinya sunyi langsung dipenuhi suara tombol ditekan cepat dan teriakan panik Nagisa yang bercampur tawa."
            nagisa "Kanan! Awas dari kanan—eh, bagus! Tahan sebentar, aku isi tenaga dulu—waduh, kena juga!"
            nar "Meski kalian berdua tetap kalah sekali di fase terakhir bos karena salah hitung waktu menghindar, kali ini tidak ada wajah cemberut ataupun gengsi yang tegang. Nagisa langsung menekan tombol ulang sambil menoleh padamu dengan mata berbinar."
            nagisa "Tadi hampir banget! Ayo ulang sekali lagi—kali ini kita pasti menang!"
            nar "Kau mengangguk sambil ikut tertawa pelan. Untuk pertama kalinya malam ini, permintaan ulangnya tidak lagi memakai kata 'aku', melainkan 'kita'."
        else:
            nar "Alih-alih langsung menekan tombol tanding ulang satu lawan satu, kau menggeser menu di layar ke mode kerja sama dua pemain melawan bos tahap akhir."
            yutaka "Daripada terus saling sikut satu lawan satu sampai subuh, mau coba main satu tim saja, Nagisa?"
            nar "Nagisa menyipitkan mata ke arahmu, mencoba menakar apakah itu cuma alasanmu agar tidak perlu melawannya lagi. Setelah dua detik menimbang, ia mendengus kecil lalu menggeser bantal duduknya merapat ke sebelahmu."
            nagisa "Boleh juga. Tapi aku sisi kiri dan garis depan! Dan dengar ya, Yutaka—kalau nanti aku teriak-teriak pas main, itu informasi, bukan marah!"
            yutaka "Siap, bos. Informasi diterima."
            nar "Beberapa menit kemudian ruang bersama yang tadinya sunyi sudah penuh oleh suara tombol ditekan cepat dan teriakan panik Nagisa yang bercampur tawa."
            nagisa "Kanan! Awas dari kanan—nah, bagus! Tahan bentar, aku isi tenaga dulu—aduh, kena juga!"
            nar "Kalian tetap kalah sekali di fase terakhir bos karena salah hitung waktu menghindar, tetapi kali ini tidak ada wajah cemberut sedikit pun. Nagisa langsung menekan tombol ulang sambil menoleh padamu dengan mata berbinar."
            nagisa "Tadi tipis banget! Ayo ulang sekali lagi—kali ini kita pasti menang!"
            nar "Untuk pertama kalinya malam ini, permintaan ulangnya tidak lagi memakai kata 'aku', melainkan 'kita'."
    return

init 1 python:
    _hook("Mo02-A", lambda: kk_rel("moeka", "aff", 5))
    _hook("Mo02-B", lambda: kk_rel("moeka", "aff", -5))
    _hook("Mo02-C", lambda: kk_rel("moeka", "trust", 5))
    _hook("S02-A", lambda: kk_adj("respek_shiori", 5))
    _hook("S02-B", lambda: kk_adj("respek_shiori", -5))
    _hook("S02-C", lambda: kk_adj("respek_shiori", 8))
    _hook("Mi02-C", lambda: kk_adj("dimanja_miyuki", 5))
    _hook("N02-A", lambda: kk_rel("nagisa", "trust", 5))
    _hook("N02-B", lambda: kk_rel("nagisa", "trust", -5))
    _hook("N02-C", lambda: kk_rel("nagisa", "trust", 5))


# Event dinamis Nagisa, Alur_Cabang/02. Lokasi ayunan mengikuti harapan
# Nagisa pada Koita yang turun hari ini, termasuk saat pemain sedang jauh.
# ┌─ PANDUAN CERITA · N-D03 · Ayunan Malam
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Sakurajima Nagisa
# │ AWALAN  : hari itu harapan_koita turun
# │ INTI    : A Duduk di ayunan sebelah / B panggil Koita / C beri ruang
# │ AKHIRAN : kelekatan +; bila Koita yang datang, hasilnya tergantung Koita
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N_D03:
    call kk_scene_enter("nagisa", "Taman Lingkungan · Ayunan malam")
    nar "Ujung sepatu Nagisa menahan ayunan agar tidak bergerak. Ia sudah berada di sana cukup lama untuk lupa bahwa udara malam membuat tangannya dingin."
    nagisa "Kalau kamu datang untuk bilang Koita sebenarnya perhatian, jangan. Aku sedang ingin kesal tanpa dibantu membelanya. Ayunan sebelah kosong kalau mau duduk."
    call kk_family_menu("N-D03", ["Duduk di ayunan sebelah.", "Tawarkan untuk memanggil Koita.", "Beri dia ruang."])
    if _return == "A":
        nar "Kau duduk, membiarkan rantai berbunyi pelan sebelum bertanya apakah ia ingin bicara. Nagisa menatap tanah."
        nagisa "Aku cuma capek menjadi orang yang selalu tahu kenapa dia nggak bisa datang. Kadang aku ingin dia yang bertanya kenapa aku masih menunggu."
        nar "Ia mengusap mata dan menyalahkan angin. Kau tidak perlu membenarkannya agar tetap boleh berada di sana."
    elif _return == "B":
        if kk_daily_place("koita") == "Taman Lingkungan":
            koita "Nagisa? Kau mau bicara?"
            nar "Nagisa menoleh, kaget karena nama yang baru saja dikeluhkan benar-benar hadir. Ia butuh beberapa detik sebelum memutuskan apakah ingin marah atau memberi kesempatan mendengar."
            nagisa "Iya. Tapi kamu dengar sampai selesai. Jangan bilang nggak apa-apa sebelum aku bilang apa yang sakit."
        else:
            nar "Koita tidak ada di taman. Nagisa mendengarkan tawaranmu memanggilnya, lalu menggeleng tanpa menatapmu."
            nagisa "Aku nggak mau merasa dia datang karena dijemput orang lain lagi. Malam ini biarkan dulu."
    else:
        nar "Kau memberi tahu bahwa akan pergi dan membiarkan ia memilih tetap di sana. Nagisa mengangguk, mengucapkan hati-hati dengan suara kecil."
        nar "Ayunan sebelah tidak bergerak ketika kau berjalan menjauh. Jarak yang kauberikan bisa menjadi ruang untuk tenang; malam itu kau tidak tinggal cukup lama untuk tahu apakah ia berhasil menemukannya."
    return

# ┌─ PANDUAN CERITA · N-D08 · Rekaman Pertandingan
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Sakurajima Nagisa
# │ AWALAN  : N02-B pernah terjadi; gengsi ≥ 60
# │ INTI    : A Akui / B sangkal / C tantang ulang dengan serius
# │ AKHIRAN : Trust dan gengsi bergeser
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N_D08:
    call kk_scene_enter("nagisa", "Studio Arsitektur · Rekaman permainan")
    nar "Nagisa menghentikan rekaman permainan tepat sebelum gerakan terakhirmu. Ia sudah menyiapkannya, lengkap dengan bagian yang menunjukkan kesempatan yang sengaja kaulewatkan."
    nagisa "Aku putar ulang. Di sini kamu bisa menang. Aku nggak sebodoh itu sampai nggak tahu perbedaannya. Kenapa mengalah?"
    call kk_family_menu("N-D08", ["Akui kau sengaja mengalah.", "Sangkal bahwa kau sengaja kalah.", "Tantang dia lagi dan mainlah dengan serius."])
    if _return == "A":
        nar "Kau mengaku ingin membuatnya senang. Nagisa mendengar sampai selesai, lalu mematikan rekaman."
        nagisa "Aku senang main denganmu, termasuk waktu kalah. Tapi kalau kamu mengalah, aku nggak bisa percaya waktu benar-benar menang."
        nar "Ia meminta kau mengingat itu. Tegurannya tajam, tetapi sesudahnya ia masih menawarkan pertandingan lain."
    elif _return == "B":
        nar "Kau menyangkal. Nagisa memutar bagian yang sama, diam selama layar menunjukkan semua yang tidak mau kauakui."
        nagisa "Ini cuma permainan. Kalau untuk hal sekecil ini saja kamu nggak bisa jujur, aku harus menebak apa lagi?"
        nar "Ia menyimpan konsol dan tidak melanjutkan. Yang rusak sore itu bukan catatan kemenangannya."
    else:
        nar "Kau menantangnya bermain sungguhan. Nagisa menatapmu cukup lama untuk memastikan tidak ada lelucon di belakang tawaran itu."
        nagisa "Baik. Aku mungkin tetap kalah. Kamu jangan menghitung itu sebagai alasan mengasihaniku lagi."
        nar "Kalian mulai. Ketika ia kalah, ia memprotes keputusan sendiri, lalu tertawa dan meminta ulang. Kali ini hasil layar terasa bisa dipercaya."
    return

init 1 python:
    _hook("N-D03-A", lambda: kk_adj("kelekatan_nagisa",5))
    _hook("N-D08-A", lambda: (kk_rel("nagisa","trust",5), kk_adj("gengsi_nagisa",-5)))
    _hook("N-D08-B", lambda: kk_rel("nagisa","trust",-5))
    _hook("N-D08-C", lambda: kk_rel("nagisa","trust",5))
