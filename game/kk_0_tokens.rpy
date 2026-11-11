# Kouseikan — token desain (warna, tipografi, metrik).
# Ganti nilai di sini untuk reskin cepat. Palet: ink gelap + bone hangat + satu aksen berani.

define kk_ink     = "#121016"   # latar utama, near-black hangat
define kk_ink2    = "#1b1920"   # panel gelap
define kk_panel   = "#232029"   # kartu
define kk_bone    = "#ece6dc"   # teks utama
define kk_bone2   = "#cfc8bd"
define kk_dim     = "#8d877f"   # teks sekunder
define kk_line    = "#332f3b"   # garis/pembatas
define kk_accent  = "#e4532b"   # aksen berani (vermilion)
define kk_acc2    = "#4a7bf0"   # aksen sekunder (biru listrik)
define kk_good    = "#36b388"
define kk_warn    = "#e0a21e"
define kk_bad     = "#dc3b3b"

# Font: default bundel Ren'Py. Taruh font grotesk kondensat di game/fonts/ dan ganti kk_display
# untuk hasil jauh lebih "cakep". Dibiarkan aman agar langsung jalan.
define kk_display = "DejaVuSans.ttf"
define kk_body    = "DejaVuSans.ttf"
define kk_mono    = "DejaVuSans.ttf"

# Transform reusable
transform kk_slidein(delay=0.0):
    alpha 0.0 xoffset 40
    pause delay
    parallel:
        ease 0.45 alpha 1.0
    parallel:
        easeout 0.5 xoffset 0

transform kk_pop(delay=0.0):
    alpha 0.0 yoffset 14
    pause delay
    ease 0.35 alpha 1.0 yoffset 0

transform kk_hoverbar:
    on hover:
        linear 0.12 xoffset 14
    on idle:
        linear 0.12 xoffset 0
