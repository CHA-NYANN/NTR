# Kouseikan — token desain (warna, tipografi, metrik).
# Ganti nilai di sini untuk reskin cepat. Palet: ink gelap + bone hangat + satu aksen berani.

define kk_ink     = "#141e26"   # latar utama, near-black hangat
define kk_ink2    = "#20303a"   # panel gelap
define kk_panel   = "#293d48"   # kartu
define kk_bone    = "#ece6dc"   # teks utama
define kk_bone2   = "#cfc8bd"
define kk_dim     = "#b1bfbd"   # teks sekunder
define kk_line    = "#52636c"   # garis/pembatas
define kk_accent  = "#ffb68b"   # aksen berani (vermilion)
define kk_acc2    = "#a9c9f2"   # aksen sekunder (biru listrik)
define kk_good    = "#36b388"
define kk_warn    = "#e0a21e"
define kk_bad     = "#dc3b3b"

# Tipografi dan ukuran logis pada kanvas 1920 × 1080.
define kk_display = "DejaVuSans.ttf"
define kk_body = "DejaVuSans.ttf"
define kk_mono = "DejaVuSans.ttf"
define kk_margin = 96
define kk_gap = 24

transform kk_enter:
    on show:
        alpha 0.0 yoffset 8
        easeout 0.18 alpha 1.0 yoffset 0

style kk_button is button:
    background Solid(kk_panel)
    hover_background Solid("#4a616b")
    selected_background Solid("#705445")
    selected_hover_background Solid("#815e4a")
    insensitive_background Solid(kk_ink2)
    padding (24, 12)
    yminimum 58

style kk_button_text is button_text:
    size 25
    color kk_bone
    hover_color "#ffffff"
    selected_color "#fff1df"
    insensitive_color "#849497"

style kk_heading is default:
    font kk_display
    size 56
    bold True
    color kk_bone

style kk_caption is default:
    size 22
    color kk_dim

style default:
    font kk_body
    color kk_bone

# Ukuran eksplisit menyisakan lebar viewport untuk daftar dan detail.
style vscrollbar:
    xsize 16
    base_bar Solid(kk_panel)
    thumb Solid(kk_line)
    hover_thumb Solid(kk_accent)
    unscrollable "hide"

style kk_slider is slider:
    left_bar Solid(kk_accent)
    right_bar Solid(kk_panel)
    thumb Transform(Solid(kk_bone), xsize=12)
    hover_thumb Transform(Solid("#ffffff"), xsize=12)
    thumb_offset 6
