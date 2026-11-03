from fractions import Fraction as F
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/integratedmath-production-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.text import Text

def draw_rational_gap(out):
    """Two finite exact witness chains, not a limit or a drawing of all Q."""
    def step(q):
        assert q>=0
        return (2*q+2)/(q+2)
    chains=[]
    for start in (F(1),F(2)):
        row=[start]
        for _ in range(2):row.append(step(row[-1]))
        chains.append(row)
    assert chains==[[F(1),F(4,3),F(7,5)],[F(2),F(3,2),F(10,7)]]
    for row in chains:
        for q,r in zip(row,row[1:]):
            assert r-q==(2-q*q)/(q+2)
            assert r*r-2==2*(q*q-2)/(q+2)**2
    assert all(x*x<2 for x in chains[0]) and chains[0][0]<chains[0][1]<chains[0][2]
    assert all(x*x>2 for x in chains[1]) and chains[1][0]>chains[1][1]>chains[1][2]
    fig,ax=plt.subplots(figsize=(10,4.5));ax.set_xlim(0,10);ax.set_ylim(0,4.5);ax.axis('off')
    ax.text(5,4.12,r'$f(q)=(2q+2)/(q+2),\quad q\geq 0$',ha='center',fontsize=18)
    for k,(row,color,y,title) in enumerate(zip(chains,['#256a8a','#a85d25'],[2.65,.85],['S 中更大的成员','更小的有理上界'])):
        ax.text(.2,y+.6,title,color=color,fontsize=14)
        for j,x in enumerate(row):
            pos=1.25+3.5*j;square=x*x
            ax.text(pos,y,str(x),ha='center',va='center',fontsize=21,color=color,bbox=dict(boxstyle='round,pad=.35',fc='#f7f9fa',ec=color))
            sign='<' if k==0 else '>'
            ax.text(pos,y-.56,f'平方为 {square} {sign} 2',ha='center',fontsize=12,color=color)
            if j<2:
                ax.annotate('',xy=(pos+2.88,y),xytext=(pos+.65,y),arrowprops=dict(arrowstyle='->',lw=1.6,color=color))
                ax.text(pos+1.75,y+.18,'应用 f',ha='center',fontsize=12,color=color)
    for label in fig.findobj(Text):label.set_fontproperties(FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',size=label.get_fontsize()))
    fig.tight_layout();fig.savefig(out/'b2_rational_gap.png',dpi=180,bbox_inches='tight',facecolor='white');plt.close(fig)

if __name__=='__main__':draw_rational_gap(Path('/tmp'))
