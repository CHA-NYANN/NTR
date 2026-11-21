# Bagian 12 — `Y03` (*"Yuu-kun?"*) · Host Yutaka (M01a)

Target File: `game/kk_yutaka_route.rpy` (`label kkscene_Y03`)

```renpy
label kkscene_Y03:
    call kk_scene_enter("yutaka", "Apartemen Yutaka · Julukan lama")
    nar "Sore hari di apartemen mewah milik keluarga Kisaragi itu biasanya terlalu sunyi, tetapi kehadiran Sakurajima Nagisa yang mampir seusai kelas langsung membuat ruang tamu terasa jauh lebih hidup."
    nar "Kau baru saja keluar dari dapur membawa dua gelas teh dingin ketika melihat gadis bertubuh mungil berambut pirang keemasan twin-tail itu berdiri di dekat rak televisi. Alih-alih langsung duduk di sofa, perhatiannya tertahan pada bingkai foto lama empat sekawan di festival musim panas yang terpajang di sana."
    nar "Untuk beberapa detik, raut galak dan kompetitif yang biasa ia pasang di kampus menghilang sepenuhnya. Ia memandangi foto masa kecil itu dengan senyum tipis yang lembut—lalu, seolah terseret kenangan lama tanpa sadar, ia menoleh ke arahmu begitu mendengar bunyi gelas diletakkan di atas meja kaca."
    nagisa "Yuu-kun! ...Eh—"
    nar "Begitu julukan masa kecil itu keceplosan meluncur dari bibirnya, Nagisa sendiri langsung tersentak. Rona merah tipis naik ke ujung telinganya; ia buru-buru berdeham kecil sambil menyentuh bingkai foto di rak dengan jari telunjuknya, lalu tertawa canggung."
    nagisa "...Aneh banget, ya, sekarang keceplosan memanggil begitu lagi. Padahal waktu SD dulu, setiap kali aku teriak 'Yuu-kun!' dari ujung gang, kau selalu yang paling pertama menoleh sebelum Koita sempat sadar. Kau masih ingat kan waktu kita hampir ketinggalan kembang api gara-gara nungguin Chiasa beli permen apel?"
    nar "Mata biru cerah Nagisa menoleh lurus menatapmu, menunggu sahutan. Di dalam kepala, kau tahu persis bahwa tidak ada satu pun ingatan masa kecil Yutaka yang ikut diwariskan kepadamu—yang kaumiliki hanyalah foto di rak itu dan serpihan informasi umum dari manga."
    call kk_family_menu("Y03", ["Jawab natural seolah memang ingat.", "Salah menyebut kenangannya.", "Pura-pura lupa sambil tersenyum."])
    if _return == "A":
        nar "Kau tidak membiarkan raut wajahmu membeku sedetik pun. Kau bersandar santai di pinggir sofa sambil menyilangkan tangan, lalu menarik sudut bibirmu menjadi senyum tipis yang terasa paling cocok dengan pembawaan santai pemilik tubuh ini."
        yutaka "Mana mungkin lupa. Kalau aku nggak langsung menoleh waktu kau teriak dulu, nanti kau bakal makin keras teriaknya sampai satu gang keluar semua. Lagipula kalau nggak salah, waktu itu kau sendiri yang paling heboh berebut tempat duduk di dekat tangga kuil, kan?"
        nar "Kau sengaja memilih detail yang paling sesuai dengan sifat keras kepala Nagisa—cukup masuk akal tanpa harus menebak hal spesifik yang berisiko meleset."
        nar "Nagisa mengerjap sesaat, lalu tawa ringan yang tulus langsung pecah dari bibirnya. Wajahnya tampak jauh lebih rileks."
        nagisa "Hei, itu kan supaya kita semua dapat pemandangan kembang api paling jelas! ...Masih ingat rupanya."
        nar "Ia menunduk kembali memandangi bingkai foto di tangannya dengan tatapan hangat, lalu meletakkannya kembali dengan rapi di atas rak televisi."
        nagisa "Jujur saja, aku sendiri juga tidak ingat semuanya dengan tepat. Yang paling kuingat cuma rasanya dulu—kita selalu merasa besok masih bisa main bareng lagi tanpa perlu mikir macam-macam."
        nar "Ia berjalan menghampiri sofa, mengambil salah satu gelas teh dingin dari meja kaca, lalu menatapmu sebentar dengan sorot mata yang tenang."
        nagisa "...Baguslah kalau sekarang pun kau masih mau menoleh, Yutaka."
        nar "Di matanya, tidak ada sedikit pun keraguan tersisa. Kau mengangguk pelan sambil meneguk tehmu, menyadari betapa mudahnya satu jawaban tepat menenangkan kecurigaan sahabat masa kecilnya."
    elif _return == "B":
        nar "Merasa harus membuktikan bahwa kau benar-benar mengingat masa kecil mereka agar tidak dicurigai, kau nekat merangkai satu detail berdasarkan foto festival di rak televisi."
        yutaka "Tentu saja ingat. Waktu itu kan gara-gara kau sempat tersesat di dekat stan ikan mas sampai Koita harus meminjamkan sandalnya dan kita semua baru ketemu lagi di depan gerbang taman kota, kan?"
        nar "Nagisa sempat mengeluarkan tawa pendek karena mengira kau sedang sengaja mengarang lelucon untuk menggodanya."
        nagisa "Haha, apaan sih, ngawur banget—tunggu dulu... kau nggak lagi bercanda ya?"
        nar "Tawa Nagisa langsung terhenti di tenggorokan begitu ia melihat raut wajahmu yang tetap serius menunggu ia mengiyakan. Alisnya perlahan berkerut dalam."
        nagisa "Yutaka... yang waktu itu tersesat di festival memang aku, tapi yang menemukan dan menenangkanku kan Chiasa—dan itu di dekat kuil sebelah timur, bukan di gerbang taman kota. Mana pernah juga Koita meminjamkan sandalnya."
        nar "Suara Nagisa melambat dan turun, nada santainya lenyap sepenuhnya. Ia meletakkan kembali bingkai foto itu ke rak televisi dengan gerakan kaku, lalu menoleh menatapmu lebih lama seolah berusaha memahami bagaimana sahabat sejak TK-nya bisa meleset sejauh itu."
        yutaka "Ah... maaf. Kayaknya kepalaku mencampuradukkan dua festival yang berbeda."
        nagisa "...Mungkin. Tapi biasanya kau paling hafal hal-hal begini, bahkan hal yang aku sendiri sudah lupa."
        nar "Ia duduk di ujung sofa dan mulai menceritakan ulang kejadian sebenarnya dengan nada pelan. Kau hanya bisa mengangguk mengikuti alurnya sambil menyadari satu kenyataan pahit: masa lalu mereka yang bertahun-tahun tidak bisa dipelajari atau ditebak seperti soal ujian."
    else:
        nar "Daripada nekat mengarang detail masa lalu dan berakhir salah sebut, kau memilih bersandar santai di sofa, mengangkat bahu ringan, lalu tersenyum tipis mengejek diri sendiri."
        yutaka "Wah, jujur saja, bagian yang itu sudah agak kabur di kepalaku. Sudah bertahun-tahun lalu juga kan, Nagisa—akhir-akhir ini kepalaku keburu penuh sama materi Ekonomi."
        nar "Nagisa langsung memutar badannya menghadapmu dengan mata biru membulat dan bibir mengerucut tidak percaya."
        nagisa "Hah?! Lupa?! Serius kau bisa lupa?! Padahal biasanya kau yang paling berisik mengungkit kejadian waktu SD cuma buat ngeledek aku kalau kita lagi kumpul!"
        nar "Ia menatapmu beberapa detik dengan sorot curiga tipis yang bercampur kesal, lalu menghela napas panjang dan menjatuhkan diri duduk di sofa sambil memeluk salah satu bantal."
        nagisa "...Ya sudah, kalau memang lupa nanti kuceritakan lagi pelan-pelan. Tapi dengar ya, Yutaka—jangan pernah cuma mengangguk-angguk pura-pura paham kalau sebenarnya kau nggak ingat. Aku bisa benar-benar kesal kalau sahabat sendiri cuma iyain aku tanpa benar-benar dengar."
        yutaka "Iya, maaf. Ceritakan saja lagi nanti."
        nar "Nagisa mendengus kecil lalu meraih gelas teh dinginnya. Meski ia akhirnya kembali mengobrol tentang jadwal kuliah Arsitekturnya, sesekali matanya masih melirik ke arahmu dari balik gelas dengan kerutan samar di kening—merasa ada sesuatu pada sikapmu hari ini yang tidak sepenuhnya sama."
    return
```
