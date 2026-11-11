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

    # --- Nagisa prolog ---
    # Kepribadian host: tidak dipilih di menu, muncul dari pilihan ini sendiri.
    _hook("N01-A", lambda: (kk_rel("nagisa","aff",3), kk_adj("kelekatan_nagisa",4), kk_persona_nudge("agresif")))
    _hook("N01-B", lambda: (kk_rel("nagisa","aff",-2), kk_persona_nudge("dingin")))
    _hook("N01-C", lambda: (kk_rel("nagisa","intim",3), kk_rel("nagisa","jeal",3), kk_persona_nudge("genit")))

    def kk_run_hook(evid, key):
        h = KK_HOOKS.get(evid + "-" + key)
        if h:
            h()
            return True
        return False
