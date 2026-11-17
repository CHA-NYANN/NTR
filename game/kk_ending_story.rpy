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

Mereka mulai bersama tanpa menganggap penantian sebagai bukti bahwa hubungan ini pasti berhasil. Pada hari Miyuki pulang terlalu lelah untuk bersikap manis, Koita tetap datang. Ia belajar bahwa dipilih seseorang juga berarti hadir pada saat dirinya tidak sedang dibuat merasa istimewa."""

    # ┌─ ENDING · E-KO-02 · Dipilih: Nagisa  [Koita · host Y/C]
    # │ KAPAN   : harapan_koita Nagisa tegak
    # │ ISI SKRG: teman masa kecil yang akhirnya dijawab
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-02"] = """Nagisa sudah menyiapkan kemarahan untuk menutupi apa pun jawaban Koita. Namun ketika ia akhirnya menyebut cinta dengan jelas, seluruh kalimat tajam itu mendadak tidak berguna. Ia hanya bertanya apakah Koita sungguh memahami yang sedang dikatakannya.

Koita tidak menjawab dengan kisah boneka kelinci atau masa kecil. Ia menyebut Nagisa yang sekarang: keras kepala, mudah khawatir, dan berhak pergi jika ia kembali menggantungnya. Barulah Nagisa menangis, kesal karena tangisnya datang sebelum ia sempat terlihat anggun.

Koko tetap duduk di kamarnya, kini tanpa tugas menjamin masa depan. Mereka masih bertengkar tentang waktu, pesan yang terlambat, dan hal-hal kecil yang dahulu dipendam demi mempertahankan kedekatan. Bedanya, Koita tidak lagi menjadikan teman masa kecil sebagai alasan untuk menghindari nama hubungan mereka."""

    # ┌─ ENDING · E-KO-03 · Dipilih: Harumi  [Koita · host Y/C]
    # │ KAPAN   : Harumi tahap ≤ 2; Koita memilihnya
    # │ ISI SKRG: variabel tetap
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-03"] = """Harumi meminta Koita mengulang pengakuannya. Bukan karena ia tidak mendengar, melainkan karena selama ini terlalu banyak perkataan baik yang bisa berarti apa saja. Koita mengulang dengan kalimat lebih pendek, sampai tidak ada bagian yang perlu ditafsirkan.

Ia memilih Harumi. Ia ingin menjadi pasangannya. Ia memahami bahwa jawaban Harumi belum tentu sama.

Harumi diam lama, lalu mengatakan ya dengan suara yang nyaris hilang di antara rak buku. Setelah itu ia justru membicarakan batas waktunya: penelitian, tidur, hal-hal yang tidak akan ia korbankan untuk membuktikan kasih sayang. Koita mendengarkan tanpa menawar. Variabel tetap yang akhirnya mereka pertahankan bukan seseorang yang selalu mengalah, melainkan hak keduanya untuk tetap menjadi diri sendiri."""

    # ┌─ ENDING · E-KO-04 · Dipilih: Moeka  [Koita · host Y/C]
    # │ KAPAN   : Moeka selamat; hatinya ke Koita
    # │ ISI SKRG: Koita belajar menepati janji
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-04"] = """Moeka terlambat dua belas menit pada kencan pertama mereka. Ia datang dengan napas putus-putus dan lelucon yang disiapkan untuk mendahului teguran. Koita mengatakan ia sudah membaca pesan keterlambatannya, lalu bertanya apakah ia sempat makan.

Perhatian sederhana itu tidak menyembuhkan semua yang pernah terjadi. Keluarga Moeka masih memerlukan bantuan, beasiswanya masih menuntut kerja, dan ada pagi ketika bangun terasa jauh lebih berat daripada yang terlihat dari fotonya. Namun Koita berhenti menawarkan janji besar yang bisa ia lupakan setelah suasana membaik.

Ia datang pada waktu yang disepakati. Jika tidak bisa, ia memberi kabar. Moeka belajar mengatakan sedang tidak baik tanpa harus tertawa sesudahnya. Cinta mereka tumbuh di antara hal-hal biasa itu, dalam hidup yang masih boleh sulit dan tetap layak dijalani."""

    # ┌─ ENDING · E-KO-05 · Dipilih: Shiori  [Koita · host Y/C]
    # │ KAPAN   : cinta Koita tumbuh di S08
    # │ ISI SKRG: lawan yang ia kira tak tersentuh
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-05"] = """Shiori menolak undangan makan malam yang disusun seperti kesepakatan keluarga. Jika Koita ingin menemuinya, ia bisa mengajaknya sendiri, dengan tempat dan jam yang jelas. Koita melakukannya, lalu datang dua puluh menit terlalu awal karena gugup.

Di hadapannya, Shiori tidak menjadi hadiah untuk keberanian seorang pemuda baik. Ia mempertanyakan kebiasaannya, menolak kecenderungannya meminta persetujuan semua orang, dan tertawa ketika ia akhirnya mampu membantah dengan alasan yang jujur. Ketertarikan mereka yang tumbuh sejak pertemuan lama kini punya ruang untuk menjadi sesuatu yang dipilih.

Koita tetap canggung di rumah Saionji. Shiori tetap harus menghadapi tuntutan keluarganya. Tetapi saat memperkenalkannya, ia menyebut nama dan hubungan mereka sendiri sebelum siapa pun sempat menawarkan gelar yang lebih menguntungkan."""

    # ┌─ ENDING · E-KO-06 · Dipilih: Chiasa  [Koita · host Y/C]
    # │ KAPAN   : Koita Success (NPC atau host)
    # │ ISI SKRG: tabu saudara tiri; lihat file 06
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-06"] = """Rumah Amamiya kehilangan kemudahan lamanya ketika Koita dan Chiasa mengakui bahwa perasaan mereka tidak lagi bisa disembunyikan di balik panggilan keluarga. Tak ada pengumuman manis yang membuat semua orang langsung memahami. Ada pintu yang ditutup, percakapan yang ditunda, dan orang tua yang perlu waktu untuk menerima bahwa mereka sedang diminta mendengar sesuatu yang sulit.

Koita berhenti membiarkan Chiasa mengucapkan seluruh keinginan sementara ia berlindung dalam diam. Ia menyebut pilihannya sebagai pilihannya sendiri. Chiasa, untuk pertama kalinya, tidak menyambut itu dengan janji bahwa ia akan selalu menyediakan segala sesuatu di rumah.

Mereka menghadapi akibat sosial dan keluarga tanpa menganggap penolakan orang lain bukti bahwa cinta mereka lebih luhur. Hubungan itu baru bisa berjalan ketika keduanya belajar bahwa tinggal bersama tidak memberi hak untuk menentukan hidup yang lain."""

    # ┌─ ENDING · E-KO-07 · Sendiri  [Netral · host Y/C]
    # │ KAPAN   : semua heroine menjauh; Koita tidak runtuh
    # │ ISI SKRG: kehilangan semuanya, mulai bertumbuh
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-07"] = """Pada malam pertama tanpa pesan dari siapa pun, Koita membuat dua cangkir teh. Ia menatap cangkir kedua cukup lama, kemudian menuangnya kembali sebelum dingin. Esoknya ia hanya membuat satu.

Tak ada yang kembali karena melihat ia mulai membaik. Ia mengembalikan buku, meminta maaf kepada orang yang bersedia mendengar, dan menerima bahwa beberapa permintaan maaf tidak dibalas. Hari-hari itu tidak menyenangkan, tetapi tidak semuanya kosong. Ada kuliah yang masih bisa diselesaikan, janji konseling yang bisa ditepati, dan tulisan yang tak harus membuat pembacanya mencintai dirinya.

Ketika seseorang bertanya apakah ia sedang sendiri, Koita menjawab ya. Ia tidak tertawa untuk menutupinya. Untuk pertama kalinya, kata itu terdengar seperti keadaan yang sedang dijalani, bukan vonis tentang seluruh sisa hidupnya."""

    # ┌─ ENDING · E-KO-08 · Tetap Menggantung  [Buruk · host Y/C]
    # │ KAPAN   : pola tidak pernah terbongkar
    # │ ISI SKRG: pola lama berlanjut dengan korban baru
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-08"] = """Beberapa orang berhenti menunggu, tetapi tidak pernah cukup banyak yang berbicara satu sama lain untuk melihat pola secara utuh. Koita menyebut semuanya perubahan wajar setelah kuliah. Ia terdengar sedih dengan cara yang membuat orang baru ingin menghiburnya.

Di tempat kerja pertamanya ada seseorang yang menyukai buku, seseorang yang sering lupa makan, seseorang yang merasa akhirnya diperhatikan. Koita mengingat detail kecil tentang mereka. Ia masih bisa sangat baik. Justru itu yang membuat pesan-pesannya terasa sulit dipertanyakan.

Saat ditanya apakah ia menyukai seseorang, ia mengusap tengkuk dan mengatakan belum mengerti perasaannya sendiri. Orang di seberang meja tersenyum, mengira sedang dipercaya mendengar sebuah keraguan yang istimewa. Kalender berganti; penantian hanya berpindah pemilik."""

    # ┌─ ENDING · E-KO-09 · Hancur  [Buruk · host Y/C]
    # │ KAPAN   : pola_koita_publik tinggi; atau E-SH-09
    # │ ISI SKRG: lingkungan menjauh setelah sifat aslinya terbukti
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-09"] = """Koita pertama-tama kehilangan hak untuk menjelaskan semuanya sebagai salah paham. Pesan yang serupa, janji yang dibiarkan bersinggungan, dan cerita yang berbeda kepada orang berbeda akhirnya dibaca bersama. Setiap alasan yang dahulu terdengar masuk akal kini memiliki pembanding.

Orang-orang tidak serentak membencinya. Ada yang marah, ada yang malu pernah membelanya, ada yang cukup lelah untuk pergi tanpa berdebat. Koita mendapati bahwa kehilangan akses kepada seseorang bisa lebih sunyi daripada pertengkaran.

Di klub, kursi sebelahnya tidak lagi diperebutkan. Ia pulang membawa naskah yang tidak diminta siapa pun. Yang terbongkar memang perbuatannya sendiri; akibatnya tetap menyakitkan, dan rasa sakit itu tidak memberinya hak meminta orang-orang yang dilukai kembali untuk merawatnya."""

    # ┌─ ENDING · E-KO-10 · Koita Membalas  [Buruk · host Y/C]
    # │ KAPAN   : manuver balik berhasil; pemain kalah perang reputasi
    # │ ISI SKRG: Koita merebut balik heroine dan menjatuhkan pemain di mata semua orang
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-10"] = """Koita berhenti datang kepadamu untuk meminta penjelasan. Ia mulai berbicara langsung kepada orang-orang yang selama ini kautafsirkan untuknya. Ketika kisah mereka dipertemukan, ada perbuatanmu yang tak lagi bisa ditutupi oleh citra penolong.

Kedekatan yang kaurebut berbalik meninggalkanmu. Beberapa orang memilih kembali berada di sisinya; yang lain sekadar menolak meneruskan hubungan denganmu. Dalam percakapan kampus, namamu menjadi jeda canggung sebelum seseorang mengganti topik.

Koita menang dalam perang reputasi itu. Ia berdiri kembali di tengah kelompok yang pernah kaubayangkan sudah menjadi milikmu. Namun ada sesuatu yang lebih terukur dalam caranya melihat reaksi orang sekarang. Kekalahanmu tidak menjamin ia belajar mencintai dengan lebih jujur; ia telah belajar seberapa besar kuasa yang dimiliki orang yang dipercaya lebih dahulu."""

    # ┌─ ENDING · E-KO-11 · Penulis yang Jujur  [Netral · host Y/C]
    # │ KAPAN   : K19 dibantu jujur; K20 diisi kebenaran sebagian
    # │ ISI SKRG: berhenti menggantung; menulis novel tentang tokoh yang tidak pernah memilih
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-11"] = """Novel Koita dibuka dengan seorang tokoh yang mengaku tak pernah memilih siapa pun. Pada draf lama, kalimat itu terdengar sedih. Pada naskah yang akhirnya ia kirim, pembaca diberi cukup ruang untuk melihat siapa yang membayar harga dari pengakuan tersebut.

Koita mengerjakannya setelah skripsi, setelah percakapan yang tidak seluruhnya menyenangkan, setelah ia mulai membedakan memahami diri dari membenarkan diri. Ia menghapus bagian yang terlalu jelas meminjam luka orang lain hanya untuk membuat tokohnya tampak dalam.

Tidak semua orang membaca bukunya. Tidak semua yang membaca menyukainya. Ia menyimpan tanggapan yang keras bersama yang baik dan tetap menulis halaman berikutnya. Kali ini pekerjaan itu tidak bergantung pada keyakinan bahwa setiap orang di sekelilingnya harus terus menyayanginya."""

    # ┌─ ENDING · E-KO-12 · Pergi  [Netral · host Y/C]
    # │ KAPAN   : K23-A didukung pergi
    # │ ISI SKRG: menerima tawaran penerbit di kota lain dan meninggalkan semuanya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-12"] = """Tawaran penerbit itu berubah menjadi tiket, kontrak magang, dan alamat kamar sewaan yang belum pernah Koita lihat langsung. Sampai malam sebelum berangkat, ia masih punya kesempatan mengatakan terlalu banyak yang harus ditinggalkan. Ia menutup kopernya juga.

Di kota baru tidak ada orang yang tahu makanan kesukaannya atau kisah boneka masa kecil. Ia harus memperkenalkan diri tanpa bantuan kenangan bersama. Pekerjaannya lebih banyak merapikan naskah orang lain daripada menulis miliknya sendiri.

Kadang ia mengirim kabar. Pesannya tidak lagi diakhiri pertanyaan yang memancing orang mengatakan rindu. Koita belum tentu berubah sepenuhnya, tetapi jarak membuat kebiasaannya terlihat. Untuk bertahan di tempat baru, ia harus belajar meminta sesuatu dengan jelas dan menerima ketika jawabannya tidak."""

    # ┌─ ENDING · E-KO-13 · Protagonis yang Terbangun  [Khusus · host Y/C]
    # │ KAPAN   : koita_tahu_naskah percaya
    # │ ISI SKRG: Koita sengaja melawan plot armor-nya; pilihannya kini benar-benar miliknya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-13"] = """Koita menguji keyakinan paling mengerikan yang pernah ia terima: bahwa sebagian hidupnya mungkin disusun agar orang terus jatuh cinta. Ia tidak bisa membuktikan setiap kebetulan. Ia bisa berhenti memakainya sebagai alasan bahwa suatu pertemuan pasti dimaksudkan untuk dirinya.

Ketika hujan menahan seseorang di sebelahnya, ia menanyakan apakah orang itu ingin ditinggal sendiri. Ketika kesempatan pengakuan terasa terlalu sempurna, ia memberi ruang untuk jawaban yang tidak sempurna. Beberapa orang pergi, dan dunia tidak runtuh untuk mengantar mereka kembali.

Sistem boleh menyebutnya protagonis. Koita mulai menolak perlakuan yang menempatkan orang lain sebagai hadiah. Pada hari ia memilih jalan yang membuatnya pulang sendirian, tak ada cahaya atau musik kemenangan. Hanya keputusan kecil yang akhirnya ia percaya sebagai miliknya."""

    # ┌─ ENDING · E-KO-14 · Persahabatan yang Diakhiri  [Netral · host Y/C]
    # │ KAPAN   : Koita tahu semua manipulasi pemain; tidak runtuh
    # │ ISI SKRG: ia memutus pemain dengan tenang dan tidak pernah kembali
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-14"] = """Koita mengembalikan barang-barangmu dalam satu tas. Tidak ada surat panjang, tidak ada daftar kebaikan yang diminta dibayar. Ia sudah mengetahui cukup banyak untuk berhenti menanyakan apakah kau sebenarnya bermaksud baik.

Ia mengatakan hubungan kalian selesai. Jika ada urusan yang belum beres, ia akan menyelesaikannya melalui orang lain. Setelah itu ia pergi sebelum percakapan berubah menjadi permintaan agar ia mendengarkan satu alasan lagi.

Kau masih melihatnya sesekali. Ia bisa tertawa bersama orang lain, tampak lelah, atau berjalan sendiri. Tidak satu pun keadaan itu menjadi undangan untuk mendekat. Keputusan paling tegas yang pernah ia buat tentangmu adalah menolak membiarkan kehadiranmu terus menentukan hari-harinya."""

    # ┌─ ENDING · E-KO-15 · Toga yang Tidak Dipakai  [Buruk · host Y/C]
    # │ KAPAN   : K19 disabotase atau Koita runtuh di Tahun 3
    # │ ISI SKRG: Koita gagal lulus tepat waktu; evaluasi tetap di tanggal wisuda angkatannya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-15"] = """Toga Koita tetap terbungkus ketika foto wisuda angkatannya mulai memenuhi grup. Skripsinya tidak selesai pada waktunya. Di antara draf yang rusak, janji bimbingan yang terlewat, dan hari-hari ketika membuka laptop terasa mustahil, tenggat itu akhirnya lewat juga.

Sistem tetap melakukan evaluasi pada hari yang sudah ditentukan. Kalendernya tidak menunggu seseorang yang kehilangan kemampuan mengikuti kalender sendiri. Kau menerima hasil sementara Koita menatap pesan administrasi tentang semester tambahan.

Gagal lulus tepat waktu bukan akhir seluruh hidupnya. Namun saat itu ia belum mampu melihat lebih jauh daripada nama-nama yang telah pindah ke daftar alumni. Ketika ditanya kapan menyusul, ia mengatakan belum tahu. Ia tidak punya tenaga untuk menambahkan senyum yang biasanya membuat orang merasa pertanyaan mereka tidak melukai."""

    # ┌─ ENDING · E-KO-16 · Semua Pergi  [Khusus · host Y/C]
    # │ KAPAN   : orbit_koita 0; sebagian besar heroine pergi sendiri (pola terbongkar atau memilih mandiri); runtuh_koita ≥ 80; tanpa penopang
    # │ ISI SKRG: NTR sempurna: tidak ada satu pun yang tersisa. Koita berhenti menulis dan kuliah, mengurung diri, kena mental; ditulis lewat kondisi dan dampaknya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-16"] = """Nama-nama itu tidak hilang dari ponsel Koita. Mereka hanya berhenti menjadi orang yang bisa ia hubungi tanpa memikirkan alasan. Satu per satu memilih kehidupan yang tak lagi berpusat padanya, sampai tidak ada lagi kursi yang sengaja disisakan.

Ia berhenti datang ke kelas. Naskahnya tertutup berhari-hari, lalu berminggu-minggu. Orang mengira ia sedang menghindari malu; di dalam kamar, hal sesederhana mandi dan menjawab satu pesan sudah memerlukan tenaga yang sulit ia kumpulkan.

Tak ada penopang yang berhasil menjangkaunya sebelum hari evaluasi. Kehancuran itu tidak membuat orang-orang wajib kembali, dan tidak membuktikan bahwa mereka salah pergi. Tetapi di balik hasil sempurna yang dicatat Sistem, ada seseorang yang kehilangan keseharian, masa depan yang pernah bisa dibayangkan, dan cara meminta tolong tanpa merasa sedang meminta cinta."""

    # ┌─ ENDING · E-KO-17 · Pusat yang Berpindah  [Khusus · host Y/C]
    # │ KAPAN   : orbit_koita 0; minimal tiga heroine kini di orbit pemain, karena memilih pemain atau terikat lewat ancaman atau Force ; Koita tahu; runtuh_koita ≥ 80
    # │ ISI SKRG: NTR sempurna: lingkaran yang dulu berputar di sekitar Koita kini berputar di sekitar pemain, dan Koita menjadi figuran di ceritanya sendiri. Slide tiap heroine berbeda: yang memilih pemain tampak bahagia, yang dipaksa tampak hancur
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-17"] = """Koita melihat kelompok itu dari luar. Nama yang dulu paling sering disebut dalam rencana mereka kini namamu. Ia datang terlalu akhir untuk percakapan, tak tahu lelucon baru, dan berhenti ditanya apakah bisa ikut sebelum sebuah jadwal ditetapkan.

Namun wajah-wajah di dekatmu tidak bisa dibaca sebagai satu kemenangan. Orang yang memilihmu bebas bisa tertawa dan pergi tanpa takut. Pada orang yang bertahan karena ancaman, yang terlihat adalah kewaspadaan. Luka akibat paksaan tidak berubah menjadi cinta hanya karena jaraknya dekat dengan tubuhmu.

Sistem menghitung pusat yang berpindah. Koita kehilangan lingkarannya dan nyaris seluruh pegangan pada dirinya sendiri. Di sekelilingmu, tiap orang masih membawa kehendak dan luka yang berbeda. Angka yang menyamakan semuanya sebagai keberhasilan adalah bagian terakhir yang membuat pemandangan itu terasa begitu dingin."""

    # ┌─ ENDING · E-KO-18 · Naskah yang Kosong  [Khusus · host Y/C]
    # │ KAPAN   : syarat E-KO-16 atau E-KO-17; Koita tahu soal naskah dan percaya; plot armor padam (K-D14)
    # │ ISI SKRG: Koita sadar ia protagonis yang ditinggalkan naskahnya sendiri; kebetulan tidak pernah datang lagi. Sistem membacakan: "Protagonis selesai."
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-18"] = """Koita kembali ke tempat kebetulan dulu selalu datang. Ia menunggu melewati jam yang masuk akal, melewati penutupan toko, sampai petugas meminta jalan masuk dikosongkan. Tidak ada siapa pun yang tiba terlambat untuk menjadi penutup yang manis.

Ia sudah percaya pada keberadaan naskah. Kini ia mempercayai sesuatu yang lebih menghancurkan: bahwa naskah itu berhenti menginginkannya. Buku catatannya tetap kosong karena setiap awal kalimat terdengar seperti meniru suara yang sudah pergi.

Protagonis selesai, kata Sistem.

Koita mendengar atau tidak mendengar kalimat itu; akibatnya sama-sama tinggal dalam hidup yang terus berjalan. Keesokan paginya matahari masih masuk melalui tirai. Seseorang yang tidak lagi dianggap pusat cerita tetap harus bangun di dalam tubuhnya sendiri, tanpa petunjuk tentang bagaimana menjadi orang biasa."""

    # ┌─ ENDING · E-KO-19 · Yang Tidak Bisa Ia Hentikan  [Hancur · host Y/C]
    # │ KAPAN   : Koita menyaksikan Force; trust_koita masih tinggi saat itu (ia masih percaya dan dekat dengan pemain), sehingga ia membeku alih-alih bertindak; korban tidak kembali padanya
    # │ ISI SKRG: trauma karena gagal melindungi orang yang masih ia percaya; ia tidak sanggup mendekati siapa pun lagi. Bisa menempel sebagai lapisan di E-KO-16 atau E-KO-17
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-19"] = """Ingatan Koita pecah di bagian ketika ia seharusnya mengenali bahaya pada orang yang masih dipercayainya. Ia mengulang saat itu dalam pikirannya, mencari satu gerakan atau satu kalimat yang bisa mengubah apa yang sudah terjadi. Tubuhnya mengingat kebekuan sebelum pikirannya selesai menyusun rasa bersalah.

Orang yang dilukai tidak kembali kepadanya. Koita tidak berhak menuntut itu sebagai bukti bahwa ia telah diampuni. Namun tanpa seseorang yang membantu membedakan tanggung jawab pelaku dari kegagalannya bertindak, ia mulai menganggap kedekatannya sendiri selalu membawa bahaya.

Ia menjauh dari teman, menolak ajakan, dan tersentak pada suara tertentu yang tak dimengerti orang lain. Di luar, namanya mungkin hanya muncul sebagai saksi yang diam. Di dalam, peristiwa itu terus terjadi ulang, merusak kemampuan mempercayai diri dan orang lain."""

    # ┌─ ENDING · E-KO-20 · Saksi yang Bersuara  [Netral · host Y/C]
    # │ KAPAN   : Koita menyaksikan atau mengetahui Force saat trust_koita sudah rendah (sudah lama curiga atau lepas dari pemain), sehingga ia bisa bertindak alih-alih membeku
    # │ ISI SKRG: dari orang yang sudah tidak percaya menjadi orang yang menjatuhkan pemain; sendiri, tetapi berdiri. Berjalan bersama E-FO-11
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-20"] = """Koita tidak mencoba membuat kesaksiannya terdengar lebih lengkap daripada yang ia ketahui. Ia membedakan apa yang dilihat, apa yang didengar, dan apa yang baru dipahami sesudahnya. Ketika ditanya tentang kedekatannya denganmu, ia tidak menyembunyikan bahwa pernah mempercayaimu.

Ia hadir kembali saat diperlukan. Ia menerima bahwa korban boleh memilih didampingi orang lain, boleh tidak ingin bertemu dengannya, dan tidak berkewajiban membenarkan rasa bersalahnya. Kesaksian itu membantu meruntuhkan kebebasan yang selama ini kaunikmati di balik kepercayaan orang.

Koita tetap sendiri pada banyak hari setelahnya. Tetapi ia tidak lagi memakai kesendirian sebagai alasan untuk tunduk kepada orang yang berbahaya. Ketika seseorang berterima kasih karena ia bersuara, ia tidak menyebut dirinya penyelamat. Ia mengatakan ada hal yang akhirnya tidak ia biarkan lewat."""

    # ┌─ ENDING · E-KO-21 · Dituduh atas Luka yang Menimpanya  [Hancur · host C]
    # │ KAPAN   : jalur manipulasi pembalikan Chiasa (06_Chiasa.md §14) bertahan; runtuh_koita ≥ 80
    # │ ISI SKRG: Koita korban yang justru dicap pelaku; tidak dipercaya dan tidak bisa membuktikan sebaliknya; runtuh dalam diam. K-D21 (ada yang tetap percaya) atau C-D14/C-D15 (Chiasa sendiri goyah) bisa membelokkan ini sebelum M35
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-KO-21"] = """Koita berusaha menjelaskan bahwa luka itu menimpanya. Setiap kata tiba di hadapan orang yang sudah membawa kesimpulan lain. Kemarahannya dianggap ancaman, tangisnya dianggap akting, dan kebingungannya dipakai untuk meragukan ingatan yang sedang susah payah ia pertahankan.

Tidak ada saksi yang berhasil menembus versi yang telanjur dipercaya sebelum evaluasi berakhir. Orang-orang menjauh dengan keyakinan sedang melindungi seseorang. Koita kehilangan ruang aman sekaligus hak untuk dikenali sebagai orang yang telah dilukai.

Ia mulai menghindari cermin, telepon, bahkan bunyi langkah di depan rumah. Fitnah yang bertahan tidak mengubah siapa yang melakukan kekerasan. Kebenaran itu tetap ada, tetapi sendirian bersamanya di kamar yang makin jarang dibuka, tanpa suara lain yang cukup kuat untuk membuat dunia mendengar."""

    # ┌─ ENDING · E-BL-01 · Berkomitmen  [Romantis · host Y]
    # │ KAPAN   : B6 memilih; dibuka terbuka
    # │ ISI SKRG: Koita berhenti menggantung dan memilih Yutaka
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-BL-01"] = """Koita memperkenalkan Yutaka sebagai pasangannya sebelum ada yang sempat menyebut mereka sahabat seperti biasa. Suaranya goyah pada kata pertama, lalu menjadi lebih jelas ketika ia mengulang untuk orang yang belum mendengar.

Tidak semua percakapan sesudahnya mudah. Ada perasaan orang lain yang harus dijawab, ada gurauan yang perlu dihentikan, ada kebiasaan Koita menyenangkan semua orang yang muncul saat ia takut. Yutaka tidak mengambil alih seluruh percakapan itu. Ia berdiri di sebelahnya, memberi waktu, lalu meminta jawaban yang sungguhan.

Mereka pulang bersama dan bertengkar tentang siapa yang lupa membeli beras. Hal biasa itu membuat Koita tertawa lebih lega daripada ucapan selamat seharian. Hubungan mereka akhirnya punya masa depan yang bisa diperdebatkan, direncanakan, dan dijalani oleh dua orang yang sama-sama memilih tinggal."""

    # ┌─ ENDING · E-BL-02 · Ditolak dan Retak  [Netral · host Y]
    # │ KAPAN   : B6 menolak
    # │ ISI SKRG: persahabatan sejak kecil retak
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-BL-02"] = """Penolakan itu jelas. Tak ada mungkin nanti yang bisa dibawa pulang untuk dipelihara sebagai harapan. Setelahnya mereka masih tahu terlalu banyak hal kecil tentang satu sama lain, tetapi tak lagi tahu cara memulai percakapan tanpa menyentuh bagian yang sakit.

Yutaka berhenti datang tanpa kabar. Koita beberapa kali mengetik cerita yang dahulu pasti dikirim kepadanya, lalu menghapusnya. Persahabatan sejak kecil ternyata tidak kebal terhadap satu keinginan yang tidak bisa dibalas.

Mereka tidak membuat janji untuk segera kembali seperti semula. Ketika akhirnya bertemu di kampus, sapaan mereka pendek dan sopan. Ada kasih yang tidak hilang seketika, ada jarak yang diperlukan untuk bertahan, dan tidak seorang pun berutang hubungan romantis demi menyelamatkan masa lalu."""

    # ┌─ ENDING · E-BL-03 · Kembali ke Pola Lama  [Netral · host Y]
    # │ KAPAN   : B6 lari; Yutaka mundur
    # │ ISI SKRG: Koita kembali menggantung semua orang, termasuk Yutaka
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-BL-03"] = """Koita mengatakan belum siap. Yutaka mendengar keraguan yang dikenalnya sejak lama dan memilih mundur sebelum seluruh hidupnya menjadi ruang tunggu. Untuk beberapa minggu pesan mereka jarang.

Lalu Koita kembali dengan cerita kecil, foto makanan, pertanyaan apakah ia sudah tidur. Tidak ada pembicaraan tentang apa yang pernah diminta Yutaka. Kedekatan itu terasa begitu akrab sehingga mudah diterima, sampai ia menyadari nama lain juga mendapat undangan untuk datang saat Koita kesepian.

Kini Yutaka termasuk di antara orang-orang yang diberi cukup kehangatan untuk bertahan dan terlalu sedikit kepastian untuk melangkah. Koita tidak menyebutnya cinta. Ia juga tidak membiarkannya menjadi sekadar persahabatan. Pola lama mendapatkan satu orang lagi yang tahu betapa manisnya seseorang dapat terdengar saat menghindari jawaban."""

    # ┌─ ENDING · E-BL-04 · Kolaps  [Buruk · host Y]
    # │ KAPAN   : semua orang, termasuk Yutaka, mundur darinya
    # │ ISI SKRG: Koita kolaps setelah sendirian
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-BL-04"] = """Yutaka adalah nomor terakhir yang masih dicoba Koita setelah semua percakapan lain berakhir. Ketika hubungan itu pun mundur, ia kehilangan orang yang selama ini dianggap akan selalu berada di luar pertanyaan memilih.

Ia berhenti menjaga waktu. Pagi dan malam ditentukan oleh kapan ia sanggup membuka mata, bukan jadwal kuliah. Pesan yang menanyakan kabarnya dibiarkan karena menjawab satu berarti mengakui bahwa keadaan memang sudah separah itu.

Kehancurannya tidak membuktikan bahwa Yutaka seharusnya menerima perasaan yang tidak ingin diterima. Itu menunjukkan betapa lama Koita menggantungkan seluruh rasa aman pada kesediaan orang lain untuk tidak pernah pergi. Pada hari evaluasi, kamar itu masih tertutup, dan bantuan yang ia perlukan belum berhasil menjadi sesuatu yang berani ia minta."""

    # ┌─ ENDING · E-BL-05 · Rahasia di Apartemen  [Romantis · host Y]
    # │ KAPAN   : B6 memilih; disembunyikan
    # │ ISI SKRG: hubungan berlanjut diam-diam; Chiasa tahu
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-BL-05"] = """Di apartemen Yutaka, Koita punya cangkir dan sikat gigi sendiri. Di luar, mereka masih sering diperkenalkan sebagai teman lama. Kesepakatan merahasiakan hubungan itu terasa aman pada awalnya; kemudian muncul malam ketika salah satu dari mereka lelah harus menimbang setiap gerakan.

Chiasa mengetahui lebih dahulu daripada orang lain. Ia tidak menjadikan pengetahuan itu tiket untuk masuk ke setiap urusan mereka, tetapi tatapannya membuat Koita sadar bahwa diam pun dapat melukai orang yang belum diberi jawaban.

Mereka tetap bersama. Pada kalender dapur, keduanya menandai hari untuk membicarakan kembali apa yang akan mereka sembunyikan dan sampai kapan. Hubungan itu nyata di balik pintu apartemen. Agar bertahan, mereka perlu memastikan pintu tersebut menjadi tempat pulang, bukan tempat salah seorang dikurung oleh ketakutan yang lain."""

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

Ia merindukan rumah dan tetap tidak pulang untuk menyerahkan pilihannya. Cinta memberi tempat sementara untuk beristirahat; ia tidak menghapus kehilangan. Di antara barang yang belum dibongkar, mereka mulai membangun hari-hari yang cukup aman untuk menampung keduanya, termasuk kesedihan yang belum selesai."""

    # ┌─ ENDING · E-BL-08 · Ia Lari dari Pintu Itu  [Netral · host Y]
    # │ KAPAN   : B4 dominan tanpa kehangatan
    # │ ISI SKRG: Koita kabur dari Yutaka dan dari semuanya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-BL-08"] = """Koita semula mengira ketegasan Yutaka akan membuat segalanya lebih mudah. Ia tidak perlu menebak siapa yang diinginkan atau kapan harus mendekat. Namun sedikit demi sedikit, kepastian berubah menjadi perasaan bahwa tak ada jawaban yang aman selain menurut.

Ketika ia akhirnya berkata berhenti, suaranya hampir tidak keluar. Ia mengambil tas dan pergi sebelum percakapan bisa berubah menjadi bujukan lain. Setelah itu ia menghindari tempat-tempat yang mempertemukan mereka, bahkan ketika jarak tersebut membuatnya kehilangan teman yang tak tahu apa-apa.

Yutaka tidak mendapatkan hubungan hanya karena pernah menjadi orang paling dekat. Di depan pintu yang tidak lagi dibuka untuknya, ketegasan tanpa kehangatan kehilangan nama yang dahulu dipakainya. Koita pergi dengan rasa takut, membawa hak yang terlambat ia percayai: ia boleh menolak, juga kepada orang yang pernah ia cintai."""


    # ═════ Miyuki ═════
    # ┌─ ENDING · E-MI-01 · Jas Putih yang Ringan  [Romantis · host Y/C]
    # │ KAPAN   : tahap ≤ 3 atau pulih; Affection dan Trust tinggi ke pemain; tanpa Force; Sena tidak memusuhi
    # │ ISI SKRG: hubungan setara; ia belajar meminta tolong dan tetap menuju pediatri
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-01"] = """Miyuki pulang dengan jas putih tersampir di lengan dan permintaan yang dahulu hampir mustahil diucapkannya: hari ini ia ingin ditemani tanpa harus menyiapkan apa pun. Kau menggeser buku dari sofa, memberinya tempat, dan menunggu ia memilih antara bercerita atau diam.

Hubungan kalian tidak menggantikan cita-citanya menjadi dokter anak. Ada jadwal yang harus dihormati, kencan yang dipindahkan, malam ketika kalian sama-sama lelah. Sena tetap bisa mengajaknya makan tanpa membuatmu merasa tersaingi. Miyuki pun belajar bahwa menerima bantuan tidak mengurangi kemampuannya merawat orang lain.

Pada suatu pagi ia lupa membuatkan teh untukmu karena terlalu asyik menceritakan pasien kecil yang akhirnya berani menyapanya. Ia baru sadar di tengah cerita, lalu tertawa. Kau tetap mendengarkan. Ia dicintai bahkan ketika tidak sedang menyediakan sesuatu."""

    # ┌─ ENDING · E-MI-02 · Dokter Anak  [Netral · host Y/C]
    # │ KAPAN   : tahap ≤ 2; karier lancar; hati tidak ke siapa pun
    # │ ISI SKRG: lulus, fokus pediatri, hangat pada semua tetapi sendiri
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-02"] = """Jalan menuju pediatri belum selesai saat Miyuki meninggalkan masa kuliahnya. Masih ada pendidikan, penilaian, dan hari-hari ketika pengetahuan terasa terlalu kecil di hadapan ketakutan sebuah keluarga. Ia tetap melangkah ke sana, kali ini dengan kebiasaan meminta bantuan sebelum kelelahan mengambil seluruh suaranya.

Tidak ada pasangan yang menunggunya sebagai hadiah atas pertumbuhan itu. Ia punya Sena, rekan yang bisa dipercaya, dan apartemen yang mulai diisinya dengan barang-barang untuk dirinya sendiri. Kesendirian kadang terasa sepi; ia tidak lagi menyamakan rasa sepi dengan bukti bahwa dirinya kurang berguna.

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

Takeru berbicara sopan tentang rencana yang sudah dibahas para orang tua. Miyuki belajar menyampaikan keberatan sebagai penyesuaian kecil agar tetap boleh didengar. Ia belum menemukan cara menolak seluruh rencana tanpa merasa telah mengecewakan semua orang sekaligus.

Ia tetap menempuh jalan kedokteran, membawa pertunangan sebagai bagian lain dari kewajiban keluarga. Di apartemennya, kotak cincin disimpan rapi di samping buku. Ada hari ketika ia lupa mengenakannya sampai telepon ibunya masuk. Kealpaan kecil itu menjadi satu-satunya percakapan jujur antara tangannya dan sesuatu yang belum berani ia katakan."""

    # ┌─ ENDING · E-MI-05 · Kereta Pagi Tanpa Tujuan  [Romantis · host Y/C]
    # │ KAPAN   : Mi25-C kabur bersama pemain
    # │ ISI SKRG: orang tua memutus hubungan; karier tertunda; cinta yang mahal
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-05"] = """Kereta pertama berangkat ketika Miyuki masih menerima panggilan dari rumah. Ia mematikan suara, menatap namamu di layar pemesanan tiket, lalu menangis karena kelegaan dan ketakutan datang bersamaan. Kalian pergi dengan lebih banyak keberanian daripada rencana.

Keluarganya memutus dukungan dan hubungan. Pendidikan tertunda; uang yang dahulu tidak perlu dihitung kini dibagi antara tempat tinggal, makan, dan kemungkinan kembali kuliah. Pada malam-malam tertentu cinta kalian dipaksa berbicara dalam bentuk tagihan dan kesabaran yang menipis.

Miyuki tidak menyesali haknya memilih. Ia juga tidak selalu bahagia dengan harga yang dibayar. Kalian bertahan hanya jika pengorbanan itu tidak dijadikan utang yang harus ia lunasi dengan terus mencintaimu. Di kamar kecil dekat rel, ia menyimpan buku kedokterannya tetap terbuka, menolak menyerahkan seluruh masa depan kepada satu pagi pelarian."""

    # ┌─ ENDING · E-MI-06 · Lampu Bangsal Padam  [Buruk · host Y/C]
    # │ KAPAN   : kelelahan ekstrem; tanpa bantuan; CBT gagal
    # │ ISI SKRG: burnout; berhenti dari kedokteran
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-06"] = """Miyuki mengenali semua istilah untuk menjelaskan kelelahan, tetapi pengetahuan itu tidak membuat tangannya sanggup membuka buku. Setelah ujian yang gagal, ia mencoba mengejar dengan waktu tidur yang semakin sedikit. Ketika tubuhnya berhenti mengikuti kemauannya, tak ada lagi senyum yang cukup untuk menutupi keadaan.

Ia meninggalkan kedokteran. Untuk beberapa waktu jas putihnya tetap tergantung seolah pemiliknya hanya sedang libur. Telepon keluarga berubah menjadi pembicaraan tentang kesempatan yang disia-siakan, membuat ia makin jarang menjawab.

Cita-citanya tidak hilang dengan rapi. Ia masih menoleh pada suara anak menangis dan masih tahu apa yang ingin ia lakukan jika punya tenaga. Pada hari evaluasi, kehilangan itu belum menemukan bentuk kehidupan pengganti. Orang yang selama ini paling pandai merawat orang lain kini kesulitan percaya bahwa dirinya sendiri layak dirawat tanpa lebih dahulu berguna."""

    # ┌─ ENDING · E-MI-07 · Kenyamanan yang Salah  [Terdistorsi · host Y/C]
    # │ KAPAN   : tahap 5 permanen; arah_luka pemain
    # │ ISI SKRG: hubungan "nyaman" yang tidak sehat; ia hanya merasa dicintai saat diperlakukan keras
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-07"] = """Miyuki mulai gelisah pada hari ketika kau memperlakukannya dengan tenang. Ia mencari kesalahan kecil yang bisa menjelaskan mengapa perhatianmu terasa begitu jauh. Jika akhirnya kau meninggikan suara, tubuhnya justru mengendur, lega karena kembali tahu cara mendapatkan tempat di hadapanmu.

Ia menyebutnya cocok. Katanya hanya kalian yang memahami bentuk kasih sayang itu. Sena mendengar kalimat tersebut dan tidak ikut tersenyum. Di mata sahabatnya, Miyuki makin sulit meminta sesuatu tanpa terlebih dahulu merendahkan diri.

Hubungan kalian terus berlangsung. Kedekatan tidak berarti aman, dan kepatuhannya tidak membuat luka menjadi keinginan yang bebas. Pada meja dapur, teh selalu siap sebelum kau meminta. Miyuki menunggu reaksimu untuk mengetahui apakah ia boleh merasa dicintai hari ini."""

    # ┌─ ENDING · E-MI-08 · Penebusan Tanpa Akhir  [Terdistorsi · host Y/C]
    # │ KAPAN   : tahap 5; arah_luka diri
    # │ ISI SKRG: lulus dan bekerja, tetapi menghukum diri lewat jam kerja tanpa batas
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-08"] = """Miyuki lulus. Ia mendapat pekerjaan dan dikenal sebagai orang yang selalu bersedia menggantikan jadwal. Ketika dipuji berdedikasi, ia tersenyum dengan sopan, menyembunyikan alasan yang tidak terdengar mulia: jika berhenti sebentar, ia takut seluruh kesalahan yang dituduhkan kepada dirinya akan kembali memenuhi ruangan.

Jam kerjanya menjadi bentuk hukuman yang diterima orang sebagai pengabdian. Ia jarang pulang sebelum benar-benar habis tenaga. Undangan makan ditolak dengan alasan sibuk, lalu ia merasa lega karena tidak perlu menjelaskan mengapa bersenang-senang terdengar seperti sesuatu yang belum pantas didapatkan.

Di bangsal ia tetap hangat. Pasien tidak selalu melihat apa yang dikorbankan setelah pintu tertutup. Hidupnya tampak berhasil dari luar, sementara setiap keberhasilan segera berubah menjadi tuntutan berikutnya. Tidak ada angka yang akhirnya membuatnya merasa sudah cukup membayar."""

    # ┌─ ENDING · E-MI-09 · Menunggu yang Menyakitkan  [Terdistorsi · host Y/C]
    # │ KAPAN   : tahap 5; arah_luka Koita; Koita tetap menggantung
    # │ ISI SKRG: ia bertahan di sisi Koita justru karena sakitnya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-09"] = """Koita masih berkata nanti. Miyuki tidak lagi mendengar kata itu sebagai penundaan semata; rasa sakit setelahnya telah menjadi cara paling dikenalnya untuk memastikan perasaannya masih nyata. Ia datang saat diminta dan bertahan ketika seharusnya boleh pergi.

Kadang Koita memberinya malam yang hangat, lalu menghilang ke kesibukan orang lain. Miyuki menyalahkan dirinya karena menginginkan lebih. Ketika seorang teman mengatakan ia layak mendapat kepastian, ia membela Koita lebih keras daripada yang Koita pernah lakukan untuk hubungan mereka.

Di apartemen, ia menyiapkan makanan untuk kemungkinan kedatangan yang tidak dijanjikan. Ada hari ketika makanan itu habis sendiri, ada yang harus dibuang. Penantian berlangsung tanpa membutuhkan janji baru, sebab ia sudah belajar menjadikan sakitnya sendiri sebagai alasan untuk tetap tinggal."""

    # ┌─ ENDING · E-MI-10 · Cuti Satu Tahun  [Netral · host Y/C]
    # │ KAPAN   : pulih sebagian lewat Sato; CBT tertunda
    # │ ISI SKRG: cuti kuliah; masa depan terbuka; pesan pendek untuk pemain di musim semi
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-10"] = """Formulir cuti terasa lebih berat bagi Miyuki daripada formulir ujian mana pun. Ia membawanya ke sesi dengan Sato, mengaku takut satu tahun istirahat akan membuktikan bahwa sejak awal ia tidak cukup kuat untuk kedokteran.

Keputusan itu tetap diambil. Ujian ditunda, kalender dikosongkan sebagian, dan ia belajar bahwa sehari tanpa pencapaian tidak harus diakhiri dengan rasa bersalah. Pemulihannya tidak lurus. Ada pagi ketika ia bangun panik karena mengira terlambat praktik, lalu perlu waktu untuk memahami bahwa tak ada yang sedang ia kecewakan.

Pada musim semi ia mengirim pesan pendek: hari ini membuat sarapan untuk diri sendiri, rasanya enak. Tidak ada janji kapan kembali sepenuhnya. Masa depannya masih terbuka, dan untuk pertama kalinya ruang yang belum terisi itu tidak hanya terasa sebagai kegagalan."""

    # ┌─ ENDING · E-MI-11 · Pintu yang Ditutup Sena  [Buruk · host Y/C]
    # │ KAPAN   : pemain memanfaatkan di depan umum; Sena memutus
    # │ ISI SKRG: Miyuki terisolasi; Sena menjadi penghalang pemain di semua lingkungan medis
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-11"] = """Sena melihat cukup banyak untuk berhenti menyebut perlakuanmu salah paham. Ia berdiri di antara kau dan Miyuki ketika penghinaan yang kauanggap biasa kembali terjadi di depan orang lain. Kali ini tidak ada tawa yang dibiarkan menyamarkannya.

Aksesmu ke lingkungan medis mulai tertutup. Sena tidak bersedia mengantarkan pesan, mencarikan alasan, atau memberimu kesempatan mendekat lewat nama orang yang pernah kauperlakukan sebagai alat. Ia mengatakan apa yang diketahuinya ketika diperlukan.

Miyuki tetap sulit dijangkau. Rasa malu membuatnya menarik diri bahkan dari orang yang berusaha membantu, dan pintu yang ditutup Sena tidak otomatis membuka jalan pemulihan. Yang berakhir adalah kemudahanmu memanfaatkan keramahan semua orang. Di baliknya masih ada seseorang yang harus belajar bahwa menerima perlindungan tidak berarti kehilangan hak menentukan hidup sendiri."""

    # ┌─ ENDING · E-MI-12 · Napas yang Tertahan  [Hancur · host Y/C]
    # │ KAPAN   : pemain pelaku Force terhadapnya
    # │ ISI SKRG: trauma terpisah dari Rute Masokis; jalur Sena, Sato, dan hukum; tanpa romansa dengan pelaku
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-12"] = """Setelah kekerasan itu, Miyuki sulit mengenali tubuh yang selama ini ia paksa untuk selalu dapat diandalkan. Ia bisa menyebut apa yang terjadi dengan istilah yang tepat dan tetap kehilangan suara ketika harus mengucapkannya sebagai sesuatu yang menimpa dirinya.

Sena datang tanpa meminta cerita lengkap. Sato menyediakan ruang yang tidak menuntutnya segera pulih. Dukungan dan jalan hukum dibicarakan sesuai kesiapan serta kehendaknya; kedokteran yang semula menjadi seluruh identitasnya kini harus memberi ruang bagi pemulihan yang tidak mengikuti kalender ujian.

Perbuatanmu tidak menjadi bagian dari romansa, dan kerentanan Miyuki sebelumnya bukan persetujuan. Ia boleh marah, diam, atau menolak bertemu orang yang pernah dekat dengannya. Pada hari ia akhirnya mengatakan bahwa ia tidak ingin melihatmu lagi, kalimat itu tidak memerlukan penerimaanmu untuk berlaku."""

    # ┌─ ENDING · E-MI-13 · Sandiwara yang Jadi Nyata  [Romantis · host Y/C]
    # │ KAPAN   : pasangan palsu dipertahankan sampai Mi18, lalu diakui jujur
    # │ ISI SKRG: dua keluarga marah lalu menerima; awal yang bohong menjadi hubungan yang jujur
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-13"] = """Hubungan yang awalnya dipakai untuk menghindari tekanan keluarga akhirnya menuntut satu pengakuan yang tidak bisa dilatih. Miyuki mengatakan ia ingin bersamamu sungguhan, lalu meminta sandiwara sebelumnya diakhiri dengan kebenaran kepada semua pihak.

Dua keluarga marah karena telah dipermainkan. Percakapan panjang mengikuti, penuh pertanyaan yang dahulu kalian harapkan bisa dilewati dengan senyum. Penerimaan datang perlahan setelah kalian berhenti menyalahkan keadaan untuk setiap kebohongan yang dipilih sendiri.

Ketika makan malam berikutnya tiba, Miyuki masih gugup. Kau tidak lagi perlu menghafal tanggal rekaan atau kebiasaan yang dibuat agar tampak mesra. Di bawah meja ia menggenggam tanganmu, lalu membiarkannya terlihat. Kali ini kedekatan itu tidak bergantung pada siapa yang sedang menonton."""

    # ┌─ ENDING · E-MI-14 · Sandiwara Terbongkar  [Buruk · host Y/C]
    # │ KAPAN   : pasangan palsu terbongkar oleh Takeru atau orang tua
    # │ ISI SKRG: malu di depan keluarga; Miyuki menjauh dari pemain dan menerima omiai
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MI-14"] = """Kebenaran tentang pasangan palsu muncul di tengah pertemuan keluarga, pada saat semua orang sudah cukup jauh membicarakan masa depan untuk merasa dipermalukan oleh masa lalu. Miyuki mencoba menjelaskan tekanan yang membuatnya setuju. Penjelasan itu terdengar seperti alasan di telinga orang yang lebih marah karena kehilangan kendali.

Ia menjauh darimu setelahnya. Bukan hanya karena sandiwara terbongkar, melainkan karena setiap percakapan denganmu mengembalikannya pada ketakutan bahwa ia telah membuat hidupnya semakin sulit untuk ditentukan sendiri.

Miyuki menerima omiai. Ia hadir dengan pakaian yang disiapkan rapi dan jawaban yang tidak lagi menyisakan ruang bagi lelucon pribadi kalian. Kebohongan yang dahulu dimaksudkan untuk membuka jalan keluar justru memberatkan pintu itu, sampai ia terlalu lelah untuk mencoba membukanya lagi."""


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

Koko masih ada di kamarnya. Masa kecil tidak dibuang, hanya dipindahkan dari posisi sebagai rencana masa depan. Di meja gambar, Nagisa mulai membuat garis yang tidak perlu menunggu siapa pun menjawab perasaannya agar dapat diselesaikan."""

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

Hubungan itu bertahan, tetapi dunianya makin sempit. Setiap kepergianmu menjadi keadaan darurat sebab ia tak lagi mempunyai banyak hal lain untuk ditempati. Rumah yang ia bangun di sekelilingmu akhirnya tak punya cukup jendela untuk melihat dirinya sendiri. Ia menyebutnya cinta, takut jika memakai kata lain maka seluruh pengorbanannya kehilangan arti."""

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

Haruto datang dengan wajah yang tak lagi mengenal cara bercanda. Ia tetap kakaknya, dan tetap harus menerima bahwa mencintai Nagisa tidak berarti membenarkan perbuatannya. Di ruang tunggu, ia menatap telepon yang penuh pertanyaan. Adik yang dahulu ingin dibantunya merasa aman kini harus bertanggung jawab karena telah merampas rasa aman seseorang yang lain."""

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

Di kota baru ia kadang menyesali cara meninggalkan Koko. Penyesalan tersebut tidak membuatnya menghubungi kalian kembali. Ia belajar bahwa satu keputusan dapat terasa perlu sekaligus menyedihkan. Rumah yang akan dirancangnya nanti masih boleh hangat, meski tak lagi dibangun untuk mengembalikan orang-orang yang telah ia tinggalkan."""

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

Pada suatu sore Chiasa memanggil Nacchan-oneechan dengan sungguh-sungguh. Nagisa tersipu, mengomel, lalu menggenggam tangannya sendiri. Kenangan lama memperoleh arti baru tanpa harus menyangkal bahwa dulu mereka pernah saling melukai. Kali ini gengsi bukan satu-satunya cara menjaga sesuatu yang penting."""

    # ┌─ ENDING · E-NA-11 · Bayangan di Bawah Jendela  [Terdistorsi · host Y/C]
    # │ KAPAN   : pemain menolak; Nagisa terus menguntit; pemain melapor ke Hanabusa
    # │ ISI SKRG: perintah menjauh; kuliah dan nama baiknya hancur
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NA-11"] = """Nagisa mengatakan hanya ingin memastikan kau baik-baik saja. Ia mengulang alasan itu meski telah diminta berhenti, meski setiap kemunculannya membuatmu makin takut pulang. Keinginan mengetahui keberadaanmu sudah mengalahkan kemauan mendengar penolakanmu.

Laporan kepada Hanabusa mengubah apa yang selama ini disebut urusan pribadi. Ada batas yang kini ditegakkan dari luar, perintah menjauh yang tak bisa dibatalkan dengan tangis atau kenangan. Kampus mulai mengenal namanya melalui keluhan dan pemeriksaan, bukan karya studionya.

Nagisa kehilangan ruang belajar dan nama baik sambil tetap merasa sedang dibuang karena terlalu peduli. Ia belum sanggup memahami bahwa kepedulian yang menolak hak orang lain untuk merasa aman telah menjadi sesuatu yang berbeda. Di seberang jendela, lampu yang ia tunggu tidak lagi memberi izin untuk mendekat."""

    # ┌─ ENDING · E-NA-12 · Gengsi yang Retak  [Hancur · host Y/C]
    # │ KAPAN   : pemain pelaku Force terhadapnya
    # │ ISI SKRG: trauma; Haruto menjadi lawan serius pelaku; tanpa romansa dengan pelaku
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NA-12"] = """Sesudah kekerasan itu, Nagisa membenci pertanyaan yang mengharuskannya mengulang bahwa ia tidak menginginkannya. Orang mengenalnya galak; kini sebagian mengira ia pasti bisa melawan apa pun. Anggapan itu menambah malu yang sama sekali bukan tanggung jawabnya.

Haruto mendengarkan dengan amarah yang harus ia tahan agar tidak mengambil alih keputusan adiknya. Ia menjadi lawan serius bagimu: hadir ketika diperlukan, membantu menjangkau dukungan, dan tidak bersedia membiarkan perbuatanmu menyusut menjadi rumor tentang hubungan yang rumit.

Nagisa tidak menjadi pasanganmu karena kau telah melukainya. Gengsinya yang retak bukan pintu menuju kepemilikan. Pemulihannya panjang, dan ada hari ia bahkan tidak ingin disentuh keluarganya. Di antara hal-hal yang lambat ia ambil kembali adalah hak mengucapkan tidak tanpa lebih dahulu harus terdengar kuat agar dipercaya."""

    # ┌─ ENDING · E-NA-13 · Ambulans di Malam Valentine  [Buruk · host Y/C]
    # │ KAPAN   : N15-B ditolak; tanpa Haruto, keluarga, atau pemain di sisinya
    # │ ISI SKRG: ia melukai diri dan dirawat (tanpa metode); pemulihan panjang; epilog berbeda bila pemain menjenguk
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NA-13"] = """Ambulans datang pada malam ketika kabar orang lain penuh coklat dan rencana bertemu. Nagisa selamat setelah melukai dirinya dalam krisis yang tak berhasil dijangkau sebelum memburuk. Di rumah sakit, percakapan tentang mengapa tidak ada yang tahu lebih dahulu terasa jauh lebih mudah daripada menerima betapa banyak hal yang belum mereka pahami.

Pemulihannya melibatkan hari-hari yang tidak dramatis: makan, tidur, janji perawatan, dan orang yang bersedia tetap hadir tanpa menuntut kabar baik. Kunjunganmu, jika terjadi, tidak boleh berubah menjadi tawaran cinta sebagai pengganti pertolongan yang ia perlukan. Ketidakhadiranmu pun tidak menentukan apakah hidupnya layak diteruskan.

Pada hari evaluasi, masa depannya belum selesai diputuskan. Ada luka yang masih perlu dirawat dan percakapan yang harus dilanjutkan di luar kalian berdua. Yang ia butuhkan tidak muat dalam satu pengakuan atau satu penyesalan yang terlambat."""

    # ┌─ ENDING · E-NA-14 · Senjata yang Kau Arahkan  [Terdistorsi · host Y/C]
    # │ KAPAN   : senjata aktif sampai M35
    # │ ISI SKRG: ia melakukan hal kejam demi pemain; saat sadar dimanfaatkan, ia runtuh atau berbalik pada pemain (risiko E-SI-16)
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NA-14"] = """Nagisa mengira setiap tindakan kejam yang dilakukannya sedang melindungi sesuatu yang kalian bangun bersama. Kau menerima hasilnya, membiarkannya menganggap keberpihakanmu sebagai pembenaran ketika orang lain mulai takut atau terluka.

Sampai hari evaluasi ia masih berada di sisimu. Sesudahnya, pertanyaan kecil mulai muncul: mengapa hanya ia yang diminta mengambil risiko, mengapa ceritamu berubah ketika tidak ada saksi, mengapa rasa bersalah selalu berakhir dengan permintaan agar ia membuktikan kesetiaan lagi.

Kesadaran bahwa dirinya dipakai tidak menghapus tanggung jawab atas apa yang sudah diperbuat. Ia dapat runtuh di bawah keduanya atau membalikkan kemarahan ke arahmu. Yang kauanggap alat ternyata masih seseorang yang bisa mengingat, menilai ulang, dan suatu hari menyebut namamu dalam cerita yang tidak lagi kausunting."""


    # ═════ Harumi ═════
    # ┌─ ENDING · E-HA-01 · Hipotesis yang Terbukti  [Romantis · host Y/C]
    # │ KAPAN   : kejelasan_emosi tinggi; pemain pelindung; tanpa Force
    # │ ISI SKRG: belajar mengenali emosi bersama; teh pagi untuk dua orang
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HA-01"] = """Harumi menyediakan dua cangkir pada pagi pertama yang tidak perlu dijelaskan sebagai sesi belajar. Ia menanyakan apakah kau ingin duduk dekat, lalu menggeser kursi setelah mendengar jawabanmu. Tidak ada catatan yang diperlukan untuk memahami bahwa senyumnya kali ini muncul karena lega.

Kalian belajar menyebut perasaan tanpa menjadikannya ujian dengan satu jawaban benar. Kadang ia baru memahami cemburu setelah beberapa jam; kadang kau salah membaca diamnya dan perlu bertanya lagi. Kesalahan itu dibicarakan sebelum berubah menjadi kewajiban bagi salah seorang untuk selalu mengalah.

Hipotesis bahwa ia merasa lebih tenang di dekatmu mendapat banyak bukti. Yang paling berarti justru hari ketika ia tidak tenang dan masih boleh mengatakan tidak. Harumi menyimpan hak itu bersama kasih sayangnya, dua hal yang akhirnya tidak perlu saling membatalkan."""

    # ┌─ ENDING · E-HA-02 · Laboratorium di Seberang Laut  [Netral · host Y/C]
    # │ KAPAN   : studi luar negeri diterima; pulih sebagian
    # │ ISI SKRG: pergi sendiri; surat panjang tiap musim
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HA-02"] = """Harumi berangkat sendiri dengan berkas beasiswa yang telah diperiksa berulang kali. Di bandara ia tahu berat koper, waktu transit, dan alamat laboratorium baru. Ia tidak tahu bagaimana mengucapkan perpisahan yang tepat, lalu memilih mengatakan bahwa ia akan rindu.

Di seberang laut, pemulihannya tetap ikut dalam barang bawaan. Ada pembicaraan akademik yang membuatnya takut tanpa sebab yang mudah dijelaskan, ada hari ketika perhatian senior terasa sulit dipercaya. Ia belajar mencari dukungan tanpa menyerahkan seluruh penilaiannya kepada satu orang lagi.

Suratnya datang setiap musim. Mulanya penuh rincian riset dan cuaca; belakangan terselip cerita teman, makanan gagal, dan keputusan yang membuatnya bangga secara pribadi. Harumi masih ingin menjadi profesor. Kini keinginan itu tidak lagi harus dibayar dengan memberikan orang lain hak atas seluruh hidupnya."""

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

Teh mereka kadang dingin karena pembicaraan terlalu lama. Harumi masih memakai istilah variabel tetap, lalu menambahkan koreksi: yang tetap adalah kemauan untuk bertanya lagi, sebab perasaan dan manusia tidak wajib berhenti berubah agar bisa dicintai."""

    # ┌─ ENDING · E-HA-05 · Persamaan Transaksi  [Terdistorsi · host Y/C]
    # │ KAPAN   : validasi_dari banyak orang; tahap 6
    # │ ISI SKRG: hidup transaksional; ia merasa akhirnya "mengerti"
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HA-05"] = """Harumi mengatakan ia akhirnya mengerti hubungan manusia. Waktu, perhatian, tubuh, uang, akses: semuanya dapat diberi nilai sehingga tidak ada lagi rasa bingung tentang mengapa orang datang atau pergi. Jika sesuatu menyakitkan, ia menganggapnya biaya yang belum dihitung dengan tepat.

Ia tampak lebih lancar berbicara, lebih cepat membaca keinginan orang, dan makin sulit menjawab pertanyaan sederhana tentang apa yang diinginkannya sendiri. Validasi datang dari banyak arah. Masing-masing membawa syarat yang ia sebut wajar karena sudah terbiasa menghubungkan kedekatan dengan pembayaran.

Ketika seseorang menawarkan duduk tanpa meminta apa pun, Harumi justru mencari maksud tersembunyi. Kerangka yang membuatnya merasa memahami dunia kini menolak pengalaman yang bisa membantahnya. Ia telah mendapatkan persamaan yang selalu menghasilkan jawaban, dengan menghapus bagian dirinya yang berhak mengatakan hasilnya tidak cukup."""

    # ┌─ ENDING · E-HA-06 · Lampu Merah di Distrik Empat  [Buruk · host Y/C]
    # │ KAPAN   : putus kuliah; Ogawa menang atau pergi; tanpa penjaga
    # │ ISI SKRG: masuk dunia kerja seks; epilog menyisakan pintu keluar bila seseorang masih mencarinya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HA-06"] = """Harumi meninggalkan kuliah tanpa perpisahan yang layak. Setelah pekerjaan akademik dan dukungan yang tersedia runtuh, ia masuk ke dunia kerja seks di Distrik Empat, menyebutnya sumber penghasilan yang setidaknya tidak berpura-pura menawarkan sesuatu tanpa harga.

Yang menghancurkan bukan sebuah penilaian tentang dirinya sebagai pekerja, melainkan betapa sempit pilihan yang tersisa setelah eksploitasi. Ia masih berpikir dalam jadwal dan target, mencoba mempertahankan kendali pada hal-hal yang dapat dihitung. Ada malam ketika namanya sendiri terasa seperti nama orang lain yang dahulu punya laboratorium untuk dituju.

Jika masih ada orang yang mencarinya dengan niat membantu, jalan keluar belum tertutup seluruhnya. Ia memerlukan dukungan yang menghormati keputusan dan keselamatannya, bukan seseorang yang datang untuk merasa telah menyelamatkan perempuan yang rusak. Pada hari evaluasi, ketukan yang seperti itu belum sampai atau belum berani ia jawab."""

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

Kau menyaksikan dari jarak yang cukup aman untuk menyebut semuanya rumit. Harumi tidak memiliki kemewahan jarak itu. Di meja kerjanya, berkas yang tidak berhasil membuat orang percaya tersusun di samping penelitian yang kehilangan masa depan. Kekalahan dalam proses tidak membuat perbuatan Ogawa benar; hanya membuat kebenaran lebih berat ditanggung orang yang telah dilukai."""

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

Pada hari evaluasi ia masih berada di dekatmu. Sistem dapat menghitung keberhasilan, tetapi tidak akan menuliskan percakapan kecil ketika ia berkata tidak tahu apa yang diinginkan sebelum kau menjawab lebih dahulu. Kau tahu itu bukan sifat asal Harumi. Ada percobaan yang kaumulai, dan seseorang yang terus menanggung hasilnya."""

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

Tidak ada hubungan romantis denganmu yang lahir dari perbuatan tersebut. Kesulitan Harumi memberi nama pada perasaan tidak pernah berarti ia kehilangan hak atas tubuhnya. Ia mulai mengambil kembali keputusan yang paling sederhana, termasuk siapa yang boleh hadir di ruangan. Namamu tidak ada dalam daftar itu."""

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

Quest Sistem tetap mencapai kesadaranmu dari jauh. Evaluasinya tiba pada hari wisuda yang telah ditentukan, meski halaman Kouseikan kini berada di zona waktu lain. Harumi sedang menyeduh teh saat itu. Kehidupan yang kalian pilih telah bergerak melampaui tempat evaluasi, tetapi akibat keputusan lama tetap dapat menyusul ke mana pun kalian pergi."""


    # ═════ Moeka ═════
    # ┌─ ENDING · E-MO-01 · Belajar Meminta Tolong  [Romantis · host Y/C]
    # │ KAPAN   : minimal 3 jendela diambil; andalan_moeka pemain; janji ditepati; tanpa Force
    # │ ISI SKRG: ia belajar meminta tolong; keluarga mulai stabil
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-01"] = """Moeka menelepon untuk meminta tolong sebelum keadaan menjadi darurat. Ia masih membuka dengan lelucon, kemudian mengoreksi dirinya: ia lelah, ada pekerjaan yang tidak sanggup diselesaikan, dan ia ingin ditemani membicarakannya. Kau datang sesuai janji. Jika tak bisa, kau mengatakan sejak awal dan membantu mencari pilihan lain.

Keluarganya mulai lebih stabil, meski tidak mendadak bebas dari masalah. Rina tetap punya tempat, bantuan kampus tetap diurus, dan cinta kalian tidak dibangun dengan menjadikanmu satu-satunya orang yang boleh mengetahui hari buruknya.

Pada suatu sore ia memperlihatkan rancangan yang dibuat karena ingin, bukan karena harus segera dijual. Ketika kau memujinya, ia membantah bagian yang belum disukai lalu tertawa. Keceriaan itu tidak lagi harus membuktikan bahwa semuanya baik. Ia boleh senang pada satu hal sementara hidupnya masih berusaha pulih."""

    # ┌─ ENDING · E-MO-02 · Cuti Setahun  [Netral · host Y/C]
    # │ KAPAN   : selamat; beasiswa dicabut
    # │ ISI SKRG: cuti kuliah; bekerja membantu keluarga; kembali setahun kemudian
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-02"] = """Beasiswa Moeka dicabut. Ia bertahan hidup, lalu harus menghadapi kehilangan lain yang tidak hilang hanya karena orang mengatakan setidaknya masih ada kesempatan. Kuliahnya dihentikan sementara agar ia bisa bekerja dan membantu keluarga.

Setahun itu penuh jadwal yang tidak difoto: perjalanan pagi, upah yang langsung dibagi, formulir yang dibuka lagi saat malam. Ia belajar membatasi bantuan yang bisa diberikan kepada rumah agar dirinya tetap punya jalan kembali. Tidak selalu berhasil; ada bulan ketika rencana itu tampak terlalu jauh.

Setahun kemudian Moeka kembali ke kampus. Adik-adiknya mengantarkan dengan candaan yang terlalu ramai, Rina memotret dari samping. Ia tidak mengejar semua orang yang telah lulus lebih dahulu. Di depan studio, ia berhenti sebentar, lalu masuk sebagai seseorang yang masih berhak melanjutkan sesuatu miliknya sendiri."""

    # ┌─ ENDING · E-MO-03 · Topeng Sempurna  [Terdistorsi · host Y/C]
    # │ KAPAN   : selamat; topeng tidak pernah dibuka; pemain satu-satunya andalan
    # │ ISI SKRG: tampak baik-baik saja; topengnya total; hidupnya bergantung pada pemain
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-03"] = """Moeka selamat dan kembali memenuhi foto dengan warna. Orang-orang mengatakan ia sudah seperti dulu. Senyum yang kini tampak sempurna membuat mereka tidak merasa perlu bertanya lebih jauh.

Hanya kepadamu ia memberi tanda bahwa hari tertentu terlalu berat, sering begitu kecil sampai mudah terlewat. Ia menyesuaikan seluruh kebutuhan dengan kapan kau tersedia, takut kehilangan satu-satunya tempat yang masih dianggap boleh menampung dirinya tanpa panggung. Di luar hubungan itu ia tetap ceria, tetap menawarkan bantuan, tetap tidak punya kata untuk meminta pertolongan.

Kau menjadi andalan yang hampir seluruh hidupnya bertumpu kepadamu. Kedekatan itu terlihat manis dari luar dan terasa menakutkan setiap kali satu pesan terlambat dijawab. Topengnya tidak pecah; ia justru menjadi begitu mahir memakainya sampai kesendirian yang paling berbahaya tak lagi terlihat berbeda dari hari yang baik."""

    # ┌─ ENDING · E-MO-04 · Malam Tanpa Balasan  [Buruk · host Y/C]
    # │ KAPAN   : Mo25 terlewati
    # │ ISI SKRG: Moeka meninggal. Yang ditampilkan: kabar, duka, pemakaman, Rina, Aya, adik-adik, penyesalan pemain. Tanpa metode. Sistem diam
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-04"] = """Kabar kematian Moeka datang dalam kalimat yang mula-mula tidak dapat kaumengerti. Namanya tetap ada di grup, fotonya tetap tersenyum, dan pesan terakhir masih tampak seperti sesuatu yang dapat dibalas jika kau cukup cepat membuka layar.

Pada pemakaman, Rina tidak memintamu menjelaskan. Diamnya lebih sulit dihadapi daripada pertanyaan. Aya berulang kali mengucapkan terima kasih kepada tamu sampai kehilangan suara. Adik-adik Moeka duduk berdekatan; salah seorang masih ingin menunjukkan sesuatu yang disiapkan untuk kakaknya, kemudian teringat tak ada lagi orang yang akan pulang menerimanya.

Kau mencari satu titik yang seandainya berbeda dapat mengembalikan seluruh cerita. Duka tidak memberimu kepastian sesederhana itu. Ada kesempatan yang terlewat dan bantuan yang tidak sampai, ada hidup yang tak boleh diringkas sebagai kegagalan seseorang mencintai dengan cukup baik.

Sistem diam. Hari-hari sesudahnya tetap meminta keluarga membayar tagihan, membereskan kamar, dan belajar menyebut nama Moeka tanpa menunggu jawaban dari pintu."""

    # ┌─ ENDING · E-MO-05 · Tepat Waktu  [Koita · host Y/C]
    # │ KAPAN   : Mo25-E pemain mengirim Koita, atau andalan_moeka Koita dan Koita menjawab
    # │ ISI SKRG: plot armor menyelamatkannya; hatinya kembali ke Koita
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-05"] = """Koita datang ketika kedatangannya masih bisa menjangkau Moeka. Kebetulan yang dibantu naskah mempertemukan mereka pada waktu yang menentukan, tetapi setelah itu yang diperlukan adalah orang-orang sungguhan: pertolongan, perawatan, keluarga, dan kesediaan tetap hadir ketika keadaan tidak cepat membaik.

Moeka mulai mempercayainya sebagai seseorang yang menjawab. Perasaannya kembali menuju Koita, tumbuh bersama janji kecil yang akhirnya ditepati, bukan karena ia wajib mencintai orang yang tiba pada malam krisis.

Kau melihat mereka sesekali setelahnya. Moeka belum selalu ceria, dan Koita tidak selalu tahu harus berkata apa. Ada hari ketika mereka hanya duduk, membiarkan bantuan orang lain tetap masuk. Jika dunia menyebut malam itu penyelamatan, hari-hari berikutnya mengingatkan bahwa tetap hidup memerlukan lebih dari satu momen yang tepat."""

    # ┌─ ENDING · E-MO-06 · Rina Mengetuk Pintu  [Netral · host Y/C]
    # │ KAPAN   : Mo25-B, atau Rina sekutu sejak Mo18
    # │ ISI SKRG: Rina tiba lebih dulu; dirawat; persahabatan pemain dan Rina menentukan epilog
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-06"] = """Rina mengetuk sampai mendapat jawaban, lalu mencari bantuan yang tidak bisa diberikan seorang sahabat sendirian. Moeka mendapat perawatan. Ketika ia akhirnya bisa berbicara, hal pertama yang keluar justru permintaan maaf karena telah merepotkan.

Rina tetap datang tanpa membiarkan rasa bersalah itu menjadi syarat agar Moeka tampak pulih. Mereka membicarakan dukungan profesional, kabar kepada keluarga, dan cara menjalani satu hari sebelum melompat ke seluruh masa depan. Ada marah karena terlalu lama tidak dipercaya untuk mendengar; ada kasih yang cukup untuk tetap duduk setelah marah itu disebutkan.

Tempatmu dalam epilog bergantung pada bagaimana kau memperlakukan persahabatan tersebut. Rina dapat menjadi rekan dalam membantu Moeka, atau batas yang menahanmu di luar. Yang pasti, Moeka tetap hidup sebagai seseorang yang pantas ditolong, tanpa harus menjadi alasan bagi siapa pun merasa paling berjasa."""

    # ┌─ ENDING · E-MO-07 · Kontrak Kuga  [Terdistorsi · host Y/C]
    # │ KAPAN   : Mo23 kontrak dibiarkan; selamat
    # │ ISI SKRG: meninggalkan kampus untuk kontrak modeling yang eksploitatif; topeng menjadi pekerjaan
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-07"] = """Kontrak Kuga membawa Moeka pergi dari kampus. Foto-fotonya menjadi lebih rapi, jadwalnya lebih padat, dan senyum yang dahulu dipakai untuk menyembunyikan lelah kini menjadi bagian pekerjaan yang dinilai orang lain.

Ia mengirim uang ke rumah. Keluarganya melihat bantuan yang datang sebelum memahami harga yang tidak tertulis dalam kabar baiknya. Ada pekerjaan yang disetujui karena takut kehilangan akses pada pekerjaan berikutnya, ada keberatan yang berhenti di mulut karena seluruh hidup terasa bergantung pada satu nama.

Moeka selamat, tetapi makin sulit mengenali keinginan sendiri di bawah tuntutan kontrak. Ketika seseorang dari kampus menanyakan apakah ia senang, ia mengirim foto terbaru dan stiker tertawa. Jawaban itu tampak lengkap bagi orang yang tidak tahu bagaimana membaca jeda panjang sebelum gambar dikirim."""

    # ┌─ ENDING · E-MO-08 · Label di Garasi  [Netral · host Y/C]
    # │ KAPAN   : berhenti kuliah; stres keluarga turun; Rina sekutu
    # │ ISI SKRG: merintis label fesyen kecil bersama Rina; adik-adik membantu
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-08"] = """Garasi keluarga berubah menjadi ruang kerja dengan dua meja, kain sisa, dan kotak pesanan yang tidak pernah benar-benar seragam. Moeka tidak kembali ke jalur kuliah yang dahulu dibayangkan. Ia dan Rina mulai membangun label kecil dari pekerjaan yang cukup sedikit untuk dipelajari dan cukup nyata untuk menghasilkan sesuatu.

Adik-adiknya membantu melipat, menempel label, lalu bertengkar soal siapa yang paling berjasa. Moeka mengusir mereka ketika mulai mengantuk, tidak lagi menerima semua pengorbanan sebagai hal yang otomatis baik. Beban keluarga yang mereda memberinya ruang untuk memilih desain karena suka.

Tidak setiap bulan untung. Ada kiriman salah dan pesanan yang dibatalkan. Tetapi saat nama label pertama kali dicetak, Moeka menangis di depan Rina tanpa lelucon untuk menutupinya. Masa depan itu kecil, belum pasti, dan akhirnya mempunyai bentuk yang ikut ia tentukan."""

    # ┌─ ENDING · E-MO-09 · Banding yang Dimenangkan  [Netral · host Y/C]
    # │ KAPAN   : beasiswa diselamatkan lewat Fujisawa, Sato, atau banding
    # │ ISI SKRG: lulus; keluarga bertahan; tanpa romansa
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-09"] = """Surat banding dikabulkan setelah Moeka berulang kali mengira tidak akan sanggup menambahkan satu dokumen lagi. Fujisawa, Sato, dan orang-orang yang membantunya tidak mengubah persoalan menjadi sekadar nasihat agar lebih pandai mengatur waktu. Ada beban nyata yang akhirnya diakui dalam penilaian.

Ia mempertahankan beasiswa dan menyelesaikan kuliah. Keluarganya bertahan, belum tanpa kesulitan, tetapi tidak lagi menggantungkan seluruh rencana pada Moeka yang harus selalu sanggup. Ia belajar membicarakan bantuan sebelum menyerahkan jatah makan atau tidur sebagai jawaban pertama.

Tidak ada romansa yang menutup kelulusannya. Rina datang, adik-adiknya ribut di belakang kamera, dan Moeka tertawa karena foto pertama gagal. Di antara semua formulir yang pernah membuatnya merasa hanya angka yang terancam hilang, ijazah itu kini dipegang seseorang yang masih punya waktu untuk membayangkan hidup sesudahnya."""

    # ┌─ ENDING · E-MO-10 · Doa yang Tidak Terkabul  [Netral · host Y/C]
    # │ KAPAN   : ayah_status meninggal; minimal 3 jendela diambil
    # │ ISI SKRG: ayahnya meninggal; Moeka bertahan karena tidak sendirian
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-10"] = """Ayah Moeka meninggal meskipun ia telah berdoa, bekerja, dan mencoba membawa pulang lebih dari yang sanggup dibawanya. Untuk beberapa waktu ia memandang setiap istirahat sebagai sesuatu yang mungkin telah mengambil kesempatan terakhir untuk menolong.

Orang-orang di sisinya tidak membiarkan pikiran itu menjadi satu-satunya suara. Mereka datang dengan makanan, menemani urusan rumah, dan mendengarkan cerita tentang ayahnya sebagai manusia yang lebih luas daripada penyakit. Moeka boleh marah kepada doa yang tidak terkabul tanpa dianggap berhenti menyayangi keluarganya.

Ia bertahan. Duka tidak menghilang pada hari ia kembali tertawa, sebagaimana tawa tidak membatalkan kehilangan. Pada peringatan berikutnya ia membawa desain yang belum sempat diperlihatkan kepada ayah. Sesudah pulang ia menelepon seseorang dan mengatakan malam itu terasa berat. Kali ini ia tidak mengucapkan tidak apa-apa sebelum jawaban datang."""

    # ┌─ ENDING · E-MO-11 · Topeng yang Pecah  [Hancur · host Y/C]
    # │ KAPAN   : pemain pelaku Force terhadapnya
    # │ ISI SKRG: risiko krisis melonjak; jendela intervensi tetap ada; tidak ada ending tenang
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-11"] = """Kekerasan yang kaulakukan merusak tempat terakhir tempat Moeka mengira boleh menurunkan kewaspadaan. Ia mencoba kembali tertawa, lalu merasa mual saat mendengar suaranya sendiri. Orang yang sebelumnya menganggapnya selalu baik kini harus belajar bahwa senyum tidak pernah dapat dipakai sebagai bukti ia menyetujui atau telah pulih.

Risiko krisisnya meningkat. Rina, keluarga, dan bantuan profesional tetap dapat menjangkaunya; tidak satu pun kesempatan itu menjadikan pelaku sebagai pusat pemulihan. Ia tidak berutang penjelasan, pertemuan, atau cinta kepadamu karena pernah mempercayaimu.

Pada hari evaluasi tidak ada ketenangan yang pantas disebut hasil hubungan kalian. Ada kehidupan yang perlu dilindungi dari akibat perbuatanmu, dan seorang perempuan yang tetap memiliki masa depan meskipun belum sanggup membayangkannya. Topeng yang pecah tidak menyingkap milikmu. Ia memperlihatkan seseorang yang selama ini kaulukai."""

    # ┌─ ENDING · E-MO-12 · Selamat, Tapi Bukan Karenamu  [Netral · host Y/C]
    # │ KAPAN   : pemain melewatkan banyak jendela; orang lain menyelamatkannya
    # │ ISI SKRG: ia hidup dan memutus hubungan dengan pemain
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-12"] = """Moeka tetap hidup. Kabar itu sampai kepadamu melalui orang lain, dengan penjelasan sesingkat yang memang ingin ia berikan. Ada orang yang datang ketika ia membutuhkan pertolongan; kali ini namamu tidak berada dalam cerita tersebut.

Sesudah cukup kuat menentukan batas, ia memutus hubungan denganmu. Ia tidak menyusun daftar kesempatan yang terlewat agar kau dapat memperdebatkan mana yang sebenarnya bukan kewajibanmu. Ia hanya mengatakan tidak ingin melanjutkan kedekatan yang membuatnya semakin sendirian.

Kau masih melihat wajahnya di foto teman. Kadang ia tersenyum, kadang memilih tidak ikut dipotret. Hidup itu berlangsung di luar aksesmu. Menyesali jarak tidak memberimu hak memasuki lagi ruang yang ia tutup. Moeka selamat, dan salah satu keputusan yang dapat ia ambil sesudahnya adalah memilih siapa yang tidak lagi ingin dibawa ke masa depan."""

    # ┌─ ENDING · E-MO-13 · Ginjal untuk Ayah  [Romantis · host Y/C]
    # │ KAPAN   : cabang donor diambil; pemain mendampingi
    # │ ISI SKRG: ayah pulih; Moeka cuti; pengorbanan yang tidak ia sesali
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-MO-13"] = """Keputusan donor dijalani setelah penilaian dan pembicaraan yang memberi Moeka ruang sungguhan untuk memahami serta menolak. Kau mendampinginya tanpa menyebut keberanian sebagai kewajiban seorang anak. Ketika keluarganya mengetahui, mereka harus membicarakan ketakutan yang selama ini saling disembunyikan demi tidak membebani.

Ayahnya pulih. Moeka mengambil cuti dan menjalani pemulihan sendiri, tidak langsung kembali mengejar semua pekerjaan yang tertunda. Ia tidak menyesali pilihannya, tetapi belajar bahwa keputusan yang dipilih dengan cinta tetap memerlukan perawatan, waktu, dan dukungan setelahnya.

Hubungan kalian tumbuh di hari yang lambat: berjalan sebentar, makanan yang tidak selalu dihabiskan, kegelisahan tentang studi yang didengarkan tanpa disuruh bersyukur saja. Moeka mulai membicarakan rencana kembali kuliah. Untuk pertama kalinya dalam waktu lama, masa depan ayah dan masa depannya sendiri tidak harus ditempatkan sebagai dua hal yang saling mengorbankan."""


    # ═════ Shiori ═════
    # ┌─ ENDING · E-SH-01 · Lawan Tanding Seumur Hidup  [Romantis · host Y/C]
    # │ KAPAN   : respek ≥ 80; Trust ≥ 80; tidak ada kebohongan yang ia temukan sendiri; lulus semua ujiannya; tanpa Force
    # │ ISI SKRG: lawan tanding sekaligus pasangan; ambang romansa tertinggi di seluruh game
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-01"] = """Shiori berhenti menyebut setiap pertemuan sebagai alasan untuk bermain. Pada suatu sore ia mengajakmu makan dan mengatakan ingin duduk bersamamu tanpa papan di tengah. Ketika kau menggoda bahwa undangan itu terlalu jujur, ia tersenyum lalu mengakui sudah terlalu lama memikirkan cara mengucapkannya.

Kepercayaan kalian tidak terbentuk karena tak pernah berselisih, melainkan karena kau memilih mengatakan hal sulit sebelum dipaksa oleh bukti. Ia pun belajar menyebut cemburu atau terluka tanpa menjadikannya ujian yang tak diketahui aturannya oleh orang lain.

Kalian masih bertanding. Kadang ia menang, kadang ia meminta satu ronde lagi dengan nada yang terlalu tenang. Namun ketika papan ditutup, tidak ada yang perlu membawa pulang ketakutan bahwa kalah berarti kehilangan hak dicintai. Lawan sepadan itu kini juga orang yang boleh melihatnya tak memiliki langkah yang sudah disiapkan."""

    # ┌─ ENDING · E-SH-02 · Skakmat  [Buruk · host Y/C]
    # │ KAPAN   : tahap 5; sasaran pemain; tanpa pengakuan
    # │ ISI SKRG: pemain dikeluarkan dan dijauhi semua lingkungan; semua target quest menjauh
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-02"] = """Akibat perbuatanmu tiba melalui pintu yang berbeda: panggilan kampus, orang yang menolak bertemu, kesempatan yang dibatalkan setelah fakta yang disimpan Shiori dibuka. Setiap keberatanmu menemui seseorang yang sudah mendengar cukup banyak untuk berhenti mempercayai penjelasanmu.

Kau dikeluarkan dan dijauhi lingkungan yang dahulu tampak dapat diatur satu per satu. Semua target quest menjauh; tidak ada lagi kedekatan yang bisa dipakai sebagai jalan memutar kembali ke kehidupan semula.

Shiori tidak datang menikmati pembelaan terakhirmu. Ia telah memastikan hasil yang diinginkannya lalu menutup akses. Pada pertemuan terakhir sebelum itu, senyumnya sama seperti ketika mengajak bermain pertama kali. Kau baru memahami betapa sedikit kesamaan ekspresi dapat menjelaskan apa yang sebenarnya sedang dilakukan seseorang kepadamu."""

    # ┌─ ENDING · E-SH-03 · Gencatan Senjata  [Netral · host Y/C]
    # │ KAPAN   : pemain mengaku di S22 atau S24
    # │ ISI SKRG: penghancuran berhenti; mereka tidak lagi bicara
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-03"] = """Kau mengaku sebelum seluruh akibat terakhir dijalankan. Shiori mendengar sampai selesai, meminta bagian yang kabur disebut lebih jelas, lalu mengatakan ia akan berhenti memperluas penghancuran. Ia tidak menyebutnya pengampunan.

Ada hal yang tetap harus kauselesaikan dan orang yang tetap berhak menolakmu. Shiori tidak menghapus keterangan yang benar hanya agar gencatan senjata terasa manis. Yang berakhir adalah keinginannya membuat setiap sisa kehidupanmu menjadi bagian dari pertarungan kalian.

Sesudahnya kalian tidak lagi berbicara. Jika berpapasan, ia tidak menyiapkan sindiran atau kesempatan kedua. Keheningan itu bukan undangan menunggu sampai amarahnya reda. Ia memilih hidup yang tidak memerlukan namamu hadir setiap hari, dan kau ditinggalkan dengan tanggung jawab yang tak lagi bisa kauserahkan kepada permusuhannya."""

    # ┌─ ENDING · E-SH-04 · Ratu Tanpa Kepercayaan  [Terdistorsi · host Y/C]
    # │ KAPAN   : tahap 5 tuntas; tidak ada yang ia percaya lagi
    # │ ISI SKRG: Shiori menang tetapi kehilangan kemampuan percaya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-04"] = """Shiori menang. Orang yang ingin dijatuhkannya kehilangan tempat, kebohongan dibuka, dan hampir tidak ada hasil yang menyimpang dari yang telah diperhitungkan. Kemenangan itu memberinya kendali yang dahulu dirampas pengkhianatan.

Ia tidak mendapatkan kembali kemudahan percaya. Undangan tulus dibaca sebagai kemungkinan motif, bantuan diperiksa untuk mencari harga, dan setiap kedekatan dipertahankan pada jarak yang memungkinkan ia pergi lebih dahulu. Orang tuanya tetap menyayanginya, tetapi bahkan dukungan mereka sering ia sambut sebagai sesuatu yang harus dibuktikan lagi.

Di klub, orang menyebutnya lebih mengagumkan daripada sebelumnya. Ia tersenyum, menata bidak, dan menunggu lawan berikutnya. Di luar papan ia tidak lagi tahu bagaimana menginginkan seseorang tinggal tanpa sekaligus menyusun cara menghukum jika orang itu kelak pergi. Segala sesuatu telah dapat dipertahankan, kecuali tempat untuk merasa aman di dalam kemenangan."""

    # ┌─ ENDING · E-SH-05 · Langkah Koita  [Koita · host Y/C]
    # │ KAPAN   : cinta Koita tumbuh di S08; Koita memilihnya di K26
    # │ ISI SKRG: jalur manga; deviasi rendah untuk Shiori
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-05"] = """Shiori mengingat setahun perkenalan mereka sebelum Koita menyadari ia sedang menghitung hari. Ketulusan yang semula dianggapnya kecerobohan ternyata menembus bagian hidup yang jarang bisa dicapai orang yang lebih pandai menyusun perkenalan.

Namun saat Koita memilihnya, ia tetap meminta jawaban yang jelas tentang orang-orang lain. Kekaguman tidak membuat Shiori tiba-tiba mau menjadi bagian dari penantian yang sama. Koita menjawab dan menyelesaikan percakapan yang dahulu dihindarinya.

Ia belajar menerima bahwa Koita tidak selalu secepat dirinya memahami keadaan. Koita belajar bahwa senyum Shiori tidak otomatis berarti baik-baik saja. Pada hari mereka berkencan tanpa alasan festival atau kebetulan hujan, Shiori datang lebih awal, lalu tampak sedikit kesal karena kegembiraannya ternyata cukup mudah dibaca."""

    # ┌─ ENDING · E-SH-06 · Sekutu di Papan yang Sama  [Netral · host Y/C]
    # │ KAPAN   : pemain memberitahunya soal Sistem; tahu_sistem percaya
    # │ ISI SKRG: Shiori menjadi ahli strategi pemain melawan naskah; persahabatan, bukan cinta
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-06"] = """Shiori tidak langsung mempercayai cerita tentang Sistem. Ia meminta membedakan yang dapat diamati dari yang hanya diberitahukan kepadamu, lalu menguji bagian yang bisa diperiksa tanpa memperlakukan orang lain sebagai korban percobaan.

Ketika akhirnya menerima bahwa ada naskah yang ikut menggeser keadaan, ia memilih menjadi sekutumu melawan kuasanya. Persahabatan itu memiliki syarat yang jelas: informasi dibagikan, keputusan yang menyangkut orang lain tidak diambil sendirian, dan angka keberhasilan bukan alasan membenarkan luka.

Tidak ada pengakuan cinta yang menutup kerja sama mereka. Shiori masih bisa marah kepadamu dan tetap datang membawa pertanyaan yang belum terpikir. Di meja yang sama, kalian belajar bahwa menolak sebuah naskah juga berarti berhenti meniru kebiasaannya menempatkan manusia sebagai bidak yang boleh dikorbankan demi akhir yang menarik."""

    # ┌─ ENDING · E-SH-07 · Pewaris dengan Caranya Sendiri  [Netral · host Y/C]
    # │ KAPAN   : tanpa rute aktif; S17 didukung
    # │ ISI SKRG: fokus karier; membatalkan pertunangan Tojo dengan strateginya sendiri
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-07"] = """Shiori membatalkan arah pertunangan dengan Tojo melalui keputusan yang dapat dipertahankannya sendiri. Orang tuanya mendengar, mendukung, dan mengingatkan bahwa ia tidak perlu menyelesaikan seluruh akibat sosial sendirian hanya untuk membuktikan mampu.

Ia memilih fokus pada studi dan tanggung jawab yang memang ingin diterima. Tidak ada pasangan yang dijadikan bukti kemenangan atau kemerdekaan. Kedekatan keluarga tetap punya tempat, juga orang-orang yang dapat mengkritik langkahnya tanpa takut dibalas.

Pada pertemuan bisnis pertama yang dipimpinnya, Shiori meminta pendapat seseorang yang tidak sepakat. Ia mendengarkan sampai selesai sebelum membantah. Menjadi pewaris dengan caranya sendiri ternyata tidak hanya soal berhak menentukan langkah; ia juga perlu tahu kapan kekuasaan membuat ruangan terlalu sunyi untuk memberi jawaban yang jujur."""

    # ┌─ ENDING · E-SH-08 · Bidak Bernama Tojo  [Terdistorsi · host Y/C]
    # │ KAPAN   : S21 Tojo dipakai sampai M35
    # │ ISI SKRG: pertunangan tanpa cinta sebagai hukuman bagi dirinya sendiri; ia tetap tersenyum di setiap foto; ikatan sosial, bukan pasangan romantis baru
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-08"] = """Shiori mempertahankan pertunangan dengan Tojo meskipun tak ada cinta di dalamnya. Keluarganya memberi kesempatan membatalkan, tetapi ia menolak, terlalu jauh menjadikan hubungan tersebut alat untuk menang dan hukuman bagi dirinya sendiri karena pernah percaya dengan ceroboh.

Tojo mendapat foto dan pengumuman yang diinginkan lingkungannya. Shiori mendapat posisi yang dapat dipakai, bersama hari-hari yang semakin terasa seperti perpanjangan acara formal. Mereka belajar tersenyum pada saat yang sama tanpa harus saling mengenal lebih jauh.

Kuroiwa pernah bertanya apakah ia masih ingin menjalaninya. Shiori menjawab sudah memutuskan. Ia tidak mengatakan bahagia. Dalam setiap foto berikutnya senyumnya tetap sempurna, dan semua orang yang hanya melihat hasilnya dapat mengira dua hal itu berarti sama."""

    # ┌─ ENDING · E-SH-09 · Ratu Menjatuhkan Protagonis  [Khusus · host Y/C]
    # │ KAPAN   : sasaran_balas Koita
    # │ ISI SKRG: Koita dijatuhkan di depan semua orang; deviasi sangat tinggi; E-KO-09 terkunci
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-09"] = """Koita kehilangan kendali atas cara ceritanya dibaca. Orang-orang yang dahulu mendengar penjelasan terpisah akhirnya melihat pola bersama, dan Shiori memastikan ia tidak dapat lagi berlindung dalam citra pemuda yang sekadar terlalu baik untuk menolak.

Ia jatuh di depan lingkungan yang paling mengenalnya. Ada tuduhan yang dapat dijawab dengan fakta, ada luka yang tak selesai oleh pembelaan bahwa ia tidak pernah bermaksud menyakiti. Setelah hari itu, sapaan hangat yang diandalkannya tidak lagi cukup membuat orang mau tinggal.

Shiori mendapat hasil yang diinginkan. Ia melihat Koita berusaha menahan wajah tetap biasa dan mengetahui tepat kapan usaha itu gagal. Yang tersisa bukan perasaan puas yang sesederhana dugaan semula, melainkan keputusan untuk tetap menyebut akibat tersebut layak. Ratu telah menjatuhkan protagonis; orang-orang di sekelilingnya kini harus menjalani hidup setelah pertunjukan selesai."""

    # ┌─ ENDING · E-SH-10 · Keadilan yang Tersenyum  [Khusus · host Y/C]
    # │ KAPAN   : sasaran_balas Ogawa, Kuga, atau Mei; pemain memberi bukti
    # │ ISI SKRG: pelaku dijatuhkan; Shiori dan pemain menjadi sekutu yang saling waspada
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-10"] = """Bukti yang kauberikan membantu Shiori menjatuhkan pihak yang telah memakai orang lain: Ogawa, Kuga, atau Mei, sesuai perbuatan yang akhirnya dapat dibuktikan. Kuasa yang mereka andalkan mulai kehilangan perlindungan ketika cerita tak lagi dapat dikendalikan satu pihak.

Orang-orang yang dilukai tetap memerlukan dukungan setelah hasil itu tiba. Shiori tidak berhak menjadikan pemulihan mereka panggung untuk menunjukkan kecerdasannya, dan kau beberapa kali mengingatkan hal tersebut dengan hati-hati. Ia mendengar, meski tidak selalu menyukai waktunya.

Kalian menjadi sekutu yang tahu cukup banyak tentang kemampuan satu sama lain untuk tidak sepenuhnya santai. Ada hormat, ada kewaspadaan, dan sebuah kesepakatan bahwa kebenaran harus tetap dapat diperiksa bahkan ketika hasilnya terasa memuaskan. Senyum Shiori kembali hangat pada beberapa hari, tanpa membuat siapa pun lupa seberapa jauh ia bersedia bergerak saat merasa perlu."""

    # ┌─ ENDING · E-SH-11 · Jalur Hukum  [Hancur · host Y/C]
    # │ KAPAN   : pemain pelaku Force terhadapnya
    # │ ISI SKRG: Rute Revenge teraktivasi paling cepat lewat hukum dan sosial; pemain dikeluarkan dan dipenjara; tanpa romansa
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-11"] = """Shiori menempuh jalan hukum setelah kekerasan yang kaulakukan. Keluarga dan Kuroiwa mendampinginya tanpa menganggap ketenangan wajahnya berarti ia tidak memerlukan pertolongan. Ada hari ia mampu menjelaskan dengan jelas; ada hari pertemuan harus ditunda karena tubuhnya menolak berada di ruangan yang mengingatkannya pada kejadian.

Proses akademik mengakhiri tempatmu di kampus, lalu proses pidana berakhir dengan hukuman penjara. Pengaruh sosial mempersempit akses yang dahulu memudahkanmu menghindari akibat, tetapi hasil tersebut tidak mengembalikan hari-hari Shiori seperti semula.

Ia tidak menyebut penuntutan sebagai cara mendapatkanmu kembali dalam bentuk lain. Tidak ada romansa yang bertahan di balik kekerasan. Ketika namamu akhirnya tidak perlu disebut setiap minggu, Shiori meminta semua orang berhenti menanyakan apakah ia puas. Ia ingin hidupnya mempunyai lebih banyak isi daripada hasil hukuman seseorang yang pernah melukainya."""

    # ┌─ ENDING · E-SH-12 · Shena dan Pembacanya  [Romantis · host C]
    # │ KAPAN   : Chiasa mengaku sebagai Shena sebelum Shiori menemukannya sendiri; respek ≥ 70; tanpa kebohongan lain yang ia temukan
    # │ ISI SKRG: pembaca dan ilustratornya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-12"] = """Chiasa mengakui dirinya Shena sebelum Shiori mengubah kesamaan kecil menjadi kesimpulan yang pasti. Ia membawa cerita tentang pekerjaan, keterbatasan, dan hal yang sulit dijelaskan, memberi Shiori kesempatan menilai kebenaran tanpa terlebih dahulu harus membongkar kebohongan.

Shiori tetap pembaca yang cerewet. Ia mengingat ilustrasi lama yang bahkan pembuatnya sudah lupa, menanyakan keputusan warna, lalu mendengarkan ketika Chiasa mengatakan ada hal yang belum dapat dikerjakan seperti dulu. Kekaguman pada karya tidak dijadikan syarat agar orang di depannya terus sama dengan harapannya.

Hubungan tumbuh dari keberanian untuk terlihat tanpa seluruh keahlian sebagai pelindung. Pada buku berikutnya Shiori melihat namanya dalam ucapan terima kasih, kecil di antara yang lain. Ia menggoda tentang ukuran huruf, kemudian menyimpan dua eksemplar tanpa menganggap perlu menjelaskan mengapa satu saja tidak cukup."""

    # ┌─ ENDING · E-SH-13 · Shena dan Penipunya  [Buruk · host C]
    # │ KAPAN   : Chiasa berbohong soal Shena lalu ketahuan
    # │ ISI SKRG: revenge menyasar karier Shena dan rahasia Chiasa
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-13"] = """Kebohongan Chiasa tentang Shena terbuka setelah kesempatan mengaku berkali-kali dilewatkan. Shiori tidak hanya kehilangan kepercayaan pada satu cerita; ia harus membaca ulang percakapan yang dahulu dianggap sebagai pertemuan tulus dengan seseorang yang dikagumi.

Balasannya menyasar tempat kebohongan itu memperoleh manfaat. Karier Shena diperiksa, relasi profesional menuntut penjelasan, dan rahasia Chiasa yang selama ini disimpan dalam lingkungan terpisah bertemu di hadapan orang-orang yang sama. Tidak ada lagi kemudahan mengganti versi berdasarkan siapa yang bertanya.

Chiasa berusaha menjelaskan bagian yang sulit dipercayai. Shiori meminta bukti dan menolak menyebut keterlambatan sebagai keberanian. Kekaguman seorang pembaca telah berubah menjadi ketelitian seorang lawan yang terluka. Setiap halaman yang dahulu mempertemukan mereka kini juga mengingatkan hal yang sengaja disembunyikan di luar gambar."""

    # ┌─ ENDING · E-SH-14 · Lawan Tanpa Nama  [Romantis · host Y/C]
    # │ KAPAN   : akun anonim aktif lama; pemain mengaku sendiri sebelum ketahuan; respek ≥ 70; tanpa kebohongan lain yang ia temukan
    # │ ISI SKRG: lawan online yang ia tunggu tiap malam ternyata duduk di kelasnya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-14"] = """Kau mengaku sebagai lawan anonim yang selama ini ditunggu Shiori pada malam hari. Ia memeriksa beberapa percakapan untuk memastikan, lalu menatapmu dengan kesal yang tidak sepenuhnya berhasil menutupi kegembiraan.

Ia menanyakan mengapa identitas itu disimpan dan mendengar jawabanmu sebelum menetapkan apa artinya. Pengakuan yang datang atas kemauan sendiri membuat kedekatan daring tidak berubah menjadi bukti bahwa seluruh pertemuan kalian telah disusun untuk mempermainkannya.

Kini lawan di layar dapat duduk di hadapannya. Ada kecanggungan baru ketika giliran bergerak bercampur dengan keinginan memperhatikan tangan atau wajah orang lain. Pada malam pertama sesudah kencan, Shiori tetap mengirim undangan bermain. Ia menambahkan pesan bahwa kali ini ia tahu siapa yang ditunggu, dan ternyata menunggu itu menjadi lebih sulit."""

    # ┌─ ENDING · E-SH-15 · Pion di Papan Orang Lain  [Terdistorsi · host Y/C]
    # │ KAPAN   : Shiori memegang semua rahasia pemain tetapi memilih tidak menghancurkannya
    # │ ISI SKRG: pemain tetap kuliah dan tampak bebas, tetapi setiap langkahnya kini atas izin Shiori; ia tersenyum setiap kali mereka berpapasan
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-15"] = """Shiori tidak menghancurkan hidupmu. Kau tetap kuliah, tetap datang ke tempat biasa, tetap tampak bebas bagi orang yang hanya mengenal permukaan. Syaratnya muncul dalam pesan pendek yang tidak pernah perlu ditulis sebagai ancaman karena kalian sama-sama tahu apa yang disimpan di belakangnya.

Kau mulai meminta izin sebelum membuat keputusan yang dahulu sederhana. Siapa yang ditemui, kapan pergi, bagian mana yang boleh diceritakan: setiap pilihan diperiksa terhadap kemungkinan membuatnya memakai pengetahuan yang kini hanya ditahan.

Jika berpapasan, Shiori tersenyum dengan sopan. Orang lain menganggap kalian akrab. Kau tahu keramahan itu bukan jaminan keselamatan, hanya pengingat bahwa kehancuran belum dipilih hari ini. Menjadi pion yang tetap berdiri ternyata memberi lebih banyak waktu untuk takut daripada dikeluarkan dari papan sekaligus."""

    # ┌─ ENDING · E-SH-16 · Senyum Terakhir  [Buruk · host Y/C]
    # │ KAPAN   : S-D15 umpan berhasil; pemain membuka rahasia terakhirnya padanya
    # │ ISI SKRG: pemain mengira sudah memenangkan hatinya; di M35 Shiori menunjukkan papannya, dan semuanya runtuh dalam satu hari
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SH-16"] = """Kau mengira Shiori akhirnya menyerahkan kepercayaannya. Ada percakapan pribadi, senyum yang tampak lebih dekat, dan kesempatan menjelaskan rahasia terakhir dengan keyakinan bahwa kedekatan telah membuat kalian berada di pihak yang sama.

Pada hari evaluasi, ia menunjukkan apa yang sebenarnya telah dipahami. Cerita yang kaubawa sebagai kemenangan bertemu bukti dan akibat yang disusun tanpa sepengetahuanmu. Dalam satu hari, hubungan, akses, dan posisi yang dahulu terasa kokoh kehilangan tempat untuk berdiri.

Shiori tersenyum ketika kau menyebut perasaannya. Ia tidak memberimu kepastian apakah pernah ada sesuatu yang tulus di antara langkah-langkah itu. Kau ditinggalkan dengan kenangan yang kini tidak bisa dibaca tanpa takut. Kekalahan terakhirnya bagimu adalah merampas kemudahan mempercayai versimu sendiri tentang bagaimana kau pernah dicintai."""


    # ═════ Chiasa ═════
    # ┌─ ENDING · E-CH-01 · Rumah Kita Sendiri  [Romantis · host Y]
    # │ KAPAN   : Yutaka mengejar Chiasa; curiga identitas rendah atau diterima
    # │ ISI SKRG: dua orang yang sama-sama kesepian membangun rumah sendiri
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-01"] = """Chiasa memilih tirai untuk rumah yang tak perlu lagi menyesuaikan diri dengan kebiasaan Koita. Yutaka menanyakan warna yang ia sukai, lalu menerima ketika jawabannya berubah setelah melihat cahaya sore. Tidak ada yang menyebut perubahan kecil itu merepotkan.

Mereka sama-sama mengenal kesepian dan belajar agar pengetahuan itu tidak menjadi alasan menahan pasangan dari kehidupan di luar rumah. Chiasa tetap menggambar; Yutaka punya tanggung jawab yang tidak selalu membuatnya bisa pulang cepat. Ada pesan yang dijawab terlambat tanpa langsung menjadi sidang tentang kesetiaan.

Kunci mereka diletakkan pada dua kait sejajar. Rumah itu tidak menjanjikan bahwa tak seorang pun akan pernah ingin pergi. Ia memberi alasan untuk kembali, dengan tempat yang dibangun oleh dua orang yang masih boleh menginginkan sesuatu miliknya sendiri."""

    # ┌─ ENDING · E-CH-02 · Diterima  [Koita · host Y]
    # │ KAPAN   : Koita Success NPC; Daisuke dan Yoshie menerima
    # │ ISI SKRG: saudara tiri menjadi pasangan dengan restu keluarga
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-02"] = """Daisuke dan Yoshie menerima hubungan Koita dan Chiasa setelah percakapan yang tidak dapat selesai dalam satu malam. Penerimaan itu tidak menghapus kecanggungan saat panggilan lama terdengar dalam arti baru, tetapi membuat rumah tidak lagi menuntut keduanya berbohong demi dapat duduk bersama.

Chiasa semula menyangka pengakuan Koita akan mengakhiri seluruh takutnya. Ia menemukan masih perlu belajar memberi ruang, tidak memeriksa setiap keterlambatan sebagai kemungkinan ditinggalkan. Koita pun tidak lagi boleh bersembunyi di balik kebiasaan serumah untuk menunda jawaban.

Pada makan malam pertama sesudah keputusan keluarga, Chiasa mengambil piring untuk dirinya lebih dahulu. Sesuatu yang kecil berubah: ia tidak harus menyediakan segalanya agar tempatnya tetap diakui."""

    # ┌─ ENDING · E-CH-03 · Berpisah Baik-baik  [Netral · host Y]
    # │ KAPAN   : Koita Success NPC; keduanya memilih berpisah
    # │ ISI SKRG: tetap keluarga, dengan bekas yang hangat
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-03"] = """Chiasa dan Koita memilih mengakhiri arah romantis yang pernah dicoba. Mereka tidak menamainya kesalahan yang membuat seluruh kedekatan lama kotor. Ada perasaan yang nyata, ada batas dan masa depan yang akhirnya tidak ingin diteruskan bersama.

Kembali menjadi keluarga memerlukan jarak. Chiasa berhenti menyiapkan rutinitas untuk memastikan Koita selalu pulang kepadanya; Koita tidak lagi memakai kelembutan yang ambigu saat merasa sepi. Keduanya perlu menerima kehilangan tanpa meminta yang lain segera bersikap biasa.

Suatu hari mereka kembali makan di meja yang sama dan membicarakan hal sederhana tanpa mempertahankan peran. Bekasnya tetap ada, tetapi tidak semua bekas harus menjadi luka yang terus dibuka. Rumah mereka pelan-pelan menemukan cara menampung keluarga yang sudah berubah."""

    # ┌─ ENDING · E-CH-04 · Dipisah Paksa  [Buruk · host Y]
    # │ KAPAN   : Koita Success NPC; keluarga menolak keras
    # │ ISI SKRG: Chiasa dipindahkan atau Koita pergi
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-04"] = """Penolakan keluarga berakhir dengan pemisahan tempat tinggal. Koper disiapkan sebelum cukup banyak percakapan berlangsung, membuat Chiasa merasa keputusan tentang tubuh dan jaraknya kembali diambil oleh orang lain.

Koita mungkin yang pergi, mungkin Chiasa yang dipindahkan; rumah yang ditinggalkan keduanya sama-sama kehilangan keseharian yang dahulu terasa aman. Panggilan telepon menjadi pendek, penuh pertanyaan yang harus dijawab hati-hati agar tak membangkitkan pertengkaran berikutnya.

Pemisahan tidak otomatis mematikan perasaan, juga tidak membuatnya lebih luhur. Chiasa harus belajar hidup di tempat yang tidak dibangun dari jam pulang Koita. Pada hari evaluasi, ia masih menyimpan satu barang dari rumah, belum tahu apakah benda itu akan membantu merawat kenangan atau membuatnya terus merasa belum sungguh pergi."""

    # ┌─ ENDING · E-CH-05 · Digantung Lagi  [Buruk · host Y]
    # │ KAPAN   : Koita Success NPC; Koita kembali ke pola lama
    # │ ISI SKRG: Chiasa menjadi korban terbaru pola Koita
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-05"] = """Koita sempat memberi jawaban yang jelas. Chiasa memegangnya terlalu erat ketika perhatian Koita mulai kembali dibagikan dalam bentuk yang sulit dipertanyakan satu per satu. Ia tahu kalimat menenangkan yang dipakai karena dahulu sering mendengarnya ditujukan kepada orang lain.

Kini ia berada di dalam pola itu. Setiap keberatan disebut terlalu sensitif, setiap janji baru cukup hangat untuk menunda keberanian pergi. Tinggal serumah membuatnya lebih dekat dan sekaligus lebih sulit mengambil jarak.

Chiasa mulai menunggu bunyi kunci dengan perasaan yang berubah-ubah: lega, marah, lalu malu karena masih lega. Yang paling pahit adalah mengetahui ia dahulu mengira kedekatan keluarga akan membuatnya menjadi pengecualian. Koita kembali tidak memilih, dan ia menjadi orang berikutnya yang diminta menyebut penantian itu pengertian."""

    # ┌─ ENDING · E-CH-06 · Shena Saja  [Netral · host Y]
    # │ KAPAN   : tanpa romansa; Chiasa pindah dan fokus seni
    # │ ISI SKRG: karier ilustrasi berjalan; rumah ditinggalkan
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-06"] = """Chiasa memindahkan meja gambar sebelum tempat tidurnya. Di studio baru, barang pertama yang benar-benar mendapat tempat adalah lampu kerja, bukan foto keluarga atau benda yang mengingatkannya pada Koita.

Karier Shena berjalan. Ia belajar membuat janji profesional yang dapat ditepati tanpa menghabiskan seluruh malam, menerima kritik yang tidak perlu dianggap penolakan terhadap dirinya. Tidak ada hubungan romantis yang dijadikan pusat perpindahan itu.

Rumah Amamiya tetap dapat dihubungi, tetapi tidak lagi menentukan seluruh isi harinya. Chiasa kadang kesepian dan tetap memilih tinggal. Pada sampul berikutnya namanya kecil seperti biasa. Ia tahu berapa banyak hidup yang diperlukan untuk membuat gambar tersebut, dan kali ini cukup banyak bagian hidup itu memang dipilihnya sendiri."""

    # ┌─ ENDING · E-CH-07 · Tersisih Dua Kali  [Buruk · host Y]
    # │ KAPAN   : Rute BL berhasil; Chiasa tidak didekati
    # │ ISI SKRG: patah, menjauh dari keduanya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-07"] = """Hubungan Yutaka dan Koita menjadi nyata ketika Chiasa masih berusaha memahami mengapa tempatnya mendadak terasa berbeda. Ia kehilangan harapan pada Koita sekaligus kemudahan mencari penghiburan pada orang yang kini berada di sisinya.

Ia tidak bisa menuntut cinta sebagai upah karena tumbuh bersama. Mengetahui itu tidak membuat sakitnya menjadi lebih rapi. Untuk beberapa waktu ia menolak undangan yang akan mempertemukan mereka bertiga, memilih diam daripada harus menampilkan dukungan yang belum sanggup dirasakan.

Chiasa menjauh dari keduanya. Di kamar, ia menggambar sampai larut lalu berhenti sebelum kelelahan mengambil seluruh pikiran. Masa depannya belum menemukan bentuk lain, tetapi ia mulai mengerti bahwa memberi jarak tidak selalu berarti menghukum. Kadang itu satu-satunya cara agar dirinya tetap punya ruang untuk pulih."""

    # ┌─ ENDING · E-CH-08 · Sekutu Paling Setia  [Khusus · host Y]
    # │ KAPAN   : Rute BL; Yutaka jujur pada Chiasa sejak awal
    # │ ISI SKRG: Chiasa menjadi pendukung Yutaka × Koita di depan keluarga
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-08"] = """Yutaka mengatakan perasaannya kepada Chiasa sejak awal, sebelum kedekatan dengan Koita menjadi rahasia yang harus dibongkarnya sendiri. Chiasa terluka dan diberi waktu untuk mengatakannya tanpa langsung dituntut menjadi pendukung yang baik.

Ketika ia akhirnya berdiri di depan keluarga untuk membela hubungan mereka, ia tidak sedang menyerahkan hidupnya agar dua orang lain bahagia. Ia menyebut bahwa Koita harus menjawab sendiri, Yutaka harus bertanggung jawab atas pilihannya, dan keluarga perlu mendengar sebelum menganggap semua telah diputuskan bagi mereka.

Sesudah percakapan panjang, Chiasa pulang ke kamarnya dan menutup pintu untuk menggambar. Ia telah memilih menjadi sekutu. Dukungan itu berharga justru karena ia masih punya kehidupan yang tidak seluruhnya harus berputar di sekitar keduanya."""

    # ┌─ ENDING · E-CH-09 · Rumah yang Tidak Aman  [Hancur · host Y]
    # │ KAPAN   : pemain pelaku Force terhadapnya
    # │ ISI SKRG: tinggal serumah dengan Koita; Daisuke dan Yoshie kecewa; tanpa romansa dengan pelaku
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-09"] = """Kekerasanmu membuat Chiasa kehilangan rasa aman pada rumah dan pertemanan yang dahulu dianggap tak perlu dicurigai. Bunyi tamu datang cukup membuatnya berhenti bekerja. Ia marah pada tubuhnya sendiri karena masih takut, lalu perlahan belajar bahwa reaksi itu bukan bukti kelemahan atau kesalahan.

Ia tetap tinggal bersama Koita. Daisuke dan Yoshie pulang dengan kecewa serta amarah yang harus diarahkan kepada pelaku, bukan kepada keputusan Chiasa sesudahnya. Mereka mencari cara mendukung tanpa mengambil alih seluruh pilihannya.

Tidak ada cinta yang membuatmu berhak kembali. Rumah mulai menegakkan batas tentang siapa yang boleh masuk, dan namamu berada di sisi yang ditutup. Chiasa belum selalu dapat merasa aman di kamarnya, tetapi kunci itu kembali menjadi sesuatu yang boleh dipegang untuk melindungi dirinya."""

    # ┌─ ENDING · E-CH-10 · Adik yang Kembali  [Netral · host Y]
    # │ KAPAN   : tidak ada rute romansa dengan Chiasa; keluarga utuh
    # │ ISI SKRG: ia tetap adik Koita dan sahabat Yutaka
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-10"] = """Chiasa tetap menjadi adik Koita dan sahabat Yutaka tanpa hubungan romantis yang harus diberikan agar kedekatan mereka dianggap lengkap. Ia masih suka menggoda, tetapi mulai membedakan keakraban dari hak mengatur siapa yang boleh pulang terlambat.

Keluarga tetap utuh. Ada makan bersama yang tidak lengkap karena jadwal berbeda, ada tugas yang dibagi lebih adil, ada hari ketika Chiasa memilih menggambar daripada mengurus seluruh rumah. Koita belajar menanyakan sebelum mengandalkan kebiasaannya menyediakan.

Pada foto berikutnya ia tidak lagi berusaha selalu berdiri paling dekat. Rumah itu punya tempat baginya tanpa perlu diukur dari jumlah sentimeter di sebelah seseorang. Ia belum tahu seluruh yang akan diinginkan setelah wisuda, dan untuk sekarang ketidaktahuan tersebut tidak terasa seperti ancaman."""

    # ┌─ ENDING · E-CH-11 · Bukan Piala  [Buruk · host Y]
    # │ KAPAN   : Yutaka merebut Chiasa hanya untuk menyakiti Koita, lalu ketahuan
    # │ ISI SKRG: Chiasa menolak keduanya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CH-11"] = """Chiasa mengetahui bahwa kedekatan Yutaka dengannya semula dipakai untuk melukai Koita. Ia membaca ulang perhatian yang pernah menenangkan dengan perasaan mual: ada saat ia benar-benar didengar, dan ada saat lukanya hanya menjadi bukti bahwa seseorang telah menang.

Ia menolak Yutaka, lalu menolak berlindung kembali pada Koita hanya karena yang satu sudah membuatnya kecewa. Keduanya tidak diberi kesempatan menjadikan keputusan itu pertarungan lanjutan tentang siapa lebih pantas mendapatkannya.

Chiasa pergi dengan barang yang memang miliknya. Pada percakapan terakhir ia mengatakan tidak mau dibahas seperti benda yang direbut atau dikembalikan. Suaranya pelan dan sangat jelas. Sesudahnya ia tidak menunggu apakah mereka akhirnya memahami; ia perlu mulai menjalani hidup yang tak bergantung pada keberhasilan dua orang itu menghormatinya."""

    # ┌─ ENDING · E-CF-01 · Rumah Baru  [Romantis · host C]
    # │ KAPAN   : yuri dengan heroine utama; deviasi cukup
    # │ ISI SKRG: hidup bersama heroine; reaksi keluarga Amamiya menentukan nada epilog
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-01"] = """Kau dan perempuan yang memilih bersamamu menata rumah baru dari barang-barang yang tidak selalu cocok. Ada dua kebiasaan minum, dua jadwal, dan pembicaraan tentang ruang yang harus dapat dipakai sendiri tanpa dianggap sedang menjauh.

Reaksi keluarga Amamiya memberi warna pada hari pertama: dukungan dapat membuat kepindahan hangat, keraguan meninggalkan percakapan yang perlu dilanjutkan, penolakan membuat beberapa perayaan terasa kehilangan kursi. Hubungan kalian tidak otomatis menghapus bagian yang sakit itu.

Di rumah ini kau dipanggil Chiasa oleh seseorang yang mengenal pilihan-pilihanmu sekarang. Pertanyaan tentang identitas dan hidup yang diwarisi belum seluruhnya selesai. Namun kebersamaan tersebut mulai dapat diuji melalui hal nyata: kalian mendengar, bertengkar, mengoreksi, dan tetap memberi ruang agar cinta tidak berubah menjadi kewajiban untuk terus sama."""

    # ┌─ ENDING · E-CF-02 · Diterima  [Koita · host C]
    # │ KAPAN   : Koita Success; keluarga menerima
    # │ ISI SKRG: tabu yang direstui
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-02"] = """Keluarga menerima hubunganmu dengan Koita setelah perasaan yang selama ini disembunyikan akhirnya dibicarakan. Daisuke dan Yoshie perlu mendengar pilihan itu lebih dari sekali, memastikan tidak ada yang hanya mengikuti ketakutan kehilangan rumah atau perhatian.

Kau menjalani penerimaan itu dalam tubuh Chiasa, dengan kedekatan masa lalu yang tidak seluruhnya menjadi ingatanmu sendiri. Koita pun mulai mengenal dirimu sekarang sebagai seseorang yang boleh berbeda dari kebiasaan adiknya dahulu.

Panggilan Ko-nii masih datang pada saat tertentu, membawa sejarah yang tak dapat dirapikan dengan keputusan baru. Kalian tidak perlu berpura-pura semua mudah. Yang disetujui keluarga adalah ruang untuk menjalani pilihan secara bertanggung jawab, bukan jaminan bahwa satu pengakuan akan menghapus seluruh akibat atau keraguan."""

    # ┌─ ENDING · E-CF-03 · Berpisah Baik-baik  [Netral · host C]
    # │ KAPAN   : Koita Success; keduanya mundur
    # │ ISI SKRG: kembali menjadi adik tiri
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-03"] = """Kau dan Koita memilih mundur sebelum hubungan itu harus dipertahankan hanya karena sudah terlalu jauh untuk merasa boleh berhenti. Perasaannya tidak disangkal, tetapi tidak lagi dipakai menuntut masa depan yang salah seorang tak ingin jalani.

Kembali menjadi saudara tiri bukan gerakan yang menghapus semua kenangan. Kalian mengubah batas dalam keseharian: mengetuk pintu, bertanya sebelum menyentuh, tidak memakai kesepian sebagai alasan menghidupkan lagi harapan yang telah ditutup.

Sistem tetap menunggu evaluasi terhadap deviasi yang dibuat. Di luar perhitungannya, ada satu hubungan keluarga yang perlu dirawat dengan lebih jujur. Pada suatu pagi Koita menanyakan apakah kau mau sarapan bersama. Kau menjawab sesuai keinginan hari itu, tak lagi merasa setiap iya atau tidak harus menjelaskan seluruh perasaan di antara kalian."""

    # ┌─ ENDING · E-CF-04 · Dipisah Paksa  [Buruk · host C]
    # │ KAPAN   : Koita Success; keluarga memisahkan
    # │ ISI SKRG: salah satu meninggalkan rumah
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-04"] = """Keputusan keluarga memisahkan tempat tinggal datang lebih cepat daripada kesempatan menyepakati masa depan. Kau atau Koita harus pergi, dan rumah yang selama ini dapat dihafal lewat bunyinya mendadak menjadi tempat yang harus diingat dari jauh.

Kau menjalani perpindahan dengan barang Chiasa, pertanyaanmu sendiri, dan percakapan yang terputus ketika semua orang terlalu marah untuk mendengar. Kedekatan tidak lenyap hanya karena alamat berubah; justru pada beberapa malam ia terasa lebih sulit karena tak dapat lagi dijalani melalui hal biasa.

Sistem menilai perubahan tanpa memedulikan koper yang belum dibongkar. Bagimu akibatnya lebih konkret: tidak ada lagi kursi sarapan yang otomatis dapat diduduki. Hidup berikutnya tetap harus dibangun, sebelum kau tahu apakah perpisahan ini akan menjadi jeda, akhir, atau luka keluarga yang terlalu lama dibiarkan tanpa kata."""

    # ┌─ ENDING · E-CF-05 · Digantung Lagi  [Buruk · host C]
    # │ KAPAN   : Koita Success; Koita kembali menggantung
    # │ ISI SKRG: pemain merasakan pola Koita dari dalam
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-05"] = """Kau mengenali pola Koita karena telah melihatnya dari luar. Mengenali tidak membuatmu kebal saat pola itu mulai terasa sebagai harapan yang ditujukan kepadamu. Ia dekat, lalu kabur; ia hangat ketika takut kehilangan, lalu kembali samar saat merasa kau aman menunggu.

Kini pengetahuan katalog tak membantu menenangkan tubuh yang menunggu jawaban. Kau dapat menamai setiap penghindaran sambil tetap ingin mempercayai satu kalimat yang menjanjikan semuanya berbeda denganmu.

Chiasa tidak lagi sekadar tubuh yang kautempati atau hubungan yang bisa digeser dalam evaluasi. Kau hidup di dalam akibatnya, mengetahui bahwa orang dapat sangat sadar sedang disakiti dan tetap kesulitan pergi. Pada malam Koita terlambat pulang, kau mendapati dirimu menyiapkan dua piring, lalu berdiri lama sebelum memutuskan apa yang sebenarnya ingin dilakukan dengan yang kedua."""

    # ┌─ ENDING · E-CF-06 · Bersama Yutaka  [Koita · host C]
    # │ KAPAN   : Chiasa × Yutaka
    # │ ISI SKRG: hidup bersama Yutaka; lolos evaluasi hanya bila ada deviasi lain (bila tidak, E-SI-06)
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-06"] = """Yutaka mengajakmu membicarakan tempat tinggal sebelum memilih perabot. Ia ingin tahu bagaimana kau hendak bekerja, apa yang harus dibawa, dan apakah dekat kampus masih penting. Sikap hangatnya terasa berbeda saat tidak dipakai menebak jawaban paling mudah untuk semua orang.

Kalian mulai hidup bersama dengan kebiasaan yang perlu dipelajari. Ada saat kau merasa dicintai sebagai Chiasa yang dikenalnya dahulu, lalu perlu mengatakan bahwa keinginanmu kini berbeda. Yutaka belajar mendengar bagian itu tanpa menganggapnya penolakan atas seluruh kenangan.

Hubungan tersebut sendiri mengikuti kemungkinan yang juga dimiliki cerita lama. Ia tidak otomatis meloloskan evaluasi Sistem; deviasi lain tetap menentukan hasil akhirnya. Di meja dapur, kehidupan yang kaupilih terasa nyata. Kenyataan itu tidak membuat aturan penilaian menjadi lebih murah hati."""

    # ┌─ ENDING · E-CF-07 · Nama Pena yang Runtuh  [Buruk · host C]
    # │ KAPAN   : rahasia Shena terbongkar sebagai kebohongan
    # │ ISI SKRG: kontrak Mio diputus; pembaca marah
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-07"] = """Nama Shena runtuh ketika penjelasan tentang karya dan kemampuan yang berubah tidak lagi dapat dipertemukan. Mio meminta jawaban profesional, Haruka memandang garis yang tak sesuai kebohonganmu, dan pembaca bereaksi pada janji yang merasa pernah dibeli bersama buku.

Kontrak diputus. Kau kehilangan akses yang dahulu diwarisi begitu saja, bersama kenyamanan menganggap nama pena akan terus menanggung ketidaksanggupanmu menjadi pemiliknya yang lama.

Di meja ada kertas kosong yang tidak menuntut ditandatangani sebagai Shena. Namun memulai dari namamu sendiri terasa menakutkan ketika bahkan nama yang dipakai sehari-hari berasal dari kehidupan orang lain. Kerusakan karier itu tidak menentukan kau tak bisa belajar, tetapi ia mengakhiri kemudahan hidup dari kepercayaan yang belum sungguh dibangun oleh tanganmu sendiri."""

    # ┌─ ENDING · E-CF-08 · Gaya Baru Shena  [Romantis · host C]
    # │ KAPAN   : pemain belajar menggambar sungguhan sampai layak
    # │ ISI SKRG: Shena kembali dengan gaya baru; Mio dan Haruka menjadi saksi
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-08"] = """Garis barumu tidak persis seperti Chiasa dahulu. Setelah cukup lama belajar, kesamaan itu tidak lagi menjadi satu-satunya ukuran yang dikejar. Kau dapat menjelaskan keputusan gambar, menerima kritik, dan mengulang tanpa harus menyembunyikan seluruh proses di balik alasan sedang lelah.

Mio melihat pekerjaan yang dapat ditepati. Haruka melihat usaha yang tidak lagi hanya berlatih meniru. Ketika Shena kembali menerbitkan karya, pembaca masih memperdebatkan perubahannya, tetapi kali ini ada jawaban yang dapat kauakui sebagai hasil tanganmu sendiri.

Kedekatan yang menyertai jalan itu tumbuh melalui orang yang melihatmu gagal dan tetap mau mengenal. Pada malam karya selesai, kau mengirim foto sketsa pertama di sebelah hasil akhir. Bukan untuk membuktikan dirimu telah menjadi orang lama, melainkan bahwa hidup baru ini akhirnya mempunyai sesuatu yang benar-benar kaubuat."""

    # ┌─ ENDING · E-CF-09 · Rumah Amamiya Retak  [Buruk · host C]
    # │ KAPAN   : Koita Success atau kejahatan memecah keluarga
    # │ ISI SKRG: Daisuke dan Yoshie berpisah tempat; rumah sepi
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-09"] = """Rumah Amamiya tak lagi mampu menampung akibat yang dibawa hubungan atau kejahatan di dalamnya. Daisuke dan Yoshie tinggal terpisah, membawa pertanyaan berbeda tentang apa yang seharusnya diketahui lebih dahulu dan keputusan mana yang membuat keluarga kehilangan rasa aman.

Percakapan yang dahulu berakhir dengan siapa mau makan berubah menjadi urusan kapan mengambil barang. Koita dan Chiasa tetap membawa hubungan mereka ke mana pun tinggal, tetapi kenangan serumah tidak lagi cukup untuk mempertemukan semua orang di meja yang sama.

Kau mendengar ruang kosong dengan tubuh yang hafal suara rumah itu. Sistem mungkin mencatat perubahan besar. Bagimu perubahan itu juga berbentuk sandal yang tidak lagi berpasangan dekat pintu, satu lampu yang tak perlu dinyalakan, dan kebenaran bahwa tidak semua akibat dapat diperbaiki hanya karena penyesalan akhirnya datang."""

    # ┌─ ENDING · E-CF-10 · Studio Sendiri  [Netral · host C]
    # │ KAPAN   : tanpa romansa
    # │ ISI SKRG: mandiri di studio kecil; lolos atau tidaknya bergantung deviasi yang dibuat dengan cara lain
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-10"] = """Studio kecilmu memiliki meja yang hanya cukup untuk satu orang bekerja dengan nyaman. Kau memilihnya karena cahaya, biaya, dan kebebasan menutup pintu pada jam sendiri, bukan karena ada seseorang yang harus dipertahankan di dalamnya.

Tidak ada romansa yang menandai keberangkatan. Kau tetap terhubung dengan beberapa orang, mengambil jarak dari yang lain, dan belajar menjalani nama Chiasa tanpa setiap keputusan harus meniru harapan pemilik hidup sebelumnya.

Di luar jendela, tanggal evaluasi tetap mendekat. Kemandirian ini tidak otomatis berarti lolos; deviasi yang dibuat di tempat lain masih menentukan penilaian. Namun hari-hari sebelum putusan itu menjadi milikmu untuk dijalani dengan sungguh-sungguh. Kau menyelesaikan satu gambar, menyiapkan makan, dan menyadari hidup sendiri pun dapat berisi keputusan yang layak dipertahankan."""

    # ┌─ ENDING · E-CF-11 · Lingkaran yang Runtuh  [Buruk · host C]
    # │ KAPAN   : beberapa hubungan yuri sekaligus terbongkar
    # │ ISI SKRG: semua pergi bersamaan; lihat E-X-01
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-11"] = """Hubungan-hubungan yang kaubiarkan percaya pada kepastian berbeda akhirnya bertemu. Percakapan yang selama ini dijaga terpisah tidak lagi dapat ditutup dengan penjelasan yang berubah sesuai orang di hadapanmu.

Mereka pergi dengan cara berbeda. Ada yang memintamu mendengar marahnya sampai selesai, ada yang hanya mengirim satu kalimat, ada yang memerlukan teman agar sanggup mengambil barang. Kebersamaan tidak menjadi masalah karena jumlah orang semata, melainkan karena kehendak mereka ditentukan oleh informasi yang sengaja kausimpan.

Rumah kembali sepi. Kau tidak dapat menjadikan kesepian itu alasan meminta mereka menebus akibat pilihanmu. Di ponsel masih ada foto saat semua tampak bahagia. Kini kau tahu betapa banyak hal yang tidak terlihat pada gambar, termasuk kesempatan yang seharusnya mereka punya untuk memilih dengan kebenaran yang utuh."""

    # ┌─ ENDING · E-CF-12 · Korban yang Ia Ciptakan  [Khusus · host C]
    # │ KAPAN   : jalur manipulasi pembalikan (§14); framing bertahan; nurani_chiasa < 70 sebelum M35
    # │ ISI SKRG: Chiasa tampil sebagai korban, Koita dicap pelaku dan hancur; tanpa romansa; tak bisa diputar balik dan bisa muncul lagi
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-12"] = """Versi yang kaubiarkan dipercaya bertahan sampai evaluasi. Chiasa diperlakukan sebagai orang yang perlu dilindungi, sementara Koita, korban yang sebenarnya, menanggung tuduhan dan keterasingan yang membuatnya kehilangan hampir semua cara meminta didengar.

Kau tidak mendapatkan hubungan romantis dari hasil itu. Ada simpati yang diberikan kepada cerita palsu, ada pintu yang dibuka karena orang mengira sedang menolong, dan semakin banyak percakapan yang harus dijalani tanpa mengakui siapa yang telah kaulukai.

Ketika Koita akhirnya berhenti mencoba menjelaskan kepadamu, keheningan itu sempat terasa nyaman. Lalu kau menyadari setiap orang yang mengetahui sebagian kebenaran masih hidup di luar kendalimu. Evaluasi berakhir tanpa membatalkan masa lalu. Fitnah yang bertahan hari ini tetap sesuatu yang dapat terbuka besok, dan kehancuran yang telah dibuat tidak akan menjadi benar hanya karena cukup lama dipercaya."""

    # ┌─ ENDING · E-CF-13 · Pengakuan yang Tidak Diminta  [Khusus · host C]
    # │ KAPAN   : nurani_chiasa ≥ 70 sebelum M35; framing pernah terpasang lalu dicabut sendiri
    # │ ISI SKRG: ia mengaku sebelum siapa pun membuktikannya; reputasi Koita pulih meski kepercayaan di antara mereka tidak pernah utuh lagi; konsekuensi sosial padanya tetap ada tapi lebih ringan karena kooperatif
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-CF-13"] = """Kau mengaku sebelum orang lain berhasil membuktikan kebohongan tersebut. Pengakuan itu tidak disusun sebagai permintaan agar Koita segera memahami alasanmu. Kau menyebut perbuatan, meluruskan tuduhan, dan menerima bahwa keterangan berikutnya tidak lagi boleh sepenuhnya kaudiktekan.

Nama Koita mulai dibersihkan. Sebagian orang meminta maaf, sebagian menghindar karena malu, dan tidak semua kerusakan dapat dipulihkan oleh berita koreksi. Kepercayaan antara kalian tidak kembali menjadi kehidupan serumah yang lama.

Kerja sama dalam mengungkap kebenaran membuat akibat terhadapmu lebih ringan daripada bila terus menutupinya, tetapi tidak menghapus tanggung jawab sosial dan proses yang tetap harus dijalani. Pada hari Koita memilih tidak bertemu, kau membiarkan jawabannya berlaku. Itu bukan penebusan yang selesai, hanya satu keputusan untuk berhenti menjadikan kebutuhanmu pusat dari luka yang menimpanya."""


    # ═════ Yutaka ═════
    # ┌─ ENDING · E-YU-01 · Bersama Chiasa  [Romantis · host C]
    # │ KAPAN   : Yutaka mengaku; Chiasa menerima
    # │ ISI SKRG: aman hanya bila ada deviasi lain (bila tidak, E-SI-06)
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YU-01"] = """Yutaka datang tanpa alasan yang dipinjam dari Koita. Ia membawa kopi untukmu, lalu mengaku sudah memikirkan kalimat pembuka sepanjang perjalanan. Kau mengatakan ia tidak perlu membuat pengakuan kedua. Jawabanmu yang pertama masih berlaku.

Hubungan kalian tumbuh dalam hal kecil: menunggu kelas selesai, bertengkar tentang waktu, mengaku cemburu sebelum candaan menjadi kejam. Ia belajar bahwa mencintai Chiasa tidak memberinya hak menebak seluruh isi kepalamu. Kau belajar menerima perhatian tanpa menjadikannya bukti bahwa kehidupan pinjaman ini sudah sepenuhnya milikmu.

Di depan rumah Amamiya, ia menggenggam tanganmu setelah bertanya apakah boleh. Masa depan itu sungguh kalian inginkan. Di tempat yang tidak dapat didengarnya, kontrak masih menunggu perhitungan lain. Kebahagiaan kalian tidak otomatis membatalkan ancaman yang sejak awal tidak peduli pada cinta."""

    # ┌─ ENDING · E-YU-02 · Mundur ke Luar Negeri  [Netral · host C]
    # │ KAPAN   : Yutaka mundur demi Koita
    # │ ISI SKRG: magang ke luar negeri untuk melupakan
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YU-02"] = """Yutaka memberitahumu soal magang di luar negeri sesudah berkasnya selesai. Ia tidak menyebut Koita sebagai alasan, tetapi jeda sebelum nama itu cukup panjang. Ia ingin pergi sebelum rasa kecewanya mengubah semua orang yang disayanginya menjadi lawan.

Di bandara, kau menawarkan tetap berkabar. Ia mengangguk dan mengatakan bahwa kadang ia mungkin tidak akan langsung menjawab. Itu bukan hukuman. Ia membutuhkan hidup yang tidak setiap harinya menunggu perubahan perasaanmu.

Foto pertama datang beberapa minggu kemudian: jalan yang tidak kaukenal, makan malam sederhana, satu keluhan tentang pekerjaan. Kau membacanya dengan lega yang juga sedih. Jarak belum menyembuhkan semuanya. Untuk pertama kalinya, ia sedang membuat sesuatu yang tidak harus berakhir dengan kembali kepadamu."""

    # ┌─ ENDING · E-YU-03 · Retak dan Menutup Diri  [Buruk · host C]
    # │ KAPAN   : Chiasa menolak lalu menggantung
    # │ ISI SKRG: apartemen menjadi satu-satunya tempatnya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YU-03"] = """Yutaka berhenti menanyakan kapan kalian bisa bertemu. Pada awalnya kau menganggap ia sibuk. Setelah beberapa undangan tidak dijawab, barulah jelas bahwa candaan yang selalu menyelamatkan suasana telah habis.

Apartemennya tetap terang pada malam hari. Permainan menyala, makanan datang, dan pesan kepada Koita dibiarkan sama lamanya dengan pesanmu. Ia malu karena merasa dipermainkan, lalu marah pada dirinya sendiri karena masih berharap satu pemberitahuan bisa mengubah semuanya.

Kau tidak mendapat adegan penutupan yang rapi. Ada orang yang pelan-pelan meninggalkan percakapan karena terlalu lama diminta menunggu jawaban yang tidak sungguh ingin diberikan. Di layar, namanya masih ada. Kebiasaan memanggilnya ketika membutuhkan kenyamanan kini hanya memperjelas mengapa ia berhenti datang."""

    # ┌─ ENDING · E-YU-04 · Sekutu Chiasa  [Khusus · host C]
    # │ KAPAN   : Chiasa jujur padanya
    # │ ISI SKRG: Yutaka membantu Chiasa di rute heroine atau Koita Success
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YU-04"] = """Kau menceritakan cukup banyak kebenaran hingga Yutaka berhenti mengira semua persoalanmu dapat diselesaikan dengan mengajak keluar. Ia bertanya apa yang kaubutuhkan, kemudian membedakannya dari apa yang sanggup ia lakukan.

Ia membantumu menghadapi percakapan sulit, tetap mengingatkan ketika kau mulai membenarkan perlakuan buruk kepada orang lain. Menjadi sekutu tidak berarti setuju pada setiap rencana. Kadang dukungan terpentingnya adalah menolak membiarkanmu memakai rasa takut sebagai alasan untuk melukai Koita.

Pada hari yang panjang itu, ia menunggumu dengan dua minuman. Tidak ada tagihan perasaan di balik bantuannya. Kalian belum tahu akan menjadi apa setelah semua selesai, tetapi persahabatan ini akhirnya berdiri di atas pengetahuan yang lebih benar daripada dugaan dan harapan diam-diam."""

    # ┌─ ENDING · E-YU-05 · Tahu Dipakai  [Buruk · host C]
    # │ KAPAN   : Chiasa memperalat Yutaka dan ia mengetahuinya
    # │ ISI SKRG: patah; memutus Chiasa dan Koita sekaligus
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YU-05"] = """Yutaka membaca kembali percakapan kalian dan akhirnya melihat pola yang selama ini ditolak pikirannya sendiri. Kau datang ketika butuh sesuatu, mendekat ketika ia mulai mundur, lalu menyebutnya salah paham saat ia berharap lebih.

Ia meminta satu pertemuan untuk mengakhiri semuanya. Ketika kau mencoba mengingatkan kenangan masa kecil, ia mengatakan kenangan itu justru alasan perbuatanmu begitu menyakitkan. Koita juga kehilangan tempat di sisinya, terseret ke dalam hubungan yang sudah terlalu penuh rahasia untuk dipisahkan dengan bersih.

Sesudah itu ia tidak membalas. Di rumah Amamiya, kursi yang biasa ia pilih tidak langsung diisi orang lain. Kau berhasil memakai kepercayaannya saat masih ada. Kehilangan yang tersisa tidak menjadi lebih ringan hanya karena baru sekarang kau mengerti berapa lama kepercayaan itu dibangun."""

    # ┌─ ENDING · E-YU-06 · Membela Koita  [Netral · host C]
    # │ KAPAN   : Yutaka melihat Chiasa menyakiti Koita
    # │ ISI SKRG: berpihak pada Koita; menjadi lawan sosial Chiasa
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YU-06"] = """Yutaka berdiri di sebelah Koita ketika kau datang. Ia tidak meninggikan suara. Ia mengatakan tahu cukup banyak untuk berhenti membiarkan kedekatan denganmu menentukan apa yang akan ia abaikan.

Koita tampak malu membutuhkan pembelaan. Yutaka memberinya waktu, mendengarkan, dan mengingatkan teman-teman lain agar tidak memperlakukan luka itu sebagai gosip. Terhadapmu ia menjaga jarak yang jelas. Perasaan yang dulu dimilikinya tidak lagi dapat kaupanggil sebagai alasan agar ia berpihak.

Kalian masih mungkin bertemu di kampus. Sapaan tetap sopan, percakapan tidak pernah lama. Di antara kalian ada keputusan sederhana yang tidak dapat kauubah dengan godaan: ia memilih membantu orang yang sedang kausakiti, sekalipun orang yang menyakiti adalah kau."""

    # ┌─ ENDING · E-YU-07 · Pewaris Kisaragi  [Buruk · host C]
    # │ KAPAN   : keluarga menekan di M31; Chiasa tidak hadir
    # │ ISI SKRG: menjadi sedingin orang tuanya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YU-07"] = """Nama Yutaka mulai muncul dalam percakapan bisnis keluarga. Ia belajar hadir tepat waktu, menjawab seperlunya, dan tidak mengatakan bahwa ia ingin pulang ke tempat lain. Ketidakhadiranmu pada saat ia membutuhkan seseorang ikut menjadi bagian dari kebiasaan barunya berhenti meminta.

Koita beberapa kali mengajaknya makan. Yutaka selalu punya alasan yang masuk akal. Di foto acara perusahaan, ia tersenyum dengan ketepatan yang dulu dipakai untuk menggoda teman. Sekarang tidak ada yang tahu kapan senyum itu berakhir setelah kamera diturunkan.

Ia menjadi pewaris yang dapat diandalkan. Orang tuanya puas pada kemandiriannya, tanpa melihat betapa mirip jarak yang ia bangun dengan jarak mereka sendiri. Di apartemen, hadiah jam dari Daisuke tetap disimpan. Ia jarang memakainya ke kantor."""

    # ┌─ ENDING · E-YU-08 · Sahabat Lagi  [Netral · host C]
    # │ KAPAN   : Chiasa menolak dengan jujur dan konsisten
    # │ ISI SKRG: geng masa kecil tetap utuh
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YU-08"] = """Penolakanmu tidak langsung membuat Yutaka lega. Ia membutuhkan waktu untuk berhenti membaca kehangatan sebagai janji yang mungkin berubah. Kau memberinya waktu itu, tidak memanggilnya kembali hanya karena rindu diperhatikan.

Ketika ia akhirnya datang lagi ke rumah Amamiya, percakapan sempat canggung. Nagisa membuat gurauan buruk, Koita salah mengambil gelas, dan Chiasa tertawa sebelum tahu harus berkata apa. Tidak ada yang memaksa keakraban kembali dalam satu malam.

Bulan-bulan berikutnya, kalian dapat berkumpul tanpa seluruh suasana bergantung pada perasaan yang tidak berbalas. Yutaka masih berarti bagimu, dan ia mulai percaya arti itu tidak harus romantis untuk nyata. Geng masa kecil bertahan karena seseorang akhirnya berani memberikan jawaban yang konsisten."""

    # ┌─ ENDING · E-YH-01 · Pewaris yang Berbeda  [Netral · host Y]
    # │ KAPAN   : Y17-A; keluarga berdamai
    # │ ISI SKRG: mengambil perusahaan keluarga dengan cara sendiri, tidak sedingin orang tuanya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YH-01"] = """Kau menerima pekerjaan di perusahaan keluarga sesudah menjelaskan apa yang ingin dipelajari dan batas yang tidak mau kaulampaui. Kenji tidak menyetujui semuanya. Untuk pertama kalinya, perbedaan itu tidak harus mengakhiri percakapan.

Hari-hari pertama tidak menyerupai kedudukan seorang pangeran. Ada laporan yang salah, karyawan yang lebih mengerti pekerjaan, dan rasa malu ketika nama keluarga mendahului kemampuanmu. Kau mulai datang untuk mendengar sebelum meminta dipercaya.

Di sela pekerjaan, kau menelepon rumah tanpa menunggu ada urusan uang. Kadang percakapan tetap kaku. Kadang ibu menceritakan hal kecil yang dulu dianggap tidak perlu. Menjadi pewaris tidak mengharuskanmu mengulang seluruh cara hidup mereka; perbedaan itu harus terus kaubuat, satu kebiasaan setiap hari."""

    # ┌─ ENDING · E-YH-02 · Bekerja di Luar  [Netral · host Y]
    # │ KAPAN   : Y17-B
    # │ ISI SKRG: lepas dari keluarga Kisaragi; hidup dengan gaji sendiri
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YH-02"] = """Gaji pertamamu masuk dengan angka yang terasa kecil dibanding uang yang dulu datang tanpa ditanya. Kau memeriksanya lama, lalu menertawakan rasa bangga yang sulit dijelaskan. Tidak ada bagian dari pekerjaan bulan ini yang dikerjakan oleh reputasi Yutaka semata.

Kau belajar menyesuaikan pengeluaran dan menerima pekerjaan yang tidak selalu menyenangkan. Orang tua Kisaragi belum sepenuhnya memahami pilihan itu. Mereka kini harus bertanya bagaimana harimu jika ingin tahu, sebab hidupmu tidak lagi dapat dibaca dari rekening yang mereka isi.

Pada akhir pekan, kau membeli makan dengan uang sendiri dan mengajak seseorang yang ingin kautemui. Pilihan itu sederhana. Justru kesederhanaannya membuat masa depan terasa dapat dijalani, bukan hanya dipertahankan sampai evaluasi berikutnya."""

    # ┌─ ENDING · E-YH-03 · Keluarga Pilihan  [Romantis · host Y]
    # │ KAPAN   : hubungan dengan keluarga Amamiya tinggi; tanpa kejahatan
    # │ ISI SKRG: Daisuke dan Yoshie memperlakukannya sebagai anak sendiri
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YH-03"] = """Yoshie tidak mengumumkan bahwa kau menjadi bagian keluarga. Ia hanya mulai menghitung porsi makan dengan menyertakanmu dan mengingatkan agar mengabarinya kalau pulang terlambat. Daisuke menanyakan pekerjaanmu seperti ia menanyakan pekerjaan Koita: cukup serius untuk percaya kau dapat menjawab.

Kau tetap harus mengetuk atau mengabari sebelum datang. Kedekatan tidak berubah menjadi hak memasuki setiap ruang. Di rumah itu, batas yang sederhana justru membuat penerimaan terasa aman; kau tidak perlu membuktikan keakraban dengan melanggarnya.

Suatu malam mereka menyuruhmu membawa pulang makanan. Kau berdiri di depan pintu dengan kotak hangat dan menyadari tidak ada pertunjukan yang perlu kauberikan sebagai imbalan. Kau diterima karena telah hidup bersama mereka dengan jujur, bukan karena berhasil menjadi salinan sempurna anak yang dahulu mereka kenal."""

    # ┌─ ENDING · E-YH-04 · Dicoret  [Buruk · host Y]
    # │ KAPAN   : membangkang keluarga berulang atau skandal besar
    # │ ISI SKRG: uang saku berhenti; apartemen dilepas; mulai dari nol
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YH-04"] = """Pemberitahuan terakhir dari keluarga berisi keputusan yang tidak lagi terdengar seperti ancaman. Uang saku dihentikan, apartemen harus dilepas, dan biaya yang selama ini tak pernah kaupikirkan kini muncul satu per satu.

Kau berkemas di ruangan yang pernah terasa terlalu luas. Ada barang yang dijual, ada yang ternyata tidak berarti tanpa tempat untuk menyimpannya. Perselisihan atau skandal yang membawa kalian ke sini tidak menghilang bersama alamat lama. Jika ada orang yang kaulukai, kesulitanmu bukan pengganti pertanggungjawaban kepada mereka.

Malam pertama di tempat baru terdengar berbeda. Kau menghitung uang, mencari kerja, dan memutuskan siapa yang masih bisa kauberi kabar dengan jujur. Hidup belum selesai. Tetapi untuk meneruskannya, kau tidak lagi memiliki kemewahan menganggap kebutuhan dasar sebagai sesuatu yang selalu akan disediakan orang lain."""

    # ┌─ ENDING · E-YH-05 · Ketahuan Bukan Yutaka  [Khusus · host Y]
    # │ KAPAN   : minimal dua orang dekat yakin ia bukan Yutaka
    # │ ISI SKRG: diterima sebagai "Yutaka yang baru", atau dijauhi
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YH-05"] = """Mereka berhenti menyebut perubahanmu sekadar fase. Dua orang yang mengenal Yutaka dari dekat akhirnya mengatakan hal yang sama: ada seseorang yang hilang dari wajah yang sedang mereka pandang.

Kau tidak punya cara mengembalikan kesadaran yang dahulu tinggal di sini. Pengakuan itu tidak membuat kehilangan mereka lebih mudah diterima. Ada yang masih menghubungimu untuk mengenal orang yang kini hadir; ada yang memerlukan jarak setiap kali mendengar suaramu.

Tidak ada upacara yang menobatkanmu sebagai Yutaka baru. Kau menjalani hari dengan nama yang masih membuat sebagian orang berduka, berusaha tidak menuntut penerimaan sebagai pembayaran atas kejujuran. Setiap hubungan yang tersisa harus tumbuh dengan pengetahuan bahwa menyayangimu dan merindukannya dapat terjadi pada waktu yang sama."""

    # ┌─ ENDING · E-YH-06 · Pergi Jauh  [Netral · host Y]
    # │ KAPAN   : Y17-C magang luar negeri
    # │ ISI SKRG: meninggalkan kota; quest Sistem tetap berjalan dari jauh
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YH-06"] = """Di kota lain, kau belajar berangkat kerja dengan rute yang belum hafal. Magang membuat harimu penuh nama baru dan kesalahan yang tidak ada hubungannya dengan Koita. Untuk beberapa jam, hidup terasa milik seorang pemuda biasa yang sedang mencoba bekerja dengan baik.

Lalu pesan dari Kouseikan datang. Perbedaan waktu mengubah percakapan menjadi balasan yang saling menunggu. Kontrak tetap bergerak bersama kalender di sana, dan jarak tidak membuatmu berhenti memikirkan akibat keputusan yang sudah kaubuat.

Dari jendela tempat tinggal sementara, kau melihat jalan yang tidak pernah muncul di manga. Dunia ini lebih luas daripada panggung yang diberikan kepadamu. Ancaman evaluasi tetap ada, tetapi untuk pertama kalinya kau punya bukti bahwa ada kehidupan di luar lingkaran yang selama ini kausahakan menguasai."""

    # ┌─ ENDING · E-YH-07 · Informan yang Menagih  [Buruk · host Y]
    # │ KAPAN   : daichi_status penagih
    # │ ISI SKRG: Daichi memeras pemain dengan semua yang ia tahu
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-YH-07"] = """Daichi tidak lagi mengajak makan dengan nada bercanda. Ia menyebut hal yang diketahuinya, lalu kebutuhan yang katanya mendesak. Kau mengerti hubungan itu telah berubah sebelum jumlah uang diucapkan.

Setiap permintaan membuatmu mengira pembayaran berikut akan menjadi yang terakhir. Setelahnya, kau tetap memeriksa ponsel dengan cemas. Rahasia yang dipakai untuk merugikan orang lain kini juga mengatur kapan kau dapat tidur tenang.

Daichi bertanggung jawab atas pemerasannya, dan perbuatanmu sendiri tetap milikmu. Tidak ada yang menjadi benar karena kini kau juga diperlakukan buruk. Di antara kalian tidak tersisa kesetiaan seorang informan, hanya transaksi yang membuat masa lalu terus memasuki hari-hari yang ingin kaujalani sebagai orang lain."""


    # ═════ Lintas / NPC / Harem ═════
    # ┌─ ENDING · E-X-01 · Harem yang Runtuh  [Buruk · host Y/C]
    # │ KAPAN   : beberapa hubungan rahasia terbongkar sekaligus di M23 atau M35
    # │ ISI SKRG: semua pergi di hari yang sama
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-01"] = """Mereka datang dengan pertanyaan berbeda dan pulang dengan alasan yang sama. Janji yang kauucapkan kepada satu orang ternyata pernah diberikan kepada yang lain, dengan kata yang hampir tidak berubah. Percakapan hari itu tidak memberimu cukup waktu untuk menyelamatkan semua versi dirimu.

Ada yang marah keras, ada yang terlalu tenang. Salah seorang meminta barangnya dikembalikan melalui teman. Yang lain hanya menghapus rencana minggu depan. Tak satu pun bersedia menenangkanmu karena kau kini takut kehilangan mereka.

Menjelang malam, ruangan menjadi kosong. Kau masih memiliki pesan-pesan lama yang dulu dibaca sebagai bukti kasih sayang. Kini setiap kalimat memperlihatkan betapa banyak orang telah mencoba mempercayaimu secara bersamaan, dan betapa sengaja kau membiarkan mereka tidak saling tahu."""

    # ┌─ ENDING · E-X-02 · Meja Panjang  [Romantis · host Y/C]
    # │ KAPAN   : hubungan terbuka yang disepakati semua pihak
    # │ ISI SKRG: makan malam panjang yang canggung, tapi jujur
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-02"] = """Meja itu memang terlalu panjang untuk dapur yang tersedia. Kursi tambahan berbeda warna, makanan tidak selesai pada waktu yang sama, dan percakapan pertama lebih canggung daripada yang kalian bayangkan. Tak seorang pun bisa memakai istilah hubungan terbuka untuk menggantikan pembicaraan yang belum selesai.

Kalian membahas waktu, kecemburuan, privasi, dan hak untuk berubah pikiran. Ada kesepakatan yang harus diperbaiki setelah ternyata menyakiti seseorang. Tidak ada orang yang diminta bertahan agar kalian terlihat berhasil di depan orang lain.

Malam itu, seseorang meminta lauk diteruskan dan candaan akhirnya terdengar wajar. Kalian belum menemukan bentuk hidup tanpa kesulitan. Kalian telah memilih bentuk yang tidak bergantung pada kebohongan, dan menerima bahwa persetujuan setiap orang harus tetap bisa didengar besok."""

    # ┌─ ENDING · E-X-03 · Domino Shiori  [Buruk · host Y/C]
    # │ KAPAN   : Shiori tahap 5 dengan daftar_kebohongan panjang
    # │ ISI SKRG: semua rahasia terbuka dan setiap rute ikut runtuh
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-03"] = """Shiori tidak memulai dengan pidato. Ia mempertemukan orang-orang yang selama ini mendengar versi berbeda dan membiarkan pertanyaan mereka menemukan jawaban yang tidak kausukai. Yang runtuh lebih dahulu adalah keyakinan bahwa setiap rahasia masih terpisah dari yang lain.

Hubungan-hubunganmu berubah dalam hitungan hari. Ada percakapan yang tidak lagi bisa dibatasi dengan meminta orang menjaga privasi, sebab permintaan itu sudah terlalu sering dipakai untuk melindungimu. Mereka perlu bicara agar memahami apa yang terjadi kepada diri masing-masing.

Shiori tidak terlihat puas ketika semuanya selesai. Balas dendam menghabiskan sesuatu dalam dirinya juga. Kau ditinggalkan bersama cerita yang kini tidak bisa kausunting seorang diri. Orang-orang yang semula kaudekati sebagai pilihan mulai menyusun hidup yang tidak memberimu posisi di tengahnya."""

    # ┌─ ENDING · E-X-04 · Musim Dingin Tanpa Moeka  [Buruk · host Y/C]
    # │ KAPAN   : E-MO-04
    # │ ISI SKRG: semua epilog berubah menjadi versi duka
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-04"] = """Musim dingin datang sesudah kematian Moeka dan membuat tempat-tempat biasa terasa salah. Konbini tetap buka. Kelas tetap dimulai. Rina berhenti pada rak barang yang pernah mereka komentari bersama, lalu berjalan lagi tanpa membeli apa pun.

Di antara teman-teman, ada yang ingin terus membicarakannya dan ada yang tidak sanggup mendengar nama itu setiap hari. Perbedaan cara berduka sempat membuat mereka saling menyakiti. Tidak satu pun memiliki kalimat yang cukup baik untuk menutup pertanyaan tentang malam terakhirnya.

Rencana masa depan tetap dibuat, tetapi selalu ada bentuk kehilangan di tepinya. Saat seseorang tertawa dan mendadak terdiam, yang lain belajar tidak menuntut penjelasan. Moeka tidak menjadi pelajaran yang rapi bagi hidup orang lain. Ia tetap seseorang yang seharusnya punya hari-hari berikutnya."""

    # ┌─ ENDING · E-X-05 · Kursi Kosong di Wisuda  [Khusus · host Y/C]
    # │ KAPAN   : semua heroine lepas dari Koita
    # │ ISI SKRG: Koita sendirian di wisuda; deviasi sangat tinggi
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-05"] = """Di wisuda, Koita berdiri sendirian setelah namanya dipanggil. Para perempuan yang dulu selalu digambarkan berada di sekelilingnya kini mempunyai tujuan sendiri. Tidak ada pertemuan terakhir yang membawa mereka kembali kepadanya hanya karena hari ini terasa pantas untuk sebuah akhir.

Ia membantu seorang teman mengambil foto, lalu memeriksa pesan di ponselnya. Ada ucapan selamat, ada urusan pekerjaan. Kursi yang kosong di dekatnya tidak otomatis berarti hidupnya sudah habis, meskipun kau tahu betapa jauh semua ini menyimpang dari kisah yang pernah kaubaca.

Kau memandangnya dari kerumunan. Sistem akan menghitung jarak antara naskah dan kenyataan. Koita masih harus memutuskan apa yang hendak dibuat dari kenyataan itu. Untuk pertama kalinya, ia tidak diberi romansa sebagai jawaban siap pakai atas pertanyaan tentang siapa dirinya."""

    # ┌─ ENDING · E-X-06 · Semua Orang Bebas  [Romantis · host Y/C]
    # │ KAPAN   : semua heroine pulih dan mandiri; tidak ada yang bersama Koita atau pemain
    # │ ISI SKRG: lingkaran yang bubar dengan sehat (sering bersama E-SI-12)
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-06"] = """Mereka tidak berkumpul untuk memilih seseorang. Pertemuan terakhir sebelum jadwal semua orang berpisah dipenuhi cerita kerja, pendidikan, tempat tinggal, dan hal yang ingin dicoba tanpa perlu meminta restu seorang pasangan.

Beberapa hubungan pernah terasa hampir romantis. Ada yang berakhir dengan sedih, ada yang berubah menjadi persahabatan yang lebih tenang. Koita mendengar mereka tanpa mengira semua rencana itu diam-diam masih menunggunya. Kau juga tidak meminta hasil dari bantuan yang pernah kauberikan.

Setelah makan, kalian berjalan ke arah yang berbeda. Tidak ada orang yang pulang sebagai hadiah untuk orang lain. Kelegaan itu sederhana dan luas: mereka tetap hidup, pulih dengan cara masing-masing, dan bebas menginginkan masa depan yang tidak menempatkan siapa pun di pusat seluruh pilihan."""

    # ┌─ ENDING · E-X-07 · Melawan Naskah Bersama  [Khusus · host Y/C]
    # │ KAPAN   : E-KO-13 dan persahabatan atau Rute BL
    # │ ISI SKRG: Koita dan pemain sama-sama sadar naskah dan melawannya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-07"] = """Koita meletakkan catatannya di antara kalian. Ia tidak lagi bertanya apakah semua kebetulan dalam hidupnya wajar. Ia bertanya bagian mana yang masih dapat dipilih ketika kisah seolah terus mendorongnya menuju jawaban yang sama.

Kau menceritakan yang kautahu tanpa mengaku menguasai seluruh aturan. Ada hal yang membuatnya marah kepadamu, dan kalian tidak menyelesaikannya dengan memanggil diri sendiri korban keadaan. Melawan naskah bersama menuntutmu mengakui kapan kau sendiri pernah memanfaatkan naskah itu.

Keesokan hari, kalian membuat rencana kecil yang tidak bergantung pada seseorang jatuh cinta atau patah. Koita membawa dua minuman dan menanyakan apakah kau siap. Untuk pertama kalinya, keberanian itu bukan adegan penyelamatan seorang protagonis. Ia seorang manusia yang bersedia menghadapi ketidakpastian bersamamu."""

    # ┌─ ENDING · E-X-08 · Pengakuan di Depan Semua  [Khusus · host Y/C]
    # │ KAPAN   : pemain membuka Sistem kepada seluruh lingkaran di M35
    # │ ISI SKRG: setiap orang bereaksi sesuai sejarahnya dengan pemain
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-08"] = """Kau mengumpulkan mereka dan mengatakan ada Sistem yang menempatkan keselamatanmu di atas penyimpangan hidup Koita. Kalimat itu terdengar mengerikan ketika akhirnya diucapkan dengan suara yang dapat didengar orang lain.

Harumi meminta rincian yang dapat diperiksa. Shiori menanyakan apa yang selama ini kausengaja. Miyuki memikirkan siapa yang sedang terancam; Nagisa marah karena perasaannya pernah diperlakukan sebagai bagian perhitungan. Orang-orang lain membawa luka dan pertanyaannya sendiri. Tidak ada jawaban bersama yang membuat pengakuan itu mudah.

Sebagian percaya, sebagian belum. Mereka sepakat setidaknya pada satu hal: ancaman yang kautanggung tidak memberi hak atas kehidupan mereka. Malam itu kau kehilangan perlindungan dari rahasia. Jika masih ada hubungan yang bertahan, ia harus tumbuh setelah mereka tahu apa yang sebenarnya sedang dipertaruhkan."""

    # ┌─ ENDING · E-X-09 · Dua Tragedi  [Buruk · host Y/C]
    # │ KAPAN   : dua rute distorsi berakhir Bad dan saling memicu
    # │ ISI SKRG: dua kehilangan dalam satu musim
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-09"] = """Dua kehilangan datang dalam musim yang sama. Belum selesai orang memahami yang pertama, kabar berikutnya memaksa mereka berkumpul lagi dengan wajah yang tidak lagi tahu bagaimana menunjukkan terkejut.

Mereka mengingat percakapan yang terlewat, pertolongan yang tidak datang, dan luka yang saling membuat keadaan lebih buruk. Tidak semua dugaan dapat dibuktikan, tidak semua penyesalan berarti seseorang memiliki kuasa mencegah segalanya. Tetapi pilihan yang disengaja tetap harus disebut dengan namanya, terutama jika seseorang telah mengambil untung dari kerentanan orang lain.

Sesudahnya, lingkaran itu tidak kembali ke bentuk lama. Ada orang yang pindah, ada yang menjalani pendampingan, ada yang hanya berusaha melewati hari tanpa kehilangan lagi. Masa depan tetap ada, terasa lebih berat karena dua tempat di dalamnya tidak akan lagi diisi."""

    # ┌─ ENDING · E-X-10 · Kota yang Tahu Semuanya  [Buruk · host Y/C]
    # │ KAPAN   : Mei menerbitkan semuanya
    # │ ISI SKRG: reputasi semua orang yang terlibat hancur
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-10"] = """Tulisan Mei tersebar melampaui orang yang mula-mula ingin membaca gosip kampus. Nama, hubungan, dan pengakuan pribadi menjadi bahan komentar orang yang tidak mengenal satu pun wajah di baliknya.

Kebenaran tentang perbuatanmu perlu diketahui mereka yang dirugikan. Namun bagian kehidupan orang lain yang ikut diumbar membuat luka baru. Ada korban yang harus menjelaskan dirinya berkali-kali, teman yang diseret hanya karena pernah terlihat bersama, dan keluarga yang mengetahui semuanya dari orang asing.

Kota tampak tahu segalanya, padahal yang dimilikinya hanyalah cerita yang terus dipotong dan diteruskan. Kau tidak bisa lagi menyelamatkan reputasimu. Mereka yang terseret juga harus berjuang mendapatkan kembali hak atas kisah hidup sendiri, jauh sesudah orang berhenti membicarakannya."""

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

Kau tidak lagi menghadapi dua hubungan yang dapat dipisahkan. Di antara akibat kebohonganmu, tumbuh kerja sama yang juga dapat melukai mereka sendiri. Tak ada kemenangan romantis dalam pengawasan dan ancaman itu. Yang tersisa adalah lingkaran permusuhan, semakin rapat setiap kali seseorang menyebut kendali sebagai perlindungan."""

    # ┌─ ENDING · E-X-13 · Tubuh yang Dibayar  [Khusus · host Y/C]
    # │ KAPAN   : pemain menyelamatkan minimal tiga heroine dari rute distorsi sambil terus memaksa tubuh
    # │ ISI SKRG: semua selamat, tubuh pemain yang membayar (dekat E-SI-07)
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-13"] = """Mereka selamat melewati masa terburuk, tetapi kau datang ke pertemuan berikutnya dengan tubuh yang tidak lagi sanggup mengikuti keinginanmu. Tanganmu cepat lelah, percakapan terputus karena kau perlu duduk, dan jadwal yang dulu kaujejalkan mulai kosong atas permintaan orang lain.

Untuk sekali ini, mereka datang menolongmu tanpa menanyakan apakah bantuan itu cukup berguna untuk dihitung. Kau harus belajar menerima makanan, istirahat, dan pendampingan tanpa mengubahnya menjadi utang yang akan segera kaubayar.

Harga yang telah ditanggung tubuhmu tidak membuat segala pilihan dahulu menjadi bijaksana. Mereka bersyukur kau hadir, sekaligus sedih karena kau mengira kehadiran harus dibuktikan dengan terus mengabaikan diri sendiri. Masa depan kalian kini juga memuat pekerjaan merawat orang yang sempat merasa hanya berhak menjadi penolong."""

    # ┌─ ENDING · E-X-14 · Dalang yang Tak Pernah Dicurigai  [Khusus · host Y/C]
    # │ KAPAN   : force_bersih[[x] bertahan untuk setiap korban Force; NTR sempurna tercapai (07_Koita_dan_BL.md §14, 09_Force_dan_Kriminal.md §10)
    # │ ISI SKRG: tidak ada yang pernah tahu apa yang sebenarnya terjadi; pemain lolos evaluasi dengan deviasi tertinggi yang mungkin, dan dunia tidak pernah mengejarnya. Sistem NTR tetap mencatat semuanya diam-diam
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-X-14"] = """Tidak ada tuduhan yang mencapai dirimu. Di hadapan kampus, kau tetap seseorang dengan sejarah yang tampak masuk akal. Orang-orang yang telah kaulukai membawa akibat kekerasan itu dalam kehidupan yang tidak disaksikan orang yang memujimu.

Ada yang semakin takut keluar, ada yang tidak sanggup menjelaskan perubahan dirinya, ada yang bertahan dengan bantuan kecil yang tidak pernah kauberikan. Ketidaktahuan dunia membuat mereka lebih sendirian. Itu tidak mengubah kekerasan menjadi hubungan, atau ketakutan mereka menjadi persetujuan.

Sistem menyatakan hasilmu sangat tinggi. Kau selamat dari evaluasi dan tidak dikejar hukum. Di balik angka yang disebutnya keberhasilan, ada kehidupan yang sengaja kaurusak dan kebenaran yang belum pernah didengar. Dunia tidak menghukummu dalam akhir ini. Naskah pun tidak akan menyebut kebebasan pelakunya sebagai akhir bahagia bagi orang yang disakitinya."""

    # ┌─ ENDING · E-NPC-01 · Dua Jas Putih  [Romantis · host Y/C]
    # │ KAPAN   : romansa tulus dengan Sena; Miyuki tidak disakiti
    # │ ISI SKRG: dua calon dokter yang saling menjaga jam tidur
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-01"] = """Di ruang istirahat, dua jas putih tergantung bersebelahan: milik Sena dan Miyuki. Kau datang membawa makanan setelah memastikan mereka memang bisa berhenti sebentar. Sena membuka bungkusnya dan langsung menanyakan apakah kau sendiri sudah makan.

Hubungan kalian tidak membuatnya meninggalkan persahabatan atau cita-citanya. Ia tetap blak-blakan, tidak memuji pengorbanan yang sebenarnya hanya menyembunyikan kebiasaan buruk mengabaikan diri. Kau belajar menerima bahwa perhatian kadang terdengar seperti teguran yang sangat tepat.

Miyuki pulang lebih dahulu malam itu. Sena duduk di sampingmu, menyandarkan kepalanya sejenak tanpa perlu menjelaskan lelahnya. Kau tidak menjadi dokter karena mencintainya. Kau menjadi seseorang yang mengenal jadwalnya dan tetap mengingat bahwa orang di balik jas itu juga perlu dijaga."""

    # ┌─ ENDING · E-NPC-02 · Sahabat yang Memilih Sisi  [Buruk · host Y/C]
    # │ KAPAN   : pemain menyakiti Miyuki sambil mendekati Sena
    # │ ISI SKRG: Sena memilih Miyuki dan menutup pintu
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-02"] = """Sena memintamu berhenti menemui Miyuki dengan janji yang terus membuatnya terluka. Ketika kau berusaha mengalihkan percakapan kepada kedekatan kalian sendiri, wajah Sena mengeras.

Ia tidak bersedia menjadikan perhatianmu kepadanya sebagai pengganti pertanggungjawaban kepada sahabatnya. Pesanmu dijawab hanya jika ada urusan yang memang perlu diselesaikan. Setiap usaha menyebut Miyuki terlalu sensitif membuat jarak itu semakin jelas.

Di kampus, kau melihat keduanya makan bersama. Sena mendengarkan sementara Miyuki mencoba mengatakan sesuatu tanpa tersenyum untuk melunakkan semuanya. Kau tidak mendapat tempat dalam percakapan itu. Ia telah memilih menjaga seseorang yang kauharapkan akan ditinggalkannya demi dirimu."""

    # ┌─ ENDING · E-NPC-03 · Thrift Hari Minggu  [Romantis · host Y/C]
    # │ KAPAN   : romansa tulus dengan Rina; Moeka selamat
    # │ ISI SKRG: Minggu pagi di toko bekas, bertiga dengan Moeka
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-03"] = """Rina mengajakmu ke toko barang bekas pada Minggu pagi. Moeka datang terlambat dengan alasan yang ditertawakan mereka berdua sebelum kau sempat bertanya. Ia masih punya masalah, tetapi hari ini ia boleh hanya menjadi teman yang sedang mencari jaket.

Rina menggandeng tanganmu di antara rak, lalu melepaskan sebentar untuk memeriksa jahitan baju. Kehidupan bersama ternyata penuh perhatian yang tidak dramatis: mengingat ukuran, membagi ongkos, bertanya apakah seseorang sungguh ingin ikut atau hanya takut mengecewakan.

Kalian makan setelah berbelanja. Moeka memotret Rina yang sedang memprotes hasil temuannya sendiri. Saat melihat foto itu, kau tahu kebahagiaan ini juga ditopang oleh orang-orang yang tetap diberi tempat, bukan oleh keberhasilan membuat pasanganmu melupakan semua orang selain dirimu."""

    # ┌─ ENDING · E-NPC-04 · Rina Tidak Memaafkan  [Buruk · host Y/C]
    # │ KAPAN   : Moeka meninggal atau disakiti pemain
    # │ ISI SKRG: Rina menjadi saksi paling keras terhadap pemain
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-04"] = """Rina tidak menerima penjelasan yang mengubah penderitaan Moeka menjadi cerita tentang betapa sulitnya posisimu. Ia menyebut apa yang diketahuinya dengan jelas dan menolak diminta diam demi nama baik.

Jika ada orang bertanya, ia menjawab sebatas yang dapat dipertanggungjawabkan. Ia tidak menyerahkan kehidupan pribadi Moeka kepada rasa ingin tahu mereka. Kemarahannya tidak membuatnya lupa kepada siapa kesetiaan itu seharusnya diberikan.

Kau pernah mengira keramahan Rina berarti ia akan selalu mencari alasan untuk memaafkan. Kini ia melewatimu tanpa berhenti. Apa yang kaulakukan kepada sahabatnya telah mengakhiri kemungkinan itu, dan ia tidak merasa berkewajiban memberimu percakapan terakhir agar kau lebih mudah melanjutkan hidup."""

    # ┌─ ENDING · E-NPC-05 · Studio Berdua  [Romantis · host Y/C]
    # │ KAPAN   : romansa dengan Haruka
    # │ ISI SKRG: dua meja gambar dalam satu studio
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-05"] = """Dua meja berada di studio yang sama, menghadap cahaya yang berbeda. Haruka tidak memindahkan semua barangnya untuk menyatukan selera kalian. Kau menyukai kebebasan kecil itu: kedekatan tidak berarti setiap sudut harus kehilangan pemiliknya.

Ada hari ketika pekerjaan berjalan baik dan kalian makan terlambat karena terlalu sibuk mengobrol. Ada hari ketika kritik terdengar terlalu pribadi, lalu perlu dibicarakan lagi sesudah marah mereda. Tak seorang pun mengerjakan karya atas nama yang lain untuk menghindari percakapan sulit.

Menjelang malam, Haruka bertanya apakah kau mau melihat sesuatu yang belum selesai. Kau menutup pekerjaanmu dan mendekat setelah ia mengangguk. Di antara dua meja itu, cinta tumbuh sebagai izin saling melihat proses, termasuk bagian yang belum cukup indah untuk dipamerkan."""

    # ┌─ ENDING · E-NPC-06 · Rahasia yang Dititipkan  [Netral · host C]
    # │ KAPAN   : Haruka tahu rahasia Shena dan menjaganya
    # │ ISI SKRG: persahabatan yang lebih kuat dari rahasia
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-06"] = """Haruka tahu ada jarak antara Chiasa yang ia kenal dan orang yang sekarang memegang pensil. Ia tidak menuntut satu cerita yang langsung membuat semua perbedaan masuk akal. Ia meminta kau berhenti berjanji dapat melakukan pekerjaan yang belum sanggup kaulakukan.

Rahasia Shena tidak dijadikannya mata uang. Ia menjaganya sambil mendorongmu membuat keputusan jujur mengenai proyek baru dan bantuan yang perlu diakui. Kadang kau kesal karena ia tidak membiarkanmu bersembunyi di balik rasa takut.

Pada suatu sesi latihan, ia memuji bagian kecil yang membaik. Kau tidak perlu memeriksa apakah pujian itu sebenarnya ditujukan kepada pemilik tangan dahulu. Haruka sedang melihat pekerjaanmu hari ini. Persahabatan itu memberimu tempat untuk memulai tanpa harus berpura-pura sudah sampai."""

    # ┌─ ENDING · E-NPC-07 · Pasal yang Membela  [Romantis · host Y/C]
    # │ KAPAN   : romansa atau aliansi dengan Ayane
    # │ ISI SKRG: Ayane membela pemain di kampus dan Moeka di sidang banding
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-07"] = """Ayane datang ke pertemuan dengan dokumen rapi dan pertanyaan yang tidak membiarkan orang bersembunyi di balik jabatan. Di kampus ia membantumu mendapat kesempatan menjawab secara adil. Dalam banding yang menyangkut Moeka, ia menolak membiarkan keadaan sulit dipakai sebagai alasan mengabaikan haknya.

Kedekatan kalian tidak membuat Ayane menjanjikan kemenangan. Ia memintamu berkata benar, datang tepat waktu, dan memahami bahwa membela seseorang tidak berarti menghapus pertanggungjawabannya.

Sesudah hari yang melelahkan, kalian duduk makan tanpa membicarakan perkara untuk beberapa saat. Kau belajar menyukai suaranya ketika tidak sedang berdebat. Ia pun mulai percaya bahwa di hadapanmu ia boleh lelah, tanpa harus selalu menjadi orang paling siap di ruangan."""

    # ┌─ ENDING · E-NPC-08 · Rapat Terakhir BEM  [Buruk · host Y/C]
    # │ KAPAN   : Ayane mengetahui manipulasi pemain
    # │ ISI SKRG: ia mengecam pemain di depan umum
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-08"] = """Pada rapat terakhir BEM, Ayane meminta waktu bicara. Ia menjelaskan manipulasi yang diketahuinya, membedakan fakta dari dugaan, dan menolak usahamu menjadikan hubungan pribadi sebagai alasan agar persoalan itu ditutup.

Ruangan tidak langsung berpihak serentak. Ada pertanyaan, keberatan, dan orang yang tampak menyesal telah terlalu mudah percaya. Ayane mendengarkan semuanya tanpa mencabut inti pernyataannya: jabatan dan kedekatan tidak boleh menjadi perlindungan bagi orang yang menyakiti.

Sesudah rapat, ia mengembalikan barang yang masih dititipkan kepadanya. Tidak ada percakapan untuk memperbaiki hubungan malam itu. Kau telah mengenal ketegasannya sebagai sesuatu yang menguntungkanmu. Kini kau harus menerima bahwa prinsip yang sama juga berlaku ketika orang yang perlu dihentikan adalah dirimu."""

    # ┌─ ENDING · E-NPC-09 · Redaksi Berdua  [Romantis · host Y/C]
    # │ KAPAN   : romansa dengan Mei; pemain jujur padanya
    # │ ISI SKRG: akun gosip berhenti menulis tentang pemain
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-09"] = """Mei berhenti menulis tentangmu untuk akun gosipnya. Ia mengatakan kedekatan kalian membuatnya tidak bisa berpura-pura menjadi pengamat yang tidak berkepentingan. Kau menertawakan cara ia mengucapkannya seperti catatan redaksi, lalu menyadari betapa seriusnya ia sedang berusaha berlaku benar.

Kalian masih berdebat tentang cerita, batas pribadi, dan orang yang tidak hadir untuk membela dirinya. Kejujuranmu tidak memberinya hak menerbitkan semua hal, dan perasaannya tidak memberimu hak menyuruhnya membentuk berita sesuai keinginanmu.

Malam di redaksi berakhir dengan makanan dingin dan tulisan yang belum selesai. Mei mematikan layar saat kau mengatakan sudah terlalu larut. Untuk sekali ini, cerita terbaik yang kalian punya tidak perlu dibaca siapa pun selain kalian berdua."""

    # ┌─ ENDING · E-NPC-10 · Headline Terakhir  [Buruk · host Y/C]
    # │ KAPAN   : Mei dipakai lalu dibuang
    # │ ISI SKRG: Mei menerbitkan semua yang ia tahu
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-10"] = """Mei menerbitkan tulisan terakhir tentangmu setelah menyadari seberapa jauh dirinya telah dipakai. Ia tidak mengirim draf untuk meminta persetujuan. Orang-orang lain membacanya lebih dahulu sebelum kau menemukan keberanian membuka tautan itu.

Tulisan tersebut memuat hal yang benar-benar kautakuti diketahui. Kemarahan Mei juga melampaui batas pada bagian yang menyeret kehidupan pribadi orang lain. Kebenaran tentang perbuatanmu tidak membenarkan setiap pilihan yang ia buat untuk menyebarkannya.

Kau kehilangan perlindungan dari reputasi, Mei kehilangan alasan menganggap dirinya tidak pernah ikut bermain. Hubungan itu berakhir dalam cerita yang terus dibaca orang asing, sementara mereka yang terseret harus hidup jauh lebih lama dengan akibatnya daripada lamanya tulisan itu menjadi pembicaraan."""

    # ┌─ ENDING · E-NPC-11 · Naskah dan Penyuntingnya  [Romantis · host C]
    # │ KAPAN   : romansa dengan Mio
    # │ ISI SKRG: hubungan kerja menjadi lebih dari itu
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-11"] = """Mio mengajakmu makan sesudah rapat kerja, lalu dengan kikuk menjelaskan bahwa undangan itu bukan bagian dari proyek. Untuk pertama kalinya, ia tidak membawa daftar revisi sebagai alasan bertemu.

Kalian membicarakan batas pekerjaan sebelum hubungan pribadi tumbuh lebih jauh. Penilaian karya dan keputusan kontrak perlu ditangani tanpa menjadikan cinta sebagai imbalan. Prosesnya tidak selalu nyaman, tetapi tidak ada yang ingin setiap penolakan revisi berubah menjadi keraguan terhadap kasih sayang.

Suatu malam, Mio membaca halaman yang tidak sedang dikejar tenggat. Kau duduk di dekatnya, menikmati kehadiran seseorang yang mengenal namamu di balik Shena. Ketika ia menutup buku dan mulai bercerita tentang harinya sendiri, kau tahu percakapan kalian akhirnya lebih luas daripada pekerjaan yang mempertemukan kalian."""

    # ┌─ ENDING · E-NPC-12 · Kontrak Diputus  [Buruk · host C]
    # │ KAPAN   : hubungan dengan Mio rusak
    # │ ISI SKRG: Mio memutus kontrak Shena
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-12"] = """Mio memutus hubungan kerja yang tidak lagi bisa dipertahankan dengan kepercayaan. Ia membicarakan penyelesaian kewajiban yang masih ada tanpa mengubahnya menjadi serangan pribadi. Kesopanan itu membuat akhir kontrak terdengar lebih pasti daripada pertengkaran.

Kau kehilangan tawaran baru dan tempat yang selama ini diberikan nama Shena di meja penerbit. Karya lama tetap mempunyai riwayatnya sendiri; masalah yang terjadi tidak dapat diperbaiki hanya dengan meminta orang mengingat betapa bagusnya sampul terdahulu.

Sesudah pertemuan, Mio tidak menelepon untuk membujukmu kembali bekerja. Kau pulang membawa catatan yang harus diselesaikan. Jika kelak ingin menggambar lagi, kau harus memulai dari keputusan yang dapat kaupertanggungjawabkan, bukan dari anggapan bahwa seseorang akan terus menunggu hanya karena pernah percaya."""

    # ┌─ ENDING · E-NPC-13 · Kakak yang Dipilih  [Romantis · host Y]
    # │ KAPAN   : romansa dengan Haruto
    # │ ISI SKRG: keluarga Sakurajima terkejut; Nagisa bereaksi sesuai tahapnya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-13"] = """Haruto mengatakan kepada keluarganya bahwa ia sedang menjalin hubungan denganmu. Keheningan pertama di meja makan membuat kalian berdua salah mengambil gelas. Nagisa menatap kakaknya, kemudian dirimu, seolah sedang menghitung berapa banyak percakapan yang telah luput didengarnya.

Ia membawa perasaan dan sejarahnya sendiri ke dalam kabar itu. Kau tidak memaksanya memberi restu dengan cepat. Haruto tetap kakaknya, dan mencintaimu tidak boleh menghapus tanggung jawabnya mendengar adiknya tanpa selalu membela diri.

Perlahan, kunjungan ke rumah Sakurajima menemukan kebiasaan baru. Haruto masih canggung ketika menunjukkan perhatian di depan keluarga. Kau menyukainya justru ketika ia berhenti berusaha terlihat paling tenang. Hubungan kalian tumbuh sebagai pilihan dua orang dewasa, dengan ruang bagi keluarga untuk mengenal bentuknya."""

    # ┌─ ENDING · E-NPC-14 · Restu Sakurajima  [Netral · host Y/C]
    # │ KAPAN   : Haruto menjadi sekutu
    # │ ISI SKRG: keluarga Nagisa membuka pintu untuk pemain
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-14"] = """Haruto membukakan pintu sebelum kau selesai merapikan salam yang sudah disiapkan. Ia mempersilakan masuk dan mengatakan orang tuanya sedang membuat minuman. Penerimaan itu terasa jauh lebih sederhana daripada semua usaha yang pernah kaulakukan untuk mendapatkannya.

Ia mempercayaimu karena telah melihat caramu memperlakukan Nagisa saat tidak ada keuntungan yang bisa diminta sebagai balasan. Kepercayaan itu tidak membuatnya berhenti bertanya. Justru karena kalian dapat bicara terus terang, ia tidak perlu selalu berdiri di antara kalian dengan kecurigaan.

Di ruang keluarga, Nagisa mengeluhkan sesuatu yang remeh dan orang tuanya menanggapi sambil tersenyum. Kau duduk sebagai tamu yang diterima. Restu mereka bukan hak atas hidup anaknya; ia kesempatan untuk terus membuktikan bahwa kedekatan ini aman bagi semua orang yang ada di dalamnya."""

    # ┌─ ENDING · E-NPC-15 · Esai untuk Satu Orang  [Romantis · host Y]
    # │ KAPAN   : romansa dengan Matsuda
    # │ ISI SKRG: Matsuda menulis esai baru, kali ini tentang tokoh yang memilih
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-15"] = """Matsuda menyerahkan esai baru dengan peringatan bahwa kau tidak wajib menyukainya. Kau membacanya di depan jendela klub sastra. Kali ini tokohnya tidak menunggu semua pintu tetap terbuka; ia memilih satu jalan sambil mengakui jalan lain akan hilang.

Ketika kautanya apakah itu tentang kalian, Matsuda mengatakan tidak semua tulisan bisa dipakai untuk bersembunyi dari jawaban pribadi. Ia menyukaimu. Kalimat itu diucapkan tanpa kutipan, tanpa tokoh pengganti, tanpa ejekan yang membuatnya mudah ditarik kembali.

Kau menyimpan esainya bersama catatan tentang hari biasa yang kalian lalui. Di luar halaman, pilihan masih perlu dibuat berkali-kali. Matsuda tetap tajam, kau tetap tidak selalu mengerti maksudnya, tetapi kini kalian dapat saling bertanya daripada menunggu seseorang menulis penjelasan yang sempurna."""

    # ┌─ ENDING · E-NPC-16 · Saksi yang Menulis  [Buruk · host Y/C]
    # │ KAPAN   : Matsuda membongkar manipulasi pemain
    # │ ISI SKRG: esai yang membongkar pemain dibaca seluruh fakultas
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-16"] = """Esai Matsuda beredar dari klub ke fakultas. Ia menulis tentang orang yang memperlakukan kehidupan teman-temannya sebagai bahan susunan, lalu menyebut kendali sebagai kepedulian. Cukup banyak pembaca mengenali siapa yang dimaksud.

Koita membacanya tanpa tertawa. Beberapa orang menghubungimu dengan pertanyaan yang tidak lagi dapat dijawab melalui gurauan. Matsuda tidak mengaku mengetahui semua isi kepalamu; ia menulis tentang pola tindakan yang sudah terlalu lama dilihat orang tanpa diberi nama.

Kau tidak dapat menuntut sebuah esai menggantikan proses yang adil, tetapi juga tidak dapat menghapus pengalaman yang membuat orang mengenalinya. Di fakultas, cara mereka menyambutmu berubah. Kalimat yang dulu kaubuat terdengar masuk akal kini selalu disusul pertanyaan tentang siapa yang akan membayar akibatnya."""

    # ┌─ ENDING · E-NPC-17 · Informan yang Setia  [Romantis · host Y]
    # │ KAPAN   : romansa dengan Daichi
    # │ ISI SKRG: informan yang berhenti menjual pemain
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-17"] = """Daichi datang membawa makanan dan informasi yang kali ini tidak dipasangi harga. Ketika kau bertanya, ia menjawab bahwa ia ingin tahu apakah kalian masih bisa mengobrol tanpa salah seorang menawarkan sesuatu.

Kalian perlu belajar berhenti memakai rahasia sebagai alat tawar. Tidak semua kebiasaan hilang karena pengakuan cinta. Daichi kadang masih menyembunyikan gugup di balik lelucon soal utang, dan kau mengingatkannya bahwa perhatianmu tidak sedang diperjualbelikan.

Pada malam ketika ia terlalu lelah untuk tampil menarik, ia tetap mengetuk pintu. Kau membiarkannya duduk tanpa meminta kabar kampus. Kesetiaan itu mulai terasa nyata ketika kalian dapat berada bersama tanpa informasi baru, hanya dua orang yang memilih tidak menjual satu sama lain kepada rasa takut."""

    # ┌─ ENDING · E-NPC-18 · Maket Kedua  [Romantis · host Y]
    # │ KAPAN   : romansa dengan Yuuto
    # │ ISI SKRG: Yuuto berhenti mengejar Nagisa
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-18"] = """Yuuto berhenti mencari alasan untuk terus berada dekat Nagisa. Ia mengakui bahwa perasaan tidak memberinya hak menunggu seseorang sampai lelah menolak. Pengakuan itu membuat percakapan kalian lebih jujur daripada pujian yang dahulu ia siapkan untuk orang lain.

Di studio arsitektur, kalian mengerjakan maket kedua. Ada bagian yang miring, jadwal yang terlalu padat, dan perselisihan tentang cara memperbaiki pekerjaan. Yuuto mulai bertanya pendapatmu tanpa menjadikanmu saksi betapa besar usahanya mendapatkan seseorang.

Sesudah maket selesai, ia mengajakmu keluar sebagai kencan dan menyebutnya begitu. Kau menerima dengan lega karena tidak harus menebak peranmu. Hubungan ini tidak dibangun sebagai tempat pelarian dari Nagisa, melainkan ruang baru yang kalian pilih setelah ia sungguh berhenti mengejarnya."""

    # ┌─ ENDING · E-NPC-19 · Pewaris yang Membangkang  [Romantis · host Y]
    # │ KAPAN   : romansa dengan Tojo
    # │ ISI SKRG: rencana pertunangan Tojo–Saionji runtuh
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-19"] = """Tojo menarik diri dari rencana pertunangan dengan Shiori. Keputusan itu menimbulkan lebih banyak percakapan keluarga daripada yang sanggup ia hindari dengan sikap percaya diri. Shiori mendengarnya sebagai kabar tentang hidupnya sendiri, bukan adegan yang harus ia selamatkan demi menjaga nama siapa pun.

Kau tidak menerima kedekatan Tojo sebagai bukti bahwa cara lamanya memperlakukan orang tiba-tiba tidak penting. Ia harus belajar mendengar penolakan dan melepaskan anggapan bahwa masa depan seseorang dapat ditentukan karena hubungan itu menguntungkan.

Saat ia datang menemuimu tanpa membawa rencana besar, suaranya terdengar kurang pasti. Kau menyukai kemungkinan perubahan itu, bukan jabatan pewaris yang dibawanya. Masa depan kalian bergantung pada apa yang ia lakukan sesudah berani membangkang, termasuk ketika orang yang perlu ia hormati sedang tidak memujinya."""

    # ┌─ ENDING · E-NPC-20 · Skandal Omiai  [Khusus · host Y]
    # │ KAPAN   : romansa dengan Takeru
    # │ ISI SKRG: omiai Miyuki runtuh dalam skandal
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-20"] = """Omiai yang seharusnya mempertemukan Takeru dan Miyuki berakhir dalam percakapan yang tidak disiapkan keluarga mana pun. Takeru mengakui hubungan yang ingin dijalaninya denganmu. Miyuki menatapnya lama, kemudian meminta mereka berhenti membicarakan masa depannya seolah ia hanya perlu menerima keputusan yang tersisa.

Kabar itu menjadi skandal karena orang-orang di sekeliling terlalu banyak menanam harapan tanpa bertanya. Kalian harus menghadapi kemarahan dan komentar yang tidak semuanya adil. Namun kegaduhan tersebut juga tidak menghapus kewajiban berkata jujur kepada orang yang telah dibawa masuk ke rencana ini.

Sesudahnya, hubungan kalian bergerak jauh dari meja perjodohan. Takeru masih bekerja, kau masih harus memilih apakah kedekatan ini sanggup hidup tanpa kesenangan melawan orang lain. Miyuki akhirnya mendapat ruang menyusun hidup yang tidak lagi menunggu keputusan seorang calon pasangan."""

    # ┌─ ENDING · E-NPC-21 · Kafe Pagi  [Netral · host Y/C]
    # │ KAPAN   : kerja tetap di Kafe Komorebi
    # │ ISI SKRG: Ito menjadi mentor; tubuh pemain paling sehat di semua ending
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-21"] = """Ito memberimu jadwal kerja tetap di Kafe Komorebi. Ia menjelaskan tanggung jawab, waktu istirahat, dan alasan mengapa datang terlalu lelah bukan sesuatu yang patut dibanggakan. Kau sempat menganggapnya cerewet sebelum menyadari betapa jarang orang lain memintamu berhenti tanpa menagih sesuatu.

Pagi-pagi di kafe punya urutan yang dapat dipelajari: membuka ruangan, menyiapkan meja, menyapa pelanggan. Kau makan pada waktunya dan tidur karena esok harus benar-benar hadir, bukan karena tubuh akhirnya tidak sanggup menolak.

Hidupmu tidak berubah menjadi mudah. Tetapi ketika mengangkat tirai pada pagi yang cerah, tubuhmu tidak lagi terasa seperti benda yang harus terus dipaksa. Ito menyerahkan cangkir dan menyuruhmu minum sebelum ramai. Kau menerima perhatian sederhana itu tanpa lebih dulu bertanya apakah kau telah pantas mendapatkannya."""

    # ┌─ ENDING · E-NPC-22 · Batas Profesional  [Netral · host Y/C]
    # │ KAPAN   : pemain mengejar Sato secara romantis
    # │ ISI SKRG: Sato menolak dan memindahkan konseling ke rekan lain
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-22"] = """Kau mengucapkan perasaanmu kepada Sato di akhir sesi. Ia mendengar sampai selesai, lalu menjawab dengan tenang bahwa hubungan romantis tidak dapat dijalani antara dirinya dan orang yang ia dampingi dalam konseling.

Penolakan itu tidak disertai ejekan atau hukuman. Ia membicarakan perpindahan pendampingan agar kau tetap bisa memperoleh bantuan tanpa harus terus menahan rasa tidak nyaman di ruangan yang sama. Kau boleh sedih; kesedihan itu tidak dipakai untuk mengubah batasnya.

Pada sesi pertama dengan rekan lain, kau hampir membatalkan kedatangan karena malu. Akhirnya kau masuk. Apa yang terjadi dengan Sato bukan kegagalan untuk layak dicintai. Ia telah menjaga hubungan profesional agar kebutuhanmu akan pertolongan tetap dapat diterima dengan aman."""

    # ┌─ ENDING · E-NPC-23 · Konseling Host  [Netral · host Y/C]
    # │ KAPAN   : konseling rutin dengan Sato
    # │ ISI SKRG: stres_host turun; rahasia Sistem dicatat sebagai "keyakinan pasien"
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-23"] = """Sato tidak meminta kau membuktikan Sistem pada pertemuan pertama. Ia mendengar keyakinan yang kauceritakan, menanyakan pengaruhnya pada tidur dan pilihanmu, lalu membahas hal yang bisa dibantu hari ini.

Konseling tidak menghapus kontrak dari duniamu. Ia membantumu membedakan rasa takut, kebutuhan tubuh, dan keputusan yang tetap berada dalam tanggung jawabmu. Perlahan kau berhenti menganggap setiap jeda sebagai waktu yang dicuri dari tugas menjaga hidup.

Dalam catatan profesional, cerita tentang Sistem dicatat sebagai keyakinan yang disampaikan. Di ruangan itu, kau juga seseorang yang belum makan, merindukan rumah, dan ingin bisa menutup mata tanpa menghitung ancaman. Bantuan yang kauterima tidak membutuhkan semua orang memahami asal ketakutanmu dengan cara yang sama."""

    # ┌─ ENDING · E-NPC-24 · Kepercayaan Kuroiwa  [Netral · host Y/C]
    # │ KAPAN   : Kuroiwa mempercayai pemain
    # │ ISI SKRG: peringatan dini setiap kali Shiori bergerak
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-24"] = """Kuroiwa menghubungimu sebelum sebuah pertemuan yang mungkin menjadi pertengkaran. Pesannya singkat: datang jika ingin bicara, dan jangan mengira Shiori akan selalu mau mendengar pada waktu yang kaupilih.

Kepercayaannya memberimu peringatan lebih dini, bukan izin memasuki kehidupan Shiori tanpa batas. Ia menegur saat kau mulai menganggap pengetahuannya sebagai jalan menghindari percakapan langsung. Kesetiaannya tetap kepada orang yang selama ini ia bantu tumbuh, termasuk ketika ia percaya kau tidak bermaksud buruk.

Pada kunjungan berikutnya, ia menyambutmu tanpa pemeriksaan panjang. Kau telah belajar menjawab dengan jelas dan pergi ketika memang waktunya pulang. Di antara kalian ada rasa hormat yang tidak perlu dibuat akrab untuk menjadi berarti."""

    # ┌─ ENDING · E-NPC-25 · Saksi yang Dipercaya  [Netral · host Y/C]
    # │ KAPAN   : pemain membantu Hanabusa
    # │ ISI SKRG: kesaksian pemain menjatuhkan Ogawa atau Kuga
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-25"] = """Hanabusa memintamu mengulang hal yang sungguh kaulihat. Ia tidak membantu mengisi bagian yang tidak kauketahui, sekalipun jawaban lengkap akan terdengar lebih meyakinkan. Menjadi saksi ternyata menuntut keberanian mengatakan tidak tahu juga.

Kesaksianmu membantu perkara terhadap orang yang selama ini merasa aman dari pertanyaan. Mereka yang dirugikan tetap harus menjalani proses yang berat, tetapi kini tidak seluruh pengalaman mereka berdiri sendirian di hadapan penyangkalan.

Sesudah semuanya, Hanabusa hanya mengucapkan terima kasih karena telah datang dan menjawab. Tidak ada gelar penyelamat yang diberikan kepadamu. Kau pulang memahami bahwa kepercayaan itu dibangun dengan membiarkan kebenaran tetap lebih penting daripada keinginanmu tampil berguna."""

    # ┌─ ENDING · E-NPC-26 · Penyusup  [Khusus · host Y/C]
    # │ KAPAN   : penyamaran berhasil; bukti cukup
    # │ ISI SKRG: Ogawa atau Kuga jatuh dari dalam
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-26"] = """Ketika perkara terbuka, orang yang dahulu menerima kehadiranmu di lingkarannya akhirnya memahami bahwa kesetiaanmu tidak pernah berada di tempat yang mereka kira. Ogawa atau Kuga kehilangan perlindungan yang diberikan orang-orang yang takut dan saling tidak tahu.

Apa yang diketahui selama penyamaran kini harus diperiksa melalui proses yang nyata. Kau tidak diminta memperindah peranmu. Ada tindakan yang perlu kauberi penjelasan sendiri, dan orang yang dirugikan tidak otomatis berutang rasa terima kasih karena rencanamu berhasil.

Sesudah memberi keterangan, kau merasa asing pada cara bicara yang sempat terlalu lama kaupalsukan. Di luar ruangan, seseorang memanggil namamu tanpa sandi atau maksud tersembunyi. Kau menoleh dengan kelegaan yang terlambat: akhirnya tidak perlu berpura-pura menjadi bagian dari sesuatu yang ingin kauhentikan."""

    # ┌─ ENDING · E-NPC-27 · Penyusup yang Tertelan  [Buruk · host Y/C]
    # │ KAPAN   : penyamaran terlalu lama
    # │ ISI SKRG: pemain ikut terseret kejahatan mereka
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-NPC-27"] = """Pada awalnya, kau mengatakan semua yang dilakukan hanya untuk mempertahankan penyamaran. Lalu ada keputusan yang mulai kaubela bahkan ketika tidak sedang berada di dekat orang yang ingin kaukelabui.

Ketika perkara terbongkar, namamu ikut disebut karena perbuatanmu sendiri. Niat awal tidak menghapus orang yang dirugikan selama kau menunggu saat yang dianggap tepat. Kau diminta menjelaskan apa yang diketahui, apa yang dilakukan, dan mengapa tidak berhenti ketika masih bisa.

Tidak ada pengungkapan terakhir yang memisahkanmu dengan bersih dari lingkaran itu. Kau telah terlalu lama mengambil manfaat dari tempatmu di dalamnya. Orang yang dulu kauanggap sasaran kini duduk dalam perkara yang juga menyangkutmu, sementara mereka yang berharap kau membantu harus menghadapi bentuk pengkhianatan yang baru."""

    # ┌─ ENDING · E-HP-01 · Bersama Satu Orang  [Romantis · host Y/C]
    # │ KAPAN   : satu hubungan romantis bertahan sampai M36
    # │ ISI SKRG: siapa pun orangnya: heroine, Koita, Chiasa atau Yutaka NPC, atau NPC sampingan
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HP-01"] = """Di antara banyak pertemuan, satu hubungan bertahan sampai kelulusan. Orang itu mengenal caramu menghindari pertanyaan, kebiasaan kecil saat lelah, dan bagian dirimu yang tidak pernah tampil baik di awal kisah cinta.

Kalian tidak berhenti berbeda pendapat. Ada janji yang perlu diperbaiki dan masa depan yang belum dapat ditentukan dalam satu percakapan. Namun tak seorang pun harus menebak apakah hubungan ini masih ada setiap kali hari menjadi sulit.

Setelah acara selesai, ia mencarimu di kerumunan dan menanyakan mau makan di mana. Pertanyaan itu terasa sederhana sesudah semua ancaman yang pernah kauhadapi. Kau menjawab dengan memikirkan seleranya juga. Hidup bersama dimulai lagi dari pilihan kecil yang tetap kalian buat untuk dua orang."""

    # ┌─ ENDING · E-HP-02 · Bersama Beberapa Orang  [Khusus · host Y/C]
    # │ KAPAN   : lebih dari satu hubungan bertahan, terbuka atau rahasia
    # │ ISI SKRG: lihat E-X-02 dan E-X-01
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HP-02"] = """Lebih dari satu orang masih menyebutmu pasangan. Dari luar, keadaan itu mungkin tampak seperti bukti betapa banyak cinta yang berhasil kaupertahankan. Dari dalam, semuanya bergantung pada apa yang benar-benar mereka ketahui dan setujui.

Pada bagian yang dibicarakan terbuka, ada jadwal, kecemburuan, dan hak menarik diri yang harus dihormati. Pada bagian yang disembunyikan, setiap ketenangan masih berdiri di atas sesuatu yang belum boleh dipilih orang yang terlibat. Jumlah hubungan tidak mengatakan mana yang sedang kalian jalani dengan jujur.

Kau menatap pesan yang masuk bergantian. Setelah kelulusan, tidak ada layar hasil yang dapat mengerjakan percakapan ini untukmu. Apa pun bentuk hubungan yang bertahan, orang-orang di dalamnya tetap berhak mengetahui kehidupan yang sedang mereka setujui."""

    # ┌─ ENDING · E-HP-03 · Tidak Dapat Siapa-Siapa  [Netral · host Y/C]
    # │ KAPAN   : pernah mengejar, tetapi tidak ada yang bertahan
    # │ ISI SKRG: pemain berakhir sendiri; cerita tidak menghukumnya karena itu
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HP-03"] = """Kau pernah mengira ada seseorang yang akan berada di sampingmu pada hari ini. Beberapa kedekatan berakhir sebelum sempat diberi nama, beberapa hubungan sungguh dimulai lalu tidak dapat diteruskan. Tidak semua akhir mempunyai seorang penjahat yang memudahkan rasa kehilangan.

Di wisuda, kau menyalami teman dan mengambil foto. Ada saat ketika melihat pasangan lain membuat dadamu nyeri, lalu ada percakapan biasa yang membuatmu tertawa tanpa merasa sedang menutupi apa pun.

Kau pulang sendiri dan menyiapkan makanan yang kausukai. Kehidupan yang tersisa bukan hadiah penghibur karena gagal mendapatkan seseorang. Ia masih milikmu untuk dijalani, dengan pekerjaan, persahabatan, dan kemungkinan yang tidak harus dibuktikan hari ini."""

    # ┌─ ENDING · E-HP-04 · Ditinggalkan Semua  [Buruk · host Y/C]
    # │ KAPAN   : semua orang yang dikejar pergi karena kebohongan atau luka
    # │ ISI SKRG: sendiri, dan semua orang tahu kenapa
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HP-04"] = """Orang-orang yang pernah kaudekati sudah pergi. Mereka tidak menyusun kepergian itu sebagai hukuman bersama. Masing-masing sampai pada batasnya sendiri setelah terlalu sering harus menebak kebenaran di balik perhatianmu.

Kau tidak dapat lagi memanggil kenangan hangat tanpa mengingat apa yang menyusul sesudahnya. Beberapa orang memblokir nomor, yang lain menjawab hanya untuk menyelesaikan urusan. Mereka berhak menolak percakapan yang kaubutuhkan demi merasa telah dimaafkan.

Di akhir hari, kau sendirian dengan pengetahuan bahwa kesepian ini mempunyai riwayat. Jika ingin berubah, pekerjaan itu harus dilakukan juga ketika tidak ada orang yang bersedia kembali untuk menyaksikannya. Tidak ada pasangan yang tersisa untuk kaubebani sebagai bukti bahwa kau kini layak dipercaya."""

    # ┌─ ENDING · E-HP-05 · Tidak Pernah Mengejar Siapa Pun  [Netral · host Y/C]
    # │ KAPAN   : tidak pernah memulai romansa
    # │ ISI SKRG: tiga tahun tanpa romansa; deviasi hanya datang dari cara lain
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HP-05"] = """Tiga tahun berlalu tanpa kau memulai romansa. Ada undangan yang diterima sebagai teman, perhatian yang tidak diteruskan menjadi janji, dan malam-malam yang dipakai untuk hal lain selain mencari pasangan.

Sebagian orang mengira kau menyembunyikan cinta besar. Kau belajar tidak harus memberi kisah yang mereka harapkan. Hidupmu tetap berisi kedekatan, pertentangan, kerja, dan keputusan yang mengubah orang di sekitarmu dengan cara yang tidak selalu romantis.

Pada hari kelulusan, kau tidak mencari seseorang untuk mengisi ruang di sampingmu agar foto terlihat lengkap. Perhitungan kontrak mempunyai urusannya sendiri. Ketiadaan romansa, pada dirinya sendiri, tidak membuat tiga tahun itu kosong atau menjadikan dirimu seseorang yang belum selesai."""

    # ┌─ ENDING · E-HP-06 · Cinta yang Datang Terlambat  [Khusus · host Y/C]
    # │ KAPAN   : seseorang mengaku di M35 atau M36 setelah pemain menyerah
    # │ ISI SKRG: jawaban pemain menjadi slide terakhir
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HP-06"] = """Pengakuan itu datang ketika kau sudah berhenti menunggu. Setelah acara hampir selesai, seseorang meminta waktu dan mengatakan ada hal yang terlambat dipahami tentang perasaannya kepadamu.

Kau mendengar tanpa memutuskan bahwa keterlambatan itu pasti romantis. Ada hidup yang telah kaususun setelah menyerah, luka yang mungkin belum selesai, dan kemungkinan yang masih dapat kainginkan. Semua itu pantas hadir dalam jawabanmu.

Ia mengatakan kau boleh berpikir. Untuk pertama kalinya, masa depan tidak menyerupai pintu yang harus dimasuki sebelum tertutup selamanya. Kau menarik napas dan mulai menjawab dengan apa yang sungguh kauinginkan hari ini. Halaman terakhir berhenti di sana, pada suaramu yang akhirnya tidak dipinjam dari harapan orang lain."""

    # ┌─ ENDING · E-HP-07 · Patah Hati yang Diterima  [Netral · host Y/C]
    # │ KAPAN   : ditolak dengan jujur, dan pemain menerimanya
    # │ ISI SKRG: sendiri, tetapi damai
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-HP-07"] = """Ia menolak dengan jujur. Kau mendengar kata-katanya tanpa mencoba menemukan celah yang akan membuat penolakan itu sementara. Sesudahnya, kau tetap sedih lebih lama daripada yang ingin kauakui.

Ada hari ketika kau perlu menjaga jarak. Kau menjelaskannya tanpa menjadikannya ancaman agar ia berubah pikiran. Perlahan, keinginan menghubungi setiap kali merasa sepi mulai berkurang, memberi tempat bagi hidup yang selama ini tertahan oleh satu harapan.

Saat bertemu lagi, kau bisa menyapa tanpa menuntut wajahnya menunjukkan penyesalan. Perasaanmu pernah nyata, demikian juga jawabannya. Kau pulang dengan hati yang belum melupakan semuanya, tetapi sudah tidak berperang melawan hak seseorang memilih lain."""


    # ═════ Sistem / Force ═════
    # ┌─ ENDING · E-SI-01 · Kontrak Selesai  [Romantis · host Y/C]
    # │ KAPAN   : deviasi cukup
    # │ ISI SKRG: Sistem berpamitan dengan satu ejekan terakhir; pemain hidup
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-01"] = """Jendela biru muncul ketika suara wisuda masih terdengar dari halaman. Sistem membacakan hasilnya dengan nada yang selama tiga tahun kaubenci dan kautunggu sekaligus. Kontrak dinyatakan selesai. Kau akan tetap hidup.

Ia menambahkan satu ejekan tentang betapa lama waktu yang kaubutuhkan. Kau hampir membalas, lalu berhenti. Tidak ada tugas baru menyusul, tidak ada ancaman kecil diselipkan setelah kalimat terakhir. Untuk pertama kalinya, diam di kepalamu bukan jeda sebelum perintah berikutnya.

Seseorang memanggilmu dari kerumunan. Kau menoleh dan berjalan ke arahnya tanpa memeriksa apakah pertemuan itu berguna bagi apa pun. Masa depan tidak tiba-tiba menjadi aman atau mudah. Ia akhirnya menjadi sesuatu yang dapat kaupikirkan tanpa lebih dahulu meminta izin kepada suara yang tidak pernah mencintai hidupmu."""

    # ┌─ ENDING · E-SI-02 · Nyaris  [Khusus · host Y/C]
    # │ KAPAN   : deviasi tipis di atas ambang
    # │ ISI SKRG: "Nyaris." Sistem tidak pernah bicara lagi
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-02"] = """Sistem hanya mengatakan satu kata sebelum menutup perhitungan: nyaris. Kau menunggu penjelasan, tetapi tidak ada. Ancaman berakhir dengan ketepatan dingin yang sama seperti ketika ia dimulai.

Tanganmu masih gemetar saat menyadari kau selamat. Orang yang berdiri di dekatmu mengira kau gugup karena hari kelulusan. Kau tidak membetulkannya. Ada jarak yang sangat tipis antara dunia ini tetap dapat kaulihat dan semua hal yang tak akan pernah sempat kaulakukan.

Sistem tidak pernah bicara lagi. Lama sesudah hari itu, kau kadang terbangun untuk memastikan masih ada suara kota di luar. Perlahan, keheningan di kepalamu berubah dari sesuatu yang mencurigakan menjadi tempat yang cukup luas untuk keinginanmu sendiri."""

    # ┌─ ENDING · E-SI-03 · Penonton Terakhir  [Romantis · host Y/C]
    # │ KAPAN   : deviasi tinggi; rapport_sistem tinggi
    # │ ISI SKRG: Sistem membacakan semua yang ia hitung, lalu pamit seperti teman
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-03"] = """Sistem membacakan perjalananmu lebih lama daripada yang diperlukan untuk memberi hasil. Nama, pilihan, perubahan yang dahulu disampaikannya sebagai angka kini terdengar seperti catatan seseorang yang memang selalu ada di sana.

Kau tidak lupa bahwa ia mengancammu. Kedekatan yang terbentuk tidak membuat kontrak itu baik. Namun ketika ia mengatakan kau lolos, ada jeda yang tidak menyerupai ejekan. Ia menyebutmu penonton yang terlalu jauh masuk ke cerita, kemudian mengaku penasaran apa yang akan kaulakukan tanpa dirinya.

Kau menjawab bahwa itu bukan urusannya lagi. Ia tertawa, atau mengeluarkan suara yang cukup mirip tawa, lalu berpamitan. Tidak ada janji akan bertemu kembali. Kau berdiri sebentar, berduka pada sesuatu yang tidak pernah layak disebut teman sepenuhnya, sebelum kembali kepada orang yang masih bisa kausentuh."""

    # ┌─ ENDING · E-SI-04 · Kontrak Baru  [Khusus · host Y/C]
    # │ KAPAN   : deviasi tinggi; sikap penyelidik
    # │ ISI SKRG: Sistem menawarkan kontrak baru (kait New Game Plus)
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-04"] = """Kau telah terlalu sering bertanya sampai Sistem berhenti berpura-pura tidak mendengar. Sesudah hasil yang tinggi diumumkan, ia menampilkan tawaran baru. Syaratnya belum seluruhnya terbuka. Imbalannya disusun agar terdengar lebih menarik daripada kebebasan yang baru saja kaudapatkan.

Kau membaca tanpa segera menjawab. Tiga tahun pertama mengajarimu bahwa kata yang tidak ditanyakan dapat berubah menjadi ancaman, dan bahwa rasa ingin tahu bukan alasan menyerahkan hidup tanpa mengetahui harga.

Jendela itu tetap menunggu. Di luar, ada orang yang mengharapkanmu datang merayakan kelulusan. Kau memiliki pilihan yang dulu tidak pernah diberikan pada awal kontrak: membiarkan tawaran terbuka sambil memutuskan apakah benar ada jawaban di baliknya yang lebih berharga daripada hidupmu sekarang."""

    # ┌─ ENDING · E-SI-05 · Gagal di Bawah Sakura  [Buruk · host Y/C]
    # │ KAPAN   : deviasi kurang; pemain di kampus
    # │ ISI SKRG: pemain mati di hari wisuda, di bawah sakura
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-05"] = """Sakura bergerak di atas halaman kampus ketika Sistem mengumumkan bahwa hasilmu tidak cukup. Kau mendengar tepuk tangan dari arah gedung wisuda dan sempat berpikir betapa kejamnya dua suara itu dapat berlangsung bersamaan.

Kau mencoba menyebut nama seseorang. Orang-orang yang melihatmu mendadak berhenti segera mendekat dan mencari pertolongan. Mereka tidak tahu ada kontrak yang telah memutuskan akhir ini; yang mereka lihat adalah seseorang yang seharusnya masih memiliki banyak hari sesudah kelulusan.

Kelopak jatuh di dekat tanganmu. Sesudahnya, dunia tetap berlanjut dengan pertanyaan yang tidak dapat dijawab oleh mereka yang tinggal. Kegagalan yang dihitung Sistem tidak menjelaskan seluruh hidupmu. Ia hanya kekuasaan yang menolak memberimu kesempatan berikutnya."""

    # ┌─ ENDING · E-SI-06 · Cinta yang Tidak Dihitung  [Buruk · host C]
    # │ KAPAN   : Chiasa × Yutaka saja
    # │ ISI SKRG: "Ini bukan penyimpangan. Ini pelarian."
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-06"] = """Yutaka menggenggam tanganmu ketika suara Sistem menyela. Kau melihat wajah orang yang mencintaimu dan menyadari ia tidak dapat mendengar keputusan yang sedang dijatuhkan di antara dua tarikan napas kalian.

Sistem mengatakan hubungan kalian bukan penyimpangan yang dimintanya. Dalam perhitungannya, hidup Koita belum cukup berubah. Kau telah mengetahui peringatan itu, tetapi tetap sempat berharap kebahagiaan yang nyata dapat membuat aturan yang kejam merasa malu.

Tidak ada rasa malu dalam suaranya. Yutaka memanggil namamu ketika kau mulai kehilangan kekuatan. Cinta kalian sungguh ada; justru itu yang membuat akhir ini tidak dapat dianggap bukti bahwa ia tidak cukup berharga. Yang tidak menghitungnya adalah sesuatu yang sejak awal hanya peduli pada kontrak."""

    # ┌─ ENDING · E-SI-07 · Tubuh Pinjaman Menyerah  [Buruk · host Y/C]
    # │ KAPAN   : mati karena tubuh sebelum wisuda
    # │ ISI SKRG: tubuh host berhenti lebih dulu daripada kontraknya
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-07"] = """Tubuhmu berhenti sanggup mengikuti jauh sebelum tanggal evaluasi. Semua jadwal yang kaubela dengan alasan hanya sedikit lagi akhirnya ditinggalkan di meja, bersama pesan yang tidak sempat dibalas.

Orang-orang mencari pertolongan dan menunggu kabar. Sebagian baru mengetahui betapa lama kau menyembunyikan kelelahan dan sakit. Sistem tidak memberi waktu tambahan karena kau sudah berusaha keras. Tubuh yang dipinjamkan kepadamu tidak menjadi lebih kebal hanya karena ada ancaman di dalam kepalamu.

Hari kelulusan datang kemudian, tanpa dirimu. Mereka yang mengenangmu juga harus hidup dengan kemarahan karena kau merasa perlu terus memaksa agar layak tinggal. Tidak ada perhitungan yang dapat mengembalikan kesempatan sederhana untuk berhenti, meminta bantuan, dan membiarkan esok datang."""

    # ┌─ ENDING · E-SI-08 · Pembangkang  [Buruk · host Y/C]
    # │ KAPAN   : hukuman kritis karena pembangkangan sengaja
    # │ ISI SKRG: Sistem menagih lebih awal
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-08"] = """Kau menolak dengan sadar, kali ini tanpa mencoba membuatnya terdengar seperti salah paham. Sistem memperingatkanmu, lalu menunggu cukup lama untuk memastikan bahwa jawabanmu tidak berubah.

Hukuman datang sebelum hari yang selama ini dijadikan batas. Kau tidak mempunyai pidato yang membuatnya kehilangan kuasa. Di sekelilingmu, orang lain terus menjalani hari biasa, tidak tahu bahwa sebuah keputusan tentang hidupmu baru saja diambil oleh sesuatu yang tidak dapat mereka temui.

Penolakanmu tetap milikmu, tetapi tidak membuat akibatnya indah. Mereka yang menemukanmu memanggil bantuan dan namamu berkali-kali. Kisah ini berakhir sebelum kontrak selesai, meninggalkan keberanian, kemarahan, dan kesedihan tanpa menyatukannya menjadi kemenangan yang mudah."""

    # ┌─ ENDING · E-SI-09 · Lolos di Balik Jeruji  [Khusus · host Y/C]
    # │ KAPAN   : lolos; sedang dipenjara
    # │ ISI SKRG: "Selamat, kau hidup. Di sini."
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-09"] = """Di balik jeruji, Sistem mengumumkan bahwa kau lolos. Suaranya hampir riang ketika menambahkan bahwa hidup yang diberikan kepadamu akan tetap berlangsung di sini.

Kau duduk tanpa menjawab. Selamat dari kontrak tidak mengubah putusan, menghapus kejahatan, atau memulihkan orang yang dirugikan. Waktu yang dahulu kauhitung menuju wisuda kini diukur dengan jadwal yang ditentukan orang lain.

Ketika jendela biru lenyap, ruangan tidak berubah. Ada langkah petugas di lorong dan suara orang lain menunggu panggilan. Kau masih hidup, dengan hari-hari yang harus dijalani serta pertanggungjawaban yang tidak dapat kauselesaikan hanya karena ancaman paling aneh dalam kepalamu sudah pergi."""

    # ┌─ ENDING · E-SI-10 · Gagal di Balik Jeruji  [Buruk · host Y/C]
    # │ KAPAN   : gagal; sedang dipenjara
    # │ ISI SKRG: mati di sel pada jam wisuda
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-10"] = """Kau mengetahui jam wisuda dari jadwal yang masih diingat, bukan dari pemandangan kampus. Di sel, suara Sistem datang tepat pada waktunya dan mengatakan hasilmu tidak memenuhi kontrak.

Kau memanggil, lalu kehilangan kemampuan menyelesaikan kalimat. Orang di dekatmu menyadari ada yang salah; bantuan dicari melalui pintu dan lorong yang membatasi setiap gerakan. Mereka tidak mempunyai cara melawan sesuatu yang bahkan tidak mereka ketahui ada.

Sesudah kematianmu, berkas hukum tetap mencatat kehidupan yang membawamu ke sini. Orang yang pernah kaulukai tetap memiliki urusan pemulihannya sendiri. Akhir kontrak tidak menyelesaikan kisah mereka, dan kematian pelaku tidak mewajibkan siapa pun mengubah kesaksian menjadi pengampunan."""

    # ┌─ ENDING · E-SI-11 · Hidup Tanpa Nama  [Khusus · host Y/C]
    # │ KAPAN   : lolos; reputasi hancur di semua lingkungan
    # │ ISI SKRG: hidup, tetapi tak ada yang menunggu
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-11"] = """Kau selamat. Sistem mengucapkannya tanpa menanyakan siapa yang masih bersedia mendengar kabar itu darimu. Setelah jendelanya hilang, ponsel tetap sepi.

Di tempat yang pernah kaukenal, orang menghindar atau berbicara seperlunya. Reputasi yang hancur tidak membedakan setiap kesalahan dengan adil, tetapi ada perbuatan nyata yang tidak dapat kausangkal hanya karena kini rasanya menyakitkan menjadi orang yang dijauhi.

Kau mencari tempat tinggal dan pekerjaan yang tidak menanyakan lebih banyak daripada yang sanggup kaujawab. Hidup terus tersedia, tanpa penonton yang menjanjikan perubahanmu akan disambut. Apa yang akan kaulakukan dengannya tidak lagi diatur Sistem. Itu kebebasan yang kecil, keras, dan sepenuhnya membutuhkan tanggung jawabmu."""

    # ┌─ ENDING · E-SI-12 · Figuran yang Baik  [Romantis · host Y/C]
    # │ KAPAN   : pemain berhenti memanipulasi dan membantu heroine pulih; mereka lepas dari Koita dan berdiri sendiri
    # │ ISI SKRG: lolos lewat kebaikan; deviasi lahir dari orang-orang yang bebas
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-12"] = """Sistem lama diam sebelum membacakan hasil. Orang-orang yang pernah diletakkan naskah di sekitar Koita telah memilih kehidupan sendiri, bukan karena menjadi milikmu, melainkan karena akhirnya memiliki ruang untuk menginginkan hal lain.

Kau membantu tanpa meminta cinta sebagai imbalan. Ada pertolongan yang diteruskan orang lain, pemulihan yang tetap sulit, dan penolakan yang harus kauhormati. Perubahan itu cukup nyata untuk melewati ambang yang selama ini menakutkanmu.

Kau lolos. Ketika suara Sistem menghilang, tidak ada mahkota yang menggantikan ancamannya. Hanya pesan seorang teman tentang rencana makan dan hari esok yang belum ditulis. Kau membalas, senang karena tidak perlu menjadi tokoh terpenting dalam hidup mereka untuk tetap mempunyai tempat."""

    # ┌─ ENDING · E-SI-13 · Kebaikan yang Tidak Dihitung  [Buruk · host Y/C]
    # │ KAPAN   : pemain berbuat baik tetapi deviasi kurang
    # │ ISI SKRG: mati, tetapi dunia yang ditinggalkan lebih baik
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-13"] = """Kau telah membantu, tetapi tidak cukup menyimpangkan kisah menurut perhitungan Sistem. Mendengar kedua hal itu dinyatakan bersamaan membuatmu ingin tertawa dan marah sekaligus. Kebaikan tidak pernah dijanjikan sebagai perlindungan oleh kontrak ini.

Orang yang kaupertahankan tetap hidup. Ada yang berani mencari bantuan, ada yang terbebas dari orang yang memanfaatkannya, ada yang akhirnya dapat tidur tanpa takut. Semua itu nyata, bahkan ketika Sistem menyebut hasil akhirnya gagal.

Kematianmu meninggalkan kesedihan yang tidak dapat dibayar dengan menyebut pengorbananmu indah. Mereka lebih suka kau masih ada untuk makan bersama. Dunia yang ditinggalkan memang lebih baik pada beberapa bagiannya, dan justru karena itu kehilanganmu terasa begitu tidak perlu serta begitu kejam."""

    # ┌─ ENDING · E-SI-14 · Jauh dari Panggung  [Khusus · host Y/C]
    # │ KAPAN   : pemain di kota atau negara lain saat wisuda
    # │ ISI SKRG: lolos atau gagal tanpa menyaksikan wisuda
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-14"] = """Saat wisuda Kouseikan berlangsung, kau berada jauh dari kampus. Jam setempat menunjukkan waktu yang berbeda, tetapi kontrak tidak mengenal keterlambatan karena jarak. Jendela biru muncul di atas hari yang telah kaususun seperti hari biasa.

Hasil evaluasi tetap mengikuti apa yang sungguh berubah selama tiga tahun, bukan seberapa jauh kau pergi sesudahnya. Jarak memberimu jalan lain, pekerjaan lain, dan orang yang tidak mengenal cerita lama. Ia tidak menghapus keputusan yang telah membawamu ke saat ini.

Kau menatap jendela dan memikirkan halaman kampus yang tidak sedang kaulihat. Pengumuman itu sampai juga. Nasibmu ditetapkan tanpa tepuk tangan wisuda, di tempat yang mungkin tidak akan pernah mengetahui mengapa kau mendadak terdiam ketika hari masih berjalan."""

    # ┌─ ENDING · E-SI-15 · Pengakuan yang Tidak Dipercaya  [Khusus · host Y/C]
    # │ KAPAN   : rahasia Sistem dibuka luas; dianggap gila
    # │ ISI SKRG: evaluasi terjadi di ruang rawat; hasil mengikuti deviasi
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-15"] = """Di ruang rawat, kau menunggu tanggal yang membuatmu ketakutan. Cerita tentang Sistem telah didengar banyak orang, tetapi tidak menjadi kenyataan yang mereka pahami seperti kau memahaminya. Petugas tetap menanyakan tidur, makanan, rasa aman, dan orang yang ingin kauhubungi.

Ketidakpercayaan mereka tidak memberi kepastian tentang kontrak. Pada jam evaluasi, suara itu datang hanya kepadamu. Hasilnya mengikuti perubahan hidup yang sudah terjadi, tanpa terpengaruh oleh sebutan yang dipakai orang lain untuk menjelaskan keyakinanmu.

Di luar jendela, cahaya bergeser seperti pada hari lain. Ada orang yang mengetuk sebelum masuk dan menanyakan keadaanmu. Apa pun hasil yang dibawa Sistem, pertanyaan itu tetap datang dari seorang manusia yang sedang berusaha merawat, bukan dari penonton yang ingin menentukan apakah ceritamu cukup masuk akal."""

    # ┌─ ENDING · E-SI-16 · Tagihan dari Orang Lain  [Buruk · host Y/C]
    # │ KAPAN   : dibunuh atau dilukai fatal oleh NPC
    # │ ISI SKRG: kematian karena tindakan orang yang pernah disakiti
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-16"] = """Kekerasan datang dari seseorang yang pernah kausakiti. Tidak ada kesempatan menyusun penjelasan lengkap, hanya kemarahan yang sudah terlalu jauh dan upaya orang di sekitar menghentikan yang sedang terjadi.

Kau meninggal sebelum evaluasi. Orang yang menyerang tidak mendapat kembali kehidupan yang dirusak dengan menghilangkan hidupmu. Ia juga harus menghadapi akibat tindakannya, sementara orang-orang lain menanggung kejutan kehilangan dan pertanyaan yang tidak selesai.

Sistem tidak memberikan penutupan yang memuaskan. Perbuatanmu dan perbuatan penyerang tetap dua tanggung jawab yang berbeda. Di akhir ini, rasa sakit tidak memulihkan siapa pun dengan sendirinya; ia berpindah ke lebih banyak rumah, lebih banyak percakapan, dan hari-hari yang akan sulit dijalani."""

    # ┌─ ENDING · E-SI-17 · Penipu yang Tertipu  [Buruk · host Y/C]
    # │ KAPAN   : hasil yang dinilai hanyalah sandiwara
    # │ ISI SKRG: Sistem harian tertipu sampai akhir; evaluasi tidak
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-17"] = """Kau sampai ke evaluasi dengan keyakinan bahwa susunanmu cukup rapi. Pernyataan cinta telah diucapkan, perpisahan dipentaskan, dan laporan harian tampak mendukung hasil yang kaubutuhkan.

Sistem berhenti pada bagian yang tidak berubah. Perasaan yang hanya diperagakan tidak menjadi nyata karena disepakati beberapa orang, dan hidup Koita tidak sungguh menyimpang hanya karena kau membuatnya tampak demikian dari luar. Untuk pertama kalinya, tidak ada kalimat tambahan yang dapat memperpanjang permainan itu.

Hasilnya gagal. Kau mendengar penipuanmu disebut dengan ketenangan yang hampir menyamai caramu dahulu menjelaskan semuanya kepada orang lain. Di sekitar, mereka masih mengira pertunjukan telah selesai dengan baik. Mereka baru menyadari ada sesuatu yang sungguh terjadi ketika kau tidak lagi dapat menjawab."""

    # ┌─ ENDING · E-SI-18 · Celah yang Tidak Pernah Dicatat  [Khusus · host Y/C]
    # │ KAPAN   : koita_bebas_naskah benar — nyaris mustahil, lihat bagian 11
    # │ ISI SKRG: pemain lolos tanpa NTR dan tanpa mati, lewat satu celah dalam kontrak yang tidak pernah diantisipasi siapa pun, termasuk Sistem sendiri
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-SI-18"] = """Koita memilih keluar dari peran yang terus disediakan baginya. Ia tidak menyerahkan seluruh cinta kepada satu pemenang, tidak menunggu orang lain menjadi alasan untuk berubah, dan tidak meminta kau menggantikannya sebagai pusat cerita.

Sistem mencoba menghitung dengan ukuran lama, lalu berhenti. Kontraknya mengandaikan seorang protagonis yang terus menjalankan naskah, sehingga penyimpangan hanya dapat dibaca sebagai sesuatu yang diambil darinya. Kini Koita sendiri telah memilih kehidupan yang tidak mengikuti anggapan itu.

Tidak ada hubungan yang perlu direbut agar kau tetap hidup. Jendela biru menghilang tanpa ejekan terakhir. Koita bertanya apa yang akan kalian lakukan besok. Kau melihat seseorang yang bebas menanyakan itu, lalu menyadari untuk pertama kalinya bahwa kau juga bebas menjawab tanpa mencari celah lain dalam ancaman."""

    # ┌─ ENDING · E-FO-01 · Jeruji  [Buruk · host Y/C]
    # │ KAPAN   : laporan atau bukti kuat; investigasi tuntas
    # │ ISI SKRG: dipenjara; game berlanjut di Rute Jeruji; evaluasi tetap terjadi di sel
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-01"] = """Laporan dan pemeriksaan akhirnya menjadi perkara yang tidak dapat kauhentikan dengan penyangkalan. Kesaksian didengar, bukti dinilai, dan putusan membawa hidupmu ke balik jeruji.

Korban tidak datang untuk memberikan pengampunan pada hari terakhir. Ia berhak menjaga jarak, meminta perlindungan, dan memilih siapa yang menemaninya menghadapi proses. Pemenjaraanmu tidak serta-merta membuat tidurnya tenang atau menghapus ketakutan yang telah kautinggalkan.

Di sel, kau mendengar kalender tetap berjalan menuju wisuda. Kontrak belum berakhir, tetapi kehidupan di luar tidak ditunda demi hasil evaluasimu. Ada tanggung jawab hukum yang harus dijalani, dan ada kerusakan yang tidak akan lunas hanya karena kau telah kehilangan kebebasan."""

    # ┌─ ENDING · E-FO-02 · Dikeluarkan dan Hancur Sosial  [Buruk · host Y/C]
    # │ KAPAN   : bukti cukup untuk kampus, tidak cukup untuk penjara
    # │ ISI SKRG: dikeluarkan; reputasi hancur di semua lingkungan; Rute Luar Kampus
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-02"] = """Keputusan kampus memutus aksesmu kepada ruang yang dahulu begitu mudah kaumasuki. Namamu dihapus dari daftar kegiatan, urusan akademik berhenti, dan teman-teman diberi alasan untuk tidak lagi menganggap kedatanganmu sesuatu yang biasa.

Perkara belum menghasilkan pemenjaraan. Itu tidak mengubah keputusan disiplin menjadi kebohongan atau luka korban menjadi sesuatu yang kurang nyata. Ia tetap menghadapi hari-hari sulit dan kebutuhan akan ruang yang aman tanpa bertemu denganmu.

Kau menjalani hidup di luar kampus dengan reputasi yang hancur. Sistem masih menghitung dari kejauhan. Dunia yang dulu dapat kaudatangi sesuka hati kini mempunyai batas yang ditujukan kepadamu, dan tak seorang pun wajib membukakannya hanya karena kau merasa masa depanmu telah menyempit."""

    # ┌─ ENDING · E-FO-03 · Lolos tapi Dihantui  [Khusus · host Y/C]
    # │ KAPAN   : force_bersih[[korban] bertahan (§10); tidak pernah terbongkar
    # │ ISI SKRG: bebas dari hukum, tidak dari ingatan; korban tetap bisa mendapat Broken Ending
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-03"] = """Tidak ada perkara yang mencapai hukuman. Orang-orang tetap menyapamu, dan kehidupan di luar tampak menerima versi dirimu yang kauperlihatkan. Kebebasan itu tidak membuat peristiwa yang kaulakukan berhenti pernah terjadi.

Korban menghadapi akibatnya tanpa kepastian bahwa orang lain akan memahami. Ada hari yang terlewat, percakapan yang diputus karena terlalu berat, dan rasa aman yang tidak kembali hanya karena ia berhasil tampak tenang. Kau tidak berhak menafsirkan diam sebagai bukti bahwa ia sudah baik-baik saja.

Ingatan itu tetap memasuki hidupmu, melalui tempat, nama, dan jeda ketika orang menyebut kepercayaan. Ketakutanmu terhadap pengungkapan tidak setara dengan luka yang kautimbulkan. Dalam akhir ini kau lolos dari hukum, tetapi tidak mendapat kebenaran yang menjadikan dirimu tak bersalah."""

    # ┌─ ENDING · E-FO-04 · Mengaku dan Menjalani Proses  [Netral · host Y/C]
    # │ KAPAN   : pelaku mengaku
    # │ ISI SKRG: proses hukum; tidak ada pengampunan otomatis; korban menentukan jaraknya sendiri
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-04"] = """Kau mengaku dan berhenti meminta orang lain menjaga versi yang melindungimu. Proses hukum tetap berjalan dengan pertanyaan, pemeriksaan, dan akibat yang tidak dapat ditawar hanya karena pengakuan itu akhirnya datang.

Korban menerima kabar melalui orang yang ia pilih untuk mendampingi. Ia tidak berkewajiban menemuimu, mendengar penyesalanmu, atau menjawab surat. Pengakuanmu baru menghentikan sebagian penyangkalan; ia belum memperbaiki hidup yang telah kaurusak.

Hari-hari berikutnya dipenuhi kewajiban yang lebih konkret daripada rasa bersalah. Kau harus menjawab dengan benar dan menjalani hasil proses. Jika perubahan akan terjadi, ia tidak boleh bergantung pada seseorang yang pernah kausakiti bersedia kembali untuk meyakinkanmu bahwa kau sudah menjadi lebih baik."""

    # ┌─ ENDING · E-FO-05 · Buron  [Buruk · host Y/C]
    # │ KAPAN   : pelaku lari
    # │ ISI SKRG: hidup bersembunyi di kota lain; quest gagal; Sistem menghukum pembangkangan
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-05"] = """Kau pergi ketika perkara mulai mengejarmu. Kota lain tidak membuat kehidupan baru terasa bersih; setiap percakapan biasa dipenuhi takut ditanya terlalu jauh tentang asalmu.

Di tempat yang ditinggalkan, korban dan orang yang mendampingi tetap menjalani proses tanpa kehadiranmu. Kepergianmu menambah penundaan dan ketidakpastian, bukan membatalkan yang telah terjadi. Orang-orang yang pernah membela namamu harus menghadapi kenyataan bahwa kau memilih menghindar.

Kontrak juga tidak menerima pelarian sebagai hasil. Sistem menagih pembangkangan sementara hidupmu semakin sempit oleh ketakutan sendiri. Kau jauh dari kampus, tetapi tidak bebas dari akibat perbuatanmu. Tidak ada alamat baru yang mengubah lari menjadi penyelesaian."""

    # ┌─ ENDING · E-FO-06 · Kakak yang Tidak Menunggu Polisi  [Buruk · host Y/C]
    # │ KAPAN   : Haruto, Kuroiwa, atau kerabat lain tahu lebih dulu
    # │ ISI SKRG: kerabat korban membalas sendiri; pemain cedera berat atau mati (E-SI-16); pembalas ikut ditangkap
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-06"] = """Orang yang menyayangi korban mengetahui apa yang terjadi dan bertindak sebelum proses resmi dapat berjalan. Kemarahan berubah menjadi kekerasan yang tidak berhenti ketika seseorang berteriak meminta tolong.

Kau mengalami cedera berat, dan kabar tentang keadaanmu kini berjalan bersama kabar penangkapan orang yang membalas. Korban kembali dikelilingi pertanyaan, kali ini juga tentang seseorang yang mungkin selama ini menjadi tempatnya merasa aman.

Pembalasan itu tidak memulihkan apa yang telah kauambil. Ia menambah rumah yang harus menunggu kabar dan orang yang perlu menjalani proses hukum. Jika hidupmu berakhir di sini, kejahatanmu tetap harus disebut; jika bertahan, keadaanmu tidak membuat luka korban menjadi hilang. Tidak ada penyelamatan romantis dalam lingkaran kekerasan yang semakin luas ini."""

    # ┌─ ENDING · E-FO-07 · Saksi yang Memeras  [Khusus · host Y/C]
    # │ KAPAN   : saksi (Daichi atau Mei) menyimpan bukti
    # │ ISI SKRG: pemain diperas sampai akhir game
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-07"] = """Seseorang yang mengetahui kekerasan itu memilih memerasmu. Ia menahan apa yang diketahuinya sebagai ancaman, meminta bayaran atau bantuan, lalu membiarkanmu menunggu kapan tuntutan berikutnya datang.

Kau mulai mengatur hidup berdasarkan pesan yang ditakuti. Sementara itu, korban belum mendapatkan keadilan dari pengetahuan yang diperdagangkan tersebut. Perbuatannya dijadikan alat tawar oleh orang lain, dan penderitaannya kembali ditempatkan setelah kepentingan orang yang memegang kuasa.

Pemeras bertanggung jawab atas tindakannya. Kau tetap bertanggung jawab atas kekerasan yang membuat ancaman itu mungkin dipakai. Akhir ini tidak menawarkan pelaku baru agar kau bisa merasa peranmu telah berubah menjadi korban satu-satunya. Ada seseorang di luar transaksi itu yang terus menanggung akibat terberat."""

    # ┌─ ENDING · E-FO-08 · Kasus yang Dibuka Kembali  [Khusus · host Y/C]
    # │ KAPAN   : bukti ditemukan belakangan
    # │ ISI SKRG: epilog: kasus dibuka setelah wisuda; hidup yang tampak selamat runtuh
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-08"] = """Sesudah wisuda, ketika kau mulai mengira masa lalu sudah cukup jauh, panggilan pemeriksaan datang. Keterangan atau bukti yang ditemukan belakangan membuat perkara dibuka kembali.

Kehidupan yang tampak mapan berhenti di tengah rencana biasa. Kau harus menjelaskan hal yang dahulu berhasil tidak dijawab. Orang-orang yang mengenalmu kemudian melihat riwayat yang selama ini tidak pernah masuk ke cerita tentang dirimu.

Bagi korban, terbukanya perkara tidak berarti semua luka langsung sembuh. Ia harus memilih lagi siapa yang dipercaya, bagian mana yang sanggup diceritakan, dan dukungan apa yang dibutuhkan. Waktu yang berlalu tidak mengubah perbuatanmu menjadi sesuatu yang boleh dilupakan hanya karena kau sudah berhasil melanjutkan hidup."""

    # ┌─ ENDING · E-FO-09 · Kejahatan Berantai  [Buruk · host Y/C]
    # │ KAPAN   : lebih dari satu kejahatan; satu membongkar yang lain
    # │ ISI SKRG: semua terbongkar bersamaan
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-09"] = """Satu perkara membuka jalan kepada perkara lain. Orang-orang yang semula mengira pengalamannya terpisah akhirnya mengetahui bahwa ada orang lain yang juga menyimpan ketakutan dan pertanyaan serupa.

Pemeriksaan tidak lagi berhenti pada penjelasan yang kausiapkan untuk satu kejadian. Setiap tindakan tetap perlu dinilai dengan fakta masing-masing. Kau kehilangan kemampuan memisahkan orang-orang yang dirugikan ke dalam ruang kebisuan yang berbeda.

Akibatnya menjangkau kampus, keluarga, dan proses hukum. Bagi mereka yang bersaksi, mengetahui tidak sendirian dapat memberi kekuatan sekaligus duka baru. Bagi dirimu, tidak ada lagi cerita tentang satu kesalahan yang berdiri sendiri. Yang harus dihadapi adalah rangkaian keputusan yang selama ini kaulanjutkan meski tahu ada orang yang terluka."""

    # ┌─ ENDING · E-FO-10 · Skorsing dan Catatan  [Netral · host Y/C]
    # │ KAPAN   : hanya kejahatan ringan–sedang
    # │ ISI SKRG: skorsing satu semester dan catatan polisi; hidup berjalan dengan bekas
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-10"] = """Keputusan akhirnya berupa skorsing satu semester dan catatan resmi yang tidak dapat diperlakukan sebagai urusan administrasi biasa. Perkara dalam akhir ini tidak dinilai sebagai kekerasan seksual, tetapi tetap melibatkan tindakan yang merugikan orang lain.

Kau meninggalkan kampus sementara teman-teman meneruskan jadwal mereka. Ada kesempatan kembali dengan syarat yang jelas, dan ada hubungan yang tidak akan kembali hanya karena masa skorsing selesai.

Ketika membuka kalender semester berikutnya, kau tidak dapat menandai tanggal kepulangan sebagai tanggal semuanya dilupakan. Hidup masih berjalan, dengan kesempatan bekerja dan belajar lagi. Kesempatan itu menuntut perubahan yang dapat dilihat melalui tindakan, tanpa meminta orang yang dirugikan menanggung tugas mengawasimu."""

    # ┌─ ENDING · E-FO-11 · Saksi di Ambang Pintu  [Buruk · host Y/C]
    # │ KAPAN   : Force disaksikan Koita; korban melapor sendiri, atau trust_koita sudah rendah sehingga Koita sendiri mencari bantuan
    # │ ISI SKRG: kasus terkuat; penjara hampir pasti; nasib Koita sendiri mengikuti trust_koita — ia bertindak sebagai saksi (E-KO-20) atau ikut dimintai kesaksian sambil membeku di dalam (E-KO-19)
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-11"] = """Koita berada di ambang pintu ketika memahami bahwa yang terjadi bukan salah paham atau hubungan pribadi yang tidak boleh dicampurinya. Pengetahuan itu mengubah wajahnya sebelum ia sanggup bergerak.

Perkara kemudian mendapat laporan dan kesaksian yang kuat. Pada bagian yang dapat diucapkan, Koita menjawab; pada bagian yang membuatnya membeku, ia perlu waktu dan pendampingan. Korban tidak kehilangan hak dipercaya hanya karena saksi juga mengalami ketakutan.

Kau menghadapi proses yang semakin sulit dielakkan. Persahabatan lama tidak lagi dapat dipakai untuk membujuk Koita menutup mata. Apa pun yang terjadi pada keberaniannya sesudah hari itu, ia telah melihat sesuatu yang tidak akan berubah menjadi cinta dengan diberi nama lain, dan dunia mulai mendengar apa yang selama ini ingin kausimpan di balik pintu."""

    # ┌─ ENDING · E-FO-12 · Kurungan Tanpa Jeruji  [Khusus · host Y/C]
    # │ KAPAN   : korban tidak melapor dan tetap terikat pada pemain lewat takut, ancaman, atau ketergantungan
    # │ ISI SKRG: dihitung Sistem sebagai lepas dari Koita; tidak pernah ditulis sebagai cinta; bisa retak kapan saja lewat sahabat, bukti, atau korban sendiri (E-FO-08)
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-12"] = """Dari luar, korban masih berada dekatmu. Ia menjawab pesan, datang ketika diminta, atau mengatakan semuanya baik-baik saja pada saat orang bertanya terlalu cepat. Orang yang hanya melihat permukaan mungkin mengira hubungan itu bertahan.

Di dalamnya ada takut, ancaman, atau ketergantungan yang membuat pilihan terasa sempit. Kedekatan itu bukan persetujuan yang bebas, dan keberadaannya di sisimu bukan akhir romantis. Ia tetap seseorang yang memiliki keinginan sendiri, meskipun kau terus memperlakukan ketidakmampuannya pergi sebagai kemenangan.

Sistem dapat menghitung jaraknya dari Koita. Perhitungan itu tidak mengubah kurungan menjadi rumah. Ada sahabat yang masih mencoba mendekat, ada pertanyaan yang belum berhenti, dan kemungkinan bahwa suatu hari korban akan mendapat ruang cukup aman untuk berbicara tanpa memeriksa reaksimu lebih dahulu."""

    # ┌─ ENDING · E-FO-13 · Kebetulan yang Datang Tepat Waktu  [Buruk · host Y/C]
    # │ KAPAN   : plot armor membawa Koita sebelum terjadi
    # │ ISI SKRG: percobaan gagal; korban berlindung pada Koita; pemain menanggung percobaan itu: laporan, skorsing, rumor
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-13"] = """Koita datang sebelum percobaan itu menjadi kekerasan yang hendak kaulakukan. Ia melihat ketakutan di wajah orang yang berada bersamamu dan berhenti mendengar alasanmu sebagai penjelasan yang harus diterima lebih dulu.

Korban mendapat jarak untuk meminta pertolongan. Koita tetap bersamanya sampai ada orang lain yang ia percaya. Kedatangan tepat waktu itu tidak menghapus ancaman yang telah terjadi, tetapi memberi kesempatan agar kejadian hari itu tidak diteruskan sesuai kehendakmu.

Laporan, pemeriksaan kampus, dan pembicaraan yang menyusul tetap menyangkut pilihanmu. Kau tidak berhak menyebut semuanya tidak berarti hanya karena percobaan gagal. Orang yang hampir kausakiti tetap perlu memulihkan rasa aman, dan keberhasilan ia keluar dari keadaan itu bukan sesuatu yang dapat kauklaim sebagai kebaikanmu."""

    # ┌─ ENDING · E-FO-14 · Dua Orang yang Diam  [Khusus · host Y/C]
    # │ KAPAN   : Koita menyaksikan tetapi diam karena takut, malu, atau diancam
    # │ ISI SKRG: pelaku bebas dari hukum, tetapi dua orang tahu; korban dan Koita sama-sama hancur dalam diam
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-14"] = """Koita mengetahui apa yang terjadi dan tidak melaporkannya. Takut, malu, dan ancaman membuat kalimat yang telah disiapkannya berhenti sebelum sampai kepada orang lain. Korban pun belum berada di tempat yang cukup aman untuk berbicara.

Kau tetap bebas dari proses hukum dalam akhir ini. Di luar, hubungan sosial tampak terus berjalan. Di dalam dua kehidupan lain, ada kejadian yang kembali melalui tidur, tempat, dan pertemuan yang tidak lagi terasa biasa.

Kebisuan mereka bukan persekutuan denganmu. Membeku bukan persetujuan, dan tidak melapor bukan pembatalan kekerasan. Mereka sama-sama tahu sesuatu yang tidak diketahui dunia. Setiap hari yang berlalu tanpa pengungkapan memperpanjang kesendirian itu, sementara hak mereka mendapat pertolongan tetap ada meski belum sanggup diminta."""

    # ┌─ ENDING · E-FO-15 · Pembalikan yang Terbongkar  [Buruk · host C]
    # │ KAPAN   : jalur manipulasi pembalikan Chiasa (06_Chiasa.md §14); framing runtuh
    # │ ISI SKRG: fitnah terbongkar lewat bukti, saksi, atau Shiori/Hanabusa; Chiasa menanggung Force sekaligus fitnah dan obstruksi, konsekuensi lebih berat
    # └─ tulis isi penuh di baris bawah (hapus "# ", isi di antara kutip) ──
    KK_END_TEXT["E-FO-15"] = """Cerita yang menjadikan Koita tertuduh akhirnya runtuh. Keterangan yang diperiksa tidak lagi mendukung versi Chiasa, dan orang-orang yang dahulu membela dengan yakin harus menghadapi apa yang telah ikut mereka sebarkan.

Kekerasan yang dilakukan Chiasa tidak menghilang di balik terbongkarnya fitnah. Kini proses juga menyangkut tuduhan palsu dan upaya menghalangi kebenaran. Koita perlu mendapatkan kembali namanya, sementara orang lain yang dirugikan tetap mempunyai luka yang tidak dapat dirangkum menjadi skandal keluarga.

Daisuke dan Yoshie datang dengan wajah yang lelah. Mereka tetap orang tua, tetapi tidak menjanjikan perlindungan dari pertanggungjawaban. Bagi Chiasa, tidak ada akhir berupa pelukan yang mengubah semua ini menjadi cinta yang salah jalan. Yang tersisa adalah kebenaran yang akhirnya didengar, proses yang harus dijalani, dan hak orang yang disakiti untuk menjauh."""
