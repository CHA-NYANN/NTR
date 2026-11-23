# Pilihan tangan Kouseikan

Sumber: paket pemilik proyek `asset/kouseikan_paket_lengkap_tangan_dan_animasi.zip`. Semua 43 PNG di folder ini disalin tanpa perubahan piksel. Nama file latar dipersingkat menjadi `background.png`; sprite ditaruh di `sprites/`, dan frame overlay pemain di `animation/pilih_{yutaka,chiasa}/`.

Latar asli sudah memuat kedua tangan yang ditawarkan dan pertanyaan. Tombol memakai mask alfa sprite tangan sehingga area gelap di luarnya tidak bisa dipilih dengan mouse. Hover memberi sorotan ringan; nama host tidak ditampilkan sebelum dipilih. Kiri mengembalikan `yutaka`, kanan `chiasa`, sesuai alur prolog yang ada.

Sesudah klik: tombol dikunci, 20 frame tangan pemain berjalan dengan interval nominal 1/12 detik, lalu pilihan dikembalikan ke cerita. Clock frame dimulai saat memilih; frame terakhir ditahan, tidak diulang. Pada FPS rendah durasinya bisa lebih panjang agar pose akhir tetap sempat ditampilkan. Saat animasi sekunder dimatikan di pengaturan, pose akhir langsung tampil dengan timer 0,25 detik. `metadata.json` adalah metadata asli paket; jalur di dalamnya merujuk struktur ZIP sumber.

Canvas 1536×864 diskalakan seragam ke 1920×1080. Koordinat dan ukuran mask di `zzz_kk_secondary.rpy` berasal dari crop metadata dengan skala 1,25. Aset tangan lama tetap tersimpan untuk referensi; screen pilihan memakai paket baru ini.

QA terisolasi (tidak memakai save pemain):

```powershell
python tools/run_hand_choice_qa.py path/ke/renpy-sdk path/ke/folder-qa-baru
```
