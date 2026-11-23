# Pilihan tangan Kouseikan

Sumber: paket pemilik proyek `asset/kouseikan_paket_lengkap_tangan_dan_animasi.zip`. Seluruh PNG disalin tanpa perubahan piksel. Screen menggunakan satu latar, dua sprite mask tangan yang ditawarkan, serta **satu PNG tangan pemain untuk setiap pilihan** (`sprites/tangan_player_pilih_{yutaka,chiasa}.png`).

Latar asli sudah memuat kedua tangan yang ditawarkan dan pertanyaan. Tombol memakai mask alfa sprite tangan sehingga area gelap di luarnya tidak bisa dipilih dengan mouse. Hover memberi sorotan ringan; nama host tidak ditampilkan sebelum dipilih. Kiri mengembalikan `yutaka`, kanan `chiasa`, sesuai alur prolog yang ada.

Sesudah klik: tombol dikunci, PNG tangan pemain digeser dari bawah layar ke posisi akhir menggunakan ATL `easeout` selama 1,3 detik, ditahan 0,3 detik, lalu pilihan dikembalikan ke cerita. Hanya posisi yang berubah, tanpa pergantian frame, rotasi atau perubahan ukuran saat bergerak. `showif` memulai gerak saat dipilih, sehingga menunggu lama di layar atau masuk ulang tidak mempercepat animasi. Saat animasi sekunder dimatikan, pose akhir langsung tampil dengan timer 0,25 detik.

Folder `animation/` dari implementasi sebelumnya tetap disimpan sebagai referensi sumber. Screen tidak merujuk atau memuat frame tersebut; `build.classify(..., None)` mengecualikannya dari export berikutnya. Lima PNG yang diperlukan screen berjumlah sekitar 0,89 MB, dibanding 3,42 MB untuk aset/frame runtime sebelumnya. `metadata.json` tetap metadata asli ZIP; jalur di dalamnya merujuk struktur sumber, bukan dependensi runtime.

Canvas 1536×864 diskalakan seragam ke 1920×1080. Koordinat dan ukuran mask di `zzz_kk_secondary.rpy` berasal dari crop metadata dengan skala 1,25. Aset tangan lama tetap tersimpan untuk referensi; screen pilihan memakai paket baru ini.

QA terisolasi (tidak memakai save pemain):

```powershell
python tools/run_hand_choice_qa.py path/ke/renpy-sdk path/ke/folder-qa-baru
```

Runner sengaja tidak menyalin folder frame lama. Uji memeriksa posisi gerak dari awal ke akhir, klik/mask kedua host, lock, mode tanpa animasi, masuk ulang, serta pilihan setelah menunggu lebih lama daripada durasi gerak.
