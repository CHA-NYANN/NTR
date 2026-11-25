# Review Ciri Tulisan AI — Event Utama M01a–M20

Audit terhadap 108 adegan event utama (semua karakter, bulan M01a sampai M20) untuk dua hal:
1. Pola kalimat/struktur yang bikin tulisan "kentara AI banget".
2. Adegan yang terlalu tipis (dialog terlalu sedikit, terasa buru-buru) sehingga perlu diperpanjang.

Semua referensi `file:baris` di bawah ini sudah dicek langsung ke source `.rpy` saat ini (per 2026-11-24). Fokus perbaikan di bagian **Pola Lintas-Rute** dulu — dampaknya paling besar karena satu tic yang sama muncul di hampir semua rute.

## Pola Lintas-Rute (perbaiki ini dulu)

### 1. Akhir adegan/cabang selalu "menyimpulkan pelajaran" secara eksplisit
Pola paling sering muncul di seluruh batch. Hampir tiap cabang pilihan ditutup dengan satu kalimat narator yang menyatakan langsung makna/kesimpulan emosinya, bukan dibiarkan berhenti di aksi atau dialog.
- Paling parah di rute **Yutaka** — hampir tiap cabang di `kk_yutaka_route.rpy`/`kk_yutaka_host.rpy` (Y02, Y04, Y05, Y06, Y07, Y08, Y11) berakhir begini. Contoh Y04 `kk_yutaka_route.rpy:117-191`: "...kamu menyadari betapa tipis batas yang baru saja kamu lewati..."; Y08-D: "...tetapi satu hal tidak bisa ia sangkal malam ini, kotak cokelat darimu tetap ia bawa pulang."
- Chiasa: C04 (`kk_chiasa_host.rpy:363,393`), C03 (`kk_chiasa_route.rpy:259` — "Tubuh ini pinjaman, nama ini pinjaman...").
- Koita: K01 (`kk_koita_y1.rpy:41,69,88,105`) — kalimat capstone yang sama dipakai ulang 4x di 2 cabang host × 2 cabang pilihan.
- Miyuki: Mi11/Mi12/Mi13 (`kk_miyuki_daily.rpy:215/229, 408/426`) — narasi penutup selalu menyatakan tema secara langsung.
- Shiori: S13 (confrontation scene, `kk_shiori_route.rpy`) dan beberapa lainnya memberi "petuah" ala epigram ("Rumor selalu jauh lebih murah dibuat daripada diluruskan").

**Minta Antigravity**: ganti kalimat penutup bertipe "kesimpulan" dengan satu beat aksi/gestur/dialog konkret yang menyiratkan makna yang sama tanpa menyatakannya.

### 2. Cabang Host Chiasa vs Host Yutaka sering cuma "reskin" nama, bukan ditulis ulang
Temuan paling berdampak secara struktural — bukan cuma gaya kalimat. Ditemukan di:
- Koita K01 (`kk_koita_y1.rpy:15-41` vs `43-69`) — rangkaian paragraf nyaris identik, hanya ganti nama/kata ganti.
- Harumi H04, H08 (`kk_harumi_route.rpy:25-167`, `kk_harumi.rpy:173-258`) — beat, struktur kalimat, dan payoff sama persis.
- Miyuki Mi11–Mi13 (`kk_miyuki_daily.rpy`) — seluruh adegan diduplikasi hampir kata-per-kata antar cabang `kk_host`.
- Shiori S03, S06, S08, S10, S11, S12 — cabang antar host nyaris identik, termasuk deskripsi fisik Shiori yang diulang persis di tiap pembukaan.
- Moeka Mo05 (`kk_moeka.rpy:388,410`) — simile yang sama ditanam di kedua cabang.

**Minta Antigravity**: untuk tiap adegan yang bercabang host, tulis ulang salah satu cabang dengan interioritas/reaksi yang benar-benar berbeda (bukan cuma ganti nama), sekalian jadi kesempatan alami untuk memperpanjang kedua cabang.

### 3. Deskriptor/gerakan fisik "baku" per karakter, diulang berkali-kali
- **Miyuki**: "mata cokelat kemerahan [yang hangat]" muncul 25+ kali (`kk_miyuki_daily.rpy:215,229,404,422,445,472,502,520`; `kk_miyuki_route.rpy:107,128,356,390,424,455,489,523,559,572,590,612`; `kk_family.rpy:390,413`; `kk_vila.rpy:27,43`; `kk_scenes.rpy:195,211,223,246,281,517,531`; `kk_spring.rpy:759,775`). Gerakan "berkedip pelan lalu tersenyum" sebagai satu-satunya reaksi fisik muncul 15+ kali.
- **Shiori**: tag fisik "rambut putih keperakan, mata ungu ametis" diulang nyaris persis di tiap kemunculan (S03, S06, S08, S10, S11, S12).
- **Chiasa**: pembuka adegan berupa daftar 3-4 benda sensorik ditutup "serta X" — `grep -c "serta"`: `kk_chiasa_host.rpy`=4, `kk_chiasa_route.rpy`=5, `kk_art.rpy`=10 (kira-kira sekali per adegan). Tic ini nol di file Koita — menandakan beda "pass" penulisan antar karakter.
- **Nagisa**: pola "menyebut dua emosi lalu bilang keduanya 'bercampur'" untuk menutup beat emosional — `kk_life_events.rpy:124,138`; `kk_nagisa_early.rpy:497,512` (nyaris verbatim antar cabang host).

**Minta Antigravity**: variasikan deskriptor fisik dan reaksi per adegan (bukan satu "default slot" yang dipakai ulang), dan hindari pola "emosi A + emosi B = bercampur" sebagai penutup default.

### 4. Narasi langsung "menjelaskan" subteks alih-alih menunjukkannya
- Yutaka Y03 (`kk_yutaka_route.rpy:37`) — strategi tipu daya si pemain dijelaskan gamblang alih-alih dibiarkan muncul dari dialog saja.
- Moeka Mo06 (`kk_moeka.rpy:548`) — narator menyebutkan "checklist" tanda penipuan secara langsung ke pembaca.
- Moeka Mo09 (`kk_moeka.rpy:825-829`) — Moeka menarasikan mekanisme copingnya sendiri secara rapi.
- Shiori S05 — rasa berhak milik Tojo sepenuhnya dinarasikan/dijelaskan, bukan didramatisasi lewat perilakunya sendiri.
- Shiori S10 (`kk_shiori_route.rpy:26,41`) — monolog batin (italic) menyatakan langsung kesimpulan yang harusnya cukup disiratkan ke pembaca.

### 5. Daftar tiga serangkai yang dipaksakan (lebih jarang, tapi ada)
- Moeka Mo03 (`kk_moeka.rpy:29`) — tiga detail fisik ditumpuk persis sama di kedua cabang host.

## Adegan yang Perlu Diperpanjang (thin scenes)

Diukur lewat jumlah baris dialog per adegan (median seluruh batch ~124 baris; p10 ~83 baris). Yang di bawah ini dikonfirmasi tipis lewat pembacaan langsung, bukan cuma angka:

- **Y12** (`kk_yutaka_route.rpy:594`) — **paling parah**: cuma 1 baris narasi + 1 baris balasan per cabang (~8 baris dialog total), tanpa scene-setting maupun pertukaran dialog. Juga ada inkonsistensi sapaan "kamu"→"kau". Prioritas utama untuk diperpanjang.
- **C04** (`kk_chiasa_host.rpy:327`) — tiap cabang cuma 1 beat, tidak ada lanjutan/reaksi setelah pilihan dijatuhkan.
- **C05** (`kk_art.rpy:9`) — seluruh adegan cuma satu telepon dengan Miono, berhenti tepat di titik pilihan tanpa negosiasi/reaksi susulan.
- Rute **Yutaka** secara umum (Y03, Y04, Y05, Y06, Y08, Y11) ada di ujung bawah distribusi panjang adegan dibanding rute lain — kalau Antigravity mau memperpanjang dialog secara menyeluruh, mulai dari file `kk_yutaka_route.rpy` dan `kk_yutaka_host.rpy` lebih dulu.

Rute **Nagisa**, **Miyuki**, **Moeka**, dan **Shiori** tidak ada adegan yang tipis — panjangnya sudah wajar (beberapa malah panjang), jadi tidak perlu diperpanjang, fokus di perbaikan pola kalimat saja untuk rute-rute ini.

## Ringkasan per Rute

- **Chiasa**: tic "serta [daftar sensorik]" di pembuka adegan + kalimat penutup "kesimpulan". C04 & C05 tipis.
- **Koita**: kalimat capstone diulang verbatim di K01; cabang host K01 nyaris reskin.
- **Yutaka**: tic paling konsisten di seluruh batch — hampir semua cabang berakhir dengan kalimat "pelajaran" eksplisit. Juga rute paling tipis dialognya (Y12 ekstrem).
- **Harumi**: H04/H08 — cabang host direskin, bukan ditulis ulang.
- **Moeka**: tiga serangkai dipaksakan (Mo03), simile diulang antar cabang (Mo05), narator menjelaskan subteks (Mo06, Mo09), pembuka bulan formulaic (Mo13-15).
- **Shiori**: hampir semua adegan diduplikasi antar host; tag fisik diulang tiap kemunculan; beberapa dialog "epigram ala pelajaran hidup".
- **Nagisa**: paling bersih di batch ini — cuma satu tic (penutup "emosi+emosi=bercampur"), tidak ada adegan tipis, deskripsi konkret dan dialog-driven.
- **Miyuki**: tidak tipis (malah cenderung panjang), tapi mekanis — satu deskriptor fisik, satu gerakan reaksi, satu arc emosi dipakai ulang di hampir semua adegan.

## Yang Tidak Perlu Disentuh

Prosa rute **Nagisa** secara umum sudah terasa paling "manusiawi" di batch ini (detail konkret spesifik ke adegan, dialog bervariasi, tanpa struktur esai yang kaku) — jadikan acuan gaya kalau Antigravity butuh contoh pembanding saat merevisi rute lain.
