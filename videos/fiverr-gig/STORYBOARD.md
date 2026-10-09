# Fiverr gig video: "Motion Graphics That Bring Ideas to Life" (by Evan)

16:9, 1920x1080, 60 fps, **34.8 s** (14 bars + a tail). Silent tempo **100 bpm** (beat 0.6 s, bar 2.4 s),
measured from `reference/ref1.mp4`. The reference changes picture every 0.6 s, every 0.3 s in its dense
parts, with 0.2 s bursts. It builds to a peak, drops to a near-empty pause, and ends on one big held
word. This piece copies that energy shape. The sound came first: `audio/sfx_cues.json` (made by
`audio/make_cues.py`, 154 cues) is the timing source of truth, and the animation is built to it.
Cue sheet: `audio/sfx_cuesheet.md`.

Look (from the thumbnail): deep green-black ground, a terracotta centre column, cream serif display type
(roman + italic), small tracked sans-serif labels, technical chrome (ruler ticks, timecodes, REC waveform,
crosshairs, dashed circles, a bezier curve, concentric rings, three leaning ellipses, a play button).
Borrowed from the reference's editing: hard block slams, one word per beat, letters scattering, colour
panel slams, a repeating tile grid flipping colour, the pause before the end.

Sound: warm, tactile, editorial. **No pops.** A soft pulse on every beat drives bars 3-11.

| bar | time | picture | sound | ref |
|---|---|---|---|---|
| 1 | 0.0–2.4 | Cold open: REC, timecode, dashed circle, crosshairs, ruler ticks build on every beat | spin-up, ticks, pencil | 0–2 s stacking |
| 2 | 2.4–4.8 | Terracotta block SLAMS in and shifts every beat; bezier draws; play disc lands | sweep + felt, block sweeps, pencil | 2.5 s block flash |
| 3 | 4.8–7.2 | PLAY pressed, rings; "Motion" · "Graphics" · *that* · *bring* one per beat | press, ripple, knocks + impact, paper | 10–17 s word per beat |
| 4 | 7.2–9.6 | *ideas* · "to" · "life", then the title scatters into flying letters | sweep, felt, knock + glow, whoosh + 8 ticks | 8–10 s scatter |
| 5 | 9.6–12.0 | **01 Motion Graphics & Animation**: ellipse bounces on every beat | sweep, type-on, felt ×3 | |
| 6 | 12.0–14.4 | Colour panel slams, accelerating; shape morph; curve snaps | sweeps + felts, swell, pencil | 17.5–19 s colour slams |
| 7 | 14.4–16.8 | **02 Video Editing**: three clips snap on, one per beat | sweep + shutter, snaps | |
| 8 | 16.8–19.2 | Playhead scrubs, then five cuts on half-beats | scrub, shutters | 22–26 s blocks |
| 9 | 19.2–21.6 | **03 Smooth Transitions & Visual Effects**: wipes both ways, zoom-through | whoosh, sweeps, riser → whoosh | |
| 10 | 21.6–24.0 | **PEAK**: repeating tile grid flips colour every half-beat, 0.2 s burst at the end | snaps, sweeps, light-leak shimmer, shutters | 26–32 s grid |
| 11 | 24.0–26.4 | **15s · 30s · 60s Packages** lock in on the beats | rising knocks + timecode rolls, felt | |
| 12 | 26.4–28.8 | **PAUSE**: everything drops out, "BY EVAN" types on small, alone | tape stop, quiet keys, riser + swell | 32.5–36 s near-empty |
| 13–14 | 28.8–34.8 | **Finale lockup** = the thumbnail, held; play button breathes as the call to action | impact + sub + knock + ripple, glow, press | 36.5–41 s held word |

Stems (`assets/audio/`): `sfx.wav` (effects), `bed.wav` (drone + beat pulse, ducked in the pause; mute it
if music is added), `room.wav` (room tone). Preview mix: sfx 0 dB, bed -20 dB, room -26 dB, -16 LUFS.
`renders/reference_with_new_sound.mp4` plays the new sound under the reference's picture, for comparing pacing only
(the picture is not ours and does not sync to these cues).
