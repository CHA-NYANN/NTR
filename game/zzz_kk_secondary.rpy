# Secondary GUI only. Protected screens remain in zz_kk_gui.rpy.
init offset = 40
default persistent.kk_secondary_motion = True
init 45 python:
    import math as _ks_math
    import re as _ks_re
    def ks_art(name,w,h):
        return Transform(kg_root+'secondary/'+name+'.png',xysize=(int(w),int(h)))
    def ks_resume_drag(drags,drop):
        drag=drags[0]
        if drag.y < 110:
            renpy.run(Return())
        else:
            drag.snap(790,235,.22)
        return None

    def ks_text_lines(text,width,size):
        plain=_ks_re.sub(r"\{[^}]*\}","",renpy.substitute(str(text)))
        capacity=max(16,int(width/(size*.53)))
        return sum(max(1,_ks_math.ceil(len(line)/float(capacity))) for line in plain.split("\n"))

    def ks_dialog_height(who,what):
        system=bool(who and "SISTEM" in who.upper())
        lines=ks_text_lines(what,1148 if system else 1380,35 if system else 32)
        return min(756,max(420,315+lines*53)) if system else min(920,max(235,158+lines*49))

    def ks_choice_height(caption):
        return max(84,36+ks_text_lines(caption,558,27)*41)

    def ks_last_met(cid):
        if cid not in kk_last_met:
            return "Belum ada percakapan yang tercatat."
        days=kk_elapsed_days-kk_last_met[cid]
        return "Terakhir berbincang hari ini." if days == 0 else "Terakhir berbincang %d hari lalu."%days

    def ks_event_place(entry):
        row=next((m for m in KK_MILESTONE_MAP if m[0] == entry['id']),None)
        return (row[2],row[3]) if row else ('d1','Kouseikan')

transform ks_motion(angle=0,delay=0):
    rotate_pad False
    rotate angle
    on show:
        alpha 0.0 yoffset (24 if persistent.kk_secondary_motion else 0)
        pause (delay if persistent.kk_secondary_motion else 0)
        easeout (.32 if persistent.kk_secondary_motion else 0) alpha 1.0 yoffset 0
    on hover:
        easeout (.14 if persistent.kk_secondary_motion else 0) alpha 1.0 zoom (1.025 if persistent.kk_secondary_motion else 1.) rotate (angle-1 if persistent.kk_secondary_motion else angle) yoffset (-5 if persistent.kk_secondary_motion else 0)
    on idle:
        ease (.14 if persistent.kk_secondary_motion else 0) alpha 1.0 zoom 1.0 rotate angle yoffset 0

style ks_button is button:
    background Frame("gui/kouseikan/secondary/ticket.png",82,22,45,25)
    hover_background Frame("gui/kouseikan/ribbon-hover.png",24,12)
    padding (85,15,25,15)
    yminimum 64

transform ks_sheet_arrive:
    on show:
        alpha 0.0 xoffset (-20 if persistent.kk_secondary_motion else 0)
        easeout (.22 if persistent.kk_secondary_motion else 0) alpha 1.0 xoffset 0

style ks_button_text is button_text:
    font kg_hand
    size 28
    color kg_ink
    hover_color "#9A4678"
    insensitive_color "#A795A6"

style ks_fader is vbar:
    xsize 38
    top_bar Solid("#2B2136")
    bottom_bar Solid("#C493BC")
    thumb Transform("gui/kouseikan/star-thumb.png",xysize=(42,42))
    thumb_offset 19

screen ks_button(caption,operation,width=300,identifier=None):
    button:
        id identifier
        style "ks_button" xsize width
        padding ((85,14,22,14) if width >= 250 else (24,14))
        background (Frame("gui/kouseikan/secondary/button-small.png",18,15,18,15) if width < 250 else Frame("gui/kouseikan/secondary/ticket.png",82,22,45,25))
        action operation
        text caption style "ks_button_text" xmaximum (width-(107 if width >= 250 else 48))

screen ks_close(operation):
    fixed:
        pos (1756,42) xysize (92,78)
        use kg_tool("close","Kembali",operation)

# The same reference art, text style and controls; only paper height adapts.
screen say(who,what):
    $ _skin=kg_dialogue_skin(who,what)
    $ _height=ks_dialog_height(who,what)
    if _skin == "system-dialogue":
        window:
            id "window"
            pos (224,int(666-_height*.5)) xysize (1472,_height) padding (0,0)
            background Frame(kg_image("system-dialogue",1472,756),270,205,140,100)
            text who id "who" font kg_hand size 29 color "#533582" pos (470,149)
            text what id "what" font kg_body size 35 color "#29165F" pos (188,254) xmaximum 1148 line_spacing 6
    else:
        window:
            id "window"
            pos (162,1052-_height) xysize (1596,_height) padding (0,0)
            background Frame(kg_image(_skin,1596,348),220,95,150,55)
            if who:
                text who id "who" font kg_body bold True size 25 color "#FFF7FF" pos (123,37) xmaximum 800
            text what id "what" font kg_body size 32 color ("#3E4047" if _skin == "dialogue-neutral" else "#F8EDFF" if _skin == "dialogue-dark" else kg_ink) pos (126,116) xmaximum 1380 line_spacing 5
    use quick_menu

screen kk_choice_panel(rows,heading):
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
                            xysize (740,ks_choice_height(caption)) padding (90,18)
                            background Frame(kg_image("choice-idle",740,108),82,64,60,12)
                            hover_background Frame(kg_image("choice-hover",740,108),82,64,60,12)
                            action operation
                            default_focus index == 0
                            text caption font kg_body size 27 color kg_ink yalign .5 xmaximum 558

screen ks_object_button(caption, icon, operation, art, px, py, width, height, angle=0, delay=0, identifier=None, departing=False, enabled=True):
    button:
        id identifier
        pos (px,py) xysize (width,height) padding (0,0)
        background ks_art(art,width,height)
        action operation
        sensitive enabled
        selected departing
        alt caption
        at ks_motion(angle,delay)
        if art == "object-stamp":
            add kg_image("icon-"+icon,52,52) pos (int(width*.32),int(height*.2))
            text caption font kg_hand size 24 color "#FFF3ED" xalign .5 ypos int(height*.62)
        elif art == "object-film":
            add kg_image("main-art",int(width*.72),int(height*.48)) pos (int(width*.12),int(height*.16))
            text caption font kg_hand size 34 color "#FFF3ED" pos (int(width*.12),int(height*.68))
        elif art == "object-folder":
            text caption font kg_hand size 35 color kg_ink pos (int(width*.1),int(height*.45))
        else:
            text caption font kg_hand size (53 if art == "object-letter" else 37) color kg_ink pos (int(width*.09),int(height*.29)) xmaximum int(width*.72)
            if art == "object-note":
                text ("Tempo, suara, gerak" if caption == "Pengaturan" else "Tutup buku sebentar") font kg_body size 16 color kg_muted pos (int(width*.1),int(height*.72))


screen kg_pause_menu():
    tag menu
    key "game_menu" action Return()
    add Solid("#191322DE")
    add ks_art("desk-threads",1920,1080)
    text "Jeda sebentar." font kg_title size 94 color "#F8EBDD" pos (156,77)
    text "Ceritamu masih di sini." font kg_hand size 29 color "#BEA8BF" pos (173,194)
    use ks_object_button("Simpan","save",ShowMenu("save") if not main_menu else None,"object-letter",220,338,470,160,-7,.04,identifier="ks_pause_save")
    use ks_object_button("Muat kenangan","load",ShowMenu("load"),"object-folder",385,573,300,214,5,.1)
    use ks_object_button("Pengaturan","settings",ShowMenu("preferences"),"object-note",156,800,340,195,-5,.15)
    use ks_object_button("Galeri adegan","gallery",ShowMenu("kk_cutscene_gallery"),"object-film",1240,284,328,247,9,.1)
    use ks_object_button("System","system",ShowMenu("kk_system_menu"),"object-stamp",1548,617,144,144,-8,.18)
    use ks_object_button("Menu utama","home",MainMenu(),"object-note",1165,809,320,185,5,.12)
    textbutton "Keluar dari permainan  /":
        pos (1532,976) action Quit()
        text_font kg_hand text_size 24 text_color "#D4BCCB" text_hover_color "#FFF1E7"
    drag:
        id "kg_resume_drag"
        drag_name "resume-phone"
        pos (790,235)
        draggable True droppable False
        dragged ks_resume_drag
        clicked Return()
        button:
            id "kg_resume"
            xysize (356,608) padding (0,0) background None action Return()
            add kg_image("phone-frame",356,608)
            text kk_clock() font kg_body size 55 color "#FFF2E6" xalign .5 ypos 132
            text "Lanjut bermain" font kg_hand size 34 color "#F7DCED" xalign .5 ypos 325
            text "Ketuk, atau geser HP ke atas" font kg_body size 17 color "#BAA8CA" xalign .5 ypos 398
            add Solid("#E6D3E5") pos (120,544) xysize (120,5)


screen save():
    tag menu
    default active_slot = 1
    key "game_menu" action Return()
    use kg_save_album(FileSave,"Save",active_slot)


screen load():
    tag menu
    default active_slot = 1
    key "game_menu" action Return()
    use kg_save_album(FileLoad,"Load Slots",active_slot)


screen kg_save_album(operation,title,active_slot):
    add Solid("#100E24")
    add kg_image("save-album",1920,1080)
    text ("Abadikan." if operation == FileSave else "Buka kembali.") font kg_title size 72 color kg_ink pos (330,65)
    text ("Ketuk foto untuk menyimpan" if operation == FileSave else "Ketuk foto untuk melanjutkan") font kg_hand size 25 color kg_muted pos (353,164)
    text "ALBUM / KOUSEIKAN" font kg_body size 14 color kg_muted pos (1425,171) xmaximum 175
    fixed:
        pos (1610,75)
        use kg_tool("close","Kembali",Return())
    key "K_LEFT" action SetScreenVariable("active_slot",6 if active_slot == 1 else active_slot-1)
    key "K_RIGHT" action SetScreenVariable("active_slot",1 if active_slot == 6 else active_slot+1)
    key "save_delete" action FileDelete(active_slot)
    add kg_image("polaroid",620,530) pos (805,252) at ks_motion(9,.1)
    add kg_image("polaroid",620,530) pos (494,275) at ks_motion(-10,.08)
    button:
        id ("kg_slot_"+str(active_slot))
        pos (608,250) xysize (710,606) padding (0,0)
        background kg_image("polaroid",710,606)
        action operation(active_slot)
        selected False
        at ks_motion(-3,.04)
        if FileLoadable(active_slot):
            add FileScreenshot(active_slot) pos (55,46) xysize (598,354) fit "contain"
        else:
            text "Halaman yang belum ditulis." font kg_hand size 34 color "#846F9D" pos (81,191) xmaximum 550 text_align .5
        text ("Kenangan / "+str(active_slot).zfill(2)) font kg_hand size 47 color kg_ink pos (53,431)
        text FileTime(active_slot,format="%d %b %Y · %H:%M",empty="Satu tempat untuk cerita baru.") font kg_body size 23 color kg_muted pos (53,520) xmaximum 590
    text (str(active_slot).zfill(2)) font kg_title size 90 color "#B8A0BC" pos (1510,356)
    text "Enam bingkai,\nsatu halaman." font kg_hand size 26 color kg_muted pos (1430,475) xmaximum 220
    text "< telusuri >" font kg_hand size 25 color kg_muted pos (1430,622)
    hbox:
        pos (445,825) spacing 15
        for slot in range(1,7):
            button:
                id ("kg_thumb_slot_"+str(slot))
                xysize (145,97) padding (7,7)
                background Solid("#8E698F" if active_slot == slot else "#DED0DD")
                action SetScreenVariable("active_slot",slot)
                if FileLoadable(slot):
                    add FileScreenshot(slot) xysize (130,73) fit "contain"
                text str(slot).zfill(2) font kg_body size 23 color ("#FFF5EF" if active_slot == slot else kg_ink) align (.5,.5)
    hbox:
        pos (380,962) spacing 13
        use kg_button("‹",FilePagePrevious(),75,59)
        use kg_button("Otomatis",FilePage("auto"),180,59)
        use kg_button("Cepat",FilePage("quick"),145,59)
        use kg_button("Manual",FilePage(1),165,59)
        text ("Halaman "+FileCurrentPage()) font kg_body size 23 color "#C7ACDA" yalign .5
        use kg_button("›",FilePageNext(),75,59)


screen kk_file_slots(act):
    default active_slot = 1
    use kg_save_album(act,"Save" if act == FileSave else "Load Slots",active_slot)


screen kg_district_detail(distrik,travel=True):
    add kg_district_picture(distrik,1920,1080)
    add Solid("#23203B9E")
    add kg_image("paper-panel",1058,790) pos (752,218) at ks_sheet_arrive
    text KK_DISTRICT_NAME[distrik] font kg_title size 72 color "#FFF5E8" pos (284,57) xmaximum 1050
    fixed:
        pos (55,57)
        use kg_button("Peta Kota",Return("back") if travel else SetScreenVariable("district",None),190,70)
    hbox:
        pos (1400,59) spacing 12
        use kg_tool("phone","HP",Show("kk_phone_locator"))
        use kg_tool("status","Status",Show("kk_status"))
        use kg_tool("save","Menu",ShowMenu("save"))
    fixed:
        pos (86,310) xysize (610,530) at ks_motion(-5,.04)
        add kg_image("polaroid",610,530)
        add kg_district_picture(distrik,520,314) pos (46,37)
        text KK_DISTRICT_NAME[distrik] font kg_hand size 37 color kg_ink pos (44,381) xmaximum 520
        text (str(len(KK_DISTRICT_LOCS[distrik]))+" tempat, satu distrik.") font kg_body size 23 color kg_muted pos (44,460)
    text "Tujuan berikutnya." font kg_hand size 42 color kg_ink pos (820,260)
    text "Pilih satu catatan untuk berangkat." font kg_body size 21 color kg_muted pos (823,310)
    $ _kg_rows = (len(KK_DISTRICT_LOCS[distrik])+1)//2
    viewport:
        pos (806,366) xysize (950,577) mousewheel True draggable renpy.variant("touch") scrollbars "vertical" arrowkeys True
        grid 2 _kg_rows:
            spacing 18
            for index,location in enumerate(KK_DISTRICT_LOCS[distrik]):
                button:
                    id ("qa_"+location)
                    xysize (440,103) padding (0,0)
                    background ks_art("route-ticket",440,103)
                    action (Show("kg_travel_confirm",distrik=distrik,lokasi=location) if travel else NullAction())
                    at ks_motion(1 if index%2 else -1,index*.018)
                    text str(index+1).zfill(2) font kg_body bold True size 22 color "#FFF4ED" pos (24,33)
                    text location font kg_hand size 25 color kg_ink xpos 88 xmaximum 321 yalign .5
            if len(KK_DISTRICT_LOCS[distrik])%2:
                null width 440 height 103
    text "Berpindah distrik memakan waktu." font kg_body size 23 color "#F4E9DB" pos (80,1030)

screen preferences():
    tag menu
    default preview = 0
    key "game_menu" action Return()
    add ks_art("desk",1920,1080)
    text "Atur iramanya." font kg_title size 86 color kg_ink pos (145,55)
    text "Pengaturan" font kg_body size 21 color kg_muted pos (151,153)
    use ks_close(Return())
    fixed:
        pos (130,215) xysize (850,710) at ks_motion(-1,.02)
        add ks_art("letter",850,710)
        text "Tempo baca" font kg_hand size 48 color kg_ink pos (59,38)
        frame:
            pos (65,132) xysize (715,145) padding (25,16) background Solid("#F0E5DF")
            text "Ini contoh kecepatan teks yang kamu pilih." id ("ks_preview_"+str(preview)) font kg_body size 30 color kg_ink slow_cps _preferences.text_cps xmaximum 665
        fixed:
            pos (63,283)
            use ks_button("Ulang contoh",SetScreenVariable("preview",preview+1),240,"ks_restart_preview")
        text "Kecepatan teks" font kg_body size 24 color kg_muted pos (64,372)
        bar value Preference("text speed") style "kk_slider" pos (63,417) xysize (677,32)
        hbox:
            pos (61,470) spacing 13
            use ks_button("Santai",SetField(_preferences,"text_cps",28),175)
            use ks_button("Cepat",SetField(_preferences,"text_cps",65),175)
            use ks_button("Langsung",SetField(_preferences,"text_cps",0),204)
        text "Jeda baca otomatis" font kg_body size 24 color kg_muted pos (64,578)
        bar value Preference("auto-forward time") style "kk_slider" pos (63,622) xysize (677,32)
    add ks_art("cassette",650,520) pos (1100,260) at ks_motion(1,.05)
    text "Suara latarmu" font kg_title size 52 color kg_ink pos (1108,179)
    vbar id "ks_music_volume" value Preference("music volume") style "ks_fader" pos (1258,490) ysize 205 alt "Volume musik"
    vbar id "ks_sound_volume" value Preference("sound volume") style "ks_fader" pos (1545,490) ysize 205 alt "Volume efek suara"
    text "Musik" font kg_body size 25 color "#F6E6E9" pos (1237,714)
    text "Efek suara" font kg_body size 25 color "#F6E6E9" pos (1495,714)
    hbox:
        pos (1100,827) spacing 15
        use ks_button("Berjendela",Preference("display","window"),280)
        use ks_button("Layar penuh",Preference("display","fullscreen"),280)
    hbox:
        pos (1100,920) spacing 15
        use ks_button("Dialog gelap",ToggleField(persistent,"kk_gui_dark"),280)
        use ks_button("Gerak benda",ToggleField(persistent,"kk_secondary_motion"),280,"ks_motion_toggle")

screen kk_status():
    modal True
    zorder 80
    default contact = None
    key "game_menu" action Hide("kk_status")
    add Solid("#171127E8")
    add ks_art("folio",1660,880) pos (130,150)
    text "Catatan tentangmu." font kg_title size 77 color "#FFF3E5" pos (150,43)
    use ks_close(Hide("kk_status"))
    $ _ks_people=[cid for cid in KK_CHARS if cid in rel]
    $ _ks_rows=max(1,(_ks_people.__len__()+3)//4)
    text KK_CHARS.get(kk_host,{"nama":"Belum memilih tubuh"})["nama"] font kg_hand size 35 color kg_ink pos (205,230) xmaximum 450
    text "Kondisi hari ini" font kg_body size 20 color kg_muted pos (205,300)
    $ _ks_tier=kk_kelelahan_tier()
    vbox:
        pos (207,355) spacing 27
        for label,value in [("Kelelahan",_ks_tier[0]),("Energi",kk_lvl(body.get("energi",0))),("Kesehatan",kk_lvl(body.get("kesehatan",0)))]:
            vbox:
                spacing 3
                text label font kg_body size 22 color kg_muted
                text value font kg_hand size 38 color kg_ink
    text "Pola pilihanmu" font kg_body size 20 color kg_muted pos (205,756)
    text kk_persona_label() font kg_hand size 28 color kg_ink pos (205,794) xmaximum 445
    fixed:
        pos (194,894)
        use ks_button("Riwayat transaksi",Show("kk_wallet"),450,"ks_open_wallet")
    text "Orang yang kamu kenal" font kg_hand size 39 color kg_ink pos (803,218)
    text "Ketuk kartu untuk membaliknya." font kg_body size 19 color kg_muted pos (808,277)
    viewport:
        pos (790,326) xysize (950,570) mousewheel True draggable renpy.variant("touch") scrollbars "vertical" arrowkeys True
        grid 4 _ks_rows:
            spacing 14
            for index,cid in enumerate(_ks_people):
                button:
                    id ("ks_contact_"+cid)
                    xysize (216,236) padding (0,0) background ks_art("contact",216,236)
                    action SetScreenVariable("contact",None if contact == cid else cid)
                    at ks_motion(1 if index%2 else -1,index*.015)
                    if contact == cid:
                        text KK_CHARS[cid]["nama"] font kg_hand size 24 color kg_ink pos (22,33) xmaximum 174
                        text ks_last_met(cid) font kg_body size 21 color kg_muted pos (22,106) xmaximum 172
                    else:
                        text kg_initial(cid) font kg_hand size 51 color KK_CHARS[cid]["warna"] xalign .5 ypos 43
                        text KK_CHARS[cid]["nama"] font kg_hand size 24 color kg_ink pos (20,139) xmaximum 178
            for i in range(_ks_rows*4-len(_ks_people)):
                null width 216 height 236

screen kk_wallet():
    modal True
    zorder 95
    default page = 0
    key "game_menu" action Hide("kk_wallet")
    $ end=len(kk_transactions)-page*7
    $ entries=kk_transactions[max(0,end-7):end]
    add Solid("#21182CEB")
    add ks_art("object-letter",650,240) pos (110,276) at ks_motion(-5,.02)
    text "Yang datang,\nyang pergi." font kg_title size 77 color "#F5E8D8" pos (142,98)
    text "Saldo sekarang" font kg_body size 24 color kg_ink pos (181,338)
    text ("¥"+"{:,}".format(saldo)) font kg_hand size 68 color kg_ink pos (179,395) xmaximum 570
    text "Riwayat transaksi" font kg_hand size 35 color "#D4B6CF" pos (168,601)
    text "Setiap pengeluaran ada catatannya." font kg_body size 23 color "#BCA5BE" pos (168,658) xmaximum 555
    add ks_art("receipt",850,800) pos (870,135) at ks_motion(1,.04)
    text "CATATAN KOUSEIKAN" font kg_body bold True size 25 color kg_ink pos (940,181)
    text ("Lembar "+str(page+1).zfill(2)) font kg_body size 19 color kg_muted pos (941,229)
    viewport:
        pos (924,280) xysize (730,545) mousewheel True draggable renpy.variant("touch") scrollbars "vertical"
        vbox:
            spacing 21
            if not entries:
                text "Belum ada transaksi yang tercatat." font kg_hand size 28 color kg_muted
            for month,day,description,amount,balance in reversed(entries):
                vbox:
                    spacing 5
                    text (str(day)+" "+KK_BACKBONE[month-1][1]) font kg_body size 17 color kg_muted
                    text description font kg_hand size 27 color kg_ink xmaximum 672
                    hbox:
                        spacing 30
                        text ("{}¥{:,}".format("+" if amount > 0 else "-",abs(amount))) font kg_body bold True size 23 color ("#497D70" if amount > 0 else "#A05176") xsize 260
                        text ("Saldo ¥{:,}".format(balance)) font kg_body size 20 color kg_muted
    hbox:
        pos (944,943) spacing 15
        if page:
            use ks_button("Lebih baru",SetScreenVariable("page",page-1),240,"ks_wallet_newer")
        if end > 7:
            use ks_button("Lebih lama",SetScreenVariable("page",page+1),240,"ks_wallet_older")
    use ks_close(Hide("kk_wallet"))

screen kk_cutscene_gallery():
    tag menu
    default page = 0
    default selected_scene = 0
    key "game_menu" action Return()
    $ entries=kg_replays()
    $ _ks_scenes=entries[page*5:page*5+5]
    $ current=_ks_scenes[min(selected_scene,len(_ks_scenes)-1)] if _ks_scenes else None
    add ks_art("desk",1920,1080)
    text "Ruang kenangan." font kg_title size 87 color kg_ink pos (148,53)
    text "Galeri adegan yang sudah kamu alami." font kg_body size 22 color kg_muted pos (157,154)
    use ks_close(Return())
    fixed:
        pos (173,244) xysize (930,640) at ks_motion(-2,.02)
        add ks_art("object-film",930,640)
        if current:
            $ _ks_did,_ks_place=ks_event_place(current)
            add kg_district_picture(_ks_did,737,360) pos (98,99)
            text current["title"] font kg_hand size 44 color "#FFF2E9" pos (102,499) xmaximum 755
        else:
            text "Kenangan menunggu\nuntuk direkam." font kg_hand size 51 color "#F9EBED" pos (135,198) xmaximum 650 text_align .5
    if current:
        text current["title"] font kg_hand size 48 color kg_ink pos (1225,292) xmaximum 525
        text _ks_place font kg_body size 25 color kg_muted pos (1230,451) xmaximum 510
        fixed:
            pos (1216,571)
            use ks_button("Putar adegan",Replay("kk_gui_replay",scope={"kk_replay_eid":current["id"],"kk_replay_host":kk_host or "yutaka"},locked=False),500,"kg_replay_"+current["id"])
        text "Pilih potongan film di bawah\nuntuk melihat kenangan lainnya." font kg_body size 23 color kg_muted pos (1233,709) xmaximum 485
    else:
        text "Belum ada adegan terbuka." font kg_hand size 39 color kg_muted pos (1208,381) xmaximum 530
    hbox:
        pos (225,887) spacing 22
        for index,entry in enumerate(_ks_scenes):
            button:
                id ("ks_scene_"+str(index))
                xysize (265,105) padding (20,14)
                background ks_art("object-note",265,105)
                action SetScreenVariable("selected_scene",index)
                at ks_motion(-2 if index%2 else 2,index*.02)
                text entry["title"] font kg_hand size 25 color kg_ink xmaximum 218
    hbox:
        pos (1500,956) spacing 14
        if page:
            use ks_button("<",[SetScreenVariable("page",page-1),SetScreenVariable("selected_scene",0)],95)
        if (page+1)*5 < len(entries):
            use ks_button(">",[SetScreenVariable("page",page+1),SetScreenVariable("selected_scene",0)],95)

screen history():
    tag menu
    key "game_menu" action Return()
    add ks_art("desk",1920,1080)
    text "Yang sempat terucap." font kg_title size 81 color kg_ink pos (150,54)
    text "Riwayat percakapan" font kg_body size 21 color kg_muted pos (159,154)
    use ks_close(Return())
    viewport:
        pos (240,242) xysize (1450,730) yinitial 1.0 mousewheel True draggable True arrowkeys True pagekeys True scrollbars "vertical"
        vbox:
            spacing 26 xsize 1375
            if not _history_list:
                text "Belum ada kata yang tersimpan." font kg_hand size 37 color kg_muted
            for index,h in enumerate(_history_list):
                hbox:
                    spacing 24
                    vbox:
                        spacing 8 xsize 180
                        text str(index+1).zfill(2) font kg_title size 55 color "#AD8FA5"
                        text (h.who or "Narasi") substitute False font kg_hand size 24 color "#896182" xmaximum 178
                    frame:
                        xsize 1130 padding (48,32)
                        background Frame("gui/kouseikan/secondary/letter.png",85,45,85,45)
                        text renpy.filter_text_tags(h.what,allow=["b","i","u","ruby","rt"]) substitute False font kg_body size 29 color kg_ink xmaximum 1020 line_spacing 7

screen confirm(message,yes_action,no_action):
    modal True
    zorder 200
    key "game_menu" action no_action
    add Solid("#17112CD9")
    $ _ks_h=min(680,max(370,220+ks_text_lines(message,800,30)*46))
    frame:
        align (.5,.5) xysize (1050,_ks_h) padding (85,55)
        background Frame("gui/kouseikan/secondary/letter.png",90,45,90,50)
        at ks_motion(-1)
        vbox:
            spacing 26
            text "Sebentar…" font kg_title size 58 color kg_ink
            text message font kg_body size 30 color kg_ink xmaximum 800
            hbox:
                spacing 30
                use ks_button("Tidak",no_action,340,"ks_confirm_no")
                use ks_button("Ya",yes_action,340,"ks_confirm_yes")

screen notify(message):
    zorder 120
    frame:
        xpos 1245 ypos 120 xsize 600 padding (32,21)
        background Frame("gui/kouseikan/secondary/ticket.png",85,25,45,25)
        at ks_motion(1)
        text "[message!tq]" font kg_body size 25 color kg_ink xmaximum 530
    timer 3.0 action Hide("notify")

screen kk_titlecard(title,sub=""):
    modal True
    add Solid("#211827F2")
    add ks_art("object-letter",1100,370) pos (400,281) at ks_motion(-4,.05)
    text title font kg_title size 73 color "#FFF3E7" xalign .5 ypos 152 xmaximum 1450 text_align .5
    text sub font kg_hand size 34 color kg_ink pos (590,422) xmaximum 750 text_align .5
    fixed:
        pos (785,802)
        use ks_button("Lanjut",Return(),350,"ks_title_continue")

screen kk_ending_card(e):
    add ks_art("desk",1920,1080)
    text "Di ujung benang." font kg_title size 80 color kg_ink pos (154,61)
    add ks_art("letter",1400,740) pos (260,203) at ks_motion(-1)
    viewport:
        pos (383,275) xysize (1130,520) mousewheel True draggable True arrowkeys True scrollbars "vertical"
        vbox:
            spacing 30
            text e["name"] font kg_hand size 48 color kg_ink xmaximum 1070
            text e.get("body","") font kg_body size 29 color kg_ink xmaximum 1070 line_spacing 8
    hbox:
        pos (535,893) spacing 30
        use ks_button("Lanjut",Return(),360)
        use ks_button("Menu utama",MainMenu(),360)

screen ks_phone_tab(tab):
    frame:
        pos (15,437) xysize (470,400) padding (24,22)
        background Frame("gui/kouseikan/secondary/letter.png",40,35,45,45)
        vbox:
            spacing 12
            text ("Jejak teman" if tab == "location" else "Surat masuk") font kg_hand size 35 color kg_ink
            if tab == "location":
                viewport:
                    xysize (420,252) mousewheel True draggable True scrollbars "vertical"
                    vbox:
                        spacing 15 xsize 388
                        for cid in KK_PHONE_ORDER:
                            $ where,district_name=kk_phone_locate(cid)
                            hbox:
                                spacing 12
                                text kg_initial(cid) font kg_hand size 38 color KK_CHARS[cid]["warna"] xsize 33
                                vbox:
                                    spacing 2 xsize 334
                                    text KK_CHARS[cid]["nama"] font kg_hand size 24 color kg_ink
                                    text where font kg_body size 19 color kg_muted xmaximum 330
                use ks_button("Lihat peta",[Hide("kk_phone_locator"),Show("kg_map_viewer")],402)
            else:
                $ _ks_messages=kk_incoming_messages() if kk_host else []
                if not _ks_messages:
                    text "Belum ada surat baru." font kg_hand size 27 color kg_muted
                    text "Lanjutkan harimu; pesan akan datang pada waktunya." font kg_body size 21 color kg_muted xmaximum 380
                else:
                    for item in _ks_messages[:4]:
                        text (KK_CHARS.get(item[0],{}).get("nama",item[0].replace("_"," ").title())) font kg_hand size 25 color kg_ink
                    text "Pesan diterima saat kamu melanjutkan aktivitas." font kg_body size 20 color kg_muted xmaximum 380

screen ks_link(caption,operation,width=None,active=False,first=False):
    button:
        style "ks_button"
        xsize width
        action operation
        selected active
        default_focus first
        text caption style "ks_button_text" xmaximum ((width-60) if width else 650)


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
                use ks_phone_tab(tab)
        button:
            pos (260,936) xysize (170,40) background None
            action Hide("kk_phone_locator")
            alt "Tutup HP"
            add Solid("#E0D5EA") xysize (160,7) yalign .5
    fixed:
        pos (1340,65)
        use kg_tool("close","Tutup HP",Hide("kk_phone_locator"))


screen kk_location_view(distrik, lokasi):
    tag kk_world
    $ present = kk_present_here(distrik, lokasi)
    $ acts = kk_acts_at(lokasi)
    $ home = "Apartemen Yutaka" if kk_host == "yutaka" else "Rumah Amamiya"
    add ks_art("desk",1920,1080)
    add ks_art("letter",850,780) pos (70,135)
    add kg_district_picture(distrik,675,380) pos (150,486)
    use kk_hud
    # Identitas tempat (kiri)
    vbox:
        xpos kk_margin ypos 150 spacing 8 xsize 820
        text KK_DISTRICT_NAME[distrik] style "kk_caption"
        text lokasi style "kk_heading"
        add Solid(kk_accent) xysize (72, 4)
        null height 6
        text KK_LOC_AMBIENCE.get(lokasi, "Tempat biasa. Dunia tetap berjalan di tempat lain.") style "kk_caption" xmaximum 760

    # Siapa di sini + aktivitas (kanan)
    viewport:
        pos (980, 150) xysize (860, 780)
        mousewheel True draggable renpy.variant("touch") arrowkeys True scrollbars "vertical"
        vbox:
            spacing 28 xsize 820
            vbox:
                spacing 10
                text "Temui seseorang" size 32 color kg_muted font kg_hand
                if present:
                    for cid in present:
                        $ meta = KK_CHARS[cid]
                        button:
                            id ("qa_"+cid)
                            style "ks_button" xysize (800, 96) action Return(("talk", cid))
                            hbox:
                                yalign .5 spacing 18
                                add Solid(kk_line) xysize (10, 44) yalign .5
                                text meta["nama"] size 25 bold True yalign .5
                else:
                    text "Tidak ada orang yang kau kenal di sini sekarang." style "kk_caption"
            vbox:
                spacing 10
                text "Isi waktumu" size 32 color kg_muted font kg_hand
                for aid, a in acts:
                    button:
                        style "ks_button" xysize (800, 104) action Return(("act", aid)) sensitive a["ok"]()
                        hbox:
                            yalign .5 spacing 16
                            text a["label"] size 24 bold True yalign .5 xsize 265
                            text a["desc"] style "kk_caption" yalign .5 xmaximum 390
                if lokasi == "Stasiun Kouseikan-mae" and kk_onsen_dates():
                    use ks_link("Berangkat ke penginapan onsen", Return(("travel", None)), 800)
                if distrik == "onsen":
                    use ks_link("Duduk sejenak di penginapan", Return(("rest", None)), 800)
                if kk_art_studio_open(lokasi):
                    use ks_link("Bicarakan sketsa dengan Haruka", Return(("portfolio", None)), 800)
                if kk_can_sketch(lokasi):
                    use ks_link("Latihan di buku sketsa", Return(("draw", None)), 800)
                if kk_can_sit_with_miyuki(lokasi):
                    button:
                        id "miyuki_library_seat"
                        style "ks_button" action Return(("sit_miyuki", None))
                        text "Duduk di sebelah Miyuki" style "ks_button_text"
                if kk_unfinished_board(lokasi):
                    button:
                        id "unfinished_board"
                        style "ks_button" xysize (800, 104) action Return(("board", None))
                        text "Perhatikan papan yang belum dibereskan" style "ks_button_text" yalign .5
                if lokasi == home and kk_desk_event(lokasi):
                    use ks_link("Periksa meja di kamar", Return(("desk", None)), 800)
                if lokasi == home:
                    use ks_link("Beristirahat di kamar", Return(("sleep", None)), 800)
                if not acts and not kk_unfinished_board(lokasi) and not kk_art_studio_open(lokasi) and lokasi != home and distrik != "onsen" and not (lokasi == "Stasiun Kouseikan-mae" and kk_onsen_dates()):
                    text "Tidak ada aktivitas khusus di sini." style "kk_caption"
    fixed:
        pos (kk_margin, 980)
        use ks_link("‹ Pergi dari sini", Return(("leave", None)))


# ══════════════════════════════════════════════════════════════════════════
# ALUR navigasi dunia
# ══════════════════════════════════════════════════════════════════════════
