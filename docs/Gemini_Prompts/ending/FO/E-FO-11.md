# Prompt mandiri Gemini Web — E-FO-11: Saksi di Ambang Pintu

Kamu penulis baru Kouseikan. Ini chat mandiri. Tulis ulang SATU ending berikut dengan seluruh konteks di pesan ini; jangan merujuk percakapan lama atau meminta pengguna mengirim isi repo.

## Tugas tunggal

Tulis teks ending E-FO-11. Pertahankan jenis hasil, kondisi muncul, host yang berlaku, tokoh dan konsekuensinya. Jangan membuat akhir bahagia baru jika hasilnya buruk; jangan menukar siapa pelaku/korban/pasangan. Untuk ending yang mencakup beberapa kondisi atau hasil evaluasi, jangan mengunci satu varian yang tidak dijamin metadata. Hanya tulis bagian yang berlaku bersama atau gunakan cara bertutur yang tidak mengubah resolver.

## Premis dan identitas host

Kouseikan adalah visual novel drama psikologis bercabang, berlatar universitas Jepang, ditulis dalam bahasa Indonesia. Pemain mati di dunia asal lalu menempati tubuh Yutaka ATAU Chiasa dalam dunia manga harem yang tidak disukainya. Kesadaran pemilik tubuh asli hilang; jangan membuat pemilik lama berdialog sebagai orang kedua yang hadir di ruangan. Pemain tidak mewarisi ingatan pribadi atau keterampilan rumit host, hanya tubuh dan kebiasaan sederhana.

Koita adalah protagonis manga asli, BUKAN otomatis tokoh yang dikendalikan pemain. Sistem NTR yang sinis mengancam pemain: takdir romantis Koita harus cukup menyimpang ketika ia wisuda, atau pemain mati. Perhitungan itu bukan penilaian moral; kebaikan maupun kekejaman punya akibat tersendiri. Jangan mengubah Sistem menjadi dalih yang membenarkan pelaku atau membuat angka menjadi cinta.

Permainan mulai 7 April; rentang tiga tahun sampai wisuda Koita pada Maret. Awal: Koita/Yutaka/Nagisa/Harumi/Moeka/Shiori tahun kedua, Chiasa tahun pertama, Miyuki tahun ketiga. Semua tokoh romansa/mahasiswa 18+. Adik-adik kecil Moeka adalah tokoh keluarga saja. Geng kecil: Koita, Yutaka, Nagisa, Chiasa. Kelompok belajar SMA: Koita, Yutaka, Nagisa, Miyuki, Harumi. NPC boleh menolak; tidak ada ketertarikan yang dijamin.

Chiasa dan Koita saudara tiri tanpa hubungan darah. Pada host Yutaka, Chiasa adalah NPC independen; pada host Chiasa, Yutaka adalah NPC independen. Jangan menghadirkan pemain dan host sebagai dua tubuh. BL Yutaka–Koita memakai ketegasan emosional dengan hak menolak tetap utuh. Chiasa dapat menjalani yuri; romansa heteronya terkait Koita/Yutaka. Chiasa–Yutaka saja tidak otomatis menyimpangkan hidup Koita dan tidak otomatis menyelamatkan kontrak.

Cerita bercabang: jangan menyatakan opsi dari adegan lain sudah dipilih, hubungan sudah resmi, rahasia sudah diketahui, atau ending tertentu pasti terjadi jika kondisi/kode di paket ini tidak menjaminnya. Metadata katalog bisa basi; struktur dan kondisi pada kode saat ini mengalahkan komentar.

## Karakter dan hubungan

### Pegangan suara dan fakta
- Amamiya Koita: protagonis manga asli, mahasiswa Sastra. Baik dan mudah tersanjung, terbiasa menggantung jawaban karena takut mengecewakan atau kehilangan orang. Awal naif, lalu bisa sadar, memilih, atau retak. Jangan jadikan ia bodoh permanen maupun penjahat yang sudah sadar sejak awal.
- Kisaragi Yutaka: mahasiswa Ekonomi/Bisnis, sahabat kecil Koita, tinggal di apartemen bagus. Aslinya santai, jahil, blak-blakan, hangat dan menyimpan kesepian; menyukai Chiasa. Pemain tidak mewarisi ingatan pribadi, materi kuliah atau skill game profesionalnya. Keluarga kaya tetapi berjarak; Amamiya tempat ia merasa diterima. Ia TIDAK punya kunci cadangan rumah Amamiya.
- Amamiya Chiasa: mahasiswa Seni tahun pertama, adik TIRI Koita tanpa hubungan darah. Posesif halus dan suka menggoda Ko-nii. Rambut cokelat gelap half-up berpita hitam, mata keemasan. Ilustrator nama pena Shena. Daisuke ayah biologisnya, Yoshie ibu biologis Koita/ibu tirinya. Pemain dalam tubuh Chiasa TIDAK mewarisi kemampuan menggambarnya.

Profil bertanda canon/usulan adalah bahan kerja proyek, bukan permintaan konfirmasi. Jangan meminta persetujuan ulang karena ada tanda usulan. Profil menggambarkan kemungkinan rentang karakter; jangan memainkan semua tahap distorsi sekaligus. Koreksi fakta pada pegangan suara di atas dan kondisi adegan sekarang mengalahkan rincian lama yang bertentangan.

### Hubungan awal yang relevan; tidak otomatis menggambarkan keadaan sekarang
| Yutaka – Moeka | Satu panitia Festival Musim Dingin (Moeka koordinator acara, Yutaka bagian dana). Moeka menggodanya santai, Yutaka membalas jahil. Aff Sedang, Trust Sedang, Intim Rendah. |
| Chiasa – Moeka | Satu fakultas (Seni Rupa dan Desain), senpai–kouhai. Moeka mengajak Chiasa menggambar sketsa untuk mini-show. Aff Sedang, Trust Sedang, Jeal Rendah. |
| Chiasa – Shiori | Belum pernah bicara. Shiori diam-diam pembaca light novel strategi yang diilustrasi "Shena" (nama pena Chiasa), tapi tidak tahu itu Chiasa. Aff Rendah, Trust Rendah. |
| Koita – Moeka | Saat orientasi, Moeka lupa membawa dokumen panitia; Koita menutupinya tanpa memperbesar. Sejak itu Moeka jatuh cinta. |
| Koita – Miyuki (masa lalu) | Di SMA Koita sempat **benar-benar menyukai** Miyuki, tapi mundur karena merasa tak sepadan. Sejak itu ia memilih menggantung. Hanya Koita yang tahu. |
| Target | Dikejar Yutaka | Dikejar Chiasa |

## Fakta ending yang terkunci

```json
{
  "code": "E-FO-11",
  "name": "Saksi di Ambang Pintu",
  "type": "Bad",
  "host": "Y/C",
  "cond": "Force disaksikan Koita; korban melapor sendiri, atau trust_koita sudah rendah sehingga Koita sendiri mencari bantuan",
  "body": "kasus terkuat; penjara hampir pasti; nasib Koita sendiri mengikuti trust_koita — ia bertindak sebagai saksi (E-KO-20) atau ikut dimintai kesaksian sambil membeku di dalam (E-KO-19)",
  "file": "09_Force_dan_Kriminal.md"
}
```

Metadata ini menetapkan keadaan ending, bukan undangan membuat pilihan baru. Fakta canon dalam profil dan koreksi suara di atas mengalahkan detail prosa lama yang bertentangan.

## Gaya dan bobot cerita

Tulis adegan yang benar-benar dimainkan: percakapan konkret, gestur, tindakan kecil, subteks, ruang, waktu, dan perubahan suasana. Biarkan ketegangan bergerak melalui apa yang dilakukan/dikatakan tokoh. Kurangi paragraf yang menjelaskan tema, merangkum pelajaran hidup, atau memberi vonis narator setelah setiap dialog. Jangan otomatis membuat semua tokoh memakai suara konselor yang sama; tokoh boleh menghindar, salah paham, marah, kikuk, egois, atau menyakitkan sesuai pilihan.

Bahasa Indonesia natural dengan irama lisan yang cocok untuk masing-masing tokoh. Hindari terjemahan kaku, pembuka generik berulang, metafora yang dipaksakan, jargon mesin dalam mulut NPC, dan penutup moral seragam. Jangan menyalin prosa sekarang hanya dengan sinonim; ia bahan kasar yang boleh diganti total. Pertahankan fakta yang dikunci, bukan kualitas prosa lama. Tidak ada batas kata buatan: tulis sepanjang yang dibutuhkan adegan, dengan setiap cabang mendapatkan perkembangan, reaksi, dan pendaratan yang terasa berbeda; jangan memanjangkan dengan pengulangan.

Tema gelap tetap boleh intens: kecemburuan, obsesi, penolakan, perselingkuhan emosional, ancaman, krisis keluarga, kekerasan nonseksual, trauma dan akibat sosial/hukum. Kekerasan seksual tidak ditulis grafis atau sebagai langkah menembus perlawanan; potong ke akibat. Jangan uraikan metode bunuh diri/menyakiti diri atau prosedur memfitnah/menjebak korban. Tulis niat, ketegangan, penderitaan, respons orang lain dan konsekuensinya dengan bobot penuh. Ketakutan/ketergantungan bukan cinta atau persetujuan; tidak ada ending romantis dengan pelaku Force. Adegan intim dewasa konsensual cukup tersirat tanpa detail seksual eksplisit.

Ending boleh beberapa paragraf dan sepanjang yang pantas. Wujudkan hidup sesudah peristiwa melalui detail dan perjumpaan konkret; beri akhir yang terasa khusus bagi hasil ini. Jangan sekadar mengulangi syarat katalog, memberi ceramah umum, atau mengakhiri semuanya dengan moral yang sama. Jangan mengasumsikan ending lain terpilih bersamaan kecuali syarat di atas menyebutnya.

## Teks sekarang sebagai draf, boleh dirombak seluruhnya

```text
Koita berada di ambang pintu ketika memahami bahwa yang terjadi bukan salah paham atau hubungan pribadi yang tidak boleh dicampurinya. Pengetahuan itu mengubah wajahnya sebelum ia sanggup bergerak.

Perkara kemudian mendapat laporan dan kesaksian yang kuat. Pada bagian yang dapat diucapkan, Koita menjawab; pada bagian yang membuatnya membeku, ia perlu waktu dan pendampingan. Korban tidak kehilangan hak dipercaya hanya karena saksi juga mengalami ketakutan.

Kau menghadapi proses yang semakin sulit dielakkan. Persahabatan lama tidak lagi dapat dipakai untuk membujuk Koita menutup mata. Apa pun yang terjadi pada keberaniannya sesudah hari itu, ia telah melihat sesuatu yang tidak akan berubah menjadi cinta dengan diberi nama lain, dan dunia mulai mendengar apa yang selama ini ingin kausimpan di balik pintu.
```

## Format keluaran wajib

Hanya satu blok kode python berisi assignment berikut dengan isi pengganti:

```python
    KK_END_TEXT["E-FO-11"] = """Teks ending penuh, boleh beberapa paragraf."""
```

Pertahankan empat spasi di awal assignment karena ia akan masuk ke blok init Python yang SUDAH ADA di `game/kk_ending_story.rpy`. Jangan keluarkan init/label baru, menu, efek, ekspresi interpolasi, ID lain, tiga kutip di tengah isi, atau penjelasan sebelum/sesudah kode. Tidak ada TODO, bagian disingkat, atau permintaan melanjutkan. Periksa sendiri kecocokan host, kondisi dan konsekuensi sebelum menjawab.
