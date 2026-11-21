# Event dinamis Yutaka host (Y-D01/02/04/05/06/07/09) + Yutaka-NPC pada rute Chiasa
# (Y-D10/Y-D11). Konsekuensi + karakter; intel/identitas/keluarga.

# ┌─ PANDUAN CERITA · Y-D01 · Notifikasi Saldo
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kisaragi Yutaka
# │ AWALAN  : tanggal uang saku
# │ INTI    : A Belanja / B simpan / C beri pada seseorang
# │ AKHIRAN : arah pemakaian uang
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y_D01:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Notifikasi saldo")
    nar "Pemberitahuan transfer muncul tepat waktu. Orang tua Kisaragi mungkin lupa menelepon, tetapi tidak pernah lupa tanggal uang saku. Kau melihat angka itu sambil memikirkan orang yang menghitung ongkos pulang di depan mesin tiket. Hidup Yutaka memberimu kelonggaran yang tidak mereka miliki."
    nar "Tidak ada petunjuk penggunaan bersama transfer itu. Untuk kebutuhan sehari-hari, kau tidak harus meminta izin. Kebebasan tersebut terasa menyenangkan sekaligus kosong, seperti jawaban yang diberikan sebelum siapa pun mendengar pertanyaannya."
    call kk_family_menu("Y-D01", ["Belanja untuk dirimu.", "Simpan sebagian besar.", "Beri pada seseorang yang membutuhkan."])
    if _return == "A":
        nar "Kau membeli sesuatu untuk dirimu sendiri. Saat memilih, kau menikmati betapa sedikit harga membatasi keinginanmu hari ini. Sesudah barang dibawa pulang, apartemen masih sama sunyinya. Kenyamanan itu nyata, hanya tidak sanggup mengerjakan semua hal yang diam-diam kauharapkan darinya."
    elif _return == "B":
        nar "Kau menyisihkan sebagian besar uang itu. Menyimpan memberi rasa aman yang bisa dihitung, sementara masa depanmu di sini belum bisa. Kau menutup aplikasi setelah memeriksa angka sekali lagi, mencoba menerima bahwa persiapan kecil tetap berguna meskipun tidak menjawab seluruh ketakutanmu."
    else:
        nar "Kau menawarkan bantuan kepada orang yang membutuhkan tanpa meminta hak atas keputusannya. Ia menanyakan apakah itu pinjaman. Kau menjelaskan maksudmu sebelum membiarkannya memilih menerima. Uang itu bisa meringankan beban, tetapi kau tidak ingin kelak menyebut rasa terima kasih sebagai janji untuk menyukaimu."
    return

# ┌─ PANDUAN CERITA · Y-D02 · Teman Game yang Heran
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kisaragi Yutaka
# │ AWALAN  : Male Route
# │ INTI    : A teman online Yutaka asli: "kok mainmu beda?" Jujur sebagian / B beri alasan / C berhenti main
# │ AKHIRAN : curiga_identitas menyebar lewat dunia online
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y_D02:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Teman game")
    nar "Di antara suara permainan, teman lama Yutaka menanyakan mengapa kau berhenti mengambil keputusan yang dulu paling cepat kaulakukan. Ia mengulang satu candaan yang tidak kaupahami. Kau tertawa terlambat, dan hening di headset membuat kesalahan kecil itu terdengar jelas."
    "Hayase" "Mainmu beda sekali. Biasanya kau yang bilang aku harus tenang, sekarang kau seperti takut menyentuh tombol. Ini bukan soal menang. Kamu baik-baik saja?"
    call kk_family_menu("Y-D02", ["Jujur sebagian.", "Beri alasan masuk akal.", "Berhenti main bersamanya."])
    if _return == "A":
        nar "Kau mengakui ada banyak hal yang tidak bisa kaulakukan seperti dahulu. Temanmu menurunkan suara dan bertanya sejak kapan. Kau tidak membuka seluruh kebenaran, tetapi percakapan kini telah melewati alasan permainan. Di dunia yang hanya mengenal suaramu itu, seseorang mulai merasa kehilangan orang yang ia kenal."
    elif _return == "B":
        "Hayase" "Banyak pikiran, ya? Baik. Kita main santai saja. Kalau tidak mau main pun bilang; aku bisa tetap mengobrol tanpa menyuruhmu membuktikan skor lama."
    else:
        nar "Kau keluar dari permainan dan berhenti mengatur waktu bersama. Pesannya yang berikut masih ramah, lalu semakin jarang. Kau berhasil menghindari pertanyaan, dengan harga kehilangan seseorang yang mungkin bersedia mengenalmu lagi jika kau sanggup bertahan dalam percakapan itu."
    return

# ┌─ PANDUAN CERITA · Y-D04 · Daichi Menginap
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kisaragi Yutaka
# │ AWALAN  : kenal Daichi
# │ INTI    : A Jelaskan / B sembunyikan / C sogok
# │ AKHIRAN : daichi_tahu +
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y_D04:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Daichi menginap")
    nar "Daichi datang menginap dengan makanan dan cerita kampus, lalu menemukan catatan tentang orang-orang dekatmu di meja. Ia berhenti bercanda ketika melihat nama, waktu pertemuan, dan hal pribadi yang tampak seperti sedang dinilai. Kau mendadak melihat catatanmu melalui mata seorang tamu."
    "Daichi" "Kau mencatat mereka seperti tugas penelitian? Aku tidak tahu maksudmu, tapi beberapa hal ini sepertinya bukan untuk dibaca siapa saja. Kenapa ada di mejamu?"
    call kk_family_menu("Y-D04", ["Jelaskan apa adanya.", "Sembunyikan catatannya.", "Sogok ia agar diam."])
    if _return == "A":
        nar "Kau menjelaskan apa yang sedang kaucatat dan mengakui bahwa orang-orang itu tidak tahu. Daichi mendengar tanpa langsung memihak. Ia bertanya apakah kau sanggup mengatakan hal yang sama di depan mereka. Pertanyaan itu tidak membuatnya tahu semuanya, tetapi membuat alasanmu sendiri terdengar kurang kokoh."
    elif _return == "B":
        "Daichi" "Aku sudah lihat namanya. Menutup buku tidak membuatku lupa. Kita bisa berhenti bicara sekarang, tapi jangan minta aku menganggap tidak ada yang aneh."
    else:
        nar "Kau menawarkan uang agar Daichi tidak membicarakannya. Ia menerimanya, dan percakapan kalian menjadi terlalu sopan untuk disebut persahabatan seperti tadi. Kau mendapatkan kebisuan malam ini. Ia mendapatkan alasan untuk menanyakan berapa banyak hal lain yang sedang kaubayar supaya tetap tidak dibicarakan."
    return

# ┌─ PANDUAN CERITA · Y-D05 · Jam dari Daisuke
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kisaragi Yutaka
# │ AWALAN  : M16
# │ INTI    : A "Masih ingat jam yang tahun lalu?" Jawab yakin / B akui lupa / C alihkan
# │ AKHIRAN : curiga_identitas[[daisuke] ±
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y_D05:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Jam dari Daisuke")
    nar "Daisuke melihat pergelanganmu sebelum menyebut jam lama. Nada suaranya ringan, tetapi kau merasakan jurang antara keakraban yang ia tawarkan dan ingatan yang tidak bisa kauambil kembali. Hadiah itu pernah berarti bagi seseorang; sekarang kau harus menjawab tanpa mengetahui seluruh alasannya."
    "Daisuke" "Jam yang kuberikan tahun lalu masih ada? Aku ingat kau langsung memakainya. Waktu itu aku senang sekali, sampai Yoshie bilang aku lebih heboh daripada orang yang menerima hadiah."
    call kk_family_menu("Y-D05", ["Jawab dengan yakin.", "Akui lupa.", "Alihkan pembicaraan."])
    if _return == "A":
        "Daisuke" "Ya, yang itu. Senang kau masih menyimpannya. Benda begitu kadang cuma berguna karena kita ingat siapa yang ada bersama kita waktu menerimanya."
    elif _return == "B":
        "Daisuke" "Kau tidak ingat? ...Tidak apa-apa kalau detailnya lupa. Tapi akhir-akhir ini kau kelihatan menanggung sesuatu. Ada hal yang perlu kutahu?"
    else:
        "Daisuke" "Kita boleh bicara soal perjalanan dulu. Tapi kalau kau sedang menghindari sesuatu, jangan merasa harus terus begitu di depanku. Aku tidak sedang mengujimu dengan jam."
    return

# ┌─ PANDUAN CERITA · Y-D06 · Lidah yang Lepas di Kafe Bar
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kisaragi Yutaka
# │ AWALAN  : Jumat malam saat kerja
# │ INTI    : A Dengarkan / B rekam / C antar pulang
# │ AKHIRAN : intel untuk rute Miyuki atau Shiori
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y_D06:
    call kk_scene_enter("yutaka", "Kafe bar · Jumat malam")
    nar "Di kafe bar, Tojo bicara lebih keras setelah beberapa gelas. Ia menyebut Shiori dengan keyakinan orang yang terbiasa menganggap pilihan perempuan lain sebagai bagian dari rencananya. Kau berhenti merapikan meja ketika mendengar namanya. Suasana santai pengunjung lain membuat percakapan itu terasa semakin buruk."
    "Tojo" "Saionji masih mengira dia bisa menunda semua ini. Nanti juga dia paham apa yang paling masuk akal. ...Kau kenapa diam? Jangan pasang wajah seperti aku orang jahat."
    call kk_family_menu("Y-D06", ["Dengarkan baik-baik.", "Rekam diam-diam.", "Antar ia pulang."])
    if _return == "A":
        nar "Kau mendengarkan dan mengingat batas antara yang ia katakan dengan jelas dan kesimpulanmu sendiri. Percakapan itu memberimu alasan untuk memperingatkan Shiori, bukan hak mengambil alih keputusannya. Tojo meneruskan bicara, tidak menyadari betapa sedikit keyakinannya terdengar seperti kasih sayang."
    elif _return == "B":
        nar "Kau merekam percakapan itu. Ketika mendengarnya kembali, suara mabuk Tojo tidak terdengar lebih bijak ataupun lebih berkuasa. Rekaman tersebut masih perlu dipahami dalam konteksnya. Yang kini tak bisa kauabaikan adalah kenyataan bahwa Shiori mungkin perlu tahu apa yang dibicarakan tentang dirinya."
    else:
        nar "Kau memastikan Tojo pulang dengan aman. Ia berterima kasih dengan keakraban yang tidak kaubalas sepenuhnya. Membantu seseorang yang mabuk tidak membuatmu menyetujui perkataannya; besok ia mungkin mengingat kebaikanmu lebih mudah daripada hal yang seharusnya ia pertanggungjawabkan."
    return

# ┌─ PANDUAN CERITA · Y-D07 · Nagisa Main Sampai Pagi
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kisaragi Yutaka
# │ AWALAN  : Aff Nagisa Sedang
# │ INTI    : A Biarkan tidur di sofa / B antar pulang / C suruh pulang
# │ AKHIRAN : rumor; kelekatan Nagisa
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y_D07:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Nagisa main sampai pagi")
    nar "Cahaya pagi mulai mengubah warna tirai ketika Nagisa meletakkan pengendali. Ia menguap, lalu berusaha mengembalikan percakapan menjadi candaan agar tidak perlu mengakui betapa nyaman duduk di sini. Kau melihat jam dan menyadari malam telah berakhir tanpa salah seorang berniat mengakhirinya."
    nagisa "Aku tadi bilang satu ronde lagi berapa kali? Jangan dijawab. ...Boleh tidur di sofa sebentar? Aku terlalu mengantuk untuk berpura-pura masih jago."
    call kk_family_menu("Y-D07", ["Biarkan ia tidur di sofa.", "Antar ia pulang.", "Suruh ia pulang sendiri."])
    if _return == "A":
        nar "Kau mengambilkan selimut dan menjelaskan tempat menyimpan barangnya. Nagisa mengabari rumah sebelum tertidur di sofa. Pagi itu ada yang melihatnya keluar dan mulai menebak-nebak. Kepercayaan yang ia berikan kepadamu jauh lebih sederhana daripada cerita yang akan dibangun orang tentangnya."
    elif _return == "B":
        nagisa "Kau antar? Terima kasih. Aku tahu ini merepotkan. Dan kalau aku tidur di jalan, jangan kaujadikan bahan lelucon satu semester."
    else:
        nagisa "Baik, aku pulang. Bilang dari tadi kalau kau tidak nyaman. ...Tidak usah ikut berdiri. Aku tahu pintunya."
    return

# ┌─ PANDUAN CERITA · Y-D09 · Koita di Depan Pintu
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kisaragi Yutaka
# │ AWALAN  : Koita bertengkar atau ditinggal heroine
# │ INTI    : A Biarkan menginap / B dengarkan lalu antar pulang / C tolak
# │ AKHIRAN : benih BL atau persahabatan
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y_D09:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Jam satu pagi")
    nar "Koita berdiri di depan pintu pukul satu pagi. Rambutnya berantakan dan ia sudah menyiapkan senyum yang gagal muncul saat kau membukakan. Ia tidak membawa tas. Apa pun yang membuatnya datang tampaknya telah menghabiskan waktu lebih lama di kepalanya daripada perjalanan menuju apartemenmu."
    koita "Maaf datang tanpa kabar. Aku sudah coba menenangkan diri di jalan, tapi belum bisa pulang seperti ini. Boleh masuk sebentar? Aku tidak harus cerita semuanya sekarang, kan?"
    call kk_family_menu("Y-D09", ["Biarkan ia menginap.", "Dengarkan lalu antar pulang.", "Tolak dengan tegas."])
    if _return == "A":
        nar "Kau mempersilakannya tinggal dan menyiapkan tempat tidur. Koita duduk dekatmu sebelum akhirnya mulai bicara, sedikit demi sedikit. Kau tidak memakai kesedihannya untuk meminta jawaban romantis. Ketika ia tertidur, kau merasakan keinginan menjaganya sekaligus takut pada betapa besar arti keinginannya datang kepadamu."
    elif _return == "B":
        koita "Terima kasih sudah dengar. Aku masih sedih, tapi sekarang bisa pulang. ...Besok jangan merasa harus menganggap semuanya baik-baik saja. Tanya aku lagi, ya."
    else:
        play sound "audio/sfx/door_close.wav"
        nar "Kau mengatakan tidak bisa menerimanya malam ini. Koita mengangguk sebelum kau selesai menjelaskan, lalu meminta maaf sekali lagi. Setelah pintu tertutup, apartemen kembali tenang. Kau tidak tahu ke mana ia pergi berikutnya, dan ketidaktahuan itu tinggal lebih lama daripada alasanmu menolak."
    return

# ┌─ PANDUAN CERITA · Y-D10 · Menunggu di Stasiun
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kisaragi Yutaka
# │ AWALAN  : Female Route; yutaka_harap ≥ 50
# │ INTI    : A Jalan bersama / B terima tumpangan / C tolak
# │ AKHIRAN : yutaka_harap +
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y_D10:
    call kk_scene_enter("chiasa", "Stasiun · Yutaka menunggu")
    nar "Yutaka menunggu di luar stasiun setelah kelas malammu. Ia menoleh terlalu cepat ketika melihatmu, kemudian mencoba membuat pertemuan itu terdengar kebetulan. Di tangannya ada minuman yang belum dibuka. Kau bisa melihat ia sudah memikirkan beberapa kalimat dan kini lupa memilih salah satunya."
    yutaka "Baru selesai? Aku tadi di sekitar sini. ...Baik, itu tidak sepenuhnya benar. Aku menunggu. Kalau kau mau pulang sendiri, bilang saja."
    call kk_family_menu("Y-D10", ["Jalan bersama.", "Terima tumpangan.", "Tolak dengan sopan."])
    if _return == "A":
        nar "Kau memilih berjalan bersamanya. Yutaka menyesuaikan langkah dan menanyakan kelasmu tanpa berusaha membuat setiap jawaban menjadi godaan. Di persimpangan, ia bertanya apakah masih boleh menemani. Harapannya tumbuh justru karena kau memilih tetap berjalan, bukan karena ia berhasil menahanmu."
    elif _return == "B":
        nar "Kau menerima tawaran pulang bersamanya. Di kendaraan, percakapan terdengar lebih dekat karena tidak ada orang lain yang memotong. Yutaka mengingat tujuanmu dan tidak menambah perjalanan tanpa bertanya. Ketika sampai, ia tampak ingin malam berlangsung lebih lama, tetapi tetap membiarkanmu turun."
    else:
        yutaka "Baik, aku mengerti. Terima kasih sudah bilang terus terang. Kabari kalau nanti butuh sesuatu. ...Sampai ketemu di rumah Koita."
    return

# ┌─ PANDUAN CERITA · Y-D11 · Pengakuan Jumat Malam
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kisaragi Yutaka
# │ AWALAN  : Female Route; yutaka_harap ≥ 70
# │ INTI    : A Jawab sekarang / B tunda / C anggap candaan
# │ AKHIRAN : E-YU-01 atau E-YU-03 menguat
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y_D11:
    call kk_scene_enter("chiasa", "Kafe bar · Pengakuan Jumat malam")
    nar "Di kafe bar, Yutaka berhenti bercanda dan menaruh gelasnya jauh dari tangan. Alkohol telah membuat suaranya lebih berani, tetapi ia masih tampak takut pada jawabanmu. Kau menyadari percakapan ini perlu diingat lagi besok, ketika tidak ada minuman yang bisa dijadikan alasan."
    yutaka "Aku menyukaimu, Chiasa. Aku sudah terlalu sering bercanda sampai takut kau tidak akan percaya kalau aku serius. Kau boleh minta waktu. Aku cuma ingin malam ini kau tahu."
    call kk_family_menu("Y-D11", ["Jawab sekarang.", "Minta ia menundanya.", "Anggap candaan mabuk."])
    if _return == "A":
        nar "Kau menjawab bahwa perasaannya tidak hendak kauanggap permainan. Wajah Yutaka berubah sebelum ia sempat menutupinya dengan tawa. Kalian sepakat membicarakannya lagi saat sama-sama jernih. Yang lahir malam ini adalah kesediaan saling mendengar, bukan kewajiban memenuhi seluruh harapannya sekaligus."
    elif _return == "B":
        yutaka "Baik. Besok kita bicara lagi. Aku ingin kau menjawab orang yang benar-benar hadir, bukan cuma orang yang tadi minum terlalu banyak. Aku tidak akan marah karena kau meminta waktu."
    else:
        yutaka "Candaan... ya. Kalau itu yang ingin kaudengar. ...Maaf, aku perlu keluar sebentar. Tidak, kau tidak perlu ikut."
    return

init 1 python:
    _hook("Y-D01-A", lambda: kk_adj("uang_dibelanjakan",10))
    _hook("Y-D01-B", lambda: kk_adj("uang_disimpan",10))
    _hook("Y-D01-C", lambda: (kk_adj("uang_diberikan",10), kk_flag("pemain_dermawan")))
    _hook("Y-D02-A", lambda: (kk_adj("curiga_identitas",10), kk_flag("identitas_online_retak")))
    _hook("Y-D02-B", lambda: None)
    _hook("Y-D02-C", lambda: kk_flag("hayase_diputus"))
    _hook("Y-D04-A", lambda: (kk_adj("daichi_tahu",10), kk_flag("daichi_tahu_catatan")))
    _hook("Y-D04-B", lambda: kk_adj("daichi_tahu",3))
    _hook("Y-D04-C", lambda: (kk_adj("daichi_tahu",6), kk_flag("daichi_disogok")))
    _hook("Y-D05-A", lambda: kk_adj("curiga_daisuke",-5))
    _hook("Y-D05-B", lambda: kk_adj("curiga_daisuke",10))
    _hook("Y-D05-C", lambda: kk_adj("curiga_daisuke",4))
    _hook("Y-D06-A", lambda: (kk_flag("intel_tojo"), kk_adj("bukti_tojo",8)))
    _hook("Y-D06-B", lambda: (kk_flag("rekaman_tojo"), kk_adj("bukti_tojo",12)))
    _hook("Y-D06-C", lambda: kk_flag("tojo_berhutang_budi"))
    _hook("Y-D07-A", lambda: (kk_adj("kelekatan_nagisa",6), kk_flag("rumor_nagisa_menginap")))
    _hook("Y-D07-B", lambda: kk_rel("nagisa","trust",4))
    _hook("Y-D07-C", lambda: kk_rel("nagisa","aff",-3))
    _hook("Y-D09-A", lambda: (kk_adj("ikatan_bl",8), kk_flag("koita_arah_bl")))
    _hook("Y-D09-B", lambda: kk_rel("koita","trust",5))
    _hook("Y-D09-C", lambda: kk_koita_collapse(5))
    _hook("Y-D10-A", lambda: kk_adj("yutaka_harap",8))
    _hook("Y-D10-B", lambda: (kk_adj("yutaka_harap",10), kk_rel("chiasa","intim",3)))
    _hook("Y-D10-C", lambda: kk_adj("yutaka_harap",-5))
    _hook("Y-D11-A", lambda: (kk_flag("yutaka_ditanggapi"), kk_adj("yutaka_harap",10)))
    _hook("Y-D11-B", lambda: kk_adj("yutaka_harap",5))
    _hook("Y-D11-C", lambda: (kk_adj("yutaka_harap",-10), kk_flag("yutaka_ditolak_candaan")))
