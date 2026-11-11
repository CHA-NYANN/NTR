# Cakupan sandbox Kouseikan

Baseline GitHub 74447c1. Matriks ini mengukur jalur pemain. Explorer pengembang dapat membaca seluruh katalog. Jumlah cabang katalog mencakup alternatif tertulis, termasuk diam atau absen yang tidak selalu berupa tombol.

## Fase dan bukti

| Fase | Hasil | Batas pengujian |
| --- | --- | --- |
| Fondasi | Kalender 36 bulan, konteks lokasi, kalender NPC, biaya aktivitas, memori pertemuan, penurunan relasi dan antrean akibat. Sebelumnya pemicu bisa memaksa NPC hadir dan hari tidak otomatis mengganti bulan. | Kondisi awal kedua host dan kalender diuji. Satu save Yutaka dari ZIP playtest sebelumnya kembali ke layar distrik dengan saldo, tanggal dan pilihan yang sama. Save pengguna lain, lokasi lain dan seluruh versi sebelumnya belum diuji. Sembilan lapisan jadwal dan ekonomi belum lengkap. Janji pertemuan mengubah lokasi, dan ketidakhadiran pemain memengaruhi kepercayaan bila NPC datang. |
| Vertical slice | N01, Mi01, N03, Mi03 memiliki adegan, pilihan, dan pengaruh ke pertemuan selanjutnya. | Driver menjalankan cabang A pada kedua host. Kalender dipercepat setelah pertemuan pertama. |
| Konten | Nagisa, Miyuki dan tawaran kerja Yutaka mendapat pertemuan lanjutan. N04-B dapat mengubah keadaan Nagisa/Koita dua minggu kemudian meski pemain absen. | Driver menguji efek N04-B melalui pencatatan pilihan. Belum menjalankan semua alternatif adegan. Dialog penghubung baru berstatus draft editorial. |
| Ending | Evaluasi saat kelulusan dan epilog berlapis. | E-SI-13, E-MI-04, dan E-HA-01 diperiksa pada akhir skenario. Referensi kode lain pada resolver belum membuktikan semua prasyarat dapat dibentuk lewat dunia normal. |
| QA | Dari folder proyek jalankan `python tests/run_living.py PATH_SDK` dengan Ren'Py 8.3.2 Windows/Linux x86-64. Driver membuat proyek dan save temporer. | Dijalankan di Windows. Lint, dua host, tindakan, perjalanan, simpan/muat, rollback, kesempatan terlewat dan akibat tertunda. Layar lokasi Hanami dengan enam NPC diperiksa di 1280×720, 1366×768 dan 1920×1080. Tombol aktivitas dan keluar terlihat pada ketiganya. Layar lain belum diperiksa ulang di semua resolusi. Belum ada benchmark satu sesi penuh tiga tahun. |

## Iterasi Hanami, Golden Week dan Harumi

Pada akhir pekan Hanami, ada pertemuan terpisah dengan Harumi di perpustakaan sains, Moeka di piknik, dan Shiori di dekat papan shogi. Pada 3–6 Mei, stasiun menawarkan perjalanan ke ryokan. NPC bepergian meski pemain tinggal di kota. Uji Yutaka memeriksa percakapan, efek dan jam pada empat peristiwa Golden Week. Uji Chiasa memeriksa kedaluwarsa. Skenario memakai kalender dipercepat dan panggilan interaksi produksi. Belum seluruh tombol perjalanan dan alternatif respons diuji manual.

Membantu Harumi memasak membuka H-D05 pada pertemuan selanjutnya. E-HA-01 mensyaratkan kejelasan emosi, dukungan nyata saat ia menamai perasaannya, dan riwayat tanpa Force. Di penginapan, mengalah sengaja pada Nagisa dapat membuka N-D08, ketika ia memutar ulang permainan. Setelah balasan Koita, kesempatan N-D03 hanya terbuka pada malam turunnya harapan Nagisa.

H08-A membuka kemungkinan teh larut malam di asrama, bila Harumi hadir. H09 mengingat percakapan tahun baru. Pemilihan slot kegiatan di ryokan, kunjungan tahun baru tanggal 1–3, dan waktu tempuh 60 menit merupakan penjadwalan prototipe. Besar efek memakai rentang Sistem_Cabang_dan_Poin §2.2. Dialog penghubung memerlukan tinjauan editorial.

Di kamar sendiri, pemain dapat memasang alarm untuk 20 menit, 90 menit, 6, 8, atau 10 jam. Ponsel memiliki mode senyap, normal, dan siaga serta daftar kontak prioritas dari orang yang pernah ditemui. Interupsi memakai dua pesan yang terhubung saat ini. Kualitas tidur di lokasi lain, panggilan darurat, dan seluruh penyebab bangun masih parsial.

## Menjalankan ulang pemeriksaan

- `python tests/check_catalog.py` memeriksa ID, duplikasi, label adegan dan angka matriks.
- `python tests/run_living.py PATH_SDK` menjalankan lint produksi dan dua perjalanan.
- `python tests/run_living.py PATH_SDK FOLDER_GAMBAR` mengambil gambar layar Hanami ramai pada tiga ukuran target.
- `python tests/run_save_upgrade.py PATH_SDK ZIP_PLAYTEST_SEBELUMNYA` membuat save baru pada versi lama yang dipercaya dan memuatnya pada versi sekarang. Sampel yang diuji berasal dari paket LivingWorld sebelum iterasi Hanami/Golden Week.
- ZIP Windows iterasi ini lolos pemeriksaan integritas. Executable hasil ekstraksi memulai renderer. Skenario panjang berjalan di proyek temporer dengan source produksi.

## Pedoman playtest

Mulai permainan baru, pilih salah satu tubuh, lalu kunjungi distrik kampus. Coba makan, berbicara dengan seseorang, kembali ke tempat itu pada waktu berbeda dan simpan sebelum sebuah keputusan. Muat kembali dan amati perbedaan respons. Untuk laporan sertakan tubuh, tanggal/jam, lokasi, tindakan dan perubahan yang terlihat. Gunakan save terpisah untuk membandingkan dua perjalanan.

Untuk mencoba Golden Week, datangi stasiun pada 3–6 Mei, pilih berangkat, lalu lihat siapa yang berada di lobi atau dapur. Untuk membandingkan, gunakan save kedua dan tetap di kota hingga liburan selesai.

## Ketidaksesuaian sumber

- K02: Milestone_3_Tahun M02 menyebut Koita sekamar dengan dua heroine. Event_Koita K02 menyebut satu heroine sesuai kesiapan. K02 belum diaktifkan. Empat event lain di Golden Week bisa ditemukan.
- GDD menyebut Master Canon v11.1. File yang ditemukan adalah v11. Isi v11.1 belum dapat dibandingkan.
- Efek kelelahan Mi03-A memakai −8 dari hook existing dan Alur_Cabang/01; contoh di Sistem_Cabang_dan_Poin §6 memakai −5. Angka existing dipertahankan sampai prioritas dua rujukan dikonfirmasi.

## Matriks katalog

Status implementasi dan bukti uji merupakan dua kolom terpisah. **implemented** menandai adegan slice dengan jalur A teruji, **partial** untuk koneksi yang masih mempunyai kondisi atau alternatif yang perlu diperiksa, **data-only** untuk entri tanpa pemicu dunia/resolver yang diidentifikasi. **blocked** berlaku bagi perbandingan canon v11.1 yang berkasnya belum tersedia. **untested** berarti belum dibuktikan melalui skenario desktop ini.

### Event utama

24 dari 190 ID mempunyai referensi langsung dalam alur atau resolver. Katalog memuat 553 alternatif tertulis pada seluruh ID.

| ID | Implementasi | Bukti |
| --- | --- | --- |
| C01 | implemented | Pembukaan A, Chiasa |
| C02 | data-only | untested |
| C03 | data-only | untested |
| C04 | data-only | untested |
| C05 | data-only | untested |
| C06 | data-only | untested |
| C07 | data-only | untested |
| C08 | data-only | untested |
| C09 | data-only | untested |
| C10 | data-only | untested |
| C11 | data-only | untested |
| C12 | data-only | untested |
| C13 | data-only | untested |
| C14 | data-only | untested |
| C15 | data-only | untested |
| C16 | data-only | untested |
| C17 | data-only | untested |
| C18 | data-only | untested |
| K01 | data-only | untested |
| K02 | data-only | untested |
| K03 | data-only | untested |
| K04 | data-only | untested |
| K05 | data-only | untested |
| K06 | data-only | untested |
| K07 | data-only | untested |
| K08 | data-only | untested |
| K09 | data-only | untested |
| K10 | data-only | untested |
| K11 | data-only | untested |
| K12 | data-only | untested |
| K13 | data-only | untested |
| K14 | data-only | untested |
| K15 | data-only | untested |
| K16 | data-only | untested |
| K17 | data-only | untested |
| K18 | data-only | untested |
| K19 | data-only | untested |
| K20 | data-only | untested |
| K21 | data-only | untested |
| K22 | data-only | untested |
| K23 | data-only | untested |
| K24 | data-only | untested |
| K25 | data-only | untested |
| K26 | data-only | untested |
| K27 | data-only | untested |
| Y01 | implemented | Pembukaan A, Yutaka |
| Y02 | data-only | untested |
| Y03 | data-only | untested |
| Y04 | data-only | untested |
| Y05 | data-only | untested |
| Y06 | data-only | untested |
| Y07 | data-only | untested |
| Y08 | data-only | untested |
| Y09 | data-only | untested |
| Y10 | data-only | untested |
| Y11 | data-only | untested |
| Y12 | data-only | untested |
| Y13 | data-only | untested |
| Y14 | data-only | untested |
| Y15 | data-only | untested |
| Y16 | data-only | untested |
| Y17 | partial | Cabang A, Yutaka; tertutup untuk Chiasa |
| Y18 | data-only | untested |
| Y19 | data-only | untested |
| Mo01 | partial | A, Chiasa |
| Mo02 | partial | A, Yutaka |
| Mo03 | data-only | untested |
| Mo04 | data-only | untested |
| Mo05 | data-only | untested |
| Mo06 | data-only | untested |
| Mo07 | data-only | untested |
| Mo08 | data-only | untested |
| Mo09 | data-only | untested |
| Mo10 | data-only | untested |
| Mo11 | data-only | untested |
| Mo12 | data-only | untested |
| Mo13 | data-only | untested |
| Mo14 | data-only | untested |
| Mo15 | data-only | untested |
| Mo16 | data-only | untested |
| Mo17 | data-only | untested |
| Mo18 | data-only | untested |
| Mo19 | data-only | untested |
| Mo20 | data-only | untested |
| Mo21 | data-only | untested |
| Mo22 | data-only | untested |
| Mo23 | data-only | untested |
| Mo24 | data-only | untested |
| Mo26 | data-only | untested |
| Mo25 | data-only | untested |
| H01 | partial | A, kedua host |
| H02 | data-only | untested |
| H03 | partial | C, Yutaka |
| H04 | data-only | untested |
| H05 | data-only | untested |
| H06 | data-only | untested |
| H07 | data-only | untested |
| H08 | partial | A, kedua host |
| H09 | partial | A, kedua host |
| H10 | data-only | untested |
| H11 | data-only | untested |
| H12 | data-only | untested |
| H13 | data-only | untested |
| H14 | data-only | untested |
| H15 | data-only | untested |
| H16 | data-only | untested |
| H17 | data-only | untested |
| H18 | data-only | untested |
| H19 | data-only | untested |
| H20 | data-only | untested |
| H21 | data-only | untested |
| H22 | data-only | untested |
| H23 | data-only | untested |
| H24 | data-only | untested |
| S01 | partial | A, Yutaka |
| S02 | partial | A, Yutaka; kedaluwarsa pada Chiasa |
| S03 | data-only | untested |
| S04 | data-only | untested |
| S05 | data-only | untested |
| S06 | data-only | untested |
| S07 | data-only | untested |
| S08 | data-only | untested |
| S09 | data-only | untested |
| S10 | data-only | untested |
| S11 | data-only | untested |
| S12 | data-only | untested |
| S13 | data-only | untested |
| S14 | data-only | untested |
| S15 | data-only | untested |
| S16 | data-only | untested |
| S17 | data-only | untested |
| S18 | data-only | untested |
| S19 | data-only | untested |
| S20 | data-only | untested |
| S21 | data-only | untested |
| S22 | data-only | untested |
| S23 | data-only | untested |
| S24 | data-only | untested |
| S25 | data-only | untested |
| N01 | implemented | Cabang A, dua host |
| N02 | partial | B, Yutaka |
| N03 | implemented | Cabang A, dua host |
| N04 | partial | Efek B, tertunda 14 hari |
| N05 | data-only | untested |
| N06 | partial | untested |
| N07 | data-only | untested |
| N08 | data-only | untested |
| N09 | data-only | untested |
| N10 | data-only | untested |
| N11 | data-only | untested |
| N12 | data-only | untested |
| N13 | data-only | untested |
| N14 | data-only | untested |
| N15 | data-only | untested |
| N16 | data-only | untested |
| N17 | data-only | untested |
| N18 | data-only | untested |
| N19 | data-only | untested |
| N20 | data-only | untested |
| N21 | data-only | untested |
| N22 | partial | untested |
| N23 | data-only | untested |
| N24 | data-only | untested |
| Mi01 | implemented | Cabang A, dua host |
| Mi02 | partial | A, Yutaka |
| Mi03 | implemented | Cabang A, dua host |
| Mi04 | data-only | untested |
| Mi05 | partial | untested |
| Mi06 | data-only | untested |
| Mi07 | partial | Cabang A, dua host |
| Mi08 | data-only | untested |
| Mi09 | partial | untested |
| Mi10 | data-only | untested |
| Mi11 | data-only | untested |
| Mi12 | data-only | untested |
| Mi13 | data-only | untested |
| Mi14 | data-only | untested |
| Mi15 | data-only | untested |
| Mi16 | data-only | untested |
| Mi17 | data-only | untested |
| Mi18 | partial | untested |
| Mi19 | data-only | untested |
| Mi20 | data-only | untested |
| Mi21 | data-only | untested |
| Mi22 | data-only | untested |
| Mi23 | data-only | untested |
| Mi24 | data-only | untested |
| Mi25 | partial | Cabang A, dua host |
| Mi26 | data-only | untested |
| Mi27 | data-only | untested |

### Event dinamis

8 dari 128 ID mempunyai referensi langsung dalam alur atau resolver. Katalog memuat 393 alternatif tertulis pada seluruh ID.

| ID | Implementasi | Bukti |
| --- | --- | --- |
| Mi-D01 | partial | untested |
| Mi-D02 | data-only | untested |
| Mi-D03 | partial | untested |
| Mi-D04 | data-only | untested |
| Mi-D05 | data-only | untested |
| Mi-D06 | data-only | untested |
| Mi-D07 | data-only | untested |
| Mi-D08 | data-only | untested |
| Mi-D09 | data-only | untested |
| Mi-D10 | data-only | untested |
| Mi-D11 | data-only | untested |
| Mi-D12 | data-only | untested |
| Mi-D13 | data-only | untested |
| Mi-D14 | data-only | untested |
| N-D01 | partial | untested |
| N-D02 | partial | untested |
| N-D03 | partial | A, Chiasa; absen dan kedaluwarsa pada Yutaka |
| N-D04 | data-only | untested |
| N-D05 | data-only | untested |
| N-D06 | data-only | untested |
| N-D07 | data-only | untested |
| N-D08 | partial | A setelah N02-B, Yutaka |
| N-D09 | data-only | untested |
| N-D10 | data-only | untested |
| N-D11 | data-only | untested |
| N-D12 | data-only | untested |
| N-D13 | data-only | untested |
| H-D01 | partial | B pada Yutaka, A pada Chiasa; akses dapur berbeda |
| H-D02 | data-only | untested |
| H-D03 | data-only | untested |
| H-D04 | data-only | untested |
| H-D05 | partial | A setelah H03-C, Yutaka |
| H-D06 | data-only | untested |
| H-D07 | data-only | untested |
| H-D08 | data-only | untested |
| H-D09 | data-only | untested |
| H-D10 | data-only | untested |
| H-D11 | data-only | untested |
| H-D12 | data-only | untested |
| Mo-D01 | data-only | untested |
| Mo-D02 | data-only | untested |
| Mo-D03 | data-only | untested |
| Mo-D04 | data-only | untested |
| Mo-D05 | data-only | untested |
| Mo-D06 | data-only | untested |
| Mo-D07 | data-only | untested |
| Mo-D08 | data-only | untested |
| Mo-D09 | data-only | untested |
| Mo-D10 | data-only | untested |
| Mo-D11 | data-only | untested |
| Mo-D12 | data-only | untested |
| Mo-D13 | data-only | untested |
| S-D01 | data-only | untested |
| S-D02 | data-only | untested |
| S-D03 | data-only | untested |
| S-D04 | data-only | untested |
| S-D05 | data-only | untested |
| S-D06 | data-only | untested |
| S-D07 | data-only | untested |
| S-D08 | data-only | untested |
| S-D09 | data-only | untested |
| S-D10 | data-only | untested |
| S-D11 | data-only | untested |
| S-D12 | data-only | untested |
| S-D13 | data-only | untested |
| S-D14 | data-only | untested |
| S-D15 | data-only | untested |
| S-D16 | data-only | untested |
| S-D17 | data-only | untested |
| C-D01 | data-only | untested |
| C-D02 | data-only | untested |
| C-D03 | data-only | untested |
| C-D04 | data-only | untested |
| C-D05 | data-only | untested |
| C-D06 | data-only | untested |
| C-D07 | data-only | untested |
| C-D08 | data-only | untested |
| C-D09 | data-only | untested |
| C-D10 | data-only | untested |
| C-D11 | data-only | untested |
| C-D12 | data-only | untested |
| C-D13 | data-only | untested |
| C-D14 | data-only | untested |
| C-D15 | data-only | untested |
| K-D01 | data-only | untested |
| K-D02 | data-only | untested |
| K-D03 | data-only | untested |
| K-D04 | data-only | untested |
| K-D05 | data-only | untested |
| K-D06 | data-only | untested |
| K-D07 | data-only | untested |
| K-D08 | data-only | untested |
| K-D09 | data-only | untested |
| K-D10 | data-only | untested |
| K-D11 | data-only | untested |
| K-D12 | data-only | untested |
| K-D13 | data-only | untested |
| K-D14 | data-only | untested |
| K-D15 | data-only | untested |
| K-D16 | data-only | untested |
| K-D17 | data-only | untested |
| K-D18 | data-only | untested |
| K-D19 | data-only | untested |
| K-D20 | data-only | untested |
| K-D21 | data-only | untested |
| Y-D01 | data-only | untested |
| Y-D02 | data-only | untested |
| Y-D03 | data-only | untested |
| Y-D04 | data-only | untested |
| Y-D05 | data-only | untested |
| Y-D06 | data-only | untested |
| Y-D07 | data-only | untested |
| Y-D08 | data-only | untested |
| Y-D09 | data-only | untested |
| Y-D10 | data-only | untested |
| Y-D11 | data-only | untested |
| X-D01 | data-only | untested |
| X-D02 | data-only | untested |
| X-D03 | data-only | untested |
| X-D04 | data-only | untested |
| X-D05 | data-only | untested |
| X-D06 | data-only | untested |
| X-D07 | data-only | untested |
| X-D08 | data-only | untested |
| X-D09 | data-only | untested |
| X-D10 | data-only | untested |
| X-D11 | data-only | untested |
| X-D12 | data-only | untested |

### Ending

22 dari 220 ID mempunyai referensi langsung dalam alur atau resolver.

| ID | Implementasi | Bukti |
| --- | --- | --- |
| E-MI-01 | partial | untested |
| E-MI-02 | data-only | untested |
| E-MI-03 | data-only | untested |
| E-MI-04 | partial | Sesudah Mi25-A, dua host |
| E-MI-05 | partial | untested |
| E-MI-06 | data-only | untested |
| E-MI-07 | data-only | untested |
| E-MI-08 | data-only | untested |
| E-MI-09 | data-only | untested |
| E-MI-10 | data-only | untested |
| E-MI-11 | data-only | untested |
| E-MI-12 | data-only | untested |
| E-MI-13 | partial | untested |
| E-MI-14 | data-only | untested |
| E-NA-01 | partial | untested |
| E-NA-02 | data-only | untested |
| E-NA-03 | data-only | untested |
| E-NA-04 | data-only | untested |
| E-NA-05 | data-only | untested |
| E-NA-06 | data-only | untested |
| E-NA-07 | partial | untested |
| E-NA-08 | data-only | untested |
| E-NA-09 | partial | untested |
| E-NA-10 | data-only | untested |
| E-NA-11 | data-only | untested |
| E-NA-12 | partial | untested |
| E-NA-13 | data-only | untested |
| E-NA-14 | data-only | untested |
| E-HA-01 | partial | Tercapai pada Yutaka, tidak pada perjalanan Chiasa |
| E-HA-02 | data-only | untested |
| E-HA-03 | data-only | untested |
| E-HA-04 | data-only | untested |
| E-HA-05 | data-only | untested |
| E-HA-06 | data-only | untested |
| E-HA-07 | data-only | untested |
| E-HA-08 | data-only | untested |
| E-HA-09 | data-only | untested |
| E-HA-10 | data-only | untested |
| E-HA-11 | data-only | untested |
| E-HA-12 | data-only | untested |
| E-HA-13 | data-only | untested |
| E-HA-14 | data-only | untested |
| E-MO-01 | data-only | untested |
| E-MO-02 | data-only | untested |
| E-MO-03 | data-only | untested |
| E-MO-04 | data-only | untested |
| E-MO-05 | data-only | untested |
| E-MO-06 | data-only | untested |
| E-MO-07 | data-only | untested |
| E-MO-08 | data-only | untested |
| E-MO-09 | data-only | untested |
| E-MO-10 | data-only | untested |
| E-MO-11 | data-only | untested |
| E-MO-12 | data-only | untested |
| E-MO-13 | data-only | untested |
| E-SH-01 | data-only | untested |
| E-SH-02 | data-only | untested |
| E-SH-03 | data-only | untested |
| E-SH-04 | data-only | untested |
| E-SH-05 | data-only | untested |
| E-SH-06 | data-only | untested |
| E-SH-07 | data-only | untested |
| E-SH-08 | data-only | untested |
| E-SH-09 | data-only | untested |
| E-SH-10 | data-only | untested |
| E-SH-11 | data-only | untested |
| E-SH-12 | data-only | untested |
| E-SH-13 | data-only | untested |
| E-SH-14 | data-only | untested |
| E-SH-15 | data-only | untested |
| E-SH-16 | data-only | untested |
| E-CH-01 | data-only | untested |
| E-CH-02 | data-only | untested |
| E-CH-03 | data-only | untested |
| E-CH-04 | data-only | untested |
| E-CH-05 | data-only | untested |
| E-CH-06 | data-only | untested |
| E-CH-07 | data-only | untested |
| E-CH-08 | data-only | untested |
| E-CH-09 | data-only | untested |
| E-CH-10 | data-only | untested |
| E-CH-11 | data-only | untested |
| E-CF-01 | data-only | untested |
| E-CF-02 | data-only | untested |
| E-CF-03 | data-only | untested |
| E-CF-04 | data-only | untested |
| E-CF-05 | data-only | untested |
| E-CF-06 | data-only | untested |
| E-CF-07 | data-only | untested |
| E-CF-08 | data-only | untested |
| E-CF-09 | data-only | untested |
| E-CF-10 | partial | untested |
| E-CF-11 | data-only | untested |
| E-CF-12 | data-only | untested |
| E-CF-13 | data-only | untested |
| E-KO-01 | data-only | untested |
| E-KO-02 | data-only | untested |
| E-KO-03 | data-only | untested |
| E-KO-04 | data-only | untested |
| E-KO-05 | data-only | untested |
| E-KO-06 | data-only | untested |
| E-KO-07 | data-only | untested |
| E-KO-08 | data-only | untested |
| E-KO-09 | data-only | untested |
| E-KO-10 | data-only | untested |
| E-KO-11 | data-only | untested |
| E-KO-12 | data-only | untested |
| E-KO-13 | data-only | untested |
| E-KO-14 | data-only | untested |
| E-KO-15 | data-only | untested |
| E-KO-16 | data-only | untested |
| E-KO-17 | data-only | untested |
| E-KO-18 | data-only | untested |
| E-KO-19 | data-only | untested |
| E-KO-20 | data-only | untested |
| E-KO-21 | data-only | untested |
| E-BL-01 | data-only | untested |
| E-BL-02 | data-only | untested |
| E-BL-03 | data-only | untested |
| E-BL-04 | data-only | untested |
| E-BL-05 | data-only | untested |
| E-BL-06 | data-only | untested |
| E-BL-07 | data-only | untested |
| E-BL-08 | data-only | untested |
| E-YH-01 | data-only | untested |
| E-YH-02 | partial | untested |
| E-YH-03 | data-only | untested |
| E-YH-04 | data-only | untested |
| E-YH-05 | data-only | untested |
| E-YH-06 | partial | untested |
| E-YH-07 | data-only | untested |
| E-YU-01 | data-only | untested |
| E-YU-02 | data-only | untested |
| E-YU-03 | data-only | untested |
| E-YU-04 | data-only | untested |
| E-YU-05 | data-only | untested |
| E-YU-06 | data-only | untested |
| E-YU-07 | data-only | untested |
| E-YU-08 | data-only | untested |
| E-FO-01 | data-only | untested |
| E-FO-02 | data-only | untested |
| E-FO-03 | data-only | untested |
| E-FO-04 | data-only | untested |
| E-FO-05 | data-only | untested |
| E-FO-06 | data-only | untested |
| E-FO-07 | data-only | untested |
| E-FO-08 | data-only | untested |
| E-FO-09 | data-only | untested |
| E-FO-10 | data-only | untested |
| E-FO-11 | data-only | untested |
| E-FO-12 | data-only | untested |
| E-FO-13 | data-only | untested |
| E-FO-14 | data-only | untested |
| E-FO-15 | data-only | untested |
| E-SI-01 | partial | untested |
| E-SI-02 | partial | untested |
| E-SI-03 | partial | untested |
| E-SI-04 | data-only | untested |
| E-SI-05 | partial | untested |
| E-SI-06 | partial | untested |
| E-SI-07 | data-only | untested |
| E-SI-08 | data-only | untested |
| E-SI-09 | data-only | untested |
| E-SI-10 | data-only | untested |
| E-SI-11 | data-only | untested |
| E-SI-12 | data-only | untested |
| E-SI-13 | partial | Evaluasi, dua host |
| E-SI-14 | data-only | untested |
| E-SI-15 | data-only | untested |
| E-SI-16 | data-only | untested |
| E-SI-17 | data-only | untested |
| E-SI-18 | partial | untested |
| E-HP-01 | partial | untested |
| E-HP-02 | partial | untested |
| E-HP-03 | data-only | untested |
| E-HP-04 | data-only | untested |
| E-HP-05 | partial | untested |
| E-HP-06 | data-only | untested |
| E-HP-07 | data-only | untested |
| E-NPC-01 | data-only | untested |
| E-NPC-02 | data-only | untested |
| E-NPC-03 | data-only | untested |
| E-NPC-04 | data-only | untested |
| E-NPC-05 | data-only | untested |
| E-NPC-06 | data-only | untested |
| E-NPC-07 | data-only | untested |
| E-NPC-08 | data-only | untested |
| E-NPC-09 | data-only | untested |
| E-NPC-10 | data-only | untested |
| E-NPC-11 | data-only | untested |
| E-NPC-12 | data-only | untested |
| E-NPC-13 | data-only | untested |
| E-NPC-14 | data-only | untested |
| E-NPC-15 | data-only | untested |
| E-NPC-16 | data-only | untested |
| E-NPC-17 | data-only | untested |
| E-NPC-18 | data-only | untested |
| E-NPC-19 | data-only | untested |
| E-NPC-20 | data-only | untested |
| E-NPC-21 | data-only | untested |
| E-NPC-22 | data-only | untested |
| E-NPC-23 | data-only | untested |
| E-NPC-24 | data-only | untested |
| E-NPC-25 | data-only | untested |
| E-NPC-26 | data-only | untested |
| E-NPC-27 | data-only | untested |
| E-X-01 | data-only | untested |
| E-X-02 | data-only | untested |
| E-X-03 | data-only | untested |
| E-X-04 | data-only | untested |
| E-X-05 | data-only | untested |
| E-X-06 | data-only | untested |
| E-X-07 | data-only | untested |
| E-X-08 | data-only | untested |
| E-X-09 | data-only | untested |
| E-X-10 | data-only | untested |
| E-X-11 | data-only | untested |
| E-X-12 | data-only | untested |
| E-X-13 | data-only | untested |
| E-X-14 | data-only | untested |
