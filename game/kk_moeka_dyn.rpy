# Event dinamis Moeka (Mo-D01..Mo-D13) — beban keluarga, topeng, isolasi,
# dan jendela-jendela intervensi menuju Mo25. Semua ditulis sebagai konsekuensi
# dan karakter; beat berat tanpa metode. Lihat [[feedback-force-route-non-operational]].

init 1 python:
    def kk_moeka_mask(delta):
        pts.setdefault("topeng_moeka", 0)
        kk_adj("topeng_moeka", delta)
    def kk_moeka_rely(delta):
        pts.setdefault("andalan_moeka", 0)
        kk_adj("andalan_moeka", delta)

# ┌─ PANDUAN CERITA · Mo-D01 · Onigiri Jam Tiga
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kohinata Moeka
# │ AWALAN  : konbini saat Dini Hari; stres_total ≥ 60
# │ INTI    : A duduk makan bersama / B tanya langsung / C bercanda / D antar pulang
# │ AKHIRAN : andalan[[pemain] +; topeng −
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo_D01:
    call kk_scene_enter("moeka", "Konbini · Dini hari")
    nar "Lampu neon toko serba ada terasa terlalu putih dan tajam untuk pukul tiga dini hari. Di sudut meja makan dekat kaca depan, Moeka duduk sendirian menghadap sebungkus onigiri yang plastik pembungkusnya baru terbuka separuh. Bahkan pada jam selarut ini, begitu mendengar bunyi lonceng pintu, senyum cerahnya langsung terpasang otomatis."
    if kk_host == "chiasa":
        moeka "Lho, Chimian juga masih melek jam segini? Aku tadinya mau bilang cuma lapar tengah malam, tapi jam tiga pagi begini sudah lebih dekat ke sarapan ya, haha!"
        chiasa "Moemoe-senpai sendiri baru selesai kerja paruh waktu ya? Wajah Senpai kelihatan lelah banget di bawah lampu sini."
    else:
        moeka "Eh, Yutayuta belum tidur jam segini? Aku mau bilang cuma cari camilan tengah malam, tapi jam segini kayaknya sudah masuk hitungan sarapan kepagian ya, haha!"
        yutaka "Kamu baru kelar shift malam, Kohinata? Pantulan wajahmu di kaca kelihatan capek sekali."
    nar "Moeka menertawakan candaannya sendiri sebelum pandangannya sempat jatuh ke pantulan kaca jendela. Di bawah sinar putih terang itu, lingkar lelah di bawah matanya terlalu jelas untuk disembunyikan."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", KK_DYN_BY_ID["Mo-D01"]["choices"])]
    call screen kk_choice_panel(_rows, "Jam tiga pagi di konbini")
    $ kk_record_choice("Mo-D01", _return)
    if _return == "A":
        nar "Kamu mengambil satu kotak sup hangat dan segelas teh dari rak lalu duduk di kursi sebelah Moeka agar ia tidak merasa sedang diawasi makan sendirian."
        if kk_host == "chiasa":
            chiasa "Aku juga lapar nih, Moemoe-senpai. Aku duduk makan bareng sini ya, nggak usah repot-repot nyari bahan bercanda."
            moeka "Chimian mau duduk nemenin? ...Makasih ya. Jujur aja, rasanya sepi banget tiap malam makan sendirian terus di pojok begini."
        else:
            yutaka "Kebetulan perutku juga kosong, Kohinata. Aku ikut duduk makan di sini ya, santai aja."
            moeka "Yutayuta mau duduk bareng? ...Makasih banget. Aneh ya, biasanya aku selalu ramai di kampus, tapi makan sendirian jam segini rasanya dingin sekali."
        nar "Beberapa menit kemudian bahu Moeka perlahan meluruh dan deretan candaannya akhirnya berhenti berdesakan."
        moeka "Aku nggak harus punya cerita seru dulu supaya boleh ditemani duduk, kan?"
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Moemoe-senpai, jujur aja, kenapa jam tiga pagi masih duduk di sini belum pulang ke kos? Di rumah baik-baik saja kan?"
        else:
            yutaka "Kohinata, kamu aman kan? Kenapa jam tiga pagi begini masih duduk di toko serba ada daripada langsung istirahat di kos?"
        moeka "Kenapa aku di sini jam segini ya... pertanyaan yang ternyata nggak kusiapkan jawaban lucunya."
        nar "Moeka menunduk memainkan bungkus onigiri di jarinya lalu mengangguk kecil."
        moeka "Kosku aman kok, nggak ada apa-apa. Cuma kadang duduk dua jam di bawah lampu toko serba ada itu rasanya jauh lebih gampang daripada pulang buka pintu kamar terus langsung berhadapan sama tumpukan struk tagihan dan tugas yang belum kelar."
    elif _return == "C":
        if kk_host == "chiasa":
            chiasa "Haha, keren juga gaya hidup anak malam nongkrong di toko serba ada jam tiga pagi, Moemoe-senpai!"
        else:
            yutaka "Wah, jangan-jangan ini gaya hidup baru selebritas toko serba ada ya, Kohinata?"
        moeka "Hahaha, bener banget! Nanti kita bikin sesi pemotretan edisi spesial di samping rak minuman dingin ya!"
        nar "Kamu menimpali candaannya, dan Moeka segera menyuguhkan lelucon demi lelucon seperti biasa. Alasan sebenarnya mengapa ia terdampar di sudut itu kembali tenggelam di balik tawa yang rapi."
    else:
        if kk_host == "chiasa":
            chiasa "Sudah hampir pagi, Moemoe-senpai. Kalau onigirinya sudah habis, yuk aku antar jalan pulang sampai depan kos biar nggak jalan sendirian."
        else:
            yutaka "Habiskan dulu onigirinya, Kohinata. Habis ini kuantar sampai depan kos, jalanan jam segini sepi sekali."
        nar "Moeka mengangguk pelan tanpa menolak. Sepanjang jalan pulang kalian tidak banyak bicara, lalu di depan pintu gerbang kosnya ia berhenti sejenak dan menatapmu dengan mata jauh lebih tenang."
        moeka "Terima kasih ya sudah mengantar sampai sini. ...Besok aku mau coba hubungi Ryena deh. Kayaknya ada beberapa hal yang sudah kelamaan kubilang nanti saja."
    return

# ┌─ PANDUAN CERITA · Mo-D02 · Panggilan Empat Detik
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kohinata Moeka
# │ AWALAN  : tahap ≥ 2; Larut
# │ INTI    : A Telepon balik sekarang / B kirim pesan / C besok saja
# │ AKHIRAN : jendela kecil; andalan ±
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo_D02:
    call kk_scene_enter("moeka", "Layar ponsel")
    nar "Panggilan Moeka hanya bertahan empat detik. Sebelum tanganmu sampai ke layar, ia sudah menutup. Tak lama muncul pesan bahwa tadi salah menekan, disertai stiker tertawa yang sangat akrab."
    call kk_family_menu("Mo-D02", ["Telepon balik sekarang.", "Kirim pesan menanyakan kabar.", "Besok saja, mungkin tidak penting."])
    if _return == "A":
        moeka "Kau menelepon balik? ...Tidak, tidak ada apa-apa. Aku cuma... senang kau mengangkat."
        nar "Kau mengatakan bisa mendengar sebentar jika ia ingin bicara. Napas di seberang goyah, kemudian ia meminta ditemani sampai bisa menyebut apa yang membuat malamnya terasa berat."
    elif _return == "B":
        moeka "Maaf, salah pencet. Sungguh. Tidurlah."
        nar "Kau mengirim pesan lagi bahwa ia boleh mengatakan jika butuh sesuatu. Balasannya datang lebih lambat, berterima kasih tanpa membuka seluruh cerita. Jalan untuk berbicara tetap ada, meski malam itu belum dipakai."
    else:
        nar "Kau menunggu besok. Pagi hari Moeka sudah kembali mengirim cerita biasa, dan panggilan itu tampak mudah dilewatkan sebagai salah tekan."
        nar "Ia tidak menanyakan mengapa kau tidak menghubungi. Kebutuhan yang nyaris disampaikan semalam kini harus menemukan keberanian baru untuk muncul."
    return

# ┌─ PANDUAN CERITA · Mo-D03 · Kostum untuk Hinari
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kohinata Moeka
# │ AWALAN  : adik bungsunya ikut pentas sekolah
# │ INTI    : A Datang ke pentas / B bantu menjahit malam itu / C tidak bisa
# │ AKHIRAN : stres_total turun karena bahagia; keluarga mengenal pemain
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo_D03:
    call kk_scene_enter("moeka", "Kos Moeka · Mesin jahit")
    nar "Di kamar kos Moeka yang sempit tapi hangat, potongan kain satin kuning pucat, jarum pentul, dan gulungan benang berserakan rapi di sekitar mesin jahit portabelnya. Moeka sedang membungkuk tekun menjahit kostum mungil untuk pentas sekolah adik bungsunya, Hinari."
    if kk_host == "chiasa":
        chiasa "Lucu banget bentuknya, Moemoe-senpai! Itu buat pementasan sekolahnya Hinari ya?"
        moeka "Iya, Chimian! Hinari dapat peran jadi bintang. Maksudku bintang sungguhan yang pakai lima sudut di panggung ya, haha! Dia bahkan sudah ngancam mau ngadu ke Ibu kalau lima sudutnya nggak sama panjang!"
    else:
        yutaka "Kamu jahit kostum anak kecil dari nol begini, Kohinata? Kelihatannya niat sekali."
        moeka "Iya dong, Yutayuta! Hinari dapat peran jadi bintang buat pentas sekolahnya. Bintang beneran bersudut lima di atas panggung! Dia sudah ngancam bakal lapor ke Ibu kalau ujung bintangnya ada yang miring sebelah, haha!"
    nar "Moeka tertawa lepas, dan kali ini tawa itu datang sepenuhnya dari rasa geli yang tulus. Di tengah segala beban yang menuntutnya terus kuat, antusiasme adiknya memberinya satu pekerjaan yang sungguh ingin ia kerjakan dengan sukarela."
    call kk_family_menu("Mo-D03", ["Datang menonton pentasnya.", "Bantu menjahit malam ini.", "Kali ini aku tidak bisa."])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Kapan pentasnya, Moemoe-senpai? Aku boleh ikut datang nonton Hinari tampil nggak?"
            moeka "Eh, Chimian beneran mau datang?! Wah, Hinari pasti langsung heboh pamer ke teman-temannya... dan jujur aja, aku juga senang banget kalau kamu ikut!"
        else:
            yutaka "Pentasnya hari apa, Kohinata? Kalau jadwalku cocok, aku mau datang ikut nonton Hinari tampil."
            moeka "Serius nih Yutayuta mau datang ke pentas anak SD?! Hinari pasti heboh banget... aku sendiri juga senang banget dengarnya!"
        nar "Ia langsung menyebutkan hari dan lokasi aula sekolah sambil mengingatkan bahwa acara anak-anak tidak pernah tepat jadwal. Pada hari pentas tiba, Moeka akhirnya bisa bertepuk tangan santai menikmati panggung tanpa sibuk terus mengarahkan kamera karena kamu membantunya merekam kenangan itu."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Sini, bagian kelim pinggir yang lurus biar aku bantu jahit tangan ya, Moemoe-senpai, biar cepat selesai malam ini."
            moeka "Wah, dikerjain berdua langsung ngebut jadinya! Eh, lihat deh, Chimian ternyata rapi banget lho megang jarumnya!"
        else:
            yutaka "Ada bagian gampang yang bisa kubantu nggak, Kohinata? Pasang jarum pentul atau jahit sisi lurusnya biar cepat kelar."
            moeka "Boleh banget! ...Wah, ternyata Yutayuta nggak payah-payah amat lho pegang jarum, lumayan lurus nih jahitannya!"
        nar "Kamu menangani bagian-bagian sederhana dan menyerahkan sudut rumit ke tangan cekatan Moeka. Kostum bintang itu rampung lebih cepat dengan sedikit perbedaan garis jahitan yang justru membuat Moeka tersenyum lega karena kali ini ada orang yang mau ikut repot bersamanya."
    else:
        if kk_host == "chiasa":
            chiasa "Maaf ya, Moemoe-senpai, jadwal tugasku minggu ini lagi padat banget jadi belum bisa bantu banyak. Semangat ya jahitnya buat Hinari!"
        else:
            yutaka "Maaf, Kohinata, minggu ini jadwalku lagi bentrok jadi aku nggak bisa ikut datang atau bantu beresin malam ini."
        moeka "Oh, nggak apa-apa banget kok! Nanti begitu jadi langsung kukirimi fotonya waktu dipakai Hinari ya."
        nar "Ia kembali ke mesin jahit dengan senyum ceria yang biasa. Keesokan harinya foto kostum yang sudah sempurna masuk ke ponselmu, tanpa sebaris pun cerita betapa larut ia menuntaskan sudut terakhirnya sendirian."
    return

# ┌─ PANDUAN CERITA · Mo-D04 · Struk di Lantai
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kohinata Moeka
# │ AWALAN  : pemain di kos Moeka
# │ INTI    : A Tanya / B pura-pura tidak lihat / C diam-diam membayar sebagian
# │ AKHIRAN : pemain tahu soal ayah; pilihan "Tanya soal cuci darah ayah" terbuka
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo_D04:
    call kk_scene_enter("moeka", "Kos Moeka · Lantai")
    nar "Struk biaya perawatan jatuh ketika Moeka mengambil gunting. Ada tanggal berulang dan jumlah yang lebih besar daripada sisa anggaran di catatan belanjanya. Ia melihat matamu berhenti pada kertas itu, lalu menanyakan apakah kau ingin minum."
    call kk_family_menu("Mo-D04", ["Tanyakan soal struk itu.", "Pura-pura tidak melihatnya.", "Diam-diam niatkan membayar sebagian."])
    if _return == "A":
        moeka "...Itu punya ayah. Ginjalnya. Setiap minggu, terus begitu. Sekarang kau tahu kenapa aku selalu butuh kerja."
        nar "Ia menjelaskan perawatan yang terus berjalan dan penghasilan keluarga yang tidak lagi sama. Kau menanyakan dukungan apa yang sudah diurus, memberi ruang agar bantuan tidak selalu berarti ia harus mengambil pekerjaan lebih banyak."
    elif _return == "B":
        nar "Kau mengalihkan pandangan. Moeka menyimpan struk, lega karena belum perlu mempertemukan citra dirinya di kampus dengan masalah di rumah."
        nar "Ia melanjutkan cerita tentang desain. Ada bagian kehidupan yang kembali ia tanggung sendirian karena terlalu malu memulai tanpa ditanya."
    else:
        moeka "Kenapa kau tiba-tiba diam? ...Jangan macam-macam dengan uangmu untuk urusanku."
        nar "Kau menyimpan niat membantu tanpa membicarakan bentuknya. Moeka menangkap perubahan sikapmu dan meminta jangan membuat keputusan keuangan atas namanya."
        moeka "Kalau mau bantu, bicarakan denganku. Aku capek merasa ada sesuatu yang harus kubalas tapi nggak tahu kapan mulai berutang."
    return

# ┌─ PANDUAN CERITA · Mo-D05 · Lokasi dari Kuga
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kohinata Moeka
# │ AWALAN  : kuga_tekanan ≥ 40
# │ INTI    : A Temani / B larang / C laporkan / D minta Ryena menemani
# │ AKHIRAN : jalur Kuga; bukti untuk E-NPC-26
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo_D05:
    call kk_scene_enter("moeka", "Pesan dari Kuga")
    nar "Kuga mengirim lokasi pemotretan malam. Moeka memperlihatkan layarnya, ragu."
    moeka "Bayarannya besar. Aku ingin kerja, tapi aku juga ingin bisa pulang kalau yang diminta berbeda dari yang disepakati. Kamu mau menemani? Atau kita cari orang lain yang bisa. Aku nggak ingin berpura-pura berani sendirian."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", KK_DYN_BY_ID["Mo-D05"]["choices"])]
    call screen kk_choice_panel(_rows, "Tawaran Kuga")
    $ kk_record_choice("Mo-D05", _return)
    if _return == "A":
        nar "Kau ikut sesuai persetujuan Moeka. Kuga mengubah nada ketika tahu ada orang lain mendengar rincian pekerjaan. Moeka mengajukan pertanyaan yang tadi hampir ditelannya dan mempertahankan batas yang telah ditentukan."
    elif _return == "B":
        moeka "Kau melarangku? ...Mudah untukmu bilang begitu. Tapi baik, kali ini aku dengar."
        nar "Ia menunda, lalu meminta kalian juga membicarakan penghasilan yang hilang. Melindunginya tidak cukup jika hanya berhenti pada larangan dan meninggalkan kebutuhan yang membuat tawaran tersebut terasa perlu."
    elif _return == "C":
        nar "Kau membantu melaporkan kekhawatiran berdasarkan pesan yang benar-benar ada, bukan cerita tambahan untuk membuatnya terdengar lebih buruk. Moeka meminta tahu siapa yang akan menerima laporan dan bagaimana keterangannya dipakai."
        moeka "Aku ingin dibantu tanpa kehilangan suara dalam ceritaku sendiri. Tolong terus kabari aku."
    else:
        moeka "Ryena yang menemani? ...Boleh. Dia tidak akan membiarkanku ceroboh."
        nar "Ryena bersedia dan langsung menanyakan rincian kepada Moeka. Ketika keduanya menyusun rencana bersama, ketakutan yang tadi disembunyikan mulai berubah menjadi pertanyaan yang dapat diucapkan dengan jelas."
    return

# ┌─ PANDUAN CERITA · Mo-D06 · Ulang Tahun yang Ia Lupakan
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kohinata Moeka
# │ AWALAN  : hari ulang tahunnya; stres_total ≥ 50
# │ INTI    : A kejutan kecil / B pesta besar / C kue di depan pintu
# │ AKHIRAN : kecil: topeng −; pesta besar: topeng +
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo_D06:
    call kk_scene_enter("moeka", "Hari ulang tahun Moeka")
    nar "Sambil mencoret angka di kalender saku kecilnya, Moeka menyebut tanggal hari ini dengan nada datar sebagai batas akhir transfer uang belanja ke rumah. Ia baru berhenti bicara dan mengerjap kaget ketika kamu tetap diam menatapnya sambil menunggu kelanjutan kalimat."
    if kk_host == "chiasa":
        chiasa "...Moemoe-senpai, tanggal hari ini bukannya ulang tahun Senpai sendiri?"
        moeka "Eh... oh! Astaga, bener juga, Chimian! Harusnya aku sudah siapin pidato keren soal tambah dewasa ya, padahal dari pagi otakku cuma muter ngitung ongkos kereta pulang sama transferan rumah."
    else:
        yutaka "Kohinata, kamu sadar nggak tanggal yang baru saja kamu lingkari itu hari ulang tahunmu sendiri?"
        moeka "Eh... hah?! Bener juga, Yutayuta! Lucu banget, harusnya aku punya rencana merayakan tambah umur, tapi kepalaku dari pagi cuma ingat tanggal kirim uang."
    call kk_family_menu("Mo-D06", ["Kejutan kecil berdua saja.", "Pesta besar dengan teman-teman.", "Tinggalkan kue di depan pintunya."])
    if _return == "A":
        nar "Kamu mengajak Moeka duduk di bangku tenang lalu mengeluarkan satu potong kue stroberi kecil dan sebatang lilin sederhana yang sempat kamu siapkan."
        if kk_host == "chiasa":
            chiasa "Selamat ulang tahun ya, Moemoe-senpai. Nggak usah ada pidato keren, cukup duduk makan kue santai aja berdua."
        else:
            yutaka "Selamat ulang tahun, Kohinata. Nggak usah mikirin ongkos atau jadwal dulu buat tiga puluh menit ke depan."
        moeka "Cuma kita berdua sama kue sekecil ini... aneh ya, kenapa justru yang begini yang bikin mataku mendadak panas mau nangis?"
        nar "Kamu membiarkan air mata di sudut matanya jatuh perlahan tanpa buru-buru memintanya tersenyum ke arah kamera. Ia menyendok kue itu pelan, menikmati satu perayaan yang tidak menuntutnya tampil ceria untuk siapa-siapa."
    elif _return == "B":
        nar "Kamu menghubungi beberapa teman kampus agar berkumpul dadakan menyambut ulang tahun Moeka dengan balon dan kue besar. Begitu ia membuka pintu, suara ucapan serentak langsung memenuhi ruangan."
        moeka "Wah, ramai sekali! Terima kasih banyak semuanya... haha, aku jadi tersenyum terus dari tadi! Senyum itu memang keahlian utamaku kan!"
        nar "Ia langsung sigap menyambut setiap tamu, membantu memotong kue, dan berpose ceria untuk semua kamera. Baru setelah seluruh ruangan kembali sepi dan sampah dibereskan, ia duduk sendirian dan sadar belum sempat memilih satu pun hal yang sungguh ia inginkan untuk dirinya hari ini."
    else:
        nar "Kamu menaruh kotak kue mungil beserta kartu ucapan singkat di depan pintu kamar kosnya lalu mengabari lewat pesan singkat agar ia langsung mengambilnya."
        play sound "audio/sfx/phone_buzz.wav"
        "Pesan Moeka" "Wah, kuenya sudah kuambil! Enak banget kelihatannya, makasih banyak sudah ingat hari ulang tahunku!"
        nar "Moeka memotret kue itu dan memakannya sendiri di meja kecilnya tanpa harus repot memasang senyum untuk tamu. Meski begitu, di tengah kamar yang hening malam itu ia sempat berharap ada suara langsung seseorang yang bisa ia dengar sambil meniup lilinnya."
    return

# ┌─ PANDUAN CERITA · Mo-D07 · Ryena Bertanya
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kohinata Moeka
# │ AWALAN  : rina_curiga ≥ 50
# │ INTI    : A "Kamu tahu sesuatu?" Jujur / B sangkal / C ajak bekerja sama
# │ AKHIRAN : Ryena menjadi sekutu; kesempatan kedua di Mo25
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo_D07:
    call kk_scene_enter("moeka", "Ryena mencegatmu")
    nar "Ryena, sahabat Moeka sejak kecil, menunggumu dengan wajah serius."
    "Ryena" "Aku nggak minta rahasia untuk dibicarakan orang. Aku khawatir, dan aku ingin tahu siapa yang benar-benar bisa menghubunginya malam ini. Kamu melihat perubahan juga?"
    call kk_family_menu("Mo-D07", ["Jujur, dan bagi apa yang kau tahu.", "Sangkal, ini bukan urusanmu.", "Ajak Ryena bekerja sama menjaganya."])
    if _return == "A":
        "Ryena" "...Jadi aku tidak salah lihat. Baik. Sekarang kita berdua yang jaga."
        nar "Kau membagikan pengamatan secukupnya untuk membantu, membedakan kekhawatiran dari fakta. Ryena menyebut perlunya menghubungkan Moeka dengan orang yang mampu memberi dukungan lebih jauh daripada kalian berdua."
    elif _return == "B":
        "Ryena" "Begitu. Kupikir kau peduli. Ternyata aku salah orang."
        nar "Ia menutup percakapan dan mencari jalan lain. Penyangkalanmu tidak membuat perubahan Moeka hilang; hanya membuat Ryena semakin enggan mempercayakan kabar berikutnya kepadamu."
    else:
        "Ryena" "Kita bagi tugas. Kalau salah satu melihat dia retak, yang lain datang. Setuju?"
        nar "Kalian menambahkan nama orang lain yang bisa dihubungi dan sepakat menanyakan kebutuhan Moeka sendiri. Menjaga bukan berarti mengawasi setiap langkahnya, melainkan memastikan ia tak kehilangan semua pintu ketika satu orang sedang tak bisa datang."
    return

# ┌─ PANDUAN CERITA · Mo-D08 · Formulir Banding
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kohinata Moeka
# │ AWALAN  : beasiswa diperingatkan; kenal Fujisawa
# │ INTI    : A bantu menulis surat banding malam itu / B suruh ia menulis sendiri / C bayar orang lain
# │ AKHIRAN : E-MO-09 menguat; membayar orang lain = kebohongan baru
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo_D08:
    call kk_scene_enter("moeka", "Kos Moeka · Formulir")
    nar "Surat peringatan beasiswa. Nilai Moeka turun karena terlalu banyak kerja; ia harus menulis banding malam ini juga."
    moeka "Aku harus menjelaskan kenapa nilaiku turun tanpa terdengar mencari alasan. Tiap menulis soal rumah, aku malah merasa sedang memakai Ayah supaya mereka kasihan. Aku nggak tahu bagaimana membuat kebenaran terdengar boleh dikatakan."
    call kk_family_menu("Mo-D08", ["Bantu menulis surat banding malam ini.", "Suruh ia menuliskannya sendiri.", "Tawarkan membayar orang menulisnya."])
    if _return == "A":
        moeka "Kau menemaniku sampai pagi untuk ini... Aku tidak akan lupa."
        nar "Kau membantunya menyusun keterangan yang ia putuskan sendiri. Kalian tidak menjanjikan hasil, hanya memastikan bandingnya tidak gugur karena ia terlalu lelah untuk menyelesaikan satu halaman."
    elif _return == "B":
        moeka "Kau benar. Ini tanganku yang harus menulisnya. ...Aku bisa."
        nar "Ia memulai sendiri, satu paragraf demi satu paragraf. Bantuanmu terbatas pada mengingatkan apa yang perlu ditanyakan kepada pengelola beasiswa; isi surat tetap memperlihatkan suara yang selama ini lebih sering dipakai menenangkan orang lain."
    else:
        moeka "Membayar orang? ...Itu kebohongan baru di atas yang lama. Tidak. Jangan begitu."
        nar "Ia mengembalikan formulir ke depannya. Tawaranmu membuat jalan keluar tampak cepat, tetapi untuk kali ini ia ingin keterangannya dapat diakui sebagai miliknya ketika nanti harus menjelaskannya lagi."
    return

# ┌─ PANDUAN CERITA · Mo-D09 · Cocok sebagai Donor
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kohinata Moeka
# │ AWALAN  : ayah memburuk
# │ INTI    : A Dukung / B tentang / C beri tahu Yaeka / D temani ke RS (Miyuki melihat)
# │ AKHIRAN : cabang donor; stres[[ayah] −40 bila jadi; beasiswa terancam
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo_D09:
    call kk_scene_enter("moeka", "Rumah Sakit · Lorong")
    nar "Ayah Moeka memburuk. Diam-diam Moeka menjalani tes kecocokan donor, tanpa memberi tahu keluarganya."
    moeka "Aku menjalani pemeriksaan kecocokan. Belum berarti keputusan sudah selesai, aku tahu. Tapi tiap dokter bilang masih ada yang harus dipertimbangkan, kepalaku langsung berteriak Ayah nggak punya waktu."
    nar "Ia belum memberitahu keluarga, takut seluruh pembicaraan akan berakhir dengan orang lain melarang sebelum sempat mendengar."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", KK_DYN_BY_ID["Mo-D09"]["choices"])]
    call screen kk_choice_panel(_rows, "Keputusan Moeka")
    $ kk_record_choice("Mo-D09", _return)
    if _return == "A":
        moeka "Kau mendukungku? ...Terima kasih. Setidaknya satu orang tidak menyuruhku berhenti."
        nar "Kau mendukung haknya mempertimbangkan, bukan menekan agar benar-benar menjadi donor. Moeka mulai menanyakan waktu pemulihan dan studinya sendiri, hal-hal yang semula ingin dianggap tidak penting agar tidak merasa egois."
    elif _return == "B":
        moeka "Kamu menentang? Aku tahu ada risiko dan banyak hal harus diperiksa. Tapi ini Ayah. Aku ingin didengar sebelum diputuskan tidak sanggup."
        nar "Ia tetap bersedia mendengar kekhawatiranmu jika kau tidak mengubahnya menjadi penilaian bahwa kasih sayangnya tidak masuk akal."
    elif _return == "C":
        nar "Kau memberi tahu Yaeka, ibu Moeka. Kabar itu membuatnya menangis sebelum menanyakan bagaimana putrinya menjalani semua ini sendirian."
        "Yaeka" "Aku ingin dengar dari Moeka. Tolong bilang Ibu tidak marah karena dia bertanya tentang pilihan itu. Ibu hanya tidak ingin dia merasa hidupnya boleh dihabiskan tanpa ikut dipikirkan."
    else:
        nar "Kau menemaninya ke rumah sakit dan menunggu selama pemeriksaan yang perlu dijalani. Miyuki melihat kalian di koridor, menyapa tanpa meminta rincian yang bukan haknya."
        miyuki "Semoga pembicaraannya membantu kamu memahami pilihanmu. Kalau perlu istirahat, ruang tunggunya ada di sana."
        nar "Moeka tersenyum kecil, lega ada orang yang memandangnya sebagai seseorang yang juga perlu dirawat."
    return

# ┌─ PANDUAN CERITA · Mo-D10 · Tawa di Grup Jam Dua
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kohinata Moeka
# │ AWALAN  : topeng ≥ 70
# │ INTI    : A Balas candaan / B japri "kamu oke?" / C abaikan
# │ AKHIRAN : japri: andalan[[pemain] +, topeng −
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo_D10:
    call kk_scene_enter("moeka", "Grup chat · Jam dua pagi")
    nar "Pukul dua, Moeka menghidupkan grup dengan stiker dan cerita kecil. Ia tidak menanggapi pertanyaan tentang kapan tidur, hanya menambahkan candaan lain agar percakapan tetap bergerak menjauh dari dirinya."
    call kk_family_menu("Mo-D10", ["Balas candaannya di grup.", "Japri: “kamu oke?”", "Abaikan, ia hanya iseng."])
    if _return == "A":
        nar "Kau membalas candaan dan grup semakin ramai. Moeka mendapat alasan terus mengetik daripada menghadapi malam yang sunyi. Ketika yang lain tidur satu per satu, ia masih mencari sesuatu yang bisa dijadikan pesan berikutnya."
    elif _return == "B":
        moeka "Kenapa justru kamu yang nanya pelan begitu... Aku oke. ...Mungkin tidak terlalu. Boleh cerita sedikit?"
        nar "Kau mengatakan boleh dan menunggu. Ceritanya datang terpotong, tidak lucu, dan beberapa kali dihapus. Kau tetap membaca sampai ia berani mengirim bagian yang paling membuatnya malu."
    else:
        nar "Kau tidak merespons. Besok Moeka memakai cerita grup itu untuk membuktikan malamnya menyenangkan. Tidak ada yang tahu ia terjaga lebih lama setelah percakapan selesai, tanpa satu pun rencana tentang bagaimana meminta ditemani secara langsung."
    return

# ┌─ PANDUAN CERITA · Mo-D11 · Barang yang Dikembalikan
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kohinata Moeka
# │ AWALAN  : tahap 4
# │ INTI    : A Tanya kenapa / B terima / C ceritakan pada Ryena
# │ AKHIRAN : tanda bahaya; menerima tanpa bertanya = jendela kecil terlewat
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo_D11:
    call kk_scene_enter("moeka", "Barang yang dikembalikan")
    nar "Buku dan syalmu dikembalikan bersama catatan kecil bahwa tidak ada lagi barang yang tertinggal padanya. Moeka menanyakan sekali apakah masih punya utang lain, lalu tertawa agar pertanyaan itu terdengar santai."
    call kk_family_menu("Mo-D11", ["Tanyakan kenapa mengembalikannya sekarang.", "Terima saja tanpa banyak tanya.", "Ceritakan hal ini pada Ryena."])
    if _return == "A":
        moeka "Kenapa sekarang? ...Entah. Rasanya aku ingin semua beres. Jangan dibesar-besarkan, ya."
        nar "Kau bertanya lebih jauh tentang keadaan dan keselamatannya. Ia mencoba mengalihkan, kemudian menyerah pada kalimat sederhana bahwa kau khawatir dan ingin tetap bersamanya mencari bantuan."
    elif _return == "B":
        nar "Kau menerima barang tanpa menanyakan perubahan itu. Moeka memastikan catatannya ikut masuk tasmu, lalu mengucapkan terima kasih karena selama ini sudah baik."
        nar "Kata selama ini tinggal lebih lama daripada ucapan pamit. Kau belum menentukan apakah keganjilan yang terdengar layak ditanyakan kembali."
    else:
        nar "Kau menghubungi Ryena malam itu, menceritakan pengembalian barang dalam konteks perubahan yang sudah kalian lihat. Ryena tidak menganggap satu benda sebagai kepastian tentang niat Moeka; ia menganggap keseluruhan kabar cukup serius untuk segera mencari dan menghubunginya."
    return

# ┌─ PANDUAN CERITA · Mo-D12 · Pertanyaan Langsung
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kohinata Moeka
# │ AWALAN  : tahap ≥ 3; pemain mengenali tanda (Intim ≥ 55 atau Ryena memberi tahu)
# │ INTI    : A Tanya langsung lalu tetap tinggal / B tanya sambil bercanda / C tidak berani
# │ AKHIRAN : tanya langsung: ia menangis dan bercerita; jendela diambil; jalan ke Sato Kyoko dan bantuan profesional terbuka
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo_D12:
    call kk_scene_enter("moeka", "Kos Moeka · Pertanyaan tenang")
    nar "Kau tidak tahu seluruh yang ada di kepala Moeka. Kau tahu ada penarikan diri, barang yang diberikan, dan kelelahan yang tidak lagi bisa ditutupi kabar biasa. Duduk di depannya, pertanyaan yang ditakuti akhirnya lebih penting daripada menjaga percakapan terasa ringan."
    call kk_family_menu("Mo-D12", ["Tanya langsung, lalu tetap di sisinya.", "Tanya sambil bercanda agar ringan.", "Tidak berani mengucapkannya."])
    if _return == "A":
        moeka "...Kau menanyakannya. Benar-benar menanyakannya."
        moeka "Aku lelah. Lelah sekali. Aku tidak tahu sampai kapan aku masih kuat."
        nar "Kau bertanya jelas apakah ia sedang memikirkan bunuh diri. Ia menangis, lalu mengatakan ada saat ketika ia takut tak akan mampu menjaga keselamatannya sendiri. Kau mendengarkan tanpa memarahinya atau meminta janji demi membuatmu tenang."
        nar "Ia menangis untuk pertama kalinya tanpa topeng. Kau tetap di sana. Esoknya, bersama Ryena, kau menghubungkan Moeka ke Sato Kyoko — konselor kampus — dan untuk pertama kalinya beban itu tidak ditanggung sendirian."
        nar "Jika keselamatannya tidak bisa menunggu, bantuan dicari malam itu juga. Kehadiranmu menjadi bagian dari dukungan, bukan pengganti seluruh pertolongan yang ia perlukan."
    elif _return == "B":
        moeka "Hahaha, kau ini... Sudah, jangan serius-serius. Aku baik-baik saja."
        nar "Candaan itu membuat pertanyaannya meleset. Moeka tetap tersenyum, dan kesempatan itu lewat."
        nar "Ia menerima jalan untuk mengatakan tidak ada apa-apa, lega sesaat karena tidak perlu membuatmu takut. Justru bagian yang hendak kautanyakan kembali tersimpan di tempat yang tak bisa dilihat dari senyumnya."
    else:
        nar "Kata-kata tertahan di tenggorokanmu. Moeka menanyakan apakah ada hal lain, lalu membuat teh agar tidak perlu duduk di dalam keheningan yang terasa mengancam."
        nar "Kau berada cukup dekat untuk mendengar, tetapi pertanyaan itu belum sampai. Ketidaktahuan tentang jawaban tidak membuat kekhawatiranmu pergi."
    return

# ┌─ PANDUAN CERITA · Mo-D13 · Sketsa Label Pertama
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Kohinata Moeka
# │ AWALAN  : stres_total < 40; Aff ≥ 55
# │ INTI    : A Dukung / B ajak Ryena / C kritik
# │ AKHIRAN : E-MO-08 menguat
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo_D13:
    call kk_scene_enter("moeka", "Kantin Pusat · Sketsa label")
    nar "Beban keluarga sedikit mereda, dan ada warna yang kembali. Moeka menunjukkan rancangan label merek kecilnya sendiri."
    moeka "Aku ingin label kecil. Belum bisnis besar, jangan langsung minta diskon seumur hidup. Untuk pertama kali setelah lama, aku menggambar sesuatu yang ingin kulihat jadi nyata, bukan cuma yang paling cepat bisa dijual."
    call kk_family_menu("Mo-D13", ["Dukung sepenuh hati.", "Ajak Ryena ikut melihat.", "Beri kritik jujur agar lebih baik."])
    if _return == "A":
        moeka "Kau pikir ini bisa jalan? ...Aku juga mulai percaya begitu."
        nar "Kau menanyakan desain pertama dan siapa yang dibayangkan akan memakainya. Moeka mulai bercerita sampai lupa merendahkan rencananya sebelum orang lain sempat menilai."
    elif _return == "B":
        nar "Ryena ikut melihat dan langsung menanyakan ruang kerja. Kalian membicarakan jumlah kecil, waktu yang realistis, dan apa yang tidak boleh dikorbankan lagi. Moeka tertawa ketika impiannya mulai mendapat ukuran yang dapat dikerjakan."
    else:
        moeka "Kritikmu pedas. ...Tapi kau benar. Aku akan perbaiki garis ini. Terima kasih sudah menganggapnya serius."
        nar "Ia menanyakan alasan di balik komentarmu, menolak satu bagian dan menerima yang lain. Rencana itu cukup miliknya untuk dibela, cukup terbuka untuk diperbaiki tanpa membuat seluruh harga dirinya ikut dipertaruhkan."
    return

init 1 python:
    _hook("Mo-D01-A", lambda: (kk_moeka_rely(6), kk_rel("moeka","intim",3)))
    _hook("Mo-D01-B", lambda: (kk_moeka_burden(4), kk_rel("moeka","trust",3)))
    _hook("Mo-D01-C", lambda: kk_moeka_mask(5))
    _hook("Mo-D01-D", lambda: (kk_moeka_rely(4), kk_rel("moeka","aff",3)))
    _hook("Mo-D02-A", lambda: (kk_moeka_rely(6), kk_rel("moeka","trust",3)))
    _hook("Mo-D02-B", lambda: kk_rel("moeka","aff",2))
    _hook("Mo-D02-C", lambda: kk_moeka_mask(4))
    _hook("Mo-D03-A", lambda: (kk_rel("moeka","aff",5), kk_flag("moeka_adik_dikenal"), kk_adj("stres_moeka",-8)))
    _hook("Mo-D03-B", lambda: (kk_rel("moeka","intim",5), kk_flag("moeka_adik_dikenal")))
    _hook("Mo-D03-C", lambda: kk_moeka_burden(3))
    _hook("Mo-D04-A", lambda: (kk_flag("moeka_ayah_diketahui"), kk_rel("moeka","trust",5)))
    _hook("Mo-D04-B", lambda: kk_moeka_mask(4))
    _hook("Mo-D04-C", lambda: kk_rel("moeka","trust",-4))
    _hook("Mo-D05-A", lambda: (kk_flag("kuga_dihalangi"), kk_rel("moeka","trust",5)))
    _hook("Mo-D05-B", lambda: (kk_rel("moeka","trust",3), kk_adj("kuga_tekanan",-10)))
    _hook("Mo-D05-C", lambda: kk_flag("bukti_kuga_terkumpul"))
    _hook("Mo-D05-D", lambda: (kk_flag("kuga_dihalangi"), kk_flag("rina_sekutu")))
    _hook("Mo-D06-A", lambda: (kk_moeka_mask(-8), kk_rel("moeka","intim",5)))
    _hook("Mo-D06-B", lambda: kk_moeka_mask(6))
    _hook("Mo-D06-C", lambda: kk_rel("moeka","aff",3))
    _hook("Mo-D07-A", lambda: (kk_flag("rina_sekutu"), kk_adj("rina_curiga",10)))
    _hook("Mo-D07-B", lambda: kk_rel("moeka","trust",-3))
    _hook("Mo-D07-C", lambda: (kk_flag("rina_sekutu"), kk_flag("moeka_intervensi_1")))
    _hook("Mo-D08-A", lambda: (kk_flag("moeka_beasiswa_dibantu"), kk_rel("moeka","intim",5)))
    _hook("Mo-D08-B", lambda: (kk_rel("moeka","trust",4), kk_adj("stres_moeka",-5)))
    _hook("Mo-D08-C", lambda: kk_moeka_mask(5))
    _hook("Mo-D09-A", lambda: (kk_rel("moeka","intim",5), kk_flag("moeka_ayah_diketahui"), kk_flag("moeka_donor_didampingi")))
    _hook("Mo-D09-B", lambda: kk_rel("moeka","trust",3))
    _hook("Mo-D09-C", lambda: (kk_flag("moeka_keluarga_diketahui"), kk_flag("moeka_intervensi_1")))
    _hook("Mo-D09-D", lambda: (kk_flag("moeka_ayah_diketahui"), kk_flag("miyuki_lihat_moeka"), kk_flag("moeka_donor_didampingi")))
    _hook("Mo-D10-A", lambda: kk_moeka_mask(5))
    _hook("Mo-D10-B", lambda: (kk_moeka_rely(6), kk_moeka_mask(-6), kk_rel("moeka","intim",3)))
    _hook("Mo-D10-C", lambda: kk_moeka_mask(4))
    _hook("Mo-D11-A", lambda: (kk_flag("moeka_tanda_bahaya_dibaca"), kk_rel("moeka","trust",4)))
    _hook("Mo-D11-B", lambda: kk_moeka_mask(4))
    _hook("Mo-D11-C", lambda: (kk_flag("rina_sekutu"), kk_flag("moeka_tanda_bahaya_dibaca")))
    _hook("Mo-D12-A", lambda: (kk_flag("moeka_intervensi_1"), kk_flag("sato_kyoko_terlibat"), kk_rel("moeka","trust",8), kk_adj("stres_moeka",-15)))
    _hook("Mo-D12-B", lambda: kk_moeka_mask(4))
    _hook("Mo-D12-C", lambda: kk_moeka_burden(4))
    _hook("Mo-D13-A", lambda: (kk_rel("moeka","aff",5), kk_flag("moeka_jalan_keluar")))
    _hook("Mo-D13-B", lambda: (kk_flag("rina_sekutu"), kk_rel("moeka","aff",4)))
    _hook("Mo-D13-C", lambda: (kk_rel("moeka","trust",4), kk_flag("moeka_jalan_keluar")))
