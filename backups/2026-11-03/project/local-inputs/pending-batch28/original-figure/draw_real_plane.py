"""Exact rational witnesses for two coordinate-model examples; original figure."""
from fractions import Fraction as F
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.text import Text


def draw_real_plane(out):
    p, q = (F(0), F(0)), (F(2), F(4))
    parameters = (F(0), F(1, 2), F(1))
    points = [tuple(p[j] + t * (q[j] - p[j])
                    for j in range(2)) for t in parameters]
    assert points == [(F(0), F(0)), (F(1), F(2)), (F(2), F(4))]
    midpoint = points[1]
    assert tuple(midpoint[j] - p[j] for j in range(2)) == tuple(
        q[j] - midpoint[j] for j in range(2))
    origin, corner, end = (F(0), F(0)), (F(3), F(0)), (F(3), F(4))
    square_sum = sum((end[j] - origin[j]) ** 2 for j in range(2))
    assert square_sum == F(25) and F(5) > 0 and F(5) ** 2 == square_sum
    # Float conversion below controls the canvas only, after exact checks.
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 5.2))
    colors = ('#2563a6', '#a85d25')
    for ax in axes:
        ax.set_aspect('equal')
        ax.set_xlim(-.65, 4.2)
        ax.set_ylim(-.65, 4.9)
        ax.set_xticks(range(5))
        ax.set_yticks(range(5))
        ax.grid(alpha=.2)
        ax.axhline(0, color='#555555', linewidth=.8)
        ax.axvline(0, color='#555555', linewidth=.8)
        ax.set_xlabel('横坐标（数值刻度）')
        ax.set_ylabel('纵坐标（数值刻度）')
    axes[0].plot([float(p[0]), float(q[0])],
                 [float(p[1]), float(q[1])], color=colors[0], linewidth=2)
    labels = [r'$P=(0,0),\ t=0$', r'$M=(1,2),\ t=1/2$',
              r'$Q=(2,4),\ t=1$']
    offsets = [(8, 10), (10, -15), (8, 10)]
    for point, label, offset in zip(points, labels, offsets):
        xy = tuple(map(float, point))
        axes[0].scatter(*xy, color=colors[0], s=34, zorder=3)
        axes[0].annotate(label, xy, xytext=offset,
                         textcoords='offset points', fontsize=10)
    axes[0].set_title('线段参数与等位移中点')
    axes[1].plot([0, 3], [0, 4], color=colors[1], linewidth=2)
    axes[1].plot([0, 3, 3], [0, 0, 4], linestyle='--',
                 color='#6b7280', linewidth=1)
    for point, label, offset in [
        (origin, r'$O=(0,0)$', (10, -25)),
        (corner, r'$A=(3,0)$', (-30, -25)),
        (end, r'$B=(3,4)$', (-65, 12)),
    ]:
        xy = tuple(map(float, point))
        axes[1].scatter(*xy, color=colors[1], s=34, zorder=3)
        axes[1].annotate(label, xy, xytext=offset,
                         textcoords='offset points', fontsize=10)
    axes[1].text(.1, 2.75, r'$d_2(O,B)=5$', color=colors[1], fontsize=12)
    axes[1].set_title('距离定义中的平方和：$3^2+4^2=5^2$')
    fig.text(.5, .02, '图中坐标简写相应有理数的实数像；示意图不代替证明。',
             ha='center', fontsize=11)
    font = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
    for label in fig.findobj(Text):
        label.set_fontproperties(FontProperties(fname=font,
                                                size=label.get_fontsize()))
    fig.tight_layout(rect=(0, .06, 1, 1))
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    fig.savefig(out / 'b2_real_plane_model.png', dpi=180,
                bbox_inches='tight', facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    draw_real_plane('/tmp/real-plane-figure')
