# frame.md: design truth (sound section; the visual section comes with the build)

## Sound: Do NOT use
- `pop` (UI chirp-pop): banned, the client dislikes it. It is removed from the generators in `audio/sfx_extra.py`.
- Bright blips, chimes, notification sounds, glitch crunches, error buzzes: wrong for a warm editorial look.
- Whooshes and sweeps: the client finds them too much. ONE whoosh in the whole piece (the bar 9 zoom-through).
  Section changes use a low `knock`, slams use `felt`/`knock`, wipes use `paper`. Risers/swells only into the two big hits.

## Sound: rules
- Landings: `felt` (shapes) or `knock` (type). Clicks: `press` (the play button only).
- Line draws: `pencil`. Edits: `snap`, `shutter`, `scrub`.
- Big moments in layers: swell/riser ending on the hit → impact + subdrop (+ knock for type).
