"""Render Kouseikan's original, seamless instrumental loops using Python."""

from array import array
from functools import lru_cache
from math import exp, pi, sin
from pathlib import Path
from struct import pack
import sys


RATE = 24000
OUTPUT = Path(__file__).resolve().parents[1] / "game" / "audio" / "bgm"

# Chords are voiced above a bass note. Phrase entries are melody offsets in
# semitones from the current chord root, with None leaving a beat to breathe.
MAJOR = [(48, 4, 7, 11), (45, 3, 7, 10), (41, 4, 7, 11), (43, 4, 7, 9)]
MINOR = [(45, 3, 7, 14), (41, 4, 7, 11), (48, 4, 7, 14), (43, 3, 7, 9)]
UNCERTAIN = [(45, 3, 6, 10), (42, 3, 7, 10), (41, 4, 7, 11), (47, 3, 6, 10)]
LYRICAL = (19, None, 14, 16, 19, 21, None, 14)
QUESTION = (14, None, 19, None, 15, 17, None, 12)
DANCE = (12, 19, 16, None, 21, 19, 14, 16)

# Lead line in written pitch, with pickups and space for the piano response.
TITLE_MELODY = (
    ((0, 76), (0.75, 79), (1.5, 81), (2, 79), (3, 76), (3.5, 74)),
    ((0, 74), (1, 71), (1.75, 74), (2.5, 79), (3.5, 78)),
    ((0, 76), (0.75, 72), (1.5, 76), (2, 79), (3, 81)),
    ((0, 77), (1, 74), (1.75, 72), (2.5, 69), (3.5, 74)),
    ((0, 76), (0.75, 79), (1.5, 81), (2, 84), (3.25, 79)),
    ((0, 81), (1, 76), (1.75, 74), (2.5, 71), (3.5, 74)),
    ((0, 77), (0.75, 81), (1.5, 84), (2.5, 86), (3.25, 84)),
    ((0, 83), (0.75, 79), (1.5, 77), (2, 74), (3, 79), (3.5, 74)),
)

# BPM, transposition, harmony, lead instrument, phrase, backing pattern.
SCORE = {
    "title": (116, 0, [(48, 4, 7, 9), (43, 4, 7, 9), (45, 3, 7, 10), (41, 4, 7, 9),
                       (48, 4, 7, 9), (40, 3, 7, 10), (41, 4, 7, 9), (43, 4, 7, 10)],
              "bell", TITLE_MELODY, "title"),
    "campus": (104, 0, MAJOR, "pluck", DANCE, "arpeggio"),
    "city": (112, 5, MAJOR, "electric", DANCE, "pulse"),
    "home": (86, 5, MAJOR, "piano", LYRICAL, "arpeggio"),
    "quiet": (69, -2, MINOR, "piano", QUESTION, "sparse"),
    "night": (72, 3, MINOR, "electric", QUESTION, "sparse"),
    "retreat": (80, 7, MAJOR, "bell", LYRICAL, "sparse"),
    "platform": (97, -2, MINOR, "electric", QUESTION, "pulse"),
    "tension": (105, -5, UNCERTAIN, "pluck", (12, None, 18, 12, None, 15, 18, None), "pulse"),
    "system": (88, 0, UNCERTAIN, "bell", (18, None, 15, 22, None, 13, None, 18), "sparse"),
    "intimacy": (73, 5, MAJOR, "piano", (16, 19, None, 21, 19, None, 14, 12), "sparse"),
    "aftermath": (62, -3, MINOR, "piano", (15, None, None, 14, 12, None, 7, None), "sparse"),
    "graduation": (82, 7, MAJOR, "piano", (12, 16, 19, None, 24, 21, 19, None), "arpeggio"),
    "koita": (88, 2, MAJOR, "piano", (12, None, 16, 19, 17, None, 16, 14), "arpeggio"),
    "yutaka": (77, -2, MINOR, "electric", (12, 19, None, 15, None, 14, 19, None), "sparse"),
    "chiasa": (92, 7, MAJOR, "pluck", (19, 16, None, 14, 12, 16, 19, None), "arpeggio"),
    "miyuki": (78, 3, MAJOR, "bell", (16, None, 19, 21, None, 19, 16, 14), "sparse"),
    "nagisa": (116, 2, MAJOR, "pluck", (19, 19, 16, 12, None, 14, 19, 21), "pulse"),
    "harumi": (85, 0, MAJOR, "piano", (12, 14, 16, None, 19, 16, None, 12), "arpeggio"),
    "moeka": (102, 5, MAJOR, "electric", (None, 12, 16, 21, 19, None, 16, 19), "pulse"),
    "shiori": (74, 2, MINOR, "piano", (19, None, 15, 14, None, 12, 15, None), "arpeggio"),
}


@lru_cache(maxsize=256)
def voice(instrument, pitch, length):
    frequency = 440 * 2 ** ((pitch - 69) / 12)
    step = 2 * pi * frequency / RATE
    samples = array("f")
    for index in range(length):
        t = index / RATE
        phase = step * index
        attack = min(1, t / (0.19 if instrument == "pad" else 0.012))
        release = min(1, (length - index) / (RATE * 0.14))
        fundamental = sin(phase)
        if instrument == "piano":
            tone = fundamental * exp(-1.5 * t) + (0.27 * sin(2.002 * phase)
                    + 0.13 * sin(3.013 * phase)) * exp(-5 * t)
        elif instrument == "pluck":
            tone = (fundamental + 0.36 * sin(2 * phase) + 0.21 * sin(3 * phase)) * exp(-5.5 * t)
        elif instrument == "bell":
            tone = fundamental * exp(-2.6 * t) + 0.23 * sin(2.76 * phase) * exp(-7 * t)
        elif instrument == "electric":
            tone = sin(phase + 0.7 * exp(-3.4 * t) * sin(2 * phase)) * exp(-1.8 * t)
        else:
            tone = 0.44 * (fundamental + sin(1.003 * phase)) + 0.12 * sin(2 * phase)
        samples.append(tone * attack * release)
    return samples


def render(path, bpm, transpose, chords, lead, phrase, arrangement):
    beat = 60 / bpm
    size = round(32 * beat * RATE)
    left, right = array("f", [0]) * size, array("f", [0]) * size

    def note(at, duration, pitch, instrument, level, pan):
        onset = round(at * beat * RATE)
        for index, sample in enumerate(voice(instrument, pitch, round(duration * beat * RATE))):
            position = (onset + index) % size
            left[position] += sample * level * (1 - pan)
            right[position] += sample * level * (1 + pan)

    for bar in range(8):
        root, third, fifth, color = chords[bar % len(chords)]
        root += transpose
        start = bar * 4
        if arrangement == "title":
            for offset, bass in ((0, root), (2, root if bar == 7 else root + fifth)):
                note(start + offset, 0.86, bass - 12, "electric", 0.13, 0)
            for offset in (0.5, 1.5, 2.75, 3.5):
                for interval in (third, fifth, color):
                    duration = min(0.56, 3.69 - offset) if bar == 7 else 0.56
                    note(start + offset, duration, root + 12 + interval, "piano", 0.048, -0.31)
            for offset, pitch in phrase[bar]:
                duration = min(0.89, 3.69 - offset) if bar == 7 else 0.89
                note(start + offset, duration, pitch, lead, 0.145, 0.23)
                note(start + offset, min(0.62, duration), pitch - 12, "pluck", 0.055, -0.08)
            continue
        note(start, 3.9, root - 12, "pad", 0.093, 0)
        note(start + 0.06, 4.13, root + third, "pad", 0.040, -0.27)
        note(start + 0.14, 4.02, root + color, "pad", 0.034, 0.28)
        if arrangement == "arpeggio":
            backing = [(0, 0), (0.75, fifth), (1.5, third + 12), (2.5, color), (3.25, fifth)]
        elif arrangement == "pulse":
            backing = [(0, 0), (1.5, fifth), (2, 12), (2.75, third + 12), (3.5, fifth)]
        else:
            backing = [(0, fifth), (2.5, color)]
        for at, interval in backing:
            note(start + at, 1.65, root + interval, "pluck" if arrangement == "pulse" else "piano",
                 0.087, -0.29)

        for index, interval in enumerate(phrase[(bar % 2) * 4:(bar % 2) * 4 + 4]):
            if interval is None or (arrangement == "sparse" and index == 3 and bar % 2 == 0):
                continue
            # Keep chord thirds in the melody consistent when the harmony changes.
            if interval in (15, 16):
                interval = 12 + third
            if bar in (3, 7) and index == 2:
                interval = 12 if bar == 7 else 14
            at = start + (0.5, 1.25, 2.0, 3.0)[index]
            note(at, 1.65 if arrangement == "pulse" else 2.35, root + interval, lead, 0.15, 0.18)

    # Circular reflections preserve the stereo reverb tail across the loop point.
    delay_a, delay_b = round(0.087 * RATE), round(0.153 * RATE)
    pcm = array("h")
    for index in range(size):
        l = left[index] + 0.18 * right[index - delay_a] + 0.09 * left[index - delay_b]
        r = right[index] + 0.18 * left[index - delay_b] + 0.09 * right[index - delay_a]
        pcm.extend((round(l * 24000), round(r * 24000)))

    if sys.byteorder != "little":
        pcm.byteswap()
    data = pcm.tobytes()
    header = pack("<4sI4s4sIHHIIHH4sI", b"RIFF", len(data) + 36, b"WAVE",
                  b"fmt ", 16, 1, 2, RATE, RATE * 4, 4, 16, b"data", len(data))
    path.write_bytes(header + data)


if __name__ == "__main__":
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for cue, settings in SCORE.items():
        render(OUTPUT / (cue + ".wav"), *settings)
        print(cue, flush=True)
