"""Original deterministic teaching diagrams for the first chapter."""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/integratedmath-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Ellipse

ROOT = Path(__file__).resolve().parents[1]
from matplotlib.font_manager import FontProperties
from matplotlib.text import Text
FONT_PATH = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
plt.rcParams.update({'font.size': 14})
BLUE, ORANGE = '#246d9c', '#b9672c'


def canvas(w=8, h=3):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 3)
    ax.set_aspect('equal')
    ax.axis('off')
    return fig, ax


def save(fig, name):
    for label in fig.findobj(Text):
        label.set_fontproperties(FontProperties(fname=FONT_PATH, size=label.get_fontsize()))
    fig.savefig(ROOT / 'figures' / ('ch01_' + name + '.png'), dpi=200,
                bbox_inches='tight', facecolor='white')
    plt.close(fig)


fig, ax = canvas()
for x in [1, 2]:
    ax.add_patch(Circle((x, 1.5), .28, color=BLUE))
for x in [4.6, 5.6, 6.6]:
    ax.add_patch(Circle((x, 1.5), .28, color=ORANGE))
ax.text(1.5, .6, '左组：2 片', ha='center')
ax.text(5.6, .6, '右组：3 片', ha='center')
ax.text(4, 2.6, '每片只属于其中一组；合起来共 5 片', ha='center')
save(fig, 'disjoint')

fig, ax = canvas()
ax.add_patch(Ellipse((3, 1.5), 4, 2, facecolor=BLUE, alpha=.15, edgecolor=BLUE))
ax.add_patch(Ellipse((5, 1.5), 4, 2, facecolor=ORANGE, alpha=.15, edgecolor=ORANGE))
for x, name in [(2.3, '安'), (4, '白'), (5.7, '陈')]:
    ax.text(x, 1.5, name, ha='center', va='center', fontsize=19)
ax.text(2.3, 2.7, '甲组', ha='center', color=BLUE)
ax.text(5.7, 2.7, '乙组', ha='center', color=ORANGE)
save(fig, 'overlap')

fig, ax = canvas()
for y, count in [(1.8, 2), (.6, 4)]:
    for i in range(count):
        ax.add_patch(Rectangle((1+6*i/count, y), 6/count, .65,
                               facecolor=BLUE if i%2==0 else ORANGE,
                               alpha=.22, edgecolor='black'))
        ax.text(1+6*(i+.5)/count, y+.325, f'1/{count} 拍', ha='center', va='center')
ax.text(4, 2.8, '两行总长度相同：都是 1 拍', ha='center')
save(fig, 'rhythm')

fig, ax = plt.subplots(figsize=(4.6, 4.2))
for i in range(2):
    for j in range(2):
        ax.add_patch(Rectangle((i,j),1,1,facecolor=BLUE,alpha=.15,edgecolor='black'))
        ax.text(i+.5,j+.5,'1',ha='center',va='center',fontsize=20)
ax.plot([0,2,2,0,0],[0,0,2,2,0],color=BLUE,lw=2)
ax.text(1,-.25,'边长 2',ha='center')
ax.text(-.25,1,'边长 2',ha='center',va='center',rotation=90)
ax.set_xlim(-.6,2.3)
ax.set_ylim(-.5,2.3)
ax.set_aspect('equal')
ax.axis('off')
save(fig,'square')
