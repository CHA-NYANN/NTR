# Arahan Nada Cerita — Pemain Sebagai Pihak yang Memanfaatkan, Bukan Protagonis Romantis

## Kenapa dokumen ini ada

Setelah dua audit gaya tulisan (ciri-AI di event utama, event dinamis, dan ending), pemilik proyek menyoroti masalah yang lebih mendasar dari sekadar gaya kalimat: **banyak tulisan — terutama bagian yang dikerjakan AI generalis (Gemini) — meromantisasi hubungan pemain dengan karakter lain**, padahal Kouseikan adalah visual novel ber-genre **NTR (18+)**. Secara desain, posisi pemain seharusnya sering berupa pihak yang memanfaatkan/memanipulasi ketimpangan kepercayaan demi kepentingannya sendiri — bukan pasangan yang "saling tumbuh" ala romance konvensional. Dokumen ini jadi acuan nada untuk revisi, dan jadi kriteria audit lanjutan.

## Bukti konkret yang sudah ditemukan (dari audit gaya tulisan sebelumnya)

- Ending Koita/Chiasa banyak ditutup kalimat ala "pertumbuhan hubungan sehat" (E-CF-13: "...satu keputusan untuk berhenti menjadikan kebutuhanmu pusat dari luka yang menimpanya") — nada ini pas untuk romance murni, tapi janggal kalau konteks akumulasi pilihannya sebenarnya eksploitatif.
- Mo-D12 (event dinamis berisiko bunuh diri) ditutup nada PSA/konselor yang suportif, bukan nada seseorang yang baru saja berperan dalam situasi itu.
- Satu-satunya tempat moralitas "pemain bersalah" benar-benar kental adalah grup ending **Force & Kriminal** (disclaimer "ini bukan penebusan/pengampunan") — artinya kesadaran itu TERISOLASI di satu grup ending saja, bukan menyebar proporsional ke seluruh cerita sesuai beratnya konteks.

## Sinyal objektif yang sudah ada di katalog — pakai ini sebagai acuan utama

`game/kk_data_kk_endings.rpy` sudah punya field `type` per ending: `Bad` (62), `Distorted` (13), `Broken` (8), `Romantis` (39), `Neutral` (52), `Khusus` (32), `Koita` (14). 83 ending bertipe **Bad/Distorted/Broken** ini SEHARUSNYA terbaca berat/eksploitatif/bermasalah secara moral — itu konsekuensi logis dari tipe dan `cond`-nya sendiri. Kalau prosa di `kk_ending_story.rpy` (`KK_END_TEXT[...]`) untuk salah satu dari 83 kode ini malah ditulis dengan nada hangat/romantis/menenangkan, itu pertanda jelas ketidakcocokan nada — bukan dugaan, tapi kontradiksi dengan metadata proyek sendiri.

## Prinsip yang harus dipegang saat merevisi

1. **Pilihan pemain = keputusan strategis, bukan cuma pilihan perasaan.** Kalau ada narasi internal pemain, boleh menunjukkan kalkulasi/pertimbangan untung-rugi, bukan melulu keraguan romantis.
2. **Reaksi karakter lain harus menyisakan jejak ketimpangan kuasa/kepercayaan yang dieksploitasi** — jangan selalu diakhiri "saling memahami dengan setara" kalau konteksnya (lihat `cond`/`type`) memang tidak setara.
3. **Narasi penutup (event maupun ending) jangan buru-buru menyimpulkan "hubungan yang sehat"** kalau latar belakangnya eksploitatif — biarkan ambiguitas moralnya tetap terasa, atau malah tunjukkan ironi/ketimpangannya secara eksplisit.
4. **Tetap ikuti batasan yang sudah berlaku** (lihat memori proyek soal Force Route): mekanisme/metode manipulasi atau rekayasa jebakan TETAP tidak ditulis eksplisit (off-screen). Revisi ini soal AKIBAT, reaksi karakter, dan NADA narasi terhadap pemain — bukan menambah instruksi "cara memanipulasi".
5. **Tidak semua rute/ending harus gelap.** Kalau pemain memang konsisten memilih jalur genuinely-romantis/jujur sepanjang rute (sistem "pohon cabang maksimal" — cabang-pemicu + akumulasi poin, bukan satu jalur tetap), ending bertipe `Romantis` yang dihasilkan SAH dan TIDAK perlu diubah jadi gelap. Yang perlu dikoreksi HANYA ketika `type`/`cond` ending itu sendiri (Bad/Distorted/Broken) menandakan konteks eksploitatif tapi teksnya tetap ditulis seolah romance biasa.

## Yang sudah jadi contoh bagus (jangan diubah, jadikan acuan nada)

- Ending grup **Force & Kriminal** — nada "ini bukan penebusan" sudah pas, pertahankan dan jadikan acuan nada untuk ending Bad/Distorted/Broken lain yang konteksnya serupa tapi belum setajam ini.

## Target audit lanjutan

Fokus pertama: 83 ending bertipe `Bad`/`Distorted`/`Broken` di `game/kk_ending_story.rpy` — cek satu per satu apakah teksnya benar-benar terasa berat/eksploitatif sesuai `type`+`cond`-nya, atau malah ditulis dengan nada hangat/romantis yang kontradiktif. 39 ending `Romantis` tidak perlu diaudit ulang (sah apa adanya). 52 `Neutral` + 32 `Khusus` + 14 `Koita` butuh penilaian kasus-per-kasus, menyusul di audit berikutnya kalau diperlukan. Event utama dan event dinamis juga menyusul kalau pola yang sama ditemukan signifikan di ending.

## Hasil audit 83 ending Bad/Distorted/Broken (selesai, 2026-11-24)

**Temuan utama: hipotesis "ending gelap ditulis dengan nada romantis" TIDAK terbukti luas.** Dari 83 ending yang dicek, cuma **1 kontradiksi jelas + 1 borderline**, jauh lebih sedikit dari dugaan awal. Sebagian besar grup (Shiori, Yutaka, Interlock, Chiasa, Koita, NPC Sampingan, Force & Kriminal, sebagian besar Miyuki/Nagisa/Harumi/Moeka) justru sudah dikalibrasi dengan baik — beberapa malah jadi contoh terbaik di proyek untuk menunjukkan manipulasi dengan bobot moral yang pas.

**Kontradiksi nyata (romantis padahal ditandai Bad):**
- **E-SI-06** "Cinta yang Tidak Dihitung" — ditulis sebagai tragedi cinta sejati yang simpatik ("Cinta kalian sungguh ada..."), bertentangan langsung dengan E-FO-06 di file yang sama yang justru menolak framing serupa. **Prioritas revisi #1 dari audit nada ini.**
- E-SI-13 "Kebaikan yang Tidak Dihitung" — borderline, agak terlalu elegis/simpatik untuk tag Bad-nya, meski `cond` memang menunjukkan pemain sungguh berubah (jadi sebagian wajar).

**Masalah berbeda yang ditemukan (bukan romantisasi, tapi "kesalahan pemain lenyap dari narasi"):**
- **E-NA-06, E-MI-14, E-X-04, E-X-09** — bukan ditulis hangat, tapi tanggung jawab pemain yang seharusnya tersirat dari `cond` pemicunya tidak pernah disebut langsung ke "kau" di teks — konsekuensi jatuh ke orang lain tanpa pernah balik menunjuk pemain. Worth revisi juga, tapi beda jenis perbaikan dari "kurangi romantisasi": di sini justru perlu MENAMBAH baris yang menuding pemain, bukan memotong kehangatan.

**Implikasi penting — sumber masalah kemungkinan BUKAN di ending bertipe Bad/Distorted/Broken:**
Contoh asli yang memicu kekhawatiran ini (E-CF-13, "...satu keputusan untuk berhenti menjadikan kebutuhanmu pusat dari luka yang menimpanya") ternyata bertipe **`Koita`**, bukan Bad/Distorted/Broken — artinya ending jenis itu tidak kena "jaring pengaman" tag dark sama sekali, jadi tidak ada yang mengecek nadanya. Dugaan kuat: masalah romantisasi yang dirasakan pengguna kemungkinan besar terkonsentrasi di **98 ending bertipe `Neutral`/`Khusus`/`Koita`** (belum diaudit) dan/atau di **prosa event utama & dinamis** (interaksi momen-ke-momen, bukan ringkasan akhir) — bukan di ending yang sudah ditandai gelap. Rekomendasi: audit lanjutan sebaiknya menyasar dua area itu, bukan mengulang 83 ending yang sudah terbukti cukup baik.
