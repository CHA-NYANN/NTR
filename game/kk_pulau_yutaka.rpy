# Grand Bab M17b · Liburan Besar Pulau (4 Hari + Kebocoran Sistem · Q19 Pulau)
# Cabang lengkap Host Yutaka · Agustus Tahun 2 (paralel Host Chiasa, terhubung langsung ke M18).

init python:
    def kk_pulau_yutaka_focus():
        targets = ("nagisa", "miyuki", "harumi", "moeka", "shiori", "chiasa")
        def _score(cid):
            return (kk_rel_get(cid, "intim") * 2
                    + kk_rel_get(cid, "trust")
                    + kk_rel_get(cid, "aff")
                    - kk_rel_get(cid, "fear"))
        return max(targets, key=_score)

    def kk_pulau_yutaka_day2_branch():
        if (kk_get("curiga_chiasa", 0) >= 12 or kk_get("curiga_koita", 0) >= 15
                or kk_has("pulau_hari1_koita")):
            return "chiasa_koita"
        if (stage.get("nagisa", 0) >= 2 or kk_rel_get("nagisa", "jeal") >= 50
                or kk_has("nagisa_dibela_chiasa")):
            return "nagisa_pergoki"
        return "shiori_miyuki"

init 1 python:
    _hook("Y17b_H1-A", lambda: (kk_adj("pulau_kendali", 15), kk_flag("pulau_hari1_kendali")))
    _hook("Y17b_H1-B", lambda: (kk_rel("koita", "aff", 4), kk_rel("koita", "intim", 3), kk_rel("nagisa", "jeal", 3), kk_flag("pulau_hari1_koita")))
    _hook("Y17b_H1-C", lambda: (kk_adj("pulau_waspada", 15), kk_rel("shiori", "trust", 3), kk_flag("pulau_hari1_amati")))

    _hook("Y17b_H2-A", lambda: (kk_adj("pulau_jujur", 15), kk_koita_suspect(-3), kk_flag("pulau_hari2_jujur")))
    _hook("Y17b_H2-B", lambda: (kk_adj("pulau_risiko", 20), kk_koita_suspect(6), kk_flag("pulau_manuver_alkohol")))
    _hook("Y17b_H2-C", lambda: (kk_adj("pulau_waspada", 15), kk_koita_fear(4), kk_flag("pulau_catat_celah_sistem")))

    _hook("Y17b_H3-A", lambda: (kk_adj("pulau_jujur", 15), kk_adj("respek_shiori", 4), kk_flag("pulau_hari3_lindungi")))
    _hook("Y17b_H3-B", lambda: (kk_adj("pulau_risiko", 20), kk_koita_suspect(6), kk_flag("pulau_hari3_pisah")))
    _hook("Y17b_H3-C", lambda: (kk_adj("pulau_intim", 15), kk_flag("pulau_hari3_berdua")))

    _hook("Y17b_H4-A", lambda: (kk_flag("sistem_celah_tercatat"), kk_flag("q19_complete")))
    _hook("Y17b_H4-B", lambda: (kk_adj("pulau_intim", 10), kk_flag("q19_complete")))
    _hook("Y17b_H4-C", lambda: (kk_adj("pulau_waspada", 10), kk_flag("meisa_diperingatkan_pulau"), kk_flag("q19_complete")))


# ══════════════════════════════════════════════════════════════════════════
# HARI 1 · Dermaga Feri & Vila Pulau — Semua Rute Bertemu (Host Yutaka)
# ══════════════════════════════════════════════════════════════════════════
label kk_pulau_yutaka_hari1(_focus):
    call kk_scene_enter("yutaka", "Dermaga Penyeberangan · Hari 1 Pulau")
    nar "Rencana liburan empat hari di pulau selatan yang ramai disusun sejak awal Agustus akhirnya tiba juga. Aroma garam laut, deru mesin kapal feri, dan terik matahari siang menyambut ketika rombongan kalian berkumpul di depan gerbang dermaga."
    "Petugas Feri" "Penumpang tujuan Pulau Minami jalur siang, harap menyiapkan tiket penyeberangan! Kapal berangkat sepuluh menit lagi!"
    nar "Kamu menyesuaikan letak tas sandang kulitmu di bahu sambil melirik jam tangan bertali kulit di pergelangan kiri. Dari posturmu yang lebih tinggi di antara antrean, seluruh lingkaran yang selama ini mengorbit di sekitar Koita terlihat berkumpul dalam satu titik."
    koita "Semua tiket sudah siap di tangan kan? Yutaka, kotak pendingin ini berat banget, pegang satu sisi dong sebelum bahuku copot duluan."
    if kk_has("koita_arah_bl") or kk_has("koita_ditawari_nama"):
        nar "Begitu kamu maju selangkah meraih gagang kotak pendingin di sisi yang sama hingga punggung tangan kalian nyaris bersentuhan, Koita refleks menarik jarinya setengah langkah dengan ujung telinga langsung memerah."
        koita "H-hei, pegang sisi satunya! Nggak usah berdiri sedekat itu di tengah dermaga ramai begini!"
        yutaka "Kamu sendiri yang barusan minta tolong pegang, Koita. Santai saja, kotaknya nggak bakal jatuh."
        koita "Terserah! Pokoknya jalan duluan sana!"
    else:
        yutaka "Sudah kubilang jangan masukin es batu dua kantong penuh sebelum naik kapal, Koita. Sini biar kubantu sampai dek atas."
    chiasa "Dasar Ko-nii, setiap kali mau pergi jauh selalu bawaannya paling ribet sendiri. Yutaka-kun juga jangan terlalu memanjakan dia, nanti kebiasaan."
    nar "Chiasa berdiri di samping kakaknya dengan rambut cokelat gelap terikat setengah berpita hitam dan tas sketsa tipis di pundaknya. Matanya yang kuning keemasan melirikmu sebentar."
    if kk_get("curiga_chiasa", 0) >= 12:
        nar "Senyumnya tetap ringan, tetapi cara matanya menakar gerakanmu terasa lebih saksama dibandingkan dulu, seolah ia masih mengingat celah aneh dari caramu berbicara belakangan ini."
    moeka "Wah, akhirnya sampai dermaga juga! Yutayuta, kemejamu rapi banget sih buat ke pulau, nanti kalau kena cipratan ombak jangan ngomel ya!"
    if kk_has("beasiswa_terancam"):
        nar "Suara Moeka terdengar riang, tetapi ada bayangan tipis di bawah matanya. Begitu ponselnya bergetar singkat di genggaman, senyumnya sempat turun sesaat."
        moeka "Eh... pesan dari Ryena. Katanya foto sesi kerja kemarin di studio Kuga mau dipakai buat unggahan promosi lebih awal. Nanti saja kubalas habis sampai vila, aku mau liburan dulu!"
    elif kk_has("moeka_intervensi_1"):
        nar "Saat melihatmu, senyum Moeka melunak lebih lega. Ia sempat menyinggung pelan bahwa Ryena baru mengirim kabar soal foto promosinya dari studio Kuga yang ternyata sudah mulai naik daring tanpa menunggunya mengecek keterangan gambar."
        moeka "Semoga saja keterangannya rapi ya, Yutayuta. Aku malas banget kalau balik ke kampus malah ditanya aneh-aneh."
    else:
        moeka "Oh iya, tadi Ryena sempat chat bilang foto proyek desain yang kutangani di studio Kuga katanya sudah mulai diunggah sebagian. Nanti malam saja kubuka, sekarang waktunya lihat laut!"
    miyuki "Moeka-chan hati-hati melangkah di dekat tepi dermaga. Aku sudah menyiapkan obat mabuk laut dan plester di tas kalau ada yang pusing di kapal."
    nar "Miyuki berdiri dengan rambut hitam panjang lurus terurai di atas kardigan tipisnya. Matanya yang cokelat kemerahan melirikmu dengan tenang."
    if stage.get("miyuki", 0) >= 3 or kk_has("miyuki_rasa_salah_dimanfaatkan"):
        miyuki "Yutaka-kun, catatan yang kemarin sudah kubawa salinannya kalau kamu masih perlu. Maaf kalau aku belum sempat merapikan bagian lampiran akhirnya, nanti malam di vila bisa kuberikan."
        yutaka "{i}Bahkan saat sudah berdiri di dermaga liburan, ia masih membawa rasa takut mengecewakan ke dalam kopernya.{/i}"
    else:
        miyuki "Yutaka-kun sudah makan siang sebelum ke sini? Kalau belum, aku bawa roti lapis kecil di tas pendingin."
    harumi "Secara teknis, bagian tengah geladak memiliki guncangan paling kecil bagi penumpang yang jarang menyeberang. Saya juga sudah mencatat jadwal pasang surut empat hari ke depan."
    nar "Harumi membetulkan bingkai kacamatanya, kepang samping abu-abu perak berjepit mawar merahnya bergerak ringan ditiup angin. Jika kamu menoleh padanya, ia mengangguk sopan."
    if kk_has("harumi_dimanfaatkan"):
        nar "Ia sempat diam setengah detik di dekatmu, seolah menunggu kepastian apakah kamu ingin ia duduk di deretan kursi tertentu."
    shiori "Kuroiwa-san sudah mengatur pengantaran seluruh koper kita langsung dari dermaga pulau menuju vila. Jadi kita tidak perlu berebut gerobak bagasi begitu turun nanti."
    nar "Shiori melangkah mendekat bersama angin laut yang menggerakkan rambut putih keperakan berhiasan mutiara ungu-emasnya. Mata ungu ametisnya melirik dingin melewati bahumu menuju antrean belakang."
    if kk_get("daftar_kebohongan_shiori", 0) > 0:
        shiori "Kebetulan yang menarik, Kisaragi-san. Sepertinya ada kenalan satu kampus di belakang antrean yang sejak tadi cukup sibuk mengarahkan ponselnya ke rombongan kita."
    else:
        shiori "Ngomong-ngomong, Kisaragi-san, kita bukan satu-satunya rombongan dari Kouseikan di kapal siang ini."
    nar "Kamu menoleh ke arah antrean belakang. Lima belas meter di sana, Kurosawa Meisa berdiri dengan kacamata hitam naik di rambut sebahunya bersama seorang teman, jelas mengamati mobil yang menurunkan bagasi Shiori sekaligus rombongan Koita."
    "Mahasiswi Wisata" "Enak banget ya jadi keluarga Saionji, ke pulau saja koper sudah diantar staf pribadi. Eh, Meisa, cowok Sastra yang kemarin ramai diomongin di festival juga ikut bareng semua cewek itu?"
    "Kurosawa Meisa" "Sst, jangan lihat langsung. Catat saja dulu, nanti kita lihat seberapa kompak rombongan itu sampai hari pulang."
    yutaka "{i}Kurosawa Meisa ikut di feri yang sama. Ia sudah melirik nama Saionji sekaligus posisi Koita. Satu langkah ceroboh di pulau ini bakal jadi bahan empuk bulan depan.{/i}"
    play sound "audio/sfx/phone_buzz.wav"
    nar "Tepat saat peluit kapal berbunyi, ponsel di saku celanamu bergetar dua kali berturut-turut. Nagisa yang baru berjalan mendekat dari kios minuman dengan twin-tail pirang berpita hitam-pink langsung menghentikan langkahnya melirik saku celanamu."
    if kk_has("nagisa_dibela_chiasa") or kk_rel_get("nagisa", "intim") >= 30:
        nagisa "Ponselmu bunyi terus dari tadi, Yutaka. Siapa sih yang ngirim pesan pas kita sudah di dermaga begini? ...Sudahlah, ini soda dingin buatmu, jangan bilang nggak haus."
    else:
        nagisa "Ponselmu bunyi lagi, Yutaka. Urusan kuliah apa lagi? Ayo cepat naik, nanti kita dapat kursi paling belakang dekat suara mesin!"
    nar "Satu jam penyeberangan membelah laut biru membawa kalian ke vila kayu dua lantai di atas tebing teluk. Aroma kayu pinus dan udara asin langsung menyambut begitu pintu kaca ruang tengah digeser terbuka."
    koita "Akhirnya sampai! Oke, sebelum turun ke pantai, kita bagi kamar sama jadwal belanja makan malam dulu ya. Siapa yang mau ikut turun ke warung pelabuhan?"
    if kk_get("curiga_koita", 0) >= 15:
        nar "Saat menyebut jadwal itu, tatapan Koita sempat berhenti di wajahmu sedikit lebih lama dari biasanya, seolah menakar apakah kamu akan memutar rencananya lagi."
    nar "Seluruh lingkaran sosial kampus kini duduk di bawah satu atap tanpa jarak gedung fakultas. Pilihanmu sore ini mulai membentuk arah empat hari ke depan."
    call kk_family_menu("Y17b_H1", ["\"Biar aku yang urus belanja makan malam bareng salah satu dari kalian, Koita bereskan barang dulu.\"", "\"Koita, ikut aku ke jalan dermaga sebentar beli es batu tambahan sebelum toko tutup.\"", "Menepi ke beranda belakang vila untuk mengamati gerak rombongan dan arah Kurosawa Meisa."])
    if _return == "A":
        yutaka "Biar aku yang turun ke warung pelabuhan ambil bahan makan malam bareng salah satu dari kalian. Koita urus pembagian kamar sama kotak es di dalam saja."
        koita "Eh, beneran nggak apa-apa, Yutaka? Padahal baru sampai vila."
        yutaka "Lebih cepat beres sebelum matahari turun. Lagipula jalannya lumayan adem buat meluruskan kaki."
        nar "Kamu mengambil tas belanja kain dan berjalan menuruni jalan batu menuju warung pesisir bersama orang yang paling dekat denganmu sepanjang perjalanan tadi."
        if _focus == "nagisa":
            $ kk_rel("nagisa", "trust", 4)
            $ kk_rel("nagisa", "intim", 3)
            nagisa "Tumben kamu langsung sigap ambil bagian belanja begini, Yutaka. Biasanya kamu milih duduk di sofa sambil nyuruh Ko-kun yang turun."
            yutaka "Kalau nunggu Koita memutuskan menu makan malam, kita semua baru makan jam sepuluh. Lagipula lebih enak jalan berdua begini daripada ribut di ruang tengah."
            nagisa "H-hmph! Jangan ngomong seenaknya! ...Tapi ya, udaranya di luar memang jauh lebih segar."
            "Penjaga Warung" "Wah, dua tamu dari vila atas ya? Jagung manis sama cumi segarnya baru naik dari perahu, sekalian ambil buat bakar-bakar malam?"
            yutaka "Ambil jagung delapan ya, Oji-san. Nagisa, mau es krim soda sekalian biar nggak cemberut di jalan naik?"
            nagisa "Siapa yang cemberut! ...Iya, ambil yang rasa soda biru satu."
        elif _focus == "miyuki":
            $ kk_rel("miyuki", "trust", 4)
            $ kk_rel("miyuki", "intim", 3)
            miyuki "Terima kasih sudah menawarkan turun bersama, Yutaka-kun. Tadi aku sempat bingung membawa belanjaan tujuh orang naik tangga tebing sendirian."
            yutaka "Selama empat hari di pulau ini, Tachibana-senpai jangan sibuk jadi pengurus dapur sendirian sementara yang lain santai. Aku yang bawa kantong beratnya."
            miyuki "Hehe, nadamu barusan kedengaran tegas banget, Yutaka-kun. Baiklah, aku menurut hari ini."
            "Penjaga Warung" "Silakan, sayuran sama bumbu panggangnya masih lengkap semua!"
            miyuki "Rasanya aneh sekaligus lega juga ada yang langsung membagi tugas tanpa menunggu aku mengeluh dulu."
        elif _focus == "moeka":
            $ kk_rel("moeka", "trust", 4)
            $ kk_rel("moeka", "intim", 3)
            moeka "Untung Yutayuta yang ikut turun! Kalau aku belanja sendiri bisa-bisa uang patungannya habis buat beli cemilan pantai sama minuman lucu."
            yutaka "Kita pegang daftarnya dulu baru beli cemilan di akhir, Kohinata. Oh iya, soal pesan Ryena tentang foto studio Kuga tadi, kamu yakin nggak perlu dicek dulu sekarang?"
            moeka "...Jujur aku agak malas buka sekarang, takut merusak liburan hari pertama. Tapi makasih ya sudah ingat dan nanya pelan-pelan begini, Yutayuta."
            "Penjaga Warung" "Cumi segar dan jagung bakarnya baru keluar dari kotak es, silakan dipilih!"
            moeka "Ambil cumi yang besar itu, Yutayuta! Biar malam ini Kocchi yang kebagian giliran jaga panggangan!"
        elif _focus == "harumi":
            $ kk_rel("harumi", "trust", 4)
            $ kk_rel("harumi", "intim", 3)
            harumi "Langkah yang efisien, Kisaragi-kun. Memisahkan tim belanja dari pembagian kamar memotong waktu tunggu hampir dua puluh menit."
            yutaka "Di pulau ini sesekali tutup dulu buku catatanmu, Kujo-san. Lihat lautnya sebelum matahari turun."
            harumi "Saya tetap mencatat hal yang perlu diingat. Namun... berjalan di jalur pesisir yang tenang seperti ini tidak mengganggu konsentrasi saya. Cukup menyenangkan."
            "Penjaga Warung" "Teh tawar dingin dan bahan panggangan masih segar, silakan!"
            yutaka "Dua teh tawar dingin sekalian buat di jalan naik nanti ya, Oji-san."
        elif _focus == "chiasa":
            $ kk_rel("chiasa", "trust", 4)
            $ kk_rel("chiasa", "intim", 3)
            chiasa "Tumben banget Yutaka-kun yang inisiatif turun belanja duluan. Mau kabur dari suasana ruang tengah, atau memang sengaja mau jalan berdua?"
            yutaka "Dua-duanya kedengaran masuk akal. Lagipula di bawah sini lebih gampang lihat posisi penginapan Kurosawa Meisa tanpa bikin anak-anak panik."
            chiasa "Hm, peka juga. Aku suka cara berpikirmu yang tenang begini, Yutaka-kun."
            "Penjaga Warung" "Silakan, Nona dan Tuan, buah persik dan jagung bakarnya masih segar semua!"
            chiasa "Ambil buah persik buat nanti malam ya, Yutaka-kun. Biar aku yang pilih yang paling manis."
        else:
            $ kk_rel("shiori", "trust", 4)
            $ kk_rel("shiori", "intim", 3)
            shiori "Keputusan yang cermat, Kisaragi-san. Di luar vila kita bisa membicarakan kehadiran Kurosawa Meisa tanpa menimbulkan kepanikan yang tidak perlu."
            yutaka "Di dermaga tadi temannya sempat menyinggung soal mobil keluarga Saionji dan rombongan Koita. Kelihatannya dia memang berniat mencari bahan."
            shiori "Ia selalu mengincar dua hal sekaligus, nama besar dan celah kelengahan. Selama tidak ada adegan ceroboh di depan umum, tulisannya hanya akan menjadi dugaan kosong."
            "Penjaga Warung" "Buah segar dan minuman dinginnya baru masuk, silakan dipilih!"
            shiori "Kita beli buah persik secukupnya. Sisanya kita awasi siapa yang paling cepat kehilangan kendali saat malam tiba."
        nar "Saat kalian kembali mendaki jalan batu menuju vila menjelang senja, kedekatan singkat itu sudah mengubah keseimbangan di ruang tengah sebelum hari kedua dimulai."
    elif _return == "B":
        yutaka "Koita, ikut aku ke toko dekat dermaga sebentar yuk. Es batu di kotak pendingin sudah hampir mencair semua, sekalian beli tambahan minuman dingin."
        koita "Oh, oke! Aku ambil dompet sebentar. Yang lain beres-beres kamar dulu nggak apa-apa ya?"
        nar "Nagisa yang baru menaruh tas di dekat tangga langsung menoleh cepat dengan kening berkerut."
        nagisa "Lho, kalian berdua saja yang turun? Kirain mau belanja bareng-bareng?"
        yutaka "Cuma sepuluh menit kok, Nagisa. Nanti pulangnya kami bawakan es krim buat semua."
        nar "Menuruni jalan setapak kayu menghadap perahu nelayan, angin sore membawa bau asin yang hangat. Di luar keramaian vila, bahu Koita tampak lebih tenang meski tetap menyimpan kegelisahan tipis."
        if kk_has("koita_arah_bl") or kk_has("koita_ditawari_nama"):
            koita "Yutaka... serius deh, kamu ngajak aku turun berdua cuma buat beli es batu, kan? Jangan mulai ngomong aneh-aneh lagi di pulau kayak waktu Valentine kemarin."
            yutaka "Aku beneran mau beli es batu. Tapi kalau kamu langsung teringat Valentine cuma gara-gara jalan berdua denganku, kelihatannya yang pikirannya ke mana-mana malah kamu sendiri, Koita."
            nar "Telinga Koita langsung memerah terang. Ia membuang muka cepat ke arah perahu sambil menggerutu defensif."
            koita "Nggak ada yang mikirin ke sana! Aku cuma... aku cuma nggak mau kamu bikin aku bingung di depan semua teman kita selama empat hari ini!"
            yutaka "Tenang saja. Aku nggak akan bikin kamu malu di depan mereka. Tapi jangan berharap aku pura-pura lupa juga sama apa yang pernah kukatakan."
            nar "Koita menelan ludah, membuka mulut seperti hendak memarahi balik, lalu akhirnya hanya mengembuskan napas panjang dengan bahu sedikit melunak."
            koita "...Menyebalkan banget sih kamu kalau lagi tenang begini. Ayo cepat beli esnya sebelum gelap."
        else:
            koita "Jujur saja, Yutaka... aku senang semua orang bisa ikut ke pulau ini. Tapi sejak kejadian festival kemarin, tiap aku ngobrol lama sama satu orang, aku malah takut orang lain langsung merasa tersisih."
            yutaka "Kalau kamu terus mencoba menyenangkan tujuh orang dalam satu vila tanpa pernah menyebut maumu sendiri, yang paling dulu habis tenaganya ya kamu sendiri, Koita."
            koita "Hehe... dari dulu kamu memang paling nggak suka lihat aku muter-muter ya. Tapi di tempat sempit begini, salah ngomong satu kalimat saja rasanya langsung bikin semua canggung."
        nar "Dari jalan setapak atas, Chiasa yang sempat berdiri di beranda tampak melirik ke arah kalian berdua di pagar dermaga sebelum kembali masuk. Kamu menepuk bahu Koita singkat dan mengajak pulang sebelum senja turun."
    else:
        nar "Alih-alih ikut sibuk berebut pembagian kamar di dalam, kamu mengambil dua kaleng teh dingin dari dapur dan melangkah keluar ke beranda kayu belakang yang menghadap jalan pesisir bawah."
        nar "Dari ketinggian tebing ini, seluruh gerak-gerik terlihat jelas. Di dalam ruang tengah, Koita kewalahan menjawab pertanyaan jadwal pantai dari Moeka dan Nagisa. Di bawah sana, di jalan menuju penginapan keluarga dekat dermaga, Kurosawa Meisa melintas santai sambil mengangkat ponselnya ke arah papan petunjuk pantai."
        shiori "Posisi pengamatan yang strategis, Kisaragi-san. Dari sudut ini jalur menuju penginapan dermaga terlihat tanpa penghalang."
        nar "Kamu menoleh. Shiori melangkah keluar membawa cangkir teh hangat, disusul Chiasa yang ikut berdiri bersandar dekat pintu kaca."
        chiasa "Yutaka-kun juga lagi memperhatikan Kurosawa Meisa di bawah sana?"
        yutaka "Penginapannya cuma lima menit jalan kaki dari tangga pantai vila kita. Kalau ada keributan kecil di luar atau orang yang kelewat mabuk malam-malam, dia nggak perlu repot-repot mencari bahan."
        shiori "Tepat sekali. Di dermaga tadi temannya sudah menyebut nama keluarga saya sekaligus nama kakakmu, Amamiya-san. Ia sedang mengumpulkan potongan cerita untuk semester baru."
        chiasa "Kalau begitu kita jangan sampai kasih dia tontonan gratis empat hari ini. Yutaka-kun, kasih kode kalau lihat dia terlalu dekat ke jalur vila ya."
        yutaka "Beres. Kita awasi sama-sama."
        nar "Shiori mengangguk dengan sorot tenang yang penuh perhitungan, sementara kamu mencatat posisi lampu pantai dan tangga samping di dalam kepalamu sebelum kembali masuk."
    return


# ══════════════════════════════════════════════════════════════════════════
# HARI 2 · Pesta Pantai, Alkohol, & KEBOCORAN SISTEM (Q19 Pulau · Host Yutaka)
# ══════════════════════════════════════════════════════════════════════════
label kk_pulau_yutaka_hari2(_focus):
    $ _d2 = kk_pulau_yutaka_day2_branch()
    call kk_scene_enter("yutaka", "Beranda Vila Pulau · Malam Hari 2")
    $ kk_bgm("night")
    nar "Seharian penuh di bawah matahari pantai dan suara ombak akhirnya berganti malam yang lembap di atas teluk. Lampu gantung kuning di beranda vila menyala terang di atas panggangan arang yang membara."
    nar "Meja kayu panjang penuh oleh piring jagung bakar, cumi saus kecap, minuman ringan, serta beberapa kaleng minuman buah beralkohol rendah. Hawa hangat pesisir membuat tawa dan obrolan meluncur jauh lebih bebas daripada di kantin kampus."
    moeka "Ayo bersulang dulu! Buat liburan tahun ketiga sebelum tugas berat dan magang mulai bikin pusing kepala!"
    nagisa "Moeka-san, minumnya pelan-pelan dong, baru setengah kaleng mukamu sudah merah begitu."
    miyuki "Makan dulu jagung dan dagingnya ya supaya perut tidak kosong. Ini, Yutaka-kun, aku sisihkan yang bumbunya nggak terlalu manis."
    harumi "Secara fisiologis, lelah berenang mempercepat reaksi alkohol meski kadarnya rendah. Saya tetap memilih teh tawar dingin."
    chiasa "Ko-nii, penjepit cadangannya jatuh ke kolong meja! Tolong ambilkan yang baru di dapur dalam dong."
    koita "Iya, sebentar kuambilkan di rak dapur."
    nar "Beberapa menit kemudian rombongan terpencar santai antara ruang tengah dan teras. Koita belum juga kembali dari dalam, sementara suara tawa Moeka yang sempat mengecek pesan singkat dari Ryena terdengar agak terburu-buru di ujung meja."
    moeka "Eh, bentar ya, Ryena kirim tautan katalog foto dari studio Kuga... duh, kenapa fotoku dipasang paling depan sih? Sudahlah, besok saja kuurus!"
    $ kk_bgm("system")
    play sound "audio/sfx/system_open.wav"
    nar "Saat kamu melangkah ke sudut gelap dekat tangga samping untuk mencari angin sejuk, bunyi statis tajam menyambar telingamu. Panel kaca biru neon membuka diri tepat di ruang pandangmu."
    sistem "( ´ v ` )/ Malam yang malas sekali, Sampah Peron~ Kau cuma berdiri memegang kaleng dingin di tengah empat hari emas begini? Ini misi khusus buatmu, Quest Pulau."
    sistem "Radar naskahku baru mendeteksi momen empuk di ujung dermaga kayu bawah. Sepuluh menit lagi Koita bakal turun sendirian ke bangku lampu pantai menemui salah satu target yang lagi goyah, dan jalur bawah kosong tanpa satu saksi pun."
    sistem "Turun lewat tangga samping sekarang dan potong jalurnya sebelum mereka mulai bicara. Angka penyimpanganmu bakal melonjak bersih~ (^_~)-*"
    play sound "audio/sfx/system_close.wav"
    nar "Panel cahaya itu padam seketika, menyisakan denyut dingin di pelipismu dan dorongan kalkulasi yang memaksa kakimu bergerak cepat."
    yutaka "{i}Jalur bawah kosong tanpa saksi, dan Koita turun sepuluh menit lagi. Kalau aku bisa mengunci momen ini sebelum terjadi, banyak hal di semester depan jadi lebih mudah.{/i}"
    $ kk_bgm("tension")
    play sound "audio/sfx/footsteps.wav"
    nar "Kamu menuruni tangga kayu tebing samping vila dengan langkah ringan, menyusuri semak pantai menuju lampu tiang tunggal di ujung dermaga bawah. Suara ombak makin keras menampar tiang kayu."
    nar "Namun tepat tiga langkah sebelum bangku kayu di bawah lampu, langkahmu terhenti mendadak di atas pasir."
    nar "Keadaan di bawah lampu tiang itu meleset total dari laporan yang baru saja dibocorkan Sistem."
    if _d2 == "chiasa_koita":
        nar "Tidak ada satu pun heroine yang menunggu Koita sendirian. Di bawah lampu dermaga, Koita justru sedang berbicara pelan bersama Chiasa dengan ekspresi serius, sementara dua puluh meter di belakang tembok penginapan dekat tiang listrik, layar ponsel Kurosawa Meisa berkedip pelan mengarah ke dermaga."
        chiasa "...Aku serius, Ko-nii. Belakangan ini cara Yutaka-kun merespons omongan orang terasa jauh lebih dingin dan terhitung. Kadang aku merasa kayak orang yang berdiri di sebelah kita sekarang berbeda dari Yutaka-kun yang dulu."
        koita "Aku juga beberapa kali merasa aneh, Chi-chan. Apalagi sejak kejadian festival minggu lalu..."
        nar "Ranting kering patah nyaring di bawah sol sepatumu. Kedua saudara tiri itu langsung serempak menoleh tajam ke arah semak gelap tempatmu berdiri."
        chiasa "Yutaka-kun...? Kamu berdiri di situ sejak kapan?"
        nar "Dari sudut matamu, bayangan Kurosawa Meisa di pos jalan pelabuhan langsung bergerak cepat menjauh sambil mengantongi ponselnya. Rahangmu mengeras. Intel Sistem benar-benar meleset dan justru menyeretmu masuk ke tengah percakapan paling berbahaya."
    elif _d2 == "nagisa_pergoki":
        nar "Koita sama sekali tidak ada di dermaga bawah. Yang duduk sendirian di bangku kayu sambil memeluk lutut adalah Nagisa, dengan pipi agak memerah oleh angin laut dan satu kaleng minuman buah dari beranda tadi."
        nar "Begitu mendengar langkah sepatumu yang cepat di papan dermaga, Nagisa langsung berdiri kaget. Matanya yang biru cerah menyapu sosokmu yang turun dari tangga gelap, lalu turun menatap layar ponsel di tanganmu yang baru saja menyala oleh notifikasi grup."
        nagisa "Yutaka?! Kamu ngapain turun mengendap-endap lewat tangga gelap sambil lihat layar ponsel jam segini?! Kamu janjian sama seseorang di bawah, atau nyari Ko-kun?!"
        nar "Suaranya yang melengking kaget memantul di atas permukaan air yang sunyi. Di jalan setapak atas menuju penginapan pantai, dua siluet termasuk Kurosawa Meisa berhenti melangkah dan menoleh ke bawah mendengar suara Nagisa."
        nagisa "Kok kamu diam saja?! Mukamu jelas kaget waktu lihat cuma aku yang duduk di sini!"
        nar "Dadamu terasa turun dingin. Tidak ada pertemuan rahasia Koita di sini; intel Sistem usang total, dan kamu baru saja tertangkap di posisi paling mencurigakan tepat di depan Nagisa."
    else:
        nar "Koita sama sekali tidak ada di bawah lampu dermaga. Yang duduk di bangku kayu menghadap laut gelap justru Shiori dan Miyuki yang berbicara pelan sambil memegang dua cangkir teh hangat."
        miyuki "...Makanya kadang aku bingung, Saionji-san, apakah aku terlalu sering mengiyakan permintaan orang sampai lupa menjaga tenagaku sendiri."
        shiori "Langkah paling penting memang membedakan siapa yang tulus peduli dan siapa yang hanya memanfaatkan rasa bersalahmu, Tachibana-senpai."
        nar "Ujung sepatumu tergelincir sedikit di atas papan kayu yang licin oleh embun laut, menimbulkan bunyi gesekan keras. Shiori langsung memutar kepala dengan sorot ungu ametis yang tajam, sementara Miyuki tersentak kaget."
        shiori "Kisaragi-san? Tangga tebing samping agak terlalu gelap untuk sekadar mencari angin. Kamu sedang mencari seseorang, atau baru saja mendengarkan obrolan kami?"
        nar "Di ujung jalan masuk dermaga di belakangmu, kilatan kecil layar ponsel milik Kurosawa Meisa yang melintas menuju penginapannya sempat terlihat jelas sebelum ia hilang di tikungan. Intel Sistem benar-benar salah alamat dan menjebakmu di ruang paling terbuka."
    $ kk_bgm("system")
    play sound "audio/sfx/system_open.wav"
    nar "Di sudut pandangmu, jendela kaca biru kecil berkedip setengah transparan hanya untuk matamu sendiri. Emotikonnya menguap lebar tanpa sedikit pun rasa bersalah."
    sistem "(¬_¬ ) Oh, salah tebak ya? Rupanya salinan data alur yang kubaca tadi masih versi dua bulan lalu sebelum pilihan-pilihanmu mengacak jadwal mereka. Salahmu sendiri menelan mentah-mentah tanpa cek ulang, Sampah Peron~"
    sistem "Jangan memelototiku begitu. Aku pengawas kontrak, aku sama sekali tidak wajib minta maaf kalau bidakku terpeleset sendiri di dermaga."
    play sound "audio/sfx/system_close.wav"
    $ kk_flag("sistem_kebocoran_pulau")
    $ kk_adj("nyeri_sistem", 8)
    $ kk_bgm("tension")
    yutaka "{i}Bajingan. Data Sistem ternyata bisa usang karena perubahan yang kubuat sendiri, dan ia bahkan tidak peduli aku rugi di lapangan. Sekarang aku yang harus membereskan kekacauan di depan mataku.{/i}"
    call kk_family_menu("Y17b_H2", ["Hadapi langsung dengan jujur tanpa mengarang alasan, sambil menyimpan catatan soal kesalahan Sistem.", "Gunakan suasana pesta dan minuman di beranda untuk membalik topik serta menggeser sorotan ke Koita.", "Tarik diri cepat ke dalam vila sebelum makin panjang, lalu bedah celah data Sistem sendirian."])
    if _return == "A":
        $ store.sikap_sistem["selidik"] = store.sikap_sistem.get("selidik", 0) + 1
        nar "Kamu menarik napas dalam di udara laut yang dingin, menelan rasa kesal terhadap layar biru yang baru padam, lalu melangkah penuh ke bawah cahaya lampu tiang agar wajahmu terlihat jelas."
        if _d2 == "chiasa_koita":
            $ kk_suspect("chiasa", -3)
            $ kk_rel("chiasa", "trust", 4)
            yutaka "Aku baru turun dua menit lalu cari udara dari asap panggangan, lalu dengar kalian menyebut namaku. Aku nggak niat menguping, tapi kalau kalian merasa caraku bicara berubah, tanya langsung saja di depanku daripada menebak di dermaga gelap begini."
            nar "Koita terdiam kaku sambil menurunkan tangan dari tengkuknya. Chiasa menatap matamu dua detik penuh, lalu bahunya sedikit mengendur melihat kamu tidak mencoba berkelit dengan lelucon palsu."
            chiasa "...Maaf, Yutaka-kun. Bukan maksudku membicarakanmu di belakang. Cuma belakangan beberapa responmu memang bikin aku penasaran."
            koita "Iya, maaf, Yutaka. Ayo kita naik saja, tadi di jalan atas kelihatan Kurosawa Meisa lewat, nggak enak kalau obrolan kita jadi bahan lihatan."
            yutaka "Oke. Kita naik bareng."
        elif _d2 == "nagisa_pergoki":
            $ kk_rel("nagisa", "trust", 4)
            $ kk_rel("nagisa", "jeal", -5)
            yutaka "Aku nggak lagi janjian sama siapa pun di sini, dan pesan barusan cuma notifikasi grup kelas. Aku turun karena mengira ada yang ketinggalan barang di dermaga, ternyata kamu sendirian di sini. Maaf bikin kaget, Nagisa."
            nar "Nagisa mengerjap cepat, kemarahan defensif di bahunya perlahan turun melihat wajahmu yang tenang tanpa sedikit pun nada meledek."
            nagisa "Hah? Cuma... cuma itu? Kamu nggak bakal ngeledek aku kabur sendirian dari beranda?"
            yutaka "Buat apa? Kalau di atas terlalu berisik, duduk sini lima menit juga nggak masalah. Kutemani sebentar baru kita naik bareng."
            nagisa "...Ya sudah. Duduk situ saja, jangan mulai ceramah."
        else:
            $ kk_rel("shiori", "trust", 4)
            $ kk_rel("miyuki", "trust", 4)
            yutaka "Maaf mengagetkan, Saionji-san, Tachibana-senpai. Asap panggangan di atas cukup pekat jadi aku turun cari angin, dan baru sadar kalian duduk di bangku ini waktu sepatuku selip. Aku sama sekali tidak berniat menguping."
            nar "Shiori menilai ekspresimu dua detik penuh tanpa berkedip, mencari tanda kebohongan, lalu menurunkan ketegangan di bahunya perlahan."
            shiori "Penjelasan yang cukup lugas, Kisaragi-san. Lagipula obrolan kami hampir selesai. Sebaiknya kita naik bersama, tadi saya melihat Kurosawa Meisa melintas di jalan atas."
            miyuki "Iya, angin malamnya juga makin kencang. Ayo naik bareng, Yutaka-kun."
        nar "Kerugian akibat jebakan data usang malam ini berhasil kamu tahan sebelum melebar, sementara satu kesadaran tajam menancap kuat di kepalamu bahwa Sistem tidak memegang kendali mutlak atas perubahan di lapangan."
    elif _return == "B":
        $ store.deviasi += 4
        nar "Alih-alih mengakui salah langkah, kamu memasang senyum miring santai yang terlalu mulus, memutar ketegangan seperti obrolan ringan di pesta."
        if _d2 == "chiasa_koita":
            yutaka "Serius amat pembahasannya di dermaga gelap begini? Koita, kamu kebanyakan minum kaleng buah di atas sampai ikut mengarang teori aneh-aneh? Yuk naik, di teras Kohinata sama Nagisa ribut nanyain kenapa ambil penjepit saja sampai setengah jam."
            koita "Aku nggak mabuk, Yutaka... dan tadi itu sama sekali bukan soal penjepit."
            nar "Kamu tertawa ringan dan melangkah mendahului mereka kembali ke beranda terang, segera mengangkat kaleng dingin dan melemparkan candaan soal Koita yang kabur dari panggangan."
            moeka "Lho, Kocchi beneran turun ke pantai?! Jagungnya hampir gosong semua tahu!"
            nagisa "Iya, bilang cuma ke dapur sebentar, tahu-tahu malah menghilang!"
            nar "Di tengah suasana beranda yang longgar oleh minuman buah, seluruh sorotan berbalik menyudutkan Koita sampai ia salah tingkah, sementara Chiasa berdiri di tepi pintu kaca mengamati manuvermu dengan alis berkerut tajam."
        elif _d2 == "nagisa_pergoki":
            yutaka "Lho, kenapa kamu malah curiga ke aku, Nagisa? Bukannya barusan Koita yang pamit ke dapur lalu menghilang entah ke mana? Aku turun justru mau ngecek dia kabur dari tugas jaga panggangan atau nggak."
            nagisa "Tunggu dulu... Ko-kun menghilang dari atas?! Jangan bilang dia jalan sendiri ke pantai sebelah!"
            nar "Dengan satu lemparan enteng dan sisa efek minuman buah dari teras, seluruh rasa curiga Nagisa langsung meleset darimu dan menghantam Koita. Kalian naik kembali tepat saat Koita baru muncul dari ruang tamu, memicu rentetan pertanyaan tajam Nagisa di depan rombongan."
            koita "Eh, bentar, aku cuma angkat telepon sebentar di dalam kok, kenapa semua jadi lihat ke sini?"
            nar "Di luar pagar taman bawah, langkah Kurosawa Meisa melambat sebentar mendengar suara perdebatan dari teras yang terang, sementara sorot mata Koita menoleh penuh curiga langsung ke arahmu."
        else:
            yutaka "Maaf bikin kaget. Di atas tadi Koita tiba-tiba hilang dari panggangan sementara anak-anak mulai agak pusing minum kaleng buah, jadi kukira dia turun ke dermaga. Ternyata Saionji-san sama Tachibana-senpai."
            shiori "...Kamu memakai nama sahabatmu terlalu cepat untuk seseorang yang turun lewat tangga gelap, Kisaragi-san."
            nar "Kamu membalas dengan senyum tenang tanpa goyah, mengajak mereka naik lalu menghidupkan lagi obrolan teras sambil menyinggung betapa seringnya Koita menghilang di saat semua orang menunggu."
            miyuki "Eh, Yutaka-kun, jangan ikut minum terlalu cepat juga, nanti besok pusing..."
            nar "Tawa beranda kembali berisik oleh obrolan setengah mabuk, sementara Shiori tidak menyentuh minumannya sedikit pun dan mencatat satu garis baru dalam diam saat melihat Koita makin terpojok."
        nar "Kamu lolos dari jebakan data usang Sistem malam ini, tetapi bara baru menyala di bawah atap vila dan gema perdebatan kecil itu merembes sampai ke jalur penginapan bawah."
    else:
        $ store.sikap_sistem["selidik"] = store.sikap_sistem.get("selidik", 0) + 2
        if _d2 == "chiasa_koita":
            $ kk_rel("koita", "trust", -3)
            $ kk_suspect("chiasa", 4)
        elif _d2 == "nagisa_pergoki":
            $ kk_rel("nagisa", "trust", -3)
        else:
            $ kk_rel("shiori", "trust", -3)
        yutaka "Maaf mengganggu. Aku salah ambil jalan waktu cari angin. Aku naik duluan."
        nar "Kamu langsung berbalik sebelum ada yang sempat menahan untuk penjelasan lebih panjang. Panggilan singkat di belakangmu tertelan deru ombak ketika langkahmu menaiki tangga samping menuju kamar lantai dua."
        play sound "audio/sfx/door_close.wav"
        nar "Begitu pintu kayu kamar tertutup rapat dan ruangan kembali hening, kamu duduk di tepi ranjang menatap jendela gelap."
        yutaka "{i}Keluar sekarang. Aku tahu kamu masih memantau.{/i}"
        $ kk_bgm("system")
        play sound "audio/sfx/system_open.wav"
        nar "Udara di depan kaca jendela bergetar pelan, menampilkan jendela kaca biru dengan emotikon menopang dagu yang tampak sedikit kesal."
        sistem "(¬_¬ ) Kau memanggilku cuma buat mengeluh soal sepatumu yang selip di dermaga? Sudah kubilang, salinan naskah aslinya memang bergeser sejak kau mulai mengacak papan."
        yutaka "{i}Berarti radarmu tidak benar-benar bisa membaca masa depan mereka lagi. Setiap kali pilihan kami bergeser, datamu langsung tertinggal di belakang.{/i}"
        nar "Garis cahaya neon pada layar biru itu berkedip patah satu ketukan sebelum kembali menyeringai tajam."
        sistem "( ` v ´ ) Jangan terlalu percaya diri, Manusia. Aku mungkin tidak peduli posisi duduk setiap pion di pantai, tapi jam wisuda dan angka evaluasimu tetap ada di tanganku. Coba saja meleset."
        play sound "audio/sfx/system_close.wav"
        nar "Layar itu menutup cepat, terasa lebih terburu-buru dibandingkan biasanya. Meski malam ini meninggalkan kecurigaan dingin di lantai bawah, kamu baru saja mengantongi satu kelemahan nyata di balik kesombongan Sistem."
    return


# ══════════════════════════════════════════════════════════════════════════
# HARI 3 · Badai Tropis di Vila — Semua Rute Bertabrakan (Host Yutaka)
# ══════════════════════════════════════════════════════════════════════════
label kk_pulau_yutaka_hari3(_focus):
    $ _d3 = kk_pulau_day3_branch()
    $ _fear_cid, _fear_val = kk_pulau_max_fear_heroine()
    call kk_scene_enter("yutaka", "Ruang Tengah Vila Pulau · Badai Hari 3")
    $ kk_bgm("tension")
    play sound "audio/sfx/rain.wav"
    nar "Menjelang sore hari ketiga, awan kelabu tebal menutup langit teluk dengan cepat. Hujan badai tropis mengguyur atap kayu vila hingga bergemuruh, memaksa seluruh rombongan membatalkan rencana pantai dan berkumpul terkurung di ruang tengah."
    nar "Lampu langit-langit berkedip sekali saat guntur berat menggema di kejauhan. Uap teh panas bercampur bau hujan lembap, tetapi tidak ada lagi obrolan ringan seperti hari pertama. Sisa ketegangan malam kedua dan beban yang menumpuk sejak di kota kini duduk bersama di ruangan yang terlalu sempit."
    if _d3 == "distorsi_tekanan":
        nar "Dentingan porselen pecah mendadak memotong keheningan dari arah dapur terbuka. Seluruh ruangan langsung menoleh ke meja konter."
        if _fear_cid == "miyuki" or stage.get("miyuki", 0) >= 3 or kk_has("miyuki_rasa_salah_dimanfaatkan"):
            nar "Miyuki berjongkok tergesa di lantai dapur dengan jemari gemetar memunguti pecahan cangkir, wajahnya pucat sekali dengan mata cokelat kemerahan yang tampak kehabisan tenaga."
            miyuki "Maaf, maaf banget semuanya! Aku ceroboh sampai cangkirnya jatuh berkeping. Nanti aku ganti ke pemilik vila, maaf bikin suasana hujan makin kacau..."
            yutaka "{i}Ujung jarinya hampir menyentuh pinggiran porselen tajam dan ia masih sibuk meminta maaf ke seisi ruangan.{/i}"
            chiasa "Tachibana-senpai, berhenti dulu! Jangan diambil pakai tangan kosong!"
            shiori "Tachibana-senpai, sejak kemarin sore kamu hampir tidak beristirahat karena terus mengerjakan catatan tambahan di kamar. Siapa yang menumpuk pekerjaan di jadwal liburanmu seperti itu?"
            nar "Pertanyaan dingin Shiori jatuh keras di tengah ruang tengah. Tatapan Miyuki sempat melirik cepat penuh cemas ke arahmu sebelum buru-buru menunduk lagi, dan Chiasa langsung menangkap arah pandang itu."
        elif kk_has("beasiswa_terancam"):
            nar "Di samping konter dapur, Moeka terhuyung pelan menahan tubuhnya di tepi meja sambil memegangi pelipis. Di sebelah tasnya berserakan berkas kuliah dan layar ponsel yang menampilkan pesan cemas Ryena soal foto studio Kuga."
            moeka "Eh, maaf semuanya, kepalaku cuma sedikit muter... nggak apa-apa kok, nanti malam aku tetap bisa bantu masak!"
            miyuki "Moeka-chan, bibirmu pucat banget! Kamu belum makan siang dan semalam begadang mengerjakan revisi sambil mikirin pesan dari studio itu ya?"
            shiori "Kamu memaksakan diri ikut liburan sekaligus menanggung ancaman beasiswa dan foto pekerjaan tanpa bicara apa-apa. Kisaragi-san, kamu satu panitia dengannya tahun lalu, bukankah kamu tahu batas kondisinya?"
            nar "Semua mata bergeser di antara Moeka yang memaksa menyalakan senyum ceria dan posisimu di sisi sofa."
        else:
            nar "Di ujung meja makan, Harumi berdiri kaku mencengkeram map catatan yang basah oleh tumpahan teh, napasnya pendek sambil berulang kali menyebut bahwa ia bisa menjadwal ulang segalanya."
            harumi "Kesalahan koordinasi ini tanggung jawab saya. Saya bisa menunda pengiriman berkas riset gelombang pertama bila mengganggu agenda di sini."
            chiasa "Kujo-senpai, tunggu dulu. Kenapa kamu tiba-tiba bahas menunda pendaftaran risetmu di tengah liburan begini?"
            shiori "Menarik. Kujo-san tidak pernah menunda tenggat akademik tanpa dorongan dari luar. Ada seseorang yang memintamu mengubah jadwal?"
            nar "Tatapan Harumi melirik singkat ke arahmu, membuat seisi ruang tengah langsung sunyi selain suara hujan badai di luar kaca."
    elif _d3 == "rumor_curiga":
        play sound "audio/sfx/phone_vibrate.wav"
        nar "Ponsel Moeka dan Nagisa di atas meja rendah bergetar hampir bersamaan. Moeka yang lebih dulu membuka layar langsung memucat."
        moeka "Eh... tunggu. Di forum obrolan mahasiswa ada unggahan foto buram dari dermaga pulau ini semalam. Keterangannya menyebut inisial anak klub Sastra yang bikin banyak orang merasa jadi satu-satunya, terus di komentar bawah ada yang ikut nyeret nama keluarga Saionji sama foto kerjaanku di studio Kuga!"
        nar "Koita langsung membeku dan meraih ponselnya sendiri. Ia menggulir beberapa detik, lalu menurunkan tangan dengan raut tegang dan menatap lurus ke arahmu."
        koita "Di foto ini kelihatan sudut tangga vila kita, dan jam unggahnya tepat habis kejadian dermaga semalam. Ini jelas ulah Kurosawa Meisa yang kita lihat di feri."
        nagisa "Kok dia bisa pas banget mengambil gambar waktu kita ribut di teras?! Tunggu... semalam kan cuma beberapa orang yang turun ke tangga bawah!"
        shiori "Kejadian yang terlalu rapi untuk disebut kebetulan. Kurosawa Meisa sudah melirik nama keluarga saya sejak di dermaga, lalu semalam ada yang turun ke bawah tepat saat ia melintas sebelum keributan naik ke beranda. Kisaragi-san, mungkin kamu mau melengkapi urutan kejadian semalam?"
        nar "Chiasa menyilangkan tangan di dekat jendela, mata kuning keemasannya menatapmu dan Koita bergantian dengan serius sementara hujan memukul kaca makin keras."
    else:
        nar "Ketika lampu ruang tengah meredup sesaat oleh guntur, suasana hening yang tegang menggantung di sekitar meja rendah. Koita meletakkan cangkir tehnya cukup keras dan menatap lurus ke arahmu."
        if kk_has("koita_arah_bl") or kk_has("koita_ditawari_nama"):
            koita "Yutaka... aku nggak tahan diam lagi. Sejak kita sampai pulau ini, kamu bikin semua orang di ruangan ini bergeser arah, terus setiap kali aku bingung dan nanya maksudmu apa, kamu cuma memasang muka tenang seolah aku yang berlebihan!"
            nar "Telinga Koita memerah oleh campuran marah dan kacau, sementara seluruh ruang tengah langsung terdiam kaget melihat Koita meledak kepada sahabat terdekatnya sendiri."
            nagisa "Tunggu dulu, Ko-kun! Kenapa kamu tiba-tiba marah besar ke Yutaka di depan semua orang begini?!"
            chiasa "Ko-nii, pelankan suaramu. Kalau memang ada masalah antara kamu sama Yutaka-kun, nggak usah bikin seisi ruangan kaku begini."
        else:
            koita "Yutaka... aku mau tanya terus terang di sini. Sejak hari pertama di pulau ini, tiap aku mengajak ngobrol, rasanya ada jarak baru di antara kita semua. Bahkan Nagisa dan yang lain lebih sering menoleh ke kamu duluan daripada ikut rencanaku."
            nagisa "Hei, Ko-kun! Kenapa namaku dibawa-bawa? Aku cuma... belakangan ini memang lebih enak ngobrol sama Yutaka daripada harus menebak jadwalmu yang selalu menggantung!"
            nar "Ruangan mendadak sunyi mendengar kalimat Nagisa yang keluar terlalu jujur. Pipinya memerah terang, tetapi ia tidak menarik ucapannya kembali dan justru menoleh ke arahmu menuntut kejelasan."
            chiasa "Sebenarnya sejak festival kemarin kamu sendiri juga berubah banget, Yutaka-kun. Kamu sebenarnya berdiri di pihak siapa di sini?"
        nar "Shiori memperhatikan seluruh meja dari balik cangkirnya, sementara Miyuki dan Harumi sama-sama menahan napas menunggu reaksimu."
    nar "Semua pasang mata di ruang tengah tertuju kepadamu. Hujan badai menutup dermaga pulau sampai besok pagi. Keputusanmu sekarang akan mengunci arah kepulangan besok."
    call kk_family_menu("Y17b_H3", ["Lindungi orang yang paling terdesak dan hentikan tekanan di depan semua orang.", "Manfaatkan kekacauan ini untuk memisahkan Koita dari yang lain dan mengunci narasi versimu.", "Ajak satu orang terdekat keluar ke serambi belakang untuk bicara empat mata dengan jujur."])
    if _return == "A":
        $ store.deviasi += 3
        nar "Kamu berdiri dari sofa dengan gerak tenang dan tegas, memotong lingkaran tatapan yang makin menekan di ruang tengah."
        if _d3 == "distorsi_tekanan":
            $ kk_rel(_fear_cid, "trust", 5)
            $ kk_rel(_fear_cid, "fear", -5)
            yutaka "Berhenti dulu semuanya. Nggak ada gunanya menyidang orang yang jelas-jelas lagi kelelahan di lantai dapur begini."
            nar "Kamu mengambil sapu kecil dan tisu tebal, lalu berlutut menyingkirkan pecahan keramik serta berkas basah sambil menahan tangan yang gemetar itu agar mundur dari pinggiran tajam."
            yutaka "Kalau ada beban tambahan atau jadwal yang bikin pusing selama ini, itu salahku karena nggak ikut menahan dari awal. Sekarang duduk dulu, minum air hangat, nggak ada yang boleh minta maaf satu kali pun lagi malam ini."
            miyuki "...Yutaka-kun..."
            nar "Bahu yang sejak tadi kaku itu akhirnya mengendur dengan tarikan napas pelan. Chiasa segera mengambilkan kain lap kering membantumu, sementara Shiori mengangguk tenang dengan raut lebih lunak."
            shiori "Mengakui bagian tanggung jawab sendiri di depan ruangan jauh lebih terhormat daripada mengarang alasan. Cukup baik, Kisaragi-san."
        elif _d3 == "rumor_curiga":
            $ kk_rel("koita", "trust", 4)
            $ kk_rel("nagisa", "trust", 4)
            yutaka "Kurosawa Meisa sengaja memotong foto gelap dari jarak jauh supaya kelihatan seperti skandal besar. Semalam aku turun ke dermaga cuma karena salah mengira ada orang di bawah, dan kalau kita mulai saling tuduh di ruangan ini, itu persis bahan lanjutan yang dia tunggu buat bulan September."
            nar "Kamu mengetuk pinggir meja dekat ponsel Moeka dengan tenang."
            yutaka "Fotonya bahkan buram tanpa satu pun wajah jelas. Kalau kita kompak nggak membalas komentar anonim di forum itu, pancingannya bakal kehilangan tenaga sebelum kapal pulang besok. Soal foto studiomu juga nanti kita bantu luruskan bareng di kampus, Kohinata."
            shiori "Analisis yang rasional. Dan saya dapat memastikan saluran resmi fakultas tidak memperbesar tulisan tanpa verifikasi."
            koita "...Iya. Maaf aku tadi langsung panik dan hampir menuduhmu, Yutaka. Makasih sudah menahan suasana sebelum tambah berantakan."
            moeka "...Makasih banget, Yutayuta, Saionji-san. Rasanya kepalaku agak bisa bernapas lagi."
        else:
            $ kk_rel("koita", "trust", 3)
            $ kk_rel("nagisa", "trust", 5)
            yutaka "Jangan memaksa Nagisa atau siapa pun memilih kubu di ruang tengah begini, Koita. Kalau orang-orang mulai bicara lebih terbuka denganku, itu karena aku dengar mereka sampai selesai tanpa menghindar."
            nar "Koita tertegun sejenak, wajahnya meredup oleh kalimat lugasmu yang tidak membawa nada mengejek."
            koita "...Jadi selama ini memang aku yang terlalu sering kabur dari jawaban ya."
            nagisa "Aku nggak bilang kamu jahat, Ko-kun. Cuma... kadang capek kalau harus terus menebak maksudmu."
            yutaka "Di luar hujan masih deras. Lebih baik kita hangatkan sup di dapur dulu daripada semua duduk kaku seperti ruang sidang."
            nar "Chiasa menghela napas kecil dan bangkit membantu menyalakan kompor, melonggarkan ketegangan yang nyaris meledak di ruangan itu."
    elif _return == "B":
        $ store.deviasi += 7
        $ store.runtuh_koita += 5
        if kk_get("daftar_kebohongan_shiori", 0) > 0:
            $ kk_adj("daftar_kebohongan_shiori", 1)
        nar "Kamu tidak meredam badai di ruang tengah itu. Kamu berdiri tegak di tengah cahaya redup, suaramu rendah dan tajam mengarahkan setiap retakan langsung ke titik paling rapuh di meja."
        yutaka "Kenapa semua orang kelihatan terkejut sih? Dari awal liburan ini sumber kekacauannya selalu sama. Setiap kali Koita nggak berani memberi kepastian, orang-orang di sekitarnya yang akhirnya menanggung canggung, rumor, sampai capek sendiri."
        koita "Yutaka... tunggu dulu, kamu bicara seolah-olah semua kekacauan di vila ini memang salahku sendiri?!"
        yutaka "Buktinya kemarin di festival siapa yang bikin dua orang menunggu bersamaan di depan antrean? Dan hari ini siapa yang paling panik begitu satu foto buram dan inisial klub Sastra naik di forum? Aku cuma menyebut fakta yang dari tadi ditahan semua orang."
        nar "Ruangan membeku seketika. Moeka menunduk memeluk tasnya, Miyuki menggigit bibirnya pelan, dan Nagisa menatap Koita dengan keraguan yang tidak lagi bisa disembunyikan."
        shiori "Langkah yang sangat bersih untuk mengalihkan sorotan, Kisaragi-san. Kamu memindahkan seluruh pertanyaan ruangan ke bahu sahabatmu sendiri dalam satu kalimat."
        chiasa "Yutaka-kun, itu keterlaluan! Kita lagi terkurung badai di satu rumah, nggak perlu membuat Ko-nii terpojok di depan semua orang begini!"
        nar "Koita berdiri kaku beberapa detik. Matanya yang hitam gelap menatapmu penuh rasa terkhianati dan dingin sebelum ia berbalik menaiki tangga kayu ke lantai dua tanpa sepatah kata pun."
        play sound "audio/sfx/door_close.wav"
        nar "Pintu kamar di atas tertutup rapat. Di bawah, tidak satu pun orang segera bangkit menyusulnya. Kamu baru saja meretakkan pusat orbit Koita secara terbuka di depan seluruh lingkaran, dengan akibat yang siap meledak begitu semester September dimulai."
    else:
        $ _target = "koita" if (kk_has("koita_arah_bl") or kk_has("koita_ditawari_nama")) else _focus
        $ kk_rel(_target, "intim", 6)
        $ kk_rel(_target, "trust", 4)
        nar "Kamu menolak membiarkan percakapan pribadi habis menjadi tontonan satu ruangan. Kamu melangkah tenang mendekati orang yang paling banyak memenuhi perhatianmu selama tiga hari ini dan menyentuh lengan bajunya pelan."
        yutaka "Ikut aku ke serambi belakang sebentar. Di dalam terlalu banyak telinga, kita bicara berdua saja."
        nar "Kalian keluar melalui pintu kaca geser menuju serambi kayu beratap yang terlindung dari guyuran hujan deras. Tirai air jatuh beberapa tapak di depan pagar kayu, menutup rapat suara dari ruang tengah."
        if _target == "koita":
            koita "Lepas dulu! Kamu ngajak aku keluar hujan-hujan cuma mau nyudutin aku lagi kayak tadi?!"
            nar "Koita memutar tubuh dengan bahu tegang dan wajah memerah padam, napasnya agak pendek, tetapi kakinya tidak beranjak kembali masuk ke pintu kaca."
            yutaka "Aku nggak lagi menyudutkan kamu, Koita. Aku justru menarikmu keluar supaya kamu nggak harus memasang senyum palsu di depan enam orang sekaligus."
            koita "Kamu tuh ya... dari kemarin bikin aku kacau terus! Aku sahabatmu dari kecil, Yutaka! Kenapa kamu nggak bisa bersikap biasa aja kayak dulu?!"
            yutaka "Karena kalau aku terus bersikap biasa aja, kamu nggak akan pernah berhenti lari dari pertanyaan yang sebenarnya sudah kamu dengar jelas."
            nar "Koita membuka mulut hendak membentak balik, lalu terhenti melihat tatapan abu-abu gelapmu yang tenang dan tidak mundur sedikit pun. Telinganya makin merah; ia memalingkan wajah ke tirai hujan sambil mengepalkan tangan di saku."
            koita "...Brengsek. Bikin orang marah terus tapi tetap berdiri di sini. Ya sudah, diam lima menit saja sampai kepalaku dingin, jangan suruh aku balik ke dalam dulu."
            nar "Meski masih menggerutu pelan, Koita bergeser bersandar di pagar serambi tepat di sampingmu tanpa pergi."
        elif _target == "chiasa":
            chiasa "Kamu menarikku keluar dari badai di dalam, Yutaka-kun? Tumben banget nggak milih jadi penengah di ruang tengah."
            yutaka "Di dalam terlalu ramai buat bicara jujur. Aku tahu sejak beberapa minggu terakhir kamu memperhatikan caraku berubah, Chiasa."
            chiasa "Iya, aku memperhatikan. Kadang terasa asing, tapi anehnya waktu kita bicara berdua di tempat sepi begini, aku nggak merasa perlu memasang tameng."
            yutaka "Kalau begitu jangan menebak-nebak dari jauh lagi. Kalau ada yang bikin kamu curiga, tanyakan langsung ke aku."
            nar "Chiasa menatap tirai hujan sebentar lalu tersenyum pelan yang jauh lebih jujur, matanya yang kuning keemasan melembut di bawah suara hujan."
        elif _target == "nagisa":
            nagisa "Yutaka... di dalam tadi suaraku kelewat keras ya? Habisnya tiap lihat semua orang muter-muter nggak jelas, kepalaku langsung panas."
            yutaka "Nggak apa-apa, Nagisa. Lebih baik kamu bicara terus terang daripada memendam sendiri lalu kesal di kamar."
            nagisa "H-hei, aku nggak gampang nangis ya! ...Tapi aneh juga, belakangan ini tiap suasana kacau, mataku malah otomatis nyari kamu duluan buat lihat reaksimu."
            yutaka "Kalau begitu nggak perlu ragu lagi aku berdiri di pihak mana. Sekarang aku di sini sama kamu, kan?"
            nar "Pipi Nagisa langsung merona hangat di tengah udara hujan. Ia memalingkan wajah ke tirai air sambil menyembunyikan senyum kikuknya."
        elif _target == "miyuki":
            miyuki "Maaf merepotkanmu keluar ke serambi dingin begini, Yutaka-kun. Tadi di dalam aku benar-benar panik..."
            yutaka "Tachibana-senpai, dengar aku sebentar. Selama sisa liburan ini, berhenti merasa bersalah untuk hal yang bukan kesalahanmu. Kamu nggak perlu jadi sempurna supaya aku mau duduk di sebelahmu."
            miyuki "...Kamu sungguh memaksudkan kalimat itu, Yutaka-kun? Bahkan waktu aku kelihatan seberantakan barusan?"
            yutaka "Justru karena itu aku mengajakmu keluar. Tarik napas dulu, nggak ada jadwal bangsal di balik hujan ini."
            nar "Miyuki memejamkan mata sebentar, lalu menyandarkan bahunya pelan ke tiang kayu di dekatmu dengan senyum tipis yang akhirnya lega."
        elif _target == "moeka":
            moeka "Aduh, Yutayuta, maaf banget kalau di dalam tadi aku bikin semua makin panik. Aku cuma takut banget semua orang tahu kepalaku lagi berantakan soal beasiswa sama foto studio itu."
            yutaka "Kamu nggak perlu pasang topeng ceria di depanku, Kohinata. Di luar sini nggak ada kamera, nggak ada Kurosawa Meisa, cuma hujan."
            moeka "...Boleh aku diam dua menit saja tanpa harus ketawa biar suasana enak?"
            yutaka "Boleh. Aku jaga pintu kaca biar nggak ada yang menyusul keluar."
            nar "Moeka menyeka sudut matanya cepat dengan punggung tangan lalu menatapmu dengan kepercayaan yang jauh lebih tenang."
        elif _target == "harumi":
            harumi "Terima kasih sudah memberi ruang di luar, Kisaragi-kun. Kebisingan konflik emosional di ruangan tertutup menurunkan fokus saya secara drastis."
            yutaka "Di luar sini jauh lebih tenang, Kujo-san. Kamu nggak perlu mengubah jadwal riset atau masa depanmu cuma karena merasa terutang budi ke siapa pun."
            harumi "...Variabel yang paling sulit saya ukur ternyata rasa nyaman ketika dipercaya tanpa syarat. Kamu membuat variabel itu terasa jauh lebih jelas."
            nar "Harumi membetulkan kacamatanya pelan sementara ujung telinganya memerah samar di balik kepang perak sampingnya."
        else:
            shiori "Kamu menarik saya keluar tepat di puncak keributan ruang tengah, Kisaragi-san. Langkah yang cukup berani."
            yutaka "Saionji-san paling paham cara membaca situasi tanpa ikut panik. Aku cuma mau memastikan kita satu garis soal kejadian semalam dan soal Kurosawa Meisa."
            shiori "Saya menghargai pembicaraan lugas daripada sandiwara panjang. Untuk saat ini, saya menilai kamu dari keputusan nyatamu, terlepas dari tulisan gosip mana pun di luar."
            nar "Shiori menatap tirai hujan sejenak lalu melirikmu dengan senyum tipis yang tenang, menandai batas kepercayaan baru di antara kalian."
        nar "Ketika badai akhirnya mereda menjelang malam, percakapan sunyi di serambi belakang itu membekas jauh lebih dalam daripada keributan di ruang tengah."
    return


# ══════════════════════════════════════════════════════════════════════════
# HARI 4 · Dermaga Pulang — 4 Cabang Hasil & Jembatan Langsung ke M18 (Host Yutaka)
# ══════════════════════════════════════════════════════════════════════════
label kk_pulau_yutaka_hari4(_focus):
    $ _out = kk_pulau_day4_outcome()
    call kk_scene_enter("yutaka", "Geladak Feri Pulang · Hari 4 Pulau")
    if _out in ("retak_meisa", "jejak_takut"):
        $ kk_bgm("aftermath")
    else:
        $ kk_bgm("intimacy")
    nar "Pagi hari keempat terbit sangat cerah sesudah badai semalam. Langit biru bersih membentang di atas teluk yang tenang, memantulkan kilau perak di permukaan laut ketika feri pulang bersandar di dermaga pulau."
    "Petugas Feri" "Penumpang tujuan daratan utama silakan naik ke dek atas! Kapal berangkat tepat lima menit lagi!"
    nar "Seluruh koper kembali diangkut ke bagasi bawah. Angin laut pagi bertiup kencang di geladak terbuka ketika kapal melepas tambat dan garis pantai pulau perlahan menjauh. Namun susunan rombongan di sepanjang pagar dek tidak lagi sama seperti empat hari lalu."
    if _out == "retak_meisa":
        $ kk_flag("pulau_koita_curiga_berat")
        nar "Koita berdiri sendirian di ujung haluan dek sambil mencengkeram pagar besi dengan kedua tangan. Ia tidak ikut bergabung di bangku minuman seperti biasanya, dan ketika matanya bertemu pandang denganmu, kehangatan sahabat lama itu sudah digantikan jarak yang kaku."
        koita "Begitu kapal merapat nanti aku langsung balik duluan ya, Yutaka. Ada beberapa hal yang perlu kupikirkan sendiri sebelum kuliah September mulai."
        nar "Beberapa meter di bangku dek belakang, Kurosawa Meisa duduk santai memakai kacamata hitam sambil mengetik panjang di ponselnya. Sekilas sudut bibirnya terangkat begitu matanya menyapu Koita, lalu bergeser ke arah Shiori dan Moeka."
        shiori "Jejak empat hari ini tidak berhenti di dermaga, Kisaragi-san. Kurosawa Meisa pulang membawa draf lengkap untuk seluruh kampus bulan depan."
        yutaka "{i}Koita curiga berat, dan Kurosawa Meisa pulang membawa bahan lengkap soal klub Sastra, keluarga Saionji, dan Moeka. September di kampus nanti bakal berubah jadi sidang rumor.{/i}"
    elif _out == "jejak_takut":
        $ kk_flag("pulau_jejak_takut")
        nar "Di bangku sebelahmu, orang yang selama dua hari terakhir terus menekan dirinya sendiri duduk terlalu tegak dengan tangan terlipat di atas tas. Ia segera bangkit menawarkan minuman dingin begitu melihatmu menggeser tali tas."
        miyuki "Kamu mau duduk di tempat teduh, Yutaka-kun? Biar aku saja yang berdiri di pinggir pagar, anginnya agak kencang buatmu."
        nar "Kepatuhan yang terlalu cepat itu tidak terdengar seperti kelegaan pulang liburan. Di sisi dek kanan, Chiasa memperhatikan adegan singkat itu tanpa senyum jahilnya yang biasa. Mata kuning keemasannya menatapmu lurus beberapa detik sebelum ia memalingkan wajah ke laut."
        yutaka "{i}Mereka memang tidak lagi berputar di sekitar Koita, tapi tatapan yang mereka berikan kepadaku sekarang lebih dekat ke rasa takut gagal daripada kepercayaan.{/i}"
    elif _out == "orbit_bergeser":
        $ store.deviasi += 5
        $ kk_flag("pulau_orbit_bergeser")
        nar "Di sepanjang pagar dek yang menghadap garis pantai, rombongan berbincang jauh lebih santai sambil berbagi minuman dingin. Tanpa harus kamu atur, arah obrolan mengalir alami ke sekitarmu."
        if _focus == "nagisa":
            nagisa "Anginnya kencang banget, pitaku hampir lepas lagi... Eh, Yutaka, habis turun kapal nanti temani aku mampir kios kue jeruk dekat stasiun ya, aku mau beli buat Onii-chan."
        elif _focus == "miyuki":
            miyuki "Empat hari ini rasanya cepat sekali lewatnya, Yutaka-kun. Untuk pertama kalinya aku pulang liburan dengan kepala yang benar-benar agak ringan."
        elif _focus == "moeka":
            moeka "Foto langit pascabadai barusan keren banget, Yutayuta! Nanti sampai daratan kukirim ke kamu duluan ya sebelum kubuka pesan Ryena soal katalog studio itu!"
        elif _focus == "harumi":
            harumi "Saya mencatat beberapa pengamatan menarik dari empat hari ini, Kisaragi-kun. Salah satunya adalah bahwa jeda bersama orang yang tepat tidak menurunkan kualitas berpikir."
        elif _focus == "chiasa":
            chiasa "Lumayan juga empat hari ini, Yutaka-kun. Kalau semester depan mulai berisik lagi di kampus, jangan lupa istirahat cukup."
        else:
            shiori "Perjalanan yang jauh lebih teratur dari perkiraan awal saya, Kisaragi-san. Saya rasa kita masih akan banyak bertukar pikiran begitu semester baru dimulai."
        nar "Di sisi kiri pagar, Koita menyaksikan keakraban itu dengan senyum tipis yang agak sepi. Tidak ada ledakan marah, hanya kesadaran tenang bahwa pusat ruangan yang dulu otomatis miliknya kini sudah bergeser."
    else:
        $ kk_flag("pulau_retak_halus")
        nar "Di sepanjang pagar dek, semua orang tampak kembali berbagi kue kering dan bercanda soal badai semalam seolah liburan berjalan biasa saja. Moeka memotret burung laut, Chiasa meledek Koita soal dompet, dan Shiori menyesap teh dinginnya."
        nar "Namun di balik tawa yang tampak rapi itu, kamu menangkap setiap tanda kecil yang sudah mulai bergerak menuju bulan depan. Di bangku belakang, Kurosawa Meisa mengetik catatan panjang di layar ponselnya; ponsel Moeka kembali bergetar oleh pesan Ryena tentang foto studio Kuga; dan di sebelahmu, mata Nagisa langsung menoleh tajam ketika ponsel di sakumu berbunyi dua kali."
        nagisa "Ponselmu dari kemarin bunyi terus ya, Yutaka. Siapa sih yang rajin banget kirim pesan? ...Nggak apa-apa, cuma nanya."
        yutaka "{i}Permukaannya kelihatan tenang, tapi seluruh benih untuk bulan September sudah mulai berjatuhan di atas dek ini. Dan yang paling penting, aku baru menyaksikan sendiri bahwa data Sistem bisa usang.{/i}"
    if _out != "rapuh_waspada":
        play sound "audio/sfx/phone_buzz.wav"
        nar "Tepat saat kapal berbelok mendekati pelabuhan utama, ponsel di saku celanamu kembali bergetar dua kali. Nagisa yang berdiri tak jauh darimu sempat berhenti merapikan pitanya dan melirik saku celanamu dengan kening sedikit berkerut sebelum cepat-cepat memalingkan wajah."
    nar "Garis dermaga daratan utama sudah jelas di depan haluan. Sebelum peluit merapat berbunyi dan seluruh rombongan kembali menghadapi bulan September di kampus, kamu menentukan satu sikap terakhir yang kamu bawa pulang dari pulau ini."
    call kk_family_menu("Y17b_H4", ["Simpan catatan soal data usang Sistem dan susun langkahmu sendiri ke depan.", "Hampiri orang yang paling banyak berubah di sisimu sebelum kapal merapat.", "Hadapi Kurosawa Meisa sebentar di jalur keluar dek sebelum ia menghilang ke stasiun."])
    if _return == "A":
        $ store.sikap_sistem["selidik"] = store.sikap_sistem.get("selidik", 0) + 2
        nar "Kamu bersandar pada pagar besi menghadap angin laut, menyusun ulang seluruh kronologi sejak malam kedua di dalam kepalamu. Setiap kali keputusan nyata orang-orang di sini melenceng dari jalur lama, radar Sistem langsung tertinggal menjadi data usang."
        yutaka "{i}Jadi aku tidak harus selalu mengikuti umpan misi darimu. Selama aku membaca gerak manusia di sekitarku lebih cepat, aku bisa melangkah satu putaran di depan radarmu.{/i}"
        $ kk_bgm("system")
        play sound "audio/sfx/system_open.wav"
        nar "Panel kaca biru berkedip singkat di sudut pandangmu, menangkap jelas arah pikiranmu dengan emotikon menyipit dingin."
        sistem "(¬_¬ ) Misi Pulau tercatat selesai. Jangan buru-buru merasa pintar, Sampah Peron. Celah kecil di satu liburan tidak membatalkan kontrak wisudamu. Mari kita lihat seberapa tenang mukamu waktu sidang rumor meledak di kampus bulan depan~"
        play sound "audio/sfx/system_close.wav"
        nar "Layar itu padam dengan dengung lebih pendek dari biasanya. Kamu menegakkan bahu, siap turun ke dermaga dengan kepala jauh lebih dingin."
    elif _return == "B":
        $ _end_t = "koita" if (kk_has("koita_arah_bl") or kk_has("koita_ditawari_nama")) else _focus
        $ kk_rel(_end_t, "intim", 4)
        $ kk_rel(_end_t, "trust", 3)
        nar "Kamu melangkah menyusuri dek yang mulai ramai oleh penumpang bersiap turun dan berdiri sejajar di samping orang yang paling banyak berbagi momen bersamamu sepanjang empat hari ini."
        yutaka "Makasih sudah ikut sampai akhir di pulau ini. Minggu depan kampus mulai ramai lagi, jangan lupa istirahat cukup begitu sampai rumah."
        if _end_t == "koita":
            koita "Hmph... iya, kamu juga. Jangan langsung kerja begadang aneh-aneh di apartemen sendirian. ...Makasih buat empat hari ini, Yutaka."
        elif _end_t == "nagisa":
            nagisa "I-iya, kamu juga! Jangan begadang main game atau keluyuran malam-malam terus habis pulang begini. ...Makasih buat empat hari ini, Yutaka."
        elif _end_t == "miyuki":
            miyuki "Terima kasih banyak, Yutaka-kun. Nanti di kampus kalau jadwal kita cocok, kita minum teh lagi tanpa terburu-buru ya."
        elif _end_t == "moeka":
            moeka "Siap, Yutayuta! Habis ini aku bakal lebih rapi atur jadwal dan langsung beresin soal katalog studio itu biar nggak bikin kamu cemas lagi."
        elif _end_t == "harumi":
            harumi "Saya akan menyimpan catatan perjalanan ini dengan rapi, Kisaragi-kun. Terima kasih sudah tidak memaksa saya memakai ukuran orang lain."
        elif _end_t == "chiasa":
            chiasa "Kamu juga jaga kesehatan di apartemen, Yutaka-kun. Kalau lagi malas masak, tinggal kirim pesan sebelum mampir ke rumah."
        else:
            shiori "Kamu pun jaga ritmemu, Kisaragi-san. Bulan depan di kampus kelihatannya akan cukup berisik, dan saya rasa kita masih akan sering berdiskusi."
        $ kk_bgm("system")
        play sound "audio/sfx/system_open.wav"
        sistem "( ´ v ` ) Misi Pulau ditutup. Lumayan juga hasilnya, meski kau sempat terpeleset sendiri di dermaga malam kedua. Kita lihat seberapa lama suasana manis ini bertahan bulan depan~"
        play sound "audio/sfx/system_close.wav"
    else:
        nar "Begitu kapal merapat dan jalur penumpang mulai bergerak turun menuju gerbang dermaga, kamu mempercepat langkah dengan santai hingga berjalan sejajar di samping Kurosawa Meisa yang sedang menggulir ponselnya."
        yutaka "Kebetulan yang rapi sekali ya, Kurosawa-san. Menginap lima menit dari vila kami, naik feri pulang yang sama, dan kelihatannya catatan ponselmu penuh sekali pagi ini."
        nar "Langkah Meisa terhenti setengah ketukan. Ia menengadah menatap posturmu, menurunkan kacamata hitamnya sedikit dengan senyum tipis yang terlatih."
        "Kurosawa Meisa" "Oh, Kisaragi Yutaka ya? Pulau ini tempat umum tiap Agustus. Nggak ada larangan mahasiswi lain ikut mencatat obrolan menarik di dermaga."
        yutaka "Memang nggak ada larangan. Cuma sekadar mengingatkan sesama mahasiswa Kouseikan, memelintir foto buram jarak jauh apalagi sampai menyeret nama keluarga Saionji dan pekerjaan orang lain biasanya punya ekor jauh lebih panjang dari yang kelihatan di forum."
        nar "Kilat kaget yang sangat tipis melintas di mata Meisa mendengar nada tenangnya. Senyumnya masih bertahan, tetapi ibu jarinya berhenti mengetik di layar."
        "Kurosawa Meisa" "Tenang saja, Kisaragi-san, aku cuma merangkum hal yang memang sudah ramai dibicarakan orang. Sampai ketemu di kampus bulan depan."
        nar "Ia melangkah cepat mendahului antrean keluar gerbang. Kamu tahu peringatan barusan tidak akan menghapus badai rumor September sepenuhnya, tetapi setidaknya ia kini sadar kamu melihat seluruh geraknya sejak dari dermaga."
        $ kk_bgm("system")
        play sound "audio/sfx/system_open.wav"
        sistem "( ` v ´ )b Misi Pulau selesai. Berani juga kau menyentil sumber gosip kampus langsung di dermaga. Mari kita lihat apakah itu menahan badainya atau malah bikin dia makin kreatif bulan depan~"
        play sound "audio/sfx/system_close.wav"
    nar "Begitu kakimu kembali menginjak aspal di luar gerbang pelabuhan menuju stasiun, hawa kota yang panas langsung menyergap. Liburan pulau empat hari selesai, menyisakan percikan yang siap menyala begitu bulan September dimulai."
    return
