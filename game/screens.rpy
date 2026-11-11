# Kouseikan — UI custom. Anti-mainstream: dialog bukan bar bawah penuh, tipografi berani,
# komposisi asimetris, blok warna, aksen tunggal. Placeholder art (color-field + watermark).

################################################################################
## Latar placeholder editorial
################################################################################
screen kk_set(char, loc=""):
    zorder -10
    $ meta = KK_CHARS.get(char, {"nama":"KOUSEIKAN","warna":kk_accent})
    $ fam = meta["nama"].split()[0].upper()
    add kk_ink
    add Solid(meta["warna"]) xpos 0.54 ysize 1.0 xsize 0.46 alpha 0.13
    add Solid(kk_ink2) xpos 0.0 ysize 1.0 xsize 0.10
    text fam:
        size 164 bold True color (meta["warna"] + "1e")
        xpos 0.985 xanchor 1.0 ypos 0.40 yanchor 0.5
    add Solid(kk_accent) xpos 120 ypos 118 xsize 60 ysize 5
    if loc:
        text loc size 19 color kk_dim font kk_mono xpos 120 ypos 134

################################################################################
## TITLECARD — layar judul/jeda tengah, klik untuk lanjut (bukan statement say)
################################################################################
screen kk_titlecard(title, sub=""):
    modal True
    button:
        action Return()
        background None
        xysize (config.screen_width, config.screen_height)
    vbox:
        align (0.5, 0.5) spacing 10
        text title size 64 color kk_bone bold True xalign 0.5 text_align 0.5
        if sub:
            text sub size 20 color kk_dim xalign 0.5 text_align 0.5
    add Text("klik untuk lanjut", size=14, color=kk_dim) xalign 0.5 yalign 0.96

################################################################################
## HUD atas (waktu + akses cepat)
################################################################################
screen kk_hud():
    zorder 50
    $ mt = kk_month_tuple()
    $ tier = kk_kelelahan_tier()
    # garis atas
    add Solid(kk_line) xpos 0 ypos 64 xsize 1.0 ysize 1
    hbox:
        xpos 120 ypos 24 spacing 22
        text "KOUSEIKAN" size 18 color kk_bone bold True
        text "·" size 18 color kk_dim
        text "[mt[0]] [mt[2]]" size 18 color kk_accent font kk_mono
        text "[KK_SLOTS[kk_slot]]" size 18 color kk_dim font kk_mono
    hbox:
        xalign 1.0 xoffset -40 ypos 24 spacing 20
        textbutton "STATUS" action Show("kk_status") text_size 16 text_color kk_dim text_hover_color kk_accent
        textbutton "MENU" action ShowMenu("save") text_size 16 text_color kk_dim text_hover_color kk_accent
    if tier[1] >= 2:
        text ("● " + tier[0]) size 15 color kk_warn font kk_mono xalign 1.0 xoffset -40 ypos 48

################################################################################
## SAY — kartu dialog offset, bukan bar bawah
################################################################################
screen say(who, what):
    style_prefix "say"
    use kk_hud
    if who is not None:
        vbox:
            xpos 120 ypos 440 spacing 0
            frame:
                background Solid(kk_accent)
                padding (16, 5, 18, 6)
                text who id "who" size 19 color "#141017" bold True font kk_mono
            frame:
                background Solid("#15121ae8")
                xmaximum 880 padding (26, 20, 26, 24)
                text what id "what" size 27 color kk_bone line_spacing 7
    else:
        frame:
            xpos 160 ypos 470 xmaximum 820 background None padding (0,0,0,0)
            text what id "what" size 26 color kk_bone2 italic True line_spacing 7
    add Text("▶", size=18, color=kk_accent) xpos 980 ypos 560 at kk_blink

transform kk_blink:
    block:
        linear 0.7 alpha 0.2
        linear 0.7 alpha 1.0
        repeat

style say_dialogue is default

################################################################################
## CHOICE — menu default (prologue), ditata editorial kiri-atas
################################################################################
screen choice(items):
    style_prefix "choice"
    add Solid("#0b0a0e99")
    vbox:
        xpos 150 ypos 150 spacing 8
        for idx in range(len(items)):
            $ it = items[idx]
            button:
                action it.action
                background None padding (0, 8, 0, 8)
                at kk_hoverbar
                hbox:
                    spacing 20
                    text "{:02d}".format(idx+1) size 22 color kk_accent font kk_mono yalign 0.5
                    text it.caption size 27 color kk_bone yalign 0.5

################################################################################
## kk_choices — pilihan dari data event, mengembalikan key
################################################################################
screen kk_choices(ev):
    modal True
    add Solid("#0b0a0e99")
    vbox:
        xpos 150 ypos 150 spacing 8
        text "PILIH" size 15 color kk_dim font kk_mono
        null height 6
        for idx in range(len(ev["choices"])):
            $ c = ev["choices"][idx]
            button:
                action Return(c["key"])
                background None padding (0, 8, 0, 8)
                at kk_hoverbar
                hbox:
                    spacing 18
                    text c["key"] size 20 color kk_accent font kk_mono yalign 0.5 min_width 28
                    text c["label"] size 25 color kk_bone yalign 0.5 xmaximum 760

################################################################################
## Pemilihan rute
################################################################################
screen kk_route_select():
    add kk_ink
    text "PILIH TUBUH" size 20 color kk_dim font kk_mono xpos 120 ypos 120
    text "Rute awal, bukan batas orientasi." size 18 color kk_dim xpos 120 ypos 150
    hbox:
        xpos 120 ypos 230 spacing 40
        for hid, judul, sub, warna in [("yutaka","MALE ROUTE","Kisaragi Yutaka — host dominan, bisa BL","#4a7bf0"),("chiasa","FEMALE ROUTE","Amamiya Chiasa — host, kebanyakan yuri","#e4532b")]:
            button:
                action Return(hid)
                background Solid(kk_panel)
                hover_background Solid(kk_ink2)
                xsize 500 ysize 360 padding (34, 34, 34, 34)
                at kk_hoverbar
                vbox:
                    spacing 14
                    add Solid(warna) xsize 54 ysize 6
                    text judul size 40 color kk_bone bold True
                    text sub size 20 color kk_dim line_spacing 5

################################################################################
## HUB vertical slice
################################################################################
screen kk_hub_menu():
    add kk_ink
    use kk_hud
    text "SANDBOX" size 18 color kk_dim font kk_mono xpos 120 ypos 110
    text "Hari berjalan. Jadwal NPC tidak tetap. Kau tak wajib tidur." size 19 color kk_dim xpos 120 ypos 134
    vbox:
        xpos 150 ypos 210 spacing 6
        for lbl, act, sub in [
            ("Jalur Miyuki","miyuki","Mi03 Perpustakaan Malam · Mi05 Vila (hub risiko)"),
            ("Jalur Nagisa","nagisa","N03 Maket Hujan · N06 Yuuto"),
            ("Jelajah semua cabang","explore","190 event · 128 dinamis · 220 ending"),
            ("Timeskip ke Evaluasi (debug)","eval","loncat ke M36, resolver ending"),
        ]:
            button:
                action Return(act)
                background None padding (0,10,0,10)
                at kk_hoverbar
                vbox:
                    text lbl size 28 color kk_bone
                    text sub size 17 color kk_dim
    textbutton "STATUS & HUBUNGAN" action Show("kk_status") xpos 150 ypos 560 text_size 18 text_color kk_acc2 text_hover_color kk_bone

################################################################################
## STATUS overlay
################################################################################
screen kk_status():
    modal True
    add Solid("#0a090cde")
    frame:
        align (0.5, 0.5) xsize 1000 ysize 600 background Solid(kk_ink2) padding (40,34,40,34)
        vbox:
            spacing 4
            add Solid(kk_accent) xsize 54 ysize 6
            text "STATUS" size 34 color kk_bone bold True
            null height 10
            hbox:
                spacing 60
                # tubuh
                vbox:
                    spacing 6
                    text "TUBUH HOST" size 16 color kk_dim font kk_mono
                    $ tier = kk_kelelahan_tier()
                    text ("Kelelahan: " + tier[0]) size 22 color (kk_warn if tier[1]>=2 else kk_bone)
                    text ("Energi: " + str(body.get('energi',0))) size 20 color kk_bone2
                    text ("Kesehatan: " + str(body.get('kesehatan',0))) size 20 color kk_bone2
                    text ("Saldo: ¥" + "{:,}".format(saldo)) size 20 color kk_bone2
                    text ("Deviasi (tersembunyi): " + str(deviasi)) size 18 color kk_dim
                    null height 8
                    text "KEPRIBADIAN (dari pola pilihanmu)" size 16 color kk_dim font kk_mono
                    text kk_persona_label() size 19 color kk_bone2
                # hubungan
                vbox:
                    spacing 6
                    text "HUBUNGAN (kualitatif)" size 16 color kk_dim font kk_mono
                    for cid in ["koita","miyuki","nagisa","harumi","moeka","shiori","chiasa","yutaka"]:
                        if cid in rel:
                            $ m = KK_CHARS[cid]
                            hbox:
                                spacing 12
                                text m["nama"] size 19 color m["warna"] min_width 230
                                text ("Aff " + kk_lvl(kk_rel_get(cid,'aff')) + " · Trust " + kk_lvl(kk_rel_get(cid,'trust'))) size 17 color kk_bone2
            null height 16
            textbutton "TUTUP" action Hide("kk_status") text_size 20 text_color kk_accent

################################################################################
## JELAJAH semua cabang
################################################################################
screen kk_explorer():
    modal True
    default cur = "miyuki"
    add Solid("#0a090cf0")
    text "JELAJAH CABANG" size 30 color kk_bone bold True xpos 80 ypos 50
    text "Semua event autogenerated dari dokumen desain. Klik untuk mainkan." size 17 color kk_dim xpos 80 ypos 92
    # kolom rute
    vbox:
        xpos 80 ypos 150 spacing 4
        for rid, rnama, rsub in KK_ROUTES:
            $ ck = {"koita_bl":"koita"}.get(rid, rid)
            textbutton rnama:
                action SetScreenVariable("cur", ck)
                text_size 21 text_color (kk_accent if cur==ck else kk_bone2) text_hover_color kk_accent
        null height 14
        textbutton "‹ KEMBALI" action Return("back") text_size 18 text_color kk_dim text_hover_color kk_accent
    # kolom event
    viewport:
        xpos 420 ypos 150 xsize 820 ysize 500 mousewheel True scrollbars "vertical"
        vbox:
            spacing 2
            for ev in KK_EV_BY_CHAR.get(cur, []):
                button:
                    action Return(ev["id"])
                    background None padding (0,6,0,6)
                    at kk_hoverbar
                    hbox:
                        spacing 14
                        text ev["id"] size 17 color kk_accent font kk_mono min_width 60
                        text ev["month"] size 16 color kk_dim font kk_mono min_width 70
                        text ev["title"] size 20 color kk_bone xmaximum 560

################################################################################
## Kartu ENDING
################################################################################
screen kk_ending_card(e):
    add kk_ink
    $ warna = {"Romantis":kk_good,"Neutral":kk_dim,"Distorted":kk_warn,"Bad":kk_bad,"Broken":"#be123c","Koita":"#8e92ff","Khusus":kk_acc2}.get(e.get("type",""), kk_accent)
    add Solid(warna) xpos 120 ypos 150 xsize 60 ysize 6
    vbox:
        xpos 120 ypos 180 spacing 10 xmaximum 1000
        text e.get("type","").upper() size 18 color warna font kk_mono
        text e.get("code","") + "  " + e.get("name","") size 46 color kk_bone bold True
        null height 6
        text e.get("body","") size 23 color kk_bone2 line_spacing 7
        null height 10
        text "SYARAT: " + e.get("cond","") size 17 color kk_dim line_spacing 5 xmaximum 900
    hbox:
        xpos 120 ypos 600 spacing 30
        textbutton "LANJUT" action Return() text_size 22 text_color kk_accent
        textbutton "MENU UTAMA" action MainMenu(confirm=False) text_size 22 text_color kk_dim text_hover_color kk_bone

################################################################################
## GALERI ENDING (dari main menu)
################################################################################
screen kk_gallery():
    tag menu
    default sel = KK_ENDINGS[0]
    default grp = "SI"
    add kk_ink
    text "GALERI ENDING" size 34 color kk_bone bold True xpos 80 ypos 44
    text "220 ending · epilog komposit" size 18 color kk_dim xpos 80 ypos 88
    # grup
    hbox:
        xpos 80 ypos 128 spacing 16
        for g in ["SI","HP","KO","BL","MI","NA","HA","MO","SH","CH","CF","YH","YU","FO","NPC","X"]:
            textbutton g:
                action SetScreenVariable("grp", g)
                text_size 17 text_color (kk_accent if grp==g else kk_dim) text_hover_color kk_bone text_font kk_mono
    # daftar
    viewport:
        xpos 80 ypos 170 xsize 560 ysize 480 mousewheel True scrollbars "vertical"
        vbox:
            spacing 2
            for e in KK_ENDINGS:
                if e["code"].split("-")[1] == grp:
                    button:
                        action SetScreenVariable("sel", e)
                        background None padding (0,5,0,5)
                        at kk_hoverbar
                        hbox:
                            spacing 12
                            text e["code"] size 16 color kk_accent font kk_mono min_width 86
                            text e["name"] size 19 color kk_bone xmaximum 400
    # detail
    frame:
        xpos 680 ypos 170 xsize 560 ysize 480 background Solid(kk_ink2) padding (28,24,28,24)
        vbox:
            spacing 8
            $ warna = {"Romantis":kk_good,"Neutral":kk_dim,"Distorted":kk_warn,"Bad":kk_bad,"Broken":"#be123c","Koita":"#8e92ff","Khusus":kk_acc2}.get(sel.get("type",""), kk_accent)
            add Solid(warna) xsize 48 ysize 5
            text sel["type"].upper() size 15 color warna font kk_mono
            text sel["code"] + " " + sel["name"] size 27 color kk_bone bold True
            text sel.get("body","") size 19 color kk_bone2 line_spacing 6
            text "SYARAT: " + sel.get("cond","") size 15 color kk_dim line_spacing 5
    textbutton "‹ MENU" action Return() xpos 80 ypos 664 text_size 18 text_color kk_dim text_hover_color kk_accent

################################################################################
## MAIN MENU
################################################################################
screen main_menu():
    tag menu
    add kk_ink
    add Solid(kk_accent) xpos 0.60 ypos 0.0 ysize 1.0 xsize 8
    add Solid(kk_panel) xpos 0.62 ypos 0.0 ysize 1.0 xsize 0.38 alpha 0.5
    text "光星館" size 120 color kk_line xpos 0.98 xanchor 1.0 ypos 0.5 yanchor 0.5
    vbox:
        xpos 130 ypos 200 spacing 2
        add Solid(kk_accent) xsize 64 ysize 7
        null height 14
        text "KOUSEIKAN" size 86 color kk_bone bold True
        text "PROTOTIPE · SISTEM CABANG · 18+" size 20 color kk_dim font kk_mono
    vbox:
        xpos 134 ypos 440 spacing 4
        for lbl, act in [("MULAI", Start()), ("MUAT", ShowMenu("load")), ("GALERI ENDING", ShowMenu("kk_gallery")), ("PENGATURAN", ShowMenu("preferences")), ("KELUAR", Quit(confirm=False))]:
            textbutton lbl:
                action act
                text_size 30 text_color kk_bone2 text_hover_color kk_accent
                at kk_hoverbar

################################################################################
## GAME MENU (save/load/prefs) — bingkai minimal
################################################################################
screen game_menu(title, scroll=None):
    add kk_ink
    add Solid(kk_accent) xpos 80 ypos 70 xsize 54 ysize 6
    text title size 40 color kk_bone bold True xpos 80 ypos 90
    frame:
        xpos 80 ypos 160 xsize 1120 ysize 490 background None
        transclude
    use kk_return_bar

screen kk_return_bar():
    hbox:
        xpos 80 ypos 668 spacing 26
        textbutton "‹ KEMBALI" action Return() text_size 18 text_color kk_dim text_hover_color kk_accent
        textbutton "MENU UTAMA" action MainMenu() text_size 18 text_color kk_dim text_hover_color kk_accent

screen save():
    tag menu
    use game_menu("SIMPAN"):
        use kk_file_slots(FileAction)

screen load():
    tag menu
    use game_menu("MUAT"):
        use kk_file_slots(FileLoad)

screen kk_file_slots(act):
    grid 3 2:
        spacing 16
        for i in range(1, 7):
            button:
                action act(i)
                xsize 356 ysize 220 background Solid(kk_ink2) hover_background Solid(kk_panel)
                padding (14,14,14,14)
                vbox:
                    text "SLOT " + str(i) size 16 color kk_dim font kk_mono
                    add FileScreenshot(i) xsize 320
                    text FileTime(i, empty="— kosong —") size 15 color kk_dim

screen preferences():
    tag menu
    use game_menu("PENGATURAN"):
        vbox:
            spacing 20
            hbox:
                spacing 30
                text "TEKS" size 18 color kk_dim font kk_mono yalign 0.5
                bar value Preference("text speed") xsize 400 yalign 0.5
            hbox:
                spacing 30
                text "MUSIK" size 18 color kk_dim font kk_mono yalign 0.5
                bar value Preference("music volume") xsize 400 yalign 0.5
            hbox:
                spacing 30
                text "SUARA" size 18 color kk_dim font kk_mono yalign 0.5
                bar value Preference("sound volume") xsize 400 yalign 0.5
            textbutton "Layar penuh" action Preference("display", "toggle") text_size 20 text_color kk_bone2 text_hover_color kk_accent

################################################################################
## Pelengkap
################################################################################
screen quick_menu():
    pass

screen confirm(message, yes_action, no_action):
    modal True
    add Solid("#0a090cde")
    frame:
        align (0.5,0.5) background Solid(kk_ink2) padding (40,34,40,34)
        vbox:
            spacing 24
            text message size 24 color kk_bone xmaximum 700
            hbox:
                spacing 30 xalign 0.5
                textbutton "YA" action yes_action text_size 22 text_color kk_accent
                textbutton "TIDAK" action no_action text_size 22 text_color kk_dim text_hover_color kk_bone
    key "game_menu" action no_action

screen skip_indicator():
    zorder 100
    if config.skipping:
        text "SKIP ▶▶" size 15 color kk_accent font kk_mono xalign 0.5 ypos 20

screen notify(message):
    zorder 100
    frame:
        xalign 0.5 ypos 40 background Solid(kk_accent) padding (18,8,18,8)
        text "[message!tq]" size 16 color "#141017" bold True
    timer 3.0 action Hide("notify")

screen nvl(dialogue, items=None):
    use say(None, "\n".join([d.what for d in dialogue]))

style default:
    font kk_body
    color kk_bone
