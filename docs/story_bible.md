# NTR — Story Bible (draft 1)

Genre: drama dewasa, slice of life. Tema: pengkhianatan, rasa bersalah, rahasia.
Aturan produksi: semua karakter dewasa (25+). Adegan intim tersirat / fade-to-black, tidak eksplisit.
POV: pemain = pihak ketiga (orang yang masuk ke hubungan orang lain).

## Premis
Arga (28) pindah ke apartemen baru setelah putus dan kena PHK. Tetangga sebelahnya, Nadia (28),
menikah dengan Bima (31) yang hampir tidak pernah di rumah karena proyek kerja. Pernikahan mereka
tidak jahat, hanya sepi. Pemain perlahan jadi bagian dari kesepian itu, dan harus menanggung akibatnya.

Nada: abu-abu secara moral. Tidak ada penjahat murni. Bima bukan monster, Nadia bukan korban
sekaligus bukan pelaku murni, Arga bukan pahlawan. Pemain yang memutuskan sejauh apa dia mau melangkah.

## Karakter
| Nama | Usia | Peran | Catatan |
|---|---|---|---|
| Arga (MC) | 28 | Pemain, penulis lepas | Kesepian, baru putus. Nama bisa diganti pemain. |
| Nadia | 28 | Tetangga, istri Bima | Hangat, menyimpan lelah. Dulu ingin jadi pelukis. |
| Bima | 31 | Suami Nadia | Kerja keras, abai tanpa sadar. Sebenarnya sayang. |
| Kirana | 29 | Sahabat Nadia | Tahu lebih banyak dari yang dia tunjukkan. Bisa jadi sekutu atau ancaman. |
| Raka | 28 | Teman lama Arga | Hati nurani Arga. Blak-blakan. |
| Bu Wati | 60 | Pemilik apartemen | Mata dan telinga gedung. Sumber gosip. |

## Variabel inti
| Variabel | Fungsi |
|---|---|
| closeness | Kedekatan Arga-Nadia (0-20) |
| guilt | Rasa bersalah Arga (0-20) |
| suspicion | Kecurigaan Bima (0-20) |
| secrecy | Seberapa rapi rahasia dijaga (0-20) |
| bima_trust | Hubungan Arga-Bima sebagai tetangga/teman (0-20) |
| kirana_ally | Kirana: -1 musuh, 0 netral, 1 sekutu |
| marriage_health | Kondisi pernikahan Nadia-Bima (0-20), turun kalau Bima terus abai |

Flag: helped_bima, told_raka, nadia_confided, saw_letter, kirana_knows, crossed_line.

## Struktur (7 bab + epilog)
1. Tetangga Baru: pindahan, bertemu Nadia dan Bima.
2. Kopi Pagi: rutinitas kecil, Nadia mulai cerita.
3. Hujan: Bima dinas, Nadia minta ditemani.
4. Garis Batas: titik balik pertama, ada pilihan menjauh atau lanjut.
5. Gosip Gedung: Bu Wati, Kirana mulai curiga.
6. Pulang: Bima kembali, ketegangan makin tinggi.
7. Konfrontasi: semua variabel diuji.
Epilog: ending ditentukan oleh resolve_ending().

## Ending (6)
| Kode | Nama | Syarat kasar |
|---|---|---|
| E1 | Pergi Diam-diam | closeness rendah, guilt tinggi |
| E2 | Rahasia Selamanya | closeness tinggi, secrecy tinggi, suspicion rendah |
| E3 | Terbongkar | suspicion tinggi |
| E4 | Pilihan Nadia | closeness tinggi, marriage_health rendah, kirana_ally = 1 |
| E5 | Semua Kehilangan | closeness, guilt, suspicion semuanya tinggi |
| E6 | True: Melepaskan | helped_bima, guilt tinggi, crossed_line False |

## Aset yang dibutuhkan nanti
Sprite: Arga (opsional), Nadia, Bima, Kirana, Raka, Bu Wati (tiap karakter 3-4 ekspresi).
Background: kamar Arga, lorong apartemen, lift, kafe bawah, balkon, atap, kamar Nadia (siluet saja), jalan hujan.
Musik: tema utama, tenang sehari-hari, tegang, sedih, hujan.
