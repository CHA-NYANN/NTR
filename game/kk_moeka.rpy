# Arc Moeka (Mo03-Mo12, Mo26): wakil kelas dari keluarga miskin dengan tiga adik
# dan ayah sakit; tekanan finansial/akademik, gerbang awal fotografer Kuga, dan
# jendela intervensi menjelang krisis. Ditulis sebagai KARAKTER dan KONSEKUENSI;
# eksploitasi/krisis hanya akibatnya yang dicatat, tanpa metode. Penempatan di
# Kantin Pusat adalah prototipe reachability (🟡); locale naratif ada di dialog.
# Efek menggerakkan stres_moeka, stage[moeka], beban_keluarga. Event_Moeka.

init 1 python:
    def kk_moeka_burden(delta):
        pts.setdefault("beban_keluarga", 0)
        kk_adj("beban_keluarga", delta)
    def kk_moeka_stage(n):
        kk_stage("moeka", max(n, stage.get("moeka", 0)))

# ┌─ PANDUAN CERITA · Mo03 · Janji yang Terlupa
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia lupa janji dengan pemain.
# │ INTI    : A marah / B maklum / C bantu mengatur jadwal.
# │ AKHIRAN : Trust; B/C mengurangi stres.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo03:
    call kk_scene_enter("moeka", "Kantin Pusat · Janji terlupa")
    if kk_host == "chiasa":
        nar "Hujan gerimis pertengahan Juni menempel di kaca jendela besar Kantin Pusat yang mulai lengang selepas jam makan siang. Bau samar kuah udon dan kopi mesin penjual masih menggantung di udara, sementara di luar, payung-payung mahasiswa melintas pelan di halaman yang basah."
        nar "Di atas meja kayu di hadapanmu, segelas teh hangat yang kaupesan hampir satu jam lalu sudah lama kehilangan uapnya. Ketika jari-jarimu menyentuh dinding gelasnya, yang tersisa hanyalah dingin yang lembap—persis seperti layar ponselmu yang sejak tadi tetap sunyi tanpa satu pun balasan pesan."
        nar "Kau menghela napas pelan, melirik jam dinding kantin yang jarum panjangnya hampir genap berputar satu kali sejak jam janji kalian. Baru saja kau merapikan tali tas dan berniat bangkit pulang, suara pintu kaca kantin yang didorong tergesa hingga berderit membuatmu menoleh."
        nar "Kohinata Moeka berlari kecil menyusuri sela-sela deretan meja dengan napas memburu. Rambut merah muda panjangnya yang bergelombang agak lembap di ujung terkena tempias hujan, tali kartu panitia masih melingkar miring di lehernya, dan di tepi bawah kardigannya yang berhias renda jahit tangan, sebuah peniti perak kecil tampak dijepit seadanya untuk menahan keliman kain yang terlepas."
        nar "Bahkan sebelum ia sempat menarik kursi di hadapanmu, ponsel di dalam saku kardigannya sudah kembali bergetar nyaring dengan deretan notifikasi masuk. Ia merogoh saku dengan satu tangan, mematikan getarannya cepat-cepat tanpa sempat membaca, lalu memandangmu dengan wajah penuh rasa bersalah."
        moeka "Chimian—! Aduh, maaf banget! Serius, aku benar-benar minta maaf!"
        nar "Panggilan 'Chimian' yang meluncur begitu ringan dari bibirnya masih selalu membuatmu tertegun sepersekian detik—rasanya aneh setiap kali harus menanggapi julukan akrab yang sebenarnya bukan milikmu, melainkan milik tubuh ini."
        nar "Moeka menjatuhkan tas kanvas beratnya yang penuh gulungan kain dan map panitia ke kursi sebelah, lalu menangkupkan kedua tangan di depan wajah sambil menarik napas pendek-pendek."
        moeka "Rapat panitia tadi molor hampir satu jam gara-gara bagian panggung mendadak ganti daftar alat, terus pas aku baru lari keluar ruang rapat, adikku mendadak telepon dari rumah—dan aku baru ingat janji kita tepat di menit yang paling nggak berguna."
        nar "Matanya yang biru cerah melirik gelas teh di atas meja di depanmu, lalu bahunya sedikit turun. Untuk sejenak, keceriaan yang biasanya menempel seperti cat terang di wajahnya tampak memudar."
        moeka "Kamu sudah menunggu lama banget, ya... aku nggak bakal bohong bilang cuma sebentar kalau gelasmu saja sudah dingin begitu. Ponselku juga tadi di-silent di dalam tas pas rapat, jadi aku sama sekali nggak sempat mengabari. Maaf banget, Chimian."
    else:
        nar "Hujan gerimis pertengahan Juni menempel tipis di kaca jendela besar Kantin Pusat yang mulai lengang selepas jam makan siang. Suara piring dicuci dari balik konter dapur terdengar samar, bercampur bunyi rintik air yang jatuh terus-menerus di halaman luar."
        nar "Di atas meja kayu di hadapanmu, segelas kopi hitam dari mesin penjual yang kaubeli hampir satu jam lalu sudah lama kehilangan hangatnya; dinding gelasnya dingin dan mengembun tipis, meninggalkan lingkaran lembap di permukaan meja."
        nar "Kau menyandarkan punggung ke sandaran kursi sambil memutar ponsel pelan di atas meja. Layarnya tetap sunyi tanpa satu pun balasan sejak jam janji kalian lewat. Baru saja kau menghela napas, menyelipkan ponsel ke saku celana, dan bersiap beranjak pergi, daun pintu kaca kantin didorong tergesa hingga berderit nyaring."
        nar "Kohinata Moeka berlari kecil menyusuri sela-sela deretan kursi kosong dengan napas memburu. Rambut merah muda panjangnya yang bergelombang agak lembap di ujung terkena tempias hujan, tali kartu panitia masih melingkar miring di lehernya, dan di tepi bawah kardigannya yang berhias renda jahit tangan, sebuah peniti perak kecil tampak dijepit darurat untuk menahan keliman yang terlepas."
        nar "Biasanya ia selalu terlihat seperti orang yang paling santai di satu kampus—tetapi hari ini, bahkan sebelum ia sempat menarik kursi di hadapanmu, ponsel di saku kardigannya sudah kembali bergetar keras oleh rentetan notifikasi masuk. Ia merogoh saku cepat-cepat dengan satu tangan, mematikan getarannya tanpa sempat membaca, lalu menatapmu dengan wajah penuh rasa bersalah."
        moeka "Yutayuta—! Aduh, maaf banget! Serius, aku benar-benar minta maaf!"
        nar "Mendengar panggilan 'Yutayuta' dilontarkan seakrab itu di tengah kantin masih selalu menimbulkan jeda ganjil sepersekian detik di kepalamu—rasanya aneh setiap kali harus menanggapi julukan konyol yang sebenarnya ditujukan untuk Kisaragi Yutaka, bukan dirimu."
        nar "Ia menjatuhkan tas kanvas beratnya yang penuh gulungan kain dan map kepanitiaan ke kursi sebelah, lalu menangkupkan kedua tangan di depan wajah sambil menarik napas pendek-pendek."
        moeka "Rapat panitia tadi molor hampir satu jam gara-gara bagian panggung mendadak ganti daftar alat, terus pas aku baru lari keluar ruang rapat, adikku telepon dari rumah—dan aku baru ingat janji kita tepat di menit yang paling nggak berguna."
        nar "Matanya yang biru cerah jatuh ke gelas kopi yang sudah dingin di depanmu, lalu bahunya sedikit turun. Untuk sesaat, keceriaan terang yang biasanya selalu menempel di wajahnya tampak menipis."
        moeka "Kamu sudah menunggu lama banget, ya... aku nggak mau bohong bilang cuma sebentar kalau jelas-jelas bukan. Ponselku tadi di-silent di dalam tas pas rapat, jadi aku sama sekali nggak sempat kirim kabar. Maaf, Yutayuta."
    call kk_family_menu("Mo03", ["\"Aku sudah menunggu hampir sejam sampai minumanku dingin.\"", "\"Tidak apa-apa, tarik napas dulu saja.\"", "Tawarkan bantuan untuk menyusun ulang jadwal di ponselnya."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau tidak memaksakan senyum maklum. Kau mendorong pelan gelas teh yang sudah dingin itu beberapa sentimeter ke tengah meja, lalu menatap wajah Moeka dengan nada suara yang tenang namun tidak menyembunyikan kekesalanmu."
            chiasa "Aku sudah menunggu hampir satu jam di sini sampai minumanku dingin, Moemoe-senpai. Aku bahkan sudah hampir pulang barusan."
            nar "Bahu Moeka langsung turun. Senyum panik yang sempat hendak ia pasang untuk mencairkan suasana mendadak padam."
            chiasa "Kalau memang rapatnya molor atau ada urusan mendadak dari rumah, aku bisa mengerti. Tapi paling tidak kirim satu pesan singkat supaya aku tidak duduk menunggu di sini tanpa kabar sama sekali."
            nar "Moeka menarik kursi di seberangmu lalu duduk perlahan, kedua tangannya meremas tali tas kanvasnya di atas pangkuan. Ia menunduk menatap permukaan meja kayu tanpa menyela sepatah kata pun."
            moeka "...Kau benar, Chimian. Aku nggak punya alasan buat membela diri. Seharusnya aku kirim pesan begitu tahu rapatnya nggak bakal selesai tepat waktu. Aku pantas dimarahi. Maaf sekali lagi."
            nar "Keheningan yang berat dan canggung turun di antara kalian selama beberapa detik. Suara gerimis di luar kaca kantin terdengar lebih nyaring. Tepat saat kau mengira ia akan diam saja atau meminta menjadwal ulang di hari lain, Moeka mendadak mengangkat wajahnya dan memasang senyum lebar yang terasa dua tingkat terlalu cerah."
            moeka "Ah—tapi dengar dulu deh, Chimian! Tadi di ruang rapat sempat ada kejadian konyol banget lho, proyektornya mati tepat waktu ketua lagi presentasi serius terus gambarnya malah kepantul miring ke papan tulis! Semua orang langsung panik kayak dikejar hantu, ahaha!"
            chiasa "Moemoe-senpai..."
            moeka "Oh iya! Di konter depan katanya hari ini ada menu puding karamel baru yang cuma keluar sore hari. Biar aku yang traktir buat tebusan ya—tunggu sebentar, aku lari beli sekarang biar kamu nggak bete lagi!"
            nar "Ia sudah setengah bangkit sambil tertawa sedikit terlalu keras, bicara terlalu cepat dari satu topik ke topik lain tanpa jeda napas."
            nar "Melihatnya begitu, kau sadar ada sesuatu yang janggal di balik keceriaannya yang mendadak meluap—seolah di dalam kepalanya, satu jam waktumu yang hilang adalah utang yang harus segera ia lunasi dengan berusaha menjadi dua kali lebih ramai dan menyenangkan."
        else:
            nar "Kau tidak repot-repot memasang senyum maklum atau bercanda untuk meringankan suasana. Kau mengetuk pelan dinding gelas kopi dingin di hadapanmu dengan punggung jari, lalu menatap Moeka lurus-lurus dengan nada datar yang blak-blakan."
            yutaka "Aku sudah duduk di sini hampir sejam sampai kopiku dingin, Kohinata. Aku bahkan sudah hampir berdiri dan pulang barusan."
            nar "Bahu Moeka langsung melorot. Senyum bersalah yang tadinya masih ia pertahankan ikut menghilang tanpa sisa."
            yutaka "Rapat molor atau ada telepon mendadak dari rumah itu hal wajar—aku nggak mempermasalahkan itu. Tapi tinggal kirim satu baris pesan kan nggak sampai sepuluh detik. Jangan biarkan orang duduk menunggu tanpa kabar begitu."
            nar "Moeka menarik kursi di seberangmu dan duduk perlahan tanpa sedikit pun mencoba memotong atau membela diri. Kedua tangannya meremas tali tas kanvas di atas lutut, kepalanya tertunduk menatap permukaan meja."
            moeka "...Kau benar, Yutayuta. Aku memang salah total. Seharusnya aku keluar sebentar buat kirim pesan begitu tahu rapatnya molor. Nggak ada alasan buat mengelak, aku pantas dimarahi. Maaf sekali lagi."
            nar "Keheningan yang berat dan agak kikuk sempat menggantung di atas meja selama beberapa detik. Suara hujan di kaca kantin terdengar lebih jelas. Namun tepat saat kau mengira pembicaraan akan masuk ke urusan utama, Moeka mendadak menegakkan punggung dan memasang senyum lebar yang terasa dua tingkat terlalu terang."
            moeka "Eh—tapi dengar dulu deh, Yutayuta! Tadi di ruang rapat ada kejadian konyol banget tahu nggak, proyektornya mendadak mati pas ketua lagi semangat presentasi terus gambarnya malah kepantul miring ke kaca jendela! Semua anak panitia langsung heboh kayak kebakaran jenggot, ahaha!"
            yutaka "Kohinata..."
            moeka "Oh iya! Di konter depan hari ini ada kopi seduh baru sama roti manis yang baru keluar oven! Biar aku yang traktir buat ganti kopimu yang dingin ya—tunggu sebentar, aku lari beli sekarang biar suasana hatimu balik lagi!"
            nar "Ia sudah setengah bangkit dari kursi, bicara terlalu cepat dari satu topik ke topik lain sambil tertawa sedikit terlalu keras untuk ruangan yang lengang."
            nar "Melihatnya mendadak memaksa suasana jadi seramai itu, kau menangkap sesuatu yang ganjil di balik keceriaannya—seolah di dalam kepalanya, satu jam waktumu yang hilang adalah utang yang harus segera ia lunasi dengan berusaha menjadi dua kali lebih berisik dan menyenangkan."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kau memperhatikan ujung jarinya yang masih sedikit gemetar menahan ponsel, peniti darurat yang menjepit keliman kardigannya, dan napasnya yang belum sepenuhnya teratur. Alih-alih memperpanjang soal waktu yang terbuang, kau menghela napas pelan lalu mendorong tisu kering di atas meja ke arahnya."
            chiasa "Terlambat hampir sejam tanpa kabar memang merepotkan, Moemoe-senpai. Tapi kelihatan sekali hari ini Senpai sedang kewalahan—rambutmu saja masih basah kena hujan. Jadi jangan dulu panik. Duduk dan tarik napas dulu saja."
            nar "Moeka mengerjap terkejut. Ekspresi siaga yang tadinya siap menerima omelan atau bersiap membalas dengan candaan panik perlahan luruh dari wajahnya."
            moeka "Eh...? Chimian nggak marah?"
            chiasa "Kesal sedikit sih iya, soalnya tehku keburu dingin. Tapi kalau aku langsung marah sekarang, Senpai kelihatannya malah makin pusing. Lain kali kalau mendadak terhambat, cukup kirim satu kata saja biar aku tahu harus menunggu atau pulang dulu. Itu saja."
            nar "Moeka terdiam sejenak sambil menerima tisu darimu dan menyeka ujung rambutnya yang basah. Ketika ia menatapmu lagi, senyum cerianya yang biasanya seperti topeng otomatis mendadak hilang—digantikan tatapan lega yang terasa jauh lebih nyata."
            moeka "...Terima kasih banyak, Chimian. Serius. Rasanya sejak pagi tadi akhirnya ada satu orang yang nggak langsung menuntut sesuatu dariku."
            nar "Ia menarik kursi, duduk, lalu menyandarkan punggungnya penuh ke sandaran kayu. Untuk pertama kalinya sejak memasuki kantin, ia memejamkan mata sejenak dan mengembuskan napas panjang yang jujur."
            moeka "Dari pagi semua orang nanya berkas ini sudah beres belum, kain ini jadi dipakai nggak, terus rumah juga telepon... kepalaku rasanya baru berhenti berputar barusan."
            chiasa "Kalau begitu tidak usah buru-buru bahas urusan kita dulu."
            moeka "...Boleh nggak, Chimian, kasih aku waktu lima menit saja buat duduk diam dan minum air sebelum kita mulai? Lima menit saja, janji."
            chiasa "Tentu. Ambil waktumu saja, Senpai."
            nar "Moeka mengangguk kecil lalu meneguk air dari botol minum yang ia keluarkan dari tasnya. Untuk lima menit penuh di tengah suara gerimis yang mengetuk kaca kantin, tidak ada tawa yang dipaksakan maupun obrolan berisik—hanya keheningan tenang yang memberi ruang bagi kelelahan yang akhirnya boleh diakui."
        else:
            nar "Kau melirik peniti kecil yang menahan keliman kardigannya, tali kartu panitia yang masih miring di bahunya, dan jari-jarinya yang masih sedikit gemetar menggenggam ponsel. Alih-alih menyindir atau membalas dengan nada kesal, kau menghela napas pelan lalu menggeser kursi di seberangmu sedikit dengan kaki agar ia bisa langsung duduk."
            yutaka "Duduk dulu, Kohinata. Terlambat sejam tanpa kabar memang bikin repot, tapi mukamu sudah kayak orang habis lari maraton dua kali. Tarik napas dulu saja."
            nar "Moeka mengerjap kaget, jelas tidak menduga nada tenang tanpa sindiran itu darimu. Bahunya yang sejak tadi menegang bersiap menerima omelan atau ejekan perlahan meluruh."
            moeka "Eh...? Yutayuta nggak marah? Nggak mau ngejek aku dulu?"
            yutaka "Kesal sedikit sih iya, kopiku keburu dingin. Tapi kalau sekarang aku ikut ngoceh, kau kelihatannya malah makin pusing. Lain kali tinggal kirim satu kata kalau molor—'telat' atau 'batal'—supaya jelas. Nggak perlu sampai panik kayak dunia mau runtuh."
            nar "Tawa gugup yang sudah hampir keluar dari bibirnya mendadak berhenti. Ia duduk perlahan, menurunkan tas kanvas beratnya ke lantai, lalu menyandarkan punggungnya penuh ke sandaran kayu."
            moeka "...Terima kasih, Yutayuta. Serius. Sejak pagi tadi akhirnya ada satu orang yang nggak langsung menuntut sesuatu dariku."
            nar "Ia memejamkan mata sejenak sambil mengembuskan napas panjang yang jujur dan berat—sama sekali jauh dari citra gadis paling ceria dan tak pernah lelah yang biasa ia tampilkan di depan anak-anak kampus."
            moeka "Dari pagi semua orang ngejar berkas panitia, jadwal studio belum beres, terus rumah juga menelepon... kepalaku rasanya baru berhenti berdengung barusan."
            yutaka "Ya sudah, nggak usah langsung bahas urusan tadi dulu."
            moeka "...Boleh minta lima menit saja buat duduk diam dan minum air sebelum kita mulai? Lima menit saja, janji."
            yutaka "Ambil saja. Aku juga nggak ke mana-mana."
            nar "Ia mengangguk pelan, mengeluarkan botol air dari tasnya, lalu meneguknya tanpa terburu-buru. Untuk lima menit penuh di tengah suara gerimis yang mengetuk jendela kantin, tidak ada candaan berisik maupun tawa yang dipaksakan—hanya dua orang seangkatan yang duduk tenang memberi ruang bagi kelelahan yang akhirnya boleh berhenti berpura-pura."
    else:
        if kk_host == "chiasa":
            nar "Kau menggeser gelas teh dinginmu ke pinggir meja, lalu mengetuk perlahan permukaan meja kayu sambil menunjuk ponsel yang baru saja berhenti bergetar di tangan Moeka."
            chiasa "Duduk dulu, Moemoe-senpai. Kalau jadwalnya sampai bertabrakan dan bikin lupa janji begini terus, nanti Senpai sendiri yang paling repot. Coba buka kalender di ponselmu—biar kubantu merapikannya sekarang."
            nar "Moeka tertegun sejenak menatapmu. Matanya yang biru cerah tampak mengerjap beberapa kali, nyaris berkaca-kaca karena lega yang tidak terduga."
            moeka "Eh—Chimian beneran mau bantu mengatur ini semua? Nggak merepotkan?"
            chiasa "Daripada kita sama-sama buang waktu lain kali, lebih bagus dibereskan sekarang mumpung kita sudah duduk di sini."
            moeka "...Astaga, aku hampir lupa rasanya ditolong duluan tanpa harus minta."
            nar "Ia menggeser kursinya lebih dekat ke sampingmu, membuka kunci layar ponselnya, lalu menyerahkannya agar kalian berdua bisa melihat tampilan kalendernya bersama."
            nar "Begitu layar itu terlihat, kau langsung mengerti mengapa ia begitu kewalahan. Blok-blok warna jadwal memenuhi hampir setiap hari: ada dua rapat kepanitiaan yang bertumpuk persis di jam yang sama minggu depan, satu shift kerja paruh waktu sore yang terlalu mepet dengan jam kelas, serta catatan tugas studio tanpa tanggal tenggat yang hanya ditulis sebagai 'minggu ini'."
            chiasa "Lihat yang hari Rabu jam empat ini, Senpai. Rapat dekorasi sama rapat anggaran ada di jam yang persis sama—Senpai beneran wajib hadir di dua-duanya?"
            moeka "Aduh, aku bahkan lupa kalau yang rapat anggaran digeser ke hari Rabu! Hmm... sebenarnya yang rapat dekorasi kan sudah ada Rina di sana. Catatan bagianku bisa kutitipkan ke Rina dulu, jadi aku cukup datang ke rapat anggaran."
            chiasa "Oke, yang dekorasi kuganti jadi pengingat titip catatan ke Rina hari Selasa malam. Terus tugas studio ini tenggat aslinya hari apa?"
            moeka "Jumat sore... kalau kutulis Kamis malam saja gimana biar aku nggak kepepet di hari H?"
            nar "Selama lima belas menit berikutnya, kalian berdua menyusun ulang urutan prioritas, memindahkan agenda yang bertumpuk, dan menyalakan pengingat setengah jam sebelum tiap jadwal penting. Kau membantu mencatat dan merapikan, tetapi selalu membiarkan Moeka sendiri yang memutuskan mana yang bisa ia tolak atau geser."
            nar "Ketika kalender itu akhirnya tersusun rapi, Moeka menyandarkan dagunya di telapak tangan sambil menatap layar ponselnya dengan napas lega."
            moeka "Fiuh... baru kali ini layar kalenderku kelihatan kayak jadwal manusia normal. Makasih banget ya, Chimian. Kalau nanti aku salah jadwal lagi, ingatkan saja—tapi jangan sampai kamu juga ikut repot hidup di dalam ponselku, ya."
            chiasa "Tenang saja, aku cuma mengingatkan kalau sudah kelihatan mulai kacau."
            nar "Ia tersenyum hangat sambil menaruh ponselnya di atas meja. Bahunya tampak jauh lebih ringan daripada saat ia berlari masuk pintu kantin tadi, dan sisa pertemuan kalian berjalan tanpa lagi dikejar rasa bersalah."
        else:
            nar "Kau menggeser gelas kopi dinginmu ke tepi meja, lalu mencondongkan badan sedikit sambil menunjuk ponsel yang baru saja berhenti bergetar di tangan Moeka."
            yutaka "Duduk dulu, Kohinata. Kalau jadwalmu sampai tabrakan dan bikin lupa janji begini terus, minggu depan kau bakal tumbang duluan. Sini, buka kalender di ponselmu—kita bereskan sekarang mumpung sama-sama sudah duduk di sini."
            nar "Moeka mengerjap tertegun. Sejenak, senyum santai yang biasa ia pasang menghilang, digantikan tatapan lega yang nyaris membuatnya tak percaya."
            moeka "Serius, Yutayuta mau bantu mengatur ini semua? Nggak ngerepotin?"
            yutaka "Lebih repot kalau lain kali aku nunggu sejam lagi gara-gara jadwalku ketindih rapatmu. Taruh saja ponselnya di tengah meja."
            moeka "...Astaga, aku hampir lupa rasanya ditolong duluan tanpa harus minta."
            nar "Ia menarik kursi, duduk agak condong ke sampingmu, lalu membuka aplikasi kalendernya di atas meja agar kalian berdua bisa melihatnya bersama."
            nar "Begitu layar itu terbuka, kau langsung melihat akar kekacauannya: blok-blok agenda menumpuk tanpa jeda—ada dua rapat panitia yang dipasang di jam persis sama pada hari Rabu, satu shift kerja paruh waktu yang terlalu mepet dengan kelas sore, dan satu catatan tugas studio yang bahkan tidak diberi tanggal tenggat."
            yutaka "Yang Rabu jam empat ini jelas mustahil kau datangi dua-duanya. Mana yang benar-benar butuh kau hadir, mana yang bisa dilepas?"
            moeka "Aduh, aku lupa kalau rapat anggaran digeser ke Rabu! Hmm... yang rapat dekorasi sebenarnya sudah ada Rina di sana. Catatanku bisa kutitipkan ke Rina saja Selasa malam, jadi aku cukup datang ke rapat anggaran."
            yutaka "Oke, yang itu kubuat jadi pengingat titip catatan ke Rina. Terus tugas studio yang cuma ditulis 'minggu ini' tenggat aslinya kapan?"
            moeka "Jumat sore. Tulis Kamis malam saja deh biar aku nggak keteteran di menit terakhir."
            nar "Selama lima belas menit berikutnya, kau membantu menuliskan ulang pengingat setengah jam sebelum tiap agenda dan merapikan jadwal yang bertumpuk tanpa mengambil alih seluruh harinya—setiap kali ada yang harus ditolak atau digeser, kau membiarkan Moeka sendiri yang memutuskan."
            nar "Begitu kalendernya akhirnya terlihat punya ruang bernapas, Moeka mengembuskan napas panjang sambil menopang dagu menatap layar ponselnya."
            moeka "Wah... baru kali ini jadwalku kelihatan bisa dijalani manusia normal. Makasih banyak ya, Yutayuta. Kalau nanti aku salah jadwal lagi, ingatkan saja—tapi jangan sampai kamu yang harus hidup di dalam ponselku."
            yutaka "Tenang saja, aku nggak serajin itu. Yang penting lain kali jangan lupa ngabarin lagi."
            nar "Ia tertawa pelan—kali ini tawa yang ringan, hangat, dan tidak dibuat-buat—dengan bahu yang tampak jauh lebih santai daripada saat ia berlari masuk pintu kantin tadi."
    return

# ┌─ PANDUAN CERITA · Mo04 · Pingsan Karena Lupa Makan
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : di vila.
# │ INTI    : A rawat / B panggil Miyuki / C abaikan.
# │ AKHIRAN : intimasi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo04:
    call kk_scene_enter("moeka", "Dapur vila · Pingsan")
    nar "Moeka berhenti bicara di tengah lelucon, meraih tepi meja, lalu jatuh sebelum selesai mengatakan hanya pusing. Makanan yang sejak siang ia tawarkan kepada semua orang ternyata belum sempat disentuhnya sendiri."
    nar "Belakangan ia mengaku mengurangi makan agar uang cukup dikirim ke rumah. Pengakuan itu disertai senyum malu, seolah sedang membahas siasat hemat yang sedikit kelewatan."
    call kk_family_menu("Mo04", ["Rawat ia sendiri sampai pulih.", "Panggil Miyuki untuk memeriksanya.", "Abaikan; itu bukan urusanmu."])
    if _return == "A":
        moeka "Kau menjagaku? ...Jangan bilang siapa-siapa soal kenapa aku tidak makan. Tolong."
        nar "Kau memastikan ia mendapat bantuan yang diperlukan dan menemaninya sampai keadaan lebih stabil. Saat ia mulai menawarkan kembali membantu dapur, kau mengingatkan bahwa malam ini ia juga orang yang perlu diperhatikan."
        moeka "Aku takut kalau bilang alasannya, orang berhenti percaya aku bisa mengurus diri. Tapi ternyata aku memang belum mengurus yang ini dengan benar."
    elif _return == "B":
        nar "Kau memanggil Miyuki, yang segera membantu menilai kebutuhan pertolongan berikutnya. Ia tidak membiarkan status mahasiswanya menjadi alasan menunda bantuan jika keadaan membutuhkannya."
        moeka "Aku tahu kamu masih belajar. Maaf, aku tadi bercanda karena malu. Aku sebenarnya senang ada yang datang."
    else:
        nar "Kau tidak ikut menolong. Orang lain akhirnya mendekat, sementara Moeka mulai sadar dan buru-buru meminta maaf atas keributan yang dibuat tubuhnya."
        nar "Setelahnya ia merapikan rambut dan mencoba kembali tersenyum. Di dekatmu ia kini lebih cepat mengatakan sudah makan, menutup persoalan sebelum kau sempat bertanya."
    return

# ┌─ PANDUAN CERITA · Mo05 · Kabar dari Rumah
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ibu menelepon.
# │ INTI    : A dengarkan / B alihkan / C tanya langsung.
# │ AKHIRAN : membuka masalah keluarga.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo05:
    call kk_scene_enter("moeka", "Kantin Pusat · Kabar dari rumah")
    nar "Aya menelepon ketika Moeka sedang memilih kain untuk tugas. Tangannya berhenti pada warna cerah yang baru dipuji, lalu pindah memegang tas seolah mendadak harus bersiap pulang."
    moeka "Iya, Bu. Aku dengar. Jangan bilang ke adik-adik aku panik, ya. Aku pikirkan dulu."
    nar "Setelah panggilan selesai, ia menatap kain yang masih di tangan seakan lupa tadi hendak membuat apa."
    call kk_family_menu("Mo05", ["Dengarkan kalau ia mau cerita.", "Alihkan agar ia tak perlu menjelaskan.", "Tanya langsung ada apa."])
    if _return == "A":
        moeka "Ayahku... kondisinya tidak membaik. Dan biaya terus jalan. ...Maaf, kau tidak perlu dengar ini."
        nar "Kau menunggu setelah kalimat terakhir, memberi kesempatan ia membatalkan permintaan maafnya sendiri. Moeka akhirnya bercerita tentang tiga adik, pekerjaan ibunya, dan uang yang selalu terasa sudah punya tujuan sebelum diterima."
    elif _return == "B":
        moeka "...Terima kasih sudah tidak bertanya. Kadang itu yang kubutuhkan."
        nar "Kau mengalihkan pembicaraan tanpa memaksanya tampak ceria. Beberapa menit kemudian ia kembali memilih kain, kali ini meminta pendapatmu sungguhan. Masalahnya belum hilang, tetapi ia mendapat jeda yang tidak harus dibayar dengan penjelasan."
    else:
        moeka "Kau mau tahu? ...Baik. Mungkin lebih ringan kalau satu orang tahu."
        nar "Ia bercerita lebih jauh daripada rencana awal, sampai angka dan kebutuhan keluarganya memenuhi percakapan. Mendengarnya membuatmu memahami mengapa tawaran kerja yang tampak buruk dari luar tetap dapat terlihat seperti pintu baginya."
    return

# ┌─ PANDUAN CERITA · Mo06 · Kuga Renji: Tawaran Foto
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : fotografer menawarkan pekerjaan modeling.
# │ INTI    : A dukung / B halangi / C ikut menemani.
# │ AKHIRAN : gerbang awal Kuga.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo06:
    call kk_scene_enter("moeka", "Kantin Pusat · Tawaran Kuga")
    nar "Kuga Renji memuji pakaian hasil ubahan Moeka sebelum menawarkan sesi foto. Ia membicarakan bayaran lebih panjang daripada rincian pekerjaan, dan setiap angka membuat Moeka mengingat tagihan yang berbeda."
    "Kuga" "Kamu bisa membantu rumah sekaligus membangun portofolio. Sayang kalau kesempatan ini lewat hanya karena terlalu banyak ragu."
    moeka "Aku perlu rincian sesi dan hak atas fotonya dulu. Boleh kubawa untuk dibaca?"
    call kk_family_menu("Mo06", ["Dukung ia mengambil tawaran itu.", "Halangi; ada yang tidak beres pada Kuga.", "Ikut menemaninya ke sesi itu."])
    if _return == "A":
        nar "Kau mendukungnya mengambil tawaran. Moeka tersenyum lega, menerima pendapatmu sebagai tanda bahwa kekhawatirannya mungkin hanya terlalu besar."
        moeka "Oke. Aku coba. Semoga nanti bisa cerita ini awal yang bagus, ya."
        nar "Bayaran yang dijanjikan terasa nyata. Bagian pekerjaan yang belum terjelaskan masih harus ia hadapi ketika kegembiraan awal sudah lewat."
    elif _return == "B":
        moeka "Kau merasa begitu juga? ...Mungkin aku terlalu butuh uang sampai mengabaikan firasat."
        nar "Kau menunjukkan bagian tawaran yang belum jelas. Moeka menahan kecewa karena penghasilan itu berarti banyak, lalu meminta Kuga waktu untuk memeriksa sebelum menjawab."
    else:
        "Kuga" "Oh, kau bawa teman. ...Tidak masalah. Untuk sekarang."
        nar "Moeka meminta kehadiran pendamping disebutkan sejak awal. Ketika nada Kuga berubah, ia melihat sendiri sesuatu yang tidak sesuai dengan keramahan tawaran tadi."
        moeka "Aku ingin bekerja dengan jelas. Temanku bukan masalah kalau pekerjaannya memang sesuai yang dibicarakan."
    return

# ┌─ PANDUAN CERITA · Mo08 · Natal Moeka dan Adik
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia pulang ke rumah.
# │ INTI    : A ikut / B kirim hadiah / C tidak.
# │ AKHIRAN : hub besar #3.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo08:
    call kk_scene_enter("moeka", "Kantin Pusat · Menjelang Natal")
    nar "Moeka membagi daftar belanja menjadi tiga kolom kecil, satu untuk setiap adik. Kolom bagi dirinya tidak ada. Ia memperlihatkan sebuah pita murah yang bisa dipakai berulang kali dengan wajah bangga seorang penemu."
    moeka "Aku pulang buat Natal. Mereka bilang nggak perlu apa-apa, jadi tentu saja aku malah makin ingin bawa sesuatu. Aku tahu. Logikaku sedang cuti."
    call kk_family_menu("Mo08", ["Ikut pulang bersamanya.", "Kirim hadiah untuk adik-adiknya.", "Tidak terlibat."])
    if _return == "A":
        moeka "Kau mau ikut? Rumahku sempit dan ramai, tapi... mereka pasti senang ada tamu."
        nar "Kau ikut sebagai tamu yang bersedia membantu, bukan penyelamat yang memeriksa kekurangan rumah. Moeka mulai menceritakan kebiasaan adik-adiknya dan memberi peringatan bahwa semua akan bertanya banyak hal sekaligus."
    elif _return == "B":
        moeka "Kau mengirim hadiah? Mereka akan mengira aku yang beli—biar kubilang dari siapa sebenarnya."
        nar "Ia meminta ukuran dan jenisnya dibicarakan lebih dahulu agar tak ada anak yang merasa dilupakan. Setelah memastikan itu, kegembiraannya keluar tanpa perlu dibesar-besarkan untuk membuktikan terima kasih."
    else:
        nar "Kau tidak terlibat. Moeka menyelesaikan belanja sendiri, membawa tas yang lebih berat daripada barang untuk beberapa hari seharusnya."
        nar "Dari rumah ia mengirim foto adik-adiknya tertawa. Ia tidak ikut masuk bingkai karena sedang memegang kamera dan memastikan seluruh hasil usahanya tampak bahagia."
    return

# ┌─ PANDUAN CERITA · Mo09 · Hatsumode: Doa Ayah
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia berdoa untuk ayah.
# │ INTI    : A temani / B tanya / C abaikan.
# │ AKHIRAN : Intimasi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo09:
    call kk_scene_enter("moeka", "Kuil · Hatsumode")
    nar "Antrean kuil sudah berganti orang ketika Moeka masih berdiri dengan telapak tangan rapat. Sesudah menunduk ia kembali memejamkan mata, seolah ada satu permintaan yang belum berani disebut sampai selesai."
    call kk_family_menu("Mo09", ["Temani ia berdoa dalam diam.", "Tanya apa yang ia doakan.", "Abaikan dan tunggu di luar."])
    if _return == "A":
        moeka "Kau menunggu sampai aku selesai? ...Aku berdoa supaya ayah bertahan sampai aku lulus."
        nar "Ia malu karena doanya terdengar seperti menawar waktu. Kau membiarkannya mengatakan takut tanpa menjanjikan hasil yang tak bisa diketahui siapa pun."
        moeka "Aku cuma ingin dia sempat melihat aku berhasil dalam sesuatu yang bukan bertahan hari ini."
    elif _return == "B":
        moeka "Untuk ayah. Selalu untuk ayah. ...Kadang aku lupa mendoakan diriku sendiri."
        nar "Kau menanyakan apa yang ingin diminta untuk dirinya. Moeka tertawa, kemudian tak punya jawaban. Baru di anak tangga terakhir ia mengatakan ingin satu hari ketika seluruh keluarganya bisa makan tanpa menghitung yang harus dikurangi besok."
    else:
        nar "Kau menunggu di luar tanpa membahas doanya. Moeka menyusul dengan mata sedikit merah, lalu menawarkan memotretmu di gerbang agar pembicaraan tidak berbalik ke wajahnya."
    return

# ┌─ PANDUAN CERITA · Mo10 · Coklat untuk Tiga Adik
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia membuat coklat untuk adik.
# │ INTI    : A bantu / B beri uang / C tak peduli.
# │ AKHIRAN : pemain mengenal adik-adik.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo10:
    call kk_scene_enter("moeka", "Kantin Pusat · Coklat untuk adik")
    nar "Tiga bungkus coklat diberi tanda berbeda agar mudah dikenali adik-adiknya. Moeka menghitung ulang bahan yang tersisa, lalu membagi hiasan dengan ketelitian yang jarang terlihat pada jadwal pribadinya."
    moeka "Kalau yang ini dapat bintang dan yang itu nggak, kami akan mengadakan perundingan damai di rumah. Jadi semuanya harus punya bintang."
    call kk_family_menu("Mo10", ["Bantu ia membuat dan membungkusnya.", "Beri ia uang untuk bahan.", "Tak peduli dengan urusan adiknya."])
    if _return == "A":
        moeka "Kau ikut membungkus? Adik-adikku akan bertanya siapa yang bantu. ...Akan kuceritakan tentangmu."
        nar "Kalian menempelkan hiasan sambil ia bercerita. Nama adik-adiknya berhenti menjadi daftar kebutuhan dan mulai menjadi orang-orang dengan humor, kesukaan, dan pertengkaran kecil yang sangat dikenalnya."
    elif _return == "B":
        moeka "Uang? ...Aku tidak enak. Tapi untuk mereka, akan kuterima. Terima kasih."
        nar "Kau menjelaskan bantuan itu tidak menuntut balasan. Moeka tetap mencatat jumlahnya, belum mudah menerima bahwa ada pemberian yang tidak akan berubah menjadi tagihan saat ia berkata tidak nanti."
    else:
        nar "Kau membiarkannya menyelesaikan sendiri. Moeka berhenti bercerita tentang adik-adik setelah sadar perhatianmu sudah berpindah. Tiga bungkus itu tetap rapi saat selesai; tidak ada yang menunjukkan berapa lama ia duduk di sana."
    return

# ┌─ PANDUAN CERITA · Mo11 · Hujan Deras: Ponsel Mati
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia hilang kontak.
# │ INTI    : A cari / B tunggu / C abaikan.
# │ AKHIRAN : jendela intervensi #1; stage 1 (beban menumpuk).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo11:
    call kk_scene_enter("moeka", "Kantin Pusat · Ponsel mati")
    play sound "audio/sfx/rain.wav"
    nar "Panggilan ke Moeka tidak tersambung sejak pagi. Ia tak muncul pada kegiatan yang biasanya justru dimintanya agar dimulai tepat waktu. Di luar, hujan membuat semua rencana mencari terasa lebih sulit."
    nar "Pesan terakhirnya hanya mengatakan akan menyusul. Kalimat yang biasa tidak cukup menenangkan ketika kabar lain juga mulai hilang."
    call kk_family_menu("Mo11", ["Cari ia sampai ketemu.", "Tunggu sampai ia muncul sendiri.", "Abaikan."])
    if _return == "A":
        moeka "Kau mencariku? Di tengah hujan begini? ...Kenapa? Aku bukan siapa-siapa yang penting."
        nar "Ponselnya mati dan harinya berantakan oleh urusan rumah. Kau menemukannya basah, terlalu letih untuk menyiapkan cerita lucu tentang itu."
        nar "Kau mengatakan ketidakhadirannya diketahui. Untuk beberapa saat ia tidak percaya bahwa seseorang boleh mencarinya tanpa sedang membutuhkan sesuatu darinya."
    elif _return == "B":
        nar "Kau menunggu sampai ia menghubungi. Kabar baru datang keesokan hari, disertai tawa tentang ponsel yang tidak bisa diandalkan. Moeka tidak menyebut berapa lama ia bingung harus pulang ke mana lebih dahulu."
    else:
        nar "Kau menganggapnya urusan biasa yang tidak perlu ditanyakan. Moeka kembali dengan penjelasan pendek dan segera mengambil tugas tambahan agar orang berhenti membahas ketidakhadirannya."
        nar "Hari yang buruk berlalu tanpa seorang pun mengetahui seberapa buruk rasanya dari dalam. Ia menyimpan pelajaran bahwa menghilang sedikit pun tampaknya tidak banyak mengubah kehidupan orang lain."
    return

# ┌─ PANDUAN CERITA · Mo12 · IPK Turun
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : nilai turun.
# │ INTI    : A bantu belajar / B beri uang / C tidak peduli.
# │ AKHIRAN : beasiswa mulai terancam.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo12:
    call kk_scene_enter("moeka", "Kantin Pusat · IPK turun")
    nar "Moeka menatap nilai lebih lama daripada pesan keluarga tentang uang. Dua masalah itu tidak bisa lagi diletakkan di laci yang berbeda: bekerja lebih banyak menggerus kuliah, kuliah yang jatuh mengancam satu hal yang membuatnya mampu tetap bekerja untuk rumah."
    moeka "Aku selalu bilang tinggal atur jadwal. Sekarang jamnya sudah habis. Kalau beasiswa hilang, aku nggak punya cadangan yang bisa dibuat dari semangat saja."
    call kk_family_menu("Mo12", ["Bantu ia belajar.", "Beri ia uang untuk meringankan beban.", "Tidak peduli."])
    if _return == "A":
        moeka "Kau mau menemaniku belajar? ...Mungkin masih ada jalan kalau tidak sendirian."
        nar "Kalian memulai dari satu tugas yang paling dekat tenggat, bukan menuntut seluruh semester diperbaiki malam itu. Ia berhenti menyebut dirinya bodoh ketika akhirnya berhasil menjelaskan bagian yang tadi tak dipahami."
    elif _return == "B":
        moeka "Uang lagi? ...Aku mulai merasa berutang padamu lebih dari yang bisa kubalas."
        nar "Bantuan itu mengurangi kebutuhan bekerja untuk sementara. Kau mengatakan ia tidak harus menukar kedekatan demi menerimanya, tetapi ia perlu waktu sebelum benar-benar percaya bahwa penolakan di masa depan tidak akan membuat uang ini disebut kembali."
    else:
        nar "Kau tidak menanggapi lebih jauh. Moeka menutup layar nilai dan mulai membicarakan pekerjaan berikutnya, sesuatu yang masih tampak dapat menghasilkan uang sekarang."
        nar "Makin sedikit ruang tersisa untuk hal yang baru akan runtuh beberapa bulan lagi. Ia terus berlari di antara keduanya, sendirian."
    return

# ┌─ PANDUAN CERITA · Mo26 · Natal Sunyi
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia sendirian.
# │ INTI    : A datang / B kirim pesan / C tidak ada.
# │ AKHIRAN : jendela #5.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo26:
    call kk_scene_enter("moeka", "Kantin Pusat · Natal sunyi")
    nar "Moeka mengirim foto lampu Natal di luar jendelanya tanpa ikut muncul. Ketika kautanya apakah sedang di rumah, jawabannya datang terlambat: masih di kos, belum tahu nanti."
    nar "Di meja ada makanan yang belum dibuka dan ponsel yang terus diperiksa. Malam itu ia tidak punya tenaga untuk membuat kesendirian terdengar seperti pilihan yang seru."
    call kk_family_menu("Mo26", ["Datang menemaninya langsung.", "Kirim pesan agar ia tahu ada yang ingat.", "Tidak melakukan apa pun."])
    if _return == "A":
        moeka "Kau datang? Di malam seperti ini? ...Aku hampir percaya tidak ada yang akan datang."
        nar "Kau tidak meminta ia segera senang. Kalian membuka makanan, menghubungi orang yang perlu tahu keadaannya, dan membiarkan malam berlangsung tanpa pertunjukan bahwa semua sudah baik."
    elif _return == "B":
        moeka "Pesanmu masuk. ...Satu pesan. Kadang satu saja cukup untuk melewati satu malam."
        nar "Kau menanggapi dengan sungguh-sungguh dan menanyakan siapa yang bisa menemaninya jika malam terasa makin berat. Ia menyebut Rina setelah ragu. Kabar singkat itu tidak menyelesaikan masalahnya, tetapi membuka jalan agar ia tidak hanya menunggu satu orang."
    else:
        nar "Kau tidak menghubungi. Foto lampu itu tetap menjadi pesan terakhir dari Moeka malam tersebut. Di kos, ia menaruh ponsel menghadap bawah lalu membaliknya lagi beberapa menit kemudian."
        nar "Tidak ada satu malam yang sendirian menjelaskan seluruh krisis. Malam ini menambah sesuatu pada tumpukan yang belum berhasil dibagikannya kepada orang lain."
    return

init 1 python:
    _hook("Mo03-A", lambda: kk_rel("moeka","trust",-2))
    _hook("Mo03-B", lambda: (kk_rel("moeka","trust",4), kk_adj("stres_moeka",-5)))
    _hook("Mo03-C", lambda: (kk_rel("moeka","trust",5), kk_adj("stres_moeka",-8)))
    _hook("Mo04-A", lambda: (kk_rel("moeka","intim",6), kk_flag("moeka_rahasia_lapar")))
    _hook("Mo04-B", lambda: kk_rel("moeka","trust",4))
    _hook("Mo04-C", lambda: (kk_adj("stres_moeka",8), kk_rel("moeka","trust",-4)))
    _hook("Mo05-A", lambda: (kk_flag("moeka_keluarga_diketahui"), kk_rel("moeka","intim",4)))
    _hook("Mo05-B", lambda: kk_rel("moeka","trust",4))
    _hook("Mo05-C", lambda: (kk_flag("moeka_keluarga_diketahui"), kk_moeka_burden(5)))
    _hook("Mo06-A", lambda: (kk_flag("kuga_jerat_mulai"), kk_adj("stres_moeka",-10)))
    _hook("Mo06-B", lambda: (kk_rel("moeka","trust",5), kk_flag("kuga_dihalangi")))
    _hook("Mo06-C", lambda: kk_flag("kuga_ditemani"))
    _hook("Mo08-A", lambda: (kk_rel("moeka","intim",6), kk_flag("moeka_adik_dikenal")))
    _hook("Mo08-B", lambda: kk_rel("moeka","aff",4))
    _hook("Mo08-C", lambda: kk_moeka_burden(8))
    _hook("Mo09-A", lambda: (kk_rel("moeka","intim",5), kk_flag("moeka_ayah_diketahui")))
    _hook("Mo09-B", lambda: (kk_rel("moeka","trust",4), kk_flag("moeka_ayah_diketahui")))
    _hook("Mo09-C", lambda: kk_rel("moeka","trust",-3))
    _hook("Mo10-A", lambda: (kk_rel("moeka","intim",5), kk_flag("moeka_adik_dikenal")))
    _hook("Mo10-B", lambda: kk_adj("stres_moeka",-6))
    _hook("Mo10-C", lambda: kk_rel("moeka","aff",-3))
    _hook("Mo11-A", lambda: (kk_rel("moeka","trust",6), kk_flag("moeka_intervensi_1")))
    _hook("Mo11-B", lambda: (kk_moeka_stage(1), kk_moeka_burden(6)))
    _hook("Mo11-C", lambda: (kk_moeka_stage(1), kk_moeka_burden(12)))
    _hook("Mo12-A", lambda: (kk_rel("moeka","trust",5), kk_adj("stres_moeka",-8)))
    _hook("Mo12-B", lambda: kk_adj("stres_moeka",-5))
    _hook("Mo12-C", lambda: (kk_adj("stres_moeka",12), kk_flag("beasiswa_terancam")))
    _hook("Mo26-A", lambda: (kk_rel("moeka","intim",8), kk_flag("moeka_ditemani_natal"), kk_adj("stres_moeka",-15)))
    _hook("Mo26-B", lambda: (kk_rel("moeka","trust",5), kk_flag("moeka_dikabari_natal")))
    _hook("Mo26-C", lambda: (kk_adj("stres_moeka",15), kk_flag("moeka_natal_sendiri")))
