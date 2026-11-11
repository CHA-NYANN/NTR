# Dialog penghubung draft editorial dari Event_Harumi dan Alur_Cabang/03.
label kkscene_H01:
    call kk_scene_enter("harumi", "Perpustakaan sains")
    nar "Di antara rak buku sains Harumi menahan halaman dengan satu jari. Kursi di sampingnya kosong."
    menu:
        "Tarik kursi dan duduk di sampingnya.":
            $ kk_record_choice("H01", "A")
            harumi "Kalau mau lihat, bukunya bisa kugeser ke tengah."
        "Tanyakan soal yang sedang ia baca.":
            $ kk_record_choice("H01", "B")
            harumi "Sebentar. Aku masih memeriksa jawabannya."
        "Lewati mejanya agar ia bisa membaca sendiri.":
            $ kk_record_choice("H01", "C")
            nar "Ia membalik halaman saat kau melewati rak berikutnya."
    return

label kkscene_H08:
    call kk_scene_enter("harumi", "Kuil · Tahun baru")
    harumi "Perhatikan hatimu. Begitu isi ramalannya. Apa yang sebenarnya harus kuperhatikan?"
    menu:
        "Bantu ia mencari arti kalimat itu.":
            $ kk_record_choice("H08", "A")
            harumi "Jadi aku boleh mulai dari apa yang kurasakan sekarang?"
        "Tertawakan betapa samarnya petunjuk itu.":
            $ kk_record_choice("H08", "B")
            nar "Harumi melipat kertas ramalannya dan memasukkannya ke saku."
    return

label kkscene_H09:
    call kk_scene_enter("harumi", "Gedung Sains & Lab")
    harumi "Aku menuliskan apa yang terjadi. Bagian perasaanku masih kosong."
    if kk_has("harumi_menafsirkan_omikuji"):
        harumi "Di kuil waktu itu kau menyuruhku memperhatikan bagian ini."
    menu:
        "Bantu ia mencari kata yang sesuai dengan perasaannya.":
            $ kk_record_choice("H09", "A")
            harumi "Bukan variabel yang salah. Aku memang merasa begitu."
        "Tertawakan usahanya mencatat perasaan.":
            $ kk_record_choice("H09", "B")
            harumi "Begitu. Berarti bagian itu tidak perlu kubahas denganmu."
        "Kembalikan buku itu dan ambil jarak.":
            $ kk_record_choice("H09", "C")
            nar "Ia menutup buku sebelum kau melihat catatan berikutnya."
    return

label kk_dorm_tea:
    if kk_host == "chiasa":
        call kk_scene_enter("harumi", "Dapur asrama")
        nar "Di dapur asrama Harumi menyisakan satu cangkir untukmu."
    else:
        call kk_scene_enter("harumi", "Di luar jendela dapur asrama")
        nar "Kau tetap di luar. Harumi mengulurkan cangkir lewat jendela dapur."
    harumi "Masih hangat. Hati-hati."
    menu:
        "Minum bersamanya dalam diam.":
            $ kk_record_choice("H-D01", "A")
            nar "Untuk beberapa saat kalian hanya mendengar air di ketel."
        "Tanyakan apa yang ia rasakan malam ini.":
            $ kk_record_choice("H-D01", "B")
            harumi "Aku sedang mencoba mencari kata yang tepat."
        "Ceritakan apa yang membuatmu masih terjaga.":
            $ kk_record_choice("H-D01", "C")
            harumi "Aku mendengarkan."
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

