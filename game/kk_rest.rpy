# Sistem_Waktu_Bebas_dan_Kondisi_Fisik §3.1. Kontak prioritas dipilih pemain.
default kk_phone_mode = "normal"
default kk_priority_contacts = []
default kk_rest_energy_minutes = 0
default kk_rest_debt_minutes = 0

label kk_rest_home:
    $ _sleep_rows = [(caption, Return(length), False) for caption,length in (("Pejamkan mata sebentar · 20 menit",20),("Pasang alarm · 90 menit",90),("Tidur enam jam",360),("Tidur delapan jam",480),("Tidur panjang · sepuluh jam",600))]
    $ _sleep_rows += [("Atur ponsel · " + kk_phone_mode.capitalize(), Return("phone"), False), ("Kembali", Return(None), False)]
    call screen kk_choice_panel(_sleep_rows, "Berapa lama kau ingin tidur?")
    if _return is None:
        return
    if _return == "phone":
        call kk_bedside_phone
        jump kk_rest_home
    $ _wake_contact = kk_sleep(_return)
    if _wake_contact:
        nar "Bunyi ponsel menarik perhatianmu."
        $ _wake_scene = next(label for cid, eid, label in kk_incoming_messages() if cid == _wake_contact)
        call expression _wake_scene
    else:
        nar "Kau membuka mata di kamarmu."
    return

label kk_bedside_phone:
    $ _modes = [("Senyap · biarkan aku tidur", Return("senyap"), kk_phone_mode == "senyap"), ("Normal · bangunkan untuk kontak prioritas", Return("normal"), kk_phone_mode == "normal"), ("Siaga · bunyikan semua pesan", Return("siaga"), kk_phone_mode == "siaga"), ("Pilih kontak prioritas", Return("contacts"), False), ("Kembali", Return(None), False)]
    call screen kk_choice_panel(_modes, "Ponsel di samping tempat tidur")
    if _return is None:
        return
    if _return == "contacts":
        call kk_bedside_contacts
        jump kk_bedside_phone
    $ kk_phone_mode = _return
    return

label kk_bedside_contacts:
    $ _people = [(KK_CHARS[cid]["nama"], Return(cid), cid in kk_priority_contacts) for cid in KK_CHARS if cid != kk_host and cid in kk_last_met]
    if kk_host == "yutaka":
        $ _people.append(("Ibu", Return("ibu_kisaragi"), "ibu_kisaragi" in kk_priority_contacts))
    if kk_host == "chiasa" and kk_done("C05"):
        $ _people.append(("Mio", Return("mio"), "mio" in kk_priority_contacts))
    $ _people.append(("Kembali", Return(None), False))
    call screen kk_choice_panel(_people, "Kontak yang boleh membangunkanmu")
    if _return is None:
        return
    if _return in kk_priority_contacts:
        $ kk_priority_contacts.remove(_return)
    else:
        $ kk_priority_contacts.append(_return)
    jump kk_bedside_contacts

