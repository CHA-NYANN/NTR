# Draft editorial. Event_Miyuki, Event_Nagisa, Event_Yutaka dan Alur_Cabang/01,02,08,13.
# Adegan keluarga memakai aksi dari katalog. Mesin hanya meresolusi kondisi
# yang memiliki sumber state, sehingga epilog yang belum terhubung tidak direka.
init python:
    def kk_family_choice(eid, key):
        if not kk_record_choice(eid, key):
            return
        if eid == "Mi07":
            kk_adj("omiai_takeru", {"A":5,"B":-5,"C":0}[key])
            if key == "C":
                kk_rel("miyuki","trust",5)
        elif eid == "Mi09":
            if key == "B":
                kk_flag("pasangan_palsu")
                kk_adj("omiai_takeru",-5)
            elif key == "A":
                kk_rel("miyuki","trust",5)
            else:
                kk_adj("omiai_takeru",5)
        elif eid == "Mi18":
            if key == "C" and kk_has("pasangan_palsu"):
                kk_flag("sandiwara_diakui")
            kk_adj("omiai_takeru",5 if key == "A" else -5)
        elif eid == "Mi25":
            kk_flag({"A":"hayase_engaged","B":"hayase_interrupted","C":"left_with_miyuki"}[key])
        elif eid == "N22":
            kk_flag("nagisa_family_visit" if key == "A" else "nagisa_family_declined")
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
        return score

    def kk_miyuki_ending():
        if kk_has("lock_romance_miyuki"):
            return None
        if kk_has("left_with_miyuki"):
            return "E-MI-05"
        if kk_has("hayase_engaged"):
            return "E-MI-04"
        if kk_has("sandiwara_diakui"):
            return "E-MI-13"
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

