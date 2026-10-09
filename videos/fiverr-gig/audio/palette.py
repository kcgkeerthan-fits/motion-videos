"""Audition file: each sound of this project's palette once, with a gap. Writes renders/sound_palette.wav."""
import os, sys, wave
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sfx_extra as X
L = X.L
order = [("press", {}), ("felt", {}), ("knock", {}), ("pencil", {"dur": 1.0}), ("ripple", {}), ("sweep", {}),
         ("whoosh", {"dur": 0.9}), ("snap", {}), ("shutter", {}), ("scrub", {}), ("tick", {}), ("paper", {}),
         ("swell", {"dur": 1.0}), ("impact", {}), ("subdrop", {}), ("riser", {"dur": 2.0}), ("tapestop", {}),
         ("spinup", {}), ("shimmer", {"dur": 2.0, "base": 587}), ("pulse", {})]
parts = []
for name, args in order:
    s = L.GENERATORS[name](**args)
    parts += [s / (np.max(np.abs(s)) + 1e-9) * 0.7, np.zeros((int(0.7 * L.SR), 2))]
    print(name)
x = np.concatenate(parts)
pcm = (np.clip(x, -1, 1) * 32767).astype(np.int16)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "renders", "sound_palette.wav")
with wave.open(out, "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(L.SR); w.writeframes(pcm.tobytes())
