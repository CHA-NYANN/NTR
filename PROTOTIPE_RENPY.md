# Kouseikan — Prototipe Ren'Py

Status: 🟡 kerangka teknis. **Belum ada story** — teks hanya poin utama (awal → pilihan → akibat ringkas). Lint bersih (Ren'Py 8.3.2, 0 error, 29 screen).

Dua kontributor di repo ini sejauh ini: kerangka data/engine/navigasi (sesi ini) dan redesign visual + playtest Windows nyata oleh **Cleopatra H.A** (lihat [docs/Playtest_UI.md](docs/Playtest_UI.md) dan commit `ui/editorial-playtest`). UI final (token, `say`, HUD, save/load, riwayat, galeri) adalah hasil kerjanya — jangan ditimpa tanpa alasan kuat.

## Menjalankan
1. Buka Ren'Py SDK (terdeteksi di `D:/Punya Patra/Aplikasi/renpy-8.0.3-sdk/`).
2. Launcher → pilih proyek folder `NTR` ini → **Launch Project**.
3. Atau lint ulang: `renpy.py "D:/Punya Patra/Projek/Glacial Remembrance/NTR" lint`.

## Arsitektur navigasi: Hybrid Location Navigation + Cinematic VN ⭐
Arahan desain terbaru (bukan bebas interpretasi): dunia dinavigasi lewat **distrik → lokasi** (menu kontekstual, **bukan** top-down/free-roam — ✅ GDD 6A, 6L.6), dan setiap interaksi/peristiwa penting masuk ke presentasi **Classic VN 2D** sinematis. Dua mode ini harus terasa satu pengalaman, bukan dua UI terpisah.

**Alur tiap pemilihan lokasi** (`kk_world_location_loop` di `kk_world.rpy`):
1. Validasi lokasi tersedia (daftar dari distrik yang dipilih).
2. Waktu maju (`kk_advance(1)` — tubuh menanggung, konsisten dengan dokumen sistem).
3–4. Cek apakah ada event milestone yang memenuhi syarat **di lokasi dan bulan ini** (`kk_pending_here`).
5. Jika ada → masuk adegan VN (`call kk_event(evid, reveal=False)`).
6. Akibat diterapkan lewat hook (`KK_HOOKS`), **tidak diucapkan langsung** — baru terbaca lewat Status/perilaku nanti.
7. Kembali ke navigasi dunia secara natural — lokasi yang sama, bukan menu global.

**Jadwal NPC tidak ditampilkan ke pemain** (✅ 6L.1/6L.7): layar lokasi **tidak** memberi tanda "ada sesuatu di sini". Pemain datang tanpa tahu, seperti simulasi dunia yang sesungguhnya — ini keputusan sengaja, bukan kekurangan.

**Data distrik/lokasi** diambil dari `docs/Jadwal_Harian_NPC.md` §2 (D1–D7), bukan dikarang di `kk_world.rpy`. Event milestone yang sudah diwire ke (bulan, distrik, lokasi) nyata: N01 (M01, Gedung Arsitektur), Mi01 (M01, Taman Kampus), N03 (M03, Gedung Arsitektur), Mi03 (M04, RS Tachibana). **Sengaja belum diwire** ke navigasi harian: Mi05 (M05b, hub Gasshuku Vila — perjalanan multi-hari, bukan lokasi harian biasa) dan N06 (M07, perlu NPC Yuuto yang belum ada). Keduanya tetap ada dan bisa dimainkan lewat Alat Uji, tidak dihapus.

## Alat uji (dipisah dari gameplay normal, tidak dihapus)
Diakses lewat tombol kecil "Alat uji" di layar peta distrik — **bukan** tombol menu utama lagi:
- **Jelajah semua cabang** — mainkan bebas satu dari 190 event, tanpa syarat lokasi/bulan.
- **Galeri ending** — 220 ending, **mengandung spoiler** (sebelumnya ada di menu utama; dipindah sesuai catatan playtest Cleopatra sendiri soal risiko spoiler).
- **Lompat ke evaluasi (M36)** — pintasan pengujian resolver ending.

## Yang sudah jalan
- **Main menu**: Mulai / Lanjutkan / Muat / Pengaturan / Keluar (galeri sudah dipindah ke Alat Uji).
- **Pilih rute** (Male/Female) → **prolog** — kepribadian host **tidak dipilih di menu** (✅ GDD 6Q.2): terbentuk dari pilihan nyata (lihat `kk_persona_nudge` di `kk_data_routes.rpy`), dibaca pasif lewat panel Status (`kk_persona_label`).
- **Navigasi dunia**: peta 7 distrik → daftar lokasi → **masuk lokasi sebagai tempat hidup**: siapa yang ada (kehadiran NPC kontekstual dari jadwal, `kk_present_here`), apa yang bisa dilakukan (aktivitas: makan/kerja/belajar/santai yang menggerakkan `body`+`saldo` nyata), dan peristiwa yang muncul karena konteks.
- **Interaksi karakter**: berbicara dengan orang yang hadir → obrolan singkat (nada jawaban membentuk hubungan + kepribadian, tanpa diumumkan) **atau** memicu event milestone bila orang & waktu & tempatnya tepat — organik, tanpa tanda "event di sini".
- **Waktu**: slot → hari (overflow), bulan maju lewat **timeskip eksplisit** ("Lewati waktu ke bulan depan"), bukan melesat karena aktivitas. Tubuh menanggung tiap tindakan.
- **Vertical slice** M01–M04: Mi01 (masuk Taman Kampus, bulan 1), N01 (ajak bicara Nagisa di Gedung Arsitektur, bulan 1), N03 (bulan 3), Mi03 (ajak bicara Miyuki di RS Tachibana, bulan 4) — ditemukan lewat hidup di dunia, bukan dipanggil dari menu.
- **STATUS**: kondisi tubuh + hubungan kualitatif (afeksi/kepercayaan) + pola kepribadian — angka mentah tetap tersembunyi.
- **Jalur Force**: non-operasional — layar hitam, "Tercatat.", lompat ke aftermath + flag konsekuensi (`kk_engine.rpy` → `kk_force_consequences`). Lihat `docs/Alur_Cabang/09 §2` — tidak ada metode/adegan di kode.

## Arsitektur (game/)
| File | Isi |
|---|---|
| `kk_0_tokens.rpy` | token desain (warna, font, style `kk_button`/`kk_heading`) — **punya Cleopatra, jangan timpa** |
| `kk_state.rpy` | semua state + tulang punggung 36 bulan + metadata karakter |
| `kk_engine.rpy` | poin, ambang, jadwal NPC (flavor), Force abstrak, **resolver ending**, `kk_persona_*`, `kk_done` |
| `kk_world.rpy` | **navigasi distrik→lokasi**, peta milestone-ke-lokasi, loop orkestrasi 7-langkah, Alat Uji |
| `kk_data_routes.rpy` | definisi rute + **hook efek pilihan** (wiring poin per event) |
| `kk_chars.rpy` | karakter bicara (ctc indikator lanjut — punya Cleopatra) |
| `kk_flow.rpy` | prolog, pembuka M01, **pemutar event generik** (`kk_event`, param `reveal`), Force, evaluasi |
| `kk_data_kk_events_main.rpy` | **190 event** (autogenerated dari `Karakter/**/Event_*.md`) |
| `kk_data_kk_events_dyn.rpy` | **128 event dinamis** (autogenerated) |
| `kk_data_kk_endings.rpy` | **220 ending** (autogenerated dari katalog) |
| `screens.rpy` | UI (kanvas logis 1920×1080 — punya Cleopatra) + layar navigasi dunia baru |
| `script.rpy` | titik masuk |

Data event/ending di-generate ulang dari dokumen desain lewat `gen_rpy.mjs` (di scratchpad sesi). Edit dokumen → regenerate → data Ren'Py ikut update.

## Cara menambah konten (data-entry, bukan engineering)
- **Wire lokasi event baru**: tambah baris di `KK_MILESTONE_MAP` (`kk_world.rpy`): `("Mi07", 7, "d3", "Apartemen Yutaka", "miyuki")` — (evid, bulan, distrik, lokasi, pemicu: `"enter"` atau id karakter). Pastikan karakternya ada di `KK_FREQ` lokasi itu (atau biarkan — pemicu "talk" otomatis memunculkannya saat tertunda).
- **Wire efek event**: tambah baris di `KK_HOOKS` (`kk_data_routes.rpy`), mis. `_hook("Mi07-B", lambda: (kk_rel("miyuki","trust",-4), kk_adj("omiai_takeru",10)))`.
- **Gate rute**: pakai `kk_stage("miyuki", 4)` saat event gerbang + cek ambang poin.
- **Ending**: resolver `kk_resolve_ending()` di `kk_engine.rpy` — tambah cabang kondisi. Semua 220 ending sudah jadi data; tinggal sambungkan syaratnya.
- **Aktivitas/kehadiran/ambience**: tabel `KK_ACTS` + `KK_ACT_BY_LOC`, `KK_FREQ`, `KK_LOC_AMBIENCE` di `kk_world.rpy` — semua data-entry.

## Belum dikerjakan (jujur, bukan disembunyikan)
- Sprite karakter/ekspresi (placeholder warna-field + watermark nama). Latar lokasi juga placeholder (SVG kampus buatan Cleopatra untuk D1; color-field untuk distrik lain).
- Dialog berkarakter: obrolan generik masih satu baris placeholder + menu nada. Isi naratif menyusul.
- `KK_FREQ` (kehadiran NPC) & `KK_ACTS` (aktivitas) + angka biaya/efek = **subset masuk akal + 🟡 usulan**, bukan simulasi penuh 8 karakter × 7 distrik × 6 slot. Mudah diperluas via tabel.
- Hub perjalanan multi-hari (onsen, vila, gasshuku) sebagai mode terpisah dari navigasi harian.
- Baru 4 event ter-wire ke lokasi+waktu (`KK_MILESTONE_MAP`). 186 sisanya ada & bisa dimainkan lewat Alat Uji, belum dipetakan ke dunia.

## Catatan Force (konsisten dgn desain)
Node Force/manipulasi = **flag + skip ke aftermath**. Tidak ada metode/adegan di kode, sama seperti `docs/Alur_Cabang/09 §2`. Jangan menuliskan cara; cukup set konsekuensi.
