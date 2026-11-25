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
    nar "Tinggal di dalam tubuh Chiasa pelan-pelan membuatmu hafal seluruh bunyi rumah ini saat larut malam. Derit pelan papan lantai di depan lemari es, dengung samar ketel listrik sebelum mendidih, dan goresan pena Koita di meja ruang makan yang seketika berhenti ketika ia mendengar langkahmu turun dari tangga."
    nar "Lampu dapur hanya menyala satu di atas wastafel, menyisakan lingkaran cahaya kuning hangat di meja makan yang dipenuhi kertas catatan kuliah dan buku saku Koita."
    koita "Eh, Chi-chan? Aku kira kamu sudah tidur dari tadi. Haus ya?"
    chiasa "Iya, tenggorokanku agak kering. Ko-nii sendiri masih ngerjain tugas selarut ini?"
    koita "Tinggal merapikan catatan esai sedikit lagi, tanggung kalau diputus. Kamu mau minum hangat sekalian? Aku tadi mau bikin teh sendiri, tapi kalau kamu belum ngantuk... kita bisa duduk sebentar di sini."
    nar "Koita memutar bahunya yang tampak kaku sambil menatap dua cangkir kosong di dekat baki kayu."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", KK_DYN_BY_ID["C-D01"]["choices"])]
    call screen kk_choice_panel(_rows, "Dapur jam dua")
    $ kk_record_choice("C-D01", _return)
    if _return == "A":
        chiasa "Duduk aja di situ, Ko-nii, biar aku yang seduhin tehnya. Kamu mau teh hijau panggang aja kan biar nggak makin melek sampai subuh?"
        koita "Wah, boleh banget. Kamu hafal aja yang paling aman buat lambungku malam-malam."
        nar "Kamu menuang air panas ke teko kecil, menunggu aroma teh panggang naik perlahan, lalu menggeser satu cangkir ke depan Koita. Koita langsung menyingkirkan tumpukan bukunya agar permukaan meja cukup lega untuk kalian berdua."
        chiasa "Mau kutemani sebentar sampai habis satu cangkir ini, Ko-nii?"
        koita "...Makasih ya, Chi-chan. Tadi aku hampir menganggap otomatis kamu pasti bakal bikinin kayak biasa. Padahal harusnya aku nggak seenaknya nganggep perhatianmu itu kewajiban."
        chiasa "Nggak apa-apa kok, Ko-nii. Aku memang pengin duduk sebentar juga sebelum balik tidur."
        koita "Lain kali gantian aku yang seduhin kalau kamu yang lagi lembur gambar, ya. Jangan cuma aku terus yang keenakan dilayani tiap larut malam."
        nar "Uap tipis naik di antara dua cangkir yang berdekatan. Percakapan malam itu sederhana sekali, tetapi tatapan Koita saat menerima cangkir dari tanganmu terasa jauh lebih sadar dan tertuju penuh kepadamu."
    elif _return == "B":
        chiasa "Ko-nii, kalau sebenarnya kepingin ditemani begadang, bilang terus terang aja dong. Jangan pakai teh hangat buat alasan undangan rahasia jam dua pagi begini."
        nar "Koita yang baru hendak meraih cangkir langsung terhenti. Telinganya memerah tipis di bawah lampu kuning dapur, lalu ia mengusap tengkuknya sendiri sambil tertawa pelan."
        koita "Hei, yang turun ke dapur selarut ini kan kamu juga! ...Oke deh, ketahuan. Iya, aku memang pengin ada teman ngobrol sebentar biar nggak sepi banget."
        chiasa "Tuh kan, bener tebakanku. Kalau ngaku dari awal kan lebih gampang."
        koita "Ternyata bilang 'temani aku sebentar' ke adik sendiri itu lebih memalukan daripada diam-diam nyalain ketel air, tahu nggak. Ya sudah, duduk sini deh mumpung airnya baru matang."
        chiasa "Siap, tapi besok pagi jangan telat bangun gara-gara kelamaan ngobrol ya, Ko-nii."
        koita "Tenang, paling lambat lima belas menit lagi aku beresin buku kok. Makasih ya sudah mau turun."
        nar "Tawa pelan Koita memberi keakraban lama rumah ini warna yang baru, sementara kamu duduk di seberangnya sambil belajar menimbang mana bagian dari kehangatan ini yang benar-benar tumbuh dari dirimu sendiri."
    elif _return == "C":
        nar "Kamu menarik kursi di hadapannya tanpa langsung menyentuh ketel, lalu menatap wajah Koita yang tampak letih di balik cahaya lampu meja."
        chiasa "Ko-nii, jujur aja. Yang bikin kamu belum tidur sampai jam segini itu beneran tugas kuliah, atau ada hal lain yang lagi muter di kepalamu?"
        nar "Koita mengetuk-ngetuk ujung penanya ke tepi buku catatan selama beberapa detik. Senyum santai yang biasa ia pasang perlahan turun."
        koita "Awalnya memang ngejar tenggat esai sih... tapi jujur aja, Chi-chan, aku takut kalau penanya kutaruh dan lampunya kumatikan, kepalaku malah langsung ramai mikirin hal-hal yang belum selesai kubereskan."
        chiasa "Soal orang-orang di sekitar kita di kampus, Ko-nii?"
        koita "Iya. Rasanya banyak banget percakapan setengah jalan yang selalu kutunda karena aku takut bikin orang kecewa. Ujung-ujungnya semua malah numpuk di kepala tiap malam sepi begini."
        chiasa "Kamu nggak harus langsung cari jawaban buat semuanya malam ini juga, Ko-nii. Kalau mau cerita pelan-pelan, aku dengerin kok."
        koita "Aku nggak minta kamu ikut pusing nyelesain masalahku, Chi-chan. Aku cuma pengin belajar bilang jujur kalau kepalaku lagi penuh, tanpa langsung nyuruh kamu atau orang lain membereskan semuanya buatku."
        nar "Kamu mengangguk pelan lalu menuangkan air hangat ke dua gelas kaca. Kalian duduk dalam keheningan yang tenang sampai napas Koita kembali teratur."
    else:
        chiasa "Kayaknya nggak usah deh, Ko-nii, aku cuma mau ambil air putih sebentar habis itu langsung balik tidur. Mata sudah berat banget."
        koita "Oh, iya dong, jangan ikutan begadang kalau sudah ngantuk. Biar aku aja yang selesaikan sedikit lagi di sini."
        chiasa "Jangan terlalu malam ya, Ko-nii. Selamat malam."
        koita "Selamat malam, Chi-chan. Hati-hati naik tangganya, lampunya agak redup."
        nar "Kamu membawa segelas air dingin kembali ke lantai atas. Di belakangmu, bunyi gelembung ketel listrik dan goresan pena Koita kembali mengisi ruang dapur yang sunyi."
    return

# ┌─ PANDUAN CERITA · C-D04 · Hari Pertama
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Chiasa
# │ AWALAN  : Chiasa host; siklus jatuh di hari penting
# │ INTI    : A tetap hadir / B izin / C minta bantuan Karuha atau Yoshie lewat video call
# │ AKHIRAN : hasil event hari itu bergeser; Yoshie menjadi lebih dekat
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C_D04:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Hari yang berat")
    nar "Nyeri tumpul di perut bagian bawah membuatmu berhenti melangkah di tepi tempat tidur sebelum sempat mengganti pakaian. Hari pertama siklus menstruasi Chiasa datang tepat bersamaan dengan jadwal kuliah dan agenda penting di kampus."
    nar "Kamu duduk sambil memeluk lutut beberapa detik, menarik napas perlahan. Seluruh pengetahuanmu tentang alur cerita dan jadwal karakter tidak mampu mengurangi rasa kram nyata yang menjalar sampai ke punggung bawah."
    chiasa "Aduh... berat banget ternyata. Duduk lurus aja sudah bikin lemas."
    nar "Pintu kamar diketuk pelan dari luar. Suara Koita terdengar agak khawatir."
    koita "Chi-chan? Kamu baik-baik saja di dalam? Tadi kamu belum turun juga, padahal hari ini jadwalmu padat kan?"
    chiasa "Iya, Ko-nii... aku cuma lagi nggak enak badan sedikit, perutku nyeri banget hari ini."
    koita "Oh... mengerti. Jangan dipaksakan keluar kamar dulu ya. Kalau butuh air hangat atau obat dari kotak P3K, bilang aja biar kuambilkan ke depan pintu."
    nar "Kamu menatap kalender jadwal di samping meja belajar. Agenda hari ini tetap menunggu, sementara tubuh ini jelas sedang meminta diperhatikan."
    call kk_family_menu("C-D04", ["Tetap hadir dengan menyesuaikan jadwal hari ini.", "Kirim pesan izin dan beristirahat di rumah.", "Hubungi Karuha atau video call Yoshie untuk minta bantuan."])
    if _return == "A":
        chiasa "Ko-nii, boleh tolong bikinin teh hangat sama ambilkan bantalan hangat di lemari bawah nggak? Aku tetap mau berangkat buat kelas wajibnya aja, nanti jadwal setelahnya kugeser pulang lebih cepat."
        koita "Kamu yakin sanggup jalan ke stasiun? Jangan sungkan kalau beneran berat lho, Chi-chan."
        chiasa "Aku pangkas jadwal yang nggak wajib kok, Ko-nii. Begitu kelas inti selesai aku langsung pulang."
        koita "Oke, tunggu sebentar, kubikinin teh jahe hangat terus kusiapkan botol air panasnya. Nanti tas sketsamu biar aku yang bawakan sampai stasiun biar bahumu nggak makin pegal."
        nar "Kamu meminum teh hangat perlahan, menempelkan penghangat di balik pakaian, lalu menata ulang agenda hari ini agar hanya menyisakan hal yang sungguh perlu dihadiri."
        nar "Sepanjang langkah menuju gerbang bersama Koita, kamu menjaga ritme napas tetap tenang dan berjanji pada diri sendiri untuk langsung pulang jika nyeri memburuk. Hari ini kamu benar-benar mengerti betapa banyak tenaga yang diam-diam dihabiskan seseorang hanya untuk terlihat menjalani hari seperti biasa."
    elif _return == "B":
        chiasa "Kayaknya aku izin istirahat di rumah aja deh hari ini, Ko-nii. Kalau kupaksakan ke kampus malah takut pingsan di jalan."
        koita "Keputusan bagus, Chi-chan. Sudah, kamu balik tiduran aja dulu. Mau kukirimkan pesan izin ke dosen atau kamu mau ketik sendiri ke Karuha?"
        chiasa "Biar kuketik sendiri ke Karuha buat titip catatan kelasnya, Ko-nii. Makasih ya."
        nar "Jari-jarimu sempat tertahan di atas layar ponsel, takut dianggap mencari alasan yang terlalu sepele, sebelum akhirnya kamu menekan tombol kirim ke ruang obrolan Karuha."
        play sound "audio/sfx/phone_buzz.wav"
        "Pesan Karuha" "Ya ampun, istirahat total aja di rumah, Chiasa! Catatan kuliah sama tugas studio hari ini biar aku yang fotoin terus kukirim malam nanti. Minum yang hangat banyak-banyak ya!"
        chiasa "Makasih banyak ya, Karuha. Maaf banget jadi merepotkan."
        koita "Chi-chan, aku taruh air hangat sama kompres di depan pintu ya. Nanti siang kubuatin bubur telur kalau kamu sudah mau makan."
        nar "Kamu menarik selimut sampai bahu dan memejamkan mata. Ada beberapa urusan jadwal yang tetap harus dibereskan besok, tanpa harus menjadikan rasa sakit fisik sebagai ujian apakah dirimu pantas dipercaya."
    else:
        chiasa "Ko-nii, aku mau telepon Ibu dulu sebentar ya, terus kabari Karuha soal jadwal studio hari ini."
        koita "Iya, silakan, Chi-chan. Kalau butuh sesuatu panggil aku di bawah."
        nar "Kamu membuka panggilan video ke nomor Yoshie, ibu tiri yang paling hafal kebiasaan rumah ini. Setelah tiga dering, wajah hangat Yoshie muncul di layar ponsel dengan latar ruang tamu terang di luar negeri."
        "Yoshie" "Halo, Chiasa? Tumben banget kamu video call jam segini. Lho, wajahmu kok agak pucat begitu, Nak? Kamu lagi nggak enak badan ya?"
        chiasa "Iya, Bu... hari pertama datang bulan, terus nyerinya lumayan berat padahal hari ini ada jadwal penting di kampus. Maaf mengganggu ya, Bu, aku bingung harus mulai dari mana biar agak enakan."
        "Yoshie" "Ya ampun, nggak mengganggu sama sekali, Chiasa! Bagus banget kamu langsung telepon Ibu. Dulu juga kadang-kadang kamu suka kram parah kalau lagi kurang tidur atau kecapekan."
        chiasa "Iya, akhir-akhir ini memang agak kurang istirahat sih, Bu."
        "Yoshie" "Di lemari lorong bawah dekat kamar mandi ada bantal pemanas kain sama teh kamomil yang Ibu simpan sebelum berangkat. Kamu pakai itu dulu ya, terus kabari Karuha supaya jadwal studionya bisa digeser. Kamu boleh kok minta bantuan orang sekitar."
        chiasa "Nggak terkesan lemah ya, Bu, kalau minta jadwalnya diubah?"
        "Yoshie" "Sama sekali nggak, Sayang. Nggak semua hal harus ditangani sambil diam-diam menahan sakit cuma biar kelihatan kuat. Kalau Koita ada di rumah, suruh dia rebuskan air panas juga, jangan ditanggung sendiri ya."
        chiasa "Iya, Bu. Makasih banyak ya, aku jadi jauh lebih tenang dengar suara Ibu."
        nar "Setelah menutup panggilan dan mengirim pesan singkat ke Karuha, kamu turun mengambil bantal pemanas yang disebut Yoshie. Hangatnya tidak hanya meredakan nyeri di perut, tetapi juga melunakkan jarak di dalam rumah yang selama ini terasa begitu asing."
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
    if kk_host == "chiasa":
        nar "Pagar rendah yang memisahkan halaman Rumah Amamiya dan Rumah Sakurajima mendadak terasa jauh lebih sempit ketika kamu keluar mengambil surat di kotak pos. Nagisa sedang berdiri di sisi pagarnya sambil menenteng tas kuliah, dan langkahnya langsung berhenti begitu melihatmu."
        nagisa "Oh, Chiasa. Pas banget. Ko-kun di dalam kan? Tadi pesanku belum dibalas-balas dari kemarin."
        chiasa "Ko-nii tadi lagi istirahat di atas, Nagisa-senpai. Mungkin ponselnya masih dicas di meja."
        nagisa "...Kamu selalu tahu banget ya jadwalnya tiap jam. Enak ya kalau tinggal serumah, apa-apa jadi bisa langsung ditangani sebelum orang lain sempat nanya."
        nar "Nada suaranya terdengar datar, tetapi bahunya yang menegang dan cara jari-jarinya mencengkeram tali tas memperlihatkan rasa kesal yang sudah terlalu lama dipendam."
        chiasa "Maksudnya apa, Nagisa-senpai? Aku cuma bilang yang kulihat di rumah tadi kok."
        nagisa "Ya memang begitu kan? Belakangan ini tiap kali aku mau bicara sama Ko-kun, ujung-ujungnya kamu selalu muncul di tengah atau tahu duluan. Jangan sok jadi orang yang paling paham soal dia cuma gara-gara kalian tinggal satu atap!"
        call kk_family_menu("C-D06", ["Redakan suasana dan hentikan adu sindir.", "Balas sindiran Nagisa tanpa mundur.", "Diam saja dan biarkan pagar jadi batas."])
        if _return == "A":
            nar "Kamu menarik napas pendek dan menurunkan tanganmu dari atas pagar kayu agar sikapmu tidak terlihat menantang."
            chiasa "Nagisa-senpai, aku nggak pernah merasa tinggal serumah itu bikin aku punya hak atas Ko-nii. Kalau kamu mau bicara langsung sama dia, nanti kukasih tahu begitu dia turun, atau kamu bisa langsung ketuk pintu depan kok."
            nar "Nagisa terdiam sejenak. Kalimat tajam yang tampaknya sudah ia siapkan di ujung lidah mendadak kehilangan sasarannya."
            nagisa "...Aku nggak bilang kamu melarangku ketuk pintu. Aku cuma... sebel aja tiap kali ngerasa ketinggalan berita soal kalian."
            chiasa "Kalau ada hal yang bikin Nagisa-senpai nggak nyaman, lebih enak kita omongin biasa aja daripada saling sindir di pagar begini."
            nagisa "...Iya deh. Maaf tadi nadaku agak tinggi. Bilangin aja ke Ko-kun kalau dia sudah senggang, suruh baca pesanku."
            chiasa "Iya, nanti langsung kusampaikan, Nagisa-senpai."
            nar "Nagisa menghela napas pelan lalu melangkah masuk ke halaman rumahnya. Ketegangan di antara kalian belum sepenuhnya hilang, tetapi untuk hari ini pagar kayu itu kembali menjadi sekadar pembatas dua halaman."
        elif _return == "B":
            nar "Kamu menatap mata Nagisa lurus-lurus tanpa memalingkan wajah sedikit pun."
            chiasa "Nagisa-senpai bilang aku sok paham cuma karena serumah? Terus menurutmu, cemburu sambil ngungkit kenangan masa kecil di pagar begini bikin kamu jadi lebih berhak atas Ko-nii?"
            nar "Wajah Nagisa langsung menegang, pipinya memerah menahan kaget sekaligus amarah."
            nagisa "Apa kamu bilang barusan? Aku kenal Ko-kun jauh sebelum kalian berdua sedekat sekarang, Chiasa! Jangan pura-pura nggak sadar cara kamu nempel terus ke dia belakangan ini!"
            chiasa "Aku nggak pura-pura apa-apa kok. Kalau Nagisa-senpai memang merasa dekat banget sama Ko-nii, harusnya nggak perlu repot-repot nyindir aku di depan rumahku sendiri kan?"
            nagisa "...Terserah kamu deh! Aku malas debat sama orang yang dari tadi cuma muter balik omongan!"
            nar "Nagisa berbalik cepat dan menutup gerbang rumahnya dengan bunyi klik logam yang keras. Kamu berdiri sendirian di sisi pagar, menyadari bahwa menang adu argumen barusan justru membuat jarak di antara kedua rumah terasa makin dingin."
        else:
            nar "Kamu tidak membalas sindirannya, hanya memegang amplop surat di tanganmu sambil menatap tenang ke seberang pagar."
            nagisa "Kenapa diam aja? Nggak ada yang mau kamu jelasin?"
            chiasa "Kalau aku jelasin sekarang juga, kayaknya Nagisa-senpai lagi nggak pengin dengar penjelasanku."
            nar "Baru saja Nagisa hendak membalas, pintu depan Rumah Amamiya terbuka. Koita keluar ke beranda sambil membawa sweter tipis di tangannya."
            if kk_has("koita_arah_success"):
                koita "Chi-chan, anginnya dingin lho, jangan keluar cuma pakai baju tipis begitu... sini kupakaikan dulu."
                nar "Koita melangkah mendekat dan menyampirkan sweter ke bahumu dengan gerakan yang terlalu akrab dan alami, sebelum akhirnya menyadari keberadaan Nagisa di seberang pagar."
                koita "Eh, Nagisa-chan? Kamu di situ dari tadi? Ada perlu apa?"
                nagisa "...Nggak. Nggak jadi. Aku mau masuk dulu, permisi."
                nar "Tatapan Nagisa sempat berhenti satu detik pada tangan Koita yang masih bertumpu di bahumu sebelum ia berbalik cepat menuju pintu rumahnya. Keheningan yang kamu pilih tadi justru memperlihatkan sesuatu yang jauh lebih sulit dijelaskan."
            else:
                koita "Chi-chan? Suratnya sudah diambil? Eh, Nagisa-chan juga ada di luar ya?"
                nagisa "...Iya, kebetulan baru pulang. Aku masuk dulu ya, Ko-kun. Nanti cek ponselmu aja."
                koita "Oh, oke, nanti langsung kubaca ya! Hati-hati masuknya."
                nar "Nagisa melangkah cepat ke dalam rumahnya tanpa menoleh lagi ke arahmu. Pagar kayu di antara dua halaman itu tetap berdiri di tempatnya, membawa arti yang kini terasa lebih berat."
    else:
        nar "Di dekat pagar pembatas halaman, Nagisa dan Chiasa saling berhadapan dengan nada suara yang meninggi, mengungkit siapa yang lebih memahami Koita."
        nagisa "Jangan sok paling tahu soal Ko-kun cuma gara-gara kalian serumah!"
        chiasa "Terus Nagisa-senpai pikir cemburu begitu bikin semuanya jadi urusanmu?"
        call kk_family_menu("C-D06", ["Lerai keduanya.", "Ikut berpihak.", "Tonton dari jauh."])
        if _return == "A":
            yutaka "Sudah, berhenti dulu kalian berdua. Tetangga bisa dengar kalau terus adu suara di pagar."
            nar "Keduanya terdiam dan saling membuang pandangan, menurunkan nada bicara sebelum kalimat yang lebih tajam sempat keluar."
        elif _return == "B":
            yutaka "Kalau kalian cuma mau cari siapa yang paling berhak, nggak bakal ada habisnya."
            nar "Campur tanganmu yang condong ke satu sisi langsung membekukan suasana dan membuat pihak lain mundur dengan raut terluka."
        else:
            nar "Kamu memilih tidak masuk ke tengah adu mulut itu. Ketika keduanya akhirnya kehabisan kata dan berpisah ke rumah masing-masing, pagar di antara dua halaman itu terasa makin tegang."
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
    nar "Sepuluh menit setelah pesan singkat Yutaka masuk menanyakan apakah kamu masih bangun, suara langkah tenang terdengar berhenti di depan pagar Rumah Amamiya. Ketika kamu membuka pintu depan, Yutaka berdiri di bawah lampu teras sambil memegang dua gelas kopi hangat dalam wadah kertas."
    yutaka "Malam, Chiasa. Maaf mendadak mampir selarut ini. Tadi kamu bilang masih melek, kebetulan aku lewat toko kopi dekat stasiun jadi sekalian kubawakan dua gelas."
    chiasa "Lho, Yutaka-kun beneran jalan ke sini cuma buat antar kopi? Dingin lho di luar."
    yutaka "Sekalian cari angin juga kok habis beres-beres apartemen. Tapi kalau ternyata kamu sudah capek dan mau langsung istirahat, bilang aja terus terang ya. Satu balasan pesan bukan berarti aku punya izin buat menyita malammu."
    nar "Ia tetap berdiri di batas undakan teras, tidak melangkah masuk sebelum kamu memberi jawaban. Uap tipis mengepul dari kedua gelas kopi di tangannya di tengah udara malam yang hening."
    call kk_family_menu("C-D08", ["Undang ia masuk.", "Mengobrol di teras saja.", "Tolak dengan sopan."])
    if _return == "A":
        chiasa "Masuk aja dulu sebentar, Yutaka-kun. Di luar anginnya lumayan kencang, nanti malah masuk angin. Ruang tamunya masih nyala kok."
        yutaka "Yakin nggak mengganggu Koita di atas? Kalau begitu aku numpang duduk sepuluh menit aja ya."
        nar "Kamu mempersilakannya masuk dan menutup pintu teras perlahan. Tepat sebelum pintu merapat, tirai jendela kamar lantai atas sempat bergerak tipis. Koita berdiri di balik kaca, memperhatikan lampu teras yang menyala lebih lama dari biasanya."
        nar "Di ruang tamu, Yutaka meletakkan gelas kopi di atas tatakan kayu dan menanyakan tugas sketsa yang sedang kamu kerjakan minggu ini."
        yutaka "Kelihatannya tanganmu nggak setegang awal semester kemarin ya, Chiasa. Sketsa yang kemarin kamu ceritakan buat kelas studio sudah hampir beres?"
        chiasa "Sudah mulai ketemu polanya sedikit-sedikit, Yutaka-kun. Masih harus banyak latihan garis, tapi setidaknya nggak sebuntu bulan lalu."
        yutaka "Bagus dong. Kalau kapan-kapan butuh teman buat cari kafe tenang atau sekadar bawa pulang kertas gambar yang berat, kabari aja. Aku suka dengar kamu cerita soal hal yang lagi kamu kerjakan sekarang."
        nar "Perhatian Yutaka tertuju sepenuhnya pada dirimu yang sedang duduk di hadapannya malam ini, tanpa memaksamu mengingat kenangan masa kecil Chiasa yang tidak kamu miliki."
    elif _return == "B":
        chiasa "Kita ngobrol sebentar di bangku teras sini aja ya, Yutaka-kun? Udara malamnya enak juga asal sambil pegang kopi hangat."
        yutaka "Teras aja sudah lebih dari cukup kok. Aku senang banget bisa ngobrol tenang begini. Oh iya, yang kiri ini agak manis, kalau ternyata kemanisan buat seleramu nggak usah dipaksa habis cuma gara-gara kubawa ya."
        chiasa "Haha, tenang aja, aku suka kopi susu manis kalau malam-malam begini. Kuliahmu sendiri minggu ini nggak bikin pusing, Yutaka-kun?"
        yutaka "Lumayan padat, ada tugas kelompok yang orangnya susah banget dikumpulkan. Tapi begitu lihat lampu teras rumah ini masih nyala, entah kenapa capeknya agak turun."
        nar "Kalian duduk berdampingan dengan jarak yang nyaman di bangku kayu teras. Di jendela lantai atas, bayangan Koita sempat melintas dan berhenti sebentar memperhatikan kalian dari balik kaca."
        chiasa "Makasih ya kopinya, Yutaka-kun. Beneran pas banget hangatnya."
        yutaka "Sama-sama, Chiasa. Kalau gelasnya sudah habis, aku langsung pulang biar kamu nggak kelamaan kena angin malam."
        nar "Sekali ini kamu membiarkan percakapan berjalan tenang apa adanya tanpa buru-buru menghentikannya demi menenangkan tatapan dari jendela lantai atas."
    else:
        chiasa "Maaf banget ya, Yutaka-kun, malam ini aku memang sudah mau siap-siap tidur soalnya besok ada kelas pagi. Lain kali aja ya ngobrolnya."
        yutaka "Oh, begitu ya? Nggak perlu minta maaf, aku memang mampir dadakan kok. Kopinya mau kutinggal di sini buat kamu minum sebentar sebelum tidur, atau kubawa pulang lagi biar nggak bikin kamu melek?"
        chiasa "Tinggalin satu aja boleh, Yutaka-kun, biar nggak mubazir sudah jauh-jauh beli. Makasih banyak ya perhatiannya."
        yutaka "Sip, ini yang kadar kopinya paling ringan kok. Selamat istirahat, Chiasa. Hati-hati kunci pintunya lagi."
        nar "Ia menyerahkan gelas kertas itu dengan senyum ringan lalu berbalik melangkah keluar pagar. Yutaka menerima penolakanmu dengan bersih tanpa sedikit pun menjadikan kopinya sebagai alasan untuk memaksamu tetap membuka pintu."
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
    play sound "audio/sfx/phone_vibrate.wav"
    nar "Ponsel rumah dan ponselmu berdering hampir bersamaan di ruang tamu. Begitu kamu mengangkat panggilan masuk dari nomor luar negeri, suara riuh pengumuman terminal bandara langsung terdengar di latar belakang."
    "Daisuke" "Halo, Chiasa? Maaf banget Ayah baru sempat kasih kabar begitu turun dari pesawat! Jadwal rapat akhir tahun di sana mendadak dimajukan selesai kemarin, jadi Ayah sama Ibu langsung ambil penerbangan pulang buat Natal!"
    chiasa "Eh?! Ayah sama Ibu sudah sampai di bandara sekarang?!"
    nar "Koita yang tadinya sedang merapikan piring di meja makan langsung menoleh kaget dan berjalan cepat mendekat ke sampingmu."
    koita "Apa, Chi-chan? Ayah sama Ibu sudah mendarat? Serius?!"
    "Yoshie" "Halo, Chiasa, itu suara Koita di sebelah ya? Maaf ya bikin kalian kaget mendadak begini. Kami baru selesai ambil koper di gerbang kedatangan. Kalian sempat nggak jemput kami pakai mobil ke bandara, atau kami naik bus limusin sendiri aja ke stasiun?"
    nar "Kepulangan yang sama sekali tidak masuk kalender itu berarti kamu dan Koita tidak punya waktu panjang untuk menata ulang suasana rumah maupun menyiapkan jawaban rapi seperti keluarga yang mereka bayangkan dari jauh."
    koita "Gimana, Chi-chan? Kuncinya ada di rak dekat pintu sih, tapi kita harus putuskan sekarang."
    call kk_family_menu("C-D10", ["Jemput mereka.", "Tidak menjemput.", "Suruh orang lain menjemput."])
    if _return == "A":
        chiasa "Kami jemput aja, Bu! Ayah sama Ibu tunggu di dekat pintu keluar terminal kedatangan ya, kami langsung jalan sekarang sama Ko-nii."
        "Yoshie" "Wah, syukurlah kalau nggak merepotkan. Hati-hati di jalan ya, Koita nyetirnya pelan-pelan aja."
        nar "Kamu dan Koita langsung mengambil jaket lalu berangkat menuju bandara. Begitu koper masuk bagasi dan kalian berempat duduk berdekatan di dalam kabin mobil yang hangat, suasana akrab keluarga langsung terasa sekaligus menyempitkan ruang gerak."
        "Daisuke" "Lho, kalian berdua kelihatan makin akur banget ya sekarang? Tadi Ayah lihat Koita sampai hafal banget posisi sandaran kursi Chiasa di depan."
        koita "Ah, itu... soalnya akhir-akhir ini sering keluar belanja kebutuhan rumah bareng, Yah, jadi kebiasaan aja."
        "Yoshie" "Chiasa juga kayaknya tidurnya lebih teratur ya sekarang? Wajahmu kelihatan beda sedikit, tapi tetap sehat. Oh iya, kemarin-kemarin kalian masak apa aja berdua di rumah?"
        chiasa "Macam-macam kok, Bu, kadang gantian masak sup sama tumisan biasa kalau sama-sama pulang cepat."
        if kk_has("koita_arah_success"):
            nar "Di kursi depan, cara tangan Koita refleks menyentuh lenganmu saat memastikan sabuk pengamanmu terpasang membuat pandangan Yoshie dari kaca spion tengah tertahan satu detik lebih lama dari biasanya."
            nar "Setiap pertanyaan ringan soal jam tidur, kebiasaan makan, dan rutinitas berdua terasa menguji seberapa tipis batas kedekatan yang sedang kalian simpan di dalam mobil itu."
        else:
            nar "Kamu dan Koita saling melempar pandangan sekilas lewat kaca spion sambil menjawab setiap pertanyaan hangat orang tua dengan tenang, menjaga peran sebagai dua saudara yang pulang ke rumah yang sama."
    elif _return == "B":
        chiasa "Maaf banget, Bu, Ayah... hari ini jadwal di rumah agak bentrok dan kami belum sempat siap-siap keluar bawa mobil. Nggak apa-apa kan kalau Ayah sama Ibu naik taksi atau bus bandara dulu ke rumah? Nanti kami siapin makan hangat di sini."
        "Yoshie" "Oh, begitu ya? Nggak apa-apa kok, Nak, kami kan memang pulangnya mendadak banget. Kalian tunggu di rumah aja."
        nar "Beberapa waktu kemudian, bunyi roda koper terdengar di depan pagar. Begitu pintu dibuka, Daisuke dan Yoshie masuk membawa udara dingin Natal beserta sederet pertanyaan yang belum sempat kamu siapkan jawabannya."
        "Yoshie" "Kami sudah sampai, Chiasa, Koita. Nggak apa-apa kok tadi nggak bisa jemput. Cuma lain kali kalau ada urusan atau lagi capek, kabari terus terang aja ya."
        "Daisuke" "Iya, kami kan jauh di luar negeri. Kami nggak mau cuma mengira kalian baik-baik saja gara-gara nggak ada yang cerita kalau lagi ada masalah."
        chiasa "Maaf ya, Bu, Yah. Tadi beneran cuma kaget aja dengar kabarnya mendadak. Ayo masuk dulu, teh hangatnya baru saja matang."
        nar "Keduanya tersenyum hangat sambil melepas mantel, tetapi tatapan teliti Daisuke yang menyapu ruang tamu terasa mengingatkan bahwa jarak jauh tidak membuat mereka berhenti memperhatikan perubahan kecil di rumah ini."
    else:
        chiasa "Bu, Ayah, tunggu sebentar ya. Rumah lagi agak berantakan dan Ko-nii juga baru selesai beres-beres. Boleh nggak kalau kupesankan taksi langganan atau minta tolong Yutaka-kun jemput dulu ke bandara biar Ayah sama Ibu nggak kelamaan nunggu?"
        "Daisuke" "Oh, kalau mau pesan jemputan juga boleh banget kok, nggak usah bikin Yutaka repot kalau dia lagi sibuk."
        nar "Kamu cepat mengonfirmasi layanan jemputan bandara yang langsung menuju alamat rumah sambil memastikan sopir sudah menghubungi Daisuke, memberi kamu dan Koita jeda hampir satu jam untuk merapikan meja dan menenangkan napas."
        koita "Lumayan ada waktu buat beresin meja makan sama ruang tamu, Chi-chan. Tadi buku sketsamu masih berserakan di mana-mana."
        chiasa "Iya, untung sempat kuberitahu dulu. Ayo cepat kita rapikan sebelum taksinya sampai di depan pagar."
        nar "Satu jam tambahan itu memberimu sedikit ruang untuk menata rumah, meski kamu tahu pertanyaan hangat dari kedua orang tua tetap akan masuk bersama mereka begitu pintu depan terbuka."
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
    nar "Yutaka membeli karya Chiasa secara anonim di pameran. Karuha, yang jeli, mengetahuinya dan menatapmu menunggu."
    "Karuha" "Pembeli anonim itu kamu, ya? Aku ingin tahu karena Chiasa tadi bilang mungkin karyanya benar-benar menarik bagi orang asing. Kalau kamu memang suka, itu bagus. Jangan biarkan dia membangun harapan dari cerita yang salah."
    call kk_family_menu("C-D11", ["Akui siapa pembelinya.", "Sangkal tahu apa-apa.", "Alihkan pembicaraan."])
    if _return == "A":
        nar "Kau mengakui pembelian dan menjelaskan bagian karya yang disukai. Karuha menyarankan kau menyampaikannya sendiri agar Chiasa tahu dukungan itu bukan belas kasihan yang perlu disembunyikan."
        chiasa "Aku senang kamu suka. Aneh rasanya baru mengetahui dari daftar pembeli, padahal kamu bisa bilang ke aku."
    elif _return == "B":
        "Karuha" "Tidak tahu? ...Hmm. Mataku jarang salah, tapi baiklah."
        nar "Ia memeriksa kembali keterangan yang dimiliki tanpa memperpanjang tuduhan. Dukungan yang semula dapat diakui dengan hangat kini menambah satu hal yang harus dipertanyakan sebelum dipercaya."
    else:
        "Karuha" "Mengalihkan pembicaraan, ya. Menarik. Aku simpan rasa penasaran ini."
        nar "Kau membahas karya lain. Karuha mengikuti secukupnya, belum membiarkan pertanyaan tadi selesai hanya karena kau menemukan topik yang lebih aman."
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
    $ _top_h = max(("miyuki", "nagisa", "harumi", "moeka", "shiori"), key=lambda h: kk_rel_get(h, "intim"))
    nar "Di meja ruang belajar Rumah Amamiya yang tenang, sebuah kuas kecil bermata halus diletakkan kembali dengan rapi di sebelah tempat pensilmu."
    if _top_h == "miyuki":
        miyuki "Ini kuas yang sempat kupinjam kemarin buat merapikan label buku catatanku, Chiasa-chan. Terima kasih banyak ya sudah boleh dipinjam."
        chiasa "Sama-sama, Tachibana-senpai. Masih enak dipakai kan ujung bulunya?"
        miyuki "Enak sekali. Oh iya... kalau Chiasa-chan nggak lagi sibuk dan nggak keberatan, kapan-kapan boleh nggak... kamu gambar wajahku di buku sketsamu? Boleh banget ditolak kok kalau merepotkan."
    elif _top_h == "nagisa":
        nagisa "Nih, kuas halusmu kukembalikan, sudah kubersihkan juga tadi biar nggak kaku. Makasih ya, Chiasa."
        chiasa "Wah, rapi banget dicucinya, Nagisa-senpai. Makasih ya."
        nagisa "Eh, anu... kalau lagi senggang sekarang, kamu mau nggak bikin sketsa kecil wajahku? Bukan buat tugas apa-apa sih, cuma penasaran aja kalau aku digambar sama tanganmu jadinya gimana. Kalau malas ya nggak usah!"
    elif _top_h == "harumi":
        harumi "Ini kuas yang kupinjam buat memberi tanda di map arsip kemarin, Amamiya-san. Sudah kubersihkan dan kukeringkan."
        chiasa "Terima kasih, Kujo-senpai. Nggak usah serapi itu juga nggak apa-apa kok."
        harumi "Amamiya-san... aku boleh mengajukan permintaan yang agak pribadi nggak? Kalau waktumu longgar, aku ingin melihat diriku digambar olehmu. Tapi kalau kamu nggak nyaman, tolong langsung bilang saja."
    elif _top_h == "moeka":
        moeka "Ta-da! Kuas andalannya Chimian kembali dengan selamat tanpa rontok sehelai pun! Makasih ya sudah dipinjami!"
        chiasa "Haha, makasih sudah dijaga baik-baik, Moemoe-senpai."
        moeka "Eh, Chimian... kalau lagi santai begini, boleh nggak sekali aja aku jadi model sketsamu? Nggak usah yang serius kayak buat pameran kok, cuma pengin tahu aja gimana matamu ngelihat aku. Boleh ditolak lho kalau lagi capek!"
    else:
        shiori "Kuas yang kupinjam kemarin sudah kubawa kembali, Amamiya-san. Kondisinya masih sama seperti waktu kamu pinjamkan."
        chiasa "Terima kasih sudah repot-repot mengantar langsung, Saionji-senpai."
        shiori "Ada satu hal lagi yang ingin kutanyakan. Kalau kamu punya waktu luang hari ini dan memang bersedia, maukah kamu membuat sketsaku? Kamu boleh menolak kapan saja kalau permintaan ini terasa terlalu mendadak."
    nar "Meski ia langsung menambahkan bahwa kamu boleh menolak, kegugupan halus di ujung suaranya dan cara jemarinya menyentuh tepi meja membuatmu tahu permintaan itu jauh lebih pribadi daripada sekadar urusan gambar."
    nar "Di hadapan meja kerja ini, kamu adalah Chiasa bagi orang yang sedang menunggu jawabanmu. Yang akan menggerakkan pensil nanti adalah tanganmu sendiri, bersama perasaan yang tidak bisa dipinjam dari pemilik tubuh terdahulu."
    call kk_family_menu("C-D12", ["Gambar dia sendiri.", "Ajak melukis bersama.", "Tolak dengan lembut."])
    if _return == "A":
        nar "Kamu mengambil buku sketsa bersih dan pensil lunak, lalu menarik kursi di dekat jendela agar cahaya jatuh lembut di sisi wajahnya."
        if _top_h == "miyuki":
            chiasa "Duduk santai di sebelah jendela sini aja, Tachibana-senpai. Nggak usah kaku-kaku, lihat ke arah meja atau keluar jendela juga boleh."
            miyuki "Begini sudah pas, Chiasa-chan? ...Aneh ya, padahal biasanya aku nggak suka dilihatin lama-lama, tapi kalau kamu yang menggambar rasanya tenang sekali."
            chiasa "Tahan senyum tipis yang barusan itu sebentar ya, Senpai. Itu bagian yang paling bagus."
        elif _top_h == "nagisa":
            chiasa "Duduk di kursi dekat jendela ya, Nagisa-senpai. Santai aja bahunya, jangan kayak lagi difoto buat kartu mahasiswa."
            nagisa "Iya, iya, tahu! ...Hei, jangan lihatin mataku terlalu lama dong, bikin gugup aja. Tapi kalau sudah jadi, aku harus boleh lihat duluan lho ya."
            chiasa "Iya, pasti kutunjukkan ke Nagisa-senpai duluan sebelum siapa-siapa."
        elif _top_h == "harumi":
            chiasa "Boleh duduk agak serong ke arah jendela sedikit, Kujo-senpai? Cahayanya bagus banget buat garis wajahmu."
            harumi "Seperti ini? ...Rasanya agak canggung duduk diam tanpa melakukan apa-apa, tapi mendengarkan suara pensilmu di kertas bikin kepalaku jadi sunyi."
            chiasa "Nggak usah buru-buru kok, Kujo-senpai. Kita jalan pelan-pelan aja."
        elif _top_h == "moeka":
            chiasa "Duduk dekat jendela sini, Moemoe-senpai. Nggak usah pasang pose senyum lebar kayak di kamera ya, ekspresi santai barusan malah jauh lebih manis."
            moeka "Eh, beneran? Biasanya orang selalu minta aku senyum lebar terus lho... oke deh, aku duduk tenang aja biar Chimian gampang gambarnya."
            chiasa "Bagus banget begitu, Senpai. Tahan sebentar ya."
        else:
            chiasa "Silakan duduk dekat jendela, Saionji-senpai. Cari posisi yang paling nyaman supaya pundaknya nggak pegal."
            shiori "Seperti ini cukup nyaman. Menarik sekali ya, Amamiya-san... biasanya aku yang mengamati orang lain, sekarang aku membiarkan diriku diamati garis demi garis olehmu."
            chiasa "Aku usahakan menangkap ekspresi Saionji-senpai sejujur mungkin ya."
        nar "Hasil goresanmu memang belum tentu menyerupai gaya lama Chiasa. Meski begitu, perhatian tenang yang kamu curahkan pada setiap lengkung wajah di hadapanmu membuat suasana ruangan melambat dan percakapan di antara kalian turun menjadi bisikan yang akrab."
    elif _return == "B":
        nar "Kamu menarik dua lembar kertas gambar ke tengah meja dan menggeser kotak cat air serta kuas kecil itu persis di antara kalian berdua."
        if _top_h == "miyuki":
            chiasa "Gimana kalau kita melukis bareng aja, Tachibana-senpai? Jadi nggak cuma aku yang lihatin Senpai, kita bisa gantian bikin warna di satu kertas yang sama."
            miyuki "Eh, aku boleh ikut pegang kuas? Gambaranku kaku sekali lho, Chiasa-chan... tapi kalau bareng kamu, rasanya jadi pengin coba."
            chiasa "Nggak harus rapi kok, Senpai! Coba oleskan warna biru muda di pojok atas sini dulu."
        elif _top_h == "nagisa":
            chiasa "Daripada Nagisa-senpai cuma duduk pegal jadi model, mending kita gambar bareng aja di satu kertas gede ini! Berani nggak adu cepat bikin sketsa?"
            nagisa "Hah? Jangan remehkan tanganku waktu megang pensil lho, Chiasa! Sini kuasnya, tapi kalau catnya belepotan di jarimu jangan nyalahin aku ya!"
            chiasa "Haha, ayo aja! Yang penting seru bareng."
        elif _top_h == "harumi":
            chiasa "Kalau boleh usul, gimana kalau kita melukis bersama aja, Kujo-senpai? Jadi nggak ada yang harus merasa canggung duduk dilihatin sendirian."
            harumi "Melukis berdua ya... ide yang bagus sekali, Amamiya-san. Aku belum pernah melukis bebas tanpa aturan sejak SD. Boleh aku mulai dari garis langitnya?"
            chiasa "Tentu aja boleh, Kujo-senpai. Nanti aku sambung warna awannya di sebelahmu."
        elif _top_h == "moeka":
            chiasa "Mending kita melukis bareng aja yuk, Moemoe-senpai! Satu kertas buat berdua, kita tukeran kuas tiap lima menit!"
            moeka "Wah, seru banget idenya! Siap-siap ya Chimian, nanti aku bikin gambar bunga kecil di sebelah gambar seriusmu!"
            chiasa "Boleh banget, Senpai, biar kertasnya makin hidup!"
        else:
            chiasa "Bagaimana kalau kita melukis bersama di satu lembar kertas, Saionji-senpai? Supaya posisinya setara dan sama-sama santai."
            shiori "Menarik. Kamu selalu tahu cara memecah jarak yang terlalu kaku ya, Amamiya-san. Baik, berikan satu kuas padaku, kita lihat ke mana warna ini membawa kita."
            chiasa "Dengan senang hati, Saionji-senpai."
        nar "Kalian bertukar kuas, menertawakan sapuan cat yang meleset kecil di tepi kertas, dan menemukan keakraban hangat yang boleh tumbuh tanpa harus menuntut hasil akhirnya tampak sempurna."
    else:
        nar "Kamu meletakkan kuas itu dengan hati-hati ke dalam wadah keramik, lalu menatapnya lembut tanpa sedikit pun menganggap kegugupannya bahan candaan."
        if _top_h == "miyuki":
            chiasa "Maaf banget ya, Tachibana-senpai. Untuk hari ini kayaknya aku belum sanggup menggambar wajah Senpai. Aku nggak mau hasilnya terburu-buru padahal Senpai sudah minta baik-baik."
            miyuki "Nggak apa-apa sama sekali, Chiasa-chan. Aku yang mendadak minta kok. Terima kasih sudah bilang terus terang ke aku."
        elif _top_h == "nagisa":
            chiasa "Maaf ya, Nagisa-senpai, hari ini tanganku belum siap buat bikin sketsa wajahmu dengan benar. Lain waktu kalau aku sudah lebih mantap aja ya?"
            nagisa "Oh... iya, santai aja! Aku tadi juga cuma nanya iseng kok. Ya sudah, kuasnya sudah kukembalikan ya, aku pulang dulu."
        elif _top_h == "harumi":
            chiasa "Maaf, Kujo-senpai. Aku menghargai banget permintaanmu, tapi hari ini aku belum bisa menyanggupi menggambar potretmu."
            harumi "Saya mengerti, Amamiya-san. Terima kasih karena tidak memaksakan diri demi menjaga perasaanku. Kita bisa mengobrol soal hal lain saja lain kali."
        elif _top_h == "moeka":
            chiasa "Maaf banget ya, Moemoe-senpai, hari ini aku belum bisa gambar potret dulu. Aku lagi nggak enak maksain tangan kalau hasilnya nanti nggak sesuai harapanku."
            moeka "Hei, nggak usah merasa bersalah gitu dong, Chimian! Kan dari awal aku sudah bilang boleh ditolak. Nanti kita jajan bareng aja gantinya!"
        else:
            chiasa "Maaf, Saionji-senpai, untuk hari ini aku harus menolak dulu. Aku belum merasa siap menggambar potretmu dengan sungguh-sungguh."
            shiori "Penolakan yang jujur jauh lebih kuhargai daripada persetujuan setengah hati, Amamiya-san. Terima kasih untuk kuasnya, sampai jumpa di kampus."
        nar "Ada sedikit rasa kecewa yang sangat wajar menggantung di udara saat ia pamit, tetapi keheningan di antara kalian tetap bersih tanpa persetujuan terpaksa yang tidak sungguh-sungguh kamu inginkan."
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
        chiasa "{i}Dia masih mengecek ponselnya. Apa dia menunggu aku menelepon? ...Aku tahu apa yang kulakukan. Kenapa selama ini aku bisa bicara seolah akibatnya tidak akan sampai ke wajahnya?{/i}"
    return

# ┌─ PANDUAN CERITA · C-D14 · Pengakuan Setengah
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Amamiya Chiasa
# │ AWALAN  : Trust Karuha atau yutaka_harap Sedang+; framing_koita terpasang
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
