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
    nar "Nagisa memakai foto lama sebagai pembatas buku, tetapi halaman yang dibacanya tidak bergerak. Empat anak berdiri di dalam gambar. Di pangkuan Nagisa kecil ada kelinci yang telinganya terlalu panjang untuk ikut masuk bingkai."
    nagisa "Jangan lihat model rambutku. Haruto yang menyisir. Dia pikir asal dua sisinya sama, sudah bagus."
    nar "Ia hampir menyimpan foto, lalu membiarkanmu melihat ketika matamu berhenti pada bonekanya."
    call kk_family_menu("N05", ["Minta ia bercerita tentang Koko.", "Goda betapa lusuhnya boneka itu.", "Biarkan ia memandangi foto itu dalam diam."])
    if _return == "A":
        nagisa "Koko. Koita yang memenangkan di festival. Aku bilang cuma mau lihat stan, padahal berhenti di depan kelinci itu terus."
        nar "Ia mengusap permukaan foto dengan ibu jari."
        nagisa "Dia ingat. Itu yang membuatku senang. Bukan karena bonekanya mahal atau susah didapat."
        nar "Saat menyadari betapa lembut suaranya, ia buru-buru membahas harga permainan di festival. Kau sudah mendengar bagian yang ingin ia sembunyikan."
    elif _return == "B":
        nagisa "Namanya juga dipelihara lama. Yang baru belum tentu tahan mendengar keluhanku bertahun-tahun."
        nar "Ia menutup bagian foto yang memperlihatkan Koko, lalu tertawa ketika menyadari ia sedang melindungi gambar boneka."
        nagisa "Kalau kamu cerita ini ke orang, kubilang kamu yang masih bicara sama mainan."
    else:
        nar "Kau membiarkannya memandang foto. Nagisa berhenti menyiapkan alasan, menyusuri wajah keempat anak di dalamnya dengan mata."
        nagisa "Waktu itu rasanya besar nanti pasti tetap begini. Lucu, ya. Kita bahkan nggak tahu semua orang bisa tumbuh ke arah berbeda."
        nar "Ia menyimpan foto dengan hati-hati, tepat di halaman yang belum selesai dibaca."
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
    if kk_has("koko_dikenal"):
        nagisa "Kau masih ingat Koko? Malam Natal begini dia selalu kududukkan di kursi sebelah."
    else:
        nar "Di kursi sebelah Nagisa ada Koko, boneka kelinci yang salah satu jahitan telinganya lebih baru daripada tubuhnya."
    nar "Dua piring sudah disiapkan. Ketika kau melihatnya, Nagisa mengatakan satu untuk jaga-jaga, lalu tampak jengkel karena alasan itu terdengar kurang meyakinkan."
    nagisa "Jangan tersenyum begitu. Aku cuma nggak mau potong kue lagi nanti kalau ada yang datang."
    call kk_family_menu("N07", ["Tetap di sana merayakan bersamanya.", "Pamit lebih dulu karena ada urusan lain.", "Ajak Koita datang menemuinya juga."])
    if _return == "A":
        nar "Kau duduk dan meminta bagian kue yang tidak terlalu besar. Nagisa memotong dua bagian yang sama sekali tidak sama, kemudian mengambil yang lebih kecil sebelum kau protes."
        nagisa "Kamu tamu. Jangan debat soal ukuran kue juga."
        nar "Beberapa saat kemudian ia menambah bagiannya sendiri, santai karena tidak perlu lagi berpura-pura dua piring tadi kebetulan."
        nagisa "Terima kasih sudah tinggal. Itu saja. Jangan minta diulang."
    elif _return == "B":
        nar "Kau menjelaskan harus pergi. Nagisa tidak menahanmu, hanya menanyakan apakah kau ingin membawa sepotong kue."
        nagisa "Bukan bekal perpisahan dramatis. Kalau nggak dibawa, aku yang menghabiskan."
        nar "Di pintu ia mengucapkan selamat Natal lebih pelan. Saat kau menoleh terakhir kali, ia sedang memindahkan piring kedua dari meja, sementara Koko tetap di kursinya."
    else:
        nar "Kau mengLangsung telepon siapapun di kontakmu yang bisa membantu. Nagisa hendak melarang agar tidak kelihatan mengundang melalui orang lain, tetapi sudah terlambat menyamarkan kegembiraannya saat ia bersedia datang."
        nagisa "Kalau begitu piringnya kurang. Tunggu, aku ambil."
        nar "Ia menyiapkan tempat ketiga, lalu memeriksa rambut di pantulan jendela. Kehadiranmu tetap dihargai; hanya saja malam itu harapan lamanya kembali mendapat kursi paling dekat."
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
    nar "Kotak hadiah di meja Nagisa masih kosong. Di sampingnya ada coklat dengan bagian yang menghitam dan resep penuh tanda seru. Ia menutup hasil itu memakai tisu ketika kau datang, terlambat untuk menyembunyikan aromanya."
    nagisa "Iya, gosong. Untuk Koita. Nah, sekarang kamu sudah tahu dua hal yang nggak perlu diumumkan ke seluruh studio."
    nar "Ia mengambil kotak itu lagi, menimbang apakah harga dirinya lebih mudah diselamatkan dengan membeli coklat atau tidak memberi sama sekali."
    call kk_family_menu("N08", ["Makan saja yang gosong itu untuknya.", "Bantu ia membuat satu loyang lagi.", "Tawarkan agar coklatnya untukmu saja."])
    if _return == "A":
        nar "Kau mencoba bagian yang masih bisa dimakan, lalu mengaku pahit. Nagisa tertawa sebelum sempat merasa tersinggung."
        nagisa "Bagus. Kalau kamu bilang enak sekali, aku malah tahu kamu bohong."
        nar "Ia menyingkirkan bagian yang rusak dan mengizinkanmu mengambil sisanya. Kegagalan itu masih menyebalkan, tetapi tidak lagi sepenuhnya memalukan."
    elif _return == "B":
        nar "Kau menawarkan membantu mengulang. Nagisa memberikan tugas sederhana sambil mengingatkan tiga kali agar kau tidak menambahkan sesuatu tanpa bertanya."
        nagisa "Aku nggak mau yang ini gagal juga. Bukan karena... sudahlah, kamu tahu untuk siapa."
        nar "Kalian menyelesaikan satu porsi yang layak dibungkus. Ia mengucapkan terima kasih sambil tetap menatap kotak, bukan dirimu."
    else:
        nar "Kau menawarkan menjadi penerimanya. Nagisa mengangkat wajah, mencoba mencari apakah itu gurauan yang akan membuatnya semakin malu."
        nagisa "Kalau buatmu, aku ingin bikin yang benar. Bukan memberimu barang gagal yang awalnya untuk orang lain."
        nar "Ia mengambil kertas pembungkus lain. Perubahan kecil itu membuatnya mendadak canggung di dekatmu, tetapi ia tidak menarik kembali niatnya."
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
    nar "Nagisa menyadari tanggal hari ini sebelum kau menyebut White Day. Ia segera membicarakan tugas yang harus selesai, lalu dua kali berhenti untuk melihat tanganmu."
    nagisa "Kalau kamu mau memberi sesuatu, nggak usah merasa wajib. Aku nggak menghitung pemberian sebagai tagihan."
    nar "Kalimatnya masuk akal. Wajah yang menunggu jawaban jauh lebih sulit ia kendalikan."
    call kk_family_menu("N09", ["Beri hadiah kecil yang sederhana.", "Beri hadiah mahal yang mencolok.", "Tidak memberi apa-apa."])
    if _return == "A":
        nar "Kau menyerahkan hadiah kecil yang bisa dipakai atau disimpannya tanpa membuat seluruh studio menoleh. Nagisa membuka perlahan, lalu menahannya dekat tas."
        nagisa "Kamu ingat aku suka yang begini. Oke. Selera kamu ternyata nggak buruk."
        nar "Ia masih menyebutnya kecil, tetapi sepanjang sisa percakapan beberapa kali memeriksa apakah hadiah itu sudah tersimpan aman."
    elif _return == "B":
        nar "Bungkus yang mencolok membuat orang di meja sebelah berkomentar sebelum Nagisa sempat membuka. Bahunya menegang."
        nagisa "Ini terlalu mahal. Kalau aku terima, orang akan bilang apa? Kalau kutolak, kamu malu. Kamu mikir sampai situ?"
        nar "Ia menurunkan suara agar tidak mempermalukanmu lebih jauh. Hadiah itu memberinya perhatian yang tidak ia pilih, dan kini ia juga harus mengurus perasaan orang yang memberikannya."
    else:
        nar "Tidak ada hadiah yang kaukeluarkan. Nagisa mengangguk, seolah tadi hanya memastikan kau tidak perlu repot."
        nagisa "Bagus. Aku juga nggak menunggu."
        nar "Ia kembali ke maket dan meminta penggaris yang sebenarnya sudah ada di dekat tangannya. Kau menyerahkan penggaris itu; ia baru menyadari setelah menerimanya."
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
