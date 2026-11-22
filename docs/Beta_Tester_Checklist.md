# Checklist QA Beta Tester — Kouseikan

Dokumen ini daftar **semua** event utama (190), event dinamis (128), dan ending (220) yang ada di game — total 538 item — supaya beta tester bisa menandai satu per satu sampai semuanya pernah dilihat, tanpa ada yang terlewat.

## Cara pakai dokumen ini

- **Event utama** (kode 2 huruf, misal `K05`, `Mi12`) muncul berurutan mengikuti jalan cerita bulan-ke-bulan. Begitu kamu sampai di scene-nya, pilihan A/B/C/D yang tercantum di sini ADALAH pilihan asli yang akan kamu lihat di layar — centang event-nya kalau sudah sampai di sana, lalu centang tiap pilihan begitu kamu sudah pernah mencobanya (butuh beberapa kali main ulang dari titik itu untuk mencoba semua pilihan, karena satu playthrough cuma bisa ambil satu pilihan per event).
- **Event dinamis** (kode dengan `-D`, misal `Mi-D02`) TIDAK muncul di jadwal tetap — ia baru muncul kalau kondisi di baris **Pemicu** sudah terpenuhi (contoh: angka relasi tertentu, status tertentu). Pakai layar status karakter / HP pelacak lokasi untuk mengecek apakah kondisinya sudah tercapai, lalu datangi karakter itu.
- **Ending** (kode `E-XX-NN`) juga berbasis syarat (baris **Syarat**), BUKAN satu jalur pilihan yang pasti — game ini pakai sistem akumulasi poin (trust/fear/dll) dari banyak cabang, jadi cara memicu satu ending adalah dengan konsisten mengarahkan pilihan-pilihan di sepanjang rute ke arah yang disebut di baris Syarat, sampai kondisinya terpenuhi di titik keputusan akhir karakter itu.
- Tiap karakter punya fitur **HP** (tombol "HP" di layar) yang menampilkan lokasi 8 karakter utama saat itu juga — pakai ini untuk mencari siapa ada di mana sebelum berburu event dinamis.
- Untuk tester yang paham developer console Ren'Py: tekan **Shift+O** lalu `jump kkscene_<ID>` bisa dipakai untuk loncat langsung ke satu scene tanpa main dari awal, supaya pengecekan 538 item ini tidak perlu ditempuh lewat playthrough linear saja. Ini opsional — boleh diabaikan kalau mau main normal dari awal.
- Game ini punya 2 pilihan karakter utama (host): **Amamiya Chiasa** atau **Kisaragi Yutaka**. Event berkode `C..` hanya muncul kalau kamu pilih Chiasa sebagai pemeran utama; event berkode `Y..` hanya muncul kalau pilih Yutaka. Untuk mencentang KEDUA bagian itu, perlu main dua kali (sekali per pilihan host).

## Ringkasan jumlah

- Event utama: 190
- Event dinamis: 128
- Ending: 220
- **Total: 538 item**

## Daftar isi

- [Amamiya Koita](#amamiya-koita)
- [Tachibana Miyuki](#tachibana-miyuki)
- [Sakurajima Nagisa](#sakurajima-nagisa)
- [Kujo Harumi](#kujo-harumi)
- [Kohinata Moeka](#kohinata-moeka)
- [Saionji Shiori](#saionji-shiori)
- [Amamiya Chiasa](#amamiya-chiasa)
- [Kisaragi Yutaka](#kisaragi-yutaka)
- [Lintas Rute / Umum](#lintas-rute--umum)

## Amamiya Koita

_27 event utama · 21 event dinamis · 29 ending_

### Event utama

- [ ] **K01** · bulan M01a · Senyum yang Terlalu Cepat
  - Pemicu: kantin hari pertama; Koita menyapa tiga heroine dengan tiga kalimat berbeda.
  - [ ] Pilihan A — amati dan catat polanya
  - [ ] Pilihan B — tegur terang-terangan
  - [ ] Pilihan C — abaikan.
  - Efek: A membuka pola_koita_dikenal (intel); B membuat Koita waspada ringan; C tidak ada.

- [ ] **K02** · bulan M02 · Kamar yang Tertukar
  - Pemicu: ryokan; plot armor menaruh Koita sekamar dengan satu heroine (ditentukan oleh siapa yang paling siap).
  - [ ] Pilihan A — tukar kamar tanpa ketahuan
  - [ ] Pilihan B — biarkan
  - [ ] Pilihan C — masuk sebagai "gangguan"
  - [ ] Pilihan D — sabotase pembagian kamar.
  - Efek: A–C menggeser Jealousy; D memicu kecurigaan Fujisawa/Rina bila ketahuan.

- [ ] **K03** · bulan M04 · Tanzaku Koita
  - Pemicu: aula Tanabata; tanzaku Koita: "semoga semuanya tetap seperti ini".
  - [ ] Pilihan A — baca diam-diam
  - [ ] Pilihan B — tukar dengan tanzaku lain
  - [ ] Pilihan C — tulis balasan di sebelahnya.
  - Efek: A memberi ketakutan_koita; B bisa menjadi sabotase kecil; C membuat Koita merasa "dilihat".

- [ ] **K04** · bulan M05a · Pertanyaan di Bawah Kembang Api
  - Pemicu: Koita bertanya, "Kalau kamu jadi aku, kamu akan memilih siapa?"
  - [ ] Pilihan A — jawab jujur
  - [ ] Pilihan B — bohong
  - [ ] Pilihan C — balik tanya
  - [ ] Pilihan D — sebut namamu sendiri.
  - Efek: A menambah Trust; B menambah risiko bila ketahuan; D menyalakan jalur BL (Male) atau Koita Success (Female).

- [ ] **K05** · bulan M05b · Malam di Dapur Vila
  - Pemicu: Koita membuat minuman untuk semua; ia memperhatikan siapa yang canggung.
  - [ ] Pilihan A — jelaskan situasi
  - [ ] Pilihan B — ancam ringan
  - [ ] Pilihan C — tertawakan
  - [ ] Pilihan D — alihkan perhatiannya.
  - Efek: C/D menurunkan koita_curiga_1; A–B meningkatkannya.

- [ ] **K06** · bulan M06 · Foto Reuni
  - Pemicu: Koita meminta foto kelompok; ia berdiri di tengah.
  - [ ] Pilihan A — ambil foto
  - [ ] Pilihan B — ikut berfoto dan geser posisi
  - [ ] Pilihan C — ganti fotografer.
  - Efek: foto menjadi bukti digital () tentang siapa dekat siapa.

- [ ] **K07** · bulan M08 · Bazar Sastra
  - Pemicu: klub sastra; Matsuda memajang esai "Tokoh Utama yang Tidak Pernah Memilih".
  - [ ] Pilihan A — baca dan dukung Matsuda
  - [ ] Pilihan B — kritik esainya
  - [ ] Pilihan C — bela Koita.
  - Efek: A menjadikan Matsuda sekutu; B musuh; C membuat Matsuda menjaga jarak.

- [ ] **K08** · bulan M09 · Natal Plot Armor
  - Pemicu: kebetulan Natal mempertemukan Koita dengan heroine paling siap.
  - [ ] Pilihan A — intersep lewat telepon
  - [ ] Pilihan B — ambil alih kencan
  - [ ] Pilihan C — biarkan
  - [ ] Pilihan D — hadir sebagai pihak ketiga.
  - Efek: hub besar #3; menentukan siapa memegang Natal Tahun 1.

- [ ] **K09** · bulan M10 · Omikuji Koita
  - Pemicu: kuil; ia menarik ramalan "pilihanmu akan datang".
  - [ ] Pilihan A — tanyakan
  - [ ] Pilihan B — tertawakan
  - [ ] Pilihan C — ancam.
  - Efek: mulai tumbuh rasa takut; kunci K15.

- [ ] **K10** · bulan M11 · Coklat yang Tidak Habis
  - Pemicu: Valentine; Koita menerima banyak coklat.
  - [ ] Pilihan A — pemain memberi coklat
  - [ ] Pilihan B — amati siapa yang tidak memberi
  - [ ] Pilihan C — bantu menghabiskan.
  - Efek: gerbang BL/Koita Success. Male: A membuka rantai BL. Female: A membuka jalur Chiasa × Koita.

- [ ] **K11** · bulan M12 · Hadiah yang Sama
  - Pemicu: White Day; Koita membalas semua dengan hadiah yang sama.
  - [ ] Pilihan A — kritik
  - [ ] Pilihan B — bantu ganti
  - [ ] Pilihan C — biarkan.
  - Efek: heroine sadar mereka "disamakan"; menaikkan kecurigaan antar heroine.

- [ ] **K12** · bulan M14 · Telepon dari Seberang
  - Pemicu: saat perjalanan Kansai Koita menelepon berulang.
  - [ ] Pilihan A — angkat
  - [ ] Pilihan B — abaikan
  - [ ] Pilihan C — minta heroine yang menjawab.
  - Efek: Jealousy Koita naik; mulai mencari tahu.

- [ ] **K13** · bulan M17a · Yukata Pilihan
  - Pemicu: festival; Koita memilih siapa yang ditemani.
  - [ ] Pilihan A — dukung pilihan
  - [ ] Pilihan B — ganti pilihannya
  - [ ] Pilihan C — hentikan.
  - Efek: konfrontasi kecil antar heroine.

- [ ] **K14** · bulan M18 · Rumor tentang Koita
  - Pemicu: Kurosawa Mei mengunggah rumor bahwa Koita "mempermainkan".
  - [ ] Pilihan A — bantu bantah
  - [ ] Pilihan B — biarkan
  - [ ] Pilihan C — sebarkan lebih jauh
  - [ ] Pilihan D — beli kebungkaman Mei.
  - Efek: reputasi Koita; C bisa memicu rute kehancuran.

- [ ] **K15** · bulan M19 · Panik Pertama
  - Pemicu: Koita meminta waktu: "ada yang aneh."
  - [ ] Pilihan A — pengakuan sebagian
  - [ ] Pilihan B — bohong
  - [ ] Pilihan C — konfrontasi
  - [ ] Pilihan D — manfaatkan kepanikannya.
  - Efek: koita_sadar naik. Mulai manuver balik.

- [ ] **K16** · bulan M21 · Telepon Larut Malam
  - Pemicu: Koita meminta pemain ke rumahnya; ia bercerita tentang ayahnya.
  - [ ] Pilihan A — hadir dan dengarkan
  - [ ] Pilihan B — tolak
  - [ ] Pilihan C — manfaatkan kerapuhannya.
  - Efek: membuka akar sifat; A memperdalam Trust; C memicu Fear.

- [ ] **K17** · bulan M23 · Hari Pengakuan Bentrok
  - Pemicu: beberapa heroine mengaku pada hari yang sama.
  - [ ] Pilihan A — dukung satu heroine
  - [ ] Pilihan B — dorong Koita memilih
  - [ ] Pilihan C — sabotase
  - [ ] Pilihan D — pengakuan BL
  - [ ] Pilihan E — pengakuan Chiasa
  - Efek: hub besar #8; menentukan arah Tahun 3.

- [ ] **K18** · bulan M24 · Daftar Orang yang Kupilih
  - Pemicu: Koita menulis daftar nama.
  - [ ] Pilihan A — baca
  - [ ] Pilihan B — hapus satu nama
  - [ ] Pilihan C — tambahkan namamu.
  - Efek: mengubah target ending Koita.

- [ ] **K19** · bulan M25 · Skripsi: Tokoh yang Tidak Memilih
  - [ ] Pilihan A — bantu
  - [ ] Pilihan B — sabotase
  - [ ] Pilihan C — beri masukan jujur.
  - Efek: A/C membuat Koita menulis lebih jujur; B merusak kepercayaannya.

- [ ] **K20** · bulan M26 · Atap Penginapan
  - Pemicu: Koita mengajak pemain bicara jujur.
  - [ ] Pilihan A — ungkapkan sebagian kebenaran
  - [ ] Pilihan B — diam
  - [ ] Pilihan C — tantang.
  - Efek: Koita bisa mengubah sikap drastis.

- [ ] **K21** · bulan M29a · Yukata Terakhir
  - Pemicu: Koita menolak ditemani siapa pun.
  - [ ] Pilihan A — temani sebagai teman
  - [ ] Pilihan B — temani sebagai lebih
  - [ ] Pilihan C — biarkan.
  - Efek: B bisa membuka jalur BL.

- [ ] **K22** · bulan M29b · Malam Terakhir di Vila
  - Pemicu: Koita menghadapi pemain; percakapan paling jujur.
  - [ ] Pilihan A — pengakuan
  - [ ] Pilihan B — penolakan
  - [ ] Pilihan C — pertengkaran.
  - Efek: menentukan ending BL (Male).

- [ ] **K23** · bulan M31 · Tawaran dari Penerbit
  - [ ] Pilihan A — dukung ia pergi
  - [ ] Pilihan B — minta tinggal
  - [ ] Pilihan C — ikut.
  - Efek: arah karier Koita.

- [ ] **K24** · bulan M32 · Pidato Klub
  - [ ] Pilihan A — hadir
  - [ ] Pilihan B — absen
  - [ ] Pilihan C — mengganggu.
  - Efek: publik melihat siapa dekat dengan siapa.

- [ ] **K25** · bulan M33 · Natal Sendirian
  - [ ] Pilihan A — datang
  - [ ] Pilihan B — kirim orang lain
  - [ ] Pilihan C — biarkan.
  - Efek: ending Koita "Sendiri" jika tak ada yang datang.

- [ ] **K26** · bulan M35 · Pilihan Terakhir Koita
  - Efek: ending Koita: Dipilih / Sendiri / Tetap Menggantung / Hancur.

- [ ] **K27** · bulan M36 · Wisuda
  - Efek: epilog; evaluasi Sistem.

### Event dinamis

- [ ] **K-D01** · Draf yang Tertinggal
  - Pemicu: Koita meninggalkan naskahnya
  - Ringkasan: baca semua / baca sebagian / kembalikan tanpa membaca
  - [ ] Opsi 1 — baca semua
  - [ ] Opsi 2 — baca sebagian
  - [ ] Opsi 3 — kembalikan tanpa membaca
  - Efek: pilihan "Kutip kalimat drafnya" terbuka; intel tentang kesadaran Koita

- [ ] **K-D02** · Jalan Pulang yang Diperpanjang
  - Pemicu: takut_ditinggal ≥ 60
  - Ringkasan: Koita sengaja pulang lewat jalan jauh. Temani / tanya kenapa / biarkan
  - [ ] Opsi 1 — Temani
  - [ ] Opsi 2 — tanya kenapa
  - [ ] Opsi 3 — biarkan
  - Efek: Koita bicara soal rumah; benih BL (Y) atau Koita Success (C)

- [ ] **K-D03** · Uang untuk Hadiah
  - Pemicu: Male Route
  - Ringkasan: Koita meminta uang untuk hadiah salah satu heroine (hadiah, bukan pinjaman ). Beri / tolak / tanya untuk siapa
  - [ ] Opsi 1 — Beri
  - [ ] Opsi 2 — tolak
  - [ ] Opsi 3 — tanya untuk siapa
  - Efek: intel pilihan_koita[[x]

- [ ] **K-D04** · Dua Pesan yang Sama
  - Pemicu: pemain melihat ponsel dua heroine
  - Ringkasan: Koita mengirim kalimat yang sama ke dua orang. Simpan tangkapan layar / hadapi Koita / abaikan
  - [ ] Opsi 1 — Simpan tangkapan layar
  - [ ] Opsi 2 — hadapi Koita
  - [ ] Opsi 3 — abaikan
  - Efek: bukti pola; pola_publik naik bila disebar

- [ ] **K-D05** · Senyum yang Berhenti
  - Pemicu: koita_sadar ≥ 50
  - Ringkasan: pemain melihat Koita berhenti tersenyum saat mengira tak ada yang melihat. Sapa / pura-pura tidak lihat / catat
  - [ ] Opsi 1 — Sapa
  - [ ] Opsi 2 — pura-pura tidak lihat
  - [ ] Opsi 3 — catat
  - Efek: Trust atau intel

- [ ] **K-D06** · Debat di Klub Sastra
  - Pemicu: Matsuda sekutu (K07-A)
  - Ringkasan: Matsuda menantang Koita di depan klub. Dukung Matsuda / bela Koita / tetap diam
  - [ ] Opsi 1 — Dukung Matsuda
  - [ ] Opsi 2 — bela Koita
  - [ ] Opsi 3 — tetap diam
  - Efek: pola_publik ±

- [ ] **K-D07** · Pelukan di Stasiun
  - Pemicu: Male Route; ikatan_bl ≥ 50
  - Ringkasan: Koita memeluk Yutaka setelah menjemputnya. Balas / tahan jarak / bercanda
  - [ ] Opsi 1 — Balas
  - [ ] Opsi 2 — tahan jarak
  - [ ] Opsi 3 — bercanda
  - Efek: rantai BL maju atau tertahan

- [ ] **K-D08** · Ponsel Pemain di Meja
  - Pemicu: pemain meninggalkan ponsel
  - Ringkasan: Koita membaca pesan pemain dengan heroine. Saat pemain kembali: hadapi / jelaskan / pura-pura tidak tahu
  - [ ] Opsi 1 — Saat pemain kembali: hadapi
  - [ ] Opsi 2 — jelaskan
  - [ ] Opsi 3 — pura-pura tidak tahu
  - Efek: koita_sadar +25; manuver balik dimulai lebih awal

- [ ] **K-D09** · Foto Ayah
  - Pemicu: setelah K16-A
  - Ringkasan: Koita menunjukkan foto ayahnya. Dengarkan / bandingkan dengan dirimu / alihkan
  - [ ] Opsi 1 — Dengarkan
  - [ ] Opsi 2 — bandingkan dengan dirimu
  - [ ] Opsi 3 — alihkan
  - Efek: akar sifat menggantung; rasa_bersalah_koita +

- [ ] **K-D10** · Kebetulan yang Gagal Tiga Kali
  - Pemicu: plot_armor_tekanan ≥ 75
  - Ringkasan: "Rasanya ada yang mengambil tempatku." Tertawakan / akui sebagian / ceritakan Sistem
  - [ ] Opsi 1 — " Tertawakan
  - [ ] Opsi 2 — akui sebagian
  - [ ] Opsi 3 — ceritakan Sistem
  - Efek: koita_sadar +; jalur E-KO-13

- [ ] **K-D11** · Pilihan Lebih Awal
  - Pemicu: pilihan_koita[[x] ≥ 80; koita_sadar ≥ 75
  - Ringkasan: Koita memilih seseorang di M30, bukan M35. Dukung / halangi / diam
  - [ ] Opsi 1 — Dukung
  - [ ] Opsi 2 — halangi
  - [ ] Opsi 3 — diam
  - Efek: belok besar bagi heroine itu

- [ ] **K-D12** · Gladi Resik Pidato
  - Pemicu: menjelang M36
  - Ringkasan: Koita meminta pendapat soal pidato wisudanya. Jujur / memuji / menulis ulang untuknya
  - [ ] Opsi 1 — Jujur
  - [ ] Opsi 2 — memuji
  - [ ] Opsi 3 — menulis ulang untuknya
  - Efek: nada epilog Koita berubah

- [ ] **K-D13** · Nama yang Dicoret
  - Pemicu: orbit_koita ≤ 2
  - Ringkasan: Koita mencoret nama di daftar K18 satu per satu. Lihat diam-diam / ambil daftarnya / tulis namamu sendiri di sana
  - [ ] Opsi 1 — Lihat diam-diam
  - [ ] Opsi 2 — ambil daftarnya
  - [ ] Opsi 3 — tulis namamu sendiri di sana
  - Efek: runtuh_koita +; pemain tahu siapa yang tersisa

- [ ] **K-D14** · Kebetulan yang Tidak Datang Lagi
  - Pemicu: plot_armor_tekanan ≥ 90; orbit_koita ≤ 1
  - Ringkasan: Koita menunggu di tempat kebetulan biasa terjadi, dan tidak ada yang datang. Datangi dia / biarkan / kirim heroine yang tersisa
  - [ ] Opsi 1 — Datangi dia
  - [ ] Opsi 2 — biarkan
  - [ ] Opsi 3 — kirim heroine yang tersisa
  - Efek: plot armor padam; jalur E-KO-18

- [ ] **K-D15** · Dari Seberang Jalan
  - Pemicu: heroine yang dulu di orbit Koita sedang bersama pemain di tempat umum
  - Ringkasan: Koita melihat dari seberang jalan, dan pemain menyadarinya. Pamer / pura-pura tidak lihat / hampiri dan jelaskan
  - [ ] Opsi 1 — Pamer
  - [ ] Opsi 2 — pura-pura tidak lihat
  - [ ] Opsi 3 — hampiri dan jelaskan
  - Efek: runtuh_koita +15 / +5 / ±; pamer menaikkan Fear dan rumor

- [ ] **K-D16** · Pengakuan yang Disengaja
  - Pemicu: pemain memutuskan memberi tahu Koita semuanya
  - Ringkasan: ceritakan dengan tenang / dengan mengejek / tunjukkan buktinya
  - [ ] Opsi 1 — ceritakan dengan tenang
  - [ ] Opsi 2 — dengan mengejek
  - [ ] Opsi 3 — tunjukkan buktinya
  - Efek: runtuh_koita +20 sampai +40; Koita runtuh atau berbalik melawan (E-KO-10, E-KO-20)

- [ ] **K-D17** · Yang Ia Temukan Setelahnya
  - Pemicu: Koita mengetahui Force setelah kejadian, bukan menyaksikan
  - Ringkasan: Koita menemukan heroine dalam keadaan hancur. Pemain ada di sana: sangkal / diam / mengaku
  - [ ] Opsi 1 — Pemain ada di sana: sangkal
  - [ ] Opsi 2 — diam
  - [ ] Opsi 3 — mengaku
  - Efek: rasa bersalah Koita; bukti; jalur E-KO-19 atau E-KO-20

- [ ] **K-D18** · Draf Terakhir
  - Pemicu: runtuh_koita ≥ 60
  - Ringkasan: Koita menghapus semua tulisannya. Selamatkan filenya / biarkan / baca halaman terakhirnya
  - [ ] Opsi 1 — Selamatkan filenya
  - [ ] Opsi 2 — biarkan
  - [ ] Opsi 3 — baca halaman terakhirnya
  - Efek: dibiarkan: ambisi_menulis nol; halaman terakhir berisi nama-nama heroine

- [ ] **K-D19** · Telepon Yoshie
  - Pemicu: runtuh_koita ≥ 60
  - Ringkasan: ibunya menelepon dari luar negeri dan bertanya pada pemain apa yang terjadi. Jujur / bohong / minta ia pulang
  - [ ] Opsi 1 — Jujur
  - [ ] Opsi 2 — bohong
  - [ ] Opsi 3 — minta ia pulang
  - Efek: Yoshie pulang: penopang, belok ke E-KO-07; bohong: runtuh berlanjut

- [ ] **K-D20** · Matsuda Mengetuk
  - Pemicu: runtuh_koita ≥ 70; Matsuda sekutu Koita
  - Ringkasan: Matsuda membawa Koita ke Sato Kyoko. Halangi / biarkan / ikut
  - [ ] Opsi 1 — Halangi
  - [ ] Opsi 2 — biarkan
  - [ ] Opsi 3 — ikut
  - Efek: pemulihan: belok dari E-KO-16 ke E-KO-07

- [ ] **K-D21** · Satu yang Tidak Ikut Percaya
  - Pemicu: framing_koita terpasang (06_Chiasa.md §14)
  - Ringkasan: Matsuda, atau satu orang lain yang mengenalnya lama, menolak ikut menuduhnya. Terima dukungan itu / tolak karena malu / minta mereka diam saja
  - [ ] Opsi 1 — Terima dukungan itu
  - [ ] Opsi 2 — tolak karena malu
  - [ ] Opsi 3 — minta mereka diam saja
  - Efek: menerima: runtuh_koita −15, dan orang itu bisa menjadi saksi yang meruntuhkan framing; menolak: makin sendirian; minta diam: tertunda, bukan dihapus

### Ending

- [ ] **E-BL-01** · Berkomitmen _(Romantis, host Y)_
  - Syarat: B6 memilih; dibuka terbuka
  - Isi: Koita berhenti menggantung dan memilih Yutaka

- [ ] **E-BL-02** · Ditolak dan Retak _(Neutral, host Y)_
  - Syarat: B6 menolak
  - Isi: persahabatan sejak kecil retak

- [ ] **E-BL-03** · Kembali ke Pola Lama _(Neutral, host Y)_
  - Syarat: B6 lari; Yutaka mundur
  - Isi: Koita kembali menggantung semua orang, termasuk Yutaka

- [ ] **E-BL-04** · Kolaps _(Bad, host Y)_
  - Syarat: semua orang, termasuk Yutaka, mundur darinya
  - Isi: Koita kolaps setelah sendirian

- [ ] **E-BL-05** · Rahasia di Apartemen _(Romantis, host Y)_
  - Syarat: B6 memilih; disembunyikan
  - Isi: hubungan berlanjut diam-diam; Chiasa tahu

- [ ] **E-BL-06** · Restu di Meja Makan _(Romantis, host Y)_
  - Syarat: B6 memilih; Daisuke dan Yoshie menerima
  - Isi: makan malam keluarga dengan satu kursi tambahan yang kini resmi

- [ ] **E-BL-07** · Kursi Kosong di Rumah Amamiya _(Bad, host Y)_
  - Syarat: B6 memilih; keluarga menolak
  - Isi: Koita meninggalkan rumah dan tinggal di apartemen Yutaka

- [ ] **E-BL-08** · Ia Lari dari Pintu Itu _(Neutral, host Y)_
  - Syarat: B4 dominan tanpa kehangatan
  - Isi: Koita kabur dari Yutaka dan dari semuanya

- [ ] **E-KO-01** · Dipilih: Miyuki _(Koita, host Y/C)_
  - Syarat: Miyuki masih memilih Koita; Koita memilihnya
  - Isi: jalur manga; cinta SMA Koita akhirnya diakui

- [ ] **E-KO-02** · Dipilih: Nagisa _(Koita, host Y/C)_
  - Syarat: harapan_koita Nagisa tegak
  - Isi: teman masa kecil yang akhirnya dijawab

- [ ] **E-KO-03** · Dipilih: Harumi _(Koita, host Y/C)_
  - Syarat: Harumi tahap ≤ 2; Koita memilihnya
  - Isi: variabel tetap

- [ ] **E-KO-04** · Dipilih: Moeka _(Koita, host Y/C)_
  - Syarat: Moeka selamat; hatinya ke Koita
  - Isi: Koita belajar menepati janji

- [ ] **E-KO-05** · Dipilih: Shiori _(Koita, host Y/C)_
  - Syarat: cinta Koita tumbuh di S08
  - Isi: lawan yang ia kira tak tersentuh

- [ ] **E-KO-06** · Dipilih: Chiasa _(Koita, host Y/C)_
  - Syarat: Koita Success (NPC atau host)
  - Isi: tabu saudara tiri; lihat file 06

- [ ] **E-KO-07** · Sendiri _(Neutral, host Y/C)_
  - Syarat: semua heroine menjauh; Koita tidak runtuh
  - Isi: kehilangan semuanya, mulai bertumbuh

- [ ] **E-KO-08** · Tetap Menggantung _(Bad, host Y/C)_
  - Syarat: pola tidak pernah terbongkar
  - Isi: pola lama berlanjut dengan korban baru

- [ ] **E-KO-09** · Hancur _(Bad, host Y/C)_
  - Syarat: pola_koita_publik tinggi; atau E-SH-09
  - Isi: lingkungan menjauh setelah sifat aslinya terbukti

- [ ] **E-KO-10** · Koita Membalas _(Bad, host Y/C)_
  - Syarat: manuver balik berhasil; pemain kalah perang reputasi
  - Isi: Koita merebut balik heroine dan menjatuhkan pemain di mata semua orang

- [ ] **E-KO-11** · Penulis yang Jujur _(Neutral, host Y/C)_
  - Syarat: K19 dibantu jujur; K20 diisi kebenaran sebagian
  - Isi: berhenti menggantung; menulis novel tentang tokoh yang tidak pernah memilih

- [ ] **E-KO-12** · Pergi _(Neutral, host Y/C)_
  - Syarat: K23-A didukung pergi
  - Isi: menerima tawaran penerbit di kota lain dan meninggalkan semuanya

- [ ] **E-KO-13** · Protagonis yang Terbangun _(Khusus, host Y/C)_
  - Syarat: koita_tahu_naskah percaya
  - Isi: Koita sengaja melawan plot armor-nya; pilihannya kini benar-benar miliknya

- [ ] **E-KO-14** · Persahabatan yang Diakhiri _(Neutral, host Y/C)_
  - Syarat: Koita tahu semua manipulasi pemain; tidak runtuh
  - Isi: ia memutus pemain dengan tenang dan tidak pernah kembali

- [ ] **E-KO-15** · Toga yang Tidak Dipakai _(Bad, host Y/C)_
  - Syarat: K19 disabotase atau Koita runtuh di Tahun 3
  - Isi: Koita gagal lulus tepat waktu; evaluasi tetap di tanggal wisuda angkatannya

- [ ] **E-KO-16** · Semua Pergi _(Khusus, host Y/C)_
  - Syarat: orbit_koita 0; sebagian besar heroine pergi sendiri (pola terbongkar atau memilih mandiri); runtuh_koita ≥ 80; tanpa penopang
  - Isi: NTR sempurna: tidak ada satu pun yang tersisa. Koita berhenti menulis dan kuliah, mengurung diri, kena mental; ditulis lewat kondisi dan dampaknya

- [ ] **E-KO-17** · Pusat yang Berpindah _(Khusus, host Y/C)_
  - Syarat: orbit_koita 0; minimal tiga heroine kini di orbit pemain, karena memilih pemain atau terikat lewat ancaman atau Force ; Koita tahu; runtuh_koita ≥ 80
  - Isi: NTR sempurna: lingkaran yang dulu berputar di sekitar Koita kini berputar di sekitar pemain, dan Koita menjadi figuran di ceritanya sendiri. Slide tiap heroine berbeda: yang memilih pemain tampak bahagia, yang dipaksa tampak hancur

- [ ] **E-KO-18** · Naskah yang Kosong _(Khusus, host Y/C)_
  - Syarat: syarat E-KO-16 atau E-KO-17; Koita tahu soal naskah dan percaya; plot armor padam (K-D14)
  - Isi: Koita sadar ia protagonis yang ditinggalkan naskahnya sendiri; kebetulan tidak pernah datang lagi. Sistem membacakan: "Protagonis selesai."

- [ ] **E-KO-19** · Yang Tidak Bisa Ia Hentikan _(Broken, host Y/C)_
  - Syarat: Koita menyaksikan Force; trust_koita masih tinggi saat itu (ia masih percaya dan dekat dengan pemain), sehingga ia membeku alih-alih bertindak; korban tidak kembali padanya
  - Isi: trauma karena gagal melindungi orang yang masih ia percaya; ia tidak sanggup mendekati siapa pun lagi. Bisa menempel sebagai lapisan di E-KO-16 atau E-KO-17

- [ ] **E-KO-20** · Saksi yang Bersuara _(Neutral, host Y/C)_
  - Syarat: Koita menyaksikan atau mengetahui Force saat trust_koita sudah rendah (sudah lama curiga atau lepas dari pemain), sehingga ia bisa bertindak alih-alih membeku
  - Isi: dari orang yang sudah tidak percaya menjadi orang yang menjatuhkan pemain; sendiri, tetapi berdiri. Berjalan bersama E-FO-11

- [ ] **E-KO-21** · Dituduh atas Luka yang Menimpanya _(Broken, host C)_
  - Syarat: jalur manipulasi pembalikan Chiasa (06_Chiasa.md §14) bertahan; runtuh_koita ≥ 80
  - Isi: Koita korban yang justru dicap pelaku; tidak dipercaya dan tidak bisa membuktikan sebaliknya; runtuh dalam diam. K-D21 (ada yang tetap percaya) atau C-D14/C-D15 (Chiasa sendiri goyah) bisa membelokkan ini sebelum M35

## Tachibana Miyuki

_27 event utama · 14 event dinamis · 14 ending_

### Event utama

- [ ] **Mi01** · bulan M01b · Bento Hanami
  - Pemicu: Miyuki membawa bento besar.
  - [ ] Pilihan A — puji
  - [ ] Pilihan B — bantu bawa
  - [ ] Pilihan C — abaikan.
  - Efek: A/B membuka akses sisi hangat.

- [ ] **Mi02** · bulan M02 · Kue Percobaan Ketiga
  - Pemicu: dapur ryokan; kue gagal.
  - [ ] Pilihan A — makan semuanya
  - [ ] Pilihan B — jujur
  - [ ] Pilihan C — bantu memperbaiki.
  - Efek: C memicu sisi manja.

- [ ] **Mi03** · bulan M04 · Perpustakaan Medis Malam
  - Pemicu: Miyuki belajar sampai larut.
  - [ ] Pilihan A — bawakan makanan
  - [ ] Pilihan B — paksa pulang
  - [ ] Pilihan C — temani diam.
  - Efek: stage 1 (kelelahan); sena_curiga mulai.

- [ ] **Mi04** · bulan M05a · Tali Obi
  - Pemicu: kesulitan memakai yukata.
  - [ ] Pilihan A — bantu
  - [ ] Pilihan B — panggil Sena
  - [ ] Pilihan C — goda.
  - Efek: intimasi.

- [ ] **Mi05** · bulan M05b · Minuman di Vila
  - Pemicu: Miyuki lebih terbuka.
  - [ ] Pilihan A — dengarkan
  - [ ] Pilihan B — mengantar ke kamar
  - [ ] Pilihan C — memanfaatkan.
  - Efek: hub risiko tinggi ( Force Route tersedia sebagai kejahatan).

- [ ] **Mi06** · bulan M06 · Rencana Masa Depan
  - Pemicu: ia bercerita tentang pediatri.
  - [ ] Pilihan A — dukung
  - [ ] Pilihan B — remehkan
  - [ ] Pilihan C — tanyakan Koita.
  - Efek: Trust.

- [ ] **Mi07** · bulan M07 · Takeru Muncul
  - Pemicu: omiai pertama dari orang tua.
  - [ ] Pilihan A — dukung Takeru
  - [ ] Pilihan B — halangi
  - [ ] Pilihan C — jujur ke Miyuki.
  - Efek: omiai_takeru.

- [ ] **Mi08** · bulan M08 · Sena dan Psikolog
  - Pemicu: Sena memperkenalkan Sato Kyoko.
  - [ ] Pilihan A — dukung konsultasi
  - [ ] Pilihan B — tolak
  - [ ] Pilihan C — abaikan.
  - Efek: membuka jalur pemulihan.

- [ ] **Mi09** · bulan M09 · Natal: Pesta Rumah Sakit
  - Pemicu: acara orang tua.
  - [ ] Pilihan A — menemani
  - [ ] Pilihan B — tampil sebagai pasangan palsu
  - [ ] Pilihan C — tidak datang.
  - Efek: hub besar #3.

- [ ] **Mi10** · bulan M10 · Omikuji Miyuki
  - Pemicu: ramalan "kesendirian".
  - [ ] Pilihan A — hibur
  - [ ] Pilihan B — tertawa
  - [ ] Pilihan C — ambil kesempatan.
  - Efek: kerentanan.

- [ ] **Mi11** · bulan M11 · Kue untuk Semua
  - Pemicu: ia membuat terlalu banyak.
  - [ ] Pilihan A — makan bersama
  - [ ] Pilihan B — bantu bagikan
  - [ ] Pilihan C — minta khusus.
  - Efek: gerbang cinta pemain.

- [ ] **Mi12** · bulan M13 · Tahun Keempat
  - Pemicu: klinik dimulai.
  - [ ] Pilihan A — bantu belajar
  - [ ] Pilihan B — ganggu
  - [ ] Pilihan C — jarak.
  - Efek: stage 2 dimulai.

- [ ] **Mi13** · bulan M14 · Telepon Ibu
  - Pemicu: tekanan dari orang tua.
  - [ ] Pilihan A — dengarkan
  - [ ] Pilihan B — tegur ibunya
  - [ ] Pilihan C — alihkan.
  - Efek: kelelahan.

- [ ] **Mi14** · bulan M15 · Hujan di Bangsal
  - Pemicu: ia dimarahi supervisor.
  - [ ] Pilihan A — hibur
  - [ ] Pilihan B — bela
  - [ ] Pilihan C — kritik Miyuki.
  - Efek: stage 2 (dimarahi = diperhatikan).

- [ ] **Mi15** · bulan M17a · Minta Maaf Berlebihan
  - Pemicu: ia meminta maaf untuk hal sepele.
  - [ ] Pilihan A — tegur halus
  - [ ] Pilihan B — biarkan
  - [ ] Pilihan C — manfaatkan.
  - Efek: stage 3 (normalisasi).

- [ ] **Mi16** · bulan M19 · Kesalahan di Bangsal
  - Pemicu: kesalahan klinis kecil; teguran keras.
  - [ ] Pilihan A — hibur
  - [ ] Pilihan B — tegas
  - [ ] Pilihan C — dingin
  - [ ] Pilihan D — bawa ke Sena/Sato.
  - Efek: gerbang Rute Masokis (stage 4); D membuka jalur pemulihan.

- [ ] **Mi17** · bulan M20 · Pingsan di Pameran
  - Pemicu: kelelahan ekstrem.
  - [ ] Pilihan A — bawa ke UGD
  - [ ] Pilihan B — diam
  - [ ] Pilihan C — manfaatkan.
  - Efek: Sena menegur pemain.

- [ ] **Mi18** · bulan M21 · Natal Kedua: Lamaran Terselubung
  - Pemicu: keluarga Hayase hadir.
  - [ ] Pilihan A — hadir
  - [ ] Pilihan B — halangi
  - [ ] Pilihan C — menawarkan alternatif.
  - Efek: omiai_takeru naik.

- [ ] **Mi19** · bulan M23 · Valentine Dingin
  - Pemicu: ia memberi coklat tanpa senyum.
  - [ ] Pilihan A — terima
  - [ ] Pilihan B — kembalikan
  - [ ] Pilihan C — tanyakan.
  - Efek: pola menguat.

- [ ] **Mi20** · bulan M24 · Audit Pribadi
  - Pemicu: ia mengevaluasi hidupnya.
  - [ ] Pilihan A — dukung
  - [ ] Pilihan B — abaikan
  - [ ] Pilihan C — bawa ke Sato.
  - Efek: titik pemulihan terakhir sebelum Tahun 3.

- [ ] **Mi21** · bulan M25 · Rotasi Klinik
  - Pemicu: cabang spesialis.
  - [ ] Pilihan A — bantu
  - [ ] Pilihan B — ganggu.
  - Efek: karier.

- [ ] **Mi22** · bulan M27 · Pola Menetap
  - Pemicu: stage 5: dinamika dominasi–penyerahan emosional (tersirat).
  - [ ] Pilihan A — lanjutkan
  - [ ] Pilihan B — hentikan
  - [ ] Pilihan C — bawa ke Sena/Sato.
  - Efek: A bisa membuat pola permanen setelah 1 semester; C membuka pemulihan sebagian.

- [ ] **Mi23** · bulan M29a · Yukata Tanpa Senyum
  - Pemicu: ia hadir tanpa ekspresi.
  - [ ] Pilihan A — hibur
  - [ ] Pilihan B — manfaatkan
  - [ ] Pilihan C — tinggalkan.
  - Efek: Sena memutus hubungan jika pemain memanfaatkan.

- [ ] **Mi24** · bulan M30 · Hasil CBT
  - Pemicu: hasil ujian.
  - [ ] Pilihan A — rayakan
  - [ ] Pilihan B — hibur
  - [ ] Pilihan C — abaikan.
  - Efek: karier.

- [ ] **Mi25** · bulan M33 · Natal: Pertunangan?
  - Pemicu: Takeru melamar.
  - [ ] Pilihan A — dukung
  - [ ] Pilihan B — halangi
  - [ ] Pilihan C — ajak kabur.
  - Efek: ending Miyuki.

- [ ] **Mi26** · bulan M34 · Ujian Akhir dan Sena
  - Pemicu: Sena berdiri di sisi pemain atau melawan.
  - [ ] Pilihan A — minta bantuan Sena
  - [ ] Pilihan B — hindari
  - [ ] Pilihan C — konfrontasi.
  - Efek: aliansi.

- [ ] **Mi27** · bulan M35 · Pilihan Miyuki
  - Pemicu: keputusan akhir. *Efek:* ending Miyuki.

### Event dinamis

- [ ] **Mi-D01** · Permintaan Kecil
  - Pemicu: dimanja ≥ 50; Trust Sedang
  - Ringkasan: jam 23:00 Miyuki minta dibelikan puding konbini, "sekali ini saja". Belikan dan temani / belikan lalu pergi / tolak / tertawakan
  - [ ] Opsi 1 — Belikan dan temani
  - [ ] Opsi 2 — belikan lalu pergi
  - [ ] Opsi 3 — tolak
  - [ ] Opsi 4 — tertawakan
  - Efek: dimanja +10 / +5 / −5 / −10; Intim

- [ ] **Mi-D02** · Tertidur di Bahu
  - Pemicu: kelelahan ≥ 60; pemain duduk di dekatnya
  - Ringkasan: ia tertidur di bahu pemain di perpustakaan atau kereta. Biarkan sampai bangun (dua jam lewat) / bangunkan / foto / pindahkan ke ruang jaga
  - [ ] Opsi 1 — Biarkan sampai bangun (dua jam lewat)
  - [ ] Opsi 2 — bangunkan
  - [ ] Opsi 3 — foto
  - [ ] Opsi 4 — pindahkan ke ruang jaga
  - Efek: Intim +, kelelahan −5; foto bisa sampai ke Mei

- [ ] **Mi-D03** · Pastry dengan Nama
  - Pemicu: Aff ≥ 55; pemain pernah memuji pastry-nya
  - Ringkasan: pastry bertuliskan nama pemain. Makan di depan Koita / sembunyikan / bagikan ke semua
  - [ ] Opsi 1 — Makan di depan Koita
  - [ ] Opsi 2 — sembunyikan
  - [ ] Opsi 3 — bagikan ke semua
  - Efek: Koita mencatat; Nagisa cemburu bila melihat

- [ ] **Mi-D04** · Telepon Ibu yang Terdengar
  - Pemicu: pemain bersamanya Sabtu malam; omiai_takeru ≥ 40
  - Ringkasan: Sayuri menelepon soal Hayase. Pura-pura tidak dengar / tanya setelahnya / minta bicara dengan ibunya
  - [ ] Opsi 1 — Pura-pura tidak dengar
  - [ ] Opsi 2 — tanya setelahnya
  - [ ] Opsi 3 — minta bicara dengan ibunya
  - Efek: omiai_takeru ±; Trust; bicara dengan ibunya membuka hubungan pemain dengan keluarga Tachibana

- [ ] **Mi-D05** · Tangga Darurat Jam Tiga
  - Pemicu: Tahun 3; jaga malam; luka[[diri] ≥ 50; pemain di RS saat Dini Hari
  - Ringkasan: ia duduk sendirian di tangga darurat. Duduk di sebelahnya / panggil Sena / pergi diam-diam
  - [ ] Opsi 1 — Duduk di sebelahnya
  - [ ] Opsi 2 — panggil Sena
  - [ ] Opsi 3 — pergi diam-diam
  - Efek: luka[[diri] −15 / Sena menjadi sekutu / tidak ada

- [ ] **Mi-D06** · Teguran yang Ia Minta
  - Pemicu: tahap ≥ 3; luka[[pemain] ≥ 40
  - Ringkasan: "Bilang aku bodoh. Aku pantas." Tolak dengan lembut / turuti / alihkan / bawa ke Sato
  - [ ] Opsi 1 — Aku pantas." Tolak dengan lembut
  - [ ] Opsi 2 — turuti
  - [ ] Opsi 3 — alihkan
  - [ ] Opsi 4 — bawa ke Sato
  - Efek: persimpangan utama; lihat Sistem_Cabang_dan_Poin §5.3

- [ ] **Mi-D07** · Hayase di Kafe
  - Pemicu: omiai_takeru ≥ 40; pemain di Kafe Komorebi hari Sabtu
  - Ringkasan: Takeru mengajak bicara. Hadapi / bersekutu / pancing ia jujur / rekam diam-diam
  - [ ] Opsi 1 — Hadapi
  - [ ] Opsi 2 — bersekutu
  - [ ] Opsi 3 — pancing ia jujur
  - [ ] Opsi 4 — rekam diam-diam
  - Efek: Takeru bisa mengaku ia tidak mencintai Miyuki; rekaman menjadi bukti sekaligus risiko

- [ ] **Mi-D08** · Rahasia di Konbini
  - Pemicu: Koita lelah atau mabuk; koita_sadar ≥ 25
  - Ringkasan: jam 03:00 Koita mengaku pernah menyukai Miyuki di SMA. Simpan / ceritakan ke Miyuki / pakai untuk menekan Koita / dorong Koita mengaku sendiri
  - [ ] Opsi 1 — Simpan
  - [ ] Opsi 2 — ceritakan ke Miyuki
  - [ ] Opsi 3 — pakai untuk menekan Koita
  - [ ] Opsi 4 — dorong Koita mengaku sendiri
  - Efek: bendera rahasia_koita_sma; bila Koita mengaku sendiri, cinta_koita bisa +20 atau Miyuki justru kesal, tergantung tahapnya

- [ ] **Mi-D09** · Pasien Kecil
  - Pemicu: rotasi pediatri Tahun 3; Aff Sedang
  - Ringkasan: pasien anak yang ia sayangi memburuk. Datang ke RS / telepon / tidak bisa datang
  - [ ] Opsi 1 — Datang ke RS
  - [ ] Opsi 2 — telepon
  - [ ] Opsi 3 — tidak bisa datang
  - Efek: didukung: luka[[diri] −, karier +; ia merasa dibutuhkan dengan cara yang sehat

- [ ] **Mi-D10** · Resep yang Salah Tulis
  - Pemicu: kelelahan ≥ 85
  - Ringkasan: hampir salah menulis resep; Sena menangkapnya. Paksa ia cuti / bantu menyembunyikan / laporkan ke pembimbing
  - [ ] Opsi 1 — Paksa ia cuti
  - [ ] Opsi 2 — bantu menyembunyikan
  - [ ] Opsi 3 — laporkan ke pembimbing
  - Efek: menyembunyikan lalu ketahuan: E-MI-06 menguat; cuti: E-MI-10 menguat

- [ ] **Mi-D11** · Malam Sebelum CBT
  - Pemicu: minggu M30
  - Ringkasan: temani belajar semalaman (tubuh pemain) / bawakan makanan lalu pulang / tidak datang
  - [ ] Opsi 1 — temani belajar semalaman (tubuh pemain)
  - [ ] Opsi 2 — bawakan makanan lalu pulang
  - [ ] Opsi 3 — tidak datang
  - Efek: hasil Mi24 bergeser

- [ ] **Mi-D12** · Ia Memilih Dirinya
  - Pemicu: dimanja ≥ 70; semua luka < 30; Trust ≥ 70
  - Ringkasan: untuk pertama kali ia berkata "tidak" pada ibunya. Dukung / goda / bilang itu berkat pemain
  - [ ] Opsi 1 — Dukung
  - [ ] Opsi 2 — goda
  - [ ] Opsi 3 — bilang itu berkat pemain
  - Efek: omiai_takeru −30; E-MI-01 dan E-MI-02 menguat

- [ ] **Mi-D13** · Pertanyaan yang Belum Pernah Ia Tanyakan
  - Pemicu: Chiasa host; Intim ≥ 55
  - Ringkasan: Miyuki bertanya pada dirinya sendiri apakah ia tertarik pada perempuan. Beri waktu / desak / bercanda
  - [ ] Opsi 1 — Beri waktu
  - [ ] Opsi 2 — desak
  - [ ] Opsi 3 — bercanda
  - Efek: Aff, Intim; desakan menurunkan Trust

- [ ] **Mi-D14** · Jaga untuk Pemain
  - Pemicu: pemain Ambruk atau sakit; tahap ≤ 3
  - Ringkasan: Miyuki merawat pemain semalaman. Terima / tolak / minta ia pulang tidur
  - [ ] Opsi 1 — Terima
  - [ ] Opsi 2 — tolak
  - [ ] Opsi 3 — minta ia pulang tidur
  - Efek: tahap ≤ 3: ia merasa dibutuhkan dengan sehat; tahap 4+: kelelahan naik

### Ending

- [ ] **E-MI-01** · Jas Putih yang Ringan _(Romantis, host Y/C)_
  - Syarat: tahap ≤ 3 atau pulih; Affection dan Trust tinggi ke pemain; tanpa Force; Sena tidak memusuhi
  - Isi: hubungan setara; ia belajar meminta tolong dan tetap menuju pediatri

- [ ] **E-MI-02** · Dokter Anak _(Neutral, host Y/C)_
  - Syarat: tahap ≤ 2; karier lancar; hati tidak ke siapa pun
  - Isi: lulus, fokus pediatri, hangat pada semua tetapi sendiri

- [ ] **E-MI-03** · Kembali ke Koita _(Koita, host Y/C)_
  - Syarat: Koita memilih Miyuki di K26; tahap ≤ 3
  - Isi: jalur manga; deviasi rendah untuk Miyuki

- [ ] **E-MI-04** · Cincin Keluarga Hayase _(Neutral, host Y/C)_
  - Syarat: Mi25-A atau pemain absen; omiai ditekan
  - Isi: bertunangan demi keluarga; senyum yang rapi; ikatan sosial, bukan pasangan romantis baru

- [ ] **E-MI-05** · Kereta Pagi Tanpa Tujuan _(Romantis, host Y/C)_
  - Syarat: Mi25-C kabur bersama pemain
  - Isi: orang tua memutus hubungan; karier tertunda; cinta yang mahal

- [ ] **E-MI-06** · Lampu Bangsal Padam _(Bad, host Y/C)_
  - Syarat: kelelahan ekstrem; tanpa bantuan; CBT gagal
  - Isi: burnout; berhenti dari kedokteran

- [ ] **E-MI-07** · Kenyamanan yang Salah _(Distorted, host Y/C)_
  - Syarat: tahap 5 permanen; arah_luka pemain
  - Isi: hubungan "nyaman" yang tidak sehat; ia hanya merasa dicintai saat diperlakukan keras

- [ ] **E-MI-08** · Penebusan Tanpa Akhir _(Distorted, host Y/C)_
  - Syarat: tahap 5; arah_luka diri
  - Isi: lulus dan bekerja, tetapi menghukum diri lewat jam kerja tanpa batas

- [ ] **E-MI-09** · Menunggu yang Menyakitkan _(Distorted, host Y/C)_
  - Syarat: tahap 5; arah_luka Koita; Koita tetap menggantung
  - Isi: ia bertahan di sisi Koita justru karena sakitnya

- [ ] **E-MI-10** · Cuti Satu Tahun _(Neutral, host Y/C)_
  - Syarat: pulih sebagian lewat Sato; CBT tertunda
  - Isi: cuti kuliah; masa depan terbuka; pesan pendek untuk pemain di musim semi

- [ ] **E-MI-11** · Pintu yang Ditutup Sena _(Bad, host Y/C)_
  - Syarat: pemain memanfaatkan di depan umum; Sena memutus
  - Isi: Miyuki terisolasi; Sena menjadi penghalang pemain di semua lingkungan medis

- [ ] **E-MI-12** · Napas yang Tertahan _(Broken, host Y/C)_
  - Syarat: pemain pelaku Force terhadapnya
  - Isi: trauma terpisah dari Rute Masokis; jalur Sena, Sato, dan hukum; tanpa romansa dengan pelaku

- [ ] **E-MI-13** · Sandiwara yang Jadi Nyata _(Romantis, host Y/C)_
  - Syarat: pasangan palsu dipertahankan sampai Mi18, lalu diakui jujur
  - Isi: dua keluarga marah lalu menerima; awal yang bohong menjadi hubungan yang jujur

- [ ] **E-MI-14** · Sandiwara Terbongkar _(Bad, host Y/C)_
  - Syarat: pasangan palsu terbongkar oleh Takeru atau orang tua
  - Isi: malu di depan keluarga; Miyuki menjauh dari pemain dan menerima omiai

## Sakurajima Nagisa

_24 event utama · 13 event dinamis · 14 ending_

### Event utama

- [ ] **N01** · bulan M01a · Tabrakan di Koridor
  - Pemicu: tumbukan di fakultas arsitektur; ia menantang main game.
  - [ ] Pilihan A — terima
  - [ ] Pilihan B — tolak
  - [ ] Pilihan C — goda.
  - Efek: A membuka rivalitas ringan. (Female: risiko "Nacchan-oneechan".)

- [ ] **N02** · bulan M02 · Rematch Malam Onsen
  - Pemicu: ia selalu meminta rematch.
  - [ ] Pilihan A — terus menang
  - [ ] Pilihan B — mengalah
  - [ ] Pilihan C — ajak tim.
  - Efek: Trust.

- [ ] **N03** · bulan M03 · Maket Hujan
  - Pemicu: maket rusak karena hujan.
  - [ ] Pilihan A — bantu semalaman
  - [ ] Pilihan B — belikan baru
  - [ ] Pilihan C — tertawakan.
  - Efek: stage 1 (rasa terima kasih) pada A.

- [ ] **N04** · bulan M05a · Gagal Mengaku Lagi
  - Pemicu: kembang api; ia mau mengaku pada Koita dan gagal.
  - [ ] Pilihan A — hibur
  - [ ] Pilihan B — dorong mengaku
  - [ ] Pilihan C — menyela.
  - Efek: C membuat Nagisa marah tapi juga lega.

- [ ] **N05** · bulan M06 · Foto Berempat
  - Pemicu: ia menatap foto lama.
  - [ ] Pilihan A — bercerita tentang Koko
  - [ ] Pilihan B — mengganggu
  - [ ] Pilihan C — diam.
  - Efek: Intimasi.

- [ ] **N06** · bulan M07 · Yuuto Menawarkan Bantuan
  - Pemicu: Mochizuki membantu maket.
  - [ ] Pilihan A — dukung
  - [ ] Pilihan B — halangi
  - [ ] Pilihan C — cemburu.
  - Efek: stage 2 (kelekatan) bila B/C.

- [ ] **N07** · bulan M09 · Natal: Koko
  - Pemicu: ia memeluk Koko.
  - [ ] Pilihan A — ada di sana
  - [ ] Pilihan B — pergi
  - [ ] Pilihan C — bawa Koita.
  - Efek: hub besar #3.

- [ ] **N08** · bulan M11 · Coklat Gosong
  - Pemicu: Valentine; coklat untuk Koita gosong.
  - [ ] Pilihan A — makan
  - [ ] Pilihan B — bantu buat ulang
  - [ ] Pilihan C — ambil alih.
  - Efek: C mengalihkan coklat ke pemain.

- [ ] **N09** · bulan M12 · Hadiah Kecil
  - Pemicu: White Day; ia menerima hadiah.
  - [ ] Pilihan A — kecil
  - [ ] Pilihan B — mahal
  - [ ] Pilihan C — tidak ada.
  - Efek: gengsi.

- [ ] **N10** · bulan M13 · Haruto Menelepon
  - Pemicu: kakak menggodanya.
  - [ ] Pilihan A — dukung
  - [ ] Pilihan B — menghindar.
  - Efek: haruto_curiga awal.

- [ ] **N11** · bulan M14 · Ditinggal di Rumah
  - Pemicu: ia tidak ikut Kansai.
  - [ ] Pilihan A — kirim kabar
  - [ ] Pilihan B — abaikan
  - [ ] Pilihan C — cerita bohong.
  - Efek: jeal naik.

- [ ] **N12** · bulan M15 · Hujan Deras: Nagisa Menyelamatkan
  - Pemicu: ia menolong Chiasa/pemain lalu mengomel.
  - [ ] Pilihan A — berterima kasih
  - [ ] Pilihan B — menjauh
  - [ ] Pilihan C — peluk.
  - Efek: hubungan dengan Chiasa.

- [ ] **N13** · bulan M17a · Konfrontasi Yukata
  - Pemicu: ia menghadapi rival.
  - [ ] Pilihan A — mendukung
  - [ ] Pilihan B — melerai
  - [ ] Pilihan C — memihak Chiasa.
  - Efek: konflik terbuka.

- [ ] **N14** · bulan M18 · Cek Pesan
  - Pemicu: ia meminta melihat ponsel pemain.
  - [ ] Pilihan A — tunjukkan
  - [ ] Pilihan B — tolak
  - [ ] Pilihan C — tipu.
  - Efek: gerbang Rute Yandere (stage 3, posesif).

- [ ] **N15** · bulan M21 · Natal Kedua: Ultimatum
  - Pemicu: "pilih aku atau mereka."
  - [ ] Pilihan A — pilih
  - [ ] Pilihan B — tolak
  - [ ] Pilihan C — manipulasi.
  - Efek: stage 4 (titik balik).

- [ ] **N16** · bulan M23 · Hari Bentrok
  - Pemicu: ia menyatakan perasaan pada pemain atau Koita.
  - [ ] Pilihan A — terima
  - [ ] Pilihan B — tolak
  - [ ] Pilihan C — alihkan.
  - Efek: hub besar #8.

- [ ] **N17** · bulan M24 · Gantungan Kunci yang Hilang
  - Pemicu: ia menuduh orang lain.
  - [ ] Pilihan A — selidiki
  - [ ] Pilihan B — pasang jebakan
  - [ ] Pilihan C — tuduh balik.
  - Efek: titik pemulihan terakhir; setelah ini hanya Distorted Ending.

- [ ] **N18** · bulan M26 · Yuuto dan Sabotase
  - Pemicu: Nagisa mengganggu pesaing.
  - [ ] Pilihan A — hentikan
  - [ ] Pilihan B — biarkan
  - [ ] Pilihan C — menjadi korban.
  - Efek: stage 5.

- [ ] **N19** · bulan M28 · Tanzaku Palsu
  - Pemicu: ia menulis tanzaku atas nama pemain.
  - [ ] Pilihan A — kecam
  - [ ] Pilihan B — biarkan.
  - Efek: pengawasan.

- [ ] **N20** · bulan M29a · Kembang Api Terakhir
  - Pemicu: ia menarik pemain pergi.
  - [ ] Pilihan A — ikut
  - [ ] Pilihan B — tolak
  - [ ] Pilihan C — ajak bicara.
  - Efek: hub #10.

- [ ] **N21** · bulan M31 · Haruto Datang
  - Pemicu: kakak menyadari.
  - [ ] Pilihan A — jujur
  - [ ] Pilihan B — bohong
  - [ ] Pilihan C — konfrontasi.
  - Efek: Haruto menjadi sekutu atau lawan.

- [ ] **N22** · bulan M33 · Natal: Rumah Sakurajima
  - Pemicu: orang tua Nagisa bertemu pemain.
  - [ ] Pilihan A — hadir
  - [ ] Pilihan B — menolak.
  - Efek: jalur pemulihan melalui keluarga.

- [ ] **N23** · bulan M34 · Koko di Meja Pemain
  - Pemicu: Koko muncul di kamar pemain.
  - [ ] Pilihan A — kembalikan
  - [ ] Pilihan B — simpan
  - [ ] Pilihan C — bawa ke Haruto.
  - Efek: isyarat ekstrem.

- [ ] **N24** · bulan M35 · Pilihan Nagisa
  - Pemicu: keputusan akhir. *Efek:* ending Nagisa.

### Event dinamis

- [ ] **N-D01** · Rematch Jam Dua
  - Pemicu: Larut atau Dini Hari; Aff Sedang
  - Ringkasan: ajakan main online. Main sampai pagi / tidur / biarkan ia menang
  - [ ] Opsi 1 — Main sampai pagi
  - [ ] Opsi 2 — tidur
  - [ ] Opsi 3 — biarkan ia menang
  - Efek: Intim + dan utang tidur; menang tipis yang jujur menaikkan gengsi; ketahuan mengalah menurunkannya

- [ ] **N-D02** · Bekal yang Tidak Diakui
  - Pemicu: Aff ≥ 55; gengsi ≥ 50
  - Ringkasan: bekal yang "kebetulan kelebihan". Puji di depan orang / puji diam-diam / kembalikan
  - [ ] Opsi 1 — Puji di depan orang
  - [ ] Opsi 2 — puji diam-diam
  - [ ] Opsi 3 — kembalikan
  - Efek: di depan orang: gengsi −, Aff +; diam-diam: Aff ++

- [ ] **N-D03** · Ayunan Malam
  - Pemicu: hari itu harapan_koita turun
  - Ringkasan: ia duduk di ayunan taman masa kecil. Duduk di ayunan sebelah / panggil Koita / beri ruang
  - [ ] Opsi 1 — Duduk di ayunan sebelah
  - [ ] Opsi 2 — panggil Koita
  - [ ] Opsi 3 — beri ruang
  - Efek: kelekatan +; bila Koita yang datang, hasilnya tergantung Koita

- [ ] **N-D04** · Tawaran Kedua Yuuto
  - Pemicu: tenggat studio; pemain absen
  - Ringkasan: Yuuto membantu maket. Datang membantu / biarkan / alihkan Yuuto
  - [ ] Opsi 1 — Datang membantu
  - [ ] Opsi 2 — biarkan
  - [ ] Opsi 3 — alihkan Yuuto
  - Efek: studio +; kelekatan ke pemain turun bila pemain absen

- [ ] **N-D05** · Tangkapan Layar
  - Pemicu: jeal[[x] ≥ 60; pemain mengunggah foto bersama x
  - Ringkasan: Nagisa mengirim tangkapan layar dengan satu tanda tanya. Jelaskan jujur / bohong / abaikan / blokir
  - [ ] Opsi 1 — Jelaskan jujur
  - [ ] Opsi 2 — bohong
  - [ ] Opsi 3 — abaikan
  - [ ] Opsi 4 — blokir
  - Efek: jujur: Trust +; bohong: luka_bohong bila ketahuan; blokir: eskalasi

- [ ] **N-D06** · Kunci Cadangan
  - Pemicu: tahap ≥ 3; kelekatan ≥ 75
  - Ringkasan: ia meminta kunci cadangan "untuk jaga-jaga". Beri / tolak / beri kunci palsu
  - [ ] Opsi 1 — Beri
  - [ ] Opsi 2 — tolak
  - [ ] Opsi 3 — beri kunci palsu
  - Efek: memberi: N23 dan kunjungan malam datang lebih awal; kunci palsu ketahuan: luka_bohong +30

- [ ] **N-D07** · Haruto di Depan Rumah
  - Pemicu: haruto_curiga ≥ 50; pemain di D2 malam hari
  - Ringkasan: Haruto pulang lembur. Jujur / bohong / ajak minum
  - [ ] Opsi 1 — Jujur
  - [ ] Opsi 2 — bohong
  - [ ] Opsi 3 — ajak minum
  - Efek: Haruto bercerita masa kecil Nagisa; ia menjadi sekutu atau lawan

- [ ] **N-D08** · Rekaman Pertandingan
  - Pemicu: N02-B pernah terjadi; gengsi ≥ 60
  - Ringkasan: Nagisa menonton ulang dan sadar pemain mengalah. Akui / sangkal / tantang ulang dengan serius
  - [ ] Opsi 1 — Akui
  - [ ] Opsi 2 — sangkal
  - [ ] Opsi 3 — tantang ulang dengan serius
  - Efek: Trust dan gengsi bergeser

- [ ] **N-D09** · Koko Robek
  - Pemicu: Koko di tempat pemain, atau tahap ≥ 4
  - Ringkasan: boneka Koko robek. Jahit sendiri / minta Moeka menjahit / beli yang baru
  - [ ] Opsi 1 — Jahit sendiri
  - [ ] Opsi 2 — minta Moeka menjahit
  - [ ] Opsi 3 — beli yang baru
  - Efek: kelekatan bergeser besar; Moeka yang menjahit bisa meredakan cemburu Nagisa padanya

- [ ] **N-D10** · Pesan Ketiga Puluh Tujuh
  - Pemicu: tahap ≥ 3; pemain tidur dengan mode Senyap
  - Ringkasan: pagi hari ada 37 pesan. Telepon langsung / balas singkat / jelaskan mode senyap / marah
  - [ ] Opsi 1 — Telepon langsung
  - [ ] Opsi 2 — balas singkat
  - [ ] Opsi 3 — jelaskan mode senyap
  - [ ] Opsi 4 — marah
  - Efek: tahap naik atau turun; contoh tubuh dan ponsel yang menjadi cabang

- [ ] **N-D11** · Ruang di Gambar Kerja
  - Pemicu: studio ≥ 70; Aff ≥ 55; tahap ≤ 2
  - Ringkasan: ia merancang rumah dengan satu ruangan untuk pemain. Tanya maksudnya / pura-pura tidak paham / tambahkan sesuatu ke gambarnya
  - [ ] Opsi 1 — Tanya maksudnya
  - [ ] Opsi 2 — pura-pura tidak paham
  - [ ] Opsi 3 — tambahkan sesuatu ke gambarnya
  - Efek: pengakuan lewat arsitektur; E-NA-01 menguat

- [ ] **N-D12** · Nacchan-oneechan
  - Pemicu: Chiasa host; momen emosional
  - Ringkasan: Chiasa memakai panggilan masa kecil. Pakai dengan sungguh-sungguh / bercanda / tidak
  - [ ] Opsi 1 — Pakai dengan sungguh-sungguh
  - [ ] Opsi 2 — bercanda
  - [ ] Opsi 3 — tidak
  - Efek: E-NA-10 menguat, atau gengsi tersinggung

- [ ] **N-D13** · Jendela Seberang
  - Pemicu: Chiasa host; tahap ≥ 3
  - Ringkasan: Nagisa memandangi jendela kamar Chiasa dari rumahnya. Lambaikan tangan / tutup tirai / keluar menemuinya
  - [ ] Opsi 1 — Lambaikan tangan
  - [ ] Opsi 2 — tutup tirai
  - [ ] Opsi 3 — keluar menemuinya
  - Efek: kelekatan bergeser; pengawasan menjadi terbuka

### Ending

- [ ] **E-NA-01** · Maket untuk Dua Orang _(Romantis, host Y/C)_
  - Syarat: pulih di N17 atau tidak pernah melewati tahap 3; tanpa kebohongan terbongkar; tanpa Force
  - Isi: hubungan jujur; ia belajar meminta maaf; arsitektur tetap jalan

- [ ] **E-NA-02** · Garis yang Ia Gambar Sendiri _(Neutral, host Y/C)_
  - Syarat: pulih; hati tidak ke siapa pun
  - Isi: fokus arsitektur; gengsinya kembali sehat

- [ ] **E-NA-03** · Pengakuan yang Akhirnya Sampai _(Koita, host Y/C)_
  - Syarat: harapan_koita tegak; Koita memilih Nagisa di K26
  - Isi: jalur manga; deviasi rendah untuk Nagisa

- [ ] **E-NA-04** · Rumah yang Dibangun di Sekitarmu _(Distorted, host Y/C)_
  - Syarat: tahap 5; pemain menerimanya
  - Isi: hidup berputar pada pemain; impian arsitektur dilepas

- [ ] **E-NA-05** · Kamar yang Dikunci _(Bad, host Y/C)_
  - Syarat: tahap 4–5; ditinggal; tanpa keluarga
  - Isi: mengasingkan diri; tugas akhir terbengkalai

- [ ] **E-NA-06** · Garis Merah _(Bad, host Y/C)_
  - Syarat: tahap 5; N18-B dibiarkan; sasaran_cemburu terus didekati pemain
  - Isi: ia melukai saingan secara fisik; ditangkap; Haruto hancur. Tanpa detail kekerasan

- [ ] **E-NA-07** · Pulang ke Rumah Sakurajima _(Neutral, host Y/C)_
  - Syarat: Haruto sekutu (N21-A) atau N22 dihadiri
  - Isi: keluarga menariknya pulang; terapi; cuti atau pindah kampus

- [ ] **E-NA-08** · Koko di Tempat Sampah _(Neutral, host Y/C)_
  - Syarat: pulih, tetapi kecewa pada Koita dan pemain
  - Isi: melepas masa kecil; memutus keduanya; studi arsitektur di luar negeri

- [ ] **E-NA-09** · Empat Orang di Foto Lama _(Neutral, host Y/C)_
  - Syarat: tahap ≤ 2; tidak ada pengkhianatan besar di geng masa kecil
  - Isi: Koita, Yutaka, Nagisa, Chiasa kembali berfoto berempat

- [ ] **E-NA-10** · Rival Jadi Kekasih _(Romantis, host C)_
  - Syarat: Chiasa host; pulih; gengsi kedua pihak runtuh
  - Isi: dari saingan sejak kecil menjadi pasangan

- [ ] **E-NA-11** · Bayangan di Bawah Jendela _(Distorted, host Y/C)_
  - Syarat: pemain menolak; Nagisa terus menguntit; pemain melapor ke Hanabusa
  - Isi: perintah menjauh; kuliah dan nama baiknya hancur

- [ ] **E-NA-12** · Gengsi yang Retak _(Broken, host Y/C)_
  - Syarat: pemain pelaku Force terhadapnya
  - Isi: trauma; Haruto menjadi lawan serius pelaku; tanpa romansa dengan pelaku

- [ ] **E-NA-13** · Ambulans di Malam Valentine _(Bad, host Y/C)_
  - Syarat: N15-B ditolak; tanpa Haruto, keluarga, atau pemain di sisinya
  - Isi: ia melukai diri dan dirawat (tanpa metode); pemulihan panjang; epilog berbeda bila pemain menjenguk

- [ ] **E-NA-14** · Senjata yang Kau Arahkan _(Distorted, host Y/C)_
  - Syarat: senjata aktif sampai M35
  - Isi: ia melakukan hal kejam demi pemain; saat sadar dimanfaatkan, ia runtuh atau berbalik pada pemain (risiko E-SI-16)

## Kujo Harumi

_24 event utama · 12 event dinamis · 14 ending_

### Event utama

- [ ] **H01** · bulan M01b · Perpustakaan Sains
  - Pemicu: ia menyendiri membaca.
  - [ ] Pilihan A — duduk bersebelahan
  - [ ] Pilihan B — tanya soal
  - [ ] Pilihan C — abaikan.
  - Efek: A membuka percakapan akademik.

- [ ] **H02** · bulan M03 · Teh di Bawah Atap
  - Pemicu: hujan; ia menyeduh teh untuk pemain.
  - [ ] Pilihan A — puji
  - [ ] Pilihan B — minta tambah
  - [ ] Pilihan C — kritik.
  - Efek: Trust.

- [ ] **H03** · bulan M04 · Masakan Eksperimental
  - Pemicu: masakannya buruk.
  - [ ] Pilihan A — makan semuanya
  - [ ] Pilihan B — jujur
  - [ ] Pilihan C — bantu memasak.
  - Efek: C membuka komedi hangat.

- [ ] **H04** · bulan M05b · Teh Malam di Vila
  - Pemicu: ia menyendiri.
  - [ ] Pilihan A — temani
  - [ ] Pilihan B — ajak bicara
  - [ ] Pilihan C — tinggalkan.
  - Efek: Intimasi.

- [ ] **H05** · bulan M06 · Reuni di Rumah Teh
  - Pemicu: kelompok belajar.
  - [ ] Pilihan A — bantu penyajian
  - [ ] Pilihan B — pembicaraan masa depan
  - [ ] Pilihan C — membuka rahasia.
  - Efek: gerbang pengecekan.

- [ ] **H06** · bulan M07 · Ogawa Masato Muncul
  - Pemicu: senior lab menawarkan "bimbingan".
  - [ ] Pilihan A — dukung
  - [ ] Pilihan B — curiga
  - [ ] Pilihan C — peringatkan.
  - Efek: ogawa_aktif.

- [ ] **H07** · bulan M09 · Natal di Laboratorium
  - Pemicu: ia menghabiskan Natal di lab.
  - [ ] Pilihan A — datang
  - [ ] Pilihan B — kirim makanan
  - [ ] Pilihan C — abaikan.
  - Efek: hub besar #3.

- [ ] **H08** · bulan M10 · Omikuji Harumi
  - Pemicu: ramalan "perhatikan hatimu".
  - [ ] Pilihan A — bantu menafsirkan
  - [ ] Pilihan B — tertawakan.
  - Efek: kejelasan emosi.

- [ ] **H09** · bulan M13 · Hipotesis Cinta
  - Pemicu: ia mencatat perasaannya sebagai data.
  - [ ] Pilihan A — bantu mengidentifikasi
  - [ ] Pilihan B — menertawakan
  - [ ] Pilihan C — menjauh.
  - Efek: stage 1 (kekosongan emosi).

- [ ] **H10** · bulan M14 · Pulang ke Kansai
  - Pemicu: orang tua Kujo dan Mizuhara.
  - [ ] Pilihan A — ikut
  - [ ] Pilihan B — tidak
  - [ ] Pilihan C — bercerita tentang Harumi.
  - Efek: konteks keluarga.

- [ ] **H11** · bulan M16 · Beasiswa Luar Negeri Dibuka
  - Pemicu: peluang sekaligus tekanan.
  - [ ] Pilihan A — dukung
  - [ ] Pilihan B — minta tetap
  - [ ] Pilihan C — manfaatkan.
  - Efek: stage 2 (salah baca validasi).

- [ ] **H12** · bulan M19 · Variabel Sosial
  - Pemicu: ia mencoba "eksperimen" interaksi.
  - [ ] Pilihan A — hentikan
  - [ ] Pilihan B — ikut
  - [ ] Pilihan C — manfaatkan.
  - Efek: stage 3–4 (eksperimen, transaksional awal).

- [ ] **H13** · bulan M20 · Dana Lab Dibekukan
  - Pemicu: Ogawa menawarkan solusi.
  - [ ] Pilihan A — bantu mencari dana
  - [ ] Pilihan B — laporkan Ogawa
  - [ ] Pilihan C — diam
  - [ ] Pilihan D — manfaatkan.
  - Efek: gerbang rute (stage 5).

- [ ] **H14** · bulan M21 · Natal: Undangan Diskusi
  - Pemicu: Ogawa mengundang.
  - [ ] Pilihan A — larang
  - [ ] Pilihan B — temani
  - [ ] Pilihan C — biarkan.
  - Efek: stage 6.

- [ ] **H15** · bulan M22 · Uang yang Tidak Jelas
  - Pemicu: saldo bertambah.
  - [ ] Pilihan A — tanya langsung
  - [ ] Pilihan B — selidiki
  - [ ] Pilihan C — abaikan.
  - Efek: Ogiwara curiga.

- [ ] **H16** · bulan M23 · Valentine: Data Lain
  - Pemicu: ia membawa hadiah dari orang lain.
  - [ ] Pilihan A — terima
  - [ ] Pilihan B — tegur
  - [ ] Pilihan C — manfaatkan.
  - Efek: Hub #8.

- [ ] **H17** · bulan M25 · Ogiwara Menegur
  - Pemicu: pengelola asrama memanggil.
  - [ ] Pilihan A — dukung teguran
  - [ ] Pilihan B — bela Harumi
  - [ ] Pilihan C — tutupi.
  - Efek: titik tanpa balik tanpa Mizuhara/Ogiwara.

- [ ] **H18** · bulan M27 · Mizuhara Memanggil
  - Pemicu: rapat tertutup.
  - [ ] Pilihan A — bersaksi
  - [ ] Pilihan B — menutup
  - [ ] Pilihan C — menantang.
  - Efek: jalur hukum akademik.

- [ ] **H19** · bulan M28 · Tanzaku Kosong
  - Pemicu: ia tidak menulis harapan.
  - [ ] Pilihan A — tanyakan
  - [ ] Pilihan B — menulis untuknya.
  - Efek: tanda bahaya.

- [ ] **H20** · bulan M29b · Teh Terakhir
  - Pemicu: ia menyeduh teh lagi.
  - [ ] Pilihan A — minum
  - [ ] Pilihan B — menolak
  - [ ] Pilihan C — menahan pergi.
  - Efek: simbol kembali.

- [ ] **H21** · bulan M30 · Pengumuman Studi
  - Pemicu: beasiswa luar negeri.
  - [ ] Pilihan A — dukung pergi
  - [ ] Pilihan B — minta tinggal
  - [ ] Pilihan C — ikut.
  - Efek: ending Harumi.

- [ ] **H22** · bulan M33 · Natal Pulang
  - Pemicu: ia pulang ke Kansai.
  - [ ] Pilihan A — mengantar
  - [ ] Pilihan B — menelepon orang tua
  - [ ] Pilihan C — biarkan.
  - Efek: keluarga.

- [ ] **H23** · bulan M34 · Ujian Akhir
  - Pemicu: ujian skripsi.
  - [ ] Pilihan A — bantu
  - [ ] Pilihan B — ganggu
  - [ ] Pilihan C — hadir.
  - Efek: hasil akademik.

- [ ] **H24** · bulan M35 · Pilihan Harumi
  - Pemicu: keputusan akhir. *Efek:* ending Harumi.

### Event dinamis

- [ ] **H-D01** · Teh Jam Satu
  - Pemicu: Larut; dapur asrama (Chiasa bisa masuk, Yutaka hanya di luar jendela); kejelasan ≥ 30
  - Ringkasan: minum dan diam / tanya perasaannya / bercerita tentang dirimu
  - [ ] Opsi 1 — minum dan diam
  - [ ] Opsi 2 — tanya perasaannya
  - [ ] Opsi 3 — bercerita tentang dirimu
  - Efek: kejelasan +

- [ ] **H-D02** · Lembar Pengamatan
  - Pemicu: jalur H12
  - Ringkasan: ia menunjukkan tabel pengamatan reaksi pemain. Koreksi datanya dengan jujur / tertawa / pakai datanya
  - [ ] Opsi 1 — Koreksi datanya dengan jujur
  - [ ] Opsi 2 — tertawa
  - [ ] Opsi 3 — pakai datanya
  - Efek: kejelasan ±; validasi[[pemain]

- [ ] **H-D03** · Pintu Lab Jam Sebelas
  - Pemicu: cengkeraman_ogawa ≥ 40; pemain lewat lab saat Larut
  - Ringkasan: ada suara dari dalam. Ketuk / catat jam keluar / pergi / panggil satpam
  - [ ] Opsi 1 — Ketuk
  - [ ] Opsi 2 — catat jam keluar
  - [ ] Opsi 3 — pergi
  - [ ] Opsi 4 — panggil satpam
  - Efek: bukti +; risiko konfrontasi

- [ ] **H-D04** · Tawaran Ogawa
  - Pemicu: Ogawa mengenal pemain
  - Ringkasan: Ogawa mengajak pemain "bekerja sama". Tolak / pura-pura menerima / laporkan
  - [ ] Opsi 1 — Tolak
  - [ ] Opsi 2 — pura-pura menerima
  - [ ] Opsi 3 — laporkan
  - Efek: pura-pura menerima membuka jalur penyusup (E-NPC-26 atau E-NPC-27)

- [ ] **H-D05** · Masakan Kedua
  - Pemicu: H03-C pernah terjadi
  - Ringkasan: masakannya membaik. Puji dengan spesifik / jujur / ajak memasak lagi
  - [ ] Opsi 1 — Puji dengan spesifik
  - [ ] Opsi 2 — jujur
  - [ ] Opsi 3 — ajak memasak lagi
  - Efek: ia menghubungkan "senang" dengan "memasak bersama"; kejelasan +

- [ ] **H-D06** · Taksi Jam Lima
  - Pemicu: tahap ≥ 4; pemain begadang di dekat asrama
  - Ringkasan: ia turun dari taksi. Sapa / ikuti / pura-pura tidak lihat / foto
  - [ ] Opsi 1 — Sapa
  - [ ] Opsi 2 — ikuti
  - [ ] Opsi 3 — pura-pura tidak lihat
  - [ ] Opsi 4 — foto
  - Efek: bukti, atau bahan pemerasan; Trust

- [ ] **H-D07** · Surat dari Kansai
  - Pemicu: setelah H10-A
  - Ringkasan: ibunya menulis dengan bahasa data. Bantu Harumi membalas / bacakan / abaikan
  - [ ] Opsi 1 — Bantu Harumi membalas
  - [ ] Opsi 2 — bacakan
  - [ ] Opsi 3 — abaikan
  - Efek: orang_tua_kujo +

- [ ] **H-D08** · Hipotesis Ditolak
  - Pemicu: kejelasan ≥ 60; validasi[[ogawa] ≥ 40
  - Ringkasan: ia menyimpulkan Ogawa tidak peduli padanya. Dukung keputusannya / ragukan / ajak ke Mizuhara
  - [ ] Opsi 1 — Dukung keputusannya
  - [ ] Opsi 2 — ragukan
  - [ ] Opsi 3 — ajak ke Mizuhara
  - Efek: cengkeraman_ogawa −30; belok besar

- [ ] **H-D09** · Celah di Jadwal
  - Pemicu: ia menghilang dua malam seminggu
  - Ringkasan: tanya / ikuti / tanya Ogiwara
  - [ ] Opsi 1 — tanya
  - [ ] Opsi 2 — ikuti
  - [ ] Opsi 3 — tanya Ogiwara
  - Efek: H15 terbuka lebih awal

- [ ] **H-D10** · Permintaan Komentar
  - Pemicu: rumor tentang Harumi; Mei menghubungi pemain
  - Ringkasan: bantah / diam / beri informasi
  - [ ] Opsi 1 — bantah
  - [ ] Opsi 2 — diam
  - [ ] Opsi 3 — beri informasi
  - Efek: reputasi Harumi; Mei mendapat bahan

- [ ] **H-D11** · Pelajaran yang Ia Minta
  - Pemicu: kejelasan ≥ 50; Intim ≥ 50
  - Ringkasan: ia meminta pemain mengajarinya apa itu cinta (teks tersirat, berpusat pada persetujuan). Jelaskan dengan kata / ajak kencan biasa / manfaatkan permintaan itu / tolak dengan lembut
  - [ ] Opsi 1 — Jelaskan dengan kata
  - [ ] Opsi 2 — ajak kencan biasa
  - [ ] Opsi 3 — manfaatkan permintaan itu
  - [ ] Opsi 4 — tolak dengan lembut
  - Efek: memanfaatkan: validasi[[pemain] naik ke arah Distorted; kencan biasa: E-HA-01 menguat

- [ ] **H-D12** · Poster Riset
  - Pemicu: Chiasa host; kolaborasi berjalan
  - Ringkasan: Chiasa mengilustrasikan poster riset Harumi. Tampilkan nama berdua / anonim / batal
  - [ ] Opsi 1 — Tampilkan nama berdua
  - [ ] Opsi 2 — anonim
  - [ ] Opsi 3 — batal
  - Efek: E-HA-13 menguat

### Ending

- [ ] **E-HA-01** · Hipotesis yang Terbukti _(Romantis, host Y/C)_
  - Syarat: kejelasan_emosi tinggi; pemain pelindung; tanpa Force
  - Isi: belajar mengenali emosi bersama; teh pagi untuk dua orang

- [ ] **E-HA-02** · Laboratorium di Seberang Laut _(Neutral, host Y/C)_
  - Syarat: studi luar negeri diterima; pulih sebagian
  - Isi: pergi sendiri; surat panjang tiap musim

- [ ] **E-HA-03** · Data yang Dihapus _(Neutral, host Y/C)_
  - Syarat: lepas dari Ogawa; tetap di Kouseikan
  - Isi: kembali ke akademik dengan luka yang tidak dibicarakan

- [ ] **E-HA-04** · Variabel Tetap _(Koita, host Y/C)_
  - Syarat: Koita memilih Harumi di K26; tahap ≤ 2
  - Isi: jalur manga; deviasi rendah untuk Harumi

- [ ] **E-HA-05** · Persamaan Transaksi _(Distorted, host Y/C)_
  - Syarat: validasi_dari banyak orang; tahap 6
  - Isi: hidup transaksional; ia merasa akhirnya "mengerti"

- [ ] **E-HA-06** · Lampu Merah di Distrik Empat _(Bad, host Y/C)_
  - Syarat: putus kuliah; Ogawa menang atau pergi; tanpa penjaga
  - Isi: masuk dunia kerja seks; epilog menyisakan pintu keluar bila seseorang masih mencarinya

- [ ] **E-HA-07** · Ogawa Jatuh _(Neutral, host Y/C)_
  - Syarat: H18-A bersaksi; bukti_ogawa cukup
  - Isi: Ogawa diproses akademik dan hukum; Harumi menjalani pemulihan

- [ ] **E-HA-08** · Ogawa Menang _(Bad, host Y/C)_
  - Syarat: bukti kurang atau ditutupi; pemain penonton
  - Isi: Ogawa lolos; Harumi yang disalahkan; kariernya runtuh

- [ ] **E-HA-09** · Rumah Teh di Kansai _(Neutral, host Y/C)_
  - Syarat: orang tua Kujo menjadi sekutu (H10, H22)
  - Isi: dibawa pulang; cuti; mulai lagi dari teh

- [ ] **E-HA-10** · Eksperimen yang Kau Mulai _(Distorted, host Y/C)_
  - Syarat: H12-C atau H13-D; pemain pengeksploitasi
  - Isi: bergantung pada validasi pemain; pemain tahu ia yang memulai

- [ ] **E-HA-11** · Rumus Tanpa Variabel Cinta _(Neutral, host Y/C)_
  - Syarat: kejelasan_emosi tinggi; hati tidak ke siapa pun
  - Isi: memutuskan romansa bukan untuknya; damai di riset

- [ ] **E-HA-12** · Disosiasi _(Broken, host Y/C)_
  - Syarat: pemain pelaku Force terhadapnya
  - Isi: penelitian terhenti; Mizuhara dan Ogiwara mendorongnya melapor; tanpa romansa dengan pelaku

- [ ] **E-HA-13** · Seni dan Sains _(Romantis, host C)_
  - Syarat: Chiasa host; kolaborasi berjalan sejak Tahun 1
  - Isi: pasangan yang saling menerjemahkan dunia masing-masing

- [ ] **E-HA-14** · Satu Tiket Lagi _(Romantis, host Y/C)_
  - Syarat: H21-C pemain ikut ke luar negeri
  - Isi: pemain meninggalkan Jepang; quest Sistem tetap berjalan dari jauh; evaluasi tetap di hari wisuda

## Kohinata Moeka

_26 event utama · 13 event dinamis · 13 ending_

### Event utama

- [ ] **Mo01** · bulan M01b · Wakil yang Selalu Terlambat
  - Pemicu: Moeka datang terlambat tapi memimpin acara.
  - [ ] Pilihan A — maklum
  - [ ] Pilihan B — tegur
  - [ ] Pilihan C — bantu.
  - Efek: C membuka sisi kompeten.

- [ ] **Mo02** · bulan M02 · Undian Onsen
  - Pemicu: ia memenangkan undian.
  - [ ] Pilihan A — ucapkan selamat
  - [ ] Pilihan B — iri
  - [ ] Pilihan C — bantu rencana.
  - Efek: kedekatan.

- [ ] **Mo03** · bulan M03 · Janji yang Terlupa
  - Pemicu: ia lupa janji dengan pemain.
  - [ ] Pilihan A — marah
  - [ ] Pilihan B — maklum
  - [ ] Pilihan C — bantu mengatur jadwal.
  - Efek: Trust; B/C mengurangi stres.

- [ ] **Mo04** · bulan M05b · Pingsan Karena Lupa Makan
  - Pemicu: di vila.
  - [ ] Pilihan A — rawat
  - [ ] Pilihan B — panggil Miyuki
  - [ ] Pilihan C — abaikan.
  - Efek: intimasi.

- [ ] **Mo05** · bulan M06 · Kabar dari Rumah
  - Pemicu: ibu menelepon.
  - [ ] Pilihan A — dengarkan
  - [ ] Pilihan B — alihkan
  - [ ] Pilihan C — tanya langsung.
  - Efek: membuka masalah keluarga.

- [ ] **Mo06** · bulan M07 · Kuga Renji: Tawaran Foto
  - Pemicu: fotografer menawarkan pekerjaan modeling.
  - [ ] Pilihan A — dukung
  - [ ] Pilihan B — halangi
  - [ ] Pilihan C — ikut menemani.
  - Efek: gerbang awal Kuga.

- [ ] **Mo07** · bulan M08 · Peragaan Pertama
  - Pemicu: ia tampil.
  - [ ] Pilihan A — hadir
  - [ ] Pilihan B — bantu backstage
  - [ ] Pilihan C — absen.
  - Efek: reputasi.

- [ ] **Mo08** · bulan M09 · Natal Moeka dan Adik
  - Pemicu: ia pulang ke rumah.
  - [ ] Pilihan A — ikut
  - [ ] Pilihan B — kirim hadiah
  - [ ] Pilihan C — tidak.
  - Efek: hub besar #3.

- [ ] **Mo09** · bulan M10 · Hatsumode: Doa Ayah
  - Pemicu: ia berdoa untuk ayah.
  - [ ] Pilihan A — temani
  - [ ] Pilihan B — tanya
  - [ ] Pilihan C — abaikan.
  - Efek: Intimasi.

- [ ] **Mo10** · bulan M11 · Coklat untuk Tiga Adik
  - Pemicu: ia membuat coklat untuk adik.
  - [ ] Pilihan A — bantu
  - [ ] Pilihan B — beri uang
  - [ ] Pilihan C — tak peduli.
  - Efek: pemain mengenal adik-adik.

- [ ] **Mo11** · bulan M15 · Hujan Deras: Ponsel Mati
  - Pemicu: ia hilang kontak.
  - [ ] Pilihan A — cari
  - [ ] Pilihan B — tunggu
  - [ ] Pilihan C — abaikan.
  - Efek: jendela intervensi #1; stage 1 (beban menumpuk).

- [ ] **Mo12** · bulan M16 · IPK Turun
  - Pemicu: nilai turun.
  - [ ] Pilihan A — bantu belajar
  - [ ] Pilihan B — beri uang
  - [ ] Pilihan C — tidak peduli.
  - Efek: beasiswa mulai terancam.

- [ ] **Mo13** · bulan M18 · Foto yang Beredar
  - Pemicu: rumor Mei tentang Moeka.
  - [ ] Pilihan A — bantu bantah
  - [ ] Pilihan B — diam
  - [ ] Pilihan C — manfaatkan.
  - Efek: topeng tebal.

- [ ] **Mo14** · bulan M19 · Topeng Tebal
  - Pemicu: ia tampak lebih ceria.
  - [ ] Pilihan A — tanyakan
  - [ ] Pilihan B — percaya
  - [ ] Pilihan C — manfaatkan.
  - Efek: stage 2.

- [ ] **Mo15** · bulan M20 · Surat Peringatan Beasiswa
  - Pemicu: beasiswa diperingatkan.
  - [ ] Pilihan A — hadir
  - [ ] Pilihan B — bantu cari bantuan
  - [ ] Pilihan C — abaikan.
  - Efek: gerbang rute; jendela #2.

- [ ] **Mo16** · bulan M22 · Nilai Kedua
  - Pemicu: semester kedua rendah.
  - [ ] Pilihan A — temani
  - [ ] Pilihan B — bantu cari kerja
  - [ ] Pilihan C — tinggalkan.
  - Efek: beasiswa terancam dicabut.

- [ ] **Mo17** · bulan M23 · Menghilang dari Grup Chat
  - Pemicu: Valentine.
  - [ ] Pilihan A — datangi
  - [ ] Pilihan B — tunggu
  - [ ] Pilihan C — abaikan.
  - Efek: stage 3 (penarikan diri).

- [ ] **Mo18** · bulan M26 · Rina Bicara
  - Pemicu: Rina menegur pemain.
  - [ ] Pilihan A — dengarkan
  - [ ] Pilihan B — tolak
  - [ ] Pilihan C — bela diri.
  - Efek: sekutu atau lawan.

- [ ] **Mo19** · bulan M27 · Barang yang Dibagikan
  - Pemicu: ia membagikan barang kesayangan.
  - [ ] Pilihan A — tanya
  - [ ] Pilihan B — terima
  - [ ] Pilihan C — abaikan.
  - Efek: jendela #3; stage 4 (tanda bahaya).

- [ ] **Mo20** · bulan M28 · Tanzaku Moeka
  - Pemicu: harapan sederhana.
  - [ ] Pilihan A — baca
  - [ ] Pilihan B — tulis bersama
  - [ ] Pilihan C — abaikan.
  - Efek: petunjuk.

- [ ] **Mo21** · bulan M29b · Tertawa Terlalu Keras
  - Pemicu: gasshuku.
  - [ ] Pilihan A — bicara pelan
  - [ ] Pilihan B — ikut tertawa
  - [ ] Pilihan C — abaikan.
  - Efek: tanda bahaya.

- [ ] **Mo22** · bulan M30 · Ren Menelepon
  - Pemicu: adiknya khawatir.
  - [ ] Pilihan A — datang
  - [ ] Pilihan B — kirim uang
  - [ ] Pilihan C — tidak.
  - Efek: jendela #4.

- [ ] **Mo23** · bulan M31 · Kontrak Kuga
  - Pemicu: kontrak modeling.
  - [ ] Pilihan A — tolak
  - [ ] Pilihan B — renegosiasi
  - [ ] Pilihan C — biarkan.
  - Efek: stres bertambah/berkurang.

- [ ] **Mo24** · bulan M32 · Peragaan Terakhir
  - Pemicu: ia tampil.
  - [ ] Pilihan A — hadir
  - [ ] Pilihan B — tinggalkan
  - [ ] Pilihan C — bantu.
  - Efek: reputasi.

- [ ] **Mo26** · bulan M33 · Natal Sunyi
  - Pemicu: ia sendirian.
  - [ ] Pilihan A — datang
  - [ ] Pilihan B — kirim pesan
  - [ ] Pilihan C — tidak ada.
  - Efek: jendela #5.

- [ ] **Mo25** · bulan M34 · Malam Tanpa Balasan
  - Pemicu: tiga pemicu bertemu: surat pencabutan beasiswa, kondisi ayah memburuk, dan orang yang ia andalkan tidak membalas.

### Event dinamis

- [ ] **Mo-D01** · Onigiri Jam Tiga
  - Pemicu: konbini saat Dini Hari; stres_total ≥ 60
  - Ringkasan: duduk makan bersama / tanya langsung / bercanda / antar pulang
  - [ ] Opsi 1 — duduk makan bersama
  - [ ] Opsi 2 — tanya langsung
  - [ ] Opsi 3 — bercanda
  - [ ] Opsi 4 — antar pulang
  - Efek: andalan[[pemain] +; topeng −

- [ ] **Mo-D02** · Panggilan Empat Detik
  - Pemicu: tahap ≥ 2; Larut
  - Ringkasan: panggilan tak terjawab, durasi 4 detik. Telepon balik sekarang / kirim pesan / besok saja
  - [ ] Opsi 1 — Telepon balik sekarang
  - [ ] Opsi 2 — kirim pesan
  - [ ] Opsi 3 — besok saja
  - Efek: jendela kecil; andalan ±

- [ ] **Mo-D03** · Kostum untuk Hinata
  - Pemicu: adik bungsunya ikut pentas sekolah
  - Ringkasan: Moeka menjahit kostum dan mengajak pemain. Datang ke pentas / bantu menjahit malam itu / tidak bisa
  - [ ] Opsi 1 — Datang ke pentas
  - [ ] Opsi 2 — bantu menjahit malam itu
  - [ ] Opsi 3 — tidak bisa
  - Efek: stres_total turun karena bahagia; keluarga mengenal pemain

- [ ] **Mo-D04** · Struk di Lantai
  - Pemicu: pemain di kos Moeka
  - Ringkasan: tagihan cuci darah tergeletak. Tanya / pura-pura tidak lihat / diam-diam membayar sebagian
  - [ ] Opsi 1 — Tanya
  - [ ] Opsi 2 — pura-pura tidak lihat
  - [ ] Opsi 3 — diam-diam membayar sebagian
  - Efek: pemain tahu soal ayah; pilihan "Tanya soal cuci darah ayah" terbuka

- [ ] **Mo-D05** · Lokasi dari Kuga
  - Pemicu: kuga_tekanan ≥ 40
  - Ringkasan: Kuga mengirim lokasi pemotretan malam; Moeka bertanya "temani?". Temani / larang / laporkan / minta Rina menemani
  - [ ] Opsi 1 — Temani
  - [ ] Opsi 2 — larang
  - [ ] Opsi 3 — laporkan
  - [ ] Opsi 4 — minta Rina menemani
  - Efek: jalur Kuga; bukti untuk E-NPC-26

- [ ] **Mo-D06** · Ulang Tahun yang Ia Lupakan
  - Pemicu: hari ulang tahunnya; stres_total ≥ 50
  - Ringkasan: kejutan kecil / pesta besar / kue di depan pintu
  - [ ] Opsi 1 — kejutan kecil
  - [ ] Opsi 2 — pesta besar
  - [ ] Opsi 3 — kue di depan pintu
  - Efek: kecil: topeng −; pesta besar: topeng +

- [ ] **Mo-D07** · Rina Bertanya
  - Pemicu: rina_curiga ≥ 50
  - Ringkasan: "Kamu tahu sesuatu?" Jujur / sangkal / ajak bekerja sama
  - [ ] Opsi 1 — "Kamu tahu sesuatu?" Jujur
  - [ ] Opsi 2 — sangkal
  - [ ] Opsi 3 — ajak bekerja sama
  - Efek: Rina menjadi sekutu; kesempatan kedua di Mo25

- [ ] **Mo-D08** · Formulir Banding
  - Pemicu: beasiswa diperingatkan; kenal Fujisawa
  - Ringkasan: bantu menulis surat banding malam itu / suruh ia menulis sendiri / bayar orang lain
  - [ ] Opsi 1 — bantu menulis surat banding malam itu
  - [ ] Opsi 2 — suruh ia menulis sendiri
  - [ ] Opsi 3 — bayar orang lain
  - Efek: E-MO-09 menguat; membayar orang lain = kebohongan baru

- [ ] **Mo-D09** · Cocok sebagai Donor
  - Pemicu: ayah memburuk
  - Ringkasan: Moeka diam-diam tes kecocokan. Dukung / tentang / beri tahu Aya / temani ke RS (Miyuki melihat)
  - [ ] Opsi 1 — Dukung
  - [ ] Opsi 2 — tentang
  - [ ] Opsi 3 — beri tahu Aya
  - [ ] Opsi 4 — temani ke RS (Miyuki melihat)
  - Efek: cabang donor; stres[[ayah] −40 bila jadi; beasiswa terancam

- [ ] **Mo-D10** · Tawa di Grup Jam Dua
  - Pemicu: topeng ≥ 70
  - Ringkasan: ia mengirim banyak pesan ceria di grup tengah malam. Balas candaan / japri "kamu oke?" / abaikan
  - [ ] Opsi 1 — Balas candaan
  - [ ] Opsi 2 — japri "kamu oke?"
  - [ ] Opsi 3 — abaikan
  - Efek: japri: andalan[[pemain] +, topeng −

- [ ] **Mo-D11** · Barang yang Dikembalikan
  - Pemicu: tahap 4
  - Ringkasan: ia mengembalikan barang pinjaman lama. Tanya kenapa / terima / ceritakan pada Rina
  - [ ] Opsi 1 — Tanya kenapa
  - [ ] Opsi 2 — terima
  - [ ] Opsi 3 — ceritakan pada Rina
  - Efek: tanda bahaya; menerima tanpa bertanya = jendela kecil terlewat

- [ ] **Mo-D12** · Pertanyaan Langsung
  - Pemicu: tahap ≥ 3; pemain mengenali tanda (Intim ≥ 55 atau Rina memberi tahu)
  - Ringkasan: pilihan bertanya langsung dan tenang muncul. Tanya langsung lalu tetap tinggal / tanya sambil bercanda / tidak berani
  - [ ] Opsi 1 — Tanya langsung lalu tetap tinggal
  - [ ] Opsi 2 — tanya sambil bercanda
  - [ ] Opsi 3 — tidak berani
  - Efek: tanya langsung: ia menangis dan bercerita; jendela diambil; jalan ke Sato Kyoko dan bantuan profesional terbuka

- [ ] **Mo-D13** · Sketsa Label Pertama
  - Pemicu: stres_total < 40; Aff ≥ 55
  - Ringkasan: ia menunjukkan rancangan label sendiri. Dukung / ajak Rina / kritik
  - [ ] Opsi 1 — Dukung
  - [ ] Opsi 2 — ajak Rina
  - [ ] Opsi 3 — kritik
  - Efek: E-MO-08 menguat

### Ending

- [ ] **E-MO-01** · Belajar Meminta Tolong _(Romantis, host Y/C)_
  - Syarat: minimal 3 jendela diambil; andalan_moeka pemain; janji ditepati; tanpa Force
  - Isi: ia belajar meminta tolong; keluarga mulai stabil

- [ ] **E-MO-02** · Cuti Setahun _(Neutral, host Y/C)_
  - Syarat: selamat; beasiswa dicabut
  - Isi: cuti kuliah; bekerja membantu keluarga; kembali setahun kemudian

- [ ] **E-MO-03** · Topeng Sempurna _(Distorted, host Y/C)_
  - Syarat: selamat; topeng tidak pernah dibuka; pemain satu-satunya andalan
  - Isi: tampak baik-baik saja; topengnya total; hidupnya bergantung pada pemain

- [ ] **E-MO-04** · Malam Tanpa Balasan _(Bad, host Y/C)_
  - Syarat: Mo25 terlewati
  - Isi: Moeka meninggal. Yang ditampilkan: kabar, duka, pemakaman, Rina, Aya, adik-adik, penyesalan pemain. Tanpa metode. Sistem diam

- [ ] **E-MO-05** · Tepat Waktu _(Koita, host Y/C)_
  - Syarat: Mo25-E pemain mengirim Koita, atau andalan_moeka Koita dan Koita menjawab
  - Isi: plot armor menyelamatkannya; hatinya kembali ke Koita

- [ ] **E-MO-06** · Rina Mengetuk Pintu _(Neutral, host Y/C)_
  - Syarat: Mo25-B, atau Rina sekutu sejak Mo18
  - Isi: Rina tiba lebih dulu; dirawat; persahabatan pemain dan Rina menentukan epilog

- [ ] **E-MO-07** · Kontrak Kuga _(Distorted, host Y/C)_
  - Syarat: Mo23 kontrak dibiarkan; selamat
  - Isi: meninggalkan kampus untuk kontrak modeling yang eksploitatif; topeng menjadi pekerjaan

- [ ] **E-MO-08** · Label di Garasi _(Neutral, host Y/C)_
  - Syarat: berhenti kuliah; stres keluarga turun; Rina sekutu
  - Isi: merintis label fesyen kecil bersama Rina; adik-adik membantu

- [ ] **E-MO-09** · Banding yang Dimenangkan _(Neutral, host Y/C)_
  - Syarat: beasiswa diselamatkan lewat Fujisawa, Sato, atau banding
  - Isi: lulus; keluarga bertahan; tanpa romansa

- [ ] **E-MO-10** · Doa yang Tidak Terkabul _(Neutral, host Y/C)_
  - Syarat: ayah_status meninggal; minimal 3 jendela diambil
  - Isi: ayahnya meninggal; Moeka bertahan karena tidak sendirian

- [ ] **E-MO-11** · Topeng yang Pecah _(Broken, host Y/C)_
  - Syarat: pemain pelaku Force terhadapnya
  - Isi: risiko krisis melonjak; jendela intervensi tetap ada; tidak ada ending tenang

- [ ] **E-MO-12** · Selamat, Tapi Bukan Karenamu _(Neutral, host Y/C)_
  - Syarat: pemain melewatkan banyak jendela; orang lain menyelamatkannya
  - Isi: ia hidup dan memutus hubungan dengan pemain

- [ ] **E-MO-13** · Ginjal untuk Ayah _(Romantis, host Y/C)_
  - Syarat: cabang donor diambil; pemain mendampingi
  - Isi: ayah pulih; Moeka cuti; pengorbanan yang tidak ia sesali

## Saionji Shiori

_25 event utama · 17 event dinamis · 16 ending_

### Event utama

- [ ] **S01** · bulan M01b · Papan Shogi di Taman
  - Pemicu: ia bermain sendiri.
  - [ ] Pilihan A — menantang
  - [ ] Pilihan B — mengamati
  - [ ] Pilihan C — lewat.
  - Efek: A membuka rivalitas.

- [ ] **S02** · bulan M02 · Ruang Catur di Ryokan
  - Pemicu: papan di lobi.
  - [ ] Pilihan A — bertanding
  - [ ] Pilihan B — sengaja kalah
  - [ ] Pilihan C — menang.
  - Efek: B membuat ia jengkel.

- [ ] **S03** · bulan M03 · Payung Hujan
  - Pemicu: dasar manga: ia dan Koita berbagi payung.
  - [ ] Pilihan A — intersep
  - [ ] Pilihan B — tawarkan payung kedua
  - [ ] Pilihan C — biarkan.
  - Efek: menentukan ketertarikan Shiori pada Koita.

- [ ] **S04** · bulan M05b · Pertandingan Malam di Vila
  - Pemicu: ia bermain shogi sampai larut.
  - [ ] Pilihan A — temani
  - [ ] Pilihan B — menang jujur
  - [ ] Pilihan C — menyontek.
  - Efek: C masuk daftar kebohongan.

- [ ] **S05** · bulan M07 · Tojo Akihiro di Pesta
  - Pemicu: pewaris Tojo mendekatinya.
  - [ ] Pilihan A — lindungi
  - [ ] Pilihan B — abaikan
  - [ ] Pilihan C — manfaatkan.
  - Efek: tojo_aktif.

- [ ] **S06** · bulan M08 · Turnamen Klub Catur
  - Pemicu: ia berpartisipasi.
  - [ ] Pilihan A — hadir
  - [ ] Pilihan B — ikut
  - [ ] Pilihan C — absen.
  - Efek: Trust.

- [ ] **S07** · bulan M09 · Natal Keluarga Saionji
  - Pemicu: makan malam keluarga.
  - [ ] Pilihan A — diundang
  - [ ] Pilihan B — tidak
  - [ ] Pilihan C — mengirim hadiah.
  - Efek: hub besar #3; keluarga mengenal pemain.

- [ ] **S08** · bulan M11 · Festival: Satu Tahun
  - Pemicu: peringatan perkenalan dengan Koita.
  - [ ] Pilihan A — hadir
  - [ ] Pilihan B — mengantisipasi
  - [ ] Pilihan C — mengganggu.
  - Efek: dasar manga: ia mulai mencintai Koita.

- [ ] **S09** · bulan M12 · Tawaran Persahabatan
  - Pemicu: ia meminta teman sejati.
  - [ ] Pilihan A — terima
  - [ ] Pilihan B — tolak
  - [ ] Pilihan C — manfaatkan.
  - Efek: shiori_kepercayaan.

- [ ] **S10** · bulan M15 · Hujan Deras: Kuroiwa Menjemput
  - Pemicu: ia dijemput.
  - [ ] Pilihan A — ikut
  - [ ] Pilihan B — tolak.
  - Efek: Kuroiwa mencatat.

- [ ] **S11** · bulan M16 · Peringkat Pertama
  - Pemicu: ujian.
  - [ ] Pilihan A — kompetisi
  - [ ] Pilihan B — bantu
  - [ ] Pilihan C — menyontek.
  - Efek: C masuk daftar.

- [ ] **S12** · bulan M18 · Rumor tentang Shiori
  - Pemicu: Mei menulis.
  - [ ] Pilihan A — bantu bantah
  - [ ] Pilihan B — diam
  - [ ] Pilihan C — menyebar.
  - Efek: reputasi.

- [ ] **S13** · bulan M20 · Penemuan
  - Pemicu: ia menemukan kebohongan pemain atau pengkhianatan pada orang yang ia pedulikan.
  - [ ] Pilihan A — mengaku
  - [ ] Pilihan B — menyangkal
  - [ ] Pilihan C — lari.
  - Efek: gerbang Rute Revenge (stage 2).

- [ ] **S14** · bulan M21 · Natal Kedua: Senyum yang Sama
  - Pemicu: ia tidak marah dan tidak menjauh; ia tersenyum persis seperti biasa.
  - [ ] Pilihan A — minta maaf
  - [ ] Pilihan B — menyalahkan
  - [ ] Pilihan C — menghindar.
  - Efek: stage 3.

- [ ] **S15** · bulan M22 · Hatsumode: Doa untuk Siapa
  - Pemicu: ia berdoa.
  - [ ] Pilihan A — tanya
  - [ ] Pilihan B — tidak
  - [ ] Pilihan C — ikut.
  - Efek: petunjuk.

- [ ] **S16** · bulan M23 · Valentine: Papan Kosong
  - Pemicu: ia tidak menjawab.
  - [ ] Pilihan A — datang
  - [ ] Pilihan B — tunggu
  - [ ] Pilihan C — abaikan.
  - Efek: stage 3.

- [ ] **S17** · bulan M25 · Keputusan Warisan
  - Pemicu: ia memutuskan masa depan.
  - [ ] Pilihan A — dukung
  - [ ] Pilihan B — ganggu.
  - Efek: karier.

- [ ] **S18** · bulan M27 · Hujan Terakhir: Pengumpulan Bukti
  - Pemicu: ia mengumpulkan.
  - [ ] Pilihan A — hapus bukti
  - [ ] Pilihan B — perbaiki
  - [ ] Pilihan C — tidak peduli.
  - Efek: stage 4; titik tanpa balik setelah ini hanya ending Distorted/Bad.

- [ ] **S19** · bulan M28 · Tanzaku Shiori
  - Pemicu: harapannya.
  - [ ] Pilihan A — baca
  - [ ] Pilihan B — abaikan.
  - Efek: petunjuk.

- [ ] **S20** · bulan M29b · Permainan Terakhir
  - Pemicu: shogi di vila.
  - [ ] Pilihan A — bertanding
  - [ ] Pilihan B — mengalah
  - [ ] Pilihan C — menolak.
  - Efek: pesan tersirat.

- [ ] **S21** · bulan M30 · Pengumuman: Tojo
  - Pemicu: Tojo diumumkan sebagai calon tunangan.
  - [ ] Pilihan A — halangi
  - [ ] Pilihan B — dukung
  - [ ] Pilihan C — manfaatkan.
  - Efek: Shiori memakai Tojo sebagai bidak.

- [ ] **S22** · bulan M31 · Penghancuran Dimulai
  - Pemicu: ia bergerak.
  - [ ] Pilihan A — melawan
  - [ ] Pilihan B — mengaku
  - [ ] Pilihan C — lari.
  - Efek: stage 5.

- [ ] **S23** · bulan M32 · Turnamen Akhir
  - Pemicu: ia menang.
  - [ ] Pilihan A — hadir
  - [ ] Pilihan B — gagal
  - [ ] Pilihan C — mengganggu.
  - Efek: reputasi.

- [ ] **S24** · bulan M33 · Natal: Skakmat
  - Pemicu: puncaknya.
  - [ ] Pilihan A — menyerah
  - [ ] Pilihan B — membalas
  - [ ] Pilihan C — menjadi sekutu.
  - Efek: menentukan ending.

- [ ] **S25** · bulan M35 · Pilihan Shiori
  - Pemicu: keputusan akhir. *Efek:* ending Shiori.

### Event dinamis

- [ ] **S-D01** · Langkah Jam Dua Belas
  - Pemicu: pemain tahu jam online Shiori
  - Ringkasan: main serius / ajak bicara di chat / log off tiba-tiba
  - [ ] Opsi 1 — main serius
  - [ ] Opsi 2 — ajak bicara di chat
  - [ ] Opsi 3 — log off tiba-tiba
  - Efek: akun_anonim +; log off tiba-tiba membuatnya curiga

- [ ] **S-D02** · Kuroiwa di Parkiran
  - Pemicu: kuroiwa_percaya ≥ 50, atau marah[[pemain] ≥ 40
  - Ringkasan: Kuroiwa mendekati pemain. Jujur / menghindar dengan sopan / tanya soal Shiori
  - [ ] Opsi 1 — Jujur
  - [ ] Opsi 2 — menghindar dengan sopan
  - [ ] Opsi 3 — tanya soal Shiori
  - Efek: Kuroiwa menjadi saluran peringatan

- [ ] **S-D03** · Kekalahan yang Ia Rayakan
  - Pemicu: respek ≥ 60
  - Ringkasan: Shiori kalah secara adil dan justru senang. Rayakan bersama / sombong / minta tanding ulang
  - [ ] Opsi 1 — Rayakan bersama
  - [ ] Opsi 2 — sombong
  - [ ] Opsi 3 — minta tanding ulang
  - Efek: E-SH-01 menguat

- [ ] **S-D04** · Pertanyaan Jebakan
  - Pemicu: daftar_kebohongan ≥ 1
  - Ringkasan: pertanyaan yang dirancang untuk menangkap kebohongan. Jujur sekarang / bohong lebih rapi / alihkan
  - [ ] Opsi 1 — Jujur sekarang
  - [ ] Opsi 2 — bohong lebih rapi
  - [ ] Opsi 3 — alihkan
  - Efek: jujur sekarang lebih murah; bohong yang ketahuan belakangan dihitung dua kali

- [ ] **S-D05** · Buku Bertanda Tangan
  - Pemicu: Chiasa host
  - Ringkasan: Shiori membawa buku berilustrasi Shena ke kelas. Akui / pura-pura tidak tahu / tawarkan tanda tangan
  - [ ] Opsi 1 — Akui
  - [ ] Opsi 2 — pura-pura tidak tahu
  - [ ] Opsi 3 — tawarkan tanda tangan
  - Efek: jembatan atau perangkap Shena

- [ ] **S-D06** · Gala dan Tojo
  - Pemicu: Tojo aktif
  - Ringkasan: ia meminta pemain menjadi pasangan pengalih di gala. Terima / tolak / datang bersama orang lain
  - [ ] Opsi 1 — Terima
  - [ ] Opsi 2 — tolak
  - [ ] Opsi 3 — datang bersama orang lain
  - Efek: orang tua Saionji bertemu pemain; jalur Tojo

- [ ] **S-D07** · Kartu yang Ia Tunjukkan
  - Pemicu: marah[[koita] ≥ 40
  - Ringkasan: Shiori menunjukkan bukti pola Koita yang ia temukan. "Kau sudah tahu?" Akui / sangkal / tambahkan bukti
  - [ ] Opsi 1 — "Kau sudah tahu?" Akui
  - [ ] Opsi 2 — sangkal
  - [ ] Opsi 3 — tambahkan bukti
  - Efek: menambahkan bukti mengalihkan sasaran ke Koita (E-SH-09)

- [ ] **S-D08** · Teh dengan Ibu Saionji
  - Pemicu: setelah S07-A
  - Ringkasan: ibunya bertanya soal kesepian Shiori. Jujur / menyanjung / membocorkan
  - [ ] Opsi 1 — Jujur
  - [ ] Opsi 2 — menyanjung
  - [ ] Opsi 3 — membocorkan
  - Efek: kehangatan keluarga; Shiori tahu apa yang dikatakan

- [ ] **S-D09** · Papan yang Ditinggalkan
  - Pemicu: tahap 3
  - Ringkasan: papan shogi setengah jalan di ruang klub; langkah terakhirnya menunjuk kebohongan pemain. Lanjutkan dengan satu langkah / bereskan / tinggalkan
  - [ ] Opsi 1 — Lanjutkan dengan satu langkah
  - [ ] Opsi 2 — bereskan
  - [ ] Opsi 3 — tinggalkan
  - Efek: langkah balasan bisa menjadi pengakuan; S20 datang lebih awal

- [ ] **S-D10** · Musuh Bersama
  - Pemicu: pemain memberi bukti tentang Ogawa atau Kuga
  - Ringkasan: Shiori menawarkan persekutuan. Bergabung / biarkan ia sendiri / minta ia berhenti
  - [ ] Opsi 1 — Bergabung
  - [ ] Opsi 2 — biarkan ia sendiri
  - [ ] Opsi 3 — minta ia berhenti
  - Efek: E-SH-10 menguat; Harumi dan Moeka terbantu

- [ ] **S-D11** · Prediksi yang Benar
  - Pemicu: pemain sudah menceritakan Sistem
  - Ringkasan: prediksi pemain terbukti. Lanjut terbuka / minta ia menyimpan rahasia / manfaatkan dia
  - [ ] Opsi 1 — Lanjut terbuka
  - [ ] Opsi 2 — minta ia menyimpan rahasia
  - [ ] Opsi 3 — manfaatkan dia
  - Efek: E-SH-06 menguat

- [ ] **S-D12** · Ratu yang Jatuh Sakit
  - Pemicu: tahap 4; ia begadang menyusun bukti
  - Ringkasan: Kuroiwa mengizinkan pemain menjenguk bila percaya. Rawat / cari bukti di kamarnya / tinggalkan buah
  - [ ] Opsi 1 — Rawat
  - [ ] Opsi 2 — cari bukti di kamarnya
  - [ ] Opsi 3 — tinggalkan buah
  - Efek: merawat: marah[[pemain] turun banyak; mencari bukti: kejahatan baru dan marah[[pemain] +40

- [ ] **S-D13** · Rahasia Palsu
  - Pemicu: Trust Sedang
  - Ringkasan: Shiori menitipkan "rahasia" kecil pada pemain, sebenarnya umpan. Simpan / ceritakan ke orang lain / jual ke Mei
  - [ ] Opsi 1 — Simpan
  - [ ] Opsi 2 — ceritakan ke orang lain
  - [ ] Opsi 3 — jual ke Mei
  - Efek: bila rahasia itu muncul di mana pun, ia tahu sumbernya; ujian gagal dan marah[[pemain] naik

- [ ] **S-D14** · Kesempatan Kecil untuk Berkhianat
  - Pemicu: Trust Sedang; pemain sedang butuh sesuatu
  - Ringkasan: ia mengatur situasi di mana pemain bisa untung dengan mengorbankan orang kecil. Ambil / tolak / ambil lalu mengaku
  - [ ] Opsi 1 — Ambil
  - [ ] Opsi 2 — tolak
  - [ ] Opsi 3 — ambil lalu mengaku
  - Efek: menolak: respek +10; mengambil: ujian gagal, dan pemain tidak sadar sedang diuji

- [ ] **S-D15** · Senyum Paling Manis
  - Pemicu: marah[[pemain] ≥ 60; pemain belum mengaku
  - Ringkasan: Shiori tampak jatuh cinta: lebih hangat, mengajak kencan, bersandar di bahu. Nikmati / amati isyaratnya / mengaku semuanya sekarang
  - [ ] Opsi 1 — Nikmati
  - [ ] Opsi 2 — amati isyaratnya
  - [ ] Opsi 3 — mengaku semuanya sekarang
  - Efek: menikmati dan membuka rahasia: E-SH-16. Membaca isyarat (butuh senyum_terbaca ≥ 70) membuka kesempatan mengaku

- [ ] **S-D16** · Langkah yang Terlalu Cepat
  - Pemicu: senyum_terbaca ≥ 40; sedang bertanding
  - Ringkasan: langkah shogi-nya lebih cepat dari biasanya. Tanya "ada apa?" / pura-pura tidak sadar / balas dengan langkah lambat
  - [ ] Opsi 1 — Tanya "ada apa?"
  - [ ] Opsi 2 — pura-pura tidak sadar
  - [ ] Opsi 3 — balas dengan langkah lambat
  - Efek: bertanya tepat waktu: senyum_terbaca +10, dan ia sedikit terkejut

- [ ] **S-D17** · Papan yang Dibalik
  - Pemicu: bukti_terkumpul ≥ 50, atau pemain hampir menang
  - Ringkasan: sambil tersenyum, Shiori menunjukkan bahwa ia sudah tahu sejak lama. Menyerah / balas dengan langkah jujur yang tak terduga / tertawa bersamanya
  - [ ] Opsi 1 — Menyerah
  - [ ] Opsi 2 — balas dengan langkah jujur yang tak terduga
  - [ ] Opsi 3 — tertawa bersamanya
  - Efek: menyerah: E-SH-03 atau E-SH-15; langkah jujur yang tak terduga: respek +15, satu-satunya pintu kembali setelah S18

### Ending

- [ ] **E-SH-01** · Lawan Tanding Seumur Hidup _(Romantis, host Y/C)_
  - Syarat: respek ≥ 80; Trust ≥ 80; tidak ada kebohongan yang ia temukan sendiri; lulus semua ujiannya; tanpa Force
  - Isi: lawan tanding sekaligus pasangan; ambang romansa tertinggi di seluruh game

- [ ] **E-SH-02** · Skakmat _(Bad, host Y/C)_
  - Syarat: tahap 5; sasaran pemain; tanpa pengakuan
  - Isi: pemain dikeluarkan dan dijauhi semua lingkungan; semua target quest menjauh

- [ ] **E-SH-03** · Gencatan Senjata _(Neutral, host Y/C)_
  - Syarat: pemain mengaku di S22 atau S24
  - Isi: penghancuran berhenti; mereka tidak lagi bicara

- [ ] **E-SH-04** · Ratu Tanpa Kepercayaan _(Distorted, host Y/C)_
  - Syarat: tahap 5 tuntas; tidak ada yang ia percaya lagi
  - Isi: Shiori menang tetapi kehilangan kemampuan percaya

- [ ] **E-SH-05** · Langkah Koita _(Koita, host Y/C)_
  - Syarat: cinta Koita tumbuh di S08; Koita memilihnya di K26
  - Isi: jalur manga; deviasi rendah untuk Shiori

- [ ] **E-SH-06** · Sekutu di Papan yang Sama _(Neutral, host Y/C)_
  - Syarat: pemain memberitahunya soal Sistem; tahu_sistem percaya
  - Isi: Shiori menjadi ahli strategi pemain melawan naskah; persahabatan, bukan cinta

- [ ] **E-SH-07** · Pewaris dengan Caranya Sendiri _(Neutral, host Y/C)_
  - Syarat: tanpa rute aktif; S17 didukung
  - Isi: fokus karier; membatalkan pertunangan Tojo dengan strateginya sendiri

- [ ] **E-SH-08** · Bidak Bernama Tojo _(Distorted, host Y/C)_
  - Syarat: S21 Tojo dipakai sampai M35
  - Isi: pertunangan tanpa cinta sebagai hukuman bagi dirinya sendiri; ia tetap tersenyum di setiap foto; ikatan sosial, bukan pasangan romantis baru

- [ ] **E-SH-09** · Ratu Menjatuhkan Protagonis _(Khusus, host Y/C)_
  - Syarat: sasaran_balas Koita
  - Isi: Koita dijatuhkan di depan semua orang; deviasi sangat tinggi; E-KO-09 terkunci

- [ ] **E-SH-10** · Keadilan yang Tersenyum _(Khusus, host Y/C)_
  - Syarat: sasaran_balas Ogawa, Kuga, atau Mei; pemain memberi bukti
  - Isi: pelaku dijatuhkan; Shiori dan pemain menjadi sekutu yang saling waspada

- [ ] **E-SH-11** · Jalur Hukum _(Broken, host Y/C)_
  - Syarat: pemain pelaku Force terhadapnya
  - Isi: Rute Revenge teraktivasi paling cepat lewat hukum dan sosial; pemain dikeluarkan dan dipenjara; tanpa romansa

- [ ] **E-SH-12** · Shena dan Pembacanya _(Romantis, host C)_
  - Syarat: Chiasa mengaku sebagai Shena sebelum Shiori menemukannya sendiri; respek ≥ 70; tanpa kebohongan lain yang ia temukan
  - Isi: pembaca dan ilustratornya

- [ ] **E-SH-13** · Shena dan Penipunya _(Bad, host C)_
  - Syarat: Chiasa berbohong soal Shena lalu ketahuan
  - Isi: revenge menyasar karier Shena dan rahasia Chiasa

- [ ] **E-SH-14** · Lawan Tanpa Nama _(Romantis, host Y/C)_
  - Syarat: akun anonim aktif lama; pemain mengaku sendiri sebelum ketahuan; respek ≥ 70; tanpa kebohongan lain yang ia temukan
  - Isi: lawan online yang ia tunggu tiap malam ternyata duduk di kelasnya

- [ ] **E-SH-15** · Pion di Papan Orang Lain _(Distorted, host Y/C)_
  - Syarat: Shiori memegang semua rahasia pemain tetapi memilih tidak menghancurkannya
  - Isi: pemain tetap kuliah dan tampak bebas, tetapi setiap langkahnya kini atas izin Shiori; ia tersenyum setiap kali mereka berpapasan

- [ ] **E-SH-16** · Senyum Terakhir _(Bad, host Y/C)_
  - Syarat: S-D15 umpan berhasil; pemain membuka rahasia terakhirnya padanya
  - Isi: pemain mengira sudah memenangkan hatinya; di M35 Shiori menunjukkan papannya, dan semuanya runtuh dalam satu hari

## Amamiya Chiasa

_18 event utama · 15 event dinamis · 24 ending_

### Event utama

- [ ] **C01** · bulan M01a · Terbangun di Kamar Chiasa
  - Pemicu: pagi 7 April; prolog.
  - [ ] Pilihan A — cek cermin dan buku sketsa
  - [ ] Pilihan B — cek ponsel
  - [ ] Pilihan C — turun sarapan
  - [ ] Pilihan D — menunggu Sistem.
  - Efek: kesan_awal; A mengungkap pita dan ciri visual.

- [ ] **C02** · bulan M01a · "Ko-nii?"
  - Pemicu: sarapan bersama Koita.
  - [ ] Pilihan A — memanggil "Ko-nii" natural
  - [ ] Pilihan B — memanggil nama
  - [ ] Pilihan C — menggoda seperti Chiasa asli.
  - Efek: B memicu curiga Koita; C menaikkan Jealousy Koita.

- [ ] **C03** · bulan M04 · Tanzaku Chiasa
  - Pemicu: Tanabata; Chiasa menulis tanzaku (apa pun).
  - [ ] Pilihan A — menulis harapan baru
  - [ ] Pilihan B — menyalin harapan asli
  - [ ] Pilihan C — tidak menulis.
  - Efek: harapan_pemain; C membuat Haruka bertanya.

- [ ] **C04** · bulan M05a · "Nacchan-oneechan"
  - Pemicu: Nagisa di festival; Chiasa kecil biasa memanggil begitu.
  - [ ] Pilihan A — pakai julukan
  - [ ] Pilihan B — pakai nama biasa
  - [ ] Pilihan C — menantang Nagisa.
  - Efek: A membangkitkan kenangan; B dingin; C memperkuat rivalitas.

- [ ] **C05** · bulan M08 · Mio Menelepon
  - Pemicu: editor meminta cover jilid baru.
  - [ ] Pilihan A — menolak halus
  - [ ] Pilihan B — menerima dan berlatih
  - [ ] Pilihan C — minta bantuan Haruka.
  - Efek: curiga_mio; B bisa membuka kemampuan baru bertahap.

- [ ] **C06** · bulan M09 · Natal Rumah Amamiya
  - [ ] Pilihan A — di rumah bersama Koita
  - [ ] Pilihan B — mengundang heroine
  - [ ] Pilihan C — pergi ke Nagisa/yuri
  - [ ] Pilihan D — sendirian.
  - Efek: hub besar #3.

- [ ] **C07** · bulan M11 · Coklat untuk Banyak Orang
  - Pemicu: Valentine.
  - [ ] Pilihan A — coklat untuk Koita
  - [ ] Pilihan B — untuk heroine tertentu
  - [ ] Pilihan C — untuk Yutaka
  - [ ] Pilihan D — tidak memberi.
  - Efek: gerbang jalur yuri/Koita Success/Yutaka.

- [ ] **C08** · bulan M13 · Haruka Curiga
  - Pemicu: gambar sketsa pemain berubah gaya.
  - [ ] Pilihan A — kerjakan lagi dari nol
  - [ ] Pilihan B — beralasan "stres"
  - [ ] Pilihan C — mengaku sebagian.
  - Efek: curiga_haruka; risiko rahasia Shena terbongkar.

- [ ] **C09** · bulan M16 · Buku Sketsa Kosong
  - Pemicu: pemain tidak bisa menggambar sebaik asli.
  - [ ] Pilihan A — latihan keras
  - [ ] Pilihan B — menyewa pihak lain
  - [ ] Pilihan C — berhenti.
  - Efek: royalti ¥50.000 tetap masuk (), tetapi tawaran proyek dari Mio bisa gagal.

- [ ] **C10** · bulan M17a · Rival di Yukata
  - Pemicu: Nagisa di festival kedua.
  - [ ] Pilihan A — damai
  - [ ] Pilihan B — tantang
  - [ ] Pilihan C — goda.
  - Efek: kebangkitan rivalitas atau kedamaian.

- [ ] **C11** · bulan M20 · Pameran Kecil dan Shiori
  - Pemicu: Shiori datang ke pameran; ia pembaca Shena.
  - [ ] Pilihan A — mengaku
  - [ ] Pilihan B — pura-pura tidak tahu
  - [ ] Pilihan C — beri tanda tangan.
  - Efek: jembatan ke Shiori atau perangkap (Rute Revenge jika kebohongan).

- [ ] **C12** · bulan M21 · Orang Tua Pulang
  - Pemicu: Daisuke dan Yoshie pulang di Natal.
  - [ ] Pilihan A — menyambut
  - [ ] Pilihan B — menghindar
  - [ ] Pilihan C — membuka rahasia.
  - Efek: gerbang Koita Success (tahap 3).

- [ ] **C13** · bulan M23 · Hari Bentrok: Chiasa
  - Pemicu: hari pengakuan.
  - [ ] Pilihan A — mengaku pada Koita
  - [ ] Pilihan B — mengaku pada heroine
  - [ ] Pilihan C — mengaku pada Yutaka
  - [ ] Pilihan D — tidak mengaku.
  - Efek: hub besar #8.

- [ ] **C14** · bulan M26 · Perjalanan Perpisahan
  - [ ] Pilihan A — menghabiskan waktu dengan Koita
  - [ ] Pilihan B — dengan Nagisa
  - [ ] Pilihan C — dengan heroine lain.
  - Efek: mempersempit jalur.

- [ ] **C15** · bulan M29a · Kembang Api dan Nagisa
  - [ ] Pilihan A — mengaku
  - [ ] Pilihan B — bergandeng
  - [ ] Pilihan C — menjaga jarak.
  - Efek: jalur yuri Nagisa.

- [ ] **C16** · bulan M31 · Cover vs Skripsi
  - [ ] Pilihan A — fokus kuliah
  - [ ] Pilihan B — fokus proyek
  - [ ] Pilihan C — berhenti.
  - Efek: karier Chiasa.

- [ ] **C17** · bulan M32 · Pameran Tunggal
  - [ ] Pilihan A — hadir sendiri
  - [ ] Pilihan B — mengundang seseorang
  - [ ] Pilihan C — membatalkan.
  - Efek: publik melihat siapa dekat dengan siapa.

- [ ] **C18** · bulan M35 · Pilihan Chiasa
  - Efek: lolos atau gagal evaluasi; ending Chiasa (Koita Success / Yutaka / Yuri / mandiri).

### Event dinamis

- [ ] **C-D01** · Dapur Jam Dua
  - Pemicu: Chiasa host; Koita menulis sampai larut
  - Ringkasan: buatkan teh untuk Koita / goda / bicara serius / kembali ke kamar
  - [ ] Opsi 1 — buatkan teh untuk Koita
  - [ ] Opsi 2 — goda
  - [ ] Opsi 3 — bicara serius
  - [ ] Opsi 4 — kembali ke kamar
  - Efek: benih Koita Success atau ikatan saudara

- [ ] **C-D02** · Dua Sketsa Berdampingan
  - Pemicu: Chiasa host; shena_risiko ≥ 40
  - Ringkasan: Haruka meletakkan sketsa lama dan baru berdampingan. Jujur / beri alasan / minta Haruka mengajar
  - [ ] Opsi 1 — Jujur
  - [ ] Opsi 2 — beri alasan
  - [ ] Opsi 3 — minta Haruka mengajar
  - Efek: rahasia Shena dibagi, atau curiga naik

- [ ] **C-D03** · Tangan yang Gemetar
  - Pemicu: Chiasa host; berlatih saat Sangat Lelah
  - Ringkasan: berhenti dan tidur / paksa sampai pagi / minta Haruka mengajar
  - [ ] Opsi 1 — berhenti dan tidur
  - [ ] Opsi 2 — paksa sampai pagi
  - [ ] Opsi 3 — minta Haruka mengajar
  - Efek: kemampuan_gambar hanya naik sedikit saat lelah; tubuh menanggung

- [ ] **C-D04** · Hari Pertama
  - Pemicu: Chiasa host; siklus jatuh di hari penting
  - Ringkasan: tetap hadir / izin / minta bantuan Haruka atau Yoshie lewat video call
  - [ ] Opsi 1 — tetap hadir
  - [ ] Opsi 2 — izin
  - [ ] Opsi 3 — minta bantuan Haruka atau Yoshie lewat video call
  - Efek: hasil event hari itu bergeser; Yoshie menjadi lebih dekat

- [ ] **C-D05** · Video Call dari Luar Negeri
  - Pemicu: kedua route
  - Ringkasan: Daisuke menelepon jam 03:00 waktu Jepang. (C) "Kamu berubah, Nak." (Y) Daisuke meminta Yutaka menjaga Chiasa
  - Efek: curiga identitas (C) atau tanggung jawab baru (Y)

- [ ] **C-D06** · Pagar di Antara Dua Rumah
  - Pemicu: kedua route; Nagisa dan Chiasa sama-sama di rumah
  - Ringkasan: adu mulut di pagar. Lerai / ikut / tonton
  - [ ] Opsi 1 — Lerai
  - [ ] Opsi 2 — ikut
  - [ ] Opsi 3 — tonton
  - Efek: rivalitas atau damai; Koita Success bisa ketahuan

- [ ] **C-D07** · Pesan Mio Jam Sebelas
  - Pemicu: Chiasa host; ada proyek
  - Ringkasan: mengaku tidak sanggup / minta perpanjangan / sewa ilustrator / begadang
  - [ ] Opsi 1 — mengaku tidak sanggup
  - [ ] Opsi 2 — minta perpanjangan
  - [ ] Opsi 3 — sewa ilustrator
  - [ ] Opsi 4 — begadang
  - Efek: menyewa = kebohongan baru yang bisa ditemukan Shiori; begadang = tubuh dan kemampuan

- [ ] **C-D08** · Kopi dari Yutaka
  - Pemicu: Chiasa host; Yutaka NPC mengabari dulu
  - Ringkasan: ia mampir membawa kopi malam. Undang masuk / mengobrol di teras / tolak
  - [ ] Opsi 1 — Undang masuk
  - [ ] Opsi 2 — mengobrol di teras
  - [ ] Opsi 3 — tolak
  - Efek: yutaka_harap ±; Koita melihat dari jendela

- [ ] **C-D09** · Tangis di Ruang Tamu
  - Pemicu: Male Route; Koita baru menggantung Chiasa
  - Ringkasan: Yutaka menemukan Chiasa menangis. Hibur / panggil Koita / pergi / manfaatkan
  - [ ] Opsi 1 — Hibur
  - [ ] Opsi 2 — panggil Koita
  - [ ] Opsi 3 — pergi
  - [ ] Opsi 4 — manfaatkan
  - Efek: nyaman_yutaka ±; memanfaatkan membuka E-CH-11

- [ ] **C-D10** · Bandara Jam Lima
  - Pemicu: kedua route; orang tua pulang mendadak
  - Ringkasan: telepon "jemput kami". Jemput / tidak
  - [ ] Opsi 1 — Jemput
  - [ ] Opsi 2 — tidak
  - Efek: Koita Success yang sedang berjalan bisa ketahuan di dalam mobil

- [ ] **C-D11** · Karya yang Dibeli Diam-diam
  - Pemicu: Male Route
  - Ringkasan: Yutaka membeli karya Chiasa secara anonim; Haruka mengetahuinya. Akui / sangkal
  - [ ] Opsi 1 — Akui
  - [ ] Opsi 2 — sangkal
  - Efek: nyaman_yutaka + bila diakui

- [ ] **C-D12** · Kuas yang Dipinjam
  - Pemicu: Chiasa host; Intim ≥ 50 dengan seorang heroine
  - Ringkasan: heroine meminjam kuas atau minta digambar. Gambar dia / ajak melukis bersama / tolak
  - [ ] Opsi 1 — Gambar dia
  - [ ] Opsi 2 — ajak melukis bersama
  - [ ] Opsi 3 — tolak
  - Efek: jalur yuri dengan heroine itu menguat

- [ ] **C-D13** · Mata yang Kering
  - Pemicu: framing_koita terpasang; fallout mulai terlihat publik
  - Ringkasan: Chiasa menyaksikan dari jauh: Koita dijauhi, dipertanyakan. Tetap tenang / berpura-pura sedih di depan orang / diam-diam merasa goyah
  - [ ] Opsi 1 — Tetap tenang
  - [ ] Opsi 2 — berpura-pura sedih di depan orang
  - [ ] Opsi 3 — diam-diam merasa goyah
  - Efek: tenang: nurani_chiasa −15 · pura-pura sedih: reputasi aman, tidak berubah · goyah diam-diam: nurani_chiasa +10, membuka C-D14 lebih cepat

- [ ] **C-D14** · Pengakuan Setengah
  - Pemicu: Trust Haruka atau yutaka_harap Sedang+; framing_koita terpasang
  - Ringkasan: Chiasa hampir mengaku pada satu orang, lalu membungkusnya sebagai "perlu dilakukan". Biarkan mereka tahu sebagian / tarik kembali ucapan / mengaku penuh
  - [ ] Opsi 1 — Biarkan mereka tahu sebagian
  - [ ] Opsi 2 — tarik kembali ucapan
  - [ ] Opsi 3 — mengaku penuh
  - Efek: mengaku penuh: nurani_chiasa +25, confidant jadi saksi yang bisa meruntuhkan framing atau bersekutu diam-diam; sebagian: confidant curiga tapi tidak yakin

- [ ] **C-D15** · Nyaris Ketahuan
  - Pemicu: framing_koita bertahan; bukti_digital mendekati ambang
  - Ringkasan: sesuatu nyaris membuka retakan dalam ceritanya. Tangani dengan tenang / dramatisir supaya dikasihani / biarkan saja
  - [ ] Opsi 1 — Tangani dengan tenang
  - [ ] Opsi 2 — dramatisir supaya dikasihani
  - [ ] Opsi 3 — biarkan saja
  - Efek: tenang: nurani_chiasa −10, orang sekitar makin tidak curiga karena reaksinya "wajar"; dramatisir berlebihan: dibaca Shiori sebagai kejanggalan

### Ending

- [ ] **E-CF-01** · Rumah Baru _(Romantis, host C)_
  - Syarat: yuri dengan heroine utama; deviasi cukup
  - Isi: hidup bersama heroine; reaksi keluarga Amamiya menentukan nada epilog

- [ ] **E-CF-02** · Diterima _(Koita, host C)_
  - Syarat: Koita Success; keluarga menerima
  - Isi: tabu yang direstui

- [ ] **E-CF-03** · Berpisah Baik-baik _(Neutral, host C)_
  - Syarat: Koita Success; keduanya mundur
  - Isi: kembali menjadi adik tiri

- [ ] **E-CF-04** · Dipisah Paksa _(Bad, host C)_
  - Syarat: Koita Success; keluarga memisahkan
  - Isi: salah satu meninggalkan rumah

- [ ] **E-CF-05** · Digantung Lagi _(Bad, host C)_
  - Syarat: Koita Success; Koita kembali menggantung
  - Isi: pemain merasakan pola Koita dari dalam

- [ ] **E-CF-06** · Bersama Yutaka _(Koita, host C)_
  - Syarat: Chiasa × Yutaka
  - Isi: hidup bersama Yutaka; lolos evaluasi hanya bila ada deviasi lain (bila tidak, E-SI-06)

- [ ] **E-CF-07** · Nama Pena yang Runtuh _(Bad, host C)_
  - Syarat: rahasia Shena terbongkar sebagai kebohongan
  - Isi: kontrak Mio diputus; pembaca marah

- [ ] **E-CF-08** · Gaya Baru Shena _(Romantis, host C)_
  - Syarat: pemain belajar menggambar sungguhan sampai layak
  - Isi: Shena kembali dengan gaya baru; Mio dan Haruka menjadi saksi

- [ ] **E-CF-09** · Rumah Amamiya Retak _(Bad, host C)_
  - Syarat: Koita Success atau kejahatan memecah keluarga
  - Isi: Daisuke dan Yoshie berpisah tempat; rumah sepi

- [ ] **E-CF-10** · Studio Sendiri _(Neutral, host C)_
  - Syarat: tanpa romansa
  - Isi: mandiri di studio kecil; lolos atau tidaknya bergantung deviasi yang dibuat dengan cara lain

- [ ] **E-CF-11** · Lingkaran yang Runtuh _(Bad, host C)_
  - Syarat: beberapa hubungan yuri sekaligus terbongkar
  - Isi: semua pergi bersamaan; lihat E-X-01

- [ ] **E-CF-12** · Korban yang Ia Ciptakan _(Khusus, host C)_
  - Syarat: jalur manipulasi pembalikan (§14); framing bertahan; nurani_chiasa < 70 sebelum M35
  - Isi: Chiasa tampil sebagai korban, Koita dicap pelaku dan hancur; tanpa romansa; tak bisa diputar balik dan bisa muncul lagi

- [ ] **E-CF-13** · Pengakuan yang Tidak Diminta _(Khusus, host C)_
  - Syarat: nurani_chiasa ≥ 70 sebelum M35; framing pernah terpasang lalu dicabut sendiri
  - Isi: ia mengaku sebelum siapa pun membuktikannya; reputasi Koita pulih meski kepercayaan di antara mereka tidak pernah utuh lagi; konsekuensi sosial padanya tetap ada tapi lebih ringan karena kooperatif

- [ ] **E-CH-01** · Rumah Kita Sendiri _(Romantis, host Y)_
  - Syarat: Yutaka mengejar Chiasa; curiga identitas rendah atau diterima
  - Isi: dua orang yang sama-sama kesepian membangun rumah sendiri

- [ ] **E-CH-02** · Diterima _(Koita, host Y)_
  - Syarat: Koita Success NPC; Daisuke dan Yoshie menerima
  - Isi: saudara tiri menjadi pasangan dengan restu keluarga

- [ ] **E-CH-03** · Berpisah Baik-baik _(Neutral, host Y)_
  - Syarat: Koita Success NPC; keduanya memilih berpisah
  - Isi: tetap keluarga, dengan bekas yang hangat

- [ ] **E-CH-04** · Dipisah Paksa _(Bad, host Y)_
  - Syarat: Koita Success NPC; keluarga menolak keras
  - Isi: Chiasa dipindahkan atau Koita pergi

- [ ] **E-CH-05** · Digantung Lagi _(Bad, host Y)_
  - Syarat: Koita Success NPC; Koita kembali ke pola lama
  - Isi: Chiasa menjadi korban terbaru pola Koita

- [ ] **E-CH-06** · Shena Saja _(Neutral, host Y)_
  - Syarat: tanpa romansa; Chiasa pindah dan fokus seni
  - Isi: karier ilustrasi berjalan; rumah ditinggalkan

- [ ] **E-CH-07** · Tersisih Dua Kali _(Bad, host Y)_
  - Syarat: Rute BL berhasil; Chiasa tidak didekati
  - Isi: patah, menjauh dari keduanya

- [ ] **E-CH-08** · Sekutu Paling Setia _(Khusus, host Y)_
  - Syarat: Rute BL; Yutaka jujur pada Chiasa sejak awal
  - Isi: Chiasa menjadi pendukung Yutaka × Koita di depan keluarga

- [ ] **E-CH-09** · Rumah yang Tidak Aman _(Broken, host Y)_
  - Syarat: pemain pelaku Force terhadapnya
  - Isi: tinggal serumah dengan Koita; Daisuke dan Yoshie kecewa; tanpa romansa dengan pelaku

- [ ] **E-CH-10** · Adik yang Kembali _(Neutral, host Y)_
  - Syarat: tidak ada rute romansa dengan Chiasa; keluarga utuh
  - Isi: ia tetap adik Koita dan sahabat Yutaka

- [ ] **E-CH-11** · Bukan Piala _(Bad, host Y)_
  - Syarat: Yutaka merebut Chiasa hanya untuk menyakiti Koita, lalu ketahuan
  - Isi: Chiasa menolak keduanya

## Kisaragi Yutaka

_19 event utama · 11 event dinamis · 15 ending_

### Event utama

- [ ] **Y01** · bulan M01a · Terbangun di Apartemen Mewah
  - Pemicu: pagi 7 April; prolog.
  - [ ] Pilihan A — periksa dompet dan ponsel
  - [ ] Pilihan B — periksa cermin
  - [ ] Pilihan C — langsung hubungi Koita
  - [ ] Pilihan D — menunggu notifikasi Sistem.
  - Efek: membentuk kesan_awal; A memberi tahu saldo.

- [ ] **Y02** · bulan M01a · Kunci yang Tidak Ada
  - Pemicu: kunjungan pertama ke rumah Amamiya.
  - [ ] Pilihan A — bunyikan bel dan sopan
  - [ ] Pilihan B — masuk seolah rumah sendiri
  - [ ] Pilihan C — mengabari dulu.
  - Efek: B memicu curiga Chiasa/Koita (Yutaka asli tidak punya kunci cadangan ).

- [ ] **Y03** · bulan M01a · Yuu-kun?
  - Pemicu: Nagisa memanggil dengan julukan masa kecil.
  - [ ] Pilihan A — jawab natural
  - [ ] Pilihan B — salah panggil
  - [ ] Pilihan C — pura-pura lupa.
  - Efek: curiga_nagisa naik/turun.

- [ ] **Y04** · bulan M04 · Kuliah Ekonomi: Ingatan yang Hilang
  - Pemicu: kuis dadakan.
  - [ ] Pilihan A — belajar semalaman
  - [ ] Pilihan B — menyontek
  - [ ] Pilihan C — jujur ke dosen
  - [ ] Pilihan D — minta bantuan Daichi.
  - Efek: IPK; B berisiko skorsing akademik ().

- [ ] **Y05** · bulan M05a · Turnamen Game: Skill yang Hilang
  - Pemicu: Nagisa menantang main game; Yutaka asli pro, pemain tidak.
  - [ ] Pilihan A — pura-pura mengalah
  - [ ] Pilihan B — kalah terang-terangan
  - [ ] Pilihan C — latihan dulu.
  - Efek: B memicu curiga ("Yutaka tidak pernah kalah").

- [ ] **Y06** · bulan M08 · Daichi Membocorkan
  - Pemicu: Daichi tahu sesuatu tentang Shiori/Moeka dan menawarkannya.
  - [ ] Pilihan A — bayar dengan makanan
  - [ ] Pilihan B — tolak
  - [ ] Pilihan C — tawar informasi lain.
  - Efek: intel; C membuat Daichi mulai mengorek rahasia pemain.

- [ ] **Y07** · bulan M09 · Natal: Apartemen Sepi
  - Pemicu: Natal; orang tua Kisaragi tidak menelepon.
  - [ ] Pilihan A — pergi ke rumah Amamiya
  - [ ] Pilihan B — mengundang heroine
  - [ ] Pilihan C — sendiri
  - [ ] Pilihan D — mengejar Koita
  - Efek: hub besar #3 untuk host.

- [ ] **Y08** · bulan M11 · Coklat dari Siapa
  - Pemicu: Valentine; Yutaka menerima coklat dari banyak orang.
  - [ ] Pilihan A — balas satu orang
  - [ ] Pilihan B — balas semua sama
  - [ ] Pilihan C — tolak semua
  - [ ] Pilihan D — memberi coklat pada Koita
  - Efek: menyalakan rantai BL atau rantai heroine.

- [ ] **Y09** · bulan M13 · Telepon Orang Tua Kisaragi
  - Pemicu: ayah menanyakan rencana setelah lulus.
  - [ ] Pilihan A — jawab sopan
  - [ ] Pilihan B — bantah
  - [ ] Pilihan C — menyebut Saionji.
  - Efek: hubungan_keluarga_kisaragi; C memberi tekanan ekstra.

- [ ] **Y10** · bulan M16 · Jam Tangan Hadiah
  - Pemicu: Yutaka menerima jam tangan dari Daisuke seperti tahun lalu.
  - [ ] Pilihan A — simpan
  - [ ] Pilihan B — pakai
  - [ ] Pilihan C — kembalikan.
  - Efek: Daisuke menilai sikap.

- [ ] **Y11** · bulan M17a · Yukata dan Chiasa
  - Pemicu: festival; Chiasa memakai yukata.
  - [ ] Pilihan A — pujian
  - [ ] Pilihan B — gunakan godaan Yutaka asli
  - [ ] Pilihan C — diam.
  - Efek: Chiasa menilai apakah "Yutaka" masih Yutaka.

- [ ] **Y12** · bulan M20 · Pameran Chiasa
  - Pemicu: pameran seni; Haruka mengenalkan Chiasa.
  - [ ] Pilihan A — belikan karya
  - [ ] Pilihan B — hadir saja
  - [ ] Pilihan C — kritik.
  - Efek: Chiasa membuka diri atau menjauh.

- [ ] **Y13** · bulan M21 · Daisuke dan Yoshie Pulang
  - Pemicu: Natal kedua; orang tua Amamiya pulang mendadak.
  - [ ] Pilihan A — makan malam bersama
  - [ ] Pilihan B — menghindar
  - [ ] Pilihan C — membuka pembicaraan serius.
  - Efek: menjadi gerbang Koita Success jika Chiasa NPC bersama Koita; atau menyetujui pemain.

- [ ] **Y14** · bulan M23 · Hari Bentrok: Pernyataan Yutaka
  - Pemicu: hari pengakuan.
  - [ ] Pilihan A — mengaku pada Chiasa
  - [ ] Pilihan B — mengaku pada Koita
  - [ ] Pilihan C — mengaku pada heroine
  - [ ] Pilihan D — tidak mengaku.
  - Efek: hub besar #8.

- [ ] **Y15** · bulan M26 · Jarak dari Rumah
  - Pemicu: perjalanan; Yutaka merasa jauh dari keluarga Kisaragi.
  - [ ] Pilihan A — bicara dengan Daisuke
  - [ ] Pilihan B — menelepon ibu
  - [ ] Pilihan C — diam.
  - Efek: ending Yutaka.

- [ ] **Y16** · bulan M29a · Kembang Api dan Chiasa
  - [ ] Pilihan A — mengaku
  - [ ] Pilihan B — bergandengan
  - [ ] Pilihan C — menjaga jarak.
  - Efek: Chiasa × Yutaka (NPC) berjalan.

- [ ] **Y17** · bulan M31 · Pilihan Karier
  - [ ] Pilihan A — perusahaan keluarga
  - [ ] Pilihan B — kerja di luar
  - [ ] Pilihan C — magang luar negeri.
  - Efek: keluarga Kisaragi bereaksi.

- [ ] **Y18** · bulan M32 · Pameran Tunggal Chiasa
  - [ ] Pilihan A — hadir
  - [ ] Pilihan B — absen
  - [ ] Pilihan C — membawa seseorang.
  - Efek: hubungan Yutaka–Chiasa.

- [ ] **Y19** · bulan M35 · Jawaban
  - Efek: ending Yutaka (lihat Kisaragi_Yutaka.md bagian 11).

### Event dinamis

- [ ] **Y-D01** · Notifikasi Saldo
  - Pemicu: tanggal uang saku
  - Ringkasan: Sistem berkomentar soal uang. Belanja / simpan / beri pada seseorang
  - [ ] Opsi 1 — Belanja
  - [ ] Opsi 2 — simpan
  - [ ] Opsi 3 — beri pada seseorang
  - Efek: arah pemakaian uang

- [ ] **Y-D02** · Teman Game yang Heran
  - Pemicu: Male Route
  - Ringkasan: teman online Yutaka asli: "kok mainmu beda?" Jujur sebagian / beri alasan / berhenti main
  - [ ] Opsi 1 — teman online Yutaka asli: "kok mainmu beda?" Jujur sebagian
  - [ ] Opsi 2 — beri alasan
  - [ ] Opsi 3 — berhenti main
  - Efek: curiga_identitas menyebar lewat dunia online

- [ ] **Y-D03** · Ayah di Lobi
  - Pemicu: keluarga_kisaragi < 40
  - Ringkasan: ayah Kisaragi datang mendadak ke apartemen. Sambut / hindari / ajak bicara serius
  - [ ] Opsi 1 — Sambut
  - [ ] Opsi 2 — hindari
  - [ ] Opsi 3 — ajak bicara serius
  - Efek: keluarga_kisaragi ±; Y17 bergeser

- [ ] **Y-D04** · Daichi Menginap
  - Pemicu: kenal Daichi
  - Ringkasan: Daichi menginap dan melihat catatan pemain tentang heroine. Jelaskan / sembunyikan / sogok
  - [ ] Opsi 1 — Jelaskan
  - [ ] Opsi 2 — sembunyikan
  - [ ] Opsi 3 — sogok
  - Efek: daichi_tahu +

- [ ] **Y-D05** · Jam dari Daisuke
  - Pemicu: M16
  - Ringkasan: "Masih ingat jam yang tahun lalu?" Jawab yakin / akui lupa / alihkan
  - [ ] Opsi 1 — "Masih ingat jam yang tahun lalu?" Jawab yakin
  - [ ] Opsi 2 — akui lupa
  - [ ] Opsi 3 — alihkan
  - Efek: curiga_identitas[[daisuke] ±

- [ ] **Y-D06** · Lidah yang Lepas di Kafe Bar
  - Pemicu: Jumat malam saat kerja
  - Ringkasan: Hayase atau Tojo mabuk membocorkan rencana. Dengarkan / rekam / antar pulang
  - [ ] Opsi 1 — Dengarkan
  - [ ] Opsi 2 — rekam
  - [ ] Opsi 3 — antar pulang
  - Efek: intel untuk rute Miyuki atau Shiori

- [ ] **Y-D07** · Nagisa Main Sampai Pagi
  - Pemicu: Aff Nagisa Sedang
  - Ringkasan: Nagisa main game di apartemen sampai subuh. Biarkan tidur di sofa / antar pulang / suruh pulang
  - [ ] Opsi 1 — Biarkan tidur di sofa
  - [ ] Opsi 2 — antar pulang
  - [ ] Opsi 3 — suruh pulang
  - Efek: rumor; kelekatan Nagisa

- [ ] **Y-D08** · Pesan dari Ibu
  - Pemicu: keluarga_kisaragi ≥ 40
  - Ringkasan: ibu Kisaragi mengirim pesan hangat yang jarang terjadi. Balas hangat / formal / abaikan
  - [ ] Opsi 1 — Balas hangat
  - [ ] Opsi 2 — formal
  - [ ] Opsi 3 — abaikan
  - Efek: pintu kecil ke keluarga yang dingin

- [ ] **Y-D09** · Koita di Depan Pintu
  - Pemicu: Koita bertengkar atau ditinggal heroine
  - Ringkasan: Koita datang jam 01:00. Biarkan menginap / dengarkan lalu antar pulang / tolak
  - [ ] Opsi 1 — Biarkan menginap
  - [ ] Opsi 2 — dengarkan lalu antar pulang
  - [ ] Opsi 3 — tolak
  - Efek: benih BL atau persahabatan

- [ ] **Y-D10** · Menunggu di Stasiun
  - Pemicu: Female Route; yutaka_harap ≥ 50
  - Ringkasan: Yutaka NPC "kebetulan" menunggu Chiasa sepulang kelas malam. Jalan bersama / terima tumpangan / tolak
  - [ ] Opsi 1 — Jalan bersama
  - [ ] Opsi 2 — terima tumpangan
  - [ ] Opsi 3 — tolak
  - Efek: yutaka_harap +

- [ ] **Y-D11** · Pengakuan Jumat Malam
  - Pemicu: Female Route; yutaka_harap ≥ 70
  - Ringkasan: Yutaka mabuk dan mengaku di kafe bar. Jawab sekarang / tunda / anggap candaan
  - [ ] Opsi 1 — Jawab sekarang
  - [ ] Opsi 2 — tunda
  - [ ] Opsi 3 — anggap candaan
  - Efek: E-YU-01 atau E-YU-03 menguat

### Ending

- [ ] **E-YH-01** · Pewaris yang Berbeda _(Neutral, host Y)_
  - Syarat: Y17-A; keluarga berdamai
  - Isi: mengambil perusahaan keluarga dengan cara sendiri, tidak sedingin orang tuanya

- [ ] **E-YH-02** · Bekerja di Luar _(Neutral, host Y)_
  - Syarat: Y17-B
  - Isi: lepas dari keluarga Kisaragi; hidup dengan gaji sendiri

- [ ] **E-YH-03** · Keluarga Pilihan _(Romantis, host Y)_
  - Syarat: hubungan dengan keluarga Amamiya tinggi; tanpa kejahatan
  - Isi: Daisuke dan Yoshie memperlakukannya sebagai anak sendiri

- [ ] **E-YH-04** · Dicoret _(Bad, host Y)_
  - Syarat: membangkang keluarga berulang atau skandal besar
  - Isi: uang saku berhenti; apartemen dilepas; mulai dari nol

- [ ] **E-YH-05** · Ketahuan Bukan Yutaka _(Khusus, host Y)_
  - Syarat: minimal dua orang dekat yakin ia bukan Yutaka
  - Isi: diterima sebagai "Yutaka yang baru", atau dijauhi

- [ ] **E-YH-06** · Pergi Jauh _(Neutral, host Y)_
  - Syarat: Y17-C magang luar negeri
  - Isi: meninggalkan kota; quest Sistem tetap berjalan dari jauh

- [ ] **E-YH-07** · Informan yang Menagih _(Bad, host Y)_
  - Syarat: daichi_status penagih
  - Isi: Daichi memeras pemain dengan semua yang ia tahu

- [ ] **E-YU-01** · Bersama Chiasa _(Romantis, host C)_
  - Syarat: Yutaka mengaku; Chiasa menerima
  - Isi: aman hanya bila ada deviasi lain (bila tidak, E-SI-06)

- [ ] **E-YU-02** · Mundur ke Luar Negeri _(Neutral, host C)_
  - Syarat: Yutaka mundur demi Koita
  - Isi: magang ke luar negeri untuk melupakan

- [ ] **E-YU-03** · Retak dan Menutup Diri _(Bad, host C)_
  - Syarat: Chiasa menolak lalu menggantung
  - Isi: apartemen menjadi satu-satunya tempatnya

- [ ] **E-YU-04** · Sekutu Chiasa _(Khusus, host C)_
  - Syarat: Chiasa jujur padanya
  - Isi: Yutaka membantu Chiasa di rute heroine atau Koita Success

- [ ] **E-YU-05** · Tahu Dipakai _(Bad, host C)_
  - Syarat: Chiasa memperalat Yutaka dan ia mengetahuinya
  - Isi: patah; memutus Chiasa dan Koita sekaligus

- [ ] **E-YU-06** · Membela Koita _(Neutral, host C)_
  - Syarat: Yutaka melihat Chiasa menyakiti Koita
  - Isi: berpihak pada Koita; menjadi lawan sosial Chiasa

- [ ] **E-YU-07** · Pewaris Kisaragi _(Bad, host C)_
  - Syarat: keluarga menekan di M31; Chiasa tidak hadir
  - Isi: menjadi sedingin orang tuanya

- [ ] **E-YU-08** · Sahabat Lagi _(Neutral, host C)_
  - Syarat: Chiasa menolak dengan jujur dan konsisten
  - Isi: geng masa kecil tetap utuh

## Lintas Rute / Umum

### Event dinamis lintas rute (12)

- [ ] **X-D01** · Pertengkaran di Konbini
  - Pemicu: jeal[[moeka] Nagisa ≥ 60; stres_total Moeka ≥ 60; keduanya di konbini saat Dini Hari
  - Ringkasan: lerai / bela Moeka / bela Nagisa / pergi
  - [ ] Opsi 1 — lerai
  - [ ] Opsi 2 — bela Moeka
  - [ ] Opsi 3 — bela Nagisa
  - [ ] Opsi 4 — pergi
  - Efek: stres Moeka; tahap Nagisa; bila pemain tidak ada, Rina mendengar ceritanya besok

- [ ] **X-D02** · Calon Dokter Membaca Tanda
  - Pemicu: kelelahan Miyuki < 60; Moeka tahap ≥ 3
  - Ringkasan: Miyuki melihat tanda Moeka dan menelepon pemain. Datang bersama / minta Miyuki menangani / abaikan
  - [ ] Opsi 1 — Datang bersama
  - [ ] Opsi 2 — minta Miyuki menangani
  - [ ] Opsi 3 — abaikan
  - Efek: jendela Moeka bisa diambil lewat Miyuki

- [ ] **X-D03** · Dua Peringkat Teratas
  - Pemicu: Shiori dan Harumi sama-sama percaya pada pemain
  - Ringkasan: mereka bersekutu melawan Ogawa. Bergabung / biarkan / pecah belah
  - [ ] Opsi 1 — Bergabung
  - [ ] Opsi 2 — biarkan
  - [ ] Opsi 3 — pecah belah
  - Efek: bukti_ogawa melonjak; E-HA-07 dan E-SH-10 menguat

- [ ] **X-D04** · Dua Coklat di Satu Loker
  - Pemicu: Valentine; dua heroine dengan Aff ≥ 55
  - Ringkasan: dua coklat di loker pemain; keduanya datang di waktu yang sama. Jujur pada keduanya / sembunyikan satu / kabur
  - [ ] Opsi 1 — Jujur pada keduanya
  - [ ] Opsi 2 — sembunyikan satu
  - [ ] Opsi 3 — kabur
  - Efek: Jealousy keduanya; rahasia baru

- [ ] **X-D05** · Rumah Amamiya Penuh
  - Pemicu: Natal; tiga heroine atau lebih diundang
  - Ringkasan: semua datang ke rumah Amamiya. Atur tempat duduk / bagi perhatian / keluar sebentar
  - [ ] Opsi 1 — Atur tempat duduk
  - [ ] Opsi 2 — bagi perhatian
  - [ ] Opsi 3 — keluar sebentar
  - Efek: panggung kecil Hari Pengakuan; Koita mengamati

- [ ] **X-D06** · Wawancara Mei
  - Pemicu: Mei menulis tentang pemain
  - Ringkasan: Mei mewawancarai heroine satu per satu. Hentikan Mei / biarkan / bayar Mei
  - [ ] Opsi 1 — Hentikan Mei
  - [ ] Opsi 2 — biarkan
  - [ ] Opsi 3 — bayar Mei
  - Efek: jawaban tiap heroine mengikuti keadaannya; reputasi

- [ ] **X-D07** · Rapat Rahasia Koita
  - Pemicu: koita_sadar ≥ 75
  - Ringkasan: Koita mengumpulkan heroine untuk "membicarakan" pemain. Hadir tanpa diundang / kirim orang / biarkan
  - [ ] Opsi 1 — Hadir tanpa diundang
  - [ ] Opsi 2 — kirim orang
  - [ ] Opsi 3 — biarkan
  - Efek: manuver balik terbesar; E-KO-10 menguat

- [ ] **X-D08** · Rina dan Sena Bertukar Cerita
  - Pemicu: rina_curiga dan sena_curiga ≥ 50
  - Ringkasan: dua sahabat membandingkan catatan tentang pemain. Temui mereka / hindari / jujur
  - [ ] Opsi 1 — Temui mereka
  - [ ] Opsi 2 — hindari
  - [ ] Opsi 3 — jujur
  - Efek: kecurigaan gabungan; dua lingkaran sosial sekaligus

- [ ] **X-D09** · Dua Penjaga
  - Pemicu: haruto_curiga ≥ 50; Kuroiwa curiga
  - Ringkasan: Haruto dan Kuroiwa bertemu dan berbagi informasi; pemain baru tahu belakangan
  - Efek: peringatan dari dua sisi; bila ada Force, E-FO-06 lebih mungkin

- [ ] **X-D10** · Malam Dua Krisis
  - Pemicu: Mo25 dan N23 jatuh di malam yang sama
  - Ringkasan: pemain hanya bisa berada di satu tempat. Datang ke Moeka / ke Nagisa / kirim orang ke salah satunya
  - [ ] Opsi 1 — Datang ke Moeka
  - [ ] Opsi 2 — ke Nagisa
  - [ ] Opsi 3 — kirim orang ke salah satunya
  - Efek: ujian terberat untuk "kirim orang lain" dan mode ponsel

- [ ] **X-D11** · Grup Belajar SMA Hidup Lagi
  - Pemicu: Koita membuka grup chat lama
  - Ringkasan: Koita, Yutaka, Nagisa, Miyuki, Harumi kembali bercakap. Ikut / diam / keluar grup
  - [ ] Opsi 1 — Ikut
  - [ ] Opsi 2 — diam
  - [ ] Opsi 3 — keluar grup
  - Efek: rahasia lama terangkat; benih E-NA-09 dan E-X-11

- [ ] **X-D12** · Salah Kirim
  - Pemicu: pemain Sangat Lelah; sedang chat dengan dua orang
  - Ringkasan: pesan untuk satu orang terkirim ke orang lain. Tarik pesan (notifikasi sudah terbaca) / jelaskan / pura-pura disengaja
  - [ ] Opsi 1 — Tarik pesan (notifikasi sudah terbaca)
  - [ ] Opsi 2 — jelaskan
  - [ ] Opsi 3 — pura-pura disengaja
  - Efek: rahasia bocor; contoh kondisi tubuh yang melahirkan cabang baru

### Lintas Rute · Force & Kriminal (15)

- [ ] **E-FO-01** · Jeruji _(Bad, host Y/C)_
  - Syarat: laporan atau bukti kuat; investigasi tuntas
  - Isi: dipenjara; game berlanjut di Rute Jeruji; evaluasi tetap terjadi di sel

- [ ] **E-FO-02** · Dikeluarkan dan Hancur Sosial _(Bad, host Y/C)_
  - Syarat: bukti cukup untuk kampus, tidak cukup untuk penjara
  - Isi: dikeluarkan; reputasi hancur di semua lingkungan; Rute Luar Kampus

- [ ] **E-FO-03** · Lolos tapi Dihantui _(Khusus, host Y/C)_
  - Syarat: force_bersih[[korban] bertahan (§10); tidak pernah terbongkar
  - Isi: bebas dari hukum, tidak dari ingatan; korban tetap bisa mendapat Broken Ending

- [ ] **E-FO-04** · Mengaku dan Menjalani Proses _(Neutral, host Y/C)_
  - Syarat: pelaku mengaku
  - Isi: proses hukum; tidak ada pengampunan otomatis; korban menentukan jaraknya sendiri

- [ ] **E-FO-05** · Buron _(Bad, host Y/C)_
  - Syarat: pelaku lari
  - Isi: hidup bersembunyi di kota lain; quest gagal; Sistem menghukum pembangkangan

- [ ] **E-FO-06** · Kakak yang Tidak Menunggu Polisi _(Bad, host Y/C)_
  - Syarat: Haruto, Kuroiwa, atau kerabat lain tahu lebih dulu
  - Isi: kerabat korban membalas sendiri; pemain cedera berat atau mati (E-SI-16); pembalas ikut ditangkap

- [ ] **E-FO-07** · Saksi yang Memeras _(Khusus, host Y/C)_
  - Syarat: saksi (Daichi atau Mei) menyimpan bukti
  - Isi: pemain diperas sampai akhir game

- [ ] **E-FO-08** · Kasus yang Dibuka Kembali _(Khusus, host Y/C)_
  - Syarat: bukti ditemukan belakangan
  - Isi: epilog: kasus dibuka setelah wisuda; hidup yang tampak selamat runtuh

- [ ] **E-FO-09** · Kejahatan Berantai _(Bad, host Y/C)_
  - Syarat: lebih dari satu kejahatan; satu membongkar yang lain
  - Isi: semua terbongkar bersamaan

- [ ] **E-FO-10** · Skorsing dan Catatan _(Neutral, host Y/C)_
  - Syarat: hanya kejahatan ringan–sedang
  - Isi: skorsing satu semester dan catatan polisi; hidup berjalan dengan bekas

- [ ] **E-FO-11** · Saksi di Ambang Pintu _(Bad, host Y/C)_
  - Syarat: Force disaksikan Koita; korban melapor sendiri, atau trust_koita sudah rendah sehingga Koita sendiri mencari bantuan
  - Isi: kasus terkuat; penjara hampir pasti; nasib Koita sendiri mengikuti trust_koita — ia bertindak sebagai saksi (E-KO-20) atau ikut dimintai kesaksian sambil membeku di dalam (E-KO-19)

- [ ] **E-FO-12** · Kurungan Tanpa Jeruji _(Khusus, host Y/C)_
  - Syarat: korban tidak melapor dan tetap terikat pada pemain lewat takut, ancaman, atau ketergantungan
  - Isi: dihitung Sistem sebagai lepas dari Koita; tidak pernah ditulis sebagai cinta; bisa retak kapan saja lewat sahabat, bukti, atau korban sendiri (E-FO-08)

- [ ] **E-FO-13** · Kebetulan yang Datang Tepat Waktu _(Bad, host Y/C)_
  - Syarat: plot armor membawa Koita sebelum terjadi
  - Isi: percobaan gagal; korban berlindung pada Koita; pemain menanggung percobaan itu: laporan, skorsing, rumor

- [ ] **E-FO-14** · Dua Orang yang Diam _(Khusus, host Y/C)_
  - Syarat: Koita menyaksikan tetapi diam karena takut, malu, atau diancam
  - Isi: pelaku bebas dari hukum, tetapi dua orang tahu; korban dan Koita sama-sama hancur dalam diam

- [ ] **E-FO-15** · Pembalikan yang Terbongkar _(Bad, host C)_
  - Syarat: jalur manipulasi pembalikan Chiasa (06_Chiasa.md §14); framing runtuh
  - Isi: fitnah terbongkar lewat bukti, saksi, atau Shiori/Hanabusa; Chiasa menanggung Force sekaligus fitnah dan obstruksi, konsekuensi lebih berat

### Lintas Rute · Sistem & Evaluasi (25)

- [ ] **E-HP-01** · Bersama Satu Orang _(Romantis, host Y/C)_
  - Syarat: satu hubungan romantis bertahan sampai M36
  - Isi: siapa pun orangnya: heroine, Koita, Chiasa atau Yutaka NPC, atau NPC sampingan

- [ ] **E-HP-02** · Bersama Beberapa Orang _(Khusus, host Y/C)_
  - Syarat: lebih dari satu hubungan bertahan, terbuka atau rahasia
  - Isi: lihat E-X-02 dan E-X-01

- [ ] **E-HP-03** · Tidak Dapat Siapa-Siapa _(Neutral, host Y/C)_
  - Syarat: pernah mengejar, tetapi tidak ada yang bertahan
  - Isi: pemain berakhir sendiri; cerita tidak menghukumnya karena itu

- [ ] **E-HP-04** · Ditinggalkan Semua _(Bad, host Y/C)_
  - Syarat: semua orang yang dikejar pergi karena kebohongan atau luka
  - Isi: sendiri, dan semua orang tahu kenapa

- [ ] **E-HP-05** · Tidak Pernah Mengejar Siapa Pun _(Neutral, host Y/C)_
  - Syarat: tidak pernah memulai romansa
  - Isi: tiga tahun tanpa romansa; deviasi hanya datang dari cara lain

- [ ] **E-HP-06** · Cinta yang Datang Terlambat _(Khusus, host Y/C)_
  - Syarat: seseorang mengaku di M35 atau M36 setelah pemain menyerah
  - Isi: jawaban pemain menjadi slide terakhir

- [ ] **E-HP-07** · Patah Hati yang Diterima _(Neutral, host Y/C)_
  - Syarat: ditolak dengan jujur, dan pemain menerimanya
  - Isi: sendiri, tetapi damai

- [ ] **E-SI-01** · Kontrak Selesai _(Romantis, host Y/C)_
  - Syarat: deviasi cukup
  - Isi: Sistem berpamitan dengan satu ejekan terakhir; pemain hidup

- [ ] **E-SI-02** · Nyaris _(Khusus, host Y/C)_
  - Syarat: deviasi tipis di atas ambang
  - Isi: "Nyaris." Sistem tidak pernah bicara lagi

- [ ] **E-SI-03** · Penonton Terakhir _(Romantis, host Y/C)_
  - Syarat: deviasi tinggi; rapport_sistem tinggi
  - Isi: Sistem membacakan semua yang ia hitung, lalu pamit seperti teman

- [ ] **E-SI-04** · Kontrak Baru _(Khusus, host Y/C)_
  - Syarat: deviasi tinggi; sikap penyelidik
  - Isi: Sistem menawarkan kontrak baru (kait New Game Plus)

- [ ] **E-SI-05** · Gagal di Bawah Sakura _(Bad, host Y/C)_
  - Syarat: deviasi kurang; pemain di kampus
  - Isi: pemain mati di hari wisuda, di bawah sakura

- [ ] **E-SI-06** · Cinta yang Tidak Dihitung _(Bad, host C)_
  - Syarat: Chiasa × Yutaka saja
  - Isi: "Ini bukan penyimpangan. Ini pelarian."

- [ ] **E-SI-07** · Tubuh Pinjaman Menyerah _(Bad, host Y/C)_
  - Syarat: mati karena tubuh sebelum wisuda
  - Isi: tubuh host berhenti lebih dulu daripada kontraknya

- [ ] **E-SI-08** · Pembangkang _(Bad, host Y/C)_
  - Syarat: hukuman kritis karena pembangkangan sengaja
  - Isi: Sistem menagih lebih awal

- [ ] **E-SI-09** · Lolos di Balik Jeruji _(Khusus, host Y/C)_
  - Syarat: lolos; sedang dipenjara
  - Isi: "Selamat, kau hidup. Di sini."

- [ ] **E-SI-10** · Gagal di Balik Jeruji _(Bad, host Y/C)_
  - Syarat: gagal; sedang dipenjara
  - Isi: mati di sel pada jam wisuda

- [ ] **E-SI-11** · Hidup Tanpa Nama _(Khusus, host Y/C)_
  - Syarat: lolos; reputasi hancur di semua lingkungan
  - Isi: hidup, tetapi tak ada yang menunggu

- [ ] **E-SI-12** · Figuran yang Baik _(Romantis, host Y/C)_
  - Syarat: pemain berhenti memanipulasi dan membantu heroine pulih; mereka lepas dari Koita dan berdiri sendiri
  - Isi: lolos lewat kebaikan; deviasi lahir dari orang-orang yang bebas

- [ ] **E-SI-13** · Kebaikan yang Tidak Dihitung _(Bad, host Y/C)_
  - Syarat: pemain berbuat baik tetapi deviasi kurang
  - Isi: mati, tetapi dunia yang ditinggalkan lebih baik

- [ ] **E-SI-14** · Jauh dari Panggung _(Khusus, host Y/C)_
  - Syarat: pemain di kota atau negara lain saat wisuda
  - Isi: lolos atau gagal tanpa menyaksikan wisuda

- [ ] **E-SI-15** · Pengakuan yang Tidak Dipercaya _(Khusus, host Y/C)_
  - Syarat: rahasia Sistem dibuka luas; dianggap gila
  - Isi: evaluasi terjadi di ruang rawat; hasil mengikuti deviasi

- [ ] **E-SI-16** · Tagihan dari Orang Lain _(Bad, host Y/C)_
  - Syarat: dibunuh atau dilukai fatal oleh NPC
  - Isi: kematian karena tindakan orang yang pernah disakiti

- [ ] **E-SI-17** · Penipu yang Tertipu _(Bad, host Y/C)_
  - Syarat: hasil yang dinilai hanyalah sandiwara
  - Isi: Sistem harian tertipu sampai akhir; evaluasi tidak

- [ ] **E-SI-18** · Celah yang Tidak Pernah Dicatat _(Khusus, host Y/C)_
  - Syarat: koita_bebas_naskah benar — nyaris mustahil, lihat bagian 11
  - Isi: pemain lolos tanpa NTR dan tanpa mati, lewat satu celah dalam kontrak yang tidak pernah diantisipasi siapa pun, termasuk Sistem sendiri

### Lintas Rute · NPC Sampingan (27)

- [ ] **E-NPC-01** · Dua Jas Putih _(Romantis, host Y/C)_
  - Syarat: romansa tulus dengan Sena; Miyuki tidak disakiti
  - Isi: dua calon dokter yang saling menjaga jam tidur

- [ ] **E-NPC-02** · Sahabat yang Memilih Sisi _(Bad, host Y/C)_
  - Syarat: pemain menyakiti Miyuki sambil mendekati Sena
  - Isi: Sena memilih Miyuki dan menutup pintu

- [ ] **E-NPC-03** · Thrift Hari Minggu _(Romantis, host Y/C)_
  - Syarat: romansa tulus dengan Rina; Moeka selamat
  - Isi: Minggu pagi di toko bekas, bertiga dengan Moeka

- [ ] **E-NPC-04** · Rina Tidak Memaafkan _(Bad, host Y/C)_
  - Syarat: Moeka meninggal atau disakiti pemain
  - Isi: Rina menjadi saksi paling keras terhadap pemain

- [ ] **E-NPC-05** · Studio Berdua _(Romantis, host Y/C)_
  - Syarat: romansa dengan Haruka
  - Isi: dua meja gambar dalam satu studio

- [ ] **E-NPC-06** · Rahasia yang Dititipkan _(Neutral, host C)_
  - Syarat: Haruka tahu rahasia Shena dan menjaganya
  - Isi: persahabatan yang lebih kuat dari rahasia

- [ ] **E-NPC-07** · Pasal yang Membela _(Romantis, host Y/C)_
  - Syarat: romansa atau aliansi dengan Ayane
  - Isi: Ayane membela pemain di kampus dan Moeka di sidang banding

- [ ] **E-NPC-08** · Rapat Terakhir BEM _(Bad, host Y/C)_
  - Syarat: Ayane mengetahui manipulasi pemain
  - Isi: ia mengecam pemain di depan umum

- [ ] **E-NPC-09** · Redaksi Berdua _(Romantis, host Y/C)_
  - Syarat: romansa dengan Mei; pemain jujur padanya
  - Isi: akun gosip berhenti menulis tentang pemain

- [ ] **E-NPC-10** · Headline Terakhir _(Bad, host Y/C)_
  - Syarat: Mei dipakai lalu dibuang
  - Isi: Mei menerbitkan semua yang ia tahu

- [ ] **E-NPC-11** · Naskah dan Penyuntingnya _(Romantis, host C)_
  - Syarat: romansa dengan Mio
  - Isi: hubungan kerja menjadi lebih dari itu

- [ ] **E-NPC-12** · Kontrak Diputus _(Bad, host C)_
  - Syarat: hubungan dengan Mio rusak
  - Isi: Mio memutus kontrak Shena

- [ ] **E-NPC-13** · Kakak yang Dipilih _(Romantis, host Y)_
  - Syarat: romansa dengan Haruto
  - Isi: keluarga Sakurajima terkejut; Nagisa bereaksi sesuai tahapnya

- [ ] **E-NPC-14** · Restu Sakurajima _(Neutral, host Y/C)_
  - Syarat: Haruto menjadi sekutu
  - Isi: keluarga Nagisa membuka pintu untuk pemain

- [ ] **E-NPC-15** · Esai untuk Satu Orang _(Romantis, host Y)_
  - Syarat: romansa dengan Matsuda
  - Isi: Matsuda menulis esai baru, kali ini tentang tokoh yang memilih

- [ ] **E-NPC-16** · Saksi yang Menulis _(Bad, host Y/C)_
  - Syarat: Matsuda membongkar manipulasi pemain
  - Isi: esai yang membongkar pemain dibaca seluruh fakultas

- [ ] **E-NPC-17** · Informan yang Setia _(Romantis, host Y)_
  - Syarat: romansa dengan Daichi
  - Isi: informan yang berhenti menjual pemain

- [ ] **E-NPC-18** · Maket Kedua _(Romantis, host Y)_
  - Syarat: romansa dengan Yuuto
  - Isi: Yuuto berhenti mengejar Nagisa

- [ ] **E-NPC-19** · Pewaris yang Membangkang _(Romantis, host Y)_
  - Syarat: romansa dengan Tojo
  - Isi: rencana pertunangan Tojo–Saionji runtuh

- [ ] **E-NPC-20** · Skandal Omiai _(Khusus, host Y)_
  - Syarat: romansa dengan Takeru
  - Isi: omiai Miyuki runtuh dalam skandal

- [ ] **E-NPC-21** · Kafe Pagi _(Neutral, host Y/C)_
  - Syarat: kerja tetap di Kafe Komorebi
  - Isi: Ito menjadi mentor; tubuh pemain paling sehat di semua ending

- [ ] **E-NPC-22** · Batas Profesional _(Neutral, host Y/C)_
  - Syarat: pemain mengejar Sato secara romantis
  - Isi: Sato menolak dan memindahkan konseling ke rekan lain

- [ ] **E-NPC-23** · Konseling Host _(Neutral, host Y/C)_
  - Syarat: konseling rutin dengan Sato
  - Isi: stres_host turun; rahasia Sistem dicatat sebagai "keyakinan pasien"

- [ ] **E-NPC-24** · Kepercayaan Kuroiwa _(Neutral, host Y/C)_
  - Syarat: Kuroiwa mempercayai pemain
  - Isi: peringatan dini setiap kali Shiori bergerak

- [ ] **E-NPC-25** · Saksi yang Dipercaya _(Neutral, host Y/C)_
  - Syarat: pemain membantu Hanabusa
  - Isi: kesaksian pemain menjatuhkan Ogawa atau Kuga

- [ ] **E-NPC-26** · Penyusup _(Khusus, host Y/C)_
  - Syarat: penyamaran berhasil; bukti cukup
  - Isi: Ogawa atau Kuga jatuh dari dalam

- [ ] **E-NPC-27** · Penyusup yang Tertelan _(Bad, host Y/C)_
  - Syarat: penyamaran terlalu lama
  - Isi: pemain ikut terseret kejahatan mereka

### Lintas Rute · Interlock Antar Rute (14)

- [ ] **E-X-01** · Harem yang Runtuh _(Bad, host Y/C)_
  - Syarat: beberapa hubungan rahasia terbongkar sekaligus di M23 atau M35
  - Isi: semua pergi di hari yang sama

- [ ] **E-X-02** · Meja Panjang _(Romantis, host Y/C)_
  - Syarat: hubungan terbuka yang disepakati semua pihak
  - Isi: makan malam panjang yang canggung, tapi jujur

- [ ] **E-X-03** · Domino Shiori _(Bad, host Y/C)_
  - Syarat: Shiori tahap 5 dengan daftar_kebohongan panjang
  - Isi: semua rahasia terbuka dan setiap rute ikut runtuh

- [ ] **E-X-04** · Musim Dingin Tanpa Moeka _(Bad, host Y/C)_
  - Syarat: E-MO-04
  - Isi: semua epilog berubah menjadi versi duka

- [ ] **E-X-05** · Kursi Kosong di Wisuda _(Khusus, host Y/C)_
  - Syarat: semua heroine lepas dari Koita
  - Isi: Koita sendirian di wisuda; deviasi sangat tinggi

- [ ] **E-X-06** · Semua Orang Bebas _(Romantis, host Y/C)_
  - Syarat: semua heroine pulih dan mandiri; tidak ada yang bersama Koita atau pemain
  - Isi: lingkaran yang bubar dengan sehat (sering bersama E-SI-12)

- [ ] **E-X-07** · Melawan Naskah Bersama _(Khusus, host Y/C)_
  - Syarat: E-KO-13 dan persahabatan atau Rute BL
  - Isi: Koita dan pemain sama-sama sadar naskah dan melawannya

- [ ] **E-X-08** · Pengakuan di Depan Semua _(Khusus, host Y/C)_
  - Syarat: pemain membuka Sistem kepada seluruh lingkaran di M35
  - Isi: setiap orang bereaksi sesuai sejarahnya dengan pemain

- [ ] **E-X-09** · Dua Tragedi _(Bad, host Y/C)_
  - Syarat: dua rute distorsi berakhir Bad dan saling memicu
  - Isi: dua kehilangan dalam satu musim

- [ ] **E-X-10** · Kota yang Tahu Semuanya _(Bad, host Y/C)_
  - Syarat: Mei menerbitkan semuanya
  - Isi: reputasi semua orang yang terlibat hancur

- [ ] **E-X-11** · Pesta di Rumah Amamiya _(Romantis, host Y/C)_
  - Syarat: semua pulih; Koita memilih dengan tulus; pemain bersama seseorang; geng masa kecil utuh
  - Isi: akhir paling bahagia, tetapi bukan True Ending

- [ ] **E-X-12** · Dua Ratu _(Bad, host Y/C)_
  - Syarat: Shiori Rute Revenge dan Nagisa Rute Yandere sama-sama menargetkan pemain
  - Isi: dua orang yang tadinya tidak akrab bersekutu melawan pemain

- [ ] **E-X-13** · Tubuh yang Dibayar _(Khusus, host Y/C)_
  - Syarat: pemain menyelamatkan minimal tiga heroine dari rute distorsi sambil terus memaksa tubuh
  - Isi: semua selamat, tubuh pemain yang membayar (dekat E-SI-07)

- [ ] **E-X-14** · Dalang yang Tak Pernah Dicurigai _(Khusus, host Y/C)_
  - Syarat: force_bersih[[x] bertahan untuk setiap korban Force; NTR sempurna tercapai (07_Koita_dan_BL.md §14, 09_Force_dan_Kriminal.md §10)
  - Isi: tidak ada yang pernah tahu apa yang sebenarnya terjadi; pemain lolos evaluasi dengan deviasi tertinggi yang mungkin, dan dunia tidak pernah mengejarnya. Sistem NTR tetap mencatat semuanya diam-diam
