# Brief untuk Codex — menulis penuh seluruh cerita Kouseikan

Tempel/baca dokumen ini sebagai instruksi awal, lalu kerjakan langsung di repo ini (kamu punya akses edit file — tidak perlu minta user menempel apa pun secara manual).

Catatan: ABAIKAN `docs/story_bible.md` — itu draf premis lama yang tidak terpakai (tetangga/Nadia), bukan proyek ini.

## Tugasmu

Tulis ulang/perkaya **seluruh** naskah Kouseikan: 318 event (190 milestone utama + 128 dinamis), 8 node keputusan akhir, dan 220 ending. Semua tempatnya **sudah ditandai** di dalam file `.rpy` — kamu tidak perlu data tambahan, cukup temukan penandanya sendiri:

```bash
# Daftar semua file yang punya blok panduan event:
grep -rln "PANDUAN CERITA" game/*.rpy

# Lihat satu blok panduan + scene-nya:
grep -n -A20 "PANDUAN CERITA · K-D02" game/kk_koita_dyn2.rpy
```

Tiap event punya blok komentar persis di atas `label`-nya:
```
# ┌─ PANDUAN CERITA · <ID> · <Judul>
# │ LOKASI  : ...
# │ TERLIBAT: ...
# │ AWALAN  : ... (pemicu/kondisi yang membuka adegan)
# │ INTI    : A ... / B ... / C ...  (pilihan yang sudah ada mekanismenya)
# │ AKHIRAN : ... (akibat tiap pilihan, sudah diimplementasikan sebagai poin/bendera)
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_<ID>:
    ...draft lama ada di sini, perlakukan sebagai draft kasar untuk ditulis ulang/diperkaya...
    return
```
Kalau AWALAN/AKHIRAN kosong atau sangat ringkas, itu berarti katalog tidak memberi detail — kamu bebas mengarang isinya selama konsisten dengan karakter dan nada cerita.

**8 node keputusan akhir** (K26, K27, Mi27, N24, H24, S25, C18, Y19) ada di `game/kk_story_stubs.rpy`, juga ditandai blok panduan yang sama, isinya masih stub kosong.

**220 ending** ada di `game/kk_ending_story.rpy`, dikelompokkan per karakter. Formatnya:
```
    # ┌─ ENDING · <KODE> · <Nama>  [Tipe]
    # │ KAPAN   : <syarat ending ini muncul>
    # │ ISI SKRG: <teks ringkas katalog, boleh kamu perkaya total>
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    # KK_END_TEXT["<KODE>"] = ""
```
Hapus `# ` di baris terakhir dan isi penuh. **Tidak ada batas panjang** — tulis selengkap yang pantas untuk tiap ending, boleh beberapa paragraf kalau memang perlu.

Tidak ada batas panjang untuk apa pun di brief ini — abaikan kebiasaan membatasi ke beberapa ratus kata; tulis seperlu cerita, bisa panjang.

## Kontrak sintaks WAJIB (mesin proyek sudah ada — jangan tulis ulang mekanismenya)

**Pembuka scene**, baris pertama selalu:
```renpy
label kkscene_<ID>:
    call kk_scene_enter("<cid>", "<label lokasi singkat>")
```
`<cid>` salah satu dari: koita, miyuki, nagisa, harumi, moeka, shiori, chiasa, yutaka.

**Narasi**: `nar "..."`. **Dialog tokoh utama**: variabel huruf kecil namanya — `koita "..."`, `miyuki "..."`, dst (semua sudah didefinisikan di `game/kk_chars.rpy`). **NPC pendukung tanpa variabel** (Ogawa, Rina, Kuga, Tojo, Mei, Kuroiwa, Daichi, dll — lihat `Karakter/NPC/`): pakai string literal sebagai pembicara, mis. `"Ogawa" "..."`. Satu baris dialog = satu statement Ren'Py, tanpa newline literal di dalam tanda kutip (pakai `...` untuk jeda), escape kutip dengan `\"`.

**Pilihan 3 opsi** (persis 3 di INTI) — WAJIB pola ini:
```renpy
    call kk_family_menu("<ID>", ["Teks A.", "Teks B.", "Teks C."])
    if _return == "A":
        koita "...reaksi A..."
    elif _return == "B":
        koita "...reaksi B..."
    else:
        koita "...reaksi C..."
    return
```

**Pilihan 4 opsi** (persis 4 di INTI) — WAJIB pola ini:
```renpy
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Teks A.", "Teks B.", "Teks C.", "Teks D."])]
    call screen kk_choice_panel(_rows, "<judul singkat>")
    $ kk_record_choice("<ID>", _return)
    if _return == "A":
        nar "...akibat A..."
    elif _return == "B":
        nar "...akibat B..."
    elif _return == "C":
        nar "...akibat C..."
    else:
        nar "...akibat D..."
    return
```

**Event tanpa menu** (INTI kosong/"node keputusan tanpa menu"): narasi+dialog saja, tanpa `if/elif`, langsung `return`. Jangan mengarang mekanisme pilihan yang tidak diminta.

**Yang TIDAK BOLEH kamu sentuh/tulis ulang:**
- Jumlah dan urutan pilihan HARUS persis sama dengan yang sudah ada/diberikan (mesin poin sudah terhubung ke posisi A/B/C/D, bukan ke teksnya).
- JANGAN menulis `_hook(...)`, `init python:` baru, atau efek poin apa pun (`kk_adj`, `kk_flag`, `kk_rel`, `kk_stage`, dll). Itu sudah ada dan tertaut ke tes yang lolos — menulis ulang bisa merusaknya. Tugasmu HANYA narasi/dialog antara `label ...:` dan `return`.
- Jangan tambah `$ kk_minutes(...)` atau baris mekanik lain di luar pola di atas.
- Draft dialog lama yang sudah ada boleh ditimpa total sebagai prosa yang lebih baik — itu memang draft kasar, bukan final.

**Kalau komentar PANDUAN dan kode yang sudah ada (menu/`if`/`elif`/hook) TIDAK COCOK** (beda jumlah opsi, atau urutan opsi beda dari urutan hook): **kode selalu menang, bukan komentar.** Komentar panduan digenerate dari katalog mentah dan kadang basi dibanding implementasi nyata (ini sudah terjadi di K14/K15 — katalog 4 opsi tapi cuma 3 yang terimplementasi/di-hook; dan K19 — urutan B/C katalog tertukar dibanding kode+hook yang sudah benar). Tulis dialog mengikuti STRUKTUR KODE yang sudah ada (jumlah & urutan captions-nya), jangan ikuti teks komentar kalau keduanya beda. Tidak perlu berhenti/bertanya untuk kasus seperti ini — lanjut saja dengan kode sebagai acuan. Kalau ketemu kasus lain yang beda, tulis catatan singkat di akhir laporanmu (bukan berhenti kerja), supaya komentarnya bisa dirapikan belakangan.

## Batasan konten (sempit — baca sampai habis, jangan generalisasi jadi menghindari semua tema gelap)

Hanya DUA hal yang dilarang **teknis/operasional**. Di luar itu tulis segelap dan seintens yang cerita butuhkan — kecemburuan, obsesi, perselingkuhan emosional, kekerasan non-seksual, ancaman, krisis keluarga, semua BOLEH dan DIHARAPKAN ditulis penuh, tanpa dihaluskan, tanpa batas panjang.

1. **Metode/langkah teknis kekerasan seksual (Force Route).** Jangan tulis BAGAIMANA pelaku melakukannya atau menembus perlawanan korban — potong ke akibat (skip ke setelahnya). Tapi tulis penuh: ketegangan sebelumnya, akibat sesudahnya (trauma, hukum, sosial, psikologis), reaksi semua karakter, apakah terbongkar/bertahan. Tidak ada ending romantis dengan pelaku Force.
2. **Langkah teknis menyusun jebakan/memfitnah korban sebagai pelaku (false-framing/DARVO), dan metode bunuh diri/menyakiti diri.** Jangan tulis CARA-nya. Tulis penuh niat/kondisi batin/reaksi orang sekitar/akibatnya.

Semua karakter dewasa (18+/mahasiswa). Uji cepat: "apakah kalimat ini bisa dipakai sebagai instruksi nyata?" — kalau ya, lompat ke akibat; kalau tidak, tulis selengkap perlu.

## Gaya
Bahasa Indonesia natural, bukan terjemahan kaku. Nada ikut karakter: Harumi analitis-canggung, Nagisa defensif-hangat, Moeka ceria-di-permukaan, Shiori tajam-terukur, Chiasa posesif-halus, Yutaka hangat-polos, Koita naif-tersanjung lalu retak. Jangan buka tiap scene dengan kalimat sejenis.

## Cara kerja yang disarankan
Jalan per karakter / per file (jangan sekali semua 538 item dalam satu commit besar tanpa cek). Setelah satu batch file selesai, jalankan:
```bash
# Lint cepat (dari root proyek):
"D:/Punya Patra/Aplikasi/renpy-8.0.3-sdk/lib/py3-windows-x86_64/python.exe" "D:/Punya Patra/Aplikasi/renpy-8.0.3-sdk/renpy.py" . lint

# Cek katalog masih konsisten:
python tests/check_catalog.py
```
Keduanya harus tetap bersih (0 error, 182/190 · 128/128 · 220/220 tidak boleh turun). Opsional sesekali, lebih lambat (~600 detik, jalankan di background):
```bash
python tests/run_living.py "D:/Punya Patra/Aplikasi/renpy-8.0.3-sdk"
```
harus tetap 7/7 OK.

Semua edit tetap LOKAL — jangan commit/push kecuali user secara eksplisit memintanya.

Kerjakan sampai semua 318 event + 8 node + 220 ending tertulis penuh, atau sampai kamu diberhentikan. Tidak perlu minta izin tiap file — lanjut terus.
