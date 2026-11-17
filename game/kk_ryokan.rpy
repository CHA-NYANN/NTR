# K02 "Kamar yang Tertukar" (M02, trip onsen/ryokan). Plot armor menaruh Koita
# sekamar dengan salah satu heroine; pemain bisa menggeser pembagian kamar.
# Pilihan manipulatif (termasuk sabotase) ditulis sebagai KONSEKUENSI + risiko,
# tanpa metode/cara. Lihat [[feedback-force-route-non-operational]].

# ┌─ PANDUAN CERITA · K02 · Kamar yang Tertukar
# │ LOKASI  : Taman luar ryokan
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : ryokan; plot armor menaruh Koita sekamar dengan satu heroine (ditentukan oleh siapa yang paling siap).
# │ INTI    : A tukar kamar tanpa ketahuan / B biarkan / C masuk sebagai "gangguan" / D sabotase pembagian kamar.
# │ AKHIRAN : A–C menggeser Jealousy; D memicu kecurigaan Fujisawa/Rina bila ketahuan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K02:
    call kk_scene_enter("koita", "Taman luar ryokan · Daftar kamar")
    nar "Pengelola ryokan meminta semua orang memeriksa daftar sebelum kunci dibagikan. Di luar kaca, koper-koper masih berdiri di samping taman; di dalam, selembar kertas telah membuat dua orang mendadak tidak tahu harus melihat ke mana."
    koita "Namaku di kamar itu juga? Mungkin pembagiannya supaya cukup. Aku bisa tanya kalau ada yang keberatan."
    nar "Orang yang sekamar dengannya mengatakan tidak apa-apa dengan suara terlalu cepat. Koita tersenyum malu, seolah kebetulan tersebut sepenuhnya berada di luar kuasanya."
    nar "Kau mengenali kerapian situasi yang disukai naskah: masalah kecil, kedekatan mendadak, lalu alasan bagi semua orang untuk menyebutnya tidak sengaja. Daftarnya belum disahkan."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Tukar kamar diam-diam, tanpa ada yang tahu.", "Biarkan pembagian apa adanya.", "Sisipkan dirimu sebagai 'yang kebetulan lewat'.", "Kacaukan pembagian kamar itu dari balik layar."])]
    call screen kk_choice_panel(_rows, "Daftar pembagian kamar")
    $ kk_record_choice("K02", _return)
    if _return == "A":
        nar "Kau mengubah susunan kamar tanpa mengumumkan campur tanganmu. Ketika kunci dibagikan, nama-nama itu dibacakan sebagai keputusan yang memang seharusnya demikian."
        koita "Oh, ternyata berubah. Iya, baik."
        nar "Kelegaan seseorang datang bersamaan dengan kekecewaan orang lain. Koita beberapa kali melihat daftar baru, berusaha mencocokkannya dengan yang tadi ia ingat."
        nar "Malam itu orang berbicara tentang kamar dengan nada ringan yang terlalu sibuk menutupi sesuatu. Kau tahu penyebabnya, tetapi membiarkan mereka menyebutnya nasib."
    elif _return == "B":
        nar "Kau tidak mengubah apa pun. Koita mengambil kunci, lalu menunggu pendamping kamarnya memastikan sendiri bahwa ia bersedia."
        koita "Kalau nanti terasa nggak nyaman, bilang. Kita bisa tanyakan ke pengelola."
        nar "Mereka berjalan menuju koridor yang sama. Di belakangnya, seseorang bertanya tentang jadwal makan dengan suara sedikit lebih keras daripada perlu."
        nar "Kedekatan malam itu mendapat kesempatan yang sudah disiapkan. Apa yang akan mereka lakukan dengannya tetap belum bisa dijawab oleh selembar daftar."
    elif _return == "C":
        nar "Kau menyelipkan kehadiranmu ke urusan kamar seolah hanya membantu sebentar. Pembicaraan yang tadinya berdua kini harus menampungmu, barangmu, dan alasan praktis yang kaubawa."
        koita "Kalau begitu kita atur lagi. Jangan sampai ada yang nggak kebagian tempat."
        nar "Ia tersenyum, tetapi orang di sebelahnya melihatmu dengan lebih cermat. Kesempatan yang semula terasa pribadi larut menjadi kesibukan bersama, menyisakan cemburu yang belum punya tempat untuk dikatakan."
    else:
        nar "Campur tanganmu membuat pembagian kamar berantakan. Pengelola meminta maaf, anggota rombongan mulai membandingkan ingatan, dan kunci yang sudah dibagikan harus dikumpulkan lagi."
        "Rina" "Aneh. Tadi waktu kubaca belum begini. Ada yang mengubah?"
        nar "Fujisawa meminta semua orang tenang dan memeriksa daftar bersama. Tidak ada yang langsung menyebut namamu. Namun kekacauan yang menghalangi Koita malam ini meninggalkan orang-orang yang kini tahu ada sesuatu untuk diperiksa."
    return

init 1 python:
    _hook("K02-A", lambda: (kk_adj("cemburu_kamar",8), kk_koita_aware(3)))
    _hook("K02-B", lambda: None)
    _hook("K02-C", lambda: kk_adj("cemburu_kamar",6))
    _hook("K02-D", lambda: (kk_flag("kamar_disabotase"), kk_adj("rina_curiga",8), kk_suspect("fujisawa",10)))
