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
        nar "Kilatan emas dan merah tua mekar di langit malam jauh lebih dahulu daripada dentuman gemanya yang menggetarkan dada. Kalian berdua berdiri agak terpisah dari kerumunan utama di tepi pagar batu yang agak tinggi, tempat suara riuh stan festival mereda menjadi dengung samar di kejauhan."
        nar "Di sebelahmu, Amamiya Koita menengadah memandangi bunga api yang perlahan gugur menjadi percikan kecil di atas atap gedung kampus. Cahaya warna-warni itu menerangi wajahnya yang tenang—tetapi ketika ia akhirnya membuka suara di sela jeda dua ledakan, pertanyaannya sama sekali tidak mengikuti apa yang sedang kalian lihat di langit."
        koita "Chi-chan... kalau kamu jadi aku, kamu akan memilih siapa?"
        nar "Kau menoleh perlahan ke arahnya. Begitu mata kalian bertemu di bawah kilatan cahaya biru dari langit, Koita buru-buru mengeluarkan tawa pendek yang terdengar terlalu ringan untuk pertanyaan seberat itu."
        koita "Haha—aneh banget ya aku nanya begitu. Aku tahu kok hal kayak gini nggak bisa diserahkan ke orang lain. Cuma... akhir-akhir ini kamu kelihatan jauh lebih tenang dan lebih paham apa yang sebenarnya terjadi di sekitar kita daripada aku sendiri."
        nar "Ia kembali menatap ke depan, kedua tangannya bertumpu di pagar batu yang dingin. Di balik senyum kecilnya yang masih terpasang, ada keraguan nyata dari seseorang yang selama ini terlalu terbiasa menunda setiap pilihan."
    else:
        nar "Kilatan kembang api tiba lebih dahulu daripada bunyinya. Koita memandang langit, tetapi pertanyaannya tidak mengikuti apa yang sedang kalian lihat."
        koita "Kalau kamu jadi aku, kamu akan memilih siapa?"
        nar "Ia buru-buru tertawa ketika kau menoleh."
        koita "Aneh, ya. Aku tahu itu nggak bisa diserahkan ke orang. Cuma kamu kelihatan lebih paham apa yang terjadi daripada aku."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Jawab jujur siapa yang menurutmu tepat.", "Beri jawaban yang bukan pendapat sebenarnya.", "Balik bertanya siapa yang ia inginkan.", "Sebut namamu sendiri."])]
    call screen kk_choice_panel(_rows, "Di bawah kembang api")
    $ kk_record_choice("K04", _return)
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kau menatap langit sebentar sebelum menjawab dengan jujur—menyebutkan tipe orang yang menurutmu paling tepat untuknya, lengkap dengan alasan mengapa hubungan itu tidak akan selalu mudah dan justru akan menuntut Koita untuk belajar jujur serta berhenti lari dari keputusan."
            nar "Koita mendengarkan dari awal sampai akhir tanpa menyela, dan yang paling mengejutkan, tanpa buru-buru menyebut nama orang lain untuk menyeimbangkan pembicaraan."
            koita "...Aku tadinya mengira kamu bakal menunjuk pilihan yang paling gampang dan paling aman buatku, Chi-chan. Ternyata kamu mempertimbangkan perasaannya juga, bukan cuma nyamanku."
            chiasa "Kalau Ko-nii cuma cari yang paling gampang, nanti ujung-ujungnya malah nyakitin dua-duanya."
            nar "Ia mengangguk pelan lalu kembali menengadah menatap kembang api perak yang mekar lebar di atas sana."
            koita "Makasih sudah jawab serius. Aku bakal pikirkan baik-baik. Tenang saja—bukan berarti nanti kalau gagal aku bakal menyalahkanmu karena ini keputusanku sendiri."
            nar "Untuk malam ini, di bawah gema kembang api, ia tampak satu langkah lebih dekat untuk memandang perasaan orang lain sebagai sesuatu yang nyata, bukan sekadar kehangatan yang boleh digantung."
        else:
            nar "Kau memberikan pendapatmu, termasuk alasan mengapa hubungan itu bisa menyulitkannya. Koita mendengar tanpa segera menyebut nama lain."
            koita "Aku pikir kamu akan pilih yang paling gampang bagiku. Ternyata kamu mempertimbangkan dia juga."
            nar "Ia menatap langit lagi."
            koita "Makasih. Aku akan pikirkan. Bukan berarti nanti aku bisa bilang keputusan ini salahmu kalau gagal."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Alih-alih memberikan pendapatmu yang sebenarnya, kau memilih satu jawaban yang sengaja kauarahkan—jawaban yang bukan sungguh kaupercaya tepat untuknya, namun terdengar cukup masuk akal untuk menggeser arah pikirannya."
            nar "Koita tidak menertawakannya ataupun menebak bahwa kau sedang bermain peran. Sebaliknya, ia justru menerimanya dengan keseriusan yang tak terduga, memutar badannya menghadapmu penuh sambil bertanya lebih dalam."
            koita "Oh... kamu beneran mikir begitu? Kenapa menurutmu dia yang paling cocok buatku, Chi-chan?"
            nar "Pertanyaan susulan itu memaksamu menyusun satu demi satu alasan tambahan yang sama sekali tidak kauyakini—kata-kata yang meluncur mulus dari bibirmu di bawah suara dentuman kembang api."
            koita "...Aku nggak pernah melihatnya dari sudut pandang itu. Pantas saja aku selalu bingung sendiri selama ini."
            nar "Melihat betapa sungguh-sungguh ia menyimpan kalimatmu, kebohongan itu mendadak terasa jauh lebih panjang daripada sekadar satu nama. Kini ada kemungkinan nyata ia akan melangkah menghampiri seseorang dengan keberanian yang baru saja kauarahkan ke tempat yang keliru."
        else:
            nar "Kau memberi jawaban yang bukan pendapatmu. Koita menerimanya dengan serius, mengajukan pertanyaan yang membuatmu harus menambahkan alasan yang juga tidak sungguh kaupercaya."
            koita "Aku nggak pernah melihatnya dari situ."
            nar "Kepercayaannya membuat kebohongan itu terasa lebih panjang daripada satu nama. Kini ada kemungkinan ia akan datang kepada seseorang dengan keberanian yang kauarahkan ke tempat yang salah."
    elif _return == "C":
        if kk_host == "chiasa":
            nar "Kau tidak memberinya nama siapa pun. Kau menoleh penuh ke arahnya dan mengembalikan pertanyaan itu tepat ke hadapannya."
            chiasa "Kenapa malah tanya aku, Ko-nii? Yang bakal menjalaninya kan kamu—sebenarnya siapa yang kamu inginkan?"
            nar "Mulut Koita sempat terbuka hendak menjawab secara otomatis, tetapi kalimat ringan yang biasa ia pakai untuk menghindar mendadak terasa terlalu murahan di bawah langit malam ini. Ia menutup mulutnya lagi, menunduk menatap tangannya di pagar batu."
            koita "...Aku cuma ingin nggak kehilangan siapa-siapa. Tapi itu bukan jawaban yang sama, ya."
            nar "Ledakan kembang api berikutnya bergema keras di kejauhan, membuat kalian berdua terdiam selama beberapa detik sementara cahaya kuning keemasan menyapu wajahnya."
            koita "Sebenarnya... ada orang yang bahkan nggak pernah berani kumasukkan ke daftar kemungkinan, Chi-chan. Mungkin karena aku terlalu takut—kalau aku mulai memikirkannya serius, semuanya yang sudah nyaman selama ini bakal berubah total."
            nar "Ia tidak menyebut nama siapa yang ia maksud, tetapi nada suaranya yang rendah dan jujur menyisakan gema yang jauh lebih lama daripada suara kembang api di atas kepala kalian."
        else:
            nar "Kau mengembalikan pertanyaan itu kepadanya. Koita membuka mulut, lalu menutupnya ketika jawaban yang biasa dipakai terasa terlalu mudah."
            koita "Aku ingin nggak kehilangan siapa-siapa. Itu bukan jawaban yang sama, ya."
            nar "Ledakan berikutnya membuat kalian diam sejenak."
            koita "Ada orang yang bahkan nggak pernah kumasukkan ke daftar kemungkinan. Mungkin karena terlalu takut kalau memikirkannya akan mengubah segalanya."
    else:
        if kk_host == "chiasa":
            nar "Kau tidak mengalihkan pandangan dari wajahnya. Tepat ketika kilatan kembang api di langit mulai memudar menjadi asap tipis dan keheningan turun selama dua detik, kau menjawab dengan suara yang tenang, jelas, dan tidak memberi ruang untuk dianggap candaan."
            chiasa "Kalau aku jadi Ko-nii? Aku pilih aku."
            nar "Koita langsung menoleh ke arahmu. Dalam sisa cahaya redup yang memudar di langit, seluruh raut santai dan senyum refleks yang biasa melindungi wajahnya lenyap tanpa bekas."
            koita "...Kamu?"
            nar "Ia tidak menertawakannya seperti setiap kali Chiasa dulu menggodanya di meja makan. Ia juga tidak memanggilmu 'Chi-chan' untuk mengembalikan percakapan ini ke wilayah aman antara kakak dan adik tiri."
            nar "Jarak di antara kalian di tepi pagar batu mendadak terasa jauh lebih sempit daripada semenit lalu. Koita menatap matamu lurus-lurus, dadanya naik turun pelan menarik napas."
            koita "Aku... aku belum tahu harus jawab apa sekarang. Jujur, kepalaku langsung kosong. Tapi aku dengar jelas apa yang barusan kamu bilang."
            chiasa "Aku nggak minta jawaban malam ini kok, Ko-nii."
            koita "Iya... dan aku nggak akan pura-pura kamu nggak pernah mengatakannya."
            nar "Dentuman kembang api terakhir mekar di atas sana, tetapi tidak satu pun dari kalian yang kembali menengadah ke langit—karena batas aman di antara kalian berdua baru saja bergeser untuk selamanya."
        else:
            nar "Kau menyebut namamu sendiri. Koita melihatmu tepat ketika cahaya di langit memudar; sesaat wajahnya terbuka tanpa bantuan lelucon."
            koita "Kamu?"
            nar "Ia tidak menertawakannya. Tidak pula memanggilmu dengan sebutan akrab yang bisa mengembalikan percakapan ke tempat aman."
            koita "Aku belum tahu harus jawab apa. Tapi aku dengar. Aku nggak akan pura-pura kamu nggak pernah mengatakannya."
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
    nar "Koita berjajar dengan cangkir-cangkir di dapur vila. Ia menakar gula tanpa bertanya; ada terlalu banyak kesukaan yang sudah dihafalnya. Dari ruang tengah terdengar percakapan mendadak pecah menjadi tawa."
    koita "Tadi pas aku masuk, semuanya diam. Waktu kamu masuk, mereka langsung lanjut. Aku baru tahu ada bagian liburan yang nggak kuikuti."
    nar "Ia menuang air panas dengan hati-hati, lalu menatapmu."
    koita "Ada yang berubah tentangmu. Aku cuma belum tahu apa."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Jelaskan situasimu dengan tenang.", "Beri peringatan halus agar ia tak menggali.", "Tertawakan kecurigaannya.", "Alihkan perhatiannya ke hal lain."])]
    call screen kk_choice_panel(_rows, "Percakapan di dapur")
    $ kk_record_choice("K05", _return)
    if _return == "A":
        nar "Kau memberinya penjelasan tenang tentang perubahan sikapmu. Koita mengikuti setiap bagian, lalu menanyakan detail kecil yang tidak kausiapkan."
        koita "Aku ingin percaya. Cuma kamu menjelaskan semua yang kutanya seperti sudah tahu aku akan bertanya."
        nar "Ia mengangkat nampan. Pembicaraan selesai karena minuman perlu diantar, bukan karena rasa ingin tahunya habis."
    elif _return == "B":
        nar "Kau memperingatkan agar ia tidak menggali urusanmu. Koita meletakkan sendok yang sejak tadi masih dipegangnya."
        koita "Baik. Aku nggak akan membuka urusan pribadimu. Tapi kalau itu menyangkut teman-temanku, aku masih boleh bertanya kepada mereka."
        nar "Ia keluar dengan nampan, tidak menunggumu membantu. Jarak itu terlalu disengaja untuk dianggap kebetulan."
    elif _return == "C":
        nar "Kau tertawa dan mengatakan orang bisa saja punya cerita tanpa melibatkan seluruh vila. Koita ikut tertawa setelah sempat tampak malu."
        koita "Iya, ya. Kedengarannya aku seperti harus dapat undangan untuk setiap obrolan."
        nar "Ia meminta kau membawa dua cangkir terakhir. Untuk malam ini ia bersedia memperlakukan keganjilan tadi sebagai rasa tersisih yang tidak perlu dibesarkan."
    else:
        nar "Kau menanyakan minuman mana yang harus diantar lebih dahulu. Koita segera menjelaskan kebiasaan semua orang, lega menemukan urusan yang bisa ia lakukan dengan baik."
        koita "Yang ini jangan ketukar. Dia bilang nggak apa-apa, tapi sebenarnya nggak suka terlalu manis."
        nar "Kalian keluar bersama membawa nampan. Pertanyaannya tertinggal di dapur, ditutupi percakapan yang memberinya kembali tempat sebagai orang yang diperlukan."
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
