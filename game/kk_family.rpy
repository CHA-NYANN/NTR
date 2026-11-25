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
        # terbongkar oleh Tatsuru (Mi18-B) -> E-MI-14.
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

# ┌─ PANDUAN CERITA · Mi07 · Tatsuru Muncul
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : omiai pertama dari orang tua.
# │ INTI    : A dukung Tatsuru / B halangi / C jujur ke Miyuki.
# │ AKHIRAN : omiai_takeru.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi07:
    call kk_scene_enter("miyuki","Rumah Sakit Tachibana")
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Malam itu kamu mampir ke kafe kecil di sudut lobi Rumah Sakit Tachibana untuk mengembalikan buku catatan anatomi warna milik Miyuki yang kemarin tertinggal di meja kantin kampus. Di bawah lampu hangat yang memantul ke dinding kaca menghadap taman gelap, Miyuki sudah duduk di meja pojok dan ia tampak tidak sedang sendirian."
        else:
            nar "Kamu mampir ke kafe kecil di sudut lobi Rumah Sakit Tachibana untuk mengembalikan buku catatan anatomi warna milik Miyuki yang kemarin tertinggal di meja kantin kampus. Saat kamu mendorong pintu kaca kafe, Miyuki sudah duduk di meja dekat dinding taman dalam, dan ia tampak tidak sedang sendirian."
        nar "Di seberang mejanya, seorang pria muda berusia sekitar dua puluh enam tahun dengan setelan jas dokter putih yang sangat rapi dan postur tegak baru saja berdiri sambil merapikan kancing jasnya. Begitu melihatmu berjalan mendekati meja, pria itu tersenyum sopan dan menggeser kursinya sedikit memberi ruang."
        "Tatsuru" "Oh, ini adik tingkat dari kampus yang tadi Anda sebutkan ya, Tachibana-san? Kalau begitu saya permisi kembali ke ruang jaga bedah dulu supaya kalian bisa mengobrol santai."
        miyuki "Terima kasih sudah menyempatkan turun, Hayase-san. Selamat bertugas kembali."
        "Tatsuru" "Sama-sama. Dan soal undangan makan malam keluarga akhir pekan nanti, tolong jangan dipikirkan terlalu berat ya, Tachibana-san. Saya tahu jadwal kuliah tahun ketiga Anda sedang padat, jadi saya sama sekali tidak keberatan menunggu sampai Anda siap."
        miyuki "Saya menghargai pengertian Anda, Hayase-san."
        "Tatsuru" "Kopi hangat Anda tadi sudah saya bayarkan di kasir sekalian. Selamat menikmati waktu istirahatnya, permisi."
        nar "Pria itu membungkuk sopan satu kali ke arahmu, lalu melangkah tenang meninggalkan kafe menuju deretan lift rumah sakit. Begitu pintu lift tertutup, bahu Miyuki yang sejak tadi lurus sempurna perlahan turun. Ia mengembuskan napas panjang dan meletakkan sebuah amplop kertas krem tebal yang tadinya ia pangku ke atas permukaan meja."
        chiasa "Ini buku catatan anatomi Senpai yang kemarin tertinggal di kantin. Ngomong-ngomong, siapa dokter yang barusan pergi itu, Tachibana-senpai? Asisten dosen Senpai di sini?"
        miyuki "Terima kasih sudah mengantarkan bukunya sampai ke sini, Chiasa-chan. Soal pria tadi... bukan asisten dosen. Namanya Hayase Tatsuru. Dia dokter residen bedah di rumah sakit rekanan milik teman lama ayahku."
        chiasa "Dia sampai membayarkan kopi Senpai di kasir juga ya, kelihatannya perhatian banget."
        miyuki "Dia memang selalu sehalus itu cara bersikapnya. Dari awal duduk tadi dia cuma menanyakan kabar kuliahku, memastikan aku nggak lupa makan siang, lalu bilang nggak masalah kalau aku butuh waktu."
        nar "Kamu duduk di kursi seberangnya sambil melirik kartu undangan yang menyembul setengah dari dalam amplop krem tersebut. Kertasnya tebal dengan huruf cetak timbul berwarna emas, jauh terlalu resmi untuk ukuran makan malam biasa. Di bagian tengahnya tertulis nama keluarga Hayase sejajar dengan nama keluarga Tachibana, sementara nama Miyuki sendiri hanya dicantumkan kecil di baris bawah."
        chiasa "Kertas undangannya tebal banget ya, Senpai, pakai cetakan huruf emas segala."
        miyuki "Tadi sekretaris Ibu mengantarkan amplop ini ke lobi fakultas, lalu barusan Hayase-san mampir sendiri buat menyapa waktu jadwal istirahat ruang bedah. Ibu bilang sudah waktunya kami berdua mulai saling mengenal untuk arah yang serius."
        chiasa "Arah yang serius... maksudnya ini undangan omiai, Senpai?"
        miyuki "Iya, pertemuan perjodohan keluarga. Yang bikin aku capek, kata serius di undangan ini sudah ditentukan bulat-bulat oleh kedua orang tua kami bahkan sebelum ada satu pun yang bertanya apakah aku ingin mengenal orangnya atau tidak."
        chiasa "Apalagi tadi cara Hayase-san bicara sopan dan sabar banget ya, Senpai?"
        miyuki "Justru itu yang paling bikin serba salah, Chiasa-chan. Dia sama sekali tidak kasar ataupun memaksa, jadi setiap kali aku merasa ingin menolak, aku malah langsung merasa jahat sendiri. Padahal kalau kupikir-pikir, di ruangan ini saja aku bahkan belum sempat pesan apa-apa, tapi jadwal akhir pekanku sudah tertulis rapi di kertas emas ini."
        chiasa "Tadi waktu Hayase-san datang ke meja ini, Senpai memang lagi istirahat atau sengaja dipanggil turun?"
        miyuki "Aku baru saja turun dari perpustakaan medis lantai tiga buat beli air mineral, terus tiba-tiba dia sudah menunggu di dekat kasir kafe sambil bawa pesan dari Ibu."
        chiasa "Jadi Senpai bahkan nggak dikasih tahu lebih dulu kalau dia mau mampir ke rumah sakit hari ini?"
        miyuki "Sama sekali nggak dikasih tahu. Ibu cuma kirim pesan singkat lima menit setelah Hayase-san duduk di depanku, mengingatkan supaya aku bersikap ramah karena keluarga Hayase sudah berbaik hati menyesuaikan jadwal dengan jam kuliahku."
        chiasa "Pantas saja bahu Senpai kelihatan tegang sekali waktu aku baru masuk pintu kafe tadi."
        miyuki "Rasanya kayak semua pintu keluar sudah ditutup pelan-pelan pakai senyum sopan, Chiasa-chan."
        nar "Miyuki merapikan kedua sisi amplop tebal itu dengan ujung jarinya, menjaga kertasnya tetap lurus di atas meja sambil menatapmu dengan raut bingung."
    else:
        if kk_slot >= 3:
            nar "Malam itu kamu mampir ke kafe lobi Rumah Sakit Tachibana untuk mengantarkan buku referensi Miyuki yang kemarin tertinggal selepas kelompok belajar. Dari balik dinding kaca kafe yang diterangi lampu kuning hangat, kamu melihat Miyuki sudah duduk di meja dekat taman dalam bersama seorang pria."
        else:
            nar "Kamu mampir ke kafe lobi Rumah Sakit Tachibana untuk mengantarkan buku referensi Miyuki yang kemarin tertinggal selepas kelompok belajar. Dari balik dinding kaca kafe, kamu melihat Miyuki sudah duduk di meja dekat taman dalam, dan ada seorang pria yang sedang berbicara dengannya."
        nar "Pria berusia pertengahan dua puluhan itu mengenakan jas dokter putih bersih di atas kemeja berdasi rapi. Ketika melihatmu melangkah menghampiri meja, ia segera berdiri dengan sikap santun dan tersenyum ramah."
        "Tatsuru" "Oh, ini teman kampusmu yang mau mengantar buku tadi ya, Tachibana-san? Kalau begitu saya permisi kembali ke bangsal bedah sekarang."
        miyuki "Terima kasih sudah meluangkan waktu istirahatnya, Hayase-san. Selamat kembali bertugas."
        "Tatsuru" "Tentu. Soal acara makan malam akhir pekan nanti, tidak perlu merasa terbebani ya, Tachibana-san. Saya paham Anda sedang fokus studi, jadi saya tidak keberatan menunggu."
        miyuki "Terima kasih atas pengertiannya, Hayase-san."
        "Tatsuru" "Minuman di meja sudah saya selesaikan di kasir tadi. Silakan dilanjutkan obrolannya, permisi."
        nar "Pria tersebut mengangguk sopan kepadamu sebelum berjalan menuju lorong lift utama. Setelah sosoknya tidak lagi terlihat, bahu Miyuki yang tadinya tegak rapi langsung melorot lelah. Ia menyandarkan punggungnya ke kursi dan menaruh sebuah amplop krem tebal dari pangkuannya ke atas meja kayu."
        yutaka "Ini buku referensimu, Tachibana-senpai. Siapa dokter yang barusan itu? Senpai pembimbing praktikmu?"
        miyuki "Makasih banyak sudah repot mengantarkannya, Yutaka-kun. Pria tadi bukan pembimbing praktikku. Itu Hayase Tatsuru, residen bedah berusia dua puluh enam tahun dari rumah sakit kolega ayahku."
        yutaka "Sopannya kebangetan ya, sampai minumanmu juga sudah dibereskan di kasir tanpa suara."
        miyuki "Dia memang selalu bersikap serapi itu. Sepuluh menit duduk tadi dia cuma menanyakan kuliahku, mengingatkan jangan telat makan, lalu bilang bersedia menunggu kapan pun aku siap."
        nar "Kamu menarik kursi di hadapannya dan melirik kartu undangan yang setengah terbuka dari amplop krem tersebut. Cetakan huruf timbulnya tampak sangat formal. Nama besar keluarga Hayase dan keluarga Tachibana terpampang mencolok di bagian atas, sedangkan nama Miyuki hanya tertulis satu kali sebagai keterangan tambahan di bawah."
        yutaka "Undangan makan malam biasa nggak bakal dicetak setebal itu pakai huruf emas ya, Senpai."
        miyuki "Ibu menyuruh orang mengantarkan amplop ini tadi. Katanya keluarga kami dan keluarga Hayase sepakat sudah saatnya kami berdua menjalin perkenalan yang serius."
        yutaka "Perkenalan resmi keluarga... maksud Senpai semacam omiai?"
        miyuki "Iya. Lucunya, kesimpulan bahwa pertemuan ini serius sudah mereka ketok palu duluan di antara orang tua, tanpa pernah sekali pun menanyakan pendapatku lebih dulu."
        yutaka "Tadi dokter itu kelihatannya ramah dan tenang sekali."
        miyuki "Itu justru bagian yang paling melelahkan, Yutaka-kun. Karena dia orang yang sopan dan tidak pernah menuntut macam-macam secara langsung, aku jadi merasa bersalah sendiri tiap kali hatiku menolak. Rasanya semua orang sudah menyusun jadwal hidupku dengan sopan sampai aku bingung di mana letak suaraku sendiri."
        yutaka "Tadi Senpai memang sudah janji ketemu dia di kafe lobi ini atau dia datang mendadak?"
        miyuki "Dia datang mendadak waktu aku baru turun dari ruang baca lantai tiga. Lima menit kemudian pesan Ibu masuk ke ponselku, menyuruhku menyambut Hayase-san dengan baik karena beliau sudah meluangkan waktu di sela jadwal bedahnya."
        yutaka "Jadi semuanya sudah diatur rapi dari belakang tanpa memberi Senpai celah buat menghindar."
        miyuki "Iya, bahkan kopi di depanku ini sudah dipesankan sebelum aku sempat duduk."
        nar "Miyuki memegang tepi amplop kaku itu dengan kedua tangannya, menatap kertas undangan tersebut dengan senyum tipis yang tampak tertekan."
    call kk_family_menu("Mi07", ["\"Kelihatannya Hayase-san sopan sih, nggak ada salahnya dengerin dulu maksudnya.\"", "\"Kalau Senpai belum siap, minta aja mereka kasih ruang dulu.\"", "\"Pertemuan kayak gini cuma masuk akal kalau Senpai bebas nolak tanpa dicap nggak tahu terima kasih.\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Kalau dilihat sekilas tadi, kelihatannya Hayase-san orangnya cukup sopan dan nggak memaksa sih, Tachibana-senpai. Mungkin nggak ada salahnya kalau Senpai hadir sekali aja akhir pekan ini buat dengerin dulu maksudnya gimana."
            nar "Miyuki menatap amplop di depannya, lalu mengangguk perlahan seolah sedang berusaha meyakinkan dirinya sendiri dengan alasan yang baru saja kamu berikan."
            miyuki "Iya... mungkin kamu benar ya, Chiasa-chan. Datang duduk makan malam dan mendengarkan mereka bicara satu kali kan tidak berarti aku langsung mengiyakan pertunangan."
            chiasa "Betul, Senpai. Paling nggak kalau Senpai datang sekali, Ibu Senpai nggak langsung marah-marah, dan Senpai bisa menilai sendiri orangnya seperti apa."
            miyuki "Aku harus terus mengingat kalimat itu waktu duduk di meja makan nanti. Soalnya kalau di depan Ibu, begitu aku duduk diam dan tersenyum sopan, beliau sering langsung menganggap itu sebagai tanda setuju."
            chiasa "Kalau Senpai merasa kurang nyaman di tengah acara, Senpai tetap bisa pamit dengan alasan jadwal belajar kan?"
            miyuki "Iya, benar juga... setidaknya aku perlu menyiapkan batasnya sebelum berangkat ke sana."
            chiasa "Mau aku temani pilih baju yang nggak terlalu kaku buat hari Sabtu nanti, Senpai?"
            miyuki "Tidak usah repot-repot, Chiasa-chan, Ibu sudah lebih dulu mengirim setelan terusan yang harus kupakai ke apartemenku tadi pagi."
            chiasa "Sampai bajunya juga sudah disiapkan Ibu Senpai ya..."
            miyuki "Begitulah kebiasaan Ibu kalau sudah menyangkut acara keluarga rekan rumah sakit."
            nar "Miyuki mendorong kembali kartu undangan itu masuk ke dalam amplopnya, lalu menyimpannya ke dalam tas kuliahnya. Raut wajahnya memang belum terlihat lebih lega, tetapi kini pertemuan omiai akhir pekan itu sudah dipastikan akan berjalan."
        else:
            yutaka "Kalau dilihat dari caranya pamit barusan, kelihatannya Hayase-san orang yang cukup sopan sih, Tachibana-senpai. Mungkin nggak ada ruginya kalau Senpai datang sekali akhir pekan ini buat dengerin dulu pembicaraannya."
            nar "Miyuki memandangi amplop krem di tangannya sejenak, lalu mengangguk pelan menerima saran yang terdengar paling aman bagi semua pihak itu."
            miyuki "Iya... benar juga kata kamu, Yutaka-kun. Sekadar hadir memenuhi undangan makan malam dan mendengar maksud mereka kan tidak sama dengan langsung menerima lamaran."
            yutaka "Iya, Senpai. Lihat aja dulu gimana sikap orangnya waktu di meja makan nanti."
            miyuki "Aku harus menjaga batas itu baik-baik akhir pekan nanti. Soalnya keluargaku punya kebiasaan langsung membicarakan tahap berikutnya begitu melihat aku tidak membantah di pertemuan pertama."
            yutaka "Yang penting Senpai nggak usah buru-buru mengiyakan jadwal lanjutan sebelum benar-benar yakin."
            miyuki "Iya, akan kuingat itu baik-baik."
            yutaka "Acara makan malamnya diadakan di restoran hotel pusat kota ya, Senpai?"
            miyuki "Iya, di ruang privat restoran langganan Ayah. Ibu bahkan sudah mengirim pakaian resmi yang harus kukenakan ke apartemenku tadi pagi."
            yutaka "Rapi sekali persiapan dari pihak keluarga Senpai."
            miyuki "Saking rapinya sampai aku cuma tinggal datang sesuai jam yang tertulis di kartu ini."
            nar "Ia memasukkan kembali amplop undangan itu ke dalam tasnya dengan gerakan rapi. Meski beban di wajahnya belum berkurang, satu pertemuan resmi dengan keluarga Hayase kini sudah punya cukup alasan untuk terlaksana."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Kalau Senpai memang belum mau mikirin soal perjodohan sekarang, bilang aja tegas-tegas ke orang tua Senpai sama Hayase-san buat kasih ruang dulu. Senpai kan baru tahun ketiga dan lagi padat banget jadwal praktiknya, nggak adil kalau diburu-buru begini."
            nar "Miyuki tersenyum lembut mendengar kamu langsung membelanya dengan bersemangat, lalu sedetik kemudian ia menggeleng pelan."
            miyuki "Aku senang banget kamu langsung mikirin posisiku sampai segitunya, Chiasa-chan. Sungguh."
            chiasa "Habisnya kelihatan banget Senpai nggak nyaman sama undangan itu dari tadi."
            miyuki "Memang nggak nyaman. Tapi masalahnya... di keluargaku, kalau aku tiba-tiba menolak hadir memakai alasan butuh ruang, Ibu justru langsung curiga ada orang di kampus yang memengaruhiku untuk membangkang."
            chiasa "Lho, kok malah mikirnya ke situ, Senpai? Padahal itu kan hak Senpai sendiri buat mengatur jadwal."
            miyuki "Waktu SMA dulu pernah kejadian sekali waktu aku menolak ikut acara kolega Ayah. Alih-alih memberi ruang, minggu depannya Ibu malah memajukan jadwal acaranya dua kali lebih padat sebelum aku sempat punya alasan lain. Jadi setelah obrolan kita di kafe ini selesai, tetap aku sendiri yang harus duduk berhadapan dengan Ibu di meja makan dan mencari cara menjawabnya."
            chiasa "Maaf ya, Senpai, aku jadi malah bikin Senpai kepikiran tambah berat."
            miyuki "Nggak kok, Chiasa-chan. Tahu ada yang mau membelaku saja sudah cukup bikin tenang."
            chiasa "Kalau nanti habis makan malam akhir pekan ini Senpai butuh teman cerita buat melepas penat, telepon aku kapan saja ya."
            miyuki "Pasti, Chiasa-chan. Janji itu sangat berarti buatku."
            nar "Miyuki menyesap kopi hangat yang tersisa di cangkirnya dengan gerakan perlahan sambil menatap halaman taman dalam rumah sakit."
            nar "Miyuki merapikan letak amplop itu di samping cangkir tehnya. Ia menghargai niatmu melindunginya, meskipun ia tahu tekanan di rumahnya tidak bisa dihentikan hanya dengan meminta waktu dari luar."
        else:
            yutaka "Kalau Senpai memang belum siap dan nggak sreg, minta aja mereka kasih ruang dan tunda semuanya dulu. Senpai kan lagi sibuk-sibuknya mengejar kuliah sama praktik rumah sakit, mana bisa dipaksa mengurus omiai sekarang."
            nar "Miyuki tersenyum tipis yang hangat mendengar pembelaanmu, tetapi ia segera menggeleng pelan."
            miyuki "Terima kasih ya sudah langsung membela aku, Yutaka-kun. Rasanya hangat dengar kamu ngomong begitu."
            yutaka "Habisnya dari raut muka Senpai tadi sudah kelihatan jelas kalau Senpai tertekan."
            miyuki "Aku memang tertekan. Cuma... orang tuaku itu sifatnya agak beda kalau menghadapi penolakan langsung. Kalau aku minta mereka mundur atau membatalkan makan malam ini dari luar, Ibu bakal langsung menyelidiki siapa teman di kampus yang bikin aku berani menolak."
            yutaka "Terus mereka malah makin menekan Senpai?"
            miyuki "Iya. Biasanya mereka justru bakal langsung mempercepat jadwal pertemuan berikutnya supaya aku nggak sempat berubah pikiran lagi. Pada akhirnya, setelah kita pisah di lobi ini nanti, tetap aku sendiri yang harus duduk di ruang makan rumah dan menghadapi pertanyaan mereka."
            yutaka "Rumit juga ya tekanan dari keluargamu, Senpai."
            miyuki "Begitulah. Tapi tetap terima kasih karena kamu langsung memihakku barusan."
            yutaka "Kalau akhir pekan nanti selesai acara itu kepala Senpai pusing dan butuh teman ngobrol di luar, kabari saja aku."
            miyuki "Terima kasih banyak, Yutaka-kun. Aku pasti akan menghubungimu kalau butuh tempat bernapas."
            nar "Miyuki memutar cangkir kopinya yang sudah mulai dingin di atas tatakan keramik sambil menghela napas pelan."
            nar "Miyuki menyimpan amplop krem itu ke sela bukunya dengan tenang, menghargai kepedulianmu sembari menyadarkanmu betapa rapatnya kendali keluarga Tachibana atas jadwal hidupnya."
    else:
        if kk_host == "chiasa":
            chiasa "Menurutku sih, Tachibana-senpai, makan malam perkenalan kayak begini baru masuk akal buat didatangi kalau dari awal Senpai beneran dikasih hak buat bilang nggak mau, tanpa harus takut dicap sebagai anak yang nggak tahu terima kasih."
            nar "Jari-jari Miyuki yang sejak tadi merapikan tepi amplop langsung berhenti. Ia menatap amplop krem di tangannya selama beberapa detik, lalu mengembuskan napas panjang yang membuat bahunya turun lega."
            miyuki "...Kamu tahu nggak, Chiasa-chan? Dari tadi sejak amplop ini sampai ke tanganku, aku pengin banget dengar ada satu orang aja yang ngomong persis kayak kalimatmu barusan."
            chiasa "Memangnya orang-orang di sekitar Senpai komentarnya gimana waktu tahu soal Hayase-san?"
            miyuki "Semuanya kompak bilang hal yang sama. 'Tatsuru itu dokter bedah yang sopan, keluarganya terpandang, kamu beruntung sekali orang tuamu mencarikan calon sebaik itu, jangan sampai bikin mereka kecewa.' Nggak ada satu pun yang peduli apakah aku sendiri menginginkan perjodohan ini atau nggak."
            chiasa "Sebaik apa pun orangnya di atas kertas, kalau Senpai nggak mau ya Senpai nggak wajib bilang iya. Menolak perjodohan bukan berarti Senpai jadi anak yang durhaka kok."
            nar "Senyum yang benar-benar tulus dan lepas akhirnya muncul di wajah Miyuki."
            miyuki "Terima kasih banyak ya, Chiasa-chan. Aku memang masih harus memikirkan cara bicara yang tepat ke Ibu nanti, tapi tahu bahwa kamu bisa membedakan antara kepatuhanku sebagai anak dengan keinginanku sendiri itu sudah bikin aku jauh lebih kuat."
            chiasa "Pelan-pelan saja, Senpai. Yang penting Senpai nggak perlu merasa bersalah cuma karena punya pilihan sendiri."
            miyuki "Ayo, sebelum kita pulang, biar Senpai traktir teh hangat sama sepotong kue di kafe ini dulu. Hari ini aku benar-benar butuh istirahat sebentar."
            chiasa "Boleh banget, Senpai! Aku pesan kue tart buah yang di etalase depan itu ya."
            miyuki "Silakan, pilih saja kue mana pun yang kamu suka, Chiasa-chan."
            chiasa "Sekalian kita duduk agak lama sampai jam ramai kereta malam lewat ya, Senpai."
            miyuki "Setuju, di kafe sini suasananya jauh lebih tenang daripada langsung pulang ke apartemen."
            nar "Kamu meletakkan buku catatan anatomi warna milik Miyuki di sisi meja yang bersih agar tidak terkena uap cangkir teh."
            nar "Miyuki menyelipkan amplop krem itu ke bagian belakang tasnya tanpa lagi memedulikannya, lalu melambai memanggil pelayan kafe dengan raut wajah yang jauh lebih cerah."
        else:
            yutaka "Terus terang aja ya, Tachibana-senpai. Pertemuan perjodohan macam ini cuma layak dijalani kalau dari awal Senpai punya kebebasan penuh buat menolak kapan pun, tanpa harus dituduh sebagai anak yang nggak tahu balas budi sama orang tua."
            nar "Tangan Miyuki yang sedang memegang pinggiran amplop langsung terhenti. Ia menatap cetakan nama keluarganya di atas kertas itu sejenak, lalu menghela napas panjang yang sejak tadi ia tahan."
            miyuki "...Dari tadi waktu kurir Ibu mengantar amplop ini, aku berharap banget ada seseorang yang mengucapkan kalimat itu kepadaku, Yutaka-kun."
            yutaka "Memangnya yang lain pada bilang apa ke Senpai?"
            miyuki "Setiap orang yang kenal keluarga kami selalu bilang, 'Hayase Tatsuru itu residen bedah yang mapan, sopan, dan sabar, kurang apa lagi? Jangan sampai mengecewakan orang tuamu.' Seolah-olah karena dia orang baik di atas kertas, maka aku otomatis berkewajiban menyukainya."
            yutaka "Orang baik sekalipun nggak bikin Senpai punya utang buat menyerahkan masa depan Senpai begitu aja. Hidup yang bakal dijalani kan tetap hidup Senpai sendiri."
            nar "Senyum hangat yang tidak lagi kaku akhirnya mengembang di bibir Miyuki."
            miyuki "Terima kasih ya, Yutaka-kun. Aku memang belum memutuskan kalimat apa yang akan kupakai untuk menjawab Ibu nanti, tapi tahu ada kamu yang tidak menyamakan sikap patuhku dengan kemauanku sendiri itu rasanya melegakan sekali."
            yutaka "Nggak usah buru-buru cari jawabannya hari ini, Senpai. Tarik napas dulu saja."
            miyuki "Iya. Ayo pesan kopi atau teh hangat sama kue dulu, kali ini biar Senpai yang traktir."
            yutaka "Kalau ditraktir kue kafe rumah sakit sih aku jelas nggak bakal nolak, Senpai."
            miyuki "Hehe, kue bolu cokelat di konter depan itu enak sekali lho, sebentar kupesankan untuk kita berdua."
            yutaka "Sekalian pesan teh hangat tawar buat Senpai supaya tenggorokan Senpai lebih rileks sebelum pulang."
            miyuki "Ide bagus, Yutaka-kun. Rasanya sore ini jauh lebih ringan berkat kamu mampir mengantar buku."
            nar "Pelayan kafe segera datang menghampiri meja kalian di dekat dinding kaca taman untuk mencatat pesanan kudapan sore tersebut."
            nar "Miyuki memasukkan amplop undangan itu ke dalam tasnya tanpa beban yang sama seperti tadi, lalu mengangkat tangan memanggil pelayan kafe dengan senyum yang jauh lebih ringan."
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
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Koridor lantai atas menuju aula serbaguna Rumah Sakit Tachibana malam itu dihiasi karangan daun pinus dan pita merah keemasan. Dari balik pintu ganda kayu mahoni yang masih tertutup rapat, terdengar alunan kuartet gesek, denting gelas kaca, serta suara perbincangan para dokter kepala dan tamu kehormatan yang berulang kali menyebut nama keluarga Tachibana dengan penuh pujian."
        else:
            nar "Koridor lantai atas menuju aula serbaguna Rumah Sakit Tachibana hari itu dihiasi karangan daun pinus dan pita merah keemasan. Dari balik pintu ganda kayu mahoni yang masih tertutup rapat, terdengar alunan kuartet gesek, denting gelas kaca, serta suara perbincangan para dokter kepala dan tamu kehormatan yang berulang kali menyebut nama keluarga Tachibana dengan penuh pujian."
        nar "Beberapa langkah dari pintu masuk aula, Miyuki berdiri seorang diri di dekat pilar marmer. Ia mengenakan gaun pesta biru tua selutut yang rapi dengan rambut hitam panjangnya yang disisir lurus berkilau. Jari-jari tangan kanannya yang dingin terus-menerus memutar pengait gelang perak di pergelangan tangan kirinya, padahal ukuran gelang itu sama sekali tidak longgar."
        chiasa "Tachibana-senpai belum masuk ke dalam? Musik pembukanya sudah mulai dari tadi kan?"
        nar "Miyuki menghentikan gerakan jarinya di atas gelang, lalu menoleh ke arahmu sambil mengembuskan napas perlahan."
        miyuki "Sudah mulai sepuluh menit lalu, Chiasa-chan. Tadi Ibu juga sudah kirim pesan menyuruhku cepat masuk ke meja utama."
        chiasa "Kenapa berdiri di luar sini terus, Senpai? Di koridor dekat tangga darurat begini udaranya dingin lho, tangan Senpai aja kelihatan pucat."
        miyuki "Soalnya aku sudah hafal mati skenario yang bakal terjadi begitu aku mendorong pintu itu nanti. Tiga menit pertama koleganya Ayah bakal tanya soal nilai ujianku di Fakultas Kedokteran, lima menit berikutnya tanya kapan aku mulai masuk rotasi klinik, lalu ujung-ujungnya Ibu bakal langsung menyuruhku duduk di sebelah Hayase Tatsuru."
        chiasa "Hayase-san datang sama keluarganya juga di jamuan Natal ini, Senpai?"
        miyuki "Iya, meja keluarga Hayase digabung langsung sama meja orang tuaku di barisan paling depan. Kadang aku sampai mikir lebih baik mereka langsung saja bicara soal Tatsuru begitu aku masuk pintu, supaya aku nggak usah pegal tersenyum setengah jam buat basa-basi pembukanya."
        chiasa "Kalau Senpai memang capek banget, nggak usah dipaksa langsung ke meja depan sekarang juga kan?"
        nar "Ia menatapmu di bawah lampu dinding koridor, lalu menarik senyum tipis yang tampak sedikit dipaksakan."
        miyuki "Mana bisa menghilang di acara rumah sakit keluarga sendiri. Tapi kamu mau datang buat menemaniku sebagai teman saja sudah bikin aku tenang kok, Chiasa-chan. Aku cuma pengin ada satu orang di gedung ini yang tahu kalau aku sebenarnya gugup, sebelum semua orang di dalam sana melihatku tersenyum rapi seperti biasa."
    else:
        if kk_slot >= 3:
            nar "Koridor lantai atas menuju aula serbaguna Rumah Sakit Tachibana malam itu dihiasi untaian daun pinus dan pita merah keemasan. Dari balik pintu ganda kayu mahoni yang masih tertutup rapat, terdengar alunan musik gesek, denting gelas kaca, serta suara obrolan para dokter senior dan tamu undangan yang beberapa kali menyebut nama Miyuki dengan nada memuji."
        else:
            nar "Koridor lantai atas menuju aula serbaguna Rumah Sakit Tachibana hari itu dihiasi untaian daun pinus dan pita merah keemasan. Dari balik pintu ganda kayu mahoni yang masih tertutup rapat, terdengar alunan musik gesek, denting gelas kaca, serta suara obrolan para dokter senior dan tamu undangan yang beberapa kali menyebut nama Miyuki dengan nada memuji."
        nar "Beberapa langkah di samping pintu aula, Miyuki berdiri seorang diri di dekat pilar marmer. Ia mengenakan gaun pesta biru tua selutut dengan rambut hitam panjang yang tersisir lurus rapi. Jemari tangan kanannya yang dingin terus saja memutar pengait gelang perak di pergelangan kirinya, padahal gelang itu terpasang rapat dan sama sekali tidak longgar."
        yutaka "Tachibana-senpai belum masuk ke aula? Kedengarannya acara di dalam sudah jalan dari tadi."
        nar "Miyuki menghentikan jarinya dari gelang perak itu lalu menoleh ke arahmu sambil mengembuskan napas pelan."
        miyuki "Sudah mulai sepuluh menit yang lalu, Yutaka-kun. Tadi Ibu juga sudah kirim pesan menyuruhku langsung bergabung ke meja depan."
        yutaka "Kenapa masih berdiri di luar koridor begini, Senpai? Di dekat sini angin dari tangga daruratnya lumayan dingin lho."
        miyuki "Soalnya aku sudah hafal persis skenario yang menungguku begitu pintu itu dibuka. Tiga menit pertama kolega Ayah bakal menanyakan nilai kuliah Kedokteran, lima menit berikutnya soal rencana rotasi klinik, lalu ujung-ujungnya Ibu bakal langsung mengarahkanku duduk di sebelah Hayase Tatsuru."
        yutaka "Hayase-san datang sama orang tuanya juga hari ini?"
        miyuki "Iya, meja keluarga Hayase dijadikan satu sama meja Ayah dan Ibu di barisan paling depan. Kadang aku sampai berharap mereka langsung saja membicarakan soal Tatsuru begitu aku masuk, biar aku nggak perlu capek tersenyum setengah jam buat basa-basi pembukanya."
        yutaka "Nggak harus langsung duduk di sana juga kan kalau kamu memang belum mau?"
        nar "Ia mengangkat wajah menatapmu di bawah lampu dinding koridor, lalu menarik senyum tipis yang agak lelah."
        miyuki "Sulit menghilang begitu saja di acara rumah sakit milik orang tua sendiri. Tapi kamu mau datang sebagai teman saja sudah sangat membantu kok, Yutaka-kun. Aku cuma ingin ada satu orang di gedung ini yang tahu kalau aku sebenarnya gugup, sebelum semua orang di dalam sana melihatku tersenyum rapi seperti biasa."
    call kk_family_menu("Mi09", ["\"Ayo masuk bareng. Aku temani di dalam supaya Senpai nggak sendirian.\"", "\"Kalau mereka terus mendesak soal Hayase-san, kenalkan saja aku sebagai pasangan Senpai.\"", "\"Aku antar sampai depan aula sini saja ya. Semoga acaranya lancar.\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Ayo kita masuk bareng sekarang, Tachibana-senpai. Aku temani Senpai di dalam supaya Senpai nggak harus menghadapi meja mereka sendirian."
            miyuki "Kamu yakin nggak bakal canggung di dalam? Tamunya kebanyakan dokter senior sama pengurus rumah sakit."
            chiasa "Nggak apa-apa, kan aku cuma perlu berdiri di sebelah Senpai sambil pegang gelas jus. Ayo."
            nar "Miyuki menatapmu sejenak, lalu mengangguk pelan. Ia merapikan sisi gaunnya, mendorong pintu kayu aula, dan melangkah masuk bersamamu ke bawah terangnya lampu gantung kristal."
            nar "Baru saja kalian mengambil dua gelas jus apel dingin dari meja jamuan tepi ruangan, ibu Miyuki, Tachibana Sayuri, melangkah anggun menghampiri kalian. Senyum seorang direktur rumah sakit terpasang rapi di wajahnya, tetapi matanya langsung memberi isyarat ke arah meja bundar di bagian depan tempat ayah Miyuki dan keluarga Hayase sedang berbincang."
            "Ibu Miyuki" "Akhirnya kamu masuk juga, Miyuki. Dari tadi Ibu cari di dekat pintu. Tatsuru-kun baru saja menanyakanmu, dan orang tuanya ingin membahas jadwal makan malam keluarga minggu depan. Ayo ke meja depan sekarang, kursi di sebelah Tatsuru-kun sudah Ibu kosongkan."
            nar "Biasanya Miyuki akan langsung mengangguk patuh dan mengikuti langkah ibunya. Kali ini, ia melirik ke arahmu yang berdiri tepat setengah langkah di sampingnya. Mengingat percakapan jujur kalian di luar koridor tadi, Miyuki tetap berdiri tenang di tempatnya."
            miyuki "Maaf, Bu. Soal jadwal makan malam dengan keluarga Hayase minggu depan itu, aku belum mengiyakan apa-apa karena jadwal kuliahku belum kupastikan. Lagipula hari ini aku mengundang temanku dari kampus, jadi aku ingin mengenalkan Chiasa-chan ke Ibu dulu."
            chiasa "Permisi, Tachibana-san. Salam kenal, saya Amamiya Chiasa, adik tingkat Tachibana-senpai di universitas. Selamat Natal untuk keluarga Tachibana."
            nar "Suara Miyuki terdengar sangat sopan dan lembut, tidak ada satu kata pun yang terdengar membangkang di depan tamu lain. Meski begitu, senyum di bibir ibunya sempat menegang selama dua detik penuh karena tidak terbiasa melihat putrinya menunda perintah secara langsung."
            "Ibu Miyuki" "...Begitu ya. Terima kasih sudah berkenan datang ke jamuan rumah sakit kami, Amamiya-san. Kalau begitu temani tamumu mengambil hidangan dulu lima belas menit, Miyuki. Setelah itu baru mampir menyapa keluarga Hayase."
            miyuki "Baik, Bu. Terima kasih."
            nar "Begitu ibunya berbalik kembali menuju meja utama, Miyuki mengembuskan napas panjang yang sejak tadi ia tahan, lalu berbisik pelan kepadamu sambil mengambil piring kue kecil."
            miyuki "Jantungku rasanya mau copot barusan, Chiasa-chan. Tadi kupikir Ibu bakal langsung menarik tanganku di depan semua tamu."
            chiasa "Tadi Senpai keren banget lho, suaranya tetap lembut tapi tegas banget. Nih, ambil kue tar buahnya dulu biar nggak tegang."
            miyuki "Terima kasih. Ternyata bilang belum memutuskan di depan Ibu nggak seseram yang kubayangkan waktu ada kamu di sebelahku."
            chiasa "Kalau nanti habis lima belas menit Ibu Senpai manggil lagi ke meja depan, aku ikut berdiri di dekat Senpai supaya pembicaraannya tetap singkat."
            miyuki "Iya, tolong tetap di dekatku sampai jamuan ini selesai ya, Chiasa-chan."
            nar "Miyuki menyuap potongan kecil kue tar buahnya dengan bahu yang kini jauh lebih tenang di bawah gemerlap lampu aula."
        else:
            yutaka "Ayo masuk bareng sekarang, Tachibana-senpai. Aku temani di dalam supaya Senpai nggak perlu menghadapi meja depan itu sendirian."
            miyuki "Kamu yakin nggak bakal bosan di dalam? Tamu-tamunya kebanyakan dokter senior dan kolega rumah sakit."
            yutaka "Nggak masalah, aku sudah biasa lihat ruang pesta yang isinya jas semua. Setidaknya sekarang ada kamu yang bisa diajak ngobrol. Ayo."
            nar "Miyuki menatapmu sebentar, lalu mengangguk mantap. Ia merapikan lipatan gaunnya, mendorong daun pintu mahoni, dan berjalan masuk bersamamu ke dalam aula yang terang oleh deretan lampu gantung kristal."
            nar "Baru saja kalian mengambil dua gelas minuman dingin dari meja hidangan tepi ruangan, Tachibana Sayuri berjalan menghampiri dengan senyum anggun seorang direktur rumah sakit. Tatapannya sekilas menilai kehadiranmu, lalu segera mengarah ke meja bundar utama tempat ayah Miyuki dan keluarga Hayase duduk."
            "Ibu Miyuki" "Akhirnya kamu masuk juga, Miyuki. Tatsuru-kun baru saja menanyakanmu, dan orang tuanya ingin memastikan jadwal makan malam keluarga minggu depan. Ayo langsung ke meja depan, kursi di sebelah Tatsuru-kun sudah Ibu siapkan."
            nar "Dalam keadaan biasa, Miyuki nyaris selalu langsung mengangguk dan mengikuti arah ibunya. Kali ini ia melirik sekilas kepadamu di sisinya, teringat percakapan jujur di luar pintu tadi, lalu menjawab dengan suara tetap lembut tanpa bergeser selangkah pun."
            miyuki "Maaf, Bu. Soal rencana makan malam dengan keluarga Hayase minggu depan, aku belum memutuskan apa-apa karena masih perlu memeriksa jadwal kuliahku dulu. Lagipula hari ini aku datang bersama temanku dari kampus, jadi aku ingin mengenalkan Yutaka-kun kepada Ibu lebih dulu."
            yutaka "Permisi, Tachibana-san. Salam kenal, saya Kisaragi Yutaka, adik tingkat Tachibana-senpai di universitas. Selamat Natal."
            nar "Tidak ada sedikit pun nada membantah dalam ucapan Miyuki. Meski begitu, senyum sopan Sayuri sempat menegang selama dua detik mendengar penolakan halus putrinya sekaligus menangkap nama marga Kisaragi yang baru kamu sebutkan."
            "Ibu Miyuki" "...Oh, Kisaragi-san. Terima kasih sudah berkenan hadir di acara rumah sakit kami. Kalau begitu temani tamumu mencicipi hidangan dulu lima belas menit ya, Miyuki. Setelah itu baru mampir menyapa keluarga Hayase di depan."
            miyuki "Baik, Bu. Terima kasih."
            nar "Begitu Sayuri berbalik menuju meja utama, Miyuki mengembuskan napas panjang yang sejak tadi tertahan, lalu tersenyum kecil sambil mengambil piring kue di sampingmu."
            miyuki "Tanganku masih agak gemetar barusan, Yutaka-kun. Kukira Ibu langsung menolak mentah-mentah di depan tamu lain."
            yutaka "Tadi kamu menyampaikannya rapi banget kok, Senpai, sampai Ibumu sendiri nggak punya celah buat memaksa. Ambil kue dulu aja mumpung masih sempat."
            miyuki "Iya. Ternyata bilang belum memutuskan di depan Ibu nggak seseram bayanganku selama ada kamu berdiri di sebelahku."
            yutaka "Nanti waktu kamu harus menyapa meja depan sebentar, aku ikut mendampingi di sampingmu supaya mereka nggak langsung mengunci jadwal baru."
            miyuki "Terima kasih banyak, Yutaka-kun. Rasanya malam ini aku benar-benar bisa bernapas lega."
            nar "Miyuki menyesap minuman dinginnya perlahan sambil tersenyum tulus di sela alunan musik gesek aula rumah sakit."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Tachibana-senpai, kalau Senpai memang keberatan terus-terusan didorong ke Hayase-san, gimana kalau hari ini Senpai kenalkan aja aku ke orang tua Senpai sebagai pasangan Senpai?"
            nar "Miyuki langsung tertegun. Jari-jarinya berhenti menyentuh gelang peraknya, dan sorot matanya menatapmu lekat-lekat untuk mencari tahu apakah kamu sedang bergurau."
            miyuki "Chiasa-chan... kamu sadar kan apa artinya kalau aku ngomong begitu di dalam aula sana? Orang tuaku itu bukan tipe yang bakal lupa besok pagi. Kalau hari ini kita berpura-pura punya hubungan khusus, bulan depan dan tahun depan kita harus terus kompak menjaga cerita bohong yang sama di depan mereka."
            chiasa "Aku paham kok risikonya, Senpai. Tapi kalau sekadar bicara sopan sebagai teman biasa, Ibu Senpai pasti tetap bakal nyuruh Senpai duduk sama Hayase-san lima menit kemudian. Pakai aja namaku hari ini."
            nar "Miyuki menatap daun pintu mahoni di samping kalian, lalu kembali menatap wajahmu yang tenang. Keraguan di wajahnya perlahan berganti menjadi tekad seseorang yang akhirnya diberikan pintu keluar. Ia mengulurkan tangannya dan menggenggam lenganmu."
            miyuki "...Kalau begitu, waktu kita berdiri di depan meja Ayah dan Ibu nanti, tolong jangan lepaskan lenganmu dari tanganku duluan ya, Chiasa-chan."
            chiasa "Iya, nggak bakal kulepas. Ayo masuk, Senpai."
            nar "Kalian mendorong pintu aula dan berjalan lurus menghampiri meja bundar utama sebelum ibunya sempat memanggil dari jauh. Begitu Tachibana Sayuri, suaminya Kazuhiro, serta Hayase Tatsuru menoleh menyambut kedatangan Miyuki, jemari Miyuki mencengkeram lenganmu sedikit lebih erat."
            "Ibu Miyuki" "Nah, Miyuki, kebetulan kamu langsung ke meja utama. Tatsuru-kun baru saja..."
            miyuki "Ayah, Ibu, dan Hayase-san juga... maaf aku harus memotong sebelum pembicaraannya berjalan lebih jauh. Aku tidak bisa melanjutkan rencana pertemuan omiai keluarga kita, karena saat ini aku sudah menjalin hubungan serius dengan Chiasa."
            nar "Suara percakapan di meja bundar utama itu langsung terputus total. Ayah Miyuki menurunkan garpunya dengan bunyi denting pendek, ibunya terdiam kaku dengan bibir sedikit terbuka, sementara Hayase Tatsuru yang baru hendak berdiri menarik kursi untuk Miyuki membeku di tempatnya."
            "Ayah Miyuki" "Miyuki... tunggu sebentar, apa maksudmu?"
            "Ibu Miyuki" "Miyuki, di sini banyak tamu rumah sakit, kita bicarakan hal tidak masuk akal seperti ini di rumah nanti..."
            "Tatsuru" "...Dengan Amamiya-san? Begitu ya... saya sama sekali belum mendengar soal itu."
            chiasa "Maaf kami baru sempat menyampaikannya langsung hari ini ke Oji-san, Oba-san, dan Hayase-san."
            miyuki "Kami permisi dulu mengambil minuman di meja samping. Terima kasih atas pengertiannya, Hayase-san."
            nar "Di tengah tatapan terkejut kedua orang tuanya yang tidak bisa membuat keributan di hadapan tamu rumah sakit, Miyuki mengajakmu bergeser ke meja jamuan samping. Begitu agak jauh dari meja utama, bahunya akhirnya sedikit turun meski jarinya masih menggenggam ujung lenganmu."
            miyuki "...Aku beneran mengatakannya di depan mereka semua barusan. Chiasa-chan, terima kasih sudah nggak melepaskan tanganku."
            chiasa "Sama-sama, Senpai. Mulai sekarang kita jaga ceritanya bareng-bareng. Tapi tangan Senpai masih dingin banget nih, duduk dulu sebentar ya."
            miyuki "Iya... nanti malam pasti Ibu langsung menelepon panjang lebar ke apartemenku. Tapi anehnya, untuk pertama kalinya aku nggak merasa panik membayangkan telepon itu."
            chiasa "Kalau nanti Ibu Senpai nanya macam-macam, bilang aja langsung ke aku biar jawaban kita nggak pernah tabrakan."
            miyuki "Kita harus menyepakati tanggal kapan kita mulai dekat supaya cerita kita rapi kalau Ibu bertanya detailnya."
            chiasa "Kita pakai tanggal waktu jalan-jalan di vila musim panas kemarin saja, Senpai, paling masuk akal."
            nar "Miyuki mengangguk setuju sambil merapatkan genggamannya di lenganmu dengan senyum tipis yang tampak jauh lebih berani."
            nar "Untuk hari ini, seluruh susunan rencana tentang kursi di sebelah Tatsuru akhirnya benar-benar kehilangan arah."
        else:
            yutaka "Tachibana-senpai, kalau kamu memang sudah capek terus-terusan diarahkan ke Hayase-san, gimana kalau hari ini kamu kenalkan saja aku ke orang tuamu sebagai pasanganmu?"
            nar "Miyuki langsung terdiam. Tangannya turun dari pergelangan gelang perak itu, sementara kedua matanya menatapmu tajam untuk mengecek apakah kamu sedang melontarkan gurauan."
            miyuki "Yutaka-kun... kamu paham kan konsekuensinya kalau aku mengatakan itu di dalam aula? Ayah dan Ibuku bukan tipe orang tua yang bakal melupakan satu nama begitu saja. Kalau nanti mereka bertanya lagi bulan depan atau tahun depan, kita berdua harus terus mengingat kebohongan yang sama."
            yutaka "Aku paham kok risikonya, Senpai. Tapi kalau kita masuk cuma sebagai teman kuliah biasa, lima menit lagi Ibumu pasti tetap menarikmu duduk di sebelah Hayase-san. Pakai aja namaku hari ini."
            nar "Miyuki menatap daun pintu kayu mahoni yang tertutup, lalu kembali menatap wajahmu yang tidak bergeming. Setelah satu tarikan napas pendek, ia melangkah mendekat dan melingkarkan jemarinya ke lengan mantelmu."
            miyuki "...Kalau begitu, waktu kita berhadapan dengan Ayah, Ibu, dan Tatsuru di meja depan nanti, tolong jangan melepaskan peganganku duluan ya, Yutaka-kun."
            yutaka "Aman, nggak bakal kulepas. Ayo masuk, Senpai."
            nar "Kalian mendorong pintu aula dan berjalan langsung menuju meja bundar utama sebelum Sayuri sempat memanggil dari jauh. Begitu Tachibana Sayuri, Kazuhiro, dan Hayase Tatsuru menoleh menyambut, jemari Miyuki mencengkeram kain lenganmu jauh lebih erat daripada sebelumnya."
            "Ibu Miyuki" "Nah, Miyuki, pas sekali kamu langsung ke meja utama. Tatsuru-kun baru saja menanyakan jadwal..."
            miyuki "Ayah, Ibu, dan juga Hayase-san... maaf aku memotong pembicaraannya di sini. Aku tidak bisa melanjutkan rencana omiai keluarga kita, karena saat ini aku sudah berpacaran serius dengan Kisaragi Yutaka."
            nar "Obrolan di meja utama seketika terhenti. Kazuhiro meletakkan garpunya dengan bunyi denting pendek, sementara Sayuri menatapmu dari atas ke bawah dengan kening berkerut kaget karena tidak menyangka nama Kisaragi muncul di situ. Hayase Tatsuru, yang baru berdiri separuh untuk menarik kursi di sebelahnya, membeku di tempat."
            "Ayah Miyuki" "Miyuki, tunggu dulu... Kisaragi dari grup Kisaragi? Sejak kapan kalian..."
            "Ibu Miyuki" "Miyuki, di sini banyak kolega kita. Kita bicarakan ini secara tertutup nanti."
            "Tatsuru" "...Dengan Kisaragi-san? Begitu ya. Maaf, saya memang belum pernah mendengar kabar ini sebelumnya."
            yutaka "Maaf kami baru sempat menyampaikannya langsung hari ini kepada Oji-san, Oba-san, dan Hayase-san."
            miyuki "Kalau begitu kami permisi ke meja hidangan samping dulu. Terima kasih pengertiannya, Hayase-san."
            nar "Di bawah tatapan kaget kedua orang tuanya yang tidak mungkin membuat keributan di tengah tamu rumah sakit, Miyuki menuntun langkahmu menjauh menuju meja jamuan samping. Tangannya di lenganmu masih sedikit dingin dan gemetar."
            miyuki "...Ayah bahkan sampai menjatuhkan garpunya barusan. Terima kasih sudah tetap tenang berdiri di sebelahku, Yutaka-kun."
            yutaka "Sudah kubilang aman kan, Senpai. Tarik napas dulu, aku ambilin air dingin. Tanganmu masih gemetar tuh."
            miyuki "Iya... nanti pulang dari sini pasti Ayah dan Ibu langsung menghubungiku minta penjelasan. Tapi anehnya, untuk pertama kalinya aku nggak merasa sesak membayangkan panggilan mereka."
            yutaka "Kalau mereka mulai nanya detail yang aneh-aneh, kabari aja duluan biar cerita kita selalu sinkron."
            miyuki "Kita samakan saja ceritanya bahwa kita mulai dekat sejak acara liburan musim panas di vila kemarin ya, Yutaka-kun."
            yutaka "Sepakat, tanggal dan tempatnya masuk akal jadi orang tuamu nggak bakal bisa membantah."
            nar "Miyuki mengembuskan napas lega sambil masih memegangi lengan mantelmu di samping meja jamuan."
            nar "Untuk hari ini, seluruh susunan rencana tentang Tatsuru di meja utama akhirnya kehilangan arah."
    else:
        if kk_host == "chiasa":
            chiasa "Maaf ya, Tachibana-senpai. Aku cuma bisa ngantar Senpai sampai depan koridor aula sini aja hari ini, soalnya aku masih harus balik karena ada urusan lain. Semoga acara jamuannya di dalam lancar ya."
            nar "Jemari Miyuki yang tadinya sempat terangkat sedikit di samping gaunnya seperti hendak memegang ujung lengan mantelmu perlahan diturunkan kembali. Dalam waktu singkat, ekspresi cemas yang tadi ia perlihatkan di depanmu langsung lenyap, berganti dengan postur tegak dan senyum senior yang rapi."
            miyuki "Oh... begitu ya, kamu masih ada urusan lain hari ini. Tidak apa-apa kok, Chiasa-chan. Kamu sudah mau mampir mengantar aku sampai depan aula ini saja Senpai sudah senang."
            chiasa "Kalau nanti acaranya sudah selesai, hati-hati pulang ke apartemennya ya, Senpai. Jangan lupa istirahat. Selamat Natal."
            miyuki "Iya, terima kasih banyak. Selamat Natal juga, Chiasa-chan. Hati-hati di jalan, di luar anginnya dingin."
            nar "Alunan musik gesek dari balik pintu ganda mahoni kembali terdengar meninggi diiringi tawa samar para tamu undangan di dalam aula."
            nar "Miyuki merapikan letak gelang perak di pergelangan tangan kirinya sekali lagi, menyiapkan senyum putri keluarga Tachibana yang tidak boleh tampak goyah."
            nar "Miyuki tetap berdiri tenang di samping pintu mahoni itu tanpa menyentuh gagangnya, menunggu dengan sopan sampai kamu berbalik dan berjalan menuju lorong lift di ujung koridor."
            nar "Tepat sebelum pintu lift tertutup, kamu melihat Miyuki akhirnya menarik napas pendek dan mendorong pintu aula seorang diri. Dari celah pintu yang terbuka, langsung terdengar suara ramah ibunya yang memanggil Miyuki untuk segera duduk di kursi kosong sebelah Hayase Tatsuru."
        else:
            yutaka "Maaf ya, Tachibana-senpai. Aku cuma bisa ngantar sampai depan aula sini aja, habis ini aku masih harus balik karena ada urusan lain. Semoga acaranya lancar di dalam."
            nar "Tangan Miyuki yang tadinya sempat sedikit terangkat di samping gaunnya seolah hendak meraih lenganmu langsung turun kembali. Seketika raut gugup yang ia perlihatkan di koridor tadi merapat tertutup oleh postur tegak dan senyum senior yang sopan."
            miyuki "Oh... begitu ya, kamu masih ada urusan lain. Tidak apa-apa kok, Yutaka-kun. Terima kasih sudah mengantar sampai sini, aku bisa masuk sendiri."
            yutaka "Nanti kalau acaranya sudah selesai, hati-hati pulang ke apartemennya ya, Senpai. Selamat Natal."
            miyuki "Iya, terima kasih banyak. Selamat Natal juga, Yutaka-kun. Hati-hati di jalan pulang."
            nar "Suara denting gelas dan perbincangan kolega rumah sakit dari balik pintu mahoni terdengar semakin ramai memenuhi koridor lantai atas."
            nar "Miyuki menegakkan bahunya perlahan, mengembalikan topeng ketenangan yang selama ini selalu diharapkan kedua orang tuanya."
            nar "Miyuki tetap berdiri di depan pintu kayu mahoni tanpa membuka gagangnya, menunggu sampai kamu berbalik dan melangkah menjauh ke arah lift di ujung koridor."
            nar "Tepat sebelum pintu lift menutup, kamu melihat Miyuki menarik napas pendek lalu mendorong pintu aula sendirian. Dari celah pintu yang terbuka, langsung terdengar sambutan ramah ibunya yang memanggil Miyuki untuk duduk di kursi kosong sebelah Hayase Tatsuru."
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
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Lampu gantung kristal di ruang jamuan pribadi lantai atas Rumah Sakit Tachibana memancarkan cahaya kuning keemasan yang sangat teratur di atas taplak meja putih bersih. Di balik jendela tinggi, deretan lampu jalan musim dingin bulan Desember tampak sunyi di bawah langit gelap."
        else:
            nar "Cahaya musim dingin bulan Desember masuk dingin melewati tirai tipis ruang jamuan pribadi lantai atas Rumah Sakit Tachibana. Di atas meja panjang berlapis taplak putih, perangkat teh porselen dan karangan bunga cemara kecil sudah tertata sepresisi ruang konferensi."
        nar "Keluarga Hayase telah tiba lebih awal membawa kotak bingkisan musim dingin berbalut kain furoshiki biru tua serta sebuah map tipis berisi daftar pilihan tanggal untuk acara keluarga berikutnya. Pertemuan resmi bahkan belum dimulai, tetapi di atas meja sudah terlalu banyak benda yang membuat satu kata penolakan terasa seolah merusak kerja keras begitu banyak orang."
        nar "Di sisi kiri meja duduk Tachibana Kazuhiro dan Tachibana Sayuri dengan setelan rapi. Di seberang mereka duduk Hayase Tatsuru, dokter residen bedah berusia dua puluh enam tahun dengan jas gelap yang bersih dan sikap tenang terdidik, mendampingi kedua orang tuanya."
        nar "Aroma samar antiseptik dari koridor rumah sakit di luar pintu seakan tersapu habis oleh wangi daun pinus segar dan teh hijau kelas atas yang baru dituang ke cangkir keramik putih."
        "Ibu Miyuki" "Wah, akhirnya kamu datang juga, Miyuki. Keluarga Hayase sudah membawa manisan kastanye khusus dari Kyoto lho. Tadi Ibu juga baru dengar Tatsuru-kun baru menyelesaikan jadwal operasi panjang minggu lalu dengan hasil sangat dipuji kepala bagian. Mari duduk di sebelah Tatsuru-kun, kursi utamanya sudah Ibu kosongkan dari tadi."
        nar "Tachibana Sayuri melonggarkan sedikit ikatan kain furoshiki biru tua di tengah meja sambil memuji kualitas kotaknya dengan senyum penuh kebanggaan, sementara Kazuhiro melirik sekilas arloji emas di pergelangan tangannya sebelum menanyakan kabar persiapan sayap baru rumah sakit kepada Tatsuru."
        "Ayah Miyuki" "Kebetulan juga Amamiya-san ikut mendampingi hari ini. Silakan duduk dulu, pertemuan keluarga kita hanya akan memakan waktu singkat sebelum jadwal rapat medis lanjutan dimulai, cukup untuk menyelaraskan tanggal awal tahun dan perluasan divisi bedah musim semi nanti."
        "Ayah Miyuki" "Nilai evaluasi seminar klinis musim dinginmu kemarin sudah sampai ke meja dekan kan, Miyuki? Ayah dengar hasilmu masih di peringkat teratas angkatan."
        miyuki "Ya, Ayah. Semuanya sudah diserahkan minggu lalu sebelum libur."
        "Ibu Miyuki" "Bagus sekali, kalau hasil studimu stabil seperti itu berarti sudah tidak ada alasan lagi menunda rencana pembicaraan kedua keluarga."
        "Tatsuru" "Terima kasih banyak atas perhatiannya, Oji-san, Oba-san. Selamat Natal, Miyuki, Amamiya-san. Terima kasih sudah menyempatkan hadir di tengah jadwal kuliah yang masih padat menjelang akhir tahun."
        chiasa "Selamat Natal, Oji-san, Oba-san, Hayase-san. Terima kasih sudah mengizinkan saya ikut masuk sebentar."
        nar "Kamu menatap deretan map putih dan piring manisan yang sudah tersusun sempurna di hadapan keluarga Hayase. Di ruangan yang serba rapi ini, bahkan sebelum satu kalimat utama dibicarakan, setiap kursi sudah diberi peran yang diharapkan oleh orang tua Miyuki."
        nar "Miyuki mengenakan gaun wol musim dingin berwarna merah anggur dengan rambut hitam panjang lurus terurai rapi melewati bahunya. Mata cokelat kemerahannya menatap deretan bingkisan dan map jadwal di atas meja tanpa sedikit pun bergerak menuju kursi yang ditunjuk ibunya."
        nar "Kamu sempat melirik sekilas pergelangan tangannya. Tidak seperti Natal tahun lalu di koridor aula saat jemarinya terus memutar pengait gelang perak karena gugup, hari ini tangan kiri Miyuki tampak jauh lebih mantap."
        nar "Ia justru menarik sendiri satu kursi di sisi tengah meja dengan bunyi gesekan pelan yang langsung memutus basa-basi ringan di ruangan itu, lalu melirik singkat ke arahmu sambil berbisik cukup pelan agar hanya kamu yang mendengar."
        miyuki "Mereka bilang pertemuan Natal ini diadakan karena ingin mendengar jawabanku, Chiasa-chan. Lalu mereka sudah menyiapkan kalender dan menanyakan bulan mana yang kosong bahkan sebelum aku sempat menjawab satu kata pun."
        chiasa "Tarik napas dulu, Tachibana-senpai. Aku di sebelahmu, nggak usah terburu-buru mengiyakan apa pun. Tahun ini Senpai sudah nggak gemetar lagi seperti dulu."
        miyuki "Iya. Aku juga capek kalau setiap bulan Desember harus mengulang skenario yang sama."
        "Ibu Miyuki" "Miyuki, tegakkan bahumu dan jangan berbisik sendiri di depan tamu. Keluarga Hayase sedang menunggu tanggapanmu."
        miyuki "Maaf, Ibu. Aku mendengarkan."
        nar "Kamu melihat rahang Miyuki sedikit mengatup menahan kesal atas teguran halus yang meluncur otomatis dari bibir ibunya, persis seperti rutinitas panjang yang sudah terlalu sering ia jalani sejak kecil."
        "Ibu Miyuki" "Nah, Miyuki, orang tua Tatsuru-kun baru saja menyebut bahwa pertengahan musim semi nanti aula hotel sudah mulai penuh. Kalau bulan Februari atau Maret jadwal ujianmu masih longgar, kita bisa langsung mengunci tanggal pertemuan resmi kedua keluarga..."
        "Tatsuru" "Tentu saja kami tetap menyesuaikan dengan kesiapan jadwal praktikum Miyuki, Oba-san. Saya tidak ingin Miyuki merasa terbebani."
        nar "Ucapan Tatsuru terdengar tulus dan sopan sama sekali jauh dari nada memaksa seorang pengganggu. Justru kesopanan rapi semua orang di ruangan ini yang membuat tekanan di sekitar kursi Miyuki terasa semakin rapat dan sulit dibantah."
        if kk_has("pasangan_palsu"):
            nar "Tatapan Tachibana Sayuri sempat melirik cepat ke arahmu dengan senyum tipis yang agak kaku, sementara Tatsuru menyentuh pelan tepi map jadwal di depannya."
            miyuki "Mereka semua masih ingat jelas kita datang bersama dan mengaku sebagai pasangan di aula Natal tahun lalu, Chiasa-chan... dan mereka mengira hari ini kita bakal lengah atau akhirnya menyerah."
            call kk_family_menu("Mi18", ["Duduk di samping Miyuki dan teruskan peran pasangan seperti tahun lalu.", "Minta Hayase Tatsuru menunda seluruh pembicaraan jadwal ini.", "Ceritakan jujur mengapa kalian berpura-pura bersama tahun lalu."])
        else:
            call kk_family_menu("Mi18", ["Tetap hadir tenang di pertemuan itu di sisi Miyuki.", "Minta mereka menunda pembicaraan jadwal pertunangan.", "Bicarakan dengan jujur alternatif masa depan yang diinginkan Miyuki."])
        if kk_has("sandiwara_diakui"):
            nar "Kamu menatap mata cokelat kemerahan Miyuki yang kini memancarkan tekad tenang, lalu mengangguk tipis memberinya dukungan penuh sebelum kamu membuka suara terlebih dahulu kepada seluruh meja."
            chiasa "Maaf menyela pembicaraan jadwal, Oji-san, Oba-san, dan Hayase-san. Sebelum pertemuan ini berjalan lebih jauh, ada satu hal dari Natal tahun lalu yang harus kami luruskan dengan jujur."
            nar "Miyuki mengembuskan napas panjang, lalu menumpukan kedua tangannya mantap di tepi meja sambil menatap kedua orang tuanya bergantian tanpa menyembunyikan keterlibatannya sedikit pun di balik namamu."
            miyuki "Kita ceritakan semuanya dari awal, Chiasa-chan. Termasuk bagian saat aku meminta bantuanmu untuk berpura-pura."
            miyuki "Ayah, Ibu, Hayase-san... hubungan yang kami umumkan di aula rumah sakit Natal tahun lalu bukan hubungan pacaran sungguhan. Aku yang menyetujui sandiwara itu bersama Chiasa karena saat itu aku merasa tidak punya jalan lain untuk menghentikan rencana omiai yang terus didorong."
            nar "Seluruh percakapan di ruang jamuan seketika padam. Wajah Tachibana Sayuri langsung memerah menahan malu sekaligus amarah, sementara Kazuhiro menurunkan cangkir tehnya begitu keras hingga sendok kecil di tatakan bergetar nyaring."
            "Ibu Miyuki" "Miyuki! Apa kamu sadar apa yang baru saja kamu ucapkan di depan keluarga Hayase?! Selama setahun penuh kamu mempermainkan Ayah dan Ibu dengan cerita bohong?!"
            "Ayah Miyuki" "Tindakan macam apa itu, Miyuki! Kamu menyeret adik tingkatmu sendiri untuk membohongi orang tua dan merusak nama baik keluarga Tachibana di depan kolega kita!"
            nar "Di seberang meja, tangan Tatsuru yang tadi masih bertumpu di dekat pita kotak bingkisan perlahan berhenti lalu ditarik mundur ke atas pangkuannya. Tidak ada amarah kasar di wajahnya, hanya raut terkejut dan kecewa yang amat tenang."
            "Tatsuru" "...Jadi sepanjang tahun kemarin, saat saya menjaga jarak karena menghormati pasangan pilihanmu, semuanya memang tidak pernah ada, Miyuki?"
            chiasa "Maaf, Hayase-san. Saya ikut terlibat sejak awal karena melihat Tachibana-senpai sangat tertekan tahun lalu. Kesalahan berpura-pura itu juga tanggung jawab saya."
            miyuki "Jangan hanya menyalahkan Chiasa, Ayah, Ibu. Keputusan itu keputusanku sendiri. Aku tidak ingin terus meminta kalian menghormati pilihanku sementara aku sendiri masih berlindung di balik cerita yang palsu."
            "Ibu Miyuki" "Kalau kamu sudah sadar perbuatanmu memalukan seperti itu, sekarang minta maaf yang layak ke keluarga Hayase dan setujui saja jadwal pertemuan bulan depan!"
            nar "Miyuki tetap duduk tegak menghadapi kemarahan ibunya. Mata cokelat kemerahannya tidak lagi menghindari tatapan siapa pun di meja itu."
            miyuki "Aku minta maaf setulusnya kepada Hayase-san dan keluarga karena telah berbohong tahun lalu. Aku tahu itu salah besar. Tapi aku ingin memperbaiki kesalahanku dengan kejujuran alih-alih menerima rencana pertunangan hanya karena merasa malu dan bersalah."
            "Tatsuru" "...Saya menghargai kamu akhirnya mengatakannya sendiri, Miyuki. Terus terang, kejujuran yang terlambat tetap jauh lebih saya hormati daripada kesopanan yang kosong. Oji-san, Oba-san, tolong jangan hanya menyalahkan Amamiya-san, karena tahun lalu saya juga sempat melihat betapa tertekannya Miyuki di aula."
            "Tatsuru" "Untuk hari ini, kurasa lebih baik kami undur diri dulu agar keluarga Tachibana bisa berbicara berdua dengan tenang."
            nar "Tatsuru beranjak berdiri dengan sangat santun, membungkuk singkat kepada Kazuhiro, Sayuri, dan Miyuki tanpa sedikit pun menyimpan nada mencela, lalu mengiringi kedua orang tuanya menuju pintu keluar ruang jamuan."
            "Ibu Miyuki" "Tatsuru-kun, tunggu dulu! Miyuki, cepat tahan mereka sekarang juga!"
            nar "Tatsuru berhenti sejenak di ambang pintu mahoni, menoleh ke arah Miyuki dengan tatapan yang sama sekali tidak menyimpan dendam."
            "Tatsuru" "Tidak perlu ditahan, Oba-san. Saya sudah paham posisimu sekarang, Miyuki. Jaga kesehatanmu baik-baik menghadapi ujian musim dingin nanti."
            miyuki "Sekali lagi saya minta maaf sebesar-besarnya, Hayase-san. Terima kasih sudah mau mendengarkan."
            miyuki "Biarkan mereka pulang dulu, Ibu. Aku siap menerima kemarahan Ayah dan Ibu hari ini, tapi aku tidak akan menarik kembali kata-kataku."
            nar "Sebelum melangkah mundur ke luar pintu agar keluarga Tachibana bisa berbicara, kamu menyentuh ringan punggung tangan Miyuki satu detik untuk menyalurkan kehangatan."
            chiasa "Tachibana-senpai, aku tunggu di luar koridor sampai pembicaraan keluargamu selesai ya. Kalau butuh apa-apa langsung panggil aku."
            miyuki "Terima kasih, Chiasa-chan. Badai di rumah setelah ini pasti panjang, tapi untuk pertama kalinya aku nggak merasa sedang bersembunyi lagi."
            nar "Suasana meja memang pecah oleh amarah kedua orang tuanya, dan harga kejujuran hari ini terasa amat berat di udara. Namun saat kamu melirik jari Miyuki di atas meja, tangannya sudah tidak lagi gemetar sedikit pun."
        elif kk_has("sandiwara_terbongkar"):
            nar "Kamu melangkah maju setengah langkah ke sisi kursi Miyuki, berusaha meredam tekanan meja dengan meminta jeda langsung kepada dokter muda di seberang sana."
            chiasa "Permisi, Hayase-san. Melihat jadwal praktikum Tachibana-senpai yang padat dan posisi kami sejak tahun lalu, bisakah pembicaraan soal tanggal acara keluarga ini ditunda dulu sampai semester depan?"
            nar "Tachibana Sayuri baru saja membuka mulut hendak menegurmu, tetapi Hayase Tatsuru mengangkat tangan kanannya dengan sangat sopan untuk meminta waktu bicara. Tatapannya tenang, jernih, dan jauh lebih tajam dari yang sempat kamu kira."
            "Tatsuru" "Sebentar, Amamiya-san. Saya memang tidak keberatan menunda jadwal apa pun kalau Miyuki belum siap. Tapi sebelum kita menunda lagi seperti tahun lalu, boleh saya ajukan satu pertanyaan jujur?"
            "Tatsuru" "Sepanjang tahun ini saya beberapa kali mampir ke perpustakaan kedokteran di akhir pekan dan mendengar cerita kolega tentang kegiatan kalian. Kalian nyaris tidak pernah terlihat bersama di luar acara resmi, bahkan teman-teman kelas Miyuki pun bingung saat mendengar kabar pasangan itu."
            "Tatsuru" "Miyuki... Natal tahun lalu waktu kalian datang ke aula bersama, apakah kalian waktu itu benar-benar berpacaran?"
            nar "Keheningan yang tajam dan dingin langsung jatuh di atas taplak meja putih. Mata Kazuhiro dan Sayuri serentak berpindah menatap wajah putri mereka. Miyuki sempat menoleh setengah detik kepadamu, lalu menarik bahunya tegak dan menolak menambah satu kebohongan baru lagi."
            miyuki "...Waktu itu? Tidak, Hayase-san. Kami tidak benar-benar berpacaran."
            nar "Miyuki menarik kursinya sedikit menjauh dari meja. Kini kedua keluarga membeku di tempat masing-masing, menunggu lanjutan ucapannya di tengah keheningan yang begitu menyesakkan."
            "Ibu Miyuki" "Apa?! Miyuki, jadi pengumuman di depan semua dokter rumah sakit tahun lalu itu cuma akal-akalan kalian berdua?!"
            "Ayah Miyuki" "Kamu mengerti tidak betapa malunya posisi kami sekarang di hadapan keluarga Hayase?!"
            miyuki "Ayah, Ibu, dengarkan dulu! Tahun lalu aku sudah berulang kali bilang belum siap membicarakan pertunangan, tapi setiap kali aku menolak dengan sopan, selalu dianggap cuma malu atau belum cukup matang!"
            chiasa "Oba-san, Oji-san, tahun lalu Tachibana-senpai sampai gemetar berdiri di luar pintu aula karena merasa nggak didengar sama sekali, sampai akhirnya kami nekat..."
            "Ibu Miyuki" "Cukup, Amamiya-san! Urusan kedisiplinan dan kehormatan keluarga Tachibana bukan tempat adik tingkat dari luar keluarga ikut menilai! Miyuki, sekarang kamu lihat sendiri akibatnya kalau kamu berbohong, kita hampir kehilangan muka total di depan keluarga besar!"
            nar "Di seberang meja, Hayase Tatsuru mengembuskan napas pelan lalu membalikkan map jadwal keluarga itu menghadap ke bawah di atas taplak putih. Tatapannya tampak lelah melihat arah perdebatan kedua orang tua Miyuki."
            nar "Semakin keras Miyuki berusaha menjelaskan tekanan yang membuat kebohongan itu dulu terasa sebagai satu-satunya pintu keluar, semakin jelas di matamu bahwa kedua orang tuanya hanya sedang mendengar soal kehilangan muka di depan tamu, sama sekali tidak menyimak perasaan putri mereka sendiri."
            "Tatsuru" "Oba-san, tenang dulu, saya tidak merasa direndahkan di sini. Saya cuma ingin tahu kenapa Miyuki harus sampai menempuh cara sejauh itu."
            miyuki "Aku seharusnya bicara lebih awal, Hayase-san, dan aku minta maaf karena sudah menyeret namamu dalam sandiwara itu. Tapi kesalahanku berbohong tahun lalu sama sekali tidak membuatku kehilangan hak untuk menolak rencana yang tidak kuinginkan hari ini."
            "Ayah Miyuki" "Amamiya-san, kurasa pertemuan hari ini sudah cukup sampai di sini untuk tamu dari luar keluarga. Kami perlu bicara serius dengan Miyuki."
            chiasa "Baik, Oji-san. Saya permisi keluar dulu... Tachibana-senpai, ponselku selalu aktif ya."
            miyuki "Aku mengerti, Chiasa-chan. Aku akan meneleponmu begitu pembicaraan ini selesai. Jangan khawatirkan aku."
            nar "Saat kamu menutup pintu ganda mahoni dari luar, suara keras Kazuhiro masih terdengar samar dari dalam. Suara Miyuki tadi terdengar sedikit bergetar di ujung kalimat, tetapi tatapan mata cokelat kemerahannya tetap berdiri tegak di tengah kehancuran sandiwara yang baru saja terbongkar di hadapan dua keluarga."
        elif kk_has("pasangan_palsu"):
            nar "Kamu tidak mundur selangkah pun. Persis seperti yang pernah kamu janjikan pada Miyuki di koridor aula Natal tahun lalu, kamu melangkah tenang ke sisi kursinya dan berdiri sejajar di sampingnya."
            chiasa "Permisi, Oji-san, Oba-san, Hayase-san. Seperti tahun lalu, saya ikut duduk di sebelah Tachibana-senpai hari ini."
            nar "Miyuki segera menggeser kursi kosong di sebelahnya sedikit lebih rapat untukmu. Bahunya yang sempat tegang merendah sedikit begitu kamu duduk tepat di sisinya."
            "Ibu Miyuki" "Kalian berdua masih saja meneruskan sikap ini rupanya. Baik, kalau kalian memang mengklaim menjalin hubungan serius sejak tahun lalu, Ibu mau dengar rencana konkret kalian setelah Miyuki masuk rotasi klinik nanti."
            "Ayah Miyuki" "Benar. Hubungan mahasiswa yang hanya muncul setiap kali ada acara keluarga tidak cukup untuk membuat kami membatalkan seluruh rencana masa depan rumah sakit. Bagaimana kalian membagi waktu saat Miyuki mulai jaga malam nanti?"
            nar "Pertanyaan tajam satu demi satu langsung meluncur dari seberang meja. Miyuki menjawab setiap pertanyaan tentang jadwal kuliah, kebiasaan belajar, hingga rencana tempat tinggal dengan nada halus dan urutan jawaban yang sudah kalian latih berkali-kali."
            miyuki "Chiasa sudah terbiasa dengan jadwalku yang padat sejak awal tahun ini, Ayah. Waktu minggu ujian praktikum kemarin saja dia yang sering membawakan makan malam ke perpustakaan tanpa pernah mengeluh soal jam belajarku."
            chiasa "Iya, Oji-san, Oba-san. Kami memang nggak selalu bisa ketemu tiap sore karena jadwal studio dan kedokteran sama-sama padat, tapi kami saling menyesuaikan."
            "Ibu Miyuki" "Begitu ya? Kalau memang sudah lebih dari setahun bersama, coba sebutkan kapan terakhir kali Chiasa-san mampir ke apartemen Miyuki dan bagaimana rencana kalian saat ujian lisensi nanti?"
            nar "Sesekali mata cokelat kemerahan Miyuki melirik singkat ke arahmu di bawah naungan rambut hitamnya untuk memastikan tidak ada satu pun rincian kecil yang meleset dari cerita tahun lalu."
            chiasa "Minggu lalu sehabis pameran seni selesai saya sempat mampir membawa kue bolu buat makan malam sebentar, Oba-san. Untuk persiapan ujian lisensi nanti, saya juga siap menyesuaikan jadwal kerja paruh waktu supaya nggak mengganggu jam belajar Senpai."
            miyuki "Benar, Ibu. Kami sudah membicarakan pembagian waktunya dari jauh-jauh hari."
            nar "Di seberang meja, Hayase Tatsuru menyimak tenang sambil sempat memperhatikan jeda setengah detik saat tatapanmu dan Miyuki saling bertemu sebelum menjawab. Ia tidak menuduh apa-apa, hanya menyandarkan punggungnya dengan sopan."
            "Tatsuru" "Kalian terlihat cukup kompak mengatur jadwal masing-masing. Kalau memang Miyuki merasa nyaman dengan pilihannya sekarang, saya tidak akan mendesak soal tanggal musim semi."
            "Ayah Miyuki" "Baik, hari ini kita tidak mengunci tanggal acara dengan keluarga Hayase dulu. Namun jika sampai kelulusan nanti tidak ada bukti keseriusan yang jelas dari rencana kalian, pembicaraan omiai ini tetap akan dibuka kembali."
            miyuki "Aku mengerti, Ayah. Terima kasih atas pengertiannya, Hayase-san."
            nar "Di bawah meja putih yang rapi, ujung jari Miyuki yang dingin menyentuh ringan pergelangan tanganmu tanda terima kasih. Meski kalian berhasil menahan desakan hari ini, keluarga Tachibana telah menaruh syarat baru yang jauh lebih ketat."
            nar "Begitu kalian pamit dan melangkah keluar melewati pintu mahoni ke koridor lantai atas yang lengang, Miyuki langsung menyandarkan punggungnya sebentar ke dinding marmer sambil mengembuskan napas panjang yang sejak tadi ia tahan."
            miyuki "Syarat baru dari Ayah soal bukti keseriusan sebelum kelulusan tadi... berarti tahun depan ruang gerak kita bakal jauh lebih sempit lagi ya, Chiasa-chan."
            chiasa "Iya, Senpai. Apalagi tadi Hayase-san kelihatan sempat memperhatikan waktu kita saling lirik sebelum menjawab pertanyaan Ibu. Kita harus benar-benar hati-hati menyusun langkah berikutnya bareng-bareng."
            miyuki "Terima kasih sudah tetap duduk di sebelahku sampai selesai. Aku nggak tahu harus bagaimana kalau tadi sendirian."
            chiasa "{i}Sandiwara yang tahun lalu kami buat cuma untuk bertahan satu hari kini makin membesar... dan menuntut masa depan sungguhan agar tetap dipercaya.{/i}"
            nar "Kalian berjalan menyusuri koridor rumah sakit tetap berdampingan, memikul kebohongan bersama yang kini membutuhkan rencana hidup utuh di depan mata orang tuanya."
        else:
            if _return == "A":
                nar "Kamu memilih menarik kursi tepat di belakang sisi kiri Miyuki, hadir sebagai teman yang tenang tanpa merebut panggungnya, memastikan ia tidak lagi merasa dikepung sendirian di dalam ruang jamuan itu."
                chiasa "Permisi, Oji-san, Oba-san, saya hanya duduk sebentar menemani Tachibana-senpai sesuai undangannya. Silakan lanjutkan pembicaraan keluarga."
                miyuki "Terima kasih sudah duduk di sebelahku, Chiasa-chan."
                nar "Miyuki melirik sekilas kepadamu dengan sorot mata cokelat kemerahan yang langsung lebih tenang, lalu memusatkan perhatiannya kembali kepada orang tuanya."
            elif _return == "B":
                nar "Kamu mengangkat tangan sopan sebelum Tachibana Sayuri sempat membuka map pilihan tanggal lebih lebar lagi."
                chiasa "Maaf menyela, Oji-san, Oba-san, dan Hayase-san. Setahu saya minggu-minggu ke depan Tachibana-senpai masih punya evaluasi praktikum yang sangat padat. Mungkin pembicaraan soal tanggal acara keluarga ini sebaiknya ditunda dulu sampai kepalanya lebih longgar?"
                "Ibu Miyuki" "Justru karena jadwalnya padat makanya orang tua membantu menyusunnya lebih awal, Amamiya-san. Miyuki sendiri kan biasanya menurut saja kalau sudah disiapkan."
                chiasa "Justru karena Senpai sering mengalah supaya suasana tenang, mungkin kali ini Senpai butuh waktu bernapas dulu, Oba-san."
            else:
                nar "Kamu menatap Miyuki yang memberi anggukan tipis, lalu membantunya membuka ruang percakapan soal rencana masa depannya sendiri di luar agenda keluarga."
                chiasa "Oji-san, Oba-san, kemarin di kampus Tachibana-senpai sempat cerita kalau ia sebenarnya sedang menimbang jalur riset klinik mandiri dulu setelah lulus nanti, sebelum memikirkan rencana pernikahan atau penggabungan manajemen rumah sakit."
                "Ayah Miyuki" "Rencana riset mandiri tetap bisa berjalan beriringan dengan pertunangan yang teratur, Amamiya-san. Apalagi Tatsuru-kun sendiri seorang dokter bedah yang paham dunia medis."
                chiasa "Tapi jadwal riset dan kebebasan memilih rumah sakit tujuan kan jauh lebih mudah ditentukan sendiri sebelum terikat acara resmi keluarga, Oji-san."
            nar "Di seberang meja, Tatsuru mengangguk sopan menanggapi ucapan orang tua Miyuki, meski matanya menangkap kekakuan di bahu Miyuki."
            "Tatsuru" "Saya tidak masalah menunggu kalau Miyuki ingin menyelesaikan target akademiknya dulu. Yang penting kita sepakat pada arah umumnya hari ini, jadi keluarga bisa mulai menyiapkan sisanya pelan-pelan."
            "Ibu Miyuki" "Nah, dengar sendiri kan betapa bijaksananya Tatsuru-kun, Miyuki? Jadi bulan Maret saja ya kita adakan pertemuan resmi kedua keluarga?"
            nar "Miyuki mendengarkan seluruh tanggapan keluarganya dan kalimat ramah Tatsuru sampai benar-benar tuntas. Tidak ada sedikit pun nada tergesa saat ia meletakkan cangkir teh porselennya kembali ke atas meja."
            nar "Ia menarik napas tenang, berusaha memisahkan sopan santun seorang anak dari persetujuan yang sejak awal terus diasumsikan oleh semua orang di ruangan ini."
            miyuki "Ayah, Ibu, Hayase-san... terima kasih atas perhatian dan bingkisannya. Tapi aku perlu meluruskan satu hal sekarang juga. Aku belum pernah memberikan persetujuan apa pun soal rencana pertunangan ini."
            "Ibu Miyuki" "Miyuki, jangan bicara seolah kamu tidak menghargai keluarga Hayase yang sudah repot datang hari ini..."
            miyuki "Aku menghargai mereka, makanya aku datang ke ruangan ini karena ingin membicarakan ini secara terbuka. Tapi kalau jawabannya sudah dianggap ada sebelum aku bicara, pertemuan ini sebenarnya untuk siapa?"
            nar "Pertanyaan jernih itu langsung menghentikan seluruh percakapan di meja panjang selama beberapa detik penuh. Kazuhiro terdiam memandangi putrinya, bibir Sayuri terkatup rapat, dan Tatsuru menunduk pelan menyadari batas yang baru saja Miyuki gariskan sendiri."
            "Tatsuru" "...Maafkan saya, Miyuki. Kalimat saya tadi memang terdengar seolah saya sudah mendahului keputusanmu. Kita tutup dulu pembahasan jadwal untuk hari ini."
            "Ayah Miyuki" "...Baik. Kalau memang itu maumu, kita simpan dulu map jadwal ini sampai ujian musim dinginmu selesai. Kita bicarakan ulang nanti dengan kepala lebih dingin."
            nar "Tachibana Sayuri menutup bibirnya dengan kaku tanpa membantah keputusan suaminya, sementara Kazuhiro merapikan map jadwal putih itu kembali ke sisi meja dengan gerakan berat."
            nar "Tidak lama kemudian, kalian berdua melangkah keluar menuju koridor lantai atas yang sepi. Begitu pintu mahoni menutup di belakang punggung kalian, Miyuki akhirnya mengembuskan napas panjang sambil bersandar pelan di pilar marmer."
            chiasa "Tachibana-senpai... tadi di dalam jelas dan tegas sekali. Bahkan Oji-san langsung menutup map jadwalnya tanpa bisa memaksa lebih jauh."
            miyuki "Padahal tepat sebelum kalimat itu keluar, suaraku hampir saja pecah lho, Chiasa-chan. Rasanya beda sekali dibanding Natal tahun lalu saat aku cuma bisa berdiri gugup di lorong ini memutar gelangku sendiri. Terima kasih sudah tetap di sini bersamaku."
            chiasa "Tangan Senpai bahkan sudah nggak dingin lagi sekarang. Ayo kita keluar cari minuman hangat dulu buat merayakan langkah pertama ini."
            miyuki "Fufu, ide bagus. Aku benar-benar butuh teh hangat yang manis sekarang."
            nar "Langkah itu belum menjadi kemenangan penuh, tetapi akhirnya membuka satu ruang nyata di tengah meja keluarga yang kini mau tidak mau harus diisi oleh suaranya sendiri."
    else:
        nar "Keluarga Hayase datang dengan bingkisan dan pilihan tanggal untuk acara berikutnya. Pertemuan belum dimulai, tetapi di meja sudah ada terlalu banyak benda yang membuat penolakan terasa seperti merusak pekerjaan banyak orang."
        miyuki "Mereka bilang ingin mendengar jawabanku. Lalu menanyakan bulan mana yang kosong sebelum aku menjawab."
        nar "Ia menarik kursi sendiri, tidak menunggu orang lain menentukan tempatnya."
        if kk_has("pasangan_palsu"):
            miyuki "Mereka masih ingat kita datang bersama tahun lalu."
            call kk_family_menu("Mi18", ["Duduk di samping Miyuki seperti tahun lalu.", "Minta Tatsuru menunda pembicaraan.", "Ceritakan mengapa kalian datang bersama tahun lalu."])
        else:
            call kk_family_menu("Mi18", ["Tetap hadir di pertemuan itu.", "Minta mereka menunda pembicaraan.", "Bicarakan dengan jujur alternatif yang kalian punya."])
        if kk_has("sandiwara_diakui"):
            miyuki "Kita ceritakan dari awal. Termasuk bagian saat berpura-pura. Aku nggak ingin meminta mereka menghormati pilihanku sambil terus memberi cerita yang palsu."
            nar "Ia menyampaikan kebenaran itu tanpa menyembunyikan keterlibatannya di balik namamu. Orang tua mereka marah; Tatsuru berhenti menyentuh bingkisan di depannya."
            miyuki "Aku tahu itu salah. Aku ingin memperbaikinya dengan jujur, bukan dengan menerima rencana lain karena malu."
        elif kk_has("sandiwara_terbongkar"):
            "Tatsuru" "Sebentar. Miyuki, waktu itu kalian benar-benar berpacaran?"
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
# │ AWALAN  : Tatsuru melamar.
# │ INTI    : A dukung / B halangi / C ajak kabur.
# │ AKHIRAN : ending Miyuki.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi25:
    call kk_scene_enter("miyuki","Natal · Keluarga Tachibana")
    nar "Tatsuru meletakkan kotak cincin di meja, belum membukanya. Orang tua kedua pihak mendadak punya urusan kecil untuk dikerjakan sambil tetap mendengar setiap napas."
    "Tatsuru" "Aku ingin jawabanmu, Miyuki. Keluarga kita sudah membicarakan banyak hal."
    miyuki "Keluarga kita, iya. Aku belum tahu apakah itu sama dengan kita berdua."
    nar "Tangannya diam di pangkuan. Di luar jendela lampu Natal menyala, tak peduli betapa sulit satu kata akan menjadi di dalam ruangan."
    call kk_family_menu("Mi25", ["Beri Miyuki dukungan untuk menerima.", "Minta Tatsuru berhenti mendesaknya.", "Tawarkan pergi bersama, jika ia menginginkannya."])
    if _return == "A":
        nar "Kau memberi dukungan untuk menerima. Miyuki memandangmu, lalu kotak di meja, mencari ketenangan pada persetujuan yang kini tampak datang dari semua arah."
        miyuki "Baik. Kita lanjutkan pembicaraan ini."
        nar "Kotak dibuka. Ucapan selamat mulai terdengar sebelum ia selesai menarik napas. Di wajahnya tersusun senyum yang sangat baik digunakan untuk foto keluarga."
    elif _return == "B":
        nar "Kau meminta Tatsuru berhenti mendesak. Ia sempat membantah bahwa dirinya hanya bertanya, tetapi Miyuki akhirnya mengangkat suara."
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
    nar "Lampu lobi apartemen yang berlapis marmer dingin menyala tenang ketika kamu melangkah masuk sepulang beraktivitas malam ini. Di sofa tunggu dekat pilar kaca, duduk seorang pria berjas gelap rapi yang posturnya terlalu tegak untuk sekadar bertamu santai."
    nar "Kenji Kisaragi. Kamu mengenali garis wajah tegasnya jauh lebih baik dari foto keluarga di nakas kamar daripada dari percakapan langsung. Tas kerja kulitnya masih berada tepat di samping sepatunya, belum dilepaskan jauh dari jangkauan, seolah kunjungan menemui anaknya sendiri hanya diselipkan di sela dua agenda kantor yang lebih pasti."
    nar "Begitu mendengar bunyi pintu kaca otomatis terbuka, Kenji menoleh dan bangkit berdiri sambil merapikan kancing jasnya."
    "Kenji" "Yutaka. Kamu baru pulang rupanya. Ayah sempat lewat distrik ini selesai rapat, jadi mampir sebentar memastikan apartemenmu baik-baik saja."
    nar "Nada suaranya datar dan tertata, terlalu kaku untuk disebut hangat sekaligus terlalu sopan untuk disebut marah. Kamu berhenti dua langkah di depan sofa lobi, menimbang bagaimana kamu hendak menghadapi ayah dari pemilik tubuh ini."
    call kk_family_menu("Y-D03", ["Sambut ayahmu.", "Lewati lobi tanpa menghampirinya.", "Duduk dan ajak ia bicara serius."])
    if _return == "B":
        nar "Kamu hanya mengangguk kaku dari jarak jauh tanpa memperlambat langkah, lalu langsung berbelok ke koridor lift yang pintunya kebetulan baru saja terbuka."
        yutaka "Maaf, Yah, aku masih ada tugas yang harus segera kukerjakan di atas."
        "Kenji" "...Begitu ya. Kalau begitu Ayah tidak mengganggu."
        nar "Pintu logam lift menutup perlahan, memotong sosok Kenji yang masih berdiri kaku dengan tas kerja di tangannya. Sepanjang lift naik ke lantai atas, kamu membuka layar ponselmu, diam-diam menunggu satu pesan masuk yang mungkin akan membuatnya terdengar bersalah lebih dulu."
        nar "Layar tetap gelap tanpa satu pun notifikasi. Ketika kamu membuka kunci pintu apartemen, ruangan luas itu menyambutmu kembali dengan kesunyian dingin yang sudah terlalu akrab."
    elif _return == "C":
        yutaka "Ayah sudah jauh-jauh mampir ke sini. Kalau memang nggak langsung dikejar jam rapat berikutnya, boleh duduk dulu lima menit? Ada hal yang mau kutanyakan langsung."
        nar "Kenji tampak sedikit terkejut, sekilas melirik arloji di pergelangan tangannya, lalu mematikan layar ponsel dan menyimpannya kembali ke saku dalam jas sebelum duduk di sofa lobi."
        "Kenji" "Silakan. Ada masalah dengan biaya apartemen atau urusan kuliahmu semester ini?"
        yutaka "Bukan soal uang, Yah. Uang bulanan selalu masuk tepat waktu dan lebih dari cukup. Aku cuma pengin dengar langsung dari Ayah, sebenarnya selain lulus kuliah tanpa bikin masalah, apa sih yang Ayah harapkan dariku?"
        nar "Kenji terdiam beberapa detik, tampak kikuk menghadapi pertanyaan yang tidak dapat dibereskan hanya dengan angka transfer. Jari-jarinya mengetuk pegangan tas kulitnya perlahan."
        "Kenji" "...Kamu jarang bertanya seterus terang itu, Yutaka. Ayah cuma ingin kamu punya pijakan yang cukup kuat supaya kelak tidak bergantung pada belas kasihan orang lain. Soal jalannya seperti apa, Ayah memang belum sempat membicarakannya pelan-pelan denganmu."
        yutaka "Kalau begitu, lain kali nggak usah cuma mampir lima menit di lobi sambil bawa tas kerja ya, Yah. Kita bisa cari makan malam biasa biar bisa ngobrol beneran."
        "Kenji" "...Baik. Bulan depan Ayah kosongkan satu malam untuk makan bersama. Jaga kesehatanmu di sini."
        nar "Jawaban Kenji masih kaku dan lambat. Meski begitu, untuk pertama kalinya malam ini kalian benar-benar berada di ruangan yang sama tanpa langsung kabur di balik kesibukan masing-masing."
    else:
        yutaka "Selamat malam, Yah. Jalanan ke sini lagi macet nggak tadi? Kalau mau minum hangat, di atas ada teh, atau kita ngobrol sebentar di sini juga boleh."
        "Kenji" "Tidak perlu repot naik, Ayah cuma sebentar. Jalanan agak padat di dekat stasiun tadi, tapi masih lancar. Kuliahmu semester ini bagaimana, tidak ada mata kuliah yang menyulitkan?"
        yutaka "Sejauh ini aman kok, Yah. Tugasnya lumayan banyak tapi masih kepegang semua."
        "Kenji" "Bagus kalau begitu. Pengaturan apartemen dan kebutuhan bulanan juga tidak ada kendala?"
        yutaka "Nggak ada kendala, semuanya lancar."
        nar "Hening canggung turun selama beberapa detik. Semua hal praktis sudah selesai ditanyakan, dan kalian berdua masih berdiri berhadapan di tengah lobi. Kamu bisa melihat Kenji mengerutkan kening tipis, berusaha mencari satu pertanyaan yang tidak terdengar seperti rapat laporan."
        "Kenji" "...Makanan di sekitar kampus cukup layak? Ibumu kemarin sempat mengingatkan supaya kamu tidak makan makanan dingin dari toko serba ada terlalu sering."
        yutaka "Lumayan sering masak sederhana sama makan hangat bareng teman kok, Yah. Bilangin ke Ibu nggak usah khawatir."
        "Kenji" "Syukurlah. Kalau begitu Ayah pamit dulu sebelum terlalu malam. Istirahat yang cukup, Yutaka."
        nar "Percakapan kalian memang belum terasa hangat. Meski begitu, melihat usahanya mencari pertanyaan sederhana di luar urusan laporan sedikit mengubah caramu memandang punggung pria yang melangkah keluar pintu kaca lobi itu."
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
    play sound "audio/sfx/phone_buzz.wav"
    nar "Di tengah suasana malam yang lengang, ponselmu bergetar satu kali. Nama pengirim yang muncul di layar membuat jarimu sempat berhenti di udara sebelum membuka aplikasinya."
    "Pesan Ibu" "Selamat malam, Yutaka. Apakah kamu sudah makan malam hari ini? Ibu hanya ingin menanyakan bagaimana kuliahmu minggu ini, apakah semuanya berjalan baik."
    nar "Kamu membaca ulang dua baris pesan dari Ibu Kisaragi itu sampai dua kali. Pesan itu berhenti tepat di situ sebagai pertanyaan pendek, jauh dari urusan dokumen maupun jadwal acara keluarga."
    nar "Kalimat sesederhana itu entah mengapa terasa sedikit asing sekaligus mencurigakan saat selama ini hubungan keluarga di tubuh Yutaka terlalu sering diukur lewat kewajiban dan kesopanan formal."
    call kk_family_menu("Y-D08", ["Ceritakan kabarmu dan tanyakan kabarnya.", "Balas singkat dengan sopan.", "Simpan ponsel tanpa membalas."])
    if _return == "A":
        yutaka "Malam, Bu. Sudah makan kok tadi, habis masak sup hangat sama teman-teman. Kuliah minggu ini lumayan padat tugas tapi masih seru dijalani. Ibu sendiri gimana kabarnya di rumah? Cuaca malam ini dingin banget lho."
        nar "Tanda terbaca muncul hampir seketika. Satu menit kemudian, balasan pertama masuk dengan susunan kata yang masih rapi dan tenang."
        play sound "audio/sfx/phone_buzz.wav"
        "Pesan Ibu" "Syukurlah kalau kamu makan dengan baik dan punya teman yang bisa diajak makan bersama. Kabar Ibu baik, Yutaka. Terima kasih sudah menanyakan."
        nar "Kamu mengira obrolan sudah berakhir di sana, sampai ponselmu kembali bergetar beberapa detik kemudian."
        play sound "audio/sfx/phone_buzz.wav"
        "Pesan Ibu" "Tadi sore Ibu membeli daun teh panggang baru yang aromanya lembut sekali. Kalau akhir pekan nanti kamu sedang tidak sibuk dengan kegiatan kampus, Ibu bisa kirimkan satu kaleng ke apartemenmu, atau kamu boleh mampir sebentar."
        yutaka "Boleh banget, Bu. Nanti kalau jadwalku longgar aku kabari ya. Ibu jangan lupa istirahat juga."
        nar "Kalian jelas belum berubah menjadi keluarga yang hangat dalam semalam. Meski begitu, ada celah pintu kecil yang baru saja terbuka, dan untuk sekali ini baik kamu maupun ibunya memilih untuk tidak langsung menutupnya lagi."
    elif _return == "B":
        yutaka "Selamat malam, Bu. Saya sudah makan malam dan kuliah minggu ini berjalan lancar. Terima kasih sudah menanyakan."
        play sound "audio/sfx/phone_buzz.wav"
        "Pesan Ibu" "Baik, Yutaka. Tolong jaga kesehatan dan jangan begadang terlalu larut. Selamat malam."
        nar "Percakapan berhenti tepat di titik itu. Kalian berdua telah menunaikan kesopanan dengan sempurna, tanpa pernah tahu apakah di balik layar sana ada salah seorang yang sebenarnya berharap obrolan ini berlangsung sedikit lebih lama."
    else:
        nar "Kamu menatap dua baris pesan itu hingga layar ponsel meredup sendiri, lalu meletakkannya telungkup di atas meja tanpa mengetik satu huruf pun."
        yutaka "{i}...Nanti saja deh. Aku lagi nggak tahu harus jawab apa.{/i}"
        nar "Saat layar menyala kembali beberapa saat kemudian karena notifikasi jam, pesan Ibu masih diam di tempat paling atas. Memilih diam memang memberimu kendali penuh untuk menghentikan percakapan, tetapi tidak sedikit pun menjelaskan kalimat seperti apa yang diam-diam kamu tunggu darinya."
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
    if kk_slot == 0:
        nar "Cahaya matahari pagi awal April masuk menembus tirai tipis ruang tamu apartemenmu yang terlalu lapang dan sunyi. Di atas meja makan kayu gelap, cangkir kopi hitammu masih mengepul tipis di samping buku teks semester baru yang baru saja kamu buka sebelum berangkat ke kampus."
    elif kk_slot in (1, 2):
        nar "Suasana ruang tamu apartemenmu terasa sejuk dan lengang di bawah cahaya siang menuju sore yang jatuh melintang di lantai kayu. Di atas meja makan, buku teks kuliah tahun ketiga terbuka berdampingan dengan catatan coretan yang sejak tadi kamu susun perlahan untuk mengejar materi semester baru."
    else:
        nar "Lampu gantung hangat menerangi meja makan kayu gelap di apartemenmu yang sunyi selepas jam makan malam. Di luar jendela kaca lebar, lampu kota berkelip tenang sementara di hadapanmu terbuka buku kuliah tahun ketiga penuh coretan catatan baru yang berusaha kamu pahami seorang diri."
    nar "Kamu baru saja menandai satu paragraf dengan pensil ketika ponsel di samping cangkir kopimu bergetar panjang di atas permukaan meja. Layar yang menyala menampilkan satu nama singkat yang jarang sekali muncul di riwayat panggilan suara, Ayah."
    nar "Kamu terdiam selama dua dering penuh menatap nama Kisaragi Kenji di layar itu, lalu menggeser tombol terima dan menempelkan ponsel ke telinga."
    if kk_slot == 0:
        yutaka "Halo, selamat pagi, Yah."
    elif kk_slot in (1, 2):
        yutaka "Halo, siang, Yah. Tumben telepon di jam kantor begini."
    else:
        yutaka "Halo, selamat malam, Yah."
    "Kenji" "Yutaka. Syukurlah kamu langsung mengangkat. Ayah punya jeda sekitar sepuluh menit sebelum rapat berikutnya, jadi sekalian menghubungi kamu langsung."
    nar "Suara Kisaragi Kenji terdengar tenang, kering, dan tertata rapi di seberang sambungan, diselingi bunyi samar lembaran berkas yang dibalik. Tidak ada pertanyaan pembuka tentang kesehatanmu ataupun apakah kamu sudah makan hari ini."
    "Kenji" "Laporan nilai akhir tahun keduamu kemarin sudah diterima. Hasilnya masih berada di kisaran yang cukup memuaskan, tidak ada masalah dengan administrasi kampus. Biaya apartemen dan kiriman bulanan untuk bulan ini juga sudah diproses seperti biasa."
    yutaka "Iya, kiriman bulan ini sudah masuk, terima kasih, Yah. Ibu gimana kabarnya?"
    "Kenji" "Ibumu sedang di luar kota mengurus pertemuan dengan rekanan sampai akhir pekan. Beliau menitipkan pesan singkat agar kamu mulai lebih serius menata jadwal tahun ketigamu."
    nar "Terdengar bunyi klik pulpen sekali di seberang telepon sebelum nada suara Kenji turun menjadi nada diskusi bisnis yang paling akrab baginya."
    "Kenji" "Karena itulah Ayah menelepon hari ini, Yutaka. Bulan ini kamu resmi masuk tahun ketiga. Di kampusmu, persiapan magang musim panas dan peta arah kerja setelah lulus sudah mulai bergerak. Jadi Ayah ingin mendengar langsung darimu, sudah ada rencana konkret apa yang ingin kamu ambil setelah wisuda nanti?"
    yutaka "Rencana setelah lulus... langsung dibahas sekarang ya, Yah?"
    "Kenji" "Dua tahun itu berjalan jauh lebih cepat daripada yang dibayangkan mahasiswa. Perusahaan distribusi kita tahun depan sedang menyiapkan perluasan jalur pasok regional. Kalau kamu berniat masuk ke Kisaragi selepas lulus, musim panas ini sebaiknya kamu mulai ikut pengenalan di divisi operasional, atau setidaknya melamar magang di perusahaan mitra."
    "Kenji" "Sebaliknya, kalau kamu punya rencana meniti pengalaman di luar selama dua atau tiga tahun lebih dulu, Ayah ingin tahu bidang apa yang kamu incar dan jejaring mana yang sedang kamu bangun. Ayah tidak mendikte secara mendadak, tapi Ayah butuh tahu kamu tidak sekadar menghabiskan dua tahun tersisa tanpa arah."
    nar "Pandanganmu turun menatap buku kuliah yang terbuka di atas meja, lalu singgah sejenak pada jam tangan tipis bertali kulit pemberian Daisuke yang melingkar di pergelangan kirimu."
    yutaka "{i}Di seberang sana dia lagi bicara sama putra yang sudah dibiayainya dua puluh tahun buat meneruskan usaha keluarga... sementara yang megang ponsel ini bahkan belum tahu masih bisa hidup lewat hari wisuda atau nggak.{/i}"
    nar "Hening pendek di sambungan membuat Kenji berdeham tipis menunggu jawabanmu."
    "Kenji" "Yutaka? Kamu masih di sana? Bagaimana pandanganmu sejauh ini?"
    yutaka "Masih di sini, Yah. Aku dengar jelas semuanya."
    "Kenji" "Di meja Ayah saat ini sudah ada tiga draf penempatan awal dari kepala divisi pengembangan wilayah untuk kuartal musim panas nanti."
    "Kenji" "Kalau kamu sudah punya gambaran arah yang jelas sejak bulan April ini, Ayah bisa meminta bagian personalia menyisihkan satu kursi observasi untukmu."
    nar "Dari balik pengeras suara ponsel, terdengar bunyi pintu ruang kerja yang diketuk pelan oleh asistennya sebelum kembali tertutup rapat."
    nar "Kisaragi Kenji berbicara dengan ritme teratur seorang pemimpin perusahaan yang terbiasa merencanakan langkah keluarganya beberapa tahun lebih awal."
    nar "Di matanya, status mahasiswa tahun ketiga bukan lagi masa pencarian bebas, melainkan tahap pemanasan terakhir sebelum masuk ke roda bisnis Kisaragi."
    nar "Kamu melirik deretan gedung tinggi Distrik Elite dari balik jendela kaca apartemenmu yang seluruh biaya sewanya masih dibayar oleh pria di seberang telepon ini."
    nar "Setiap fasilitas nyaman yang mengelilingi kehidupan harian Yutaka di kota ini pada dasarnya datang bersama ekspektasi jangka panjang yang tidak tertulis."
    nar "Menjawab terlalu patuh akan langsung mengikat waktu luangmu pada jadwal magang perusahaan keluarga yang menguras kebebasan gerakmu."
    nar "Sebaliknya, membantah terlalu keras tanpa alasan yang terukur hanya akan memancing pengawasan yang lebih ketat dari kedua orang tuanya."
    nar "Atau kamu juga bisa melemparkan satu nama besar di kampus yang pasti akan langsung mengalihkan fokus bisnis ayahmu ke arah lain."
    nar "Ketukan ujung pulpen Kenji kembali terdengar dua kali dari seberang sambungan, mengingatkan bahwa waktu sepuluh menitnya sebelum rapat terus berjalan."
    nar "Di atas meja makan, uap tipis dari cangkir kopimu hampir habis seluruhnya di tengah udara apartemen yang tenang."
    nar "Setiap kata yang akan kamu ucapkan ke mikrofon ponsel ini akan dicatat oleh Kenji sebagai pegangan untuk menilai langkahmu sepanjang tahun ketiga."
    nar "Kamu sudah mengenal betul bagaimana keluarga Kisaragi selalu mengukur hubungan manusia lewat keselarasan rencana dan manfaat masa depan."
    nar "Tanpa membiarkan jeda hening itu berlangsung lebih lama lagi, kamu menarik napas pendek dan menentukan sikapmu."
    nar "Kamu menegakkan posisi dudukmu di kursi meja makan sambil menyusun kalimat pembuka yang paling tepat untuk menghadapi pertanyaannya."
    call kk_family_menu("Y09", ["\"Sejauh ini aku sudah mulai memetakan beberapa pilihan, Yah, meski detail akhirnya memang belum kukunci semua.\"", "\"Soal mau ke mana setelah lulus, aku ingin menentukan keputusanku sendiri tanpa langsung diarahkan, Yah.\"", "\"Kalau soal lingkungan pergaulan yang Ayah dan Ibu singgung dulu, aku memang satu fakultas dan cukup mengenal Saionji Shiori.\""])
    if _return == "C":
        nar "Kamu menimbang sejenak bagaimana cara mengalihkan arah pertanyaan yang terlalu sempit itu, lalu memilih melempar nama yang pernah sekali disinggung orang tuamu lewat telepon lama."
        yutaka "Kalau soal membangun jejaring yang pernah Ayah sama Ibu singgung dulu... kebetulan di kampus aku memang satu fakultas dan cukup mengenal Saionji Shiori, Yah."
        nar "Bunyi lembaran kertas di seberang sambungan langsung berhenti total. Keheningan selama dua detik penuh itu terasa jauh lebih tajam daripada nada datar Kenji semenit yang lalu."
        "Kenji" "...Saionji Shiori? Putri tunggal keluarga Saionji Holdings?"
        yutaka "Iya, kami satu angkatan dan lumayan sering ketemu di kegiatan kampus. Belum ada urusan apa-apa sih, cuma sebatas kenal baik aja."
        "Kenji" "Tunggu dulu, Yutaka. Seberapa dekat tepatnya kalian sekarang? Kamu cuma sebatas saling sapa di ruang kuliah, atau sudah pernah berbincang panjang dan dikenal oleh pihak keluarganya?"
        nar "Nada suara Kenji berubah seketika. Sisi dingin seorang ayah yang biasanya hanya memeriksa angka nilai mendadak penuh perhatian terukur layaknya eksekutif yang baru menemukan celah kontrak besar."
        yutaka "Kami beberapa kali ngobrol santai di kampus sama di kegiatan klub, Yah. Nggak ada urusan khusus sama keluarganya juga, murni pertemanan satu fakultas aja."
        "Kenji" "Pertemanan satu fakultas sejak masa kuliah justru sering menjadi pintu paling bersih sebelum masuk ke meja bisnis, Yutaka. Jalur distribusi logistik kita di kawasan barat kebetulan beberapa kali bersinggungan dengan anak usaha grup Saionji. Kalau kamu memang punya hubungan baik dengannya, jangan disia-siakan."
        yutaka "Ayah, aku tadi cuma nyebut buat bilang lingkungan pergaulanku di kampus baik-baik aja, nggak usah langsung ditarik ke urusan perusahaan."
        "Kenji" "Ayah tahu batasnya, tentu saja kamu tidak boleh terlihat memaksa di depan putri keluarga sebesar itu. Hanya saja, jaga reputasimu di kampus dengan rapi. Kalau nanti ada kesempatan makan malam resmi atau acara yayasan yang melibatkan keluarga mereka, kabari Ayah lebih awal. Ayah bisa minta sekretaris menyiapkan bingkisan yang pantas atas nama keluarga Kisaragi."
        yutaka "...Iya, Yah. Nanti kulihat situasinya dulu."
        "Kenji" "Bagus. Ibumu pasti ikut senang mendengar kamu mulai memperhatikan pergaulan yang tepat di tahun ketiga. Rapat Ayah sebentar lagi dimulai, kita bicarakan lagi akhir bulan."
        yutaka "Baik, Yah. Selamat rapat."
        nar "Begitu layar ponsel meredup, keheningan ruang makan apartemen kembali terasa menekan di sekeliling mejamu."
        nar "Kamu meraih cangkir kopi hitam yang sudah mulai dingin di samping buku teks lalu menyesapnya perlahan sambil menatap pantulan kaca jendela."
        nar "Menyebut nama Saionji Shiori memang terbukti ampuh menghentikan desakan ayahmu soal magang divisi operasional musim panas ini."
        nar "Kenji bahkan langsung melupakan pertanyaannya mengenai peta karier lima tahun ke depan begitu mendengar peluang kedekatan dengan putri tunggal Saionji Holdings."
        nar "Namun perubahan nada bicaranya yang seketika berganti menjadi antusiasme seorang pebisnis menunjukkan betapa cepat nama itu tercatat sebagai aset di kepalanya."
        nar "Di lingkungan keluarga seperti Kisaragi dan Saionji, satu penyebutan nama di meja telepon tidak pernah berhenti sebagai obrolan santai belaka."
        nar "Mulai akhir bulan nanti, ayah dan ibumu pasti akan terus menanyakan perkembangan hubunganmu dengan Shiori setiap kali mereka menghubungi."
        nar "Jika Shiori sampai mengetahui bahwa namanya kamu gunakan sebagai tameng negosiasi di hadapan keluargamu, kepercayaan yang baru dibangun di ruang klub catur bisa runtuh seketika."
        nar "Kamu telah membeli kelonggaran waktu untuk semester ini dengan menggadaikan ketenangan pergaulanmu sendiri di fakultas."
        nar "Jarum jam tangan kulit di pergelangan kirimu terus berdetak pelan di tengah ruang tamu yang lapang."
        nar "Kamu menutup buku catatan semester baru di hadapanmu sambil merapikan letak pensil ke samping cangkir kopi."
        nar "Di luar jendela kaca apartemen, deretan kendaraan di jalan utama Distrik Elite tampak bergerak teratur di bawah langit bulan April."
        nar "Menjadikan marga Saionji sebagai umpan pembicaraan memang memberi hasil instan, tetapi juga mengundang ekspektasi baru yang jauh lebih rumit."
        nar "Kamu harus memastikan Shiori tidak pernah merasa didekati demi kepentingan jaringan logistik keluarga Kisaragi."
        nar "Dengan kening sedikit berkerut, kamu menyimpan catatan kuliahmu ke dalam tas sebelum bersiap menjalani sisa agenda hari ini."
        nar "Langkah yang baru saja kamu pilih menuntutmu untuk berhati-hati menjaga jarak antara urusan kampus dan ambisi orang tua Yutaka."
        nar "Sambungan telepon terputus. Kamu meletakkan ponsel agak keras ke atas meja kayu sambil mengusap pelipis. Dalam hitungan kurang dari dua menit, satu kalimat yang tadi kamu ucapkan demi menarik perhatian ayahmu baru saja mengubah hubungan pribadi menjadi peluang bisnis di kepalanya, dan kamu sadar akan jauh lebih sulit memintanya melupakan kepentingan yang sudah telanjur ia bayangkan."
    elif _return == "B":
        nar "Rahangmu sedikit mengeras mendengar masa depan tubuh ini dibahas serapi jadwal pengiriman barang. Kamu bersandar ke sandaran kursi dan memilih menjawab secara lugas tanpa membungkusnya dengan basa-basi."
        yutaka "Maaf, Yah, tapi soal mau ke mana setelah lulus nanti, aku ingin itu tetap jadi keputusanku sendiri. Aku nggak mau jalur hidupku langsung dipatok masuk divisi operasional atau ikut daftar perusahaan mitra cuma karena dianggap paling praktis."
        nar "Di seberang telepon tidak terdengar bentakan ataupun suara meninggi. Justru keheningan dingin yang menyusul selama tiga detik terasa jauh lebih menekan sebelum Kenji kembali bersuara dengan ketenangan yang tajam."
        "Kenji" "Ayah tidak melarang kamu memilih jalanmu sendiri, Yutaka. Tapi sebelum kamu bicara soal kemandirian penuh, Ayah mau bertanya satu hal sederhana. Apakah kamu sudah menghitung biaya hidup, sewa apartemen tempatmu tinggal sekarang, dan tanggung jawab penuh yang menempel di belakang kalimatmu barusan?"
        yutaka "Aku tahu semua fasilitas di sini masih datang dari Ayah sama Ibu. Aku juga nggak pernah pura-pura lupa soal itu."
        "Kenji" "Bagus kalau kamu sadar. Mudah sekali mengucapkan bahwa keputusan ada di tanganmu sendiri selama seluruh tagihan bulanan masih ditanggung rekening keluarga. Kalau kamu memang menolak jalur yang Ayah tawarkan, tunjukkan peta rencanamu yang lebih baik."
        yutaka "Terus terang aja, Yah, aku belum punya rencana lengkap sampai lima tahun ke depan. Aku memang masih nyari tahu bidang apa yang beneran sanggup kupikul sendiri. Tapi kalau tiap kali aku belum punya jawaban final lalu langsung disuruh ikut rute yang sudah disiapkan Ayah, sampai lulus pun aku nggak bakal pernah belajar ambil keputusan sendiri."
        nar "Kalian berdua terdengar persis seperti dua pihak yang sedang berunding di meja rapat, saling menguji batas tanpa ada satu pun yang bersedia melunak duluan. Kamu membenci dinginnya percakapan ini, sekaligus diam-diam membutuhkan ketegasan batas itu agar tidak terus terseret oleh peran orang lain."
        "Kenji" "...Setidaknya kali ini kamu jujur mengakui bahwa rencanamu memang belum selesai, dan tidak asal memberi alasan manis."
        yutaka "Aku nggak mau bikin janji kosong cuma supaya telepon ini cepat selesai, Yah."
        "Kenji" "Baik. Ayah beri kamu waktu sepanjang tahun ketiga ini untuk membuktikan bahwa pilihanmu sendiri layak diperhitungkan. Gunakan dana yang ada untuk belajar dengan benar, dan akhir tahun nanti kita bicara lagi dengan hasil nyata. Jaga kesehatanmu."
        yutaka "Iya, terima kasih, Yah."
        "Kenji" "Satu hal lagi sebelum Ayah masuk ke ruang rapat. Jangan ragu menghubungi sekretaris kantor kalau kamu butuh data industri untuk menyusun rencanamu itu."
        yutaka "Baik, Yah. Nanti kukabari kalau memang diperlukan."
        nar "Layar ponsel kembali gelap setelah nada putus singkat terdengar di telingamu."
        nar "Kamu meletakkan ponsel itu di samping buku teks kuliah lalu menyandarkan punggung ke kursi kayu sambil mengembuskan napas panjang."
        nar "Menolak jalur instan yang disodorkan Kisaragi Kenji memang membuat ketegangan di antara kalian terasa dingin dan tanpa basa-basi."
        nar "Akan tetapi, cara ayah Yutaka menanggapi kejujuranmu barusan memperlihatkan bahwa pria itu jauh lebih menghormati bantahan yang berdasar daripada kepatuhan yang palsu."
        nar "Ia tidak memotong uang kiriman bulananmu dan tidak pula memaksamu masuk ke divisi operasional musim panas ini secara sepihak."
        nar "Sebagai gantinya, ia memberikan tenggat satu tahun penuh yang menuntut pembuktian nyata sebelum kamu menginjak tahun terakhir kuliah."
        nar "Di satu sisi, ketegasan itu memberimu ruang bernapas yang bersih dari campur tangan keluarga sepanjang semester ketiga ini."
        nar "Di sisi lain, kamu kini memikul beban untuk memastikan kehidupan akademik Yutaka tetap berjalan meyakinkan di tengah seluruh persoalan yang sedang kamu hadapi."
        nar "Kamu menatap deretan perabot minimalis di ruang tengah apartemen yang terasa begitu tertib sekaligus menuntut pertanggungjawaban."
        nar "Cangkir kopi di dekat tanganmu kamu angkat kembali untuk menghabiskan sisa tegukan terakhir sebelum bersiap menjalani jadwal hari ini."
        nar "Keheningan yang tertinggal setelah panggilan telepon itu tidak lagi terasa menyesakkan, melainkan menyerupai ruang kerja yang menunggu diisi."
        nar "Selama satu tahun ke depan, kamu memegang kendali penuh atas jadwal harianmu tanpa harus melapor ke divisi operasional perusahaan keluarga."
        nar "Kamu merapikan lembar catatan semester ketiga di atas meja makan dan memasukkannya ke dalam map kulitmu."
        nar "Tantangan dari Kenji untuk menunjukkan hasil nyata di akhir tahun nanti justru memperjelas batas waktu yang sedang kamu miliki."
        nar "Di luar kaca jendela apartemen, angin bulan April menggoyangkan pucuk pepohonan jalan raya Distrik Elite dengan tenang."
        nar "Kemampuanmu berdiri di atas kaki sendiri tahun ini akan menjadi bukti terbaik saat kamu kembali berbicara dengan ayahmu nanti."
        nar "Kamu merapikan letak kursi kayu ruang makan sebelum melangkah mengambil tas kuliahmu di dekat sofa."
        nar "Pikiranmu kini terasa jauh lebih jernih untuk menghadapi jadwal perkuliahan hari ini."
        nar "Setidaknya dengan menarik garis batas secara terang-terangan hari ini, kamu tidak perlu berpura-pura menjadi anak penurut yang pasrah diatur dari jauh."
        nar "Bunyi klik singkat menandai panggilan berakhir. Kamu menurunkan ponsel perlahan, memandang ruangan apartemen mewah yang terasa semakin asing sekaligus jelas batasnya."
    else:
        nar "Kamu menarik napas perlahan dan memilih bersikap tenang serta terukur. Memancing pertengkaran di telepon sekarang tidak akan membereskan apa pun, sementara menjawab jujur secukupnya masih memberimu ruang gerak."
        yutaka "Sejauh ini aku memang sudah mulai memetakan beberapa pilihan, Yah. Untuk semester ini aku mau merapikan dulu dasar analisis sama mata kuliah inti tahun ketiga biar nggak keteteran, terus musim panas nanti rencana mau lihat beberapa peluang magang di luar dulu buat tahu cara kerja di lapangan."
        nar "Kamu berhenti sejenak, lalu menambahkan dengan nada jujur tanpa dibuat-buat."
        yutaka "Kalau soal keputusan akhir mau langsung masuk Kisaragi atau cari pengalaman di perusahaan lain dulu, jujur aja aku masih belum mengunci jawabannya sekarang, Yah. Aku pengin lihat langsung dulu bidang mana yang paling cocok waktu magang nanti."
        nar "Di seberang sambungan, Kenji diam mendengarkan sampai kalimatmu benar-benar selesai tanpa sekali pun memotong."
        "Kenji" "Pendekatan yang cukup realistis. Mencoba magang di luar sebelum memutuskan kembali ke usaha keluarga sebenarnya bukan ide buruk. Kamu perlu melihat bagaimana struktur perusahaan lain bekerja supaya sudut pandangmu tidak sempit."
        yutaka "Ayah nggak keberatan kalau musim panas ini aku nggak langsung ikut divisi operasional dulu?"
        "Kenji" "Tidak masalah, selama tempat magang yang kamu pilih punya bobot kerja yang jelas dan sungguh-sungguh melatih cara berpikirmu. Nanti Ayah kirimkan daftar dua perusahaan logistik rekanan dan satu firma riset pasar yang biasa menerima mahasiswa tahun ketiga. Kamu tidak wajib melamar ke sana, anggap saja bahan pembanding."
        yutaka "Baik, Yah. Nanti kubaca dulu begitu berkasnya masuk."
        nar "Terdengar suara kertas dirapikan di meja Kenji, menandakan waktunya sebelum rapat hampir habis. Tepat saat kamu mengira ia akan langsung memutus sambungan, ada jeda satu detik yang terasa sedikit canggung."
        "Kenji" "...Jadwal tahun ketiga biasanya membuat jam makan berantakan. Pastikan kamu tetap makan teratur, Yutaka. Ibumu kemarin sempat menanyakan apakah kamu masih sering pulang larut."
        yutaka "Aman kok, Yah, aku lumayan sering makan hangat bareng teman-teman. Sampaikan salamku buat Ibu kalau sudah pulang."
        "Kenji" "Akan Ayah sampaikan. Selamat melanjutkan belajarmu."
        yutaka "Selamat bekerja juga, Yah."
        nar "Panggilan suara itu berakhir tepat ketika jam dinding ruang makan menunjukkan waktu sepuluh menit sejak dering pertama berbunyi."
        nar "Kamu menurunkan ponsel dari telinga dan menatap layar yang kembali meredup di samping buku teks semester ketiga."
        nar "Menanggapi pertanyaan Kenji dengan sikap kooperatif yang terukur terbukti menjadi langkah paling aman untuk menjaga ketenangan di kedua belah pihak."
        nar "Dengan mengakui secara jujur bahwa kamu ingin melihat pengalaman magang di luar lebih dulu, kamu berhasil menghindari penempatan langsung di perusahaan keluarga."
        nar "Kenji pun tampak cukup puas karena putranya menunjukkan kerangka berpikir yang logis dan tidak sekadar menghamburkan waktu kuliah."
        nar "Pertanyaan singkatnya di akhir pembicaraan mengenai jam makan dan pesan ibumu memperlihatkan cara perhatian keluarga Kisaragi yang kaku namun tetap ada."
        nar "Tak lama setelah telepon ditutup, satu notifikasi surat elektronik masuk ke layar ponselmu dari alamat sekretariat kantor Kisaragi."
        nar "Berkas lampiran berisi profil dua perusahaan logistik rekanan dan satu firma riset pasar yang dijanjikan ayahmu sudah tersusun rapi di sana."
        nar "Kamu menandai surat elektronik tersebut untuk dibaca nanti malam tanpa harus merasa terburu-buru mengambil keputusan hari ini."
        nar "Ketenangan yang terjaga dalam hubungan keluarga ini memberimu keleluasaan penuh untuk mengatur langkahmu sendiri di kampus sepanjang semester baru."
        nar "Kamu meraih pensil di atas meja dan kembali melanjutkan membaca paragraf buku kuliah yang tadi sempat tertunda oleh dering telepon."
        nar "Tidak ada kecurigaan maupun ketegangan baru yang muncul dari pihak orang tua Yutaka setelah percakapan singkat yang tertata barusan."
        nar "Daftar perusahaan rekanan yang dikirimkan sekretariat kantor ayahmu bahkan bisa menjadi cadangan berguna bila kamu membutuhkan alasan kegiatan di musim panas."
        nar "Kamu membawa cangkir kopimu yang telah kosong ke wastafel dapur lalu membilasnya dengan air hangat."
        nar "Sinar cahaya dari luar jendela apartemen menerangi meja makan yang kini kembali siap menemani rutinitas kuliah tahun ketigamu."
        nar "Menjaga komunikasi yang tertib dengan Kenji memastikan kamu tidak perlu menghadapi intervensi mendadak dari pihak keluarga Kisaragi."
        nar "Kamu mengeringkan tanganmu dengan handuk dapur sambil menyusun urutan buku yang perlu kamu bawa ke kampus."
        nar "Segala urusan mengenai masa depan selepas wisuda kini telah tertata pada tempatnya tanpa mengganggu fokusmu hari ini."
        nar "Kamu kembali ke meja makan dengan langkah yang tenang dan siap melanjutkan aktivitasmu."
        nar "Suasana apartemen yang sunyi kini terasa jauh lebih ringan setelah satu kewajiban keluarga berhasil kamu tangani dengan rapi."
        nar "Sambungan terputus dengan tenang. Tidak semua saran Kenji cocok dengan situasi sebenarnya yang sedang kamu hadapi di dunia ini, tetapi setidaknya obrolan tadi tidak berubah menjadi bentrokan dingin. Kamu meletakkan ponsel di samping buku kuliah dengan daftar tugas nyata di kepala yang bisa kamu susun langkah demi langkah."
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
