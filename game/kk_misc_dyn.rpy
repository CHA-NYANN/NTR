# Event dinamis lepas: Mi-D13 (Miyuki, pertanyaan pada dirinya sendiri) dan
# N-D04 (Nagisa, tawaran kedua Yuuto saat pemain absen). Konsekuensi + karakter.

# ┌─ PANDUAN CERITA · Mi-D13 · Pertanyaan yang Belum Pernah Ia Tanyakan
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Tachibana Miyuki
# │ AWALAN  : Chiasa host; Intim ≥ 55
# │ INTI    : A Beri waktu / B desak / C bercanda
# │ AKHIRAN : Aff, Intim; desakan menurunkan Trust
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi_D13:
    call kk_scene_enter("miyuki", "Kafe Komorebi · Pertanyaan yang belum pernah ia tanyakan")
    nar "Miyuki memutar cangkir sebelum bertanya apakah Chiasa sedang ingin mendengar sesuatu yang belum ia pahami. Ia tidak membuka pembicaraan dengan lelucon, dan itu membuat kegugupannya terlihat."
    miyuki "Belakangan aku memikirkan apakah aku bisa menyukai perempuan. Mungkin ini tentang seseorang. Mungkin juga tentang hal yang selama ini nggak pernah kuizinkan kupikirkan."
    nar "Ia menatapmu, lalu mengalihkan mata, cukup terlambat untuk menyembunyikan mengapa pertanyaan itu disampaikan kepadamu."
    call kk_family_menu("Mi-D13", ["Beri ia waktu untuk mencari jawabannya sendiri.", "Desak ia menjawab sekarang.", "Cairkan dengan bercanda."])
    if _return == "A":
        nar "Kau memberinya waktu tanpa menganggap ketidakpastian sebagai penolakan atau janji. Miyuki mengendurkan bahu."
        miyuki "Aku ingin memahami pelan-pelan. Kalau suatu hari aku punya jawaban, aku ingin mengatakannya karena itu benar, bukan karena takut kamu sudah menunggu terlalu lama."
        nar "Kalian melanjutkan minum. Kedekatan itu kini menampung satu pertanyaan baru tanpa harus segera menyelesaikannya."
    elif _return == "B":
        nar "Kau mendesaknya menentukan apa arti pembicaraan ini bagi kalian. Miyuki menjauhkan cangkir, mengatur napas sebelum menjawab."
        miyuki "Aku belum tahu. Aku cerita karena percaya boleh belum tahu di dekatmu."
        nar "Sesudah itu ia memilih kata lebih hati-hati. Pertanyaan yang baru saja berani dibuka kembali terasa seperti pintu yang harus dijaga agar orang lain tidak masuk terlalu jauh."
    else:
        nar "Kau bercanda bahwa senpai sedang mengajukan soal yang tidak ada di buku ujian. Miyuki tertawa pendek, lega sekaligus berusaha membaca apakah kau menertawakannya."
        miyuki "Kalau ada jawabannya di buku, aku pasti sudah hafal sebelum berani bertanya."
        nar "Ia tersenyum lagi, kali ini lebih lepas. Pertanyaannya belum dijawab, tetapi rasa malu tidak lagi memenuhi seluruh meja."
    return

# ┌─ PANDUAN CERITA · N-D04 · Tawaran Kedua Yuuto
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Sakurajima Nagisa
# │ AWALAN  : tenggat studio; pemain absen
# │ INTI    : A Datang membantu / B biarkan / C alihkan Yuuto
# │ AKHIRAN : studio +; kelekatan ke pemain turun bila pemain absen
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N_D04:
    call kk_scene_enter("nagisa", "Gedung Arsitektur · Tenggat maket")
    nar "Foto maket yang belum selesai masuk ke ponselmu bersama kabar bahwa Yuuto sudah berada di studio. Tenggat tinggal semalam. Nagisa tidak sempat mempertahankan gengsi sekaligus menyelesaikan seluruh pekerjaan."
    nagisa "Dia bisa bantu. Aku bukan melapor untuk membuatmu cemburu. Aku perlu tahu kamu datang atau nggak supaya bisa membagi kerjaan."
    nar "Kalimat berikutnya lebih pendek: aku tadi berharap kamu yang ada di sini."
    call kk_family_menu("N-D04", ["Datang membantu sendiri.", "Biarkan Yuuto yang membantu.", "Alihkan Yuuto dengan halus."])
    if _return == "A":
        nar "Kau datang dan meminta tugas tanpa menyuruh Yuuto pergi. Nagisa memeriksa jam, lalu mengangguk, lebih lega daripada yang ingin ditunjukkan."
        nagisa "Baik. Yang itu untukmu. Terima kasih sudah datang. Omelannya nanti kalau sudah selesai."
        nar "Kalian bekerja dengan pembagian yang akhirnya jelas. Kehadiranmu tidak menghapus waktu ketika kau absen, tetapi memberi sesuatu yang nyata untuk dinilai selain janji akan menyusul."
    elif _return == "B":
        nar "Kau mengatakan tidak akan datang. Nagisa membalas singkat, kemudian berhenti memeriksa layar agar bisa bekerja bersama Yuuto."
        nar "Maket selesai menjelang pagi. Ia mengucapkan terima kasih kepada orang yang benar-benar melihat bagian mana yang paling melelahkan malam itu. Kedekatan tumbuh di sela bantuan yang tidak perlu ditagih, sementara tempatmu dalam harapannya sedikit bergeser."
    else:
        nar "Kau mengalihkan Yuuto dari malam yang semula hendak diberikannya. Ia menanyakan apakah ada orang lain yang akan membantu sebelum bersedia pergi."
        "Yuuto" "Baik, kalau sudah diatur. Tolong jangan sampai Nagisa harus mengulang sendirian."
        nar "Nagisa melihat orang yang baru bersedia menolong kembali membereskan tas. Kau telah mengubah siapa yang boleh hadir di dekatnya; pekerjaan yang masih menumpuk tetap memerlukan tangan, bukan sekadar alasan."
    return

init 1 python:
    _hook("Mi-D13-A", lambda: (kk_rel("miyuki","aff",6), kk_rel("miyuki","intim",5), kk_flag("miyuki_bertanya_diri")))
    _hook("Mi-D13-B", lambda: (kk_rel("miyuki","trust",-5), kk_rel("miyuki","intim",3)))
    _hook("Mi-D13-C", lambda: kk_rel("miyuki","aff",3))
    _hook("N-D04-A", lambda: (kk_rel("nagisa","aff",5), kk_adj("kelekatan_nagisa",6)))
    _hook("N-D04-B", lambda: (kk_adj("kelekatan_nagisa",-10), kk_flag("yuuto_mendekat")))
    _hook("N-D04-C", lambda: (kk_adj("kelekatan_nagisa",3), kk_flag("yuuto_dialihkan")))
