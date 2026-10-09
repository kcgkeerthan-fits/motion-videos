"""Project sound palette for the Fiverr gig video: warm, tactile, editorial. Adds generators to the
skill's sfx_lib, then runs the skill's build_sfx.py. Pops are banned in this project (client dislikes them):
landings use felt / knock / click instead.

  python3 audio/sfx_extra.py <project>      (same args as build_sfx.py)
"""
import os
import runpy
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SFX_DIR = os.path.abspath(os.path.join(HERE, "..", "..", "..", "motion-studio-skill", "scripts", "sfx"))
sys.path.insert(0, SFX_DIR)
import sfx_lib as L  # noqa: E402

SR = L.SR


def felt(seed=40, freq=118, dur=0.32, pan=0.0):
    """Soft felt-mallet thud: a shape landing, no chirp, no click."""
    r = L.rng(seed)
    t = L.t_axis(dur)
    f = freq * (1 + 0.35 * np.exp(-t / 0.012))
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.07)
    thud = L.fft_filter(r.standard_normal(len(t)), lo=60, hi=700) * np.exp(-t / 0.018) * 0.5
    return L.stereo(L.norm(np.tanh(1.3 * (body + thud)), 0.7), pan)


def knock(seed=41, freq=210, dur=0.9, pan=0.0):
    """Letterpress / wood knock with a short room: a serif word stamping onto the page."""
    r = L.rng(seed)
    t = L.t_axis(dur)
    modes = sum(np.sin(2 * np.pi * freq * m * t + r.uniform(0, 3)) * np.exp(-t / (0.05 / m)) / m for m in (1, 2.31, 3.9))
    tap = L.fft_filter(r.standard_normal(len(t)), lo=900, hi=5000) * np.exp(-t / 0.003) * 0.5
    low = np.sin(2 * np.pi * 62 * t) * np.exp(-t / 0.09) * 0.6
    st = L.stereo(L.norm(modes + tap + low, 0.8), pan)
    return L.reverb(st, decay=0.7, mix=0.22, seed=seed, tone=4000)


def press(seed=42, pan=0.0):
    """Tactile button press + release (mechanical, no tone): the play button."""
    r = L.rng(seed)
    t = L.t_axis(0.22)
    n = len(t)
    down = L.fft_filter(r.standard_normal(n), lo=1200, hi=6000) * np.exp(-t / 0.0025)
    body = np.sin(2 * np.pi * 140 * t) * np.exp(-t / 0.025) * 0.9
    up = np.zeros(n)
    k = int(0.095 * SR)
    up[k:] = L.fft_filter(r.standard_normal(n - k), lo=2000, hi=8000) * np.exp(-np.arange(n - k) / SR / 0.002) * 0.45
    return L.stereo(L.norm(down + body + up, 0.75), pan)


def pencil(seed=43, dur=1.0, pan_from=-0.3, pan_to=0.3):
    """Graphite/stroke draw-on: grainy scratch that follows a line being drawn."""
    r = L.rng(seed)
    n = int(dur * SR)
    t = np.arange(n) / SR
    x = r.standard_normal(n)
    grain = np.abs(L.fft_filter(r.standard_normal(n), hi=60)) * 3 + 0.3
    centers = 2600 + 1400 * np.sin(2 * np.pi * 1.7 * t) ** 2
    mono = L.time_varying_bandpass(x, centers, q=2.2) * grain
    env = np.minimum(1, t / 0.06) * np.minimum(1, (dur - t) / 0.12)
    mono = mono * env
    p = t / dur
    a = ((pan_from + (pan_to - pan_from) * p) + 1) * np.pi / 4
    return L.norm(np.stack([mono * np.cos(a), mono * np.sin(a)], axis=1), 0.45).astype(np.float32)


def ripple(seed=44, base=196, dur=2.2):
    """Concentric rings spreading out: soft bowl tone with slow beating, wide reverb."""
    t = L.t_axis(dur)
    tone = sum(np.sin(2 * np.pi * base * m * t) * np.exp(-t / (0.9 / m)) / m for m in (1, 2.0, 2.98, 4.1))
    beat = 0.75 + 0.25 * np.sin(2 * np.pi * 3.2 * t)
    st = L.stereo(L.norm(tone * beat * np.minimum(1, t / 0.01), 0.5))
    return L.reverb(st, decay=2.2, mix=0.45, seed=seed, tone=3000)


def spinup(seed=45, dur=0.9):
    """Tape spinning up to speed (reverse tape stop): the reel starts."""
    return np.ascontiguousarray(L.tape_stop(dur=dur, seed=seed)[::-1])


def scrub(seed=46, dur=1.2, rate0=10, rate1=34):
    """Playhead scrubbing a timeline: accelerating dry ticks with drifting pitch."""
    r = L.rng(seed)
    n = int(dur * SR)
    out = np.zeros(n)
    tt, i = 0.0, 0
    while tt < dur - 0.03:
        p = tt / dur
        k = int(tt * SR)
        g = L.t_axis(0.025)
        f = 1800 + 900 * r.uniform(-1, 1)
        s = np.sin(2 * np.pi * f * g) * np.exp(-g / 0.004) + L.fft_filter(r.standard_normal(len(g)), lo=2500) * np.exp(-g / 0.0015) * 0.5
        out[k : k + len(s)] += s[: n - k] * (0.5 + 0.5 * p)
        tt += 1.0 / (rate0 + (rate1 - rate0) * p)
        i += 1
    return L.stereo(L.norm(out, 0.45), 0.15)


def sweep(seed=47, dur=0.9, pan_from=-0.9, pan_to=0.9):
    """A softer, darker whoosh for panel wipes (less hiss than the stock whoosh)."""
    return L.whoosh(dur=dur, f_lo=140, f_hi=1800, pan_from=pan_from, pan_to=pan_to, seed=seed)


def bed(seed=48, dur=32.0, root=73.42):
    """Low warm drone bed (D2 + A2 + F3 colour), slow breathing. Glue for a no-music cut; mute it under music."""
    r = L.rng(seed)
    t = L.t_axis(dur)
    out = np.zeros(len(t))
    for m, g in ((1, 1.0), (1.5, 0.55), (2, 0.35), (2.378, 0.18), (3, 0.12)):
        det = r.uniform(-0.25, 0.25)
        out += g * (np.sin(2 * np.pi * (root * m + det) * t) + np.sin(2 * np.pi * (root * m - det) * t + 1.3))
    breath = 0.8 + 0.2 * np.sin(2 * np.pi * t / 5.0)  # one breath per 2 bars at 96 bpm
    air = L.fft_filter(r.standard_normal(len(t)), lo=500, hi=3000) * 0.04
    mono = L.fft_filter(out, hi=900) * breath + air
    env = np.minimum(1, t / 2.0) * np.minimum(1, (dur - t) / 3.0)
    st = np.stack([mono, np.roll(mono, 911)], axis=1) * env[:, None]
    return L.norm(st, 0.6)


def pulse(seed=49, dur=0.5):
    """Soft heartbeat kick on the bar line: keeps the silent tempo audible without being music."""
    t = L.t_axis(dur)
    f = 48 + 60 * np.exp(-t / 0.03)
    k = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.12)
    return L.stereo(L.norm(np.tanh(1.2 * k), 0.8))


L.GENERATORS.update(felt=felt, knock=knock, press=press, pencil=pencil, ripple=ripple, spinup=spinup,
                    scrub=scrub, sweep=sweep, bed=bed, pulse=pulse)
L.GENERATORS.pop("pop", None)  # banned for this project

if __name__ == "__main__":
    sys.argv = [os.path.join(SFX_DIR, "build_sfx.py")] + sys.argv[1:]
    runpy.run_path(sys.argv[0], run_name="__main__")
