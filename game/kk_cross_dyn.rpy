# Event dinamis lintas-karakter (X-D01..X-D12): titik di mana dua lingkaran sosial
# bertemu. Konsekuensi + karakter; beat berat (krisis, kecurigaan gabungan) tanpa
# metode. X-D05/09 adalah node naratif (katalog: choices kosong atau dekat kosong).

# ┌─ PANDUAN CERITA · X-D01 · Pertengkaran di Konbini
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Lintas-tokoh
# │ AWALAN  : jeal[[moeka] Nagisa ≥ 60; stres_total Moeka ≥ 60; keduanya di konbini saat Dini Hari
# │ INTI    : A lerai / B bela Moeka / C bela Nagisa / D pergi
# │ AKHIRAN : stres Moeka; tahap Nagisa; bila pemain tidak ada, Ryena mendengar ceritanya besok
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_X_D01:
    call kk_scene_enter("moeka", "Konbini · Dini hari")
    nar "Pintu konbini berbunyi lagi ketika Nagisa masuk. Moeka masih memakai seragam kerja, menahan menguap sambil menghitung uang di kasir. Pertanyaan tentang Koita datang saat antrean akhirnya kosong. Moeka menjawab terlambat, dan Nagisa menganggap keterlambatan itu sebagai sikap meremehkan."
    nagisa "Aku tahu kau capek. Tapi setiap aku ingin bicara dengannya, namamu selalu muncul. Aku cuma ingin tahu apa yang sebenarnya terjadi."
    moeka "Yang terjadi sekarang, aku masih bekerja dan ingin segera pulang. Aku tidak bisa menjelaskan semua hubungan orang hanya supaya kau berhenti merasa terancam, Nagisa."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", KK_DYN_BY_ID["X-D01"]["choices"])]
    call screen kk_choice_panel(_rows, "Pertengkaran di konbini")
    $ kk_record_choice("X-D01", _return)
    if _return == "A":
        nar "Kau meminta Nagisa mundur dari meja kasir dan memberi Moeka waktu menyelesaikan pekerjaannya. Kau tidak meminta salah seorang mengalah demi menenangkan yang lain. Nagisa masih marah, Moeka masih lelah, tetapi keduanya akhirnya berhenti bicara cukup lama untuk mendengar apa yang baru saja mereka lakukan."
    elif _return == "B":
        nagisa "Jadi kau membelanya. ...Aku dengar. Aku tahu aku sedang marah, tapi jangan perlakukan aku seolah perasaanku cuma gangguan di sini."
    elif _return == "C":
        moeka "Baik. Sekarang aku harus menerima penilaian kalian sambil tetap melayani pelanggan. Kalau sudah selesai membicarakanku, tolong beri aku ruang untuk bekerja."
    else:
        nar "Kau keluar saat pertengkaran belum selesai. Dari balik kaca, kau melihat Moeka kembali berdiri tegak ketika pelanggan lain masuk. Esoknya Ryena mendengar cerita itu darinya. Ketidakhadiranmu tidak menghapus peranmu; seseorang akan mengingat bahwa kau ada, lalu memilih pergi."
    return

# ┌─ PANDUAN CERITA · X-D02 · Calon Dokter Membaca Tanda
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Lintas-tokoh
# │ AWALAN  : kelelahan Miyuki < 60; Moeka tahap ≥ 3
# │ INTI    : A Datang bersama / B minta Miyuki menangani / C abaikan
# │ AKHIRAN : jendela Moeka bisa diambil lewat Miyuki
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_X_D02:
    call kk_scene_enter("miyuki", "Kampus · Calon dokter membaca tanda")
    nar "Miyuki melihat Moeka duduk terlalu lama di tangga dan menolak makanan dengan senyum yang cepat hilang. Ia tidak menyebut diagnosis. Ia menghubungimu karena tahu ada sesuatu yang perlu ditanyakan dengan perhatian, dan ia tidak ingin Moeka merasa sedang dibicarakan tanpa diberi kesempatan bicara."
    miyuki "Aku khawatir pada Kohinata-san. Aku belum tahu apa yang sedang ia alami, dan aku tidak akan pura-pura tahu hanya karena kuliah kedokteran. Kau mau menemaniku menanyakan apa yang ia butuhkan?"
    call kk_family_menu("X-D02", ["Datang bersama Miyuki.", "Minta Miyuki menanganinya.", "Abaikan, bukan urusanmu."])
    if _return == "A":
        nar "Kalian mendekati Moeka tanpa mengepungnya. Miyuki meminta izin duduk, lalu memberi ruang ketika Moeka belum ingin menjawab. Kau mengatakan bersedia menemani. Percakapan itu tidak langsung membenahi hidupnya, tetapi membuat satu hal jelas: ia tidak perlu terlihat ceria agar tetap layak didatangi."
    elif _return == "B":
        miyuki "Baik, aku akan menanyakan apakah ia mau bicara denganku. Kalau ia meminta ditemani orang lain, kita hormati. Tolong tetap bisa dihubungi; ini bukan sesuatu yang cukup diserahkan lalu dilupakan."
    else:
        nar "Kau menolak terlibat. Miyuki mengakhiri percakapan setelah memastikan ia tidak salah mendengar. Ia tetap akan mendatangi Moeka. Kau menyadari orang lain dapat melanjutkan kepedulian tanpa persetujuanmu, dan bahwa ketidakpedulianmu sendiri juga akan diingat."
    return

# ┌─ PANDUAN CERITA · X-D03 · Dua Peringkat Teratas
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Lintas-tokoh
# │ AWALAN  : Shiori dan Harumi sama-sama percaya pada pemain
# │ INTI    : A Bergabung / B biarkan / C pecah belah
# │ AKHIRAN : bukti_ogawa melonjak; E-HA-07 dan E-SH-10 menguat
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_X_D03:
    call kk_scene_enter("shiori", "Klub Catur · Dua peringkat teratas")
    nar "Harumi membawa catatan, Shiori membawa pertanyaan yang belum terjawab. Di meja klub catur, keduanya mencoba menyusun apa yang benar-benar diketahui tentang Ogawa. Mereka berbeda cara bicara: Harumi merinci, Shiori memotong kesimpulan yang terlalu cepat. Perbedaan itu justru membuat percakapan semakin tajam."
    shiori "Kujo dan aku sepakat soal yang perlu dihentikan. Kami belum sepakat pada semua kesimpulan. Kalau kau bergabung, bantu kami memastikan fakta, bukan sekadar menambah orang yang sudah telanjur membenci Ogawa."
    call kk_family_menu("X-D03", ["Bergabung dengan keduanya.", "Biarkan mereka bergerak sendiri.", "Pecah belah aliansi itu."])
    if _return == "A":
        nar "Kau duduk dan menyumbangkan apa yang sungguh kauketahui. Harumi membedakan catatan yang dapat diperiksa dari dugaan, sementara Shiori membicarakan siapa yang perlu dilindungi ketika persoalan ini dilaporkan. Kerja bersama memberi mereka pijakan lebih kuat untuk menghentikan Ogawa tanpa menjadikan orang yang dirugikan sekadar bahan pembuktian."
    elif _return == "B":
        nar "Kau tidak ikut. Harumi mengangguk dan kembali pada catatannya; Shiori tidak meminta kau mengubah keputusan. Kerja sama mereka tetap berjalan. Untuk sekali ini, kau melihat dua orang yang tidak memerlukanmu sebagai pusat agar bisa saling mempercayai."
    else:
        nar "Kau merusak kepercayaan yang baru mereka bangun. Percakapan berubah berhati-hati, catatan ditutup lebih cepat. Saat keduanya berpisah, tidak ada kemenangan yang layak dirayakan. Ogawa tetap menjadi masalah, sementara dua orang yang bisa saling membantu kini harus menghabiskan tenaga untuk meragukan satu sama lain."
    return

# ┌─ PANDUAN CERITA · X-D04 · Dua Coklat di Satu Loker
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Lintas-tokoh
# │ AWALAN  : Valentine; dua heroine dengan Aff ≥ 55
# │ INTI    : A Jujur pada keduanya / B sembunyikan satu / C kabur
# │ AKHIRAN : Jealousy keduanya; rahasia baru
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_X_D04:
    call kk_scene_enter("koita", "Loker · Valentine")
    nar "Dua kotak cokelat menunggu di loker. Kau baru mengambil salah satunya ketika kedua pengirim datang dari arah berbeda. Sapaan mereka berhenti pada saat yang sama. Di hadapanmu ada dua orang yang sama-sama berharap perasaan mereka akan diterima dengan sungguh-sungguh."
    call kk_family_menu("X-D04", ["Jujur pada keduanya.", "Sembunyikan satu kotak.", "Kabur dari situasi."])
    if _return == "A":
        nar "Kau mengakui menerima keduanya dan menjelaskan bahwa kau belum memberi kepastian yang seharusnya dibicarakan. Tidak ada yang langsung memaafkan kecanggungan itu. Salah seorang meminta waktu, yang lain meminta jawaban lebih jelas. Kejujuran memberimu pekerjaan yang nyata, bukan jalan keluar tanpa luka."
    elif _return == "B":
        nar "Kau menyembunyikan satu kotak dan melanjutkan percakapan seolah tidak ada yang tertahan di belakang punggungmu. Pemberinya melihat gerakan itu meskipun tidak langsung memprotes. Hadiah yang disiapkan dengan gugup kini diperlakukan seperti sesuatu yang memalukan untuk diakui."
    else:
        nar "Kau pergi dengan alasan yang bahkan tidak sempat kaulengkapi. Kedua pengirim tertinggal di depan loker, dipaksa berbagi canggung yang seharusnya kautanggung bersama mereka. Nanti akan ada pesan yang perlu dijawab; melarikan diri hanya memindahkan percakapan ke tempat yang lebih sepi."
    return

# ┌─ PANDUAN CERITA · X-D05 · Rumah Amamiya Penuh
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Lintas-tokoh
# │ AWALAN  : Natal; tiga heroine atau lebih diundang
# │ INTI    : A Atur tempat duduk / B bagi perhatian / C keluar sebentar
# │ AKHIRAN : panggung kecil Hari Pengakuan; Koita mengamati
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_X_D05:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Natal")
    if kk_host == "chiasa":
        nar "Ruang makan Rumah Amamiya penuh suara dan aroma hidangan hangat pada malam Natal itu. Piring berpindah tangan, musik lembut mengalir dari pemutar kecil di sudut lemari, dan beberapa orang yang sama-sama dekat denganmu akhirnya berada di dalam satu ruangan yang sama."
        moeka "Wah, bau supnya enak banget! Chimian, aku taruh kotak kue Natalnya di tengah meja ya biar semua kebagian!"
        miyuki "Terima kasih sudah mengundang, Chiasa-chan. Aku juga membawa teh hangat buat nanti setelah makan. Boleh aku bantu tata gelasnya?"
        nagisa "Eh, piring tambahannya masih di rak dapur kan? Biar aku yang ambilkan sekalian lihat Ko-kun masih butuh bantuan apa nggak."
        nar "Dari balik meja dapur, Koita keluar membawa panci sup mengepul sambil tersenyum, tetapi sorot matanya sempat menyapu ruangan dan menangkap betapa sering beberapa tamu menoleh untuk memastikan di mana kamu berdiri."
        koita "Wah, ramai banget malam ini! Chi-chan, kursinya sudah cukup semua kan? Kamu mau atur duduknya dulu biar nggak sempit?"
    else:
        nar "Malam Natal ini kamu datang membantu Koita dan Chiasa menyiapkan jamuan di Rumah Amamiya, dan ruang makan yang biasanya tenang itu kini dipenuhi tawa serta aroma masakan hangat. Beberapa orang yang sama-sama dekat denganmu akhirnya berkumpul di bawah satu atap pada waktu yang bersamaan."
        moeka "Yutayuta! Tolong dong pembuka botol jusnya di sebelah mana ya? Aku sudah muter meja dua kali nggak ketemu!"
        miyuki "Malam, Yutaka-kun. Terima kasih sudah bantu menyiapkan meja bareng Koita-kun. Kue Natalnya kutaruh sebelah sini ya?"
        nagisa "Heh, Yutaka, jangan cuma berdiri di tengah jalan dong, gelasnya mau lewat nih. Chiasa, ini ditaruh sebelah piring besar kan?"
        chiasa "Iya, taruh situ aja, Nagisa-senpai. Makasih ya!"
        nar "Koita melangkah dari dapur membawa nampan besar berisi hidangan utama. Sambil menurunkan piring ke meja, ia sempat memperhatikan bagaimana setiap kali kamu bergerak, ada dua atau tiga pasang mata di ruangan itu yang tanpa sadar ikut menoleh."
        koita "Oke, makanan utamanya siap! Yutaka, kursinya kita atur sekarang biar semua bisa langsung duduk nyaman."
    call kk_family_menu("X-D05", ["Atur tempat duduk dengan hati-hati.", "Bagi perhatian secara merata.", "Keluar sebentar mencari udara."])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Sebentar ya semuanya, biar nggak sempit dan gampang ambil kuahnya, Tachibana-senpai duduk di sisi kiri dekat jendela, Moemoe-senpai di sebelahnya, terus Nagisa-senpai di seberang biar dekat sama teko teh."
            nagisa "Hm, oke juga sih, jadi gampang nuang tehnya."
            miyuki "Rapi sekali susunannya, Chiasa-chan. Kamu duduk di sebelah mana?"
            nar "Kamu terlalu sadar siapa yang sengaja kamu tempatkan berdekatan dan siapa yang kamu pisahkan satu kursi. Koita mengikuti gerak matamu dengan tenang, lalu berhenti di samping bahumu sambil meletakkan sendok saji."
            koita "Semua sudah dapat posisi yang nyaman kan, Chi-chan? Kamu sendiri duduk di kursi yang enak juga lho, jangan cuma mikirin tamu sampai lupa makan."
            chiasa "Iya, Ko-nii... aku duduk sini kok."
        else:
            yutaka "Biar gampang ambil kuahnya, Tachibana-senpai sama Kohinata di sisi kiri aja ya, terus Nagisa di sebelah Chiasa biar dekat sama piring kue. Aku sama Koita di ujung sini."
            moeka "Siap, kapten pengatur kursi! Tapi Yutayuta duduknya dekat aku dong biar gampang minta tolong ambilin salad!"
            nagisa "Dasar, tinggal ulurin tangan sendiri juga nyampe, Kohinata-san."
            nar "Kamu terus mengawasi susunan kursi itu seolah satu geseran kecil bisa menjaga suasana tetap aman. Koita melirikmu pelan sambil meletakkan mangkuk terakhir di dekat tempatmu."
            koita "Sudah pas semua posisinya, Yutaka? Semua orang kelihatan nyaman nggak menurutmu?"
            yutaka "Iya, sudah aman semua kok, Koita. Ayo kita mulai makan."
        nar "Pertanyaan sederhana Koita barusan membuatmu terdiam sejenak. Kamu baru sadar betapa tegangnya kamu memperlakukan meja makan malam Natal itu seperti papan strategi yang harus dikendalikan agar perasaan semua orang tetap rapi."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Duduk di mana aja yang paling nyaman ya semuanya! Nggak usah sungkan ambil lauknya. Oh iya, Moemoe-senpai, gimana acara kampus minggu kemarin? Terus Tachibana-senpai, jadwal ujian akhir semester sudah mulai padat ya?"
            moeka "Seru banget, Chimian! Tunggu, aku cerita sambil makan ayam panggangnya ya!"
            miyuki "Lumayan padat, Chiasa-chan, tapi malam ini rasanya lega sekali bisa duduk santai makan hangat bareng kalian semua."
            nagisa "Eh, kalau kuahnya kurang hangat bilang ya, tadi aku sama Chiasa sengaja sisain sedikit di kompor."
            koita "Nah, kalau begini kan enak, semua ikut ngobrol bareng! Ayo, jangan sampai dingin supnya."
        else:
            yutaka "Bebas aja duduk di mana yang paling enak, nggak usah formal-formal. Gimana minggu ini, Tachibana-senpai? Kohinata juga katanya habis lembur beres-beres kostum?"
            miyuki "Syukurlah minggu ini agak longgar sedikit, Yutaka-kun. Terima kasih sudah menanyakan."
            moeka "Iya nih! Akhirnya malam Natal bisa istirahat makan enak tanpa mikirin jahitan baju!"
            nagisa "Eh, Yutaka, ambilin saus yang di depanmu dong. Chiasa juga mau sekalian nggak?"
            chiasa "Boleh, Nagisa-senpai, makasih!"
            koita "Wah, akhirnya suasana meja makannya hidup banget! Sini kuambilkan tambahannya dari dapur."
        nar "Kamu menyimak cerita setiap orang dengan utuh tanpa menyelipkan bisikan istimewa yang membedakan satu tamu dari tamu lainnya. Masih ada beberapa percakapan kecil yang terlewat dan sisa cemburu tipis di sudut pandang, tetapi malam ini tidak seorang pun dibiarkan merasa hanya menjadi penonton."
        if kk_bulan >= 21:
            nar "Yoshie ikut tersenyum dari dekat dapur sambil menambahkan potongan roti hangat ke tengah meja ketika tawa para tamu akhirnya mengalir lepas tanpa lagi terlalu sering melirik reaksimu."
        else:
            nar "Koita tersenyum lega sambil menambahkan piring kue hangat ke tengah meja ketika tawa para tamu akhirnya mengalir lepas tanpa lagi terlalu sering melirik reaksimu."
    else:
        if kk_host == "chiasa":
            chiasa "Kalian makan dulu aja ya, aku ke teras sebentar mau cek kotak surat sama cari angin, di dalam agak gerah dekat kompor."
            koita "Jangan lama-lama ya, Chi-chan, dingin di luar. Nanti supmu keburu dingin."
        else:
            yutaka "Aku keluar teras sebentar cari udara dingin ya, habis bantu angkat panci tadi gerah juga. Kalian lanjut dulu aja."
            koita "Oke, jangan kelamaan, nanti kuenya habis disikat Moeka-chan lho."
        nar "Kamu melangkah ke teras depan yang disapu angin dingin Desember. Dari balik jendela kaca yang berembun tipis, suara tawa dari ruang makan terdengar jauh lebih ringan dan lepas daripada yang kamu rasakan saat duduk tegang di tengah meja tadi."
        nar "Lima menit kemudian, saat kamu kembali membuka pintu, Miyuki dan Moeka sedang tertawa membicarakan resep kue sementara Nagisa dan Koita saling menimpali cerita lama dengan santai."
        moeka "Eh, sudah balik! Sini, duduk lagi, tadi kita lagi bahas resep kue coklatnya Miyumiyu-senpai!"
        koita "Sudah mendingan udaranya? Ayo, piringmu sudah kusiapkan di sebelah sini."
        nar "Melihat kehangatan yang tetap mengalir di meja itu membuatmu mengerti satu hal penting. Hubungan di antara orang-orang ini tetap bergerak dan bernapas dengan sendirinya bahkan ketika kamu sedang tidak berdiri di tengahnya."
    return

# ┌─ PANDUAN CERITA · X-D06 · Wawancara Meisa
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Lintas-tokoh
# │ AWALAN  : Meisa menulis tentang pemain
# │ INTI    : A Hentikan Meisa / B biarkan / C bayar Meisa
# │ AKHIRAN : jawaban tiap heroine mengikuti keadaannya; reputasi
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_X_D06:
    call kk_scene_enter("koita", "Kampus · Wawancara Meisa")
    "Meisa" "Aku sedang menulis tentang cara orang-orang di kampus mengenalmu. Aku akan meminta persetujuan mereka untuk bagian pribadi. Kau boleh memberi komentar, tapi aku tidak akan menjadikan jawabanmu satu-satunya versi."
    call kk_family_menu("X-D06", ["Hentikan Meisa.", "Biarkan ia menulis.", "Bayar Meisa agar menyetir ceritanya."])
    if _return == "A":
        nar "Kau menuntut Meisa menghentikan tulisan itu. Ia menutup buku catatan setelah perdebatan yang tidak lagi terdengar seperti permintaan menjaga privasi. Tulisan itu belum terbit, tetapi caramu menekan pembicaraan menjadi sesuatu yang kini ia ketahui sendiri, tanpa perlu mewawancarai orang lain."
    elif _return == "B":
        nar "Kau membiarkan Meisa menulis dan menjawab pertanyaan yang bersedia kaubahas. Ia tidak berjanji hasilnya akan menyenangkanmu. Untuk pertama kalinya, kisah tentang dirimu akan memuat suara orang yang tidak dapat kaatur urutannya atau kaupotong ketika mulai membuatmu tidak nyaman."
    else:
        nar "Kau membayar agar tulisan itu menguntungkanmu. Begitu transaksi selesai, keramahan percakapan berubah menjadi kesepakatan yang kelak bisa dipersoalkan. Pembaca mungkin belum tahu, tetapi kau dan Meisa tahu ada bagian kisah yang dibentuk demi orang yang sanggup membelinya."
    return

# ┌─ PANDUAN CERITA · X-D07 · Rapat Rahasia Koita
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Lintas-tokoh
# │ AWALAN  : koita_sadar ≥ 75
# │ INTI    : A Hadir tanpa diundang / B kirim orang / C biarkan
# │ AKHIRAN : manuver balik terbesar; E-KO-10 menguat
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_X_D07:
    call kk_scene_enter("koita", "Ruang klub · Rapat rahasia")
    nar "Koita meminta beberapa orang dekatnya bertemu di ruang klub. Kau mendengar rencana itu dari percakapan yang terputus ketika kau datang. Ia tidak sedang menyiapkan kejutan. Untuk pertama kalinya, orang-orang yang selama ini kaudekati hendak membicarakan apa yang mereka alami tanpa menunggu izinmu."
    koita "Aku tidak mau menuduh sebelum mendengar kalian. Tapi ada hal yang berbeda dari cerita yang disampaikan kepadaku. Kita boleh saling membandingkan apa yang kita tahu. Kita tidak harus terus menjawab sendirian."
    call kk_family_menu("X-D07", ["Hadir tanpa diundang.", "Kirim orang untuk mewakilimu.", "Biarkan rapat itu berjalan."])
    if _return == "A":
        nar "Kau masuk sebelum mereka siap menerima kehadiranmu. Beberapa orang langsung terdiam; Koita kehilangan keberanian yang baru dikumpulkannya. Kau berhasil mengubah jalannya pertemuan hari itu. Melihat ia mencoba menjelaskan bahwa ia tidak bermaksud jahat membuat keberhasilan itu terasa lebih buruk daripada yang kauperkirakan."
    elif _return == "B":
        nar "Kau meminta orang yang kaupercaya menyampaikan versimu. Koita mendengarnya, lalu menanyakan mengapa kau tidak mau menjawab sendiri. Pertemuan tidak selesai dengan kesimpulan yang mudah. Orang yang kautunjuk pulang membawa pertanyaan yang tidak bisa kauserahkan kepadanya untuk dijawab."
    else:
        nar "Kau membiarkan mereka berbicara. Dari luar, sulit menerima bahwa mereka berhak membahas pengalaman masing-masing tanpa memberimu kesempatan menyela. Ketika pertemuan selesai, beberapa hubungan di dalamnya menjadi lebih kuat. Koita tidak lagi harus menanggung keraguannya seorang diri."
    return

# ┌─ PANDUAN CERITA · X-D08 · Ryena dan Yuina Bertukar Cerita
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Lintas-tokoh
# │ AWALAN  : rina_curiga dan sena_curiga ≥ 50
# │ INTI    : A Temui mereka / B hindari / C jujur
# │ AKHIRAN : kecurigaan gabungan; dua lingkaran sosial sekaligus
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_X_D08:
    call kk_scene_enter("moeka", "Kafe · Dua sahabat bertukar cerita")
    nar "Ryena dan Yuina bertemu di kafe dan menemukan bahwa beberapa cerita yang mereka dengar tentangmu tidak cocok. Keduanya tidak saling mengenal cukup lama untuk langsung percaya. Justru karena itu, pertanyaan mereka menjadi hati-hati dan semakin sulit diabaikan sebagai kecemburuan seorang teman."
    "Ryena" "Jadi ada bagian yang berbeda dari yang diceritakan kepadaku. Aku tidak mau menyimpulkan sendiri. Tapi kalau teman kita terus yang menanggung akibat, kita harus bertanya."
    call kk_family_menu("X-D08", ["Temui mereka langsung.", "Hindari keduanya.", "Jujur sepenuhnya."])
    if _return == "A":
        nar "Kau duduk di hadapan keduanya dan mendengarkan sebelum menjawab. Ryena membahas yang terjadi pada temannya, Yuina menanyakan perkataanmu yang tidak cocok. Menjawab langsung meredakan sebagian dugaan, tetapi kau tidak dapat meminta mereka melupakan hak teman-temannya untuk mengetahui hal yang sama."
    elif _return == "B":
        nar "Kau menghindari keduanya. Mereka tidak mendapatkan penjelasan darimu, lalu berusaha memeriksa cerita yang sudah ada. Ketiadaan jawaban bukan bukti untuk setiap dugaan, tetapi cukup membuat mereka berhenti memberimu kepercayaan hanya karena selama ini kau terdengar meyakinkan."
    else:
        nar "Kau mengakui bagian yang selama ini kausampaikan berbeda kepada orang berbeda. Ryena marah, Yuina meminta kau tidak menyebut pengakuan itu sebagai hadiah. Mereka akan menyampaikan kebenaran kepada orang yang perlu tahu. Kau kehilangan kendali atas cerita, sekaligus berhenti menambah kebohongan pada hari ini."
    return

# ┌─ PANDUAN CERITA · X-D09 · Dua Penjaga
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Lintas-tokoh
# │ AWALAN  : haruto_curiga ≥ 50; Kuroiwa curiga
# │ INTI    : (node keputusan / penutup — tak ada menu)
# │ AKHIRAN : peringatan dari dua sisi; bila ada Force, E-FO-06 lebih mungkin
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_X_D09:
    call kk_scene_enter("koita", "Kabar yang datang terlambat")
    nar "Haruto menemui Kuroiwa setelah beberapa kekhawatiran yang semula dianggap terpisah mulai menunjuk orang yang sama. Mereka berbicara tanpa orang yang sedang mereka lindungi berada di ruangan. Tujuannya bukan mengambil keputusan atas nama orang itu, melainkan memastikan tidak ada ancaman yang dihadapi sendirian."
    "Kuroiwa" "Ada hal yang perlu kita pastikan. Jangan jadikan dugaan sebagai kepastian, dan jangan membuat mereka takut bicara karena merasa akan langsung dibawa ke pertengkaran kita."
    nar "Haruto mengatakan ia akan mendengar lebih dulu sebelum menuntut jawaban. Kuroiwa mengangguk, tetapi tegas bahwa ancaman yang nyata tidak akan mereka biarkan berlalu. Ketika kau mengetahui pertemuan itu, orang-orang yang selama ini terpisah sudah mulai saling menghubungi. Kau tidak lagi bisa menganggap setiap kekhawatiran sebagai masalah yang hanya hidup di satu rumah."
    $ kk_record_choice("X-D09", "A")
    return

# ┌─ PANDUAN CERITA · X-D10 · Malam Dua Krisis
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Lintas-tokoh
# │ AWALAN  : Mo25 dan N23 jatuh di malam yang sama
# │ INTI    : A Datang ke Moeka / B ke Nagisa / C kirim orang ke salah satunya
# │ AKHIRAN : ujian terberat untuk "kirim orang lain" dan mode ponsel
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_X_D10:
    call kk_scene_enter("moeka", "Malam dua krisis")
    nar "Dua pesan meminta pertolongan pada malam yang sama. Moeka terdengar hampir tidak sanggup meneruskan percakapan; Nagisa mengatakan ia tidak tahu apa yang akan dilakukannya jika terus sendirian. Kau membaca keduanya dengan tangan dingin. Mereka bukan dua ujian cinta yang harus dimenangkan. Keduanya manusia yang sedang membutuhkan orang lain hadir."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABC", KK_DYN_BY_ID["X-D10"]["choices"])]
    call screen kk_choice_panel(_rows, "Hanya satu tempat")
    $ kk_record_choice("X-D10", _return)
    if _return == "A":
        nar "Kau menuju Moeka dan tetap memberitahunya bahwa kau sedang datang. Di tempat lain, Nagisa belum mendapat kehadiran yang ia minta darimu. Perjalanan itu dipenuhi kekhawatiran, tanpa kepastian yang bisa mengubah satu keputusan menjadi jawaban untuk dua krisis sekaligus."
    elif _return == "B":
        nar "Kau menuju Nagisa. Ketika mendengar suaramu lagi, ia meminta kau tidak berhenti mengabarinya sebelum tiba. Di tempat lain, Moeka masih menghadapi malamnya. Kau tidak mendapat kemenangan dari memilih; hanya tanggung jawab melakukan pertolongan yang benar-benar sanggup kauberikan."
    else:
        nar "Kau meminta orang tepercaya datang ke salah satu tempat dan pergi ke yang lain. Mengakui keterbatasanmu terasa menakutkan, tetapi jauh lebih berguna daripada menjanjikan bisa hadir di dua tempat. Kau menunggu kepastian orang itu sudah tiba, memahami bahwa bantuan tidak harus memakai wajahmu untuk berarti bagi yang menerimanya."
    return

# ┌─ PANDUAN CERITA · X-D11 · Grup Belajar SMA Hidup Lagi
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Lintas-tokoh
# │ AWALAN  : Koita membuka grup chat lama
# │ INTI    : A Ikut / B diam / C keluar grup
# │ AKHIRAN : rahasia lama terangkat; benih E-NA-09 dan E-X-11
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_X_D11:
    call kk_scene_enter("koita", "Grup chat SMA hidup lagi")
    nar "Pemberitahuan grup lama muncul setelah Koita mengirim foto masa sekolah. Nama-nama yang jarang terlihat berdekatan mulai membalas. Candaan tentang tugas dan guru membawa percakapan ke orang yang dahulu sering menunggu seusai kelas. Kau membaca sambil mengingat bahwa masa lalu ini milik mereka, bukan sesuatu yang bisa kauisi sembarang."
    koita "Aku menemukan foto ini waktu beres-beres. Kalian masih punya yang lain? ...Dulu rasanya ada banyak hal yang tidak pernah kita tanyakan karena mengira besok masih bisa."
    call kk_family_menu("X-D11", ["Ikut mengobrol.", "Diam membaca saja.", "Keluar dari grup."])
    if _return == "A":
        nar "Kau ikut mengobrol dan membiarkan orang lain melengkapi kenangan yang tidak kauketahui. Ada tawa, ada koreksi kecil, ada nama yang membuat percakapan mendadak melambat. Keakraban mereka tidak terdiri hanya dari kisah manis. Beberapa hal yang belum selesai mulai mendapat kalimat pertamanya."
    elif _return == "B":
        nar "Kau membaca tanpa ikut membalas. Orang-orang berbagi cerita yang dianggap sudah diketahui semua anggota, dan setiap pesan memberimu gambaran lebih utuh tentang hubungan mereka. Pengetahuan itu bisa membuatmu lebih berhati-hati, atau hanya lebih pandai berpura-pura pernah ada di sana."
    else:
        nar "Kau keluar dari grup. Pemberitahuan singkat mengumumkan kepergianmu di tengah percakapan yang masih hangat. Koita mengirim pesan pribadi menanyakan apakah ada yang salah. Kau kini harus menjawab seorang teman, bukan sekadar menekan tombol untuk mengakhiri suara yang membuatmu tidak nyaman."
    return

# ┌─ PANDUAN CERITA · X-D12 · Salah Kirim
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Lintas-tokoh
# │ AWALAN  : pemain Sangat Lelah; sedang chat dengan dua orang
# │ INTI    : A Tarik pesan (notifikasi sudah terbaca) / B jelaskan / C pura-pura disengaja
# │ AKHIRAN : rahasia bocor; contoh kondisi tubuh yang melahirkan cabang baru
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_X_D12:
    call kk_scene_enter("koita", "Salah kirim")
    nar "Kau membaca dua percakapan dengan mata pedih dan pikiran yang terlambat mengikuti jari. Satu kalimat tentang janji pribadi terkirim ke orang yang salah. Ketika menyadarinya, tanda telah dibaca sudah muncul. Orang di seberang tidak langsung membalas, dan jeda itu terasa lebih keras daripada pertengkaran."
    call kk_family_menu("X-D12", ["Tarik pesan (sudah terbaca).", "Jelaskan dengan jujur.", "Pura-pura memang disengaja."])
    if _return == "A":
        nar "Kau menarik pesan yang sudah dibaca. Pertanyaan datang tidak lama kemudian: untuk siapa sebenarnya kalimat itu? Layar kosong di tempat pesan tadi tidak menghapus apa yang sudah dipahami. Kau harus menghadapi percakapan yang sempat ingin kaubuat hilang."
    elif _return == "B":
        nar "Kau mengakui salah kirim dan menjelaskan konteks yang selama ini tidak disampaikan. Jawaban itu membuat orang di seberang terluka, tetapi memberinya sesuatu yang jelas untuk diputuskan. Kau tidak meminta ia segera tenang hanya supaya malam yang sudah melelahkan ini lekas selesai."
    else:
        nar "Kau mengatakan pesan itu memang untuknya. Kebohongan itu menuntut jawaban baru ketika ia menanyakan bagian yang tidak masuk akal. Kau mengetik lebih lama, semakin lelah, semakin jauh dari percakapan awal. Tubuhmu tidak sanggup menjadi tempat aman untuk seluruh cerita yang kaupaksa terus berjalan."
    return

init 1 python:
    _hook("X-D01-A", lambda: (kk_rel("nagisa","trust",3), kk_rel("moeka","trust",3)))
    _hook("X-D01-B", lambda: (kk_rel("moeka","aff",4), kk_rel("nagisa","jeal",6)))
    _hook("X-D01-C", lambda: (kk_rel("nagisa","aff",4), kk_adj("stres_moeka",8)))
    _hook("X-D01-D", lambda: (kk_adj("stres_moeka",10), kk_adj("rina_curiga",8)))
    _hook("X-D02-A", lambda: (kk_flag("moeka_intervensi_1"), kk_flag("miyuki_lihat_moeka"), kk_rel("miyuki","aff",3)))
    _hook("X-D02-B", lambda: (kk_flag("miyuki_lihat_moeka"), kk_rel("miyuki","trust",3)))
    _hook("X-D02-C", lambda: kk_rel("miyuki","trust",-4))
    _hook("X-D03-A", lambda: (kk_flag("ogawa_dihentikan"), kk_flag("shiori_sekutu_musuh"), kk_adj("bukti_ogawa",15)))
    _hook("X-D03-B", lambda: None)
    _hook("X-D03-C", lambda: (kk_rel("shiori","trust",-4), kk_rel("harumi","trust",-4)))
    _hook("X-D04-A", lambda: kk_flag("valentine_jujur"))
    _hook("X-D04-B", lambda: (kk_flag("valentine_rahasia"), kk_adj("rahasia_pemain",5)))
    _hook("X-D04-C", lambda: kk_flag("valentine_kabur"))
    _hook("X-D05-A", lambda: (kk_flag("natal_panggung_pengakuan"), kk_koita_aware(4)))
    _hook("X-D05-B", lambda: None)
    _hook("X-D05-C", lambda: None)
    _hook("X-D06-A", lambda: (kk_flag("mei_dihentikan"), kk_adj("rahasia_pemain",5)))
    _hook("X-D06-B", lambda: kk_flag("mei_menulis_bebas"))
    _hook("X-D06-C", lambda: (kk_flag("mei_dibayar"), kk_flag("kebohongan_baru")))
    _hook("X-D07-A", lambda: (kk_flag("koita_rapat_dibalik"), kk_koita_collapse(10)))
    _hook("X-D07-B", lambda: kk_koita_aware(5))
    _hook("X-D07-C", lambda: (kk_koita_aware(10), kk_flag("koita_rapat_berjalan")))
    _hook("X-D08-A", lambda: (kk_adj("rina_curiga",-6), kk_adj("sena_curiga",-6)))
    _hook("X-D08-B", lambda: (kk_adj("rina_curiga",10), kk_adj("sena_curiga",10)))
    _hook("X-D08-C", lambda: kk_flag("pemain_jujur_sahabat"))
    _hook("X-D09-A", lambda: (kk_adj("haruto_curiga",8), kk_adj("kuroiwa_percaya",-5)))
    _hook("X-D10-A", lambda: (kk_flag("moeka_intervensi_1"), kk_rel("moeka","intim",5)))
    _hook("X-D10-B", lambda: (kk_flag("nagisa_dipilih_krisis"), kk_rel("nagisa","intim",5)))
    _hook("X-D10-C", lambda: kk_flag("kirim_orang_krisis"))
    _hook("X-D11-A", lambda: (kk_flag("grup_sma_hidup"), kk_rel("nagisa","aff",3)))
    _hook("X-D11-B", lambda: kk_flag("grup_sma_disimak"))
    _hook("X-D11-C", lambda: kk_flag("grup_sma_ditinggalkan"))
    _hook("X-D12-A", lambda: kk_adj("rahasia_pemain",6))
    _hook("X-D12-B", lambda: kk_rel("koita","trust",3))
    _hook("X-D12-C", lambda: (kk_flag("kebohongan_baru"), kk_adj("rahasia_pemain",8)))
