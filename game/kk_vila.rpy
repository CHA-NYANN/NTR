# Mi05 "Minuman di Vila" (M05b, bulan 5, Vila Izu). Miyuki lebih terbuka saat
# menginap. Pilihan "memanfaatkan" membuat Force Route TERSEDIA sebagai kejahatan,
# ditulis sebagai KONSEKUENSI + KARAKTER saja: kerentanan korban dan sikap pemain,
# tanpa metode, tanpa adegan, tanpa cara. Force tetap non-operasional/off-screen.
# Lihat [[feedback-force-route-non-operational]].

# ┌─ PANDUAN CERITA · Mi05 · Minuman di Vila
# │ LOKASI  : Alam & Pantai · Vila (Izu)
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : Miyuki lebih terbuka.
# │ INTI    : A dengarkan / B mengantar ke kamar / C memanfaatkan.
# │ AKHIRAN : hub risiko tinggi ( Force Route tersedia sebagai kejahatan).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi05:
    call kk_scene_enter("miyuki", "Vila (Izu) · Malam")
    nar "Miyuki melepas peran senpai sedikit demi sedikit di ruang tengah vila. Ia tertawa pada cerita yang sebenarnya tidak terlalu lucu, lupa melanjutkan kalimat, kemudian mengakui kepalanya terasa berat."
    miyuki "Aku seharusnya berhenti tadi. Jangan jadikan ini bahan cerita besok, ya. Aku ingin punya satu malam yang nggak harus rapi."
    nar "Ia meletakkan gelas menjauh. Kepercayaannya tampak jelas dalam cara ia tidak menyiapkan pembelaan ketika menyandarkan kepala pada sofa."
    call kk_family_menu("Mi05", ["Dengarkan ia bicara.", "Antar ia ke kamarnya dengan aman.", "Catat betapa rentannya ia malam ini."])
    if _return == "A":
        nar "Kau menaruh air di dekatnya dan mendengarkan tanpa mendesak cerita lebih pribadi. Miyuki mengeluh tentang kesepian apartemen, lalu malu karena merasa sudah berbicara terlalu banyak."
        miyuki "Biasanya aku berhenti sebelum sampai bagian ini. Nanti orang bingung harus menghibur dengan apa."
        nar "Kau tidak memintanya melanjutkan. Ia bisa memilih diam, dan justru itu membuatnya merasa lebih aman untuk tetap duduk."
    elif _return == "B":
        nar "Kau menawarkan mengantarnya beristirahat dan menanyakan siapa yang ingin ia hubungi. Miyuki menyebut Sena. Kalian memastikan ia tidak perlu menghadapi malam yang membuatnya bingung seorang diri."
        miyuki "Terima kasih. Besok kalau aku malu, ingatkan bahwa aku memang minta tidur, bukan minta ditertawakan."
        nar "Kau meninggalkannya setelah ia aman di kamar. Esok hari ia mengingat bahwa kepercayaannya tidak diubah menjadi kesempatan mengambil sesuatu darinya."
    else:
        nar "Kau menyadari kerentanannya dan membiarkan pikiranmu memperlakukannya sebagai kesempatan. Di hadapanmu, Miyuki masih mengira perhatian yang diterima tidak menuntut kewaspadaan."
        miyuki "Aku senang bisa percaya pada seseorang sebentar."
        nar "Tidak ada kekerasan yang kauperbuat malam ini. Tetapi cara pandangmu sudah mulai menggeser seseorang yang mempercayaimu menjadi peluang untuk dilanggar. Apa yang akan terjadi sesudahnya tetap menjadi tanggung jawab pilihanmu, bukan keadaan Miyuki."
    return

init 1 python:
    _hook("Mi05-A", lambda: (kk_rel("miyuki","trust",6), kk_rel("miyuki","intim",4)))
    _hook("Mi05-B", lambda: (kk_rel("miyuki","trust",8), kk_flag("miyuki_dijaga_vila")))
    _hook("Mi05-C", lambda: kk_flag("force_tersedia_miyuki"))
