# Draft editorial. Milestone_3_Tahun M01b/M02 dan Event_Moeka, Event_Shiori,
# Event_Nagisa, Event_Miyuki. Adegan memakai urutan pilihan dari katalog.
# ┌─ PANDUAN CERITA · Mo01 · Wakil yang Selalu Terlambat
# │ LOKASI  : Kampus Kouseikan · Taman Kampus
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : Moeka datang terlambat tapi memimpin acara.
# │ INTI    : A maklum / B tegur / C bantu.
# │ AKHIRAN : C membuka sisi kompeten.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo01:
    call kk_scene_enter("moeka", "Hanami · Taman Kampus")
    nar "Moeka tiba di taman dengan kamera tersampir, gulungan alas di lengan, dan permintaan maaf yang belum selesai ketika ia mulai membagi pekerjaan. Ia terlambat, tetapi dalam setengah menit semua orang sudah tahu harus membawa apa."
    moeka "Yang pegang alas ke sana, yang bawa makanan jangan kena matahari! Maaf aku telat. Kalian boleh mengomel setelah semuanya dapat tempat, ya."
    nar "Ia melihat satu orang berdiri sendirian di ujung, memanggil namanya, dan memberi tugas yang membuatnya segera menjadi bagian rombongan."
    call kk_family_menu("Mo01", ["Geser sedikit agar ia bisa lewat.", "Ingatkan bahwa orang-orang tadi menunggunya.", "Bantu membentangkan alas sesuai arahannya."])
    if _return == "A":
        moeka "Makasih. Aku menyusul setelah semuanya duduk."
        nar "Kau memberi jalan dan membiarkan ia menyelesaikan arahan. Ia kembali beberapa menit kemudian dengan napas lebih teratur, meminta pendapat tentang penataan alih-alih hanya meminta dimaafkan."
    elif _return == "B":
        moeka "Iya. Maaf membuat kalian menunggu."
        nar "Ia menerima teguran tanpa lelucon, lalu mengatakan akan memberi kabar lebih awal jika terlambat lagi. Setelah itu barulah ia kembali bekerja, kali ini lebih hati-hati melihat apakah kesibukannya membuat orang lain menunggu jawaban."
    else:
        nar "Kau membentangkan alas menurut petunjuknya. Moeka menyesuaikan tempat duduk agar makanan terjangkau semua orang dan tidak ada yang tersisih di belakang pohon."
        moeka "Nah. Jangan percaya kalau nanti ada yang bilang aku cuma bagian meramaikan. Aku juga pandai membuat keramaian punya tempat duduk."
        nar "Ia tertawa, lalu akhirnya duduk di sebelahmu dengan rasa lega yang tidak bisa dipalsukan oleh suara ceria."
    return

# ┌─ PANDUAN CERITA · S01 · Papan Shogi di Taman
# │ LOKASI  : Kampus Kouseikan · Taman Kampus
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia bermain sendiri.
# │ INTI    : A menantang / B mengamati / C lewat.
# │ AKHIRAN : A membuka rivalitas.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S01:
    call kk_scene_enter("shiori", "Hanami · Taman Kampus")
    nar "Di tengah hanami, Shiori memindahkan bidak shogi lalu memutar papan untuk melihat dari sisi lain. Satu kelopak jatuh di antara petak; ia memindahkannya sebelum melanjutkan seolah benda itu tamu yang salah memilih kursi."
    shiori "Kalau ingin duduk, silakan. Kalau ingin bertanya mengapa bermain sendiri di piknik, jawabannya karena belum ada yang duduk di seberang."
    call kk_family_menu("S01", ["Duduk di seberangnya dan tantang ia bermain.", "Amati langkah berikutnya.", "Biarkan ia bermain sendiri."])
    if _return == "A":
        shiori "Kalau begitu, sisi papan itu milikmu."
        nar "Ia memberi waktu memeriksa posisi, kemudian mengembalikan bidak ke susunan awal agar tak ada keuntungan yang disimpan sepihak. Tantangan diterima dengan kesungguhan yang membuat namamu mulai menarik baginya di luar perkenalan singkat."
    elif _return == "B":
        nar "Ia memperlambat gerakan agar kau dapat mengikuti. Ketika kau menunjuk ancaman yang terlewat, ia memeriksanya alih-alih langsung mengatakan sudah tahu."
        shiori "Benar. Aku terlalu sibuk membela rencanaku sendiri. Kau ingin melihat kemungkinan berikutnya bersama?"
    else:
        nar "Kau memberi salam dan membiarkannya sendiri. Bunyi kayu kembali terdengar ketika kau beranjak; Shiori punya kesenangan yang tetap berlangsung tanpa harus memintamu menjadi penonton."
    return

# ┌─ PANDUAN CERITA · Mo02 · Undian Onsen
# │ LOKASI  : Stasiun & Pasar · Stasiun Kouseikan-mae
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia memenangkan undian.
# │ INTI    : A ucapkan selamat / B iri / C bantu rencana.
# │ AKHIRAN : kedekatan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo02:
    call kk_scene_enter("moeka", "Stasiun Kouseikan-mae")
    nar "Moeka memegang bukti undian dengan dua tangan, takut selembar kertas itu berubah jadi salah baca kalau dilihat terlalu lama. Hadiah perjalanan onsen tertulis jelas, lengkap dengan tanggal yang perlu dipilih."
    moeka "Menang! Aku tadinya cuma ikut karena kuponnya hampir habis masa berlaku. Sekarang kita harus betulan membuat rencana. Seru, ya. Seram juga karena rencananya harus benar."
    if any(c["ev"] == "Mo01" and c["key"] == "C" for c in choices_log):
        nar "Kau mengenali caranya mengumpulkan rombongan. Waktu piknik pun ia mengatur semuanya seperti ini."
    call kk_family_menu("Mo02", ["Ucapkan selamat.", "Akui kau iri pada keberuntungannya.", "Bantu dia memeriksa rencana perjalanan."])
    if _return == "A":
        moeka "Hehe. Rasanya masih belum percaya."
        nar "Kau membiarkannya senang tanpa langsung membebani dengan seluruh urusan rombongan. Ia bercerita bagaimana hampir membuang kupon tersebut, lalu tertawa lagi karena kali ini kesalahan kecil justru tidak terjadi."
    elif _return == "B":
        moeka "Kalau aku yang berharap menang, biasanya malah meleset."
        nar "Pengakuan irimu membuatnya menunduk pada tiket, memikirkan apakah perlu merendahkan kegembiraan agar kau tak merasa kalah."
        moeka "Kamu juga ikut menikmati, kan? Aku nggak ingin hadiah ini jadi alasan kita menghitung siapa yang lebih beruntung."
    else:
        moeka "Boleh! Baca dari atas, ya. Aku cek yang sudah siap."
        nar "Kalian membagi urusan jadwal, peserta, dan biaya yang tidak termasuk hadiah. Moeka lebih tenang ketika kegembiraan boleh disertai angka nyata, dan lebih gembira lagi ketika tahu bukan hanya dirinya yang harus mengingat semuanya."
    return

# ┌─ PANDUAN CERITA · S02 · Ruang Catur di Ryokan
# │ LOKASI  : Lobi ryokan
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : papan di lobi.
# │ INTI    : A bertanding / B sengaja kalah / C menang.
# │ AKHIRAN : B membuat ia jengkel.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S02:
    call kk_scene_enter("shiori", "Lobi ryokan")
    if any(c["ev"] == "S01" and c["key"] == "A" for c in choices_log):
        shiori "Kali ini juga mau duduk di seberangku?"
    else:
        shiori "Papannya sudah tersedia. Kau mau bermain?"
    nar "Lobi ryokan lebih sunyi daripada aula piknik. Shiori meletakkan minuman jauh dari papan, lalu bertanya apakah kau ingin pertandingan singkat atau membiarkannya berlangsung sampai selesai. Kali ini ia tampak punya cukup waktu untuk benar-benar ingin tahu cara pikirmu."
    call kk_family_menu("S02", ["Terima tantangannya dan bermain serius.", "Biarkan dia mengambil bidak yang bisa kauselamatkan.", "Ambil kesempatan untuk memenangkan permainan."])
    if _return == "A":
        shiori "Bagus. Aku ingin melihat langkahmu sendiri."
        nar "Kau bermain dengan seluruh perhatian. Shiori menanyakan alasan satu langkah sesudah pertandingan selesai, lalu menjelaskan bagaimana pertanyaan itu mengubah cara ia membaca lawan yang tadinya dikira sudah dipahami."
    elif _return == "B":
        shiori "Kau melihat langkah itu. Jangan mengalah padaku."
        nar "Ia menolak mengambil kemenangan yang sengaja kaubuat. Ketika kau menyebut niat menyenangkan, ia bertanya apakah dirinya pernah mengatakan tak sanggup kalah. Keramahan yang mengabaikan keinginannya terasa jauh lebih dingin daripada hasil buruk."
    else:
        shiori "Kau melihat celahnya duluan. Satu lagi?"
        nar "Ia mengakui hasil dengan jelas dan segera ingin bertemu caramu berpikir sekali lagi. Pujian paling tulus darinya malam itu berbentuk bidak yang disusun ulang sebelum minuman habis."
    return

# ┌─ PANDUAN CERITA · Mi02 · Kue Percobaan Ketiga
# │ LOKASI  : Dapur ryokan
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : dapur ryokan; kue gagal.
# │ INTI    : A makan semuanya / B jujur / C bantu memperbaiki.
# │ AKHIRAN : C memicu sisi manja.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi02:
    call kk_scene_enter("miyuki", "Dapur ryokan")
    nar "Kue percobaan ketiga keluar dari cetakan dengan bagian tengah yang turun. Miyuki memandangnya seperti pasien yang baru saja menolak seluruh teori terbaiknya."
    miyuki "Baik. Bentuk bukan segalanya. Tapi kalau rasanya ikut begitu, aku perlu membicarakan ini secara serius dengan resepnya."
    nar "Dapur ryokan dipenuhi aroma manis dan dua hasil percobaan sebelumnya. Ia menyerahkan piring kecil, sudah siap meminta maaf sebelum kau mencicipi."
    call kk_family_menu("Mi02", ["Habiskan kue yang sudah ia sajikan.", "Katakan dengan jujur bagian yang kurang enak.", "Gulung lengan bajumu dan bantu memperbaiki adonannya."])
    if _return == "A":
        nar "Kau menghabiskan porsi yang disajikan. Miyuki tertawa kaget, lalu mengambil garpumu sejenak agar kau tidak merasa perlu membuktikan apa-apa dengan potongan berikutnya."
        miyuki "Satu gigitan untuk penilaian cukup. Tapi terima kasih. Aku jadi tahu kegagalan ini masih punya penggemar."
        nar "Ia mencicipi bagiannya sendiri dan akhirnya menertawakan bentuk yang tadi begitu mengganggu."
    elif _return == "B":
        nar "Kau mengatakan bagian tengahnya terlalu padat, sementara pinggirnya enak. Miyuki mencicipi bagian yang kaumaksud, mengangguk tanpa senyum yang dipaksakan."
        miyuki "Itu juga yang kurasakan. Lega kalau kamu nggak harus bilang sempurna cuma karena aku yang membuat."
        nar "Ia menulis catatan pada resep, kali ini tanpa mencoret seluruh percobaannya sebagai gagal."
    else:
        nar "Kau menggulung lengan dan menanyakan pekerjaan yang bisa dibagi. Miyuki memberikan mangkuk, lalu memindahkan dirinya agar kalian sama-sama punya ruang."
        miyuki "Kali ini kalau gagal, kita bisa menyalahkan kerja sama tim. Senpai suka rencana ini."
        nar "Ia mulai memberi instruksi dengan nada manja yang tidak terdengar saat orang lain mengandalkannya. Percobaan keempat belum tentu lebih bagus, tetapi kini ada yang membuat selain dirinya."
    return

# ┌─ PANDUAN CERITA · N02 · Rematch Malam Onsen
# │ LOKASI  : Ruang bersama ryokan
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : ia selalu meminta rematch.
# │ INTI    : A terus menang / B mengalah / C ajak tim.
# │ AKHIRAN : Trust.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N02:
    call kk_scene_enter("nagisa", "Ruang bersama ryokan · Malam")
    nar "Ruang bersama ryokan mulai sepi, tetapi Nagisa masih duduk menghadap layar. Ia mengulangi kekalahannya dengan istilah yang sangat teknis, lalu menyimpulkan satu pertandingan lagi akan membuktikan teorinya."
    nagisa "Jangan tidur dulu. Aku baru paham tombol yang tadi. Kalau berhenti sekarang, besok lupa."
    call kk_family_menu("N02", ["Bermain sepenuh kemampuanmu.", "Perlambat permainanmu agar ia bisa menang.", "Ajak dia bermain satu tim."])
    if _return == "A":
        nar "Kau bermain serius. Nagisa kalah lagi, tetapi kali ini bisa menunjukkan tepat di mana ia salah."
        nagisa "Jangan senyum dulu. Aku makin dekat. Lihat, yang tadi bukan kesalahan yang sama."
        nar "Ia menyodorkan pengendali ketika kau perlu jeda, lalu menunggu dengan tidak sabar. Tantangannya keras, namun kini ia percaya kau menganggapnya lawan yang layak dihadapi sungguhan."
    elif _return == "B":
        nar "Kau memperlambat permainan agar ia menang. Nagisa mengangkat kedua tangan, lalu menurunkannya ketika mengingat gerakanmu di akhir pertandingan."
        nagisa "Tadi kamu bisa mengambil itu. Kenapa berhenti?"
        nar "Kemenangan di layar mendadak tidak cukup. Ia menyimpan pertanyaan tersebut, lebih kesal karena mengira kau merasa perlu melindunginya dari hal sekecil kekalahan dalam permainan."
    else:
        nar "Kau menawarkan permainan satu tim. Nagisa menyipitkan mata, mencoba menentukan apakah itu alasan agar tidak perlu melawannya lagi, lalu mengambil tempat di sebelahmu."
        nagisa "Baik. Aku sisi kiri. Kalau aku berteriak, itu informasi, bukan marah."
        nar "Beberapa menit kemudian ia sudah berteriak sekaligus tertawa. Kalian tetap kalah sekali, tetapi kali ini ia meminta ulang dengan kata kita."
    return

init 1 python:
    _hook("Mo02-A", lambda: kk_rel("moeka", "aff", 5))
    _hook("Mo02-B", lambda: kk_rel("moeka", "aff", -5))
    _hook("Mo02-C", lambda: kk_rel("moeka", "trust", 5))
    _hook("S02-A", lambda: kk_adj("respek_shiori", 5))
    _hook("S02-B", lambda: kk_adj("respek_shiori", -5))
    _hook("S02-C", lambda: kk_adj("respek_shiori", 8))
    _hook("Mi02-C", lambda: kk_adj("dimanja_miyuki", 5))
    _hook("N02-A", lambda: kk_rel("nagisa", "trust", 5))
    _hook("N02-B", lambda: kk_rel("nagisa", "trust", -5))
    _hook("N02-C", lambda: kk_rel("nagisa", "trust", 5))


# Event dinamis Nagisa, Alur_Cabang/02. Lokasi ayunan mengikuti harapan
# Nagisa pada Koita yang turun hari ini, termasuk saat pemain sedang jauh.
# ┌─ PANDUAN CERITA · N-D03 · Ayunan Malam
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Sakurajima Nagisa
# │ AWALAN  : hari itu harapan_koita turun
# │ INTI    : A Duduk di ayunan sebelah / B panggil Koita / C beri ruang
# │ AKHIRAN : kelekatan +; bila Koita yang datang, hasilnya tergantung Koita
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N_D03:
    call kk_scene_enter("nagisa", "Taman Lingkungan · Ayunan malam")
    nar "Ujung sepatu Nagisa menahan ayunan agar tidak bergerak. Ia sudah berada di sana cukup lama untuk lupa bahwa udara malam membuat tangannya dingin."
    nagisa "Kalau kamu datang untuk bilang Koita sebenarnya perhatian, jangan. Aku sedang ingin kesal tanpa dibantu membelanya. Ayunan sebelah kosong kalau mau duduk."
    call kk_family_menu("N-D03", ["Duduk di ayunan sebelah.", "Tawarkan untuk memanggil Koita.", "Beri dia ruang."])
    if _return == "A":
        nar "Kau duduk, membiarkan rantai berbunyi pelan sebelum bertanya apakah ia ingin bicara. Nagisa menatap tanah."
        nagisa "Aku cuma capek menjadi orang yang selalu tahu kenapa dia nggak bisa datang. Kadang aku ingin dia yang bertanya kenapa aku masih menunggu."
        nar "Ia mengusap mata dan menyalahkan angin. Kau tidak perlu membenarkannya agar tetap boleh berada di sana."
    elif _return == "B":
        if kk_daily_place("koita") == "Taman Lingkungan":
            koita "Nagisa? Kau mau bicara?"
            nar "Nagisa menoleh, kaget karena nama yang baru saja dikeluhkan benar-benar hadir. Ia butuh beberapa detik sebelum memutuskan apakah ingin marah atau memberi kesempatan mendengar."
            nagisa "Iya. Tapi kamu dengar sampai selesai. Jangan bilang nggak apa-apa sebelum aku bilang apa yang sakit."
        else:
            nar "Koita tidak ada di taman. Nagisa mendengarkan tawaranmu memanggilnya, lalu menggeleng tanpa menatapmu."
            nagisa "Aku nggak mau merasa dia datang karena dijemput orang lain lagi. Malam ini biarkan dulu."
    else:
        nar "Kau memberi tahu bahwa akan pergi dan membiarkan ia memilih tetap di sana. Nagisa mengangguk, mengucapkan hati-hati dengan suara kecil."
        nar "Ayunan sebelah tidak bergerak ketika kau berjalan menjauh. Jarak yang kauberikan bisa menjadi ruang untuk tenang; malam itu kau tidak tinggal cukup lama untuk tahu apakah ia berhasil menemukannya."
    return

# ┌─ PANDUAN CERITA · N-D08 · Rekaman Pertandingan
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Sakurajima Nagisa
# │ AWALAN  : N02-B pernah terjadi; gengsi ≥ 60
# │ INTI    : A Akui / B sangkal / C tantang ulang dengan serius
# │ AKHIRAN : Trust dan gengsi bergeser
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N_D08:
    call kk_scene_enter("nagisa", "Studio Arsitektur · Rekaman permainan")
    nar "Nagisa menghentikan rekaman permainan tepat sebelum gerakan terakhirmu. Ia sudah menyiapkannya, lengkap dengan bagian yang menunjukkan kesempatan yang sengaja kaulewatkan."
    nagisa "Aku putar ulang. Di sini kamu bisa menang. Aku nggak sebodoh itu sampai nggak tahu perbedaannya. Kenapa mengalah?"
    call kk_family_menu("N-D08", ["Akui kau sengaja mengalah.", "Sangkal bahwa kau sengaja kalah.", "Tantang dia lagi dan mainlah dengan serius."])
    if _return == "A":
        nar "Kau mengaku ingin membuatnya senang. Nagisa mendengar sampai selesai, lalu mematikan rekaman."
        nagisa "Aku senang main denganmu, termasuk waktu kalah. Tapi kalau kamu mengalah, aku nggak bisa percaya waktu benar-benar menang."
        nar "Ia meminta kau mengingat itu. Tegurannya tajam, tetapi sesudahnya ia masih menawarkan pertandingan lain."
    elif _return == "B":
        nar "Kau menyangkal. Nagisa memutar bagian yang sama, diam selama layar menunjukkan semua yang tidak mau kauakui."
        nagisa "Ini cuma permainan. Kalau untuk hal sekecil ini saja kamu nggak bisa jujur, aku harus menebak apa lagi?"
        nar "Ia menyimpan konsol dan tidak melanjutkan. Yang rusak sore itu bukan catatan kemenangannya."
    else:
        nar "Kau menantangnya bermain sungguhan. Nagisa menatapmu cukup lama untuk memastikan tidak ada lelucon di belakang tawaran itu."
        nagisa "Baik. Aku mungkin tetap kalah. Kamu jangan menghitung itu sebagai alasan mengasihaniku lagi."
        nar "Kalian mulai. Ketika ia kalah, ia memprotes keputusan sendiri, lalu tertawa dan meminta ulang. Kali ini hasil layar terasa bisa dipercaya."
    return

init 1 python:
    _hook("N-D03-A", lambda: kk_adj("kelekatan_nagisa",5))
    _hook("N-D08-A", lambda: (kk_rel("nagisa","trust",5), kk_adj("gengsi_nagisa",-5)))
    _hook("N-D08-B", lambda: kk_rel("nagisa","trust",-5))
    _hook("N-D08-C", lambda: kk_rel("nagisa","trust",5))
