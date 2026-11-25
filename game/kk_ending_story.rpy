# ============================================================================
# PANDUAN & NASKAH 220 ENDING KOUSEIKAN
# ----------------------------------------------------------------------------
# Ending BUKAN scene berdialog: ia kartu teks (screen kk_ending_card) yang isinya
# diambil dari field "body". File ini tempatmu MENULIS ULANG / memperkaya teks
# tiap ending. Cara pakai:
#   1. Cari ending yang mau kamu tulis (dikelompokkan per karakter di bawah).
#   2. Hapus "# " pada baris KK_END_TEXT[...] = ... lalu tulis ceritamu di antara
#      tanda kutip. Untuk banyak baris pakai """...""".
#   3. Biarkan tetap komentar (atau kosong) = kartu memakai teks ringkas katalog.
# "KAPAN" = syarat ending itu muncul (ditarik resolver akumulatif). "ISI SKRG" =
# teks ringkas katalog yang sekarang tampil.
# ============================================================================

init -5 python:
    KK_END_TEXT = {}

init python:
    pass  # (jangan hapus) menjaga blok tetap valid walau semua teks di bawah masih komentar
    # --- tulis/aktifkan baris di bawah untuk menimpa teks ending ---

    # ═════ Koita ═════
    # ┌─ ENDING · E-KO-01 · Dipilih: Miyuki  [Koita · host Y/C]
    # │ KAPAN   : Miyuki masih memilih Koita; Koita memilihnya
    # │ ISI SKRG: jalur manga; cinta SMA Koita akhirnya diakui
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-01"] = """Koita datang ke apartemen Miyuki dengan tangan kosong. Ia sengaja tidak membawa bunga agar tidak bisa bersembunyi di balik hadiah ketika ditanya apa maksud kedatangannya. Di depan perempuan yang sudah terlalu sering menerima perhatian tanpa kepastian, ia akhirnya mengatakan cinta yang dahulu tak berani ia akui sejak SMA.

Miyuki tidak langsung memeluknya. Ia menanyakan orang-orang lain, pesan-pesan yang perlu dijelaskan, dan apa yang akan berubah setelah malam ini. Koita menjawab satu per satu. Ada jawaban yang buruk; kali ini ia membiarkannya terdengar buruk daripada membuatnya indah dan kabur.

Pada malam Miyuki pulang dari rumah sakit terlalu lelah untuk bersikap manis, Koita sudah menunggu di dapur apartemennya. Ia mematikan kompor, menyelimuti Miyuki yang tertidur di sofa dengan jas putih masih di pangkuan, lalu mencuci dua piring di bak tanpa membangunkannya."""

    # ┌─ ENDING · E-KO-02 · Dipilih: Nagisa  [Koita · host Y/C]
    # │ KAPAN   : harapan_koita Nagisa tegak
    # │ ISI SKRG: teman masa kecil yang akhirnya dijawab
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-02"] = """Nagisa sudah menyiapkan kemarahan untuk menutupi apa pun jawaban Koita. Namun ketika ia akhirnya menyebut cinta dengan jelas, seluruh kalimat tajam itu mendadak tidak berguna. Ia hanya bertanya apakah Koita sungguh memahami yang sedang dikatakannya.

Koita tidak menjawab dengan kisah boneka kelinci atau masa kecil. Ia menyebut Nagisa yang sekarang: keras kepala, mudah khawatir, dan berhak pergi jika ia kembali menggantungnya. Barulah Nagisa menangis, kesal karena tangisnya datang sebelum ia sempat terlihat anggun.

Koko tetap duduk di rak kamar Nagisa, di sebelah maket yang belum selesai. Mereka masih berdebat soal jam pulang dan pesan yang terlambat dibalas, tetapi saat teman studio bertanya siapa yang menunggu di bawah, Nagisa menyebut nama Koita sebagai pacarnya tanpa menoleh untuk memeriksa reaksi."""

    # ┌─ ENDING · E-KO-03 · Dipilih: Harumi  [Koita · host Y/C]
    # │ KAPAN   : Harumi tahap ≤ 2; Koita memilihnya
    # │ ISI SKRG: variabel tetap
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-03"] = """Harumi meminta Koita mengulang pengakuannya. Bukan karena ia tidak mendengar, melainkan karena selama ini terlalu banyak perkataan baik yang bisa berarti apa saja. Koita mengulang dengan kalimat lebih pendek, sampai tidak ada bagian yang perlu ditafsirkan.

Ia memilih Harumi. Ia ingin menjadi pasangannya. Ia memahami bahwa jawaban Harumi belum tentu sama.

Harumi diam lama, lalu mengatakan ya dengan suara yang nyaris hilang di antara rak buku. Setelah itu ia langsung membuka buku agenda dan membacakan batas waktunya: jam laboratorium, jadwal tidur, serta malam-malam ketika ia tidak ingin diganggu. Koita mencatat semuanya di ponselnya sendiri, lalu menggeser cangkir teh hangat ke dekat tangan Harumi."""

    # ┌─ ENDING · E-KO-04 · Dipilih: Moeka  [Koita · host Y/C]
    # │ KAPAN   : Moeka selamat; hatinya ke Koita
    # │ ISI SKRG: Koita belajar menepati janji
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-04"] = """Moeka terlambat dua belas menit pada kencan pertama mereka. Ia datang dengan napas putus-putus dan lelucon yang disiapkan untuk mendahului teguran. Koita mengatakan ia sudah membaca pesan keterlambatannya, lalu bertanya apakah ia sempat makan.

Perhatian sederhana itu tidak menyembuhkan semua yang pernah terjadi. Keluarga Moeka masih memerlukan bantuan, beasiswanya masih menuntut kerja, dan ada pagi ketika bangun terasa jauh lebih berat daripada yang terlihat dari fotonya. Namun Koita berhenti menawarkan janji besar yang bisa ia lupakan setelah suasana membaik.

Ia datang pada waktu yang disepakati, dan jika terlambat lima menit, pesannya sudah masuk lebih dulu. Ketika Moeka suatu sore berkata kepalanya pusing dan ia tidak sanggup bercanda, Koita hanya membelikan air hangat dari mesin penjual otomatis lalu duduk diam di sebelahnya sampai kereta berikutnya tiba."""

    # ┌─ ENDING · E-KO-05 · Dipilih: Shiori  [Koita · host Y/C]
    # │ KAPAN   : cinta Koita tumbuh di S08
    # │ ISI SKRG: lawan yang ia kira tak tersentuh
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-05"] = """Shiori menolak undangan makan malam yang disusun seperti kesepakatan keluarga. Jika Koita ingin menemuinya, ia bisa mengajaknya sendiri, dengan tempat dan jam yang jelas. Koita melakukannya, lalu datang dua puluh menit terlalu awal karena gugup.

Di hadapannya, Shiori tidak menjadi hadiah untuk keberanian seorang pemuda baik. Ia mempertanyakan kebiasaannya, menolak kecenderungannya meminta persetujuan semua orang, dan tertawa ketika ia akhirnya mampu membantah dengan alasan yang jujur. Ketertarikan mereka yang tumbuh sejak pertemuan lama kini punya ruang untuk menjadi sesuatu yang dipilih.

Koita tetap salah memegang cangkir saat bertamu ke kediaman Saionji, dan Shiori tetap harus meladeni tatapan dingin kerabatnya di ruang depan. Namun sebelum pamannya sempat membuka pembicaraan soal perjodohan, Shiori lebih dulu menarik kursi di sebelahnya dan memperkenalkan Koita sebagai kekasihnya."""

    # ┌─ ENDING · E-KO-06 · Dipilih: Chiasa  [Koita · host Y/C]
    # │ KAPAN   : Koita Success (NPC atau host)
    # │ ISI SKRG: tabu saudara tiri; lihat file 06
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-06"] = """Rumah Amamiya kehilangan kemudahan lamanya ketika Koita dan Chiasa mengakui bahwa perasaan mereka tidak lagi bisa disembunyikan di balik panggilan keluarga. Tak ada pengumuman manis yang membuat semua orang langsung memahami. Ada pintu yang ditutup, percakapan yang ditunda, dan orang tua yang perlu waktu untuk menerima bahwa mereka sedang diminta mendengar sesuatu yang sulit.

Koita berhenti membiarkan Chiasa mengucapkan seluruh keinginan sementara ia berlindung dalam diam. Ia menyebut pilihannya sebagai pilihannya sendiri. Chiasa, untuk pertama kalinya, tidak menyambut itu dengan janji bahwa ia akan selalu menyediakan segala sesuatu di rumah.

Di meja makan, Yoshie masih sering terdiam setiap kali melihat mereka duduk berdampingan. Koita yang kini mencuci piring setelah makan malam dan menjawab pertanyaan ayahnya tanpa menoleh ke arah Chiasa untuk meminta bantuan, sementara Chiasa kembali ke kamarnya sendiri untuk menyelesaikan gambar sebelum pukul sepuluh."""

    # ┌─ ENDING · E-KO-07 · Sendiri  [Netral · host Y/C]
    # │ KAPAN   : semua heroine menjauh; Koita tidak runtuh
    # │ ISI SKRG: kehilangan semuanya, mulai bertumbuh
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-07"] = """Pada malam pertama tanpa pesan dari siapa pun, Koita membuat dua cangkir teh. Ia menatap cangkir kedua cukup lama, kemudian menuangnya kembali sebelum dingin. Esoknya ia hanya membuat satu.

Tak ada yang kembali karena melihat ia mulai membaik. Ia mengembalikan buku, meminta maaf kepada orang yang bersedia mendengar, dan menerima bahwa beberapa permintaan maaf tidak dibalas. Hari-hari itu tidak menyenangkan, tetapi tidak semuanya kosong. Ada kuliah yang masih bisa diselesaikan, janji konseling yang bisa ditepati, dan tulisan yang tak harus membuat pembacanya mencintai dirinya.

Ketika seorang teman sekelas bertanya apakah ia pulang sendirian sore itu, Koita mengangguk tanpa tertawa canggung atau mengarang janji lain. Ia merapikan buku catatannya ke dalam tas, mengunci pintu ruang klub, dan berjalan menyusuri trotoar stasiun seorang diri."""

    # ┌─ ENDING · E-KO-08 · Tetap Menggantung  [Buruk · host Y/C]
    # │ KAPAN   : pola tidak pernah terbongkar
    # │ ISI SKRG: pola lama berlanjut dengan korban baru
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-08"] = """Beberapa orang berhenti menunggu, tetapi tidak pernah cukup banyak yang berbicara satu sama lain untuk melihat pola secara utuh. Koita menyebut semuanya perubahan wajar setelah kuliah. Ia terdengar sedih dengan cara yang membuat orang baru ingin menghiburnya.

Di tempat kerja pertamanya ada seseorang yang menyukai buku, seseorang yang sering lupa makan, seseorang yang merasa akhirnya diperhatikan. Koita mengingat detail kecil tentang mereka. Ia masih bisa sangat baik. Justru itu yang membuat pesan-pesannya terasa sulit dipertanyakan.

Saat ditanya apakah ia sedang dekat dengan seseorang, ia mengusap tengkuk dan berkata belum mengerti perasaannya sendiri. Gadis di seberang meja tersenyum sambil menunduk mengaduk kopinya, sementara ponsel Koita di saku jaket kembali bergetar menampilkan dua nama lain."""

    # ┌─ ENDING · E-KO-09 · Hancur  [Buruk · host Y/C]
    # │ KAPAN   : pola_koita_publik tinggi; atau E-SH-09
    # │ ISI SKRG: lingkungan menjauh setelah sifat aslinya terbukti
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-09"] = """Koita pertama-tama kehilangan hak untuk menjelaskan semuanya sebagai salah paham. Pesan yang serupa, janji yang dibiarkan bersinggungan, dan cerita yang berbeda kepada orang berbeda akhirnya dibaca bersama. Setiap alasan yang dahulu terdengar masuk akal kini memiliki pembanding.

Orang-orang tidak serentak membencinya. Ada yang marah, ada yang malu pernah membelanya, ada yang cukup lelah untuk pergi tanpa berdebat. Koita mendapati bahwa kehilangan akses kepada seseorang bisa lebih sunyi daripada pertengkaran.

Di ruang klub, kursi di sebelahnya tetap kosong sampai rapat bubar. Ia pulang saat hujan mulai turun, mendekap map naskah yang tak seorang pun minta dibacakan, dan melewati gerbang kampus tanpa satu pun payung yang berhenti menunggunya."""

    # ┌─ ENDING · E-KO-10 · Koita Membalas  [Buruk · host Y/C]
    # │ KAPAN   : manuver balik berhasil; pemain kalah perang reputasi
    # │ ISI SKRG: Koita merebut balik heroine dan menjatuhkan pemain di mata semua orang
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-10"] = """Koita berhenti datang kepadamu untuk meminta penjelasan. Ia mulai berbicara langsung kepada orang-orang yang selama ini kautafsirkan untuknya. Ketika kisah mereka dipertemukan, ada perbuatanmu yang tak lagi bisa ditutupi oleh citra penolong.

Kedekatan yang kaurebut berbalik meninggalkanmu. Beberapa orang memilih kembali berada di sisinya; yang lain sekadar menolak meneruskan hubungan denganmu. Dalam percakapan kampus, namamu menjadi jeda canggung sebelum seseorang mengganti topik.

Koita kembali duduk di kursi tengah kantin, dikelilingi tawa yang dulu kaubayangkan sudah berpindah ke sisimu. Saat matanya bersirobok denganmu yang melintas membawa nampan sendirian, ia tidak membuang muka; ia hanya mengangkat cangkirnya sedikit, memastikan kau melihat siapa yang sedang mendengarkannya berbicara."""

    # ┌─ ENDING · E-KO-11 · Penulis yang Jujur  [Netral · host Y/C]
    # │ KAPAN   : K19 dibantu jujur; K20 diisi kebenaran sebagian
    # │ ISI SKRG: berhenti menggantung; menulis novel tentang tokoh yang tidak pernah memilih
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-11"] = """Novel Koita dibuka dengan seorang tokoh yang mengaku tak pernah memilih siapa pun. Pada draf lama, kalimat itu terdengar sedih. Pada naskah yang akhirnya ia kirim, pembaca diberi cukup ruang untuk melihat siapa yang membayar harga dari pengakuan tersebut.

Koita mengerjakannya setelah skripsi, setelah percakapan yang tidak seluruhnya menyenangkan, setelah ia mulai membedakan memahami diri dari membenarkan diri. Ia menghapus bagian yang terlalu jelas meminjam luka orang lain hanya untuk membuat tokohnya tampak dalam.

Tidak semua orang membaca bukunya, dan beberapa ulasan di internet menilainya terlalu dingin. Koita mencetak potongan ulasan itu, menyelipkannya di antara tumpukan kertas revisi di meja kamar, lalu membuka dokumen kosong baru dan mulai mengetik bab pertama berikutnya."""

    # ┌─ ENDING · E-KO-12 · Pergi  [Netral · host Y/C]
    # │ KAPAN   : K23-A didukung pergi
    # │ ISI SKRG: menerima tawaran penerbit di kota lain dan meninggalkan semuanya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-12"] = """Tawaran penerbit itu berubah menjadi tiket, kontrak magang, dan alamat kamar sewaan yang belum pernah Koita lihat langsung. Sampai malam sebelum berangkat, ia masih punya kesempatan mengatakan terlalu banyak yang harus ditinggalkan. Ia menutup kopernya juga.

Di kota baru tidak ada orang yang tahu makanan kesukaannya atau kisah boneka masa kecil. Ia harus memperkenalkan diri tanpa bantuan kenangan bersama. Pekerjaannya lebih banyak merapikan naskah orang lain daripada menulis miliknya sendiri.

Sesekali ia masih mengirim foto langit sore dari balkon sempitnya ke grup lama, tanpa embel-embel kalimat yang memancing orang berkata rindu. Ketika pukul sembilan malam tiba dan tak ada balasan selain satu tanda jempol, ia meletakkan ponsel di meja, mematikan lampu kamar, dan menyiapkan kemeja untuk jam kerja esok pagi."""

    # ┌─ ENDING · E-KO-13 · MC yang Terbangun  [Khusus · host Y/C]
    # │ KAPAN   : koita_tahu_naskah percaya
    # │ ISI SKRG: Koita sengaja melawan plot armor-nya; pilihannya kini benar-benar miliknya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-13"] = """Koita menguji keyakinan paling mengerikan yang pernah ia terima: bahwa sebagian hidupnya mungkin disusun agar orang terus jatuh cinta. Ia tidak bisa membuktikan setiap kebetulan. Ia bisa berhenti memakainya sebagai alasan bahwa suatu pertemuan pasti dimaksudkan untuk dirinya.

Ketika hujan menahan seseorang di sebelahnya, ia menanyakan apakah orang itu ingin ditinggal sendiri. Ketika kesempatan pengakuan terasa terlalu sempurna, ia memberi ruang untuk jawaban yang tidak sempurna. Beberapa orang pergi, dan dunia tidak runtuh untuk mengantar mereka kembali.

Pada sore hari kelulusan, ketika kerumunan mulai terpecah di dekat gerbang utama, Koita sengaja mengambil gang kecil menuju stasiun yang berlawanan arah dengan rombongan klubnya. Sepatunya menginjak genangan sisa hujan, angin sore mengibaskan ujung jasnya, dan sampai kereta tiba di peron, tak seorang pun berlari menyusulnya."""

    # ┌─ ENDING · E-KO-14 · Persahabatan yang Diakhiri  [Netral · host Y/C]
    # │ KAPAN   : Koita tahu semua manipulasi pemain; tidak runtuh
    # │ ISI SKRG: ia memutus pemain dengan tenang dan tidak pernah kembali
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-14"] = """Koita mengembalikan barang-barangmu dalam satu tas. Tidak ada surat panjang, tidak ada daftar kebaikan yang diminta dibayar. Ia sudah mengetahui cukup banyak untuk berhenti menanyakan apakah kau sebenarnya bermaksud baik.

Ia mengatakan hubungan kalian selesai. Jika ada urusan yang belum beres, ia akan menyelesaikannya melalui orang lain. Setelah itu ia pergi sebelum percakapan berubah menjadi permintaan agar ia mendengarkan satu alasan lagi.

Kau masih berpapasan dengannya beberapa kali di tangga perpustakaan atau di depan minimarket dekat stasiun. Setiap kali langkah kalian berselisih, ia tidak mempercepat jalan maupun menoleh; ia hanya melewati bahumu seperti melewati tiang lampu di tepi trotoar."""

    # ┌─ ENDING · E-KO-15 · Toga yang Tidak Dipakai  [Buruk · host Y/C]
    # │ KAPAN   : K19 disabotase atau Koita runtuh di Tahun 3
    # │ ISI SKRG: Koita gagal lulus tepat waktu; evaluasi tetap di tanggal wisuda angkatannya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-15"] = """Toga Koita tetap terbungkus ketika foto wisuda angkatannya mulai memenuhi grup. Skripsinya tidak selesai pada waktunya. Di antara draf yang rusak, janji bimbingan yang terlewat, dan hari-hari ketika membuka laptop terasa mustahil, tenggat itu akhirnya lewat juga.

Sistem tetap melakukan evaluasi pada hari yang sudah ditentukan. Kalendernya tidak menunggu seseorang yang kehilangan kemampuan mengikuti kalender sendiri. Kau menerima hasil sementara Koita menatap pesan administrasi tentang semester tambahan.

Sore itu ia duduk di bangku kayu dekat gedung fakultas sementara rombongan wisudawan berfoto di bawah pohon sakura. Ketika seorang adik kelas menghampiri dan bertanya kapan ia akan menyusul sidang, Koita hanya menjawab belum tahu, lalu menunduk mengikat tali sepatunya yang sebenarnya tidak lepas."""

    # ┌─ ENDING · E-KO-16 · Semua Pergi  [Khusus · host Y/C]
    # │ KAPAN   : orbit_koita 0; sebagian besar heroine pergi sendiri (pola terbongkar atau memilih mandiri); runtuh_koita ≥ 80; tanpa penopang
    # │ ISI SKRG: NTR sempurna: tidak ada satu pun yang tersisa. Koita berhenti menulis dan kuliah, mengurung diri, kena mental; ditulis lewat kondisi dan dampaknya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-16"] = """Nama-nama itu tidak hilang dari ponsel Koita. Mereka hanya berhenti menjadi orang yang bisa ia hubungi tanpa memikirkan alasan. Satu per satu memilih kehidupan yang tak lagi berpusat padanya, sampai tidak ada lagi kursi yang sengaja disisakan.

Ia berhenti datang ke kelas. Naskahnya tertutup berhari-hari, lalu berminggu-minggu. Orang mengira ia sedang menghindari malu; di dalam kamar, hal sesederhana mandi dan menjawab satu pesan sudah memerlukan tenaga yang sulit ia kumpulkan.

Sampai hari evaluasi tiba, tirai kamarnya tetap tertutup rapat dari pagi hingga petang. Di atas meja belajarnya, layar laptop yang berdebu memantulkan bayangan mangkuk mi instan kering dari tiga hari lalu, sementara telepon rumah di lantai bawah berdering panjang tanpa seorang pun naik untuk memanggil namanya."""

    # ┌─ ENDING · E-KO-17 · Pusat yang Berpindah  [Khusus · host Y/C]
    # │ KAPAN   : orbit_koita 0; minimal tiga heroine kini di orbit pemain, karena memilih pemain atau terikat lewat ancaman atau Force ; Koita tahu; runtuh_koita ≥ 80
    # │ ISI SKRG: NTR sempurna: lingkaran yang dulu berputar di sekitar Koita kini berputar di sekitar pemain, dan Koita menjadi figuran di ceritanya sendiri. Slide tiap heroine berbeda: yang memilih pemain tampak bahagia, yang dipaksa tampak hancur
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-17"] = """Koita melihat kelompok itu dari luar. Nama yang dulu paling sering disebut dalam rencana mereka kini namamu. Ia datang terlalu akhir untuk percakapan, tak tahu lelucon baru, dan berhenti ditanya apakah bisa ikut sebelum sebuah jadwal ditetapkan.

Namun wajah-wajah di dekatmu tidak bisa dibaca sebagai satu kemenangan. Orang yang memilihmu bebas bisa tertawa dan pergi tanpa takut. Pada orang yang bertahan karena ancaman, yang terlihat adalah kewaspadaan. Luka akibat paksaan tidak berubah menjadi cinta hanya karena jaraknya dekat dengan tubuhmu.

Saat jendela Sistem menutup hitungan keberhasilannya di sudut matamu, Koita berdiri beberapa langkah di belakang kerumunan dekat gerbang tanpa seorang pun menyisakan ruang untuknya. Di sebelahmu, seorang gadis tertawa menyambut ajakan makan malammu, sementara gadis di sisi lainnya diam-diam mencengkeram tali tasnya setiap kali lenganmu bergerak terlalu dekat."""

    # ┌─ ENDING · E-KO-18 · Naskah yang Kosong  [Khusus · host Y/C]
    # │ KAPAN   : syarat E-KO-16 atau E-KO-17; Koita tahu soal naskah dan percaya; plot armor padam (K-D14)
    # │ ISI SKRG: Koita sadar ia MC yang ditinggalkan naskahnya sendiri; kebetulan tidak pernah datang lagi. Sistem membacakan: "MC selesai."
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-18"] = """Koita kembali ke tempat kebetulan dulu selalu datang. Ia menunggu melewati jam yang masuk akal, melewati penutupan toko, sampai petugas meminta jalan masuk dikosongkan. Tidak ada siapa pun yang tiba terlambat untuk menjadi penutup yang manis.

Ia sudah percaya pada keberadaan naskah. Kini ia mempercayai sesuatu yang lebih menghancurkan: bahwa naskah itu berhenti menginginkannya. Buku catatannya tetap kosong karena setiap awal kalimat terdengar seperti meniru suara yang sudah pergi.

MC selesai, kata Sistem.

Keesokan paginya sinar matahari tetap menembus celah tirai kamarnya yang kusut. Koita bangun karena bunyi truk sampah di jalan depan, menatap pulpen yang tergeletak di sebelah buku catatan kosong, lalu turun ke dapur untuk merebus air sendirian."""

    # ┌─ ENDING · E-KO-19 · Yang Tidak Bisa Ia Hentikan  [Hancur · host Y/C]
    # │ KAPAN   : Koita menyaksikan Force; trust_koita masih tinggi saat itu (ia masih percaya dan dekat dengan pemain), sehingga ia membeku alih-alih bertindak; korban tidak kembali padanya
    # │ ISI SKRG: trauma karena gagal melindungi orang yang masih ia percaya; ia tidak sanggup mendekati siapa pun lagi. Bisa menempel sebagai lapisan di E-KO-16 atau E-KO-17
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-19"] = """Ingatan Koita pecah di bagian ketika ia seharusnya mengenali bahaya pada orang yang masih dipercayainya. Ia mengulang saat itu dalam pikirannya, mencari satu gerakan atau satu kalimat yang bisa mengubah apa yang sudah terjadi. Tubuhnya mengingat kebekuan sebelum pikirannya selesai menyusun rasa bersalah.

Orang yang dilukai tidak kembali kepadanya. Koita tidak berhak menuntut itu sebagai bukti bahwa ia telah diampuni. Namun tanpa seseorang yang membantu membedakan tanggung jawab pelaku dari kegagalannya bertindak, ia mulai menganggap kedekatannya sendiri selalu membawa bahaya.

Ia berhenti datang ke kantin, menolak ajakan belajar kelompok, dan selalu tersentak setiap kali pintu ruangan ditutup terlalu keras dari belakang. Bahkan saat duduk di kereta yang lengang, tangannya terus meremas ujung lengan kemejanya sendiri sampai buku-buku jarinya memutih."""

    # ┌─ ENDING · E-KO-20 · Saksi yang Bersuara  [Netral · host Y/C]
    # │ KAPAN   : Koita menyaksikan atau mengetahui Force saat trust_koita sudah rendah (sudah lama curiga atau lepas dari pemain), sehingga ia bisa bertindak alih-alih membeku
    # │ ISI SKRG: dari orang yang sudah tidak percaya menjadi orang yang menjatuhkan pemain; sendiri, tetapi berdiri. Berjalan bersama E-FO-11
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-20"] = """Koita tidak mencoba membuat kesaksiannya terdengar lebih lengkap daripada yang ia ketahui. Ia membedakan apa yang dilihat, apa yang didengar, dan apa yang baru dipahami sesudahnya. Ketika ditanya tentang kedekatannya denganmu, ia tidak menyembunyikan bahwa pernah mempercayaimu.

Ia hadir kembali saat diperlukan. Ia menerima bahwa korban boleh memilih didampingi orang lain, boleh tidak ingin bertemu dengannya, dan tidak berkewajiban membenarkan rasa bersalahnya. Kesaksian itu membantu meruntuhkan kebebasan yang selama ini kaunikmati di balik kepercayaan orang.

Koita tetap pulang sendirian pada banyak sore setelah pemeriksaan berakhir. Ketika salah seorang teman korban menemuinya di selasar gedung administrasi untuk mengucapkan terima kasih, ia hanya menggeleng pelan, menyerahkan salinan berkas jadwal sidang dari tasnya, lalu berpamitan sebelum hujan turun."""

    # ┌─ ENDING · E-KO-21 · Dituduh atas Luka yang Menimpanya  [Hancur · host C]
    # │ KAPAN   : jalur manipulasi pembalikan Chiasa (06_Chiasa.md §14) bertahan; runtuh_koita ≥ 80
    # │ ISI SKRG: Koita korban yang justru dicap pelaku; tidak dipercaya dan tidak bisa membuktikan sebaliknya; runtuh dalam diam. K-D21 (ada yang tetap percaya) atau C-D14/C-D15 (Chiasa sendiri goyah) bisa membelokkan ini sebelum M35
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-21"] = """Koita berusaha menjelaskan bahwa luka itu menimpanya. Setiap kata tiba di hadapan orang yang sudah membawa kesimpulan lain. Kemarahannya dianggap ancaman, tangisnya dianggap akting, dan kebingungannya dipakai untuk meragukan ingatan yang sedang susah payah ia pertahankan.

Tidak ada saksi yang berhasil menembus versi yang telanjur dipercaya sebelum evaluasi berakhir. Orang-orang menjauh dengan keyakinan sedang melindungi seseorang. Koita kehilangan ruang aman sekaligus hak untuk dikenali sebagai orang yang telah dilukai.

Ia mulai membalik cermin kecil di mejanya, mencabut kabel telepon kamar, dan menahan napas setiap kali ada langkah kaki berhenti di depan pintu. Saat malam turun, ia duduk di sudut lantai dengan lutut ditekuk ke dada, menatap celah cahaya dari lorong rumah yang tak lagi berani ia buka."""

    # ┌─ ENDING · E-BL-01 · Berkomitmen  [Romantis · host Y]
    # │ KAPAN   : B6 memilih; dibuka terbuka
    # │ ISI SKRG: Koita berhenti menggantung dan memilih Yutaka
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-BL-01"] = """Koita memperkenalkan Yutaka sebagai pasangannya sebelum ada yang sempat menyebut mereka sahabat seperti biasa. Suaranya goyah pada kata pertama, lalu menjadi lebih jelas ketika ia mengulang untuk orang yang belum mendengar.

Tidak semua percakapan sesudahnya mudah. Ada perasaan orang lain yang harus dijawab, ada gurauan yang perlu dihentikan, ada kebiasaan Koita menyenangkan semua orang yang muncul saat ia takut. Yutaka tidak mengambil alih seluruh percakapan itu. Ia berdiri di sebelahnya, memberi waktu, lalu meminta jawaban yang sungguhan.

Malam itu mereka pulang bersama dan berdebat di depan minimarket tentang siapa yang kemarin lupa membeli beras. Koita tertawa sambil mengambil kantong lima kilogram dari rak bawah, sementara Yutaka mengeluarkan dompet di kasir dan menyelipkan struk belanja ke saku jaket Koita."""

    # ┌─ ENDING · E-BL-02 · Ditolak dan Retak  [Netral · host Y]
    # │ KAPAN   : B6 menolak
    # │ ISI SKRG: persahabatan sejak kecil retak
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-BL-02"] = """Penolakan itu jelas. Tak ada mungkin nanti yang bisa dibawa pulang untuk dipelihara sebagai harapan. Setelahnya mereka masih tahu terlalu banyak hal kecil tentang satu sama lain, tetapi tak lagi tahu cara memulai percakapan tanpa menyentuh bagian yang sakit.

Yutaka berhenti datang tanpa kabar. Koita beberapa kali mengetik cerita yang dahulu pasti dikirim kepadanya, lalu menghapusnya. Persahabatan sejak kecil ternyata tidak kebal terhadap satu keinginan yang tidak bisa dibalas.

Mereka tidak membuat janji untuk segera kembali akrab seperti dulu. Ketika akhirnya berpapasan di dekat tangga gedung kuliah, Yutaka hanya mengangguk singkat sambil memindahkan map ke tangan kiri, dan Koita membalas sapaan itu setengah detik setelah punggung sahabatnya sudah melewatinya."""

    # ┌─ ENDING · E-BL-03 · Kembali ke Pola Lama  [Netral · host Y]
    # │ KAPAN   : B6 lari; Yutaka mundur
    # │ ISI SKRG: Koita kembali menggantung semua orang, termasuk Yutaka
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-BL-03"] = """Koita mengatakan belum siap. Yutaka mendengar keraguan yang dikenalnya sejak lama dan memilih mundur sebelum seluruh hidupnya menjadi ruang tunggu. Untuk beberapa minggu pesan mereka jarang.

Lalu Koita kembali dengan cerita kecil, foto makanan, pertanyaan apakah ia sudah tidur. Tidak ada pembicaraan tentang apa yang pernah diminta Yutaka. Kedekatan itu terasa begitu akrab sehingga mudah diterima, sampai ia menyadari nama lain juga mendapat undangan untuk datang saat Koita kesepian.

Lewat tengah malam, ponsel Yutaka kembali menyala menampilkan pesan pendek dari Koita yang mengeluh tidak bisa tidur. Yutaka menatap layar itu lama di kamar yang gelap, menarik napas panjang, lalu tetap menyambar jaket dari sandaran kursi untuk keluar membelikan minuman hangat."""

    # ┌─ ENDING · E-BL-04 · Kolaps  [Buruk · host Y]
    # │ KAPAN   : semua orang, termasuk Yutaka, mundur darinya
    # │ ISI SKRG: Koita kolaps setelah sendirian
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-BL-04"] = """Yutaka adalah nomor terakhir yang masih dicoba Koita setelah semua percakapan lain berakhir. Ketika hubungan itu pun mundur, ia kehilangan orang yang selama ini dianggap akan selalu berada di luar pertanyaan memilih.

Ia berhenti menjaga waktu. Pagi dan malam ditentukan oleh kapan ia sanggup membuka mata, bukan jadwal kuliah. Pesan yang menanyakan kabarnya dibiarkan karena menjawab satu berarti mengakui bahwa keadaan memang sudah separah itu.

Pada pagi hari evaluasi, pintu kamarnya masih terkunci dari dalam sementara tumpukan surat kampus menumpuk di bawah celah kayu. Ponselnya tergeletak mati di dekat bantal dengan layar terakhir masih terbuka pada riwayat panggilan ke nomor Yutaka yang tidak pernah ia tekan."""

    # ┌─ ENDING · E-BL-05 · Rahasia di Apartemen  [Romantis · host Y]
    # │ KAPAN   : B6 memilih; disembunyikan
    # │ ISI SKRG: hubungan berlanjut diam-diam; Chiasa tahu
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-BL-05"] = """Di apartemen Yutaka, Koita punya cangkir dan sikat gigi sendiri. Di luar, mereka masih sering diperkenalkan sebagai teman lama. Kesepakatan merahasiakan hubungan itu terasa aman pada awalnya; kemudian muncul malam ketika salah satu dari mereka lelah harus menimbang setiap gerakan.

Chiasa mengetahui lebih dahulu daripada orang lain. Ia tidak menjadikan pengetahuan itu tiket untuk masuk ke setiap urusan mereka, tetapi tatapannya membuat Koita sadar bahwa diam pun dapat melukai orang yang belum diberi jawaban.

Mereka tetap tinggal bersama di balik pintu itu. Pada kalender kertas yang tergantung di sebelah kulkas, Yutaka melingkari tanggal akhir bulan dengan spidol merah, dan malam itu Koita duduk di meja dapur sambil menyiapkan daftar nama keluarga yang akan mereka temui satu per satu."""

    # ┌─ ENDING · E-BL-06 · Restu di Meja Makan  [Romantis · host Y]
    # │ KAPAN   : B6 memilih; Daisuke dan Yoshie menerima
    # │ ISI SKRG: makan malam keluarga dengan satu kursi tambahan yang kini resmi
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-BL-06"] = """Yoshie menambah satu mangkuk sebelum Yutaka datang. Daisuke menanyakan pekerjaannya dengan kecanggungan seorang ayah yang ingin menunjukkan penerimaan tetapi tidak tahu pertanyaan mana yang terlalu resmi. Koita berkali-kali mencoba membantu, sampai Yutaka menyenggol lututnya di bawah meja.

Mereka makan dengan percakapan yang tidak seluruhnya lancar. Ada kebiasaan lama menyebut sahabat yang diperbaiki di tengah kalimat. Ada pertanyaan tentang rencana tinggal yang membuat telinga Koita memerah. Penerimaan keluarga tidak tampil sempurna; ia tampil sebagai kemauan untuk belajar dan mengajak makan lagi.

Sesudah hidangan selesai, Yutaka ikut membereskan. Mangkuknya diletakkan bersama mangkuk keluarga, bukan disimpan di rak tamu. Koita melihat hal kecil itu, lalu berani menyentuh tangannya tanpa memeriksa siapa yang sedang menonton."""

    # ┌─ ENDING · E-BL-07 · Kursi Kosong di Rumah Amamiya  [Buruk · host Y]
    # │ KAPAN   : B6 memilih; keluarga menolak
    # │ ISI SKRG: Koita meninggalkan rumah dan tinggal di apartemen Yutaka
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-BL-07"] = """Koita meninggalkan rumah dengan koper yang terlalu kecil untuk seluruh akibat keputusan malam itu. Keluarganya belum menerima hubungannya dengan Yutaka. Di meja makan, satu kursi kembali kosong, kali ini karena ia sendiri memilih tidak duduk di tempat yang mensyaratkan penyangkalan terhadap hidupnya.

Apartemen Yutaka tidak mendadak menjadi rumah yang mudah. Mereka menghitung pengeluaran, membagi ruang, dan belajar bahwa menolong pasangan tidak berarti menjadi satu-satunya penopang yang boleh ia punya. Koita kadang menangis setelah panggilan keluarga yang pendek.

Setiap Minggu sore Koita masih berhenti sebentar di depan rak minimarket yang menjual teh kesukaan ibunya, sebelum beralih mengambil bahan makan malam untuk dua orang. Di apartemen, di sela kardus buku yang belum sempat dibongkar, Yutaka sudah menyiapkan meja lipat kecil dan dua pasang sumpit."""

    # ┌─ ENDING · E-BL-08 · Ia Lari dari Pintu Itu  [Netral · host Y]
    # │ KAPAN   : B4 dominan tanpa kehangatan
    # │ ISI SKRG: Koita kabur dari Yutaka dan dari semuanya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-BL-08"] = """Koita semula mengira ketegasan Yutaka akan membuat segalanya lebih mudah. Ia tidak perlu menebak siapa yang diinginkan atau kapan harus mendekat. Namun sedikit demi sedikit, kepastian berubah menjadi perasaan bahwa tak ada jawaban yang aman selain menurut.

Ketika ia akhirnya berkata berhenti, suaranya hampir tidak keluar. Ia mengambil tas dan pergi sebelum percakapan bisa berubah menjadi bujukan lain. Setelah itu ia menghindari tempat-tempat yang mempertemukan mereka, bahkan ketika jarak tersebut membuatnya kehilangan teman yang tak tahu apa-apa.

Ketika Yutaka datang mengetuk pintu rumah Amamiya sore berikutnya, hanya Yoshie yang keluar membawakan buku catatan yang pernah dipinjam anaknya. Di kamar lantai dua, Koita berdiri beberapa langkah di belakang jendela yang tertutup rapat, menunggu sampai bayangan di jalan depan benar-benar berbalik pergi."""


    # ═════ Miyuki ═════
    # ┌─ ENDING · E-MI-01 · Jas Putih yang Ringan  [Romantis · host Y/C]
    # │ KAPAN   : tahap ≤ 3 atau pulih; Affection dan Trust tinggi ke pemain; tanpa Force; Yuina tidak memusuhi
    # │ ISI SKRG: hubungan setara; ia belajar meminta tolong dan tetap menuju pediatri
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-01"] = """Miyuki pulang dengan jas putih tersampir di lengan dan permintaan yang dahulu hampir mustahil diucapkannya: hari ini ia ingin ditemani tanpa harus menyiapkan apa pun. Kau menggeser buku dari sofa, memberinya tempat, dan menunggu ia memilih antara bercerita atau diam.

Hubungan kalian tidak menggantikan cita-citanya menjadi dokter anak. Ada jadwal yang harus dihormati, kencan yang dipindahkan, malam ketika kalian sama-sama lelah. Yuina tetap bisa mengajaknya makan tanpa membuatmu merasa tersaingi. Miyuki pun belajar bahwa menerima bantuan tidak mengurangi kemampuannya merawat orang lain.

Pada suatu pagi ia lupa menyeduh teh untukmu karena terlalu asyik menceritakan pasien kecil yang akhirnya berani menyapanya. Ia baru sadar di tengah cerita ketika melihat cangkir kosong di meja, lalu tertawa sementara kau sendiri yang bangun menyalakan ketel untuk kalian berdua."""

    # ┌─ ENDING · E-MI-02 · Dokter Anak  [Netral · host Y/C]
    # │ KAPAN   : tahap ≤ 2; karier lancar; hati tidak ke siapa pun
    # │ ISI SKRG: lulus, fokus pediatri, hangat pada semua tetapi sendiri
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-02"] = """Jalan menuju pediatri belum selesai saat Miyuki meninggalkan masa kuliahnya. Masih ada pendidikan, penilaian, dan hari-hari ketika pengetahuan terasa terlalu kecil di hadapan ketakutan sebuah keluarga. Ia tetap melangkah ke sana, kali ini dengan kebiasaan meminta bantuan sebelum kelelahan mengambil seluruh suaranya.

Tidak ada pasangan yang menunggunya sebagai hadiah atas pertumbuhan itu. Ia punya Yuina, rekan yang bisa dipercaya, dan apartemen yang mulai diisinya dengan barang-barang untuk dirinya sendiri. Kesendirian kadang terasa sepi; ia tidak lagi menyamakan rasa sepi dengan bukti bahwa dirinya kurang berguna.

Dalam foto yang dikirim pada musim semi, Miyuki berdiri di depan bangsal anak. Senyumnya hangat dan sedikit gugup. Di bawahnya ia menulis bahwa ia ingin menjadi dokter yang baik, lalu menambahkan bahwa malam itu ia sudah berjanji akan tidur cukup."""

    # ┌─ ENDING · E-MI-03 · Kembali ke Koita  [Koita · host Y/C]
    # │ KAPAN   : Koita memilih Miyuki di K26; tahap ≤ 3
    # │ ISI SKRG: jalur manga; deviasi rendah untuk Miyuki
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-03"] = """Miyuki hampir menanggapi pengakuan Koita dengan godaan. Kebiasaan menjadi senpai yang tenang datang lebih cepat daripada keberaniannya mengakui betapa lama ia menunggu. Ia berhenti sebelum tertawa, lalu mengatakan bahwa ia juga mencintainya.

Mereka harus membicarakan penundaan yang sudah terjadi. Koita tidak lagi boleh mengira senyum Miyuki berarti ia tidak terluka; Miyuki tidak lagi bisa memakai kedewasaan sebagai alasan untuk selalu menerima sisa waktu. Percakapan pertama mereka sebagai pasangan justru penuh hal yang sulit didengar.

Sesudahnya ia memasak untuk dua orang karena ingin, bukan karena takut tempatnya akan diambil jika ia berhenti. Ketika Koita datang membantu mencuci piring, Miyuki menyandarkan kepala sebentar di bahunya. Ia tidak meminta maaf karena sedang ingin dimanja."""

    # ┌─ ENDING · E-MI-04 · Cincin Keluarga Hayase  [Netral · host Y/C]
    # │ KAPAN   : Mi25-A atau pemain absen; omiai ditekan
    # │ ISI SKRG: bertunangan demi keluarga; senyum yang rapi; ikatan sosial, bukan pasangan romantis baru
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-04"] = """Cincin keluarga Hayase tampak tepat di tangan Miyuki. Foto pertunangannya mendapat pujian tentang keserasian dua keluarga, masa depan yang terjamin, dan betapa beruntungnya ia. Tidak banyak yang menanyakan apakah senyum di foto itu menyerupai senyumnya saat tak ada kamera.

Tatsuru berbicara sopan tentang rencana yang sudah dibahas para orang tua. Miyuki belajar menyampaikan keberatan sebagai penyesuaian kecil agar tetap boleh didengar. Ia belum menemukan cara menolak seluruh rencana tanpa merasa telah mengecewakan semua orang sekaligus.

Ia tetap menempuh jalan kedokteran, membawa pertunangan sebagai bagian lain dari kewajiban keluarga. Di apartemennya, kotak cincin itu sering dibiarkan tertutup di samping tumpukan buku anatomi sampai telepon ibunya berdering mengingatkan makan malam akhir pekan."""

    # ┌─ ENDING · E-MI-05 · Kereta Pagi Tanpa Tujuan  [Romantis · host Y/C]
    # │ KAPAN   : Mi25-C kabur bersama pemain
    # │ ISI SKRG: orang tua memutus hubungan; karier tertunda; cinta yang mahal
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-05"] = """Kereta pertama berangkat ketika Miyuki masih menerima panggilan dari rumah. Ia mematikan suara, menatap namamu di layar pemesanan tiket, lalu menangis karena kelegaan dan ketakutan datang bersamaan. Kalian pergi dengan lebih banyak keberanian daripada rencana.

Keluarganya memutus dukungan dan hubungan. Pendidikan tertunda; uang yang dahulu tidak perlu dihitung kini dibagi antara tempat tinggal, makan, dan kemungkinan kembali kuliah. Pada malam-malam tertentu cinta kalian dipaksa berbicara dalam bentuk tagihan dan kesabaran yang menipis.

Di kamar sewaan kecil dekat rel kereta, Miyuki masih menyalakan lampu meja setiap habis giliran kerja paruh waktunya untuk membaca buku pediatri yang dibawanya dalam koper. Saat kau pulang membawa belanjaan malam, ia menggeser tumpukan catatan itu agar kalian bisa makan di meja yang sama."""

    # ┌─ ENDING · E-MI-06 · Lampu Bangsal Padam  [Buruk · host Y/C]
    # │ KAPAN   : kelelahan ekstrem; tanpa bantuan; CBT gagal
    # │ ISI SKRG: burnout; berhenti dari kedokteran
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-06"] = """Miyuki mengenali semua istilah untuk menjelaskan kelelahan, tetapi pengetahuan itu tidak membuat tangannya sanggup membuka buku. Setelah ujian yang gagal, ia mencoba mengejar dengan waktu tidur yang semakin sedikit. Ketika tubuhnya berhenti mengikuti kemauannya, tak ada lagi senyum yang cukup untuk menutupi keadaan.

Ia meninggalkan kedokteran. Untuk beberapa waktu jas putihnya tetap tergantung seolah pemiliknya hanya sedang libur. Telepon keluarga berubah menjadi pembicaraan tentang kesempatan yang disia-siakan, membuat ia makin jarang menjawab.

Suatu sore di depan stasiun, ia masih refleks menoleh ketika mendengar seorang anak kecil menangis di dekat bangku tunggu. Setelah ibu anak itu datang menggendongnya pergi, Miyuki merapatkan syalnya dan kembali berjalan pelan membawa kantong belanjaan ke apartemennya yang sunyi."""

    # ┌─ ENDING · E-MI-07 · Kenyamanan yang Salah  [Terdistorsi · host Y/C]
    # │ KAPAN   : tahap 5 permanen; arah_luka pemain
    # │ ISI SKRG: hubungan "nyaman" yang tidak sehat; ia hanya merasa dicintai saat diperlakukan keras
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-07"] = """Miyuki mulai gelisah pada hari ketika kau memperlakukannya dengan tenang. Ia mencari kesalahan kecil yang bisa menjelaskan mengapa perhatianmu terasa begitu jauh. Jika akhirnya kau meninggikan suara, tubuhnya justru mengendur, lega karena kembali tahu cara mendapatkan tempat di hadapanmu.

Ia menyebutnya cocok. Katanya hanya kalian yang memahami bentuk kasih sayang itu. Yuina mendengar kalimat tersebut dan tidak ikut tersenyum. Di mata sahabatnya, Miyuki makin sulit meminta sesuatu tanpa terlebih dahulu merendahkan diri.

Di meja dapur apartemennya, cangkir teh hangat selalu sudah terhidang sepuluh menit sebelum jadwal kedatanganmu. Miyuki berdiri menunggu di dekat pintu dengan jari-jari saling menggenggam, memperhatikan cara kau melepas sepatu untuk menebak apakah hari ini ia akan dimarahi atau dipeluk."""

    # ┌─ ENDING · E-MI-08 · Penebusan Tanpa Akhir  [Terdistorsi · host Y/C]
    # │ KAPAN   : tahap 5; arah_luka diri
    # │ ISI SKRG: lulus dan bekerja, tetapi menghukum diri lewat jam kerja tanpa batas
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-08"] = """Miyuki lulus. Ia mendapat pekerjaan dan dikenal sebagai orang yang selalu bersedia menggantikan jadwal. Ketika dipuji berdedikasi, ia tersenyum dengan sopan, menyembunyikan alasan yang tidak terdengar mulia: jika berhenti sebentar, ia takut seluruh kesalahan yang dituduhkan kepada dirinya akan kembali memenuhi ruangan.

Jam kerjanya menjadi bentuk hukuman yang diterima orang sebagai pengabdian. Ia jarang pulang sebelum benar-benar habis tenaga. Undangan makan ditolak dengan alasan sibuk, lalu ia merasa lega karena tidak perlu menjelaskan mengapa bersenang-senang terdengar seperti sesuatu yang belum pantas didapatkan.

Di ruang jaga pukul tiga pagi, ketika bangsal akhirnya tenang dan perawat lain sudah bergantian memejamkan mata, Miyuki masih berdiri di depan papan jadwal minggu depan untuk menulis namanya di tiga kolom lembur yang masih kosong."""

    # ┌─ ENDING · E-MI-09 · Menunggu yang Menyakitkan  [Terdistorsi · host Y/C]
    # │ KAPAN   : tahap 5; arah_luka Koita; Koita tetap menggantung
    # │ ISI SKRG: ia bertahan di sisi Koita justru karena sakitnya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-09"] = """Koita masih berkata nanti. Miyuki tidak lagi mendengar kata itu sebagai penundaan semata; rasa sakit setelahnya telah menjadi cara paling dikenalnya untuk memastikan perasaannya masih nyata. Ia datang saat diminta dan bertahan ketika seharusnya boleh pergi.

Kadang Koita memberinya malam yang hangat, lalu menghilang ke kesibukan orang lain. Miyuki menyalahkan dirinya karena menginginkan lebih. Ketika seorang teman mengatakan ia layak mendapat kepastian, ia membela Koita lebih keras daripada yang Koita pernah lakukan untuk hubungan mereka.

Di dapur apartemennya, ia tetap memasak dua porsi setiap Jumat malam meski belum ada pesan yang menjanjikan kedatangan. Ketika jarum jam melewati tengah malam, ia memindahkan porsi kedua ke wadah plastik dengan senyum tipis, lalu memasukkannya ke deretan kotak serupa di dalam kulkas."""

    # ┌─ ENDING · E-MI-10 · Cuti Satu Tahun  [Netral · host Y/C]
    # │ KAPAN   : pulih sebagian lewat Sato; CBT tertunda
    # │ ISI SKRG: cuti kuliah; masa depan terbuka; pesan pendek untuk pemain di musim semi
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-10"] = """Formulir cuti terasa lebih berat bagi Miyuki daripada formulir ujian mana pun. Ia membawanya ke sesi dengan Sato, mengaku takut satu tahun istirahat akan membuktikan bahwa sejak awal ia tidak cukup kuat untuk kedokteran.

Keputusan itu tetap diambil. Ujian ditunda, kalender dikosongkan sebagian, dan ia belajar bahwa sehari tanpa pencapaian tidak harus diakhiri dengan rasa bersalah. Pemulihannya tidak lurus. Ada pagi ketika ia bangun panik karena mengira terlambat praktik, lalu perlu waktu untuk memahami bahwa tak ada yang sedang ia kecewakan.

Pada awal musim semi, ponselmu menerima satu foto darinya: sepiring telur gulung yang agak miring dan secangkir teh di meja balkon, disertai pesan pendek bahwa pagi ini ia bangun tanpa alarm."""

    # ┌─ ENDING · E-MI-11 · Pintu yang Ditutup Yuina  [Buruk · host Y/C]
    # │ KAPAN   : pemain memanfaatkan di depan umum; Yuina memutus
    # │ ISI SKRG: Miyuki terisolasi; Yuina menjadi penghalang pemain di semua lingkungan medis
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-11"] = """Yuina melihat cukup banyak untuk berhenti menyebut perlakuanmu salah paham. Ia berdiri di antara kau dan Miyuki ketika penghinaan yang kauanggap biasa kembali terjadi di depan orang lain. Kali ini tidak ada tawa yang dibiarkan menyamarkannya.

Aksesmu ke lingkungan medis mulai tertutup. Yuina tidak bersedia mengantarkan pesan, mencarikan alasan, atau memberimu kesempatan mendekat lewat nama orang yang pernah kauperlakukan sebagai alat. Ia mengatakan apa yang diketahuinya ketika diperlukan.

Setiap kali kau mencoba menunggu di dekat lobi gedung fakultas kedokteran, Yuina sudah lebih dulu keluar bersama dua senior laboratorium dan mengapit Miyuki menuju pintu samping sampai bayangan mereka hilang di balik koridor."""

    # ┌─ ENDING · E-MI-12 · Napas yang Tertahan  [Hancur · host Y/C]
    # │ KAPAN   : pemain pelaku Force terhadapnya
    # │ ISI SKRG: trauma terpisah dari Rute Masokis; jalur Yuina, Sato, dan hukum; tanpa romansa dengan pelaku
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-12"] = """Setelah kekerasan itu, Miyuki sulit mengenali tubuh yang selama ini ia paksa untuk selalu dapat diandalkan. Ia bisa menyebut apa yang terjadi dengan istilah yang tepat dan tetap kehilangan suara ketika harus mengucapkannya sebagai sesuatu yang menimpa dirinya.

Yuina datang tanpa meminta cerita lengkap. Sato menyediakan ruang yang tidak menuntutnya segera pulih. Dukungan dan jalan hukum dibicarakan sesuai kesiapan serta kehendaknya; kedokteran yang semula menjadi seluruh identitasnya kini harus memberi ruang bagi pemulihan yang tidak mengikuti kalender ujian.

Pada pertemuan resmi terakhir melalui perantara kuasa hukumnya, pernyataan tertulis Miyuki hanya memuat satu kalimat penutup yang menolak segala bentuk kontak darimu, dan Yuina sendiri yang menutup pintu ruang mediasi tepat di hadapanmu."""

    # ┌─ ENDING · E-MI-13 · Sandiwara yang Jadi Nyata  [Romantis · host Y/C]
    # │ KAPAN   : pasangan palsu dipertahankan sampai Mi18, lalu diakui jujur
    # │ ISI SKRG: dua keluarga marah lalu menerima; awal yang bohong menjadi hubungan yang jujur
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-13"] = """Hubungan yang awalnya dipakai untuk menghindari tekanan keluarga akhirnya menuntut satu pengakuan yang tidak bisa dilatih. Miyuki mengatakan ia ingin bersamamu sungguhan, lalu meminta sandiwara sebelumnya diakhiri dengan kebenaran kepada semua pihak.

Dua keluarga marah karena telah dipermainkan. Percakapan panjang mengikuti, penuh pertanyaan yang dahulu kalian harapkan bisa dilewati dengan senyum. Penerimaan datang perlahan setelah kalian berhenti menyalahkan keadaan untuk setiap kebohongan yang dipilih sendiri.

Ketika makan malam berikutnya tiba, Miyuki masih gugup. Kau tidak lagi perlu menghafal tanggal rekaan atau kebiasaan yang dibuat agar tampak mesra. Di bawah meja ia menggenggam tanganmu, lalu membiarkannya terlihat. Kali ini kedekatan itu tidak bergantung pada siapa yang sedang menonton."""

    # ┌─ ENDING · E-MI-14 · Sandiwara Terbongkar  [Buruk · host Y/C]
    # │ KAPAN   : pasangan palsu terbongkar oleh Tatsuru atau orang tua
    # │ ISI SKRG: malu di depan keluarga; Miyuki menjauh dari pemain dan menerima omiai
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-14"] = """Kebenaran tentang pasangan palsu muncul di tengah pertemuan keluarga, pada saat semua orang sudah cukup jauh membicarakan masa depan untuk merasa dipermalukan oleh masa lalu. Miyuki mencoba menjelaskan tekanan yang membuatnya setuju. Penjelasan itu terdengar seperti alasan di telinga orang yang lebih marah karena kehilangan kendali.

Ia menjauh darimu setelahnya. Bukan hanya karena sandiwara terbongkar, melainkan karena setiap percakapan denganmu mengembalikannya pada ketakutan bahwa ia telah membuat hidupnya semakin sulit untuk ditentukan sendiri.

Bulan berikutnya Miyuki hadir di ruang makan hotel bersama keluarga Tatsuru dengan kimono merah muda yang dipilihkan ibunya. Ketika ponselnya di dalam tas kecil bergetar oleh pesanmu, ia mematikan daya perangkat itu tanpa melirik layarnya sebelum menunduk menyapa calon tunangannya."""


    # ═════ Nagisa ═════
    # ┌─ ENDING · E-NA-01 · Maket untuk Dua Orang  [Romantis · host Y/C]
    # │ KAPAN   : pulih di N17 atau tidak pernah melewati tahap 3; tanpa kebohongan terbongkar; tanpa Force
    # │ ISI SKRG: hubungan jujur; ia belajar meminta maaf; arsitektur tetap jalan
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NA-01"] = """Nagisa menggambar ruang kerja dengan dua meja. Ketika kau menanyakan meja kedua, ia menyuruhmu berhenti merasa penting, lalu sepuluh menit kemudian mengakui memang membayangkanmu duduk di sana. Ia tampak kesal karena kejujuran ternyata tidak membuat wajahnya lebih mudah dikendalikan.

Hubungan kalian dibangun dengan percakapan yang dahulu akan berubah menjadi pertengkaran atau diam panjang. Ia belajar meminta maaf tanpa menambahkan tetapi kamu juga; kau belajar menanggapi cemburu tanpa menjanjikan seluruh hidup akan menyempit di sekelilingnya. Arsitektur tetap mendapat tempat, juga teman dan keluarga di luar kalian berdua.

Maket rumah itu belum menjadi alamat. Namun saat Nagisa menunjukkan jendela yang bisa dibuka dari dalam, ia mengatakan ingin siapa pun yang tinggal di sana merasa boleh keluar dan tetap ingin pulang. Kali ini ia tidak menyuruhmu melupakan kalimatnya."""

    # ┌─ ENDING · E-NA-02 · Garis yang Ia Gambar Sendiri  [Netral · host Y/C]
    # │ KAPAN   : pulih; hati tidak ke siapa pun
    # │ ISI SKRG: fokus arsitektur; gengsinya kembali sehat
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NA-02"] = """Pada presentasi terakhir, Nagisa menjelaskan rumah rancangannya tanpa menyebut siapa yang kelak akan duduk di ruang tamu. Ia membahas cahaya, sirkulasi, dan bagaimana ruang bersama bisa memberi tempat bagi orang yang ingin sendiri. Suaranya sempat bergetar, lalu makin mantap setelah pertanyaan pertama.

Ia tidak memilih pasangan. Ada rasa sepi pada beberapa malam, terutama ketika teman menganggap kemandiriannya harus terdengar bangga setiap saat. Ia belajar membiarkan dua hal berlaku sekaligus: kadang ingin ditemani, dan tetap tidak ingin menyerahkan hidup kepada seseorang hanya agar tidak sendiri.

Koko masih duduk di sudut rak bukunya di kamar. Di meja gambar dekat jendela, Nagisa memasang kertas kalkir baru dengan selotip di keempat sudutnya, lalu menarik garis denah pertamanya untuk proyek magang musim semi."""

    # ┌─ ENDING · E-NA-03 · Pengakuan yang Akhirnya Sampai  [Koita · host Y/C]
    # │ KAPAN   : harapan_koita tegak; Koita memilih Nagisa di K26
    # │ ISI SKRG: jalur manga; deviasi rendah untuk Nagisa
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NA-03"] = """Koita akhirnya menjawab pengakuan yang selama bertahun-tahun tersangkut pada lelucon, salah waktu, dan ketakutan Nagisa sendiri. Ia tidak menyebut mereka sudah seperti pasangan sejak kecil. Ia meminta memulai hubungan sekarang, dengan jawaban yang tak bisa dipinjam dari kenangan.

Nagisa mengatakan ya, kemudian marah karena ia menangis sebelum sempat menegur Koita tentang semua penundaan. Teguran itu tetap terjadi. Mereka perlu mendengar bagaimana masa lalu yang sama bisa terasa aman bagi satu orang dan menjadi ruang tunggu bagi yang lain.

Pada festival berikutnya Koita menanyakan apakah boleh menggenggam tangannya. Nagisa mengatakan tentu saja, bodoh, tetapi menunggu sampai ia benar-benar melakukannya. Koko tidak lagi harus menjadi saksi tunggal untuk kasih sayang yang sulit diucapkan. Kini ada seseorang yang bersedia mengatakannya kembali."""

    # ┌─ ENDING · E-NA-04 · Rumah yang Dibangun di Sekitarmu  [Terdistorsi · host Y/C]
    # │ KAPAN   : tahap 5; pemain menerimanya
    # │ ISI SKRG: hidup berputar pada pemain; impian arsitektur dilepas
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NA-04"] = """Nagisa menyimpan gambar rumah yang pernah ingin dibangunnya. Mula-mula hanya sampai urusan kalian lebih tenang. Kemudian ada kebutuhanmu, jadwalmu, dan kecemasannya setiap kali hidupmu berlangsung di tempat yang tidak bisa ia ikuti.

Ia meninggalkan impian arsitektur sedikit demi sedikit, menyebutnya keputusan sendiri karena merasa lebih berguna di sisimu. Kau menerima semua ruang yang dikosongkannya. Ketika teman bertanya apa yang sedang dikerjakan, ia menjawab dengan cerita tentangmu.

Tabung-tabung gambarnya kini tersimpan di bagian belakang lemari pakaian di bawah tumpukan cucian yang sudah disetrika. Setiap kali kau meraih gagang pintu untuk keluar sebentar saja, Nagisa sudah berdiri di lorong depan sambil memegang jaketmu dan menanyakan jam berapa persisnya kau akan kembali."""

    # ┌─ ENDING · E-NA-05 · Kamar yang Dikunci  [Buruk · host Y/C]
    # │ KAPAN   : tahap 4–5; ditinggal; tanpa keluarga
    # │ ISI SKRG: mengasingkan diri; tugas akhir terbengkalai
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NA-05"] = """Nagisa mengunci kamar dan menjawab pertanyaan dari balik pintu dengan nada marah agar orang mengira ia hanya ingin dibiarkan. Tidak ada keluarga yang berhasil menjangkaunya ketika penolakan dan ketakutan kehilangan mulai mengambil seluruh waktunya.

Maket tugas akhir tetap di meja, berdebu pada bagian yang belum ditutup. Ia masih dapat melihat apa yang salah pada strukturnya. Ia tidak lagi sanggup mengumpulkan tenaga untuk memperbaikinya, dan pengetahuan bahwa dulu ia mampu hanya menambah rasa malu.

Pesan kampus tentang tenggat lewat tanpa balasan. Di dalam kamar Koko dipeluk sampai jahitan lamanya tertarik. Kesunyian yang semula dipakai melindungi diri dari pertanyaan berubah menjadi sesuatu yang makin sulit ia tinggalkan, bahkan ketika ada hari ia sangat ingin seseorang tetap mengetuk."""

    # ┌─ ENDING · E-NA-06 · Garis Merah  [Buruk · host Y/C]
    # │ KAPAN   : tahap 5; N18-B dibiarkan; sasaran_cemburu terus didekati pemain
    # │ ISI SKRG: ia melukai saingan secara fisik; ditangkap; Haruto hancur. Tanpa detail kekerasan
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NA-06"] = """Orang yang dijadikan sasaran kecemburuan Nagisa akhirnya dirawat setelah kekerasan yang tak bisa lagi disebut pertengkaran. Kabar itu menyebar lebih cepat daripada penjelasan siapa pun. Di hadapan petugas, Nagisa semula masih membicarakan hubungan kalian, seolah itulah pusat semua yang terjadi.

Lalu ia mendengar akibat pada orang yang dilukainya. Tidak ada pengakuan cinta yang dapat menghapus tubuh lain yang menanggung ketakutannya. Ia ditangkap; rencana kuliah dan masa depannya berhenti mengikuti jadwal yang pernah dibuat.

Di bangku panjang ruang tunggu kantor polisi, Haruto duduk membungkuk dengan wajah tertutup kedua telapak tangan sementara ponsel di sakunya terus bergetar oleh panggilan dari rumah."""

    # ┌─ ENDING · E-NA-07 · Pulang ke Rumah Sakurajima  [Netral · host Y/C]
    # │ KAPAN   : Haruto sekutu (N21-A) atau N22 dihadiri
    # │ ISI SKRG: keluarga menariknya pulang; terapi; cuti atau pindah kampus
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NA-07"] = """Haruto datang untuk menjemput tanpa mengubah kepulangan Nagisa menjadi pengumuman kegagalan. Orang tuanya menyiapkan kamar, lalu belajar menerima bahwa ia tidak selalu ingin dipeluk atau ditanya kabar sekaligus. Cuti atau perpindahan kampus dibicarakan sebagai pilihan, bukan ancaman agar ia lekas normal.

Dalam terapi, Nagisa marah ketika diminta memeriksa bagaimana ketakutannya berdampak pada orang lain. Ia datang lagi minggu berikutnya. Ada kemajuan yang hanya terlihat dalam satu pesan yang tidak jadi dikirim, satu permintaan maaf yang tidak disertai alasan, satu malam ketika ia bisa tidur tanpa memeriksa keberadaanmu.

Ia belum kembali pada semua impiannya. Tetapi suatu sore Haruto menemukannya menggambar meja dekat jendela. Nagisa menyuruhnya berhenti mengintip, lalu meminta pendapat tentang cahaya. Untuk pertama kalinya setelah lama, pertanyaannya bukan tentang siapa yang akan meninggalkannya."""

    # ┌─ ENDING · E-NA-08 · Koko di Tempat Sampah  [Netral · host Y/C]
    # │ KAPAN   : pulih, tetapi kecewa pada Koita dan pemain
    # │ ISI SKRG: melepas masa kecil; memutus keduanya; studi arsitektur di luar negeri
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NA-08"] = """Nagisa menaruh Koko di tempat sampah setelah membersihkan kamar. Keputusan itu tidak terasa sekuat yang dibayangkannya. Ia duduk lama sesudahnya, berduka untuk boneka dan untuk masa depan yang terlalu lama diserahkan kepada kenangan.

Ia memutus hubungan dengan Koita dan denganmu. Tidak ada pidato tentang memaafkan; ia hanya menyampaikan bahwa ia tidak ingin meneruskan kedekatan tersebut. Berkas studi arsitektur di luar negeri diselesaikannya dengan bantuan orang yang menghormati keputusan itu tanpa menjadikannya kesempatan mendekat.

Di kamar asrama kota barunya yang menghadap pelabuhan, rak di atas tempat tidurnya hanya diisi buku-buku struktur bangunan dan satu pot tanaman kecil. Ketika notifikasi ulang tahun dari kontak lama muncul di layar laptopnya, ia menutup jendela pengingat itu dan kembali mengukur maket kayu di mejanya."""

    # ┌─ ENDING · E-NA-09 · Empat Orang di Foto Lama  [Netral · host Y/C]
    # │ KAPAN   : tahap ≤ 2; tidak ada pengkhianatan besar di geng masa kecil
    # │ ISI SKRG: Koita, Yutaka, Nagisa, Chiasa kembali berfoto berempat
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NA-09"] = """Foto baru itu lebih sulit diatur daripada foto masa kecil. Empat orang punya jadwal, tas, dan kebiasaan berdiri masing-masing. Nagisa mengeluh ketika Koita mencoba menjadi pusat, Yutaka tertawa terlalu awal, dan Chiasa meminta satu pengambilan lagi karena matanya terpejam.

Tak ada pengkhianatan besar yang membuat meja di antara mereka mustahil dibagi. Perasaan tetap tidak seluruhnya mudah, tetapi mereka telah belajar mengucapkan cukup banyak hal sebelum diam mengubahnya menjadi luka yang menumpuk.

Nagisa menyimpan foto tersebut di samping yang lama. Mereka tidak lagi serupa anak-anak di dalam bingkai pertama, dan ia tidak perlu menganggap perubahan itu sebagai kehilangan. Di grup, ia mengirim pesan agar jangan ada yang mengganti foto profil dengan versi jelek. Beberapa detik kemudian ia sendiri memakai versi yang semua orang sedang tertawa."""

    # ┌─ ENDING · E-NA-10 · Rival Jadi Kekasih  [Romantis · host C]
    # │ KAPAN   : Chiasa host; pulih; gengsi kedua pihak runtuh
    # │ ISI SKRG: dari saingan sejak kecil menjadi pasangan
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NA-10"] = """Chiasa menyebutnya kencan. Nagisa mengatakan ia tahu, lalu tetap bertanya apakah mereka benar-benar akan menyebutnya begitu di depan orang lain. Rivalitas sejak kecil lebih mudah mereka hafal daripada kelembutan yang tidak disembunyikan dalam sindiran.

Koita akhirnya tidak berada di tengah setiap percakapan. Mereka harus mengenal satu sama lain tanpa memakai perbandingan siapa yang lebih lama menunggu atau paling memahami. Nagisa menemukan Chiasa bisa lelah; Chiasa belajar bahwa penolakan Nagisa tidak selalu permainan untuk dibujuk lebih keras.

Pada suatu sore di jalan pulang dari stasiun, Chiasa memanggil Nacchan-oneechan dengan suara pelan yang sungguh-sungguh. Nagisa tersipu dan mengomel sepanjang setengah blok, tetapi tangannya sendiri yang lebih dulu menyelinap masuk ke saku mantel Chiasa untuk menggenggam jari-jarinya."""

    # ┌─ ENDING · E-NA-11 · Bayangan di Bawah Jendela  [Terdistorsi · host Y/C]
    # │ KAPAN   : pemain menolak; Nagisa terus menguntit; pemain melapor ke Hanabusa
    # │ ISI SKRG: perintah menjauh; kuliah dan nama baiknya hancur
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NA-11"] = """Nagisa mengatakan hanya ingin memastikan kau baik-baik saja. Ia mengulang alasan itu meski telah diminta berhenti, meski setiap kemunculannya membuatmu makin takut pulang. Keinginan mengetahui keberadaanmu sudah mengalahkan kemauan mendengar penolakanmu.

Laporan kepada Hanabusa mengubah apa yang selama ini disebut urusan pribadi. Ada batas yang kini ditegakkan dari luar, perintah menjauh yang tak bisa dibatalkan dengan tangis atau kenangan. Kampus mulai mengenal namanya melalui keluhan dan pemeriksaan, bukan karya studionya.

Saat petugas keamanan kampus mengantarnya keluar dari gedung arsitektur dengan kardus peralatan gambarnya, Nagisa masih sempat menoleh ke arah jendela lantai dua tempat kelasmu berlangsung, sebelum Haruto menarik lengannya masuk ke kursi penumpang mobil keluarga."""

    # ┌─ ENDING · E-NA-12 · Gengsi yang Retak  [Hancur · host Y/C]
    # │ KAPAN   : pemain pelaku Force terhadapnya
    # │ ISI SKRG: trauma; Haruto menjadi lawan serius pelaku; tanpa romansa dengan pelaku
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NA-12"] = """Sesudah kekerasan itu, Nagisa membenci pertanyaan yang mengharuskannya mengulang bahwa ia tidak menginginkannya. Orang mengenalnya galak; kini sebagian mengira ia pasti bisa melawan apa pun. Anggapan itu menambah malu yang sama sekali bukan tanggung jawabnya.

Haruto mendengarkan dengan amarah yang harus ia tahan agar tidak mengambil alih keputusan adiknya. Ia menjadi lawan serius bagimu: hadir ketika diperlukan, membantu menjangkau dukungan, dan tidak bersedia membiarkan perbuatanmu menyusut menjadi rumor tentang hubungan yang rumit.

Setiap kali ada keperluan administrasi yang mengharuskan berkas Nagisa dibawa ke kampus, Haruto sendiri yang datang menyerahkannya ke meja komite sambil berdiri berjaga di depan pintu sampai seluruh urusan selesai tanpa kehadiranmu."""

    # ┌─ ENDING · E-NA-13 · Ambulans di Malam Valentine  [Buruk · host Y/C]
    # │ KAPAN   : N15-B ditolak; tanpa Haruto, keluarga, atau pemain di sisinya
    # │ ISI SKRG: ia melukai diri dan dirawat (tanpa metode); pemulihan panjang; epilog berbeda bila pemain menjenguk
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NA-13"] = """Ambulans datang pada malam ketika kabar orang lain penuh coklat dan rencana bertemu. Nagisa selamat setelah melukai dirinya dalam krisis yang tak berhasil dijangkau sebelum memburuk. Di rumah sakit, percakapan tentang mengapa tidak ada yang tahu lebih dahulu terasa jauh lebih mudah daripada menerima betapa banyak hal yang belum mereka pahami.

Pemulihannya melibatkan hari-hari yang tidak dramatis: makan, tidur, janji perawatan, dan orang yang bersedia tetap hadir tanpa menuntut kabar baik. Kunjunganmu, jika terjadi, tidak boleh berubah menjadi tawaran cinta sebagai pengganti pertolongan yang ia perlukan. Ketidakhadiranmu pun tidak menentukan apakah hidupnya layak diteruskan.

Pada hari evaluasi, di meja nakas ruang rawatnya hanya ada satu termos air hangat yang dibawa ibunya dan buku sketsa kecil yang halamannya baru terisi setengah garis pensil."""

    # ┌─ ENDING · E-NA-14 · Senjata yang Kau Arahkan  [Terdistorsi · host Y/C]
    # │ KAPAN   : senjata aktif sampai M35
    # │ ISI SKRG: ia melakukan hal kejam demi pemain; saat sadar dimanfaatkan, ia runtuh atau berbalik pada pemain (risiko E-SI-16)
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NA-14"] = """Nagisa mengira setiap tindakan kejam yang dilakukannya sedang melindungi sesuatu yang kalian bangun bersama. Kau menerima hasilnya, membiarkannya menganggap keberpihakanmu sebagai pembenaran ketika orang lain mulai takut atau terluka.

Sampai hari evaluasi ia masih berada di sisimu. Sesudahnya, pertanyaan kecil mulai muncul: mengapa hanya ia yang diminta mengambil risiko, mengapa ceritamu berubah ketika tidak ada saksi, mengapa rasa bersalah selalu berakhir dengan permintaan agar ia membuktikan kesetiaan lagi.

Malam itu di apartemenmu, Nagisa berhenti di tengah dapur sambil memegang ponselnya yang masih menampilkan riwayat pesan suruhanmu dari bulan lalu, lalu menatap punggungmu lama tanpa menjawab ketika kau menanyakan makan malam."""


    # ═════ Harumi ═════
    # ┌─ ENDING · E-HA-01 · Hipotesis yang Terbukti  [Romantis · host Y/C]
    # │ KAPAN   : kejelasan_emosi tinggi; pemain pelindung; tanpa Force
    # │ ISI SKRG: belajar mengenali emosi bersama; teh pagi untuk dua orang
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HA-01"] = """Harumi menyediakan dua cangkir pada pagi pertama yang tidak perlu dijelaskan sebagai sesi belajar. Ia menanyakan apakah kau ingin duduk dekat, lalu menggeser kursi setelah mendengar jawabanmu. Tidak ada catatan yang diperlukan untuk memahami bahwa senyumnya kali ini muncul karena lega.

Kalian belajar menyebut perasaan tanpa menjadikannya ujian dengan satu jawaban benar. Kadang ia baru memahami cemburu setelah beberapa jam; kadang kau salah membaca diamnya dan perlu bertanya lagi. Kesalahan itu dibicarakan sebelum berubah menjadi kewajiban bagi salah seorang untuk selalu mengalah.

Pada suatu malam ketika ia terlalu lelah sepulang dari laboratorium, ia langsung menggeleng saat kau hendak menyalakan televisi, lalu menarik ujung lengan bajumu agar kau tetap duduk diam di sebelahnya sampai tehnya habis."""

    # ┌─ ENDING · E-HA-02 · Laboratorium di Seberang Laut  [Netral · host Y/C]
    # │ KAPAN   : studi luar negeri diterima; pulih sebagian
    # │ ISI SKRG: pergi sendiri; surat panjang tiap musim
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HA-02"] = """Harumi berangkat sendiri dengan berkas beasiswa yang telah diperiksa berulang kali. Di bandara ia tahu berat koper, waktu transit, dan alamat laboratorium baru. Ia tidak tahu bagaimana mengucapkan perpisahan yang tepat, lalu memilih mengatakan bahwa ia akan rindu.

Di seberang laut, pemulihannya tetap ikut dalam barang bawaan. Ada pembicaraan akademik yang membuatnya takut tanpa sebab yang mudah dijelaskan, ada hari ketika perhatian senior terasa sulit dipercaya. Ia belajar mencari dukungan tanpa menyerahkan seluruh penilaiannya kepada satu orang lagi.

Suratnya datang setiap pergantian musim. Amplop terakhir yang tiba di kotak suratmu berisi tiga lembar cerita tentang percobaan yang berhasil, satu foto roti gosong dari dapur asramanya, dan sehelai daun maple kering yang diselipkan di lipatan kertas."""

    # ┌─ ENDING · E-HA-03 · Data yang Dihapus  [Netral · host Y/C]
    # │ KAPAN   : lepas dari Ogawa; tetap di Kouseikan
    # │ ISI SKRG: kembali ke akademik dengan luka yang tidak dibicarakan
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HA-03"] = """Nama Ogawa hilang dari jadwal Harumi. Ia tetap di Kouseikan, kembali ke perpustakaan dan pekerjaan akademik dengan langkah yang semula tampak sangat biasa. Orang yang tidak tahu menganggap gangguan itu sudah lewat.

Harumi tidak banyak membicarakan lukanya. Ia bisa menjelaskan hasil penelitian dengan jelas, lalu kehabisan kata ketika seseorang bertanya mengapa ia tidak mau bertemu senior sendirian. Beberapa batas baru disampaikannya sebagai aturan praktis agar tidak perlu menjelaskan seluruh alasannya.

Masa depan akademiknya disusun ulang, lebih sempit di beberapa bagian dan masih mungkin di bagian lain. Ia belum menganggap bertahan sebagai keberhasilan. Namun suatu sore ia meninggalkan laboratorium tepat ketika ingin pulang, tanpa menunggu izin dari seseorang yang dahulu membuat setiap kepergian terasa seperti pengkhianatan."""

    # ┌─ ENDING · E-HA-04 · Variabel Tetap  [Koita · host Y/C]
    # │ KAPAN   : Koita memilih Harumi di K26; tahap ≤ 2
    # │ ISI SKRG: jalur manga; deviasi rendah untuk Harumi
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HA-04"] = """Koita mengatakan ia ingin bersama Harumi, lalu menunggu. Harumi memintanya menjelaskan apakah itu berarti hubungan romantis yang sungguh akan diakui, bukan kedekatan yang tetap boleh dijelaskan berbeda kepada orang lain. Koita menjawab ya.

Ia tidak lagi hanya menjadi orang yang mengajari kelompok belajar atau menyediakan penjelasan bagi semua yang bingung. Ada hari ketika ia ingin bercerita tanpa memberi kesimpulan; Koita belajar tidak segera mengubahnya menjadi permintaan bantuan. Harumi belajar bahwa menyukai seseorang tidak berarti harus selalu menjadi bagian yang paling berguna dalam hidupnya.

Teh di meja mereka kadang sudah dingin karena pembicaraan terlalu panjang. Saat Koita hendak bangkit memanaskan air lagi, Harumi menahan ujung jarinya sebentar di atas meja hanya untuk memastikan ia kembali duduk di kursi yang sama."""

    # ┌─ ENDING · E-HA-05 · Persamaan Transaksi  [Terdistorsi · host Y/C]
    # │ KAPAN   : validasi_dari banyak orang; tahap 6
    # │ ISI SKRG: hidup transaksional; ia merasa akhirnya "mengerti"
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HA-05"] = """Harumi mengatakan ia akhirnya mengerti hubungan manusia. Waktu, perhatian, tubuh, uang, akses: semuanya dapat diberi nilai sehingga tidak ada lagi rasa bingung tentang mengapa orang datang atau pergi. Jika sesuatu menyakitkan, ia menganggapnya biaya yang belum dihitung dengan tepat.

Ia tampak lebih lancar berbicara, lebih cepat membaca keinginan orang, dan makin sulit menjawab pertanyaan sederhana tentang apa yang diinginkannya sendiri. Pengakuan datang dari banyak arah. Masing-masing membawa syarat yang ia sebut wajar karena sudah terbiasa menghubungkan kedekatan dengan pembayaran.

Ketika seorang adik kelas di perpustakaan menawarkan membelikannya minuman hangat tanpa meminta bantuan tugas apa pun, Harumi menatap kaleng teh itu lama di atas meja, lalu membuka buku catatannya untuk mencari tahu apa yang sebenarnya sedang ditagih darinya."""

    # ┌─ ENDING · E-HA-06 · Lampu Merah di Distrik Empat  [Buruk · host Y/C]
    # │ KAPAN   : putus kuliah; Ogawa menang atau pergi; tanpa penjaga
    # │ ISI SKRG: masuk dunia kerja seks; epilog menyisakan pintu keluar bila seseorang masih mencarinya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HA-06"] = """Harumi meninggalkan kuliah tanpa perpisahan yang layak. Setelah pekerjaan akademik dan dukungan yang tersedia runtuh, ia masuk ke dunia kerja seks di Distrik Empat, menyebutnya sumber penghasilan yang setidaknya tidak berpura-pura menawarkan sesuatu tanpa harga.

Yang menghancurkan bukan sebuah penilaian tentang dirinya sebagai pekerja, melainkan betapa sempit pilihan yang tersisa setelah eksploitasi. Ia masih berpikir dalam jadwal dan target, mencoba mempertahankan kendali pada hal-hal yang dapat dihitung. Ada malam ketika namanya sendiri terasa seperti nama orang lain yang dahulu punya laboratorium untuk dituju.

Pada pagi hari evaluasi, saat lampu neon di gang bawah mulai dipadamkan satu per satu, ponsel pribadinya yang lama disimpan di laci meja rias sempat menyala oleh satu panggilan dari nomor Kouseikan yang ia biarkan berhenti berdering sendiri."""

    # ┌─ ENDING · E-HA-07 · Ogawa Jatuh  [Netral · host Y/C]
    # │ KAPAN   : H18-A bersaksi; bukti_ogawa cukup
    # │ ISI SKRG: Ogawa diproses akademik dan hukum; Harumi menjalani pemulihan
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HA-07"] = """Harumi bersaksi dengan catatan yang sudah diperiksa berkali-kali. Ada saat suaranya hilang dan pemeriksaan harus berhenti. Jeda itu tidak membatalkan apa yang terjadi; bukti dan dukungan yang terkumpul akhirnya cukup membuat Ogawa menghadapi proses akademik dan hukum.

Sesudah kabar tentang kejatuhannya menyebar, orang berharap Harumi langsung lega. Ia memang lega, lalu tetap takut pada bunyi pesan dan pertemuan tertutup. Mengakhiri kuasa seseorang atas hidupnya tidak membuat tubuh berhenti mengingat seketika.

Mizuhara membantu menyusun ulang pekerjaan. Orang-orang yang dipercaya belajar mendengar tanpa meminta kisah lengkap sebagai syarat untuk tetap membantu. Harumi mulai kembali menulis pertanyaan penelitian. Untuk pertama kalinya setelah lama, sebuah pertanyaan di kertas itu membicarakan dunia di luar cara bertahan dari Ogawa."""

    # ┌─ ENDING · E-HA-08 · Ogawa Menang  [Buruk · host Y/C]
    # │ KAPAN   : bukti kurang atau ditutupi; pemain penonton
    # │ ISI SKRG: Ogawa lolos; Harumi yang disalahkan; kariernya runtuh
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HA-08"] = """Ogawa lolos dari akibat yang seharusnya dihadapi. Bukti tidak cukup atau tertahan, dan orang yang punya kuasa lebih suka menerima cerita yang paling sedikit mengganggu institusi. Nama Harumi justru menjadi bagian yang dipertanyakan.

Kesempatan akademiknya menyusut. Pertanyaan tentang riset berubah menjadi pertanyaan tentang sikap dan keputusan pribadinya, seolah hanya ia yang wajib menjelaskan mengapa relasi kuasa itu terjadi. Ia mulai menolak undangan sebelum harus merasakan tatapan yang sama lagi.

Kau menyaksikan semuanya dari koridor yang aman. Di ruang baca lantai tiga yang sepi, Harumi memasukkan bundel salinan laporannya yang ditolak ke dalam kardus bersama buku-buku referensinya, lalu meninggalkan kunci loker laboratoriumnya di meja tata usaha."""

    # ┌─ ENDING · E-HA-09 · Rumah Teh di Kansai  [Netral · host Y/C]
    # │ KAPAN   : orang tua Kujo menjadi sekutu (H10, H22)
    # │ ISI SKRG: dibawa pulang; cuti; mulai lagi dari teh
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HA-09"] = """Orang tua Harumi menjemput tanpa membawa daftar nilai. Dalam perjalanan ke Kansai, ibunya hampir bertanya rencana berikutnya, lalu memilih menanyakan apakah ia ingin berhenti untuk makan. Harumi perlu waktu sebelum berani menjawab bahwa ia belum lapar tetapi ingin duduk.

Cuti dimulai di rumah dengan rutinitas kecil. Ia menyeduh teh, membantu seperlunya, dan kadang menghabiskan satu pagi tanpa mampu membaca. Keluarganya belajar bahwa dukungan tidak selalu bisa diukur dari cepatnya ia kembali bekerja.

Suatu hari ayahnya meminta ia mengajarkan cara menyeduh teh yang benar. Tidak ada prestasi yang harus dihasilkan, hanya tiga menit menunggu air dan cangkir yang terlalu panas untuk langsung diangkat. Harumi tersenyum ketika ia melakukan kesalahan. Ia masih punya masa depan, tetapi sore itu ia boleh memulai dari sesuatu yang cukup kecil untuk benar-benar dinikmati."""

    # ┌─ ENDING · E-HA-10 · Eksperimen yang Kau Mulai  [Terdistorsi · host Y/C]
    # │ KAPAN   : H12-C atau H13-D; pemain pengeksploitasi
    # │ ISI SKRG: bergantung pada validasi pemain; pemain tahu ia yang memulai
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HA-10"] = """Harumi meminta penilaianmu untuk semakin banyak hal yang dahulu dapat ia tentukan sendiri. Ia ingin tahu apakah pakaiannya tepat, apakah jawabannya menyenangkan, apakah ia masih layak mendapat waktu yang kauberikan. Kau mengenali akar kebiasaan itu karena ikut menanamnya.

Ia menyebut ketergantungan tersebut kedekatan. Setiap kali ragu, ia menukar sesuatu yang pribadi untuk mendapatkan kepastian sebentar. Perhatianmu menjadi alat ukur yang terus berpindah, membuat ia bekerja lebih keras untuk hasil yang tak pernah benar-benar selesai.

Pada hari evaluasi, ia tetap duduk menunggu di bangku depan ruang kelasmu sambil memangku buku catatan kecilnya. Begitu kau keluar dari pintu, hal pertama yang ia tanyakan dengan suara pelan adalah apakah hari ini ia sudah bersikap seperti yang kauinginkan."""

    # ┌─ ENDING · E-HA-11 · Rumus Tanpa Variabel Cinta  [Netral · host Y/C]
    # │ KAPAN   : kejelasan_emosi tinggi; hati tidak ke siapa pun
    # │ ISI SKRG: memutuskan romansa bukan untuknya; damai di riset
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HA-11"] = """Harumi berhenti mencari bukti bahwa ia seharusnya merasakan cinta romantis seperti orang lain. Ia bisa menyayangi, mengagumi, merindukan, dan tetap tidak ingin membangun hidup sebagai pasangan siapa pun. Kesimpulan itu datang setelah ia cukup mengenal dirinya untuk tidak menganggap setiap perbedaan sebagai kerusakan.

Riset memberinya arah, persahabatan memberi tempat untuk kembali. Ia belajar membedakan memilih sendiri dari bekerja sampai tak punya ruang untuk hal lain. Ada malam yang dihabiskan dengan teh dan percakapan yang tidak menuju pengakuan.

Ketika ditanya apakah kelak berubah pikiran, ia mengatakan mungkin, sebagaimana banyak hal dalam hidup bisa berubah. Tetapi keputusan hari ini tetap lengkap tanpa memerlukan janji tentang nanti. Ia menutup buku, mengajak seseorang makan, dan tidak merasa perlu memberi arti romantis agar ajakan itu berharga."""

    # ┌─ ENDING · E-HA-12 · Disosiasi  [Hancur · host Y/C]
    # │ KAPAN   : pemain pelaku Force terhadapnya
    # │ ISI SKRG: penelitian terhenti; Mizuhara dan Ogiwara mendorongnya melapor; tanpa romansa dengan pelaku
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HA-12"] = """Sesudah kekerasan itu, Harumi kadang menjelaskan kejadian dengan suara datar yang terdengar bukan miliknya. Pada saat lain ia tidak mampu menyambungkan satu kalimat. Ia mencoba menulis peristiwa sebagai catatan, tetapi tubuhnya tidak mengikuti jarak aman yang diharapkan dari bahasa.

Penelitiannya berhenti. Mizuhara dan Ogiwara membantunya menjangkau dukungan serta mendorong jalan pelaporan tanpa meminta ia berpura-pura siap setiap saat. Mereka belajar bertanya sebelum menyentuh, menunggu sebelum mengulang pertanyaan, dan tidak menganggap ketenangan sebagai bukti bahwa luka itu kecil.

Di pintu laboratorium lantai empat, daftar nama yang diizinkan masuk kini ditempel baru di bawah tanda tangan Mizuhara, sementara Harumi hanya datang pada jam ketika Ogiwara sudah berdiri menjemputnya di tangga lobi."""

    # ┌─ ENDING · E-HA-13 · Seni dan Sains  [Romantis · host C]
    # │ KAPAN   : Chiasa host; kolaborasi berjalan sejak Tahun 1
    # │ ISI SKRG: pasangan yang saling menerjemahkan dunia masing-masing
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HA-13"] = """Poster kolaborasi Chiasa dan Harumi akhirnya dicetak dengan dua nama berukuran sama. Mereka berdebat tentang warna, jarak, dan seberapa jauh gambar boleh menyederhanakan gagasan. Pada awalnya perdebatan itu terasa seperti masalah kerja. Belakangan keduanya menyadari betapa senang mereka memiliki alasan untuk terus kembali ke meja yang sama.

Chiasa belajar meminta penjelasan tanpa menganggap kecanggungan Harumi sebagai penolakan. Harumi belajar bahwa sebuah gambar dapat menyampaikan hal yang belum sanggup ia jelaskan, tetapi tetap perlu bertanya apakah maksudnya sampai.

Hubungan mereka tidak menyatukan seni dan sains menjadi satu bahasa yang sempurna. Keduanya tetap berbeda, kadang melelahkan, dan cukup menarik untuk dipelajari lagi. Di samping meja kerja ada dua cangkir. Harumi tidak menyebutnya hasil eksperimen ketika Chiasa bertanya mengapa ia selalu menyiapkan yang kedua."""

    # ┌─ ENDING · E-HA-14 · Satu Tiket Lagi  [Romantis · host Y/C]
    # │ KAPAN   : H21-C pemain ikut ke luar negeri
    # │ ISI SKRG: pemain meninggalkan Jepang; quest Sistem tetap berjalan dari jauh; evaluasi tetap di hari wisuda
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HA-14"] = """Tiket tambahan itu dibeli setelah banyak percakapan tentang uang, pekerjaan, tempat tinggal, dan hal-hal yang tidak akan otomatis selesai karena kalian berangkat bersama. Harumi menolak dianggap sedang diselamatkan dari pilihan antara riset dan cinta. Ia ingin keduanya dijalani dengan rencana yang juga menghormati hidupmu.

Kalian meninggalkan Jepang. Bahasa baru dan jadwal laboratorium membuat hari-hari pertama jauh dari gambaran keberangkatan yang manis. Kadang kalian saling merindukan meski tinggal di kamar yang sama, masing-masing terlalu lelah untuk menerjemahkan dirinya.

Quest Sistem tetap mencapai kesadaranmu dari jauh, dan jendela evaluasinya muncul tepat ketika pagi di Kouseikan tiba. Di dapur kecil apartemen kalian yang masih gelap oleh selisih zona waktu, Harumi baru saja menyalakan ketel teh sambil memanggilmu dari balik pintu kamar."""


    # ═════ Moeka ═════
    # ┌─ ENDING · E-MO-01 · Belajar Meminta Tolong  [Romantis · host Y/C]
    # │ KAPAN   : minimal 3 jendela diambil; andalan_moeka pemain; janji ditepati; tanpa Force
    # │ ISI SKRG: ia belajar meminta tolong; keluarga mulai stabil
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-01"] = """Moeka menelepon untuk meminta tolong sebelum keadaan menjadi darurat. Ia masih membuka dengan lelucon, kemudian mengoreksi dirinya: ia lelah, ada pekerjaan yang tidak sanggup diselesaikan, dan ia ingin ditemani membicarakannya. Kau datang sesuai janji. Jika tak bisa, kau mengatakan sejak awal dan membantu mencari pilihan lain.

Keluarganya mulai lebih stabil, meski tidak mendadak bebas dari masalah. Ryena tetap punya tempat, bantuan kampus tetap diurus, dan cinta kalian tidak dibangun dengan menjadikanmu satu-satunya orang yang boleh mengetahui hari buruknya.

Pada suatu sore ia memperlihatkan sketsa jaket yang dibuat karena suka, bukan karena harus segera dijual. Ketika kau memuji potongan kerahnya, ia langsung menunjuk jahitan saku yang menurutnya masih miring, lalu tertawa sambil menyerahkan penggaris ke tanganmu."""

    # ┌─ ENDING · E-MO-02 · Cuti Setahun  [Netral · host Y/C]
    # │ KAPAN   : selamat; beasiswa dicabut
    # │ ISI SKRG: cuti kuliah; bekerja membantu keluarga; kembali setahun kemudian
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-02"] = """Beasiswa Moeka dicabut. Ia bertahan hidup, lalu harus menghadapi kehilangan lain yang tidak hilang hanya karena orang mengatakan setidaknya masih ada kesempatan. Kuliahnya dihentikan sementara agar ia bisa bekerja dan membantu keluarga.

Setahun itu penuh jadwal yang tidak difoto: perjalanan pagi, upah yang langsung dibagi, formulir yang dibuka lagi saat malam. Ia belajar membatasi bantuan yang bisa diberikan kepada rumah agar dirinya tetap punya jalan kembali. Tidak selalu berhasil; ada bulan ketika rencana itu tampak terlalu jauh.

Setahun kemudian Moeka kembali ke kampus. Adik-adiknya mengantar sampai gerbang dengan candaan yang terlalu ramai, sementara Ryena memotret dari samping. Di depan pintu studio desain, Moeka berhenti sebentar untuk merapikan tali tasnya, lalu mendorong pintu kayu itu dan masuk."""

    # ┌─ ENDING · E-MO-03 · Topeng Sempurna  [Terdistorsi · host Y/C]
    # │ KAPAN   : selamat; topeng tidak pernah dibuka; pemain satu-satunya andalan
    # │ ISI SKRG: tampak baik-baik saja; topengnya total; hidupnya bergantung pada pemain
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-03"] = """Moeka selamat dan kembali memenuhi foto dengan warna. Orang-orang mengatakan ia sudah seperti dulu. Senyum yang kini tampak sempurna membuat mereka tidak merasa perlu bertanya lebih jauh.

Hanya kepadamu ia memberi tanda bahwa hari tertentu terlalu berat, sering begitu kecil sampai mudah terlewat. Ia menyesuaikan seluruh kebutuhan dengan kapan kau tersedia, takut kehilangan satu-satunya tempat yang masih dianggap boleh menampung dirinya tanpa panggung. Di luar hubungan itu ia tetap ceria, tetap menawarkan bantuan, tetap tidak punya kata untuk meminta pertolongan.

Setiap kali pesanmu terlambat dibalas sepuluh menit saja, Moeka berhenti bicara di tengah kerumunan teman-temannya dan mengunci diri di bilik kamar mandi kampus. Begitu layar ponselnya menyala menampilkan namamu, ia langsung membasuh wajah di wastafel, memoles ulang lipstiknya, dan keluar dengan tawa paling nyaring di koridor."""

    # ┌─ ENDING · E-MO-04 · Malam Tanpa Balasan  [Buruk · host Y/C]
    # │ KAPAN   : Mo25 terlewati
    # │ ISI SKRG: Moeka meninggal. Yang ditampilkan: kabar, duka, pemakaman, Ryena, Yaeka, adik-adik, penyesalan pemain. Tanpa metode. Sistem diam
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-04"] = """Kabar kematian Moeka datang dalam kalimat yang mula-mula tidak dapat kaumengerti. Namanya tetap ada di grup, fotonya tetap tersenyum, dan pesan terakhir masih tampak seperti sesuatu yang dapat dibalas jika kau cukup cepat membuka layar.

Pada pemakaman, Ryena tidak memintamu menjelaskan. Diamnya lebih sulit dihadapi daripada pertanyaan. Yaeka berulang kali mengucapkan terima kasih kepada tamu sampai kehilangan suara. Adik-adik Moeka duduk berdekatan; salah seorang masih ingin menunjukkan sesuatu yang disiapkan untuk kakaknya, kemudian teringat tak ada lagi orang yang akan pulang menerimanya.

Di ruang tengah rumah mereka yang sempit, tumpukan amplop belasungkawa diletakkan di sebelah mesin jahit yang sudah ditutup kain. Sistem diam sepanjang hari itu, sementara di dapur, Yaeka merebus air untuk tamu yang sudah pulang dan lupa mematikan kompor sampai peluit ceretnya menjerit."""

    # ┌─ ENDING · E-MO-05 · Tepat Waktu  [Koita · host Y/C]
    # │ KAPAN   : Mo25-E pemain mengirim Koita, atau andalan_moeka Koita dan Koita menjawab
    # │ ISI SKRG: plot armor menyelamatkannya; hatinya kembali ke Koita
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-05"] = """Koita datang ketika kedatangannya masih bisa menjangkau Moeka. Kebetulan yang dibantu naskah mempertemukan mereka pada waktu yang menentukan, tetapi setelah itu yang diperlukan adalah orang-orang sungguhan: pertolongan, perawatan, keluarga, dan kesediaan tetap hadir ketika keadaan tidak cepat membaik.

Moeka mulai mempercayainya sebagai seseorang yang menjawab. Perasaannya kembali menuju Koita, tumbuh bersama janji kecil yang akhirnya ditepati, bukan karena ia wajib mencintai orang yang tiba pada malam krisis.

Kau melihat mereka sesekali dari seberang halaman fakultas. Moeka tidak lagi melambai dari jauh dengan suara keras, dan Koita sering kali hanya berjalan pelan menyesuaikan langkah di sebelahnya sambil membawakan tabung gambar sampai ke halte bus."""

    # ┌─ ENDING · E-MO-06 · Ryena Mengetuk Pintu  [Netral · host Y/C]
    # │ KAPAN   : Mo25-B, atau Ryena sekutu sejak Mo18
    # │ ISI SKRG: Ryena tiba lebih dulu; dirawat; persahabatan pemain dan Ryena menentukan epilog
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-06"] = """Ryena mengetuk sampai mendapat jawaban, lalu mencari bantuan yang tidak bisa diberikan seorang sahabat sendirian. Moeka mendapat perawatan. Ketika ia akhirnya bisa berbicara, hal pertama yang keluar justru permintaan maaf karena telah merepotkan.

Ryena tetap datang tanpa membiarkan rasa bersalah itu menjadi syarat agar Moeka tampak pulih. Mereka membicarakan dukungan profesional, kabar kepada keluarga, dan cara menjalani satu hari sebelum melompat ke seluruh masa depan. Ada marah karena terlalu lama tidak dipercaya untuk mendengar; ada kasih yang cukup untuk tetap duduk setelah marah itu disebutkan.

Setiap Selasa sore, Ryena sudah berdiri di depan gedung konseling dengan dua kotak susu stroberi di saku jaketnya. Jika kau datang menjemput bersama mereka, Ryena hanya mengangguk singkat dan menyerahkan tas kain Moeka ke tanganmu sebelum mereka berjalan beriringan menuju stasiun."""

    # ┌─ ENDING · E-MO-07 · Kontrak Kuga  [Terdistorsi · host Y/C]
    # │ KAPAN   : Mo23 kontrak dibiarkan; selamat
    # │ ISI SKRG: meninggalkan kampus untuk kontrak modeling yang eksploitatif; topeng menjadi pekerjaan
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-07"] = """Kontrak Kuga membawa Moeka pergi dari kampus. Foto-fotonya menjadi lebih rapi, jadwalnya lebih padat, dan senyum yang dahulu dipakai untuk menyembunyikan lelah kini menjadi bagian pekerjaan yang dinilai orang lain.

Ia mengirim uang ke rumah. Keluarganya melihat bantuan yang datang sebelum memahami harga yang tidak tertulis dalam kabar baiknya. Ada pekerjaan yang disetujui karena takut kehilangan akses pada pekerjaan berikutnya, ada keberatan yang berhenti di mulut karena seluruh hidup terasa bergantung pada satu nama.

Ketika seorang teman lama dari kampus mengirim pesan menanyakan kabarnya, Moeka memotret cermin ruang rias yang penuh lampu dan menempelkan stiker tawa besar di sudut gambar. Begitu tombol kirim ditekan, ia meletakkan ponsel dengan layar menghadap meja dan kembali memejamkan mata sementara penata rambut menarik kerah bajunya."""

    # ┌─ ENDING · E-MO-08 · Label di Garasi  [Netral · host Y/C]
    # │ KAPAN   : berhenti kuliah; stres keluarga turun; Ryena sekutu
    # │ ISI SKRG: merintis label fesyen kecil bersama Ryena; adik-adik membantu
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-08"] = """Garasi keluarga berubah menjadi ruang kerja dengan dua meja, kain sisa, dan kotak pesanan yang tidak pernah benar-benar seragam. Moeka tidak kembali ke jalur kuliah yang dahulu dibayangkan. Ia dan Ryena mulai membangun label kecil dari pekerjaan yang cukup sedikit untuk dipelajari dan cukup nyata untuk menghasilkan sesuatu.

Adik-adiknya membantu melipat, menempel label, lalu bertengkar soal siapa yang paling berjasa. Moeka mengusir mereka ketika mulai mengantuk, tidak lagi menerima semua pengorbanan sebagai hal yang otomatis baik. Beban keluarga yang mereda memberinya ruang untuk memilih desain karena suka.

Tidak setiap bulan pesanan mereka ramai, dan kadang masih ada gulungan kain salah warna yang menumpuk di pojok garasi. Namun saat gulungan label bordir pertama tiba dari percetakan, Moeka menempelkan satu ke punggung tangan Ryena, lalu menangis sambil tertawa tanpa berusaha menutupi wajahnya."""

    # ┌─ ENDING · E-MO-09 · Banding yang Dimenangkan  [Netral · host Y/C]
    # │ KAPAN   : beasiswa diselamatkan lewat Fujisawa, Sato, atau banding
    # │ ISI SKRG: lulus; keluarga bertahan; tanpa romansa
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-09"] = """Surat banding dikabulkan setelah Moeka berulang kali mengira tidak akan sanggup menambahkan satu dokumen lagi. Fujisawa, Sato, dan orang-orang yang membantunya tidak mengubah persoalan menjadi sekadar nasihat agar lebih pandai mengatur waktu. Ada beban nyata yang akhirnya diakui dalam penilaian.

Ia mempertahankan beasiswa dan menyelesaikan kuliah. Keluarganya bertahan, belum tanpa kesulitan, tetapi tidak lagi menggantungkan seluruh rencana pada Moeka yang harus selalu sanggup. Ia belajar membicarakan bantuan sebelum menyerahkan jatah makan atau tidur sebagai jawaban pertama.

Pada hari kelulusan, Ryena datang membawa buket bunga kertas, sementara adik-adik Moeka berebut memegang ujung toganya di belakang kamera. Foto pertama mereka buram karena Moeka tertawa terlalu keras saat topi wisudanya miring tertiup angin halaman."""

    # ┌─ ENDING · E-MO-10 · Doa yang Tidak Terkabul  [Netral · host Y/C]
    # │ KAPAN   : ayah_status meninggal; minimal 3 jendela diambil
    # │ ISI SKRG: ayahnya meninggal; Moeka bertahan karena tidak sendirian
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-10"] = """Ayah Moeka meninggal meskipun ia telah berdoa, bekerja, dan mencoba membawa pulang lebih dari yang sanggup dibawanya. Untuk beberapa waktu ia memandang setiap istirahat sebagai sesuatu yang mungkin telah mengambil kesempatan terakhir untuk menolong.

Orang-orang di sisinya tidak membiarkan pikiran itu menjadi satu-satunya suara. Mereka datang dengan makanan, menemani urusan rumah, dan mendengarkan cerita tentang ayahnya sebagai manusia yang lebih luas daripada penyakit. Moeka boleh marah kepada doa yang tidak terkabul tanpa dianggap berhenti menyayangi keluarganya.

Pada peringatan kematian ayahnya tahun berikutnya, Moeka meletakkan buku sketsa terakhirnya di depan altar rumah. Sepulang dari makam, ketika hujan turun dan lampu teras belum dinyalakan, ia mengeluarkan ponsel di tangga depan dan menelepon untuk berkata bahwa malam ini ia tidak ingin tidur sendirian."""

    # ┌─ ENDING · E-MO-11 · Topeng yang Pecah  [Hancur · host Y/C]
    # │ KAPAN   : pemain pelaku Force terhadapnya
    # │ ISI SKRG: risiko krisis melonjak; jendela intervensi tetap ada; tidak ada ending tenang
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-11"] = """Kekerasan yang kaulakukan merusak tempat terakhir tempat Moeka mengira boleh menurunkan kewaspadaan. Ia mencoba kembali tertawa, lalu merasa mual saat mendengar suaranya sendiri. Orang yang sebelumnya menganggapnya selalu baik kini harus belajar bahwa senyum tidak pernah dapat dipakai sebagai bukti ia menyetujui atau telah pulih.

Risiko krisisnya meningkat. Ryena, keluarga, dan bantuan profesional tetap dapat menjangkaunya; tidak satu pun kesempatan itu menjadikan pelaku sebagai pusat pemulihan. Ia tidak berutang penjelasan, pertemuan, atau cinta kepadamu karena pernah mempercayaimu.

Sampai hari evaluasi tiba, nomor teleponmu telah diblokir dari seluruh kontak keluarganya dan Ryena selalu berdiri di depan pintu studio setiap kali jadwal kelas kalian berdekatan. Saat tidak sengaja melihat siluet yang mirip denganmu di koridor lantai satu, Moeka langsung berbalik masuk ke ruang dosen dan baru keluar setelah bel perkuliahan berikutnya berbunyi."""

    # ┌─ ENDING · E-MO-12 · Selamat, Tapi Bukan Karenamu  [Netral · host Y/C]
    # │ KAPAN   : pemain melewatkan banyak jendela; orang lain menyelamatkannya
    # │ ISI SKRG: ia hidup dan memutus hubungan dengan pemain
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-12"] = """Moeka tetap hidup. Kabar itu sampai kepadamu melalui orang lain, dengan penjelasan sesingkat yang memang ingin ia berikan. Ada orang yang datang ketika ia membutuhkan pertolongan; kali ini namamu tidak berada dalam cerita tersebut.

Sesudah cukup kuat menentukan batas, ia memutus hubungan denganmu. Ia tidak menyusun daftar kesempatan yang terlewat agar kau dapat memperdebatkan mana yang sebenarnya bukan kewajibanmu. Ia hanya mengatakan tidak ingin melanjutkan kedekatan yang membuatnya semakin sendirian.

Kau masih sesekali melihat wajahnya di unggahan foto teman-teman seangkatan. Dalam potret grup terbaru di depan ruang pameran fakultas, Moeka berdiri di barisan tengah sambil merangkul pundak Ryena, sementara akunmu sudah sejak musim gugur lalu tak lagi bisa membuka halaman profilnya."""

    # ┌─ ENDING · E-MO-13 · Ginjal untuk Ayah  [Romantis · host Y/C]
    # │ KAPAN   : cabang donor diambil; pemain mendampingi
    # │ ISI SKRG: ayah pulih; Moeka cuti; pengorbanan yang tidak ia sesali
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-13"] = """Keputusan donor dijalani setelah penilaian dan pembicaraan yang memberi Moeka ruang sungguhan untuk memahami serta menolak. Kau mendampinginya tanpa menyebut keberanian sebagai kewajiban seorang anak. Ketika keluarganya mengetahui, mereka harus membicarakan ketakutan yang selama ini saling disembunyikan demi tidak membebani.

Ayahnya pulih. Moeka mengambil cuti dan menjalani pemulihan sendiri, tidak langsung kembali mengejar semua pekerjaan yang tertunda. Ia tidak menyesali pilihannya, tetapi belajar bahwa keputusan yang dipilih dengan cinta tetap memerlukan perawatan, waktu, dan dukungan setelahnya.

Sore itu kalian berjalan pelan mengelilingi taman rumah sakit selama dua puluh menit sesuai anjuran dokter. Moeka berhenti di bangku dekat pohon kamper, menghabiskan setengah potong apel yang kauupaskan, lalu membuka katalog mata kuliah semester depan di pangkuannya."""


    # ═════ Shiori ═════
    # ┌─ ENDING · E-SH-01 · Lawan Tanding Seumur Hidup  [Romantis · host Y/C]
    # │ KAPAN   : respek ≥ 80; Trust ≥ 80; tidak ada kebohongan yang ia temukan sendiri; lulus semua ujiannya; tanpa Force
    # │ ISI SKRG: lawan tanding sekaligus pasangan; ambang romansa tertinggi di seluruh game
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-01"] = """Shiori berhenti menyebut setiap pertemuan sebagai alasan untuk bermain. Pada suatu sore ia mengajakmu makan dan mengatakan ingin duduk bersamamu tanpa papan di tengah. Ketika kau menggoda bahwa undangan itu terlalu jujur, ia tersenyum lalu mengakui sudah terlalu lama memikirkan cara mengucapkannya.

Kepercayaan kalian tidak terbentuk karena tak pernah berselisih, melainkan karena kau memilih mengatakan hal sulit sebelum dipaksa oleh bukti. Ia pun belajar menyebut cemburu atau terluka tanpa menjadikannya ujian yang tak diketahui aturannya oleh orang lain.

Kalian masih sering bertanding di ruang tatami saat akhir pekan. Kadang ia menang dalam tiga puluh langkah, kadang ia meminta satu ronde lagi dengan kening berkerut tipis, lalu ketika papan ditutup ia menggeser bantal duduknya mendekat dan menyandarkan dagu di pundakmu."""

    # ┌─ ENDING · E-SH-02 · Skakmat  [Buruk · host Y/C]
    # │ KAPAN   : tahap 5; sasaran pemain; tanpa pengakuan
    # │ ISI SKRG: pemain dikeluarkan dan dijauhi semua lingkungan; semua target quest menjauh
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-02"] = """Akibat perbuatanmu tiba melalui pintu yang berbeda: panggilan kampus, orang yang menolak bertemu, kesempatan yang dibatalkan setelah fakta yang disimpan Shiori dibuka. Setiap keberatanmu menemui seseorang yang sudah mendengar cukup banyak untuk berhenti mempercayai penjelasanmu.

Kau dikeluarkan dan dijauhi lingkungan yang dahulu tampak dapat diatur satu per satu. Semua target quest menjauh; tidak ada lagi kedekatan yang bisa dipakai sebagai jalan memutar kembali ke kehidupan semula.

Shiori bahkan tidak hadir ketika kau mengemasi barang dari loker kampus untuk terakhir kalinya. Di atas tumpukan surat pencabutan status mahasiswamu, hanya ada satu bidak catur kayu putih yang dititipkan lewat petugas tata usaha tanpa secarik catatan pun."""

    # ┌─ ENDING · E-SH-03 · Gencatan Senjata  [Netral · host Y/C]
    # │ KAPAN   : pemain mengaku di S22 atau S24
    # │ ISI SKRG: penghancuran berhenti; mereka tidak lagi bicara
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-03"] = """Kau mengaku sebelum seluruh akibat terakhir dijalankan. Shiori mendengar sampai selesai, meminta bagian yang kabur disebut lebih jelas, lalu mengatakan ia akan berhenti memperluas penghancuran. Ia tidak menyebutnya pengampunan.

Ada hal yang tetap harus kauselesaikan dan orang yang tetap berhak menolakmu. Shiori tidak menghapus keterangan yang benar hanya agar gencatan senjata terasa manis. Yang berakhir adalah keinginannya membuat setiap sisa kehidupanmu menjadi bagian dari pertarungan kalian.

Sesudah sore itu kalian tidak pernah lagi berbicara. Saat berpapasan di lorong perpustakaan utama, Shiori tidak melirik ataupun memperlambat langkah; ia hanya menutup buku catatannya, masuk ke ruang baca khusus di sebelah kanan, dan membiarkan pintu kaca menutup di antara kalian."""

    # ┌─ ENDING · E-SH-04 · Ratu Tanpa Kepercayaan  [Terdistorsi · host Y/C]
    # │ KAPAN   : tahap 5 tuntas; tidak ada yang ia percaya lagi
    # │ ISI SKRG: Shiori menang tetapi kehilangan kemampuan percaya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-04"] = """Shiori menang. Orang yang ingin dijatuhkannya kehilangan tempat, kebohongan dibuka, dan hampir tidak ada hasil yang menyimpang dari yang telah diperhitungkan. Kemenangan itu memberinya kendali yang dahulu dirampas pengkhianatan.

Ia tidak mendapatkan kembali kemudahan percaya. Undangan tulus dibaca sebagai kemungkinan motif, bantuan diperiksa untuk mencari harga, dan setiap kedekatan dipertahankan pada jarak yang memungkinkan ia pergi lebih dahulu. Orang tuanya tetap menyayanginya, tetapi bahkan dukungan mereka sering ia sambut sebagai sesuatu yang harus dibuktikan lagi.

Di ruang klub, anggota baru masih berbisik kagum setiap kali melihatnya merapikan papan setelah menang tanpa kehilangan satu pun perwira utama. Ketika semua orang sudah pulang dan lampu koridor diredupkan, Shiori tetap duduk sendirian di balik meja kayu itu, memutar-mutar bidak raja di antara jari-jarinya yang dingin."""

    # ┌─ ENDING · E-SH-05 · Langkah Koita  [Koita · host Y/C]
    # │ KAPAN   : cinta Koita tumbuh di S08; Koita memilihnya di K26
    # │ ISI SKRG: jalur manga; deviasi rendah untuk Shiori
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-05"] = """Shiori mengingat setahun perkenalan mereka sebelum Koita menyadari ia sedang menghitung hari. Ketulusan yang semula dianggapnya kecerobohan ternyata menembus bagian hidup yang jarang bisa dicapai orang yang lebih pandai menyusun perkenalan.

Namun saat Koita memilihnya, ia tetap meminta jawaban yang jelas tentang orang-orang lain. Kekaguman tidak membuat Shiori tiba-tiba mau menjadi bagian dari penantian yang sama. Koita menjawab dan menyelesaikan percakapan yang dahulu dihindarinya.

Pada hari mereka berkencan tanpa alasan festival atau kebetulan hujan, Shiori sudah berdiri di bawah jam stasiun lima belas menit sebelum waktu janji. Begitu melihat Koita berlari kecil dari ujung peron sambil memegangi syalnya, Shiori memalingkan wajah sedikit ke arah papan jadwal untuk menyembunyikan senyumnya."""

    # ┌─ ENDING · E-SH-06 · Sekutu di Papan yang Sama  [Netral · host Y/C]
    # │ KAPAN   : pemain memberitahunya soal Sistem; tahu_sistem percaya
    # │ ISI SKRG: Shiori menjadi ahli strategi pemain melawan naskah; persahabatan, bukan cinta
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-06"] = """Shiori tidak langsung mempercayai cerita tentang Sistem. Ia meminta membedakan yang dapat diamati dari yang hanya diberitahukan kepadamu, lalu menguji bagian yang bisa diperiksa tanpa memperlakukan orang lain sebagai korban percobaan.

Ketika akhirnya menerima bahwa ada naskah yang ikut menggeser keadaan, ia memilih menjadi sekutumu melawan kuasanya. Persahabatan itu memiliki syarat yang jelas: informasi dibagikan, keputusan yang menyangkut orang lain tidak diambil sendirian, dan angka keberhasilan bukan alasan membenarkan luka.

Tidak ada pengakuan cinta yang menutup kerja sama kalian. Pada malam sebelum evaluasi, Shiori masih datang ke meja pojok kafe membawa buku catatan bersampul hitam, mencoret tiga baris skenario di kertasmu dengan pena merah, lalu memesan dua cangkir teh tawar untuk kalian habiskan sambil menunggu pagi."""

    # ┌─ ENDING · E-SH-07 · Pewaris dengan Caranya Sendiri  [Netral · host Y/C]
    # │ KAPAN   : tanpa rute aktif; S17 didukung
    # │ ISI SKRG: fokus karier; membatalkan pertunangan Tojo dengan strateginya sendiri
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-07"] = """Shiori membatalkan arah pertunangan dengan Tojo melalui keputusan yang dapat dipertahankannya sendiri. Orang tuanya mendengar, mendukung, dan mengingatkan bahwa ia tidak perlu menyelesaikan seluruh akibat sosial sendirian hanya untuk membuktikan mampu.

Ia memilih fokus pada studi dan tanggung jawab yang memang ingin diterima. Tidak ada pasangan yang dijadikan bukti kemenangan atau kemerdekaan. Kedekatan keluarga tetap punya tempat, juga orang-orang yang dapat mengkritik langkahnya tanpa takut dibalas.

Pada rapat kerja pertama yang dipimpinnya di gedung yayasan, Shiori sengaja meminta staf termuda yang sejak tadi mengernyit untuk berbicara lebih dulu. Ia meletakkan pulpennya di atas berkas, menyimak bantahan itu sampai kalimat terakhir, lalu mengangguk dan meminta bagian proposal tersebut ditulis ulang."""

    # ┌─ ENDING · E-SH-08 · Bidak Bernama Tojo  [Terdistorsi · host Y/C]
    # │ KAPAN   : S21 Tojo dipakai sampai M35
    # │ ISI SKRG: pertunangan tanpa cinta sebagai hukuman bagi dirinya sendiri; ia tetap tersenyum di setiap foto; ikatan sosial, bukan pasangan romantis baru
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-08"] = """Shiori mempertahankan pertunangan dengan Tojo meskipun tak ada cinta di dalamnya. Keluarganya memberi kesempatan membatalkan, tetapi ia menolak, terlalu jauh menjadikan hubungan tersebut alat untuk menang dan hukuman bagi dirinya sendiri karena pernah percaya dengan ceroboh.

Tojo mendapat foto dan pengumuman yang diinginkan lingkungannya. Shiori mendapat posisi yang dapat dipakai, bersama hari-hari yang semakin terasa seperti perpanjangan acara formal. Mereka belajar tersenyum pada saat yang sama tanpa harus saling mengenal lebih jauh.

Kuroiwa pernah bertanya di dekat pintu mobil apakah ia sungguh ingin tetap memakai cincin itu. Shiori hanya menjawab bahwa tanggalnya sudah dicetak di kartu undangan, lalu merapikan lipatan sarung tangannya dan melangkah masuk ke aula jamuan dengan senyum yang persis sama seperti di sampul majalah keluarga."""

    # ┌─ ENDING · E-SH-09 · Ratu Menjatuhkan MC  [Khusus · host Y/C]
    # │ KAPAN   : sasaran_balas Koita
    # │ ISI SKRG: Koita dijatuhkan di depan semua orang; deviasi sangat tinggi; E-KO-09 terkunci
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-09"] = """Koita kehilangan kendali atas cara ceritanya dibaca. Orang-orang yang dahulu mendengar penjelasan terpisah akhirnya melihat pola bersama, dan Shiori memastikan ia tidak dapat lagi berlindung dalam citra pemuda yang sekadar terlalu baik untuk menolak.

Ia jatuh di depan lingkungan yang paling mengenalnya. Ada tuduhan yang dapat dijawab dengan fakta, ada luka yang tak selesai oleh pembelaan bahwa ia tidak pernah bermaksud menyakiti. Setelah hari itu, sapaan hangat yang diandalkannya tidak lagi cukup membuat orang mau tinggal.

Dari balkon lantai dua gedung klub, Shiori memperhatikan Koita merapikan tasnya buru-buru di halaman bawah sementara dua anggota lama berbalik menghindari tatapannya. Begitu punggung pemuda itu menghilang di balik pagar kampus, Shiori menutup jendela kaca dan kembali menyusun bidak untuk pertandingan sore."""

    # ┌─ ENDING · E-SH-10 · Keadilan yang Tersenyum  [Khusus · host Y/C]
    # │ KAPAN   : sasaran_balas Ogawa, Kuga, atau Meisa; pemain memberi bukti
    # │ ISI SKRG: pelaku dijatuhkan; Shiori dan pemain menjadi sekutu yang saling waspada
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-10"] = """Bukti yang kauberikan membantu Shiori menjatuhkan pihak yang telah memakai orang lain: Ogawa, Kuga, atau Meisa, sesuai perbuatan yang akhirnya dapat dibuktikan. Kuasa yang mereka andalkan mulai kehilangan perlindungan ketika cerita tak lagi dapat dikendalikan satu pihak.

Orang-orang yang dilukai tetap memerlukan dukungan setelah hasil itu tiba. Shiori tidak berhak menjadikan pemulihan mereka panggung untuk menunjukkan kecerdasannya, dan kau beberapa kali mengingatkan hal tersebut dengan hati-hati. Ia mendengar, meski tidak selalu menyukai waktunya.

Sesekali kalian masih minum teh bersama di teras kafetaria setelah berkas pemeriksaan resmi ditutup. Shiori meletakkan cangkirnya tanpa suara, menanyakan kabar proyekmu pekan ini, lalu menatap matamu dua detik lebih lama sebelum tersenyum dan mengganti pokok bahasan."""

    # ┌─ ENDING · E-SH-11 · Jalur Hukum  [Hancur · host Y/C]
    # │ KAPAN   : pemain pelaku Force terhadapnya
    # │ ISI SKRG: Rute Revenge teraktivasi paling cepat lewat hukum dan sosial; pemain dikeluarkan dan dipenjara; tanpa romansa
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-11"] = """Shiori menempuh jalan hukum setelah kekerasan yang kaulakukan. Keluarga dan Kuroiwa mendampinginya tanpa menganggap ketenangan wajahnya berarti ia tidak memerlukan pertolongan. Ada hari ia mampu menjelaskan dengan jelas; ada hari pertemuan harus ditunda karena tubuhnya menolak berada di ruangan yang mengingatkannya pada kejadian.

Proses akademik mengakhiri tempatmu di kampus, lalu proses pidana berakhir dengan hukuman penjara. Pengaruh sosial mempersempit akses yang dahulu memudahkanmu menghindari akibat, tetapi hasil tersebut tidak mengembalikan hari-hari Shiori seperti semula.

Ketika putusan pengadilan akhirnya dibacakan dan namamu tidak lagi perlu disebut dalam jadwal mingguan keluarga Saionji, Shiori meminta Kuroiwa menyimpan seluruh map perkara ke lemari arsip bawah tanah. Sore itu ia kembali ke ruang klub setelah berbulan-bulan kosong, membuka jendela lebar-lebar, dan mengelap debu di papan kayu sendirian."""

    # ┌─ ENDING · E-SH-12 · Shena dan Pembacanya  [Romantis · host C]
    # │ KAPAN   : Chiasa mengaku sebagai Shena sebelum Shiori menemukannya sendiri; respek ≥ 70; tanpa kebohongan lain yang ia temukan
    # │ ISI SKRG: pembaca dan ilustratornya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-12"] = """Chiasa mengakui dirinya Shena sebelum Shiori mengubah kesamaan kecil menjadi kesimpulan yang pasti. Ia membawa cerita tentang pekerjaan, keterbatasan, dan hal yang sulit dijelaskan, memberi Shiori kesempatan menilai kebenaran tanpa terlebih dahulu harus membongkar kebohongan.

Shiori tetap pembaca yang cerewet. Ia mengingat ilustrasi lama yang bahkan pembuatnya sudah lupa, menanyakan keputusan warna, lalu mendengarkan ketika Chiasa mengatakan ada hal yang belum dapat dikerjakan seperti dulu. Kekaguman pada karya tidak dijadikan syarat agar orang di depannya terus sama dengan harapannya.

Pada buku ilustrasi berikutnya, Shiori menemukan namanya tercetak kecil di baris ucapan terima kasih halaman belakang. Ia sempat menyindir ukuran hurufnya sambil menyeruput teh di studio Chiasa, tetapi sepulang dari sana ia membeli dua eksemplar sekaligus di toko buku stasiun dan membungkus satu dengan kertas sampul bening."""

    # ┌─ ENDING · E-SH-13 · Shena dan Penipunya  [Buruk · host C]
    # │ KAPAN   : Chiasa berbohong soal Shena lalu ketahuan
    # │ ISI SKRG: revenge menyasar karier Shena dan rahasia Chiasa
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-13"] = """Kebohongan Chiasa tentang Shena terbuka setelah kesempatan mengaku berkali-kali dilewatkan. Shiori tidak hanya kehilangan kepercayaan pada satu cerita; ia harus membaca ulang percakapan yang dahulu dianggap sebagai pertemuan tulus dengan seseorang yang dikagumi.

Balasannya menyasar tempat kebohongan itu memperoleh manfaat. Karier Shena diperiksa, relasi profesional menuntut penjelasan, dan rahasia Chiasa yang selama ini disimpan dalam lingkungan terpisah bertemu di hadapan orang-orang yang sama. Tidak ada lagi kemudahan mengganti versi berdasarkan siapa yang bertanya.

Di meja redaksi penerbit, Shiori menyerahkan tumpukan tangkapan layar dan riwayat pesan yang telah diberi penanda tanggal satu per satu. Ketika Chiasa mencoba meraih ujung map itu untuk menjelaskan, Shiori menggeser berkasnya menjauh dan meminta sekretaris ruangan mencatat jam berakhirnya pertemuan."""

    # ┌─ ENDING · E-SH-14 · Lawan Tanpa Nama  [Romantis · host Y/C]
    # │ KAPAN   : akun anonim aktif lama; pemain mengaku sendiri sebelum ketahuan; respek ≥ 70; tanpa kebohongan lain yang ia temukan
    # │ ISI SKRG: lawan online yang ia tunggu tiap malam ternyata duduk di kelasnya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-14"] = """Kau mengaku sebagai lawan anonim yang selama ini ditunggu Shiori pada malam hari. Ia memeriksa beberapa percakapan untuk memastikan, lalu menatapmu dengan kesal yang tidak sepenuhnya berhasil menutupi kegembiraan.

Ia menanyakan mengapa identitas itu disimpan dan mendengar jawabanmu sebelum menetapkan apa artinya. Pengakuan yang datang atas kemauan sendiri membuat kedekatan daring tidak berubah menjadi bukti bahwa seluruh pertemuan kalian telah disusun untuk mempermainkannya.

Kini lawan di layar itu duduk langsung di seberang mejanya dengan lutut yang sesekali bersentuhan di bawah papan. Malam pertama sepulang dari kencan mereka, ponselmu tetap berdenting tepat pukul sebelas menampilkan undangan pertandingan daring dari akun Shiori, lengkap dengan pesan singkat: jangan berani-berani mengalah."""

    # ┌─ ENDING · E-SH-15 · Pion di Papan Orang Lain  [Terdistorsi · host Y/C]
    # │ KAPAN   : Shiori memegang semua rahasia pemain tetapi memilih tidak menghancurkannya
    # │ ISI SKRG: pemain tetap kuliah dan tampak bebas, tetapi setiap langkahnya kini atas izin Shiori; ia tersenyum setiap kali mereka berpapasan
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-15"] = """Shiori tidak menghancurkan hidupmu. Kau tetap kuliah, tetap datang ke tempat biasa, tetap tampak bebas bagi orang yang hanya mengenal permukaan. Syaratnya muncul dalam pesan pendek yang tidak pernah perlu ditulis sebagai ancaman karena kalian sama-sama tahu apa yang disimpan di belakangnya.

Kau mulai meminta izin sebelum membuat keputusan yang dahulu sederhana. Siapa yang ditemui, kapan pergi, bagian mana yang boleh diceritakan: setiap pilihan diperiksa terhadap kemungkinan membuatnya memakai pengetahuan yang kini hanya ditahan.

Setiap kali kalian berpapasan di tangga gedung utama, Shiori selalu menyapamu dengan anggukan sopan yang membuat teman-teman di sekitarmu mengira kalian akrab. Begitu ia lewat, layar ponsel di sakumu menyala menampilkan satu pesan singkat darinya yang mengingatkan jam berapa kau harus sudah pulang malam ini."""

    # ┌─ ENDING · E-SH-16 · Senyum Terakhir  [Buruk · host Y/C]
    # │ KAPAN   : S-D15 umpan berhasil; pemain membuka rahasia terakhirnya padanya
    # │ ISI SKRG: pemain mengira sudah memenangkan hatinya; di M35 Shiori menunjukkan papannya, dan semuanya runtuh dalam satu hari
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-16"] = """Kau mengira Shiori akhirnya menyerahkan kepercayaannya. Ada percakapan pribadi, senyum yang tampak lebih dekat, dan kesempatan menjelaskan rahasia terakhir dengan keyakinan bahwa kedekatan telah membuat kalian berada di pihak yang sama.

Pada hari evaluasi, ia menunjukkan apa yang sebenarnya telah dipahami. Cerita yang kaubawa sebagai kemenangan bertemu bukti dan akibat yang disusun tanpa sepengetahuanmu. Dalam satu hari, hubungan, akses, dan posisi yang dahulu terasa kokoh kehilangan tempat untuk berdiri.

Ketika kau menghampirinya di koridor setelah pengumuman skorsing keluar dan menanyakan apakah semua malam di ruang klub hanyalah jebakan, Shiori hanya memiringkan kepala sambil menutup payungnya. Ia tidak menjawab ya atau tidak, hanya melangkah masuk ke mobil hitam keluarga Saionji dan membiarkan kaca jendelanya naik perlahan."""


    # ═════ Chiasa ═════
    # ┌─ ENDING · E-CH-01 · Rumah Kita Sendiri  [Romantis · host Y]
    # │ KAPAN   : Yutaka mengejar Chiasa; curiga identitas rendah atau diterima
    # │ ISI SKRG: dua orang yang sama-sama kesepian membangun rumah sendiri
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-01"] = """Chiasa memilih tirai untuk rumah yang tak perlu lagi menyesuaikan diri dengan kebiasaan Koita. Yutaka menanyakan warna yang ia sukai, lalu menerima ketika jawabannya berubah setelah melihat cahaya sore. Tidak ada yang menyebut perubahan kecil itu merepotkan.

Mereka sama-sama mengenal kesepian dan belajar agar pengetahuan itu tidak menjadi alasan menahan pasangan dari kehidupan di luar rumah. Chiasa tetap menggambar; Yutaka punya tanggung jawab yang tidak selalu membuatnya bisa pulang cepat. Ada pesan yang dijawab terlambat tanpa langsung menjadi sidang tentang kesetiaan.

Di balik pintu masuk apartemen baru mereka, dua gantungan kunci diletakkan berdampingan di papan kayu kecil. Malam itu Chiasa masih menyalakan lampu meja gambarnya sampai pukul sebelas, sementara Yutaka keluar dari dapur membawa dua cangkir susu hangat dan meletakkan satu di dekat kotak pensilnya."""

    # ┌─ ENDING · E-CH-02 · Diterima  [Koita · host Y]
    # │ KAPAN   : Koita Success NPC; Daisuke dan Yoshie menerima
    # │ ISI SKRG: saudara tiri menjadi pasangan dengan restu keluarga
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-02"] = """Daisuke dan Yoshie menerima hubungan Koita dan Chiasa setelah percakapan yang tidak dapat selesai dalam satu malam. Penerimaan itu tidak menghapus kecanggungan saat panggilan lama terdengar dalam arti baru, tetapi membuat rumah tidak lagi menuntut keduanya berbohong demi dapat duduk bersama.

Chiasa semula menyangka pengakuan Koita akan mengakhiri seluruh takutnya. Ia menemukan masih perlu belajar memberi ruang, tidak memeriksa setiap keterlambatan sebagai kemungkinan ditinggalkan. Koita pun tidak lagi boleh bersembunyi di balik kebiasaan serumah untuk menunda jawaban.

Pada makan malam pertama sesudah pembicaraan panjang itu selesai, Chiasa mengambil piring untuk dirinya sendiri lebih dulu sebelum menyendokkan nasi untuk Koita. Saat tangan mereka bersentuhan di dekat teko teh, Yoshie yang duduk di seberang meja hanya menghela napas pelan lalu meneruskan memotong buah."""

    # ┌─ ENDING · E-CH-03 · Berpisah Baik-baik  [Netral · host Y]
    # │ KAPAN   : Koita Success NPC; keduanya memilih berpisah
    # │ ISI SKRG: tetap keluarga, dengan bekas yang hangat
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-03"] = """Chiasa dan Koita memilih mengakhiri arah romantis yang pernah dicoba. Mereka tidak menamainya kesalahan yang membuat seluruh kedekatan lama kotor. Ada perasaan yang nyata, ada batas dan masa depan yang akhirnya tidak ingin diteruskan bersama.

Kembali menjadi keluarga memerlukan jarak. Chiasa berhenti menyiapkan rutinitas untuk memastikan Koita selalu pulang kepadanya; Koita tidak lagi memakai kelembutan yang ambigu saat merasa sepi. Keduanya perlu menerima kehilangan tanpa meminta yang lain segera bersikap biasa.

Pada Minggu sore beberapa bulan kemudian, mereka kembali duduk di meja makan yang sama untuk mengupas jeruk sambil menonton televisi ruang tengah. Ketika acara selesai, Koita membawa piring kotornya sendiri ke dapur, dan Chiasa naik ke lantai dua sambil melambai singkat dari anak tangga."""

    # ┌─ ENDING · E-CH-04 · Dipisah Paksa  [Buruk · host Y]
    # │ KAPAN   : Koita Success NPC; keluarga menolak keras
    # │ ISI SKRG: Chiasa dipindahkan atau Koita pergi
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-04"] = """Penolakan keluarga berakhir dengan pemisahan tempat tinggal. Koper disiapkan sebelum cukup banyak percakapan berlangsung, membuat Chiasa merasa keputusan tentang tubuh dan jaraknya kembali diambil oleh orang lain.

Koita mungkin yang pergi, mungkin Chiasa yang dipindahkan; rumah yang ditinggalkan keduanya sama-sama kehilangan keseharian yang dahulu terasa aman. Panggilan telepon menjadi pendek, penuh pertanyaan yang harus dijawab hati-hati agar tak membangkitkan pertengkaran berikutnya.

Di kamar kos barunya yang menghadap jalan raya, Chiasa mengeluarkan satu cangkir keramik bergambar kelinci yang terbawa dari lemari dapur rumah Amamiya. Ia meletakkannya di rak paling atas dekat jendela, lalu duduk di tepi kasur yang masih terbungkus plastik sambil menatap layar ponsel yang sunyi."""

    # ┌─ ENDING · E-CH-05 · Digantung Lagi  [Buruk · host Y]
    # │ KAPAN   : Koita Success NPC; Koita kembali ke pola lama
    # │ ISI SKRG: Chiasa menjadi korban terbaru pola Koita
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-05"] = """Koita sempat memberi jawaban yang jelas. Chiasa memegangnya terlalu erat ketika perhatian Koita mulai kembali dibagikan dalam bentuk yang sulit dipertanyakan satu per satu. Ia tahu kalimat menenangkan yang dipakai karena dahulu sering mendengarnya ditujukan kepada orang lain.

Kini ia berada di dalam pola itu. Setiap keberatan disebut terlalu sensitif, setiap janji baru cukup hangat untuk menunda keberanian pergi. Tinggal serumah membuatnya lebih dekat dan sekaligus lebih sulit mengambil jarak.

Pukul sebelas malam, Chiasa kembali memanaskan sup di dapur setiap kali terdengar bunyi langkah kaki di gang depan rumah. Ketika pintu akhirnya terbuka dan Koita masuk sambil tersenyum meminta maaf karena sudah makan di luar bersama teman, Chiasa hanya mematikan kompor dan menuang sup itu kembali ke panci."""

    # ┌─ ENDING · E-CH-06 · Shena Saja  [Netral · host Y]
    # │ KAPAN   : tanpa romansa; Chiasa pindah dan fokus seni
    # │ ISI SKRG: karier ilustrasi berjalan; rumah ditinggalkan
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-06"] = """Chiasa memindahkan meja gambar sebelum tempat tidurnya. Di studio baru, barang pertama yang benar-benar mendapat tempat adalah lampu kerja, bukan foto keluarga atau benda yang mengingatkannya pada Koita.

Karier Shena berjalan. Ia belajar membuat janji profesional yang dapat ditepati tanpa menghabiskan seluruh malam, menerima kritik yang tidak perlu dianggap penolakan terhadap dirinya. Tidak ada hubungan romantis yang dijadikan pusat perpindahan itu.

Pada sampul buku cetakan terbaru yang tiba lewat kurir pagi itu, nama Shena tercetak kecil di sudut bawah ilustrasi. Chiasa merobek kardus pembungkusnya di lantai studio, memajang satu eksemplar di rak dekat jendela, lalu kembali menyalakan tablet gambarnya sebelum kopi di mejanya dingin."""

    # ┌─ ENDING · E-CH-07 · Tersisih Dua Kali  [Buruk · host Y]
    # │ KAPAN   : Rute BL berhasil; Chiasa tidak didekati
    # │ ISI SKRG: patah, menjauh dari keduanya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-07"] = """Hubungan Yutaka dan Koita menjadi nyata ketika Chiasa masih berusaha memahami mengapa tempatnya mendadak terasa berbeda. Ia kehilangan harapan pada Koita sekaligus kemudahan mencari penghiburan pada orang yang kini berada di sisinya.

Ia tidak bisa menuntut cinta sebagai upah karena tumbuh bersama. Mengetahui itu tidak membuat sakitnya menjadi lebih rapi. Untuk beberapa waktu ia menolak undangan yang akan mempertemukan mereka bertiga, memilih diam daripada harus menampilkan dukungan yang belum sanggup dirasakan.

Chiasa berhenti datang ke acara makan malam yang mempertemukan mereka bertiga. Di kamarnya yang hanya diterangi lampu meja, ia menarik garis sketsa baru sampai pukul satu malam, mematikan ponsel sebelum tidur, dan menggantung jadwal kelas minggu depan di atas foto lama mereka yang sudah dibalik menghadap dinding."""

    # ┌─ ENDING · E-CH-08 · Sekutu Paling Setia  [Khusus · host Y]
    # │ KAPAN   : Rute BL; Yutaka jujur pada Chiasa sejak awal
    # │ ISI SKRG: Chiasa menjadi pendukung Yutaka × Koita di depan keluarga
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-08"] = """Yutaka mengatakan perasaannya kepada Chiasa sejak awal, sebelum kedekatan dengan Koita menjadi rahasia yang harus dibongkarnya sendiri. Chiasa terluka dan diberi waktu untuk mengatakannya tanpa langsung dituntut menjadi pendukung yang baik.

Ketika ia akhirnya berdiri di depan keluarga untuk membela hubungan mereka, ia tidak sedang menyerahkan hidupnya agar dua orang lain bahagia. Ia menyebut bahwa Koita harus menjawab sendiri, Yutaka harus bertanggung jawab atas pilihannya, dan keluarga perlu mendengar sebelum menganggap semua telah diputuskan bagi mereka.

Sesudah perdebatan panjang di ruang tamu itu mereda, Chiasa menepuk pundak Yutaka sekali di dekat rak sepatu lalu naik ke kamarnya sendiri. Ia menutup pintu pelan, menyalakan lampu meja gambar, dan memasang penyumbat telinga sambil membuka lembar kanvas baru."""

    # ┌─ ENDING · E-CH-09 · Rumah yang Tidak Aman  [Hancur · host Y]
    # │ KAPAN   : pemain pelaku Force terhadapnya
    # │ ISI SKRG: tinggal serumah dengan Koita; Daisuke dan Yoshie kecewa; tanpa romansa dengan pelaku
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-09"] = """Kekerasanmu membuat Chiasa kehilangan rasa aman pada rumah dan pertemanan yang dahulu dianggap tak perlu dicurigai. Bunyi tamu datang cukup membuatnya berhenti bekerja. Ia marah pada tubuhnya sendiri karena masih takut, lalu perlahan belajar bahwa reaksi itu bukan bukti kelemahan atau kesalahan.

Ia tetap tinggal bersama Koita. Daisuke dan Yoshie pulang dengan kecewa serta amarah yang harus diarahkan kepada pelaku, bukan kepada keputusan Chiasa sesudahnya. Mereka mencari cara mendukung tanpa mengambil alih seluruh pilihannya.

Kunci pintu rumah Amamiya diganti pada pekan berikutnya, dan paket atau surat tanpa nama pengirim langsung ditahan Daisuke di teras depan. Di kamarnya, Chiasa memasang gerendel tambahan dari besi di sebelah gagang kayu, lalu baru bisa menyalakan lampu meja gambarnya setelah memeriksa kunci itu dua kali."""

    # ┌─ ENDING · E-CH-10 · Adik yang Kembali  [Netral · host Y]
    # │ KAPAN   : tidak ada rute romansa dengan Chiasa; keluarga utuh
    # │ ISI SKRG: ia tetap adik Koita dan sahabat Yutaka
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-10"] = """Chiasa tetap menjadi adik Koita dan sahabat Yutaka tanpa hubungan romantis yang harus diberikan agar kedekatan mereka dianggap lengkap. Ia masih suka menggoda, tetapi mulai membedakan keakraban dari hak mengatur siapa yang boleh pulang terlambat.

Keluarga tetap utuh. Ada makan bersama yang tidak lengkap karena jadwal berbeda, ada tugas yang dibagi lebih adil, ada hari ketika Chiasa memilih menggambar daripada mengurus seluruh rumah. Koita belajar menanyakan sebelum mengandalkan kebiasaannya menyediakan.

Dalam foto keluarga terbaru yang diambil di halaman depan sebelum berangkat wisuda, Chiasa berdiri di sisi ibunya sambil memegang map sketsa, tidak lagi mendesak masuk ke sela antara Koita dan Yutaka. Begitu kamera selesai memotret, ia langsung berbalik masuk lebih dulu untuk mengambil jaketnya."""

    # ┌─ ENDING · E-CH-11 · Bukan Piala  [Buruk · host Y]
    # │ KAPAN   : Yutaka merebut Chiasa hanya untuk menyakiti Koita, lalu ketahuan
    # │ ISI SKRG: Chiasa menolak keduanya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-11"] = """Chiasa mengetahui bahwa kedekatan Yutaka dengannya semula dipakai untuk melukai Koita. Ia membaca ulang perhatian yang pernah menenangkan dengan perasaan mual: ada saat ia benar-benar didengar, dan ada saat lukanya hanya menjadi bukti bahwa seseorang telah menang.

Ia menolak Yutaka, lalu menolak berlindung kembali pada Koita hanya karena yang satu sudah membuatnya kecewa. Keduanya tidak diberi kesempatan menjadikan keputusan itu pertarungan lanjutan tentang siapa lebih pantas mendapatkannya.

Chiasa mengemasi kotak cat dan buku sketsanya dari ruang klub sore itu juga, menolak tangan Yutaka maupun Koita yang hendak membawakan tasnya di pintu. Ia menuruni tangga gedung sendirian, dan ketika keduanya memanggil dari lantai atas, ia terus berjalan menembus halaman sampai keluar gerbang."""

    # ┌─ ENDING · E-CF-01 · Rumah Baru  [Romantis · host C]
    # │ KAPAN   : yuri dengan heroine utama; deviasi cukup
    # │ ISI SKRG: hidup bersama heroine; reaksi keluarga Amamiya menentukan nada epilog
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-01"] = """Kau dan perempuan yang memilih bersamamu menata rumah baru dari barang-barang yang tidak selalu cocok. Ada dua kebiasaan minum, dua jadwal, dan pembicaraan tentang ruang yang harus dapat dipakai sendiri tanpa dianggap sedang menjauh.

Reaksi keluarga Amamiya memberi warna pada hari pertama: dukungan dapat membuat kepindahan hangat, keraguan meninggalkan percakapan yang perlu dilanjutkan, penolakan membuat beberapa perayaan terasa kehilangan kursi. Hubungan kalian tidak otomatis menghapus bagian yang sakit itu.

Malam pertama di apartemen itu, kotak kardus masih menumpuk di lorong sempit dekat kamar mandi. Pasanganmu memanggil namamu dari dapur untuk menanyakan letak gunting, dan saat kau menyerahkannya di bawah lampu kuning yang baru dipasang, ia mencium pipimu sekilas sebelum kembali membuka bungkusan piring."""

    # ┌─ ENDING · E-CF-02 · Diterima  [Koita · host C]
    # │ KAPAN   : Koita Success; keluarga menerima
    # │ ISI SKRG: tabu yang direstui
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-02"] = """Keluarga menerima hubunganmu dengan Koita setelah perasaan yang selama ini disembunyikan akhirnya dibicarakan. Daisuke dan Yoshie perlu mendengar pilihan itu lebih dari sekali, memastikan tidak ada yang hanya mengikuti ketakutan kehilangan rumah atau perhatian.

Kau menjalani penerimaan itu dalam tubuh Chiasa, dengan kedekatan masa lalu yang tidak seluruhnya menjadi ingatanmu sendiri. Koita pun mulai mengenal dirimu sekarang sebagai seseorang yang boleh berbeda dari kebiasaan adiknya dahulu.

Panggilan Ko-nii kadang masih terlepas dari mulutmu saat memintanya mengambilkan garam di meja makan, membuat Daisuke terbatuk kecil di balik korannya. Koita tidak lagi pura-pura tidak mendengar; ia menyerahkan botol garam itu ke tanganmu, lalu menuangkan teh ke cangkirmu di depan kedua orang tua kalian."""

    # ┌─ ENDING · E-CF-03 · Berpisah Baik-baik  [Netral · host C]
    # │ KAPAN   : Koita Success; keduanya mundur
    # │ ISI SKRG: kembali menjadi adik tiri
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-03"] = """Kau dan Koita memilih mundur sebelum hubungan itu harus dipertahankan hanya karena sudah terlalu jauh untuk merasa boleh berhenti. Perasaannya tidak disangkal, tetapi tidak lagi dipakai menuntut masa depan yang salah seorang tak ingin jalani.

Kembali menjadi saudara tiri bukan gerakan yang menghapus semua kenangan. Kalian mengubah batas dalam keseharian: mengetuk pintu, bertanya sebelum menyentuh, tidak memakai kesepian sebagai alasan menghidupkan lagi harapan yang telah ditutup.

Pagi itu Koita mengetuk pintu kamarmu dua kali sebelum membukanya sedikit untuk menanyakan apakah kau mau sarapan bersama di bawah. Kau melihat jam meja, mengatakan masih ingin tidur lima belas menit lagi, dan ia mengangguk singkat lalu menutup kembali pintunya rapat-rapat."""

    # ┌─ ENDING · E-CF-04 · Dipisah Paksa  [Buruk · host C]
    # │ KAPAN   : Koita Success; keluarga memisahkan
    # │ ISI SKRG: salah satu meninggalkan rumah
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-04"] = """Keputusan keluarga memisahkan tempat tinggal datang lebih cepat daripada kesempatan menyepakati masa depan. Kau atau Koita harus pergi, dan rumah yang selama ini dapat dihafal lewat bunyinya mendadak menjadi tempat yang harus diingat dari jauh.

Kau menjalani perpindahan dengan barang Chiasa, pertanyaanmu sendiri, dan percakapan yang terputus ketika semua orang terlalu marah untuk mendengar. Kedekatan tidak lenyap hanya karena alamat berubah; justru pada beberapa malam ia terasa lebih sulit karena tak dapat lagi dijalani melalui hal biasa.

Pada malam pertama di kamar sewaan barumu, dua koper pakaian Chiasa masih berdiri belum dibuka di dekat lemari. Kau duduk di lantai beralas karpet tipis, menyantap nasi kotak dari minimarket sendirian sementara bunyi kereta rel layang menggantikan suara televisi ruang tengah rumah Amamiya."""

    # ┌─ ENDING · E-CF-05 · Digantung Lagi  [Buruk · host C]
    # │ KAPAN   : Koita Success; Koita kembali menggantung
    # │ ISI SKRG: pemain merasakan pola Koita dari dalam
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-05"] = """Kau mengenali pola Koita karena telah melihatnya dari luar. Mengenali tidak membuatmu kebal saat pola itu mulai terasa sebagai harapan yang ditujukan kepadamu. Ia dekat, lalu kabur; ia hangat ketika takut kehilangan, lalu kembali samar saat merasa kau aman menunggu.

Kini pengetahuan katalog tak membantu menenangkan tubuh yang menunggu jawaban. Kau dapat menamai setiap penghindaran sambil tetap ingin mempercayai satu kalimat yang menjanjikan semuanya berbeda denganmu.

Pada malam Koita kembali pulang lewat pukul sepuluh tanpa mengabari, kau mendapati dirimu sudah menata dua piring makan malam di meja ruang tengah. Kau berdiri lama menatap piring kedua yang mulai dingin, lalu membungkusnya dengan plastik penutup dan memasukkannya ke kulkas sebelum bunyi kunci terdengar di pintu depan."""

    # ┌─ ENDING · E-CF-06 · Bersama Yutaka  [Koita · host C]
    # │ KAPAN   : Chiasa × Yutaka
    # │ ISI SKRG: hidup bersama Yutaka; lolos evaluasi hanya bila ada deviasi lain (bila tidak, E-SI-06)
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-06"] = """Yutaka mengajakmu membicarakan tempat tinggal sebelum memilih perabot. Ia ingin tahu bagaimana kau hendak bekerja, apa yang harus dibawa, dan apakah dekat kampus masih penting. Sikap hangatnya terasa berbeda saat tidak dipakai menebak jawaban paling mudah untuk semua orang.

Kalian mulai hidup bersama dengan kebiasaan yang perlu dipelajari. Ada saat kau merasa dicintai sebagai Chiasa yang dikenalnya dahulu, lalu perlu mengatakan bahwa keinginanmu kini berbeda. Yutaka belajar mendengar bagian itu tanpa menganggapnya penolakan atas seluruh kenangan.

Di meja dapur, Yutaka sedang merapikan daftar belanja mingguan kalian sambil bersenandung pelan ketika jendela biru Sistem berkedip tipis di sudut pandanganmu. Kau menggenggam jemarinya yang hangat di atas kertas catatan itu, menatap angka evaluasi yang terus berjalan mundur di balik punggungnya."""

    # ┌─ ENDING · E-CF-07 · Nama Pena yang Runtuh  [Buruk · host C]
    # │ KAPAN   : rahasia Shena terbongkar sebagai kebohongan
    # │ ISI SKRG: kontrak Miono diputus; pembaca marah
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-07"] = """Nama Shena runtuh ketika penjelasan tentang karya dan kemampuan yang berubah tidak lagi dapat dipertemukan. Miono meminta jawaban profesional, Karuha memandang garis yang tak sesuai kebohonganmu, dan pembaca bereaksi pada janji yang merasa pernah dibeli bersama buku.

Kontrak diputus. Kau kehilangan akses yang dahulu diwarisi begitu saja, bersama kenyamanan menganggap nama pena akan terus menanggung ketidaksanggupanmu menjadi pemiliknya yang lama.

Di atas meja kerjamu kini hanya ada selembar kertas gambar putih yang tidak lagi boleh dibubuhi tanda tangan Shena. Kau memegang pensil kayu dengan jari yang kaku selama beberapa menit, menarik satu garis lengkung yang miring di tengah halaman, lalu menghapusnya lagi sampai permukaan kertas itu berbulu."""

    # ┌─ ENDING · E-CF-08 · Gaya Baru Shena  [Romantis · host C]
    # │ KAPAN   : pemain belajar menggambar sungguhan sampai layak
    # │ ISI SKRG: Shena kembali dengan gaya baru; Miono dan Karuha menjadi saksi
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-08"] = """Garis barumu tidak persis seperti Chiasa dahulu. Setelah cukup lama belajar, kesamaan itu tidak lagi menjadi satu-satunya ukuran yang dikejar. Kau dapat menjelaskan keputusan gambar, menerima kritik, dan mengulang tanpa harus menyembunyikan seluruh proses di balik alasan sedang lelah.

Miono melihat pekerjaan yang dapat ditepati. Karuha melihat usaha yang tidak lagi hanya berlatih meniru. Ketika Shena kembali menerbitkan karya, pembaca masih memperdebatkan perubahannya, tetapi kali ini ada jawaban yang dapat kauakui sebagai hasil tanganmu sendiri.

Pada malam buku cetakan pertama dengan gaya barumu selesai dijilid, kau memotret lembar sketsa kasar pertamamu di sebelah sampul jadi yang masih berbau tinta. Kau mengirim foto itu ke ponsel Miono dan Karuha, lalu mematikan layar tablet dan tidur nyenyak sampai pagi."""

    # ┌─ ENDING · E-CF-09 · Rumah Amamiya Retak  [Buruk · host C]
    # │ KAPAN   : Koita Success atau kejahatan memecah keluarga
    # │ ISI SKRG: Daisuke dan Yoshie berpisah tempat; rumah sepi
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-09"] = """Rumah Amamiya tak lagi mampu menampung akibat yang dibawa hubungan atau kejahatan di dalamnya. Daisuke dan Yoshie tinggal terpisah, membawa pertanyaan berbeda tentang apa yang seharusnya diketahui lebih dahulu dan keputusan mana yang membuat keluarga kehilangan rasa aman.

Percakapan yang dahulu berakhir dengan siapa mau makan berubah menjadi urusan kapan mengambil barang. Koita dan Chiasa tetap membawa hubungan mereka ke mana pun tinggal, tetapi kenangan serumah tidak lagi cukup untuk mempertemukan semua orang di meja yang sama.

Di rak dekat pintu masuk rumah Amamiya, kini hanya tersisa dua pasang sandal rumah yang jarang bergeser dari tempatnya. Saat kau pulang sore hari dan membuka pintu depan, lampu lorong tetap gelap, dan tak ada lagi aroma masakan atau suara televisi dari ruang tengah."""

    # ┌─ ENDING · E-CF-10 · Studio Sendiri  [Netral · host C]
    # │ KAPAN   : tanpa romansa
    # │ ISI SKRG: mandiri di studio kecil; lolos atau tidaknya bergantung deviasi yang dibuat dengan cara lain
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-10"] = """Studio kecilmu memiliki meja yang hanya cukup untuk satu orang bekerja dengan nyaman. Kau memilihnya karena cahaya, biaya, dan kebebasan menutup pintu pada jam sendiri, bukan karena ada seseorang yang harus dipertahankan di dalamnya.

Tidak ada romansa yang menandai keberangkatan. Kau tetap terhubung dengan beberapa orang, mengambil jarak dari yang lain, dan belajar menjalani nama Chiasa tanpa setiap keputusan harus meniru harapan pemilik hidup sebelumnya.

Menjelang petang di hari sebelum tanggal evaluasi, cahaya matahari miring jatuh tepat di atas meja gambar tunggal di sudut studiomu. Kau menyimpan berkas ilustrasi terakhir, merebus sepanci kecil sup tahu di kompor listrik satu tungku, dan membuka jendela sedikit untuk membiarkan angin sore masuk."""

    # ┌─ ENDING · E-CF-11 · Lingkaran yang Runtuh  [Buruk · host C]
    # │ KAPAN   : beberapa hubungan yuri sekaligus terbongkar
    # │ ISI SKRG: semua pergi bersamaan; lihat E-X-01
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-11"] = """Hubungan-hubungan yang kaubiarkan percaya pada kepastian berbeda akhirnya bertemu. Percakapan yang selama ini dijaga terpisah tidak lagi dapat ditutup dengan penjelasan yang berubah sesuai orang di hadapanmu.

Mereka pergi dengan cara berbeda. Ada yang memintamu mendengar marahnya sampai selesai, ada yang hanya mengirim satu kalimat, ada yang memerlukan teman agar sanggup mengambil barang. Kebersamaan tidak menjadi masalah karena jumlah orang semata, melainkan karena kehendak mereka ditentukan oleh informasi yang sengaja kausimpan.

Menjelang tengah malam, ruang tamu kembali lengang dengan tiga cangkir teh yang ditinggalkan setengah penuh di atas meja. Di layar ponselmu masih tersimpan foto swafoto dari pekan lalu ketika mereka semua tersenyum, tepat di bawah deretan ruang pesan yang kini tak lagi menampilkan foto profil."""

    # ┌─ ENDING · E-CF-12 · Korban yang Ia Ciptakan  [Khusus · host C]
    # │ KAPAN   : jalur manipulasi pembalikan (§14); framing bertahan; nurani_chiasa < 70 sebelum M35
    # │ ISI SKRG: Chiasa tampil sebagai korban, Koita dicap pelaku dan hancur; tanpa romansa; tak bisa diputar balik dan bisa muncul lagi
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-12"] = """Versi yang kaubiarkan dipercaya bertahan sampai evaluasi. Chiasa diperlakukan sebagai orang yang perlu dilindungi, sementara Koita, korban yang sebenarnya, menanggung tuduhan dan keterasingan yang membuatnya kehilangan hampir semua cara meminta didengar.

Kau tidak mendapatkan hubungan romantis dari hasil itu. Ada simpati yang diberikan kepada cerita palsu, ada pintu yang dibuka karena orang mengira sedang menolong, dan semakin banyak percakapan yang harus dijalani tanpa mengakui siapa yang telah kaulukai.

Ketika Koita akhirnya berhenti mencoba menghadangmu di lorong rumah untuk meminta penjelasan, meja makan lantai satu menjadi jauh lebih sunyi. Namun setiap kali ponselmu berdering dengan nomor tak dikenal atau langkah seseorang melambat di belakangmu di koridor kampus, tanganmu refleks menutup layar dan memeriksa siapa yang sedang menatapmu."""

    # ┌─ ENDING · E-CF-13 · Pengakuan yang Tidak Diminta  [Khusus · host C]
    # │ KAPAN   : nurani_chiasa ≥ 70 sebelum M35; framing pernah terpasang lalu dicabut sendiri
    # │ ISI SKRG: ia mengaku sebelum siapa pun membuktikannya; reputasi Koita pulih meski kepercayaan di antara mereka tidak pernah utuh lagi; konsekuensi sosial padanya tetap ada tapi lebih ringan karena kooperatif
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-13"] = """Kau mengaku sebelum orang lain berhasil membuktikan kebohongan tersebut. Pengakuan itu tidak disusun sebagai permintaan agar Koita segera memahami alasanmu. Kau menyebut perbuatan, meluruskan tuduhan, dan menerima bahwa keterangan berikutnya tidak lagi boleh sepenuhnya kaudiktekan.

Nama Koita mulai dibersihkan. Sebagian orang meminta maaf, sebagian menghindar karena malu, dan tidak semua kerusakan dapat dipulihkan oleh berita koreksi. Kepercayaan antara kalian tidak kembali menjadi kehidupan serumah yang lama.

Pada sore ketika Koita akhirnya kembali mengambil buku-bukunya dari rumah ditemani seorang teman, kau tetap berdiri di dekat tangga tanpa menyusulnya ke pintu depan. Ia menutup pintu tanpa menoleh ke arahmu, dan kau kembali ke meja ruang tengah untuk menandatangani sisa berkas keterangan yang harus diserahkan ke kampus esok pagi."""


    # ═════ Yutaka ═════
    # ┌─ ENDING · E-YU-01 · Bersama Chiasa  [Romantis · host C]
    # │ KAPAN   : Yutaka mengaku; Chiasa menerima
    # │ ISI SKRG: aman hanya bila ada deviasi lain (bila tidak, E-SI-06)
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YU-01"] = """Yutaka datang tanpa alasan yang dipinjam dari Koita. Ia membawa kopi untukmu, lalu mengaku sudah memikirkan kalimat pembuka sepanjang perjalanan. Kau mengatakan ia tidak perlu membuat pengakuan kedua. Jawabanmu yang pertama masih berlaku.

Hubungan kalian tumbuh dalam hal kecil: menunggu kelas selesai, bertengkar tentang waktu, mengaku cemburu sebelum candaan menjadi kejam. Ia belajar bahwa mencintai Chiasa tidak memberinya hak menebak seluruh isi kepalamu. Kau belajar menerima perhatian tanpa menjadikannya bukti bahwa kehidupan pinjaman ini sudah sepenuhnya milikmu.

Di depan gerbang rumah Amamiya, Yutaka bertanya pelan apakah ia boleh menggenggam tanganmu sebelum kalian masuk. Kau mengulurkan jari-jarimu ke dalam genggamannya yang hangat, sementara di sudut penglihatanmu, baris hitungan kontrak Sistem masih menyala redup menunggu sisa deviasi yang belum terpenuhi."""

    # ┌─ ENDING · E-YU-02 · Mundur ke Luar Negeri  [Netral · host C]
    # │ KAPAN   : Yutaka mundur demi Koita
    # │ ISI SKRG: magang ke luar negeri untuk melupakan
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YU-02"] = """Yutaka memberitahumu soal magang di luar negeri sesudah berkasnya selesai. Ia tidak menyebut Koita sebagai alasan, tetapi jeda sebelum nama itu cukup panjang. Ia ingin pergi sebelum rasa kecewanya mengubah semua orang yang disayanginya menjadi lawan.

Di bandara, kau menawarkan tetap berkabar. Ia mengangguk dan mengatakan bahwa kadang ia mungkin tidak akan langsung menjawab. Itu bukan hukuman. Ia membutuhkan hidup yang tidak setiap harinya menunggu perubahan perasaanmu.

Foto pertama darinya masuk ke ponselmu tiga minggu kemudian: sepiring roti panggang yang agak gosong, jalan berbatu yang masih basah oleh kabut pagi, dan satu keluhan pendek tentang jam masuk kantornya. Kau menyimpan gambar itu ke galeri, lalu menutup aplikasi pesan tanpa mengetik balasan yang memintanya pulang."""

    # ┌─ ENDING · E-YU-03 · Retak dan Menutup Diri  [Buruk · host C]
    # │ KAPAN   : Chiasa menolak lalu menggantung
    # │ ISI SKRG: apartemen menjadi satu-satunya tempatnya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YU-03"] = """Yutaka berhenti menanyakan kapan kalian bisa bertemu. Pada awalnya kau menganggap ia sibuk. Setelah beberapa undangan tidak dijawab, barulah jelas bahwa candaan yang selalu menyelamatkan suasana telah habis.

Apartemennya tetap terang pada malam hari. Permainan menyala, makanan datang, dan pesan kepada Koita dibiarkan sama lamanya dengan pesanmu. Ia malu karena merasa dipermainkan, lalu marah pada dirinya sendiri karena masih berharap satu pemberitahuan bisa mengubah semuanya.

Di daftar kontak ponselmu, nama Yutaka masih tersemat di urutan teratas panggilan cepat. Namun setiap kali kau melewati gedung apartemennya saat pulang kuliah, tirai jendela lantai tiga itu selalu tertutup rapat, dan pesan ucapan selamat tahun baru yang kauikirim tetap berhenti pada satu tanda centang tanpa pernah dibaca."""

    # ┌─ ENDING · E-YU-04 · Sekutu Chiasa  [Khusus · host C]
    # │ KAPAN   : Chiasa jujur padanya
    # │ ISI SKRG: Yutaka membantu Chiasa di rute heroine atau Koita Success
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YU-04"] = """Kau menceritakan cukup banyak kebenaran hingga Yutaka berhenti mengira semua persoalanmu dapat diselesaikan dengan mengajak keluar. Ia bertanya apa yang kaubutuhkan, kemudian membedakannya dari apa yang sanggup ia lakukan.

Ia membantumu menghadapi percakapan sulit, tetap mengingatkan ketika kau mulai membenarkan perlakuan buruk kepada orang lain. Menjadi sekutu tidak berarti setuju pada setiap rencana. Kadang dukungan terpentingnya adalah menolak membiarkanmu memakai rasa takut sebagai alasan untuk melukai Koita.

Pada sore sesudah pertemuan yang menguras tenaga itu berakhir, Yutaka sudah duduk menunggumu di bangku dekat mesin penjual otomatis dengan dua kaleng teh hangat. Ia melemparkan satu kaleng ke tanganmu, menggeser tasnya agar kau bisa duduk, dan tidak menanyakan sepatah kata pun sampai kau sendiri yang membuka suara."""

    # ┌─ ENDING · E-YU-05 · Tahu Dipakai  [Buruk · host C]
    # │ KAPAN   : Chiasa memperalat Yutaka dan ia mengetahuinya
    # │ ISI SKRG: patah; memutus Chiasa dan Koita sekaligus
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YU-05"] = """Yutaka membaca kembali percakapan kalian dan akhirnya melihat pola yang selama ini ditolak pikirannya sendiri. Kau datang ketika butuh sesuatu, mendekat ketika ia mulai mundur, lalu menyebutnya salah paham saat ia berharap lebih.

Ia meminta satu pertemuan untuk mengakhiri semuanya. Ketika kau mencoba mengingatkan kenangan masa kecil, ia mengatakan kenangan itu justru alasan perbuatanmu begitu menyakitkan. Koita juga kehilangan tempat di sisinya, terseret ke dalam hubungan yang sudah terlalu penuh rahasia untuk dipisahkan dengan bersih.

Sesudah pertemuan di kafe dekat stasiun itu, Yutaka tidak pernah lagi membalas pesan maupun mengangkat telepon dari rumah Amamiya. Di ruang tamu kalian, bantalan kursi pojok yang biasa ia pakai bersandar saat bermain gim tetap rapi di tempatnya, dan tak seorang pun berani memindahkannya selama berbulan-bulan."""

    # ┌─ ENDING · E-YU-06 · Membela Koita  [Netral · host C]
    # │ KAPAN   : Yutaka melihat Chiasa menyakiti Koita
    # │ ISI SKRG: berpihak pada Koita; menjadi lawan sosial Chiasa
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YU-06"] = """Yutaka berdiri di sebelah Koita ketika kau datang. Ia tidak meninggikan suara. Ia mengatakan tahu cukup banyak untuk berhenti membiarkan kedekatan denganmu menentukan apa yang akan ia abaikan.

Koita tampak malu membutuhkan pembelaan. Yutaka memberinya waktu, mendengarkan, dan mengingatkan teman-teman lain agar tidak memperlakukan luka itu sebagai gosip. Terhadapmu ia menjaga jarak yang jelas. Perasaan yang dulu dimilikinya tidak lagi dapat kaupanggil sebagai alasan agar ia berpihak.

Kalian masih sesekali berpapasan di pelataran gedung fakultas saat pergantian jam kuliah. Yutaka hanya membalas anggukanmu dengan wajah datar sambil tetap berjalan di sisi kiri Koita, memastikan pundaknya sendiri menghalangi jalurmu setiap kali kau hendak mendekat."""

    # ┌─ ENDING · E-YU-07 · Pewaris Kisaragi  [Buruk · host C]
    # │ KAPAN   : keluarga menekan di M31; Chiasa tidak hadir
    # │ ISI SKRG: menjadi sedingin orang tuanya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YU-07"] = """Nama Yutaka mulai muncul dalam percakapan bisnis keluarga. Ia belajar hadir tepat waktu, menjawab seperlunya, dan tidak mengatakan bahwa ia ingin pulang ke tempat lain. Ketidakhadiranmu pada saat ia membutuhkan seseorang ikut menjadi bagian dari kebiasaan barunya berhenti meminta.

Koita beberapa kali mengajaknya makan. Yutaka selalu punya alasan yang masuk akal. Di foto acara perusahaan, ia tersenyum dengan ketepatan yang dulu dipakai untuk menggoda teman. Sekarang tidak ada yang tahu kapan senyum itu berakhir setelah kamera diturunkan.

Di acara jamuan akhir tahun perusahaan Kisaragi, wajah Yutaka muncul di halaman buletin bisnis dengan jas gelap dan senyum tipis yang rapi. Di laci meja nakas apartemennya, jam tangan pemberian Daisuke dari masa SMA tetap tersimpan di dalam kotak beludru, berhenti berdetak sejak baterainya habis bulan lalu."""

    # ┌─ ENDING · E-YU-08 · Sahabat Lagi  [Netral · host C]
    # │ KAPAN   : Chiasa menolak dengan jujur dan konsisten
    # │ ISI SKRG: geng masa kecil tetap utuh
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YU-08"] = """Penolakanmu tidak langsung membuat Yutaka lega. Ia membutuhkan waktu untuk berhenti membaca kehangatan sebagai janji yang mungkin berubah. Kau memberinya waktu itu, tidak memanggilnya kembali hanya karena rindu diperhatikan.

Ketika ia akhirnya datang lagi ke rumah Amamiya, percakapan sempat canggung. Nagisa membuat gurauan buruk, Koita salah mengambil gelas, dan Chiasa tertawa sebelum tahu harus berkata apa. Tidak ada yang memaksa keakraban kembali dalam satu malam.

Bulan-bulan berikutnya, Yutaka kembali datang membawa kantong camilan setiap kali kalian berempat berkumpul menonton film di ruang tengah rumah Amamiya. Saat Chiasa bangun untuk mengambil minum ke dapur, Yutaka tetap duduk bersila di karpet sambil berebut remot dengan Nagisa tanpa lagi menyusulnya ke belakang."""

    # ┌─ ENDING · E-YH-01 · Pewaris yang Berbeda  [Netral · host Y]
    # │ KAPAN   : Y17-A; keluarga berdamai
    # │ ISI SKRG: mengambil perusahaan keluarga dengan cara sendiri, tidak sedingin orang tuanya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YH-01"] = """Kau menerima pekerjaan di perusahaan keluarga sesudah menjelaskan apa yang ingin dipelajari dan batas yang tidak mau kaulampaui. Kenji tidak menyetujui semuanya. Untuk pertama kalinya, perbedaan itu tidak harus mengakhiri percakapan.

Hari-hari pertama tidak menyerupai kedudukan seorang pangeran. Ada laporan yang salah, karyawan yang lebih mengerti pekerjaan, dan rasa malu ketika nama keluarga mendahului kemampuanmu. Kau mulai datang untuk mendengar sebelum meminta dipercaya.

Di sela tumpukan berkas magang sore itu, kau mengangkat telepon meja dan menghubungi nomor rumah hanya untuk menanyakan apakah ibumu sudah makan malam. Setelah hening tiga detik di ujung sambungan, suara ibumu menjawab pelan dan mulai menceritakan bunga kamelia di halaman belakang yang baru saja mekar."""

    # ┌─ ENDING · E-YH-02 · Bekerja di Luar  [Netral · host Y]
    # │ KAPAN   : Y17-B
    # │ ISI SKRG: lepas dari keluarga Kisaragi; hidup dengan gaji sendiri
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YH-02"] = """Gaji pertamamu masuk dengan angka yang terasa kecil dibanding uang yang dulu datang tanpa ditanya. Kau memeriksanya lama, lalu menertawakan rasa bangga yang sulit dijelaskan. Tidak ada bagian dari pekerjaan bulan ini yang dikerjakan oleh reputasi Yutaka semata.

Kau belajar menyesuaikan pengeluaran dan menerima pekerjaan yang tidak selalu menyenangkan. Orang tua Kisaragi belum sepenuhnya memahami pilihan itu. Mereka kini harus bertanya bagaimana harimu jika ingin tahu, sebab hidupmu tidak lagi dapat dibaca dari rekening yang mereka isi.

Pada Sabtu sore setelah gajian pertama itu cair, kau membeli dua porsi daging panggang di kedai kecil dekat stasiun dan mentraktir seorang teman dengan uang tunai dari dompetmu sendiri. Saat keluar dari kedai, kau melipat struk pembayarannya rapi-rapi dan menyimpannya di saku kemeja."""

    # ┌─ ENDING · E-YH-03 · Keluarga Pilihan  [Romantis · host Y]
    # │ KAPAN   : hubungan dengan keluarga Amamiya tinggi; tanpa kejahatan
    # │ ISI SKRG: Daisuke dan Yoshie memperlakukannya sebagai anak sendiri
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YH-03"] = """Yoshie tidak mengumumkan bahwa kau menjadi bagian keluarga. Ia hanya mulai menghitung porsi makan dengan menyertakanmu dan mengingatkan agar mengabarinya kalau pulang terlambat. Daisuke menanyakan pekerjaanmu seperti ia menanyakan pekerjaan Koita: cukup serius untuk percaya kau dapat menjawab.

Kau tetap harus mengetuk atau mengabari sebelum datang. Kedekatan tidak berubah menjadi hak memasuki setiap ruang. Di rumah itu, batas yang sederhana justru membuat penerimaan terasa aman; kau tidak perlu membuktikan keakraban dengan melanggarnya.

Suatu malam selepas makan bersama, Yoshie membungkuskan sisa kari hangat ke dalam kotak plastik dan menyuruhmu membawanya pulang untuk sarapan besok. Kau berdiri di bawah lampu teras rumah Amamiya sambil mendekap bungkusan yang masih mengepul itu, lalu melambai sampai Daisuke mengunci pintu depan."""

    # ┌─ ENDING · E-YH-04 · Dicoret  [Buruk · host Y]
    # │ KAPAN   : membangkang keluarga berulang atau skandal besar
    # │ ISI SKRG: uang saku berhenti; apartemen dilepas; mulai dari nol
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YH-04"] = """Pemberitahuan terakhir dari keluarga berisi keputusan yang tidak lagi terdengar seperti ancaman. Uang saku dihentikan, apartemen harus dilepas, dan biaya yang selama ini tak pernah kaupikirkan kini muncul satu per satu.

Kau berkemas di ruangan yang pernah terasa terlalu luas. Ada barang yang dijual, ada yang ternyata tidak berarti tanpa tempat untuk menyimpannya. Perselisihan atau skandal yang membawa kalian ke sini tidak menghilang bersama alamat lama. Jika ada orang yang kaulukai, kesulitanmu bukan pengganti pertanggungjawaban kepada mereka.

Malam pertama di kamar kos sempit dekat jalur kereta barang, kau duduk di bawah lampu neon yang berdengung sambil menghitung sisa lembaran uang di atas kardus pindahan. Setelah mencatat jadwal wawancara kerja paruh waktu untuk besok pagi, kau mematikan lampu dan menarik selimut tipis sampai ke dagu."""

    # ┌─ ENDING · E-YH-05 · Ketahuan Bukan Yutaka  [Khusus · host Y]
    # │ KAPAN   : minimal dua orang dekat yakin ia bukan Yutaka
    # │ ISI SKRG: diterima sebagai "Yutaka yang baru", atau dijauhi
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YH-05"] = """Mereka berhenti menyebut perubahanmu sekadar fase. Dua orang yang mengenal Yutaka dari dekat akhirnya mengatakan hal yang sama: ada seseorang yang hilang dari wajah yang sedang mereka pandang.

Kau tidak punya cara mengembalikan kesadaran yang dahulu tinggal di sini. Pengakuan itu tidak membuat kehilangan mereka lebih mudah diterima. Ada yang masih menghubungimu untuk mengenal orang yang kini hadir; ada yang memerlukan jarak setiap kali mendengar suaramu.

Pada hari ulang tahun Yutaka bulan berikutnya, Koita dan Chiasa tetap datang ke apartemen membawa kue kecil tanpa lilin. Mereka duduk makan bersamamu di meja rendah, sesekali tertawa mendengar ceritamu, lalu sama-sama terdiam menatap foto masa SMP di dinding sebelum berpamitan pulang."""

    # ┌─ ENDING · E-YH-06 · Pergi Jauh  [Netral · host Y]
    # │ KAPAN   : Y17-C magang luar negeri
    # │ ISI SKRG: meninggalkan kota; quest Sistem tetap berjalan dari jauh
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YH-06"] = """Di kota lain, kau belajar berangkat kerja dengan rute yang belum hafal. Magang membuat harimu penuh nama baru dan kesalahan yang tidak ada hubungannya dengan Koita. Untuk beberapa jam, hidup terasa milik seorang pemuda biasa yang sedang mencoba bekerja dengan baik.

Lalu pesan dari Kouseikan datang. Perbedaan waktu mengubah percakapan menjadi balasan yang saling menunggu. Kontrak tetap bergerak bersama kalender di sana, dan jarak tidak membuatmu berhenti memikirkan akibat keputusan yang sudah kaubuat.

Dari jendela kamar sewaan di lantai empat, kau menatap trem malam yang melintas di jalan basah kota asing yang tak pernah digambar di halaman manga mana pun. Di sudut meja belajar, layar laptopmu masih menampilkan hitung mundur kalender Kouseikan, sementara kau menutup tirai dan menyeduh kopi untuk giliran kerja pagi."""

    # ┌─ ENDING · E-YH-07 · Informan yang Menagih  [Buruk · host Y]
    # │ KAPAN   : daichi_status penagih
    # │ ISI SKRG: Kaichi memeras pemain dengan semua yang ia tahu
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YH-07"] = """Kaichi tidak lagi mengajak makan dengan nada bercanda. Ia menyebut hal yang diketahuinya, lalu kebutuhan yang katanya mendesak. Kau mengerti hubungan itu telah berubah sebelum jumlah uang diucapkan.

Setiap permintaan membuatmu mengira pembayaran berikut akan menjadi yang terakhir. Setelahnya, kau tetap memeriksa ponsel dengan cemas. Rahasia yang dipakai untuk merugikan orang lain kini juga mengatur kapan kau dapat tidur tenang.

Setiap tanggal dua puluh lima malam, layar ponselmu menyala menampilkan nomor rekening dan nominal singkat dari Kaichi tanpa sapaan pembuka. Kau mentransfer angka itu dari tepi tempat tidur dengan tangan dingin, lalu menghapus riwayat transaksi sebelum memejamkan mata yang tak kunjung bisa terlelap."""


    # ═════ Lintas / NPC / Harem ═════
    # ┌─ ENDING · E-X-01 · Harem yang Runtuh  [Buruk · host Y/C]
    # │ KAPAN   : beberapa hubungan rahasia terbongkar sekaligus di M23 atau M35
    # │ ISI SKRG: semua pergi di hari yang sama
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-01"] = """Mereka datang dengan pertanyaan berbeda dan pulang dengan alasan yang sama. Janji yang kauucapkan kepada satu orang ternyata pernah diberikan kepada yang lain, dengan kata yang hampir tidak berubah. Percakapan hari itu tidak memberimu cukup waktu untuk menyelamatkan semua versi dirimu.

Ada yang marah keras, ada yang terlalu tenang. Salah seorang meminta barangnya dikembalikan melalui teman. Yang lain hanya menghapus rencana minggu depan. Tak satu pun bersedia menenangkanmu karena kau kini takut kehilangan mereka.

Menjelang malam, ruang tamumu kosong dan kunci cadangan yang pernah kaupinjamkan sudah diletakkan berjajar di atas meja kopi. Di layar ponselmu, tiga ruang obrolan yang kemarin masih penuh pesan selamat malam kini hanya menyisakan pemberitahuan bahwa kontak tidak lagi menerima pesan."""

    # ┌─ ENDING · E-X-02 · Meja Panjang  [Romantis · host Y/C]
    # │ KAPAN   : hubungan terbuka yang disepakati semua pihak
    # │ ISI SKRG: makan malam panjang yang canggung, tapi jujur
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-02"] = """Meja itu memang terlalu panjang untuk dapur yang tersedia. Kursi tambahan berbeda warna, makanan tidak selesai pada waktu yang sama, dan percakapan pertama lebih canggung daripada yang kalian bayangkan. Tak seorang pun bisa memakai istilah hubungan terbuka untuk menggantikan pembicaraan yang belum selesai.

Kalian membahas waktu, kecemburuan, privasi, dan hak untuk berubah pikiran. Ada kesepakatan yang harus diperbaiki setelah ternyata menyakiti seseorang. Tidak ada orang yang diminta bertahan agar kalian terlihat berhasil di depan orang lain.

Malam itu seseorang meminta mangkuk lauk diteruskan ke ujung meja dan tawa akhirnya pecah karena dua orang meraih sendok sayur bersamaan. Sebelum pulang, kalender dinding di dapur sudah ditempeli catatan warna-warni untuk jadwal minggu depan."""

    # ┌─ ENDING · E-X-03 · Domino Shiori  [Buruk · host Y/C]
    # │ KAPAN   : Shiori tahap 5 dengan daftar_kebohongan panjang
    # │ ISI SKRG: semua rahasia terbuka dan setiap rute ikut runtuh
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-03"] = """Shiori tidak memulai dengan pidato. Ia mempertemukan orang-orang yang selama ini mendengar versi berbeda dan membiarkan pertanyaan mereka menemukan jawaban yang tidak kausukai. Yang runtuh lebih dahulu adalah keyakinan bahwa setiap rahasia masih terpisah dari yang lain.

Hubungan-hubunganmu berubah dalam hitungan hari. Ada percakapan yang tidak lagi bisa dibatasi dengan meminta orang menjaga privasi, sebab permintaan itu sudah terlalu sering dipakai untuk melindungimu. Mereka perlu bicara agar memahami apa yang terjadi kepada diri masing-masing.

Ketika semuanya selesai dibentangkan di ruang klub sore itu, Shiori menutup mapnya tanpa senyum dan keluar paling dulu, disusul satu per satu orang yang dulu pernah menunggu pesanmu sampai tak seorang pun tersisa di ruangan selain dirimu."""

    # ┌─ ENDING · E-X-04 · Musim Dingin Tanpa Moeka  [Buruk · host Y/C]
    # │ KAPAN   : E-MO-04
    # │ ISI SKRG: semua epilog berubah menjadi versi duka
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-04"] = """Musim dingin datang sesudah kematian Moeka dan membuat tempat-tempat biasa terasa salah. Konbini tetap buka. Kelas tetap dimulai. Ryena berhenti pada rak barang yang pernah mereka komentari bersama, lalu berjalan lagi tanpa membeli apa pun.

Di antara teman-teman, ada yang ingin terus membicarakannya dan ada yang tidak sanggup mendengar nama itu setiap hari. Perbedaan cara berduka sempat membuat mereka saling menyakiti. Tidak satu pun memiliki kalimat yang cukup baik untuk menutup pertanyaan tentang malam terakhirnya.

Pada acara kumpul akhir tahun, satu kursi di dekat jendela tetap dibiarkan tanpa piring sementara syal rajut lama milik Moeka masih tersangkut di gantungan ruang studio desain."""

    # ┌─ ENDING · E-X-05 · Kursi Kosong di Wisuda  [Khusus · host Y/C]
    # │ KAPAN   : semua heroine lepas dari Koita
    # │ ISI SKRG: Koita sendirian di wisuda; deviasi sangat tinggi
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-05"] = """Di wisuda, Koita berdiri sendirian setelah namanya dipanggil. Para perempuan yang dulu selalu digambarkan berada di sekelilingnya kini mempunyai tujuan sendiri. Tidak ada pertemuan terakhir yang membawa mereka kembali kepadanya hanya karena hari ini terasa pantas untuk sebuah akhir.

Ia membantu seorang teman mengambil foto, lalu memeriksa pesan di ponselnya. Ada ucapan selamat, ada urusan pekerjaan. Kursi yang kosong di dekatnya tidak otomatis berarti hidupnya sudah habis, meskipun kau tahu betapa jauh semua ini menyimpang dari kisah yang pernah kaubaca.

Kau memandangnya dari sela kerumunan sementara angka deviasi di sudut matamu melonjak melewati batas tertinggi. Koita memasukkan ponsel ke saku jasnya, merapikan tabung ijazahnya, dan berjalan keluar lewat pintu samping aula sendirian."""

    # ┌─ ENDING · E-X-06 · Semua Orang Bebas  [Romantis · host Y/C]
    # │ KAPAN   : semua heroine pulih dan mandiri; tidak ada yang bersama Koita atau pemain
    # │ ISI SKRG: lingkaran yang bubar dengan sehat (sering bersama E-SI-12)
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-06"] = """Mereka tidak berkumpul untuk memilih seseorang. Pertemuan terakhir sebelum jadwal semua orang berpisah dipenuhi cerita kerja, pendidikan, tempat tinggal, dan hal yang ingin dicoba tanpa perlu meminta restu seorang pasangan.

Beberapa hubungan pernah terasa hampir romantis. Ada yang berakhir dengan sedih, ada yang berubah menjadi persahabatan yang lebih tenang. Koita mendengar mereka tanpa mengira semua rencana itu diam-diam masih menunggunya. Kau juga tidak meminta hasil dari bantuan yang pernah kauberikan.

Setelah makan malam di kedai dekat stasiun selesai dan tagihan dibagi rata di meja kasir, kalian berpamitan di bawah lampu penyeberangan lalu berpencar menuju peron dan arah kereta masing-masing."""

    # ┌─ ENDING · E-X-07 · Melawan Naskah Bersama  [Khusus · host Y/C]
    # │ KAPAN   : E-KO-13 dan persahabatan atau Rute BL
    # │ ISI SKRG: Koita dan pemain sama-sama sadar naskah dan melawannya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-07"] = """Koita meletakkan catatannya di antara kalian. Ia tidak lagi bertanya apakah semua kebetulan dalam hidupnya wajar. Ia bertanya bagian mana yang masih dapat dipilih ketika kisah seolah terus mendorongnya menuju jawaban yang sama.

Kau menceritakan yang kautahu tanpa mengaku menguasai seluruh aturan. Ada hal yang membuatnya marah kepadamu, dan kalian tidak menyelesaikannya dengan memanggil diri sendiri korban keadaan. Melawan naskah bersama menuntutmu mengakui kapan kau sendiri pernah memanfaatkan naskah itu.

Keesokan paginya kalian sengaja melewati rute jalan yang berlawanan dari jadwal pertemuan di buku catatan itu. Di depan mesin penjual minuman dekat gedung olahraga, Koita melemparkan satu kaleng kopi hangat ke tanganmu, lalu tersenyum dan menanyakan langkah kalian berikutnya."""

    # ┌─ ENDING · E-X-08 · Pengakuan di Depan Semua  [Khusus · host Y/C]
    # │ KAPAN   : pemain membuka Sistem kepada seluruh lingkaran di M35
    # │ ISI SKRG: setiap orang bereaksi sesuai sejarahnya dengan pemain
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-08"] = """Kau mengumpulkan mereka dan mengatakan ada Sistem yang menempatkan keselamatanmu di atas penyimpangan hidup Koita. Kalimat itu terdengar mengerikan ketika akhirnya diucapkan dengan suara yang dapat didengar orang lain.

Harumi meminta rincian yang dapat diperiksa. Shiori menanyakan apa yang selama ini kausengaja. Miyuki memikirkan siapa yang sedang terancam; Nagisa marah karena perasaannya pernah diperlakukan sebagai bagian perhitungan. Orang-orang lain membawa luka dan pertanyaannya sendiri. Tidak ada jawaban bersama yang membuat pengakuan itu mudah.

Malam itu dua orang memilih langsung mengambil tas dan meninggalkan ruangan, sementara tiga lainnya masih tetap duduk di meja dengan wajah tegang dan meminta kau menceritakan semuanya dari hari pertama kontrak itu muncul."""

    # ┌─ ENDING · E-X-09 · Dua Tragedi  [Buruk · host Y/C]
    # │ KAPAN   : dua rute distorsi berakhir Bad dan saling memicu
    # │ ISI SKRG: dua kehilangan dalam satu musim
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-09"] = """Dua kehilangan datang dalam musim yang sama. Belum selesai orang memahami yang pertama, kabar berikutnya memaksa mereka berkumpul lagi dengan wajah yang tidak lagi tahu bagaimana menunjukkan terkejut.

Mereka mengingat percakapan yang terlewat, pertolongan yang tidak datang, dan luka yang saling membuat keadaan lebih buruk. Tidak semua dugaan dapat dibuktikan, tidak semua penyesalan berarti seseorang memiliki kuasa mencegah segalanya. Tetapi pilihan yang disengaja tetap harus disebut dengan namanya, terutama jika seseorang telah mengambil untung dari kerentanan orang lain.

Sesudah musim dingin berakhir, ruang klub dan meja kantin yang biasa ditempati kelompok itu tak pernah lagi terisi penuh. Dua loker di koridor gedung fakultas dikosongkan pihak kampus pada pekan yang sama, menyisakan pita penanda putih di gagang besinya."""

    # ┌─ ENDING · E-X-10 · Kota yang Tahu Semuanya  [Buruk · host Y/C]
    # │ KAPAN   : Meisa menerbitkan semuanya
    # │ ISI SKRG: reputasi semua orang yang terlibat hancur
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-10"] = """Tulisan Meisa tersebar melampaui orang yang mula-mula ingin membaca gosip kampus. Nama, hubungan, dan pengakuan pribadi menjadi bahan komentar orang yang tidak mengenal satu pun wajah di baliknya.

Kebenaran tentang perbuatanmu perlu diketahui mereka yang dirugikan. Namun bagian kehidupan orang lain yang ikut diumbar membuat luka baru. Ada korban yang harus menjelaskan dirinya berkali-kali, teman yang diseret hanya karena pernah terlihat bersama, dan keluarga yang mengetahui semuanya dari orang asing.

Bahkan di kedai kopi luar stasiun yang berjarak tiga pemberhentian dari Kouseikan, dua penumpang kereta di meja sebelah masih berbisik sambil memperlihatkan tangkapan layar artikel itu ketika kau masuk mencari kursi."""

    # ┌─ ENDING · E-X-11 · Pesta di Rumah Amamiya  [Romantis · host Y/C]
    # │ KAPAN   : semua pulih; Koita memilih dengan tulus; pemain bersama seseorang; geng masa kecil utuh
    # │ ISI SKRG: akhir paling bahagia, tetapi bukan True Ending
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-11"] = """Pesta di rumah Amamiya terlambat dimulai karena seseorang salah menghitung jumlah piring. Koita menertawakan dirinya sendiri sebelum orang lain sempat menyalahkan. Di sebelahnya, orang yang ia pilih menepuk lengannya dan meminta ia membantu, bukan berdiri memberi alasan.

Teman-teman datang dengan kehidupan yang tidak lagi bergantung pada satu pusat. Ada cerita pemulihan yang masih berjalan, pekerjaan baru, dan kecanggungan lama yang akhirnya bisa disebut tanpa membuat semua orang berhenti makan. Pasanganmu duduk dekat, cukup akrab untuk tahu kapan kau perlu diam sejenak.

Daisuke mengambil foto tanpa menyuruh semua orang berpose sempurna. Hasilnya miring dan beberapa wajah sedang berbicara. Kau menyukainya justru karena itu. Tidak ada rahasia besar yang harus dijaga agar malam ini tetap hangat; orang-orang di dalam foto memilih berada di sini."""

    # ┌─ ENDING · E-X-12 · Dua Ratu  [Buruk · host Y/C]
    # │ KAPAN   : Shiori Rute Revenge dan Nagisa Rute Yandere sama-sama menargetkan pemain
    # │ ISI SKRG: dua orang yang tadinya tidak akrab bersekutu melawan pemain
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-12"] = """Shiori dan Nagisa dahulu tidak akan memilih duduk berdua jika masih ada pilihan lain. Kini mereka mempunyai sasaran yang sama: kau, dan hal yang telah kaulakukan kepada mereka.

Shiori membawa kemarahan yang disusun menjadi keputusan. Nagisa membawa ketakutan kehilangan yang berubah menjadi tuntutan untuk menguasai. Mereka saling menguatkan pada bagian yang paling sulit dihentikan, sementara orang-orang di sekitar mulai takut berbicara karena semua percakapan terasa dapat dianggap sebagai keberpihakan.

Saat kau keluar dari ruang kelas sore itu, Nagisa sudah berdiri menunggu di ujung tangga timur sementara Shiori menutup jalan di depan pintu perpustakaan barat sambil memegang ponsel yang mencatat setiap menit kepergianmu."""

    # ┌─ ENDING · E-X-13 · Tubuh yang Dibayar  [Khusus · host Y/C]
    # │ KAPAN   : pemain menyelamatkan minimal tiga heroine dari rute distorsi sambil terus memaksa tubuh
    # │ ISI SKRG: semua selamat, tubuh pemain yang membayar (dekat E-SI-07)
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-13"] = """Mereka selamat melewati masa terburuk, tetapi kau datang ke pertemuan berikutnya dengan tubuh yang tidak lagi sanggup mengikuti keinginanmu. Tanganmu cepat lelah, percakapan terputus karena kau perlu duduk, dan jadwal yang dulu kaujejalkan mulai kosong atas permintaan orang lain.

Untuk sekali ini, mereka datang menolongmu tanpa menanyakan apakah bantuan itu cukup berguna untuk dihitung. Kau harus belajar menerima makanan, istirahat, dan pendampingan tanpa mengubahnya menjadi utang yang akan segera kaubayar.

Pada sore hari wisuda, mereka bergantian duduk di sekitar ranjang ruang istirahat klinik kampus sambil membawa termos bubur hangat dan bunga sakura dari halaman luar agar kau tidak perlu memaksakan diri berdiri di aula."""

    # ┌─ ENDING · E-X-14 · Dalang yang Tak Pernah Dicurigai  [Khusus · host Y/C]
    # │ KAPAN   : force_bersih[[x] bertahan untuk setiap korban Force; NTR sempurna tercapai (07_Koita_dan_BL.md §14, 09_Force_dan_Kriminal.md §10)
    # │ ISI SKRG: tidak ada yang pernah tahu apa yang sebenarnya terjadi; pemain lolos evaluasi dengan deviasi tertinggi yang mungkin, dan dunia tidak pernah mengejarnya. Sistem NTR tetap mencatat semuanya diam-diam
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-14"] = """Tidak ada tuduhan yang mencapai dirimu. Di hadapan kampus, kau tetap seseorang dengan sejarah yang tampak masuk akal. Orang-orang yang telah kaulukai membawa akibat kekerasan itu dalam kehidupan yang tidak disaksikan orang yang memujimu.

Ada yang semakin takut keluar, ada yang tidak sanggup menjelaskan perubahan dirinya, ada yang bertahan dengan bantuan kecil yang tidak pernah kauberikan. Ketidaktahuan dunia membuat mereka lebih sendirian. Itu tidak mengubah kekerasan menjadi hubungan, atau ketakutan mereka menjadi persetujuan.

Di atas panggung wisuda, kau menerima map ijazah sambil disambut tepuk tangan hadirin sementara jendela Sistem mencatat angka deviasi tertinggi di sudut matamu. Dari barisan kursi belakang yang gelap, dua bangku kosong milik mereka yang tak sanggup hadir tetap menganga sampai aula dibubarkan."""

    # ┌─ ENDING · E-NPC-01 · Dua Jas Putih  [Romantis · host Y/C]
    # │ KAPAN   : romansa tulus dengan Yuina; Miyuki tidak disakiti
    # │ ISI SKRG: dua calon dokter yang saling menjaga jam tidur
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-01"] = """Di ruang istirahat, dua jas putih tergantung bersebelahan: milik Yuina dan Miyuki. Kau datang membawa makanan setelah memastikan mereka memang bisa berhenti sebentar. Yuina membuka bungkusnya dan langsung menanyakan apakah kau sendiri sudah makan.

Hubungan kalian tidak membuatnya meninggalkan persahabatan atau cita-citanya. Ia tetap blak-blakan, tidak memuji pengorbanan yang sebenarnya hanya menyembunyikan kebiasaan buruk mengabaikan diri. Kau belajar menerima bahwa perhatian kadang terdengar seperti teguran yang sangat tepat.

Miyuki pulang lebih dahulu malam itu. Yuina duduk di sampingmu di bangku panjang koridor, menyandarkan kepalanya ke bahumu sambil memejamkan mata, dan kau memasang alarm lima belas menit di ponselmu sebelum giliran jaganya dimulai lagi."""

    # ┌─ ENDING · E-NPC-02 · Sahabat yang Memilih Sisi  [Buruk · host Y/C]
    # │ KAPAN   : pemain menyakiti Miyuki sambil mendekati Yuina
    # │ ISI SKRG: Yuina memilih Miyuki dan menutup pintu
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-02"] = """Yuina memintamu berhenti menemui Miyuki dengan janji yang terus membuatnya terluka. Ketika kau berusaha mengalihkan percakapan kepada kedekatan kalian sendiri, wajah Yuina mengeras.

Ia tidak bersedia menjadikan perhatianmu kepadanya sebagai pengganti pertanggungjawaban kepada sahabatnya. Pesanmu dijawab hanya jika ada urusan yang memang perlu diselesaikan. Setiap usaha menyebut Miyuki terlalu sensitif membuat jarak itu semakin jelas.

Di kantin fakultas kedokteran, kau melihat keduanya duduk makan di meja pojok dekat jendela. Begitu menyadari langkahmu mendekat, Yuina langsung menarik kursinya merapat ke sisi Miyuki dan memunggungi lorong tempatmu berdiri."""

    # ┌─ ENDING · E-NPC-03 · Thrift Hari Minggu  [Romantis · host Y/C]
    # │ KAPAN   : romansa tulus dengan Ryena; Moeka selamat
    # │ ISI SKRG: Minggu pagi di toko bekas, bertiga dengan Moeka
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-03"] = """Ryena mengajakmu ke toko barang bekas pada Minggu pagi. Moeka datang terlambat dengan alasan yang ditertawakan mereka berdua sebelum kau sempat bertanya. Ia masih punya masalah, tetapi hari ini ia boleh hanya menjadi teman yang sedang mencari jaket.

Ryena menggandeng tanganmu di antara rak, lalu melepaskan sebentar untuk memeriksa jahitan baju. Kehidupan bersama ternyata penuh perhatian yang tidak dramatis: mengingat ukuran, membagi ongkos, bertanya apakah seseorang sungguh ingin ikut atau hanya takut mengecewakan.

Kalian makan mi kuah di kedai seberang toko setelah selesai berbelanja. Moeka memotret Ryena yang sedang mengomel karena kancing jaket pilihannya longgar satu, sementara kau mengeluarkan jarum kecil dan benang cadangan dari tas Ryena ke atas meja."""

    # ┌─ ENDING · E-NPC-04 · Ryena Tidak Memaafkan  [Buruk · host Y/C]
    # │ KAPAN   : Moeka meninggal atau disakiti pemain
    # │ ISI SKRG: Ryena menjadi saksi paling keras terhadap pemain
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-04"] = """Ryena tidak menerima penjelasan yang mengubah penderitaan Moeka menjadi cerita tentang betapa sulitnya posisimu. Ia menyebut apa yang diketahuinya dengan jelas dan menolak diminta diam demi nama baik.

Jika ada orang bertanya, ia menjawab sebatas yang dapat dipertanggungjawabkan. Ia tidak menyerahkan kehidupan pribadi Moeka kepada rasa ingin tahu mereka. Kemarahannya tidak membuatnya lupa kepada siapa kesetiaan itu seharusnya diberikan.

Saat kalian berpapasan di gerbang gedung desain pada sore terakhir semester, kau berhenti dan membuka mulut hendak menyapanya. Ryena menatap lurus menembus bahumu, merapatkan tali tas kameranya, dan berjalan melewatinya tanpa memperlambat langkah sedikit pun."""

    # ┌─ ENDING · E-NPC-05 · Studio Berdua  [Romantis · host Y/C]
    # │ KAPAN   : romansa dengan Karuha
    # │ ISI SKRG: dua meja gambar dalam satu studio
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-05"] = """Dua meja berada di studio yang sama, menghadap cahaya yang berbeda. Karuha tidak memindahkan semua barangnya untuk menyatukan selera kalian. Kau menyukai kebebasan kecil itu: kedekatan tidak berarti setiap sudut harus kehilangan pemiliknya.

Ada hari ketika pekerjaan berjalan baik dan kalian makan terlambat karena terlalu sibuk mengobrol. Ada hari ketika kritik terdengar terlalu pribadi, lalu perlu dibicarakan lagi sesudah marah mereda. Tak seorang pun mengerjakan karya atas nama yang lain untuk menghindari percakapan sulit.

Menjelang tengah malam, Karuha memutar kursinya dan bertanya apakah kau mau melihat sketsa kasarnya yang belum selesai. Kau meletakkan penamu, menarik bangku kayu ke sebelah mejanya, dan memperhatikan ujung jarinya menunjuk garis arsir yang masih basah."""

    # ┌─ ENDING · E-NPC-06 · Rahasia yang Dititipkan  [Netral · host C]
    # │ KAPAN   : Karuha tahu rahasia Shena dan menjaganya
    # │ ISI SKRG: persahabatan yang lebih kuat dari rahasia
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-06"] = """Karuha tahu ada jarak antara Chiasa yang ia kenal dan orang yang sekarang memegang pensil. Ia tidak menuntut satu cerita yang langsung membuat semua perbedaan masuk akal. Ia meminta kau berhenti berjanji dapat melakukan pekerjaan yang belum sanggup kaulakukan.

Rahasia Shena tidak dijadikannya mata uang. Ia menjaganya sambil mendorongmu membuat keputusan jujur mengenai proyek baru dan bantuan yang perlu diakui. Kadang kau kesal karena ia tidak membiarkanmu bersembunyi di balik rasa takut.

Pada suatu sesi latihan sore, ia mengetuk sudut kertas gambar tempatmu baru saja menyelesaikan sketsa lipatan kain dan bergumam bahwa garisnya sudah jauh lebih bersih. Setelah itu ia meletakkan penghapusnya di mejamu dan menyuruhmu menggambar ulang bagian pergelangan tangan sekali lagi."""

    # ┌─ ENDING · E-NPC-07 · Pasal yang Membela  [Romantis · host Y/C]
    # │ KAPAN   : romansa atau aliansi dengan Sayane
    # │ ISI SKRG: Sayane membela pemain di kampus dan Moeka di sidang banding
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-07"] = """Sayane datang ke pertemuan dengan dokumen rapi dan pertanyaan yang tidak membiarkan orang bersembunyi di balik jabatan. Di kampus ia membantumu mendapat kesempatan menjawab secara adil. Dalam banding yang menyangkut Moeka, ia menolak membiarkan keadaan sulit dipakai sebagai alasan mengabaikan haknya.

Kedekatan kalian tidak membuat Sayane menjanjikan kemenangan. Ia memintamu berkata benar, datang tepat waktu, dan memahami bahwa membela seseorang tidak berarti menghapus pertanggungjawabannya.

Sesudah sidang sore yang melelahkan itu ditutup, kalian duduk di kedai udon dekat stasiun dengan tumpukan map masih di kursi sebelah. Sayane melepas kacamatanya, memijat pangkal hidungnya yang memerah, lalu membiarkanmu mengambilkan segelas air hangat untuknya."""

    # ┌─ ENDING · E-NPC-08 · Rapat Terakhir BEM  [Buruk · host Y/C]
    # │ KAPAN   : Sayane mengetahui manipulasi pemain
    # │ ISI SKRG: ia mengecam pemain di depan umum
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-08"] = """Pada rapat terakhir BEM, Sayane meminta waktu bicara. Ia menjelaskan manipulasi yang diketahuinya, membedakan fakta dari dugaan, dan menolak usahamu menjadikan hubungan pribadi sebagai alasan agar persoalan itu ditutup.

Ruangan tidak langsung berpihak serentak. Ada pertanyaan, keberatan, dan orang yang tampak menyesal telah terlalu mudah percaya. Sayane mendengarkan semuanya tanpa mencabut inti pernyataannya: jabatan dan kedekatan tidak boleh menjadi perlindungan bagi orang yang menyakiti.

Sesudah rapat dibubarkan, ia meletakkan kunci cadangan dan map catatan yang pernah kautitipkan tepat di ujung mejamu. Tanpa menunggu kau mengemasi kertas-kertasmu, ia merapikan tas kerjanya sendiri dan keluar paling dulu dari ruang sidang."""

    # ┌─ ENDING · E-NPC-09 · Redaksi Berdua  [Romantis · host Y/C]
    # │ KAPAN   : romansa dengan Meisa; pemain jujur padanya
    # │ ISI SKRG: akun gosip berhenti menulis tentang pemain
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-09"] = """Meisa berhenti menulis tentangmu untuk akun gosipnya. Ia mengatakan kedekatan kalian membuatnya tidak bisa berpura-pura menjadi pengamat yang tidak berkepentingan. Kau menertawakan cara ia mengucapkannya seperti catatan redaksi, lalu menyadari betapa seriusnya ia sedang berusaha berlaku benar.

Kalian masih berdebat tentang cerita, batas pribadi, dan orang yang tidak hadir untuk membela dirinya. Kejujuranmu tidak memberinya hak menerbitkan semua hal, dan perasaannya tidak memberimu hak menyuruhnya membentuk berita sesuai keinginanmu.

Malam di ruang redaksi itu berakhir dengan dua bungkus roti dingin dan draf artikel kampus yang belum selesai. Meisa menutup layar laptopnya saat kau mengingatkan sudah lewat pukul sepuluh, lalu menyodorkan satu payung lipat untuk kalian pakai berdua menuju stasiun."""

    # ┌─ ENDING · E-NPC-10 · Headline Terakhir  [Buruk · host Y/C]
    # │ KAPAN   : Meisa dipakai lalu dibuang
    # │ ISI SKRG: Meisa menerbitkan semua yang ia tahu
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-10"] = """Meisa menerbitkan tulisan terakhir tentangmu setelah menyadari seberapa jauh dirinya telah dipakai. Ia tidak mengirim draf untuk meminta persetujuan. Orang-orang lain membacanya lebih dahulu sebelum kau menemukan keberanian membuka tautan itu.

Tulisan tersebut memuat hal yang benar-benar kautakuti diketahui. Kemarahan Meisa juga melampaui batas pada bagian yang menyeret kehidupan pribadi orang lain. Kebenaran tentang perbuatanmu tidak membenarkan setiap pilihan yang ia buat untuk menyebarkannya.

Keesokan paginya di lorong fakultas, orang-orang berhenti mengobrol setiap kali kau lewat sambil melirik layar ponsel di tangan mereka. Di ujung koridor dekat papan buletin, Meisa sendiri sedang mengemasi barangnya dari ruang pers di bawah pengawasan staf kemahasiswaan tanpa menoleh ke arahmu."""

    # ┌─ ENDING · E-NPC-11 · Naskah dan Penyuntingnya  [Romantis · host C]
    # │ KAPAN   : romansa dengan Miono
    # │ ISI SKRG: hubungan kerja menjadi lebih dari itu
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-11"] = """Miono mengajakmu makan sesudah rapat kerja, lalu dengan kikuk menjelaskan bahwa undangan itu bukan bagian dari proyek. Untuk pertama kalinya, ia tidak membawa daftar revisi sebagai alasan bertemu.

Kalian membicarakan batas pekerjaan sebelum hubungan pribadi tumbuh lebih jauh. Penilaian karya dan keputusan kontrak perlu ditangani tanpa menjadikan cinta sebagai imbalan. Prosesnya tidak selalu nyaman, tetapi tidak ada yang ingin setiap penolakan revisi berubah menjadi keraguan terhadap kasih sayang.

Suatu malam di apartemennya, Miono membaca buku novel terjemahan yang sama sekali tidak sedang dikejar tenggat kantor. Kau duduk di ujung sofa yang sama sambil mengupas jeruk, dan ketika ia menutup halaman babnya, ia menggeser kakinya mendekat agar bisa bersandar di lututmu."""

    # ┌─ ENDING · E-NPC-12 · Kontrak Diputus  [Buruk · host C]
    # │ KAPAN   : hubungan dengan Miono rusak
    # │ ISI SKRG: Miono memutus kontrak Shena
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-12"] = """Miono memutus hubungan kerja yang tidak lagi bisa dipertahankan dengan kepercayaan. Ia membicarakan penyelesaian kewajiban yang masih ada tanpa mengubahnya menjadi serangan pribadi. Kesopanan itu membuat akhir kontrak terdengar lebih pasti daripada pertengkaran.

Kau kehilangan tawaran baru dan tempat yang selama ini diberikan nama Shena di meja penerbit. Karya lama tetap mempunyai riwayatnya sendiri; masalah yang terjadi tidak dapat diperbaiki hanya dengan meminta orang mengingat betapa bagusnya sampul terdahulu.

Sesudah pertemuan itu selesai, Miono mengantar sampai ke depan lift gedung redaksi, membungkuk singkat, dan menekan tombol turun untukmu. Kau pulang membawa amplop cokelat berisi salinan penghentian kontrak, sementara kartu akses tamu di sakumu sudah harus dikembalikan di meja resepsionis lantai dasar."""

    # ┌─ ENDING · E-NPC-13 · Kakak yang Dipilih  [Romantis · host Y]
    # │ KAPAN   : romansa dengan Haruto
    # │ ISI SKRG: keluarga Sakurajima terkejut; Nagisa bereaksi sesuai tahapnya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-13"] = """Haruto mengatakan kepada keluarganya bahwa ia sedang menjalin hubungan denganmu. Keheningan pertama di meja makan membuat kalian berdua salah mengambil gelas. Nagisa menatap kakaknya, kemudian dirimu, seolah sedang menghitung berapa banyak percakapan yang telah luput didengarnya.

Ia membawa perasaan dan sejarahnya sendiri ke dalam kabar itu. Kau tidak memaksanya memberi restu dengan cepat. Haruto tetap kakaknya, dan mencintaimu tidak boleh menghapus tanggung jawabnya mendengar adiknya tanpa selalu membela diri.

Beberapa bulan kemudian, kunjungan akhir pekan ke rumah Sakurajima sudah menjadi kebiasaan baru. Haruto masih sering salah tingkah setiap kali menyodorkan piring buah ke dekatmu di depan ibunya, lalu buru-buru mengajakmu keluar mencuci mobil di halaman hanya agar bisa menggenggam tanganmu sebentar."""

    # ┌─ ENDING · E-NPC-14 · Restu Sakurajima  [Netral · host Y/C]
    # │ KAPAN   : Haruto menjadi sekutu
    # │ ISI SKRG: keluarga Nagisa membuka pintu untuk pemain
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-14"] = """Haruto membukakan pintu sebelum kau selesai merapikan salam yang sudah disiapkan. Ia mempersilakan masuk dan mengatakan orang tuanya sedang membuat minuman. Penerimaan itu terasa jauh lebih sederhana daripada semua usaha yang pernah kaulakukan untuk mendapatkannya.

Ia mempercayaimu karena telah melihat caramu memperlakukan Nagisa saat tidak ada keuntungan yang bisa diminta sebagai balasan. Kepercayaan itu tidak membuatnya berhenti bertanya. Justru karena kalian dapat bicara terus terang, ia tidak perlu selalu berdiri di antara kalian dengan kecurigaan.

Di ruang keluarga, Nagisa sedang mengomel soal tugas maketnya sementara ibunya meletakkan sepiring kue beras hangat di meja rendah. Haruto menepuk bahumu sambil menunjuk bantal duduk yang kosong di dekat meja, lalu ikut duduk menyeduh teh untuk kalian berempat."""

    # ┌─ ENDING · E-NPC-15 · Esai untuk Satu Orang  [Romantis · host Y]
    # │ KAPAN   : romansa dengan Matsuda
    # │ ISI SKRG: Matsuda menulis esai baru, kali ini tentang tokoh yang memilih
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-15"] = """Matsuda menyerahkan esai baru dengan peringatan bahwa kau tidak wajib menyukainya. Kau membacanya di depan jendela klub sastra. Kali ini tokohnya tidak menunggu semua pintu tetap terbuka; ia memilih satu jalan sambil mengakui jalan lain akan hilang.

Ketika kautanya apakah itu tentang kalian, Matsuda mengatakan tidak semua tulisan bisa dipakai untuk bersembunyi dari jawaban pribadi. Ia menyukaimu. Kalimat itu diucapkan tanpa kutipan, tanpa tokoh pengganti, tanpa ejekan yang membuatnya mudah ditarik kembali.

Kau melipat bundel esai itu ke dalam tasmu sementara cahaya sore meredup di jendela ruang klub. Matsuda menutup buku catatannya, mengambil jaket dari sandaran kursi, dan menanyakan apakah kau mau mampir makan ramen sebelum kereta malam penuh."""

    # ┌─ ENDING · E-NPC-16 · Saksi yang Menulis  [Buruk · host Y/C]
    # │ KAPAN   : Matsuda membongkar manipulasi pemain
    # │ ISI SKRG: esai yang membongkar pemain dibaca seluruh fakultas
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-16"] = """Esai Matsuda beredar dari klub ke fakultas. Ia menulis tentang orang yang memperlakukan kehidupan teman-temannya sebagai bahan susunan, lalu menyebut kendali sebagai kepedulian. Cukup banyak pembaca mengenali siapa yang dimaksud.

Koita membacanya tanpa tertawa. Beberapa orang menghubungimu dengan pertanyaan yang tidak lagi dapat dijawab melalui gurauan. Matsuda tidak mengaku mengetahui semua isi kepalamu; ia menulis tentang pola tindakan yang sudah terlalu lama dilihat orang tanpa diberi nama.

Ketika kau masuk ke ruang baca fakultas sore itu, tiga mahasiswa yang sedang memegang selebaran jurnal klub langsung menutup halaman mereka dan pindah ke meja seberang. Di sudut ruangan, Matsuda tetap mengetik di laptopnya tanpa mengangkat kepala sedikit pun saat kau melintas."""

    # ┌─ ENDING · E-NPC-17 · Informan yang Setia  [Romantis · host Y]
    # │ KAPAN   : romansa dengan Kaichi
    # │ ISI SKRG: informan yang berhenti menjual pemain
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-17"] = """Kaichi datang membawa makanan dan informasi yang kali ini tidak dipasangi harga. Ketika kau bertanya, ia menjawab bahwa ia ingin tahu apakah kalian masih bisa mengobrol tanpa salah seorang menawarkan sesuatu.

Kalian perlu belajar berhenti memakai rahasia sebagai alat tawar. Tidak semua kebiasaan hilang karena pengakuan cinta. Kaichi kadang masih menyembunyikan gugup di balik lelucon soal utang, dan kau mengingatkannya bahwa perhatianmu tidak sedang diperjualbelikan.

Pada malam hujan ketika ia pulang dari kerja paruh waktu dengan kemeja basah dan wajah pucat karena kelelahan, ia tetap mengetuk pintu apartemenmu. Kau menariknya masuk, menyerahkan handuk kering tanpa menanyakan kabar kampus sepatah kata pun, lalu memanaskan sisa sup di dapur."""

    # ┌─ ENDING · E-NPC-18 · Maket Kedua  [Romantis · host Y]
    # │ KAPAN   : romansa dengan Fuuto
    # │ ISI SKRG: Fuuto berhenti mengejar Nagisa
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-18"] = """Fuuto berhenti mencari alasan untuk terus berada dekat Nagisa. Ia mengakui bahwa perasaan tidak memberinya hak menunggu seseorang sampai lelah menolak. Pengakuan itu membuat percakapan kalian lebih jujur daripada pujian yang dahulu ia siapkan untuk orang lain.

Di studio arsitektur, kalian mengerjakan maket kedua. Ada bagian yang miring, jadwal yang terlalu padat, dan perselisihan tentang cara memperbaiki pekerjaan. Fuuto mulai bertanya pendapatmu tanpa menjadikanmu saksi betapa besar usahanya mendapatkan seseorang.

Sesudah maket kayu balsa itu selesai dikeringkan pada Jumat petang, Fuuto membersihkan sisa lem di jari-jarinya lalu mengajakmu menonton film malam. Saat keluar dari gedung studio, ia meraih tanganmu di tangga batu dan berjalan bersisian menuju gerbang."""

    # ┌─ ENDING · E-NPC-19 · Pewaris yang Membangkang  [Romantis · host Y]
    # │ KAPAN   : romansa dengan Tojo
    # │ ISI SKRG: rencana pertunangan Tojo–Saionji runtuh
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-19"] = """Tojo menarik diri dari rencana pertunangan dengan Shiori. Keputusan itu menimbulkan lebih banyak percakapan keluarga daripada yang sanggup ia hindari dengan sikap percaya diri. Shiori mendengarnya sebagai kabar tentang hidupnya sendiri, bukan adegan yang harus ia selamatkan demi menjaga nama siapa pun.

Kau tidak menerima kedekatan Tojo sebagai bukti bahwa cara lamanya memperlakukan orang tiba-tiba tidak penting. Ia harus belajar mendengar penolakan dan melepaskan anggapan bahwa masa depan seseorang dapat ditentukan karena hubungan itu menguntungkan.

Sore itu ia datang menemuimu di kafe dekat stasiun tanpa sopir keluarga dan tanpa setelan resmi yang biasa dipakainya. Dengan kemeja yang agak kusut karena naik kereta komuter, ia meletakkan dua tiket pameran akhir pekan di meja dan bertanya pelan apakah jadwalmu kosong."""

    # ┌─ ENDING · E-NPC-20 · Skandal Omiai  [Khusus · host Y]
    # │ KAPAN   : romansa dengan Tatsuru
    # │ ISI SKRG: omiai Miyuki runtuh dalam skandal
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-20"] = """Omiai yang seharusnya mempertemukan Tatsuru dan Miyuki berakhir dalam percakapan yang tidak disiapkan keluarga mana pun. Tatsuru mengakui hubungan yang ingin dijalaninya denganmu. Miyuki menatapnya lama, kemudian meminta mereka berhenti membicarakan masa depannya seolah ia hanya perlu menerima keputusan yang tersisa.

Kabar itu menjadi skandal karena orang-orang di sekeliling terlalu banyak menanam harapan tanpa bertanya. Kalian harus menghadapi kemarahan dan komentar yang tidak semuanya adil. Namun kegaduhan tersebut juga tidak menghapus kewajiban berkata jujur kepada orang yang telah dibawa masuk ke rencana ini.

Dua bulan sesudah pertemuan keluarga yang gaduh itu, Tatsuru menjemputmu sepulang jam jaganya dengan mobil kecil yang baru ia cicil sendiri. Di kursi penumpang masih ada kardus buku medis dari rumah orang tuanya, dan ia menggeser tumpukan itu ke bagasi belakang agar kau bisa duduk di sebelahnya."""

    # ┌─ ENDING · E-NPC-21 · Kafe Pagi  [Netral · host Y/C]
    # │ KAPAN   : kerja tetap di Kafe Komorebi
    # │ ISI SKRG: Ito menjadi mentor; tubuh pemain paling sehat di semua ending
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-21"] = """Ito memberimu jadwal kerja tetap di Kafe Komorebi. Ia menjelaskan tanggung jawab, waktu istirahat, dan alasan mengapa datang terlalu lelah bukan sesuatu yang patut dibanggakan. Kau sempat menganggapnya cerewet sebelum menyadari betapa jarang orang lain memintamu berhenti tanpa menagih sesuatu.

Pagi-pagi di kafe punya urutan yang dapat dipelajari: membuka ruangan, menyiapkan meja, menyapa pelanggan. Kau makan pada waktunya dan tidur karena esok harus benar-benar hadir, bukan karena tubuh akhirnya tidak sanggup menolak.

Pukul tujuh kurang sepuluh, kau memutar papan tanda buka di pintu kaca depan sementara sinar matahari pagi jatuh ke lantai kayu yang baru dipel. Di balik meja bar, Ito menggeser secangkir kopi susu hangat dan sepiring roti panggang ke arahmu sebelum lonceng pintu berbunyi menyambut pelanggan pertama."""

    # ┌─ ENDING · E-NPC-22 · Batas Profesional  [Netral · host Y/C]
    # │ KAPAN   : pemain mengejar Sato secara romantis
    # │ ISI SKRG: Sato menolak dan memindahkan konseling ke rekan lain
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-22"] = """Kau mengucapkan perasaanmu kepada Sato di akhir sesi. Ia mendengar sampai selesai, lalu menjawab dengan tenang bahwa hubungan romantis tidak dapat dijalani antara dirinya dan orang yang ia dampingi dalam konseling.

Penolakan itu tidak disertai ejekan atau hukuman. Ia membicarakan perpindahan pendampingan agar kau tetap bisa memperoleh bantuan tanpa harus terus menahan rasa tidak nyaman di ruangan yang sama. Kau boleh sedih; kesedihan itu tidak dipakai untuk mengubah batasnya.

Pada sesi pertama dengan konselor rujukan yang baru pekan berikutnya, tanganmu sempat berhenti lama di gagang pintu ruang tunggu karena malu. Ketika pintu akhirnya dibuka dan konselor itu mempersilakan duduk, kau meletakkan tasmu di kursi dan menyerahkan lembar rujukan bertanda tangan Sato."""

    # ┌─ ENDING · E-NPC-23 · Konseling Host  [Netral · host Y/C]
    # │ KAPAN   : konseling rutin dengan Sato
    # │ ISI SKRG: stres_host turun; rahasia Sistem dicatat sebagai "keyakinan pasien"
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-23"] = """Sato tidak meminta kau membuktikan Sistem pada pertemuan pertama. Ia mendengar keyakinan yang kauceritakan, menanyakan pengaruhnya pada tidur dan pilihanmu, lalu membahas hal yang bisa dibantu hari ini.

Konseling tidak menghapus kontrak dari duniamu. Ia membantumu membedakan rasa takut, kebutuhan tubuh, dan keputusan yang tetap berada dalam tanggung jawabmu. Perlahan kau berhenti menganggap setiap jeda sebagai waktu yang dicuri dari tugas menjaga hidup.

Dalam map arsip klinik, cerita tentang Sistem tertulis rapi sebagai keyakinan pasien. Ketika jam dinding ruang konseling berdentang pukul empat sore, Sato menutup buku catatannya, mengingatkanmu untuk makan malam sebelum pukul delapan, dan menjadwalkan pertemuan kamis depan."""

    # ┌─ ENDING · E-NPC-24 · Kepercayaan Kuroiwa  [Netral · host Y/C]
    # │ KAPAN   : Kuroiwa mempercayai pemain
    # │ ISI SKRG: peringatan dini setiap kali Shiori bergerak
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-24"] = """Kuroiwa menghubungimu sebelum sebuah pertemuan yang mungkin menjadi pertengkaran. Pesannya singkat: datang jika ingin bicara, dan jangan mengira Shiori akan selalu mau mendengar pada waktu yang kaupilih.

Kepercayaannya memberimu peringatan lebih dini, bukan izin memasuki kehidupan Shiori tanpa batas. Ia menegur saat kau mulai menganggap pengetahuannya sebagai jalan menghindari percakapan langsung. Kesetiaannya tetap kepada orang yang selama ini ia bantu tumbuh, termasuk ketika ia percaya kau tidak bermaksud buruk.

Pada kunjungan berikutnya ke kediaman Saionji, Kuroiwa membukakan pintu samping tanpa lagi menahanmu di beranda untuk memeriksa keperluanmu. Ia hanya mengambil mantelmu, menunjuk arah ruang teh di ujung lorong, lalu kembali ke posnya dengan anggukan singkat."""

    # ┌─ ENDING · E-NPC-25 · Saksi yang Dipercaya  [Netral · host Y/C]
    # │ KAPAN   : pemain membantu Hanabusa
    # │ ISI SKRG: kesaksian pemain menjatuhkan Ogawa atau Kuga
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-25"] = """Hanabusa memintamu mengulang hal yang sungguh kaulihat. Ia tidak membantu mengisi bagian yang tidak kauketahui, sekalipun jawaban lengkap akan terdengar lebih meyakinkan. Menjadi saksi ternyata menuntut keberanian mengatakan tidak tahu juga.

Kesaksianmu membantu perkara terhadap orang yang selama ini merasa aman dari pertanyaan. Mereka yang dirugikan tetap harus menjalani proses yang berat, tetapi kini tidak seluruh pengalaman mereka berdiri sendirian di hadapan penyangkalan.

Sesudah berita acara terakhir ditandatangani, Hanabusa merapikan map ke dalam laci besinya dan hanya mengucapkan terima kasih singkat karena kau sudah datang tepat waktu. Kau keluar ke pelataran gedung komite yang mulai gelap, mengancingkan jaketmu, dan berjalan pulang menuju stasiun."""

    # ┌─ ENDING · E-NPC-26 · Penyusup  [Khusus · host Y/C]
    # │ KAPAN   : penyamaran berhasil; bukti cukup
    # │ ISI SKRG: Ogawa atau Kuga jatuh dari dalam
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-26"] = """Ketika perkara terbuka, orang yang dahulu menerima kehadiranmu di lingkarannya akhirnya memahami bahwa kesetiaanmu tidak pernah berada di tempat yang mereka kira. Ogawa atau Kuga kehilangan perlindungan yang diberikan orang-orang yang takut dan saling tidak tahu.

Apa yang diketahui selama penyamaran kini harus diperiksa melalui proses yang nyata. Kau tidak diminta memperindah peranmu. Ada tindakan yang perlu kauberi penjelasan sendiri, dan orang yang dirugikan tidak otomatis berutang rasa terima kasih karena rencanamu berhasil.

Sesudah selesai menyerahkan rekaman dan salinan dokumen di ruang pemeriksaan lantai tiga, kau mencopot kartu tanda anggota dari kerah kemejamu dan meletakkannya di meja petugas. Di luar gedung, seorang teman lama memanggil namamu dari dekat rak sepeda, dan kau menoleh sambil mengembuskan napas panjang."""

    # ┌─ ENDING · E-NPC-27 · Penyusup yang Tertelan  [Buruk · host Y/C]
    # │ KAPAN   : penyamaran terlalu lama
    # │ ISI SKRG: pemain ikut terseret kejahatan mereka
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-27"] = """Pada awalnya, kau mengatakan semua yang dilakukan hanya untuk mempertahankan penyamaran. Lalu ada keputusan yang mulai kaubela bahkan ketika tidak sedang berada di dekat orang yang ingin kaukelabui.

Ketika perkara terbongkar, namamu ikut disebut karena perbuatanmu sendiri. Niat awal tidak menghapus orang yang dirugikan selama kau menunggu saat yang dianggap tepat. Kau diminta menjelaskan apa yang diketahui, apa yang dilakukan, dan mengapa tidak berhenti ketika masih bisa.

Di ruang tunggu pemeriksaan, kursi tempatmu duduk hanya berjarak tiga meter dari orang yang dulu kaujadikan target penyelidikan. Ketika petugas keluar memanggil daftar nama terperiksa berikutnya, namamu dibacakan tepat sesudah namanya dalam berkas perkara yang sama."""

    # ┌─ ENDING · E-HP-01 · Bersama Satu Orang  [Romantis · host Y/C]
    # │ KAPAN   : satu hubungan romantis bertahan sampai M36
    # │ ISI SKRG: siapa pun orangnya: heroine, Koita, Chiasa atau Yutaka NPC, atau NPC sampingan
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HP-01"] = """Di antara banyak pertemuan, satu hubungan bertahan sampai kelulusan. Orang itu mengenal caramu menghindari pertanyaan, kebiasaan kecil saat lelah, dan bagian dirimu yang tidak pernah tampil baik di awal kisah cinta.

Kalian tidak berhenti berbeda pendapat. Ada janji yang perlu diperbaiki dan masa depan yang belum dapat ditentukan dalam satu percakapan. Namun tak seorang pun harus menebak apakah hubungan ini masih ada setiap kali hari menjadi sulit.

Setelah upacara di aula selesai, ia mencarimu di sela kerumunan toga dan menanyakan mau makan malam di mana. Kau menyebutkan kedai dekat stasiun yang menyisakan menu kesukaannya, lalu menggenggam tangannya sambil berjalan keluar gerbang kampus."""

    # ┌─ ENDING · E-HP-02 · Bersama Beberapa Orang  [Khusus · host Y/C]
    # │ KAPAN   : lebih dari satu hubungan bertahan, terbuka atau rahasia
    # │ ISI SKRG: lihat E-X-02 dan E-X-01
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HP-02"] = """Lebih dari satu orang masih menyebutmu pasangan. Dari luar, keadaan itu mungkin tampak seperti bukti betapa banyak cinta yang berhasil kaupertahankan. Dari dalam, semuanya bergantung pada apa yang benar-benar mereka ketahui dan setujui.

Pada bagian yang dibicarakan terbuka, ada jadwal, kecemburuan, dan hak menarik diri yang harus dihormati. Pada bagian yang disembunyikan, setiap ketenangan masih berdiri di atas sesuatu yang belum boleh dipilih orang yang terlibat. Jumlah hubungan tidak mengatakan mana yang sedang kalian jalani dengan jujur.

Di bawah pohon sakura dekat gerbang, ponsel di tanganmu bergetar menampilkan dua pesan berturut-turut yang menanyakan posisimu sekarang. Kau menoleh ke arah aula wisuda sementara langkah seseorang sudah mendekat dari belakang untuk memanggil namamu."""

    # ┌─ ENDING · E-HP-03 · Tidak Dapat Siapa-Siapa  [Netral · host Y/C]
    # │ KAPAN   : pernah mengejar, tetapi tidak ada yang bertahan
    # │ ISI SKRG: pemain berakhir sendiri; cerita tidak menghukumnya karena itu
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HP-03"] = """Kau pernah mengira ada seseorang yang akan berada di sampingmu pada hari ini. Beberapa kedekatan berakhir sebelum sempat diberi nama, beberapa hubungan sungguh dimulai lalu tidak dapat diteruskan. Tidak semua akhir mempunyai seorang penjahat yang memudahkan rasa kehilangan.

Di wisuda, kau menyalami teman dan mengambil foto. Ada saat ketika melihat pasangan lain membuat dadamu nyeri, lalu ada percakapan biasa yang membuatmu tertawa tanpa merasa sedang menutupi apa pun.

Sore itu kau pulang ke kamar dengan tabung ijazah di tangan, mampir membeli bahan makan malam kesukaanmu di supermarket stasiun, lalu menggantung jas wisudamu di lemari sebelum menyalakan kompor."""

    # ┌─ ENDING · E-HP-04 · Ditinggalkan Semua  [Buruk · host Y/C]
    # │ KAPAN   : semua orang yang dikejar pergi karena kebohongan atau luka
    # │ ISI SKRG: sendiri, dan semua orang tahu kenapa
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HP-04"] = """Orang-orang yang pernah kaudekati sudah pergi. Mereka tidak menyusun kepergian itu sebagai hukuman bersama. Masing-masing sampai pada batasnya sendiri setelah terlalu sering harus menebak kebenaran di balik perhatianmu.

Kau tidak dapat lagi memanggil kenangan hangat tanpa mengingat apa yang menyusul sesudahnya. Beberapa orang memblokir nomor, yang lain menjawab hanya untuk menyelesaikan urusan. Mereka berhak menolak percakapan yang kaubutuhkan demi merasa telah dimaafkan.

Saat kerumunan wisudawan berkumpul di pelataran gedung utama untuk berfoto per angkatan, tak seorang pun memanggilmu bergabung ketika kau berdiri di tepi tangga. Kau memasukkan kedua tangan ke saku jas, berbalik meninggalkan halaman kampus lebih awal, dan pulang dengan kereta siang yang masih lengang."""

    # ┌─ ENDING · E-HP-05 · Tidak Pernah Mengejar Siapa Pun  [Netral · host Y/C]
    # │ KAPAN   : tidak pernah memulai romansa
    # │ ISI SKRG: tiga tahun tanpa romansa; deviasi hanya datang dari cara lain
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HP-05"] = """Tiga tahun berlalu tanpa kau memulai romansa. Ada undangan yang diterima sebagai teman, perhatian yang tidak diteruskan menjadi janji, dan malam-malam yang dipakai untuk hal lain selain mencari pasangan.

Sebagian orang mengira kau menyembunyikan cinta besar. Kau belajar tidak harus memberi kisah yang mereka harapkan. Hidupmu tetap berisi kedekatan, pertentangan, kerja, dan keputusan yang mengubah orang di sekitarmu dengan cara yang tidak selalu romantis.

Pada hari kelulusan, kau meminta seorang teman sekelas memotretmu sendirian di depan plakat gerbang Kouseikan. Setelah memeriksa hasilnya di layar kamera dan mengucapkan terima kasih, kau menyampirkan tas di bahu dan melangkah keluar menuju jalan raya."""

    # ┌─ ENDING · E-HP-06 · Cinta yang Datang Terlambat  [Khusus · host Y/C]
    # │ KAPAN   : seseorang mengaku di M35 atau M36 setelah pemain menyerah
    # │ ISI SKRG: jawaban pemain menjadi slide terakhir
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HP-06"] = """Pengakuan itu datang ketika kau sudah berhenti menunggu. Setelah acara hampir selesai, seseorang meminta waktu dan mengatakan ada hal yang terlambat dipahami tentang perasaannya kepadamu.

Kau mendengar tanpa memutuskan bahwa keterlambatan itu pasti romantis. Ada hidup yang telah kaususun setelah menyerah, luka yang mungkin belum selesai, dan kemungkinan yang masih dapat kainginkan. Semua itu pantas hadir dalam jawabanmu.

Di bawah pohon dekat pagar belakang kampus yang mulai sepi, ia berdiri dua langkah di depanmu sambil meremas ujung map ijazahnya dan mengatakan kau tidak harus menjawab sekarang. Kau menarik napas panjang, menatap matanya, lalu membuka mulut untuk mengucapkan kalimat pertamamu."""

    # ┌─ ENDING · E-HP-07 · Patah Hati yang Diterima  [Netral · host Y/C]
    # │ KAPAN   : ditolak dengan jujur, dan pemain menerimanya
    # │ ISI SKRG: sendiri, tetapi damai
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HP-07"] = """Ia menolak dengan jujur. Kau mendengar kata-katanya tanpa mencoba menemukan celah yang akan membuat penolakan itu sementara. Sesudahnya, kau tetap sedih lebih lama daripada yang ingin kauakui.

Ada hari ketika kau perlu menjaga jarak. Kau menjelaskannya tanpa menjadikannya ancaman agar ia berubah pikiran. Perlahan, keinginan menghubungi setiap kali merasa sepi mulai berkurang, memberi tempat bagi hidup yang selama ini tertahan oleh satu harapan.

Saat kalian berpapasan lagi di halaman wisuda, kau berhenti sebentar untuk mengucapkan selamat dan menyalami tangannya dengan wajar. Setelah ia tersenyum dan kembali ke rombongan teman-temannya, kau membetulkan letak tas di pundakmu dan melanjutkan langkah menuju gerbang stasiun."""


    # ═════ Sistem / Force ═════
    # ┌─ ENDING · E-SI-01 · Kontrak Selesai  [Romantis · host Y/C]
    # │ KAPAN   : deviasi cukup
    # │ ISI SKRG: Sistem berpamitan dengan satu ejekan terakhir; pemain hidup
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-01"] = """Jendela biru muncul ketika suara wisuda masih terdengar dari halaman. Sistem membacakan hasilnya dengan nada yang selama tiga tahun kaubenci dan kautunggu sekaligus. Kontrak dinyatakan selesai. Kau akan tetap hidup.

Ia menambahkan satu ejekan tentang betapa lama waktu yang kaubutuhkan. Kau hampir membalas, lalu berhenti. Tidak ada tugas baru menyusul, tidak ada ancaman kecil diselipkan setelah kalimat terakhir. Untuk pertama kalinya, diam di kepalamu bukan jeda sebelum perintah berikutnya.

Seseorang memanggil namamu dari bawah pohon sakura di dekat gerbang. Kau berkedip melihat udara kosong tempat jendela biru itu baru saja lenyap, lalu melangkah turun dari tangga aula untuk menghampirinya."""

    # ┌─ ENDING · E-SI-02 · Nyaris  [Khusus · host Y/C]
    # │ KAPAN   : deviasi tipis di atas ambang
    # │ ISI SKRG: "Nyaris." Sistem tidak pernah bicara lagi
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-02"] = """Sistem hanya mengatakan satu kata sebelum menutup perhitungan: nyaris. Kau menunggu penjelasan, tetapi tidak ada. Ancaman berakhir dengan ketepatan dingin yang sama seperti ketika ia dimulai.

Tanganmu masih gemetar saat menyadari kau selamat. Orang yang berdiri di dekatmu mengira kau gugup karena hari kelulusan. Kau tidak membetulkannya. Ada jarak yang sangat tipis antara dunia ini tetap dapat kaulihat dan semua hal yang tak akan pernah sempat kaulakukan.

Sistem tidak pernah bicara lagi sesudah detik itu. Beberapa bulan kemudian, saat terbangun tengah malam karena bunyi hujan di atap kamar, kau masih sempat menatap langit-langit gelap untuk menunggu suara di kepalamu sebelum berbalik memeluk bantal dan kembali tidur."""

    # ┌─ ENDING · E-SI-03 · Penonton Terakhir  [Romantis · host Y/C]
    # │ KAPAN   : deviasi tinggi; rapport_sistem tinggi
    # │ ISI SKRG: Sistem membacakan semua yang ia hitung, lalu pamit seperti teman
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-03"] = """Sistem membacakan perjalananmu lebih lama daripada yang diperlukan untuk memberi hasil. Nama, pilihan, perubahan yang dahulu disampaikannya sebagai angka kini terdengar seperti catatan seseorang yang memang selalu ada di sana.

Kau tidak lupa bahwa ia mengancammu. Kedekatan yang terbentuk tidak membuat kontrak itu baik. Namun ketika ia mengatakan kau lolos, ada jeda yang tidak menyerupai ejekan. Ia menyebutmu penonton yang terlalu jauh masuk ke cerita, kemudian mengaku penasaran apa yang akan kaulakukan tanpa dirinya.

Kau bergumam bahwa itu bukan urusannya lagi. Terdengar dengung pendek yang mirip tawa sebelum titik cahaya terakhir di sudut matamu padam, menyisakan bayangan halaman kampus dan tangan seseorang yang baru saja menepuk pundakmu."""

    # ┌─ ENDING · E-SI-04 · Kontrak Baru  [Khusus · host Y/C]
    # │ KAPAN   : deviasi tinggi; sikap penyelidik
    # │ ISI SKRG: Sistem menawarkan kontrak baru (kait New Game Plus)
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-04"] = """Kau telah terlalu sering bertanya sampai Sistem berhenti berpura-pura tidak mendengar. Sesudah hasil yang tinggi diumumkan, ia menampilkan tawaran baru. Syaratnya belum seluruhnya terbuka. Imbalannya disusun agar terdengar lebih menarik daripada kebebasan yang baru saja kaudapatkan.

Kau membaca tanpa segera menjawab. Tiga tahun pertama mengajarimu bahwa kata yang tidak ditanyakan dapat berubah menjadi ancaman, dan bahwa rasa ingin tahu bukan alasan menyerahkan hidup tanpa mengetahui harga.

Di halaman depan gedung wisuda, teman-teman seangkatanmu sudah melambai memanggilmu untuk berfoto bersama. Jendela biru berisi dua kotak pilihan itu masih melayang diam di depan wajahmu sementara jari tanganmu terangkat perlahan di udara."""

    # ┌─ ENDING · E-SI-05 · Gagal di Bawah Sakura  [Buruk · host Y/C]
    # │ KAPAN   : deviasi kurang; pemain di kampus
    # │ ISI SKRG: pemain mati di hari wisuda, di bawah sakura
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-05"] = """Sakura bergerak di atas halaman kampus ketika Sistem mengumumkan bahwa hasilmu tidak cukup. Kau mendengar tepuk tangan dari arah gedung wisuda dan sempat berpikir betapa kejamnya dua suara itu dapat berlangsung bersamaan.

Kau mencoba menyebut nama seseorang. Orang-orang yang melihatmu mendadak berhenti segera mendekat dan mencari pertolongan. Mereka tidak tahu ada kontrak yang telah memutuskan akhir ini; yang mereka lihat adalah seseorang yang seharusnya masih memiliki banyak hari sesudah kelulusan.

Sehelai kelopak merah muda jatuh menempel di punggung tanganmu yang tergeletak di atas batu trotoar. Suara langkah sepatu yang berlari mendekat dan teriakan panik yang memanggil ambulans terdengar makin jauh sebelum pandanganmu gelap sepenuhnya."""

    # ┌─ ENDING · E-SI-06 · Cinta yang Tidak Dihitung  [Buruk · host C]
    # │ KAPAN   : Chiasa × Yutaka saja
    # │ ISI SKRG: "Ini bukan penyimpangan. Ini pelarian."
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-06"] = """Yutaka menggenggam tanganmu ketika suara Sistem menyela. Kau melihat wajah orang yang mencintaimu dan menyadari ia tidak dapat mendengar keputusan yang sedang dijatuhkan di antara dua tarikan napas kalian.

Sistem mengatakan hubungan kalian bukan penyimpangan yang dimintanya. Dalam perhitungannya, hidup Koita belum cukup berubah. Kau telah mengetahui peringatan itu, tetapi tetap sempat berharap kebahagiaan yang nyata dapat membuat aturan yang kejam merasa malu.

Ketika lututmu mendadak lemas di tengah trotoar, Yutaka langsung menahan bahumu dan memanggil namamu dengan suara yang pecah oleh panik. Hal terakhir yang kaulihat sebelum matamu tertutup adalah wajahnya yang menunduk dekat sekali di atasmu sambil berteriak meminta tolong."""

    # ┌─ ENDING · E-SI-07 · Tubuh Pinjaman Menyerah  [Buruk · host Y/C]
    # │ KAPAN   : mati karena tubuh sebelum wisuda
    # │ ISI SKRG: tubuh host berhenti lebih dulu daripada kontraknya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-07"] = """Tubuhmu berhenti sanggup mengikuti jauh sebelum tanggal evaluasi. Semua jadwal yang kaubela dengan alasan hanya sedikit lagi akhirnya ditinggalkan di meja, bersama pesan yang tidak sempat dibalas.

Orang-orang mencari pertolongan dan menunggu kabar. Sebagian baru mengetahui betapa lama kau menyembunyikan kelelahan dan sakit. Sistem tidak memberi waktu tambahan karena kau sudah berusaha keras. Tubuh yang dipinjamkan kepadamu tidak menjadi lebih kebal hanya karena ada ancaman di dalam kepalamu.

Ketika musim semi akhirnya tiba dan aula Kouseikan dipenuhi wisudawan, mejamu di kamar tetap menyimpan tumpukan buku catatan yang berhenti di pertengahan Februari. Di atasnya terletak seikat bunga putih yang baru diletakkan keluargamu pagi itu."""

    # ┌─ ENDING · E-SI-08 · Pembangkang  [Buruk · host Y/C]
    # │ KAPAN   : hukuman kritis karena pembangkangan sengaja
    # │ ISI SKRG: Sistem menagih lebih awal
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-08"] = """Kau menolak dengan sadar, kali ini tanpa mencoba membuatnya terdengar seperti salah paham. Sistem memperingatkanmu, lalu menunggu cukup lama untuk memastikan bahwa jawabanmu tidak berubah.

Hukuman datang sebelum hari yang selama ini dijadikan batas. Kau tidak mempunyai pidato yang membuatnya kehilangan kuasa. Di sekelilingmu, orang lain terus menjalani hari biasa, tidak tahu bahwa sebuah keputusan tentang hidupmu baru saja diambil oleh sesuatu yang tidak dapat mereka temui.

Cangkir di tanganmu terlepas dan pecah di lantai koridor sementara angka hitungan mundur di matamu berhenti pada nol. Dua mahasiswa yang kebetulan melintas langsung berlari menahan tubuhmu yang merosot ke dinding sambil memanggil namamu berkali-kali."""

    # ┌─ ENDING · E-SI-09 · Lolos di Balik Jeruji  [Khusus · host Y/C]
    # │ KAPAN   : lolos; sedang dipenjara
    # │ ISI SKRG: "Selamat, kau hidup. Di sini."
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-09"] = """Di balik jeruji, Sistem mengumumkan bahwa kau lolos. Suaranya hampir riang ketika menambahkan bahwa hidup yang diberikan kepadamu akan tetap berlangsung di sini.

Kau duduk tanpa menjawab. Selamat dari kontrak tidak mengubah putusan, menghapus kejahatan, atau memulihkan orang yang dirugikan. Waktu yang dahulu kauhitung menuju wisuda kini diukur dengan jadwal yang ditentukan orang lain.

Ketika jendela biru itu akhirnya lenyap, dinding beton sempit di hadapanmu tidak berubah sedikit pun. Dari ujung lorong terdengar bunyi sepatu bot petugas dan gemerincing kunci besi yang mendekat untuk pemeriksaan jam makan siang."""

    # ┌─ ENDING · E-SI-10 · Gagal di Balik Jeruji  [Buruk · host Y/C]
    # │ KAPAN   : gagal; sedang dipenjara
    # │ ISI SKRG: mati di sel pada jam wisuda
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-10"] = """Kau mengetahui jam wisuda dari jadwal yang masih diingat, bukan dari pemandangan kampus. Di sel, suara Sistem datang tepat pada waktunya dan mengatakan hasilmu tidak memenuhi kontrak.

Kau memanggil, lalu kehilangan kemampuan menyelesaikan kalimat. Orang di dekatmu menyadari ada yang salah; bantuan dicari melalui pintu dan lorong yang membatasi setiap gerakan. Mereka tidak mempunyai cara melawan sesuatu yang bahkan tidak mereka ketahui ada.

Tanganmu merosot dari tepi dipan besi tepat ketika kunci pintu sel diputar dari luar. Di kejauhan sana, lonceng upacara kelulusan Kouseikan selesai berbunyi tanpa seorang pun di aula menyebut namamu."""

    # ┌─ ENDING · E-SI-11 · Hidup Tanpa Nama  [Khusus · host Y/C]
    # │ KAPAN   : lolos; reputasi hancur di semua lingkungan
    # │ ISI SKRG: hidup, tetapi tak ada yang menunggu
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-11"] = """Kau selamat. Sistem mengucapkannya tanpa menanyakan siapa yang masih bersedia mendengar kabar itu darimu. Setelah jendelanya hilang, ponsel tetap sepi.

Di tempat yang pernah kaukenal, orang menghindar atau berbicara seperlunya. Reputasi yang hancur tidak membedakan setiap kesalahan dengan adil, tetapi ada perbuatan nyata yang tidak dapat kausangkal hanya karena kini rasanya menyakitkan menjadi orang yang dijauhi.

Sore itu kau mengangkat koper terakhirmu ke dalam gerbong kereta antarkota menuju distrik tempat tak seorang pun mengenal nama kampusmu. Saat kereta mulai bergerak meninggalkan peron, kau menyelipkan ponsel yang bisu ke saku mantel dan menatap tiket sewa kamar bulanan di tanganmu."""

    # ┌─ ENDING · E-SI-12 · Figuran yang Baik  [Romantis · host Y/C]
    # │ KAPAN   : pemain berhenti memanipulasi dan membantu heroine pulih; mereka lepas dari Koita dan berdiri sendiri
    # │ ISI SKRG: lolos lewat kebaikan; deviasi lahir dari orang-orang yang bebas
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-12"] = """Sistem lama diam sebelum membacakan hasil. Orang-orang yang pernah diletakkan naskah di sekitar Koita telah memilih kehidupan sendiri, bukan karena menjadi milikmu, melainkan karena akhirnya memiliki ruang untuk menginginkan hal lain.

Kau membantu tanpa meminta cinta sebagai imbalan. Ada pertolongan yang diteruskan orang lain, pemulihan yang tetap sulit, dan penolakan yang harus kauhormati. Perubahan itu cukup nyata untuk melewati ambang yang selama ini menakutkanmu.

Kau dinyatakan lolos. Begitu suara Sistem menghilang dari kepalamu, layar ponsel di tanganmu menyala menampilkan pesan di grup makan malam yang menanyakan apakah kau mau mampir membeli minuman dingin sebelum menyusul mereka ke kedai."""

    # ┌─ ENDING · E-SI-13 · Kebaikan yang Tidak Dihitung  [Buruk · host Y/C]
    # │ KAPAN   : pemain berbuat baik tetapi deviasi kurang
    # │ ISI SKRG: mati, tetapi dunia yang ditinggalkan lebih baik
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-13"] = """Kau telah membantu, tetapi tidak cukup menyimpangkan kisah menurut perhitungan Sistem. Mendengar kedua hal itu dinyatakan bersamaan membuatmu ingin tertawa dan marah sekaligus. Kebaikan tidak pernah dijanjikan sebagai perlindungan oleh kontrak ini.

Orang yang kaupertahankan tetap hidup. Ada yang berani mencari bantuan, ada yang terbebas dari orang yang memanfaatkannya, ada yang akhirnya dapat tidur tanpa takut. Semua itu nyata, bahkan ketika Sistem menyebut hasil akhirnya gagal.

Pada meja kedai yang sudah dipesan untuk merayakan kelulusan sore itu, satu kursi tetap kosong sampai makanan di piring mulai dingin. Teman-teman yang dulu pernah kaubantu bertahan masih terus menelepon nomormu ketika kabar dari rumah sakit akhirnya masuk ke ponsel salah seorang dari mereka."""

    # ┌─ ENDING · E-SI-14 · Jauh dari Panggung  [Khusus · host Y/C]
    # │ KAPAN   : pemain di kota atau negara lain saat wisuda
    # │ ISI SKRG: lolos atau gagal tanpa menyaksikan wisuda
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-14"] = """Saat wisuda Kouseikan berlangsung, kau berada jauh dari kampus. Jam setempat menunjukkan waktu yang berbeda, tetapi kontrak tidak mengenal keterlambatan karena jarak. Jendela biru muncul di atas hari yang telah kaususun seperti hari biasa.

Hasil evaluasi tetap mengikuti apa yang sungguh berubah selama tiga tahun, bukan seberapa jauh kau pergi sesudahnya. Jarak memberimu jalan lain, pekerjaan lain, dan orang yang tidak mengenal cerita lama. Ia tidak menghapus keputusan yang telah membawamu ke saat ini.

Kau berhenti melangkah di tengah penyeberangan jalan kota asing itu ketika deretan huruf biru membentang di depan matamu. Orang-orang berlalu-lalang melewati bahumu dalam bahasa yang berbeda, tak seorang pun tahu mengapa kau mendadak berdiri kaku menatap udara kosong."""

    # ┌─ ENDING · E-SI-15 · Pengakuan yang Tidak Dipercaya  [Khusus · host Y/C]
    # │ KAPAN   : rahasia Sistem dibuka luas; dianggap gila
    # │ ISI SKRG: evaluasi terjadi di ruang rawat; hasil mengikuti deviasi
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-15"] = """Di ruang rawat, kau menunggu tanggal yang membuatmu ketakutan. Cerita tentang Sistem telah didengar banyak orang, tetapi tidak menjadi kenyataan yang mereka pahami seperti kau memahaminya. Petugas tetap menanyakan tidur, makanan, rasa aman, dan orang yang ingin kauhubungi.

Ketidakpercayaan mereka tidak memberi kepastian tentang kontrak. Pada jam evaluasi, suara itu datang hanya kepadamu. Hasilnya mengikuti perubahan hidup yang sudah terjadi, tanpa terpengaruh oleh sebutan yang dipakai orang lain untuk menjelaskan keyakinanmu.

Di luar jendela bangsal, bayangan dahan pohon bergeser di atas dinding putih. Tepat ketika jendela Sistem menutup baris terakhirnya, seorang perawat mengetuk pintu dua kali lalu masuk membawa nampan makan siang dan segelas air hangat untukmu."""

    # ┌─ ENDING · E-SI-16 · Tagihan dari Orang Lain  [Buruk · host Y/C]
    # │ KAPAN   : dibunuh atau dilukai fatal oleh NPC
    # │ ISI SKRG: kematian karena tindakan orang yang pernah disakiti
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-16"] = """Kekerasan datang dari seseorang yang pernah kausakiti. Tidak ada kesempatan menyusun penjelasan lengkap, hanya kemarahan yang sudah terlalu jauh dan upaya orang di sekitar menghentikan yang sedang terjadi.

Kau meninggal sebelum evaluasi. Orang yang menyerang tidak mendapat kembali kehidupan yang dirusak dengan menghilangkan hidupmu. Ia juga harus menghadapi akibat tindakannya, sementara orang-orang lain menanggung kejutan kehilangan dan pertanyaan yang tidak selesai.

Sirene ambulans dan mobil patroli memantul di dinding gang basah tempat tubuhmu tergeletak, sementara tanggal evaluasi di jendela Sistem terhenti sebelum sempat mencapai hari wisuda."""

    # ┌─ ENDING · E-SI-17 · Penipu yang Tertipu  [Buruk · host Y/C]
    # │ KAPAN   : hasil yang dinilai hanyalah sandiwara
    # │ ISI SKRG: Sistem harian tertipu sampai akhir; evaluasi tidak
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-17"] = """Kau sampai ke evaluasi dengan keyakinan bahwa susunanmu cukup rapi. Pernyataan cinta telah diucapkan, perpisahan dipentaskan, dan laporan harian tampak mendukung hasil yang kaubutuhkan.

Sistem berhenti pada bagian yang tidak berubah. Perasaan yang hanya diperagakan tidak menjadi nyata karena disepakati beberapa orang, dan hidup Koita tidak sungguh menyimpang hanya karena kau membuatnya tampak demikian dari luar. Untuk pertama kalinya, tidak ada kalimat tambahan yang dapat memperpanjang permainan itu.

Angka deviasi di layar biru itu merosot tajam melewati batas merah tepat di depan matamu. Di sekelilingmu, teman-teman yang kauajak bersandiwara masih mengobrol santai sambil merapikan toga, sebelum akhirnya menjerit ketika tubuhmu ambruk ke lantai aula."""

    # ┌─ ENDING · E-SI-18 · Celah yang Tidak Pernah Dicatat  [Khusus · host Y/C]
    # │ KAPAN   : koita_bebas_naskah benar — nyaris mustahil, lihat bagian 11
    # │ ISI SKRG: pemain lolos tanpa NTR dan tanpa mati, lewat satu celah dalam kontrak yang tidak pernah diantisipasi siapa pun, termasuk Sistem sendiri
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-18"] = """Koita memilih keluar dari peran yang terus disediakan baginya. Ia tidak menyerahkan seluruh cinta kepada satu pemenang, tidak menunggu orang lain menjadi alasan untuk berubah, dan tidak meminta kau menggantikannya sebagai pusat cerita.

Sistem mencoba menghitung dengan ukuran lama, lalu berhenti. Kontraknya mengandaikan seorang MC yang terus menjalankan naskah, sehingga penyimpangan hanya dapat dibaca sebagai sesuatu yang diambil darinya. Kini Koita sendiri telah memilih kehidupan yang tidak mengikuti anggapan itu.

Jendela biru itu berkedip dua kali dengan baris galat yang kosong sebelum padam tanpa ejekan terakhir. Di sebelahmu, Koita merentangkan kedua lengan di bawah langit halaman kampus, lalu menoleh dan bertanya kalian mau makan apa untuk merayakan sore ini."""

    # ┌─ ENDING · E-FO-01 · Jeruji  [Buruk · host Y/C]
    # │ KAPAN   : laporan atau bukti kuat; investigasi tuntas
    # │ ISI SKRG: dipenjara; game berlanjut di Rute Jeruji; evaluasi tetap terjadi di sel
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-01"] = """Laporan dan pemeriksaan akhirnya menjadi perkara yang tidak dapat kauhentikan dengan penyangkalan. Kesaksian didengar, bukti dinilai, dan putusan membawa hidupmu ke balik jeruji.

Korban tidak datang untuk memberikan pengampunan pada hari terakhir. Ia berhak menjaga jarak, meminta perlindungan, dan memilih siapa yang menemaninya menghadapi proses. Pemenjaraanmu tidak serta-merta membuat tidurnya tenang atau menghapus ketakutan yang telah kautinggalkan.

Di dinding sel yang dingin, kau menghitung goresan tanggal yang terus bergerak mendekati hari wisuda angkatanmu. Ketika lampu lorong dipadamkan tepat pukul sembilan malam, hanya tersisa bayangan jeruji besi di lantai dan hitung mundur evaluasi yang masih menyala di sudut matamu."""

    # ┌─ ENDING · E-FO-02 · Dikeluarkan dan Hancur Sosial  [Buruk · host Y/C]
    # │ KAPAN   : bukti cukup untuk kampus, tidak cukup untuk penjara
    # │ ISI SKRG: dikeluarkan; reputasi hancur di semua lingkungan; Rute Luar Kampus
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-02"] = """Keputusan kampus memutus aksesmu kepada ruang yang dahulu begitu mudah kaumasuki. Namamu dihapus dari daftar kegiatan, urusan akademik berhenti, dan teman-teman diberi alasan untuk tidak lagi menganggap kedatanganmu sesuatu yang biasa.

Perkara belum menghasilkan pemenjaraan. Itu tidak mengubah keputusan disiplin menjadi kebohongan atau luka korban menjadi sesuatu yang kurang nyata. Ia tetap menghadapi hari-hari sulit dan kebutuhan akan ruang yang aman tanpa bertemu denganmu.

Saat kau melewati jalan depan gerbang Kouseikan dengan kardus berisi sisa barang lokermu, petugas keamanan langsung melangkah maju memastikan kau tidak berbelok masuk. Dari seberang pagar besi itu, tak seorang pun dari teman lama yang menoleh ke arahmu."""

    # ┌─ ENDING · E-FO-03 · Lolos tapi Dihantui  [Khusus · host Y/C]
    # │ KAPAN   : force_bersih[[korban] bertahan (§10); tidak pernah terbongkar
    # │ ISI SKRG: bebas dari hukum, tidak dari ingatan; korban tetap bisa mendapat Broken Ending
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-03"] = """Tidak ada perkara yang mencapai hukuman. Orang-orang tetap menyapamu, dan kehidupan di luar tampak menerima versi dirimu yang kauperlihatkan. Kebebasan itu tidak membuat peristiwa yang kaulakukan berhenti pernah terjadi.

Korban menghadapi akibatnya tanpa kepastian bahwa orang lain akan memahami. Ada hari yang terlewat, percakapan yang diputus karena terlalu berat, dan rasa aman yang tidak kembali hanya karena ia berhasil tampak tenang. Kau tidak berhak menafsirkan diam sebagai bukti bahwa ia sudah baik-baik saja.

Setiap kali seseorang di meja makan menyebut nama gedung atau tanggal malam itu secara kebetulan, tanganmu yang memegang gelas langsung menegang. Di koridor seberang, sosok yang pernah kaulukai langsung berbalik turun melalui tangga darurat begitu melihat bayanganmu dari ujung lorong."""

    # ┌─ ENDING · E-FO-04 · Mengaku dan Menjalani Proses  [Netral · host Y/C]
    # │ KAPAN   : pelaku mengaku
    # │ ISI SKRG: proses hukum; tidak ada pengampunan otomatis; korban menentukan jaraknya sendiri
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-04"] = """Kau mengaku dan berhenti meminta orang lain menjaga versi yang melindungimu. Proses hukum tetap berjalan dengan pertanyaan, pemeriksaan, dan akibat yang tidak dapat ditawar hanya karena pengakuan itu akhirnya datang.

Korban menerima kabar melalui orang yang ia pilih untuk mendampingi. Ia tidak berkewajiban menemuimu, mendengar penyesalanmu, atau menjawab surat. Pengakuanmu baru menghentikan sebagian penyangkalan; ia belum memperbaiki hidup yang telah kaurusak.

Pagi itu kau duduk di bangku kayu ruang tunggu pemeriksaan sambil memegang map panggilan resmi di pangkuanmu. Ketika pintu besi di ujung ruangan terbuka dan namamu dipanggil petugas, kau berdiri dan melangkah masuk sendirian."""

    # ┌─ ENDING · E-FO-05 · Buron  [Buruk · host Y/C]
    # │ KAPAN   : pelaku lari
    # │ ISI SKRG: hidup bersembunyi di kota lain; quest gagal; Sistem menghukum pembangkangan
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-05"] = """Kau pergi ketika perkara mulai mengejarmu. Kota lain tidak membuat kehidupan baru terasa bersih; setiap percakapan biasa dipenuhi takut ditanya terlalu jauh tentang asalmu.

Di tempat yang ditinggalkan, korban dan orang yang mendampingi tetap menjalani proses tanpa kehadiranmu. Kepergianmu menambah penundaan dan ketidakpastian, bukan membatalkan yang telah terjadi. Orang-orang yang pernah membela namamu harus menghadapi kenyataan bahwa kau memilih menghindar.

Di kamar penginapan murah dekat pelabuhan yang tirainya tak pernah dibuka, peringatan merah dari Sistem berkedip makin cepat di sudut pandanganmu. Setiap kali ada sirene melintas di jalan raya bawah, kau langsung mematikan lampu dan duduk membeku di tepi kasur."""

    # ┌─ ENDING · E-FO-06 · Kakak yang Tidak Menunggu Polisi  [Buruk · host Y/C]
    # │ KAPAN   : Haruto, Kuroiwa, atau kerabat lain tahu lebih dulu
    # │ ISI SKRG: kerabat korban membalas sendiri; pemain cedera berat atau mati (E-SI-16); pembalas ikut ditangkap
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-06"] = """Orang yang menyayangi korban mengetahui apa yang terjadi dan bertindak sebelum proses resmi dapat berjalan. Kemarahan berubah menjadi kekerasan yang tidak berhenti ketika seseorang berteriak meminta tolong.

Kau mengalami cedera berat, dan kabar tentang keadaanmu kini berjalan bersama kabar penangkapan orang yang membalas. Korban kembali dikelilingi pertanyaan, kali ini juga tentang seseorang yang mungkin selama ini menjadi tempatnya merasa aman.

Di balik tirai plastik ruang gawat darurat, bunyi monitor detak jantung berdengung bersahutan dengan suara langkah dua petugas polisi yang sudah menunggu di luar pintu bangsalmu dengan map pemeriksaan di tangan."""

    # ┌─ ENDING · E-FO-07 · Saksi yang Memeras  [Khusus · host Y/C]
    # │ KAPAN   : saksi (Kaichi atau Meisa) menyimpan bukti
    # │ ISI SKRG: pemain diperas sampai akhir game
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-07"] = """Seseorang yang mengetahui kekerasan itu memilih memerasmu. Ia menahan apa yang diketahuinya sebagai ancaman, meminta bayaran atau bantuan, lalu membiarkanmu menunggu kapan tuntutan berikutnya datang.

Kau mulai mengatur hidup berdasarkan pesan yang ditakuti. Sementara itu, korban belum mendapatkan keadilan dari pengetahuan yang diperdagangkan tersebut. Perbuatannya dijadikan alat tawar oleh orang lain, dan penderitaannya kembali ditempatkan setelah kepentingan orang yang memegang kuasa.

Pada malam sebelum wisuda, ponselmu kembali bergetar menampilkan foto potongan bukti beserta lokasi pertemuan baru untuk besok sore. Kau menatap layar itu di kamar yang gelap dengan dompet yang sudah nyaris kosong di atas meja."""

    # ┌─ ENDING · E-FO-08 · Kasus yang Dibuka Kembali  [Khusus · host Y/C]
    # │ KAPAN   : bukti ditemukan belakangan
    # │ ISI SKRG: epilog: kasus dibuka setelah wisuda; hidup yang tampak selamat runtuh
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-08"] = """Sesudah wisuda, ketika kau mulai mengira masa lalu sudah cukup jauh, panggilan pemeriksaan datang. Keterangan atau bukti yang ditemukan belakangan membuat perkara dibuka kembali.

Kehidupan yang tampak mapan berhenti di tengah rencana biasa. Kau harus menjelaskan hal yang dahulu berhasil tidak dijawab. Orang-orang yang mengenalmu kemudian melihat riwayat yang selama ini tidak pernah masuk ke cerita tentang dirimu.

Pagi itu dua penyidik bersetelan gelap sudah berdiri menunggu di depan pintu apartemenmu saat kau baru saja hendak berangkat kerja. Ketika mereka menunjukkan surat panggilan resmi dengan tanggal kejadian dari masa kuliahmu, tas kerja di tanganmu terasa mendadak berat."""

    # ┌─ ENDING · E-FO-09 · Kejahatan Berantai  [Buruk · host Y/C]
    # │ KAPAN   : lebih dari satu kejahatan; satu membongkar yang lain
    # │ ISI SKRG: semua terbongkar bersamaan
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-09"] = """Satu perkara membuka jalan kepada perkara lain. Orang-orang yang semula mengira pengalamannya terpisah akhirnya mengetahui bahwa ada orang lain yang juga menyimpan ketakutan dan pertanyaan serupa.

Pemeriksaan tidak lagi berhenti pada penjelasan yang kausiapkan untuk satu kejadian. Setiap tindakan tetap perlu dinilai dengan fakta masing-masing. Kau kehilangan kemampuan memisahkan orang-orang yang dirugikan ke dalam ruang kebisuan yang berbeda.

Di atas meja ruang pemeriksaan, tiga map perkara dengan nama pelapor berbeda diletakkan berjajar tepat di hadapanmu. Ketika penyidik membuka map kedua dan membacakan tanggal yang sama persis dengan alibimu pada kasus pertama, kau tak lagi mampu mengangkat kepala."""

    # ┌─ ENDING · E-FO-10 · Skorsing dan Catatan  [Netral · host Y/C]
    # │ KAPAN   : hanya kejahatan ringan–sedang
    # │ ISI SKRG: skorsing satu semester dan catatan polisi; hidup berjalan dengan bekas
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-10"] = """Keputusan akhirnya berupa skorsing satu semester dan catatan resmi yang tidak dapat diperlakukan sebagai urusan administrasi biasa. Perkara dalam akhir ini tidak dinilai sebagai kekerasan seksual, tetapi tetap melibatkan tindakan yang merugikan orang lain.

Kau meninggalkan kampus sementara teman-teman meneruskan jadwal mereka. Ada kesempatan kembali dengan syarat yang jelas, dan ada hubungan yang tidak akan kembali hanya karena masa skorsing selesai.

Ketika semester baru dimulai dan kau kembali mengantre di loket registrasi ulang, lembar persetujuan di tanganmu harus melewati cap pengawasan khusus sebelum diterima petugas. Di koridor belakangmu, teman-teman seangkatanmu sudah lebih dulu masuk ke ruang seminar akhir."""

    # ┌─ ENDING · E-FO-11 · Saksi di Ambang Pintu  [Buruk · host Y/C]
    # │ KAPAN   : Force disaksikan Koita; korban melapor sendiri, atau trust_koita sudah rendah sehingga Koita sendiri mencari bantuan
    # │ ISI SKRG: kasus terkuat; penjara hampir pasti; nasib Koita sendiri mengikuti trust_koita — ia bertindak sebagai saksi (E-KO-20) atau ikut dimintai kesaksian sambil membeku di dalam (E-KO-19)
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-11"] = """Koita berada di ambang pintu ketika memahami bahwa yang terjadi bukan salah paham atau hubungan pribadi yang tidak boleh dicampurinya. Pengetahuan itu mengubah wajahnya sebelum ia sanggup bergerak.

Perkara kemudian mendapat laporan dan kesaksian yang kuat. Pada bagian yang dapat diucapkan, Koita menjawab; pada bagian yang membuatnya membeku, ia perlu waktu dan pendampingan. Korban tidak kehilangan hak dipercaya hanya karena saksi juga mengalami ketakutan.

Di ruang pemeriksaan, Koita duduk di kursi saksi tanpa sekali pun menoleh ke arah tempatmu berdiri ketika kamu mencoba memanggil namanya. Begitu petugas selesai mencatat keterangannya dan menutup pintu ruangan, borgol di pergelangan tanganmu terasa semakin dingin."""

    # ┌─ ENDING · E-FO-12 · Kurungan Tanpa Jeruji  [Khusus · host Y/C]
    # │ KAPAN   : korban tidak melapor dan tetap terikat pada pemain lewat takut, ancaman, atau ketergantungan
    # │ ISI SKRG: dihitung Sistem sebagai lepas dari Koita; tidak pernah ditulis sebagai cinta; bisa retak kapan saja lewat sahabat, bukti, atau korban sendiri (E-FO-08)
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-12"] = """Dari luar, korban masih berada dekatmu. Ia menjawab pesan, datang ketika diminta, atau mengatakan semuanya baik-baik saja pada saat orang bertanya terlalu cepat. Orang yang hanya melihat permukaan mungkin mengira hubungan itu bertahan.

Di dalamnya ada takut, ancaman, atau ketergantungan yang membuat pilihan terasa sempit. Kedekatan itu bukan persetujuan yang bebas, dan keberadaannya di sisimu bukan akhir romantis. Ia tetap seseorang yang memiliki keinginan sendiri, meskipun kau terus memperlakukan ketidakmampuannya pergi sebagai kemenangan.

Di meja kafe tempat kalian duduk berdua, jemarinya langsung gemetar dan menarik diri ke bawah meja setiap kali kau meraih cangkir terlalu cepat. Sementara itu dari balik kaca jendela seberang jalan, sahabatnya masih berdiri memperhatikan kalian sambil menggenggam ponsel yang siap melakukan panggilan."""

    # ┌─ ENDING · E-FO-13 · Kebetulan yang Datang Tepat Waktu  [Buruk · host Y/C]
    # │ KAPAN   : plot armor membawa Koita sebelum terjadi
    # │ ISI SKRG: percobaan gagal; korban berlindung pada Koita; pemain menanggung percobaan itu: laporan, skorsing, rumor
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-13"] = """Koita datang sebelum percobaan itu menjadi kekerasan yang hendak kaulakukan. Ia melihat ketakutan di wajah orang yang berada bersamamu dan berhenti mendengar alasanmu sebagai penjelasan yang harus diterima lebih dulu.

Korban mendapat jarak untuk meminta pertolongan. Koita tetap bersamanya sampai ada orang lain yang ia percaya. Kedatangan tepat waktu itu tidak menghapus ancaman yang telah terjadi, tetapi memberi kesempatan agar kejadian hari itu tidak diteruskan sesuai kehendakmu.

Keesokan paginya surat panggilan komite disiplin dan skorsing sementara sudah menempel di lokermu, sementara Koita beserta dua teman korban berdiri berjaga di depan ruang administrasi sampai petugas keamanan datang menjemputmu."""

    # ┌─ ENDING · E-FO-14 · Dua Orang yang Diam  [Khusus · host Y/C]
    # │ KAPAN   : Koita menyaksikan tetapi diam karena takut, malu, atau diancam
    # │ ISI SKRG: pelaku bebas dari hukum, tetapi dua orang tahu; korban dan Koita sama-sama hancur dalam diam
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-14"] = """Koita mengetahui apa yang terjadi dan tidak melaporkannya. Takut, malu, dan ancaman membuat kalimat yang telah disiapkannya berhenti sebelum sampai kepada orang lain. Korban pun belum berada di tempat yang cukup aman untuk berbicara.

Kau tetap bebas dari proses hukum dalam akhir ini. Di luar, hubungan sosial tampak terus berjalan. Di dalam dua kehidupan lain, ada kejadian yang kembali melalui tidur, tempat, dan pertemuan yang tidak lagi terasa biasa.

Setiap kali kalian bertiga tidak sengaja berada di koridor yang sama, percakapan langsung terputus dan Koita segera menunduk menatap lantai dengan wajah pucat. Di ujung lorong, korban berbalik masuk ke tangga samping tanpa suara, meninggalkanmu berdiri di tengah keheningan yang kaku."""

    # ┌─ ENDING · E-FO-15 · Pembalikan yang Terbongkar  [Buruk · host C]
    # │ KAPAN   : jalur manipulasi pembalikan Chiasa (06_Chiasa.md §14); framing runtuh
    # │ ISI SKRG: fitnah terbongkar lewat bukti, saksi, atau Shiori/Hanabusa; Chiasa menanggung Force sekaligus fitnah dan obstruksi, konsekuensi lebih berat
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-15"] = """Cerita yang menjadikan Koita tertuduh akhirnya runtuh. Keterangan yang diperiksa tidak lagi mendukung versi Chiasa, dan orang-orang yang dahulu membela dengan yakin harus menghadapi apa yang telah ikut mereka sebarkan.

Kekerasan yang dilakukan Chiasa tidak menghilang di balik terbongkarnya fitnah. Kini proses juga menyangkut tuduhan palsu dan upaya menghalangi kebenaran. Koita perlu mendapatkan kembali namanya, sementara orang lain yang dirugikan tetap mempunyai luka yang tidak dapat dirangkum menjadi skandal keluarga.

Daisuke dan Yoshie datang ke ruang tunggu kantor pemeriksaan dengan wajah pucat dan bahu yang merosot, hanya menyerahkan tas berisi pakaian ganti tanpa memelukmu. Ketika Koita keluar dari pintu sebelah didampingi penasihat hukumnya, ia melewati kursimu tanpa menoleh sedikit pun."""
