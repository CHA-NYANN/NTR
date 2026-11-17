# Kesadaran Koita, Tahun 2 (K12, K14, K15, K16). Ia mulai merasa ada yang ganjil
# dan membalas. Cabang gelap (manfaatkan kepanikan/kerapuhan, sebar rumor) ditulis
# sebagai konsekuensi singkat tanpa metode. Efek mengikuti Event_Koita.
# ┌─ PANDUAN CERITA · K12 · Telepon dari Seberang
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : saat perjalanan Kansai Koita menelepon berulang.
# │ INTI    : A angkat / B abaikan / C minta heroine yang menjawab.
# │ AKHIRAN : Jealousy Koita naik; mulai mencari tahu.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K12:
    call kk_scene_enter("koita", "Kansai · Panggilan dari Koita")
    nar "Nama Koita muncul lagi ketika kereta di Kansai memasuki stasiun. Tiga panggilan terlewat memenuhi layar; yang keempat bergetar di tanganmu sebelum kau selesai membaca pesan sebelumnya."
    koita "Kamu dengar? Di sana berisik sekali. Katanya nggak ada acara minggu ini. Kalian pergi?"
    nar "Ia tertawa pendek, lalu bertanya siapa saja yang ikut. Nama pertama terdengar santai. Pada nama berikutnya, ia mulai menunggu jawaban lebih lama."
    call kk_family_menu("K12", ["Akui kau memang pergi dan minta maaf.", "Alihkan pembicaraan.", "Minta orang lain yang menjawab teleponnya."])
    if _return == "A":
        nar "Kau mengakui perjalanan itu dan meminta maaf karena tidak memberi kabar setelah ia menghubungimu. Kau tidak menjanjikan akan meminta izin setiap kali pergi."
        koita "Iya. Aku juga nggak bermaksud kamu harus lapor. Aku cuma... baru tahu dari foto orang lain."
        nar "Ia menarik napas, berusaha mengembalikan suara yang ringan."
        koita "Selamat jalan-jalan. Kalau ada waktu, kirim foto. Kalau nggak sempat juga nggak apa-apa."
        nar "Kali ini ia menutup telepon sebelum meminta penjelasan lain."
    elif _return == "B":
        nar "Kau membicarakan kereta dan sinyal, menghindari pertanyaannya tentang siapa yang berada di dekatmu. Koita membiarkan penjelasanmu selesai."
        koita "Oh. Jadi kapan pulang?"
        nar "Kau kembali menjawab samar. Di seberang, suara cerianya menghilang sedikit demi sedikit."
        koita "Ya sudah. Aku nggak mau mengganggu perjalanan kalian."
        nar "Kata kalian terdengar sangat jelas. Setelah panggilan terputus, ia masih mengirim satu pertanyaan yang sama."
    else:
        nar "Kau menyerahkan ponsel kepada orang yang bepergian bersamamu. Sapaan singkatnya disambut keheningan sebelum Koita akhirnya menjawab."
        koita "Oh, kamu juga di sana. Aku nggak tahu."
        nar "Pertanyaannya kini terdengar lebih sopan, lebih berhati-hati. Ketika ponsel kembali kepadamu, ia tidak lagi menanyakan lokasimu."
        koita "Nanti kalau sudah pulang, kita bicara, ya. Ada yang rupanya selalu aku tahu paling akhir."
    return

# ┌─ PANDUAN CERITA · K14 · Rumor tentang Koita
# │ LOKASI  : Kampus Kouseikan · Kafe Komorebi
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : Kurosawa Mei mengunggah rumor bahwa Koita "mempermainkan".
# │ INTI    : A bantu bantah / B biarkan / C sebarkan lebih jauh
# │ AKHIRAN : reputasi Koita; C bisa memicu rute kehancuran.
# │ KOREKSI : katalog asli punya opsi ke-4 ("beli kebungkaman Mei") yang TIDAK
# │           diimplementasikan (tak ada hook D). 3 opsi di atas = final, jangan
# │           menambah cabang D.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K14:
    call kk_scene_enter("koita", "Kafe Komorebi")
    nar "Mei tidak menuliskan seluruh nama. Ia tidak perlu: cukup inisial, klub, dan kisah seseorang yang katanya membuat banyak orang merasa menjadi satu-satunya. Di Komorebi, meja sebelah berhenti membicarakannya ketika Koita masuk."
    koita "Aku sudah baca. Yang kalian kirim ke grup juga."
    nar "Ia meletakkan ponsel telungkup, lalu membaliknya lagi sebelum sempat memesan."
    koita "Ada yang benar. Ada yang dia dengar dari orang lain. Sekarang semuanya dibaca dengan nada yang sama."
    call kk_family_menu("K14", ["Bantu bantah rumor itu terang-terangan.", "Biarkan rumor itu berjalan.", "Dorong rumor itu lebih jauh di belakang layar."])
    if _return == "A":
        nar "Kau membantah bagian yang tidak berdasar dan menolak menjadikan dugaan sebagai fakta. Tidak semua pembaca menyambut baik pembelaan itu, tetapi Koita mendapat ruang bernapas."
        koita "Makasih. Aku sempat berharap kamu bilang semuanya bohong. Padahal itu juga nggak benar."
        nar "Ia menggeser ponsel menjauh, cukup jauh untuk tak lagi membaca setiap balasan."
        koita "Yang memang harus kujelaskan, akan kujelaskan ke orangnya. Tolong ingatkan kalau aku mulai memakai pembelaanmu untuk kabur dari bagian itu."
    elif _return == "B":
        nar "Kau tidak ikut membantah atau menguatkan. Unggahan itu tetap bergerak melalui orang-orang yang merasa meneruskan kabar berbeda dari membuat tuduhan."
        koita "Aku nggak minta kamu membelaku."
        nar "Ia mengatakannya tanpa menatapmu. Beberapa menit kemudian, seseorang membatalkan rencana bertemu dengannya tanpa menjelaskan mengapa."
        nar "Koita membalas tidak apa-apa, lalu menghabiskan minumannya terlalu cepat."
    else:
        nar "Kau ikut memperluas peredaran rumor. Orang yang membaca kemudian tidak melihat pilihan kecilmu; mereka hanya melihat kabar yang tampaknya sudah diketahui semua orang."
        nar "Koita mulai menemui pintu percakapan yang tertutup sebelum ia sampai. Orang-orang berhenti bertanya langsung karena merasa telah memiliki jawaban."
        koita "Aku tahu ada yang membantu ini menyebar. Aku cuma belum tahu siapa."
        nar "Kau masih bisa duduk di depannya tanpa dibantah. Kepercayaan itu kini menjadi bagian dari apa yang sedang kaurusak."
    return

# ┌─ PANDUAN CERITA · K15 · Panik Pertama
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : Koita meminta waktu: "ada yang aneh."
# │ INTI    : A pengakuan sebagian / B bohong / C konfrontasi
# │ AKHIRAN : koita_sadar naik. Mulai manuver balik.
# │ KOREKSI : katalog asli punya opsi ke-4 ("manfaatkan kepanikannya") yang TIDAK
# │           diimplementasikan (tak ada hook D). 3 opsi di atas = final, jangan
# │           menambah cabang D.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K15:
    call kk_scene_enter("koita", "Gedung Sastra")
    nar "Koita menunggumu selesai kuliah, lalu meminta berjalan ke ujung koridor yang sepi. Ia membawa botol minuman untukmu. Tutupnya belum dibuka; ia terus memutarnya setengah putaran lalu mengencangkan lagi."
    koita "Aku mencoba mengingat kapan semuanya mulai berubah. Pesan, ajakan, cara mereka diam kalau aku datang. Kamu ada di banyak bagian yang kuingat."
    nar "Ia menyerahkan botol itu, menyadari tangannya memerlukan sesuatu untuk dilakukan."
    koita "Aku nggak mau menuduh cuma karena takut. Makanya aku tanya dulu. Ada yang kamu sembunyikan dariku?"
    call kk_family_menu("K15", ["Akui sebagian: ada yang kau sembunyikan.", "Katakan ia hanya terlalu banyak berpikir.", "Hadapi langsung dan buka kartunya."])
    if _return == "A":
        nar "Kau mengakui sebagian keterlibatanmu. Koita tidak memotong sampai bagian yang sengaja kaulewati menjadi lebih jelas daripada penjelasanmu."
        koita "Kamu tahu itu belum cukup. Aku juga tahu."
        nar "Ia mengambil kembali botolnya sendiri dari ambang jendela."
        koita "Setidaknya sekarang aku nggak perlu pura-pura semua ini cuma perasaanku. Sisanya akan kutanyakan ke mereka."
    elif _return == "B":
        nar "Kau mengatakan ia terlalu banyak berpikir. Koita sempat mengangguk, gerakan lama ketika ia ingin menerima versi yang paling sedikit mengancam."
        koita "Mungkin. Tapi kalau aku berhenti bertanya, kamu jadi lebih nyaman, ya?"
        nar "Pertanyaan itu mengagetkan dirinya sendiri. Ia menatapmu lebih lama, lalu meminta waktu untuk berpikir tanpa diberi jawaban tambahan."
        nar "Kali ini penyangkalanmu tidak menutup persoalan. Ia hanya menambah satu hal yang ingin Koita periksa."
    else:
        nar "Kau membuka bagian yang selama ini ia curigai, lalu menantang caranya mempertahankan semua orang tanpa memilih. Wajah Koita memerah."
        koita "Aku bisa salah kepada mereka. Itu nggak membuat kamu boleh mengatur mereka di belakangku."
        nar "Ia mundur setengah langkah, mengambil ruang untuk mengucapkan kalimat berikutnya tanpa meninggikan suara."
        koita "Mulai sekarang, kalau ada yang mau tahu tentangku, aku akan bicara sendiri. Kamu nggak perlu jadi perantaranya lagi."
    return

# ┌─ PANDUAN CERITA · K16 · Telepon Larut Malam
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : Koita meminta pemain ke rumahnya; ia bercerita tentang ayahnya.
# │ INTI    : A hadir dan dengarkan / B tolak / C manfaatkan kerapuhannya.
# │ AKHIRAN : membuka akar sifat; A memperdalam Trust; C memicu Fear.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K16:
    call kk_scene_enter("koita", "Rumah Amamiya · Malam")
    nar "Koita belum menyalakan lampu utama ketika kau sampai. Ia membukakan pintu dengan rambut basah dan mata seseorang yang sudah mencoba tidur lebih dari sekali."
    koita "Maaf. Aku tahu sudah malam. Kamu boleh bilang nggak bisa. Aku tadi cuma... ingin ada suara orang."
    nar "Di ruang keluarga ada album tertutup. Koita menyentuh sampulnya, lalu memindahkan tangan."
    koita "Tadi aku ingat ayah kandungku. Yang meninggal waktu aku kecil. Boleh cerita? Aku nggak tahu kenapa baru sekarang begini."
    call kk_family_menu("K16", ["Duduk dan dengarkan ceritanya sampai selesai.", "Katakan kau tidak bisa malam ini.", "Pakai kerapuhannya untuk keuntunganmu."])
    if _return == "A":
        nar "Kau duduk. Koita memulai dari hal yang sepele: suara kunci, mainan yang dijanjikan akan diperbaiki, kebingungan ketika orang dewasa tidak pernah menjawab kapan ayahnya pulang."
        koita "Aku tahu meninggal bukan meninggalkan dengan sengaja. Waktu kecil aku nggak ngerti bedanya."
        nar "Ia berhenti beberapa kali. Kau tidak mengisi setiap jeda."
        koita "Terus aku belajar bikin orang betah. Ingat yang mereka suka, jangan menolak, jangan sampai ada yang benar-benar selesai. Aku baru sadar cara itu bisa menyakiti mereka."
        nar "Menjelang akhir, ia tidak lagi meminta maaf setiap kali menarik napas. Kau tetap duduk sampai ceritanya selesai."
    elif _return == "B":
        nar "Kau mengatakan tidak bisa tinggal malam ini. Koita mengangguk segera, sebelum kau selesai menjelaskan."
        koita "Iya. Tentu. Aku mendadak sekali mintanya. Hati-hati pulang."
        nar "Ia menahan pintu sampai kau melewati teras, lalu menutupnya pelan. Lampu ruang keluarga tetap menyala ketika kau mencapai jalan."
        nar "Kau tak tahu apakah ia akhirnya menghubungi orang lain. Kepergianmu sah, tetapi bagi seseorang yang sedang takut kehilangan, penjelasan yang masuk akal belum tentu cukup untuk menenangkan malam."
    else:
        nar "Kau membiarkan percakapannya berubah menjadi kesempatan menuntut kepastian dan keberpihakan. Setiap ia ragu, malam dan kesepiannya terasa makin menekan di antara kalian."
        koita "Aku minta didengarkan. Aku nggak tahu harus menjanjikan apa untuk itu."
        nar "Ia menarik album menjauh. Rasa malu datang lebih dahulu daripada marah, membuatnya mengangguk pada hal-hal yang belum sanggup ia pertimbangkan."
        nar "Ketika kau pulang, ia mengucapkan terima kasih. Kalimat itu tidak menghapus ketakutan yang kini ikut melekat pada bunyi kedatanganmu."
    return

init 1 python:
    def kk_koita_wake(step=1):
        store.koita_sadar = max(0, min(100, koita_sadar + step))

    _hook("K12-A", lambda: kk_rel("koita","trust",4))
    _hook("K12-B", lambda: kk_rel("koita","jeal",4))
    _hook("K12-C", lambda: kk_rel("koita","jeal",6))
    _hook("K14-A", lambda: (kk_rel("koita","trust",5), kk_flag("koita_dibela")))
    _hook("K14-B", lambda: kk_koita_suspect(5))
    _hook("K14-C", lambda: (kk_flag("koita_rumor_didorong"), kk_koita_fear(8)))
    _hook("K15-A", lambda: kk_koita_wake(1))
    _hook("K15-B", lambda: kk_koita_suspect(8))
    _hook("K15-C", lambda: (kk_koita_wake(1), kk_koita_fear(6)))
    _hook("K16-A", lambda: (kk_rel("koita","trust",6), kk_flag("koita_akar_diketahui")))
    _hook("K16-B", lambda: kk_rel("koita","trust",-4))
    _hook("K16-C", lambda: (kk_koita_fear(12), kk_flag("koita_dimanfaatkan")))
