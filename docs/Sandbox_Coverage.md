# Cakupan sandbox Kouseikan

Baseline GitHub 74447c1. Matriks ini mengukur jalur pemain. Explorer pengembang dapat membaca seluruh katalog. Jumlah cabang katalog mencakup alternatif tertulis, termasuk diam atau absen yang tidak selalu berupa tombol.

## Fase dan bukti

| Fase | Hasil | Batas pengujian |
| --- | --- | --- |
| Fondasi | Kalender 36 bulan, konteks lokasi, kalender NPC, biaya aktivitas, memori pertemuan, penurunan relasi dan antrean akibat. Sebelumnya pemicu bisa memaksa NPC hadir dan hari tidak otomatis mengganti bulan. | Kondisi awal kedua host dan kalender diuji. Satu save Yutaka dari ZIP playtest sebelumnya kembali ke layar distrik dengan saldo, tanggal dan pilihan yang sama. Save pengguna lain, lokasi lain dan seluruh versi sebelumnya belum diuji. Sembilan lapisan jadwal dan ekonomi belum lengkap. Janji pertemuan mengubah lokasi, dan ketidakhadiran pemain memengaruhi kepercayaan bila NPC datang. |
| Vertical slice | N01, Mi01, N03, Mi03 memiliki adegan, pilihan, dan pengaruh ke pertemuan selanjutnya. | Driver menjalankan cabang A pada kedua host. Kalender dipercepat setelah pertemuan pertama. |
| Konten | Nagisa, Miyuki dan tawaran kerja Yutaka mendapat pertemuan lanjutan. N04-B dapat mengubah keadaan Nagisa/Koita dua minggu kemudian meski pemain absen. | Driver menguji efek N04-B melalui pencatatan pilihan. Belum menjalankan semua alternatif adegan. Dialog penghubung baru berstatus draft editorial. |
| Ending | Evaluasi saat kelulusan dan epilog berlapis. | E-SI-13, E-SI-02, E-MI-04, E-MI-05, E-HA-01, E-YH-01 dan E-CF-08 diperiksa pada akhir skenario. Referensi kode lain pada resolver belum membuktikan semua prasyarat dapat dibentuk lewat dunia normal. |
| QA | Dari folder proyek jalankan `python tests/run_living.py PATH_SDK` dengan Ren'Py 8.3.2 Windows/Linux x86-64. Driver membuat proyek dan save temporer. | Dijalankan di Windows. Lint, dua host, tindakan, perjalanan, simpan/muat, rollback, kesempatan terlewat dan akibat tertunda. Layar lokasi Hanami dengan enam NPC serta riwayat transaksi dengan tujuh baris diperiksa di 1280×720, 1366×768 dan 1920×1080. Tombol aktivitas dan keluar terlihat pada ketiganya. Layar lain belum diperiksa ulang di semua resolusi. Belum ada benchmark satu sesi penuh tiga tahun. |

## Iterasi Hanami, Golden Week dan Harumi

Pada akhir pekan Hanami, ada pertemuan terpisah dengan Harumi di perpustakaan sains, Moeka di piknik, dan Shiori di dekat papan shogi. Pada 3–6 Mei, stasiun menawarkan perjalanan ke ryokan. NPC bepergian meski pemain tinggal di kota. Uji Yutaka memeriksa percakapan, efek dan jam pada empat peristiwa Golden Week. Uji Chiasa memeriksa kedaluwarsa. Skenario memakai kalender dipercepat dan panggilan interaksi produksi. Belum seluruh tombol perjalanan dan alternatif respons diuji manual.

Membantu Harumi memasak membuka H-D05 pada pertemuan selanjutnya. E-HA-01 mensyaratkan kejelasan emosi, dukungan nyata saat ia menamai perasaannya, dan riwayat tanpa Force. Di penginapan, mengalah sengaja pada Nagisa dapat membuka N-D08, ketika ia memutar ulang permainan. Setelah balasan Koita, kesempatan N-D03 hanya terbuka pada malam turunnya harapan Nagisa.

H08-A membuka kemungkinan teh larut malam di asrama, bila Harumi hadir. H09 mengingat percakapan tahun baru. Pemilihan slot kegiatan di ryokan, kunjungan tahun baru tanggal 1–3, dan waktu tempuh 60 menit merupakan penjadwalan prototipe. Besar efek memakai rentang Sistem_Cabang_dan_Poin §2.2. Dialog penghubung memerlukan tinjauan editorial.

Di kamar sendiri, pemain dapat memasang alarm untuk 20 menit, 90 menit, 6, 8, atau 10 jam. Ponsel memiliki mode senyap, normal, dan siaga serta daftar kontak prioritas dari orang yang pernah ditemui. Mode ponsel memakai pemicu pesan Nagisa, Miyuki, ibu Yutaka, dan editor Mio. Kualitas tidur di lokasi lain, panggilan darurat, dan seluruh penyebab bangun masih parsial.

## Menjalankan ulang pemeriksaan

- `python tests/check_catalog.py` memeriksa ID, duplikasi, label adegan dan angka matriks.
- `python tests/run_living.py PATH_SDK` menjalankan lint produksi, tiga perjalanan umum, tiga perjalanan khusus keluarga, dan satu perjalanan klinik Yutaka.
- `python tests/run_living.py PATH_SDK FOLDER_GAMBAR` mengambil gambar layar Hanami ramai pada tiga ukuran target.
- `python tests/run_save_upgrade.py PATH_SDK ZIP_PLAYTEST_SEBELUMNYA` membuat save baru pada versi lama yang dipercaya dan memuatnya pada versi sekarang. Sampel yang diuji berasal dari paket SandboxSpring sebelum iterasi keluarga dan ilustrasi.
- ZIP Windows iterasi ini lolos pemeriksaan integritas. Executable hasil ekstraksi memulai renderer. Skenario panjang berjalan di proyek temporer dengan source produksi.

## Keluarga Kisaragi

Di lobi apartemen pada malam hari, Yutaka bisa bertemu ayahnya ketika hubungan keluarga masih dingin. Setelah hubungan membaik, pesan dari ibu dapat masuk, termasuk ketika Yutaka beristirahat. Panggilan ayah pada M13, makan Natal di rumah Amamiya pada M21, dan jawaban karier pada M31 tercatat dalam perjalanan. E-YH-01 memerlukan Yutaka lolos evaluasi, memilih perusahaan keluarga, dan hubungan Kisaragi ≥60. Dasar 30 dan ambang 40/60 berasal dari Alur_Cabang/08. Jam malam, kedatangan di apartemen untuk panggilan M13, dan bobot respons 5–10 adalah penjadwalan dan penyetelan prototipe. Y13 kini membangun bond keluarga Amamiya (dasar 45; makan bersama +15, bicara dari hati +20, pamit −15) yang dibaca E-YH-03 "Keluarga Pilihan" saat epilog, didahulukan E-YH-01 bila Yutaka memilih perusahaan keluarga dengan Kisaragi ≥60. Dasar 45 dari Master Canon §5.3; ambang 60 dan bobot 15/20 adalah penyetelan prototipe dari Alur_Cabang/08. **Gerbang Koita Success** (cabang Y13 yang lain, saat Chiasa-NPC bersama Koita) masih diblok: butuh subsistem Chiasa-NPC-dengan-Koita dan simulasi romansa Koita yang belum ada — menambahkannya adalah mekanik baru, bukan menyambung yang sudah terdokumentasi.

Tiga skenario desktop mencapai epilog dengan kalender dipercepat. Di antara ketiganya, pemeriksaan mencakup E-SI-13, E-SI-02, E-MI-04, E-MI-05, E-HA-01, E-YH-01 dan E-CF-08. Riwayat transaksi dan navigasi halaman lama diuji pada ketiga resolusi.

Di pesta rumah sakit (M09), berpura-pura menjadi pasangan membuka percakapan khusus saat pertemuan keluarga M21. Duduk di samping Miyuki mempertahankan sandiwara. Meminta Takeru menunda percakapan membuatnya bertanya langsung kepada Miyuki dan membongkarnya. Menceritakan asal sandiwara memberi Miyuki kesempatan mengaku. Tiga hasil berasal dari Alur_Cabang/01 §Mi18; kalimat percakapan adalah draf editorial. Save yang sudah melewati Mi18 mempertahankan keputusan tersimpan.

Tiga skenario keluarga memakai Chiasa. Driver mempercepat tanggal dan memilih seed kehadiran, lalu memakai tombol NPC di layar lokasi serta pilihan adegan sebenarnya. Di M33 pemain bisa bertamu ke rumah Nagisa, pamit di depan pintu, atau melewatkan kunjungan. Jika lamaran Mi25 muncul, pemain meminta Takeru berhenti mendesak. Pengujian memeriksa E-MI-13, E-MI-14 dan E-NA-07 pada hasil evaluasi wisuda. Pada M31, saat Nagisa di rumah, Haruto bisa mendengar cerita pemain sendiri. Kejujuran juga membuka E-NA-07 meski pemain absen di N22. Bohong atau konfrontasi memberi akses ke meja kamar host pada M34 (N23). Menyimpan Koko membuka N-D09. Alternatif tahap 4 memakai percakapan dengan Nagisa. Besar perubahan kelekatan (+10/+5/−5) adalah setelan prototipe. Pemicu N21 lebih awal dan dampak kecemburuan khusus pada Moeka masih terbuka. E-CF-01 mengikuti hasil romansa heroine dan kelulusan Chiasa, termasuk bila pekerjaannya sebagai ilustrator juga berhasil.

## Ilustrasi Chiasa dan penghasilan

Mio menawarkan proyek pada M08. Bila diterima, ia bisa mengirim pesan jam 23. Pada M16, menyewa ilustrator dapat membuat Haruka membandingkan sketsa. Chiasa bisa belajar dengannya di studio atau berlatih di rumah pada malam hari. Tangan yang gemetar mengubah pilihannya. Pada M20, Shiori dapat datang ke studio untuk pameran. Ambang kemampuan 80 membuka E-CF-08 bagi Chiasa yang lolos evaluasi. Hari pameran di akhir pekan, durasi latihan 60 menit dan kenaikan 1–3 poin per sesi merupakan penyetelan prototipe dari Alur_Cabang/06 dan Sistem_Cabang_dan_Poin. Adegan dan dialog penghubung adalah draft editorial.

Saldo awal mencakup awal perjalanan. Setiap pergantian bulan berikutnya membukukan satu uang saku Yutaka ¥150.000 atau dua transaksi Chiasa (uang saku ¥50.000 dan royalti ¥50.000). Royalti dibayar meski proyek baru ditolak. Panel Status memberi akses ke saldo dan riwayat per halaman. Save lama mempertahankan saldo dan mencatat transaksi mulai saat dimuat. Tidak ada pembayaran retroaktif.

## Keluarga Saionji dan kepercayaan Shiori

Pada malam 24 Desember tahun pertama, temui Shiori di rumah ketika ia ada di sana. Jika ikut makan, kembalilah pada hari lain dan ajak dia bicara di rumahnya. Ibunya mengingat tamu Natal, dan Shiori membicarakan kembali jawaban saat minum teh ketika menyiapkan keputusan warisan pada M25. Mengirim hadiah atau langsung pulang memberi hasil berbeda.

Pada Chiasa, menyangkal mengenal Shena di pameran M20 memberi Shiori alasan untuk bertanya di klub catur pada bulan yang sama. Mengaku tentang satu kebohongan mencegah eskalasi; menyangkal atau pergi mengaktifkan tahap 2 Shiori. Bila kebohongan Chiasa tentang Shena terbongkar dan tidak diselesaikan, E-SH-13 menyasar karier Shena. Dukungan terhadap rencana kariernya dapat mencapai E-SH-07 jika jalur balas dendam tidak aktif. Sumber lain bagi penemuan S13 dan akibat setelah Valentine masih parsial. Lokasi percakapan dan dialog merupakan penyajian prototipe berdasarkan Event_Shiori, Alur_Cabang/05, dan Milestone_3_Tahun M09.

Setelah pertemanan di klub (M12), coba temui Shiori lagi pada Minggu sore di studio setelah menyangkal soal Shena pada Sabtu pameran M20. Mengaku sebelum ia menemukan bukti menghapus satu entri; alasan lain yang kemudian terbongkar di klub dihitung dua kali. Bila konfrontasi membuka Revenge, ia tetap tersenyum saat Natal kedua dan duduk di depan papan kosong pada 14 Februari. Hatsumode pada 1–3 Januari bisa ditemui di kedua keadaan. Jadwal jam kunjungan serta dialog adalah penyajian prototipe dari Event_Shiori dan Alur_Cabang/05. Nilai Trust S09 (+5/0/−5) adalah setelan prototipe.

Pada tahap 3, perhatikan papan di Klub Catur saat Shiori tidak berada di sana. Langkah balasan diingat ketika berbicara di rumah Saionji pada Juni tahun ketiga. Dalam S18 Kuroiwa menghentikan upaya menghapus berkas; masuk tanpa izin tercatat. Menjelaskan keadaan kepada pihak terdampak sebelum penyerahan berkas mencatat perbaikan tanpa menaikkan tahap; pergi membiarkan Shiori meneruskan pengumpulan. S22 dan dampak akhir dari upaya perbaikan masih parsial.

Pada 7 Juli tahun ketiga, datangi Taman Kampus pada siang, sore, atau malam dan pilih sendiri siapa yang diajak bicara. Shiori, Harumi, Nagisa, dan Moeka memiliki tanzaku berbeda; jadwal absen dan janji sebelumnya tetap berlaku. Tanggal, tempat, dan slot adalah penyajian prototipe M28. Catatan canon: Event_Shiori S18 membatasi ending setelah titik tanpa balik ke Distorted/Bad, sementara Alur_Cabang/05 dan Katalog Ending menyebut gencatan senjata netral melalui pengakuan di S22/S24. E-SH-03 menunggu penetapan prioritas.

## Hari kecil Miyuki: puding dan pastry

Pada malam hari, tandai Miyuki sebagai kontak prioritas atau gunakan mode Siaga, lalu tidur setelah hubungan hangat dan `dimanja` mencapai 50. Sekitar pukul 01:00 ia meminta puding konbini. Menemani menaikkan `dimanja` 10, mengantar lalu pergi 5, menolak menurunkan 5, dan menertawakan menurunkan 10, sesuai Alur_Cabang/01 baris Mi-D01. Pilihan itu diingat: pada obrolan berikutnya Miyuki menyinggungnya satu kali. Dalam mode Senyap pesan terlewat, tidak ada perubahan poin, dan ia tidak pernah menyinggungnya.

Setelah memuji pastry Miyuki di Kafe Komorebi pada hari Sabtu dan Affection mencapai 55, ia dapat membawa pastry bertuliskan nama pemain. Memakannya di depan Koita (hanya muncul bila Koita ada di sana) membuat Koita mencatatnya dan menyinggungnya sekali pada obrolan berikutnya. Membagikannya ke semua orang saat Nagisa berada di tempat yang sama menaikkan cemburu Nagisa 5 (setelan prototipe) dan Nagisa menyinggungnya sekali. Menyembunyikan pastry tidak terlihat siapa pun. Di jadwal biasa Nagisa tidak pernah berada di satu tempat dengan Miyuki, sehingga cemburu ini hanya muncul pada acara bersama atau lewat janji. Kalimat percakapan adalah draf editorial. Tes menaikkan poin dan Affection serta menandai pujian pastry secara langsung sebagai prasyarat, dan memakai janji untuk menempatkan Nagisa di kafe. Pesan puding, layar lokasi, tombol Miyuki, panel pilihan dan hook memakai kode produksi. Mi-D12 membutuhkan dimanja dan Trust ≥70 serta ketiga luka <30. Miyuki sendiri menolak ibunya dan tekanan Hayase turun 30. Satu skenario memeriksa batas numerik. Skenario klinik terpisah membangun kesiapan dari awal melalui janji besok dan makanan yang dibeli dengan saldo pemain, kemudian memeriksa penolakan dan jendela Mi25 pada Natal. Pada perjalanan Yutaka yang diuji, ia membeli 15 makanan dan memenuhi tujuh janji; angka tersebut adalah hasil satu perjalanan. Kalender dipercepat. Luka Koita dan diri memakai dasar canon 10 dan 15; perkembangan lengkapnya masih parsial. Kenaikan luka pemain +5 setelah ejekan puding dan perubahan Mi11 (+5 dimanja atau +2 intim) adalah penyetelan prototipe.

Pada Sabtu malam ketika tekanan perjodohan sudah terasa (`omiai_takeru` ≥ 40), bicara dengan Miyuki bisa membuka telepon ibunya tentang Hayase. Pura-pura tidak mendengar menambah `omiai_takeru` 3, bertanya setelahnya menambah Trust Miyuki 5, dan meminta bicara dengan ibunya menurunkan `omiai_takeru` 10 serta menambah Trust 3. Nilai ini setelan prototipe; arahnya mengikuti Alur_Cabang/01. Lamaran Mi25 membaca `omiai_takeru` ≥ 70 dan pembacaan itu sudah diuji di perjalanan lama, tetapi tes Mi-D04 hanya memeriksa nilainya, bukan lamaran sesudahnya. Miyuki menyinggung pilihan itu sekali pada obrolan berikutnya. Mi-D07 (Takeru di kafe) belum terhubung karena Takeru belum punya jalur kehadiran sendiri.

## Teh dan keluarga Kansai Harumi

Pada M3 saat hujan, temui Harumi di Gedung Sains & Lab pada slot pagi atau siang untuk H02 (teh di bawah atap); memuji tehnya menambah Trust. Pada M6, slot siang di Kafe Komorebi membuka H05 (reuni rumah teh); menanyakan rencananya setelah lulus menambah `orang_tua_kujo`. Pada akhir pekan M14 di Stasiun Kouseikan-mae, ikut menemaninya pulang (H10-A) menandai `harumi_kansai_ikut` dan menaikkan `orang_tua_kujo` 15. Sesudah itu, surat ibunya (H-D07) muncul saat bicara dengan Harumi di Perpustakaan Pusat; membantunya membalas menaikkan `orang_tua_kujo` 10. Pada Natal M33 di Stasiun, H22 (Natal pulang) terhubung lewat peta, window dan jadwal, dan ketiga respons kini diuji lewat layar.

`orang_tua_kujo` bermula 30 dan di-seed ulang untuk save lama di `after_load`. Bila mencapai 60 tanpa Force, dan jalur kejelasan emosi (E-HA-01) tidak tercapai, epilog Harumi menjadi E-HA-09 "Rumah Teh di Kansai". Pada perjalanan romansa (Yutaka dan Chiasa seniman) E-HA-01 tetap menang karena diperiksa lebih dulu. Nilai angka adalah setelan prototipe; arahnya mengikuti Alur_Cabang/03. Rute eksploitasi (Ogawa, lab malam, transaksional) tidak disentuh.

## Klinik Miyuki dan kursi perpustakaan

Pada awal tahun kedua, cari Miyuki di Gedung Kedokteran (M13), lalu di rumah sakit (M14). Memulai klinik memengaruhi jadwal malamnya. Aksi membawakan makanan dan memenuhi janji yang dibuat sehari sebelumnya dapat membuka Mi-D12. Bila Miyuki sedang di perpustakaan dan kelelahannya mencapai 60, layar lokasi menawarkan duduk di sebelahnya. Menunggu sampai ia bangun memakan dua jam dan menurunkan kelelahan lima poin. Versi kereta dan kemungkinan foto sampai ke Mei belum tersambung. Waktu untuk membangunkan atau mengambil foto (5 menit), pindah tempat (15 menit), bonus belajar dan intimasi adalah setelan prototipe.

Saat M06, ajak Miyuki bicara di Gedung Kedokteran. Ia bisa mengingat dukunganmu ketika rotasi pediatri dimulai pada M25. Temui ia di Rumah Sakit Tachibana selama rotasi; bila afeksi sudah Sedang atau lebih, ia dapat bercerita tentang pasien kecilnya. Menemani atau menelepon mendukung karier dan mengurangi luka terhadap diri; menolak membiarkan keduanya tetap. Slot rotasi M25 dan bobot perubahan ±5 adalah penyajian prototipe. Pada malam 14 September tahun ketiga temui Miyuki di RS. Hasil CBT ditetapkan sekali pada pergantian hari ke tanggal 15, walaupun pemain tidak datang. Karier <40 dan kelelahan ≥75 masing-masing menambah satu faktor risiko; dukungan malam ujian mengimbangi satu faktor. Tanggal dan penggabungan kedua faktor adalah penyetelan prototipe, bukan keputusan canon baru. Save lama yang sudah melewati pengumuman tidak diberi hasil retroaktif. E-MI-02 tersedia bila karier lancar, CBT lulus, tahap ≤2 dan tidak ada hasil hubungan lain yang sudah terhubung. Cabang Koita dan cuti belum lengkap.

## Tahun pertama Nagisa yang hangat

Empat event awal Nagisa kini terhubung lewat tombolnya di layar lokasi, semuanya sebelum gerbang yandere (N14): N05 (M6, foto berempat dan boneka Koko) di Studio Arsitektur, N07 (Natal M9, memeluk Koko) di Rumah Sakurajima, N08 (Valentine M11, coklat gosong) dan N09 (White Day M12) kembali di studio. Meminta cerita tentang Koko menambah Intim dan menandai `koko_dikenal`; merayakan Natal bersamanya menambah `kelekatan_nagisa` 10; membantu membuat ulang coklat menambah `kelekatan_nagisa` 5; memberi hadiah kecil menurunkan `gengsi_nagisa` 5. Boneka Koko menyambung ke rangkaian yang sudah ada (N-D09 reparasi, N23). N10 (M13, telepon kakak Haruto) di studio menambahkan intro hangat Haruto: menanggapinya dengan baik menandai `haruto_kenal`, yang memunculkan satu kalimat callback saat Haruto datang di N21 (M31). Keempatnya diuji lewat layar pada tiga perjalanan utama. Nilai angka adalah setelan prototipe; arahnya mengikuti Event_Nagisa dan Alur_Cabang/02. Bagian posesif (cek ponsel, ultimatum, sabotase) tidak disentuh.

## Lapisan kesadaran Koita (Tahun 1)

Koita bukan sekadar target; ia aktor yang membalas. Enam event Tahun 1 kini terhubung lewat tombol Koita di tempat ia biasa berada: K01 (M1, pola sapaan) di Gedung Sastra, K03 (M4, tanzaku) di Gedung Sastra, K06 (M6, foto reuni) di Kafe Komorebi, K09 (M10, omikuji) di Kuil saat Tahun Baru, K10 (M11, Valentine) dan K11 (M12, White Day) di Gedung Sastra. Membaca pola menandai `pola_koita_dikenal`; tanzaku dan omikuji menaikkan `ketakutan_koita`; menyamakan hadiah menaikkan `koita_curiga_1`. Semua observasional dan aman. Gerbang rute BL (Male) dan Koita Success (Female) di K04-D dan K10-A sengaja TIDAK dibangun di sini; event dimainkan netral. Nilai angka adalah setelan prototipe; arahnya mengikuti Event_Koita. Tahun 2 menambah K12 (M14, telepon terlewat), K14 (M18, rumor Mei), K15 (M19, panik pertama yang menaikkan `koita_sadar`), dan K16 (M21, malam ia bercerita tentang ayahnya). Cabang gelap (dorong rumor, manfaatkan kepanikan atau kerapuhan) ditulis sebagai konsekuensi singkat tanpa metode. Tahun 3 menutup arc: K18 (M24, daftar nama), K19 (M25, skripsi yang lebih jujur bila dibantu), K23 (M31, tawaran penerbit), K24 (M32, pidato klub), K25 (M33, Natal sendirian yang menandai `koita_natal_ditemani` atau `koita_sendiri`). Gerbang rute BL (K17/K22) dan Koita Success tetap tidak dibangun.

## Shiori awal: senyum yang tak terbaca

Lima event awal Shiori kini terhubung di Klub Catur (tempat ia rutin berada pada slot siang): S03 (M3, berbagi payung dengan Koita), S06 (M8, turnamen), S08 (M11, peringatan satu tahun dengan Koita), S11 (M16, peringkat ujian), S12 (M18, rumor Mei). Membela atau bersaing jujur menaikkan `respek_shiori` dan Trust; menawarkan menyontek (S11-C) menambah `daftar_kebohongan_shiori` yang dibaca S13; mengganggu atau menyebar rumor menaikkan `marah_shiori`. Cabang gelap ditulis sebagai konsekuensi singkat tanpa metode. Nilai angka adalah setelan prototipe; arahnya mengikuti Event_Shiori dan Alur_Cabang/05.

## Miyuki awal: kerentanan dan pemulihan

Tiga event awal Miyuki terhubung: Mi04 (M5, tali obi) di Gedung Kedokteran, Mi08 (M8, Sena mengenalkan psikolog Sato) di Rumah Sakit Tachibana, Mi10 (M10, omikuji 'kesendirian') di Kuil saat Tahun Baru. Mendukung konsultasi Sato (Mi08-A) menandai `miyuki_sato_dikenal` dan menurunkan `luka_miyuki_diri`, menyambung jalur pemulihan yang dibaca arc klinik/CBT. Menghibur saat omikuji menaikkan Trust; memanfaatkan kerapuhannya (Mi10-C) menaikkan `luka_miyuki_diri` sebagai konsekuensi singkat tanpa metode. Nilai angka adalah setelan prototipe; arahnya mengikuti Event_Miyuki.

## Yutaka menjaga penyamaran

Pemain menghuni tubuh Yutaka; tingkah yang meleset dari Yutaka asli menaikkan kecurigaan. Tiga event host (fire saat masuk lokasi, hanya pada perjalanan Yutaka) kini terhubung: Y02 (M1, kunjungan pertama ke Rumah Amamiya; masuk seolah rumah sendiri menaikkan `curiga_chiasa`), Y05 (M5, tantangan game Nagisa; kalah terang-terangan menaikkan `curiga_nagisa` karena 'Yutaka tidak pernah kalah'), Y10 (M16, jam tangan dari Daisuke). Variabel `curiga_*` di-seed lewat helper tanpa migrasi save. Nama dan arahnya mengikuti Event_Yutaka; angka adalah setelan prototipe. Gerbang rute BL (Y07-D, Y08-D) tidak dibangun. Chiasa punya lapisan penyamaran paralel: C02 (M1, sapaan 'Ko-nii' ke Koita), C03 (M4, tanzaku), C04 (M5, julukan 'Nacchan' untuk Nagisa), C08 (M13, Haruka menyadari gaya gambar berubah; menaikkan `curiga_haruka` dan berisiko membongkar nama pena Shena). Gerbang yuri/Koita Success (C06-D, C07) tidak dibangun.

## Pedoman playtest

Untuk membandingkan dua perjalanan Nagisa, simpan sebelum bertamu ke Rumah Sakurajima pada akhir pekan Oktober tahun ketiga (M31). Ajak Nagisa bicara saat ia ada di rumah. Pada save pertama, jawab pertanyaan Haruto dengan jujur dan lewatkan undangan Natal. Pada save kedua, bohong dan pulanglah ke kamar sendiri pada Januari (M34). Periksa meja, tentukan apa yang akan dilakukan dengan Koko, lalu lihat apakah masih ada yang bisa dikerjakan di meja. Catat juga apa yang terjadi bila bonekanya tidak disimpan. Di wisuda, pertemuan dengan Haruto dan makan Natal mempunyai narasi keluarga yang berbeda. Skenario otomatis memeriksa pilihan melalui layar percakapan dan memakai aksi meja langsung; pengujian manual tombol meja masih terbuka.

Mulai permainan baru, pilih salah satu tubuh, lalu kunjungi distrik kampus. Coba makan, berbicara dengan seseorang, kembali ke tempat itu pada waktu berbeda dan simpan sebelum sebuah keputusan. Muat kembali dan amati perbedaan respons. Untuk laporan sertakan tubuh, tanggal/jam, lokasi, tindakan dan perubahan yang terlihat. Gunakan save terpisah untuk membandingkan dua perjalanan.

Untuk mencoba Golden Week, datangi stasiun pada 3–6 Mei, pilih berangkat, lalu lihat siapa yang berada di lobi atau dapur. Untuk membandingkan, gunakan save kedua dan tetap di kota hingga liburan selesai.

## Ketidaksesuaian sumber

- K02: Milestone_3_Tahun M02 menyebut Koita sekamar dengan dua heroine. Event_Koita K02 menyebut satu heroine sesuai kesiapan. K02 belum diaktifkan. Empat event lain di Golden Week bisa ditemukan.
- GDD menyebut Master Canon v11.1. File yang ditemukan adalah v11. Isi v11.1 belum dapat dibandingkan.
- Efek kelelahan Mi03-A memakai −8 dari hook existing dan Alur_Cabang/01; contoh di Sistem_Cabang_dan_Poin §6 memakai −5. Angka existing dipertahankan sampai prioritas dua rujukan dikonfirmasi.

## Matriks katalog

Status implementasi dan bukti uji merupakan dua kolom terpisah. **implemented** menandai adegan slice dengan jalur A teruji, **partial** untuk koneksi yang masih mempunyai kondisi atau alternatif yang perlu diperiksa, **data-only** untuk entri tanpa pemicu dunia/resolver yang diidentifikasi. **blocked** berlaku bagi perbandingan canon v11.1 yang berkasnya belum tersedia. **untested** berarti belum dibuktikan melalui skenario desktop ini.

### Event utama

182 dari 190 ID mempunyai referensi langsung dalam alur atau resolver. Katalog memuat 553 alternatif tertulis pada seluruh ID.

| ID | Implementasi | Bukti |
| --- | --- | --- |
| C01 | implemented | Pembukaan A, Chiasa |
| C02 | partial | A/B enter Rumah Amamiya M1; 'Ko-nii', curiga_koita |
| C03 | partial | A enter Rumah Amamiya M4; tanzaku, harapan_pemain |
| C04 | partial | A enter Rumah Amamiya M5; 'Nacchan', kenangan Nagisa |
| C05 | partial | A dan B, dua perjalanan Chiasa |
| C06 | partial | Host Chiasa Rumah Amamiya M9; Natal, arah rute (B yuri/C Nagisa) |
| C07 | partial | Host Chiasa M11; Valentine, gerbang yuri/Success/Yutaka |
| C08 | partial | A/B enter Studio M13; Haruka curiga, curiga_haruka |
| C09 | partial | A dan B, dua perjalanan Chiasa |
| C10 | partial | Host Chiasa M17; rival Nagisa yukata |
| C11 | partial | A, Chiasa di pameran |
| C12 | partial | Host Chiasa M21; orang tua pulang, gerbang Koita Success |
| C13 | partial | Host Chiasa M23; hari pengakuan, arah rute (A/B/C) |
| C14 | partial | Host Chiasa M26; perjalanan perpisahan, mempersempit jalur |
| C15 | partial | Host Chiasa M29; kembang api Nagisa, jalur yuri |
| C16 | partial | Host Chiasa Studio M31; cover vs skripsi, karier |
| C17 | partial | Host Chiasa Studio M32; pameran tunggal |
| C18 | data-only | untested |
| K01 | partial | A di Gedung Sastra M1; baca pola, pola_koita_dikenal |
| K02 | partial | Milestone onsen bulan 2, talk Koita Taman luar ryokan; 4 pilihan, D sabotase=konsekuensi+risiko curiga (tanpa metode) |
| K03 | partial | A/C di Gedung Sastra M4; tanzaku, ketakutan_koita |
| K04 | partial | Talk koita Gedung Sastra M5; pilih siapa, D pointer rute |
| K05 | partial | Talk koita Rumah Amamiya M5; dapur vila, koita_curiga |
| K06 | partial | A di Kafe M6; foto bukti |
| K07 | partial | Talk koita Gedung Sastra M8; Matsuda sekutu/lawan |
| K08 | partial | Talk koita Gedung Sastra M9; sabotase Natal (konsekuensi) |
| K09 | partial | A di Kuil M10; omikuji, ketakutan_koita |
| K10 | partial | A di Gedung Sastra M11; coklat (gerbang rute tidak dibuka) |
| K11 | partial | A/C di Gedung Sastra M12; hadiah sama, koita_curiga_1 |
| K12 | partial | A di Gedung Sastra M14; telepon terlewat, Trust |
| K13 | partial | Talk koita Gedung Sastra M17; yukata pilihan |
| K14 | partial | A di Kafe M18; bantah rumor (C abstrak) |
| K15 | partial | A di Gedung Sastra M19; koita_sadar naik |
| K16 | partial | A di Rumah Amamiya malam M21; akar sifat, Trust |
| K17 | partial | Talk koita Gedung Sastra M23; hari pengakuan, D/E pointer rute |
| K18 | partial | A di Gedung Sastra M24; daftar nama dibaca |
| K19 | partial | A di Gedung Sastra M25; skripsi lebih jujur |
| K20 | partial | Talk koita Rumah Amamiya M26; atap jujur |
| K21 | partial | Talk koita Rumah Amamiya M29; yukata terakhir, B pointer BL |
| K22 | partial | Talk koita Gedung Sastra M29; malam terakhir, pointer ending BL |
| K23 | partial | A di Gedung Sastra M31; tawaran penerbit |
| K24 | partial | A di Gedung Sastra M32; pidato dihadiri |
| K25 | partial | A di Rumah Amamiya Natal M33; ditemani vs sendiri |
| K26 | data-only | untested |
| K27 | data-only | untested |
| Y01 | implemented | Pembukaan A, Yutaka |
| Y02 | partial | A/B enter Rumah Amamiya M1; penyamaran, curiga_chiasa |
| Y03 | partial | Host Yutaka Apartemen M1; julukan Nagisa, curiga |
| Y04 | partial | Host Yutaka M4; kuis dadakan, IPK |
| Y05 | partial | A/B enter Apartemen Yutaka M5; skill game, curiga_nagisa |
| Y06 | partial | Host Yutaka M8; Daichi membocorkan, intel |
| Y07 | partial | Host Yutaka M9; Natal sepi, arah (A Amamiya/D Koita) |
| Y08 | partial | Host Yutaka M11; Valentine, D rantai BL |
| Y09 | partial | A pada Yutaka; tertutup untuk Chiasa |
| Y10 | partial | A enter Rumah Amamiya M16; jam tangan Daisuke |
| Y11 | partial | Host Yutaka Rumah Amamiya M17; yukata Chiasa, curiga |
| Y12 | partial | Host Yutaka M20; pameran Chiasa |
| Y13 | implemented | A pada Yutaka; flag dibaca E-YH-03; tertutup untuk Chiasa |
| Y14 | partial | Host Yutaka M23; hari pengakuan, arah rute |
| Y15 | partial | Host Yutaka M26; jarak dari rumah Kisaragi |
| Y16 | partial | Host Yutaka Amamiya M29; kembang api Chiasa |
| Y17 | partial | Cabang A, Yutaka; tertutup untuk Chiasa |
| Y18 | partial | Host Yutaka M32; pameran tunggal Chiasa |
| Y19 | data-only | untested |
| Mo01 | partial | A, Chiasa |
| Mo02 | partial | A, Yutaka |
| Mo03 | partial | Talk moeka Kantin Pusat M3; janji terlupa, stres- |
| Mo04 | partial | Talk moeka M5; pingsan lupa makan, intim |
| Mo05 | partial | Talk moeka M6; kabar rumah, keluarga diketahui |
| Mo06 | partial | Talk moeka M7; gerbang Kuga (A mulai jerat) |
| Mo07 | partial | Talk moeka Kantin M8; peragaan pertama |
| Mo08 | partial | Talk moeka M9; Natal + adik, kenal keluarga |
| Mo09 | partial | Talk moeka M10; hatsumode doa ayah |
| Mo10 | partial | Talk moeka M11; coklat 3 adik |
| Mo11 | partial | Talk moeka M15; ponsel mati, jendela intervensi 1, stage 1 |
| Mo12 | partial | Talk moeka M16; IPK turun, beasiswa terancam |
| Mo13 | partial | Talk moeka M18; foto beredar, topeng |
| Mo14 | partial | Talk moeka M19; topeng tebal, stage 2 |
| Mo15 | partial | Talk moeka M20; surat beasiswa, jendela 2 |
| Mo16 | partial | Talk moeka M22; nilai kedua |
| Mo17 | partial | Talk moeka M23; menghilang grup chat, stage 3 |
| Mo18 | partial | Talk moeka M26; Rina bicara, sekutu/lawan |
| Mo19 | partial | Talk moeka M27; barang dibagikan, jendela 3, tanda bahaya |
| Mo20 | partial | B: menulis bersama Moeka |
| Mo21 | partial | Talk moeka M29; tertawa keras, tanda bahaya |
| Mo22 | partial | Talk moeka M30; Ren menelepon, jendela 4 |
| Mo23 | partial | Talk moeka M31; kontrak Kuga |
| Mo24 | partial | Talk moeka M32; peragaan terakhir |
| Mo26 | partial | Talk moeka M33; Natal sunyi, jendela intervensi akhir |
| Mo25 | partial | Talk moeka M34; klimaks bercabang (tertolong vs kehilangan), tanpa metode |
| H01 | partial | A, kedua host |
| H02 | partial | A lewat tombol Harumi di Gedung Sains, M3 |
| H03 | partial | C, Yutaka |
| H04 | partial | Talk harumi Perpus M5; teh vila, data kedekatan |
| H05 | partial | B di Kafe Komorebi, M6; menambah orang_tua_kujo |
| H06 | partial | Talk harumi M7; Ogawa muncul, ogawa_aktif |
| H07 | partial | Talk harumi M9; Natal di lab |
| H08 | partial | A, kedua host |
| H09 | partial | A, kedua host |
| H10 | partial | A di Stasiun, M14; ikut pulang ke Kansai |
| H11 | partial | Talk harumi M16; beasiswa, stage 2 |
| H12 | partial | Talk harumi M19; variabel sosial, transaksional |
| H13 | partial | Talk harumi M20; dana lab beku, gerbang rute (B lapor) |
| H14 | partial | Talk harumi M21; undangan Ogawa, stage 6 |
| H15 | partial | Talk harumi M22; uang tidak jelas, Ogiwara curiga |
| H16 | partial | Talk harumi M23; Valentine data lain |
| H17 | partial | Talk harumi M25; Ogiwara menegur (B bela) |
| H18 | partial | Talk harumi M27; Mizuhara, jalur hukum akademik (A bersaksi) |
| H19 | partial | A: menanyakan harapan Harumi |
| H20 | partial | Talk harumi M29; teh terakhir, simbol kembali |
| H21 | partial | Talk harumi M30; pengumuman studi, ending |
| H22 | implemented | Ketiga respons lewat stasiun pada M33 |
| H23 | partial | Talk harumi M34; ujian skripsi |
| H24 | data-only | untested |
| S01 | partial | A, Yutaka |
| S02 | partial | A, Yutaka; kedaluwarsa pada Chiasa |
| S03 | partial | A/B di Klub Catur M3; payung, respek_shiori |
| S04 | partial | Talk shiori Klub Catur M5; shogi vila, C masuk daftar bohong |
| S05 | partial | Talk shiori M7; Tojo di pesta, tojo_aktif |
| S06 | partial | A/B di Klub Catur M8; turnamen, Trust |
| S07 | implemented | Makan, pamit dan titip hadiah |
| S08 | partial | A di Klub Catur M11; satu tahun, Trust |
| S09 | partial | Pertemanan lewat klub pada M12; A/B/C |
| S10 | partial | A di Klub Catur M15; Kuroiwa mencatat |
| S11 | partial | A/B di Klub Catur M16; C masuk daftar kebohongan |
| S12 | partial | A di Klub Catur M18; rumor Mei (C abstrak) |
| S13 | partial | Bukti dari C11-B, mengaku atau menyangkal. Sumber pengkhianatan lain belum tersambung |
| S14 | partial | Permintaan maaf setelah penemuan; A |
| S15 | partial | Doa Tahun Baru untuk kedua keadaan; A/B |
| S16 | partial | Papan kosong di Valentine, B; tertutup setelah pengakuan kecil |
| S17 | partial | Dukungan dibaca saat wisuda |
| S18 | partial | A/B/C di rumah dengan pemuatan ulang satu save |
| S19 | partial | Membaca atau membiarkan harapan Shiori |
| S20 | partial | Talk shiori M29; permainan terakhir, pesan tersirat |
| S21 | partial | Talk shiori M30; pengumuman Tojo, bidak |
| S22 | partial | Talk shiori M31; penghancuran dimulai, stage 5 |
| S23 | partial | Talk shiori M32; turnamen akhir |
| S24 | partial | Talk shiori M33; Natal skakmat, menentukan ending |
| S25 | data-only | untested |
| N01 | implemented | Cabang A, dua host |
| N02 | partial | B, Yutaka |
| N03 | implemented | Cabang A, dua host |
| N04 | partial | Efek B, tertunda 14 hari |
| N05 | partial | A di Studio Arsitektur, M6; cerita Koko |
| N06 | partial | untested |
| N07 | partial | A di Rumah Sakurajima saat Natal M9; Koko |
| N08 | partial | B di Studio, M11 Valentine; buat ulang coklat |
| N09 | partial | A di Studio, M12 White Day; hadiah kecil |
| N10 | partial | A di Studio M13; telepon Haruto, menandai haruto_kenal |
| N11 | partial | Talk nagisa Rumah Sakurajima M14; ditinggal, jeal |
| N12 | partial | Talk nagisa Gedung Arsitektur M15; hujan, relasi Chiasa |
| N13 | partial | Talk nagisa Gedung Arsitektur M17; konfrontasi yukata |
| N14 | partial | Talk nagisa G.Arsitektur M18; cek ponsel, gerbang yandere stage 3 |
| N15 | partial | Talk nagisa M21; ultimatum Natal, stage 4 |
| N16 | partial | Talk nagisa M23; pengakuan/bentrok |
| N17 | partial | Talk nagisa M24; tuduhan, pemulihan terakhir (jebakan konsekuensi-saja) |
| N18 | partial | Talk nagisa M26; sabotase Yuuto, stage 5 (konsekuensi) |
| N19 | partial | A: meminta Nagisa mencopot kertas |
| N20 | partial | A di Taman Lingkungan M29 malam; kembang api, kelekatan |
| N21 | partial | A/B lewat Nagisa di rumah, M31. Jendela lebih awal belum terhubung |
| N22 | implemented | Hadir, pamit, dan absen sampai wisuda |
| N23 | partial | B di kamar Chiasa setelah N21-B |
| N24 | data-only | untested |
| Mi01 | implemented | Cabang A, dua host |
| Mi02 | partial | A, Yutaka |
| Mi03 | implemented | Cabang A, dua host |
| Mi04 | partial | A di Gedung Kedokteran M5; tali obi, intim |
| Mi05 | partial | untested |
| Mi06 | partial | A lewat gedung kedokteran |
| Mi07 | partial | Cabang A, dua host |
| Mi08 | partial | A di Rumah Sakit M8; Sato, jalur pemulihan |
| Mi09 | partial | B melalui tombol Miyuki di lokasi pesta |
| Mi10 | partial | A di Kuil M10; omikuji kesendirian, Trust |
| Mi11 | implemented | A/B/C di Kafe Komorebi M11, Sabtu sore |
| Mi12 | partial | Membantu belajar lewat tombol Miyuki di Gedung Kedokteran |
| Mi13 | partial | Mendengarkan di rumah sakit, kelelahan +8 |
| Mi14 | partial | Talk miyuki RS M15; dimarahi supervisor, stage 2 |
| Mi15 | partial | Talk miyuki RS M17; minta maaf berlebihan, stage 3 |
| Mi16 | partial | Talk miyuki RS M19; gerbang rute masokis (C), D pemulihan |
| Mi17 | partial | Talk miyuki RS M20; pingsan, Sena menegur (konsekuensi) |
| Mi18 | partial | A, B, C setelah Mi09-B. Versi tanpa sandiwara belum diperiksa lewat layar |
| Mi19 | partial | Talk miyuki RS M23; Valentine dingin, pola menguat |
| Mi20 | partial | Talk miyuki RS M24; audit pribadi, C pemulihan Sato |
| Mi21 | partial | A/B di rotasi dan dampak pada karier |
| Mi22 | partial | Talk miyuki RS M27; pola menetap (A permanen), C pemulihan |
| Mi23 | partial | Talk miyuki RS M29; yukata, B memutus Sena (konsekuensi) |
| Mi24 | partial | Lulus dan gagal dicatat sebelum pengumuman; A dan B di RS |
| Mi25 | partial | A pada Chiasa; C pada Yutaka dan perjalanan seni Chiasa |
| Mi26 | partial | Talk miyuki RS M34; ujian akhir, Sena sekutu/lawan |
| Mi27 | data-only | untested |

### Event dinamis

128 dari 128 ID mempunyai referensi langsung dalam alur atau resolver. Katalog memuat 393 alternatif tertulis pada seluruh ID.

| ID | Implementasi | Bukti |
| --- | --- | --- |
| Mi-D01 | partial | A: membalas dan menemani (Yutaka). Pesan terlewat saat mode senyap (Chiasa). B/C/D belum diuji lewat layar |
| Mi-D02 | partial | Kursi di perpustakaan: A/B/C, waktu dan hasil diperiksa |
| Mi-D03 | partial | A di depan Koita (Yutaka). C dengan Nagisa hadir (Chiasa). B belum diuji lewat layar |
| Mi-D04 | partial | A (Yutaka) dan C (Chiasa) lewat tombol Miyuki. B belum diuji lewat layar |
| Mi-D05 | partial | Talk miyuki (RS, dini hari, luka>=50); tangga darurat, luka -15 |
| Mi-D06 | partial | Talk miyuki (stage>=3, luka>=40); teguran yang ia minta, 4 pilihan (konsekuensi) |
| Mi-D07 | partial | Talk miyuki (Kafe, Sabtu, omiai>=40); Hayase mengaku, 4 pilihan |
| Mi-D08 | partial | Talk koita (dini hari, sadar>=25); rahasia SMA, 4 pilihan |
| Mi-D09 | partial | A dari afeksi yang tumbuh lewat percakapan; perubahan karier dan luka diri |
| Mi-D10 | partial | Talk miyuki (RS, kelelahan>=85); resep salah tulis |
| Mi-D11 | partial | Makan malam B dibayar dan memengaruhi hasil CBT |
| Mi-D12 | partial | A di kafe dengan fixture dan di RS dari state awal; gerbang Mi25 ikut berubah |
| Mi-D13 | partial | Talk miyuki (Chiasa host, intim>=55); pertanyaan pada diri (yuri, menghargai) |
| Mi-D14 | partial | Talk miyuki (kesehatan<=60, stage<=3); merawat pemain |
| N-D01 | partial | untested |
| N-D02 | partial | untested |
| N-D03 | partial | A, Chiasa; absen dan kedaluwarsa pada Yutaka |
| N-D04 | partial | Talk nagisa (stage>=2, aff>=30, malam); tawaran kedua Yuuto, kelekatan |
| N-D05 | partial | Talk nagisa (jeal>=50); tangkapan layar, 4 pilihan |
| N-D06 | partial | Talk nagisa (stage>=3, kelekatan>=70); kunci cadangan |
| N-D07 | partial | Talk nagisa (haruto_kenal, larut); Haruto sekutu/lawan |
| N-D08 | partial | A setelah N02-B, Yutaka |
| N-D09 | partial | Meminta Moeka menjahit sesudah N23-B |
| N-D10 | partial | Talk nagisa (N-D01 terlewat, stage>=3); 37 pesan, 4 pilihan |
| N-D11 | partial | Talk nagisa (kelekatan>=70, aff>=55, stage<=2); denah rumah, intim |
| N-D12 | partial | Talk nagisa (Chiasa host, intim>=40); Nacchan-oneechan |
| N-D13 | partial | Talk nagisa (Chiasa host, stage>=3); jendela seberang |
| H-D01 | partial | B pada Yutaka, A pada Chiasa; akses dapur berbeda |
| H-D02 | partial | Talk harumi (ogawa_aktif); lembar pengamatan, koreksi/manfaatkan |
| H-D03 | partial | Talk harumi (cengkeraman>=40, malam); pintu lab, 4 pilihan, bukti |
| H-D04 | partial | Talk harumi (ogawa_aktif); tawaran Ogawa, tolak/susup/lapor |
| H-D05 | partial | A setelah H03-C, Yutaka |
| H-D06 | partial | Talk harumi (ogawa_aktif, stage>=4); taksi jam lima, 4 pilihan |
| H-D07 | partial | A di Perpustakaan setelah H10-A; A/B/C via hook |
| H-D08 | partial | Talk harumi (kejelasan>=60, validasi>=40); hipotesis ditolak, grip -30 |
| H-D09 | partial | Talk harumi (ogawa_aktif, stage>=3); celah jadwal, H15 dini |
| H-D10 | partial | Talk harumi (stage>=3, rumor>=20); permintaan komentar Mei |
| H-D11 | partial | Talk harumi (kejelasan>=50, intim>=50); diajari cinta (berpusat persetujuan) |
| H-D12 | partial | Talk harumi (Chiasa host, stage>=2); poster riset kolaborasi |
| Mo-D01 | partial | Talk moeka (stres>=60, malam); onigiri jam tiga, 4 pilihan (konsekuensi) |
| Mo-D02 | partial | Talk moeka (stage>=2, stres>=60); panggilan empat detik |
| Mo-D03 | partial | Talk moeka (stage>=2, aff>=30); kostum Hinata, keluarga mengenal pemain |
| Mo-D04 | partial | Talk moeka (intim>=40); struk cuci darah ayah, ayah diketahui |
| Mo-D05 | partial | Talk moeka (kuga_tekanan>=40); lokasi Kuga, 4 pilihan, bukti/penjaga |
| Mo-D06 | partial | Talk moeka (bulan ultah, stres>=50); ulang tahun, topeng -/+ |
| Mo-D07 | partial | Talk moeka (rina_curiga>=50); Rina sekutu, jendela Mo25 |
| Mo-D08 | partial | Talk moeka (stage>=3, stres>=55); surat banding beasiswa |
| Mo-D09 | partial | Talk moeka (ayah diketahui, stage>=3); tes donor, cabang (konsekuensi) |
| Mo-D10 | partial | Talk moeka (topeng>=70, malam); tawa grup jam dua, japri menurunkan topeng |
| Mo-D11 | partial | Talk moeka (stage>=4); barang dikembalikan, tanda bahaya |
| Mo-D12 | partial | Talk moeka (stage>=3, intim>=55); pertanyaan tenang->Sato Kyoko, selamat |
| Mo-D13 | partial | Talk moeka (stres<40, aff>=55); sketsa label, jalan keluar |
| S-D01 | partial | Talk shiori (trust>=25); langkah jam dua belas, akun anonim |
| S-D02 | partial | Talk shiori (stage>=3); Kuroiwa di parkiran |
| S-D03 | partial | Talk shiori (respek>=60); kekalahan yang ia rayakan |
| S-D04 | partial | A sebelum S13 mencegah penemuan; B menambah catatan saat alasan kedua terbongkar |
| S-D05 | partial | Talk shiori (Chiasa host); buku Shena, jembatan/perangkap |
| S-D06 | partial | Talk shiori (tojo_aktif); gala pengalih |
| S-D07 | partial | Talk shiori (marah_koita>=40); kartu pola Koita, sasaran bergeser |
| S-D08 | partial | Jujur saat minum teh setelah S07-A |
| S-D09 | partial | A melalui tombol papan di klub; percepatan S20 belum tersambung |
| S-D10 | partial | Talk shiori (bukti Ogawa/Kuga); persekutuan musuh bersama |
| S-D11 | partial | Talk shiori (respek>=50, tahu_sistem); prediksi benar |
| S-D12 | partial | Talk shiori (stage>=4); ratu sakit, rawat/geledah (marah +40) |
| S-D13 | partial | Talk shiori (trust>=30); rahasia palsu umpan, ujian |
| S-D14 | partial | Talk shiori (trust>=30); ujian khianat, tolak->respek +10 |
| S-D15 | partial | Talk shiori (marah>=60); senyum manis/honeytrap, konsekuensi |
| S-D16 | partial | Talk shiori (senyum_terbaca>=40); langkah cepat, +baca |
| S-D17 | partial | Talk shiori (bukti>=50); papan dibalik, langkah jujur->respek +15 |
| C-D01 | partial | Host Chiasa (rumah, malam); dapur jam dua, 4 pilihan, benih Success |
| C-D02 | partial | C, setelah menerima proyek dan mencari ilustrator |
| C-D03 | partial | B, latihan saat tubuh lelah |
| C-D04 | partial | Host Chiasa (lelah tier>=2); hari berat, Yoshie dekat |
| C-D05 | partial | Host Chiasa (M16); video call Daisuke, node naratif, curiga identitas |
| C-D06 | partial | Host Chiasa (nagisa stage>=2); adu mulut di pagar |
| C-D07 | partial | A, pukul 23 setelah proyek diterima |
| C-D08 | partial | Host Chiasa (yutaka_harap>=30, malam); kopi Yutaka, Koita melihat |
| C-D09 | partial | Host Chiasa (koita_arah_bl); tangis ruang tamu, 4 pilihan (konsekuensi) |
| C-D10 | partial | Host Chiasa (bulan 9/21, hari 24/25); bandara, Success berisiko |
| C-D11 | partial | Host Chiasa (koita_arah_bl); karya dibeli anonim, Haruka |
| C-D12 | partial | Host Chiasa (intim heroine>=50); kuas dipinjam (yuri menguat) |
| C-D13 | partial | Host Chiasa (framing_koita); mata kering, nurani -15/+10 |
| C-D14 | partial | Host Chiasa (framing_koita); pengakuan setengah, mengaku penuh->framing terbuka |
| C-D15 | partial | Host Chiasa (framing_koita); nyaris ketahuan, Shiori baca kejanggalan |
| K-D01 | partial | Talk koita; draf tertinggal, kutipan_draf_koita + sadar |
| K-D02 | partial | Talk koita (takut_ditinggal>=60); jalan pulang jauh, takut diproses |
| K-D03 | partial | Talk koita (Yutaka, M8+); uang hadiah, intel pilihan |
| K-D04 | partial | Talk koita (M20+, pola dicurigai); dua pesan kembar, bukti pola |
| K-D05 | partial | Talk koita (sadar>=50); senyum berhenti, Trust/intel |
| K-D06 | partial | Talk koita (matsuda_sekutu); debat klub, pola_publik |
| K-D07 | partial | Talk koita (Yutaka, ikatan_bl>=50); pelukan stasiun, pointer BL (non-eksplisit) |
| K-D08 | partial | Talk koita (M13+); baca ponsel, sadar +25 |
| K-D09 | partial | Talk koita (pasca K16-A); foto ayah, rasa_bersalah |
| K-D10 | partial | Talk koita (plot_armor>=75); tiga kegagalan, sadar/Sistem |
| K-D11 | partial | Talk koita (sadar>=75, pilihan>=80); memilih lebih awal |
| K-D12 | partial | Talk koita (M35+); gladi pidato wisuda, nada epilog |
| K-D13 | partial | Talk koita (orbit<=2); nama dicoret, runtuh+ |
| K-D14 | partial | Talk koita (plot_armor>=90, orbit<=1); kebetulan kosong, pelindung padam |
| K-D15 | partial | Talk koita (runtuh>=30, orbit<=2); dari seberang jalan, runtuh+/Fear |
| K-D16 | partial | Talk koita (sadar>=60); pengakuan disengaja, runtuh +20..40 (konsekuensi) |
| K-D17 | partial | Talk koita (force_pernah); menemukan akibat (konsekuensi+karakter saja, tanpa metode) |
| K-D18 | partial | Talk koita (runtuh>=60); draf terakhir dihapus (konsekuensi) |
| K-D19 | partial | Talk koita (runtuh>=60); telepon Yoshie, belok pemulihan |
| K-D20 | partial | Talk koita (runtuh>=70); Matsuda ke konselor, runtuh- |
| K-D21 | partial | Talk koita (runtuh>=50, rumor); saksi menolak menuduh, runtuh- |
| Y-D01 | partial | Host Yutaka (hari 25); notifikasi saldo, arah uang |
| Y-D02 | partial | Host Yutaka (koita_arah_bl); teman game heran, curiga identitas |
| Y-D03 | partial | A pada Yutaka; tertutup untuk Chiasa |
| Y-D04 | partial | Host Yutaka (daichi_kenal); Daichi melihat catatan |
| Y-D05 | partial | Host Yutaka (M16); jam Daisuke, curiga identitas |
| Y-D06 | partial | Host Yutaka (Jumat malam); Tojo mabuk, intel/rekaman |
| Y-D07 | partial | Host Yutaka (Nagisa aff>=40, malam); main sampai pagi, kelekatan |
| Y-D08 | partial | A pada Yutaka; tertutup untuk Chiasa |
| Y-D09 | partial | Host Yutaka (koita_arah_bl); Koita depan pintu, benih BL |
| Y-D10 | partial | Host Chiasa, Yutaka-NPC (harap>=50); menunggu di stasiun |
| Y-D11 | partial | Host Chiasa, Yutaka-NPC (harap>=70); pengakuan Jumat malam |
| X-D01 | partial | Talk moeka (nagisa jeal>=60, stres>=60, malam); pertengkaran konbini, 4 pilihan |
| X-D02 | partial | Talk miyuki (moeka stage>=3, kelelahan<60); dokter baca tanda, jendela Moeka |
| X-D03 | partial | Talk shiori (ogawa_aktif, harumi+shiori trust>=40); dua peringkat vs Ogawa |
| X-D04 | partial | Talk koita (Valentine, bln14 hari14); dua coklat, rahasia |
| X-D05 | partial | Host (Natal, rumah, slot 3/4); rumah penuh, panggung pengakuan, node |
| X-D06 | partial | Talk koita (mei_menulis); wawancara Mei, reputasi |
| X-D07 | partial | Talk koita (sadar>=75); rapat rahasia, manuver dibalik |
| X-D08 | partial | Talk moeka (rina+sena curiga>=50); dua sahabat bertukar cerita |
| X-D09 | partial | Talk koita (haruto>=50, kuroiwa>=20); dua penjaga, node naratif |
| X-D10 | partial | Talk moeka (krisis_ganda); malam dua krisis, kirim orang |
| X-D11 | partial | Talk koita (grup_sma_dibuka); grup SMA hidup lagi |
| X-D12 | partial | Talk koita (lelah tier>=3); salah kirim pesan, cabang baru |

### Ending

220 dari 220 ID mempunyai referensi langsung dalam alur atau resolver.

| ID | Implementasi | Bukti |
| --- | --- | --- |
| E-MI-01 | partial | untested |
| E-MI-02 | partial | Perjalanan klinik Yutaka sampai wisuda; hasil keluarga dan romansa yang sudah terhubung didahulukan |
| E-MI-03 | partial | resolver (gerbang flag rute distingtif) |
| E-MI-04 | partial | Sesudah Mi25-A, dua host |
| E-MI-05 | partial | Yutaka dan perjalanan seni Chiasa |
| E-MI-06 | partial | resolver (gerbang flag rute distingtif) |
| E-MI-07 | partial | resolver rute |
| E-MI-08 | partial | resolver rute |
| E-MI-09 | partial | resolver (gerbang flag rute distingtif) |
| E-MI-10 | partial | resolver rute |
| E-MI-11 | partial | resolver rute |
| E-MI-12 | partial | resolver (gerbang flag rute distingtif) |
| E-MI-13 | partial | Pengakuan Mi18-C mencapai wisuda |
| E-MI-14 | partial | Pertanyaan Takeru di Mi18-B hingga wisuda |
| E-NA-01 | partial | untested |
| E-NA-02 | partial | resolver (gerbang flag rute distingtif) |
| E-NA-03 | partial | resolver (gerbang flag rute distingtif) |
| E-NA-04 | partial | resolver (gerbang flag rute distingtif) |
| E-NA-05 | partial | resolver rute |
| E-NA-06 | partial | resolver rute |
| E-NA-07 | partial | Jujur pada Haruto tanpa hadir di N22, atau hadir di N22 tanpa N21 |
| E-NA-08 | partial | resolver rute |
| E-NA-09 | partial | untested |
| E-NA-10 | partial | resolver rute |
| E-NA-11 | partial | resolver rute |
| E-NA-12 | partial | untested |
| E-NA-13 | partial | resolver (gerbang flag rute distingtif) |
| E-NA-14 | partial | resolver (gerbang flag rute distingtif) |
| E-HA-01 | partial | Dua perjalanan mencapai epilog, satu melewatkannya |
| E-HA-02 | partial | resolver (gerbang flag rute distingtif) |
| E-HA-03 | partial | resolver (gerbang flag rute distingtif) |
| E-HA-04 | partial | resolver (gerbang flag rute distingtif) |
| E-HA-05 | partial | resolver rute |
| E-HA-06 | partial | resolver rute |
| E-HA-07 | partial | resolver rute |
| E-HA-08 | partial | resolver rute |
| E-HA-09 | partial | orang_tua_kujo ≥ 60 lewat H05-B, H10-A, H-D07-A; muncul saat jalur kejelasan tidak aktif |
| E-HA-10 | partial | resolver (gerbang flag rute distingtif) |
| E-HA-11 | partial | resolver (gerbang flag rute distingtif) |
| E-HA-12 | partial | resolver (gerbang flag rute distingtif) |
| E-HA-13 | partial | resolver (gerbang flag rute distingtif) |
| E-HA-14 | partial | resolver (gerbang flag rute distingtif) |
| E-MO-01 | partial | resolver (gerbang flag rute distingtif) |
| E-MO-02 | partial | resolver (gerbang flag rute distingtif) |
| E-MO-03 | partial | resolver (gerbang flag rute distingtif) |
| E-MO-04 | partial | resolver rute |
| E-MO-05 | partial | resolver rute |
| E-MO-06 | partial | resolver rute |
| E-MO-07 | partial | resolver rute |
| E-MO-08 | partial | resolver (gerbang flag rute distingtif) |
| E-MO-09 | partial | resolver rute |
| E-MO-10 | partial | resolver (gerbang flag rute distingtif) |
| E-MO-11 | partial | resolver (gerbang flag rute distingtif) |
| E-MO-12 | partial | resolver (gerbang flag rute distingtif) |
| E-MO-13 | partial | resolver (gerbang flag rute distingtif) |
| E-SH-01 | partial | resolver (gerbang flag rute distingtif) |
| E-SH-02 | partial | resolver rute |
| E-SH-03 | partial | resolver (gerbang flag rute distingtif) |
| E-SH-04 | partial | resolver (gerbang flag rute distingtif) |
| E-SH-05 | partial | resolver (gerbang flag rute distingtif) |
| E-SH-06 | partial | resolver rute |
| E-SH-07 | partial | Dukungan S17 saat Revenge belum aktif. Pemeriksaan dengan dan tanpa penyangkalan S13 |
| E-SH-08 | partial | resolver rute |
| E-SH-09 | partial | resolver (gerbang flag rute distingtif) |
| E-SH-10 | partial | resolver (gerbang flag rute distingtif) |
| E-SH-11 | partial | resolver (gerbang flag rute distingtif) |
| E-SH-12 | partial | resolver (gerbang flag rute distingtif) |
| E-SH-13 | partial | Penyangkalan C11-B terungkap di S13-B, lalu menargetkan karier Shena di wisuda |
| E-SH-14 | partial | resolver (gerbang flag rute distingtif) |
| E-SH-15 | partial | resolver rute |
| E-SH-16 | partial | resolver rute |
| E-CH-01 | partial | resolver (gerbang flag rute distingtif) |
| E-CH-02 | partial | resolver (gerbang flag rute distingtif) |
| E-CH-03 | partial | resolver (gerbang flag rute distingtif) |
| E-CH-04 | partial | resolver (gerbang flag rute distingtif) |
| E-CH-05 | partial | resolver (gerbang flag rute distingtif) |
| E-CH-06 | partial | resolver (gerbang flag rute distingtif) |
| E-CH-07 | partial | resolver (gerbang flag rute distingtif) |
| E-CH-08 | partial | resolver (gerbang flag rute distingtif) |
| E-CH-09 | partial | resolver (gerbang flag rute distingtif) |
| E-CH-10 | partial | resolver (gerbang flag rute distingtif) |
| E-CH-11 | partial | resolver (gerbang flag rute distingtif) |
| E-CF-01 | partial | Chiasa dengan romansa dan evaluasi berhasil. Nada respons keluarga belum terhubung |
| E-CF-02 | partial | resolver (gerbang flag rute distingtif) |
| E-CF-03 | partial | resolver (gerbang flag rute distingtif) |
| E-CF-04 | partial | resolver (gerbang flag rute distingtif) |
| E-CF-05 | partial | resolver (gerbang flag rute distingtif) |
| E-CF-06 | partial | resolver (gerbang flag rute distingtif) |
| E-CF-07 | partial | resolver (gerbang flag rute distingtif) |
| E-CF-08 | partial | Perjalanan Chiasa yang berlatih dan lolos evaluasi |
| E-CF-09 | partial | resolver (gerbang flag rute distingtif) |
| E-CF-10 | partial | untested |
| E-CF-11 | partial | resolver (gerbang flag rute distingtif) |
| E-CF-12 | partial | resolver (gerbang flag rute distingtif) |
| E-CF-13 | partial | resolver (gerbang flag rute distingtif) |
| E-KO-01 | partial | resolver (gerbang flag rute distingtif) |
| E-KO-02 | partial | resolver (gerbang flag rute distingtif) |
| E-KO-03 | partial | resolver (gerbang flag rute distingtif) |
| E-KO-04 | partial | resolver (gerbang flag rute distingtif) |
| E-KO-05 | partial | resolver (gerbang flag rute distingtif) |
| E-KO-06 | partial | resolver (gerbang flag rute distingtif) |
| E-KO-07 | partial | resolver rute |
| E-KO-08 | partial | resolver (gerbang flag rute distingtif) |
| E-KO-09 | partial | resolver rute |
| E-KO-10 | partial | resolver rute |
| E-KO-11 | partial | resolver rute |
| E-KO-12 | partial | resolver (gerbang flag rute distingtif) |
| E-KO-13 | partial | resolver (gerbang flag rute distingtif) |
| E-KO-14 | partial | resolver (gerbang flag rute distingtif) |
| E-KO-15 | partial | resolver (gerbang flag rute distingtif) |
| E-KO-16 | partial | resolver (gerbang flag rute distingtif) |
| E-KO-17 | partial | resolver (gerbang flag rute distingtif) |
| E-KO-18 | partial | resolver (gerbang flag rute distingtif) |
| E-KO-19 | partial | resolver (gerbang flag rute distingtif) |
| E-KO-20 | partial | resolver rute |
| E-KO-21 | partial | resolver (gerbang flag rute distingtif) |
| E-BL-01 | partial | resolver (gerbang flag rute distingtif) |
| E-BL-02 | partial | resolver (gerbang flag rute distingtif) |
| E-BL-03 | partial | resolver (gerbang flag rute distingtif) |
| E-BL-04 | partial | resolver (gerbang flag rute distingtif) |
| E-BL-05 | partial | resolver (gerbang flag rute distingtif) |
| E-BL-06 | partial | resolver (gerbang flag rute distingtif) |
| E-BL-07 | partial | resolver (gerbang flag rute distingtif) |
| E-BL-08 | partial | resolver (gerbang flag rute distingtif) |
| E-YH-01 | partial | Epilog Yutaka; absen untuk Chiasa |
| E-YH-02 | partial | untested |
| E-YH-03 | partial | Bond Amamiya dari Y13; dua keadaan diuji lewat resolver |
| E-YH-04 | partial | resolver (gerbang flag rute distingtif) |
| E-YH-05 | partial | resolver (gerbang flag rute distingtif) |
| E-YH-06 | partial | untested |
| E-YH-07 | partial | resolver (gerbang flag rute distingtif) |
| E-YU-01 | partial | resolver (gerbang flag rute distingtif) |
| E-YU-02 | partial | resolver (gerbang flag rute distingtif) |
| E-YU-03 | partial | resolver (gerbang flag rute distingtif) |
| E-YU-04 | partial | resolver (gerbang flag rute distingtif) |
| E-YU-05 | partial | resolver (gerbang flag rute distingtif) |
| E-YU-06 | partial | resolver (gerbang flag rute distingtif) |
| E-YU-07 | partial | resolver (gerbang flag rute distingtif) |
| E-YU-08 | partial | resolver (gerbang flag rute distingtif) |
| E-FO-01 | partial | resolver (gerbang flag rute distingtif) |
| E-FO-02 | partial | resolver (gerbang flag rute distingtif) |
| E-FO-03 | partial | resolver (gerbang flag rute distingtif) |
| E-FO-04 | partial | resolver (gerbang flag rute distingtif) |
| E-FO-05 | partial | resolver (gerbang flag rute distingtif) |
| E-FO-06 | partial | resolver (gerbang flag rute distingtif) |
| E-FO-07 | partial | resolver (gerbang flag rute distingtif) |
| E-FO-08 | partial | resolver (gerbang flag rute distingtif) |
| E-FO-09 | partial | resolver (gerbang flag rute distingtif) |
| E-FO-10 | partial | resolver (gerbang flag rute distingtif) |
| E-FO-11 | partial | resolver (gerbang flag rute distingtif) |
| E-FO-12 | partial | resolver (gerbang flag rute distingtif) |
| E-FO-13 | partial | resolver (gerbang flag rute distingtif) |
| E-FO-14 | partial | resolver (gerbang flag rute distingtif) |
| E-FO-15 | partial | resolver (gerbang flag rute distingtif) |
| E-SI-01 | partial | untested |
| E-SI-02 | partial | Yutaka dan perjalanan seni Chiasa |
| E-SI-03 | partial | untested |
| E-SI-04 | partial | resolver (gerbang flag rute distingtif) |
| E-SI-05 | partial | untested |
| E-SI-06 | partial | untested |
| E-SI-07 | partial | resolver (gerbang flag rute distingtif) |
| E-SI-08 | partial | resolver (gerbang flag rute distingtif) |
| E-SI-09 | partial | resolver (gerbang flag rute distingtif) |
| E-SI-10 | partial | resolver (gerbang flag rute distingtif) |
| E-SI-11 | partial | resolver (gerbang flag rute distingtif) |
| E-SI-12 | partial | resolver (gerbang flag rute distingtif) |
| E-SI-13 | partial | Perjalanan Chiasa yang gagal evaluasi |
| E-SI-14 | partial | resolver (gerbang flag rute distingtif) |
| E-SI-15 | partial | resolver (gerbang flag rute distingtif) |
| E-SI-16 | partial | resolver (gerbang flag rute distingtif) |
| E-SI-17 | partial | resolver (gerbang flag rute distingtif) |
| E-SI-18 | partial | untested |
| E-HP-01 | partial | untested |
| E-HP-02 | partial | untested |
| E-HP-03 | partial | resolver (gerbang flag rute distingtif) |
| E-HP-04 | partial | resolver (gerbang flag rute distingtif) |
| E-HP-05 | partial | untested |
| E-HP-06 | partial | resolver (gerbang flag rute distingtif) |
| E-HP-07 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-01 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-02 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-03 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-04 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-05 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-06 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-07 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-08 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-09 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-10 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-11 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-12 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-13 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-14 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-15 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-16 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-17 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-18 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-19 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-20 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-21 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-22 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-23 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-24 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-25 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-26 | partial | resolver (gerbang flag rute distingtif) |
| E-NPC-27 | partial | resolver (gerbang flag rute distingtif) |
| E-X-01 | partial | resolver (gerbang flag rute distingtif) |
| E-X-02 | partial | resolver (gerbang flag rute distingtif) |
| E-X-03 | partial | resolver (gerbang flag rute distingtif) |
| E-X-04 | partial | resolver (gerbang flag rute distingtif) |
| E-X-05 | partial | resolver (gerbang flag rute distingtif) |
| E-X-06 | partial | resolver (gerbang flag rute distingtif) |
| E-X-07 | partial | resolver (gerbang flag rute distingtif) |
| E-X-08 | partial | resolver (gerbang flag rute distingtif) |
| E-X-09 | partial | resolver (gerbang flag rute distingtif) |
| E-X-10 | partial | resolver (gerbang flag rute distingtif) |
| E-X-11 | partial | resolver (gerbang flag rute distingtif) |
| E-X-12 | partial | resolver (gerbang flag rute distingtif) |
| E-X-13 | partial | resolver (gerbang flag rute distingtif) |
| E-X-14 | partial | resolver (gerbang flag rute distingtif) |
