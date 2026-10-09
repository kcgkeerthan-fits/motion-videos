"""The few big hits mixed under Vibin (times come from the scene->song beat map in index.html)."""
import os, sys, wave
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "fiverr-gig", "audio"))
import sfx_extra as X  # project palette (felt, knock, press, ...) on top of the skill's sfx_lib
L = X.L
DUR = 28.6
HITS = [  # (time s, effect, gain dB, args)
    (3.622, "press", -6, {}),                       # play pressed
    (4.481, "knock", -6, {"freq": 220, "seed": 22}),  # 'Graphics' stamps in
    (4.481, "impact", -12, {"dur": 1.4}),
    (24.141, "impact", -4, {"dur": 2.8}),           # the lockup
    (24.141, "subdrop", -8, {}),
    (24.141, "knock", -8, {"freq": 196, "seed": 141}),
]
out = np.zeros((int(DUR * L.SR) + L.SR * 3, 2))
for t, fx, g, a in HITS:
    s = L.GENERATORS[fx](**a).astype(np.float64)
    k = int(t * L.SR)
    n = min(len(s), len(out) - k)
    out[k:k + n] += s[:n] * 10 ** (g / 20)
out = out[: int(DUR * L.SR)]
out = out / np.max(np.abs(out)) * 10 ** (-3 / 20)
pcm = (np.clip(out, -1, 1) * 32767).astype(np.int16)
with wave.open(os.path.join(HERE, "..", "assets", "audio", "hits.wav"), "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(L.SR); w.writeframes(pcm.tobytes())
print("hits.wav", len(HITS), "cues")
# then: ffmpeg -i assets/audio/vibin-cut.wav -i assets/audio/hits.wav -filter_complex "[1]volume=0.5[h];[0][h]amix=inputs=2:normalize=0,alimiter=limit=0.89:level=false" assets/audio/mix.wav
