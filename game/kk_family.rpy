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
            crime = kk_has("force_pernah")
        if bond >= 60 and not crime:
            return "E-YH-03"
        return None

    def kk_miyuki_sham_ending(palsu=None, diakui=None, terbongkar=None):
        # Alur_Cabang/01: pasangan palsu (Mi09-B). Diakui jujur di Mi18-C -> E-MI-13;
        # terbongkar oleh Takeru/orang tua (Mi18 selain C) -> E-MI-14.
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
                else:
                    kk_flag("sandiwara_terbongkar")
            kk_adj("omiai_takeru",5 if key == "A" else -5)
        elif eid == "Mi25":
            kk_flag({"A":"hayase_engaged","B":"hayase_interrupted","C":"left_with_miyuki"}[key])
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
        if kk_has("nagisa_family_visit"):
            return "E-NA-07"
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
        if kk_has("left_with_miyuki"):
            return "E-MI-05"
        if kk_has("hayase_engaged"):
            return "E-MI-04"
        sham = kk_miyuki_sham_ending()
        if sham:
            return sham
        if (stage.get("miyuki",0) <= 3 and kk_rel_get("miyuki","aff") >= 55 and
                kk_rel_get("miyuki","trust") >= 55 and kk_get("sena_curiga") < 60):
            return "E-MI-01"
        return None

label kkscene_Mi07:
    call kk_scene_enter("miyuki","Rumah Sakit Tachibana")
    miyuki "Orang tuaku mengundang Takeru lagi. Aku tahu apa maksud mereka."
    call kk_family_menu("Mi07", ["Dengarkan apa yang Takeru tawarkan.", "Minta mereka memberi Miyuki ruang.", "Katakan terus terang apa yang kaupikir."])
    if _return == "C":
        miyuki "Setidaknya aku tahu apa yang sebenarnya kaupikirkan."
    else:
        nar "Miyuki mengulang kata-katamu pelan sebelum kembali ke keluarganya."
    return

label kkscene_Mi09:
    call kk_scene_enter("miyuki","Pesta rumah sakit")
    miyuki "Keluargaku sudah di dalam. Aku sedikit gugup."
    call kk_family_menu("Mi09", ["Temani dia masuk.", "Tawarkan berpura-pura menjadi pasangannya.", "Pamit sebelum pesta dimulai."])
    if _return == "B":
        miyuki "Kalau mereka bertanya lagi nanti, apa yang akan kita katakan?"
    return

label kkscene_Mi18:
    call kk_scene_enter("miyuki","Pertemuan keluarga")
    miyuki "Hayase datang bersama keluarganya. Mereka ingin mendengar jawabanku."
    if kk_has("pasangan_palsu"):
        miyuki "Mereka masih ingat kita datang bersama tahun lalu."
    call kk_family_menu("Mi18", ["Tetap hadir di pertemuan itu.", "Minta mereka menunda pembicaraan.", "Bicarakan dengan jujur alternatif yang kalian punya."])
    if kk_has("sandiwara_diakui"):
        miyuki "Kalau begitu kita ceritakan dari awal. Termasuk bagian saat kita berpura-pura."
    return

label kkscene_Mi25:
    call kk_scene_enter("miyuki","Natal · Keluarga Tachibana")
    nar "Takeru menunggu. Untuk sesaat Miyuki hanya memandang tangannya sendiri."
    miyuki "Kalau aku mengambil langkah ini, semuanya akan berubah."
    call kk_family_menu("Mi25", ["Beri Miyuki dukungan untuk menerima.", "Minta Takeru berhenti mendesaknya.", "Tawarkan pergi bersama, jika ia menginginkannya."])
    if _return == "C":
        miyuki "Kalau begitu, ayo."
    return

label kkscene_N22:
    call kk_scene_enter("nagisa","Rumah Sakurajima")
    nagisa "Orang tuaku ada di rumah. Kalau mau masuk, sekarang."
    call kk_family_menu("N22", ["Masuk dan sapa keluarganya.", "Berterima kasih lalu pamit."])
    if _return == "A":
        nagisa "Tunggu sini. Aku panggil mereka."
    return

label kkscene_Y17:
    call kk_scene_enter("yutaka","Apartemen Yutaka")
    nar "Perusahaan keluarga mengharapkan jawabanmu. Masih ada lamaran lain di meja."
    call kk_family_menu("Y17", ["Jawab tawaran perusahaan keluarga.", "Kirim lamaran kerja ke perusahaan lain.", "Daftar untuk magang di luar negeri."])
    nar "Kau mengirim jawabanmu."
    return

label kk_family_menu(eid, captions):
    $ _rows = [(caption, Return(key), False) for key,caption in zip("ABC",captions)]
    call screen kk_choice_panel(_rows, "Apa yang kau lakukan?")
    $ _decision = _return
    $ kk_family_choice(eid, _decision)
    return _decision


# Draft editorial. Event_Yutaka Y09/Y13; Alur_Cabang/08 Y-D03 dan Y-D08.
label kk_visit_kisaragi:
    if not kk_father_visit("Apartemen Yutaka"):
        return
    call kk_scene_enter("yutaka", "Lobi apartemen")
    nar "Ayahmu sedang menunggu di lobi. Kau baru melihatnya setelah pintu lift menutup di belakangmu."
    call kk_family_menu("Y-D03", ["Sambut ayahmu.", "Lewati lobi tanpa menghampirinya.", "Duduk dan ajak ia bicara serius."])
    if _return == "B":
        nar "Kau naik sendiri. Percakapan itu belum terjadi."
    elif _return == "C":
        nar "Ia menyimpan ponselnya. Kali ini kau punya perhatiannya."
    else:
        nar "Kau berhenti di sisinya. Ia menanyakan kabarmu."
    return

label kk_message_kisaragi:
    if not kk_mother_message():
        return
    nar "Nama Ibu muncul di layar ponsel. Ia hanya ingin tahu kabarmu. Sudah lama ia tidak bertanya seperti ini."
    call kk_family_menu("Y-D08", ["Ceritakan kabarmu dan tanyakan kabarnya.", "Balas singkat dengan sopan.", "Simpan ponsel tanpa membalas."])
    if _return == "A":
        nar "Untuk sekali ini percakapan kalian berlanjut setelah pertanyaan pertama."
    $ kk_minutes(1)
    return

label kkscene_Y09:
    call kk_scene_enter("yutaka", "Apartemen Yutaka")
    nar "Ayah menelepon. Setelah salam singkat, ia langsung menanyakan rencanamu sesudah lulus."
    call kk_family_menu("Y09", ["Jawab pertanyaannya dengan sopan.", "Katakan bahwa keputusan itu milikmu.", "Singgung keluarga Saionji."])
    if _return == "C":
        nar "Nama itu membuatnya berhenti sejenak. Sekarang ia meminta penjelasan."
    elif _return == "B":
        nar "Ia menunggu. Kau membiarkan jawabanmu tetap seperti tadi."
    else:
        nar "Ayah mendengarkan sampai kau selesai."
    return

label kkscene_Y13:
    call kk_scene_enter("yutaka", "Rumah Amamiya · Natal")
    nar "Daisuke dan Yoshie ternyata sudah pulang. Di meja makan masih ada tempat untukmu."
    call kk_family_menu("Y13", ["Tarik kursi dan makan bersama mereka.", "Pamit sebelum makan malam.", "Minta waktu untuk bicara dari hati ke hati."])
    if _return == "A":
        nar "Yoshie menggeser lauknya agar kau bisa ikut mengambil."
    elif _return == "C":
        nar "Daisuke meletakkan sumpitnya. Kau mulai bicara."
    else:
        nar "Kau mengucapkan selamat Natal dari pintu."
    return
