"""Banner: a continuous speech waveform resolving into discrete tokens.

Left is the signal, right is what a recogniser emits from it. Deterministic,
so both themes render the identical geometry.
"""
import math

W, H = 1200, 170
MID = H / 2
WAVE_END = 610
TOK_START = 665
N = 420

# syllable bursts: (centre, width, gain). Gaps between them are real silence.
BURSTS = [(0.05, 0.030, 0.85), (0.13, 0.038, 1.00), (0.23, 0.026, 0.62),
          (0.36, 0.042, 0.95), (0.47, 0.030, 0.70), (0.60, 0.036, 1.00),
          (0.71, 0.024, 0.55), (0.83, 0.040, 0.80), (0.93, 0.022, 0.45)]

# token chips: width in px. Varied like real subword lengths.
CHIPS = [34, 18, 52, 26, 14, 44, 30, 20, 58, 24, 16, 38, 28]


def env(t):
    a = 0.0
    for c, w, g in BURSTS:
        a += g * math.exp(-((t - c) ** 2) / (2 * w * w))
    return min(a, 1.0)


def wave_path():
    pts = []
    for i in range(N + 1):
        t = i / N
        x = t * WAVE_END
        carrier = (math.sin(t * 61) * 0.60 + math.sin(t * 148 + 1.1) * 0.26
                   + math.sin(t * 263 + 2.3) * 0.14)
        y = MID - carrier * env(t) * (H * 0.36)
        pts.append(f"{x:.1f},{y:.1f}")
    return "M" + " L".join(pts)


def svg(fg, accent, dim):
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" fill="none" role="img" '
         f'aria-label="A speech waveform resolving into discrete tokens">']
    p.append(f'<line x1="0" y1="{MID}" x2="{WAVE_END}" y2="{MID}" stroke="{dim}" stroke-width="1"/>')
    p.append(f'<path d="{wave_path()}" stroke="{fg}" stroke-width="1.5" '
             f'stroke-linejoin="round" stroke-linecap="round" fill="none"/>')
    # the hand-off
    for k in range(3):
        p.append(f'<circle cx="{WAVE_END + 14 + k * 13}" cy="{MID}" r="1.7" fill="{dim}"/>')
    # token chips, constant height, varying width
    x, ch = TOK_START, 13
    for i, cw in enumerate(CHIPS):
        if x + cw > W - 20:
            break
        op = 1.0 if i % 3 else 0.72
        p.append(f'<rect x="{x}" y="{MID - ch/2:.1f}" width="{cw}" height="{ch}" '
                 f'rx="{ch/2}" fill="{accent}" fill-opacity="{op}"/>')
        x += cw + 9
    p.append('</svg>')
    return "\n".join(p)


open("assets/banner-light.svg", "w").write(svg("#1B2430", "#1F6F66", "#CBD2DB"))
open("assets/banner-dark.svg", "w").write(svg("#D8DEE7", "#6FC0B4", "#2E3846"))
print("ok")
