# Bagian 9 — `K01` (*Senyum yang Terlalu Cepat*) · Host Chiasa (M01a)

Target File: `game/kk_koita_y1.rpy` (`label kkscene_K01`, blok `if kk_host == "chiasa":`)

```renpy
label kkscene_K01:
    call kk_scene_enter("koita", "Gedung Sastra")
    if kk_host == "chiasa":
        nar "Jam makan siang di kantin dekat Gedung Sastra penuh dengan riuh rendah mahasiswa yang baru selesai mengikuti kelas dan sesi pengenalan hari pertama. Aroma kari hangat, kuah udon, serta bunyi baki plastik yang diletakkan di atas meja panjang bercampur di bawah cahaya matahari siang yang masuk melalui jendela kaca tinggi."
        nar "Baru saja selesai dari acara orientasi di sayap barat, kau melangkah menyusuri lorong meja sambil memegangi nampan makan siangmu. Dua langkah sebelum mencapai barisan kursi dekat jendela, langkahmu melambat ketika melihat sosok Amamiya Koita sudah duduk di sana—dan sebuah pertunjukan kecil sedang berlangsung tepat di depan matamu."
        nar "Di sebelah meja, Sakurajima Nagisa baru saja tiba sambil menyeimbangkan nampan makan siang dan gulungan kertas gambar di ketiaknya. Tanpa diminta, Koita langsung menahan sandaran kursi kosong di sebelahnya dengan lutut agar tidak bergeser sambil merapikan tasnya sendiri supaya Nagisa bisa meletakkan nampan dengan mudah."
        nar "Namun belum sempat Koita benar-benar duduk, matanya sudah menangkap sosok Tachibana Miyuki yang melintas di lorong sambil memeluk map plastik dan segelas kopi dari mesin penjual otomatis. Koita langsung mengangkat satu tangan dan melambai dengan senyum hangat."
        koita "Miyuki-senpai, sudah makan siang? Jangan minum kopi lagi dong, ya. Kemarin katanya perut Senpai agak nggak enak habis jaga praktikum."
        nar "Langkah anggun Miyuki terhenti di tepi meja. Mahasiswi tahun ketiga Kedokteran itu mengedip pelan, lalu tersenyum lembut yang tampak tulus tersentuh."
        miyuki "Ara, Koita-kun masih ingat hal sekecil itu? Senpai jadi terharu lho. Baiklah, setelah mengantar map ini ke ruang dosen, Senpai janji beli roti dulu sebelum lanjut."
        nar "Di samping Koita, ujung alis Nagisa langsung berkedut tipis mendengar nada hangat itu. Ia meletakkan sumpit kayunya di atas nampan dengan bunyi yang sedikit lebih keras dari biasanya."
        nagisa "Kalau ingatanmu soal orang lain memang sehebat itu, harusnya kau juga ingat janjimu mengembalikan buku catatanku yang kaupinjam minggu lalu, Koita."
        nar "Koita sama sekali tidak tampak kikuk. Ia memutar tubuhnya menghadap Nagisa sepenuhnya, menepuk tas selempangnya, lalu menurunkan suaranya menjadi nada lembut yang seolah hanya ditujukan untuk mereka berdua."
        koita "Ada di tas kok, sudah kubawa dari pagi. Sengaja kutaruh di sini supaya aku punya alasan buat duduk dan makan siang bareng kamu hari ini."
        nar "Rona merah tipis langsung naik ke pipi Nagisa. Ia mendengus pelan dan membuang muka ke arah jendela, tetapi tangannya tetap menggeser tasnya sedikit ke samping untuk memberi Koita ruang duduk yang lega."
        nar "Tepat di belakang Miyuki, Kujo Harumi melintas pelan sambil mendekap sebuah buku sampul tebal. Sebelum Harumi sempat hanya mengangguk singkat dan berlalu, Koita sudah lebih dulu mengangkat buku saku yang tadi sempat ia jadikan alas tepi nampan di meja, memperlihatkan sampulnya."
        koita "Harumi! Aku sudah baca novel rekomendasi darimu kemarin malam. Bagian akhirnya bikin kepikiran terus—nanti kalau ada waktu luang, tolong jelaskan sudut pandangmu soal bab terakhirnya, ya. Aku mau dengar pendapatmu dulu sebelum baca ulasan lain."
        nar "Langkah Harumi melambat. Sorot matanya yang tadinya datar sedikit melunak, memancarkan binar kecil seseorang yang merasa pendapatnya sungguh-sungguh dinantikan."
        harumi "...Baiklah. Kalau kamu memang sudah selesai membacanya sampai akhir, nanti aku bisa jelaskan di perpustakaan atau kafe."
        nar "Kau berdiri diam di pinggir lorong memegangi nampanmu, menyaksikan seluruh rangkaian itu dalam waktu kurang dari dua menit. Tiga gadis, tiga cara berbeda untuk membuat masing-masing dari mereka merasa diingat dan ditunggu."
        nar "Dan satu detail kecil langsung menusuk matamu: setiap kali Koita melontarkan kalimat-kalimat manis itu, senyum hangatnya selalu tiba sepersekian detik lebih cepat daripada jawaban lawan bicaranya—seolah ia sedang memeriksa apakah kehangatannya berhasil mengena."
    else:
        ...
    call kk_family_menu("K01", ["Amati dan catat polanya diam-diam.", "Tegur terang-terangan bahwa ia pilih kasih.", "Abaikan saja."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau menahan diri untuk tidak langsung melangkah maju atau menyela. Kau berdiri diam di dekat tiang kantin selama beberapa detik lagi, memetakan setiap detail cara kerja Koita di kepalamu."
            nar "Kau memperhatikan siapa yang ia tatap ketika menyebut kata 'nanti' kepada Harumi—tidak ada hari, jam, atau tempat yang benar-benar dikunci. Kepada Miyuki, ia menawarkan kepedulian yang manis tanpa harus ikut menemaninya pergi. Dan kepada Nagisa, satu kalimat menggoda yang terdengar pribadi sudah cukup memadamkan rasa kesalnya."
            nar "Tidak ada satu pun komitmen nyata yang keluar dari mulutnya, tetapi ketiga gadis itu menerima potongan kecil dari perhatian dan masa depannya."
            nar "Baru ketika Miyuki melangkah pergi membawa map dan Harumi berjalan menuju rak pengembalian baki, tatapan Koita akhirnya menangkap sosokmu yang berdiri diam memegang nampan di pinggir lorong."
            koita "Lho, Chiasa? Dari tadi berdiri di situ saja? Kenapa nggak langsung panggil—mau duduk bareng di sini juga?"
            nar "Bahkan sebelum kau sempat mengangguk, Koita sudah lebih dulu menggeser kursi kosong di seberangnya dengan satu tangan sambil tersenyum ramah. Di sebelahnya, Nagisa menoleh sekilas ke arahmu sambil meletakkan gelas airnya."
            nagisa "Oh, acara pengenalan Fakultas Seni sudah selesai, Chiasa?"
            chiasa "Baru saja selesai. Aku ikut duduk di sini, ya."
            nar "Kau berjalan mendekat dan meletakkan nampanmu di meja. Saat kau duduk, satu catatan penting sudah terkunci rapi di benakmu: keramahan Koita memang nyata—tetapi sama nyatanya dengan betapa cepat matanya memeriksa apakah keramahan itu berhasil menahan orang-orang di sekelilingnya."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kau tidak membiarkan pertunjukan kecil itu berlalu begitu saja. Kau melangkah maju mendekati meja panjang, meletakkan nampan makan siangmu di pinggir kayu dengan bunyi yang cukup jelas untuk menarik perhatian, lalu menatap Koita lurus-lurus sebelum Miyuki dan Harumi sempat menjauh."
            chiasa "Hebat juga, ya. Dalam waktu kurang dari dua menit, semua orang kebagian jatah perhatian khusus masing-masing—tapi tidak ada satu pun yang jelas kapan waktunya. Itu namanya ramah, atau sengaja pilih kasih supaya semua tetap menunggu?"
            nar "Seketika, obrolan hangat di sekitar meja itu terhenti total. Miyuki yang baru hendak membalikkan badan ikut terdiam dengan map masih di pelukannya, sementara Harumi menunduk sedikit menatap sampul bukunya dengan wajah canggung."
            nar "Senyum hangat di wajah Koita mengendur sepersekian detik. Ia berkedip kaget, lalu menggaruk pelipisnya pelan sambil tertawa pendek yang berusaha terdengar ringan."
            koita "Eh, pilih kasih? Maksudmu apa sih, Chiasa? Aku kan cuma ingat hal-hal kecil tentang teman-teman sendiri. Masa menanyakan kabar Senpai atau bahas buku sama Harumi dianggap aneh? Kamu juga begitu ke teman-temanmu, kan?"
            nar "Sebelum kau sempat membalas, Nagisa yang duduk di sebelah Koita langsung menoleh ke arahmu dengan kening berkerut dan nada membela yang muncul begitu saja."
            nagisa "Memangnya hal sepele begini harus diributkan di tengah kantin? Koita kan dari dulu memang begitu orangnya kalau sama teman."
            miyuki "Ara, tidak perlu tegang begitu. Kalau begitu Senpai duluan ya, nanti terlambat mengantar map ke ruang dosen."
            nar "Miyuki tersenyum halus untuk meredakan suasana lalu melangkah pergi, diikuti Harumi yang mengangguk pelan sebelum cepat-cepat menjauh dari meja."
            nar "Koita tertawa kecil untuk mencairkan sisa kecanggungan dan menggeserkan kursi kosong untukmu seolah tidak ada yang berubah. Namun sepanjang sisa jam makan siang itu, kau merasakan betul pergeserannya: setiap kali ada kenalan lewat di lorong kantin, tatapan Koita sempat melirik ke arahmu terlebih dahulu sebelum ia memutuskan bagaimana cara menyapa mereka."
    else:
        if kk_host == "chiasa":
            nar "Kau memutuskan tidak membuang tenaga mengomentari kebiasaan lama sang protagonis di hari pertama kuliah. Kau melangkah santai mendekati meja panjang, menarik kursi kosong di ujung yang tidak mengganggu siapa pun, lalu meletakkan nampan makan siangmu sambil menyapa biasa."
            chiasa "Meja ini ramai juga. Aku ikut duduk di ujung sini ya—jam istirahat Fakultas Seni lumayan mepet, habis ini masih ada pengarahan ruang studio."
            nar "Koita langsung menyambut topik aman itu dengan mudah dan tampak lega. Ia menggeser tempat sumpit ke arahmu sambil menanyakan bagaimana kesan gedung Fakultas Seni Rupa di sayap barat."
            koita "Oh, sudah selesai sesi pembukaannya? Gedung sayap barat lumayan jauh kan kalau jalan kaki dari gerbang depan? Kalau nanti kelasmu selesai sore, kabari saja ya."
            nar "Tanpa ada gesekan tambahan, kerumunan kecil di sekitar meja itu perlahan terurai dengan sendirinya. Miyuki tersenyum pamit dan melanjutkan langkahnya sambil memeluk map menuju ruang dosen, Harumi menyimpan kembali bukunya ke dalam tas kanvas dan mengangguk pelan sebelum pergi, sementara Nagisa membuka buku catatan yang akhirnya dikeluarkan Koita dari tasnya."
            nar "Masing-masing dari mereka pergi atau melanjutkan siang membawa potongan percakapan yang terasa utuh dan menyenangkan di kepala mereka sendiri—sangat berbeda dari keseluruhan gambaran yang baru saja kaudengar dan kausaksikan dari pinggir lorong."
```
