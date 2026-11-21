# Bagian 4 — `Y01` (Paruh 2): Cabang C (*Angkat Telepon Masuk dari Koita*) & Cabang D (*Duduk Membisu Menuntut Penjelasan*)

- **Alur:** `M01a` (`C01` & `C02` selesai → `Y01` → `Y02` → `Y03` → `K01` → `N01`)
- **File Target (Sudah Dipasang):** `game/kk_flow.rpy` (`label kk_first_morning` Cabang C dan Cabang D untuk `Y01`, termasuk penyesuaian pemicu ponsel bergetar karena ditelepon Koita).
- **Status:** Menunggu ACC Bagian 4.

---

## Teks Naskah Ren'Py (Bagian 4)

```renpy
# [Penyesuaian pemicu ponsel bergetar di label kk_prologue — game/kk_flow.rpy]
    if kk_host == "yutaka":
        yutaka "Tubuh pinjaman...? Pemilik aslinya sudah tidak ada?! Kau pikir aku bakal menelan ocehan gila dari benda mencurigakan di kepalaku?!"
        nar "Denyut ngilu di pelipismu perlahan mereda, menyisakan napasmu yang memburu kasar di tengah keheningan apartemen yang terlalu luas itu."
        nar "Tepat saat kau menggeram kesal, ponsel pintar di atas nakas sebelah ranjang—tepat di samping sebuah jam tangan tipis bertali kulit yang tampak sering dipakai—bergetar panjang berulang-ulang, menyalakan layar panggilan masuk dengan nama kontak 'Koita' yang terus berkedip."
        nar "Sementara itu, beberapa langkah di seberang ranjang, tampak sebuah dompet kulit hitam di atas meja kaca ruang tamu serta pintu kamar mandi dalam yang sedikit terbuka, seolah menantangmu untuk membuktikan sendiri klaim suara tersebut."

# [Opsi menu Y01 di label kk_first_morning — game/kk_flow.rpy]
    if kk_host == "yutaka":
        $ _actions = ["Bongkar isi dompet dan ponselnya.", "Hampiri cermin kamar mandi untuk memastikan.", "Angkat telepon masuk dari Koita sekarang juga.", "Duduk membisu menuntut penjelasan."]

# [Y01 Cabang C & Cabang D di label kk_first_morning — game/kk_flow.rpy]
        elif _opening_key == "C":
            nar "Pandanganmu terpaku pada ponsel pintar di atas nakas sebelah ranjang yang masih terus bergetar panjang, bergeser tipis di atas permukaan kayu seiring dering getarannya."
            nar "Nama 'Koita' yang berkedip-kedip di layar panggilan masuk itu membuat dadamu terasa dingin—terlalu ganjil dan terlalu kebetulan jika dibandingkan dengan nama protagonis manga yang baru saja kaucibir habis-habisan di peron stasiun."
            nar "Dengan jantung yang berdegup kencang, kau menggeser tubuh ke tepi kasur dan menyambar ponsel itu dari kabel pengisi dayanya."
            nar "Sebelum jemarimu sempat menyentuh tombol jawab maupun tolak, bagian kaca layar di sekitar foto kontak memantulkan bayangan seorang pemuda asing berwajah tampan dengan rambut hitam pekat agak berantakan dan sepasang mata abu-abu gelap."
            nar "Pada saat yang sama, sensor pemindai wajah otomatis mengenali pemilik tubuh ini dan membuka bilah informasi profil di sudut atas layar kunci: 'Kisaragi Yutaka — Tahun Kedua, Universitas Kouseikan'."
            yutaka "Universitas Kouseikan...? Kisaragi Yutaka...? Tunggu dulu..."
            nar "Kau membandingkan pantulan wajahmu sendiri di permukaan kaca ponsel itu dengan nama yang tertera di layar, dan seketika darah di seluruh tubuhmu terasa berdesir hebat."
            yutaka "Ahhh...?! Jangan gila—wajah ini kan Kisaragi Yutaka?! Sahabat karib Amamiya Koita di manga 'Kouseikan' tadi?!"
            nar "Itu berarti orang yang saat ini sedang meneleponmu di seberang sana adalah sang protagonis utama, Amamiya Koita sendiri!"
            nar "Getaran panggilan masuk di telapak tanganmu hampir berhenti karena terlalu lama dibiarkan. Didorong kepanikan sekaligus dorongan untuk membuktikan apakah dunia ini benar-benar hidup atau sekadar ilusi, ibu jarimu refleks menggeser ikon hijau di layar untuk mengangkat panggilan tersebut."
            nar "Bahkan sebelum kau sempat menarik napas untuk menyiapkan sepatah alasan pun, suara seorang pemuda langsung terdengar jernih dari balik pengeras telinga."
            koita "Halo, Yutaka? Tumben lama sekali angkat teleponnya, kau baru bangun ya? Kita tetap jadi berangkat kuliah bareng dari depan stasiun pagi ini, kan?"
            nar "Suara itu terdengar begitu nyata—ramah, hangat, sedikit terburu-buru khas mahasiswa di pagi hari pertama semester, dan penuh keakraban seseorang yang sudah mengenal pemilik tubuh ini sejak kecil tanpa menaruh curiga sedikit pun."
            nar "Mendengar tokoh manga yang beberapa menit lalu hanya berupa balon teks dua dimensi kini berbicara langsung di telingamu membuat lidahmu mendadak kelu."
            yutaka "A-ah... soal itu, kepalaku agak pusing waktu bangun barusan. Kau berangkat duluan saja, nanti kukabari lagi kalau sudah di kampus ya, Koita."
            koita "Eh, kau nggak apa-apa? Tumben sekali kau mengeluh pusing pagi-pagi. Jangan dipaksa kalau memang belum enak badan, ya. Nanti absen kelas pagi biar kutanyakan ke anak-anak fakultasmu kalau berpapasan. Kabari aku kalau butuh sesuatu."
            nar "Sambungan telepon itu terputus dengan bunyi klik halus. Kau menurunkan ponsel dari telingamu perlahan-lahan dengan napas tertahan; bukan hanya dunia manga ini benar-benar nyata, tetapi Amamiya Koita juga memercayai setiap patah kata yang keluar dari mulut tubuh ini tanpa keraguan sedikit pun."
        else:
            nar "Kau meremas seprai linen kasur itu kuat-kuat hingga buku-buku jarimu memutih dan menolak beranjak satu langkah pun dari tempat tidur."
            nar "Enak saja suara sialan itu menyuruhmu jalan-jalan memeriksa kamar seperti pesuruh setelah menculik kesadaranmu ke tempat asing. Di atas nakas sebelahmu, getaran telepon masuk di layar ponsel akhirnya berhenti sendiri, menyisakan notifikasi panggilan tak terjawab yang meredup."
            nar "Namun tepat saat kau mendongak hendak memaki ruang kosong di depan ranjang lagi, tatapanmu tanpa sengaja menangkap pantulan dirimu sendiri di cermin pintu lemari pakaian besar yang berseberangan langsung dengan kasur."
            nar "Di dalam cermin itu, tampak seorang pemuda bertubuh tinggi ramping dengan rambut hitam pekat bergaya two-block yang agak berantakan dan sepasang mata abu-abu gelap yang menatap lurus ke arahmu—tepat di sebelah rak televisi yang memajang bingkai foto masa kecil empat sekawan di festival musim panas."
            nar "Kau menghentikan napas sejenak, menyipitkan mata memperhatikan pemuda di dalam cermin, lalu beralih menatap sosok anak laki-laki dan gadis kecil berpita hitam di dalam bingkai foto tersebut."
            yutaka "Tunggu dulu... potret empat anak di festival itu... jam tangan di nakas itu... dan wajah pria di cermin itu..."
            nar "Ingatan tentang bab-bab manga yang baru saja kaucibir habis-habisan di peron stasiun kereta bawah tanah berkelebat cepat di kepalamu."
            yutaka "Ahhh...?! Tunggu—jangan bercanda! Wajah ini kan Kisaragi Yutaka dari manga 'Kouseikan'?!"
            nar "Menyadari kau dilempar masuk ke dalam tubuh si sahabat kaya yang kesepian—figuran yang di sepanjang cerita hanya dijadikan tempat curhat sementara cintanya pada adik tiri sang protagonis tak pernah terbalas—membuat amarahmu langsung meledak ke arah ruang kosong di depan kasur."
            yutaka "Hei, keluar lagi kau! Kau pikir lucu memasukkanku ke tubuh figuran manga sampah ini?! Kembalikan aku ke tubuhku sekarang juga, pengecut!"
            nar "Udara kosong di depan wajahmu berkedip tajam. Emotikon garis di layar kaca biru itu melebarkan senyum miringnya, lalu detik berikutnya dengung frekuensi tinggi mendadak menghantam gendang telingamu, disusul rasa ngilu yang buas di belakang bola mata hingga kau terbungkuk di atas kasur sambil mencengkeram kening."
            yutaka "Argh—sialan! Hentikan!"
            sistem "(¬_¬\") Menuntut pelayanan sambil berteriak seolah kau pelanggan raja di restoran bintang lima? Nyalimu lumayan juga, Manusia, sayang sekali otakmu tertinggal di bawah roda kereta~"
            nar "Sengatan ngilu itu dicabut seketika, menyisakan napasmu yang terengah-engah di atas kasur dengan keringat dingin membasahi tengkuk dan pelipis."
            yutaka "Hah... hah... dasar psikopat sakit jiwa! Kau memungutku ke apartemen ini cuma buat dijadikan bahan tontonanmu?!"
            sistem "( ´ v ` )~ Aku lebih suka disebut sutradara yang murah hati. Mesin pendingin apartemen mewah ini masih menyala, saldo bankmu masih penuh, kota di balik jendela itu terus berjalan, dan kau masih hidup. Jadi berhentilah merengek sebelum kutambah dosis perkenalannya, ya~"
```
