# Alur Cabang 13 — Katalog Ending

Status: 🟡 usulan. Katalog ini **disusun ulang otomatis** dari tabel Ending di file 01–12. Sumber kebenaran tetap tabel di file rute: kalau kamu merevisi ending, revisi di sana, lalu minta aku menyusun ulang katalog dan diagramnya.
✅ GDD 6H: banyak ending, tidak ada True Ending. ✅ 6N.6: setelah playthrough ada rekap lengkap. ⭐ Tidak ada target yang dipilih di awal; ending ditarik oleh akumulasi poin dan bisa dibelokkan sampai resolusi ([Sistem_Cabang_dan_Poin.md](../Sistem_Cabang_dan_Poin.md) §5).

## 1. Epilog komposit
Ending Kouseikan tidak dipilih dari satu daftar. Setiap lapisan diselesaikan sendiri, lalu dirangkai menjadi satu epilog:

1. **Evaluasi** — nasib pemain (`E-SI`).
2. **Hati pemain** — dengan siapa pemain berakhir, atau tidak dengan siapa pun (`E-HP`).
3. **Koita** — `E-KO`, atau `E-BL` bila Rute BL berhasil.
4. **Enam heroine** — Miyuki, Nagisa, Harumi, Moeka, Shiori, Chiasa. Heroine yang paling dekat dengan pemain di akhir tampil terakhir.
5. **Host** — `E-YH` (Male Route) atau `E-CF` (Female Route).
6. **Host yang menjadi NPC** — `E-CH` (Male Route) atau `E-YU` (Female Route).
7. **NPC sampingan** — `E-NPC`, hanya untuk NPC yang punya hubungan berarti dengan pemain.
8. **Ending kombinasi** — `E-X` bukan pengganti, melainkan **lapisan** yang mengubah nada slide lain (misalnya E-X-04 mengubah semua slide menjadi versi duka).
9. **Kata terakhir Sistem** — berbeda per `sikap_sistem` dan `rapport_sistem`; kosong bila Moeka meninggal.
10. **Rekap playthrough** (✅ 6N.6).

Aturan tambahan 🟡:
- Bila pemain mati, slide host berubah menjadi versi duka: siapa yang datang ke pemakaman, siapa yang lega, apa yang tidak sempat dikatakan.
- Ending `Broken` korban Force selalu mengunci ending romantis korban dengan pelaku.
- Satu karakter hanya mendapat satu ending utama; ending kombinasi menempel di atasnya.

## 2. Hitungan
| Kelompok | Jumlah ending bernama |
|---|---|
| Sistem dan nasib pemain (`E-SI`) | 18 |
| Hati pemain (`E-HP`) | 7 |
| Koita (`E-KO`) | 21 |
| Rute BL (`E-BL`) | 8 |
| Miyuki (`E-MI`) | 14 |
| Nagisa (`E-NA`) | 14 |
| Harumi (`E-HA`) | 14 |
| Moeka (`E-MO`) | 13 |
| Shiori (`E-SH`) | 16 |
| Chiasa (NPC, Male Route) (`E-CH`) | 11 |
| Chiasa (host, Female Route) (`E-CF`) | 13 |
| Yutaka (host, Male Route) (`E-YH`) | 7 |
| Yutaka (NPC, Female Route) (`E-YU`) | 8 |
| Force dan kriminal (`E-FO`) | 15 |
| Rute sampingan NPC (`E-NPC`) | 27 |
| Kombinasi (`E-X`) | 14 |
| **Total** | **220** |

| Jenis | Jumlah |
|---|---|
| Bad | 62 |
| Neutral | 52 |
| Romantis | 39 |
| Khusus | 32 |
| Koita | 14 |
| Distorted | 13 |
| Broken | 8 |

Event dinamis yang bisa memicu belok: **128** (Mi-D 14, N-D 13, H-D 12, Mo-D 13, S-D 17, C-D 15, K-D 21, Y-D 11, X-D 12).

**Batas atas kombinasi epilog** (perkalian kasar, sebelum kombinasi yang saling meniadakan dibuang):
- Male Route: 160.585.641.216 kombinasi.
- Female Route: 157.061.818.368 kombinasi.

Banyak kombinasi itu mustahil (misalnya Koita memilih Miyuki sementara Miyuki bersama pemain), jadi angka sebenarnya jauh lebih kecil. Tetapi praktisnya, hampir setiap playthrough menghasilkan rangkaian epilog yang berbeda.

## 3. Daftar lengkap

### Sistem dan nasib pemain — sumber: [10_Sistem_dan_Evaluasi.md](10_Sistem_dan_Evaluasi.md)
| Kode | Nama | Jenis | Host | Syarat inti |
|---|---|---|---|---|
| E-SI-01 | Kontrak Selesai | Romantis | Y/C | deviasi cukup |
| E-SI-02 | Nyaris | Khusus | Y/C | deviasi tipis di atas ambang |
| E-SI-03 | Penonton Terakhir | Romantis | Y/C | deviasi tinggi; `rapport_sistem` tinggi |
| E-SI-04 | Kontrak Baru | Khusus | Y/C | deviasi tinggi; sikap penyelidik |
| E-SI-05 | Gagal di Bawah Sakura | Bad | Y/C | deviasi kurang; pemain di kampus |
| E-SI-06 | Cinta yang Tidak Dihitung | Bad | C | Chiasa × Yutaka saja ⭐ |
| E-SI-07 | Tubuh Pinjaman Menyerah | Bad | Y/C | mati karena tubuh sebelum wisuda |
| E-SI-08 | Pembangkang | Bad | Y/C | hukuman kritis karena pembangkangan sengaja |
| E-SI-09 | Lolos di Balik Jeruji | Khusus | Y/C | lolos; sedang dipenjara |
| E-SI-10 | Gagal di Balik Jeruji | Bad | Y/C | gagal; sedang dipenjara |
| E-SI-11 | Hidup Tanpa Nama | Khusus | Y/C | lolos; reputasi hancur di semua lingkungan |
| E-SI-12 | Figuran yang Baik | Romantis | Y/C | pemain berhenti memanipulasi dan membantu heroine pulih; mereka lepas dari Koita dan berdiri sendiri |
| E-SI-13 | Kebaikan yang Tidak Dihitung | Bad | Y/C | pemain berbuat baik tetapi deviasi kurang |
| E-SI-14 | Jauh dari Panggung | Khusus | Y/C | pemain di kota atau negara lain saat wisuda |
| E-SI-15 | Pengakuan yang Tidak Dipercaya | Khusus | Y/C | rahasia Sistem dibuka luas; dianggap gila |
| E-SI-16 | Tagihan dari Orang Lain | Bad | Y/C | dibunuh atau dilukai fatal oleh NPC |
| E-SI-17 | Penipu yang Tertipu | Bad | Y/C | hasil yang dinilai hanyalah sandiwara |
| E-SI-18 | Celah yang Tidak Pernah Dicatat | Khusus | Y/C | `koita_bebas_naskah` benar — nyaris mustahil, lihat bagian 11 |

### Hati pemain — sumber: [10_Sistem_dan_Evaluasi.md](10_Sistem_dan_Evaluasi.md)
| Kode | Nama | Jenis | Host | Syarat inti |
|---|---|---|---|---|
| E-HP-01 | Bersama Satu Orang | Romantis | Y/C | satu hubungan romantis bertahan sampai M36 |
| E-HP-02 | Bersama Beberapa Orang | Khusus | Y/C | lebih dari satu hubungan bertahan, terbuka atau rahasia |
| E-HP-03 | Tidak Dapat Siapa-Siapa | Neutral | Y/C | pernah mengejar, tetapi tidak ada yang bertahan |
| E-HP-04 | Ditinggalkan Semua | Bad | Y/C | semua orang yang dikejar pergi karena kebohongan atau luka |
| E-HP-05 | Tidak Pernah Mengejar Siapa Pun | Neutral | Y/C | tidak pernah memulai romansa |
| E-HP-06 | Cinta yang Datang Terlambat | Khusus | Y/C | seseorang mengaku di M35 atau M36 setelah pemain menyerah |
| E-HP-07 | Patah Hati yang Diterima | Neutral | Y/C | ditolak dengan jujur, dan pemain menerimanya |

### Koita — sumber: [07_Koita_dan_BL.md](07_Koita_dan_BL.md)
| Kode | Nama | Jenis | Host | Syarat inti |
|---|---|---|---|---|
| E-KO-01 | Dipilih: Miyuki | Koita | Y/C | Miyuki masih memilih Koita; Koita memilihnya |
| E-KO-02 | Dipilih: Nagisa | Koita | Y/C | `harapan_koita` Nagisa tegak |
| E-KO-03 | Dipilih: Harumi | Koita | Y/C | Harumi tahap ≤ 2; Koita memilihnya |
| E-KO-04 | Dipilih: Moeka | Koita | Y/C | Moeka selamat; hatinya ke Koita |
| E-KO-05 | Dipilih: Shiori | Koita | Y/C | cinta Koita tumbuh di S08 |
| E-KO-06 | Dipilih: Chiasa | Koita | Y/C | Koita Success (NPC atau host) |
| E-KO-07 | Sendiri | Neutral | Y/C | semua heroine menjauh; Koita tidak runtuh |
| E-KO-08 | Tetap Menggantung | Bad | Y/C | pola tidak pernah terbongkar |
| E-KO-09 | Hancur | Bad | Y/C | `pola_koita_publik` tinggi; atau E-SH-09 |
| E-KO-10 | Koita Membalas | Bad | Y/C | manuver balik berhasil; pemain kalah perang reputasi |
| E-KO-11 | Penulis yang Jujur | Neutral | Y/C | K19 dibantu jujur; K20 diisi kebenaran sebagian |
| E-KO-12 | Pergi | Neutral | Y/C | K23-A didukung pergi |
| E-KO-13 | Protagonis yang Terbangun | Khusus | Y/C | `koita_tahu_naskah` percaya |
| E-KO-14 | Persahabatan yang Diakhiri | Neutral | Y/C | Koita tahu semua manipulasi pemain; tidak runtuh |
| E-KO-15 | Toga yang Tidak Dipakai | Bad | Y/C | K19 disabotase atau Koita runtuh di Tahun 3 |
| E-KO-16 | Semua Pergi | Khusus | Y/C | `orbit_koita` 0; sebagian besar heroine pergi sendiri (pola terbongkar atau memilih mandiri); `runtuh_koita` ≥ 80; tanpa penopang |
| E-KO-17 | Pusat yang Berpindah | Khusus | Y/C | `orbit_koita` 0; minimal tiga heroine kini di orbit pemain, karena memilih pemain atau terikat lewat ancaman atau Force ⭐; Koita tahu; `runtuh_koita` ≥ 80 |
| E-KO-18 | Naskah yang Kosong | Khusus | Y/C | syarat E-KO-16 atau E-KO-17; Koita tahu soal naskah dan percaya; plot armor padam (K-D14) |
| E-KO-19 | Yang Tidak Bisa Ia Hentikan | Broken | Y/C | Koita menyaksikan Force; `trust_koita` masih tinggi saat itu (ia masih percaya dan dekat dengan pemain), sehingga ia membeku alih-alih bertindak; korban tidak kembali padanya |
| E-KO-20 | Saksi yang Bersuara | Neutral | Y/C | Koita menyaksikan atau mengetahui Force saat `trust_koita` sudah rendah (sudah lama curiga atau lepas dari pemain), sehingga ia bisa bertindak alih-alih membeku |
| E-KO-21 | Dituduh atas Luka yang Menimpanya | Broken | C | jalur manipulasi pembalikan Chiasa ([06_Chiasa.md](06_Chiasa.md) §14) bertahan; `runtuh_koita` ≥ 80 |

### Rute BL — sumber: [07_Koita_dan_BL.md](07_Koita_dan_BL.md)
| Kode | Nama | Jenis | Host | Syarat inti |
|---|---|---|---|---|
| E-BL-01 | Berkomitmen | Romantis | Y | B6 memilih; dibuka terbuka |
| E-BL-02 | Ditolak dan Retak | Neutral | Y | B6 menolak |
| E-BL-03 | Kembali ke Pola Lama | Neutral | Y | B6 lari; Yutaka mundur |
| E-BL-04 | Kolaps | Bad | Y | semua orang, termasuk Yutaka, mundur darinya |
| E-BL-05 | Rahasia di Apartemen | Romantis | Y | B6 memilih; disembunyikan |
| E-BL-06 | Restu di Meja Makan | Romantis | Y | B6 memilih; Daisuke dan Yoshie menerima |
| E-BL-07 | Kursi Kosong di Rumah Amamiya | Bad | Y | B6 memilih; keluarga menolak |
| E-BL-08 | Ia Lari dari Pintu Itu | Neutral | Y | B4 dominan tanpa kehangatan |

### Miyuki — sumber: [01_Miyuki_Masokis.md](01_Miyuki_Masokis.md)
| Kode | Nama | Jenis | Host | Syarat inti |
|---|---|---|---|---|
| E-MI-01 | Jas Putih yang Ringan | Romantis | Y/C | tahap ≤ 3 atau pulih; Affection dan Trust tinggi ke pemain; tanpa Force; Sena tidak memusuhi |
| E-MI-02 | Dokter Anak | Neutral | Y/C | tahap ≤ 2; karier lancar; hati tidak ke siapa pun |
| E-MI-03 | Kembali ke Koita | Koita | Y/C | Koita memilih Miyuki di K26; tahap ≤ 3 |
| E-MI-04 | Cincin Keluarga Hayase | Neutral | Y/C | Mi25-A atau pemain absen; omiai ditekan |
| E-MI-05 | Kereta Pagi Tanpa Tujuan | Romantis | Y/C | Mi25-C kabur bersama pemain |
| E-MI-06 | Lampu Bangsal Padam | Bad | Y/C | kelelahan ekstrem; tanpa bantuan; CBT gagal |
| E-MI-07 | Kenyamanan yang Salah | Distorted | Y/C | tahap 5 permanen; `arah_luka` pemain |
| E-MI-08 | Penebusan Tanpa Akhir | Distorted | Y/C | tahap 5; `arah_luka` diri |
| E-MI-09 | Menunggu yang Menyakitkan | Distorted | Y/C | tahap 5; `arah_luka` Koita; Koita tetap menggantung |
| E-MI-10 | Cuti Satu Tahun | Neutral | Y/C | pulih sebagian lewat Sato; CBT tertunda |
| E-MI-11 | Pintu yang Ditutup Sena | Bad | Y/C | pemain memanfaatkan di depan umum; Sena memutus |
| E-MI-12 | Napas yang Tertahan | Broken | Y/C | pemain pelaku Force terhadapnya |
| E-MI-13 | Sandiwara yang Jadi Nyata | Romantis | Y/C | pasangan palsu dipertahankan sampai Mi18, lalu diakui jujur |
| E-MI-14 | Sandiwara Terbongkar | Bad | Y/C | pasangan palsu terbongkar oleh Takeru atau orang tua |

### Nagisa — sumber: [02_Nagisa_Yandere.md](02_Nagisa_Yandere.md)
| Kode | Nama | Jenis | Host | Syarat inti |
|---|---|---|---|---|
| E-NA-01 | Maket untuk Dua Orang | Romantis | Y/C | pulih di N17 atau tidak pernah melewati tahap 3; tanpa kebohongan terbongkar; tanpa Force |
| E-NA-02 | Garis yang Ia Gambar Sendiri | Neutral | Y/C | pulih; hati tidak ke siapa pun |
| E-NA-03 | Pengakuan yang Akhirnya Sampai | Koita | Y/C | `harapan_koita` tegak; Koita memilih Nagisa di K26 |
| E-NA-04 | Rumah yang Dibangun di Sekitarmu | Distorted | Y/C | tahap 5; pemain menerimanya |
| E-NA-05 | Kamar yang Dikunci | Bad | Y/C | tahap 4–5; ditinggal; tanpa keluarga |
| E-NA-06 | Garis Merah | Bad | Y/C | tahap 5; N18-B dibiarkan; `sasaran_cemburu` terus didekati pemain |
| E-NA-07 | Pulang ke Rumah Sakurajima | Neutral | Y/C | Haruto sekutu (N21-A) atau N22 dihadiri |
| E-NA-08 | Koko di Tempat Sampah | Neutral | Y/C | pulih, tetapi kecewa pada Koita dan pemain |
| E-NA-09 | Empat Orang di Foto Lama | Neutral | Y/C | tahap ≤ 2; tidak ada pengkhianatan besar di geng masa kecil |
| E-NA-10 | Rival Jadi Kekasih | Romantis | C | Chiasa host; pulih; gengsi kedua pihak runtuh |
| E-NA-11 | Bayangan di Bawah Jendela | Distorted | Y/C | pemain menolak; Nagisa terus menguntit; pemain melapor ke Hanabusa |
| E-NA-12 | Gengsi yang Retak | Broken | Y/C | pemain pelaku Force terhadapnya |
| E-NA-13 | Ambulans di Malam Valentine | Bad | Y/C | N15-B ditolak; tanpa Haruto, keluarga, atau pemain di sisinya |
| E-NA-14 | Senjata yang Kau Arahkan | Distorted | Y/C | `senjata` aktif sampai M35 |

### Harumi — sumber: [03_Harumi_Eksploitasi.md](03_Harumi_Eksploitasi.md)
| Kode | Nama | Jenis | Host | Syarat inti |
|---|---|---|---|---|
| E-HA-01 | Hipotesis yang Terbukti | Romantis | Y/C | `kejelasan_emosi` tinggi; pemain pelindung; tanpa Force |
| E-HA-02 | Laboratorium di Seberang Laut | Neutral | Y/C | studi luar negeri diterima; pulih sebagian |
| E-HA-03 | Data yang Dihapus | Neutral | Y/C | lepas dari Ogawa; tetap di Kouseikan |
| E-HA-04 | Variabel Tetap | Koita | Y/C | Koita memilih Harumi di K26; tahap ≤ 2 |
| E-HA-05 | Persamaan Transaksi | Distorted | Y/C | `validasi_dari` banyak orang; tahap 6 |
| E-HA-06 | Lampu Merah di Distrik Empat | Bad | Y/C | putus kuliah; Ogawa menang atau pergi; tanpa penjaga |
| E-HA-07 | Ogawa Jatuh | Neutral | Y/C | H18-A bersaksi; `bukti_ogawa` cukup |
| E-HA-08 | Ogawa Menang | Bad | Y/C | bukti kurang atau ditutupi; pemain penonton |
| E-HA-09 | Rumah Teh di Kansai | Neutral | Y/C | orang tua Kujo menjadi sekutu (H10, H22) |
| E-HA-10 | Eksperimen yang Kau Mulai | Distorted | Y/C | H12-C atau H13-D; pemain pengeksploitasi |
| E-HA-11 | Rumus Tanpa Variabel Cinta | Neutral | Y/C | `kejelasan_emosi` tinggi; hati tidak ke siapa pun |
| E-HA-12 | Disosiasi | Broken | Y/C | pemain pelaku Force terhadapnya |
| E-HA-13 | Seni dan Sains | Romantis | C | Chiasa host; kolaborasi berjalan sejak Tahun 1 |
| E-HA-14 | Satu Tiket Lagi | Romantis | Y/C | H21-C pemain ikut ke luar negeri |

### Moeka — sumber: [04_Moeka_DeathFlag.md](04_Moeka_DeathFlag.md)
| Kode | Nama | Jenis | Host | Syarat inti |
|---|---|---|---|---|
| E-MO-01 | Belajar Meminta Tolong | Romantis | Y/C | minimal 3 jendela diambil; `andalan_moeka` pemain; janji ditepati; tanpa Force |
| E-MO-02 | Cuti Setahun | Neutral | Y/C | selamat; beasiswa dicabut |
| E-MO-03 | Topeng Sempurna | Distorted | Y/C | selamat; topeng tidak pernah dibuka; pemain satu-satunya andalan |
| E-MO-04 | Malam Tanpa Balasan | Bad | Y/C | Mo25 terlewati |
| E-MO-05 | Tepat Waktu | Koita | Y/C | Mo25-E pemain mengirim Koita, atau `andalan_moeka` Koita dan Koita menjawab |
| E-MO-06 | Rina Mengetuk Pintu | Neutral | Y/C | Mo25-B, atau Rina sekutu sejak Mo18 |
| E-MO-07 | Kontrak Kuga | Distorted | Y/C | Mo23 kontrak dibiarkan; selamat |
| E-MO-08 | Label di Garasi | Neutral | Y/C | berhenti kuliah; stres keluarga turun; Rina sekutu |
| E-MO-09 | Banding yang Dimenangkan | Neutral | Y/C | beasiswa diselamatkan lewat Fujisawa, Sato, atau banding |
| E-MO-10 | Doa yang Tidak Terkabul | Neutral | Y/C | `ayah_status` meninggal; minimal 3 jendela diambil |
| E-MO-11 | Topeng yang Pecah | Broken | Y/C | pemain pelaku Force terhadapnya |
| E-MO-12 | Selamat, Tapi Bukan Karenamu | Neutral | Y/C | pemain melewatkan banyak jendela; orang lain menyelamatkannya |
| E-MO-13 | Ginjal untuk Ayah | Romantis | Y/C | cabang donor diambil; pemain mendampingi |

### Shiori — sumber: [05_Shiori_Revenge.md](05_Shiori_Revenge.md)
| Kode | Nama | Jenis | Host | Syarat inti |
|---|---|---|---|---|
| E-SH-01 | Lawan Tanding Seumur Hidup | Romantis | Y/C | `respek` ≥ 80; Trust ≥ 80; tidak ada kebohongan yang ia temukan sendiri; lulus semua ujiannya; tanpa Force |
| E-SH-02 | Skakmat | Bad | Y/C | tahap 5; sasaran pemain; tanpa pengakuan |
| E-SH-03 | Gencatan Senjata | Neutral | Y/C | pemain mengaku di S22 atau S24 |
| E-SH-04 | Ratu Tanpa Kepercayaan | Distorted | Y/C | tahap 5 tuntas; tidak ada yang ia percaya lagi |
| E-SH-05 | Langkah Koita | Koita | Y/C | cinta Koita tumbuh di S08; Koita memilihnya di K26 |
| E-SH-06 | Sekutu di Papan yang Sama | Neutral | Y/C | pemain memberitahunya soal Sistem; `tahu_sistem` percaya |
| E-SH-07 | Pewaris dengan Caranya Sendiri | Neutral | Y/C | tanpa rute aktif; S17 didukung |
| E-SH-08 | Bidak Bernama Tojo | Distorted | Y/C | S21 Tojo dipakai sampai M35 |
| E-SH-09 | Ratu Menjatuhkan Protagonis | Khusus | Y/C | `sasaran_balas` Koita |
| E-SH-10 | Keadilan yang Tersenyum | Khusus | Y/C | `sasaran_balas` Ogawa, Kuga, atau Mei; pemain memberi bukti |
| E-SH-11 | Jalur Hukum | Broken | Y/C | pemain pelaku Force terhadapnya |
| E-SH-12 | Shena dan Pembacanya | Romantis | C | Chiasa mengaku sebagai Shena sebelum Shiori menemukannya sendiri; `respek` ≥ 70; tanpa kebohongan lain yang ia temukan |
| E-SH-13 | Shena dan Penipunya | Bad | C | Chiasa berbohong soal Shena lalu ketahuan |
| E-SH-14 | Lawan Tanpa Nama | Romantis | Y/C | akun anonim aktif lama; pemain mengaku sendiri sebelum ketahuan; `respek` ≥ 70; tanpa kebohongan lain yang ia temukan |
| E-SH-15 | Pion di Papan Orang Lain | Distorted | Y/C | Shiori memegang semua rahasia pemain tetapi memilih tidak menghancurkannya |
| E-SH-16 | Senyum Terakhir | Bad | Y/C | S-D15 umpan berhasil; pemain membuka rahasia terakhirnya padanya |

### Chiasa (NPC, Male Route) — sumber: [06_Chiasa.md](06_Chiasa.md)
| Kode | Nama | Jenis | Host | Syarat inti |
|---|---|---|---|---|
| E-CH-01 | Rumah Kita Sendiri | Romantis | Y | Yutaka mengejar Chiasa; curiga identitas rendah atau diterima |
| E-CH-02 | Diterima | Koita | Y | Koita Success NPC; Daisuke dan Yoshie menerima |
| E-CH-03 | Berpisah Baik-baik | Neutral | Y | Koita Success NPC; keduanya memilih berpisah |
| E-CH-04 | Dipisah Paksa | Bad | Y | Koita Success NPC; keluarga menolak keras |
| E-CH-05 | Digantung Lagi | Bad | Y | Koita Success NPC; Koita kembali ke pola lama |
| E-CH-06 | Shena Saja | Neutral | Y | tanpa romansa; Chiasa pindah dan fokus seni |
| E-CH-07 | Tersisih Dua Kali | Bad | Y | Rute BL berhasil; Chiasa tidak didekati |
| E-CH-08 | Sekutu Paling Setia | Khusus | Y | Rute BL; Yutaka jujur pada Chiasa sejak awal |
| E-CH-09 | Rumah yang Tidak Aman | Broken | Y | pemain pelaku Force terhadapnya |
| E-CH-10 | Adik yang Kembali | Neutral | Y | tidak ada rute romansa dengan Chiasa; keluarga utuh |
| E-CH-11 | Bukan Piala | Bad | Y | Yutaka merebut Chiasa hanya untuk menyakiti Koita, lalu ketahuan |

### Chiasa (host, Female Route) — sumber: [06_Chiasa.md](06_Chiasa.md)
| Kode | Nama | Jenis | Host | Syarat inti |
|---|---|---|---|---|
| E-CF-01 | Rumah Baru | Romantis | C | yuri dengan heroine utama; deviasi cukup |
| E-CF-02 | Diterima | Koita | C | Koita Success; keluarga menerima |
| E-CF-03 | Berpisah Baik-baik | Neutral | C | Koita Success; keduanya mundur |
| E-CF-04 | Dipisah Paksa | Bad | C | Koita Success; keluarga memisahkan |
| E-CF-05 | Digantung Lagi | Bad | C | Koita Success; Koita kembali menggantung |
| E-CF-06 | Bersama Yutaka | Koita | C | Chiasa × Yutaka |
| E-CF-07 | Nama Pena yang Runtuh | Bad | C | rahasia Shena terbongkar sebagai kebohongan |
| E-CF-08 | Gaya Baru Shena | Romantis | C | pemain belajar menggambar sungguhan sampai layak |
| E-CF-09 | Rumah Amamiya Retak | Bad | C | Koita Success atau kejahatan memecah keluarga |
| E-CF-10 | Studio Sendiri | Neutral | C | tanpa romansa |
| E-CF-11 | Lingkaran yang Runtuh | Bad | C | beberapa hubungan yuri sekaligus terbongkar |
| E-CF-12 | Korban yang Ia Ciptakan | Khusus | C | jalur manipulasi pembalikan (§14); framing bertahan; `nurani_chiasa` < 70 sebelum M35 |
| E-CF-13 | Pengakuan yang Tidak Diminta | Khusus | C | `nurani_chiasa` ≥ 70 sebelum M35; framing pernah terpasang lalu dicabut sendiri |

### Yutaka (host, Male Route) — sumber: [08_Yutaka.md](08_Yutaka.md)
| Kode | Nama | Jenis | Host | Syarat inti |
|---|---|---|---|---|
| E-YH-01 | Pewaris yang Berbeda | Neutral | Y | Y17-A; keluarga berdamai |
| E-YH-02 | Bekerja di Luar | Neutral | Y | Y17-B |
| E-YH-03 | Keluarga Pilihan | Romantis | Y | hubungan dengan keluarga Amamiya tinggi; tanpa kejahatan |
| E-YH-04 | Dicoret | Bad | Y | membangkang keluarga berulang atau skandal besar |
| E-YH-05 | Ketahuan Bukan Yutaka | Khusus | Y | minimal dua orang dekat yakin ia bukan Yutaka |
| E-YH-06 | Pergi Jauh | Neutral | Y | Y17-C magang luar negeri |
| E-YH-07 | Informan yang Menagih | Bad | Y | `daichi_status` penagih |

### Yutaka (NPC, Female Route) — sumber: [08_Yutaka.md](08_Yutaka.md)
| Kode | Nama | Jenis | Host | Syarat inti |
|---|---|---|---|---|
| E-YU-01 | Bersama Chiasa | Romantis | C | Yutaka mengaku; Chiasa menerima |
| E-YU-02 | Mundur ke Luar Negeri | Neutral | C | Yutaka mundur demi Koita |
| E-YU-03 | Retak dan Menutup Diri | Bad | C | Chiasa menolak lalu menggantung |
| E-YU-04 | Sekutu Chiasa | Khusus | C | Chiasa jujur padanya |
| E-YU-05 | Tahu Dipakai | Bad | C | Chiasa memperalat Yutaka dan ia mengetahuinya |
| E-YU-06 | Membela Koita | Neutral | C | Yutaka melihat Chiasa menyakiti Koita |
| E-YU-07 | Pewaris Kisaragi | Bad | C | keluarga menekan di M31; Chiasa tidak hadir |
| E-YU-08 | Sahabat Lagi | Neutral | C | Chiasa menolak dengan jujur dan konsisten |

### Force dan kriminal — sumber: [09_Force_dan_Kriminal.md](09_Force_dan_Kriminal.md)
| Kode | Nama | Jenis | Host | Syarat inti |
|---|---|---|---|---|
| E-FO-01 | Jeruji | Bad | Y/C | laporan atau bukti kuat; investigasi tuntas |
| E-FO-02 | Dikeluarkan dan Hancur Sosial | Bad | Y/C | bukti cukup untuk kampus, tidak cukup untuk penjara |
| E-FO-03 | Lolos tapi Dihantui | Khusus | Y/C | `force_bersih[korban]` bertahan (§10); tidak pernah terbongkar |
| E-FO-04 | Mengaku dan Menjalani Proses | Neutral | Y/C | pelaku mengaku |
| E-FO-05 | Buron | Bad | Y/C | pelaku lari |
| E-FO-06 | Kakak yang Tidak Menunggu Polisi | Bad | Y/C | Haruto, Kuroiwa, atau kerabat lain tahu lebih dulu |
| E-FO-07 | Saksi yang Memeras | Khusus | Y/C | saksi (Daichi atau Mei) menyimpan bukti |
| E-FO-08 | Kasus yang Dibuka Kembali | Khusus | Y/C | bukti ditemukan belakangan |
| E-FO-09 | Kejahatan Berantai | Bad | Y/C | lebih dari satu kejahatan; satu membongkar yang lain |
| E-FO-10 | Skorsing dan Catatan | Neutral | Y/C | hanya kejahatan ringan–sedang |
| E-FO-11 | Saksi di Ambang Pintu | Bad | Y/C | Force disaksikan Koita; korban melapor sendiri, atau `trust_koita` sudah rendah sehingga Koita sendiri mencari bantuan |
| E-FO-12 | Kurungan Tanpa Jeruji | Khusus | Y/C | korban tidak melapor dan tetap terikat pada pemain lewat takut, ancaman, atau ketergantungan |
| E-FO-13 | Kebetulan yang Datang Tepat Waktu | Bad | Y/C | plot armor membawa Koita sebelum terjadi |
| E-FO-14 | Dua Orang yang Diam | Khusus | Y/C | Koita menyaksikan tetapi diam karena takut, malu, atau diancam |
| E-FO-15 | Pembalikan yang Terbongkar | Bad | C | jalur manipulasi pembalikan Chiasa ([06_Chiasa.md](06_Chiasa.md) §14); framing runtuh |

### Rute sampingan NPC — sumber: [11_Rute_Sampingan_NPC.md](11_Rute_Sampingan_NPC.md)
| Kode | Nama | Jenis | Host | Syarat inti |
|---|---|---|---|---|
| E-NPC-01 | Dua Jas Putih | Romantis | Y/C | romansa tulus dengan Sena; Miyuki tidak disakiti |
| E-NPC-02 | Sahabat yang Memilih Sisi | Bad | Y/C | pemain menyakiti Miyuki sambil mendekati Sena |
| E-NPC-03 | Thrift Hari Minggu | Romantis | Y/C | romansa tulus dengan Rina; Moeka selamat |
| E-NPC-04 | Rina Tidak Memaafkan | Bad | Y/C | Moeka meninggal atau disakiti pemain |
| E-NPC-05 | Studio Berdua | Romantis | Y/C | romansa dengan Haruka |
| E-NPC-06 | Rahasia yang Dititipkan | Neutral | C | Haruka tahu rahasia Shena dan menjaganya |
| E-NPC-07 | Pasal yang Membela | Romantis | Y/C | romansa atau aliansi dengan Ayane |
| E-NPC-08 | Rapat Terakhir BEM | Bad | Y/C | Ayane mengetahui manipulasi pemain |
| E-NPC-09 | Redaksi Berdua | Romantis | Y/C | romansa dengan Mei; pemain jujur padanya |
| E-NPC-10 | Headline Terakhir | Bad | Y/C | Mei dipakai lalu dibuang |
| E-NPC-11 | Naskah dan Penyuntingnya | Romantis | C | romansa dengan Mio |
| E-NPC-12 | Kontrak Diputus | Bad | C | hubungan dengan Mio rusak |
| E-NPC-13 | Kakak yang Dipilih | Romantis | Y | romansa dengan Haruto |
| E-NPC-14 | Restu Sakurajima | Neutral | Y/C | Haruto menjadi sekutu |
| E-NPC-15 | Esai untuk Satu Orang | Romantis | Y | romansa dengan Matsuda |
| E-NPC-16 | Saksi yang Menulis | Bad | Y/C | Matsuda membongkar manipulasi pemain |
| E-NPC-17 | Informan yang Setia | Romantis | Y | romansa dengan Daichi |
| E-NPC-18 | Maket Kedua | Romantis | Y | romansa dengan Yuuto |
| E-NPC-19 | Pewaris yang Membangkang | Romantis | Y | romansa dengan Tojo |
| E-NPC-20 | Skandal Omiai | Khusus | Y | romansa dengan Takeru |
| E-NPC-21 | Kafe Pagi | Neutral | Y/C | kerja tetap di Kafe Komorebi |
| E-NPC-22 | Batas Profesional | Neutral | Y/C | pemain mengejar Sato secara romantis |
| E-NPC-23 | Konseling Host | Neutral | Y/C | konseling rutin dengan Sato |
| E-NPC-24 | Kepercayaan Kuroiwa | Neutral | Y/C | Kuroiwa mempercayai pemain |
| E-NPC-25 | Saksi yang Dipercaya | Neutral | Y/C | pemain membantu Hanabusa |
| E-NPC-26 | Penyusup | Khusus | Y/C | penyamaran berhasil; bukti cukup |
| E-NPC-27 | Penyusup yang Tertelan | Bad | Y/C | penyamaran terlalu lama |

### Kombinasi — sumber: [12_Interlock_Antar_Rute.md](12_Interlock_Antar_Rute.md)
| Kode | Nama | Jenis | Host | Syarat inti |
|---|---|---|---|---|
| E-X-01 | Harem yang Runtuh | Bad | Y/C | beberapa hubungan rahasia terbongkar sekaligus di M23 atau M35 |
| E-X-02 | Meja Panjang | Romantis | Y/C | hubungan terbuka yang disepakati semua pihak |
| E-X-03 | Domino Shiori | Bad | Y/C | Shiori tahap 5 dengan `daftar_kebohongan` panjang |
| E-X-04 | Musim Dingin Tanpa Moeka | Bad | Y/C | E-MO-04 |
| E-X-05 | Kursi Kosong di Wisuda | Khusus | Y/C | semua heroine lepas dari Koita |
| E-X-06 | Semua Orang Bebas | Romantis | Y/C | semua heroine pulih dan mandiri; tidak ada yang bersama Koita atau pemain |
| E-X-07 | Melawan Naskah Bersama | Khusus | Y/C | E-KO-13 dan persahabatan atau Rute BL |
| E-X-08 | Pengakuan di Depan Semua | Khusus | Y/C | pemain membuka Sistem kepada seluruh lingkaran di M35 |
| E-X-09 | Dua Tragedi | Bad | Y/C | dua rute distorsi berakhir Bad dan saling memicu |
| E-X-10 | Kota yang Tahu Semuanya | Bad | Y/C | Mei menerbitkan semuanya |
| E-X-11 | Pesta di Rumah Amamiya | Romantis | Y/C | semua pulih; Koita memilih dengan tulus; pemain bersama seseorang; geng masa kecil utuh |
| E-X-12 | Dua Ratu | Bad | Y/C | Shiori Rute Revenge dan Nagisa Rute Yandere sama-sama menargetkan pemain |
| E-X-13 | Tubuh yang Dibayar | Khusus | Y/C | pemain menyelamatkan minimal tiga heroine dari rute distorsi sambil terus memaksa tubuh |
| E-X-14 | Dalang yang Tak Pernah Dicurigai | Khusus | Y/C | `force_bersih[x]` bertahan untuk setiap korban Force; NTR sempurna tercapai ([07_Koita_dan_BL.md](07_Koita_dan_BL.md) §14, [09_Force_dan_Kriminal.md](09_Force_dan_Kriminal.md) §10) |
