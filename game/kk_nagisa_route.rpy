# Gerbang Rute Yandere Nagisa (N14-N18): posesif -> ultimatum -> bentrok ->
# tuduhan -> sabotase. Ditulis sebagai KARAKTER dan KONSEKUENSI. Tindakan ekstrem
# (jebakan, sabotase, memfitnah) hanya AKIBATNYA yang dicatat singkat; metode,
# rekayasa jebakan, dan cara memfitnah korban TIDAK ditulis. Efek menggerakkan
# stage[nagisa], kelekatan_nagisa, jeal/fear. Nilai prototipe; Event_Nagisa.

init 1 python:
    def kk_nagisa_stage(n):
        kk_stage("nagisa", max(n, stage.get("nagisa", 0)))

# ┌─ PANDUAN CERITA · N14 · Cek Pesan
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : ia meminta melihat ponsel pemain.
# │ INTI    : A tunjukkan / B tolak / C tipu.
# │ AKHIRAN : gerbang Rute Yandere (stage 3, posesif).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N14:
    call kk_scene_enter("nagisa", "Gedung Arsitektur · Cek pesan")
    nar "Nagisa berhenti menggambar setiap ponselmu berbunyi. Pada bunyi ketiga, ia meletakkan pensil dengan hati-hati dan menanyakan siapa yang menghubungi."
    nagisa "Boleh lihat? Sebentar. Aku capek menebak dari caramu tersenyum."
    nar "Kau belum menjawab ketika ia menambahkan alasan yang membuat penolakan terdengar seperti pengakuan."
    nagisa "Kalau nggak ada yang disembunyikan, harusnya nggak masalah, kan?"
    call kk_family_menu("N14", ["Tunjukkan ponselmu.", "Tolak; itu privasimu.", "Tipu ia dengan ponsel yang sudah disiapkan."])
    if _return == "A":
        nar "Kau menyerahkan ponsel. Nagisa memeriksa lebih lama daripada sebentar yang diminta, kemudian mengembalikannya dengan senyum lega."
        nagisa "Maaf. Aku cuma takut. Sekarang lebih tenang."
        nar "Ia kembali menggambar. Kepercayaan yang didapat melalui pemeriksaan itu tampak hangat malam ini, tetapi belum menjawab apa yang akan terjadi ketika kecemasannya datang lagi tanpa layar yang boleh dibuka."
    elif _return == "B":
        nar "Kau menolak dan menjelaskan bahwa privasi tidak sama dengan menyembunyikan pengkhianatan. Nagisa memerah sebelum sempat mendengar seluruh kalimat."
        nagisa "Aku cuma minta lihat. Kenapa jadi sebesar ini?"
        nar "Ia menarik tas mendekat, bersiap pergi, lalu tak bergerak. Di hadapan batas yang tidak langsung kaulunakkan, ketakutannya kehilangan cara paling mudah untuk diredakan."
    else:
        nar "Kau memberinya tampilan yang sengaja tidak memperlihatkan seluruh kebenaran. Nagisa memeriksa dan akhirnya tersenyum, merasa ketakutannya telah dijawab."
        nagisa "Harusnya aku percaya dari awal. Maaf."
        nar "Permintaan maaf itu memudahkanmu menyimpan sisi lain hidupmu. Jika kebohongan tersebut terbuka, ia juga akan mengingat bahwa rasa aman yang pernah diterimanya disusun oleh orang yang sedang menipunya."
    return

# ┌─ PANDUAN CERITA · N15 · Natal Kedua: Ultimatum
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : "pilih aku atau mereka."
# │ INTI    : A pilih / B tolak / C manipulasi.
# │ AKHIRAN : stage 4 (titik balik).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N15:
    call kk_scene_enter("nagisa", "Gedung Arsitektur · Natal kedua")
    nar "Nagisa menghapus pesan yang baru diketikkannya dan memilih mengatakannya langsung. Di luar studio orang-orang saling mengucapkan selamat Natal; di dalam, suaranya terlalu tenang untuk kalimat yang disiapkan sepanjang hari."
    nagisa "Aku, atau mereka. Jangan jawab semuanya penting. Aku tahu mereka penting. Aku ingin tahu siapa yang akan kamu tinggalkan kalau harus memilih."
    nar "Ia tidak lagi meminta malam bersama. Ia sedang meminta seluruh hubunganmu menjadi jaminan bahwa dirinya tak akan ditinggalkan."
    call kk_family_menu("N15", ["Pilih Nagisa.", "Tolak ultimatum itu.", "Manipulasi agar ia merasa menang tanpa kau memilih."])
    if _return == "A":
        nar "Kau memilihnya. Nagisa mendekat, lega begitu cepat sampai air matanya baru keluar sesudah ia tersenyum."
        nagisa "Sekarang aku nggak perlu takut lagi, kan?"
        nar "Ia menanyakan hal itu dua kali. Jawabanmu telah memberinya kepastian tentang malam ini, tetapi kecemasannya segera mulai mencari bukti bahwa pilihan itu akan berlaku setiap kali orang lain muncul."
    elif _return == "B":
        nar "Kau menolak syarat tersebut. Nagisa menatapmu seolah penolakan terhadap ultimatum hanya mungkin berarti penolakan terhadap dirinya."
        nagisa "Jadi aku masih yang harus mengerti. Selalu begitu."
        nar "Tangannya gemetar saat menutup tas. Ia pergi tanpa meminta ditemani. Kau tidak tahu siapa yang akan dihubunginya atau apakah ia akan membiarkan seseorang mendengar sebelum takut berubah menjadi tindakan."
    else:
        nar "Kau memberinya kesan menang tanpa mengambil keputusan yang ia minta. Nagisa memegang bagian perkataanmu yang terdengar paling pasti, menyingkirkan sisanya agar bisa bernapas lega."
        nagisa "Aku ingat yang kamu bilang. Jangan nanti bilang aku salah paham."
        nar "Ia pulang membawa sebuah janji yang tidak ingin kautanggung. Kedamaian malam itu dibeli dengan kemungkinan luka yang lebih besar ketika arti kata-kata kalian akhirnya bertemu."
    return

# ┌─ PANDUAN CERITA · N16 · Hari Bentrok
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : ia menyatakan perasaan pada pemain atau Koita.
# │ INTI    : A terima / B tolak / C alihkan.
# │ AKHIRAN : hub besar #8.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N16:
    call kk_scene_enter("nagisa", "Gedung Arsitektur · Hari bentrok")
    nar "Nagisa menghampirimu di luar studio dengan kalimat yang tampaknya sudah diulang berkali-kali sendirian. Ketika mulai bicara, ia justru membuang kalimat pembukanya."
    nagisa "Aku menyukaimu. Aku nggak mau menyebutnya cuma khawatir atau kebiasaan lagi. Dan aku nggak mau kalah karena orang lain berani bicara lebih dulu."
    nar "Ia menyadari kata kalah setelah mengucapkannya, tetapi terlalu takut untuk memperbaiki."
    nagisa "Jangan jawab karena kasihan. Tapi jangan bercanda juga. Tolong."
    call kk_family_menu("N16", ["Terima perasaannya.", "Tolak dengan jujur.", "Alihkan jawabannya."])
    if _return == "A":
        nar "Kau menerima perasaannya. Nagisa menutup mata sebentar, seperti baru selesai menahan napas yang sudah dimulai bertahun-tahun lalu."
        nagisa "Aku senang. Aku juga takut kamu berubah pikiran setelah melihat aku yang sebenarnya."
        nar "Ia meraih tanganmu terlalu erat, kemudian mengendurkan ketika kau bergerak. Menerima cinta ini membuka kedekatan; cara kalian memperlakukan ketakutannya akan menentukan apa yang tumbuh di dalamnya."
    elif _return == "B":
        nar "Kau menolak dengan jelas. Nagisa mengangguk berkali-kali, tersenyum dengan wajah yang semakin pucat."
        nagisa "Aku minta jujur, kan. Kamu sudah jujur. Bagus."
        nar "Ia melangkah pergi sebelum senyum itu jatuh. Penolakanmu bukan kesalahan, tetapi ketenangan yang ia pakai untuk membungkusnya tidak tampak seperti sesuatu yang dapat bertahan sendirian."
    else:
        nar "Kau mengalihkan jawaban ke waktu yang buruk dan keadaan yang rumit. Nagisa memegang kata nanti sebelum kau benar-benar menjanjikannya."
        nagisa "Aku bisa menunggu. Aku sudah pandai soal itu."
        nar "Ia mengucapkannya sebagai bukti kesungguhan. Kau mendengar betapa mudah satu penghindaran baru bisa ditumpuk di atas penantian lama yang belum pernah ia akui menyakitkan."
    return

# ┌─ PANDUAN CERITA · N17 · Gantungan Kunci yang Hilang
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : ia menuduh orang lain.
# │ INTI    : A selidiki / B pasang jebakan / C tuduh balik.
# │ AKHIRAN : titik pemulihan terakhir; setelah ini hanya Distorted Ending.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N17:
    call kk_scene_enter("nagisa", "Gedung Arsitektur · Gantungan kunci hilang")
    nar "Nagisa mengeluarkan isi tas di atas meja. Tempat gantungan kunci itu biasa terpasang kosong; yang tidak kosong adalah daftar orang yang sudah ia salahkan dalam kepalanya."
    nagisa "Orang itu terakhir berdiri dekat tasmu. Terus barang dariku hilang. Kamu masih mau bilang nggak ada hubungannya?"
    nar "Ia punya urutan kejadian, tetapi belum punya alasan untuk menganggap urutan itu bukti. Ketakutannya sudah melompati jarak tersebut."
    call kk_family_menu("N17", ["Selidiki dengan tenang sebelum menuduh.", "Biarkan ia memasang jebakan untuk orang itu.", "Tuduh balik agar ia ragu."])
    if _return == "A":
        nar "Kau mengajaknya mencari tanpa menghubungi orang yang dituduh terlebih dahulu. Nagisa protes, lalu mengikuti ketika kau menolak menjadikan keberpihakan sebagai syarat mencari kebenaran."
        nar "Gantungan itu akhirnya ditemukan di antara barang yang dipindahkan sebelumnya. Tak ada pencuri, hanya kesimpulan yang telanjur diinginkan."
        nagisa "Aku sudah hampir... aku tahu. Jangan selesaikan kalimatnya untukku. Aku harus memikirkan apa yang tadi ingin kulakukan."
        nar "Ia duduk lama. Kali ini rasa malu tidak boleh diselesaikan dengan mencari orang baru untuk disalahkan."
    elif _return == "B":
        nar "Kau membiarkan tuduhannya menjadi tindakan. Sesudahnya seseorang yang tidak bersalah dipanggil untuk menjelaskan hal yang tidak pernah diperbuat, sementara teman-temannya mulai menjaga jarak."
        nagisa "Sekarang kamu tahu aku nggak cuma diam kalau ada yang mengganggu kita."
        nar "Ia menunggu persetujuanmu. Orang yang terseret kehilangan rasa aman di studio; Nagisa justru mulai mempercayai bahwa menyingkirkan orang lain adalah cara paling jelas membuktikan cinta."
    else:
        nar "Kau menuduhnya sengaja membuat persoalan. Nagisa berdiri begitu cepat kursinya bergeser keras."
        nagisa "Jadi sekarang aku yang harus dibuktikan salah? Kamu bahkan belum dengar semuanya!"
        nar "Ia membela dirinya, bukan memeriksa tuduhannya. Percakapan yang bisa saja menahannya justru berubah menjadi bukti lain bahwa orang lain selalu lebih mudah dipercaya daripada dirinya."
    return

# ┌─ PANDUAN CERITA · N18 · Yuuto dan Sabotase
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : Nagisa mengganggu pesaing.
# │ INTI    : A hentikan / B biarkan / C menjadi korban.
# │ AKHIRAN : stage 5.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N18:
    call kk_scene_enter("nagisa", "Gedung Arsitektur · Sabotase")
    nar "Yuuto berhenti duduk di meja yang sama. Saat ditanya, ia menyebut ingin menghindari masalah, menatap Nagisa sebentar, lalu membawa pekerjaannya pergi."
    nagisa "Bagus kalau dia paham sendiri. Aku sudah capek melihatnya cari alasan dekat denganmu."
    nar "Ia mengatakannya hampir lega. Yang paling mengusik adalah betapa ia mengira kau akan merasakan kelegaan yang sama."
    call kk_family_menu("N18", ["Hentikan ia sebelum keterlaluan.", "Biarkan ia berjalan terus.", "Jadikan dirimu seolah korban untuk mengikatnya lebih dalam."])
    if _return == "A":
        nar "Kau menghentikannya dan menyebut dampaknya kepada Yuuto tanpa memperdebatkan siapa yang lebih penting bagimu. Nagisa mencoba mengalihkan, lalu kehilangan kata-kata ketika kau tetap pada pokok itu."
        nagisa "Aku cuma takut kalau dia ada, kamu nggak memilih duduk denganku lagi."
        nar "Kau mendengar ketakutannya tanpa menerima perbuatannya. Untuk pertama kalinya malam itu, ia harus memikirkan apa yang telah dilakukan kepada seseorang yang tidak sedang bertanggung jawab atas rasa takutnya."
    elif _return == "B":
        nar "Kau tidak menghentikan. Gangguan itu berlanjut sampai kesempatan dan pekerjaan Yuuto ikut rusak. Ia mulai menghindari studio yang seharusnya menjadi tempat belajarnya."
        nagisa "Akhirnya lebih tenang. Kita bisa kerja tanpa diganggu."
        nar "Ia menyiapkan kursi untukmu dengan hangat. Keamanan yang ditawarkannya dibangun dari ketidakamanan orang lain, dan diammu telah diterima sebagai persetujuan."
    else:
        nar "Kau menempatkan dirimu sebagai orang yang harus ia bela, membiarkan luka yang kautampilkan mengarahkan amarahnya lebih jauh. Nagisa segera berpindah dari mencari kepastian ke menjanjikan perlindungan."
        nagisa "Aku nggak akan membiarkan siapa pun memperlakukanmu begitu. Kamu cukup percaya aku."
        nar "Ia tidak memeriksa bagian ceritamu yang kabur. Kau memperoleh kesetiaan yang makin keras, sementara orang di luar kalian berdua menjadi sasaran dari rasa takut yang sengaja kaupelihara."
    return

init 1 python:
    _hook("N14-A", lambda: (kk_rel("nagisa","trust",4), kk_nagisa_stage(3)))
    _hook("N14-B", lambda: (kk_rel("nagisa","jeal",10), kk_nagisa_stage(3)))
    _hook("N14-C", lambda: (kk_adj("luka_bohong",10), kk_nagisa_stage(3), kk_flag("rute_yandere_nagisa")))
    _hook("N15-A", lambda: (kk_adj("kelekatan_nagisa",15), kk_nagisa_stage(4), kk_flag("nagisa_dipilih")))
    _hook("N15-B", lambda: (kk_rel("nagisa","fear",8), kk_nagisa_stage(4)))
    _hook("N15-C", lambda: (kk_adj("luka_bohong",12), kk_nagisa_stage(4)))
    _hook("N16-A", lambda: (kk_rel("nagisa","intim",8), kk_flag("nagisa_diterima")))
    _hook("N16-B", lambda: (kk_rel("nagisa","jeal",12), kk_flag("nagisa_ditolak_keras")))
    _hook("N16-C", lambda: kk_rel("nagisa","jeal",6))
    _hook("N17-A", lambda: (kk_rel("nagisa","trust",5), kk_flag("nagisa_pemulihan_terakhir")))
    _hook("N17-B", lambda: (kk_nagisa_stage(5), kk_flag("nagisa_jebakan_dipasang")))
    _hook("N17-C", lambda: kk_rel("nagisa","jeal",8))
    _hook("N18-A", lambda: (kk_rel("nagisa","trust",4), kk_flag("nagisa_dihentikan")))
    _hook("N18-B", lambda: (kk_nagisa_stage(5), kk_flag("yuuto_disabotase")))
    _hook("N18-C", lambda: (kk_adj("kelekatan_nagisa",20), kk_nagisa_stage(5), kk_flag("nagisa_distorted")))
