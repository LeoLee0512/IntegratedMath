from fractions import Fraction as F
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/integratedmath-production-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.text import Text

def draw_dedekind_grid(out):
    """Six exact samples for a specified rational cut, not a general cut algorithm."""
    endpoint,epsilon,a0,b0=F(3,2),F(1,2),F(1),F(2)
    delta=epsilon/2
    points=[a0+n*delta for n in range(6)]
    inside=[q<endpoint for q in points]
    assert inside==[True,True,False,False,False,False]
    m=next(n for n,member in enumerate(inside) if not member)
    u,v=points[m-1],points[m]
    assert m==2 and points[5]>b0 and u<endpoint<=v
    assert 0<v-u==delta<epsilon
    fig,ax=plt.subplots(figsize=(10.6,3.8));ax.set_xlim(-.9,5.5);ax.set_ylim(-1.55,2.2);ax.axis('off')
    ax.text(2.25,1.9,r'$A=i(3/2),\quad\varepsilon=1/2,\quad\delta=\varepsilon/2=1/4$',ha='center',fontsize=17)
    ax.text(-.78,.72,'指标 n',ha='center',fontsize=12)
    ax.text(-.78,.15,'有理点',ha='center',fontsize=12)
    for n,(q,member) in enumerate(zip(points,inside)):
        color='#256a8a' if member else '#a85d25'
        ax.text(n,.72,str(n),ha='center',fontsize=14)
        ax.text(n,.15,str(q),ha='center',va='center',fontsize=18,color=color,bbox=dict(boxstyle='round,pad=.25',ec=color,fc='#f7f9fa'))
        ax.text(n,-.35,'在 A 内' if member else '不在 A 内',ha='center',fontsize=11,color=color)
    ax.text(1,-.82,r'$u=5/4$',ha='center',fontsize=13,color='#256a8a')
    ax.text(2,-.82,r'$v=3/2$',ha='center',fontsize=13,color='#a85d25')
    ax.text(4,-.82,r'$b_0=2$',ha='center',fontsize=13,color='#a85d25')
    ax.text(5,-.82,r'$N=5$',ha='center',fontsize=13,color='#a85d25')
    ax.text(1.5,-1.28,r'$m=2,\quad v-u=1/4<\varepsilon$',ha='center',fontsize=15)
    for label in fig.findobj(Text):label.set_fontproperties(FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',size=label.get_fontsize()))
    fig.tight_layout();fig.savefig(out/'b2_dedekind_grid.png',dpi=180,bbox_inches='tight',facecolor='white');plt.close(fig)

if __name__=='__main__':draw_dedekind_grid(Path('/tmp'))
