# Rancangan Alur Pembuka Host Chiasa (M01a: C01 → C02 → K01 → N01)

Status: **Menunggu ACC Rancangan Alur** (belum ada file `.rpy` game yang diubah).

## 1. Identitas Alur & Sudut Pandang (POV)
- **Alur:** Pembuka Female Route — Hari Pertama di Tubuh Amamiya Chiasa (`M01a`: `C01` → `C02` → `K01` → `N01`).
- **Host / POV Pemain:** **Amamiya Chiasa** (mahasiswi tahun pertama Fakultas Seni Rupa dan Desain, 19 tahun). Kesadaran Chiasa asli telah hilang permanen; pemain tidak mewarisi ingatan pribadi maupun kemampuan ilustrasi *Shena*, hanya refleks otot sederhana tubuhnya.
- **Tokoh NPC dalam Alur Ini:**
  - **Sistem NTR** (`sistem`): entitas pemberi kontrak 3 tahun dengan layar kaca biru transparan dan ikon garis wajah sarkastis.
  - **Amamiya Koita** (`koita`): kakak tiri tanpa hubungan darah (tahun kedua Sastra, 20 tahun), tinggal satu atap di rumah Amamiya.
  - **Sakurajima Nagisa** (`nagisa`): teman masa kecil empat sekawan & saingan cinta Chiasa asli (tahun kedua Arsitektur, 20 tahun).
  - **Tachibana Miyuki** (`miyuki`): senpai Kedokteran tahun ketiga (21 tahun), anggota kelompok belajar SMA Koita.
  - **Kujo Harumi** (`harumi`): mahasiswi Sains tahun kedua (20 tahun), mantan pengajar kelompok belajar SMA Koita.
  - **NPC yang Disebut/Hadir Lewat Pesan di C01–C02:** **Amamiya Yoshie** (ibu kandung Koita / ibu tiri Chiasa, kerja jarak jauh & sedang bepergian bersama Daisuke), **Ishikawa Haruka** (teman sejurusan Seni Rupa, penggemar berat *Shena*), dan **Higashiyama Mio** (editor novel ringan yang menaungi nama pena *Shena*).

## 2. Koreksi Kontinuitas Kunci (Sesuai Arahan Pengguna)
1. **Larangan Memanggil `"Ko-nii"` Sebelum Pilihan `C02`:**
   - Pada draf lama `C01` di `game/kk_flow.rpy`, cabang B (baris 206) dan cabang C (baris 218) membuat Chiasa langsung memanggil `"Ko-nii"` secara refleks. Ini merusak bobot dramatik `C02` (*"Ko-nii?"*), yang justru menjadi ujian pertama pemain memilih cara memanggil Koita (`A`: memanggil `"Ko-nii"` natural, `B`: memanggil nama `"Koita"`, `C`: menggoda memakai panggilan `"Ko-nii~"` seperti Chiasa asli).
   - **Perbaikan di `C01`:**
     - Pada **Cabang B** (cek ponsel), ketika Koita memanggil dari lantai bawah, pemain menyadari bahwa riwayat chat menyematkan nama `'Ko-nii'`, tetapi lidahnya tercekat dan ia hanya menyahut tanpa sebutan kakak (`"I-iya! Sebentar lagi aku turun!"`).
     - Pada **Cabang C** (nekat keluar kamar dan turun ke bawah), pemain menuruni tangga dan mendapati Koita bercelemek di ruang makan menyapanya `"Pagi, Chi-chan"`. Pemain **belum** memanggilnya `"Ko-nii"` dan **belum** duduk menyelesaikan sarapan di `C01`; pemain hanya membalas gugup tanpa sebutan sambil beralasan hendak membasuh wajah sebentar ke wastafel ketika layar biru Sistem menyergap untuk membacakan kontrak. Dengan demikian, keempat cabang `C01` (`A`, `B`, `C`, `D`) bermuara dengan mulus ke meja sarapan `C02`.
2. **Jangan Membocorkan Pilihan Antar-Event:**
   - `C02` tidak mengasumsikan pemain hanya memilih salah satu cabang `C01`; pembuka `C02` menyambung masuk akal dari semua cabang `C01`.
   - `K01` dan `N01` tidak mengasumsikan opsi tertentu di `C02` sudah dipilih, dan di `N01` pemain belum memanggil Nagisa `"Nacchan-oneechan"` karena pilihan julukan masa kecil itu baru diuji secara mekanik pada event `C04`.

## 3. Daftar Event, Label, dan File `.rpy` yang Disentuh
| Urutan | ID Event | Judul | Label Ren'Py | File Sumber | Waktu & Lokasi |
|---|---|---|---|---|---|
| 1 | **C01** | Terbangun di Kamar Chiasa | `kk_prologue` & `kk_first_morning` (cabang `kk_host == "chiasa"`) | `game/kk_flow.rpy` | Senin, 7 April (Pagi) · Kamar Chiasa & Tangga/Ambang Ruang Makan Rumah Amamiya |
| 2 | **C02** | *"Ko-nii?"* | `kkscene_C02` | `game/kk_chiasa_host.rpy` | Awal April (`kk_hari_n < 19`, pagi hari pertama) · Ruang Makan Rumah Amamiya |
| 3 | **K01** | Senyum yang Terlalu Cepat | `kkscene_K01` | `game/kk_koita_y1.rpy` | Awal April (`kk_hari_n < 19`, `kk_slot in (0,1)`) · Kampus Kouseikan (Gedung Sastra / Area Kantin) |
| 4 | **N01** | Tabrakan di Koridor | `kkscene_N01` | `game/kk_scenes.rpy` | Senin, 7 April (`kk_hari_n == 7`, `kk_slot in (1,2)`) · Kampus Kouseikan (Gedung Arsitektur) |

*Catatan Teknis Mekanik:*
- Pada `kk_prologue` dan `kk_first_morning` (`game/kk_flow.rpy`), cabang `kk_host == "yutaka"` (`Y01`) dipertahankan utuh agar tidak merusak Male Route.
- Pada `kkscene_K01` dan `kkscene_N01`, bila diperlukan detail interaksi spesifik antara Chiasa dengan Koita/Nagisa/Miyuki/Harumi, kita menggunakan percabangan naratif `if kk_host == "chiasa": ... else: ...` di dalam blok dialog/narasi dengan tetap mempertahankan `call kk_scene_enter(...)`, `call kk_family_menu(...)`, dan struktur `if _return == "A": / elif _return == "B": / else:` sehingga kompatibel 100% dengan mesin dan skenario uji.

## 4. Pembagian Bagian Penulisan (8 Bagian Mendalam)

### Bagian 1 — `C01` (Paruh 1): Bangun di Tubuh Asing, Ancaman Awal Sistem, serta Cabang A & Cabang B
- **Cakupan Kode:** `label kk_prologue` (bagian pembuka host Chiasa hingga `call kk_first_morning`) + `label kk_first_morning` untuk `C01` **Cabang A** (*Hampiri cermin dan periksa meja belajarnya*) dan **Cabang B** (*Bongkar isi ponsel di sebelah kasur*).
- **Peristiwa & Perkembangan Emosi:**
  - Sensasi fisik terbangun dari kematian di rel kereta ke dalam kamar bernuansa kayu hangat yang beraroma sabun bunga dan cat akrilik kering; keterkejutan mendengar suara perempuan dari tenggorokan sendiri; sengatan pertama Sistem NTR di pelipis.
  - **Cabang A:** Langkah goyah karena perubahan titik berat tubuh; berdiri di depan cermin meja rias memandangi mata kuning keemasan dan rambut cokelat gelap sepunggung; refleks otot jari yang merapikan pita hitam tanpa diperintah; menyadari identitas Amamiya Chiasa; membuka buku sketsa tebal berisi karya *Shena* lalu mencoba menarik garis dengan pensil mekanik yang berakhir miring, kaku, dan patah.
  - **Cabang B:** Membuka ponsel dengan pemindai wajah; menelusuri saldo ¥400.000, royalti pasif ¥50.000, surel redaksi Mio, pesan Haruka, dan pesan Yoshie; membaca riwayat chat `'Ko-nii'` yang penuh nada manja dan posesif halus; panggilan Koita dari lantai bawah yang membuat pemain panik menyahut **tanpa** sanggup mengucapkan kata `"Ko-nii"`.

### Bagian 2 — `C01` (Paruh 2): Cabang C, Cabang D, serta Kontrak Tiga Tahun Sistem
- **Cakupan Kode:** `label kk_first_morning` untuk `C01` **Cabang C** (*Nekat keluar kamar dan turun ke bawah*) dan **Cabang D** (*Duduk membisu menuntut penjelasan*), dilanjutkan penutup `label kk_prologue` (kontrak 3 tahun Sistem) dan jembatan ke `kk_intro`/`kk_main`.
- **Peristiwa & Perkembangan Emosi:**
  - **Cabang C:** Menyibak selimut untuk memeriksa suara di lantai bawah; tertegun di depan cermin panjang dan papan nama kayu `'Chiasa'` di pintu kamar; kaki yang otomatis melangkahi anak tangga kelima yang berderit; melihat Amamiya Koita secara langsung di balik meja makan memakai celemek; menyahut sapaan `"Pagi, Chi-chan"` secara kaku **tanpa** memanggil `"Ko-nii"`, lalu menahan diri di dekat ambang/wastafel sebelum duduk makan.
  - **Cabang D:** Menolak bergerak dari kasur; menyapu detail kamar mahasiswi Seni Rupa dan pantulan cermin; memaki Sistem setelah menyadari dirinya dilempar ke tubuh adik tiri di manga *Kouseikan*; menerima sengatan hukuman di pangkal leher hingga terbungkuk di kasur; ejekan dingin Sistem saat langkah kaki Koita terdengar di bawah.
  - **Penutup Prolog:** Sistem meresmikan kontrak penyimpangan takdir Koita dengan taruhan nyawa saat wisuda dan memberikan misi pembuka 7 hari.

### Bagian 3 — `C02` (Paruh 1): Meja Sarapan Rumah Amamiya, Ritual Teh Koita, & Cabang A (*"Ko-nii" Natural*)
- **Cakupan Kode:** Pembuka `label kkscene_C02` hingga menu `kk_family_menu("C02", ...)` dan keseluruhan **Cabang A** (`_return == "A"`).
- **Peristiwa & Perkembangan Emosi:**
  - Duduk berhadapan dengan Koita di meja makan kayu rumah Amamiya; detail sarapan pagi (sup miso, telur mata sapi, roti panggang, kotak lauk plastik biru kiriman Yoshie).
  - Koita menanyakan apakah Chiasa mau dibuatkan teh *"seperti biasa"* sambil tangannya otomatis meraih cangkir keramik kuning bermotif kucing dan menjatuhkan gula batu—momen yang menyadarkan pemain bahwa setiap ketidaktahuan kecil bisa membongkar penyamarannya.
  - Ketegangan batin saat harus memilih panggilan pertama untuk Koita di jarak kurang dari dua meter.
  - **Cabang A (`_hook("C02-A")`: `curiga_koita -3`):** Menekan ego dan melantunkan `"Ko-nii"` dengan nada akrab yang lembut; kelegaan Koita yang langsung mengalirkan percakapan pagi tentang kebiasaan susah bangun Chiasa, pesan subuh Yoshie, letak gedung Fakultas Seni Rupa di sayap barat kampus, dan janji bertemu di dekat kantin utama—sementara pemain diam-diam memunguti setiap informasi itu sebagai bekal bertahan hidup.

### Bagian 4 — `C02` (Paruh 2): Cabang B (*Memanggil Nama "Koita"*) & Cabang C (*Menggoda Seperti Chiasa Asli*)
- **Cakupan Kode:** Kelanjutan `label kkscene_C02` untuk **Cabang B** (`_return == "B"`) dan **Cabang C** (`else` / `"C"`) sampai `return`.
- **Peristiwa & Perkembangan Emosi:**
  - **Cabang B (`_hook("C02-B")`: `curiga_koita +8`):** Lidah yang kelu menolak meniru nada manja dan justru memanggil `"Koita"` secara datar; kucuran teh dari teko terhenti; keheningan canggung dan kerutan dahi Koita yang mengira adiknya sedang marah atau sakit; upaya pemain mencari alasan *"sudah jadi mahasiswi"* yang menyisakan tatapan menyelidik di mata Koita sepanjang sisa sarapan.
  - **Cabang C (`_hook("C02-C")`: `jeal koita +5`):** Menutupi kegugupan dengan menyerang lebih dulu lewat senjata utama Chiasa asli—menopang dagu, memanggil `"Ko-nii~"` panjang, dan menggoda apakah Koita ekstra manis karena takut adik tirinya dilirik mahasiswa atau senior di Fakultas Seni Rupa; reaksi Koita yang tersipu sekaligus mengeluarkan sisi posesif halusnya (*"jangan gampang ikut ajakan orang"*); kesalahan kecil pemain yang mengakhiri godaan terlalu cepat untuk kembali makan sehingga Koita terpaku menatap perubahan ritme itu.

### Bagian 5 — `K01` (Paruh 1): Hari Pertama di Kampus, Tiga Sambutan Koita, & Cabang A (*Amati dan Catat Polanya*)
- **Cakupan Kode:** Pembuka `label kkscene_K01` hingga menu `kk_family_menu("K01", ...)` dan keseluruhan **Cabang A** (`_return == "A"`).
- **Peristiwa & Perkembangan Emosi:**
  - Suasana hari/minggu pertama musim semi di Universitas Kouseikan sekitar Gedung Sastra dan area makan siang; kelopak sakura, keriuhan mahasiswa baru, dan posisi Chiasa yang menghampiri meja Koita.
  - Menyaksikan langsung bagaimana gravitasi harem Koita bekerja dalam hitungan menit melalui tiga interaksi beruntun:
    1. **Tachibana Miyuki** yang lewat membawa map praktikum: Koita menegur soal kopi dan mengingat keluhan lambung Miyuki kemarin dengan perhatian hangat yang membuat sang senpai luluh (`"Ara, masih ingat?"`).
    2. **Sakurajima Nagisa** yang datang membawa nampan: Koita menahan kursi dengan lutut, dan ketika Nagisa menagih buku catatan dengan nada ketus, Koita membalas dengan kalimat menggantung (*"Sengaja kubawa supaya punya alasan duduk sama kamu"*) yang melumpuhkan omelan Nagisa.
    3. **Kujo Harumi** yang muncul membawa buku: Koita mengangkat buku rekomendasi Harumi dan meminta waktu khusus untuk mendengar penjelasan Harumi lebih dulu.
  - Pengamatan tajam pemain atas tanda fisik Koita: senyumnya terbit sepersekian detik lebih cepat sebelum kalimat lawan bicaranya selesai, dan matanya selalu sempat memeriksa efek ucapannya.
  - **Cabang A (`_hook("K01-A")`: flag `pola_koita_dikenal`):** Pemain menahan diri di tepi meja, mengurai anatomi janji-janji samar Koita (*"nanti"*, *"kapan-kapan"*) yang tidak pernah punya tanggal tetapi membuat ketiga gadis merasa menjadi prioritas; interaksi ketika Koita menyadari pemain diam memperhatikan lalu menarikkan kursi dengan keramahan tulus yang sama berbahayanya.

### Bagian 6 — `K01` (Paruh 2): Cabang B (*Tegur Terang-terangan*) & Cabang C (*Abaikan dan Bicarakan Jadwal*)
- **Cakupan Kode:** Kelanjutan `label kkscene_K01` untuk **Cabang B** (`_return == "B"`) dan **Cabang C** (`else` / `"C"`) sampai `return`.
- **Peristiwa & Perkembangan Emosi:**
  - **Cabang B (`_hook("K01-B")`: `kk_koita_suspect(5)`):** Pemain memotong suasana hangat meja itu dengan menyentil langsung kebiasaan Koita menebar perhatian khusus kepada tiga perempuan sekaligus; meja mendadak hening; Nagisa refleks membela Koita dengan nada sengit karena gengsi dan ketidaksadarannya, Miyuki tersenyum canggung, dan Harumi mengamati; Koita berlindung di balik kalimat *"Aku cuma ingat hal-hal tentang teman"* sambil mengusap tengkuk, namun sejak detik itu mulai mencuri pandang waspada ke arah pemain.
  - **Cabang C (Tidak ada hook penalti/intel):** Pemain menyimpan penilaiannya sendiri, menarik kursi, dan mengalihkan pembicaraan ke urusan jadwal kuliah minggu pertama; Koita menyambut pengalihan itu dengan lega; Miyuki, Harumi, dan Nagisa berpisah satu per satu dengan membawa potongan harapan masing-masing tanpa melihat pola utuh yang baru saja disaksikan pemain.

### Bagian 7 — `N01` (Paruh 1): Koridor Gedung Arsitektur, Tabrakan dengan Nagisa, & Cabang A (*Bantu Maket & Terima Tantangan*)
- **Cakupan Kode:** Pembuka `label kkscene_N01` hingga menu `kk_family_menu("N01", ...)` dan keseluruhan **Cabang A** (`_return == "A"`).
- **Peristiwa & Perkembangan Emosi:**
  - Siang/sore hari pertama (`7 April`) di koridor Gedung Arsitektur yang beraroma kayu balsa, lem maket, dan kertas kalkir; alasan Chiasa melintas di dekat studio arsitektur (memenuhi tenggat misi pembuka Sistem / melewati gedung tetangga Seni Rupa).
  - Tabrakan di tikungan koridor: sudut map gambar dan tabung draf menghantam bahu; gulungan kertas denah, penggaris skala segitiga, dan potongan maket berhamburan ke lantai—tetapi tangan Sakurajima Nagisa justru melesat lebih dulu menangkap konsol game genggamnya sebelum menyentuh ubin.
  - Reaksi galak Nagisa yang mendadak salah tingkah begitu melihat siapa yang ditabraknya (Chiasa, adik tiri Koita sekaligus rival lamanya) dan menyadari layar konsolnya masih memampang tulisan *"DEFEAT"* dengan suara efek kekalahan yang belum sempat dibisukan.
  - Dalih klasik Nagisa (*"Tadi cuma koneksinya jelek!"*) yang berujung pada tantangan bertanding game untuk menyelamatkan harga dirinya.
  - **Cabang A (`_hook("N01-A")`: `aff +3`, `kelekatan_nagisa +4`, persona `agresif`):** Pemain berjongkok membantu memunguti gulungan gambar dan bagian maket tanpa mengejek, lalu menerima tantangan tandingnya secara serius; keterkejutan Nagisa melihat respons yang tidak menyindir soal Koita, disusul antusiasme kompetitifnya menetapkan janji rematch dan ucapan terima kasih yang gumamannya nyaris tertelan gengsi.

### Bagian 8 — `N01` (Paruh 2): Cabang B (*Minta Maaf Singkat & Buru-buru*) & Cabang C (*Goda Soal Game vs Tabrakan*)
- **Cakupan Kode:** Kelanjutan `label kkscene_N01` untuk **Cabang B** (`_return == "B"`) dan **Cabang C** (`else` / `"C"`) sampai `return`.
- **Peristiwa & Perkembangan Emosi:**
  - **Cabang B (`_hook("N01-B")`: `aff -2`, persona `dingin`):** Pemain hanya memungutkan barang terdekat, meminta maaf singkat dengan nada sopan-berjarak, dan pamit karena sedang buru-buru; Nagisa yang sudah menyiapkan amunisi argumen langsung kehilangan sasaran, menggerutu canggung sambil menepi, namun diam-diam tetap memeriksa lantai untuk memastikan tidak ada barang milik pemain yang tertinggal atau rusak.
  - **Cabang C (`_hook("N01-C")`: `intim +3`, `jeal +3`, persona `genit`):** Pemain menyentil betapa refleks tangan mahasiswi Arsitektur itu jauh lebih sigap menyelamatkan konsol game daripada gambar tugasnya sendiri; wajah Nagisa memerah sampai ke daun telinga di bawah kuncir kembar pirangnya; perdebatan salah tingkah yang berujung tawa setengah kesal dan tantangan ulang yang kini menjadi alasan personal di antara mereka berdua—menutup rangkaian `M01a` dengan benih dinamika baru antara Chiasa dan Nagisa.

## 5. Sambungan ke Event Dinamis, Misi Pembuka, dan Cabang Selanjutnya
- **Misi Pembuka Sistem (`q01`):** Menyelesaikan `N01` pada tanggal 7 April otomatis mencatat kontak pertama dari tiga heroine yang wajib ditemui dalam 7 hari (`q01_met_nagisa`), menyambung langsung ke subfase `M01b` (`Mo01` → `H01` → `S01` → `Mi01` saat Hanami).
- **Event Dinamis yang Dapat Terbuka Sesudahnya:**
  - `C-D01` (*Dapur Jam Dua*): terbuka saat Chiasa berada di Rumah Amamiya pada slot Larut/Dini Hari (`kk_slot in (4,5)`), menyambung langsung dari atmosfer meja makan `C02`.
  - `N-D01` (*Rematch Jam Dua*): terbuka pada malam hari (`kk_slot in (4,5)`) bila `aff` Nagisa mencapai `>= 25` (yang dapat tercapai setelah `N01-A` atau interaksi ringan), menagih janji pertandingan dari `N01`.
- **Tokoh Baru:** Tidak ada penambahan NPC bernama baru pada subfase `M01a` ini; seluruh fokus diberikan untuk menghidupkan suara, gestur, dan ketegangan batin Chiasa, Sistem, Koita, Miyuki, Harumi, dan Nagisa.
