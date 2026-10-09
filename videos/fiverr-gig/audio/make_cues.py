"""Writes audio/sfx_cues.json for the Fiverr gig video. Grid: 96 bpm, beat 0.625 s, bar 2.5 s, 32 s total.
Edit the CUES table, re-run this, then audio/sfx_extra.py. Times are the storyboard's (STORYBOARD.md)."""
import json, os

B = 0.625          # one beat
def bar(n, beat=0):  # bar n (1-based), plus beats
    return round((n - 1) * 4 * B + beat * B, 4)

C = []
def cue(t, fx, g, label, bus="sfx", **kw):
    c = {"t": round(t, 4), "fx": fx, "gain_db": g, "label": label, "bus": bus}
    if "args" in kw: c["args"] = kw["args"]
    if kw.get("end"): c["align"] = "end"
    if kw.get("peak"): c["peak"] = True
    C.append(c)

# ---- Bar 1-2: cold open on dark green, the reel switches on
cue(bar(1, 1), "spinup", -10, "tape spins up as the frame wakes", end=True, args={"dur": 0.6})
cue(bar(1, 1), "tick", -20, "REC dot blinks on", args={"freq": 2200, "seed": 1})
for i, b in enumerate((2, 3)):
    cue(bar(1, b), "tick", -25, "timecode ticks", args={"freq": 3100, "seed": 2 + i, "pan": -0.6})
cue(bar(1, 2), "pencil", -15, "dashed circle draws (top-left)", args={"dur": 0.9, "seed": 3, "pan_from": -0.7, "pan_to": -0.4})
cue(bar(1, 3), "tick", -23, "crosshair marks appear", args={"freq": 2600, "seed": 5, "pan": 0.5})
cue(bar(2), "pencil", -14, "bezier curve draws (bottom-right)", args={"dur": 1.2, "seed": 4, "pan_from": 0.2, "pan_to": 0.8})
cue(bar(2, 2), "felt", -15, "play button disc lands centre", args={"freq": 98, "seed": 6})
cue(bar(2, 3), "pencil", -17, "play triangle draws", args={"dur": 0.4, "seed": 7, "pan_from": -0.1, "pan_to": 0.1})

# ---- Bar 3-4: PRESS -> title
cue(bar(3), "press", -6, "PLAY is pressed")
cue(bar(3), "ripple", -12, "rings spread from the button", args={"base": 196})
cue(bar(3, 1), "sweep", -10, "terracotta column wipes open", peak=True, args={"dur": 0.8, "pan_from": 0, "pan_to": 0, "seed": 8})
cue(bar(3, 2), "swell", -12, "into 'Motion'", end=True, args={"dur": 1.0, "freq": 98})
cue(bar(3, 2), "knock", -7, "'Motion' stamps in", args={"freq": 196, "seed": 9, "pan": -0.2})
cue(bar(3, 3), "knock", -6, "'Graphics' stamps in", args={"freq": 220, "seed": 10, "pan": 0.2})
cue(bar(3, 3), "impact", -11, "title weight", args={"dur": 1.6})
cue(bar(3, 3), "subdrop", -13, "title weight (sub)")
cue(bar(4), "sweep", -15, "italic 'that bring ideas' glides in", peak=True, args={"dur": 0.7, "pan_from": -0.6, "pan_to": 0.6, "seed": 11})
cue(bar(4, 1), "paper", -19, "italic settles", args={"dur": 0.3, "seed": 12})
cue(bar(4, 2), "knock", -8, "'to life' lands", args={"freq": 247, "seed": 13})
cue(bar(4, 2), "shimmer", -19, "warm glow on 'to life'", args={"dur": 2.2, "base": 587})
for i, (b, f) in enumerate(((3, 130), (3.25, 116), (3.5, 103))):
    cue(bar(4, b), "felt", -14 - i, f"leaning ellipse {i + 1} falls into place", args={"freq": f, "seed": 14 + i, "pan": -0.3 + 0.3 * i})

# ---- Bar 5-6: 01 MOTION GRAPHICS & ANIMATION
cue(bar(5), "sweep", -9, "SECTION 01 transition", peak=True, args={"dur": 0.9, "seed": 20})
cue(bar(5), "scrub", -22, "label types on: MOTION GRAPHICS & ANIMATION", args={"dur": 0.5, "rate0": 26, "rate1": 30, "seed": 21})
for i, b in enumerate((1, 2, 3)):
    cue(bar(5, b), "felt", -10 - 3 * i, f"ellipse bounce {i + 1} (squash)", args={"freq": 110 - 6 * i, "seed": 22 + i})
cue(bar(6), "pencil", -15, "bezier handle dragged, curve redraws", args={"dur": 0.8, "seed": 25})
cue(bar(6, 2), "swell", -13, "shape morphs", end=True, args={"dur": 0.6, "freq": 147})
cue(bar(6, 2), "felt", -10, "morph lands", args={"freq": 98, "seed": 26})
cue(bar(6, 3), "tick", -22, "keyframe diamonds blink", args={"freq": 2900, "seed": 27, "pan": 0.4})

# ---- Bar 7-8: 02 VIDEO EDITING
cue(bar(7), "sweep", -9, "SECTION 02 transition", peak=True, args={"dur": 0.9, "pan_from": 0.9, "pan_to": -0.9, "seed": 30})
cue(bar(7), "shutter", -14, "frame flash", args={"seed": 31})
cue(bar(7), "scrub", -22, "label types on: VIDEO EDITING", args={"dur": 0.4, "rate0": 26, "rate1": 30, "seed": 32})
for i, (b, p) in enumerate(((1, -0.5), (2, 0.0), (3, 0.5))):
    cue(bar(7, b), "snap", -12, f"clip {i + 1} snaps onto the timeline", args={"seed": 33 + i, "pan": p})
cue(bar(8), "scrub", -15, "playhead scrubs the timeline", args={"dur": 1.2, "seed": 36})
for i, b in enumerate((2, 2.5, 3)):
    cue(bar(8, b), "shutter", -14 + i, f"cut {i + 1} (accelerating edit)", args={"seed": 37 + i, "pan": (-0.4, 0.4, 0)[i]})

# ---- Bar 9-10: 03 SMOOTH TRANSITIONS & VISUAL EFFECTS
cue(bar(9), "whoosh", -8, "SECTION 03 transition", peak=True, args={"dur": 0.9, "seed": 40})
cue(bar(9), "scrub", -22, "label types on: SMOOTH TRANSITIONS & VISUAL EFFECTS", args={"dur": 0.6, "rate0": 26, "rate1": 30, "seed": 41})
cue(bar(9, 1), "sweep", -11, "panel wipe right-to-left", peak=True, args={"dur": 0.7, "pan_from": 0.8, "pan_to": -0.8, "seed": 42})
cue(bar(9, 2), "sweep", -11, "panel wipe left-to-right", peak=True, args={"dur": 0.7, "pan_from": -0.8, "pan_to": 0.8, "seed": 43})
cue(bar(10), "riser", -13, "into the zoom-through", end=True, args={"dur": 1.2, "f0": 220, "f1": 1400, "seed": 44})
cue(bar(10), "whoosh", -8, "zoom-through transition", peak=True, args={"dur": 0.8, "seed": 45, "pan_from": 0, "pan_to": 0})
cue(bar(10, 1), "shimmer", -17, "light leak washes across", args={"dur": 2.0, "base": 440})
cue(bar(10, 2), "tapestop", -12, "VFX time-freeze", args={"dur": 0.6})
cue(bar(11), "spinup", -12, "time restarts", end=True, args={"dur": 0.5, "seed": 46})

# ---- Bar 11: 15s . 30s . 60s PACKAGES
cue(bar(11), "scrub", -21, "timecode rolls to 00:00:15", args={"dur": 0.55, "seed": 47})
for i, (b, f, txt) in enumerate(((0.75, 196, "15S"), (1.75, 233, "30S"), (2.75, 294, "60S"))):
    cue(bar(11, b), "knock", -10 + i, f"package {txt} locks in", args={"freq": f, "seed": 48 + i, "pan": (-0.4, 0, 0.4)[i]})
cue(bar(11, 3.5), "felt", -15, "'PACKAGES' label settles", args={"seed": 51, "freq": 104})

# ---- Bar 12+: LOCKUP (the thumbnail composition), BY EVAN, CTA
cue(bar(12), "riser", -11, "into the lockup", end=True, args={"dur": 2.2, "seed": 52})
cue(bar(12), "swell", -10, "into the lockup", end=True, args={"dur": 1.2, "freq": 73.42})
cue(bar(12), "impact", -7, "LOCKUP: full title + three columns", args={"dur": 2.8})
cue(bar(12), "subdrop", -10, "LOCKUP sub")
cue(bar(12), "knock", -9, "LOCKUP title stamp", args={"freq": 196, "seed": 53})
cue(bar(12), "ripple", -14, "rings spread behind the play button", args={"base": 146.83})
cue(bar(12, 2), "shimmer", -19, "lockup glow", args={"dur": 3.0, "base": 587})
cue(bar(12, 2), "felt", -15, "BY EVAN settles", args={"freq": 92, "seed": 54, "pan": -0.5})
cue(bar(13), "press", -14, "play button breathes (CTA)", args={"seed": 55})
cue(bar(13), "ripple", -19, "CTA ring", args={"base": 196, "seed": 56})

# ---- bed bus: drone + soft bar pulse (separate stem; mute it if music is added)
cue(0, "bed", 0, "warm drone bed", bus="bed", args={"dur": 32.0})
for n in list(range(3, 11)) + [12, 13]:
    cue(bar(n), "pulse", -7, f"bar {n} pulse", bus="bed", args={"seed": 60 + n})

cfg = {"duration": 32.0,
       "room_env": [[0, 0.9], [4.9, 0.6], [6.25, 0.2], [27.4, 0.15], [29, 0.4], [32, 0.4]],
       "cues": C}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sfx_cues.json")
json.dump(cfg, open(out, "w"), indent=1)
print(f"{len(C)} cues -> {out}")
