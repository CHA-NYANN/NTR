# Kouseikan — definisi rute + hook efek pilihan (vertical slice).
# Hook = efek poin nyata untuk event yang sudah diwire. Event lain: pilihan dicatat + teks efek ringkas.

init python:

    KK_ROUTES = [
        ("miyuki","Rute Masokis","gerbang Mi16 · arah luka berpindah"),
        ("nagisa","Rute Yandere","gerbang N14 · sasaran cemburu berpindah"),
        ("harumi","Rute Eksploitasi","gerbang H13 · Ogawa & dana lab"),
        ("moeka","Rute Death-Flag","5 jendela · Malam Tanpa Balasan"),
        ("shiori","Rute Revenge","paling sulit · senyum tak terbaca"),
        ("chiasa","Koita Success / Manipulasi","tabu saudara tiri"),
        ("koita_bl","Koita & Rute BL","NTR sempurna · celah sistem"),
    ]

    # Pilihan yang mengarah ke jalur Force (adegan di-skip; lihat engine).
    KK_FORCE_CHOICES = {
        "Mi05-C": "miyuki", "H04-C": "harumi", "Mo04-C": "moeka",
        "N12-C": "nagisa", "S04-C": "shiori",
    }

    # Hook efek: fungsi dipanggil saat (ID,key) dipilih di event yang diwire.
    def _h(fn): return fn
    KK_HOOKS = {}
    def _hook(key, fn): KK_HOOKS[key] = fn

    # --- Miyuki thread (contoh wiring penuh) ---
    _hook("Mi01-A", lambda: (kk_rel("miyuki","aff",4), kk_rel("miyuki","trust",3), kk_persona_nudge("ramah")))
    _hook("Mi01-B", lambda: (kk_rel("miyuki","trust",6), kk_adj("dimanja_miyuki",4), kk_persona_nudge("ramah")))
    _hook("Mi01-C", lambda: (kk_rel("miyuki","aff",-3), kk_persona_nudge("dingin")))
    _hook("Mi03-A", lambda: (kk_adj("kelelahan_miyuki",-8), kk_adj("dimanja_miyuki",4),
                              kk_rel("miyuki","trust",6), kk_adj("sena_curiga",5),
                              kk_stage("miyuki",1)))
    _hook("Mi03-B", lambda: (kk_adj("kelelahan_miyuki",-4), kk_rel("miyuki","aff",-2),
                              kk_stage("miyuki",1)))
    _hook("Mi03-C", lambda: (kk_rel("miyuki","intim",6), kk_stage("miyuki",1)))
    _hook("Mi05-A", lambda: kk_rel("miyuki","trust",5))
    _hook("Mi05-B", lambda: kk_rel("miyuki","intim",4))
    # Mi05-C → jalur Force (ditangani KK_FORCE_CHOICES)

    # --- Nagisa ---
    # Kepribadian host: tidak dipilih di menu, muncul dari pilihan dalam adegan.
    _hook("N01-A", lambda: (kk_rel("nagisa","aff",3), kk_adj("kelekatan_nagisa",4), kk_persona_nudge("agresif")))
    _hook("N01-B", lambda: (kk_rel("nagisa","aff",-2), kk_persona_nudge("dingin")))
    _hook("N01-C", lambda: (kk_rel("nagisa","intim",3), kk_rel("nagisa","jeal",3), kk_persona_nudge("genit")))
    _hook("N03-A", lambda: (kk_adj("kelekatan_nagisa",8), kk_rel("nagisa","trust",5), kk_stage("nagisa",1), kk_persona_nudge("ramah")))
    _hook("N03-B", lambda: (kk_rel("nagisa","aff",2),))
    _hook("N03-C", lambda: (kk_rel("nagisa","aff",-4), kk_persona_nudge("dingin")))

    # N04-B menghasilkan penolakan dua minggu kemudian (Sistem Cabang §1).
    def kk_nagisa_confession():
        store.kk_due["koita_reply"] = kk_elapsed_days + 14
        store.kk_npc_rel["nagisa_koita"] = "menunggu jawaban"

    _hook("N04-A", lambda: kk_adj("kelekatan_nagisa", 5))
    _hook("N04-B", kk_nagisa_confession)
    _hook("N04-C", lambda: kk_flag("pengakuan_terputus"))
    _hook("N06-A", lambda: kk_flag("yuuto_bantu"))
    _hook("N06-B", lambda: kk_stage("nagisa", 2))
    _hook("N06-C", lambda: kk_stage("nagisa", 2))
    _hook("N-D01-A", lambda: (kk_rel("nagisa","intim",1), kk_adj("gengsi_nagisa",1)))
    _hook("N-D01-B", lambda: kk_flag("rematch_ditunda"))
    _hook("N-D01-C", lambda: (kk_rel("nagisa","intim",1), kk_adj("gengsi_nagisa",-1)))

    _hook("N-D02-A", lambda: (kk_adj("gengsi_nagisa",-2), kk_rel("nagisa","aff",2)))
    _hook("N-D02-B", lambda: kk_rel("nagisa","aff",5))
    _hook("N-D02-C", lambda: kk_flag("bekal_dikembalikan"))
    _hook("Mi-D03-A", lambda: kk_flag("koita_mencatat_pastry"))
    _hook("Mi-D03-B", lambda: kk_flag("pastry_disimpan"))
    _hook("Mi-D03-C", lambda: kk_flag("pastry_dibagi"))
    for key, delta in zip("ABCD",(10,5,-5,-10)):
        _hook("Mi-D01-" + key, lambda delta=delta: kk_adj("dimanja_miyuki",delta))

    def kk_run_hook(evid, key):
        h = KK_HOOKS.get(evid + "-" + key)
        if h:
            h()
            return True
        return False

