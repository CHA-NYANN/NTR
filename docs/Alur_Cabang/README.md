# Alur Cabang Kouseikan — indeks

Status: 🟡 usulan, kecuali yang ditandai ✅ (canon) atau ⭐ (keputusanmu).
Folder ini memetakan **pohon cabang** seluruh game: per rute, antar rute, dan sampai ke ending.

Pilar ⭐ (10 November 2026): game ini harus menjadi pohon dengan cabang sebanyak mungkin. Jumlah ending tidak dibatasi. Pemain tidak boleh merasa dibatasi pilihan. Jadwal tidak tetap. Tidur tidak wajib. Malam selalu bisa ada kejadian, dan tubuh menanggung akibatnya. Tidak ada target yang dipilih di awal; semua tindakan bisa mengarah ke rute mana saja atau tidak ke mana pun. Pilihan muncul sedikit demi sedikit, dan cabang bisa membelok ke ending lain.

## Isi
| File | Isi |
|---|---|
| [00_Pohon_Global.md](00_Pohon_Global.md) | Tulang punggung tiga tahun, lapisan cabang, template cabang event, pintu keluar awal |
| [01_Miyuki_Masokis.md](01_Miyuki_Masokis.md) | Rute Masokis: arah luka, burnout, omiai Hayase, pasangan palsu |
| [02_Nagisa_Yandere.md](02_Nagisa_Yandere.md) | Rute Yandere: tangga eskalasi, Koko, Haruto, dan target obsesi |
| [03_Harumi_Eksploitasi.md](03_Harumi_Eksploitasi.md) | Rute Hypersexual/Exploitation: Ogawa, dana lab, studi luar negeri |
| [04_Moeka_DeathFlag.md](04_Moeka_DeathFlag.md) | Rute Death-Flag: lima jendela intervensi, beasiswa, ayah, Malam Tanpa Balasan |
| [05_Shiori_Revenge.md](05_Shiori_Revenge.md) | Rute Revenge: kebohongan, bukti, sasaran balas dendam yang bisa berpindah |
| [06_Chiasa.md](06_Chiasa.md) | Chiasa sebagai NPC (Male Route) dan sebagai host (Female Route), Koita Success, rahasia Shena |
| [07_Koita_dan_BL.md](07_Koita_dan_BL.md) | Nasib Koita, plot armor, Rute BL Yutaka × Koita |
| [08_Yutaka.md](08_Yutaka.md) | Yutaka sebagai host (Male Route) dan sebagai NPC (Female Route) |
| [09_Force_dan_Kriminal.md](09_Force_dan_Kriminal.md) | Force Route dan kejahatan lain: aftermath, investigasi, konsekuensi |
| [10_Sistem_dan_Evaluasi.md](10_Sistem_dan_Evaluasi.md) | Sikap pada Sistem, hukuman, membongkar Sistem, evaluasi, nasib pemain, hati pemain |
| [11_Rute_Sampingan_NPC.md](11_Rute_Sampingan_NPC.md) | NPC yang bisa dikejar dan efek tidak langsungnya pada rute utama |
| [12_Interlock_Antar_Rute.md](12_Interlock_Antar_Rute.md) | Matriks tabrakan antar rute, reaksi berantai, ending kombinasi |
| [13_Katalog_Ending.md](13_Katalog_Ending.md) | Semua kode ending dan cara epilog komposit disusun |
| [14_Pilihan_Harian.md](14_Pilihan_Harian.md) | Pilihan harian di sandbox: efek poin, pengali konteks, selera per karakter, pilihan yang terbuka belakangan |

Tiap file karakter (01–08) juga punya bagian **Poin dan ambang**, **Event dinamis**, dan **Belok ke ending lain**. File 12 punya event dinamis lintas karakter.

Dokumen pendukung: [Sistem_Cabang_dan_Poin.md](../Sistem_Cabang_dan_Poin.md) (dua jenis cabang, poin dan ambang, pilihan yang muncul bertahap, tarikan ending), [Sistem_Waktu_Bebas_dan_Kondisi_Fisik.md](../Sistem_Waktu_Bebas_dan_Kondisi_Fisik.md) (tidak wajib tidur, malam, tubuh), [Milestone_3_Tahun.md](../Milestone_3_Tahun.md), [Jadwal_Harian_NPC.md](../Jadwal_Harian_NPC.md), [Aturan_Evaluasi_dan_Force_Route.md](../Aturan_Evaluasi_dan_Force_Route.md), dan `Karakter/<nama>/Event_<nama>.md`.

## Cara membaca diagram
Diagram ditulis dalam Mermaid. Di VS Code, pratinjau Markdown bawaan belum menggambar Mermaid; pasang ekstensi pratinjau Mermaid atau buka versi interaktifnya di artifact. Semua diagram sudah dicek sintaksnya.

| Bentuk | Arti |
|---|---|
| Kapsul `([ ])` | titik mulai atau titik waktu |
| Kotak `[ ]` | event atau keadaan |
| Belah ketupat `{ }` | pemeriksaan kondisi tersembunyi |
| Segi enam `{{ }}` | **gerbang** rute atau hub besar |
| Bendera `> ]` | **titik tanpa balik** |
| Kotak ganda `[[ ]]` | **ending** |
| Garis putus-putus | pengaruh tidak langsung atau pintu keluar |

Warna garis tepi: oranye = gerbang, merah = bahaya atau Bad, hijau toska = romantis atau pulih, kuning tua = Distorted, abu-abu = Neutral, nila = Koita, ungu = khusus atau kombinasi.

## Kode
- **Event:** ID lama tetap dipakai (Mi16, N14, K17, dan seterusnya). Cabang baru di dalam event ditulis `Mi16-B` (pilihan B).
- **Event dinamis:** `Mi-D01`, `N-D01`, `H-D01`, `Mo-D01`, `S-D01`, `C-D01`, `K-D01`, `Y-D01`; lintas karakter `X-D01`. Muncul karena poin atau bendera, bukan tanggal.
- **Ending:** `E-<rute>-<nomor>`. Prefiks: MI, NA, HA, MO, SH, CH (Chiasa NPC), CF (Chiasa host), KO, BL, YU (Yutaka NPC), YH (Yutaka host), FO (Force/kriminal), SI (Sistem dan nasib pemain), HP (hati pemain), NPC (rute sampingan), X (kombinasi).
- **Host:** (Y) hanya Male Route, (C) hanya Female Route, (Y/C) keduanya.
