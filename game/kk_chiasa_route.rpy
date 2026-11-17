# Milestone host Chiasa (C06, C07, C10, C12-C17): hidup pemain-sebagai-Chiasa dan
# navigasi arah (yuri / Koita Success / Yutaka). Fire saat MASUK lokasi sebagai
# host Chiasa (trigger "host"). Pilihan yang membuka arah rute disambung sebagai
# POINTER-RUTE (bendera + teks terkendali), bukan adegan eksplisit. Mengikuti
# Event_Chiasa; melengkapi C02-C05/C08/C09 (kk_chiasa_host.rpy).

# ┌─ PANDUAN CERITA · C06 · Natal Rumah Amamiya
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : A di rumah bersama Koita / B mengundang heroine / C pergi ke Nagisa/yuri / D sendirian.
# │ AKHIRAN : hub besar #3.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C06:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Natal")
    nar "Rumah Amamiya menampung dua piring, hiasan sederhana, dan kebiasaan yang belum sepenuhnya kauhafal. Koita menanyakan rencana malam ini seolah jawabanmu akan datang dengan mudah."
    nar "Natal pertama dalam tubuh Chiasa memberi alasan untuk mendekat atau mengambil jarak. Tak ada pilihan yang bisa dijelaskan hanya sebagai mengikuti jadwal orang yang dahulu tinggal di sini."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Di rumah bersama Koita.", "Mengundang salah satu heroine.", "Pergi menemui Nagisa.", "Habiskan sendirian."])]
    call screen kk_choice_panel(_rows, "Pilihan")
    $ kk_record_choice("C06", _return)
    if _return == "A":
        koita "Cuma kita berdua di rumah, ya. ...Tidak buruk. Aku jarang punya Natal yang tenang."
        nar "Kalian membagi pekerjaan dapur. Koita menceritakan kenangan Natal yang tidak kauingat, lalu bertanya apa yang ingin kaulakukan sekarang. Pertanyaan kedua jauh lebih mudah dijawab dengan jujur."
    elif _return == "B":
        nar "Kau mengundang seseorang yang ingin kaukenal lebih jauh. Kalian menyepakati waktu dan makan malam yang sederhana; ketika ia tiba, rumah tidak lagi terasa hanya sebagai panggung yang memaksamu meniru adik Koita."
    elif _return == "C":
        nagisa "Kau datang ke tempatku di malam Natal? ...Masuklah. Di luar dingin."
        nar "Ia menggeser barang dari kursi dengan gerakan cepat, mencoba menyembunyikan betapa senang undanganmu tidak membawa nama Koita sebagai alasan. Malam itu kalian bisa membicarakan sesuatu yang bukan persaingan."
    else:
        nar "Kau memilih sendiri dan memberi kabar agar tidak ada yang menunggu. Keheningan rumah terasa asing, tetapi juga memberi waktu untuk mengetahui apa yang kauinginkan ketika tak sedang dibaca oleh wajah-wajah yang mengenal Chiasa."
    return

# ┌─ PANDUAN CERITA · C07 · Coklat untuk Banyak Orang
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Valentine.
# │ INTI    : A coklat untuk Koita / B untuk heroine tertentu / C untuk Yutaka / D tidak memberi.
# │ AKHIRAN : gerbang jalur yuri/Koita Success/Yutaka.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C07:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Valentine")
    nar "Bungkus coklat di meja belum diberi nama. Kau telah melihat betapa mudah satu hadiah menjadi alasan berharap dan betapa sulit menjelaskan sesudahnya jika maksudnya sengaja dibiarkan kabur."
    nar "Hari ini kau harus memilih penerima sebelum menemukan kata yang akan mengiringinya. Tubuh Chiasa dapat membawa kebiasaan lama, tetapi niat di balik hadiah ini harus kaubawa sendiri."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Coklat untuk Koita.", "Untuk heroine tertentu.", "Untuk Yutaka.", "Tidak memberi pada siapa pun."])]
    call screen kk_choice_panel(_rows, "Pilihan")
    $ kk_record_choice("C07", _return)
    if _return == "A":
        koita "Untukku? Terima kasih. Aku hampir otomatis bilang dari adik. Tapi aku ingin tahu maksudmu, bukan memutuskan sebelum mendengar."
        nar "Ia menyimpan hadiahmu terpisah, belum memberi jawaban atas semua yang mungkin dibawa kedekatan tersebut. Setidaknya kali ini ia mengakui ada pertanyaan."
    elif _return == "B":
        nar "Kau menuliskan pesan kepada perempuan yang kausukai. Tidak menjamin ia akan membalas, tetapi cukup jelas untuk tidak meminta ia mencari sendiri maksudmu di antara rasa manis dan sopan santun."
    elif _return == "C":
        nar "Yutaka menerima dengan kedua tangan, lalu menanyakan apakah ia boleh membukanya sekarang. Ia tidak menertawakan kegugupanmu. Ketika membaca pesan, wajah hangatnya berubah lebih serius daripada sapaan seorang teman keluarga."
    else:
        nar "Kau tidak memberi kepada siapa pun. Bahan yang tersisa dibuat untuk dimakan sendiri, tanpa nama atau pesan yang harus dipertanggungjawabkan nanti. Tidak mengaku hari ini tidak menentukan seluruh masa depan, hanya membiarkan hari itu lewat tanpa mengundang harapan baru."
    return

# ┌─ PANDUAN CERITA · C10 · Rival di Yukata
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Nagisa di festival kedua.
# │ INTI    : A damai / B tantang / C goda.
# │ AKHIRAN : kebangkitan rivalitas atau kedamaian.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C10:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Rival di yukata")
    nar "Nagisa memeriksa yukatamu dengan pandangan cepat, lalu berkata tak sedang membandingkan. Kau mengenali cara lama Chiasa akan membalasnya: satu sindiran yang membuat seluruh malam kembali tentang siapa lebih dipilih."
    nagisa "Kita mau mulai berdebat dari sekarang, atau menunggu sampai semua stan tutup? Aku cuma tanya supaya bisa mengatur waktu."
    call kk_family_menu("C10", ["Tawarkan damai.", "Tantang balik rivalitasnya.", "Goda ia alih-alih bertengkar."])
    if _return == "A":
        nagisa "Damai? ...Baik. Untuk malam ini, aku turunkan pedangku."
        nar "Kalian menukar komentar tentang makanan alih-alih Koita. Pada mulanya terasa kaku, kemudian sebuah lelucon tentang penjaga stan membuat Nagisa tertawa sebelum sempat memikirkan apakah itu berarti kalah."
    elif _return == "B":
        nagisa "Begitu caramu? Bagus. Aku lebih suka lawan yang tidak mengalah."
        nar "Kalian kembali memakai ketajaman yang sudah hafal tempat melukai. Kegembiraan bersaing membuat jarak lama terasa akrab, meski keakraban itu semakin sulit dipisahkan dari kebutuhan membuat yang lain tampak kurang."
    else:
        nagisa "He—! Jangan menggodaku di tempat ramai begini. ...Dasar."
        nar "Godaanmu kali ini menyebutnya cantik tanpa membandingkan dengan siapa pun. Nagisa mencari balasan tajam, tak menemukannya cukup cepat, lalu mengajak berjalan agar tidak harus terus berdiri dengan wajah merah."
    return

# ┌─ PANDUAN CERITA · C12 · Orang Tua Pulang
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Daisuke dan Yoshie pulang di Natal.
# │ INTI    : A menyambut / B menghindar / C membuka rahasia.
# │ AKHIRAN : gerbang Koita Success (tahap 3).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C12:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Orang tua pulang")
    nar "Koper Daisuke dan Yoshie memenuhi pintu masuk. Mereka membawa hadiah kecil dan pengetahuan tentang Chiasa yang tidak tersimpan dalam benda mana pun yang bisa kauperiksa sebelum menjawab."
    "Daisuke" "Chiasa. Kau tampak... berbeda. Lebih dewasa, mungkin. Kemari, biar kulihat baik-baik."
    call kk_family_menu("C12", ["Sambut mereka dengan hangat.", "Hindari tatapan mereka.", "Buka rahasia siapa dirimu sebenarnya."])
    if _return == "A":
        "Yoshie" "Anak kami sudah besar. ...Entah kenapa aku ingin menangis."
        nar "Kau menerima kehangatan dengan takut yang tidak terlihat dari luar. Daisuke menanyakan kabar gambar, Yoshie menanyakan tidur. Perhatian yang diberikan kepada seseorang yang mereka kenal terasa semakin sulit dipakai hanya sebagai perlindungan penyamaranmu."
    elif _return == "B":
        nar "Kau mengambil jarak dan menawarkan mengurus barang agar tak perlu menjawab terlalu lama. Daisuke memberi ruang, lalu bertanya dengan pelan apakah ada sesuatu yang membuatmu tidak nyaman berada di rumah."
        nar "Kecurigaannya datang melalui kepedulian, lebih sulit ditolak daripada tuduhan yang dapat dibantah."
    else:
        nar "Kau menceritakan siapa dirimu dan apa yang tidak bisa dijelaskan sebagai perubahan biasa. Daisuke meminta kau berhenti sejenak agar ia dapat memahami, sementara Yoshie tetap menatap wajah anak yang dikenalnya."
        "Yoshie" "Aku belum tahu apa yang harus kupercaya. Tapi aku ingin mendengar sampai selesai. Jangan menjanjikan jawaban yang tidak kamu punya hanya supaya kami tenang."
    return

# ┌─ PANDUAN CERITA · C13 · Hari Bentrok: Chiasa
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : hari pengakuan.
# │ INTI    : A mengaku pada Koita / B mengaku pada heroine / C mengaku pada Yutaka / D tidak mengaku.
# │ AKHIRAN : hub besar #8.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C13:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Hari pengakuan")
    nar "Permintaan bertemu datang di antara rencana orang-orang lain menyatakan perasaan. Kau tidak dapat mengatur agar setiap jawaban melindungi semua kedekatan sekaligus."
    nar "Yang dapat dipilih adalah berhenti memakai wajah Chiasa sebagai alasan bahwa kedekatanmu pasti sudah dimengerti tanpa perlu dikatakan."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Mengaku pada Koita.", "Mengaku pada seorang heroine.", "Mengaku pada Yutaka.", "Tidak mengaku pada siapa pun."])]
    call screen kk_choice_panel(_rows, "Pilihan")
    $ kk_record_choice("C13", _return)
    if _return == "A":
        chiasa "Aku ingin kamu mendengar ini tanpa menjawab hanya sebagai kakak. Aku menyukaimu. Aku juga tahu kamu boleh merasa berbeda."
        nar "Koita menatapmu lama, kemudian mengatakan ingin menjawab setelah benar-benar memikirkan seluruh yang ada di antara kalian. Kali ini penundaan itu diberi alasan dan batas percakapan berikutnya, bukan dibiarkan menjadi nanti yang tak berujung."
    elif _return == "B":
        nar "Kau mengucapkan perasaan kepada perempuan yang selama ini dicari dalam percakapan dan alasan kecil untuk bertemu. Sesudah kalimat itu selesai, kau memberi ruang mendengar jawabannya tanpa mencoba menyelamatkan diri dengan menyebutnya gurauan."
    elif _return == "C":
        chiasa "Aku ingin mengenalmu dengan cara yang bukan cuma teman Koita. Ini bukan permintaan agar kamu menolongku melupakan siapa pun."
        yutaka "Aku dengar. Aku juga ingin membicarakan perasaanku dengan jujur. Duduk sebentar, ya. Jangan kita lewati ini sambil pura-pura buru-buru."
    else:
        nar "Kau tidak mengaku hari itu. Orang lain tetap mengambil keputusan, tak menunggu sampai dirimu siap memilih arah. Saat malam berakhir, kebebasan menunda datang bersama kemungkinan beberapa kesempatan tak akan tersedia dengan cara yang sama lagi."
    return

# ┌─ PANDUAN CERITA · C14 · Perjalanan Perpisahan
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : A menghabiskan waktu dengan Koita / B dengan Nagisa / C dengan heroine lain.
# │ AKHIRAN : mempersempit jalur.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C14:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Perjalanan perpisahan")
    nar "Rencana perjalanan perpisahan terhampar dengan terlalu banyak tempat untuk satu hari. Teman-teman mulai membagi rombongan. Kau melihat bagaimana memilih pendamping berarti memberikan waktu yang tak dapat dibagikan utuh kepada semua orang."
    call kk_family_menu("C14", ["Bersama Koita.", "Bersama Nagisa.", "Bersama heroine lain."])
    if _return == "A":
        koita "Perjalanan berdua? ...Baik. Rasanya sudah lama kita tidak bicara sungguh-sungguh."
        nar "Kalian membicarakan tujuan yang sama-sama diinginkan, bukan hanya mengulang tempat masa kecil. Di sepanjang jalan Koita bertanya tentang rencana setelah pulang, belajar mengenal seseorang yang selama ini terlalu mudah dianggap sudah diketahui."
    elif _return == "B":
        nagisa "Kau memilihku untuk perjalanan ini? ...Jangan membuatku berharap kalau kau tidak serius."
        nar "Kau menjelaskan bahwa ingin waktunya, bukan reaksinya terhadap Koita. Nagisa menerima, lalu mulai mengusulkan tempat yang disukai dengan antusiasme yang makin sulit ia samarkan."
    else:
        nar "Kau menyisihkan hari untuk perempuan lain yang telah menjadi dekat. Percakapan tentang barang bawaan perlahan berpindah ke hari-hari yang ingin dijalani setelah perjalanan, membuat kebersamaan itu terasa lebih nyata daripada satu pengecualian menjelang perpisahan."
    return

# ┌─ PANDUAN CERITA · C15 · Kembang Api dan Nagisa
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : A mengaku / B bergandeng / C menjaga jarak.
# │ AKHIRAN : jalur yuri Nagisa.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C15:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Kembang api dan Nagisa")
    nar "Nagisa berdiri di sampingmu saat keramaian mulai menghitung waktu pertunjukan terakhir. Ia berkali-kali hampir mengatakan sesuatu, lalu memandangi langit sebelum sempat memilih kata. Kali ini keheningan juga menjadi pertanyaan untukmu."
    call kk_family_menu("C15", ["Mengaku pada Nagisa.", "Bergandengan tangan tanpa kata.", "Menjaga jarak."])
    if _return == "A":
        nagisa "Kamu mengatakannya sekarang? Dasar... aku sudah menyiapkan cara pura-pura nggak menunggu."
        nar "Kau memastikan ia tidak harus menerima hanya karena momen terlihat sempurna. Nagisa menatapmu kembali."
        nagisa "Aku tahu aku boleh menolak. Aku justru sedang ingin bilang iya. Dengar sampai selesai, bodoh."
    elif _return == "B":
        nar "Kau menawarkan tangan, membiarkan Nagisa memilih mendekat. Ia menautkan jari dengan wajah merah, lalu menggenggam lebih erat saat ledakan pertama menyala."
        nagisa "Nanti kita bicara juga, ya. Aku senang begini, tapi nggak mau harus menerjemahkan semuanya dari tangan terus."
    else:
        nagisa "...Begitu. Ya sudah. Kembang apinya bagus, kan? Anggap saja aku tidak berharap apa-apa."
        nar "Jarak yang kaujaga terasa jelas meski kalian berdiri dekat. Nagisa kembali melihat langit dan membiarkan tangan di samping tubuhnya tetap kosong. Ia belum bisa mengakui kecewa tanpa mencoba menghapus harapan yang sempat terlihat."
    return

# ┌─ PANDUAN CERITA · C16 · Cover vs Skripsi
# │ LOKASI  : Kampus Kouseikan · Gedung Seni Rupa & Studio
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : A fokus kuliah / B fokus proyek / C berhenti.
# │ AKHIRAN : karier Chiasa.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C16:
    call kk_scene_enter("chiasa", "Gedung Seni Rupa & Studio · Cover vs skripsi")
    nar "Tenggat karya akademik dan proyek Mio saling menutup ruang di kalender. Kau sudah memindahkan waktu tidur dua kali tanpa menemukan jam tambahan. Nama Shena menjanjikan penghasilan; nama Chiasa tetap harus menyelesaikan kelulusannya."
    call kk_family_menu("C16", ["Fokus pada kuliah.", "Fokus pada proyek ilustrasi.", "Berhenti dari keduanya."])
    if _return == "A":
        nar "Kau memprioritaskan kuliah dan memberitahu Mio sebelum pekerjaan lain ikut terhambat. Kesempatan itu hilang, tetapi keputusan yang jelas memberi waktu mengerjakan sesuatu tanpa sekaligus takut pada dua orang yang menunggu."
    elif _return == "B":
        nar "Kau menerima proyek dan membicarakan penyesuaian akademik yang perlu dihadapi. Pekerjaan seni mendapat ruang nyata, bukan sekadar dilakukan di sisa tenaga. Kelulusan kini harus menanggung akibat waktu yang memang dipindahkan."
    else:
        nar "Kau menghentikan keduanya untuk sekarang. Kabar itu harus disampaikan kepada orang-orang yang sudah menunggu, dan kelegaan awal segera bertemu ruang kosong yang belum mempunyai rencana pengganti."
        nar "Berhenti dapat menjadi pilihan yang perlu. Ia tetap meminta tanggung jawab atas pekerjaan yang telah dijanjikan dan kehidupan yang akan dijalani sesudahnya."
    return

# ┌─ PANDUAN CERITA · C17 · Pameran Tunggal
# │ LOKASI  : Kampus Kouseikan · Gedung Seni Rupa & Studio
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : A hadir sendiri / B mengundang seseorang / C membatalkan.
# │ AKHIRAN : publik melihat siapa dekat dengan siapa.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C17:
    call kk_scene_enter("chiasa", "Gedung Seni Rupa & Studio · Pameran tunggal")
    nar "Karya-karya di ruang pamer memperlihatkan garis yang kaukenal dari latihan, kegagalan, dan keputusan sulit yang akhirnya tidak dibuang. Di dekat pintu ada daftar undangan yang belum seluruhnya dikirim."
    call kk_family_menu("C17", ["Hadir sendiri saja.", "Mengundang seseorang yang berarti.", "Membatalkan pameran."])
    if _return == "A":
        nar "Kau hadir sendiri dan menjawab pertanyaan pengunjung dengan nama yang kini harus ditanggung melalui pekerjaanmu. Ada bangga dan sepi pada saat yang sama. Tak satu pun membuat pilihan itu kurang sah."
    elif _return == "B":
        nar "Kau mengundang orang yang berarti dengan jelas, menanyakan apakah bersedia hadir tanpa harus menjadi bagian dari pertunjukan kedekatan. Saat ia datang, tatapan pengunjung tidak sepenting kenyataan bahwa ia mengenali beberapa garis yang pernah dilihat sebelum menjadi karya jadi."
    else:
        nar "Kau membatalkan pameran dan menghubungi pihak yang sudah bersiap. Karya-karya kembali dibungkus, belum mendapat kesempatan dibaca orang lain."
        nar "Ruangan kosong tidak menilaimu. Orang-orang yang waktunya berubah tetap berhak mendapat penjelasan, dan kau harus memulai dari percakapan itu sebelum menanyakan apakah suatu hari siap mencoba lagi."
    return

init 1 python:
    _hook("C06-A", lambda: kk_rel("koita","trust",4))
    _hook("C06-B", lambda: kk_flag("chiasa_arah_yuri"))
    _hook("C06-C", lambda: kk_rel("nagisa","intim",4))
    _hook("C06-D", lambda: kk_rel("koita","aff",-2))
    _hook("C07-A", lambda: (kk_rel("koita","intim",4), kk_flag("chiasa_arah_success")))
    _hook("C07-B", lambda: kk_flag("chiasa_arah_yuri"))
    _hook("C07-C", lambda: (kk_flag("chiasa_arah_yutaka"), kk_suspect("koita",3)))
    _hook("C07-D", lambda: None)
    _hook("C10-A", lambda: kk_rel("nagisa","trust",4))
    _hook("C10-B", lambda: kk_rel("nagisa","jeal",5))
    _hook("C10-C", lambda: (kk_rel("nagisa","intim",4), kk_flag("chiasa_arah_yuri")))
    _hook("C12-A", lambda: kk_rel("koita","aff",4))
    _hook("C12-B", lambda: kk_suspect("koita",8))
    _hook("C12-C", lambda: (kk_flag("chiasa_arah_success"), kk_flag("chiasa_rahasia_dibuka")))
    _hook("C13-A", lambda: kk_flag("chiasa_arah_success"))
    _hook("C13-B", lambda: kk_flag("chiasa_arah_yuri"))
    _hook("C13-C", lambda: kk_flag("chiasa_arah_yutaka"))
    _hook("C13-D", lambda: None)
    _hook("C14-A", lambda: (kk_rel("koita","intim",4), kk_flag("chiasa_arah_success")))
    _hook("C14-B", lambda: (kk_rel("nagisa","intim",4), kk_flag("chiasa_arah_yuri")))
    _hook("C14-C", lambda: kk_flag("chiasa_jalur_sempit"))
    _hook("C15-A", lambda: (kk_rel("nagisa","intim",8), kk_flag("chiasa_nagisa_diakui")))
    _hook("C15-B", lambda: (kk_rel("nagisa","intim",6), kk_flag("chiasa_arah_yuri")))
    _hook("C15-C", lambda: kk_rel("nagisa","jeal",5))
    _hook("C16-A", lambda: kk_flag("chiasa_fokus_kuliah"))
    _hook("C16-B", lambda: (kk_adj("kemampuan_gambar",10), kk_flag("chiasa_fokus_proyek")))
    _hook("C16-C", lambda: kk_flag("chiasa_berhenti_seni"))
    _hook("C17-A", lambda: kk_flag("chiasa_pameran_sendiri"))
    _hook("C17-B", lambda: kk_flag("chiasa_pameran_berdua"))
    _hook("C17-C", lambda: kk_flag("chiasa_pameran_batal"))
