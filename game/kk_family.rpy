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
    if kk_host == "chiasa":
        nar "Sore itu kamu mampir ke kafe kecil di sudut lobi Rumah Sakit Tachibana untuk mengembalikan buku catatan anatomi warna milik Miyuki yang kemarin tertinggal di meja kantin kampus. Saat kamu mendorong pintu kaca kafe, Miyuki sudah duduk di meja dekat dinding taman dalam, dan ia tampak tidak sedang sendirian."
        nar "Di seberang mejanya, seorang pria muda berusia sekitar dua puluh enam tahun dengan setelan jas dokter putih yang sangat rapi dan postur tegak baru saja berdiri sambil merapikan kancing jasnya. Begitu melihatmu berjalan mendekati meja, pria itu tersenyum sopan dan menggeser kursinya sedikit memberi ruang."
        "Takeru" "Oh, ini adik tingkat dari kampus yang tadi Anda sebutkan ya, Tachibana-san? Kalau begitu saya permisi kembali ke ruang jaga bedah dulu supaya kalian bisa mengobrol santai."
        miyuki "Terima kasih sudah menyempatkan turun, Hayase-san. Selamat bertugas kembali."
        "Takeru" "Sama-sama. Dan soal undangan makan malam keluarga akhir pekan nanti, tolong jangan dipikirkan terlalu berat ya, Tachibana-san. Saya tahu jadwal kuliah tahun ketiga Anda sedang padat, jadi saya sama sekali tidak keberatan menunggu sampai Anda siap."
        nar "Pria itu membungkuk sopan satu kali ke arahmu, lalu melangkah tenang meninggalkan kafe menuju deretan lift rumah sakit. Begitu pintu lift tertutup, Miyuki mengembuskan napas panjang dan meletakkan sebuah amplop kertas krem tebal yang tadinya ia pangku ke atas permukaan meja."
        chiasa "Siapa dokter yang barusan pergi itu, Tachibana-senpai? Asisten dosen Senpai di sini?"
        miyuki "Bukan, Chiasa-chan. Namanya Hayase Takeru. Dia dokter residen bedah di rumah sakit rekanan milik teman lama ayahku."
        nar "Kamu duduk di kursi seberangnya sambil melirik kartu undangan yang menyembul setengah dari dalam amplop krem tersebut. Kertasnya tebal dengan huruf cetak timbul berwarna emas, jauh terlalu resmi untuk ukuran makan malam biasa. Di bagian tengahnya tertulis nama keluarga Hayase sejajar dengan nama keluarga Tachibana, sementara nama Miyuki sendiri hanya dicantumkan kecil di baris bawah."
        miyuki "Tadi siang sekretaris Ibu mengantarkan amplop ini ke lobi fakultas, lalu barusan Hayase-san mampir sendiri buat menyapa. Ibu bilang sudah waktunya kami berdua mulai saling mengenal untuk arah yang serius."
        chiasa "Arah yang serius... maksudnya ini undangan omiai, Senpai?"
        miyuki "Iya, pertemuan perjodohan keluarga. Yang bikin aku capek, kata 'serius' di undangan ini sudah ditentukan bulat-bulat oleh kedua orang tua kami bahkan sebelum ada satu pun yang bertanya apakah aku ingin mengenal orangnya atau tidak."
        nar "Miyuki merapikan kedua sisi amplop tebal itu dengan ujung jarinya, menjaga kertasnya tetap lurus di atas meja sambil menatapmu dengan raut bingung."
    else:
        nar "Sore itu kamu mampir ke kafe lobi Rumah Sakit Tachibana untuk mengantarkan buku referensi Miyuki yang kemarin tertinggal selepas kelompok belajar. Dari balik dinding kaca kafe, kamu melihat Miyuki sudah duduk di meja dekat taman dalam, tetapi ada seorang pria yang sedang berbicara dengannya."
        nar "Pria berusia pertengahan dua puluhan itu mengenakan jas dokter putih bersih di atas kemeja berdasi rapi. Ketika melihatmu melangkah menghampiri meja, ia segera berdiri dengan sikap santun dan tersenyum ramah."
        "Takeru" "Oh, ini teman kampusmu yang mau mengantar buku tadi ya, Tachibana-san? Kalau begitu saya permisi kembali ke bangsal bedah sekarang."
        miyuki "Terima kasih sudah meluangkan waktu istirahatnya, Hayase-san. Selamat kembali bertugas."
        "Takeru" "Tentu. Soal acara makan malam akhir pekan nanti, tidak perlu merasa terbebani ya, Tachibana-san. Saya paham Anda sedang fokus studi, jadi saya tidak keberatan menunggu."
        nar "Pria tersebut mengangguk sopan kepadamu sebelum berjalan menuju lorong lift utama. Setelah sosoknya tidak lagi terlihat, Miyuki menyandarkan punggungnya ke kursi dan menaruh sebuah amplop krem tebal dari pangkuannya ke atas meja kayu."
        yutaka "Siapa dokter yang barusan itu, Tachibana-senpai? Senior pembimbing praktikmu?"
        miyuki "Bukan, Yutaka-kun. Itu Hayase Takeru, residen bedah berusia dua puluh enam tahun dari rumah sakit kolega ayahku."
        nar "Kamu menarik kursi di hadapannya dan melirik kartu undangan yang setengah terbuka dari amplop krem tersebut. Cetakan huruf timbulnya tampak sangat formal; nama besar keluarga Hayase dan keluarga Tachibana terpampang mencolok di bagian atas, sedangkan nama Miyuki hanya tertulis satu kali sebagai keterangan tambahan di bawah."
        miyuki "Ibu menyuruh orang mengantarkan amplop ini tadi siang. Katanya keluarga kami dan keluarga Hayase sepakat sudah saatnya kami berdua menjalin perkenalan yang serius."
        yutaka "Perkenalan resmi keluarga... maksud Senpai semacam omiai?"
        miyuki "Iya. Lucunya, kesimpulan bahwa pertemuan ini 'serius' sudah mereka ketok palu duluan di antara orang tua, tanpa pernah sekali pun menanyakan pendapatku lebih dulu."
        nar "Miyuki memegang tepi amplop kaku itu dengan kedua tangannya, menatap kertas undangan tersebut dengan senyum tipis yang tampak tertekan."
    call kk_family_menu("Mi07", ["\"Kelihatannya Hayase-san sopan sih, nggak ada salahnya dengerin dulu maksudnya.\"", "\"Kalau Senpai belum siap, minta aja mereka kasih ruang dulu.\"", "\"Pertemuan kayak gini cuma masuk akal kalau Senpai bebas nolak tanpa dicap nggak tahu terima kasih.\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Kalau dilihat sekilas tadi, kelihatannya Hayase-san orangnya cukup sopan dan nggak memaksa sih, Tachibana-senpai. Mungkin nggak ada salahnya kalau Senpai hadir sekali aja akhir pekan ini buat dengerin dulu maksudnya gimana."
            nar "Miyuki menatap amplop di depannya, lalu mengangguk perlahan seolah sedang berusaha meyakinkan dirinya sendiri dengan alasan yang baru saja kamu berikan."
            miyuki "Iya... mungkin kamu benar ya, Chiasa-chan. Datang duduk makan malam dan mendengarkan mereka bicara satu kali kan bukan berarti aku langsung mengiyakan pertunangan."
            chiasa "Betul, Senpai. Paling nggak kalau Senpai datang sekali, Ibu Senpai nggak langsung marah-marah."
            miyuki "Aku harus terus mengingat kalimat itu waktu duduk di meja makan nanti. Soalnya kalau di depan Ibu, begitu aku duduk diam dan tersenyum sopan, beliau sering langsung menganggap itu sebagai tanda setuju."
            nar "Miyuki mendorong kembali kartu undangan itu masuk ke dalam amplopnya, lalu menyimpannya ke dalam tas kuliahnya. Raut wajahnya memang belum terlihat lebih lega, tetapi kini pertemuan omiai akhir pekan itu sudah dipastikan akan berjalan."
        else:
            yutaka "Kalau dilihat dari caranya pamit barusan, kelihatannya Hayase-san orang yang cukup sopan sih, Tachibana-senpai. Mungkin nggak ada ruginya kalau Senpai datang sekali akhir pekan ini buat dengerin dulu pembicaraannya."
            nar "Miyuki memandangi amplop krem di tangannya sejenak, lalu mengangguk pelan menerima saran yang terdengar paling aman bagi semua pihak itu."
            miyuki "Iya... benar juga kata kamu, Yutaka-kun. Sekadar hadir memenuhi undangan makan malam dan mendengar maksud mereka kan tidak sama dengan langsung menerima lamaran."
            yutaka "Iya, Senpai. Lihat aja dulu gimana sikap orangnya waktu di meja makan nanti."
            miyuki "Aku harus menjaga batas itu baik-baik akhir pekan nanti. Soalnya keluargaku punya kebiasaan langsung membicarakan tahap berikutnya begitu melihat aku tidak membantah di pertemuan pertama."
            nar "Ia memasukkan kembali amplop undangan itu ke dalam tasnya dengan gerakan rapi. Meski beban di wajahnya belum berkurang, satu pertemuan resmi dengan keluarga Hayase kini sudah punya cukup alasan untuk terlaksana."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Kalau Senpai memang belum mau mikirin soal perjodohan sekarang, bilang aja tegas-tegas ke orang tua Senpai sama Hayase-san buat kasih ruang dulu. Senpai kan baru tahun ketiga dan lagi padat banget jadwal praktiknya, nggak adil kalau diburu-buru begini."
            nar "Miyuki tersenyum lembut mendengar kamu langsung membelanya dengan bersemangat, lalu sedetik kemudian ia menggeleng pelan."
            miyuki "Aku senang banget kamu langsung mikirin posisiku sampai segitunya, Chiasa-chan. Beneran."
            chiasa "Habisnya kelihatan banget Senpai nggak nyaman sama undangan itu dari tadi."
            miyuki "Memang nggak nyaman. Tapi masalahnya... di keluargaku, kalau aku tiba-tiba menolak hadir memakai alasan butuh ruang, Ibu justru langsung curiga ada orang di kampus yang memengaruhiku untuk membangkang."
            chiasa "Lho, kok malah mikirnya ke situ?"
            miyuki "Waktu SMA dulu pernah kejadian sekali waktu aku menolak ikut acara kolega Ayah. Bukannya memberi ruang, minggu depannya Ibu malah memajukan jadwal acaranya dua kali lebih padat sebelum aku sempat punya alasan lain. Jadi setelah obrolan kita di kafe ini selesai, tetap aku sendiri yang harus duduk berhadapan dengan Ibu di meja makan dan mencari cara menjawabnya."
            nar "Miyuki merapikan letak amplop itu di samping cangkir tehnya. Ia menghargai niatmu melindunginya, meskipun ia tahu tekanan di rumahnya tidak bisa dihentikan hanya dengan meminta waktu dari luar."
        else:
            yutaka "Kalau Senpai memang belum siap dan nggak sreg, minta aja mereka kasih ruang dan tunda semuanya dulu. Senpai kan lagi sibuk-sibuknya ngejar kuliah sama praktik rumah sakit, mana bisa dipaksa ngurusin omiai sekarang."
            nar "Miyuki tersenyum tipis yang hangat mendengar pembelaanmu, tetapi ia segera menggeleng pelan."
            miyuki "Terima kasih ya sudah langsung membela aku, Yutaka-kun. Rasanya hangat dengar kamu ngomong begitu."
            yutaka "Habisnya dari raut muka Senpai tadi sudah kelihatan jelas kalau Senpai tertekan."
            miyuki "Aku memang tertekan. Cuma... orang tuaku itu sifatnya agak beda kalau menghadapi penolakan langsung. Kalau aku minta mereka mundur atau membatalkan makan malam ini dari luar, Ibu bakal langsung menyelidiki siapa teman di kampus yang bikin aku berani menolak."
            yutaka "Terus mereka malah makin menekan Senpai?"
            miyuki "Iya. Biasanya mereka justru bakal langsung mempercepat jadwal pertemuan berikutnya supaya aku nggak sempat berubah pikiran lagi. Pada akhirnya, setelah kita pisah di lobi ini nanti, tetap aku sendiri yang harus duduk di ruang makan rumah dan menghadapi pertanyaan mereka."
            nar "Miyuki menyimpan amplop krem itu ke sela bukunya dengan tenang, menghargai kepedulianmu sembari menyadarkanmu betapa rapatnya kendali keluarga Tachibana atas jadwal hidupnya."
    else:
        if kk_host == "chiasa":
            chiasa "Menurutku sih, Tachibana-senpai, makan malam perkenalan kayak begini baru masuk akal buat didatangi kalau dari awal Senpai beneran dikasih hak buat bilang nggak mau, tanpa harus takut dicap sebagai anak yang nggak tahu terima kasih."
            nar "Jari-jari Miyuki yang sejak tadi merapikan tepi amplop langsung berhenti. Ia menatap amplop krem di tangannya selama beberapa detik, lalu mengembuskan napas panjang yang membuat bahunya turun lega."
            miyuki "...Kamu tahu nggak, Chiasa-chan? Dari tadi siang sejak amplop ini sampai ke tanganku, aku pengin banget dengar ada satu orang aja yang ngomong persis kayak kalimatmu barusan."
            chiasa "Memangnya orang-orang di sekitar Senpai komentarnya gimana waktu tahu soal Hayase-san?"
            miyuki "Semuanya kompak bilang hal yang sama. 'Takeru itu dokter bedah yang sopan, keluarganya terpandang, kamu beruntung sekali orang tuamu mencarikan calon sebaik itu, jangan sampai bikin mereka kecewa.' Nggak ada satu pun yang peduli apakah aku sendiri menginginkan perjodohan ini atau nggak."
            chiasa "Sebaik apa pun orangnya, kalau Senpai nggak mau ya Senpai nggak wajib bilang iya."
            nar "Senyum yang benar-benar tulus dan lepas akhirnya muncul di wajah Miyuki."
            miyuki "Terima kasih banyak ya, Chiasa-chan. Aku memang masih harus mikirin gimana cara bicara ke Ibu malam ini, tapi tahu bahwa kamu bisa membedakan antara kepatuhanku sebagai anak dengan keinginanku sendiri itu sudah bikin aku jauh lebih kuat. Ayo, Senpai traktir teh hangat sama kue dulu sebelum kita pulang."
        else:
            yutaka "Terus terang aja ya, Tachibana-senpai. Pertemuan perjodohan macam ini cuma layak dijalani kalau dari awal Senpai punya kebebasan penuh buat menolak kapan pun, tanpa harus dituduh sebagai anak yang nggak tahu balas budi sama orang tua."
            nar "Tangan Miyuki yang sedang memegang pinggiran amplop langsung terhenti. Ia menatap cetakan nama keluarganya di atas kertas itu sejenak, lalu menghela napas panjang yang sejak tadi ia tahan."
            miyuki "...Dari tadi siang waktu kurir Ibu mengantar amplop ini, aku berharap banget ada seseorang yang mengucapkan kalimat itu kepadaku, Yutaka-kun."
            yutaka "Memangnya yang lain pada bilang apa ke Senpai?"
            miyuki "Setiap orang yang kenal keluarga kami selalu bilang, 'Hayase Takeru itu residen bedah yang mapan, sopan, dan sabar, kurang apa lagi? Jangan sampai mengecewakan orang tuamu.' Seolah-olah karena dia orang baik di atas kertas, maka aku otomatis berkewajiban menyukainya."
            yutaka "Orang baik sekalipun nggak bikin Senpai punya utang buat menyerahkan masa depan Senpai begitu aja."
            nar "Senyum hangat yang tidak lagi kaku akhirnya mengembang di bibir Miyuki."
            miyuki "Terima kasih ya, Yutaka-kun. Aku memang belum memutuskan kalimat apa yang akan kupakai untuk menjawab Ibu nanti malam, tapi tahu ada kamu yang tidak menyamakan sikap patuhku dengan kemauanku sendiri itu rasanya melegakan sekali. Ayo pesan kopi atau teh hangat dulu, malam ini biar Senpai yang traktir."
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
        nar "Koridor lantai atas menuju aula serbaguna Rumah Sakit Tachibana malam itu dihiasi karangan daun pinus dan pita merah keemasan. Dari balik pintu ganda kayu mahoni yang masih tertutup rapat, terdengar alunan kuartet gesek, denting gelas kaca, serta suara perbincangan para dokter kepala dan tamu kehormatan yang berulang kali menyebut nama keluarga Tachibana dengan penuh pujian."
        nar "Beberapa langkah dari pintu masuk aula, Miyuki berdiri seorang diri di dekat pilar marmer. Ia mengenakan gaun malam biru tua selutut yang rapi dengan rambut hitam panjangnya yang disisir lurus berkilau. Jari-jari tangan kanannya yang dingin terus-menerus memutar pengait gelang perak di pergelangan tangan kirinya, padahal ukuran gelang itu sama sekali tidak longgar."
        chiasa "Tachibana-senpai belum masuk ke dalam? Musik pembukanya sudah mulai dari tadi kan?"
        nar "Miyuki menghentikan gerakan jarinya di atas gelang, lalu menoleh ke arahmu sambil mengembuskan napas perlahan."
        miyuki "Sudah mulai sepuluh menit lalu, Chiasa-chan. Tadi Ibu juga sudah kirim pesan menyuruhku cepat masuk ke meja utama."
        chiasa "Kenapa berdiri di luar sini terus, Senpai? Di koridor kan angin dari tangga daruratnya dingin."
        miyuki "Soalnya aku sudah hafal mati apa yang bakal terjadi begitu aku mendorong pintu itu nanti. Tiga menit pertama koleganya Ayah bakal tanya soal nilai ujianku di Fakultas Kedokteran, lima menit berikutnya tanya kapan aku mulai masuk rotasi klinik, lalu ujung-ujungnya Ibu bakal langsung menyuruhku duduk di sebelah Hayase Takeru."
        chiasa "Hayase-san datang sama keluarganya juga malam ini, Senpai?"
        miyuki "Iya, meja keluarga Hayase digabung langsung sama meja orang tuaku di barisan paling depan. Kadang aku sampai mikir lebih baik mereka langsung saja bicara soal Takeru begitu aku masuk pintu, supaya aku nggak usah pegal tersenyum setengah jam buat basa-basi pembukanya."
        nar "Ia menatapmu di bawah lampu dinding koridor, lalu menarik senyum tipis yang tampak sedikit dipaksakan."
        miyuki "Tapi kamu mau datang malam ini buat menemaniku sebagai teman saja sudah bikin aku tenang kok, Chiasa-chan. Aku cuma pengin ada satu orang di gedung ini yang tahu kalau aku sebenarnya gugup, sebelum semua orang di dalam sana melihatku tersenyum rapi seperti biasa."
    else:
        nar "Koridor lantai atas menuju aula serbaguna Rumah Sakit Tachibana dihiasi untaian daun pinus dan pita merah keemasan. Dari balik pintu ganda kayu mahoni yang masih tertutup rapat, terdengar alunan musik gesek, denting gelas kaca, serta suara obrolan para dokter senior dan tamu undangan yang beberapa kali menyebut nama Miyuki dengan nada memuji."
        nar "Beberapa langkah di samping pintu aula, Miyuki berdiri seorang diri di dekat pilar marmer. Ia mengenakan gaun malam biru tua selutut dengan rambut hitam panjang yang tersisir lurus rapi. Jemari tangan kanannya yang dingin terus saja memutar pengait gelang perak di pergelangan kirinya, padahal gelang itu terpasang pas dan sama sekali tidak longgar."
        yutaka "Tachibana-senpai belum masuk ke aula? Kedengarannya acara di dalam sudah jalan dari tadi."
        nar "Miyuki menghentikan jarinya dari gelang perak itu lalu menoleh ke arahmu sambil mengembuskan napas pelan."
        miyuki "Sudah mulai sepuluh menit yang lalu, Yutaka-kun. Tadi Ibu juga sudah kirim pesan menyuruhku langsung bergabung ke meja depan."
        yutaka "Kenapa masih berdiri di luar koridor begini, Senpai? Di dekat sini angin dari tangga daruratnya lumayan dingin lho."
        miyuki "Soalnya aku sudah hafal persis skenario yang menungguku begitu pintu itu dibuka. Tiga menit pertama kolega Ayah bakal menanyakan nilai kuliah Kedokteran, lima menit berikutnya soal rencana rotasi klinik, lalu ujung-ujungnya Ibu bakal langsung mengarahkanku duduk di sebelah Hayase Takeru."
        yutaka "Hayase-san datang sama orang tuanya juga hari ini?"
        miyuki "Iya, meja keluarga Hayase dijadikan satu sama meja Ayah dan Ibu di barisan paling depan. Kadang aku sampai berharap mereka langsung saja membicarakan soal Takeru begitu aku masuk, biar aku nggak perlu capek tersenyum setengah jam buat basa-basi pembukanya."
        nar "Ia mengangkat wajah menatapmu di bawah lampu dinding koridor, lalu menarik senyum tipis yang agak lelah."
        miyuki "Tapi kamu mau datang sebagai teman saja sudah sangat membantu kok, Yutaka-kun. Aku cuma ingin ada satu orang di gedung ini yang tahu kalau aku sebenarnya gugup, sebelum semua orang di dalam sana melihatku tersenyum rapi seperti biasa."
    call kk_family_menu("Mi09", ["\"Ayo masuk bareng. Aku temani di dalam supaya Senpai nggak sendirian.\"", "\"Kalau mereka terus mendesak soal Hayase-san, kenalkan saja aku sebagai pasangan Senpai.\"", "\"Aku antar sampai depan aula sini saja ya. Semoga acaranya lancar.\""])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Ayo kita masuk bareng sekarang, Tachibana-senpai. Aku temani Senpai di dalam supaya Senpai nggak harus menghadapi meja mereka sendirian."
            nar "Miyuki menatapmu sejenak, lalu mengangguk pelan. Ia merapikan sisi gaunnya, mendorong pintu kayu aula, dan melangkah masuk bersamamu ke bawah terangnya lampu gantung kristal."
            nar "Baru saja kalian mengambil dua gelas jus apel dingin dari meja jamuan tepi ruangan, ibu Miyuki, Tachibana Sayuri, melangkah anggun menghampiri kalian. Senyum seorang direktur rumah sakit terpasang rapi di wajahnya, tetapi matanya langsung memberi isyarat ke arah meja bundar di bagian depan tempat ayah Miyuki dan keluarga Hayase sedang berbincang."
            "Ibu Miyuki" "Akhirnya kamu masuk juga, Miyuki. Dari tadi Ibu cari di dekat pintu. Takeru-kun baru saja menanyakanmu, dan orang tuanya ingin membahas jadwal makan malam keluarga minggu depan. Ayo ke meja depan sekarang, kursi di sebelah Takeru-kun sudah Ibu kosongkan."
            nar "Biasanya Miyuki akan langsung mengangguk patuh dan mengikuti langkah ibunya. Malam ini, ia melirik ke arahmu yang berdiri tepat setengah langkah di sampingnya. Mengingat percakapan jujur kalian di luar koridor tadi, Miyuki tetap berdiri tenang di tempatnya."
            miyuki "Maaf, Bu. Soal jadwal makan malam dengan keluarga Hayase minggu depan itu, aku belum mengiyakan apa-apa karena jadwal kuliahku belum kupastikan. Lagipula malam ini aku mengundang temanku dari kampus, jadi aku ingin mengenalkan Chiasa-chan ke Ibu dulu."
            chiasa "Selamat malam, Bibi. Saya Amamiya Chiasa, adik tingkat Tachibana-senpai di universitas."
            nar "Suara Miyuki terdengar sangat sopan dan lembut, tidak ada satu kata pun yang terdengar membangkang di depan tamu lain. Meski begitu, senyum di bibir ibunya sempat menegang selama dua detik penuh karena tidak terbiasa melihat putrinya menunda perintah secara langsung."
            "Ibu Miyuki" "...Begitu ya. Selamat malam, Amamiya-san, terima kasih sudah datang ke acara rumah sakit kami. Kalau begitu temani tamumu mengambil hidangan dulu lima belas menit, Miyuki. Setelah itu baru mampir menyapa keluarga Hayase."
            miyuki "Baik, Bu. Terima kasih."
            nar "Begitu ibunya berbalik kembali menuju meja utama, Miyuki mengembuskan napas panjang yang sejak tadi ia tahan, lalu berbisik pelan kepadamu sambil mengambil piring kue kecil."
            miyuki "Jantungku rasanya mau copot barusan, Chiasa-chan. Tapi ternyata bilang belum memutuskan di depan Ibu nggak seseram yang kubayangkan waktu ada kamu di sebelahku."
        else:
            yutaka "Ayo masuk bareng sekarang, Tachibana-senpai. Aku temani di dalam supaya Senpai nggak perlu menghadapi meja depan itu sendirian."
            nar "Miyuki menatapmu sebentar, lalu mengangguk mantap. Ia merapikan lipatan gaunnya, mendorong daun pintu mahoni, dan berjalan masuk bersamamu ke dalam aula yang terang oleh deretan lampu gantung kristal."
            nar "Baru saja kalian mengambil dua gelas minuman dingin dari meja hidangan tepi ruangan, Tachibana Sayuri berjalan menghampiri dengan senyum anggun seorang direktur rumah sakit. Tatapannya sekilas menilai kehadiranmu, lalu segera mengarah ke meja bundar utama tempat ayah Miyuki dan keluarga Hayase duduk."
            "Ibu Miyuki" "Akhirnya kamu masuk juga, Miyuki. Takeru-kun baru saja menanyakanmu, dan orang tuanya ingin memastikan jadwal makan malam keluarga minggu depan. Ayo langsung ke meja depan, kursi di sebelah Takeru-kun sudah Ibu siapkan."
            nar "Dalam keadaan biasa, Miyuki nyaris selalu langsung mengangguk dan mengikuti arah ibunya. Kali ini ia melirik sekilas kepadamu di sisinya, teringat percakapan jujur di luar pintu tadi, lalu menjawab dengan suara tetap lembut tanpa bergeser selangkah pun."
            miyuki "Maaf, Bu. Soal rencana makan malam dengan keluarga Hayase minggu depan, aku belum memutuskan apa-apa karena masih perlu memeriksa jadwal kuliahku dulu. Lagipula hari ini aku datang bersama temanku dari kampus, jadi aku ingin mengenalkan Yutaka-kun kepada Ibu lebih dulu."
            yutaka "Selamat malam, Bibi. Saya Kisaragi Yutaka, adik tingkat Tachibana-senpai di universitas."
            nar "Tidak ada sedikit pun nada membantah dalam ucapan Miyuki. Meski begitu, senyum sopan Sayuri sempat menegang selama dua detik mendengar penolakan halus putrinya sekaligus menangkap nama marga Kisaragi yang baru kamu sebutkan."
            "Ibu Miyuki" "...Oh, Kisaragi-san. Selamat malam, terima kasih sudah berkenan hadir di acara rumah sakit kami. Kalau begitu temani tamumu mencicipi hidangan dulu lima belas menit ya, Miyuki. Setelah itu baru mampir menyapa keluarga Hayase di depan."
            miyuki "Baik, Bu. Terima kasih."
            nar "Begitu Sayuri berbalik menuju meja utama, Miyuki mengembuskan napas panjang yang sejak tadi tertahan, lalu tersenyum kecil sambil mengambil piring kue di sampingmu."
            miyuki "Tanganku masih agak gemetar barusan, Yutaka-kun. Tapi ternyata bilang belum memutuskan di depan Ibu nggak seseram bayanganku selama ada kamu berdiri di sebelahku."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Tachibana-senpai, kalau Senpai memang keberatan terus-terusan didorong ke Hayase-san, gimana kalau malam ini Senpai kenalkan aja aku ke orang tua Senpai sebagai pasangan Senpai?"
            nar "Miyuki langsung tertegun. Jari-jarinya berhenti menyentuh gelang peraknya, dan mata biru safirnya menatapmu lekat-lekat untuk mencari tahu apakah kamu sedang bergurau."
            miyuki "Chiasa-chan... kamu sadar kan apa artinya kalau aku ngomong begitu di dalam aula sana? Orang tuaku itu bukan tipe yang bakal lupa besok pagi. Kalau malam ini kita berpura-pura punya hubungan khusus, bulan depan dan tahun depan kita harus terus kompak menjaga cerita bohong yang sama di depan mereka."
            chiasa "Aku paham kok risikonya, Senpai. Kalau sekadar bicara sopan sebagai teman biasa, Ibu Senpai pasti tetap bakal nyuruh Senpai duduk sama Hayase-san lima menit kemudian. Pakai aja namaku malam ini."
            nar "Miyuki menatap daun pintu mahoni di samping kalian, lalu kembali menatap wajahmu yang tenang. Keraguan di wajahnya perlahan berganti menjadi tekad seseorang yang akhirnya diberikan pintu keluar. Ia mengulurkan tangannya dan menggenggam lenganmu."
            miyuki "...Kalau begitu, waktu kita berdiri di depan meja Ayah dan Ibu nanti, tolong jangan lepaskan lenganmu dari tanganku ya, Chiasa-chan."
            chiasa "Iya, nggak bakal kulepas. Ayo masuk, Senpai."
            nar "Kalian mendorong pintu aula dan berjalan lurus menghampiri meja bundar utama sebelum ibunya sempat memanggil dari jauh. Begitu Tachibana Sayuri, suaminya Kazuhiro, serta Hayase Takeru menoleh menyambut kedatangan Miyuki, jemari Miyuki mencengkeram lenganmu sedikit lebih erat."
            "Ibu Miyuki" "Nah, Miyuki, kebetulan kamu langsung ke meja utama. Takeru-kun baru saja—"
            miyuki "Ayah, Ibu, dan Hayase-san juga... maaf aku harus memotong sebelum pembicaraannya berjalan lebih jauh. Aku tidak bisa melanjutkan rencana pertemuan omiai keluarga kita, karena saat ini aku sudah menjalin hubungan serius dengan Chiasa."
            nar "Suara percakapan di meja bundar utama itu langsung terputus total. Ayah Miyuki menurunkan garpunya, ibunya terdiam kaku dengan bibir sedikit terbuka, sementara Hayase Takeru yang baru hendak berdiri menarik kursi untuk Miyuki membeku di tempatnya."
            "Takeru" "...Dengan Amamiya-san? Begitu ya... saya sama sekali belum mendengar soal itu."
            chiasa "Maaf kami baru sempat menyampaikannya malam ini ke Paman, Bibi, dan Hayase-san."
            nar "Di tengah tatapan terkejut kedua orang tuanya yang tidak bisa membuat keributan di hadapan tamu rumah sakit, Miyuki mengajakmu bergeser ke meja jamuan samping dengan langkah yang akhirnya terasa bebas dari kursi yang sudah mereka siapkan."
        else:
            yutaka "Tachibana-senpai, kalau kamu memang sudah capek terus-terusan diarahkan ke Hayase-san, gimana kalau malam ini kamu kenalkan saja aku ke orang tuamu sebagai pasanganmu?"
            nar "Miyuki langsung terdiam. Tangannya turun dari pergelangan gelang perak itu, sementara mata biru safirnya menatapmu tajam untuk mengecek apakah kamu sedang melontarkan gurauan."
            miyuki "Yutaka-kun... kamu paham kan konsekuensinya kalau aku mengatakan itu di dalam aula? Ayah dan Ibuku bukan tipe orang tua yang bakal melupakan satu nama begitu saja. Kalau nanti mereka bertanya lagi bulan depan atau tahun depan, kita berdua harus terus mengingat kebohongan yang sama."
            yutaka "Aku paham kok risikonya, Senpai. Tapi kalau kita masuk cuma sebagai teman kuliah biasa, lima menit lagi Ibumu pasti tetap menarikmu duduk di sebelah Hayase-san. Pakai aja namaku malam ini."
            nar "Miyuki menatap daun pintu kayu mahoni yang tertutup, lalu kembali menatap wajahmu yang tidak bergeming. Setelah satu tarikan napas pendek, ia melangkah mendekat dan melingkarkan jemarinya ke lengan mantelmu."
            miyuki "...Kalau begitu, waktu kita berhadapan dengan Ayah, Ibu, dan Takeru di meja depan nanti, tolong jangan melepaskan peganganku duluan ya, Yutaka-kun."
            yutaka "Aman, nggak bakal kulepas. Ayo masuk, Senpai."
            nar "Kalian mendorong pintu aula dan berjalan langsung menuju meja bundar utama sebelum Sayuri sempat memanggil dari jauh. Begitu Tachibana Sayuri, Kazuhiro, dan Hayase Takeru menoleh menyambut, jemari Miyuki mencengkeram kain lenganmu jauh lebih erat daripada sebelumnya."
            "Ibu Miyuki" "Nah, Miyuki, pas sekali kamu langsung ke meja utama. Takeru-kun baru saja menanyakan jadwal—"
            miyuki "Ayah, Ibu, dan juga Hayase-san... maaf aku memotong pembicaraannya di sini. Aku tidak bisa melanjutkan rencana omiai keluarga kita, karena saat ini aku sudah berpacaran serius dengan Kisaragi Yutaka."
            nar "Obrolan di meja utama seketika terhenti. Kazuhiro meletakkan garpunya dengan bunyi denting pendek, sementara Sayuri menatapmu dari atas ke bawah dengan kening berkerut kaget karena tidak menyangka nama Kisaragi muncul di situ. Hayase Takeru, yang baru berdiri separuh untuk menarik kursi di sebelahnya, membeku di tempat."
            "Takeru" "...Dengan Kisaragi-san? Begitu ya. Maaf, saya memang belum pernah mendengar kabar ini sebelumnya."
            yutaka "Maaf kami baru sempat menyampaikannya langsung malam ini kepada Paman, Bibi, dan Hayase-san."
            nar "Di bawah tatapan kaget kedua orang tuanya yang tidak mungkin membuat keributan di tengah tamu rumah sakit, Miyuki menuntun langkahmu menjauh menuju meja jamuan samping. Untuk malam ini, seluruh susunan rencana tentang Takeru di meja utama akhirnya kehilangan arah."
    else:
        if kk_host == "chiasa":
            chiasa "Maaf ya, Tachibana-senpai. Aku cuma bisa ngantar Senpai sampai depan koridor aula sini aja malam ini, soalnya aku masih harus balik karena ada urusan lain. Semoga acara jamuannya di dalam lancar ya."
            nar "Jemari Miyuki yang tadinya sempat terangkat sedikit di samping gaunnya seperti hendak memegang ujung lengan mantelmu perlahan diturunkan kembali. Dalam waktu singkat, ekspresi cemas yang tadi ia perlihatkan di depanmu langsung lenyap, berganti dengan postur tegak dan senyum senior yang rapi."
            miyuki "Oh... begitu ya, kamu masih ada urusan lain malam ini. Tidak apa-apa kok, Chiasa-chan. Kamu sudah mau mampir mengantar aku sampai depan aula ini saja Senpai sudah senang."
            chiasa "Kalau nanti acaranya sudah selesai, hati-hati pulang ke apartemennya ya, Senpai. Selamat Natal."
            miyuki "Iya, terima kasih banyak. Selamat Natal juga, Chiasa-chan. Hati-hati di jalan, di luar anginnya dingin."
            nar "Miyuki tetap berdiri tenang di samping pintu mahoni itu tanpa menyentuh gagangnya, menunggu dengan sopan sampai kamu berbalik dan berjalan menuju lorong lift di ujung koridor."
            nar "Tepat sebelum pintu lift tertutup, kamu melihat Miyuki akhirnya menarik napas pendek dan mendorong pintu aula seorang diri. Dari celah pintu yang terbuka, langsung terdengar suara ramah ibunya yang memanggil Miyuki untuk segera duduk di kursi kosong sebelah Hayase Takeru."
        else:
            yutaka "Maaf ya, Tachibana-senpai. Aku cuma bisa ngantar sampai depan aula sini aja, habis ini aku masih harus balik karena ada urusan lain. Semoga acaranya lancar di dalam."
            nar "Tangan Miyuki yang tadinya sempat sedikit terangkat di samping gaunnya seolah hendak meraih lenganmu langsung turun kembali. Seketika raut gugup yang ia perlihatkan di koridor tadi merapat tertutup oleh postur tegak dan senyum senior yang sopan."
            miyuki "Oh... begitu ya, kamu masih ada urusan lain. Tidak apa-apa kok, Yutaka-kun. Terima kasih sudah mengantar sampai sini, aku bisa masuk sendiri."
            yutaka "Nanti kalau acaranya sudah selesai, hati-hati pulang ke apartemennya ya, Senpai. Selamat Natal."
            miyuki "Iya, terima kasih banyak. Selamat Natal juga, Yutaka-kun. Hati-hati di jalan pulang."
            nar "Miyuki tetap berdiri di depan pintu kayu mahoni tanpa membuka gagangnya, menunggu sampai kamu berbalik dan melangkah menjauh ke arah lift di ujung koridor."
            nar "Tepat sebelum pintu lift menutup, kamu melihat Miyuki menarik napas pendek lalu mendorong pintu aula sendirian. Dari celah pintu yang terbuka, langsung terdengar sambutan ramah ibunya yang memanggil Miyuki untuk duduk di kursi kosong sebelah Hayase Takeru."
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
