# Cleanup milestone berdiri sendiri: Harumi H20 (teh
# terakhir), H21 (pengumuman studi), H23 (ujian akhir); Moeka Mo07 (peragaan
# pertama). Node "Pilihan X" (menu kosong) ditangani sebagai resolver ending,
# bukan di sini. Konsekuensi + karakter. Mengikuti Event_Harumi / Event_Moeka.

# ┌─ PANDUAN CERITA · H20 · Teh Terakhir
# │ LOKASI  : Kampus Kouseikan · Perpustakaan Pusat
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : ia menyeduh teh lagi.
# │ INTI    : A minum / B menolak / C menahan pergi.
# │ AKHIRAN : simbol kembali.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H20:
    call kk_scene_enter("harumi", "Perpustakaan Pusat · Teh terakhir")
    nar "Harumi meletakkan cangkir di meja yang pernah kalian pakai membaca bersama. Aroma tehnya sama; cara ia menawarkan kini lebih hati-hati, tidak lagi yakin sebuah kebiasaan lama otomatis masih diterima."
    harumi "Aku menyeduh lagi. Aku ingin membaginya denganmu. Kalau tidak mau, aku tetap ingin mengatakannya dengan jelas."
    call kk_family_menu("H20", ["Minum teh itu bersamanya.", "Menolak teh itu.", "Menahan ia agar tidak pergi."])
    if _return == "A":
        harumi "Kau meminumnya. ...Simbol yang kembali. Aku senang sebagian dari dulu masih ada."
        nar "Kau menyebut rasanya, lalu bertanya bagaimana ia belakangan. Harumi tidak perlu menjadikan satu cangkir bukti bahwa semua yang pernah berubah sudah kembali."
        harumi "Aku belum tahu cara merangkum. Tapi aku bisa mulai dari hari ini."
    elif _return == "B":
        nar "Kau menolak. Harumi menurunkan cangkir, berusaha menerima satu jawaban tanpa segera mengubahnya menjadi penilaian atas seluruh kedekatan kalian."
        harumi "Baik. Terima kasih sudah bilang. Aku tidak ingin kamu meminumnya karena takut membuatku sedih."
        nar "Ia tetap sedih sedikit. Kali ini ia membiarkan rasa itu ada tanpa menagih perubahan jawabanmu."
    else:
        harumi "Kau menahanku? ...Itu bukan logika. Dan justru karena itu, aku ingin tinggal sebentar lagi."
        nar "Kau meminta waktu tambahan, bukan menghalangi langkahnya. Harumi memeriksa jadwal, lalu memilih duduk."
        harumi "Dua puluh menit. Aku ingin tinggal, dan sesudahnya tetap harus pergi. Aku rasa dua hal itu boleh benar bersama."
    return

# ┌─ PANDUAN CERITA · H21 · Pengumuman Studi
# │ LOKASI  : Kampus Kouseikan · Perpustakaan Pusat
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : beasiswa luar negeri.
# │ INTI    : A dukung pergi / B minta tinggal / C ikut.
# │ AKHIRAN : ending Harumi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H21:
    call kk_scene_enter("harumi", "Perpustakaan Pusat · Pengumuman studi")
    nar "Harumi menunjukkan surat penerimaan dengan tangan yang sulit diam. Ia sudah membaca syaratnya, tetapi masih perlu mendengar dirinya sendiri mengatakan diterima."
    harumi "Ini jalan yang kuinginkan. Aku senang. Aku juga memikirkan jarak dari orang-orang di sini. Aku ingin mendengar keinginanmu, tetapi keputusannya harus tetap bisa kuambil sendiri."
    call kk_family_menu("H21", ["Dukung ia pergi mengejar studinya.", "Minta ia tinggal, dengan jujur.", "Tawarkan ikut bersamanya."])
    if _return == "A":
        harumi "Kau mendukungku pergi, meski itu menjauhkan kita? ...Itu bentuk kepercayaan yang paling bersih."
        nar "Ia mulai membicarakan laboratorium tujuan, bukan hanya kesulitan pergi. Kehadirannya mendadak lebih hidup ketika harapannya boleh terlihat tanpa lebih dahulu meminta maaf karena akan jauh."
    elif _return == "B":
        harumi "Kau memintaku tinggal—sebagai dirimu, bukan sebagai saran. ...Aku akan menimbang itu dengan sungguh-sungguh."
        nar "Ia menanyakan seperti apa masa depan yang kaubayangkan jika ia tinggal. Pertanyaan itu tidak bisa dijawab hanya dengan rindu; ada cita-cita yang perlu mendapat tempat nyata, bukan pujian bahwa ia rela berkorban."
    else:
        harumi "Kau mau ikut? ...Variabel itu tidak kuperhitungkan. Dan ternyata, ia mengubah seluruh persamaan."
        nar "Setelah terkejut, ia meminta kalian membahas pekerjaanmu, izin tinggal, dan uang sebelum menyebutnya janji. Gembira tidak membuatnya ingin mengabaikan akibat yang akan kalian tanggung berdua."
    return

# ┌─ PANDUAN CERITA · H23 · Ujian Akhir
# │ LOKASI  : Kampus Kouseikan · Perpustakaan Pusat
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : ujian skripsi.
# │ INTI    : A bantu / B ganggu / C hadir.
# │ AKHIRAN : hasil akademik.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H23:
    call kk_scene_enter("harumi", "Perpustakaan Pusat · Ujian skripsi")
    nar "Harumi menyusun kartu presentasi menurut urutan yang sudah dihafal. Ia terus mengubah posisi kartu kedua dan ketiga, meski keduanya menjelaskan hal yang sama."
    harumi "Aku bisa menjawab pertanyaan tentang penelitian. Yang membuatku takut adalah merasa mereka sedang memutuskan apakah seluruh diriku cukup. Aku tahu skripsi tidak seharusnya berarti itu."
    call kk_family_menu("H23", ["Bantu ia mempersiapkan pembelaannya.", "Ganggu persiapannya.", "Sekadar hadir mendukungnya."])
    if _return == "A":
        harumi "Kau menemaniku berlatih sampai larut? ...Dengan begini, aku menghadapi panel itu tidak sendirian."
        nar "Kau memintanya menjelaskan kepada seseorang yang belum tahu seluruh riset. Ketika ia tersendat, kalian mengulang bagian itu tanpa menyebutnya kegagalan."
        harumi "Aku tidak perlu terdengar sempurna agar orang bisa mengikuti. Itu berguna sekali untuk diingat sebelum masuk ruangan."
    elif _return == "B":
        nar "Kau mengganggu waktu yang disiapkannya untuk latihan. Harumi mencoba menyesuaikan, lalu kehilangan urutan yang tadi sudah ia pahami."
        harumi "Aku perlu berhenti melayanimu sekarang. Ini penting bagiku."
        nar "Ia akhirnya mengatakan batas itu, tetapi gugup yang bertambah tetap ikut dibawa ketika kembali membuka kartu."
    else:
        harumi "Kau hadir di hari itu? ...Satu wajah yang kukenal di antara panel asing. Itu sudah menurunkan satu variabel ketakutan."
        nar "Kau menunggu di tempat yang diperbolehkan. Sebelum masuk, ia menoleh sekali dan tersenyum kecil, kemudian berjalan menuju ujian yang tetap harus ia jalani sendiri."
    return

# ┌─ PANDUAN CERITA · Mo07 · Peragaan Pertama
# │ LOKASI  : Kampus Kouseikan · Kantin Pusat
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : ia tampil.
# │ INTI    : A hadir / B bantu backstage / C absen.
# │ AKHIRAN : reputasi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo07:
    call kk_scene_enter("moeka", "Kantin Pusat · Peragaan pertama")
    nar "Moeka memeriksa pakaian pertama peragaannya dengan jari yang terus berhenti pada jahitan yang sama. Di depan orang lain ia sudah menjanjikan pertunjukan seru; kepadamu ia akhirnya mengaku takut."
    moeka "Ini kerjaan, tapi ini juga hasil yang ingin kubanggakan. Aku capek kalau setiap hal yang kusukai langsung berubah jadi harus berhasil demi semua orang. Malam ini boleh gugup dulu, ya?"
    call kk_family_menu("Mo07", ["Hadir untuk menontonnya.", "Bantu ia di belakang panggung.", "Absen dari acara itu."])
    if _return == "A":
        moeka "Kau datang menonton? ...Kalau aku tahu ada satu wajah yang kukenal, mungkin aku tidak akan gemetar."
        nar "Kau mengatakan tempat dudukmu dan tinggal sampai acara selesai. Di panggung ia tidak kehilangan seluruh gugup, tetapi menemukan arah untuk melihat ketika lampu membuat wajah penonton lain sukar dikenali."
    elif _return == "B":
        moeka "Kau bantu di backstage? ...Tangan ini lebih tenang kalau ada yang menahannya sedetik."
        nar "Kau menanyakan pekerjaan yang dapat dibagi dan membantu tanpa mengubah keputusan desainnya. Sebelum mulai, ia memberi tahu bahwa sentuhan singkat di tangan boleh, lalu menarik napas dan mengembalikan tangannya untuk bekerja."
    else:
        nar "Kau tidak hadir. Moeka tetap tampil, menuntaskan langkah yang sudah dilatih dan tersenyum saat diminta. Sesudahnya ia memotret amplop bayaran untuk memastikan dirinya mengingat apa yang sudah berhasil."
        nar "Foto itu tidak memperlihatkan siapa yang ingin ia temui setelah turun panggung. Ia pulang dengan letih, bangga sedikit, dan kecewa yang belum tentu ingin diakui."
    return

init 1 python:
    _hook("H20-A", lambda: kk_rel("harumi","intim",5))
    _hook("H20-B", lambda: kk_rel("harumi","trust",-3))
    _hook("H20-C", lambda: (kk_rel("harumi","intim",4), kk_adj("kejelasan_harumi",5)))
    _hook("H21-A", lambda: (kk_rel("harumi","trust",6), kk_flag("harumi_studi_didukung")))
    _hook("H21-B", lambda: (kk_adj("kejelasan_harumi",6), kk_flag("harumi_diminta_tinggal")))
    _hook("H21-C", lambda: (kk_rel("harumi","intim",6), kk_flag("harumi_diikuti")))
    _hook("H23-A", lambda: (kk_rel("harumi","trust",5), kk_flag("harumi_ujian_dibantu")))
    _hook("H23-B", lambda: kk_rel("harumi","trust",-5))
    _hook("H23-C", lambda: kk_rel("harumi","aff",4))
    _hook("Mo07-A", lambda: (kk_rel("moeka","aff",5), kk_flag("moeka_peragaan_dihadiri")))
    _hook("Mo07-B", lambda: (kk_rel("moeka","intim",5), kk_adj("stres_moeka",-5)))
    _hook("Mo07-C", lambda: kk_rel("moeka","aff",-3))
