# Komponen UI Kouseikan. Kanvas logis 1920 × 1080.
screen kk_link(caption, operation, width=None, active=False, first=False):
    textbutton caption:
        style "kk_button"
        text_style "kk_button_text"
        action operation
        selected active
        default_focus first
        xsize width

screen kk_set(char, loc=""):
    zorder -10
    $ meta = KK_CHARS.get(char, {"nama": "Kouseikan", "warna": kk_accent})
    if loc.startswith(("Kampus Kouseikan", "Hanami Kampus")):
        add "gui/kk_evening.svg"
        add Solid("#18273488")
    else:
        add kk_ink2
        add Solid(meta["warna"] + "30") xpos 0.62 xsize 0.38 ysize 1.0
        add Solid(meta["warna"] + "55") pos (1190, 0) xysize (4, 1080)
        text meta["nama"] xpos kk_margin ypos 340 size 84 bold True color kk_bone
    frame:
        xpos kk_margin ypos 134 background Solid(kk_ink) padding (22, 14)
        vbox:
            spacing 6
            add Solid(meta["warna"]) xysize (52, 4)
            text loc size 24 xmaximum 1420

screen kk_titlecard(title, sub=""):
    modal True
    add kk_ink
    vbox:
        align (.5, .47) spacing kk_gap
        add Solid(kk_accent) xalign .5 xysize (72, 4)
        text title style "kk_heading" xalign .5
        if sub:
            text sub style "kk_caption" xalign .5
    button:
        xfill True yfill True background None
        action Return()
        text "Klik atau tekan Enter untuk lanjut" style "kk_caption" align (.5, .90)
    key "dismiss" action Return()

screen kk_hud():
    frame:
        xfill True ysize 86 padding (kk_margin, 12) background Solid(kk_ink)
        hbox:
            yalign .5 spacing kk_gap
            text "KOUSEIKAN" bold True size 24
            if kk_host:
                $ mt = kk_month_tuple()
                $ clock_text = kk_clock()
                text "[clock_text]   [kk_hari], [kk_hari_n] [mt[1]]   /   [KK_SLOTS[kk_slot]]" style "kk_caption"
                $ tier = kk_kelelahan_tier()
                if tier[1] >= 2:
                    text tier[0] color kk_warn size 22
        hbox:
            xalign 1.0 yalign .5 spacing 12
            if kk_host:
                use kk_link("Status", Show("kk_status"))
            use kk_link("Menu", ShowMenu("save"))

screen say(who, what):
    use kk_hud
    window:
        id "window"
        xpos kk_margin yalign .89 xsize 1512 yminimum 208
        background Solid("#15212af7") padding (46, 24, 64, 28)
        vbox:
            spacing 12
            if who:
                text who id "who" size 24 bold True color kk_accent
            else:
                add Solid(kk_accent) xysize (56, 4)
            text what id "what" size 34 line_spacing 6 color kk_bone
    use quick_menu

image kk_continue = Text("  ›", size=30, color=kk_accent)

screen quick_menu():
    if quick_menu:
        hbox:
            xpos kk_margin yalign .985 spacing 8
            use kk_link("Riwayat", ShowMenu("history"))
            use kk_link("Simpan", ShowMenu("save"))
            use kk_link("Muat", ShowMenu("load"))
            use kk_link("Otomatis", Preference("auto-forward", "toggle"), active=_preferences.afm_enable)
            use kk_link("Lewati", Skip())

default quick_menu = True

screen kk_choice_panel(rows, heading):
    add Solid(kk_ink)
    vbox:
        pos (kk_margin, 128) spacing kk_gap
        text heading style "kk_heading" xmaximum 1680
        viewport:
            xysize (1600, 700) mousewheel True draggable renpy.variant("touch") scrollbars "vertical"
            vbox:
                spacing 12
                for index, (caption, operation, chosen) in enumerate(rows):
                    use kk_link(caption, operation, 1500, chosen, index == 0)

screen choice(items):
    use kk_choice_panel([(i.caption, i.action, i.chosen) for i in items], "Pilihanmu")

screen kk_choices(ev):
    modal True
    use kk_choice_panel([(c["label"], Return(c["key"]), False) for c in ev["choices"]], ev["title"])

screen kk_route_select():
    add "gui/kk_evening.svg"
    add Solid("#13212bd9")
    vbox:
        xpos kk_margin yalign .48 spacing 30
        text "Pilih tubuh" style "kk_heading"
        hbox:
            spacing kk_gap
            for host, name, route, detail, tint in [("yutaka","Kisaragi Yutaka","Male Route","Sahabat Koita sejak kecil.","#93b6df"), ("chiasa","Amamiya Chiasa","Female Route","Adik tiri Koita.",kk_accent)]:
                button:
                    style "kk_button" xysize (780, 300) padding (36, 36)
                    action Return(host)
                    vbox:
                        spacing 18
                        add Solid(tint) xysize (68, 5)
                        text name size 46 bold True
                        text detail style "kk_caption"

screen kk_status():
    modal True
    zorder 80
    key "game_menu" action Hide("kk_status")
    add Solid("#101b24ee")
    frame:
        align (.5,.5) xysize (1660, 820) background Solid(kk_ink2) padding (54, 44)
        vbox:
            spacing 26
            text "Status & hubungan" style "kk_heading"
            hbox:
                spacing 72
                vbox:
                    xsize 440 spacing 14
                    $ tier = kk_kelelahan_tier()
                    text "Tubuh host" size 30 bold True
                    text ("Kelelahan · " + tier[0]) size 24
                    text ("Energi · " + kk_lvl(body.get("energi", 0))) size 24
                    text ("Kesehatan · " + kk_lvl(body.get("kesehatan", 0))) size 24
                    text ("Saldo · ¥" + "{:,}".format(saldo)) size 24
                    use kk_link("Riwayat transaksi", Show("kk_wallet"), 420)
                    null height 18
                    text "Pola pilihanmu" style "kk_caption"
                    text kk_persona_label() size 26
                viewport:
                    xysize (1000, 475) mousewheel True draggable renpy.variant("touch") scrollbars "vertical" arrowkeys True
                    vbox:
                        spacing 16
                        for cid in KK_CHARS:
                            if cid in rel:
                                text KK_CHARS[cid]["nama"] size 27 bold True color kk_bone
                                if cid in kk_last_met:
                                    $ days_since = kk_elapsed_days - kk_last_met[cid]
                                    text ("Terakhir berbincang hari ini." if days_since == 0 else "Terakhir berbincang {} hari lalu.".format(days_since)) style "kk_caption"
                                else:
                                    text "Belum ada percakapan yang tercatat." style "kk_caption"
            use kk_link("Tutup", Hide("kk_status"))

screen kk_wallet():
    modal True
    zorder 85
    default page = 0
    key "game_menu" action Hide("kk_wallet")
    add Solid("#101b24ee")
    frame:
        align (.5,.5) xysize (1500, 840) background Solid(kk_ink2) padding (54, 44)
        vbox:
            spacing 18
            text "Riwayat transaksi" style "kk_heading"
            text ("Saldo   ¥" + "{:,}".format(saldo)) size 30
            $ end = len(kk_transactions) - page * 7
            $ entries = kk_transactions[max(0, end-7):end]
            if not entries:
                text "Belum ada transaksi yang tercatat." style "kk_caption"
            for month, day, description, amount, balance in reversed(entries):
                hbox:
                    spacing 22
                    text ("{} {}".format(day, KK_BACKBONE[month-1][1])) style "kk_caption" xsize 220
                    text description size 26 xsize 490
                    text ("{}¥{:,}".format("+" if amount > 0 else "−", abs(amount))) size 26 xsize 220
                    text ("Saldo ¥{:,}".format(balance)) style "kk_caption"
            hbox:
                spacing 16
                if page > 0:
                    use kk_link("Lebih baru", SetScreenVariable("page", page - 1), 255)
                if end > 7:
                    use kk_link("Lebih lama", SetScreenVariable("page", page + 1), 255)
                use kk_link("Kembali ke status", Hide("kk_wallet"), 360)

screen kk_explorer():
    modal True
    default cur = "miyuki"
    key "game_menu" action Return("back")
    add kk_ink
    text "Jelajah cabang" style "kk_heading" pos (kk_margin, 64)
    vbox:
        pos (kk_margin, 176) spacing 8
        for rid, rnama, rsub in KK_ROUTES:
            $ ck = "koita" if rid == "koita_bl" else rid
            use kk_link(KK_CHARS[ck]["nama"], SetScreenVariable("cur", ck), 510, cur == ck)
        if "yutaka" in KK_EV_BY_CHAR:
            use kk_link("Kisaragi Yutaka", SetScreenVariable("cur", "yutaka"), 510, cur == "yutaka")
    viewport:
        pos (650, 176) xysize (1160, 740) mousewheel True draggable renpy.variant("touch") scrollbars "vertical"
        vbox:
            spacing 8
            for event in KK_EV_BY_CHAR.get(cur, []):
                use kk_link("{}   /   {}     {}".format(event["id"], event["month"], event["title"]), Return(event["id"]), 1090)
    textbutton "‹ Kembali" style "kk_button" action Return("back") pos (kk_margin, 956)

screen kk_ending_detail(entry, diagnostics=False):
    vbox:
        spacing 20
        if diagnostics:
            text (entry["type"].upper() + "   /   " + entry["code"]) size 23 color kk_accent
        text entry["name"] size 44 bold True
        text entry.get("body", "") size 28 line_spacing 6
        null height 8
        if diagnostics:
            text "Syarat" style "kk_caption"
            text entry.get("cond", "") size 24 line_spacing 5

screen kk_ending_card(e):
    add kk_ink
    viewport:
        pos (kk_margin, 110) xysize (1440, 740) mousewheel True draggable True arrowkeys True scrollbars "vertical"
        use kk_ending_detail(e)
    hbox:
        pos (kk_margin, 940) spacing 20
        use kk_link("Lanjut", Return())
        use kk_link("Menu utama", MainMenu())

screen kk_gallery():
    tag menu
    key "game_menu" action Return()
    default grp = KK_ENDINGS[0]["code"].split("-")[1]
    default code = None
    $ groups = list(dict.fromkeys(e["code"].split("-")[1] for e in KK_ENDINGS))
    $ entries = [e for e in KK_ENDINGS if e["code"].split("-")[1] == grp]
    $ current = next((e for e in entries if e["code"] == code), entries[0])
    add kk_ink
    text "Galeri ending" style "kk_heading" pos (kk_margin, 54)
    hbox:
        pos (kk_margin, 154) spacing 6
        for group in groups:
            use kk_link(group, [SetScreenVariable("grp", group), SetScreenVariable("code", None)], active=group == grp)
    viewport:
        pos (kk_margin, 250) xysize (740, 650) mousewheel True draggable renpy.variant("touch") scrollbars "vertical"
        vbox:
            spacing 8
            for entry in entries:
                use kk_link(entry["code"] + "    " + entry["name"], SetScreenVariable("code", entry["code"]), 674, entry == current)
    frame:
        pos (880, 250) xysize (936, 650) background Solid(kk_ink2) padding (36, 32)
        viewport:
            mousewheel True draggable True arrowkeys True scrollbars "vertical"
            use kk_ending_detail(current, diagnostics=True)
    textbutton "‹ Kembali" style "kk_button" action Return() pos (kk_margin, 956)

screen main_menu():
    tag menu
    add "gui/kk_evening.svg"
    frame:
        xysize (790, 1080) background Solid("#16232df9") padding (84, 80)
        vbox:
            yalign .5 spacing 12 at kk_enter
            text "PROTOTIPE     /     18+" size 24 color kk_accent
            text "Kouseikan" size 100 font kk_display bold True
            add Solid(kk_line) xysize (590, 2)
            null height 42
            textbutton "Mulai   ›":
                style "kk_button" text_style "kk_button_text" action Start() xsize 560
                background Solid(kk_accent) hover_background Solid("#ffceb1")
                text_color kk_ink text_hover_color kk_ink text_bold True
            use kk_link("Lanjutkan", Continue(), 560)
            use kk_link("Muat", ShowMenu("load"), 560)
            use kk_link("Pengaturan", ShowMenu("preferences"), 560)
            use kk_link("Keluar", Quit(confirm=True), 560)

screen game_menu(title, scroll=None):
    key "game_menu" action Return()
    add kk_ink
    frame:
        xysize (470, 1080) background Solid(kk_ink2) padding (52, 70)
        vbox:
            spacing 12
            text "Kouseikan" size 48 bold True
            add Solid(kk_accent) xysize (64, 4)
            null height 40
            if not main_menu:
                use kk_link("Simpan", ShowMenu("save"), 352, title == "Simpan")
            use kk_link("Muat", ShowMenu("load"), 352, title == "Muat")
            use kk_link("Pengaturan", ShowMenu("preferences"), 352, title == "Pengaturan")
            if not main_menu:
                use kk_link("Riwayat", ShowMenu("history"), 352, title == "Riwayat")
                use kk_link("Menu utama", MainMenu(), 352)
            null height 36
            use kk_link("‹ Kembali", Return(), 352)
    text title style "kk_heading" pos (552, 66)
    frame:
        pos (552, 170) xysize (1280, 850) background None padding (0, 0)
        transclude

screen save():
    tag menu
    use game_menu("Simpan"):
        use kk_file_slots(FileSave)

screen load():
    tag menu
    use game_menu("Muat"):
        use kk_file_slots(FileLoad)

screen kk_file_slots(act):
    vbox:
        spacing 24
        grid 3 2:
            spacing 18
            for i in range(1, 7):
                button:
                    style "kk_button" xysize (400, 298) padding (18, 16)
                    action act(i)
                    vbox:
                        spacing 9
                        text ("Slot " + str(i)) size 24 color kk_accent
                        fixed:
                            xysize (360, 176)
                            add Solid(kk_ink2)
                            if FileLoadable(i):
                                add FileScreenshot(i) fit "contain" xysize (360, 176)
                        text FileTime(i, format="%d/%m/%Y   %H:%M", empty="Kosong") style "kk_caption"
        hbox:
            spacing 12
            use kk_link("‹", FilePagePrevious())
            use kk_link("Otomatis", FilePage("auto"), active=FileCurrentPage() == "auto")
            use kk_link("Cepat", FilePage("quick"), active=FileCurrentPage() == "quick")
            text ("Halaman " + FileCurrentPage()) style "kk_caption" yalign .5
            use kk_link("›", FilePageNext())
            use kk_link("Manual", FilePage(1))

screen preferences():
    tag menu
    use game_menu("Pengaturan"):
        vbox:
            spacing 24
            for caption, pref in [("Kecepatan teks", "text speed"), ("Jeda baca otomatis", "auto-forward time"), ("Volume musik", "music volume"), ("Volume efek suara", "sound volume")]:
                vbox:
                    spacing 12
                    text caption size 28
                    bar value Preference(pref) style "kk_slider" xsize 820 ysize 24 alt caption
            null height 12
            hbox:
                spacing 16
                use kk_link("Berjendela", Preference("display", "window"), active=not _preferences.fullscreen)
                use kk_link("Layar penuh", Preference("display", "fullscreen"), active=_preferences.fullscreen)

screen history():
    tag menu
    use game_menu("Riwayat"):
        viewport:
            yinitial 1.0 mousewheel True draggable True arrowkeys True pagekeys True scrollbars "vertical"
            vbox:
                spacing 20
                if not _history_list:
                    text "Belum ada dialog." style "kk_caption"
                for h in _history_list:
                    if h.who:
                        text h.who substitute False size 24 color kk_accent
                    text renpy.filter_text_tags(h.what, allow=["b","i","u","ruby","rt"]) substitute False size 28 xmaximum 1160

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    key "game_menu" action no_action
    add Solid("#101b24df")
    frame:
        align (.5,.5) xsize 840 background Solid(kk_panel) padding (50, 40)
        vbox:
            spacing 32
            text message size 30
            hbox:
                spacing 16
                use kk_link("Tidak", no_action)
                use kk_link("Ya", yes_action)

screen skip_indicator():
    zorder 100
    text "Melewati dialog ››" color kk_accent size 24 xalign .52 ypos 24

screen notify(message):
    zorder 120
    frame:
        xalign .98 ypos 102 background Solid(kk_panel) padding (28, 16) at kk_enter
        text "[message!tq]" size 24 xmaximum 950
    timer 3.0 action Hide("notify")

screen nvl(dialogue, items=None):
    window:
        id "window"
        background Solid(kk_ink)
        padding (kk_margin, 54)
        viewport:
            yinitial 1.0 mousewheel True draggable True
            vbox:
                spacing 18
                for d in dialogue:
                    vbox:
                        id d.window_id
                        if d.who:
                            text d.who id d.who_id size 24 color kk_accent
                        text d.what id d.what_id size 30
                for item in items or []:
                    use kk_link(item.caption, item.action)
