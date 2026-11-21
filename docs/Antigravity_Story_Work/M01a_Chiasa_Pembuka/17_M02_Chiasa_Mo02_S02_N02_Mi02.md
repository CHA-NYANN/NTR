# Grand Bab M02 — Host Chiasa (`Mo02` → `S02` → `N02` → `Mi02`)
*(Melengkapi `K02` Host Chiasa di `game/kk_ryokan.rpy`)*

Target File: `game/kk_spring.rpy` (`kkscene_Mo02`, `kkscene_S02`, `kkscene_Mi02`, `kkscene_N02`, blok `if kk_host == "chiasa":`)

## 1. `Mo02` — *Undian Onsen*
```renpy
label kkscene_Mo02:
    call kk_scene_enter("moeka", "Stasiun Kouseikan-mae")
    if kk_host == "chiasa":
        nar "Sore hari di depan perbelanjaan dekat Stasiun Kouseikan-mae cukup ramai oleh mahasiswa dan warga sekitar yang baru pulang beraktivitas. Di dekat pintu kaca pusat perbelanjaan, sebuah stan undian belanja berhias pita warna-warni masih memutar lonceng kuningan setiap kali ada pembeli yang mendapat hadiah kecil."
        nar "Kau baru saja keluar dari gerbang tiket stasiun sambil menenteng tas kainmu ketika suara teriakan tertahan yang familiar membuat beberapa orang menoleh ke arah meja undian."
        nar "Di sana, Kohinata Moeka berdiri membeku sambil menggenggam selembar kupon hadiah bergambar pemandian air panas dengan kedua tangannya—seolah takut kertas itu mendadak berubah menjadi salah baca kalau ia berkedip terlalu lama. Di sampingnya, petugas stan baru saja berhenti membunyikan lonceng besar warna emas."
        nar "Begitu matanya yang biru cerah menangkap sosokmu yang berjalan melintas di trotoar, Moeka langsung berlari kecil menghampirimu sambil mengacungkan kertas undian itu hati-hati."
        moeka "Chimian! Chimian, tolong cubit pipiku sebentar—ini beneran tulisan hadiah utama paket perjalanan onsen buat rombongan, kan?! Aku nggak salah baca huruf kanjinya, kan?!"
        nar "Kau menunduk membaca tulisan tercetak tebal di kertas itu: kupon menginap rombongan di sebuah ryokan pemandian air panas, lengkap dengan kolom tanggal keberangkatan yang harus segera dikonfirmasi sebelum akhir bulan."
        chiasa "Beneran hadiah utama, Moemoe-senpai. Lengkap sama jatah kamar rombongannya."
        moeka "Menang! Seriusan aku menang?! Padahal tadi aku cuma ikut mutar roda undian gara-gara kupon belanja dari minimarket sama toko kain hampir habis masa berlakunya hari ini!"
        nar "Moeka tertawa kecil penuh semangat, lalu tawa itu melambat sepersekian detik saat ia menatap lembaran syarat dan tanggal di bagian bawah kupon. Alisnya sedikit berkerut antara senang dan cemas."
        moeka "Wah... sekarang kita beneran harus bikin rencana perjalanan, dong. Seru banget sih, tapi agak seram juga ya—soalnya rencananya harus benar-benar rapi biar nggak kacau pas hari-H."
        if any(c["ev"] == "Mo01" and c["key"] == "C" for c in choices_log):
            nar "Melihat caranya langsung memikirkan daftar peserta dan jadwal di tengah rasa kagetnya, kau teringat betul bagaimana ia mengatur kerumunan dan terpal saat piknik Hanami kemarin."
    call kk_family_menu("Mo02", ["\"Selamat! Nikmati dulu saja rasa senangnya.\"", "\"Wah, iri juga sih bisa seberuntung itu.\"", "Tawarkan bantuan untuk ikut memeriksa rencana perjalanannya."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau tersenyum dan memutuskan membiarkannya menikmati momen langka itu tanpa langsung membebaninya dengan urusan jadwal dan daftar nama."
            chiasa "Selamat, Moemoe-senpai! Urusan jadwal bisa dipikirkan nanti malam—sekarang nikmati dulu saja rasa senangnya."
            nar "Bahu Moeka yang sempat sedikit naik karena memikirkan teknis acara langsung mengendur. Ia menatap kembali tiket di tangannya, lalu tertawa lepas."
            moeka "Hehe... iya juga ya! Rasanya masih belum percaya banget. Tahu nggak, Chimian, tadi pagi waktu aku bereskan dompet, kupon struknya hampir ikut kubuang ke tempat sampah dekat mesin tiket lho."
            chiasa "Untung tidak jadi dibuang."
            moeka "Asli! Biasanya kalau urusan barang kecil begini aku selalu ceroboh dan berakhir nyesel sendiri. Tapi kali ini malah jadi tiket onsen! Rasanya kayak sekali-sekali semesta lagi baik banget sama aku~"
            nar "Ia menyelipkan kupon hadiah itu ke dalam map plastik kecil di tas kanvasnya dengan gerakan ekstra hati-hati—sangat berbeda dari kebiasaannya yang serba tergesa—lalu menoleh padamu dengan wajah berseri-seri."
            moeka "Nanti begitu tanggalnya ketemu, Chimian wajib ikut ya! Pokoknya nggak boleh absen!"
            nar "Melihat kegembiraannya yang begitu ringan tanpa sedikit pun beban tambahan, kau hanya mengangguk sambil tersenyum tipis."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kau menatap kertas undian itu lalu melontarkan komentar jujur yang agak kering tanpa banyak berpikir."
            chiasa "Wah, iri juga sih. Aku bahkan tidak pernah dapat hadiah tisu dari undian belanja, tapi Moemoe-senpai malah langsung dapat paket menginap."
            nar "Senyum lebar di wajah Moeka surut sepersekian detik. Ia menurunkan sedikit kupon di tangannya, menunduk menatap kertas itu dengan ekspresi canggung, seolah mendadak ragu apakah kegembiraannya tadi terlihat berlebihan."
            moeka "Eh... kalau aku yang beneran berharap menang, biasanya malah meleset terus kok, Chimian. Ini beneran cuma kebetulan saja."
            chiasa "Tetap saja, itu keberuntungan besar."
            nar "Moeka diam sejenak sambil memutar sudut kertas di antara jari-jarinya, lalu mengangkat wajah kembali menatapmu dengan nada yang lebih pelan."
            moeka "Tapi... nanti Chimian juga ikut pergi dan menikmati onsen-nya bareng-bareng, kan? Aku nggak mau hadiah ini malah bikin kita jadi hitung-hitungan siapa yang lebih beruntung."
            chiasa "Iya, tentu saja. Maaf kalau tadi kedengaran sinis."
            nar "Ia mengangguk kecil dan kembali tersenyum, tetapi binar meluap-luap yang tadi memenuhi matanya tampak sudah jauh lebih tertahan saat ia menyimpan kupon itu ke dalam tas."
    else:
        if kk_host == "chiasa":
            nar "Melihat raut cemas tipis di balik kegembiraan Moeka saat membaca tulisan syarat kecil di bagian bawah kertas, kau melangkah setengah langkah lebih dekat dan menunjuk bangku panjang di dekat taman kecil depan stasiun."
            chiasa "Kalau mau, kita duduk sebentar di bangku sana sambil mengecek syarat dan tanggalnya sekarang, Moemoe-senpai. Biar lebih jelas apa saja yang perlu disiapkan."
            nar "Mata biru Moeka langsung berbinar lega—jauh lebih tulus daripada tawa hebohnya semenit lalu."
            moeka "Boleh banget! Ayo! Chimian baca dari daftar syarat paling atas ya, nanti aku catat di ponsel siapa saja yang kira-kira bisa ikut dan tanggal mana yang nggak bentrok sama jadwal kuliah!"
            nar "Kalian duduk berdampingan di bangku kayu depan stasiun. Kau membacakan poin demi poin: batas akhir reservasi ryokan, jumlah kamar yang ditanggung kupon, serta biaya transportasi kereta dan makan tambahan yang tidak termasuk dalam hadiah."
            moeka "Oke, berarti kereta pulang-pergi kita patungan sendiri—untung nggak terlalu mahal kalau pakai tiket rombongan. Terus soal daftar peserta, nanti aku kabari di grup malam ini biar semua bisa konfirmasi sebelum Jumat."
            chiasa "Jangan lupa catat juga siapa yang punya alergi makanan sebelum telepon ryokan-nya, Senpai."
            moeka "Wah, iya juga! Hampir saja kelewat kalau nggak kauingatkan. Serius deh, Chimian, kalau mikir angkanya bareng begini rasanya langsung tenang banget—nggak kerasa kayak harus mengingat semuanya sendirian di kepalaku."
            nar "Ia menepuk buku catatan kecilnya dengan senyum puas yang hangat. Kegembiraannya kini terasa jauh lebih mantap karena bukan lagi beban yang harus ia pikul sendiri."
```

## 2. `S02` — *Ruang Catur di Ryokan*
```renpy
label kkscene_S02:
    call kk_scene_enter("shiori", "Lobi ryokan")
    if kk_host == "chiasa":
        nar "Malam hari di lobi penginapan ryokan terasa jauh lebih tenang daripada ruang makan yang tadi penuh obrolan rombongan. Cahaya lampu kuning hangat dari lentera kertas memantul lembut di atas lantai kayu gelap, sementara suara air pancuran bambu di taman luar sesekali terdengar menembus pintu kaca."
        nar "Di sudut ruang tunggu yang menghadap ke taman, Saionji Shiori duduk anggun mengenakan yukata penginapan berwarna biru tua bermotif bunga halus. Rambut putih keperakannya yang panjang jatuh bergelombang melewati bahu saat ia menata barisan bidak kayu di atas papan catur klasik milik ryokan."
        nar "Begitu langkah sandalmu berhenti di dekat meja rendah itu, Shiori mengangkat wajah dan menatapmu dengan mata ungu amethyst serta senyum tipis yang tenang."
        if any(c["ev"] == "S01" and c["key"] == "A" for c in choices_log):
            shiori "Selamat malam, Amamiya-san. Kebetulan sekali—kali ini juga mau duduk di seberangku?"
        else:
            shiori "Selamat malam, Amamiya-san. Kebetulan papan catur di lobi ini sedang kosong. Kamu mau bermain satu babak?"
        nar "Ia meraih gelas teh hangat miliknya dan memindahkannya ke meja samping yang cukup jauh dari papan agar tidak tersenggol, lalu menautkan jari-jarinya dengan rapi di pangkuan."
        shiori "Lobi malam ini jauh lebih sunyi daripada taman waktu Hanami. Kamu mau permainan singkat sekadar mengisi waktu sebelum tidur, atau membiarkannya berlangsung penuh sampai selesai?"
        nar "Sorot matanya yang tenang terasa berbeda dari sekadar ajakan sopan—malam ini ia jelas punya cukup waktu luang untuk benar-benar ingin melihat bagaimana caramu berpikir."
    call kk_family_menu("S02", ["\"Ayo main penuh saja sampai selesai.\"", "Bermain santai dan biarkan dia mengambil bidak pentingmu.", "Fokus penuh dan incar celah untuk menang."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau duduk bersila di bantal duduk seberang meja rendah, lalu menatap barisan bidak putih di hadapanmu dengan tatapan mantap."
            chiasa "Ayo main penuh saja, Saionji-senpai. Tanggung kalau cuma setengah jalan."
            shiori "Bagus. Jawaban seperti itu yang paling kusuka—aku ingin melihat langkahmu sendiri tanpa dipotong waktu."
            nar "Permainan dimulai dengan tempo yang pelan namun rapat. Setiap kali kau menggerakkan satu bidak, Shiori tidak pernah membalas secara asal; ia membaca arah tekananmu, menutup jalur tengah, lalu melempar jebakan kecil di sayap kanan yang memaksamu berpikir dua langkah lebih jauh."
            nar "Di pertengahan babak, kau mengambil satu keputusan berisiko dengan menukar kuda milikmu demi membuka garis serangan menteri. Alis perak Shiori terangkat tipis—pertandingan berlanjut sengit hingga akhirnya berakhir setelah lebih dari empat puluh langkah."
            nar "Begitu raja tumbang dan permainan selesai, Shiori tidak langsung merapikan papan. Ia menunjuk satu petak di tengah yang tadi sempat kaulepas."
            shiori "Amamiya-san, tadi di giliran kedua belas—mengapa kamu memilih mengorbankan kuda di petak ini padahal pertahanan kirimu masih bisa ditutup pion?"
            chiasa "Soalnya kalau kututup pakai pion, pergerakanku langsung terkunci sampai akhir. Lebih baik kupaksa papan terbuka sekalian meskipun berisiko."
            nar "Shiori menatap petak itu selama beberapa detik, lalu tersenyum pelan dengan binar puas yang jujur di matanya."
            shiori "...Menarik sekali. Aku tadi mengira sudah cukup memahami pola bermainmu, ternyata kamu lebih memilih ruang bergerak daripada keamanan semu. Jawabanmu barusan mengubah caraku membaca lawan malam ini."
            nar "Ia mengangkat gelas tehnya dan menyesap pelan, jelas menghargai keseriusanmu sepanjang babak."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kau duduk di seberangnya dan memulai permainan, tetapi di pertengahan babak kau memilih tidak mempersulit suasana. Ketika menterimu sebenarnya bisa ditarik mundur ke petak aman, kau justru menggerakkan pion pinggir yang tidak penting dan membiarkan bidak berharga itu terbuka lebar di jalur serangannya."
            nar "Tangan Shiori sempat terangkat di atas papan—lalu berhenti mendadak di udara. Ia tidak mengambil menterimu."
            nar "Ia menarik tangannya kembali ke pangkuan, lalu menatapmu lurus-lurus dengan mata ungu amethyst yang mendadak kehilangan kehangatan sopannya."
            shiori "Amamiya-san. Kamu melihat jalur aman di petak sebelah kiri tadi, bukan? Jangan mengalah padaku."
            nar "Suaranya tetap rendah dan halus, namun ketajamannya langsung membuat suhu di lobi terasa turun beberapa derajat."
            chiasa "Ah... aku cuma pikir ini kan malam liburan, jadi tidak perlu dibuat terlalu tegang—"
            shiori "Apakah aku pernah mengatakan bahwa aku tidak sanggup kalah, atau bahwa aku membutuhkan kemenangan yang dibungkus rasa kasihan?"
            nar "Shiori mengembalikan satu bidaknya sendiri ke kotak kayu dengan bunyi pelan yang terasa jauh lebih dingin daripada kemarahan yang meledak-ledak."
            shiori "Kalau kamu tidak ingin bermain sungguhan, menolak sejak awal jauh lebih sopan daripada berpura-pura kalah demi menyenangkanku. Keramahan yang mengabaikan keinginan lawan bicara hanya terasa meremehkan."
            chiasa "...Maaf, Saionji-senpai. Itu memang salahku."
            nar "Ia mengangguk singkat dengan senyum tipis yang kini sepenuhnya tertutup seperti dinding kaca, lalu menutup papan catur itu sebelum permainan selesai."
    else:
        if kk_host == "chiasa":
            nar "Kau duduk di seberang meja rendah dan langsung memusatkan seluruh perhatianmu pada papan kayu. Tidak ada alasan untuk menahan diri; jika ia memang ingin melihat cara pikirmu, kau akan memberinya pertandingan yang paling tajam yang sanggup kauberikan."
            nar "Sepanjang dua puluh menit penuh, hanya bunyi 'klak' bidak kayu dan detak samar pancuran bambu di luar yang terdengar di lobi. Shiori membangun tekanan sistematis di sisi kanan, memaksamu bertahan rapat—sampai kau melihat satu celah kecil yang ia tinggalkan di baris belakang demi mempercepat serangannya."
            nar "Kau mendorong bentengmu menembus garis belakang, mengunci posisi rajanya dalam dua langkah tak terelakkan."
            chiasa "Skakmat, Saionji-senpai."
            nar "Shiori menatap papan selama tiga detik penuh. Tidak ada raut kesal, tidak ada alasan, dan tidak ada senyum palsu. Bibirnya justru melengkung naik menjadi senyum percaya diri yang tajam dan sangat hidup."
            shiori "Luar biasa. Kamu melihat celah di baris belakangku satu giliran lebih cepat daripada perkiraanku."
            nar "Tanpa sedikit pun ragu, kedua tangannya langsung bergerak cekatan mengumpulkan seluruh bidak dan menyusunnya kembali ke garis awal sebelum teh di gelas kalian sempat dingin."
            shiori "Aku mengaku kalah untuk babak ini, Amamiya-san. Bagaimana—mau satu babak lagi? Kali ini aku tidak akan membiarkan baris belakangku terbuka semudah itu."
            chiasa "Boleh saja, Senpai. Aku masih belum mengantuk."
            nar "Di lobi yang tenang itu, pujian paling tulus yang bisa keluar dari seorang Saionji Shiori malam ini hadir dalam bentuk bidak-bidak kayu yang langsung ia susun ulang untuk menantangmu lagi."
```

## 3. `N02` — *Rematch Malam Onsen*
```renpy
label kkscene_N02:
    call kk_scene_enter("nagisa", "Ruang bersama ryokan · Malam")
    if kk_host == "chiasa":
        nar "Lewat pukul sepuluh malam, ruang bersama ryokan yang berkarpet tatami mulai sepi karena sebagian besar rombongan sudah kembali ke kamar masing-masing setelah berendam di onsen. Hanya cahaya layar televisi di sudut ruangan yang masih menyala terang."
        nar "Di depan layar itu, Sakurajima Nagisa duduk bersila mengenakan yukata penginapan, rambut pirang keemasannya yang biasanya diikat twin-tail kini masih agak lembap sehabis mandi dan diikat longgar di kiri-kanan. Dua stik pengendali konsol portabel yang disambungkan ke televisi tergeletak di antara kalian—dan di layar baru saja muncul tulisan 'GAME OVER' untuk kesekian kalinya."
        nar "Nagisa mengerutkan kening menatap layar sambil menekan tombol ulang dengan suara cepat, lalu mengoceh panjang lebar membedah kekalahannya sendiri memakai istilah frame, jeda serangan, dan arah menghindar."
        nagisa "Tunggu, tunggu! Barusan itu aku sudah pencet tangkis duluan, tapi jeda animasi seranganku belum selesai sepersekian detik! Jadi secara teknis aku nggak salah baca—cuma telat mencet tombolnya saja!"
        nar "Ketika kau hendak menguap pelan dan melirik jam dinding, Nagisa langsung menyambar lengan bajumu pelan sambil menyodorkan kembali stik pengendali ke pangkuanmu."
        nagisa "Hei, Chiasa, jangan tidur dulu! Aku baru saja paham timing tombol yang tadi. Kalau berhenti sekarang, besok pagi tanganku pasti lupa lagi—satu ronde lagi saja, ayo!"
    call kk_family_menu("N02", ["Ambil stiknya dan main dengan serius.", "Perlambat permainanmu supaya dia kebagian menang.", "\"Daripada terus beradu, mau coba main satu tim saja?\""])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau menerima stik pengendali itu, duduk kembali tegak di atas bantal tatami, dan memutuskan tidak menahan satu pun gerakanmu. Jika ia memang ingin mengukur batasnya sendiri, maka kau akan melawannya dengan sungguh-sungguh."
            chiasa "Oke, satu ronde lagi, Nagisa-senpai. Tapi aku main serius seperti tadi, ya."
            nagisa "Memang harus begitu! Awas kalau kau main-main!"
            nar "Pertandingan berlangsung cepat dan sengit. Ibu jari Nagisa bergerak heboh di atas tombol sambil sesekali memekik tertahan tiap kali serangannya hampir masuk. Kali ini bar darah karaktermu benar-benar terkuras hingga tersisa tipis—sebelum kau membaca lompatan terakhirnya dan menutup ronde dengan kemenangan tipis."
            nar "Nagisa mengembuskan napas keras lalu menjatuhkan punggungnya sedikit, tetapi alih-alih marah, matanya justru langsung menatap layar tayangan ulang dengan penuh semangat."
            nagisa "Hah... kalah lagi! Tapi jangan senyum dulu, Chiasa! Lihat bar darahmu barusan—aku makin dekat! Dan yang bikin aku kena tadi bukan kesalahan yang sama kayak ronde sebelumnya, kan?!"
            chiasa "Iya, tangkisanmu di tengah ronde tadi jauh lebih cepat daripada sebelumnya."
            nagisa "Tuh kan! Sebentar, minum dulu sana kalau tanganmu pegal—habis ini ronde penentuan!"
            nar "Ia menyodorkan botol minuman dingin di dekat meja kepadamu sambil menunggu dengan tidak sabar. Nada tantangannya masih sama kerasnya, tetapi sorot matanya kini jauh lebih lepas—ia tahu kau menghadapinya sebagai lawan sungguhan."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Melihatnya sudah kalah berkali-kali padahal matanya masih menyala penuh ambisi, kau mengambil stik dan memutuskan mengendurkan sedikit tempomu. Di detik-detik terakhir ronde, ketika karakter Nagisa terbuka lebar untuk serangan balasan yang mudah, kau sengaja menahan ibu jarimu sepersekian detik dan membiarkan serangannya masuk duluan."
            nar "Tulisan 'PLAYER 2 WINS' menyala terang di layar televisi."
            nagisa "YES! Akhirnya menang juga—!"
            nar "Nagisa langsung mengangkat kedua tangannya tinggi-tinggi dengan senyum lebar—namun gerakannya mendadak berhenti di udara. Senyumnya perlahan luruh saat ia menatap tayangan ulang di layar dan mengingat kembali detik terakhir gerakan karaktermu."
            nar "Ia menurunkan kedua tangannya perlahan, lalu menoleh menatapmu dengan mata biru yang meredup kesal."
            nagisa "...Chiasa. Tadi karaktermu jelas-jelas bisa langsung menyerang balik waktu aku melompat. Kenapa kau tiba-tiba berhenti pencet tombol?"
            chiasa "Eh... jariku tadi agak telat saja—"
            nagisa "Jangan bohong. Dari tiga ronde sebelumnya kau nggak pernah telat di gerakan semudah itu."
            nar "Kemenangan di layar televisi mendadak terasa hambar dan tidak berarti. Nagisa meletakkan stiknya ke atas meja rendah dengan bunyi agak keras, lalu membuang muka ke samping—jelas jauh lebih kesal karena mengira kau merasa perlu melindunginya dari hal sekecil kekalahan dalam permainan."
            nagisa "Sudahlah, aku capek. Aku balik ke kamar duluan."
    else:
        if kk_host == "chiasa":
            nar "Alih-alih langsung menekan tombol tanding ulang satu lawan satu, kau menggeser menu di layar televisi ke mode kerja sama dua pemain melawan musuh komputer."
            chiasa "Daripada terus saling sikut satu lawan satu, mau coba main satu tim melawan bos tahap akhir saja, Nagisa-senpai?"
            nar "Nagisa langsung menyipitkan kedua matanya ke arahmu, mencoba menakar apakah tawaranmu itu cuma alasan halus supaya kau tidak perlu melawannya lagi. Setelah dua detik menimbang, ia mendengus kecil lalu menggeser bantal duduknya merapat ke sebelahmu."
            nagisa "Boleh juga. Tapi aku pegang sisi kiri dan garis depan! Dan dengar ya, Chiasa—kalau nanti aku teriak-teriak pas main, itu artinya aku ngasih informasi, bukan lagi marah!"
            chiasa "Siap, informasi diterima."
            nar "Begitu ronde kerja sama dimulai, ruang bersama yang tadinya sunyi langsung dipenuhi suara tombol ditekan cepat dan teriakan panik Nagisa yang bercampur tawa."
            nagisa "Kanan! Awas dari kanan—eh, bagus! Tahan sebentar, aku isi tenaga dulu—waduh, kena juga!"
            nar "Meski kalian berdua tetap kalah sekali di fase terakhir bos karena salah hitung waktu menghindar, kali ini tidak ada wajah cemberut ataupun gengsi yang tegang. Nagisa langsung menekan tombol ulang sambil menoleh padamu dengan mata berbinar."
            nagisa "Tadi hampir banget! Ayo ulang sekali lagi—kali ini kita pasti menang!"
            nar "Kau mengangguk sambil ikut tertawa pelan. Untuk pertama kalinya malam ini, permintaan ulangnya tidak lagi memakai kata 'aku', melainkan 'kita'."
```

## 4. `Mi02` — *Kue Percobaan Ketiga*
```renpy
label kkscene_Mi02:
    call kk_scene_enter("miyuki", "Dapur ryokan")
    if kk_host == "chiasa":
        nar "Saat kau berjalan melewati lorong belakang ryokan untuk mengambil air minum malam, aroma manis mentega hangat dan vanila yang sedikit gosong tercium dari balik pintu dapur yang terbuka setengah."
        nar "Begitu melongok masuk, kau mendapati Tachibana Miyuki berdiri di depan meja saji mengenakan celemek putih di atas yukata tidurnya yang lengannya sudah diikat tali kain agar tidak kotor. Rambut hitam panjangnya diikat longgar ke belakang, dan di atas meja berjajar dua loyang kue hasil percobaan sebelumnya bersama mangkuk tepung."
        nar "Baru saja Miyuki membalik cetakan kue percobaan ketiga ke atas rak pendingin—dan tepat di depan mata kalian berdua, bagian tengah kue spons itu perlahan melesak turun membentuk cekungan yang agak menyedihkan."
        nar "Miyuki menatap kue itu dengan wajah serius yang begitu kontras, persis seperti seorang dokter yang baru saja melihat hasil percobaannya membantah seluruh teori terbaiknya."
        miyuki "Baiklah... bentuk memang bukan segalanya. Tapi kalau rasanya ikut melesak seperti bagian tengahnya, sepertinya Senpai perlu bicara serius dengan resep ini."
        nar "Ketika ia menoleh dan menyadari sosokmu berdiri di ambang pintu dapur, rona malu tipis langsung menyapu pipinya."
        miyuki "Ara, Chiasa-chan? Belum tidur ya? Maaf dapurnya jadi bau manis begini—tadi pengelola ryokan mengizinkan Senpai meminjam oven sebentar buat coba resep kue untuk sarapan besok, tapi... ya, hasilnya seperti yang kamu lihat."
        nar "Ia memotong sepotong kecil kue yang bentuknya miring itu, meletakkannya di piring keramik kecil bersama garpu, lalu menyodorkannya kepadamu dengan ekspresi sudah siap meminta maaf bahkan sebelum kau sempat mencicipinya."
        miyuki "Kalau Chiasa-chan tidak keberatan jadi juri dadakan... boleh bantu cicipi sedikit? Kalau tidak enak, langsung taruh saja ya."
    call kk_family_menu("Mi02", ["Habiskan seluruh potongan kue yang ia sajikan.", "\"Bagian tengahnya agak padat, tapi pinggirnya enak kok.\"", "Gulung lengan bajumu dan tawarkan bantuan memperbaiki adonannya."])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau menerima piring kecil itu, memotong satu gigitan dengan garpu, lalu mengunyahnya. Memang bagian tengahnya agak bantat dan terlalu padat, tetapi aroma mentega serta rasa manisnya sebenarnya masih sangat layak dimakan."
            nar "Tanpa banyak komentar, kau terus menyendok potongan kedua, ketiga, hingga piring kecil itu bersih tidak tersisa sedikit pun."
            chiasa "Habis. Rasanya tetap enak kok, Tachibana-senpai—manisnya pas buat camilan malam."
            nar "Miyuki mengerjap tak percaya melihat piring kosong di tanganmu, lalu tawa kaget yang lembut pecah dari bibirnya. Sebelum kau sempat melirik potongan berikutnya di rak pendingin, ia buru-buru mengambil garpu dari tanganmu sambil menggeleng geli."
            miyuki "Ara, tunggu dulu, Chiasa-chan! Satu gigitan buat penilaian itu sudah cukup—kamu tidak perlu memaksa menghabiskan semuanya cuma buat menghibur Senpai, nanti malah kekenyangan sebelum tidur."
            chiasa "Aku memang tidak memaksa, beneran enak."
            miyuki "Hehe... terima kasih banyak ya. Setidaknya sekarang Senpai tahu kegagalan percobaan ketiga ini masih punya satu penggemar setia."
            nar "Ia mengambil garpu bersih, mencicipi sedikit bagian tengah kuenya sendiri, lalu akhirnya ikut menertawakan bentuk cekung yang tadi membuatnya murung di depan oven."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kau mencicipi satu gigitan dari bagian pinggir lalu satu gigitan kecil dari bagian tengah yang cekung, mengunyah pelan sebelum menjawab dengan jujur."
            chiasa "Kalau boleh jujur, Tachibana-senpai—bagian pinggirnya lembut dan wangi menteganya enak sekali. Tapi bagian tengah yang turun ini memang agak terlalu padat, kayak kurang mengembang waktu di oven."
            nar "Miyuki tidak tampak tersinggung sedikit pun. Ia mengambil garpu bersih, memotong sedikit dari bagian pinggir dan bagian tengah yang baru kau tunjuk, lalu mencicipinya sambil mengangguk pelan tanpa senyum yang dipaksakan."
            miyuki "Hmm... benar juga. Persis seperti yang kurasakan tadi. Suhu oven ryokan ini sepertinya agak terlalu panas di awal, jadi luarnya matang duluan sementara tengahnya belum sempat naik."
            nar "Ia menghela napas lega sambil menatapmu dengan sorot mata biru sapphire yang hangat."
            miyuki "Terima kasih sudah jujur, Chiasa-chan. Lega rasanya kalau kamu nggak merasa harus bilang 'sempurna' cuma karena Senpai yang membuatnya."
            nar "Ia meraih pulpen dan buku resep kecilnya di sudut meja, menuliskan catatan penyesuaian suhu dan waktu panggang di pinggir halaman—kali ini tanpa mencoret seluruh percobaannya sebagai kegagalan total."
    else:
        if kk_host == "chiasa":
            nar "Kau meletakkan piring kecil itu setelah satu gigitan, lalu langsung mengikat ujung lengan yukata-mu ke belakang dan melangkah masuk ke sisi meja saji."
            chiasa "Kalau masih ada bahan buat percobaan keempat, bagi tugas saja yuk, Tachibana-senpai. Biar aku yang bantu mengocok adonan atau menakar tepungnya."
            nar "Mata Miyuki membulat pelan melihat kesigapanmu. Untuk beberapa detik ia hanya menatapmu, lalu bahunya turun lega dan ia menggeser posisinya di depan meja agar kalian berdua punya ruang yang sama lapangnya."
            miyuki "Ara... kamu serius mau menemani Senpai begadang sedikit di dapur? Baiklah—kalau begitu Chiasa-chan pegang mangkuk yang ini, ya."
            nar "Ia menyodorkan mangkuk kaca dan pengocok telur kepadamu sambil tersenyum jahil yang jarang sekali terlihat di kampus."
            miyuki "Lagipula, kalau percobaan keempat ini ternyata gagal lagi, kali ini kita bisa menyalahkan kerja sama tim. Senpai suka rencana ini."
            chiasa "Jangan langsung pesimis dulu, Senpai. Telurnya dikocok sampai kaku, kan?"
            miyuki "Iyaa~ pelan-pelan saja, jangan sampai pegal. Kalau Chiasa-chan capek, nanti gantian sama Senpai, oke?"
            nar "Nada suaranya mendadak melunak jadi jauh lebih manja dan santai—sisi hangat yang tidak pernah keluar ketika semua orang di kampus hanya datang mengandalkannya. Percobaan keempat mungkin belum tentu langsung sempurna, tetapi malam ini ia tidak lagi berdiri sendirian di depan oven."
```
