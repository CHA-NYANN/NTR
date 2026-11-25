# Grand Bab M17b · Liburan Besar Pulau (4 Hari + Kebocoran Sistem · Q19 Pulau)
# Paralel Agustus Tahun 2 (M17) untuk Host Chiasa dan Host Yutaka (terhubung ke M18).
# Gerbang masuk: kk_bulan == 17 pada lokasi utama tanpa syarat akumulasi poin tambahan.
# Percabangan di dalam 4 hari dipicu secara dinamis oleh akumulasi relasi,
# ketakutan, kecurigaan, tahap rute, dan pilihan pemain sepanjang arc.

init python:
    def kk_pulau_m17b_due(distrik, lokasi):
        if kk_bulan != 17 or kk_has("m17b_pulau_selesai"):
            return False
        if kk_host == "chiasa":
            return lokasi in ("Rumah Amamiya", "Stasiun Kouseikan-mae", "Pantai", "Vila (Izu)")
        if kk_host == "yutaka":
            return lokasi in ("Apartemen Yutaka", "Rumah Amamiya", "Stasiun Kouseikan-mae", "Pantai", "Vila (Izu)")
        return False

    def kk_pulau_focus_heroine():
        heroines = ("nagisa", "miyuki", "harumi", "moeka", "shiori")
        def _score(cid):
            return (kk_rel_get(cid, "intim") * 2
                    + kk_rel_get(cid, "trust")
                    + kk_rel_get(cid, "aff")
                    - kk_rel_get(cid, "fear"))
        return max(heroines, key=_score)

    def kk_pulau_max_fear_heroine():
        heroines = ("miyuki", "harumi", "moeka", "nagisa", "shiori")
        best = max(heroines, key=lambda c: kk_rel_get(c, "fear"))
        return best, kk_rel_get(best, "fear")

    def kk_pulau_day2_branch():
        if kk_get("curiga_koita", 0) >= 15 or kk_has("pulau_hari1_koita"):
            return "koita_yutaka"
        if (stage.get("nagisa", 0) >= 2 or kk_rel_get("nagisa", "jeal") >= 50
                or kk_has("chiasa_arah_yuri") or kk_has("nagisa_dibela_chiasa")):
            return "nagisa_pergoki"
        return "shiori_miyuki"

    def kk_pulau_day3_branch():
        fear_cid, fear_val = kk_pulau_max_fear_heroine()
        if (fear_val >= 20 or stage.get("miyuki", 0) >= 3
                or kk_has("miyuki_rasa_salah_dimanfaatkan")
                or kk_has("harumi_dimanfaatkan")
                or kk_has("beasiswa_terancam")):
            return "distorsi_tekanan"
        if (kk_get("curiga_koita", 0) >= 18
                or kk_get("daftar_kebohongan_shiori", 0) > 0
                or kk_has("pulau_manuver_alkohol")
                or kk_get("pulau_risiko", 0) >= 15):
            return "rumor_curiga"
        return "tarik_hati"

    def kk_pulau_day4_outcome():
        _, fear_val = kk_pulau_max_fear_heroine()
        risiko = kk_get("pulau_risiko", 0)
        jujur = kk_get("pulau_jujur", 0)
        intim_p = kk_get("pulau_intim", 0)
        if (risiko >= 25 or kk_get("curiga_koita", 0) >= 25
                or (kk_has("pulau_manuver_alkohol") and jujur < 20)):
            return "retak_meisa"
        if ((fear_val >= 25 or kk_has("miyuki_rasa_salah_dimanfaatkan")
                or kk_has("harumi_dimanfaatkan"))
                and not kk_has("pulau_hari3_lindungi")):
            return "jejak_takut"
        if (jujur >= 20 or intim_p >= 15) and risiko < 25:
            return "orbit_bergeser"
        return "rapuh_waspada"

    def kk_pulau_advance_days():
        if kk_bulan == 17 and kk_hari_n <= 26:
            for _ in range(3):
                kk_new_day()
        store.kk_slot = 2
        store.kk_minute = 0

init 1 python:
    _hook("C17b_H1-A", lambda: (kk_adj("pulau_kendali", 15), kk_flag("pulau_hari1_kendali")))
    _hook("C17b_H1-B", lambda: (kk_rel("koita", "aff", 4), kk_rel("koita", "intim", 3), kk_rel("nagisa", "jeal", 4), kk_flag("pulau_hari1_koita")))
    _hook("C17b_H1-C", lambda: (kk_adj("pulau_waspada", 15), kk_rel("shiori", "trust", 3), kk_flag("pulau_hari1_amati")))

    _hook("C17b_H2-A", lambda: (kk_adj("pulau_jujur", 15), kk_koita_suspect(-3), kk_flag("pulau_hari2_jujur")))
    _hook("C17b_H2-B", lambda: (kk_adj("pulau_risiko", 20), kk_koita_suspect(6), kk_flag("pulau_manuver_alkohol")))
    _hook("C17b_H2-C", lambda: (kk_adj("pulau_waspada", 15), kk_koita_fear(4), kk_flag("pulau_catat_celah_sistem")))

    _hook("C17b_H3-A", lambda: (kk_adj("pulau_jujur", 15), kk_adj("respek_shiori", 4), kk_flag("pulau_hari3_lindungi")))
    _hook("C17b_H3-B", lambda: (kk_adj("pulau_risiko", 20), kk_koita_suspect(6), kk_flag("pulau_hari3_pisah")))
    _hook("C17b_H3-C", lambda: (kk_adj("pulau_intim", 15), kk_flag("pulau_hari3_berdua")))

    _hook("C17b_H4-A", lambda: (kk_flag("sistem_celah_tercatat"), kk_flag("q19_complete")))
    _hook("C17b_H4-B", lambda: (kk_adj("pulau_intim", 10), kk_flag("q19_complete")))
    _hook("C17b_H4-C", lambda: (kk_adj("pulau_waspada", 10), kk_flag("meisa_diperingatkan_pulau"), kk_flag("q19_complete")))


# ┌─ PANDUAN CERITA · M17b · Liburan Besar Pulau (4 Hari + Kebocoran Sistem)
# │ LOKASI  : Alam & Pantai · Vila Pulau (4 Hari · Agustus Tahun 2)
# │ TERLIBAT: Host Chiasa, Koita, Yutaka, Nagisa, Miyuki, Harumi, Moeka, Shiori, Sistem, Kurosawa Meisa
# │ AWALAN  : Berangkat feri menuju liburan pulau empat hari; semua lingkaran bertemu di satu vila.
# │ INTI    : H1 formasi vila / H2 pesta pantai & Kebocoran Sistem (data usang) / H3 badai bentrok rute / H4 feri pulang.
# │ AKHIRAN : Percabangan 4 hasil akhir sesuai akumulasi trust/fear/curiga/risiko + catatan celah Sistem.
# └─ tulis / perbaiki dialog di bawah ──
label kk_pulau_m17b:
    if kk_has("m17b_pulau_selesai"):
        return
    $ kk_bgm("retreat")
    if kk_host == "chiasa":
        $ _focus = kk_pulau_focus_heroine()
        call kk_pulau_hari1(_focus)
        call kk_pulau_hari2(_focus)
        call kk_pulau_hari3(_focus)
        call kk_pulau_hari4(_focus)
    else:
        $ _focus = kk_pulau_yutaka_focus()
        call kk_pulau_yutaka_hari1(_focus)
        call kk_pulau_yutaka_hari2(_focus)
        call kk_pulau_yutaka_hari3(_focus)
        call kk_pulau_yutaka_hari4(_focus)
    $ kk_flag("m17b_pulau_selesai")
    $ kk_pulau_advance_days()
    $ kk_bgm_location("d5", "Stasiun Kouseikan-mae")
    return


# ══════════════════════════════════════════════════════════════════════════
# HARI 1 · Dermaga Feri & Vila Pulau — Semua Rute Bertemu
# ══════════════════════════════════════════════════════════════════════════
label kk_pulau_hari1(_focus):
    call kk_scene_enter("chiasa", "Dermaga Penyeberangan · Hari 1 Pulau")
    nar "Rencana liburan empat hari di pulau selatan yang sejak awal bulan ramai dibahas di grup pesan akhirnya berangkat juga. Bau garam laut, deru mesin kapal feri, dan terik matahari Agustus menyambut ketika rombongan kalian berkumpul di depan gerbang dermaga sambil menyeret koper masing-masing."
    "Petugas Feri" "Penumpang tujuan Pulau Minami jalur siang, harap menyiapkan tiket penyeberangan! Kapal berangkat sepuluh menit lagi!"
    nar "Kamu membetulkan pita hitam pada ikatan setengah rambut cokelat gelapmu sambil memindahkan tali tas kanvas ke bahu kanan. Di depan loket, hampir seluruh lingkaran yang selama setahun lebih ini berputar di sekitar Koita berdiri dalam jarak beberapa langkah satu sama lain."
    koita "Semua tiket sudah di tangan masing-masing kan? Chi-chan, tas gambarmu nggak berat banget? Sini sebagian biar Ko-nii bantu bawakan sampai dek atas."
    chiasa "Nggak usah, Ko-nii, isinya cuma buku sketsa tipis sama baju ganti. Ko-nii bawa kotak pendingin minuman saja sudah penuh dua tangan."
    yutaka "Betul kata Chiasa. Kalau kamu jatuh di tangga kapal sambil megang kotak es, nanti kita semua minum air laut empat hari penuh."
    nar "Yutaka berdiri di sisi kiri Koita dengan kemeja linen terang dan jam tangan bertali kulit melingkar rapi di pergelangannya. Senyum santainya melonggarkan suasana dermaga, meski matanya yang abu-abu gelap sempat melirik singkat ke arah seluruh rombongan seolah menghitung siapa berdiri dekat siapa."
    moeka "Wah, akhirnya sampai dermaga juga! Chimian, lihat nih, aku bawa topi jerami lebar biar nggak gosong di pantai! Kocchi, nanti sampai vila langsung foto bareng ya!"
    if kk_has("beasiswa_terancam"):
        nar "Suara Moeka terdengar cerah seperti biasanya, tetapi kamu melihat kantong mata tipis di balik riasannya yang rapi. Di sudut tas kainnya terselip map plastik tipis berisi berkas catatan kuliah, dan ponselnya baru saja menampilkan pesan singkat dari Ryena soal foto sesi kerja di studio Kuga yang mulai dipakai promosi daring."
    elif kk_has("moeka_intervensi_1"):
        nar "Saat matanya bertemu matamu, senyum Moeka melunak sedikit lebih tenang. Ia sempat mengacungkan dua jari kecil ke arahmu sambil menyinggung pelan bahwa Ryena baru mengirim kabar soal foto promosinya dari studio Kuga yang diunggah lebih awal, lalu segera menyimpan ponselnya demi menikmati empat hari liburan."
    else:
        moeka "Oh iya, barusan Ryena kirim pesan bilang foto kerjaanku dari studio Kuga katanya sudah mulai diunggah sebagian. Nanti malam saja kubuka, sekarang waktunya lihat laut dulu!"
    miyuki "Moeka-chan jangan lari-lari di dekat ramp kapal nanti terpeleset. Aku sudah menyiapkan obat mabuk laut dan perban kecil di tas samping kalau ada yang pusing di perjalanan."
    nar "Miyuki berdiri anggun dengan rambut hitam panjang lurus terurai dan kardigan tipis melapisi blus musim panasnya. Matanya yang cokelat kemerahan menyapu rombongan dengan hangat, lalu berhenti sebentar pada wajahmu."
    if stage.get("miyuki", 0) >= 3 or kk_has("miyuki_rasa_salah_dimanfaatkan"):
        miyuki "Chiasa-chan sudah sarapan tadi? Kalau belum, aku bawa potongan kue kering di tas. Maaf kalau rasanya agak manis, nanti bilang saja kalau nggak cocok."
        chiasa "{i}Bahkan di dermaga liburan begini, refleksnya meminta maaf sebelum aku bicara masih langsung keluar.{/i}"
    else:
        miyuki "Chiasa-chan kelihatan segar hari ini. Di kapal nanti duduk di bagian tengah saja ya biar nggak terlalu terasa goyangannya."
    harumi "Secara hidrodinamika, bagian tengah lambung memang memiliki amplitudo goyangan paling kecil. Saya juga sudah mencatat jadwal pasang surut empat hari ke depan agar jadwal jalan malam di tepi pantai tidak meleset."
    nar "Harumi membetulkan bingkai kacamata tipisnya sambil memeluk buku catatan hitam dan termos teh baja. Rambut abu-abu peraknya dikepang menyamping dengan jepit mawar merah kecil yang mencolok di bawah cahaya matahari siang."
    if kk_has("harumi_dimanfaatkan"):
        nar "Begitu tatapannya bertemu matamu, ia mengangguk sopan dan menunggu setengah detik seolah mengecek apakah kamu ingin ia duduk di barisan tertentu."
    shiori "Kuroiwa-san sudah memastikan barang bawaan kita diantar langsung dari dermaga pulau ke vila. Jadi kalian tidak perlu terburu-buru berebut bagasi di geladak bawah."
    nar "Shiori melangkah mendekat dengan langkah teratur, rambut putih keperakannya terurai bergelombang dengan jepit mutiara kecil di sisi kanan. Mata ungu ametisnya menyapu dermaga sebelum melirik tajam ke sudut antrean belakang."
    if kk_get("daftar_kebohongan_shiori", 0) > 0:
        shiori "Kebetulan yang cukup menarik, Amamiya-san. Di belakang antrean tiket penumpang umum, ada seseorang dari kampus kita yang ikut naik feri yang sama."
    else:
        shiori "Ngomong-ngomong, sepertinya bukan hanya rombongan kita dari Kouseikan yang memilih pulau ini untuk libur akhir Agustus."
    nar "Kamu mengikuti arah pandang Shiori. Lima belas meter di belakang antrean, seorang mahasiswi berambut sebahu dengan kacamata hitam naik di atas kepalanya berdiri memegang ponsel pintar sambil berbicara pelan dengan seorang temannya. Kurosawa Meisa, sumber berbagai rumor paling cepat di kampus."
    "Mahasiswi Wisata" "Enak banget ya jadi keluarga Saionji, ke pulau saja koper sudah diantar staf pribadi. Eh, Meisa, cowok Sastra yang kemarin ramai diomongin di festival juga ikut bareng semua cewek itu?"
    "Kurosawa Meisa" "Pelan suaramu. Menarik juga ya mereka semua liburan di satu pulau yang sama. Simpan dulu, nanti kita lihat seberapa kompak mereka sampai hari pulang."
    chiasa "{i}Kurosawa Meisa ikut di feri yang sama, dan matanya sudah melirik nama Saionji sekaligus rombongan Ko-nii. Kalau satu saja keributan mencuat di pulau ini, beritanya bisa sampai ke kampus sebelum kapal pulang merapat.{/i}"
    play sound "audio/sfx/phone_buzz.wav"
    nar "Tepat ketika peluit kapal berbunyi panjang dan ponsel di tasmu bergetar dua kali, Nagisa yang baru selesai membeli minuman dingin di kios dermaga berjalan cepat menghampiri barisanmu dengan twin-tail pirang berpita hitam-pink melambai ditiup angin laut."
    if kk_has("nagisa_dibela_chiasa") or kk_has("chiasa_arah_yuri"):
        nagisa "Ponselmu bunyi terus dari tadi, Chiasa, siapa yang kirim pesan pas sudah di dermaga begini? ...Sudahlah, ini teh jelai dingin buatmu, jangan bilang nggak haus."
        nar "Ia menyodorkan botol dingin tepat ke tanganmu alih-alih langsung berjalan ke sisi Koita. Koita yang melihatnya dari depan pintu masuk sempat mengedip pelan, agak terkejut melihat Nagisa memilih naik kapal tepat di sampingmu."
    elif kk_rel_get("nagisa", "jeal") >= 45:
        nagisa "Sudah kubilang jangan berdiri terlalu dekat pinggir dermaga. Ayo naik duluan, Ko-kun sudah di depan tuh, jangan sampai kursinya diambil rombongan lain."
        nar "Matanya yang biru cerah menyapu wajahmu cepat dengan nada defensif yang kembali menajam."
    else:
        nagisa "Ayo cepat naik! Kalau telat nanti kita dapat bangku paling dekat suara mesin kapal. Ko-kun, tunggu dulu, jangan jalan cepat-cepat!"
    nar "Satu jam penyeberangan melewati laut biru berkilau membawa kalian ke sebuah vila kayu dua lantai di atas tebing kecil yang menghadap langsung ke teluk berpasir putih. Begitu pintu kaca ruang tengah dibuka, aroma kayu pinus dan udara asin memenuhi ruangan yang luas."
    koita "Wah, pemandangannya mantap banget! Oke, sebelum beres-beres, kita bagi kamar sama jadwal belanja makan malam dulu ya. Siapa yang mau ikut ke pasar pelabuhan sebentar?"
    if kk_get("curiga_koita", 0) >= 15:
        nar "Saat menyebut pembagian tugas itu, sorot mata Koita sempat berhenti di wajahmu sedikit terlalu lama. Senyumnya tetap ramah, tetapi ada kehati-hatian baru di caranya menunggumu bergerak duluan."
    nar "Di dalam satu ruang tengah kayu ini, seluruh benang hubungan selama lebih dari setahun akhirnya terkumpul tanpa sekat kampus. Langkah pertamamu sore ini akan menentukan siapa yang berdiri di dekatmu ketika malam tiba."
    call kk_family_menu("C17b_H1", ["\"Biar aku yang atur pembagian kamar dan ikut belanja bareng salah satu Senpai, Ko-nii bereskan barang saja.\"", "\"Ko-nii, temani aku ke jalan dermaga sebentar? Aku mau beli minuman dan buku sketsa kecil.\"", "Menepi ke beranda belakang vila untuk mengamati gerak rombongan dan arah Kurosawa Meisa."])
    if _return == "A":
        chiasa "Biar aku yang bantu atur daftar kamar putri sama ikut belanja bahan makan malam, Ko-nii bereskan kotak minuman di dapur saja biar nggak bolak-balik."
        koita "Eh, beneran nggak apa-apa, Chi-chan? Aku kira kamu mau langsung istirahat habis naik kapal."
        chiasa "Nggak capek kok. Lagipula lebih cepat kalau belanjaannya diurus sekalian sebelum warung pelabuhan tutup."
        nar "Kamu membagi kunci kamar lantai dua dengan rapi sehingga tidak ada yang merasa disisihkan, lalu berjalan beriringan menuruni jalan batu menuju warung pesisir bersama orang yang paling dekat denganmu sepanjang perjalanan tadi."
        if _focus == "nagisa":
            $ kk_rel("nagisa", "trust", 4)
            $ kk_rel("nagisa", "intim", 3)
            nagisa "Tumben kamu langsung ambil alih daftar kamar begitu, Chiasa. Biasanya kamu biarkan Ko-kun yang bingung sendiri sampai sore."
            chiasa "Kalau dibiarkan Ko-nii yang atur, nanti semua orang ditanyai satu-satu sampai matahari terbenam. Lagipula enak jalan berdua ke bawah, anginnya adem."
            nagisa "H-hmph! Jangan ngomong seenaknya. ...Tapi iya, lumayan tenang kalau nggak ramai-ramai."
            "Penjaga Warung" "Wah, dua nona manis dari vila atas ya? Ikan kembung barunya baru naik dari perahu, mau sekalian jagung manis buat bakar-bakar malam?"
            chiasa "Boleh, Oji-san, jagungnya delapan ya. Nagisa-senpai mau tambah es krim batang nggak?"
            nagisa "Soda biru satu! ...Biar aku yang bayar bagian es krimnya, jangan rebutan."
        elif _focus == "miyuki":
            $ kk_rel("miyuki", "trust", 4)
            $ kk_rel("miyuki", "intim", 3)
            miyuki "Terima kasih sudah ikut turun ke warung, Chiasa-chan. Tadi aku sempat khawatir belanjaan untuk tujuh orang bakal terlalu berat kubawa sendiri."
            chiasa "Makanya aku ikut, Tachibana-senpai. Selama empat hari di pulau ini, Senpai nggak boleh sibuk di dapur sendirian sementara yang lain santai di pantai."
            miyuki "Hehe, kedengarannya kayak perintah dari dokter yang lebih galak dariku ya. Baiklah, aku ikuti aturanmu hari ini."
            "Penjaga Warung" "Silakan pilih sayurannya, Nona! Bawang dan jagung bakarnya masih segar semua!"
            chiasa "Senpai pilih bumbunya, biar aku yang pegang keranjangnya. Jangan rebutan angkat barang berat terus."
            miyuki "Iya, Chiasa-chan. Rasanya lega juga sekali-sekali ada yang benar-benar membagi beban tanpa harus kuminta duluan."
        elif _focus == "moeka":
            $ kk_rel("moeka", "trust", 4)
            $ kk_rel("moeka", "intim", 3)
            moeka "Aduh, untung Chimian ikut turun! Kalau aku belanja sendiri bisa-bisa uang patungannya kebablasan beli camilan pantai semua."
            chiasa "Makanya kita cek daftarnya bareng, Moemoe-senpai. Senpai sendiri sudah agak lega bisa napas sebentar dari kerjaan di kota?"
            moeka "...Jujur? Baru pas kaki menginjak pasir dermaga tadi kepalaku serasa berhenti berisik. Makasih ya selalu nggak bikin aku merasa aneh waktu lagi capek, Chimian."
            "Penjaga Warung" "Jagung bakar sama cumi segarnya baru datang, silakan dipilih!"
            moeka "Wah, cuminya besar-besar! Chimian, kita beli ini ya biar malam nanti Kocchi sama Yutayuta yang kebagian tugas bakar!"
        elif _focus == "harumi":
            $ kk_rel("harumi", "trust", 4)
            $ kk_rel("harumi", "intim", 3)
            harumi "Pembagian tugasmu tadi cukup efisien, Amamiya-san. Tanpa keributan kecil di ruang tengah, waktu tunggu berkurang hampir dua puluh menit."
            chiasa "Anggap saja aku mulai ketularan gaya rapi Kujo-senpai. Di pulau ini Senpai jangan buka buku catatan terus ya, lihat lautnya juga."
            harumi "Saya tetap mencatat hal yang perlu diingat. Namun... berjalan menyusuri jalan pesisir seperti ini memang tidak mengganggu konsentrasi saya. Cukup menyenangkan."
            "Penjaga Warung" "Teh botol dingin dan sayur segarnya masih lengkap, silakan!"
            chiasa "Aku ambil dua teh tawar dingin sekalian buat di jalan naik nanti ya, Senpai."
        else:
            $ kk_rel("shiori", "trust", 4)
            $ kk_rel("shiori", "intim", 3)
            shiori "Kamu mengatur formasi kamar dengan sangat cepat, Amamiya-san. Hampir seperti seseorang yang sudah membaca seluruh dinamika meja sebelum kartu dibagikan."
            chiasa "Aku cuma nggak mau malam pertama sudah diisi suasana canggung, Saionji-senpai. Lagipula aku mau tanya pendapat Senpai soal Kurosawa Meisa tadi."
            shiori "Pilihan bijak untuk membicarakannya di luar vila. Ia menginap di penginapan keluarga dekat dermaga bawah. Selama tidak ada adegan ceroboh di tempat umum, ia tidak punya bahan apa pun."
            "Penjaga Warung" "Silakan, Nona, buah persik dan minumannya baru keluar dari kotak es!"
            shiori "Kita beli buah persik secukupnya saja. Sisanya kita lihat siapa yang paling mudah kehilangan kendali saat malam tiba."
        nar "Ketika kalian kembali mendaki jalan batu menuju vila menjelang senja, obrolan ringan itu sudah mengikat posisi kepercayaan tersendiri jauh sebelum hari kedua dimulai."
    elif _return == "B":
        chiasa "Ko-nii, temani aku turun ke jalan dekat dermaga sebentar yuk? Aku lupa beli penghapus lembut di kota, sekalian ambil minuman dingin buat kulkas vila."
        koita "Oh, boleh banget! Kebetulan aku juga mau beli arang tambahan buat barbekyu besok. Yang lain istirahat dulu nggak apa-apa ya?"
        nar "Nagisa yang baru menaruh tasnya di dekat tangga langsung menoleh cepat dengan bibir terkatup tipis."
        nagisa "Pergi berdua saja? Bukannya tadi mau belanja rame-rame?"
        chiasa "Cuma sebentar kok, Nagisa-senpai. Nanti pulangnya kami bawakan es krim buat semua."
        nar "Sepanjang jalan setapak kayu menurun ke dermaga, angin sore bertiup kencang membawa bau garam. Koita berjalan di sampingmu sambil menenteng kantong belanja lipat, tetapi langkahnya sedikit lebih tenang dibandingkan di depan keramaian tadi."
        koita "Chi-chan, tumben kamu ngajak aku keluar duluan begitu sampai vila. Ada yang mau kamu omongin?"
        chiasa "Cuma pengin jalan santai sebelum jadwal empat hari ini penuh acara, Ko-nii. Di ruang tengah tadi semua orang kelihatan punya ekspektasinya masing-masing ke kamu."
        nar "Koita berhenti sebentar di dekat pagar kayu yang menghadap perahu nelayan. Senyum mudahnya sedikit surut, digantikan raut berpikir yang jarang ia tunjukkan di depan teman-temannya."
        koita "Kelihatan banget ya? Jujur saja... aku senang semua orang bisa ikut liburan bareng. Tapi sejak kejadian festival minggu lalu, rasanya tiap aku ngobrol lama sama satu orang, aku takut orang lain langsung salah paham."
        chiasa "Kalau Ko-nii terus berusaha menyenangkan semua orang dalam satu vila, yang paling capek nanti ya Ko-nii sendiri."
        koita "Hehe... kadang omonganmu sekarang tajam banget ya, Chi-chan. Hampir kayak Yutaka waktu lagi serius."
        nar "Dari kejauhan di dekat kios es krim pelabuhan, Yutaka yang rupanya ikut turun membeli kopi kaleng melihat kalian berdua berdiri berdekatan di pagar kayu. Ia hanya mengangkat kaleng kopinya sekilas sebagai sapaan tanpa menyela, sementara tatapannya sempat singgah lama di wajahmu."
        koita "Ayo balik ke atas sebelum gelap. Makasih ya sudah ngajak jalan sebentar, kepalaku lumayan adem sekarang."
        nar "Kamu mengangguk dan melangkah sejajar di sampingnya, menyadari betapa cepat arah perhatian Koita kembali condong ketika kamu sengaja mengambil langkah pertama."
    else:
        nar "Alih-alih langsung berebut posisi di ruang tengah, kamu mengambil segelas air dingin dari dapur lalu melangkah keluar melalui pintu kaca geser menuju beranda kayu belakang yang menghadap langsung ke jalan pesisir bawah."
        nar "Dari atas tebing ini, seluruh pergerakan terlihat jelas. Di dalam ruang tengah, Koita sibuk menjawab pertanyaan Moeka tentang jadwal pantai sementara Nagisa dan Miyuki berbagi meja menyiapkan minuman. Di bawah sana, di jalan setapak dekat penginapan dermaga, sosok Kurosawa Meisa baru saja melintas sambil mengarahkan kamera ponselnya ke arah papan petunjuk pantai."
        yutaka "Posisi pengamatan yang bagus, Chiasa. Dari sini kelihatan sampai atap dermaga."
        nar "Kamu menoleh. Yutaka berdiri bersandar pada kusen pintu kaca dengan dua kaleng teh dingin, diikuti Shiori yang melangkah keluar beberapa detik kemudian sambil membawa cangkir teh hangat."
        chiasa "Yutaka-kun sama Saionji-senpai nggak ikut heboh bagi kamar di dalam?"
        shiori "Kamar sudah cukup jelas tanpa perlu diperdebatkan. Saya lebih tertarik memperhatikan apa yang barusan kamu lihat di jalan bawah, Amamiya-san."
        chiasa "Kurosawa Meisa. Penginapannya cuma berjarak lima menit jalan kaki dari jalan pantai di bawah vila kita."
        yutaka "Pantas dari feri tadi dia kelihatan santai banget waktu lihat rombongan kita. Kalau ada orang yang mabuk atau ribut di pantai malam-malam, dia nggak perlu repot-repot mencari bahan."
        shiori "Pengamatan yang tepat. Dan saya senang kamu menyadarinya lebih awal, Amamiya-san. Banyak orang baru panik setelah foto sudah beredar di grup mahasiswa."
        chiasa "Aku cuma nggak mau liburan empat hari ini berubah jadi bahan sidang gosip begitu kita balik ke kampus."
        yutaka "Setuju. Kalau begitu kita saling kasih kode saja kalau lihat Meisa terlalu dekat ke jalur vila."
        nar "Shiori mengangguk kecil dengan sorot respek yang tenang, lalu menyesap tehnya memandangi garis laut yang mulai menguning oleh matahari sore. Kamu menandai jalur tangga belakang dan sudut lampu pantai di dalam kepalamu sebelum kembali masuk."
    return


# ══════════════════════════════════════════════════════════════════════════
# HARI 2 · Pesta Pantai, Alkohol, & KEBOCORAN SISTEM (Q19 Pulau)
# ══════════════════════════════════════════════════════════════════════════
label kk_pulau_hari2(_focus):
    $ _d2 = kk_pulau_day2_branch()
    call kk_scene_enter("chiasa", "Beranda Vila Pulau · Malam Hari 2")
    $ kk_bgm("night")
    nar "Hari kedua dihabiskan dengan terik pantai dan suara ombak sampai kulit bahu terasa hangat. Begitu malam turun pekat di atas teluk, lampu gantung kuning di beranda vila dinyalakan di atas panggangan arang yang masih membara."
    nar "Di atas meja kayu panjang berjajar piring jagung bakar, cumi saus kecap, minuman ringan, serta beberapa kaleng minuman buah beralkohol rendah yang dibawa dari toko pelabuhan. Hawa laut yang hangat membuat percakapan mengalir jauh lebih longgar dibandingkan di kampus."
    moeka "Ayo bersulang dulu! Buat liburan tahun kedua sebelum tugas akhir dan ujian aneh-aneh mulai mengejar!"
    nagisa "Moeka-san, jangan minum cepat-cepat begitu, nanti baru satu kaleng mukamu sudah merah semua."
    miyuki "Betul, makan dulu daging sama jagungnya supaya perut nggak kosong. Ini, Chiasa-chan, jagung bakarnya masih panas."
    harumi "Secara teknis kadar alkohol minuman buah ini rendah, tetapi kombinasi kelelahan berenang dan suhu lembap mempercepat penyerapan. Saya tetap memilih teh tawar dingin."
    yutaka "Tenang, Kujo-san, kami nggak bakal memaksa siapa pun ikut pusing malam ini. Koita, tolong ambilkan penjepit baru dong, yang ini jatuh ke dekat arang."
    koita "Siap, sebentar kuambilkan di dapur dalam."
    nar "Beberapa menit kemudian rombongan mulai terpencar kecil di sekitar beranda dan ruang tengah. Koita belum juga kembali dari dalam rumah, sementara suara gelak tawa Moeka dan Nagisa memantul di teras."
    $ kk_bgm("system")
    play sound "audio/sfx/system_open.wav"
    nar "Tepat saat kamu melangkah ke sudut gelap samping tangga vila untuk mengambil udara segar, derik statis dingin menyambar rongga telingamu. Udara di depan wajahmu berkedip pecah menjadi jendela kaca biru neon yang melayang pelan."
    sistem "( ´ v ` )/ Halo, Sampah Peron~ Melihatmu cuma makan jagung bakar di tengah empat hari emas begini bikin aku mengantuk. Ini bonus misi khusus untukmu, Quest Pulau."
    sistem "Layar radar ceritaku baru menangkap celah cantik di ujung dermaga kayu bawah. Sepuluh menit lagi Koita bakal turun sendirian ke bangku lampu pantai untuk bertemu salah satu target yang lagi goyah, tanpa ada saksi satu pun di jalur bawah."
    sistem "Kalau kau turun lewat tangga samping sekarang dan memotong pertemuannya sebelum mereka sempat bicara, poin penyimpanganmu bakal melonjak rapi~ (^_~)-* Cepat bergerak sebelum jendelanya tutup."
    play sound "audio/sfx/system_close.wav"
    nar "Panel kaca biru itu lenyap secepat kemunculannya, menyisakan denyut dingin di pelipismu dan rasa tergesa yang memaksa kakimu memilih langkah."
    chiasa "{i}Jalur bawah kosong tanpa saksi, dan Koita turun sepuluh menit lagi. Kalau aku tidak mengeceknya sekarang, aku bisa kehilangan momen paling besar di pulau ini.{/i}"
    $ kk_bgm("tension")
    play sound "audio/sfx/footsteps.wav"
    nar "Kamu menuruni tangga kayu di tebing samping vila dengan sandal tipis, menyusuri deretan semak pantai menuju lampu tiang tunggal di ujung dermaga bawah. Debur ombak terdengar makin keras di kegelapan."
    nar "Namun tepat tiga langkah sebelum mencapai bangku kayu di bawah lampu, kakimu membeku di atas pasir."
    nar "Situasi di bawah lampu tiang itu sama sekali bertolak belakang dengan apa yang baru saja dibocorkan oleh Sistem."
    if _d2 == "koita_yutaka":
        nar "Tidak ada satu pun heroine yang menunggu Koita sendirian. Di bawah lampu dermaga, Koita berdiri menghadap Yutaka dengan suara rendah yang tegang, sementara dua puluh meter di belakang tembok penginapan dekat tiang listrik, layar ponsel Kurosawa Meisa berkedip pelan mengarah ke dermaga."
        koita "...Jujur saja, Yutaka. Aku nggak tahu kenapa belakangan ini rasanya Chiasa selalu muncul di tempat yang paling pas buat memotong obrolanku. Kadang aku merasa kayak dia bukan lagi adik yang biasa kukenal."
        yutaka "Hati-hati kalau ngomong begitu, Koita. Kamu yakin itu cuma perasaanmu karena lagi tertekan soal festival kemarin?"
        nar "Pijakan sandalmu di atas ranting kering mengeluarkan bunyi patah yang tajam. Kedua kepala itu langsung serempak menoleh lurus ke arah semak tempatmu berdiri."
        koita "Chi-chan...? Sejak kapan kamu berdiri di situ?!"
        nar "Dari sudut matamu, bayangan Kurosawa Meisa di dekat pos jalan pelabuhan langsung bergerak cepat menjauh sambil mengantongi ponselnya. Dadamu mendadak dingin. Informasi Sistem benar-benar meleset dan justru mendorongmu masuk ke tengah percakapan terburuk."
    elif _d2 == "nagisa_pergoki":
        nar "Koita sama sekali tidak ada di dermaga bawah. Yang duduk di bangku kayu sambil memeluk lutut dan memegang kaleng soda dingin adalah Nagisa, dengan wajah masih agak memerah oleh angin laut dan satu kaleng minuman buah dari beranda tadi."
        nar "Begitu mendengar langkah sandalmu yang terburu-buru di atas kayu dermaga, Nagisa langsung bangkit kaget. Matanya yang biru cerah menyapu posisimu yang datang mengendap dari tangga gelap, lalu melirik ke arah jalan setapak vila."
        nagisa "Chiasa?! Kamu ngapain turun mengendap-endap lewat tangga gelap jam segini?! Kamu nyari Ko-kun, atau kamu kira aku lagi janjian diam-diam sama seseorang di sini?!"
        nar "Suaranya yang naik tajam memantul di permukaan air laut yang sunyi. Tepat di jalan setapak atas menuju penginapan pantai, dua siluet termasuk Kurosawa Meisa berhenti melangkah dan menoleh ke bawah mendengar teriakan Nagisa."
        nagisa "Kok kamu diam saja? Mukamu kaget banget waktu lihat cuma aku yang ada di sini!"
        nar "Dadamu turun dingin. Tidak ada pertemuan rahasia Koita di sini; intel Sistem jelas usang, dan kamu baru saja tertangkap basah di posisi paling mencurigakan tepat di depan Nagisa."
    else:
        nar "Koita sama sekali tidak ada di bawah lampu dermaga. Yang duduk di bangku kayu menghadap laut gelap justru Shiori dan Miyuki yang sedang berbicara pelan dengan dua cangkir teh hangat dari termos."
        miyuki "...Makanya kadang aku bingung, Saionji-san, apakah aku terlalu sering mengiyakan permintaan orang sampai lupa mengukur tenagaku sendiri."
        shiori "Langkah pertama memang membedakan siapa yang sungguh peduli dan siapa yang hanya memanfaatkan rasa bersalahmu, Tachibana-senpai."
        nar "Sandalmu terpeleset sedikit di atas papan kayu yang lembap oleh embun laut, menimbulkan bunyi gesekan keras. Shiori langsung menoleh dengan tatapan ungu ametis yang sangat jernih dan tajam, sementara Miyuki tersentak pelan."
        shiori "Amamiya-san? Jalur tangga samping cukup gelap untuk sekadar jalan santai. Kamu sedang mencari seseorang, atau baru saja menguping pembicaraan kami?"
        nar "Di ujung jembatan masuk dermaga di belakangmu, kilatan kecil layar ponsel dari Kurosawa Meisa yang sedang berjalan kembali ke penginapannya sempat tertangkap jelas sebelum ia menghilang di tikungan. Darahmu terasa turun seketika. Intel Sistem benar-benar salah alamat dan menjebakmu di titik paling terbuka."
    $ kk_bgm("system")
    play sound "audio/sfx/system_open.wav"
    nar "Di sudut pandanganmu, jendela kaca biru kecil berkedip setengah transparan hanya untuk matamu sendiri. Emotikonnya menguap lebar tanpa sedikit pun rasa bersalah."
    sistem "(¬_¬ ) Oh, meleset ya? Kelihatannya data alur yang kubaca tadi masih salinan dua bulan lalu sebelum pilihan-pilihanmu menggeser jadwal mereka. Salahmu sendiri menelan mentah-mentah tanpa cek ulang, Sampah Peron~"
    sistem "Jangan memasang muka menuntut begitu. Aku pengawas kontrak, aku sama sekali tidak berutang permintaan maaf kalau prajuritku terpeleset sendiri di pasir."
    play sound "audio/sfx/system_close.wav"
    $ kk_flag("sistem_kebocoran_pulau")
    $ kk_adj("nyeri_sistem", 8)
    $ kk_bgm("tension")
    chiasa "{i}Sialan. Data Sistem bisa usang karena perubahan yang kubuat sendiri, dan ia bahkan tidak peduli aku rugi di lapangan. Sekarang aku harus membereskan kekacauan di depanku sendiri.{/i}"
    call kk_family_menu("C17b_H2", ["Hadapi langsung dengan jujur tanpa mengarang alasan, sambil menyimpan catatan soal kesalahan Sistem.", "Gunakan suasana pesta dan minuman di beranda untuk membalik topik serta menggeser sorotan ke Koita.", "Tarik diri cepat ke dalam vila sebelum makin panjang, lalu bedah celah data Sistem sendirian."])
    if _return == "A":
        $ store.sikap_sistem["selidik"] = store.sikap_sistem.get("selidik", 0) + 1
        nar "Kamu menarik napas dalam di udara laut yang dingin, menelan rasa geram kepada panel biru yang baru lenyap, lalu melangkah keluar penuh ke bawah lampu tiang agar wajahmu terlihat jelas."
        if _d2 == "koita_yutaka":
            $ kk_rel("yutaka", "trust", 4)
            chiasa "Aku baru turun dua menit lalu cari angin dari panggangan, terus dengar suaramu menyebut namaku, Ko-nii. Aku nggak berniat menguping, tapi kalau kamu memang merasa aku berubah, lebih baik bilang langsung ke depanku daripada bicara di dermaga gelap begini."
            nar "Koita terdiam kaku, tangannya yang sempat terangkat ke tengkuk berhenti di tengah udara. Yutaka menatapmu tenang, sedikit terkesan oleh ketegasanmu yang tidak berputar-putar."
            koita "...Maaf, Chi-chan. Aku nggak bermaksud membicarakanmu di belakang. Aku cuma bingung karena belakangan kamu kelihatan menyimpan banyak hal sendiri."
            yutaka "Bagus juga dibicarakan sekalian biar nggak jadi dugaan aneh-aneh. Ayo naik, di jalan atas tadi Kurosawa Meisa sempat lewat, nggak enak kalau obrolan keluarga jadi tontonan."
            chiasa "Iya. Kita naik saja, Ko-nii."
        elif _d2 == "nagisa_pergoki":
            $ kk_rel("nagisa", "trust", 4)
            $ kk_rel("nagisa", "jeal", -5)
            chiasa "Aku nggak lagi mencari Ko-nii dan nggak menyangka kamu sembunyi di sini, Nagisa-senpai. Aku salah kira dengar ada orang di bawah, ternyata kamu lagi sendirian. Maaf bikin kamu kaget."
            nar "Nagisa mengerjap cepat, kemarahan defensif di bahunya perlahan turun melihatmu tidak membalas dengan sindiran maupun tawa licik."
            nagisa "Hah? Cuma... cuma itu? Kamu beneran nggak bakal meledek aku duduk sendirian di dermaga?"
            chiasa "Buat apa? Kalau kamu mau duduk sebentar kena angin laut, aku temani lima menit, habis itu kita naik bareng sebelum yang lain bingung."
            nagisa "...Ya sudah. Duduk situ saja, jangan berisik. Tadi di atas agak terlalu ramai buat kepalaku."
        else:
            $ kk_rel("shiori", "trust", 4)
            $ kk_rel("miyuki", "trust", 4)
            chiasa "Maaf mengagetkan, Saionji-senpai, Tachibana-senpai. Aku turun cari udara karena asap barbekyu di atas lumayan pekat, dan baru sadar kalian di sini pas sandalku kepleset. Aku nggak bermaksud menguping sedikit pun."
            nar "Shiori menatap matamu dua detik penuh, mencari celah kebohongan, lalu menurunkan ketegangan di bahunya perlahan."
            shiori "Sikap yang cukup terbuka, Amamiya-san. Lagipula pembicaraan kami sudah hampir selesai. Sebaiknya kita naik bersama, tadi saya melihat Kurosawa Meisa melintas di jalan atas."
            miyuki "Iya, anginnya juga makin dingin di bawah sini. Ayo naik bareng, Chiasa-chan."
        nar "Kerugian malam itu berhasil kamu redam sebelum berubah menjadi luka baru, sementara satu fakta besar kini menancap tajam di kepalamu bahwa Sistem sama sekali tidak memegang kendali mutlak atas perubahan orang-orang di pulau ini."
    elif _return == "B":
        $ store.deviasi += 4
        nar "Alih-alih mengakui salah langkah, kamu memasang senyum santai yang sedikit terlalu tenang, memutar keadaan seperti permainan sosial di pesta."
        if _d2 == "koita_yutaka":
            chiasa "Wah, serius banget sih topiknya di dermaga gelap begini? Ko-nii kebanyakan minum kaleng buah di atas sampai jadi sensitif begitu ya? Yuk naik, di beranda Moemoe-senpai sama Nagisa-senpai nanyain kenapa kamu lama banget cuma ambil penjepit."
            koita "Aku nggak mabuk, Chi-chan... dan tadi itu bukan soal penjepit."
            nar "Kamu sengaja tertawa ringan lalu melangkah lebih dulu kembali ke beranda vila, menarik perhatian rombongan dengan mengangkat kaleng minuman dingin dan menggoda Koita soal kelakuannya yang menghilang dari panggangan."
            moeka "Lho, Kocchi ke mana saja sih dari tadi? Jagungnya hampir gosong semua lho!"
            nagisa "Iya, Ko-kun bilang cuma ke dapur sebentar, tahu-tahu malah turun ke pantai segala!"
            nar "Di bawah pengaruh minuman buah dan tawa berisik beranda, sorotan langsung berbalik menekan Koita hingga ia salah tingkah membela diri, sementara Yutaka memandangmu diam-diam dari pinggir meja dengan alis sedikit berkerut."
        elif _d2 == "nagisa_pergoki":
            chiasa "Lho, kenapa Nagisa-senpai malah curiga ke aku? Bukannya barusan Ko-nii yang bilang mau ke dapur lalu menghilang entah ke mana? Aku turun justru mau ngecek dia kabur dari tugas bakar jagung atau nggak."
            nagisa "Tunggu... Ko-kun menghilang dari atas?! Jangan bilang dia jalan ke pantai sebelah tanpa bilang siapa-siapa!"
            nar "Dengan satu kalimat enteng dan sisa efek minuman buah dari beranda, seluruh curiga Nagisa langsung meleset dari dirimu dan menghantam Koita. Kalian naik kembali ke teras tepat saat Koita baru muncul dari ruang tamu, memicu rentetan pertanyaan tajam Nagisa di depan semua orang."
            koita "Eh, bentar, aku cuma mengangkat telepon sebentar di ruang dalam kok, kenapa semua jadi lihat ke sini?"
            nar "Di luar pagar taman bawah, langkah Kurosawa Meisa melambat sebentar mendengar suara perdebatan yang merembes dari beranda terang, sementara sorot mata Koita akhirnya tertuju penuh curiga ke arahmu."
        else:
            chiasa "Wah, maaf bikin kaget! Di atas Ko-nii baru saja menghilang dari panggangan entah ke mana sementara anak-anak mulai agak pusing habis minum kaleng buah, jadi aku kira dia turun ke sini. Rupanya cuma Saionji-senpai sama Tachibana-senpai."
            shiori "...Kamu menyebut nama kakakmu cepat sekali untuk ukuran orang yang datang mengendap di tangga gelap, Amamiya-san."
            nar "Kamu tertawa ringan tanpa goyah, mengajak mereka naik dan segera menghidupkan lagi obrolan beranda dengan menawarkan gelas tambahan serta menyinggung soal Koita yang selalu menghilang di saat semua orang menunggu."
            miyuki "Eh, Chiasa-chan, kalengnya jangan diminum terlalu cepat, nanti besok pagi pusing..."
            nar "Tawa beranda kembali ramai oleh obrolan setengah mabuk, sementara Shiori tidak menyentuh minumannya sedikit pun dan mencatat satu garis baru dalam diam ketika Koita tampak makin terpojok."
        nar "Kamu lolos dari jebakan data usang Sistem malam ini, tetapi api kecil baru saja menyala di bawah atap vila dan gema suaranya sempat terdengar sampai ke jalan penginapan bawah."
    else:
        $ store.sikap_sistem["selidik"] = store.sikap_sistem.get("selidik", 0) + 2
        if _d2 == "koita_yutaka":
            $ kk_rel("koita", "trust", -3)
        elif _d2 == "nagisa_pergoki":
            $ kk_rel("nagisa", "trust", -3)
        else:
            $ kk_rel("shiori", "trust", -3)
        chiasa "Maaf mengganggu. Aku cuma salah jalur waktu cari angin. Aku naik duluan."
        nar "Kamu berbalik sebelum siapa pun sempat mengejar penjelasan lebih panjang. Panggilan pelan dari belakang kamu biarkan tertelan suara ombak saat kakimu menaiki tangga samping menuju kamar lantai dua."
        play sound "audio/sfx/door_close.wav"
        nar "Begitu pintu kayu kamar tertutup dan ruangan kembali sunyi, kamu duduk di tepi kasur sambil menatap langit-langit gelap. Napasmu perlahan kembali teratur."
        chiasa "{i}Keluar sekarang. Aku tahu kamu masih mendengar.{/i}"
        $ kk_bgm("system")
        play sound "audio/sfx/system_open.wav"
        nar "Udara di depan jendela kamar bergetar tipis, memunculkan jendela kaca biru dengan emotikon menopang dagu yang tampak sedikit terganggu."
        sistem "(¬_¬ ) Kau memanggilku cuma buat mengeluh soal sandalmu yang basah kena embun? Sudah kubilang, salinan naskah aslinya memang bergeser sejak kau mulai ikut campur."
        chiasa "{i}Artinya kamu tidak benar-benar bisa membaca masa depan mereka lagi. Setiap kali pilihan kami berubah, radarmu ketinggalan di belakang.{/i}"
        nar "Garis cahaya neon pada layar biru itu sempat berkedip patah satu ketukan sebelum kembali menyeringai tajam."
        sistem "( ` v ´ ) Jangan besar kepala, Manusia. Aku mungkin tidak selalu peduli posisi duduk setiap pion di pantai, tapi jam wisuda dan angka evaluasimu tetap ada di tanganku. Coba saja main-main."
        play sound "audio/sfx/system_close.wav"
        nar "Layar itu menutup cepat, terasa lebih terburu-buru dibandingkan biasanya. Meski malam ini meninggalkan tanda tanya dingin di bawah sana, kamu baru saja menemukan satu kelemahan nyata di balik kesombongan Sistem."
    return


# ══════════════════════════════════════════════════════════════════════════
# HARI 3 · Badai Tropis di Vila — Semua Rute Bertabrakan
# ══════════════════════════════════════════════════════════════════════════
label kk_pulau_hari3(_focus):
    $ _d3 = kk_pulau_day3_branch()
    $ _fear_cid, _fear_val = kk_pulau_max_fear_heroine()
    call kk_scene_enter("chiasa", "Ruang Tengah Vila Pulau · Badai Hari 3")
    $ kk_bgm("tension")
    play sound "audio/sfx/rain.wav"
    nar "Siang menjelang sore hari ketiga, langit biru di atas teluk mendadak tertutup awan kelabu pekat. Hujan badai Agustus mengguyur atap kayu vila dengan suara bergemuruh, memaksa seluruh rombongan membatalkan rencana pantai dan berkumpul terkurung di ruang tengah."
    nar "Lampu langit-langit sempat berkedip satu kali saat guntur jauh bergema. Aroma teh panas bercampur bau hujan lembap, tetapi tidak satu pun obrolan terasa ringan seperti hari pertama. Sisa ketegangan dari malam kedua dan seluruh beban yang menumpuk sejak di kota kini duduk di satu ruangan yang terlalu sempit."
    if _d3 == "distorsi_tekanan":
        nar "Dentingan porselen pecah tiba-tiba terdengar dari arah dapur terbuka. Semua kepala langsung menoleh ke meja konter."
        if _fear_cid == "miyuki" or stage.get("miyuki", 0) >= 3 or kk_has("miyuki_rasa_salah_dimanfaatkan"):
            nar "Miyuki berjongkok buru-buru di lantai dapur dengan tangan gemetar memunguti pecahan cangkir teh, wajahnya pucat sekali dengan mata cokelat kemerahan yang tampak kelelahan."
            miyuki "Maaf, maaf banget semuanya! Aku ceroboh sampai cangkirnya jatuh. Nanti kuganti sama pemilik vila, maaf bikin suasana hujan jadi berantakan..."
            chiasa "{i}Jarinya nyaris menyentuh pecahan keramik tajam dan ia masih sibuk meminta maaf ke seisi ruangan.{/i}"
            yutaka "Tachibana-senpai, berhenti dulu! Jangan diambil pakai tangan kosong, nanti robek jarimu!"
            shiori "Tachibana-senpai, sejak kemarin sore kamu hampir tidak beristirahat karena terus mengerjakan catatan tambahan di kamar. Siapa yang menumpuk pekerjaan di jadwal liburanmu seperti itu?"
            nar "Pertanyaan tenang Shiori jatuh seperti batu ke lantai ruang tengah. Mata Miyuki sempat melirik singkat penuh takut ke arahmu sebelum buru-buru menunduk lagi, dan Yutaka langsung menangkap arah tatapan itu."
        elif kk_has("beasiswa_terancam"):
            nar "Di dekat konter dapur, Moeka terhuyung pelan menumpukan kedua tangannya di pinggir meja kayu sambil memegangi pelipisnya. Daftar pengeluaran dan berkas kuliahnya berserakan di sisi tas."
            moeka "Eh, maaf banget semuanya, aku cuma agak pusing sedikit... nggak apa-apa kok, nanti malam aku tetap bisa bantu masak!"
            miyuki "Moeka-chan, bibirmu pucat sekali! Kamu tadi pagi belum makan dan semalam begadang mengerjakan revisi kuliah ya?"
            shiori "Kamu memaksakan diri ikut liburan sekaligus mengejar beasiswa tanpa bilang apa-apa. Amamiya-san, kamu kan satu fakultas dengannya, bukankah kamu tahu batas kondisinya?"
            nar "Semua mata bergeser di antara Moeka yang berusaha menyalakan senyum ceria paksa dan posisimu di dekat sofa."
        else:
            nar "Di sudut meja makan, Harumi berdiri kaku dengan tangan mencengkeram map catatan yang ujungnya basah terkena tumpahan teh, napasnya pendek sementara ia terus mengulang bahwa ia akan menjadwal ulang segalanya."
            harumi "Kesalahan koordinasi ini tanggung jawab saya. Saya bisa menunda pengiriman berkas riset gelombang pertama bila memang mengganggu rencana di sini."
            yutaka "Kujo-san, tunggu dulu. Kenapa kamu tiba-tiba bicara soal menunda pendaftaran risetmu di tengah liburan?"
            shiori "Menarik. Kujo-san tidak pernah menunda tenggat akademik tanpa alasan besar. Ada seseorang yang memintamu mengubah jadwalmu?"
            nar "Tatapan Harumi melirik singkat ke arahmu, membuat seluruh ruang tengah mendadak sunyi selain suara hujan badai di luar kaca."
    elif _d3 == "rumor_curiga":
        play sound "audio/sfx/phone_vibrate.wav"
        nar "Ponsel Moeka dan Nagisa di atas meja rendah bergetar hampir bersamaan. Moeka yang paling dulu membuka layar langsung kehilangan senyum cerianya."
        moeka "Eh... tunggu. Di grup obrolan mahasiswa ada unggahan foto buram dari dermaga pulau ini semalam. Tulisannya menyebut inisial anak klub Sastra yang bikin banyak orang merasa jadi satu-satunya, terus di komentar bawah ada yang ikut menyeret nama keluarga Saionji sama foto kerjaanku di studio Kuga!"
        nar "Koita langsung pucat dan meraih ponselnya sendiri. Ia menggulir layar beberapa detik, lalu perlahan menurunkan ponselnya dan menatap lurus ke arahmu."
        koita "Di foto ini kelihatan sudut tangga vila kita, dan jam unggahnya persis tidak lama sesudah kejadian di dermaga semalam. Ini pasti ulah Kurosawa Meisa yang kita lihat di feri."
        nagisa "Kok dia bisa tahu persis jam kita ribut di beranda?! Tunggu... semalam kan cuma ada beberapa orang yang turun ke tangga bawah!"
        shiori "Menarik sekali. Semalam ada yang turun ke dermaga tepat ketika Kurosawa Meisa lewat, lalu keributan berpindah ke beranda terbuka. Amamiya-san, mungkin kamu mau menjelaskan urutan kejadiannya dengan lebih utuh kali ini?"
        nar "Yutaka menyilangkan tangan di depan dada, matanya yang abu-abu gelap menatapmu dan Koita bergantian dengan serius. Di luar jendela, hujan memukul kaca makin keras."
    else:
        nar "Ketika lampu ruang tengah sempat meredup oleh guntur, suasana sunyi yang canggung menggantung di sekitar meja rendah. Koita menaruh cangkir tehnya pelan dan akhirnya mengangkat wajah menatapmu."
        koita "Chi-chan... aku mau tanya satu hal di depan semua orang, soalnya kalau kupendam terus rasanya makin aneh."
        koita "Sejak hari pertama sampai di pulau ini, tiap aku mengajak ngobrol, rasanya ada jarak yang nggak pernah ada dulu. Bahkan Nagisa-chan dan teman-teman yang lain lebih sering langsung menoleh ke kamu daripada ikut rencanaku."
        nagisa "Tunggu dulu, Ko-kun! Kenapa kamu tiba-tiba bawa namaku ke situ? Aku cuma... akhir-akhir ini memang lebih nyambung bicara sama Chiasa daripada harus menebak-nebak jadwalmu yang selalu nggak jelas!"
        nar "Ruangan langsung terdiam mendengar kalimat Nagisa yang keluar terlalu cepat dan jujur. Wajah Nagisa memerah terang, tetapi ia tidak menarik ucapannya kembali. Ia justru menoleh ke arahmu dengan mata biru cerah yang menuntut satu jawaban pasti."
        nagisa "Lagipula, Chiasa, kamu sendiri yang sejak festival kemarin terus bersikap beda banget. Sebenarnya kamu mau berdiri di pihak siapa di sini?"
        yutaka "Hei, pelan-pelan dulu kalian berdua. Di luar lagi badai, nggak ada gunanya semua orang saling menyudutkan di ruang tengah."
        nar "Shiori menatap seluruh meja dari balik cangkirnya, sementara Miyuki dan Harumi sama-sama terdiam memperhatikan setiap gerakmu."
    nar "Seluruh mata di ruang tengah vila tertuju padamu. Di luar kaca, hujan badai menutup jalan keluar pulau sampai esok pagi. Pilihanmu sekarang akan mengunci bagaimana empat hari ini berakhir di dermaga besok."
    call kk_family_menu("C17b_H3", ["Lindungi orang yang paling terdesak dan hentikan tekanan di depan semua orang.", "Manfaatkan kekacauan ini untuk memisahkan Koita dari yang lain dan mengunci narasi versimu.", "Ajak satu orang terdekat keluar ke serambi belakang untuk bicara empat mata dengan jujur."])
    if _return == "A":
        $ store.deviasi += 3
        nar "Kamu berdiri dari sofa dengan gerak tenang dan tegas, memotong lingkaran tatapan yang makin mencekik di ruang tengah."
        if _d3 == "distorsi_tekanan":
            $ kk_rel(_fear_cid, "trust", 5)
            $ kk_rel(_fear_cid, "fear", -5)
            chiasa "Berhenti dulu semuanya. Jangan menyidang orang yang jelas-jelas lagi kelelahan di lantai dapur begini."
            nar "Kamu mengambil sapu kecil dan tisu tebal, lalu berlutut di samping orang yang gemetar itu sambil menggeser tangannya pelan menjauh dari pecahan keramik dan berkas yang basah."
            chiasa "Kalau ada jadwal atau permintaan yang terlalu berat selama ini, itu salahku karena nggak ikut membatasi dari awal. Sekarang duduk dulu di kursi, minum air hangat, nggak ada yang boleh minta maaf satu kali pun lagi malam ini."
            miyuki "...Chiasa-chan..."
            nar "Bahu yang sejak tadi tegang itu akhirnya turun dengan helaan napas gemetar. Yutaka segera mengambilkan kain lap kering membantumu, sementara Shiori mengangguk pelan dengan raut yang jauh lebih melunak."
            shiori "Mengakui bagian tanggung jawab sendiri di depan ruangan memang lebih sulit daripada mencari alasan. Bagus, Amamiya-san."
        elif _d3 == "rumor_curiga":
            $ kk_rel("koita", "trust", 4)
            $ kk_rel("nagisa", "trust", 4)
            chiasa "Kurosawa Meisa sengaja memotong sudut foto dari jauh supaya kelihatan seperti skandal. Semalam aku memang turun ke dermaga karena salah dengar ada orang di bawah, dan kalau kalian mulai saling curiga di ruang tengah ini, itu persis yang dia inginkan buat bahan gosip di kampus."
            nar "Kamu melangkah ke meja dan menunjuk layar ponsel Moeka dengan tenang."
            chiasa "Fotonya bahkan nggak menunjukkan wajah jelas siapa pun. Kalau kita kompak nggak terpancing komentar grup, unggahannya bakal tenggelam sendiri sebelum kapal pulang besok."
            shiori "Analisis yang masuk akal. Dan saya bisa memastikan grup resmi fakultas tidak memperbesar rumor tanpa bukti."
            koita "...Iya. Maaf aku tadi langsung panik dan hampir menyalahkanmu, Chi-chan. Makasih sudah meredam sebelum makin kacau."
            nagisa "Hmph... benar juga. Enak saja Kurosawa Meisa mengacak-acak liburan kita cuma modal foto buram."
        else:
            $ kk_rel("nagisa", "trust", 5)
            $ kk_rel("koita", "trust", 3)
            chiasa "Jangan memaksa Nagisa-senpai atau siapa pun memilih kubu di ruang tengah begini, Ko-nii. Kalau orang-orang mulai bicara lebih terbuka denganku, itu karena aku dengar mereka sampai selesai tanpa mengalihkan topik."
            nar "Koita tertegun sejenak, wajahnya meredup oleh kejujuran kalimatmu tanpa ada nada mengejek sedikit pun."
            koita "...Jadi selama ini aku yang terlalu sering mengalihkan pembicaraan ya."
            nagisa "Aku nggak bilang kamu orang jahat, Ko-kun. Cuma... kadang capek kalau harus terus menebak jawabanmu."
            chiasa "Sekarang hujan masih deras, lebih baik kita hangatkan sup sisa makan siang dulu daripada semuanya duduk kaku begini."
            nar "Yutaka tersenyum tipis dan bangkit ke dapur menghidupkan kompor, mencairkan sebagian besar ketegangan yang nyaris meledak di ruangan itu."
    elif _return == "B":
        $ store.deviasi += 7
        $ store.runtuh_koita += 5
        if kk_get("daftar_kebohongan_shiori", 0) > 0:
            $ kk_adj("daftar_kebohongan_shiori", 1)
        nar "Kamu tidak menenangkan badai di ruangan itu. Kamu justru berdiri tenang di tengah cahaya redup dan mengarahkan setiap retakan kecil tepat ke titik paling rapuh di meja."
        chiasa "Kenapa semua orang kelihatan kaget sih? Dari awal liburan ini juga jelas kok sumber masalahnya selalu di tempat yang sama. Setiap kali Ko-nii nggak pernah berani memberi kepastian, orang-orang di sekitarnya yang akhirnya menanggung canggung, rumor, sampai capek sendiri."
        koita "Chi-chan... tunggu dulu, kenapa kamu ngomong seolah-olah semua hal yang terjadi di vila ini salahku sendiri?!"
        chiasa "Buktinya kemarin di festival siapa yang bikin dua orang menunggu bersamaan? Dan malam ini siapa yang langsung panik begitu satu foto buram muncul di grup? Aku cuma bilang fakta yang dari tadi ditahan semua orang."
        nar "Suasana di ruang tengah langsung membeku tajam. Moeka menunduk meremas tali tasnya, Miyuki menggigit bibirnya pelan, dan Nagisa memandangi Koita dengan ragu yang sulit disembunyikan."
        shiori "Cara yang cukup tajam untuk memutus perdebatan, Amamiya-san. Kamu memindahkan seluruh beban pertanyaan dari dirimu sendiri ke bahu kakakmu dalam satu kalimat."
        yutaka "Chiasa, itu agak keterlaluan. Kita lagi terkurung hujan di satu rumah, nggak perlu membuat Koita terpojok di depan semua teman-temannya."
        nar "Koita berdiri kaku beberapa detik, matanya yang hitam gelap memandangmu dengan rasa tidak percaya yang dingin sebelum ia berbalik melangkah naik ke lantai dua tanpa mengucapkan sepatah kata lagi."
        play sound "audio/sfx/door_close.wav"
        nar "Pintu kamar di lantai atas tertutup pelan. Di bawah, tidak ada satu pun yang menyusulnya naik. Kamu baru saja meretakkan pusat orbit Koita secara terang-terangan di depan semua orang, dengan harga yang akan segera menagih di kampus nanti."
    else:
        $ _target = "koita" if kk_has("chiasa_arah_success") else ("yutaka" if kk_has("chiasa_arah_yutaka") else _focus)
        $ kk_rel(_target, "intim", 6)
        $ kk_rel(_target, "trust", 4)
        nar "Kamu tidak membiarkan percakapan pribadi habis terbakar menjadi tontonan satu ruangan. Kamu melangkah tenang mendekati orang yang paling banyak memenuhi pikiranmu selama tiga hari ini dan menyentuh ujung lengannya pelan."
        chiasa "Ikut aku ke serambi belakang sebentar. Di dalam terlalu banyak telinga, kita bicara berdua saja."
        nar "Kalian melangkah keluar melalui pintu kaca geser menuju serambi beratap kayu yang terlindung dari hujan deras. Tirai air jatuh beberapa langkah di depan pagar kayu, menenggelamkan suara ruang tengah di belakang."
        if _target == "koita":
            koita "Chi-chan... aku kira tadi kamu bakal ikut menyudutkanku di dalam."
            chiasa "Aku nggak mau ribut di depan teman-teman, Ko-nii. Aku memang berubah dibanding tahun lalu, dan aku nggak mau pura-pura cuma jadi adik kecil yang ikut ketawa supaya suasana aman."
            koita "Jujur, aku takut kehilangan rasa rumah yang biasa kita punya. Tapi mendengar kamu bilang langsung di sini... jauh lebih tenang daripada menebak-nebak sendirian."
            chiasa "Kalau begitu jangan lari ke alasan aman lagi waktu bicara denganku, Ko-nii."
            nar "Koita menatap matamu lama di bawah suara hujan yang rata, lalu mengangguk pelan tanpa senyum canggungnya yang biasa."
        elif _target == "yutaka":
            yutaka "Menarik juga kamu malah menarikku keluar dari badai di dalam, Chiasa. Kirain aku cuma kebagian tugas jadi penengah lagi."
            chiasa "Yutaka-kun satu-satunya orang di dalam tadi yang nggak langsung termakan panik. Aku cuma butuh lima menit bicara sama orang yang kepalanya dingin."
            yutaka "Hehe, anggap saja itu pujian. Tapi kamu juga kelihatan tegang banget sejak malam kemarin. Ada sesuatu yang lagi kamu simpan sendirian?"
            chiasa "Ada beberapa hal yang belum bisa kuceritakan sekarang. Tapi makasih sudah nggak ikut menekan aku di dalam tadi."
            nar "Yutaka bersandar pada tiang serambi sambil menatapmu tenang dengan mata abu-abu gelapnya, memberi ruang sunyi yang anehnya terasa paling aman di seluruh vila."
        elif _target == "nagisa":
            nagisa "Chiasa... di dalam tadi suaraku kelewat keras ya? Habisnya tiap lihat semua orang muter-muter nggak jelas, kepalaku ikut panas."
            chiasa "Nggak apa-apa, Nagisa-senpai. Justru aku senang kamu bicara jujur daripada memendam sampai menangis sendiri di kamar."
            nagisa "H-hei, siapa yang nangis?! ...Tapi iya. Belakangan ini aneh banget, tiap ada masalah aku malah cari wajahmu duluan buat lihat kamu bakal bilang apa."
            chiasa "Kalau begitu nggak usah bingung soal pihak mana yang kupilih. Aku berdiri di sini sama kamu sekarang, kan?"
            nar "Rona hangat naik cepat di pipi Nagisa di tengah udara hujan yang dingin. Ia membuang muka sebentar ke tirai hujan sambil menyembunyikan senyum kecilnya."
        elif _target == "miyuki":
            miyuki "Maaf merepotkanmu keluar hujan-hujan begini, Chiasa-chan. Tadi di dalam aku benar-benar panik..."
            chiasa "Tachibana-senpai, dengar aku baik-baik. Selama sisa perjalanan ini, berhenti merasa bersalah untuk hal yang nggak kamu sebabkan. Kamu nggak harus jadi sempurna supaya aku mau berdiri di sampingmu."
            miyuki "...Kamu sungguh memaksudkan kalimat itu, Chiasa-chan? Bahkan waktu aku kelihatan rapuh seperti barusan?"
            chiasa "Justru karena itu aku mengajakmu keluar ke sini. Tarik napas dulu, nggak ada jadwal bangsal di balik hujan ini."
            nar "Miyuki menutup matanya sebentar, lalu menyandarkan bahunya pelan ke tiang kayu di dekatmu dengan senyum tipis yang akhirnya tulus."
        elif _target == "moeka":
            moeka "Aduh, Chimian, maaf banget kalau di dalam tadi aku bikin suasananya makin tegang. Aku cuma takut banget semua orang tahu kepalaku lagi penuh masalah."
            chiasa "Moemoe-senpai nggak perlu pasang topeng ceria di depanku. Di luar sini nggak ada kamera, nggak ada Kurosawa Meisa, cuma suara hujan."
            moeka "...Rasanya pengin nangis sebentar aja boleh nggak? Nggak usah lama-lama, dua menit aja sebelum kita masuk lagi."
            chiasa "Boleh. Aku jaga pintu kaca biar nggak ada yang keluar."
            nar "Moeka menunduk menyeka sudut matanya cepat dengan punggung tangan, lalu mengangkat wajah menatapmu dengan kepercayaan yang jauh lebih dalam dari sebelumnya."
        elif _target == "harumi":
            harumi "Terima kasih sudah memberi jeda di luar, Amamiya-san. Kebisingan ruangan tertutup saat konflik emosional membuat proses berpikir saya turun drastis."
            chiasa "Di sini lebih tenang kan, Kujo-senpai? Kamu nggak harus mengambil keputusan soal masa depan atau jadwal risetmu cuma karena merasa terutang budi ke siapa pun."
            harumi "...Variabel yang paling sulit saya ukur ternyata memang rasa ingin dipercaya oleh satu orang tanpa syarat. Kamu membuat variabel itu terasa jauh lebih masuk akal."
            nar "Harumi membetulkan kacamatanya perlahan, ujung telinganya memerah samar di balik kepang perak sampingnya."
        else:
            shiori "Kamu menarik saya keluar dari ruang tengah tepat di puncak ketegangan, Amamiya-san. Langkah yang berani."
            chiasa "Saionji-senpai paling tahu bagaimana cara menilai situasi tanpa ikut panik. Aku cuma ingin memastikan kita nggak saling salah baca soal kejadian semalam dan hari ini."
            shiori "Saya menghargai orang yang memilih percakapan langsung daripada sandiwara bertele-tele. Untuk saat ini, saya akan menilai tindakanmu dari apa yang benar-benar kamu perbuat, lepas dari gosip luar."
            nar "Shiori menatap tirai hujan sejenak lalu melirikmu dengan senyum tipis yang tenang, menandai batas kepercayaan baru di antara kalian."
        nar "Ketika hujan badai mulai reda menjelang malam, percakapan sunyi di serambi itu tetap tinggal jauh lebih lama daripada keributan di dalam ruangan."
    return


# ══════════════════════════════════════════════════════════════════════════
# HARI 4 · Dermaga Pulang — Percabangan Hasil & Catatan Celah Sistem
# ══════════════════════════════════════════════════════════════════════════
label kk_pulau_hari4(_focus):
    $ _out = kk_pulau_day4_outcome()
    call kk_scene_enter("chiasa", "Geladak Feri Pulang · Hari 4 Pulau")
    if _out in ("retak_meisa", "jejak_takut"):
        $ kk_bgm("aftermath")
    else:
        $ kk_bgm("intimacy")
    nar "Pagi hari keempat menyingsing sangat bersih sesudah badai semalam. Langit biru terang membentang di atas teluk yang kembali tenang, memantulkan cahaya perak di sepanjang permukaan air ketika kapal feri pulang merapat di dermaga pulau."
    "Petugas Feri" "Penumpang tujuan daratan utama silakan naik ke dek atas! Kita berangkat tepat lima menit lagi!"
    nar "Seluruh koper sudah masuk ke bagasi bawah. Angin laut pagi bertiup kencang di geladak terbuka ketika kapal perlahan melepas tali tambat dan pulau hijau di belakang mulai mengecil. Namun susunan orang-orang yang berdiri di sepanjang pagar dek tidak lagi sama dengan saat kalian berangkat empat hari lalu."
    if _out == "retak_meisa":
        $ kk_flag("pulau_koita_curiga_berat")
        nar "Koita berdiri sendirian di ujung depan dek sambil memegangi pagar besi dengan kedua tangan. Ia tidak ikut bergabung di lingkaran minuman dingin seperti biasanya, dan setiap kali matanya melintas ke arahmu, senyum kakaknya yang hangat tidak lagi muncul."
        koita "Begitu sampai daratan nanti aku langsung pulang duluan ya, Chi-chan. Aku ada beberapa hal yang harus kupikirkan sendiri sebelum semester mulai lagi."
        nar "Beberapa meter di bangku dek belakang, Kurosawa Meisa duduk santai memakai kacamata hitam sambil mengetik cepat di layar ponselnya. Saat pandangannya berpapasan denganmu, sudut bibirnya terangkat tipis seperti orang yang baru saja pulang membawa cerita besar."
        shiori "Jejak empat hari ini tidak akan berhenti di dermaga, Amamiya-san. Persiapkan dirimu begitu kita kembali menginjak gerbang kampus bulan depan."
        chiasa "{i}Koita curiga berat, dan Kurosawa Meisa pulang membawa bahan. September di kampus nanti tidak akan berjalan tenang.{/i}"
    elif _out == "jejak_takut":
        $ kk_flag("pulau_jejak_takut")
        nar "Di bangku sampingmu, orang yang selama dua hari terakhir terus menekan dirinya sendiri duduk sangat tegak dengan kedua tangan terlipat rapi di atas tas. Ia langsung bangkit menawarkan diri membawakan minuman dingin begitu melihatmu menggeser tali tas."
        miyuki "Kamu mau duduk di bangku yang teduh, Chiasa-chan? Biar aku saja yang berdiri dekat pagar, jangan sampai kamu kena angin terlalu kencang."
        nar "Kepatuhan yang terlalu cepat itu tidak terdengar seperti kelegaan liburan. Di ujung dek sebelah kanan, Yutaka memandangi adegan kecil itu tanpa senyum jahilnya yang biasa. Matanya yang abu-abu gelap menatapmu lurus beberapa detik sebelum ia memalingkan wajah ke arah laut."
        chiasa "{i}Mereka tidak lagi berputar di sekitar Koita, tapi cara mereka menatapku sekarang lebih dekat ke rasa takut mengecewakan daripada kepercayaan.{/i}"
    elif _out == "orbit_bergeser":
        $ store.deviasi += 5
        $ kk_flag("pulau_orbit_bergeser")
        nar "Di pagar dek yang menghadap garis pantai, rombongan mengobrol jauh lebih ringan sambil berbagi kaleng minuman dingin. Tanpa diminta siapa pun, lingkaran obrolan itu mengalir alami ke sekitarmu."
        if _focus == "nagisa":
            nagisa "Anginnya kencang banget, pitaku hampir lepas lagi... Eh, Chiasa, habis turun kapal nanti kamu langsung pulang atau mampir beli oleh-oleh dulu? Aku mau beli kue jeruk buat Onii-chan."
        elif _focus == "miyuki":
            miyuki "Empat hari ini rasanya cepat sekali lewatnya ya, Chiasa-chan. Untuk pertama kalinya aku pulang liburan dengan kepala yang benar-benar agak ringan."
        elif _focus == "moeka":
            moeka "Foto langit pascabadai barusan bagus banget, Chimian! Nanti sampai daratan kukirim semua ke kamu duluan ya sebelum masuk grup!"
        elif _focus == "harumi":
            harumi "Saya sudah menandai empat pengamatan menarik dari perjalanan ini, Amamiya-san. Salah satunya adalah bahwa beristirahat bersama orang yang tepat tidak menurunkan efisiensi berpikir."
        else:
            shiori "Perjalanan yang jauh lebih teratur dari dugaan awal saya, Amamiya-san. Saya cukup menantikan bagaimana kamu menghadapi semester depan."
        nar "Di sisi kiri pagar, Koita melihat keakraban itu dengan senyum tipis yang agak sepi. Tidak ada ledakan amarah, hanya kesadaran sunyi bahwa tempat yang dulu otomatis menjadi miliknya kini sudah bergeser tanpa sempat ia tahan. Yutaka menepuk bahu Koita singkat, lalu mengangguk tenang ke arahmu."
    else:
        $ kk_flag("pulau_retak_halus")
        nar "Di sepanjang pagar geladak, semua orang tampak kembali berbagi kue kering dan bercanda tentang badai semalam seolah liburan berjalan biasa saja. Moeka memotret burung laut, Nagisa berdebat kecil dengan Yutaka soal oleh-oleh, dan Koita tertawa singkat menanggapi mereka."
        nar "Namun di balik tawa yang tampak wajar itu, kamu bisa membaca setiap jeda kecil yang tersisa. Shiori sesekali melirik ke bangku belakang tempat Kurosawa Meisa duduk, Koita lebih cepat mengecek reaksimu setiap kali bicara, dan kamu sendiri pulang dengan satu pengetahuan baru yang tidak dimiliki siapa pun di kapal ini."
        chiasa "{i}Permukaannya terlihat tenang, tapi retakannya sudah terbentuk di bawah dek. Dan yang paling penting, aku baru melihat sendiri bahwa data Sistem bisa meleset.{/i}"
    play sound "audio/sfx/phone_buzz.wav"
    nar "Tepat saat kapal berbelok mendekati pelabuhan utama, ponsel di tasmu kembali bergetar dua kali sementara ponsel Moeka ikut berbunyi menerima pesan susulan dari Ryena soal katalog foto studio Kuga. Nagisa yang berdiri tidak jauh darimu sempat berhenti merapikan pitanya dan melirik tasmu dengan kening sedikit berkerut sebelum cepat-cepat memalingkan wajah."
    nar "Garis dermaga daratan utama mulai tampak jelas di cakrawala depan. Sebelum peluit tanda merapat berbunyi dan seluruh rombongan kembali ke rutinitas kampus bulan September, kamu menentukan satu langkah terakhir yang kamu bawa pulang dari pulau ini."
    call kk_family_menu("C17b_H4", ["Simpan catatan soal data usang Sistem dan susun langkahmu sendiri ke depan.", "Hampiri orang yang paling banyak berubah di sisimu sebelum kapal merapat.", "Hadapi Kurosawa Meisa sebentar di jalur keluar dek sebelum ia menghilang ke stasiun."])
    if _return == "A":
        $ store.sikap_sistem["selidik"] = store.sikap_sistem.get("selidik", 0) + 2
        nar "Kamu bersandar di pagar besi menghadap angin laut, merangkai ulang seluruh urutan kejadian sejak malam kedua di dalam kepalamu. Setiap kali kamu menggeser keputusan orang secara nyata, naskah lama di dalam radar Sistem langsung menjadi usang."
        chiasa "{i}Jadi aku tidak harus selalu menari mengikuti jebakan misi darimu. Kalau aku paham bagaimana manusia di sini bergerak, aku bisa melangkah satu putaran di depan radarmu.{/i}"
        $ kk_bgm("system")
        play sound "audio/sfx/system_open.wav"
        nar "Panel kaca biru berkedip singkat di sudut pandangmu, jelas menangkap arah pikiranmu dengan emotikon menyipit tajam."
        sistem "(¬_¬ ) Misi Pulau tercatat selesai. Dan berhenti tersenyum puas begitu, Sampah Peron. Celah kecil di satu liburan tidak menghapus kontrakmu. Lihat saja apakah kau masih sesombong itu waktu rumor kampus meledak bulan depan~"
        play sound "audio/sfx/system_close.wav"
        nar "Layar itu padam dengan dengung lebih pendek dari biasanya. Kamu menegakkan bahu, siap turun ke dermaga dengan kepala jauh lebih dingin."
    elif _return == "B":
        $ kk_rel(_focus, "intim", 4)
        $ kk_rel(_focus, "trust", 3)
        nar "Kamu melangkah menyusuri dek yang mulai ramai oleh penumpang bersiap turun dan berdiri sejajar di samping orang yang paling banyak berbagi momen bersamamu sepanjang empat hari ini."
        chiasa "Terima kasih sudah ikut sampai selesai di pulau ini. Minggu depan kampus sudah mulai ramai lagi, jangan lupa istirahat cukup begitu sampai rumah."
        if _focus == "nagisa":
            nagisa "I-iya, kamu juga! Jangan langsung begadang bikin sketsa habis pulang begini, nanti mukamu kayak zombie lagi. ...Makasih juga buat empat hari ini, Chiasa."
        elif _focus == "miyuki":
            miyuki "Terima kasih banyak, Chiasa-chan. Nanti kalau sudah sempat di kampus, kita minum teh bersama lagi tanpa terburu-buru jadwal ya."
        elif _focus == "moeka":
            moeka "Pasti dong, Chimian! Habis ini aku bakal lebih rajin atur jadwal supaya nggak bikin kamu cemas lagi. Makasih banget ya buat liburan ini!"
        elif _focus == "harumi":
            harumi "Saya akan menyimpan catatan perjalanan ini dengan baik, Amamiya-san. Terima kasih sudah tidak memaksa saya memakai standar orang lain."
        else:
            shiori "Kamu pun jaga ritmemu, Amamiya-san. Bulan depan sepertinya akan cukup menarik di kampus, dan saya rasa kita masih akan sering berdiskusi."
        $ kk_bgm("system")
        play sound "audio/sfx/system_open.wav"
        sistem "( ´ v ` ) Misi Pulau ditutup. Lumayan juga hasilnya, meski kau sempat terpeleset sendiri di malam kedua. Kita lihat berapa lama kedamaian manis ini bertahan bulan depan~"
        play sound "audio/sfx/system_close.wav"
    else:
        nar "Begitu kapal merapat dan jalur penumpang mulai bergerak turun menuju gerbang dermaga, kamu mempercepat langkah dua meter hingga sejajar tepat di samping Kurosawa Meisa yang sedang menggulir ponselnya."
        chiasa "Liburan yang kebetulan sekali ya, Kurosawa-san. Menginap lima menit dari vila kami, naik feri pulang yang sama juga."
        nar "Langkah Meisa terhenti setengah ketukan. Ia menurunkan kacamata hitamnya sedikit dan tersenyum tipis yang terasa terlatih."
        "Kurosawa Meisa" "Oh, Amamiya Chiasa ya? Pulau ini kan memang ramai tiap Agustus. Nggak ada larangan mahasiswi lain ikut menikmati pemandangan dermaga malam-malam."
        chiasa "Tentu saja nggak ada larangan. Cuma sekadar mengingatkan, foto buram dari jarak jauh gampang sekali kelihatan berbeda dari kejadian aslinya. Apalagi kalau ada nama keluarga Saionji di dalam rombongan yang sama."
        nar "Kilat kaget yang sangat tipis melintas di mata Meisa mendengar nama Saionji disebut setenang itu. Senyumnya tetap terpasang, tetapi jarinya berhenti mengetik di layar ponsel."
        "Kurosawa Meisa" "Tenang saja, aku cuma mencatat hal yang memang sudah jadi pembicaraan orang-orang kok. Sampai ketemu di kampus bulan depan, Amamiya-san."
        nar "Ia melangkah cepat mendahului antrean keluar gerbang. Kamu tahu peringatan barusan tidak akan menghentikan rumor September sepenuhnya, tetapi setidaknya ia kini sadar kamu melihatnya jelas di pulau ini."
        $ kk_bgm("system")
        play sound "audio/sfx/system_open.wav"
        sistem "( ` v ´ )b Misi Pulau selesai. Berani juga kau menyentil penyebar gosip kampus langsung di dermaga. Mari kita lihat apakah itu menahan badainya atau malah membuat ia makin bersemangat bulan depan~"
        play sound "audio/sfx/system_close.wav"
    nar "Begitu kakimu kembali menginjak aspal di luar gerbang pelabuhan menuju stasiun, hawa kota yang panas langsung menyergap. Liburan pulau empat hari berakhir, meninggalkan jejak yang tidak akan hilang ketika bulan September dimulai."
    return
