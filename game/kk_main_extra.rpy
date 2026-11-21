# Milestone utama tambahan di lokasi standar: Koita K07 (Matsuda sekutu/musuh)
# dan K08 (sabotase Natal, konsekuensi), Nagisa N11/N12/N13 (pra-gerbang; jeal,
# relasi Chiasa, konflik terbuka). Route-gate eksplisit (BL/Koita-Success/yandere
# N14+) dan event vila tidak disentuh. Cabang gelap = konsekuensi tanpa metode.
# Nilai prototipe; mengikuti Event_Koita / Event_Nagisa.

# ┌─ PANDUAN CERITA · K07 · Bazar Sastra
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : klub sastra; Matsuda memajang esai "Tokoh Utama yang Tidak Pernah Memilih".
# │ INTI    : A baca dan dukung Matsuda / B kritik esainya / C bela Koita.
# │ AKHIRAN : A menjadikan Matsuda sekutu; B musuh; C membuat Matsuda menjaga jarak.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K07:
    call kk_scene_enter("koita", "Gedung Sastra · Bazar Sastra")
    nar "Lembar esai Matsuda di bazar sastra habis lebih cepat daripada cerpennya. Judulnya membuat orang tersenyum, lalu menoleh ke arah Koita: Tokoh Utama yang Tidak Pernah Memilih."
    "Matsuda" "Aku membahas pola cerita. Kalau ada yang merasa dekat, mungkin pola itu memang terlalu sering dibiarkan."
    koita "Kalau begitu kenapa contoh dialognya terdengar seperti aku?"
    nar "Matsuda tidak segera menjawab. Di antara mereka berdiri orang-orang yang mulai menikmati ketegangan tanpa harus menanggungnya."
    call kk_family_menu("K07", ["Baca dan dukung Matsuda.", "Kritik esainya di depan umum.", "Bela Koita."])
    if _return == "A":
        nar "Kau membaca sampai selesai, lalu mengatakan bagian tentang perhatian tanpa komitmen memang perlu dibicarakan. Matsuda berhenti memasang senyum menantang."
        "Matsuda" "Aku nggak minta orang membenci tokohnya. Aku ingin orang berhenti menyebut semua yang menunggu itu tidak sabar."
        nar "Ia menandai satu paragraf untukmu. Kini kau punya seseorang yang bersedia membahas pola itu dengan kata-kata, bukan hanya saling bertukar pandang."
    elif _return == "B":
        nar "Kau mengkritik esai itu di depan pembacanya, mempertanyakan apakah Matsuda sedang menulis analisis atau menyindir seseorang yang tak diberi ruang menjawab."
        "Matsuda" "Kalau kamu ingin membantah argumennya, bantah. Jangan pura-pura membahas etika supaya kita nggak perlu membahas isinya."
        nar "Percakapan mengeras. Sesudahnya ia masih menjawab pertanyaan orang lain, tetapi menutup map ketika kau mendekat lagi."
    else:
        nar "Kau membela Koita dan mengatakan potongan perilaku tidak cukup untuk merangkum seseorang. Koita menoleh kepadamu dengan kelegaan yang nyaris kekanak-kanakan."
        koita "Makasih. Aku tadi nggak tahu harus bilang apa."
        "Matsuda" "Baik. Tapi orang yang terluka oleh perilaku itu juga lebih dari potongan cerita. Ingat mereka waktu membela."
        nar "Koita mengajakmu pergi ke stan lain sebelum kalimat tersebut mengundang pembicaraan lebih jauh."
    return

# ┌─ PANDUAN CERITA · K08 · Natal Plot Armor
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : kebetulan Natal mempertemukan Koita dengan heroine paling siap.
# │ INTI    : A intersep lewat telepon / B ambil alih kencan / C biarkan / D hadir sebagai pihak ketiga.
# │ AKHIRAN : hub besar #3; menentukan siapa memegang Natal Tahun 1.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K08:
    call kk_scene_enter("koita", "Gedung Sastra · Menjelang Natal")
    nar "Rangkaian lampu Natal di depan gedung menyala ketika Koita keluar dengan syal yang belum selesai dililitkan. Di ujung jalan, seseorang berhenti memeriksa waktu untuk melihat ke arah yang sama."
    koita "Aku belum punya rencana. Mungkin lihat-lihat di dekat stasiun dulu."
    nar "Ia mengatakan tidak punya rencana tepat ketika keadaan menyiapkan pertemuan yang hampir tak perlu direncanakan. Orang yang menunggu di bawah lampu sudah menyimpan keberanian untuk malam ini."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Intersep lewat telepon.", "Ambil alih kencan itu.", "Biarkan saja.", "Hadir sebagai pihak ketiga."])]
    call screen kk_choice_panel(_rows, "Natal tahun pertama")
    $ kk_record_choice("K08", _return)
    if _return == "A":
        nar "Teleponmu membuat Koita berhenti cukup lama hingga arah malam berubah. Ia menjawab sambil memandang lampu, tidak menyadari ada seseorang yang menunggu lalu menganggap dirinya telah salah berharap."
        koita "Iya, aku masih di kampus. Ada apa?"
        nar "Kelak ia akan mengingat panggilan ini sebagai percakapan biasa. Orang yang terlewat mungkin akan mengingat malam yang sama sebagai penolakan yang tak pernah benar-benar diucapkan."
    elif _return == "B":
        nar "Kau mengambil tempat di samping orang yang semula berharap bertemu Koita. Percakapan mengalir karena ia masih ingin malamnya berarti sesuatu, dan kau menawarkan kehadiran pada saat yang tepat."
        nar "Ketika Koita sampai di ujung jalan, kalian sudah bergerak menuju stasiun. Ia sempat mengangkat tangan, tetapi tak ada yang melihat sebelum arus orang menutup jalan."
        nar "Perhatian malam itu beralih kepadamu. Harapan yang mendahuluinya belum tentu ikut hilang."
    elif _return == "C":
        nar "Kau membiarkan mereka saling melihat. Koita terkejut dengan cara yang tampak menyenangkan bagi orang yang menunggunya."
        koita "Kamu juga belum pulang? Mau jalan sebentar?"
        nar "Ia mengangguk. Mereka pergi di bawah lampu-lampu, membawa peluang untuk mengatakan sesuatu yang selama ini ditahan. Kali ini kau tidak berdiri di antara peluang dan orang yang memilikinya."
    else:
        nar "Kau menyapa dan bergabung sebelum percakapan mereka menemukan iramanya. Koita segera membuat ruang untuk bertiga, kebiasaan yang menjadikannya ramah sekaligus sulit didekati secara utuh."
        koita "Pas sekali. Kita cari makan dulu?"
        nar "Orang yang menyiapkan keberanian tadi mengangguk setelah jeda. Malam tetap berjalan, tetapi ketika kesempatan bicara berdua muncul, selalu ada kalimat lain yang harus mengakomodasi kehadiranmu."
    return

# ┌─ PANDUAN CERITA · N11 · Ditinggal di Rumah
# │ LOKASI  : Hunian Biasa · Rumah Sakurajima
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : ia tidak ikut Kansai.
# │ INTI    : A kirim kabar / B abaikan / C cerita bohong.
# │ AKHIRAN : jeal naik.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N11:
    call kk_scene_enter("nagisa", "Rumah Sakurajima · Ditinggal")
    nar "Foto rombongan Kansai masuk ke grup ketika Nagisa sedang menunggu bahan maket mengering. Ia memperbesar gambar, menutupnya, lalu membuka lagi saat pesan berikutnya datang."
    nagisa "Ramai juga. Aku nggak ikut, jadi nggak tahu apa yang harus dikomentari. Kalau cuma tulis seru ya, terdengar kesal, nggak?"
    nar "Ia mengirimkan pertanyaan itu kepadamu secara pribadi, lalu buru-buru menambahkan bahwa ia punya banyak pekerjaan dan tidak sedang menunggu."
    call kk_family_menu("N11", ["Kirim kabar untuknya dari perjalanan.", "Abaikan saja.", "Karang cerita agar ia tak cemburu."])
    if _return == "A":
        nar "Kau mengirim kabar yang sungguh terjadi dan menanyakan pekerjaan studionya. Nagisa membalas dengan foto maket, lengkap dengan keluhan yang tidak sempat dimasukkan ke grup."
        nagisa "Terima kasih. Aku nggak minta diajak lewat layar terus. Cuma senang masih boleh punya cerita meski nggak ada di foto."
        nar "Setelah itu ia kembali bekerja. Kabar singkatmu memberinya tempat tanpa mengharuskan perjalananmu berhenti untuk menenangkan setiap takutnya."
    elif _return == "B":
        nar "Kau tidak membalas selama perjalanan. Di grup Nagisa tetap muncul sesekali dengan komentar singkat, semakin berhati-hati agar tidak terdengar menuntut perhatian."
        nar "Ketika pulang, kau bertanya bagaimana tugasnya. Ia mengatakan selesai dan tidak menunjukkan foto yang sudah disiapkannya. Ada bagian dari hari-harinya yang kini ia simpan karena mengira kau telah memilih tidak ingin tahu."
    else:
        nar "Kau mengarang cerita untuk membuat perjalanan itu terdengar kurang menyenangkan dan kurang dekat dengan siapa pun. Nagisa menghiburmu, mengatakan lain kali ia akan mengajakmu bermain supaya liburmu tidak sia-sia."
        nar "Kau menerima perhatian yang diberikan kepada versi palsu dari malammu. Foto dan cerita orang lain belum berhenti beredar; kelak ia mungkin mengingat betapa tulus ia mencoba menenangkan sesuatu yang tidak pernah terjadi."
    return

# ┌─ PANDUAN CERITA · N12 · Hujan Deras: Nagisa Menyelamatkan
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : ia menolong Chiasa/pemain lalu mengomel.
# │ INTI    : A berterima kasih / B menjauh / C peluk.
# │ AKHIRAN : hubungan dengan Chiasa.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N12:
    call kk_scene_enter("nagisa", "Gedung Arsitektur · Hujan deras")
    play sound "audio/sfx/rain.wav"
    nar "Nagisa muncul dengan payung tepat ketika kau bersiap menerobos hujan. Ia menarik ujung tasmu ke bawah atap, kemudian memberimu handuk kecil sambil mengomel tentang orang yang memperlakukan demam sebagai rencana akhir pekan."
    nagisa "Pakai. Bukan koleksi pameran, nggak perlu dilihat dulu. Rambutmu menetes ke mana-mana."
    nar "Satu bahunya sendiri basah karena payung tadi lebih banyak menutupimu. Ia tampak baru sadar ketika kau melihatnya."
    call kk_family_menu("N12", ["Berterima kasih dengan tulus.", "Menjauh dan merasa canggung.", "Peluk ia sebagai ucapan terima kasih."])
    if _return == "A":
        nar "Kau mengucapkan terima kasih tanpa mengejek caranya khawatir. Nagisa menarik sisi payung untuk menyembunyikan wajah."
        nagisa "Iya. Sama-sama. Lain kali bawa sendiri, tapi kalau lupa... jangan lari begitu saja. Cari aku dulu kalau ada."
        nar "Ia mengoreksi tawaran itu dengan cepat, mengatakan siapa saja yang punya payung juga boleh. Kau sudah mendengar nama yang pertama ia tawarkan."
    elif _return == "B":
        nar "Kau memberi jarak karena canggung. Nagisa berhenti merapikan ujung handuk dan menurunkan tangan."
        nagisa "Aku cuma nggak mau kamu sakit. Kalau terlalu dekat, bilang."
        nar "Ia memegang payung lebih lurus, menyisakan ruang di antara kalian. Perhatian yang tadi bergerak spontan kini harus mencari bentuk yang tidak membuatnya merasa telah ditolak sebagai orang."
    else:
        nar "Kau membuka tangan, menunggu reaksinya sebelum mendekat. Nagisa terpaku, lalu mengangguk kecil seolah takut gerakan besar akan terlihat semua orang."
        nagisa "Sebentar saja. Handuknya nanti jatuh."
        nar "Ia membalas pelukan dengan satu tangan yang bebas. Sesudah kalian menjauh, omelannya kembali, tetapi tidak lagi cukup lancar untuk menutupi senyum yang terus muncul."
    return

# ┌─ PANDUAN CERITA · N13 · Konfrontasi Yukata
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : ia menghadapi rival.
# │ INTI    : A mendukung / B melerai / C memihak Chiasa.
# │ AKHIRAN : konflik terbuka.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N13:
    call kk_scene_enter("nagisa", "Gedung Arsitektur · Konfrontasi Yukata")
    nar "Sebuah sindiran tentang siapa yang memakai yukata agar diperhatikan membuat Nagisa berhenti di depan stan. Orang yang mengucapkannya tersenyum, mencoba mempertahankan perlindungan bahwa itu hanya bercanda."
    nagisa "Kalau mau bilang sesuatu, bilang jelas. Jangan mengandalkan aku yang terlihat galak supaya kamu selalu bisa pura-pura nggak sengaja."
    nar "Ia benar-benar marah, sekaligus sadar orang-orang mulai menonton. Matanya menemukanmu di antara mereka."
    call kk_family_menu("N13", ["Dukung Nagisa terang-terangan.", "Lerai keduanya.", "Memihak dan bicara sebagai Chiasa."])
    if _return == "A":
        nar "Kau mendukungnya menolak sindiran tersebut, tidak ikut menertawakan atau memintanya menjadi pihak yang mengalah agar suasana enak. Nagisa menarik napas, terkejut karena tidak perlu membela dirinya sendirian."
        nagisa "Aku cuma mau dia berhenti. Bukan minta semua orang setuju aku menyenangkan."
        nar "Sesudah orang itu mundur, ia berterima kasih tanpa memalingkan wajah."
    elif _return == "B":
        nar "Kau melerai dan meminta keduanya memberi ruang. Nagisa memprotes karena mengira ia kembali dipaksa menanggung kesalahan agar keramaian segera tenang."
        nagisa "Aku mau pergi. Tapi jangan bilang kami sama-sama bercanda. Aku nggak bercanda waktu bilang tersinggung."
        nar "Ia bersedia menjauh setelah itu didengar. Kalian berjalan lebih pelan sampai tangannya berhenti gemetar."
    else:
        chiasa "Aku dengar yang kamu katakan. Menyebutnya bercanda nggak membuat Nagisa wajib tertawa."
        nar "Nagisa menatap Chiasa, lupa sesaat bahwa sepanjang sore mereka saling bersaing tentang banyak hal kecil. Orang yang menyindir kehilangan tempat bersembunyi di balik permusuhan mereka."
        nagisa "Kamu... iya. Terima kasih. Aku kira kamu bakal senang melihatku kesal."
        nar "Ketika kalian pergi, jarak di antara dua saingan lama itu tidak sekeras sebelumnya."
    return

init 1 python:
    _hook("K07-A", lambda: kk_flag("matsuda_sekutu"))
    _hook("K07-B", lambda: kk_flag("matsuda_lawan"))
    _hook("K07-C", lambda: kk_rel("koita","trust",4))
    _hook("K08-A", lambda: (kk_flag("koita_natal_diintersep"), kk_koita_suspect(5)))
    _hook("K08-B", lambda: (kk_flag("koita_natal_diambil"), kk_koita_suspect(8)))
    _hook("K08-D", lambda: kk_rel("koita","jeal",5))
    _hook("N11-A", lambda: (kk_rel("nagisa","trust",4), kk_adj("kelekatan_nagisa",5)))
    _hook("N11-B", lambda: kk_rel("nagisa","jeal",8))
    _hook("N11-C", lambda: (kk_rel("nagisa","jeal",5), kk_adj("luka_bohong",8)))
    _hook("N12-A", lambda: kk_rel("nagisa","aff",4))
    _hook("N12-B", lambda: kk_rel("nagisa","trust",-3))
    _hook("N12-C", lambda: (kk_rel("nagisa","intim",6), kk_adj("kelekatan_nagisa",6)))
    _hook("N13-A", lambda: (kk_rel("nagisa","aff",5), kk_adj("gengsi_nagisa",-5)))
    _hook("N13-B", lambda: kk_rel("nagisa","trust",3))
    _hook("N13-C", lambda: (kk_rel("nagisa","intim",4), kk_flag("nagisa_dibela_chiasa")))
