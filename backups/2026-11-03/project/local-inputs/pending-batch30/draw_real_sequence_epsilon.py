"""Exact rational witnesses for an epsilon-tail illustration; finite plot only."""
from fractions import Fraction as F
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.text import Text


def draw_real_sequence_epsilon(out):
    epsilon = F(1, 4)
    threshold = 4
    indices = tuple(range(15))
    values = tuple(F(1, n + 1) for n in indices)
    assert epsilon > 0
    assert values[3] == epsilon
    assert not abs(values[3]) < epsilon
    assert values[threshold] == F(1, 5) < epsilon
    assert all(abs(values[n]) < epsilon for n in indices if n >= threshold)
    assert all(not abs(values[n]) < epsilon for n in indices if n < threshold)
    # These assertions check plotted inputs, not a universal tail theorem.
    # For every natural n >= 4, n+1 >= 5 > 0 implies
    # 0 < 1/(n+1) <= 1/5 < 1/4. This is the exact tail proof.
    fig, ax = plt.subplots(figsize=(10.8, 6.3))
    eps_display = float(epsilon)
    ax.axhspan(-eps_display, eps_display, color='#dcecf9', alpha=.85,
               label=r'$-\varepsilon<b_n<\varepsilon$')
    ax.axhline(eps_display, color='#a85d25', linestyle='--', linewidth=1.4)
    ax.axhline(-eps_display, color='#a85d25', linestyle='--', linewidth=1.4)
    ax.axhline(0, color='#58616a', linewidth=1)
    ax.axvline(threshold, color='#2563a6', linestyle=':', linewidth=1.2)
    # Conversion to float is restricted to the display, after exact checks.
    ax.scatter(indices[:3], [float(x) for x in values[:3]],
               color='#a85d25', s=40, zorder=4)
    ax.scatter([3], [float(values[3])], facecolors='white',
               edgecolors='#a85d25', linewidths=2, s=80, zorder=5)
    ax.scatter(indices[threshold:], [float(x) for x in values[threshold:]],
               color='#2563a6', s=40, zorder=4)
    ax.annotate(r'$b_3=1/4=\varepsilon$' + '\n等于边界，不满足严格小于',
                (3, float(values[3])), xytext=(4.6, .66),
                arrowprops={'arrowstyle': '->', 'color': '#a85d25'},
                color='#8f4b18', fontsize=11)
    ax.annotate(r'$b_4=1/5<\varepsilon$' + '\n从 N=4 开始满足',
                (4, float(values[4])), xytext=(7.3, .42),
                arrowprops={'arrowstyle': '->', 'color': '#2563a6'},
                color='#2563a6', fontsize=11)
    ax.text(13.9, .28, r'$+\varepsilon=1/4$', ha='right',
            color='#8f4b18', fontsize=11)
    ax.text(13.9, -.30, r'$-\varepsilon=-1/4$', ha='right',
            color='#8f4b18', fontsize=11)
    ax.text(13.9, -.065, '极限候选 0', ha='right',
            color='#58616a', fontsize=11)
    ax.text(4.12, -.19, 'N=4', color='#2563a6', fontsize=11)
    ax.set_xlim(-.5, 14.5)
    ax.set_ylim(-.36, 1.08)
    ax.set_xticks(indices)
    ax.set_yticks([-.25, 0, .25, .5, .75, 1])
    ax.set_yticklabels([r'$-1/4$', r'$0$', r'$1/4$',
                        r'$1/2$', r'$3/4$', r'$1$'])
    ax.set_xlabel('自然数下标 n（从 0 开始；图中只画到 14）', fontsize=11)
    ax.set_ylabel(r'$b_n=1/(n+1)$', fontsize=12)
    ax.grid(axis='x', alpha=.13)
    ax.set_title('先给 ε=1/4，再选 N=4；之后要求任意 n≥N 都满足',
                 fontsize=14, pad=16)
    ax.legend(loc='upper right', frameon=False, fontsize=11)
    fig.text(.5, .145,
             r'$n\geq4\ \Longrightarrow\ n+1\geq5>0'
             r'\ \Longrightarrow\ 0<b_n\leq1/5<1/4=\varepsilon$',
             ha='center', fontsize=12)
    fig.text(.5, .085,
             '上式证明整个尾段；有限点图只展示样例。此图只处理一个 ε，不代替任意 ε 的收敛证明。',
             ha='center', fontsize=10.5)
    fig.text(.5, .035,
             '因 n=3 仍等于边界，任何 N≤3 都不合要求；故本例最早严格阈值为 N=4。',
             ha='center', fontsize=10.5)
    font = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
    for label in fig.findobj(Text):
        label.set_fontproperties(FontProperties(fname=font,
                                                size=label.get_fontsize()))
    fig.tight_layout(rect=(0, .22, 1, 1))
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    fig.savefig(out / 'b2_real_sequence_epsilon.png', dpi=180,
                bbox_inches='tight', facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    draw_real_sequence_epsilon('/tmp/real-sequence-epsilon-figure')
