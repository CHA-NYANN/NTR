# Cleanup milestone berdiri sendiri: Harumi H20 (teh
# terakhir), H21 (pengumuman studi), H23 (ujian akhir); Moeka Mo07 (peragaan
# pertama). Node "Pilihan X" (menu kosong) ditangani sebagai resolver ending,
# bukan di sini. Konsekuensi + karakter. Mengikuti Event_Harumi / Event_Moeka.

# ┌─ PANDUAN CERITA · H20 · Teh Terakhir
# │ LOKASI  : Kampus Kouseikan · Perpustakaan Pusat
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : ia menyeduh teh lagi.
# │ INTI    : A minum / B menolak / C menahan pergi.
# │ AKHIRAN : simbol kembali.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H20:
    call kk_scene_enter("harumi", "Perpustakaan Pusat · Teh terakhir")
    nar "Harumi meletakkan cangkir di meja yang pernah kalian pakai membaca bersama. Aroma tehnya sama; cara ia menawarkan kini lebih hati-hati, tidak lagi yakin sebuah kebiasaan lama otomatis masih diterima."
    harumi "Aku menyeduh lagi. Aku ingin membaginya denganmu. Kalau tidak mau, aku tetap ingin mengatakannya dengan jelas."
    call kk_family_menu("H20", ["Minum teh itu bersamanya.", "Menolak teh itu.", "Menahan ia agar tidak pergi."])
    if _return == "A":
        harumi "Kau meminumnya. ...Simbol yang kembali. Aku senang sebagian dari dulu masih ada."
        nar "Kau menyebut rasanya, lalu bertanya bagaimana ia belakangan. Harumi tidak perlu menjadikan satu cangkir bukti bahwa semua yang pernah berubah sudah kembali."
        harumi "Aku belum tahu cara merangkum. Tapi aku bisa mulai dari hari ini."
    elif _return == "B":
        nar "Kau menolak. Harumi menurunkan cangkir, berusaha menerima satu jawaban tanpa segera mengubahnya menjadi penilaian atas seluruh kedekatan kalian."
        harumi "Baik. Terima kasih sudah bilang. Aku tidak ingin kamu meminumnya karena takut membuatku sedih."
        nar "Ia tetap sedih sedikit. Kali ini ia membiarkan rasa itu ada tanpa menagih perubahan jawabanmu."
    else:
        harumi "Kau menahanku? ...Itu bukan logika. Dan justru karena itu, aku ingin tinggal sebentar lagi."
        nar "Kau meminta waktu tambahan, bukan menghalangi langkahnya. Harumi memeriksa jadwal, lalu memilih duduk."
        harumi "Dua puluh menit. Aku ingin tinggal, dan sesudahnya tetap harus pergi. Aku rasa dua hal itu boleh benar bersama."
    return

# ┌─ PANDUAN CERITA · H21 · Pengumuman Studi
# │ LOKASI  : Kampus Kouseikan · Perpustakaan Pusat
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : beasiswa luar negeri.
# │ INTI    : A dukung pergi / B minta tinggal / C ikut.
# │ AKHIRAN : ending Harumi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H21:
    call kk_scene_enter("harumi", "Perpustakaan Pusat · Pengumuman studi")
    nar "Harumi menunjukkan surat penerimaan dengan tangan yang sulit diam. Ia sudah membaca syaratnya, tetapi masih perlu mendengar dirinya sendiri mengatakan diterima."
    harumi "Ini jalan yang kuinginkan. Aku senang. Aku juga memikirkan jarak dari orang-orang di sini. Aku ingin mendengar keinginanmu, tetapi keputusannya harus tetap bisa kuambil sendiri."
    call kk_family_menu("H21", ["Dukung ia pergi mengejar studinya.", "Minta ia tinggal, dengan jujur.", "Tawarkan ikut bersamanya."])
    if _return == "A":
        harumi "Kau mendukungku pergi, meski itu menjauhkan kita? ...Itu bentuk kepercayaan yang paling bersih."
        nar "Ia mulai membicarakan laboratorium tujuan, bukan hanya kesulitan pergi. Kehadirannya mendadak lebih hidup ketika harapannya boleh terlihat tanpa lebih dahulu meminta maaf karena akan jauh."
    elif _return == "B":
        harumi "Kau memintaku tinggal—sebagai dirimu, bukan sebagai saran. ...Aku akan menimbang itu dengan sungguh-sungguh."
        nar "Ia menanyakan seperti apa masa depan yang kaubayangkan jika ia tinggal. Pertanyaan itu tidak bisa dijawab hanya dengan rindu; ada cita-cita yang perlu mendapat tempat nyata, bukan pujian bahwa ia rela berkorban."
    else:
        harumi "Kau mau ikut? ...Variabel itu tidak kuperhitungkan. Dan ternyata, ia mengubah seluruh persamaan."
        nar "Setelah terkejut, ia meminta kalian membahas pekerjaanmu, izin tinggal, dan uang sebelum menyebutnya janji. Gembira tidak membuatnya ingin mengabaikan akibat yang akan kalian tanggung berdua."
    return

# ┌─ PANDUAN CERITA · H23 · Ujian Akhir
# │ LOKASI  : Kampus Kouseikan · Perpustakaan Pusat
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : ujian skripsi.
# │ INTI    : A bantu / B ganggu / C hadir.
# │ AKHIRAN : hasil akademik.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H23:
    call kk_scene_enter("harumi", "Perpustakaan Pusat · Ujian skripsi")
    nar "Harumi menyusun kartu presentasi menurut urutan yang sudah dihafal. Ia terus mengubah posisi kartu kedua dan ketiga, meski keduanya menjelaskan hal yang sama."
    harumi "Aku bisa menjawab pertanyaan tentang penelitian. Yang membuatku takut adalah merasa mereka sedang memutuskan apakah seluruh diriku cukup. Aku tahu skripsi tidak seharusnya berarti itu."
    call kk_family_menu("H23", ["Bantu ia mempersiapkan pembelaannya.", "Ganggu persiapannya.", "Sekadar hadir mendukungnya."])
    if _return == "A":
        harumi "Kau menemaniku berlatih sampai larut? ...Dengan begini, aku menghadapi panel itu tidak sendirian."
        nar "Kau memintanya menjelaskan kepada seseorang yang belum tahu seluruh riset. Ketika ia tersendat, kalian mengulang bagian itu tanpa menyebutnya kegagalan."
        harumi "Aku tidak perlu terdengar sempurna agar orang bisa mengikuti. Itu berguna sekali untuk diingat sebelum masuk ruangan."
    elif _return == "B":
        nar "Kau mengganggu waktu yang disiapkannya untuk latihan. Harumi mencoba menyesuaikan, lalu kehilangan urutan yang tadi sudah ia pahami."
        harumi "Aku perlu berhenti melayanimu sekarang. Ini penting bagiku."
        nar "Ia akhirnya mengatakan batas itu, tetapi gugup yang bertambah tetap ikut dibawa ketika kembali membuka kartu."
    else:
        harumi "Kau hadir di hari itu? ...Satu wajah yang kukenal di antara panel asing. Itu sudah menurunkan satu variabel ketakutan."
        nar "Kau menunggu di tempat yang diperbolehkan. Sebelum masuk, ia menoleh sekali dan tersenyum kecil, kemudian berjalan menuju ujian yang tetap harus ia jalani sendiri."
    return

# ┌─ PANDUAN CERITA · Mo07 · Peragaan Pertama
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia tampil.
# │ INTI    : A hadir / B bantu backstage / C absen.
# │ AKHIRAN : reputasi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo07:
    call kk_scene_enter("moeka", "Kantin Pusat · Peragaan pertama")
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Ruang persiapan di belakang panggung aula mini Fakultas Seni malam itu terang oleh deretan lampu cermin rias, dipenuhi aroma semprotan penata rambut, bedak tabur, dan suara derit roda gantungan besi yang didorong hilir mudik. Beberapa mahasiswi desain tampak sibuk merapikan lipatan rok model mereka sambil memeriksa daftar urutan tampil di papan klip."
        else:
            nar "Ruang persiapan di belakang panggung aula mini Fakultas Seni hari itu penuh oleh bau semprotan penata rambut, bedak tabur, dan suara derit roda gantungan besi yang didorong hilir mudik. Beberapa mahasiswi desain tampak sibuk merapikan lipatan rok model mereka sambil memeriksa daftar urutan tampil di papan klip."
        nar "Di sudut paling belakang dekat cermin lampu, Kohinata Moeka duduk di tepi meja kayu sambil memangku jaket denim hasil rancangannya sendiri. Jari-jari tangan kanannya terus-menerus meraba keliman renda putih di bagian kerah jaket itu, memeriksa baris jahitan yang sebenarnya sudah tiga kali ia periksa sejak sepuluh menit lalu."
        chiasa "Jahitan kerahnya sudah rapi banget kok, Moemoe-senpai. Nggak ada benang yang keluar sama sekali."
        moeka "Eh... iya ya? Kelihatan banget ya kalau tanganku dari tadi nggak bisa diam, Chimian?"
        chiasa "Barusan ada anak tahun kedua yang lewat bawa jarum pentul, Senpai bahkan nggak sadar dipanggil."
        moeka "Aduh, separah itu ya fokusku buyar..."
        nar "Baru lima menit lalu, ketika anak-anak panitia tahun pertama mampir ke ruang tunggu untuk menanyakan kesiapan peserta, Moeka masih tertawa lebar dan menyemangati semua orang bahwa peragaan busana hari ini pasti bakal meriah. Begitu rombongan panitia itu keluar dan hanya tinggal kalian berdua di sudut cermin, ia menjatuhkan bahunya sambil mengembuskan napas panjang."
        moeka "Jujur aja nih, Chimian... ujung jariku dingin banget dari tadi. Coba deh pegang, kayak habis celup es batu kan? Padahal kemarin malam waktu menjahit kancing terakhirnya di kos, aku masih semangat banget."
        chiasa "Wajar kok kalau tegang, Senpai. Ini kan pertama kalinya Senpai jalan sendiri di panggung membawakan baju rancangan sendiri."
        moeka "Masalahnya, dari kemarin semua anak di kelas maupun di panitia sudah keburu bilang, 'Kalau punya Moeka mah pasti keren, dia kan biasa tampil di depan orang.' Padahal jalan di panggung sambil dinilai dosen sama ditonton satu aula itu beda jauh sama memimpin rapat."
        chiasa "Beban ekspektasi orang memang suka bikin napas jadi pendek sebelum mulai ya, Senpai."
        moeka "Apalagi dosen penguji depan panggung bawa papan nilai tebal, rasanya setiap langkah nanti langsung dihitung angkanya."
        nar "Moeka memeluk bagian lengan jaket denim itu sedikit lebih erat ke dadanya."
        moeka "Lama-lama aku capek juga kalau setiap hal yang beneran kusuka langsung berubah jadi tontonan yang wajib berhasil demi menyenangkan semua orang. Sebelum namaku dipanggil panitia keluar tirai, aku boleh gugup lima menit dulu di depanmu kan, Chimian?"
        chiasa "Tentu saja boleh, Moemoe-senpai. Di sudut cermin sini cuma ada kita berdua kok."
        nar "Moeka tersenyum tipis penuh rasa syukur sambil menyandarkan punggungnya sebentar ke tepi meja rias."
    else:
        if kk_slot >= 3:
            nar "Lorong persiapan di belakang panggung aula peragaan busana kampus malam itu terang oleh lampu rias, dipenuhi aroma semprotan rambut, bunyi ritsleting tas pakaian, dan langkah tergesa para kru mahasiswa. Di sudut dekat rak gantungan baju cadangan, Kohinata Moeka berdiri bersandar sambil memegangi jaket denim hasil rancangannya sendiri."
        else:
            nar "Lorong persiapan di belakang panggung aula peragaan busana kampus hari itu penuh oleh aroma semprotan rambut, bunyi ritsleting tas pakaian, dan langkah tergesa para kru mahasiswa. Di sudut dekat rak gantungan baju cadangan, Kohinata Moeka berdiri bersandar sambil memegangi jaket denim hasil rancangannya sendiri."
        nar "Ibu jarinya berulang kali menelusuri jahitan renda tangan di bagian kerah jaket yang sama, sebuah gerakan gelisah yang sangat kontras dengan tawa lepasnya lima menit lalu di depan anak-anak panitia."
        yutaka "Kerah jaketnya bakal lecek beneran kalau kamu gosok-gosok terus dari tadi, Kohinata. Jahitannya sudah lurus kok."
        moeka "Aduh, ketahuan ya? Kelihatan banget ya kalau aku lagi nggak bisa tenang, Yutayuta?"
        yutaka "Tadi waktu panitia sebelah lewat nanya nomor urutan, kamu sampai telat menyahut tiga detik."
        moeka "Ketahuan banget berarti..."
        yutaka "Padahal lima menit lalu waktu anak-anak panitia lewat perasaan kamu masih ketawa paling kencang."
        moeka "Ya kalau di depan mereka masa aku pasang muka pucat, nanti satu ruangan ikutan tegang semua. Tapi asli deh, telapak tanganku sekarang dingin banget. Padahal kemarin waktu menyelesaikan pola lengannya di studio, aku senang banget."
        yutaka "Namanya juga peragaan busana pertamamu. Wajar kalau deg-degan sebelum naik panggung."
        moeka "Habisnya semua orang dari tadi sudah keburu muji duluan, bilang aku pasti santai lah, pasti paling mencolok lah. Lama-lama tiap kali bikin sesuatu yang kubanggakan, rasanya malah kayak lagi ujian yang nggak boleh meleset satu langkah pun."
        yutaka "Nggak usah terlalu mikirin omongan orang di depan, yang penting kamu senang sama hasil jahitanmu sendiri."
        moeka "Di baris depan aula nanti dosen penguji duduk bawa daftar nilai semua, Yutayuta, rasanya malah makin deg-degan."
        nar "Dari balik tirai hitam tebal di ujung lorong, terdengar suara koordinator panggung yang mengecek mikrofon dan mengingatkan bahwa giliran kelompok pembuka tinggal lima belas menit lagi. Moeka menelan ludah, lalu menoleh menatapmu."
        moeka "Sebelum dipanggil berbaris ke balik tirai, aku boleh panik lima menit dulu di sini kan, Yutayuta?"
        yutaka "Silakan saja, di pojok rak gantungan baju ini nggak ada panitia lain yang memperhatikan."
        nar "Bahu Moeka yang sejak tadi terangkat kaku perlahan turun sedikit mendengar jawaban tenangmu."
    call kk_family_menu("Mo07", ["\"Aku duduk di barisan depan kok, nanti kalau gugup lihat aja ke arahku.\"", "\"Sini biar aku bantu jagain barang-barangmu di belakang panggung.\"", "\"Maaf banget, habis ini aku ada urusan lain dan harus pergi sekarang.\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Gugup aja sepuasnya di sini dulu, Moemoe-senpai. Habis ini aku langsung keluar cari kursi di barisan paling depan sebelah kiri. Jadi nanti waktu Senpai keluar ke panggung dan lampu sorotnya terasa silau, Senpai tinggal lihat ke arah kursiku aja."
            nar "Moeka menatapmu sejenak, lalu senyum cemas di bibirnya perlahan berubah jauh lebih ringan."
            moeka "Beneran kamu mau duduk di barisan paling depan, Chimian? Nggak bosan menunggu urutan tampilku di tengah?"
            chiasa "Nggak bakal bosan, aku malah pengin lihat detail jaketnya dari dekat waktu kena lampu panggung. Pasti benang rendanya kelihatan menonjol banget."
            moeka "Syukurlah... kalau ada satu wajah yang kukenal duduk di bawah sana, setidaknya aku punya patokan harus lihat ke mana waktu jalan di ujung panggung nanti. Sana cari kursinya dulu sebelum diambil orang!"
            chiasa "Siap, semangat ya, Senpai! Sampai ketemu dari bawah panggung!"
            nar "Kamu melangkah keluar dari ruang persiapan menuju area aula penonton dan berhasil mendapatkan kursi kosong di barisan terdepan sisi kiri. Sepuluh menit kemudian, lampu aula dipadamkan, musik pengiring mulai berdentum dari pengeras suara, dan satu per satu mahasiswa desain berjalan keluar melewati lintasan panggung."
            nar "Ketika nama Kohinata Moeka diumumkan dan ia melangkah keluar mengenakan jaket denim berhias renda buatannya, dua langkah pertamanya masih tampak sedikit kaku. Begitu matanya menyapu barisan depan sisi kiri dan mendapati kamu sedang duduk memperhatikan sambil mengangkat jempol kecil, dagunya langsung terangkat mantap."
            nar "Ia menyelesaikan putaran di ujung panggung dengan senyum percaya diri yang memikat hingga tepuk tangan penonton bergema memenuhi ruangan. Begitu acara penutupan selesai dan lampu aula dinyalakan kembali, Moeka setengah berlari keluar dari pintu samping panggung menghampirimu."
            moeka "Chimian! Kamu lihat kan tadi waktu aku berputar di ujung panggung?! Kakiku sama sekali nggak kesandung dan rendanya kelihatan jelas banget!"
            chiasa "Keren banget tadi, Moemoe-senpai. Dosen pengujinya aja sampai manggut-manggut sambil mencatat nilai waktu Senpai berhenti di ujung lintasan."
            moeka "Serius dosennya mengangguk?! Wah, lega banget rasanya!"
            chiasa "Serius, tadi aku lihat persis dari kursi depan."
            moeka "Hehe, itu gara-gara begitu aku keluar tirai langsung lihat kamu duduk manis di kursi depan! Makasih banyak ya sudah menunggu sampai acara selesai!"
            chiasa "Sama-sama, Moemoe-senpai. Sekarang jaketnya mau langsung dimasukkan ke tas pakaian atau masih mau dipakai foto dokumentasi klub?"
            moeka "Masih harus foto bersama panitia lima menit lagi di depan panggung, habis itu kita cari minuman manis dingin di kantin yuk!"
            chiasa "Ayo, kutunggu di dekat pintu aula ini sambil pegangin tas kain Senpai."
            nar "Moeka menyerahkan tas kanvasnya kepadamu dengan wajah berseri-seri sebelum berlari kecil menghampiri barisan peserta untuk sesi foto penutup."
        else:
            yutaka "Panik aja dulu lima menit di sini, nggak ada yang melarang kok. Habis ini aku keluar dan duduk di kursi barisan paling depan sebelah kiri. Nanti waktu kamu jalan di panggung terus bingung mau lihat ke mana, lihat ke arahku aja."
            moeka "Serius kamu mau duduk di barisan paling depan sampai acaranya selesai, Yutayuta? Biasanya kamu paling malas duduk lama di acara kampus."
            yutaka "Khusus hari ini aku duduk paling depan. Jadi kamu nggak usah merasa lagi ditonton orang asing satu aula."
            moeka "...Oke, itu membantu banget jujur aja. Sana keluar dulu cari kursinya sebelum penuh, aku mau pakai jaketnya sekarang!"
            yutaka "Oke, kulihat dari bawah panggung nanti."
            nar "Kamu keluar dari lorong belakang dan mengambil tempat duduk di barisan terdepan sisi kiri aula. Tidak lama kemudian lampu ruangan diredupkan, musik mulai mengalun, dan para peserta peragaan busana keluar bergantian di bawah sorot lampu putih."
            nar "Saat giliran Moeka tiba, langkah awalnya dari balik tirai sempat terlihat agak tegang. Begitu pandangannya mengarah ke barisan depan sebelah kiri dan menangkap sosokmu yang duduk bersandar santai sambil mengangguk kecil padanya, ketegangan di wajahnya langsung mencair."
            nar "Ia melangkah ringan sampai ke ujung lintasan, memamerkan detail jaket rancangannya dengan luwes, lalu berbalik diiringi tepuk tangan meriah. Begitu seluruh rangkaian acara selesai, Moeka langsung menerobos kerumunan penonton di tepi panggung untuk menghampirimu."
            moeka "Yutayuta! Gimana tadi jalanku di atas panggung? Kelihatan kayak model profesional beneran kan?!"
            yutaka "Lancar banget. Sama sekali nggak kelihatan kalau lima belas menit sebelumnya tanganmu dingin kayak es batu di belakang."
            moeka "Ahaha, jangan dibuka lagi dong rahasia belakang panggungnya! Tadi dosennya sempat kelihatan mencatat nggak waktu aku muter?"
            yutaka "Sempat, sambil senyum puas malah."
            moeka "Asyik! Serius, makasih banget ya sudah duduk di depan tadi. Begitu lihat mukamu, gugupku langsung hilang setengah!"
            yutaka "Syukurlah kalau begitu. Sana ikut foto dokumentasi bareng panitia dulu, tasmu biar kupegangin di sini."
            moeka "Oke, tunggu lima menit ya, habis foto kita beli minuman dingin di depan!"
            nar "Moeka menitipkan tas pakaiannya ke tanganmu dengan langkah ringan yang penuh rasa bangga sebelum bergabung dengan rekan-rekan sekelasnya di depan panggung."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Aku nggak usah keluar ke kursi penonton deh, Moemoe-senpai. Biar aku tetap di belakang panggung sini aja bantu jagain tas, sepatu ganti, sama perlengkapan jahit darurat Senpai."
            nar "Mata biru Moeka langsung melebar senang mendengar tawaranmu."
            moeka "Eh, kamu beneran mau menunggu aku di belakang panggung sini, Chimian? Padahal dari sini panggungnya cuma kelihatan dari celah tirai samping lho."
            chiasa "Nggak apa-apa, dari samping tirai juga tetap kelihatan jelas kok. Lagian kalau Senpai sendirian di sini sambil pegang peniti sama gantungan baju, nanti malah makin panik."
            moeka "Aduh, kamu penyelamat banget! Jujur aja dari tadi tanganku rasanya gemetar kalau disuruh memasang peniti punggung sendiri."
            chiasa "Sini biar kubantu rapikan lipatan kerah belakangnya dulu, Senpai putar badan sedikit."
            moeka "Hati-hati jangan sampai renda pinggirnya terlipat ke dalam ya, Chimian."
            chiasa "Aman, sudah lurus semua dari bahu kiri sampai kanan."
            nar "Selama sepuluh menit menjelang gilirannya naik panggung, kamu membantunya mengenakan jaket denim rancangannya serta memegang kotak peralatan jahitnya tanpa mengubah satu detail pun dari konsep aslinya."
            nar "Ketika koordinator panggung memanggil nama Moeka untuk bersiap di urutan berikutnya tepat di balik tirai hitam, Moeka menarik napas dalam-dalam, lalu menoleh kepadamu dengan suara setengah berbisik."
            moeka "Chimian... pinjam tanganmu sebentar, boleh? Dua detik aja sebelum aku keluar."
            chiasa "Sini, Senpai. Pegang aja."
            nar "Kamu mengulurkan kedua tanganmu. Moeka menggenggam jari-jarimu erat-erat, merasakan hangat telapak tanganmu sambil memejamkan mata selama dua tarikan napas panjang. Saat ia membuka matanya lagi, getaran di ujung jarinya sudah berhenti."
            moeka "Oke, sudah hangat sekarang. Doain aku nggak kesandung tangga ya, tunggu di sini sampai aku balik!"
            chiasa "Pasti kutunggu di sini, Senpai. Semangat!"
            nar "Ia melepaskan genggamannya, lalu melangkah mantap menembus celah tirai menuju sorot lampu panggung yang terang benderang."
            nar "Dari celah sempit di samping tirai beludru hitam, kamu memperhatikan Moeka melangkah di atas panggung dengan punggung tegak dan senyum lebar yang memancarkan kebanggaan atas jaket hasil jahitannya sendiri."
            nar "Tepuk tangan penonton di dalam aula terdengar bergemuruh saat ia berhenti sejenak di ujung lintasan untuk memperlihatkan detail renda pada kerah dan manset lengannya."
            nar "Begitu gilirannya selesai dan ia kembali masuk melewati tirai belakang panggung, Moeka langsung menghampirimu dengan mata berbinar dan napas yang masih sedikit terengah."
            moeka "Chimian! Rasanya lega banget! Begitu keluar tirai tadi kakiku langsung ringan!"
            chiasa "Bagus banget jalannya tadi, Moemoe-senpai! Nih, minum dulu airnya sebentar sebelum ganti sepatu."
            moeka "Makasih banyak ya sudah jagain aku di belakang tirai sini, Chimian!"
            nar "Moeka menerima botol air minum darimu dengan senyum cerah yang kali ini benar-benar lepas dari segala ketegangan."
        else:
            yutaka "Daripada aku cuma duduk di depan, mending aku tetap di belakang panggung sini aja bantu jagain tas sama barang-barang cadanganmu, Kohinata. Biar kamu nggak usah bolak-balik mengecek barang sambil menunggu giliran."
            moeka "Eh, serius kamu mau menunggu di belakang panggung yang sempit dan ribut begini, Yutayuta?"
            yutaka "Nggak masalah. Kalau kamu berdiri sendirian di pojok sini sambil menunggu nama dipanggil, kepalamu malah makin penuh memikirkan hal yang nggak-nggak."
            moeka "...Iya sih, kamu benar banget. Makasih ya, Yutayuta. Tolong pegangin tas kain sama kotak jarumku itu sebentar ya, aku mau kenakan jaketnya sekarang."
            yutaka "Sip, botol air minummu juga kubawakan di sini kalau tenggorokanmu kering."
            moeka "Coba lihat sebentar, kerah bagian belakangnya sudah rapi belum?"
            yutaka "Ujung kirinya agak terlipat sedikit... tahan sebentar, sudah kuluruskan. Rapi sekarang."
            nar "Selama sepuluh menit berikutnya, kamu berdiri di dekat cermin membantu menjaga barang-barang di sekitarnya sehingga ia bisa fokus penuh pada pakaiannya sendiri."
            nar "Tepat ketika panitia panggung memberi isyarat satu menit lagi sebelum gilirannya keluar ke lintasan, Moeka berdiri di samping tirai hitam sambil mengepalkan kedua tangannya yang masih tampak dingin. Ia menoleh padamu dengan suara pelan."
            moeka "Yutayuta... boleh pinjam tanganmu sebentar nggak? Dua detik aja."
            yutaka "Nih. Pegang aja, tarik napas pelan-pelan."
            nar "Moeka menggenggam tangan kananmu dengan kedua tangannya yang dingin selama beberapa detik sambil memejamkan mata rapat-rapat. Begitu ia mengembuskan napas dan membuka matanya kembali, raut tegang di wajahnya sudah jauh berkurang."
            moeka "Sip, sudah nggak gemetar lagi. Tunggu di dekat tirai sini ya, jangan pergi dulu sampai aku balik dari panggung!"
            yutaka "Aku nggak ke mana-mana. Jalan santai aja di atas sana."
            nar "Ia melepaskan tanganmu sambil tersenyum mantap, lalu melangkah keluar memasuki sorot lampu panggung ketika namanya dipanggil."
            nar "Dari balik lipatan tirai samping, kamu menyaksikan bagaimana langkah Moeka yang tadinya sempat tegang langsung berubah luwes mengikuti ketukan musik pengiring."
            nar "Sorot lampu putih panggung memantulkan detail renda putih pada jaket denim rancangannya dengan sangat jelas di hadapan meja para dosen penguji."
            nar "Ketika ia berbalik dan melangkah masuk kembali ke lorong persiapan diiringi tepuk tangan meriah dari ruang aula, wajahnya tampak berseri-seri penuh kelegaan."
            moeka "Yutayuta! Aku berhasil melewati putaran ujung panggungnya tanpa salah langkah sedikit pun!"
            yutaka "Kerja bagus, Kohinata. Nih botol airmu, minum dulu sebelum kita bereskan gantungan bajunya."
            moeka "Hehe, makasih banyak sudah nungguin persis di balik tirai sesuai janji ya, Yutayuta!"
            nar "Moeka meneguk air minumnya sambil tertawa ringan, menikmati keberhasilan peragaan busana pertamanya dengan tenang di sampingmu."
    else:
        if kk_host == "chiasa":
            chiasa "Maaf banget ya, Moemoe-senpai. Aku tadi mampir ke ruang tunggu cuma buat menyemangati sebentar, soalnya habis ini aku masih ada urusan lain yang nggak bisa ditinggal jadi harus pergi sekarang."
            nar "Tangan Moeka yang masih memegangi kerah jaket denimnya terdiam sesaat, lalu ia segera mengangkat wajah dan memasang kembali senyum cerahnya yang biasa."
            moeka "Oh, kamu masih ada urusan lain ya? Nggak apa-apa kok, Chimian! Kamu sudah menyempatkan mampir ke ruang belakang sini sebelum acara mulai aja aku sudah senang banget."
            chiasa "Maaf ya nggak bisa lihat waktu Senpai jalan di panggung. Semoga lancar ya peragaannya."
            moeka "Pasti lancar dong! Nanti kalau ada foto dari panitia, kukirim ke kamu deh! Hati-hati di jalan ya, Chimian, sampai ketemu besok di kampus!"
            nar "Kamu melambai singkat lalu keluar meninggalkan ruang persiapan sebelum acara dimulai. Di belakang panggung yang bising, Moeka mengenakan jaketnya seorang diri, merapikan kerahnya di depan cermin tanpa bantuan siapa pun, lalu melangkah naik ke panggung saat gilirannya tiba."
            nar "Saat melewati koridor luar gedung aula menuju gerbang fakultas, suara musik pembuka dan tepuk tangan penonton dari dalam ruangan terdengar samar menembus pintu kayu."
            nar "Di dalam sana, tidak ada satu pun penonton di barisan depan maupun rekan di balik tirai yang mengetahui betapa dingin ujung jari Moeka sesaat sebelum namanya dipanggil."
            nar "Ia tetap memaksa dirinya berdiri tegak seorang diri di tengah keramaian kru belakang panggung seperti yang selama ini selalu ia lakukan di rumah maupun di kampus."
            nar "Ia tetap berjalan dengan senyum lebar yang berkilau di bawah lampu sorot dan melambai ramah setiap kali kamera panitia memotretnya. Baru ketika seluruh penonton sudah meninggalkan aula dan ruang tunggu kembali kosong, Moeka duduk sendirian di kursi lipat sambil merapikan jaketnya ke dalam tas dengan bahu yang tampak sangat letih."
        else:
            yutaka "Maaf banget, Kohinata. Aku tadi mampir ke belakang sini cuma buat menyapa sebentar, habis ini aku ada urusan lain di luar yang nggak bisa ditunda jadi harus langsung jalan."
            nar "Jari Moeka yang memegangi kerah jaketnya sempat berhenti, tetapi hanya dalam hitungan detik ia sudah kembali menarik senyum lebarnya seperti biasa."
            moeka "Oh, ada urusan lain ya? Santai aja kali, Yutayuta! Kamu sudah menyempatkan mampir ke lorong belakang buat lihat jaketku aja aku sudah senang kok."
            yutaka "Semoga peragaan pertamanya lancar ya, Kohinata. Aku duluan."
            moeka "Siap, pasti kuberikan pertunjukan paling keren! Nanti kukirimin fotonya dari panitia. Hati-hati di jalan ya!"
            nar "Kamu berpamitan lalu berjalan keluar meninggalkan gedung aula sebelum tirai panggung dibuka. Moeka mengenakan jaket rancangannya seorang diri di sudut lorong, lalu tetap tampil memukau dan tersenyum cerah ke arah kamera sepanjang gilirannya di atas panggung."
            nar "Begitu pintu belakang gedung aula tertutup di punggungmu, dentuman musik peragaan busana dan riuh tepuk tangan penonton mulai bergema dari arah dalam."
            nar "Tanpa ada orang terdekat yang menunggu di kursi depan ataupun menjaga barangnya di balik tirai, Moeka kembali memikul sendiri seluruh rasa gugupnya di balik topeng ceria."
            nar "Para peserta lain tampak langsung dikerubungi teman-teman mereka begitu turun dari tangga panggung, sedangkan Moeka langsung berjalan menepi ke sudut rak pakaian."
            nar "Sesudah acara berakhir dan para mahasiswa lain pulang bersama teman-teman yang datang menonton mereka, Moeka membereskan gantungan bajunya seorang diri di ruang tunggu yang sudah sepi, lalu berjalan pulang ke kosnya dengan rasa lelah yang ia simpan rapat-rapat."
    return

init 1 python:
    _hook("H20-A", lambda: kk_rel("harumi","intim",5))
    _hook("H20-B", lambda: kk_rel("harumi","trust",-3))
    _hook("H20-C", lambda: (kk_rel("harumi","intim",4), kk_adj("kejelasan_harumi",5)))
    _hook("H21-A", lambda: (kk_rel("harumi","trust",6), kk_flag("harumi_studi_didukung")))
    _hook("H21-B", lambda: (kk_adj("kejelasan_harumi",6), kk_flag("harumi_diminta_tinggal")))
    _hook("H21-C", lambda: (kk_rel("harumi","intim",6), kk_flag("harumi_diikuti")))
    _hook("H23-A", lambda: (kk_rel("harumi","trust",5), kk_flag("harumi_ujian_dibantu")))
    _hook("H23-B", lambda: kk_rel("harumi","trust",-5))
    _hook("H23-C", lambda: kk_rel("harumi","aff",4))
    _hook("Mo07-A", lambda: (kk_rel("moeka","aff",5), kk_flag("moeka_peragaan_dihadiri")))
    _hook("Mo07-B", lambda: (kk_rel("moeka","intim",5), kk_adj("stres_moeka",-5)))
    _hook("Mo07-C", lambda: kk_rel("moeka","aff",-3))
