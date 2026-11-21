# Bagian 2 — `C01` (Paruh 2): Cabang C, Cabang D, serta Kontrak Tiga Tahun Sistem

- **Alur:** `M01a` Host Chiasa (`C01` → `C02` → `K01` → `N01`)
- **File Target (Sudah Dipasang):** `game/kk_flow.rpy` (`label kk_first_morning` Cabang C & Cabang D untuk `C01`, serta penutup kontrak Sistem di `label kk_prologue` dan `label kk_intro`).
- **Status:** Menunggu ACC Bagian 2.

---

## Teks Naskah Ren'Py (Bagian 2)

```renpy
# [Di dalam label kk_first_morning (C01 Cabang C & Cabang D) — game/kk_flow.rpy]
        elif _opening_key == "C":
            nar "Daripada terus terkurung di dalam kamar asing bersama suara sinting yang berbisik di dalam tengkorakmu, kau menyibak selimut dengan gerakan cepat dan melangkah menuju pintu kamar untuk memeriksa langsung siapa yang sedang beraktivitas di lantai bawah."
            nar "Namun tepat ketika jemarimu baru saja menyentuh kenop pintu kayu, langkahmu mendadak terhenti di depan cermin panjang yang menempel di dinding samping lemari pakaian."
            nar "Dari balik permukaan kaca itu, seorang gadis bertubuh mungil dan ramping menatapmu balik dengan wajah oval yang pucat, sepasang mata kuning keemasan yang melebar kaku, serta rambut cokelat gelap sepunggung yang separuh bagian atasnya terikat rapi menggunakan pita hitam."
            chiasa "Tunggu dulu... wajah gadis ini... kenapa rasanya aku baru saja melihatnya beberapa menit lalu?"
            nar "Saat kau menahan napas karena gugup, jari-jari tangan kananmu tanpa sadar terangkat menyentuh simpul pita hitam di belakang kepala dan anting mungil di daun telingamu—sementara ekor matamu menangkap papan nama kayu kecil bergambar kuas lukis di pintu kamar yang bertuliskan 'Chiasa'."
            nar "Potongan ciri visual itu langsung menyambung dengan halaman manga yang baru saja kaucibir di peron stasiun kereta bawah tanah sebelum kematianmu."
            chiasa "Ahhh!! Tunggu—jangan bercanda! Wajah ini kan... Amamiya Chiasa?! Adik tiri dari manga 'Kouseikan' yang baru kubaca di stasiun tadi?!"
            nar "Kau membekap mulutmu sendiri dengan telapak tangan yang dingin. Dari seluruh tokoh yang ada di cerita romansa kampus itu, kau justru terlempar masuk ke tubuh si adik tiri tanpa hubungan darah yang tinggal satu atap dengan sang protagonis utama!"
            nar "Belum sempat keterkejutan di dadamu mereda, aroma kaldu sup miso hangat, roti panggang, dan telur goreng dari lantai bawah menarik langkahmu keluar dari kamar."
            nar "Anehnya, begitu telapak kakimu menapak di deretan tangga kayu menuju lantai satu, otot-otot tungkai tubuh ini melangkah turun dengan sangat hafal—bahkan secara otomatis melangkahi anak tangga kelima yang kayunya agak berderit tanpa perlu kauperhatikan."
            nar "Begitu kau tiba di ambang ruang makan lantai bawah yang terang oleh sinar matahari pagi, tampak sebuah kotak plastik biru berisi lauk kiriman dari Amamiya Yoshie tergeletak di atas meja kayu."
            nar "Dan tepat di seberang meja itu, Amamiya Koita berdiri mengenakan celemek di atas kaus rumahnya, sedang meletakkan piring sarapan sambil mengangkat wajah dan menyunggingkan senyum ramah tanpa pertahanan."
            koita "Pagi, Chi-chan. Cepat duduk, makan selagi hangat sebelum dingin. Tumben sekali kau sudah turun sebelum kupanggil dua kali."
            nar "Kau terpaku di ambang pintu ruang makan. Wajah ramah dengan potongan rambut hitam agak berantakan yang tadi hanya berupa gambar dua dimensi yang membuatmu muak di layar ponsel, kini berdiri nyata, bernapas, dan menatapmu dengan akrab dari jarak beberapa langkah."
            nar "Kau tahu dari halaman manga bahwa Chiasa asli selalu menyapanya dengan panggilan manja 'Ko-nii'. Namun di hadapan orangnya langsung, lidahmu mendadak tercekat menolak mengeluarkan sebutan itu."
            chiasa "P-pagi... aku cuma kebetulan bangun lebih awal. A-aku mau cuci muka sebentar sebelum duduk."
            koita "Haha, gugup karena hari pertama kuliah di Seni Rupa, ya? Jangan lama-lama, nanti telur mata sapinya keburu dingin."
            nar "Koita berbalik kembali ke arah kompor tanpa sedikit pun curiga pada caramu berdiri kaku di ambang ruangan. Menjadi Chiasa di rumah ini berarti harus duduk berhadapan setiap hari dengan pria yang merasa paling mengenalmu—sementara salah bicara sedikit saja di meja makan nanti bisa langsung membongkar semuanya."
        else:
            nar "Kau duduk membeku di tepi ranjang, mencengkeram ujung selimut kuat-kuat hingga buku-buku jarimu yang lentik memutih, dan menolak beranjak satu langkah pun."
            nar "Enak saja suara kurang ajar itu menyuruhmu berkeliling memeriksa kamar seperti pesuruh setelah menculik kesadaranmu ke tempat asing. Sebelum kau sudi menggerakkan satu jari pun, entitas yang menyeretmu ke sini harus memberikan jawaban."
            nar "Namun saat kau memutar pandangan dengan kesal ke sekeliling kamar untuk mencari celah, matamu tanpa sengaja menangkap pantulan dirimu sendiri di cermin meja rias yang berseberangan langsung dengan kasur."
            nar "Di samping cermin itu, tampak jadwal kuliah tahun pertama Fakultas Seni Rupa dan Desain, buku sketsa tebal yang terbuka dengan tanda tangan pena 'Shena', serta nampan kayu kecil berisi pita hitam cadangan."
            nar "Kau menghentikan napas sejenak, menyipitkan mata menatap gadis berwajah oval dengan mata kuning keemasan dan rambut cokelat gelap half-up berpita hitam di balik kaca cermin tersebut."
            chiasa "Tunggu sebentar... mahasiswi tahun pertama Seni Rupa... pita hitam... mata keemasan... dan wajah itu..."
            nar "Ingatan tentang bab-bab manga yang baru saja kaucibir habis-habisan di peron stasiun kereta bawah tanah langsung menyambar kepalamu."
            chiasa "Ahhh...?! Jangan bercanda—wajah ini kan Amamiya Chiasa dari manga 'Kouseikan'?!"
            nar "Menyadari kau dilempar masuk ke dalam tubuh si adik tiri posesif tanpa hubungan darah di cerita harem yang paling kaubenci membuat amarahmu langsung meledak ke arah ruang kosong di depan kasur."
            chiasa "Hei, keluar lagi kau! Kau pikir lucu memasukkanku ke tubuh karakter manga sampah ini?! Kembalikan aku ke tubuhku sekarang juga, pengecut!"
            nar "Udara di depan wajahmu berkedip tajam. Emotikon garis di layar kaca biru itu melebarkan senyum miringnya, lalu detik berikutnya sengatan ngilu yang jauh lebih brutal menghantam pangkal lehermu hingga kau terbungkuk di atas kasur sambil memekik tertahan."
            chiasa "Akh—! Sialan, hentikan!"
            sistem "(¬_¬\") Berteriak menuntut ganti rugi seolah kau sedang memarahi kasir toko? Menggemaskan sekali, Manusia. Sayangnya kau bukan pelanggan di sini—kau cuma rongsokan peron yang kupungut~"
            nar "Sengatan listrik itu dicabut seketika, menyisakan napasmu yang terengah-engah di atas seprai dan keringat dingin yang membasahi pelipis, sementara dari lantai bawah terdengar bunyi piring beradu dan langkah kaki yang tenang di dapur."
            chiasa "Hah... hah... dasar psikopat sakit jiwa! Kau memaksaku masuk ke tubuh gadis ini cuma buat bahan tontonanmu?!"
            sistem "( ´ v ` )~ Anggap saja aku penonton setia yang bosan melihat alur cerita yang lurus. Pemilik asli kamar ini sudah tidak ada, dan kakak kesayangannya sedang menyiapkan sarapan di bawah—jadi simpan tenagamu untuk berakting, ya~"
    return

# [Penutup label kk_prologue setelah call kk_first_morning — game/kk_flow.rpy]
    nar "Tepat ketika kau masih berusaha menelan kenyataan gila tentang identitas barumu dan siapa saja orang yang tinggal di sekelilingmu, udara kosong di depan wajahmu kembali bergetar."
    nar "Jendela kaca biru itu meluncur turun untuk kedua kalinya, menampilkan emotikon garis yang membentuk gerakan tepuk tangan lambat yang sarat ejekan."
    sistem "(*^v^*)// Selamat atas pencerahannya, Manusia~ Ekspresi terkejutmu barusan benar-benar layak dijadikan pembuka pagi."
    if kk_host == "yutaka":
        yutaka "Kau... kau sengaja memasukkanku ke dalam manga sampah yang baru kubaca sebelum mati?! Sebagai Kisaragi Yutaka pula?! Apa maumu sebenarnya, brengsek?!"
    else:
        chiasa "Kau... kau sengaja memasukkanku ke dalam manga sampah yang baru kuhina sebelum mati?! Di tubuh Amamiya Chiasa pula?! Otakmu sudah miring, hah?!"
    sistem "( ´ w ` )/ Justru karena kau begitu membenci manga ini dari ujung rambut sampai ujung kaki, kau adalah kandidat paling cocok untukku. Panggil aku Sistem—dan mulai detik ini, kontrak sewa nyawamu resmi aktif."
    sistem "Aturan mainnya sangat sederhana: kau punya waktu tiga tahun penuh sampai Amamiya Koita lulus kuliah untuk menyimpangkan takdir romantisnya sejauh mungkin dari jalur asli manga ini."
    sistem "Evaluasinya hanya dilakukan satu kali, tepat pada hari ia naik ke panggung aula untuk menerima ijazah wisuda (´• v •`). Kalau sampai detik itu skenario romansa sang protagonis masih berjalan mulus... jantung pinjaman di dadamu itu akan kubuat berhenti berdetak di tempat~"
    if kk_host == "yutaka":
        yutaka "Jangan bercanda! Kenapa aku harus ikut campur mengurus urusan ranjang dan percintaan si protagonis naif itu pakai taruhan nyawa segala?!"
    else:
        chiasa "Jangan gila! Kenapa nyawaku harus digantungkan pada urusan cinta kakak tiri menyebalkan itu?!"
    nar "Layar biru transparan itu mendadak berkedip merah menyala selama sepersekian detik, memancarkan gelombang tekanan dingin yang membuat bulu kuduk di tengkukmu berdiri."
    sistem "(¬_¬ ) Karena hidup keduamu adalah milikku. Bagaimana caramu merusak takdirnya, siapa yang kaurangkul atau kauhancurkan, dan seperti apa wajah aslimu di balik topeng tubuh itu? Bukan urusanku menebaknya sekarang."
    sistem "Simpan keluhan moralmu, Manusia ( ´ v ` )~. Aku akan menilai siapa kau sebenarnya dari apa yang kaulakukan selama tiga tahun ini, bukan dari seberapa keras kau memakiku di kamar."
    return

# [Penutup label kk_intro setelah call kk_prologue — game/kk_flow.rpy]
    nar "Ikon wajah di layar kaca biru itu menyipitkan mata, lalu memunculkan barisan teks baru berwarna kuning menyala tepat di depan hidungmu."
    sistem "( ` v ´ )b Dan karena aku tahu kau bakal malas bergerak kalau tidak dipecut, ini misi pembukamu: dalam tujuh hari ke depan, temui tiga orang yang dekat dengan Koita."
    sistem "Amati tabiat mereka, ajak bicara, dan cari tahu celah mana yang bisa kauungkit. Jangan coba-coba mengurung diri di kamar sampai tenggatnya habis—aku paling benci pemeran yang mogok kerja, dan kau sudah merasakan sendiri caraku memberi teguran~ (^_~)-*"
    nar "Jendela kaca biru itu menutup dirinya paksa dengan bunyi dengung halus, meninggalkanmu bersama detak jantung yang masih memburu di tengah pagi tanggal tujuh April."
    jump kk_main
```
