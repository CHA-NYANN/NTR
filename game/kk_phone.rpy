# Fitur HP — bantuan kecil dari Sistem: buka HP untuk melihat perkiraan lokasi
# 8 karakter penting pada waktu saat ini. Hanya membaca jadwal (kk_daily_place),
# tidak mengubah apa pun. Tampilan seragam (tanpa warna berbeda per-pilihan).

init python:
    KK_PHONE_ORDER = ("koita","miyuki","nagisa","harumi","moeka","shiori","chiasa","yutaka")

    def kk_phone_locate(cid):
        # Kembalikan (lokasi, distrik) sebagai teks untuk ditampilkan di HP.
        if cid == kk_host:
            return ("— tubuh yang kau tinggali —", "")
        p = kk_daily_place(cid)
        if not p:
            return ("Tak terlacak saat ini", "di luar jangkauan Sistem")
        dn = ""
        for did, dnama, locs in KK_DISTRICTS:
            if p in locs:
                dn = dnama
                break
        return (p, dn)


screen kk_phone_locator():
    modal True
    zorder 80
    key "game_menu" action Hide("kk_phone_locator")
    key "dismiss" action Hide("kk_phone_locator")
    add Solid("#101b24ee")
    frame:
        align (.5, .5) xysize (1000, 824) background Solid(kk_ink2) padding (48, 42)
        vbox:
            spacing 14
            text "HP · Pelacak Lokasi" style "kk_heading"
            text "Bantuan kecil dari Sistem: perkiraan posisi orang-orang penting saat ini." style "kk_caption" xmaximum 880
            $ _mt = kk_month_tuple()
            text (kk_hari + ", " + str(kk_hari_n) + " " + _mt[1] + " · " + KK_SLOTS[kk_slot]) style "kk_caption"
            null height 8
            viewport:
                mousewheel True draggable renpy.variant("touch") scrollbars "vertical"
                ysize 566
                vbox:
                    spacing 8
                    for cid in KK_PHONE_ORDER:
                        $ _meta = KK_CHARS[cid]
                        $ _loc, _dn = kk_phone_locate(cid)
                        frame:
                            background Solid(kk_panel) xysize (884, 86) padding (20, 10)
                            hbox:
                                yalign .5 spacing 18
                                add Solid(kk_line) xysize (6, 54) yalign .5
                                vbox:
                                    yalign .5 xsize 356
                                    text _meta["nama"] size 25 bold True
                                    text _meta["tag"] style "kk_caption"
                                vbox:
                                    yalign .5 xsize 420
                                    text _loc size 24 color kk_bone
                                    if _dn:
                                        text _dn style "kk_caption"
            null height 6
            use kk_link("Tutup", Hide("kk_phone_locator"), 884)
