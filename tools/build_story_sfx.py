"""Synthesize wordless environmental and prop sounds for Kouseikan."""
from array import array
from math import exp, pi, sin, tanh
from pathlib import Path
from random import Random
from struct import pack

RATE = 24000
TAU = 2 * pi
OUT = Path(__file__).resolve().parents[1] / "game/audio/sfx"
rng = Random(831)


class Clip:
    def __init__(self, seconds):
        self.frames = round(seconds * RATE)
        self.left = array("f", [0]) * self.frames
        self.right = array("f", [0]) * self.frames

    def layer(self, at, seconds, sound, gain, pan=0):
        start = round(at * RATE)
        for i in range(min(round(seconds * RATE), self.frames - start)):
            x = sound(i / RATE) * gain
            self.left[start + i] += x * (1 - pan)
            self.right[start + i] += x * (1 + pan)

    def save(self, name, looping=False):
        pcm = array("h")
        delay = round(0.037 * RATE)
        for i, (left, right) in enumerate(zip(self.left, self.right)):
            if looping or i >= delay:
                left += 0.13 * self.right[i - delay]
                right += 0.13 * self.left[i - delay]
            fade = 1 if looping else min(1, (self.frames - 1 - i) / 260)
            pcm.extend((round(tanh(left) * 30000 * fade), round(tanh(right) * 30000 * fade)))
        data = pcm.tobytes()
        header = pack("<4sI4s4sIHHIIHH4sI", b"RIFF", len(data) + 36, b"WAVE",
                      b"fmt ", 16, 1, 2, RATE, RATE * 4, 4, 16, b"data", len(data))
        (OUT / (name + ".wav")).write_bytes(header + data)


def noise(color):
    previous = 0

    def sample(t):
        nonlocal previous
        white = rng.uniform(-1, 1)
        previous += color * (white - previous)
        return previous

    return sample


def strike(pitches, decay, grit=0.2):
    rough = noise(0.6)
    return lambda t: min(1, 350*t) * (
        exp(-decay*t) * sum(sin(TAU*f*t) for f in pitches)/len(pitches)
        + grit * exp(-43*t)*rough(t)
    )


def voice_like(frequency, length, gasp=False):
    breath = noise(0.32)
    # A single resonant exhalation or startled cry, with no syllables.
    def sample(t):
        blend = sin(pi*t/length) ** 1.7
        phase = TAU*(frequency*t + (68 if gasp else 9)*t*t/length)
        throat = sum(sin(h*phase)/h for h in (1, 2, 3, 5, 7))
        return blend * (0.44*throat + 0.46*breath(t))
    return sample


def crowd(name, panic):
    seconds = 8
    clip = Clip(seconds)
    air = noise(0.095)
    clip.layer(0, seconds, lambda t: air(t)*sin(pi*t/seconds)**0.3, 0.24)
    for i in range(66 if panic else 106):
        length = rng.uniform(0.22, 0.85)
        at = rng.uniform(0, seconds-length)
        clip.layer(at, length, voice_like(rng.uniform(100, 310), length),
                   rng.uniform(0.017, 0.055), rng.uniform(-0.8, 0.8))
    for at in (0.06, 0.42, 1.2, 2.3, 3.45, 5.7) if panic else ():
        length = rng.uniform(0.58, 1.12)
        clip.layer(at, length, voice_like(rng.uniform(330, 510), length, True),
                   rng.uniform(0.12, 0.21), rng.uniform(-0.73, 0.73))
    for i in range(28):
        clip.layer(rng.uniform(0.05, 7.7), 0.2, strike((69, 119), 26, 1.1),
                   0.062 if panic else 0.034, rng.uniform(-0.8, 0.8))
    clip.save(name, looping=True)


def train():
    rail = Clip(8)
    rumble = noise(0.063)
    rail.layer(0, 8, lambda t: (rumble(t)*1.85 + 0.22*sin(TAU*52*t))
               * (0.82 + 0.18*sin(TAU*9*t)) * sin(pi*t/8)**0.15, 0.57)
    for i in range(54):
        rail.layer(i*0.142, 0.22, strike((81, 173, 620), 19, 0.9), 0.055, (-1)**i*0.33)
    rail.save("train_rail", looping=True)

    horn = Clip(2.45)
    horn.layer(0, 2.45, lambda t: min(1, 9*t)*exp(-1.8*max(0,t-1.45))
               * sum(sin(TAU*(f*t + 2*t*t)) + 0.23*sin(TAU*2*f*t)
                     for f in (295, 374, 445))/3, 0.58, -0.24)
    horn.save("train_horn")

    brake = Clip(2.25)
    scrape = noise(0.62)
    brake.layer(0, 2.25, lambda t: min(1, 5*t)*exp(-0.82*t) * (
        0.37*sin(TAU*(1650*t - 140*t*t) + 0.7*sin(47*t))
        + 0.24*sin(TAU*(2511*t - 170*t*t))
        + 0.74*scrape(t)), 0.56, 0.22)
    brake.save("train_brake")

    hit = Clip(0.82)
    hit.layer(0, 0.82, strike((47, 62, 135, 260), 9, 1.9), 0.83)
    hit.layer(0.036, 0.5, strike((143, 418, 927), 18, 0.9), 0.26, 0.32)
    hit.save("train_impact")


def props():
    specs = {
        "system_open": (0.72, [(0, (1175, 2352, 3087), 8, 0.32),
                               (0.078, (1760, 3515, 4203), 8, 0.22)]),
        "system_close": (0.48, [(0, (940, 1882), 12, 0.17), (0.075, (630, 1261), 16, 0.14)]),
        "phone_drop": (0.46, [(0, (173, 568, 2100), 32, 0.48), (0.094, (630, 2200), 44, 0.20)]),
        "ceramic": (1.8, [(0.12, (1070, 1489, 3010), 13, 0.21),
                         (0.29, (1100, 1910, 3280), 19, 0.19),
                         (1.02, (138, 205, 430), 22, 0.20), (1.37, (109, 224), 23, 0.16)]),
        "door_knock": (0.85, [(0, (103, 210, 470), 32, 0.45),
                             (0.165, (109, 208, 430), 31, 0.40),
                             (0.34, (116, 225, 438), 30, 0.35)]),
        "door_close": (0.44, [(0, (85, 129, 310), 19, 0.54), (0.048, (729, 1829), 36, 0.15)]),
        "footsteps": (1.28, [(i*0.205, (85+i*5, 169, 335), 29, 0.21+i*0.042) for i in range(6)]),
        "school_clatter": (0.9, [(0, (97, 163), 19, 0.52), (0.055, (1780, 2599, 4002), 9, 0.27),
                                 (0.21, (145, 371, 551), 25, 0.25), (0.33, (2154, 2980), 10, 0.17)]),
        "bamboo": (0.62, [(0, (299, 707, 1148), 15, 0.38), (0.057, (500, 893), 21, 0.11)]),
        "fireworks": (3.25, [(0, (42, 69, 90), 5, 0.54), (0.44, (77, 139), 9, 0.22),
                             (1.38, (48, 81, 121), 5, 0.42), (2.17, (43, 73, 118), 5, 0.53)]),
    }
    for name, (duration, hits) in specs.items():
        clip = Clip(duration)
        for i, (at, pitches, decay, gain) in enumerate(hits):
            clip.layer(at, duration-at, strike(pitches, decay, 0.8 if name in ("footsteps", "fireworks") else 0.26),
                       gain, (-1)**i * 0.18)
        if name == "ceramic":
            steam = noise(0.43)
            clip.layer(0.33, 1.29, lambda t: steam(t)*sin(pi*t/1.29), 0.16, 0.28)
        if name == "fireworks":
            for _ in range(55):
                clip.layer(rng.uniform(0.12, 3), 0.09, strike((530, 910, 1560), 56, 2),
                           rng.uniform(0.018, 0.077), rng.uniform(-0.7, 0.7))
        clip.save(name)

    for name, bursts in (("phone_vibrate", (0, 0.62, 1.25)), ("phone_buzz", (0,))):
        length = 0.33 if name == "phone_vibrate" else 0.15
        clip = Clip(bursts[-1]+length+0.11)
        for at in bursts:
            clip.layer(at, length, lambda t: sin(pi*t/length)**0.45 * (
                0.69*sin(TAU*151*t) + 0.24*sin(TAU*302*t) + 0.14*sin(TAU*619*t)), 0.37, 0.29)
        clip.save(name)

    rain = Clip(6.8)
    for pan in (-0.63, 0.63):
        water = noise(0.49)
        rain.layer(0, 6.8, lambda t: water(t)*min(1, t*3, (6.8-t)/1.05), 0.28, pan)
    for _ in range(142):
        at = rng.uniform(0.1, 6.4)
        rain.layer(at, 0.16, strike((rng.randrange(760, 1950), 2350), 46, 0.55),
                   rng.uniform(0.035, 0.15), rng.uniform(-0.8, 0.8))
    rain.save("rain")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    crowd("platform_crowd", False)
    crowd("platform_panic", True)
    train()
    props()
