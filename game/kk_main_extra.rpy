# Milestone utama tambahan di lokasi standar: Koita K07 (Matsuda sekutu/musuh)
# dan K08 (sabotase Natal, konsekuensi), Nagisa N11/N12/N13 (pra-gerbang; jeal,
# relasi Chiasa, konflik terbuka). Route-gate eksplisit (BL/Koita-Success/yandere
# N14+) dan event vila tidak disentuh. Cabang gelap = konsekuensi tanpa metode.
# Nilai prototipe; mengikuti Event_Koita / Event_Nagisa.

# ┌─ PANDUAN CERITA · K07 · Bazar Sastra
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : klub sastra; Matsuda memajang esai "Tokoh Utama yang Tidak Pernah Memilih".
# │ INTI    : A baca dan dukung Matsuda / B kritik esainya / C bela Koita.
# │ AKHIRAN : A menjadikan Matsuda sekutu; B musuh; C membuat Matsuda menjaga jarak.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K07:
    call kk_scene_enter("koita", "Gedung Sastra · Bazar Sastra")
    if kk_host == "chiasa":
        if kk_slot >= 3:
            nar "Selasar lantai dasar Gedung Sastra malam itu masih ramai di bawah lampu gantung menjelang penutupan bazar buku dan buletin tahunan Klub Sastra. Meja-meja lipat berjejer di sepanjang dinding bata, dipenuhi tumpukan antologi cerpen mahasiswa, pembatas buku buatan tangan, dan buku-buku sastra bekas."
        else:
            nar "Selasar lantai dasar Gedung Sastra hari itu jauh lebih ramai daripada hari kuliah biasa karena Klub Sastra sedang menggelar bazar buku dan buletin tahunan. Meja-meja lipat berjejer di sepanjang dinding bata, dipenuhi tumpukan antologi cerpen mahasiswa, pembatas buku buatan tangan, dan buku-buku sastra bekas."
        nar "Saat kamu berjalan menyusuri lorong di antara meja pameran, sebuah kerumunan kecil di stan paling pojok menarik perhatianmu. Beberapa mahasiswi tampak sedang membaca selembar buklet tipis sambil menahan tawa dan sesekali melirik ke arah Koita yang berdiri dengan wajah serba salah di samping meja tersebut."
        chiasa "Ko-nii? Kenapa pada berkumpul di pojok sini? Lagi ada buku baru yang laris ya?"
        koita "Eh, Chi-chan... nggak usah dibaca deh buklet di meja ini, cuma tulisan iseng teman seklubku."
        nar "Di balik meja pojok itu duduk Matsuda Takumi, rekan satu klub Koita yang berambut ikal agak gondrong dan berkacamata bulat. Keranjang plastik di depannya yang berisi buklet esai fotokopian sudah hampir kosong, jauh lebih laris dibandingkan tumpukan buku cerpen resmi klub di sebelahnya."
        "Matsuda" "Jangan dilarang dong, Koita. Justru semakin banyak pembaca semakin bagus buat kritik sastra."
        nar "Kamu melangkah mendekat dan mengambil satu salinan contoh buklet yang tersisa di atas taplak meja. Pada halaman sampulnya tercetak judul dengan huruf hitam tebal, 'Tokoh Utama yang Tidak Pernah Memilih', lengkap dengan subjudul tentang analisis kebiasaan menggantung perasaan dalam romansa kampus."
        chiasa "Judulnya lumayan tajam juga ya, Matsuda-senpai."
        koita "Matsuda... tunggu sebentar deh. Aku baru selesai baca halaman keduanya barusan. Ini kamu menulis esai soal aku ya?"
        "Matsuda" "Lho, kok kamu langsung merasa begitu, Koita? Di bagian pengantarnya kan sudah kutulis kalau ini cuma bedah pola karakter cerita fiksi pada umumnya."
        koita "Masalahnya contoh kalimat dialog yang kamu kutip di paragraf ketiga ini, yang berbunyi 'Ayo kita kumpul semua aja biar nggak ada yang ditinggal', itu sama persis sampai ke titik komanya sama omonganku waktu di meja kantin hari Kamis minggu lalu!"
        nar "Dua mahasiswa di sebelah meja langsung memelankan bisik-bisik mereka, pura-pura memeriksa harga buku bekas sambil memasang telinga lebar-lebar."
        "Matsuda" "Aku sama sekali nggak mencantumkan marga ataupun inisial siapa-siapa di kertas itu, Koita. Kalau kamu baca kalimatnya terus langsung merasa itu dirimu sendiri, bukannya itu berarti kamu memang terlalu sering pakai kalimat kayak gitu ke orang-orang?"
        koita "Bukan gitu maksudku... waktu di kantin kemarin kan konteksnya memang lagi ramai dan semua orang teman sendiri. Aku cuma nggak mau ada yang merasa tersisih!"
        "Matsuda" "Dan persis kalimat pembelaanmu barusan itu sudah kubahas juga di paragraf keempat halaman dua."
        nar "Koita terdiam sambil menggaruk tengkuknya, senyum ramahnya tampak kaku karena puluhan mata di selasar sedang memperhatikan mereka. Matsuda lalu melirik ke arahmu yang sedang memegang buklet esai tersebut di samping meja."
        "Matsuda" "Eh, kebetulan ada adiknya Koita juga di sini. Kamu barusan sudah baca halaman duanya kan? Coba jujur deh dari sudut pandang orang yang tinggal serumah, menurutmu isi tulisanku di situ mengarang bebas atau memang tepat sasaran?"
    else:
        if kk_slot >= 3:
            nar "Selasar utama Gedung Sastra malam itu masih dipadati deretan meja kayu bazar tahunan Klub Sastra di bawah cahaya lampu lorong. Ketika kamu melangkah masuk melewati lobi untuk mencari Koita, kerumunan mahasiswa yang berkumpul di salah satu meja pojok langsung menarik perhatianmu."
        else:
            nar "Selasar utama Gedung Sastra hari itu dipadati deretan meja kayu untuk acara bazar tahunan Klub Sastra. Ketika kamu melangkah masuk melewati lobi untuk mencari Koita, kerumunan mahasiswa yang berkumpul di salah satu meja pojok langsung menarik perhatianmu."
        yutaka "Ramai amat pojok sini, Koita. Antologi klubmu laris keras ya tahun ini?"
        koita "Ah, Yutaka... bukan antologinya. Itu buklet esai pribadinya Matsuda, nggak usah kamu ambil deh."
        nar "Di belakang meja itu duduk Matsuda Takumi, anggota Klub Sastra berambut ikal dan berkacamata bulat yang satu angkatan dengan kalian. Tumpukan buklet esai tipis hasil cetakan sendiri di mejanya laris manis hingga tersisa beberapa lembar, sementara tumpukan antologi cerpen di sebelahnya masih utuh."
        "Matsuda" "Biarkan saja Kisaragi baca, Koita. Kalau memang cuma tulisan fiksi, buat apa disembunyikan?"
        nar "Begitu kamu mengambil satu lembar contoh buklet dari atas meja, kamu langsung paham mengapa beberapa pengunjung di sekitar sana tersenyum penuh arti sambil melirik Koita yang berdiri kaku di dekat papan stan."
        nar "Judul di halaman depannya tercetak tegas, 'Tokoh Utama yang Tidak Pernah Memilih', diikuti subjudul tentang analisis kebiasaan menggantung perasaan dalam romansa kampus."
        yutaka "Wah, judulnya nggak main-main ya, Matsuda."
        koita "Matsuda, sebentar deh. Halaman duanya baru aja selesai kubaca. Kamu sengaja menulis sindiran buat aku ya di sini?"
        "Matsuda" "Kok langsung menuduh begitu, Koita? Itu kan esai kritik sastra soal pola tokoh pria baik hati di cerita romansa populer."
        koita "Ya gimana aku nggak merasa, contoh dialog di halaman dua bawah ini, yang soal mengajak semua orang jalan bareng biar nggak ada yang sedih, itu persis banget sama kalimat yang kuomongin waktu di kantin minggu kemarin!"
        nar "Beberapa pengunjung di dekat meja langsung pura-pura membolak-balik buku bekas sambil menahan senyum dan mendengarkan perdebatan itu."
        "Matsuda" "Aku kan nggak menulis nama Amamiya Koita satu huruf pun di situ. Kalau kamu langsung merasa tersindir waktu baca contohnya, berarti kalimat mengambang macam itu memang sudah jadi kebiasaan harianmu, kan?"
        koita "Ya nggak gitu juga maksudku... waktu di kantin itu kan situasinya semua orang lagi kumpul, masa aku biarin ada yang sendirian!"
        "Matsuda" "Nah, alasan itu juga sudah kucatat rapi di paragraf keempat halaman dua."
        nar "Koita terdiam dengan wajah merah tipis, tampak sangat canggung karena menjadi pusat perhatian di tengah selasar. Matsuda kemudian menoleh kepadamu yang masih memegang lembaran esai itu."
        "Matsuda" "Nah, kebetulan ada Kisaragi nih. Kamu kan sahabatnya dari kecil yang paling sering jalan bareng dia. Setelah baca tulisanku barusan, menurutmu analisis polaku di situ ngawur nggak?"
    call kk_family_menu("K07", ["\"Jujur aja, bagian soal baik ke semua orang tapi nggak pernah ngasih kepastian itu memang bener.\"", "\"Kalau mau ngritik teman sendiri ngomong langsung dong, jangan disindir lewat bazar begini.\"", "\"Kamu kan cuma lihat dari luar. Koita dari dulu memang ramah ke semua orang.\""])
    if _return == "A":
        if kk_host == "chiasa":
            nar "Kamu membalik halaman buklet tipis itu sampai ke paragraf penutupnya, lalu menatap Matsuda dengan tenang di depan kerumunan kecil tersebut."
            chiasa "Kalau boleh jujur sih, bagian yang nulis soal bersikap manis ke semua orang tapi nggak pernah berani ngasih kepastian itu memang ada benernya, Matsuda-senpai."
            koita "Eh... Chi-chan?! Kok kamu malah ngomong gitu di depan orang-orang?"
            chiasa "Habisnya yang ditulis di halaman tiga ini masuk akal, Ko-nii. Di sini dibilang, kadang ada orang yang mikir selama dia nggak pernah menolak dengan kalimat kasar, berarti dia nggak menyakiti siapa pun. Padahal buat orang yang terus-terusan dikasih harapan setengah-setengah, menunggu tanpa kejelasan itu jauh lebih bikin capek."
            nar "Senyum miring di bibir Matsuda perlahan mereda. Ia menaikkan kacamata bulatnya dan menatapmu dengan sorot mata yang jauh lebih serius."
            "Matsuda" "Tumben banget ada anggota keluarganya sendiri yang langsung menangkap inti argumenku. Aku menulis esai ini juga sebenarnya nggak buat mengajak orang-orang di kampus membenci tokoh utamanya kok."
            chiasa "Terus tujuan Senpai mencetak ini buat apa?"
            "Matsuda" "Soalnya selama ini aku muak lihat polanya di sekitar kita. Tiap kali ada satu gadis yang akhirnya kecewa atau makan hati gara-gara kelamaan menunggu, orang-orang selalu menyalahkan gadisnya yang dianggap salah paham sendiri atau terlalu berharap. Padahal sumber masalahnya ada di pihak yang terus sengaja buka celah supaya nggak kehilangan perhatian."
            chiasa "Biar semua orang tetap menyukainya tanpa harus mengambil risiko kehilangan siapa-siapa ya, Senpai?"
            "Matsuda" "Tepat sekali. Kalimatmu barusan bahkan lebih tajam daripada paragraf penutupku."
            nar "Matsuda mencabut pulpen dari saku kemejanya, menuliskan nomor ruang diskusi klub di sudut belakang buklet tersebut, lalu menyodorkannya kepadamu."
            "Matsuda" "Salinan yang itu ambil aja buatmu, nggak usah bayar. Kapan-kapan kalau kamu mau ngobrol lebih jauh tanpa ditonton satu selasar kayak sekarang, mampir aja ke meja pojok ruang klub sastra."
            chiasa "Terima kasih bukletnya, Matsuda-senpai."
            nar "Di sampingmu, Koita hanya berdiri membisu sambil menggigit bibir bawahnya, tampak terpukul karena adik tirinya sendiri justru membenarkan kritik tajam tersebut di hadapan teman-teman seklubnya."
        else:
            nar "Kamu membaca halaman terakhir esai itu sampai habis, lalu melipatnya rapi dan mengangguk pelan kepada Matsuda."
            yutaka "Analisisnya nggak ngawur sih, Matsuda. Bagian yang menyoroti soal orang yang terlalu baik ke semua pihak sampai nggak pernah ngasih batas tegas itu memang tepat sasaran."
            koita "Hah? Yutaka?! Kok kamu malah ikut-ikutan membenarkan tulisan dia sih?"
            yutaka "Aku nggak lagi ikut-ikutan menyerang kamu, Koita. Tapi coba kamu pikir pakai kepala dingin, selama ini kamu kan memang paling nggak sanggup bilang tidak secara tegas kalau ada yang mendekat. Buat orang yang terlanjur berharap, digantung terus pakai kebaikan setengah-setengah itu lama-lama menyiksa juga."
            nar "Cengiran sinis di wajah Matsuda perlahan hilang. Ia membetulkan letak kacamatanya dan menatapmu dengan respek yang tidak ia sembunyikan."
            "Matsuda" "Jujur aku tadinya mengira kamu bakal langsung pasang badan membela sahabatmu tanpa baca isinya dulu, Kisaragi. Aku menulis esai itu juga nggak karena dendam pribadi kok."
            yutaka "Terus kenapa sampai kamu cetak buat bazar?"
            "Matsuda" "Aku cuma gerah aja melihat orang-orang di kampus selalu menyalahkan pihak perempuan kalau sampai ada yang patah hati, dibilang salah paham sendiri lah, terlalu terbawa perasaan lah. Padahal jelas-jelas ada orang yang terus memelihara harapan mereka supaya tetap disukai semua orang."
            yutaka "Semua kebaikan yang dikasih merata ujung-ujungnya cuma jadi cara paling aman buat menghindar dari tanggung jawab memilih."
            "Matsuda" "Wah, tajam sekali rangkumanmu. Harusnya kalimat itu yang kutaruh di halaman sampul."
            nar "Matsuda mengambil pulpen dari saku kemejanya, melingkari satu catatan di halaman belakang buklet itu, lalu menyerahkannya kembali ke tanganmu."
            "Matsuda" "Ambil aja buklet itu, gratis buatmu. Kalau kapan-kapan kamu pengin diskusi tanpa dikerubungi penonton bazar begini, datang aja ke ruang klub sastra sore-sore."
            yutaka "Oke, kuterima bukletnya."
            nar "Di sebelahmu, Koita hanya berdiri kaku sambil mengusap tengkuknya, tidak mampu berkata apa-apa lagi setelah sahabat terdekatnya sendiri mengakui kebenaran esai tersebut di depan umum."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Kamu menutup buklet fotokopian itu, lalu meletakkannya kembali ke atas meja kayu tepat di depan tumpukan uang kembalian Matsuda."
            chiasa "Kalau Matsuda-senpai memang punya kritik buat teman satu klub sendiri, harusnya ngomong empat mata aja langsung ke orangnya. Nggak usah dicetak puluhan lembar terus dijual di bazar sambil pura-pura bilang ini cuma bahas tokoh fiksi."
            nar "Suara obrolan mahasiswa di sekitar meja pojok itu langsung berhenti. Mata Matsuda menyipit di balik lensa kacamata bulatnya."
            "Matsuda" "Kalau menurutmu ada bagian dari analisis di tulisanku yang keliru, tunjukkan aja paragraf mana yang salah. Jangan mengalihkan diskusi ke soal etika bazar."
            chiasa "Masalahnya bukan soal analisis sastra atau bukan, Senpai. Senpai sengaja memasukkan kutipan omongan kantin yang semua anak di selasar ini langsung tahu itu siapa, tapi giliran Ko-nii nanya baik-baik, Senpai malah berlindung di balik alasan nggak menulis nama. Itu kan cuma cari aman supaya nggak bisa disalahkan."
            "Matsuda" "Kalau orangnya memang tidak merasa punya tabiat seperti yang kutulis di situ, seharusnya tidak perlu panik siapa yang membaca buklet ini, kan?"
            chiasa "Dan kalau Senpai memang yakin sama kritik Senpai, harusnya nggak perlu pakai sindiran anonim di depan pengunjung bazar buat menjatuhkan teman seklub sendiri."
            koita "Sudah, Chi-chan, cukup... jangan berdebat makin keras di sini, nggak enak dilihatin anak-anak jurusan lain. Ayo kita pergi saja."
            nar "Suasana di sekitar stan Klub Sastra langsung mendingin. Matsuda tidak lagi membalas ucapanmu. Ia langsung merapikan kotak uangnya dan beralih melayani pembeli di sisi kanan meja, menutup rapat map catatan drafnya setiap kali kamu melirik ke arahnya."
        else:
            nar "Kamu menutup lembaran buklet itu lalu menaruhnya kembali ke atas meja kayu dengan tepukan pelan yang cukup jelas terdengar oleh orang-orang di sekitar stan."
            yutaka "Kalau kamu memang punya ganjalan sama sikap teman satu klubmu sendiri, harusnya omongin langsung empat mata di ruang klub, Matsuda. Nggak usah dicetak terus dipajang di bazar umum pakai kedok esai fiksi begini."
            nar "Beberapa pengunjung di dekat meja langsung mundur setengah langkah melihat ketegangan di antara kalian. Matsuda menatapmu dengan kening berkerut."
            "Matsuda" "Kalau menurutmu isi argumenku di dalam kertas itu salah, bantah aja isinya, Kisaragi. Nggak perlu menggeser pembicaraan ke soal sopan santun pertemanan."
            yutaka "Yang kupersoalkan itu caramu lempar batu sembunyi tangan. Kamu comot kalimat omongan dia di kantin supaya satu gedung tahu siapa yang kamu sindir, tapi begitu ditanya langsung, kamu malah ngeles bilang nggak mencantumkan nama. Itu cuma mencari panggung yang aman."
            "Matsuda" "Lho, kalau sahabatmu itu memang merasa bersih dan nggak pernah menggantung perasaan orang, buat apa kalian berdua repot-repot pusing soal siapa yang baca?"
            yutaka "Bukan soal pusing dibaca, ini soal pengecut atau nggaknya caramu mengkritik orang."
            koita "Sudah, Yutaka, jangan diterusin di sini... semua orang sudah pada melihat ke meja ini. Ayo kita geser saja."
            nar "Percakapan di depan stan itu langsung membeku. Matsuda mendengus pendek, menarik kursinya mundur, lalu kembali melayani pengunjung lain sambil mengunci laci catatannya rapat-rapat dari hadapanmu."
    else:
        if kk_host == "chiasa":
            nar "Kamu meletakkan kembali buklet contoh itu ke atas meja, lalu bergeser berdiri tepat di sebelah lengan Koita."
            chiasa "Matsuda-senpai bisa nulis begitu kan cuma karena melihat potongan dari luar aja. Aku tinggal serumah sama Ko-nii dari kecil, aku tahu persis Ko-nii itu memang nggak tegaan dan tulus suka bantu orang. Dia nggak pernah sengaja mau mempermainkan perasaan siapa-siapa."
            nar "Ketegangan di wajah Koita langsung mencair. Ia menoleh menatapmu dengan senyum yang sangat lega karena dibela secara terbuka di depan teman-temannya."
            koita "Makasih ya, Chi-chan. Tadi aku beneran bingung mau jelasin gimana kalau langsung dituduh begitu."
            nar "Matsuda tidak ikut menaikkan nada suaranya. Ia hanya menyandarkan punggungnya ke kursi lipat dan menatap kalian berdua secara bergantian dari balik kacamatanya."
            "Matsuda" "Seseorang memang bisa saja tidak punya niat jahat sedikit pun di dalam kepalanya. Tapi kalau kebiasaan tidak tegaannya itu tetap berakhir membuat orang lain terluka dan berharap sia-sia, apakah alasan tidak berniat buruk itu otomatis menghapus akibatnya?"
            chiasa "Urusan perasaan orang lain kan nggak bisa semuanya dibebankan ke Ko-nii sendirian, Senpai."
            "Matsuda" "...Menarik. Sepertinya aku tidak perlu memperpanjang diskusi ini dengan kalian."
            koita "Ayo, Chi-chan, kita pindah lihat stan buku bekas di ujung koridor sana aja yuk. Di pojok sini udaranya sudah terlalu pengap."
            chiasa "Iya, ayo ke sana aja, Ko-nii."
            nar "Koita segera menyentuh lengan bajumu dan mengajakmu berjalan menjauh dari meja pojok tersebut sementara Matsuda hanya memperhatikan punggung kalian dengan tatapan menjaga jarak."
        else:
            nar "Kamu menaruh kembali buklet tipis itu ke atas meja pameran, lalu berdiri sejajar di samping bahu Koita."
            yutaka "Kamu bisa nulis kesimpulan sesederhana itu karena cuma lihat dari pinggir, Matsuda. Aku kenal Koita dari zaman kami masih anak-anak, dia itu memang dasarnya ramah dan nggak tega menolak orang yang minta tolong. Dia nggak sengaja mau mainin perasaan siapa pun."
            nar "Wajah Koita yang sejak tadi kaku langsung melunak. Ia mengembuskan napas panjang dan menoleh padamu dengan senyum penuh terima kasih."
            koita "Makasih banyak, Yutaka. Tadi aku beneran nggak tahu harus jawab apa waktu dipojokin begitu."
            nar "Matsuda tidak terpancing untuk berdebat keras. Ia hanya menumpukan dagunya di atas punggung tangan dan menatap kalian berdua dengan ekspresi datar."
            "Matsuda" "Tidak punya niat buruk itu satu hal, Kisaragi. Tapi kalau pola kebaikan yang sama terus diulang sampai ujung-ujungnya tetap ada orang yang makan hati, masa selamanya mau dimaafkan cuma dengan alasan tidak sengaja?"
            yutaka "Orang lain juga punya akal buat menilai batasnya sendiri, Matsuda, nggak adil kalau semua kesalahan dilempar ke Koita."
            "Matsuda" "...Begitu pandanganmu rupanya. Baiklah, tidak ada gunanya juga kubantah."
            koita "Ayo, Yutaka, kita geser lihat meja buku sastra klasik di dekat pintu lobi sana aja. Di sini sudah terlalu ramai orang lewat."
            yutaka "Iya, ayo pindah ke depan."
            nar "Koita segera menepuk lengan jaketmu dan mengajakmu melangkah meninggalkan kerumunan stan pojok tersebut sementara Matsuda kembali merapikan bukletnya dengan sikap berjarak."
    return

# ┌─ PANDUAN CERITA · K08 · Natal Plot Armor
# │ LOKASI  : Kampus Kouseikan · Gedung Sastra
# │ TERLIBAT: Amamiya Koita
# │ AWALAN  : kebetulan Natal mempertemukan Koita dengan heroine paling siap.
# │ INTI    : A intersep lewat telepon / B ambil alih kencan / C biarkan / D hadir sebagai pihak ketiga.
# │ AKHIRAN : hub besar #3; menentukan siapa memegang Natal Tahun 1.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_K08:
    call kk_scene_enter("koita", "Gedung Sastra · Menjelang Natal")
    if kk_host == "chiasa":
        nar "Angin akhir Desember bertiup dingin menyusuri pelataran Gedung Sastra. Di sepanjang kanopi batu dan dahan pohon kamper di tepi jalan setapak, untaian lampu hias berwarna kuning hangat yang dipasang panitia mahasiswa sudah menyala, memantulkan cahaya redup di atas paving yang lembap."
        nar "Kamu baru saja melintas dari arah jalur perpustakaan sambil membawa map lipat ketika melihat pintu kaca lobi Gedung Sastra didorong terbuka. Koita keluar bersama dua teman sekelasnya sambil melilitkan syal rajut abu-abu ke lehernya."
        "Mahasiswa Sastra" "Kita orang mau langsung ke kedai ramen dekat perempatan nih, Koita. Kamu jadi ikut nggak?"
        koita "Duluan aja deh. Aku belum ada janji pasti sih habis ini, paling mau jalan kaki pelan-pelan lihat suasana dekat stasiun dulu sebentar."
        "Mahasiswa Sastra" "Oke, hati-hati ya. Selamat libur Natal!"
        nar "Kedua temannya berbelok ke jalur parkir sepeda, meninggalkan Koita yang masih berdiri di teras tangga sambil merapikan tali tas selempangnya. Kalimat bahwa ia tidak punya rencana tadi terdengar begitu polos, tetapi saat matamu bergeser ke ujung jalan setapak menuju gerbang utama, pemandangan di sana berkata lain."
        nar "Tepat di bawah tiang lampu taman dekat bangku kayu, seorang gadis yang sangat kamu kenal sedang berdiri menunggu seorang diri. Sejak beberapa menit lalu ia terus merapatkan kerah mantelnya, melirik jam di layar ponsel, lalu menoleh ke arah pintu Gedung Sastra dengan raut wajah seseorang yang sudah mengumpulkan keberanian seharian demi pertemuan yang tampak tidak disengaja."
        nar "Koita baru saja hendak melangkah turun dari anak tangga teras menuju jalan setapak itu. Dari posisimu di dekat pilar selasar samping, jarak mereka tinggal sekitar lima belas langkah lagi."
    else:
        nar "Angin akhir Desember bertiup dingin menyusuri pelataran Gedung Sastra. Rangkaian lampu hias berwarna kuning hangat sudah menyala di sepanjang kanopi batu dan dahan pohon kamper, memantulkan cahaya redup ke permukaan paving yang lembap."
        nar "Kamu baru saja melintas dari arah gedung fakultasmu sambil memasukkan kedua tangan ke dalam saku mantel ketika melihat pintu kaca lobi Gedung Sastra didorong terbuka. Koita keluar bersama dua teman sekelasnya, masih sibuk melilitkan syal rajut abu-abu di lehernya yang belum rapi."
        "Mahasiswa Sastra" "Kami mau langsung cari ramen hangat di perempatan depan nih, Koita. Kamu jadi ikut nggak?"
        koita "Kalian duluan aja deh. Aku belum ada rencana pasti sih habis ini, paling mau jalan kaki pelan-pelan lihat suasana di dekat stasiun dulu sebentar."
        "Mahasiswa Sastra" "Sip kalau gitu. Selamat libur Natal ya!"
        nar "Kedua temannya berbelok ke jalur parkir sepeda, meninggalkan Koita di teras tangga yang sedang merapikan tali tas selempangnya. Ucapan bahwa ia tidak punya rencana barusan terdengar santai dan biasa saja, tetapi saat pandanganmu menyapu ujung jalan setapak menuju gerbang utama, ada pemandangan yang langsung menarik perhatianmu."
        nar "Tepat di bawah tiang lampu taman dekat bangku kayu, seorang gadis yang kamu kenal berdiri seorang diri. Ia beberapa kali menggosok kedua telapak tangannya, melirik jam di layar ponsel, lalu memandang kembali ke arah pintu Gedung Sastra dengan raut wajah seseorang yang sejak tadi menunggu momen untuk membuat pertemuannya terlihat seperti kebetulan."
        nar "Koita baru saja menginjak anak tangga teratas untuk turun ke jalan setapak itu. Dari posisimu di dekat pilar selasar samping, jarak antara mereka berdua tidak sampai lima belas langkah lagi."
    $ _rows = [(c, Return(k), False) for k,c in zip("ABCD", ["Telepon Koita sekarang untuk mengalihkan langkahnya.", "Hampiri lebih dulu orang yang menunggu di ujung jalan.", "Biarkan saja mereka bertemu tanpa ikut campur.", "Melangkah keluar dan bergabung di tengah mereka."])]
    call screen kk_choice_panel(_rows, "Natal tahun pertama")
    $ kk_record_choice("K08", _return)
    if _return == "A":
        if kk_host == "chiasa":
            nar "Sebelum sepatu Koita sempat menyentuh jalan setapak utama, kamu segera bergeser ke balik pilar batu selasar, merogoh ponsel dari saku mantelmu, dan menghubungi nomornya."
            nar "Nada sambung baru berbunyi dua kali ketika langkah Koita terhenti di kaki tangga teras. Ia mengeluarkan ponselnya, melihat namamu di layar, lalu langsung menempelkannya ke telinga sambil menatap lurus ke arah kanopi tanpa menyadari siapa yang menunggu di ujung jalan."
            koita "Halo, Chi-chan? Aku baru aja keluar dari pintu Gedung Sastra nih. Kenapa telepon, kamu masih di kampus?"
            chiasa "Untung Ko-nii belum keluar gerbang. Tolong ke selasar belakang dekat gerbang timur sekarang dong, Ko-nii. Tadi aku habis ambil titipan kanvas sama bahan dapur buat di rumah, terus kantong kertasnya sobek sebelah. Tanganku nggak kuat kalau bawa jalan kaki sendirian."
            koita "Lho, kok bisa sobek? Kamu di gerbang timur yang dekat toko buku tua itu sekarang?"
            chiasa "Iya, aku nunggu di dekat pos satpam timur ya. Tapi Ko-nii jangan lewat jalan setapak depan Gedung Sastra, tadi kulihat lagi macet banget ada rombongan klub olahraga bubaran. Langsung potong jalan lewat lorong belakang perpustakaan aja biar cepat."
            koita "Oh, iya-iya, lewat belakang perpustakaan memang lebih dekat ke timur. Tunggu di situ ya, jangan dipaksa angkat dulu nanti barangnya jatuh semua. Aku ke sana sekarang."
            chiasa "Iya, cepat ya Ko-nii, dingin banget di sini."
            nar "Koita menutup telepon, memasukkan ponselnya kembali ke saku jaket, lalu langsung memutar balik tubuhnya menuju lorong sempit di belakang gedung tanpa sekali pun sempat melirik ke arah tiang lampu taman di ujung jalan setapak."
            nar "Setelah punggung Koita menghilang di belokan perpustakaan, kamu melirik kembali ke arah bangku taman di depan. Gadis yang menunggu di bawah lampu hias itu masih berdiri di tempatnya selama hampir sepuluh menit, beberapa kali menatap pintu Gedung Sastra yang sudah sepi dan memeriksa layar ponselnya yang tetap gelap."
            nar "Ketika lampu lobi gedung akhirnya dipadamkan oleh petugas jaga, ia mengembuskan napas putih tipis ke udara dingin, merapatkan syalnya, lalu berbalik melangkah keluar gerbang seorang diri sebelum kamu bergegas memutar jalan menyusul Koita ke gerbang timur."
        else:
            nar "Sebelum Koita turun ke jalan setapak utama, kamu melangkah mundur ke samping deretan mesin penjual minuman di selasar, mengeluarkan ponsel dari saku mantel, lalu menekan nomornya."
            nar "Baru berdering dua kali, Koita berhenti di anak tangga paling bawah sambil merogoh saku jaketnya. Ia mengangkat panggilan itu dengan wajah santai sambil menatap deretan lampu hias di kanopi, sama sekali belum melihat ke arah bangku taman di ujung jalan."
            koita "Halo, Yutaka? Tumben langsung telepon. Iya, aku masih di depan Gedung Sastra nih. Ada apa?"
            yutaka "Syukurlah kamu belum keluar gerbang. Bisa minta tolong mampir sebentar ke dekat gerbang timur nggak? Tadi aku ambil titipan kardus minuman sama buku cetak dari ruang panitia, eh tali pengikatnya putus di jalan. Males banget kalau harus bolak-balik dua kali."
            koita "Lho, kamu bawa sebanyak apa memangnya? Posisimu sekarang di pos satpam gerbang timur?"
            yutaka "Iya, di selasar sebelah toko buku tua. Eh, kamu jangan lewat jalan setapak depan Gedung Sastra ya, barusan kulihat rombongan klub basket lagi bubaran penuh banget di situ. Potong lewat lorong belakang perpustakaan aja, lebih cepat sampai ke sini."
            koita "Oh, oke-oke, lewat belakang perpustakaan memang lebih dekat. Tunggu situ sebentar ya, jangan dipaksa angkat sendirian. Aku jalan ke sana sekarang."
            yutaka "Sip, makasih ya, Koita. Kutunggu."
            nar "Sambungan terputus. Dari balik pilar, kamu melihat Koita mengantongi ponselnya, mengencangkan syal di lehernya, lalu langsung berbalik menyusuri jalur sempit ke belakang gedung tanpa sempat menoleh ke ujung jalan setapak."
            nar "Setelah sosok Koita lenyap di belokan perpustakaan, pandanganmu kembali mengarah ke bawah tiang lampu taman. Gadis yang berdiri di sana tetap menunggu hampir sepuluh menit lamanya, beberapa kali melirik pintu kaca Gedung Sastra yang kini sepi dan menyalakan layar ponselnya yang tak kunjung menerima pesan."
            nar "Saat petugas keamanan mulai memadamkan lampu lobi gedung, ia mengembuskan napas tipis ke udara dingin, merapatkan kerah mantelnya, lalu berbalik berjalan ke arah gerbang seorang diri. Setelah ia menjauh, barulah kamu memutar langkah lewat jalur belakang untuk menemui Koita."
    elif _return == "B":
        if kk_host == "chiasa":
            nar "Sementara Koita masih berhenti di tangga teras untuk mengancingkan jaketnya yang terbuka, kamu langsung mengambil jalur pintas melewati rumput samping selasar dan melangkah cepat menuju tiang lampu di ujung jalan setapak."
            chiasa "Lho, Senpai masih di kampus juga jam segini? Sendirian aja berdiri di dekat angin dingin begini?"
            nar "Sosok yang sedang berdiri di bawah lampu taman itu terkesiap kecil dan langsung menoleh ke arahmu. Ia sempat melirik gugup melewati bahumu ke arah teras Gedung Sastra yang masih terhalang beberapa mahasiswa lain, bingung harus menjawab apa karena tidak menyangka adik tiri Koita yang justru muncul di depannya."
            chiasa "Jangan-jangan lagi nunggu orang ya? Tapi gedung sebelah sana barusan sudah mulai dikunci lho sama petugasnya."
            nar "Ia buru-buru menggeleng dan beralasan baru saja selesai membereskan urusan kuliah lalu hendak mencari minuman hangat sebelum pulang. Kamu tidak membiarkan jeda itu memberinya kesempatan menoleh ke belakang lagi."
            chiasa "Kebetulan banget, aku juga baru selesai dari studio dan kedinginan setengah mati nih. Temani aku beli cokelat panas sama kue manis di kedai depan stasiun yuk? Hari ini ada menu khusus Natal lho, nggak enak kalau duduk minum sendirian."
            nar "Mendengar ajakanmu yang begitu langsung dan ramah, ia tampak ragu selama dua detik, menimbang antara tetap berdiri menunggu sesuatu yang belum pasti atau menerima kehadiranmu. Akhirnya ia mengangguk pelan dan mulai melangkah di sampingmu menuju gerbang."
            chiasa "Nah, gitu dong. Tanganmu aja sudah dingin banget tuh, sini masukin saku mantel dulu."
            nar "Tepat ketika kalian berdua sudah melewati gerbang batu kampus dan mulai berbaur dengan arus mahasiswa yang menuju stasiun, Koita baru saja sampai di dekat tiang lampu taman yang kini kosong. Matanya menangkap sosokmu dari kejauhan."
            koita "Eh... Chi-chan?! Tunggu, kalian mau ke mana?"
            nar "Koita sempat mengangkat sebelah tangannya dan melangkah cepat hendak menyusul, tetapi lampu penyeberangan jalan di depan gerbang keburu berganti hijau. Kamu langsung menggandeng ringan lengan teman jalanmu untuk menyeberang bersama kerumunan pejalan kaki sebelum Koita sempat mencapai trotoar."
            nar "Di seberang jalan, ponsel di dalam sakumu bergetar dua kali oleh pesan singkat dari Koita yang menanyakan kenapa kamu tidak mendengar panggilannya tadi. Kamu membiarkan pesan itu tetap di dalam saku, lalu mendorong pintu kaca kedai kopi yang hangat sambil melanjutkan obrolan dengan orang di sebelahmu."
        else:
            nar "Selagi Koita masih berhenti di tangga teras untuk mengancingkan jaketnya, kamu langsung memotong lewat jalur samping taman dan menghampiri tiang lampu di ujung jalan setapak lebih dulu."
            yutaka "Hei, masih belum pulang jam segini? Berdiri di bawah angin begini bisa masuk angin lho."
            nar "Gadis yang menunggu di bawah lampu taman itu menoleh sedikit kaget. Tatapannya sempat melirik cepat melewati bahumu ke arah teras Gedung Sastra yang masih tertutup lalu lalang beberapa mahasiswa, agak salah tingkah karena bukan Koita yang datang menghampiri."
            yutaka "Lagi nunggu orang ya? Soalnya pintu Gedung Sastra di belakang situ barusan sudah mulai sepi dan lampu lobinya mau dimatikan petugas."
            nar "Ia segera menggeleng dan menjawab pendek bahwa ia baru saja selesai mengurus catatan di kampus lalu sempat berhenti sebentar karena udara dingin. Kamu tersenyum santai tanpa memancing lebih jauh, tidak memberi jeda yang membuatnya kembali menoleh ke belakang."
            yutaka "Pas banget kalau gitu. Aku juga baru kelar dari gedung sebelah dan pengin cari kopi hangat sebelum balik. Ikut mampir ke kedai depan stasiun yuk? Ada menu roti kayu manis hangat buat Natal, nggak asyik kalau duduk sendiri di sana."
            nar "Ia tampak menimbang selama beberapa detik antara tetap berdiri di udara dingin menunggu kemungkinan yang tidak pasti atau menerima ajakanmu yang terdengar santai dan tidak memaksa. Akhirnya ia mengangguk kecil dan mulai berjalan di sampingmu ke arah gerbang utama."
            yutaka "Ayo, mending jalan agak cepat biar badan nggak keburu kaku. Tanganmu kelihatannya sudah dingin banget tuh."
            nar "Tepat saat kalian melewati gerbang batu kampus dan menyatu dengan arus pejalan kaki menuju stasiun, Koita baru tiba di dekat tiang lampu taman yang sudah kosong. Pandangannya menangkap punggungmu dari kejauhan."
            koita "Eh... Yutaka?! Tunggu, kalian mau ke stasiun juga?"
            nar "Koita sempat mengangkat tangannya tinggi-tinggi dan melangkah cepat hendak menyusul, tetapi lampu penyeberangan di depan gerbang baru saja menyala hijau. Kamu melangkah tenang mengiringi teman jalanmu menyeberangi zebra cross bersama rombongan mahasiswa lain sebelum Koita sempat mengejar ke tepi trotoar."
            nar "Begitu kalian sampai di seberang, ponsel di saku mantelmu bergetar dua kali oleh pesan singkat dari Koita yang bertanya kenapa kamu tidak menoleh saat dipanggil tadi. Kamu membiarkan ponsel itu tetap di dalam saku, lalu membukakan pintu kaca kedai kopi hangat untuk orang di sebelahmu."
    elif _return == "C":
        if kk_host == "chiasa":
            nar "Kamu memutuskan tidak mengeluarkan ponsel dan tidak pula memotong jalan ke depan. Kamu hanya berdiri tenang di dekat papan pengumuman selasar sambil memeluk mapmu. Saat Koita menuruni anak tangga teras dan kebetulan menoleh ke samping, ia melihatmu lalu melambat."
            koita "Lho, Chi-chan? Kamu belum pulang dari studio? Mau jalan bareng ke arah stasiun sekarang?"
            chiasa "Ko-nii jalan duluan aja. Aku masih mau mampir ke ruang loker gedung sebelah sebentar, ada kuas yang ketinggalan."
            koita "Nggak mau kutungguin di sini? Cuma lima menit kan?"
            chiasa "Nggak usah, nanti aku masih mau ngobrol sebentar sama teman studio kalau ketemu di sana. Ko-nii langsung jalan ke depan aja, katanya tadi mau lihat suasana dekat stasiun."
            koita "Oh, oke deh kalau gitu. Jangan pulang terlalu malam ya, nanti sup di rumah keburu dingin."
            nar "Koita melambai singkat, merapatkan syal di lehernya, lalu kembali melangkah menyusuri jalan setapak di bawah deretan lampu hias. Kamu tetap berdiri di dekat pilar selasar, memperhatikan punggungnya yang berjalan lurus menuju gerbang."
            nar "Begitu mencapai tiang lampu taman di ujung jalan, langkah Koita otomatis melambat saat melihat sosok yang berdiri menunggu di dekat bangku kayu."
            koita "Eh, kamu juga belum pulang jam segini? Kebetulan banget ketemu di sini. Dingin lho berdiri di luar, mau jalan bareng sebentar ke arah stasiun?"
            nar "Dari tempatmu berdiri, kamu bisa melihat bahu gadis itu yang tadinya kaku karena dingin langsung rileks. Ia mengangguk cepat dengan senyum yang tak lagi ditahan, lalu melangkah sejajar di samping Koita melewati gerbang kampus menuju keramaian jalan stasiun."
        else:
            nar "Kamu memilih tidak mengeluarkan ponsel maupun memotong langkah ke depan. Kamu tetap bersandar santai di pilar batu dekat papan pengumuman sambil melihat ke arah jalan setapak. Begitu Koita menuruni tangga teras dan menoleh ke samping, ia langsung mengenalimu."
            koita "Lho, Yutaka? Belum pulang juga? Kebetulan, mau jalan bareng ke arah stasiun sekarang nggak?"
            yutaka "Kamu duluan aja, Koita. Aku masih mau balik sebentar ke gedung fakultasku, ada berkas kelompok yang kelupaan di ruang diskusi."
            koita "Mau kutungguin di sini sebentar? Paling cuma lima menit kan?"
            yutaka "Nggak usah, tanggung juga kalau nanti aku mampir ngobrol sama anak kelas. Kamu jalan aja ke depan, katanya tadi mau lihat-lihat dekat stasiun."
            koita "Oh, ya sudah deh kalau gitu. Nanti kalau sudah sampai apartemen kabari ya."
            nar "Koita melambai singkat, merapatkan syalnya, lalu berjalan lurus menyusuri jalur di bawah deretan lampu hias menuju gerbang. Kamu tetap berdiri di tempatmu sambil mengawasi punggungnya yang makin dekat ke ujung jalan."
            nar "Begitu sampai di bawah tiang lampu taman, langkah Koita langsung melambat saat melihat siapa yang berdiri menunggu di dekat bangku kayu."
            koita "Eh, kamu juga baru mau pulang? Kebetulan banget ketemu di sini. Anginnya dingin lho, mau jalan bareng sebentar ke arah stasiun?"
            nar "Dari kejauhan terlihat jelas ketegangan di wajah gadis itu langsung mencair. Ia mengangguk sambil tersenyum lega, lalu melangkah sejajar di samping Koita keluar dari gerbang kampus menuju deretan lampu jalan arah stasiun."
    else:
        if kk_host == "chiasa":
            nar "Kamu menunggu sampai Koita menuruni tangga dan berjalan mendekati tiang lampu taman di ujung jalan setapak. Tepat pada detik Koita berhenti di depan bangku kayu dan gadis yang menunggunya baru saja membuka mulut untuk menyapa, kamu mempercepat langkahmu dan langsung masuk ke tengah mereka."
            chiasa "Ko-nii! Tungguin aku dong, jalannya cepat banget sih! Eh, lho, ada Senpai juga di sini!"
            nar "Gadis di hadapan Koita langsung terdiam dengan kalimat yang tertahan di ujung lidah, menatapmu yang tiba-tiba sudah berdiri di samping lengan Koita. Sementara Koita, dengan refleks ramahnya yang selalu ingin menyenangkan semua orang sekaligus, langsung bergeser setengah langkah agar kalian berdiri membentuk segitiga."
            koita "Lho, Chi-chan? Kirain kamu sudah pulang duluan tadi. Pas banget kita ketemu bertiga di sini."
            chiasa "Baru aja selesai beresin meja studio kok. Kalian berdua baru mau jalan ke arah stasiun ya? Aku ikut dong, perutku sudah lapar banget nih dari sore belum makan apa-apa."
            koita "Boleh banget. Gimana kalau kita bertiga mampir cari minuman hangat sama makan ringan dulu di kedai depan stasiun? Kamu nggak buru-buru pulang kan?"
            nar "Pertanyaan terakhir Koita ditujukan kepada gadis di hadapannya dengan senyum hangat yang polos, sama sekali tidak peka bahwa undangan makan bertiga barusan telah membuyarkan rencana bicara empat mata yang sudah disiapkan sejak tadi. Setelah jeda hening selama dua detik, gadis itu hanya bisa mengangguk pelan."
            chiasa "Asyik! Ayo jalan sekarang sebelum kedainya penuh. Eh, Ko-nii, tadi waktu aku lewat gedung depan kayaknya pohon Natal di lobi utama sudah dipasang bintangnya lho."
            koita "Oh ya? Tadi pagi waktu aku lewat belum selesai dipasang tuh tangga besinya."
            nar "Sepanjang jalan menuju stasiun hingga kalian duduk satu meja di kedai hangat, kamu terus menjaga obrolan tetap berputar pada hal-hal ringan di kampus. Setiap kali gadis di seberang meja mencoba membuka topik yang lebih pribadi dengan Koita, kamu langsung menimpali atau menyodorkan buku menu, memastikan malam itu berakhir sebagai kumpul bertiga yang biasa."
        else:
            nar "Kamu membiarkan Koita menuruni tangga dan berjalan hingga tepat di bawah tiang lampu taman. Persis saat Koita berhenti di depan bangku kayu dan gadis yang menunggunya baru menarik napas hendak memulai percakapan, kamu mempercepat langkah lalu menepuk ringan bahu Koita dari samping."
            yutaka "Hei, Koita! Jalannya cepat amat, nggak nungguin dari tadi? Wah, kebetulan banget, kamu masih di kampus juga?"
            nar "Kalimat yang sudah disiapkan gadis di depan Koita langsung tertahan. Ia mengedipkan mata, menatapmu yang berdiri santai dengan satu tangan di saku mantel tepat di samping Koita. Sementara itu, Koita langsung tersenyum lebar dan bergeser setengah langkah agar kalian bertiga bisa saling berhadapan."
            koita "Lho, Yutaka? Kirain kamu sudah balik ke apartemen duluan tadi. Pas sekali kita ketemu bertiga di sini."
            yutaka "Baru selesai beresin catatan di gedung sebelah. Kalian berdua mau jalan ke arah stasiun? Boleh dong aku ikut gabung, perutku dari tadi sore belum diisi apa-apa nih."
            koita "Ya jelas boleh lah. Gimana kalau kita bertiga sekalian mampir cari makan hangat di kedai dekat stasiun? Kamu nggak buru-buru pulang kan?"
            nar "Koita menoleh ke gadis di hadapannya dengan senyum ramah yang polos, tanpa sedikit pun menyadari bahwa ajakan makan bertiga barusan langsung memotong kesempatan bicara empat mata yang telah dinantikannya. Setelah jeda singkat yang agak canggung, gadis itu mengangguk pelan."
            yutaka "Beres kalau gitu. Ayo jalan sekarang sebelum kedainya keburu penuh sama anak kampus. Eh, Koita, tadi kamu lihat nggak pohon Natal di depan aula utama sudah dinyalain lampunya?"
            koita "Serius? Tadi siang waktu aku lewat kabelnya masih dicek panitia."
            nar "Sepanjang perjalanan menuju stasiun sampai kalian duduk mengelilingi meja kayu di kedai hangat, kamu terus menjaga arus percakapan tetap ringan dan ramai oleh komentar soal ujian akhir dan jadwal libur. Setiap kali gadis di seberang meja tampak ingin mengarahkan pembicaraan berdua dengan Koita, kamu menimpali dengan santai atau menawarkan camilan di tengah meja, menjaga pertemuan itu tetap berjalan sebagai obrolan bertiga hingga bubar."
    return

# ┌─ PANDUAN CERITA · N11 · Ditinggal di Rumah
# │ LOKASI  : Hunian Biasa · Rumah Sakurajima
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : ia tidak ikut Kansai.
# │ INTI    : A kirim kabar / B abaikan / C cerita bohong.
# │ AKHIRAN : jeal naik.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N11:
    call kk_scene_enter("nagisa", "Rumah Sakurajima · Ditinggal")
    nar "Foto rombongan Kansai masuk ke grup ketika Nagisa sedang menunggu bahan maket mengering. Ia memperbesar gambar, menutupnya, lalu membuka lagi saat pesan berikutnya datang."
    nagisa "Ramai juga. Aku nggak ikut, jadi nggak tahu apa yang harus dikomentari. Kalau cuma tulis seru ya, terdengar kesal, nggak?"
    nar "Ia mengirimkan pertanyaan itu kepadamu secara pribadi, lalu buru-buru menambahkan bahwa ia punya banyak pekerjaan dan tidak sedang menunggu."
    call kk_family_menu("N11", ["Kirim kabar untuknya dari perjalanan.", "Abaikan saja.", "Karang cerita agar ia tak cemburu."])
    if _return == "A":
        nar "Kau mengirim kabar yang sungguh terjadi dan menanyakan pekerjaan studionya. Nagisa membalas dengan foto maket, lengkap dengan keluhan yang tidak sempat dimasukkan ke grup."
        nagisa "Terima kasih. Aku nggak minta diajak lewat layar terus. Cuma senang masih boleh punya cerita meski nggak ada di foto."
        nar "Setelah itu ia kembali bekerja. Kabar singkatmu memberinya tempat tanpa mengharuskan perjalananmu berhenti untuk menenangkan setiap takutnya."
    elif _return == "B":
        nar "Kau tidak membalas selama perjalanan. Di grup Nagisa tetap muncul sesekali dengan komentar singkat, semakin berhati-hati agar tidak terdengar menuntut perhatian."
        nar "Ketika pulang, kau bertanya bagaimana tugasnya. Ia mengatakan selesai dan tidak menunjukkan foto yang sudah disiapkannya. Ada bagian dari hari-harinya yang kini ia simpan karena mengira kau telah memilih tidak ingin tahu."
    else:
        nar "Kau mengarang cerita untuk membuat perjalanan itu terdengar kurang menyenangkan dan kurang dekat dengan siapa pun. Nagisa menghiburmu, mengatakan lain kali ia akan mengajakmu bermain supaya liburmu tidak sia-sia."
        nar "Kau menerima perhatian yang diberikan kepada versi palsu dari malammu. Foto dan cerita orang lain belum berhenti beredar; kelak ia mungkin mengingat betapa tulus ia mencoba menenangkan sesuatu yang tidak pernah terjadi."
    return

# ┌─ PANDUAN CERITA · N12 · Hujan Deras: Nagisa Menyelamatkan
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : ia menolong Chiasa/pemain lalu mengomel.
# │ INTI    : A berterima kasih / B menjauh / C peluk.
# │ AKHIRAN : hubungan dengan Chiasa.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N12:
    call kk_scene_enter("nagisa", "Gedung Arsitektur · Hujan deras")
    play sound "audio/sfx/rain.wav"
    nar "Nagisa muncul dengan payung tepat ketika kau bersiap menerobos hujan. Ia menarik ujung tasmu ke bawah atap, kemudian memberimu handuk kecil sambil mengomel tentang orang yang memperlakukan demam sebagai rencana akhir pekan."
    nagisa "Pakai. Bukan koleksi pameran, nggak perlu dilihat dulu. Rambutmu menetes ke mana-mana."
    nar "Satu bahunya sendiri basah karena payung tadi lebih banyak menutupimu. Ia tampak baru sadar ketika kau melihatnya."
    call kk_family_menu("N12", ["Berterima kasih dengan tulus.", "Menjauh dan merasa canggung.", "Peluk ia sebagai ucapan terima kasih."])
    if _return == "A":
        nar "Kau mengucapkan terima kasih tanpa mengejek caranya khawatir. Nagisa menarik sisi payung untuk menyembunyikan wajah."
        nagisa "Iya. Sama-sama. Lain kali bawa sendiri, tapi kalau lupa... jangan lari begitu saja. Cari aku dulu kalau ada."
        nar "Ia mengoreksi tawaran itu dengan cepat, mengatakan siapa saja yang punya payung juga boleh. Kau sudah mendengar nama yang pertama ia tawarkan."
    elif _return == "B":
        nar "Kau memberi jarak karena canggung. Nagisa berhenti merapikan ujung handuk dan menurunkan tangan."
        nagisa "Aku cuma nggak mau kamu sakit. Kalau terlalu dekat, bilang."
        nar "Ia memegang payung lebih lurus, menyisakan ruang di antara kalian. Perhatian yang tadi bergerak spontan kini harus mencari bentuk yang tidak membuatnya merasa telah ditolak sebagai orang."
    else:
        nar "Kau membuka tangan, menunggu reaksinya sebelum mendekat. Nagisa terpaku, lalu mengangguk kecil seolah takut gerakan besar akan terlihat semua orang."
        nagisa "Sebentar saja. Handuknya nanti jatuh."
        nar "Ia membalas pelukan dengan satu tangan yang bebas. Sesudah kalian menjauh, omelannya kembali, tetapi tidak lagi cukup lancar untuk menutupi senyum yang terus muncul."
    return

# ┌─ PANDUAN CERITA · N13 · Konfrontasi Yukata
# │ LOKASI  : Kampus Kouseikan · Gedung Arsitektur
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : ia menghadapi rival.
# │ INTI    : A mendukung / B melerai / C memihak Chiasa.
# │ AKHIRAN : konflik terbuka.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N13:
    call kk_scene_enter("nagisa", "Gedung Arsitektur · Konfrontasi Yukata")
    nar "Sebuah sindiran tentang siapa yang memakai yukata agar diperhatikan membuat Nagisa berhenti di depan stan. Orang yang mengucapkannya tersenyum, mencoba mempertahankan perlindungan bahwa itu hanya bercanda."
    nagisa "Kalau mau bilang sesuatu, bilang jelas. Jangan mengandalkan aku yang terlihat galak supaya kamu selalu bisa pura-pura nggak sengaja."
    nar "Ia benar-benar marah, sekaligus sadar orang-orang mulai menonton. Matanya menemukanmu di antara mereka."
    call kk_family_menu("N13", ["Dukung Nagisa terang-terangan.", "Lerai keduanya.", "Memihak dan bicara sebagai Chiasa."])
    if _return == "A":
        nar "Kau mendukungnya menolak sindiran tersebut, tidak ikut menertawakan atau memintanya menjadi pihak yang mengalah agar suasana enak. Nagisa menarik napas, terkejut karena tidak perlu membela dirinya sendirian."
        nagisa "Aku cuma mau dia berhenti. Bukan minta semua orang setuju aku menyenangkan."
        nar "Sesudah orang itu mundur, ia berterima kasih tanpa memalingkan wajah."
    elif _return == "B":
        nar "Kau melerai dan meminta keduanya memberi ruang. Nagisa memprotes karena mengira ia kembali dipaksa menanggung kesalahan agar keramaian segera tenang."
        nagisa "Aku mau pergi. Tapi jangan bilang kami sama-sama bercanda. Aku nggak bercanda waktu bilang tersinggung."
        nar "Ia bersedia menjauh setelah itu didengar. Kalian berjalan lebih pelan sampai tangannya berhenti gemetar."
    else:
        chiasa "Aku dengar yang kamu katakan. Menyebutnya bercanda nggak membuat Nagisa wajib tertawa."
        nar "Nagisa menatap Chiasa, lupa sesaat bahwa sepanjang sore mereka saling bersaing tentang banyak hal kecil. Orang yang menyindir kehilangan tempat bersembunyi di balik permusuhan mereka."
        nagisa "Kamu... iya. Terima kasih. Aku kira kamu bakal senang melihatku kesal."
        nar "Ketika kalian pergi, jarak di antara dua saingan lama itu tidak sekeras sebelumnya."
    return

init 1 python:
    _hook("K07-A", lambda: kk_flag("matsuda_sekutu"))
    _hook("K07-B", lambda: kk_flag("matsuda_lawan"))
    _hook("K07-C", lambda: kk_rel("koita","trust",4))
    _hook("K08-A", lambda: (kk_flag("koita_natal_diintersep"), kk_koita_suspect(5)))
    _hook("K08-B", lambda: (kk_flag("koita_natal_diambil"), kk_koita_suspect(8)))
    _hook("K08-D", lambda: kk_rel("koita","jeal",5))
    _hook("N11-A", lambda: (kk_rel("nagisa","trust",4), kk_adj("kelekatan_nagisa",5)))
    _hook("N11-B", lambda: kk_rel("nagisa","jeal",8))
    _hook("N11-C", lambda: (kk_rel("nagisa","jeal",5), kk_adj("luka_bohong",8)))
    _hook("N12-A", lambda: kk_rel("nagisa","aff",4))
    _hook("N12-B", lambda: kk_rel("nagisa","trust",-3))
    _hook("N12-C", lambda: (kk_rel("nagisa","intim",6), kk_adj("kelekatan_nagisa",6)))
    _hook("N13-A", lambda: (kk_rel("nagisa","aff",5), kk_adj("gengsi_nagisa",-5)))
    _hook("N13-B", lambda: kk_rel("nagisa","trust",3))
    _hook("N13-C", lambda: (kk_rel("nagisa","intim",4), kk_flag("nagisa_dibela_chiasa")))
