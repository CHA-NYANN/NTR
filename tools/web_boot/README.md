# Kouseikan web startup

Alur: logo asli Zzz (2,5 detik; klik/Enter untuk lewati) → loading Kouseikan → frame game pertama. Mode reduced motion memakai intro 0,65 detik tanpa animasi. Tidak ada audio otomatis.

Progress mengikuti byte/progres tahap yang dilaporkan mesin Ren'Py. Tahap tanpa jumlah pasti menampilkan bintang bergerak tanpa persentase palsu. Overlay baru hilang ketika `window.presplashEnd()` dipanggil oleh mesin. Gagal mengunduh atau abort menampilkan tombol coba lagi dan detail diagnostik.

Setelah **setiap** export web Ren'Py, jalankan dari root proyek:

```powershell
python tools/apply_web_boot.py "path/ke/folder-web"
```

Ren'Py membuat ulang index.html ketika export. Tool ini memasang ulang shell ke index tersebut, menyalin `boot/`, dan menambahkan aset ke katalog PWA. Aman dijalankan ulang. Jalankan sebelum upload isi folder web ke repo `CHA-NYANN/kouseikan`/Vercel. Jangan menimpa renpy-pre.js atau renpy.js dengan versi berbeda dari export.

Tool mempertahankan game.zip, vendor engine, service worker, manifest, input native, dan impor/ekspor save. Gambar presplash lama tidak lagi dimuat; file lama tidak dihapus. IndexedDB/save pemain tidak diubah. Bila proses export atau engine berubah, uji hook DOM dan first-frame handoff lagi.

Logo `assets/studio-logo.jpg` adalah JPEG asli pemilik proyek, tanpa perubahan piksel. Bagian bantal dan tiga huruf ditampilkan lewat SVG clipping untuk animasi. Font Tinos Italic dan Nunito mengikuti aset yang sudah digunakan proyek.

Pemeriksaan kontrak JavaScript (Node 18+):

```powershell
node tools/test_web_boot.mjs
```

Pengujian ini tidak menggantikan pengujian visual/browser: periksa desktop, layar kecil, reduced motion, koneksi lambat/gagal, serta masuknya game ke menu.
