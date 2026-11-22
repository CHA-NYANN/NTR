# Tahun 1 Nagisa yang hangat: foto lama, Koko, Valentine, White Day.
# Efek mengikuti Event_Nagisa dan Alur_Cabang/02 (kelekatan, gengsi); angka adalah setelan prototipe.
# Bagian posesif/yandere (N14 ke atas) tidak disentuh di sini.
# ┌─ PANDUAN CERITA · N05 · Foto Berempat
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : ia menatap foto lama.
# │ INTI    : A bercerita tentang Koko / B mengganggu / C diam.
# │ AKHIRAN : Intimasi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N05:
    call kk_scene_enter("nagisa", "Studio Arsitektur")
    if kk_host == "chiasa":
        if kk_slot == 1:
            nar "Studio Arsitektur siang itu sudah mulai sepi setelah sebagian besar mahasiswa tahun kedua bergegas turun menuju kantin. Bau serbuk kayu balsa, lem kertas, dan grafit pensil masih tercium samar di dekat deretan meja gambar panjang, sementara cahaya matahari siang jatuh terang melewati jendela kaca tinggi."
        else:
            nar "Studio Arsitektur sore itu sudah mulai sepi setelah sebagian besar mahasiswa tahun kedua bergegas pulang. Bau serbuk kayu balsa, lem kertas, dan grafit pensil masih tercium samar di dekat deretan meja gambar panjang, sementara sinar matahari sore menembus jendela kaca tinggi dan menyinari debu-debu halus di udara."
        nar "Di meja paling sudut dekat jendela, Sakurajima Nagisa duduk seorang diri dengan buku referensi tebal terbuka di pangkuannya. Ia menyelipkan selembar foto cetak lama di antara halaman buku tersebut sebagai pembatas, tetapi sejak kamu membuka pintu studio semenit lalu, lembaran bukunya sama sekali belum dibalik."
        chiasa "Nagisa-senpai, masih di studio? Aku mampir sebentar mau pinjam penggaris skala besinya dong, punyaku tertinggal di loker gedung sebelah."
        nar "Nagisa tidak langsung menjawab, seolah baru menyadari pintu studio terbuka ketika langkah kakimu sudah dekat. Kamu melangkah mendekati meja kerjanya. Begitu sampai di samping kursinya, pandanganmu jatuh ke atas foto cetak yang tergeletak di tengah halaman buku. Warna tepi kertas fotonya sudah agak menguning. Di dalam gambar itu tampak empat anak usia sekolah dasar berdiri berjejer di depan gerbang festival kuil, dan di pelukan Nagisa kecil terdapat sebuah boneka kelinci putih yang kedua telinganya terlalu panjang hingga nyaris terpotong batas atas bingkai foto."
        chiasa "Eh, tunggu sebentar... itu foto kita berempat waktu masih SD ya, Nagisa-senpai?"
        nagisa "Waduh! Chiasa?! Sejak kapan kamu berdiri di situ?! Jangan lihat rambutku di foto ini, tutup mata sana!"
        nar "Nagisa refleks mengangkat kedua bahunya dan menutupi wajahnya sendiri dengan sebelah tangan, padahal yang sedang kamu lihat adalah foto masa kecilnya bertahun-tahun silam."
        chiasa "Haha, kenapa malah wajah Senpai yang ditutup sekarang? Yang ada di foto kan zaman SD dulu."
        nagisa "Tetap aja memalukan tahu! Hari itu sebelum berangkat ke festival, Kak Haruto yang maksa nyisirin rambutku di ruang tamu! Dikiranya asal belahan kanan sama kirinya seimbang sudah rapi, tahunya waktu kena angin malam malah mekar kayak sapu ijuk!"
        chiasa "Nggak kayak sapu ijuk kok, Senpai. Malah kelihatan imut banget waktu masih kecil. Pipinya masih bulat lagi."
        nagisa "Nggak usah muji basa-basi, dari suaramu aja kelihatan kamu lagi nahan ketawa! Berhenti melihatnya!"
        nar "Tangan Nagisa bergerak cepat hendak menyelipkan kembali foto lama itu ke dalam lipatan buku. Gerakannya mendadak melambat ketika ia menyadari matamu sudah berpindah dari ikatan rambutnya, kini tertahan pada boneka kelinci putih bertelinga panjang di pelukannya."
    else:
        if kk_slot == 1:
            nar "Studio Arsitektur siang itu sudah mulai kosong setelah kelas studio pagi berakhir dan sebagian besar mahasiswa keluar mencari makan siang. Aroma potongan kayu balsa dan lem kering masih tertinggal di sekitar meja-meja gambar, sementara cahaya matahari siang masuk terang melewati deretan jendela tinggi."
        else:
            nar "Studio Arsitektur sore itu sudah mulai kosong setelah jam kuliah studio berakhir. Aroma potongan kayu balsa dan lem kering masih tertinggal di sekitar meja-meja gambar, sementara cahaya matahari sore jatuh miring melewati deretan jendela tinggi."
        nar "Di meja sudut dekat jendela, Sakurajima Nagisa duduk sendirian dengan sebuah buku arsitektur tebal terbuka di atas pangkuannya. Selembar foto cetak lama tergeletak di atas halaman yang terbuka sebagai pembatas buku, dan sejak kamu masuk dari pintu depan tadi, mata Nagisa belum bergeser sedikit pun dari foto tersebut."
        yutaka "Masih betah aja duduk di studio, Nagisa? Kirain kamu sudah turun duluan bareng anak-anak kelasmu."
        nar "Kamu berjalan santai menghampiri mejanya untuk mengembalikan flashdisk materi yang kemarin kamu pinjam. Saat berhenti di samping kursinya, matamu ikut melihat foto cetak lama di atas halaman bukunya. Di sana tampak empat anak kecil berdiri berbaris di depan gerbang festival musim panas, dan di pelukan Nagisa kecil ada boneka kelinci putih yang telinganya begitu panjang sampai hampir keluar dari batas atas foto."
        yutaka "Lho, tunggu dulu... itu foto kita berempat waktu zaman SD dulu kan?"
        nagisa "Waduh! Yutaka?! Sejak kapan kamu di situ?! Jangan lihat model rambutku di foto ini, minggir sana!"
        nar "Nagisa refleks mengibaskan tangannya di atas halaman buku dengan pipi yang langsung bersemu merah."
        yutaka "Tenang dulu, aku cuma melirik sekilas. Itu rambutmu kenapa dulu ikatannya tinggi sebelah begitu?"
        nagisa "Waktu itu kan Kak Haruto yang maksa nyisirin rambutku sebelum kita berangkat! Dikiranya asal ikatan kanan sama kirinya sama tinggi sudah bagus, hasilnya malah mekar nggak karuan begitu kena angin!"
        yutaka "Haha, padahal lucu kok. Kelihatan banget dulu kamu masih polos dan belum galak kayak sekarang. Eh, lihat juga tuh Koita di sebelahmu, masih megang permen kapas yang lebih gede dari kepalanya."
        nagisa "Diam! Nggak usah komentar soal mukaku waktu SD! Itu kan gara-gara kamu sama Ko-kun lari duluan terus aku disuruh foto terburu-buru!"
        yutaka "Lah, kok jadi nyalahin aku segala."
        nar "Ia sudah memegang tepi foto itu untuk menyembunyikannya kembali ke sela halaman buku, tetapi gerakannya terhenti saat melihat tatapanmu justru tertuju pada boneka kelinci putih di pelukan masa kecilnya."
    call kk_family_menu("N05", ["\"Boneka kelinci yang kamu peluk itu namanya Koko, kan? Masih disimpan?\"", "\"Telinganya kepanjangan, sekarang pasti sudah lusuh banget ya bonekanya?\"", "Biarkan ia memandangi foto itu dalam diam."])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Boneka kelinci putih yang Senpai peluk erat-erat di foto itu namanya Koko, kan? Sampai sekarang masih Senpai simpan di kamar?"
            nagisa "Iya, masih kusimpan lah di dekat bantal. Masa boneka kayak gitu langsung dibuang begitu aja."
            nar "Nagisa menurunkan kembali foto itu ke atas halaman bukunya, lalu mengusap bagian gambar telinga kelinci tersebut dengan ujung ibu jarinya. Suaranya yang tadi melengking galak perlahan turun jauh lebih lembut."
            nagisa "Koko ini... dulu Ko-kun yang menangin buatku waktu kita mampir ke stan lempar gelang di festival musim panas."
            chiasa "Oh ya? Ko-nii menangin dari permainan stan? Perasaan Ko-nii dulu nggak terlalu jago permainan lempar-lempar begitu."
            nagisa "Memang nggak jago-jago amat! Lima gelang pertamanya aja meleset semua kena pinggir meja, malah hampir nyangkut di botol hadiah sebelah. Waktu itu aku gengsi mau bilang pengin boneka kelincinya, jadi aku cuma bilang mau lihat-lihat lampu stan aja, padahal kakiku berhenti terus di depan rak hadiah itu."
            chiasa "Terus gimana ceritanya sampai dapat?"
            nar "Sudut bibir Nagisa melengkung kecil saat mengingat malam festival tersebut."
            nagisa "Kupikir nggak ada yang sadar. Eh, waktu kita sudah jalan ke stan takoyaki di sebelah, Ko-kun malah pamit balik lagi sendirian dan tukar sisa uang sakunya buat beli kupon tambahan. Aku pikir dia cuma lupa kembalian, tahunya sepuluh menit kemudian dia lari-lari nyusul sambil bawa Koko di tangannya. Aku senang banget waktu itu... gara-gara ternyata dia memperhatikan apa yang kulihat."
            chiasa "Kelihatan banget kok dari foto ini, Senpai. Di antara kita berempat, senyum Senpai yang paling lebar sendiri waktu meluk Koko."
            nar "Begitu mendengar kalimatmu, Nagisa langsung tersentak sadar betapa lembut nada bicaranya barusan di hadapanmu. Seketika wajahnya memerah sampai ke telinga, dan ia buru-buru menutup bukunya dengan bunyi gedebuk pelan."
            nagisa "H-hei, jangan mikir yang aneh-aneh ya! Lagian waktu itu harga kupon lempar gelangnya juga murah banget kok, cuma dua ratus yen! Anak kecil mana aja juga bisa menang kalau lagi kebetulan beruntung!"
            chiasa "Iya, iya, murah kok, anggap aja Ko-nii lagi kebetulan beruntung malam itu, Nagisa-senpai. Tapi dua ratus yen zaman SD kan lumayan buat beli dua es serut lho."
            nagisa "Nggak usah ikut menghitung uang sakunya segala! Pokoknya itu cuma kenangan masa kecil biasa!"
            chiasa "Hehe, baik, baik, aku nggak bakal bahas soal es serut lagi."
            nagisa "Sudah ah, jangan senyum-senyum begitu! Tadi katanya mau pinjam penggaris skala besi kan?! Tuh ambil sendiri di tempat pensil sebelah kiri, jangan berdiri di sini terus!"
            chiasa "Siap, Senpai. Nanti besok kukembalikan lagi ke meja ini ya."
            nagisa "Awas kalau sampai hilang atau bengkok ujungnya!"
        else:
            yutaka "Eh, boneka kelinci putih yang kamu peluk di foto itu si Koko kan? Yang dulu sering kamu bawa main ke rumah? Masih ada di kamarmu sampai sekarang?"
            nagisa "Masih ada lah, masa dibuang begitu aja. Masih rapi di sudut kasurku kok."
            nar "Nagisa meletakkan kembali lembar foto itu di atas buku referensinya, lalu menyentuh tepi gambarnya dengan ibu jari. Nada suaranya yang tadi tinggi perlahan melunak."
            nagisa "Koko ini... dulu Ko-kun yang menangin di stan lempar gelang waktu festival dekat kuil."
            yutaka "Oh, waktu kita masih kelas empat SD itu ya? Kukira dulu kamu menang sendiri."
            nagisa "Mana sempat aku main, waktu itu aku malu mau bilang pengin boneka kelinci di rak atas, jadi aku cuma berdiri diam pura-pura lihat lampu stan. Padahal dalam hati pengin banget."
            yutaka "Pantas aja kita berhenti lama sekali di depan stan itu dulu."
            nar "Senyum kecil yang hangat muncul di wajah Nagisa saat matanya menatap foto lama tersebut."
            nagisa "Aku pikir nggak ada yang sadar. Eh, ternyata Ko-kun lihat aku bolak-balik melirik kelinci itu. Begitu kita jalan ke stan sebelah, dia diam-diam balik lagi ke stan lempar gelang dan menghabiskan uang sakunya buat beli kupon tambahan sampai akhirnya menang. Itu yang bikin aku senang banget sampai sekarang, karena ternyata dia ingat apa yang kumau tanpa perlu kuminta."
            yutaka "Pantas aja di foto itu kamu meluk kelincinya kencang banget sambil senyum paling lebar di antara kita berempat."
            nar "Mendengar godaan ringanmu, Nagisa langsung tersadar bahwa ia baru saja bicara terlalu jujur. Pipinya langsung memerah padam, dan ia buru-buru menutup buku tebalnya."
            nagisa "J-jangan salah paham! Lagian waktu itu tiket mainan stannya juga murah banget kok, cuma beberapa ratus yen! Siapa aja juga bisa dapat kalau lemparannya lagi beruntung!"
            yutaka "Iya deh, iya, murah kok, Nagisa. Padahal zaman kelas empat SD uang jajan segitu bisa buat beli dua mangkuk takoyaki."
            nagisa "Berisik! Nggak usah pakai hitungan harga takoyaki segala! Itu kan sudah lama sekali!"
            yutaka "Oke, oke, nggak kubawa-bawa lagi soal takoyaki."
            nagisa "Mana flashdisk catatanku yang kamu pinjam kemarin? Taruh aja di meja, nggak usah senyum-senyum begitu!"
            yutaka "Ini kutaruh di sebelah kotak pensilmu ya. Terima kasih pinjamannya."
            nagisa "Sama-sama. Sekarang cepat sana keluar sebelum aku lempar penghapus!"
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Telinga kelincinya kepanjangan banget sampai hampir keluar dari foto. Kalau sudah disimpan dari zaman SD, sekarang pasti bonekanya sudah lusuh dan kempes banget ya, Nagisa-senpai?"
            nagisa "Heh! Enak aja mulutmu bilang Koko lusuh! Namanya juga sudah kupelihara bertahun-tahun di kamar!"
            nar "Nagisa langsung merengut tajam dan menempelkan kedua telapak tangannya tepat di atas foto tersebut, menutupi gambar Koko seolah khawatir boneka di dalam cetakan kertas itu ikut tersinggung mendengar ucapanmu."
            nagisa "Asal kamu tahu ya, boneka baru yang dipajang rapi di etalase toko belum tentu kuat nemenin aku begadang dan dengerin aku mengomel soal revisi tugas tiap malam! Tiap sebulan sekali selalu kucuci tangan pakai sabun lembut, terus kalau ada benang telinganya yang kendur langsung kujahit sendiri pakai benang katun putih, jadi masih bersih dan rapi!"
            chiasa "Wah, sampai ditutupin pakai dua tangan segala fotonya, plus ada jadwal perawatan rutin segala. Segitu sayangnya ya sama Koko, Senpai?"
            nar "Nagisa menunduk melihat kedua tangannya sendiri yang sedang memayungi selembar kertas foto di atas buku. Ia terdiam dua detik, lalu mendadak tertawa kecil menertawakan tingkahnya sendiri."
            nagisa "Aduh... ngapain juga aku sampai nutupin foto kertas segala. Konyol banget sih aku."
            chiasa "Nggak konyol kok, justru kelihatan kalau Senpai beneran sayang dan telaten sama barang pemberian."
            nagisa "Diam! Dengar ya, Chiasa! Awas aja kalau besok-besok kamu bocorin ke Ko-kun atau anak-anak lain soal aku masih menaruh Koko di kasur sampai sekarang!"
            chiasa "Kenapa memangnya kalau ketahuan?"
            nagisa "Malu tahu! Pokoknya kalau sampai bocor, bakal kubilang ke satu kampus kalau kamu di rumah masih suka ngajak boneka ngobrol sebelum tidur!"
            chiasa "Lho, kok malah aku yang kena fitnah sih, Senpai?"
            nagisa "Biar adil dan kamu nggak macam-macam! Sudah sana ambil penggaris besimu di meja sebelah, sebentar lagi aku mau beres-beres keluar!"
        else:
            yutaka "Telinga kelincinya kepanjangan banget sampai hampir nggak muat di bingkai foto. Kalau disimpan dari zaman SD, sekarang pasti bonekanya sudah buluk dan kempes banget ya, Nagisa?"
            nagisa "Heh! Sembarangan banget bilang Koko buluk! Namanya juga sudah dirawat bertahun-tahun!"
            nar "Nagisa langsung mengernyit kesal dan menempelkan kedua telapak tangannya tepat di atas gambar Koko di foto tersebut, seperti sedang memasang tameng agar bonekanya tidak diejek."
            nagisa "Boneka baru di toko mainan juga belum tentu tahan dengerin keluhanku soal revisi gambar sampai tengah malam tahu! Lagian tiap sebulan sekali selalu kucuci bersih pakai tangan, kalau ada jahitan telinganya yang lepas juga langsung kujahit ulang sendiri!"
            yutaka "Haha, sampai ditutupin pakai dua tangan begitu fotonya. Segitu berharganya ya kelinci satu itu?"
            nar "Nagisa melirik tangannya sendiri yang sedang menempel rapat di atas selembar foto lama. Ia tertegun sejenak, lalu akhirnya tertawa pendek merasa geli sendiri."
            nagisa "Aduh... konyol banget aku, masa foto kertas aja ikut kulindungi dari omonganmu."
            yutaka "Tenang aja, aku cuma bercanda kok. Hebat juga kamu masih merawatnya serapi itu."
            nagisa "Awas aja ya, Yutaka! Kalau sampai kamu ember cerita ke anak-anak kampus soal aku masih menyimpan Koko di kamar sampai sekarang..."
            yutaka "Kalau sampai keceplosan memangnya kamu mau ngapain?"
            nagisa "Bakal kusebarin ke semua orang kalau kamu tiap malam masih suka ngajak mainan robot ngobrol sendiri di apartemen!"
            yutaka "Lah, kok jadi aku yang kena fitnah aneh-aneh?"
            nagisa "Makanya tutup mulutmu rapat-rapat! Sudah, taruh flashdisk-nya di meja, aku mau beres-beres tas keluar!"
    else:
        if kk_host == "chiasa":
            nar "Kamu tidak melontarkan godaan dan tidak pula mengorek cerita soal boneka di pelukannya. Kamu hanya berdiri tenang di samping meja gambarnya, ikut memandangi foto empat anak kecil di depan gerbang festival itu dalam keheningan studio yang teduh."
            nar "Karena kamu tidak mengejeknya, Nagisa perlahan menurunkan tangannya yang tadi hendak menyembunyikan foto tersebut. Selama beberapa saat hanya terdengar deru samar kendaraan dari jalan raya di luar kampus sementara mata Nagisa menelusuri wajah keempat anak di dalam foto satu per satu."
            nagisa "...Waktu foto ini diambil Ayah dulu, rasanya kalau kita sudah besar nanti semuanya bakal tetap persis kayak gini terus ya, Chiasa."
            chiasa "Memangnya menurut Senpai sekarang kita sudah beda jauh? Kita berempat kan masih kuliah di kampus yang sama, masih sering ketemu juga."
            nagisa "Ya masih satu kampus sih... cuma rasanya tetap beda, Chi-chan. Waktu masih SD dulu semuanya kelihatan gampang banget. Kalau pengin main atau ada apa-apa, tinggal lari ketok pintu pagar rumah sebelah tanpa mikir dua kali."
            chiasa "Sekarang rasanya lebih banyak hal yang harus dipertimbangkan dulu ya sebelum mengetuk pintu?"
            nar "Nagisa menghela napas pelan sambil merapikan tepi foto yang sedikit melengkung dengan jarinya."
            nagisa "Iya. Dulu kita berempat bahkan nggak pernah kepikiran kalau suatu hari nanti masing-masing bakal tumbuh ke arah yang beda-beda, punya kesibukan sendiri, dan kenal orang-orang baru yang dulunya nggak ada di foto ini."
            chiasa "Tapi buktinya foto itu masih Senpai bawa terus di buku kuliah sampai hari ini."
            nagisa "Cuma buat pembatas halaman kok... biar nggak lupa aja dari mana kita semua mulai bareng."
            chiasa "Kalau begitu jangan sampai fotonya hilang ya, Senpai."
            nagisa "Nggak bakal hilang, selalu kuselipkan di halaman tengah."
            nar "Nagisa tersenyum tipis, menyelipkan kembali foto itu dengan sangat hati-hati di halaman bukunya, lalu mengambilkan penggaris skala besi dari kotak alatnya dan menyerahkannya ke tanganmu."
        else:
            nar "Kamu tidak melontarkan ledekan apa pun dan tidak mendesaknya bercerita. Kamu hanya menaruh flashdisk di sudut mejanya, lalu bersandar santai di tepi meja gambar sebelah sambil ikut memandangi foto lama itu dalam diam."
            nar "Melihatmu tidak berniat menggodanya, bahu Nagisa yang tadinya siaga perlahan mengendur. Di tengah keheningan ruang studio itu, tatapannya menyusuri wajah keempat anak kecil di dalam foto tersebut satu demi satu."
            nagisa "...Waktu kita berempat difoto di depan gerbang kuil ini dulu, rasanya sampai tua nanti kita bakal tetap kayak gitu terus ya, Yutaka."
            yutaka "Sekarang juga kita berempat masih di universitas yang sama kan, masih sering kumpul juga."
            nagisa "Memang masih sering ketemu. Cuma waktu kecil dulu rasanya semuanya jauh lebih sederhana. Kalau pengin mengajak main atau makan es krim bareng, tinggal teriak di depan gerbang tanpa harus menebak jadwal atau isi kepala masing-masing."
            yutaka "Sekarang memang nggak sesederhana zaman SD lagi ya."
            nagisa "Iya. Dulu kita nggak pernah kepikiran kalau waktu sudah kuliah begini, semua orang pelan-pelan bisa jalan ke arah yang beda dan punya pikiran yang nggak bisa ditebak lagi."
            yutaka "Tapi foto zaman SD itu masih kamu pakai terus buat pembatas buku sampai sekarang."
            nagisa "Kebetulan aja ukurannya pas buat menandai halaman buku tebal... sekalian buat pengingat."
            yutaka "Jaga baik-baik biar nggak terlipat di dalam tasmu."
            nagisa "Tenang aja, aku selalu taruh di halaman tengah biar aman."
            nar "Nagisa tersenyum kecil, menyelipkan kembali foto itu dengan rapi ke sela halaman bukunya, lalu menutup sampulnya perlahan sebelum mulai mengemasi alat gambarnya ke dalam tas."
    return

# ┌─ PANDUAN CERITA · N07 · Natal: Koko
# │ LOKASI  : Hunian Biasa · Rumah Sakurajima
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : ia memeluk Koko.
# │ INTI    : A ada di sana / B pergi / C bawa Koita.
# │ AKHIRAN : hub besar #3.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N07:
    call kk_scene_enter("nagisa", "Rumah Sakurajima · Natal")
    if kk_host == "chiasa":
        nar "Ruang tengah rumah keluarga Sakurajima malam itu terasa lengang karena kedua orang tua Nagisa sedang pergi ke acara makan malam kerabat, sementara Kak Haruto masih terjebak lembur akhir tahun di kantornya. Lampu ruang makan menyala hangat di atas meja kayu yang sudah bersih dari tumpukan kertas kuliah."
        nar "Di tengah meja, terhidang satu loyang kue bolu Natal berlapis krim kocok putih dan potongan buah stroberi segar yang belum dipotong."
        if kk_has("koko_dikenal"):
            nar "Tepat di kursi kayu sebelah kanan Nagisa, duduk Koko, boneka kelinci putih bertelinga panjang hadiah festival masa kecilnya yang disandarkan rapi memakai bantal kursi."
            nagisa "Kamu masih ingat Koko kan, Chiasa? Tiap malam Natal kalau orang rumah lagi pada keluar begini, dia selalu kubawa turun dari kamar terus kududukkan di kursi sebelah biar meja makannya nggak kelihatan kosong."
        else:
            nar "Tepat di kursi kayu sebelah kanan Nagisa, duduk sebuah boneka kelinci putih bertelinga panjang bernama Koko. Salah satu jahitan benang di pangkal telinganya tampak jauh lebih baru dan bersih dibandingkan bulu kain tubuhnya yang sudah sering dicuci."
        nar "Ketika kamu melangkah mendekati meja, pandanganmu tertuju pada dua piring keramik kecil dan dua garpu perak yang sudah diletakkan bersebelahan di dekat kotak kue, lengkap dengan pisau kue yang belum terpakai. Menyadari arah matamu, Nagisa langsung menegakkan punggung dan menyilangkan lengan di depan dadanya."
        nagisa "J-jangan salah paham dulu lihat piringnya ada dua! Piring kedua itu cuma kusimpan di meja buat jaga-jaga, tahu! Aku cuma malas aja kalau nanti tiba-tiba Kak Haruto pulang cepat atau ada orang mampir, terus aku harus bolak-balik lagi ke dapur ambil piring bersih!"
        chiasa "Aku kan baru masuk dan belum komentar satu kata pun soal piringnya, Nagisa-senpai."
        nagisa "Nggak usah ngomong juga kelihatan dari cara kamu ngelirik mejanya! Sudut bibirmu tuh barusan sudah mau naik buat ngeledek aku, kan?! Pokoknya nggak usah senyum-senyum kayak gitu!"
    else:
        nar "Ruang makan rumah keluarga Sakurajima malam itu terasa lebih senyap daripada biasanya karena orang tua Nagisa sedang menghadiri jamuan kerabat, sedangkan Kak Haruto masih lembur akhir tahun di kantor. Di bawah lampu gantung yang hangat, meja kayu panjang sudah bersih dan di tengahnya terhidang satu loyang kue bolu Natal berlapis krim putih dan potongan stroberi segar yang masih utuh."
        if kk_has("koko_dikenal"):
            nar "Tepat di kursi kayu di samping kanan Nagisa, duduk Koko, boneka kelinci putih bertelinga panjang hadiah festival masa kecilnya yang disandarkan rapi pada bantal kursi."
            nagisa "Kamu masih ingat Koko kan, Yutaka? Tiap malam Natal kalau rumah lagi sepi begini, dia selalu kubawa turun terus kududukkan di kursi sebelah biar mejanya nggak kelihatan kosong banget."
        else:
            nar "Tepat di kursi kayu sebelah kanan Nagisa, duduk sebuah boneka kelinci putih bertelinga panjang bernama Koko. Salah satu jahitan benang di pangkal telinganya terlihat jauh lebih baru dan bersih dibandingkan bulu kain tubuhnya yang sudah sering dicuci."
        nar "Ketika kamu melangkah mendekat sambil melepas syal, matamu langsung tertumbuk pada dua piring keramik kecil, dua garpu perak, dan pisau kue yang sudah ditata rapi di tepi meja. Menyadari pandanganmu berhenti di sana, Nagisa segera menyilangkan lengannya di depan dada dengan wajah sedikit memerah."
        nagisa "H-hei, jangan pasang muka mau ngeledek dulu ya, Yutaka! Piring kedua itu cuma kusimpan di meja buat jaga-jaga! Aku cuma malas aja kalau nanti tiba-tiba Kak Haruto pulang cepat atau ada yang mampir, terus aku harus repot potong kue dua kali!"
        yutaka "Aku bahkan belum buka mulut sama sekali lho, Nagisa."
        nagisa "Nggak usah ngomong juga kelihatan dari cara sudut bibirmu naik barusan! Pokoknya nggak usah senyum-senyum mencurigakan begitu!"
    call kk_family_menu("N07", ["\"Kebetulan piringnya sudah dua, aku temani makan kuenya di sini ya.\"", "\"Maaf, aku cuma mampir sebentar karena masih ada urusan lain malam ini.\"", "\"Tunggu sebentar, biar sekalian kutelepon dan kuajak Koita ke sini juga.\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Kebetulan piringnya sudah telanjur disiapkan dua di meja, aku temani makan kuenya di sini aja ya, Nagisa-senpai. Sayang banget kalau piring keduanya beneran nganggur sampai malam."
            nar "Nagisa terdiam sesaat, lalu membuang napas pendek lewat hidung sambil menarik pisau kue dari samping kotak agar wajah leganya tidak terlalu kentara."
            nagisa "Hmph. Ya sudah kalau kamu memang maksa mau numpang makan kue di sini. Duduk di kursi seberang situ, biar kubuatin teh hangat dulu."
            chiasa "Jangan potong gede-gede buatku ya, Senpai, tadi sore aku sudah sempat ngemil roti soalnya."
            nagisa "Cerewet ah, lihat aja nanti."
            nar "Nagisa mulai mengiris bolu Natal itu menjadi dua potongan. Tangan kirinya yang menahan piring tampak sedikit ragu menakar garis tengah, sehingga hasil potongannya sama sekali tidak seimbang. Satu iris tampak lebar dengan dua buah stroberi utuh dan cokelat bertuliskan selamat Natal di atasnya, sedangkan iris satunya jauh lebih ramping."
            nar "Sebelum kamu sempat menunjuk piring yang kecil, Nagisa sudah lebih dulu menyambar piring berpotongan tipis itu ke hadapannya sendiri dan mendorong potongan yang besar ke depanmu."
            nagisa "Jangan mulai debat soal ukuran kue juga! Kamu itu tamu di rumahku malam ini, jadi makan aja bagian yang besar. Masa tuan rumah ngasih potongan kecil ke tamu."
            chiasa "Padahal dari kecil Senpai paling rewel kalau nggak kebagian lempengan cokelat yang ada tulisannya itu."
            nagisa "Itu kan waktu masih SD! Sekarang aku sudah kuliah, nggak bakal nangis cuma gara-gara lempengan cokelat. Sudah, makan aja selagi tehnya masih panas!"
            chiasa "Kalau gitu cokelat tulisannya kita patah bagi dua aja nih. Setengah buat Senpai, setengah buatku."
            nar "Kamu mematahkan kepingan cokelat di atas krim itu dan menaruh separuhnya di piring Nagisa. Nagisa sempat memelototimu singkat sebelum akhirnya memakan potongan cokelat itu tanpa protes lagi. Sepuluh menit kemudian, setelah piring pertamanya bersih, ia mengiris satu potong tambahan untuk dirinya sendiri sambil mengobrol santai soal rencana liburan musim dingin."
            nagisa "...Eh, Chiasa. Makasih ya sudah mau tinggal makan kue bareng di sini malam ini. Sudah, cukup! Nggak usah senyum-senyum dan jangan minta aku ngulang kalimat barusan!"
        else:
            yutaka "Kebetulan piringnya sudah telanjur kamu siapkan dua, ya sudah, aku temani makan kuenya di sini aja, Nagisa. Sayang kan kalau piring satunya nganggur sampai tengah malam."
            nar "Nagisa mendengus kecil, lalu cepat-cepat meraih pisau kue di samping kotak agar ekspresi leganya tidak terlalu kentara."
            nagisa "Hmph. Ya sudah kalau kamu memang lagi nggak ada kerjaan dan mau numpang makan kue di sini. Duduk di seberang situ, biar kubuatin teh hangat dulu."
            yutaka "Potongin bagian yang nggak usah gede-gede ya buatku, tadi sore aku sudah sempat makan berat."
            nagisa "Banyak maunya banget sih, duduk diam aja di situ."
            nar "Nagisa mengiris bolu krim itu menjadi dua potongan yang sama sekali tidak sama besarnya. Satu bagian tampak tebal dengan dua buah stroberi utuh dan lempengan cokelat bertuliskan selamat Natal, sedangkan bagian lainnya jauh lebih tipis."
            nar "Sebelum kamu sempat mengangkat tangan menunjuk piring yang lebih kecil, Nagisa sudah lebih dulu menarik potongan tipis itu ke hadapannya sendiri dan mendorong piring besar ke depanmu."
            nagisa "Kamu itu tamu malam ini. Jangan mulai debat soal ukuran kue juga, makan aja bagian yang besar!"
            yutaka "Lho, padahal dulu waktu kita masih SD, kamu yang paling ngamuk kalau nggak dapat lempengan cokelat tulisannya."
            nagisa "Itu kan sepuluh tahun yang lalu, bodoh! Sekarang aku sudah kuliah, nggak bakal ribut cuma gara-gara kepingan cokelat! Sudah, makan aja selagi tehnya masih panas!"
            yutaka "Iya, iya. Nih, cokelat tulisannya kupatah bagi dua biar adil. Separuh buatmu, separuh buatku."
            nar "Kamu mematahkan lempengan cokelat di atas krim lalu meletakkan setengahnya di piring Nagisa. Ia sempat melirik tajam ke arahmu, tetapi tetap mengambilnya dan makan tanpa membalas omelan. Sepuluh menit kemudian, setelah piring pertamanya kosong, ia santai saja mengiris satu potong lagi untuk dirinya sendiri tanpa perlu lagi berpura-pura bahwa dua piring tadi cuma kebetulan."
            nagisa "...Hei, Yutaka. Makasih ya sudah mau tinggal di sini malam ini. Itu saja. Jangan senyum-senyum dan jangan pernah minta aku mengulangnya!"
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Maaf ya, Nagisa-senpai. Aku tadi mampir ke sini cuma mau kasih salam Natal sebentar, habis ini masih ada urusan lain yang harus kuberesin malam ini."
            nar "Jari Nagisa yang tadinya sudah menyentuh gagang pisau kue perlahan ditarik kembali. Ia langsung berdiri tegak, merapikan ujung kardigannya dengan cepat seolah sejak awal tidak pernah berharap kamu duduk lama."
            nagisa "Oh, masih ada urusan lain ya. Bilang dong dari tadi kalau cuma mampir sebentar. Tunggu di situ satu menit, jangan keluar pintu dulu."
            chiasa "Eh, mau ambil apa, Senpai?"
            nar "Nagisa tidak menjawab dan langsung melangkah cepat ke dapur. Tak lama kemudian ia kembali membawa sebuah kotak mika plastik kecil, memotong seperempat bagian kue bolu stroberi itu dengan cekatan, lalu memasukkannya ke dalam kotak dan mengikatnya dengan kantong plastik bersih."
            nagisa "Nih, bawa pulang."
            chiasa "Lho, kok malah dibungkusin buatku, Senpai? Nanti kue di rumah Senpai tinggal sedikit."
            nagisa "Ambil aja, nggak usah banyak alasan! Jangan kepedean mikir ini bekal perpisahan dramatis atau apa ya. Kalau nggak kamu bawa sebagian sekarang, nanti aku yang terpaksa ngabisin satu loyang penuh sendirian terus pipiku tambah tembam habis liburan!"
            chiasa "Haha, iya deh. Makasih banyak ya kuenya, Nagisa-senpai. Selamat Natal."
            nagisa "...Iya. Selamat Natal juga, Chiasa. Jalanan depan agak licin kena embun malam, hati-hati jalannya."
            nar "Ia mengantarmu sampai ke pintu genkan dengan suara yang lebih pelan daripada saat menyambutmu tadi. Ketika kamu menutup pintu geser luar dan sempat menoleh sekilas lewat kaca buram serambi, kamu melihat Nagisa berjalan kembali ke meja makan, mengambil piring kedua yang masih kosong untuk dibawa masuk ke bak cuci dapur, sementara Koko tetap duduk diam di kursi kayu sebelahnya."
        else:
            yutaka "Maaf ya, Nagisa. Aku mampir ke sini cuma buat ngucapin selamat Natal sebentar, habis ini masih ada urusan lain yang harus kuurus malam ini."
            nar "Tangan Nagisa yang tadi hampir menyentuh gagang pisau kue langsung ditarik mundur. Ia menegakkan punggung dan merapikan ujung kardigannya dengan gerakan cepat seolah sejak awal tidak berniat menahanmu."
            nagisa "Oh, masih ada acara lain ya. Bilang dong dari awal kalau cuma numpang lewat sebentar. Tunggu di situ dulu, jangan langsung kabur keluar pintu."
            yutaka "Mau ambil apa lagi?"
            nar "Tanpa menjawab, Nagisa berjalan cepat ke dapur lalu kembali membawa kotak mika bening. Ia memotong seperempat bagian kue stroberi itu dengan rapi, menutup kotaknya, lalu memasukkannya ke kantong plastik kecil."
            nagisa "Nih, bawa pulang ke apartemenmu."
            yutaka "Lho, kok malah dibungkusin? Nanti jatahmu sendiri tinggal sedikit."
            nagisa "Sudah bawa aja, nggak usah banyak komentar! Ini bukan bekal perpisahan dramatis atau apa ya, jangan kelewat percaya diri. Kalau nggak kamu bawa sebagian sekarang, nanti aku sendiri yang terpaksa ngabisin satu loyang sendirian!"
            yutaka "Haha, oke-oke, kuterima deh. Makasih ya kuenya, Nagisa. Selamat Natal."
            nagisa "...Iya. Selamat Natal juga, Yutaka. Hati-hati di jalan, angin malam ini dingin banget."
            nar "Ia mengantarmu sampai ke pintu depan dengan suara yang jauh lebih pelan daripada saat mengomel tadi. Saat kamu melangkah keluar pagar dan sempat menoleh sekali lewat celah kaca serambi, kamu melihat Nagisa memindahkan piring kedua yang masih bersih dari meja makan ke dapur, sementara Koko tetap duduk sendirian di kursinya."
    else:
        if kk_host == "chiasa":
            chiasa "Kuenya masih utuh satu loyang gede gini, sayang kalau cuma dimakan berdua. Tunggu sebentar ya, Nagisa-senpai, biar sekalian kutelepon Ko-nii dan kuajak nyusul ke sini sekarang."
            nar "Kamu langsung mengeluarkan ponsel dari saku mantel dan membuka kontak Koita. Seketika wajah Nagisa memerah sampai ke leher; ia melangkah maju setengah panik hendak menahan pergelangan tanganmu."
            nagisa "Eh, tunggu dulu, Chiasa! Jangan ngawur! Nggak usah telepon Ko-kun segala malam-malam begini! Nanti dia malah mikir aku yang nyuruh kamu ngundang dia ke rumahku!"
            chiasa "Kan memang aku yang ngajak, Senpai. Halo, Ko-nii? Aku lagi di rumah Nagisa-senpai nih. Di sini ada kue bolu Natal satu loyang penuh belum dipotong, Ko-nii belum makan kue kan? Sini nyusul jalan kaki sebentar!"
            nar "Di seberang telepon, suara Koita terdengar kaget sebentar lalu langsung menyanggupi dengan nada hangat bahwa ia akan segera mengunci rumah dan menyusul dalam sepuluh menit. Selama kamu berbicara di telepon, Nagisa berdiri kaku di sebelahmu sambil menahan napas, dan begitu sambungan ditutup, ia sudah terlambat menyembunyikan senyum cerah yang langsung merekah di bibirnya."
            chiasa "Nah, Ko-nii bilang sepuluh menit lagi sampai sini, Senpai."
            nagisa "D-dasar kamu itu ya, dari dulu hobi banget ngatur-ngatur seenaknya sendiri! Kalau Ko-kun beneran ikut datang ke sini, berarti piring sama garpu di meja kurang satu dong! Tunggu sebentar, aku ambil piring ketiga sama seduh teh baru dulu di dapur!"
            chiasa "Mau kubantu bawa cangkirnya?"
            nagisa "Nggak usah, kamu duduk aja di situ jangan berantakin meja!"
            nar "Nagisa setengah berlari ke dapur dengan langkah yang jauh lebih ringan, lalu kembali membawa piring ketiga beserta teko teh hangat. Saat melewati jendela kaca ruang tengah yang gelap, ia sempat berhenti dua detik untuk merapikan poni dan ikatan rambut kembarnya di pantulan kaca."
            nar "Ia tetap menuangkan teh pertama untukmu dan menyodorkannya dengan ramah, tetapi begitu bunyi bel pintu depan berdenting menandakan kedatangan Koita, perhatian dan kursi terdekat di meja itu langsung kembali terisi oleh harapan lamanya."
        else:
            yutaka "Kue segede ini masih utuh satu loyang, sayang banget kalau cuma kita berdua yang makan. Tunggu sebentar, biar sekalian kutelepon Koita suruh nyusul ke sini."
            nar "Kamu langsung merogoh ponsel dari saku mantel dan memencet nomor Koita. Wajah Nagisa seketika memerah sampai ke daun telinga; ia melangkah maju setengah panik mencoba menggapai lenganmu."
            nagisa "Hei, Yutaka! Jangan seenaknya sendiri dong! Nggak usah telepon Ko-kun segala malam-malam begini! Nanti dia malah mikir aku yang nyuruh kamu ngundang dia ke rumahku!"
            yutaka "Kan memang aku yang nelpon, santai aja. Halo, Koita? Aku lagi di rumah Nagisa nih. Di sini ada kue bolu Natal utuh satu loyang belum disentuh, kamu belum makan kue kan? Sini nyusul jalan kaki sebentar!"
            nar "Di ujung telepon, Koita terdengar agak terkejut lalu langsung menjawab antusias bahwa ia akan segera memakai jaket dan berjalan ke rumah Sakurajima dalam sepuluh menit. Sepanjang sambungan itu Nagisa berdiri kaku sambil menahan napas, dan begitu kamu mematikan telepon, ia sudah terlambat menyembunyikan senyum cerah yang langsung mengembang di wajahnya."
            yutaka "Beres. Sepuluh menit lagi dia sampai sini."
            nagisa "D-dasar tukang bikin heboh! Kalau Ko-kun beneran datang, berarti piring sama garpu di meja kurang satu dong! Tunggu situ sebentar, aku ambil piring ketiga sama seduh teh baru dulu ke dapur!"
            yutaka "Perlu kubantu bawain tekonya nggak?"
            nagisa "Nggak usah, kamu duduk manis aja di kursi jangan bikin mejanya berantakan!"
            nar "Nagisa melangkah cepat ke dapur lalu kembali membawa piring keramik ketiga dan teko teh panas. Ketika melewati kaca jendela ruang tengah yang gelap, langkahnya sempat berhenti dua detik untuk merapikan poni dan ikatan rambut pirang kembarnya di pantulan kaca."
            nar "Ia tetap menuangkan cangkir teh pertama untukmu dan menaruhnya dengan sopan. Begitu bel pintu depan berbunyi menandakan Koita telah tiba, perhatian dan kursi terdekat di sisi meja itu kembali sepenuhnya menjadi milik harapan lamanya."
    return

# ┌─ PANDUAN CERITA · N08 · Coklat Gosong
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : Valentine; coklat untuk Koita gosong.
# │ INTI    : A makan / B bantu buat ulang / C ambil alih.
# │ AKHIRAN : C mengalihkan coklat ke pemain.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N08:
    call kk_scene_enter("nagisa", "Studio Arsitektur · Valentine")
    if kk_host == "chiasa":
        nar "Ruang Studio Arsitektur lantai dua di hari Valentine terasa lebih sepi daripada biasanya karena sebagian besar mahasiswa sedang keluar mencari makan atau berkumpul di pelataran gedung. Di meja gambar sudut belakang yang masih menyimpan bau samar lem maket, Sakurajima Nagisa duduk kaku memandangi sebuah kotak hadiah berwarna merah muda yang masih kosong melompong."
        nar "Di samping kotak itu tergeletak loyang aluminium kecil berisi potongan brownies cokelat yang pinggirannya menghitam keras, berdampingan dengan selembar resep cetak yang penuh coretan spidol merah dan tanda seru di bagian suhu oven. Begitu pintu studio berderit terbuka dan kamu melangkah masuk, Nagisa langsung panik menyambar beberapa lembar tisu untuk menutupi loyang tersebut."
        nar "Gerakannya jelas sudah terlambat karena aroma cokelat hangus yang menyengat sudah tercium sampai ke deretan meja tengah."
        chiasa "Nagisa-senpai... kok di dalam studio bau gosong banget sih? Ada kabel pemanas yang konslet ya?"
        nar "Wajah Nagisa langsung memerah sampai ke ujung telinga. Ia menekan lembaran tisu di atas loyang itu lebih keras, lalu akhirnya menghela napas panjang dengan bahu turun dan menatapmu ketus."
        nagisa "Nggak ada kabel konslet! Iya, gosong! Cokelat buat Ko-kun gosong di bagian pinggirnya! Nah, puas kan? Sekarang kamu sudah tahu dua hal sekaligus yang sama sekali nggak perlu diumumkan ke seluruh studio!"
        chiasa "Padahal aku cuma nanya bau gosongnya dari mana, Senpai."
        nagisa "Sudah deh, nggak usah pura-pura polos! Tadi pagi di rumah aku terlalu buru-buru nyetel pemanggang gara-gara takut telat masuk kelas struktur, eh malah lupa kecilin suhunya lima menit terakhir."
        nar "Nagisa mengambil kotak hadiah merah muda yang masih kosong itu, memutar-mutarnya di tangan dengan bibir terkatup kesal. Ia tampak jelas sedang menimbang apakah harga dirinya masih lebih mudah diselamatkan dengan lari membeli cokelat jadi di toko dekat stasiun, atau sekalian menyerah tidak memberi apa-apa tahun ini."
    else:
        nar "Ruang Studio Arsitektur lantai dua di hari Valentine terasa jauh lebih sepi daripada biasanya karena sebagian besar mahasiswa sedang keluar mencari makan atau berkumpul di pelataran gedung. Di meja gambar sudut belakang yang masih menyimpan bau samar lem maket, Sakurajima Nagisa duduk kaku memandangi sebuah kotak hadiah merah muda yang masih kosong melompong."
        nar "Di samping kotak itu tergeletak loyang aluminium kecil berisi potongan brownies cokelat yang pinggirannya menghitam keras, berdampingan dengan selembar resep cetak penuh coretan spidol merah dan tanda seru di bagian suhu oven. Begitu pintu studio berderit terbuka dan kamu melangkah masuk, Nagisa langsung panik menyambar beberapa lembar tisu untuk menutupi loyang tersebut."
        nar "Gerakannya jelas sudah terlambat karena aroma cokelat hangus yang menyengat sudah lebih dulu memenuhi ruangan sampai ke meja tengah."
        yutaka "Nagisa, ini di dalam studio ada alat pemotong kayu yang kebakar atau gimana sih? Bau gosongnya nyengat banget sampai pintu."
        nar "Wajah Nagisa langsung memerah sampai ke ujung telinga. Ia menekan lembaran tisu di atas loyang itu lebih keras, lalu akhirnya menghela napas panjang dengan bahu turun dan menatapmu ketus."
        nagisa "Nggak ada alat yang kebakar! Iya, gosong! Cokelat buat Koita gosong di bagian pinggirnya! Nah, puas kan? Sekarang kamu sudah tahu dua hal sekaligus yang sama sekali nggak perlu diumumkan ke seluruh studio!"
        yutaka "Santai aja, aku juga nggak niat bikin pengumuman lewat pengeras suara. Kok bisa sampai gosong begini sih?"
        nagisa "Tadi pagi di rumah aku buru-buru nyetel pemanggang gara-gara takut telat masuk kelas struktur, eh malah lupa kecilin suhunya lima menit terakhir."
        nar "Nagisa mengambil kotak hadiah merah muda yang masih kosong itu, memutar-mutarnya di tangan dengan bibir terkatup kesal. Ia tampak jelas sedang menimbang apakah harga dirinya masih lebih mudah diselamatkan dengan lari membeli cokelat jadi di toko dekat stasiun, atau sekalian menyerah tidak memberi apa-apa tahun ini."
    call kk_family_menu("N08", ["\"Sini aku cicipi dulu bagian tengahnya, kayaknya masih bisa dimakan kok.\"", "\"Masih sempat kok kalau mau bikin ulang satu loyang lagi. Biar aku bantu.\"", "\"Kalau gagal buat dikasih ke dia, mending bikin buat aku aja gimana?\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Jangan buru-buru dibuang dulu, Nagisa-senpai. Sini aku cicipi bagian tengahnya dulu, kayaknya yang hitam cuma pinggirannya aja kok."
            nagisa "Eh, tunggu dulu, Chiasa! Jangan sembarangan makan nanti sakit perut—"
            nar "Sebelum Nagisa sempat menarik loyang itu menjauh, kamu sudah menyingkirkan tisu di atasnya, mematahkan satu potongan kecil dari bagian tengah yang warnanya masih cokelat tua, lalu langsung memasukkannya ke mulut."
            nar "Nagisa langsung terdiam sambil menahan napas, menatapmu dengan mata biru melebar setengah cemas menunggu reaksimu. Kamu mengunyah perlahan sampai habis, lalu menatapnya lurus-lurus."
            chiasa "Pinggirnya memang pahit banget kayak kopi hangus, Senpai. Tapi bagian tengahnya masih agak manis kok, cuma teksturnya memang agak kering sama keras sedikit."
            nar "Alih-alih tersinggung mendengar penilaian jujurmu, ketegangan di wajah Nagisa mendadak buyar. Keluar tawa pendek yang tak tertahan dari bibirnya sambil ia menutup wajah sebelah tangan."
            nagisa "Haha... bagus deh kamu jujur bilang pahit! Kalau tadi kamu nekat muji bilang enak banget cuma supaya aku senang, aku malah langsung tahu kamu bohong dan bakal tambah kesel!"
            chiasa "Ya masa gosong begini kubilang rasa toko kue bintang lima."
            nagisa "Iya juga sih. Nih, tunggu sebentar."
            nar "Nagisa mengambil sendok plastik bersih dari tasnya, menyingkirkan bagian pinggiran yang menghitam ke atas tisu, lalu mendorong loyang berisi potongan bagian tengah itu ke depanmu dan ikut mencicipi satu potong kecil sendiri."
            nagisa "Hm... beneran pahit di belakangnya ya. Ya sudah, kalau kamu masih mau ambil lagi, habisin aja bagian tengahnya daripada mubazir kubuang."
            chiasa "Makasih, Senpai. Eh, coba lihat lembar resepnya deh, kok tadi bisa gosong di lima menit terakhir?"
            nar "Kalian duduk berdampingan di bangku studio sambil memakan sisa brownies yang tidak sempurna itu dan menertawakan coretan tanda seru di kertas resep Nagisa yang ternyata keliru mengira suhu derajat pemanggang."
        else:
            yutaka "Jangan langsung dibuang dulu, Nagisa. Sini kucicipi bagian tengahnya, kayaknya yang hitam cuma pinggirannya aja."
            nagisa "Eh, tunggu dulu, Yutaka! Jangan asal makan nanti malah sakit perut—"
            nar "Sebelum Nagisa sempat menarik loyang itu menjauh, kamu sudah menyingkirkan tisu di atasnya, mematahkan satu potongan kecil dari bagian tengah yang masih berwarna cokelat tua, lalu langsung memasukkannya ke mulut."
            nar "Nagisa langsung terdiam sambil menahan napas, menatapmu dengan mata biru melebar cemas menunggu komentarmu. Kamu mengunyah perlahan sampai tandas, lalu menatapnya lurus-lurus."
            yutaka "Pinggirnya sih beneran pahit kayak arang kopi, Nagisa. Tapi bagian tengahnya masih agak manis kok, cuma agak kering sama padat sedikit."
            nar "Alih-alih tersinggung, ketegangan di wajah Nagisa langsung buyar. Keluar tawa pendek yang tak tertahan dari bibirnya sambil ia menutup wajah sebelah tangan."
            nagisa "Haha... bagus deh kamu jujur bilang pahit! Kalau tadi kamu sok muji bilang enak sekali cuma biar aku senang, aku malah langsung tahu kamu bohong dan bakal tambah kesel!"
            yutaka "Memangnya kapan aku pernah muji masakan gosong jadi enak."
            nagisa "Iya juga sih, mulutmu kan memang selalu blak-blakan. Nih, tunggu sebentar."
            nar "Nagisa mengambil sendok plastik bersih dari tasnya, menyingkirkan pinggiran yang menghitam ke atas tisu, lalu mendorong loyang berisi potongan tengah itu ke depanmu dan ikut mencicipi satu potong sendiri."
            nagisa "Hm... iya ya, pahit di belakangnya. Ya sudah, habisin aja bagian tengahnya kalau kamu masih mau daripada kubuang percuma."
            yutaka "Oke, lumayan buat ganjal perut. Coba sini kulihat kertas resepmu, bagian mana yang bikin suhunya kebablasan?"
            nar "Kalian duduk berdampingan di bangku studio sambil menghabiskan sisa brownies yang tidak sempurna itu dan menertawakan coretan tanda seru di lembar resep Nagisa. Kegagalan hari itu tetap menyebalkan baginya, tetapi tidak lagi terasa memalukan."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Masih ada waktu kok sebelum jam pulang, Nagisa-senpai. Kita turun beli bahan cokelat baru di pasar swalayan depan gerbang, terus pinjam dapur kecil di ruang kegiatan mahasiswa buat bikin satu loyang lagi. Biar aku bantu."
            nar "Nagisa berkedip kaget, sempat hendak menolak secara otomatis karena gengsi, lalu melirik lagi ke kotak merah muda yang kosong di tangannya."
            nagisa "Kamu serius mau bantuin aku bikin ulang buat Ko-kun? Nggak lagi berniat nyabotase resepku kan, Chiasa?"
            chiasa "Kalau aku mau sabotase, mending kubiarin aja Senpai kasih loyang gosong itu ke Ko-nii. Ayo buruan mumpung tokonya belum ramai."
            nagisa "...Hmph. Ya sudah! Tapi dengar ya, di dapur nanti kamu cuma boleh ngerjain bagian yang kuminta! Jangan sekali-kali asal nambahin gula, mentega, atau ubah-ubah suhu pemanggang tanpa nanya aku dulu!"
            nar "Lima belas menit kemudian, kalian berdua sudah berdiri di depan meja dapur kecil ruang kegiatan mahasiswa dengan celemek pinjaman. Nagisa menyerahkan pisau dan talenan kepadamu untuk mencincang cokelat batangan sementara ia menyiapkan loyang baru, dan benar saja, sampai tiga kali ia mengingatkanmu agar tidak menambahkan bahan apa pun di luar takaran."
            chiasa "Iya, Senpai, aku cuma aduk menteganya pelan-pelan kok, nggak kutambah apa-apa."
            nagisa "Bagus! Tadi pagi tuh aku keliru pas mindahin ke oven. Kali ini harus dijaga terus di depan kaca pemanggang biar nggak lewat satu menit pun."
            nar "Begitu adonan masuk ke dalam pemanggang, kalian berdiri berdampingan memandangi lampu kuning di dalam oven kecil. Suasana dapur perlahan dipenuhi aroma cokelat panggang yang manis dan hangat. Nagisa mengembuskan napas panjang sambil menatap jarum pewaktu."
            nagisa "Aku nggak mau loyang yang ini gagal juga, Chiasa. Soalnya... ya sudahlah, kamu kan sudah tahu juga ini buat siapa."
            chiasa "Kali ini aromanya sudah pas banget kok, Senpai, nggak ada bau hangus sama sekali."
            nar "Tepat saat bunyi ting terdengar, Nagisa mengeluarkan loyang memakai sarung tangan kain. Permukaan browniesnya matang merata dan lembut. Setelah agak dingin, ia memotongnya dengan rapi, menatanya ke dalam kotak merah muda, lalu menatap kotak itu dengan senyum lega."
            nagisa "...Makasih banyak ya, Chiasa. Kalau aku sendirian tadi, kayaknya aku sudah keburu nyerah beli cokelat di minimarket."
            nar "Ia mengucapkan terima kasih dengan tulus sementara pandangannya masih terus tertuju pada kotak hadiah di tangannya."
        else:
            yutaka "Masih sempat kok sebelum jam pulang, Nagisa. Kita turun beli bahan cokelat baru di pasar swalayan depan gerbang, terus pinjam dapur kecil di ruang kegiatan mahasiswa buat bikin satu loyang lagi. Biar aku bantu."
            nar "Nagisa mengerjap kaget, sempat hendak menolak secara refleks, lalu melirik kembali kotak merah muda yang masih kosong di tangannya."
            nagisa "Kamu serius mau bantuin bikin kue di dapur kampus? Kamu kan paling malas disuruh urusan timbang-timbang bahan, Yutaka. Jangan sampai nanti malah kamu kacauin lagi!"
            yutaka "Aku cuma bantuin potong cokelat sama aduk adonan sesuai perintahmu kok, nggak bakal sok improvisasi. Ayo cepetan sebelum swalayan penuh."
            nagisa "...Hmph. Ya sudah! Tapi dengar ya, di dapur nanti kamu cuma boleh kerjain bagian yang kuminta! Jangan sekali-kali asal nambahin gula, mentega, atau sentuh tombol suhu tanpa tanya aku dulu!"
            nar "Lima belas menit kemudian, kalian berdua sudah berdiri di depan meja dapur kecil ruang kegiatan mahasiswa dengan celemek pinjaman. Nagisa menyerahkan pisau dan talenan kepadamu untuk mencincang cokelat batangan sementara ia menyiapkan loyang baru, dan sampai tiga kali ia mengingatkanmu agar tidak menambahkan satu bahan pun tanpa izinnya."
            yutaka "Iya, iya, aku cuma ngaduk mentega cairnya pelan-pelan kok, nggak kucampur apa-apa."
            nagisa "Bagus! Tadi pagi aku ceroboh karena terlalu buru-buru. Kali ini harus kutungguin terus di depan kaca pemanggang biar nggak lewat satu menit pun."
            nar "Begitu adonan masuk ke dalam pemanggang, aroma cokelat panggang yang manis dan hangat perlahan memenuhi dapur. Nagisa mengembuskan napas panjang sambil mengawasi jarum pewaktu dengan dahi berkerut."
            nagisa "Aku nggak mau yang ini gagal juga, Yutaka. Ya sudahlah... kamu juga kan dari dulu sudah tahu ini buat siapa."
            yutaka "Kali ini baunya sudah bener, nggak ada bau gosong sama sekali."
            nar "Tepat saat bunyi ting terdengar, Nagisa mengangkat loyang dengan sarung tangan kain. Permukaan browniesnya matang merata dan lembut. Setelah dingin, ia memotongnya dengan teliti, menatanya rapi ke dalam kotak merah muda, lalu mengikat pitanya dengan senyum lega."
            nagisa "...Makasih banyak ya, Yutaka. Kalau tadi aku sendirian, kayaknya aku sudah keburu nyerah beli cokelat di minimarket."
            nar "Ia mengucapkan terima kasih dengan tulus sementara pandangannya tetap tertuju penuh pada kotak hadiah merah muda di tangannya."
    else:
        if kk_host == "chiasa":
            nar "Kamu meletakkan kedua tanganmu di tepi meja gambar lalu menatap Nagisa lurus-lurus tanpa nada menggoda seperti biasanya."
            chiasa "Kalau Nagisa-senpai bingung mau diapain kotak itu gara-gara gosong, gimana kalau tahun ini bikin cokelatnya buat aku aja? Aku nggak bakal protes kok walaupun pinggirannya agak gosong sedikit."
            nar "Nagisa langsung mendongak cepat. Wajahnya yang tadi sudah mulai tenang seketika kembali memerah sampai ke pangkal leher. Ia menyipitkan mata menatapmu penuh curiga."
            nagisa "H-hah?! Kamu ngomong apaan sih, Chiasa?! Kalau mau ngeledek aku gara-gara gagal bikin kue, cari bahan lain aja deh, jangan ngomong aneh-aneh kayak gitu!"
            chiasa "Aku nggak lagi ngeledek kok, Nagisa-senpai. Aku serius. Lagian meja Ko-nii di Gedung Sastra kan tiap Valentine sudah penuh puluhan kotak. Aku beneran pengin coba cokelat buatan tangan Senpai."
            nar "Suasana di meja sudut studio itu mendadak hening selama beberapa detik. Nagisa menatap wajahmu lekat-lekat, mencari tanda-tanda senyum jahil yang biasa dipakai Chiasa untuk memancingnya marah. Karena sama sekali tidak menemukan candaan di matamu, nada suaranya langsung mengecil dan berubah canggung."
            nagisa "...D-dasar aneh banget kamu hari ini. Tunggu dulu."
            nar "Nagisa menyingkirkan loyang brownies yang gosong itu jauh ke tepi meja, lalu membuka tasnya dan menarik keluar selembar kertas pembungkus baru berwarna biru muda yang masih terlipat rapi."
            nagisa "Kalau memang buat kamu, aku mau bikin yang beneran enak dan matang dengan benar. Masa aku ngasih barang gagal yang awalnya kubikin buat orang lain ke kamu."
            chiasa "Berarti Senpai beneran mau bikinin satu buat aku?"
            nagisa "I-iya! Sudah, jangan tanya ulang segala! Besok siang sepulang kelas kamu tunggu di depan tangga studio ini ya. Jangan telat, dan berhenti lihatin aku sambil senyum-senyum begitu!"
            nar "Nagisa buru-buru merapikan lembar resep dan kertas pembungkus biru muda itu ke dalam tasnya dengan gerakan salah tingkah. Wajahnya masih merah padam, tetapi ia sama sekali tidak menarik kembali janjinya kepadamu."
        else:
            nar "Kamu meletakkan kedua tangan di tepi meja gambar lalu menatap Nagisa lurus-lurus tanpa cengiran jahil yang biasa kamu pasang saat mengajaknya berdebat."
            yutaka "Kalau kamu bingung mau diapain kotak itu gara-gara gosong, gimana kalau tahun ini bikin cokelatnya buat aku aja, Nagisa? Aku nggak bakal komplain kok walaupun pinggirannya agak gosong dikit."
            nar "Nagisa langsung mendongak cepat. Rona merah yang tadi mulai surut seketika kembali menyapu pipi sampai ke pangkal lehernya. Ia menyipitkan mata menatapmu penuh curiga."
            nagisa "H-hah?! Kamu ngomong apaan sih, Yutaka?! Kalau mau ngeledek aku gara-gara gagal bikin kue, nggak usah ngomong ngawur kayak gitu dong! Bikin malu aja!"
            yutaka "Aku nggak lagi ngeledek kok. Aku serius. Lagian meja Koita di Gedung Sastra kan sudah penuh puluhan kotak, sedangkan aku beneran pengin dapat cokelat buatan tanganmu."
            nar "Suasana di sudut studio itu mendadak hening selama beberapa detik. Nagisa menatap wajahmu lekat-lekat, mencari tanda-tanda lelucon yang biasa dipakai Yutaka untuk membuatnya kesal. Begitu sadar kamu sama sekali tidak sedang bercanda, nada suaranya langsung mengecil dan berubah serba salah."
            nagisa "...Tumben banget kamu ngomong lurus begitu tanpa ketawa. Tunggu sebentar."
            nar "Nagisa menggeser loyang brownies yang gosong itu jauh ke tepi meja, lalu membuka tasnya dan menarik keluar selembar kertas pembungkus lain berwarna krem gelap yang masih terlipat rapi."
            nagisa "Kalau buatmu, aku mau bikin yang beneran matang dengan benar. Mana mungkin aku ngasih barang gagal yang awalnya kubikin buat orang lain ke kamu."
            yutaka "Berarti kamu beneran mau bikinin satu khusus buat aku?"
            nagisa "I-iya! Sudah, jangan tanya ulang segala! Besok siang sepulang kelas kamu tunggu di depan tangga studio ini ya. Jangan telat, dan berhenti lihatin aku dengan muka begitu!"
            nar "Nagisa buru-buru memasukkan kertas pembungkus krem dan lembar resep itu ke dalam tasnya dengan gerakan yang mendadak canggung di dekatmu, tetapi ia sama sekali tidak menarik kembali niatnya."
    return

# ┌─ PANDUAN CERITA · N09 · Hadiah Kecil
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : White Day; ia menerima hadiah.
# │ INTI    : A kecil / B mahal / C tidak ada.
# │ AKHIRAN : gengsi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N09:
    call kk_scene_enter("nagisa", "Studio Arsitektur · White Day")
    if kk_host == "chiasa":
        nar "Ruang Studio Arsitektur lantai dua di tanggal empat belas Maret dipenuhi bau lem maket, suara pisau pemotong papan busa, serta obrolan beberapa mahasiswa yang saling memamerkan kotak camilan White Day di deretan meja tengah."
        nar "Di meja gambar dekat jendela, Sakurajima Nagisa duduk membungkuk sambil menempelkan potongan kayu balsa mungil pada rangka atap maket rumah keluarga. Begitu melihatmu berjalan menghampiri mejanya, Nagisa langsung mendongak cepat. Dari caranya langsung merapikan posisi duduk, jelas sekali ia sudah sangat sadar tanggal berapa hari ini bahkan sebelum kamu sempat menyebut White Day."
        nagisa "Eh, Chiasa? Tumben mampir ke lantai dua. Maaf ya mejaku lagi berantakan banget, maket tugas strukturku tenggatnya tinggal tiga hari lagi, terus lemnya dari tadi susah banget kering padahal sudah kupakaiin penjepit..."
        nar "Sambil bicara cepat soal tugas maket dan dosen pembimbingnya yang banyak merevisi ukuran jendela, matanya sudah dua kali melirik turun ke arah kedua tanganmu dan tas kanvas yang kamu selempangkan di bahu."
        chiasa "Santai aja, Nagisa-senpai. Aku cuma mampir sebentar lihat progres maket Senpai kok."
        nar "Nagisa terdiam sejenak, mengetuk-ngetuk penggaris plastik ke tepi meja gambarnya, lalu berdeham kaku sambil membuang sedikit pandangannya ke arah jendela dengan pipi agak memerah."
        nagisa "Oh iya, mumpung kamu di sini, aku mau bilang duluan supaya nggak canggung. Hari ini kan memang White Day, tapi kalau kamu mau kasih sesuatu, nggak usah merasa wajib atau repot segala ya! Aku sama sekali nggak pernah menghitung pemberian orang sebagai tagihan balik kok!"
        nar "Kalimat yang keluar dari mulutnya terdengar sangat masuk akal dan tegas. Namun raut wajahnya yang jelas-jelas sedang menahan napas menunggu reaksimu jauh lebih sulit ia kendalikan."
    else:
        nar "Ruang Studio Arsitektur lantai dua di tanggal empat belas Maret dipenuhi bau lem maket, suara pisau pemotong papan busa, serta obrolan beberapa mahasiswa yang saling memamerkan kotak camilan White Day di deretan meja tengah."
        nar "Di meja gambar dekat jendela, Sakurajima Nagisa duduk membungkuk sambil menempelkan potongan kayu balsa mungil pada rangka atap maket rumah keluarga. Begitu melihatmu berjalan menghampiri mejanya, Nagisa langsung mendongak cepat. Dari caranya langsung merapikan posisi duduk, jelas sekali ia sudah sangat sadar tanggal berapa hari ini bahkan sebelum kamu sempat menyebut White Day."
        nagisa "Eh, Yutaka? Tumben naik ke lantai dua. Maaf ya mejaku lagi berantakan banget, maket tugas strukturku tenggatnya tinggal tiga hari lagi, terus lemnya dari tadi susah banget kering padahal sudah kupakaiin penjepit..."
        nar "Sambil bicara cepat soal tugas maket dan dosen pembimbingnya yang banyak merevisi ukuran jendela, matanya sudah dua kali melirik turun ke arah kedua tanganmu dan saku jaketmu."
        yutaka "Santai aja, aku cuma mampir sebentar lihat maketmu sudah jadi rumah beneran atau masih kayak kandang merpati."
        nagisa "Mulutmu ya, ini sudah hampir beres tahu! Eh... oh iya, mumpung kamu di sini, aku mau bilang duluan supaya nggak canggung."
        nar "Nagisa berhenti sejenak, mengetuk-ngetuk penggaris plastik ke tepi meja gambarnya, lalu berdeham kaku sambil membuang sedikit pandangannya ke arah jendela dengan pipi agak memerah."
        nagisa "Hari ini kan memang White Day, tapi kalau kamu mau kasih sesuatu, nggak usah merasa wajib atau repot segala ya! Aku sama sekali nggak pernah menghitung pemberian orang sebagai tagihan balik kok!"
        nar "Kalimat yang keluar dari mulutnya terdengar sangat masuk akal dan tegas. Namun raut wajahnya yang jelas-jelas sedang menahan napas menunggu reaksimu jauh lebih sulit ia kendalikan."
    call kk_family_menu("N09", ["Keluarkan hadiah kecil yang sederhana dari tasmu dan serahkan padanya.", "Letakkan kotak hadiah bermerek mahal yang mencolok di atas mejanya.", "\"Oh, syukurlah kalau begitu. Soalnya aku memang nggak bawa apa-apa hari ini.\""])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu tersenyum tipis, lalu merogoh saku samping tas kanvasmu dan mengeluarkan satu bungkus kertas polos berukuran kecil yang sama sekali tidak menarik perhatian mahasiswa di meja-meja sebelah. Kamu meletakkannya pelan tepat di samping kotak pensil Nagisa."
            chiasa "Tenang aja, Senpai, aku nggak merasa ditagih kok. Nih, cuma hadiah kecil biasa buat White Day."
            nar "Nagisa mengerjap kaget, melirik cepat ke meja sebelah untuk memastikan tidak ada yang mengintip, lalu menarik bungkus kecil itu ke dekat pangkuannya dan membuka selotipnya pelan-pelan."
            nar "Begitu kertasnya terbuka, tampak sebuah gantungan kunci akrilik mungil bergambar kelinci putih yang sedang memegang penggaris segitiga kecil bersama satu pak kecil permen jeruk madu. Mata biru Nagisa langsung melebar sedikit dan rona merah muda merambat ke kedua pipinya."
            nagisa "H-hah? Cuma gantungan kunci kelinci kecil sama permen jeruk? ...Tunggu, kelincinya beneran pegang penggaris segitiga arsitektur ya? Kamu sengaja nyari yang model begini?"
            chiasa "Kemarin kebetulan lewat toko alat tulis dekat stasiun terus lihat itu di rak depan. Langsung kepikiran kayaknya lucu kalau dipasang di tas maket Nagisa-senpai."
            nagisa "...Hmph. Kamu ternyata masih ingat aku suka barang-barang model begini ya. Ya sudah, oke deh, kuterima. Selera kamu ternyata nggak seburuk yang kukira, Chiasa."
            chiasa "Kalau menurut Senpai terlalu kekanak-kanakan nggak usah dipakai kok."
            nagisa "Siapa bilang kekanak-kanakan?! Jangan ditarik lagi! Enak aja, barang yang sudah dikasih nggak boleh diambil balik!"
            nar "Dengan gerakan cepat tapi sangat hati-hati, Nagisa langsung mengaitkan gantungan kelinci mungil itu ke ritsleting tas ranselnya dan menaruh tasnya rapat di samping kursinya. Sepanjang sisa obrolan tentang revisi atap maketnya, mulutnya masih sempat menyebut hadiah itu cuma barang kecil biasa, tetapi kamu melihat tangannya sampai tiga kali meraba ritsleting tas untuk memastikan gantungan barunya masih terpasang dengan aman."
        else:
            nar "Kamu tersenyum tipis, lalu merogoh saku jaketmu dan mengeluarkan satu bungkus kertas polos berukuran kecil yang sama sekali tidak menarik perhatian mahasiswa di meja-meja sebelah. Kamu meletakkannya pelan tepat di samping kotak pensil Nagisa."
            yutaka "Tenang aja, aku nggak merasa ditagih kok. Nih, cuma barang kecil biasa buat White Day."
            nar "Nagisa mengerjap kaget, melirik cepat ke meja sebelah untuk memastikan tidak ada yang mengintip, lalu menarik bungkus kecil itu ke dekat pangkuannya dan membuka selotipnya pelan-pelan."
            nar "Begitu kertasnya terbuka, tampak sebuah gantungan kunci akrilik mungil bergambar kelinci putih yang sedang memegang penggaris segitiga kecil bersama satu pak kecil permen jeruk madu. Mata biru Nagisa langsung melebar sedikit dan rona merah muda merambat ke kedua pipinya."
            nagisa "H-hah? Gantungan kunci kelinci kecil sama permen jeruk? ...Tunggu, kelincinya beneran pegang penggaris segitiga arsitektur ya? Kamu sengaja nyari yang model begini, Yutaka?"
            yutaka "Kemarin kebetulan lewat toko alat tulis dekat stasiun terus lihat di rak depan. Langsung kepikiran cocok aja dipasang di tas maketmu."
            nagisa "...Hmph. Kamu ternyata masih ingat aku suka barang-barang model begini. Ya sudah, oke deh, kuterima. Selera kamu ternyata nggak seburuk biasanya."
            yutaka "Kalau menurutmu kekanak-kanakan biar kubawa pulang lagi aja."
            nagisa "Siapa bilang kekanak-kanakan?! Jangan ditarik lagi! Barang yang sudah dikasih nggak boleh diambil balik!"
            nar "Dengan gerakan cepat tapi sangat hati-hati, Nagisa langsung mengaitkan gantungan kelinci mungil itu ke ritsleting tas ranselnya dan meletakkan tasnya rapat di samping kursinya. Sepanjang sisa obrolan tentang revisi atap maketnya, mulutnya masih sempat menyebut hadiah itu cuma barang remeh, tetapi kamu melihat tangannya sampai tiga kali meraba ritsleting tas untuk memastikan gantungan barunya masih terpasang aman."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kamu membuka tas belanja kertas berlogo emas dari sebuah butik aksesori ternama, lalu meletakkan kotak hadiah kaku berpita satin tebal tersebut langsung ke tengah meja gambar Nagisa."
            chiasa "Selamat hari White Day, Nagisa-senpai. Aku pilihin yang paling bagus di butik dekat stasiun kemarin."
            nar "Belum sempat Nagisa menyentuh pitanya, dua mahasiswa di meja gambar sebelah langsung menoleh bersamaan dan melontarkan seruan kaget begitu melihat merek butik mahal yang tercetak jelas di permukaan kotak."
            "Mahasiswi Studio" "Eh, Nagisa! Itu kotak dari butik yang di gedung department store pusat ya?! Gila, mahal banget itu lho!"
            "Mahasiswa Studio" "Wah, seriusan dapat hadiah White Day semahal itu di studio? Keren banget!"
            nar "Bahu Nagisa langsung menegang kaku dan wajahnya memerah karena malu bercampur risih. Tanpa membuka kotaknya sama sekali, ia buru-buru memasukkan kotak itu kembali ke dalam tas kertasnya agar mereknya tertutup, lalu meraih pergelangan tanganmu menarikmu tiga langkah menjauh ke sudut dekat rak penyimpanan maket."
            nagisa "Chiasa... kamu mikir apa sih bawa kotak butik semahal ini langsung ke tengah studio di depan semua orang?!"
            chiasa "Lho, aku kan cuma mau kasih hadiah White Day yang bagus buat Nagisa-senpai. Memangnya salah ya?"
            nar "Nagisa menurunkan suaranya lebih rendah lagi agar mahasiswa di deretan meja tengah tidak mendengar ketegangan kalian dan agar kamu tidak dipermalukan lebih jauh."
            nagisa "Bukan soal bagus atau nggaknya! Ini terlalu mahal dan terlalu mencolok! Kamu lihat sendiri kan barusan semua orang langsung melotot lihat logonya! Kalau aku terima di depan mereka, nanti orang-orang bakal ngomong apa di belakangku? Kalau kutolak di tempat, kamu yang bakal malu dilihat satu ruangan! Kamu sempat mikir sampai situ nggak sih sebelum beli ini?!"
            chiasa "...Maaf, Senpai. Aku nggak kepikiran efeknya bakal bikin Senpai nggak nyaman sampai segitunya."
            nagisa "Hah... ya sudahlah. Kuterima dulu hari ini supaya nggak jadi bahan tontonan orang di studio. Tapi tolong banget, lain kali jangan pernah kasih aku barang semahal ini lagi di tempat ramai begini."
            nar "Nagisa merapatkan pegangan tas kertas itu ke sisinya dengan dahi yang masih berkerut. Hadiah mencolok tersebut memberinya sorotan yang sama sekali tidak ia pilih, dan kini di tengah rasa risihnya sendiri ia juga harus ikut menjaga perasaan orang yang memberikannya."
        else:
            nar "Kamu mengangkat tas belanja kertas berlogo emas dari sebuah butik aksesori ternama, lalu meletakkan kotak hadiah kaku berpita satin tebal tersebut langsung ke tengah meja gambar Nagisa."
            yutaka "Selamat hari White Day, Nagisa. Kupilihin yang paling bagus di butik dekat stasiun kemarin."
            nar "Belum sempat Nagisa menyentuh pitanya, dua mahasiswa di meja gambar sebelah langsung menoleh bersamaan dan melontarkan seruan kaget begitu melihat merek butik mahal yang tercetak jelas di permukaan kotak."
            "Mahasiswi Studio" "Eh, Nagisa! Itu kotak dari butik gedung pusat ya?! Wah, pantesan Kisaragi-kun yang kasih, mahal banget itu lho!"
            "Mahasiswa Studio" "Seriusan dapat hadiah White Day semahal itu di studio? Keren banget!"
            nar "Bahu Nagisa langsung menegang kaku dan wajahnya memerah karena malu bercampur risih. Tanpa membuka kotaknya sama sekali, ia buru-buru memasukkan kotak itu kembali ke dalam tas kertasnya agar mereknya tertutup, lalu menarik lengan jaketmu tiga langkah menjauh ke sudut dekat rak penyimpanan maket."
            nagisa "Yutaka... aku tahu uang sakumu banyak, tapi kamu mikir apa sih bawa kotak butik semahal ini langsung ke tengah studio di depan semua orang?!"
            yutaka "Lho, aku cuma mau kasih hadiah White Day yang bagus buatmu. Memangnya salah?"
            nar "Nagisa menurunkan suaranya lebih rendah lagi agar mahasiswa di deretan meja tengah tidak mendengar ketegangan kalian dan agar kamu tidak dipermalukan lebih jauh."
            nagisa "Bukan soal bagus atau nggaknya! Ini terlalu mahal dan terlalu mencolok! Kamu dengar sendiri kan barusan semua orang langsung ngoceh lihat logonya! Kalau aku terima di depan mereka, nanti orang-orang bakal ngomong apa di belakangku? Kalau kutolak di tempat, kamu yang bakal malu dilihat satu ruangan! Kamu sempat mikir sampai situ nggak sih sebelum beli ini?!"
            yutaka "...Maaf, Nagisa. Aku nggak kepikiran bakal bikin kamu nggak nyaman sampai segitunya."
            nagisa "Hah... ya sudahlah. Kuterima dulu hari ini supaya nggak jadi bahan tontonan satu studio. Tapi tolong banget, lain kali jangan pernah kasih aku barang semahal ini lagi di tempat umum."
            nar "Nagisa merapatkan pegangan tas kertas itu ke sisinya dengan dahi yang masih berkerut. Hadiah mencolok tersebut memberinya sorotan yang sama sekali tidak ia pilih, dan kini di tengah rasa risihnya sendiri ia juga harus ikut menjaga perasaan orang yang memberikannya."
    else:
        if kk_host == "chiasa":
            chiasa "Oh, syukurlah kalau Nagisa-senpai nggak keberatan. Soalnya minggu ini aku sibuk banget sama tugas studio seni, jadi memang nggak sempat beli atau bawa apa-apa hari ini."
            nar "Tidak ada satu pun bungkus yang kamu keluarkan dari tasmu. Raut wajah Nagisa sempat membeku sepersekian detik, lalu ia langsung mengangguk cepat dengan senyum tipis yang kaku, seolah sejak awal ia memang hanya ingin memastikan kamu tidak perlu repot."
            nagisa "Bagus deh. Aku juga sama sekali nggak nunggu apa-apa kok. Lagian buat apa juga repot-repot mikirin tanggal empat belas pas tenggat maket lagi mepet begini."
            chiasa "Bagian rangka atapnya kelihatan sudah hampir beres ya, Senpai."
            nagisa "Belum, masih banyak yang harus dipotong ulang di sisi belakang. Eh, Chiasa, tolong ambilin penggaris besiku dong, kayaknya tadi kutaruh di sebelah sana."
            nar "Kamu menoleh ke permukaan meja gambar tepat di samping siku kiri Nagisa. Penggaris besi sepanjang tiga puluh sentimeter yang ia minta sebenarnya sejak tadi tergeletak jelas tepat di dekat tangannya sendiri. Kamu mengambilnya tanpa berkomentar lalu menyodorkannya ke hadapan Nagisa."
            nagisa "Makasih... eh, tunggu, tadi sudah ada di samping tanganku ya?"
            chiasa "Iya, tepat di samping potongan kayu balsa tadi."
            nagisa "...Oh. Ya sudah, aku lanjutin potong bingkainya dulu ya, takut nggak keburu sore."
            nar "Wajah Nagisa memerah tipis karena malu salah tingkah. Ia segera menunduk jauh lebih rendah ke atas papan maket, menolak menatapmu lagi sementara obrolan di meja sudut itu perlahan kehilangan seluruh kehangatannya."
        else:
            yutaka "Oh, syukurlah kalau kamu nggak keberatan. Soalnya minggu ini aku lagi pusing sama tugas kuliah, jadi memang nggak bawa apa-apa hari ini."
            nar "Tidak ada satu pun bungkus yang kamu keluarkan dari saku jaket maupun tasmu. Raut wajah Nagisa sempat membeku sepersekian detik, lalu ia langsung mengangguk cepat dengan senyum tipis yang kaku, seolah sejak awal ia memang hanya ingin memastikan kamu tidak perlu repot."
            nagisa "Bagus deh. Aku juga sama sekali nggak nunggu apa-apa kok. Lagian buat apa juga repot-repot mikirin tanggal empat belas pas tenggat maket lagi mepet begini."
            yutaka "Rangka atapnya kelihatan sudah hampir selesai tuh."
            nagisa "Belum, masih banyak yang harus dipotong ulang di sisi belakang. Eh, Yutaka, tolong ambilin penggaris besiku dong, kayaknya tadi jatuh di sebelah sana."
            nar "Kamu menoleh ke permukaan meja gambar tepat di samping siku kiri Nagisa. Penggaris besi sepanjang tiga puluh sentimeter yang ia minta sebenarnya sejak tadi tergeletak jelas tepat di dekat tangannya sendiri. Kamu mengambilnya tanpa berkomentar lalu menyodorkannya ke hadapan Nagisa."
            nagisa "Makasih... eh, tunggu, tadi sudah ada di samping tanganku ya?"
            yutaka "Iya, tepat di samping potongan kayu balsa tadi."
            nagisa "...Oh. Ya sudah, aku lanjutin potong bingkainya dulu ya, takut nggak keburu sore."
            nar "Wajah Nagisa memerah tipis karena malu salah tingkah. Ia segera menunduk jauh lebih rendah ke atas papan maket, menolak menatapmu lagi sementara suasana di meja sudut itu perlahan kehilangan seluruh kehangatannya."
    return

init 1 python:
    _hook("N05-A", lambda: (kk_rel("nagisa","intim",4), kk_flag("koko_dikenal")))
    _hook("N05-B", lambda: kk_rel("nagisa","intim",2))
    _hook("N05-C", lambda: kk_rel("nagisa","trust",2))
    _hook("N07-A", lambda: (kk_rel("nagisa","intim",4), kk_adj("kelekatan_nagisa",10), kk_flag("koko_dikenal")))
    _hook("N07-B", lambda: kk_adj("kelekatan_nagisa",-5))
    _hook("N07-C", lambda: (kk_rel("nagisa","trust",3), kk_rel("nagisa","jeal",3)))
    _hook("N08-A", lambda: kk_rel("nagisa","intim",3))
    _hook("N08-B", lambda: (kk_rel("nagisa","trust",4), kk_adj("kelekatan_nagisa",5)))
    _hook("N08-C", lambda: (kk_rel("nagisa","intim",3), kk_rel("nagisa","jeal",3)))
    _hook("N09-A", lambda: kk_adj("gengsi_nagisa",-5))
    _hook("N09-B", lambda: (kk_adj("gengsi_nagisa",8), kk_rel("nagisa","jeal",2)))
    _hook("N09-C", lambda: kk_rel("nagisa","trust",-3))

# N10 (M13): telepon dari Haruto, kakak Nagisa. Intro hangat; menyambung ke N21.
# ┌─ PANDUAN CERITA · N10 · Haruto Menelepon
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : kakak menggodanya.
# │ INTI    : A dukung / B menghindar.
# │ AKHIRAN : haruto_curiga awal.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N10:
    call kk_scene_enter("nagisa", "Studio Arsitektur")
    play sound "audio/sfx/phone_vibrate.wav"
    nar "Ponsel Nagisa bergetar. Di layar: 'Kak Haruto'. Ia mengangkatnya sambil memutar matanya."
    nagisa "Iya, iya, aku makan teratur. ...Dia mau bicara denganmu, katanya."
    "Haruto" "Aku dengar namamu makin sering. Nagisa kalau pulang capek suka mengeluh, terus mendadak membela orang yang baru dikeluhkannya. Lumayan jelas polanya."
    nagisa "Kak! Aku masih bisa dengar!"
    menu:
        "Tanggapi Haruto dengan hangat dan berjanji menjaga Nagisa.":
            $ kk_record_choice("N10", "A")
            nar "Kau menanggapi dengan hangat dan berjanji tidak menganggap kegalakannya alasan untuk mengabaikan kabarnya. Haruto tertawa, lalu menjadi lebih serius."
            "Haruto" "Kalau ada masalah, bicara ke dia juga. Aku kakaknya, bukan orang yang boleh menjawab seluruh hidupnya. Tapi kalau perlu bantuan, kamu tahu siapa yang bisa dihubungi."
            nar "Nagisa mengambil ponsel kembali sambil mengomel. Wajahnya merah, tetapi ia tidak terlihat ingin menghapus perkenalan tadi."
        "Serahkan ponsel kembali dan hindari bicara panjang.":
            $ kk_record_choice("N10", "B")
            nar "Kau mengembalikan ponsel sebelum pembicaraan panjang. Haruto sempat menyampaikan salam, kemudian suaranya mengecil di dekat telinga Nagisa."
            nagisa "Sudah. Jangan menginterogasi temanku."
            nar "Sesudah panggilan selesai ia mengatakan kakaknya berlebihan, tetapi bertanya juga apakah kau memang tidak suka keluarganya ikut mengenalmu. Pertanyaan itu ia bungkus sebagai keluhan, agar tidak tampak sedang mencari kepastian."
    return

init 1 python:
    _hook("N10-A", lambda: (kk_flag("haruto_kenal"), kk_rel("nagisa","trust",3)))
    _hook("N10-B", lambda: kk_rel("nagisa","jeal",2))
