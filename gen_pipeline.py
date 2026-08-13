"""The loop, drawn honestly. Train and evaluate trade places for a while before anything wins."""

W, H = 1200, 250
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

STAGES = [
    ("DATA",     ["clean, label, augment", "usually the bottleneck"]),
    ("TRAIN",    ["TTS, ASR, LLM, LoRA", "anomaly detectors"]),
    ("EVALUATE", ["WER, F1, AUC", "the leaderboard"]),
    ("WIN",      ["eventually"]),
]

BOX_W, BOX_H, GAP = 262, 118, 42
X0 = (W - (BOX_W * 4 + GAP * 3)) / 2
Y0 = 26


def svg(fg, sub, accent, line, box, winbg, wintx):
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
         f'fill="none" role="img" aria-label="Data, train, evaluate, back to train a few times, then win">']
    xs = []
    for i, (title, items) in enumerate(STAGES):
        x = X0 + i * (BOX_W + GAP)
        xs.append(x)
        last = i == 3
        p.append(f'<rect x="{x}" y="{Y0}" width="{BOX_W}" height="{BOX_H}" rx="5" '
                 f'fill="{winbg if last else box}" stroke="{accent if last else line}" stroke-width="1"/>')
        p.append(f'<rect x="{x}" y="{Y0}" width="3" height="{BOX_H}" rx="1.5" fill="{accent}"/>')
        p.append(f'<text x="{x + 20}" y="{Y0 + 34}" font-family="{MONO}" font-size="15.5" '
                 f'letter-spacing="1.9" fill="{wintx if last else accent}" font-weight="600">{title}</text>')
        for j, it in enumerate(items):
            p.append(f'<text x="{x + 20}" y="{Y0 + 66 + j * 26}" font-family="{FONT}" '
                     f'font-size="17.5" fill="{sub}">{it}</text>')
        if i < 3:
            ax, ay = x + BOX_W + GAP / 2, Y0 + BOX_H / 2
            p.append(f'<path d="M{ax-10},{ay} L{ax+7},{ay} M{ax+2},{ay-5} L{ax+7},{ay} L{ax+2},{ay+5}" '
                     f'stroke="{line}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>')

    # the honest part: evaluate sends you back to train, repeatedly
    fy = Y0 + BOX_H + 40
    x_ev, x_tr = xs[2] + BOX_W / 2, xs[1] + BOX_W / 2
    p.append(f'<path d="M{x_ev},{Y0+BOX_H} L{x_ev},{fy} L{x_tr},{fy} L{x_tr},{Y0+BOX_H+8} '
             f'M{x_tr-5},{Y0+BOX_H+14} L{x_tr},{Y0+BOX_H+7} L{x_tr+5},{Y0+BOX_H+14}" '
             f'stroke="{accent}" stroke-width="1.4" stroke-dasharray="4 5" fill="none" '
             f'stroke-linecap="round" stroke-linejoin="round"/>')
    p.append(f'<text x="{(x_tr + x_ev) / 2}" y="{fy - 10}" text-anchor="middle" '
             f'font-family="{FONT}" font-size="16" fill="{sub}">score went down</text>')
    p.append(f'<text x="{(x_tr + x_ev) / 2}" y="{fy + 24}" text-anchor="middle" '
             f'font-family="{MONO}" font-size="14.5" fill="{accent}">repeat &#215; a lot</text>')
    p.append('</svg>')
    return "\n".join(p)


open("assets/loop-light.svg", "w").write(
    svg("#1B2430", "#4A5566", "#1F6F66", "#D3D9E1", "#FBFCFD", "#EDF6F4", "#14514A"))
open("assets/loop-dark.svg", "w").write(
    svg("#D8DEE7", "#96A1B0", "#6FC0B4", "#2E3846", "#12171E", "#16302C", "#8FD8CD"))
print("ok")
