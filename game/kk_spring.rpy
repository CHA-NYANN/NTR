# Draft editorial. Milestone_3_Tahun M01b/M02 dan Event_Moeka, Event_Shiori,
# Event_Nagisa, Event_Miyuki. Adegan memakai urutan pilihan dari katalog.
label kkscene_Mo01:
    call kk_scene_enter("moeka", "Hanami · Taman Kampus")
    nar "Moeka tiba dengan kamera masih tersampir. Sambil mengatur napas, ia sudah mengarahkan orang-orang ke tempat piknik."
    moeka "Maaf! Yang sudah pegang alas, ikut aku dulu!"
    menu:
        "Geser sedikit agar ia bisa lewat.":
            $ kk_record_choice("Mo01", "A")
            moeka "Makasih. Aku menyusul setelah semuanya duduk."
        "Ingatkan bahwa orang-orang tadi menunggunya.":
            $ kk_record_choice("Mo01", "B")
            moeka "Iya. Maaf membuat kalian menunggu."
        "Bantu membentangkan alas sesuai arahannya.":
            $ kk_record_choice("Mo01", "C")
            nar "Dari dekat, kau melihat Moeka membagi pekerjaan sampai orang terakhir mendapat tempat."
    return

label kkscene_S01:
    call kk_scene_enter("shiori", "Hanami · Taman Kampus")
    nar "Shiori memindahkan satu bidak shogi, lalu berbalik melihat posisi itu dari sisi lawan."
    menu:
        "Duduk di seberangnya dan tantang ia bermain.":
            $ kk_record_choice("S01", "A")
            shiori "Kalau begitu, sisi papan itu milikmu."
        "Amati langkah berikutnya.":
            $ kk_record_choice("S01", "B")
            nar "Ia membiarkan posisi itu terbuka agar kau dapat melihatnya."
        "Biarkan ia bermain sendiri.":
            $ kk_record_choice("S01", "C")
            nar "Bunyi bidak kayu terdengar lagi ketika kau beranjak."
    return

label kkscene_Mo02:
    call kk_scene_enter("moeka", "Stasiun Kouseikan-mae")
    moeka "Undiannya menang! Kita benar-benar bisa berangkat."
    if any(c["ev"] == "Mo01" and c["key"] == "C" for c in choices_log):
        nar "Kau mengenali caranya mengumpulkan rombongan. Waktu piknik pun ia mengatur semuanya seperti ini."
    menu:
        "Ucapkan selamat.":
            $ kk_record_choice("Mo02", "A")
            moeka "Hehe. Rasanya masih belum percaya."
        "Akui kau iri pada keberuntungannya.":
            $ kk_record_choice("Mo02", "B")
            moeka "Kalau aku yang berharap menang, biasanya malah meleset."
        "Bantu dia memeriksa rencana perjalanan.":
            $ kk_record_choice("Mo02", "C")
            moeka "Boleh! Baca dari atas, ya. Aku cek yang sudah siap."
    return

label kkscene_S02:
    call kk_scene_enter("shiori", "Lobi ryokan")
    if any(c["ev"] == "S01" and c["key"] == "A" for c in choices_log):
        shiori "Kali ini juga mau duduk di seberangku?"
    else:
        shiori "Papannya sudah tersedia. Kau mau bermain?"
    menu:
        "Terima tantangannya dan bermain serius.":
            $ kk_record_choice("S02", "A")
            shiori "Bagus. Aku ingin melihat langkahmu sendiri."
        "Biarkan dia mengambil bidak yang bisa kauselamatkan.":
            $ kk_record_choice("S02", "B")
            shiori "Kau melihat langkah itu. Jangan mengalah padaku."
        "Ambil kesempatan untuk memenangkan permainan.":
            $ kk_record_choice("S02", "C")
            shiori "Kau melihat celahnya duluan. Satu lagi?"
    return

label kkscene_Mi02:
    call kk_scene_enter("miyuki", "Dapur ryokan")
    miyuki "Yang ketiga pun bentuknya masih begitu. Sebaiknya jangan dimakan dulu."
    menu:
        "Habiskan kue yang sudah ia sajikan.":
            $ kk_record_choice("Mi02", "A")
            miyuki "Semuanya? Padahal aku baru mau minta satu gigitan saja."
        "Katakan dengan jujur bagian yang kurang enak.":
            $ kk_record_choice("Mi02", "B")
            miyuki "Ah, itu juga yang kurasakan. Baiklah, kucoba lagi."
        "Gulung lengan bajumu dan bantu memperbaiki adonannya.":
            $ kk_record_choice("Mi02", "C")
            miyuki "Boleh kutitipkan mangkuknya padamu? Kali ini kita buat bersama."
    return

label kkscene_N02:
    call kk_scene_enter("nagisa", "Ruang bersama ryokan · Malam")
    nagisa "Jangan tidur dulu. Satu ronde lagi."
    menu:
        "Bermain sepenuh kemampuanmu.":
            $ kk_record_choice("N02", "A")
            nagisa "Menang lagi? Tunggu. Belum selesai."
        "Perlambat permainanmu agar ia bisa menang.":
            $ kk_record_choice("N02", "B")
            nagisa "Tadi kau sengaja, ya?"
        "Ajak dia bermain satu tim.":
            $ kk_record_choice("N02", "C")
            nagisa "Geser sedikit. Aku ambil sisi ini."
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

