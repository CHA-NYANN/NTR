# Kouseikan — adegan naratif untuk event yang benar-benar dimainkan (vertical slice).
# Rangkuman cerita yang mengalir + pilihan yang muncul dari adegan, BUKAN poin desain
# atau menu nada abstrak. Pilihan tidak mengungkap ke mana arahnya.
#
# Event lain (yang hanya muncul di Alat Uji) tetap pakai pemutar generik kk_event.

# Dispatcher: pakai adegan tulisan tangan bila ada; kalau tidak, pemutar generik ringkas.
label kk_play_scene(evid):
    if kk_done(evid):
        return
    if renpy.has_label("kkscene_" + evid):
        call expression ("kkscene_" + evid)
    else:
        call kk_event(evid, reveal=False)
    return

# ── N01 · Tabrakan di Koridor (Nagisa, Gedung Arsitektur) ──
# ┌─ PANDUAN CERITA · N01 · Tabrakan di Koridor
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : tumbukan di fakultas arsitektur; ia menantang main game.
# │ INTI    : A terima / B tolak / C goda.
# │ AKHIRAN : A membuka rivalitas ringan. (Female: risiko "Nacchan-oneechan".)
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N01:
    call kk_scene_enter("nagisa", "Gedung Arsitektur")
    nar "Sudut map menghantam bahumu sebelum pemiliknya terlihat. Gulungan gambar jatuh, disusul penggaris dan konsol kecil yang segera diselamatkan Nagisa dengan gerakan jauh lebih cepat daripada caranya menangkap tugas sendiri."
    nagisa "Lihat jalan kalau lewat! ...Aku juga? Iya, tapi aku sudah mau berhenti."
    nar "Ia berjongkok mengambil gambar sambil memeriksa layar. Tulisan kalah masih menyala ketika ia buru-buru mematikannya."
    nagisa "Tadi cuma koneksinya jelek. Kalau kamu mau komentar, lawan aku dulu."
    call kk_family_menu("N01", ["Angkat maketnya, lalu balas tantangannya.", "Minta maaf singkat, kau sedang buru-buru.", "Goda dia soal game yang lebih penting dari tabrakan."])
    if _return == "A":
        nar "Kau membantunya merapikan barang dan menerima tantangan. Nagisa menyebut jam dan tempat dengan semangat yang tidak cocok untuk orang yang baru saja mengomel."
        nagisa "Jangan kabur setelah bikin janji. Dan jangan bilang mengalah supaya aku senang. Itu lebih menyebalkan."
        nar "Ia mengambil gulungan terakhir dari tanganmu, kali ini mengucapkan terima kasih cukup jelas untuk didengar."
    elif _return == "B":
        nar "Kau meminta maaf dan menyerahkan barang yang paling dekat sebelum pamit. Nagisa hendak melanjutkan keluhan, lalu melihat wajahmu yang memang sedang buru-buru."
        nagisa "Ya sudah. Jalan hati-hati. Kalau nabrak orang lagi, nanti bilang koridor ini yang salah."
        nar "Ia menepi agar kau bisa lewat. Ketika menoleh, kau melihat ia memeriksa gulunganmu juga, memastikan tak ada barangmu yang ikut tertinggal."
    else:
        nar "Kau menyebut betapa cepat ia menyelamatkan konsol dibanding tugas. Nagisa memerah, mendekap layar yang sudah gelap."
        nagisa "Yang ini jatuh bisa rusak! Gambar bisa... ya, gambar juga bisa rusak. Sudah, jangan bantu argumenmu sendiri."
        nar "Ia tertawa setengah marah. Tantangan bertanding diulang sebelum kalian berpisah, kini terasa seperti alasan untuk bertemu lagi."
    return

# ── Mi01 · Bento Hanami (Miyuki, Taman Kampus) ──
# ┌─ PANDUAN CERITA · Mi01 · Bento Hanami
# │ LOKASI  : Kampus Kouseikan · Taman Kampus
# │ TERLIBAT: (saat masuk) (+ Koita bila relevan)
# │ AWALAN  : Miyuki membawa bento besar.
# │ INTI    : A puji / B bantu bawa / C abaikan.
# │ AKHIRAN : A/B membuka akses sisi hangat.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi01:
    call kk_scene_enter("miyuki", "Taman Kampus")
    nar "Kelopak sakura mendarat di tutup bento sebelum Tachibana Miyuki sempat meletakkannya. Ia meniupnya pergi dengan wajah begitu serius sampai orang di sebelah tertawa. Setelah itu barulah ia ikut tersenyum."
    miyuki "Aku membuat terlalu banyak. Kalimat itu mulai terdengar seperti kebiasaan buruk, ya. Kalau belum makan, silakan."
    nar "Bento bertingkatnya berisi makanan yang disusun untuk mudah dibagikan. Miyuki, senpai kedokteran tahun ketiga, sudah menyiapkan sumpit tambahan sebelum tahu siapa yang akan duduk."
    miyuki "Yang pedas di sebelah sini. Jangan sampai senpai merusak hari pertamamu karena salah sambal."
    call kk_family_menu("Mi01", ["Puji masakannya dengan tulus.", "Bantu ia membawakan kotaknya yang berat.", "Permisi, kau ada urusan lain."])
    if _return == "A":
        nar "Kau menyebut bagian yang kausukai dengan jelas, bukan sekadar mengatakan enak. Miyuki menanyakan sekali lagi seolah ingin memastikan kau tidak sedang sopan."
        miyuki "Itu yang paling lama kubuat. Aku senang kamu menyadarinya."
        nar "Ia menyendokkan sedikit lagi, lalu teringat belum mengambil bagiannya sendiri. Untuk sesaat senyumnya tampak lebih muda daripada cara ia memperkenalkan diri tadi."
    elif _return == "B":
        nar "Ketika ia hendak memindahkan kotak, kau menawarkan mengangkat bagian terbawah. Miyuki hampir menolak otomatis, lalu menimbang beratnya dan menyerahkannya."
        miyuki "Terima kasih. Aku selalu yakin bisa membawa semuanya sampai sudah terlanjur pegal."
        nar "Kalian mengatur tempat bersama. Ia tidak lagi sendirian mengawasi agar semua orang kebagian, dan akhirnya sempat menikmati satu gigitan sebelum makanan dingin."
    else:
        nar "Kau menjelaskan ada urusan dan pamit. Miyuki mengangguk segera, menggeser kotak agar jalanmu lapang."
        miyuki "Tentu. Hati-hati, ya. Kalau nanti sempat, masih boleh mampir."
        nar "Kau meninggalkannya menawarkan porsi kepada orang berikutnya. Tangannya tetap cekatan, tetapi ada jeda kecil sebelum senyumnya kembali siap."
    return

# ── N03 · Maket Hujan (Nagisa, Gedung Arsitektur, M03) ──
# ┌─ PANDUAN CERITA · N03 · Maket Hujan
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : maket rusak karena hujan.
# │ INTI    : A bantu semalaman / B belikan baru / C tertawakan.
# │ AKHIRAN : stage 1 (rasa terima kasih) pada A.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N03:
    call kk_scene_enter("nagisa", "Gedung Arsitektur")
    nar "Hujan menerobos jendela studio yang lupa ditutup. Maket tugas akhir Nagisa—kerja berminggu-minggu—basah dan melengkung di satu sudut. Ia berdiri mematung, rahang mengeras, menolak menangis di depan siapa pun."
    if any(c["ev"] == "N01" and c["key"] == "A" for c in choices_log):
        nagisa "Kalau mau tanding lagi, kau harus tunggu. Lihat sendiri maketku."
    nagisa "...Tidak apa-apa. Masih bisa. Aku tinggal mengulang bagian ini. Semalaman. Lagi."
    call kk_family_menu("N03", ["Tinggal, bantu memperbaikinya sampai pagi.", "Tawarkan membelikan bahan maket baru.", "Tertawakan nasib sialnya."])
    if _return == "A":
        nar "Kau menanyakan bagian yang bisa ditangani tanpa mengganggu rancangannya. Nagisa semula hendak mengatakan tidak ada, lalu melihat sudut rusak yang terlalu luas untuk dikerjakan sendirian."
        nagisa "Bagian dasar. Yang ini harus rata. Atap jangan disentuh dulu, aku yang urus."
        nar "Malam berjalan lewat potongan bahan, koreksi singkat, dan dua cangkir yang lama dibiarkan dingin. Menjelang pagi ia bertanya apakah kau lelah, kemudian menyuruhmu berhenti lima menit bersama dirinya."
        nagisa "Terima kasih. Aku tahu kamu bisa saja pulang. Aku cuma belum tahu cara bilang tanpa terdengar seperti pidato."
    elif _return == "B":
        nar "Kau menawarkan membeli bahan pengganti. Nagisa tersinggung sejenak, lalu menyadari kau tidak sedang menawarkan membeli seluruh keberhasilannya."
        nagisa "Kalau begitu yang jenisnya sama. Jangan yang mahal karena kasihan. Ini proyek, bukan sumbangan."
        nar "Ia menuliskan kebutuhannya dan jumlah yang benar. Menerima bantuan masih membuatnya canggung, tetapi malam itu uang tidak perlu dianggap musuh harga dirinya."
    else:
        nar "Kau menertawakan nasibnya. Nagisa melihatmu, lalu kembali ke maket dengan wajah yang berubah sangat tenang."
        nagisa "Keluar. Aku nggak sedang mencari penonton untuk hari terburukku."
        nar "Ia menunggu sampai kau benar-benar bergerak. Pintu ditutup sebelum kau sempat mengubah tawa menjadi gurauan yang katanya tidak dimaksudkan melukai."
    return

# ── Mi03 · Perpustakaan Medis Malam (Miyuki, RS Tachibana, M04) ──
# ┌─ PANDUAN CERITA · Mi03 · Perpustakaan Medis Malam
# │ LOKASI  : Medis · Rumah Sakit Tachibana
# │ TERLIBAT: Tachibana Miyuki (+ Koita bila relevan)
# │ AWALAN  : Miyuki belajar sampai larut.
# │ INTI    : A bawakan makanan / B paksa pulang / C temani diam.
# │ AKHIRAN : stage 1 (kelelahan); sena_curiga mulai.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mi03:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana")
    nar "Lewat tengah malam. Lampu perpustakaan medis sudah separuh dimatikan, tapi Miyuki masih di sana, dikelilingi tumpukan buku anatomi. Ia tidak sadar kau datang sampai kau cukup dekat untuk melihat betapa pucatnya ia."
    miyuki "...Jam berapa? Ah, tidak apa. Sedikit lagi. Bab ini saja."
    if any(c["ev"] == "Mi01" and c["key"] == "B" for c in choices_log):
        miyuki "Kau lagi. Kotak bento waktu itu juga kau yang bawa, ya?"
    nar "Ia sudah mengatakan 'bab ini saja' entah berapa kali, kelihatannya."
    call kk_family_menu("Mi03", ["Bawakan sesuatu untuk ia makan, diam-diam temani.", "Tegas: tutup bukunya, suruh ia pulang.", "Duduk diam di sebelahnya tanpa bicara."])
    if _return == "A":
        nar "Kau membawakan makanan yang bisa dimakan tanpa mengotori buku. Miyuki menatap bungkusnya, kemudian jam, baru menyadari betapa lama ia tidak makan."
        miyuki "Aku tadi mau berhenti sebelum lapar. Ternyata aku melewatkan laparnya juga."
        nar "Ia menutup buku sementara kalian makan. Ketika kembali membukanya, ia tidak lagi mengaku masih segar hanya agar kau tidak khawatir."
    elif _return == "B":
        nar "Kau menutup buku dan memintanya pulang. Miyuki refleks menahan halaman, lalu membiarkan tangannya jatuh."
        miyuki "Aku tahu kamu khawatir. Tapi lain kali bilang dulu sebelum menutupnya. Aku jadi merasa sedang ditegur karena belum cukup pandai menjaga diri."
        nar "Ia tetap mengemasi tas. Kalian meninggalkan perpustakaan dengan satu percakapan sulit yang ternyata bisa berlangsung tanpa membatalkan kepedulian."
    else:
        nar "Kau duduk dan mengeluarkan bacaanmu sendiri. Miyuki melihatmu beberapa kali, memastikan kehadiranmu tidak menuntut ia segera menyambut."
        miyuki "Kamu nggak harus tinggal sampai selesai. Tapi... jangan pergi dulu. Sebentar saja."
        nar "Permintaan itu keluar tanpa godaan. Beberapa menit kemudian ia berhenti membaca, menyandarkan punggung, dan membiarkan dirinya terlihat lelah."
    return
