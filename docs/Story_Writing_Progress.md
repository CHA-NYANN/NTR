# Progres penulisan Kouseikan

Catatan kerja lokal, 17 November 2026. Daftar ini mencatat penulisan prosa, bukan cakupan implementasi mesin. Menu, urutan pilihan, hook, resolver, dan kondisi yang sudah ada menjadi acuan. `docs/story_bible.md` tidak digunakan.

## Batch selesai ditulis

| Karakter | Milestone yang diperkaya | Dinamis yang diperkaya | Ending aktif |
| --- | --- | --- | --- |
| Koita | K01–K25 | K-D01–K-D21 | E-KO-01–21, E-BL-01–08 |
| Miyuki | Mi01–Mi26 | Mi-D01–Mi-D14 | E-MI-01–14 |
| Nagisa | N01–N23 | N-D01–N-D13 | E-NA-01–14 |
| Harumi | H01–H23 | H-D01–H-D12 | E-HA-01–14 |
| Moeka | Mo01–Mo26 | Mo-D01–Mo-D13 | E-MO-01–13 |
| Shiori | S01–S24 | S-D01–S-D17 | E-SH-01–16 |
| Chiasa | C01–C17 | C-D01–C-D15 | E-CH-01–11, E-CF-01–13 |
| Yutaka | Y01–Y18 | Y-D01–Y-D11 | E-YU-01–08, E-YH-01–07 |
| Lintas rute / lainnya | — | X-D01–X-D12 | E-X-01–14, E-NPC-01–27, E-HP-01–07, E-SI-01–18, E-FO-01–15 |

Delapan node tanpa menu di `game/kk_story_stubs.rpy` sudah diisi: K26, K27, Mi27, N24, H24, S25, C18, Y19. Node tetap tidak ditambahkan ke penjadwal.

Jumlah prosa yang telah dikerjakan: **182 milestone terjadwal + 8 node penutup + 128 dinamis = 318 dari 318 ID event unik**, serta **220 dari 220 ending**. Delapan node merupakan bagian dari 190 ID utama katalog, bukan delapan ID tambahan.

Seluruh assignment ending sudah aktif, unik, dan dapat dievaluasi sebagai dictionary Python. Total teks ending: 25.196 kata, minimum tiga paragraf per ending. Statistik lint dialog: 3.146 blok, 62.264 kata. Statistik lint tidak memasukkan teks ending dalam dictionary.

## Status akhir

Penulisan seluruh item selesai. Pemeriksaan struktural sudah memastikan 190/190 ID utama dan 128/128 ID dinamis memiliki panduan yang tercakup; semua label `kkscene_*` dimulai dengan `kk_scene_enter`; tidak ada dialog tanpa atribusi; delapan node penutup tetap tanpa menu/cabang. Tidak ada assignment ending kosong yang tersisa.

Uji integrasi akhir setelah seluruh teks, koreksi pembicara NPC, dan format helper seni selesai: **7/7 OK**, proses berakhir dengan exit code 0. Skenario klinik menegaskan 15 kunjungan membawa makanan, 7 janji ditepati, dan proposal Hayase tidak muncul.

## Validasi dan catatan

- Lint Ren’Py setelah setiap batch dan seluruh penulisan: bersih (0 error).
- `tests/check_catalog.py`: tetap 182/190 utama, 128/128 dinamis, 220/220 ending. Angka tersebut adalah cakupan mesin, bukan jumlah prosa yang selesai.
- `tests/run_living.py`: **7/7 OK pada versi akhir**: Yutaka, Chiasa, Chiasa seniman, keluarga keep/reveal/admit, dan klinik sampai wisuda.
- Python tidak ada di PATH. Gunakan `D:/Punya Patra/Aplikasi/renpy-8.0.3-sdk/lib/py3-windows-x86_64/python.exe` untuk menjalankan tes.
- K14/K15 tetap tiga opsi; K19 tetap B=masukan jujur dan C=sabotase, sesuai koreksi pengguna.
- K17 tetap lima opsi sesuai implementasi, sehingga menu lima opsinya dipertahankan.
- H04 opsi C tetap bercerita tentang diri sesuai menu/hook, meski komentar lama menyebut meninggalkan.
- N13 opsi C tetap bicara sebagai Chiasa sesuai implementasi, meski ringkasan panduan berbeda.
- Koko diperbaiki dalam prosa menjadi kelinci hadiah Koita, sesuai profil canon. Panggilan Nacchan-oneechan diperbaiki menjadi panggilan Chiasa untuk Nagisa.
- Ogiwara di H-D09 diperbaiki sebagai pengelola asrama, bukan teman lab. Aya pada batch Moeka harus mengikuti profil sebagai ibu, bukan kakak.
- Helper yang sudah memiliki efek waktu, kondisi host, pilihan bersyarat, atau efek lain dipertahankan. Tidak menambahkan hook atau sistem poin baru.
- Ada banyak perubahan lokal sebelum pekerjaan ini dimulai. Jangan menimpa atau mengembalikan perubahan pengguna. Tidak ada commit/push.

- C-D10 dan C-D11 tetap tiga opsi mengikuti kode; komentar ringkas hanya menyebut dua. H08, N10, dan S10 tetap dua opsi; K17 tetap lima opsi.
- Menu bersyarat Miyuki (Mi-D02, Mi-D11, Mi24) dipertahankan agar opsi yang bergantung pada hasil ujian atau biaya tidak berubah menjadi selalu tersedia. Efek waktu/uang pada helper tetap dipertahankan.
- Pengarah input di `tests/sandbox_scenario.rpy` disesuaikan agar pilihan N02 yang sengaja memperlambat permainan tetap dipilih sesudah konversi ke `kk_choice_panel`. Assertion skenario tidak dilonggarkan.
- Force, fitnah, dan krisis menyakiti diri ditulis melalui ketegangan, keadaan batin, respons orang sekitar, serta akibat; tanpa uraian metode teknis. Tidak ada ending romantis dengan pelaku Force.
