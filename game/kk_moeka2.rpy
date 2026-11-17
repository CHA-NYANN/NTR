# Arc Moeka lanjutan (Mo13-Mo24, Mo25): topeng -> isolasi -> tanda bahaya ->
# klimaks. Mo19 (membagikan barang) dan Mo21 (tertawa keras) adalah tanda bahaya
# klasik; jendela intervensi dibuat bermakna. Mo25 TIDAK mendepiksi tindakan apa
# pun: ia bercabang pada apakah pemain mengisi jendela-jendela itu — tertolong
# tepat waktu, atau sebuah kehilangan yang disampaikan sebagai akibat, tanpa
# metode. Eksploitasi Kuga = konsekuensi saja. Penempatan Kantin Pusat prototipe.

# ┌─ PANDUAN CERITA · Mo13 · Foto yang Beredar
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : rumor Mei tentang Moeka.
# │ INTI    : A bantu bantah / B diam / C manfaatkan.
# │ AKHIRAN : topeng tebal.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo13:
    call kk_scene_enter("moeka", "Kantin Pusat · Foto beredar")
    nar "Foto pekerjaan Moeka beredar bersama keterangan yang tidak pernah ia berikan. Nama Kuga disebut sedikit, nama Moeka dibahas panjang. Di kantin seseorang menanyakan bayarannya dengan nada yang membuat pertanyaan itu terasa seperti penghinaan."
    moeka "Itu kerjaan. Kalian lihat baju yang kubuat juga, kan? Bukan cuma hal yang kalian bayangkan sendiri."
    call kk_family_menu("Mo13", ["Bantu bantah rumor itu.", "Diam saja.", "Manfaatkan rumor itu."])
    if _return == "A":
        moeka "Kau membelaku di depan mereka? ...Tidak banyak yang mau ambil risiko begitu untukku."
        nar "Kau membantah dugaan sebagai fakta tanpa memaksa Moeka menunjukkan rincian pribadi untuk dianggap pantas dibela. Ia berhenti tertawa ketika tahu kau mendengarkan keberatannya dengan serius."
    elif _return == "B":
        nar "Kau diam. Moeka mulai menjawab sindiran dengan lelucon lebih dulu agar orang lain tidak mendapat kesempatan membuatnya terlihat tersinggung."
        nar "Keramahan itu membuat meja kembali ramai. Ia pulang membawa kesan bahwa bahkan harga dirinya harus dilindungi dengan membuat orang lain merasa terhibur."
    else:
        nar "Kau memakai rumor untuk membuatnya semakin bergantung pada keberpihakanmu. Moeka mendengar tawaran dukungan sebagai sesuatu yang mungkin hilang jika ia tidak menuruti keinginanmu."
        moeka "Aku kira kamu mau mendengar versiku. Bukan menentukan apa yang harus kuberikan supaya kamu mau percaya."
        nar "Kalimat itu keluar sekali, lalu ia menunduk sebelum tahu apakah aman untuk mempertahankannya."
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
    nar "Moeka membawa cerita baru untuk setiap meja. Ia tertawa lebih keras ketika tidak ada yang menjawab, menyambung satu lelucon dengan yang lain sebelum keheningan sempat mengembalikan percakapan kepadanya."
    moeka "Lihat, masih bisa bikin kalian ketawa. Berarti belum kalah sama minggu ini, ya."
    call kk_family_menu("Mo14", ["Tanyakan apa ia benar-benar baik.", "Percaya pada senyumnya.", "Manfaatkan keceriaannya."])
    if _return == "A":
        moeka "Baik? Tentu. ...Kenapa kau bertanya begitu? Apa kelihatan tidak?"
        nar "Kau mengatakan ia tidak perlu membuktikan apa pun dari wajahnya dan boleh memilih cerita yang tidak lucu. Moeka memegang ujung meja, mempertimbangkan tawaran itu cukup lama hingga senyumnya turun sendiri."
        moeka "Aku belum tahu bisa mulai dari mana. Boleh duduk dulu tanpa cerita?"
    elif _return == "B":
        nar "Kau mengatakan senang ia sudah membaik. Moeka menerima pujian itu, lalu bekerja lebih keras agar perkataanmu tetap tampak benar."
        nar "Saat akhirnya sendirian, wajahnya jatuh dengan lelah yang tak boleh masuk ke foto berikutnya. Kini mengatakan sedang buruk juga terasa seperti mengecewakan keyakinanmu."
    else:
        nar "Kau menambah permintaan karena ia terlihat sanggup. Moeka menjawab bisa sebelum melihat jadwal, menyelipkan satu tugas lagi di hari yang sudah tidak punya ruang."
        moeka "Tenang, aku urus. Kalau aku kelihatan nggak capek, mungkin tubuhku ikut percaya."
        nar "Ia tertawa sesudahnya. Kau mendapatkan bantuan dari seseorang yang baru saja memberitahumu betapa keras ia berusaha menyembunyikan batas."
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
    nar "Moeka mengeluarkan surat peringatan dari tas setelah semua orang pergi. Lipatannya sudah lemah karena dibuka berkali-kali, tetapi belum ditunjukkan kepada siapa pun."
    moeka "Aku baca bagian kalau nilainya turun lagi terus. Nggak ada bagian kalau mahasiswanya sudah berusaha mati-matian tapi tetap kehabisan waktu. Aku tahu surat memang bukan tempat begitu. Aku cuma... ingin ada yang dengar."
    call kk_family_menu("Mo15", ["Hadir dan dengarkan sampai habis.", "Bantu ia mencari jalan keluar nyata.", "Abaikan."])
    if _return == "A":
        moeka "Kau mau menemani sampai aku selesai bicara? ...Itu saja sudah menahan satu hal dari runtuh."
        nar "Ia mulai dari angka, lalu berhenti pada takut memberi kabar kepada ibunya. Kau tidak mengatakan pasti lolos. Kau mendengarkan sampai ia berani mengakui masih ingin kuliah, bukan sekadar takut kehilangan pembiayaannya."
    elif _return == "B":
        moeka "Kau mau bantu cari bantuan? Beasiswa darurat, kerja paruh waktu... mungkin masih ada pintu."
        nar "Kalian mencari orang yang dapat ditanya, memeriksa tenggat banding, dan membicarakan beban yang justru harus dikurangi. Moeka mencatat satu nama kontak sebelum menerima pekerjaan tambahan sebagai jawaban otomatis."
    else:
        nar "Kau tidak tinggal pada pembicaraan itu. Moeka melipat surat, mengembalikannya ke tas, lalu meminta maaf sudah membuat suasana tegang."
        nar "Besok surat yang sama akan tetap menuntut jawaban. Malam ini ia belum menemukan tempat untuk mengatakan bahwa dirinya tidak sanggup menjawab sendirian."
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

# ┌─ PANDUAN CERITA · Mo18 · Rina Bicara
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : Rina menegur pemain.
# │ INTI    : A dengarkan / B tolak / C bela diri.
# │ AKHIRAN : sekutu atau lawan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo18:
    call kk_scene_enter("moeka", "Kantin Pusat · Rina bicara")
    nar "Rina menunggumu setelah kegiatan selesai. Ia tidak membawa gosip atau pertanyaan tentang siapa yang sedang disukai Moeka. Di tangannya ada daftar pertemuan yang belakangan dibatalkan sahabatnya."
    "Rina" "Aku khawatir. Ini sudah lebih dari sibuk atau salah jadwal. Aku ingin kita menghubungi dia dan cari bantuan kalau perlu. Jangan tunggu sampai kita harus menyesal karena semua orang mengira orang lain sudah bertanya."
    call kk_family_menu("Mo18", ["Dengarkan peringatan Rina.", "Tolak ikut campur.", "Bela diri bahwa itu bukan salahmu."])
    if _return == "A":
        "Rina" "Terima kasih mau dengar. Aku tidak tahu harus minta tolong ke siapa lagi."
        nar "Kalian membicarakan apa yang benar-benar diketahui dan siapa yang dekat secara fisik malam ini. Rina tidak memintamu menjadi satu-satunya penanggung jawab; justru ia ingin lingkar dukungan Moeka lebih luas daripada satu telepon."
    elif _return == "B":
        "Rina" "...Begitu. Kukira kau berbeda. Maaf sudah mengganggu."
        nar "Ia pergi untuk mencari orang lain. Penolakanmu membuat jalannya lebih sulit, tetapi tidak memberinya alasan membiarkan Moeka hanya ditangani oleh kesediaanmu peduli."
    else:
        "Rina" "Tidak ada yang menyalahkanmu. Aku cuma minta kau tidak menambah beratnya."
        nar "Kau membela catatan bantuanmu sendiri. Rina mendengar, lalu mengatakan pembicaraan ini tentang keadaan Moeka sekarang, bukan pertandingan tentang siapa paling bersih dari kesalahan."
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

# ┌─ PANDUAN CERITA · Mo22 · Ren Menelepon
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : adiknya khawatir.
# │ INTI    : A datang / B kirim uang / C tidak.
# │ AKHIRAN : jendela #4.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo22:
    call kk_scene_enter("moeka", "Kantin Pusat · Ren menelepon")
    "Ren" "Kak Moeka nggak menjawab tiga hari. Terakhir bilang baik-baik saja, tapi kalau memang baik, biasanya dia yang terus bertanya aku sudah makan apa. Bisa lihat dia? Aku nggak tahu harus menghubungi siapa lagi."
    nar "Ia mencoba terdengar tenang, menanyakan alamat yang bahkan tak bisa ia datangi sendiri malam itu. Kekhawatirannya lebih besar daripada usianya."
    call kk_family_menu("Mo22", ["Datang menengok Moeka.", "Kirim uang untuk keluarganya.", "Tidak melakukan apa-apa."])
    if _return == "A":
        moeka "Ren meneleponmu? ...Dasar. Dia tidak perlu mengkhawatirkanku. ...Tapi kau datang."
        nar "Kau mengabari kedatanganmu dan memastikan keluarganya menerima kabar yang jujur. Moeka memandang ponsel lama sebelum menelepon adiknya."
        moeka "Aku belum baik. Tapi aku ditemani sekarang. Kamu boleh berhenti berjaga menunggu telepon, ya."
    elif _return == "B":
        nar "Kau mengirim bantuan uang. Kebutuhan rumah mendapat ruang bernapas, tetapi pertanyaan Ren tentang keberadaan kakaknya belum terjawab."
        nar "Moeka mengucapkan terima kasih melalui pesan. Kau belum mendengar suaranya, belum mengetahui apakah kata terima kasih itu satu-satunya kalimat yang masih mampu ia susun malam ini."
    else:
        nar "Kau tidak bertindak. Ren mengatakan akan mencoba menelepon lagi, suaranya makin kecil ketika kehabisan pertanyaan yang bisa diajukan kepadamu."
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
        nar "Kabar datang keesokan hari. Rina menelepon, mengucapkan nama Moeka dua kali sebelum sanggup menyelesaikan kalimat. Di kampus jadwal masih menuliskan giliran presentasinya. Orang-orang berulang kali menanyakan siapa yang sudah mengetahui, seolah jawaban itu dapat membuat peristiwa menjadi lebih mungkin dipercaya."
        nar "Aya menerima kabar di rumah. Adik-adiknya masih harus diberi tahu. Ada pekerjaan yang akan tetap menunggu, kain yang belum dipotong, dan hal kecil yang sekarang memerlukan seseorang mengambilnya dari kamar tanpa pemiliknya berkata tunggu, yang itu jangan dibuang."
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
