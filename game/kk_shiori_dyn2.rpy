# Event dinamis Shiori tambahan (S-D01/02/05/06/10/11/12) — permainan baca-membaca,
# persekutuan melawan antagonis, dan titik-titik rawan. Konsekuensi + karakter.

# ┌─ PANDUAN CERITA · S-D01 · Langkah Jam Dua Belas
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : pemain tahu jam online Shiori
# │ INTI    : A main serius / B ajak bicara di chat / C log off tiba-tiba
# │ AKHIRAN : akun_anonim +; log off tiba-tiba membuatnya curiga
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S_D01:
    call kk_scene_enter("shiori", "Papan catur daring · Jam dua belas")
    nar "Pukul dua belas, akun anonim yang sudah kaukenali menyalakan tantangan. Di kampus Shiori dapat memutus percakapan dengan senyum. Di papan daring, ia tinggal sebagai serangkaian keputusan yang harus dijawab dengan kesungguhan yang sama."
    call kk_family_menu("S-D01", ["Main serius sampai tuntas.", "Ajak bicara lewat kolom chat.", "Log off tiba-tiba."])
    if _return == "A":
        shiori "Lawan yang ini... berbeda. Membuatku serius. Siapa kau sebenarnya?"
        nar "Kau menyelesaikan pertandingan tanpa menggunakan identitas tersembunyi untuk mengejek hal yang hanya diketahui dari kampus. Di akhir ia mengirim undangan untuk malam lain, tertarik pada orang yang belum diberi nama."
    elif _return == "B":
        shiori "Kau mengajakku bicara di tengah pertandingan? Berani. ...Aku suka itu."
        nar "Percakapan dimulai dari permainan, lalu berpindah ke hal kecil yang membuat hari melelahkan. Ia tidak menyebut nama keluarga. Kau mendengar versi dirinya yang belum harus menanggapi seluruh reputasi yang datang sebelum ia bicara."
    else:
        nar "Kau keluar tanpa kabar. Shiori menunggu beberapa menit lalu menutup tantangan, belum tahu apakah ia sedang dihindari atau hanya menghadapi koneksi yang gagal."
        nar "Kali berikutnya ia akan memperhatikan lebih banyak hal sebelum memberi waktu pada percakapan yang sama. Ketidaktahuan membuatnya penasaran, tidak otomatis semakin dekat."
    return

# ┌─ PANDUAN CERITA · S-D02 · Kuroiwa di Parkiran
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : kuroiwa_percaya ≥ 50, atau marah[[pemain] ≥ 40
# │ INTI    : A Jujur / B menghindar dengan sopan / C tanya soal Shiori
# │ AKHIRAN : Kuroiwa menjadi saluran peringatan
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S_D02:
    call kk_scene_enter("shiori", "Parkiran · Kuroiwa mendekat")
    nar "Kuroiwa menutup pintu mobil setelah memastikan Shiori sudah menuju ruang acara. Ia menyapamu tanpa menghalangi jalan, sikap seseorang yang ingin bertanya jelas alih-alih mengandalkan ukuran tubuh untuk membuatmu takut."
    "Kuroiwa" "Saya sudah mendampinginya sejak kecil. Ia tidak meminta saya menguji teman-temannya. Tetapi saya ingin tahu apakah Anda memahami bahwa kepercayaannya bukan akses yang boleh dipakai sesuka hati."
    call kk_family_menu("S-D02", ["Jujur soal niatmu.", "Menghindar dengan sopan.", "Balik bertanya soal Shiori."])
    if _return == "A":
        nar "Kau menjawab tanpa menjanjikan sesuatu yang belum diketahui. Kuroiwa menanyakan satu hal sulit, lalu menerima ketika kau membedakan keinginanmu dari kepastian tentang perasaan Shiori."
        "Kuroiwa" "Baik. Bicarakan dengan dia juga. Saya bisa membantu menjaga keselamatannya, bukan menjawab siapa yang seharusnya ia percaya."
    elif _return == "B":
        "Kuroiwa" "Mengelak. Baik. Tapi tahu saja: aku tidak akan jauh dari dia."
        nar "Ia memberi jalan setelah itu, tidak menganggap kesopananmu sama dengan jawaban. Pada kesempatan berikutnya keramahan tetap ada, namun kemudahan mendekat harus lebih dahulu melewati pertanyaan yang belum dijawab."
    else:
        "Kuroiwa" "Jika ingin mengenalnya, tanyakan kepadanya. Kalau yang ditanyakan cara memastikan ia aman, saya bersedia membantu. Itu dua hal berbeda."
        nar "Ia tidak memberimu rahasia pribadi sebagai balasan atas keberanian bertanya. Batas tersebut justru menjelaskan mengapa Shiori dapat mempercayainya."
    return

# ┌─ PANDUAN CERITA · S-D05 · Buku Bertanda Tangan
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : Chiasa host
# │ INTI    : A Akui / B pura-pura tidak tahu / C tawarkan tanda tangan
# │ AKHIRAN : jembatan atau perangkap Shena
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S_D05:
    call kk_scene_enter("shiori", "Gedung Seni Rupa & Studio · Buku bertanda tangan")
    nar "Buku di tangan Shiori sudah dibaca sampai sudut sampulnya lembut. Ilustrasinya karya Shena; catatan kecil terselip pada halaman yang tampaknya sering dibuka. Ia melihat caramu mengenali gambar sebelum menyebut nama di sampul."
    shiori "Aku pengagum Shena. Karyanya seperti mengenalku. ...Kau tahu sesuatu soal siapa dia?"
    call kk_family_menu("S-D05", ["Akui kaitannya.", "Pura-pura tidak tahu.", "Tawarkan tanda tangan Shena."])
    if _return == "A":
        shiori "Jadi benar. ...Kau menyimpan rahasia sebesar itu. Sekarang aku penasaran rahasia apa lagi yang kau punya."
        nar "Kau mengakui kaitan itu dengan batas yang memang bisa dijelaskan. Shiori bertanya tentang karya lebih dahulu, lalu mendengar bagian yang membuat identitasmu sekarang tidak sesederhana dugaan seorang pembaca."
    elif _return == "B":
        shiori "Tidak tahu? Baik. Aku tidak akan menyebut firasat sebagai bukti. Tetapi jawabanmu akan kuingat."
        nar "Ia kembali membuka buku. Yang dapat kaulihat hanyalah jeda lebih panjang sebelum ia mengajak membicarakan gambar lagi."
    else:
        shiori "Tanda tangan asli Shena? Untukku? ...Kau tahu cara membuat seseorang berhutang budi."
        nar "Kau mengatakan ia tidak perlu berutang untuk menikmati karya. Shiori tertawa, lalu meminta dituliskan namanya tanpa gelar atau tambahan yang biasa mengikuti nama Saionji."
    return

# ┌─ PANDUAN CERITA · S-D06 · Gala dan Tojo
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : Tojo aktif
# │ INTI    : A Terima / B tolak / C datang bersama orang lain
# │ AKHIRAN : orang tua Saionji bertemu pemain; jalur Tojo
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S_D06:
    call kk_scene_enter("shiori", "Undangan gala")
    shiori "Orang tuaku mengadakan gala. Mereka tahu aku tidak ingin semua percakapan berakhir pada Tojo. Dia tetap akan datang. Maukah kamu menemaniku supaya ada bagian malam yang bisa kuhabiskan dengan orang yang memang ingin kutemui?"
    nar "Ia mengakui tawaran itu juga akan mengalihkan perhatian tamu. Keluarganya tidak memerlukan sandiwara hubungan; lingkungan lain mungkin akan menafsirkannya sendiri."
    call kk_family_menu("S-D06", ["Terima jadi pasangan pengalih.", "Tolak permintaannya.", "Datang bersama orang lain."])
    if _return == "A":
        shiori "Terima kasih. Di depan orang tuaku, bersikaplah wajar. Sisanya biar aku yang atur."
        nar "Kalian menyepakati bagaimana akan diperkenalkan. Shiori tidak meminta kau menjanjikan keintiman yang tidak diinginkan hanya agar tamu lain mudah mengerti mengapa kalian datang bersama."
    elif _return == "B":
        shiori "Baik. Aku kecewa sedikit, tapi aku bisa menghadapi malam itu. Kuroiwa dan keluargaku juga ada."
        nar "Ia merapikan undangan, menerima penolakan tanpa mengubahnya menjadi tuntutan agar kau membuktikan peduli dengan cara lain."
    else:
        nar "Kau datang bersama orang lain. Shiori menyambut keduanya dengan sopan, menyesuaikan rencana tanpa membiarkan rasa cemburu menentukan perlakuan kepada tamu."
        nar "Tojo memperhatikan perubahan itu dan mulai mendekat lagi. Malam yang diharapkan memberi ruang bagi Shiori justru menuntut ia menjaga wajah pada dua arah sekaligus."
    return

# ┌─ PANDUAN CERITA · S-D10 · Musuh Bersama
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : pemain memberi bukti tentang Ogawa atau Kuga
# │ INTI    : A Bergabung / B biarkan ia sendiri / C minta ia berhenti
# │ AKHIRAN : E-SH-10 menguat; Harumi dan Moeka terbantu
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S_D10:
    call kk_scene_enter("shiori", "Klub Catur · Musuh bersama")
    nar "Keterangan tentang Ogawa dan Kuga membuat Shiori berhenti tersenyum sebelum mencapai halaman terakhir. Ia membacanya dua kali, memisahkan bagian yang dapat diverifikasi dari bagian yang masih perlu ditanyakan."
    shiori "Ada orang yang dilukai. Aku ingin pelakunya kehilangan ruang untuk terus melakukannya. Kalau kita bekerja sama, kita perlu memastikan itu tidak berubah menjadi pertunjukan tentang betapa pandainya kita."
    call kk_family_menu("S-D10", ["Bergabung dengannya.", "Biarkan ia bergerak sendiri.", "Minta ia berhenti."])
    if _return == "A":
        shiori "Sekutu. Tapi keputusan tentang cerita Harumi dan Moeka perlu melibatkan mereka. Kita tidak sedang mengambil alih hak bicara hanya karena merasa tahu cara menang."
        nar "Kau menyetujui, lalu membicarakan bantuan yang dapat diberikan tanpa memaksa keduanya tampil sebagai bukti pada hari yang belum mereka pilih."
    elif _return == "B":
        nar "Kau menyerahkan keterangan dan tidak ikut bergerak. Shiori menanyakan batas penggunaan informasi tersebut, kemudian meneruskan upaya melalui orang-orang yang dapat membantu. Ketiadaanmu tidak membuat persoalan berhenti penting."
    else:
        shiori "Berhenti? ...Kau tahu aku tidak pandai berhenti. Tapi akan kupertimbangkan, karena kau yang minta."
        nar "Ia menanyakan apakah kau takut pada akibat bagi korban atau sekadar tak ingin konflik meluas kepadamu. Jawaban itu akan menentukan bagian mana dari kehati-hatianmu yang pantas didengar sebagai kepedulian."
    return

# ┌─ PANDUAN CERITA · S-D11 · Prediksi yang Benar
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : pemain sudah menceritakan Sistem
# │ INTI    : A Lanjut terbuka / B minta ia menyimpan rahasia / C manfaatkan dia
# │ AKHIRAN : E-SH-06 menguat
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S_D11:
    call kk_scene_enter("shiori", "Klub Catur · Prediksi yang benar")
    nar "Prediksi tentang Sistem terbukti pada bagian yang sebelumnya dapat diperiksa. Shiori membuka catatan lama dan menandai apa yang sungguh cocok, tidak memindahkan satu keberhasilan menjadi bukti untuk semua klaimmu sekaligus."
    shiori "Kau benar. Setiap langkah. ...Jadi yang kau ceritakan itu nyata. Pertanyaannya sekarang: apa yang akan kita lakukan dengan pengetahuan ini?"
    call kk_family_menu("S-D11", ["Lanjut terbuka padanya.", "Minta ia menyimpan rahasia.", "Manfaatkan kepercayaannya."])
    if _return == "A":
        shiori "Terbuka. Termasuk jika nanti aku menyimpulkan sesuatu yang tidak kamu sukai. Kamu tidak sedang mengajak sekutu hanya untuk mengulang keputusanmu sendiri, kan?"
        nar "Kau memberinya bagian yang selama ini tidak nyaman dibahas. Pengetahuan itu mulai menjadi sesuatu yang bisa diperdebatkan bersama, bukan sekadar alasan mempercayaimu lebih jauh."
    elif _return == "B":
        shiori "Rahasia tetap rahasia. ...Aku pandai menyimpan. Percayalah sejauh itu."
        nar "Ia meminta kalian menentukan kapan keselamatan orang lain mengharuskan mencari bantuan di luar kesepakatan tersebut. Rahasia tidak akan dipakai sebagai alasan membiarkan luka hanya agar kalian tetap merasa memegang keistimewaan."
    else:
        nar "Kau menyisakan bagian yang menguntungkanmu dan membiarkan ia merencanakan berdasarkan cerita yang tidak lengkap. Shiori bekerja dengan sungguh-sungguh, belum tahu bahwa kesediaannya membantu juga sedang dipakai untuk melindungi kebohongan baru."
    return

# ┌─ PANDUAN CERITA · S-D12 · Ratu yang Jatuh Sakit
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : tahap 4; ia begadang menyusun bukti
# │ INTI    : A Rawat / B cari bukti di kamarnya / C tinggalkan buah
# │ AKHIRAN : merawat: marah[[pemain] turun banyak; mencari bukti: kejahatan baru dan marah[[pemain] +40
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S_D12:
    call kk_scene_enter("shiori", "Kamar Saionji · Ratu yang sakit")
    nar "Shiori jatuh sakit setelah terlalu lama memaksakan diri menyusun keterangan. Kuroiwa meminta persetujuannya sebelum mengantarmu menjenguk. Di kamar, map masih menunggu dekat tempat tidur, tetapi pemiliknya tidak lagi sanggup mempertahankan ketenangan yang biasa."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABC", KK_DYN_BY_ID["S-D12"]["choices"])]
    call screen kk_choice_panel(_rows, "Ratu yang jatuh sakit")
    $ kk_record_choice("S-D12", _return)
    if _return == "A":
        shiori "Kau... merawatku? Tidak mencari apa-apa? ...Aku tidak tahu harus menaruh ini di kolom mana."
        nar "Kau menanyakan bantuan yang diinginkan dan memberi ruang bagi istirahat. Shiori melihat map sekali, lalu kembali padamu, mengakui bahwa ia tidak menduga kehadiranmu dapat berhenti pada menemaninya tanpa harga lain."
    elif _return == "B":
        nar "Ketika ia tertidur, kau mencari keterangan yang dapat melindungi dirimu. Kepercayaan untuk masuk ke kamar dipakai menembus batas lain yang tidak pernah ia izinkan."
        nar "Kau mungkin menemukan sesuatu. Jika perbuatan itu terbuka, ia juga akan memiliki jawaban yang sangat jelas tentang apa yang kaupilih saat mengira dirinya tidak mampu melihat."
    else:
        nar "Kau meninggalkan buah dan pesan singkat, lalu memberi ruang istirahat. Kuroiwa menyampaikan siapa yang datang ketika Shiori terbangun."
        nar "Ia membaca pesan dua kali, belum menyamakan satu perhatian dengan semua urusan selesai. Namun map itu tidak disentuh, dan batas yang tetap dihormati memberi sesuatu yang bisa ia pikirkan tanpa marah."
    return

init 1 python:
    _hook("S-D01-A", lambda: (kk_adj("akun_anonim",8), kk_rel("shiori","intim",3)))
    _hook("S-D01-B", lambda: (kk_adj("akun_anonim",6), kk_shiori_read(5)))
    _hook("S-D01-C", lambda: (kk_adj("curiga_shiori",10), kk_flag("shiori_curiga_akun")))
    _hook("S-D02-A", lambda: (kk_adj("kuroiwa_percaya",10), kk_rel("shiori","trust",3)))
    _hook("S-D02-B", lambda: kk_adj("kuroiwa_percaya",-5))
    _hook("S-D02-C", lambda: (kk_adj("kuroiwa_percaya",-3), kk_shiori_read(4)))
    _hook("S-D05-A", lambda: (kk_flag("shena_terbongkar"), kk_rel("shiori","intim",5)))
    _hook("S-D05-B", lambda: kk_adj("curiga_shiori",6))
    _hook("S-D05-C", lambda: (kk_rel("shiori","aff",5), kk_flag("shena_jembatan")))
    _hook("S-D06-A", lambda: (kk_flag("shiori_gala_pengalih"), kk_rel("shiori","trust",5)))
    _hook("S-D06-B", lambda: kk_rel("shiori","trust",-4))
    _hook("S-D06-C", lambda: (kk_flag("tojo_membaca"), kk_adj("marah_shiori",5)))
    _hook("S-D10-A", lambda: (kk_flag("shiori_sekutu_musuh"), kk_adj("respek_shiori",10)))
    _hook("S-D10-B", lambda: None)
    _hook("S-D10-C", lambda: kk_rel("shiori","trust",4))
    _hook("S-D11-A", lambda: (kk_flag("shiori_tahu_sistem"), kk_adj("respek_shiori",10)))
    _hook("S-D11-B", lambda: (kk_flag("shiori_tahu_sistem"), kk_rel("shiori","trust",5)))
    _hook("S-D11-C", lambda: (kk_shiori_read(8), kk_flag("shiori_dimanfaatkan")))
    _hook("S-D12-A", lambda: (kk_adj("marah_shiori",-20), kk_rel("shiori","intim",6)))
    _hook("S-D12-B", lambda: (kk_adj("marah_shiori",40), kk_flag("shiori_kamar_digeledah")))
    _hook("S-D12-C", lambda: (kk_adj("marah_shiori",-8), kk_rel("shiori","aff",4)))
