# Driver is copied to a temporary game by run_living.py, never into production.
init python:
    import os
    if os.name == 'nt' and os.environ.get('KK_CAPTURE'):
        import ctypes
        ctypes.windll.user32.SetProcessDPIAware()
    def kk_test_romance():
        return kk_host == "yutaka" or bool(os.environ.get("KK_ART_WIN"))

    def kk_test_input(name):
        if os.environ.get("KK_CAPTURE"):
            size = os.environ["KK_SIZE"]
            if name == "main_menu" and not os.environ.get("KK_SIZED"):
                os.environ["KK_SIZED"] = "1"
                if size == "1920x1080":
                    renpy.run(Preference("display","fullscreen"))
                else:
                    renpy.set_physical_size(tuple(int(n) for n in size.split("x")))
                return
            if name == "kk_location_view":
                physical = tuple(renpy.get_physical_size())
                expected = tuple(int(n) for n in size.split("x"))
                # The 16:9 viewport can round an odd drawable dimension down a pixel.
                assert all(abs(a-b) <= 1 for a,b in zip(physical,expected)), (physical, expected)
                renpy.screenshot(os.path.join(os.environ["KK_CAPTURE"], "Hanami-"+size+".png"))
                return renpy.run(Return())
            if name == "main_menu":
                return renpy.run(Start("kk_capture_hanami"))
        if name == "main_menu":
            return renpy.run(Start())
        if name == "kk_titlecard":
            return renpy.run(Return())
        if name == "kk_world_district":
            assert not kk_debug_tools
            store.kk_world_seed = next(s for s in range(1,200) if int.from_bytes(hashlib.sha256(("%d/0/1/nagisa"%s).encode()).digest()[:4],"big") % 100 >= 15)
            return renpy.run(renpy.get_displayable(name,"qa_d1").action)
        if name == "kk_world_location":
            return renpy.run(renpy.get_displayable(name,"qa_Gedung Arsitektur").action)
        if name == "kk_location_view":
            if getattr(store,"kk_test_seat",False):
                return renpy.run(renpy.get_displayable(name,"miyuki_library_seat").action)
            if getattr(store,"kk_test_board",False):
                return renpy.run(renpy.get_displayable(name,"unfinished_board").action)
            if getattr(store,"kk_test_speaker",None):
                return renpy.run(renpy.get_displayable(name,"qa_"+kk_test_speaker).action)
            if kk_done("N01") and os.environ.get("KK_FAMILY_CASE") == "clinic":
                return renpy.run(Jump("kk_test_clinic"))
            if kk_done("N01") and os.environ.get("KK_FAMILY_CASE"):
                return renpy.run(Jump("kk_test_family_years"))
            if kk_done("N01"):
                return renpy.run(Jump("kk_sandbox_test"))
            return renpy.run(renpy.get_displayable(name,"qa_nagisa").action)
        if name == "kk_route_select":
            return renpy.run(Return(os.environ["KK_HOST"]))
        if name == "say":
            renpy.queue_event("dismiss")
        if name == "choice":
            items = renpy.get_screen("choice").scope["items"]
            selected = next((item for item in items if item.caption.startswith("Perlambat permainanmu")), items[0])
            if kk_test_romance():
                selected = next((item for item in items if item.caption.startswith(("Tawarkan membuat percobaan", "Tanyakan apa yang ia rasakan", "Teruskan sampai pagi", "Ambil proyeknya", "Cari orang lain untuk mengerjakannya", "Minta ia mengajarimu membuat garis"))),selected)
            caption = getattr(store,"kk_test_family_caption",None)
            if caption:
                selected = next(item for item in items if item.caption == caption)
            return renpy.run(selected.action)
        if name == "kk_choice_panel":
            screen = renpy.get_screen("kk_choice_panel")
            if screen:
                rows = screen.scope["rows"]
                selected = next((row for row in rows if row[0].startswith("Perlambat permainanmu")), rows[0])
                if kk_test_romance():
                    selected = next((row for row in rows if row[0].startswith(("Tawarkan membuat percobaan", "Tanyakan apa yang ia rasakan", "Teruskan sampai pagi", "Ambil proyeknya", "Cari orang lain untuk mengerjakannya", "Minta ia mengajarimu membuat garis"))), selected)
                selected = next((row for row in rows if kk_test_romance() and row[0].startswith("Tawarkan pergi bersama")), selected)
                caption = getattr(store,"kk_test_family_caption",None)
                if caption:
                    selected = next((row for row in rows if row[0] == caption), None)
                    assert selected, 'Missing choice %r among %r' % (caption, [row[0] for row in rows])
                return renpy.run(selected[1])
        if name == "kk_wallet":
            scope = renpy.get_screen(name).scope
            entries = scope["entries"]
            if scope["page"] == 0:
                assert len(entries) == 7 and entries[-1][4] == saldo
                if os.environ.get("KK_CAPTURE"):
                    renpy.screenshot(os.path.join(os.environ["KK_CAPTURE"], "Transaksi-"+os.environ["KK_SIZE"]+".png"))
                return renpy.run(SetScreenVariable("page", 1))
            assert entries and entries[-1] == kk_transactions[-8]
            return renpy.run(Return())
        if name == "kk_ending_card":
            return renpy.run(Return())

    def kk_test_at(month, day, slot):
        # Advance via the production day hook, never set events or missed flags.
        while (kk_bulan,kk_hari_n) < (month,day):
            kk_new_day()
        store.kk_slot = slot
        store.kk_minute = 0

    def kk_test_expect(name,check):
        with open(os.path.join(config.basedir,"progress.txt"),"a",encoding="utf8") as f:
            f.write(name + "\n")
        assert check, name

label kk_sandbox_test:
    $ kk_test_expect("Host, calendar and district-location-talk loop", kk_host == os.environ["KK_HOST"] and kk_hari_n == 7 and kk_hari == "Senin" and _lokasi == "Gedung Arsitektur")
    $ kk_test_expect("Host-specific opening", kk_done("Y01") == (kk_host == "yutaka") and kk_done("C01") == (kk_host == "chiasa"))
    $ kk_test_expect("Host absent from NPC list", kk_daily_place(kk_host) is None)
    $ kk_test_expect("No duplicate effect", kk_done("N01") and not kk_record_choice("N01","B") and kk_rel_get("nagisa","aff") == 23)
    $ kk_test_expect("Acknowledged sham resolves to the honest ending", kk_miyuki_sham_ending(palsu=True, diakui=True) == "E-MI-13")
    $ kk_test_expect("Exposed sham resolves to the broken ending", kk_miyuki_sham_ending(palsu=True, diakui=False, terbongkar=True) == "E-MI-14")
    $ kk_test_expect("No sham no sham ending", kk_miyuki_sham_ending(palsu=False) is None)
    $ balance_before = saldo
    call kk_do_activity("Kantin Pusat","makan")
    $ kk_test_expect("Meal", saldo == balance_before - 800 and body["lapar"] < 20)
    call kk_test_seek_talk("K01","koita","d1","Gedung Sastra","Amati dan catat polanya diam-diam.",1)
    $ kk_test_expect("Reading Koita's pattern is logged", kk_done("K01") and kk_has("pola_koita_dikenal"))
    if kk_host == "yutaka":
        $ y02_before = kk_get("curiga_chiasa",0)
        $ kk_test_expect("Y02 pending on the first Amamiya visit", "Y02" in kk_pending_enter("d2","Rumah Amamiya"))
        $ kk_test_family_caption = "Masuk saja seolah rumah sendiri."
        call kk_play_scene("Y02")
        $ kk_test_family_caption = None
        $ kk_test_expect("Barging in raises Chiasa's suspicion", kk_done("Y02") and kk_get("curiga_chiasa",0) == y02_before + 10)
    if kk_host == "chiasa":
        $ c02_before = kk_get("curiga_koita",0)
        $ kk_test_expect("C02 pending at breakfast", "C02" in kk_pending_enter("d2","Rumah Amamiya"))
        $ kk_test_family_caption = "Panggil namanya saja."
        call kk_play_scene("C02")
        $ kk_test_family_caption = None
        $ kk_test_expect("Wrong name raises Koita's suspicion", kk_done("C02") and kk_get("curiga_koita",0) == c02_before + 8)
    $ kk_test_at(1,19,0)
    $ kk_world_seed = next(n for n in range(1,200) if int.from_bytes(hashlib.sha256(("%d/%d/0/harumi" % (n,kk_elapsed_days)).encode()).digest()[:4],"big") % 100 >= 8 and int.from_bytes(hashlib.sha256(("%d/%d/1/miyuki" % (n,kk_elapsed_days)).encode()).digest()[:4],"big") % 100 >= 10)
    call kk_do_talk("d1","Gedung Sains & Lab","harumi")
    $ kk_test_expect("Science library before picnic", kk_done("H01"))
    $ kk_test_at(1,19,1)
    if kk_daily_place("miyuki") != "Taman Kampus":
        $ kk_test_at(1,19,2)
    if kk_daily_place("miyuki") != "Taman Kampus":
        $ kk_test_at(1,20,1)
    $ kk_test_expect("Hanami", kk_pending_enter("d1","Taman Kampus") == ["Mi01"])
    call kk_play_scene("Mi01")
    $ kk_test_at(1,20,1)
    $ kk_world_seed = next(seed for seed in range(1,500) if all(int.from_bytes(hashlib.sha256(("%d/%d/1/%s" % (seed, kk_elapsed_days, who)).encode()).digest()[:4], "big") % 100 >= pct for who,pct in (("moeka",30),("shiori",5))))
    $ spring_cid = "shiori" if kk_host == "yutaka" else "moeka"
    $ spring_id = "S01" if kk_host == "yutaka" else "Mo01"
    $ kk_test_expect("Hanami contextual conversation", kk_pending_talk(spring_cid,"d1","Taman Kampus") == [spring_id])
    call kk_do_talk("d1","Taman Kampus",spring_cid)
    $ kk_test_expect("Hanami recorded", kk_done(spring_id))
    $ test_april_balance = saldo
    $ kk_test_at(2,3,0)
    $ test_income = 150000 if kk_host == "yutaka" else 100000
    $ kk_test_expect("Monthly income once, royalties separate", saldo == test_april_balance + test_income and sum(t[3] for t in kk_transactions if t[0] == 2) == test_income and any(t[2] == "Royalti ilustrasi" for t in kk_transactions) == (kk_host == "chiasa"))
    $ kk_test_expect("Meal retained in ledger", any(t[2:4] == ("Makan",-800) for t in kk_transactions))
    $ kk_world_seed = next(seed for seed in range(1,1000) if all(int.from_bytes(hashlib.sha256(("%d/%d/%d/%s" % (seed, kk_elapsed_days, slot, who)).encode()).digest()[:4], "big") % 100 >= pct for slot,who,pct in ((0,"moeka",30),(1,"shiori",5),(2,"miyuki",10),(3,"nagisa",15))))
    $ kk_test_expect("Invitation at station", kk_pending_talk("moeka","d5","Stasiun Kouseikan-mae") == ["Mo02"])
    if kk_host == "yutaka":
        call kk_do_talk("d5","Stasiun Kouseikan-mae","moeka")
        $ spring_before = kk_get("respek_shiori")
        call kk_do_talk("onsen","Lobi ryokan","shiori")
        $ kk_test_expect("Shogi remembered", kk_done("S02") and kk_get("respek_shiori") > spring_before)
        call kk_do_talk("onsen","Dapur ryokan","miyuki")
        call kk_do_talk("onsen","Ruang bersama ryokan","nagisa")
        $ kk_test_expect("Ryokan dinner and night", kk_done("Mi02") and kk_done("N02"))
    if kk_host == "yutaka":
        while kk_daily_place("nagisa") != "Ruang bersama ryokan":
            $ kk_advance()
            $ kk_test_expect("Replay within trip", kk_onsen_dates())
        call kk_do_talk("onsen","Ruang bersama ryokan","nagisa")
        $ kk_test_expect("Losing on purpose leads to replay", kk_done("N-D08"))
    $ kk_test_at(2,7,0)
    $ kk_test_expect("Holiday closes; absence persists", not kk_onsen_dates() and ("S02" in kk_missed) == (kk_host == "chiasa"))
    $ kk_test_at(3,1,1)
    while not kk_pending_talk("harumi","d1","Gedung Sains & Lab"):
        $ kk_advance()
        $ kk_test_expect("Rain tea bounded", kk_bulan == 3)
    $ tea_trust = kk_rel_get("harumi","trust")
    $ kk_test_speaker = "harumi"
    $ kk_test_family_caption = "Puji rasanya dengan jujur."
    call screen kk_location_view("d1","Gedung Sains & Lab")
    $ kk_test_expect("Rain tea button", _return == ("talk","harumi"))
    call kk_do_talk("d1","Gedung Sains & Lab","harumi")
    $ kk_test_speaker = None
    $ kk_test_family_caption = None
    $ kk_test_expect("Rain tea recorded, trust up", kk_done("H02") and kk_rel_get("harumi","trust") == tea_trust + 4)
    $ kk_test_at(3,1,1)
    while not kk_pending_talk("nagisa","d1","Gedung Arsitektur"):
        $ kk_advance()
        $ kk_test_expect("N03 bounded", kk_bulan == 3)
    call kk_do_talk("d1","Gedung Arsitektur","nagisa")
    $ kk_test_expect("N03 stage", stage["nagisa"] == 1)
    $ kk_test_at(4,1,1)
    $ kk_test_expect("Mi03 cannot fire in daytime", not kk_pending_talk("miyuki","d6","Rumah Sakit Tachibana"))
    while not kk_pending_talk("miyuki","d6","Rumah Sakit Tachibana"):
        $ kk_advance()
        $ kk_test_expect("Mi03 bounded",kk_bulan == 4)
    call kk_do_talk("d6","Rumah Sakit Tachibana","miyuki")
    $ kk_test_expect("Mi03 effect",kk_get("kelelahan_miyuki") == 27 and kk_done("Mi03"))
    if kk_test_romance():
        while not kk_pending_talk("harumi","d1","Asrama Putri"):
            $ kk_advance()
            $ kk_test_expect("Cooking reachable before end of exams", kk_bulan == 4)
        call kk_do_talk("d1","Asrama Putri","harumi")
        while kk_social_event("harumi","Asrama Putri") != "H-D05":
            $ kk_advance()
            $ kk_test_expect("Harumi tries again", kk_bulan == 4)
        call kk_do_talk("d1","Asrama Putri","harumi")
        $ kk_test_expect("Cooking callback", kk_done("H-D05") and kk_get("kejelasan_harumi") == 30)
    $ test_balance = saldo
    nar "Pemeriksaan simpan."
    if not os.environ.get("KK_TEST_LOADED"):
        $ renpy.save("qa-world")
        $ saldo -= 321
        $ os.environ["KK_TEST_LOADED"] = "1"
        $ renpy.load("qa-world")
    $ kk_test_expect("Save/load",saldo == test_balance and kk_done("Mi03"))
    $ kk_test_at(5,9,3)
    $ test_before = len(choices_log)
    nar "Pemeriksaan rollback."
    $ kk_record_choice("N04","B")
    nar "Pemeriksaan sesudah pilihan."
    if not os.environ.get("KK_TEST_ROLLED"):
        $ os.environ["KK_TEST_ROLLED"] = "1"
        $ renpy.rollback(force=True, checkpoints=2, greedy=False)
    $ kk_test_expect("Rollback and replay once", len(choices_log) == test_before+1 and kk_due["koita_reply"] == kk_elapsed_days+14)
    $ kk_test_at(5,23,3)
    if kk_host == "chiasa":
        $ kk_world_seed = next(n for n in range(1,200) if int.from_bytes(hashlib.sha256(("%d/%d/3/nagisa" % (n,kk_elapsed_days)).encode()).digest()[:4],"big") % 100 >= 15)
        $ kk_test_expect("Swing only on the evening of the reply", kk_social_event("nagisa","Taman Lingkungan") == "N-D03")
        call kk_do_talk("d2","Taman Lingkungan","nagisa")
    $ kk_test_at(5,28,1)
    $ kk_test_expect("Swing expires for absent host", ("N-D03" in kk_missed) == (kk_host == "yutaka"))
    $ kk_test_expect("Consequence without player", kk_has("nagisa_koita_ditolak") and "koita_reply" not in kk_due)
    if kk_host == "yutaka":
        $ y05_before = kk_get("curiga_nagisa",0)
        $ kk_test_expect("Y05 pending in May", "Y05" in kk_pending_enter("d3","Apartemen Yutaka"))
        $ kk_test_family_caption = "Kalah terang-terangan saja."
        call kk_play_scene("Y05")
        $ kk_test_family_caption = None
        $ kk_test_expect("Losing openly raises Nagisa's suspicion", kk_done("Y05") and kk_get("curiga_nagisa",0) == y05_before + 12)
    if kk_host == "chiasa":
        $ c04_intim = kk_rel_get("nagisa","intim")
        $ kk_test_expect("C04 pending at the festival", "C04" in kk_pending_enter("d2","Rumah Amamiya"))
        $ kk_test_family_caption = "Pakai julukan lama itu."
        call kk_play_scene("C04")
        $ kk_test_family_caption = None
        $ kk_test_expect("The old nickname stirs Nagisa", kk_done("C04") and kk_rel_get("nagisa","intim") == c04_intim + 3)
    $ kk_test_expect("Silence and misses", kk_has("q01_expired") and "Mi09" not in kk_missed)
    $ kk_world_seed = next(seed for seed in range(1,500) if all(int.from_bytes(hashlib.sha256(("%d/%d/1/harumi" % (seed, kk_elapsed_days+days)).encode()).digest()[:4],"big") % 100 >= 8 for days in (1,2)))
    $ kk_test_expect("Promise timing", kk_make_promise("harumi","Taman Kampus") and not kk_keep_promise("harumi","Taman Kampus"))
    $ kk_new_day()
    $ kk_test_expect("Promise takes precedence", kk_daily_place("harumi") == "Taman Kampus" and kk_keep_promise("harumi","Taman Kampus"))
    $ kk_make_promise("harumi","Taman Kampus")
    $ before_miss = kk_rel_get("harumi","trust")
    $ kk_new_day()
    $ kk_new_day()
    $ kk_test_expect("Missed promise remembered", "harumi" not in kk_promises and kk_rel_get("harumi","trust") == before_miss - 3)
    $ kk_test_at(6,1,2)
    while not kk_pending_talk("harumi","d1","Kafe Komorebi"):
        $ kk_advance()
        $ kk_test_expect("Tea reunion bounded", kk_bulan == 6)
    $ kujo_before = kk_get("orang_tua_kujo")
    $ kk_test_speaker = "harumi"
    $ kk_test_family_caption = "Tanyakan ke mana ia ingin melangkah setelah lulus."
    call screen kk_location_view("d1","Kafe Komorebi")
    $ kk_test_expect("Reunion button", _return == ("talk","harumi"))
    call kk_do_talk("d1","Kafe Komorebi","harumi")
    $ kk_test_speaker = None
    $ kk_test_family_caption = None
    $ kk_test_expect("Future talk nudges the Kujo household", kk_done("H05") and kk_get("orang_tua_kujo") == kujo_before + 5)
    while kk_date().weekday() >= 5 or kk_slot not in (1,2):
        $ kk_advance()
        $ kk_test_expect("Nagisa photo reachable", kk_bulan == 6)
    $ n05_intim = kk_rel_get("nagisa","intim")
    call kk_test_family_visit("N05","nagisa","d1","Gedung Arsitektur","Minta ia bercerita tentang Koko.")
    $ kk_test_expect("Koko story deepens intimacy", kk_rel_get("nagisa","intim") == n05_intim + 4 and kk_has("koko_dikenal"))
    call kk_test_seek_talk("K06","koita","d1","Kafe Komorebi","Ambilkan fotonya dari luar bingkai.",6)
    $ kk_test_expect("Group photo becomes evidence", kk_done("K06") and kk_has("foto_bukti_koita"))
    $ kk_test_at(7,1,1)
    while not kk_pending_talk("miyuki","d6","Rumah Sakit Tachibana"):
        $ kk_advance()
        $ kk_test_expect("Family meeting opens in October", kk_bulan == 7)
    $ pressure_before = kk_get("omiai_takeru")
    call kk_do_talk("d6","Rumah Sakit Tachibana","miyuki")
    $ kk_test_expect("Family meeting", kk_done("Mi07") and kk_get("omiai_takeru") == pressure_before+5)
    $ kk_test_at(8,1,3)
    $ kk_test_expect("Cover commission limited to Chiasa", ("C05" in kk_pending_enter("d2","Rumah Amamiya")) == (kk_host == "chiasa"))
    if kk_host == "chiasa":
        call kk_play_scene("C05")
        $ kk_test_expect("Accepting or declining keeps passive income", kk_has("proyek_mio_diterima") == bool(os.environ.get("KK_ART_WIN")))
    $ kk_test_at(8,1,2)
    $ s06_respek = kk_get("respek_shiori",20)
    call kk_test_seek_talk("S06","shiori","d3","Klub Catur","Hadir dan dukung permainannya.",8)
    $ kk_test_expect("Chess tournament earns respect", kk_done("S06") and kk_get("respek_shiori",20) == s06_respek + 3)
    call kk_test_seek_talk("Mi08","miyuki","d6","Rumah Sakit Tachibana","Dukung ia mencoba berkonsultasi.",8)
    $ kk_test_expect("Supporting Sato opens recovery", kk_done("Mi08") and kk_has("miyuki_sato_dikenal"))
    $ kk_test_at(8,2,4)
    $ kk_minute = 60
    $ kk_test_expect("Mio only writes about an accepted project at eleven", kk_mio_message() == bool(os.environ.get("KK_ART_WIN")))
    if kk_mio_message():
        call kk_mio_deadline
        $ kk_test_expect("Mio remembers honest answer", kk_has("mio_tahu_kesulitan") and not kk_mio_message())
    $ kk_test_at(9,24,3)
    $ n07_attach = kk_get("kelekatan_nagisa")
    call kk_test_family_visit("N07","nagisa","d2","Rumah Sakurajima","Tetap di sana merayakan bersamanya.")
    $ kk_test_expect("Christmas with Koko builds attachment", kk_get("kelekatan_nagisa") == n07_attach + 10 and kk_has("koko_dikenal"))
    $ kk_test_at(10,1,0)
    while not kk_pending_talk("harumi","d7","Kuil"):
        $ kk_advance()
        $ kk_test_expect("Hatsumode within New Year", kk_hari_n <= 3)
    call kk_do_talk("d7","Kuil","harumi")
    $ kk_test_expect("Interpreting the fortune unlocks late tea", kk_get("kejelasan_harumi") == (40 if kk_test_romance() else 30))
    $ k09_fear = kk_get("ketakutan_koita",0)
    call kk_test_seek_talk("K09","koita","d7","Kuil","Tanyakan pilihan apa yang ia maksud.",10)
    $ kk_test_expect("Omikuji stirs Koita's fear", kk_done("K09") and kk_get("ketakutan_koita",0) == k09_fear + 8)
    $ mi10_trust = kk_rel_get("miyuki","trust")
    call kk_test_seek_talk("Mi10","miyuki","d7","Kuil","Hibur dan temani ia sebentar.",10)
    $ kk_test_expect("Comforting Miyuki at the shrine builds trust", kk_done("Mi10") and kk_rel_get("miyuki","trust") == mi10_trust + 5)
    $ kk_test_at(10,5,4)
    $ kk_minute = 180
    while not kk_social_event("harumi", "Asrama Putri"):
        $ kk_advance()
        $ kk_test_expect("Dorm tea reachable at one", kk_bulan == 10)
    call kk_do_talk("d1", "Asrama Putri", "harumi")
    $ kk_test_expect("Dorm tea happens once", kk_done("H-D01") and kk_get("kejelasan_harumi") == (50 if kk_test_romance() else 35))
    $ kk_test_at(11,1,1)
    while kk_date().weekday() >= 5 or kk_slot not in (1,2):
        $ kk_advance()
        $ kk_test_expect("Valentine studio reachable", kk_bulan == 11)
    $ n08_attach = kk_get("kelekatan_nagisa")
    call kk_test_family_visit("N08","nagisa","d1","Gedung Arsitektur","Bantu ia membuat satu loyang lagi.")
    $ kk_test_expect("Remaking chocolate together builds attachment", kk_get("kelekatan_nagisa") == n08_attach + 5)
    $ kk_test_at(12,10,3)
    $ kk_test_expect("Lobby visit respects host and location", kk_father_visit("Apartemen Yutaka") == (kk_host == "yutaka") and not kk_father_visit("Kos Moeka"))
    if kk_host == "yutaka":
        call kk_visit_kisaragi
        $ kk_test_expect("Father visit opens mother message", kk_family_bond() == 40 and not kk_father_visit("Apartemen Yutaka") and kk_mother_message())
        call kk_message_kisaragi
        $ kk_test_expect("Reply recorded only once", kk_done("Y-D08") and not kk_mother_message() and kk_family_bond() == 45)
    $ kk_test_at(12,11,1)
    while kk_date().weekday() >= 5 or kk_slot not in (1,2):
        $ kk_advance()
        $ kk_test_expect("White Day studio reachable", kk_bulan == 12)
    $ n09_gengsi = kk_get("gengsi_nagisa",70)
    call kk_test_family_visit("N09","nagisa","d1","Gedung Arsitektur","Beri hadiah kecil yang sederhana.")
    $ kk_test_expect("A modest gift lowers her pride", kk_get("gengsi_nagisa",70) == n09_gengsi - 5)
    $ k11_suspect = kk_get("koita_curiga_1",0)
    call kk_test_seek_talk("K11","koita","d1","Gedung Sastra","Biarkan saja.",12)
    $ kk_test_expect("Identical gifts breed suspicion", kk_done("K11") and kk_get("koita_curiga_1",0) == k11_suspect + 10)
    $ kk_test_at(13,1,1)
    while not kk_pending_talk("harumi","d1","Gedung Sains & Lab"):
        $ kk_advance()
        $ kk_test_expect("Spring lab meeting bounded", kk_bulan == 13)
    call kk_do_talk("d1","Gedung Sains & Lab","harumi")
    $ kk_test_expect("Harumi remembers earlier conversation", kk_has("harumi_dibantu_menamai_emosi"))
    $ kk_test_expect("Father call is host specific", ("Y09" in kk_pending_enter("d3","Apartemen Yutaka")) == (kk_host == "yutaka"))
    if kk_host == "chiasa":
        $ c08_before = kk_get("curiga_haruka",0)
        $ kk_test_expect("C08 pending when the style shifts", "C08" in kk_pending_enter("d1","Gedung Seni Rupa & Studio"))
        $ kk_test_family_caption = "Beralasan kau sedang stres."
        call kk_play_scene("C08")
        $ kk_test_family_caption = None
        $ kk_test_expect("A thin excuse raises Haruka's suspicion", kk_done("C08") and kk_get("curiga_haruka",0) == c08_before + 6)
    if kk_host == "yutaka":
        call kk_play_scene("Y09")
        $ kk_test_expect("Family listens to graduation plans", kk_family_bond() == 55)
    $ kk_test_at(13,2,1)
    while kk_date().weekday() >= 5 or kk_slot not in (1,2):
        $ kk_advance()
        $ kk_test_expect("Haruto call reachable", kk_bulan == 13)
    $ n10_trust = kk_rel_get("nagisa","trust")
    call kk_test_family_visit("N10","nagisa","d1","Gedung Arsitektur","Tanggapi Haruto dengan hangat dan berjanji menjaga Nagisa.")
    $ kk_test_expect("Warm reply to Haruto is remembered", kk_done("N10") and kk_has("haruto_kenal") and kk_rel_get("nagisa","trust") == n10_trust + 3)
    $ kk_test_at(14,1,0)
    $ k12_trust = kk_rel_get("koita","trust")
    call kk_test_seek_talk("K12","koita","d1","Gedung Sastra","Akui kau memang pergi dan minta maaf.",14)
    $ kk_test_expect("Owning the trip keeps Koita's trust", kk_done("K12") and kk_rel_get("koita","trust") == k12_trust + 4)
    $ kk_test_at(14,1,0)
    while kk_date().weekday() != 5:
        $ kk_new_day()
    while not kk_pending_talk("harumi","d5","Stasiun Kouseikan-mae"):
        $ kk_advance()
        $ kk_test_expect("Kansai trip bounded", kk_bulan == 14)
    $ kujo_before = kk_get("orang_tua_kujo")
    $ kk_test_speaker = "harumi"
    $ kk_test_family_caption = "Tawarkan ikut menemaninya pulang."
    call screen kk_location_view("d5","Stasiun Kouseikan-mae")
    $ kk_test_expect("Kansai button", _return == ("talk","harumi"))
    call kk_do_talk("d5","Stasiun Kouseikan-mae","harumi")
    $ kk_test_speaker = None
    $ kk_test_family_caption = None
    $ kk_test_expect("Going along builds the family and sets a flag", kk_done("H10") and kk_has("harumi_kansai_ikut") and kk_get("orang_tua_kujo") == kujo_before + 15)
    while not kk_social_event("harumi","Perpustakaan Pusat"):
        $ kk_advance()
        $ kk_test_expect("Kansai letter bounded", kk_bulan <= 15)
    $ kujo_before = kk_get("orang_tua_kujo")
    $ kk_test_speaker = "harumi"
    $ kk_test_family_caption = "Bantu ia menyusun balasan dengan kata-katanya sendiri."
    call screen kk_location_view("d1","Perpustakaan Pusat")
    $ kk_test_expect("Letter button", _return == ("talk","harumi"))
    call kk_do_talk("d1","Perpustakaan Pusat","harumi")
    $ kk_test_speaker = None
    $ kk_test_family_caption = None
    $ kk_test_expect("Answering the letter raises the family to the threshold", kk_done("H-D07") and kk_get("orang_tua_kujo") == kujo_before + 10 and kk_get("orang_tua_kujo") >= 60)
    $ kk_test_at(15,1,2)
    call kk_test_seek_talk("S10","shiori","d3","Klub Catur","Ikut diantar bersamanya.",15)
    $ kk_test_expect("Riding with Kuroiwa is noted", kk_done("S10") and kk_has("kuroiwa_mencatat"))
    $ kk_test_at(16,1,3)
    if kk_host == "chiasa":
        $ _lokasi = "Rumah Amamiya"
        $ kk_test_expect("Empty sketchbook before mastering art", "C09" in kk_pending_enter("d2",_lokasi))
        call kk_play_scene("C09")
        if os.environ.get("KK_ART_WIN"):
            $ kk_test_expect("Two choices bring Shena sketches to Haruka", kk_comparison_due())
            while not kk_art_studio_open("Gedung Seni Rupa & Studio"):
                $ kk_advance()
                $ kk_test_expect("Haruka available on a weekday", kk_bulan == 16)
            $ _lokasi = "Gedung Seni Rupa & Studio"
            call kk_show_portfolio
            $ kk_test_expect("Haruka teaches after the comparison", kk_done("C-D02") and kk_has("haruka_dimintai_bantuan") and not kk_comparison_due())
            $ _lokasi = "Rumah Amamiya"
            while kk_kelelahan_tier()[1] < 2 or not kk_can_sketch(_lokasi):
                $ kk_advance()
            call kk_draw_at_home
            $ kk_test_expect("Exhaustion changes practice", kk_done("C-D03") and kk_clock() == "06:00")
            while kk_get("kemampuan_gambar") < 80:
                if kk_can_sketch(_lokasi):
                    $ kk_practice_sketch(_lokasi)
                else:
                    $ kk_sleep(480)
                $ kk_test_expect("Art mastery within available weeks", kk_bulan == 16)
    if kk_host == "yutaka":
        $ kk_test_expect("Y10 pending in M16", "Y10" in kk_pending_enter("d2","Rumah Amamiya"))
        $ kk_test_family_caption = "Simpan dengan hati-hati dan berterima kasih."
        call kk_play_scene("Y10")
        $ kk_test_family_caption = None
        $ kk_test_expect("Keeping the watch pleases Daisuke", kk_done("Y10") and kk_has("daisuke_setuju"))
    $ kk_test_at(18,1,2)
    $ s12_trust = kk_rel_get("shiori","trust")
    call kk_test_seek_talk("S12","shiori","d3","Klub Catur","Bantu bantah tulisan itu.",18)
    $ kk_test_expect("Defending Shiori against the rumor builds trust", kk_done("S12") and kk_rel_get("shiori","trust") == s12_trust + 6)
    $ kk_test_at(19,1,0)
    $ k15_wake = koita_sadar
    call kk_test_seek_talk("K15","koita","d1","Gedung Sastra","Akui sebagian: ada yang kau sembunyikan.",19)
    $ kk_test_expect("First panic wakes Koita", kk_done("K15") and koita_sadar == k15_wake + 1)
    $ kk_test_at(20,1,2)
    if kk_host == "chiasa":
        while not kk_pending_talk("shiori","d1","Gedung Seni Rupa & Studio"):
            $ kk_advance()
            $ kk_test_expect("Exhibition is reachable in November", kk_bulan == 20)
        call kk_do_talk("d1","Gedung Seni Rupa & Studio","shiori")
        $ kk_test_expect("Shiori knows the pen name", kk_has("shiori_tahu_shena"))
    $ kk_test_at(21,24,1)
    $ kk_test_expect("Amamiya dinner is not open at lunch", not kk_pending_enter("d2","Rumah Amamiya"))
    $ kk_test_at(21,24,3)
    $ kk_test_expect("Amamiya Christmas dinner", ("Y13" in kk_pending_enter("d2","Rumah Amamiya")) == (kk_host == "yutaka"))
    if kk_host == "yutaka":
        call kk_play_scene("Y13")
        $ kk_test_expect("Dinner remembered", kk_has("makan_bersama_amamiya"))
        $ kk_test_expect("Christmas dinner builds the Amamiya bond", kk_amamiya_bond() >= 60)
        $ kk_test_expect("Warm ties resolve to the chosen family", kk_yutaka_relation_ending() == "E-YH-03")
        $ kk_test_expect("Avoiding the dinner leaves no chosen-family ending", kk_yutaka_relation_ending(bond=40) is None)
    $ k16_trust = kk_rel_get("koita","trust")
    call kk_test_seek_talk("K16","koita","d2","Rumah Amamiya","Duduk dan dengarkan ceritanya sampai selesai.",21)
    $ kk_test_expect("Listening reaches the root of her nature", kk_done("K16") and kk_has("koita_akar_diketahui") and kk_rel_get("koita","trust") == k16_trust + 6)
    $ kk_test_at(24,1,0)
    call kk_test_seek_talk("K18","koita","d1","Gedung Sastra","Curi baca daftar itu diam-diam.",24)
    $ kk_test_expect("Reading the name list is remembered", kk_done("K18") and kk_has("koita_daftar_dibaca"))
    $ kk_test_at(29,1,5)
    $ n20_attach = kk_get("kelekatan_nagisa")
    call kk_test_seek_talk("N20","nagisa","d2","Taman Lingkungan","Ikut dengannya menjauh dari keramaian.",29)
    $ kk_test_expect("Last fireworks deepen attachment", kk_done("N20") and kk_get("kelekatan_nagisa") == n20_attach + 5)
    $ kk_test_at(31,1,1)
    $ kk_test_expect("Offer only for Yutaka", bool(kk_pending_enter("d3","Apartemen Yutaka")) == (kk_host == "yutaka"))
    if kk_host == "yutaka":
        call kk_play_scene("Y17")
        $ kk_test_expect("Career choice sticks", kk_has("job_family"))
    $ kk_test_at(32,1,0)
    $ k24_trust = kk_rel_get("koita","trust")
    call kk_test_seek_talk("K24","koita","d1","Gedung Sastra","Hadir dan dengarkan pidatonya.",32)
    $ kk_test_expect("Attending the speech is remembered", kk_done("K24") and kk_has("koita_pidato_dihadiri") and kk_rel_get("koita","trust") == k24_trust + 4)
    $ kk_test_at(33,24,0)
    python:
        for seed in range(1,400):
            kk_world_seed = seed
            if "H22" in kk_pending_talk("harumi","d5","Stasiun Kouseikan-mae"):
                break
        kk_test_expect("Homecoming visitor at Christmas", "H22" in kk_pending_talk("harumi","d5","Stasiun Kouseikan-mae"))
    $ kujo_before = kk_get("orang_tua_kujo")
    $ kk_test_speaker = "harumi"
    $ kk_test_family_caption = "Antar ia sampai peron dan tunggu keretanya berangkat."
    call screen kk_location_view("d5","Stasiun Kouseikan-mae")
    $ kk_test_expect("Homecoming button", _return == ("talk","harumi"))
    call kk_do_talk("d5","Stasiun Kouseikan-mae","harumi")
    $ kk_test_speaker = None
    $ kk_test_family_caption = None
    $ kk_test_expect("Seeing her off builds the family", kk_done("H22") and kk_get("orang_tua_kujo") == kujo_before + 10)
    $ kk_test_at(33,24,3)
    python:
        for seed in range(1,400):
            kk_world_seed = seed
            if kk_pending_talk("miyuki","d6","Rumah Sakit Tachibana") == ["Mi25"]:
                break
        if kk_pending_talk("miyuki","d6","Rumah Sakit Tachibana") != ["Mi25"]:
            kk_test_at(33,25,3)
            for seed in range(1,400):
                kk_world_seed = seed
                if kk_pending_talk("miyuki","d6","Rumah Sakit Tachibana") == ["Mi25"]:
                    break
    $ kk_test_expect("Proposal due to pressure accumulated over years", kk_pending_talk("miyuki","d6","Rumah Sakit Tachibana") == ["Mi25"])
    call kk_do_talk("d6","Rumah Sakit Tachibana","miyuki")
    $ kk_test_expect("Miyuki family ending", ("E-MI-05" if kk_test_romance() else "E-MI-04") in kk_epilogue())
    $ kk_test_at(33,26,1)
    $ kk_test_expect("Late host and missed opportunities", "Mi09" in kk_missed and not kk_pending_enter("d3","Apartemen Yutaka"))
    # Koita: thread kesadaran -> keruntuhan -> pemulihan (event dinamis K-D).
    # Cabang gelap diuji sebagai konsekuensi (runtuh naik/turun), tanpa metode.
    $ kk_test_at(34,1,1)
    $ store.koita_sadar = 60
    $ store.runtuh_koita = 10
    # Jalur sosial penuh (location-view -> talk -> kk_social_scene) sudah
    # diregresi oleh H-D05/N-D03; di sini cukup drive langsung agar hemat waktu.
    $ kk_test_expect("Selector offers the deliberate disclosure", kk_social_event("koita","Gedung Sastra") == "K-D16" or kk_daily_place("koita") != "Gedung Sastra")
    $ kd16_runtuh = runtuh_koita
    $ kk_test_family_caption = "Ceritakan dengan tenang, sejujurnya."
    call kk_social_scene("K-D16")
    $ kk_test_family_caption = None
    $ kk_test_expect("Deliberate disclosure raises collapse", kk_done("K-D16") and runtuh_koita == kd16_runtuh + 20 and kk_has("koita_diberi_tahu"))
    $ store.runtuh_koita = 72
    $ kd20_runtuh = runtuh_koita
    $ kk_test_family_caption = "Ikut mengantar mereka."
    call kk_social_scene("K-D20")
    $ kk_test_family_caption = None
    $ kk_test_expect("Counselor path eases collapse", kk_done("K-D20") and runtuh_koita == kd20_runtuh - 25 and kk_has("koita_ke_konselor"))
    # Nagisa: event dinamis posesif (N-D). Jalur reachability sosial sudah
    # dibuktikan K-D di atas; di sini dispatch + panel (4 pilihan) + hook diuji
    # langsung agar deterministik lepas dari prioritas selektor akhir-game.
    $ nd05_trust = kk_rel_get("nagisa","trust")
    $ kk_test_family_caption = "Jelaskan apa adanya."
    call kk_social_scene("N-D05")
    $ kk_test_family_caption = None
    $ kk_test_expect("Jealousy screenshot: honesty builds trust", kk_done("N-D05") and kk_rel_get("nagisa","trust") == nd05_trust + 6)
    $ nd11_intim = kk_rel_get("nagisa","intim")
    $ kk_test_family_caption = "Tanya apa maksud ruangan itu."
    call kk_social_scene("N-D11")
    $ kk_test_family_caption = None
    $ kk_test_expect("Blueprint room: asking draws intimacy", kk_done("N-D11") and kk_rel_get("nagisa","intim") == nd11_intim + 6 and kk_has("pengakuan_arsitektur"))
    # Miyuki: luka-diri/karier (Mi-D). Pemulihan dan cabang gelap (menuruti
    # hukuman-diri) diuji sebagai konsekuensi angka, tanpa metode.
    $ pts["luka_miyuki_diri"] = 50
    $ md05_luka = kk_get("luka_miyuki_diri",0)
    $ kk_test_family_caption = "Duduk di sebelahnya tanpa banyak kata."
    call kk_social_scene("Mi-D05")
    $ kk_test_family_caption = None
    $ kk_test_expect("Fire escape: sitting with her eases the wound", kk_done("Mi-D05") and kk_get("luka_miyuki_diri",0) == md05_luka - 15)
    $ md06_luka = kk_get("luka_miyuki_diri",0)
    $ kk_test_family_caption = "Turuti permintaannya."
    call kk_social_scene("Mi-D06")
    $ kk_test_family_caption = None
    $ kk_test_expect("Requested rebuke: complying deepens the wound", kk_done("Mi-D06") and kk_get("luka_miyuki_diri",0) == md06_luka + 12 and kk_has("miyuki_direndahkan"))
    # Shiori: ujian & pembongkaran (S-D). Dipilih event yang gerbangnya tidak
    # tercapai di permainan normal, agar tidak sudah terpakai sebelum M34.
    $ kk_test_family_caption = "Nikmati kehangatan itu apa adanya."
    call kk_social_scene("S-D15")
    $ kk_test_family_caption = None
    $ kk_test_expect("Sweetest smile: indulging walks into the trap", kk_done("S-D15") and kk_has("shiori_senyum_dinikmati"))
    $ pts["respek_shiori"] = 40
    $ sd17_respek = kk_get("respek_shiori",0)
    $ kk_test_family_caption = "Balas dengan langkah jujur yang tak terduga."
    call kk_social_scene("S-D17")
    $ kk_test_family_caption = None
    $ kk_test_expect("Flipped board: an honest move earns the way back", kk_done("S-D17") and kk_get("respek_shiori",0) == sd17_respek + 15 and kk_has("shiori_langkah_jujur"))
    $ kk_test_at(35,1,3)
    $ kk_minute = 220
    $ kk_rel("nagisa","aff", 30)
    $ kk_priority_contacts.append("nagisa")
    $ kk_test_expect("Normal priority interrupted at 22:00", kk_sleep(90) == "nagisa" and kk_clock() == "22:00" and not kk_done("N-D01"))
    $ kk_phone_mode = "senyap"
    $ kk_test_expect("Silent sleeping crosses midnight", kk_sleep(360) is None and kk_clock() == "04:00" and kk_hari_n == 2 and "N-D01" in kk_missed)
    $ kk_test_expect("Twenty minute nap", kk_sleep(20) is None and kk_clock() == "04:20")
    call kk_test_miyuki_daily
    $ kk_test_at(36,31,4)
    $ kk_minutes(120)
    $ kk_test_expect("Graduation on normal clock", kk_graduated and kk_epilogue()[0] == ("E-SI-02" if kk_test_romance() else "E-SI-13"))
    $ kk_test_expect("Organic Harumi ending only for this journey", ("E-HA-01" in kk_epilogue()) == kk_test_romance())
    $ kk_test_expect("Kujo family ending fills in when romance clarity is absent", ("E-HA-09" in kk_epilogue()) == (not kk_test_romance()))
    $ kk_test_expect("Reconciled heir after graduation", ("E-YH-01" in kk_epilogue()) == (kk_host == "yutaka"))
    $ kk_test_expect("Chosen-family ending yields to the Kisaragi post here", "E-YH-03" not in kk_epilogue())
    $ kk_test_expect("Thirty-five monthly deposits", len([t for t in kk_transactions if t[2].startswith("Uang saku")]) == 35 and kk_transactions[-1][4] == saldo)
    $ kk_test_expect("Shena builds her own style", ("E-CF-08" in kk_epilogue()) == bool(os.environ.get("KK_ART_WIN")))
    $ kk_test_expect("Shared home follows a surviving Chiasa romance", ("E-CF-01" in kk_epilogue()) == bool(os.environ.get("KK_ART_WIN")))
    call screen kk_wallet
    call kk_evaluasi
    $ open(os.path.join(config.basedir, ("artist" if os.environ.get("KK_ART_WIN") else kk_host)+".ok"),"w").write(kk_host+" · life, four VN scenes, save/load, rollback, expiry, delayed response, epilogue: OK")
    $ renpy.quit()


# The driver sets the calendar and a reproducible attendance seed. It clicks the
# real NPC button and family choice, then uses the production conversation label.
label kk_test_family_visit(eid, cid, district, place, caption):
    if eid in ("Mi09","Mi18","Mi25","N22","S07"):
        $ kk_test_expect("Correct Christmas window " + eid, kk_hari_n in (24,25) and kk_slot == 3)
    python:
        for seed in range(1,100):
            kk_world_seed = seed
            if eid in kk_pending_talk(cid,district,place) or kk_social_event(cid,place) == eid:
                break
        kk_test_expect("Scheduled visitor " + eid, eid in kk_pending_talk(cid,district,place) or kk_social_event(cid,place) == eid)
    $ kk_test_speaker = cid
    $ kk_test_family_caption = caption
    call screen kk_location_view(district,place)
    $ kk_test_expect("Talk button " + eid, _return == ("talk",cid))
    call kk_do_talk(district,place,cid)
    $ kk_test_family_caption = None
    $ kk_test_speaker = None
    $ kk_test_expect("Recorded once " + eid, kk_done(eid) and eid not in kk_pending_talk(cid,district,place))
    return

# Advance day and seed until the visitor is actually at the place, then drive the talk.
# Needed for Koita, whose slot can resolve to one of two locations depending on the day.
label kk_test_seek_talk(eid, cid, district, place, caption, maxmonth):
    python:
        ok = False
        while not ok and kk_bulan <= maxmonth:
            for seed in range(1,150):
                kk_world_seed = seed
                if eid in kk_pending_talk(cid,district,place):
                    ok = True
                    break
            if not ok:
                kk_advance()
        kk_test_expect("Reachable " + eid, ok)
    $ kk_test_speaker = cid
    $ kk_test_family_caption = caption
    call screen kk_location_view(district,place)
    $ kk_test_expect("Talk button " + eid, _return == ("talk",cid))
    call kk_do_talk(district,place,cid)
    $ kk_test_speaker = None
    $ kk_test_family_caption = None
    $ kk_test_expect("Recorded " + eid, kk_done(eid))
    return

label kk_test_seek_social(eid, cid, district, place, caption, maxmonth):
    # Seperti kk_test_seek_talk tetapi untuk event sosial (kk_social_event),
    # yang hanya fire bila tidak ada milestone talk yang membayanginya.
    python:
        ok = False
        while not ok and kk_bulan <= maxmonth:
            for seed in range(1,30):
                kk_world_seed = seed
                if (not kk_pending_talk(cid,district,place)
                        and kk_social_event(cid,place) == eid):
                    ok = True
                    break
            if not ok:
                kk_advance()
        kk_test_expect("Reachable social " + eid, ok)
    $ kk_test_speaker = cid
    $ kk_test_family_caption = caption
    call screen kk_location_view(district,place)
    $ kk_test_expect("Talk button social " + eid, _return == ("talk",cid))
    call kk_do_talk(district,place,cid)
    $ kk_test_speaker = None
    $ kk_test_family_caption = None
    $ kk_test_expect("Recorded social " + eid, kk_done(eid))
    return

label kk_test_family_years:
    $ variant = os.environ["KK_FAMILY_CASE"]
    $ kk_test_at(9,23,3)
    $ kk_test_expect("Christmas dinner only opens on Christmas Eve", not kk_window("S07"))
    $ kk_test_at(9,24,3)
    $ answer = {"keep":"Masuk dan makan bersama keluarganya.","reveal":"Titipkan hadiah untuk keluarganya.","admit":"Ucapkan selamat Natal lalu pamit."}[variant]
    call kk_test_family_visit("S07","shiori","d3","Rumah Saionji",answer)
    $ kk_test_expect("Tea is a later visit", kk_social_event("shiori","Rumah Saionji") != "S-D08")
    $ kk_test_at(9,25,3)
    call kk_test_family_visit("Mi09","miyuki","d6","Rumah Sakit Tachibana","Tawarkan berpura-pura menjadi pasangannya.")
    $ kk_test_expect("The hospital party starts the sham", kk_has("pasangan_palsu"))
    $ kk_test_at(10,1,3)
    while kk_date().weekday() != 5:
        $ kk_new_day()
    if variant == "keep":
        call kk_test_family_visit("S-D08","shiori","d3","Rumah Saionji","Ceritakan apa yang kaulihat tanpa menebak perasaannya.")
        $ kk_test_expect("Tea remembered", kk_has("shiori_teh_jujur"))
    else:
        python:
            for seed in range(1,100):
                kk_world_seed = seed
                if kk_daily_place("shiori") == "Rumah Saionji":
                    break
            kk_test_expect("Shiori is present for the negative tea check", kk_daily_place("shiori") == "Rumah Saionji")
        $ kk_test_expect("A gift or departure does not open the tea scene", kk_social_event("shiori","Rumah Saionji") != "S-D08")
    $ kk_test_at(11,1,2)
    while kk_date().weekday() != 5:
        $ kk_new_day()
    $ before_cake = kk_get("dimanja_miyuki")
    $ answer = {"keep":"Tarik kursi dan makan bersamanya.","reveal":"Bantu bagikan kue selagi masih hangat.","admit":"Minta satu kue khusus untukmu."}[variant]
    call kk_test_family_visit("Mi11","miyuki","d1","Kafe Komorebi",answer)
    $ kk_test_expect("Sharing cake", kk_get("dimanja_miyuki") == before_cake + (0 if variant == "admit" else 5))
    $ kk_test_at(12,1,1)
    while kk_date().weekday() != 5:
        $ kk_new_day()
    $ trust_before = kk_rel_get("shiori","trust")
    $ answer = {"keep":"Katakan kau lebih nyaman hanya bertemu untuk bermain.","admit":"Terima, lalu minta dia mengenalkanmu pada orang penting.","reveal":"Geser kursi dan ajak dia tinggal setelah klub tutup."}[variant]
    call kk_test_family_visit("S09","shiori","d3","Klub Catur",answer)
    $ kk_test_expect("Shiori distinguishes friendship, refusal, and an introduction", kk_has("shiori_teman_dipercaya") == (variant == "reveal") and kk_rel_get("shiori","trust") == trust_before + {"reveal":5,"keep":0,"admit":-5}[variant])
    $ kk_test_at(20,1,2)
    while kk_date().weekday() != 5:
        $ kk_new_day()
    $ kk_test_expect("Shiori needs evidence", not kk_window("S13"))
    call kk_test_family_visit("C11","shiori","d1","Gedung Seni Rupa & Studio","Pura-pura tidak mengenal nama itu.")
    if variant != "admit":
        $ kk_test_at(20,kk_hari_n+1,2)
        $ answer = "Ceritakan bagian yang sengaja kaulewatkan." if variant == "keep" else "Susun alasan lain agar ceritamu terdengar cocok."
        call kk_test_family_visit("S-D04","shiori","d1","Gedung Seni Rupa & Studio",answer)
    $ kk_test_expect("Early honesty clears the lie before discovery", kk_window("S13") == (variant != "keep") and kk_has("shiori_tahu_shena") == (variant == "keep"))
    if variant != "keep":
        $ kk_new_day()
        while kk_date().weekday() != 5:
            $ kk_new_day()
        $ kk_slot = 1
        $ answer = "Tetap pada ceritamu semula." if variant == "reveal" else "Ceritakan terus terang apa yang kausembunyikan."
        call kk_test_family_visit("S13","shiori","d3","Klub Catur",answer)
        $ kk_test_expect("Answer at the chess club changes Shiori's decision", (stage["shiori"] >= 2) == (variant == "reveal"))
        $ kk_test_expect("Discovered second lie counts twice", kk_get("daftar_kebohongan_shiori") == (3 if variant == "reveal" else 0))
    $ kk_test_at(21,24,3)
    $ kk_test_expect("Second Christmas depends on discovery", kk_window("S14") == (variant == "reveal"))
    if variant == "reveal":
        call kk_test_family_visit("S14","shiori","d3","Rumah Saionji","Minta maaf atas jawabanmu waktu itu.")
        $ kk_test_expect("She hears the apology without forgetting", kk_has("shiori_mendengar_maaf") and stage["shiori"] == 3)
    $ kk_test_at(21,25,3)
    $ answer = {"keep":"Duduk di samping Miyuki seperti tahun lalu.","reveal":"Minta Takeru menunda pembicaraan.","admit":"Ceritakan mengapa kalian datang bersama tahun lalu."}[variant]
    call kk_test_family_visit("Mi18","miyuki","d6","Rumah Sakit Tachibana",answer)
    $ kk_test_expect("Mi18 distinguishes all three outcomes", kk_has("sandiwara_diakui") == (variant == "admit") and kk_has("sandiwara_terbongkar") == (variant == "reveal"))
    $ kk_test_at(22,2,1)
    $ answer = "Tanya untuk siapa ia akan berdoa." if variant == "reveal" else "Biarkan ia berdoa sendiri."
    call kk_test_family_visit("S15","shiori","d7","Kuil",answer)
    $ kk_test_expect("Shrine conversation is independent of revenge", kk_has("shiori_doa_ditanya") == (variant == "reveal"))
    $ kk_test_at(23,14,2)
    $ kk_test_expect("Empty board only follows discovery", kk_window("S16") == (variant == "reveal"))
    if variant == "reveal":
        call kk_test_family_visit("S16","shiori","d3","Klub Catur","Tunggu di pintu sampai ia bicara.")
    $ kk_test_at(25,1,3)
    while kk_date().weekday() != 5:
        $ kk_new_day()
    call kk_test_family_visit("S17","shiori","d3","Rumah Saionji","Dengarkan sampai ia selesai menyampaikan rencananya.")
    $ kk_test_at(25,kk_hari_n+7,1)
    if variant != "keep":
        $ career_before = kk_get("karier_miyuki",70)
        $ answer = "Tahan dia sebentar untuk urusanmu sendiri." if variant == "reveal" else "Bantu susun jadwalnya agar ia bisa segera masuk."
        call kk_test_family_visit("Mi21","miyuki","d6","Rumah Sakit Tachibana",answer)
        $ kk_test_expect("Rotation direction is saved", kk_get("karier_miyuki") == career_before + (-5 if variant == "reveal" else 5))
    $ kk_test_at(25,15,3)
    while not kk_can_sit_with_miyuki("Perpustakaan Pusat"):
        $ kk_new_day()
        $ kk_test_expect("Reachable library seat", kk_bulan == 25)
    $ kk_test_seat = True
    call screen kk_location_view("d1","Perpustakaan Pusat")
    $ kk_test_expect("The player chooses the library seat", _return == ("sit_miyuki",None))
    $ kk_test_seat = False
    $ kk_test_family_caption = {"keep":"Tetap duduk sampai ia terbangun.","reveal":"Bangunkan ia dengan pelan.","admit":"Ambil foto saat ia tertidur."}[variant]
    $ tired_before = kk_get("kelelahan_miyuki")
    call kk_library_rest("Perpustakaan Pusat")
    $ kk_test_family_caption = None
    $ kk_test_expect("Time, rest and optional photo", kk_done("Mi-D02") and kk_minute == (120 if variant == "keep" else 5) and kk_get("kelelahan_miyuki") == tired_before - (5 if variant == "keep" else 0) and kk_has("foto_miyuki_tertidur") == (variant == "admit") and not kk_can_sit_with_miyuki("Perpustakaan Pusat"))
    $ kk_test_at(26,1,0)
    if variant == "reveal":
        $ kk_test_expect("Unattended board only in the club", kk_unfinished_board("Klub Catur") and not kk_unfinished_board("Rumah Saionji"))
        $ kk_test_board = True
        call screen kk_location_view("d3","Klub Catur")
        $ kk_test_expect("Inspect the board from the location screen", _return == ("board",None))
        $ kk_test_board = False
        $ kk_test_family_caption = "Balas dengan langkah yang dulu urung kaumainkan."
        call kk_inspect_board("Klub Catur")
        $ kk_test_family_caption = None
        $ kk_test_expect("Board reply recorded once", kk_has("shiori_langkah_balasan") and not kk_unfinished_board("Klub Catur"))
    $ kk_test_at(27,1,3)
    while kk_date().weekday() != 5:
        $ kk_new_day()
    $ kk_test_expect("Only unresolved discovery opens the evidence meeting", kk_window("S18") == (variant == "reveal"))
    if variant == "reveal":
        nar "Pemeriksaan percabangan saat hujan."
        if not os.environ.get("KK_RAIN_BRANCH"):
            $ renpy.save("qa-rain")
        $ rain = os.environ.get("KK_RAIN_BRANCH","A")
        $ answer = {"A":"Masuk tanpa izin untuk menghapus catatan itu.","B":"Luruskan ceritamu kepada orang yang ikut dirugikan.","C":"Biarkan catatan itu dan pulang."}[rain]
        call kk_test_family_visit("S18","shiori","d3","Rumah Saionji",answer)
        $ kk_test_expect("Rain visit keeps the three consequences separate", (stage["shiori"] == 4) == (rain != "B") and kk_has("saionji_masuk_tanpa_izin") == (rain == "A") and kk_has("shiori_koreksi_disampaikan") == (rain == "B"))
        if rain in ("A","B"):
            $ os.environ["KK_RAIN_BRANCH"] = "B" if rain == "A" else "C"
            $ renpy.load("qa-rain")
    $ kk_test_at(28,6,1)
    $ kk_test_expect("The bamboo is not there a day early", not kk_window("S19"))
    $ kk_test_at(28,7,1)
    if variant == "reveal":
        call kk_test_family_visit("N19","nagisa","d1","Taman Kampus","Minta ia mencopot kertas yang ia tulis atas namamu.")
    elif variant == "keep":
        call kk_test_family_visit("Mo20","moeka","d1","Taman Kampus","Tulis harapanmu di sebelah tulisannya.")
    else:
        call kk_test_family_visit("H19","harumi","d1","Taman Kampus","Tanya apa yang ingin ia tulis.")
    $ answer = "Baca tulisan Shiori." if variant == "reveal" else "Biarkan harapannya tetap pribadi."
    call kk_test_family_visit("S19","shiori","d1","Taman Kampus",answer)
    $ kk_test_at(29,1,0)
    $ kk_test_expect("Unvisited wishes expire independently", ("H19" in kk_missed) == (variant != "admit") and ("Mo20" in kk_missed) == (variant != "keep") and ("N19" in kk_missed) == (variant != "reveal"))
    $ kk_test_at(30,15,3)
    $ kk_test_expect("Without support the fatigued student receives a failed result", kk_has("cbt_miyuki_gagal") and not kk_has("cbt_miyuki_lulus"))
    if variant == "reveal":
        while not kk_pending_talk("miyuki","d6","Rumah Sakit Tachibana"):
            $ kk_advance()
            $ kk_test_expect("Hospital visit after the result", kk_bulan == 30)
        call kk_test_family_visit("Mi24","miyuki","d6","Rumah Sakit Tachibana","Duduk bersamanya dan dengarkan.")
    if variant != "admit":
        $ kk_test_at(31,1,3)
        while kk_date().weekday() != 5:
            $ kk_new_day()
        $ answer = "Ceritakan apa yang kaulihat sendiri." if variant == "keep" else "Katakan semuanya biasa saja."
        call kk_test_family_visit("N21","nagisa","d2","Rumah Sakurajima",answer)
        $ kk_test_expect("Haruto remembers the conversation", kk_has("haruto_sekutu") == (variant == "keep") and kk_has("haruto_lawan") == (variant == "reveal"))
    if variant == "keep":
        $ kk_test_at(32,1,2)
        while kk_date().weekday() != 5:
            $ kk_new_day()
        # Set thresholds only; use normal NPC action and calendar for the outcome.
        $ pts["dimanja_miyuki"] = 70
        $ rel["miyuki"]["trust"] = 69
        $ kk_test_expect("Trust below threshold", not kk_miyuki_ready_to_refuse())
        $ kk_rel("miyuki","trust",1)
        python:
            for key in ("luka_miyuki_pemain","luka_miyuki_koita","luka_miyuki_diri"):
                pts[key] = 30
                kk_test_expect("Wound blocks refusal: " + key, not kk_miyuki_ready_to_refuse())
                pts[key] = 29
        $ pts["omiai_takeru"] = 75
        call kk_test_family_visit("Mi-D12","miyuki","d1","Kafe Komorebi","Dukung keputusan Miyuki.")
        $ kk_test_expect("Refusal reduces pressure once", kk_get("omiai_takeru") == 45 and kk_social_event("miyuki","Kafe Komorebi") != "Mi-D12")
    $ kk_test_at(33,23,3)
    $ kk_test_expect("Family invitation is not available early", not kk_pending_talk("nagisa","d2","Rumah Sakurajima"))
    $ kk_test_at(33,24,0)
    $ before_station = kk_get("orang_tua_kujo",30)
    $ answer = {"keep":"Antar ia sampai peron dan tunggu keretanya berangkat.","reveal":"Tawarkan menelepon orang tuanya untuk menitip salam.","admit":"Ucapkan selamat jalan lalu biarkan ia pergi."}[variant]
    call kk_test_family_visit("H22","harumi","d5","Stasiun Kouseikan-mae",answer)
    $ kk_test_expect("Station farewell", kk_get("orang_tua_kujo") == min(100,before_station + (0 if variant == "admit" else 10)))
    $ kk_test_at(33,24,3)
    if variant == "keep":
        $ kk_test_expect("Refusal closes Christmas proposal", not kk_window("Mi25"))
    if variant != "keep":
        $ answer = "Masuk dan sapa keluarganya." if variant == "admit" else "Berterima kasih lalu pamit."
        call kk_test_family_visit("N22","nagisa","d2","Rumah Sakurajima",answer)
    $ kk_test_at(33,25,3)
    if kk_get("omiai_takeru") >= 70:
        call kk_test_family_visit("Mi25","miyuki","d6","Rumah Sakit Tachibana","Minta Takeru berhenti mendesaknya.")
    $ kk_test_at(34,1,3)
    $ _lokasi = "Rumah Amamiya"
    $ kk_test_expect("Koko only appears at the host's desk after opposition", (kk_desk_event(_lokasi) == "N23") == (variant == "reveal") and not kk_desk_event("Apartemen Yutaka"))
    if variant == "reveal":
        $ kk_test_family_caption = "Simpan Koko di meja untuk sementara."
        call kk_check_desk
        $ kk_test_expect("The kept doll can be repaired", kk_desk_event(_lokasi) == "N-D09")
        $ attachment_before = kk_get("kelekatan_nagisa")
        $ kk_test_family_caption = "Kirim pesan ke Moeka dan minta bantuannya menjahit."
        call kk_check_desk
        $ kk_test_family_caption = None
        $ kk_test_expect("Repair remembered once", kk_has("moeka_menjahit_koko") and kk_get("kelekatan_nagisa") > attachment_before and not kk_desk_event(_lokasi))
    $ kk_test_at(36,31,4)
    $ kk_minutes(120)
    $ endings = kk_epilogue()
    $ kk_test_expect("Graduation records the actual family visit", kk_graduated and ("E-NA-07" in endings) == (variant in ("admit","keep")) and ("N22" in kk_missed) == (variant == "keep"))
    $ kk_test_expect("Shena is targeted only when the lie was discovered and unresolved", ("E-SH-13" in endings) == (variant == "reveal"))
    $ kk_test_expect("Support reaches graduation unless revenge is active", ("E-SH-07" in endings) == (variant != "reveal"))
    $ kk_test_expect("Graduation remembers the party and confrontation", ("E-MI-13" in endings) == (variant == "admit") and ("E-MI-14" in endings) == (variant == "reveal"))
    call kk_evaluasi
    $ open(os.path.join(config.basedir, variant+".ok"),"w").write("Miyuki and Nagisa at graduation: "+variant+" OK")
    $ renpy.quit()

label kk_capture_hanami:
    $ kk_host = "chiasa"
    $ kk_setup_state()
    $ kk_test_at(1,19,1)
    $ kk_world_seed = next(seed for seed in range(1,5000) if all(int.from_bytes(hashlib.sha256(("%d/%d/1/%s" % (seed, kk_elapsed_days, who)).encode()).digest()[:4],"big") % 100 >= pct for who,pct in (("miyuki",10),("shiori",5),("nagisa",15),("moeka",30),("harumi",8),("koita",12))))
    call screen kk_location_view("d1","Taman Kampus")
    $ kk_test_at(6,1,1)
    call screen kk_wallet
    $ open(os.path.join(config.basedir, os.environ["KK_SIZE"]+".ok"),"w").write("Hanami and transaction history "+os.environ["KK_SIZE"])
    $ renpy.quit()

# Miyuki's small days. Setup raises the pre-conditions (points, praise flag) directly;
# the pudding message and the cafe conversation then run through production code.
label kk_test_miyuki_daily:
    $ kk_test_at(35,3,3)
    $ kk_minute = 220
    $ kk_adj("dimanja_miyuki", max(0, 50 - kk_get("dimanja_miyuki",10)))
    $ kk_rel("miyuki","trust", 10)
    $ dimanja_before = kk_get("dimanja_miyuki")
    $ kk_test_expect("Pudding message needs the pampering threshold", kk_get("dimanja_miyuki") >= 50 and not kk_done("Mi-D01"))
    if kk_host == "yutaka":
        $ kk_phone_mode = "normal"
        $ kk_priority_contacts.append("miyuki")
        $ kk_test_expect("Priority contact wakes the sleeper for the pudding", kk_sleep(300) == "miyuki")
        $ kk_test_family_caption = "Belikan dan temani"
        call kk_pudding
        $ kk_test_family_caption = None
        $ kk_test_expect("Staying raises pampering and is remembered", kk_done("Mi-D01") and kk_get("dimanja_miyuki") == dimanja_before + 10 and kk_has("pudding_ditemani"))
        $ kk_test_expect("Her thanks arrive once", kk_afterglow("miyuki") and not kk_afterglow("miyuki"))
    else:
        $ kk_phone_mode = "senyap"
        $ kk_test_expect("Silent sleeper misses the pudding", kk_sleep(300) is None and "Mi-D01" in kk_missed and not kk_done("Mi-D01"))
        $ kk_test_expect("A missed pudding changes nothing", kk_get("dimanja_miyuki") == dimanja_before and not kk_has("pudding_ditemani") and kk_afterglow("miyuki") is None)
    $ kk_phone_mode = "normal"

    $ kk_flag("puji_pastry")
    python:
        for step in range(12):
            if kk_rel_get("miyuki","aff") >= 55:
                break
            kk_rel("miyuki","aff", 10)
    $ kk_test_at(36,1,2)
    while kk_date().weekday() != 5:
        $ kk_new_day()
    $ kk_test_at(kk_bulan,kk_hari_n,2)
    python:
        found = False
        for seed in range(1,400):
            kk_world_seed = seed
            if kk_social_event("miyuki","Kafe Komorebi") == "Mi-D03" and kk_daily_place("koita") == "Kafe Komorebi":
                if kk_host == "yutaka":
                    found = kk_daily_place("nagisa") != "Kafe Komorebi"
                else:
                    kk_promises["nagisa"] = (kk_elapsed_days, kk_slot, "Kafe Komorebi")
                    found = kk_daily_place("nagisa") == "Kafe Komorebi"
                    if not found:
                        del kk_promises["nagisa"]
            if found:
                break
        kk_test_expect("Pastry conversation seed found", found)
    $ jeal_before = kk_rel_get("nagisa","jeal")
    $ _distrik = "d1"
    $ _lokasi = "Kafe Komorebi"
    $ kk_test_speaker = "miyuki"
    $ kk_test_family_caption = "Makan di depan Koita" if kk_host == "yutaka" else "bagikan ke semua"
    call screen kk_location_view("d1","Kafe Komorebi")
    $ kk_test_expect("Miyuki button at the cafe", _return == ("talk","miyuki"))
    call kk_do_talk("d1","Kafe Komorebi","miyuki")
    $ kk_test_family_caption = None
    $ kk_test_speaker = None
    $ kk_test_expect("Pastry recorded once", kk_done("Mi-D03") and not kk_record_choice("Mi-D03","B"))
    if kk_host == "yutaka":
        $ kk_test_expect("Eating it in front of Koita is noted, nobody else saw", kk_has("koita_mencatat_pastry") and not kk_has("nagisa_lihat_pastry") and kk_rel_get("nagisa","jeal") == jeal_before)
        $ kk_test_expect("Koita mentions it once", kk_afterglow("koita") and not kk_afterglow("koita"))
    else:
        $ kk_test_expect("Sharing it where Nagisa stands stings her", kk_has("pastry_dibagikan") and kk_has("nagisa_lihat_pastry") and kk_rel_get("nagisa","jeal") == jeal_before + 5)
        $ kk_test_expect("Nagisa mentions it once", kk_afterglow("nagisa") and not kk_afterglow("nagisa"))

    # Mi-D04: the call from her mother, on a Saturday night once the arranged match is pressing.
    $ kk_adj("omiai_takeru", 70 - kk_get("omiai_takeru"))
    $ kk_test_at(kk_bulan,kk_hari_n + 1,0)
    while kk_date().weekday() != 5:
        $ kk_new_day()
    $ kk_test_at(kk_bulan,kk_hari_n,4)
    python:
        found = False
        for seed in range(1,400):
            kk_world_seed = seed
            if kk_daily_place("miyuki") and kk_social_event("miyuki", kk_daily_place("miyuki")) == "Mi-D04":
                found = True
                break
        kk_test_expect("Overheard call seed found", found)
        call_place = kk_daily_place("miyuki")
        call_district = next(d for d, n, locs in KK_DISTRICTS if call_place in locs)
    $ omiai_before = kk_get("omiai_takeru")
    $ trust_before = kk_rel_get("miyuki","trust")
    $ kk_test_speaker = "miyuki"
    $ kk_test_family_caption = "Pura-pura tidak dengar" if kk_host == "yutaka" else "minta bicara dengan ibunya"
    call screen kk_location_view(call_district,call_place)
    $ kk_test_expect("Miyuki button for the call", _return == ("talk","miyuki"))
    call kk_do_talk(call_district,call_place,"miyuki")
    $ kk_test_family_caption = None
    $ kk_test_speaker = None
    $ kk_test_expect("Call recorded once", kk_done("Mi-D04") and not kk_record_choice("Mi-D04","B"))
    if kk_host == "yutaka":
        $ kk_test_expect("Looking away leaves the match pressing", kk_get("omiai_takeru") == omiai_before + 3 and kk_has("telepon_diabaikan") and not kk_has("kenal_sayuri"))
    else:
        $ kk_test_expect("Speaking to her mother eases the match", kk_get("omiai_takeru") == omiai_before - 10 and kk_get("omiai_takeru") < 70 and kk_has("kenal_sayuri") and kk_rel_get("miyuki","trust") == trust_before + 3)
    $ kk_test_expect("Her remark arrives once", kk_afterglow("miyuki") and not kk_afterglow("miyuki"))
    return

# No flags, pressure, affection, trust or wound values are set by this scenario.
label kk_test_clinic:
    $ kk_test_at(6,1,1)
    while kk_daily_place("miyuki") != "Gedung Kedokteran":
        $ kk_new_day()
        $ kk_test_expect("Aspirations can be discussed before clinic", kk_bulan == 6)
    $ trust_before = kk_rel_get("miyuki","trust")
    call kk_test_family_visit("Mi06","miyuki","d1","Gedung Kedokteran","Tanya apa lagi yang membuatnya ingin bekerja dengan anak-anak.")
    $ kk_test_expect("She remembers being heard", kk_has("miyuki_cita_didengar") and kk_rel_get("miyuki","trust") == trust_before+5)
    $ kk_test_at(13,1,1)
    while kk_daily_place("miyuki") != "Gedung Kedokteran":
        $ kk_new_day()
        $ kk_test_expect("Medical faculty reachable", kk_bulan == 13)
    call kk_test_family_visit("Mi12","miyuki","d1","Gedung Kedokteran","Bantu ia mengulang bahan belajarnya.")
    $ kk_test_expect("Start of clinic changes Miyuki's schedule", stage["miyuki"] == 2 and kk_get("karier_miyuki") == 75)
    $ kk_test_at(14,1,3)
    $ fatigue = kk_get("kelelahan_miyuki")
    call kk_test_family_visit("Mi13","miyuki","d6","Rumah Sakit Tachibana","Tunggu dan dengarkan setelah ia selesai.")
    $ kk_test_expect("Call from her mother", kk_get("kelelahan_miyuki") == min(100,fatigue+8))
    $ kk_test_at(25,1,3)
    $ _lokasi = "Rumah Sakit Tachibana"
    call kk_test_family_visit("Mi21","miyuki","d6",_lokasi,"Bantu susun jadwalnya agar ia bisa segera masuk.")
    $ kk_test_expect("Rotation without sufficient closeness", kk_get("karier_miyuki") == 80 and kk_rel_get("miyuki","aff") < 25 and not kk_done("Mi-D09"))
    while kk_rel_get("miyuki","aff") < 25:
        $ kk_new_day()
        $ kk_slot = 3
        $ kk_minute = 0
        $ kk_test_expect("Patient shift remains reachable in this rotation", kk_bulan == 25)
        if kk_daily_place("miyuki") == _lokasi:
            $ kk_test_expect("Patient event waits until she knows the player", kk_social_event("miyuki",_lokasi) != "Mi-D09")
            $ kk_test_family_caption = "Balas sapaannya lalu pamit."
            call kk_do_talk("d6",_lokasi,"miyuki")
            $ kk_test_family_caption = None
    $ career_before = kk_get("karier_miyuki")
    $ hurt_before = kk_get("luka_miyuki_diri",15)
    call kk_test_family_visit("Mi-D09","miyuki","d6",_lokasi,"Temani Miyuki di ruang tunggu rumah sakit.")
    $ kk_test_expect("Support on the ward is recorded once", kk_get("karier_miyuki") == career_before+5 and kk_get("luka_miyuki_diri") == hurt_before-5 and kk_social_event("miyuki",_lokasi) != "Mi-D09")
    $ kk_test_at(30,14,3)
    $ kk_test_expect("Result not known on exam eve", not kk_window("Mi24"))
    $ fatigue = kk_get("kelelahan_miyuki")
    $ kk_test_expect("One risk factor before final preparation", fatigue >= 75 and kk_get("karier_miyuki") >= 40)
    $ money_before = saldo
    call kk_test_family_visit("Mi-D11","miyuki","d6","Rumah Sakit Tachibana","Bawakan makan malam dan beri ia waktu untuk istirahat.")
    $ kk_test_expect("Prep meal charged once", saldo == money_before-800 and kk_get("kelelahan_miyuki") == fatigue-8)
    $ kk_test_at(30,15,3)
    $ kk_test_expect("Passing recorded before the visit", kk_has("cbt_miyuki_lulus") and not kk_has("cbt_miyuki_gagal"))
    call kk_test_family_visit("Mi24","miyuki","d6","Rumah Sakit Tachibana","Ajak ia merayakannya.")
    $ _lokasi = "Rumah Sakit Tachibana"
    $ meals = 0
    $ kept = 0
    while not kk_miyuki_ready_to_refuse():
        $ kk_test_expect("Care is reachable before the third Christmas", kk_bulan < 33)
        if kk_daily_place("miyuki") == _lokasi:
            $ kk_test_speaker = "miyuki"
            call screen kk_location_view("d6",_lokasi)
            $ kk_test_expect("Miyuki is present", _return == ("talk","miyuki"))
            $ kk_test_speaker = None
            $ promised = "miyuki" in kk_promises
            $ bring_food = promised or kk_rel_get("miyuki","trust") >= 70
            $ kk_test_family_caption = "Bawakan makanan untuk Miyuki." if bring_food else "Janjikan bertemu lagi di sini besok pada waktu yang sama."
            $ money_before = saldo
            call kk_do_talk("d6",_lokasi,"miyuki")
            if bring_food:
                $ kk_test_expect("One meal purchased", saldo == money_before - 800)
                $ meals += 1
            if promised:
                $ kept += 1
            $ kk_test_family_caption = None
        $ kk_new_day()
        $ kk_slot = 3
        $ kk_minute = 0
    $ before = kk_get("omiai_takeru")
    $ kk_test_expect("Promises and meals unlock refusal organically", meals > 0 and kept > 0 and before >= 70)
    call kk_test_family_visit("Mi-D12","miyuki","d6",_lokasi,"Dukung keputusan Miyuki.")
    $ kk_test_expect("Her refusal changes the household pressure", kk_get("omiai_takeru") == before-30)
    $ kk_test_at(33,24,3)
    $ kk_test_expect("The later proposal would qualify without her refusal", kk_get("omiai_takeru") < 70 <= kk_get("omiai_takeru")+30 and not kk_window("Mi25"))
    $ kk_test_at(36,31,4)
    $ kk_minutes(120)
    $ kk_test_expect("Pediatrics is the independent outcome at graduation", "E-MI-02" in kk_epilogue())
    call kk_evaluasi
    $ open(os.path.join(config.basedir,"clinic.ok"),"w").write("Clinic graduation: %d visits with food, %d promises kept; Hayase proposal absent: OK" % (meals,kept))
    $ renpy.quit()
