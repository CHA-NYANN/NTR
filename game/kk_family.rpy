# Draft editorial. Event_Miyuki, Event_Nagisa, Event_Yutaka dan Alur_Cabang/01,02,08,13.
# Adegan keluarga memakai aksi dari katalog. Mesin hanya meresolusi kondisi
# yang memiliki sumber state, sehingga epilog yang belum terhubung tidak direka.
init python:
    def kk_family_bond():
        # Alur_Cabang/08: dasar 30; Y17-A tetap berlaku pada save sebelumnya.
        return max(0, min(100, 30 + pts.get("perubahan_kisaragi", 0) + (10 if kk_has("job_family") else 0)))

    def kk_change_family(delta):
        current = kk_family_bond()
        pts["perubahan_kisaragi"] = pts.get("perubahan_kisaragi", 0) + max(0,min(100,current+delta)) - current

    def kk_amamiya_bond():
        # Master Canon §5.3: Yutaka lebih nyaman bersama keluarga Amamiya. Dasar 45; Y13 menggerakkannya.
        return max(0, min(100, 45 + pts.get("perubahan_amamiya", 0)))

    def kk_change_amamiya(delta):
        current = kk_amamiya_bond()
        pts["perubahan_amamiya"] = pts.get("perubahan_amamiya", 0) + max(0,min(100,current+delta)) - current

    def kk_yutaka_relation_ending(bond=None, crime=None):
        # E-YH-03 Keluarga Pilihan (Alur_Cabang/08): hubungan keluarga Amamiya tinggi, tanpa kejahatan.
        # Membaca flag yang dicatat Y13. bond/crime bisa dioverride untuk uji dua keadaan.
        if kk_host != "yutaka":
            return None
        if bond is None:
            bond = kk_amamiya_bond()
        if crime is None:
            crime = kk_has("force_pernah") or kk_has("saionji_masuk_tanpa_izin")
        if bond >= 60 and not crime:
            return "E-YH-03"
        return None

    def kk_miyuki_sham_ending(palsu=None, diakui=None, terbongkar=None):
        # Alur_Cabang/01: pasangan palsu (Mi09-B). Diakui jujur di Mi18-C -> E-MI-13;
        # terbongkar oleh Takeru (Mi18-B) -> E-MI-14.
        if palsu is None:
            palsu = kk_has("pasangan_palsu")
        if not palsu:
            return None
        if diakui is None:
            diakui = kk_has("sandiwara_diakui")
        if terbongkar is None:
            terbongkar = kk_has("sandiwara_terbongkar")
        if diakui:
            return "E-MI-13"
        if terbongkar:
            return "E-MI-14"
        return None

    def kk_family_choice(eid, key):
        if not kk_record_choice(eid, key):
            return
        if eid == "Mi07":
            kk_adj("omiai_takeru", {"A":5,"B":10,"C":0}[key])
            if key == "B":
                kk_flag("pemain_menghalangi")
            if key == "C":
                kk_rel("miyuki","trust",5)
        elif eid == "Mi09":
            if key == "B":
                kk_flag("pasangan_palsu")
                kk_adj("omiai_takeru",-15)
            elif key == "A":
                kk_rel("miyuki","trust",5)
            else:
                kk_adj("omiai_takeru",5)
        elif eid == "Mi18":
            if kk_has("pasangan_palsu"):
                if key == "C":
                    kk_flag("sandiwara_diakui")
                elif key == "B":
                    kk_flag("sandiwara_terbongkar")
            kk_adj("omiai_takeru",5 if key == "A" else -5)
        elif eid == "Mi25":
            kk_flag({"A":"hayase_engaged","B":"hayase_interrupted","C":"left_with_miyuki"}[key])
        elif eid == "N21":
            kk_flag("haruto_sekutu" if key == "A" else "haruto_lawan")
        elif eid == "N23":
            kk_flag({"A":"koko_dikembalikan","B":"koko_di_meja","C":"koko_dibawa_ke_haruto"}[key])
        elif eid == "N-D09":
            kk_adj("kelekatan_nagisa", {"A":10,"B":5,"C":-5}[key])
            if key == "B":
                kk_flag("moeka_menjahit_koko")
        elif eid == "N22":
            kk_flag("nagisa_family_visit" if key == "A" else "nagisa_family_declined")
        elif eid == "Y09":
            kk_change_family({"A":10,"B":-10,"C":-5}[key])
            if key == "C":
                kk_flag("saionji_disebut_ke_ayah")
        elif eid == "Y-D03":
            kk_change_family({"A":10,"B":-5,"C":10}[key])
        elif eid == "Y-D08":
            kk_change_family({"A":5,"B":0,"C":-5}[key])
        elif eid == "Y13":
            kk_flag({"A":"makan_bersama_amamiya","B":"menghindari_amamiya","C":"bicara_dengan_amamiya"}[key])
            kk_change_amamiya({"A":15,"B":-15,"C":20}[key])
        elif eid == "Y17":
            kk_flag({"A":"job_family","B":"job_outside","C":"intern_abroad"}[key])

    def kk_nagisa_ending():
        if kk_has("force_nagisa"):
            return "E-NA-12"
        # Koita memilih Nagisa (K26).
        if kk_has("koita_pilih_nagisa"):
            return "E-NA-03"
        # Rute Yandere (hanya bila gerbang N14+ ditempuh).
        if kk_has("rute_yandere_nagisa") or stage.get("nagisa",0) >= 5:
            if kk_has("nagisa_senjata_aktif") and kk_bulan >= 35:
                return "E-NA-14"
            if kk_has("nagisa_distorted"):
                return "E-NA-06"
            if kk_has("nagisa_jebakan_dipasang"):
                return "E-NA-11"
            if kk_has("yuuto_disabotase"):
                return "E-NA-05"
            if kk_has("nagisa_rumah_diterima"):
                return "E-NA-04"
            if kk_has("nagisa_ditolak_keras"):
                return "E-NA-08"
            if kk_has("nagisa_valentine_sendiri"):
                return "E-NA-13"
            if kk_has("nagisa_diterima"):
                return "E-NA-10"
        if kk_has("nagisa_family_visit") or kk_has("haruto_sekutu"):
            return "E-NA-07"
        if (stage.get("nagisa",0) <= 2 and kk_has("nagisa_pulih")
                and not kk_has("romansa_nagisa")):
            return "E-NA-02"
        if (stage.get("nagisa",0) <= 3 and kk_has("nagisa_koita_ditolak")
                and kk_rel_get("nagisa","aff") > kk_npc_rel.get("harapan_koita",70)
                and kk_rel_get("nagisa","trust") >= 55 and not kk_get("luka_bohong")):
            return "E-NA-01"
        if stage.get("nagisa",0) <= 2 and not kk_has("pengkhianatan_geng") and not kk_has("force_pernah"):
            return "E-NA-09"
        return None

    def kk_orbit_delta():
        score = 0
        if kk_miyuki_ending() in ("E-MI-05","E-MI-13","E-MI-01"):
            score += 25
        if kk_nagisa_ending() == "E-NA-01":
            score += 25
        if kk_harumi_ending() == "E-HA-01":
            score += 25
        return score

    def kk_miyuki_ending():
        if kk_has("lock_romance_miyuki"):
            return None
        if kk_has("force_miyuki"):
            return "E-MI-12"
        if kk_has("left_with_miyuki"):
            return "E-MI-05"
        if kk_has("hayase_engaged"):
            return "E-MI-04"
        # Koita memilih Miyuki (K26).
        if kk_has("koita_pilih_miyuki"):
            return "E-MI-03"
        # Rute Masokis (hanya bila gerbang Mi16-C+ ditempuh).
        if kk_has("pola_masokis_permanen"):
            return "E-MI-07"
        if kk_has("rute_masokis_miyuki") and kk_has("koita_menggantung_miyuki"):
            return "E-MI-09"
        if kk_has("sena_memutus"):
            return "E-MI-11"
        if kk_has("rute_masokis_miyuki"):
            if kk_has("miyuki_sato_dikenal") or kk_has("miyuki_cuti"):
                return "E-MI-10"
            return "E-MI-08"
        if (kk_get("kelelahan_miyuki",35) >= 90 and not kk_has("cbt_miyuki_lulus")
                and stage.get("miyuki",0) >= 4):
            return "E-MI-06"
        sham = kk_miyuki_sham_ending()
        if sham:
            return sham
        if (stage.get("miyuki",0) <= 3 and kk_rel_get("miyuki","aff") >= 55 and
                kk_rel_get("miyuki","trust") >= 55 and kk_get("sena_curiga") < 60):
            return "E-MI-01"
        if (stage.get("miyuki",0) <= 2 and kk_has("cbt_miyuki_lulus")
                and kk_get("karier_miyuki",70) >= 40 and not kk_has("force_miyuki")):
            return "E-MI-02"
        return None

# ┌─ PANDUAN CERITA · Mi07 · Takeru Muncul
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : omiai pertama dari orang tua.
# │ INTI    : A dukung Takeru / B halangi / C jujur ke Miyuki.
# │ AKHIRAN : omiai_takeru.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi07:
    call kk_scene_enter("miyuki","Rumah Sakit Tachibana")
    nar "Miyuki membawa undangan makan yang dicetak terlalu resmi untuk sekadar pertemuan kenalan. Nama keluarga Hayase tertulis di samping nama keluarganya. Namanya sendiri muncul hanya sekali."
    miyuki "Takeru kenalan lama keluarga. Ibu bilang kami sebaiknya saling mengenal lebih serius. Kata seriusnya sudah ditentukan sebelum aku ditanya."
    nar "Ia memegang amplop dengan rapi, seperti masih bisa menjaga pertemuan itu tetap kecil jika kertasnya tidak kusut."
    call kk_family_menu("Mi07", ["Dengarkan apa yang Takeru tawarkan.", "Minta mereka memberi Miyuki ruang.", "Katakan terus terang apa yang kaupikir."])
    if _return == "A":
        nar "Kau menyarankan mendengar tawaran Takeru terlebih dahulu. Miyuki mengangguk, menemukan alasan yang bisa diterima semua orang untuk hadir."
        miyuki "Iya. Mendengar bukan berarti menyetujui. Aku harus ingat itu ketika mereka mulai bicara seolah sudah ada keputusan."
        nar "Ia menyimpan undangan, tetapi tidak tampak lebih lega. Satu pertemuan lagi kini punya cukup pembenaran untuk terjadi."
    elif _return == "B":
        nar "Kau meminta keluarga memberi Miyuki ruang. Keberatanmu segera menjadi bahan percakapan baru tentang siapa yang memengaruhinya."
        miyuki "Aku senang kamu memikirkan aku. Tapi setelah ini aku tetap yang harus menjawab mereka. Aku ingin kamu tahu bagian itu juga."
        nar "Penolakan yang datang dari luar justru membuat keluarganya ingin mempercepat pertemuan, seolah kedekatan dapat dijamin sebelum Miyuki sempat berubah."
    else:
        nar "Kau mengatakan terus terang bahwa pertemuan seperti itu hanya layak jika ia bebas menerima atau menolak tanpa dianggap tidak tahu terima kasih. Miyuki membaca undangan itu sekali lagi."
        miyuki "Aku ingin mendengar seseorang mengatakan bagian itu. Bukan hanya dia orang baik, jangan mengecewakan keluarga."
        nar "Ia tidak langsung memutuskan. Namun kini ia tahu kau tidak akan menganggap kepatuhannya sama dengan keinginan."
    return

# ┌─ PANDUAN CERITA · Mi09 · Natal: Pesta Rumah Sakit
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : acara orang tua.
# │ INTI    : A menemani / B tampil sebagai pasangan palsu / C tidak datang.
# │ AKHIRAN : hub besar #3.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi09:
    call kk_scene_enter("miyuki","Pesta rumah sakit")
    nar "Dari balik pintu pesta terdengar nama Miyuki disebut bersama kata membanggakan. Ia berdiri di luar dengan rambut rapi dan tangan dingin, menunda masuk dengan membetulkan gelang yang tidak longgar."
    miyuki "Di dalam aku akan ditanya kuliah, rencana masa depan, lalu Takeru. Urutannya selalu begitu. Kadang aku ingin mereka langsung ke pertanyaan terakhir supaya nggak perlu berpura-pura."
    nar "Ia menatapmu, mencoba tersenyum."
    miyuki "Kamu datang sebagai teman saja sudah membantu. Aku cuma ingin ada orang yang tahu aku gugup sebelum melihatku tersenyum di sana."
    call kk_family_menu("Mi09", ["Temani dia masuk.", "Tawarkan berpura-pura menjadi pasangannya.", "Pamit sebelum pesta dimulai."])
    if _return == "A":
        nar "Kau menemaninya masuk dengan perkenalan yang sederhana. Saat keluarganya mulai mengarahkan pembicaraan, ia sempat melihatmu dan mengingat bahwa seseorang telah mendengar jawaban yang lebih jujur di luar."
        miyuki "Aku belum memutuskan soal itu, Bu. Hari ini aku ingin mengenalkan temanku dulu."
        nar "Kalimatnya sopan. Jeda sesudahnya cukup tegang untuk menunjukkan bahwa ia baru saja melakukan sesuatu yang biasanya dihindari."
    elif _return == "B":
        nar "Kau menawarkan berpura-pura menjadi pasangan. Miyuki memandang pintu, kemudian dirimu, menimbang kelegaan sesaat terhadap percakapan yang akan menyusul."
        miyuki "Kalau mereka bertanya lagi nanti, kita harus mengingat kebohongan yang sama. Kamu paham, kan?"
        nar "Ia tetap menyetujui. Ketika memperkenalkanmu, tangannya mencengkeram lenganmu terlalu kuat. Keluarganya terkejut; untuk malam itu, rencana tentang Takeru akhirnya kehilangan arah."
    else:
        nar "Kau pamit sebelum pesta dimulai. Miyuki melepas lengan yang tadi hampir diraihnya, lalu mengucapkan selamat malam dengan nada senpai yang rapi."
        miyuki "Terima kasih sudah mengantar. Aku bisa masuk sendiri."
        nar "Ia menunggu kau berbalik sebelum membuka pintu. Dari celahnya terdengar sambutan yang langsung menempatkannya di antara orang-orang yang telah merencanakan tempat duduknya."
    return

# ┌─ PANDUAN CERITA · Mi18 · Natal Kedua: Lamaran Terselubung
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : keluarga Hayase hadir.
# │ INTI    : A hadir / B halangi / C menawarkan alternatif.
# │ AKHIRAN : omiai_takeru naik.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi18:
    call kk_scene_enter("miyuki","Pertemuan keluarga")
    nar "Keluarga Hayase datang dengan bingkisan dan pilihan tanggal untuk acara berikutnya. Pertemuan belum dimulai, tetapi di meja sudah ada terlalu banyak benda yang membuat penolakan terasa seperti merusak pekerjaan banyak orang."
    miyuki "Mereka bilang ingin mendengar jawabanku. Lalu menanyakan bulan mana yang kosong sebelum aku menjawab."
    nar "Ia menarik kursi sendiri, tidak menunggu orang lain menentukan tempatnya."
    if kk_has("pasangan_palsu"):
        miyuki "Mereka masih ingat kita datang bersama tahun lalu."
        call kk_family_menu("Mi18", ["Duduk di samping Miyuki seperti tahun lalu.", "Minta Takeru menunda pembicaraan.", "Ceritakan mengapa kalian datang bersama tahun lalu."])
    else:
        call kk_family_menu("Mi18", ["Tetap hadir di pertemuan itu.", "Minta mereka menunda pembicaraan.", "Bicarakan dengan jujur alternatif yang kalian punya."])
    if kk_has("sandiwara_diakui"):
        miyuki "Kita ceritakan dari awal. Termasuk bagian saat berpura-pura. Aku nggak ingin meminta mereka menghormati pilihanku sambil terus memberi cerita yang palsu."
        nar "Ia menyampaikan kebenaran itu tanpa menyembunyikan keterlibatannya di balik namamu. Orang tua mereka marah; Takeru berhenti menyentuh bingkisan di depannya."
        miyuki "Aku tahu itu salah. Aku ingin memperbaikinya dengan jujur, bukan dengan menerima rencana lain karena malu."
    elif kk_has("sandiwara_terbongkar"):
        "Takeru" "Sebentar. Miyuki, waktu itu kalian benar-benar berpacaran?"
        miyuki "Waktu itu? Tidak."
        nar "Miyuki menarik kursinya sedikit menjauh. Kini kedua keluarga menunggu dia melanjutkan."
        nar "Ia mencoba menjelaskan tekanan yang membuat kebohongan itu terasa sebagai jalan keluar. Semakin ia berbicara, semakin jelas keluarganya sedang mendengar persoalan kehilangan muka, bukan keinginan putri mereka."
        miyuki "Aku seharusnya bicara lebih awal. Tapi bukan berarti karena aku berbohong, sekarang aku nggak boleh menolak apa pun lagi."
    elif kk_has("pasangan_palsu"):
        nar "Miyuki menggeser kursi untukmu. Pertanyaan tentang hubungan kalian dijawab dengan kebiasaan yang sudah dilatih. Sesekali ia melihatmu untuk memastikan tidak ada rincian yang berbeda."
        nar "Keluarga itu meneruskan pembicaraan dengan syarat baru, sementara kalian mempertahankan sandiwara yang kini memerlukan masa depan sendiri agar tetap dipercaya."
    else:
        nar "Miyuki mendengarkan tanggapan keluarga dan menyebut bahwa keputusan akhirnya belum diberikan. Ia berusaha memisahkan sopan santun dari persetujuan yang terus diasumsikan semua orang."
        miyuki "Aku datang karena ingin membicarakan ini. Kalau jawabannya sudah dianggap ada sebelum aku bicara, pertemuan ini untuk siapa?"
        nar "Pertanyaannya menghentikan meja untuk beberapa saat. Bukan kemenangan, tetapi sebuah ruang yang akhirnya harus diisi suaranya sendiri."
    return

# ┌─ PANDUAN CERITA · Mi25 · Natal: Pertunangan?
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : Takeru melamar.
# │ INTI    : A dukung / B halangi / C ajak kabur.
# │ AKHIRAN : ending Miyuki.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi25:
    call kk_scene_enter("miyuki","Natal · Keluarga Tachibana")
    nar "Takeru meletakkan kotak cincin di meja, belum membukanya. Orang tua kedua pihak mendadak punya urusan kecil untuk dikerjakan sambil tetap mendengar setiap napas."
    "Takeru" "Aku ingin jawabanmu, Miyuki. Keluarga kita sudah membicarakan banyak hal."
    miyuki "Keluarga kita, iya. Aku belum tahu apakah itu sama dengan kita berdua."
    nar "Tangannya diam di pangkuan. Di luar jendela lampu Natal menyala, tak peduli betapa sulit satu kata akan menjadi di dalam ruangan."
    call kk_family_menu("Mi25", ["Beri Miyuki dukungan untuk menerima.", "Minta Takeru berhenti mendesaknya.", "Tawarkan pergi bersama, jika ia menginginkannya."])
    if _return == "A":
        nar "Kau memberi dukungan untuk menerima. Miyuki memandangmu, lalu kotak di meja, mencari ketenangan pada persetujuan yang kini tampak datang dari semua arah."
        miyuki "Baik. Kita lanjutkan pembicaraan ini."
        nar "Kotak dibuka. Ucapan selamat mulai terdengar sebelum ia selesai menarik napas. Di wajahnya tersusun senyum yang sangat baik digunakan untuk foto keluarga."
    elif _return == "B":
        nar "Kau meminta Takeru berhenti mendesak. Ia sempat membantah bahwa dirinya hanya bertanya, tetapi Miyuki akhirnya mengangkat suara."
        miyuki "Aku merasa didesak. Tolong jangan jelaskan perasaanku sebelum aku selesai menyebutnya."
        nar "Pertemuan itu tidak berakhir dengan cincin dipasang. Ketegangan tinggal di meja, bersama hak menolak yang baru saja ia tuntut kembali dengan kata-katanya sendiri."
    else:
        nar "Kau menawarkan pergi bersamanya jika itu yang diinginkan. Miyuki tidak bergerak sampai tawaran tersebut selesai, tanpa janji bahwa akibatnya akan mudah."
        miyuki "Aku mau pergi. Bukan supaya kamu menang di depan mereka. Aku ingin berhenti menjawab hidupku seperti pertanyaan ujian yang cuma punya satu jawaban benar."
        nar "Ia berdiri, mengambil tasnya sendiri, lalu mengucapkan bahwa ia akan menghubungi keluarga ketika siap bicara. Pintu ditutup sebelum suara-suara yang saling memotong berhasil mengubah keputusannya."
    return

# ┌─ PANDUAN CERITA · N21 · Haruto Datang
# │ LOKASI  : Hunian Biasa · Rumah Sakurajima
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : kakak menyadari.
# │ INTI    : A jujur / B bohong / C konfrontasi.
# │ AKHIRAN : Haruto menjadi sekutu atau lawan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N21:
    call kk_scene_enter("nagisa","Rumah Sakurajima")
    nar "Haruto menunggu di teras dengan kemeja kerja yang belum diganti. Nagisa membukakan pintu dan mengatakan kalian boleh bicara, tetapi tidak perlu merendahkan suara seolah dirinya tidak ada di rumah."
    nagisa "Aku di dalam. Kalau ada yang perlu kutahu, panggil. Jangan selesai membuat keputusan baru bilang ke aku."
    if kk_has("haruto_kenal"):
        "Haruto" "Kita pernah ngobrol lewat telepon dulu, ya. Waktu itu kau menanggapiku dengan baik."
    "Haruto" "Akhir-akhir ini setiap kutanya bagaimana kuliahnya, dia malah bertanya kapan aku pulang. Apa yang terjadi?"
    call kk_family_menu("N21", ["Ceritakan apa yang kaulihat sendiri.", "Katakan semuanya biasa saja.", "Tanya kenapa dia baru datang sekarang."])
    if _return == "A":
        nar "Kau menceritakan apa yang kaulihat, termasuk bagian yang membuatmu tidak nyaman dengan tindakanmu sendiri. Haruto mendengarkan tanpa buru-buru membela atau menyalahkan."
        "Haruto" "Terima kasih. Aku akan dengar dari dia juga. Kalau perlu bantuan lain, kita cari. Aku nggak ingin ini berhenti sebagai obrolan dua orang di teras."
        nar "Ia memanggil Nagisa dengan suaranya yang biasa. Malam itu keluarganya mulai mendapat jalan masuk yang tidak hanya bergantung pada penyangkalan adiknya atau penjelasanmu."
    elif _return == "B":
        nar "Kau mengatakan semuanya biasa. Haruto melihat jendela ruang tengah sebelum membalas."
        "Haruto" "Kalau memang biasa, aku senang. Tapi yang kulihat sendiri nggak terasa begitu. Aku tetap akan bicara dengannya."
        nar "Ia tidak meminta persetujuanmu untuk memedulikan adiknya. Kebohongan itu hanya membuatnya lebih berhati-hati terhadap bagian hidup Nagisa yang melewati dirimu."
    else:
        nar "Kau mempertanyakan mengapa ia baru datang sekarang. Haruto terdiam, menerima bagian tuduhan yang memang menyentuh kesalahannya sebelum menatapmu kembali."
        "Haruto" "Aku terlambat melihat. Aku harus bertanggung jawab soal itu. Tapi keterlambatanku nggak menghapus pertanyaan tentang yang terjadi di sini."
        nar "Ia membuka pintu dan masuk menemui Nagisa. Percakapan kalian berakhir tanpa menjadi kerja sama yang sempat mungkin dibentuk."
    return

label kk_check_desk:
    if kk_desk_event(_lokasi) == "N23":
        call kk_play_scene("N23")
    elif kk_desk_event(_lokasi) == "N-D09":
        call kk_torn_koko
    else:
        return
    $ kk_minutes(10)
    return

# ┌─ PANDUAN CERITA · N23 · Koko di Meja Pemain
# │ LOKASI  : —
# │ TERLIBAT: nagisa (+ Koita bila relevan)
# │ AWALAN  : Koko muncul di kamar pemain.
# │ INTI    : A kembalikan / B simpan / C bawa ke Haruto.
# │ AKHIRAN : isyarat ekstrem.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N23:
    call kk_scene_enter("nagisa", "Kamar pemain · Koko di meja")
    nar "Koko duduk di atas mejamu, telinganya bersandar pada buku yang belum selesai kaubaca. Ketika kau keluar tadi, meja itu kosong. Tidak ada pesan yang meminta izin masuk."
    nar "Boneka yang begitu penting bagi Nagisa tampak hangat di tempat baru. Cara ia sampai ke sana membuat kehangatan itu terasa lain. Kini ada seseorang yang telah memutuskan kamarmu boleh dimasuki sebelum kau diberi kesempatan menjawab."
    call kk_family_menu("N23", ["Kembalikan Koko pada Nagisa.", "Simpan Koko di meja untuk sementara.", "Bawa Koko ke Haruto dan ceritakan di mana kau menemukannya."])
    if _return == "A":
        nar "Kau mengembalikan Koko dan menanyakan kedatangannya tanpa membiarkan pembicaraan berpindah ke apakah kau menyukai hadiah tersebut."
        nagisa "Aku ingin sesuatu dariku ada di sana. Kedengarannya berbeda kalau kamu bilang aku masuk tanpa izin."
        nar "Ia menerima boneka itu perlahan."
        nagisa "Iya. Lain kali tanya dulu. Aku dengar. Kamu boleh marah soal itu meskipun aku nggak bermaksud mengambil apa-apa."
    elif _return == "B":
        nar "Kau menyisihkan tempat untuk Koko. Nagisa mengirim pesan senang ketika mengetahui ia masih di sana, seolah kamar itu baru saja mengakui sebagian haknya."
        nar "Kau belum menjawab bagaimana ia boleh datang. Di antara buku dan lampu meja, boneka itu kini menampung persetujuan yang tidak pernah benar-benar dibicarakan."
    else:
        nar "Kau membawa Koko ke Haruto, menjelaskan di mana ia ditemukan dan bahwa kau tidak pernah mengundang Nagisa masuk. Haruto tidak menyebutnya sekadar perhatian berlebihan."
        "Haruto" "Baik. Aku akan tanyakan kepadanya. Kamu berhak merasa aman di kamar sendiri. Biar aku simpan dulu kalau kamu tidak ingin membawanya kembali."
        nar "Ia meletakkan boneka dengan hati-hati. Menangani batas yang dilanggar tidak mengharuskannya menghina benda yang dicintai adiknya."
    return

# ┌─ PANDUAN CERITA · N-D09 · Koko Robek
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Sakurajima Nagisa
# │ AWALAN  : Koko di tempat pemain, atau tahap ≥ 4
# │ INTI    : A Jahit sendiri / B minta Moeka menjahit / C beli yang baru
# │ AKHIRAN : kelekatan bergeser besar; Moeka yang menjahit bisa meredakan cemburu Nagisa padanya
# └─ tulis / perbaiki dialog di bawah ──
label kk_torn_koko:
    nar "Jahitan di sisi Koko terbuka. Isinya sedikit menyembul, menampilkan betapa lama boneka itu sudah dipeluk dan dibawa melewati hari-hari yang tidak disaksikan siapa pun."
    nar "Nagisa mencoba mengatakan bisa diperbaiki kapan saja. Tangannya terus menutup bagian yang robek, seolah malu bahwa sesuatu yang disayanginya terlihat rapuh di depanmu."
    call kk_family_menu("N-D09", ["Ambil benang dan jahit sendiri.", "Kirim pesan ke Moeka dan minta bantuannya menjahit.", "Cari boneka pengganti di toko."])
    if _return == "A":
        nar "Kau menawarkan memperbaiki dan menunggu Nagisa mengizinkan. Hasilnya miring, jelas berbeda dari jahitan lama, tetapi isi Koko tidak lagi keluar."
        nagisa "Kelihatan pernah rusak. Nggak apa-apa. Yang penting ini tetap dia."
        nar "Ia menyentuh bagian baru dengan hati-hati. Perhatianmu meninggalkan tanda yang tidak perlu berpura-pura sempurna agar berarti."
    elif _return == "B":
        nar "Moeka membalas pesan dengan foto gulungan benang. Ia meminta melihat robeknya, lalu menjelaskan bisa membantu tanpa harus mengganti bagian yang masih baik."
        moeka "Koko pulang dalam keadaan tetap Koko, ya. Bukan dapat makeover mendadak."
        nagisa "Terima kasih. Aku tahu aku kadang nggak ramah ke kamu. Soal itu... nanti aku bicara benar-benar."
        nar "Untuk satu sore, orang yang biasa ia pandang sebagai saingan menjadi seseorang yang memegang sesuatu miliknya dengan lembut."
    else:
        nar "Kau mencari pengganti di toko. Kelinci-kelinci baru bersih, simetris, dan tidak punya satu pun bekas yang diingat Nagisa."
        nagisa "Aku tahu maksudmu baik. Tapi aku nggak minta boneka yang lebih bagus. Aku ingin yang ini tetap ada."
        nar "Kau berdiri di antara pilihan yang mudah dibeli dan sesuatu yang tidak bisa diganti dengan kemiripan. Nagisa membawa Koko pulang tanpa memilih yang baru."
    return

# ┌─ PANDUAN CERITA · N22 · Natal: Rumah Sakurajima
# │ LOKASI  : Hunian Biasa · Rumah Sakurajima
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : orang tua Nagisa bertemu pemain.
# │ INTI    : A hadir / B menolak.
# │ AKHIRAN : jalur pemulihan melalui keluarga.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N22:
    call kk_scene_enter("nagisa","Rumah Sakurajima")
    nar "Nagisa membuka pintu sebelum kau menentukan bagaimana menyapa. Dari ruang makan terdengar orang tuanya menanyakan apakah tamu perlu tambahan nasi. Haruto menyahut bahwa mereka bisa bertanya langsung."
    nagisa "Mereka ada di rumah. Mereka ingin kenal orang yang sering kuceritakan. Aku sudah bilang jangan macam-macam, tapi itu biasanya nggak membantu."
    nar "Ia berusaha terdengar kesal. Tangan pada gagang pintu tidak melepaskannya, menunggu jawabanmu."
    call kk_family_menu("N22", ["Masuk dan sapa keluarganya.", "Berterima kasih lalu pamit."])
    if _return == "A":
        nar "Kau masuk dan menyapa keluarganya. Percakapan dimulai dengan makanan, lalu perlahan memberi ruang untuk kabar kuliah dan keadaan Nagisa yang belakangan tidak selalu mudah dibicarakan."
        nagisa "Aku masih di sini, ya. Kalau mau tanya tentangku, boleh tanya ke aku juga."
        nar "Ibunya menggeser kursi dan mempersilakannya duduk. Tidak semua jawaban langsung keluar, tetapi malam itu keluarga tidak hanya menjadi orang di balik pintu yang harus dijauhkan dari cerita."
    else:
        nar "Kau berterima kasih dan pamit. Nagisa menerima penolakan itu, meski sempat menatap ruang makan seperti harus menyiapkan penjelasan untuk kursi yang tetap kosong."
        nagisa "Baik. Hati-hati. Aku masuk dulu."
        nar "Pintu menutup. Kau tidak ikut dalam percakapan keluarga malam itu, tidak tahu apakah ia akan menceritakan yang sedang dialami atau hanya mengatakan tamunya kebetulan sibuk."
    return

# ┌─ PANDUAN CERITA · Y17 · Pilihan Karier
# │ LOKASI  : Distrik Elite · Apartemen Yutaka
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : — (kosong di katalog; bebas karang)
# │ INTI    : A perusahaan keluarga / B kerja di luar / C magang luar negeri.
# │ AKHIRAN : keluarga Kisaragi bereaksi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y17:
    call kk_scene_enter("yutaka","Apartemen Yutaka")
    nar "Di meja ada tawaran perusahaan keluarga dan beberapa lamaran lain. Ayah tidak menelepon untuk menyuruhmu menjawab, tetapi kau tahu ia menunggu. Ini bukan hanya persoalan siapa yang menanggung biaya hidupmu setelah lulus. Kau akan memakai nama Kisaragi untuk menjalani pekerjaan yang harus kaulakukan sendiri setiap pagi."
    call kk_family_menu("Y17", ["Jawab tawaran perusahaan keluarga.", "Kirim lamaran kerja ke perusahaan lain.", "Daftar untuk magang di luar negeri."])
    nar "Kau mengirim jawaban dan menyimpan salinannya. Untuk pertama kalinya, rencana setelah lulus berada di luar kepalamu. Akan ada orang yang kecewa atau lega, dokumen yang harus diurus, dan hari pertama ketika kau tidak bisa lagi menyebut semuanya sekadar kemungkinan."
    return

label kk_family_menu(eid, captions):
    $ _rows = [(caption, Return(key), False) for key,caption in zip("ABC",captions)]
    call screen kk_choice_panel(_rows, "Apa yang kau lakukan?")
    $ _decision = _return
    $ kk_family_choice(eid, _decision)
    return _decision


# Draft editorial. Event_Yutaka Y09/Y13; Alur_Cabang/08 Y-D03 dan Y-D08.
# ┌─ PANDUAN CERITA · Y-D03 · Ayah di Lobi
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kisaragi Yutaka
# │ AWALAN  : keluarga_kisaragi < 40
# │ INTI    : A Sambut / B hindari / C ajak bicara serius
# │ AKHIRAN : keluarga_kisaragi ±; Y17 bergeser
# └─ tulis / perbaiki dialog di bawah ──
label kk_visit_kisaragi:
    if not kk_father_visit("Apartemen Yutaka"):
        return
    call kk_scene_enter("yutaka", "Lobi apartemen")
    nar "Kenji Kisaragi duduk di lobi dengan tas kerja masih di sisinya. Kau mengenal wajahnya dari foto lebih baik daripada dari percakapan. Ketika ia berdiri, kau melihat betapa siapnya ia berangkat lagi, seolah kunjungan kepada anak sendiri harus diselipkan di antara dua urusan yang lebih pasti."
    call kk_family_menu("Y-D03", ["Sambut ayahmu.", "Lewati lobi tanpa menghampirinya.", "Duduk dan ajak ia bicara serius."])
    if _return == "B":
        nar "Kau melewati kesempatan menyapanya. Sesudah pintu lift menutup, kau memeriksa ponsel, mengharapkan pesan yang mungkin akan membuatnya tampak bersalah lebih dulu. Tidak ada yang masuk. Di lantai atas, apartemen kembali menyambutmu dengan kesunyian yang sudah kaukenal."
    elif _return == "C":
        nar "Kau meminta ia duduk dan mendengarkan tanpa terburu-buru. Kenji menyimpan ponselnya, kikuk menghadapi permintaan yang tidak dapat diselesaikan dengan transfer. Kau mengatakan bahwa kau ingin tahu apa yang ia harapkan darimu selain lulus. Jawabannya lambat; setidaknya kali ini kalian ada di tempat yang sama."
    else:
        nar "Kau menghampirinya dan menanyakan perjalanan ke sini. Ia bertanya tentang kuliah, lalu kehabisan topik. Kalian tetap berdiri bersama beberapa saat. Percakapan itu belum hangat, tetapi kau melihat usahanya mencari pertanyaan yang tidak terdengar seperti memeriksa laporan."
    return

# ┌─ PANDUAN CERITA · Y-D08 · Pesan dari Ibu
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kisaragi Yutaka
# │ AWALAN  : keluarga_kisaragi ≥ 40
# │ INTI    : A Balas hangat / B formal / C abaikan
# │ AKHIRAN : pintu kecil ke keluarga yang dingin
# └─ tulis / perbaiki dialog di bawah ──
label kk_message_kisaragi:
    if not kk_mother_message():
        return
    nar "Pesan ibu Kisaragi menanyakan apakah kau sudah makan dan bagaimana kuliahmu. Kau membaca ulang karena tidak ada urusan lain setelah pertanyaan itu. Kalimat sederhana dapat terasa mencurigakan ketika sudah terlalu lama orang hanya menghubungi untuk membicarakan kewajiban."
    call kk_family_menu("Y-D08", ["Ceritakan kabarmu dan tanyakan kabarnya.", "Balas singkat dengan sopan.", "Simpan ponsel tanpa membalas."])
    if _return == "A":
        nar "Kau menceritakan satu hal kecil dari harimu dan menanyakan kabarnya. Balasan pertama datang formal, lalu disusul cerita yang tidak perlu ia kirim jika hanya hendak menjalankan kewajiban. Kalian belum menjadi dekat. Ada sedikit ruang yang dibuka, dan untuk sekali ini tidak langsung kalian tutup."
    elif _return == "B":
        nar "Kau memberi kabar singkat bahwa semuanya baik. Ibu membalas agar menjaga kesehatan, lalu percakapan berhenti. Kalian telah menunaikan kesopanan tanpa mengetahui apakah ada yang ingin mengatakan lebih banyak."
    else:
        nar "Kau menyimpan ponsel tanpa membalas. Pesan itu tetap ada saat layar kembali menyala. Tidak menjawab memberimu kuasa menghentikan percakapan, tetapi tidak menjelaskan apa yang sebenarnya ingin kaudengar darinya."
    $ kk_minutes(1)
    return

# ┌─ PANDUAN CERITA · Y09 · Telepon Orang Tua Kisaragi
# │ LOKASI  : Distrik Elite · Apartemen Yutaka
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : ayah menanyakan rencana setelah lulus.
# │ INTI    : A jawab sopan / B bantah / C menyebut Saionji.
# │ AKHIRAN : hubungan_keluarga_kisaragi; C memberi tekanan ekstra.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y09:
    call kk_scene_enter("yutaka", "Apartemen Yutaka")
    nar "Ayah menelepon setelah jam makan malam. Ia menanyakan rencanamu sesudah lulus sebelum bertanya apakah kau sehat. Kau memandang buku kuliah yang masih terbuka. Di telinganya barangkali ada anak yang sudah dibesarkan untuk mengetahui jawabannya; di sini ada seseorang yang belum yakin berhak menyusun masa depan anak itu."
    call kk_family_menu("Y09", ["Jawab pertanyaannya dengan sopan.", "Katakan bahwa keputusan itu milikmu.", "Singgung keluarga Saionji."])
    if _return == "C":
        nar "Nama Saionji membuatnya berhenti. Ia menanyakan seberapa dekat kalian dan apakah keluarga Shiori mengenalmu. Kau mendengar percakapan pribadi berubah menjadi kemungkinan bisnis. Sekali nama itu kaupakai untuk mendapat perhatian, akan lebih sulit meminta ayah melupakan kepentingan yang sudah ia bayangkan."
    elif _return == "B":
        nar "Kau mengatakan keputusan itu milikmu. Ayah menanyakan apakah kau sudah memahami biaya dan tanggung jawabnya. Kalian terdengar seperti dua pihak yang sedang berunding, dan kau membenci sekaligus membutuhkan kejelasan itu. Kau mempertahankan jawaban tanpa mengaku sudah punya semua rencana."
    else:
        nar "Kau menjawab dengan sopan tentang hal yang sudah dipikirkan dan hal yang belum pasti. Ayah mendengar sampai selesai, lalu memberi beberapa saran. Tidak semuanya cocok untukmu, tetapi percakapan ini tidak berubah menjadi pertengkaran. Kau menutup telepon dengan pekerjaan rumah yang nyata, bukan sekadar rasa takut mengecewakannya."
    return

# ┌─ PANDUAN CERITA · Y13 · Daisuke dan Yoshie Pulang
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Saudara (host) (+ Koita bila relevan)
# │ AWALAN  : Natal kedua; orang tua Amamiya pulang mendadak.
# │ INTI    : A makan malam bersama / B menghindar / C membuka pembicaraan serius.
# │ AKHIRAN : menjadi gerbang Koita Success jika Chiasa NPC bersama Koita; atau menyetujui pemain.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Y13:
    call kk_scene_enter("yutaka", "Rumah Amamiya · Natal")
    nar "Koper Daisuke dan Yoshie masih berada dekat pintu. Mereka pulang lebih cepat, dan Yoshie sudah mengeluarkan piring tambahan ketika melihatmu. Kau berdiri di ambang ruang makan, mendadak sadar betapa sering rumah ini memberimu tempat tanpa meminta penjelasan mengapa apartemenmu sendiri terasa sulit didatangi."
    call kk_family_menu("Y13", ["Tarik kursi dan makan bersama mereka.", "Pamit sebelum makan malam.", "Minta waktu untuk bicara dari hati ke hati."])
    if _return == "A":
        nar "Yoshie menggeser lauk dan menyuruh Koita mengambilkan nasi untukmu. Daisuke bercerita tentang perjalanan, sementara Chiasa membetulkan kisah yang menurutnya dilebih-lebihkan. Tidak ada yang meminta kau menjadi tamu menarik. Kau makan sambil merasakan betapa berbahayanya menyukai rumah yang bisa hilang jika kepercayaan mereka kaurusak."
    elif _return == "C":
        nar "Kau meminta waktu untuk bicara sungguh-sungguh. Daisuke meletakkan sumpit, Yoshie menunggu tanpa mendesak. Kau mulai dari rasa takut kehilangan tempat di rumah ini. Mereka tidak langsung menjanjikan persetujuan untuk segala hal; mereka memberimu kesempatan menerangkan apa yang selama ini kauhindari."
    else:
        nar "Kau mengucapkan selamat Natal dan pamit sebelum duduk. Yoshie tidak memaksamu, hanya menanyakan apakah perlu membawakan makanan. Kebaikan itu hampir membuatmu kembali. Di luar, kau mendengar percakapan keluarga berlanjut dan sadar bahwa mereka dapat merindukanmu tanpa mengetahui alasanmu pergi."
    return
