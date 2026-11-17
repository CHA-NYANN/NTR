# Event netral tambahan: S10 (Kuroiwa menjemput Shiori) dan N20 (kembang api terakhir).
# Efek mengikuti Event_Shiori dan Event_Nagisa; angka adalah setelan prototipe.
# ┌─ PANDUAN CERITA · S10 · Hujan Deras: Kuroiwa Menjemput
# │ LOKASI  : Distrik Elite · Klub Catur
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : ia dijemput.
# │ INTI    : A ikut / B tolak.
# │ AKHIRAN : Kuroiwa mencatat.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S10:
    call kk_scene_enter("shiori", "Klub Catur · Hujan deras")
    nar "Kuroiwa menunggu di dekat mobil dengan payung besar. Shiori berhenti sebelum masuk ketika melihatmu memperhitungkan apakah tas dapat dijadikan pelindung dari hujan."
    shiori "Kamu boleh ikut diantar. Bukan ujian tentang kemandirian, hanya kursi yang masih kosong. Kalau lebih nyaman pulang sendiri, aku juga tidak tersinggung."
    menu:
        "Ikut diantar bersamanya.":
            $ kk_record_choice("S10", "A")
            shiori "Kuroiwa akan mencatat siapa yang kuajak. Tak apa, aku yang memintanya."
            nar "Kuroiwa menyapamu dan menanyakan tujuan, tidak lebih. Di perjalanan Shiori membicarakan hal biasa, menikmati bahwa kebersamaan tidak memerlukan panggung atau rencana yang rumit agar boleh terjadi."
        "Tolak dan pulang sendiri.":
            $ kk_record_choice("S10", "B")
            shiori "Hati-hati di jalan, kalau begitu. Jangan sampai sakit."
            nar "Ia menawarkan menunggu sebentar jika kau perlu memesan kendaraan lain, kemudian menghormati keputusanmu pergi. Kepeduliannya tidak berubah menjadi tuntutan agar diterima demi menjaga harga dirinya."
    return

# ┌─ PANDUAN CERITA · N20 · Kembang Api Terakhir
# │ LOKASI  : Hunian Biasa · Taman Lingkungan
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : ia menarik pemain pergi.
# │ INTI    : A ikut / B tolak / C ajak bicara.
# │ AKHIRAN : hub #10.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N20:
    call kk_scene_enter("nagisa", "Taman Lingkungan · Kembang api")
    nar "Nagisa menyentuh lenganmu ketika orang-orang mulai bergerak menuju tepi sungai. Ada jalan lebih sepi di dekat taman, cukup terang untuk dilewati tetapi jauh dari rombongan."
    nagisa "Ikut sebentar? Aku ingin melihat yang terakhir tanpa harus mendengar semua orang bicara. Kamu boleh bilang nggak. Aku sedang mencoba bertanya sebelum menarik."
    nar "Ia melepaskan lenganmu sesudah mengatakan itu. Kesungguhan gerakan kecil tersebut lebih jelas daripada kalimat yang masih terdengar ketus."
    call kk_family_menu("N20", ["Ikut dengannya menjauh dari keramaian.", "Tolak dan tetap di keramaian.", "Ajak ia bicara alih-alih pergi."])
    if _return == "A":
        nar "Kau ikut. Kalian menemukan tempat di mana ledakan masih terdengar utuh dan orang lain tidak cukup dekat untuk mendengar setiap kata."
        nagisa "Terima kasih. Aku tahu harus belajar bisa sendiri. Tapi malam ini aku senang kamu mau."
        nar "Ia tidak langsung meminta janji tentang festival berikutnya. Untuk beberapa menit, kebersamaan boleh berhenti sebagai sesuatu yang sedang terjadi."
    elif _return == "B":
        nar "Kau memilih tetap di keramaian. Nagisa melihat jalan sepi itu, lalu orang-orang yang ada di dekatmu."
        nagisa "Baik. Aku juga mungkin tetap di sini. Bukan buat mengawasi. Aku cuma... belum ingin pergi sendirian."
        nar "Ia menjaga jarak, tetapi matanya beberapa kali kembali mencarimu. Penolakan yang kecil masih terasa besar di dalam ketakutan yang belum selesai."
    else:
        nar "Kau mengajaknya bicara di tempat kalian berdiri, menanyakan mengapa perlu membawa kalian menjauh. Nagisa hendak marah, lalu mengakui ia ingin merasa punya waktumu tanpa bersaing dengan wajah lain."
        nagisa "Aku tahu itu mulai terdengar seperti harus selalu dipilih. Aku nggak mau jadi orang yang cuma bisa tenang kalau yang lain hilang."
        nar "Kembang api terakhir membuat kalian berhenti. Sesudahnya, pembicaraan yang belum selesai tetap boleh dilanjutkan."
    return

init 1 python:
    _hook("S10-A", lambda: (kk_adj("respek_shiori",3), kk_flag("kuroiwa_mencatat")))
    _hook("S10-B", lambda: kk_rel("shiori","trust",3))
    _hook("N20-A", lambda: (kk_rel("nagisa","intim",4), kk_adj("kelekatan_nagisa",5)))
    _hook("N20-B", lambda: kk_rel("nagisa","jeal",4))
    _hook("N20-C", lambda: kk_rel("nagisa","trust",4))
