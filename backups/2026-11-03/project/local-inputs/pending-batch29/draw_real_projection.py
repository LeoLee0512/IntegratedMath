"""Exact rational projection example; the plot illustrates proved identities."""
from fractions import Fraction as F
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.text import Text


def draw_real_projection(out):
    p, u = (F(0), F(2)), (F(1), F(-1))
    x, y = (F(0), F(0)), (F(2), F(0))
    w = tuple(x[j] - p[j] for j in range(2))
    denominator = sum(z * z for z in u)
    assert denominator > 0
    t0 = sum(w[j] * u[j] for j in range(2)) / denominator
    h = tuple(p[j] + t0 * u[j] for j in range(2))
    residual = tuple(x[j] - h[j] for j in range(2))
    assert t0 == 1 and h == (F(1), F(1))
    assert sum(residual[j] * u[j] for j in range(2)) == 0
    squared_xy = sum((x[j] - y[j]) ** 2 for j in range(2))
    squared_xh = sum((x[j] - h[j]) ** 2 for j in range(2))
    squared_hy = sum((h[j] - y[j]) ** 2 for j in range(2))
    assert (squared_xy, squared_xh, squared_hy) == (F(4), F(2), F(2))
    assert squared_xy == squared_xh + squared_hy
    # Exact arithmetic above checks this instance, not the general theorem.
    # Floating-point coordinates below serve only to draw the canvas.
    fig, ax = plt.subplots(figsize=(7.4, 5.7))
    ax.set_aspect('equal')
    ax.set_xlim(-.65, 3.15)
    ax.set_ylim(-.7, 2.9)
    ax.set_xticks(range(4))
    ax.set_yticks(range(3))
    ax.grid(alpha=.2)
    ax.axhline(0, color='#777777', linewidth=.8)
    ax.axvline(0, color='#777777', linewidth=.8)
    ax.plot([-.4, 2.5], [2.4, -.5], color='#2563a6', linewidth=2)
    ax.plot([float(x[0]), float(h[0])],
            [float(x[1]), float(h[1])], color='#a85d25', linewidth=2.4)
    ax.plot([float(x[0]), float(y[0])],
            [float(x[1]), float(y[1])], color='#6b7280', linestyle='--')
    for point, label, offset in [
        (p, r'$P=(0,2)$', (10, 8)),
        (x, r'$X=(0,0)$', (-38, -28)),
        (h, r'$H=(1,1)$', (12, 12)),
        (y, r'$Y=(2,0)$', (12, 7)),
    ]:
        xy = tuple(map(float, point))
        ax.scatter(*xy, color='#2563a6', s=34, zorder=3)
        ax.annotate(label, xy, xytext=offset,
                    textcoords='offset points', fontsize=11)
    ax.text(1.45, 2.35, r'$L:\ x_1+x_2=2$', fontsize=12)
    ax.text(1.45, 1.96, r'$u=(1,-1)$', fontsize=11)
    ax.text(-.05, .55, r'$d_2(X,H)=\sqrt{2}$',
            color='#a85d25', rotation=45, fontsize=11)
    ax.set_xlabel('第一坐标（数值刻度）')
    ax.set_ylabel('第二坐标（数值刻度）')
    ax.set_title('正交投影与最近点：坐标模型的一个实例')
    fig.text(.5, .075,
             r'$d_2(X,Y)^2=4=2+2=d_2(X,H)^2+d_2(H,Y)^2$',
             ha='center', fontsize=11)
    fig.text(.5, .025, '坐标简写有理数的实数像；最短与唯一性由正文证明。',
             ha='center', fontsize=10)
    font = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
    for label in fig.findobj(Text):
        label.set_fontproperties(FontProperties(fname=font,
                                                size=label.get_fontsize()))
    fig.tight_layout(rect=(0, .12, 1, 1))
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    fig.savefig(out / 'b2_real_plane_projection.png', dpi=180,
                bbox_inches='tight', facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    draw_real_projection('/tmp/real-projection-figure')
