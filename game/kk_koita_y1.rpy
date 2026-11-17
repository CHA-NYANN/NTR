# Lapisan kesadaran Koita, Tahun 1 (K01, K03, K06, K09, K10, K11).
# Koita adalah aktor yang membalas (NPC mandiri). Event observasional: pemain membaca pola,
# Koita mulai merasa diperhatikan. Efek mengikuti Event_Koita; angka adalah setelan prototipe.
# Gerbang rute BL/Koita-Success (K04-D, K10-A) TIDAK dibangun di sini.
# ┌─ PANDUAN CERITA · K01 · Senyum yang Terlalu Cepat
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : kantin hari pertama; Koita menyapa tiga heroine dengan tiga kalimat berbeda.
# │ INTI    : A amati dan catat polanya / B tegur terang-terangan / C abaikan.
# │ AKHIRAN : A membuka pola_koita_dikenal (intel); B membuat Koita waspada ringan; C tidak ada.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K01:
    call kk_scene_enter("koita", "Gedung Sastra")
    nar "Koita menahan kursi dengan lutut agar Nagisa bisa meletakkan nampannya. Belum sempat duduk, ia sudah melambaikan tangan kepada Miyuki yang lewat membawa map."
    koita "Senpai, sudah makan? Jangan kopi lagi, ya. Kemarin katanya perutmu nggak enak."
    miyuki "Ara, masih ingat? Senpai jadi terharu."
    nagisa "Kalau ingat begitu hebat, ingat juga janjimu mengembalikan catatanku."
    koita "Ada di tas. Sengaja kubawa supaya punya alasan duduk sama kamu."
    nar "Nagisa mendengus, tetapi bergeser memberinya tempat. Di belakangnya Harumi muncul; Koita segera mengangkat buku yang tadi menjadi alas nampan."
    koita "Harumi, aku sudah baca rekomendasimu. Nanti jelaskan bagian akhirnya, ya. Aku mau dengar pendapatmu dulu."
    nar "Tiga sambutan, tiga cara membuat seseorang merasa ditunggu. Senyum Koita datang sedikit lebih cepat daripada jawaban mereka."
    call kk_family_menu("K01", ["Amati dan catat polanya diam-diam.", "Tegur terang-terangan bahwa ia pilih kasih.", "Abaikan saja."])
    if _return == "A":
        nar "Kau memperhatikan siapa yang ia tatap ketika menyebut nanti. Tak ada waktu atau tempat yang benar-benar disepakati, tetapi masing-masing mendapat bagian kecil dari masa depannya."
        koita "Kamu diam saja. Mau duduk juga?"
        nar "Ia sudah menggeser kursi sebelum kau menjawab. Keramahannya nyata; begitu pula betapa cepat ia memeriksa apakah keramahan itu berhasil."
    elif _return == "B":
        nar "Kau menyebut caranya memberi perhatian khusus kepada semua orang. Percakapan di meja berhenti."
        koita "Pilih kasih? Aku cuma ingat hal-hal tentang teman. Kamu juga begitu, kan?"
        nagisa "Memangnya harus diributkan di kantin?"
        nar "Koita tertawa untuk meredakan keadaan, tetapi sejak itu ia beberapa kali melihatmu sebelum menyapa orang lain."
    else:
        nar "Kau menarik kursi dan membicarakan jadwal kuliah. Koita menyambut topik itu dengan mudah."
        nar "Miyuki melanjutkan langkah, Harumi menyimpan bukunya, Nagisa membuka catatan. Masing-masing pergi membawa percakapan yang terasa berbeda dari percakapan yang kaudengar secara utuh."
    return

# ┌─ PANDUAN CERITA · K03 · Tanzaku Koita
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : aula Tanabata; tanzaku Koita: "semoga semuanya tetap seperti ini".
# │ INTI    : A baca diam-diam / B tukar dengan tanzaku lain / C tulis balasan di sebelahnya.
# │ AKHIRAN : A memberi ketakutan_koita; B bisa menjadi sabotase kecil; C membuat Koita merasa "dilihat".
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K03:
    call kk_scene_enter("koita", "Gedung Sastra · Tanabata")
    nar "Keinginan lain di dahan bambu cukup tegas: lolos ujian, dapat pekerjaan, menyatakan cinta. Kertas biru muda milik Koita hanya berisi satu baris."
    nar "Semoga semuanya tetap seperti ini."
    nar "Di bawahnya ada bekas huruf yang dicoret. Kau masih bisa membedakan awal sebuah kata, jangan, sebelum coretan hitam menutup sisanya."
    koita "Punyaku nggak ambisius, ya. Yang lain minta masa depan. Aku malah meminta hari ini diperpanjang."
    call kk_family_menu("K03", ["Baca diam-diam lalu tinggalkan.", "Tukar diam-diam dengan tanzaku lain.", "Tulis balasan di tanzaku sebelahnya."])
    if _return == "A":
        nar "Kau tidak mengomentarinya. Koita tersenyum lega dan beranjak ke meja spidol."
        nar "Sesaat kemudian ia kembali hanya untuk memastikan tali kertasnya terikat kuat. Tidak ada angin yang cukup kencang untuk menjatuhkannya."
        nar "Kau mengingat gerakan itu lebih jelas daripada kalimatnya: seseorang yang memeriksa apakah sebuah permintaan sudah cukup aman untuk ditinggalkan."
    elif _return == "B":
        nar "Ketika Koita membelakangimu, kau menukar tempat kertasnya dengan tanzaku dari dahan bawah. Keinginannya masih ada, hanya tidak lagi mudah terlihat."
        koita "Tadi aku menggantungnya di sini... ah, ketemu."
        nar "Ia membungkuk membaca kertasnya sendiri. Lalu ia memperbaiki letaknya tanpa bertanya kepada siapa pun. Usikan sekecil itu sudah cukup membuatnya memeriksa sekeliling."
    else:
        nar "Kau menulis: kalau ada yang berubah, semoga kita berani membicarakannya. Kertasmu kauikat di sebelah kertas birunya."
        koita "Itu balasan buat aku?"
        nar "Ia membacanya lagi sebelum kau sempat menjawab."
        koita "Aku biasanya menganggap diam itu berarti semuanya masih baik. Padahal mungkin cuma aku yang nggak bertanya, ya."
        nar "Kalian berdiri di bawah dua keinginan yang tidak menjanjikan hal yang sama. Koita tidak memindahkan salah satunya."
    return

# ┌─ PANDUAN CERITA · K06 · Foto Reuni
# │ LOKASI  : Kampus Kouseikan · Kafe Komorebi
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : Koita meminta foto kelompok; ia berdiri di tengah.
# │ INTI    : A ambil foto / B ikut berfoto dan geser posisi / C ganti fotografer.
# │ AKHIRAN : foto menjadi bukti digital () tentang siapa dekat siapa.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K06:
    call kk_scene_enter("koita", "Kafe Komorebi")
    nar "Cangkir di Komorebi sudah dikumpulkan, tetapi tak seorang pun ingin menjadi yang pertama mengatakan pulang. Koita mengambil ponselnya."
    koita "Foto dulu, yuk. Sudah lama nggak lengkap begini."
    nar "Ia berdiri di tengah tanpa perlu diminta. Nagisa bergerak ke satu sisinya; Miyuki ragu sepersekian detik di sisi lain. Harumi mundur agar tidak menutupi papan menu, lalu nyaris keluar bingkai."
    koita "Harumi, dekat sedikit. Nggak usah sejauh itu."
    nar "Ia mengucapkannya sambil menoleh kepada Miyuki, memastikan sang senpai masih tersenyum."
    call kk_family_menu("K06", ["Ambilkan fotonya dari luar bingkai.", "Ikut berfoto dan geser posisimu.", "Minta orang lain yang memotret."])
    if _return == "A":
        nar "Kau mundur sampai semua masuk layar. Hitungan ketiga menangkap tangan yang hampir menyentuh, bahu yang menegang, dan senyum yang tiba tepat pada waktunya."
        koita "Kirim ke grup, ya. Jangan pilih yang aku merem."
        nar "Kau menyimpan foto aslinya. Di layar, jarak beberapa sentimeter terlihat remeh. Kau ingat siapa yang bersusah payah mempertahankannya."
    elif _return == "B":
        nar "Kau meminta ruang di tengah dan menyelipkan diri ke dalam kelompok. Koita bergeser, membuat seluruh susunan ikut berubah."
        nagisa "Eh, tunggu. Kalau begitu tasku keinjak."
        koita "Kita geser semua saja. Pelan-pelan."
        nar "Foto akhirnya lebih berantakan dan lebih hidup. Saat memeriksa hasilnya, Koita memperbesar gambar sekali, melihat tempatmu berdiri, lalu mengecilkannya lagi."
    else:
        nar "Kau meminta bantuan pelayan dan bergabung di ujung. Ia mengarahkan semua orang merapat; kini posisi kalian ditentukan oleh orang yang hanya ingin segera selesai memotret."
        koita "Satu lagi, boleh? Yang tadi kayaknya aku belum siap."
        nar "Pada foto kedua ia sudah tersenyum. Ketika kedua gambar masuk grup, orang-orang memilih versi yang berbeda sebagai favorit."
    return

# ┌─ PANDUAN CERITA · K09 · Omikuji Koita
# │ LOKASI  : Alam & Pantai · Kuil
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : kuil; ia menarik ramalan "pilihanmu akan datang".
# │ INTI    : A tanyakan / B tertawakan / C ancam.
# │ AKHIRAN : mulai tumbuh rasa takut; kunci K15.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K09:
    call kk_scene_enter("koita", "Kuil · Tahun Baru")
    nar "Jari Koita kedinginan ketika membuka omikuji. Ia membacakan bagian studi dan kesehatan dengan nada pembawa acara, lalu berhenti pada bagian hubungan."
    koita "Pilihanmu akan datang. Jangan mengira diam menghentikan waktu."
    nar "Ia membalik kertas, mencari kelanjutan yang bisa membuat kalimat itu terdengar lucu. Bagian belakang kosong."
    koita "Agak galak untuk ramalan Tahun Baru, ya. Aku bahkan belum merasa harus memilih."
    call kk_family_menu("K09", ["Tanyakan pilihan apa yang ia maksud.", "Tertawakan ramalan yang samar itu.", "Katakan ia tak perlu memikirkannya."])
    if _return == "A":
        koita "Entah. Itu masalahnya. Begitu dibaca, aku langsung kepikiran beberapa orang. Kalau benar-benar nggak ada pilihan, harusnya aku nggak kepikiran siapa-siapa, kan?"
        nar "Ia menghangatkan jari dengan napas, tetapi kertas itu tetap terbuka."
        koita "Aku takut salah memilih. Tapi mungkin selama ini orang lain yang menanggung ketakutanku."
    elif _return == "B":
        nar "Kau tertawa dan mengatakan kalimat itu bisa berlaku untuk memilih makan siang. Koita ikut tertawa, kali ini sedikit terlambat."
        koita "Benar. Kalau begitu aku pilih mi. Selesai, takdir sudah dipenuhi."
        nar "Ia melipat kertas dengan rapi, jauh lebih rapi daripada leluconnya memerlukan. Ketika kalian turun dari kuil, ia masih meraba saku tempat menyimpannya."
    else:
        nar "Kau mengatakan ia tak perlu membiarkan selembar ramalan mengatur hidupnya. Koita mengangguk cepat."
        koita "Iya. Aku nggak perlu memikirkannya sekarang."
        nar "Penekanan pada sekarang terdengar seperti batas waktu yang baru ia tetapkan sendiri. Ia menyimpan kertas itu, tidak mengikatnya pada tempat ramalan buruk."
    return

# ┌─ PANDUAN CERITA · K10 · Coklat yang Tidak Habis
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : Valentine; Koita menerima banyak coklat.
# │ INTI    : A pemain memberi coklat / B amati siapa yang tidak memberi / C bantu menghabiskan.
# │ AKHIRAN : gerbang BL/Koita Success. Male: A membuka rantai BL. Female: A membuka jalur Chiasa × Koita.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K10:
    call kk_scene_enter("koita", "Gedung Sastra · Valentine")
    nar "Pita merah, stiker toko, kotak kecil yang sudutnya penyok karena dibawa di dalam tas. Hadiah Valentine menutupi separuh meja Koita. Ia memindahkan semuanya dengan hati-hati agar tak terlihat sedang menyusun peringkat."
    koita "Aku harus ingat yang mana dari siapa. Tahun lalu salah mengucapkan terima kasih, malu sekali."
    nar "Ia tersenyum, tetapi sesekali matanya mencari pintu. Jumlah di meja ternyata belum cukup menjawab siapa yang masih akan datang."
    call kk_family_menu("K10", ["Beri ia satu coklat darimu juga.", "Amati siapa yang justru tidak memberi.", "Bantu ia menghabiskan yang menumpuk."])
    if _return == "A":
        nar "Kau meletakkan hadiahmu di depannya. Koita baru mengulurkan tangan ketika kau menyebut bahwa ini memang untuknya."
        koita "Dari kamu juga? Aku nggak tahu kamu... menyiapkan."
        nar "Ia hampir menyebutnya kejutan dari teman, lalu berhenti sebelum kata terakhir keluar."
        koita "Boleh kubuka nanti? Sendiri. Aku mau membacanya tanpa orang lain melihat dulu."
        nar "Hadiahmu ia taruh di dalam tas, terpisah dari tumpukan meja. Itu belum sebuah jawaban, tetapi kali ini ia tidak buru-buru mengubah pertanyaannya."
    elif _return == "B":
        nar "Kau mengamati orang yang melambai lalu lewat, orang yang memilih pintu lain, dan orang yang membawa bingkisan tetapi menyimpannya lagi. Tidak semua ketidakhadiran berarti hal yang sama."
        koita "Kamu lihat seseorang di luar?"
        nar "Ia berusaha bertanya ringan. Kau mulai mengenali bahwa bagian terpenting dari mejanya justru tempat kosong yang hanya ia lihat sendiri."
    else:
        nar "Koita memisahkan kotak yang boleh dibagi dari kotak dengan pesan pribadi. Kali ini kau menunggu ia yang membukanya sebelum mengambil."
        koita "Yang ini banyak. Katanya memang buat ramai-ramai."
        nar "Kalian makan sambil membicarakan kuliah. Setelah beberapa menit, ia berhenti menghadap pintu."
        koita "Aku suka begini. Nggak perlu menebak apa artinya."
        nar "Ia mengucapkannya dengan lega yang membuat tumpukan hadiah di antara kalian terasa sedikit lebih berat."
    return

# ┌─ PANDUAN CERITA · K11 · Hadiah yang Sama
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : White Day; Koita membalas semua dengan hadiah yang sama.
# │ INTI    : A kritik / B bantu ganti / C biarkan.
# │ AKHIRAN : heroine sadar mereka "disamakan"; menaikkan kecurigaan antar heroine.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K11:
    call kk_scene_enter("koita", "Gedung Sastra · White Day")
    nar "Koita mengeluarkan kantong-kantong White Day dari tas belanja. Semua berpita sama. Semua berisi biskuit yang sama, bahkan kartu kecilnya memiliki kalimat cetak yang sama."
    koita "Kupikir kalau ada yang lebih mahal, nanti malah nggak enak. Jadi kubuat adil."
    nar "Ia mengatakannya sebelum ada yang bertanya. Di dekat pintu, dua penerima membandingkan kantong mereka, lalu berhenti tersenyum pada saat yang hampir bersamaan."
    call kk_family_menu("K11", ["Kritik bahwa menyamakan semua orang itu ceroboh.", "Bantu ia mengganti beberapa dengan yang berbeda.", "Biarkan saja."])
    if _return == "A":
        nar "Kau mengingatkan bahwa sebagian hadiah sebelumnya adalah pengakuan, bukan kewajiban bertukar makanan. Balasan seragam membiarkan semua pertanyaan itu tetap terbuka."
        koita "Kalau kubedakan, mereka tahu aku..."
        nar "Ia berhenti. Kalimat yang tak diselesaikannya menjelaskan lebih banyak daripada pembelaan tentang keadilan."
        koita "Aku takut ada yang sedih. Tapi aku juga takut ada yang berhenti memberiku hadiah. Itu jelek, ya."
    elif _return == "B":
        nar "Kau membantu memisahkan beberapa kantong dan menyarankan tambahan yang sesuai dengan penerimanya. Koita menyambut bantuan itu dengan lega."
        koita "Yang ini dia suka. Aku ingat. Terus yang ini... iya, lebih cocok."
        nar "Hadiahnya kini tampak lebih pribadi. Pertanyaan tentang apa yang sebenarnya ia balas belum terjawab, hanya mendapatkan bungkus yang lebih meyakinkan."
        nar "Ketika ia berterima kasih, kau menyadari betapa mudah perhatian yang cermat dipakai untuk menunda kejujuran."
    else:
        nar "Kau membiarkannya membagikan seluruh kantong. Ucapan terima kasih tetap terdengar sopan, tetapi tidak semua penerima menunggu untuk berbicara lebih lama."
        koita "Mereka nggak suka biskuitnya, ya?"
        nar "Dari seberang ruangan terdengar kalimat pelan: oh, kamu juga dapat yang ini. Koita mendengarnya. Ia menunduk merapikan tas belanja yang sudah kosong."
    return

init 1 python:
    def kk_koita_fear(delta):
        pts.setdefault("ketakutan_koita",0)
        kk_adj("ketakutan_koita",delta)
    def kk_koita_suspect(delta):
        pts.setdefault("koita_curiga_1",0)
        kk_adj("koita_curiga_1",delta)

    _hook("K01-A", lambda: kk_flag("pola_koita_dikenal"))
    _hook("K01-B", lambda: kk_koita_suspect(5))
    _hook("K03-A", lambda: kk_koita_fear(5))
    _hook("K03-C", lambda: (kk_flag("koita_merasa_dilihat"), kk_koita_fear(3)))
    _hook("K06-A", lambda: kk_flag("foto_bukti_koita"))
    _hook("K09-A", lambda: kk_koita_fear(8))
    _hook("K09-B", lambda: kk_koita_fear(3))
    _hook("K10-A", lambda: kk_rel("koita","aff",2))
    _hook("K10-B", lambda: kk_flag("pola_koita_dikenal"))
    _hook("K11-A", lambda: kk_koita_suspect(8))
    _hook("K11-C", lambda: kk_koita_suspect(10))
