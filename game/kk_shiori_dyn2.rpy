# Event dinamis Shiori tambahan (S-D01/02/05/06/10/11/12) — permainan baca-membaca,
# persekutuan melawan antagonis, dan titik-titik rawan. Konsekuensi + karakter.

# ┌─ PANDUAN CERITA · S-D01 · Langkah Jam Dua Belas
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : pemain tahu jam online Shiori
# │ INTI    : A main serius / B ajak bicara di chat / C log off tiba-tiba
# │ AKHIRAN : akun_anonim +; log off tiba-tiba membuatnya curiga
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S_D01:
    call kk_scene_enter("shiori", "Papan catur daring · Jam dua belas")
    nar "Tepat pukul dua belas malam, jendela situs catur daring di layarmu memunculkan bunyi notifikasi tantangan baru. Nama pengguna anonim yang pola pembukaannya sudah sangat kamu kenali itu baru saja masuk ke meja permainan."
    nar "Di koridor kampus, Shiori selalu bisa menutup jarak dengan satu senyum sopan. Di atas papan daring tanpa wajah ini, yang tersisa hanyalah rangkaian langkah tajam yang menuntut jawaban sama seriusnya."
    "Chat Lawan" "Selamat malam. Masih mau satu partai cepat sebelum tidur?"
    call kk_family_menu("S-D01", ["Main serius sampai tuntas.", "Ajak bicara lewat kolom chat.", "Log off tiba-tiba."])
    if _return == "A":
        nar "Kamu membalas tantangan itu dengan pembukaan agresif tanpa sekali pun memancing hal-hal yang hanya kamu ketahui dari kampus. Setiap pertukaran perwira berjalan ketat hingga menit terakhir sebelum akhirnya papan menemui jalan buntu yang menegangkan."
        "Chat Lawan" "Langkah kuda di giliran dua puluh empat barusan sungguh nggak terduga. Lawan kali ini berbeda sekali dari pemain yang biasa kutemui, sampai bikin aku lupa jam. Siapa kamu sebenarnya?"
        if kk_host == "chiasa":
            chiasa "Cuma seseorang yang kebetulan senang belajar membaca langkah dari lawan yang jauh lebih jago. Terima kasih partainya."
        else:
            yutaka "Anggap saja sesama orang yang belum bisa tidur tengah malam. Permainan yang sangat rapi."
        "Chat Lawan" "Menarik. Kalau jam dua belas malam lain hari kamu senggang lagi, aku kirim tantangan ulang ya."
        nar "Di akhir partai, akun itu mengirim permintaan tanding ulang untuk malam berikutnya, tertarik pada sosok di balik layar yang bahkan belum diberi nama."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Langkah pembukaannya kelihatan lebih cepat dari biasanya malam ini. Lagi ada hari yang lumayan melelahkan ya?"
        else:
            yutaka "Tempo mainmu agak lebih terburu-buru dari minggu lalu. Hari ini baru melewati urusan yang bikin capek ya?"
        nar "Bidak putih di layar sempat diam hampir setengah menit sebelum kolom obrolan berkedip."
        "Chat Lawan" "Kamu mengajakku ngobrol di tengah-tengah partai catur? Berani juga ya... anehnya aku malah suka itu."
        "Chat Lawan" "Yah, anggap saja hari ini terlalu banyak orang yang cuma bicara dengan nama keluargaku alih-alih mendengarkan aku sendiri. Di sini lumayan lega rasanya karena nggak ada yang peduli latar belakang siapa pun."
        nar "Obrolan pelan bergulir di antara langkah-langkah bidak tanpa pernah menyebut nama kampus ataupun keluarga. Malam itu kamu mendengarkan sisi diri Shiori yang jauh lebih santai sebelum reputasinya ikut masuk ke ruangan."
    else:
        nar "Begitu giliranmu tiba di langkah kelima, kamu langsung menutup peramban dan keluar dari akun tanpa mengetik sepatah kata pun."
        nar "Di seberang layar, Shiori menunggu hitungan mundur waktu hingga habis sebelum menutup papan dengan kening berkerut, tidak tahu apakah koneksi lawannya terputus atau ia baru saja sengaja ditinggalkan. Lain kali ia akan membaca setiap detail lebih waspada sebelum membuka ruang obrolan yang sama."
    return

# ┌─ PANDUAN CERITA · S-D02 · Kuroiwa di Parkiran
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : kuroiwa_percaya ≥ 50, atau marah[[pemain] ≥ 40
# │ INTI    : A Jujur / B menghindar dengan sopan / C tanya soal Shiori
# │ AKHIRAN : Kuroiwa menjadi saluran peringatan
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S_D02:
    call kk_scene_enter("shiori", "Parkiran · Kuroiwa mendekat")
    nar "Kuroiwa menutup pintu mobil setelah memastikan Shiori sudah menuju ruang acara. Ia menyapamu tanpa menghalangi jalan, sikap seseorang yang ingin bertanya jelas alih-alih mengandalkan ukuran tubuh untuk membuatmu takut."
    "Kuroiwa" "Saya sudah mendampinginya sejak kecil. Ia tidak meminta saya menguji teman-temannya. Tetapi saya ingin tahu apakah Anda memahami bahwa kepercayaannya bukan akses yang boleh dipakai sesuka hati."
    call kk_family_menu("S-D02", ["Jujur soal niatmu.", "Menghindar dengan sopan.", "Balik bertanya soal Shiori."])
    if _return == "A":
        nar "Kau menjawab tanpa menjanjikan sesuatu yang belum diketahui. Kuroiwa menanyakan satu hal sulit, lalu menerima ketika kau membedakan keinginanmu dari kepastian tentang perasaan Shiori."
        "Kuroiwa" "Baik. Bicarakan dengan dia juga. Saya bisa membantu menjaga keselamatannya, bukan menjawab siapa yang seharusnya ia percaya."
    elif _return == "B":
        "Kuroiwa" "Mengelak. Baik. Tapi tahu saja: aku tidak akan jauh dari dia."
        nar "Ia memberi jalan setelah itu, tidak menganggap kesopananmu sama dengan jawaban. Pada kesempatan berikutnya keramahan tetap ada, namun kemudahan mendekat harus lebih dahulu melewati pertanyaan yang belum dijawab."
    else:
        "Kuroiwa" "Jika ingin mengenalnya, tanyakan kepadanya. Kalau yang ditanyakan cara memastikan ia aman, saya bersedia membantu. Itu dua hal berbeda."
        nar "Ia tidak memberimu rahasia pribadi sebagai balasan atas keberanian bertanya. Batas tersebut justru menjelaskan mengapa Shiori dapat mempercayainya."
    return

# ┌─ PANDUAN CERITA · S-D05 · Buku Bertanda Tangan
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : Chiasa host
# │ INTI    : A Akui / B pura-pura tidak tahu / C tawarkan tanda tangan
# │ AKHIRAN : jembatan atau perangkap Shena
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S_D05:
    $ _s_loc = getattr(store, "_lokasi", None) or "Klub Catur"
    $ _s_dist = KK_DISTRICT_NAME.get(getattr(store, "_distrik", "d3"), "Distrik Elite")
    call kk_scene_enter("shiori", _s_dist + " · " + _s_loc)
    if _s_loc == "Klub Catur":
        nar "Ruang Klub Catur sedang lengang saat kamu datang menghampiri meja dekat jendela. Di samping cangkir teh porselen milik Shiori, tergeletak sebuah novel strategi ringan yang sudut sampulnya sudah agak melunak karena sering dibaca, dengan beberapa penanda kertas tipis terselip di bagian tengah."
    elif _s_loc == "Rumah Saionji":
        nar "Di ruang duduk Rumah Saionji yang tenang, Shiori baru saja meletakkan buku yang sedang dibacanya di samping cangkir teh ketika kamu duduk di seberangnya. Sudut sampul novel strategi ringan itu sudah agak melunak karena sering dibuka, dengan beberapa penanda kertas tipis terselip di bagian tengah."
    else:
        nar "Di meja tempat kalian duduk di [_s_loc], Shiori baru saja menutup sebuah novel strategi ringan di samping cangkir minumannya. Sudut sampul buku itu sudah agak melunak karena sering dibaca, dengan beberapa penanda kertas tipis terselip di bagian tengah."
    nar "Begitu matamu jatuh pada ilustrasi sampulnya, kamu langsung mengenali tarikan garis halus dan warna dingin yang persis sama dengan cetakan contoh di meja belajar kamarmu. Kamu menahan diri supaya tidak terlihat kaget, lalu membuka obrolan biasa saja."
    chiasa "Eh, Saionji-senpai baca seri novel strategi yang itu juga ya? Kelihatannya lumayan sering dibuka sampai pinggiran kertasnya halus begitu."
    nar "Shiori melirik buku di samping tangannya, lalu tersenyum sopan sambil menggeser cangkir tehnya sedikit."
    shiori "Iya, Amamiya-san. Lumayan bagus buat bacaan selingan di luar materi kuliah. Alur strateginya cukup rapi dan nggak terlalu menggampangkan masalah."
    chiasa "Aku kira Senpai lebih sering baca buku referensi ekonomi atau catatan permainan catur aja."
    shiori "Kalau isi kepalaku cuma diisi laporan dan notasi pertandingan terus, bisa jenuh juga. Lagipula, jujur saja, yang bikin aku selalu beli jilid barunya justru ilustrasi di dalamnya."
    nar "Ia membuka salah satu halaman yang diberi penanda kertas tipis lalu memutarnya sedikit ke arahmu, memperlihatkan ilustrasi hitam-putih seorang tokoh yang berdiri di tengah ruangan penuh orang."
    shiori "Kebetulan kamu anak Seni Rupa, Amamiya-san. Aku selalu suka cara ilustrator bernama Shena ini menggambar tatapan mata yang terasa sepi di tengah keramaian. Menurutmu dari sudut pandang orang seni, gaya goresan seperti ini kelihatan dikerjakan ilustrator senior yang sudah lama di industri, atau orang yang masih cukup muda?"
    nar "Pertanyaan santai itu datang tepat saat kamu sedang memandangi gambar yang pernah kamu lihat rancangannya di kamar Chiasa. Karena berusaha menjawab secepat mungkin supaya tidak kelihatan canggung, kalimatmu malah meluncur sedikit kelewatan."
    chiasa "Kalau dilihat dari tarikan garisnya sih kayaknya masih seumuran mahasiswa, soalnya di buku sketsa aslinya... eh, maksudku kalau dibayangkan waktu masih jadi sketsa pensil sebelum dicetak, goresannya kelihatan masih ringan dan belum kaku kayak ilustrator lama."
    nar "Begitu kalimat itu keluar, lidahmu langsung terasa kelu. Di seberang meja, tangan Shiori yang hendak menutup kembali halaman buku itu berhenti di udara. Mata ungu ametisnya terangkat pelan menatap wajahmu, mengamati raut salah tingkah yang gagal kamu sembunyikan."
    shiori "...'Di buku sketsa aslinya', ya?"
    chiasa "I-itu cuma cara ngomongku aja kok, Saionji-senpai, habis di kelas seni biasanya kami sering nebak-nebak bentuk sketsa awal di balik hasil cetakan."
    nar "Shiori tidak langsung membantah. Ia justru menutup bukunya perlahan, menumpukan dagu ringan di atas punggung jari, lalu menatapmu dengan senyum tipis yang tenang sekaligus menyelidik."
    shiori "Penjelasan yang cukup rapi, Amamiya-san. Hanya saja, barusan nada bicaramu lebih terdengar seperti orang yang pernah melihat langsung kertas sketsanya, lalu mendadak sadar salah bicara. Wajahmu juga sempat berubah kaku begitu kusebut nama Shena."
    shiori "Aku nggak suka asal menuduh tanpa dasar. Jadi aku tanya langsung saja ke kamu, apakah kamu mengenal orang di balik nama pena Shena itu, atau sebenarnya ada kaitan lain?"
    call kk_family_menu("S-D05", ["Akui kaitannya.", "Pura-pura tidak tahu.", "Tawarkan tanda tangan Shena."])
    if _return == "A":
        nar "Melihat sorot mata Shiori yang sudah membaca kejanggalan ucapanmu dengan terlalu tepat, kamu mengembuskan napas pelan dan memilih tidak memperpanjang alasan yang hanya akan terdengar makin aneh."
        chiasa "...Sebenarnya nama pena Shena itu memang punyaku, Saionji-senpai. Tapi aku minta tolong banget jangan dibocorkan ke siapa-siapa di kampus ya, soalnya bahkan teman-teman di studio pun hampir nggak ada yang tahu."
        nar "Shiori terdiam dua detik, alisnya terangkat tipis karena dugaannya ternyata meleset sedikit lebih jauh ke arah yang lebih mengejutkan, sebelum senyum yang lebih tulus muncul di wajahnya."
        shiori "Jadi ternyata kamu sendiri orangnya. Kamu menyimpan rahasia sebesar ini sendirian sejak masuk kuliah, Amamiya-san? Jujur saja, sekarang aku malah makin penasaran sisi lain apa lagi yang masih kamu simpan."
        chiasa "Cuma soal ilustrasi itu aja kok, Senpai. Lagipula jujur aja, belakangan ini gambaranku lagi nggak sebagus waktu bikin jilid itu, jadi aku memang agak enggan kalau orang-orang di kampus tahu terus berharap terlalu tinggi."
        shiori "Tenang saja, aku tahu bedanya menikmati karya dengan mencampuri urusan pribadi pembuatnya. Rahasiamu aman denganku. Kalau kamu nggak keberatan, kapan-kapan boleh kan kita ngobrol santai soal ilustrasi di halaman yang paling kusuka tadi?"
        chiasa "Boleh kok, Senpai, selama memang cuma jadi obrolan kita berdua aja."
        nar "Shiori mengangguk pelan sambil merapikan penanda kertas di dalam novelnya, kali ini tanpa jarak sopan yang biasanya selalu ia pasang."
    elif _return == "B":
        nar "Kamu menarik napas pendek, merapikan ekspresi wajahmu supaya terlihat lebih santai, lalu menggeleng pelan."
        chiasa "Nggak kok, Saionji-senpai. Aku beneran nggak kenal siapa orang di balik nama Shena. Tadi aku cuma keceplosan pakai istilah kelas studio aja, dan sempat kaget karena ternyata Senpai suka baca novel ringan juga."
        nar "Shiori menatap wajahmu beberapa detik tanpa menyela ataupun mendesak. Kemudian ia menunduk, menyelipkan kembali penanda kertas yang agak mencuat ke dalam novel, dan merapikannya di samping tasnya dengan gerakan yang terlalu tenang."
        shiori "Begitu, ya. Kalau memang cuma kebetulan salah pilih kata, aku nggak bakal memaksa atau menjadikan firasat pribadi sebagai bukti apa-apa."
        chiasa "Iya, maaf ya, Senpai, tadi cara ngomongku memang agak membingungkan."
        shiori "Nggak perlu minta maaf, Amamiya-san. Hanya saja aku punya kebiasaan mengingat detail percakapan yang terasa janggal, jadi jawabanmu hari ini tetap bakal kusimpan baik-baik."
        nar "Ia kembali meraih cangkir tehnya dengan senyum sopan yang persis seperti biasa. Tidak ada nada marah di suaranya, tetapi jeda sebelum ia mengganti topik obrolan terasa sedikit lebih dingin daripada sebelumnya."
    else:
        nar "Daripada terjebak membela diri dengan wajah gugup, kamu justru menegakkan dudukmu dan menatap balik senyum menyelidik Shiori dengan nada lebih santai."
        chiasa "Kalau Saionji-senpai memang suka banget sama ilustrasinya sampai bukunya dibaca berulang-ulang begitu... gimana kalau kutuliskan tanda tangan Shena langsung di halaman dalam buku ini? Asal tetap jadi rahasia kita berdua aja ya."
        nar "Mata ungu ametis Shiori melebar sebentar mendengar tawaran yang tidak ia duga itu. Sedetik kemudian, ia tertawa pelan sambil menggeleng kecil."
        shiori "Tanda tangan asli Shena langsung di bukuku, tepat setelah aku hampir selesai menebak? ...Wah, Amamiya-san, kamu tahu betul cara membalik keadaan sekaligus bikin orang merasa berutang budi ya."
        chiasa "Nggak ada utang budi apa-apa kok, Senpai. Aku malah senang lihat bukunya beneran dibaca sampai ujung kertasnya lembut begini, nggak cuma dipajang di rak."
        nar "Shiori membuka tasnya, mengeluarkan sebuah pulpen tinta hitam yang rapi, lalu menyodorkannya bersama halaman pembuka novel yang masih bersih ke hadapanmu."
        shiori "Kalau begitu, tolong tulis namaku di atasnya cukup 'untuk Shiori' saja ya, tanpa embel-embel marga Saionji. Biar buku ini benar-benar jadi milikku sendiri."
        chiasa "Siap, sebentar ya, Senpai... tanganku agak deg-degan nulis langsung di buku orang."
        nar "Kamu menuliskan catatan singkat dan tanda tangan itu hati-hati di sudut halaman, lalu menyerahkan buku tersebut kembali. Shiori memandangi goresan tinta hitam itu dengan senyum puas sebelum menutupnya rapi dan menyimpannya kembali ke dalam tas."
    return

# ┌─ PANDUAN CERITA · S-D06 · Gala dan Tojo
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : Tojo aktif
# │ INTI    : A Terima / B tolak / C datang bersama orang lain
# │ AKHIRAN : orang tua Saionji bertemu pemain; jalur Tojo
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S_D06:
    call kk_scene_enter("shiori", "Undangan gala")
    nar "Di koridor yang sepi seusai jadwal kampus, Shiori mengeluarkan sebuah amplop undangan berbahan kertas krem tebal dari tasnya dan memegangnya sejenak sebelum menatapmu."
    if kk_host == "chiasa":
        shiori "Amamiya-san, akhir pekan ini keluargaku mengadakan jamuan gala tahunan. Orang tuaku sebenarnya paham aku nggak ingin seluruh obrolan malam itu berakhir di meja Tojo Akihiro, tapi secara formal dia tetap datang. Maukah kamu ikut menemaniku malam itu supaya ada sebagian waktu yang bisa kuhabiskan bersama orang yang benar-benar ingin kutemui?"
    else:
        shiori "Kisaragi-san, akhir pekan ini keluargaku mengadakan acara gala. Orang tuaku tahu aku nggak mau seluruh malam itu dihabiskan meladeni Tojo Akihiro, tapi dia tetap akan hadir. Maukah kamu menemaniku ke sana supaya ada bagian malam yang bisa kujalani dengan orang yang memang ingin kuajak bicara?"
    nar "Ia sama sekali tidak menyembunyikan bahwa kehadiranmu juga akan memotong ruang gerak Tojo. Keluarganya tidak menuntut sandiwara hubungan apa pun, meski para tamu kalangan elite pasti akan cepat menarik kesimpulan mereka sendiri."
    call kk_family_menu("S-D06", ["Terima jadi pasangan pengalih.", "Tolak permintaannya.", "Datang bersama orang lain."])
    if _return == "A":
        if kk_host == "chiasa":
            chiasa "Boleh, Saionji-senpai. Kalau kehadiranku bisa bikin Senpai bernapas lebih lega di acara itu, aku siap ikut menemani."
        else:
            yutaka "Oke, aku ikut, Saionji-san. Kalau butuh alasan buat menghindar dari obrolan Tojo di tengah aula, tinggal beri kode saja."
        shiori "Terima kasih banyak. Di depan orang tuaku, bersikaplah biasa saja seperti di kampus. Urusan menghadapi tamu-tamu yang terlalu ingin tahu, biar aku yang tangani."
        nar "Kalian menyepakati cara perkenalan yang nyaman tanpa memaksamu berpura-pura memiliki hubungan yang tidak kamu inginkan demi memuaskan rasa ingin tahu para tamu."
    elif _return == "B":
        if kk_host == "chiasa":
            chiasa "Maaf banget, Saionji-senpai, aku kayaknya nggak sanggup ikut acara gala resmi sebesar itu. Aku takut malah canggung dan bikin Senpai makin repot."
        else:
            yutaka "Maaf, Saionji-san, untuk acara gala keluarga kali ini kayaknya aku harus menolak dulu. Kalau keluarga Kisaragi lihat aku datang sebagai pendamping, urusannya bisa tambah panjang."
        shiori "Baik, aku mengerti kok. Jujur sedikit kecewa, tapi aku sanggup menghadapi malam itu. Lagi pula ada Kuroiwa dan orang tuaku di sana."
        nar "Ia menyimpan kembali amplop undangan itu dengan rapi, menerima penolakanmu dengan bersih tanpa sedikit pun mencoba membuatmu merasa bersalah."
    else:
        if kk_host == "chiasa":
            chiasa "Aku bisa datang kok, Saionji-senpai, tapi boleh nggak aku sekalian ajak teman lain biar suasananya lebih santai dan nggak terlalu mencolok?"
        else:
            yutaka "Aku datang ke galanya, Saionji-san, tapi aku bakal datang bareng kenalan lain supaya nggak memicu gosip berlebihan di antara keluarga kita."
        nar "Pada malam acara, Shiori menyambut kedatanganmu dan rekanmu di dekat pintu aula dengan kesopanan sempurna tanpa membiarkan rasa kecewa sedikit pun terlihat."
        nar "Dari seberang meja minuman, Tojo langsung menangkap perubahan formasi itu dan melangkah mendekat lagi dengan senyum percaya diri. Malam yang semula diharapkan memberi Shiori ruang bernapas kini memaksanya menjaga ketenangan dari dua arah sekaligus."
    return

# ┌─ PANDUAN CERITA · S-D10 · Musuh Bersama
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : pemain memberi bukti tentang Ogawa atau Kuga
# │ INTI    : A Bergabung / B biarkan ia sendiri / C minta ia berhenti
# │ AKHIRAN : E-SH-10 menguat; Harumi dan Moeka terbantu
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S_D10:
    call kk_scene_enter("shiori", "Klub Catur · Musuh bersama")
    nar "Keterangan tentang Ogawa dan Kuga membuat Shiori berhenti tersenyum sebelum mencapai halaman terakhir. Ia membacanya dua kali, memisahkan bagian yang dapat diverifikasi dari bagian yang masih perlu ditanyakan."
    shiori "Ada orang yang dilukai. Aku ingin pelakunya kehilangan ruang untuk terus melakukannya. Kalau kita bekerja sama, kita perlu memastikan itu tidak berubah menjadi pertunjukan tentang betapa pandainya kita."
    call kk_family_menu("S-D10", ["Bergabung dengannya.", "Biarkan ia bergerak sendiri.", "Minta ia berhenti."])
    if _return == "A":
        shiori "Sekutu. Tapi keputusan tentang cerita Harumi dan Moeka perlu melibatkan mereka. Kita tidak sedang mengambil alih hak bicara hanya karena merasa tahu cara menang."
        nar "Kau menyetujui, lalu membicarakan bantuan yang dapat diberikan tanpa memaksa keduanya tampil sebagai bukti pada hari yang belum mereka pilih."
    elif _return == "B":
        nar "Kau menyerahkan keterangan dan tidak ikut bergerak. Shiori menanyakan batas penggunaan informasi tersebut, kemudian meneruskan upaya melalui orang-orang yang dapat membantu. Ketiadaanmu tidak membuat persoalan berhenti penting."
    else:
        shiori "Berhenti? ...Kau tahu aku tidak pandai berhenti. Tapi akan kupertimbangkan, karena kau yang minta."
        nar "Ia menanyakan apakah kau takut pada akibat bagi korban atau sekadar tak ingin konflik meluas kepadamu. Jawaban itu akan menentukan bagian mana dari kehati-hatianmu yang pantas didengar sebagai kepedulian."
    return

# ┌─ PANDUAN CERITA · S-D11 · Prediksi yang Benar
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : pemain sudah menceritakan Sistem
# │ INTI    : A Lanjut terbuka / B minta ia menyimpan rahasia / C manfaatkan dia
# │ AKHIRAN : E-SH-06 menguat
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S_D11:
    call kk_scene_enter("shiori", "Klub Catur · Prediksi yang benar")
    nar "Prediksi tentang Sistem terbukti pada bagian yang sebelumnya dapat diperiksa. Shiori membuka catatan lama dan menandai apa yang sungguh cocok, tidak memindahkan satu keberhasilan menjadi bukti untuk semua klaimmu sekaligus."
    shiori "Kau benar. Setiap langkah. ...Jadi yang kau ceritakan itu nyata. Pertanyaannya sekarang: apa yang akan kita lakukan dengan pengetahuan ini?"
    call kk_family_menu("S-D11", ["Lanjut terbuka padanya.", "Minta ia menyimpan rahasia.", "Manfaatkan kepercayaannya."])
    if _return == "A":
        shiori "Terbuka. Termasuk jika nanti aku menyimpulkan sesuatu yang tidak kamu sukai. Kamu tidak sedang mengajak sekutu hanya untuk mengulang keputusanmu sendiri, kan?"
        nar "Kau memberinya bagian yang selama ini tidak nyaman dibahas. Pengetahuan itu mulai menjadi sesuatu yang bisa diperdebatkan bersama, bukan sekadar alasan mempercayaimu lebih jauh."
    elif _return == "B":
        shiori "Rahasia tetap rahasia. ...Aku pandai menyimpan. Percayalah sejauh itu."
        nar "Ia meminta kalian menentukan kapan keselamatan orang lain mengharuskan mencari bantuan di luar kesepakatan tersebut. Rahasia tidak akan dipakai sebagai alasan membiarkan luka hanya agar kalian tetap merasa memegang keistimewaan."
    else:
        nar "Kau menyisakan bagian yang menguntungkanmu dan membiarkan ia merencanakan berdasarkan cerita yang tidak lengkap. Shiori bekerja dengan sungguh-sungguh, belum tahu bahwa kesediaannya membantu juga sedang dipakai untuk melindungi kebohongan baru."
    return

# ┌─ PANDUAN CERITA · S-D12 · Ratu yang Jatuh Sakit
# │ LOKASI  : (dinamis — muncul dari kondisi)
# │ TERLIBAT: Saionji Shiori
# │ AWALAN  : tahap 4; ia begadang menyusun bukti
# │ INTI    : A Rawat / B cari bukti di kamarnya / C tinggalkan buah
# │ AKHIRAN : merawat: marah[[pemain] turun banyak; mencari bukti: kejahatan baru dan marah[[pemain] +40
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S_D12:
    call kk_scene_enter("shiori", "Kamar Saionji · Ratu yang sakit")
    nar "Shiori jatuh sakit setelah terlalu lama memaksakan diri menyusun keterangan. Kuroiwa meminta persetujuannya sebelum mengantarmu menjenguk. Di kamar, map masih menunggu dekat tempat tidur, tetapi pemiliknya tidak lagi sanggup mempertahankan ketenangan yang biasa."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABC", KK_DYN_BY_ID["S-D12"]["choices"])]
    call screen kk_choice_panel(_rows, "Ratu yang jatuh sakit")
    $ kk_record_choice("S-D12", _return)
    if _return == "A":
        shiori "Kau... merawatku? Tidak mencari apa-apa? ...Aku tidak tahu harus menaruh ini di kolom mana."
        nar "Kau menanyakan bantuan yang diinginkan dan memberi ruang bagi istirahat. Shiori melihat map sekali, lalu kembali padamu, mengakui bahwa ia tidak menduga kehadiranmu dapat berhenti pada menemaninya tanpa harga lain."
    elif _return == "B":
        nar "Ketika ia tertidur, kau mencari keterangan yang dapat melindungi dirimu. Kepercayaan untuk masuk ke kamar dipakai menembus batas lain yang tidak pernah ia izinkan."
        nar "Kau mungkin menemukan sesuatu. Jika perbuatan itu terbuka, ia juga akan memiliki jawaban yang sangat jelas tentang apa yang kaupilih saat mengira dirinya tidak mampu melihat."
    else:
        nar "Kau meninggalkan buah dan pesan singkat, lalu memberi ruang istirahat. Kuroiwa menyampaikan siapa yang datang ketika Shiori terbangun."
        nar "Ia membaca pesan dua kali, belum menyamakan satu perhatian dengan semua urusan selesai. Namun map itu tidak disentuh, dan batas yang tetap dihormati memberi sesuatu yang bisa ia pikirkan tanpa marah."
    return

init 1 python:
    _hook("S-D01-A", lambda: (kk_adj("akun_anonim",8), kk_rel("shiori","intim",3)))
    _hook("S-D01-B", lambda: (kk_adj("akun_anonim",6), kk_shiori_read(5)))
    _hook("S-D01-C", lambda: (kk_adj("curiga_shiori",10), kk_flag("shiori_curiga_akun")))
    _hook("S-D02-A", lambda: (kk_adj("kuroiwa_percaya",10), kk_rel("shiori","trust",3)))
    _hook("S-D02-B", lambda: kk_adj("kuroiwa_percaya",-5))
    _hook("S-D02-C", lambda: (kk_adj("kuroiwa_percaya",-3), kk_shiori_read(4)))
    _hook("S-D05-A", lambda: (kk_flag("shena_terbongkar"), kk_rel("shiori","intim",5)))
    _hook("S-D05-B", lambda: kk_adj("curiga_shiori",6))
    _hook("S-D05-C", lambda: (kk_rel("shiori","aff",5), kk_flag("shena_jembatan")))
    _hook("S-D06-A", lambda: (kk_flag("shiori_gala_pengalih"), kk_rel("shiori","trust",5)))
    _hook("S-D06-B", lambda: kk_rel("shiori","trust",-4))
    _hook("S-D06-C", lambda: (kk_flag("tojo_membaca"), kk_adj("marah_shiori",5)))
    _hook("S-D10-A", lambda: (kk_flag("shiori_sekutu_musuh"), kk_adj("respek_shiori",10)))
    _hook("S-D10-B", lambda: None)
    _hook("S-D10-C", lambda: kk_rel("shiori","trust",4))
    _hook("S-D11-A", lambda: (kk_flag("shiori_tahu_sistem"), kk_adj("respek_shiori",10)))
    _hook("S-D11-B", lambda: (kk_flag("shiori_tahu_sistem"), kk_rel("shiori","trust",5)))
    _hook("S-D11-C", lambda: (kk_shiori_read(8), kk_flag("shiori_dimanfaatkan")))
    _hook("S-D12-A", lambda: (kk_adj("marah_shiori",-20), kk_rel("shiori","intim",6)))
    _hook("S-D12-B", lambda: (kk_adj("marah_shiori",40), kk_flag("shiori_kamar_digeledah")))
    _hook("S-D12-C", lambda: (kk_adj("marah_shiori",-8), kk_rel("shiori","aff",4)))
