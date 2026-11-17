# M28, Tanabata ketiga. Pemain mendekati orang yang hadir di taman.
# ┌─ PANDUAN CERITA · S19 · Tanzaku Shiori
# │ LOKASI  : Kampus Kouseikan · Taman Kampus
# │ TERLIBAT: Saionji Shiori (+ Koita bila relevan)
# │ AWALAN  : harapannya.
# │ INTI    : A baca / B abaikan.
# │ AKHIRAN : petunjuk.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_S19:
    call kk_scene_enter("shiori","Tanabata di taman kampus")
    nar "Tanzaku Shiori digantung cukup rendah untuk dibaca tanpa menarik dahan. Ia melihatmu mendekat dan sengaja menyebut kertas mana miliknya, tidak perlu berpura-pura membiarkannya ditemukan secara kebetulan."
    shiori "Yang biru itu. Kamu boleh membaca. Aku tidak akan menganggapmu lebih peka hanya karena berhasil menebak sebelum diberi tahu."
    call kk_family_menu("S19", ["Baca tulisan Shiori.", "Biarkan harapannya tetap pribadi."])
    if _return == "A":
        if kk_has("shiori_koreksi_disampaikan"):
            nar "Semoga orang berani mengatakan sendiri apa yang perlu dikatakan. Kau teringat percakapan kalian saat hujan."
        elif stage.get("shiori",0) >= 4:
            nar "Semoga yang kusembunyikan di balik senyum ini akhirnya bisa kukatakan."
        else:
            nar "Semoga jawaban yang kuberikan nanti benar-benar jawabanku sendiri."
        nar "Kau tidak memintanya menjelaskan seluruh yang disembunyikan harapan tersebut. Shiori berdiri di sebelahmu, menerima satu keinginan pribadi telah dibaca tanpa langsung diubah menjadi celah yang harus ia lindungi."
        shiori "Aku bisa membuat rencana sangat baik. Kadang tetap perlu bertanya apakah aku ingin hidup di dalam hasilnya."
    else:
        nar "Kau membiarkan harapannya tetap pribadi. Shiori tidak menarik perhatianmu kembali ke kertas."
        shiori "Baik. Terima kasih sudah memilih dengan jelas. Kalau nanti ingin tahu, kamu boleh bertanya lagi. Aku juga boleh menjawab lain kali."
    return

# ┌─ PANDUAN CERITA · H19 · Tanzaku Kosong
# │ LOKASI  : Kampus Kouseikan · Taman Kampus
# │ TERLIBAT: Kujo Harumi (+ Koita bila relevan)
# │ AWALAN  : ia tidak menulis harapan.
# │ INTI    : A tanyakan / B menulis untuknya.
# │ AKHIRAN : tanda bahaya.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_H19:
    call kk_scene_enter("harumi","Tanabata di taman kampus")
    nar "Harumi memutar pensil di tangan. Ia sudah membantu orang lain memilih tali dan tempat menggantung, tetapi tanzakunya sendiri masih kosong."
    harumi "Aku bisa menulis hasil penelitian yang kuinginkan. Tadi saat mau menulis, rasanya bukan itu. Sepertinya ada keinginan yang terus kubatalkan sebelum selesai menjadi kata."
    call kk_family_menu("H19", ["Tanya apa yang ingin ia tulis.", "Tawarkan menuliskan satu harapan untuknya."])
    if _return == "A":
        harumi "Biasanya aku tahu apa yang orang lain butuhkan. Kalau untukku sendiri, aku harus berpikir dulu."
        nar "Kau memberi waktu tanpa menawarkan kalimat yang dianggap cocok. Harumi akhirnya menulis ingin mengetahui kapan ia bahagia sebelum saat itu berlalu."
        harumi "Belum rapi. Aku ingin membiarkannya tetap begitu. Ini harapan, bukan abstrak penelitian."
    else:
        harumi "Boleh. Sisakan sedikit ruang kalau nanti aku punya kata-kata sendiri."
        nar "Kau menuliskan harapan sederhana dan menyerahkan kembali kertasnya. Harumi membaca, lalu menambahkan satu kata dengan pensilnya sendiri."
        nar "Ia berterima kasih, tetapi tangan yang begitu mudah menyerahkan jawabannya membuatmu sadar betapa pentingnya tidak menganggap kepercayaan itu sebagai izin untuk terus berbicara atas namanya."
    return

# ┌─ PANDUAN CERITA · Mo20 · Tanzaku Moeka
# │ LOKASI  : Kampus Kouseikan · Taman Kampus
# │ TERLIBAT: Kohinata Moeka (+ Koita bila relevan)
# │ AWALAN  : harapan sederhana.
# │ INTI    : A baca / B tulis bersama / C abaikan.
# │ AKHIRAN : petunjuk.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_Mo20:
    call kk_scene_enter("moeka","Tanabata di taman kampus")
    nar "Moeka memilih kertas paling cerah, lalu menulis harapan yang tidak memenuhi separuhnya. Ia sudah hendak melipat ketika kau mendekat, kemudian membiarkan tulisan itu terlihat."
    moeka "Pendek, ya. Biasanya aku banyak maunya. Yang ini cuma satu, tapi aku sudah lama ingin. Kalau kamu juga mau menulis, tempatnya masih cukup."
    call kk_family_menu("Mo20", ["Baca harapan kecilnya.", "Tulis harapanmu di sebelah tulisannya.", "Bantu pegang talinya tanpa membaca."])
    if _return == "A":
        nar "Ia ingin makan malam bersama keluarganya. Satu meja, semua kursi terisi."
        moeka "Nggak harus restoran. Nggak harus ada hadiah. Aku cuma ingin nggak ada yang izin pulang cepat karena kerja, atau nggak bisa duduk karena sakit."
        nar "Ia menyentuh ujung kertas, tersenyum dengan campuran malu dan harapan yang tidak sengaja dibuat manis."
    elif _return == "B":
        moeka "Nah, sekarang kita harus ingat yang mana kertas kita."
        nar "Kau menulis di sebelahnya tanpa mengubah harapannya menjadi janji yang tak bisa dijamin. Moeka membaca, lalu menyebut akan senang jika suatu hari kalian bisa membicarakan bagaimana keinginan kecil itu mulai terpenuhi."
    else:
        nar "Kau membantu memegang tali tanpa membaca. Moeka menggantung sendiri, melindungi permintaan yang belum ingin dijelaskan."
        moeka "Makasih. Aku senang kamu bisa membantu tanpa harus tahu semuanya dulu."
        nar "Kertas itu berayun di antara banyak keinginan lain, cukup pribadi untuk tetap menjadi miliknya."
    return

# ┌─ PANDUAN CERITA · N19 · Tanzaku Palsu
# │ LOKASI  : Kampus Kouseikan · Taman Kampus
# │ TERLIBAT: Sakurajima Nagisa (+ Koita bila relevan)
# │ AWALAN  : ia menulis tanzaku atas nama pemain.
# │ INTI    : A kecam / B biarkan.
# │ AKHIRAN : pengawasan.
# └─ tulis / perbaiki dialog di bawah ──
label kkscene_N19:
    call kk_scene_enter("nagisa","Tanabata di taman kampus")
    nar "Di ujung selembar tanzaku tertulis namamu, tetapi huruf-hurufnya milik Nagisa. Harapannya tentang terus bersama, tidak berpisah, tidak membiarkan orang lain masuk di antara kalian."
    nagisa "Aku tahu kamu belum menulis. Jadi kubuatkan. Kita kan pasti ingin hal yang sama."
    nar "Ia memeriksa tali yang sudah kuat terikat, menghindari matamu ketika mengatakan pasti."
    call kk_family_menu("N19", ["Minta ia mencopot kertas yang ia tulis atas namamu.", "Biarkan kertas itu tetap tergantung."])
    if _return == "A":
        nar "Kau memintanya mencopot kertas yang mengatasnamakanmu. Nagisa hendak mempertahankan isinya, lalu terdiam ketika kau menjelaskan bahwa persoalannya adalah hak menjawab untuk dirimu sendiri."
        nagisa "Baik. Aku turunkan. Kalau aku ingin itu, harusnya kutulis atas namaku."
        nar "Ia melepaskan tali dengan jari kaku. Permintaan maaf belum keluar, tetapi setidaknya namamu tidak lagi dipakai untuk mengesahkan ketakutannya."
    else:
        nar "Kau membiarkan kertas itu. Nagisa tersenyum, menganggap tidak adanya keberatan sebagai persetujuan atas semua yang ditulisnya."
        nagisa "Nah. Aku tahu kamu sebenarnya mengerti."
        nar "Saat kalian berjalan, namamu tetap tergantung pada keinginan yang tidak pernah kauucapkan. Peristiwa kecil itu akan mudah ia ingat sebagai bukti bahwa kau dahulu sudah setuju."
    return
