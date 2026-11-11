# Event Yutaka (Y01–Y19) — host Male Route

Semua 🟡 usulan. Ini event saat **pemain memerankan Yutaka**. Saat Yutaka NPC (Female Route), perannya lewat event Chiasa (C##) dan event heroine.
ID mengacu ke `docs/Milestone_3_Tahun.md`.

**Arc:** Pemain terbangun di tubuh orang lain, belajar hidup sebagai Yutaka, dan memilih apakah ia mengejar Koita (BL), Chiasa, atau heroine. Orang terdekat mulai curiga karena kebiasaan berubah (✅).
**Variabel:** `yutaka_ingatan_hilang`, `curiga_nagisa`, `curiga_koita`, `curiga_daisuke`, `ekonomi_saldo` (¥500.000 awal ✅), `hubungan_keluarga_kisaragi`.

---

**Y01 · M01a · Terbangun di Apartemen Mewah**
- *Pemicu:* pagi 7 April; prolog.
- *Cabang:* (A) periksa dompet dan ponsel; (B) periksa cermin; (C) langsung hubungi Koita; (D) menunggu notifikasi Sistem.
- *Efek:* membentuk `kesan_awal`; A memberi tahu saldo.

**Y02 · M01a · Kunci yang Tidak Ada**
- *Pemicu:* kunjungan pertama ke rumah Amamiya.
- *Cabang:* (A) bunyikan bel dan sopan; (B) masuk seolah rumah sendiri (salah); (C) mengabari dulu.
- *Efek:* B memicu curiga Chiasa/Koita (Yutaka asli tidak punya kunci cadangan ✅).

**Y03 · M01a · Yuu-kun?**
- *Pemicu:* Nagisa memanggil dengan julukan masa kecil.
- *Cabang:* (A) jawab natural; (B) salah panggil; (C) pura-pura lupa.
- *Efek:* `curiga_nagisa` naik/turun.

**Y04 · M04 · Kuliah Ekonomi: Ingatan yang Hilang**
- *Pemicu:* kuis dadakan.
- *Cabang:* (A) belajar semalaman; (B) menyontek; (C) jujur ke dosen; (D) minta bantuan Daichi.
- *Efek:* IPK; B berisiko skorsing akademik (✅).

**Y05 · M05a · Turnamen Game: Skill yang Hilang**
- *Pemicu:* Nagisa menantang main game; Yutaka asli pro, pemain tidak.
- *Cabang:* (A) pura-pura mengalah; (B) kalah terang-terangan; (C) latihan dulu.
- *Efek:* B memicu curiga ("Yutaka tidak pernah kalah").

**Y06 · M08 · Daichi Membocorkan**
- *Pemicu:* Daichi tahu sesuatu tentang Shiori/Moeka dan menawarkannya.
- *Cabang:* (A) bayar dengan makanan; (B) tolak; (C) tawar informasi lain.
- *Efek:* intel; C membuat Daichi mulai mengorek rahasia pemain.

**Y07 · M09 · Natal: Apartemen Sepi**
- *Pemicu:* Natal; orang tua Kisaragi tidak menelepon.
- *Cabang:* (A) pergi ke rumah Amamiya; (B) mengundang heroine; (C) sendiri; (D) mengejar Koita (BL).
- *Efek:* hub besar #3 untuk host.

**Y08 · M11 · Coklat dari Siapa**
- *Pemicu:* Valentine; Yutaka menerima coklat dari banyak orang.
- *Cabang:* (A) balas satu orang; (B) balas semua sama; (C) tolak semua; (D) memberi coklat pada Koita (BL).
- *Efek:* menyalakan rantai BL atau rantai heroine.

**Y09 · M13 · Telepon Orang Tua Kisaragi**
- *Pemicu:* ayah menanyakan rencana setelah lulus.
- *Cabang:* (A) jawab sopan; (B) bantah; (C) menyebut Saionji.
- *Efek:* `hubungan_keluarga_kisaragi`; C memberi tekanan ekstra.

**Y10 · M16 · Jam Tangan Hadiah**
- *Pemicu:* Yutaka menerima jam tangan dari Daisuke seperti tahun lalu.
- *Cabang:* (A) simpan; (B) pakai; (C) kembalikan.
- *Efek:* Daisuke menilai sikap.

**Y11 · M17a · Yukata dan Chiasa**
- *Pemicu:* festival; Chiasa memakai yukata.
- *Cabang:* (A) pujian; (B) gunakan godaan Yutaka asli; (C) diam.
- *Efek:* Chiasa menilai apakah "Yutaka" masih Yutaka.

**Y12 · M20 · Pameran Chiasa**
- *Pemicu:* pameran seni; Haruka mengenalkan Chiasa.
- *Cabang:* (A) belikan karya; (B) hadir saja; (C) kritik.
- *Efek:* Chiasa membuka diri atau menjauh.

**Y13 · M21 · Daisuke dan Yoshie Pulang**
- *Pemicu:* Natal kedua; orang tua Amamiya pulang mendadak.
- *Cabang:* (A) makan malam bersama; (B) menghindar; (C) membuka pembicaraan serius.
- *Efek:* menjadi gerbang Koita Success jika Chiasa NPC bersama Koita; atau menyetujui pemain.

**Y14 · M23 · Hari Bentrok: Pernyataan Yutaka**
- *Pemicu:* hari pengakuan.
- *Cabang:* (A) mengaku pada Chiasa; (B) mengaku pada Koita (BL); (C) mengaku pada heroine; (D) tidak mengaku.
- *Efek:* hub besar #8.

**Y15 · M26 · Jarak dari Rumah**
- *Pemicu:* perjalanan; Yutaka merasa jauh dari keluarga Kisaragi.
- *Cabang:* (A) bicara dengan Daisuke; (B) menelepon ibu; (C) diam.
- *Efek:* ending Yutaka.

**Y16 · M29a · Kembang Api dan Chiasa**
- *Cabang:* (A) mengaku; (B) bergandengan; (C) menjaga jarak.
- *Efek:* Chiasa × Yutaka (NPC) berjalan.

**Y17 · M31 · Pilihan Karier**
- *Cabang:* (A) perusahaan keluarga; (B) kerja di luar; (C) magang luar negeri.
- *Efek:* keluarga Kisaragi bereaksi.

**Y18 · M32 · Pameran Tunggal Chiasa**
- *Cabang:* (A) hadir; (B) absen; (C) membawa seseorang.
- *Efek:* hubungan Yutaka–Chiasa.

**Y19 · M35 · Jawaban**
- *Cabang:* ditentukan flag BL, Chiasa, atau heroine.
- *Efek:* ending Yutaka (lihat Kisaragi_Yutaka.md bagian 11).

---

## Catatan
- **Evaluasi Sistem:** Yutaka × Chiasa dihitung deviasi Sedang (Chiasa heroine tambahan Koita ✅). Bukan nol.
- **Force Route:** tersedia pada hub berisiko tinggi; konsekuensi di `docs/Aturan_Evaluasi_dan_Force_Route.md`.
