"""Original exact-coordinate diagram for FLI exercise 8.
Run: python draw_fli_redundancy.py [output-directory]
Requires matplotlib. Writes PNG and SVG. A picture does not replace a proof.
This complete source is intended for the code appendix.
"""
from pathlib import Path
import sys

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def draw_fli_redundancy(output_directory):
    output_directory = Path(output_directory)
    output_directory.mkdir(parents=True, exist_ok=True)
    font = FontProperties(
        fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
    )
    plt.rcParams.update({'svg.fonttype': 'path', 'font.size': 11})
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.9))
    colors = {'v0': '#1864ab', 'v1': '#087f5b', 'v2': '#e67700'}
    for ax in axes:
        ax.set_aspect('equal')
        ax.set_xlim(-0.4, 2.6)
        ax.set_ylim(-0.55, 1.55)
        ax.axhline(0, color='#adb5bd', lw=1, zorder=0)
        ax.axvline(0, color='#adb5bd', lw=1, zorder=0)
        ax.set_xticks([0, 1, 2])
        ax.set_yticks([0, 1])
        ax.grid(alpha=0.2)
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.text(2.47, -0.20, r'$x_0$', fontsize=12)
        ax.text(-0.29, 1.40, r'$x_1$', fontsize=12)
        # Horizontal arrows share the exact origin; draw the longer one first.
        # Zero endpoint shrinking preserves the specified data coordinates.
        ax.annotate(
            '', xy=(2, 0), xytext=(0, 0), zorder=2,
            arrowprops={
                'arrowstyle': '-|>', 'color': colors['v2'],
                'lw': 5.0, 'mutation_scale': 22,
                'shrinkA': 0, 'shrinkB': 0,
            },
        )
        ax.annotate(
            '', xy=(1, 0), xytext=(0, 0), zorder=3,
            arrowprops={
                'arrowstyle': '-|>', 'color': colors['v0'],
                'lw': 2.4, 'mutation_scale': 18,
                'shrinkA': 0, 'shrinkB': 0,
            },
        )
        ax.text(
            0.45, -0.34, r'$v_0=(1,0)$',
            color=colors['v0'], fontsize=11,
        )
        ax.text(
            1.36, 0.20, r'$v_2=(2,0)$',
            color=colors['v2'], fontsize=11,
        )
    axes[0].annotate(
        '', xy=(0, 1), xytext=(0, 0), zorder=3,
        arrowprops={
            'arrowstyle': '-|>', 'color': colors['v1'],
            'lw': 2.8, 'mutation_scale': 20,
            'shrinkA': 0, 'shrinkB': 0,
        },
    )
    axes[0].text(
        0.14, 1.08, r'$v_1=(0,1)$',
        color=colors['v1'], fontsize=11,
    )
    axes[0].set_title(
        '原表：第三项由第一项的 2 倍给出', fontproperties=font, pad=16,
    )
    axes[1].scatter(
        [0], [1], facecolors='none', edgecolors='#c92a2a',
        s=95, linewidths=2, zorder=4,
    )
    axes[1].text(
        0.15, 1.05, '无法产生 (0,1)',
        fontproperties=font, color='#c92a2a',
    )
    axes[1].text(
        0.62, 0.55, r'$p v_0+q v_2=(p+2q,0)$', fontsize=12,
    )
    axes[1].set_title(
        '删去中间项：所有组合仍在横轴上', fontproperties=font, pad=16,
    )
    caption = (
        '所有箭头均从原点出发；蓝、橙箭头部分重合。'
        '图示帮助读例，代数证明见正文与题 8 解答。'
    )
    fig.text(
        0.5, 0.055, caption, fontproperties=font,
        ha='center', fontsize=11,
    )
    fig.subplots_adjust(
        left=0.055, right=0.98, top=0.88, bottom=0.18, wspace=0.21,
    )
    for ext in ('png', 'svg'):
        fig.savefig(
            output_directory / f'fli_redundancy.{ext}',
            dpi=180, facecolor='white',
        )
    plt.close(fig)


if __name__ == '__main__':
    target = (
        Path(sys.argv[1]) if len(sys.argv) > 1
        else Path(__file__).resolve().parent / 'figures'
    )
    draw_fli_redundancy(target)
