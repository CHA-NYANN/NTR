# Draft adegan dari Event_Shiori dan Alur_Cabang/05. kk_family_menu mencatat pilihan satu kali.
# ┌─ PANDUAN CERITA · S07 · Natal Keluarga Saionji
# │ LOKASI  : Distrik Elite · Rumah Saionji
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : makan malam keluarga.
# │ INTI    : A diundang / B tidak / C mengirim hadiah.
# │ AKHIRAN : hub besar #3; keluarga mengenal pemain.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S07:
    call kk_scene_enter("shiori", "Natal di rumah Saionji")
    nar "Aroma sup dari ruang makan tidak menyerupai pesta yang kaubayangkan dari nama Saionji. Ayah Shiori sedang memindahkan kursi, ibunya menegur bahwa tak perlu mengatur tamu sebelum tamunya memilih masuk."
    shiori "Kami baru mau makan. Kalau belum punya janji, silakan. Mereka lebih mudah diajak bicara daripada reputasi rumah ini. Biasanya."
    call kk_family_menu("S07", ["Masuk dan makan bersama keluarganya.", "Ucapkan selamat Natal lalu pamit.", "Titipkan hadiah untuk keluarganya."])
    if _return == "A":
        nar "Ibunya menggeser piring agar ada tempat untukmu. Saat membagikan sup, ia sudah ingat namamu."
        nar "Pertanyaannya tentang kuliah dan makanan yang kausukai, bukan nama keluarga. Shiori memerhatikan kegugupanmu dengan geli, lalu membantu mengubah topik sebelum keramahan ibunya terasa seperti pemeriksaan panjang."
    elif _return == "B":
        nar "Kau pamit dengan ucapan selamat Natal. Shiori menyampaikan salam keluarga dan tidak menjadikan undangan yang ditolak alasan membuatmu merasa kurang sopan."
        shiori "Lain waktu boleh datang. Tidak harus menunggu hari raya agar diizinkan makan di sini."
    else:
        shiori "Biar kusampaikan sendiri. Terima kasih sudah mampir."
        nar "Ia menanyakan pesan yang ingin dititipkan, memastikan hadiah itu tetap dikenali sebagai niatmu sendiri, bukan tanda kedekatan yang akan ditafsirkan sembarangan oleh tamu lain."
    return

# ┌─ PANDUAN CERITA · S-D08 · Teh dengan Ibu Saionji
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : setelah S07-A
# │ INTI    : A Jujur / B menyanjung / C membocorkan
# │ AKHIRAN : kehangatan keluarga; Shiori tahu apa yang dikatakan
# └─ tulis / perbaiki dialog di bawah ──
label kk_saionji_tea:
    nar "Ibu Shiori mengenalimu dari meja makan malam Natal. Ia menuangkan dua cangkir teh."
    "Ibu Shiori" "Di rumah ia sering duduk sendiri. Aku tahu dia menyukainya kadang-kadang. Aku hanya ingin tahu apakah di kampus dia punya teman yang memang diinginkan, bukan orang yang merasa harus dekat."
    call kk_family_menu("S-D08", ["Ceritakan apa yang kaulihat tanpa menebak perasaannya.", "Katakan bahwa semua orang selalu ingin bersamanya.", "Ulangi obrolan pribadi kalian kepada ibunya."])
    if _return == "A":
        "Ibu Shiori" "Terima kasih. Mungkin aku harus bertanya sendiri padanya."
        nar "Kau menceritakan yang kaulihat tanpa menebak seluruh perasaan Shiori. Ibunya tampak lega, lalu meminta agar kau tidak merasa perlu menjadi juru bicara putrinya pada pertemuan berikutnya."
    elif _return == "B":
        nar "Kau menyanjung seolah semua orang selalu ingin bersamanya. Ibunya tersenyum sopan, tetapi menanyakan apakah Shiori sendiri senang berada di tengah mereka. Pujianmu ternyata belum menjawab hal yang dikhawatirkannya."
    else:
        nar "Ibu Shiori meletakkan cangkirnya. Baru sekarang kau sadar itu cerita Shiori untukmu."
        "Ibu Shiori" "Aku ingin mengenal kabarnya. Aku tidak memintamu menyerahkan kepercayaan yang diberikan kepadamu. Yang ini lebih baik dia sendiri yang menceritakan."
    return

# ┌─ PANDUAN CERITA · S09 · Tawaran Persahabatan
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia meminta teman sejati.
# │ INTI    : A terima / B tolak / C manfaatkan.
# │ AKHIRAN : shiori_kepercayaan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S09:
    call kk_scene_enter("shiori","Klub Catur")
    nar "Shiori memasukkan bidak ke kotak sebelum percakapan selesai. Ia berhenti pada dua buah terakhir, tampak sedang mempertimbangkan pertanyaan yang tidak bisa diuji dengan gerakan lawan."
    shiori "Kalau aku datang tanpa papan, tanpa undangan pesta, tanpa hal yang bisa kuberikan... kau masih mau duduk denganku? Aku tahu itu terdengar terlalu bersungguh-sungguh. Aku memang sedang begitu."
    call kk_family_menu("S09", ["Geser kursi dan ajak dia tinggal setelah klub tutup.", "Katakan kau lebih nyaman hanya bertemu untuk bermain.", "Terima, lalu minta dia mengenalkanmu pada orang penting."])
    if _return == "A":
        nar "Ia menyimpan papan dan menarik kursinya kembali."
        shiori "Baik. Aku ingin bercerita tentang hari yang agak membosankan. Kamu boleh bilang kalau mulai bosan. Aku ingin mencoba tidak menebak semuanya sendiri."
        nar "Kalian tetap tinggal sesudah klub tutup, menemukan bahwa pembicaraan biasa juga dapat menjadi sesuatu yang ingin ditunggu."
    elif _return == "B":
        nar "Kau memilih menjaga pertemuan sebatas permainan. Shiori menerima, menutup kotak yang tadi hampir dibiarkan terbuka sebagai alasan tinggal."
        shiori "Terima kasih sudah jelas. Aku kecewa sedikit. Itu bukan permintaan agar kamu mengubah jawaban."
    else:
        shiori "Oh. Jadi ada orang lain yang ingin kautemui."
        nar "Ia mendengar permintaan perkenalanmu sampai selesai. Sesudahnya keramahan tetap ada, tetapi tawaran persahabatan yang baru diberikan tidak diulang dalam bentuk lain."
    return

# ┌─ PANDUAN CERITA · S-D04 · Pertanyaan Jebakan
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : daftar_kebohongan ≥ 1
# │ INTI    : A Jujur sekarang / B bohong lebih rapi / C alihkan
# │ AKHIRAN : jujur sekarang lebih murah; bohong yang ketahuan belakangan dihitung dua kali
# └─ tulis / perbaiki dialog di bawah ──
label kk_shiori_question:
    if any(c["ev"] == "C11" and c["key"] == "B" for c in choices_log):
        shiori "Waktu kita melihat ilustrasi sampul itu, kau seperti hendak mengatakan sesuatu tentang Shena. Apa aku salah ingat?"
    else:
        shiori "Aku masih memikirkan ceritamu kemarin. Ada bagian yang belum kauceritakan?"
    nar "Pertanyaannya tidak memastikan apa yang sudah diketahui. Ia memberimu satu kesempatan mengatakan bagian yang sengaja disimpan tanpa lebih dahulu perlu ditunjukkan buktinya."
    call kk_family_menu("S-D04", ["Ceritakan bagian yang sengaja kaulewatkan.", "Susun alasan lain agar ceritamu terdengar cocok.", "Balik bertanya tentang buku yang ia baca."])
    if _return == "A":
        shiori "Aku senang mendengarnya darimu sendiri."
        nar "Ia menanyakan akibat yang belum dipahami, tidak langsung menjanjikan percaya. Namun kesediaanmu bicara sebelum didesak memberinya alasan untuk tetap berada dalam percakapan."
    elif _return == "B":
        nar "Shiori mengulang satu kalimatmu persis seperti yang baru saja kauucapkan."
        shiori "Baik. Aku ingin memastikan mengingat jawabanmu dengan benar. Supaya nanti kita tidak perlu berdebat tentang kata yang sebenarnya dipakai."
    else:
        nar "Kau menanyakan buku yang dibaca. Shiori menjawab secukupnya, lalu mengatakan pertanyaannya tadi belum hilang hanya karena ia bersedia sopan mengenai topik lain."
    return

# ┌─ PANDUAN CERITA · S14 · Natal Kedua: Senyum yang Sama
# │ LOKASI  : Distrik Elite · Rumah Saionji
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia tidak marah dan tidak menjauh; ia tersenyum persis seperti biasa.
# │ INTI    : A minta maaf / B menyalahkan / C menghindar.
# │ AKHIRAN : stage 3.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S14:
    call kk_scene_enter("shiori","Natal kedua di rumah Saionji")
    if kk_has("shiori_teman_dipercaya"):
        shiori "Dulu kau mau duduk denganku bahkan setelah klub tutup. Malam ini juga ada kursi kosong."
    else:
        shiori "Masuklah sebentar. Di luar dingin."
    nar "Ia menyambut dengan senyum yang kaubawa dalam banyak kenangan baik. Keluarganya tetap hangat; hanya jarak pribadi Shiori yang terasa lebih rapi, seolah setiap celah kini harus sengaja diberikan."
    call kk_family_menu("S14", ["Minta maaf atas jawabanmu waktu itu.", "Katakan bahwa ia juga ikut membuat keadaan sulit.", "Ucapkan selamat Natal tanpa membahasnya."])
    if _return == "A":
        shiori "Aku dengar. Terima kasih sudah datang."
        nar "Ia meminta kau menyebut bagian yang disesali, bukan merangkum semuanya sebagai keadaan yang rumit. Setelah mendengar, ia mengajak masuk tanpa mengatakan urusan kalian sudah selesai."
    elif _return == "B":
        nar "Kau mengatakan ia juga membuat keadaan sulit. Shiori mendengarkan, kemudian menanyakan apakah kesulitan itu dipakai untuk menjelaskan atau membatalkan tanggung jawabmu."
        shiori "Aku bisa punya bagian salah. Itu tidak membuat dua cerita yang bertentangan mendadak sama-sama benar."
    else:
        nar "Kau mengucapkan selamat Natal dan menghindari persoalan lama. Shiori membalas ucapanmu dengan hangat yang cukup untuk tamu. Kalian melewati malam tanpa satu pun langkah mendekati yang belum selesai."
    return

# ┌─ PANDUAN CERITA · S15 · Hatsumode: Doa untuk Siapa
# │ LOKASI  : Alam & Pantai · Kuil
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia berdoa.
# │ INTI    : A tanya / B tidak / C ikut.
# │ AKHIRAN : petunjuk.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S15:
    call kk_scene_enter("shiori","Kuil saat Tahun Baru")
    nar "Shiori memberi jalan kepada keluarga yang membawa anak kecil. Ia mengamati tangan orang tua yang menahan agar anak itu tidak jatuh, lalu lama tidak bergerak meski antrean di depan sudah kosong."
    call kk_family_menu("S15", ["Tanya untuk siapa ia akan berdoa.", "Biarkan ia berdoa sendiri.", "Berdiri di sampingnya dan ikut berdoa."])
    if _return == "A":
        shiori "Untuk seseorang yang jawabannya masih kutunggu."
        nar "Ia tidak menyebut nama. Ketika kau menanyakan hasil yang diharapkan, ia mengatakan ingin jawaban yang benar, lalu mengakui dirinya juga bisa takut pada kebenaran tersebut."
    elif _return == "B":
        nar "Kau memberi ruang untuk doanya sendiri. Shiori menunduk, menutup mata, dan kembali dengan wajah yang tidak perlu menjelaskan seluruh isinya kepadamu."
    else:
        nar "Kalian baru membuka mata setelah bunyi lonceng berhenti."
        shiori "Aku biasanya lebih percaya usaha daripada doa. Hari ini aku ingin membiarkan ada satu keinginan yang tidak harus kubuktikan dapat kukendalikan."
    return

# ┌─ PANDUAN CERITA · S16 · Valentine: Papan Kosong
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia tidak menjawab.
# │ INTI    : A datang / B tunggu / C abaikan.
# │ AKHIRAN : stage 3.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S16:
    call kk_scene_enter("shiori","Klub Catur saat Valentine")
    if kk_has("shiori_mendengar_maaf"):
        nar "Saat Natal ia mendengarkan permintaan maafmu. Hari ini kursi di seberangnya kosong lagi."
    if kk_has("shiori_doa_ditanya"):
        nar "Kau teringat jawabannya di kuil. Kini Shiori duduk di depan papan tanpa satu bidak pun."
    else:
        nar "Biasanya Shiori sudah menata bidak sebelum siapa pun datang. Hari ini papannya kosong."
    call kk_family_menu("S16", ["Hampiri kursi di seberangnya.", "Tunggu di pintu sampai ia bicara.", "Terus berjalan menuju festival."])
    if _return == "A":
        nar "Kau duduk dan menanyakan apakah ia ingin berbicara. Shiori tersenyum, lalu menggeleng. Kali ini ia tidak memberikan permainan sebagai jalan memutar menuju hal yang belum bersedia disebut."
        nar "Kau tinggal sampai bel berbunyi. Tidak semua jarak dapat diselesaikan dengan keberanian mendekat sekali."
    elif _return == "B":
        nar "Kau menunggu di pintu. Shiori mengetahui kehadiranmu tetapi tidak memanggil. Setelah bel, ia membereskan kotak tanpa pernah mengisi papan."
        nar "Penantianmu mendapat bentuk, belum mendapat jawaban. Ia belum memilih membiarkanmu masuk lebih jauh dari tempat yang kautentukan sendiri."
    else:
        nar "Kau terus berjalan. Shiori melihatmu lewat dan kembali pada papan kosong. Hari yang biasa dipakai orang lain meminta kepastian kalian lewati tanpa mengucapkan apa pun."
    return

# ┌─ PANDUAN CERITA · S13 · Penemuan
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia menemukan kebohongan pemain atau pengkhianatan pada orang yang ia pedulikan.
# │ INTI    : A mengaku / B menyangkal / C lari.
# │ AKHIRAN : gerbang Rute Revenge (stage 2).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S13:
    call kk_scene_enter("shiori","Klub Catur")
    if any(c["ev"] == "C11" and c["key"] == "B" for c in choices_log):
        shiori "Di pameran itu kau bilang tidak mengenal Shena. Aku sudah membaca bukunya. Mengapa kau mengatakan itu?"
    else:
        shiori "Ada yang tidak cocok antara ceritamu dan yang kutemukan. Aku ingin mendengarnya darimu."
    if kk_has("shiori_alasan_kedua"):
        shiori "Yang itu pun berbeda dari penjelasanmu sesudah pameran."
    nar "Ia tidak menatap seperti sudah mengetahui seluruh isi kepalamu. Justru ruang untuk jawaban yang masih diberikannya membuat kebohongan berikutnya menjadi pilihan yang jelas."
    call kk_family_menu("S13", ["Ceritakan terus terang apa yang kausembunyikan.", "Tetap pada ceritamu semula.", "Bereskan barangmu dan pergi."])
    if _return == "A":
        shiori "Baik. Aku akan mengingat apa yang kaukatakan hari ini juga."
        nar "Kau memberikan penjelasan yang dapat diperiksa, bukan sekadar meminta dipercaya. Shiori tidak langsung tenang, tetapi ia mengajukan pertanyaan berikutnya alih-alih menutup map."
    elif _return == "B":
        nar "Kau bertahan pada cerita lama. Shiori menyebut satu perbedaan, menunggu, lalu berhenti ketika jelas kau memilih menambah penyangkalan daripada menanggapi."
        shiori "Aku sudah mendengar jawabanmu. Sekarang aku akan mencari yang tidak bergantung pada kesediaanmu mengatakan benar."
    else:
        nar "Kau membereskan barang dan pergi. Shiori tidak memaksamu tinggal, hanya meminta jangan menyebut kepergian itu bukti bahwa persoalannya memang tidak layak dibahas."
    return

# ┌─ PANDUAN CERITA · S17 · Keputusan Warisan
# │ LOKASI  : Distrik Elite · Rumah Saionji
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia memutuskan masa depan.
# │ INTI    : A dukung / B ganggu.
# │ AKHIRAN : karier.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S17:
    call kk_scene_enter("shiori","Rumah Saionji")
    if kk_has("shiori_teh_rahasia"):
        shiori "Ibu memberitahuku apa yang kauceritakan saat minum teh. Kali ini biar aku yang bicara."
    elif kk_has("shiori_teh_jujur"):
        shiori "Ibu bilang kau menyuruhnya bertanya padaku. Kemarin akhirnya kami duduk dan bicara."
    elif kk_has("shiori_teh_sanjung"):
        shiori "Rupanya Ibu mengira aku tak pernah sendirian di kampus. Aku sudah bicara dengannya."
    shiori "Orang tuaku ingin tahu peran apa yang kuinginkan di perusahaan. Mereka memberi ruang memilih. Aku tidak mau menjawab asal terdengar mampu lalu menjalani sesuatu yang sebenarnya tidak kupahami."
    nar "Ia menunjukkan rencana dengan bagian yang belum pasti tetap terlihat. Kepercayaan keluarga membuatnya berani meminta waktu, bukan menutup semua keraguan dengan ambisi."
    call kk_family_menu("S17", ["Dengarkan sampai ia selesai menyampaikan rencananya.", "Potong penjelasannya dan ajukan rencanamu sendiri."])
    if _return == "A":
        nar "Kau mendengar sampai selesai, lalu bertanya pada bagian yang belum jelas. Shiori mengubah satu kesimpulan setelah pembicaraan, senang karena didukung tidak harus berarti seluruh pikirannya disetujui."
        shiori "Terima kasih. Aku ingin punya orang yang bisa berkata belum cukup jelas tanpa takut kehilangan tempat di dekatku."
    else:
        shiori "Tunggu. Aku belum selesai."
        nar "Kau menyisipkan rencanamu sebelum ia menyelesaikan miliknya. Shiori menghentikan penjelasan dan meminta kembali ruang yang baru saja dipercayakan kepadamu."
    return

init 1 python:
    def kk_saionji_dinner():
        kk_npc_rel["hari_natal_saionji"] = kk_elapsed_days

    def kk_shiori_early_truth():
        kk_adj("daftar_kebohongan_shiori",-1)
        kk_adj("ujian_lulus_shiori",1)
        if any(c["ev"] == "C11" and c["key"] == "B" for c in choices_log):
            kk_flag("shiori_tahu_shena")

    def kk_shiori_winter():
        kk_stage("shiori",max(3,stage.get("shiori",0)))

    def kk_shiori_admission():
        small = kk_get("daftar_kebohongan_shiori") == 1 and not kk_has("shiori_alasan_kedua")
        kk_adj("daftar_kebohongan_shiori",-1)
        if not small:
            kk_shiori_revenge()

    def kk_shiori_revenge():
        kk_stage("shiori",max(2,stage.get("shiori",0)))
        if kk_has("shiori_alasan_kedua"):
            kk_adj("daftar_kebohongan_shiori",2)
        if kk_host == "chiasa" and any(c["ev"] == "C11" and c["key"] == "B" for c in choices_log):
            kk_flag("shiori_menemukan_kebohongan_shena")

    _hook("S07-A",kk_saionji_dinner)
    _hook("S-D08-A",lambda: kk_flag("shiori_teh_jujur"))
    _hook("S-D08-B",lambda: kk_flag("shiori_teh_sanjung"))
    _hook("S-D08-C",lambda: kk_flag("shiori_teh_rahasia"))
    def kk_shiori_friendship():
        kk_flag("shiori_teman_dipercaya")
        kk_rel("shiori","trust",5)

    _hook("S09-A",kk_shiori_friendship)
    _hook("S09-C",lambda: kk_rel("shiori","trust",-5))
    _hook("S-D04-A",kk_shiori_early_truth)
    _hook("S-D04-B",lambda: kk_flag("shiori_alasan_kedua"))
    _hook("S14-A",lambda: (kk_shiori_winter(),kk_flag("shiori_mendengar_maaf")))
    _hook("S14-B",kk_shiori_winter)
    _hook("S14-C",kk_shiori_winter)
    _hook("S15-A",lambda: kk_flag("shiori_doa_ditanya"))
    _hook("S16-A",kk_shiori_winter)
    _hook("S16-B",kk_shiori_winter)
    _hook("S16-C",kk_shiori_winter)
    _hook("S13-A",kk_shiori_admission)
    _hook("S13-B",kk_shiori_revenge)
    _hook("S13-C",kk_shiori_revenge)
    _hook("S17-A",lambda: kk_flag("shiori_warisan_didukung"))

# ┌─ PANDUAN CERITA · S-D09 · Papan yang Ditinggalkan
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : tahap 3
# │ INTI    : A Lanjutkan dengan satu langkah / B bereskan / C tinggalkan
# │ AKHIRAN : langkah balasan bisa menjadi pengakuan; S20 datang lebih awal
# └─ tulis / perbaiki dialog di bawah ──
label kk_inspect_board(place):
    if not kk_unfinished_board(place):
        return
    nar "Papan yang ditinggalkan Shiori mengulang posisi yang pernah dibahas bersama. Ada jawaban yang saat itu tidak kauambil karena risikonya, bukan karena tak melihatnya. Kini bidak itu menunggu tanpa pemiliknya berada di hadapanmu."
    call kk_family_menu("S-D09", ["Balas dengan langkah yang dulu urung kaumainkan.", "Masukkan bidak ke dalam kotaknya.", "Biarkan papan tetap seperti itu."])
    if _return == "A":
        nar "Kau membiarkan bidak itu di petaknya yang baru. Kali ini Shiori bisa melihat jawabanmu ketika ia kembali."
        nar "Itu belum percakapan yang lengkap. Setidaknya kau memilih meninggalkan sesuatu yang bisa dibaca sebagai tanggung jawab atas langkahmu sendiri, alih-alih menunggu semua pertanyaan dimulai olehnya."
    elif _return == "B":
        nar "Kau memasukkan bidak ke kotak, memutuskan pertandingan yang belum selesai tidak perlu diteruskan. Ketika kembali, Shiori akan menemukan meja rapi dan satu cara berbicara yang tidak lagi tersedia."
    else:
        nar "Kau membiarkan papan tetap seperti itu. Posisi tersebut tidak memburuk, tidak pula mendapatkan jawaban. Waktu yang berjalan di luar papan tidak tunduk pada kesabaran kayu-kayu kecil di atasnya."
    $ kk_minutes(10)
    return

# ┌─ PANDUAN CERITA · S18 · Hujan Terakhir: Pengumpulan Bukti
# │ LOKASI  : Distrik Elite · Rumah Saionji
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia mengumpulkan.
# │ INTI    : A hapus bukti / B perbaiki / C tidak peduli.
# │ AKHIRAN : stage 4; titik tanpa balik setelah ini hanya ending Distorted/Bad.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S18:
    call kk_scene_enter("shiori","Rumah Saionji saat hujan")
    if kk_has("shiori_langkah_balasan"):
        shiori "Aku lihat langkah yang kautinggalkan di klub. Sekarang aku ingin mendengar jawabanmu sendiri."
    else:
        shiori "Aku ingin mendengar jawabanmu sebelum aku meneruskan ini."
    nar "Map di meja berisi catatan yang bisa mengubah cara orang lain membaca perbuatanmu. Shiori menutupnya, mengatakan masih memberi kesempatan meluruskan kepada pihak yang dirugikan, lalu keluar sebentar menemui keluarganya."
    call kk_family_menu("S18", ["Masuk tanpa izin untuk menghapus catatan itu.", "Luruskan ceritamu kepada orang yang ikut dirugikan.", "Biarkan catatan itu dan pulang."])
    if _return == "A":
        "Kuroiwa" "Anda tidak diizinkan masuk ke ruangan ini."
        nar "Ia menghentikanmu sebelum berkas itu hilang. Sekarang ia juga tahu apa yang hendak kaulakukan."
        nar "Shiori kembali setelah dipanggil. Ia tidak tampak terkejut oleh niatmu, tetapi kecewanya terlihat pada jeda sebelum ia menanyakan apakah masih ada penjelasan yang hendak kaupertahankan."
    elif _return == "B":
        if kk_has("shiori_menemukan_kebohongan_shena"):
            nar "Kau menelepon Mio sendiri. Kau menceritakan apa yang sebenarnya kaukatakan tentang Shena, tanpa meminta Shiori menutupinya."
        else:
            nar "Kau menghubungi orang yang dirugikan dan meluruskan ceritamu, kali ini atas namamu sendiri."
        nar "Kau tidak meminta Shiori menanggung malu atau amarah yang muncul dari koreksi itu. Ia mendengar cukup banyak untuk mengetahui bahwa kali ini ada akibat yang bersedia kauhadapi tanpa lebih dahulu mencari cara agar tampak menang."
    else:
        nar "Kau pulang tanpa menanggapi. Map tetap di meja dan kesempatan terakhir untuk menjelaskan sendiri tidak otomatis ikut pulang bersamamu."
        nar "Di luar, hujan tidak cukup deras untuk menahanmu. Kau tidak punya kebetulan yang dapat disalahkan atas keputusan pergi."
    return

init 1 python:
    def kk_shiori_files():
        kk_stage("shiori",max(4,stage.get("shiori",0)))

    def kk_shiori_intrusion():
        kk_shiori_files()
        kk_flag("saionji_masuk_tanpa_izin")

    _hook("S18-A",kk_shiori_intrusion)
    _hook("S18-B",lambda: kk_flag("shiori_koreksi_disampaikan"))
    _hook("S18-C",kk_shiori_files)
    _hook("S-D09-A",lambda: kk_flag("shiori_langkah_balasan"))
