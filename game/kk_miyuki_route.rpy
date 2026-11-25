# Milestone utama Miyuki tahun 2-3 (Mi14-Mi23, Mi26): arc "Rute Masokis" —
# Miyuki menormalisasi menyalahkan diri dan penyerahan emosional di bawah tekanan
# supervisor/karier/keluarga. DITULIS sebagai KONSEKUENSI dan KARAKTER: pilihan
# "manfaatkan" dicatat singkat tanpa metode; opsi pemulihan (Yuina/Sato Kyoko)
# selalu tersedia. Bukan Force. Efek menggerakkan stage[miyuki], luka_miyuki_diri,
# omiai_takeru, dan bendera pemulihan. Nilai prototipe; mengikuti Event_Miyuki.

init 1 python:
    def kk_miyuki_stage(n):
        kk_stage("miyuki", max(n, stage.get("miyuki", 0)))

# ┌─ PANDUAN CERITA · Mi14 · Hujan di Bangsal
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : ia dimarahi supervisor.
# │ INTI    : A hibur / B bela / C kritik Miyuki.
# │ AKHIRAN : stage 2 (dimarahi = diperhatikan).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi14:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana · Hujan di bangsal")
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Hujan deras bulan Juni memukul keras kaca jendela tinggi koridor lantai tiga Rumah Sakit Tachibana yang diterangi lampu putih dingin."
        else:
            nar "Langit musim hujan bulan Juni tampak kelabu gelap di balik kaca tinggi koridor lantai tiga Rumah Sakit Tachibana. Bunyi air hujan menghantam kaca beradu dengan langkah sunyi sepatu di atas lantai linoleum yang bersih."
        nar "Kamu duduk di bangku tunggu sudut dekat meja perawat sambil memegangi kantong roti hangat yang tadinya berniat kamu titipkan untuk jeda jaga Tachibana Miyuki."
        nar "Tepat ketika kamu hendak berdiri mengecek jam pergantian rotasi, pintu geser salah satu kamar bangsal anak terbuka setengah dan suara tajam seorang pria paruh baya langsung memotong kesunyian koridor."
        "Dokter Pembimbing" "Tachibana, ini lembar catatan grafik pasien yang resmi! Jangan disamakan dengan buku catatan kuliah biasa! Bagaimana bisa kamu melompati kolom waktu observasi kedua, lalu masih sempat-sempatnya tersenyum mengajak bicara ibu pasien padahal tabelmu sendiri belum rapi?!"
        nar "Bunyi ketukan jari yang cukup keras menghantam papan jepit kertas bergema hingga keluar pintu. Di dalam kamar yang terbuka separuh itu, suara obrolan keluarga pasien langsung terhenti canggung. Beberapa perawat di dekat konter melirik sebentar sebelum segera menunduk kembali."
        "Dokter Pembimbing" "Jangan membawa kebiasaan santai mahasiswa ke bangsal saya. Periksa ulang semuanya dan serahkan lagi sebelum pergantian jaga!"
        nar "Dokter pembimbing berjas panjang itu melangkah keluar dengan wajah dingin, berjalan cepat melewati bangku tunggumu menuju ujung koridor tanpa menoleh sedikit pun."
        nar "Dua detik kemudian, Tachibana Miyuki melangkah keluar dari kamar bangsal sambil menutup pintu gesernya sangat pelan. Wajahnya tampak pucat di bawah rambut hitam panjang lurus yang terurai rapi, jemarinya mencengkeram papan jepit catatan hingga buku-buku jarinya memutih."
        chiasa "Tachibana-senpai! Senpai nggak apa-apa?"
        nar "Kamu langsung bangkit menghampiri dan menyentuh pelan lengan jas dokternya. Miyuki mengerjap cepat mendengar suaramu, lalu buru-buru menarik sudut bibirnya membentuk senyum tipis yang terasa rapuh."
        miyuki "Eh, Chiasa-chan? Aduh, maaf banget kamu malah jadi lihat kejadian barusan... aku nggak apa-apa kok, sungguh. Memang ada bagian yang harus kubetulkan di lembar grafik ini. Sensei benar soal kolom waktunya."
        chiasa "Tapi tadi suaranya keras banget sampai orang di dalam kamar ikut diam semua, Senpai. Memangnya salahnya sampai fatal banget?"
        miyuki "Nggak fatal sampai salah obat kok, aku cuma kelewat mencatat jam observasi kedua lima menit karena tadi pasien anak di ranjang dekat jendela sempat menangis takut diperiksa, jadi aku menenangkannya dulu sebelum nulis. Harusnya memang kutulis dulu jamnya baru bicara."
        nar "Ia menjabarkan kesalahan teknisnya dengan sangat jernih dan tertib. Akan tetapi, belum selesai kamu menarik napas, Miyuki langsung menyambung dengan nada datar yang membuat tengkukmu mendadak dingin."
        miyuki "Lagian wajar juga sih beliau menegur sekeras itu di depan orang tua pasien tadi supaya aku langsung kapok dan ingat terus. Setidaknya beliau masih mau repot-repot memperhatikan pekerjaanku di bangsal. Lebih buruk dan lebih menakutkan kan kalau aku sudah dianggap nggak layak ditegur sama sekali, Chiasa-chan?"
        chiasa "{i}Tunggu dulu... nada suaranya tadi kedengaran kayak dia beneran lega habis dimarahi di depan umum. Dia mulai menyamakan dimarahi keras sama diperhatikan...{/i}"
        nar "Di koridor rumah sakit yang dingin oleh deru hujan, cara Miyuki tersenyum sambil membenarkan perlakuan kasar itu terasa begitu menyayat hati."
        nar "Tekanan bertahun-tahun untuk selalu menjadi sempurna telah mengaburkan batas di dalam dirinya antara bimbingan yang sehat dan kemarahan yang merendahkan."
        nar "Tatapan mata Miyuki yang lembut menatapmu sambil masih memegang papan catatannya erat-erat di depan dada, menunggu apakah kamu akan membenarkan kalimatnya."
    else:
        if kk_slot >= 3:
            nar "Hujan deras bulan Juni memukul keras kaca jendela tinggi koridor lantai tiga Rumah Sakit Tachibana yang diterangi pendar lampu putih dingin."
        else:
            nar "Langit musim hujan bulan Juni tampak kelabu gelap di balik kaca tinggi koridor lantai tiga Rumah Sakit Tachibana. Bunyi hujan menghantam kaca beradu dengan langkah sunyi sepatu di atas lantai linoleum yang bersih."
        nar "Kamu duduk di bangku tunggu sudut dekat meja perawat sambil memegangi kantong roti hangat yang tadinya hendak kamu titipkan untuk jeda jaga Tachibana Miyuki."
        nar "Tepat saat kamu hendak berdiri mengecek jam pergantian jaga, pintu geser salah satu kamar bangsal anak terbuka setengah dan suara tajam seorang dokter paruh baya langsung memotong kesunyian lorong."
        "Dokter Pembimbing" "Tachibana, ini lembar catatan grafik pasien yang resmi! Jangan disamakan dengan buku catatan kuliah biasa! Bagaimana bisa kamu melompati kolom waktu observasi kedua, lalu masih sempat-sempatnya tersenyum mengajak bicara ibu pasien padahal tabelmu sendiri belum rapi?!"
        nar "Bunyi ketukan jari yang keras menghantam papan jepit kertas bergema hingga keluar pintu. Di dalam kamar yang terbuka separuh itu, suara obrolan keluarga pasien langsung terhenti kaku. Dua perawat di dekat konter sempat melirik sebentar sebelum segera menunduk kembali."
        "Dokter Pembimbing" "Jangan membawa kebiasaan santai mahasiswa ke bangsal saya. Periksa ulang semuanya dan serahkan lagi sebelum pergantian jaga!"
        nar "Dokter pembimbing berjas panjang itu melangkah keluar dengan wajah dingin, berjalan cepat melewati bangku tunggumu menuju ujung koridor tanpa menoleh sedikit pun."
        nar "Dua detik kemudian, Tachibana Miyuki melangkah keluar dari kamar bangsal sambil menutup pintu gesernya sangat pelan. Wajahnya tampak pucat di bawah rambut hitam panjang lurus yang terurai rapi, jemarinya mencengkeram papan jepit catatan hingga buku-buku jarinya memutih."
        yutaka "Tachibana-senpai? Senpai nggak apa-apa?"
        nar "Kamu langsung berdiri menghampiri dan menahan langkahnya dengan nada tenang. Miyuki mengerjap cepat mendengar suaramu, lalu refleks menarik sudut bibirnya membentuk senyum tipis yang tampak rapuh."
        miyuki "Eh, Yutaka-kun? Aduh, maaf banget kamu jadi kebetulan melihat kejadian barusan... aku nggak apa-apa kok, sungguh. Memang ada bagian yang harus kubetulkan di lembar grafik ini. Sensei benar soal kolom waktunya."
        yutaka "Tapi suaranya tadi sampai bikin satu kamar diam semua, Senpai. Memangnya kesalahannya sampai fatal banget?"
        miyuki "Nggak fatal sampai salah dosis kok, aku cuma kelewat mencatat jam observasi kedua lima menit karena tadi pasien anak di ranjang dekat jendela sempat menangis takut diperiksa, jadi aku menenangkannya dulu sebelum menulis. Harusnya memang kutulis dulu jamnya baru bicara."
        nar "Ia menjabarkan kesalahan teknisnya dengan sangat jernih dan tertib. Akan tetapi, belum selesai kamu menarik napas, Miyuki langsung menyambung dengan nada datar yang membuat tengkukmu mendadak terasa dingin."
        miyuki "Lagian wajar juga sih beliau menegur sekeras itu di depan orang tua pasien supaya aku langsung ingat terus. Setidaknya beliau masih mau repot-repot memperhatikan pekerjaanku di bangsal. Lebih buruk dan lebih menakutkan kan kalau aku sudah dianggap nggak layak ditegur sama sekali, Yutaka-kun?"
        yutaka "{i}Tunggu dulu... nada suaranya tadi kedengaran kayak dia beneran lega habis dipermalukan di depan umum. Dia mulai menyamakan dimarahi keras sama diperhatikan...{/i}"
        nar "Di tengah lorong bangsal yang sepi, kepasrahan Miyuki yang justru mensyukuri kemarahan kasar itu memperlihatkan luka batin yang jauh lebih dalam."
        nar "Ketakutannya akan diabaikan telah membuatnya rela menerima perlakuan buruk apa pun selama ia masih merasa dibutuhkan."
        nar "Sorot mata Miyuki yang teduh menatapmu sambil masih memegang papan catatannya erat-erat di depan dada, menunggu apakah kamu akan mengiyakan kalimatnya."
    call kk_family_menu("Mi14", ["\"Kesalahan catatan memang perlu diperbaiki, tapi Senpai tetap nggak pantas dipermalukan begitu.\"", "Hampiri dokter pembimbing di koridor dan sampaikan keberatanmu langsung.", "\"Harusnya Senpai memang lebih teliti dari awal biar nggak sampai ditegur sekeras itu.\""])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu menarik tangan Miyuki pelan menuju bangku tunggu dekat jendela hujan dan mengajaknya duduk dulu sebelum ia terburu-buru kembali bekerja. Kamu menatapnya lurus dengan suara tenang yang tegas."
            chiasa "Tachibana-senpai, tolong dengar aku sebentar ya. Soal kolom jam observasi yang terlewat, iya, itu memang hal yang perlu diperbaiki supaya catatan medisnya lengkap. Tapi cara dokter pembimbing tadi memarahi dan menepuk papan catatan Senpai keras-keras di depan pasien dan keluarganya itu tetap salah."
            nar "Miyuki mengerjap pelan, pandangannya turun menatap lembar kertas di atas pangkuannya seolah baru pertama kali mendengar bahwa kedua hal itu bisa dipisahkan."
            miyuki "Tapi kan... aku yang duluan bikin salah, Chiasa-chan. Kalau aku nggak lupa mengisi kolom jamnya, beliau nggak bakal sampai marah di depan pasien."
            chiasa "Kalau pembimbing mau mengoreksi kesalahan mahasiswa, dia bisa panggil Senpai keluar pintu dulu baru menegur dengan tegas. Mempermalukan orang di depan pasien itu cuma bikin Senpai tertekan dan bikin keluarga pasien ikut cemas, nggak ada hubungannya sama peduli."
            nar "Keheningan pendek turun di antara suara deras hujan yang menghantam kaca jendela. Jari-jari Miyuki yang sejak tadi mencengkeram pinggiran papan jepit akhirnya mengendur sedikit."
            miyuki "...Jadi aku bisa benar-benar membuat kesalahan dalam pekerjaan, dan di saat yang sama tetap nggak pantas dipermalukan di depan orang lain ya?"
            chiasa "Iya, Senpai. Dua hal itu beda. Bikin salah bukan berarti Senpai jadi pantas dibentak begitu atau harus berterima kasih habis diperlakukan kasar."
            nar "Kamu mengangguk mantap dan menyodorkan sebotol air mineral dari tasmu ke tangannya. Miyuki menerimanya dengan kedua tangan, lalu menyandarkan punggungnya ke dinding koridor sambil mengembuskan napas pelan."
            miyuki "Aneh banget rasanya dengar kalimat itu... biasanya kalau di rumah atau di kampus ada yang menegurku keras, kepalaku langsung otomatis mencari alasan kenapa aku memang layak dimarahi."
            chiasa "Sekarang nggak usah buru-buru membela orang yang barusan bikin tangan Senpai gemetar. Istirahat dulu tiga menit, minum dulu, baru habis itu kita rapikan catatan jamnya ya."
            miyuki "...Iya. Terima kasih banyak sudah bilang itu langsung ke aku, Chiasa-chan."
            nar "Untuk pertama kalinya sejak keluar dari pintu bangsal, Miyuki tidak terburu-buru mencari alasan untuk menyalahkan dirinya sendiri. Ia duduk tenang di bangku koridor bersama bunyi hujan, membiarkan pertanyaan barusan tinggal lebih lama di kepalanya."
        else:
            nar "Kamu mengarahkan bahu Miyuki pelan menuju bangku tunggu dekat jendela hujan dan mengajaknya duduk sebentar sebelum ia langsung memaksakan diri kembali bekerja. Kamu menatap matanya lurus dengan nada bicara yang tenang dan tegas."
            yutaka "Tachibana-senpai, coba pisahkan dua hal ini dulu ya. Soal kolom jam observasi yang terlewat, iya, itu memang harus diperbaiki supaya datanya lengkap. Tapi cara dokter pembimbing tadi membentak dan menepuk papan catatan Senpai keras-keras di depan pasien dan orang tuanya itu tetap salah."
            nar "Miyuki mengerjap pelan, pandangannya turun menatap lembar catatan di atas pangkuannya seolah baru pertama kali mendengar bahwa dua hal itu boleh berdiri secara terpisah."
            miyuki "Tapi kan... aku yang duluan ceroboh, Yutaka-kun. Kalau aku nggak lupa mengisi kolom jamnya, beliau nggak bakal sampai menegur keras di depan pasien."
            yutaka "Kalau pembimbing mau mengoreksi kesalahan praktik, dia bisa memanggil Senpai keluar pintu dulu baru bicara tegas. Mempermalukan orang di depan keluarga pasien cuma bikin Senpai tertekan dan bikin orang tua pasien ikut cemas, sama sekali nggak ada hubungannya sama rasa peduli."
            nar "Keheningan pendek turun di antara deru hujan yang memukul kaca koridor. Cengkeraman jari-jari Miyuki di tepi papan jepit akhirnya mengendur."
            miyuki "...Jadi aku bisa sungguh-sungguh bikin salah dalam pekerjaan, dan di saat yang sama tetap nggak pantas dipermalukan di depan orang lain ya?"
            yutaka "Betul, Senpai. Dua hal itu terpisah. Melakukan satu kesalahan teknis nggak otomatis bikin Senpai pantas dibentak begitu atau harus merasa bersyukur habis diperlakukan kasar."
            nar "Kamu mengangguk mantap dan menyodorkan sebotol air mineral dari tasmu ke tangannya. Miyuki menerimanya dengan kedua tangan, lalu menyandarkan punggungnya ke dinding koridor sambil mengembuskan napas panjang."
            miyuki "Rasanya asing banget dengar kalimat itu... biasanya kalau di rumah atau di bangsal ada yang menegurku keras, kepalaku langsung otomatis sibuk menyusun alasan kenapa aku memang pantas dimarahi."
            yutaka "Sekarang berhenti dulu membela orang yang barusan bikin tangan Senpai gemetar. Duduk tiga menit, minum dulu, baru habis itu rapikan kolom waktunya dengan kepala dingin."
            miyuki "...Iya. Terima kasih banyak sudah meluruskan itu buatku, Yutaka-kun."
            nar "Untuk pertama kalinya sejak melangkah keluar dari pintu bangsal, Miyuki tidak terburu-buru mencari pembelaan bagi perlakuan yang melukainya. Ia duduk diam di bangku koridor ditemani bunyi hujan, membiarkan pertanyaan barusan mengendap lebih lama di kepalanya."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Melihat tangan Miyuki masih gemetar memegangi papan catatan sementara punggung dokter pembimbing tadi belum menghilang di tikungan meja perawat, rasa geram membuatmu langsung melangkah cepat menyusulnya."
            miyuki "Eh, Chiasa-chan! Tunggu, jangan ke sana!"
            chiasa "Sebentar aja, Senpai, aku cuma mau bicara sopan kok."
            nar "Kamu berhenti dua langkah di depan sang dokter pembimbing dekat tikungan lorong dan membungkuk singkat agar sikapmu tetap terjaga."
            chiasa "Permisi, Sensei. Maaf sekali mengganggu waktu Anda sebentar. Saya kebetulan duduk menunggu di koridor tadi saat Anda menegur Tachibana-senpai."
            nar "Dokter paruh baya itu berhenti melangkah dan menoleh ke arahmu dengan kening berkerut tajam di balik kacamatanya."
            "Dokter Pembimbing" "Kamu mahasiswa dari luar bagian medis, ya? Ada urusan apa sampai menghentikan saya di lorong bangsal?"
            chiasa "Saya tahu ketelitian catatan pasien itu sangat penting, Sensei. Tapi menegur mahasiswa praktik sekeras itu sambil menepuk papan catatan di depan pasien anak dan orang tuanya, bukannya justru membuat pasien ikut takut dan mempermalukan Tachibana-senpai secara tidak perlu?"
            nar "Hening dingin langsung jatuh di sudut lorong. Tatapan dokter itu menyipit kaku dan suaranya turun menjadi sangat singkat serta tak terbantahkan."
            "Dokter Pembimbing" "Ini rumah sakit pendidikan yang punya aturan sendiri. Cara saya membimbing calon dokter di bangsal ini adalah urusan internal medis, tidak seharusnya dibahas oleh tamu di tengah koridor. Tolong jangan menghalangi jalan saya."
            nar "Ia segera memutar badan dan melangkah pergi melewati pintu ruang dokter tanpa memberi ruang tanggapan lagi. Kamu menarik napas panjang lalu berjalan kembali ke tempat Miyuki berdiri menunggumu dengan raut cemas."
            chiasa "Maaf ya, Senpai, aku jadi terbawa emosi dan langsung nyamperin beliau tadi... kayaknya beliau malah makin kesal."
            nar "Miyuki menatapmu dengan sorot mata yang berkaca-kaca tipis. Untuk sesaat ia tampak sangat tegang, lalu sudut bibirnya terangkat lembut."
            miyuki "Jujur aja... aku agak takut besok suasana di bangsal jadi jauh lebih kaku dan sulit gara-gara tadi, Chiasa-chan."
            chiasa "Aduh, maaf banget, Senpai..."
            miyuki "Tapi jangan cuma dengar bagian takutnya aja. Di sisi lain... aku juga lega dan senang banget tahu ada satu orang di sini yang langsung merasa perlakuan tadi memang nggak semestinya."
            nar "Miyuki menarik napas dalam dan menegakkan bahunya perlahan, kali ini dengan sorot mata yang lebih mantap."
            miyuki "Boleh aku minta tolong satu hal, Chiasa-chan? Untuk koreksi catatan grafik ini dan menghadapi Sensei nanti, biarkan aku sendiri yang menyelesaikannya dulu ya. Kamu tunggu di lobi bawah atau pulang duluan aja nggak apa-apa, nanti sepulang jaga aku langsung kabari kamu."
            chiasa "Iya, Senpai. Aku nggak bakal ikut campur lagi ke ruang bangsal. Semangat beresin catatannya ya."
            nar "Kamu menyerahkan kantong roti hangat yang sejak tadi kamu bawa agar ia bisa memakannya begitu jadwal jaganya selesai."
            nar "Miyuki menerima bungkusan itu dengan senyum tulus sambil merapikan kembali lembaran grafik pasien di atas papan jepitnya."
            nar "Kali ini kamu sungguh-sungguh mendengarkan permintaannya sendiri dan memberinya ruang untuk membereskan pekerjaannya. Miyuki mengangguk berterima kasih dengan raut yang sedikit lebih kuat sebelum melangkah kembali menuju meja perawat."
        else:
            nar "Melihat jemari Miyuki masih sedikit gemetar memegangi papan catatan sementara punggung sang dokter pembimbing belum menghilang di tikungan meja perawat, kamu langsung melangkah mantap menyusulnya."
            miyuki "Eh, Yutaka-kun! Tunggu, jangan ke sana!"
            yutaka "Sebentar aja, Senpai, aku cuma mau bicara baik-baik kok."
            nar "Kamu berhenti dua langkah di hadapan sang dokter pembimbing dekat tikungan lorong dengan postur tegak, lalu menunduk sopan sekali agar sikapmu tetap terkendali."
            yutaka "Permisi, Sensei. Maaf mengganggu waktu Anda sebentar. Saya kebetulan duduk menunggu di koridor tadi saat Anda menegur Tachibana-senpai."
            nar "Dokter paruh baya itu berhenti berjalan dan mengangkat wajah menatapmu dari balik kacamatanya dengan alis menukik tajam."
            "Dokter Pembimbing" "Kamu tamu dari luar bagian medis, ya? Ada urusan apa sampai menghentikan saya di lorong bangsal?"
            yutaka "Saya paham ketelitian catatan pasien itu mutlak, Sensei. Tapi menegur mahasiswa praktik dengan suara keras sambil menepuk papan catatan di depan pasien anak dan ibunya, bukannya justru membuat keluarga pasien ikut panik dan mempermalukan Tachibana-senpai tanpa alasan yang perlu?"
            nar "Keheningan dingin segera turun di sudut lorong. Tatapan dokter itu menyipit kaku dan jawabannya keluar singkat, dingin, serta tertutup."
            "Dokter Pembimbing" "Ini rumah sakit pendidikan yang punya aturan sendiri. Cara saya membimbing calon dokter di bangsal ini adalah urusan internal medis, tidak seharusnya dibahas oleh tamu di tengah koridor. Tolong jangan menghalangi jalan saya."
            nar "Ia segera memutar badan dan melangkah masuk melewati pintu ruang dokter tanpa memberi kesempatan bicara lagi. Kamu mengembuskan napas pendek lalu berbalik menghampiri Miyuki yang menunggumu dengan wajah cemas."
            yutaka "Maaf ya, Senpai, aku langsung maju nyamperin beliau tadi... kayaknya beliau malah makin kaku."
            nar "Miyuki menatapmu dengan tatapan mata yang berkaca-kaca tipis. Untuk sesaat ia tampak sangat tegang, sebelum sudut bibirnya perlahan melengkung hangat."
            miyuki "Terus terang... aku agak takut besok suasana bangsal bakal jadi jauh lebih sulit gara-gara tadi, Yutaka-kun."
            yutaka "Salahku juga sih langsung motong beliau di koridor."
            miyuki "Jangan cuma dengar bagian takutnya aja dong. Di sisi lain... aku juga senang dan lega banget tahu ada satu orang di sini yang langsung merasa perlakuan barusan memang nggak semestinya."
            nar "Miyuki menarik napas pelan dan menegakkan bahunya, kali ini dengan sorot mata yang lebih tenang."
            miyuki "Tapi boleh aku minta tolong satu hal, Yutaka-kun? Untuk koreksi grafik ini dan menghadapi Sensei nanti, biarkan aku sendiri yang menanganinya dulu ya. Kamu tunggu di lobi bawah atau pulang duluan aja nggak apa-apa, nanti sepulang jaga aku langsung kirim kabar ke kamu."
            yutaka "Paham, Senpai. Aku nggak bakal ikut campur ke urusan bangsal lagi. Semangat beresin catatannya ya."
            nar "Kamu menyerahkan kantong roti hangat yang tadi kamu siapkan untuknya agar ia tetap punya bekal makan saat gilirannya berakhir."
            nar "Miyuki menyimpan kantong roti itu di saku jasnya sambil memeriksa kembali pena di tangannya dengan ketenangan yang mulai pulih."
            nar "Kali ini kamu benar-benar mendengarkan permintaannya sendiri dan memberinya ruang penuh untuk menyelesaikan pekerjaannya. Miyuki mengangguk berterima kasih dengan raut lebih mantap sebelum melangkah kembali ke arah konter perawat."
    else:
        if kk_host == "chiasa":
            nar "Sebelum Miyuki sempat duduk ataupun menenangkan napasnya, kamu justru ikut mengerutkan kening menatap papan catatan di tangannya dan melontarkan teguran tajam."
            chiasa "Kalau memang kolom jam observasi pasien yang terlewat, ya harusnya Tachibana-senpai lebih teliti lagi dari awal dong. Di rumah sakit kayak gini, lupa mencatat lima menit aja bisa bikin dokter lain salah baca kondisi pasien. Jangan gampang buyar fokusnya cuma gara-gara suasana kamar ramai."
            nar "Kamu bahkan menyambung dengan mengomentari cara Miyuki membagi waktu istirahat serta jadwal belajarnya minggu ini, termasuk bagian-bagian tugas bangsal yang sebenarnya sama sekali tidak kamu saksikan sendiri."
            nar "Alih-alih mundur tersinggung ataupun membela diri, reaksi Miyuki justru membuat suasana koridor terasa janggal. Ia langsung menegakkan punggungnya, lalu mengangguk patuh pada setiap kalimat kritikmu dengan mata terbuka lebar."
            miyuki "Iya... benar banget kata Chiasa-chan. Aku memang ceroboh banget hari ini. Harusnya tadi aku nggak ikut panik pas pasien anaknya nangis dan langsung merapikan tabel dulu sesuai urutan."
            chiasa "Nah, lain kali jangan sampai keulang lagi, Senpai. Nanti Senpai sendiri yang terus-terusan kena tegur."
            miyuki "Iya, aku janji bakal periksa dua kali lipat lebih teliti mulai hari ini. Aku bakal kerjakan ulang laporannya sampai nggak ada satu garis pun yang meleset... jadi tolong jangan kecewa sama aku dulu ya, Chiasa-chan."
            nar "Suara Miyuki terdengar jauh lebih tenang daripada satu menit lalu, bahkan ada seberkas kelegaan aneh yang menyelinap di balik sorot matanya. Ia tampak lega karena kini tahu persis kesalahan apa yang harus ia tebus agar perhatianmu tidak berpaling darinya."
            miyuki "Terima kasih sudah mau menegurku juga, Chiasa-chan. Kalau nggak diingatkan keras begini, aku takut nanti aku jadi terlalu memanjakan diri sendiri. Aku langsung ke meja perawat dulu ya untuk membetulkannya sekarang."
            nar "Miyuki membungkuk singkat lalu berjalan cepat ke arah konter perawat sambil memeluk papan catatannya erat-erat. Di tengah deru hujan yang memukul kaca koridor, kamu baru menyadari bahwa luka yang baru saja ia terima di dalam bangsal kini mendapatkan suara kedua yang akan ikut ia bawa pulang."
        else:
            nar "Sebelum Miyuki sempat duduk ataupun menenangkan napasnya, kamu justru ikut mengerutkan kening menatap papan catatan di tangannya dan melontarkan teguran dingin."
            yutaka "Kalau memang kolom jam observasi pasien yang sampai terlewat, harusnya Tachibana-senpai jauh lebih teliti lagi dari awal dong. Di bangsal rumah sakit, lupa mencatat lima menit aja bisa bikin dokter lain salah baca kondisi pasien. Jangan gampang buyar fokus cuma gara-gara suasana kamar agak ribut."
            nar "Kamu bahkan meneruskan dengan mengomentari cara Miyuki mengatur jam tidur serta disiplin catatannya minggu ini, termasuk rincian tugas bangsal yang sebenarnya sama sekali tidak kamu lihat langsung."
            nar "Alih-alih tersinggung ataupun membela diri, reaksi Miyuki justru membuat udara koridor terasa ganjil. Ia langsung menegakkan punggungnya kaku, lalu mengangguk patuh pada setiap kritikmu dengan mata terbuka lebar."
            miyuki "Iya... benar banget kata Yutaka-kun. Aku memang ceroboh banget hari ini. Harusnya tadi aku nggak ikut panik pas pasien anaknya menangis dan langsung merapikan tabel dulu sesuai urutan."
            yutaka "Nah, lain kali jangan sampai terulang lagi, Senpai. Nanti Senpai sendiri yang bakal terus-terusan kena tegur pembimbing."
            miyuki "Iya, aku janji bakal periksa dua kali lipat lebih teliti mulai hari ini. Aku kerjakan ulang laporannya sampai nggak ada satu garis pun yang meleset... jadi tolong jangan kecewa sama aku dulu ya, Yutaka-kun."
            nar "Suara Miyuki terdengar jauh lebih tenang dibandingkan satu menit lalu, bahkan terselip seberkas kelegaan aneh di balik sorot matanya. Ia tampak lega karena kini tahu persis kesalahan apa yang harus ia tebus supaya perhatianmu tetap tertuju kepadanya."
            miyuki "Terima kasih sudah mau menegurku langsung juga, Yutaka-kun. Kalau nggak diingatkan tegas begini, aku takut nanti aku malah memanjakan diri sendiri. Aku ke meja perawat sekarang ya untuk langsung membetulkannya."
            nar "Ia segera duduk di kursi ujung konter perawat dan mulai menulis ulang kolom waktu observasi dengan punggung yang tampak terlalu tegang."
            nar "Sikapmu yang ikut memarahinya tadi justru memperkuat keyakinan kelirunya bahwa ia hanya dicintai ketika sedang menebus kesalahan."
            nar "Miyuki membungkuk singkat lalu melangkah cepat ke arah konter perawat sambil memeluk papan catatannya erat-erat. Di tengah deru hujan yang memukul kaca koridor, kamu baru menyadari bahwa luka yang baru saja ia terima di dalam bangsal kini mendapatkan suara kedua yang akan terus ia bawa pulang."
    return

# ┌─ PANDUAN CERITA · Mi15 · Minta Maaf Berlebihan
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : ia meminta maaf untuk hal sepele.
# │ INTI    : A tegur halus / B biarkan / C manfaatkan.
# │ AKHIRAN : stage 3 (normalisasi).
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi15:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana · Permintaan maaf")
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Lampu neon putih menyinari sayap lobi Rumah Sakit Tachibana yang sudah lebih lengang. Kaca jendela besar memantulkan deretan mesin penjual minuman otomatis yang berdengung pelan di sudut ruang tunggu."
        else:
            nar "Hawa sejuk pendingin ruangan mengisi sayap lobi Rumah Sakit Tachibana sementara sinar bulan Agustus jatuh miring di lantai keramik dekat deretan mesin penjual minuman otomatis dan bangku tunggu."
        nar "Di sampingmu, Miyuki berdiri dengan rambut hitam panjang lurus terurai di atas jas dokter putihnya dan stetoskop terselip di saku. Seorang perawat yang baru melintas dari arah lift sempat mengangguk ramah kepadanya."
        "Perawat" "Tachibana-san, jeda istirahat sebentar ya? Jangan lupa minum air yang cukup, di bangsal tadi sibuk sekali."
        miyuki "Iya, terima kasih banyak. Aku ambil minum sebentar lalu kembali naik."
        nar "Senyum seniornya tetap terjaga rapi sampai perawat itu menghilang di tikungan koridor. Begitu hanya tersisa kalian berdua, Miyuki langsung melirik pipimu yang masih terasa hangat setelah berjalan dari luar."
        miyuki "Ara, Chiasa-chan repot-repot mampir cuma buat mengembalikan daftar buku rujukan kemarin? Padahal bisa dikirim lewat pesan saja, udara di luar gerah banget kan?"
        chiasa "Sekalian lewat arah stasiun habis beli kertas sketsa, Tachibana-senpai. Lagipula aku sekalian mau ketemu sebentar kalau Senpai lagi sempat."
        miyuki "Syukurlah kebetulan aku baru selesai keliling bangsal. Sini, mesin di sudut lorong ini biasanya teh jelainya paling dingin. Kamu sudah minum air yang cukup hari ini?"
        chiasa "Baru mau beli sekarang, Tachibana-senpai. Makasih sudah menyempatkan turun di sela jeda bangsal."
        miyuki "Nggak apa-apa kok, sepuluh menit lumayan buat meluruskan kaki. Pilih dulu yang kamu mau."
        nar "Kamu memasukkan dua koin seratus yen ke lubang logam dan menekan tombol teh jelai dingin. Koin berdenting pelan di dalam mesin, lampu angka berkedip padam sesaat, lalu tidak ada satu botol pun yang jatuh ke baki bawah."
        nar "Kamu memutar tuas pengembalian uang dua kali. Tetap tidak terdengar apa pun dari dalam."
        chiasa "Yah, koinnya ketelan. Tuas kembaliannya juga nggak bunyi sama sekali."
        nar "Sebelum kamu selesai menarik tangan dari mesin, senyum di wajah Miyuki langsung menegang. Tangannya segera menyelam ke saku jas dokter putih dan menarik dompet kulit kremnya terlalu cepat hingga pengaitnya nyaris terlepas."
        miyuki "Maaf banget, Chiasa-chan! Harusnya tadi aku langsung ajak kamu ke mesin dekat lobi barat saja. Aku nggak tahu mesin di sudut ini lagi rusak. Maaf, ya."
        nar "Ia mulai merinci tiga hal beruntun yang menurutnya seharusnya ia lakukan lebih dulu. Ia menyalahkan dirinya karena tidak memeriksa stiker perawatan mesin, lupa mengambilkan teh dingin dari ruang staf, dan tidak melihat lampu slot koin yang redup sebelum kamu memasukkan uang."
        nar "Tak satu pun dari tiga hal itu masuk akal untuk menjadi tanggung jawabnya. Ketika kamu menunduk melihat tangannya, jari-jarinya yang panjang ternyata gemetar halus saat mengorek kantong koin di dompetnya, sementara matanya yang cokelat kemerahan melirik wajahmu cemas seolah menunggu teguran."
        chiasa "{i}Itu jauh lewat dari sekadar sopan santun. Ia panik begitu cepat hanya karena takut aku kecewa gara-gara mesin rusak.{/i}"
        call kk_family_menu("Mi15", ["\"Tachibana-senpai, simpan dompetnya. Mesin rusak itu bukan salahmu.\"", "Biarkan saja ia membayar minuman penggantinya.", "Manfaatkan rasa bersalahnya untuk menitipkan urusan pribadimu."])
        if _return == "A":
            nar "Kamu mengulurkan tangan dan menahan pinggiran dompetnya dengan lembut sebelum ia sempat mengeluarkan koin."
            chiasa "Tachibana-senpai, simpan dompetnya. Mesin yang rusak itu bukan salahmu, dan kamu juga bukan teknisi mesin minuman rumah sakit."
            nar "Miyuki membeku di tengah gerakannya. Bibirnya sudah sempat terbuka untuk menyusun permintaan maaf berikutnya."
            miyuki "Tapi kan tadi aku yang nunjukin mesin di lorong ini, jadi kalau Chiasa-chan rugi dua ratus yen..."
            chiasa "Berhenti dulu. Jangan tambah satu kata maaf lagi. Kamu sama sekali nggak berbuat salah di sini."
            nar "Hening pendek menggantung di samping suara dengung mesin pendingin. Miyuki menunduk memandangi dua koin seratus yen yang masih terjepit di ujung jarinya yang gemetar, lalu berkedip pelan."
            miyuki "...Aku bahkan belum sempat mikir, Chiasa-chan. Kata maafnya langsung keluar sendiri sebelum aku sadar."
            nar "Ia memasukkan dompetnya perlahan kembali ke saku jas putih, lalu menatap kotak logam di depannya dengan raut agak bingung."
            chiasa "Kalau kesal sama mesinnya, bilang saja mesinnya menyebalkan. Coba sekali, Senpai."
            nar "Miyuki ragu sejenak dan melirik lorong yang sepi, lalu mengembuskan napas pendek ke arah mesin minuman itu."
            miyuki "...Mesin ini beneran menyebalkan. Uangnya sudah masuk, tapi minumannya nggak mau keluar."
            nar "Tawa canggung yang tipis segera keluar darinya begitu kalimat itu selesai, melonggarkan ketegangan di sudut matanya yang cokelat kemerahan."
            miyuki "Aneh banget rasanya ngomong begitu keras-keras. Ternyata aku boleh ikut kesal duluan tanpa harus membereskan perasaan semua orang, ya?"
            chiasa "Boleh banget. Ayo lapor ke meja resepsionis sebentar biar uangnya balik, lalu kita pindah ke mesin sebelah."
            nar "Di meja resepsionis yang tenang, kamu menyebutkan nomor mesin di sudut lorong. Petugas segera mencatatnya di buku laporan pemeliharaan dan mengeluarkan dua koin seratus yen dari kotak kas kecil."
            "Resepsionis" "Maaf sekali atas ketidaknyamanannya. Ini pengembalian dua ratus yennya, nanti teknisi segera kami panggil untuk mengecek mesin sudut."
            chiasa "Terima kasih banyak."
            nar "Kalian berjalan berdampingan menuju mesin di sebelah ruang tunggu utama. Di depan deretan tombol minuman, Miyuki sempat berhenti sejenak dan melirikmu dengan senyum kikuk."
            miyuki "Kalau begitu... aku beli teh susu hangat boleh kan, meskipun di luar lagi musim panas? Ruang bangsal berpendingin banget."
            chiasa "Kenapa mesti minta izin? Beli saja yang Senpai suka."
            nar "Miyuki berkedip sekali, menyadari ia baru saja menyampaikan keinginannya sendiri tanpa menyelipkan kata maaf di ujung kalimat. Ia menekan tombolnya dengan jemari yang sudah tenang."
        elif _return == "B":
            nar "Kamu mundur setengah langkah dan membiarkan tanganmu turun di sisi badan, tidak menghentikan gerakannya mencari koin di dalam dompet."
            nar "Begitu ujung jarinya menemukan dua koin seratus yen, getaran kecil di tangannya sedikit mereda. Miyuki segera bergeser ke mesin minuman di sebelahnya, memasukkan uang dengan cepat, lalu menekan tombol teh jelai dingin sampai botol plastik itu jatuh ke baki bawah."
            nar "Ia membungkuk mengambil botol itu, menyeka embun dingin di tutupnya dengan ujung lengan jas, lalu menyodorkannya kepadamu dengan dua tangan."
            miyuki "Ini, Chiasa-chan. Teh jelai yang sama seperti pilihanmu tadi. Maaf jadi bikin kamu menunggu lebih lama."
            chiasa "Oh... makasih, Tachibana-senpai."
            nar "Tepat ketika jarimu menutup di sekitar botol dingin itu, bahu Miyuki turun sedikit. Senyum lega yang rapi baru muncul kembali di wajahnya setelah melihatmu menerimanya."
            miyuki "Nah. Sekarang sudah beres. Syukurlah kamu nggak jadi kehausan."
            nar "Kalian duduk sebentar di bangku tunggu lobi. Kamu membuka tutup botol dan meneguk sedikit teh dingin, sementara Miyuki memperhatikannya dengan tenang."
            miyuki "Dinginnya pas, kan? Nggak terlalu hambar?"
            chiasa "Pas kok. Tachibana-senpai sendiri nggak beli minum?"
            miyuki "Nanti saja di ruang jaga. Yang penting minumanmu sudah ada dulu."
            nar "Saat seorang pengunjung rumah sakit berjalan tergesa dan tanpa sengaja menyenggol ujung lengan jas Miyuki, Miyuki langsung berdiri sedikit dan membungkuk duluan sebelum orang itu sempat berkata apa-apa."
            miyuki "Ah, maaf sekali, aku agak menghalangi jalan."
            "Pengunjung" "Eh, nggak apa-apa, saya yang kurang hati-hati."
            chiasa "Tachibana-senpai, tadi kan bukan kamu yang menabrak. Kamu bahkan duduk di pinggir bangku."
            miyuki "Nggak apa-apa, Chiasa-chan. Lebih cepat minta maaf duluan daripada bikin suasana koridor rumah sakit jadi canggung."
            nar "Miyuki duduk kembali dan merapikan saku jasnya dengan wajah tenang. Di matanya, persoalan selesai tuntas setiap kali orang di depannya tidak lagi tampak kecewa. Kebiasaan yang baru saja mendapat pembenaran halus itu akan keluar jauh lebih cepat pada kesempatan berikutnya."
        else:
            nar "Kamu membiarkan tangannya tetap memegang dompet kulit krem itu. Kamu melirik mesin yang macet, lalu menatap balik matanya yang cokelat kemerahan dengan jeda yang disengaja."
            chiasa "Ya sudah, kalau Tachibana-senpai memang merasa nggak enak, nggak perlu ganti dua ratus yen di sini. Kebetulan ada satu urusan yang bikin aku repot minggu ini."
            nar "Punggung Miyuki langsung menegak. Raut gelisahnya sedikit mengendur, seolah ia justru lega diberi cara konkret untuk menebus kesalahan yang sebenarnya tidak ada."
            miyuki "Apa pun itu, bilang saja, Chiasa-chan. Kalau aku bisa bantu, pasti kubantu."
            chiasa "Aku perlu ringkasan referensi buku anatomi dasar buat sketsa figur di kelas seni. Istilah medis di perpustakaan Kedokteran bikin aku bingung. Senpai bisa pilihkan lalu tuliskan poin pentingnya sebelum lusa?"
            nar "Kamu tahu betul jadwal rotasi klinik tahun keempat dan belajar ujiannya sudah menyita jam tidurnya, dan permintaan itu sama sekali jauh dari urusan mesin minuman. Miyuki sempat terdiam setengah detik menimbang hari, lalu buru-buru mengangguk."
            miyuki "Lusa pagi, ya... besok aku ada jaga bangsal sampai cukup larut, tapi selesai itu masih bisa kubuka bukunya di apartemen. Nanti aku rangkumkan bagian struktur bahu sama lengan sekalian."
            nar "Kamu tidak menarik permintaanmu kembali ataupun menyuruhnya beristirahat saja. Kamu justru tersenyum hangat seolah mengandalkannya sepenuhnya."
            chiasa "Makasih banyak, Tachibana-senpai. Aku memang paling percaya sama kerapian catatan Senpai."
            nar "Kalimat itu langsung menghapus sisa keraguannya. Ia mengeluarkan buku saku kecil dari balik jas putihnya dan membuka halaman yang sudah sesak oleh jadwal jaga bangsal, catatan kasus pasien, dan blok belajar malam."
            nar "Ia menambahkan satu baris baru bertuliskan ringkasan anatomi untukmu di pinggiran sempit halaman itu tanpa mencoret satu pun jadwal lamanya."
            miyuki "Bisa. Nanti aku atur semuanya, jangan khawatir. Kalau ada bagian khusus yang ingin kamu fokuskan, kirim pesan saja kapan pun, ya."
            miyuki "Terima kasih sudah percaya sama aku, Chiasa-chan. Aku janji kali ini nggak bikin kamu kecewa."
            nar "Ponsel di saku jasnya bergetar singkat menandakan waktu jeda bangsal hampir selesai. Miyuki berdiri sambil merapikan kerah jas putihnya."
            miyuki "Aku naik dulu ke lantai tiga ya. Hati-hati di jalan pulang, jangan lupa minum air yang dingin."
            chiasa "Iya, semangat jaga bangsalnya, Tachibana-senpai."
            nar "Ia melangkah menuju lift dengan senyum yang terasa terlalu tenang. Urusanmu baru saja beres tanpa tenaga, sementara di saku jasnya bertambah satu alasan baru untuk takut gagal di depanmu."
    else:
        if kk_slot >= 3:
            nar "Lampu neon putih menyinari sayap lobi Rumah Sakit Tachibana yang sudah lebih lengang. Kaca jendela besar memantulkan deretan mesin penjual minuman otomatis yang berdengung pelan di sudut ruang tunggu."
        else:
            nar "Hawa sejuk pendingin ruangan mengisi sayap lobi Rumah Sakit Tachibana sementara sinar bulan Agustus jatuh miring di lantai keramik dekat deretan mesin penjual minuman otomatis dan bangku tunggu."
        nar "Di sampingmu, Miyuki berdiri dengan rambut hitam panjang lurus terurai di atas jas dokter putihnya dan stetoskop terselip di saku. Seorang perawat yang baru melintas dari arah lift sempat mengangguk ramah kepadanya."
        "Perawat" "Tachibana-san, jeda istirahat sebentar ya? Jangan lupa minum air yang cukup, di bangsal tadi sibuk sekali."
        miyuki "Iya, terima kasih banyak. Aku ambil minum sebentar lalu kembali naik."
        nar "Senyum seniornya tetap terjaga rapi sampai perawat itu menghilang di tikungan koridor. Begitu hanya tersisa kalian berdua, Miyuki melirik dahimu yang masih sedikit terasa hangat setelah berjalan dari luar."
        miyuki "Ara, Yutaka-kun repot-repot mampir cuma buat mengembalikan buku catatan yang kemarin? Padahal bisa dikirim lewat pesan saja, udara di luar gerah banget kan?"
        yutaka "Sekalian lewat arah stasiun habis dari toko buku, Tachibana-senpai. Lagipula aku sekalian mau ketemu sebentar kalau Senpai lagi sempat."
        miyuki "Syukurlah kebetulan aku baru selesai keliling bangsal. Sini, mesin di sudut lorong ini biasanya kopi hitam dinginnya masih ada. Kamu sudah minum air yang cukup hari ini?"
        yutaka "Baru mau beli sekarang, Tachibana-senpai. Makasih sudah menyempatkan turun di sela jeda bangsal."
        miyuki "Nggak apa-apa kok, sepuluh menit lumayan buat meluruskan kaki. Pilih dulu yang kamu mau."
        nar "Kamu memasukkan dua koin seratus yen ke lubang logam dan menekan tombol kopi hitam dingin. Koin berdenting pelan di dalam mesin, lampu angka berkedip padam sesaat, lalu tidak ada satu kaleng pun yang jatuh ke baki bawah."
        nar "Kamu memutar tuas pengembalian uang dua kali. Tetap tidak terdengar apa pun dari dalam."
        yutaka "Yah, koinnya ketelan. Tuas kembaliannya juga nggak bunyi sama sekali."
        nar "Sebelum kamu selesai menarik tangan dari mesin, senyum di wajah Miyuki langsung menegang. Tangannya segera menyelam ke saku jas dokter putih dan menarik dompet kulit kremnya terlalu cepat hingga pengaitnya nyaris terlepas."
        miyuki "Maaf banget, Yutaka-kun! Harusnya tadi aku langsung ajak kamu ke mesin dekat lobi barat saja. Aku nggak tahu mesin di sudut ini lagi rusak. Maaf, ya."
        nar "Ia mulai merinci tiga hal beruntun yang menurutnya seharusnya ia lakukan lebih dulu. Ia menyalahkan dirinya karena tidak memeriksa stiker perawatan mesin, lupa mengambilkan kopi dingin dari ruang staf, dan tidak melihat lampu slot koin yang redup sebelum kamu memasukkan uang."
        nar "Tak satu pun dari tiga hal itu masuk akal untuk menjadi tanggung jawabnya. Ketika kamu menunduk melihat tangannya, jari-jarinya yang panjang ternyata gemetar halus saat mengorek kantong koin di dompetnya, sementara matanya yang cokelat kemerahan mendongak cemas seolah menunggu teguran."
        yutaka "{i}Aku kenal betul reaksi tegang seperti itu dari rumah yang serba menuntut. Itu jauh lewat dari sopan santun biasa; ia panik begitu cepat hanya karena takut aku kecewa gara-gara mesin rusak.{/i}"
        call kk_family_menu("Mi15", ["\"Tachibana-senpai, simpan dompetnya. Mesin rusak itu bukan salahmu.\"", "Biarkan saja ia membayar minuman penggantinya.", "Manfaatkan rasa bersalahnya untuk menitipkan urusan pribadimu."])
        if _return == "A":
            nar "Kamu mengulurkan tangan dan menahan pinggiran dompetnya dengan lembut sebelum ia sempat mengeluarkan koin."
            yutaka "Tachibana-senpai, simpan dompetnya. Mesin yang rusak itu bukan salahmu, kecuali kamu diam-diam kerja paruh waktu jadi teknisi mesin minuman rumah sakit."
            nar "Miyuki membeku di tengah gerakannya. Bibirnya sudah sempat terbuka untuk menyusun permintaan maaf berikutnya."
            miyuki "Tapi kan tadi aku yang menyarankan mesin di lorong ini, jadi kalau Yutaka-kun rugi dua ratus yen..."
            yutaka "Berhenti dulu. Jangan tambah satu kata maaf lagi. Kamu sama sekali nggak berbuat salah di sini."
            nar "Hening pendek menggantung di samping suara dengung mesin pendingin. Miyuki menunduk memandangi dua koin seratus yen yang masih terjepit di ujung jarinya yang gemetar, lalu berkedip pelan."
            miyuki "...Aku bahkan belum sempat mikir, Yutaka-kun. Kata maafnya langsung keluar sendiri sebelum aku sadar."
            nar "Ia memasukkan dompetnya perlahan kembali ke saku jas putih, lalu menatap kotak logam di depannya dengan raut agak bingung."
            yutaka "Kalau kesal sama mesinnya, bilang saja mesinnya menyebalkan. Coba sekali, Senpai."
            nar "Miyuki ragu sejenak dan melirik lorong yang sepi, lalu mengembuskan napas pendek ke arah mesin minuman itu."
            miyuki "...Mesin ini beneran menyebalkan. Uangnya sudah masuk, tapi minumannya nggak mau keluar."
            nar "Tawa canggung yang tipis segera keluar darinya begitu kalimat itu selesai, melonggarkan ketegangan di sudut matanya yang cokelat kemerahan."
            miyuki "Aneh banget rasanya ngomong begitu keras-keras. Ternyata aku boleh ikut kesal duluan tanpa harus membereskan perasaan semua orang, ya?"
            yutaka "Boleh banget. Ayo lapor ke meja resepsionis sebentar biar uangnya balik, lalu kita pindah ke mesin sebelah."
            nar "Di meja resepsionis yang tenang, kamu menyebutkan nomor mesin di sudut lorong. Petugas segera mencatatnya di buku laporan pemeliharaan dan mengeluarkan dua koin seratus yen dari kotak kas kecil."
            "Resepsionis" "Maaf sekali atas ketidaknyamanannya. Ini pengembalian dua ratus yennya, nanti teknisi segera kami panggil untuk mengecek mesin sudut."
            yutaka "Terima kasih banyak."
            nar "Kalian berjalan berdampingan menuju mesin di sebelah ruang tunggu utama. Di depan deretan tombol minuman, Miyuki sempat berhenti sejenak dan menoleh kepadamu dengan senyum kikuk."
            miyuki "Kalau begitu... aku beli teh susu hangat boleh kan, meskipun di luar lagi musim panas? Ruang bangsal berpendingin banget."
            yutaka "Kenapa mesti minta izin? Beli saja yang Senpai suka."
            nar "Miyuki berkedip sekali, menyadari ia baru saja menyampaikan keinginannya sendiri tanpa menyelipkan kata maaf di ujung kalimat. Ia menekan tombolnya dengan jemari yang sudah tenang."
        elif _return == "B":
            nar "Kamu mundur setengah langkah dengan kedua tangan masuk ke saku celana, tidak menghentikan gerakannya mencari koin di dalam dompet."
            nar "Begitu ujung jarinya menemukan dua koin seratus yen, getaran kecil di tangannya sedikit mereda. Miyuki segera bergeser ke mesin minuman di sebelahnya, memasukkan uang dengan cepat, lalu menekan tombol kopi hitam dingin sampai kaleng logam itu jatuh ke baki bawah."
            nar "Ia membungkuk mengambil kaleng itu, menyeka embun dingin di permukaannya dengan ujung lengan jas, lalu menyodorkannya kepadamu dengan dua tangan."
            miyuki "Ini, Yutaka-kun. Kopi hitam dingin yang sama seperti pilihanmu tadi. Maaf jadi bikin kamu menunggu lebih lama."
            yutaka "Oh... makasih, Tachibana-senpai."
            nar "Tepat ketika jarimu menutup di sekitar kaleng dingin itu, bahu Miyuki turun sedikit. Senyum lega yang rapi baru muncul kembali di wajahnya setelah melihatmu menerimanya."
            miyuki "Nah. Sekarang sudah beres. Syukurlah kamu nggak jadi kehausan."
            nar "Kalian duduk sebentar di bangku tunggu lobi. Kamu menarik pembuka kaleng dan meneguk sedikit kopi dingin, sementara Miyuki memperhatikannya dengan tenang."
            miyuki "Dinginnya pas, kan? Nggak terlalu pahit?"
            yutaka "Pas kok. Tachibana-senpai sendiri nggak beli minum?"
            miyuki "Nanti saja di ruang jaga. Yang penting minumanmu sudah ada dulu."
            nar "Saat seorang pengunjung rumah sakit berjalan tergesa dan tanpa sengaja menyenggol ujung lengan jas Miyuki, Miyuki langsung berdiri sedikit dan membungkuk duluan sebelum orang itu sempat berkata apa-apa."
            miyuki "Ah, maaf sekali, aku agak menghalangi jalan."
            "Pengunjung" "Eh, nggak apa-apa, saya yang kurang hati-hati."
            yutaka "Tachibana-senpai, tadi kan bukan kamu yang menabrak. Kamu bahkan duduk rapi di pinggir bangku."
            miyuki "Nggak apa-apa, Yutaka-kun. Lebih cepat minta maaf duluan daripada bikin suasana koridor rumah sakit jadi canggung."
            nar "Miyuki duduk kembali dan merapikan saku jasnya dengan wajah tenang. Di matanya, persoalan selesai tuntas setiap kali orang di depannya tidak lagi tampak kecewa. Kebiasaan yang baru saja mendapat pembenaran halus itu akan keluar jauh lebih cepat pada kesempatan berikutnya."
        else:
            nar "Kamu membiarkan tangannya tetap memegang dompet kulit krem itu. Kamu melirik mesin yang macet, lalu menatap balik matanya yang cokelat kemerahan dengan jeda yang disengaja."
            yutaka "Ya sudah, kalau Tachibana-senpai memang merasa nggak enak, nggak perlu ganti dua ratus yen di sini. Kebetulan ada satu urusan yang bikin aku repot minggu ini."
            nar "Punggung Miyuki langsung menegak. Raut gelisahnya sedikit mengendur, seolah ia justru lega diberi cara konkret untuk menebus kesalahan yang sebenarnya tidak ada."
            miyuki "Apa pun itu, bilang saja, Yutaka-kun. Kalau aku bisa bantu, pasti kubantu."
            yutaka "Aku perlu ringkasan istilah operasional rumah sakit buat bahan makalah ekonomi kesehatan minggu ini. Istilah klinis di buku referensinya bikin aku bingung. Senpai bisa pilihkan lalu tuliskan poin pentingnya sebelum lusa?"
            nar "Kamu tahu betul jadwal rotasi klinik tahun keempat dan belajar ujiannya sudah menyita jam tidurnya, dan permintaan itu sama sekali jauh dari urusan mesin minuman. Miyuki sempat terdiam setengah detik menimbang hari, lalu buru-buru mengangguk."
            miyuki "Lusa pagi, ya... besok aku ada jaga bangsal sampai cukup larut, tapi selesai itu masih bisa kubuka bukunya di apartemen. Nanti aku rangkumkan alur rujukan sama istilah biayanya sekalian."
            nar "Kamu tidak menarik permintaanmu kembali ataupun menyuruhnya beristirahat saja. Kamu justru tersenyum tenang seolah mengandalkannya sepenuhnya."
            yutaka "Makasih banyak, Tachibana-senpai. Aku memang paling percaya sama ketelitian catatan Senpai."
            nar "Kalimat itu langsung menghapus sisa keraguannya. Ia mengeluarkan buku saku kecil dari balik jas putihnya dan membuka halaman yang sudah sesak oleh jadwal jaga bangsal, catatan kasus pasien, dan blok belajar malam."
            nar "Ia menambahkan satu baris baru bertuliskan ringkasan makalah untukmu di pinggiran sempit halaman itu tanpa mencoret satu pun jadwal lamanya."
            miyuki "Bisa. Nanti aku atur semuanya, jangan khawatir. Kalau ada bagian khusus yang ingin kamu fokuskan, kirim pesan saja kapan pun, ya."
            miyuki "Terima kasih sudah percaya sama aku, Yutaka-kun. Aku janji kali ini nggak bikin kamu kecewa."
            nar "Ponsel di saku jasnya bergetar singkat menandakan waktu jeda bangsal hampir selesai. Miyuki berdiri sambil merapikan kerah jas putihnya."
            miyuki "Aku naik dulu ke lantai tiga ya. Hati-hati di jalan pulang, jangan lupa minum air yang dingin."
            yutaka "Iya, semangat jaga bangsalnya, Tachibana-senpai."
            nar "Ia melangkah menuju lift dengan senyum yang terasa terlalu tenang. Urusanmu baru saja beres tanpa tenaga, sementara di saku jasnya bertambah satu alasan baru untuk takut gagal di depanmu."
    return

# ┌─ PANDUAN CERITA · Mi16 · Kesalahan di Bangsal
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : kesalahan klinis kecil; teguran keras.
# │ INTI    : A hibur / B tegas / C dingin / D bawa ke Yuina/Sato.
# │ AKHIRAN : gerbang Rute Masokis (stage 4); D membuka jalur pemulihan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi16:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana · Kesalahan di bangsal")
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Lampu koridor sayap pediatri Rumah Sakit Tachibana menyala putih bersih di atas lantai vinil yang mulai lengang. Bau antiseptik tipis bercampur udara pendingin ruangan yang dingin di sekitar bangku tunggu."
        else:
            nar "Cahaya bulan Oktober menembus jendela kaca panjang koridor sayap pediatri Rumah Sakit Tachibana. Langkah perawat melintas teratur di kejauhan, menyisakan sudut bangku tunggu yang tenang di dekat ruang istirahat."
        nar "Miyuki duduk tegak di bangku dengan jas dokter putih rapi dan stetoskop masih menggantung di lehernya. Rambut hitam panjang lurusnya terurai menutupi sebagian bahu, sementara kedua tangannya menggenggam papan catatan klinis terlalu erat di pangkuan."
        nar "Satu jam sebelumnya, ia sempat keliru menuliskan jam pantauan suhu pada salah satu lembar pasien anak dan langsung menyadari lalu mengoreksinya dalam lima menit sebelum berdampak pada tindakan apa pun. Namun dokter pembimbing tetap menegurnya dengan nada keras tepat di depan meja perawat."
        nar "Seorang perawat jaga yang baru keluar dari ruang observasi sempat berhenti sebentar di depan bangku kalian dengan senyum menenangkan sambil menepuk map miliknya."
        "Perawat" "Tachibana-san, lembar pantauan kamar tiga tadi sudah dicek ulang dokter jaga dan semuanya beres kok. Adik kecil di dalam juga sudah tidur nyenyak, ibunya tadi malah titip salam terima kasih soalnya kamu sabar banget waktu mengukur suhunya."
        miyuki "Maaf sekali sudah merepotkan tim jaga... saya benar-benar tidak teliti tadi. Lain kali saya akan mengecek ulang lebih awal lagi."
        "Perawat" "Sudah, nggak usah terus minta maaf begitu. Istirahat dulu ya, minum yang hangat."
        nar "Begitu langkah perawat itu berbelok menjauh di ujung koridor, senyum sopan di wajah Miyuki langsung lenyap tanpa sisa. Kamu menyodorkan segelas teh hangat dari mesin minuman ke samping tangannya, tetapi ia bahkan tidak melirik gelas itu."
        nar "Ia kembali membuka halaman belakang catatannya, memutar-mutar ujung pulpennya dengan gelisah sambil membaca ulang kalimat teguran yang baru saja ia salin sendiri dengan tinta biru yang sangat rapi."
        nar "Di bawah mata cokelat kemerahannya tampak bayangan letih yang tipis. Di tepi ibu jari kanannya bahkan ada bekas noda tinta biru samar akibat terlalu sering menyalin dan menggaris ulang kalimat di pinggir kertas."
        nar "Jari-jarinya yang putih pucat terus mengencang di pinggiran papan aluminium itu sampai ujung lengan jas dokternya kusut terlipat."
        miyuki "Pukul empat belas lewat sepuluh seharusnya tercatat empat belas lewat dua puluh... cuma beda sepuluh menit, tapi kalau aku sampai salah tulis di lembar yang lebih kritis bagaimana?"
        chiasa "Tachibana-senpai... bahkan perawat jaga barusan langsung bilang semuanya aman, pasien anaknya sudah tidur nyenyak, dan menyuruhmu istirahat. Teh hangatmu saja belum disentuh sejak sepuluh menit lalu."
        nar "Miyuki menggeleng pelan. Mata cokelat kemerahannya menatap baris tulisan di pangkuannya seperti seorang terdakwa yang sedang membacakan daftar bukti kesalahannya sendiri."
        miyuki "Kalau aku memang pantas memakai jas ini dan berdiri di bangsal anak, hal ceroboh seperti itu harusnya nggak pernah terjadi, Chiasa-chan."
        chiasa "Semua orang yang kerja jaga berturut-turut bisa salah tulis satu angka jam, Senpai. Yang penting Senpai langsung sadar lima menit kemudian dan langsung membetulkannya sendiri sebelum berdampak ke siapa pun."
        miyuki "Dokter pembimbing tadi benar kok... katanya orang yang terlalu mengandalkan nama keluarga sering menyepelekan hal kecil. Mungkin selama ini aku memang cuma kelihatan rapi di luar saja."
        chiasa "Tachibana-senpai sudah kerja paling pagi dan pulang paling terakhir di bangsal ini sepanjang bulan. Mana ada orang yang menyepelekan pekerjaan sampai lupa makan begitu?"
        miyuki "Tetap saja aku meleset, Chiasa-chan. Seharusnya aku mengecek tiga kali sebelum menyerahkan berkasnya. Mungkin sebaiknya aku minta tambahan jam jaga akhir pekan biar tanganku nggak ceroboh lagi."
        nar "Suaranya sama sekali tidak terdengar panik atau menangis, justru terlalu tenang dan terus menambahkan daftar hukuman untuk dirinya sendiri. Saat kamu menunduk melirik pangkuannya, kamu melihat pinggiran kertas catatannya dipenuhi tujuh baris pengulangan kalimat teguran yang persis sama."
        chiasa "{i}Ia mengulang seluruh teguran itu di luar kepala sampai hafal, seolah dadanya baru bisa berhenti sesak kalau ada hukuman yang cukup berat dijatuhkan kepadanya.{/i}"
        $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["\"Senpai sudah memperbaikinya tepat waktu. Satu kesalahan kecil nggak menghapus kerja kerasmu.\"", "Tegur dengan tegas agar ia berhenti merendahkan dirinya sendiri.", "Tarik perhatianmu dan bersikap dingin kepadanya.", "Ajak ia menemui Yuina atau konselor Sato Kyoko."])]
        call screen kk_choice_panel(_rows, "Sesudah teguran")
        $ kk_record_choice("Mi16", _return)
        if _return == "A":
            nar "Kamu meletakkan tanganmu lembut di atas papan catatannya supaya ia berhenti membalik halaman yang sama, lalu menggeser gelas teh hangat ke dekat jemarinya."
            chiasa "Tachibana-senpai nggak perlu merangkum seluruh dirimu cuma dari satu kesalahan jam yang bahkan sudah kamu bereskan sendiri. Anak-anak di bangsal itu selalu tenang tiap Senpai datang memeriksa, dan ibunya kamar tiga barusan bahkan menitip salam terima kasih. Satu salah tulis nggak menghapus semua itu."
            nar "Miyuki mengangkat wajah menatapmu. Ia berusaha sungguh-sungguh mendengar kalimatmu, tetapi garis tegang di antara alisnya tidak langsung meluruh."
            miyuki "Aku benar-benar ingin percaya ucapanmu, Chiasa-chan... tapi anehnya, setiap kali ada orang bilang aku sudah cukup baik, kepalaku malah langsung sibuk mencari bagian kurang mana yang belum sempat kamu lihat."
            chiasa "Suara di kepalamu itu lagi capek banget, Senpai. Nggak apa-apa kalau kamu belum langsung merasa lega hari ini. Aku juga nggak minta Senpai kelihatan sempurna atau ceria sekarang."
            chiasa "Yang penting berhenti menambah tuduhan baru ke buku catatanmu dulu, terus minum teh hangatnya mumpung masih panas."
            nar "Miyuki terdiam beberapa ketukan panjang, menatap uap tipis yang naik dari gelas kertasnya, lalu perlahan menyelipkan pulpennya kembali ke saku jas dokter dan menggenggam gelas hangat itu dengan kedua tangan."
            miyuki "...Tanganku ternyata sedingin ini ya dari tadi. Aku bahkan nggak sadar sampai menyentuh gelasnya."
            chiasa "Tadi di jalan masuk depan rumah sakit, pohon ginkgo di pinggir taman sudah mulai menguning terang semua, Senpai. Nanti kalau jam jaga selesai, kita jalan keluar pelan-pelan lihat taman sebentar ya, nggak usah bahas lembar bangsal lagi."
            miyuki "Pohon ginkgo dekat pintu depan ya... aku sampai nggak sempat menengok ke luar kaca sepanjang minggu ini."
            chiasa "Di papan gambar ruang tunggu anak tadi juga masih ada gambar krayon beruang yang kemarin Senpai bantu tempel. Itu juga bagian dari siapa Tachibana-senpai di rumah sakit ini."
            miyuki "...Haha, anak kamar dua yang menggambar telinganya kebesaran itu ya."
            chiasa "Nah, akhirnya ingat hal lain selain lembar teguran. Duduk dulu sepuluh menit di sini sebelum kembali ke bangsal, aku temani."
            miyuki "Baiklah... aku minum pelan-pelan dulu ya. Terima kasih masih mau duduk di sini tanpa memintaku cepat-cepat tersenyum, Chiasa-chan."
            nar "Ketegangan di bahunya belum sepenuhnya hilang, tetapi senyum tipis yang nyaris tak terlihat sempat singgah saat ia meneguk teh hangatnya perlahan dan berhenti menulis baris teguran baru di sampingmu."
        elif _return == "B":
            nar "Kamu menegakkan dudukmu dan menatapnya lurus dengan suara yang sengaja kamu buat tegas agar ia berhenti menyiksa dirinya sendiri di depan matamu."
            chiasa "Tachibana-senpai, tolong berhenti merendahkan dirimu sendiri terus-terusan. Kesalahannya sudah selesai satu jam lalu, kalau Senpai terus bicara seolah-olah nggak pantas berdiri di sini, itu sama sekali nggak membantu apa-apa."
            nar "Maksudmu jelas untuk menguatkannya dan memutus lingkaran pikiran buruknya. Namun begitu nada tegasmu jatuh di udara koridor yang hening, mata cokelat kemerahan Miyuki langsung berkejap turun seolah kalimatmu baru saja mendaftar satu lagi kegagalan yang baru ia perbuat."
            miyuki "Aku... sedang mencoba berhenti, Chiasa-chan. Maaf kalau keluhanku barusan bikin kamu capek mendengarnya."
            chiasa "Aku nggak bilang kamu bikin capek, Senpai. Aku bicara tegas karena aku peduli dan ingin kamu lebih menghargai usahamu sendiri daripada terus mengulang teguran dokter tadi..."
            nar "Belum sempat kalimatmu tuntas, Miyuki sudah menarik sudut bibirnya membentuk senyum senior yang rapi dan dingin seperti biasa, lalu menutup papan catatannya cepat-cepat."
            miyuki "Kamu nggak perlu merasa tidak enak sudah menegurku, Chiasa-chan. Aku memang butuh orang yang berani bicara keras supaya aku cepat sadar dan nggak terus mengeluh hal sepele di depan adik tingkat."
            chiasa "Tachibana-senpai, tunggu sebentar! Aku sama sekali nggak bermaksud menyuruh Senpai langsung pergi..."
            miyuki "Aku mengerti kok, Chiasa-chan. Lain kali aku nggak akan mengeluh seperti tadi lagi. Terima kasih sudah mengingatkanku ya, hati-hati di jalan pulang."
            chiasa "{i}Kalimat tegasku barusan malah langsung dia terima sebagai teguran kedua...{/i}"
            nar "Ia membungkuk sopan sekali lagi, lalu berbalik melangkah lurus menuju pintu ayun bangsal dengan punggung yang terlalu kaku dan cepat."
            nar "Daun pintu menutup pelan di belakangnya, meninggalkan gelas teh hangat yang belum tersentuh di atas bangku. Pembicaraan berhenti jauh lebih cepat daripada rasa bersalahnya, dan ia mengucapkan terima kasih semata karena mengira diam dan patuh adalah hal yang kamu harapkan."
        elif _return == "C":
            nar "Tepat ketika Miyuki menoleh kepadamu mencari pegangan, kamu sengaja memalingkan wajah menatap ujung koridor kosong. Kamu melipat kedua tanganmu dengan tenang dan membiarkan keheningan dingin menggantung di antara kalian."
            nar "Satu detik lewat tanpa satu pun kalimat penghibur. Alih-alih mundur menjaga jarak, napas Miyuki justru tersendat tipis. Ia langsung mencondongkan tubuh ke arahmu dengan cemas, membuka kembali papan catatannya cepat-cepat untuk menunjukkan halaman-halaman lain yang rapi seolah sedang memohon penilaian ulang."
            miyuki "Chiasa-chan... kamu kecewa juga ya melihatku ceroboh begini? Tadi pasien kamar dua sampai kamar lima semua datanya sudah kuperiksa ulang dua kali kok, lihat ini semua angkanya rapi..."
            miyuki "Kalau kamu mau, habis jam jaga nanti biar aku bantu mencarikan referensi anatomi buat tugas senimu juga, atau aku bawakan kue yang kemarin kamu suka. Asal kamu jangan diam begini..."
            chiasa "Kalau Tachibana-senpai memang sadar tadi kurang teliti, cukup buktikan lewat sikapmu mulai hari ini. Aku nggak butuh penjelasan panjang atau janji macam-macam."
            nar "Mata cokelat kemerahan Miyuki membelalak tipis mendengar nada dinginmu yang nyaris tanpa kehangatan, lalu jarinya mencengkeram ujung jas dokternya erat-erat."
            miyuki "Bilang saja apa yang harus kubetulkan atau kulakukan, Chiasa-chan. Kalau kamu diam dan memalingkan muka begini, aku nggak tahu kapan aku boleh berhenti merasa salah."
            chiasa "Tutup papan catatanmu sekarang, duduk tegak, dan pastikan besok nggak ada satu baris pun yang meleset lagi."
            nar "Kamu melihat bahunya yang sejak tadi gemetar justru sedikit mengendur begitu kamu menjatuhkan perintah dingin itu kepadanya. Dengan gerakan patuh yang menyakitkan dilihat, ia langsung menutup papan aluminium itu di atas pangkuannya."
            miyuki "...Iya. Aku mengerti. Besok boleh kutunjukkan catatanku yang baru supaya kamu periksa sendiri apakah sudah cukup rapi, Chiasa-chan?"
            chiasa "Lihat nanti saja."
            miyuki "Terima kasih karena kamu masih mau bicara padaku, Chiasa-chan."
            chiasa "{i}Dia malah kelihatan tenang setelah kudiamkan lalu kuberi perintah dingin...{/i}"
            nar "Senyum tipis yang muncul di wajahnya terasa begitu ganjil. Kedekatan di antara kalian mengencang dengan cara yang rusak, membuat ketenangannya mulai bergantung sepenuhnya pada kapan kamu bersedia mengakhiri hukuman yang tidak pernah jelas."
        else:
            nar "Kamu meletakkan tanganmu pelan di samping papan catatan Miyuki dan berbicara dengan suara rendah yang tidak menghakimi."
            if kk_has("miyuki_sato_dikenal"):
                chiasa "Tachibana-senpai masih simpan kartu kontak Sato Kyoko yang kemarin diberikan Yuina-san kan? Ayo kita panggil Yuina-san sebentar dan atur jadwal bicara dengan Sato-san."
            else:
                chiasa "Tachibana-senpai nggak bisa terus memikul ini sendirian di kepala. Gimana kalau kita panggil Yuina-san sekarang, lalu cari jadwal bicara dengan konselor Sato Kyoko di kampus?"
            nar "Refleks lama Miyuki langsung membuatnya menggeleng cepat sambil berusaha menarik papan catatannya mundur."
            miyuki "Jangan, Chiasa-chan... Yuina juga lagi sibuk jaga di lantai atas, aku nggak mau merepotkan dia atau konselor cuma gara-gara salah tulis satu baris di bangsal..."
            chiasa "Coba Senpai lihat sendiri pinggiran kertas catatanmu. Kamu menyalin kalimat teguran yang sama sampai tujuh kali dalam satu jam. Itu sudah jauh melewati evaluasi kerja biasa."
            nar "Miyuki terdiam, pandangannya jatuh pada deretan tulisan tangannya sendiri yang tampak semakin gemetar di baris ketujuh. Bahunya meluruh perlahan sementara mata cokelat kemerahannya mulai berkaca-kaca tipis."
            miyuki "...Aku capek sekali mendengar suara ini terus menyalahkanku di dalam kepala, Chiasa-chan. Bahkan waktu tidur pun rasanya nggak pernah berhenti. Aku... mau mencoba bicara."
            nar "Kamu mengirim pesan singkat yang langsung dibalas seketika. Lima menit berselang, langkah cepat terdengar di koridor dan Akiyama Yuina muncul dengan jas lab berhias banyak pin, rambut cokelat bob pendeknya sedikit berantakan karena baru turun dari bangsal atas."
            miyuki "Eh, Yuina? Aku beneran nggak apa-apa kok, nggak usah repot turun dari lantai atas..."
            "Yuina" "Jangan mulai lagi, Miyuki. Aku kenal mukamu kalau sudah hampir tumbang."
            nar "Yuina langsung duduk di sisi lain Miyuki, menarik papan catatan aluminium itu dengan tegas dari jari-jari Miyuki yang kaku lalu menyentuh sebentar punggung tangannya yang dingin."
            "Yuina" "Sini papannya kukembalikan ke meja jaga, kamu nggak boleh pegang ini lagi sampai habis makan. Tanganmu sedingin es, kamu belum makan, dan catatanmu penuh coretan ulang lagi."
            nar "Ia menoleh singkat kepadamu di seberang bangku dengan anggukan lugas penuh rasa terima kasih."
            "Yuina" "Makasih sudah langsung kabari aku dan nggak membiarkan dia berputar sendirian di sini, Chiasa-san."
            chiasa "Aku cuma menemani Tachibana-senpai sampai Yuina-san datang."
            "Yuina" "Kalau cuma disuruh semangat sama istirahat, dia pasti cuma mengangguk sopan terus begadang lagi. Besok pagi kita telepon Sato-san buat cari waktu paling pas minggu ini. Kamu nggak perlu menjelaskan semuanya sekaligus hari ini."
            miyuki "Maaf merepotkanmu di jam jaga, Yuina..."
            "Yuina" "Berhenti minta maaf buat hal yang nggak perlu. Sekarang ayo berdiri pelan-pelan, ikut aku turun ambil roti hangat di kantin bawah."
            nar "Sebelum mengiringi Miyuki melangkah pergi, Yuina sempat menoleh setengah badan kepadamu dengan suara pelan yang sungguh-sungguh."
            "Yuina" "Kalau suatu saat kamu lihat dia mulai menyalin ulang teguran begini lagi, langsung hubungi aku lagi ya, Chiasa-san. Satu orang saja yang menyela tepat waktu itu besar sekali artinya buat dia."
            chiasa "Pasti kukabari, Yuina-san. Tolong jaga Tachibana-senpai ya."
            miyuki "Iya, Yuina... terima kasih. Terima kasih banyak juga sudah menahanku tadi, Chiasa-chan."
            nar "Miyuki bangkit perlahan bersama Yuina tanpa menoleh lagi ke papan catatannya. Untuk sementara, kesalahan di bangsal tidak lagi menjadi satu-satunya hal yang dibicarakan tentang dirinya."
    else:
        if kk_slot >= 3:
            nar "Lampu koridor sayap pediatri Rumah Sakit Tachibana menyala putih bersih di atas lantai vinil yang mulai lengang. Bau antiseptik tipis bercampur udara pendingin ruangan yang dingin di sekitar bangku tunggu."
        else:
            nar "Cahaya bulan Oktober menembus jendela kaca panjang koridor sayap pediatri Rumah Sakit Tachibana. Langkah perawat melintas teratur di kejauhan, menyisakan sudut bangku tunggu yang tenang di dekat ruang istirahat."
        nar "Miyuki duduk tegak di bangku dengan jas dokter putih rapi dan stetoskop masih menggantung di lehernya. Rambut hitam panjang lurusnya terurai menutupi sebagian bahu, sementara kedua tangannya menggenggam papan catatan klinis terlalu erat di pangkuan."
        nar "Satu jam sebelumnya, ia sempat keliru menuliskan jam pantauan suhu pada salah satu lembar pasien anak dan langsung menyadari lalu mengoreksinya dalam lima menit sebelum berdampak pada tindakan apa pun. Namun dokter pembimbing tetap menegurnya dengan nada keras tepat di depan meja perawat."
        nar "Seorang perawat jaga yang baru keluar dari ruang observasi sempat berhenti sebentar di depan bangku kalian dengan senyum menenangkan sambil menepuk map miliknya."
        "Perawat" "Tachibana-san, lembar pantauan kamar tiga tadi sudah dicek ulang dokter jaga dan semuanya beres kok. Adik kecil di dalam juga sudah tidur nyenyak, ibunya tadi malah titip salam terima kasih soalnya kamu sabar banget waktu mengukur suhunya."
        miyuki "Maaf sekali sudah merepotkan tim jaga... saya benar-benar tidak teliti tadi. Lain kali saya akan mengecek ulang lebih awal lagi."
        "Perawat" "Sudah, nggak usah terus minta maaf begitu. Istirahat dulu ya, minum yang hangat."
        nar "Begitu langkah perawat itu berbelok menjauh di ujung koridor, senyum sopan di wajah Miyuki langsung lenyap tanpa sisa. Kamu menyodorkan segelas teh hangat dari mesin minuman ke samping tangannya, tetapi ia bahkan tidak melirik gelas itu."
        nar "Ia kembali membuka halaman belakang catatannya, memutar-mutar ujung pulpennya dengan gelisah sambil membaca ulang kalimat teguran yang baru saja ia salin sendiri dengan tinta biru yang sangat rapi."
        nar "Di bawah mata cokelat kemerahannya tampak bayangan letih yang tipis. Di tepi ibu jari kanannya bahkan ada bekas noda tinta biru samar akibat terlalu sering menyalin dan menggaris ulang kalimat di pinggir kertas."
        nar "Jari-jarinya yang putih pucat terus mengencang di pinggiran papan aluminium itu sampai ujung lengan jas dokternya kusut terlipat."
        miyuki "Pukul empat belas lewat sepuluh seharusnya tercatat empat belas lewat dua puluh... cuma beda sepuluh menit, tapi kalau aku sampai salah tulis di lembar yang lebih kritis bagaimana?"
        yutaka "Tachibana-senpai... bahkan perawat jaga barusan langsung bilang semuanya aman, pasien anaknya sudah tidur nyenyak, dan menyuruhmu istirahat. Teh hangatmu saja belum disentuh sejak sepuluh menit lalu."
        nar "Miyuki menggeleng pelan. Mata cokelat kemerahannya menatap baris tulisan di pangkuannya seperti seorang terdakwa yang sedang membacakan daftar bukti kesalahannya sendiri."
        miyuki "Kalau aku memang pantas memakai jas ini dan berdiri di bangsal anak, hal ceroboh seperti itu harusnya nggak pernah terjadi, Yutaka-kun."
        yutaka "Semua orang yang kerja jaga berturut-turut bisa salah tulis satu angka jam, Senpai. Yang penting Senpai langsung sadar lima menit kemudian dan langsung membetulkannya sendiri sebelum berdampak ke siapa pun."
        miyuki "Dokter pembimbing tadi benar kok... katanya orang yang terlalu mengandalkan nama keluarga sering menyepelekan hal kecil. Mungkin selama ini aku memang cuma kelihatan rapi di luar saja."
        yutaka "Aku cukup kenal seperti apa rasanya dinilai lewat nama belakang sebelum orang melihat kerja kerasnya, Senpai. Kamu datang paling pagi dan pulang paling terakhir di bangsal ini sepanjang bulan, nggak ada ceritanya kamu menyepelekan pekerjaan."
        miyuki "Tetap saja aku meleset, Yutaka-kun. Seharusnya aku mengecek tiga kali sebelum menyerahkan berkasnya. Mungkin sebaiknya aku minta tambahan jam jaga akhir pekan biar tanganku nggak ceroboh lagi."
        nar "Suaranya sama sekali tidak terdengar panik atau menangis, justru terlalu tenang dan terus menambahkan daftar hukuman untuk dirinya sendiri. Saat kamu menunduk melirik pangkuannya, kamu melihat pinggiran kertas catatannya dipenuhi tujuh baris pengulangan kalimat teguran yang persis sama."
        yutaka "{i}Ia mengulang seluruh teguran itu di luar kepala sampai hafal, seolah dadanya baru bisa berhenti sesak kalau ada hukuman yang cukup berat dijatuhkan kepadanya.{/i}"
        $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["\"Senpai sudah memperbaikinya tepat waktu. Satu kesalahan kecil nggak menghapus kerja kerasmu.\"", "Tegur dengan tegas agar ia berhenti merendahkan dirinya sendiri.", "Tarik perhatianmu dan bersikap dingin kepadanya.", "Ajak ia menemui Yuina atau konselor Sato Kyoko."])]
        call screen kk_choice_panel(_rows, "Sesudah teguran")
        $ kk_record_choice("Mi16", _return)
        if _return == "A":
            nar "Kamu meletakkan tanganmu dengan tenang di tepi papan catatannya supaya ia berhenti membalik halaman yang sama, lalu menggeser gelas teh hangat ke dekat jemarinya."
            yutaka "Tachibana-senpai nggak perlu merangkum seluruh dirimu cuma dari satu kesalahan jam yang bahkan sudah kamu bereskan sendiri. Anak-anak di bangsal itu selalu tenang tiap Senpai datang memeriksa, dan ibunya kamar tiga barusan bahkan menitip salam terima kasih. Satu salah tulis nggak menghapus semua itu."
            nar "Miyuki mengangkat wajah menatapmu. Ia berusaha sungguh-sungguh mendengar kalimatmu, tetapi garis tegang di antara alisnya tidak langsung meluruh."
            miyuki "Aku benar-benar ingin percaya ucapanmu, Yutaka-kun... tapi anehnya, setiap kali ada orang bilang aku sudah cukup baik, kepalaku malah langsung sibuk mencari bagian kurang mana yang belum sempat kamu lihat."
            yutaka "Kepalamu lagi capek banget, Senpai. Nggak apa-apa kalau kamu belum langsung merasa lega hari ini. Aku juga nggak minta Senpai kelihatan sempurna atau ceria sekarang."
            yutaka "Yang penting berhenti menambah tuduhan baru ke buku catatanmu dulu, terus minum teh hangatnya mumpung masih panas."
            nar "Miyuki terdiam beberapa ketukan panjang, menatap uap tipis yang naik dari gelas kertasnya, lalu perlahan menyelipkan pulpennya kembali ke saku jas dokter dan menggenggam gelas hangat itu dengan kedua tangan."
            miyuki "...Tanganku ternyata sedingin ini ya dari tadi. Aku bahkan nggak sadar sampai menyentuh gelasnya."
            yutaka "Tadi waktu aku masuk lewat gerbang rumah sakit, pohon ginkgo di pinggir taman sudah menguning terang semua, Senpai. Nanti habis jam jaga selesai, kita jalan keluar pelan-pelan lihat taman sebentar, nggak usah bahas lembar bangsal lagi."
            miyuki "Pohon ginkgo dekat pintu depan ya... aku sampai nggak sempat menengok ke luar kaca sepanjang minggu ini."
            yutaka "Di papan gambar ruang tunggu anak tadi juga masih ada gambar krayon beruang yang kemarin Senpai bantu tempel. Itu juga bagian dari siapa Tachibana-senpai di rumah sakit ini."
            miyuki "...Haha, anak kamar dua yang menggambar telinganya kebesaran itu ya."
            yutaka "Nah, akhirnya ingat hal lain selain lembar teguran. Duduk dulu sepuluh menit di sini sebelum kembali ke bangsal, aku temani."
            miyuki "Baiklah... aku minum pelan-pelan dulu ya. Terima kasih masih mau duduk di sini tanpa memintaku cepat-cepat tersenyum, Yutaka-kun."
            nar "Ketegangan di bahunya belum sepenuhnya hilang, tetapi senyum tipis yang nyaris tak terlihat sempat singgah saat ia meneguk teh hangatnya perlahan dan berhenti menulis baris teguran baru di sampingmu."
        elif _return == "B":
            nar "Kamu menegakkan dudukmu dan menatapnya lurus dengan suara yang sengaja kamu buat tegas dan berat agar ia berhenti menyiksa dirinya sendiri di depan matamu."
            yutaka "Tachibana-senpai, tolong berhenti merendahkan dirimu sendiri terus-terusan. Kesalahannya sudah selesai satu jam lalu, kalau Senpai terus bicara seolah-olah nggak pantas berdiri di sini, itu sama sekali nggak membantu apa-apa."
            nar "Maksudmu jelas untuk menguatkannya dan memutus lingkaran pikiran buruknya. Namun begitu nada tegasmu jatuh di udara koridor yang hening, mata cokelat kemerahan Miyuki langsung berkejap turun seolah kalimatmu baru saja mendaftar satu lagi kegagalan yang baru ia perbuat."
            miyuki "Aku... sedang mencoba berhenti, Yutaka-kun. Maaf kalau keluhanku barusan bikin kamu capek mendengarnya."
            yutaka "Aku nggak bilang kamu bikin capek, Senpai. Aku bicara tegas karena aku peduli dan ingin kamu lebih menghargai usahamu sendiri daripada terus mengulang teguran dokter tadi..."
            nar "Belum sempat kalimatmu tuntas, Miyuki sudah menarik sudut bibirnya membentuk senyum senior yang rapi dan dingin seperti biasa, lalu menutup papan catatannya cepat-cepat."
            miyuki "Kamu nggak perlu merasa tidak enak sudah menegurku, Yutaka-kun. Aku memang butuh orang yang berani bicara keras supaya aku cepat sadar dan nggak terus mengeluh hal sepele di depan adik tingkat."
            yutaka "Tachibana-senpai, tunggu sebentar! Aku sama sekali nggak bermaksud menyuruh Senpai langsung pergi..."
            miyuki "Aku mengerti kok, Yutaka-kun. Lain kali aku nggak akan mengeluh seperti tadi lagi. Terima kasih sudah mengingatkanku ya, hati-hati di jalan pulang."
            yutaka "{i}Kalimat tegasku barusan malah langsung dia terima sebagai teguran kedua...{/i}"
            nar "Ia membungkuk sopan sekali lagi, lalu berbalik melangkah lurus menuju pintu ayun bangsal dengan punggung yang terlalu kaku dan cepat."
            nar "Daun pintu menutup pelan di belakangnya, meninggalkan gelas teh hangat yang belum tersentuh di atas bangku. Pembicaraan berhenti jauh lebih cepat daripada rasa bersalahnya, dan ia mengucapkan terima kasih semata karena mengira diam dan patuh adalah hal yang kamu harapkan."
        elif _return == "C":
            nar "Tepat ketika Miyuki menoleh kepadamu mencari pegangan, kamu sengaja memalingkan wajah menatap ujung koridor kosong. Kamu melipat kedua tanganmu dengan tenang dan membiarkan keheningan dingin menggantung di antara kalian."
            nar "Satu detik lewat tanpa satu pun kalimat penghibur. Alih-alih mundur menjaga jarak, napas Miyuki justru tersendat tipis. Ia langsung mencondongkan tubuh ke arahmu dengan cemas, membuka kembali papan catatannya cepat-cepat untuk menunjukkan halaman-halaman lain yang rapi seolah sedang memohon penilaian ulang."
            miyuki "Yutaka-kun... kamu kecewa juga ya melihatku ceroboh begini? Tadi pasien kamar dua sampai kamar lima semua datanya sudah kuperiksa ulang dua kali kok, lihat ini semua angkanya rapi..."
            miyuki "Kalau kamu mau, habis jam jaga nanti biar aku bantu merangkumkan istilah medis buat makalah ekonomimu juga, atau aku bawakan kue yang kemarin kamu suka. Asal kamu jangan diam begini..."
            yutaka "Kalau Tachibana-senpai memang sadar tadi kurang teliti, cukup buktikan lewat sikapmu mulai hari ini. Aku nggak butuh penjelasan panjang atau janji macam-macam."
            nar "Mata cokelat kemerahan Miyuki membelalak tipis mendengar nada dinginmu yang nyaris tanpa kehangatan, lalu jarinya mencengkeram ujung jas dokternya erat-erat."
            miyuki "Bilang saja apa yang harus kubetulkan atau kulakukan, Yutaka-kun. Kalau kamu diam dan memalingkan muka begini, aku nggak tahu kapan aku boleh berhenti merasa salah."
            yutaka "Tutup papan catatanmu sekarang, duduk tegak, dan pastikan besok nggak ada satu baris pun yang meleset lagi."
            nar "Kamu melihat bahunya yang sejak tadi gemetar justru sedikit mengendur begitu kamu menjatuhkan perintah dingin itu kepadanya. Dengan gerakan patuh yang menyakitkan dilihat, ia langsung menutup papan aluminium itu di atas pangkuannya."
            miyuki "...Iya. Aku mengerti. Besok boleh kutunjukkan catatanku yang baru supaya kamu periksa sendiri apakah sudah cukup rapi, Yutaka-kun?"
            yutaka "Lihat nanti saja."
            miyuki "Terima kasih karena kamu masih mau bicara padaku, Yutaka-kun."
            yutaka "{i}Dia malah kelihatan tenang setelah kudiamkan lalu kuberi perintah dingin...{/i}"
            nar "Senyum tipis yang muncul di wajahnya terasa begitu ganjil. Kedekatan di antara kalian mengencang dengan cara yang rusak, membuat ketenangannya mulai bergantung sepenuhnya pada kapan kamu bersedia mengakhiri hukuman yang tidak pernah jelas."
        else:
            nar "Kamu meletakkan tanganmu pelan di samping papan catatan Miyuki dan berbicara dengan suara rendah yang tidak menghakimi."
            if kk_has("miyuki_sato_dikenal"):
                yutaka "Tachibana-senpai masih simpan kartu kontak Sato Kyoko yang kemarin diberikan Yuina-san kan? Ayo kita panggil Yuina-san sebentar dan atur jadwal bicara dengan Sato-san."
            else:
                yutaka "Tachibana-senpai nggak bisa terus memikul ini sendirian di kepala. Gimana kalau kita panggil Yuina-san sekarang, lalu cari jadwal bicara dengan konselor Sato Kyoko di kampus?"
            nar "Refleks lama Miyuki langsung membuatnya menggeleng cepat sambil berusaha menarik papan catatannya mundur."
            miyuki "Jangan, Yutaka-kun... Yuina juga lagi sibuk jaga di lantai atas, aku nggak mau merepotkan dia atau konselor cuma gara-gara salah tulis satu baris di bangsal..."
            yutaka "Coba Senpai lihat sendiri pinggiran kertas catatanmu. Kamu menyalin kalimat teguran yang sama sampai tujuh kali dalam satu jam. Itu sudah jauh melewati evaluasi kerja biasa."
            nar "Miyuki terdiam, pandangannya jatuh pada deretan tulisan tangannya sendiri yang tampak semakin gemetar di baris ketujuh. Bahunya meluruh perlahan sementara mata cokelat kemerahannya mulai berkaca-kaca tipis."
            miyuki "...Aku capek sekali mendengar suara ini terus menyalahkanku di dalam kepala, Yutaka-kun. Bahkan waktu tidur pun rasanya nggak pernah berhenti. Aku... mau mencoba bicara."
            nar "Kamu mengirim pesan singkat yang langsung dibalas seketika. Lima menit berselang, langkah cepat terdengar di koridor dan Akiyama Yuina muncul dengan jas lab berhias banyak pin, rambut cokelat bob pendeknya sedikit berantakan karena baru turun dari bangsal atas."
            miyuki "Eh, Yuina? Aku beneran nggak apa-apa kok, nggak usah repot turun dari lantai atas..."
            "Yuina" "Jangan mulai lagi, Miyuki. Aku kenal mukamu kalau sudah hampir tumbang."
            nar "Yuina langsung duduk di sisi lain Miyuki, menarik papan catatan aluminium itu dengan tegas dari jari-jari Miyuki yang kaku lalu menyentuh sebentar punggung tangannya yang dingin."
            "Yuina" "Sini papannya kukembalikan ke meja jaga, kamu nggak boleh pegang ini lagi sampai habis makan. Tanganmu sedingin es, kamu belum makan, dan catatanmu penuh coretan ulang lagi."
            nar "Ia menoleh singkat kepadamu di seberang bangku dengan anggukan lugas penuh rasa terima kasih."
            "Yuina" "Makasih sudah langsung kabari aku dan nggak membiarkan dia berputar sendirian di sini, Kisaragi-kun."
            yutaka "Aku cuma menemani Tachibana-senpai sampai Yuina-san datang."
            "Yuina" "Kalau cuma disuruh semangat sama istirahat, dia pasti cuma mengangguk sopan terus begadang lagi. Besok pagi kita telepon Sato-san buat cari waktu paling pas minggu ini. Kamu nggak perlu menjelaskan semuanya sekaligus hari ini."
            miyuki "Maaf merepotkanmu di jam jaga, Yuina..."
            "Yuina" "Berhenti minta maaf buat hal yang nggak perlu. Sekarang ayo berdiri pelan-pelan, ikut aku turun ambil roti hangat di kantin bawah."
            nar "Sebelum mengiringi Miyuki melangkah pergi, Yuina sempat menoleh setengah badan kepadamu dengan suara pelan yang sungguh-sungguh."
            "Yuina" "Kalau suatu saat kamu lihat dia mulai menyalin ulang teguran begini lagi, langsung hubungi aku lagi ya, Kisaragi-kun. Satu orang saja yang menyela tepat waktu itu besar sekali artinya buat dia."
            yutaka "Pasti kukabari, Yuina-san. Tolong jaga Tachibana-senpai."
            miyuki "Iya, Yuina... terima kasih. Terima kasih banyak juga sudah menahanku tadi, Yutaka-kun."
            nar "Miyuki bangkit perlahan bersama Yuina tanpa menoleh lagi ke papan catatannya. Untuk sementara, kesalahan di bangsal tidak lagi menjadi satu-satunya hal yang dibicarakan tentang dirinya."
    return

# ┌─ PANDUAN CERITA · Mi17 · Pingsan di Pameran
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : kelelahan ekstrem.
# │ INTI    : A bawa ke UGD / B diam / C manfaatkan.
# │ AKHIRAN : Yuina menegur pemain.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi17:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana · Pingsan")
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Lampu putih aula sayap pengunjung Rumah Sakit Tachibana bersinar terang di atas deretan meja stan pameran kesehatan terbuka bulan November. Meski jam kunjungan mulai menipis, antrean terakhir keluarga pasien masih bertahan di dekat pojok konsultasi anak."
        else:
            nar "Cahaya bulan November masuk melewati jendela kaca besar aula sayap pengunjung Rumah Sakit Tachibana yang ramai oleh stan pameran kesehatan terbuka. Poster ilustrasi edukasi anak berjejer di sepanjang dinding sementara antrean pengunjung bergantian mengisi kursi periksa."
        nar "Kamu datang mengantarkan beberapa lembar poster ilustrasi edukasi tambahan yang sempat diminta Fakultas Kedokteran. Begitu kamu menyandarkan gulungan poster di sudut belakang meja stan, kamu sempat melirik papan jadwal di samping kursi Miyuki yang dipenuhi dua giliran jaga tambahan bertinta merah."
        nar "Sejak kamu tiba lima belas menit lalu, Miyuki tidak pernah sekali pun duduk lebih dari satu menit di kursinya. Botol air mineralnya pun masih terisi penuh di samping kotak bekal plastik yang belum dibuka sama sekali di dekat kaki meja."
        nar "Jas dokter putihnya masih terkancing rapi dengan stetoskop menggantung di leher, rambut hitam panjang lurusnya terurai tenang di atas bahu. Namun dari samping meja, kamu melihat jelas bibirnya pucat kering dan lingkar bawah mata cokelat kemerahannya gelap sekali."
        "Relawan Medis" "Tachibana-senpai, antrean tinggal empat keluarga lagi. Senpai istirahat dulu sepuluh menit di belakang yuk, dari tadi kotak makan Senpai di bawah meja saja belum disentuh kan?"
        miyuki "Terima kasih perhatiannya, aku baik-baik saja kok. Sisa empat keluarga ini biar kubantu selesaikan dulu, ibunya yang nomor empat tadi sudah menunggu lumayan lama."
        nar "Kamu melihat tangan kirinya sempat menekan tepi meja lipat selama satu detik seolah sedang menahan pusing ringan sebelum ia segera menegakkan punggungnya lagi."
        chiasa "Tachibana-senpai, mukamu beneran kelihatan pucat banget lho. Barusan Senpai agak limbung ya? Duduk sebentar aja dulu, biar aku bantu bagikan brosur anak-anak di depan meja."
        miyuki "Ara, cuma udara ruangan pameran agak hangat saja kok, Chiasa-chan. Terima kasih banyak ya sudah antar posternya. Sebentar saja lagi, habis menyerahkan lembar jadwal imunisasi ini aku langsung istirahat."
        chiasa "Minimal minum airnya seteguk dulu dong, Senpai. Botol di sebelah tasmu masih penuh dari tadi."
        miyuki "Iya, nanti langsung kuminum begitu selesai bicara dengan ibu yang ini ya."
        nar "Ia menarik senyum hangatnya kembali dan menoleh menyambut seorang ibu bersama anak kecil yang baru mendekat ke tepi meja stan. Melihat si kecil sedikit takut pada jas dokter, Miyuki langsung berjongkok sejajar tinggi anak itu dan mengeluarkan stiker beruang kecil dari saku jasnya dengan jari yang sedikit gemetar."
        miyuki "Halo, hebat sekali sudah mau ikut antre bersama Ibu. Mau tempel stiker beruang di punggung tangan dulu?"
        "Anak Kecil" "Mau! Beruangnya lucu!"
        "Tamu Pameran" "Permisi, Dokter, terima kasih banyak tadi anak saya mau diperiksa tanpa menangis. Boleh tanya sedikit soal catatan demam yang tadi dijelaskan di papan?"
        miyuki "Tentu, silakan tunggu sebentar ya, saya ambilkan lembar contohnya di ujung meja..."
        nar "Miyuki berputar setengah langkah sambil menjangkau map plastik tebal. Tepat saat ujung jemarinya menyentuh map itu, kedua bahunya mendadak bergetar tipis dan tatapan mata cokelat kemerahannya kehilangan titik fokus."
        nar "Ia masih berusaha meminta tamu pameran menunggu sebentar dengan suara pelan yang terputus di tengah kata ketika kedua lututnya tiba-tiba kehilangan tenaga."
        miyuki "Maaf... sebentar..."
        nar "Map plastik terlepas begitu saja dari tangannya. Lembaran brosur, lembar stiker, dan kertas jadwal meluncur jauh menyebar di atas lantai vinil, sementara tubuh Miyuki merosot jatuh miring di belakang meja stan."
        "Tamu Pameran" "Eh?! Dokternya jatuh! Tolong, ada yang pingsan di sini!"
        "Relawan Medis" "Tachibana-senpai! Senpai, dengar suaraku nggak?!"
        "Anak Kecil" "Ibu, dokternya tidur di lantai?"
        nar "Suara keramaian aula mendadak terasa jauh dan gaduh bersamaan. Kamu berdiri paling dekat di sisi belakang meja ketika nama Miyuki dipanggil berulang kali tanpa satu pun jawaban keluar dari bibirnya yang pucat."
        chiasa "{i}Badannya benar-benar sudah habis tenaganya dari tadi... dan sekarang ia tergeletak tepat di depan kakiku.{/i}"
        call kk_family_menu("Mi17", ["Panggil petugas dan bawa ia ke UGD segera.", "Diam di tempat dan tunggu ia sadar sendiri.", "Manfaatkan keadaannya yang lemah untuk menuntut sesuatu darinya."])
        if _return == "A":
            nar "Kamu langsung berlutut di samping Miyuki, menahan kepala dan bahunya agar tidak terbentur kaki meja besi, lalu menoleh cepat ke arah relawan yang masih terpaku kaget."
            chiasa "Tolong cepat panggil perawat UGD dan minta brankar sekarang juga! Jangan dikerumuni dulu biar udaranya kebuka!"
            "Relawan Medis" "B-baik! Aku langsung lari ke meja perawat pintu sebelah!"
            chiasa "Tachibana-senpai, tenang ya, petugasnya sebentar lagi datang."
            nar "Kamu melonggarkan kancing teratas jas dokternya perlahan agar napasnya lebih lega, memungut cepat map dan lembar stikernya ke dalam tasmu, lalu membantu perawat jaga memindahkannya ke brankar dorong menyusuri koridor sampai ke bilik pemeriksaan UGD."
            "Perawat UGD" "Tekanan darahnya agak rendah dan kadar gulanya turun, kemungkinan besar kelelahan ekstrem plus telat makan. Saya pasang infus cairan dulu ya, tolong tunggu sebentar."
            chiasa "Baik, terima kasih banyak."
            nar "Dua puluh menit kemudian, ketika cairan infus sudah menetes teratur di punggung tangan Miyuki dan kelopak mata cokelat kemerahannya baru mulai terbuka sayu, tirai putih bilik tersibak cepat."
            nar "Akiyama Yuina masuk dengan napas sedikit terengah, jas lab penuh pin dan kacamata bingkai tipisnya agak miring karena baru turun berlari dari ruang jaga atas. Ia langsung mengecek papan tensi di samping ranjang."
            "Yuina" "Tekanan darahnya turun, dehidrasi, kurang tidur beruntun... astaga, Miyuki, kamu beneran nekat sampai tumbang di depan stan sendiri."
            chiasa "Kotak makannya di bawah meja stan tadi memang masih utuh belum dibuka sama sekali, Yuina-san."
            "Yuina" "Sudah kuduga. Tiap sibuk jaga dia selalu lupa tubuhnya sendiri."
            miyuki "Yuina... maaf ya... pamerannya di depan tadi belum selesai, ibu yang mengantre nomor empat tadi masih menunggu lembaran... sama stiker beruangku tadi jatuh semua di lantai ya?"
            chiasa "Lembar brosur sama stikernya sudah kurapikan semua di tasku, Tachibana-senpai. Nggak ada yang hilang."
            "Yuina" "Dan ada orang lain di sana, Miyuki. Relawan sama dokter jaga sudah ambil alih meja stan sejak lima menit lalu. Sekarang kamu di sini dulu, diam di atas ranjang."
            nar "Yuina menoleh kepadamu dengan hembusan napas lega yang jujur, bahunya yang sejak tadi tegang akhirnya sedikit turun."
            "Yuina" "Makasih sudah cepat bawa dia masuk UGD, Chiasa-san. Aku akan bantu bereskan urusan jadwalnya sama dokter pembimbing hari ini. Tolong banget, jangan biarkan dia mengira harus langsung balik kerja begitu dia bilang sudah enakan."
            chiasa "Iya, Yuina-san. Kalau dia coba bangun lagi sebelum infusnya habis, aku langsung kabari Yuina-san."
            miyuki "Chiasa-chan juga... kamu jadi ketinggalan jadwal pameran seni di kampus gara-gara mengurusku di sini ya? Maaf sekali sudah bikin kamu kaget dan repot..."
            chiasa "Nggak usah memikirkan pameranku dulu, Tachibana-senpai. Di gedung seni masih ada Karuha yang jaga. Tugas Senpai hari ini cuma tidur dan membiarkan orang lain mengurus sisanya."
            "Yuina" "Dengar tuh kata Chiasa-san. Minum air hangatnya sedikit, lalu pejamkan mata. Aku mau ke meja perawat sebentar buat mengonfirmasi izin istirahatmu."
            miyuki "...Baik, Yuina. Terima kasih banyak ya, Chiasa-chan."
            nar "Miyuki menatap langit-langit bilik sebentar lalu memejamkan mata perlahan. Kalimat bahwa orang lain dapat menggantikannya di meja pameran tampak menakutkan sekaligus sangat menenangkan bagi bahunya yang akhirnya bisa diam."
        elif _return == "B":
            nar "Kamu berdiri diam terpaku di sisi belakang meja, hanya memandangi tubuh Miyuki yang pucat tanpa memanggil petugas ataupun berlutut memindahkan kertas-kertas yang berserakan di dekat wajahnya."
            nar "Dua detik terbuang dalam kebekuan. Baru ketika dua tamu pameran ikut berseru panik, relawan medis di meja sebelah akhirnya berlari menerobos kerumunan sambil menghubungi meja perawat."
            "Relawan Medis" "Permisi, tolong minggir sedikit! Saya sudah panggil perawat jaga, sebentar lagi mereka bawa kursi roda!"
            "Tamu Pameran" "Aduh, kasihan sekali dokternya pucat banget... tolong ambilkan air minum dulu di meja sana."
            "Relawan Medis" "Amamiya-san, tolong bantu tahan map di meja biar nggak jatuh lagi ya, saya mau longgarkan kerah Tachibana-senpai dulu!"
            nar "Kamu hanya memungut satu lembar brosur di ujung kakimu sambil terus berdiri diam. Beberapa menit kemudian, sebelum petugas medis tiba mendorong kursi roda, kelopak mata cokelat kemerahan Miyuki mengerjap lambat dengan wajah kebingungan."
            nar "Pandangannya yang masih berkabut menangkapmu berdiri diam di dekat ujung meja. Alih-alih tetap berbaring menunggu diperiksa, ia langsung menopang lantai dengan kedua telapak tangan yang gemetar dan memaksakan dirinya duduk setengah badan."
            chiasa "Tachibana-senpai baru aja pingsan. Sebaiknya jangan langsung bangun dulu."
            miyuki "Ah... aku pingsan di depan stan ya...?"
            nar "Begitu melihat kertas-kertas jadwal berserakan dan beberapa pengunjung ikut membantu memungutinya, rona malu yang perih langsung naik ke wajahnya yang pucat. Tangannya yang masih gemetar ikut menggapai brosur di lantai."
            miyuki "Aku merepotkan semua orang lagi. Maaf... maaf sekali ya, terima kasih sudah memungut kertasnya..."
            "Tamu Pameran" "Nggak apa-apa, Dok, lembar jadwalnya biar kami saja yang kumpulkan, jangan dipaksakan berdiri dulu ya!"
            "Perawat" "Tachibana-san, jangan gerak dulu, biar kami bantu naik ke kursi roda pelan-pelan. Adik yang berdiri di sebelah meja, tahu sejak jam berapa Tachibana-san berdiri tanpa makan?"
            chiasa "...Sepertinya kotak bekalnya di bawah meja memang belum sempat dibuka sejak tadi."
            miyuki "Saya baik-baik saja kok, sebentar lagi saya bisa jalan sendiri... maaf juga ya, Chiasa-chan, kamu jadi harus melihat hal memalukan begini..."
            "Perawat" "Tachibana-san, berhenti membungkuk dulu ya, sandarkan kepalamu ke belakang."
            nar "Sepanjang didorong keluar aula, Miyuki terus menunduk meminta maaf kepada tamu yang memungut brosur, kepada perawat yang mendorong kursinya, lalu sekali lagi menoleh meminta maaf kepadamu."
            "Relawan Medis" "Amamiya-san, tolong bantu rapikan brosur imunisasi yang jatuh di dekat kakimu itu ya, aku mau ambil alih antrean depan dulu..."
            chiasa "Iya... biar kurapikan di atas meja."
            chiasa "{i}Ia meminta maaf kepada semua orang berturut-turut, seolah-olah jatuh pingsan karena kelelahan itu kejahatan pribadi yang harus ditebus.{/i}"
            nar "Kamu tertinggal berdiri di belakang meja stan yang setengah kosong bersama kotak bekal yang masih tersegel rapi. Tidak ada satu orang pun yang menghentikan rentetan permintaan maafnya cukup cepat untuk membuatnya merasa bahwa jatuh sakit bisa berarti butuh istirahat."
        else:
            nar "Ketika relawan berlari mencari petugas medis dan memapah Miyuki setengah sadar ke kursi ruang tunggu sempit di samping tirai stan, kamu ikut masuk lebih dulu sebelum perawat UGD tiba."
            nar "Miyuki masih memejamkan mata sambil memegangi pelipisnya yang berdenyut, napasnya pendek dan suaranya nyaris tidak terdengar. Melihat pertahanannya yang paling rapuh terbuka tepat di hadapanmu, kamu mencondongkan badan lebih dekat."
            chiasa "Tachibana-senpai... Senpai tahu kan tadi sempat bikin satu aula panik banget, padahal aku sudah datang jauh-jauh mengantarkan poster buat Senpai?"
            nar "Bulu mata Miyuki bergetar pelan. Ia mengangkat wajahnya yang masih kabur oleh rasa pusing dengan raut bersalah yang langsung muncul."
            miyuki "Maaf, Chiasa-chan... aku memang ceroboh sekali hari ini sampai bikin kamu ikut repot dan menunggu..."
            chiasa "Kalau Senpai beneran merasa nggak enak sudah bikin aku khawatir dan menunggu begini, habis ini Senpai harus menuruti jadwalku minggu depan tanpa alasan sibuk lagi ya. Nggak usah tolak kalau aku ajak pergi, anggap saja buat menebus hari ini."
            nar "Tangan Miyuki mencengkeram ujung roknya dengan jemari dingin. Dengan gerak kaku yang gemetar, ia bahkan merogoh saku jas dokternya berusaha menarik buku saku jadwal untuk langsung menuliskan tanggal yang kamu minta semata karena takut membuatmu semakin kecewa."
            miyuki "Iya... aku nggak keberatan kok, Chiasa-chan... hari apa saja kamu butuh aku temani? Biar kucatat dulu sekarang, asalkan kamu jangan marah..."
            nar "Tepat saat pulpen itu nyaris jatuh dari jemarinya yang pucat, tirai ruang tunggu tersibak keras hingga cincin besinya berderak nyaring. Akiyama Yuina berdiri tepat di ambang tirai dengan tatapan setajam pisau di balik kacamata tipisnya."
            "Yuina" "Mundur, Amamiya Chiasa. Dia baru saja pingsan dan butuh pertolongan medis sekarang, sama sekali bukan permintaan sepihakmu."
            chiasa "Yuina-san, aku cuma lagi ngobrol sama Tachibana-senpai sambil menunggu perawat..."
            "Yuina" "Aku dengar jelas apa yang barusan kamu tagih dari depan tirai tadi. Orang baru melek dari pingsan sampai gemetar pegang buku jadwal begitu kamu tekan pakai rasa bersalah?"
            nar "Yuina langsung mengambil buku saku dari jari Miyuki yang dingin lalu menyelipkannya kembali ke saku jas dokter dengan satu gerakan tegas. Dua jarinya menyentuh pergelangan tangan Miyuki memeriksa denyut nadinya."
            "Yuina" "Nadinya makin cepat cuma karena panik takut mengecewakanmu. Kamu sadar nggak apa yang baru saja kamu lakukan?"
            miyuki "Yuina, jangan marah ke Chiasa-chan... aku beneran nggak keberatan kok, tadi salahku sendiri yang nggak kuat berdiri..."
            "Yuina" "Miyuki, diam dulu dan sandarkan kepalamu ke kursi. Kamu nggak berutang apa pun ke siapa pun hari ini, apalagi menebus rasa bersalah karena jatuh sakit."
            nar "Yuina langsung berdiri menghalangi penuh antara kursimu dan Miyuki, lalu berseru memanggil dua perawat jaga yang baru tiba membawa brankar."
            "Perawat" "Permisi, Tachibana-san kami bawa masuk ke ruang observasi sekarang ya."
            "Yuina" "Tolong langsung bawa masuk ke ruang observasi UGD. Dan maaf, Chiasa-san, mulai sekarang kamu tidak perlu ikut masuk atau tinggal berduaan dengan dia dulu. Urusan istirahatnya aku yang pegang."
            chiasa "Yuina-san..."
            "Yuina" "Sudah cukup hari ini. Aku tidak mau mendengar alasan apa pun lagi."
            chiasa "{i}Pintu kepercayaan sahabat terdekatnya baru saja ditutup rapat di depan wajahku.{/i}"
            nar "Yuina memutar tubuh mengikuti brankar Miyuki tanpa menoleh kembali kepadamu. Pintu kaca ruang observasi menutup rapat di depan matamu, mengunci rapat kepercayaan sahabat terdekat Miyuki yang baru saja kamu patahkan sendiri."
    else:
        if kk_slot >= 3:
            nar "Lampu putih aula sayap pengunjung Rumah Sakit Tachibana bersinar terang di atas deretan meja stan pameran kesehatan terbuka bulan November. Meski jam kunjungan mulai menipis, antrean terakhir keluarga pasien masih bertahan di dekat pojok konsultasi anak."
        else:
            nar "Cahaya bulan November masuk melewati jendela kaca besar aula sayap pengunjung Rumah Sakit Tachibana yang ramai oleh stan pameran kesehatan terbuka. Poster edukasi kesehatan anak berjejer di sepanjang dinding sementara antrean pengunjung bergantian mengisi kursi periksa."
        nar "Kamu datang mengantarkan salinan berkas anggaran stan gabungan kampus yang sempat diminta Fakultas Kedokteran. Begitu kamu menaruh map berkas di sudut belakang meja stan, kamu sempat melirik papan jadwal di samping kursi Miyuki yang dipenuhi dua giliran jaga tambahan bertinta merah."
        nar "Sejak kamu tiba lima belas menit lalu, Miyuki tidak pernah sekali pun duduk lebih dari satu menit di kursinya. Botol air mineralnya pun masih terisi penuh di samping kotak bekal plastik yang belum dibuka sama sekali di dekat kaki meja."
        nar "Jas dokter putihnya masih terkancing rapi dengan stetoskop menggantung di leher, rambut hitam panjang lurusnya terurai tenang di atas bahu. Namun dari samping meja, kamu melihat jelas bibirnya pucat kering dan lingkar bawah mata cokelat kemerahannya gelap sekali."
        "Relawan Medis" "Tachibana-senpai, antrean tinggal empat keluarga lagi. Senpai istirahat dulu sepuluh menit di belakang yuk, dari tadi kotak makan Senpai di bawah meja saja belum disentuh kan?"
        miyuki "Terima kasih perhatiannya, aku baik-baik saja kok. Sisa empat keluarga ini biar kubantu selesaikan dulu, ibunya yang nomor empat tadi sudah menunggu lumayan lama."
        nar "Kamu melihat tangan kirinya sempat menekan tepi meja lipat selama satu detik seolah sedang menahan pusing ringan sebelum ia segera menegakkan punggungnya lagi."
        yutaka "Tachibana-senpai, mukamu kelihatan pucat banget lho. Barusan Senpai agak limbung ya? Duduk sebentar saja dulu, biar aku bantu bagikan brosur anak-anak di depan meja."
        miyuki "Ara, cuma udara ruangan pameran agak hangat saja kok, Yutaka-kun. Terima kasih banyak ya sudah antar berkas panitianya. Sebentar saja lagi, habis menyerahkan lembar jadwal imunisasi ini aku langsung istirahat."
        yutaka "Minimal minum airnya seteguk dulu, Senpai. Botol di sebelah tasmu masih penuh dari tadi."
        miyuki "Iya, nanti langsung kuminum begitu selesai bicara dengan ibu yang ini ya."
        nar "Ia menarik senyum hangatnya kembali dan menoleh menyambut seorang ibu bersama anak kecil yang baru mendekat ke tepi meja stan. Melihat si kecil sedikit takut pada jas dokter, Miyuki langsung berjongkok sejajar tinggi anak itu dan mengeluarkan stiker beruang kecil dari saku jasnya dengan jari yang sedikit gemetar."
        miyuki "Halo, hebat sekali sudah mau ikut antre bersama Ibu. Mau tempel stiker beruang di punggung tangan dulu?"
        "Anak Kecil" "Mau! Beruangnya lucu!"
        "Tamu Pameran" "Permisi, Dokter, terima kasih banyak tadi anak saya mau diperiksa tanpa menangis. Boleh tanya sedikit soal catatan demam yang tadi dijelaskan di papan?"
        miyuki "Tentu, silakan tunggu sebentar ya, saya ambilkan lembar contohnya di ujung meja..."
        nar "Miyuki berputar setengah langkah sambil menjangkau map plastik tebal. Tepat saat ujung jemarinya menyentuh map itu, kedua bahunya mendadak bergetar tipis dan tatapan mata cokelat kemerahannya kehilangan titik fokus."
        nar "Ia masih berusaha meminta tamu pameran menunggu sebentar dengan suara pelan yang terputus di tengah kata ketika kedua lututnya tiba-tiba kehilangan tenaga."
        miyuki "Maaf... sebentar..."
        nar "Map plastik terlepas begitu saja dari tangannya. Lembaran brosur, lembar stiker, dan kertas jadwal meluncur jauh menyebar di atas lantai vinil, sementara tubuh Miyuki merosot jatuh miring di belakang meja stan."
        "Tamu Pameran" "Eh?! Dokternya jatuh! Tolong, ada yang pingsan di sini!"
        "Relawan Medis" "Tachibana-senpai! Senpai, dengar suaraku nggak?!"
        "Anak Kecil" "Ibu, dokternya tidur di lantai?"
        nar "Suara keramaian aula mendadak terasa jauh dan gaduh bersamaan. Kamu berdiri paling dekat di sisi belakang meja ketika nama Miyuki dipanggil berulang kali tanpa satu pun jawaban keluar dari bibirnya yang pucat."
        yutaka "{i}Badannya benar-benar sudah habis tenaganya dari tadi... dan sekarang ia tergeletak tepat di depan kakiku.{/i}"
        call kk_family_menu("Mi17", ["Panggil petugas dan bawa ia ke UGD segera.", "Diam di tempat dan tunggu ia sadar sendiri.", "Manfaatkan keadaannya yang lemah untuk menuntut sesuatu darinya."])
        if _return == "A":
            nar "Kamu langsung berlutut di samping Miyuki, menahan kepala dan bahunya agar tidak terbentur kaki meja besi, lalu menoleh cepat ke arah relawan yang masih terpaku kaget."
            yutaka "Tolong cepat panggil perawat UGD dan minta brankar sekarang juga! Jangan dikerumuni dulu biar udaranya kebuka!"
            "Relawan Medis" "B-baik! Aku langsung lari ke meja perawat pintu sebelah!"
            yutaka "Tachibana-senpai, tenang ya, petugasnya sebentar lagi datang."
            nar "Kamu melonggarkan kancing teratas jas dokternya perlahan agar napasnya lebih lega, memungut cepat map dan lembar stikernya ke dalam tasmu, lalu membantu perawat jaga memindahkannya ke brankar dorong menyusuri koridor sampai ke bilik pemeriksaan UGD."
            "Perawat UGD" "Tekanan darahnya agak rendah dan kadar gulanya turun, kemungkinan besar kelelahan ekstrem plus telat makan. Saya pasang infus cairan dulu ya, tolong tunggu sebentar."
            yutaka "Baik, terima kasih banyak."
            nar "Dua puluh menit kemudian, ketika cairan infus sudah menetes teratur di punggung tangan Miyuki dan kelopak mata cokelat kemerahannya baru mulai terbuka sayu, tirai putih bilik tersibak cepat."
            nar "Akiyama Yuina masuk dengan napas sedikit terengah, jas lab penuh pin dan kacamata bingkai tipisnya agak miring karena baru turun berlari dari ruang jaga atas. Ia langsung mengecek papan tensi di samping ranjang."
            "Yuina" "Tekanan darahnya turun, dehidrasi, kurang tidur beruntun... astaga, Miyuki, kamu beneran nekat sampai tumbang di depan stan sendiri."
            yutaka "Kotak makannya di bawah meja stan tadi memang masih utuh belum dibuka sama sekali, Yuina-san."
            "Yuina" "Sudah kuduga. Tiap sibuk jaga dia selalu lupa tubuhnya sendiri."
            miyuki "Yuina... maaf ya... pamerannya di depan tadi belum selesai, ibu yang mengantre nomor empat tadi masih menunggu lembaran... sama stiker beruangku tadi jatuh semua di lantai ya?"
            yutaka "Lembar brosur sama stikernya sudah kurapikan semua di tasku, Tachibana-senpai. Nggak ada yang hilang."
            "Yuina" "Dan ada orang lain di sana, Miyuki. Relawan sama dokter jaga sudah ambil alih meja stan sejak lima menit lalu. Sekarang kamu di sini dulu, diam di atas ranjang."
            nar "Yuina menoleh kepadamu dengan hembusan napas lega yang jujur, bahunya yang sejak tadi tegang akhirnya sedikit turun."
            "Yuina" "Makasih sudah cepat bawa dia masuk UGD, Kisaragi-kun. Aku akan bantu bereskan urusan jadwalnya sama dokter pembimbing hari ini. Tolong banget, jangan biarkan dia mengira harus langsung balik kerja begitu dia bilang sudah enakan."
            yutaka "Iya, Yuina-san. Kalau dia coba bangun lagi sebelum infusnya habis, aku langsung kabari Yuina-san."
            miyuki "Yutaka-kun juga... kamu jadi ketinggalan rapat panitia di kampus gara-gara mengurusku di sini ya? Maaf sekali sudah bikin kamu kaget dan repot..."
            yutaka "Nggak usah memikirkan urusan panitia dulu, Tachibana-senpai. Berkasnya sudah aman di loker. Tugas Senpai hari ini cuma tidur dan membiarkan orang lain mengurus sisanya."
            "Yuina" "Dengar tuh kata Kisaragi-kun. Minum air hangatnya sedikit, lalu pejamkan mata. Aku mau ke meja perawat sebentar buat mengonfirmasi izin istirahatmu."
            miyuki "...Baik, Yuina. Terima kasih banyak ya, Yutaka-kun."
            nar "Miyuki menatap langit-langit bilik sebentar lalu memejamkan mata perlahan. Kalimat bahwa orang lain dapat menggantikannya di meja pameran tampak menakutkan sekaligus sangat menenangkan bagi bahunya yang akhirnya bisa diam."
        elif _return == "B":
            nar "Kamu berdiri diam terpaku di sisi belakang meja, hanya memandangi tubuh Miyuki yang pucat tanpa memanggil petugas ataupun berlutut memindahkan kertas-kertas yang berserakan di dekat wajahnya."
            nar "Dua detik terbuang dalam kebekuan. Baru ketika dua tamu pameran ikut berseru panik, relawan medis di meja sebelah akhirnya berlari menerobos kerumunan sambil menghubungi meja perawat."
            "Relawan Medis" "Permisi, tolong minggir sedikit! Saya sudah panggil perawat jaga, sebentar lagi mereka bawa kursi roda!"
            "Tamu Pameran" "Aduh, kasihan sekali dokternya pucat banget... tolong ambilkan air minum dulu di meja sana."
            "Relawan Medis" "Kisaragi-senpai, tolong bantu tahan map di meja biar nggak jatuh lagi ya, saya mau longgarkan kerah Tachibana-senpai dulu!"
            nar "Kamu hanya memungut satu lembar brosur di ujung kakimu sambil terus berdiri diam. Beberapa menit kemudian, sebelum petugas medis tiba mendorong kursi roda, kelopak mata cokelat kemerahan Miyuki mengerjap lambat dengan wajah kebingungan."
            nar "Pandangannya yang masih berkabut menangkapmu berdiri diam di dekat ujung meja. Alih-alih tetap berbaring menunggu diperiksa, ia langsung menopang lantai dengan kedua telapak tangan yang gemetar dan memaksakan dirinya duduk setengah badan."
            yutaka "Tachibana-senpai baru saja pingsan. Sebaiknya jangan langsung bangun dulu."
            miyuki "Ah... aku pingsan di depan stan ya...?"
            nar "Begitu melihat kertas-kertas jadwal berserakan dan beberapa pengunjung ikut membantu memungutinya, rona malu yang perih langsung naik ke wajahnya yang pucat. Tangannya yang masih gemetar ikut menggapai brosur di lantai."
            miyuki "Aku merepotkan semua orang lagi. Maaf... maaf sekali ya, terima kasih sudah memungut kertasnya..."
            "Tamu Pameran" "Nggak apa-apa, Dok, lembar jadwalnya biar kami saja yang kumpulkan, jangan dipaksakan berdiri dulu ya!"
            "Perawat" "Tachibana-san, jangan gerak dulu, biar kami bantu naik ke kursi roda pelan-pelan. Mahasiswa yang berdiri di sebelah meja, tahu sejak jam berapa Tachibana-san berdiri tanpa makan?"
            yutaka "...Sepertinya kotak bekalnya di bawah meja memang belum sempat dibuka sejak tadi."
            miyuki "Saya baik-baik saja kok, sebentar lagi saya bisa jalan sendiri... maaf juga ya, Yutaka-kun, kamu jadi harus melihat hal memalukan begini..."
            "Perawat" "Tachibana-san, berhenti membungkuk dulu ya, sandarkan kepalamu ke belakang."
            nar "Sepanjang didorong keluar aula, Miyuki terus menunduk meminta maaf kepada tamu yang memungut brosur, kepada perawat yang mendorong kursinya, lalu sekali lagi menoleh meminta maaf kepadamu."
            "Relawan Medis" "Kisaragi-senpai, tolong bantu rapikan brosur imunisasi yang jatuh di dekat kakimu itu ya, aku mau ambil alih antrean depan dulu..."
            yutaka "Iya... biar kurapikan di atas meja."
            yutaka "{i}Ia meminta maaf kepada semua orang berturut-turut, seolah-olah jatuh pingsan karena kelelahan itu kejahatan pribadi yang harus ditebus.{/i}"
            nar "Kamu tertinggal berdiri di belakang meja stan yang setengah kosong bersama kotak bekal yang masih tersegel rapi. Tidak ada satu orang pun yang menghentikan rentetan permintaan maafnya cukup cepat untuk membuatnya merasa bahwa jatuh sakit bisa berarti butuh istirahat."
        else:
            nar "Ketika relawan berlari mencari petugas medis dan memapah Miyuki setengah sadar ke kursi ruang tunggu sempit di samping tirai stan, kamu ikut masuk lebih dulu sebelum perawat UGD tiba."
            nar "Miyuki masih memejamkan mata sambil memegangi pelipisnya yang berdenyut, napasnya pendek dan suaranya nyaris tidak terdengar. Melihat pertahanannya yang paling rapuh terbuka tepat di hadapanmu, kamu mencondongkan badan lebih dekat."
            yutaka "Tachibana-senpai... Senpai tahu kan tadi sempat bikin satu aula panik banget, padahal aku sudah datang jauh-jauh mengantarkan berkas panitia buat Senpai?"
            nar "Bulu mata Miyuki bergetar pelan. Ia mengangkat wajahnya yang masih kabur oleh rasa pusing dengan raut bersalah yang langsung muncul."
            miyuki "Maaf, Yutaka-kun... aku memang ceroboh sekali hari ini sampai bikin kamu ikut repot dan menunggu..."
            yutaka "Kalau Senpai beneran merasa nggak enak sudah bikin aku khawatir dan menunggu begini, habis ini Senpai harus menuruti jadwalku minggu depan tanpa alasan sibuk lagi ya. Nggak usah tolak kalau aku ajak pergi, anggap saja buat menebus hari ini."
            nar "Tangan Miyuki mencengkeram ujung roknya dengan jemari dingin. Dengan gerak kaku yang gemetar, ia bahkan merogoh saku jas dokternya berusaha menarik buku saku jadwal untuk langsung menuliskan tanggal yang kamu minta semata karena takut membuatmu semakin kecewa."
            miyuki "Iya... aku nggak keberatan kok, Yutaka-kun... hari apa saja kamu butuh aku temani? Biar kucatat dulu sekarang, asalkan kamu jangan marah..."
            nar "Tepat saat pulpen itu nyaris jatuh dari jemarinya yang pucat, tirai ruang tunggu tersibak keras hingga cincin besinya berderak nyaring. Akiyama Yuina berdiri tepat di ambang tirai dengan tatapan setajam pisau di balik kacamata tipisnya."
            "Yuina" "Mundur, Kisaragi Yutaka. Dia baru saja pingsan dan butuh pertolongan medis sekarang, sama sekali bukan permintaan sepihakmu."
            yutaka "Yuina-san, aku cuma lagi ngobrol sama Tachibana-senpai sambil menunggu perawat..."
            "Yuina" "Aku dengar jelas apa yang barusan kamu tagih dari depan tirai tadi. Orang baru melek dari pingsan sampai gemetar pegang buku jadwal begitu kamu tekan pakai rasa bersalah?"
            nar "Yuina langsung mengambil buku saku dari jari Miyuki yang dingin lalu menyelipkannya kembali ke saku jas dokter dengan satu gerakan tegas. Dua jarinya menyentuh pergelangan tangan Miyuki memeriksa denyut nadinya."
            "Yuina" "Nadinya makin cepat cuma karena panik takut mengecewakanmu. Kamu sadar nggak apa yang baru saja kamu lakukan?"
            miyuki "Yuina, jangan marah ke Yutaka-kun... aku beneran nggak keberatan kok, tadi salahku sendiri yang nggak kuat berdiri..."
            "Yuina" "Miyuki, diam dulu dan sandarkan kepalamu ke kursi. Kamu nggak berutang apa pun ke siapa pun hari ini, apalagi menebus rasa bersalah karena jatuh sakit."
            nar "Yuina langsung berdiri menghalangi penuh antara kursimu dan Miyuki, lalu berseru memanggil dua perawat jaga yang baru tiba membawa brankar."
            "Perawat" "Permisi, Tachibana-san kami bawa masuk ke ruang observasi sekarang ya."
            "Yuina" "Tolong langsung bawa masuk ke ruang observasi UGD. Dan maaf, Kisaragi-kun, mulai sekarang kamu tidak perlu ikut masuk atau tinggal berduaan dengan dia dulu. Urusan istirahatnya aku yang pegang."
            yutaka "Yuina-san..."
            "Yuina" "Sudah cukup hari ini. Aku tidak mau mendengar alasan apa pun lagi."
            yutaka "{i}Pintu kepercayaan sahabat terdekatnya baru saja ditutup rapat di depan wajahku.{/i}"
            nar "Yuina memutar tubuh mengikuti brankar Miyuki tanpa menoleh kembali kepadamu. Pintu kaca ruang observasi menutup rapat di depan matamu, mengunci rapat kepercayaan sahabat terdekat Miyuki yang baru saja kamu patahkan sendiri."
    return

# ┌─ PANDUAN CERITA · Mi19 · Valentine Dingin
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : ia memberi coklat tanpa senyum.
# │ INTI    : A terima / B kembalikan / C tanyakan.
# │ AKHIRAN : pola menguat.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi19:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana · Valentine")
    nar "Kotak coklat itu dibungkus sempurna. Miyuki menyerahkannya di koridor rumah sakit, menyebut kapan sebaiknya dimakan dan bagaimana menyimpannya, lalu berdiri menunggu penilaian."
    miyuki "Aku membuatnya tadi malam. Kalau kurang manis, bilang. Aku masih punya bahan."
    nar "Tidak ada nada jahil atau kebanggaan kecil yang biasa mengikuti hasil dapurnya. Ia terdengar seperti sedang menyerahkan tugas yang harus diperiksa."
    call kk_family_menu("Mi19", ["Terima apa adanya.", "Kembalikan dan minta ia memberinya dengan tulus.", "Tanyakan kenapa ia tak tersenyum."])
    if _return == "A":
        nar "Kau menerima kotak itu dan mengucapkan terima kasih. Miyuki mengangguk, lega karena tidak perlu membuatnya ulang."
        miyuki "Sudah cukup? Baik. Aku senang kalau kamu nggak kecewa."
        nar "Ia baru menyadari pilihan katanya setelah mengucapkannya. Namun ketika dipanggil kembali ke dalam, ia segera pergi, meninggalkan rasa getir yang tidak berasal dari coklat."
    elif _return == "B":
        nar "Kau mengembalikan kotaknya dan mengatakan tidak ingin ia memberimu sesuatu sebagai pembayaran agar tetap disukai. Miyuki menatap pita yang sudah begitu hati-hati dibuatnya."
        miyuki "Aku tadi mengira kamu minta kubuat lebih bagus. Ternyata kamu bertanya aku ingin memberi atau nggak."
        nar "Ia menarik kotak itu ke dada."
        miyuki "Boleh kusimpan dulu? Aku ingin tahu jawabannya sebelum memberimu lagi."
    else:
        nar "Kau menanyakan keadaannya, bukan meminta ia tersenyum untukmu. Miyuki sempat mengatakan baik-baik saja, lalu berhenti di tengah kalimat."
        miyuki "Aku bangun tadi dan yang kupikirkan cuma jangan lupa. Bukan siapa yang ingin kubuat senang."
        nar "Kotak itu terasa berat di tanganmu. Ia meminta duduk sebentar sebelum kembali ke bangsal, dan kali ini membiarkanmu melihat bahwa ia belum punya jawaban."
    return

# ┌─ PANDUAN CERITA · Mi20 · Audit Pribadi
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : ia mengevaluasi hidupnya.
# │ INTI    : A dukung / B abaikan / C bawa ke Sato.
# │ AKHIRAN : titik pemulihan terakhir sebelum Tahun 3.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi20:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana · Audit pribadi")
    nar "Miyuki membuat dua daftar. Yang pertama berjudul harus. Yang kedua hanya punya satu baris, ditulis lalu dicoret hingga sulit dibaca."
    miyuki "Aku mencoba menulis yang kuinginkan. Setiap kali muncul sesuatu, aku langsung teringat siapa yang akan kecewa."
    nar "Ia menunjuk pediatri sebagai satu hal yang masih terasa miliknya, kemudian menutup bagian keluarga dengan telapak tangan."
    miyuki "Kalau baru sekarang bertanya tentang hidupku sendiri, apa sudah terlalu terlambat?"
    call kk_family_menu("Mi20", ["Dukung ia mengambil kembali pilihannya.", "Abaikan; biarkan ia memutuskan sendiri.", "Bawa ia ke Sato Kyoko untuk membicarakannya."])
    if _return == "A":
        nar "Kau mendukungnya tanpa mengisi daftar kosong itu dengan keinginanmu. Miyuki menunggu saran, lalu menyadari kau sedang membiarkan ia sendiri yang menulis."
        miyuki "Aku ingin satu malam tanpa menjawab telepon keluarga. Aku ingin tidur sebelum merasa pantas tidur."
        nar "Dua kalimat masuk ke daftar. Tidak mengubah seluruh hidupnya, tetapi keduanya tidak dicoret."
    elif _return == "B":
        nar "Kau mengatakan keputusan itu miliknya, lalu membiarkan pembicaraan berhenti tanpa menanyakan bantuan apa yang diperlukan. Miyuki mengangguk seperti menerima pekerjaan tambahan."
        miyuki "Iya. Aku harus bisa memutuskan sendiri."
        nar "Ia menutup daftar kedua dan kembali memeriksa jadwal. Ketidakmampuannya memilih kini terasa seperti kekurangan baru yang juga harus ia tanggung sendirian."
    else:
        nar "Kau menawarkan membicarakannya dengan Sato. Miyuki membawa kedua daftar itu ke pertemuan, bahkan bagian yang menurutnya memalukan."
        "Sato Kyoko" "Kita bisa mulai dari apa yang terjadi saat kamu hendak mencoret sebuah keinginan. Tidak perlu memutuskan seluruh masa depan hari ini."
        nar "Miyuki menarik tangannya dari daftar yang ditutupi. Untuk sekali ini bagian yang sulit tidak harus dirapikan sebelum boleh dilihat seseorang."
    return

# ┌─ PANDUAN CERITA · Mi22 · Pola Menetap
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : stage 5: dinamika dominasi–penyerahan emosional (tersirat).
# │ INTI    : A lanjutkan / B hentikan / C bawa ke Yuina/Sato.
# │ AKHIRAN : A bisa membuat pola permanen setelah 1 semester; C membuka pemulihan sebagian.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi22:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana · Pola yang menetap")
    nar "Miyuki meminta izin sebelum memilih minumannya sendiri. Ia mengatakannya begitu biasa hingga penjaga kantin menjawab lebih dahulu, mengira pertanyaan itu untuknya."
    miyuki "Aku cuma ingin memastikan kamu nggak keberatan. Kalau kamu memilihkan, aku lebih tenang."
    nar "Pola itu kini hidup di dalam hal-hal kecil. Ia menunggu arahan, kau terbiasa memberi, dan kata nyaman mulai dipakai setiap kali seseorang bertanya apakah ia masih punya keinginan sendiri."
    call kk_family_menu("Mi22", ["Lanjutkan pola ini.", "Hentikan sebelum menetap.", "Bawa ia ke Yuina atau Sato Kyoko."])
    if _return == "A":
        nar "Kau memilihkan dan menerima kelegaan di wajahnya sebagai pembenaran. Miyuki menyimpan pilihan yang berbeda sebelum sempat mengucapkannya."
        miyuki "Begini lebih mudah. Aku nggak perlu takut salah."
        nar "Semester itu berlalu dengan semakin sedikit perbedaan yang terlihat. Ia menjadi sangat pandai memperkirakan kehendakmu; orang lain menyebutnya pengertian. Dirinya sendiri makin sulit ditemukan di antara tebakan-tebakan tersebut."
    elif _return == "B":
        nar "Kau menolak meneruskan kebiasaan itu dan mengatakan ia tidak perlu membuat pilihan yang menyenangkanmu. Miyuki justru tampak ketakutan."
        miyuki "Kalau aku nggak tahu apa yang kumau hari ini, kamu tetap mau duduk denganku?"
        nar "Kau tetap di tempat. Ia memilih minuman setelah cukup lama, lalu mengubah pesanannya satu kali tanpa meminta maaf. Gerakan kecil itu belum pemulihan penuh, tetapi pola yang lama akhirnya bertemu gangguan."
    else:
        nar "Kau mengusulkan bantuan di luar hubungan kalian. Yuina mendengarkan sebelum mengatakan bahwa keduanya memerlukan jarak untuk melihat kebiasaan yang telah terasa terlalu biasa."
        "Yuina" "Aku bisa menemani Miyuki menghubungi Sato. Kamu perlu memberi ruang, termasuk saat itu membuatmu nggak nyaman."
        nar "Miyuki menanyakan siapa yang akan menentukan pertemuan. Yuina menjawab bahwa ia sendiri boleh ikut menentukannya. Pertanyaan berikutnya datang lebih lambat, tetapi mulai terdengar seperti keinginan."
    return

# ┌─ PANDUAN CERITA · Mi23 · Yukata Tanpa Senyum
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : ia hadir tanpa ekspresi.
# │ INTI    : A hibur / B manfaatkan / C tinggalkan.
# │ AKHIRAN : Yuina memutus hubungan jika pemain memanfaatkan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi23:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana · Yukata tanpa senyum")
    nar "Yuina menemani Miyuki keluar setelah jadwal terakhir agar ia sempat pergi ke festival. Yukatanya indah, tetapi ia menatap lampion seperti orang yang sedang mencoba mengingat alasan datang."
    miyuki "Aku sudah berganti pakaian. Harusnya habis ini rasanya berbeda, ya."
    nar "Ia menyadari wajahmu, lalu cepat-cepat meminta maaf karena tidak tampak senang. Bahkan malam libur hampir berubah menjadi ujian lain yang harus ia luluskan."
    call kk_family_menu("Mi23", ["Hibur dan temani ia malam itu.", "Manfaatkan keadaannya.", "Tinggalkan ia sendiri."])
    if _return == "A":
        nar "Kau mengatakan ia tidak harus menikmati seluruh festival agar boleh berada di sana. Kalian memilih tempat duduk yang jauh dari pengeras suara."
        miyuki "Aku boleh bilang mau pulang nanti? Meski baru sebentar?"
        nar "Kau menyetujuinya. Justru setelah mendapat jalan untuk pergi, ia sanggup memperhatikan warna lampion dan mulai bercerita tentang yukata yang dipinjamkan Yuina."
    elif _return == "B":
        nar "Kau memperlakukan kepatuhannya sebagai kesempatan menekan, membiarkan ia membayar suasana hatimu dengan tenaganya yang hampir habis. Yuina kembali sebelum percakapan selesai."
        "Yuina" "Miyuki, ikut aku dulu. Kamu nggak berutang malam yang menyenangkan kepada siapa pun."
        nar "Sesudah mendengar apa yang terjadi, Yuina menutup jalanmu untuk mendekat melalui dirinya. Senyum sopan yang selama ini ia berikan kepadamu tidak muncul lagi."
    else:
        nar "Kau pergi setelah mengatakan ada urusan. Miyuki mengangguk dan melambaikan tangan, berusaha membuat perpisahan itu semudah mungkin untukmu."
        nar "Ia tetap duduk dengan yukata rapi, memandang orang lewat. Ketika Yuina menemuinya lagi, ia berkata belum lama menunggu, padahal minuman di tangannya sudah hangat."
        miyuki "Aku mungkin memang belum cocok pergi bersenang-senang."
    return

# ┌─ PANDUAN CERITA · Mi26 · Ujian Akhir dan Yuina
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : Yuina berdiri di sisi pemain atau melawan.
# │ INTI    : A minta bantuan Yuina / B hindari / C konfrontasi.
# │ AKHIRAN : aliansi.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi26:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana · Ujian akhir")
    nar "Yuina membawa salinan jadwal akhir dan daftar barang yang sering dilupakan Miyuki ketika gugup. Ia berhenti berbicara begitu melihatmu di koridor."
    "Yuina" "Aku mau memastikan dia punya waktu makan dan tidur. Kalau kamu datang untuk menambah sesuatu yang harus ia tanggung, sekarang bukan waktunya."
    nar "Miyuki berada beberapa langkah di belakangnya, cukup dekat untuk mendengar. Ia tidak boleh lagi dijadikan alasan oleh dua orang yang saling berebut hak paling memahami."
    call kk_family_menu("Mi26", ["Minta bantuan Yuina.", "Hindari Yuina.", "Konfrontasi Yuina."])
    if _return == "A":
        nar "Kau meminta bantuan dengan tugas yang jelas, bukan meminta Yuina menjamin bahwa kehadiranmu baik untuk Miyuki. Ia memeriksa apakah Miyuki menginginkan rencana itu."
        miyuki "Aku mau. Asal kalau aku bilang cukup, kita berhenti."
        "Yuina" "Baik. Kita bantu sesuai itu. Demi dia."
        nar "Kerja sama kalian dimulai dari persetujuan Miyuki, tanpa perlu menghapus apa yang Yuina ingat tentangmu."
    elif _return == "B":
        nar "Kau memilih menghindari Yuina. Ia tidak mengejar, kembali menyerahkan jadwal kepada Miyuki dan membicarakan hal-hal yang tetap perlu diselesaikan."
        nar "Kau kehilangan kesempatan mengetahui bagian yang tak pernah Miyuki ceritakan kepadamu. Persiapan itu berjalan juga, dengan pintu yang kini harus diketuk melalui Miyuki sendiri."
    else:
        nar "Kau mempertanyakan hak Yuina menghalangi. Ia mendengarkan tanpa mundur, lalu menoleh ketika Miyuki hendak meminta maaf untuk kalian berdua."
        "Yuina" "Bukan salahmu. Jangan ambil ini juga."
        nar "Barulah ia menjawabmu."
        "Yuina" "Aku akan berdiri di pihak yang membuat dia lebih aman, termasuk kalau itu membuatmu marah. Kamu baru saja menunjukkan kenapa aku perlu tegas."
    return

init 1 python:
    _hook("Mi14-A", lambda: (kk_rel("miyuki","trust",5), kk_miyuki_stage(2)))
    _hook("Mi14-B", lambda: (kk_rel("miyuki","aff",4), kk_miyuki_stage(2)))
    _hook("Mi14-C", lambda: (kk_miyuki_hurt_self(8), kk_miyuki_stage(2)))
    _hook("Mi15-A", lambda: kk_rel("miyuki","trust",4))
    _hook("Mi15-B", lambda: kk_miyuki_stage(3))
    _hook("Mi15-C", lambda: (kk_miyuki_hurt_self(10), kk_miyuki_stage(3), kk_flag("miyuki_rasa_salah_dimanfaatkan")))
    _hook("Mi16-A", lambda: kk_rel("miyuki","trust",4))
    _hook("Mi16-B", lambda: kk_rel("miyuki","aff",-3))
    _hook("Mi16-C", lambda: (kk_miyuki_hurt_self(12), kk_miyuki_stage(4), kk_flag("rute_masokis_miyuki")))
    _hook("Mi16-D", lambda: (kk_miyuki_hurt_self(-10), kk_flag("miyuki_sato_dikenal")))
    _hook("Mi17-A", lambda: (kk_rel("miyuki","trust",5), kk_adj("kelelahan_miyuki",-20)))
    _hook("Mi17-B", lambda: kk_miyuki_hurt_self(6))
    _hook("Mi17-C", lambda: (kk_miyuki_hurt_self(10), kk_flag("sena_memutus")))
    _hook("Mi19-A", lambda: kk_flag("miyuki_pola_valentine"))
    _hook("Mi19-B", lambda: kk_rel("miyuki","aff",3))
    _hook("Mi19-C", lambda: kk_rel("miyuki","trust",4))
    _hook("Mi20-A", lambda: (kk_rel("miyuki","trust",6), kk_flag("miyuki_ambil_pilihan")))
    _hook("Mi20-C", lambda: (kk_miyuki_hurt_self(-8), kk_flag("miyuki_sato_dikenal")))
    _hook("Mi22-A", lambda: (kk_miyuki_stage(5), kk_flag("pola_masokis_permanen")))
    _hook("Mi22-B", lambda: (kk_miyuki_hurt_self(-12), kk_flag("pola_dihentikan")))
    _hook("Mi22-C", lambda: (kk_miyuki_hurt_self(-10), kk_flag("miyuki_sato_dikenal")))
    _hook("Mi23-A", lambda: kk_rel("miyuki","intim",5))
    _hook("Mi23-B", lambda: (kk_miyuki_hurt_self(12), kk_flag("sena_memutus")))
    _hook("Mi23-C", lambda: kk_rel("miyuki","trust",-5))
    _hook("Mi26-A", lambda: kk_flag("sena_sekutu"))
    _hook("Mi26-B", lambda: kk_rel("miyuki","trust",-2))
    _hook("Mi26-C", lambda: kk_flag("sena_lawan"))
