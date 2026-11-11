# GAME DESIGN DOCUMENT — KOUSEIKAN

**Versi:** 1.29 — Addendum audit final Batch 20; keputusan ekonomi #1–#84 dan klarifikasi #1–#9
**Tanggal:** 10 November 2026
**Status:** Dokumen kerja; bukan pengganti Master Canon.
**Referensi canon:** Master_Canon_Visual_Novel_Kouseikan_v11.1.md

## 1. Tujuan dokumen
GDD ini mendefinisikan pengalaman bermain dan aturan desain Kouseikan sebagai Interactive Visual Novel. Fokusnya adalah narasi interaktif, simulasi kehidupan NPC, relationship system, branching choices, dan NTR mechanics. Implementasi teknis (engine, kode, struktur data, database, dan arsitektur perangkat lunak) ditunda ke tahap berikutnya.

## 2. Identitas dan format game
- Genre/format: 2D Interactive Visual Novel / Interactive Storytelling dengan unsur life simulation dan sandbox naratif.
- Presentasi: **Classic Visual Novel 2D**.
- Komponen visual utama: background lokasi, sprite karakter, kotak dialog, dan tombol pilihan.
- Interaksi utama: pemain memilih dialog/tindakan melalui tombol pilihan yang disediakan game. Free-form text input bukan metode interaksi utama yang dipilih.
- Fokus desain: narasi, kehidupan NPC, hubungan, pilihan bercabang, konflik, konsekuensi, dan sistem NTR.

## 3. Design pillars
1. **Interactive Storytelling:** cerita berkembang melalui pilihan dan tindakan pemain.
2. **Living NPCs:** NPC memiliki jadwal, relasi, aktivitas, dan perkembangan di luar interaksi langsung dengan pemain.
3. **Relationship Simulation:** hubungan merupakan proses bertahap dan tidak otomatis mengikuti kehendak pemain.
4. **Branching Choices:** pilihan dapat mengubah adegan, relasi, akses event, dan arah cerita.
5. **NTR Mechanics:** konflik hubungan, rivalitas, perubahan takdir romantis, dan konsekuensi merupakan bagian inti gameplay.
6. **Player Freedom:** tidak ada kewajiban semua heroine jatuh cinta kepada pemain atau berakhir bersama pemain.

## 4. Struktur rute protagonis (canon)
- **Male Route:** pemain mengambil alih Kisaragi Yutaka. Amamiya Chiasa tetap NPC independen dan merupakan heroine Koita. Yutaka asli diam-diam menyukai Chiasa.
- **Female Route:** pemain mengambil alih Amamiya Chiasa. Yutaka tetap NPC independen. Chiasa asli diam-diam mencintai Koita.
- Kujo Harumi (nama lama: Kujo Ritsuka) adalah NPC heroine Koita, bukan protagonis Female Route.

## 5. Status heroine pada awal permainan (canon)
- Tachibana Miyuki: sudah mencintai Koita.
- Sakurajima Nagisa: sudah mencintai Koita.
- Kujo Harumi (sebelumnya Ritsuka): sudah mencintai Koita.
- Kohinata Moeka: sudah mencintai Koita.
- Saionji Shiori: belum mencintai Koita.
- Amamiya Chiasa: heroine tambahan Koita di luar lima heroine utama manga.

## 6. Core gameplay loop — konsep tingkat tinggi
Siklus gameplay yang akan dirinci lebih lanjut:
1. Pemain menentukan aktivitas/tindakan melalui pilihan yang tersedia.
2. Pemain berinteraksi dengan lokasi, karakter, atau aktivitas.
3. Pemain membuat pilihan dialog atau tindakan.
4. Dunia dan NPC bereaksi sesuai kondisi, jadwal, hubungan, serta konteks.
5. Konsekuensi dapat mengubah relasi, membuka/menutup event, dan memengaruhi perkembangan cerita.
6. Waktu dan kehidupan dunia berlanjut sesuai durasi tindakan.

Catatan: ini kerangka konseptual, bukan spesifikasi final durasi atau aturan waktu.

## 6A. Navigasi dunia dan peta (keputusan v0.2)
- Navigasi lokasi menggunakan **peta kota berbasis distrik**.
- Cakupan peta tidak terbatas pada Universitas Kouseikan; peta mencakup universitas dan berbagai lokasi di kota.
- Contoh kategori lokasi: area/fasilitas universitas, rumah karakter, apartemen karakter, pusat perbelanjaan, restoran, dan lokasi publik atau tempat lain yang relevan.
- Alur navigasi: pemain memilih **distrik** terlebih dahulu, kemudian memilih **lokasi** di dalam distrik tersebut.
- Presentasi tetap mengikuti format Classic Visual Novel 2D; peta merupakan layar/menu navigasi, bukan perubahan menjadi eksplorasi top-down.
- Daftar distrik, nama lokasi, syarat membuka lokasi, biaya/waktu perjalanan, dan dampak perjalanan terhadap jadwal NPC **belum ditetapkan**.

## 6B. Distorted Heroine Routes (keputusan desain v0.3)

### 6B.1 Konsep umum
- Nama sistem: **Distorted Heroine Routes**.
- Sistem ini menyediakan rute alternatif ketika pemain terlalu jauh merusak kondisi emosional, psikologis, atau kehidupan heroine.
- Pemicu tidak hanya berasal dari satu tindakan: sistem mempertimbangkan **akumulasi tindakan buruk/pengabaian/manipulasi pemain** dan **peristiwa kehidupan heroine di luar kendali pemain**.
- Perubahan berlangsung **bertahap**, dengan satu atau beberapa peristiwa besar sebagai titik balik.
- Setiap heroine memiliki tingkat kerusakan/kondisi psikologis tersembunyi; angka atau meter pastinya **tidak ditampilkan kepada pemain**.
- Pemulihan dimungkinkan untuk sebagian heroine, sedangkan pada heroine lain kondisi tertentu dapat menjadi permanen. Identitas heroine yang dapat/tidak dapat dipulihkan dan syaratnya **BELUM DITETAPKAN**.
- Distorted Route bukan perubahan kepribadian instan. Perubahan harus dibangun melalui rangkaian adegan, pilihan, respons NPC, dan konsekuensi yang konsisten.

### 6B.2 Rute khusus per heroine

**Tachibana Miyuki — Masochistic Route**
- Arah perubahan: menjadi masokis secara emosional sekaligus romantis/seksual.
- Perubahan emosional dapat membuatnya mengasosiasikan perlakuan buruk, penghinaan, atau penderitaan dengan perhatian/kasih sayang.
- Sisi romantis/seksual berhubungan dengan ketertarikan pada dinamika dominasi dan penyerahan kendali.
- Tahap, batas, pemicu spesifik, serta kemungkinan pemulihan **BELUM DITETAPKAN**.

**Sakurajima Nagisa — Yandere Route**
- Pusat obsesi Nagisa dalam rute ini adalah **pemain**, bukan Koita.
- Cinta, kecemburuan, dan ketakutan kehilangan dapat berkembang menjadi obsesi serta perilaku posesif.
- Bentuk eskalasi, tindakan spesifik, titik balik, dan kemungkinan pemulihan **BELUM DITETAPKAN**.

**Kujo Harumi (nama lama: Kujo Ritsuka) — Hypersexual / Exploitation Route**
- Arah perubahan: menjadi sangat terobsesi dengan seks dan validasi seksual.
- Jalur dapat mencakup perilaku promiscuous, penggunaan seks sebagai alat memperoleh perhatian/uang/kekuasaan, dan kemungkinan memasuki dunia prostitusi.
- Semua tahap merupakan kemungkinan perkembangan naratif, bukan hasil otomatis; pemicu, agensi karakter, batas, dan kemungkinan pemulihan **BELUM DITETAPKAN**.

**Kohinata Moeka — Suicide Death-Flag Route**
- Arah rute: risiko bunuh diri muncul dari **akumulasi stres**.
- Kondisi keluarga Moeka juga sedang **tidak baik-baik saja**; bentuk masalah keluarga secara spesifik **BELUM DITETAPKAN**.
- Rute diperlakukan sebagai tragedi psikologis serius, bukan kejutan sensasional. Penggambaran tidak grafis dan berfokus pada kondisi, tanda bahaya, dampak, serta kemungkinan intervensi/konsekuensi.
- Apakah kematian dapat dicegah dalam semua cabang, syarat intervensi, dan ending spesifik **BELUM DITETAPKAN**.

**Saionji Shiori — Destructive Revenge Route**
- Arah rute: Shiori berusaha menghancurkan kehidupan pemain atau orang-orang yang menjadi sasaran kemarahannya.
- Kemampuan Shiori untuk menghancurkan pemain **tidak bergantung pada dukungan atau pengaruh keluarga Saionji**; dia mampu melakukannya dengan kapasitas dan upayanya sendiri.
- Metode, sumber daya, sasaran, tahapan eskalasi, dan kemungkinan pemulihan **BELUM DITETAPKAN**.

### 6B.3 Rute khusus Chiasa — Koita Success / Step-Sibling Taboo Route
- Chiasa memiliki rute khusus yang berbeda dari lima Distorted Heroine Routes lainnya.
- Pemicu rute aneh Chiasa justru ketika **Chiasa berhasil menjalin hubungan dengan Koita**.
- Keanehan/konflik utamanya adalah hubungan romantis antara saudara tiri yang telah tinggal dan tumbuh bersama sejak kecil. Mereka **tidak memiliki hubungan darah**, tetapi relasi tersebut membawa unsur tabu keluarga/step-sibling yang dapat dipersepsikan sebagai incest secara sosial atau tematik.
- Rute ini tidak otomatis berarti Chiasa mengalami kerusakan psikologis seperti lima rute lainnya; sifat, konflik, konsekuensi, dan ending khususnya **BELUM DITETAPKAN**.



### 6B.5 Aturan aktivasi dan cakupan rute (keputusan v0.4)
- Distorted Heroine Routes tersedia pada **Male Route maupun Female Route**. Tidak ada pembatasan bahwa rute tertentu hanya bisa muncul pada salah satu protagonis; detail interaksi dan konteksnya dapat berbeda sesuai rute protagonis.
- **Semua enam rute khusus** (lima heroine utama dan rute khusus Chiasa) dapat aktif dalam satu playthrough secara bersamaan. Rute-rute tersebut tidak saling eksklusif secara default.
- Pembukaan setiap rute membutuhkan **kondisi/ambang tertentu sekaligus event penting**. Memenuhi kondisi saja tidak otomatis membuka rute tanpa peristiwa naratif yang relevan.
- Jumlah dan susunan tahap perubahan **berbeda untuk setiap heroine**; tidak ada satu template jumlah tahap yang wajib dipakai semua karakter.
- Pemain tidak melihat angka, meter, atau status psikologis numerik. Pemain membaca perubahan melalui **dialog, ekspresi, dan perilaku** heroine.
- NPC lain, terutama **teman dan keluarga dekat**, dapat menyadari perubahan heroine. Seberapa cepat dan seberapa tepat mereka memahami masalah bergantung pada kedekatan serta situasi naratif.
- Pemain dapat **sengaja mengejar/memicu** Distorted Route melalui manipulasi hubungan dan tindakan yang relevan. Rute juga dapat berkembang dari konsekuensi dan peristiwa kehidupan yang tidak sepenuhnya dikendalikan pemain.
- Dampak rute tidak terbatas pada heroine: perubahan dapat memengaruhi **lingkaran sosial heroine**, termasuk hubungan dengan teman, keluarga, dan karakter lain yang relevan.
- Setiap heroine memiliki beberapa kemungkinan ending dalam kelompok **Bad Ending, Neutral Ending, dan Distorted Ending**. Makna, syarat, variasi, dan jumlah ending spesifik belum ditetapkan.
- **Rute khusus Chiasa** menggunakan fondasi sistem yang sama, tetapi memiliki **mekanik dan konsekuensi khusus**. Pemicu khasnya tetap keberhasilan Chiasa menjalin hubungan dengan Koita; ia bukan sekadar salinan dari lima rute Distorted lainnya.

### 6B.6 Konsekuensi desain dari keputusan v0.4
- Karena beberapa rute dapat aktif bersamaan, desain event harus memperhitungkan kemungkinan konflik atau tumpang tindih jadwal, hubungan, dan reaksi NPC.
- Karena keluarga/teman dekat dapat menyadari perubahan, NPC pendukung perlu memiliki reaksi dan konsekuensi sosial yang masuk akal; mereka tidak otomatis mengetahui seluruh penyebab atau detail kondisi heroine.
- Karena jumlah tahap berbeda per karakter, tiap heroine membutuhkan struktur perkembangan, titik balik, dan tanda-tanda perilaku yang dirancang secara individual.
- Karena pemain dapat sengaja mengejar rute, pilihan manipulatif harus memiliki konsekuensi dan risiko yang terbaca melalui narasi, bukan sekadar menjadi tombol tanpa dampak.
- Hal-hal tersebut adalah prinsip desain tingkat tinggi; urutan event, ambang, kondisi gabungan, pemulihan, dan ending spesifik tetap terbuka.

### 6B.4 Batas desain dan hal yang belum ditetapkan
- Distorted Routes harus tumbuh dari akumulasi kondisi dan keputusan, bukan satu meter tunggal yang secara ajaib mengendalikan karakter.
- Sistem tersembunyi memantau kondisi, tetapi pemain mempelajari perubahan melalui perilaku, dialog, event, dan konsekuensi.
- Tidak semua rute harus dapat dipulihkan; status tiap heroine belum ditetapkan.
- ~~Belum ditentukan apakah rute-rute ini eksklusif, dapat saling tumpang tindih, atau dapat aktif bersamaan.~~ **SUPERSEDED oleh v0.4:** semua enam rute dapat aktif bersamaan dalam satu playthrough.
- Belum ditentukan nama variabel/status internal, angka ambang kondisi, urutan event spesifik, jumlah dan susunan tahap masing-masing heroine, serta syarat dan variasi ending.
- Belum ditentukan detail perbedaan konteks rute Male/Female, reaksi spesifik masing-masing teman/keluarga, serta detail mekanik khusus Chiasa.

## 7. Ruang lingkup bab GDD
### Part I — Core Game Design
- Game overview dan player experience
- Core gameplay loop
- Struktur sesi dan alur hari

### Part II — World & Life Simulation
- Navigasi lokasi dan pemilihan tempat
- Kalender dan waktu
- Aktivitas harian
- NPC schedule dan autonomous behavior
- Event dunia dan event berbasis kondisi

### Part III — Character & Relationship
- Interaksi karakter dan dialog
- Relationship dimensions
- Affection, trust, intimacy, familiarity, jealousy, rivalry
- NPC-to-NPC relationship simulation

### Part IV — Narrative Design
- Struktur cerita utama dan subplot
- Branching choices dan konsekuensi
- Character routes dan route availability
- Dynamic events dan scene conditions

### Part V — NTR Gameplay
- Fungsi dan batas Sistem NTR
- Misi utama/sampingan/darurat
- Fate Deviation dan evaluasi kontrak
- Rivalitas romantis, pengkhianatan, dan perubahan hubungan
- Reward, warning, dan punishment

### Part VI — Player Progression & Resources
- Perkembangan personal
- Reputasi sosial
- Uang dan sumber daya
- Unlockable content

### Part VII — Content Design
- Lokasi, aktivitas, event, side stories
- Ending dan outcome

### Part VIII — UI/UX Design (non-technical)
- Classic VN screen composition
- Dialogue box dan choice buttons
- Character sprites, expressions, poses
- Location/background presentation
- Status, map/location selection, schedule, relationship information

## 8. Hal yang belum ditetapkan
- Detail layout layar Classic VN, posisi sprite, jumlah sprite sekaligus, ekspresi/pose, transisi, dan variasi background.
- ~~Apakah perpindahan lokasi dilakukan melalui menu peta, daftar lokasi, atau pilihan naratif.~~ **SUPERSEDED oleh keputusan v0.2:** navigasi menggunakan peta kota berbasis distrik.
- Struktur waktu final, durasi tindakan, dan batas aksi per hari.
- Dimensi relationship final, skala, ambang, decay, dan visibilitas informasi kepada pemain.
- Aturan rinci NPC autonomy, prioritas jadwal, konflik jadwal, dan event simulation.
- Format branching, konsekuensi permanen/sementara, dan cara mengelola route flags.
- Rincian UI Sistem NTR, bentuk misi, dan tampilan Fate Deviation.
- Detail pemicu, tahapan, pemulihan, dan ending setiap Distorted Heroine Route; kemungkinan beberapa rute aktif bersamaan; detail rute khusus Chiasa.
- Semua detail implementasi teknis.

## 9. Aturan pemeliharaan GDD
1. Master Canon adalah sumber kebenaran untuk lore dan fakta karakter. GDD menjelaskan bagaimana fakta tersebut menjadi pengalaman dan aturan gameplay.
2. Jangan mengubah canon melalui asumsi desain. Jika ada konflik, tandai dan minta keputusan pemain.
3. Jangan menghapus keputusan lama; jika diganti, gunakan label **SUPERSEDED** dan catat versi penggantinya.
4. Tambahkan keputusan yang disetujui ke GDD dan Master Canon yang relevan.
5. Pembahasan teknis ditunda sampai desain pengalaman dan sistem gameplay cukup matang.
6. GDD diperbarui secara berkala setiap enam pertanyaan desain yang dijawab pemain. Keputusan yang sudah disepakati tetap menjadi acuan selama proses pengumpulan; pembaruan dokumen dilakukan saat siklus enam pertanyaan tercapai atau jika pemain meminta pembaruan lebih awal.

## 10. Changelog
- **v1.20 — 10 Nov 2026:** Mempertahankan seluruh isi v1.19; menambahkan visual canon Shiori (ACC), revisi visual Miyuki (rambut lurus tanpa hiasan kepala, ACC), dan draft visual Nagisa (belum ACC) menggunakan template character sheet yang sama tanpa kategori baru.
- **v1.18 — 10 Nov 2026:** Mempertahankan seluruh isi v1.17 dan memasukkan enam keputusan pertama Batch 19: event ditemukan melalui observasi/interaksi/jadwal/informasi dunia; semua quest berasal dari Sistem NTR; quest memiliki kategori/tingkat kepentingan yang tidak ditampilkan; percakapan dapat menjadi konteks/pemicu sesuai hubungan dan situasi; event rahasia ditemukan melalui eksplorasi dan kondisi tersembunyi; quest dapat memiliki beberapa solusi dengan konsekuensi berbeda serta dapat gagal akibat tindakan pemain. Empat keputusan terakhir Batch 19 ditahan untuk pembaruan berikutnya.

- **v1.17 — 10 Nov 2026:** Mempertahankan seluruh isi v1.16 dan memasukkan empat keputusan terakhir Batch 17 serta enam keputusan pertama Batch 18: profil host yang diketahui NPC bergantung rute/karakter; pemain dapat mengganti pakaian dan aksesori tetapi bukan penampilan dasar host; prolog dan perspektif Male/Female Route berbeda; hubungan awal host mengikuti canon masing-masing; pemain hanya mengetahui garis besar manga dan beberapa spoiler; pengetahuan dapat menjadi tidak akurat akibat penyimpangan; perasaan awal heroine diketahui sejauh tercakup manga; rahasia keluarga/masa lalu NPC harus ditemukan; petunjuk dapat ambigu/menyesatkan; jurnal tidak memberi label kepastian fakta/dugaan/rumor. Empat jawaban terakhir Batch 18 ditahan untuk pembaruan berikutnya.

- **v1.16 — 10 Nov 2026:** Mempertahankan seluruh isi v1.15 dan memasukkan enam keputusan pertama Batch 17: gender/rute dipilih sebelum cerita; Male Route menggunakan Kisaragi Yutaka dan Female Route menggunakan Amamiya Chiasa; nama canon host tidak dapat diganti; pemain bebas menentukan kepribadian dan gaya interaksi; fondasi keluarga host tetap canon tetapi hubungan keluarga dapat berubah. Empat keputusan terakhir Batch 17 ditahan untuk pembaruan berikutnya.

- **v1.14 — 10 Nov 2026:** Mempertahankan seluruh isi v1.13 dan memasukkan empat keputusan terakhir Batch 15 serta dua keputusan pertama Batch 16: berita kota mencakup berita lokal/rumor/kejadian NPC; kota berubah secara visual dan gameplay menurut waktu/musim; tempat tinggal pemain sudah ditentukan dan tidak ada sistem beli/sewa properti; NPC mengalami kejadian kota tanpa pemain jika relevan; tersedia media sosial fiktif dan grup chat; pemain memiliki ponsel sebagai menu komunikasi/informasi.
- **v1.15 — 10 Nov 2026:** Mempertahankan seluruh isi v1.14 dan memasukkan enam keputusan berikutnya Batch 16: komunikasi NPC berupa chat, telepon, atau pertemuan langsung sesuai hubungan/situasi; rumor menyebar otomatis melalui jaringan NPC maupun tindakan pemain; informasi dapat salah atau dimanipulasi sesuai sumber; pemain dapat mengunggah dan memengaruhi opini NPC; NPC memiliki akun serta aktivitas media sosial mandiri; pesan pribadi dapat memicu event, pesan mendadak, dan undangan. Dua keputusan terakhir Batch 16 (blokir/abaikan kontak serta bukti digital) ditahan untuk pembaruan berikutnya.

- **v1.13 — 10 Nov 2026:** Mempertahankan seluruh isi v1.12 dan memasukkan enam keputusan pertama Batch 15: tempat kota memiliki jam operasional; NPC dapat bepergian ke lokasi lain; transportasi menggabungkan berjalan kaki, transportasi umum, dan kendaraan pribadi; kota memiliki festival, konser, pameran, serta acara musiman; sebagian fasilitas interaktif dan sebagian hanya latar; NPC dapat mengunjungi rumah/apartemen karakter lain sesuai karakter dan izin/keadaan. Empat keputusan terakhir Batch 15 ditahan untuk pembaruan berikutnya.

- **v1.11 — 10 Nov 2026:** Mempertahankan seluruh isi v1.10 dan memasukkan dua keputusan terakhir Batch 13 serta empat keputusan pertama Batch 14: dialog memiliki autoplay dan skip; pengaturan lengkap mencakup kecepatan dialog, volume terpisah, dan preferensi visual; durasi cerita utama tiga tahun sampai kelulusan; chapter naratif berjalan bersama kalender; timeskip tersedia untuk periode yang tidak perlu dimainkan detail; main story menggunakan milestone dengan perkembangan dinamis di antaranya.
- **v1.12 — 10 Nov 2026:** Mempertahankan seluruh isi v1.11 dan memasukkan enam keputusan terakhir Batch 14: pemain dapat mengubah hasil akhir manga asli sepenuhnya; tersedia New Game Plus dengan informasi tambahan; tersedia galeri CG dan replay event; tingkat kesulitan adaptif; achievement termasuk rahasia; rekap akhir playthrough mencakup hubungan, event, ending, keputusan, konsekuensi, dan perkembangan dunia.

- **v1.9 — 10 Nov 2026:** Mempertahankan seluruh isi v1.8 dan memasukkan empat keputusan terakhir Batch 12 serta dua keputusan pertama Batch 13: jadwal NPC tidak ditampilkan dan harus dicari tahu pemain; inventory menyimpan hadiah/barang/dokumen/item; notifikasi Sistem NTR menggunakan kotak khusus dan dialog persona AI; save system memiliki manual save, autosave, dan beberapa slot; sprite full body/half body bergantung adegan dengan variasi ekspresi dan pose; kostum berubah berdasarkan musim, kegiatan, dan event.
- **v1.10 — 10 Nov 2026:** Mempertahankan seluruh isi v1.9 dan memasukkan enam keputusan berikutnya Batch 13: CG khusus mencakup event penting, momen spesial, rahasia, dan event alternatif; transisi bergantung jenis adegan; BGM merupakan kombinasi lokasi, karakter, dan suasana; SFX dinamis berdasarkan situasi; game menggunakan full voice acting. Dua keputusan terakhir Batch 13 (autoplay/skip dan pengaturan lengkap) ditahan untuk siklus pembaruan berikutnya.

- **v1.8 — 9 Nov 2026:** Mempertahankan seluruh isi v1.7 dan memasukkan enam keputusan pertama Batch 12: UI dialog Classic VN dapat disembunyikan; pilihan dialog menyesuaikan jenis event; menu status menampilkan kondisi, skill, uang, dan informasi pribadi; informasi hubungan tersedia melalui profil karakter dan jurnal interaksi tanpa angka relationship; jurnal mencatat event, informasi diketahui, rumor, petunjuk, dan rahasia yang ditemukan; peta distrik berupa ilustrasi dengan menu detail lokasi. Empat keputusan terakhir Batch 12 ditahan untuk pembaruan berikutnya.

- **v1.5 — 9 Nov 2026:** Mempertahankan seluruh isi v1.4 dan memasukkan enam keputusan berikutnya: NPC dapat mengambil keputusan penting mandiri; NPC dapat saling berbohong; respons rumor bergantung karakter dan kedekatan sumber; tujuan pribadi bergantung karakter; perkembangan kepribadian melalui pengalaman terjadi dalam character route; opini NPC tentang pemain bergantung kredibilitas informasi dan hubungan.
- **v1.6 — 9 Nov 2026:** Mempertahankan seluruh isi v1.5 dan memasukkan enam keputusan berikutnya: NPC dapat menyimpan rahasia pribadi/keluarga/hubungan; NPC dapat menyelesaikan konflik sendiri sesuai konteks; investigasi polisi bergantung tingkat keparahan; korban melapor sesuai karakter, kondisi psikologis, dan bukti; saksi merespons sesuai situasi; bukti dapat ditemukan belakangan sesuai jenis bukti dan investigasi.
- **v1.7 — 9 Nov 2026:** Mempertahankan seluruh isi v1.6 dan memasukkan enam keputusan berikutnya: tidak ada reputasi kriminal khusus; konsekuensi hukum melalui laporan korban mensyaratkan korban melapor; dampak akademik bergantung tingkat kasus; NPC menjauh/memutus hubungan sesuai karakter dan relasi; Force Route dapat berakhir tanpa penjara tetapi tetap dengan kehancuran sosial/psikologis; Broken Heroine Ending dapat terjadi tanpa kejahatan terbongkar karena kerusakan psikologis terpisah dari sistem hukum.

- **v1.4 — 9 Nov 2026:** Mempertahankan seluruh isi v1.3 dan memasukkan enam keputusan: empat keputusan terakhir Batch 9 (pasangan romantis NPC mengikuti canon; kegagalan hubungan bervariasi sesuai karakter/sebab; event kedekatan mayoritas dinamis; pemain dapat tamat tanpa pasangan dan hal itu dapat memengaruhi evaluasi) serta dua keputusan pertama Batch 10 (kepribadian konsisten namun dapat berkembang melalui pengalaman; NPC dapat menyembunyikan perasaan dan berbohong kepada pemain). Delapan jawaban terakhir Batch 10 ditahan untuk pembaruan berikutnya.

- **v1.3 — 9 Nov 2026:** Mempertahankan seluruh isi v1.2 dan memasukkan enam keputusan pertama Batch 9: setiap heroine memiliki personal storyline panjang; character route dibuka melalui kombinasi hubungan, event, dan kondisi tersembunyi; benturan route bergantung karakter/situasi; heroine dapat memilih Koita tanpa campur tangan pemain melalui event manga asli; pemain dapat merusak hubungan Koita dengan heroine melalui tindakan/manipulasi; setiap heroine memiliki kemungkinan ending romantis dengan pemain. Empat jawaban terakhir Batch 9 ditahan untuk pembaruan berikutnya sesuai aturan enam jawaban per pembaruan.

- **v1.0 — 9 Nov 2026:** Mempertahankan seluruh isi v0.9 dan memasukkan enam keputusan lanjutan Batch 7 (nomor 3–8): deadline bergantung jenis/kepentingan misi; hadiah adaptif; hukuman bergantung jenis misi; pemain tidak dapat menolak misi; target NTR tersembunyi sampai evaluasi akhir; persona Sistem NTR sarkastis, provokatif, dan suka mengejek.
- **v1.1 — 9 Nov 2026:** Mempertahankan seluruh isi v1.0 dan memasukkan dua keputusan terakhir Batch 7 serta empat keputusan pertama Batch 8: informasi NPC dari sistem terbatas; evaluasi kontrak hanya saat kelulusan; main story dan sandbox berjalan paralel; event memakai kombinasi jadwal tetap dan kondisi dinamis; event manga asli umumnya tetap berjalan sampai penyimpangan besar; plot armor Koita selalu memberinya kesempatan romantis melalui kebetulan.
- **v1.2 — 9 Nov 2026:** Mempertahankan seluruh isi v1.1 dan memasukkan enam keputusan terakhir Batch 8: NPC mengingat pilihan event secara konsisten; pilihan dialog banyak dengan konsekuensi tersembunyi; event memiliki banyak outcome; event gagal/terlewat ditangani sesuai jenis; tindakan pemain dapat memicu konflik baru; game memiliki banyak ending tanpa True Ending.

- **v0.9 — 9 Nov 2026:** Mempertahankan seluruh isi v0.8. Memasukkan empat keputusan tersisa Batch 6: hadiah NPC dengan preferensi karakter; aktivitas sosial umum dan event karakter; reputasi berbeda menurut lingkungan sosial; kebebasan aktivitas harian dengan tekanan misi/deadline Sistem NTR. Memasukkan dua keputusan pertama Batch 7: Sistem NTR memiliki persona AI yang dapat diajak bicara; struktur misi sepenuhnya dinamis berdasarkan situasi. Keputusan Batch 7 nomor 3–10 sudah dijawab dan menunggu giliran integrasi sesuai aturan pembaruan setiap enam jawaban.

- **v0.8 — 9 Nov 2026:** Mempertahankan seluruh isi v0.7 dan memasukkan enam keputusan pertama Batch 6 Player Activities: aktivitas pemain luas dan bebas; kuliah opsional dengan konsekuensi akademik; pekerjaan part-time dan pekerjaan khusus dengan jadwal serta gaji; pengembangan skill pribadi; ekonomi lengkap untuk pemasukan/pengeluaran/anggaran termasuk pekerjaan, belanja, hadiah, dan biaya hidup; kencan bebas jika kondisi memungkinkan. Empat keputusan terakhir Batch 6 dicatat untuk pembaruan berikutnya sesuai aturan enam jawaban per pembaruan.

- **v0.7 — 9 Nov 2026:** Mempertahankan seluruh isi v0.6 dan menambahkan 10 keputusan Batch 5 Time & Calendar: hari 24 jam; dialog/interaksi menghabiskan waktu; kalender mencakup akademik, hari libur, acara kota, tanggal dan musim; hari Senin–Minggu; cuaca dinamis; empat musim Jepang; event yang terlambat dapat terlewat permanen; aktivitas menggunakan kombinasi AP dan waktu; pemain bebas memilih kapan tidur; rutinitas mingguan tersedia tetapi boleh diabaikan. Rincian implementasi gameplay tetap terbuka.

- **v0.6 — 9 Nov 2026:** Mempertahankan seluruh isi v0.5 dan menambahkan enam keputusan pertama Batch 4 NPC Life Simulation: setiap NPC memiliki jadwal harian penuh; melakukan aktivitas mandiri; berpindah lokasi mengikuti jadwal/kebutuhan; dapat menginisiasi interaksi jika situasi memungkinkan; lokasi tetap dapat dikunjungi saat NPC tidak hadir; NPC dapat membuat janji yang mungkin dilanggar. Empat jawaban Batch 4 sisanya ditahan untuk siklus pembaruan berikutnya.

- **v0.5 — 9 Nov 2026:** Mempertahankan seluruh isi v0.4 dan menambahkan 10 keputusan Batch 3 Relationship System: lima dimensi hubungan (Affection, Trust, Intimacy, Jealousy, Fear); kemunduran hubungan tanpa tindakan langsung pemain hanya pada event tertentu; relasi romantis NPC-ke-NPC dibatasi pada pasangan canon; pemain dapat memengaruhi kualitas/dinamika relasi NPC yang sudah ada; penolakan tidak menutup kesempatan mencoba memperbaiki hubungan tetapi tidak menjamin keberhasilan; pemicu kecemburuan bersifat spesifik karakter; hubungan dapat disembunyikan dengan risiko terbongkar; NPC mengingat perlakuan buruk; emosi yang bertentangan dapat hadir bersamaan; dan kondisi hubungan tidak ditampilkan sebagai angka, melainkan melalui narasi/perilaku. Menambahkan daftar detail yang masih perlu dirancang.

- **v0.4 — 9 Nov 2026:** Mempertahankan seluruh isi v0.3 dan menambahkan 10 keputusan Batch 2: seluruh rute tersedia pada Male dan Female Route; keenam rute dapat aktif bersamaan; pembukaan membutuhkan ambang kondisi dan event penting; jumlah tahap berbeda per heroine; kondisi dibaca melalui dialog/ekspresi/perilaku; teman dan keluarga dekat dapat menyadari perubahan; pemain dapat sengaja mengejar rute melalui manipulasi; dampak meluas ke lingkaran sosial; setiap heroine memiliki beberapa ending Bad, Neutral, dan Distorted; rute Chiasa memakai fondasi yang sama dengan mekanik/konsekuensi khusus. Mengganti status lama tentang simultanitas rute menjadi SUPERSEDED.
- **v0.3 — 9 Nov 2026:** Mempertahankan seluruh isi v0.2 dan menambahkan sistem **Distorted Heroine Routes** berdasarkan 10 jawaban pemain: pemicu berupa akumulasi tindakan buruk pemain dan peristiwa hidup heroine; perubahan bertahap dengan titik balik; pemulihan hanya mungkin bagi sebagian heroine; tingkat kerusakan tersembunyi. Menambahkan arah rute Miyuki (masokis emosional dan romantis/seksual), Nagisa (yandere dengan pemain sebagai pusat obsesi), Harumi (hypersexual hingga kemungkinan prostitusi), Moeka (risiko bunuh diri akibat akumulasi stres dan masalah keluarga), Shiori (mampu menghancurkan pemain tanpa dukungan keluarga), serta rute khusus Chiasa ketika berhasil bersama Koita dengan konflik tabu saudara tiri tanpa hubungan darah. Detail pemicu/tahap/ending tetap terbuka.
- **v0.2 — 9 Nov 2026:** Menambahkan navigasi peta kota berbasis distrik. Peta mencakup Universitas Kouseikan dan lokasi kota seperti rumah karakter, apartemen, pusat perbelanjaan, restoran, serta lokasi lain. Pemain memilih distrik terlebih dahulu, lalu memilih lokasi di dalam distrik. Menetapkan cadence pembaruan GDD setiap enam pertanyaan desain.
- **v0.1 — 9 Nov 2026:** Dokumen GDD awal. Mencatat fokus Interactive Visual Novel, prioritas narasi/NPC simulation/relationship/branching/NTR, struktur protagonis Male/Female Route, status heroine, button-choice interaction, serta keputusan presentasi Classic Visual Novel 2D.


## 6C. Relationship System (keputusan Batch 3)

### 6C.1 Dimensi hubungan
Setiap karakter memiliki beberapa parameter hubungan yang terpisah:
- **Affection:** perasaan suka/cinta terhadap karakter lain.
- **Trust:** tingkat kepercayaan.
- **Intimacy:** kedekatan emosional dan personal.
- **Jealousy:** kecemburuan yang dapat muncul dari pemicu tertentu.
- **Fear:** rasa takut atau kewaspadaan terhadap karakter lain.

Parameter ini merupakan model desain internal. Pemain **tidak melihat angka atau meter hubungan**; perubahan dibaca melalui dialog, ekspresi, perilaku, dan respons karakter.

### 6C.2 Perubahan hubungan dan otonomi NPC
- Hubungan dapat memburuk tanpa tindakan langsung pemain, tetapi hanya pada **event atau situasi tertentu** yang relevan. Perubahan tidak terjadi secara acak tanpa konteks.
- NPC dapat memiliki hubungan romantis satu sama lain, tetapi pasangan romantis yang tersedia dibatasi pada **pasangan yang sudah ditentukan dalam canon**. Sistem tidak otomatis membentuk pasangan romantis baru secara bebas.
- Hubungan NPC-ke-NPC tetap dapat dipengaruhi pemain: pemain dapat memperbaiki atau merusak kualitas/dinamika hubungan yang sudah ada melalui tindakan dan event. Keputusan ini tidak dengan sendirinya mengizinkan pembentukan pasangan romantis baru di luar canon.
- NPC mengingat perlakuan buruk pemain. Ingatan tersebut dapat memengaruhi interaksi berikutnya secara permanen atau dalam jangka panjang.
- Karakter dapat memiliki perasaan yang bertentangan secara bersamaan, misalnya masih mencintai seseorang tetapi juga membencinya atau takut kepadanya.

### 6C.3 Penolakan, kecemburuan, dan rahasia
- Karakter dapat menolak pemain. Pemain tetap memiliki kesempatan untuk mencoba memperbaiki hubungan, tetapi kesempatan tersebut **tidak menjamin** karakter akan memaafkan, menerima, atau kembali memiliki perasaan yang sama.
- Setiap karakter memiliki tingkat kecemburuan dan pemicu kecemburuan masing-masing; tidak ada satu pola pemicu yang harus berlaku sama untuk semua karakter.
- Pemain dapat menyembunyikan hubungan dari NPC lain. Rahasia memiliki risiko terbongkar melalui situasi, interaksi, atau event yang relevan.
- Cara rahasia diketahui, siapa yang mengetahuinya, serta konsekuensinya ditentukan oleh konteks naratif dan kondisi dunia.

### 6C.4 Prinsip penyajian kepada pemain
- Tidak ada angka, bar, atau meter numerik untuk Affection, Trust, Intimacy, Jealousy, atau Fear yang ditampilkan kepada pemain.
- Pemain menyimpulkan keadaan hubungan melalui dialog, ekspresi, perilaku, perubahan cara NPC memperlakukan satu sama lain, dan event.
- Informasi yang diketahui pemain dapat tidak lengkap: karakter dapat menyembunyikan perasaan atau memiliki emosi yang saling bertentangan.

### 6C.5 Hal yang masih terbuka
- Skala internal, bobot, laju perubahan, decay, dan aturan interaksi antardimensi belum ditetapkan.
- Daftar pasangan romantis NPC-ke-NPC yang telah ditentukan canon belum dirinci dalam GDD ini; Master Canon tetap menjadi sumber kebenaran untuk pasangan dan lore.
- Batas perubahan hubungan NPC-ke-NPC akibat pemain (misalnya perubahan kedekatan, konflik, perpisahan, atau rekonsiliasi) belum ditetapkan secara terperinci.
- Syarat, metode, dan konsekuensi terbongkarnya hubungan rahasia belum ditetapkan.
- Bentuk dan durasi kesempatan memperbaiki hubungan setelah penolakan belum ditetapkan.
- Pemicu kecemburuan spesifik setiap karakter belum dirancang satu per satu.

### 6C.6 Konsekuensi desain
- Relationship System harus mampu menyimpan beberapa dimensi perasaan yang tidak selalu sejalan; satu karakter dapat tetap mencintai tetapi kehilangan kepercayaan, merasa takut, atau cemburu.
- Reaksi NPC harus mempertimbangkan sejarah perlakuan pemain, termasuk tindakan buruk yang sudah lama terjadi.
- Event NPC-ke-NPC dapat berkembang tanpa kehadiran pemain, tetapi perubahan tersebut harus memiliki pemicu naratif yang jelas.
- Karena pemain tidak melihat angka hubungan, narasi, ekspresi, dan konsistensi perilaku menjadi sarana utama untuk menyampaikan kondisi relasi.
- Hubungan rahasia dan kecemburuan perlu menghasilkan konsekuensi yang berbeda sesuai karakter, pasangan canon, saksi, dan konteks kejadian.


## 6D. NPC Life Simulation (keputusan Batch 4 — enam keputusan pertama)

### 6D.1 Jadwal dan aktivitas mandiri
- Setiap NPC memiliki jadwal harian lengkap dari pagi sampai malam.
- NPC menjalankan aktivitas tanpa kehadiran pemain, termasuk belajar, bekerja, berkencan, bersosialisasi, dan aktivitas lain yang sesuai dengan karakter serta situasinya.
- NPC dapat berpindah lokasi secara mandiri mengikuti jadwal dan kebutuhan mereka.
- Jadwal dan aktivitas NPC merupakan bagian dari simulasi dunia, bukan sekadar dekorasi untuk adegan pemain.

### 6D.2 Inisiatif interaksi NPC
- NPC dapat menginisiasi interaksi dengan pemain kapan pun situasinya memungkinkan.
- Inisiatif interaksi harus tetap mempertimbangkan jadwal, lokasi, hubungan, kepribadian, dan konteks kejadian.
- NPC dapat membuat janji dengan pemain, dan janji tersebut dapat dilanggar. Pelanggaran janji dapat menjadi bagian dari perkembangan hubungan atau event, sesuai konteks.

### 6D.3 Ketidakhadiran NPC
- Pemain dapat mengunjungi lokasi meskipun NPC yang dicari tidak berada di sana.
- Jika NPC tidak ada, lokasi tetap dapat dikunjungi; NPC tidak otomatis dipindahkan ke lokasi hanya agar pemain bisa bertemu dengannya.
- Cara mencari tahu lokasi NPC berikutnya atau keberadaan terakhirnya belum ditetapkan dalam keputusan yang sudah dijawab.

### 6D.4 Prinsip simulasi
- Dunia tetap menjalankan aktivitas NPC meskipun pemain tidak hadir.
- Jadwal lengkap, aktivitas otonom, perpindahan lokasi, interaksi yang diinisiasi NPC, dan janji yang dapat dilanggar harus menghasilkan dunia yang terasa hidup.
- Rincian prioritas jadwal, konflik jadwal, kebutuhan, batas simulasi, dan konsekuensi spesifik masih perlu dirancang.

### 6D.5 Keputusan Batch 4 yang belum masuk versi ini
Empat jawaban terakhir Batch 4 tetap dicatat dalam percakapan dan menjadi empat pertanyaan terjawab menuju pembaruan berikutnya:
7. NPC memiliki kehidupan sosial di luar heroine utama: teman, keluarga, klub, dan kenalan.
8. NPC dapat mengalami event ketika pemain tidak hadir; event tetap berlangsung dan dapat mengubah dunia.
9. Pemain mengetahui aktivitas NPC dengan mencari tahu sendiri melalui pertemuan atau penyelidikan.
10. Jadwal NPC dapat berubah mendadak karena kondisi, hubungan, cuaca, dan event.


## 6E. Time, Calendar & Daily Activities (keputusan Batch 5)

### 6E.1 Waktu harian
- Game menggunakan waktu harian 24 jam.
- Waktu terus berjalan dan interaksi/dialog menghabiskan waktu.
- Pemain dapat memilih kapan tidur; tidur bukan hanya tindakan yang tersedia pada malam hari.
- Aktivitas harian menggunakan gabungan waktu dan Action Point (AP). Rincian biaya AP dan hubungan AP dengan durasi waktu belum ditetapkan.

### 6E.2 Kalender
- Kalender mencakup tanggal dan musim, kalender akademik, hari libur, serta acara kota.
- Hari mengikuti siklus nyata Senin sampai Minggu.
- Kalender dan musim menjadi bagian dari simulasi kehidupan universitas dan kota.
- Detail tahun, bulan, tanggal mulai permainan, dan pemetaan kalender akademik belum ditetapkan.

### 6E.3 Cuaca dan musim
- Game memiliki cuaca dinamis.
- Game menggunakan empat musim Jepang.
- Rincian dampak cuaca terhadap aktivitas, perjalanan, lokasi, dan jadwal NPC belum ditetapkan.
- Rincian dampak musim terhadap event, pakaian, dan aktivitas NPC belum ditetapkan.

### 6E.4 Event dan rutinitas
- Event yang terlewat karena pemain terlambat tetap berlangsung dan dapat terlewat secara permanen.
- Terdapat aktivitas rutin mingguan, seperti kuliah, klub, pekerjaan, dan kegiatan sosial.
- Pemain bebas mengabaikan rutinitas tersebut; konsekuensi dari mengabaikannya bergantung pada sistem dan event terkait yang masih perlu dirancang.

### 6E.5 Hal yang masih terbuka
- Pembagian jam dan menit untuk aktivitas, serta apakah dialog menghabiskan waktu berdasarkan durasi tetap atau konteks.
- Biaya AP, pemulihan AP, batas AP, dan interaksi AP dengan waktu.
- Detail kalender akademik, tanggal mulai, tanggal ujian, masa libur, dan acara kota.
- Frekuensi serta dampak mekanis cuaca dan empat musim.
- Aturan event yang terlewat: apakah semua event permanen terlewat atau hanya event tertentu; keputusan yang ada menetapkan bahwa event yang terlambat dapat terlewat permanen.
- Aturan tidur, durasi tidur, bangun otomatis, dan pemulihan sumber daya.
- Konsekuensi mengabaikan kuliah, klub, pekerjaan, dan rutinitas sosial.

### 6E.6 Konsekuensi desain
- Sistem waktu harus menyelaraskan aktivitas pemain, jadwal NPC, event latar, kalender akademik, dan perubahan kondisi dunia.
- Karena dialog juga menghabiskan waktu, pemain harus mempertimbangkan durasi interaksi dan kemungkinan kehilangan kesempatan.
- Kombinasi waktu dan AP membatasi aktivitas melalui dua sumber daya yang berbeda; keduanya harus dirancang agar tidak terasa sebagai pembatas ganda yang tidak adil.
- Event yang dapat terlewat permanen memberi bobot pada ketepatan waktu dan pilihan prioritas pemain.


## 6F. Player Activities & Gameplay Loop (Batch 6 — enam keputusan pertama)

### 6F.1 Aktivitas pemain
Pemain memiliki pilihan aktivitas harian yang luas, antara lain:
- Mengikuti kuliah dan kegiatan akademik.
- Bekerja.
- Belajar dan mengembangkan kemampuan.
- Berkencan dan berinteraksi dengan karakter.
- Bersosialisasi dan mengikuti kegiatan sosial.
- Melakukan aktivitas lain yang tersedia sesuai lokasi, waktu, dan kondisi dunia.

### 6F.2 Sistem kuliah
- Kuliah merupakan aktivitas opsional dengan konsekuensi akademik.
- Pemain dapat memilih hadir atau tidak hadir melalui aktivitas kuliah.
- Rincian jadwal, penilaian, absensi, tugas, ujian, dan konsekuensi akademik belum ditetapkan.

### 6F.3 Sistem pekerjaan
- Pemain dapat mengakses pekerjaan part-time.
- Pekerjaan khusus berdasarkan karakter juga tersedia.
- Pekerjaan memiliki jadwal dan gaji.
- Daftar pekerjaan, syarat penerimaan, jam kerja, besaran gaji, dan konsekuensi absen belum ditetapkan.

### 6F.4 Pengembangan kemampuan
- Pemain dapat mengembangkan kemampuan pribadi seperti akademik, memasak, olahraga, sosial, dan kemampuan lain.
- Cara memperoleh, menaikkan, menguji, serta dampak kemampuan pada pilihan dan event belum ditetapkan.

### 6F.5 Ekonomi pemain
- Game menggunakan sistem ekonomi yang mencakup uang pribadi, pemasukan, pengeluaran, dan anggaran.
- Ekonomi mencakup pekerjaan, belanja, hadiah, serta biaya hidup.
- Rincian saldo awal, sumber pemasukan, harga barang, biaya rutin, dan batas anggaran belum ditetapkan.

### 6F.6 Kencan
- Pemain dapat mengajak karakter berkencan secara bebas selama kondisi memungkinkan.
- Ketersediaan kencan dipengaruhi konteks seperti waktu, lokasi, jadwal, hubungan, dan kesediaan karakter.
- Kencan tidak terbatas pada event khusus yang sudah ditentukan sebelumnya.

### 6F.7 Keputusan Batch 6 yang ditahan untuk pembaruan berikutnya
Empat jawaban terakhir Batch 6 sudah diterima dan tetap menjadi bagian dari keputusan desain, tetapi belum dimasukkan ke versi dokumen ini karena aturan pembaruan setiap enam jawaban:
7. Hadiah dapat diberikan kepada NPC; preferensi karakter berbeda dan hadiah dapat memengaruhi hubungan serta menghasilkan reaksi berbeda.
8. Aktivitas sosial mencakup kegiatan umum dan event karakter, seperti pesta, festival, klub, pertemuan, dan acara lainnya.
9. Reputasi sosial berbeda di setiap lingkungan sosial.
10. Pemain bebas menentukan aktivitas harian tanpa wajib mengikuti alur utama, tetapi Sistem NTR memberi tekanan melalui misi dan deadline.


## 6F.8 Aktivitas sosial, hadiah, reputasi, dan kebebasan (sisa keputusan Batch 6)

### Hadiah untuk NPC
- Pemain dapat memberikan hadiah kepada NPC.
- Setiap karakter memiliki preferensi hadiah yang berbeda.
- Hadiah dapat memengaruhi hubungan dan menghasilkan reaksi yang berbeda sesuai karakter serta konteks.

### Aktivitas sosial
- Tersedia aktivitas sosial umum dan event khusus karakter.
- Contoh aktivitas: pesta, festival, klub, pertemuan, dan acara lainnya.

### Reputasi sosial
- Reputasi pemain tidak hanya satu nilai global.
- Reputasi berbeda di setiap lingkungan sosial.
- Rincian lingkungan, cara reputasi berubah, dan konsekuensi reputasi masih perlu dirancang.

### Kebebasan aktivitas dan tekanan sistem
- Pemain bebas menentukan aktivitas harian dan tidak wajib mengikuti alur utama setiap saat.
- Sistem NTR tetap memberikan tekanan melalui misi dan deadline.
- Detail bagaimana tekanan misi berinteraksi dengan kebebasan sandbox masih perlu dirancang.

## 6G. NTR System & Mission Mechanics (dua keputusan pertama Batch 7)

### Persona dan komunikasi Sistem NTR
- Sistem NTR memiliki persona AI yang dapat diajak bicara oleh pemain.
- Kepribadian Sistem NTR telah ditetapkan dalam desain sebelumnya sebagai sarkastis, provokatif, dan suka mengejek.
- Bentuk antarmuka, frekuensi komunikasi, batas pengetahuan, dan cara persona menyampaikan informasi masih perlu dirancang.

### Struktur misi dinamis
- Misi sepenuhnya dinamis berdasarkan situasi.
- Misi dapat menyesuaikan keadaan dunia, tindakan pemain, karakter yang terlibat, dan perkembangan hubungan.
- Kategori misi, termasuk main, side, dan sudden mission, belum ditetapkan oleh keputusan Batch 7 ini; struktur misi yang pernah dicatat dalam Master Canon tetap menjadi referensi canon sampai ada koreksi eksplisit.


## 6G.1 NTR System & Mission Mechanics — keputusan Batch 7 lanjutan

### Deadline misi
- Deadline bergantung pada jenis dan tingkat kepentingan misi.
- Tidak semua misi harus memiliki deadline yang sama; urgensi ditentukan oleh konteks misi.

### Hadiah dan hukuman
- Hadiah misi bersifat adaptif berdasarkan misi dan tindakan pemain.
- Hukuman kegagalan bergantung pada jenis misi.
- Sistem tidak menggunakan satu bentuk hadiah atau hukuman universal untuk seluruh misi.

### Kewajiban misi
- Pemain tidak dapat menolak misi Sistem NTR.
- Konsekuensi jika pemain tidak memenuhi misi tetap mengikuti aturan hukuman berdasarkan jenis misi.

### Target dan evaluasi
- Target NTR bersifat tersembunyi dan baru diketahui saat evaluasi akhir.
- Evaluasi kontrak utama hanya dilakukan ketika kelulusan universitas.
- Detail kriteria evaluasi akhir, hasil penilaian, dan kaitannya dengan target tersembunyi belum ditetapkan.

### Informasi NPC
- Sistem NTR hanya memberikan informasi NPC secara terbatas.
- Batas informasi, cara membuka informasi tambahan, dan tingkat akurasinya belum ditetapkan.

### Persona Sistem NTR
- Sistem NTR memiliki persona AI yang dapat diajak bicara.
- Persona bersifat sarkastis, provokatif, dan suka mengejek pemain.
- Sistem NTR bukan sekadar menu quest; ia menjadi entitas naratif yang berinteraksi dengan pemain.

## 6H. Branching Narrative & Story Events (Batch 8)

### Struktur cerita
- Main story dan sandbox berjalan secara paralel.
- Pemain dapat menjalani aktivitas bebas di dunia simulasi sementara perkembangan cerita utama tetap berlangsung.
- Detail frekuensi, pemicu, dan struktur bab main story belum ditetapkan.

### Event naratif
- Event dapat muncul melalui kombinasi jadwal/tanggal tetap dan kondisi dinamis.
- Kondisi dinamis dapat mencakup hubungan, tindakan pemain, situasi NPC, serta keadaan dunia.
- Event manga asli sebagian besar tetap berlangsung sampai terjadi penyimpangan besar.
- Event yang terlewat atau gagal memiliki konsekuensi sesuai jenis event; tidak semua event harus diperlakukan dengan aturan yang sama.

### Plot armor Koita
- Koita selalu mendapatkan kesempatan romantis melalui kebetulan sebagai bagian dari plot armor.
- Plot armor memberikan peluang dan situasi yang menguntungkan Koita, bukan jaminan bahwa semua heroine akan memilihnya atau bahwa setiap kesempatan pasti berhasil.
- Rincian bentuk kebetulan, batas kewajaran, dan interaksi plot armor dengan perubahan dunia masih perlu dirancang.

### Memori pilihan dan konsekuensi
- NPC mengingat pilihan pemain dalam event sebelumnya secara konsisten sepanjang permainan.
- Pilihan dialog memiliki banyak opsi dan konsekuensinya tersembunyi.
- Satu event dapat memiliki banyak outcome.
- Pemain dapat memicu konflik baru yang tidak terdapat dalam manga asli apabila tindakan pemain menghasilkan konsekuensi yang relevan.

### Event gagal atau terlewat
- Penanganan event gagal atau terlewat bergantung pada jenis event.
- Sebagian event dapat hilang permanen, sementara event lain dapat memiliki penanganan berbeda sesuai sifat dan konteksnya.
- Aturan spesifik tiap kategori event belum ditetapkan.

### Ending keseluruhan
- Game memiliki banyak ending dan tidak memiliki satu True Ending.
- Ending tidak dibatasi pada satu hasil kanonis yang wajib dicapai.
- Hubungan antara ending keseluruhan, evaluasi kontrak saat kelulusan, dan hasil target tersembunyi masih perlu dirancang lebih lanjut.

### Pilihan dan konsekuensi naratif
- Sistem pilihan dialog menampilkan banyak pilihan dengan konsekuensi tersembunyi.
- NPC membawa ingatan atas pilihan pemain dari event sebelumnya; respons dan hubungan di kemudian hari harus konsisten dengan riwayat tersebut.
- Event bercabang harus dapat menghasilkan outcome berbeda berdasarkan kondisi yang relevan.
- Dunia manga asli tetap menjadi titik awal, tetapi tindakan pemain dapat memunculkan konflik dan perkembangan baru.


## 6I. Character Routes & Romance Progression (Batch 9 — enam keputusan pertama)

### 6I.1 Personal storyline
- Setiap heroine memiliki personal storyline tersendiri dan cerita yang panjang.
- Detail panjang, bab, struktur, dan variasi personal storyline dirancang pada tahap desain karakter dan narasi lanjutan.

### 6I.2 Pembukaan character route
- Character route dibuka melalui kombinasi perkembangan hubungan, event tertentu, dan kondisi tersembunyi.
- Tidak ada satu syarat tunggal yang berlaku otomatis untuk semua heroine.
- Rincian syarat masing-masing heroine harus mengikuti karakter, canon, dan situasi cerita.

### 6I.3 Benturan antar-route
- Character route dapat saling bertabrakan, tetapi hal tersebut bergantung pada karakter dan situasi.
- Konflik route tidak harus selalu terjadi; desain tiap karakter menentukan apakah perkembangan hubungan dapat berjalan berdampingan atau saling menghalangi.

### 6I.4 Kehendak heroine dan cerita manga asli
- Heroine dapat memilih Koita tanpa campur tangan pemain melalui event manga asli.
- Keputusan ini berlaku dalam konteks event manga asli; mekanisme pilihan di luar event tersebut belum ditetapkan oleh jawaban ini.
- Otonomi heroine dan perkembangan manga asli harus tetap diperhitungkan dalam simulasi dunia.

### 6I.5 Intervensi pemain terhadap hubungan Koita
- Pemain dapat merusak hubungan Koita dengan heroine melalui tindakan dan manipulasi.
- Dampak tindakan pemain harus mengikuti konteks, karakter, hubungan, dan konsekuensi naratif yang telah dibangun.

### 6I.6 Ending romantis pemain
- Setiap heroine memiliki kemungkinan ending romantis dengan pemain.
- Ketersediaan dan syarat ending tetap bergantung pada perkembangan cerita, protagonis, dan keputusan pemain; rincian rute spesifik belum ditetapkan.

### 6I.7 Keputusan Batch 9 yang menunggu giliran integrasi
Empat jawaban terakhir Batch 9 telah diterima dan menjadi keputusan desain, tetapi ditahan untuk pembaruan berikutnya sesuai aturan integrasi setiap enam jawaban:
7. NPC tidak membentuk pasangan romantis baru; hubungan romantis NPC-ke-NPC mengikuti pasangan yang ditetapkan canon.
8. Hubungan romantis yang gagal dapat berakhir berbeda sesuai karakter dan penyebab kegagalan.
9. Event khusus kedekatan tersedia, dengan sebagian besar event bersifat dinamis.
10. Pemain dapat menyelesaikan permainan tanpa hubungan romantis; hal tersebut dapat memengaruhi evaluasi akhir.


## 6I.1 Character Routes & Romance Progression — keputusan Batch 9 lanjutan

### Hubungan NPC-ke-NPC
- Hubungan romantis NPC-ke-NPC mengikuti pasangan yang sudah ditetapkan dalam canon.
- Sistem tidak secara bebas membentuk pasangan romantis baru di luar pasangan canon.
- Ketentuan ini tidak menghapus kemungkinan perubahan kualitas, konflik, atau perkembangan hubungan yang sudah ada.

### Kegagalan hubungan romantis
- Hubungan romantis yang gagal dapat menghasilkan konsekuensi berbeda sesuai karakter dan penyebab kegagalan.
- Hasilnya tidak harus selalu persahabatan atau permusuhan; bentuk akhirnya ditentukan oleh konteks cerita.

### Event kedekatan
- Tersedia event khusus yang dipicu oleh kedekatan.
- Sebagian besar event kedekatan bersifat dinamis, bukan hanya event tetap yang dijadwalkan.

### Menyelesaikan permainan tanpa pasangan
- Pemain dapat menyelesaikan permainan tanpa menjalin hubungan romantis.
- Tidak memiliki pasangan dapat memengaruhi evaluasi akhir kontrak; bentuk dan besaran dampaknya belum ditetapkan.

## 6J. Character Behavior & Personality Simulation (Batch 10 — dua keputusan pertama)

### Kepribadian dan perkembangan karakter
- Setiap karakter memiliki kepribadian dasar yang konsisten berdasarkan profil dan pengalaman hidup.
- Kepribadian dapat berkembang karena pengalaman, tetapi tidak berubah secara bebas tanpa sebab.
- Perubahan kepribadian akibat pengalaman positif, negatif, atau traumatis harus mengikuti karakter dan konteksnya.
- Rincian batas perubahan, durasi, dan pemicu perkembangan kepribadian belum ditetapkan.

### Perasaan tersembunyi dan kebohongan
- NPC dapat menyembunyikan perasaan sebenarnya, termasuk berbohong kepada pemain.
- Perilaku yang terlihat tidak selalu mencerminkan perasaan atau niat sebenarnya.
- Kemampuan dan kecenderungan menyembunyikan perasaan dapat berbeda menurut karakter dan situasi.

### Keputusan Batch 10 yang menunggu integrasi
Delapan jawaban terakhir Batch 10 telah diterima dan dicatat untuk pembaruan berikutnya:
3. NPC dapat mengambil keputusan penting tanpa pemain, termasuk keputusan yang mengubah hidup mereka.
4. NPC dapat berbohong satu sama lain berdasarkan kepentingan dan kepribadian.
5. Respons NPC terhadap rumor bergantung pada karakter dan kedekatan dengan sumber.
6. NPC memiliki tujuan pribadi yang bergantung pada karakter.
7. NPC dapat berubah karena pengalaman, tetapi perkembangan ini terjadi melalui character route.
8. Opini NPC tentang pemain berdasarkan informasi yang dilihat atau didengar bergantung pada kredibilitas informasi dan hubungan.
9. NPC dapat menyimpan rahasia pribadi, keluarga, dan hubungan satu sama lain.
10. NPC dapat menyelesaikan konflik sendiri tanpa pemain, bergantung pada konflik dan karakter yang terlibat.


## 6J.1 Character Behavior & Personality Simulation — keputusan Batch 10 lanjutan

### Keputusan mandiri dan kebohongan antar-NPC
- NPC dapat mengambil keputusan penting tanpa kehadiran atau campur tangan pemain, termasuk keputusan yang mengubah hidup mereka.
- NPC dapat berbohong satu sama lain berdasarkan kepentingan dan kepribadian masing-masing.

### Rumor dan opini NPC
- Respons NPC terhadap rumor bergantung pada karakter dan kedekatan mereka dengan sumber rumor.
- Opini NPC terhadap pemain dapat terbentuk dari informasi yang mereka lihat atau dengar secara langsung maupun tidak langsung.
- Penilaian terhadap informasi tersebut bergantung pada kredibilitas informasi dan hubungan NPC dengan pihak terkait.

### Tujuan pribadi dan perkembangan karakter
- NPC memiliki tujuan pribadi, tetapi tujuan dan prioritasnya bergantung pada karakter masing-masing.
- Perubahan kepribadian melalui pengalaman terjadi dalam konteks character route.
- Kepribadian dasar tetap menjadi fondasi; perkembangan tidak berlangsung secara bebas tanpa konteks cerita.

### Rahasia dan konflik antar-NPC
- NPC dapat menyimpan rahasia satu sama lain, termasuk rahasia pribadi, keluarga, dan hubungan.
- NPC dapat menyelesaikan konflik tanpa campur tangan pemain.
- Apakah konflik selesai sendiri, memburuk, atau membutuhkan pihak lain bergantung pada jenis konflik dan karakter yang terlibat.

## 6K. Force / Criminal Route & Consequence Systems

### 6K.1 Force / Criminal Route
- Pemain dapat memilih jalur antagonis yang menggunakan tindakan kriminal langsung dan pemaksaan, bukan hanya manipulasi sosial atau psikologis.
- Force / Criminal Route merupakan pilihan gameplay yang memiliki konsekuensi serius; tindakan kriminal tidak diperlakukan sebagai jalan pintas tanpa risiko.
- NPC tetap memiliki kehendak, kemampuan mengambil tindakan, dan kemungkinan mencari pertolongan.
- Detail tindakan yang tersedia, pemicu route, serta batas konten naratif belum ditetapkan. Sistem akan menggambarkan konsekuensi secara naratif dan tidak menjadi panduan operasional melakukan kejahatan.

### 6K.2 Sistem hukum dan investigasi
- Tingkat investigasi bergantung pada tingkat keparahan kasus.
- Korban dapat melapor, tetapi keputusan untuk melapor bergantung pada karakter, kondisi psikologis, dan bukti.
- Saksi dapat mengingat atau melaporkan kejadian; respons mereka bergantung pada situasi.
- Bukti kriminal dapat ditemukan belakangan atau tidak, bergantung pada jenis bukti dan jalannya investigasi.
- Konsekuensi hukum melalui jalur laporan korban hanya berjalan jika korban melapor. Jawaban ini tidak menetapkan apakah jalur independen lain dapat memulai proses hukum tanpa laporan korban.
- Tidak ada sistem reputasi kriminal khusus yang terpisah. Reputasi sosial umum dan respons NPC tetap dapat berubah sesuai informasi yang diketahui.
- Konsekuensi akademik, seperti skorsing atau pengusiran, bergantung pada tingkat kasus.

### 6K.3 Konsekuensi sosial dan hubungan
- NPC dapat menjauh atau memutus hubungan setelah mengetahui kejahatan; reaksinya bergantung pada hubungan dan karakter.
- Force / Criminal Route dapat berakhir tanpa hukuman penjara.
- Tidak dipenjara bukan berarti bebas konsekuensi: ending tetap dapat berisi kehancuran sosial dan psikologis.
- Sistem harus membedakan konsekuensi hukum, sosial, akademik, dan psikologis; satu jalur tidak otomatis menentukan hasil jalur lainnya.

### 6K.4 Hidden Crime dan Broken Heroine Ending
- Kejahatan yang berhasil disembunyikan tetap dapat memicu Broken Heroine Ending.
- Broken Heroine Ending dapat terjadi tanpa kejahatan terbongkar.
- Kerusakan psikologis heroine berdiri terpisah dari sistem hukum dan tidak mensyaratkan pengungkapan kejahatan.
- Dengan demikian, pemain dapat menghindari penjara atau pengungkapan publik, tetapi tetap menyebabkan kerusakan psikologis yang berujung pada ending heroine rusak.
- Pemicu, ambang kondisi, tahapan kerusakan, serta ending spesifik tiap heroine belum dirinci.

### 6K.5 Batas dan hal yang masih terbuka
- Kriteria tingkat keparahan kasus dan intensitas investigasi belum ditetapkan.
- Mekanisme laporan korban, keputusan saksi, dan kemungkinan investigasi tanpa laporan korban masih perlu diperjelas.
- Kategori bukti, cara bukti ditemukan, dan jangka waktu penemuan belum dirinci.
- Konsekuensi akademik dan sosial spesifik masih bergantung pada jenis kasus dan perlu dirancang.
- Tidak ada criminal reputation meter khusus yang disepakati.
- Ending tanpa penjara tetap dapat memiliki konsekuensi sosial/psikologis.
- Broken Heroine Ending tidak bergantung pada terbongkarnya kejahatan.



## 6L. UI, Player Information & Interface (Batch 12 — enam keputusan pertama)

### 6L.1 Tampilan dialog utama
- Presentasi utama menggunakan format Classic Visual Novel 2D.
- Background lokasi, sprite karakter, nama karakter, kotak dialog, dan elemen pilihan menjadi bagian dari tampilan VN.
- UI dapat disembunyikan agar pemain dapat menikmati ilustrasi/background tanpa elemen antarmuka yang mengganggu.
- Rincian tombol dan perilaku hide/show UI belum ditetapkan.

### 6L.2 Pilihan dialog
- Pilihan dialog ditampilkan secara kontekstual sesuai jenis event.
- Tidak semua pilihan harus selalu berada pada posisi atau format visual yang sama.
- Pilihan tetap menggunakan kontrol tombol, sesuai keputusan dasar gameplay.

### 6L.3 Menu status pemain
- Pemain memiliki menu status karakter.
- Menu status menampilkan kondisi pemain, skill, uang, dan informasi pribadi.
- Rincian kategori status, atribut yang terlihat, serta apakah informasi tertentu bersifat tersembunyi belum ditetapkan.

### 6L.4 Informasi hubungan
- Informasi hubungan ditampilkan melalui profil karakter dan deskripsi hubungan.
- Informasi hubungan juga tersedia melalui jurnal interaksi.
- Sesuai keputusan Relationship System sebelumnya, parameter hubungan tidak ditampilkan sebagai angka atau meter numerik kepada pemain.
- Profil dan jurnal menyampaikan keadaan relasi melalui deskripsi dan informasi naratif.

### 6L.5 Jurnal dan log cerita
- Pemain memiliki jurnal/log yang mencatat event dan informasi yang sudah diketahui.
- Jurnal juga dapat mencatat rumor, petunjuk, dan rahasia yang telah ditemukan pemain.
- Jurnal tidak otomatis mengungkap informasi yang belum diketahui karakter pemain.
- Struktur kategori, filter, dan cara memperbarui entri belum ditetapkan.

### 6L.6 Peta distrik
- Peta menggunakan ilustrasi visual dan menu detail lokasi.
- Navigasi tetap mengikuti keputusan sebelumnya: pemain memilih distrik terlebih dahulu, lalu memilih lokasi di dalam distrik.
- Peta mencakup universitas dan lokasi kota seperti rumah, apartemen, pusat perbelanjaan, restoran, serta tempat lain.
- Detail tampilan peta, ikon, dan informasi pada menu lokasi belum ditetapkan.

### 6L.7 Keputusan Batch 12 yang menunggu integrasi
Empat jawaban terakhir Batch 12 telah diterima dan akan dimasukkan pada pembaruan berikutnya sesuai aturan enam jawaban per pembaruan:
7. Jadwal NPC tidak ditampilkan; pemain harus mencari tahu sendiri.
8. Pemain memiliki inventory untuk hadiah, barang, dokumen, dan item.
9. Notifikasi Sistem NTR menggunakan kotak notifikasi khusus sekaligus dialog persona AI.
10. Sistem penyimpanan mencakup manual save, autosave, dan beberapa slot.


## 6L.1 UI, Player Information & Interface — keputusan Batch 12 lanjutan

### Jadwal NPC
- Jadwal NPC tidak ditampilkan secara langsung kepada pemain.
- Pemain harus mencari tahu sendiri aktivitas atau keberadaan NPC melalui pertemuan, observasi, informasi, dan interaksi di dunia.

### Inventory
- Pemain memiliki inventory untuk menyimpan hadiah, barang, dokumen, dan item.
- Kategori item, kapasitas, pengelompokan, dan aturan penggunaan belum ditetapkan.

### Notifikasi Sistem NTR
- Sistem NTR menggunakan kotak notifikasi khusus dan dialog persona AI.
- Frekuensi, prioritas, dan aturan kapan notifikasi atau dialog muncul belum ditetapkan.

### Save System
- Sistem penyimpanan menyediakan manual save, autosave, dan beberapa slot.
- Jumlah slot, frekuensi autosave, serta aturan penyimpanan event/branch state belum ditetapkan.

## 6M. Visual Presentation & Audio (Batch 13 — delapan keputusan pertama)

### Sprite karakter
- Sprite karakter dapat menggunakan full body maupun half body, bergantung pada adegan.
- Sprite memiliki banyak variasi ekspresi dan pose yang mengikuti emosi serta konteks adegan.
- Pakaian karakter dapat berbeda berdasarkan musim, kegiatan, dan event.

### CG dan ilustrasi khusus
- Game memiliki CG khusus untuk event penting, momen spesial, CG rahasia, dan event alternatif.
- Syarat membuka CG dan pengelompokan galeri belum ditetapkan.

### Transisi adegan
- Transisi visual bergantung pada jenis adegan.
- Rincian jenis transisi, durasi, dan adegan yang menggunakan transisi khusus belum ditetapkan.

### Musik latar
- Musik latar menggunakan kombinasi konteks lokasi, karakter, dan suasana.
- Daftar musik dan aturan pergantian BGM belum ditetapkan.

### Efek suara
- Efek suara bersifat dinamis berdasarkan situasi.
- Efek suara mendukung aktivitas, lingkungan, dan perubahan kondisi adegan sesuai konteks.

### Voice acting
- Game menggunakan full voice acting.
- Cakupan bahasa, pengisi suara, variasi dialog, dan pengaturan voice belum ditetapkan.

### Keputusan Batch 13 yang menunggu integrasi
Dua jawaban terakhir Batch 13 telah diterima dan dicatat untuk pembaruan berikutnya:
9. Dialog memiliki fitur autoplay dan skip.
10. Pengaturan lengkap mencakup kecepatan dialog, volume terpisah, dan preferensi visual.


## 6M.1 Visual Presentation & Audio — keputusan Batch 13 lanjutan

### Dialog playback
- Dialog menyediakan fitur autoplay dan skip.
- Detail perilaku skip, batas skip untuk dialog belum terbaca, serta opsi konfirmasi belum ditetapkan.

### Pengaturan tampilan dan audio
- Pengaturan game mencakup kecepatan dialog, volume audio terpisah, dan preferensi visual.
- Rincian kategori volume, opsi aksesibilitas visual, dan pengaturan tambahan belum ditetapkan.

## 6N. Game Structure & Progression (Batch 14)

### 6N.1 Durasi dan struktur waktu cerita
- Durasi cerita utama berlangsung selama tiga tahun sampai kelulusan universitas.
- Struktur chapter menggunakan format naratif dengan kalender yang berjalan sendiri.
- Timeskip tersedia ketika periode tertentu tidak perlu dimainkan secara detail.
- Rincian pemicu timeskip, durasi yang dapat dilewati, dan cara menjaga konsistensi jadwal NPC selama timeskip belum ditetapkan.

### 6N.2 Perkembangan cerita utama
- Main story menggunakan milestone utama, dengan perkembangan dinamis di antara milestone tersebut.
- Struktur milestone, urutan, dan kondisi pencapaiannya masih perlu dirancang.
- Pemain dapat mengubah hasil akhir manga asli sepenuhnya melalui tindakan dan penyimpangan cerita.
- Perubahan hasil manga harus tetap mengikuti sebab-akibat dunia dan respons NPC.

### 6N.3 New Game Plus
- Game memiliki fitur New Game Plus.
- New Game Plus dapat membuka informasi tambahan.
- Detail bonus, informasi yang dibuka, serta apakah progres atau item dibawa ke playthrough baru belum ditetapkan.

### 6N.4 Galeri dan replay
- Game memiliki galeri CG dan fitur replay event.
- Rincian kategori galeri, syarat unlock, dan batas event yang dapat diputar ulang belum ditetapkan.

### 6N.5 Kesulitan dan achievement
- Tingkat kesulitan bersifat adaptif berdasarkan tindakan pemain dan situasi.
- Game memiliki achievement, termasuk achievement rahasia.
- Rincian parameter adaptasi kesulitan, daftar achievement, dan syarat unlock belum ditetapkan.

### 6N.6 Rekap akhir playthrough
- Setelah playthrough, game menampilkan rekap lengkap.
- Rekap mencakup hubungan, event, ending, keputusan, konsekuensi, dan perkembangan dunia.
- Detail format rekap, statistik yang ditampilkan, dan keterkaitannya dengan New Game Plus belum ditetapkan.


## 6O. World Simulation & City Activities (Batch 15 — enam keputusan pertama)

### 6O.1 Operasional kota
- Kota memiliki siklus aktivitas harian.
- Toko, restoran, fasilitas, dan tempat hiburan memiliki jam operasional.
- Rincian jam operasional setiap kategori tempat dan pengecualiannya belum ditetapkan.

### 6O.2 Mobilitas NPC
- NPC dapat ditemukan di luar lokasi yang biasa mereka kunjungi.
- Mereka dapat bepergian dan mengunjungi tempat lain sesuai jadwal, kebutuhan, hubungan, dan situasi.
- Detail frekuensi perjalanan dan aturan pemilihan lokasi belum ditetapkan.

### 6O.3 Transportasi kota
- Transportasi menggunakan kombinasi berjalan kaki, transportasi umum, dan kendaraan pribadi.
- Ketersediaan moda transportasi, biaya, waktu perjalanan, serta akses karakter terhadap kendaraan pribadi belum ditetapkan.

### 6O.4 Event publik
- Kota memiliki event publik, termasuk festival, konser, pameran, dan acara musiman.
- Event publik menjadi bagian dari kalender dan simulasi kehidupan kota.
- Rincian jadwal, skala, dan dampak event belum ditetapkan.

### 6O.5 Fasilitas kota
- Sebagian fasilitas kota memiliki fungsi gameplay dan dapat digunakan untuk aktivitas.
- Sebagian fasilitas lain berfungsi sebagai latar cerita.
- Daftar fasilitas interaktif dan fungsi masing-masing belum ditetapkan.

### 6O.6 Kunjungan ke rumah atau apartemen
- NPC dapat mengunjungi rumah atau apartemen karakter lain sesuai karakter dan izin/keadaan.
- Kunjungan tidak otomatis tersedia untuk semua NPC atau semua situasi.
- Aturan undangan, izin masuk, dan kondisi kunjungan belum dirinci.

### 6O.7 Keputusan Batch 15 yang menunggu integrasi
Empat jawaban terakhir Batch 15 telah diterima dan dicatat untuk pembaruan berikutnya sesuai aturan enam jawaban per pembaruan:
7. Sistem berita dan informasi kota mencakup berita lokal, rumor, serta kejadian yang memengaruhi NPC.
8. Kondisi kota berubah menurut waktu dan musim; visual serta aktivitas gameplay ikut berubah.
9. Pemain tidak memiliki sistem menyewa atau membeli properti sendiri; tempat tinggal sudah ditentukan.
10. NPC dapat mengalami kejadian kota tanpa pemain, tetapi hanya kejadian yang relevan dengan NPC.


## 6O.1 World Simulation & City Activities — keputusan Batch 15 lanjutan

### Berita dan informasi kota
- Kota memiliki sistem berita dan informasi yang mencakup berita lokal, rumor, serta kejadian yang memengaruhi NPC.
- Informasi yang tersedia bagi pemain tetap mengikuti prinsip pengetahuan karakter: pemain perlu menemukan atau menerima informasi tersebut di dunia.

### Perubahan kota berdasarkan waktu dan musim
- Kondisi kota berubah mengikuti waktu dan musim.
- Perubahan mencakup aspek visual dan aktivitas gameplay, bukan hanya dekorasi.
- Rincian perubahan spesifik untuk tiap musim, distrik, dan jenis fasilitas belum ditetapkan.

### Tempat tinggal pemain
- Tempat tinggal pemain sudah ditentukan oleh identitas/rute karakter.
- Pemain tidak memiliki sistem untuk menyewa atau membeli properti sendiri.

### Kejadian mandiri NPC di kota
- NPC dapat mengalami kejadian di kota tanpa kehadiran pemain.
- Kejadian mandiri yang disimulasikan dibatasi pada kejadian yang relevan dengan NPC terkait.
- Relevansi kejadian ditentukan oleh karakter, jadwal, tujuan, hubungan, dan konteks dunia; aturan detailnya belum ditetapkan.

## 6P. Social Network & Information System (Batch 16 — delapan keputusan pertama)

### 6P.1 Media sosial dan ponsel
- Dunia game memiliki media sosial fiktif dan grup chat.
- Pemain memiliki ponsel sebagai menu komunikasi dan informasi.
- Detail aplikasi, tampilan, fungsi, serta batas akses belum ditetapkan.

### 6P.2 Komunikasi NPC
- Komunikasi NPC bergantung pada hubungan dan situasi.
- Bentuk komunikasi dapat mencakup chat, telepon, dan pertemuan langsung.
- Tidak semua karakter atau situasi harus menggunakan seluruh kanal komunikasi.

### 6P.3 Penyebaran rumor dan informasi
- Rumor dapat menyebar secara otomatis melalui interaksi dan jaringan sosial NPC, serta dapat disebarkan oleh pemain.
- Informasi yang beredar dapat salah atau dimanipulasi; tingkat keandalan bergantung pada sumber dan penyebarnya.
- Sistem harus membedakan fakta, rumor, kesalahpahaman, dan informasi yang sengaja dimanipulasi.

### 6P.4 Aktivitas media sosial pemain dan NPC
- Pemain dapat membuat unggahan di media sosial; unggahan dapat memengaruhi opini NPC.
- NPC memiliki akun dan aktivitas media sosial sendiri serta dapat mengunggah dan berinteraksi secara mandiri.
- Aktivitas digital NPC menjadi bagian dari simulasi kehidupan sosial.

### 6P.5 Pesan pribadi dan event
- Pesan pribadi dapat memicu event, termasuk pesan mendadak dan undangan.
- Rincian pemicu, prioritas, dan masa berlaku pesan/event belum ditetapkan.

### 6P.6 Kontrol kontak
- Pemain dapat memblokir atau mengabaikan kontak NPC.
- Tindakan tersebut dapat memiliki konsekuensi sosial.
- Rincian konsekuensi per karakter dan per kanal komunikasi belum ditetapkan.

### 6P.7 Informasi digital sebagai bukti dan pemicu konflik
- Pesan, unggahan, dan foto dapat memengaruhi cerita serta menjadi bukti atau pemicu konflik.
- Dampaknya bergantung pada isi dan konteks informasi.
- Aturan autentikasi, kepemilikan, penyebaran, dan interpretasi bukti digital belum ditetapkan.

### 6P.8 Keputusan Batch 16 yang menunggu integrasi
Dua jawaban terakhir Batch 16 telah diterima dan dicatat untuk pembaruan berikutnya:
9. Pemain dapat memblokir atau mengabaikan kontak NPC dengan konsekuensi sosial tertentu.
10. Informasi digital seperti pesan, unggahan, dan foto dapat menjadi bukti atau memicu konflik sesuai isi dan konteks.


## 6Q. Character Creation & Player Identity (Batch 17 — enam keputusan pertama)

### 6Q.1 Pemilihan rute dan identitas host
- Pemain memilih gender/rute sebelum cerita dimulai: Male Route atau Female Route.
- Identitas protagonis mengikuti host canon:
  - **Male Route:** Kisaragi Yutaka.
  - **Female Route:** Amamiya Chiasa.
- Nama canon host tidak dapat diganti oleh pemain.
- Prolog dan perspektif awal Male Route dan Female Route berbeda.
- Detail perbedaan prolog dan perspektif tiap rute masih perlu dirancang.

### 6Q.2 Kepribadian dan gaya interaksi pemain
- Pemain bebas menentukan kepribadian protagonis melalui pilihan dan tindakan.
- Pemain dapat menentukan gaya interaksi, termasuk ramah, dingin, genit, agresif, manipulatif, dan gaya lain yang didukung pilihan.
- Kepribadian host tidak mengunci pemain pada satu pola perilaku; identitas sosial dan latar host tetap menjadi fondasi cerita.
- Rincian bagaimana pilihan membentuk konsistensi kepribadian dan bagaimana NPC menilainya belum ditetapkan.

### 6Q.3 Latar belakang keluarga
- Fondasi latar belakang keluarga host tetap canon.
- Hubungan pemain dengan anggota keluarga dapat berubah melalui tindakan, pilihan, dan perkembangan cerita.
- Detail batas perubahan hubungan keluarga serta event yang dapat memicunya belum ditetapkan.

### 6Q.4 Keputusan Batch 17 yang menunggu integrasi
Empat jawaban terakhir Batch 17 telah diterima dan dicatat untuk pembaruan berikutnya sesuai aturan enam jawaban per pembaruan:
7. Profil pribadi yang diketahui NPC bergantung pada rute dan karakter NPC.
8. Penampilan host mengikuti canon, tetapi pemain dapat mengubah pakaian dan aksesori.
9. Male Route dan Female Route memiliki prolog serta perspektif awal berbeda.
10. Masing-masing host memiliki kondisi hubungan awal canon yang berbeda dengan heroine.


## 6Q.1 Character Creation & Player Identity — keputusan Batch 17 lanjutan

### Profil yang diketahui NPC
- Informasi profil pribadi host yang diketahui NPC bergantung pada rute dan karakter NPC.
- Pengetahuan setiap NPC tidak otomatis seragam; apa yang diketahui seseorang mengikuti hubungan, pengalaman, dan konteksnya.
- Detail data profil apa saja yang diketahui masing-masing NPC belum dirinci.

### Penampilan host
- Penampilan dasar host mengikuti desain canon.
- Pemain dapat mengubah pakaian dan aksesori protagonis.
- Perubahan pakaian/aksesori tidak mengubah identitas atau penampilan dasar canon host.

### Perbedaan rute
- Male Route dan Female Route memiliki prolog serta perspektif awal yang berbeda.
- Kondisi hubungan awal masing-masing host dengan heroine mengikuti canon dan dapat berbeda antar-rute.
- Rincian adegan prolog, perbedaan perspektif, dan status awal tiap hubungan perlu dirancang pada dokumen narasi/karakter.

## 6R. Player Knowledge & Information Boundaries (Batch 18 — enam keputusan pertama)

### 6R.1 Pengetahuan tentang manga asli
- Pemain mengetahui garis besar cerita manga asli dan beberapa spoiler, bukan seluruh detail.
- Pengetahuan tersebut dapat menjadi tidak akurat akibat penyimpangan timeline dan perubahan yang dibuat pemain.
- Informasi manga menjadi bekal awal, bukan jaminan pemain mengetahui masa depan secara pasti.

### 6R.2 Pengetahuan tentang heroine dan NPC
- Pemain mengetahui perasaan awal heroine terhadap Koita sejauh informasi tersebut tercakup dalam manga yang diketahui pemain.
- Rahasia keluarga dan masa lalu NPC tidak otomatis diketahui pemain; informasi tersebut harus ditemukan melalui gameplay.
- Pemain dapat salah memahami petunjuk karena informasi dapat ambigu atau menyesatkan.

### 6R.3 Jurnal dan tingkat kepastian informasi
- Jurnal mencatat informasi yang sudah diketahui, tetapi tidak memberi label tingkat kepastian.
- Fakta, dugaan, dan rumor tidak dibedakan melalui penanda kepastian khusus dalam jurnal.
- Pemain perlu menilai sendiri keandalan informasi berdasarkan sumber dan konteks.

### 6R.4 Keputusan Batch 18 yang menunggu integrasi
Empat jawaban terakhir Batch 18 telah diterima dan dicatat untuk pembaruan berikutnya sesuai aturan enam jawaban per pembaruan:
7. NPC dapat menyadari pemain mengetahui sesuatu yang seharusnya tidak diketahui; kemungkinan kecurigaan bergantung karakter dan situasi.
8. Pemain dapat menyebarkan informasi yang belum terverifikasi dengan risiko rumor dan konsekuensi.
9. Informasi yang telah diketahui dapat berubah atau terbukti salah setelah pemain menemukan fakta baru.
10. Pengetahuan awal Male Route dan Female Route sama.


## 6S. Events, Scheduling & Quest Discovery (Batch 19 — enam keputusan pertama)

### 6S.1 Penemuan event
- Pemain menemukan event melalui observasi, interaksi, jadwal, dan informasi yang diperoleh di dunia.
- Event tidak seluruhnya diumumkan melalui notifikasi; pemain perlu aktif memperhatikan dunia dan aktivitas NPC.
- Rincian petunjuk, indikator, serta cara tiap kategori event ditemukan belum ditetapkan.

### 6S.2 Sumber quest
- Semua quest berasal dari Sistem NTR.
- NPC tidak memberikan quest secara mandiri kepada pemain.
- Percakapan biasa dapat menjadi konteks atau pemicu perkembangan cerita, tetapi bukan sumber quest independen di luar Sistem NTR.
- Hubungan antara quest Sistem NTR dan event dunia yang ditemukan pemain masih perlu dirancang.

### 6S.3 Kategori dan kepentingan quest
- Quest memiliki kategori atau tingkat kepentingan, tetapi kategorinya tidak ditampilkan kepada pemain.
- Dasar kategorisasi, dampak, serta konsekuensi masing-masing kategori belum ditetapkan.

### 6S.4 Quest dari percakapan
- Kemungkinan munculnya quest atau perkembangan terkait percakapan bergantung pada hubungan dan konteks.
- Karena semua quest berasal dari Sistem NTR, percakapan NPC tidak secara langsung membuat quest independen; percakapan dapat menjadi kondisi atau pemicu bagi Sistem NTR.

### 6S.5 Event rahasia
- Pemain dapat menemukan event rahasia melalui eksplorasi dan kondisi tersembunyi.
- Rincian petunjuk, syarat, dan jenis event rahasia belum ditetapkan.

### 6S.6 Solusi dan kegagalan quest
- Quest dapat memiliki beberapa solusi.
- Pendekatan yang berbeda dapat menghasilkan konsekuensi yang berbeda.
- Quest dapat gagal akibat tindakan pemain, termasuk kegagalan tidak langsung.
- Rincian kategori kegagalan, konsekuensi, dan apakah kegagalan dapat dipulihkan belum ditetapkan.

### 6S.7 Keputusan Batch 19 yang menunggu integrasi
Empat jawaban terakhir Batch 19 telah diterima dan dicatat untuk pembaruan berikutnya sesuai aturan enam jawaban per pembaruan:
7. Quest dapat gagal akibat tindakan pemain, termasuk secara tidak langsung.
8. NPC tidak memberikan quest secara mandiri; quest berasal dari Sistem NTR.
9. Pemain dapat menunda quest selama belum melewati deadline.
10. Quest yang tidak relevan dapat berubah, kedaluwarsa, atau digantikan event lain.


## ADDENDUM VISUAL — 10 November 2026 (keputusan terbaru, prioritas tertinggi)

**Kebijakan canon:** keputusan eksplisit terbaru mengungguli uraian lama yang bertentangan. Seluruh teks historis tetap disimpan. Gambar generatif adalah referensi visual, bukan sumber perubahan canon otomatis. Tingkat persetujuan desain setiap karakter dicatat terpisah.

### Amamiya Chiasa — Female Route / heroine Koita pada Male Route
**Status: visual canon disetujui oleh pemain.**
- Referensi utama: gambar anime perempuan yang diunggah pemain (rambut half-up dengan pita gelap, poni menyamping, senyum jahil, pose tangan dekat dagu, sweater off-shoulder). Penampilan mengikuti referensi itu **kecuali warna rambut dan mata**.
- Rambut **dark brown/cokelat gelap** (menggantikan putih/keperakan; **SUPERSEDED**); panjang sampai punggung tengah, long layered, sedikit bergelombang; half-up dengan pita hitam; poni dan helaian wajah dibuat ekspresif, mendukung kesan tengil.
- Mata **kuning keemasan/golden yellow** (menggantikan ungu/amethyst; **SUPERSEDED**).
- Tinggi **160–163 cm**, tubuh proporsional feminin, wajah oval, ekspresi khas smirk jahil/menggoda dan percaya diri.
- Aksesori elegan tidak berlebihan, terutama anting kecil dan kalung tipis; pita rambut sebagai elemen khas. Model anting gantung pada referensi tidak wajib untuk setiap outfit.
- Fashion: **simple but stylish**, tahu cara memadukan pakaian simpel agar tampak modis, cantik, feminin, dan berkelas. **Lebih sering memakai rok (pilihan A)**; blus, knit top, cardigan, sweater, rok high-waist, dan sepatu serasi. Celana tetap boleh saat lebih praktis; dress untuk kesempatan khusus.
- Sweater putih off-shoulder dari referensi merupakan salah satu outfit, **bukan pakaian default tunggal yang wajib**. Outfit dapat berubah menurut kegiatan/musim/event.
- Ilustrasi character sheet Chiasa yang dibuat dan dipuji pemain: `a_detailed_anime_style_character_sheet_collage_of.png` (berkas referensi tersedia bersama dokumen; penetapan desain tetap didasarkan pada pilihan dan koreksi eksplisit pemain).

### Kisaragi Yutaka — Male Route / NPC pada Female Route
**Status: desain sangat disukai pemain; persetujuan penguncian final belum dinyatakan eksplisit.**
- Rambut hitam pekat, modern two-block; mata dark grey.
- Tinggi **183–187 cm**; tubuh slim athletic; wajah refined handsome.
- Aura relaxed handsome: santai, karismatik, approachable, tidak terlalu intimidating.
- Pakaian minimalist luxury, dominan **navy, putih, beige**; tidak menggunakan aksesori mencolok. Kesan mahal dari kualitas dan padu padan, bukan logo berlebihan.
- Ilustrasi character sheet Yutaka: `a_detailed_anime_character_profile_sheet_in_a_styl.png` (referensi gambar, bukan sumber detail baru).

### Amamiya Koita — MC manga asli, pusat konflik
**Status: draft visual dari 10 jawaban pemain; ilustrasi telah dibuat, tetapi belum disetujui/dikunci final.**
- Rambut **hitam alami**, messy short hair, dengan **satu ahoge** khas protagonis manga.
- Mata **hitam gelap**; tinggi **172–175 cm**; tubuh **slim average**.
- Wajah **boy-next-door**, tampan natural, mudah didekati; ekspresi default senyum hangat yang terlihat tulus.
- Pakaian kasual ala MC shonen: kaus, jaket/hoodie, celana kasual, sneakers.
- Penampilan **sama sekali tidak mengisyaratkan sifat manipulatif** pada kesan pertama. Kontras antara citra ramah dan sifat sebenarnya merupakan elemen naratif, bukan desain wajah yang tampak jahat.
- Character sheet Koita: `a_detailed_anime_character_sheet_infographic_in_a.png` (hasil generasi terbaru). Ekspresi, variasi outfit, dan tampak samping/belakang pada gambar adalah **referensi visual**, tidak otomatis menjadi canon detail yang belum dipilih.

### Konsistensi rute dan status desain
- Male Route = pemain sebagai Yutaka; Chiasa tetap heroine NPC Koita. Female Route = pemain sebagai Chiasa; Yutaka tetap NPC. Koita adalah MC asli manga di kedua rute.
- Chiasa: visual dikunci. Yutaka: desain dipuji, menunggu konfirmasi final. Koita: draft dengan gambar untuk dievaluasi.
- Aturan lama bahwa pemain dapat mengganti **pakaian dan aksesori**, bukan ciri dasar host, tetap berlaku.
- **SUPERSEDED khusus Chiasa:** semua penyebutan rambut putih/keperakan dan mata ungu/amethyst sebagai desain Chiasa aktif pada versi terdahulu diganti dengan dark brown dan golden yellow. Warna rambut putih dan mata amethyst **tetap milik Shiori**, bila disebut dalam canon Shiori; jangan ikut mengubah karakter lain.

### Backlog keputusan gameplay (belum digabungkan ke seksi tematik)
- Batch 19 no. 7–10 telah dijawab: quest dapat gagal langsung/tidak langsung; quest hanya dari Sistem NTR (NPC tidak memberi quest mandiri); quest dapat ditunda sebelum deadline; quest yang tidak relevan dapat berubah, kedaluwarsa, atau digantikan event lain.
- Batch 20 tentang ekonomi **belum dijawab**; jangan menganggap opsi pertanyaannya sebagai keputusan canon.
- Pembaruan ini dibuat atas permintaan eksplisit pemain dan **tidak mengubah aturan pembaruan rutin setiap enam jawaban**.

**Changelog 1.19 — 10 November 2026:** Seluruh konten versi sebelumnya dipertahankan; ditambahkan addendum visual tiga karakter, supersession Chiasa, status persetujuan desain, dan backlog keputusan.


## ADDENDUM VISUAL HEROINE — 10 November 2026 (pembaruan setelah desain Shiori, Miyuki, dan Nagisa)

**Aturan:** Template character sheet tetap sama seperti yang telah digunakan untuk karakter sebelumnya. Tidak ada kategori profil baru yang ditambahkan. Ilustrasi adalah referensi presentasi; hanya detail yang dipilih atau disetujui eksplisit oleh pemain yang menjadi canon.

### Saionji Shiori — heroine #5
**Status: visual canon disetujui (ACC).**
- Rambut putih keperakan dan mata ungu amethyst tetap menjadi ciri visual Shiori.
- Gaya rambut mengikuti referensi sketsa yang dikirim pemain: bagian atas rambut ditata/digerai menyilang dan bervolume, sementara rambut panjang bergelombang diarahkan jatuh ke depan melewati bahu. Penataan rambut bukan sanggul rendah di belakang kepala.
- Character sheet final yang disetujui: `a_detailed_character_sheet_illustration_in_a_purpl.png`.
- Ilustrasi character sheet menjadi acuan visual untuk sprite, ekspresi, pose, turnaround, dan variasi outfit. Detail tambahan yang hanya muncul pada gambar dan belum dipilih secara terpisah tidak otomatis menjadi fakta canon.

### Tachibana Miyuki — heroine #2
**Status: visual canon disetujui (ACC), setelah revisi.**
- Rambut hitam panjang, lurus, dan terurai alami.
- Tidak menggunakan hiasan rambut atau aksesori kepala. Revisi ini menggantikan ornamen bunga/aksesori kepala yang sempat muncul pada draft ilustrasi sebelumnya (**SUPERSEDED**).
- Mata biru sapphire.
- Identitas visual tetap elegan, dewasa, hangat, dan memiliki aura onee-san; outfit utama pada character sheet menampilkan jas dokter putih di atas atasan ungu gelap, rok hitam, dan stetoskop sesuai konteks mahasiswi kedokteran.
- Character sheet revisi yang disetujui: `a_detailed_anime_character_sheet_visual_profile_fo.png`.
- Detail tinggi badan atau ukuran fisik yang hanya tertulis pada ilustrasi generatif tidak ditetapkan sebagai canon baru kecuali telah dipilih secara eksplisit.

### Sakurajima Nagisa — heroine #3
**Status: draft visual; belum ACC.**
- Rambut blonde dengan twin-tail, mata biru.
- Tinggi 155 cm; tubuh petite, ramping, dan atletis.
- Mahasiswi tahun kedua Fakultas Arsitektur; ekspresi dan presentasi mengikuti karakter tsundere yang kompetitif, peduli melalui tindakan, dan menyukai game kompetitif meskipun kemampuan bermainnya kurang baik.
- Draft character sheet menggunakan template yang sama seperti Shiori dan Miyuki: `a_detailed_anime_character_sheet_illustration_boar.png`.
- Pemain meminta agar template tetap sama dan tidak menambah kategori baru. Draft ini belum disetujui sebagai visual canon; revisi masih dapat dilakukan.

### Status persetujuan visual heroine
- Shiori: **ACC — visual canon**.
- Miyuki: **ACC — visual canon**, rambut lurus dan tanpa hiasan kepala.
- Nagisa: **draft — menunggu ACC**.
- Chiasa: **ACC — visual canon** (lihat addendum visual sebelumnya).
- Yutaka dan Koita: status tetap mengikuti addendum visual sebelumnya; tidak diubah oleh pembaruan ini.

**Changelog v1.20 — 10 November 2026:** Seluruh isi v1.19 dipertahankan. Ditambahkan desain visual Shiori yang telah di-ACC, revisi Miyuki (rambut lurus tanpa hiasan kepala) yang telah di-ACC, serta draft character sheet Nagisa dengan template yang sama dan tanpa kategori tambahan. Tidak ada perubahan pada sistem gameplay atau canon karakter lain.

## ADDENDUM BATCH 20 — SISTEM EKONOMI & KEUANGAN (Keputusan #1–#14 ACC)

**Status historis v1.21:** Keputusan #1–#14 ACC; keputusan #15–#24 ditetapkan dalam addendum v1.22 di bawah.

1. **Detail ekonomi — C, realistis penuh untuk pemain:** seluruh pemasukan dan pengeluaran pemain dalam yen dicatat; makanan, transportasi, tagihan, belanja, hadiah, hiburan, dan kencan memiliki biaya nyata. Ekonomi NPC kemudian disederhanakan khusus oleh keputusan #7.
2. **Sumber penghasilan — B:** uang saku keluarga dan pekerjaan paruh waktu (*baito*) adalah sumber standar. **Pengecualian eksplisit:** Chiasa memiliki royalti pasif tetap dari ilustrasi light novel yang telah dibuatnya.
3. **Pekerjaan — C, hybrid:** shift rutin bisa dilewati otomatis dengan waktu dan gaji tetap dihitung; pertemuan, konflik, dan event penting bisa dimainkan interaktif.
4. **Pengeluaran — D:** transaksi default manual; pemain dapat mengaktifkan pembayaran otomatis per kategori, dan mengubah pengaturannya kapan saja. Kekurangan dana menyebabkan pembayaran gagal.
5. **Harga — B, dinamis sederhana:** harga dasar wajar untuk Jepang modern; diskon, promosi, musim, event kampus, dan perbedaan toko dapat memengaruhi harga. Tidak ada simulasi inflasi makro yang rumit.
6. **Utang — A, tidak ada mekanik pinjaman:** pemain hanya membelanjakan dana yang tersedia; tidak ada kartu kredit berbasis utang, cicilan, atau pinjaman dari NPC/keluarga. Transaksi tanpa dana cukup ditolak.
7. **Ekonomi NPC — A, sederhana:** NPC mempunyai tingkat ekonomi dan kebiasaan belanja sesuai latar, tetapi saldo serta seluruh transaksi individualnya tidak disimulasikan detail. Yutaka/Chiasa sebagai host pemain tetap menggunakan saldo detail.
8. **Uang saku — A:** nominal tetap dibayar bulanan, sesuai latar keluarga masing-masing.
9. **Yutaka — B:** uang saku ¥150.000 per bulan; kuliah dan apartemen ditanggung keluarga Kisaragi. Pengeluaran pribadi dibayar dari saldo pemain.
10. **Chiasa — custom:** uang saku keluarga Amamiya ¥50.000 per bulan **ditambah royalti pasif tetap ¥50.000 per bulan** dari ilustrasi light novel yang sudah dikerjakannya. Total pendapatan tetap ¥100.000/bulan.
11. **Royalti Chiasa — A:** pasif penuh; tidak ada kewajiban membuat ilustrasi baru, deadline, shift, atau kontak editor untuk menerima royalti. Pekerjaan/proyek baru boleh dipilih pemain secara sukarela.
12. **Saldo awal — B dengan revisi eksplisit:** Yutaka **¥500.000**, Chiasa **¥400.000** (menggantikan angka lama ¥250.000). Saldo tersimpan lintas hari/bulan, bukan reset.
13. **Penyimpanan uang — A:** satu saldo utama; uang tunai, debit, transfer, dompet digital hanyalah pilihan metode pembayaran, tidak memiliki saldo terpisah. Tidak perlu simulasi ATM.
14. **Inventaris — C:** semua barang yang dibeli memiliki kepemilikan, kuantitas, kondisi, lokasi penyimpanan, dan fungsi; barang konsumsi dapat habis, pakaian digunakan ulang, elektronik dapat rusak, hadiah bisa diberikan. Tidak termasuk manajemen dekorasi/furnitur terperinci.

**Penting:** Nominal di atas adalah aturan gameplay yang di-ACC, bukan simulasi saldo terperinci untuk semua NPC. Perbedaan sumber penghasilan Chiasa dari opsi umum #2 merupakan pengecualian canon yang disengaja.

**Status selanjutnya (historis v1.21):** Paket #15–#24 dijawab dan di-ACC dalam v1.22.


## ADDENDUM BATCH 20 — SISTEM EKONOMI & KEUANGAN (Keputusan #15–#24 ACC)

**Status:** Semua keputusan Batch 20 #1–#24 ACC. Ketentuan berikut melengkapi addendum #1–#14; tidak mengubah saldo awal dan pendapatan host yang sudah ditetapkan.

15. **Penjualan barang bekas — A:** tidak ada fitur menjual kembali barang. Item dapat disimpan, digunakan, diberikan, atau dibuang.
16. **Belanja — B:** katalog lengkap berdasarkan toko, kategori, dan stok; transaksi mengikuti saldo tunggal dan harga yang berlaku.
17. **Stok — B:** barang umum selalu tersedia, sedangkan barang khusus dapat habis stok.
18. **Pengiriman online — D:** pembelian online memiliki waktu pengiriman, pilihan ekspedisi, ongkos kirim, dan kemungkinan keterlambatan; barang masuk inventaris setelah diterima.
19. **Hadiah — D:** reaksi NPC dipengaruhi preferensi, hubungan, situasi, makna hadiah, serta ingatan atas riwayat pemberian hadiah dan konsekuensi sosial.
20. **Biaya kencan — D:** pemain bebas menawarkan traktiran, patungan, atau menerima traktiran; NPC dapat merespons sesuai karakter dan keadaan.
21. **Diskon — A:** diskon otomatis tercermin pada harga barang; tidak perlu mekanik kupon terpisah. Tetap selaras dengan perubahan harga sederhana yang di-ACC pada #5.
22. **Kerusakan barang — B:** kerusakan hanya dipicu event tertentu, bukan degradasi otomatis berkala. Inventaris tetap menyimpan kondisi barang sesuai #14; perubahan kondisi dapat terjadi akibat event.
23. **Kebutuhan hidup — C:** indikator lapar, energi, dan kebersihan memengaruhi aktivitas pemain; pemenuhan kebutuhan menimbulkan pengeluaran sesuai aturan ekonomi.
24. **Antarmuka keuangan — B:** menampilkan saldo dan riwayat transaksi; tidak wajib ada grafik, dashboard anggaran, atau laporan bulanan terperinci.

**Changelog v1.22 — 10 November 2026:** Menambahkan sepuluh keputusan ACC #15–#24 pada Batch 20, mempertahankan seluruh isi GDD v1.21 termasuk keputusan #1–#14, saldo awal Yutaka ¥500.000 dan Chiasa ¥400.000, serta royalti pasif Chiasa ¥50.000/bulan. Pertanyaan berikutnya dimulai dari #25 dalam paket sepuluh pertanyaan.

## ADDENDUM BATCH 20 — SISTEM EKONOMI & KEUANGAN (Keputusan #25–#34 ACC)

**Status:** Seluruh keputusan Batch 20 #1–#34 ACC. Addendum ini melengkapi keputusan sebelumnya tanpa menghapus atau mengubah canon terdahulu.

25. **Jenis pekerjaan paruh waktu — C:** pilihan pekerjaan realistis mencakup pekerjaan umum (kafe, retail, restoran, tutor, administrasi) serta pekerjaan berbasis kemampuan karakter seperti ilustrasi, pemrograman, dan penerjemahan.
26. **Sistem gaji — D:** upah per jam bervariasi menurut jenis pekerjaan, keterampilan, dan pengalaman. Kinerja/masa kerja dapat membuka kenaikan gaji, bonus, dan evaluasi.
27. **Melamar dan berhenti kerja — B:** pekerjaan diperoleh melalui proses melamar lowongan dan diterima jika memenuhi syarat. Mekanik wawancara/seleksi lanjutan tidak diwajibkan oleh keputusan ini.
28. **Jadwal dan batas jam kerja — C:** shift dapat tetap atau fleksibel bergantung pada pekerjaan; benturan dengan kuliah dan kelelahan diperhitungkan.
29. **Konsekuensi kinerja kerja — B:** keterlambatan, bolos, dan kinerja memengaruhi gaji serta risiko pemecatan. Dampak tambahan terhadap reputasi dan relasi kerja tidak ditetapkan oleh pilihan ini.
30. **Sistem lapar — C:** rasa lapar memengaruhi energi, konsentrasi, suasana hati, dan efektivitas aktivitas.
31. **Energi dan istirahat — C:** tidur, istirahat, dan aktivitas santai memulihkan energi dengan efektivitas berbeda.
32. **Kebersihan pribadi — D:** kebersihan dipengaruhi aktivitas, cuaca, dan kebersihan pakaian; memengaruhi kenyamanan serta reaksi NPC.
33. **Kesulitan finansial — C:** saldo tidak cukup membatasi pembelian dan pemenuhan kebutuhan; dapat memengaruhi kondisi karakter, jadwal, dan peluang sosial. Event bantuan nonpinjaman khusus tidak otomatis ditambahkan.
34. **Informasi harga — A:** harga hanya terlihat ketika pemain membuka toko; tidak ada fitur pembanding harga lintas toko, daftar keinginan, notifikasi diskon, atau riwayat harga.

**Catatan konsistensi:** Pekerjaan tetap mengikuti sistem hybrid #3 (shift rutin dapat dilewati otomatis, event penting dimainkan interaktif). Keputusan #29 dipilih sebagai B sehingga konsekuensi yang dikunci adalah gaji dan risiko pemecatan; jangan menambahkan reputasi kerja atau relasi kerja sebagai efek sistematis tanpa persetujuan baru. Keputusan #34 membatasi informasi harga pada tampilan toko yang sedang dibuka, meskipun katalog tiap toko tetap tersedia sesuai #16.

**Changelog v1.23 — 10 November 2026:** Mempertahankan seluruh isi GDD v1.22 dan menambahkan sepuluh keputusan ACC Batch 20 #25–#34. Tidak ada perubahan pada keputusan ekonomi #1–#24, termasuk saldo awal Yutaka ¥500.000, saldo awal Chiasa ¥400.000, uang saku Yutaka ¥150.000/bulan, uang saku Chiasa ¥50.000/bulan, serta royalti pasif Chiasa ¥50.000/bulan.


## ADDENDUM BATCH 20 — SISTEM EKONOMI & KEUANGAN (Keputusan #35–#44 ACC)

**Status:** Seluruh keputusan Batch 20 #1–#44 ACC. Addendum ini melengkapi keputusan terdahulu dan tidak menghapus atau mengubahnya.

35. **Sistem menabung — A:** tidak ada mekanik target tabungan khusus. Saldo yang tidak dibelanjakan otomatis tetap tersimpan sebagai tabungan dalam saldo utama.
36. **Pengeluaran bulanan — D:** tagihan berkala memiliki rincian dan konsekuensi keterlambatan. Pembayaran dapat dilakukan manual atau melalui auto-payment sesuai pengaturan #4; kegagalan pembayaran karena saldo tidak cukup tetap berlaku.
37. **Biaya kuliah dan akademik — A:** seluruh biaya kuliah ditanggung keluarga host. Ini tidak mengubah ketentuan pengeluaran pribadi atau kebutuhan akademik lain yang belum secara eksplisit ditanggung keluarga.
38. **Transportasi — C:** ongkos perjalanan berbeda berdasarkan jarak dan moda transportasi.
39. **Biaya kesehatan — C:** biaya perawatan berbeda menurut jenis perawatan dan fasilitas kesehatan. Tidak ada mekanik asuransi tambahan yang ditetapkan oleh pilihan ini.
40. **Pakaian — D:** pakaian dapat dipilih dan digunakan; kesesuaiannya dipengaruhi cuaca, acara, dress code, serta kondisi pakaian. Kondisi tidak menurun otomatis karena pemakaian; kerusakan tetap mengikuti keputusan #22 dan terjadi melalui event tertentu.
41. **Makanan dan memasak — C:** pemain dapat membeli makanan atau memasak dengan bahan yang dibeli; tersedia resep, kemampuan memasak, dan kualitas hasil masakan.
42. **Hiburan berbayar — D:** aktivitas seperti karaoke, bioskop, arcade, dan konser memiliki biaya; tersedia variasi harga, reservasi, tiket terbatas, dan event khusus.
43. **Pembelian barang digital — B:** game, DLC, aplikasi, dan konten digital dapat dibeli melalui transaksi sederhana. Sistem langganan/biaya berulang tidak ditetapkan.
44. **Pengeluaran NPC — D:** NPC dapat mentraktir, memberi hadiah, membayar kencan, dan membeli sesuatu untuk karakter lain berdasarkan kepribadian, hubungan, dan kondisi ekonomi. Ini tetap tidak mengaktifkan simulasi saldo/transaksi NPC secara detail; kategori ekonomi NPC mengikuti keputusan #7.

**Catatan konsistensi:** Saldo pemain tetap satu saldo utama (#13); tidak ada rekening tabungan terpisah atau bunga (#35). Biaya kuliah ditanggung keluarga untuk kedua host (#37), sedangkan uang saku dan royalti Chiasa tetap mengikuti keputusan #9–#11. Pengeluaran NPC bersifat perilaku/kejadian yang disimulasikan secara sederhana, bukan ledger finansial penuh (#7).

**Changelog v1.24 — 10 November 2026:** Mempertahankan seluruh isi GDD v1.23 dan menambahkan sepuluh keputusan ACC Batch 20 #35–#44. Tidak ada perubahan pada keputusan ekonomi #1–#34, saldo awal Yutaka ¥500.000, saldo awal Chiasa ¥400.000, uang saku Yutaka ¥150.000/bulan, uang saku Chiasa ¥50.000/bulan, serta royalti pasif Chiasa ¥50.000/bulan. Pertanyaan berikutnya dimulai dari #45.


## ADDENDUM BATCH 20 — SISTEM EKONOMI & KEUANGAN (Keputusan #45–#54 ACC)

**Status:** Seluruh keputusan Batch 20 #1–#54 ACC. Addendum ini melengkapi keputusan terdahulu dan tidak menghapus atau mengubahnya.

45. **Telepon dan internet — A:** biaya telepon dan internet ditanggung keluarga sepenuhnya; tidak ada tagihan komunikasi yang dibayar dari saldo pemain.
46. **Layanan berlangganan digital — A:** layanan streaming, musik, dan aplikasi premium tidak tersedia sebagai mekanik pembelian/berlangganan.
47. **Tempat tinggal Yutaka — A:** seluruh biaya apartemen dan utilitas Yutaka ditanggung keluarga Kisaragi.
48. **Rumah keluarga Amamiya — A:** seluruh biaya rumah tangga tempat Chiasa dan Koita tinggal ditanggung orang tua.
49. **Kebutuhan rumah — A:** pembelian kebutuhan rumah seperti sabun, deterjen, tisu, dan perlengkapan kebersihan tidak disimulasikan sebagai mekanik rutin.
50. **Laundry — B:** pakaian dibersihkan otomatis setelah waktu tertentu; tidak perlu memilih mencuci sendiri atau membayar layanan laundry.
51. **Hewan peliharaan — D:** pemain dapat merawat atau membantu membiayai hewan peliharaan NPC; kebutuhan dapat mencakup makanan, perawatan, perlengkapan, dan dokter hewan.
52. **Pemberian uang kepada NPC — C:** pemain dapat memberikan uang secara bebas kepada NPC yang memiliki hubungan dekat. Ini adalah pemberian langsung, bukan pinjaman atau sistem utang.
53. **Barang mahal — A:** pembelian barang bernilai tinggi dapat dilakukan langsung selama saldo cukup; tidak ada prosedur konfirmasi/pertimbangan khusus tambahan.
54. **Peringatan saldo — A:** tidak ada peringatan otomatis atau rekomendasi ketika saldo menipis atau pengeluaran meningkat.

**Catatan konsistensi:** Biaya apartemen/utilitas Yutaka dan biaya rumah tangga Amamiya tidak mengurangi saldo host karena ditanggung keluarga. Biaya kesehatan hewan peliharaan berlaku ketika pemain memilih merawat atau membantu membiayai hewan NPC. Pemberian uang kepada NPC (#52) tidak membatalkan larangan pinjaman/utang (#6). Pakaian tetap dibersihkan otomatis (#50), sedangkan kerusakan pakaian hanya terjadi melalui event tertentu (#22).

**Changelog v1.25 — 10 November 2026:** Mempertahankan seluruh isi GDD v1.24 dan menambahkan sepuluh keputusan ACC Batch 20 #45–#54. Tidak ada perubahan pada keputusan ekonomi #1–#44, saldo awal Yutaka ¥500.000, saldo awal Chiasa ¥400.000, uang saku Yutaka ¥150.000/bulan, uang saku Chiasa ¥50.000/bulan, serta royalti pasif Chiasa ¥50.000/bulan. Pertanyaan berikutnya dimulai dari #55.

## ADDENDUM BATCH 20 — SISTEM EKONOMI & KEUANGAN (Keputusan #55–#64 ACC)

**Status:** Seluruh keputusan Batch 20 #1–#64 ACC. Addendum ini melengkapi keputusan terdahulu dan tidak menghapus atau mengubahnya.

55. **Uang tunai hadiah — D:** uang yang diberikan NPC kepada pemain langsung menambah saldo utama dan dicatat sebagai hadiah; NPC dapat memberi secara spontan atau dalam event, dengan nominal/frekuensi dipengaruhi hubungan serta kemampuan ekonomi NPC.
56. **Barang koleksi dan hobi — A:** barang koleksi seperti figur, merchandise, kartu, dan model kit tidak tersedia sebagai mekanik pembelian khusus.
57. **Hadiah ulang tahun — D:** NPC memiliki preferensi dan reaksi khusus terhadap hadiah ulang tahun serta mengingat hadiah yang diterima pada tahun sebelumnya.
58. **Biaya kegiatan klub — D:** klub dapat memiliki iuran, perlengkapan, biaya kegiatan, perjalanan, kompetisi, dan event khusus berbayar.
59. **Festival universitas — D:** pemain dapat membeli makanan/barang, permainan, merchandise, dan tiket kegiatan; pemain juga dapat bekerja di stan dan memperoleh penghasilan.
60. **Perjalanan dan liburan — D:** perjalanan memiliki biaya transportasi, penginapan, makan, aktivitas, dan durasi; pemain dapat merencanakan anggaran, melakukan reservasi, serta memilih akomodasi.
61. **Kehilangan barang dan uang — B:** kehilangan hanya terjadi melalui event cerita; bukan kejadian acak atau akibat kelalaian yang disimulasikan rutin.
62. **Pemberian barang kepada NPC — D:** pemain dapat memberi barang sesuai hubungan dan preferensi; NPC dapat menerima, menolak, menyimpan, atau menggunakan hadiah.
63. **Barang rusak dan penggantian — B:** barang yang rusak akibat event tetap dimiliki, tetapi tidak dapat digunakan. Opsi perbaikan/penggantian atau klaim garansi tidak ditetapkan oleh pilihan ini.
64. **Tingkat detail ekonomi — B:** ekonomi penting untuk keputusan sehari-hari, tetapi tidak mendominasi permainan; fokus utama tetap kehidupan kampus, interaksi sosial, dan cerita.

**Catatan konsistensi:** Uang hadiah NPC menambah saldo tunggal pemain dan bukan pinjaman (#6, #13). Keputusan #56 meniadakan sistem koleksi khusus, tanpa menghapus kemungkinan barang biasa atau hadiah relevan muncul sebagai item cerita. Kerusakan barang tetap dipicu event (#22), dan barang rusak tidak dapat digunakan (#63). Ekonomi NPC tetap sederhana (#7), meskipun perilaku pemberian hadiah mengikuti hubungan dan kemampuan ekonomi (#44, #55).

**Changelog v1.26 — 10 November 2026:** Mempertahankan seluruh isi GDD v1.25 dan menambahkan sepuluh keputusan ACC Batch 20 #55–#64. Tidak ada perubahan pada keputusan ekonomi #1–#54, saldo awal Yutaka ¥500.000, saldo awal Chiasa ¥400.000, uang saku Yutaka ¥150.000/bulan, uang saku Chiasa ¥50.000/bulan, serta royalti pasif Chiasa ¥50.000/bulan. Pertanyaan berikutnya dimulai dari #65.

## ADDENDUM BATCH 20 — SISTEM EKONOMI & KEUANGAN (Keputusan #65–#74 ACC)

**Status:** Seluruh keputusan Batch 20 #1–#74 ACC. Addendum ini melengkapi keputusan terdahulu dan tidak menghapus atau mengubahnya.

65. **Beasiswa — A:** beasiswa tidak tersedia sebagai mekanik pemain.
66. **Hadiah keluarga — C:** orang tua dapat memberikan hadiah tambahan pada ulang tahun, hari raya, atau pencapaian. Hadiah ini merupakan pemberian situasional, bukan perubahan uang saku bulanan tetap.
67. **Pekerjaan freelance — A:** pekerjaan freelance di luar pekerjaan paruh waktu yang sudah ditetapkan tidak tersedia sebagai mekanik.
68. **Kompetisi berhadiah — D:** kompetisi dapat memberikan hadiah uang dengan variasi berdasarkan tingkat kompetisi dan prestasi yang diraih.
69. **Kencan spesial — D:** aktivitas romantis spesial dapat memiliki pilihan anggaran, kejutan, reservasi, dan reaksi pasangan.
70. **Donasi dan bantuan sosial — A:** tidak ada mekanik donasi atau pemberian bantuan sosial secara terpisah.
71. **Pajak — A:** tidak ada simulasi pajak; pendapatan pekerjaan diterima tanpa penghitungan/pemotongan pajak dalam gameplay.
72. **Biaya administrasi dan layanan — A:** tidak ada biaya tambahan administrasi atau layanan transaksi.
73. **Event ekonomi musiman — C:** musim dan hari besar Jepang memengaruhi belanja, hadiah, perjalanan, dan aktivitas sosial.
74. **Integrasi ekonomi dengan sandbox — C:** ekonomi terintegrasi dengan kalender, hubungan NPC, pekerjaan, dan event dinamis, tetapi tetap menjadi sistem pendukung dan tidak mendominasi permainan sesuai #64.

**Catatan konsistensi:** Hadiah keluarga (#66) tidak mengubah nominal uang saku bulanan tetap Yutaka dan Chiasa. Hadiah kompetisi (#68) merupakan hadiah event, bukan pekerjaan freelance atau beasiswa. Tidak ada pajak (#71) maupun biaya transaksi tambahan (#72). Pengaruh musim dan hari besar (#73) berjalan bersama sistem harga dinamis sederhana (#5), tanpa menambahkan simulasi inflasi makroekonomi. Integrasi ekonomi (#74) tetap mengikuti batas tingkat detail yang dipilih pada #64.

**Changelog v1.27 — 10 November 2026:** Mempertahankan seluruh isi GDD v1.26 dan menambahkan sepuluh keputusan ACC Batch 20 #65–#74. Tidak ada perubahan pada keputusan ekonomi #1–#64, saldo awal Yutaka ¥500.000, saldo awal Chiasa ¥400.000, uang saku Yutaka ¥150.000/bulan, uang saku Chiasa ¥50.000/bulan, serta royalti pasif Chiasa ¥50.000/bulan.


## ADDENDUM BATCH 20 — SISTEM EKONOMI & KEUANGAN (Keputusan #75–#84 ACC)

**Status:** Seluruh keputusan Batch 20 #1–#84 telah dijawab dan ACC. Addendum ini mempertahankan keputusan terdahulu tanpa menghapusnya.

75. **Hadiah hari raya Jepang — D:** pada Natal, Tahun Baru, Valentine, White Day, dan hari besar relevan, hadiah dapat dipilih berdasarkan tradisi, preferensi penerima, hubungan, serta anggaran; reaksi NPC berbeda sesuai karakter.
76. **Pembayaran hadiah kompetisi — C:** hadiah uang dibayarkan setelah hasil diumumkan dan diserahkan melalui event penyerahan hadiah.
77. **Hadiah dari teman — D:** NPC dapat memberi hadiah pada ulang tahun, hari raya, pencapaian, atau secara spontan sesuai kepribadian dan kedekatan.
78. **Uang tambahan keluarga — B:** permintaan uang tambahan kepada orang tua hanya dapat terjadi melalui event cerita. Ini tidak mengubah uang saku bulanan tetap (#8–#10).
79. **Pengeluaran romantis — D:** tersedia kejutan dan aktivitas berdasarkan preferensi pasangan serta anggaran; kejutan yang terlalu mahal atau tidak sesuai preferensi dapat menimbulkan konsekuensi.
80. **Biaya kompetisi gaming — A:** semua kompetisi gaming gratis; tidak ada biaya pendaftaran, perjalanan, perlengkapan, atau sponsor yang ditambahkan sebagai mekanik biaya kompetisi.
81. **Perlengkapan hobi kreatif Chiasa — A:** tidak ada biaya khusus untuk perlengkapan ilustrasi/desain dalam sistem ekonomi.
82. **Pengeluaran sosial grup — D:** biaya kelompok dapat dibagi atau ditraktir; pembagian dan reaksi sosial mengikuti karakter serta hubungan.
83. **Acara pribadi — D:** pemain dapat mengatur perayaan ulang tahun dengan anggaran, reservasi, kejutan, dan respons tamu.
84. **Prioritas penyelesaian — D:** lakukan audit konsistensi keputusan #1–#84 sebelum menambah pertanyaan ekonomi. Pertanyaan tambahan hanya dibuat jika audit menunjukkan kebutuhan yang benar-benar belum ditetapkan.

## AUDIT KONSISTENSI BATCH 20 (#1–#84)

Audit awal menemukan beberapa area yang perlu dibedakan atau diklarifikasi sebelum dianggap sebagai aturan final yang sepenuhnya operasional:

1. **Tagihan berkala (#36) vs biaya tempat tinggal ditanggung keluarga (#47–#48):** keluarga menanggung apartemen/utilitas Yutaka dan seluruh biaya rumah tangga Amamiya, sedangkan #36 menetapkan tagihan berkala dan konsekuensi keterlambatan. Belum ditentukan tagihan pribadi apa yang masih menjadi tanggung jawab pemain. Jangan menganggap utilitas rumah sebagai tagihan pemain.
2. **Barang rusak (#22 dan #63):** kerusakan hanya terjadi melalui event (#22); bila rusak, barang tetap dimiliki tetapi tidak dapat digunakan (#63). Tidak ada mekanik perbaikan atau penggantian yang dipilih. Ini konsisten, tetapi berarti barang rusak dapat tetap tidak dapat digunakan.
3. **Laundry (#50) vs kebersihan pakaian (#40):** laundry berjalan otomatis setelah waktu tertentu, sedangkan kondisi pakaian juga relevan terhadap cuaca/acara/dress code. Belum ditentukan apakah laundry otomatis memerlukan biaya atau mengonsumsi waktu.
4. **Hadiah uang NPC (#55, #77) dan pemberian uang kepada NPC (#52):** uang yang diberikan adalah hadiah, bukan pinjaman; nominal/frekuensi NPC bergantung hubungan dan kemampuan ekonomi. Tidak ada sistem utang.
5. **Biaya kompetisi gaming (#80) vs biaya kompetisi/klub umum (#58):** kompetisi gaming gratis, sementara klub secara umum dapat memiliki biaya kegiatan/perjalanan/kompetisi. Untuk gaming, pilihan #80 menjadi aturan lebih spesifik.
6. **Perlengkapan ilustrasi Chiasa (#81):** tidak ada biaya khusus untuk perlengkapan hobi kreatif. Royalti pasif ¥50.000/bulan tetap diterima tanpa kewajiban kerja baru (#10–#11).
7. **Hadiah dan pengeluaran NPC (#7, #19, #44, #55, #57, #62, #77):** perilaku dan reaksi NPC disimulasikan berdasarkan kategori ekonomi, kepribadian, preferensi, dan hubungan; tidak berarti setiap NPC memiliki ledger saldo individual.
8. **Pengeluaran rumah tangga (#47–#49):** kebutuhan rumah tidak disimulasikan sebagai pembelian rutin (#49); seluruh biaya rumah keluarga Amamiya dan biaya apartemen/utilitas Yutaka ditanggung keluarga.

**Status audit pada v1.28:** Butir #1 dan #3 ditandai memerlukan klarifikasi. Keduanya telah diselesaikan melalui klarifikasi #1–#3 pada v1.29, dan seluruh audit kini dinyatakan selesai.

**Changelog v1.28 — 10 November 2026:** Mempertahankan seluruh isi v1.27 dan menambahkan sepuluh keputusan ACC Batch 20 #75–#84 serta audit konsistensi ekonomi #1–#84. Tidak ada keputusan lama yang dihapus atau diubah.


## ADDENDUM AUDIT FINAL BATCH 20 — KLARIFIKASI #1–#9 ACC

**Status:** Seluruh klarifikasi #1–#9 telah dijawab dan ACC. Addendum ini menyelesaikan area yang sebelumnya ditandai ambigu dalam audit v1.28. Keputusan Batch 20 #1–#84 tetap dipertahankan.

1. **Tagihan pribadi rutin — A:** tidak ada tagihan pribadi rutin. Biaya rumah tangga Amamiya serta apartemen dan utilitas Yutaka ditanggung keluarga. Pengeluaran hanya muncul jika pemain memilih layanan atau melakukan pembelian tertentu. Ini memperjelas #36 tanpa mengubah tanggung jawab keluarga pada #47–#48.
2. **Laundry profesional — B:** layanan laundry profesional berbayar; penggunaan layanan mengurangi saldo pemain.
3. **Metode laundry — C:** sistem hybrid. Pakaian sehari-hari dicuci di rumah menggunakan mesin cuci; pakaian khusus dapat menggunakan layanan laundry profesional.
4. **Biaya laundry rumah — A:** pencucian sehari-hari di rumah gratis sepenuhnya bagi pemain; tidak ada biaya deterjen, air, listrik, atau operasional mesin yang dibebankan ke saldo. Ini selaras dengan biaya rumah/utilitas yang ditanggung keluarga.
5. **Harga laundry profesional — D:** biaya layanan profesional menggunakan biaya standar setiap kali layanan digunakan; rincian biaya per jenis pakaian atau tingkat kesulitan tidak disimulasikan.
6. **Perbaikan barang rusak — D:** barang yang rusak akibat event dapat diperbaiki melalui event khusus atau jasa reparasi berbayar, bergantung pada jenis barang. Barang tetap tidak dapat digunakan selama statusnya rusak. Ini memperjelas #22 dan #63, bukan mengganti keputusan bahwa kerusakan hanya terjadi melalui event.
7. **Hewan peliharaan — D:** pemain dapat mengadopsi hewan sendiri dan menanggung seluruh biaya pemeliharaannya, termasuk makanan, perlengkapan, serta perawatan dokter hewan. Perawatan hewan NPC tetap mengikuti #51 dan bantuan pemain bersifat sesuai pilihan.
8. **Pemberian uang kepada NPC — C:** pemain dapat memberikan uang secara bebas kepada NPC yang memiliki hubungan dekat selama saldo mencukupi; NPC bereaksi sesuai hubungan dan situasi. Pemberian tersebut adalah hadiah, bukan pinjaman, sehingga larangan utang pada #6 tetap berlaku.
9. **Inventaris barang rusak — B:** barang yang rusak dipindahkan otomatis ke kategori barang rusak dalam inventaris. Barang tetap dimiliki dan tidak dapat digunakan sampai diperbaiki.

### Hasil audit konsistensi final
- **Tagihan dan rumah:** tidak ada tagihan pribadi rutin; rumah dan utilitas ditanggung keluarga. Pengeluaran pilihan pemain tetap dibayar dari saldo pemain.
- **Laundry:** pakaian sehari-hari dicuci otomatis di rumah tanpa biaya; pakaian khusus dapat dikirim ke laundry profesional dengan biaya standar. Tidak ada konflik antara #40, #50, #47–#48 dan klarifikasi ini.
- **Barang rusak:** kerusakan hanya melalui event (#22); barang rusak tidak dapat digunakan (#63), dipindahkan ke kategori rusak, dan dapat diperbaiki melalui event atau jasa berbayar sesuai jenis barang.
- **Hewan:** NPC dapat memiliki hewan sesuai latar; pemain juga boleh mengadopsi hewan sendiri dan menanggung biaya. Ini tidak mengaktifkan simulasi ledger finansial NPC.
- **Hadiah uang:** pemberian uang kepada NPC dekat dan uang yang diberikan NPC kepada pemain adalah hadiah, bukan pinjaman. Tidak ada sistem utang.
- **Kompetisi dan hobi:** kompetisi gaming gratis (#80); perlengkapan ilustrasi Chiasa tidak menimbulkan biaya khusus (#81); royalti pasif Chiasa tetap ¥50.000/bulan.
- **Ekonomi NPC:** tetap sederhana sesuai #7; respons dan pemberian hadiah mengikuti kategori ekonomi, kepribadian, preferensi, dan hubungan tanpa simulasi saldo individual.
- **Tingkat detail:** ekonomi terintegrasi dengan kalender, hubungan, pekerjaan, dan event (#74), tetapi tetap sistem pendukung dan tidak mendominasi gameplay (#64).

**Kesimpulan audit:** Tidak ada kontradiksi tersisa yang memerlukan pertanyaan tambahan. Batch 20 Sistem Ekonomi #1–#84 beserta klarifikasi #1–#9 dinyatakan lengkap dan konsisten. Tidak perlu membuat pertanyaan #85–#94.

**Changelog v1.29 — 10 November 2026:** Mempertahankan seluruh isi GDD v1.28 dan menambahkan klarifikasi audit #1–#9, menyelesaikan dua area ambigu terkait tagihan rutin dan laundry, serta memperjelas perbaikan barang rusak, adopsi hewan, pemberian uang, dan kategori inventaris barang rusak. Seluruh keputusan Batch 20 #1–#84 tetap berlaku; audit final selesai tanpa menghapus atau mengganti keputusan canon sebelumnya.
