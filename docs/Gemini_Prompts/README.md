# Paket prompt Kouseikan untuk Gemini Web

Tersedia **318 prompt adegan** (190 utama termasuk 8 node akhir, serta 128 dinamis), ditambah **220 prompt ending**. Total **538 prompt mandiri**. Semuanya dibuat dari naskah dan profil di repo; game tidak diubah oleh pembuat paket ini.

## Cara pakai

1. Buka [indeks](INDEX.md), pilih ID adegan yang mau dikerjakan. Contoh awal: [K01](adegan/koita/K01.md), [C01](adegan/chiasa/C01.md), atau [Y01](adegan/yutaka/Y01.md).
2. Buka file prompt, lalu **salin seluruh isinya** ke satu pesan Gemini Web. Boleh memakai chat baru untuk setiap adegan. Tidak perlu mengunggah semua paket atau berharap Gemini mengingat profil dari chat lain.
3. Gemini diminta mengembalikan satu blok label lengkap atau satu assignment ending. Simpan jawabannya dengan ID yang sama. Paket ini tidak memasang keluaran Gemini secara otomatis.
4. Untuk label bersama (misalnya prolog dan beberapa helper), prompt sudah memerintahkan perubahan hanya pada event sasaran. Tetap tinjau agar ID/cabang lain tidak ikut ditimpa.
5. Kalau puas, pasang hasil di label/assignment sumber yang tertulis pada prompt, lalu jalankan lint dan cek katalog. Periksa jumlah/urutan opsi, semua statement mekanik, host, dan kondisi. Lint tidak menilai konsistensi cerita atau mutu dialog.

Isi tiap prompt: premis, POV dua host, suara tokoh terkait, profil lengkap tokoh fokus, profil NPC yang disebut, hubungan awal, panduan lokal, katalog, koreksi kode/katalog, efek hook terkait sebagai referensi, kode/naskah acuan, serta format keluaran. Ending juga punya paket sendiri, contoh [E-KO-01](ending/KO/E-KO-01.md).

## Menjaga kesinambungan versi Gemini

Paket ini merekam sumber saat dibangun. Ia mengulang konteks dasar, tetapi belum mengetahui perubahan yang baru ditulis Gemini dan belum dimasukkan repo. Setelah satu adegan disetujui, masukkan hasilnya lebih dulu lalu bangun ulang paket. Untuk detail baru yang perlu berlaku lintas adegan (misalnya janji pribadi, kebiasaan, atau barang penting), catat di profil/desain yang benar dan tinjau sebelum membangun ulang. Jangan otomatis memperlakukan pilihan A/B/C dari adegan lain sebagai kejadian tetap.

Jika hanya ingin memperbaiki hasil dalam chat Gemini yang sama, kirim instruksi spesifik, misalnya: "Revisi seluruh label terakhir. Kurangi narator yang menjelaskan makna percakapan, tambah interaksi konkret sebelum pilihan, dan beri cabang B akibat yang lebih berbeda. Semua kondisi, opsi dan statement mekanik harus tetap persis seperti prompt awal. Keluarkan label lengkap."

Jika jawaban terpotong, gunakan: "Jawaban terpotong. Lanjutkan persis dari baris terakhir, tanpa mengulang bagian yang sudah ada dan tanpa menutup cabang lebih cepat. Pertahankan indentasi. Sesudah selesai, jangan menambah penjelasan." Gabungkan kedua bagian sebelum memasangnya. Jika konteks chat sudah kacau, mulai chat baru dengan prompt lengkap.

## Pengecualian yang sengaja dipertahankan

- K14/K15 tiga opsi; K19 B=masukan jujur, C=sabotase.
- K17 lima opsi; H08/N10/S10 dua opsi.
- Menu bersyarat, dispatch helper bersama, efek waktu/uang lama, dan percabangan otomatis Mo25 tidak diubah menjadi pola generik.
- Delapan node akhir tetap tidak dijadwalkan; menulisnya tidak menghubungkannya ke scheduler.
- `docs/story_bible.md` tidak dipakai.
- Kekerasan dan krisis boleh ditulis intens, tetapi tanpa metode kekerasan seksual, menyakiti diri, atau prosedur fitnah; Force tidak dibuat menjadi akhir romantis.

## Bangun ulang dan verifikasi paket

Dari root repo dengan PowerShell:

```powershell
& "D:/Punya Patra/Aplikasi/renpy-8.0.3-sdk/lib/py3-windows-x86_64/python.exe" docs/Gemini_Prompts/build_prompts.py
& "D:/Punya Patra/Aplikasi/renpy-8.0.3-sdk/lib/py3-windows-x86_64/python.exe" docs/Gemini_Prompts/build_prompts.py --check
```

Pembuat hanya menulis folder dokumentasi ini. `--check` memeriksa kecocokan seluruh prompt dengan sumber terkini tanpa menulis file. `manifest.json` memetakan ID, file sumber, label bersama dan hash naskah acuan. Sesudah memasang hasil Gemini di game, validasi proyek:

```powershell
& "D:/Punya Patra/Aplikasi/renpy-8.0.3-sdk/lib/py3-windows-x86_64/python.exe" "D:/Punya Patra/Aplikasi/renpy-8.0.3-sdk/renpy.py" . lint
& "D:/Punya Patra/Aplikasi/renpy-8.0.3-sdk/lib/py3-windows-x86_64/python.exe" tests/check_catalog.py
```

Cakupan mesin yang dijaga: 182/190 utama, 128/128 dinamis, 220/220 ending. Delapan node akhir termasuk dalam 190 utama, sehingga total adegan tetap 318.
