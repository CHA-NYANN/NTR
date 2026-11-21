# Catatan Kontinuitas — Alur M01a–M05a (Selang-seling Host Chiasa & Yutaka)

Status Alur: **M01a–M04 Selesai Penuh (ACC) · M05a Host Chiasa Terpasang — Menunggu ACC Grand Bab M05a Host Chiasa**

## 1. Status Bagian
| Bagian | Event & Cakupan | Status | File Target |
|---|---|---|---|
| Bagian 1–2 | `C01` (Host Chiasa, M01a) | **ACC** | `game/kk_flow.rpy` |
| Bagian 3–4 | `Y01` (Host Yutaka, M01a) | **ACC** | `game/kk_flow.rpy` |
| Bagian 5–6 | `Mo01` (Host Chiasa & Yutaka, M01b) | **ACC** | `game/kk_spring.rpy` |
| Bagian 8–10 | `C02`, `K01`, `N01` (Host Chiasa, M01a) | **ACC** | `game/kk_chiasa_host.rpy`, `game/kk_koita_y1.rpy`, `game/kk_scenes.rpy` |
| Bagian 11–14 | `Y02`, `Y03`, `K01`, `N01` (Host Yutaka, M01a) | **ACC** | `game/kk_yutaka_host.rpy`, `game/kk_yutaka_route.rpy`, `game/kk_koita_y1.rpy`, `game/kk_scenes.rpy` |
| Grand Bab M01b (Chiasa) | `H01` + `S01` + `Mi01` — Host Chiasa | **ACC** | `game/kk_harumi.rpy`, `game/kk_spring.rpy`, `game/kk_scenes.rpy` |
| Grand Bab M01b (Yutaka) | `H01` + `S01` + `Mi01` — Host Yutaka | **ACC** | `game/kk_harumi.rpy`, `game/kk_spring.rpy`, `game/kk_scenes.rpy` |
| Grand Bab M02 (Chiasa) | `K02` + `Mo02` + `S02` + `N02` + `Mi02` — Host Chiasa | **ACC** | `game/kk_ryokan.rpy`, `game/kk_spring.rpy` |
| Grand Bab M02 (Yutaka) | `K02` + `Mo02` + `S02` + `N02` + `Mi02` — Host Yutaka | **ACC** | `game/kk_ryokan.rpy`, `game/kk_spring.rpy` |
| Grand Bab M03 (Chiasa) | `Mo03` + `H02` + `S03` + `N03` — Host Chiasa | **ACC** | `game/kk_moeka.rpy`, `game/kk_harumi_family.rpy`, `game/kk_shiori_early.rpy`, `game/kk_scenes.rpy` |
| Grand Bab M03 (Yutaka) | `Mo03` + `H02` + `S03` + `N03` — Host Yutaka | **ACC** | `game/kk_moeka.rpy`, `game/kk_harumi_family.rpy`, `game/kk_shiori_early.rpy`, `game/kk_scenes.rpy` |
| Grand Bab M04 (Chiasa) | `C03` + `K03` + `H03` + `Mi03` — Host Chiasa | **ACC** | `game/kk_chiasa_host.rpy`, `game/kk_koita_y1.rpy`, `game/kk_harumi.rpy`, `game/kk_scenes.rpy` |
| Grand Bab M04 (Yutaka) | `K03` + `Y04` + `H03` + `Mi03` — Host Yutaka | **ACC** | `game/kk_koita_y1.rpy`, `game/kk_yutaka_route.rpy`, `game/kk_harumi.rpy`, `game/kk_scenes.rpy` |
| Grand Bab M05a (Chiasa) | `C04` + `K04` + `N04` + `Mi04` — Host Chiasa | **Terpasang — Menunggu ACC Grand Bab M05a Chiasa** | `game/kk_chiasa_host.rpy`, `game/kk_koita_route.rpy`, `game/kk_life_events.rpy`, `game/kk_miyuki_early.rpy` |
| Berikutnya | Grand Bab M05a — Host Yutaka (`K04`, `Y05`, `N04`, `Mi04`) | Menunggu ACC M05a Chiasa | `game/kk_koita_route.rpy`, `game/kk_yutaka_host.rpy`, `game/kk_life_events.rpy`, `game/kk_miyuki_early.rpy` |

## Aturan Panggilan & SOP Permanen (Terkunci oleh User)
- **Acuan Utama Panggilan:** Wajib mengikuti matriks resmi di [Panggilan_Antarkarakter.md](../../../docs/Panggilan_Antarkarakter.md) (NPC wajib mengikuti tahap perkembangan di tabel; panggilan dari pemain boleh sama atau bervariasi secara natural sesuai situasi/pilihan).
- **Ringkasan Tahap Awal (M01a–M02):**
  - **Koita →** `Yutaka`, `Chi-chan`, `Nagisa-chan`, `Miyuki-senpai`, `Harumi-san`, `Moeka-chan`, `Saionji-san`
  - **Yutaka →** `Koita`, `Chiasa`, `Nagisa`, `Tachibana-senpai`, `Kujo-san`, `Kohinata`, `Saionji-san`
  - **Chiasa →** `Ko-nii` (`Koita` hanya jika sengaja menjauh), `Yutaka-kun`, `Nagisa-senpai`, `Tachibana-senpai`, `Kujo-senpai`, `Moemoe-senpai`, `Saionji-senpai`
  - **Nagisa →** `Ko-kun`, `Yutaka`, `Chiasa`, `Miyuki-senpai`, `Harumi-chan`, `Kohinata-san`, `Saionji-san`
  - **Miyuki →** `Koita-kun`, `Yutaka-kun`, `Chiasa-chan`, `Nagisa-chan`, `Harumi-san`, `Moeka-chan`, `Saionji-san`
  - **Harumi →** `Amamiya-kun`, `Kisaragi-kun`, `Amamiya-san`, `Nagisa`, `Tachibana-senpai`, `Kohinata-san`, `Saionji-san`
  - **Moeka →** `Kocchi`, `Yutayuta`, `Chimian`, `Nacchan`, `Miyumiyu-senpai`, `Hahamama`, `Saionji-san`
  - **Shiori →** `Amamiya-san`, `Kisaragi-san`, `Amamiya-san` (Chiasa), `Sakurajima-san`, `Tachibana-senpai`, `Kujo-san`, `Kohinata-san`
- **Dislokasi Identitas pada Panggilan Khusus:** Buat pemain sesekali merasa aneh/ganjil saat dipanggil dengan julukan khusus (`Chimian`, `Yutayuta`, `Chi-chan`, `Chiasa-chan`, dsb.) karena tubuh ini memang bukan tubuh asli pemain.
- **Fleksibilitas Moral Pemain:** Jangan memaksakan satu suara moral yang seragam (seolah pemain selalu jijik atau selalu antusias terhadap misi NTR). Biarkan tiap pilihan dan reaksi mencerminkan spektrum sikap yang berbeda—bisa tidak nyaman/terpaksa/tertekan, pragmatis/dingin, santai, atau malah bersemangat—sesuai arah pilihannya.
- **Perbedaan Reaksi Host Yutaka vs Host Chiasa:** Meskipun pemain di dalamnya sama, Yutaka dan Chiasa memiliki tubuh, posisi sosial, dan hubungan yang berbeda, sehingga reaksi, gaya bicara, dan detail pengamatan mereka pada situasi yang sama **harus terasa berbeda**, tidak sekadar mengulang teks yang sama dengan nama diganti.
- **Pengetahuan Pemain soal Manga Terbatas (Tidak Serba Tahu):** Pemain bukan pembaca fanatik yang hafal seluruh isi manga—banyak hal, latar belakang, rahasia, dan alur cerita yang **tidak ia ketahui**. Jangan membuat narasi POV seolah pemain hafal profil wiki atau masa depan tokoh.
- **Teks Pilihan (`choice`) Anti-Spoiler:** Boleh disesuaikan agar lebih alami (dialog sebagai dialog, tindakan tetap tindakan) selama inti dan urutan opsi tetap sama, dan **jangan pernah membocorkan hasil/efek** di dalam teks pilihan.
- **Jangan sering mengulang nama jurusan dalam dialog:** Di percakapan alami antar teman, cukup sebut "kelasmu", "kelas pagi tadi", "dosenmu", dsb.—jangan menyebut nama jurusan berulang kali kecuali memang benar-benar perlu secara konteks.
- **SOP Wajib Sebelum Menulis:** Selalu baca dulu `docs/Panggilan_Antarkarakter.md`, file prompt terkait di `docs/Gemini_Prompts/adegan/...`, profil karakter di `Karakter/...`, dan cerita sebelumnya agar detail fisik, panggilan, dan kontinuitas tidak pernah meleset.
