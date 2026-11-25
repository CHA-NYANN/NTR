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
        nar "Di luar jendela kaca lebar lantai dua Gedung Sains & Lab, puncak-puncak pohon sakura bergoyang diterpa angin pagi pertengahan April sementara suara obrolan mahasiswa yang mulai menggelar terpal Hanami terdengar samar dari kejauhan. Di dalam ruang baca ini, suasana nyaris sunyi sepenuhnya."
        nar "Sinar matahari pagi miring menembus kaca dan menyoroti butiran debu halus di antara rak buku tinggi. Hanya terdengar dengung halus pendingin ruangan, bau kertas buku referensi yang kering, sesekali bunyi halaman dibalik di baris rak jauh, serta goresan pelan ujung pensil mekanik di atas kertas."
        nar "Kamu melangkah pelan menyusuri lorong di antara rak-rak tinggi untuk mencari buku referensi teori warna dan komposisi optik yang kebetulan tersimpan di bagian arsip lintas bidang. Begitu melewati deretan rak paling ujung dekat jendela sudut, langkahmu terhenti."
        nar "Di meja baca yang paling dekat dengan cahaya pagi pucat itu, seorang mahasiswi duduk sendirian menghadap buku teks tebal terbuka yang tepinya dipenuhi pembatas kertas kecil berwarna biru dan abu-abu. Rambut abu-abunya yang agak panjang diikat satu menyamping hingga menjuntai rapi ke depan bahu kiri. Ia mengenakan kardigan abu-abu sederhana di atas kemeja putih bersih."
        nar "Dialah Kujo Harumi, mahasiswi tahun kedua yang wajahnya baru sempat kamu kenal sepintas dari lingkar pertemanan Koita. Dari caranya duduk tegak dan fokus penuh pada bukunya, ia terkesan tenang dan tidak banyak bicara."
        nar "Satu jari tangan kirinya menahan tepi halaman buku agar tidak menutup, sementara tangan kanannya berulang kali menuliskan deretan angka dan tanda panah kecil pada buku catatan bersampul hitam di sebelahnya. Kotak isi ulang pensil mekanik, penghapus putih, dan penggaris bening tersusun sejajar sempurna di pinggir atas meja. Setiap beberapa saat, ia menaikkan bingkai kacamatanya dengan ujung jari tengah tanpa sedikit pun mengalihkan pandangan dari kertas."
        nar "Tepat di sampingnya, sebuah kursi kayu tampak sedikit tertarik keluar dari kolong meja, entah bekas seseorang yang baru saja beranjak pergi atau ruang kosong yang memang dibiarkan terbuka."
        nar "Belum sempat kamu memutuskan apakah akan langsung berbelok ke rak di belakangnya, mata biru tua di balik kacamata itu naik sekilas menangkap bayanganmu yang berdiri di ujung meja."
        harumi "Amamiya-san, ya?"
        nar "Suaranya pelan, datar, dan terjaga rapi menyesuaikan keheningan ruang baca, sama sekali tidak terdengar kesal karena terganggu."
        chiasa "Selamat pagi, Kujo-senpai. Maaf kalau langkahku bikin terganggu."
        harumi "Tidak. Suara langkahmu cukup pelan. Pagi ini penghuni ruang baca memang hampir tidak ada karena kebanyakan mahasiswa turun ke taman untuk persiapan Hanami."
        chiasa "Di bawah tadi memang sudah mulai ramai yang angkat terpal sama minuman. Kujo-senpai sudah lama di sini?"
        harumi "Sekitar empat puluh menit. Pagi begini jendela sebelah timur belum menyilaukan mata, jadi paling nyaman untuk memeriksa perhitungan."
        nar "Ia menoleh sekilas ke buku tebal yang sedang terbentang di hadapannya, lalu kembali menatapmu dengan tenang."
        harumi "Kalau kamu mencari buku referensi yang sedang kubuka ini, masih ada satu salinan lagi di rak baris ketiga sebelah kiri. Tapi kalau kamu sedang mencari tempat duduk... kursi di sebelahku ini belum dipakai siapa-siapa."
    else:
        nar "Di luar jendela kaca lebar lantai dua Gedung Sains & Lab, kelopak sakura berterbangan tertiup angin pagi di atas taman tempat beberapa rombongan awal mulai menyiapkan terpal Hanami. Suara mereka terdengar samar seperti dengung jauh. Sebaliknya, di dalam ruang baca ini, udara terasa dingin, kering, dan nyaris sunyi sepenuhnya."
        nar "Sinar pagi miring jatuh di antara lorong-lorong rak tinggi yang dipenuhi jilid buku referensi tua. Kamu masuk ke sini sekadar untuk menjauh sebentar dari keramaian pagi di luar sekaligus mencari buku referensi dasar yang mungkin bisa membantu menutupi banyak materi kuliah yang sama sekali tidak kamu ingat. Dengan kedua tangan masih terselip di saku jaket, langkahmu melambat di ujung lorong rak dekat jendela sudut."
        nar "Di meja baca paling pojok yang diterangi cahaya pagi pucat, duduk seorang mahasiswi berkacamata dengan rambut abu-abu agak panjang yang diikat satu menyamping hingga menjuntai ke depan bahu kirinya. Kardigan abu-abu di atas kemeja putihnya tampak serapi cara duduknya yang tegak."
        nar "Dialah Kujo Harumi, sosok yang sempat kamu lihat di foto lama dan grup obrolan teman-teman Koita. Di depan dirinya terbuka sebuah buku teks tebal berhias pembatas kertas berwarna biru dan abu-abu, berdampingan dengan kotak isi ulang pensil, penghapus putih, dan penggaris bening yang diletakkan sejajar sempurna."
        nar "Satu jari tangan kirinya menahan halaman buku agar tidak menutup, sementara tangan kanannya berulang kali menggoreskan deretan perhitungan pada buku catatan kecil bersampul hitam di sebelahnya. Sesekali ia menaikkan bingkai kacamatanya dengan ujung jari tengah tanpa sedikit pun mengangkat pandangan."
        nar "Tepat di sebelah kursinya, sebuah kursi kayu lain tampak agak tertarik keluar dari kolong meja, tidak jelas apakah bekas seseorang yang baru saja beranjak atau ruang yang memang dibiarkan terbuka."
        nar "Ketika kamu berhenti dua langkah dari ujung meja, mata biru tua di balik kacamata itu naik sekilas menangkap bayanganmu."
        harumi "Kisaragi-kun?"
        nar "Suaranya datar, pelan, dan terjaga sesuai keheningan ruang baca, sama sekali tidak terdengar terkejut maupun terganggu."
        yutaka "Pagi, Kujo-san. Tumben jam segini sudah di ruang baca, nggak ikut ke taman?"
        harumi "Pagi, Kisaragi-kun. Keramaian di taman biasanya memuncak menjelang siang, jadi aku menyelesaikan catatan praktikum di sini dulu selagi ruangan masih sepi."
        yutaka "Sudah lama di sini? Di lantai satu tadi hampir nggak ada orang lewat."
        harumi "Sekitar empat puluh menit. Cahaya pagi dari jendela timur belum terlalu terik, jadi enak untuk membaca tabel angka."
        nar "Ia menoleh singkat ke buku tebal yang terbentang di depannya, lalu menatapmu kembali dengan ekspresi tenang."
        harumi "Kalau kamu mencari buku referensi yang sedang kubuka ini, masih ada satu salinan lagi di rak baris ketiga sebelah kiri. Kalau kamu sedang mencari tempat duduk... kursi di sebelahku ini belum dipakai."
    call kk_family_menu("H01", ["Tarik kursi dan duduk di sampingnya.", "\"Sedang mengerjakan soal apa?\"", "Lewati mejanya agar ia bisa membaca dengan tenang."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu mengangguk singkat, lalu menarik kursi kayu di sebelahnya dengan sangat pelan agar kakinya tidak berdecit di atas lantai linoleum. Kamu meletakkan tas kainmu di pangkuan, mengeluarkan buku catatan tipis dan pensil, lalu duduk menghadap meja yang sama."
            chiasa "Terima kasih, Kujo-senpai. Di luar mulai ramai anak-anak menyiapkan Hanami, jadi rasanya lebih enak menepi sebentar buat baca dengan tenang di sini."
            nar "Harumi menoleh sekilas ke arah jendela kaca yang memperlihatkan mahasiswa-mahasiswa yang mulai menggelar terpal biru di taman bawah, lalu kembali menatap mejanya dengan ekspresi datar."
            harumi "Benar. Keramaian di bawah pohon sakura menghasilkan terlalu banyak kebisingan untuk membaca atau menghitung. Di sudut ini tingkat gangguannya jauh lebih rendah, dan pencahayaan paginya cukup stabil."
            nar "Tanpa perlu diminta, ia mendorong buku teks tebal di depannya beberapa sentimeter ke tengah meja agar sudut halamannya tidak tertutup bayangan lengannya, lalu merapikan kotak pensil dan penghapusnya sejajar di tepi atas supaya ruang di sisimu lapang."
            harumi "Kalau kamu mau melihat referensi di sini atau butuh ruang lebih lebar di sisi kanan, bukunya bisa kugeser ke tengah seperti ini."
            nar "Alih-alih langsung menenggelamkan wajahnya kembali ke deretan rumus, Harumi diam sejenak, menunggu dengan sabar sampai kamu selesai membuka bukumu dan menemukan posisi duduk yang nyaman."
            chiasa "Maaf kalau kehadiranku malah memecah konsentrasi Kujo-senpai. Nanti kalau sudah siang, Kujo-senpai tetap ikut turun ke Hanami?"
            harumi "Tidak terganggu. Konsentrasiku tidak serapuh itu. Dan soal Hanami, aku mungkin cuma mampir sebentar nanti kalau catatanku selesai tepat waktu."
            chiasa "Berarti Kujo-senpai lebih suka suasana sepi begini ya?"
            harumi "Bukan berarti tidak suka orang lain. Hanya saja, di ruang ramai aku butuh tenaga tambahan cuma untuk menyaring suara sekitar sebelum bisa menangkap isi percakapan."
            nar "Mata Harumi turun sekilas ke buku catatan yang baru kamu buka di atas meja, tempat terdapat beberapa catatan skema warna dan garis pembagian bidang."
            harumi "Itu catatan tentang pembiasan cahaya dan kontras warna?"
            chiasa "Iya, materi pengantar untuk kelas studio minggu depan. Ternyata penjelasannya lumayan banyak bersinggungan sama optik dasar, makanya aku cari referensinya sampai ke gedung ini."
            harumi "Kalau kamu butuh tabel panjang gelombang cahaya yang ringkas, bagian lampiran di belakang buku teks ini punya diagram yang cukup bersih. Nanti boleh kamu lihat kalau mau."
            chiasa "Wah, boleh sekali. Terima kasih, Kujo-senpai."
            nar "Ia membetulkan letak kacamatanya dengan gerakan jari yang tenang, lalu menoleh setengah badan kepadamu dengan sorot mata biru tua yang lurus dan jujur."
            harumi "Aku juga tidak keberatan dijeda kalau kamu sedang kesulitan mencari buku atau ingin menanyakan sesuatu, Amamiya-san. Aku hanya perlu diberi tahu secara langsung kalau memang ada pertanyaan, soalnya aku sering gagal membaca ekspresi orang yang sebenarnya ingin bicara."
            chiasa "Begitu ya... baik, kalau ada yang ingin kutanyakan nanti pasti langsung kubilang, Kujo-senpai."
            harumi "Bagus. Itu jauh lebih efisien daripada sama-sama menebak."
            nar "Harumi mengangguk tipis seolah kesepakatan sederhana itu sudah cukup jelas dan menenangkan baginya, lalu kembali menurunkan pandangan ke deretan perhitungannya. Kamu membuka catatanmu di bawah sinar matahari pagi yang bergeser pelan di permukaan meja kayu."
            nar "Selama beberapa belas menit berikutnya, hanya bunyi lembut goresan pensil, helaan napas teratur, dan gesekan kertas yang menemani kalian berdua di meja sudut ruang baca."
        else:
            nar "Kamu mengangguk santai, menarik kursi kayu di sebelahnya dengan pelan agar tidak menimbulkan bunyi gesekan, lalu duduk sambil meletakkan buku catatan tipis dan tasmu di samping kaki meja."
            yutaka "Makasih, Kujo-san. Di luar mulai ramai orang menyiapkan Hanami, jadi aku numpang duduk sebentar buat baca tenang di sini."
            nar "Harumi melirik sekilas ke arah jendela kaca yang memperlihatkan beberapa rombongan mahasiswa menggelar terpal biru di taman bawah, lalu kembali menatap mejanya dengan wajah datar."
            harumi "Masuk akal. Tingkat kebisingan di taman pagi ini mulai naik dan tidak cocok untuk berkonsentrasi."
            nar "Tanpa diminta, ia menggeser buku teks tebal di hadapannya beberapa sentimeter ke tengah meja agar ruang di sisimu lebih lega, lalu merapikan penghapus dan kotak pensilnya sejajar di tepi atas."
            harumi "Kalau kamu mau ikut melihat atau butuh ruang menulis di sebelah kanan, bukunya bisa kugeser ke tengah seperti ini."
            nar "Ia benar-benar menunggu dengan tenang sampai kamu selesai membuka buku catatanmu dan duduk nyaman, tanpa terburu-buru kembali membenamkan wajah ke bacaan."
            yutaka "Tidak apa-apa kalau aku di sini? Takutnya malah mengganggu ritme belajarmu."
            harumi "Tidak. Konsentrasiku tidak terganggu oleh orang yang duduk diam. Dulu waktu kelompok belajar juga kamu sering diam dulu lumayan lama sebelum bertanya."
            nar "Kalimat pendek itu memberimu satu petunjuk berharga tentang bagaimana pemilik asli tubuh ini biasanya bersikap di depan Harumi. Kamu mengangguk santai seolah mengingat kebiasaan yang sama."
            yutaka "Nanti siang kamu ikut turun ke Hanami, Kujo-san?"
            harumi "Mungkin mampir sebentar setelah bab ini selesai. Di keramaian aku biasanya butuh tenaga lebih banyak hanya untuk menyaring suara sekitar sebelum bisa mengikuti obrolan."
            nar "Pandangan Harumi sempat singgah sebentar pada halaman buku catatan kuliah yang kamu buka di atas meja, penuh deretan grafik keseimbangan yang tampak rumit."
            harumi "Kamu sedang mengulang materi statistik dasar?"
            yutaka "Iya, sekalian menyegarkan ingatan sebelum tugas kelompok mulai banyak minggu depan."
            harumi "Di bagian indeks belakang perpustakaan ini ada modul ringkasan probabilitas yang contoh soalnya jauh lebih runtut daripada buku wajib fakultasmu. Kalau nanti butuh, bilang saja, aku hafal nomor raknya."
            yutaka "Serius? Itu bakal membantu banget."
            nar "Ia membetulkan letak kacamatanya dengan ujung jari tengah, lalu menoleh setengah badan kepadamu dengan tatapan yang jernih dan lurus."
            harumi "Aku juga tidak keberatan dijeda kalau ada yang mau ditanyakan, Kisaragi-kun. Hanya saja, katakan langsung kalau ada pertanyaan, karena aku kurang pandai menebak dari ekspresi wajah."
            yutaka "Oke, dicatat. Nanti pasti langsung kubilang kalau aku mentok di bagian tertentu."
            harumi "Baik. Itu jauh lebih efisien daripada sama-sama menebak."
            nar "Harumi mengangguk pelan seolah kesepakatan lurus itu sudah menenangkan pikirannya, lalu kembali menurunkan pandangannya ke kertas hitungannya sementara kamu membuka halaman pertama buku catatanmu."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Alih-alih langsung duduk, kamu berhenti di ujung meja dan mencondongkan badan sedikit sambil melirik barisan persamaan, tanda panah koreksi, serta grafik kecil yang digambar sangat rapi di buku catatan hitamnya."
            chiasa "Permisi, Kujo-senpai. Kelihatannya sejak tadi Kujo-senpai mengulang baris perhitungan yang sama berkali-kali. Sedang mengerjakan soal apa?"
            nar "Ujung pensil mekanik Harumi terhenti tepat di atas sebuah angka. Ia tidak langsung menjawab. Pandangannya tetap tertuju pada baris terakhir tulisannya selama beberapa detik penuh sambil ia mengangkat sedikit telunjuk tangan kirinya memberi isyarat."
            harumi "Sebentar. Aku masih memeriksa bagian akhir jawabannya."
            nar "Caranya memintamu menunggu sama sekali tidak terasa angkuh. Kamu memperhatikan bibirnya bergerak menggumamkan dua perbandingan angka tanpa suara, lalu ia mencoret satu baris kecil di pinggir kertas dan menuliskan angka pembanding baru dengan hati-hati. Jelas ia menolak menjelaskan sebuah kesimpulan sebelum ia sendiri yakin akan ketepatannya."
            nar "Sepuluh detik kemudian, ia menghela napas tipis, meletakkan pensil mekaniknya sejajar tepi buku, membetulkan kacamata, lalu memutar buku catatan hitamnya sembilan puluh derajat menghadap ke arahmu."
            harumi "Sudah. Ada satu variabel pada contoh soal di buku ini yang hasilnya tidak konsisten dengan grafiknya, jadi aku mengujinya ulang dari awal. Bagian mana yang ingin kamu tahu dulu, Amamiya-san?"
            chiasa "Grafik lengkung kecil di pojok bawah itu kelihatannya menarik, kalau tidak merepotkan Kujo-senpai."
            harumi "Tidak merepotkan. Untung kamu langsung menunjuk bagiannya, soalnya aku sering mulai menjelaskan terlalu jauh dari teori dasar kalau tidak ditanya secara spesifik."
            nar "Ia menarik kursi kosong di sebelahnya beberapa sentimeter lebih dekat agar kamu bisa duduk atau membungkuk melihat dengan nyaman, lalu menunjuk garis kurva itu dengan ujung belakang pensilnya."
            harumi "Coba lihat titik tekukan di tengah ini. Bayangkan seperti gradasi cahaya pada permukaan melengkung. Kalau nilai di baris sebelumnya berubah tiba-tiba, garisnya seharusnya patah tajam di sini. Di buku teks tercetak mulus karena penyuntingnya membulatkan angka terlalu cepat."
            chiasa "Oh... pantas saja tadi Kujo-senpai sampai menghitung ulang di kertas terpisah. Padahal kalau dilihat sepintas, garis cetakan di buku kelihatan rapi dan benar-benar saja."
            nar "Harumi mengerjap sesaat mendengar tanggapanmu, seolah tidak menyangka kamu benar-benar mengikuti penjelasannya sampai ke titik itu alih-alih sekadar mengangguk sopan."
            chiasa "Memangnya kesalahan cetak seperti itu sering ada di buku referensi kampus, Senpai?"
            harumi "Cukup sering di cetakan pertama. Penerbit kadang terburu-buru mengejar jadwal awal semester, jadi grafik ilustrasinya dirapikan tanpa mengecek ulang baris hitungannya. Kalau orang hanya menghafal bentuk kurvanya tanpa memeriksa prosesnya, kesalahan kecil itu terbawa sampai ujian."
            nar "Ia membalik satu halaman buku catatannya ke belakang, memperlihatkan dua kurva pembanding yang ia gambar sendiri dengan penggaris bening, lalu melirikmu dengan rasa ingin tahu yang tenang."
            harumi "Kalau memakai sudut pandangmu yang terbiasa membaca proporsi garis, antara kurva atas dan kurva bawah ini, mana yang menurutmu lebih masuk akal mengikuti angka di kolom kiri?"
            nar "Kamu mencondongkan badan sedikit, membandingkan lonjakan angka di tabel kiri dengan kedua gambar garisnya, lalu menunjuk titik potong pada kurva bawah."
            chiasa "Yang bawah, Kujo-senpai. Di baris keempat lonjakannya hampir dua kali lipat, jadi sudut naiknya harusnya jauh lebih curam daripada gambar yang atas."
            nar "Bahu Harumi tampak rileks tipis, dan seberkas senyum sangat kecil hampir tak terlihat muncul di sudut bibirnya."
            harumi "...Ya, persis seperti itu. Pengamatanmu cepat juga, Amamiya-san. Aku tidak menyangka penjelasanku barusan langsung bisa dipakai melihat baris berikutnya."
            chiasa "Penjelasan Kujo-senpai tadi pakai perumpamaan cahaya, jadi langsung kebayang bentuknya."
            harumi "Kalau kamu mau melihat dua halaman berikutnya, silakan duduk saja. Ini ada selembar kertas kotak-kotak cadangan kalau mau ikut mencatat."
            nar "Ia mendorong kursi kayu itu sedikit lagi ke arahmu bersama selembar kertas rapi dari mapnya. Kamu menarik kursi dan duduk untuk mendengarkan penjelasannya yang pelan, teratur, dan sama sekali tidak terasa menggurui."
        else:
            nar "Kamu berhenti di tepi meja sambil menumpukan sebelah tangan ringan di sandaran kursi kosong dan melirik deretan angka serta coretan koreksi di buku catatan hitamnya."
            yutaka "Dari tadi kelihatannya kamu mengulang baris yang sama terus, Kujo-san. Lagi mengerjakan soal apa?"
            nar "Ujung pensil mekanik Harumi berhenti di atas kertas. Ia tidak langsung menoleh. Pandangannya bertahan pada baris terakhir hitungannya selama beberapa detik penuh sambil mengangkat sedikit telunjuk tangan kirinya."
            harumi "Sebentar. Aku masih memeriksa bagian akhir jawabannya."
            nar "Caranya memintamu menunggu sama sekali tidak terasa seperti orang yang sedang pamer kepandaian. Kamu melihatnya mencoret satu angka pembulatan, menggumamkan perbandingan pelan tanpa suara, lalu menuliskan ulang hasil akhirnya untuk memastikan kesimpulannya tidak meleset."
            nar "Setelah memastikan angkanya cocok, ia meletakkan pensilnya sejajar tepi buku, membetulkan kacamata, lalu memutar buku catatannya menghadap ke arahmu agar mudah dibaca."
            harumi "Sudah selesai. Ada satu tabel tren di buku ini yang selisih datanya meleset dari rumus pengantarnya, jadi aku menghitung ulang untuk memastikan mana yang salah cetak. Bagian mana yang ingin kamu lihat dulu, Kisaragi-kun?"
            yutaka "Bagian selisih tabel yang kamu coret di tengah itu. Kenapa di bukunya malah kelihatan rata?"
            harumi "Untung kamu langsung menunjuk intinya, karena aku sering mulai menjelaskan terlalu jauh dari definisi awal kalau tidak ditanya secara spesifik."
            nar "Ia menunjuk dua kolom angka di kertasnya dengan ujung belakang pensil mekanik."
            harumi "Di kolom ketiga, penulisnya membuang angka di belakang koma sebelum mengalikannya ke baris bawah. Untuk contoh singkat mungkin kelihatan sepele, tapi kalau dipakai membaca tren jangka panjang, arah grafiknya langsung melenceng jauh."
            yutaka "Oh... berarti kalau cuma menghafal hasil akhirnya tanpa mengecek langkah tengahnya, pasti ikut salah semua waktu dipakai di kasus lain."
            nar "Harumi mengedip pelan, seolah sedikit terkejut kamu menangkap celah praktisnya secepat itu."
            yutaka "Tapi kok kamu bisa langsung curiga tabel cetakan resmi salah? Biasanya orang langsung percaya saja kalau sudah masuk buku teks."
            harumi "Kalau kurva di halaman berikutnya tidak cocok dengan besar perubahan di baris kedua, pasti ada angka yang dipotong paksa. Aku cuma terbiasa menghitung ulang satu baris sampel sebelum memakai rumusnya."
            nar "Ia membalik satu lembar buku catatannya, memperlihatkan dua kolom pembanding yang sudah ia susun ulang, lalu menatapmu tenang."
            harumi "Coba lihat baris kelima di halaman ini. Menurutmu selisih angka cetakannya masih bisa ditoleransi atau sudah membalik kesimpulan?"
            nar "Kamu menunduk memeriksa deretan angka yang sudah ia tandai dengan panah kecil, lalu menunjuk tanda minus yang mendadak berubah menjadi positif di kolom kanan."
            yutaka "Sudah membalik kesimpulan. Kalau trennya berubah arah cuma gara-gara pembulatan di baris ketiga, berarti contoh soal ini memang jebakan kalau langsung disalin."
            harumi "...Benar. Kamu menangkap polanya lebih cepat daripada dugaanku, Kisaragi-kun. Kebiasaan mengecek langkah tengah seperti itu lumayan jarang dipakai orang kalau sedang buru-buru mengejar ujian."
            yutaka "Lagipula penjelasanmu juga langsung ke intinya, jadi gampang diikuti."
            harumi "Kalau mau duduk dan lihat bagian selanjutnya, silakan. Ini ada kertas coretan cadangan kalau kamu butuh."
            nar "Harumi menggeser kursi kayu di sebelahnya sedikit ke arahmu bersama selembar kertas kotak-kotak dari mapnya. Kamu menarik kursi itu dan duduk di sisinya untuk melihat lembaran catatan berikutnya, menemukan cara berpikirnya yang jujur dan presisi terasa sangat menyegarkan."
    else:
        if kk_host == "chiasa":
            nar "Kamu menatap sekilas lembaran perhitungan yang terbentang rapi di atas meja, lalu memutuskan tidak memecah ketenangan belajarnya pagi ini. Kamu tersenyum tipis dan membungkuk kecil dengan sopan."
            chiasa "Terima kasih tawarannya, Kujo-senpai. Aku cuma lewat mau mengambil buku di rak belakang saja, tidak enak kalau sampai mengganggu waktu bacanya pagi-pagi begini."
            nar "Harumi mempertahankan tatapannya padamu selama satu detik penuh, seolah benar-benar ingin memastikan kamu tidak sedang menolak karena sungkan atau bingung mencari rak."
            harumi "Kamu yakin tidak butuh petunjuk letak raknya? Penomoran di lantai ini agak berbeda dengan perpustakaan pusat, dan beberapa mahasiswa tahun pertama sering memutar dua kali mencari katalog lintas bidang."
            chiasa "Oh, begitu ya? Tadi aku sempat lihat denah di pintu masuk, tapi memang cuma sekilas. Aku lagi cari buku teori warna sama optik dasar."
            harumi "Kalau begitu masuk ke lorong sebelah kanan setelah meja ini, lalu cek rak keempat dari depan. Edisi lamanya yang bergambar lengkap biasanya ditaruh di papan paling bawah."
            chiasa "Wah, rinci sekali. Untung tadi Kujo-senpai kasih tahu, kalau nggak pasti aku cari di rak atas terus. Terima kasih banyak ya, Kujo-senpai."
            harumi "Sama-sama. Silakan, Amamiya-san."
            nar "Ia mengangguk singkat dengan sopan. Kamu melanjutkan langkah melewati mejanya menuju deretan rak belakang yang teduh dan langsung menemukan jilid buku yang dimaksud di papan bawah persis seperti petunjuknya."
            nar "Ketika beberapa menit kemudian kamu membawa buku itu melangkah keluar dari ujung lorong dan sempat melirik sekali lagi ke arah meja sudut, Harumi sudah kembali menundukkan kepala dengan satu jari menahan halaman buku teksnya. Kursi kayu di sebelahnya tetap tertarik sedikit keluar dalam keadaan kosong di bawah cahaya pagi."
        else:
            nar "Kamu melirik sekilas lembaran hitungan yang tersusun begitu rapi di depannya, lalu memutuskan tidak memotong konsentrasinya pagi ini. Kamu mengangkat satu tangan singkat sebagai isyarat sopan."
            yutaka "Makasih, Kujo-san. Aku cuma lewat mau cari buku di rak belakang saja, nggak usah terganggu."
            nar "Harumi menatapmu satu detik lebih lama, seolah benar-benar memeriksa apakah kamu sedang butuh petunjuk atau memang berniat lewat saja."
            harumi "Baiklah. Penomoran rak di gedung ini sedikit berbeda dengan perpustakaan pusat. Kalau kamu mencari buku pengantar statistik atau referensi kuantitatif umum, letaknya di lorong kedua sebelah kanan."
            yutaka "Oh, pas sekali, aku memang lagi cari rak pengantar statistik buat mengulang materi lama."
            harumi "Ambil yang jilid sampul biru tua di rak tengah. Edisi merah yang paling depan terlalu ringkas dan banyak melewatkan langkah pembuktian."
            yutaka "Wah, makasih banyak infonya, Kujo-san. Lumayan menghemat waktu cari-cari. Duluan ya."
            harumi "Sama-sama. Silakan, Kisaragi-kun."
            nar "Kamu melanjutkan langkah menyusuri deretan rak tinggi yang berbau kertas tua dan langsung menemukan jilid biru tua yang ia sebutkan tanpa kesulitan. Beberapa menit kemudian saat kamu melirik balik dari ujung lorong dengan buku di tangan, Harumi sudah kembali menunduk menahan halaman bukunya dengan satu jari, sementara kursi kosong di sebelahnya tetap tidak tersentuh."
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
    if kk_host == "chiasa":
        nar "Pelataran kuil pada hari-hari pertama Tahun Baru masih dipenuhi lalu lalang pengunjung yang mengenakan mantel tebal dan syal wol. Di tepi halaman dekat rak kayu pengikat omikuji, Kujo Harumi berdiri agak menyamping agar tidak menghalangi orang lewat sambil memegangi selembar kertas ramalan yang baru ia ambil."
        nar "Cara ia membaca kertas putih tipis itu sama sekali tidak terlihat seperti orang yang sedang mencari hiburan Tahun Baru. Alisnya sedikit berkerut, kacamatanya sempat dinaikkan sekali, dan ia membacakan tiap barisnya dengan nada terukur layaknya memeriksa prosedur lembar praktikum."
        harumi "Keberuntungan umumnya sedang. Di bagian studi dan riset tertulis ketekunan pada rincian kecil akan membuahkan hasil sebelum musim panas. Bagian kesehatan menyarankan agar tidak mengurangi waktu tidur demi pekerjaan yang bisa dibagi. Semua bagian itu cukup masuk akal dan punya indikator yang jelas."
        chiasa "Bagus dong hasilnya, Kujo-senpai. Lengkap banget dibaca sampai kayak lagi ngecek catatan praktikum. Punyaku tadi cuma kubaca bagian atasnya terus langsung kulipat."
        harumi "Kalau sudah membayar seratus yen untuk satu lembar data cetak, sayang sekali kalau tidak dibaca sampai baris terakhir."
        chiasa "Haha, iya juga sih. Terus yang bagian bawahnya soal hubungan atau perasaan gimana?"
        nar "Harumi tidak langsung menjawab. Pandangannya menempel di kolom tengah kertas tersebut. Kamu melihat bibirnya bergerak pelan membaca baris yang sama untuk kedua kalinya, lalu ketiga kalinya."
        harumi "'Perhatikan hatimu.'"
        chiasa "Cuma dua kata itu aja, Senpai?"
        harumi "Di bawahnya ada tambahan singkat yang berbunyi, 'jangan menunggu semuanya selesai baru menyadari apa yang tertinggal.' Kalau itu dimaksudkan sebagai instruksi, kriterianya sangat buruk dan sama sekali tidak terukur."
        nar "Meski mengkritiknya secara logis, Harumi sama sekali belum melipat kertas itu. Ia menurunkan sedikit tangannya lalu melirik keramaian pengunjung di sekitar kuil."
        harumi "Tapi terus terang, Amamiya-san... aku tetap ingin tahu apa maksudnya. Selama ini aku memang punya kebiasaan yang cukup mengganggu. Aku sering baru sadar kalau diriku sebenarnya sedang sedih, lelah, atau kecewa beberapa jam setelah semua orang sudah pulang dan ruangannya kembali kosong."
        chiasa "Jadi waktu acaranya lagi jalan, Kujo-senpai sama sekali nggak kerasa?"
        harumi "Waktu itu pikiranku sibuk memastikan semuanya berjalan sesuai urutan. Baru malamnya di asrama aku duduk terdiam dan sadar ada bagian yang tertinggal. Karena itulah dua baris ini agak mengusikku."
        chiasa "Memangnya waktu di buku catatan hitam Senpai, kolom buat perasaan pribadi itu biasanya ditulis gimana?"
        harumi "Biasanya kukosongkan dulu sampai aku menemukan definisi kata yang paling tepat. Masalahnya, sering kali sampai minggunya berganti pun aku masih belum yakin apakah yang kurasakan itu rindu, cemas, atau sekadar kelelahan fisik."
        chiasa "Kalau harus menunggu yakin seratus persen sama istilahnya dulu, pantas saja Senpai sering merasa terlambat menyadarinya."
        harumi "Itulah kelemahan metodologiku selama ini, Amamiya-san. Aku terlalu terbiasa dengan parameter laboratorium yang pasti, sedangkan reaksi di dalam kepala sendiri tidak punya satuan ukur yang baku."
        nar "Angin musim dingin yang bertiup dari sela pepohonan kuil menggerakkan ujung kertas omikuji di jari Harumi."
        nar "Ia menatapmu dari balik lensa kacamatanya dengan kesungguhan seseorang yang benar-benar sedang mencari cara memahami dirinya sendiri."
        chiasa "Tapi fakta kalau Senpai sekarang langsung berhenti dan memikirkan kalimat di kertas itu berarti Senpai sebenarnya peduli sama apa yang Senpai rasakan."
        harumi "Aku memang ingin memperbaikinya tahun ini, Amamiya-san. Aku hanya belum menemukan metode latihan yang praktis."
        chiasa "Namanya belajar mengenali perasaan sendiri kan memang nggak bisa selesai dalam sehari, Senpai."
        harumi "Itu benar. Proses pengamatan jangka panjang selalu membutuhkan tahapan bertahap."
        nar "Harumi memegang kedua tepi kertas omikuji itu dengan rapi di depan dadanya, menunggu pendapatmu."
    else:
        nar "Pelataran kuil pada hari-hari pertama Tahun Baru masih dipadati pengunjung yang berlalu-lalang mengenakan mantel tebal. Di tepi halaman dekat rak kayu pengikat omikuji, Kujo Harumi berdiri agak menyamping agar tidak menghalangi jalan sambil membuka selembar kertas ramalan yang baru ia ambil."
        nar "Cara ia menatap kertas tipis itu sama sekali tidak terlihat seperti orang yang sedang mencari hiburan Tahun Baru. Keningnya sedikit berkerut, kacamatanya dinaikkan sekali dengan telunjuk, lalu ia membacakan tiap bagian dengan nada terukur persis seperti memeriksa lembar prosedur praktikum."
        harumi "Keberuntungan umumnya sedang. Bagian studi dan riset bilang ketekunan pada rincian kecil membawa hasil sebelum musim panas. Bagian kesehatan mengingatkan agar tidak memotong jam tidur demi pekerjaan yang bisa dibagi. Semua bagian itu jelas dan masuk akal."
        yutaka "Bagus dong hasilnya, Kujo-san. Cara kamu bacanya serius banget kayak lagi review jurnal. Punyaku tadi cuma kulirik sekilas terus langsung masuk kantong."
        harumi "Kalau sudah menukar seratus yen dengan satu lembar informasi, seharusnya seluruh bagiannya dibaca sampai selesai dulu."
        yutaka "Oke, masuk akal juga. Terus bagian bawahnya soal hubungan gimana?"
        nar "Harumi tidak langsung menjawab. Matanya tertahan cukup lama pada kolom tengah kertas tersebut. Kamu melihat bibirnya bergerak pelan mengulang baris yang sama sampai tiga kali berturut-turut."
        harumi "'Perhatikan hatimu.'"
        yutaka "Cuma itu doang isinya?"
        harumi "Di bawahnya ada tambahan singkat berbunyi, 'jangan menunggu semuanya selesai baru menyadari apa yang tertinggal.' Kalau itu dimaksudkan sebagai instruksi, kriterianya sangat buruk dan sama sekali tidak terukur."
        nar "Kendati mengkritiknya dengan logis, Harumi belum juga melipat kertas itu. Ia menurunkan sedikit tangannya lalu memandang keramaian di sekitar pelataran kuil."
        harumi "Tapi terus terang, Kisaragi-kun... aku tetap ingin mengerti maksudnya. Aku punya kebiasaan yang cukup mengganggu. Aku sering baru sadar kalau diriku sebenarnya sedang sedih atau kecewa beberapa jam setelah semua orang pulang."
        yutaka "Pas kejadiannya berlangsung, kamu nggak langsung kerasa gitu?"
        harumi "Saat itu pikiranku penuh oleh hal-hal yang harus kuselesaikan di depan mata. Baru nanti sendirian di kamar asrama aku sadar ada rasa yang datang terlambat. Jadi melihat kalimat itu di kertas ramalan begini rasanya agak ganjil."
        yutaka "Di buku catatan hitam yang sering kamu bawa itu, bagian perasaan kayak gitu biasanya kamu tulis gimana?"
        harumi "Sering kali kubiarkan kosong dengan tanda tanya karena aku belum menemukan istilah yang paling akurat. Kadang sampai berhari-hari kemudian aku masih ragu apakah reaksi itu namanya kecewa, senang, atau cuma efek kurang istirahat."
        yutaka "Kalau kamu nunggu ketemu istilah ilmiah yang pas dulu, ya wajar aja momennya selalu keburu lewat, Kujo-san."
        harumi "Analisis itu tepat sekali, Kisaragi-kun. Di laboratorium semua perubahan larutan punya indikator warna yang pasti, sementara perubahan perasaan di dalam diri sendiri sering tidak punya batas awal yang jelas."
        nar "Angin awal Januari berembus pelan melewati rak kayu pengikat ramalan, menggoyangkan ujung kertas putih di tangan Harumi."
        nar "Ia memandangmu dari balik kacamatanya dengan raut wajah serius, menunggu tanggapanmu atas kebingungan yang baru saja ia akui."
        yutaka "Tapi kalau kamu sampai berhenti lama mikirin dua baris kalimat ini, berarti kamu sendiri sebenarnya pengin lebih peka dari awal kan?"
        harumi "Benar, Kisaragi-kun. Tahun ini aku ingin mengurangi jeda keterlambatan itu, hanya saja aku belum tahu harus mulai dari parameter mana."
        yutaka "Belajar peka sama perasaan sendiri memang nggak bisa instan kayak menghafal tabel rumus, Kujo-san."
        harumi "Aku mengerti. Setiap pembiasaan baru memang memerlukan pengulangan yang konsisten."
        nar "Harumi masih memegangi lembar kertas ramalan tersebut dengan kedua tangan di tengah udara dingin pelataran kuil."
        nar "Di antara keramaian pengunjung awal tahun yang lalu-lalang di belakangnya, perhatiannya kini terpusat penuh pada saran yang akan kamu berikan."
    menu:
        "\"Nggak usah langsung cari istilah yang berat. Mulai dari yang paling gampang dirasakan sekarang aja.\"":
            $ kk_record_choice("H08", "A")
            if kk_host == "chiasa":
                chiasa "Menurutku Kujo-senpai nggak usah memaksa diri langsung cari nama emosi yang besar atau istilah yang rapi buat dicatat di buku. Mulai aja dari hal paling kecil yang gampang Senpai rasakan detik ini juga."
                nar "Harumi menoleh kepadamu dari balik lensa kacamatanya dengan kening masih agak berkerut."
                harumi "Hal paling kecil yang kurasakan sekarang? Maksudnya seperti suhu udara atau kecepatan angin di halaman ini?"
                chiasa "Bukan suhu udara, Senpai. Misalnya, sekarang ini Senpai lagi pengin berdiri agak dekat atau pengin mundur ke tempat sepi? Lagi merasa agak lega, atau malah tegang? Pengin cepat pulang ke asrama, atau masih betah di sini sebentar? Nggak perlu langsung tahu itu namanya senang atau sayang."
                nar "Harumi terdiam memikirkan kalimatmu. Ia mengedarkan pandangan ke kerumunan orang-orang di depan tangga kuil, lalu kembali melihat ke arahmu. Setelah jeda beberapa detik, tanpa berkata apa-apa ia menggeser langkahnya setengah tapak berdiri lebih dekat ke sisimu di dekat pagar kayu yang lebih teduh dari angin."
                harumi "Kalau memakai metode sederhana seperti itu... saat ini aku tidak ingin buru-buru kembali ke asrama. Aku ingin tetap berdiri di sini sebentar lagi bersama Amamiya-san, sebelum kita turun membeli teh hangat."
                chiasa "Nah, itu dia. Gampang banget kan, Senpai? Nggak perlu nunggu pulang ke kamar dulu baru ketahuan."
                harumi "...Iya. Aku ingin tetap di sini sebentar. Ternyata tanpa harus mencari istilah rumit, satu kalimat itu sudah cukup menjadi informasi yang jelas."
                chiasa "Terus selain itu, ada lagi yang Senpai rasakan sekarang?"
                harumi "Tanganku agak dingin, tapi rasanya tenang karena angin di sebelah pagar sini tidak terlalu kencang... dan karena aku tidak berdiri sendirian."
                chiasa "Nah, makin jago tuh! Kalau kertasnya sudah nggak bikin bingung, mau diikat di rak situ?"
                harumi "Tidak, biar kusimpan saja. Bagaimanapun ini pengingat yang cukup berguna."
                nar "Harumi melipat kertas omikuji itu dengan hati-hati lalu memasukkannya ke saku dalam mantel abu-abunya. Sudut bibirnya melengkung tipis sebelum ia menanyakan apakah kamu ingin mencoba minuman jahe hangat di kedai bawah tangga."
                chiasa "Boleh banget, Senpai. Ayo jalan pelan-pelan ke bawah."
                harumi "Kalau nanti waktu minum teh jahe di bawah aku mencoba menyebutkan satu atau dua hal kecil lagi yang kurasakan saat itu, apakah kamu bersedia mendengarkannya untuk memeriksa apakah kalimatku terdengar wajar?"
                chiasa "Dengan senang hati, Kujo-senpai! Anggap saja kita lagi latihan bareng tanpa buku catatan."
                harumi "Latihan pengamatan langsung tanpa buku catatan... metode yang baru bagiku, tapi rasanya cukup menjanjikan."
                chiasa "Awas tangganya agak ramai di sebelah kiri, Senpai, kita lewat jalur pinggir dekat lentera batu ini saja."
                harumi "Baik. Terima kasih sudah berjalan di sebelahku, Amamiya-san."
                chiasa "Pelan-pelan saja turunnya, Senpai, batu anak tangganya agak lembap kena embun pagi."
                harumi "Iya, sol sepatuku cukup kesat, tetapi aku tetap memperhatikan pijakan tangganya."
                chiasa "Di kedai bawah itu selain teh jahe juga ada kue beras panggang kecap manis yang enak banget."
                harumi "Kue beras panggang hangat terdengar seperti sumber kalori yang sangat masuk akal untuk cuaca sedingin ini."
                chiasa "Hehe, cara Senpai menyebut makanan saja masih terdengar kayak laporan laboratorium."
                harumi "Kebiasaan lama memang butuh waktu untuk disesuaikan, Amamiya-san. Tapi saat ini aku merasa senang mengobrolkannya denganmu."
                nar "Senyum kecil yang muncul di wajah Harumi tampak jauh lebih alami dibandingkan saat ia pertama kali membuka kertas omikuji tadi."
                nar "Harumi melangkah sejajar di sampingmu menuruni tangga batu kuil dengan raut wajah yang tampak jauh lebih jernih dan tenang."
            else:
                yutaka "Kamu nggak perlu langsung cari nama emosi yang besar atau istilah rapi buat dimasukin ke catatan, Kujo-san. Mulai aja dari hal paling kecil yang bisa kamu rasakan detik ini juga."
                nar "Harumi menoleh dari balik kacamatanya dengan kening masih sedikit berkerut."
                harumi "Hal paling kecil yang kurasakan sekarang? Jadi aku boleh mulai dari reaksi sederhana saja, tanpa harus melabeli apa jenis perasaannya?"
                yutaka "Iya. Misalnya sekarang ini kamu pengin berdiri lebih dekat atau pengin mundur menjauh, merasa agak lega atau malah tegang, mau buru-buru balik ke asrama atau masih betah di sini sebentar. Nggak usah langsung mikir namanya senang, sedih, atau sayang."
                nar "Harumi terdiam sejenak menimbang kalimatmu. Ia menatap arus pengunjung di dekat tangga kuil, lalu kembali menoleh ke arahmu. Perlahan, ia melangkah setengah tapak lebih dekat ke sisimu di dekat pagar kayu yang agak terlindung dari angin."
                harumi "Kalau memakai patokan sesederhana itu... sekarang aku tidak ingin buru-buru pulang ke asrama. Aku ingin tetap berdiri di sini sebentar lagi bersama Kisaragi-kun."
                yutaka "Nah, gampang kan? Nggak perlu nunggu kamar kosong dulu buat tahu."
                harumi "...Iya. Aku ingin tetap di sini sebentar. Ternyata satu kalimat itu saja sudah menjadi informasi yang cukup jelas."
                yutaka "Ada hal kecil lain yang langsung ketangkap juga?"
                harumi "Udara di luar sini dingin, tapi suasana di dekat pagar kayu ini terasa nyaman... terutama karena aku tidak perlu berdiri mengurainya sendirian."
                yutaka "Tuh, makin lancar kan. Kertasnya mau kamu ikat di rak kayu sana?"
                harumi "Tidak perlu, kusimpan saja sebagai catatan awal tahun."
                nar "Harumi melipat kertas ramalannya dengan rapi lalu memasukkannya ke saku dalam mantel abu-abunya. Sudut bibirnya terangkat tipis sebelum ia mengajakmu turun mencari teh jahe hangat di kedai dekat gerbang."
                yutaka "Ayo, mumpung antrean kedainya lagi nggak terlalu panjang."
                harumi "Nanti selagi kita duduk minum teh jahe di bawah, bolehkah aku mencoba menyebutkan beberapa reaksi sederhana lagi supaya aku makin terbiasa mengenalinya secara langsung?"
                yutaka "Tentu saja boleh, Kujo-san. Sebutkan saja apa pun yang terlintas di kepalamu tanpa perlu disensor dulu."
                harumi "Tanpa disensor dan tanpa tabel waktu. Baiklah, aku rasa aku mulai menyukai latihan praktis ini."
                yutaka "Lewat sisi kanan tangga ini saja jalannya, bagian tengah lagi padat orang antre naik."
                harumi "Mengerti, aku mengikuti langkahmu di sebelah sini, Kisaragi-kun."
                yutaka "Hati-hati pijakannya, batu tangga sebelah pinggir situ agak licin kena sisa embun."
                harumi "Terima kasih peringatannya. Aku sudah menyesuaikan titik tumpu langkahku supaya tidak tergelincir."
                yutaka "Di kedai dekat gerbang bawah itu ada jual roti kukus kacang merah hangat juga kalau kamu lapar."
                harumi "Roti kukus hangat di udara dingin seperti ini merupakan pilihan konsumsi yang sangat efisien."
                yutaka "Haha, bahkan waktu bahas jajanan kuil pun istilahmu tetap nggak jauh-jauh dari kata efisien, Kujo-san."
                harumi "Aku memang belum pandai menggunakan kalimat puitis, Kisaragi-kun. Namun yang jelas, saat ini aku merasa sangat nyaman berjalan turun bersamamu."
                nar "Ekspresi kaku di wajah Harumi perlahan menghangat saat kalian melewati deretan lentera batu menuju gerbang bawah."
                nar "Harumi berjalan berdampingan denganmu menuruni anak tangga batu menuju gerbang kuil dengan langkah yang terasa jauh lebih ringan."
        "\"Haha, kalimat seumum itu sih memang sengaja dibikin biar cocok buat siapa aja.\"":
            $ kk_record_choice("H08", "B")
            if kk_host == "chiasa":
                nar "Kamu tertawa ringan sambil melirik kertas ramalan di tangan Harumi."
                chiasa "Ya ampun, Kujo-senpai serius banget sih nganalisis kertas omikuji. Kalimat kayak 'perhatikan hatimu' kan sengaja ditulis seumum mungkin supaya siapa pun yang baca, mulai dari anak SMP sampai kakek-kakek, pasti merasa kesindir semua!"
                nar "Harumi berkedip sejenak, lalu menurunkan kertas putih itu dan ikut mengangguk kecil seolah tersadar dari lamunannya sendiri."
                harumi "Benar juga. Secara statistik, pernyataan yang sangat kabur memang memiliki tingkat kecocokan subjektif yang tinggi bagi pembaca mana pun. Aku terlalu berlebihan menganggapnya sebagai petunjuk."
                chiasa "Nah, kan. Kalau dipikir terus nanti malah bikin kepala Senpai penuh sendiri padahal ini lagi hari libur."
                harumi "Iya. Sebaiknya tidak usah kubawa pikiran. Lagipula minggu depan laboratorium sudah mulai buka lagi, ada beberapa data lama yang perlu kurapikan sebelum kuliah dimulai."
                chiasa "Semangat deh, Senpai. Yuk turun cari minum hangat dulu."
                harumi "Iya, mari kita turun sekarang sebelum suhu udara sore makin turun."
                chiasa "Senpai mau teh hijau hangat atau amazake di kedai depan?"
                harumi "Teh hijau hangat biasa saja sudah cukup untuk menormalkan suhu tangan, Amamiya-san."
                chiasa "Kalau begitu aku juga beli teh hijau hangat saja biar cepat."
                harumi "Sesudah minum teh nanti, aku berencana langsung kembali ke asrama untuk menyusun jadwal pemakaian instrumen semester baru."
                chiasa "Hari pertama tahun baru pun langsung beresin jadwal instrumen ya, Senpai."
                harumi "Lebih baik menyiapkannya lebih awal selagi tidak ada variabel lain yang perlu dipikirkan."
                nar "Ia kembali menarik garis pembatas yang rapi di sekeliling rutinitas akademiknya, menutup celah keraguan yang tadi sempat terlihat."
                nar "Meskipun suaranya tetap teratur dan sopan seperti biasa, percakapan jujur yang tadi hampir terbuka di dekat rak omikuji langsung kembali tertutup rapat."
                nar "Harumi segera melipat kertas ramalannya menjadi lipatan persegi kecil dan menyimpannya ke dalam saku mantel. Ia membetulkan kacamatanya sekali lagi, lalu terus membahas jadwal pembukaan laboratorium tanpa pernah kembali menyinggung pengakuannya soal rasa sedih yang terlambat ia sadari tadi."
            else:
                nar "Kamu tertawa ringan sambil menatap kertas putih di tangan Harumi."
                yutaka "Jangan diseriusin banget dong, Kujo-san. Kalimat seumum 'perhatikan hatimu' itu memang sengaja dibikin kabur biar siapa pun yang baca pasti merasa kena."
                nar "Harumi berkedip singkat, lalu menurunkan tangannya dan mengangguk kecil seolah baru tersadar sendiri."
                harumi "Kamu benar. Secara statistik, pernyataan yang tidak spesifik memang bisa diterapkan pada hampir semua orang. Aku terlalu berlebihan memperlakukannya seperti petunjuk."
                yutaka "Nah, mending jangan dibawa pusing di hari libur begini."
                harumi "Iya. Sebaiknya aku berhenti menganalisisnya. Omong-omong, minggu depan perpustakaan sudah buka normal lagi, kamu sudah menyiapkan bahan semester baru?"
                yutaka "Belum semua sih, paling habis libur baru nyicil. Yuk turun dulu cari teh hangat."
                harumi "Baiklah, mari kita turun menuju kedai dekat gerbang depan."
                yutaka "Kamu mau minum teh hijau panas atau kopi kaleng hangat dari mesin?"
                harumi "Teh hijau panas saja sudah cukup untuk menghangatkan jari tangan, Kisaragi-kun."
                yutaka "Oke, kita mampir ke mesin minuman hangat dekat gerbang bawah saja."
                harumi "Selesai dari sini, aku akan langsung pulang ke asrama untuk memeriksa daftar katalog jurnal semester depan."
                yutaka "Hari libur tahun baru begini masih langsung buka katalog jurnal?"
                harumi "Menyusun jadwal riset jauh lebih mudah dilakukan ketika pikiran tidak terganggu oleh pertanyaan yang tidak memiliki parameter jelas."
                nar "Nada bicaranya kembali datar dan terukur seperti saat memimpin diskusi ilmiah di perpustakaan kampus."
                nar "Dengan kembali menempatkan semuanya ke dalam kerangka logika dan statistik semata, celah kecil tempat Harumi hampir mempelajari perasaannya sendiri kembali terkunci."
                nar "Harumi melipat kertas omikuji itu rapi-rapi dan memasukkannya ke saku mantel. Ia membetulkan letak kacamatanya lalu terus membicarakan jadwal kuliah minggu depan, tidak lagi menanyakan atau menyinggung bagian tentang dirinya yang terlambat menyadari rasa sedih tadi."
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
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Koridor lantai tiga Gedung Sains sudah nyaris kosong ketika kamu melangkah masuk ke ruang persiapan laboratorium yang pintunya terbuka separuh. Lampu putih panjang di langit-langit menerangi meja keramik panjang, rak tabung reaksi yang kering, serta aroma etanol tipis bercampur wangi teh hijau dingin."
        else:
            nar "Cahaya matahari awal musim semi menembus jendela lebar ruang persiapan laboratorium Gedung Sains yang lengang. Di sekeliling meja keramik panjang, deretan gelas ukur tersusun rapi di rak pengering, menyisakan bau etanol tipis dan dengung pelan lemari pendingin sampel dari sudut ruangan."
        nar "Kujo Harumi duduk sendirian di bangku tinggi paling ujung dekat jendela. Rambut abu-abu peraknya yang panjang tersusun rapi dalam kepang samping dan sanggul kecil berhias jepit mawar merah, sementara kalung lambang atom tipisnya berkilau samar di atas kerah kemeja putih dan kardigan abu-abu."
        nar "Di hadapannya tergeletak sebuah buku catatan kecil bersampul hitam yang biasa ia simpan rapat di saku kardigannya, menggantikan tumpukan buku teks kimia maupun lembar praktikum yang biasanya memenuhi meja. Begitu mendengar langkahmu mendekat, Harumi sempat menoleh dengan mata abu-kebiruan yang tenang, lalu menggeser bangku tinggi di sebelahnya sedikit keluar."
        harumi "Amamiya-san. Kebetulan kamu lewat sini. Kalau jadwalmu sedang tidak terburu-buru, boleh aku minta pendapatmu sebentar soal satu halaman di catatanku?"
        chiasa "Boleh banget, Kujo-senpai. Lagi ngerjain tabel data riset baru buat semester ini ya?"
        harumi "Bukan data praktikum laboratorium. Justru karena bukan data laboratorium, aku mulai kesulitan menentukan metode pembacaannya."
        nar "Harumi memutar buku catatan hitam itu pelan menghadap ke arahmu. Sekilas halamannya tampak sama rapinya dengan catatan kuliahnya, lengkap dengan garis pembatas buatan penggaris bening. Ketika kamu membungkuk membaca judul tiap kolomnya, kedua alismu sedikit terangkat."
        nar "Kolom pertama berisi tanggal dan waktu, kolom kedua mencatat percakapan singkatnya bersama Koita sepanjang beberapa bulan terakhir, lalu kolom ketiga merinci reaksi tubuh dan konsentrasinya sesudahnya. Tertulis rapi di sana catatan tentang kesulitan membaca jurnal selama dua puluh menit setelah berpapasan, keinginan mengajak bicara lagi selepas kelompok belajar bubar, hingga rasa kecewa yang mengganggu ritme kerjanya ketika undangan makan siang bersama dibatalkan."
        nar "Di sisi paling kanan, terdapat satu kolom lebar bertajuk klasifikasi emosi. Seluruh baris di kolom itu dibiarkan kosong melompong."
        chiasa "{i}Dia beneran nyatet tiap reaksinya ke Ko-nii dalam bentuk tabel observasi lengkap sama durasi waktunya...{/i}"
        nar "Kamu menahan diri agar tidak mengeluarkan suara kaget. Di balik kerapian garis penggaris dan tulisan tangan tegak itu, tergambar jelas betapa dalamnya Koita mengendap di kepala Harumi tanpa pernah memberinya kejelasan apa pun."
        chiasa "Kujo-senpai mencatat semua interaksi sama Ko-nii sampai sedetail ini... tapi kolom paling kanannya sengaja belum diisi?"
        harumi "Iya. Aku menimbang kolom itu sejak dua minggu lalu, dan sampai sekarang belum berani menuliskan satu kata pun di sana."
        nar "Harumi menaikkan bingkai kacamatanya yang tipis dengan ujung jari tengah, lalu menatap halaman kosong di sebelah kanan bukunya dengan kening berkerut samar."
        harumi "Aku takut kalau aku asal menuliskan satu nama perasaan di kolom itu, otakku akan mengalami bias konfirmasi. Begitu labelnya tertulis, aku mungkin mulai memilih hanya kejadian yang mendukung label itu dan mengabaikan kenyataan lain."
        chiasa "Tapi kalau terus dibiarkan kosong begitu, Kujo-senpai juga masih kepikiran kan?"
        harumi "Benar. Membiarkannya kosong justru membuatku terus curiga jangan-jangan semua reaksi ini cuma gangguan konsentrasi yang harus diperbaiki. Seperti angka menyimpang dalam percobaan yang belum ketahuan salahnya di mana."
        if kk_has("harumi_menafsirkan_omikuji"):
            harumi "Di kuil awal tahun waktu itu, Amamiya-san bilang aku harus mulai memperhatikan bagian ini dari hal paling kecil tanpa menunggu semuanya selesai dulu. Aku sudah coba mengumpulkan catatannya, tapi ternyata begitu sampai di tahap memberi nama, aku tetap buntu."
        nar "Harumi menoleh penuh ke arahmu. Suaranya tetap datar dan lurus, menyiratkan kejujuran seseorang yang sungguh-sungguh menyerahkan lembar kerentanannya untuk dibaca oleh adik tiri dari orang yang sedang ia catat."
    else:
        if kk_slot >= 3:
            nar "Lantai tiga Gedung Sains sudah lengang ketika kamu melangkah melewati ruang persiapan laboratorium untuk mengembalikan buku referensi statistik yang sempat kamu pinjam. Lampu putih ruangan menyala terang di atas meja keramik, menyisakan bau etanol tipis dan dengung pelan lemari pendingin sampel."
        else:
            nar "Cahaya awal musim semi masuk lebar melalui jendela ruang persiapan laboratorium Gedung Sains yang relatif sepi. Kamu mampir ke lantai tiga untuk mengembalikan buku referensi statistik sekaligus menghindari koridor utama yang ramai oleh jadwal kuliah baru."
        nar "Di bangku tinggi paling ujung dekat jendela, Kujo Harumi duduk sendirian mengenakan kemeja putih dan kardigan abu-abu. Rambut abu-abu peraknya tersusun rapi dalam kepang samping dan sanggul kecil berhias jepit mawar merah, dengan kalung lambang atom tipis menggantung di lehernya."
        nar "Alih-alih membuka jurnal kimia tebal seperti biasanya, ia tengah menatap buku catatan kecil bersampul hitam yang diletakkan rata di hadapannya. Begitu bunyi langkahmu berhenti di ambang pintu, mata abu-kebiruan di balik bingkai kacamata tipis itu langsung menoleh."
        harumi "Kisaragi-kun. Kebetulan sekali. Kalau kamu belum buru-buru kembali ke gedung fakultasmu, boleh aku minta pendapatmu sebentar?"
        yutaka "Boleh aja, Kujo-san. Tumben jam segini kamu nggak lagi pegang tabung sampel atau tumpukan jurnal. Ada soal kuliah yang mau dibahas?"
        harumi "Bukan soal kuliah. Aku butuh sudut pandang dari seseorang yang sudah lama mengenal Amamiya-kun dan tidak gampang bereaksi berlebihan."
        nar "Alismu terangkat sedikit mendengar nama sahabatmu disebut dengan nada setenang membahas suhu ruangan. Kamu melangkah mendekat, meletakkan buku pinjaman di pinggir rak, lalu berhenti di samping meja keramik tempat buku catatan hitam itu terbuka."
        nar "Harumi memutar buku itu sembilan puluh derajat menghadapmu. Halamannya penuh garis pembatas rapi buatan penggaris. Kolom kiri mencatat tanggal dan potongan percakapan singkatnya dengan Koita beberapa bulan terakhir, kolom tengah merinci efek fisik dan kognitifnya sesudahnya seperti konsentrasi buyar dua puluh menit, dorongan ingin bicara lebih lama, hingga rasa kecewa yang membuat ritme kerjanya kacau saat undangan makan siang dibatalkan."
        nar "Sementara itu, satu kolom paling kanan bertajuk klasifikasi emosi dibiarkan kosong seluruhnya."
        yutaka "{i}Gila juga si Koita... sampai siswi paling logis di angkatan pun bikin tabel laporan praktikum cuma gara-gara kelakuannya yang nggak jelas itu.{/i}"
        yutaka "Kamu beneran mencatat tiap obrolan sama Koita lengkap dengan durasi efeknya, Kujo-san? Terus kolom sebelah kanan ini sengaja belum kamu isi?"
        harumi "Iya. Sudah hampir dua minggu kolom itu kosong. Aku takut kalau aku terlanjur menuliskan satu nama perasaan di sana, aku akan mulai memilih data yang hanya mendukung label itu dan mengabaikan fakta lain."
        yutaka "Jadi kamu khawatir bakal kena bias sendiri?"
        harumi "Persis. Tapi membiarkannya kosong begini juga membuatku terus bertanya jangan-jangan seluruh reaksi yang kucatat di kolom tengah ini cuma kesalahan konsentrasi yang seharusnya bisa kuhilangkan."
        if kk_has("harumi_menafsirkan_omikuji"):
            harumi "Di kuil waktu awal tahun kemarin, Kisaragi-kun menyarankan supaya aku memperhatikan hal-hal kecil di bagian ini dulu tanpa buru-buru mencari istilah besar. Catatannya sudah terkumpul, tapi begitu harus memberi nama pada baris-baris ini, aku tetap tidak yakin."
        nar "Harumi mengangkat wajah menatapmu lurus dari balik lensa kacamatanya. Ia berbicara sebagai rekan seangkatan yang sungguh-sungguh mempercayakan satu kelemahannya kepada seseorang yang ia anggap sanggup berpikir jernih."
    call kk_family_menu("H09", ["\"Nggak perlu langsung cari istilah besar. Kita cari kata yang paling pas buat kolom kosong itu bareng-bareng.\"", "\"Haha, perasaan kok dicatat pakai tabel praktikum segala? Terlalu kaku deh.\"", "Tutup buku catatannya, kembalikan ke meja, dan ambil jarak."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu menarik bangku tinggi di sampingnya dan duduk menghadap meja keramik itu tanpa memperlakukan tabelnya seperti hal aneh."
            chiasa "Kujo-senpai nggak perlu langsung menulis kata yang besar dan berat di situ kok. Gimana kalau kita coba cari satu kata sederhana dulu yang paling pas buat salah satu barisnya? Kalau menurut Senpai nggak cocok, coret aja."
            nar "Harumi mengerjap sekali, lalu mengambil pensil mekanik dari sisi bukunya dan mengangguk kecil."
            harumi "Metode eliminasi seperti itu terdengar lebih aman. Baik, kita coba baris yang paling bawah ini saja. Waktu rencana makan siang bersama batal minggu lalu karena kakakmu ada urusan mendadak dengan panitia."
            chiasa "Oke. Waktu dengar acaranya batal, apakah Kujo-senpai merasa marah?"
            harumi "Tidak. Aku tidak ingin membentak siapa-siapa, dan alasannya memang masuk akal. Jadi kata marah jelas tidak akurat."
            chiasa "Kalau begitu... gimana dengan iri, atau takut tertinggal?"
            harumi "Hm... sedikit mendekati, tapi di ruangan waktu itu tidak ada orang lain yang sedang kubandingkan. Yang muncul cuma rasa ruangan jadi terasa terlalu sepi setelah pesan pembatalannya masuk."
            chiasa "Kalau kata rindu, gimana? Atau mungkin sebenarnya Kujo-senpai cuma lagi pengin ditemani?"
            nar "Ujung pensil mekanik di jari Harumi berhenti beberapa milimeter di atas kertas. Ia menatap baris catatannya cukup lama, menguji kedua kata itu pelan-pelan dalam kepalanya sebelum akhirnya menuliskan kata rindu sangat tipis, lalu menghapusnya dan menggantinya dengan frasa ingin ditemani."
            harumi "...Ternyata semua gejala di kolom tengah ini memang bukan variabel yang rusak, ya. Aku memang sungguh-sungguh merasakannya."
            chiasa "Cocoknya lebih ke yang kedua ya, Senpai?"
            harumi "Iya. Ingin ditemani jauh lebih akurat buat hari ini. Anehnya, begitu kata itu tertulis, dadaku terasa jauh lebih ringan. Aku jadi sadar aku tidak harus langsung memutuskan arti seluruh hubunganku dengan kakakmu hanya untuk mengakui satu perasaan sederhana ini."
            chiasa "Nah, kan. Perasaan itu nggak selalu harus langsung jadi kesimpulan permanen kok, Senpai."
            harumi "Terima kasih sudah mau ikut membacanya tanpa menganggapku aneh, Amamiya-san. Kalau sendirian, mungkin sampai semester berakhir kolom ini masih kosong."
            chiasa "Kapan pun Kujo-senpai butuh teman buat nyocokin kata di baris berikutnya, panggil aku aja lagi."
            harumi "Akan kuingat tawaran itu. Rasanya metode diskusi dua orang jauh lebih efektif untuk mengurangi keraguanku."
            nar "Ia merapikan letak pensil mekaniknya di samping buku catatan sambil menatap satu baris klasifikasi yang kini telah terisi dengan tulisan tangannya."
            nar "Sudut bibir Harumi terangkat membentuk senyum tipis yang tenang. Ia tidak buru-buru menutup buku hitamnya, membiarkan baris tulisan pertama di kolom kanan itu tetap terbuka di bawah cahaya ruangan."
        else:
            nar "Kamu menarik bangku tinggi di sampingnya, menumpukan sebelah siku di meja keramik, lalu memperhatikan kolom kosong itu dengan santai tanpa sedikit pun terdengar mengejek."
            yutaka "Nggak usah langsung mikirin istilah besar atau kesimpulan akhir, Kujo-san. Kita pakai cara simpel aja. Pilih satu baris yang paling baru, terus kutawarkan beberapa kata biasa. Kalau menurutmu meleset, langsung tolak."
            nar "Harumi tampak langsung menangkap alurnya. Ia meraih pensil mekaniknya dan mengetuk baris terbawah di halaman."
            harumi "Masuk akal. Mari pakai catatan hari Rabu kemarin, ketika rencana makan siang bersama Amamiya-kun batal mendadak dan konsentrasiku di lab turun hampir setengah jam."
            yutaka "Oke. Waktu pesan pembatalannya masuk, yang pertama muncul itu kesal atau marah?"
            harumi "Bukan marah. Jadwalnya memang bentrok dengan urusan panitia, jadi tidak ada alasan logis untuk menyalahkannya."
            yutaka "Kalau cemburu, atau ngerasa kalah penting sama urusan lain?"
            harumi "Agak mirip, tapi aku bahkan tidak tahu dia pergi menemui siapa. Aku cuma merasa meja kantin jadi terlalu berisik ketika aku duduk sendirian."
            yutaka "Nah, kalau gitu coba bandingkan dua kata ini. Rindu, atau cuma lagi ingin ditemani?"
            nar "Harumi terdiam memandang kolom kosongnya. Ia sempat menuliskan kata rindu tipis sekali dengan ujung pensil, mengernyit sejenak seolah menimbang akurasinya, lalu menghapusnya pelan dan menulis ulang frasa ingin ditemani."
            harumi "...Ternyata ini memang bukan variabel yang salah, ya. Aku sungguh-sungguh merasakan itu."
            yutaka "Yang kedua lebih kena di kepala?"
            harumi "Jauh lebih tepat untuk hari ini. Dan ternyata menulis satu kata itu tidak langsung memaksaku menentukan status seluruh hubunganku dengan Amamiya-kun. Aku boleh mengakui satu perasaan sederhana tanpa harus langsung menarik kesimpulan besar."
            yutaka "Nah, bener kan. Nggak semua rasa harus langsung jadi kontrak permanen kok, Kujo-san."
            nar "Sudut bibir Harumi melengkung tipis, nyaris seperti tawa kering yang lega."
            harumi "Kalau memakai perumpamaan kontrak ekonomi begitu, penjelasannya malah jauh lebih mudah dicerna. Terima kasih sudah meluangkan waktu mendengarkan, Kisaragi-kun."
            yutaka "Santai aja. Kalau kolom sisanya masih bikin bingung lain kali, tinggal panggil."
            harumi "Baik. Lain kali kalau ada baris observasi yang sulit kupetakan sendiri, aku akan meminta pendapatmu lagi."
            nar "Ia menyandarkan punggungnya dengan lebih santai di bangku tinggi laboratorium sambil memperhatikan tulisan baru di buku catatannya."
            nar "Harumi mengangguk tenang dan membiarkan halaman itu terbuka di bawah cahaya, kali ini dengan satu jawaban jujur yang tidak lagi ia sembunyikan di balik angka."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Melihat deretan kolom rapi berisi jam, menit, dan gejala berdebar hanya karena batal makan siang dengan Koita, tawa kecil refleks lepas dari tenggorokanmu sebelum kamu sempat menahannya."
            chiasa "Haha, serius nih Kujo-senpai sampai bikin tabel lengkap pakai penggaris buat nyatet perasaan kayak laporan praktikum? Aduh, maaf, cuma lucu aja lihatnya. Kaku banget sih, Senpai, perasaan mana bisa dihitung pakai kolom begini."
            nar "Tawamu langsung menggantung canggung di ruang laboratorium yang sunyi. Harumi tidak membantah. Ia juga tidak memerah malu ataupun mengangkat suaranya."
            nar "Dengan gerakan sangat teratur, Harumi menarik buku catatan hitam itu kembali ke sisinya, menutup sampulnya hingga berbunyi pelan, lalu meratakan posisi pensil mekaniknya sejajar tepi meja."
            harumi "Begitu ya. Berarti caraku memang keliru, dan bagian ini memang tidak perlu kubahas dengan Amamiya-san."
            chiasa "Eh, tunggu, Senpai, aku tadi cuma bercanda doang kok. Nggak bermaksud ngejek catatan Kujo-senpai..."
            harumi "Tidak apa-apa. Kamu tidak perlu meminta maaf. Aku sendiri yang salah mengira obrolan ini relevan untuk ditanyakan di ruang lab."
            nar "Ia menaikkan bingkai kacamatanya dan menyelipkan buku hitam itu ke dalam saku dalam kardigan abu-abunya, seakan seluruh percakapan lima menit terakhir baru saja dicoret dari agenda."
            harumi "Omong-omong, kalau kamu kemarin butuh contoh diagram pembiasan warna untuk kelas tahun keduamu, modulnya sudah kukembalikan ke rak perpustakaan sains. Nanti kamu bisa langsung pinjam dengan kartu mahasiswa."
            chiasa "Oh... iya, makasih infonya, Kujo-senpai."
            harumi "Sama-sama. Maaf menyita waktumu, aku harus mengecek suhu inkubator sampel di ruang sebelah dulu."
            nar "Ia meraih papan klip praktikum dari rak samping dan langsung memeriksa deretan angka pada layar mesin pendingin di sudut laboratorium."
            nar "Tawa spontanmu tadi telah membuatnya menyimpulkan bahwa kerentanan pribadinya hanya akan terlihat konyol bila dibagi dengan orang lain."
            nar "Kamu berdiri canggung di dekat pintu ruang persiapan sebelum akhirnya berbalik melangkah keluar menuju tangga gedung."
            nar "Harumi mengangguk sopan dengan raut wajah kembali datar sepenuhnya, lalu beranjak ke meja belakang. Setiap kalimatnya terdengar sangat terukur dan ramah, sementara pintu kecil yang tadi sempat ia buka kini tertutup rapat tanpa menyisakan celah sedikit pun."
        else:
            nar "Melihat susunan tabel lengkap dengan penggaris, menit gangguan fokus, dan kolom kosong hanya untuk mencatat interaksi singkat dengan Koita, tawa kering refleks keluar dari mulutmu."
            yutaka "Haha, serius kamu, Kujo-san? Urusan perasaan sampai dibikin tabel praktikum lengkap pakai menit begini? Kaku banget deh, mana bisa rasa suka atau kecewa dihitung pakai rumus lab segala."
            nar "Suara tawamu jatuh datar di tengah ruang laboratorium yang sepi. Harumi tidak membentak, tidak pula terlihat malu ataupun membela diri. Ekspresinya tetap tenang sepenuhnya."
            nar "Ia menarik buku catatan hitamnya kembali dengan kedua tangan, menutup sampulnya rapat, lalu meletakkan pensil mekanik sejajar pinggir meja."
            harumi "Begitu. Berarti bagian itu memang tidak perlu kubahas denganmu, Kisaragi-kun."
            yutaka "Hei, santai dong, aku cuma bercanda soal gayamu yang terlalu rapi aja. Nggak bermaksud bikin kamu tersinggung."
            harumi "Aku tidak tersinggung. Aku cuma menyadari sudut pandang yang kucari ternyata tidak cocok di sini. Salahku sendiri karena mengangkat topik tidak terukur di ruang lab."
            nar "Ia menyelipkan buku hitam itu ke saku kardigan abu-abunya dan membetulkan letak kacamatanya dengan gerakan kaku."
            harumi "Terima kasih sudah mengembalikan buku referensinya tepat waktu. Kalau semester ini kamu butuh catatan ringkasan probabilitas lanjutan, kabari saja lewat pesan seperti biasa. Aku harus memeriksa larutan di meja belakang sekarang."
            yutaka "...Oke. Duluan kalau gitu, Kujo-san."
            nar "Ia sudah berbalik menghadap rak tabung reaksi dan mencatat angka takaran tanpa menoleh sedikit pun lagi ke arah meja depan."
            nar "Komentar meremehkanmu barusan membuat Harumi segera kembali berlindung di balik kebiasaan akademiknya yang dingin dan tertutup."
            nar "Percakapan langsung kembali kering sebatas urusan akademik yang bisa diukur tanpa menyerahkan sepotong pun isi hatinya. Kamu melangkah keluar ruang lab sambil merasakan dinginnya jarak rapi yang baru saja ia pasang kembali di antara kalian."
    else:
        if kk_host == "chiasa":
            nar "Kamu menatap baris-baris nama Koita di halaman buku itu sejenak, lalu perlahan menutup kembali sampul hitamnya dan mendorong buku tersebut kembali ke depan tangan Harumi. Kamu mundur setengah langkah dari tepi meja keramik."
            chiasa "Maaf ya, Kujo-senpai... aku rasa aku bukan orang yang tepat buat ikut menilai catatan pribadi begini. Apalagi isinya menyangkut Ko-nii. Kalau aku asal nebak kata di kolom itu, takutnya malah ikut mengarahkan pikiran Senpai ke hal yang salah."
            nar "Harumi memandangi buku hitam yang kini tertutup di hadapannya selama dua detik penuh. Ia hanya menarik napas pendek yang nyaris tak terdengar sebelum meraih buku itu kembali dengan kedua tangan."
            harumi "Kamu benar. Melibatkan adik dari orang yang tercatat di sini memang membuat posisinya tidak netral. Maaf sudah menempatkan Amamiya-san dalam situasi yang canggung."
            chiasa "Nggak apa-apa kok, Senpai. Aku cuma nggak pengin salah kasih saran soal perasaan orang lain."
            harumi "Baik. Aku mengerti. Kalau begitu aku coba urai sendiri dulu di waktu luang nanti."
            nar "Ia menyelipkan buku catatan itu kembali ke dalam tas kainnya dengan rapi, lalu bangkit merapikan gelas ukur yang sudah kering di samping wastafel lab."
            chiasa "Kalau begitu aku permisi duluan ya, Kujo-senpai. Semangat risetnya buat semester baru."
            harumi "Terima kasih, Amamiya-san. Hati-hati di tangga."
            nar "Di balik punggungmu, terdengar bunyi gesekan kursi kayu saat Harumi kembali duduk seorang diri di meja keramik dekat jendela."
            nar "Penolakan halusmu untuk ikut campur menjaga posisimu tetap aman, namun membiarkan kolom emosi di bukunya tetap kosong tanpa jawaban."
            nar "Kamu melangkah keluar meninggalkan ruang persiapan yang kembali sunyi. Suara Harumi yang tenang dan rapi tadi sama sekali tidak memberi petunjuk apakah ia memang lega diberi ruang, atau baru saja menarik kesimpulan dingin bahwa keinginannya untuk dimengerti sebaiknya tidak pernah lagi ia sodorkan kepadamu."
        else:
            nar "Kamu melirik baris-baris nama Koita yang tertulis begitu serius di halaman itu, lalu perlahan menutup sampul hitam buku catatan tersebut dan mendorongnya kembali ke sisi meja Harumi. Kamu mundur setengah langkah sambil memasukkan tangan ke saku jaket."
            yutaka "Maaf, Kujo-san, tapi kayaknya aku bukan orang yang tepat buat ikut mengisi kolom itu. Aku kenal Koita terlalu dekat, jadi pendapatku pasti nggak bakal netral. Lebih baik kamu sendiri yang menentukan apa artinya buatmu."
            nar "Harumi menatap buku tertutup di depannya beberapa detik tanpa protes. Ia meraih buku hitam itu dengan tenang, lalu memasukkannya kembali ke dalam tas kainnya yang bersandar di kaki bangku."
            harumi "Poin yang masuk akal. Melibatkan sahabat dekat Amamiya-kun memang menambah variabel yang tidak perlu. Maaf sudah menahan waktumu, Kisaragi-kun."
            yutaka "Nggak masalah. Aku cuma nggak mau asal nebak perasaan orang lain terus malah bikin kamu tambah bingung."
            harumi "Baik. Aku coba selesaikan sendiri dulu."
            yutaka "Kalau begitu aku duluan ya, Kujo-san. Jangan sampai lupa makan gara-gara keasyikan di lab."
            harumi "Iya. Terima kasih, Kisaragi-kun."
            nar "Ia menarik kembali jurnal kimia tebal dari ujung meja dan membukanya di halaman yang telah ditandai pembatas kertas."
            nar "Sikapmu yang memilih menjaga jarak membuat Harumi kembali menyimpan kebingungannya seorang diri di balik tumpukan literatur ilmiah."
            nar "Dengung pelan lemari pendingin sampel di sudut ruangan kembali menjadi satu-satunya suara yang menemani kesendiriannya sore itu."
            nar "Langkah kakimu di koridor lantai tiga Gedung Sains perlahan menjauh dari pintu ruang persiapan yang tetap terbuka separuh."
            nar "Kamu meninggalkan ruang persiapan laboratorium yang hening tanpa mengetahui kesimpulan apa yang akhirnya akan ia tulis di buku hitam tersebut."
            nar "Ia mengangguk sopan lalu berbalik merapikan catatan praktikum di mejanya. Suaranya yang terlampau tenang itu tidak memberimu petunjuk apakah ia memang membutuhkan ruang sendiri, atau diam-diam sedang mencatat bahwa keinginan untuk dimengerti sebaiknya tidak pernah diajukan kepadamu."
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
        nar "Pukul satu dini hari, dapur bersama Asrama Putri hanya diterangi lampu kecil di atas kompor. Harumi berdiri di dekat meja kayu dengan dua cangkir keramik yang mengepul tipis, lalu menyodorkan satu cangkir ke depan kursimu begitu kamu masuk."
        chiasa "Lho, Kujo-senpai belum tidur jam segini? Kok cangkirnya sudah ada dua?"
        harumi "Tadi lampu lorong sempat menyala dan aku dengar langkahmu turun, Amamiya-san. Aku menyeduh lebih banyak memang dengan sengaja. Pegang pelan-pelan, masih cukup panas."
    else:
        call kk_scene_enter("harumi", "Di luar jendela dapur asrama")
        nar "Pukul satu dini hari, jendela kecil dapur lantai dasar Asrama Putri masih menyala redup. Kamu berhenti di jalur paving di luar batas gedung asrama ketika tirai digeser sedikit dan Harumi muncul sambil memegang dua cangkir teh hangat."
        yutaka "Kujo-san masih bangun jam satu begini? Aku kebetulan lewat depan asrama habis cari udara."
        harumi "Tadi aku melihat pesan statusmu masih aktif, Kisaragi-kun, jadi aku sengaja menyeduh dua cangkir. Kamu tetap di luar saja ya, sini kuambilkan lewat kusen jendela. Hati-hati, masih hangat sekali."
    nar "Ia menahan tangannya sebentar hingga jarimu benar-benar menggenggam cangkir dengan aman sebelum melepaskan. Kebaikan sederhana malam itu tidak diikuti permintaan catatan kuliah ataupun alasan akademik apa pun untuk menahanmu tetap berdiri di sana."
    call kk_family_menu("H-D01", ["Minum bersamanya dalam diam.", "Tanyakan apa yang ia rasakan malam ini.", "Ceritakan apa yang membuatmu masih terjaga."])
    if _return == "A":
        nar "Kamu menyesap teh hijau hangat itu perlahan tanpa memecah keheningan. Selama beberapa menit hanya terdengar dengung pelan lemari es dan tetesan air dari ketel yang mendingin. Harumi sempat membuka mulut seperti hendak memulai topik, lalu mengurungkannya dengan raut agak lega."
        if kk_host == "chiasa":
            harumi "Sebenarnya tadi aku sudah menyiapkan dua topik berita riset supaya Amamiya-san nggak bosan duduk di sini. Ternyata diam begini nggak terasa canggung sama sekali ya."
            chiasa "Nggak usah repot-repot nyari topik kok, Kujo-senpai. Minum teh hangat tenang begini aja sudah enak banget."
        else:
            harumi "Tadi aku sempat menyiapkan beberapa topik kuliah supaya Kisaragi-kun nggak bosan berdiri di luar jendela. Ternyata melewatkan topik begitu saja nggak bikin kita kehilangan alasan buat tetap di sini ya."
            yutaka "Angin malam sama teh hangatnya sudah cukup banget kok, Kujo-san. Santai aja."
        harumi "...Iya. Aku suka keheningan yang nggak mengharuskanku terus menjelaskan apa-apa."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Kujo-senpai, kalau boleh tahu, apa yang sebenarnya lagi Senpai rasakan malam ini?"
        else:
            yutaka "Kujo-san, malam ini pikiranmu lagi ke mana? Kamu kelihatan jauh lebih tenang dari biasanya."
        nar "Harumi menatap permukaan teh di cangkirnya selama beberapa detik, seolah benar-benar menimbang kata demi kata dengan hati-hati sebelum menjawab."
        harumi "Aku sedang mencoba mencari nama yang paling akurat buat yang kurasakan sekarang. Tenang, mungkin. Tapi di saat yang sama ada keinginan aneh supaya jarum jam malam ini jalan lebih lambat."
        nar "Ia mengangkat pandangan menatap matamu langsung."
        harumi "Aku nggak mau buru-buru menyebut perasaan ini cinta cuma supaya punya jawaban yang rapi di kepalaku. Aku pengin mengenali bagian yang ini dulu pelan-pelan."
    else:
        if kk_host == "chiasa":
            chiasa "Jujur aja kepalaku masih ramai banget malam ini, Kujo-senpai. Banyak hal yang harus kujalani besok sampai rasanya bingung mau mulai mikir dari mana."
        else:
            yutaka "Jujur aja malam ini aku belum bisa tidur karena terlalu banyak hal di kampus yang belum nemu ujungnya, Kujo-san."
        harumi "Aku mendengarkan kok. Kamu nggak perlu menyusun kalimatnya jadi ringkas kalau memang belum ketemu kesimpulannya."
        nar "Kamu bercerita pelan tanpa urutan yang rapi, beberapa kali terhenti di tengah kalimat. Harumi menyimak utuh tanpa menyela ataupun mengoreksi, lalu setelah cangkirmu hampir kosong ia mengulang satu inti kecil yang ia tangkap dari ceritamu."
        harumi "Kalau yang kudengar tadi benar, berarti yang paling bikin kamu lelah itu keharusan buat terus memilih langkah tanpa boleh salah ya? Apakah pemahamanku sudah mendekati?"
        nar "Pertanyaan sederhana itu membuat bahumu jauh lebih ringan saat kamu mengangguk pelan."
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
        nar "Lampu kuning hangat menerangi dapur bersama Asrama Putri yang sudah lengang malam itu. Suara panci dan obrolan penghuni kamar lain sudah mereda di balik pintu-pintu koridor. Di atas meja makan panjang di depanmu, Kujo Harumi meletakkan sepiring tumis sayur dan daging dengan gerakan rapi, tepat di samping sebuah buku catatan resep yang dipenuhi tulisan kecil, angka takaran, dan coretan konversi mililiter."
        nar "Harumi mengenakan celemek polos berwarna abu-abu di atas kemeja putihnya, sementara rambut abu-abunya yang diikat menyamping di atas bahu tampak sedikit berantakan terkena uap wajan. Secara visual, hidangan di atas piring itu masih bisa dikenali sebagai masakan rumahan, hanya saja aromanya yang menyengat tajam antara manis pekat, asin kecap, dan sedikit bau hangus langsung membuatmu refleks melirik buku catatannya lebih dahulu."
        nar "Harumi membetulkan letak kacamatanya dengan ujung jari, lalu menatap piring itu dan dirimu bergantian dengan wajah sangat serius."
        harumi "Aku mengikuti urutan di buku resepnya, Amamiya-san. Lalu aku menyesuaikan beberapa takaran bumbu dan suhu apinya karena kupikir prosesnya bisa dibuat lebih efisien."
        chiasa "Efisien... maksudnya Kujo-senpai menaikkan suhu apinya biar cepat matang?"
        harumi "Iya. Menurut perkiraanku, mempercepat reaksi pemanasan akan memangkas waktu berdiri di depan kompor sampai setengahnya. Dan aku juga menggabungkan dua tahap pemberian bumbu sekaligus supaya tidak perlu mencuci sendok takar dua kali."
        chiasa "Lalu hasilnya jadi seperti ini ya, Senpai..."
        harumi "Ternyata resep masakan tidak senang diperlakukan seperti prosedur laboratorium. Kecapnya langsung mengental di dasar wajan sebelum sayurnya sempat empuk."
        nar "Ia menggeser sepasang sumpit bersih ke sebelah piringmu dengan ekspresi datar yang tampak berada di antara pasrah dan penasaran."
        harumi "Secara teori semua bahannya masih segar dan layak konsumsi, tidak ada yang kedaluwarsa. Mungkin... kamu mau coba sedikit untuk verifikasi rasa?"
    else:
        nar "Malam musim panas di area ruang tamu bersama lantai satu Asrama Putri, batas terjauh yang boleh dimasuki tamu laki-laki dengan izin pengelola asrama. Jendela samping yang menghadap langsung ke dapur bersama terbuka lebar, membiarkan aroma masakan yang agak mencurigakan mengalir keluar menyapa hidungmu."
        nar "Tidak lama kemudian, Kujo Harumi melangkah keluar dari balik pintu dapur membawa sebuah nampan berisi sepiring tumis sayur dan daging, sepasang sumpit, serta buku catatan resep yang penuh angka takaran dan coretan konversi mililiter. Celemek abu-abu polos masih terikat rapi di pinggangnya, dan rambut abu-abu panjang yang diikat menyamping itu sedikit lembap oleh uap wajan."
        nar "Ia meletakkan piring itu di atas meja tamu di depanmu. Dari bentuknya, hidangan itu masih bisa dikenali sebagai tumisan biasa, tetapi baunya yang menusuk tajam antara asin kecap, manis pekat, dan sedikit bau hangus langsung membuatmu ingin membaca buku catatannya lebih dulu sebelum menyentuh sumpit."
        nar "Harumi membetulkan letak kacamatanya dengan ujung jari, lalu menatap piring dan dirimu bergantian dengan wajah sangat serius."
        harumi "Aku mengikuti urutan di buku resepnya, Kisaragi-kun. Lalu aku menyesuaikan beberapa jumlah bumbu dan suhu apinya karena kupikir prosesnya bisa dibuat lebih efisien."
        yutaka "Efisien... maksudmu kamu besarkan apinya biar cepat matang?"
        harumi "Iya. Secara logika, energi panas yang lebih besar seharusnya mempersingkat waktu memasak. Aku juga menggabungkan dua tahap bumbu sekaligus supaya tidak perlu mencuci sendok takar berulang kali."
        yutaka "Dan bau karamel gosong yang sampai ke ruang tamu tadi itu efek gabungannya?"
        harumi "Ternyata gula dan kecap langsung mengeras di dasar wajan kalau dipanaskan terlalu cepat. Resep masakan rupanya tidak senang diperlakukan seperti prosedur laboratorium."
        nar "Ia menggeser sumpit bersih ke sebelah piringmu dengan ekspresi datar antara pasrah dan penasaran."
        harumi "Secara teknis semua bahannya baru kubeli sore tadi dan aman dikonsumsi. Kebetulan kamu mampir mengantar catatan ke asrama, mau coba sedikit untuk verifikasi rasa?"
    call kk_family_menu("H03", ["Habiskan bagian yang ia tawarkan.", "\"Maaf ya, jujur asin kecap sama manisnya terlalu nabrak di lidah.\"", "\"Bahannya masih sisa kan? Kita bikin percobaan kedua bareng yuk.\""])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Melihat kesungguhan di wajahnya dan buku catatan yang penuh tulisan rapi itu, kamu memutuskan tidak merusak semangatnya di suapan pertama. Kamu mengambil sumpit, menyumpit sepotong besar, lalu memasukkannya ke mulut."
            nar "Pada detik pertama, rasa asin langsung menyambar lidahmu. Pada detik kedua, rasa manis gula menempel pekat di belakangnya, diikuti tekstur sayur yang terlalu layu dan agak gosong di bagian pinggir. Kamu menelannya dengan tenang, lalu langsung mengambil suapan kedua dan ketiga."
            chiasa "Hmm... rasanya... unik sekali, Kujo-senpai. Biar kuhabiskan saja sekalian supaya nggak mubazir."
            nar "Harumi mengerjap pelan di balik kacamatanya, menatapmu yang terus mengunyah dengan wajah terkendali sementara ujung telingamu mulai terasa panas menahan rasa asin."
            harumi "Sampai habis, Amamiya-san? Tunggu dulu, dari aromanya saja aku masih belum yakin dengan rasanya. Kenapa kecepatan mengunyahmu makin lambat di suapan ketiga?"
            chiasa "Nggak kok, aku cuma lagi menikmati bumbunya saja, Senpai."
            nar "Merasa ada yang tidak beres antara ekspresimu yang terlalu tenang dengan catatan eksperimennya sendiri, Harumi mengambil sumpit cadangan lalu mencicipi satu potong kecil dari pinggir piring."
            nar "Begitu potongan itu menyentuh lidahnya, alisnya tidak naik dan ia tidak berseru, tetapi satu detik kemudian tangannya langsung bergerak cepat menggeser piring itu menjauh dari jangkauan sumpitmu."
            harumi "Cukup. Berhenti sekarang, Amamiya-san."
            chiasa "Eh, tapi masih tinggal sedikit lagi, Senpai..."
            harumi "Kesediaanmu menghabiskannya sama sekali bukan bukti bahwa rasanya baik. Konsentrasi garam dan gulanya jelas melewati batas wajar, bahkan tenggorokanku langsung kering dari satu potong kecil tadi. Ini... ini tidak seharusnya dimakan siapa pun."
            nar "Ia segera berdiri mengambil teko dari meja samping, menuangkan segelas penuh air putih dingin, dan mendorongnya ke hadapanmu dengan raut wajah penuh penyesalan."
            harumi "Minum dulu sampai habis. Terima kasih sudah berusaha bersikap sopan dan menjaga perasaanku, tapi lain kali kamu tidak perlu melanjutkan pengorbanan seperti ini demi menghargai percobaanku."
            chiasa "Hehe... maaf ya, Senpai, aku tadi cuma nggak tega bilang gagal begitu lihat catatannya serapi itu."
            harumi "Catatanku justru hanya berguna kalau pengamatannya jujur. Lain kali kalau gagal lagi, tolong langsung bilang berhenti di suapan pertama."
            chiasa "Iya, janji lain kali aku langsung jujur di gigitan pertama."
            harumi "Tunggu di situ sebentar, aku ambilkan biskuit tawar dari lemari atas supaya rasa asin di lidahmu cepat hilang."
            nar "Kamu meneguk sisa air dingin itu dengan lega selagi Harumi menyingkirkan piring eksperimennya ke bak cuci dan mencoret halaman takaran kecap di buku catatannya."
        else:
            nar "Melihat buku catatan yang penuh hitungan rapi itu, kamu memutuskan tidak langsung menjatuhkan semangatnya. Kamu mengambil sumpit, menyumpit porsi besar, lalu memasukkannya ke mulut dengan wajah paling tenang yang bisa kamu pertahankan."
            nar "Begitu dikunyah, kombinasi rasa asin kecap yang menyengat, manis gula pekat, dan pinggiran sayur yang agak hangus langsung menyerang lidah bersamaan. Kamu menelannya cepat-cepat lalu menyumpit lagi."
            yutaka "Yah... rasanya cukup berkarakter, Kujo-san. Biar kuhabiskan saja sekalian."
            nar "Harumi mengamati caramu bertahan mengunyah di balik kacamatanya dengan sorot curiga yang sangat rasional."
            harumi "Sampai habis, Kisaragi-kun? Tunggu dulu, dari aromanya saja aku masih belum yakin dengan rasanya. Lehermu juga kelihatan tegang waktu menelan barusan."
            yutaka "Cuma kebetulan potongannya agak besar saja."
            nar "Ia mengambil sumpit cadangan dari nampan lalu mencicipi satu potong kecil dari tepi piring. Raut wajahnya tidak berubah sedikit pun, namun sedetik kemudian tangannya langsung menggeser piring itu menjauh dari jangkauanmu."
            harumi "Cukup. Berhenti sekarang."
            yutaka "Eh, masih sisa sedikit lagi nih..."
            harumi "Kesediaanmu makan sama sekali bukan bukti rasanya baik. Kadar garam dan gulanya jelas di luar rentang yang layak. Tenggorokanku sendiri langsung terasa seret. Ini tidak seharusnya dilanjutkan."
            nar "Ia segera menuangkan segelas penuh air dingin dari teko di nampan dan mendorongnya ke depanmu dengan wajah sedikit kaku karena merasa bersalah."
            harumi "Minum dulu, Kisaragi-kun. Terima kasih sudah mencoba menghargai, tapi kamu tidak perlu melanjutkan pengorbanan ini demi kesopanan."
            yutaka "Haha, oke, menyerah deh. Memang agak terlalu berani sih takaran kecapnya."
            harumi "Lain kali langsung tolak di suapan pertama supaya aku bisa mencatat kesalahan sebenarnya. Aku bereskan piring ini dulu ke dalam."
            yutaka "Iya, maaf, tadi lihat buku resepnya penuh coretan rumus begitu jadi nggak enak kalau langsung nolak."
            harumi "Dalam eksperimen apa pun, menyembunyikan hasil gagal hanya akan merusak percobaan berikutnya. Tunggu sebentar, kuambilkan air dingin satu teko lagi dari dapur."
            nar "Kamu meneguk air dingin dengan lega sementara Harumi mengangkat piring eksperimennya kembali ke dapur sambil mencatat satu tanda silang besar di buku resepnya."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kamu mengambil satu potongan kecil dengan hati-hati, mengunyahnya perlahan, lalu meneguk sedikit air sebelum menatap Harumi dengan jujur."
            chiasa "Maaf, Kujo-senpai, aku jawab jujur saja ya. Bagian asin kecap sama manis gulanya bertabrakan terlalu kuat di lidah. Terus karena apinya tadi dibesarkan, bagian luarnya agak gosong sementara bumbunya belum meresap rata ke dalam daging."
            nar "Alih-alih terlihat kecewa atau tersinggung, sorot mata Harumi di balik kacamatanya justru tampak jauh lebih tenang. Ia langsung mengambil pensil yang terselip di buku catatannya dan mulai menulis cepat."
            harumi "Rasio kecap terlalu tinggi, gula tidak seimbang, dan suhu terlalu panas di awal sehingga bagian permukaan mengering duluan. Berarti ada tiga variabel yang perlu kuubah. Terima kasih sudah mencobanya dan memberi laporan yang jelas, Amamiya-san."
            nar "Ia kemudian mengambil sumpit cadangan dan mencicipi potongan yang sama dari piring itu agar tidak sekadar menerima penilaianmu mentah-mentah. Begitu merasakannya sendiri, ia mengangguk pelan dengan wajah datar."
            harumi "...Ya. Data di lidahku cocok dengan penjelasanmu. Bahkan lebih asin daripada perkiraanku."
            chiasa "Ini tadi Kujo-senpai pakai takaran kecap berapa sendok memangnya?"
            harumi "Tiga sendok makan penuh untuk setengah porsi sayur. Di buku tertulis dua sendok untuk dua porsi, tapi tadi kupikir rasa kecap akan berkurang selama penguapan."
            chiasa "Wah, pantas saja pekat banget! Kalau airnya menguap di wajan panas, garam di dalam kecapnya justru makin kental tertinggal di bawah, Senpai."
            harumi "Masuk akal. Berarti penguapan pelarut justru menaikkan konsentrasi garamnya secara drastis, kebalikan dari dugaanku. Kalau tadi kamu cuma bilang 'enak' demi kesopanan, aku tidak akan tahu bagian mana yang salah dan mungkin akan mengulang kesalahan yang sama minggu depan."
            chiasa "Kalau apinya diturunkan ke tingkat sedang dan kecapnya baru dimasukkan paling terakhir waktu sayurnya sudah setengah layu, pasti langsung enak kok."
            harumi "Masukkan kecap di tahap akhir setelah sayur layu... tunggu, biar kutulis urutannya di halaman sebelah."
            chiasa "Kalau Senpai mau coba lagi besok-besok, kabari saja, aku siap jadi penguji rasa lagi."
            harumi "Akan kucatat tawarannya, Amamiya-san. Sebentar, biar kubuatkan teh tawar hangat untuk menetralkan rasa asin di mulutmu."
            chiasa "Terima kasih, Kujo-senpai."
        else:
            nar "Kamu menyumpit satu potongan kecil, mengunyahnya pelan, lalu menaruh sumpit di pinggir piring dan menatap Harumi dengan nada terus terang."
            yutaka "Jujur saja ya, Kujo-san. Asin kecap sama manis gulanya tabrakan terlalu keras di lidah. Terus karena apinya kebesaran di awal, luarnya keburu hangus sementara bumbunya belum meresap."
            nar "Alih-alih tersinggung, ekspresi Harumi justru langsung tampak jauh lebih lega. Ia segera mengambil pensil dari jepitan buku catatannya dan mencatat penjelasanmu dengan huruf rapi."
            harumi "Rasio kecap berlebihan, gula tidak seimbang, dan suhu terlalu tinggi di tahap awal. Berarti ada yang jelas perlu kuubah. Terima kasih sudah mencobanya, Kisaragi-kun."
            nar "Ia kemudian mencicipi bagian yang persis sama dengan sumpit cadangan agar tidak sekadar menerima penilaianmu tanpa verifikasi sendiri. Setelah menelannya, ia mengangguk singkat."
            harumi "...Ya. Hasilnya cocok dengan catatanmu. Bahkan lebih menyengat daripada perkiraanku."
            yutaka "Memangnya tadi kamu tuang kecap berapa banyak sampai bisa sepekat ini?"
            harumi "Tiga sendok makan untuk satu porsi kecil. Kupikir sebagian rasanya akan hilang menguap saat terkena wajan panas."
            yutaka "Justru airnya yang menguap, asinnya makin pekat mengendap di wajan. Kalau apinya dikecilkan sedikit dan bumbunya dimasukkan bertahap sesuai urutan resep, harusnya langsung beres kok."
            harumi "Masuk akal sekali. Aku memperlakukan kecap seperti larutan mudah menguap, padahal kandungan natriumnya tetap tertinggal di permukaan sayur."
            yutaka "Persis. Lain kali tumis daging sama sayurnya pakai api sedang dulu, baru kecapnya masuk satu sendok teh di menit terakhir sebelum kompor dimatikan."
            harumi "Satu sendok teh di menit terakhir... sudah kutulis di catatan revisi. Kalau kamu tadi memuji demi kesopanan, aku tidak akan bisa memperbaiki apa pun."
            yutaka "Santai saja. Lain kali kalau bikin percobaan kedua, panggil saja lagi biar kucek."
            harumi "Baik, akan kucatat. Tunggu sebentar, kuambilkan teh hangat dari dapur untuk membersihkan rasa asin di lidahmu."
            yutaka "Makasih, Kujo-san."
    else:
        if kk_host == "chiasa":
            nar "Kamu mencicipi sedikit ujung sendok bumbunya, mengernyit tipis, lalu melirik bahan-bahan segar yang rupanya masih tersisa cukup banyak di meja dapur belakang Harumi."
            chiasa "Kujo-senpai, bahannya kan masih ada sisa setengah lagi di dekat kompor. Gimana kalau kita bikin percobaan kedua sekarang bareng-bareng? Biar aku ikut bantu jaga api sama cicipi di tengah jalan."
            nar "Harumi terdiam sejenak, memandang sisa kubis, wortel, dan irisan daging di meja dapur lalu kembali menatapmu dengan mata berbinar tipis."
            harumi "Dua orang untuk satu percobaan. Itu... ide yang rasional. Kalau begitu kamu yang cicipi dulu di setiap tahap sebelum aku menambahkan bumbu lagi, Amamiya-san."
            chiasa "Siap. Tapi buku catatannya ditaruh agak jauh dulu dari wajan biar nggak kena cipratan minyak, ya."
            harumi "Baik, kutaruh di meja belakang sini. Wajan bersihnya sudah siap, minyaknya kutuang satu sendok makan rata dulu ya."
            chiasa "Tunggu wajannya hangat dulu baru masukkan bawang putih sama dagingnya, jangan langsung api besar."
            harumi "Dicatat. Api sedang, tumis sampai aroma bawang keluar baru masukkan irisan daging."
            nar "Lima belas menit berikutnya di dapur asrama berubah jauh lebih hidup daripada suasana tenang biasanya. Kamu mengambil alih urusan menjaga api kompor tetap sedang dan mengaduk wajan, sementara Harumi menakar bumbu di sebelahmu sambil terus berdebat ringan soal istilah resep."
            harumi "Amamiya-san, di buku ini tertulis 'garam secukupnya'. Berapa gram definisi 'secukupnya' menurutmu?"
            chiasa "Nggak usah ditimbang pakai gram, Senpai. Cukup sejumput pakai ujung jari, aduk, terus kita cicipi. Kalau kurang baru tambah lagi."
            harumi "Metode coba-coba tanpa standar awal itu tidak efisien... tapi baiklah, aku coba ikuti caramu kali ini."
            nar "Ia menjepit sejumput kecil garam dan menaburkannya ke atas wajan dengan ketegangan penuh seolah sedang menuang reagen kimia berbahaya, sampai kamu tidak tahan untuk tertawa kecil."
            chiasa "Haha, santai saja, Senpai, garamnya nggak bakal meledak kok kalau jatuh ke wajan."
            harumi "Aku hanya tidak ingin mengulang kelebihan natrium seperti di piring pertama."
            chiasa "Nah, sekarang tuang kecapnya satu sendok makan saja dari pinggir wajan, lalu aduk rata bareng kubisnya."
            nar "Melihatmu tertawa, ketegangan di bahu Harumi ikut meluruh. Sudut bibirnya terangkat membentuk senyum tipis yang tulus bahkan sebelum masakan keduanya selesai matang."
            harumi "...Ternyata bagian yang menyenangkan dari memasak tidak harus menunggu hasil akhirnya jadi sempurna dulu. Aku baru tahu."
            chiasa "Nah, sekarang matikan kompornya terus coba Senpai cicipi sedikit. Jauh lebih mendingan kan?"
            nar "Harumi mengambil sendok kecil, meniup uapnya pelan, lalu mencicipi kuah tumisan kedua itu. Matanya membesar sedikit sebelum ia mengangguk puas dengan raut wajah hangat."
            harumi "Rasanya seimbang. Tidak ada yang hangus dan manisnya pas. Kalau kamu belum makan malam, ayo kita makan bersama sekarang selagi hangat, Amamiya-san."
            chiasa "Boleh banget, aku ambilkan dua mangkuk nasi dari meja sudut dulu ya, Senpai."
            harumi "Sebentar, nasi di penanak juga baru matang tadi. Terima kasih banyak sudah membantu malam ini, Amamiya-san."
            chiasa "Sama-sama, Senpai. Jangan lupa tulis takaran percobaan kedua ini di buku resepnya biar besok-besok nggak balik ke tiga sendok kecap lagi."
            harumi "Sudah kusiapkan halaman baru khusus untuk prosedur revisi kita malam ini."
        else:
            nar "Kamu mencicipi sedikit ujung kuahnya, mengernyit tipis, lalu melirik lewat jendela samping dapur bersama yang terbuka, tempat masih ada sisa bahan segar di atas meja dapur di dalam."
            yutaka "Masih ada sisa bahannya kan, Kujo-san? Aku memang nggak boleh masuk ke dalam area dapur asrama, tapi kalau aku berdiri di dekat jendela samping sini buat jaga-jaga dan cicipi tiap tahap sebelum kamu tambahin bumbu lagi, gimana? Kita bikin percobaan kedua bareng."
            nar "Harumi menoleh ke arah jendela lebar yang menghubungkan konter dapur dengan teras ruang tamu, lalu kembali menatapmu dengan mata berbinar tipis."
            harumi "Dua orang untuk satu percobaan, satu di depan kompor dan satu sebagai penguji rasa di jendela. Itu cukup rasional. Kalau begitu kamu cicipi dulu setiap kali aku memasukkan bumbu, sebelum aku menambahkannya lagi."
            yutaka "Setuju. Tapi jauhkan dulu buku catatanmu dari kompor biar nggak ikut gosong."
            harumi "Baik, kusimpan di rak belakang. Aku panaskan wajan bersih dengan api sedang sesuai saranmu."
            yutaka "Tunggu bawang putihnya harum dulu baru masukkan daging, jangan langsung dituang barengan sama kecap."
            harumi "Mengerti. Tahap satu tumis bawang dan daging, tahap dua baru masukkan sayur dan bumbu."
            nar "Lima belas menit berikutnya berubah menjadi adegan yang jauh lebih hangat dan menghibur daripada bayanganmu. Kamu bersandar santai di kusen jendela luar dapur, menerima sendok kecil cicipan yang Harumi ulurkan setiap beberapa menit sambil berdebat ringan soal istilah resep."
            harumi "Di resep tertulis 'garam secukupnya'. Kisaragi-kun, secara kuantitatif berapa gram batas 'secukupnya' itu?"
            yutaka "Nggak ada gramnya, Kujo-san. Ambil sejumput pakai ujung jari, aduk, terus sodorkan ke sini biar kucicipi. Kalau kurang baru tambah lagi."
            harumi "Metode coba-coba tanpa angka awal itu sangat tidak terukur... tapi baiklah, aku coba ikuti caramu."
            nar "Melihatnya menaburkan sejumput garam dengan ketegangan penuh seolah sedang mencampur larutan kimia membuatmu tidak tahan untuk tertawa kecil dari balik kusen jendela."
            yutaka "Santai saja, Kujo-san, wajannya nggak bakal meledak cuma gara-gara kelebihan dua butir garam."
            harumi "Aku hanya tidak ingin mengulang kesalahan rasio dari percobaan pertama."
            yutaka "Nah, sekarang baru masuk kecap satu sendok makan, terus aduk cepat sebelum sayurnya kelayuan."
            nar "Mendengar tawamu dari balik jendela, bahu Harumi ikut melonggar. Sudut bibirnya terangkat membentuk senyum tipis yang tulus bahkan sebelum masakan keduanya selesai matang."
            harumi "...Ternyata bagian yang menyenangkan tidak harus menunggu hasil akhirnya jadi sempurna dulu. Aku baru tahu."
            yutaka "Nah, coba sekarang kamu sendiri yang cicipi. Beda jauh kan?"
            nar "Harumi mencicipi sesendok kecil dari wajan sambil meniup uapnya, lalu mengangguk pelan dengan raut puas yang hangat."
            harumi "Jauh lebih seimbang. Kalau kamu belum makan malam, tunggu di ruang tamu sebentar, biar kusiapkan dua piring untuk kita berdua."
            yutaka "Siap, aku bantu rapikan meja ruang tamunya dulu."
            harumi "Tunggu dua menit ya, nasinya baru saja matang di penanak."
            yutaka "Jangan lupa piring pertama yang keasinan tadi disisihkan dulu biar nggak ketukar waktu dibawa keluar."
            harumi "Tenang saja, piring yang itu sudah resmi masuk daftar sampel gagal di bak cuci."
    return

# ┌─ PANDUAN CERITA · H-D05 · Masakan Kedua
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kujo Harumi
# │ AWALAN  : H03-C pernah terjadi
# │ INTI    : A Puji dengan spesifik / B jujur / C ajak memasak lagi
# │ AKHIRAN : ia menghubungkan "senang" dengan "memasak bersama"; kejelasan +
# └─ tulis / perbaiki dialog di bawah ──
label kk_second_meal:
    if kk_host == "chiasa":
        nar "Di ruang makan kecil Asrama Putri malam ini, Harumi sudah menata dua mangkuk sup hangat dan tumisan sederhana di atas meja. Berbeda dari percobaan sebelumnya, tidak ada buku catatan takaran gram maupun pengatur waktu di samping piring."
        chiasa "Wah, baunya enak banget, Kujo-senpai! Catatan resepnya kali ini nggak dibawa keluar ya?"
        harumi "Sengaja kutinggal di kamar, Amamiya-san. Aku mengulang masakan kita waktu itu dengan porsi lebih kecil. Tadi sempat mau kirim foto dulu lewat ponsel, tapi akhirnya aku pengin lihat ekspresimu waktu mencicipi langsung."
    else:
        nar "Di ruang tamu lobi Asrama Putri yang hangat malam ini, Harumi muncul membawa kotak makan bertingkat yang masih mengepul tipis bersama dua pasang sumpit. Tidak ada buku catatan takaran ataupun kertas tabel eksperimen di tangannya kali ini."
        yutaka "Wah, harum banget dari tadi, Kujo-san. Kali ini nggak bawa buku catatan gram sama pengatur waktu lagi?"
        harumi "Nggak kubawa, Kisaragi-kun. Aku mencoba mengulang masakan kita kemarin dengan porsi yang lebih pas. Tadi hampir cuma kukirim fotonya, tapi aku sadar aku lebih ingin melihat reaksimu langsung begitu mencicipinya."
    nar "Ia mencondongkan tubuh sedikit menunggu suapan pertamamu sebelum menjelaskan satu pun perubahan bumbu yang ia lakukan."
    call kk_family_menu("H-D05", ["Tunjukkan rasa yang kali ini lebih seimbang.", "Katakan dengan jujur apa yang masih kurang.", "Ajak dia memasak bersama lagi."])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Wah, kali ini bumbunya jauh lebih seimbang, Kujo-senpai! Rasa manis bawangnya keluar pelan, terus asinnya nggak menyengat kayak percobaan pertama dulu."
        else:
            yutaka "Jauh lebih seimbang kali ini, Kujo-san. Kaldu sama manis bawangnya nyatu rapi, nggak keasinan lagi di ujung lidah."
        harumi "...Kamu juga bisa merasakan bedanya ya? Aku senang."
        nar "Ia sempat terdiam sejenak lalu mengulang kata senang dengan suara lebih pelan, seolah baru saja mencocokkan nama emosi yang benar di kepalanya. Setelah itu ia menarik mangkuk bagiannya sendiri dan ikut makan bersama tanpa hanya duduk menunggu penilaianmu."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Secara keseluruhan sudah enak banget, Kujo-senpai, cuma potongan wortelnya masih agak keras sedikit di tengah. Kalau apinya dikecilkan dua menit lebih lama pasti langsung lembut."
        else:
            yutaka "Rasanya sudah jauh lebih bagus, Kujo-san, cuma tingkat kematangan wortelnya masih agak keras sedikit. Tinggal tambah dua menit di api kecil pasti sempurna."
        harumi "Wortelnya kurang empuk dua menit ya... baik, kucatat di kepala. Aneh ya, biasanya dengar kekurangan begitu bikin aku frustrasi, tapi sekarang aku malah pengin coba masak lagi. Rupanya aku menyukai proses ini."
        nar "Ia menanyakan satu detail kecil lalu membiarkan sisa perbaikannya untuk lain hari, tidak lagi merasa setiap kekurangan harus langsung dibereskan sebelum ia berhak menikmati makan malam."
    else:
        if kk_host == "chiasa":
            chiasa "Ini sudah enak banget, Kujo-senpai! Kapan-kapan kita masak bareng lagi yuk, aku mau coba resep kari rumahan sekalian sama Senpai."
        else:
            yutaka "Sudah enak banget ini, Kujo-san. Lain kali kita masak bareng lagi yuk, sekalian coba menu baru."
        harumi "Boleh banget. Jujur saja, aku memang lebih senang waktu kita membuatnya berdua dibanding sendirian di dapur."
        nar "Kali ini ia tidak memutar kalimatnya menjadi alasan efisiensi kerja. Kalian langsung mencocokkan hari kosong dan membagi daftar bahan belanja, dan kesepakatan kecil itu saja sudah cukup menerbitkan senyum tenang di wajah Harumi."
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
