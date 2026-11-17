# Chiasa host, menjaga penyamaran (C02, C03, C04, C08). Paralel dengan rute Yutaka:
# tingkah yang meleset dari Chiasa asli menaikkan kecurigaan. Event host (fire saat masuk lokasi).
# Variabel curiga_* mengikuti Event_Chiasa; angka adalah setelan prototipe.
# ┌─ PANDUAN CERITA · C02 · "Ko-nii?"
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : sarapan bersama Koita.
# │ INTI    : A memanggil "Ko-nii" natural / B memanggil nama / C menggoda seperti Chiasa asli.
# │ AKHIRAN : B memicu curiga Koita; C menaikkan Jealousy Koita.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C02:
    call kk_scene_enter("chiasa", "Rumah Amamiya")
    nar "Koita menaruh dua piring di meja, menanyakan apakah kau mau teh seperti biasa. Kau tidak tahu seperti biasa berarti apa sebelum melihat tangannya sudah menuju cangkir yang tepat."
    nar "Di kepala, panggilan Chiasa terasa seperti dialog yang pernah dibaca. Di meja ini ia harus keluar dari mulutmu sendiri tanpa membuat seseorang sadar sedang mendengar tiruan."
    call kk_family_menu("C02", ["Panggil 'Ko-nii' dengan natural.", "Panggil namanya saja.", "Goda ia seperti Chiasa asli biasanya."])
    if _return == "A":
        koita "Pagi, Chiasa. Tumben rapi."
        nar "Panggilan itu diterima begitu mudah sampai kau justru merasa makin asing. Koita melanjutkan cerita tentang kuliah, tak tahu berapa banyak petunjuk hidup sehari-hari yang sedang kauambil dari percakapan biasa."
    elif _return == "B":
        koita "...'Koita'? Sejak kapan kau memanggilku begitu?"
        nar "Ia tertawa pendek, lalu menunggu alasan. Kau baru menyadari satu nama dapat menjadi jarak ketika seluruh hubungan dibangun dari cara seseorang menyebutnya."
    else:
        koita "Hei, jangan iseng pagi-pagi."
        nar "Kau meniru keluwesan Chiasa, menyisipkan godaan untuk menutup kegugupan. Koita malu dengan cara yang tampaknya sudah sering terjadi, tetapi menatapmu lagi ketika kau berhenti terlalu cepat."
    return

# ┌─ PANDUAN CERITA · C03 · Tanzaku Chiasa
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Tanabata; Chiasa menulis tanzaku (apa pun).
# │ INTI    : A menulis harapan baru / B menyalin harapan asli / C tidak menulis.
# │ AKHIRAN : harapan_pemain; C membuat Haruka bertanya.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C03:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Tanabata")
    nar "Tanzaku menunggu di dekat alat gambar. Kau mengetahui harapan yang biasanya ditulis Chiasa, cukup untuk menyalinnya tanpa berpikir. Justru itu yang membuat pensil tertahan."
    nar "Di luar, Koita menanyakan apakah kertasnya sudah selesai. Kau masih harus menentukan apakah satu keinginan dalam hidup pinjaman ini boleh benar-benar menjadi milikmu."
    call kk_family_menu("C03", ["Tulis harapan baru, milikmu sendiri.", "Salin harapan aslinya persis.", "Biarkan tanzaku itu kosong."])
    if _return == "A":
        nar "Kau menulis harapanmu sendiri, dengan kalimat yang tidak berusaha menyenangkan bayangan tentang siapa Chiasa seharusnya. Kertas itu terasa terlalu kecil untuk menjelaskan perbedaan, cukup luas untuk memulainya."
    elif _return == "B":
        nar "Kau menyalin harapan lama. Koita mengenalinya dan tersenyum, mengira masih melihat adiknya yang sama."
        nar "Kau mendapat keamanan dari rasa percaya itu, bersama ketidaknyamanan bahwa kelegaan seseorang baru saja dibeli dengan mengulangi keinginan yang belum tentu hidup di dalam dirimu."
    else:
        "Haruka" "Tidak menulis? Tidak biasanya kau melewatkan ini."
        nar "Kau membiarkan kosong daripada menyampaikan sesuatu yang tak dapat diakui. Haruka menawarkan pensil lain, mengira masalahnya ada pada alat. Perhatian kecilnya membuat keputusan tidak menjawab terasa lebih terlihat."
    return

# ┌─ PANDUAN CERITA · C04 · "Nacchan-oneechan"
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Nagisa di festival; Chiasa kecil biasa memanggil begitu.
# │ INTI    : A pakai julukan / B pakai nama biasa / C menantang Nagisa.
# │ AKHIRAN : A membangkitkan kenangan; B dingin; C memperkuat rivalitas.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C04:
    call kk_scene_enter("chiasa", "Rumah Amamiya · Festival")
    nar "Nagisa membetulkan tali tas di depan stan festival. Kau mengingat Chiasa kecil pernah memanggilnya Nacchan-oneechan, sebuah kedekatan yang kemudian terkubur oleh rivalitas."
    nar "Panggilan lama itu tersedia dalam pengetahuanmu. Belum jelas apakah mengucapkannya sekarang akan menjadi kebohongan tentang masa lalu atau tawaran hubungan yang baru."
    call kk_family_menu("C04", ["Pakai julukan lama itu.", "Panggil namanya biasa saja.", "Tantang Nagisa dengan sikap dingin."])
    if _return == "A":
        nagisa "...Lama tidak kudengar panggilan itu. Kau masih ingat, ya."
        nar "Ia menurunkan suara, lupa sesaat pada kebiasaan mencari celah untuk membalas. Kau melihat seseorang yang ternyata masih menunggu bagian lama kedekatan itu disebut tanpa ejekan."
    elif _return == "B":
        nagisa "Oh. Kukira kita lebih dekat dari itu."
        nar "Ia segera menambahkan bahwa nama biasa tentu boleh dipakai. Namun langkahnya lebih cepat ketika kalian mulai berjalan lagi, memberi jarak pada harapan kecil yang terlanjur terlihat."
    else:
        nagisa "Begitu caramu sekarang? Baik, aku terima."
        nar "Rivalitas memberimu peran yang mudah ditiru: sindir, balas, jangan mengalah. Di baliknya ada dua perempuan yang mulai sulit mengingat kapan terakhir kali berbicara tanpa mempertahankan tempat di dekat orang lain."
    return

# ┌─ PANDUAN CERITA · C08 · Haruka Curiga
# │ LOKASI  : Kampus Kouseikan · Gedung Seni Rupa & Studio
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : gambar sketsa pemain berubah gaya.
# │ INTI    : A kerjakan lagi dari nol / B beralasan "stres" / C mengaku sebagian.
# │ AKHIRAN : curiga_haruka; risiko rahasia Shena terbongkar.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_C08:
    call kk_scene_enter("chiasa", "Gedung Seni Rupa & Studio")
    nar "Haruka menaruh gambar lama dan sketsa barumu di dekat cahaya. Ia tidak menunjuk hasil yang buruk lebih dahulu, melainkan keputusan kecil yang dahulu dibuat Chiasa tanpa berpikir."
    "Haruka" "Bukan cuma kualitas. Caramu mencari bentuknya berbeda. Kamu sedang mencoba sesuatu, atau kesulitan yang belum ingin kamu ceritakan?"
    call kk_family_menu("C08", ["Kerjakan ulang dari nol agar cocok dengan gaya lama.", "Beralasan kau sedang stres.", "Akui sebagian bahwa kau sedang mencoba hal baru."])
    if _return == "A":
        nar "Kau mengulang dari awal, memeriksa contoh sampai sebagian garis tampak lebih dekat dengan kebiasaan lama. Haruka mengangguk, tetapi melihat kerja keras yang sebelumnya tak perlu terlihat untuk hasil serupa."
        "Haruka" "Lebih mendekati. Kamu boleh bilang jika butuh waktu. Aku tidak ingin kamu mengira harus menyembunyikan setiap kesulitan agar tetap dianggap Chiasa."
    elif _return == "B":
        "Haruka" "Stres... mungkin. Tapi garis tidak biasanya berbohong."
        nar "Ia tidak menolak alasanmu, hanya menanyakan apa yang dapat dibantu. Kebohongan pendek itu kini memerlukan jawaban yang harus cukup meyakinkan untuk kepedulian seseorang yang tidak sedang mencari kesalahan."
    else:
        "Haruka" "Hal baru, ya. Akan kuperhatikan ke mana arahnya."
        nar "Kau mengakui sebagian perubahan tanpa membuka seluruh identitasmu. Haruka memberi ruang untuk mencoba, tetapi meminta jangan menjanjikan hasil profesional sebelum kau sendiri tahu kemampuan yang ada sekarang."
    return

init 1 python:
    _hook("C02-A", lambda: kk_suspect("koita", -3))
    _hook("C02-B", lambda: kk_suspect("koita", 8))
    _hook("C02-C", lambda: kk_rel("koita","jeal",5))
    _hook("C03-A", lambda: kk_flag("harapan_pemain_baru"))
    _hook("C03-C", lambda: kk_suspect("haruka", 5))
    _hook("C04-A", lambda: kk_rel("nagisa","intim",3))
    _hook("C04-B", lambda: kk_rel("nagisa","trust",-3))
    _hook("C04-C", lambda: kk_rel("nagisa","jeal",4))
    _hook("C08-A", lambda: kk_suspect("haruka", -3))
    _hook("C08-B", lambda: kk_suspect("haruka", 6))
    _hook("C08-C", lambda: (kk_suspect("haruka", 3), kk_flag("shena_hampir_terbongkar")))
