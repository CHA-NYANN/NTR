# Dialog penghubung draft editorial dari Event_Harumi dan Alur_Cabang/03.
# ┌─ PANDUAN CERITA · H01 · Perpustakaan Sains
# │ LOKASI  : Kampus Kouseikan · Gedung Sains & Lab
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : ia menyendiri membaca.
# │ INTI    : A duduk bersebelahan / B tanya soal / C abaikan.
# │ AKHIRAN : A membuka percakapan akademik.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H01:
    call kk_scene_enter("harumi", "Perpustakaan sains")
    if kk_host == "chiasa":
        nar "Di luar jendela kaca lebar lantai dua Gedung Sains & Lab, puncak-puncak pohon sakura bergoyang diterpa angin April sementara suara tawa rombongan Hanami terdengar samar dari kejauhan. Namun di dalam ruang baca ini, suasana nyaris sunyi sepenuhnya."
        nar "Hanya terdengar dengung halus pendingin ruangan, bau kertas buku referensi yang kering, sesekali bunyi halaman dibalik, serta goresan pelan ujung pensil mekanik di atas kertas."
        nar "Kau melangkah pelan menyusuri lorong di antara rak-rak tinggi untuk mencari buku referensi teori warna dan komposisi optik yang kebetulan tersimpan di bagian arsip lintas bidang. Begitu melewati deretan rak paling ujung dekat jendela sudut, langkahmu terhenti."
        nar "Di meja baca yang paling dekat dengan cahaya pagi pucat itu, seorang mahasiswi duduk sendirian menghadap buku teks tebal terbuka. Rambut abu-abunya yang agak panjang diikat satu menyamping hingga menjuntai rapi ke depan bahu kiri. Ia mengenakan kardigan abu-abu sederhana di atas kemeja putih bersih."
        nar "Kujo Harumi—mahasiswi tahun kedua yang wajahnya baru sempat kau kenal sepintas dari lingkar pertemanan Koita. Dari caranya duduk tegak dan fokus penuh pada bukunya, ia terkesan tenang dan tidak banyak bicara."
        nar "Satu jari tangan kirinya menahan tepi halaman buku agar tidak menutup, sementara tangan kanannya berulang kali menuliskan deretan angka dan tanda panah kecil pada buku catatan bersampul hitam di sebelahnya. Setiap beberapa detik, ia menaikkan bingkai kacamatanya dengan ujung jari tengah tanpa sedikit pun mengalihkan pandangan dari kertas."
        nar "Tepat di sampingnya, sebuah kursi kayu tampak sedikit tertarik keluar dari kolong meja—entah bekas seseorang yang baru saja beranjak pergi, atau ruang kosong yang memang dibiarkan terbuka."
        nar "Belum sempat kau memutuskan apakah akan langsung berbelok ke rak di belakangnya, mata biru tua di balik kacamata itu naik sekilas menangkap bayanganmu yang berdiri di ujung meja."
        harumi "Amamiya-san, bukan?"
        nar "Suaranya pelan, datar, dan terjaga rapi menyesuaikan keheningan ruang baca—sama sekali tidak terdengar kesal karena terganggu."
        harumi "Kalau kamu mencari buku referensi yang sedang kubuka ini, masih ada satu salinan lagi di rak baris ketiga sebelah kiri. Tapi kalau kamu sedang mencari tempat duduk... kursi di sebelahku ini belum dipakai siapa-siapa."
    else:
        nar "Di luar jendela kaca lebar lantai dua Gedung Sains & Lab, kelopak sakura berterbangan di atas keramaian Hanami yang terdengar samar seperti dengung jauh. Sebaliknya, di dalam ruang baca ini, udara terasa dingin, kering, dan nyaris sunyi sepenuhnya."
        nar "Kau masuk ke sini sekadar untuk menjauh sebentar dari bisingnya taman kampus sekaligus mencari buku referensi dasar yang mungkin bisa membantu menutupi banyak materi kuliah yang sama sekali tidak kauingat. Dengan kedua tangan masih terselip di saku jaket, langkahmu melambat di ujung lorong rak dekat jendela sudut."
        nar "Di meja baca paling pojok yang diterangi cahaya pagi pucat, duduk seorang mahasiswi berkacamata dengan rambut abu-abu agak panjang yang diikat satu menyamping hingga menjuntai ke depan bahu kirinya. Kardigan abu-abu di atas kemeja putihnya tampak serapi cara duduknya yang tegak."
        nar "Kujo Harumi—wajah yang sempat kaulihat di foto lama dan grup obrolan teman-teman Koita. Satu jari tangan kirinya menahan halaman buku teks tebal agar tidak menutup, sementara tangan kanannya berulang kali menggoreskan deretan perhitungan pada buku catatan kecil bersampul hitam di sebelahnya. Sesekali ia menaikkan bingkai kacamatanya dengan ujung jari tengah tanpa sedikit pun mengangkat pandangan."
        nar "Tepat di sebelah kursinya, sebuah kursi kayu lain tampak agak tertarik keluar dari kolong meja—tidak jelas apakah bekas seseorang yang baru saja beranjak, atau ruang yang memang dibiarkan terbuka."
        nar "Ketika kau berhenti dua langkah dari ujung meja, mata biru tua di balik kacamata itu naik sekilas menangkap bayanganmu."
        harumi "Kisaragi-kun?"
        nar "Suaranya datar, pelan, dan terjaga sesuai keheningan ruang baca—sama sekali tidak terdengar terkejut maupun terganggu."
        harumi "Kalau kamu mencari buku referensi yang sedang kubuka ini, masih ada satu salinan lagi di rak baris ketiga sebelah kiri. Kalau kamu sedang mencari tempat duduk... kursi di sebelahku ini belum dipakai."
    call kk_family_menu("H01", ["Tarik kursi dan duduk di sampingnya.", "\"Sedang mengerjakan soal apa?\"", "Lewati mejanya agar ia bisa membaca dengan tenang."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau mengangguk singkat, lalu menarik kursi kayu di sebelahnya dengan sangat pelan agar kakinya tidak berdecit di atas lantai linoleum. Kau meletakkan tas kainmu di pangkuan dan duduk menghadap meja yang sama."
            chiasa "Terima kasih, Kujo-senpai. Di luar sedang agak terlalu ramai buat membaca dengan tenang, jadi aku numpang duduk sebentar di sini."
            nar "Harumi menoleh sekilas ke arah jendela kaca yang memperlihatkan kerumunan mahasiswa di taman bawah, lalu kembali menatap mejanya dengan ekspresi datar yang nyaris menyerupai humor kering."
            harumi "Benar. Keramaian di bawah pohon sakura menghasilkan terlalu banyak kebisingan akustik untuk membaca atau menghitung. Di sudut ini tingkat gangguannya jauh lebih rendah."
            nar "Tanpa perlu diminta, ia mendorong buku teks tebal di depannya beberapa sentimeter ke tengah meja agar sudut halamannya tidak tertutup bayangan lengannya, lalu merapikan kotak pensil dan penghapusnya sejajar di tepi atas."
            harumi "Kalau kamu mau melihat referensi di sini atau butuh ruang lebih lebar di sisi kanan, bukunya bisa kugeser ke tengah seperti ini."
            nar "Alih-alih langsung menenggelamkan wajahnya kembali ke deretan rumus, Harumi diam sejenak—menunggu dengan sabar sampai kau selesai mengeluarkan buku catatanmu dan menemukan posisi duduk yang nyaman."
            chiasa "Maaf kalau kehadiranku malah memecah konsentrasi Kujo-senpai."
            harumi "Tidak. Konsentrasiku tidak serapuh itu."
            nar "Ia membetulkan letak kacamatanya dengan gerakan jari yang tenang, lalu menoleh setengah badan kepadamu dengan sorot mata biru tua yang lurus dan jujur."
            harumi "Aku juga tidak keberatan dijeda kalau kamu sedang kesulitan mencari buku atau ingin menanyakan sesuatu. Aku hanya perlu diberi tahu secara langsung kalau memang ada pertanyaan—soalnya aku sering gagal membaca ekspresi orang yang sebenarnya ingin bicara."
            chiasa "Begitu, ya... baik, kalau ada yang ingin kutanyakan nanti pasti langsung kubilang, Senpai."
            harumi "Bagus. Itu jauh lebih efisien daripada sama-sama menebak."
            nar "Harumi mengangguk tipis seolah kesepakatan sederhana itu sudah cukup jelas dan menenangkan baginya, lalu kembali menurunkan pandangan ke deretan perhitungannya. Keheningan yang turun di antara kalian berdua kini terasa jauh lebih hangat dan akrab daripada basa-basi perkenalan yang biasanya diucapkan orang di kampus."
        else:
            nar "Kau mengangguk santai, menarik kursi kayu di sebelahnya dengan pelan agar tidak menimbulkan bunyi gesekan, lalu duduk sambil meletakkan buku catatan tipis dan tasmu di samping kaki meja."
            yutaka "Makasih, Kujo-san. Di luar terlalu berisik buat baca tenang, jadi aku numpang duduk sebentar di sini."
            nar "Harumi melirik sekilas ke arah jendela kaca yang memperlihatkan kerumunan di bawah pohon sakura, lalu kembali menatap mejanya dengan wajah datar."
            harumi "Masuk akal. Tingkat kebisingan di taman siang ini memang tidak cocok untuk berkonsentrasi."
            nar "Tanpa diminta, ia menggeser buku teks tebal di hadapannya beberapa sentimeter ke tengah meja agar ruang di sisimu lebih lega, lalu merapikan penghapus dan kotak pensilnya sejajar di tepi atas."
            harumi "Kalau kamu mau ikut melihat atau butuh ruang menulis di sebelah kanan, bukunya bisa kugeser ke tengah seperti ini."
            nar "Ia benar-benar menunggu dengan tenang sampai kau selesai membuka catatanmu dan duduk nyaman, tidak langsung menenggelamkan wajahnya kembali ke bacaan."
            yutaka "Tidak apa-apa kalau aku di sini? Takutnya malah mengganggu."
            harumi "Tidak. Konsentrasiku tidak terganggu oleh orang yang duduk diam. Dulu waktu kelompok belajar juga kamu sering diam dulu sebelum bertanya."
            nar "Kalimat pendek itu memberimu satu petunjuk kecil tentang bagaimana pemilik asli tubuh ini biasanya bersikap di depan Harumi. Ia membetulkan letak kacamatanya, lalu menoleh setengah badan padamu."
            harumi "Aku juga tidak keberatan dijeda kalau ada yang mau ditanyakan, Kisaragi-kun. Hanya saja, katakan langsung kalau ada pertanyaan—aku kurang pandai menebak dari ekspresi wajah."
            yutaka "Oke, catat. Nanti pasti langsung kubilang kalau aku mentok."
            nar "Harumi mengangguk pelan seolah kesepakatan lurus itu sudah cukup jelas, lalu kembali menurunkan pandangannya ke kertas hitungannya. Cara kerjanya yang sabar dan tanpa basa-basi itu terasa jauh lebih hangat daripada perkenalan ramah yang dibuat-buat."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Alih-alih langsung duduk, kau berhenti di ujung meja dan mencondongkan badan sedikit sambil melirik barisan persamaan, tanda panah koreksi, serta grafik kecil yang digambar sangat rapi di buku catatan hitamnya."
            chiasa "Permisi, Kujo-senpai. Kelihatannya sejak tadi Kujo-senpai mengulang baris perhitungan yang sama berkali-kali—sedang mengerjakan soal apa?"
            nar "Ujung pensil mekanik Harumi terhenti tepat di atas sebuah angka. Ia tidak langsung menjawab, melainkan menatap baris terakhir tulisannya selama beberapa detik penuh sambil mengangkat sedikit telunjuk tangan kirinya memberi isyarat."
            harumi "Sebentar. Aku masih memeriksa bagian akhir jawabannya."
            nar "Caranya memintamu menunggu sama sekali tidak terasa angkuh atau seperti ingin memamerkan kepandaian. Kau memperhatikan bibirnya bergerak menggumamkan dua perbandingan angka tanpa suara, lalu ia mencoret satu baris kecil di pinggir kertas dan menuliskan angka pembanding baru dengan hati-hati—jelas ia hanya tidak mau menjelaskan sebuah kesimpulan sebelum ia sendiri yakin kebenarannya."
            nar "Sepuluh detik kemudian, ia menghela napas tipis yang nyaris tak terdengar, meletakkan pensil mekaniknya sejajar tepi buku, membetulkan kacamata, lalu memutar buku catatan hitamnya sembilan puluh derajat menghadap ke arahmu."
            harumi "Sudah. Ada satu variabel pada contoh soal di buku ini yang hasilnya tidak konsisten dengan grafiknya, jadi aku mengujinya ulang dari awal. Bagian mana yang ingin kamu tahu dulu, Amamiya-san?"
            chiasa "Grafik lengkung kecil di pojok bawah itu kelihatannya menarik—kalau tidak merepotkan Kujo-senpai."
            harumi "Tidak merepotkan. Untung kamu langsung menunjuk bagiannya—aku sering mulai menjelaskan terlalu jauh dari teori dasar kalau tidak ditanya secara spesifik."
            nar "Ia menarik kursi kosong di sebelahnya beberapa sentimeter lebih dekat agar kau bisa duduk atau membungkuk melihat dengan nyaman, lalu menunjuk garis kurva itu dengan ujung belakang pensilnya."
            harumi "Coba lihat titik tekukan di tengah ini. Bayangkan seperti gradasi cahaya pada permukaan melengkung—kalau nilai di baris sebelumnya berubah tiba-tiba, garisnya seharusnya patah tajam di sini. Di buku teks tercetak mulus karena penyuntingnya membulatkan angka terlalu cepat."
            chiasa "Oh... pantas saja tadi Kujo-senpai sampai menghitung ulang di kertas terpisah. Padahal kalau dilihat sepintas, garis di buku kelihatan benar-benar saja."
            nar "Harumi mengerjap sesaat mendengar tanggapanmu, seolah tidak menyangka kau benar-benar mengikuti penjelasannya sampai ke titik itu alih-alih sekadar mengangguk sopan."
            harumi "...Ya, persis seperti itu. Pengamatanmu cepat juga, Amamiya-san. Kalau kamu mau melihat dua halaman berikutnya, silakan duduk saja."
            nar "Untuk pertama kalinya sejak kau masuk ruang baca ini, sudut bibir Harumi tampak sedikit lebih rileks saat ia menggeser kursi untukmu."
        else:
            nar "Kau tidak langsung duduk, melainkan berhenti di tepi meja sambil menumpukan sebelah tangan ringan di sandaran kursi kosong dan melirik deretan angka serta coretan koreksi di buku catatan hitamnya."
            yutaka "Dari tadi kelihatannya kau mengulang baris yang sama terus, Kujo-san. Lagi mengerjakan soal apa?"
            nar "Ujung pensil mekanik Harumi berhenti di atas kertas. Ia tidak langsung menoleh, melainkan menatap baris terakhir hitungannya selama beberapa detik penuh sambil mengangkat sedikit telunjuk tangan kirinya."
            harumi "Sebentar. Aku masih memeriksa bagian akhir jawabannya."
            nar "Caranya memintamu menunggu sama sekali tidak terasa seperti orang yang sedang pamer kepandaian. Kau melihatnya mencoret satu angka pembulatan, menggumamkan perbandingan pelan tanpa suara, lalu menuliskan ulang hasil akhirnya—ia jelas tidak mau menjelaskan kesimpulan yang belum ia yakini sendiri."
            nar "Setelah memastikan angkanya cocok, ia meletakkan pensilnya sejajar tepi buku, membetulkan kacamata, lalu memutar buku catatannya menghadap ke arahmu agar mudah dibaca."
            harumi "Sudah selesai. Ada satu tabel tren di buku ini yang selisih datanya meleset dari rumus pengantarnya, jadi aku menghitung ulang untuk memastikan mana yang salah cetak. Bagian mana yang ingin kamu lihat dulu, Kisaragi-kun?"
            yutaka "Bagian selisih tabel yang kaucoret di tengah itu. Kenapa di bukunya malah kelihatan rata?"
            harumi "Untung kamu langsung menunjuk intinya—aku sering mulai menjelaskan terlalu jauh dari definisi awal kalau tidak ditanya spesifik."
            nar "Ia menunjuk dua kolom angka di kertasnya dengan ujung belakang pensil."
            harumi "Di kolom ketiga, penulisnya membuang angka di belakang koma sebelum mengalikannya ke baris bawah. Untuk contoh singkat mungkin kelihatan sepele, tapi kalau dipakai membaca tren jangka panjang, arah grafiknya langsung melenceng jauh."
            yutaka "Oh... berarti kalau cuma menghafal hasil akhirnya tanpa mengecek langkah tengahnya, pasti ikut salah semua."
            nar "Harumi mengedip pelan, seolah sedikit terkejut kau menangkap celah praktisnya secepat itu."
            harumi "...Benar. Kau menangkap polanya lebih cepat daripada dugaanku, Kisaragi-kun. Kalau mau duduk dan lihat bagian selanjutnya, silakan."
    else:
        if kk_host == "chiasa":
            nar "Kau menatap sekilas lembaran perhitungan yang terbentang rapi di atas meja, lalu memutuskan tidak memecah ketenangan belajarnya pagi ini. Kau tersenyum tipis dan membungkuk kecil dengan sopan."
            chiasa "Terima kasih tawarannya, Kujo-senpai. Aku cuma lewat mau mengambil buku di rak belakang saja—tidak enak kalau sampai mengganggu waktu bacanya."
            nar "Harumi mempertahankan tatapannya padamu selama satu detik penuh, seolah benar-benar ingin memastikan kau tidak sedang menolak karena sungkan atau bingung mencari rak."
            harumi "Kamu yakin tidak butuh petunjuk letak raknya?"
            chiasa "Iya, tadi aku sudah lihat denahnya di dekat pintu masuk. Permisi, Kujo-senpai."
            harumi "Baiklah. Rak arsip lintas bidang ada di lorong sebelah kanan."
            nar "Ia mengangguk singkat dengan sopan. Kau melanjutkan langkah melewati mejanya menuju deretan rak belakang yang teduh."
            nar "Ketika beberapa menit kemudian kau mengambil buku dan sempat melirik dari ujung lorong, Harumi sudah kembali menundukkan kepala dengan satu jari menahan halaman buku teksnya. Kursi kayu di sebelahnya tetap tertarik sedikit keluar dalam keadaan kosong—sebuah kesempatan percakapan yang jelas tidak akan pernah ia panggil kembali dengan suara keras di tengah perpustakaan."
        else:
            nar "Kau melirik sekilas lembaran hitungan yang tersusun begitu rapi di depannya, lalu memutuskan tidak memotong konsentrasinya siang ini. Kau mengangkat satu tangan singkat sebagai isyarat sopan."
            yutaka "Makasih, Kujo-san. Aku cuma lewat mau cari buku di rak belakang saja—nggak usah terganggu."
            nar "Harumi menatapmu satu detik lebih lama, seolah benar-benar memeriksa apakah kau sedang butuh petunjuk atau memang berniat lewat saja."
            harumi "Baiklah. Kalau kamu mencari buku pengantar statistik atau referensi umum, letaknya di lorong kedua sebelah kanan."
            yutaka "Siap. Duluan ya."
            nar "Kau melanjutkan langkah menyusuri deretan rak tinggi. Beberapa menit kemudian saat kau melirik balik dari ujung lorong, Harumi sudah kembali menunduk menahan halaman bukunya dengan satu jari, sementara kursi kosong di sebelahnya tetap tidak tersentuh—kesempatan obrolan yang jelas tidak akan ia panggil ulang dengan suara keras di ruang baca."
    return

# ┌─ PANDUAN CERITA · H08 · Omikuji Harumi
# │ LOKASI  : Alam & Pantai · Kuil
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : ramalan "perhatikan hatimu".
# │ INTI    : A bantu menafsirkan / B tertawakan.
# │ AKHIRAN : kejelasan emosi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H08:
    call kk_scene_enter("harumi", "Kuil · Tahun baru")
    nar "Harumi membacakan ramalannya dengan nada yang biasa dipakai menguji petunjuk praktikum. Bagian studi cukup jelas. Bagian cinta membuatnya membaca tiga kali."
    harumi "Perhatikan hatimu. Kalau itu perintah, kriterianya sangat buruk. Tapi aku ingin tahu maksudnya. Aku sering baru mengerti sedang sedih setelah semua orang pergi."
    menu:
        "Bantu ia mencari arti kalimat itu.":
            $ kk_record_choice("H08", "A")
            harumi "Jadi aku boleh mulai dari apa yang kurasakan sekarang?"
            nar "Kau menawarkan mulai dari hal kecil: ingin mendekat atau menjauh, merasa lega atau takut, tanpa harus langsung menemukan nama yang paling tepat. Harumi memandang kerumunan, lalu memilih berdiri sedikit lebih dekat kepadamu."
            harumi "Aku ingin tetap di sini sebentar. Itu sudah informasi, ya."
        "Tertawakan betapa samarnya petunjuk itu.":
            $ kk_record_choice("H08", "B")
            nar "Kau tertawa tentang petunjuk yang dapat berarti apa saja. Harumi ikut mengakui ketidakjelasannya, lalu menyimpan kertas tersebut."
            nar "Ia tidak menanyakan bagian yang sesungguhnya ingin dipahami lagi. Pertanyaan yang mudah ditertawakan rupanya belum tentu mudah diberikan untuk kedua kali."
    return

# ┌─ PANDUAN CERITA · H09 · Hipotesis Cinta
# │ LOKASI  : Kampus Kouseikan · Gedung Sains & Lab
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : ia mencatat perasaannya sebagai data.
# │ INTI    : A bantu mengidentifikasi / B menertawakan / C menjauh.
# │ AKHIRAN : stage 1 (kekosongan emosi).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H09:
    call kk_scene_enter("harumi", "Gedung Sains & Lab")
    nar "Catatan Harumi memuat percakapan singkat dengan Koita dan reaksi tubuhnya sesudahnya: sulit berkonsentrasi, ingin bicara lagi, kecewa ketika undangan dibatalkan. Kolom perasaan sengaja dibiarkan kosong."
    harumi "Aku takut kalau memberi nama, aku akan mulai memilih data yang mendukungnya. Tapi membiarkan kosong juga membuatku terus bertanya apakah semuanya hanya kesalahan."
    if kk_has("harumi_menafsirkan_omikuji"):
        harumi "Di kuil waktu itu kau menyuruhku memperhatikan bagian ini."
    call kk_family_menu("H09", ["Bantu ia mencari kata yang sesuai dengan perasaannya.", "Tertawakan usahanya mencatat perasaan.", "Kembalikan buku itu dan ambil jarak."])
    if _return == "A":
        harumi "Bukan variabel yang salah. Aku memang merasa begitu."
        nar "Kau menawarkan beberapa kata dan membiarkan ia menolak yang tidak sesuai. Harumi memilih rindu, lalu mengubahnya menjadi ingin ditemani."
        harumi "Yang kedua lebih tepat hari ini. Aku tidak harus memutuskan arti seluruh hubungannya untuk mengakui satu perasaan ini."
    elif _return == "B":
        harumi "Begitu. Berarti bagian itu tidak perlu kubahas denganmu."
        nar "Ia tidak mengucapkannya dengan marah. Buku ditarik mendekat, dan percakapan berikutnya hanya tentang hal-hal yang bisa dinilai tanpa menyerahkan sesuatu dari dirinya."
    else:
        nar "Kau mengembalikan buku dan memberi jarak. Harumi menerima, lalu menyimpan halaman yang tadi berharap bisa dibaca bersama."
        harumi "Baik. Aku coba sendiri dulu."
        nar "Suara tenangnya tidak memberitahumu apakah ia membutuhkan ruang atau sedang belajar bahwa kebutuhan untuk dimengerti sebaiknya tidak diajukan kepadamu."
    return

# ┌─ PANDUAN CERITA · H-D01 · Teh Jam Satu
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kujo Harumi
# │ AWALAN  : Larut; dapur asrama (Chiasa bisa masuk, Yutaka hanya di luar jendela); kejelasan ≥ 30
# │ INTI    : A minum dan diam / B tanya perasaannya / C bercerita tentang dirimu
# │ AKHIRAN : kejelasan +
# └─ tulis / perbaiki dialog di bawah ──
label kk_dorm_tea:
    if kk_host == "chiasa":
        call kk_scene_enter("harumi", "Dapur asrama")
        nar "Di dapur asrama Harumi menyisakan satu cangkir untukmu."
    else:
        call kk_scene_enter("harumi", "Di luar jendela dapur asrama")
        nar "Kau tetap di luar. Harumi mengulurkan cangkir lewat jendela dapur."
    harumi "Masih hangat. Hati-hati. Aku menyeduh lebih banyak setelah tahu kamu belum tidur. Itu memang disengaja."
    nar "Ia menunggu kau memegang cangkir dengan aman sebelum menarik tangan. Kebaikan kecil itu tidak diikuti permintaan bantuan atau alasan akademik untuk tetap berada di dekatmu."
    call kk_family_menu("H-D01", ["Minum bersamanya dalam diam.", "Tanyakan apa yang ia rasakan malam ini.", "Ceritakan apa yang membuatmu masih terjaga."])
    if _return == "A":
        nar "Untuk beberapa saat kalian hanya mendengar air di ketel. Harumi tampak akan bertanya, lalu mengurungkannya karena keheningan ternyata tidak terasa salah."
        harumi "Aku tadinya menyiapkan topik supaya kamu tidak bosan. Mungkin kita boleh melewatkan satu topik tanpa kehilangan alasan untuk duduk bersama."
    elif _return == "B":
        harumi "Aku sedang mencoba mencari kata yang tepat. Tenang, mungkin. Tapi juga ingin waktu bergerak lebih lambat."
        nar "Ia memandang cangkirnya, kemudian dirimu."
        harumi "Aku tidak ingin buru-buru menyebutnya cinta hanya agar ada jawaban. Aku ingin mengenali yang ini dulu."
    else:
        harumi "Aku mendengarkan. Kamu tidak perlu menyederhanakan kalau belum tahu kesimpulannya."
        nar "Kau bercerita dan beberapa kali berhenti tanpa urutan yang jelas. Harumi tidak mengoreksi. Sesudahnya ia menyampaikan satu hal yang didengarnya, lalu bertanya apakah ia memahami dengan benar."
    $ kk_minutes(10)
    return

init 1 python:
    _hook("H08-A", lambda: (kk_adj("kejelasan_harumi",10), kk_flag("harumi_menafsirkan_omikuji")))
    _hook("H08-B", lambda: kk_adj("kejelasan_harumi",-5))
    _hook("H09-A", lambda: (kk_adj("kejelasan_harumi",10), kk_flag("harumi_dibantu_menamai_emosi")))
    _hook("H09-B", lambda: (kk_stage("harumi",1), kk_adj("kejelasan_harumi",-5)))
    _hook("H09-C", lambda: kk_stage("harumi",1))
    _hook("H-D01-A", lambda: kk_adj("kejelasan_harumi",5))
    _hook("H-D01-B", lambda: kk_adj("kejelasan_harumi",10))
    _hook("H-D01-C", lambda: kk_adj("kejelasan_harumi",5))


# ┌─ PANDUAN CERITA · H03 · Masakan Eksperimental
# │ LOKASI  : Kampus Kouseikan · Asrama Putri
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : masakannya buruk.
# │ INTI    : A makan semuanya / B jujur / C bantu memasak.
# │ AKHIRAN : C membuka komedi hangat.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H03:
    call kk_scene_enter("harumi", "Asrama Putri")
    if kk_host == "chiasa":
        nar "Cahaya sore musim panas masuk miring melalui jendela dapur bersama Asrama Putri yang sedang lengang. Di atas meja makan panjang di depanmu, Kujo Harumi meletakkan sepiring tumis sayur dan daging dengan gerakan rapi, tepat di samping sebuah buku catatan resep yang dipenuhi tulisan kecil, angka takaran, dan coretan konversi mililiter."
        nar "Harumi mengenakan celemek polos berwarna abu-abu di atas kemeja putihnya, rambut abu-abunya yang diikat menyamping di atas bahu tampak sedikit berantakan oleh uap wajan. Secara visual, hidangan di atas piring itu masih bisa dikenali sebagai masakan rumah—hanya saja aromanya yang menyengat tajam antara manis pekat, asin kecap, dan sedikit bau hangus langsung membuatmu refleks melirik buku catatannya lebih dahulu."
        nar "Harumi membetulkan letak kacamatanya dengan ujung jari, lalu menatap piring itu dan dirimu bergantian dengan wajah sangat serius."
        harumi "Aku mengikuti urutan di buku resepnya, Amamiya-san. Lalu aku menyesuaikan beberapa takaran bumbu dan suhu apinya karena kupikir prosesnya bisa dibuat lebih efisien."
        chiasa "Efisien... maksudnya Kujo-senpai menaikkan suhu apinya biar cepat matang?"
        harumi "Iya. Dan menggabungkan dua tahap bumbu sekaligus supaya tidak perlu mencuci sendok takar dua kali. Ternyata resep masakan tidak senang diperlakukan seperti prosedur laboratorium."
        nar "Ia menggeser sepasang sumpit bersih ke sebelah piringmu dengan ekspresi datar yang nyaris tak bisa ditebak antara pasrah dan penasaran."
        harumi "Secara teori semua bahannya masih layak konsumsi. Mungkin... kamu mau coba sedikit untuk verifikasi rasa?"
    else:
        nar "Sore musim panas di area ruang tamu bersama lantai satu Asrama Putri—batas terjauh yang boleh dimasuki tamu laki-laki dengan izin pengelola asrama. Jendela samping yang menghadap langsung ke dapur bersama terbuka lebar, membiarkan aroma masakan yang agak mencurigakan mengalir keluar menyapa hidungmu."
        nar "Tidak lama kemudian, Kujo Harumi melangkah keluar dari balik pintu dapur membawa sebuah nampan berisi sepiring tumis sayur dan daging, sepasang sumpit, serta buku catatan resep yang penuh angka takaran dan coretan konversi mililiter. Celemek abu-abu polos masih terikat rapi di pinggangnya, dan rambut abu-abu panjang yang diikat menyamping itu sedikit lembap oleh uap wajan."
        nar "Ia meletakkan piring itu di atas meja tamu di depanmu. Dari bentuknya, hidangan itu masih bisa dikenali sebagai tumisan biasa—tetapi baunya yang menusuk tajam antara asin kecap, manis pekat, dan sedikit bau hangus langsung membuatmu ingin membaca buku catatannya lebih dulu sebelum menyentuh sumpit."
        nar "Harumi membetulkan letak kacamatanya dengan ujung jari, lalu menatap piring dan dirimu bergantian dengan wajah sangat serius."
        harumi "Aku mengikuti urutan di buku resepnya, Kisaragi-kun. Lalu aku menyesuaikan beberapa jumlah bumbu dan suhu apinya karena kupikir prosesnya bisa dibuat lebih efisien."
        yutaka "Efisien... maksudmu kau besarkan apinya biar cepat matang?"
        harumi "Iya. Dan menggabungkan dua tahap bumbu sekaligus supaya tidak perlu mencuci sendok takar berulang kali. Ternyata resep masakan tidak senang diperlakukan seperti itu."
        nar "Ia menggeser sumpit bersih ke sebelah piringmu dengan ekspresi datar yang nyaris tak terbaca antara pasrah dan penasaran."
        harumi "Secara teknis semua bahannya masih aman dikonsumsi. Kebetulan kamu lewat di depan asrama—mau coba sedikit?"
    call kk_family_menu("H03", ["Habiskan bagian yang ia tawarkan.", "Jelaskan dengan jujur bagian mana yang terasa aneh.", "Tawarkan membuat percobaan berikutnya bersama."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Melihat kesungguhan di wajahnya dan buku catatan yang penuh tulisan rapi itu, kau memutuskan tidak merusak semangatnya di suapan pertama. Kau mengambil sumpit, menyumpit sepotong besar, lalu memasukkannya ke mulut."
            nar "Detik pertama: asin yang langsung menyambar lidah. Detik kedua: rasa manis gula yang entah kenapa menempel pekat di belakangnya, diikuti tekstur sayur yang terlalu layu namun masih agak gosong di pinggir. Meski matamu sempat menyipit sepersekian detik, kau menelannya tenang—lalu langsung mengambil suapan kedua dan ketiga."
            chiasa "Hmm... rasanya... unik banget, Kujo-senpai. Aku habiskan saja sekalian biar nggak mubazir."
            nar "Harumi mengerjap pelan di balik kacamatanya, menatapmu yang terus mengunyah dengan wajah terkendali."
            harumi "Sampai habis, Amamiya-san? Tunggu—dari aromanya saja aku masih belum yakin dengan rasanya."
            nar "Merasa ada yang tidak beres antara ekspresimu yang terlalu tenang dengan catatan eksperimennya sendiri, Harumi mengambil sumpit cadangan lalu mencicipi satu potong kecil dari pinggir piring."
            nar "Begitu potongan itu menyentuh lidahnya, alisnya tidak naik dan ia tidak menjerit—ekspresinya tetap datar tanpa cela. Namun satu detik kemudian, tangannya langsung bergerak cepat menggeser piring itu menjauh dari jangkauan sumpitmu."
            harumi "Cukup. Berhenti sekarang, Amamiya-san."
            chiasa "Eh—tapi masih tinggal sedikit lagi, Senpai—"
            harumi "Kesediaanmu menghabiskannya bukan bukti bahwa rasanya baik. Konsentrasi garam dan gulanya jelas melewati batas wajar. Ini... ini tidak seharusnya dimakan siapa pun."
            nar "Ia segera menuangkan segelas air putih dingin dan mendorongnya ke hadapanmu dengan raut wajah penuh penyesalan yang kaku."
            harumi "Terima kasih sudah berusaha sopan, tapi lain kali kamu tidak perlu melanjutkan pengorbanan seperti ini demi menghargai percobaanku."
        else:
            nar "Melihat buku catatan yang penuh hitungan rapi itu, kau memutuskan tidak langsung menjatuhkan semangatnya. Kau mengambil sumpit, menyumpit porsi besar, lalu memasukkannya ke mulut dengan tampang paling tenang yang bisa kaupertahankan."
            nar "Begitu dikunyah, kombinasi rasa asin kecap yang menyengat, manis gula pekat, dan pinggiran sayur yang agak hangus langsung menyerang lidah bersamaan. Kau menelannya cepat-cepat lalu menyumpit lagi."
            yutaka "Yah... rasanya cukup berkarakter, Kujo-san. Biar kuhabiskan saja sekalian."
            nar "Harumi mengerjap pelan di balik kacamatanya, mengamati caramu bertahan mengunyah dengan sorot curiga yang sangat rasional."
            harumi "Sampai habis, Kisaragi-kun? Tunggu dulu—dari aromanya saja aku masih belum yakin dengan rasanya."
            nar "Ia mengambil sumpit cadangan dari nampan lalu mencicipi satu potong kecil dari tepi piring. Raut wajahnya tidak berubah sedikit pun—tidak mengernyit, tidak berseru—tetapi sedetik kemudian tangannya langsung menggeser piring itu menjauh dari jangkauanmu."
            harumi "Cukup. Berhenti sekarang."
            yutaka "Eh, masih sisa sedikit lagi nih—"
            harumi "Kesediaanmu makan bukan bukti rasanya baik. Kadar garam dan gulanya jelas di luar rentang yang layak. Ini tidak seharusnya dilanjutkan."
            nar "Ia segera menuangkan segelas air dingin dari teko di nampan dan mendorongnya ke depanmu dengan wajah sedikit kaku karena merasa bersalah."
            harumi "Terima kasih sudah mencoba menghargai, Kisaragi-kun. Tapi kamu tidak perlu melanjutkan pengorbanan ini."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kau mengambil satu potongan kecil dengan hati-hati, mengunyahnya perlahan, lalu meneguk sedikit air sebelum menatap Harumi dengan jujur."
            chiasa "Maaf, Kujo-senpai, aku jawab jujur saja ya—bagian asin kecap sama manisnya tabrakan terlalu kuat di lidah. Terus karena apinya tadi dibesarkan, bagian luarnya agak gosong sementara bumbunya belum meresap rata."
            nar "Alih-alih terlihat kecewa atau tersinggung, sorot mata Harumi di balik kacamatanya justru tampak jauh lebih tenang. Ia langsung mengambil pensil yang terselip di buku catatannya dan mulai menulis cepat."
            harumi "Rasio kecap terlalu tinggi, gula tidak seimbang, dan suhu terlalu panas di awal. Berarti ada tiga variabel yang perlu kuubah. Terima kasih sudah mencobanya dan memberi laporan yang jelas, Amamiya-san."
            nar "Ia kemudian mengambil sumpit cadangan dan mencicipi potongan yang sama dari piring itu agar tidak sekadar menerima penilaianmu mentah-mentah. Begitu merasakannya sendiri, ia mengangguk pelan dengan wajah datar."
            harumi "...Ya. Data di lidahku cocok dengan penjelasanmu. Bahkan lebih asin daripada perkiraanku."
            chiasa "Kalau apinya dikecilkan sedikit dan bumbunya dimasukkan bertahap sesuai resep, harusnya langsung jauh lebih enak kok, Senpai."
            harumi "Masuk akal. Kalau tadi kamu cuma bilang 'enak' demi kesopanan, aku tidak akan tahu bagian mana yang salah dan mungkin akan mengulang kesalahan yang sama minggu depan."
            nar "Ia membetulkan letak kacamatanya dengan ekspresi lega yang tulus—baginya, kritik yang jujur dan bisa dipakai memahami hasil jauh lebih melegakan daripada pujian kosong."
        else:
            nar "Kau menyumpit satu potongan kecil, mengunyahnya pelan, lalu menaruh sumpit di pinggir piring dan menatap Harumi dengan nada terus terang."
            yutaka "Jujur saja ya, Kujo-san—asin kecap sama manis gulanya tabrakan terlalu keras di lidah. Terus karena apinya kebesaran di awal, luarnya keburu hangus sementara bumbunya belum meresap."
            nar "Alih-alih tersinggung, ekspresi Harumi justru langsung tampak jauh lebih lega. Ia segera mengambil pensil dari jepitan buku catatannya dan mencatat penjelasanmu dengan huruf rapi."
            harumi "Rasio kecap berlebihan, gula tidak seimbang, dan suhu terlalu tinggi di tahap awal. Berarti ada yang jelas perlu kuubah. Terima kasih sudah mencobanya, Kisaragi-kun."
            nar "Ia kemudian mencicipi bagian yang persis sama dengan sumpit cadangan agar tidak sekadar menerima penilaianmu tanpa verifikasi sendiri. Setelah menelannya, ia mengangguk singkat."
            harumi "...Ya. Hasilnya cocok dengan catatanmu. Bahkan lebih menyengat daripada perkiraanku."
            yutaka "Kalau apinya dikecilkan sedikit dan bumbunya dimasukkan bertahap sesuai urutan resep, harusnya langsung beres kok."
            harumi "Masuk akal. Kalau kamu tadi memuji demi kesopanan, aku tidak akan bisa memperbaiki apa pun. Kritik yang jelas jauh lebih membantu."
            nar "Ia membetulkan letak kacamatanya dengan raut puas yang tenang—baginya, kejujuran yang bisa dipakai memahami hasil jauh lebih berharga daripada pujian kosong."
    else:
        if kk_host == "chiasa":
            nar "Kau mencicipi sedikit ujung sendok bumbunya, mengernyit tipis, lalu melirik bahan-bahan segar yang rupanya masih tersisa cukup banyak di meja dapur belakang Harumi."
            chiasa "Kujo-senpai, bahannya kan masih ada sisa setengah lagi di dekat kompor. Gimana kalau kita bikin percobaan kedua sekarang bareng-bareng? Biar aku ikut bantu jaga api sama cicipi di tengah jalan."
            nar "Harumi terdiam sejenak, memandang sisa sayuran di meja dapur lalu kembali menatapmu dengan mata berbinar tipis."
            harumi "Dua orang untuk satu percobaan. Itu... ide yang rasional. Kalau begitu kamu yang cicipi dulu di setiap tahap sebelum aku menambahkan bumbu lagi, Amamiya-san."
            chiasa "Siap. Tapi buku catatannya ditaruh agak jauh dulu dari wajan biar nggak kena cipratan minyak, ya."
            nar "Lima belas menit berikutnya di dapur asrama berubah jauh lebih hidup daripada suasana tenang biasanya. Kau mengambil alih urusan menjaga api kompor tetap kecil dan mengaduk wajan, sementara Harumi menakar bumbu di sebelahmu sambil terus berdebat ringan soal istilah resep."
            harumi "Di sini tertulis 'garam secukupnya'. Berapa gram definisi 'secukupnya' menurutmu, Amamiya-san?"
            chiasa "Nggak usah ditimbang pakai gram, Senpai—cukup sejumput pakai ujung jari, aduk, terus kita cicipi. Kalau kurang baru tambah lagi."
            harumi "Metode trial-and-error tanpa standar awal itu tidak efisien... tapi baiklah, aku coba ikuti caramu kali ini."
            nar "Ia menaburkan sejumput kecil garam dengan gerakan yang begitu hati-hati seolah sedang menuang reagen kimia, sampai kau tidak tahan untuk tertawa kecil. Melihatmu tertawa, sudut bibir Harumi ikut terangkat—senyum tipis yang tulus muncul bahkan sebelum masakan keduanya selesai matang."
            harumi "...Ternyata bagian yang menyenangkan dari memasak tidak harus menunggu hasil akhirnya jadi sempurna dulu. Aku baru tahu."
            chiasa "Nah, coba sekarang dicicipi sedikit, Senpai. Jauh lebih mendingan kan?"
            nar "Harumi mencicipi sesendok kecil kuahnya, mengangguk pelan dengan raut wajah puas yang hangat—dan aroma dapur sore itu akhirnya benar-benar tercium seperti makanan rumahan yang layak dinikmati bersama."
        else:
            nar "Kau mencicipi sedikit ujung kuahnya, mengernyit tipis, lalu melirik lewat jendela samping dapur bersama yang terbuka—masih ada sisa bahan segar di atas meja dapur di dalam."
            yutaka "Masih ada sisa bahannya kan, Kujo-san? Aku memang nggak boleh masuk ke dalam area dapur asrama, tapi kalau aku berdiri di dekat jendela samping sini buat jaga-jaga dan cicipi tiap tahap sebelum kau tambahin bumbu lagi, gimana? Kita bikin percobaan kedua bareng."
            nar "Harumi menoleh ke arah jendela lebar yang menghubungkan konter dapur dengan teras ruang tamu, lalu kembali menatapmu dengan mata berbinar tipis."
            harumi "Dua orang untuk satu percobaan—satu di depan kompor, satu sebagai penguji rasa di jendela. Itu cukup rasional. Kalau begitu kamu cicipi dulu setiap kali aku memasukkan bumbu, sebelum aku menambahkannya lagi."
            yutaka "Deal. Tapi jauhkan dulu buku catatanmu dari kompor biar nggak ikut gosong."
            nar "Lima belas menit berikutnya berubah menjadi adegan yang jauh lebih hangat dan konyol daripada bayanganmu. Kau bersandar santai di kusen jendela luar dapur, menerima sendok kecil cicipan yang Harumi ulurkan setiap beberapa menit sambil berdebat ringan soal istilah resep."
            harumi "Di resep tertulis 'garam secukupnya'. Kisaragi-kun, secara kuantitatif berapa gram batas 'secukupnya' itu?"
            yutaka "Nggak ada gramnya, Kujo-san—ambil sejumput pakai ujung jari, aduk, terus sodorkan ke sini biar kucicipi. Kalau kurang baru tambah lagi."
            harumi "Metode coba-coba tanpa angka awal itu sangat tidak terukur... tapi baiklah, aku coba ikuti caramu."
            nar "Melihatnya menaburkan sejumput garam dengan ketegangan seolah sedang mencampur larutan kimia membuatmu tidak tahan untuk tertawa kecil. Mendengar tawamu dari balik jendela, sudut bibir Harumi ikut terangkat—senyum tipis yang tulus muncul bahkan sebelum masakan keduanya selesai matang."
            harumi "...Ternyata bagian yang menyenangkan tidak harus menunggu hasil akhirnya jadi sempurna dulu. Aku baru tahu."
            yutaka "Nah, coba sekarang kau sendiri yang cicipi. Beda jauh kan?"
            nar "Harumi mencicipi sesendok kecil dari wajan, lalu mengangguk pelan dengan raut puas yang hangat—dan aroma yang keluar dari jendela dapur sore itu akhirnya benar-benar tercium seperti masakan rumah yang layak dinikmati bersama."
    return

# ┌─ PANDUAN CERITA · H-D05 · Masakan Kedua
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kujo Harumi
# │ AWALAN  : H03-C pernah terjadi
# │ INTI    : A Puji dengan spesifik / B jujur / C ajak memasak lagi
# │ AKHIRAN : ia menghubungkan "senang" dengan "memasak bersama"; kejelasan +
# └─ tulis / perbaiki dialog di bawah ──
label kk_second_meal:
    nar "Kali ini Harumi menyiapkan porsi lebih kecil dan tidak menaruh catatan resep di meja. Ia ingin mendengar reaksi sebelum menjelaskan apa yang sudah diubah."
    harumi "Aku mengulang masakan kita. Tadi hampir mengirim foto, lalu memutuskan ingin melihatmu mencicipi langsung."
    call kk_family_menu("H-D05", ["Tunjukkan rasa yang kali ini lebih seimbang.", "Katakan dengan jujur apa yang masih kurang.", "Ajak dia memasak bersama lagi."])
    if _return == "A":
        harumi "Kau juga bisa merasakan bedanya. Aku senang."
        nar "Ia mengulang kata senang setelah menyebutnya, seolah memeriksa bahwa akhirnya menemukan nama yang tepat. Lalu ia mengambil porsi sendiri agar tidak hanya duduk menunggu penilaianmu."
    elif _return == "B":
        harumi "Aku ingin mencobanya lagi. Rupanya aku menyukai bagian ini."
        nar "Kritikmu tidak menghapus kegembiraannya kali ini. Ia menanyakan satu perbaikan dan menyisakan sisanya untuk kesempatan lain, tidak lagi menganggap setiap kekurangan harus selesai sebelum ia boleh menikmati makan bersama."
    else:
        harumi "Boleh. Aku lebih senang waktu kita membuatnya bersama."
        nar "Ia tidak mengoreksi kalimat tersebut menjadi alasan teknis. Kalian memilih hari, membagi bahan, dan menyadari jadwal yang disepakati sudah cukup untuk membuatnya tersenyum hari ini."
    $ kk_minutes(10)
    return

init 1 python:
    _hook("H-D05-A", lambda: kk_adj("kejelasan_harumi",10))
    _hook("H-D05-B", lambda: kk_adj("kejelasan_harumi",5))
    _hook("H-D05-C", lambda: kk_adj("kejelasan_harumi",10))

    def kk_harumi_ending():
        if kk_has("lock_romance_harumi"):
            return None
        if kk_has("force_harumi"):
            return "E-HA-12"
        # Koita memilih Harumi (K26).
        if kk_has("koita_pilih_harumi"):
            return "E-HA-04"
        # Rute Ogawa (hanya bila gerbang H06+ ditempuh).
        if kk_has("ogawa_aktif"):
            if kk_get("validasi_pemain", 0) >= 60 and kk_has("harumi_dimanfaatkan"):
                return "E-HA-10"
            if kk_has("ogawa_dihentikan"):
                return "E-HA-03" if kk_has("harumi_tetap_kouseikan") else "E-HA-07"
            if kk_has("ogawa_lolos") or kk_get("cengkeraman_ogawa", 0) >= 60:
                return "E-HA-08"
            if kk_has("harumi_titik_tanpa_balik"):
                return "E-HA-06"
            if kk_has("harumi_menjauh_ogawa") and kk_get("kejelasan_harumi") >= 50:
                return "E-HA-02"
            if kk_has("harumi_dimanfaatkan"):
                return "E-HA-05"
        # Romantis.
        if kk_has("harumi_ikut_luar"):
            return "E-HA-14"
        if kk_host == "chiasa" and kk_has("harumi_chiasa_kolaborasi"):
            return "E-HA-13"
        if (kk_get("kejelasan_harumi") >= 60 and kk_has("harumi_dibantu_menamai_emosi")
                and not kk_has("force_pernah")):
            return "E-HA-01"
        if kk_get("orang_tua_kujo", 30) >= 60 and not kk_has("force_pernah"):
            return "E-HA-09"
        # Netral: kejelasan tinggi tapi hati tidak ke siapa pun.
        if kk_get("kejelasan_harumi") >= 60 and not kk_has("harumi_kencan_biasa"):
            return "E-HA-11"
        return None
