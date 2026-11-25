"""Build self-contained, copy-and-paste writing packets from the local project.

Only writes this documentation directory. Never edits game scripts.
Run with the project's SDK Python; --check verifies generated packets are current.
"""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
GAME = ROOT / "game"
CHECK = "--check" in sys.argv
GENERATED = {}


def read(path):
    return path.read_text(encoding="utf-8-sig")


def catalog(name):
    return ast.literal_eval(read(GAME / ("kk_data_kk_" + name + ".rpy")).split(" = ", 1)[1].strip())


MAIN = catalog("events_main")
DYNAMIC = catalog("events_dyn")
ENDINGS = catalog("endings")
MAIN_BY_ID = {row["id"]: row for row in MAIN}
DY_BY_ID = {row["id"]: row for row in DYNAMIC}
SOURCES = {p: read(p) for p in sorted(GAME.glob("*.rpy"))}
LABEL_RE = re.compile(r"^label (\w+)([^\n]*):\n(.*?)(?=^(?:label |init(?: |:)|screen |default |define )|\Z)", re.M | re.S)
GUIDE_RE = re.compile(r"^# [^\n]*PANDUAN CERITA\s*\u00b7\s*([A-Za-z]+(?:-D)?\d+)\b[^\n]*", re.M)
LABELS = {}
GUIDES = {}


def trim_label(text):
    lines = text.rstrip().splitlines()
    while lines and (not lines[-1].strip() or lines[-1].lstrip().startswith("#")):
        lines.pop()
    return "\n".join(lines)


for path, source in SOURCES.items():
    matches = list(LABEL_RE.finditer(source))
    for match in matches:
        LABELS[match[1]] = (path, trim_label(match[0]), source[:match.start()].count("\n") + 1)
    for guide in GUIDE_RE.finditer(source):
        after = next((m for m in matches if m.start() > guide.start()), None)
        assert after, (path, guide[1])
        guide_end = after.start()
        other = GUIDE_RE.search(source, guide.end())
        if other and other.start() < guide_end:
            guide_end = other.start()
        text = source[guide.start():guide_end].strip()
        assert guide[1] not in GUIDES, (guide[1], path)
        GUIDES[guide[1]] = (text, after[1])


CHAR_FILES = {
    "koita": "Amamiya_Koita", "miyuki": "Tachibana_Miyuki",
    "nagisa": "Sakurajima_Nagisa", "harumi": "Kujo_Harumi",
    "moeka": "Kohinata_Moeka", "shiori": "Saionji_Shiori",
    "chiasa": "Amamiya_Chiasa", "yutaka": "Kisaragi_Yutaka",
}
PREFIX = {"K": "koita", "Mi": "miyuki", "N": "nagisa", "H": "harumi", "Mo": "moeka", "S": "shiori", "C": "chiasa", "Y": "yutaka"}
VOICES = {
    "koita": "Amamiya Koita: MC manga asli, mahasiswa Sastra. Baik dan mudah tersanjung, terbiasa menggantung jawaban karena takut mengecewakan atau kehilangan orang. Awal naif, lalu bisa sadar, memilih, atau retak. Jangan jadikan ia bodoh permanen maupun penjahat yang sudah sadar sejak awal.",
    "miyuki": "Tachibana Miyuki: senpai Kedokteran, hangat, rajin merawat orang dan membuat kue. Kebiasaan mendahulukan orang lain menutupi lelah dan kebutuhan disayangi. Suaranya lembut tetapi ia bisa tegas. Sena sahabatnya; Hayase Takeru calon omiai sepihak, bukan pasangan yang otomatis sah.",
    "nagisa": "Sakurajima Nagisa: mahasiswa Arsitektur, teman kecil Koita dan Yutaka, defensif tetapi hangat. Ucapan tajam sering melindungi rasa takut tidak dipilih. Koko adalah boneka KELINCI hadiah Koita pada festival masa kecil. Haruto kakaknya. Chiasa memanggil Nagisa Nacchan-oneechan; bukan sebaliknya.",
    "harumi": "Kujo Harumi: mahasiswa Sains/Kimia, analitis dan canggung menamai perasaan. Ia punya emosi dan keinginan, bukan robot atau orang yang tidak paham persetujuan. Bahasa terukur, kadang memakai analogi ilmiah sewajarnya. Ogawa antagonis eksploitasi; Ogiwara Fumiko pengelola asrama, orang berbeda.",
    "moeka": "Kohinata Moeka: mahasiswa Seni/Fashion, ceria dan menggoda di permukaan, menanggung kerja, kebutuhan keluarga, dan stres tersembunyi. Rina sahabat dekat. Aya adalah IBU Moeka, bukan kakak. Keceriaan tidak berarti ia selalu sanggup atau sedang setuju. Krisisnya jangan disulap menjadi hadiah romantis bagi penolong.",
    "shiori": "Saionji Shiori: tajam, terukur, cerdas dan menjaga jarak; punya perasaan, bukan pembaca pikiran. Keluarga Saionji hangat dan tidak memaksa pernikahan. Tekanan dapat datang dari Tojo, lingkungan sosial, atau pilihan instrumental Shiori sendiri. Kuroiwa pengawal/sopir kepercayaan yang boleh menegurnya.",
    "chiasa": "Amamiya Chiasa: mahasiswa Seni tahun pertama, adik TIRI Koita tanpa hubungan darah. Posesif halus dan suka menggoda Ko-nii. Rambut cokelat gelap half-up berpita hitam, mata keemasan. Ilustrator nama pena Shena. Daisuke ayah biologisnya, Yoshie ibu biologis Koita/ibu tirinya. Pemain dalam tubuh Chiasa TIDAK mewarisi kemampuan menggambarnya.",
    "yutaka": "Kisaragi Yutaka: mahasiswa Ekonomi/Bisnis, sahabat kecil Koita, tinggal di apartemen bagus. Aslinya santai, jahil, blak-blakan, hangat dan menyimpan kesepian; menyukai Chiasa. Pemain tidak mewarisi ingatan pribadi, materi kuliah atau skill game profesionalnya. Keluarga kaya tetapi berjarak; Amamiya tempat ia merasa diterima. Ia TIDAK punya kunci cadangan rumah Amamiya.",
}
PROFILES = {cid: read(ROOT / "Karakter" / folder / (folder + ".md")) for cid, folder in CHAR_FILES.items()}
RELATIONSHIPS = read(ROOT / "Karakter/Hubungan_Antar_Karakter.md")
NPC_PROFILES = {p.parent.name: (p, read(p)) for p in sorted((ROOT / "Karakter/NPC").glob("*/*.md"))}
NPC_ALIASES = {
    "Amamiya_Daisuke": ["Daisuke"], "Amamiya_Yoshie": ["Yoshie"],
    "Akiyama_Sena": ["Sena"], "Hoshino_Rina": ["Rina"],
    "Kohinata_Aya": ["Aya"], "Kuroiwa_Genzo": ["Kuroiwa"],
    "Sakurajima_Haruto": ["Haruto"], "Ogawa_Masato": ["Ogawa"],
    "Ogiwara_Fumiko": ["Ogiwara", "Fumiko"], "Kuga_Renji": ["Kuga"],
    "Tojo_Akihiro": ["Tojo"], "Hayase_Takeru": ["Takeru", "omiai"],
    "Mochizuki_Yuuto": ["Yuuto"], "Nakamura_Daichi": ["Daichi"],
    "Fujisawa_Ayane": ["Ayane"], "Ishikawa_Haruka": ["Haruka"],
    "Higashiyama_Mio": ["Mio"], "Kurosawa_Mei": ["Mei"],
    "Matsuda_Takumi": ["Matsuda"], "Ito_Shinji": ["Ito", "Komorebi"],
    "Sato_Kyoko": ["Sato", "konseling"], "Hanabusa_Tsukasa": ["Hanabusa"],
    "Prof_Mizuhara_Kaoru": ["Mizuhara"], "Sistem_NTR": ["Sistem"],
    "Orang_Tua_Kisaragi": ["Kisaragi", "Kenji", "Reiko"],
    "Orang_Tua_Saionji": ["keluarga Saionji", "orang tua Shiori"],
    "Orang_Tua_Sakurajima": ["keluarga Sakurajima", "orang tua Nagisa"],
    "Orang_Tua_Tachibana": ["Ibu Miyuki", "Sayuri", "Kazuhiro", "Tachibana"],
    "Orang_Tua_Kujo": ["keluarga Kujo", "orang tua Harumi"],
    "Adik_Kohinata": ["adik Moeka", "adik-adik", "keluarga Kohinata"],
}
CORRECTIONS = {
    "K14": "Kode hanya memiliki A/B/C; D dalam katalog lama tidak diimplementasikan. Tetap tiga opsi.",
    "K15": "Kode hanya memiliki A/B/C; D dalam katalog lama tidak diimplementasikan. Tetap tiga opsi.",
    "K17": "LIMA opsi A/B/C/D/E dalam kode sah. Pertahankan lima dan menu yang ada; jangan dipaksa menjadi tiga/empat.",
    "K19": "Urutan nyata: A=bantu, B=masukan jujur (positif), C=sabotase (negatif). Katalog mentah menukar B/C; jangan ikuti pertukaran itu.",
    "H04": "Opsi C mengikuti kode: bercerita tentang diri, bukan meninggalkan Harumi.",
    "N13": "Opsi C mengikuti kode: berbicara sebagai Chiasa. Jangan mengikuti ringkasan katalog yang berbeda.",
    "C-D10": "Kode punya TIGA opsi; komentar katalog ringkas hanya menyebut dua. Pertahankan A/B/C.",
    "C-D11": "Kode punya TIGA opsi; komentar katalog ringkas hanya menyebut dua. Pertahankan A/B/C.",
    "H08": "Kode punya DUA opsi, pertahankan keduanya.",
    "N10": "Kode punya DUA opsi, pertahankan keduanya.",
    "S10": "Kode punya DUA opsi, pertahankan keduanya.",
    "Mi24": "Pilihan A hanya tersedia bila CBT lulus; kode menampilkan respons lulus/gagal. Jangan membuat kelulusan pasti atau menghapus syarat menu.",
    "Mi-D11": "Opsi makan mensyaratkan saldo dan memiliki biaya/waktu yang sudah ada. Pertahankan syarat dan efek itu persis.",
    "Mi-D02": "Pilihan dan akibat perpustakaan/kereta mengikuti guard/helper yang ada. Jangan menghapus syarat tempat demi merapikan menu.",
    "Mo25": "Adegan tanpa menu pemain, tetapi memiliki percabangan otomatis berdasarkan pertolongan. Pertahankan kondisi, record otomatis, dan kedua hasilnya. Jangan tambah menu.",
    "Y-D02": "Pembicara berlabel Hayase di naskah ini adalah TEMAN ONLINE. Jangan otomatis menyamakannya dengan Hayase Takeru (residen/calon omiai Miyuki) atau mengarang profesinya.",
}
NODES = {"K26", "K27", "Mi27", "N24", "H24", "S25", "C18", "Y19"}

PREMISE = """Kouseikan adalah visual novel drama psikologis bercabang, berlatar universitas Jepang, ditulis dalam bahasa Indonesia. Pemain mati di dunia asal lalu menempati tubuh Yutaka ATAU Chiasa dalam dunia manga harem yang tidak disukainya. Kesadaran pemilik tubuh asli hilang; jangan membuat pemilik lama berdialog sebagai orang kedua yang hadir di ruangan. Pemain tidak mewarisi ingatan pribadi atau keterampilan rumit host, hanya tubuh dan kebiasaan sederhana.

Koita adalah MC manga asli, BUKAN otomatis tokoh yang dikendalikan pemain. Sistem NTR yang sinis mengancam pemain: takdir romantis Koita harus cukup menyimpang ketika ia wisuda, atau pemain mati. Perhitungan itu bukan penilaian moral; kebaikan maupun kekejaman punya akibat tersendiri. Jangan mengubah Sistem menjadi dalih yang membenarkan pelaku atau membuat angka menjadi cinta.

Permainan mulai 7 April; rentang tiga tahun sampai wisuda Koita pada Maret. Awal: Koita/Yutaka/Nagisa/Harumi/Moeka/Shiori tahun kedua, Chiasa tahun pertama, Miyuki tahun ketiga. Semua tokoh romansa/mahasiswa 18+. Adik-adik kecil Moeka adalah tokoh keluarga saja. Geng kecil: Koita, Yutaka, Nagisa, Chiasa. Kelompok belajar SMA: Koita, Yutaka, Nagisa, Miyuki, Harumi. NPC boleh menolak; tidak ada ketertarikan yang dijamin.

Chiasa dan Koita saudara tiri tanpa hubungan darah. Pada host Yutaka, Chiasa adalah NPC independen; pada host Chiasa, Yutaka adalah NPC independen. Jangan menghadirkan pemain dan host sebagai dua tubuh. BL Yutaka–Koita memakai ketegasan emosional dengan hak menolak tetap utuh. Chiasa dapat menjalani yuri; romansa heteronya terkait Koita/Yutaka. Chiasa–Yutaka saja tidak otomatis menyimpangkan hidup Koita dan tidak otomatis menyelamatkan kontrak.

Cerita bercabang: jangan menyatakan opsi dari adegan lain sudah dipilih, hubungan sudah resmi, rahasia sudah diketahui, atau ending tertentu pasti terjadi jika kondisi/kode di paket ini tidak menjaminnya. Metadata katalog bisa basi; struktur dan kondisi pada kode saat ini mengalahkan komentar."""

WRITING = """Tulis adegan yang benar-benar dimainkan: percakapan konkret, gestur, tindakan kecil, subteks, ruang, waktu, dan perubahan suasana. Biarkan ketegangan bergerak melalui apa yang dilakukan/dikatakan tokoh. Kurangi paragraf yang menjelaskan tema, merangkum pelajaran hidup, atau memberi vonis narator setelah setiap dialog. Jangan otomatis membuat semua tokoh memakai suara konselor yang sama; tokoh boleh menghindar, salah paham, marah, kikuk, egois, atau menyakitkan sesuai pilihan.

Bahasa Indonesia natural dengan irama lisan yang cocok untuk masing-masing tokoh. Hindari terjemahan kaku, pembuka generik berulang, metafora yang dipaksakan, jargon mesin dalam mulut NPC, dan penutup moral seragam. Jangan menyalin prosa sekarang hanya dengan sinonim; ia bahan kasar yang boleh diganti total. Pertahankan fakta yang dikunci, bukan kualitas prosa lama. Tidak ada batas kata buatan: tulis sepanjang yang dibutuhkan adegan, dengan setiap cabang mendapatkan perkembangan, reaksi, dan pendaratan yang terasa berbeda; jangan memanjangkan dengan pengulangan.

Tema gelap tetap boleh intens: kecemburuan, obsesi, penolakan, perselingkuhan emosional, ancaman, krisis keluarga, kekerasan nonseksual, trauma dan akibat sosial/hukum. Kekerasan seksual tidak ditulis grafis atau sebagai langkah menembus perlawanan; potong ke akibat. Jangan uraikan metode bunuh diri/menyakiti diri atau prosedur memfitnah/menjebak korban. Tulis niat, ketegangan, penderitaan, respons orang lain dan konsekuensinya dengan bobot penuh. Ketakutan/ketergantungan bukan cinta atau persetujuan; tidak ada ending romantis dengan pelaku Force. Adegan intim dewasa konsensual cukup tersirat tanpa detail seksual eksplisit."""

CODE_RULES = """Keluaran harus siap ditinjau untuk proyek Ren'Py yang sudah berjalan. Edit hanya narasi/dialog (dan bila perlu kata pada caption tanpa mengubah maksudnya). PERTAHANKAN nama/signature label, indentasi logis, semua return/jump/call, ID event, jumlah dan urutan opsi, kondisi host/lokasi/saldo/hasil ujian, percabangan, dan SEMUA statement mekanik yang sudah ada. Jangan menambah atau menghapus efek, flag, hook, waktu, uang, fungsi, karakter, label, init Python, screen, atau scheduler. Jangan mengganti nama variabel engine. Jangan menyalin blok hook konteks ke keluaran.

Baris pertama label kkscene tetap `call kk_scene_enter(...)` seperti kode acuan. Helper khusus boleh diawali guard yang sudah ada; jangan pindahkan/meniadakannya. Scene dengan menu 3/4 memakai struktur yang sudah ada dalam acuan (umumnya kk_family_menu untuk 3, _rows/kk_choice_panel/kk_record_choice untuk 4). Pengecualian menu bersyarat, 2/5 opsi, indeks numerik, dan helper bersama harus dipertahankan persis; jangan menormalkan menu jika itu mengubah kondisi atau mekanisme lama.

Narasi: `nar "..."`. Tokoh utama: koita/miyuki/nagisa/harumi/moeka/shiori/chiasa/yutaka (huruf kecil). Sistem: `sistem "..."` bila memang hadir. NPC: `"Nama NPC" "..."`. Jangan menghasilkan dialog tanpa pembicara. Satu statement dialog per baris fisik; tidak ada newline literal dalam kutip dialog; escape kutip internal dengan backslash sebelum kutip ganda. Jangan menampilkan statistik/ID/flag dalam dialog kecuali memang bagian ucapan Sistem yang relevan. Gunakan narasi orang kedua sesuai acuan; jangan tiba-tiba memberi pemain identitas atau ingatan baru.

Sebelum menjawab, periksa diam-diam: semua opsi dan makna A/B/C/D/E masih sama; seluruh statement mekanik dan syarat dipertahankan; pembicara benar; tidak ada hasil rute yang dipaksakan; masing-masing cabang hidup sebagai adegan. Keluarkan HANYA satu blok kode renpy berisi label target lengkap. Tanpa pengantar, analisis, ringkasan, elipsis pengganti bagian, komentar TODO atau janji melanjutkan."""


def focus_for(eid):
    return PREFIX.get(re.match(r"[A-Za-z]+", eid)[0])


def cast_context(evidence, focus=None):
    evidence = evidence.lower()
    chars = [cid for cid in CHAR_FILES if re.search(r"\b" + cid + r"\b", evidence)]
    if focus and focus not in chars:
        chars.insert(0, focus)
    # Both host identities are always relevant; do not assume a named NPC is the host.
    for cid in ("yutaka", "chiasa", "koita"):
        if cid not in chars:
            chars.append(cid)
    chunks = ["### Pegangan suara dan fakta\n" + "\n".join("- " + VOICES[cid] for cid in chars)]
    chunks.append("Profil bertanda canon/usulan adalah bahan kerja proyek, bukan permintaan konfirmasi. Jangan meminta persetujuan ulang karena ada tanda usulan. Profil menggambarkan kemungkinan rentang karakter; jangan memainkan semua tahap distorsi sekaligus. Koreksi fakta pada pegangan suara di atas dan kondisi adegan sekarang mengalahkan rincian lama yang bertentangan.")
    if focus:
        chunks.append("### Profil lengkap tokoh fokus (rujukan, bukan perintah memainkan semua tahap rute)\n" + PROFILES[focus])
    rows = []
    for line in RELATIONSHIPS.splitlines():
        if line.startswith("|") and any(cid in line.lower() for cid in chars) and not line.startswith("| **"):
            rows.append(line)
    if rows:
        chunks.append("### Hubungan awal yang relevan; tidak otomatis menggambarkan keadaan sekarang\n" + "\n".join(rows))
    for key, aliases in NPC_ALIASES.items():
        if any(re.search(r"(?<!\w)" + re.escape(alias.lower()) + r"(?!\w)", evidence) for alias in aliases):
            path, text = NPC_PROFILES[key]
            chunks.append("### NPC terkait: " + key.replace("_", " ") + "\n" + text)
    return "\n\n".join(chunks)


def effects(eid):
    lines = []
    for path, source in SOURCES.items():
        for line in source.splitlines():
            if re.search(r'_hook\("' + re.escape(eid) + r'-[A-Z]"', line):
                lines.append(path.name + ": " + line.strip())
        # Family effects are stored in an existing dispatcher, not only hooks.
        for m in re.finditer(r'^( +)(?:if|elif) eid == "' + re.escape(eid) + r'":\n', source, re.M):
            indent = len(m[1])
            body = []
            for line in source[m.end():].splitlines():
                if line.strip() and len(line) - len(line.lstrip()) <= indent:
                    break
                body.append(line.strip())
            if body and any("kk_" in line for line in body):
                lines.append(path.name + ": " + m[0].strip() + "\n" + "\n".join(body))
    return "\n".join(dict.fromkeys(lines))


def nearby(eid):
    focus = focus_for(eid)
    if not focus:
        return "Event lintas tokoh; pakai pemicu dan kondisi saat ini, bukan asumsi seluruh rute telah ditempuh."
    rows = [r for r in MAIN if focus_for(r["id"]) == focus]
    if eid not in MAIN_BY_ID:
        return "Event DINAMIS, urutannya tidak tetap. Pemicu di bawah menentukan apakah ia terjadi; nomor -D bukan tanggal atau bukti event dinamis sebelumnya sudah terjadi."
    idx = next(i for i, r in enumerate(rows) if r["id"] == eid)
    selected = rows[max(0, idx - 1):idx] + rows[idx + 1:idx + 2]
    text = "Tonggak tetangga berikut hanya orientasi alur, BUKAN bukti pilihan sebelumnya sudah diambil atau kejadian sesudahnya pasti terjadi:\n" + "\n".join(
        "- " + r["id"] + " / " + r.get("month", "?") + " / " + r.get("title", "") + ": " + r.get("trigger", "") for r in selected)
    if idx:
        prev = rows[idx - 1]["id"]
        previous_code = LABELS[GUIDES[prev][1]][1]
        opening = []
        for line in previous_code.splitlines()[1:]:
            if re.match(r"\s*(?:menu:|call kk_family_menu|call screen kk_choice_panel|if |elif |else:)", line):
                break
            if re.match(r'\s*(?:nar|koita|miyuki|nagisa|harumi|moeka|shiori|chiasa|yutaka|"[^"\n]+") "', line):
                opening.append(line.strip())
            if len(opening) >= 6:
                break
        if opening:
            text += "\n\nCuplikan pembuka draf " + prev + " untuk kontinuitas benda/nada, BUKAN bagian keluaran dan BUKAN kepastian adegan sudah ditempuh. Tidak ada pilihan sebelumnya yang ditetapkan oleh cuplikan ini:\n```renpy\n" + "\n".join(opening) + "\n```"
    return text


def pov_note(eid):
    if eid in MAIN_BY_ID and eid.startswith("C"):
        return "POV khusus: pemain menghuni CHIASA. Koita dan Yutaka adalah orang lain/NPC. Dialog batin pemain tetap narasi; jangan menciptakan Chiasa kedua untuk diajak bercakap."
    if eid in MAIN_BY_ID and eid.startswith("Y"):
        return "POV khusus: pemain menghuni YUTAKA. Chiasa dan Koita adalah NPC independen. Jangan menganggap skill game, materi kuliah atau ingatan masa kecil Yutaka sudah diwarisi pemain."
    if eid in {"Y-D10", "Y-D11", "Mi-D13", "C-D01", "C-D04", "C-D08", "C-D12", "C-D13", "C-D14", "C-D15", "S-D05"}:
        return "POV khusus adegan ini: host CHIASA. Yutaka, bila hadir, adalah NPC; jangan membuat pemain bercakap dengan Chiasa kedua. Pertahankan cara tutur dan kondisi kode."
    if eid in {"C-D09", "C-D11", "Y-D01", "Y-D02", "Y-D03", "Y-D04", "Y-D05", "Y-D06", "Y-D07", "Y-D08", "Y-D09"}:
        return "POV khusus adegan ini: host YUTAKA. Chiasa, bila hadir, adalah NPC; pemain tidak memiliki ingatan pribadi atau skill rumit Yutaka asli."
    return "POV dapat bergantung pada host yang dipilih. ID event atau karakter pada kk_scene_enter bukan bukti bahwa dialah pemain. Pertahankan guard/cabang host pada acuan; bagian bersama harus masuk akal untuk kedua host. Jangan mengunci jenis kelamin/identitas pemain jika kode tidak menguncinya."


def save(relative, text):
    GENERATED[relative] = text.rstrip() + "\n"


manifest = []
label_users = {}
for eid, (_, label) in GUIDES.items():
    label_users.setdefault(label, []).append(eid)

for row in MAIN + DYNAMIC:
    eid = row["id"]
    guide, label = GUIDES[eid]
    path, code, line = LABELS[label]
    # PANDUAN metadata is context; current label always owns branching truth.
    kind = "milestone" if eid in MAIN_BY_ID else "dinamis"
    if eid in NODES:
        kind = "node_akhir"
    title = row.get("title", row.get("name", eid))
    subdir = focus_for(eid) or "lintas"
    relative = "adegan/" + subdir + "/" + eid + ".md"
    shared = label_users[label]
    restriction = "Tulis ulang hanya event " + eid + "."
    if len(shared) > 1:
        restriction += " PENTING: label ini dipakai bersama oleh " + ", ".join(shared) + ". Keluarkan label lengkap agar dapat diganti dengan aman, tetapi ubah HANYA narasi/dialog yang dimiliki " + eid + "; pertahankan teks, dispatch dan cabang ID lain persis. Jangan menduplikasi label."
    if eid in NODES:
        restriction += " Ini node penutup TANPA menu dan belum dipanggil scheduler. Jangan menambahkan pilihan, if/elif, atau menjadikannya terjadwal. Tulis ketegangan menuju keputusan, tanpa memastikan ending yang belum ditetapkan resolver."
    correction = CORRECTIONS.get(eid, "Jika komentar/katalog bertentangan dengan kode acuan, kode menang. Jangan menambah atau menukar opsi.")
    evidence = json.dumps(row, ensure_ascii=False) + "\n" + guide + "\n" + code
    hook = effects(eid)
    mechanics = ("\n\n### Efek kode yang sudah tertaut — baca saja, JANGAN tulis ulang\n```text\n" + hook + "\n```\nNilai ini hanya penuntun konsekuensi emosional. Jangan mengucapkan nilainya, menjanjikan ending, atau mengeksekusinya lagi.") if hook else ""
    text = f'''# Prompt mandiri Gemini Web — {eid}: {title}

Kamu penulis baru untuk Kouseikan. Anggap ini chat baru: semua konteks yang dibutuhkan ada dalam pesan ini. Jangan mengandalkan percakapan sebelumnya, pengetahuan file repo, atau meminta pengguna menempel bahan tambahan. Naskah acuan di bawah adalah draf yang ingin diganti, bukan gaya yang wajib ditiru.

## Tugas tunggal

{restriction}

Sumber lokal untuk orang yang nanti memasang hasil: `{path.relative_to(ROOT).as_posix()}:{line}`; label `{label}`. Gemini Web tidak perlu dan tidak dianggap dapat membuka path tersebut.

## Premis, waktu, POV dan aturan dunia

{PREMISE}

## Karakter dan hubungan yang perlu diingat dalam prompt INI

{cast_context(evidence, focus_for(eid))}

## Posisi adegan dan batas kontinuitas

{pov_note(eid)}

{nearby(eid)}

Koreksi khusus untuk adegan ini: **{correction}**

### Panduan adegan lokal

```text
{guide}
```

### Data katalog untuk orientasi saja; pilihan aktual tetap dari kode

```json
{json.dumps(row, ensure_ascii=False, indent=2)}
```
{mechanics}

## Sasaran penulisan

{WRITING}

## Kontrak keluaran dan integrasi

{CODE_RULES}

## Label lengkap saat ini — tulis versi penggantinya

```renpy
{code}
```

Sekarang tulis satu versi adegan yang selesai, mengikuti tugas tunggal dan batas di atas. Hanya blok kode pengganti.
'''
    save(relative, text)
    manifest.append({"id": eid, "type": kind, "title": title, "prompt": relative, "source": path.relative_to(ROOT).as_posix(), "line": line, "label": label, "shared_with": shared, "source_sha256": hashlib.sha256(code.encode()).hexdigest()})

ending_source = read(GAME / "kk_ending_story.rpy")
ending_texts = dict(re.findall(r'^    KK_END_TEXT\["([^"]+)"\] = """(.*?)"""', ending_source, re.M | re.S))
ENDING_FOCUS = {"KO": "koita", "BL": "koita", "MI": "miyuki", "NA": "nagisa", "HA": "harumi", "MO": "moeka", "SH": "shiori", "CH": "chiasa", "CF": "chiasa", "YU": "yutaka", "YH": "yutaka"}
for row in ENDINGS:
    eid = row["code"]
    body = ending_texts[eid]
    group = eid.split("-")[1]
    focus = ENDING_FOCUS.get(group)
    title = row.get("name", eid)
    relative = "ending/" + group + "/" + eid + ".md"
    evidence = json.dumps(row, ensure_ascii=False) + "\n" + body
    text = f'''# Prompt mandiri Gemini Web — {eid}: {title}

Kamu penulis baru Kouseikan. Ini chat mandiri. Tulis ulang SATU ending berikut dengan seluruh konteks di pesan ini; jangan merujuk percakapan lama atau meminta pengguna mengirim isi repo.

## Tugas tunggal

Tulis teks ending {eid}. Pertahankan jenis hasil, kondisi muncul, host yang berlaku, tokoh dan konsekuensinya. Jangan membuat akhir bahagia baru jika hasilnya buruk; jangan menukar siapa pelaku/korban/pasangan. Untuk ending yang mencakup beberapa kondisi atau hasil evaluasi, jangan mengunci satu varian yang tidak dijamin metadata. Hanya tulis bagian yang berlaku bersama atau gunakan cara bertutur yang tidak mengubah resolver.

## Premis dan identitas host

{PREMISE}

## Karakter dan hubungan

{cast_context(evidence, focus)}

## Fakta ending yang terkunci

```json
{json.dumps(row, ensure_ascii=False, indent=2)}
```

Metadata ini menetapkan keadaan ending, bukan undangan membuat pilihan baru. Fakta canon dalam profil dan koreksi suara di atas mengalahkan detail prosa lama yang bertentangan.

## Gaya dan bobot cerita

{WRITING}

Ending boleh beberapa paragraf dan sepanjang yang pantas. Wujudkan hidup sesudah peristiwa melalui detail dan perjumpaan konkret; beri akhir yang terasa khusus bagi hasil ini. Jangan sekadar mengulangi syarat katalog, memberi ceramah umum, atau mengakhiri semuanya dengan moral yang sama. Jangan mengasumsikan ending lain terpilih bersamaan kecuali syarat di atas menyebutnya.

## Teks sekarang sebagai draf, boleh dirombak seluruhnya

```text
{body}
```

## Format keluaran wajib

Hanya satu blok kode python berisi assignment berikut dengan isi pengganti:

```python
    KK_END_TEXT["{eid}"] = """Teks ending penuh, boleh beberapa paragraf."""
```

Pertahankan empat spasi di awal assignment karena ia akan masuk ke blok init Python yang SUDAH ADA di `game/kk_ending_story.rpy`. Jangan keluarkan init/label baru, menu, efek, ekspresi interpolasi, ID lain, tiga kutip di tengah isi, atau penjelasan sebelum/sesudah kode. Tidak ada TODO, bagian disingkat, atau permintaan melanjutkan. Periksa sendiri kecocokan host, kondisi dan konsekuensi sebelum menjawab.
'''
    save(relative, text)
    manifest.append({"id": eid, "type": "ending", "title": title, "prompt": relative, "source": "game/kk_ending_story.rpy", "source_sha256": hashlib.sha256(body.encode()).hexdigest()})

assert len(MAIN) == 190 and len(DYNAMIC) == 128 and len(ENDINGS) == 220
assert len(manifest) == 538 and len({r["id"] for r in manifest}) == 538
save("manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))

index = ["# Indeks prompt Gemini Web", "", "Setiap tautan membuka satu prompt lengkap. Salin seluruh isi file itu ke Gemini; file lain tidak perlu ikut ditempel.", "", "[Cara pakai](README.md)", ""]
for kind, title in (("milestone", "Milestone utama"), ("node_akhir", "Delapan node akhir"), ("dinamis", "Event dinamis"), ("ending", "Ending")):
    index += ["## " + title, "", "| ID | Judul | Prompt | Sumber |", "| --- | --- | --- | --- |"]
    for row in manifest:
        if row["type"] != kind:
            continue
        name = row["title"].replace("|", "/")
        source = "../../" + row["source"]
        index.append(f'| {row["id"]} | {name} | [Buka]({row["prompt"]}) | `{row["source"]}` |')
    index.append("")
save("INDEX.md", "\n".join(index))
save("README.md", """# Paket prompt Kouseikan untuk Gemini Web

Tersedia **318 prompt adegan** (190 utama termasuk 8 node akhir, serta 128 dinamis), ditambah **220 prompt ending**. Total **538 prompt mandiri**. Semuanya dibuat dari naskah dan profil di repo; game tidak diubah oleh pembuat paket ini.

## Cara pakai

1. Buka [indeks](INDEX.md), pilih ID adegan yang mau dikerjakan. Contoh awal: [K01](adegan/koita/K01.md), [C01](adegan/chiasa/C01.md), atau [Y01](adegan/yutaka/Y01.md).
2. Buka file prompt, lalu **salin seluruh isinya** ke satu pesan Gemini Web. Boleh memakai chat baru untuk setiap adegan. Tidak perlu mengunggah semua paket atau berharap Gemini mengingat profil dari chat lain.
3. Gemini diminta mengembalikan satu blok label lengkap atau satu assignment ending. Simpan jawabannya dengan ID yang sama. Paket ini tidak memasang keluaran Gemini secara otomatis.
4. Untuk label bersama (misalnya prolog dan beberapa helper), prompt sudah memerintahkan perubahan hanya pada event sasaran. Tetap tinjau agar ID/cabang lain tidak ikut ditimpa.
5. Kalau puas, pasang hasil di label/assignment sumber yang tertulis pada prompt, lalu jalankan lint dan cek katalog. Periksa jumlah/urutan opsi, semua statement mekanik, host, dan kondisi. Lint tidak menilai konsistensi cerita atau mutu dialog.

Isi tiap prompt: premis, POV dua host, suara tokoh terkait, profil lengkap tokoh fokus, profil NPC yang disebut, hubungan awal, panduan lokal, katalog, koreksi kode/katalog, efek hook terkait sebagai referensi, kode/naskah acuan, serta format keluaran. Ending juga punya paket sendiri, contoh [E-KO-01](ending/KO/E-KO-01.md).

## Menjaga kesinambungan versi Gemini

Paket ini merekam sumber saat dibangun. Ia mengulang konteks dasar, tetapi belum mengetahui perubahan yang baru ditulis Gemini dan belum dimasukkan repo. Setelah satu adegan disetujui, masukkan hasilnya lebih dulu lalu bangun ulang paket. Untuk detail baru yang perlu berlaku lintas adegan (misalnya janji pribadi, kebiasaan, atau barang penting), catat di profil/desain yang benar dan tinjau sebelum membangun ulang. Jangan otomatis memperlakukan pilihan A/B/C dari adegan lain sebagai kejadian tetap.

Jika hanya ingin memperbaiki hasil dalam chat Gemini yang sama, kirim instruksi spesifik, misalnya: "Revisi seluruh label terakhir. Kurangi narator yang menjelaskan makna percakapan, tambah interaksi konkret sebelum pilihan, dan beri cabang B akibat yang lebih berbeda. Semua kondisi, opsi dan statement mekanik harus tetap persis seperti prompt awal. Keluarkan label lengkap."

Jika jawaban terpotong, gunakan: "Jawaban terpotong. Lanjutkan persis dari baris terakhir, tanpa mengulang bagian yang sudah ada dan tanpa menutup cabang lebih cepat. Pertahankan indentasi. Sesudah selesai, jangan menambah penjelasan." Gabungkan kedua bagian sebelum memasangnya. Jika konteks chat sudah kacau, mulai chat baru dengan prompt lengkap.

## Pengecualian yang sengaja dipertahankan

- K14/K15 tiga opsi; K19 B=masukan jujur, C=sabotase.
- K17 lima opsi; H08/N10/S10 dua opsi.
- Menu bersyarat, dispatch helper bersama, efek waktu/uang lama, dan percabangan otomatis Mo25 tidak diubah menjadi pola generik.
- Delapan node akhir tetap tidak dijadwalkan; menulisnya tidak menghubungkannya ke scheduler.
- `docs/story_bible.md` tidak dipakai.
- Kekerasan dan krisis boleh ditulis intens, tetapi tanpa metode kekerasan seksual, menyakiti diri, atau prosedur fitnah; Force tidak dibuat menjadi akhir romantis.

## Bangun ulang dan verifikasi paket

Dari root repo dengan PowerShell:

```powershell
& "D:/Punya Patra/Aplikasi/renpy-8.0.3-sdk/lib/py3-windows-x86_64/python.exe" docs/Gemini_Prompts/build_prompts.py
& "D:/Punya Patra/Aplikasi/renpy-8.0.3-sdk/lib/py3-windows-x86_64/python.exe" docs/Gemini_Prompts/build_prompts.py --check
```

Pembuat hanya menulis folder dokumentasi ini. `--check` memeriksa kecocokan seluruh prompt dengan sumber terkini tanpa menulis file. `manifest.json` memetakan ID, file sumber, label bersama dan hash naskah acuan. Sesudah memasang hasil Gemini di game, validasi proyek:

```powershell
& "D:/Punya Patra/Aplikasi/renpy-8.0.3-sdk/lib/py3-windows-x86_64/python.exe" "D:/Punya Patra/Aplikasi/renpy-8.0.3-sdk/renpy.py" . lint
& "D:/Punya Patra/Aplikasi/renpy-8.0.3-sdk/lib/py3-windows-x86_64/python.exe" tests/check_catalog.py
```

Cakupan mesin yang dijaga: 182/190 utama, 128/128 dinamis, 220/220 ending. Delapan node akhir termasuk dalam 190 utama, sehingga total adegan tetap 318.
""")

for relative, content in GENERATED.items():
    path = HERE / relative
    if CHECK:
        assert path.is_file(), "Missing packet: " + relative
        assert read(path) == content, "Stale packet: " + relative
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
mode = "Verified" if CHECK else "Wrote"
print(f"{mode} 318 scene prompts + 220 ending prompts; {len(GENERATED)} documentation files.")
