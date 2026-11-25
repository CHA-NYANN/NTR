# Gerbang Rute Yandere Nagisa (N14-N18): posesif -> ultimatum -> bentrok ->
# tuduhan -> sabotase. Ditulis sebagai KARAKTER dan KONSEKUENSI. Tindakan ekstrem
# (jebakan, sabotase, memfitnah) hanya AKIBATNYA yang dicatat singkat; metode,
# rekayasa jebakan, dan cara memfitnah korban TIDAK ditulis. Efek menggerakkan
# stage[nagisa], kelekatan_nagisa, jeal/fear. Nilai prototipe; Event_Nagisa.

init 1 python:
    def kk_nagisa_stage(n):
        kk_stage("nagisa", max(n, stage.get("nagisa", 0)))

# ┌─ PANDUAN CERITA · N14 · Cek Pesan
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : ia meminta melihat ponsel pemain.
# │ INTI    : A tunjukkan / B tolak / C tipu.
# │ AKHIRAN : gerbang Rute Yandere (stage 3, posesif).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N14:
    call kk_scene_enter("nagisa", "Gedung Arsitektur · Cek pesan")
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Lampu meja gambar di ruang Studio Arsitektur memancarkan lingkaran cahaya putih di atas kertas kalkir dan potongan kayu balsa. Sebagian besar mahasiswa lain sudah pulang, menyisakan dengung halus pendingin ruangan."
        else:
            nar "Cahaya bulan September menembus jendela lebar Studio Arsitektur yang berbau kertas gambar dan lem kayu. Beberapa meja jauh di sudut masih terisi, sementara di meja dekat jendela kamu menemani Nagisa merapikan gambar denahnya."
        nar "Nagisa duduk tegak dengan pita hitam-pink di kedua twin-tail pirangnya yang bergoyang tipis setiap kali ia menggeser penggaris besi. Kamu duduk di kursi tinggi di sebelahnya sambil memotong selotip kertas dan meletakkan ponselmu di tepi meja gambar."
        nagisa "Garis tangga sudut kiri ini selalu bikin kesal kalau pakai skala kecil. Tolong pegang ujung kertasnya sebentar ya, Chiasa, biar nggak bergeser."
        chiasa "Sini kupegang. Garis jendela utamamu yang tadi sudah lurus banget kok, Nagisa-senpai."
        nagisa "Iya dong, aku sampai ulang tiga kali dari kemarin. Soalnya dosen kelas ini paling cerewet kalau ketebalan garis pintu nggak rata."
        nar "Suasana meja sempat terasa hangat dan akrab sampai ponselmu yang tergeletak di tepi kayu bergetar pelan sekali sambil menyalakan layar. Goresan pensil mekanik Nagisa langsung berhenti satu ketukan."
        nar "Ia hanya melirik cepat dari sudut mata, lalu menarik garis berikutnya agak lebih kencang dari sebelumnya."
        nagisa "Pesan dari rumah, Chiasa?"
        chiasa "Bukan, paling obrolan grup kelas seni."
        nagisa "Oh... grup kelas seni ya. Kirain ada yang manggil kamu buat pergi sekarang juga."
        chiasa "Nggak kok, aku kan sudah janji nemenin kamu sampai garis lantai satunya selesai."
        nar "Dua menit berselang, ponselmu kembali bergetar untuk kedua kalinya. Bibir Nagisa mengatup tipis dan ujung pensil mekaniknya meleset dua milimeter dari tepi penggaris besi."
        nar "Ia langsung meraih penghapus putih dan menggosok garis yang meleset itu terlalu keras sampai ujung kertas kalkirnya sedikit terlipat."
        if kk_has("m17b_pulau_selesai"):
            nagisa "Dari waktu kita naik feri pulang pulau kemarin juga ponselmu nyala terus begini... padahal kamu duduk tepat di sebelahku."
        else:
            nagisa "Belakangan ini ponselmu sepertinya sibuk terus ya, Chiasa. Setiap kita duduk bareng pasti ada saja yang masuk."
        nar "Begitu ponselmu bergetar untuk ketiga kalinya dan kamu sempat melirik notifikasi di layar sambil tersenyum tipis, Nagisa berhenti menggambar sepenuhnya. Ia meletakkan pensil mekaniknya sangat pelan dan sejajar persis di samping penggaris besi."
        nar "Suaranya yang keluar sama sekali tidak keras seperti omelannya yang biasa, justru turun terlalu tenang dan rapat."
        nagisa "Siapa yang mengirim pesan terus-terusan dari tadi, Chiasa?"
        chiasa "Cuma obrolan biasa sama urusan tugas kampus, Nagisa-senpai. Nggak ada hal penting kok."
        nagisa "Boleh lihat? Sebentar saja. Aku capek terus menebak-nebak dari caramu melirik layar lalu tersenyum tipis sendiri."
        chiasa "Nagisa-senpai... aku benar-benar cuma lagi baca obrolan biasa. Kenapa tiba-tiba jadi serius banget begini?"
        nagisa "Kamu sendiri nggak sadar ya? Dari tiga puluh menit terakhir setiap layarmu nyala, matamu langsung pindah ke sana duluan."
        chiasa "Itu kan cuma refleks karena getarannya di atas meja kayu berisik..."
        nar "Kamu belum sempat mengangkat tangan dari meja ketika Nagisa mencondongkan tubuh sedikit mendekat. Mata biru cerahnya menatapmu lurus tanpa berkedip, menambahkan satu kalimat pelan yang langsung mengubah penolakan terdengar seperti pengakuan bersalah."
        nagisa "Kalau memang nggak ada yang kamu sembunyikan dariku, harusnya nggak masalah dong kalau cuma kulihat sebentar?"
        chiasa "{i}Tatapannya beda sekali dari gengsi biasanya. Ia benar-benar sedang menahan cemas yang siap meledak kalau salah jawab.{/i}"
        call kk_family_menu("N14", ["Tunjukkan layar ponselmu kepadanya.", "Tolak dengan tenang karena itu privasimu.", "Tipu ia dengan tampilan layar pesan yang sudah kamu rapikan."])
        if _return == "A":
            chiasa "Nih, lihat saja sendiri, Nagisa-senpai. Biar kamu berhenti menebak-nebak di dalam kepala."
            nar "Kamu membuka kunci layar dan menggeser ponsel itu melintasi kertas gambar ke hadapannya. Nagisa segera meraihnya dengan kedua tangan yang terasa sedikit dingin."
            nar "Ia tadi hanya meminta sebentar, tetapi ibu jarinya menggulir jauh lebih lama daripada beberapa detik. Ia berhenti di deretan pesan teratas, mengecek jam pengiriman satu per satu dengan kening berkerut."
            nagisa "Yang masuk tiga kali barusan ini... obrolan grup kelas seni soal pameran akhir bulan?"
            chiasa "Iya, anak-anak lagi ribut soal pembagian dinding pajang. Yang barusan bikin aku senyum itu gara-gara mereka salah hitung lebar papan."
            nar "Nagisa menggulir sedikit lebih ke bawah lagi, memastikan tidak ada nama tersembunyi di urutan teratas, lalu jemarinya akhirnya berhenti di pinggir bingkai ponsel."
            chiasa "Sudah cukup, Senpai?"
            nar "Nagisa mengembuskan napas panjang yang bergetar tipis, lalu meletakkan ponselmu kembali di samping gelas airmu. Senyum lega yang tiba-tiba muncul di wajahnya terasa sangat rapuh."
            nagisa "Maaf banget, Chiasa... aku cuma takut akhir-akhir ini. Rasanya belakangan semua orang di sekitarku gampang sekali berubah atau menjauh begitu aku lengah sedikit saja."
            chiasa "Aku masih duduk di sini menemani kamu menggambar, kan? Aku nggak bakal mendadak menghilang cuma gara-gara pesan grup."
            nagisa "Aku tahu harusnya aku nggak mikir sampai ke sana... tapi begitu melihat layarmu menyala berkali-kali sementara kamu senyum sendiri, kepalaku langsung penuh pikiran aneh."
            chiasa "Kalau kamu lagi cemas begitu, bilang langsung saja ke aku, Senpai. Nggak usah dipendam sampai pensilmu meleset begitu."
            nagisa "Iya... maaf ya aku jadi kelihatan kekanakan banget tadi. Sekarang aku jauh lebih tenang, beneran. Nanti habis bagian denah ini beres, kita beli teh dingin di lantai bawah ya."
            chiasa "Oke, sekarang beresin dulu garis tangganya biar nggak miring lagi."
            nagisa "Hmph, cerewet. Iya, ini lagi kubenarkan kok!"
            nar "Ia kembali mengambil pensil mekaniknya dengan raut wajah yang tampak hangat dan lega. Namun ketenangan yang baru saja didapat lewat membuka layar itu tidak menjawab satu hal pun tentang apa yang akan terjadi ketika kecemasannya kembali datang di saat tidak ada layar yang bisa ia periksa."
        elif _return == "B":
            nar "Kamu meletakkan telapak tanganmu dengan tenang di atas layar ponsel yang tertutup, tidak menggesernya satu senti pun."
            chiasa "Nggak, Nagisa-senpai. Aku nggak mau menyerahkan ponselku. Menjaga privasi itu sama sekali nggak sama dengan menyembunyikan pengkhianatan."
            nar "Belum sempat kalimatmu selesai sepenuhnya, rona merah tajam langsung naik ke pipi Nagisa sampai ke pangkal pita twin-tailnya."
            nagisa "Aku cuma minta lihat sebentar! Kenapa kamu langsung bicara sekeras itu seolah-olah aku lagi menginterogasi penjahat?!"
            chiasa "Karena kalau setiap ponselku bunyi aku harus membuka layar buat membuktikan sesuatu, itu artinya dari awal kamu nggak percaya padaku."
            nagisa "Kalau kamu memang nggak menyembunyikan apa-apa, tinggal buka dua detik saja padahal semuanya langsung selesai! Buat apa kamu lindungi layar itu segitunya?!"
            chiasa "Bukan soal ada atau nggak ada yang disembunyikan, Senpai. Aku cuma nggak mau hubungan kita jalan pakai curiga seperti itu."
            nar "Nagisa langsung mengatupkan bibir rapat. Ia menyambar tali tasnya di kursi sebelah dengan gerakan kasar hingga gantungan kelinci Koko di ritsletingnya beradu nyaring dengan pinggir meja, seolah hendak langsung pergi meninggalkan studio."
            nar "Namun langkahnya justru berhenti mematung tepat di samping meja gambar. Tangannya mencengkeram tali tas erat-erat sementara dadanya naik turun cepat, tidak sanggup melangkah keluar pintu sekaligus tidak punya cara memaksamu menurunkan tangan."
            nagisa "Selalu begitu... ujung-ujungnya aku lagi yang kelihatan salah karena terlalu peduli."
            chiasa "Aku nggak bilang kamu salah karena peduli, Nagisa-senpai. Aku cuma nggak mau kita saling mengawasi layar ponsel masing-masing."
            nagisa "Mengawasi?! Aku cuma tanya satu kali, Chiasa, dan kamu langsung pasang tembok setinggi itu di depan mukaku!"
            chiasa "Nagisa-senpai..."
            nagisa "...Sudah, terserah kamu deh, Chiasa. Simpan saja ponselmu baik-baik. Aku masih harus menyelesaikan garis ini sendirian."
            nar "Ia menjatuhkan tasnya kembali ke kursi tanpa menatapmu lagi, lalu menyambar penggaris besinya dengan bunyi denting keras di atas meja."
            nar "Di hadapan batas tegas yang tidak langsung kamu lunakkan, ketakutannya kehilangan jalan paling mudah untuk diredakan, meninggalkan jarak panas yang penuh curiga di antara kalian."
        else:
            chiasa "Ya sudah, sebentar ya. Aku tutup dulu tab foto referensi gambar yang lagi berantakan."
            nar "Kamu memiringkan layar sejenak menjauh dari sudut pandangnya dengan gerakan santai, memastikan hanya tampilan pesan aman dari grup studio dan obrolan keluarga yang terbuka rapi di layar, menyimpan seluruh percakapan pribadi lain jauh di luar jangkauannya."
            nar "Begitu kamu menggeser ponsel itu melintasi meja gambar, Nagisa langsung menunduk memeriksanya cepat. Matanya menyapu barisan obrolan tentang jadwal kertas sketsa, bahan maket, dan pesan singkat ibumu yang menanyakan jam pulang ke rumah."
            nagisa "Oh... beneran cuma grup kelas sama pesan dari rumah yang menanyakan jam pulang, ya..."
            nagisa "Haha, beneran ada yang salah ukur lebar papan pameran sampai dua puluh senti... pantas tadi kamu sempat tersenyum."
            chiasa "Kan sudah kubilang tadi, Nagisa-senpai. Memang cuma obrolan biasa."
            nar "Bahu Nagisa yang sejak tadi kaku langsung turun seluruhnya. Ia menyerahkan ponselmu kembali dengan kedua tangan, wajahnya berubah sungguh-sungguh merasa bersalah sampai telinganya ikut memerah."
            nagisa "Harusnya aku percaya sama kamu dari awal. Maaf banget ya, Chiasa, aku malah curiga aneh-aneh sampai minta cek ponselmu segala."
            chiasa "Nggak apa-apa, Nagisa-senpai. Yang penting sekarang kamu nggak cemas lagi."
            nagisa "Jangan bilang nggak apa-apa gitu, aku jadi makin merasa nggak enak tahu... Nanti habis aku rapikan garis sudut ini, biar aku yang traktir teh dingin di mesin bawah buat minta maaf ya. Kali ini kamu nggak boleh menolak."
            chiasa "Iya, Senpai. Selesaikan dulu garis tangganya pelan-pelan."
            nagisa "Siap! Kalau ada pesan masuk lagi dari grup itu, nggak bakal kulirik lagi deh, janji."
            chiasa "{i}Ia bahkan sampai berjanji tidak akan melirik lagi karena merasa bersalah. Cukup satu layar yang dirapikan untuk mengubah curiganya menjadi rasa berutang budi.{/i}"
            nar "Ia tersenyum cerah dan kembali memegang pensil mekaniknya dengan gerakan mantap. Permintaan maafnya memudahkanmu menyimpan rapat seluruh sisi lain hidupmu dari matanya, tetapi di balik ketenangan manis itu tertanam satu bom waktu apabila suatu hari ia tahu rasa aman yang baru saja ia syukuri ternyata disusun untuk menipunya."
    else:
        if kk_slot >= 3:
            nar "Lampu meja gambar di ruang Studio Arsitektur memancarkan lingkaran cahaya putih di atas kertas kalkir dan potongan kayu balsa. Sebagian besar mahasiswa lain sudah pulang, menyisakan dengung halus pendingin ruangan."
        else:
            nar "Cahaya bulan September menembus jendela lebar Studio Arsitektur yang berbau kertas gambar dan lem kayu. Beberapa meja jauh di sudut masih terisi, sementara di meja dekat jendela kamu menemani Nagisa merapikan gambar denahnya."
        nar "Nagisa duduk tegak dengan pita hitam-pink di kedua twin-tail pirangnya yang bergoyang tipis setiap kali ia menggeser penggaris besi. Kamu duduk miring di kursi tinggi di sebelahnya agar lututmu tidak menyenggol rangka meja gambar, membantu memotong selotip kertas sambil meletakkan ponselmu di tepi kayu."
        nagisa "Garis tangga sudut kiri ini selalu bikin kesal kalau pakai skala kecil. Dudukmu jangan gerak-gerak dulu ya, Yutaka, nanti mejanya goyang terus garisku miring lagi."
        yutaka "Aku bahkan nggak menyentuh kaki mejanya, Nagisa. Sini kupegang ujung kertas kalkirmu biar nggak bergeser."
        nagisa "Nah, gitu dong. Aku sudah ulang garis jendela utamanya tiga kali dari kemarin soalnya dosen kelas ini paling cerewet kalau ketebalan garis pintu nggak rata."
        nar "Suasana meja sempat terasa hangat dan akrab seperti kebiasaan lama kalian sampai ponselmu yang tergeletak di tepi kayu bergetar pelan sekali sambil menyalakan layar. Goresan pensil mekanik Nagisa langsung berhenti satu ketukan."
        nar "Ia hanya melirik cepat dari sudut mata, lalu menarik garis berikutnya agak lebih kencang dari sebelumnya."
        nagisa "Pesan dari Koita? Atau urusan apartemenmu, Yutaka?"
        yutaka "Bukan, cuma obrolan grup kelas Ekonomi."
        nagisa "Oh... grup kelas ya. Kirain ada yang langsung manggil kamu buat pergi sekarang juga."
        yutaka "Nggak kok, aku kan sudah bilang nemenin kamu sampai denah lantai satunya kelar."
        nar "Dua menit berselang, ponselmu kembali bergetar untuk kedua kalinya. Bibir Nagisa mengatup tipis dan ujung pensil mekaniknya meleset dua milimeter dari tepi penggaris besi."
        nar "Ia langsung meraih penghapus putih dan menggosok garis yang meleset itu terlalu keras sampai ujung kertas kalkirnya sedikit terlipat."
        if kk_has("m17b_pulau_selesai"):
            nagisa "Dari waktu kita berdiri di dek feri pulang pulau kemarin juga ponsel di sakumu bunyi terus begini... padahal aku berdiri tepat di sebelahmu."
        else:
            nagisa "Belakangan ini ponselmu sibuk terus ya, Yutaka. Setiap kita duduk berdua pasti ada saja yang nyari kamu."
        nar "Begitu ponselmu bergetar untuk ketiga kalinya dan kamu sempat melirik notifikasi di layar sambil tersenyum tipis, Nagisa berhenti menggambar sepenuhnya. Ia meletakkan pensil mekaniknya sangat pelan dan sejajar persis di samping penggaris besi."
        nar "Suaranya yang keluar sama sekali tidak keras seperti omelan teman masa kecilnya yang biasa, justru turun terlalu tenang dan rapat."
        nagisa "Siapa yang mengirim pesan terus-terusan dari tadi, Yutaka?"
        yutaka "Cuma obrolan biasa sama urusan tugas kuliah, Nagisa. Nggak ada hal penting."
        nagisa "Boleh lihat? Sebentar saja. Aku capek terus menebak-nebak dari caramu melirik layar lalu tersenyum tipis sendiri."
        yutaka "Nagisa... aku beneran cuma lagi baca obrolan grup. Kenapa tiba-tiba jadi tegang begini?"
        nagisa "Kamu sendiri nggak sadar ya? Dari tiga puluh menit terakhir setiap layarmu nyala, matamu langsung pindah ke sana duluan."
        yutaka "Itu cuma refleks karena getarannya di atas meja kayu kedengaran jelas."
        nar "Kamu belum sempat mengangkat tangan dari meja ketika Nagisa mencondongkan tubuh sedikit mendekat. Mata biru cerahnya menatapmu lurus tanpa berkedip, menambahkan satu kalimat pelan yang langsung mengubah penolakan terdengar seperti pengakuan bersalah."
        nagisa "Kalau memang nggak ada yang kamu sembunyikan dariku, harusnya nggak masalah dong kalau cuma kulihat sebentar?"
        yutaka "{i}Tatapannya beda jauh dari gengsi atau omelan biasanya. Ia benar-benar sedang menahan rasa cemas yang siap meledak kalau salah jawab.{/i}"
        call kk_family_menu("N14", ["Tunjukkan layar ponselmu kepadanya.", "Tolak dengan tenang karena itu privasimu.", "Tipu ia dengan tampilan layar pesan yang sudah kamu rapikan."])
        if _return == "A":
            yutaka "Nih, lihat saja sendiri, Nagisa. Biar kamu berhenti menebak-nebak di dalam kepala."
            nar "Kamu membuka kunci layar dan menggeser ponsel itu melintasi kertas gambar ke hadapannya. Nagisa segera meraihnya dengan kedua tangan yang terasa sedikit dingin."
            nar "Ia tadi hanya meminta sebentar, tetapi ibu jarinya menggulir jauh lebih lama daripada beberapa detik. Ia berhenti di deretan pesan teratas, mengecek jam pengiriman satu per satu dengan kening berkerut."
            nagisa "Yang masuk tiga kali barusan ini... obrolan grup tugas Ekonomi soal tabel laporan?"
            yutaka "Iya, ada teman kelompok yang salah masukin angka nol di kolom anggaran sampai satu grup ribut. Itu yang barusan bikin aku senyum."
            nar "Nagisa menggulir sedikit lebih ke bawah lagi, memastikan tidak ada nama tersembunyi di urutan teratas, lalu jemarinya akhirnya berhenti di pinggir bingkai ponsel."
            yutaka "Sudah cukup, Nagisa?"
            nar "Nagisa mengembuskan napas panjang yang bergetar tipis, lalu meletakkan ponselmu kembali di samping botol airmu. Senyum lega yang tiba-tiba muncul di wajahnya terasa sangat rapuh."
            nagisa "Maaf banget, Yutaka... aku cuma takut akhir-akhir ini. Rasanya belakangan semua orang di sekitarku gampang sekali berubah atau menjauh begitu aku lengah sedikit saja."
            yutaka "Aku masih duduk di sini dari tadi megangin ujung kertas gambarmu, kan? Aku nggak bakal mendadak menghilang cuma gara-gara pesan grup."
            nagisa "Aku tahu harusnya aku nggak mikir sampai ke sana... tapi begitu melihat layarmu menyala berkali-kali sementara kamu senyum sendiri, kepalaku langsung penuh pikiran aneh."
            yutaka "Kalau kamu lagi cemas begitu, bilang langsung saja ke aku. Nggak usah dipendam sampai garis gambarmu meleset begitu."
            nagisa "Iya... maaf ya aku jadi kelihatan kekanakan banget tadi. Sekarang aku jauh lebih tenang, beneran. Nanti habis bagian denah ini beres, kita beli minuman dingin di lantai bawah ya."
            yutaka "Oke, sekarang beresin dulu garis tanggamu biar nggak miring lagi."
            nagisa "Hmph, nggak usah sok santai begitu! Iya, ini lagi kubenarkan kok!"
            nar "Ia kembali mengambil pensil mekaniknya dengan raut wajah yang tampak hangat dan lega. Namun ketenangan yang baru saja didapat lewat membuka layar itu tidak menjawab satu hal pun tentang apa yang akan terjadi ketika kecemasannya kembali datang di saat tidak ada layar yang bisa ia periksa."
        elif _return == "B":
            nar "Kamu meletakkan telapak tanganmu dengan tenang di atas layar ponsel yang tertutup, tidak menggesernya satu senti pun."
            yutaka "Nggak, Nagisa. Aku nggak mau menyerahkan ponselku. Menjaga privasi itu sama sekali nggak sama dengan menyembunyikan pengkhianatan."
            nar "Belum sempat kalimatmu selesai sepenuhnya, rona merah tajam langsung naik ke pipi Nagisa sampai ke pangkal pita twin-tailnya."
            nagisa "Aku cuma minta lihat sebentar! Kenapa kamu langsung bicara sedingin itu seolah-olah aku lagi menginterogasi orang asing?!"
            yutaka "Karena kalau setiap ponselku bunyi aku harus membuka layar buat membuktikan sesuatu, itu artinya dari awal kamu nggak percaya padaku."
            nagisa "Kalau kamu memang nggak menyembunyikan apa-apa, tinggal buka dua detik saja padahal semuanya langsung selesai! Buat apa kamu lindungi layar itu segitunya?!"
            yutaka "Bukan soal ada atau nggak ada yang disembunyikan, Nagisa. Aku cuma nggak mau hubungan kita jalan pakai curiga seperti itu."
            nar "Nagisa langsung mengatupkan bibir rapat. Ia menyambar tali tasnya di kursi sebelah dengan gerakan kasar hingga gantungan kelinci Koko di ritsletingnya beradu nyaring dengan pinggir meja, seolah hendak langsung pergi meninggalkan studio."
            nar "Namun langkahnya justru berhenti mematung tepat di samping meja gambar. Tangannya mencengkeram tali tas erat-erat sementara dadanya naik turun cepat, tidak sanggup melangkah keluar pintu sekaligus tidak punya cara memaksamu menurunkan tangan."
            nagisa "Selalu begitu... ujung-ujungnya aku lagi yang kelihatan salah karena terlalu peduli."
            yutaka "Aku nggak bilang kamu salah karena peduli, Nagisa. Aku cuma nggak mau kita saling mengawasi layar ponsel masing-masing."
            nagisa "Mengawasi?! Aku cuma tanya satu kali, Yutaka, dan kamu langsung pasang tembok setinggi itu di depan mukaku!"
            yutaka "Nagisa..."
            nagisa "...Sudah, terserah kamu deh, Yutaka. Simpan saja ponselmu baik-baik. Aku masih harus menyelesaikan garis ini sendirian."
            nar "Ia menjatuhkan tasnya kembali ke kursi tanpa menatapmu lagi, lalu menyambar penggaris besinya dengan bunyi denting keras di atas meja."
            nar "Di hadapan batas tegas yang tidak langsung kamu lunakkan, ketakutannya kehilangan jalan paling mudah untuk diredakan, meninggalkan jarak panas yang penuh curiga di antara kalian."
        else:
            yutaka "Ya sudah, sebentar ya. Aku tutup dulu tab lembar grafik kuliah yang lagi berantakan."
            nar "Kamu memiringkan layar sejenak menjauh dari sudut pandangnya dengan gerakan santai, memastikan hanya tampilan pesan aman dari grup kelas Ekonomi dan pesan singkat Koita soal alat tulis yang terbuka rapi di layar, menyimpan seluruh percakapan pribadi lain jauh di luar jangkauannya."
            nar "Begitu kamu menggeser ponsel itu melintasi meja gambar, Nagisa langsung menunduk memeriksanya cepat. Matanya menyapu barisan obrolan tentang tabel tugas kelompok dan pesan biasa Koita yang menanyakan bolpoin tertinggal di apartemenmu."
            nagisa "Oh... beneran cuma grup kelas sama pesan Ko-kun soal bolpoin ketinggalan, ya..."
            nagisa "Haha, beneran ada yang salah masukin angka nol di tabel anggaran kelompok... pantas tadi kamu sempat tersenyum tipis."
            yutaka "Kan sudah kubilang tadi, Nagisa. Memang cuma obrolan biasa."
            nar "Bahu Nagisa yang sejak tadi kaku langsung turun seluruhnya. Ia menyerahkan ponselmu kembali dengan kedua tangan, wajahnya berubah sungguh-sungguh merasa bersalah sampai telinganya ikut memerah."
            nagisa "Harusnya aku percaya sama kamu dari awal. Maaf banget ya, Yutaka, aku malah curiga aneh-aneh sampai minta cek ponselmu segala."
            yutaka "Nggak apa-apa, Nagisa. Yang penting sekarang kamu nggak cemas lagi."
            nagisa "Jangan bilang nggak apa-apa gitu, aku jadi makin merasa nggak enak tahu... Nanti habis aku rapikan garis sudut ini, biar aku yang traktir kopi dingin di mesin bawah buat minta maaf ya. Kali ini kamu nggak boleh menolak."
            yutaka "Iya. Selesaikan dulu garis tanggamu pelan-pelan."
            nagisa "Siap! Kalau ada pesan masuk lagi dari grup itu, nggak bakal kulirik lagi deh, janji."
            yutaka "{i}Ia bahkan sampai berjanji tidak akan melirik lagi karena merasa bersalah. Cukup satu layar yang dirapikan untuk mengubah curiganya menjadi rasa berutang budi.{/i}"
            nar "Ia tersenyum cerah dan kembali memegang pensil mekaniknya dengan gerakan mantap. Permintaan maafnya memudahkanmu menyimpan rapat seluruh sisi lain hidupmu dari matanya, tetapi di balik ketenangan manis itu tertanam satu bom waktu apabila suatu hari ia tahu rasa aman yang baru saja ia syukuri ternyata disusun untuk menipunya."
    return

# ┌─ PANDUAN CERITA · N15 · Natal Kedua: Ultimatum
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : "pilih aku atau mereka."
# │ INTI    : A pilih / B tolak / C manipulasi.
# │ AKHIRAN : stage 4 (titik balik).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N15:
    call kk_scene_enter("nagisa", "Gedung Arsitektur · Natal kedua")
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Lampu neon memanjang di langit-langit studio Gedung Arsitektur menyala putih terang di atas deretan meja gambar yang mulai kosong menjelang libur Natal. Dari balik kaca jendela lantai atas, hiasan lampu bulan Desember di halaman kampus berkelap-kelip diterpa angin dingin."
        else:
            nar "Cahaya dingin bulan Desember masuk miring melalui jendela kaca besar studio Gedung Arsitektur yang mulai sepi menjelang libur Natal. Aroma kertas kalkir, lem maket, dan kopi dingin masih menempel di sekitar meja kerja kayu."
        nar "Di koridor luar pintu studio, beberapa mahasiswa jurusan arsitektur terdengar sibuk menutup tabung gambar sambil saling tertawa dan melambaikan tangan pamit pulang."
        "Mahasiswa Arsitektur" "Duluan ya semua! Jangan lupa kumpulkan revisi denah pas masuk Januari nanti! Selamat Natal!"
        "Mahasiswi Arsitektur" "Selamat Natal juga! Sakurajima-san, kami kunci ruang bahan di ujung lorong ya, nanti kamu jangan kelamaan di studio sendirian!"
        nagisa "Iya, terima kasih. Selamat Natal juga ya, hati-hati di jalan."
        nar "Kamu berpapasan singkat dengan dua mahasiswa itu di ambang pintu sebelum melangkah masuk ke dalam studio yang mendadak begitu sunyi. Mahasiswi yang memeluk tabung gambar sempat menoleh lega melihat kedatanganmu."
        "Mahasiswi Arsitektur" "Oh, Amamiya-san datang nemenin Sakurajima-san ya? Syukurlah! Dari tadi dia duduk terus sendirian di sudut meja maket sambil megang ponsel, kami jadi agak khawatir ninggalin dia sendirian di gedung kosong."
        chiasa "Iya, nanti aku temani sampai dia beres kok. Selamat Natal ya, hati-hati di tangga."
        "Mahasiswa Arsitektur" "Siap, duluan ya, Amamiya-san!"
        nar "Pintu kayu studio menutup di belakang mereka, meninggalkan keheningan panjang yang hanya diisi dengung pelan pemanas ruangan. Di meja sudut dekat jendela, Sakurajima Nagisa duduk sendirian mengenakan sweter rajut krem dengan mantel hangat tersampir di sandaran kursinya."
        nar "Rambut pirang twin-tail berpita hitam-pink miliknya tampak terikat sangat rapi, sementara di ritsleting tas kain di samping sikunya bergantung gantungan kunci boneka kecil Koko yang ujung jahitannya mulai sedikit lusuh. Di atas meja maket tergeletak jangka gambar, gulungan kertas kalkir, serta dua gelas kertas cokelat panas yang sudah tidak mengepul lagi, satu di antaranya masih tertutup utuh di sisi kursi kosong seolah telah ia beli lebih dari satu jam lalu sambil menunggumu."
        nar "Tepat di antara kedua gelas dingin itu berdiri sebuah maket rumah kecil berjendela lebar buatan tugas akhirnya. Lampu baterai mungil di bagian dalam ruang tengah maket tersebut masih menyala kuning redup, seolah Nagisa lupa mematikannya sejak sore kemarin."
        chiasa "Nagisa-senpai? Tadi aku lihat pesan Senpai masuk separuh lalu hilang, kupikir ada barang Senpai yang ketinggalan di studio makanya aku langsung naik ke sini. Eh, maket rumah kecilnya rapi banget, lampunya masih menyala lho. Itu tugas desain akhir semester?"
        nagisa "Iya, desain rumah tinggal berjendela lebar buat evaluasi Januari nanti. Aku bikin lorong tengahnya serba kaca supaya orang di dalamnya bisa langsung lihat kalau ada yang pulang dan nggak pernah merasa dikurung di balik pintu tertutup."
        nar "Kamu menyentuh ringan salah satu gelas cokelat panas yang masih tertutup rapat di sisi meja dan langsung merasakan permukaannya sudah mendingin."
        chiasa "Ini cokelat panas buatku ya, Senpai? Maaf banget, aku nggak tahu Senpai sudah nunggu lama di studio sampai minumannya dingin begini."
        nagisa "Nggak apa-apa. Aku sendiri yang dari tadi ragu mau pencet kirim atau nggak."
        nar "Kamu baru melangkah tiga tapak mendekat ketika kamu melihat layar ponsel di tangan Nagisa masih menyala terang. Jari jempolnya baru saja menekan tombol hapus panjang, menghapus habis tiga paragraf teks yang tampak sudah ia ketik lalu edit berulang kali sepanjang hari."
        chiasa "Gedung Arsitektur sudah sepi banget ya menjelang libur. Oh iya, tahun ini Haruto-san jadi pulang ke rumah buat libur Natal bareng Senpai kan?"
        nar "Jari Nagisa berhenti sejenak di atas layar ponselnya yang kini sudah kosong. Senyum yang amat kecil dan datar sempat melintas di bibirnya sebelum lenyap lagi."
        nagisa "Tadi Onii-chan kirim pesan, katanya proyek kantornya lembur sampai tanggal dua puluh enam. Ia cuma kirim dua baris pesan minta maaf sama transfer uang jajan tambahan, seolah kupon kue bisa bikin meja makan rumah nggak kosong lagi kayak tahun lalu."
        chiasa "Ah... maaf, Nagisa-senpai, aku nggak tahu... Kalau Senpai masih mau membereskan meja dulu, biar aku bantu merapikan gulungan kertasnya terus kita turun ke stasiun bareng."
        nagisa "Nggak usah minta maaf. Aku sudah biasa melihat lampu ruang tengah rumah cuma menyala satu setiap akhir tahun. Lucu ya, bikin maket rumah mungil yang lampunya kelihatan hangat begini gampang banget, tinggal pasang baterai kecil. Tapi bikin orang beneran betah tinggal di dalam rumah yang asli susah banget."
        chiasa "Nagisa-senpai... dari tadi kamu sudah makan sesuatu belum selain cokelat panas dari mesin minuman itu? Wajahmu kelihatan agak pucat lho."
        nagisa "Sudah makan setengah roti manis tadi di koridor kok. Perutku nggak terlalu lapar kalau kepalaku lagi penuh pikiran."
        chiasa "Harusnya Senpai langsung meneleponku sejak tadi kalau memang lagi nggak enak hati, jangan duduk diam sendirian di studio dingin begini berjam-jam."
        nagisa "Kalau aku menelepon setiap kali merasa sepi, lama-lama kamu pasti juga bakal capek dengar suaraku, Chiasa-chan."
        nar "Kamu menatap wajahnya yang terlalu tenang di samping lampu maket yang berpendar lembut, baru menyadari betapa lama ia telah duduk menatap layar ponsel kosong di ruangan yang makin sepi ini."
        nar "Nagisa meletakkan ponselnya dalam posisi terbalik di atas meja maket. Saat ia mengangkat wajahnya, mata biru cerahnya menatapmu lurus tanpa air mata ataupun amarah yang meledak. Justru ketenangan suaranya terasa terlalu datar untuk kalimat yang sudah jelas ia timbang sejak lama."
        nagisa "Aku tadinya mau mengirimnya lewat pesan aja, Chiasa-chan. Tapi aku capek kalau nanti pesanku cuma kamu balas pakai stiker lucu atau janji ketemu lain hari. Jadi aku hapus semua biar bisa kukatakan langsung di depanmu."
        chiasa "Senpai... tanganmu dingin banget kelihatannya. Kenapa suaramu mendadak serius begitu? Ada masalah lagi sama anak-anak studio?"
        if kk_has("rute_yandere_nagisa"):
            nagisa "Bukan soal anak studio. Sejak bulan Oktober kemarin, aku terus ingat setiap janji yang pernah kamu ucapkan sambil terus melihat kamu tetap berdiri di antara semua orang yang sama."
        else:
            nagisa "Bukan soal anak studio, Chiasa-chan. Mereka semua sudah pulang merayakan Natal bareng orang-orang yang mereka pilih."
        nar "Di luar jendela kaca, tawa mahasiswa yang berjalan menuju gerbang kampus masih terdengar sayup membawa ucapan selamat Natal. Di dalam studio, Nagisa menarik napas pendek lalu meletakkan kedua tangannya rata di atas tepi meja gambar."
        nagisa "Aku, atau mereka, Chiasa-chan."
        chiasa "Eh? Sebentar, Nagisa-senpai, maksudnya apa tiba-tiba bilang begini? Ini kan bukan perlombaan yang harus ada pemenangnya... Memangnya ada kejadian apa sama Ko-nii atau teman-teman lain hari ini?"
        nagisa "Nggak perlu ada kejadian baru buat bikin aku sadar, Chiasa-chan. Melihat kalender liburan semua orang penuh duluan sementara aku lagi-lagi kebagian sisa waktu sudah lebih dari cukup."
        nagisa "Jangan jawab ini bukan perlombaan, dan jangan jawab semuanya penting. Aku sudah hafal kalimat itu, dan aku tahu kok Koita-kun, teman-teman seni rupamu, Tachibana-san, dan semua orang lain di sekitarmu itu memang penting buatmu."
        nagisa "Setiap kali seseorang bilang semua orang sama-sama penting, ujung-ujungnya selalu sama, aku yang duduk sendirian di ruang kosong sambil melihat semua orang lain pulang bareng orang pilihan mereka."
        nagisa "Aku nggak nanya siapa saja yang kamu anggap baik. Aku ingin tahu siapa yang akan kamu tinggalkan kalau hari ini kamu cuma boleh mempertahankan satu sisi."
        nar "Kamu tertegun memandangi sosok bertubuh mungil setinggi seratus lima puluh lima sentimeter di depanmu itu. Bahunya sedikit tegang di balik sweter rajutnya, dan jemarinya diam-diam meremas ujung tali tas tepat di samping gantungan Koko."
        nar "Ia tidak lagi sekadar meminta ditemani makan kue atau menghabiskan waktu Natal bersama. Di ruang studio yang hening ini, Nagisa sedang meminta seluruh peta hubunganmu menjadi jaminan mutlak bahwa dirinya tidak akan pernah lagi berada di urutan kedua lalu ditinggalkan."
        chiasa "{i}Kalau aku menjawab asal-asalan sekarang, tidak ada satu pun kalimat manis yang bisa meredam apa yang sedang menumpuk di belakang mata birunya.{/i}"
        call kk_family_menu("N15", ["\"Aku pilih kamu, Nagisa-senpai. Aku di sisimu.\"", "\"Maaf, Senpai, aku nggak bisa menerima ultimatum seperti itu.\"", "Tenangkan ia seolah ia menang tanpa benar-benar memutus yang lain."])
        if _return == "A":
            nar "Kamu menatap matanya yang tegang dan ketakutan di balik suara datarnya, lalu melangkah maju mendekati meja maket sebelum meletakkan tanganmu lembut di atas punggung tangannya yang dingin."
            chiasa "Aku pilih kamu, Nagisa-senpai. Aku nggak mau lihat Senpai terus merasa sendirian kayak begini. Aku berdiri di sisimu."
            nar "Nagisa membeku selama dua ketukan penuh, kelopak matanya mengerjap cepat seolah otaknya butuh waktu untuk memproses bahwa kamu benar-benar mengucapkan kalimat yang sejak lama ia tunggu."
            nar "Begitu kalimatmu meresap, ia langsung beranjak berdiri dan melangkah mendekat hingga bahunya nyaris menempel ke lengan mantelmu. Senyum lega merekah di wajahnya begitu cepat sampai dua bulir air mata justru baru jatuh di pipinya sesudah bibirnya tersenyum lebar."
            nagisa "...Beneran, Chiasa-chan? Kamu beneran memilihku? Sekarang aku nggak perlu takut lagi, kan?"
            chiasa "Iya, Senpai. Jangan menangis terus, pipimu nanti tambah dingin kena angin jendela."
            nar "Kamu mengusap pelan sudut pipinya yang basah dengan tisu saku, sementara Nagisa mencengkeram ujung lengan mantelmu dengan kedua tangannya sekuat tenaga seolah takut kamu menghilang jika pegangannya mengendur sedikit saja."
            nagisa "Sungguh ya, Chiasa-chan... sekarang aku nggak perlu takut lagi, kan? Aku nggak perlu lagi mikir kamu bakal pergi duluan pas Koita-kun atau orang lain manggil?"
            chiasa "Iya, aku dengar kok, Nagisa-senpai. Tarik napas pelan-pelan dulu ya."
            nar "Ia mengangguk-angguk cepat dengan mata biru yang masih berkilau basah, lalu segera menghapus jejak air matanya sendiri dengan punggung tangan. Tangannya mematikan sakelar kecil lampu maket rumah di atas meja, lalu merogoh buku agenda saku bersampul merah muda dari dalam tasnya."
            nar "Belum sampai satu menit setelah tangisnya reda, nada suaranya sudah kembali rapat oleh ketegangan baru yang menyamar sebagai rencana liburan."
            nagisa "Kalau begitu, kita tulis sekarang aja ya jadwal liburannya biar jelas! Tanggal dua puluh empat, dua puluh lima, sama dua puluh enam kamu kosong buatku kan? Jam berapa kita ketemu supaya nggak ada yang sempat bikin janji duluan sama kamu?"
            nar "Ia membuka halaman kalender bulan Desember di buku agenda merah mudanya, lalu menyodorkan pena gel berwarna merah muda ke tanganmu sambil menatap kalender di layar ponselmu."
            nagisa "Tulis sendiri namamu di kotak tanggal dua puluh empat sama dua puluh lima pakai penaku ya, Chiasa-chan. Biar tiap aku bangun tidur dan buka buku ini, aku lihat tulisan tanganmu sendiri dan tahu ini beneran bukan cuma kalimat pengantar tidur."
            chiasa "Eh... iya, sebentar aku tulis. Tapi nanti aku tetap harus izin sebentar di rumah ya, Senpai."
            nar "Kamu sempat menahan napas setengah detik menatap kotak tanggal yang kosong di buku agenda itu, lalu menuliskan namamu perlahan. Begitu ujung penamu terangkat, Nagisa langsung mendekap buku agenda terbuka itu sebentar di depan dadanya dengan raut lega yang teramat dalam."
            nar "Jari ibu jarinya menyentuh pelan tepi kertas di dekat goresan tinta merah muda namamu, seolah sedang memastikan huruf-huruf itu sungguh ada dan tidak akan memudar begitu halaman ditutup."
            nagisa "Akhirnya kotak tanggal merah bulan Desember di bukuku nggak kosong lagi tahun ini..."
            chiasa "Tulisan tanganku agak berantakan ya gara-gara jariku dingin."
            nagisa "Nggak apa-apa, justru aku suka banget. Jadi aku tahu persis kamu sendiri yang menulisnya di sini."
            nar "Ia mengembalikan tutup pena dengan gerakan lembut, tetapi sorot mata biru cerahnya yang masih agak basah segera kembali menyiratkan kecemasan yang terlalu mudah terusik."
            nar "Nagisa menyandarkan keningnya sebentar ke bahu mantelmu, suaranya mendadak melirih nyaris seperti anak kecil yang kelelahan berjaga sendirian."
            nagisa "Aku sebenarnya benci banget kelihatan serba menuntut begini, Chiasa-chan... aku cuma takut banget kalau aku lengah satu detik aja, semua orang lain langsung menarikmu pergi lagi."
            nagisa "Kalau misal tanggal dua puluh empat nanti Koita-kun mendadak telepon minta bantuan di jam yang sama, kamu tetap mendahulukan janji sama aku kan? Dan tolong jangan matikan suara ponselmu selama liburan ya."
            chiasa "Aku sudah bilang aku memilihmu, Nagisa-senpai. Aku nggak bakal membatalkan janji kita begitu saja."
            nagisa "Nggak masalah, yang penting kamu langsung kasih tahu aku duluan setiap kali ponselmu bunyi ada pesan dari anak klub lain atau dari rumah ya. Soalnya aku nggak mau ada salah paham kecil lagi kayak kemarin."
            nagisa "Kalau kita saling kasih tahu setiap rencana dari awal dan nggak ada yang disembunyikan, nggak bakal ada orang luar yang bisa nyelip di tengah-tengah kita lagi."
            nar "Kamu sempat menoleh ke meja ketika layar ponselmu menyala sebentar memunculkan notifikasi pengingat cuaca. Mata biru cerah Nagisa langsung refleks melirik cepat ke arah layar itu sebelum kembali tersenyum manis kepadamu."
            chiasa "Cuma pengingat prakiraan hujan salju kok, Senpai."
            nagisa "Fufu, syukurlah. Aku cuma nggak mau ada hal mendadak yang merusak liburan kita. Ayo keluar dari studio sekarang, di sini mulai dingin."
            nar "Nagisa tersenyum begitu cerah sambil merapikan tasnya dan meraih gantungan kunci Koko dengan gerakan lembut, lalu menyelipkan lengannya erat ke lenganmu saat kalian melangkah menuju pintu studio."
            nar "Sepanjang menuruni tangga Gedung Arsitektur yang sepi, setiap beberapa anak tangga Nagisa sempat menoleh singkat memeriksa raut wajahmu seolah ingin memastikan senyummu belum memudar sedikit pun."
            nagisa "Kamu nggak menyesal kan sudah memilihku tadi, Chiasa-chan?"
            chiasa "Nggak, Senpai. Ayo hati-hati di tangga, licin."
            chiasa "{i}Aku sudah memberinya jawaban yang paling ia inginkan... tapi cara matanya langsung mencari kepastian baru bahkan sebelum kami keluar dari ruangan ini bikin dadaku ikut sesak.{/i}"
            nar "Jawabanmu memang telah memberinya kepastian penuh untuk saat ini. Namun jauh di dalam sorot mata biru cerahnya, kecemasan Nagisa sudah segera mulai mencari bukti baru bahwa pilihanmu itu akan tetap berlaku setiap kali wajah orang lain muncul di hadapan kalian."
        elif _return == "B":
            nar "Kamu menarik napas perlahan, tetap berdiri di tempatmu dengan sorot mata tenang meski jantungmu berdetak keras, lalu menggeleng pelan menolak syarat yang baru saja ia bentangkan di atas meja."
            chiasa "Maaf, Nagisa-senpai... aku nggak bisa menerima ultimatum seperti itu. Aku peduli sama Senpai, sungguh. Tapi aku nggak bisa memutus hubunganku sama Ko-nii dan teman-teman lain cuma buat membuktikan sesuatu."
            chiasa "Menolak disuruh memilih begini bukan berarti aku mau meninggalkan Senpai atau menganggap Senpai nggak penting. Aku tetap mau merayakan libur Natal sama Senpai kok, tanpa harus menghapus orang lain dari hidupku."
            nar "Suasana studio langsung membeku. Nagisa menatapmu tanpa berkedip sedikit pun, seolah seluruh kalimat penjelasan di bagian belakang sama sekali tidak masuk ke telinganya, dan penolakan terhadap ultimatum hanya mungkin memiliki satu arti, yaitu penolakan terhadap dirinya sendiri."
            nagisa "...Begitu, ya. Jadi pada akhirnya aku masih yang harus mengerti."
            chiasa "Nagisa-senpai, tolong dengarkan dulu penjelasanku baik-baik..."
            nagisa "Selalu begitu dari dulu, Chiasa-chan. Waktu Onii-chan sibuk kerja sampai lupa pulang, aku yang disuruh mengerti. Waktu Koita-kun ramah ke semua cewek di kampus, aku lagi yang harus senyum dan mengerti."
            nagisa "Berbagi sisa waktu setelah kamu selesai melayani semua orang lain bukan berarti kamu memilihku, Chiasa-chan. Sekarang waktu aku akhirnya berani minta satu tempat yang jelas darimu, jawabannya tetap sama."
            nagisa "Aku tetap harus berdiri di pinggir sambil melihat kamu menjaga perasaan semua orang lain duluan."
            chiasa "Bukan begitu, Senpai! Duduk dulu dua menit saja dan tarik napas sebentar! Aku benar-benar peduli sama Senpai sejak musim gugur kemarin, tapi kalau hubungan dibangun dengan membuang semua orang di sekitar kita, ujung-ujungnya kita berdua juga yang bakal terluka!"
            nar "Nagisa menggeleng tajam hingga ujung rambut pirang twin-tail berpita hitam-pink miliknya terayun cepat. Mata birunya tampak berkaca-kaca tipis, tetapi ia menahannya keras agar tidak satu tetes pun jatuh di depanmu."
            nagisa "Kalau kamu bilang peduli tapi tetap nggak berani melepaskan satu orang pun demi aku, bedanya kamu sama Koita-kun yang ramah ke semua orang apa, Chiasa-chan?"
            nar "Perbandingan tajam itu langsung menghantam dadamu hingga kalimat pembelaanmu tertahan di tenggorokan. Kamu menelan gugup lalu menjawab sepelan dan sejujur yang kamu mampu."
            chiasa "Aku nggak pernah menganggap Senpai cadangan! Aku cuma nggak percaya kedekatan yang sehat bisa tumbuh kalau aku harus membuang semua orang lain dari hidupku."
            nagisa "Mudah sekali bicara soal hubungan yang sehat kalau rumahmu selalu ada lampu menyala dan suara orang yang menunggumu pulang, Chiasa-chan."
            nar "Kamu refleks melangkah maju setengah tapak sambil mengulurkan tangan hendak menyentuh lengan sweternya pelan, berharap suaramu masih bisa menembus dingin yang baru saja turun di antara kalian."
            chiasa "Nagisa-senpai, aku tahu rasanya kesepian di rumah besar yang kosong itu berat banget, tapi tolong jangan tutup telinga dulu..."
            nar "Nagisa langsung mundur setengah langkah menghindari sentuhan jarimu dengan tatapan yang begitu dingin hingga tanganmu tertahan di udara."
            nagisa "Kamu nggak tahu rasanya pulang ke rumah yang sama sekali nggak ada suara orang lain selama berhari-hari, Chiasa-chan. Jangan pura-pura paham cuma buat menenangkan aku lima menit."
            nagisa "Nggak usah mengajari aku soal luka, Chiasa-chan. Aku sudah hafal rasanya jauh sebelum kamu pindah masuk ke kampus ini."
            nar "Ia memutar badan cepat membelakangimu dan mulai memasukkan buku catatan, penggaris skala, serta tempat pensilnya ke dalam tas kain. Kamu bisa melihat jelas kedua tangannya gemetar saat menarik ritsleting tas sampai tempat pensilnya tergelincir jatuh ke lantai kayu."
            nar "Begitu kamu refleks membungkuk hendak mengambilkannya, Nagisa langsung menyambar tempat pensil itu lebih cepat sampai ujung jarinya hampir menyentuh tanganmu, sementara gantungan kunci Koko berayun keras membentur tepi meja."
            chiasa "Tunggu, Nagisa-senpai, tanganmu masih gemetar begitu. Biar aku antar jalan sampai gerbang atau stasiun ya, di luar anginnya kencang banget."
            nagisa "Nggak usah. Jangan sentuh barangku. Kamu kan sibuk harus menjaga perasaan banyak orang. Jangan buang waktumu mengantar orang yang cuma bikin repot."
            nar "Nagisa menyampirkan mantelnya terburu-buru di atas satu bahu, meraih tali tasnya erat, lalu melangkah cepat melewati dirimu tanpa sedikit pun menoleh lagi. Pintu kayu studio berderit lalu menutup cukup keras menggema di koridor kosong."
            nar "Kamu sempat melangkah dua tapak menuju ambang pintu, tetapi bunyi langkah sepatu cepatnya sudah menghilang menuruni tangga darurat Gedung Arsitektur. Di atas meja maket hanya tersisa dua gelas kertas cokelat panas yang sudah dingin total dan lampu kecil maket rumah yang masih menyala sendirian."
            nar "Kamu berjalan perlahan kembali ke meja kayu itu, menemukan satu jepit rambut kecil berbentuk silang merah muda milik Nagisa yang terlepas di samping alas potong maket. Kamu memungutnya pelan, lalu menekan sakelar baterai kecil di bawah maket rumah agar lampu mungilnya tidak terus menyala sendirian sampai habis di ruang kosong."
            nar "Setelah memastikan semua lampu neon studio padam satu per satu, kamu melangkah keluar ke koridor yang dingin sambil menggenggam jepit rambut merah muda itu di saku mantelmu."
            chiasa "{i}Aku tahu aku nggak boleh tunduk pada ultimatum itu... tapi melihat tangannya gemetar waktu pergi sendirian barusan, aku sama sekali nggak tenang memikirkan siapa yang bakal ia hubungi selanjutnya.{/i}"
            nar "Kamu berdiri lama di tengah studio yang hening, tidak tahu apakah ia akan pulang menemui Haruto, mengurung diri sendirian, atau membiarkan rasa takutnya di dalam kepala berubah pelan-pelan menjadi tindakan yang tidak lagi bisa kamu cegah."
        else:
            nar "Kamu melihat betapa tegangnya bahu Nagisa dan betapa rapuh ketenangannya di balik ultimatum itu. Kamu tidak ingin memutus seluruh hubunganmu dengan orang lain, tetapi kamu juga tidak sanggup menghadapi ledakan jika menolak langsung. Maka kamu memilih merangkai jawaban lunak yang terdengar seperti kemenangan baginya."
            chiasa "Nagisa-senpai, dengar aku dulu ya. Senpai tuh nggak perlu bikin perbandingan aneh-aneh sama mereka semua. Dari dulu kamu kan sudah tahu sendiri tempat Senpai di hidupku itu beda banget dibanding teman-teman kampus lain."
            nar "Kamu melangkah mendekat setengah langkah dan menyentuh lembut punggung tangannya sambil tersenyum menenangkan, sengaja menghindari kalimat pasti tentang meninggalkan Koita ataupun yang lain."
            chiasa "Mana mungkin aku lupa sama Senpai cuma gara-gara urusan lain? Kalau Senpai butuh aku, aku selalu usahakan datang buat Senpai kan? Jadi nggak usah mikir yang berat-berat lagi ya pas liburan Natal begini."
            nar "Sorot mata biru Nagisa menyipit sejenak menyaring seluruh kalimatmu. Ia belum langsung melepaskan ketegangan di bahunya, justru memiringkan wajah untuk menguji apakah kalimat manismu itu benar-benar memiliki isi."
            nagisa "...Jadi tempatku memang berbeda dari mereka semua? Berarti kalau nanti Koita-kun atau anak-anak klub lain mengajakmu pergi di hari yang sama, kamu bakal mengutamakan aku duluan kan, Chiasa-chan?"
            chiasa "Aduh, Senpai, tentu saja aku bakal cari cara buat nemuin Senpai duluan kok. Buatku waktu berdua sama Senpai selalu beda rasanya dibanding keramaian di klub. Mana mungkin aku membiarkan Senpai nunggu sendirian."
            nagisa "Kalau tengah malam aku telepon karena rumah terlalu sepi juga kamu nggak bakal bilang lagi sibuk sama orang lain kan?"
            chiasa "Mana mungkin aku mengabaikan telepon Senpai kalau Senpai lagi sedih sendirian di rumah? Sekarang wajahnya jangan tegang lagi ya, nanti pusing lho."
            nar "Kamu sengaja menjaga nada suaramu selembut dan sehangat mungkin agar tidak satu pun kalimatmu terasa seperti penolakan, sekaligus tanpa pernah berjanji secara nyata akan memutus hubungan dengan siapa pun."
            nar "Persis seperti seseorang yang terlalu lelah menahan napas, Nagisa akhirnya memilih menyingkirkan seluruh kata bersyarat di belakang ucapanmu dan hanya menggenggam erat potongan kalimat yang terdengar paling pasti agar dadanya bisa bernapas lega."
            nar "Ketegangan di bahu Nagisa langsung luruh dalam satu tarikan napas panjang. Senyum lega perlahan kembali naik ke bibirnya, meski sorot matanya masih memegang kalimatmu dengan kesungguhan yang jauh lebih keras dari niatmu."
            nagisa "Syukurlah... aku sempat takut banget kamu bakal jawab sama persis kayak orang-orang lain. Maaf ya tadi aku bicara terlalu kaku, aku cuma terlalu cemas seharian ini."
            chiasa "Nggak apa-apa, Senpai. Aku ngerti kok kamu lagi capek gara-gara tugas maket juga."
            nar "Ia membuka buku agenda sakunya sebentar dan menggambar satu bintang kecil dengan pena merah muda tepat di kolom tanggal libur Natal berikutnya, lalu menutup bukunya perlahan."
            nar "Ia merapikan tempat pensilnya ke dalam tas kain dengan tenang, lalu berhenti tepat sebelum menyandang tasnya dan menatap lurus ke matamu dengan keseriusan yang membuat tengkukmu sedikit dingin."
            nagisa "Aku ingat persis semua yang baru kamu bilang tadi, Chiasa-chan. Aku bakal pegang itu baik-baik. Jadi nanti kalau ada kejadian apa-apa di depan orang lain, jangan pernah bilang aku cuma salah paham ya."
            chiasa "Ah... iya, Nagisa-senpai."
            nagisa "Kalau begitu ayo kita turun bareng sampai gerbang depan. Di dekat stasiun ada toko kue tart stroberi kecil yang kemarin kulihat di majalah, besok kita mampir ke sana ya mumpung kamu sudah nggak perlu sibuk mengurus rencana Koita-kun atau Tachibana-san lagi."
            chiasa "Iya, nanti kita lihat jam bukanya bareng ya, Senpai."
            nar "Nagisa tersenyum manis sambil menepuk lembut gantungan boneka Koko di ritsleting tasnya lalu menggandeng ujung lengan mantelmu menuju pintu studio, langkahnya jauh lebih ringan dari sepuluh menit lalu."
            nar "Menuruni tangga Gedung Arsitektur yang sepi, jari-jarinya melingkar hangat di lenganmu sambil terus bercerita riang soal hiasan etalase kue tart, sementara setiap kalimat rencananya mengunci hari-harimu satu per satu."
            nagisa "Oh iya, kamu masih ingat kan rasa kue yang paling kusuka waktu kita pertama kali beli jajan bareng di musim semi dulu?"
            chiasa "Kue tart stroberi yang krimnya nggak terlalu manis kan, Senpai?"
            nagisa "Fufu, tuh kan! Kamu memang paling ingat hal-hal kecil tentangku dibanding siapa pun. Rasanya lega banget tahu aku nggak salah memilih untuk percaya sama kamu."
            nar "Kamu membalas celotehannya tentang kue tart dengan senyum kaku sambil merasakan jerat halus dari kata-katamu sendiri mulai mengencang."
            chiasa "{i}Suasana memang langsung tenang lagi... tapi aku tahu persis ia pulang membawa janji yang sebenarnya nggak sanggup kutanggung kalau hari itu benar-benar datang.{/i}"
            nar "Ia pulang dengan membawa keyakinan mutlak yang tidak pernah benar-benar kamu niatkan untuk ditepati. Kedamaian sesaat di libur Natal ini baru saja kamu beli dengan utang luka yang jauh lebih besar ketika makna kata-kata kalian akhirnya bertabrakan nanti."
    else:
        nar "Nagisa menghapus pesan yang baru diketikkannya dan memilih mengatakannya langsung. Di luar studio orang-orang saling mengucapkan selamat Natal; di dalam, suaranya terlalu tenang untuk kalimat yang disiapkan sepanjang hari."
        nagisa "Aku, atau mereka. Jangan jawab semuanya penting. Aku tahu mereka penting. Aku ingin tahu siapa yang akan kamu tinggalkan kalau harus memilih."
        nar "Ia tidak lagi meminta malam bersama. Ia sedang meminta seluruh hubunganmu menjadi jaminan bahwa dirinya tak akan ditinggalkan."
        call kk_family_menu("N15", ["Pilih Nagisa.", "Tolak ultimatum itu.", "Manipulasi agar ia merasa menang tanpa kau memilih."])
        if _return == "A":
            nar "Kau memilihnya. Nagisa mendekat, lega begitu cepat sampai air matanya baru keluar sesudah ia tersenyum."
            nagisa "Sekarang aku nggak perlu takut lagi, kan?"
            nar "Ia menanyakan hal itu dua kali. Jawabanmu telah memberinya kepastian tentang malam ini, tetapi kecemasannya segera mulai mencari bukti bahwa pilihan itu akan berlaku setiap kali orang lain muncul."
        elif _return == "B":
            nar "Kau menolak syarat tersebut. Nagisa menatapmu seolah penolakan terhadap ultimatum hanya mungkin berarti penolakan terhadap dirinya."
            nagisa "Jadi aku masih yang harus mengerti. Selalu begitu."
            nar "Tangannya gemetar saat menutup tas. Ia pergi tanpa meminta ditemani. Kau tidak tahu siapa yang akan dihubunginya atau apakah ia akan membiarkan seseorang mendengar sebelum takut berubah menjadi tindakan."
        else:
            nar "Kau memberinya kesan menang tanpa mengambil keputusan yang ia minta. Nagisa memegang bagian perkataanmu yang terdengar paling pasti, menyingkirkan sisanya agar bisa bernapas lega."
            nagisa "Aku ingat yang kamu bilang. Jangan nanti bilang aku salah paham."
            nar "Ia pulang membawa sebuah janji yang tidak ingin kautanggung. Kedamaian malam itu dibeli dengan kemungkinan luka yang lebih besar ketika arti kata-kata kalian akhirnya bertemu."
    return

# ┌─ PANDUAN CERITA · N16 · Hari Bentrok
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : ia menyatakan perasaan pada pemain atau Koita.
# │ INTI    : A terima / B tolak / C alihkan.
# │ AKHIRAN : hub besar #8.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N16:
    call kk_scene_enter("nagisa", "Gedung Arsitektur · Hari bentrok")
    nar "Nagisa menghampirimu di luar studio dengan kalimat yang tampaknya sudah diulang berkali-kali sendirian. Ketika mulai bicara, ia justru membuang kalimat pembukanya."
    nagisa "Aku menyukaimu. Aku nggak mau menyebutnya cuma khawatir atau kebiasaan lagi. Dan aku nggak mau kalah karena orang lain berani bicara lebih dulu."
    nar "Ia menyadari kata kalah setelah mengucapkannya, tetapi terlalu takut untuk memperbaiki."
    nagisa "Jangan jawab karena kasihan. Tapi jangan bercanda juga. Tolong."
    call kk_family_menu("N16", ["Terima perasaannya.", "Tolak dengan jujur.", "Alihkan jawabannya."])
    if _return == "A":
        nar "Kau menerima perasaannya. Nagisa menutup mata sebentar, seperti baru selesai menahan napas yang sudah dimulai bertahun-tahun lalu."
        nagisa "Aku senang. Aku juga takut kamu berubah pikiran setelah melihat aku yang sebenarnya."
        nar "Ia meraih tanganmu terlalu erat, kemudian mengendurkan ketika kau bergerak. Menerima cinta ini membuka kedekatan; cara kalian memperlakukan ketakutannya akan menentukan apa yang tumbuh di dalamnya."
    elif _return == "B":
        nar "Kau menolak dengan jelas. Nagisa mengangguk berkali-kali, tersenyum dengan wajah yang semakin pucat."
        nagisa "Aku minta jujur, kan. Kamu sudah jujur. Bagus."
        nar "Ia melangkah pergi sebelum senyum itu jatuh. Penolakanmu bukan kesalahan, tetapi ketenangan yang ia pakai untuk membungkusnya tidak tampak seperti sesuatu yang dapat bertahan sendirian."
    else:
        nar "Kau mengalihkan jawaban ke waktu yang buruk dan keadaan yang rumit. Nagisa memegang kata nanti sebelum kau benar-benar menjanjikannya."
        nagisa "Aku bisa menunggu. Aku sudah pandai soal itu."
        nar "Ia mengucapkannya sebagai bukti kesungguhan. Kau mendengar betapa mudah satu penghindaran baru bisa ditumpuk di atas penantian lama yang belum pernah ia akui menyakitkan."
    return

# ┌─ PANDUAN CERITA · N17 · Gantungan Kunci yang Hilang
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : ia menuduh orang lain.
# │ INTI    : A selidiki / B pasang jebakan / C tuduh balik.
# │ AKHIRAN : titik pemulihan terakhir; setelah ini hanya Distorted Ending.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N17:
    call kk_scene_enter("nagisa", "Gedung Arsitektur · Gantungan kunci hilang")
    nar "Nagisa mengeluarkan isi tas di atas meja. Tempat gantungan kunci itu biasa terpasang kosong; yang tidak kosong adalah daftar orang yang sudah ia salahkan dalam kepalanya."
    nagisa "Orang itu terakhir berdiri dekat tasmu. Terus barang dariku hilang. Kamu masih mau bilang nggak ada hubungannya?"
    nar "Ia punya urutan kejadian, tetapi belum punya alasan untuk menganggap urutan itu bukti. Ketakutannya sudah melompati jarak tersebut."
    call kk_family_menu("N17", ["Selidiki dengan tenang sebelum menuduh.", "Biarkan ia memasang jebakan untuk orang itu.", "Tuduh balik agar ia ragu."])
    if _return == "A":
        nar "Kau mengajaknya mencari tanpa menghubungi orang yang dituduh terlebih dahulu. Nagisa protes, lalu mengikuti ketika kau menolak menjadikan keberpihakan sebagai syarat mencari kebenaran."
        nar "Gantungan itu akhirnya ditemukan di antara barang yang dipindahkan sebelumnya. Tak ada pencuri, hanya kesimpulan yang telanjur diinginkan."
        nagisa "Aku sudah hampir... aku tahu. Jangan selesaikan kalimatnya untukku. Aku harus memikirkan apa yang tadi ingin kulakukan."
        nar "Ia duduk lama. Kali ini rasa malu tidak boleh diselesaikan dengan mencari orang baru untuk disalahkan."
    elif _return == "B":
        nar "Kau membiarkan tuduhannya menjadi tindakan. Sesudahnya seseorang yang tidak bersalah dipanggil untuk menjelaskan hal yang tidak pernah diperbuat, sementara teman-temannya mulai menjaga jarak."
        nagisa "Sekarang kamu tahu aku nggak cuma diam kalau ada yang mengganggu kita."
        nar "Ia menunggu persetujuanmu. Orang yang terseret kehilangan rasa aman di studio; Nagisa justru mulai mempercayai bahwa menyingkirkan orang lain adalah cara paling jelas membuktikan cinta."
    else:
        nar "Kau menuduhnya sengaja membuat persoalan. Nagisa berdiri begitu cepat kursinya bergeser keras."
        nagisa "Jadi sekarang aku yang harus dibuktikan salah? Kamu bahkan belum dengar semuanya!"
        nar "Ia membela dirinya, bukan memeriksa tuduhannya. Percakapan yang bisa saja menahannya justru berubah menjadi bukti lain bahwa orang lain selalu lebih mudah dipercaya daripada dirinya."
    return

# ┌─ PANDUAN CERITA · N18 · Fuuto dan Sabotase
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : Nagisa mengganggu pesaing.
# │ INTI    : A hentikan / B biarkan / C menjadi korban.
# │ AKHIRAN : stage 5.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N18:
    call kk_scene_enter("nagisa", "Gedung Arsitektur · Sabotase")
    nar "Fuuto berhenti duduk di meja yang sama. Saat ditanya, ia menyebut ingin menghindari masalah, menatap Nagisa sebentar, lalu membawa pekerjaannya pergi."
    nagisa "Bagus kalau dia paham sendiri. Aku sudah capek melihatnya cari alasan dekat denganmu."
    nar "Ia mengatakannya hampir lega. Yang paling mengusik adalah betapa ia mengira kau akan merasakan kelegaan yang sama."
    call kk_family_menu("N18", ["Hentikan ia sebelum keterlaluan.", "Biarkan ia berjalan terus.", "Jadikan dirimu seolah korban untuk mengikatnya lebih dalam."])
    if _return == "A":
        nar "Kau menghentikannya dan menyebut dampaknya kepada Fuuto tanpa memperdebatkan siapa yang lebih penting bagimu. Nagisa mencoba mengalihkan, lalu kehilangan kata-kata ketika kau tetap pada pokok itu."
        nagisa "Aku cuma takut kalau dia ada, kamu nggak memilih duduk denganku lagi."
        nar "Kau mendengar ketakutannya tanpa menerima perbuatannya. Untuk pertama kalinya malam itu, ia harus memikirkan apa yang telah dilakukan kepada seseorang yang tidak sedang bertanggung jawab atas rasa takutnya."
    elif _return == "B":
        nar "Kau tidak menghentikan. Gangguan itu berlanjut sampai kesempatan dan pekerjaan Fuuto ikut rusak. Ia mulai menghindari studio yang seharusnya menjadi tempat belajarnya."
        nagisa "Akhirnya lebih tenang. Kita bisa kerja tanpa diganggu."
        nar "Ia menyiapkan kursi untukmu dengan hangat. Keamanan yang ditawarkannya dibangun dari ketidakamanan orang lain, dan diammu telah diterima sebagai persetujuan."
    else:
        nar "Kau menempatkan dirimu sebagai orang yang harus ia bela, membiarkan luka yang kautampilkan mengarahkan amarahnya lebih jauh. Nagisa segera berpindah dari mencari kepastian ke menjanjikan perlindungan."
        nagisa "Aku nggak akan membiarkan siapa pun memperlakukanmu begitu. Kamu cukup percaya aku."
        nar "Ia tidak memeriksa bagian ceritamu yang kabur. Kau memperoleh kesetiaan yang makin keras, sementara orang di luar kalian berdua menjadi sasaran dari rasa takut yang sengaja kaupelihara."
    return

init 1 python:
    _hook("N14-A", lambda: (kk_rel("nagisa","trust",4), kk_nagisa_stage(3)))
    _hook("N14-B", lambda: (kk_rel("nagisa","jeal",10), kk_nagisa_stage(3)))
    _hook("N14-C", lambda: (kk_adj("luka_bohong",10), kk_nagisa_stage(3), kk_flag("rute_yandere_nagisa")))
    _hook("N15-A", lambda: (kk_adj("kelekatan_nagisa",15), kk_nagisa_stage(4), kk_flag("nagisa_dipilih")))
    _hook("N15-B", lambda: (kk_rel("nagisa","fear",8), kk_nagisa_stage(4)))
    _hook("N15-C", lambda: (kk_adj("luka_bohong",12), kk_nagisa_stage(4)))
    _hook("N16-A", lambda: (kk_rel("nagisa","intim",8), kk_flag("nagisa_diterima")))
    _hook("N16-B", lambda: (kk_rel("nagisa","jeal",12), kk_flag("nagisa_ditolak_keras")))
    _hook("N16-C", lambda: kk_rel("nagisa","jeal",6))
    _hook("N17-A", lambda: (kk_rel("nagisa","trust",5), kk_flag("nagisa_pemulihan_terakhir")))
    _hook("N17-B", lambda: (kk_nagisa_stage(5), kk_flag("nagisa_jebakan_dipasang")))
    _hook("N17-C", lambda: kk_rel("nagisa","jeal",8))
    _hook("N18-A", lambda: (kk_rel("nagisa","trust",4), kk_flag("nagisa_dihentikan")))
    _hook("N18-B", lambda: (kk_nagisa_stage(5), kk_flag("yuuto_disabotase")))
    _hook("N18-C", lambda: (kk_adj("kelekatan_nagisa",20), kk_nagisa_stage(5), kk_flag("nagisa_distorted")))
