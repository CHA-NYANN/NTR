# Milestone Koita bergerbang-rute (K04, K05, K13, K17, K20, K21, K22). Pilihan
# yang membuka arah BL (Male) / Koita Success (Female) kini disambung sebagai
# POINTER-RUTE: menyetel bendera arah dengan teks terkendali, bukan adegan
# eksplisit. Cabang sabotase/manuver ditulis sebagai konsekuensi tanpa metode.
# Event vila dipetakan ke lokasi standar Koita demi reachability (🟡 prototipe).
# Efek: koita_curiga_1, trust/jeal, bendera rute. Mengikuti Event_Koita.

# ┌─ PANDUAN CERITA · K04 · Pertanyaan di Bawah Kembang Api
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : Koita bertanya, "Kalau kamu jadi aku, kamu akan memilih siapa?"
# │ INTI    : A jawab jujur / B bohong / C balik tanya / D sebut namamu sendiri.
# │ AKHIRAN : A menambah Trust; B menambah risiko bila ketahuan; D menyalakan jalur BL (Male) atau Koita Success (Female).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K04:
    call kk_scene_enter("koita", "Gedung Sastra · Di bawah kembang api")
    play sound "audio/sfx/fireworks.wav"
    if kk_host == "chiasa":
        nar "Kilatan emas dan merah tua mekar di langit malam lebih dahulu daripada dentuman gemanya yang menggetarkan udara. Kalian berdua berdiri agak terpisah dari kerumunan utama di tepi pagar batu beranda Gedung Sastra yang agak tinggi, tempat riuh rendah stan festival mereda menjadi dengung samar di kejauhan."
        nar "Angin malam Agustus bertiup tipis membawa bau mesiu samar dan suara tawa pengunjung dari jalan setapak di bawah. Di sebelahmu, Amamiya Koita menengadah memandangi bunga api yang perlahan gugur menjadi percikan kecil di atas siluet atap gedung kampus."
        koita "Dari beranda sini kelihatan penuh banget ya langitnya, Chi-chan. Nggak usah berdesak-desakan sama kerumunan di bawah."
        chiasa "Iya, anginnya juga lebih sejuk di atas sini. Tanganmu sudah nggak pegal bawa kantong minuman tadi?"
        koita "Aman kok, sudah kutaruh di bangku belakang kita. Tadi kamu sempat kebagian es serut nggak waktu lewat stan bawah?"
        chiasa "Sempat, sudah habis sebelum naik tangga. Kembang api babak keduanya kayaknya bakal lebih besar dari yang tadi ya."
        koita "Biasanya memang begitu. Waktu kita kecil dulu, setiap kali babak kedua mulai, kamu selalu tutup telinga sebelah sambil tetap nggak mau kedip."
        chiasa "Itu kan waktu aku masih SD, Ko-nii."
        nar "Cahaya warna-warni kembali menerangi sisi wajahnya yang tenang, tetapi ketika jeda sunyi jatuh di antara dua ledakan besar dan ia akhirnya membuka suara lagi, pertanyaannya sama sekali tidak berkaitan dengan pemandangan di langit."
        koita "Chi-chan... kalau kamu jadi aku, di antara mereka semua, kamu akan memilih siapa?"
        chiasa "Eh? Tumben sekali Ko-nii tiba-tiba tanya begitu di tengah festival."
        nar "Kamu menoleh perlahan ke arahnya. Begitu mata kalian bertemu di bawah kilatan cahaya biru dari langit, Koita buru-buru mengeluarkan tawa pendek yang terdengar kaku."
        koita "Haha, aneh ya aku nanya begini ke adik sendiri. Aku tahu kok urusan perasaan kayak gini nggak seharusnya diserahkan ke orang lain. Cuma... beberapa bulan terakhir ini kamu kelihatan jauh lebih tenang dan lebih jeli melihat apa yang sebenarnya terjadi di sekitar kita daripada aku sendiri."
        chiasa "Ko-nii lagi kepikiran sesuatu dari obrolan anak-anak tadi sore?"
        koita "Dari beberapa minggu lalu sebenarnya... rasanya akhir-akhir ini aku makin sadar kalau aku nggak mungkin terus-terusan cuma tersenyum dan pura-pura nggak lihat."
        nar "Ia kembali menatap ke depan, kedua tangannya bertumpu pada pagar batu yang dingin. Di balik senyum kecilnya yang masih terpasang, tampak jelas kegamangan seseorang yang selama ini terlalu terbiasa menunda setiap keputusan penting."
    else:
        nar "Kilatan emas dan merah tua mekar di langit malam lebih dahulu daripada dentuman gemanya yang menggetarkan dada. Kalian berdua berdiri agak terpisah dari kerumunan utama di tepi pagar batu yang agak tinggi, tempat suara riuh stan festival mereda menjadi dengung samar di kejauhan."
        nar "Angin malam Agustus membawa bau samar asap kembang api dari arah sungai. Di sebelahmu, Amamiya Koita bersandar menengadah memandangi bunga api yang gugur pelan menjadi percikan perak di atas atap gedung kampus."
        koita "Enak juga ya lihat dari pagar atas sini, Yutaka. Nggak kena dorong-dorong pengunjung dari belakang."
        yutaka "Lebih leluasa lihat langitnya juga. Tadi di bawah terlalu banyak kepala sama layar ponsel."
        koita "Haha, benar juga. Tadi aku sempat beli teh dingin dua botol di dekat gerbang, satu lagi kutaruh di bangku belakang kalau kamu haus."
        yutaka "Makasih. Babak kedua kayaknya sebentar lagi naik tuh, lampion di tepi sungai mulai dimatikan sebagian."
        koita "Iya, kerumunan di bawah juga sudah mulai diam nunggu tembakan berikutnya."
        nar "Cahaya warna-warni menerangi wajahnya yang tenang, tetapi ketika jeda sunyi turun di antara dua ledakan dan ia akhirnya membuka suara lagi, pertanyaannya sama sekali tidak mengikuti apa yang sedang kalian lihat di langit."
        koita "Yutaka... kalau kamu jadi aku, kamu bakal memilih siapa?"
        yutaka "Pertanyaan macam apa itu tiba-tiba di tengah kembang api, Koita?"
        nar "Kamu menoleh pelan ke arahnya. Begitu tatapan kalian bertemu di bawah kilatan cahaya biru dari langit, Koita buru-buru mengeluarkan tawa pendek yang terdengar agak gugup."
        koita "Haha, aneh banget ya aku nanya begini ke sahabat sendiri. Aku tahu kok hal kayak gini nggak bisa diserahkan ke orang lain. Cuma... akhir-akhir ini kamu kelihatan jauh lebih tenang dan lebih paham apa yang sebenarnya terjadi di sekitar kita daripada aku."
        yutaka "Kamu lagi kepikiran sesuatu sejak acara tadi sore?"
        koita "Dari beberapa minggu lalu sebenarnya... rasanya makin lama makin susah buat pura-pura semuanya cuma pertemanan biasa saja."
        yutaka "Memangnya ada yang mendesakmu buat langsung memilih malam ini?"
        koita "Nggak ada yang maksa secara langsung sih... tapi lihat saja malam ini di bawah. Setiap kali aku ngobrol agak lama sama satu orang, aku selalu sadar ada pandangan lain yang ikut memperhatikan dari pinggir."
        nar "Ia kembali menatap ke depan, kedua tangannya bertumpu di pagar batu yang dingin. Di balik senyum kecilnya yang masih terpasang, terlihat keraguan nyata dari seseorang yang selama ini terlalu terbiasa menunda setiap pilihan."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["\"Kalau jujur menurutku, pilih yang paling tulus sama kamu.\"", "Sebut nama yang bukan pendapatmu sebenarnya.", "\"Tunggu, kamu sendiri sebenarnya penginnya siapa?\"", "\"Bagaimana kalau aku?\""])]
    call screen kk_choice_panel(_rows, "Di bawah kembang api")
    $ kk_record_choice("K04", _return)
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu menatap langit malam sebentar sebelum menjawab dengan jujur, tidak berusaha menyenangkan telinganya dengan jawaban yang samar."
            chiasa "Kalau kamu tanya pendapat jujurku, Ko-nii... pilih orang yang selama ini paling tulus merhatiin kamu tanpa minta balasan aneh-aneh, dan yang paling berani jujur soal dirinya sendiri meskipun kadang canggung, kayak Nagisa-senpai atau Kujo-senpai. Tapi siapa pun yang kamu pilih nanti, kamu harus sadar satu hal."
            koita "Sadar soal apa, Chi-chan?"
            chiasa "Hubungan yang beneran itu nggak bakal selalu mulus dan nyaman kayak waktu kalian masih cuma berteman ramai-ramai. Begitu kamu pilih satu orang, kamu harus belajar berhenti bersikap manis yang sama ke gadis-gadis lain, dan berhenti lari setiap kali ada pembicaraan yang nggak enak."
            koita "Maksudmu... aku selama ini terlalu sering lari dari pembicaraan kayak begitu ya?"
            chiasa "Kamu sendiri tahu jawabannya kan, Ko-nii. Setiap kali suasana mulai agak tegang sedikit, kamu langsung melempar candaan atau nawarin sesuatu biar semuanya kembali tersenyum."
            nar "Koita mendengarkan dari awal sampai akhir tanpa menyela, dan tanpa buru-buru membela diri seperti kebiasaannya di rumah."
            koita "...Aku tadinya mengira kamu bakal menunjuk pilihan yang paling gampang dan paling nggak bikin ribut buatku, Chi-chan. Ternyata kamu beneran memikirkan perasaan orang yang kupilih itu juga."
            chiasa "Kalau Ko-nii cuma cari yang paling gampang dan paling sabar ngalah sama kamu, ujung-ujungnya kamu malah bakal nyakitin semuanya, termasuk orang yang kamu pilih."
            koita "Iya... setiap kali aku membiarkan semuanya tetap samar karena takut ada yang kecewa, sebenarnya aku cuma menumpuk kekecewaan yang lebih besar di belakang, ya."
            chiasa "Setidaknya sekarang Ko-nii mulai melihat bagian itu."
            nar "Ia mengangguk pelan lalu kembali menengadah saat kembang api berwarna perak mekar lebar di langit malam, menyinari matanya yang tampak lebih teguh daripada semenit lalu."
            koita "Terima kasih sudah jawab serius, Chi-chan. Aku bakal renungkan baik-baik omonganmu barusan. Tenang saja, kalau nanti aku gagal menjalaninya, aku nggak bakal lempar tanggung jawab dan nyalahin saranmu. Ini tetap keputusanku sendiri."
            chiasa "Memang harus begitu. Jangan bikin orang menunggu terlalu lama kalau kamu sudah tahu jawabannya."
            koita "Iya. Aku janji nggak bakal terus lari."
            nar "Kalian berdua kembali berdiri berdampingan memandangi sisa percikan perak yang gugur di langit gelap, membawa keheningan yang kali ini jauh lebih jujur daripada sebelumnya."
        else:
            nar "Kamu menatap langit malam sebentar sebelum menjawab dengan nada lugas yang jujur, tanpa memberi celah baginya untuk terus bermain aman."
            yutaka "Kalau kamu minta pendapat jujurku, Koita, pilih orang yang selama ini paling tulus berdiri di dekatmu dan nggak pernah main tebak-tebakan palsu, entah itu Nagisa yang sudah dari dulu nungguin kamu atau Kujo-san yang selalu jujur. Tapi siapa pun satu nama yang kamu ambil, kamu harus siap bayar harganya."
            koita "Bayar harganya gimana maksudmu, Yutaka?"
            yutaka "Begitu kamu memilih satu orang, kamu nggak bisa lagi bagi-bagi perhatian setengah-setengah ke yang lain supaya semuanya tetap suka sama kamu. Hubungan yang nyata itu bakal menuntut kamu buat tegas pasang batas, meskipun itu bikin suasana geng kita nggak senyaman dulu lagi."
            koita "Kamu ngerasa selama ini aku terlalu pengecut buat pasang batas ya?"
            yutaka "Bukan cuma ngerasa, aku lihat sendiri dari dulu. Tiap kali ada yang mulai serius sedikit, kamu langsung bagi senyum rata ke semua orang biar suasana balik aman."
            nar "Koita mendengarkan tanpa menyela sepatah kata pun, dan kali ini ia tidak berusaha meringankan suasana dengan lelucon."
            koita "...Aku pikir kamu bakal nyaranin orang yang paling gampang diajak kompromi buatku, Yutaka. Ternyata kamu beneran menimbang perasaan mereka juga."
            yutaka "Kalau kamu cuma cari yang paling gampang dan nggak banyak nuntut, ujung-ujungnya kamu bakal nyakitin orang yang kamu pilih sekaligus orang-orang yang kamu gantung."
            koita "Benar juga... aku selama ini mengira nggak memilih itu cara paling baik biar nggak ada yang terluka, padahal justru sebaliknya ya."
            yutaka "Bagus kalau kamu sadar sendiri."
            nar "Ia mengangguk pelan lalu kembali memandang langit saat kembang api perak mekar lebar di atas sana."
            koita "Makasih sudah ngomong apa adanya, Yutaka. Aku bakal pikirkan baik-baik. Tenang saja, aku tanya tadi bukan buat cari kambing hitam kalau nanti pilihanku salah. Itu tetap tanggung jawabku sendiri."
            yutaka "Jangan tunda terus sampai semuanya keburu muak menunggu."
            koita "Iya, aku mengerti."
            nar "Kalian tetap berdiri di tepi pagar batu memandangi rentetan kembang api berikutnya, sementara percakapan barusan meninggalkan bobot yang jelas belum selesai di pikiran Koita."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Alih-alih memberikan penilaianmu yang sesungguhnya, kamu sengaja melontarkan satu arah yang berlawanan dengan apa yang menurutmu paling baik untuknya, sebuah saran yang terdengar meyakinkan di permukaan padahal kamu tahu akan menggeser langkahnya ke jalur yang rapuh."
            chiasa "Kalau menurutku sih, Ko-nii paling cocok sama orang yang dari luar kelihatan paling dewasa dan nggak bakal pernah menuntut waktu Ko-nii macam-macam, kayak Tachibana-senpai. Sama dia, Ko-nii kan nggak perlu repot mengubah kebiasaan Ko-nii sedikit pun."
            nar "Koita tidak menertawakan saran itu ataupun mencurigai ada maksud lain di balik ucapanmu. Sebaliknya, ia memutar tubuhnya menghadapmu penuh dengan raut sangat serius."
            koita "Oh... kamu beneran mikir begitu, Chi-chan? Menurutmu kenapa kami berdua bisa cocok?"
            chiasa "Soalnya kalian berdua sama-sama nggak suka suasana yang penuh perdebatan. Dia selalu tenang dan pengertian, jadi Ko-nii nggak bakal pernah ditekan buat buru-buru ambil sikap."
            koita "Tapi... bukannya kadang dia justru kelihatan terlalu memendam semuanya sendiri ya? Aku kadang takut malah nambah beban di kepalanya kalau aku nggak cukup peka."
            chiasa "Justru karena sama-sama menjaga ketenangan itu kalian nggak bakal saling membebani, Ko-nii. Orang setenang dia pasti lebih nyaman sama seseorang yang selalu lembut dan nggak ribut kayak kamu. Hubungan kayak gitu kan yang paling jarang ada dramanya."
            koita "Begitu ya... kalau kupikir-pikir, setiap kali ngobrol sama Miyuki-senpai, aku memang jarang merasa gugup seperti waktu berhadapan sama yang lain. Senyumnya selalu bikin tenang."
            chiasa "Nah, kan. Itu tandanya ritme kalian memang paling sejalan. Lagipula kalau Ko-nii yang mendekat duluan dengan pelan-pelan, dia pasti nggak bakal menolak."
            koita "Hmm... padahal tadi aku sempat mikir dia terlalu tinggi buat kugapai sebagai senior teladan."
            chiasa "Cuma karena selama ini Ko-nii belum pernah benar-benar melangkah ke arahnya saja."
            nar "Koita terdiam beberapa detik, meresapi setiap alasan tambahan yang kamu rangkai dengan begitu mulus di bawah suara dentuman kembang api."
            koita "...Aku sama sekali nggak pernah melihatnya dari sudut pandang itu. Selama ini aku selalu mikir aku bakal bikin dia repot, tapi kalau kamu yang bilang begitu, rasanya masuk akal sekali. Makasih ya, Chi-chan."
            chiasa "Sama-sama, Ko-nii."
            nar "Melihat betapa bulat ia menelan saranmu, kamu menyadari bahwa dorongan kecil barusan tidak akan berhenti di pagar batu ini. Ada kemungkinan nyata ia akan melangkah mendekati seseorang dengan keyakinan keliru yang baru saja kamu tanamkan di kepalanya."
        else:
            nar "Alih-alih memberikan pendapatmu yang sebenarnya, kamu sengaja mengarahkan pandangannya pada pilihan yang kamu tahu tidak akan menyelesaikan sifat ragu-ragunya, walaupun terdengar sangat nyaman di telinganya."
            yutaka "Kalau aku jadi kamu sih, aku bakal pilih orang yang dari awal kelihatan paling dewasa, tenang, dan nggak bakal pernah ngajak kamu ribut soal hal sepele, kayak Tachibana-senpai. Sama orang setenang dia, hidupmu nggak bakal banyak tekanan."
            nar "Koita tidak mencurigai arah kalimatmu sedikit pun. Ia justru memutar badannya menghadapmu penuh dan menatapmu dengan keseriusan yang jarang ia tunjukkan."
            koita "Serius kamu mikir begitu, Yutaka? Dari mata kamu, kenapa menurutmu aku paling cocok ke arah sana?"
            yutaka "Soalnya kalau dilihat dari luar, ritme kalian berdua itu paling nggak pernah bentrok. Kamu nggak perlu capek-capek menebak suasana hatinya atau takut dimarahi kalau lagi sibuk sendiri."
            koita "Tapi... bukannya selama ini dia kelihatan terlalu sempurna buatku ya? Kadang aku ngerasa dia selalu pasang jarak sebagai senior, dan aku nggak mau malah bikin dia repot."
            yutaka "Itu kan cuma karena kamu belum pernah maju duluan secara khusus. Orang yang kelihatan selalu tenang di kampus justru paling gampang luluh kalau kamu kasih perhatian yang konsisten tanpa banyak drama."
            koita "Hmm... padahal selama ini aku selalu merasa nggak enak kalau mau ngajak Miyuki-senpai bicara lebih lama karena takut mengganggu jadwal belajarnya."
            yutaka "Justru karena dia sibuk, dia paling butuh orang yang nggak banyak menuntut kayak kamu. Kamu tinggal jaga ritme perhatianmu yang biasa saja."
            koita "Masuk akal banget kalau dilihat dari sisi itu..."
            nar "Koita mengangguk perlahan, mencerna alasan demi alasan yang kamu susun dengan nada meyakinkan seorang sahabat dekat di bawah gema kembang api."
            koita "...Aku nggak pernah kepikiran dari sudut pandang itu, Yutaka. Pantas saja selama ini aku bingung sendiri menimbang semuanya. Makasih sudah kasih pandangan lain."
            yutaka "Santai saja."
            nar "Kepercayaannya yang begitu utuh pada ucapanmu membuat kebohongan itu punya bobot yang nyata. Kini bukan mustahil ia akan melangkah menghampiri seseorang dengan keberanian yang baru saja kamu belokkan ke arah yang keliru."
    elif _return == "C":
        if kk_host == "chiasa":
            nar "Kamu tidak memberinya satu nama pun untuk dijadikan pegangan. Kamu menoleh penuh ke arahnya dan mengembalikan pertanyaan itu tepat ke hadapannya."
            chiasa "Kenapa malah lempar pertanyaannya ke aku, Ko-nii? Yang bakal menjalani hubungannya kan kamu sendiri. Sebenarnya di dalam hati, siapa yang paling kamu inginkan?"
            nar "Mulut Koita sempat terbuka hendak melontarkan jawaban ringan seperti biasa, tetapi kalimat pengelakan yang lazim ia pakai mendadak tertahan di kerongkongannya. Ia menutup mulutnya kembali dan menunduk menatap kedua tangannya yang bertumpu di pagar batu."
            koita "...Kalau boleh jujur, aku cuma pengin nggak kehilangan siapa-siapa di sekitar kita. Tapi itu jelas bukan jawaban untuk pertanyaanmu barusan, ya."
            chiasa "Bukan, Ko-nii. Itu cuma cara lain buat bilang kamu nggak mau memilih."
            koita "Aku tahu... setiap kali aku mencoba membayangkan cuma ada satu orang di sampingku sementara yang lain perlahan menjauh, dadaku langsung terasa sempit."
            nar "Ledakan kembang api berikutnya bergema keras di kejauhan, membuat kalian berdua terdiam selama beberapa detik sementara cahaya kuning keemasan menyapu sisi wajahnya."
            koita "Sebenarnya... ada satu orang yang bahkan nggak pernah berani kumasukkan ke dalam daftar kemungkinan di kepalaku, Chi-chan."
            chiasa "Kenapa nggak berani dimasukin ke daftar kemungkinan?"
            koita "Mungkin karena aku terlalu takut. Kalau aku mulai memikirkan orang itu secara serius... seluruh hubungan dan kenyamanan yang sudah ada selama bertahun-tahun ini bakal berubah total, dan nggak akan pernah bisa balik kayak semula lagi kalau aku salah langkah."
            chiasa "Jadi lebih mudah buat Ko-nii pura-pura nggak ada apa-apa di sana daripada mengambil risiko?"
            koita "...Iya. Kedengarannya pengecut banget ya kalau diucapkan keras-keras begini."
            chiasa "Setidaknya malam ini kamu berhenti pura-pura nggak tahu kalau perasaan itu ada, Ko-nii."
            koita "Haha... entah kenapa ngobrol sama kamu belakangan ini selalu terasa kayak lagi berkaca. Aku nggak bisa sembunyi di balik senyum biasa lagi."
            nar "Ia tidak menyebutkan nama siapa yang ia maksud, tetapi nada suaranya yang rendah dan jujur menyisakan gema yang bertahan jauh lebih lama daripada suara kembang api di atas kepala kalian."
        else:
            nar "Kamu tidak memberinya satu nama pun. Kamu menoleh penuh ke arahnya, bersandar di pagar batu sambil membalikkan pertanyaan itu langsung kepadanya."
            yutaka "Kenapa malah tanya ke aku, Koita? Yang bakal menjalaninya kan kamu sendiri. Kalau tanpa mikirin pendapat orang lain, sebenarnya siapa yang paling kamu inginkan?"
            nar "Koita membuka mulut hendak melempar jawaban santai seperti biasanya, lalu menutupnya kembali ketika sadar alasan klise itu terdengar terlalu kosong malam ini. Ia menunduk menatap kedua telapak tangannya di atas pagar batu."
            koita "...Aku cuma ingin nggak ada satu pun dari kita yang menjauh atau hilang. Tapi itu bukan jawaban yang kamu minta, ya."
            yutaka "Jelas bukan. Itu namanya kamu cuma mau semuanya tetap jalan di tempat."
            koita "Susah dijelaskan, Yutaka... tiap kali aku membayangkan memilih satu orang terus melihat yang lain perlahan menjaga jarak, aku langsung nggak tega."
            nar "Ledakan kembang api berikutnya bergema keras di langit, membuat kalian berdua diam sejenak sementara cahaya keemasan menyapu wajahnya."
            koita "Sebenarnya... ada orang yang bahkan nggak pernah berani kumasukkan ke dalam daftar kemungkinan, Yutaka."
            yutaka "Kenapa nggak berani kamu hitung?"
            koita "Karena aku terlalu pengecut soal yang satu itu. Kalau aku mulai memikirkannya dengan serius... semua batas aman yang selama ini bikin kita bisa tertawa bareng tiap hari bakal berubah total, dan aku takut nggak siap kehilangan kedekatan yang sekarang."
            yutaka "Jadi kamu lebih milih mengunci pintu itu sebelum sempat dibuka?"
            koita "...Iya. Payah banget ya kedengarannya."
            yutaka "Minimal malam ini kamu berani ngaku sendiri di depan orang lain."
            koita "Haha... entah kenapa ngomong sama kamu malam ini rasanya susah sekali mau menghindar."
            nar "Ia tidak menyebutkan siapa sosok yang ada di kepalanya itu, tetapi pengakuan singkat tersebut tertinggal jauh lebih berat di udara malam daripada sisa asap kembang api di langit."
    else:
        if kk_host == "chiasa":
            nar "Kamu tidak mengalihkan pandangan sedikit pun dari wajahnya. Tepat ketika kilatan kembang api di langit mulai meredup menjadi asap tipis dan keheningan turun di sela dua tembakan, kamu menjawab dengan suara yang tenang, jernih, dan sama sekali tidak menyisakan ruang untuk dianggap sebagai gurauan."
            chiasa "Kalau aku jadi Ko-nii? Aku bakal memilih aku."
            nar "Koita langsung menoleh ke arahmu. Dalam sisa cahaya kemerahan yang memudar di langit, seluruh raut santai dan senyum refleks yang biasa melindungi wajahnya lenyap seketika."
            koita "...Memilih kamu?"
            chiasa "Iya. Aku bilang pilih aku, Ko-nii."
            nar "Ia tidak tertawa untuk menganggapnya candaan adik perempuan seperti waktu di meja makan rumah. Ia juga tidak langsung memanggilmu 'Chi-chan' untuk menarik kembali percakapan ini ke dalam batas aman saudara tiri."
            nar "Jarak beberapa puluh sentimeter di antara kalian di tepi pagar batu mendadak terasa begitu rapat. Koita menatap matamu lurus-lurus, sementara dadanya naik turun menarik napas yang terasa berat."
            koita "Tunggu... kamu nggak lagi ngeledek aku kayak biasanya, kan? Nggak lagi main-main buat bikin aku panik?"
            chiasa "Kelihatannya aku lagi bercanda, Ko-nii?"
            nar "Koita menelan ludah pelan, tangannya yang bertumpu di pagar batu sedikit mencengkeram pinggiran beton. Pandangannya turun sejenak lalu kembali mengangkat menatap matamu tanpa berkedip."
            koita "Aku... jujur kepalaku langsung kosong barusan. Semua kalimat yang biasanya gampang keluar buat mencairkan suasana mendadak hilang semua. Aku belum tahu harus menjawab apa malam ini. Tapi aku dengar jelas setiap kata yang kamu ucapkan."
            chiasa "Aku memang nggak minta Ko-nii kasih jawabannya malam ini kok. Kamu boleh pikirkan selama yang kamu butuh."
            koita "Iya... dan aku janji, setelah malam ini aku nggak akan pura-pura kamu nggak pernah mengatakannya. Aku nggak akan kabur pakai candaan adik-kakak lagi."
            chiasa "Kupegang janjimu itu."
            nar "Dentuman kembang api penutup mekar besar di langit atas, menghujani beranda dengan cahaya emas, dan tidak satu pun dari kalian berdua yang mengangkat pandangan dari satu sama lain. Garis batas lama yang selama ini memagari kalian baru saja bergeser secara permanen."
        else:
            nar "Kamu tidak memalingkan wajah dan tidak menyelipkan tawa sedikit pun. Tepat ketika kilatan kembang api di langit memudar menjadi asap tipis dan keheningan turun di antara kalian, kamu menoleh menatap Koita lurus-lurus dengan senyum tipis yang tenang."
            yutaka "Kalau aku jadi kamu? Pilih aku saja, Koita."
            nar "Koita langsung menoleh ke arahmu. Dalam cahaya kemerahan yang tersisa di langit, ekspresi santainya membeku selama satu detik, lalu ia langsung mendengus sambil tertawa pendek yang terdengar terlalu dipaksakan."
            koita "Haha... apaan sih, Yutaka? Nggak lucu banget bercandamu malam ini. Aku lagi nanya beneran soal cewek-cewek di sekitar kita lho, malah dijawab ngawur begitu."
            yutaka "Aku kelihatan lagi bercanda?"
            nar "Kamu bersandar lebih santai ke pagar batu sambil menggeser bahumu sedikit lebih dekat ke arahnya, mempertahankan tatapan gelap yang tenang tanpa sedikit pun berkedip. Tawa canggung Koita langsung mati di tenggorokan. Warna merah padam merambat cepat sampai ke ujung kedua telinganya, dan ia refleks mundur setengah langkah sambil memelototimu tajam."
            koita "Hei! Berhenti lihatin aku dengan muka datar begitu, merinding tahu nggak?! Kamu habis minum alkohol diam-diam di stan festival atau gimana sih?!"
            yutaka "Cuma minum teh dingin. Kenapa kamu langsung panik begitu? Tadi kan kamu sendiri yang tanya kalau aku jadi kamu bakal milih siapa."
            koita "Ya jelas aku kaget lah! Kita sama-sama cowok, Yutaka! Aku ini normal, aku suka cewek! Terus kamu sahabatku dari kecil, tempatku cerita kalau lagi pusing ngadepin urusan begini, masa tiba-tiba ngomong kalimat aneh kayak gitu sambil nyengir tipis begitu?!"
            nar "Suara Koita meninggi karena salah tingkah bercampur kesal dan sedikit rasa terkhianati. Ia sempat berbalik setengah badan seolah hendak melangkah pergi dari beranda itu, lalu kakinya tertahan sendiri ketika melihatmu sama sekali tidak mundur ataupun menarik ucapanmu."
            yutaka "Reaksimu waktu kaget selalu paling jujur ya, Koita. Sampai telinga merah semua begitu."
            koita "Siapa yang telinganya merah?! Ini gara-gara udara Agustus gerah tahu nggak! Jangan deket-deket, sana geser!"
            nar "Kamu menghormati batasnya dan tidak melangkah lebih dekat, tetapi senyum tenang di bibirmu sama sekali tidak goyah."
            yutaka "Santai saja, aku nggak nyuruh kamu langsung jawab malam ini kok. Aku juga nggak maksa kamu apa-apa. Cuma biar kamu tahu saja, kalau kamu capek muter-muter terus di antara mereka, aku ada di sini."
            koita "Tutup mulutmu! Dasar menyebalkan banget malam ini! Awas ya kalau besok kamu berani bahas-bahas kalimat ngawur barusan lagi!"
            yutaka "Tergantung kamu besok masih sanggup pura-pura lupa atau nggak."
            koita "Ck... dasar gila!"
            nar "Meski ucapannya galak dan bahunya menegang penuh, ia tetap tidak benar-benar pergi meninggalkan beranda. Koita membuang muka dengan kasar kembali menghadap langit malam, kedua tangannya mencengkeram pagar batu erat-erat dengan telinga yang masih merah menyala. Ledakan kembang api terakhir mekar besar di atas atap kampus, sementara kamu tetap berdiri diam di sampingnya memandangi profil wajahnya yang tegang dan kesal tanpa menengadah sedikit pun ke arah langit."
    return

# ┌─ PANDUAN CERITA · K05 · Malam di Dapur Vila
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : Koita membuat minuman untuk semua; ia memperhatikan siapa yang canggung.
# │ INTI    : A jelaskan situasi / B ancam ringan / C tertawakan / D alihkan perhatiannya.
# │ AKHIRAN : C/D menurunkan koita_curiga_1; A–B meningkatkannya.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K05:
    call kk_scene_enter("koita", "Rumah Amamiya · Dapur vila malam")
    if kk_host == "chiasa":
        nar "Dari ruang tengah vila masih terdengar suara acara televisi larut malam dan tawa rombongan yang belum ingin naik ke kamar. Begitu kamu menggeser pintu kayu dan melangkah masuk ke dapur untuk mengambil air minum, udara terasa jauh lebih tenang. Hanya dengung ketel listrik yang baru selesai mendidih mengisi ruangan di bawah sorot lampu gantung berwarna kuning hangat."
        nar "Koita berdiri membelakangimu di depan meja konter. Di hadapannya berjajar tujuh cangkir keramik di atas nampan kayu besar. Sendok teh di tangannya bergerak terampil dari satu cangkir ke cangkir berikutnya, menakar satu sendok gula penuh, setengah sendok, teh tawar tanpa gula, lalu tambahan susu hangat. Ia meracik seluruhnya di luar kepala tanpa perlu kembali menanyakan pesanan ke ruang depan."
        chiasa "Rajin sekali malam-malam bikin minuman hangat buat satu vila, Ko-nii. Padahal dari siang tadi kamu yang paling banyak mondar-mandir."
        koita "Ah, Chi-chan. Mau ambil air dingin atau sekalian kubuatkan teh susu hangat juga? Air panasnya baru saja matang."
        chiasa "Teh susu hangat boleh deh, satu cangkir kecil aja. Tapi itu cangkirnya kok sampai tujuh? Memangnya semua masih bangun di ruang tengah?"
        koita "Masih. Tadi barusan aku sempat melongok sebentar buat hitung berapa orang yang belum naik ke lantai atas."
        nar "Koita tidak langsung menoleh. Tepat pada detik itu, dari balik pintu geser ruang tengah, suara tawa teman-teman kembali terdengar ramai. Padahal lima menit sebelumnya, sewaktu Koita sempat membuka pintu ruang tengah itu, seluruh percakapan di dalam mendadak berhenti."
        koita "Lucu juga ya, Chi-chan. Tadi waktu aku buka pintu ruang tengah buat mengecek siapa saja yang belum tidur, mereka semua mendadak diam serentak."
        chiasa "Eh? Kebetulan saja kali, Ko-nii. Mungkin topik obrolannya memang baru saja selesai terus mereka lagi bingung mau bahas apa lagi."
        koita "Mungkin. Tapi waktu kamu yang masuk ke ruang tengah sepuluh menit sebelumnya, suasana di dalam langsung ramai lagi."
        chiasa "Ya wajar dong, tadi kan aku masuk bawa camilan kacang panggang dari teras. Begitu lihat mangkuknya penuh lagi, ya mereka langsung berebut."
        nar "Koita menekan tombol mati pada ketel listrik, lalu mulai menuangkan air panas perlahan ke cangkir pertama. Kepulan uap tipis naik di depan wajahnya. Gerakan tangannya tetap stabil dan teratur, tetapi garis bahunya tampak sedikit menegang."
        koita "Bukan cuma soal camilan tadi, Chi-chan. Waktu kita di tepi pantai sore tadi juga sempat begitu, dan kemarin waktu di kantin juga sama. Aku baru sadar ternyata ada bagian dari obrolan liburan ini yang sama sekali nggak kuikuti."
        chiasa "Ko-nii mikirnya terlalu jauh deh. Di depan tadi kami cuma ngobrolin hal-hal ringan kok, nggak ada rapat rahasia atau apa."
        nar "Koita berhenti menuang dan meletakkan kembali ketel listrik ke alas dudukannya. Kali ini ia memutar badan menghadapmu sepenuhnya. Senyum tipisnya masih bertahan di bibirnya, tetapi sorot matanya menatapmu jauh lebih lama dan lebih tajam daripada biasanya."
        koita "Sebenarnya aku nggak cuma mikirin soal ruang tengah barusan, Chi-chan. Sejak beberapa minggu terakhir ini, ada yang terasa beda sekali dari kamu."
        chiasa "Beda gimana maksudnya, Ko-nii?"
        koita "Cara kamu bicara, cara kamu merespons teman-teman kita, sampai cara matamu memperhatikan sekitar waktu orang lain sedang lengah. Rasanya aku kayak lagi bicara sama seseorang yang tahu lebih banyak daripada yang ia tunjukkan. Aku cuma belum tahu apa yang sebenarnya berubah."
    else:
        nar "Dari ruang tengah vila masih terdengar suara acara televisi larut malam dan tawa rombongan yang belum ingin beranjak tidur. Begitu kamu menggeser pintu kayu dan masuk ke ruang dapur untuk mengambil air dingin, suasananya terasa jauh lebih sunyi. Hanya dengung ketel listrik yang baru selesai mendidih terdengar di bawah lampu kuning di atas meja konter."
        nar "Koita berdiri membelakangimu, sibuk menata tujuh cangkir keramik di atas nampan kayu besar. Sendok kecil di tangannya bergerak cepat dari satu cangkir ke cangkir lainnya, menakar satu sendok gula, setengah sendok, tanpa gula, lalu susu hangat. Ia menghafal takaran semua orang di vila tanpa perlu bertanya lagi ke ruang depan."
        yutaka "Rajin amat bikin minuman hangat buat satu vila jam segini, Koita. Bukannya dari siang tadi kamu sudah capek nyetir?"
        koita "Eh, Yutaka. Mau air dingin atau sekalian kubuatkan kopi hitam? Airnya barusan banget mendidih."
        yutaka "Kopi hitam boleh, tapi jangan kebanyakan airnya. Itu cangkirnya tujuh biji berarti di ruang depan belum ada yang naik tidur ya?"
        koita "Belum. Lima menit lalu aku sempat melongok ke ruang tengah buat hitung berapa orang yang masih melek."
        nar "Koita tidak langsung menoleh. Tepat pada detik itu, dari balik pintu geser ruang tengah, suara tawa rombongan kembali terdengar hidup. Padahal beberapa menit lalu, sewaktu Koita membuka pintu ruang depan itu, obrolan di sana langsung terhenti seketika."
        koita "Aneh juga ya, Yutaka. Tadi waktu aku melongok ke ruang tengah, mereka mendadak diam semua."
        yutaka "Kebetulan saja itu. Mungkin topiknya memang baru selesai dibahas terus lagi jeda sebentar."
        koita "Bisa jadi. Tapi waktu kamu yang masuk ke sana lima menit sebelumnya, obrolannya langsung hidup lagi."
        yutaka "Kan tadi aku masuk bawa baki es batu sama sisa semangka potong dari kulkas. Ya jelas langsung pada heboh."
        nar "Koita mematikan sakelar ketel listrik, lalu mulai menuangkan air panas perlahan ke cangkir pertama. Uap tipis mengepul di depan wajahnya. Gerakannya tetap tenang dan rapi, sementara kedua bahunya terlihat sedikit kaku."
        koita "Nggak cuma malam ini, Yutaka. Waktu kita di pantai siang tadi, terus waktu kumpul di kampus minggu lalu juga rasanya beberapa kali begini. Aku baru sadar ternyata ada bagian dari obrolan liburan kali ini yang sama sekali nggak kuikuti."
        yutaka "Jangan kejauhan mikirnya, Koita. Di depan tadi cuma obrolan biasa kok, nggak ada yang disembunyikan."
        nar "Koita berhenti menuang dan meletakkan ketel itu kembali ke dudukannya. Kali ini ia menoleh penuh ke arahmu. Senyum ramahnya masih menempel, tetapi matanya mengamati wajahmu dengan tatapan menyelidik yang cukup lama."
        koita "Sebenarnya ini nggak cuma soal ruang tengah barusan, Yutaka. Dari beberapa minggu belakangan ini, ada yang berubah drastis dari kamu."
        yutaka "Berubah di bagian mananya?"
        koita "Cara kamu bicara, jedamu sebelum menjawab orang, sampai caramu memperhatikan teman-teman di geng kita. Dulu kamu nggak pernah seteliti ini mengamati tiap gerak-gerik orang lain. Aku cuma belum menemukan apa penyebabnya."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["\"Nggak ada yang aneh kok, aku cuma lagi mikirin banyak hal aja.\"", "\"Jangan terlalu jauh nebak-nebak hal yang nggak kamu tahu.\"", "\"Haha, serius kamu mikir aku berubah jadi orang lain?\"", "\"Sudahlah, bahas jadwal kita minggu depan aja yuk.\""])]
    call screen kk_choice_panel(_rows, "Percakapan di dapur")
    $ kk_record_choice("K05", _return)
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu berjalan mendekat ke meja konter dan menyandarkan punggung dengan tenang di tepi kayu. Kamu tahu betul, jika kamu tampak gugup atau menghindar sekarang, rasa ingin tahunya justru akan semakin membesar."
            chiasa "Nggak ada yang aneh kok, Ko-nii. Aku cuma lagi mikirin banyak hal aja akhir-akhir ini. Wajar kan kalau sikapku agak berubah sedikit?"
            koita "Mikirin banyak hal soal kuliah di fakultasmu?"
            chiasa "Iya lah. Aku kan sekarang sudah mahasiswi, masa mau ke mana-mana selalu mengekor di belakang kamu seperti waktu SMA. Di kampus aku juga mulai punya lingkar obrolan sendiri sama senior-senior yang lain, jadi wajar kalau caraku bawa diri ikut berubah."
            koita "Kalau soal kamu makin akrab sama mereka di kampus, aku ngerti kok, Chi-chan. Aku malah senang lihat kamu cepat beradaptasi."
            chiasa "Makanya, tadi di ruang tengah juga kami cuma bahas urusan tugas studio sama jadwal kegiatan kampus minggu depan. Kebetulan saja pas Ko-nii buka pintu, pembahasannya memang baru selesai."
            nar "Koita mengangguk pelan sambil meraih sendok kecil untuk mengaduk cangkir teh susu. Sekilas ia tampak menerima penjelasanmu, sebelum tiba-tiba gerakan sendoknya melambat dan ia kembali mengangkat wajah menatapmu."
            koita "Kalau begitu, gimana soal kemarin waktu kalian membicarakan rencana pergi akhir pekan depan di kantin? Tadi siang aku dengar sekilas Nagisa-chan menyinggung soal itu waktu di pantai."
            chiasa "Rencana akhir pekan depan? Oh, yang mampir ke toko alat gambar dekat stasiun itu ya?"
            koita "Waktu kita makan malam berdua di rumah kemarin malam, kamu sama sekali nggak menyinggung soal itu ke aku, Chi-chan. Biasanya kalau ada rencana keluar sama teman-teman, kamu langsung cerita sambil makan."
            chiasa "Ah... yang itu kan waktunya belum pasti jadi, Ko-nii. Jadwal studio mereka masih bisa geser. Aku malas cerita duluan ke kamu kalau nanti ujung-ujungnya malah batal."
            koita "Terus waktu di pantai tadi, kenapa kamu sempat berbisik sebentar ke Harumi-san tepat waktu aku jalan mendekat?"
            chiasa "Itu aku cuma nanya apakah dia bawa salep pelindung matahari cadangan, soalnya bahuku mulai perih kena angin laut. Memangnya hal sekecil itu harus diumumkan keras-keras?"
            nar "Koita menatapmu selama beberapa detik penuh dalam keheningan dapur. Senyum tipis muncul di sudut bibirnya, tetapi sorot matanya sama sekali belum mengendur."
            koita "Aku pengin percaya sama alasanmu barusan, Chi-chan. Sungguh. Cuma... belakangan ini setiap kali aku bertanya sesuatu ke kamu, jawabanmu selalu keluar terlalu cepat dan terlalu rapi."
            chiasa "Terlalu rapi gimana sih, Ko-nii? Aku kan cuma menjawab pertanyaanmu satu per satu."
            koita "Persis itu masalahnya. Dulu kalau kamu lupa cerita sesuatu, kamu bakal bengong dulu atau protes balik. Sekarang kalimatmu selalu meluncur mulus, kayak kamu sudah menyiapkan semua alasan itu di kepalamu jauh sebelum aku buka mulut."
            chiasa "Nggak ada alasan yang sengaja kusiapkan, Ko-nii. Aku cuma jawab apa adanya kok."
            nar "Koita tidak mendebat lebih lanjut. Ia mengembuskan napas perlahan, mengangkat nampan kayu berisi tujuh cangkir hangat itu dengan kedua tangannya, lalu berjalan melewati pintu dapur menuju ruang tengah. Sisa uap air panas tertinggal menggantung di udara di antara kalian."
        else:
            nar "Kamu melangkah mendekat ke meja konter dan bersandar santai di tepinya. Kamu sadar bahwa menghindar secara terang-terangan hanya akan mempertebal kecurigaannya."
            yutaka "Nggak ada yang aneh kok, Koita. Aku cuma lagi banyak pikiran aja belakangan ini. Wajar kan kalau pembawaanku terasa sedikit berbeda?"
            koita "Banyak pikiran soal urusan kuliah atau urusan dari rumah?"
            yutaka "Campur-campur lah. Lagian jadwal kelas kita sekarang kan nggak selalu bareng, jadi aku juga makin sering ngobrol sendiri sama teman-teman lain di luar waktu kumpul kita. Otomatis caraku menanggapi orang juga ikut menyesuaikan."
            koita "Iya, kalau soal kesibukan masing-masing di kampus, aku paham."
            yutaka "Tadi di ruang tengah juga kami cuma bahas hal sepele soal dosen sama jadwal kuliah minggu depan. Kebetulan saja waktu kamu melongok masuk, topiknya memang pas habis."
            nar "Koita mengangguk pelan sambil mengaduk cangkir teh di atas nampan dengan sendok kecil. Ia tampak hampir menyudahi pertanyaannya, sebelum tiba-tiba menghentikan gerakan tangannya dan menoleh lagi ke arahmu."
            koita "Lalu gimana soal kemarin waktu kalian bahas rencana jalan akhir pekan depan? Siang tadi aku dengar sekilas Moeka-chan menyebut namamu soal rencana itu."
            yutaka "Oh, yang rencana mampir ke pusat belanja dekat stasiun itu ya?"
            koita "Biasanya kalau ada rencana kumpul apa pun, kamu orang pertama yang ngasih tahu aku, Yutaka. Minimal kamu lempar pesan singkat malamnya. Kali ini nggak ada kabar sama sekali."
            yutaka "Yang itu kan baru obrolan mentah, belum tentu jadi berangkat. Aku malas ngajak kamu duluan kalau ujung-ujungnya malah batal gara-gara jadwal mereka bentrok."
            koita "Terus tadi sore waktu di beranda, kenapa kamu buru-buru memotong kalimatmu sendiri begitu aku keluar bawa minuman?"
            yutaka "Itu karena kami lagi bahas nilai kuis yang jelek, malas aja kalau kamu ikut ngeledek dari belakang."
            nar "Koita menatap wajahmu selama beberapa detik penuh. Senyum tipis terbit di sudut bibirnya, sementara nada suaranya terdengar kaku."
            koita "Aku pengin percaya, Yutaka. Sungguh. Cuma... akhir-akhir ini setiap kali aku nanya sesuatu ke kamu, jawabanmu selalu terdengar terlalu rapi dan cepat."
            yutaka "Masa jawab cepat malah dianggap mencurigakan?"
            koita "Dulu kamu nggak begitu. Dulu kalau kamu lupa ngabarin, kamu langsung bilang lupa terus ketawa santai. Sekarang tiap aku tanya celah kecil sedikit saja, penjelasanmu langsung pas mengunci semua arah, kayak kamu sudah menebak dari jauh-jauh hari aku bakal menanyakan hal itu."
            yutaka "Nggak ada yang kuhitung atau kusiapkan. Memang begitu kenyataannya."
            nar "Koita tidak membalas lagi. Ia mengangkat nampan kayu berisi deretan cangkir hangat itu dengan kedua tangan lalu melangkah keluar menuju ruang tengah, membiarkan keheningan dapur menggantung di belakangnya."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kamu tidak ikut membalas senyumnya. Kamu berdiri tegak di depan meja konter dapur dan menatap balik matanya tanpa berkedip."
            chiasa "Jangan terlalu jauh nebak-nebak hal yang nggak kamu tahu, Ko-nii. Memangnya sejak kapan semua obrolanku sama teman-teman harus kulaporkan satu per satu ke kamu dulu?"
            nar "Koita mengerjap pelan, tampak terkejut mendengar nada suaramu yang mendadak dingin dan memotong lurus."
            koita "Eh, tunggu dulu, Chi-chan. Aku sama sekali nggak minta kamu laporan ke aku. Aku tadi cuma merasa suasananya agak ganjil terus pengin memastikan nggak ada apa-apa..."
            chiasa "Kamu barusan bilang caraku bicara, caraku merespons, sampai tatapan mataku kelihatan mencurigakan. Buatku itu sudah kedengaran kayak kamu lagi memeriksa gerak-gerikku."
            koita "Bukan memeriksa, aku cuma khawatir sama kamu..."
            chiasa "Kalau sikapku berubah sedikit atau aku punya obrolan sendiri sama orang lain di vila ini, itu urusan pribadiku. Tolong berhenti mengorek-ngorek hal yang nggak perlu kamu tahu, ya."
            nar "Tangan Koita yang masih memegang sendok teh perlahan turun. Ia meletakkan sendok logam itu di tepi nampan kayu dengan bunyi denting pelan. Raut ramah yang biasanya hampir tidak pernah lepas dari wajahnya perlahan mengeras menjadi datar."
            koita "...Begitu ya. Baiklah, aku mengerti sekarang. Kalau kamu memang merasa terganggu oleh pertanyaanku, aku nggak akan ikut campur urusan pribadimu lagi."
            chiasa "Baguslah kalau Ko-nii paham."
            nar "Koita tidak mengulurkan cangkir teh susu mana pun ke arahmu. Ia mengangkat nampan kayu berisi cangkir-cangkir hangat itu dengan kedua tangannya, melangkah sampai ke dekat pintu geser dapur, lalu berhenti sejenak dan menoleh sedikit melewati bahunya."
            koita "Tapi satu hal saja, Chi-chan. Kalau hal yang kalian bicarakan di belakangku itu ikut menyangkut teman-temanku yang lain di vila ini... aku masih punya hak buat bertanya langsung ke mereka masing-masing, kan?"
            chiasa "Silakan saja kalau Ko-nii memang mau tanya ke mereka satu per satu."
            koita "Baik. Akan kuingat itu."
            nar "Koita mengangguk singkat, lalu mendorong pintu geser dengan sikunya dan melangkah keluar menuju ruang tengah tanpa menunggumu membantunya membawa satu cangkir pun."
        else:
            nar "Kamu tidak ikut tersenyum. Kamu berdiri tegak sambil menyelipkan kedua tangan ke saku celana dan membalas tatapannya dengan ekspresi datar."
            yutaka "Jangan terlalu jauh nebak-nebak hal yang nggak kamu tahu, Koita. Memangnya sejak kapan setiap obrolanku sama orang lain di vila ini harus lewat persetujuanmu dulu?"
            nar "Koita mengerjap kaget mendengar nada bicaramu yang mendadak tajam tanpa basa-basi."
            koita "Tunggu dulu, Yutaka. Aku sama sekali nggak minta kamu izin ke aku. Aku kan cuma merasa akhir-akhir ini ada yang ganjil, jadi aku nanya langsung ke kamu..."
            yutaka "Kamu barusan nyebut caraku bicara sampai caraku menatap orang berubah drastis. Kalau didengar-dengar, kamu kayak lagi menuduh aku main belakang di liburan ini."
            koita "Aku nggak menuduh, aku cuma nggak biasa lihat kamu menyimpan sesuatu dari..."
            yutaka "Kalau ada yang berubah dari caraku bicara atau bertindak, itu urusanku sendiri. Nggak usah repot-repot mengorek hal yang bukan bagianmu."
            nar "Tangan Koita yang masih memegang sendok kecil perlahan turun. Ia menaruh sendok itu di pinggir nampan kayu dengan bunyi denting halus, sementara raut hangat di wajahnya ikut meredup dan menegang."
            koita "...Oke. Aku paham batasnya. Aku nggak bakal mengorek urusan pribadimu lagi."
            yutaka "Bagus kalau gitu."
            nar "Ia tidak lagi menawarkan kopi hitam yang tadi ia sebutkan. Koita mengangkat nampan kayu itu dengan kedua tangan, berhenti sebentar di depan pintu geser dapur, lalu menoleh sedikit lewat bahunya ke arahmu."
            koita "Tapi kalau apa yang kalian bicarakan tadi menyangkut orang-orang di geng kita juga, aku masih boleh kan menanyakannya langsung ke mereka?"
            yutaka "Silakan saja kalau menurutmu itu memang perlu."
            koita "Oke. Kalau begitu aku ke depan dulu."
            nar "Koita mengangguk singkat lalu mendorong pintu geser dapur dengan sikunya, melangkah keluar ke ruang tengah tanpa menunggumu."
    elif _return == "C":
        if kk_host == "chiasa":
            nar "Mendengar nadanya yang begitu serius hanya karena percakapan ruang tengah yang sempat terhenti, kamu langsung mengeluarkan tawa kecil yang ringan."
            chiasa "Haha, serius nih Ko-nii mikir aku berubah jadi orang lain? Mukamu tegang sekali cuma gara-gara pintu ruang tengah tadi?"
            koita "Lho, aku serius nanya, Chi-chan. Tadi beneran mendadak hening waktu aku buka pintu."
            chiasa "Ya ampun, Ko-nii... coba pikir pakai akal sehat deh. Tadi di ruang tengah yang duduk merapat di karpet kan hampir semuanya perempuan. Masa iya kami lagi ngobrolin gosip sepele, merek perawatan kulit, sama soal pakaian harus ngundang kamu ikut duduk mendengarkan juga?"
            nar "Koita langsung tertegun sebentar, lalu rona merah samar naik ke telinganya karena merasa dugaannya barusan terdengar konyol. Ia menggaruk tengkuknya dengan tangan kiri sambil ikut tertawa canggung."
            koita "Eh... kalian tadi bahas soal pakaian sama gosip perempuan ya? Aduh, pantas saja pas aku melongok semua langsung pada diam..."
            chiasa "Nah, baru nyambung kan sekarang? Aku kira Ko-nii sudah paham sendiri tanpa perlu dijelasin."
            koita "Haha, parah sekali aku barusan. Kedengarannya berlebihan banget ya? Kayak orang yang merasa wajib dapat undangan resmi buat setiap obrolan di vila ini."
            chiasa "Mungkin kamu cuma kecapekan habis menyetir jauh sama bantu angkat-angkat barang bawaan dari siang tadi, makanya malam ini jadi gampang berpikiran macam-macam."
            koita "Iya juga sih, pundakku dari sore tadi memang pegal sekali, terus tadi sempat kena angin pantai pas jemur handuk. Maaf deh, Chi-chan, aku malah ngomong ngelantur kayak orang curigaan begitu ke kamu."
            chiasa "Santai saja, aku nggak ambil hati kok. Lagian kalau aku beneran berubah jadi orang lain, masa aku masih minta dibikinin teh susu manis kayak biasa?"
            koita "Haha, benar juga! Kalau yang itu sih jelas masih Chi-chan."
            chiasa "Sudah, mana cangkir yang harus kubantu bawa ke ruang depan? Jangan sampai ketelnya dingin duluan."
            nar "Koita mengembuskan napas lega. Seluruh ketegangan di pundaknya hilang saat ia meraih kembali ketel listrik untuk mengisi dua cangkir terakhir, lalu menggeser dua cangkir keramik hangat ke dekat tanganmu."
            koita "Tolong bantu bawa dua cangkir yang di pinggir ini ya, hati-hati gagangnya agak panas. Ayo kita ke depan, nanti acara kuisnya keburu selesai."
            chiasa "Siap, jalan duluan aja, Ko-nii."
        else:
            nar "Mendengar nadanya yang kelewat tegang hanya gara-gara percakapan ruang tengah yang berhenti saat ia masuk, kamu langsung tertawa pelan."
            yutaka "Haha, serius kamu mikir aku berubah jadi orang lain, Koita? Mukamu sampai kaku begitu cuma gara-gara obrolan di ruang depan?"
            koita "Hei, aku nggak bercanda, Yutaka. Tadi beneran langsung sepi begitu aku buka pintu geser."
            yutaka "Ya ampun, coba kamu ingat-ingat lagi. Tadi di karpet ruang tengah itu mereka lagi rebutan nebak skor kuis televisi sambil ngegosipin dosen pengampu yang galak. Begitu lihat mahasiswa teladan kayak kamu muncul di pintu, ya refleks pada berhenti sebentar lah."
            nar "Koita terdiam sesaat, lalu wajahnya tampak sedikit memerah karena merasa kecurigaannya barusan terdengar berlebihan. Ia menggaruk bagian belakang kepalanya sambil ikut tertawa kikuk."
            koita "Eh... cuma gara-gara lagi bahas dosen sama acara televisi? Aduh, aku kedengaran konyol banget ya barusan?"
            yutaka "Lumayan. Kayak pejabat yang tersinggung gara-gara nggak dikasih undangan resmi ke rapat obrolan receh."
            koita "Haha, jangan diledek terus dong. Habisnya dari sore kepalaku memang agak berat sedikit, jadi gampang mikir aneh-aneh."
            yutaka "Makanya. Dari siang tadi kamu yang paling sibuk nyetir, angkat kardus belanjaan, sampai beresin teras. Wajar kalau malam ini fokusmu agak oleng."
            koita "Iya juga sih, bahuku memang mulai pegal. Maaf deh, Yutaka, aku malah ngomong yang nggak-nggak dan terkesan menuduh kamu tadi."
            yutaka "Santai saja, nggak kuanggap serius juga. Lagian kalau aku beneran jadi orang lain, masa aku masih nagih kopi hitam tanpa susu ke kamu?"
            koita "Haha, masuk akal. Selera pahitmu itu mana mungkin ketukar sama orang lain."
            yutaka "Sudah, bereskan dulu tuangnya. Mana cangkir yang perlu kubantu bawa ke depan?"
            nar "Koita tersenyum lega. Seluruh kerutan curiga di keningnya lenyap saat ia menuangkan sisa air panas ke cangkir terakhir lalu menggeser dua cangkir hangat ke arahmu."
            koita "Tolong bawa dua yang sebelah kanan ini ya sebelum dingin. Ayo kita balik ke ruang tengah."
            yutaka "Oke, kamu jalan duluan, biar kututup pintu dapurnya."
    else:
        if kk_host == "chiasa":
            nar "Kamu berpura-pura tidak menangkap arah selidik di dalam kalimatnya. Kamu justru melangkah santai ke samping nampan kayu dan menunduk mengamati deretan cangkir keramik yang baru selesai ia seduh."
            chiasa "Sudahlah, bahas jadwal kita minggu depan aja yuk, Ko-nii. Eh, tunggu, ini air panasnya sudah dituang ke semua cangkir ya? Yang mana dulu yang harus kubawa ke ruang tengah? Jangan sampai salah bagi lho, nanti ada yang protes kalau tertukar."
            nar "Begitu pembicaraan dialihkan ke urusan pembagian minuman untuk teman-teman dan rencana pekan depan, ketegangan di bahu Koita langsung mengendur. Ia segera menunjuk deretan cangkir itu satu per satu dengan antusiasme kebiasaannya mengurus orang lain."
            koita "Oh, tunggu sebentar, jangan asal ambil ya! Cangkir warna biru muda yang ini khusus punya Harumi-san, teh hijau tawar sama sekali nggak pakai gula. Terus cangkir hijau di pojok kanan itu punya Nagisa-chan. Tadi waktu kutanya dia bilangnya terserah, tapi aslinya dia nggak suka teh yang terlalu manis, jadi cuma kukasih gula setengah sendok."
            chiasa "Ya ampun, Ko-nii hafal di luar kepala sampai takaran gula masing-masing orang ya. Terus dua cangkir putih polos di tengah itu punya siapa?"
            koita "Yang satu teh jelai hangat punya Miyuki-senpai, soalnya tadi dia bilang pengin minuman tanpa kafein biar gampang tidur. Yang sebelahnya cokelat susu agak manis punya Moeka-chan biar badannya cepat hangat lagi."
            chiasa "Lengkap sekali sampai urusan kafein segala diingat. Nah, punyaku yang mana nih?"
            koita "Punya kamu yang paling kiri itu, teh susu hangat pakai gula satu sendok penuh kayak biasa di rumah. Kalau salah takaran nanti malah nggak habis diminum kan sayang."
            chiasa "Sip, terima kasih, Ko-nii. Oh iya, soal minggu depan, jadi nggak kita mampir ke toko buku dekat stasiun sepulang kelas hari Rabu?"
            koita "Jadi dong! Kemarin aku sudah catat judul novel yang mau kubeli, sekalian kalau Chi-chan mau cari kertas gambar baru aku bisa bantu bawakan pulang."
            chiasa "Wah, pas sekali kalau begitu. Ya sudah, aku bawa cangkirku sama punya Kujo-senpai duluan ke depan ya sebelum tehnya keburu dingin."
            koita "Iya, tunggu sebentar, biar kumatikan lampu kompor belakang dulu terus aku langsung jalan di belakangmu angkat nampan sisanya."
            nar "Kalian berdua melangkah keluar dari ruang dapur secara beriringan sambil terus membicarakan daftar belanja pekan depan. Kecurigaan yang sempat hampir terucap tadi tertinggal begitu saja di dekat ketel listrik yang mulai mendingin."
        else:
            nar "Kamu berpura-pura tidak menangkap nada menyelidik di balik ucapannya. Kamu langsung melangkah ke sisi meja konter dan menunjuk deretan cangkir yang masih mengepulkan uap hangat."
            yutaka "Sudahlah, bahas jadwal kita minggu depan aja yuk, Koita. Eh, air panasnya sudah kamu tuang semua nih? Cangkir mana dulu yang harus kubantu bawa ke ruang tengah? Jangan sampai ketukar, nanti aku yang disalahkan kalau rasanya beda."
            nar "Begitu perhatiannya ditarik kembali ke urusan melayani kebutuhan teman-teman, postur kaku Koita langsung mencair. Ia buru-buru menunjuk beberapa cangkir di atas nampan sambil menjelaskan dengan rinci."
            koita "Oh, tunggu dulu, jangan sampai ketukar! Yang cangkir biru muda ini punya Harumi-san, teh tawar tanpa gula sama sekali. Terus yang cangkir hijau di ujung kanan itu punya Nagisa-chan. Dia tadi bilangnya apa saja boleh, tapi dari dulu dia nggak suka kalau kemanisan, jadi gulanya cuma setengah sendok."
            yutaka "Hafal betul ya kamu sampai takaran gula semua orang di ruangan depan. Terus yang dua cangkir keramik putih di tengah itu punya siapa?"
            koita "Yang ini teh jelai hangat tanpa kafein punya Miyuki-senpai, soalnya besok pagi dia mau bangun lebih awal. Sebelahnya cokelat susu hangat buat Moeka-chan."
            yutaka "Berarti punyaku yang warna cokelat tua di pojok kiri ini ya?"
            koita "Betul, kopi hitam tanpa susu dan tanpa gula. Kalau salah bikin nanti orang sungkan mau bilang terus minumannya malah dibiarkan utuh di meja."
            yutaka "Pas banget. Oh iya, soal minggu depan, jadwal kumpul kita di kantin hari Kamis tetap jadi kan? Katanya kamu mau sekalian tukar catatan mata kuliah umum."
            koita "Tetap jadi dong. Nanti sorenya kalau sempat kita bisa mampir sebentar ke kedai ramen dekat gerbang selatan juga, mumpung tugas kuliah minggu depan belum terlalu menumpuk."
            yutaka "Boleh juga itu. Ya sudah, aku bawa kopiku sama cangkir sebelah ini duluan ke depan ya."
            koita "Oke, aku jalan persis di belakangmu bawa nampan kayu ini."
            nar "Kalian berdua melangkah keluar dari dapur menuju keramaian ruang tengah sambil menyusun rencana makan pekan depan, membiarkan pertanyaan tajam Koita tadi menguap begitu saja bersama sisa uap ketel."
    return

# ┌─ PANDUAN CERITA · K13 · Yukata Pilihan
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : festival; Koita memilih siapa yang ditemani.
# │ INTI    : A dukung pilihan / B ganti pilihannya / C hentikan.
# │ AKHIRAN : konfrontasi kecil antar heroine.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K13:
    call kk_scene_enter("koita", "Gedung Sastra · Yukata pilihan")
    nar "Di depan stan festival, dua orang datang dengan ingatan tentang janji yang berbeda. Koita mengatakan ia memang pernah membahas berkeliling dengan keduanya, tetapi belum menetapkan jam."
    koita "Aku pikir nanti kita ketemu semua. Ternyata kalian... menunggu sendiri-sendiri."
    nar "Ia akhirnya menyebut siapa yang akan ditemaninya malam itu. Orang yang tidak dipilih langsung merapikan lengan yukata, gerakan kecil untuk menahan wajahnya agar tidak berubah."
    call kk_family_menu("K13", ["Dukung pilihan Koita.", "Coba ganti pilihannya.", "Hentikan sebelum jadi keributan."])
    if _return == "A":
        nar "Kau mendukungnya mempertahankan pilihan dan menjelaskannya sendiri. Koita sempat ingin mengajak semua orang lagi, lalu menahan kalimat itu."
        koita "Aku minta maaf karena membuatmu mengira sudah ada janji. Malam ini aku pergi dengannya. Aku harusnya bilang lebih awal."
        nar "Kata-kata itu tetap menyakiti. Setidaknya ia tidak lagi meminta orang yang kecewa tersenyum agar pilihan tersebut terasa mudah."
    elif _return == "B":
        nar "Kau menawarkan alasan agar Koita mengganti pendamping. Orang yang semula dipilih bertanya apakah persetujuannya beberapa detik lalu memang bisa dipindahkan begitu saja."
        koita "Tunggu. Jangan kalian yang bertengkar. Aku yang bilang iya dulu."
        nar "Tetapi keduanya sudah saling menatap, masing-masing terpaksa membela harga diri di depan orang banyak. Koita memandangmu seolah baru melihat tangan yang ikut menggeser keadaan."
    else:
        nar "Kau meminta mereka menjauh dari antrean dan berhenti membuat keputusan di hadapan penonton. Koita mengangguk, tampak lega mendapat waktu tanpa harus langsung menyebutnya penundaan."
        koita "Iya. Kita bicara dulu. Aku perlu menjelaskan apa yang pernah kukatakan ke masing-masing."
        nar "Musik festival tetap terdengar dari belakang. Tidak ada yang lagi berpura-pura ini hanya salah memilih stan makanan."
    return

# ┌─ PANDUAN CERITA · K17 · Hari Pengakuan Bentrok
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : beberapa heroine mengaku pada hari yang sama.
# │ INTI    : A dukung satu heroine / B dorong Koita memilih / C sabotase / D pengakuan BL / E pengakuan Chiasa
# │ AKHIRAN : hub besar #8; menentukan arah Tahun 3.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K17:
    call kk_scene_enter("koita", "Gedung Sastra · Hari pengakuan bentrok")
    nar "Koita menunjukkan pesan-pesan yang meminta waktu bicara hari ini. Ia tidak memperlihatkan isinya, tetapi caranya menjaga layar membuatmu tahu ia sudah memahami kemungkinan yang menunggunya."
    koita "Dulu aku akan bilang kita ketemu ramai-ramai saja. Sekarang itu kedengaran seperti cara paling pengecut yang bisa kupilih."
    nar "Ia melihat jam, kemudian pintu koridor. Orang-orang yang akan datang tidak tahu bahwa hari yang mereka siapkan sendirian berbagi tanggal dengan keberanian orang lain."
    koita "Aku harus mendengar satu-satu. Tapi aku takut jawaban yang kuberikan hanya supaya orang itu nggak menangis di depanku."
    menu:
        "Dukung satu heroine untuk maju.":
            $ kk_record_choice("K17", "A")
            nar "Kau membantu satu orang mendapatkan waktu bicara yang utuh. Yang lain tetap menunggu dengan pertanyaan yang tidak boleh dianggap batal hanya karena belum sempat disampaikan."
            koita "Aku akan mendengar. Setelah itu aku harus menjawab yang lain juga."
            nar "Pintu tertutup di belakang mereka. Kau tinggal di koridor, menyadari doronganmu barusan sudah memilih siapa yang mendapat kesempatan pertama, bukan siapa yang pasti dicintai."
        "Dorong Koita yang memilih sendiri.":
            $ kk_record_choice("K17", "B")
            nar "Kau mengingatkannya bahwa rasa takut melukai tidak membebaskannya dari keharusan jujur. Koita menyimpan ponsel tanpa memeriksa siapa yang mengetik."
            koita "Aku tahu pada siapa aku ingin bilang ya. Aku cuma terus mencari cara supaya kata itu nggak terdengar seperti tidak bagi yang lain."
            nar "Ia menarik napas, lalu beranjak."
            koita "Nggak ada cara begitu, ya. Aku akan bicara."
        "Sabotase agar tak ada yang berhasil.":
            $ kk_record_choice("K17", "C")
            nar "Kau menghalangi kesempatan-kesempatan yang hendak mereka gunakan. Menjelang malam, rencana yang dibuat dengan susah payah tinggal salah paham tentang waktu dan keberadaan."
            nar "Koita menunggu seseorang yang tidak datang. Di tempat lain seseorang menunggu balasan yang salah ia pahami. Ketika malam selesai, masing-masing punya alasan merasa keberaniannya tidak dianggap penting."
            koita "Aneh. Hari ini semua ingin bicara, tapi tak satu pun percakapan benar-benar terjadi."
        "Arahkan sebagai pengakuan jalur Yutaka.":
            $ kk_record_choice("K17", "D")
            yutaka "Aku juga punya sesuatu yang harus kamu dengar. Aku menyukaimu. Bukan cuma sebagai sahabat."
            nar "Koita tidak bergerak. Ponsel di tangannya berbunyi, tetapi ia menunggu sampai Yutaka selesai."
            koita "Aku takut kalau menanyakan ini, kita nggak bisa kembali seperti dulu. Ternyata kamu yang harus mengatakannya lebih dulu."
            nar "Pengakuan itu belum jawaban. Tetapi sesudahnya Koita tidak bisa lagi menempatkan Yutaka di luar semua pilihan hanya karena persahabatan mereka terasa paling aman."
        "Arahkan sebagai pengakuan jalur Chiasa.":
            $ kk_record_choice("K17", "E")
            chiasa "Ko-nii, kali ini jangan jawab seolah aku cuma meminta ditemani pulang. Aku ingin kamu mendengar perasaanku sebagai perasaan seorang perempuan dewasa."
            nar "Koita menunduk, lalu mengangkat wajah agar ia tidak harus mengucapkan sisanya kepada orang yang menghindari tatapannya."
            koita "Aku dengar, Chiasa. Aku tahu jawaban asal-asalan akan menyakiti kita lebih lama."
            nar "Rumah yang sama menunggu mereka nanti malam. Kedekatan itu kini tak lagi cukup untuk menyamarkan percakapan yang harus mereka selesaikan."
    return

# ┌─ PANDUAN CERITA · K20 · Atap Penginapan
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : Koita mengajak pemain bicara jujur.
# │ INTI    : A ungkapkan sebagian kebenaran / B diam / C tantang.
# │ AKHIRAN : Koita bisa mengubah sikap drastis.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K20:
    call kk_scene_enter("koita", "Rumah Amamiya · Atap, malam jujur")
    nar "Di atap penginapan, Koita memilih bangku yang jauh dari pagar. Bunyi pendingin ruangan menelan suara dari halaman bawah. Ia sudah menunggu sebelum kau datang."
    koita "Aku mau bicara tanpa orang lain yang harus kita buat nyaman. Kamu boleh marah. Aku mungkin juga akan marah. Tapi aku capek pulang dari percakapan denganmu sambil menebak apa yang sebenarnya terjadi."
    nar "Ia menunjuk sisi bangku yang kosong, membiarkanmu memilih duduk atau tetap berdiri."
    call kk_family_menu("K20", ["Ungkapkan sebagian kebenaran.", "Diam saja.", "Tantang balik kejujurannya."])
    if _return == "A":
        nar "Kau mengungkap bagian kebenaran yang selama ini ditutup. Koita mendengarkan, beberapa kali mengulang perkataanmu agar kau tidak bisa berlindung di balik makna yang berubah."
        koita "Aku menghargai kamu bilang. Tapi aku belum tahu apakah yang tersisa lebih besar daripada yang baru kudengar."
        nar "Ia meremas ujung lengan bajunya."
        koita "Jangan minta aku langsung tenang. Aku perlu memikirkan apa yang kulakukan setelah ini."
    elif _return == "B":
        nar "Kau membiarkan mesin pendingin mengisi waktu. Koita menunggu sampai jelas bahwa kau tidak sedang mencari kata-kata."
        koita "Baik. Aku nggak bisa memaksa. Aku juga nggak harus terus menganggap diam berarti aku aman di dekatmu."
        nar "Ia berdiri, tidak membanting apa pun, tidak membuat permintaan terakhir. Jarak yang ia sisakan kali ini terasa disengaja dan sulit diseberangi."
    else:
        nar "Kau menantang kejujurannya sendiri: ketakutan yang dipakai untuk menahan orang, perhatian yang selalu berhenti sebelum komitmen. Koita bereaksi seperti ditampar, lalu memaksa dirinya tetap duduk."
        koita "Iya. Ada yang benar. Aku ingin dicintai tanpa menanggung keputusan."
        nar "Ia menatapmu kembali."
        koita "Sekarang giliranmu. Jangan jadikan kesalahanku alasan untuk berhenti membahas perbuatanmu. Kalau kita mau jujur, kita harus tinggal di percakapan yang sama."
    return

# ┌─ PANDUAN CERITA · K21 · Yukata Terakhir
# │ LOKASI  : Hunian Biasa · Rumah Amamiya
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : Koita menolak ditemani siapa pun.
# │ INTI    : A temani sebagai teman / B temani sebagai lebih / C biarkan.
# │ AKHIRAN : B bisa membuka jalur BL.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K21:
    call kk_scene_enter("koita", "Rumah Amamiya · Yukata terakhir")
    nar "Koita selesai memakai yukata, lalu duduk di beranda dengan sandal yang belum dikenakan. Ia sudah menolak ajakan kelompok untuk berangkat bersama. Musik festival datang sayup dari arah sungai."
    koita "Aku bilang mau sendiri karena lebih mudah daripada menjelaskan ingin ditemani siapa."
    nar "Ia akhirnya mengenakan sandal, tetapi belum berdiri."
    koita "Kalau itu kamu, aku mau. Cuma aku harus tanya juga: kamu datang sebagai apa malam ini?"
    call kk_family_menu("K21", ["Temani ia sebagai teman.", "Temani ia sebagai sesuatu yang lebih.", "Biarkan ia sendiri."])
    if _return == "A":
        nar "Kau menyebut persahabatan dengan jelas. Koita menatap halaman sebentar, lalu mengangguk."
        koita "Baik. Aku senang kamu nggak membiarkan aku menebak."
        nar "Kalian berangkat berdampingan, menyisakan ruang yang cukup bagi jawaban itu. Di gerbang festival ia bertanya stan mana yang ingin kautuju, bukan siapa yang mungkin akan kalian temui."
    elif _return == "B":
        nar "Kau mengatakan ingin malam ini menjadi kencan. Koita membetulkan lengan yukatanya yang tidak berantakan, lalu tertawa malu pada dirinya sendiri."
        koita "Kamu bisa bilang begitu langsung, ya. Aku dari tadi mencari lima cara memutarinya."
        nar "Ketika kalian berdiri, ia menawarkan tangannya dan menunggu. Gerakan kecil itu punya arti yang tidak lagi perlu disembunyikan di balik sesaknya keramaian."
    else:
        nar "Kau memilih tidak menemaninya. Koita mengangguk, menghabiskan beberapa detik untuk menerima jawaban sebelum memaksakan senyum."
        koita "Baik. Aku akan pergi sebentar. Mungkin pulang kalau sudah terlalu ramai."
        nar "Ia berjalan menuju lampion tanpa menunggu langkah lain menyusul. Festival tetap berlangsung, dan malam ini ia harus menentukan sendiri kapan ingin menikmatinya dan kapan ingin berhenti."
    return

# ┌─ PANDUAN CERITA · K22 · Malam Terakhir di Vila
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : Koita menghadapi pemain; percakapan paling jujur.
# │ INTI    : A pengakuan / B penolakan / C pertengkaran.
# │ AKHIRAN : menentukan ending BL (Male).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K22:
    call kk_scene_enter("koita", "Gedung Sastra · Malam terakhir")
    nar "Barang-barang vila sudah ditumpuk dekat pintu. Koita meminta waktu sebelum perjalanan pulang, membawa dua minuman yang kali ini ia pilih setelah menanyakan apa yang kauinginkan."
    koita "Aku ingin berhenti memakai besok sebagai tempat menyimpan semua keberanianku. Tentang kita... aku punya perasaan yang bukan cuma persahabatan."
    nar "Ia menaruh minumannya agar tangannya tidak terus bergetar pada botol."
    koita "Kamu nggak harus menjawab sesuai harapanku. Tapi aku ingin mendengarnya dengan jelas. Setelah itu aku akan belajar hidup dengan jawabannya."
    call kk_family_menu("K22", ["Balas dengan pengakuan.", "Tolak dengan jujur.", "Biarkan jadi pertengkaran."])
    if _return == "A":
        nar "Kau membalas pengakuannya. Koita menunduk, tertawa satu kali seperti tidak percaya suara lega itu miliknya."
        koita "Aku mau bersamamu. Kalimatnya ternyata sesederhana itu. Kenapa aku membuatnya sesusah ini?"
        nar "Ia mengulurkan tangan. Ketika kau menerimanya, ia tidak buru-buru mengubah momen itu menjadi gurauan."
        koita "Masih ada yang harus kujelaskan ke orang lain. Aku akan melakukannya sendiri. Aku nggak mau kita mulai dengan menyuruh semua orang terus menebak."
    elif _return == "B":
        nar "Kau menolak tanpa menawarkan kemungkinan yang tidak kauinginkan. Koita menarik napas panjang, lalu mengangguk pada kata-kata yang baru didengarnya."
        koita "Sakit. Tapi aku mengerti. Aku nggak akan meminta kamu menjelaskannya sampai alasanmu terdengar cukup untukku."
        nar "Ia meminta waktu sendiri sebelum kembali membantu mengangkat tas. Ketika kalian pulang, ia memilih tempat duduk yang tidak memaksanya terus bersikap biasa di sampingmu."
    else:
        nar "Percakapan membesar ketika masing-masing mulai memakai kesalahan lama untuk membatalkan hak yang lain merasa terluka. Nama orang lain terseret, lalu janji yang pernah tidak ditepati."
        koita "Kamu selalu mau kejujuran, tapi begitu jawabanku nggak mudah untukmu, kamu menghitung semua hal yang pernah salah!"
        nar "Kau membalas. Ia juga. Pada akhirnya tidak ada yang memenangkan percakapan, hanya dua orang yang kini tahu kalimat mana yang dipilih untuk paling melukai."
        nar "Barang-barang tetap harus dibawa pulang. Kalian mengangkat tas secara bergantian tanpa lagi menawarkan bantuan."
    return

init 1 python:
    _hook("K04-A", lambda: kk_rel("koita","trust",5))
    _hook("K04-B", lambda: (kk_koita_suspect(5), kk_flag("koita_dibohongi_pilihan")))
    _hook("K04-C", lambda: kk_rel("koita","trust",3))
    _hook("K04-D", lambda: (kk_flag("koita_ditawari_nama"), kk_rel("koita","intim",4)))
    _hook("K05-A", lambda: kk_koita_suspect(6))
    _hook("K05-B", lambda: (kk_koita_suspect(8), kk_flag("koita_diperingatkan")))
    _hook("K05-C", lambda: kk_koita_suspect(-5))
    _hook("K05-D", lambda: kk_koita_suspect(-4))
    _hook("K13-A", lambda: kk_rel("koita","trust",4))
    _hook("K13-B", lambda: (kk_flag("koita_pilihan_diganti"), kk_koita_suspect(5)))
    _hook("K13-C", lambda: kk_rel("koita","trust",3))
    _hook("K17-A", lambda: kk_flag("koita_heroine_diarahkan"))
    _hook("K17-B", lambda: (kk_rel("koita","trust",5), kk_flag("koita_memilih_sendiri")))
    _hook("K17-C", lambda: (kk_flag("koita_hari_pengakuan_disabotase"), kk_koita_fear(6)))
    _hook("K17-D", lambda: kk_flag("koita_arah_bl"))
    _hook("K17-E", lambda: kk_flag("koita_arah_success"))
    _hook("K20-A", lambda: (kk_rel("koita","trust",5), kk_flag("koita_diberi_sebagian")))
    _hook("K20-B", lambda: kk_rel("koita","trust",-4))
    _hook("K20-C", lambda: kk_rel("koita","jeal",5))
    _hook("K21-A", lambda: kk_rel("koita","aff",4))
    _hook("K21-B", lambda: (kk_flag("koita_arah_bl"), kk_rel("koita","intim",6)))
    _hook("K21-C", lambda: kk_rel("koita","aff",-3))
    _hook("K22-A", lambda: (kk_flag("koita_bl_pengakuan"), kk_rel("koita","intim",8)))
    _hook("K22-B", lambda: kk_flag("koita_bl_ditolak"))
    _hook("K22-C", lambda: (kk_rel("koita","jeal",8), kk_flag("koita_bl_bertengkar")))
