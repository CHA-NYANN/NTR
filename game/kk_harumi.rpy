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
            nar "Selama beberapa belas menit berikutnya, hanya bunyi lembut goresan pensil, helaan napas teratur, dan gesekan kertas yang menemani kalian berdua. Keheningan di sudut meja itu terasa jauh lebih hangat dan nyaman daripada basa-basi perkenalan di kampus."
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
            nar "Harumi mengangguk pelan seolah kesepakatan lurus itu sudah menenangkan pikirannya, lalu kembali menurunkan pandangannya ke kertas hitungannya. Kalian berdua duduk berdampingan dalam sunyi yang teratur selama beberapa belas menit di bawah cahaya pagi. Cara kerjanya yang sabar dan tanpa basa-basi itu terasa jauh lebih hangat daripada keramahan yang dibuat-buat."
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
        chiasa "Bagus dong hasilnya, Kujo-senpai. Terus yang bagian bawahnya soal hubungan atau perasaan gimana?"
        nar "Harumi tidak langsung menjawab. Pandangannya menempel di kolom tengah kertas tersebut. Kamu melihat bibirnya bergerak pelan membaca baris yang sama untuk kedua kalinya, lalu ketiga kalinya."
        harumi "'Perhatikan hatimu.'"
        chiasa "Cuma dua kata itu aja, Senpai?"
        harumi "Di bawahnya ada tambahan singkat yang berbunyi, 'jangan menunggu semuanya selesai baru menyadari apa yang tertinggal.' Kalau itu dimaksudkan sebagai instruksi, kriterianya sangat buruk dan tidak terukur."
        nar "Meski mengkritiknya secara logis, Harumi sama sekali belum melipat kertas itu. Ia menurunkan sedikit tangannya lalu melirik keramaian pengunjung di sekitar kuil."
        harumi "Tapi terus terang, Amamiya-san... aku tetap ingin tahu apa maksudnya. Selama ini aku memang punya kebiasaan yang cukup mengganggu. Aku sering baru sadar kalau diriku sebenarnya sedang sedih, lelah, atau kecewa beberapa jam setelah semua orang sudah pulang dan ruangannya kembali kosong."
    else:
        nar "Pelataran kuil pada hari-hari pertama Tahun Baru masih dipadati pengunjung yang berlalu-lalang mengenakan mantel tebal. Di tepi halaman dekat rak kayu pengikat omikuji, Kujo Harumi berdiri agak menyamping agar tidak menghalangi jalan sambil membuka selembar kertas ramalan yang baru ia ambil."
        nar "Cara ia menatap kertas tipis itu sama sekali tidak terlihat seperti orang yang sedang mencari hiburan Tahun Baru. Keningnya sedikit berkerut, kacamatanya dinaikkan sekali dengan telunjuk, lalu ia membacakan tiap bagian dengan nada terukur persis seperti memeriksa lembar prosedur praktikum."
        harumi "Keberuntungan umumnya sedang. Bagian studi dan riset bilang ketekunan pada rincian kecil membawa hasil sebelum musim panas. Bagian kesehatan mengingatkan agar tidak memotong jam tidur demi pekerjaan yang bisa dibagi. Semua bagian itu jelas dan masuk akal."
        yutaka "Bagus dong hasilnya, Kujo-san. Terus bagian bawahnya soal hubungan gimana?"
        nar "Harumi tidak langsung menjawab. Matanya tertahan cukup lama pada kolom tengah kertas tersebut. Kamu melihat bibirnya bergerak pelan mengulang baris yang sama sampai tiga kali berturut-turut."
        harumi "'Perhatikan hatimu.'"
        yutaka "Cuma itu doang isinya?"
        harumi "Di bawahnya ada tambahan singkat berbunyi, 'jangan menunggu semuanya selesai baru menyadari apa yang tertinggal.' Kalau itu dimaksudkan sebagai instruksi, kriterianya sangat buruk dan sama sekali tidak terukur."
        nar "Kendati mengkritiknya dengan logis, Harumi belum juga melipat kertas itu. Ia menurunkan sedikit tangannya lalu memandang keramaian di sekitar pelataran kuil."
        harumi "Tapi terus terang, Kisaragi-kun... aku tetap ingin mengerti maksudnya. Aku punya kebiasaan yang cukup mengganggu. Aku sering baru sadar kalau diriku sebenarnya sedang sedih atau kecewa beberapa jam setelah semua orang pulang."
    menu:
        "\"Nggak usah langsung cari istilah yang berat. Mulai dari yang paling gampang dirasakan sekarang aja.\"":
            $ kk_record_choice("H08", "A")
            if kk_host == "chiasa":
                chiasa "Menurutku Kujo-senpai nggak usah memaksa diri langsung cari nama emosi yang besar atau istilah yang rapi buat dicatat di buku. Mulai aja dari hal paling kecil yang gampang Senpai rasakan detik ini juga."
                nar "Harumi menoleh kepadamu dari balik lensa kacamatanya dengan kening masih agak berkerut."
                harumi "Hal paling kecil yang kurasakan sekarang? Maksudnya seperti suhu udara?"
                chiasa "Bukan suhu udara, Senpai. Misalnya, sekarang ini Senpai lagi pengin berdiri agak dekat atau pengin mundur ke tempat sepi? Lagi merasa agak lega, atau malah tegang? Pengin cepat pulang ke asrama, atau masih betah di sini sebentar? Nggak perlu langsung tahu itu namanya senang atau sayang."
                nar "Harumi terdiam memikirkan kalimatmu. Ia mengedarkan pandangan ke kerumunan orang-orang di depan tangga kuil, lalu kembali melihat ke arahmu. Setelah jeda beberapa detik, tanpa berkata apa-apa ia menggeser langkahnya setengah tapak berdiri lebih dekat ke sisimu di dekat pagar kayu yang lebih teduh dari angin."
                harumi "Kalau memakai metode sederhana seperti itu... saat ini aku tidak ingin buru-buru kembali ke asrama. Aku ingin tetap berdiri di sini sebentar lagi bersama Amamiya-san, sebelum kita turun membeli teh hangat."
                chiasa "Nah, itu dia. Gampang kan, Senpai?"
                harumi "...Iya. Aku ingin tetap di sini sebentar. Ternyata tanpa harus mencari istilah rumit, satu kalimat itu sudah cukup menjadi informasi yang jelas."
                nar "Harumi melipat kertas omikuji itu dengan hati-hati lalu memasukkannya ke saku dalam mantel abu-abunya alih-alih mengikatnya di rak kayu. Sudut bibirnya melengkung tipis sebelum ia menanyakan apakah kamu ingin mencoba minuman jahe hangat di kedai bawah tangga."
            else:
                yutaka "Kamu nggak perlu langsung cari nama emosi yang besar atau istilah rapi buat dimasukin ke catatan, Kujo-san. Mulai aja dari hal paling kecil yang bisa kamu rasakan detik ini juga."
                nar "Harumi menoleh dari balik kacamatanya dengan kening masih sedikit berkerut."
                harumi "Hal paling kecil yang kurasakan sekarang? Jadi aku boleh mulai dari reaksi sederhana saja?"
                yutaka "Iya. Misalnya sekarang ini kamu pengin berdiri lebih dekat atau pengin mundur menjauh, merasa agak lega atau malah tegang, mau buru-buru balik ke asrama atau masih betah di sini sebentar. Nggak usah langsung mikir namanya senang, sedih, atau sayang."
                nar "Harumi terdiam sejenak menimbang kalimatmu. Ia menatap arus pengunjung di dekat tangga kuil, lalu kembali menoleh ke arahmu. Perlahan, ia melangkah setengah tapak lebih dekat ke sisimu di dekat pagar kayu yang agak terlindung dari angin."
                harumi "Kalau memakai patokan sesederhana itu... sekarang aku tidak ingin buru-buru pulang ke asrama. Aku ingin tetap berdiri di sini sebentar lagi bersama Kisaragi-kun."
                yutaka "Nah, gampang kan?"
                harumi "...Iya. Aku ingin tetap di sini sebentar. Ternyata satu kalimat itu saja sudah menjadi informasi yang cukup jelas."
                nar "Harumi melipat kertas ramalannya dengan rapi lalu memasukkannya ke saku dalam mantel abu-abunya. Sudut bibirnya terangkat tipis sebelum ia mengajakmu turun mencari teh hangat di kedai dekat gerbang."
        "\"Haha, kalimat seumum itu sih memang sengaja dibikin biar cocok buat siapa aja.\"":
            $ kk_record_choice("H08", "B")
            if kk_host == "chiasa":
                nar "Kamu tertawa ringan sambil melirik kertas ramalan di tangan Harumi."
                chiasa "Ya ampun, Kujo-senpai serius banget sih nganalisis kertas omikuji. Kalimat kayak 'perhatikan hatimu' kan sengaja ditulis seumum mungkin supaya siapa pun yang baca, mulai dari anak SMP sampai kakek-kakek, pasti merasa kesindir semua!"
                nar "Harumi berkedip sejenak, lalu menurunkan kertas putih itu dan ikut mengangguk kecil seolah tersadar dari lamunannya sendiri."
                harumi "Benar juga. Secara statistik, pernyataan yang sangat kabur memang memiliki tingkat kecocokan subjektif yang tinggi bagi pembaca mana pun. Aku terlalu berlebihan menganggapnya sebagai petunjuk."
                chiasa "Nah, kan. Kalau dipikir terus nanti malah bikin kepala Senpai penuh sendiri padahal ini lagi hari libur."
                harumi "Iya. Sebaiknya tidak usah kubawa pikiran."
                nar "Harumi segera melipat kertas ramalannya menjadi lipatan persegi kecil dan menyimpannya ke dalam saku mantel. Ia membetulkan kacamatanya sekali lagi, lalu langsung mengalihkan pembicaraan ke jadwal pembukaan laboratorium minggu depan tanpa pernah kembali menyinggung pengakuannya soal rasa sedih yang terlambat ia sadari tadi."
            else:
                nar "Kamu tertawa ringan sambil menatap kertas putih di tangan Harumi."
                yutaka "Jangan diseriusin banget dong, Kujo-san. Kalimat seumum 'perhatikan hatimu' itu memang sengaja dibikin kabur biar siapa pun yang baca pasti merasa kena."
                nar "Harumi berkedip singkat, lalu menurunkan tangannya dan mengangguk kecil seolah baru tersadar sendiri."
                harumi "Kamu benar. Secara statistik, pernyataan yang tidak spesifik memang bisa diterapkan pada hampir semua orang. Aku terlalu berlebihan memperlakukannya seperti petunjuk."
                yutaka "Nah, mending jangan dibawa pusing di hari libur begini."
                harumi "Iya. Sebaiknya aku berhenti menganalisisnya."
                nar "Harumi melipat kertas omikuji itu rapi-rapi dan memasukkannya ke saku mantel. Ia membetulkan letak kacamatanya lalu langsung mengganti topik ke jadwal kuliah minggu depan, tidak lagi menanyakan atau menyinggung bagian tentang dirinya yang terlambat menyadari rasa sedih tadi."
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
            nar "Kamu meneguk air dingin itu dengan lega sambil tersenyum tipis melihat Harumi menyingkirkan piring eksperimennya ke bak cuci dengan wajah yang jauh lebih bersalah daripada kesal."
        else:
            nar "Melihat buku catatan yang penuh hitungan rapi itu, kamu memutuskan tidak langsung menjatuhkan semangatnya. Kamu mengambil sumpit, menyumpit porsi besar, lalu memasukkannya ke mulut dengan wajah paling tenang yang bisa kamu pertahankan."
            nar "Begitu dikunyah, kombinasi rasa asin kecap yang menyengat, manis gula pekat, dan pinggiran sayur yang agak hangus langsung menyerang lidah bersamaan. Kamu menelannya cepat-cepat lalu menyumpit lagi."
            yutaka "Yah... rasanya cukup berkarakter, Kujo-san. Biar kuhabiskan saja sekalian."
            nar "Harumi mengerjap pelan di balik kacamatanya, mengamati caramu bertahan mengunyah dengan sorot curiga yang sangat rasional."
            harumi "Sampai habis, Kisaragi-kun? Tunggu dulu, dari aromanya saja aku masih belum yakin dengan rasanya. Lehermu juga kelihatan tegang waktu menelan barusan."
            yutaka "Cuma kebetulan potongannya agak besar saja."
            nar "Ia mengambil sumpit cadangan dari nampan lalu mencicipi satu potong kecil dari tepi piring. Raut wajahnya tidak berubah sedikit pun, tetapi sedetik kemudian tangannya langsung menggeser piring itu menjauh dari jangkauanmu."
            harumi "Cukup. Berhenti sekarang."
            yutaka "Eh, masih sisa sedikit lagi nih..."
            harumi "Kesediaanmu makan sama sekali bukan bukti rasanya baik. Kadar garam dan gulanya jelas di luar rentang yang layak. Tenggorokanku sendiri langsung terasa seret. Ini tidak seharusnya dilanjutkan."
            nar "Ia segera menuangkan segelas penuh air dingin dari teko di nampan dan mendorongnya ke depanmu dengan wajah sedikit kaku karena merasa bersalah."
            harumi "Minum dulu, Kisaragi-kun. Terima kasih sudah mencoba menghargai, tapi kamu tidak perlu melanjutkan pengorbanan ini demi kesopanan."
            yutaka "Haha, oke, menyerah deh. Memang agak terlalu berani sih takaran kecapnya."
            harumi "Lain kali langsung tolak di suapan pertama supaya aku bisa mencatat kesalahan sebenarnya. Aku bereskan piring ini dulu."
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
            chiasa "Wah, pantas saja pekat banget! Kalau apinya dikecilkan sedikit dan bumbunya dimasukkan bertahap sesuai resep asli, harusnya langsung jauh lebih enak kok, Senpai."
            harumi "Masuk akal. Berarti penguapan air justru menaikkan konsentrasi garamnya, kebalikan dari dugaanku. Kalau tadi kamu cuma bilang 'enak' demi kesopanan, aku tidak akan tahu bagian mana yang salah dan mungkin akan mengulang kesalahan yang sama minggu depan."
            chiasa "Kalau Senpai mau coba lagi besok-besok, kabari saja, aku siap jadi juri jujur lagi."
            harumi "Akan kucatat tawarannya, Amamiya-san. Sebentar, biar kubuatkan teh tawar hangat untuk menetralkan rasa asin di mulutmu."
            nar "Ia membetulkan letak kacamatanya dengan ekspresi lega yang tulus. Baginya, kritik yang jujur dan bisa dipakai memahami hasil jauh lebih melegakan daripada pujian kosong."
        else:
            nar "Kamu menyumpit satu potongan kecil, mengunyahnya pelan, lalu menaruh sumpit di pinggir piring dan menatap Harumi dengan nada terus terang."
            yutaka "Jujur saja ya, Kujo-san. Asin kecap sama manis gulanya tabrakan terlalu keras di lidah. Terus karena apinya kebesaran di awal, luarnya keburu hangus sementara bumbunya belum meresap."
            nar "Alih-alih tersinggung, ekspresi Harumi justru langsung tampak jauh lebih lega. Ia segera mengambil pensil dari jepitan buku catatannya dan mencatat penjelasanmu dengan huruf rapi."
            harumi "Rasio kecap berlebihan, gula tidak seimbang, dan suhu terlalu tinggi di tahap awal. Berarti ada yang jelas perlu kuubah. Terima kasih sudah mencobanya, Kisaragi-kun."
            nar "Ia kemudian mencicipi bagian yang persis sama dengan sumpit cadangan agar tidak sekadar menerima penilaianmu tanpa verifikasi sendiri. Setelah menelannya, ia mengangguk singkat."
            harumi "...Ya. Hasilnya cocok dengan catatanmu. Bahkan lebih menyengat daripada perkiraanku."
            yutaka "Memangnya tadi kamu tuang kecap berapa banyak sampai bisa sepekat ini?"
            harumi "Tiga sendok makan untuk satu porsi kecil. Kupikir sebagian rasanya akan hilang menguap saat terkena wajan panas."
            yutaka "Justru airnya yang menguap, asinnya makin pekat di wajan. Kalau apinya dikecilkan sedikit dan bumbunya dimasukkan bertahap sesuai urutan resep, harusnya langsung beres kok."
            harumi "Masuk akal sekali. Kalau kamu tadi memuji demi kesopanan, aku tidak akan bisa memperbaiki apa pun. Kritik yang jelas jauh lebih membantu."
            yutaka "Santai saja. Lain kali kalau bikin percobaan revisi, panggil saja lagi biar kucek."
            harumi "Baik, akan kucatat. Tunggu sebentar, kuambilkan teh hangat dari dapur untuk membersihkan rasa asin di lidahmu."
            nar "Ia membetulkan letak kacamatanya dengan raut puas yang tenang. Baginya, kejujuran yang bisa dipakai memahami hasil jauh lebih berharga daripada pujian kosong."
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
            chiasa "Nah, sekarang tuang kecapnya satu sendok makan saja, lalu aduk rata bareng kubisnya."
            nar "Melihatmu tertawa, ketegangan di bahu Harumi ikut meluruh. Sudut bibirnya terangkat membentuk senyum tipis yang tulus bahkan sebelum masakan keduanya selesai matang."
            harumi "...Ternyata bagian yang menyenangkan dari memasak tidak harus menunggu hasil akhirnya jadi sempurna dulu. Aku baru tahu."
            chiasa "Nah, sekarang matikan kompornya terus coba Senpai cicipi sedikit. Jauh lebih mendingan kan?"
            nar "Harumi mengambil sendok kecil, meniup uapnya pelan, lalu mencicipi kuah tumisan kedua itu. Matanya membesar sedikit sebelum ia mengangguk puas dengan raut wajah hangat."
            harumi "Rasanya seimbang. Tidak ada yang hangus dan manisnya pas. Kalau kamu belum makan malam, ayo kita makan bersama sekarang selagi hangat, Amamiya-san."
            chiasa "Boleh banget, aku ambilkan dua mangkuk nasi dulu ya."
            harumi "Sebentar, nasi di penanak juga baru matang tadi. Terima kasih banyak sudah membantu, Amamiya-san."
            nar "Aroma dapur malam itu akhirnya benar-benar tercium seperti makanan rumahan yang layak dinikmati bersama."
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
            yutaka "Siap, aku bantu rapikan mejanya di sini."
            harumi "Tunggu dua menit ya, nasinya baru saja matang."
            nar "Aroma yang keluar dari jendela dapur malam itu akhirnya benar-benar tercium seperti masakan rumah yang layak dinikmati bersama."
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
