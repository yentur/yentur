"""Pipeline strip: the loop I actually work in, as one image instead of four paragraphs."""

W, H = 1200, 226
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

STAGES = [
    ("DATA",     ["telephone channel sim", "forced alignment", "hard negatives"]),
    ("TRAIN",    ["TTS / ASR fine-tune", "LoRA and full", "from scratch when needed"]),
    ("EVALUATE", ["WER, word-level", "A/B harnesses", "LLM judges"]),
    ("SERVE",    ["quantise", "batched inference", "measure the latency"]),
]

BOX_W, BOX_H, GAP = 272, 140, 37
X0 = (W - (BOX_W * 4 + GAP * 3)) / 2
Y0 = 30


def svg(fg, sub, accent, line, box):
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
         f'fill="none" role="img" aria-label="Data, train, evaluate, serve">']
    for i, (title, items) in enumerate(STAGES):
        x = X0 + i * (BOX_W + GAP)
        p.append(f'<rect x="{x}" y="{Y0}" width="{BOX_W}" height="{BOX_H}" rx="5" '
                 f'fill="{box}" stroke="{line}" stroke-width="1"/>')
        p.append(f'<rect x="{x}" y="{Y0}" width="3" height="{BOX_H}" rx="1.5" fill="{accent}"/>')
        p.append(f'<text x="{x + 20}" y="{Y0 + 32}" font-family="{MONO}" font-size="15" '
                 f'letter-spacing="1.9" fill="{accent}" font-weight="600">{title}</text>')
        for j, it in enumerate(items):
            p.append(f'<text x="{x + 20}" y="{Y0 + 64 + j * 26}" font-family="{FONT}" '
                     f'font-size="17.5" fill="{sub}">{it}</text>')
        if i < 3:
            ax = x + BOX_W + GAP / 2
            ay = Y0 + BOX_H / 2
            p.append(f'<path d="M{ax-9},{ay} L{ax+7},{ay} M{ax+2},{ay-4.5} L{ax+7},{ay} '
                     f'L{ax+2},{ay+4.5}" stroke="{line}" stroke-width="1.4" '
                     f'stroke-linecap="round" stroke-linejoin="round"/>')
    # feedback arc: evaluate feeds back into data
    fy = Y0 + BOX_H + 32
    x_end = X0 + 2 * (BOX_W + GAP) + BOX_W / 2
    p.append(f'<path d="M{x_end},{Y0+BOX_H} L{x_end},{fy} L{X0+BOX_W/2},{fy} L{X0+BOX_W/2},{Y0+BOX_H+7} '
             f'M{X0+BOX_W/2-4.5},{Y0+BOX_H+12} L{X0+BOX_W/2},{Y0+BOX_H+6} L{X0+BOX_W/2+4.5},{Y0+BOX_H+12}" '
             f'stroke="{line}" stroke-width="1.2" stroke-dasharray="3 4" fill="none" '
             f'stroke-linecap="round" stroke-linejoin="round"/>')
    p.append(f'<text x="{(X0+BOX_W/2 + x_end)/2}" y="{fy - 7}" text-anchor="middle" '
             f'font-family="{FONT}" font-size="15" fill="{sub}" font-style="italic">'
             f'most of the gain lives here</text>')
    p.append('</svg>')
    return "\n".join(p)


open("assets/loop-light.svg", "w").write(svg("#1B2430", "#4A5566", "#1F6F66", "#D3D9E1", "#FBFCFD"))
open("assets/loop-dark.svg", "w").write(svg("#D8DEE7", "#96A1B0", "#6FC0B4", "#2E3846", "#12171E"))
print("ok")
