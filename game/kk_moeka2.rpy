# Arc Moeka lanjutan (Mo13-Mo24, Mo25): topeng -> isolasi -> tanda bahaya ->
# klimaks. Mo19 (membagikan barang) dan Mo21 (tertawa keras) adalah tanda bahaya
# klasik; jendela intervensi dibuat bermakna. Mo25 TIDAK mendepiksi tindakan apa
# pun: ia bercabang pada apakah pemain mengisi jendela-jendela itu — tertolong
# tepat waktu, atau sebuah kehilangan yang disampaikan sebagai akibat, tanpa
# metode. Eksploitasi Kuga = konsekuensi saja. Penempatan Kantin Pusat prototipe.

# ┌─ PANDUAN CERITA · Mo13 · Foto yang Beredar
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : rumor Meisa tentang Moeka.
# │ INTI    : A bantu bantah / B diam / C manfaatkan.
# │ AKHIRAN : topeng tebal.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo13:
    call kk_scene_enter("moeka", "Kantin Pusat · Foto beredar")
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Lampu neon panjang menerangi Kantin Pusat yang masih ramai oleh mahasiswa selesai kelas maupun kegiatan klub. Bau kuah kari dan uap mesin teh mengisi udara di antara deretan meja panjang."
        else:
            nar "Cahaya bulan September masuk lewat deretan jendela tinggi Kantin Pusat yang dipenuhi bunyi nampan dan obrolan mahasiswa di antara jam kuliah. Aroma kuah udon dan kopi mesin memenuhi ruangan."
        nar "Kamu duduk di samping Moeka membawa nampan makanmu ketika layar ponsel di beberapa meja sekitar menampilkan unggahan yang sama. Foto sesi kerja fashion Moeka bersama fotografer Kuga Renma beredar luas di akun gosip Kouseikan Whisper disertai keterangan sinis yang tidak pernah ia tulis."
        nar "Dalam tulisan Kurosawa Meisa itu, nama Kuga dan nama studionya hanya disebut satu baris sambil lalu, sementara foto wajah Moeka dan potongan gaya pakaiannya dibahas panjang lebar dengan nada merendahkan."
        if kk_has("m17b_pulau_selesai"):
            moeka "Tautan promosi studio yang waktu di pulau kemarin dikabari Ryena ternyata beneran dicomot Meisa dan dipelintir habis-habisan di forum kampus, Chimian..."
        else:
            moeka "Aku bahkan belum sempat cek hasil edit akhirnya dari studio Kuga, tahu-tahu fotonya sudah dipotong lalu ditempel keterangan aneh-aneh di akun gosip itu..."
        nar "Moeka memutar layar ponselnya sedikit ke arahmu. Potongan foto yang beredar sengaja memotong habis detail jahitan bahu jaket buatannya sehingga yang tersisa hanya wajah dan gaya berdirinya di depan lampu studio."
        chiasa "Bagian detail pola jaketmu malah dipotong semua sama Meisa. Jelas banget dia sengaja biar kelihatan cuma foto gaya biasa."
        moeka "Padahal aku begadang tiga malam buat menyambung bordir di lengan jaket itu..."
        nar "Dua meja di belakangmu, beberapa mahasiswa saling menyenggol bahu sambil menoleh cepat ke arah rambut merah muda bergelombang dan anting hoop emas Moeka."
        chiasa "Ryena-senpai ke mana? Tumben dia nggak langsung duduk di sebelahmu."
        moeka "Lagi antre beli teh dingin buatku biar kepalaku agak adem... soalnya dari tadi tanganku rasanya dingin banget lihat kolom komentarnya."
        nar "Belum sempat Moeka meneguk air putihnya, dua mahasiswi yang membawa nampan melambat tepat di ujung meja kalian. Salah satunya tersenyum terlalu lebar sambil memiringkan layar ponselnya ke arah Moeka."
        "Mahasiswi Kantin" "Eh, Kohinata-san, fotomu yang diunggah bareng fotografer luar kampus itu keren banget lho. Beneran sekali sesi begitu bayarannya bisa nutup dua bulan kerja konbini? Enak ya tinggal bergaya depan kamera."
        "Teman Kantin" "Iya, kalau kerja sambilan segampang itu, pantes gaya bajumu selalu kelihatan baru terus."
        nar "Nada pertanyaan itu terdengar begitu manis sampai seluruh meja sebelah langsung menoleh menahan tawa. Jemari Moeka mencengkeram pinggiran nampan plastiknya hingga ujung jarinya memucat. Untuk satu detik yang jarang terlihat, senyum ceria di wajahnya jatuh sepenuhnya."
        moeka "Itu kerjaan pemotretan dan desain beneran! Kalian lihat jaket dan potongan kain yang kupakai di foto itu juga, kan? Itu hasil jahitanku sendiri buat portofolio! Jangan disamakan dengan cerita murahan yang kalian karang sendiri di kolom komentar!"
        "Mahasiswi Kantin" "Wah, jangan marah dulu dong, Kohinata-san. Kami kan cuma nanya karena di unggahannya memang nggak ditulis soal tugas kuliah."
        nar "Mata biru cerah Moeka berkilat tegang menahan emosi di bawah sorotan mata seisi kantin, sementara Ryena masih mengantre jauh di konter minuman. Ia melirik sekilas ke arahmu yang duduk persis di sebelahnya."
        call kk_family_menu("Mo13", ["\"Hentikan omongan ngawur itu. Jaket di foto itu buatan Moemoe-senpai sendiri di studio kami.\"", "Tetap diam dan biarkan Moeka menyelesaikannya sendiri.", "Tawarkan pembelaan dengan syarat Moeka mengikuti keinginanmu ke depan."])
        if _return == "A":
            nar "Kamu meletakkan sumpitmu pelan dan berdiri tepat di sisi Moeka, menatap kedua mahasiswi itu lurus tanpa sedikit pun rasa sungkan."
            chiasa "Hentikan omongan ngawur itu. Jaket tambal kain di foto itu polanya dikerjakan Moemoe-senpai tiga minggu di studio jahit lantai dua Fakultas Seni. Aku lihat sendiri potongan kainnya dari hari pertama."
            "Mahasiswi Kantin" "Eh, kamu adik tingkatnya ya? Kami kan cuma mengulang pertanyaan yang ramai di komentar..."
            chiasa "Komentar anonim yang bahkan nggak tahu beda katalog portofolio fashion sama gosip murahan? Kalau kalian nggak paham kerjaan desain dan pemotretan profesional, lebih baik nggak usah sok menilai bayaran orang lain di tengah kantin."
            nar "Kamu sengaja tidak memaksa Moeka membuka rincian kontrak, nominal upah, ataupun urusan keluarganya di depan umum hanya untuk dianggap pantas dibela. Dua mahasiswi itu langsung bertukar pandang kaku."
            "Teman Kantin" "Sudah, ayo cari meja belakang saja, nggak usah diperpanjang."
            nar "Begitu keduanya bergegas menjauh dan meja sebelah kembali menunduk ke piring masing-masing, Ryena tiba di meja sambil membawa dua gelas teh dingin dan menatap punggung kedua mahasiswi itu dengan kening berkerut."
            "Ryena" "Lho, ada apa tadi? Kok muka dua anak itu langsung merah banget waktu berpapasan denganku?"
            moeka "Tadi mereka nyindir soal foto studio Kuga di depan meja, terus Chimian langsung maju membantah mereka di depan satu kantin..."
            "Ryena" "Syukurlah kamu ada di sini, Chiasa. Aku tadi sudah hampir lari bawa dua gelas ini."
            nar "Kamu duduk kembali di kursimu. Moeka menatapmu diam selama dua detik penuh tanpa menyalakan tawa cerianya."
            moeka "Chimian... kamu barusan membantah mereka di depan satu kantin begitu?"
            chiasa "Habisnya tuduhan mereka jelas-jelas ngawur, Moemoe-senpai. Masa kerja kerasmu di studio jahit dicap seenaknya begitu."
            nar "Tangan Moeka di pinggiran nampan perlahan mengendur. Senyum yang muncul di bibirnya kali ini jauh lebih kecil dan tidak terdengar dipaksakan."
            moeka "...Nggak banyak orang yang mau ambil risiko ikut disorot orang satu kantin cuma buat membelaku, Chimian. Biasanya orang cuma bilang sudahlah, biarin aja, nanti juga lupa sendiri."
            chiasa "Kalau dibiarkan terus nanti mereka mengira boleh bicara seenaknya lagi. Ayo makan dulu selagi udonnya masih hangat, nanti habis ini kita minta studio Kuga mencantumkan kredit desainer di unggahan aslinya."
            "Ryena" "Setuju banget! Sepulang dari sini aku ikut bantu kirim pesan ke pihak studio Kuga supaya nama desainer bajunya dipasang terang-terangan di keterangan foto."
            moeka "Iya... terima kasih banyak ya, Chimian, Ryena. Sungguh."
            nar "Ia mulai menyuap makanannya dengan bahu yang akhirnya turun, berhenti berpura-pura bahwa sindiran barusan hanya lelucon ringan."
        elif _return == "B":
            nar "Kamu tetap duduk menunduk memandangi gelas minumanmu, tidak mengangkat wajah maupun memotong pertanyaan kedua mahasiswi itu. Hening canggung menggantung di atas meja selama tiga detik yang terasa sangat panjang."
            nar "Moeka sempat menoleh singkat kepadamu, lalu begitu menyadari tidak ada kalimat pembelaan yang datang dari sebelahnya, ia menarik napas cepat dan segera menaikkan sudut bibirnya tinggi-tinggi."
            moeka "Haha, astaga, muka kalian serius banget sih! Kalau beneran sekali foto bisa langsung kaya raya, aku sudah beli mesin jahit baru tiga biji dari kemarin kali!"
            "Mahasiswi Kantin" "Oh... jadi cuma proyek kecil ya?"
            moeka "Iya dong, namanya juga anak desain cari pengalaman sekalian nambah uang jajan! Tenang aja, aku masih pelanggan setia roti diskon konbini kok!"
            nar "Lelucon cepat itu langsung melonggarkan ketegangan. Kedua mahasiswi tadi ikut tertawa ringan sebelum akhirnya berlalu mencari tempat duduk lain, dan suasana meja sekitar kembali ramai seperti biasa."
            nar "Namun begitu mereka pergi, Moeka tidak langsung melanjutkan makannya. Ia menaruh sumpitnya rapi di samping mangkuk yang masih hampir penuh dan menoleh padamu dengan senyum yang terlalu lebar."
            moeka "Tuh kan, beres! Untung aku cepat ketawa tadi, kalau diteruskan serius nanti satu kantin malah jadi kaku lihat kita."
            chiasa "Moemoe-senpai nggak apa-apa?"
            moeka "Nggak apa-apa banget lah, Chimian! Sudah biasa kok digosipin gara-gara penampilan gyaru begini. Aku duluan ke ruang jahit ya, masih ada pola yang belum kugunting."
            nar "Tepat saat Moeka bangkit membawa nampan makan yang nyaris utuh, Ryena kembali dari konter membawa dua gelas minuman dan langsung mengernyit keheranan."
            "Ryena" "Eh, Moeka, udonmu belum disentuh kok sudah mau pergi? Ini teh dinginmu baru kuambilkan!"
            moeka "Sudah kenyang banget kok, Ryena! Minumannya titip buat Chimian aja ya, ketemu di kelas nanti!"
            nar "Ryena menatap punggung Moeka yang berjalan cepat keluar pintu kantin, lalu menoleh pelan ke arahmu dengan wajah cemas."
            "Ryena" "Tadi meja sebelah nyindir soal foto itu lagi ya, Chiasa?"
            chiasa "Iya, sempat menyinggung soal bayaran pemotretan. Moemoe-senpai langsung membalas pakai bercanda biar mereka cepat pergi."
            "Ryena" "Aduh... kalau dia sudah tertawa sekeras itu sambil meninggalkan makanan utuh, berarti hatinya beneran lagi kena banget. Aku susul dia ke ruang jahit dulu ya."
            nar "Ryena bergegas mengambil nampannya dan berjalan cepat mengikuti arah pintu keluar. Di bangkumu yang mendadak sunyi, kamu tahu Moeka pulang dari kantin membawa satu pelajaran pahit lagi bahwa bahkan harga dirinya sendiri harus ia tutupi dengan membuat orang lain terhibur."
        else:
            nar "Kamu menunggu sampai kedua mahasiswi itu berlalu dengan cibiran kecil sambil meninggalkan tatapan dingin di meja sebelah. Begitu hanya tersisa kalian berdua, kamu mendekat setengah langkah dengan suara rendah yang tenang."
            chiasa "Kalau dibiarkan begini sampai besok, omongan anak-anak kantin bakal makin liar, Moemoe-senpai. Aku bisa langsung bantu luruskan di grup Fakultas Seni dan bilang sendiri ke anak-anak angkatan kalau itu proyek desain beneran."
            nar "Mata biru cerah Moeka sempat menyala lega mendengar tawaranmu."
            moeka "Beneran, Chimian? Kalau kamu yang ikut bicara sebagai sesama anak studio, mereka pasti lebih gampang percaya..."
            chiasa "Pasti kubantu bereskan. Tapi habis ini, kalau aku butuh bantuanmu atau minta waktu buat urusan yang kuatur, Moemoe-senpai jangan menghilang atau mendahulukan orang lain lagi ya. Kan adil kalau kita saling menjaga."
            nar "Tangan Moeka yang baru meraih gelas airnya langsung berhenti kaku di udara. Sorot lega di matanya perlahan meredup ketika ia menangkap syarat yang terikat jelas di balik uluran tanganmu."
            moeka "...Chimian. Aku kira kamu duduk di sini karena memang mau mendengar versiku dulu."
            chiasa "Aku memang dengar versimu kok, Senpai. Aku cuma nggak mau buang tenaga pasang badan buat orang yang besoknya langsung lupa."
            moeka "Kamu bukan sedang mempercayaiku. Kamu cuma menentukan apa yang harus kuberikan supaya kamu bersedia berdiri di pihakku."
            nar "Kalimat tajam itu meluncur pelan satu kali dari bibirnya, lalu ia segera menunduk menatap nampan makannya sendiri sebelum sempat memastikan apakah aman untuk terus membantahmu."
            nar "Jemarinya meraba pinggiran buku saku jadwal di samping tasnya dengan gerakan kecil yang gelisah."
            moeka "Kalau sampai pihak kampus ikut baca unggahan Meisa lalu menganggap kerjaanku melanggar aturan beasiswa, aku beneran nggak punya jalan keluar lagi..."
            chiasa "Makanya ikuti langkahku saja, Moemoe-senpai. Aku bantu tahan di grup studio sekarang, dan kamu nggak perlu bingung jalan sendirian lagi."
            moeka "...Iya. Kalau kamu bisa bantu meredam di grup studio, nanti aku usahakan ikut jadwalmu. Terima kasih, Chimian."
            nar "Kamu meraih ponselmu dengan tenang dan mengetik pesan pembelaan yang diminta tepat di hadapannya."
            "Pesan Chiasa" "Buat yang lihat unggahan foto Moemoe-senpai di forum sebelah, jaket di foto itu tugas jahitan studio lantai dua yang dia kerjakan tiga minggu penuh. Jangan asal telan potongan gosip."
            nar "Kamu meletakkan ponsel kembali ke meja. Kamu baru saja mengikat bantuannya, sementara bahu Moeka di sampingmu tampak jauh lebih berat daripada sebelum dua penggosip tadi datang."
    else:
        if kk_slot >= 3:
            nar "Lampu neon panjang menerangi Kantin Pusat yang masih ramai oleh mahasiswa selesai kelas maupun kegiatan klub. Bau kuah kari dan uap mesin teh mengisi udara di antara deretan meja panjang."
        else:
            nar "Cahaya bulan September masuk lewat deretan jendela tinggi Kantin Pusat yang dipenuhi bunyi nampan dan obrolan mahasiswa di antara jam kuliah. Aroma kuah udon dan kopi mesin memenuhi ruangan."
        nar "Kamu duduk di seberang Moeka meletakkan nampan makan dan es kopi hitammu ketika layar ponsel di beberapa meja sekitar menampilkan unggahan yang sama. Foto sesi kerja fashion Moeka bersama fotografer Kuga Renma beredar luas di akun gosip Kouseikan Whisper disertai keterangan sinis yang tidak pernah ia tulis."
        nar "Dalam tulisan Kurosawa Meisa itu, nama Kuga dan nama studionya hanya disebut satu baris sambil lalu, sementara foto wajah Moeka dan potongan gaya pakaiannya dibahas panjang lebar dengan nada merendahkan."
        if kk_has("m17b_pulau_selesai"):
            moeka "Tautan promosi studio yang waktu di pulau kemarin dikabari Ryena ternyata beneran dicomot Meisa dan dipelintir habis-habisan di forum kampus, Yutayuta..."
        else:
            moeka "Aku bahkan belum sempat cek hasil edit akhirnya dari studio Kuga, tahu-tahu fotonya sudah dipotong lalu ditempel keterangan aneh-aneh di akun gosip itu..."
        nar "Moeka memutar layar ponselnya sedikit ke arahmu. Potongan foto yang beredar sengaja memangkas habis detail jahitan bahu jaket buatannya sehingga yang tersisa hanya wajah dan gaya berdirinya di depan lampu studio."
        yutaka "Detail sambungan kain di bahu jaketmu dipotong habis sama Meisa. Kelihatan jelas dia sengaja mengatur bingkainya supaya orang mengira itu cuma foto gaya biasa."
        moeka "Padahal aku begadang tiga malam buat menyambung bordir di lengan jaket itu..."
        nar "Dua meja di belakangmu, beberapa mahasiswa saling menyenggol bahu sambil menoleh cepat ke arah rambut merah muda bergelombang dan anting hoop emas Moeka."
        yutaka "Ryena ke mana? Tumben dia nggak duduk di sebelahmu."
        moeka "Lagi antre beli teh dingin buatku biar kepalaku agak adem... soalnya dari tadi tanganku rasanya dingin banget lihat kolom komentarnya."
        nar "Belum sempat Moeka meneguk air putihnya, dua mahasiswi yang membawa nampan melambat tepat di ujung meja kalian. Salah satunya tersenyum terlalu lebar sambil memiringkan layar ponselnya ke arah Moeka."
        "Mahasiswi Kantin" "Eh, Kohinata-san, fotomu yang diunggah bareng fotografer luar kampus itu keren banget lho. Beneran sekali sesi begitu bayarannya bisa nutup dua bulan kerja konbini? Enak ya tinggal bergaya depan kamera."
        "Teman Kantin" "Iya, kalau kerja sambilan segampang itu, pantes gaya bajumu selalu kelihatan baru terus."
        nar "Nada pertanyaan itu terdengar begitu manis sampai seluruh meja sebelah langsung menoleh menahan tawa. Jemari Moeka mencengkeram pinggiran nampan plastiknya hingga ujung jarinya memucat. Untuk satu detik yang jarang terlihat, senyum ceria di wajahnya jatuh sepenuhnya."
        moeka "Itu kerjaan pemotretan dan desain beneran! Kalian lihat jaket dan potongan kain yang kupakai di foto itu juga, kan? Itu hasil jahitanku sendiri buat portofolio! Jangan disamakan dengan cerita murahan yang kalian karang sendiri di kolom komentar!"
        "Mahasiswi Kantin" "Wah, jangan marah dulu dong, Kohinata-san. Kami kan cuma nanya karena di unggahannya memang nggak ditulis soal tugas kuliah."
        nar "Mata biru cerah Moeka berkilat tegang menahan emosi di bawah sorotan mata seisi kantin, sementara Ryena masih mengantre jauh di konter minuman. Ia melirik sekilas ke arahmu yang duduk tepat di hadapannya."
        call kk_family_menu("Mo13", ["\"Hentikan omongan ngawur itu. Jaket di foto itu hasil jahitan Kohinata sendiri.\"", "Tetap diam dan biarkan Moeka menyelesaikannya sendiri.", "Tawarkan pembelaan dengan syarat Moeka mengikuti keinginanmu ke depan."])
        if _return == "A":
            nar "Kamu meletakkan sumpitmu pelan dan berdiri penuh di sisi meja. Bayangan posturmu yang tinggi dan tatapan abu-abu gelapmu yang rata langsung menghentikan senyum di wajah kedua mahasiswi tersebut."
            yutaka "Hentikan omongan ngawur itu. Nggak perlu jadi anak seni buat tahu foto yang beredar itu sengaja dipotong tepat di sambungan jahitan bahu. Aku sendiri lihat Kohinata mengerjakan jaket dan polanya bermalam-malam untuk portofolionya."
            "Mahasiswi Kantin" "Eh, Kisaragi-kun?! Kami kan cuma mengulang pertanyaan yang ramai di komentar..."
            yutaka "Komentar anonim yang bahkan nggak bisa membedakan katalog portofolio busana dengan gosip murahan? Kalau kalian nggak paham kerjaan desain dan pemotretan profesional, lebih baik cari meja lain daripada sok menilai bayaran orang di tengah kantin."
            nar "Kamu sengaja tidak memaksa Moeka membuka rincian kontrak, nominal upah, ataupun urusan keluarganya di depan umum hanya untuk dianggap pantas dibela. Kedua mahasiswi itu langsung memerah kaku di hadapan sorotan meja sekitar."
            "Teman Kantin" "Sudah, ayo cari meja belakang saja, nggak usah diperpanjang."
            nar "Begitu keduanya bergegas menjauh dan meja sebelah kembali menunduk ke piring masing-masing, Ryena tiba di meja sambil membawa dua gelas teh dingin dan menatap punggung kedua mahasiswi itu dengan kening berkerut."
            "Ryena" "Lho, ada apa tadi? Kok muka dua anak itu langsung merah banget waktu berpapasan denganku?"
            moeka "Tadi mereka nyindir soal foto studio Kuga di depan meja, terus Yutayuta langsung berdiri membantah mereka di depan satu kantin..."
            "Ryena" "Syukurlah ada kamu di sini, Kisaragi-kun. Aku tadi sudah hampir lari bawa dua gelas ini."
            nar "Kamu duduk kembali di kursimu. Moeka menatapmu diam selama dua detik penuh tanpa menyalakan tawa cerianya."
            moeka "Yutayuta... kamu barusan membantah mereka di depan satu kantin begitu?"
            yutaka "Habisnya tuduhan mereka jelas-jelas ngawur, Kohinata. Masa kerja kerasmu bermalam-malam dicap seenaknya begitu."
            nar "Tangan Moeka di pinggiran nampan perlahan mengendur. Senyum yang muncul di bibirnya kali ini jauh lebih kecil dan tidak terdengar dipaksakan."
            moeka "...Nggak banyak orang yang mau ambil risiko ikut disorot orang satu kantin cuma buat membelaku, Yutayuta. Biasanya orang cuma bilang sudahlah, biarin aja, nanti juga lupa sendiri."
            yutaka "Kalau dibiarkan terus mereka mengira boleh bicara seenaknya lagi. Makan dulu selagi udonnya masih hangat, nanti habis ini kita kirim pesan resmi ke studio Kuga supaya mencantumkan kredit desainer di unggahan aslinya."
            "Ryena" "Setuju banget! Sepulang dari sini aku ikut bantu kirim pesan ke pihak studio Kuga supaya nama desainer bajunya dipasang terang-terangan di keterangan foto."
            moeka "Iya... terima kasih banyak ya, Yutayuta, Ryena. Sungguh."
            nar "Ia mulai menyuap makanannya dengan bahu yang akhirnya turun, berhenti berpura-pura bahwa sindiran barusan hanya lelucon ringan."
        elif _return == "B":
            nar "Kamu tetap duduk menyandar memandangi gelas es kopimu, tidak mengangkat wajah maupun memotong pertanyaan kedua mahasiswi itu. Hening canggung menggantung di atas meja selama tiga detik yang terasa sangat panjang."
            nar "Moeka sempat menoleh singkat kepadamu, lalu begitu menyadari tidak ada kalimat pembelaan yang keluar darimu, ia menarik napas cepat dan segera menaikkan sudut bibirnya tinggi-tinggi."
            moeka "Haha, astaga, muka kalian serius banget sih! Kalau beneran sekali foto bisa langsung kaya raya, aku sudah beli mesin jahit baru tiga biji dari kemarin kali!"
            "Mahasiswi Kantin" "Oh... jadi cuma proyek kecil ya?"
            moeka "Iya dong, namanya juga anak desain cari pengalaman sekalian nambah uang jajan! Tenang aja, aku masih pelanggan setia roti diskon konbini kok!"
            nar "Lelucon cepat itu langsung melonggarkan ketegangan. Kedua mahasiswi tadi ikut tertawa ringan sebelum akhirnya berlalu mencari tempat duduk lain, dan suasana meja sekitar kembali ramai seperti biasa."
            nar "Namun begitu mereka pergi, Moeka tidak langsung melanjutkan makannya. Ia menaruh sumpitnya rapi di samping mangkuk yang masih hampir penuh dan menoleh padamu dengan senyum yang terlalu lebar."
            moeka "Tuh kan, beres! Untung aku cepat ketawa tadi, kalau diteruskan serius nanti satu kantin malah jadi kaku lihat kita."
            yutaka "Kamu nggak apa-apa, Kohinata?"
            moeka "Nggak apa-apa banget lah, Yutayuta! Sudah biasa kok digosipin gara-gara penampilan gyaru begini. Aku duluan ke ruang jahit ya, masih ada pola yang belum kugunting."
            nar "Tepat saat Moeka bangkit membawa nampan makan yang nyaris utuh, Ryena kembali dari konter membawa dua gelas minuman dan langsung mengernyit keheranan."
            "Ryena" "Eh, Moeka, udonmu belum disentuh kok sudah mau pergi? Ini teh dinginmu baru kuambilkan!"
            moeka "Sudah kenyang banget kok, Ryena! Minumannya titip buat Yutayuta aja ya, ketemu di kelas nanti!"
            nar "Ryena menatap punggung Moeka yang berjalan cepat keluar pintu kantin, lalu menoleh pelan ke arahmu dengan wajah cemas."
            "Ryena" "Tadi meja sebelah nyindir soal foto itu lagi ya, Kisaragi-kun?"
            yutaka "Iya, sempat menyinggung soal bayaran pemotretan. Kohinata langsung membalas pakai candaan biar mereka cepat pergi."
            "Ryena" "Aduh... kalau dia sudah tertawa sekeras itu sambil meninggalkan makanan utuh, berarti hatinya beneran lagi kena banget. Aku susul dia ke ruang jahit dulu ya."
            nar "Ryena bergegas mengambil nampannya dan berjalan cepat mengikuti arah pintu keluar. Di bangkumu yang mendadak sunyi, kamu tahu Moeka pulang dari kantin membawa satu pelajaran pahit lagi bahwa bahkan harga dirinya sendiri harus ia tutupi dengan membuat orang lain terhibur."
        else:
            nar "Kamu menunggu sampai kedua mahasiswi itu berlalu dengan cibiran kecil sambil meninggalkan tatapan dingin di meja sebelah. Begitu hanya tersisa kalian berdua, kamu mencondongkan badan sedikit dengan suara rendah yang tenang."
            yutaka "Kalau dibiarkan liar sampai besok, omongan anak-anak kantin bakal merembet ke urusan panitia beasiswa, Kohinata. Aku bisa bantu meluruskan di grup angkatan dan memastikan semua orang tahu itu proyek desain resmi."
            nar "Mata biru cerah Moeka sempat menyala lega mendengar tawaranmu."
            moeka "Beneran, Yutayuta? Kalau kamu yang ikut bicara di grup angkatan, orang-orang pasti langsung percaya..."
            yutaka "Pasti kubantu bereskan. Tapi habis ini, kalau aku butuh bantuanmu atau mengatur jadwal yang perlu kamu ikuti, jangan menghilang atau mendahulukan orang lain lagi ya. Kan adil kalau kita saling menjaga."
            nar "Tangan Moeka yang baru meraih gelas airnya langsung berhenti kaku di udara. Sorot lega di matanya perlahan meredup ketika ia menangkap syarat yang terikat jelas di balik uluran tanganmu."
            moeka "...Yutayuta. Aku kira kamu duduk di sini karena memang mau mendengar versiku dulu."
            yutaka "Aku memang dengar versimu, Kohinata. Aku cuma nggak mau buang tenaga pasang badan buat orang yang besoknya langsung lupa."
            moeka "Kamu bukan sedang mempercayaiku. Kamu cuma menentukan apa yang harus kuberikan supaya kamu bersedia berdiri di pihakku."
            nar "Kalimat tajam itu meluncur pelan satu kali dari bibirnya, lalu ia segera menunduk menatap nampan makannya sendiri sebelum sempat memastikan apakah aman untuk terus membantahmu."
            nar "Jemarinya meraba pinggiran buku saku jadwal di samping tasnya dengan gerakan kecil yang gelisah."
            moeka "Kalau sampai pihak kampus ikut baca unggahan Meisa lalu menganggap kerjaanku melanggar aturan beasiswa, aku beneran nggak punya jalan keluar lagi..."
            yutaka "Makanya ikuti langkahku saja, Kohinata. Aku bantu tahan di grup angkatan sekarang, dan kamu nggak perlu bingung jalan sendirian lagi."
            moeka "...Iya. Kalau kamu bisa bantu meredam di grup angkatan, nanti aku usahakan ikut jadwalmu. Terima kasih, Yutayuta."
            nar "Kamu meraih ponselmu dengan tenang dan mengetik pesan pembelaan yang diminta tepat di hadapannya."
            "Pesan Yutaka" "Buat yang lihat unggahan foto Kohinata di forum sebelah, jaket di foto itu tugas jahitan studio yang dia kerjakan bermalam-malam untuk portofolio. Jangan asal telan potongan gosip."
            nar "Kamu meletakkan ponsel kembali ke meja. Kamu baru saja mengikat bantuannya, sementara bahu Moeka di sampingmu tampak jauh lebih berat daripada sebelum dua penggosip tadi datang."
    return

# ┌─ PANDUAN CERITA · Mo14 · Topeng Tebal
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia tampak lebih ceria.
# │ INTI    : A tanyakan / B percaya / C manfaatkan.
# │ AKHIRAN : stage 2.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo14:
    call kk_scene_enter("moeka", "Kantin Pusat · Topeng tebal")
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Lampu neon Kantin Pusat berpendar terang di atas deretan meja panjang yang terisi mahasiswa selepas jam studio dan kegiatan klub. Bau kuah kari serta uap ketel teh memenuhi udara bulan Oktober yang mulai dingin."
        else:
            nar "Cahaya bulan Oktober mengalir masuk melalui jendela kaca lebar Kantin Pusat yang dipenuhi bunyi nampan, gesekan kursi, dan obrolan mahasiswa di antara jam kuliah. Aroma kaldu udon hangat bercampur kopi mesin memenuhi ruangan."
        nar "Bahkan sebelum kamu sempat mencari kursi kosong sambil membawa nampanmu, tawa renyah Moeka sudah lebih dulu terdengar melintasi tiga baris meja. Rambut merah muda panjang bergelombangnya memantul riang setiap kali ia melambaikan tangan, sementara anting hoop emasnya berkilau terang di bawah cahaya ruangan."
        nar "Sejak sepuluh menit terakhir, ia sudah berpindah dari satu meja ke meja lain membawa cerita baru dengan suara nyaring. Setiap kali satu kelompok selesai tertawa, ia langsung pindah menyambut meja sebelahnya."
        "Mahasiswi Seni" "Serius deh, Kohinata-san, kantong jarum pentulmu beneran tumpah di lantai kereta pagi tadi?"
        moeka "Iya dong! Untung aku pakai sepatu bot sol tebal, jadi cuma bunyi klontang-klontang terus satu gerbong langsung lihatin aku semua, haha! Mana ada bapak kantoran yang ikut bantu mungut sambil bingung lihat warnanya pink semua!"
        "Mahasiswa Seni" "Hebat juga kamu masih sempat menjahit ulang keliman jaketmu itu di tengah jadwal padat begini. Kapan tidurnya sih kamu?"
        moeka "Ah, gampang kok, tinggal pasang musik keras di kamar terus langsung kelar sebelum subuh! Tidur kan bisa dirapel habis festival bulan depan!"
        "Mahasiswa Seni" "Aduh, jangan sampai pingsan di ruang jahit aja ya. Eh, kami duluan ke ruang cetak ya, masih harus revisi poster buat festival bulan depan."
        nar "Tawa di meja itu sudah mereda dan kedua mahasiswa tersebut mulai membereskan tas mereka. Sebelum keheningan sempat mengembalikan percakapan kepada dirinya, Moeka langsung tertawa lebih keras sambil melompat ke lelucon berikutnya."
        moeka "Hati-hati ya, jangan sampai tintanya tumpah kayak jarumku! Kalau keliman rok pameranmu ada yang lepas lagi, panggil aku aja nanti!"
        "Mahasiswi Seni" "Siap, makasih banyak ya, Kohinata-san!"
        nar "Begitu mereka berdua berlalu, dua mahasiswi tingkat satu di meja seberang sempat menoleh sambil memegangi gulungan kain tipis. Moeka langsung melambai lebar ke arah mereka tanpa mengambil jeda napas."
        moeka "Eh, kain latar panggungnya kalau kepanjangan nanti kirim fotonya ke aku aja ya, biar sekalian kupotongin besok!"
        "Mahasiswi Junior" "Wah, beneran nggak merepotkan, Kohinata-senpai? Makasih banget lho!"
        nar "Baru sesudah meja seberang kembali menunduk ke makanan masing-masing, Moeka berputar menghampiri mejamu sambil melambai riang dan menjatuhkan diri ke kursi tepat di hadapanmu. Ia menaruh sebungkus roti diskon konbini yang baru digigit sedikit bersama segelas kopi manis dingin."
        moeka "Eh, Chimian! Lihat kan, aku masih bisa bikin satu barisan meja ketawa keras semua. Berarti belum kalah sama minggu ini, ya!"
        nar "Bungkus roti di atas mejanya bahkan tidak disentuhnya lagi sejak tadi. Dari jarak sedekat ini, kamu melihat lapisan riasan tipis di bawah matanya tidak sepenuhnya mampu menutupi bayangan gelap kurang tidur. Bibirnya tampak kering di bawah lip gloss cerah, dan jari-jarinya mengetuk dinding gelas plastik terlalu cepat begitu tidak ada lagi orang yang memancingnya bicara."
        chiasa "Moemoe-senpai sudah makan makanan hangat hari ini? Dari tadi kulihat cuma roti dingin itu yang dipegang, itu pun baru kegigit ujungnya."
        moeka "Sudah dong! Tadi sebelum ke sini aku sudah makan onigiri dua biji di jalan, perutku masih penuh banget kok! Lagian bulan Oktober begini jadwal pameran mulai seru, mana boleh kelihatan lemas di depan anak-anak studio."
        nar "Tepat saat itu, Hoshino Ryena melintas membawa nampannya menuju rak pengembalian dan berhenti setengah detik di ujung meja kalian dengan kening berkerut cemas."
        "Ryena" "Moeka, semalam jam dua lewat kamu masih aktif kirim daftar ukuran di grup kain ya? Jangan bilang kamu baru tidur subuh lagi."
        chiasa "Moemoe-senpai beneran begadang lagi semalam?"
        moeka "Haha, ketahuan deh! Cuma kebangun mau minum air terus nggak sengaja kepencet grup kok, Ryena! Tenang aja, aku segar banget hari ini, lihat tuh mataku melek lebar!"
        "Ryena" "Roti diskonmu saja dari tadi cuma digigit ujungnya, Moeka. Jaga badanmu sedikit dong. Aku dipanggil dosen pembimbing dulu, nanti kukabari lagi ya, Chiasa."
        nar "Ryena menggeleng pelan dengan sorot khawatir yang tidak disembunyikan, sempat bertukar lirikan singkat penuh arti kepadamu sebelum berjalan cepat keluar pintu kantin. Begitu punggung sahabatnya menghilang, Moeka segera menyedot kopi manis dinginnya terlalu cepat."
        moeka "Haha, Ryena tuh suka berlebihan kayak ibu-ibu asrama aja! Eh, Chimian, tahu nggak? Kemarin Hinari kirim gambar pita bunga warna kuning lewat ponsel Ibu, katanya mau dipakai buat acara sekolah minggu depan! Jadi nanti habis kelas aku mau sekalian jahitin tiga pita baru biar bisa kupaketkan ke rumah!"
        nar "Di meja sebelah, seorang mahasiswa yang baru lewat sempat menoleh pelan dengan senyum kagum."
        "Mahasiswa Kantin" "Gila ya, Kohinata-san energinya beneran nggak pernah habis tiap hari."
        moeka "Rahasia kecantikan dong! Kalau semangat terus nanti rezekinya ikut lancar, haha!"
        nar "Namun begitu mahasiswa itu berlalu dan kamu menunduk sekilas ke bawah meja, kamu melihat lutut kanan Moeka bergoyang naik turun sangat cepat dan gelisah, sama sekali bertolak belakang dengan suara riangnya."
        chiasa "{i}Tawanya makin keras setiap kali ruang di sekitarnya mulai sepi. Ia seperti sedang berlari secepat mungkin supaya tidak ada satu orang pun sempat melihat ke balik senyumnya.{/i}"
        call kk_family_menu("Mo14", ["\"Moemoe-senpai beneran baik-baik saja? Nggak usah pura-pura di depanku.\"", "\"Syukurlah kalau Senpai sudah membaik dan kembali ceria seperti biasa.\"", "\"Kalau Senpai sedang sanggup, boleh bantu potong kain tambahan buat stan pameran bulan depan?\""])
        if _return == "A":
            nar "Kamu meletakkan sumpitmu perlahan dan menatap Moeka lurus tanpa ikut tersenyum membalas candaannya barusan."
            chiasa "Moemoe-senpai... kamu beneran baik-baik saja? Nggak usah terus memaksa bikin lelucon di depanku."
            nar "Tawa ringan yang baru hendak keluar dari bibir Moeka langsung terpotong di tenggorokan. Sudut matanya berkedip cepat sementara senyumnya sempat menegang satu ketukan penuh."
            moeka "Baik? Tentu aja lah! ...Kenapa Chimian tiba-tiba nanya begitu? Memangnya wajahku kelihatan berantakan banget ya hari ini? Bedakku luntur?"
            nar "Tangannya refleks naik meraba pipi sendiri, lalu ia segera memiringkan tubuh berusaha mengembalikan suasana ceria seperti kebiasaannya."
            moeka "Oh iya, draf ilustrasi stanmu buat bulan depan sudah sampai mana? Kalau butuh referensi warna kain buat latar, aku masih simpan contoh beludrunya di loker lho! Mau kuambilkan sekarang?"
            chiasa "Jangan mengalihkan ke tugasku dulu, Moemoe-senpai. Aku lagi tanya soal keadaanmu sekarang."
            moeka "Haha, ya ampun, Chimian serius banget sih mukanya! Aku cuma butuh es kopi satu gelas lagi sama tidur panjang habis festival selesai, beres kok!"
            chiasa "Dari tadi setiap meja sebelah diam sebentar saja, Senpai langsung buru-buru lempar cerita lucu baru. Senpai nggak perlu membuktikan apa pun lewat wajah ceria terus-terusan. Kalau hari ini memang berat, Senpai boleh cerita hal yang sama sekali nggak lucu."
            nar "Kalimat pelan itu akhirnya menghentikan seluruh gerak tangannya. Moeka terdiam cukup lama di kursinya. Kedua tangannya meraih pinggiran meja kayu di depannya, jemarinya meremas tepi meja pelan sambil menatap seratnya seolah sedang menimbang apakah aman jika ia menurunkan pertahanannya satu inci saja."
            nar "Perlahan, lengkungan senyum yang sejak tadi ditarik tinggi itu turun sendiri hingga wajahnya tampak jauh lebih muda, jauh lebih rapuh, dan sangat letih."
            moeka "Kalau aku berhenti ketawa sebentar saja... rasanya semua hal yang sudah kutahan sejak bulan lalu bakal langsung jatuh barengan, Chimian."
            moeka "Kalau anak-anak di studio sampai tahu aku ternyata selemah ini, nanti mereka malah bingung harus bersikap gimana ke aku. Aku nggak mau jadi beban di saat semua orang juga lagi capek mikirin pameran."
            chiasa "Nggak harus dibereskan semuanya hari ini kok, Senpai. Di depanku Senpai nggak perlu jadi panitia paling ceria se-fakultas."
            nar "Kamu menggeser tisu bersih dan gelas air putih hangat ke dekat tangannya tanpa menuntut penjelasan panjang ataupun jawaban yang harus rapi."
            moeka "Jujur, aku bahkan belum tahu bisa mulai cerita dari mana. Semuanya kayak benang kusut di dalam kepala... Boleh nggak, kita duduk dulu sebentar di sini tanpa harus ada cerita apa-apa?"
            chiasa "Tentu, Moemoe-senpai. Ambil napas pelan-pelan saja dulu, aku nggak buru-buru ke mana-mana."
            nar "Moeka memejamkan mata beberapa detik sambil menyandarkan dahinya tipis ke punggung tangannya di atas meja, membiarkan riuh kantin mengalir lewat begitu saja di belakangnya."
            moeka "Rasanya baru kali ini aku duduk di kantin tanpa harus memikirkan mau melucu apa lagi..."
            nar "Beberapa menit kemudian, ia mengangkat wajah perlahan dan melirik bungkus roti dinginnya dengan sedikit rasa malu."
            moeka "Sebenarnya tadi pagi aku cuma sempat gigit roti ini dua kali di kereta, perutku dari tadi agak perih..."
            chiasa "Tunggu sebentar di sini, Senpai. Aku masih punya separuh mangkuk udon hangat yang belum kusentuh di nampan sebelah, kita bagi dua saja."
            moeka "...Boleh? Terima kasih banyak ya, Chimian."
            nar "Kamu tetap duduk tenang di seberangnya tanpa memaksa kalimat berikutnya keluar. Di tengah riuh kantin yang terus berjalan, Moeka akhirnya makan pelan dan membiarkan bahunya turun tanpa harus menghibur siapa pun."
        elif _return == "B":
            nar "Kamu ikut tersenyum lega melihat betapa ramai dan bersemangatnya ia di depan meja-meja tadi, menerima keceriaannya persis seperti yang ia tampilkan."
            chiasa "Syukurlah kalau Moemoe-senpai memang sudah membaik. Rasanya lega lihat Senpai bisa ketawa lepas lagi kayak biasa setelah minggu-minggu kemarin yang penuh gosip."
            nar "Kelopak mata Moeka berkedip satu kali mendengar pujian itu. Alih-alih mengendur, senyumnya justru ditarik semakin lebar seakan kalimatmu adalah sebuah janji baru yang wajib ia jaga mati-matian supaya tetap tampak benar."
            moeka "Iya dong! Masa aku kalah cuma gara-gara beberapa minggu yang berisik? Pokoknya mulai minggu ini aku balik jadi Moeka yang paling bisa diandalkan di studio!"
            chiasa "Hebat banget Senpai bisa cepat bangkit begini. Jangan lupa jaga tenaga buat persiapan pameran bulan depan ya."
            nar "Moeka sempat melirik arloji tipis di pergelangan tangannya dengan gerak cepat yang tersembunyi di balik tawa cerianya, lalu segera berdiri mengambil nampan."
            moeka "Aman banget, Chimian! Besok aku juga mau bawa biskuit buat anak-anak studio biar suasananya makin ramai. Habis ini aku harus balik ke ruang jahit buat ngecek ukuran manekin sebelum giliran kerja tambahanku, ketemu lagi besok ya!"
            chiasa "Iya, hati-hati di tangga, Senpai."
            chiasa "{i}Ia langsung bergegas pergi bahkan sebelum aku sempat bertanya soal jam istirahatnya.{/i}"
            nar "Ia melambai cerah sebelum berlari kecil membawa nampannya keluar pintu kantin, masih sempat melempar candaan singkat kepada dua adik tingkat di dekat gerbang."
            nar "Sepuluh menit kemudian ketika kamu melintas di selasar kaca dekat sudut mesin minuman menuju Gedung Seni Rupa, kamu tidak sengaja melihat Moeka berdiri sendirian membelakangi arah lorong."
            nar "Tidak ada satu pun orang di dekatnya. Kedua bahunya meluruh jatuh menyandar pada kusen kaca, dahinya sempat menempel diam ke kaca dingin sementara tangannya memijat pangkal hidungnya dengan wajah benar-benar hampa oleh kelelahan."
            nar "Ia menatap layar catatan jadwal kerja paruh waktunya dalam diam cukup lama, lalu tiba-tiba layar ponsel di tangannya menyala terang oleh dua pesan beruntun dari grup panitia pameran."
            "Pesan Grup" "Kohinata-san, tolong kirim satu foto ceria buat halaman promosi pameran dong!"
            "Pesan Grup" "Yang senyumnya paling cerah ya biar stan Fakultas Seni kelihatan seru!"
            nar "Dalam hitungan satu tarikan napas, Moeka langsung menegakkan bahu, menepuk kedua pipinya ringan, dan mengangkat kamera. Pada jepretan pertama, ia mengernyit melihat sudut matanya yang masih terlalu kaku di layar lalu segera menghapusnya."
            nar "Ia menarik kedua sudut bibirnya lebih tinggi lagi, mengangkat dua jari di samping pipinya, lalu memotret senyum ceria kedua yang sama sekali tidak sampai ke matanya."
            nar "Begitu foto terkirim dan layar ponsel meredup kembali, senyum itu langsung lenyap dalam sekejap seolah tidak pernah menempel di wajahnya."
            chiasa "{i}Ia sampai mengulang fotonya dua kali sendirian di lorong cuma supaya tidak ada yang melihat betapa lelahnya ia sebenarnya...{/i}"
            nar "Kamu memilih tidak memanggilnya dari kejauhan dan terus melangkah pelan melewati tikungan lorong. Kini mengakui bahwa dirinya sedang buruk pun mulai terasa baginya seperti mengecewakan keyakinanmu."
        else:
            nar "Melihat betapa penuh tenaga ia bersikeras terlihat di depan seluruh kantin, kamu mencondongkan badan sedikit dan langsung memanfaatkan keterbukaannya."
            chiasa "Bagus deh kalau Moemoe-senpai lagi penuh tenaga begini. Kebetulan jadwalku minggu ini lagi padat banget, boleh aku titip bantu potong kain spanduk sama rapikan daftar perlengkapan stan buat festival bulan depan?"
            nar "Senyum Moeka tidak goyah sedikit pun. Ia bahkan langsung mengangguk mantap sebelum sempat membuka buku saku jadwalnya."
            moeka "Bisa banget, Chimian! Urusan potong kain sama cek daftar begitu kan gampang banget buatku, serahkan ke aku aja!"
            chiasa "Serius nggak keberatan? Kalau sekalian cek ulang daftar lampu sorot dari gudang panitia bisa juga nggak, Senpai? Tenggatnya dua hari lagi soalnya."
            moeka "Sekalian aja biar rapi sekalian! Nanti aku mampir gudang habis kelas. Biar kucatat sekarang biar nggak lupa."
            nar "Ia mengeluarkan buku saku kecil yang sampulnya sudah agak lusuh lalu membukanya di atas meja. Dari seberang, kamu melihat jelas setiap baris di halaman minggu ini sudah penuh sesak oleh jadwal kuliah, dua blok kerja paruh waktu berdekatan, lingkaran tanggal biaya obat rumah, dan tugas studio hingga nyaris tanpa ruang kosong."
            nar "Moeka sempat membolak-balik dua halaman bersebelahan sambil bergumam pelan menghitung jam keretanya."
            moeka "Hmm... kalau dari konbini lari ke stasiun jam sepuluh malam, sampai kos setengah sebelas berarti masih sempat menggunting spanduk sampai jam satu..."
            nar "Ia memiringkan bukunya dan menyelipkan ketiga tugas tambahanmu dengan tulisan sangat kecil di tepi bawah halaman yang hampir tidak menyisakan ruang putih."
            chiasa "Jadwal Senpai di halaman itu kelihatan padat sekali. Itu jadwal kerja paruh waktu dua tempat sekaligus?"
            moeka "Ah, cuma kelihatan penuh gara-gara tulisanku kegedean kok! Tinggal geser jam tidur sejam doang pasti beres semua, gampang lah."
            nar "Ia menutup buku saku itu dengan bunyi tepukan kecil, lalu mengangkat wajah dengan senyum lebar yang terdengar terlalu ringan untuk beban yang baru ia tuliskan."
            moeka "Tenang, aku urus semua. Kalau aku kelihatan nggak capek, mungkin tubuhku ikut percaya."
            chiasa "Makasih banyak ya, Moemoe-senpai. Nanti kain spanduknya kutaruh di meja studio lantai dua."
            moeka "Sip! Aku duluan ke ruang kain ya, Chimian, mau langsung ambil gunting sama meteran!"
            chiasa "{i}Ia bahkan tidak mengecek apakah tubuhnya masih sanggup berdiri besok sebelum mengiyakan seluruh permintaan tambahanku.{/i}"
            nar "Ia tertawa ceria sesudahnya sambil bergegas pergi membawa tumpukan jadwal yang sudah melampaui batas. Kamu mendapatkan bantuan yang kamu inginkan dari seseorang yang baru saja memberitahumu betapa keras ia berusaha menyembunyikan retakannya."
    else:
        if kk_slot >= 3:
            nar "Lampu neon Kantin Pusat berpendar terang di atas deretan meja panjang yang terisi mahasiswa selepas jam kuliah dan kegiatan panitia. Bau kuah kari serta uap ketel teh memenuhi udara bulan Oktober yang mulai dingin."
        else:
            nar "Cahaya bulan Oktober mengalir masuk melalui jendela kaca lebar Kantin Pusat yang dipenuhi bunyi nampan, gesekan kursi, dan obrolan mahasiswa di antara jam kuliah. Aroma kaldu udon hangat bercampur kopi mesin memenuhi ruangan."
        nar "Bahkan sebelum kamu sempat mencari meja kosong sambil membawa nampan makan dan es kopi hitammu, tawa renyah Moeka sudah lebih dulu terdengar melintasi tiga baris meja. Rambut merah muda panjang bergelombangnya memantul riang setiap kali ia melambaikan tangan, sementara anting hoop emasnya berkilau terang di bawah cahaya ruangan."
        nar "Sejak sepuluh menit terakhir, ia sudah berpindah dari satu meja ke meja lain membawa cerita baru dengan suara nyaring. Setiap kali satu kelompok selesai tertawa, ia langsung pindah menyambut meja sebelahnya."
        "Mahasiswi Seni" "Serius deh, Kohinata-san, kantong jarum pentulmu beneran tumpah di lantai kereta pagi tadi?"
        moeka "Iya dong! Untung aku pakai sepatu bot sol tebal, jadi cuma bunyi klontang-klontang terus satu gerbong langsung lihatin aku semua, haha! Mana ada bapak kantoran yang ikut bantu mungut sambil bingung lihat warnanya pink semua!"
        "Mahasiswa Seni" "Hebat juga kamu masih sempat menjahit ulang keliman jaketmu itu di tengah jadwal padat begini. Kapan tidurnya sih kamu?"
        moeka "Ah, gampang kok, tinggal pasang musik keras di kamar terus langsung kelar sebelum subuh! Tidur kan bisa dirapel habis festival bulan depan!"
        "Mahasiswa Seni" "Aduh, jangan sampai pingsan di ruang jahit aja ya. Eh, kami duluan ke ruang cetak ya, masih harus revisi poster buat festival bulan depan."
        nar "Tawa di meja itu sudah mereda dan kedua mahasiswa tersebut mulai membereskan tas mereka. Sebelum keheningan sempat mengembalikan percakapan kepada dirinya, Moeka langsung tertawa lebih keras sambil melompat ke lelucon berikutnya."
        moeka "Hati-hati ya, jangan sampai tintanya tumpah kayak jarumku! Kalau keliman rok pameranmu ada yang lepas lagi, panggil aku aja nanti!"
        "Mahasiswi Seni" "Siap, makasih banyak ya, Kohinata-san!"
        nar "Begitu mereka berdua berlalu, dua mahasiswi tingkat satu di meja seberang sempat menoleh sambil memegangi gulungan kain tipis. Moeka langsung melambai lebar ke arah mereka tanpa mengambil jeda napas."
        moeka "Eh, kain latar panggungnya kalau kepanjangan nanti kirim fotonya ke aku aja ya, biar sekalian kupotongin besok!"
        "Mahasiswi Junior" "Wah, beneran nggak merepotkan, Kohinata-senpai? Makasih banget lho!"
        nar "Baru sesudah meja seberang kembali menunduk ke makanan masing-masing, Moeka berputar menghampiri mejamu sambil melambai riang dan menjatuhkan diri ke kursi tepat di hadapanmu. Ia menaruh sebungkus roti diskon konbini yang baru digigit sedikit bersama segelas kopi manis dingin."
        moeka "Eh, Yutayuta! Lihat kan, aku masih bisa bikin satu barisan meja ketawa keras semua. Berarti belum kalah sama minggu ini, ya!"
        nar "Bungkus roti di atas mejanya bahkan tidak disentuhnya lagi sejak tadi. Dari jarak sedekat ini, kamu melihat lapisan riasan tipis di bawah matanya tidak sepenuhnya mampu menutupi bayangan gelap kurang tidur. Bibirnya tampak kering di bawah lip gloss cerah, dan jari-jarinya mengetuk dinding gelas plastik terlalu cepat begitu tidak ada lagi orang yang memancingnya bicara."
        yutaka "Kamu sudah makan makanan hangat hari ini, Kohinata? Dari tadi kulihat cuma roti dingin itu yang kamu bawa, itu pun baru kegigit ujungnya."
        moeka "Sudah dong! Tadi sebelum ke sini aku sudah makan onigiri dua biji di jalan, perutku masih penuh banget kok! Lagian bulan Oktober begini jadwal pameran mulai seru, mana boleh kelihatan lemas di depan anak-anak panitia."
        nar "Tepat saat itu, Hoshino Ryena melintas membawa nampannya menuju rak pengembalian dan berhenti setengah detik di ujung meja kalian dengan kening berkerut cemas."
        "Ryena" "Moeka, semalam jam dua lewat kamu masih aktif kirim daftar ukuran di grup kain ya? Jangan bilang kamu baru tidur subuh lagi."
        yutaka "Beneran begadang lagi semalam, Kohinata?"
        moeka "Haha, ketahuan deh! Cuma kebangun mau minum air terus nggak sengaja kepencet grup kok, Ryena! Tenang aja, aku segar banget hari ini, lihat tuh mataku melek lebar!"
        "Ryena" "Roti diskonmu saja dari tadi cuma digigit ujungnya, Moeka. Jaga badanmu sedikit dong. Aku dipanggil dosen pembimbing dulu, nanti kukabari lagi ya, Kisaragi-kun."
        nar "Ryena menggeleng pelan dengan sorot khawatir yang tidak disembunyikan, sempat bertukar lirikan singkat penuh arti kepadamu sebelum berjalan cepat keluar pintu kantin. Begitu punggung sahabatnya menghilang, Moeka segera menyedot kopi manis dinginnya terlalu cepat."
        moeka "Haha, Ryena tuh suka berlebihan kayak ibu-ibu asrama aja! Eh, Yutayuta, tahu nggak? Kemarin Hinari kirim gambar pita bunga warna kuning lewat ponsel Ibu, katanya mau dipakai buat acara sekolah minggu depan! Jadi nanti habis kelas aku mau sekalian jahitin tiga pita baru biar bisa kupaketkan ke rumah!"
        nar "Di meja sebelah, seorang mahasiswa yang baru lewat sempat menoleh pelan dengan senyum kagum."
        "Mahasiswa Kantin" "Gila ya, Kohinata-san energinya beneran nggak pernah habis tiap hari."
        moeka "Rahasia kecantikan dong! Kalau semangat terus nanti rezekinya ikut lancar, haha!"
        nar "Namun begitu mahasiswa itu berlalu dan kamu melirik sekilas ke bawah meja, kamu melihat lutut kanan Moeka bergoyang naik turun sangat cepat dan gelisah, sama sekali bertolak belakang dengan suara riangnya."
        yutaka "{i}Tawanya makin keras setiap kali ruang di sekitarnya mulai sepi. Ia seperti sedang berlari secepat mungkin supaya tidak ada satu orang pun sempat melihat ke balik senyumnya.{/i}"
        call kk_family_menu("Mo14", ["\"Kamu beneran baik-baik saja, Kohinata? Nggak usah pura-pura di depanku.\"", "\"Syukurlah kalau kamu sudah membaik dan kembali ceria seperti biasa.\"", "\"Kalau kamu sedang sanggup, boleh bantu cek ulang nota sama daftar lampu stan bulan depan?\""])
        if _return == "A":
            nar "Kamu meletakkan sumpitmu perlahan dan menyandarkan lengan yang melingkari jam tangan tali kulit di tepi meja, menatap Moeka lurus tanpa ikut tertawa membalas candaannya barusan."
            yutaka "Kohinata... kamu beneran baik-baik saja? Nggak usah terus memaksa bikin lelucon di depanku."
            nar "Tawa ringan yang baru hendak keluar dari bibir Moeka langsung terpotong di tenggorokan. Sudut matanya berkedip cepat sementara senyumnya sempat menegang satu ketukan penuh."
            moeka "Baik? Tentu aja lah! ...Kenapa kamu tiba-tiba nanya begitu, Yutayuta? Memangnya wajahku kelihatan berantakan banget ya hari ini? Bedakku luntur?"
            nar "Tangannya refleks naik meraba pipi sendiri, lalu ia segera memiringkan tubuh berusaha mengembalikan suasana ceria seperti kebiasaannya."
            moeka "Oh iya, lembar rincian dana pameran buat bulan depan sudah kamu cek semua, Yutayuta? Kalau perlu bantuan menyortir nota belanja kain dari anak-anak seni, aku masih simpan salinannya di tas lho!"
            yutaka "Jangan mengalihkan ke urusan panitia dulu, Kohinata. Aku lagi tanya soal keadaanmu sekarang."
            moeka "Haha, ya ampun, tampangmu serius banget sih! Aku cuma butuh es kopi satu gelas lagi sama tidur panjang habis festival selesai, beres kok!"
            yutaka "Dari tadi setiap meja sebelah diam sebentar saja, kamu langsung buru-buru lempar cerita lucu baru. Kamu nggak perlu membuktikan apa pun lewat wajah ceria terus-terusan. Kalau hari ini memang berat, kamu boleh cerita hal yang sama sekali nggak lucu."
            nar "Kalimat datar yang tenang itu akhirnya menghentikan seluruh gerak tangannya. Moeka terdiam cukup lama di kursinya. Kedua tangannya meraih pinggiran meja kayu di depannya, jemarinya meremas tepi meja pelan sambil menatap seratnya seolah sedang menimbang apakah aman jika ia menurunkan pertahanannya satu inci saja."
            nar "Perlahan, lengkungan senyum yang sejak tadi ditarik tinggi itu turun sendiri hingga wajahnya tampak jauh lebih muda, jauh lebih rapuh, dan sangat letih."
            moeka "Kalau aku berhenti ketawa sebentar saja... rasanya semua hal yang sudah kutahan sejak bulan lalu bakal langsung jatuh barengan, Yutayuta."
            moeka "Kalau anak-anak di studio sampai tahu aku ternyata selemah ini, nanti mereka malah bingung harus bersikap gimana ke aku. Aku nggak mau jadi beban di saat semua orang juga lagi capek mikirin pameran."
            yutaka "Nggak harus dibereskan semuanya hari ini, Kohinata. Di depanku kamu nggak perlu jadi orang paling ceria se-kampus."
            nar "Kamu menggeser tisu bersih dan gelas air putih hangat ke dekat tangannya tanpa menuntut penjelasan panjang ataupun jawaban yang harus rapi."
            moeka "Jujur, aku bahkan belum tahu bisa mulai cerita dari mana. Semuanya kayak benang kusut di dalam kepala... Boleh nggak, kita duduk dulu sebentar di sini tanpa harus ada cerita apa-apa?"
            yutaka "Boleh. Ambil napas pelan-pelan saja dulu, aku nggak buru-buru ke mana-mana."
            nar "Moeka memejamkan mata beberapa detik sambil menyandarkan dahinya tipis ke punggung tangannya di atas meja, membiarkan riuh kantin mengalir lewat begitu saja di belakangnya."
            moeka "Rasanya baru kali ini aku duduk di kantin tanpa harus memikirkan mau melucu apa lagi..."
            nar "Beberapa menit kemudian, ia mengangkat wajah perlahan dan melirik bungkus roti dinginnya dengan sedikit rasa malu."
            moeka "Sebenarnya tadi pagi aku cuma sempat gigit roti ini dua kali di kereta, perutku dari tadi agak perih..."
            yutaka "Tunggu di sini sebentar. Porsi nasi kari hangat di nampanku ini masih banyak dan belum disentuh setengahnya, kita bagi dua saja biar perutmu keisi."
            moeka "...Boleh? Terima kasih banyak ya, Yutayuta."
            nar "Kamu tetap duduk tenang di seberangnya tanpa memaksa kalimat berikutnya keluar. Di tengah riuh kantin yang terus berjalan, Moeka akhirnya makan pelan dan membiarkan bahunya turun tanpa harus menghibur siapa pun."
        elif _return == "B":
            nar "Kamu ikut tersenyum santai melihat betapa ramai dan bersemangatnya ia di depan meja-meja tadi, menerima keceriaannya persis seperti yang ia tampilkan."
            yutaka "Syukurlah kalau kamu memang sudah membaik, Kohinata. Rasanya lega lihat kamu bisa ketawa lepas lagi kayak biasa setelah minggu-minggu kemarin yang penuh gosip."
            nar "Kelopak mata Moeka berkedip satu kali mendengar pujian itu. Alih-alih mengendur, senyumnya justru ditarik semakin lebar seakan kalimatmu adalah sebuah janji baru yang wajib ia jaga mati-matian supaya tetap tampak benar."
            moeka "Iya dong! Masa aku kalah cuma gara-gara beberapa minggu yang berisik? Pokoknya mulai minggu ini aku balik jadi Moeka yang paling bisa diandalkan di panitia!"
            yutaka "Bagus lah kalau sudah segar lagi. Jangan lupa jaga tenaga buat persiapan pameran bulan depan."
            nar "Moeka sempat melirik arloji tipis di pergelangan tangannya dengan gerak cepat yang tersembunyi di balik tawa cerianya, lalu segera berdiri mengambil nampan."
            moeka "Aman banget, Yutayuta! Besok aku juga mau bawa biskuit buat anak-anak studio biar suasananya makin ramai. Habis ini aku harus balik ke ruang jahit buat ngecek ukuran manekin sebelum giliran kerja tambahanku, ketemu lagi besok ya!"
            yutaka "Oke, hati-hati di jalan."
            yutaka "{i}Ia langsung bergegas pergi bahkan sebelum aku sempat bertanya soal jam istirahatnya.{/i}"
            nar "Ia melambai cerah sebelum berlari kecil membawa nampannya keluar pintu kantin, masih sempat melempar candaan singkat kepada dua mahasiswa di dekat gerbang."
            nar "Sepuluh menit kemudian ketika kamu melintas di selasar kaca dekat sudut mesin minuman menuju gedung kuliah, kamu tidak sengaja melihat Moeka berdiri sendirian membelakangi arah lorong."
            nar "Tidak ada satu pun orang di dekatnya. Kedua bahunya meluruh jatuh menyandar pada kusen kaca, dahinya sempat menempel diam ke kaca dingin sementara tangannya memijat pangkal hidungnya dengan wajah benar-benar hampa oleh kelelahan."
            nar "Ia menatap layar catatan jadwal kerja paruh waktunya dalam diam cukup lama, lalu tiba-tiba layar ponsel di tangannya menyala terang oleh dua pesan beruntun dari grup panitia pameran."
            "Pesan Grup" "Kohinata-san, tolong kirim satu foto ceria buat halaman promosi pameran dong!"
            "Pesan Grup" "Yang senyumnya paling cerah ya biar stan Fakultas Seni kelihatan seru!"
            nar "Dalam hitungan satu tarikan napas, Moeka langsung menegakkan bahu, menepuk kedua pipinya ringan, dan mengangkat kamera. Pada jepretan pertama, ia mengernyit melihat sudut matanya yang masih terlalu kaku di layar lalu segera menghapusnya."
            nar "Ia menarik kedua sudut bibirnya lebih tinggi lagi, mengangkat dua jari di samping pipinya, lalu memotret senyum ceria kedua yang sama sekali tidak sampai ke matanya."
            nar "Begitu foto terkirim dan layar ponsel meredup kembali, senyum itu langsung lenyap dalam sekejap seolah tidak pernah menempel di wajahnya."
            yutaka "{i}Ia sampai mengulang fotonya dua kali sendirian di lorong cuma supaya tidak ada yang melihat betapa lelahnya ia sebenarnya...{/i}"
            nar "Kamu memilih tidak memanggilnya dari kejauhan dan terus melangkah pelan melewati tikungan lorong. Kini mengakui bahwa dirinya sedang buruk pun mulai terasa baginya seperti mengecewakan keyakinanmu."
        else:
            nar "Melihat betapa penuh tenaga ia bersikeras terlihat di depan seluruh kantin, kamu mencondongkan badan sedikit dan langsung memanfaatkan keterbukaannya untuk meringankan daftar tugasmu sendiri."
            yutaka "Bagus lah kalau kamu lagi penuh tenaga begini, Kohinata. Kebetulan berkas dana pameran di mejaku lagi menumpuk, boleh aku titip kamu bantu cek ulang nota bahan kain sekaligus merapikan ukuran spanduk stan buat festival bulan depan?"
            nar "Senyum Moeka tidak goyah sedikit pun. Ia bahkan langsung mengangguk mantap sebelum sempat membuka buku saku jadwalnya."
            moeka "Bisa banget, Yutayuta! Urusan nota bahan sama cek spanduk begitu kan gampang banget buatku, serahkan ke aku aja!"
            yutaka "Serius nggak keberatan? Kalau sekalian cek ulang daftar lampu sorot dari gudang panitia bisa juga? Tenggatnya dua hari lagi."
            moeka "Sekalian aja biar rapi sekalian! Nanti aku mampir gudang habis kelas. Biar kucatat sekarang biar nggak lupa."
            nar "Ia mengeluarkan buku saku kecil yang sampulnya sudah agak lusuh lalu membukanya di atas meja. Dari seberang, kamu melihat jelas setiap baris di halaman minggu ini sudah penuh sesak oleh jadwal kuliah, dua blok kerja paruh waktu berdekatan, lingkaran tanggal biaya obat rumah, dan tugas studio hingga nyaris tanpa ruang kosong."
            nar "Moeka sempat membolak-balik dua halaman bersebelahan sambil bergumam pelan menghitung jam keretanya."
            moeka "Hmm... kalau dari konbini lari ke stasiun jam sepuluh malam, sampai kos setengah sebelas berarti masih sempat cek nota sama ukur spanduk sampai jam satu..."
            nar "Ia memiringkan bukunya dan menyelipkan ketiga tugas tambahanmu dengan tulisan sangat kecil di tepi bawah halaman yang hampir tidak menyisakan ruang putih."
            yutaka "Halaman jadwalmu kelihatan penuh sekali. Itu giliran kerja paruh waktu dua tempat sekaligus?"
            moeka "Ah, cuma kelihatan penuh gara-gara tulisanku kegedean kok! Tinggal geser jam tidur sejam doang pasti beres semua, gampang lah."
            nar "Ia menutup buku saku itu dengan bunyi tepukan kecil, lalu mengangkat wajah dengan senyum lebar yang terdengar terlalu ringan untuk beban yang baru ia tuliskan."
            moeka "Tenang, aku urus semua. Kalau aku kelihatan nggak capek, mungkin tubuhku ikut percaya."
            yutaka "Makasih banyak, Kohinata. Nanti map notanya kukirimkan lewat ruang kegiatan mahasiswa."
            moeka "Sip! Aku duluan ke ruang kain ya, Yutayuta, mau langsung ambil meteran!"
            yutaka "{i}Ia bahkan tidak mengecek apakah tubuhnya masih sanggup berdiri besok sebelum mengiyakan seluruh permintaan tambahanku.{/i}"
            nar "Ia tertawa ceria sesudahnya sambil bergegas pergi membawa tumpukan jadwal yang sudah melampaui batas. Kamu mendapatkan bantuan yang kamu inginkan dari seseorang yang baru saja memberitahumu betapa keras ia berusaha menyembunyikan retakannya."
    return

# ┌─ PANDUAN CERITA · Mo15 · Surat Peringatan Beasiswa
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : beasiswa diperingatkan.
# │ INTI    : A hadir / B bantu cari bantuan / C abaikan.
# │ AKHIRAN : gerbang rute; jendela #2.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo15:
    call kk_scene_enter("moeka", "Kantin Pusat · Surat peringatan beasiswa")
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Lampu neon Kantin Pusat masih menyala terang di atas barisan meja panjang yang sudah mulai kosong selepas kegiatan Festival Seni. Hanya suara pegawai dapur merapikan panci di balik konter yang terdengar samar di udara dingin bulan November."
        else:
            nar "Cahaya bulan November mengalir masuk melewati kaca lebar Kantin Pusat yang mulai lengang setelah jam makan ramai berlalu. Kursi-kursi plastik tergeser acak di sekitar meja panitia Fakultas Seni yang baru saja selesai dipakai rapat kecil."
        nar "Moeka baru saja merapikan gulungan kain latar dan daftar giliran jaga stan bersama dua mahasiswa tingkat satu. Rambut merah muda panjang bergelombangnya diikat longgar ke samping, sementara anting hoop emasnya beradu pelan tiap kali ia melambaikan tangan melepas mereka."
        "Mahasiswi Panitia" "Makasih banyak ya, Kohinata-senpai! Kalau nggak dibantu rapikan tadi, ukuran latar panggungnya pasti keliru."
        moeka "Aman banget dong! Semangat ya buat besok, jangan lupa bawa peniti cadangan biar nggak panik pas tamu sudah mulai datang!"
        "Mahasiswa Panitia" "Eh, Senpai nggak sekalian ikut naik ke ruang studio buat ngecek lampu sorot?"
        moeka "Kalian duluan aja ya! Aku masih mau duduk minum teh sebentar sama Chimian biar kakiku lurus dulu, nanti aku nyusul kalau perlu."
        "Mahasiswa Panitia" "Siap, Senpai! Kami duluan ke ruang studio ya, Amamiya-san!"
        chiasa "Hati-hati di tangga ya, gulungannya lumayan berat."
        nar "Begitu langkah rombongan panitia itu hilang di balik pintu geser kantin dan seluruh deretan meja di sekitar kalian benar-benar kosong, bahu Moeka perlahan merosot turun. Senyum cerah yang tadi menempel sempurna di wajahnya langsung padam tanpa perlu menunggu aba-aba."
        nar "Kamu menaruh dua gelas kertas teh hangat dari mesin minuman di tengah meja. Moeka menatap uap tipis yang naik dari gelasnya selama beberapa detik tanpa langsung menyentuhnya."
        chiasa "Teh hangatnya mumpung masih ngebul, Moemoe-senpai. Tangan Senpai kelihatan dingin banget dari tadi."
        moeka "...Makasih ya, Chimian. Rasanya aneh banget begitu kantin mendadak sepi begini."
        if kk_has("topeng_moeka_ditanya"):
            chiasa "{i}Kali ini ia bahkan tidak mencoba menahan tawanya lagi begitu orang-orang sudah pergi.{/i}"
        else:
            chiasa "{i}Begitu kantin sepi, wajahnya kelihatan jauh lebih pucat dibanding lima menit yang lalu.{/i}"
        nar "Moeka duduk diam beberapa detik memandangi permukaan meja, lalu membuka saku resleting terdalam tas kainnya. Jarinya sempat berhenti ragu di tepi ritsleting sebelum ia mengembuskan napas pendek dan menarik keluar buku saku kecil penuh coretan hitungan jam kerja dan angka yen, lengkap dengan catatan terpisah untuk ongkos kereta pulang ke kota satelit, iuran sekolah Reito dan Soura, serta buku gambar Hinari."
        nar "Dari selipan paling belakang buku saku itu, ia menarik keluar selembar kertas resmi berkop bagian kemahasiswaan universitas."
        nar "Lipatan kertas itu sudah lunak dan nyaris sobek tipis di bagian tengah karena terlalu sering dibuka lalu dilipat lagi di dalam tas, padahal belum pernah ia tunjukkan kepada siapa pun."
        chiasa "Moemoe-senpai... itu amplop dari kantor administrasi kemahasiswaan ya? Dan di buku saku itu semuanya hitungan pengeluaran rumah?"
        moeka "Iya, Chimian... surat ini sudah tiga hari kusimpan terus di tas. Setiap kali mau kubuang ke dasar laci kos, tanganku malah otomatis mengambilnya lagi dan membacanya ulang di kereta sambil mencocokkannya dengan angka pengeluaran bulan ini."
        chiasa "Kenapa baru sekarang Senpai keluarkan? Tiga hari disimpan sendiri pasti berat banget di kepala."
        moeka "Habisnya tiap mau kubuka di ruang studio, selalu ada anak-anak yang datang nanya ukuran kain atau minta foto. Nggak ada celah buat kelihatan bingung."
        nar "Ia menggeser lembar itu setengah jalan ke tengah meja agar kamu bisa melihat judul resminya yang dicetak tebal, pemberitahuan peringatan kelayakan beasiswa prestasi."
        moeka "Aku baca terus bagian yang bilang kalau indeks prestasiku turun satu semester lagi dari batas tiga koma dua, beasiswa penuhku langsung dicabut mulai semester depan."
        chiasa "Batasnya tiga koma dua... dan ini baru peringatan pertama ya, Senpai?"
        moeka "Iya, peringatan pertama. Tapi lihat kalimat di halaman resminya deh, Chimian. Semuanya cuma angka rata-rata, daftar kehadiran mata kuliah teori, sama tenggat evaluasi akhir semester."
        moeka "Nggak ada satu pun kolom di surat ini yang menuliskan kalau mahasiswanya sudah berusaha mati-matian tapi tetap kehabisan waktu. Nggak ada kolom buat jadwal cuci darah ayahku di rumah, nggak ada kolom buat shift konbini sampai tengah malam, apalagi buat bantu Ibu mengurus sekolah Reito, Soura, sama Hinari."
        nar "Jari-jarinya menyentuh pinggir kertas yang mulai mengeriting, lalu ia tertawa pendek tanpa suara sambil menunduk."
        moeka "Aku tahu surat kampus memang nggak dibuat buat menampung cerita hidup orang satu per satu. Aku cuma... sudah tiga hari memelototi kertas ini sendirian di kamar, rasanya pengap banget. Aku cuma ingin ada satu orang yang dengar tanpa langsung kaget."
        chiasa "Ryena-san atau Ibu di rumah belum tahu soal surat ini?"
        moeka "Belum... mana berani aku bilang ke Ibu, Chimian. Ibu sudah kerja dua tempat buat menutup biaya obat Ayah. Kalau aku kasih tahu beasiswaku terancam, Ibu pasti langsung menyuruhku pulang terus nggak usah mikirin uang kos lagi, padahal..."
        nar "Kalimatnya terputus begitu saja. Bibirnya bergetar tipis sementara mata biru cerahnya berkaca-kaca, menahan diri agar air matanya tidak jatuh membasahi kertas resmi di atas meja."
        call kk_family_menu("Mo15", ["\"Aku nggak ke mana-mana, Moemoe-senpai. Ceritakan pelan-pelan, aku dengerin sampai habis.\"", "\"Ayo kita cek tenggat banding sama bantuan darurat kampus sekarang, Senpai. Kita cari jalan keluarnya.\"", "Minta maaf sedang dikejar jadwal dan tinggalkan pembicaraan."])
        if _return == "A":
            nar "Kamu meletakkan tas sketsamu ke kursi sebelah, menggeser gelas teh hangat yang baru kamu beli ke dekat tangan Moeka, lalu duduk menghadapnya dengan tenang."
            chiasa "Aku nggak ke mana-mana kok, Moemoe-senpai. Suratnya taruh dulu aja di meja, terus ceritakan pelan-pelan dari bagian yang paling berat buat Senpai. Aku dengerin sampai habis."
            nar "Moeka mengangkat wajahnya dengan kelopak mata yang sedikit memerah, tampak tidak percaya karena kamu tidak langsung mencecarnya dengan angka ataupun ceramah tentang jadwal belajar."
            moeka "Kamu beneran mau duduk menemani di sini sampai aku selesai bicara, Chimian? Padahal panitia pameran pasti juga lagi sibuk..."
            chiasa "Pameran masih ada anak-anak lain yang jaga. Sekarang giliran Senpai yang didengarkan."
            moeka "...Entah kenapa, dengar kalimat segitu aja rasanya sudah menahan satu hal besar di dadaku supaya nggak langsung runtuh."
            nar "Ia menarik napas dalam beberapa kali sebelum akhirnya mulai bicara pelan. Ia bercerita dari angka nilai mata kuliah teori desain yang melorot karena dua kali tertidur di kelas pagi sehabis lembur, lalu terhenti cukup lama ketika masuk ke ketakutannya memberi kabar kepada ibunya, Yaeka."
            moeka "Tiap kali aku kirim uang belanja ke rumah, Ibu selalu balas pesan panjang bilang jangan lupa makan enak di Tokyo dan jaga kuliahnya baik-baik. Kemarin Hinari juga kirim foto pita kuning buatannya sambil bilang nanti mau masuk kampus desain kayak aku..."
            chiasa "Pasti berat banget menahan semua itu sendiri sambil terus senyum di depan Ryena-san sama anak-anak studio ya, Senpai."
            moeka "Iya... kalau aku kelihatan goyang sedikit aja di depan Ryena, dia pasti langsung panik dan memaksaku istirahat, padahal kalau aku berhenti kerja satu minggu saja tagihan di rumah bisa meleset."
            moeka "Kalau aku berhenti kuliah buat kerja penuh waktu, sebenarnya biaya di rumah bakal langsung jauh lebih ringan kan, Chimian? Kadang di kereta pulang malam aku mikir begitu terus..."
            chiasa "Terus kalau boleh jujur sama dirimu sendiri hari ini, Moemoe-senpai sebenarnya pengin berhenti, atau masih pengin lanjut?"
            nar "Keheningan turun cukup lama di meja kantin. Jemari Moeka mencengkeram cangkir teh hangatnya, lalu setetes air mata akhirnya jatuh ke punggung tangannya sebelum ia buru-buru menyekanya dengan lengan sweter."
            moeka "...Aku masih ingin kuliah, Chimian. Jujur banget, aku masih pengin belajar bikin koleksi pakaianku sendiri dan berdiri di panggung kelulusan Seni Rupa. Aku bukan cuma takut kehilangan biaya beasiswanya... aku beneran belum mau melepaskan tempat ini."
            chiasa "Koleksi pakaian kayak gimana yang paling pengin Senpai buat untuk pameran kelulusan nanti?"
            nar "Untuk satu detik yang hangat, sorot lelah di mata biru cerahnya melunak sedikit saat ia memandangi jari-jarinya sendiri."
            moeka "Mantel musim dingin warna krem sama merah muda pudar pakai renda jahitan tangan yang bahannya gampang dirawat... supaya orang biasa pun bisa merasa cantik tanpa harus keluar uang jutaan."
            chiasa "Keinginan sejelas itu berharga banget, Senpai. Aku nggak bisa janji semuanya bakal gampang atau langsung beres besok, tapi paling nggak mulai hari ini Senpai nggak perlu menyimpan ketakutan itu sendirian lagi."
            moeka "Kamu bahkan nggak bilang semua pasti bakal lolos dengan mudah kayak orang lain... anehnya itu justru bikin aku jauh lebih tenang, Chimian."
            chiasa "Minum tehnya pelan-pelan dulu ya, Senpai. Habis ini kalau mau jalan bareng sampai gerbang stasiun juga aku temani."
            moeka "Makasih ya, Chimian... rasanya kepalaku baru bisa bernapas lagi setelah tiga hari penuh sesak. Iya, nanti kita jalan bareng pelan-pelan."
            nar "Kamu tetap duduk di seberangnya sampai seluruh ceritanya selesai tanpa menyela ataupun menggurui. Di bawah lampu kantin yang tenang, Moeka melipat surat itu kembali dengan tangan yang tidak lagi gemetar."
        elif _return == "B":
            nar "Kamu menarik kursi sedikit lebih dekat, membuka buku catatan kecil di tasmu, lalu menatap surat peringatan itu dengan keseriusan yang langsung membuat Moeka berhenti tenggelam dalam rasa panik sendirian."
            chiasa "Moemoe-senpai, jangan hadapi ini sendirian pakai cara nekat nambah kerja lagi ya. Ayo kita periksa tenggat bandingnya sama cari jalur bantuan darurat kampus sekarang, pasti masih ada pintu yang bisa diketuk."
            moeka "Kamu mau bantu aku cari jalan keluarnya sekarang, Chimian? ...Beasiswa darurat, keringanan biaya kuliah, atau penjadwalan ulang kerja paruh waktu... beneran masih ada pintunya?"
            chiasa "Pasti ada prosedur khusus buat mahasiswa yang kondisi keluarganya berubah mendadak. Coba lihat di bagian bawah suratnya, ada jadwal konsultasi bagian kemahasiswaan atau nama petugas penanggung jawabnya nggak?"
            nar "Moeka mengerjap cepat, lalu menunduk memeriksa catatan kaki berhuruf kecil di bagian paling bawah surat yang selama tiga hari ini bahkan terlewat oleh matanya karena terlalu fokus pada ancaman pencabutan."
            moeka "Eh... ada! Tertulis pengajuan peninjauan kondisi ekonomi keluarga paling lambat dua puluh lima November di loket tiga gedung administrasi, dengan surat keterangan rawat jalan rumah sakit."
            chiasa "Nah, berarti masih ada waktu sebelum akhir bulan! Terus soal tugas kuliah teori yang nilainya turun kemarin, mata kuliah mana yang paling butuh dikejar duluan?"
            moeka "Sejarah Desain Modern sama analisis bahan tekstil... dua-duanya jadwal pagi, jadi catatanku banyak yang bolong."
            chiasa "Kebetulan aku punya fotokopian rangkuman semester lalu dari kelas dasar yang materinya nyambung, nanti kubawakan buat Senpai belajar pelan-pelan."
            nar "Kamu membuka halaman informasi dana dukungan mahasiswa Kouseikan di ponselmu lalu memutar layarnya menghadap Moeka. Di sana tercantum skema hibah darurat non-pinjaman serta kontak konselor akademik yang biasa mendampingi kasus perubahan kondisi keluarga."
            moeka "Aku kira selama ini kalau uang kurang, satu-satunya cara ya cuma ambil lebih banyak giliran kerja malam atau terima tawaran pemotretan mahal dari studio luar kayak Kuga..."
            chiasa "Justru kalau Senpai nambah kerja malam lagi, nilai semester depan pasti makin terancam jatuh dan beasiswanya malah beneran hilang. Kita harus lihat dulu beban mana yang bisa dikurangi bulan ini supaya tenagamu nggak terus terkuras."
            nar "Kamu menuding buku saku jadwal Moeka yang terbuka di sebelah surat peringatan. Bersama-sama kalian melingkari dua shift larut malam dengan upah paling kecil yang paling sering membuatnya tertidur di kelas pagi."
            moeka "Bener juga ya... selama ini jawabanku selalu otomatis mengiyakan semua tambahan kerja tanpa pernah menghitung apa yang dikorbankan."
            chiasa "Selain loket tiga, kita juga bisa tanya dosen wali Fakultas Seni buat rekomendasi peninjauan, atau minta jadwal bicara sama konselor Sato Kyoko supaya berkasnya ikut dikawal resmi."
            nar "Ia mengeluarkan pulpen berwarna merah muda dari kotak pensilnya dan menuliskan rapi nomor loket tiga gedung administrasi, nama petugas konseling beasiswa, serta jadwal pengumpulan surat medis ayahnya di halaman bersih buku sakunya."
            moeka "Aku juga mau kirim pesan singkat ke Ryena sekarang buat pinjam catatan dua kelas teori yang sempat kulewati minggu kemarin. Daripada terus pura-pura sudah mengejar semuanya sendiri..."
            nar "Ia membuka ruang obrolan ponselnya dan mengetik pesan jujur itu di depanmu, lalu menarik napas lega kecil ketika tombol kirim ditekan."
            chiasa "Langkah bagus banget, Senpai. Besok habis kelas pagi mau kutemani mampir ke loket tiga buat ambil formulir bandingnya sekalian?"
            moeka "Kalau kamu nggak keberatan... mau banget, Chimian. Rasanya jauh lebih nggak menakutkan kalau nggak harus berdiri di depan loket itu sendirian."
            chiasa "Beres, besok kita atur jamnya. Sekarang makan sesuatu yang hangat dulu ya sebelum pulang ke kos."
            nar "Untuk pertama kalinya dalam beberapa minggu terakhir, Moeka menutup tasnya dengan satu rencana konkret yang tidak memaksanya mengorbankan sisa tenaganya sendiri."
        else:
            nar "Kamu melirik arloji di pergelangan tanganmu lalu menarik tas sketsamu ke pangkuan, merasakan beban surat itu terasa terlalu berat untuk ikut kamu tanggung hari ini."
            chiasa "Maaf banget, Moemoe-senpai... aku masih harus balik ke ruang studio buat mengecek ulang instalasi pameran sebelum pintunya dikunci penjaga. Kayaknya aku nggak bisa tinggal lama-lama sekarang."
            nar "Kalimat itu jatuh dingin di antara meja panjang yang kosong. Tangan Moeka yang tadi setengah terulur di samping surat resmi itu langsung terhenti."
            nar "Dalam hitungan dua detik, topeng ceria yang tadi sempat luruh kembali terpasang cepat di wajahnya, seolah ia mendadak malu karena baru saja menunjukkan sisi terlemahnya kepada adik tingkatnya."
            moeka "Eh, ya ampun, bener juga! Pameran kan masih jalan, aku malah menahanmu di sini buat dengar keluhan nggak penting begini! Maaf ya, Chimian, suasana jadi tegang gara-gara aku!"
            chiasa "Nggak apa-apa kok, Senpai. Semoga urusan suratnya cepat ketemu jalannya ya."
            moeka "Pasti beres kok, tenang aja! Aku kan jago cari akal, haha. Lagian habis ini aku juga masih harus mampir toko benang buat tambah bahan stan kok, hampir lupa!"
            nar "Ia buru-buru melipat kembali surat peringatan yang sudutnya sudah lunak itu, memasukkannya jauh ke dasar tas kainnya hingga tidak lagi tampak, lalu berdiri ikut membenahi kursi dengan gerak terlalu cepat."
            moeka "...Aku nggak kelihatan terlalu membesar-besarkan masalah tadi kan, Chimian?"
            chiasa "Nggak kok, Senpai. Cuma memang jadwalku lagi mepet aja sekarang."
            moeka "Iya, tentu aja! Duluan aja ke studio, Chimian, nanti pintunya keburu dikunci penjaga! Aku juga mau mampir beli minum bentar sebelum naik kereta."
            chiasa "Iya, aku duluan ya, Moemoe-senpai. Hati-hati di jalan."
            moeka "Sampai ketemu besok di pameran ya, Chimian!"
            nar "Ketika kamu melangkah keluar dari pintu geser kantin dan sempat menoleh sekali melewati kaca jendela, Moeka belum juga beranjak pergi. Begitu yakin tidak ada lagi orang di sekelilingnya, ia kembali duduk sendirian di kursi panjang yang kosong, menarik amplop putih itu setengah keluar dari tasnya dengan bahu mengecil."
            nar "Gelas teh hangat di depannya mendingin tanpa pernah disentuh. Besok surat yang sama akan tetap menuntut jawaban, sementara hari ini ia belum menemukan satu tempat pun untuk mengatakan dengan aman bahwa dirinya sudah tidak sanggup menjawab semuanya sendirian."
    else:
        if kk_slot >= 3:
            nar "Lampu neon Kantin Pusat masih menyala terang di atas barisan meja panjang yang sudah mulai kosong selepas kegiatan Festival Seni. Hanya suara pegawai dapur merapikan panci di balik konter yang terdengar samar di udara dingin bulan November."
        else:
            nar "Cahaya bulan November mengalir masuk melewati kaca lebar Kantin Pusat yang mulai lengang setelah jam makan ramai berlalu. Kursi-kursi plastik tergeser acak di sekitar meja panitia yang baru saja dipakai memeriksa nota akhir festival."
        nar "Kamu baru selesai mencocokkan salinan tanda terima sewa lampu panggung bersama Moeka dan dua mahasiswa panitia tingkat satu. Rambut merah muda panjang bergelombang Moeka diikat longgar ke samping, sementara anting hoop emasnya beradu pelan setiap kali ia melambaikan tangan melepas mereka."
        "Mahasiswi Panitia" "Makasih banyak ya, Kohinata-senpai, Kisaragi-senpai! Kalau nggak dibantu rapikan tadi, hitungan ukuran kain panggung sama anggarannya pasti meleset."
        moeka "Aman banget dong! Semangat ya buat besok, jangan lupa bawa peniti cadangan biar nggak panik pas tamu sudah mulai datang!"
        "Mahasiswa Panitia" "Senpai nggak sekalian naik ke ruang panitia buat serahin map nota ini?"
        yutaka "Biar nanti aku aja yang taruh di loker panitia. Kalian duluan saja sebelum tangga belakang dikunci."
        "Mahasiswa Panitia" "Siap, Kisaragi-senpai! Kami duluan ya, Kohinata-senpai!"
        nar "Begitu langkah rombongan panitia itu hilang di balik pintu geser kantin dan seluruh deretan meja di sekitar kalian benar-benar kosong, bahu Moeka perlahan merosot turun. Senyum cerah yang tadi menempel sempurna di wajahnya langsung padam tanpa perlu menunggu aba-aba."
        nar "Kamu menggeser segelas teh hangat dari mesin minuman ke dekat lengannya. Moeka menatap uap tipis yang naik dari gelas kertas itu selama beberapa detik tanpa langsung menyentuhnya."
        yutaka "Teh hangatnya diminum dulu, Kohinata. Dari tadi tanganmu kelihatan dingin banget waktu menyusun kwitansi."
        moeka "...Makasih ya, Yutayuta. Rasanya aneh banget begitu kantin mendadak sepi begini."
        if kk_has("topeng_moeka_ditanya"):
            yutaka "{i}Kali ini ia bahkan tidak mencoba memaksakan tawa keras lagi begitu seluruh panitia sudah pergi.{/i}"
        else:
            yutaka "{i}Begitu ruang kantin kosong, wajahnya kelihatan jauh lebih pucat dibanding lima menit yang lalu.{/i}"
        nar "Moeka duduk diam beberapa detik memandangi permukaan meja, lalu membuka saku resleting terdalam tas kainnya. Jarinya sempat berhenti ragu di tepi ritsleting sebelum ia mengembuskan napas pendek dan menarik keluar buku saku penuh coretan jam kerja serta rincian pengeluaran ongkos kereta pulang ke kota satelit, iuran sekolah Reito dan Soura, serta buku gambar Hinari."
        nar "Dari selipan paling belakang buku saku itu, ia menarik keluar selembar kertas resmi berkop bagian kemahasiswaan universitas."
        nar "Lipatan kertas itu sudah lunak dan nyaris sobek tipis di bagian tengah karena terlalu sering dibuka lalu dilipat lagi di dalam tas, padahal belum pernah ia tunjukkan kepada siapa pun."
        yutaka "Kohinata... itu amplop dari kantor administrasi kemahasiswaan? Bukan nota festival kan?"
        moeka "Iya, Yutayuta... surat ini sudah tiga hari kusimpan terus di tas. Setiap kali mau kubuang ke dasar laci kos, tanganku malah otomatis mengambilnya lagi dan membacanya ulang di kereta sambil mencocokkannya dengan catatan uang bulan ini."
        yutaka "Tiga hari kamu simpan sendirian di tas sambil tetap mengurus stan festival?"
        moeka "Habisnya tiap mau kubuka di ruang panitia atau studio, selalu ada anak-anak yang datang nanya ukuran kain atau minta foto. Nggak ada celah buat kelihatan bingung."
        nar "Ia menggeser lembar itu setengah jalan ke tengah meja agar kamu bisa melihat judul resminya yang dicetak tebal, pemberitahuan peringatan kelayakan beasiswa prestasi."
        moeka "Aku baca terus bagian yang bilang kalau indeks prestasiku turun satu semester lagi dari batas tiga koma dua, beasiswa penuhku langsung dicabut mulai semester depan."
        yutaka "Batasnya tiga koma dua... dan ini baru peringatan pertama kan?"
        moeka "Iya, peringatan pertama. Tapi lihat kalimat di halaman resminya deh, Yutayuta. Semuanya cuma angka rata-rata, daftar kehadiran mata kuliah teori, sama tenggat evaluasi akhir semester."
        moeka "Nggak ada satu pun kolom di surat ini yang menuliskan kalau mahasiswanya sudah berusaha mati-matian tapi tetap kehabisan waktu. Nggak ada kolom buat jadwal cuci darah ayahku di rumah, nggak ada kolom buat shift konbini sampai tengah malam, apalagi buat bantu Ibu mengurus sekolah Reito, Soura, sama Hinari."
        nar "Jari-jarinya menyentuh pinggir kertas yang mulai mengeriting, lalu ia tertawa pendek tanpa suara sambil menunduk."
        moeka "Aku tahu surat kampus memang nggak dibuat buat menampung cerita hidup orang satu per satu. Aku cuma... sudah tiga hari memelototi kertas ini sendirian di kamar, rasanya pengap banget. Aku cuma ingin ada satu orang yang dengar tanpa langsung kaget."
        yutaka "Ryena atau ibumu di rumah belum tahu soal surat ini?"
        moeka "Belum... mana berani aku bilang ke Ibu, Yutayuta. Ibu sudah kerja dua tempat buat menutup biaya obat Ayah. Kalau aku kasih tahu beasiswaku terancam, Ibu pasti langsung menyuruhku pulang terus nggak usah mikirin uang kos lagi, padahal..."
        nar "Kalimatnya terputus begitu saja. Bibirnya bergetar tipis sementara mata biru cerahnya berkaca-kaca, menahan diri agar air matanya tidak jatuh membasahi kertas resmi di atas meja."
        call kk_family_menu("Mo15", ["\"Aku nggak ke mana-mana, Kohinata. Ceritakan pelan-pelan, aku dengerin sampai habis.\"", "\"Ayo kita cek tenggat banding sama bantuan darurat kampus sekarang, Kohinata. Kita cari jalan keluarnya.\"", "Minta maaf masih harus mengurus berkas panitia dan tinggalkan pembicaraan."])
        if _return == "A":
            nar "Kamu menaruh map nota panitia ke kursi sebelah, menyandarkan lengan yang melingkari jam tangan tali kulit di atas meja, lalu menatap Moeka tenang."
            yutaka "Aku nggak ke mana-mana kok, Kohinata. Suratnya taruh dulu saja di meja, terus ceritakan pelan-pelan dari bagian yang paling berat buatmu. Aku dengerin sampai habis."
            nar "Moeka mengangkat wajahnya dengan kelopak mata yang sedikit memerah, tampak tidak percaya karena kamu tidak langsung menyodorkan hitung-hitungan dingin ataupun ceramah jadwal belajar."
            moeka "Kamu beneran mau duduk menemani di sini sampai aku selesai bicara, Yutayuta? Padahal nota festival masih harus kamu serahkan kan..."
            yutaka "Loker panitia bisa kutunggu besok pagi. Sekarang giliran kamu yang bicara tanpa harus menghibur siapa pun."
            moeka "...Entah kenapa, dengar kalimat segitu aja rasanya sudah menahan satu hal besar di dadaku supaya nggak langsung runtuh."
            nar "Ia menarik napas dalam beberapa kali sebelum akhirnya mulai bicara pelan. Ia bercerita dari angka nilai mata kuliah teori desain yang melorot karena dua kali tertidur di kelas pagi sehabis lembur, lalu terhenti cukup lama ketika masuk ke ketakutannya memberi kabar kepada ibunya, Yaeka."
            moeka "Tiap kali aku kirim uang belanja ke rumah, Ibu selalu balas pesan panjang bilang jangan lupa makan enak di Tokyo dan jaga kuliahnya baik-baik. Kemarin Hinari juga kirim foto pita kuning buatannya sambil bilang nanti mau masuk kampus desain kayak aku..."
            yutaka "Pasti berat banget menahan semua itu sendiri sambil terus tertawa paling keras di depan Ryena sama anak-anak panitia."
            moeka "Iya... kalau aku kelihatan goyang sedikit aja di depan Ryena, dia pasti langsung panik dan memaksaku istirahat, padahal kalau aku berhenti kerja satu minggu saja tagihan di rumah bisa meleset."
            moeka "Kalau aku berhenti kuliah buat kerja penuh waktu, sebenarnya biaya di rumah bakal langsung jauh lebih ringan kan, Yutayuta? Kadang di kereta pulang malam aku mikir begitu terus..."
            yutaka "Terus kalau boleh jujur sama dirimu sendiri hari ini, kamu sebenarnya memang mau berhenti, atau masih pengin lanjut?"
            nar "Keheningan turun cukup lama di meja kantin. Jemari Moeka mencengkeram cangkir teh hangatnya, lalu setetes air mata akhirnya jatuh ke punggung tangannya sebelum ia buru-buru menyekanya dengan lengan sweter."
            moeka "...Aku masih ingin kuliah, Yutayuta. Jujur banget, aku masih pengin belajar bikin koleksi pakaianku sendiri dan berdiri di panggung kelulusan Seni Rupa. Aku bukan cuma takut kehilangan biaya beasiswanya... aku beneran belum mau melepaskan tempat ini."
            yutaka "Koleksi pakaian kayak gimana yang paling pengin kamu buat untuk pameran kelulusan nanti?"
            nar "Untuk satu detik yang hangat, sorot lelah di mata biru cerahnya melunak sedikit saat ia memandangi jari-jarinya sendiri."
            moeka "Mantel musim dingin warna krem sama merah muda pudar pakai renda jahitan tangan yang bahannya gampang dirawat... supaya orang biasa pun bisa merasa cantik tanpa harus keluar uang jutaan."
            yutaka "Keinginan sejelas itu berharga banget, Kohinata. Aku nggak bisa janji semuanya bakal gampang atau langsung beres besok, tapi paling nggak mulai hari ini kamu nggak perlu menyimpan ketakutan itu sendirian lagi."
            moeka "Kamu bahkan nggak bilang semua pasti bakal lolos dengan mudah kayak orang lain... anehnya itu justru bikin aku jauh lebih tenang, Yutayuta."
            yutaka "Minum tehnya pelan-pelan dulu. Habis ini kalau mau jalan bareng sampai gerbang stasiun juga aku temani."
            moeka "Makasih ya, Yutayuta... rasanya kepalaku baru bisa bernapas lagi setelah tiga hari penuh sesak. Iya, nanti kita jalan bareng pelan-pelan."
            nar "Kamu tetap duduk di seberangnya sampai seluruh ceritanya selesai tanpa menyela ataupun menggurui. Di bawah lampu kantin yang tenang, Moeka melipat surat itu kembali dengan tangan yang tidak lagi gemetar."
        elif _return == "B":
            nar "Kamu menarik kursi sedikit lebih dekat, membuka buku catatan kecil di tasmu, lalu menatap surat peringatan itu dengan ketelitian anak Ekonomi yang langsung membuat Moeka berhenti tenggelam dalam rasa panik sendirian."
            yutaka "Kohinata, jangan hadapi ini sendirian pakai cara nekat nambah jam kerja lagi. Ayo kita periksa tenggat bandingnya sama jalur bantuan darurat kampus sekarang, pasti masih ada pintu yang bisa diketuk."
            moeka "Kamu mau bantu aku cari jalan keluarnya sekarang, Yutayuta? ...Beasiswa darurat, keringanan biaya kuliah, atau penjadwalan ulang kerja paruh waktu... beneran masih ada pintunya?"
            yutaka "Di buku panduan administrasi Kouseikan selalu ada prosedur khusus buat mahasiswa yang kondisi ekonomi keluarganya berubah mendadak. Coba lihat catatan kaki di bagian paling bawah suratmu, ada jadwal konsultasi atau nama loketnya nggak?"
            nar "Moeka mengerjap cepat, lalu menunduk memeriksa catatan kaki berhuruf kecil di bagian paling bawah surat yang selama tiga hari ini bahkan terlewat oleh matanya karena terlalu fokus pada ancaman pencabutan."
            moeka "Eh... ada! Tertulis pengajuan peninjauan kondisi ekonomi keluarga paling lambat dua puluh lima November di loket tiga gedung administrasi, dengan surat keterangan rawat jalan rumah sakit."
            yutaka "Nah, berarti masih ada waktu sebelum akhir bulan. Terus soal mata kuliah teori yang nilainya turun kemarin, kelas mana yang paling krusial buat dikejar sebelum ujian akhir?"
            moeka "Sejarah Desain Modern sama analisis bahan tekstil... dua-duanya jadwal pagi, jadi catatanku banyak yang bolong."
            yutaka "Kalau begitu kita hitung ulang sekalian beban kerjamu di buku saku itu. Sebagai orang bagian dana, aku bisa langsung lihat mana shift yang cuma menguras tenagamu dengan upah paling tipis."
            nar "Kamu membuka halaman informasi dana dukungan mahasiswa Kouseikan di ponselmu lalu memutar layarnya menghadap Moeka. Di sana tercantum skema hibah darurat non-pinjaman serta kontak konselor akademik yang biasa mendampingi kasus perubahan kondisi keluarga."
            moeka "Aku kira selama ini kalau uang kurang, satu-satunya cara ya cuma ambil lebih banyak giliran kerja malam atau terima tawaran pemotretan mahal dari studio luar kayak Kuga..."
            yutaka "Kalau kamu nambah kerja malam terus, nilai semester depan makin anjlok dan kerugian dari hilangnya beasiswa penuhmu jauh lebih besar daripada upah shift mana pun. Yang harus dipotong dulu itu jadwal larut malam yang bikin kamu ketiduran di kelas pagi."
            nar "Kamu menuding dua kotak jadwal kerja paling larut di buku saku Moeka. Bersama-sama kalian membandingkan jam tidur, ongkos kereta, dan opsi pengurangan beban yang masuk akal."
            moeka "Bener juga ya... selama ini jawabanku selalu otomatis mengiyakan semua tambahan kerja tanpa pernah menghitung apa yang dikorbankan."
            yutaka "Selain loket tiga, kamu juga bisa minta rekomendasi dosen wali Fakultas Seni atau jadwal bicara dengan konselor Sato Kyoko supaya berkas bandingmu ikut dikawal resmi."
            nar "Ia mengeluarkan pulpen berwarna merah muda dari kotak pensilnya dan menuliskan rapi nomor loket tiga gedung administrasi, nama petugas konseling beasiswa, serta jadwal pengumpulan surat medis ayahnya di halaman bersih buku sakunya."
            moeka "Aku juga mau kirim pesan singkat ke Ryena sekarang buat pinjam catatan dua kelas teori yang sempat kulewati minggu kemarin. Daripada terus pura-pura sudah mengejar semuanya sendiri..."
            nar "Ia membuka ruang obrolan ponselnya dan mengetik pesan jujur itu di depanmu, lalu menarik napas lega kecil ketika tombol kirim ditekan."
            yutaka "Langkah yang tepat, Kohinata. Besok habis kelas pagi mau kutemani mampir ke loket tiga buat ambil formulir bandingnya sekalian?"
            moeka "Kalau kamu nggak keberatan... mau banget, Yutayuta. Rasanya jauh lebih nggak menakutkan kalau nggak harus berdiri di depan loket itu sendirian."
            yutaka "Beres, besok kita atur jamnya. Sekarang makan sesuatu yang hangat dulu sebelum pulang ke kos."
            nar "Untuk pertama kalinya dalam beberapa minggu terakhir, Moeka menutup tasnya dengan satu rencana konkret yang tidak memaksanya mengorbankan sisa tenaganya sendiri."
        else:
            nar "Kamu melirik jam tangan tali kulit di pergelangan tanganmu lalu meraih map nota festival ke atas pangkuan, merasakan beban surat itu terlalu berat untuk ikut kamu tanggung hari ini."
            yutaka "Maaf banget, Kohinata... aku masih harus menyerahkan rekap nota sewa lampu ke ruang panitia sebelum kuncinya dibawa penjaga. Kayaknya aku nggak bisa tinggal lama-lama sekarang."
            nar "Kalimat itu jatuh dingin di antara meja panjang yang kosong. Tangan Moeka yang tadi setengah terulur di samping surat resmi itu langsung terhenti."
            nar "Dalam hitungan dua detik, topeng ceria yang tadi sempat luruh kembali terpasang cepat di wajahnya, seolah ia mendadak malu karena baru saja menunjukkan sisi terlemahnya kepada rekan panitianya."
            moeka "Eh, ya ampun, bener juga! Urusan rekap dana festival kan lebih penting, aku malah menahanmu di sini buat dengar keluhan nggak penting begini! Maaf ya, Yutayuta, suasana jadi tegang gara-gara aku!"
            yutaka "Nggak apa-apa. Semoga urusan suratnya cepat ketemu jalannya."
            moeka "Pasti beres kok, tenang aja! Aku kan jago cari akal, haha. Lagian habis ini aku juga masih harus mampir toko benang buat tambah bahan stan kok, hampir lupa!"
            nar "Ia buru-buru melipat kembali surat peringatan yang sudutnya sudah lunak itu, memasukkannya jauh ke dasar tas kainnya hingga tidak lagi tampak, lalu berdiri ikut membenahi kursi dengan gerak terlalu cepat."
            moeka "...Aku nggak kelihatan terlalu membesar-besarkan masalah tadi kan, Yutayuta?"
            yutaka "Nggak kok. Cuma memang jadwalku lagi mepet saja sekarang."
            moeka "Iya, tentu aja! Duluan aja ke ruang panitia, Yutayuta, nanti lokernya keburu dikunci penjaga! Aku juga mau mampir beli minum bentar sebelum naik kereta."
            yutaka "Oke, aku duluan ya, Kohinata. Hati-hati di jalan."
            moeka "Sampai ketemu besok di pameran ya, Yutayuta!"
            nar "Ketika kamu melangkah keluar dari pintu geser kantin dan sempat menoleh sekali melewati kaca jendela, Moeka belum juga beranjak pergi. Begitu yakin tidak ada lagi orang di sekelilingnya, ia kembali duduk sendirian di kursi panjang yang kosong, menarik amplop putih itu setengah keluar dari tasnya dengan bahu mengecil."
            nar "Gelas teh hangat di depannya mendingin tanpa pernah disentuh. Besok surat yang sama akan tetap menuntut jawaban, sementara hari ini ia belum menemukan satu tempat pun untuk mengatakan dengan aman bahwa dirinya sudah tidak sanggup menjawab semuanya sendirian."
    return

# ┌─ PANDUAN CERITA · Mo16 · Nilai Kedua
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : semester kedua rendah.
# │ INTI    : A temani / B bantu cari kerja / C tinggalkan.
# │ AKHIRAN : beasiswa terancam dicabut.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo16:
    call kk_scene_enter("moeka", "Kantin Pusat · Nilai kedua")
    nar "Nilai kedua tidak memberi ruang bagi alasan yang dahulu ia pakai untuk menenangkan diri. Moeka melihat hasilnya sambil memegang daftar sif kerja, mencoba mencari pengorbanan lain yang belum diberikan."
    moeka "Aku sudah mengurangi tidur. Mengurangi makan. Ternyata tetap bisa gagal. Aku mulai nggak tahu bagian mana lagi yang boleh diminta berhenti."
    call kk_family_menu("Mo16", ["Temani ia melewati masa ini.", "Bantu ia mencari kerja yang aman.", "Tinggalkan ia."])
    if _return == "A":
        moeka "Kau tetap di sini meski aku begini? ...Kenapa?"
        nar "Kau menyebut bahwa kehadiranmu tidak dibayar dengan nilai yang baik. Moeka menangis diam-diam, kesal karena justru kalimat sederhana itu membuat pertahanannya runtuh."
        moeka "Aku masih ingin mencoba. Tapi aku butuh cara yang nggak menghabiskan orangnya dulu."
    elif _return == "B":
        moeka "Kerja yang jelas, bukan yang seperti Kuga tawarkan... ya. Itu lebih baik. Terima kasih."
        nar "Kalian membicarakan waktu dan syarat dengan terbuka. Tidak semua lowongan cocok; menolak yang buruk membuat masalah uang belum selesai, tetapi menjaga agar satu kesulitan tidak ditukar dengan keterikatan baru yang lebih merusak."
    else:
        nar "Kau pergi sebelum pembicaraan selesai. Moeka membalas pamit dengan senyum kecil, lalu kembali menatap dua daftar yang saling memakan waktu."
        nar "Ia tidak mengejarmu. Rasa malu membuat bantuan terasa semakin mahal untuk diminta, terlebih kepada orang yang sudah melihatnya gagal dua kali."
    return

# ┌─ PANDUAN CERITA · Mo17 · Menghilang dari Grup Chat
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : Valentine.
# │ INTI    : A datangi / B tunggu / C abaikan.
# │ AKHIRAN : stage 3 (penarikan diri).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo17:
    call kk_scene_enter("moeka", "Kantin Pusat · Menghilang dari grup chat")
    nar "Moeka keluar dari grup yang biasanya paling ramai olehnya. Ia menyebut ingin mengurangi distraksi pada satu grup, tidak memberi alasan pada yang lain. Di percakapan pribadi fotonya juga mulai jarang berubah."
    nar "Valentine berjalan dengan rencana orang lain. Ketidakhadirannya tampak mudah dijelaskan sampai kau mencoba mengingat kapan terakhir mendengar kabarnya sungguhan."
    call kk_family_menu("Mo17", ["Datangi ia langsung.", "Tunggu ia kembali sendiri.", "Abaikan."])
    if _return == "A":
        moeka "Kau datang sendiri? ...Aku pikir kalau aku menghilang pelan-pelan, tidak ada yang akan sadar."
        nar "Kau memberi tahu sebelum datang dan menanyakan apakah ia ingin ditemani. Ia membuka pintu dengan kamar yang tidak serapi senyum biasanya, lalu membiarkanmu melihat bahwa hari-harinya sudah menjadi sulit."
    elif _return == "B":
        nar "Kau menunggu ia kembali. Grup tetap ramai oleh orang lain; Moeka tidak kembali masuk. Setiap hari yang lewat membuat menyapa lagi terasa memerlukan penjelasan lebih panjang."
        nar "Kebebasan mengambil jarak memang miliknya. Tanpa pertanyaan yang tenang, kau belum tahu apakah jarak tersebut sedang menolong atau justru membuatnya makin sendirian."
    else:
        nar "Kau mengabaikan perubahan itu. Ketika seseorang bertanya, percakapan segera mendapat jawaban bahwa Moeka pasti sibuk. Semua orang mengenal cukup banyak kesibukannya untuk mempercayai alasan yang tidak pernah mereka tanyakan kepadanya."
    return

# ┌─ PANDUAN CERITA · Mo18 · Ryena Bicara
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : Ryena menegur pemain.
# │ INTI    : A dengarkan / B tolak / C bela diri.
# │ AKHIRAN : sekutu atau lawan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo18:
    call kk_scene_enter("moeka", "Kantin Pusat · Ryena bicara")
    nar "Ryena menunggumu setelah kegiatan selesai. Ia tidak membawa gosip atau pertanyaan tentang siapa yang sedang disukai Moeka. Di tangannya ada daftar pertemuan yang belakangan dibatalkan sahabatnya."
    "Ryena" "Aku khawatir. Ini sudah lebih dari sibuk atau salah jadwal. Aku ingin kita menghubungi dia dan cari bantuan kalau perlu. Jangan tunggu sampai kita harus menyesal karena semua orang mengira orang lain sudah bertanya."
    call kk_family_menu("Mo18", ["Dengarkan peringatan Ryena.", "Tolak ikut campur.", "Bela diri bahwa itu bukan salahmu."])
    if _return == "A":
        "Ryena" "Terima kasih mau dengar. Aku tidak tahu harus minta tolong ke siapa lagi."
        nar "Kalian membicarakan apa yang benar-benar diketahui dan siapa yang dekat secara fisik malam ini. Ryena tidak memintamu menjadi satu-satunya penanggung jawab; justru ia ingin lingkar dukungan Moeka lebih luas daripada satu telepon."
    elif _return == "B":
        "Ryena" "...Begitu. Kukira kau berbeda. Maaf sudah mengganggu."
        nar "Ia pergi untuk mencari orang lain. Penolakanmu membuat jalannya lebih sulit, tetapi tidak memberinya alasan membiarkan Moeka hanya ditangani oleh kesediaanmu peduli."
    else:
        "Ryena" "Tidak ada yang menyalahkanmu. Aku cuma minta kau tidak menambah beratnya."
        nar "Kau membela catatan bantuanmu sendiri. Ryena mendengar, lalu mengatakan pembicaraan ini tentang keadaan Moeka sekarang, bukan pertandingan tentang siapa paling bersih dari kesalahan."
    return

# ┌─ PANDUAN CERITA · Mo19 · Barang yang Dibagikan
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia membagikan barang kesayangan.
# │ INTI    : A tanya / B terima / C abaikan.
# │ AKHIRAN : jendela #3; stage 4 (tanda bahaya).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo19:
    call kk_scene_enter("moeka", "Kantin Pusat · Barang yang dibagikan")
    nar "Moeka memberikan gunting kain favoritnya, lalu aksesori yang dahulu diperbaiki berkali-kali agar tetap dapat dipakai. Ia mengatakan sedang merapikan kamar. Saat ditanya mengapa sekarang, ia menyebut tidak akan butuh lagi dengan nada terlalu ringan."
    nar "Perubahan itu datang bersama banyak kabar lain yang sudah membuatmu khawatir. Barang-barang ini tidak menjelaskan semuanya, tetapi cukup untuk tidak dilewatkan sebagai kegiatan beres-beres biasa."
    call kk_family_menu("Mo19", ["Tanya kenapa ia membagikan semuanya.", "Terima pemberiannya tanpa berpikir.", "Abaikan isyarat itu."])
    if _return == "A":
        moeka "Kenapa? ...Cuma beres-beres. Jangan dibesar-besarkan. ...Tapi kau menyadarinya, ya."
        nar "Kau menanyakan apakah ia sedang berpikir mengakhiri hidup dan tetap mendengarkan setelah pertanyaan itu keluar. Moeka tidak langsung menjawab. Kau memberinya waktu tanpa mundur menjadi lelucon."
        moeka "Aku takut kamu akan panik kalau tahu. Aku juga takut kalau nggak ada yang tahu."
    elif _return == "B":
        nar "Kau menerima dan berterima kasih tanpa bertanya. Moeka tersenyum, tampak lega karena satu urusan dianggap selesai."
        nar "Benda itu terasa seperti hadiah yang biasa sampai kau mengingat betapa keras ia mempertahankannya dahulu. Pertanyaan yang tidak diajukan sekarang akan tetap berada di antara kenanganmu tentang sore ini."
    else:
        nar "Kau menganggapnya kebiasaan lain yang akan dijelaskan nanti. Moeka melanjutkan pembagian dengan rapi, memberi setiap benda kepada orang yang diingat pernah menyukainya."
        nar "Ia menunjukkan betapa banyak ia memperhatikan hidup orang lain, sementara pergeseran dalam hidupnya sendiri berlalu tanpa ditanyakan."
    return

# ┌─ PANDUAN CERITA · Mo21 · Tertawa Terlalu Keras
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : gasshuku.
# │ INTI    : A bicara pelan / B ikut tertawa / C abaikan.
# │ AKHIRAN : tanda bahaya.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo21:
    call kk_scene_enter("moeka", "Kantin Pusat · Tertawa terlalu keras")
    nar "Tawa Moeka masih terdengar ketika orang lain sudah pindah topik. Ia menutup mulut, meminta maaf sambil tertawa lagi, lalu menawarkan permainan baru sebelum suasana sempat diam."
    moeka "Jangan berhenti gara-gara aku. Kalau masih ramai, kita masih punya malam yang bagus, kan?"
    call kk_family_menu("Mo21", ["Tarik ia bicara pelan, berdua.", "Ikut tertawa bersamanya.", "Abaikan."])
    if _return == "A":
        moeka "Kau menyadari tawaku aneh? ...Aku sudah tidak tahu cara tertawa yang biasa."
        nar "Kau mengajaknya ke tempat lebih tenang tanpa menyentuhnya mendadak. Ia berhenti menghibur dan menatap lantai, menanyakan apakah boleh duduk di sini sampai tak perlu lagi mengisi setiap jeda dengan sesuatu yang lucu."
    elif _return == "B":
        nar "Kau ikut tertawa dan menambah candaan. Moeka mengikuti, senang menemukan cara yang masih membuat orang ingin bersamanya. Setelahnya ia tidak punya tenaga untuk menyatakan betapa buruk rasa sepi yang datang ketika acara akhirnya bubar."
    else:
        nar "Kau mengalihkan perhatian ke percakapan lain. Dari sudut mata, tawa Moeka berhenti sekaligus ketika tak ada lagi yang melihat. Ia menunduk pada ponsel tanpa membuka percakapan."
    return

# ┌─ PANDUAN CERITA · Mo22 · Reito Menelepon
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : adiknya khawatir.
# │ INTI    : A datang / B kirim uang / C tidak.
# │ AKHIRAN : jendela #4.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo22:
    call kk_scene_enter("moeka", "Kantin Pusat · Reito menelepon")
    "Reito" "Moeka-nee nggak menjawab tiga hari. Terakhir bilang baik-baik saja, tapi kalau memang baik, biasanya dia yang terus bertanya aku sudah makan apa. Bisa lihat dia? Aku nggak tahu harus menghubungi siapa lagi."
    nar "Ia mencoba terdengar tenang, menanyakan alamat yang bahkan tak bisa ia datangi sendiri malam itu. Kekhawatirannya lebih besar daripada usianya."
    call kk_family_menu("Mo22", ["Datang menengok Moeka.", "Kirim uang untuk keluarganya.", "Tidak melakukan apa-apa."])
    if _return == "A":
        moeka "Reito meneleponmu? ...Dasar. Dia tidak perlu mengkhawatirkanku. ...Tapi kau datang."
        nar "Kau mengabari kedatanganmu dan memastikan keluarganya menerima kabar yang jujur. Moeka memandang ponsel lama sebelum menelepon adiknya."
        moeka "Aku belum baik. Tapi aku ditemani sekarang. Kamu boleh berhenti berjaga menunggu telepon, ya."
    elif _return == "B":
        nar "Kau mengirim bantuan uang. Kebutuhan rumah mendapat ruang bernapas, tetapi pertanyaan Reito tentang keberadaan kakaknya belum terjawab."
        nar "Moeka mengucapkan terima kasih melalui pesan. Kau belum mendengar suaranya, belum mengetahui apakah kata terima kasih itu satu-satunya kalimat yang masih mampu ia susun malam ini."
    else:
        nar "Kau tidak bertindak. Reito mengatakan akan mencoba menelepon lagi, suaranya makin kecil ketika kehabisan pertanyaan yang bisa diajukan kepadamu."
        nar "Sesudah panggilan berakhir, kekhawatiran itu kembali ke tangan seorang anak yang sudah mengatakan tidak sanggup menanggungnya sendirian."
    return

# ┌─ PANDUAN CERITA · Mo23 · Kontrak Kuga
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : kontrak modeling.
# │ INTI    : A tolak / B renegosiasi / C biarkan.
# │ AKHIRAN : stres bertambah/berkurang.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo23:
    call kk_scene_enter("moeka", "Kantin Pusat · Kontrak Kuga")
    nar "Kontrak Kuga menjanjikan pekerjaan jangka panjang. Moeka membaca baris pertama tiga kali, lalu menghitung penghasilan sebelum sampai pada syarat yang menentukan berapa banyak hidupnya harus diserahkan."
    moeka "Aku ingin punya bulan depan yang sudah bisa dihitung. Tapi kalau tanda tangan cuma karena capek takut, itu tetap keputusan yang akan harus kujalani. Tolong temani aku baca."
    call kk_family_menu("Mo23", ["Bantu ia menolak kontrak itu.", "Bantu ia merenegosiasi syaratnya.", "Biarkan ia menandatanganinya."])
    if _return == "A":
        moeka "Menolaknya berarti kehilangan uang itu... tapi kau benar. Ada harga yang terlalu mahal. Terima kasih."
        nar "Kau membantunya mengucapkan penolakan yang tidak meminta maaf atas setiap keberatan. Uang belum tersedia dari tempat lain, tetapi malam ini ia tidak harus menutup masalah dengan memberikan persetujuan yang tidak diinginkan."
    elif _return == "B":
        moeka "Renegosiasi? Aku bahkan tidak tahu boleh. ...Kalau kau temani, mungkin aku berani."
        nar "Kalian memeriksa bagian yang tidak dipahami dan mencari bantuan membaca ketentuannya. Moeka meminta waktu serta perubahan syarat, mengetahui bahwa jawaban Kuga terhadap keberatan juga bagian dari informasi tentang pekerjaan itu."
    else:
        nar "Kau membiarkannya menandatangani sebelum kelelahan dan ketakutannya sempat diberi ruang. Moeka tersenyum setelah pena diletakkan, mengucapkan bahwa sekarang setidaknya satu hal selesai."
        nar "Satu keputusan memang selesai. Tuntutan yang dibukanya baru mulai, dan tidak semuanya dapat ditolak dengan mudah setelah kebutuhan keluarga telanjur diletakkan di atas penghasilan tersebut."
    return

# ┌─ PANDUAN CERITA · Mo24 · Peragaan Terakhir
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia tampil.
# │ INTI    : A hadir / B tinggalkan / C bantu.
# │ AKHIRAN : reputasi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo24:
    call kk_scene_enter("moeka", "Kantin Pusat · Peragaan terakhir")
    nar "Label pada pakaian peragaan terakhir dijahit Moeka sendiri. Di belakang panggung ia memeriksa seluruh jahitan, lalu meminta orang lain memeriksa lagi karena tangannya mulai gemetar."
    moeka "Aku ingin bagian ini bagus karena aku memang suka membuatnya. Bukan cuma karena kalau gagal, semuanya selesai. Sulit sekali membedakan di kepala sekarang."
    call kk_family_menu("Mo24", ["Hadir untuk menontonnya.", "Tinggalkan acara itu.", "Bantu ia di belakang panggung."])
    if _return == "A":
        moeka "Kau datang menonton? ...Aku akan mencarimu dari panggung. Satu wajah yang kukenal sudah cukup."
        nar "Kau duduk di tempat yang disepakati dan tetap tinggal ketika pertunjukan selesai. Moeka melihatmu sesudah turun, lega karena tak harus mengejar perhatian yang hanya tersedia saat ia tampak bersinar."
    elif _return == "B":
        nar "Kau meninggalkan acara. Moeka sempat mencari tempatmu sebelum musik dimulai, lalu mengembalikan wajahnya ke depan."
        nar "Penonton tetap bertepuk tangan. Di belakang panggung, tepuk tangan itu belum tentu menjawab kebutuhan yang tak pernah ia tahu bagaimana meminta tanpa merasa kekanak-kanakan."
    else:
        moeka "Kau di backstage menemaniku? ...Tangan ini gemetar, tapi sekarang sedikit lebih tenang."
        nar "Kau menangani hal kecil yang dapat dibagi dan membiarkan keputusan desain tetap miliknya. Sebelum naik panggung ia menarik napas, menyebut satu bagian yang disukai dari karyanya sendiri. Kali ini yang akan ditampilkan tidak hanya tubuh yang diminta terus tersenyum."
    return

# ┌─ PANDUAN CERITA · Mo25 · Malam Tanpa Balasan
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : tiga pemicu bertemu: surat pencabutan beasiswa, kondisi ayah memburuk, dan orang yang ia andalkan tidak membalas.
# │ INTI    : (node keputusan / penutup — tak ada menu)
# │ AKHIRAN : — (kosong di katalog; bebas karang)
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo25:
    call kk_scene_enter("moeka", "Kantin Pusat · Malam tanpa balasan")
    python:
        _tertolong = (kk_has("moeka_ditemani_natal") or kk_has("moeka_intervensi_1")
                      or kk_has("sato_kyoko_terlibat") or kk_has("moeka_ayah_diketahui")
                      or sum(kk_has(f) for f in ("moeka_dikabari_natal","moeka_adik_dikenal",
                            "moeka_keluarga_diketahui","kuga_dihalangi","rina_sekutu",
                            "moeka_jalan_keluar","moeka_tanda_bahaya_dibaca",
                            "moeka_beasiswa_dibantu")) >= 2)
    if _tertolong:
        nar "Kabar ayah memburuk datang setelah surat tentang beasiswa. Moeka membuka percakapan yang biasa dijadikan tempat meminta tenang dan mendapati belum ada balasan. Untuk beberapa waktu semua jalan terlihat menyempit ke rasa takut yang sama."
        nar "Namun bantuan yang telah dibangun sebelumnya tidak hanya hidup dalam satu nomor. Ada orang yang mengetahui keadaannya, ada jalan menghubungi dukungan, dan malam itu seseorang berhasil menjangkaunya sebelum ia terus sendirian dalam krisis."
        moeka "Aku takut pada pikiranku sendiri. Tolong tetap bicara. Aku perlu bantuan, bukan cuma disuruh tidur."
        nar "Permintaan itu didengar. Pertolongan datang tanpa menjadikannya ujian apakah ia cukup mencintai keluarga untuk bertahan. Ia ditemani melewati malam, lalu diarahkan pada perawatan dan dukungan berikutnya."
        moeka "Besok masalahnya masih ada, ya. Aku tahu. Tapi aku belum sanggup memikirkan besok sekaligus sekarang."
        nar "Tidak seorang pun memintanya menyelesaikan seluruh masa depan sebelum boleh ditolong malam ini."
        $ kk_record_choice("Mo25", "A")
    else:
        nar "Surat beasiswa, kabar ayah, dan kesendirian bertemu pada malam yang sudah terlalu berat bagi Moeka. Pertolongan tidak berhasil menjangkaunya sebelum krisis itu berakhir dengan kematian. Tidak ada satu pesan yang sendirian dapat menjelaskan seluruh kehilangan tersebut."
        nar "Kabar datang keesokan hari. Ryena menelepon, mengucapkan nama Moeka dua kali sebelum sanggup menyelesaikan kalimat. Di kampus jadwal masih menuliskan giliran presentasinya. Orang-orang berulang kali menanyakan siapa yang sudah mengetahui, seolah jawaban itu dapat membuat peristiwa menjadi lebih mungkin dipercaya."
        nar "Yaeka menerima kabar di rumah. Adik-adiknya masih harus diberi tahu. Ada pekerjaan yang akan tetap menunggu, kain yang belum dipotong, dan hal kecil yang sekarang memerlukan seseorang mengambilnya dari kamar tanpa pemiliknya berkata tunggu, yang itu jangan dibuang."
        nar "Kau membuka percakapan lama dan menemukan banyak kalimat biasa. Penyesalan mencoba mengubah semuanya menjadi petunjuk yang seharusnya jelas. Ia tidak memberimu cara memutar waktu, hanya beban untuk mengakui bahwa seseorang jauh lebih luas daripada tanda-tanda yang sempat atau gagal kaukenali."
        nar "Sistem tidak mengatakan apa pun. Keheningan itu tidak mengecilkan yang terjadi."
        $ kk_record_choice("Mo25", "B")
    return

init 1 python:
    _hook("Mo13-A", lambda: (kk_rel("moeka","trust",5), kk_flag("moeka_dibela_rumor")))
    _hook("Mo13-B", lambda: kk_adj("stres_moeka",8))
    _hook("Mo13-C", lambda: (kk_adj("stres_moeka",12), kk_flag("moeka_dimanfaatkan")))
    _hook("Mo14-A", lambda: (kk_rel("moeka","intim",4), kk_flag("topeng_moeka_ditanya")))
    _hook("Mo14-B", lambda: (kk_moeka_stage(2), kk_adj("stres_moeka",6)))
    _hook("Mo14-C", lambda: (kk_moeka_stage(2), kk_adj("stres_moeka",10)))
    _hook("Mo15-A", lambda: (kk_rel("moeka","trust",5), kk_flag("moeka_jendela_2")))
    _hook("Mo15-B", lambda: (kk_adj("stres_moeka",-12), kk_flag("moeka_jalan_keluar")))
    _hook("Mo15-C", lambda: (kk_adj("stres_moeka",15), kk_flag("beasiswa_terancam")))
    _hook("Mo16-A", lambda: (kk_rel("moeka","trust",5), kk_adj("stres_moeka",-6)))
    _hook("Mo16-B", lambda: (kk_adj("stres_moeka",-10), kk_flag("moeka_kerja_aman")))
    _hook("Mo16-C", lambda: (kk_adj("stres_moeka",12), kk_rel("moeka","trust",-6)))
    _hook("Mo17-A", lambda: (kk_rel("moeka","intim",5), kk_flag("moeka_dijemput_isolasi")))
    _hook("Mo17-B", lambda: kk_moeka_stage(3))
    _hook("Mo17-C", lambda: (kk_moeka_stage(3), kk_adj("stres_moeka",10)))
    _hook("Mo18-A", lambda: (kk_flag("rina_sekutu"), kk_rel("moeka","trust",4)))
    _hook("Mo18-B", lambda: kk_flag("rina_lawan"))
    _hook("Mo18-C", lambda: kk_rel("moeka","trust",-2))
    _hook("Mo19-A", lambda: (kk_rel("moeka","trust",6), kk_flag("moeka_jendela_3"), kk_flag("moeka_tanda_dibaca")))
    _hook("Mo19-B", lambda: kk_moeka_stage(4))
    _hook("Mo19-C", lambda: (kk_moeka_stage(4), kk_adj("stres_moeka",15)))
    _hook("Mo21-A", lambda: (kk_rel("moeka","intim",4), kk_flag("moeka_tawa_ditahan")))
    _hook("Mo21-B", lambda: kk_adj("stres_moeka",6))
    _hook("Mo21-C", lambda: kk_adj("stres_moeka",10))
    _hook("Mo22-A", lambda: (kk_rel("moeka","intim",6), kk_flag("moeka_jendela_4"), kk_flag("moeka_ditengok")))
    _hook("Mo22-B", lambda: kk_adj("stres_moeka",-8))
    _hook("Mo22-C", lambda: (kk_adj("stres_moeka",15), kk_flag("moeka_ren_diabaikan")))
    _hook("Mo23-A", lambda: (kk_adj("stres_moeka",-10), kk_flag("kuga_ditolak")))
    _hook("Mo23-B", lambda: (kk_adj("stres_moeka",-5), kk_flag("kuga_renegosiasi")))
    _hook("Mo23-C", lambda: (kk_adj("stres_moeka",15), kk_flag("kuga_kontrak_terikat")))
    _hook("Mo24-A", lambda: kk_rel("moeka","aff",5))
    _hook("Mo24-B", lambda: kk_rel("moeka","aff",-4))
    _hook("Mo24-C", lambda: (kk_rel("moeka","intim",5), kk_flag("moeka_backstage_ditemani")))
    _hook("Mo25-A", lambda: kk_flag("moeka_selamat"))
    _hook("Mo25-B", lambda: kk_flag("moeka_kehilangan"))
