# Original instrumental loops. Scene mood takes precedence over character theme.
define config.main_menu_music = "audio/bgm/title.wav"

init python:
    KK_BGM_CHARACTER = {
        "Mi": "miyuki", "Mo": "moeka", "C": "chiasa", "Y": "yutaka",
        "K": "koita", "H": "harumi", "N": "nagisa", "S": "shiori",
    }

    KK_BGM_MOOD = {
        "tension": (
            "C08 C10 C13 K14 K15 K17 Y06 Y14 Mo04 Mo11 Mo13 Mo15 Mo23 "
            "H13 H15 H17 H18 S05 S12 S13 S18 S21 S22 S24 N13 N15 N16 N18 "
            "Mi07 Mi16 Mi17 Mi20 C-D03 C-D15 K-D10 K-D17 Mi-D10 Mo-D05 N-D04 "
            "S-D06 S-D13 S-D14 X-D01 X-D10 X-D12"
        ),
        "intimacy": (
            "C15 K04 K05 K22 Y10 Y11 Y16 H04 H16 S03 N09 N20 Mi04 Mi18 "
            "C-D14 K-D02 K-D07 K-D16 Mi-D02 Mi-D08 Y-D11"
        ),
        "aftermath": (
            "C14 K25 Y07 Y15 Mo17 Mo25 Mo26 H19 N11 N17 Mi15 Mi19 Mi23 "
            "C-D09 K-D05 K-D13 K-D14 Mo-D06 Mo-D11 N-D09 S-D09"
        ),
        "night": "C-D01 H-D03 Mi-D05 N-D03 Y-D07",
        "graduation": "K27",
        "retreat": "Mi05 Mo02 S02",
        "home": "X-D05",
        "platform": "Y-D10",
    }
    KK_BGM_EVENT = {
        event: cue for cue, events in KK_BGM_MOOD.items() for event in events.split()
    }

    KK_BGM_LABEL = {
        "kk_main": "campus",
        "kk_world_loop": "campus",
        "kk_explore_loop": "campus",
        "kk_evaluasi": "graduation",
        "kk_draw_at_home": "chiasa",
        "kk_mio_deadline": "tension",
        "kk_show_portfolio": "chiasa",
        "kk_dorm_tea": "harumi",
        "kk_second_meal": "home",
        "kk_check_desk": "quiet",
        "kk_torn_koko": "aftermath",
        "kk_visit_kisaragi": "yutaka",
        "kk_message_kisaragi": "yutaka",
        "kk_kansai_letter": "harumi",
        "kk_overheard_call": "tension",
        "kk_miyuki_refuses": "aftermath",
        "kk_library_rest": "quiet",
        "kk_pediatric_patient": "miyuki",
        "kk_exam_eve": "quiet",
        "kk_rest_home": "home",
        "kk_bedside_phone": "night",
        "kk_bedside_contacts": "night",
        "kk_saionji_tea": "shiori",
        "kk_shiori_question": "shiori",
        "kk_inspect_board": "quiet",
        "kk_phone_rematch": "nagisa",
        "kk_pudding": "intimacy",
    }

    KK_BGM_DISTRICT = {
        "d2": "home", "d3": "quiet", "d4": "city", "d5": "city",
        "d6": "quiet", "d7": "retreat", "onsen": "retreat",
    }

    def kk_bgm(cue, fade=0.65, level=1.0):
        path = "audio/bgm/" + cue + ".wav"
        renpy.music.play(path, channel="music", loop=True, tight=True, if_changed=True,
                         fadeout=fade, fadein=fade, relative_volume=level)

    def kk_bgm_location(district, place=""):
        hour = (6 + kk_slot * 4 + kk_minute // 60) % 24
        if hour >= 20 or hour < 6:
            cue = "night"
        elif place in ("Perpustakaan Pusat", "Pusat Konseling", "Klub Catur"):
            cue = "quiet"
        elif place in ("Taman Kampus", "Taman Lingkungan"):
            cue = "retreat"
        elif place in ("Kafe Komorebi", "Asrama Putri"):
            cue = "home"
        else:
            cue = KK_BGM_DISTRICT.get(district, "campus")
        kk_bgm(cue)

    def kk_bgm_event(event):
        prefix = event.rstrip("0123456789").removesuffix("-D")
        kk_bgm(KK_BGM_EVENT.get(event) or KK_BGM_CHARACTER.get(prefix, "campus"))

    def kk_bgm_ending(kind):
        cue = {
            "Romantis": "intimacy", "Neutral": "graduation", "Koita": "koita",
            "Bad": "aftermath", "Broken": "aftermath", "Distorted": "tension",
            "Khusus": "system",
        }.get(kind, "graduation")
        kk_bgm(cue)

    def kk_bgm_label(label, abnormal):
        if isinstance(label, str) and label.startswith("kkscene_"):
            kk_bgm_event(label[len("kkscene_"):].replace("_", "-"))
        elif label in KK_BGM_LABEL:
            kk_bgm(KK_BGM_LABEL[label])

    config.label_callbacks.append(kk_bgm_label)
