# Review Ciri Tulisan AI — Event Dinamis (128) & Ending (220)

Lanjutan dari `Review_Ciri_AI_M01-M20.md` (yang mencakup 110 event utama). Dokumen ini mencakup SELURUH katalog event dinamis (128/128, semuanya sudah ditulis lengkap, tidak terikat progres bulan) dan SELURUH ending (220/220, juga lengkap). Semua referensi file/label di bawah sudah diverifikasi langsung ke source per 2026-11-24.

## Event Dinamis (128)

### Pola Lintas-Rute

**1. Kalimat penutup "tesis/kesimpulan" — JAUH lebih konsisten daripada event utama**
Di event utama tic ini sudah jadi masalah utama (terutama rute Yutaka). Di event dinamis, tic yang sama justru makin seragam, nyaris 100% di beberapa rute:
- **Cross-Route (X-D01-12)**: nyaris tanpa kecuali di SEMUA 12 adegan — `kk_cross_dyn.rpy:27,43,82,160,179,251,253,255,271,273,275,290,292,294`.
- **Yutaka (Y-D01-11)**: nyaris tiap cabang di `kk_yutaka_dyn.rpy`, sering berpola "bukan X, melainkan Y" (Y-D11-A `:240`).
- **Harumi (H-D02-12)**: sama tic, contoh H-D10-B `kk_harumi_dyn.rpy:209`.
- **Moeka (Mo-D01-13)**: hampir tiap penutup adegan, paling jelas di Mo-D12 (`kk_moeka_dyn.rpy:349-351`, gaya PSA).
- **Shiori (S-D01-17)**: dominan di hampir semua, bernada abstrak-filosofis (`kk_shiori_dyn2.rpy:37,63,103,173,184`).
- **Pengecualian bagus**: Nagisa (nol kemunculan), Chiasa (nyaris nol — hanya template ringan di C-D12), Koita (nyaris nol, semua 21 adegan berakhir di gambar/aksi ambigu), Miyuki (cuma 2 dari 14: Mi-D09, Mi-D11).

**2. Reskin cabang Host — tidak merata, ada contoh bagus DAN buruk dalam karakter yang sama**
- Harumi (H-D02, H-D04): sama persis seperti masalah di event utamanya — kalimat identik, cuma nama/sapaan beda.
- Shiori: `kk_shiori_dyn2.rpy` (S-D01,05,06) mengulang pola reskin; TAPI `kk_shiori_dyn.rpy` (S-D03,07,13-17) sama sekali TIDAK ada percabangan host — lebih sehat dari event utamanya.
- Moeka: ringan, nama panggilan ("Chimian"/"Yutayuta") memberi sedikit tekstur ekstra dibanding reskin event utama yang lebih parah.
- Miyuki: ringan, cuma 2 instance (Mi-D02, Mi-D04).
- **Koita (K-D01)**: justru CONTOH BAGUS — cabang Chiasa/Yutaka pakai register benar-benar beda (kehangatan "Chi-chan" vs kecasualan teman), bukan tempel nama.

**3. Tic deskriptor per karakter dari event utama SEBAGIAN TIDAK terbawa ke dinamis**
- Miyuki: "mata cokelat kemerahan" dan "berkedip lalu tersenyum" — **nol** kemunculan di 14 event dinamisnya. Kabar baik, tic ini terisolasi di file event utama saja.
- Chiasa: tic "serta [list sensorik]" juga nyaris nol di event dinamis.
- Shiori: "mata ungu ametis" **tetap terbawa** — `kk_shiori_dyn2.rpy:90,117`.

**4. Tidak ada adegan tipis di SELURUH 128 event dinamis.** Semua batch (Chiasa, Koita, Yutaka, Harumi, Moeka, Shiori, Nagisa, Miyuki, Cross-Route) mengonfirmasi tidak ada yang serushed/sethin Y12. Event dinamis tidak perlu masuk daftar "perpanjang adegan".

### Catatan struktural (bukan soal gaya tulisan — buat referensi kalau menelusuri kode)
Beberapa ID event dinamis tidak pakai label `kkscene_<ID>` standar, melainkan label custom:
- Chiasa: C-D02→`kk_show_portfolio`, C-D03→`kk_draw_at_home`, C-D07→`kk_mio_deadline` (semua di `kk_art.rpy`)
- Nagisa: N-D01→`kk_phone_rematch`, N-D02→dispatch generik, N-D09→`kk_torn_koko` (di `kk_life_events.rpy`/`kk_family.rpy`)
- Miyuki (separuh dari 14!): Mi-D01→`kk_pudding`, Mi-D02→`kk_library_rest`, Mi-D04→`kk_overheard_call`, Mi-D09→`kk_pediatric_patient`, Mi-D11→`kk_exam_eve`, Mi-D03/Mi-D12→label lain di dispatcher yang sama (`kk_life_events.rpy:1180-1245`, `kk_miyuki_daily.rpy`)
- Yutaka: Y-D03, Y-D08 → `kk_family.rpy`
- Harumi: H-D01, H-D05, H-D07 → belum terlacak pasti di audit ini (tidak ditemukan lewat grep sederhana) — cek manual dulu kalau mau direvisi.

## Ending (220)

### Pola Lintas-Rute — berlaku ke SEMUA 220 ending tanpa kecuali
Ini temuan paling sistemik di seluruh audit (event utama + dinamis + ending digabung): **struktur 3-paragraf yang kaku dan nyaris identik di semua 220 entry**, dikonfirmasi oleh keempat agen audit ending tanpa pengecualian:
- Paragraf 1 — adegan/gambar pembuka konkret (kualitasnya bagus, spesifik per karakter, TIDAK perlu diubah).
- Paragraf 2 — kualifier yang menegasikan ("tidak otomatis menghapus/mengubah...").
- Paragraf 3 — kalimat tesis/aforisme penutup yang **menyatakan makna secara eksplisit**, bukan berhenti di gambar/aksi.

Rumus penutup paragraf 3 bervariasi sedikit per kelompok tapi tetap templat:
- **Force & Kriminal (15/15), Shiori (~14/16), sebagian Moeka/Yutaka**: "X tidak/bukan Y" — menyangkal pembacaan "penebusan/pengampunan" (`E-FO-01,03,08,12,13,14`; `E-SH-04,11`; `E-MO-09,11`; `E-YU-04`).
- **Sistem & Evaluasi (25), NPC Sampingan (27)**: "...tanpa harus/lebih dulu [beban yang dihindari]" (`E-SI-01,12`; `E-HP-07`; `E-NPC-06,21,26,07,18,22,25`) — bahkan dipakai seragam di ending personal (E-HP) maupun ending sistem (E-SI) walau registernya beda.
- **Koita (29) & Chiasa (24)**: pola 2-slot — P2 "tidak otomatis menghapus..." + P3 aforisme umum (`E-KO-01,09,14`; `E-BL-02,08`; `E-CH-04,07`; `E-CF-08,10,13`) — tic paling konsisten (25+ dari 29 entry Koita).
- **Miyuki, Nagisa, Harumi, Interlock (56 total)**: versi paling ringan, cuma ~separuh entry (`E-MI-01`; `E-NA-04`; `E-HA-05`; `E-X-14`) — **batch ending paling bersih di seluruh audit**.

### Yang TIDAK jadi masalah di ending (beda dengan event)
- **Tidak ada pengulangan frasa/deskriptor persis** antar ending — detail dan karakterisasi tetap spesifik dan grounded per tokoh (beda dengan event, yang punya tic deskriptor berulang seperti "mata cokelat kemerahan").
- Tic "serta [list sensorik]" khusus Chiasa **tidak terbawa** ke endingnya — dikonfirmasi bersih.
- Tidak ada ending yang kependekan/tipis.
- Rule-of-three dipaksakan cuma muncul sesekali (~4-5 dari 220), bukan pola dominan.

## Prioritas Revisi (gabungan dinamis + ending)

1. **[Dampak terbesar di seluruh audit]** Ending: ganti rumus paragraf penutup (P3 "tesis/disclaimer") supaya berhenti di gambar/aksi konkret, bukan menyatakan makna eksplisit. Ini SATU tic yang muncul di hampir SEMUA 220 ending — kalau Antigravity bikin satu pass khusus "potong/ganti kalimat terakhir tiap ending", dampaknya lebih besar daripada revisi manapun di event utama/dinamis.
2. Event dinamis: kalimat penutup tesis di Yutaka, Harumi, Moeka, Shiori, Cross-Route X — treatment sama seperti perbaikan di event utama (ganti dengan beat aksi/gestur).
3. Reskin cabang host: Harumi (H-D02/04) dan Shiori `kk_shiori_dyn2.rpy` — sama seperti event utama, tulis ulang salah satu cabang dengan interioritas berbeda.
4. *(Prioritas rendah, bukan soal gaya)* Kalau nanti mau ada refactor penamaan label, catatan struktural di atas (ID yang pakai label custom, terutama separuh event dinamis Miyuki) bisa jadi acuan — tapi ini housekeeping, bukan kebutuhan revisi prosa.

## Tidak Perlu Disentuh

- Event dinamis Nagisa — bersih total, tidak ada temuan sama sekali.
- Event dinamis Chiasa & Koita — jauh lebih bersih dari event utama keduanya, cuma 1 catatan ringan (template beat C-D12).
- Event dinamis Miyuki — tic terburuk dari event utamanya (deskriptor fisik, gerakan baku) tidak terbawa ke sini.
- Ending grup Miyuki/Nagisa/Harumi/Interlock — batch ending paling bersih.
- Semua event dinamis: tidak ada yang perlu diperpanjang (beda dengan event utama rute Yutaka).
