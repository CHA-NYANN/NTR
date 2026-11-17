# Daftar pusat eid dinamis batch tambahan yang punya label kkscene_<eid> sendiri
# dan dirutekan generik oleh kk_social_scene / kk_host_dyn. Prefix K-D tidak
# dimasukkan karena sudah dirutekan oleh cabang khusus di kk_social_scene.

init python:
    KK_DYNX = set([
        # Moeka
        "Mo-D01","Mo-D02","Mo-D03","Mo-D04","Mo-D05","Mo-D06","Mo-D07",
        "Mo-D08","Mo-D09","Mo-D10","Mo-D11","Mo-D12","Mo-D13",
        # Harumi
        "H-D02","H-D03","H-D04","H-D06","H-D08","H-D09","H-D10","H-D11","H-D12",
        # Shiori
        "S-D01","S-D02","S-D05","S-D06","S-D10","S-D11","S-D12",
        # Chiasa (host)
        "C-D01","C-D04","C-D05","C-D06","C-D08","C-D09","C-D10","C-D11",
        "C-D12","C-D13","C-D14","C-D15",
        # Yutaka (host)
        "Y-D01","Y-D02","Y-D04","Y-D05","Y-D06","Y-D07","Y-D09","Y-D10","Y-D11",
        # lintas-karakter
        "X-D01","X-D02","X-D03","X-D04","X-D05","X-D06",
        "X-D07","X-D08","X-D09","X-D10","X-D11","X-D12",
        # lain
        "Mi-D13","N-D04",
    ])
