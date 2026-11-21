# Reference GUI integration. Presentation only; existing story/state/travel remain authoritative.
# Loaded after the original screens, so local story edits and save identifiers stay intact.
init offset = 20

define kg_root = "gui/kouseikan/"
define kg_body = "gui/kouseikan/fonts/Nunito.ttf"
define kg_dialogue = "font/Buat dialog orang/BRLNSR.TTF"
define kg_system_dialogue = "font/Buat dialog system/Blue Highway Rg.otf"
define kg_system_scale = 1120.0 / 1472.0
define kg_hand = "gui/kouseikan/fonts/Kalam-Bold.ttf"
define kg_title = "gui/kouseikan/fonts/Tinos-Italic.ttf"
define kg_ink = "#35234F"
define kg_muted = "#896C98"
define kg_pink = "#D579B5"
default persistent.kk_gui_dark = False

init 25 python:
    import copy as _kg_copy

    def kg_image(name, width, height):
        return Transform(kg_root + name + ".png", xysize=(int(width), int(height)))

    def kg_dialogue_skin(who, what):
        if who and "SISTEM" in who.upper():
            return "system-dialogue"
        if kk_host not in ("yutaka", "chiasa"):
            return "dialogue-neutral"
        if persistent.kk_gui_dark:
            return "dialogue-dark"
        return "dialogue-chiasa" if kk_host == "chiasa" else "dialogue-yutaka"

    KG_DISTRICT_POS = {
        "d1": (205, 346, 540), "d2": (126, 592, 438),
        "d3": (1454, 341, 444), "d4": (845, 596, 432),
        "d5": (443, 860, 552), "d6": (865, 325, 390),
        "d7": (1279, 813, 474),
    }
    KG_DISTRICT_CROP = {"d1":(390,190),"d2":(240,500),"d3":(1360,190),
                        "d4":(820,475),"d5":(530,790),"d6":(900,150),"d7":(1240,745)}

    def kg_district_picture(district, width=500, height=300):
        cx, cy = KG_DISTRICT_CROP.get(district, (900, 500))
        return Transform(kg_root + "city.png", crop=(max(0,int(cx-300)),max(0,int(cy-190)),600,380), xysize=(width,height))

    def kg_initial(cid):
        return KK_CHARS[cid]["nama"].split()[-1][:1].upper()

    def kg_map_people():
        # Current schedule only. No fabricated face/name pairing or new NPC state.
        groups = {}
        for cid in KK_PHONE_ORDER:
            place = kk_daily_place(cid)
            if not place:
                continue
            for did, name, places in KK_DISTRICTS:
                if place in places:
                    groups.setdefault(did, []).append((cid, place))
                    break
        return groups

    def kg_replays():
        entries = {}
        for events in KK_EV_BY_CHAR.values():
            for event in events:
                label = "kkscene_" + event["id"]
                if renpy.has_label(label) and renpy.seen_label(label):
                    entries[event["id"]] = event
        return sorted(entries.values(), key=lambda e:(e["month"], e["id"]))

    # Retheme legacy/diagnostic screens as well, without replacing their operations.
    kk_ink, kk_ink2, kk_panel = "#FAF3FC", "#EDE1F3", "#F8ECF6"
    kk_bone, kk_bone2, kk_dim = kg_ink, "#71587F", kg_muted
    kk_accent, kk_acc2, kk_line = "#A574BC", "#8EAADC", "#CDB6D8"
    kk_body, kk_display = kg_body, kg_hand
    # Character-specific legacy colors would override the new screen contrast.
    # Keep names, callbacks, CTC and story behavior; let each skin supply colors.
    for _kg_character in (nar, sistem, koita, miyuki, nagisa, harumi, moeka, shiori, chiasa, yutaka, mc):
        _kg_character.who_args.pop("color", None)
        _kg_character.what_args.pop("color", None)

style default:
    font kg_body
    color kg_ink

style kk_heading:
    font kg_hand
    color kg_ink

style kk_caption:
    font kg_body
    color kg_muted

style kk_button:
    background Frame("gui/kouseikan/ribbon.png", 24, 12)
    hover_background Frame("gui/kouseikan/ribbon-hover.png", 24, 12)
    selected_background Frame("gui/kouseikan/ribbon-selected.png", 24, 12)

style kk_button_text:
    font kg_body
    color kg_ink
    hover_color "#5E2E88"
    selected_color kg_ink

style kk_slider:
    left_bar Solid("#C58BC6")
    right_bar Solid("#DACEEC")
    thumb Transform("gui/kouseikan/star-thumb.png", xysize=(38,38))
    hover_thumb Transform("gui/kouseikan/star-thumb.png", xysize=(42,42))
    thumb_offset 18

style vscrollbar:
    base_bar Solid("#E8DAEE")
    thumb Solid("#B594CA")
    hover_thumb Solid("#D99BC7")

transform kg_enter:
    on show:
        alpha 0.0 yoffset 10
        easeout .18 alpha 1.0 yoffset 0

image kk_continue = ConditionSwitch("not kk_host", Text("  ›", size=30, color="#B89B35"), "True", Text("  ›", size=30, color=kk_accent))

style kg_button is button:
    background Frame("gui/kouseikan/ribbon.png", 22, 10)
    hover_background Frame("gui/kouseikan/ribbon-hover.png", 22, 10)
    selected_background Frame("gui/kouseikan/ribbon-selected.png", 22, 10)
    insensitive_background Frame("gui/kouseikan/ribbon-disabled.png", 22, 10)
    padding (25, 12)
    yminimum 62

style kg_button_text is button_text:
    font kg_body
    color kg_ink
    hover_color "#662E8A"
    selected_color kg_ink
    insensitive_color "#A494AD"
    size 27

screen kg_button(caption, operation, width=310, height=70, selected=False, identifier=None):
    button:
        id identifier
        style "kg_button"
        xysize (width,height)
        action operation
        selected selected
        text caption style "kg_button_text" yalign .5 xmaximum (width-50)

screen kk_link(caption, operation, width=None, active=False, first=False):
    textbutton caption:
        style "kg_button"
        text_style "kg_button_text"
        action operation
        selected active
        default_focus first
        xsize width

screen kg_tool(icon, caption, operation, selected=False, identifier=None):
    $ _kg_tag = "tool-tag-neutral" if not kk_host and not main_menu else "tool-tag"
    button:
        id identifier
        xysize (92,78)
        padding (0,0)
        background kg_image(_kg_tag,92,78)
        hover_background Transform(kg_root+_kg_tag+".png",xysize=(92,78),matrixcolor=BrightnessMatrix(.16))
        action operation
        selected selected
        alt caption
        add kg_image("icon-"+icon,40,40) align (.5,.5)

screen kg_main_icon(icon,caption,operation):
    imagebutton:
        id ("kg_main_"+icon)
        idle Transform(kg_root+"main-icons/"+icon+".png",xysize=(104,104))
        hover Transform(kg_root+"main-icons/"+icon+".png",xysize=(104,104),matrixcolor=BrightnessMatrix(.10))
        focus_mask True
        action operation
        alt caption
        at ks_main_icon_motion

screen main_menu():
    tag menu
    add kg_image("main-art",1920,1080)
    add Solid("#17112E14")
    text "Kouseikan" font kg_title size 128 color "#FFF7F8" pos (1100,150) outlines [(2,"#6D477A66",0,2)]
    text "— To NTR the Shounen MC —" font kg_title size 27 color "#FFF3FB" pos (1215,302)
    button:
        id "kg_new_game"
        pos (1280,399) xysize (492,154) padding (0,0)
        background kg_image("main-new",492,154)
        hover_background Transform(kg_root+"main-new.png",xysize=(492,154),matrixcolor=BrightnessMatrix(.06))
        action Start()
        alt "New Game"
        text "New" font kg_hand size 64 color "#29204B" pos (67,28)
        text "Game" font kg_hand size 64 color "#CC489B" pos (222,38)
    button:
        pos (1280,563) xysize (492,132) padding (0,0)
        background kg_image("main-continue",492,132)
        hover_background Transform(kg_root+"main-continue.png",xysize=(492,132),matrixcolor=BrightnessMatrix(.1))
        action Continue()
        alt "Continue"
        text "Continue" font kg_body bold True italic True size 45 color "#FFFFFF" pos (146,36)
    hbox:
        id "kg_main_icon_row"
        pos (1238,710) spacing 14
        use kg_main_icon("settings","Pengaturan",ShowMenu("preferences"))
        use kg_main_icon("gallery","Galeri cutscene",ShowMenu("kk_cutscene_gallery"))
        use kg_main_icon("bookmark","Muat permainan",ShowMenu("load"))
        use kg_main_icon("system","System",ShowMenu("kk_system_menu"))
        use kg_main_icon("exit","Keluar",Quit(confirm=True))
    text "KOUSEIKAN" font kg_body size 18 color "#FFFFFFAA" pos (44,1030)

screen kk_hud():
    if kk_host:
        frame:
            pos (630,20) xysize (665,60) padding (28,10)
            background Frame(kg_root+"ribbon.png",24,12)
            text (kk_clock()+"  ·  "+kk_hari+", "+str(kk_hari_n)+" "+kk_month_tuple()[1]+"  /  "+KK_SLOTS[kk_slot]) font kg_body size 22 color kg_ink yalign .5

screen say(who, what):
    $ _kg_skin = kg_dialogue_skin(who,what)
    if _kg_skin == "system-dialogue":
        window:
            id "window"
            pos (224,288) xysize (1472,756) padding (0,0)
            background kg_image("system-dialogue",1472,756)
            text who id "who" font kg_hand size 29 color "#533582" pos (470,149)
            text what id "what" font kg_system_dialogue size 30 color "#29165F" pos (188,254) xmaximum 1148 line_spacing 5
    else:
        window:
            id "window"
            pos (162,704) xysize (1596,348) padding (0,0)
            background kg_image(_kg_skin,1596,348)
            if who:
                text who id "who" font kg_body bold True size 25 color "#FFF7FF" pos (123,37) xmaximum 800
            text what id "what" font kg_dialogue size 32 color ("#3E4047" if _kg_skin == "dialogue-neutral" else "#F8EDFF" if _kg_skin == "dialogue-dark" else kg_ink) pos (126,116) xmaximum 1380 line_spacing 5
    use quick_menu

screen quick_menu():
    if quick_menu:
        hbox:
            pos (34,18) spacing 12
            use kg_tool("play","Lewati",Skip())
            use kg_tool("fast","Baca otomatis",Preference("auto-forward","toggle"),_preferences.afm_enable)
            use kg_tool("hide","Sembunyikan GUI",HideInterface())
        hbox:
            pos (1576,18) spacing 12
            use kg_tool("history","Riwayat",ShowMenu("history"))
            use kg_tool("save","Simpan",ShowMenu("save"))
            use kg_tool("load","Muat",ShowMenu("load"))
        button:
            id "kg_phone_launcher"
            pos (1758,820) xysize (144,216) padding (0,0) background None
            action Show("kk_phone_locator")
            alt "Buka HP"
            add kg_image("phone-launch-full" if kk_host else "phone-launch-neutral",144,216)
        if _preferences.afm_enable:
            text "AUTO" font kg_hand size 24 color ("#B89B35" if not kk_host else "#CEB9F0") pos (1600,108)
screen kk_choice_panel(rows, heading):
    modal True
    add Solid("#17112842")
    frame:
        pos (1000,196) xysize (840,650) padding (25,20) background None at kg_enter
        vbox:
            spacing 17
            text heading font kg_hand size 36 color "#FFF1FB" xmaximum 780 outlines [(1,"#342249",0,1)]
            viewport:
                xysize (790,540) mousewheel True draggable renpy.variant("touch") scrollbars "vertical" arrowkeys True
                vbox:
                    spacing 15 xsize 748
                    for index,(caption,operation,chosen) in enumerate(rows):
                        button:
                            xysize (740,108) padding (90,18)
                            background kg_image("choice-idle",740,108)
                            hover_background kg_image("choice-hover",740,108)
                            action operation
                            default_focus index == 0
                            text caption font kg_body size 27 color kg_ink yalign .5 xmaximum 558

screen choice(items):
    use kk_choice_panel([(i.caption,i.action,i.chosen) for i in items],"Pilihanmu")

screen kk_choices(ev):
    modal True
    use kk_choice_panel([(c["label"],Return(c["key"]),False) for c in ev["choices"]],ev["title"])

screen kk_route_select():
    add "gui/kk_evening.svg"
    add Solid("#1D1233B9")
    text "Tangan mana yang akan kau raih?" font kg_hand size 64 color "#FFF1FD" xalign .5 ypos 180
    hbox:
        pos (202,432) spacing 55
        for host,name in [("yutaka","Tangan pria di sebelah kiri"),("chiasa","Tangan wanita di sebelah kanan")]:
            button:
                xysize (730,240) padding (65,45)
                background kg_image("action-idle",730,240)
                hover_background kg_image("action-hover",730,240)
                action Return(host)
                text name font kg_hand size 45 color kg_ink align (.5,.5) text_align .5 xmaximum 600

screen kg_panel(title):
    add Solid("#141125ED")
    add kg_image("paper-panel",1640,900) pos (140,105)
    text title font kg_hand size 65 color kg_ink pos (224,130)
    fixed:
        pos (1680,119)
        use kg_tool("close","Kembali",Return())
    frame:
        pos (230,250) xysize (1450,650) background None padding (0,0)
        transclude

screen game_menu(title, scroll=None):
    key "game_menu" action Return()
    use kg_panel(title):
        transclude
    hbox:
        pos (252,949) spacing 12
        if not main_menu:
            use kg_button("Simpan",ShowMenu("save"),214,62)
        use kg_button("Muat",ShowMenu("load"),214,62)
        use kg_button("Pengaturan",ShowMenu("preferences"),270,62)
        if not main_menu:
            use kg_button("Menu utama",MainMenu(),270,62)

screen kg_pause_menu():
    tag menu
    key "game_menu" action Return()
    use kg_panel("Menu"):
        vbox:
            spacing 28
            text "Mau melanjutkan ke mana?" font kg_hand size 37 color kg_muted
            grid 2 4:
                spacing 25
                use kg_button("Lanjut bermain",Return(),650,108,identifier="kg_resume")
                use kg_button("Simpan",ShowMenu("save") if not main_menu else None,650,108)
                use kg_button("Muat",ShowMenu("load"),650,108)
                use kg_button("Pengaturan",ShowMenu("preferences"),650,108)
                use kg_button("Galeri adegan",ShowMenu("kk_cutscene_gallery"),650,108)
                use kg_button("System",ShowMenu("kk_system_menu"),650,108)
                use kg_button("Menu utama",MainMenu(),650,108)
                use kg_button("Keluar",Quit(),650,108)

screen save():
    tag menu
    key "game_menu" action Return()
    use kg_save_album(FileSave,"Save")

screen load():
    tag menu
    key "game_menu" action Return()
    use kg_save_album(FileLoad,"Load Slots")

screen kg_save_album(operation,title):
    add Solid("#100E24")
    add kg_image("save-album",1920,1080)
    text title font kg_hand size 78 color kg_ink pos (330,65)
    text "Manual" font kg_hand size 24 color kg_muted pos (1427,160)
    fixed:
        pos (1610,75)
        use kg_tool("close","Kembali",Return())
    grid 3 2:
        pos (435,264) spacing 36
        for slot in range(1,7):
            button:
                id ("kg_slot_"+str(slot))
                xysize (324,276) padding (0,0)
                background kg_image("polaroid",324,276)
                hover_background Transform(kg_root+"polaroid.png",xysize=(324,276),matrixcolor=BrightnessMatrix(.035))
                action operation(slot)
                key "save_delete" action FileDelete(slot)
                if FileLoadable(slot):
                    add FileScreenshot(slot) pos (25,21) xysize (275,164) fit "contain"
                text ("Slot "+str(slot)) font kg_hand size 27 color kg_ink pos (24,188)
                text FileTime(slot,format="%d/%m/%Y  %H:%M",empty="Kosong") font kg_body size 18 color kg_muted pos (24,236) xmaximum 275
    hbox:
        pos (386,946) spacing 13
        use kg_button("‹",FilePagePrevious(),75,59)
        use kg_button("Otomatis",FilePage("auto"),180,59)
        use kg_button("Cepat",FilePage("quick"),145,59)
        use kg_button("Manual",FilePage(1),165,59)
        text ("Halaman "+FileCurrentPage()) font kg_body size 23 color "#C7ACDA" yalign .5
        use kg_button("›",FilePageNext(),75,59)

screen kk_file_slots(act):
    use kg_save_album(act,"Save" if act == FileSave else "Load Slots")

screen preferences():
    tag menu
    key "game_menu" action Return()
    add Solid("#100E24")
    add kg_image("settings-notebook",1920,1080)
    text "Settings" font kg_hand size 78 color kg_ink pos (416,162)
    fixed:
        pos (1614,131)
        use kg_tool("close","Kembali",Return())
    vbox:
        pos (413,309) spacing 38
        for caption,pref in [("Kecepatan teks","text speed"),("Jeda baca otomatis","auto-forward time"),("Volume musik","music volume"),("Volume efek suara","sound volume")]:
            vbox:
                spacing 14
                text caption font kg_body bold True size 27 color "#71537E"
                bar value Preference(pref) style "kk_slider" xsize 650 ysize 35 alt caption
        textbutton "Kotak dialog gelap":
            style "kg_button" text_style "kg_button_text"
            action ToggleField(persistent,"kk_gui_dark")
            selected persistent.kk_gui_dark
    text "Display" font kg_hand size 40 color "#735388" pos (1398,276)
    vbox:
        pos (1376,577) spacing 22
        use kg_button("Berjendela",Preference("display","window"),276,72,not _preferences.fullscreen)
        use kg_button("Layar penuh",Preference("display","fullscreen"),276,72,_preferences.fullscreen)

screen history():
    tag menu
    use game_menu("History"):
        viewport:
            yinitial 1.0 xysize (1435,650) mousewheel True draggable True arrowkeys True pagekeys True scrollbars "vertical"
            vbox:
                spacing 23 xsize 1350
                if not _history_list:
                    text "Belum ada dialog." font kg_hand size 32 color kg_muted
                for h in _history_list:
                    vbox:
                        spacing 7
                        if h.who:
                            text h.who substitute False font kg_hand size 27 color "#9A70B0"
                        text renpy.filter_text_tags(h.what,allow=["b","i","u","ruby","rt"]) substitute False font kg_body size 29 color kg_ink xmaximum 1310
                        add Solid("#E3CEE5") xysize (1310,1)

screen confirm(message,yes_action,no_action):
    modal True
    zorder 200
    key "game_menu" action no_action
    add Solid("#17112CD9")
    frame:
        align (.5,.5) xysize (980,480) background kg_image("paper-panel",980,480) padding (75,65) at kg_enter
        vbox:
            spacing 42
            text "Sebentar…" font kg_hand size 48 color kg_ink
            text message font kg_body size 31 color kg_ink xmaximum 810
            hbox:
                spacing 30
                use kg_button("Tidak",no_action,330,78)
                use kg_button("Ya",yes_action,330,78)

screen notify(message):
    zorder 120
    frame:
        xalign .98 ypos 108 xsize 780 yminimum 100 padding (35,24)
        background Frame(kg_root+"ribbon.png",24,10) at kg_enter
        text "[message!tq]" font kg_body size 25 color kg_ink xmaximum 700
    timer 3.0 action Hide("notify")

screen skip_indicator():
    zorder 100
    text "SKIP ››" font kg_hand color "#C8ACED" size 25 xalign .50 ypos 95

screen kk_system_menu():
    tag menu
    key "game_menu" action Return()
    add Solid("#110D27EE")
    add kg_image("system-dialogue",1490,766) pos (214,160)
    text "SYSTEM" font kg_body bold True size 60 color "#422579" pos (686,326)
    grid 2 2:
        pos (570,454) spacing 45
        if kk_host:
            use kg_button("Status",Show("kk_status"),340,100)
            use kg_button("HP",Show("kk_phone_locator"),340,100)
        else:
            use kg_button("Pengaturan",ShowMenu("preferences"),340,100)
            use kg_button("Galeri adegan",ShowMenu("kk_cutscene_gallery"),340,100)
        use kg_button("Simpan" if kk_host else "Muat",ShowMenu("save" if kk_host else "load"),340,100)
        use kg_button("Kembali",Return(),340,100)

screen kk_cutscene_gallery():
    tag menu
    default page = 0
    $ entries = kg_replays()
    use game_menu("Cutscene Gallery"):
        hbox:
            spacing 45
            fixed:
                xysize (680,560)
                add Solid("#59406C") xysize (680,395)
                add kg_image("main-art",648,365) pos (16,15)
                for i in range(24):
                    add Solid("#EFDAEE") pos (12+i*28,4) xysize (15,7)
                    add Solid("#EFDAEE") pos (12+i*28,385) xysize (15,7)
                text "Kenangan Kouseikan" font kg_hand size 39 color kg_ink pos (38,427)
                text "Adegan yang sudah kamu alami." font kg_body size 25 color kg_muted pos (38,484)
            vbox:
                spacing 17
                if not entries:
                    text "Belum ada adegan yang terbuka." font kg_hand size 34 color kg_muted xmaximum 590
                for entry in entries[page*5:page*5+5]:
                    use kg_button(entry["title"],Replay("kk_gui_replay",scope={"kk_replay_eid":entry["id"],"kk_replay_host":kk_host or "yutaka"},locked=False),660,88,identifier="kg_replay_"+entry["id"])
                hbox:
                    spacing 18
                    if page:
                        use kg_button("‹",SetScreenVariable("page",page-1),95,62)
                    if len(entries) > (page+1)*5:
                        use kg_button("›",SetScreenVariable("page",page+1),95,62)

label kk_gui_replay:
    $ kk_host = kk_replay_host
    $ kk_setup_state()
    $ _kg_ev = next(e for es in KK_EV_BY_CHAR.values() for e in es if e["id"] == kk_replay_eid)
    $ kk_bulan = next((i+1 for i,m in enumerate(KK_BACKBONE) if m[0] == _kg_ev["month"]), 1)
    $ _distrik, _lokasi = next(((m[2],m[3]) for m in KK_MILESTONE_MAP if m[0] == kk_replay_eid), ("d1","Taman Kampus"))
    call expression ("kkscene_"+kk_replay_eid)
    $ renpy.end_replay()
    return

screen kk_world_district():
    tag kk_world
    use kg_city_map(True)
    hbox:
        pos (58,996) spacing 18
        if kk_can_skip():
            use kg_button("Lanjutkan rutinitas mingguan",Return(("skip",None)),460,62)
        if config.developer and kk_debug_tools:
            use kg_button("Alat uji",Show("kk_debug_panel"),200,62)

screen kg_city_map(travel=True):
    add kg_image("city",1894,941) pos (13,90)
    add kg_image("map-bands",1920,1080)
    text "Kouseikan" font kg_title size 89 color "#24116C" pos (90,1)
    text "P E T A   K O T A" font kg_body bold True size 24 color "#9B73DC" pos (92,84)
    text kk_clock() font kg_hand size 52 color "#24116C" pos (862,20)
    $ _mt = kk_month_tuple()
    text (kk_hari+", "+str(kk_hari_n)+" "+_mt[1]) font kg_body bold True size 29 color "#24116C" pos (1103,25)
    text ("Hari ke-"+str(kk_hari_n)+" · "+KK_SLOTS[kk_slot]) font kg_body size 23 color "#6A4AA3" pos (1104,64)
    text "N" font kg_body bold True size 24 color "#24116C" pos (82,149)
    text "Berpindah distrik memakan waktu." font kg_body size 24 color "#4C2590" pos ((750 if travel and kk_can_skip() else 112),1033)
    for index,(did,dnama,places) in enumerate(KK_DISTRICTS):
        $ px,py,pw = KG_DISTRICT_POS[did]
        button:
            id ("qa_"+did)
            pos (px,py) xysize (pw,83) padding (0,0)
            background kg_image("map-label",pw,83)
            hover_background Transform(kg_root+"map-label.png",xysize=(pw,83),matrixcolor=BrightnessMatrix(.045))
            action (Return(("go",did)) if travel else SetScreenVariable("district",did))
            alt dnama
            text (str(index+1).zfill(2)) font kg_body bold True size 28 color "#FFFFFF" pos (30,19)
            text dnama font kg_hand size (29 if len(dnama)>17 else 33) color "#24116C" pos (97,4) xmaximum (pw-113)
            text (str(len(places))+" lokasi") font kg_body size 23 color "#39236D" pos (98,47)
    $ _kg_people = kg_map_people()
    for did,people in _kg_people.items():
        $ px,py,pw = KG_DISTRICT_POS[did]
        $ _kg_pin_gap = min(104, int((pw-104)/max(1,len(people)-1)))
        $ _kg_pin_left = px + int((pw-104-_kg_pin_gap*(len(people)-1))/2)
        for index,(cid,place) in enumerate(people):
            button:
                pos (_kg_pin_left+index*_kg_pin_gap,py-138-index%2*12) xysize (104,134) padding (0,0) background None
                action (Return(("go",did)) if travel else SetScreenVariable("district",did))
                alt (KK_CHARS[cid]["nama"]+" di "+place)
                add kg_image("pin",104,134)
                text kg_initial(cid) font kg_hand size 43 color KK_CHARS[cid]["warna"] xalign .5 ypos 23
    button:
        id "kg_map_phone_launcher"
        pos (1762,828) xysize (144,216) background None padding (0,0)
        action Show("kk_phone_locator")
        alt "Buka HP"
        add kg_image("phone-launch-full" if kk_host else "phone-launch-neutral",144,216)
screen kk_world_location(distrik):
    tag kk_world
    use kg_district_detail(distrik,True)

screen kg_district_detail(distrik,travel=True):
    add Solid("#F9F2EA")
    add kg_image("paper-panel",1058,713) pos (752,274)
    text KK_DISTRICT_NAME[distrik] font kg_hand size 68 color kg_ink pos (284,57) xmaximum 1050
    fixed:
        pos (55,57)
        use kg_button("Peta Kota",Return("back") if travel else SetScreenVariable("district",None),190,70)
    hbox:
        pos (1400,59) spacing 12
        use kg_tool("phone","HP",Show("kk_phone_locator"))
        use kg_tool("status","Status",Show("kk_status"))
        use kg_tool("save","Menu",ShowMenu("save"))
    add kg_image("paper-panel",590,570) pos (72,259)
    add kg_district_picture(distrik,535,330) pos (98,325)
    text KK_DISTRICT_NAME[distrik] font kg_hand size 38 color "#795884" pos (104,689) xmaximum 515
    text (str(len(KK_DISTRICT_LOCS[distrik]))+" lokasi") font kg_body size 25 color "#A582A1" pos (105,755)
    text "Pilih tempat tujuanmu." font kg_hand size 36 color "#A87CA0" pos (110,907)
    text (str(len(KK_DISTRICT_LOCS[distrik]))+" tempat untuk dikunjungi") font kg_hand size 32 color kg_muted pos (804,209)
    viewport:
        pos (803,311) xysize (943,620) mousewheel True draggable renpy.variant("touch") scrollbars "vertical" arrowkeys True
        vbox:
            spacing 14
            for index,location in enumerate(KK_DISTRICT_LOCS[distrik]):
                button:
                    id ("qa_"+location)
                    xysize (890,72) padding (28,12)
                    style "kg_button"
                    action (Show("kg_travel_confirm",distrik=distrik,lokasi=location) if travel else NullAction())
                    text (str(index+1).zfill(2)+"   "+location+"   ›") font kg_body size 28 color kg_ink yalign .5
    text "Berpindah distrik memakan waktu." font kg_body size 23 color kg_muted pos (80,1030)

screen kg_travel_confirm(distrik,lokasi):
    modal True
    zorder 100
    key "game_menu" action Hide("kg_travel_confirm")
    add Solid("#17112AD9")
    frame:
        align (.5,.5) xysize (1040,530) background kg_image("paper-panel",1040,530) padding (65,55) at kg_enter
        vbox:
            spacing 20
            text "Mau ke sini?" font kg_hand size 58 color kg_ink
            text KK_DISTRICT_NAME[distrik] font kg_hand size 27 color kg_muted
            text lokasi font kg_body bold True size 37 color kg_ink xmaximum 900
            text "Berpindah lokasi memakan waktu." font kg_body size 25 color kg_muted
            hbox:
                spacing 27
                use kg_button("Batal",Hide("kg_travel_confirm"),360,78)
                use kg_button("Pergi",[Hide("kg_travel_confirm"),Return(lokasi)],360,78)

screen kk_phone_locator():
    modal True
    zorder 90
    default tab = "home"
    key "game_menu" action Hide("kk_phone_locator")
    add Solid("#100D25DF")
    fixed:
        pos (620,32) xysize (680,1010) at kg_enter
        add kg_image("phone-frame",610,1000) pos (35,0)
        frame:
            pos (89,44) xysize (501,875) padding (0,0) background None
            if not kk_host:
                add kg_image("phone-neutral",501,875)
            elif kk_host == "chiasa":
                add kg_image("phone-chiasa",501,875)
            else:
                add kg_image("phone-yutaka",501,875)
            $ _pc = "#41434B" if not kk_host else "#56354D" if kk_host == "chiasa" else "#FFFFFF"
            text kk_clock() font kg_body size 22 color _pc pos (23,19)
            text "Kouseikan" font kg_body size 21 color _pc xalign .5 ypos 118
            text kk_clock() font kg_body size 73 color _pc xalign .5 ypos 157
            text (kk_hari+", "+str(kk_hari_n)+" "+kk_month_tuple()[1]) font kg_body size 24 color _pc xalign .5 ypos 247
            hbox:
                pos (24,334) spacing 17
                use kg_tool("messages","Messages",SetScreenVariable("tab","messages"))
                use kg_tool("location","Location",SetScreenVariable("tab","location"))
                use kg_tool("status","Status",[Hide("kk_phone_locator"),Show("kk_status")])
                use kg_tool("home","Menu game",[Hide("kk_phone_locator"),ShowMenu("kg_pause_menu")],identifier="kg_phone_menu")
            if tab != "home":
                frame:
                    pos (15,437) xysize (470,400) background Frame(kg_root+"paper-panel.png",22,15) padding (24,22)
                    vbox:
                        spacing 14
                        text ("Location" if tab == "location" else "Messages") font kg_hand size 35 color kg_ink
                        if tab == "location":
                            viewport:
                                xysize (424,254) mousewheel True draggable True scrollbars "vertical"
                                vbox:
                                    spacing 13 xsize 388
                                    for cid in KK_PHONE_ORDER:
                                        $ where,district_name = kk_phone_locate(cid)
                                        text KK_CHARS[cid]["nama"] font kg_body bold True size 23 color kg_ink
                                        text where font kg_body size 20 color kg_muted xmaximum 380
                            use kg_button("Lihat peta",[Hide("kk_phone_locator"),Show("kg_map_viewer")],402,60)
                        else:
                            $ _messages = kk_incoming_messages() if kk_host else []
                            if not _messages:
                                text "Belum ada pesan baru." font kg_body size 24 color kg_muted
                            else:
                                for item in _messages[:4]:
                                    text (KK_CHARS.get(item[0],{}).get("nama",item[0].replace("_"," ").title())) font kg_body size 23 color kg_ink
                                text "Pesan akan diterima saat kamu melanjutkan aktivitas." font kg_body size 20 color kg_muted
        button:
            pos (260,936) xysize (170,40) background None
            action Hide("kk_phone_locator")
            alt "Tutup HP"
            add Solid("#E0D5EA") xysize (160,7) yalign .5
    fixed:
        pos (1340,65)
        use kg_tool("close","Tutup HP",Hide("kk_phone_locator"))

screen kg_map_viewer():
    modal True
    zorder 85
    default district = None
    key "game_menu" action Hide("kg_map_viewer")
    if district:
        use kg_district_detail(district,False)
    else:
        use kg_city_map(False)
    fixed:
        pos (1780,20)
        use kg_tool("close","Kembali",Hide("kg_map_viewer"))
