# Dialog penghubung draft editorial dari Event_Harumi dan Alur_Cabang/03.
# ┌─ PANDUAN CERITA · H01 · Perpustakaan Sains
# │ LOKASI  : Kampus Kouseikan · Gedung Sains & Lab
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : ia menyendiri membaca.
# │ INTI    : A duduk bersebelahan / B tanya soal / C abaikan.
# │ AKHIRAN : A membuka percakapan akademik.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H01:
    call kk_scene_enter("harumi", "Perpustakaan sains")
    nar "Harumi menahan halaman buku dengan satu jari dan mengulang sebuah perhitungan pada kertas terpisah. Di sebelahnya kursi kosong ditarik sedikit keluar, tak jelas bekas seseorang pergi atau tawaran yang belum diucapkan."
    harumi "Kalau mencari buku itu, ada satu salinan lagi di rak. Kalau mencari tempat duduk... yang ini belum dipakai."
    call kk_family_menu("H01", ["Tarik kursi dan duduk di sampingnya.", "Tanyakan soal yang sedang ia baca.", "Lewati mejanya agar ia bisa membaca sendiri."])
    if _return == "A":
        harumi "Kalau mau lihat, bukunya bisa kugeser ke tengah."
        nar "Ia benar-benar menggesernya, lalu menunggu sampai kau menemukan baris yang sedang dibaca. Gerakan sabar itu lebih hangat daripada perkenalan yang biasanya diucapkan orang."
        harumi "Aku tidak keberatan dijeda. Hanya perlu diberi tahu bahwa ada pertanyaan."
    elif _return == "B":
        harumi "Sebentar. Aku masih memeriksa jawabannya."
        nar "Ia memintamu menunggu bukan untuk menunjukkan kepandaian, melainkan karena tak ingin menjelaskan kesimpulan yang belum ia percaya sendiri. Setelah selesai, ia memutar kertas agar bisa kaubaca."
        harumi "Bagian mana yang ingin kamu tahu dulu? Aku sering mulai terlalu jauh kalau tidak ditanya."
    else:
        nar "Kau melanjutkan langkah. Harumi kembali membaca setelah satu pandangan singkat memastikan kau tidak sedang membutuhkan sesuatu."
        nar "Kursi itu tetap kosong. Kau melewatkan kesempatan yang tidak akan ia panggil kembali dengan suara keras di perpustakaan."
    return

# ┌─ PANDUAN CERITA · H08 · Omikuji Harumi
# │ LOKASI  : Alam & Pantai · Kuil
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : ramalan "perhatikan hatimu".
# │ INTI    : A bantu menafsirkan / B tertawakan.
# │ AKHIRAN : kejelasan emosi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H08:
    call kk_scene_enter("harumi", "Kuil · Tahun baru")
    nar "Harumi membacakan ramalannya dengan nada yang biasa dipakai menguji petunjuk praktikum. Bagian studi cukup jelas. Bagian cinta membuatnya membaca tiga kali."
    harumi "Perhatikan hatimu. Kalau itu perintah, kriterianya sangat buruk. Tapi aku ingin tahu maksudnya. Aku sering baru mengerti sedang sedih setelah semua orang pergi."
    menu:
        "Bantu ia mencari arti kalimat itu.":
            $ kk_record_choice("H08", "A")
            harumi "Jadi aku boleh mulai dari apa yang kurasakan sekarang?"
            nar "Kau menawarkan mulai dari hal kecil: ingin mendekat atau menjauh, merasa lega atau takut, tanpa harus langsung menemukan nama yang paling tepat. Harumi memandang kerumunan, lalu memilih berdiri sedikit lebih dekat kepadamu."
            harumi "Aku ingin tetap di sini sebentar. Itu sudah informasi, ya."
        "Tertawakan betapa samarnya petunjuk itu.":
            $ kk_record_choice("H08", "B")
            nar "Kau tertawa tentang petunjuk yang dapat berarti apa saja. Harumi ikut mengakui ketidakjelasannya, lalu menyimpan kertas tersebut."
            nar "Ia tidak menanyakan bagian yang sesungguhnya ingin dipahami lagi. Pertanyaan yang mudah ditertawakan rupanya belum tentu mudah diberikan untuk kedua kali."
    return

# ┌─ PANDUAN CERITA · H09 · Hipotesis Cinta
# │ LOKASI  : Kampus Kouseikan · Gedung Sains & Lab
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : ia mencatat perasaannya sebagai data.
# │ INTI    : A bantu mengidentifikasi / B menertawakan / C menjauh.
# │ AKHIRAN : stage 1 (kekosongan emosi).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H09:
    call kk_scene_enter("harumi", "Gedung Sains & Lab")
    nar "Catatan Harumi memuat percakapan singkat dengan Koita dan reaksi tubuhnya sesudahnya: sulit berkonsentrasi, ingin bicara lagi, kecewa ketika undangan dibatalkan. Kolom perasaan sengaja dibiarkan kosong."
    harumi "Aku takut kalau memberi nama, aku akan mulai memilih data yang mendukungnya. Tapi membiarkan kosong juga membuatku terus bertanya apakah semuanya hanya kesalahan."
    if kk_has("harumi_menafsirkan_omikuji"):
        harumi "Di kuil waktu itu kau menyuruhku memperhatikan bagian ini."
    call kk_family_menu("H09", ["Bantu ia mencari kata yang sesuai dengan perasaannya.", "Tertawakan usahanya mencatat perasaan.", "Kembalikan buku itu dan ambil jarak."])
    if _return == "A":
        harumi "Bukan variabel yang salah. Aku memang merasa begitu."
        nar "Kau menawarkan beberapa kata dan membiarkan ia menolak yang tidak sesuai. Harumi memilih rindu, lalu mengubahnya menjadi ingin ditemani."
        harumi "Yang kedua lebih tepat hari ini. Aku tidak harus memutuskan arti seluruh hubungannya untuk mengakui satu perasaan ini."
    elif _return == "B":
        harumi "Begitu. Berarti bagian itu tidak perlu kubahas denganmu."
        nar "Ia tidak mengucapkannya dengan marah. Buku ditarik mendekat, dan percakapan berikutnya hanya tentang hal-hal yang bisa dinilai tanpa menyerahkan sesuatu dari dirinya."
    else:
        nar "Kau mengembalikan buku dan memberi jarak. Harumi menerima, lalu menyimpan halaman yang tadi berharap bisa dibaca bersama."
        harumi "Baik. Aku coba sendiri dulu."
        nar "Suara tenangnya tidak memberitahumu apakah ia membutuhkan ruang atau sedang belajar bahwa kebutuhan untuk dimengerti sebaiknya tidak diajukan kepadamu."
    return

# ┌─ PANDUAN CERITA · H-D01 · Teh Jam Satu
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kujo Harumi
# │ AWALAN  : Larut; dapur asrama (Chiasa bisa masuk, Yutaka hanya di luar jendela); kejelasan ≥ 30
# │ INTI    : A minum dan diam / B tanya perasaannya / C bercerita tentang dirimu
# │ AKHIRAN : kejelasan +
# └─ tulis / perbaiki dialog di bawah ──
label kk_dorm_tea:
    if kk_host == "chiasa":
        call kk_scene_enter("harumi", "Dapur asrama")
        nar "Di dapur asrama Harumi menyisakan satu cangkir untukmu."
    else:
        call kk_scene_enter("harumi", "Di luar jendela dapur asrama")
        nar "Kau tetap di luar. Harumi mengulurkan cangkir lewat jendela dapur."
    harumi "Masih hangat. Hati-hati. Aku menyeduh lebih banyak setelah tahu kamu belum tidur. Itu memang disengaja."
    nar "Ia menunggu kau memegang cangkir dengan aman sebelum menarik tangan. Kebaikan kecil itu tidak diikuti permintaan bantuan atau alasan akademik untuk tetap berada di dekatmu."
    call kk_family_menu("H-D01", ["Minum bersamanya dalam diam.", "Tanyakan apa yang ia rasakan malam ini.", "Ceritakan apa yang membuatmu masih terjaga."])
    if _return == "A":
        nar "Untuk beberapa saat kalian hanya mendengar air di ketel. Harumi tampak akan bertanya, lalu mengurungkannya karena keheningan ternyata tidak terasa salah."
        harumi "Aku tadinya menyiapkan topik supaya kamu tidak bosan. Mungkin kita boleh melewatkan satu topik tanpa kehilangan alasan untuk duduk bersama."
    elif _return == "B":
        harumi "Aku sedang mencoba mencari kata yang tepat. Tenang, mungkin. Tapi juga ingin waktu bergerak lebih lambat."
        nar "Ia memandang cangkirnya, kemudian dirimu."
        harumi "Aku tidak ingin buru-buru menyebutnya cinta hanya agar ada jawaban. Aku ingin mengenali yang ini dulu."
    else:
        harumi "Aku mendengarkan. Kamu tidak perlu menyederhanakan kalau belum tahu kesimpulannya."
        nar "Kau bercerita dan beberapa kali berhenti tanpa urutan yang jelas. Harumi tidak mengoreksi. Sesudahnya ia menyampaikan satu hal yang didengarnya, lalu bertanya apakah ia memahami dengan benar."
    $ kk_minutes(10)
    return

init 1 python:
    _hook("H08-A", lambda: (kk_adj("kejelasan_harumi",10), kk_flag("harumi_menafsirkan_omikuji")))
    _hook("H08-B", lambda: kk_adj("kejelasan_harumi",-5))
    _hook("H09-A", lambda: (kk_adj("kejelasan_harumi",10), kk_flag("harumi_dibantu_menamai_emosi")))
    _hook("H09-B", lambda: (kk_stage("harumi",1), kk_adj("kejelasan_harumi",-5)))
    _hook("H09-C", lambda: kk_stage("harumi",1))
    _hook("H-D01-A", lambda: kk_adj("kejelasan_harumi",5))
    _hook("H-D01-B", lambda: kk_adj("kejelasan_harumi",10))
    _hook("H-D01-C", lambda: kk_adj("kejelasan_harumi",5))


# ┌─ PANDUAN CERITA · H03 · Masakan Eksperimental
# │ LOKASI  : Kampus Kouseikan · Asrama Putri
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : masakannya buruk.
# │ INTI    : A makan semuanya / B jujur / C bantu memasak.
# │ AKHIRAN : C membuka komedi hangat.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H03:
    call kk_scene_enter("harumi", "Asrama Putri")
    nar "Harumi menaruh piring di depanmu bersama catatan resep yang bersih. Hidangannya tampak dapat dikenali, tetapi aromanya membuatmu ingin membaca catatan tersebut lebih dahulu."
    harumi "Aku mengikuti urutannya. Lalu menyesuaikan beberapa jumlah karena kupikir hasilnya lebih efisien. Ternyata resep tidak senang diperlakukan begitu. Coba sedikit?"
    call kk_family_menu("H03", ["Habiskan bagian yang ia tawarkan.", "Jelaskan dengan jujur bagian mana yang terasa aneh.", "Tawarkan membuat percobaan berikutnya bersama."])
    if _return == "A":
        harumi "Sampai habis? Aku masih belum yakin dengan rasanya."
        nar "Ia mencicipi setelah melihatmu bertahan. Ekspresinya tetap datar, tetapi ia segera menggeser piring menjauh dari tanganmu."
        harumi "Cukup. Kesediaanmu makan bukan bukti rasanya baik. Terima kasih, tapi kamu tidak perlu melanjutkan pengorbanan ini."
    elif _return == "B":
        harumi "Berarti ada yang perlu kuubah. Terima kasih sudah mencobanya."
        nar "Ia menuliskan penjelasanmu, kemudian mencoba bagian yang sama agar tidak sekadar menerima penilaian. Kritik yang jelas membuatnya lebih lega daripada pujian yang tidak bisa dipakai memahami hasil."
    else:
        harumi "Dua orang untuk satu percobaan. Kalau begitu kau cicipi dulu, sebelum kutambahkan lagi."
        nar "Kalian berbagi pekerjaan dan berdebat ringan tentang perbedaan cukup garam dengan jumlah yang dapat diukur. Harumi sempat tersenyum sebelum masakannya membaik."
        harumi "Ternyata bagian yang menyenangkan tidak harus menunggu hasil akhirnya. Aku baru tahu."
    return

# ┌─ PANDUAN CERITA · H-D05 · Masakan Kedua
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kujo Harumi
# │ AWALAN  : H03-C pernah terjadi
# │ INTI    : A Puji dengan spesifik / B jujur / C ajak memasak lagi
# │ AKHIRAN : ia menghubungkan "senang" dengan "memasak bersama"; kejelasan +
# └─ tulis / perbaiki dialog di bawah ──
label kk_second_meal:
    nar "Kali ini Harumi menyiapkan porsi lebih kecil dan tidak menaruh catatan resep di meja. Ia ingin mendengar reaksi sebelum menjelaskan apa yang sudah diubah."
    harumi "Aku mengulang masakan kita. Tadi hampir mengirim foto, lalu memutuskan ingin melihatmu mencicipi langsung."
    call kk_family_menu("H-D05", ["Tunjukkan rasa yang kali ini lebih seimbang.", "Katakan dengan jujur apa yang masih kurang.", "Ajak dia memasak bersama lagi."])
    if _return == "A":
        harumi "Kau juga bisa merasakan bedanya. Aku senang."
        nar "Ia mengulang kata senang setelah menyebutnya, seolah memeriksa bahwa akhirnya menemukan nama yang tepat. Lalu ia mengambil porsi sendiri agar tidak hanya duduk menunggu penilaianmu."
    elif _return == "B":
        harumi "Aku ingin mencobanya lagi. Rupanya aku menyukai bagian ini."
        nar "Kritikmu tidak menghapus kegembiraannya kali ini. Ia menanyakan satu perbaikan dan menyisakan sisanya untuk kesempatan lain, tidak lagi menganggap setiap kekurangan harus selesai sebelum ia boleh menikmati makan bersama."
    else:
        harumi "Boleh. Aku lebih senang waktu kita membuatnya bersama."
        nar "Ia tidak mengoreksi kalimat tersebut menjadi alasan teknis. Kalian memilih hari, membagi bahan, dan menyadari jadwal yang disepakati sudah cukup untuk membuatnya tersenyum hari ini."
    $ kk_minutes(10)
    return

init 1 python:
    _hook("H-D05-A", lambda: kk_adj("kejelasan_harumi",10))
    _hook("H-D05-B", lambda: kk_adj("kejelasan_harumi",5))
    _hook("H-D05-C", lambda: kk_adj("kejelasan_harumi",10))

    def kk_harumi_ending():
        if kk_has("lock_romance_harumi"):
            return None
        if kk_has("force_harumi"):
            return "E-HA-12"
        # Koita memilih Harumi (K26).
        if kk_has("koita_pilih_harumi"):
            return "E-HA-04"
        # Rute Ogawa (hanya bila gerbang H06+ ditempuh).
        if kk_has("ogawa_aktif"):
            if kk_get("validasi_pemain", 0) >= 60 and kk_has("harumi_dimanfaatkan"):
                return "E-HA-10"
            if kk_has("ogawa_dihentikan"):
                return "E-HA-03" if kk_has("harumi_tetap_kouseikan") else "E-HA-07"
            if kk_has("ogawa_lolos") or kk_get("cengkeraman_ogawa", 0) >= 60:
                return "E-HA-08"
            if kk_has("harumi_titik_tanpa_balik"):
                return "E-HA-06"
            if kk_has("harumi_menjauh_ogawa") and kk_get("kejelasan_harumi") >= 50:
                return "E-HA-02"
            if kk_has("harumi_dimanfaatkan"):
                return "E-HA-05"
        # Romantis.
        if kk_has("harumi_ikut_luar"):
            return "E-HA-14"
        if kk_host == "chiasa" and kk_has("harumi_chiasa_kolaborasi"):
            return "E-HA-13"
        if (kk_get("kejelasan_harumi") >= 60 and kk_has("harumi_dibantu_menamai_emosi")
                and not kk_has("force_pernah")):
            return "E-HA-01"
        if kk_get("orang_tua_kujo", 30) >= 60 and not kk_has("force_pernah"):
            return "E-HA-09"
        # Netral: kejelasan tinggi tapi hati tidak ke siapa pun.
        if kk_get("kejelasan_harumi") >= 60 and not kk_has("harumi_kencan_biasa"):
            return "E-HA-11"
        return None
