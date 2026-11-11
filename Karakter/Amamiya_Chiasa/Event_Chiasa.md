# Event Chiasa (C01–C18) — host Female Route

Semua 🟡 usulan. Ini event saat **pemain memerankan Chiasa**. Saat Chiasa NPC (Male Route), perannya lewat event heroine dan event Yutaka.
ID mengacu ke `docs/Milestone_3_Tahun.md`.

**Arc:** Pemain masuk ke Chiasa yang mencintai Koita, kebanyakan yuri, dan harus menggeser takdir Koita agar tidak mati (⭐ Chiasa × Yutaka saja = tetap mati).
**Variabel:** `chiasa_rahasia_shena`, `curiga_haruka`, `curiga_mio`, `chiasa_koita_success`, `deviasi_total`, `peringatan_1`, `peringatan_final`.

---

**C01 · M01a · Terbangun di Kamar Chiasa**
- *Pemicu:* pagi 7 April; prolog.
- *Cabang:* (A) cek cermin dan buku sketsa; (B) cek ponsel; (C) turun sarapan; (D) menunggu Sistem.
- *Efek:* `kesan_awal`; A mengungkap pita dan ciri visual.

**C02 · M01a · "Ko-nii?"**
- *Pemicu:* sarapan bersama Koita.
- *Cabang:* (A) memanggil "Ko-nii" natural; (B) memanggil nama; (C) menggoda seperti Chiasa asli.
- *Efek:* B memicu curiga Koita; C menaikkan Jealousy Koita.

**C03 · M04 · Tanzaku Chiasa**
- *Pemicu:* Tanabata; Chiasa menulis tanzaku (apa pun).
- *Cabang:* (A) menulis harapan baru; (B) menyalin harapan asli; (C) tidak menulis.
- *Efek:* `harapan_pemain`; C membuat Haruka bertanya.

**C04 · M05a · "Nacchan-oneechan"**
- *Pemicu:* Nagisa di festival; Chiasa kecil biasa memanggil begitu.
- *Cabang:* (A) pakai julukan; (B) pakai nama biasa; (C) menantang Nagisa.
- *Efek:* A membangkitkan kenangan; B dingin; C memperkuat rivalitas.

**C05 · M08 · Mio Menelepon**
- *Pemicu:* editor meminta cover jilid baru.
- *Cabang:* (A) menolak halus (royalti pasif ✅); (B) menerima dan berlatih; (C) minta bantuan Haruka.
- *Efek:* `curiga_mio`; B bisa membuka kemampuan baru bertahap.

**C06 · M09 · Natal Rumah Amamiya**
- *Cabang:* (A) di rumah bersama Koita; (B) mengundang heroine; (C) pergi ke Nagisa/yuri; (D) sendirian.
- *Efek:* hub besar #3.

**C07 · M11 · Coklat untuk Banyak Orang**
- *Pemicu:* Valentine.
- *Cabang:* (A) coklat untuk Koita; (B) untuk heroine tertentu (yuri); (C) untuk Yutaka; (D) tidak memberi.
- *Efek:* gerbang jalur yuri/Koita Success/Yutaka.

**C08 · M13 · Haruka Curiga**
- *Pemicu:* gambar sketsa pemain berubah gaya.
- *Cabang:* (A) kerjakan lagi dari nol; (B) beralasan "stres"; (C) mengaku sebagian.
- *Efek:* `curiga_haruka`; risiko rahasia Shena terbongkar.

**C09 · M16 · Buku Sketsa Kosong**
- *Pemicu:* pemain tidak bisa menggambar sebaik asli.
- *Cabang:* (A) latihan keras; (B) menyewa pihak lain; (C) berhenti.
- *Efek:* royalti ¥50.000 tetap masuk (✅), tetapi tawaran proyek dari Mio bisa gagal.

**C10 · M17a · Rival di Yukata**
- *Pemicu:* Nagisa di festival kedua.
- *Cabang:* (A) damai; (B) tantang; (C) goda.
- *Efek:* kebangkitan rivalitas atau kedamaian.

**C11 · M20 · Pameran Kecil dan Shiori**
- *Pemicu:* Shiori datang ke pameran; ia pembaca Shena.
- *Cabang:* (A) mengaku; (B) pura-pura tidak tahu; (C) beri tanda tangan.
- *Efek:* jembatan ke Shiori atau perangkap (Rute Revenge jika kebohongan).

**C12 · M21 · Orang Tua Pulang**
- *Pemicu:* Daisuke dan Yoshie pulang di Natal.
- *Cabang:* (A) menyambut; (B) menghindar; (C) membuka rahasia.
- *Efek:* **gerbang Koita Success** (tahap 3).

**C13 · M23 · Hari Bentrok: Chiasa**
- *Pemicu:* hari pengakuan.
- *Cabang:* (A) mengaku pada Koita; (B) mengaku pada heroine; (C) mengaku pada Yutaka; (D) tidak mengaku.
- *Efek:* hub besar #8.

**C14 · M26 · Perjalanan Perpisahan**
- *Cabang:* (A) menghabiskan waktu dengan Koita; (B) dengan Nagisa; (C) dengan heroine lain.
- *Efek:* mempersempit jalur.

**C15 · M29a · Kembang Api dan Nagisa**
- *Cabang:* (A) mengaku; (B) bergandeng; (C) menjaga jarak.
- *Efek:* jalur yuri Nagisa.

**C16 · M31 · Cover vs Skripsi**
- *Cabang:* (A) fokus kuliah; (B) fokus proyek; (C) berhenti.
- *Efek:* karier Chiasa.

**C17 · M32 · Pameran Tunggal**
- *Cabang:* (A) hadir sendiri; (B) mengundang seseorang; (C) membatalkan.
- *Efek:* publik melihat siapa dekat dengan siapa.

**C18 · M35 · Pilihan Chiasa**
- *Cabang:* ditentukan oleh deviasi total dan hubungan.
- *Efek:* lolos atau gagal evaluasi; ending Chiasa (Koita Success / Yutaka / Yuri / mandiri).

---

## Peringatan Sistem ⭐ (Chiasa × Yutaka saja = mati)
- **Peringatan 1 (M24):** bila `deviasi_total` masih nol. "Ini bukan penyimpangan. Ini pelarian."
- **Peringatan Final (M33):** tiga bulan sebelum wisuda.
- **Jalur aman:** yuri ke heroine utama; Koita Success **plus** deviasi heroine; merebut heroine lewat cara lain.

## Perbedaan penting
- Kemampuan menggambar tidak diwarisi (✅). Rahasia Shena menjadi sumber ketegangan.
- Chiasa dominan secara canon; arah lembut/tunduk dipilih pemain.
- Force Route tersedia pada hub berisiko tinggi; konsekuensi di `docs/Aturan_Evaluasi_dan_Force_Route.md`.
