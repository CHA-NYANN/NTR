# Event dinamis Chiasa host (C-D01/04/05/06/08/09/10/11/12/13/14/15).
# Termasuk konflik batin Chiasa soal framing Koita (C-D13/14/15) — ditulis sebagai
# KONSEKUENSI + KARAKTER: beban nurani, nyaris mengaku; tanpa metode memfitnah.

init 1 python:
    def kk_chiasa_conscience(delta):
        pts.setdefault("nurani_chiasa", 0)
        kk_adj("nurani_chiasa", delta)

# ┌─ PANDUAN CERITA · C-D01 · Dapur Jam Dua
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Chiasa
# │ AWALAN  : Chiasa host; Koita menulis sampai larut
# │ INTI    : A buatkan teh untuk Koita / B goda / C bicara serius / D kembali ke kamar
# │ AKHIRAN : benih Koita Success atau ikatan saudara
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C_D01:
    call kk_scene_enter("chiasa", "Dapur · Jam dua pagi")
    nar "Dalam tubuh Chiasa, kau sudah mulai mengenali bunyi rumah malam hari: ketel yang bergetar sebelum mendidih, papan lantai dekat kulkas, dan pena Koita yang berhenti saat ia menyadari kau belum tidur."
    koita "Mau minum? Aku tadi hendak buat sendiri, tapi kalau kamu juga bangun... kita bisa duduk sebentar."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", KK_DYN_BY_ID["C-D01"]["choices"])]
    call screen kk_choice_panel(_rows, "Dapur jam dua")
    $ kk_record_choice("C-D01", _return)
    if _return == "A":
        nar "Kau membuat teh dan menanyakan apakah ia ingin ditemani. Koita menggeser naskah agar meja punya ruang untuk dua cangkir."
        koita "Makasih. Aku hampir menganggap kamu pasti akan membuatkan seperti biasa. Aku perlu berhenti menganggap begitu, ya."
    elif _return == "B":
        chiasa "Ko-nii, kalau menunggu ditemani, bilang. Jangan memakai teh sebagai surat undangan rahasia."
        koita "Kamu yang belum tidur juga. Baik, iya. Aku ingin ditemani. Ternyata mengatakannya lebih memalukan daripada membuat minuman."
        nar "Tawanya memberi keakraban lama tempat baru, meski kau masih sedang belajar bagian mana yang benar-benar menjadi keinginanmu."
    elif _return == "C":
        nar "Kau menanyakan apa yang membuatnya terus menulis sampai larut. Koita semula menjawab soal tenggat, lalu mengaku takut jika berhenti ia harus memikirkan hubungan yang tak pernah selesai dibahas."
        koita "Aku nggak minta kamu menyelesaikan. Aku ingin belajar bilang kalau kepalaku ramai tanpa langsung menyuruhmu membereskannya."
    else:
        nar "Kau kembali ke kamar. Di belakangmu, suara pena Koita dan gelembung air tetap berlomba dalam sunyi."
    return

# ┌─ PANDUAN CERITA · C-D04 · Hari Pertama
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Chiasa
# │ AWALAN  : Chiasa host; siklus jatuh di hari penting
# │ INTI    : A tetap hadir / B izin / C minta bantuan Haruka atau Yoshie lewat video call
# │ AKHIRAN : hasil event hari itu bergeser; Yoshie menjadi lebih dekat
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C_D04:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Hari yang berat")
    nar "Hari pertama menstruasi datang bersamaan dengan kegiatan penting. Kau mengenali tubuh ini melalui rasa nyeri yang tidak dapat diselesaikan dengan pengetahuan tentang cerita. Kalender tetap menunjukkan janji, sementara duduk sebentar saja terasa perlu."
    nar "Kau menimbang hadir, meminta izin, atau menghubungi orang yang dapat membantu menyesuaikan hari. Kesulitan ini nyata meski sebelumnya hanya dianggap bagian kecil kehidupan Chiasa."
    call kk_family_menu("C-D04", ["Dukung ia tetap hadir.", "Sarankan ia izin.", "Minta bantuan Haruka atau Yoshie lewat video call."])
    if _return == "A":
        nar "Kau memilih hadir dengan menyesuaikan hal yang dapat dikurangi. Keputusan itu perlu diperiksa lagi jika keadaan memburuk; bertahan bukan janji untuk mengabaikan tubuh sampai kegiatan selesai."
        nar "Di perjalanan kau mulai memahami mengapa terlihat seperti biasa tidak mengatakan banyak tentang seberapa sulit seseorang menjalani hari."
    elif _return == "B":
        nar "Kau mengabari pihak yang menunggu dan meminta izin. Jari berhenti sebentar sebelum mengirim, takut dianggap memakai alasan yang tak cukup besar."
        nar "Sesudah pesan terkirim, kau membiarkan tubuh beristirahat. Ada konsekuensi jadwal yang perlu diurus nanti, tanpa harus membuat rasa sakit menjadi ujian apakah dirimu pantas dipercaya."
    else:
        nar "Kau menghubungi Yoshie, ibu tiri yang mengenal kebiasaan rumah ini, dan menanyakan hal yang membuatmu kesulitan. Ia mendengar tanpa menertawakan pertanyaan yang mungkin terdengar baru bagi Chiasa."
        "Yoshie" "Kamu boleh minta bantuan. Kabari Haruka juga kalau jadwalmu perlu diubah. Tidak semua hal harus ditangani dengan diam agar tampak kuat."
    return

# ┌─ PANDUAN CERITA · C-D05 · Video Call dari Luar Negeri
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Chiasa
# │ AWALAN  : kedua route
# │ INTI    : (node keputusan / penutup — tak ada menu)
# │ AKHIRAN : curiga identitas (C) atau tanggung jawab baru (Y)
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C_D05:
    call kk_scene_enter("chiasa", "Panggilan dari luar negeri · 03:00")
    nar "Panggilan Daisuke masuk ketika rumah hampir seluruhnya gelap. Ia meminta maaf salah memperkirakan jam, lalu tetap di layar karena sudah telanjur melihat wajah yang ingin dipastikan kabarnya."
    "Daisuke" "Aku lihat foto kalian. Ada yang berbeda. Bukan soal potongan rambut. Cara melihat kamera, mungkin. Kamu sedang baik-baik saja?"
    nar "Pertanyaan itu dapat dijawab dengan senyum yang cukup mirip orang lama. Tetapi perhatian seorang ayah tidak berhenti setelah satu jawaban yang terdengar benar."
    "Daisuke" "Kalau ada yang berubah, aku ingin tahu sebelum kita sama-sama terlalu sibuk mencari alasan untuk tidak bicara. Aku jauh, bukan berarti kalian harus menunggu sampai aku pulang untuk minta didengar."
    nar "Di belakangnya terdengar Yoshie menanyakan apakah semua sehat. Rumah yang jauh tetap dapat menjangkau melalui pertanyaan sederhana, dan justru itu yang membuat penyamaran terasa lebih berat daripada menghadapi ancaman Sistem."
    $ kk_record_choice("C-D05", "A")
    return

# ┌─ PANDUAN CERITA · C-D06 · Pagar di Antara Dua Rumah
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Chiasa
# │ AWALAN  : kedua route; Nagisa dan Chiasa sama-sama di rumah
# │ INTI    : A Lerai / B ikut / C tonton
# │ AKHIRAN : rivalitas atau damai; Koita Success bisa ketahuan
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C_D06:
    call kk_scene_enter("chiasa", "Pagar antara dua rumah")
    nar "Pagar di antara rumah menjadi tempat percakapan yang terlalu lama dipendam. Nagisa dan Chiasa mengulang soal siapa lebih memahami Koita, masing-masing memakai kenangan sebagai bukti bahwa yang lain tak berhak bicara."
    nagisa "Jangan sok akrab dengan dia hanya karena kalian serumah!"
    chiasa "Dan kau pikir cemburu itu membuatmu lebih berhak?"
    call kk_family_menu("C-D06", ["Lerai keduanya.", "Ikut berpihak.", "Tonton dari jauh."])
    if _return == "A":
        nar "Kau menghentikan pertukaran sindiran dan meminta persoalan dibicarakan tanpa menjadikan satu rumah atau masa kecil sebagai hak atas seseorang. Nagisa terdiam, Chiasa menarik napas, dan untuk sementara tidak ada yang melanjutkan kalimat paling tajam yang telah disiapkan."
    elif _return == "B":
        nar "Kau memperkuat satu sisi. Pertengkaran segera mempunyai pemenang yang harus dipertahankan dan pihak yang makin sulit meminta berhenti tanpa merasa kalah. Kenangan bersama berubah menjadi senjata untuk membuat orang yang dahulu akrab terasa seperti tamu yang tak diundang."
    else:
        nar "Kau membiarkan percakapan itu berlangsung. Ketika akhirnya berhenti, tak seorang pun tampak puas; keduanya hanya kehabisan cara bertengkar tanpa terlihat terlalu terluka. Pagar tetap di tempatnya, kini diberi arti lebih berat daripada batas dua halaman."
    return

# ┌─ PANDUAN CERITA · C-D08 · Kopi dari Yutaka
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Chiasa
# │ AWALAN  : Chiasa host; Yutaka NPC mengabari dulu
# │ INTI    : A Undang masuk / B mengobrol di teras / C tolak
# │ AKHIRAN : yutaka_harap ±; Koita melihat dari jendela
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C_D08:
    call kk_scene_enter("chiasa", "Teras · Kopi dari Yutaka")
    nar "Yutaka, yang sudah mengabari lebih dulu, mampir membawa dua gelas kopi malam."
    yutaka "Tadi kamu bilang masih bangun, jadi aku bawa kopi. Kalau ternyata sudah ingin istirahat, bilang. Aku belum mau menganggap satu pesan sebagai izin menghabiskan malammu."
    call kk_family_menu("C-D08", ["Undang ia masuk.", "Mengobrol di teras saja.", "Tolak dengan sopan."])
    if _return == "A":
        nar "Kau mengundangnya masuk. Dari jendela lantai atas, Koita memperhatikan lampu teras yang menyala lama."
        nar "Yutaka mengikuti setelah menunggu kau membuka pintu. Ia menanyakan karya yang dikerjakan, memberi perhatian pada hal yang sedang kaupilih sekarang, bukan hanya cerita tentang Chiasa kecil yang tak kaubawa sebagai ingatan."
    elif _return == "B":
        yutaka "Teras saja cukup. Aku senang bisa bicara. Kalau kopinya terlalu manis, jangan diminum cuma karena kubawa."
        nar "Kalian duduk dengan jarak yang masih bisa dipilih. Sesekali Koita terlihat di jendela, tetapi kali ini percakapan tidak harus diubah untuk mengurus perasaannya dari jauh."
    else:
        yutaka "Baik. Lain kali. Kopinya mau kutinggal atau kubawa lagi?"
        nar "Ia menunggu jawaban sebelum pergi, menerima penolakan kunjungan tanpa membuat pemberiannya menjadi alasan kau harus menerima kedatangan."
    return

# ┌─ PANDUAN CERITA · C-D09 · Tangis di Ruang Tamu
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Chiasa
# │ AWALAN  : Male Route; Koita baru menggantung Chiasa
# │ INTI    : A Hibur / B panggil Koita / C pergi / D manfaatkan
# │ AKHIRAN : nyaman_yutaka ±; memanfaatkan membuka E-CH-11
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C_D09:
    call kk_scene_enter("chiasa", "Ruang tamu · Tangis")
    nar "Chiasa menghapus air mata begitu mendengar langkah Yutaka. Di meja masih ada makanan untuk rencana yang Koita tunda dengan alasan yang tampak cukup baik sampai diletakkan di sebelah penundaan lain."
    chiasa "Jangan bilang dia pasti punya alasan. Aku sudah menyusun semua alasannya sendiri. Aku ingin kecewa tanpa harus membelanya dulu."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", KK_DYN_BY_ID["C-D09"]["choices"])]
    call screen kk_choice_panel(_rows, "Tangis di ruang tamu")
    $ kk_record_choice("C-D09", _return)
    if _return == "A":
        chiasa "Kau menghiburku? ...Terima kasih. Aku tidak tahu harus bersandar pada siapa lagi malam ini."
        nar "Kau mendengar tanpa menawarkan diri sebagai pengganti yang harus langsung dipilih. Chiasa meminta tisu, lalu mulai bercerita dengan marah yang tidak seluruhnya perlu dirapikan agar tetap pantas didengar."
    elif _return == "B":
        nar "Kau menghubungi Koita dan meminta ia menjawab langsung. Chiasa sempat menahan tanganmu, takut terlihat menuntut, lalu mengakui ada hal yang memang perlu dikatakan kepadanya sendiri."
        nar "Kehadiran Koita belum menjamin percakapan aman atau selesai. Yang tak boleh dilakukan lagi adalah memakai Yutaka untuk terus menjelaskan maksud dua orang yang tidak mau saling bertanya."
    elif _return == "C":
        nar "Kau pamit. Chiasa mengangguk dan segera merapikan makanan agar punya pekerjaan yang tidak membuatnya terus melihat pintu. Ia tidak mengejarmu, tetapi sesudah itu lebih cepat mengatakan tidak apa-apa setiap hampir menangis di depanmu."
    else:
        nar "Kau memakai tangisnya untuk mendekat dengan maksud yang tidak mempertimbangkan keinginannya sendiri. Chiasa hampir menerima apa pun yang membuat malam ini terasa seperti ia masih dipilih seseorang."
        chiasa "Kamu melihatku, atau cuma senang dia gagal membuatku senang?"
        nar "Pertanyaan itu belum tentu ia pertahankan, tetapi cukup jelas untuk membuatmu tahu ada orang di dalam kesedihan yang sedang kauperlakukan sebagai peluang."
    return

# ┌─ PANDUAN CERITA · C-D10 · Bandara Jam Lima
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Chiasa
# │ AWALAN  : kedua route; orang tua pulang mendadak
# │ INTI    : A Jemput / B tidak
# │ AKHIRAN : Koita Success yang sedang berjalan bisa ketahuan di dalam mobil
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C_D10:
    call kk_scene_enter("chiasa", "Telepon · Bandara jam lima")
    nar "Daisuke menelepon setelah mendarat, meminta maaf karena baru mendapat kesempatan memberi kabar. Yoshie mengambil alih sebentar untuk menanyakan apakah kalian bisa menjemput atau perlu membiarkan mereka mencari kendaraan sendiri."
    nar "Kepulangan mendadak berarti tak ada waktu menata seluruh rumah dan jawaban agar sesuai dengan versi keluarga yang selama ini mereka bayangkan dari jauh."
    call kk_family_menu("C-D10", ["Jemput mereka.", "Tidak menjemput.", "Suruh orang lain menjemput."])
    if _return == "A":
        nar "Kau berangkat menjemput. Di dalam mobil yang sempit, apa pun yang sedang berjalan diam-diam berisiko terlihat."
        nar "Pertanyaan ringan tentang tidur, makan, dan siapa duduk di depan membawa tanda-tanda kedekatan yang sulit disembunyikan. Kalian tetap harus menjawab sebagai orang yang pulang ke rumah yang sama."
    elif _return == "B":
        nar "Kau tidak menjemput. Orang tua tiba sendiri, membawa pertanyaan yang belum sempat kausiapkan jawabannya."
        "Yoshie" "Tidak apa-apa kalau tidak bisa. Tapi lain kali kabari jelas, ya. Kami tidak ingin mengira kalian aman hanya karena tak ada yang bilang ada masalah."
    else:
        nar "Kau meminta orang lain menjemput dan memastikan persetujuannya. Perjalanan itu memberimu sedikit waktu, belum memberikan jawaban untuk orang-orang yang tetap akan masuk melalui pintu keluarga."
    return

# ┌─ PANDUAN CERITA · C-D11 · Karya yang Dibeli Diam-diam
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Chiasa
# │ AWALAN  : Male Route
# │ INTI    : A Akui / B sangkal
# │ AKHIRAN : nyaman_yutaka + bila diakui
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C_D11:
    call kk_scene_enter("chiasa", "Studio · Karya yang dibeli diam-diam")
    nar "Yutaka membeli karya Chiasa secara anonim di pameran. Haruka, yang jeli, mengetahuinya dan menatapmu menunggu."
    "Haruka" "Pembeli anonim itu kamu, ya? Aku ingin tahu karena Chiasa tadi bilang mungkin karyanya benar-benar menarik bagi orang asing. Kalau kamu memang suka, itu bagus. Jangan biarkan dia membangun harapan dari cerita yang salah."
    call kk_family_menu("C-D11", ["Akui siapa pembelinya.", "Sangkal tahu apa-apa.", "Alihkan pembicaraan."])
    if _return == "A":
        nar "Kau mengakui pembelian dan menjelaskan bagian karya yang disukai. Haruka menyarankan kau menyampaikannya sendiri agar Chiasa tahu dukungan itu bukan belas kasihan yang perlu disembunyikan."
        chiasa "Aku senang kamu suka. Aneh rasanya baru mengetahui dari daftar pembeli, padahal kamu bisa bilang ke aku."
    elif _return == "B":
        "Haruka" "Tidak tahu? ...Hmm. Mataku jarang salah, tapi baiklah."
        nar "Ia memeriksa kembali keterangan yang dimiliki tanpa memperpanjang tuduhan. Dukungan yang semula dapat diakui dengan hangat kini menambah satu hal yang harus dipertanyakan sebelum dipercaya."
    else:
        "Haruka" "Mengalihkan pembicaraan, ya. Menarik. Aku simpan rasa penasaran ini."
        nar "Kau membahas karya lain. Haruka mengikuti secukupnya, belum membiarkan pertanyaan tadi selesai hanya karena kau menemukan topik yang lebih aman."
    return

# ┌─ PANDUAN CERITA · C-D12 · Kuas yang Dipinjam
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Chiasa
# │ AWALAN  : Chiasa host; Intim ≥ 50 dengan seorang heroine
# │ INTI    : A Gambar dia / B ajak melukis bersama / C tolak
# │ AKHIRAN : jalur yuri dengan heroine itu menguat
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C_D12:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Kuas yang dipinjam")
    nar "Seorang perempuan yang dekat denganmu mengembalikan kuas, lalu meminta kau menggambarnya jika mau. Ia menyebut boleh menolak, tetapi kegugupan yang tampak membuatmu tahu permintaan itu lebih pribadi daripada kebutuhan gambar untuk tugas."
    nar "Di meja ini kau adalah Chiasa bagi orang yang menunggu. Yang akan digambar tanganmu sendiri, bersama keinginan yang tak dapat dipinjam dari pemilik tubuh dahulu."
    call kk_family_menu("C-D12", ["Gambar dia sendiri.", "Ajak melukis bersama.", "Tolak dengan lembut."])
    if _return == "A":
        nar "Kau menanyakan posisi yang nyaman dan mulai menggambar. Hasilnya belum tentu menyerupai gaya lama, tetapi perhatian yang diberikan kepada wajah di hadapanmu terasa cukup jelas untuk membuat percakapan menjadi lebih pelan."
    elif _return == "B":
        nar "Kau menawarkan membuat gambar bersama, meniadakan keharusan salah seorang selalu dilihat sementara yang lain menilai. Kalian menukar kuas dan menertawakan kesalahan kecil, menemukan keakraban yang boleh tumbuh tanpa seluruh hasilnya harus indah."
    else:
        nar "Kau menolak dengan lembut, tidak menjadikan kegugupannya bahan gurauan. Ia menerima dan mengembalikan kuas ke tempatnya. Ada kecewa yang sah di antara kalian, tanpa perlu diperbaiki dengan persetujuan yang sebenarnya tidak diinginkan."
    return

# ┌─ PANDUAN CERITA · C-D13 · Mata yang Kering
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Chiasa
# │ AWALAN  : framing_koita terpasang; fallout mulai terlihat publik
# │ INTI    : A Tetap tenang / B berpura-pura sedih di depan orang / C diam-diam merasa goyah
# │ AKHIRAN : tenang: nurani_chiasa −15 · pura-pura sedih: reputasi aman, tidak berubah · goyah diam-diam: nurani_chiasa +10, membuka C-D14 lebih cepat
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C_D13:
    call kk_scene_enter("chiasa", "Dari jauh · Mata yang kering")
    nar "Di seberang halaman, Koita berhenti berbicara ketika dua teman mengubah arah untuk menghindarinya. Tuduhan yang dibangun di atas kebohongan sudah mencapai orang yang tidak pernah mendengar penjelasannya. Chiasa menyaksikan ia menurunkan tangan yang semula hendak melambai. Ia mengenal gerakan kecil itu lebih baik daripada siapa pun."
    call kk_family_menu("C-D13", ["Tetap tenang menyaksikannya.", "Berpura-pura sedih di depan orang.", "Diam-diam merasa goyah."])
    if _return == "A":
        nar "Chiasa tidak memalingkan muka. Ia mengatakan kepada dirinya sendiri bahwa semua ini perlu terjadi, tetapi Koita tidak tampak seperti musuh yang dikalahkan. Ia hanya berdiri sendirian sambil memeriksa ponsel yang tidak berbunyi. Untuk tetap tenang, Chiasa harus berhenti memikirkan apa yang mungkin sedang ditunggunya."
    elif _return == "B":
        nar "Ketika orang mendekat, Chiasa membiarkan mereka membaca kesedihan di wajahnya. Simpati yang diterimanya terasa asing, seolah diberikan kepada orang yang tidak hadir di sana. Tidak ada yang menuntut penjelasan darinya hari itu. Kebisuan orang lain memberinya perlindungan, dan ia tahu siapa yang membayar harganya."
    else:
        chiasa "Dia masih mengecek ponselnya. Apa dia menunggu aku menelepon? ...Aku tahu apa yang kulakukan. Kenapa selama ini aku bisa bicara seolah akibatnya tidak akan sampai ke wajahnya?"
    return

# ┌─ PANDUAN CERITA · C-D14 · Pengakuan Setengah
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Chiasa
# │ AWALAN  : Trust Haruka atau yutaka_harap Sedang+; framing_koita terpasang
# │ INTI    : A Biarkan mereka tahu sebagian / B tarik kembali ucapan / C mengaku penuh
# │ AKHIRAN : mengaku penuh: nurani_chiasa +25, confidant jadi saksi yang bisa meruntuhkan framing atau bersekutu diam-diam; sebagian: confidant curiga tapi tidak yakin
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C_D14:
    call kk_scene_enter("chiasa", "Pengakuan setengah")
    nar "Di hadapan orang yang ia percaya, Chiasa berkata bahwa cerita tentang Koita tidak sepenuhnya benar. Sesudah kalimat itu, ruangan terasa begitu sunyi hingga ia mendengar tarikan napasnya sendiri. Ia mencoba menyebut perbuatannya sebagai sesuatu yang terpaksa dilakukan. Orang di hadapannya tidak mengangguk untuk membantunya merasa benar."
    call kk_family_menu("C-D14", ["Biarkan mereka tahu sebagian.", "Tarik kembali ucapannya.", "Dorong ia mengaku penuh."])
    if _return == "A":
        nar "Chiasa menceritakan sebagian, cukup untuk memperlihatkan bahwa ada yang disembunyikan. Pendengarnya menanyakan keselamatan Koita dan siapa yang perlu mengetahui kebenaran. Chiasa belum sanggup menjawab. Hubungan mereka berubah: kini ada seseorang yang tidak bisa lagi mendengar tuduhan itu sebagai cerita sederhana."
    elif _return == "B":
        chiasa "Lupakan yang barusan. Aku belum siap. ...Aku tahu itu tidak membuat kata-kataku hilang. Tapi kalau kau memintaku meneruskannya sekarang, aku takut aku akan mulai berbohong lagi."
    else:
        chiasa "Koita tidak melakukan apa yang dituduhkan kepadanya. Aku ikut membuat orang percaya bahwa dia melakukannya. Jangan berjanji akan melindungiku dari akibatnya. Tolong dengarkan sampai selesai, supaya aku tidak bisa menariknya kembali besok."
    return

# ┌─ PANDUAN CERITA · C-D15 · Nyaris Ketahuan
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Chiasa
# │ AWALAN  : framing_koita bertahan; bukti_digital mendekati ambang
# │ INTI    : A Tangani dengan tenang / B dramatisir supaya dikasihani / C biarkan saja
# │ AKHIRAN : tenang: nurani_chiasa −10, orang sekitar makin tidak curiga karena reaksinya "wajar"; dramatisir berlebihan: dibaca Shiori sebagai kejanggalan
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C_D15:
    call kk_scene_enter("chiasa", "Nyaris ketahuan")
    nar "Dalam percakapan yang semula biasa, seseorang menyebut adanya keterangan yang tidak cocok dengan tuduhan terhadap Koita. Chiasa mendengar namanya sendiri dipanggil. Shiori berada di ruangan itu, tidak memotong pembicaraan. Tak seorang pun tahu seberapa keras Chiasa sedang berusaha menjaga suaranya."
    call kk_family_menu("C-D15", ["Tangani dengan tenang.", "Dramatisir agar dikasihani.", "Biarkan saja."])
    if _return == "A":
        nar "Chiasa menjawab dengan tenang tanpa membiarkan kegelisahannya terlihat. Percakapan beralih, dan beberapa orang menganggap ketenangannya cukup untuk menyingkirkan keraguan mereka. Ia tetap duduk sampai selesai, semakin sadar bahwa orang bisa berhenti bertanya tanpa pernah sungguh mengetahui kebenaran. Koita tetap menanggung akibat kebodohan itu."
    elif _return == "B":
        nar "Chiasa bereaksi begitu keras hingga orang lain mulai menenangkannya. Shiori tidak ikut menyimpulkan apa pun dari air mata itu. Sesudah percakapan bubar, ia mengatakan bahwa pertanyaan tentang kebenaran masih perlu dijawab. Chiasa merasakan untuk pertama kalinya bagaimana tatapan yang teliti dapat menembus rasa kasihan."
    else:
        nar "Chiasa diam. Orang yang bertanya akhirnya mengalah kepada suasana canggung dan tidak melanjutkan. Bahaya hari itu berlalu karena orang lain lelah bertengkar, bukan karena tuduhan menjadi benar. Dalam perjalanan pulang, Chiasa tidak mampu menikmati kelegaan yang telah ditunggunya."
    return

init 1 python:
    _hook("C-D01-A", lambda: (kk_rel("chiasa","trust",4), kk_flag("koita_arah_success")))
    _hook("C-D01-B", lambda: kk_rel("chiasa","intim",4))
    _hook("C-D01-C", lambda: kk_rel("chiasa","trust",5))
    _hook("C-D01-D", lambda: None)
    _hook("C-D04-A", lambda: kk_rel("chiasa","aff",4))
    _hook("C-D04-B", lambda: kk_rel("chiasa","trust",4))
    _hook("C-D04-C", lambda: (kk_flag("yoshie_dekat"), kk_rel("chiasa","trust",5)))
    _hook("C-D05-A", lambda: kk_adj("curiga_daisuke",10))
    _hook("C-D06-A", lambda: kk_rel("chiasa","trust",3))
    _hook("C-D06-B", lambda: kk_rel("nagisa","jeal",6))
    _hook("C-D06-C", lambda: (kk_flag("koita_success_terlihat") if kk_has("koita_arah_success") else None))
    _hook("C-D08-A", lambda: (kk_adj("yutaka_harap",8), kk_flag("koita_lihat_teras")))
    _hook("C-D08-B", lambda: kk_adj("yutaka_harap",4))
    _hook("C-D08-C", lambda: kk_adj("yutaka_harap",-4))
    _hook("C-D09-A", lambda: (kk_adj("nyaman_yutaka",8), kk_rel("chiasa","intim",4)))
    _hook("C-D09-B", lambda: kk_rel("chiasa","aff",3))
    _hook("C-D09-C", lambda: None)
    _hook("C-D09-D", lambda: (kk_flag("chiasa_dimanfaatkan"), kk_adj("nyaman_yutaka",-10)))
    _hook("C-D10-A", lambda: kk_flag("koita_success_berisiko"))
    _hook("C-D10-B", lambda: kk_adj("curiga_orangtua",6))
    _hook("C-D10-C", lambda: None)
    _hook("C-D11-A", lambda: (kk_adj("nyaman_yutaka",8), kk_rel("chiasa","trust",3)))
    _hook("C-D11-B", lambda: kk_adj("curiga_haruka",5))
    _hook("C-D11-C", lambda: kk_adj("curiga_haruka",3))
    _hook("C-D12-A", lambda: (kk_flag("chiasa_yuri_tumbuh"), kk_rel("chiasa","intim",5)))
    _hook("C-D12-B", lambda: kk_rel("chiasa","aff",4))
    _hook("C-D12-C", lambda: kk_rel("chiasa","aff",-3))
    _hook("C-D13-A", lambda: kk_chiasa_conscience(-15))
    _hook("C-D13-B", lambda: None)
    _hook("C-D13-C", lambda: (kk_chiasa_conscience(10), kk_flag("chiasa_goyah")))
    _hook("C-D14-A", lambda: (kk_chiasa_conscience(8), kk_flag("chiasa_confidant_curiga")))
    _hook("C-D14-B", lambda: kk_chiasa_conscience(-5))
    _hook("C-D14-C", lambda: (kk_chiasa_conscience(25), kk_flag("chiasa_mengaku_penuh"), kk_flag("framing_terbuka")))
    _hook("C-D15-A", lambda: kk_chiasa_conscience(-10))
    _hook("C-D15-B", lambda: (kk_flag("shiori_baca_kejanggalan"), kk_adj("curiga_shiori",8)))
    _hook("C-D15-C", lambda: None)
