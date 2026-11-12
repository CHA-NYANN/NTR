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
            return renpy.run(selected.action)
        if name == "kk_choice_panel":
            screen = renpy.get_screen("kk_choice_panel")
            if screen:
                rows = screen.scope["rows"]
                selected = next((row for row in rows if kk_test_romance() and row[0].startswith("Tawarkan pergi bersama")),rows[0])
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
    $ balance_before = saldo
    call kk_do_activity("Kantin Pusat","makan")
    $ kk_test_expect("Meal", saldo == balance_before - 800 and body["lapar"] < 20)
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
    $ kk_test_at(8,2,4)
    $ kk_minute = 60
    $ kk_test_expect("Mio only writes about an accepted project at eleven", kk_mio_message() == bool(os.environ.get("KK_ART_WIN")))
    if kk_mio_message():
        call kk_mio_deadline
        $ kk_test_expect("Mio remembers honest answer", kk_has("mio_tahu_kesulitan") and not kk_mio_message())
    $ kk_test_at(10,1,0)
    while not kk_pending_talk("harumi","d7","Kuil"):
        $ kk_advance()
        $ kk_test_expect("Hatsumode within New Year", kk_hari_n <= 3)
    call kk_do_talk("d7","Kuil","harumi")
    $ kk_test_expect("Interpreting the fortune unlocks late tea", kk_get("kejelasan_harumi") == (40 if kk_test_romance() else 30))
    $ kk_test_at(10,5,4)
    $ kk_minute = 180
    while not kk_social_event("harumi", "Asrama Putri"):
        $ kk_advance()
        $ kk_test_expect("Dorm tea reachable at one", kk_bulan == 10)
    call kk_do_talk("d1", "Asrama Putri", "harumi")
    $ kk_test_expect("Dorm tea happens once", kk_done("H-D01") and kk_get("kejelasan_harumi") == (50 if kk_test_romance() else 35))
    $ kk_test_at(12,10,3)
    $ kk_test_expect("Lobby visit respects host and location", kk_father_visit("Apartemen Yutaka") == (kk_host == "yutaka") and not kk_father_visit("Kos Moeka"))
    if kk_host == "yutaka":
        call kk_visit_kisaragi
        $ kk_test_expect("Father visit opens mother message", kk_family_bond() == 40 and not kk_father_visit("Apartemen Yutaka") and kk_mother_message())
        call kk_message_kisaragi
        $ kk_test_expect("Reply recorded only once", kk_done("Y-D08") and not kk_mother_message() and kk_family_bond() == 45)
    $ kk_test_at(13,1,1)
    while not kk_pending_talk("harumi","d1","Gedung Sains & Lab"):
        $ kk_advance()
        $ kk_test_expect("Spring lab meeting bounded", kk_bulan == 13)
    call kk_do_talk("d1","Gedung Sains & Lab","harumi")
    $ kk_test_expect("Harumi remembers earlier conversation", kk_has("harumi_dibantu_menamai_emosi"))
    $ kk_test_expect("Father call is host specific", ("Y09" in kk_pending_enter("d3","Apartemen Yutaka")) == (kk_host == "yutaka"))
    if kk_host == "yutaka":
        call kk_play_scene("Y09")
        $ kk_test_expect("Family listens to graduation plans", kk_family_bond() == 55)
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
    $ kk_test_at(31,1,1)
    $ kk_test_expect("Offer only for Yutaka", bool(kk_pending_enter("d3","Apartemen Yutaka")) == (kk_host == "yutaka"))
    if kk_host == "yutaka":
        call kk_play_scene("Y17")
        $ kk_test_expect("Career choice sticks", kk_has("job_family"))
    $ kk_test_at(33,24,3)
    if not kk_pending_talk("miyuki","d6","Rumah Sakit Tachibana"):
        $ kk_test_at(33,25,3)
    $ kk_test_expect("Proposal due to pressure accumulated over years", kk_pending_talk("miyuki","d6","Rumah Sakit Tachibana") == ["Mi25"])
    call kk_do_talk("d6","Rumah Sakit Tachibana","miyuki")
    $ kk_test_expect("Miyuki family ending", ("E-MI-05" if kk_test_romance() else "E-MI-04") in kk_epilogue())
    $ kk_test_at(33,26,1)
    $ kk_test_expect("Late host and missed opportunities", "Mi09" in kk_missed and not kk_pending_enter("d3","Apartemen Yutaka"))
    $ kk_test_at(35,1,3)
    $ kk_minute = 220
    $ kk_rel("nagisa","aff", 30)
    $ kk_priority_contacts.append("nagisa")
    $ kk_test_expect("Normal priority interrupted at 22:00", kk_sleep(90) == "nagisa" and kk_clock() == "22:00" and not kk_done("N-D01"))
    $ kk_phone_mode = "senyap"
    $ kk_test_expect("Silent sleeping crosses midnight", kk_sleep(360) is None and kk_clock() == "04:00" and kk_hari_n == 2 and "N-D01" in kk_missed)
    $ kk_test_expect("Twenty minute nap", kk_sleep(20) is None and kk_clock() == "04:20")
    $ kk_test_at(36,31,4)
    $ kk_minutes(120)
    $ kk_test_expect("Graduation on normal clock", kk_graduated and kk_epilogue()[0] == ("E-SI-02" if kk_test_romance() else "E-SI-13"))
    $ kk_test_expect("Organic Harumi ending only for this journey", ("E-HA-01" in kk_epilogue()) == kk_test_romance())
    $ kk_test_expect("Reconciled heir after graduation", ("E-YH-01" in kk_epilogue()) == (kk_host == "yutaka"))
    $ kk_test_expect("Thirty-five monthly deposits", len([t for t in kk_transactions if t[2].startswith("Uang saku")]) == 35 and kk_transactions[-1][4] == saldo)
    $ kk_test_expect("Shena builds her own style", ("E-CF-08" in kk_epilogue()) == bool(os.environ.get("KK_ART_WIN")))
    call screen kk_wallet
    call kk_evaluasi
    $ open(os.path.join(config.basedir, ("artist" if os.environ.get("KK_ART_WIN") else kk_host)+".ok"),"w").write(kk_host+" · life, four VN scenes, save/load, rollback, expiry, delayed response, epilogue: OK")
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
