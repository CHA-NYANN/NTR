# Perpanjang jatah "possible infinite loop" Ren'Py (renpy/execution.py) untuk
# build WEB. Ini BUKAN infinite loop sungguhan — sudah diverifikasi tidak ada
# `while True`/loop jump-ke-diri-sendiri di kode. Watchdog bawaan Ren'Py
# membatalkan proses kalau >1000 statement script berjalan beruntun tanpa
# interaksi pemain dan itu makan waktu lebih dari jatahnya (default 60 detik,
# x5 di build non-developer = 300 detik via renpy.not_infinite_loop).
#
# Konten game ini sudah tumbuh besar (~5000+ blok dialog, ratusan `init python:`
# + ribuan statement `define`/style/katalog yang dieksekusi berurutan saat
# start). gui.rpy sengaja dijalankan lebih dulu dari file lain
# (`init offset = -2`) dan berisi ratusan `define gui.xxx = ...` beruntun tanpa
# reset — di desktop ini selesai dalam milidetik, tapi di web/WebAssembly tiap
# statement Python jauh lebih lambat, sehingga total waktu startup bisa
# melebihi jatah 300 detik dan watchdog salah mengira ini infinite loop
# ("Exception: Possible infinite loop." di gui.rpyc).
#
# Jalankan SEPALING AWAL (lebih awal dari gui.rpy yang init offset = -2) untuk
# memberi jatah waktu besar HANYA untuk fase startup ini. Tidak mematikan
# watchdog secara permanen — gameplay normal setelah ini tetap diawasi seperti
# biasa (lihat [[project-kouseikan-web-build]]).
init -999 python:
    renpy.not_infinite_loop(600)
