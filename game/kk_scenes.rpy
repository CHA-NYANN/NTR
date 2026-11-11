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
label kkscene_N01:
    call kk_scene_enter("nagisa", "Gedung Arsitektur")
    nar "Bahu seseorang menghantammu di koridor fakultas arsitektur. Gulungan maket dan pena potong berhamburan ke lantai. Gadis bertwin-tail pirang itu mendelik—lalu, anehnya, matanya kembali ke konsol game kecil di tangannya."
    nagisa "Punya mata, tidak? Jangan berdiri di tengah jalan orang."
    nar "Sakurajima Nagisa. Teman masa kecil Koita. Ia belum tahu ada yang berbeda darimu, dan menantangmu seolah kalian memang selalu begini."
    menu:
        "Angkat maketnya, lalu balas tantangannya.":
            $ kk_record_choice("N01", "A")
            nagisa "...Hmph. Setidaknya kau tidak lari. Lain kali, lawan aku yang benar."
        "Minta maaf singkat, kau sedang buru-buru.":
            $ kk_record_choice("N01", "B")
            nagisa "Hah. Ya sudah. Pergi sana."
        "Goda dia soal game yang lebih penting dari tabrakan.":
            $ kk_record_choice("N01", "C")
            nagisa "A-apa—bukan urusanmu! Lagian aku hampir menang."
    return

# ── Mi01 · Bento Hanami (Miyuki, Taman Kampus) ──
label kkscene_Mi01:
    call kk_scene_enter("miyuki", "Taman Kampus")
    nar "Sakura belum sepenuhnya gugur. Di bawah salah satu pohon, seorang senpai berambut hitam panjang membuka kotak bento bertingkat yang jauh terlalu besar untuk satu orang."
    miyuki "Ah—kebetulan. Aku membuat terlalu banyak lagi. Kalau kau tidak keberatan... duduklah."
    nar "Tachibana Miyuki, mahasiswi kedokteran tahun ketiga. Senyumnya hangat, tapi ada lelah tipis di sudut matanya yang ia sembunyikan rapi."
    menu:
        "Puji masakannya dengan tulus.":
            $ kk_record_choice("Mi01", "A")
            miyuki "Benarkah enak? Syukurlah. Aku... jarang dapat alasan untuk memasak sebanyak ini."
        "Bantu ia membawakan kotaknya yang berat.":
            $ kk_record_choice("Mi01", "B")
            miyuki "Eh, tidak perlu—tapi... terima kasih. Tidak banyak yang menawarkan."
        "Permisi, kau ada urusan lain.":
            $ kk_record_choice("Mi01", "C")
            miyuki "Oh. Tentu, maaf menahanmu. Hati-hati, ya."
    return

# ── N03 · Maket Hujan (Nagisa, Gedung Arsitektur, M03) ──
label kkscene_N03:
    call kk_scene_enter("nagisa", "Gedung Arsitektur")
    nar "Hujan menerobos jendela studio yang lupa ditutup. Maket tugas akhir Nagisa—kerja berminggu-minggu—basah dan melengkung di satu sudut. Ia berdiri mematung, rahang mengeras, menolak menangis di depan siapa pun."
    if any(c["ev"] == "N01" and c["key"] == "A" for c in choices_log):
        nagisa "Kalau mau tanding lagi, kau harus tunggu. Lihat sendiri maketku."
    nagisa "...Tidak apa-apa. Masih bisa. Aku tinggal mengulang bagian ini. Semalaman. Lagi."
    menu:
        "Tinggal, bantu memperbaikinya sampai pagi.":
            $ kk_record_choice("N03", "A")
            nagisa "Kenapa kau... tidak usah. ...Terserah. Jangan sentuh bagian atap, itu bagianku."
            nar "Kalian bekerja sampai langit memutih. Ia tidak bilang terima kasih—tapi tidak menyuruhmu pulang."
        "Tawarkan membelikan bahan maket baru.":
            $ kk_record_choice("N03", "B")
            nagisa "Aku tidak butuh dikasihani dengan uang. ...Tapi, ya. Terima kasih, kurasa."
        "Tertawakan nasib sialnya.":
            $ kk_record_choice("N03", "C")
            nagisa "...Keluar. Keluar dari studioku."
    return

# ── Mi03 · Perpustakaan Medis Malam (Miyuki, RS Tachibana, M04) ──
label kkscene_Mi03:
    call kk_scene_enter("miyuki", "Rumah Sakit Tachibana")
    nar "Lewat tengah malam. Lampu perpustakaan medis sudah separuh dimatikan, tapi Miyuki masih di sana, dikelilingi tumpukan buku anatomi. Ia tidak sadar kau datang sampai kau cukup dekat untuk melihat betapa pucatnya ia."
    miyuki "...Jam berapa? Ah, tidak apa. Sedikit lagi. Bab ini saja."
    if any(c["ev"] == "Mi01" and c["key"] == "B" for c in choices_log):
        miyuki "Kau lagi. Kotak bento waktu itu juga kau yang bawa, ya?"
    nar "Ia sudah mengatakan 'bab ini saja' entah berapa kali, kelihatannya."
    menu:
        "Bawakan sesuatu untuk ia makan, diam-diam temani.":
            $ kk_record_choice("Mi03", "A")
            miyuki "Kau... membelikan ini? Kau tidak perlu. ...Terima kasih. Sungguh."
        "Tegas: tutup bukunya, suruh ia pulang.":
            $ kk_record_choice("Mi03", "B")
            miyuki "Kau benar. Maaf. Aku memang berlebihan. Aku... pulang sekarang."
        "Duduk diam di sebelahnya tanpa bicara.":
            $ kk_record_choice("Mi03", "C")
            miyuki "...Kau tidak harus tinggal. Tapi... jangan pergi dulu. Sebentar saja."
    return
