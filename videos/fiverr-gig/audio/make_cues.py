"""Writes audio/sfx_cues.json for the Fiverr gig video.
Grid: 100 bpm (beat 0.6 s, bar 2.4 s), measured from the reference (reference/ref1.mp4: cuts every 0.6 s,
0.3 s in the dense parts, 0.2 s bursts, a near-empty breath before the finale). 14 bars + tail = 34.8 s.
Edit the cues, re-run this, then audio/sfx_extra.py. STORYBOARD.md describes the picture for every bar."""
import json, os

B = 0.6
def b(n, beat=0.0):  # bar n (1-based) + beats
    return round((n - 1) * 4 * B + beat * B, 4)

C = []
def cue(t, fx, g, label, bus="sfx", end=False, peak=False, **args):
    c = {"t": round(t, 4), "fx": fx, "gain_db": g, "label": label, "bus": bus}
    if args: c["args"] = args
    if end: c["align"] = "end"
    if peak: c["peak"] = True
    C.append(c)

# ---- Bar 1: cold open, chrome builds on every beat (ref 0-2 s: words stack fast)
cue(b(1, 0.5), "spinup", -10, "tape spins up", end=True, dur=0.5)
cue(b(1, 0.5), "tick", -19, "REC dot on", freq=2200, seed=1)
for i in range(1, 8):
    cue(b(1, i / 2 + 0.5), "tick", -26, "timecode tick", freq=3100, seed=2 + i, pan=-0.6)
cue(b(1, 1), "pencil", -15, "dashed circle draws", dur=0.5, seed=3, pan_from=-0.7, pan_to=-0.4)
cue(b(1, 2), "tick", -21, "crosshairs snap on", freq=2600, seed=11, pan=0.5)
cue(b(1, 3), "pencil", -15, "ruler ticks run down the edge", dur=0.5, seed=12, pan_from=-0.9, pan_to=-0.9)

# ---- Bar 2: the terracotta block slams in and shifts on every beat (ref 2.5 s: hard white block flash)
cue(b(2), "sweep", -9, "terracotta block SLAMS in", peak=True, dur=0.5, pan_from=0, pan_to=0, seed=13)
cue(b(2), "felt", -10, "block lands", freq=92, seed=14)
for i, (bt, p) in enumerate(((1, -0.6), (2, 0.6), (3, -0.3))):
    cue(b(2, bt), "sweep", -15, f"block shifts {i + 1}", peak=True, dur=0.4, pan_from=-p, pan_to=p, seed=15 + i)
cue(b(2, 1), "pencil", -16, "bezier curve draws", dur=0.5, seed=18, pan_from=0.3, pan_to=0.8)
cue(b(2, 2), "felt", -13, "play disc lands", freq=98, seed=19)
cue(b(2, 3), "pencil", -18, "play triangle draws", dur=0.3, seed=20)

# ---- Bar 3-4: PRESS, then the title one word per beat (ref 10-17 s: a word every 0.5-0.6 s)
cue(b(3), "press", -6, "PLAY pressed")
cue(b(3), "ripple", -13, "rings spread", base=196)
cue(b(3, 1), "knock", -8, "'Motion'", freq=196, seed=21, pan=-0.2)
cue(b(3, 2), "knock", -6, "'Graphics'", freq=220, seed=22, pan=0.2)
cue(b(3, 2), "impact", -14, "title weight", dur=1.4)
cue(b(3, 2), "subdrop", -14, "title weight (sub)")
cue(b(3, 3), "paper", -18, "italic 'that'", dur=0.2, seed=23)
cue(b(3, 3.5), "paper", -18, "italic 'bring'", dur=0.2, seed=24)
cue(b(4), "sweep", -14, "italic 'ideas' glides in", peak=True, dur=0.45, pan_from=-0.6, pan_to=0.6, seed=25)
cue(b(4, 1), "felt", -15, "'to'", freq=130, seed=26)
cue(b(4, 2), "knock", -7, "'life' lands", freq=247, seed=27)
cue(b(4, 2), "shimmer", -20, "glow on 'life'", dur=1.2, base=587)
# letters scatter (ref 8-10 s): the title breaks into flying letters
cue(b(4, 3), "whoosh", -10, "title SCATTERS into letters", peak=True, dur=0.6, seed=28, pan_from=0, pan_to=0)
for i in range(8):
    cue(b(4, 3) + 0.05 * i + 0.03, "tick", -20 - (i % 3), f"letter {i + 1} flies", freq=1500 + 230 * i, seed=30 + i, pan=(-0.9 + 0.25 * i))

# ---- Bar 5-6: 01 MOTION GRAPHICS & ANIMATION, a change on every beat, then colour slams (ref 17.5-19 s)
cue(b(5), "sweep", -9, "SECTION 01", peak=True, dur=0.6, seed=40)
cue(b(5), "scrub", -22, "label types on", dur=0.35, rate0=28, rate1=32, seed=41)
for i in range(3):
    cue(b(5, 1 + i), "felt", -10 - 2 * i, f"ellipse bounce {i + 1}", freq=112 - 7 * i, seed=42 + i, pan=(-0.3, 0.3, 0)[i])
for i, bt in enumerate((0, 1, 1.5, 2)):  # colour panel slams, accelerating
    cue(b(6, bt), "sweep", -12 + (i == 0) * 2, f"colour panel slam {i + 1}", peak=True, dur=0.35, pan_from=(-0.8, 0.8)[i % 2], pan_to=(0.8, -0.8)[i % 2], seed=46 + i)
    cue(b(6, bt), "felt", -14, f"panel lands {i + 1}", freq=(98, 110, 123, 131)[i], seed=50 + i)
cue(b(6, 2.5), "swell", -14, "shape morphs", end=True, dur=0.5, freq=147)
cue(b(6, 3), "pencil", -15, "bezier handle snaps the curve", dur=0.4, seed=54)
cue(b(6, 3), "tick", -21, "keyframe diamonds", freq=2900, seed=55, pan=0.4)

# ---- Bar 7-8: 02 VIDEO EDITING, clips snap per beat, then cuts on half-beats
cue(b(7), "sweep", -9, "SECTION 02", peak=True, dur=0.6, pan_from=0.9, pan_to=-0.9, seed=60)
cue(b(7), "shutter", -13, "frame flash", seed=61)
cue(b(7), "scrub", -22, "label types on", dur=0.3, rate0=28, rate1=32, seed=62)
for i, p in enumerate((-0.5, 0.0, 0.5)):
    cue(b(7, 1 + i), "snap", -8, f"clip {i + 1} snaps on", seed=63 + i, pan=p)
cue(b(8), "scrub", -12, "playhead scrubs", dur=0.6, seed=66)
for i in range(5):
    cue(b(8, 1 + i / 2), "shutter", -10 + 0.5 * i, f"cut {i + 1}", seed=67 + i, pan=(-0.4, 0.4, -0.2, 0.2, 0)[i])

# ---- Bar 9: 03 SMOOTH TRANSITIONS & VISUAL EFFECTS
cue(b(9), "whoosh", -8, "SECTION 03", peak=True, dur=0.6, seed=80)
cue(b(9), "scrub", -22, "label types on", dur=0.45, rate0=28, rate1=32, seed=81)
cue(b(9, 1), "sweep", -11, "panel wipe right-to-left", peak=True, dur=0.45, pan_from=0.8, pan_to=-0.8, seed=82)
cue(b(9, 2), "sweep", -11, "panel wipe left-to-right", peak=True, dur=0.45, pan_from=-0.8, pan_to=0.8, seed=83)
cue(b(9, 3), "riser", -14, "into the zoom-through", end=True, dur=0.6, f0=300, f1=1600, seed=84)
cue(b(9, 3), "whoosh", -8, "zoom-through", peak=True, dur=0.5, seed=85, pan_from=0, pan_to=0)

# ---- Bar 10: THE PEAK, a repeating tile grid flipping colour every half-beat, ending in a 0.2 s burst (ref 26-32 s)
cue(b(10), "shimmer", -19, "light leak over the grid", dur=2.2, base=440)
for i in range(6):
    t = b(10, i / 2)
    cue(t, "snap", -7 if i % 2 == 0 else -10, f"grid flips colour {i + 1}", seed=90 + i, pan=(-0.5, 0.5)[i % 2])
    if i % 2 == 0:
        cue(t, "sweep", -12, f"grid slides {i // 2 + 1}", peak=True, dur=0.3, pan_from=-0.6, pan_to=0.6, seed=100 + i)
for i in range(3):
    cue(b(10, 3) + 0.2 * i, "shutter", -8 + i, f"burst {i + 1}", seed=110 + i, pan=(-0.5, 0.5, 0)[i])

# ---- Bar 11: 15s . 30s . 60s PACKAGES on the beats
for i, (bt, f, txt) in enumerate(((0, 196, "15S"), (1, 233, "30S"), (2, 294, "60S"))):
    cue(b(11, bt), "knock", -9 + i, f"package {txt} locks in", freq=f, seed=120 + i, pan=(-0.4, 0, 0.4)[i])
    cue(b(11, bt), "scrub", -23, f"timecode rolls to {txt}", dur=0.25, rate0=30, rate1=36, seed=123 + i)
cue(b(11, 3), "felt", -13, "'PACKAGES' settles", freq=104, seed=126)

# ---- Bar 12: THE BREATH, everything drops out, small type ticks on (ref 32.5-36 s)
cue(b(12), "tapestop", -11, "everything stops", dur=0.5)
for i, ch in enumerate("BY EVAN"):
    if ch != " ":
        cue(b(12, 1) + 0.09 * i, "key", -24, f"types '{ch}'", seed=130 + i)
cue(b(13), "riser", -12, "into the finale", end=True, dur=1.6, seed=140)
cue(b(13), "swell", -10, "into the finale", end=True, dur=1.0, freq=73.42)

# ---- Bar 13-14: FINALE LOCKUP (the thumbnail), held like the reference's stretched last word
cue(b(13), "impact", -6, "LOCKUP: title + three columns", dur=2.8)
cue(b(13), "subdrop", -9, "LOCKUP sub")
cue(b(13), "knock", -8, "title stamp", freq=196, seed=141)
cue(b(13), "ripple", -14, "rings behind the play button", base=146.83)
cue(b(13, 1), "felt", -14, "BY EVAN settles", freq=92, seed=142, pan=-0.5)
for i in range(3):
    cue(b(13, 2) + 0.15 * i, "tick", -21, f"'15S . 30S . 60S' corner label {i + 1}", freq=2400, seed=143 + i, pan=0.6)
cue(b(13, 2), "shimmer", -20, "lockup glow", dur=3.0, base=587)
cue(b(14), "press", -14, "play button breathes (CTA)", seed=146)
cue(b(14), "ripple", -19, "CTA ring", base=196, seed=147)

# ---- bed bus: drone (ducked in the breath) + a soft pulse on every beat while the reel is running
DUR = 34.8
cue(0, "bed", 0, "warm drone bed", bus="bed", dur=DUR, dips=[[b(12), b(13) - 0.3, 0.12]])
for n in range(3, 12):
    for bt in range(4):
        cue(b(n, bt), "pulse", -6 if bt == 0 else -11, f"bar {n} beat {bt + 1} pulse", bus="bed", seed=200 + n * 4 + bt)
for t in (b(13), b(14)):
    cue(t, "pulse", -5, "finale pulse", bus="bed", seed=260 + int(t))

cfg = {"duration": DUR,
       "room_env": [[0, 0.9], [2.3, 0.5], [4.8, 0.15], [26.3, 0.15], [26.6, 0.9], [28.6, 0.6], [28.8, 0.1], [31, 0.35], [DUR, 0.35]],
       "cues": C}
json.dump(cfg, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sfx_cues.json"), "w"), indent=1)
print(f"{len(C)} cues, {DUR}s")
