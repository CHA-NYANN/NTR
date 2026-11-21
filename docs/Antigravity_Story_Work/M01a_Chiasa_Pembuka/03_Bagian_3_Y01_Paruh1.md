# Bagian 3 (ACC) — `Y01` (Paruh 1): Kebangkitan di Apartemen Mewah Yutaka, Interogasi Awal Sistem, serta Cabang A & Cabang B

- **Alur:** `M01a` (`C01` & `C02` selesai → lanjut `Y01` → `Y02` → `Y03` → `K01` → `N01`)
- **File Target:** `game/kk_flow.rpy` (`label kk_prologue` bagian pembuka host Yutaka & `label kk_first_morning` Cabang A dan B untuk `Y01`).
- **Status:** **ACC (Disetujui, dengan penyesuaian ponsel bergetar karena ditelepon Koita)**

---

## Teks Naskah Ren'Py (Bagian 3 — Disetujui)

```renpy
# [Di dalam label kk_prologue — game/kk_flow.rpy]
    if kk_host == "yutaka":
        $ kk_mc_nama = "YUTAKA (kau)"
        show screen kk_set("yutaka", "Apartemen Mewah · Dini Hari")
        with fade
        nar "Begitu jemarimu menggenggam tangan pria itu di dalam kehampaan, gravitasi mendadak berbalik arah. Sebuah sentakan keras merenggut kesadaranmu turun menembus lorong gelap yang pengap, seolah tubuhmu diikat batu dan dilempar paksa ke dasar air yang tak bertepi."
        nar "Gema derit rem baja dan raungan klakson kereta ekspres masih memekakkan telinga batinmu ketika kau tersentak bangun dengan tarikan napas panjang yang memburu."
        nar "Kedua tanganmu refleks mencengkeram bagian tengah dadamu kuat-kuat. Otot-ototmu menegang hebat, bersiap menyambut rasa ngilu dari tulang rusuk yang remuk dihantam moncong lokomotif serta rembesan darah panas di atas batu rel."
        nar "Namun rasa sakit yang kauantisipasi itu tidak pernah datang. Tidak ada tulang yang patah, tidak ada bau amis besi dari darah yang tumpah, dan tidak ada dinginnya kerikil peron kereta bawah tanah di punggungmu."
        nar "Yang tergenggam oleh jari-jarimu yang panjang justru permukaan kaus tidur berbahan katun lembut yang lembap oleh keringat dingin, membungkus bidang dada yang terasa rata, utuh, berotot ramping, dan jauh lebih lebar dari ukuran tubuh yang kauingat."
        nar "Dari lipatan selimut linen berwarna abu-abu gelap yang menutup pinggangmu, menguar aroma deterjen bersih yang sejuk bercampur samar dengan wangi kayu cedar."
        nar "Kau mengerjap keras berkali-kali, mengatur tarikan napas yang masih tersengal di kerongkongan sambil mengedarkan pandangan ke sekeliling ruangan."
        nar "Kau tidak sedang berbaring di aspal stasiun maupun di atas brankar ruang gawat darurat, melainkan di atas ranjang berukuran besar di dalam sebuah kamar apartemen modern yang sangat luas, rapi, dan sunyi senyap."
        nar "Langit-langit beton ekspos yang tinggi, tirai jendela kaca setinggi dinding yang menyisakan siluet gedung-gedung kota saat dini hari, serta dengung halus mesin pendingin udara di tengah keheningan yang terasa terlalu hampa untuk satu orang membuat keningmu berkerut dalam."
        nar "Setiap detail di ruangan mewah yang dingin ini terasa begitu nyata—dan kau yakin belum pernah menginjakkan kaki di tempat seperti ini seumur hidupmu."
    else:
        ...
    if kk_host == "yutaka":
        yutaka "Suara apa itu—?! Siapa yang bicara di dalam kamarku?!"
        nar "Kalimat itu terputus di ujung lidahmu sendiri. Kau membeku selama satu detak jantung penuh, meraba pangkal tenggorokanmu yang bergetar."
        nar "Suara yang baru saja memantul di dinding beton kamar ini adalah suara bariton seorang pria muda—rendah, jernih, terdengar berwibawa secara alami meski sedang serak oleh kepanikanmu, namun jelas bukan warna suaramu sendiri."
        yutaka "Suaraku... tunggu, kenapa suaraku terdengar seperti orang lain?! Hei! Proyektor macam apa ini—keluar dan tunjukkan wajahmu!"
    else:
        ...
    if kk_host == "yutaka":
        yutaka "Tubuh pinjaman...? Pemilik aslinya sudah tidak ada?! Kau pikir aku bakal menelan ocehan gila dari benda mencurigakan di kepalaku?!"
        nar "Denyut ngilu di pelipismu perlahan mereda, menyisakan napasmu yang memburu kasar di tengah keheningan apartemen yang terlalu luas itu."
        nar "Tepat saat kau menggeram kesal, ponsel pintar di atas nakas sebelah ranjang—tepat di samping sebuah jam tangan tipis bertali kulit yang tampak sering dipakai—bergetar panjang berulang-ulang, menyalakan layar panggilan masuk dengan nama kontak 'Koita' yang terus berkedip."
        nar "Sementara itu, beberapa langkah di seberang ranjang, tampak sebuah dompet kulit hitam di atas meja kaca ruang tamu serta pintu kamar mandi dalam yang sedikit terbuka, seolah menantangmu untuk membuktikan sendiri klaim suara tersebut."
    else:
        ...
```
