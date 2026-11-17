# Yutaka host, menjaga penyamaran (Y02, Y05, Y10). Pemain menghuni tubuh Yutaka;
# tingkah yang meleset dari Yutaka asli menaikkan kecurigaan. Event host (fire saat masuk lokasi).
# Variabel curiga_* mengikuti Event_Yutaka; angka adalah setelan prototipe.
init 1 python:
    def kk_suspect(who, delta):
        key = "curiga_" + who
        pts.setdefault(key, 0)
        kk_adj(key, delta)

# ┌─ PANDUAN CERITA · Y02 · Kunci yang Tidak Ada
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : kunjungan pertama ke rumah Amamiya.
# │ INTI    : A bunyikan bel dan sopan / B masuk seolah rumah sendiri / C mengabari dulu.
# │ AKHIRAN : B memicu curiga Chiasa/Koita (Yutaka asli tidak punya kunci cadangan ).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y02:
    call kk_scene_enter("yutaka", "Rumah Amamiya")
    nar "Di depan rumah Amamiya, tubuhmu berhenti dengan keakraban yang tidak kaumiliki. Kau tahu Yutaka sering makan di sini, tetapi tidak tahu apakah ia biasa datang tanpa kabar. Dari balik pintu terdengar Koita tertawa. Kehangatan yang mudah dibayangkan dari luar mendadak terasa seperti ruangan yang bisa kaurusak hanya dengan salah masuk."
    call kk_family_menu("Y02", ["Bunyikan bel dan bersikap sopan.", "Masuk saja seolah rumah sendiri.", "Kabari dulu sebelum datang."])
    if _return == "A":
        nar "Chiasa membuka pintu dan menanyakan apakah kau sudah makan. Kau mengikuti kebiasaan bertamu: menunggu dipersilakan, melepas sepatu, mengucapkan salam. Koita menyuruhmu mengambil gelas sendiri. Penerimaan itu terasa ringan bagi mereka dan nyaris menyakitkan bagimu; kau baru saja dipersilakan masuk ke kehidupan seorang sahabat."
    elif _return == "B":
        nar "Kau meraih pintu seolah memiliki hak untuk membukanya. Chiasa muncul dari dalam dan berhenti ketika melihat gerakanmu. Ia bertanya sejak kapan kau merasa tidak perlu mengetuk. Tidak ada kunci cadangan di sakumu, tidak ada ingatan yang bisa menyelamatkan jawaban. Koita menyela dengan ajakan masuk, tetapi tatapan Chiasa belum berubah hangat."
    else:
        nar "Kau mengirim pesan lebih dulu. Balasan Koita datang bersama permintaan membeli minuman, seolah tidak ada yang luar biasa dari kedatanganmu. Ketika Chiasa membukakan pintu, ia langsung mengambil belanjaan. Kepastian kecil tentang kapan orang mengharapkanmu memberi kelegaan yang tidak bisa dibeli apartemen mewahmu."
    return

# ┌─ PANDUAN CERITA · Y05 · Turnamen Game: Skill yang Hilang
# │ LOKASI  : Distrik Elite · Apartemen Yutaka
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Nagisa menantang main game; Yutaka asli pro, pemain tidak.
# │ INTI    : A pura-pura mengalah / B kalah terang-terangan / C latihan dulu.
# │ AKHIRAN : B memicu curiga ("Yutaka tidak pernah kalah").
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y05:
    call kk_scene_enter("yutaka", "Apartemen Yutaka")
    nar "Nagisa memilih permainan yang sudah tersimpan di konsolmu. Ia bicara sambil memasang pengaturan, percaya bahwa kau hafal lebih banyak daripada dirinya. Nama akun Yutaka tampak di antara catatan skor. Jari-jarimu mengenali cara memegang pengendali, tetapi keputusan cepat yang membuatnya hebat tidak ikut diwariskan."
    call kk_family_menu("Y05", ["Pura-pura mengalah agar terlihat wajar.", "Kalah terang-terangan saja.", "Minta waktu latihan dulu."])
    if _return == "A":
        nagisa "Kau mengalah, ya? Aku ingin menang, tapi bukan menang yang dibungkus kado begini. ...Sudah, ronde berikutnya jangan terlalu sibuk menjaga perasaanku."
    elif _return == "B":
        nagisa "Tunggu. Itu bukan salah tekan biasa. Kau kelihatan tidak tahu harus melakukan apa. Aku tidak sedang mengejek, Yuu-kun. Akhir-akhir ini ada apa?"
    else:
        nagisa "Minta latihan dulu? Biasanya kau yang menyuruhku pemanasan. ...Ya sudah. Aku mau tanding sama orang yang siap main, bukan orang yang panik menjaga reputasi."
    return

# ┌─ PANDUAN CERITA · Y10 · Jam Tangan Hadiah
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Yutaka menerima jam tangan dari Daisuke seperti tahun lalu.
# │ INTI    : A simpan / B pakai / C kembalikan.
# │ AKHIRAN : Daisuke menilai sikap.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y10:
    call kk_scene_enter("yutaka", "Rumah Amamiya")
    nar "Daisuke menyerahkan kotak jam tipis. Ia menyebut jam tahun lalu dan tertawa tentang betapa sering Yutaka memakainya. Kau baru memahami bahwa benda itu bukan hadiah mahal dari relasi keluarga; seseorang di rumah ini memperhatikan apa yang melekat di pergelangan seorang anak yang bukan anaknya."
    call kk_family_menu("Y10", ["Simpan dengan hati-hati dan berterima kasih.", "Pakai langsung di pergelanganmu.", "Kembalikan karena merasa terlalu berharga."])
    if _return == "A":
        nar "Kau mengucapkan terima kasih dan menyimpan kotaknya dengan hati-hati. Daisuke mengatakan hadiah itu untuk dipakai sesukamu, bukan untuk dipajang demi menyenangkan pemberi. Kau mengangguk, malu karena sempat menganggap percakapan ini sekadar ujian yang harus dilalui."
    elif _return == "B":
        nar "Kau memakainya, lalu mengangkat pergelangan untuk menunjukkan hasilnya. Daisuke tersenyum dan membetulkan letak kotak kosong di meja. Untuk sesaat ia tidak memeriksa apa pun tentang dirimu. Ia hanya tampak senang hadiah yang dipilihnya disukai."
    else:
        nar "Kau mengembalikan kotak itu karena merasa tak berhak menerima sesuatu seberharga ini. Daisuke menerimanya perlahan. Ia tidak tersinggung oleh kesopananmu, tetapi bertanya apakah ada yang membuatmu tidak nyaman di rumah mereka. Chiasa memandangmu, terkejut oleh jarak yang baru saja kauciptakan."
    return

init 1 python:
    _hook("Y02-A", lambda: kk_suspect("chiasa", -3))
    _hook("Y02-B", lambda: kk_suspect("chiasa", 10))
    _hook("Y05-A", lambda: kk_rel("nagisa","trust",2))
    _hook("Y05-B", lambda: kk_suspect("nagisa", 12))
    _hook("Y10-A", lambda: kk_flag("daisuke_setuju"))
    _hook("Y10-B", lambda: kk_flag("daisuke_setuju"))
    _hook("Y10-C", lambda: kk_suspect("chiasa", 5))
