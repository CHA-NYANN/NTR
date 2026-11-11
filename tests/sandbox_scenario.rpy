# Driver is copied to a temporary game by run_living.py, never into production.
init python:
    import os
    def kk_test_input(name):
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
            return renpy.run(items[0].action)
        if name == "kk_choice_panel":
            screen = renpy.get_screen("kk_choice_panel")
            if screen:
                return renpy.run(screen.scope["rows"][0][1])
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
    $ kk_test_at(1,19,1)
    if kk_daily_place("miyuki") != "Taman Kampus":
        $ kk_test_at(1,19,2)
    if kk_daily_place("miyuki") != "Taman Kampus":
        $ kk_test_at(1,20,1)
    $ kk_test_expect("Hanami", kk_pending_enter("d1","Taman Kampus") == ["Mi01"])
    call kk_play_scene("Mi01")
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
    $ test_balance = saldo
    nar "Pemeriksaan simpan."
    if not os.environ.get("KK_TEST_LOADED"):
        $ renpy.save("qa-world")
        $ saldo -= 321
        $ os.environ["KK_TEST_LOADED"] = "1"
        $ renpy.load("qa-world")
    $ kk_test_expect("Save/load",saldo == test_balance and kk_done("Mi03"))
    $ test_before = len(choices_log)
    nar "Pemeriksaan rollback."
    $ kk_record_choice("N04","B")
    nar "Pemeriksaan sesudah pilihan."
    if not os.environ.get("KK_TEST_ROLLED"):
        $ os.environ["KK_TEST_ROLLED"] = "1"
        $ renpy.rollback(force=True, checkpoints=2, greedy=False)
    $ kk_test_expect("Rollback and replay once", len(choices_log) == test_before+1 and kk_due["koita_reply"] == kk_elapsed_days+14)
    $ kk_test_at(5,28,1)
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
    $ kk_test_at(33,26,1)
    $ kk_test_expect("Late host and missed opportunities", "Mi09" in kk_missed and not kk_pending_enter("d3","Apartemen Yutaka"))
    $ kk_test_at(36,31,4)
    $ kk_minutes(120)
    $ kk_test_expect("Graduation on normal clock", kk_graduated and kk_epilogue()[0] == "E-SI-13")
    call kk_evaluasi
    $ open(os.path.join(config.basedir, kk_host+".ok"),"w").write(kk_host+" · life, four VN scenes, save/load, rollback, expiry, delayed response, epilogue: OK")
    $ renpy.quit()

