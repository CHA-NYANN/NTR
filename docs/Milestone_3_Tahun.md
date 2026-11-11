# Milestone 3 Tahun — tulang punggung cerita utama

Status: kerangka 🟡 (usulanku). Dasar canon: GDD 6N (3 tahun sampai kelulusan, chapter naratif berjalan bersama kalender, timeskip, milestone utama dengan perkembangan dinamis di antaranya), 6H (event manga asli mostly tetap berjalan sampai penyimpangan besar, plot armor Koita, event bisa terlewat permanen), dan 6B/6K (rute distorsi, Force Route).

Kekuatan game ini adalah **banyaknya rute dan cabang**, jadi dokumen ini memetakan: kapan hub cabang terbuka, apa yang menggerbang rute, dan di mana jendela intervensi terakhir. Diagram alur cabang per rute, interlock, dan semua ending ada di [Alur_Cabang/](Alur_Cabang/README.md).

---

## 0. Cara membaca

**Event utama (M##)** = milestone cerita bulanan. Satu bulan satu milestone, kadang dua (a, b).
**Event karakter (K/Y/C/Mi/N/H/Mo/S + nomor)** = event khusus tiap karakter, lengkap di `Karakter/<nama>/Event_<nama>.md`.
**Hub** = titik cabang besar yang mengubah rute. **Gerbang** = hub yang membuka atau menutup satu rute.
**Dasar manga** = apa yang terjadi di manga asli bila pemain tidak ada (🟡 karena canon hanya menyebut arah umum). Event ini "mostly tetap berjalan" sampai ada penyimpangan besar (✅).
Penanda: ✅ canon, 🟡 usulan, ⭐ keputusanmu.

## 1. Bingkai waktu 🟡
- **Tahun 1 (M01–M12):** Senin 7 April sampai akhir Maret. Tema: **Kontrak**.
- **Tahun 2 (M13–M24):** April–Maret berikutnya. Tema: **Retak**.
- **Tahun 3 (M25–M36):** April–Maret terakhir, berakhir pada **Wisuda Koita**. Tema: **Tagihan**.
- **Semester:** Musim Semi (Apr–Jul, ujian akhir Juli), Libur Musim Panas (Agu–Sep), Musim Gugur (Okt–Jan, ujian akhir Januari), Libur Musim Semi (Feb–Mar). Festival Musim Dingin awal Februari.
- **Hari:** 24 jam (✅). Slot waktu 🟡: Pagi 06–10, Siang 10–14, Sore 14–18, Malam 18–22, Larut 22–02, Dini Hari 02–06. Tiap interaksi memakai 1 slot atau lebih, plus Action Point (✅ kombinasi AP dan waktu). Tidur tidak wajib ⭐; lihat [Sistem_Waktu_Bebas_dan_Kondisi_Fisik.md](Sistem_Waktu_Bebas_dan_Kondisi_Fisik.md).
- **Timeskip (✅):** boleh melompati minggu tanpa event bila tidak ada quest aktif. Jadwal NPC tetap disimulasikan, jadi event latar tetap terjadi.

### Peta bulan
| M | Bulan | Tema utama |
|---|---|---|
| 01 | Apr T1 | Hari Pertama + Hanami |
| 02 | Mei | Golden Week: Penginapan Onsen |
| 03 | Jun | Tsuyu: Hujan Bersama |
| 04 | Jul | Tanabata + Ujian Semester 1 |
| 05 | Agu | Natsu Matsuri + Gasshuku Vila Pantai |
| 06 | Sep | Tsukimi + Reuni Kelompok Belajar |
| 07 | Okt | Semester Baru: Pesaing Muncul |
| 08 | Nov | Momiji + Festival Klub |
| 09 | Des | Malam Natal |
| 10 | Jan | Hatsumode + Ujian Semester 2 |
| 11 | Feb | Festival Musim Dingin + Valentine |
| 12 | Mar | White Day + Audit Tahun 1 |
| 13 | Apr T2 | Adik Tingkat Baru |
| 14 | Mei | Golden Week: Pulang ke Kansai |
| 15 | Jun | Tsuyu: Hujan Deras |
| 16 | Jul | Tanabata Kedua + Ujian |
| 17 | Agu | Natsu Matsuri Kedua + Liburan Besar |
| 18 | Sep | Tsukimi: Sidang Rumor |
| 19 | Okt | Semester Kritis: Koita Menyadari |
| 20 | Nov | Festival Seni dan Pameran |
| 21 | Des | Natal Kedua |
| 22 | Jan | Hatsumode Kedua + Ujian |
| 23 | Feb | Festival Musim Dingin Kedua: Pengakuan Bentrok |
| 24 | Mar | White Day + Audit Tahun 2 |
| 25 | Apr T3 | Tahun Terakhir: Skripsi dan Shukatsu |
| 26 | Mei | Golden Week: Perjalanan Perpisahan Dini |
| 27 | Jun | Tsuyu Terakhir |
| 28 | Jul | Tanabata Ketiga + Ujian |
| 29 | Agu | Natsu Matsuri Ketiga + Gasshuku Terakhir |
| 30 | Sep | Tsukimi: Pengumuman Hasil |
| 31 | Okt | Pilihan Karier |
| 32 | Nov | Festival Akhir + Pameran Tunggal |
| 33 | Des | Natal Terakhir + Peringatan Final Sistem |
| 34 | Jan | Malam Tanpa Balasan + Ujian Akhir |
| 35 | Feb | Festival Musim Dingin Terakhir |
| 36 | Mar | White Day, Wisuda, Evaluasi |

---

## 2. Event utama per bulan 🟡

Format tiap entri: **Dasar manga** (apa yang terjadi tanpa pemain) · **Hub cabang** · **Event karakter terkait** · **Efek besar** · **Quest Sistem** · **Risiko**.
Event karakter diacu dengan ID (misal N04). Semuanya didefinisikan di file Event masing-masing.

---

### TAHUN 1 — KONTRAK

#### M01 · April T1 · Hari Pertama + Hanami
**M01a — Hari Pertama (Senin 7 April).**
- **Dasar manga:** hari pertama semester; Koita dikelilingi heroine di kantin.
- **Hub:** (1) *Kesan awal* — ramah / dingin / genit / agresif / manipulatif (flag `kesan_awal`); (2) menerima atau menolak mengikuti "naskah" manga yang diketahui pemain; (3) siapa yang pertama dihubungi.
- **Prolog berbeda (✅):** Male Route di apartemen mewah Yutaka; Female Route di kamar Chiasa di rumah Amamiya, sarapan bersama Koita.
- **Event karakter:** Y01–Y03 / C01–C02, K01, N01.
- **Efek besar:** Sistem NTR muncul dan kontrak aktif. Possession slips mulai dihitung (orang dekat mulai curiga).
- **Quest Sistem:** Q01 *Kenali Takdir* — temui tiga heroine dalam 7 hari. Tidak bisa ditolak (✅).
- **Risiko:** salah memanggil panggilan masa kecil memicu curiga Nagisa dan Koita.

**M01b — Hanami Kampus (Sabtu–Minggu, minggu ke-2).**
- **Dasar manga:** piknik di bawah sakura; Miyuki membawa bento, Moeka membawa kamera, Shiori lewat membawa papan shogi.
- **Hub:** tempat duduk; siapa yang dibantu; siapa yang diajak pulang bersama.
- **Event karakter:** Mi01, Mo01, S01, H01.
- **Efek besar:** pertama kali pemain melihat semua heroine dalam satu lokasi. Menentukan siapa yang mengenali pemain sebagai "orang baru".
- **Quest Sistem:** Q02 *Duduk di Sebelah Target*.
- **Risiko:** rendah.

#### M02 · Mei T1 · Golden Week: Penginapan Onsen (3–6 Mei)
- **Dasar manga:** Moeka memenangkan undian penginapan onsen; rombongan Koita berangkat; kamar tertukar karena kebetulan (plot armor); Koita berada satu ruang dengan dua heroine.
- **Hub:** (1) ikut atau tidak; (2) pembagian kamar; (3) malam di ryokan; (4) siapa yang menemani Koita di taman luar.
- **Event karakter:** K02, Mi02, N02, Mo02, S02.
- **Efek besar:** kesempatan pertama menggeser takdir. Hub risiko tinggi: ruang tertutup, malam hari, minuman.
- **Quest Sistem:** Q03 *Kamar yang Salah* — jangan biarkan Koita menang di plot armor.
- **Risiko:** sedang–tinggi untuk Force Route dan rumor.

#### M03 · Juni T1 · Tsuyu: Hujan Bersama
- **Dasar manga:** Koita dan Shiori berbagi payung di perpustakaan (awal ketertarikan Shiori); Moeka lupa janji; Harumi menyeduh teh di bawah atap.
- **Hub:** menawarkan payung kedua; mengantar siapa pulang; menepati atau melanggar janji pada Moeka.
- **Event karakter:** S03, Mo03, H02, N03.
- **Efek besar:** hujan = kesempatan "Moment" bagi pemain mengganti Koita. Moeka mulai terbiasa mengandalkan pemain bila dibantu.
- **Quest Sistem:** Q04 *Payung Kedua*.
- **Risiko:** rendah.

#### M04 · Juli T1 · Tanabata + Ujian Semester 1
- **Dasar manga:** 7 Juli, tanzaku harapan tiap orang digantung di aula; ujian akhir.
- **Hub:** (1) membaca tanzaku orang lain (intel) vs menulis harapan sendiri; (2) belajar vs bekerja; (3) membantu kelompok belajar.
- **Event karakter:** K03, Mi03, H03, Y04/C03.
- **Efek besar:** gerbang akademik pertama (IPK) — memengaruhi beasiswa Moeka, peringkat Harumi, peringkat Shiori. `harapan_pemain` mengubah nada Sistem.
- **Quest Sistem:** Q05 *Baca Harapan* (tanpa ketahuan).
- **Risiko:** rendah.

#### M05 · Agustus T1 · Natsu Matsuri + Gasshuku Vila Pantai
**M05a — Natsu Matsuri & Hanabi (≈ 9 Agustus malam).**
- **Dasar manga:** yukata; Koita dan Nagisa serta Chiasa di festival kenangan; kembang api; Nagisa gagal mengaku.
- **Hub besar #1:** siapa pemain ajak; menyela pengakuan; kembang api bersama siapa.
- **Event karakter:** N04, C04/Y05, K04, Mi04.
- **Efek besar:** pengakuan pertama bisa terjadi di sini. Boneka Koko dan foto berempat jadi simbol.
- **Quest Sistem:** Q06 *Hanabi Pertama* — tutup satu jalan Koita.
- **Risiko:** rendah.

**M05b — Gasshuku Vila Pantai (24–27 Agustus).**
- **Dasar manga:** 3H2M kelompok di vila; BBQ; permainan; kebetulan kamar; satu malam penuh.
- **Hub besar #2:** acara malam; ruang pribadi; siapa pergi sendiri.
- **Event karakter:** Mi05, Mo04, H04, S04, K05.
- **Efek besar:** hub paling berisiko tahun 1. Pembagian rahasia, alkohol, dan ruang tertutup.
- **Quest Sistem:** Q07 *Malam Terpanjang*.
- **Risiko:** tinggi (Force Route, rumor, bukti digital).

#### M06 · September T1 · Tsukimi + Reuni Kelompok Belajar
- **Dasar manga:** reuni di rumah teh Harumi; Koita meminta foto bersama; masing-masing bicara tentang masa depan.
- **Hub:** menanggapi pembicaraan masa depan; bercerita soal rencana; menggali rencana orang lain.
- **Event karakter:** H05, Mi06, N05, Mo05, K06.
- **Efek besar:** gerbang pengecekan #1 untuk semua rute distorsi (cek benih: kelelahan, kecemburuan, isolasi, tekanan keuangan).
- **Quest Sistem:** Q08 *Rencana Orang Lain*.
- **Risiko:** rendah.

#### M07 · Oktober T1 · Semester Baru: Pesaing Muncul
- **Dasar manga:** klub baru; pesaing baru muncul untuk heroine.
- **Hub:** menolong, menghalangi, atau mengabaikan pesaing.
- **Pengenalan:** Hayase Takeru (Miyuki), Tojo Akihiro (Shiori), Mochizuki Yuuto (Nagisa), Ogawa Masato (Harumi), Kuga Renji (Moeka).
- **Event karakter:** Mi07, Mo06, H06, S05, N06.
- **Efek besar:** gerbang awal untuk Harumi (Ogawa) dan Moeka (Kuga). Tekanan sosial bagi semua.
- **Quest Sistem:** Q09 *Pesaing Baru*.
- **Risiko:** sedang.

#### M08 · November T1 · Momiji + Festival Klub
- **Dasar manga:** bazar klub sastra; peragaan Moeka; pameran seni Chiasa; Sena memperkenalkan psikolog kampus.
- **Hub:** jadi panitia (via Fujisawa Ayane); membantu satu klub lebih banyak; hadir di acara siapa.
- **Event karakter:** K07, Mo07, S06, C05/Y06, Mi08.
- **Efek besar:** memperlihatkan Sato Kyoko sebagai jalur bantuan. Kurosawa Mei mulai merekam.
- **Quest Sistem:** Q10 *Acara Bersama*.
- **Risiko:** rendah.

#### M09 · Desember T1 · Malam Natal (24 Desember)
- **Dasar manga:** plot armor mempertemukan Koita dengan heroine yang paling siap; kencan Natal.
- **Hub besar #3:** pemain bisa menyela, mengambil alih, atau mengajak orang lain; opsi "Natal rahasia".
- **Event karakter:** N07, Mi09, Mo08, K08, C06/Y07, H07, S07.
- **Efek besar:** siapa yang bersama siapa saat Natal menentukan arah Tahun 2. Bisa memicu hubungan rahasia dan rumor.
- **Quest Sistem:** Q11 *Natal Bukan Milik Protagonis*.
- **Risiko:** sedang.

#### M10 · Januari T1 · Hatsumode + Ujian Semester 2
- **Dasar manga:** doa tahun baru; omikuji; ujian akhir.
- **Hub:** omikuji (petunjuk samar), siapa diundang ke kuil, belajar bersama.
- **Event karakter:** H08, Mo09, K09, Mi10.
- **Efek besar:** gerbang akademik kedua. Beasiswa Moeka mulai terancam bila IPK turun.
- **Quest Sistem:** Q12 *Doa yang Terkabul*.
- **Risiko:** rendah.

#### M11 · Februari T1 · Festival Musim Dingin + Valentine
- **Dasar manga:** peringatan setahun Koita dan Shiori; Shiori mulai mencintai Koita; Valentine coklat dari para heroine.
- **Hub besar #4:** coklat siapa yang diterima, siapa memberi pemain coklat, pengakuan, ujian rasa.
- **Event karakter:** S08, N08, Mi11, Mo10, C07/Y08, K10.
- **Efek besar:** gerbang awal Koita Success dan rute yuri/BL. Banyak pengakuan dipicu.
- **Quest Sistem:** Q13 *Coklat dan Konsekuensi*.
- **Risiko:** sedang.

#### M12 · Maret T1 · White Day + Audit Tahun 1
- **Dasar manga:** balasan White Day; musim libur.
- **Hub:** hadiah balasan; menutup tahun dengan siapa.
- **Event karakter:** K11, S09, N09.
- **Efek besar:** **Audit Tahun 1** — Sistem memberi ringkasan samar (✅ evaluasi utama hanya sekali, jadi ini bukan evaluasi; hanya "kesan"). Rangkum tren hubungan.
- **Quest Sistem:** Q14 *Audit Awal*.
- **Risiko:** rendah.

---

### TAHUN 2 — RETAK

#### M13 · April T2 · Adik Tingkat Baru
- **Dasar manga:** mahasiswa baru masuk; Chiasa naik ke tahun kedua; Miyuki tahun keempat (klinik).
- **Hub:** menyambut mahasiswa baru; Haruka dan lingkaran seni; rumor baru.
- **Event karakter:** Mi12, N10, H09, C08/Y09.
- **Efek besar:** rute distorsi mulai terlihat. Teman dan keluarga mulai menyadari.
- **Quest Sistem:** Q15 *Wajah Baru, Aturan Baru*.
- **Risiko:** sedang.

#### M14 · Mei T2 · Golden Week: Pulang ke Kansai
- **Dasar manga:** rombongan kecil ikut Harumi pulang menemui orang tuanya; bertemu Prof. Mizuhara.
- **Hub:** ikut atau tidak; apa yang diceritakan; menjaga atau membuka rahasia Harumi.
- **Event karakter:** H10, Mi13, K12, N11.
- **Efek besar:** mengungkap latar keluarga Harumi (Kujo). Orang tua Kujo bisa menjadi sekutu atau tekanan.
- **Quest Sistem:** Q16 *Wali yang Tidak Tahu*.
- **Risiko:** rendah.

#### M15 · Juni T2 · Tsuyu: Hujan Deras
- **Dasar manga:** hujan deras menyebabkan banjir kecil; Koita menyelamatkan satu heroine.
- **Hub:** siapa diselamatkan; apakah pemain mengambil alih peran.
- **Event karakter:** Mo11, S10, Mi14, N12.
- **Efek besar:** **jendela intervensi Moeka #1** (stres pertama memuncak). Gerbang Nagisa Yandere mulai terbuka.
- **Quest Sistem:** Q17 *Banjir*.
- **Risiko:** sedang.

#### M16 · Juli T2 · Tanabata Kedua + Ujian
- **Dasar manga:** tanzaku kedua; ujian.
- **Hub:** harapan berubah: orang menulis hal berbeda dari tahun lalu.
- **Event karakter:** H11, S11, Mo12, C09/Y10.
- **Efek besar:** IPK menentukan beasiswa Moeka, peringkat Harumi, dan jalur karier Miyuki.
- **Quest Sistem:** Q18 *Harapan yang Berubah*.
- **Risiko:** rendah.

#### M17 · Agustus T2 · Natsu Matsuri Kedua + Liburan Besar
**M17a — Natsu Matsuri Kedua.**
- **Dasar manga:** festival kedua; Koita memilih satu heroine untuk ditemani.
- **Hub besar #5:** konfrontasi antar heroine; pemain memihak.
- **Event karakter:** N13, C10/Y11, K13, Mi15.
**M17b — Liburan Besar (pulau).**
- **Dasar manga:** liburan pulau 4 hari; vila; kebetulan.
- **Hub besar #6:** tinggi risiko; semua rute bertemu.
- **Efek besar:** **kebocoran Sistem** — Sistem memberi informasi usang sekali (pemain rugi); ia tidak minta maaf.
- **Quest Sistem:** Q19 *Pulau*.
- **Risiko:** tinggi.

#### M18 · September T2 · Tsukimi: Sidang Rumor
- **Dasar manga:** gosip tentang Koita beredar; Kurosawa Mei mengunggah.
- **Hub:** membantah, membiarkan, memanfaatkan, atau membayar Mei.
- **Event karakter:** K14, N14, S12, Mo13.
- **Efek besar:** jaringan rumor aktif penuh. Reputasi per lingkungan berubah.
- **Quest Sistem:** Q20 *Rumor Bukan Kebenaran*.
- **Risiko:** sedang–tinggi (bukti digital).

#### M19 · Oktober T2 · Semester Kritis: Koita Menyadari
- **Dasar manga:** Koita melihat heroine mulai menjauh; ia panik.
- **Hub:** menghadapi Koita; mengakui; berpura-pura; memanfaatkannya.
- **Event karakter:** K15, Mi16, Mo14, H12.
- **Efek besar:** Koita mulai melakukan manuver balik (✅ NPC mengambil keputusan mandiri). Dimulainya konfrontasi terbuka.
- **Quest Sistem:** Q21 *Protagonis Marah*.
- **Risiko:** sedang.

#### M20 · November T2 · Festival Seni dan Pameran
- **Dasar manga:** pameran seni; peragaan Moeka kedua; turnamen catur Shiori.
- **Hub:** hadir di acara siapa; membantu siapa.
- **Event karakter:** C11/Y12, Mo15, S13, Mi17, H13.
- **Efek besar:** **Surat Peringatan Beasiswa Moeka** (Nov). **Penemuan Shiori** (bila ada kebohongan terkait). **Dana lab Harumi dibekukan** (bila Ogawa aktif).
- **Quest Sistem:** Q22 *Sorotan*.
- **Risiko:** sedang.

#### M21 · Desember T2 · Natal Kedua
- **Dasar manga:** Natal; bergantung siapa yang masih bersama Koita.
- **Hub besar #7:** pilihan akhir tahun.
- **Event karakter:** N15, Mi18, H14, S14, K16, C12/Y13.
- **Efek besar:** gerbang Nagisa Yandere (ultimatum). Hubungan rahasia mulai bocor.
- **Quest Sistem:** Q23 *Malam Tak Bersahabat*.
- **Risiko:** tinggi.

#### M22 · Januari T2 · Hatsumode Kedua + Ujian
- **Hub:** harapan tahun baru; ujian akhir.
- **Event karakter:** Mo16, H15, S15.
- **Efek besar:** semester kedua yang rendah mendorong beasiswa Moeka mendekati pencabutan.
- **Quest Sistem:** Q24.
- **Risiko:** rendah.

#### M23 · Februari T2 · Festival Musim Dingin Kedua: Pengakuan Bentrok
- **Dasar manga:** beberapa heroine mengaku pada hari yang sama; Koita dipaksa memilih.
- **Hub besar #8 (puncak tahun 2):** siapa pemain dukung; mengirim Koita ke arah tertentu; bergerak sendiri.
- **Event karakter:** K17, Mi19, N16, S16, Mo17, C13/Y14, H16.
- **Efek besar:** bisa memutus lingkaran harem; Koita Success; BL; yuri; konfrontasi sosial.
- **Quest Sistem:** Q25 *Satu Hari, Banyak Pengakuan*.
- **Risiko:** tinggi.

#### M24 · Maret T2 · White Day + Audit Tahun 2
- **Hub:** balasan; menutup tahun.
- **Event karakter:** K18, N17, Mi20.
- **Efek besar:** **Audit Tahun 2.** Sistem memberi **peringatan pertama** bila deviasi terlalu rendah (khususnya untuk Chiasa × Yutaka saja ⭐).
- **Quest Sistem:** Q26 *Audit Kedua*.
- **Risiko:** rendah.

---

### TAHUN 3 — TAGIHAN

#### M25 · April T3 · Tahun Terakhir: Skripsi dan Shukatsu
- **Dasar manga:** Koita memasuki tahun akhir; mencari kerja.
- **Hub:** membantu siapa dalam skripsi/shukatsu; jalur karier pemain.
- **Event karakter:** K19, Mi21, S17, H17.
- **Efek besar:** penentuan arah hidup para heroine setelah lulus.
- **Quest Sistem:** Q27 *Hitung Mundur*.
- **Risiko:** sedang.

#### M26 · Mei T3 · Golden Week: Perjalanan Perpisahan Dini
- **Dasar manga:** perjalanan terakhir bersama.
- **Hub besar #9.**
- **Event karakter:** K20, N18, Mo18, Y15/C14.
- **Efek besar:** Shiori mulai tahap eksekusi bila Rute Revenge aktif.
- **Quest Sistem:** Q28.
- **Risiko:** tinggi.

#### M27 · Juni T3 · Tsuyu Terakhir
- **Hub:** hujan, janji terakhir; **jendela intervensi Moeka #3**.
- **Event karakter:** Mo19, Mi22, H18, S18.
- **Efek besar:** pola Miyuki menetap bila tidak ada intervensi sejak M19. Harumi memutuskan program luar negeri.
- **Quest Sistem:** Q29.
- **Risiko:** sedang.

#### M28 · Juli T3 · Tanabata Ketiga + Ujian
- **Hub:** harapan terakhir.
- **Event karakter:** N19, H19, S19, Mo20.
- **Quest Sistem:** Q30 *Harapan Terakhir*.
- **Risiko:** rendah.

#### M29 · Agustus T3 · Natsu Matsuri Ketiga + Gasshuku Terakhir
**M29a — Natsu Matsuri Ketiga.** Hub besar #10. Event: N20, K21, Mi23, C15/Y16.
**M29b — Gasshuku Terakhir.** Hub besar #11, risiko tinggi. Event: Mo21, S20, H20, K22.
- **Efek besar:** malam pengakuan besar; konfrontasi terakhir antar rute.
- **Quest Sistem:** Q31 *Malam Pengakuan Besar*.
- **Risiko:** tinggi.

#### M30 · September T3 · Tsukimi: Pengumuman Hasil
- **Dasar manga:** hasil ujian akhir, lamaran kerja, pascasarjana.
- **Hub:** menerima atau menolak hasil orang lain.
- **Event karakter:** H21, Mi24, S21, Mo22.
- **Efek besar:** Harumi menerima atau menolak studi luar negeri; Miyuki mendapat hasil CBT/ujian.
- **Quest Sistem:** Q32.
- **Risiko:** sedang.

#### M31 · Oktober T3 · Pilihan Karier
- **Hub:** karier dan hubungan bentrok.
- **Event karakter:** K23, S22, Mo23, Y17/C16, N21.
- **Efek besar:** **Rute Revenge Shiori memasuki eksekusi penuh** bila terpicu. Keluarga Kisaragi menekan Yutaka bila ia NPC.
- **Quest Sistem:** Q33.
- **Risiko:** sedang.

#### M32 · November T3 · Festival Akhir + Pameran Tunggal
- **Hub:** Chiasa pameran tunggal; Moeka peragaan terakhir; turnamen akhir Shiori.
- **Event karakter:** C17/Y18, Mo24, S23, K24.
- **Efek besar:** dampak sosial rute terlihat jelas.
- **Quest Sistem:** Q34.
- **Risiko:** sedang.

#### M33 · Desember T3 · Natal Terakhir + Peringatan Final
- **Hub besar #12.**
- **Event karakter:** N22, Mi25, H22, S24, K25, Mo26 (*Natal Sunyi*, jendela intervensi Moeka #5).
- **Efek besar:** **Peringatan Final Sistem** (3 bulan sebelum wisuda) untuk siapa pun yang deviasinya belum cukup.
- **Quest Sistem:** Q35 *Hitung Mundur Akhir*.
- **Risiko:** tinggi.

#### M34 · Januari T3 · Malam Tanpa Balasan + Ujian Akhir
- **Dasar manga:** ujian akhir; Hatsumode.
- **Hub:** respons pemain pada tanda bahaya.
- **Event karakter:** Mo25 (*Malam Tanpa Balasan*), Mi26, H23, N23.
- **Efek besar:** **titik tanpa kembali Moeka** bila tiga pemicu bertemu. Sisa jendela intervensi tertutup setelah malam ini.
- **Quest Sistem:** Q36.
- **Risiko:** sangat tinggi.

#### M35 · Februari T3 · Festival Musim Dingin Terakhir + Valentine
- **Dasar manga:** pengakuan terakhir; Koita memilih (atau tidak).
- **Hub besar #13 (puncak akhir):** semua konflik bertemu.
- **Event karakter:** K26, S25, N24, Mi27, H24, C18/Y19.
- **Efek besar:** penentuan ending tiap heroine, Koita, dan BL.
- **Quest Sistem:** Q37 *Naskah Terakhir*.
- **Risiko:** sangat tinggi.

#### M36 · Maret T3 · White Day, Wisuda, Evaluasi
- **Hub:** wisuda; evaluasi Sistem; epilog.
- **Event karakter:** K27, semua heroine epilog.
- **Efek besar:** **Evaluasi tunggal (✅)** saat wisuda. Ambang disembunyikan. Gagal = kematian pemain. Setelah itu `resolve_ending()` menetapkan semua ending.
- **Quest Sistem:** Q38 *Kontrak Berakhir*.

---

## 3. Gerbang rute distorsi 🟡
Syarat GDD (✅): kondisi tersembunyi **dan** event penting, bukan salah satunya. Jumlah tahap berbeda per heroine.

| Rute | Event gerbang | Jendela | Syarat tersembunyi | Titik tanpa balik |
|---|---|---|---|---|
| **Miyuki — Masokis** | Mi16 *Kesalahan di Bangsal* (M19) | M13–M27 | Kelelahan Tinggi, dilihat sebagai "dibutuhkan" hanya saat dimarahi, pemain atau Koita tidak menahan | Tahap 5 > 1 semester tanpa intervensi (M25+) |
| **Nagisa — Yandere** | N14 *Cek Pesan* (M18) | M12–M24 | Aff pemain Tinggi, Jealousy Sedang+, harapan pada Koita goyah | N17 (M24); setelah itu hanya Distorted Ending |
| **Harumi — Eksploitasi** | H13 *Dana Lab Dibekukan* (M20) | M17–M26 | Ogawa aktif, kebingungan emosi belum terjawab, pemain tidak hadir | Setelah H17 (M25) tanpa Mizuhara/Ogiwara |
| **Moeka — Death-Flag** | Mo15 *Surat Peringatan Beasiswa* (M20) | M15–M34 | Stres keuangan, topeng tebal, janji tak tertepati | **Mo25 Malam Tanpa Balasan (M34)** |
| **Shiori — Revenge** | S13 *Penemuan* (M20) | M17–M33 | Pemain berbohong atau menyakiti orang yang ia pedulikan | Setelah S18 (M27) hanya ending Distorted/Bad |
| **Chiasa — Koita Success** | C13/K17 (M23) | M11–M24 | Chiasa berhasil bersama Koita | Orang tua pulang (C12/Y13, M21) |

### Hub berisiko tinggi untuk Force Route (✅ GDD 6K) 🟡
M02 (onsen), M05b (vila pantai), M09 (Natal), M17b (pulau), M21 (Natal 2), M23 (pengakuan bentrok), M29b (gasshuku akhir), M33–M35. Di semua hub itu kondisi tersembunyi dan pilihan berlapis diperlukan; tidak ada jalan pintas. Konsekuensi lengkap ada di `Aturan_Evaluasi_dan_Force_Route.md`.

### Jendela intervensi Moeka 🟡
M15, M20, M27, M30, M33 (minimal tiga harus terlewat agar Malam Tanpa Balasan terjadi).

## 4. Tangga quest Sistem NTR 🟡
- **Q01–Q14 (Tahun 1):** pengenalan; sebagian besar membuat pemain mengenal target.
- **Q15–Q26 (Tahun 2):** menggeser takdir secara nyata; kegagalan punya harga (hukuman tahap ringan sampai sedang).
- **Q27–Q38 (Tahun 3):** menuntut hasil; hukuman bisa tahap berat.
- Semua quest: kategori tersembunyi (✅), bisa gagal langsung/tidak langsung, bisa ditunda sebelum deadline, bisa kedaluwarsa atau digantikan event lain (✅).

## 5. Peta ending 🟡
Per heroine: **Bad / Neutral / Distorted / Romantis dengan pemain** (✅ kategori; isi 🟡 ada di file karakter). Ditambah:
- **Ending Koita:** Dipilih / Sendiri / Tetap Menggantung / Hancur.
- **Ending BL:** Berkomitmen / Ditolak / Kembali ke pola lama / Kolaps.
- **Ending Force:** Penjara, Pengusiran dan kehancuran sosial, Lolos tanpa hukuman tapi dihantui (tanpa ending romantis dengan korban).
- **Ending Sistem:** Lolos evaluasi / Gagal evaluasi (kematian) / Mati sebelum wisuda.
- Tidak ada True Ending (✅).

## 6. Registry flag utama 🟡
**Global:** `kesan_awal`, `route_host` (Yutaka/Chiasa), `mc_orientasi`, `harapan_pemain`, `ikut_naskah`.
**Hubungan (tersembunyi):** `aff/trust/intim/jeal/fear` per pasangan.
**Rute:** `miyuki_stage`, `nagisa_stage`, `harumi_stage`, `moeka_stage`, `shiori_stage`, `chiasa_koita_success`.
**Sistem:** `deviasi_total`, `peringatan_1`, `peringatan_final`, `sistem_bocor`, `kuota_quest`.
**Sosial:** `rumor_aktif`, `bukti_digital`, `reputasi_[lingkungan]`, `rahasia_[pasangan]`.
**Risiko:** `force_hub_[M##]` (tersembunyi), `korban_lapor`, `saksi_ada`, `bukti_ditemukan`.
**Moeka:** `beasiswa_status`, `jendela_intervensi_terlewat`, `titik_tanpa_balik`.
**NPC kunci:** `sena_curiga`, `mizuhara_curiga`, `haruto_curiga`, `kuroiwa_curiga`, `rina_curiga`, `mei_punya_info`.

## 7. Yang masih terbuka ❓
- ❓ Tanggal pasti festival dan libur nasional di tiap bulan.
- ❓ Berapa lama timeskip yang boleh dilewati tanpa kehilangan event wajib.
- ~~❓ Apakah event manga asli bisa dibatalkan seluruhnya (GDD: "mostly" berjalan).~~ **Terjawab:** boleh batal permanen setelah penyimpangan besar (✅ GDD 6N.2, ditambah arahanmu untuk cabang sebebas mungkin ⭐). Aturan berjalan/bermutasi/ditunda/batal ada di [Alur_Cabang/00_Pohon_Global.md](Alur_Cabang/00_Pohon_Global.md) §5.
