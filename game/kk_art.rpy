# Draft editorial dari Event_Chiasa C05/C09 dan Alur_Cabang/06 §11–12.
label kkscene_C05:
    call kk_scene_enter("chiasa", "Rumah Amamiya")
    nar "Mio menelepon. Untuk jilid yang baru, ia ingin Shena mengerjakan sampulnya lagi."
    menu:
        "Ucapkan terima kasih dan tolak dengan halus.":
            $ kk_record_choice("C05","A")
            nar "Mio menerima jawabanmu. Pekerjaan lama tetap menghasilkan royalti."
        "Ambil proyeknya dan siapkan waktu untuk berlatih.":
            $ kk_record_choice("C05","B")
            nar "Sesudah menutup telepon, kau membuka buku sketsa."
        "Katakan kau perlu mendiskusikannya dengan Haruka.":
            $ kk_record_choice("C05","C")
            nar "Kau mencatat permintaan Mio sebelum mencari Haruka."
    return

label kkscene_C09:
    call kk_scene_enter("chiasa", "Rumah Amamiya")
    nar "Kau membuka buku sketsa. Garis pertama di halaman kosong itu belum seperti yang kauingat dari ilustrasi Shena."
    menu:
        "Mulai lagi dengan latihan sendiri.":
            $ kk_record_choice("C09","A")
            nar "Kau mencoba garis itu beberapa kali, sampai tanganmu mulai mengenal gerakannya."
        "Cari orang lain untuk mengerjakannya.":
            $ kk_record_choice("C09","B")
            nar "Jika ada yang bertanya siapa yang menggambar, kau tahu jawaban itu akan sulit."
        "Tutup bukunya untuk hari ini.":
            $ kk_record_choice("C09","C")
            nar "Halaman itu masih ada ketika kau menyimpan bukunya."
    return

init 1 python:
    def kk_take_cover_project():
        kk_flag("proyek_mio_diterima")
        pts.setdefault("shena_risiko",20)
        kk_adj("shena_risiko",10)

    def kk_practice_sketch(place):
        if not kk_can_sketch(place):
            return
        kk_adj("kemampuan_gambar", 1 if kk_kelelahan_tier()[1] >= 2 else 3)
        pts.setdefault("shena_risiko",20)
        kk_adj("shena_risiko",-1)
        kk_minutes(60)

    _hook("C05-B", kk_take_cover_project)
    _hook("C05-C", lambda: kk_flag("haruka_dimintai_bantuan"))
    _hook("C09-A", lambda: kk_adj("kemampuan_gambar",5))
    def kk_commission_secret():
        kk_flag("ilustrasi_dikerjakan_orang_lain")
        pts.setdefault("shena_risiko",20)
        kk_adj("shena_risiko",10)

    _hook("C09-B", kk_commission_secret)

label kk_draw_at_home:
    if not kk_can_sketch(_lokasi):
        return
    if kk_shaking_hands():
        nar "Garis yang kau tarik bergeser di ujungnya. Jari-jarimu gemetar."
        menu:
            "Letakkan pensil dan beristirahat.":
                $ kk_record_choice("C-D03","A")
                call kk_rest_home
                return
            "Teruskan sampai pagi.":
                $ kk_record_choice("C-D03","B")
                $ kk_adj("kemampuan_gambar",1)
                $ kk_minutes((6 - kk_slot)*240 - kk_minute)
                nar "Pagi datang. Hanya sedikit garis yang ingin kausimpan."
                return
            "Singkirkan kertasnya dan minta Haruka mengajarimu.":
                $ kk_record_choice("C-D03","C")
                $ kk_flag("haruka_dimintai_bantuan")
                $ kk_minutes(5)
                nar "Kau menulis pesan saat masalahnya masih segar dalam ingatan."
                return
    $ kk_practice_sketch(_lokasi)
    nar "Kau menghabiskan satu jam bersama buku sketsa. Kali ini kau menandai bagian yang ingin kaulatih lagi."
    return

label kk_mio_deadline:
    if not kk_mio_message():
        return
    nar "Pesan dari Mio masuk. Ia ingin tahu kapan bisa melihat sketsa sampul yang kaujanjikan."
    menu:
        "Akui bahwa kau kesulitan mengerjakannya.":
            $ kk_record_choice("C-D07","A")
            nar "Kau mengirim jawaban itu sebelum sempat menghapusnya lagi."
        "Minta waktu tambahan.":
            $ kk_record_choice("C-D07","B")
            nar "Kau meminta sedikit waktu lagi untuk menyelesaikan sketsa."
        "Cari ilustrator lain untuk menyelesaikannya.":
            $ kk_record_choice("C-D07","C")
            nar "Kau menyimpan percakapan dengan ilustrator itu terpisah dari pesan Mio."
        "Buka sketsanya dan lanjutkan sampai pagi.":
            $ kk_record_choice("C-D07","D")
            $ kk_adj("kemampuan_gambar",1 if kk_kelelahan_tier()[1] >= 2 else 3)
            $ kk_minutes((6 - kk_slot)*240 - kk_minute)
            nar "Saat kau menaruh pensil, langit sudah terang."
            return
    $ kk_minutes(5)
    return

init 1 python:
    _hook("C-D07-A", lambda: kk_flag("mio_tahu_kesulitan"))
    _hook("C-D07-B", lambda: kk_flag("perpanjangan_diminta"))
    _hook("C-D07-C", kk_commission_secret)

label kk_show_portfolio:
    if not kk_art_studio_open(_lokasi):
        return
    if kk_comparison_due():
        nar "Haruka meletakkan dua lembar sketsa berdampingan. Ia menunjuk bagian tempat garis tanganmu berubah."
        menu:
            "Ceritakan terus terang kenapa sketsa itu berbeda.":
                $ kk_record_choice("C-D02","A")
                nar "Haruka menyimpan kedua lembar itu. Ia ingin mendengar ceritamu sampai selesai."
            "Beri alasan untuk perbedaan itu.":
                $ kk_record_choice("C-D02","B")
                nar "Ia menatap kedua gambar lagi sebelum menjawab."
            "Minta ia mengajarimu membuat garis itu lagi.":
                $ kk_record_choice("C-D02","C")
                nar "Haruka menggeser kertas kosong ke tengah meja."
    else:
        nar "Kau membentangkan sketsamu. Haruka menunjukkan di mana tekanan pensilmu berubah."
    if kk_has("haruka_dimintai_bantuan") or kk_get("kemampuan_gambar") >= 30:
        $ kk_adj("kemampuan_gambar",3)
        $ pts.setdefault("shena_risiko",20)
        $ kk_adj("shena_risiko",-1)
    $ kk_minutes(60)
    return

label kkscene_C11:
    call kk_scene_enter("shiori","Pameran seni · Studio")
    shiori "Aku pernah melihat garis seperti itu. Aku membaca buku yang diilustrasikan Shena."
    menu:
        "Akui bahwa kau yang memakai nama Shena.":
            $ kk_record_choice("C11","A")
            shiori "Begitu. Terima kasih sudah memberitahuku sendiri."
        "Pura-pura tidak mengenal nama itu.":
            $ kk_record_choice("C11","B")
            nar "Shiori memandang gambar di dinding sekali lagi."
        "Tawarkan membubuhkan tanda tangan.":
            $ kk_record_choice("C11","C")
            shiori "Kalau begitu, di halaman ini."
    return

init 1 python:
    def kk_tell_haruka():
        kk_flag("haruka_tahu_shena")
        kk_adj("shena_risiko",-10)

    _hook("C-D02-A", kk_tell_haruka)
    _hook("C-D02-B", lambda: kk_adj("curiga_haruka",5))
    _hook("C-D02-C", lambda: kk_flag("haruka_dimintai_bantuan"))
    _hook("C11-A", lambda: kk_flag("shiori_tahu_shena"))
    _hook("C11-B", lambda: kk_adj("daftar_kebohongan_shiori",1))
    _hook("C11-C", lambda: kk_flag("shiori_tahu_shena"))
