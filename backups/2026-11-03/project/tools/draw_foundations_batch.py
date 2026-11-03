"""Draw original place-value, rational-distance and ratio diagrams; no external assets."""
from pathlib import Path
from fractions import Fraction as F
import os
os.environ.setdefault("MPLCONFIGDIR", "/tmp/integratedmath-production-matplotlib")
os.environ.setdefault("XDG_CACHE_HOME", "/tmp/integratedmath-production-cache")
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Ellipse
from matplotlib.font_manager import FontProperties
from matplotlib.text import Text

ROOT=Path(__file__).resolve().parents[1]

def draw_rational_distance(out):
    """Finite rational ticks illustrate d(r,s)=1, d(s,t)=2, d(r,t)=3."""
    fig, ax = plt.subplots(figsize=(9, 4.3))
    ax.plot([-1.7, 1.7], [0, 0], color='#4b5563', linewidth=1.5)
    ticks = [-1.5, -.5, 0, .5, 1.5]
    labels = [r'$-\frac{3}{2}$', r'$-\frac{1}{2}$', '$0$', r'$\frac{1}{2}$', r'$\frac{3}{2}$']
    for x, label in zip(ticks, labels):
        ax.plot([x, x], [-.07, .07], color='#4b5563', linewidth=1.1)
        ax.text(x, -.28, label, ha='center', va='center', fontsize=17)
    for x, name, color in [(-1.5, '$r$', '#286c94'), (-.5, '$s$', '#b65c21'), (1.5, '$t$', '#6a519e')]:
        ax.scatter([x], [0], s=62, color=color, zorder=3)
        ax.text(x, .22, name, ha='center', va='center', fontsize=17, color=color)
    for left, right, height, label, color in [
        (-1.5, -.5, .66, '$d(r,s)=1$', '#286c94'),
        (-.5, 1.5, .66, '$d(s,t)=2$', '#b65c21'),
        (-1.5, 1.5, -.85, '$d(r,t)=3=1+2$', '#6a519e'),
    ]:
        ax.annotate('', xy=(right, height), xytext=(left, height),
                    arrowprops={'arrowstyle': '<->', 'color': color, 'linewidth': 1.6})
        ax.text((left + right)/2, height + (.17 if height > 0 else -.22),
                label, ha='center', va='center', fontsize=16, color=color)
    ax.text(0, 1.2, '有理刻度上的距离：经过中间点', ha='center', fontsize=16)
    ax.set_xlim(-1.9, 1.9)
    ax.set_ylim(-1.3, 1.4)
    ax.axis('off')
    for label in fig.findobj(Text):
        label.set_fontproperties(FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc', size=label.get_fontsize()))
    fig.savefig(out/'b1_rational_distance.png', dpi=180, bbox_inches='tight', facecolor='white')
    plt.close(fig)

def draw_ratio_allocation(out):
    """A finite 2:3 split of 10; all displayed values are exact integers."""
    fig, ax = plt.subplots(figsize=(9, 3.2))
    for i in range(5):
        color = '#dcebf5' if i < 2 else '#f8e5cc'
        ax.add_patch(Rectangle((i, .9), 1, .75, facecolor=color,
                               edgecolor='#384454', linewidth=1.2))
        ax.text(i+.5, 1.275, '2', ha='center', va='center', fontsize=18)
    for left, right, name, color in [(0, 2, 'A：2份，共4', '#286c94'),
                                    (2, 5, 'B：3份，共6', '#97591d')]:
        ax.annotate('', xy=(right, .65), xytext=(left, .65),
                    arrowprops={'arrowstyle':'<->', 'color':color, 'linewidth':1.5})
        ax.text((left+right)/2, .3, name, ha='center', fontsize=15, color=color)
    ax.text(2.5, 2.0, '总量10，按2比3分配：10 ÷ (2 + 3) = 2',
            ha='center', fontsize=16)
    ax.set_xlim(-.2, 5.2); ax.set_ylim(0, 2.35); ax.axis('off')
    for label in fig.findobj(Text):
        label.set_fontproperties(FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc', size=label.get_fontsize()))
    fig.savefig(out/'b1_ratio_allocation.png', dpi=180, bbox_inches='tight', facecolor='white')
    plt.close(fig)

def draw_function_mapping(out):
    """Complete finite graph on A={0,1,2}, target B={0,1,4,9}."""
    fig, ax = plt.subplots(figsize=(9, 5.4))
    ax.add_patch(Ellipse((0, 1.9), 1.8, 4.2, facecolor='#f5f8fb', edgecolor='#55748b'))
    ax.add_patch(Ellipse((4, 1.9), 1.8, 4.2, facecolor='#faf7f1', edgecolor='#8b7755'))
    left = [(0, 3.1), (1, 2.0), (2, .9)]
    right = [(0, 3.4), (1, 2.4), (4, 1.4), (9, .4)]
    for value, y in left:
        ax.add_patch(Circle((0, y), .22, facecolor='white', edgecolor='#286c94'))
        ax.text(0, y, str(value), ha='center', va='center', fontsize=16)
    for value, y in right:
        ax.add_patch(Circle((4, y), .22, facecolor='#e7eff6' if value != 9 else 'white', edgecolor='#8b7755'))
        ax.text(4, y, str(value), ha='center', va='center', fontsize=16)
    for (_, y), (_, z) in zip(left, right):
        ax.annotate('', xy=(3.72, z), xytext=(.28, y),
                    arrowprops={'arrowstyle':'->', 'color':'#286c94', 'linewidth':1.5})
    ax.text(0, 4.25, '定义域 A = {0, 1, 2}', ha='center', fontsize=15)
    ax.text(4, 4.25, '目标集合 B = {0, 1, 4, 9}', ha='center', fontsize=15)
    ax.text(2, 3.95, '输入数与自身相乘', ha='center', fontsize=13)
    ax.text(2, -.55, '实际输出集合 f(A) = {0, 1, 4}', ha='center', fontsize=15)
    ax.text(2, -.95, '已列出 A 的全部输入；9 在 B 中，但没有输入映到 9。', ha='center', fontsize=12)
    ax.set_xlim(-1.1, 5.1); ax.set_ylim(-1.2, 4.65); ax.axis('off')
    for label in fig.findobj(Text):
        label.set_fontproperties(FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc', size=label.get_fontsize()))
    fig.savefig(out/'b2_function_mapping.png', dpi=180, bbox_inches='tight', facecolor='white')
    plt.close(fig)

def draw_inverse_mapping(out):
    """A complete finite bijection and its inverse; no continuous curve."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))
    for ax, reverse in zip(axes, [False, True]):
        left = [1, 3, 5] if reverse else [0, 1, 2]
        right = [0, 1, 2] if reverse else [1, 3, 5]
        for x, color in [(0, '#55748b'), (3, '#8b7755')]:
            ax.add_patch(Ellipse((x, 1.5), 1.35, 3.3,
                                facecolor='#f5f8fb', edgecolor=color))
        for y, a, b in zip([2.5, 1.5, .5], left, right):
            for x, value in [(0, a), (3, b)]:
                ax.text(x, y, str(value), ha='center', va='center', fontsize=17)
            ax.annotate('', xy=(2.65, y), xytext=(.35, y),
                        arrowprops={'arrowstyle': '->', 'color': '#286c94', 'linewidth': 1.5})
        ax.text(0, 3.45, 'H = {1, 3, 5}' if reverse else 'E = {0, 1, 2}',
                ha='center', fontsize=13)
        ax.text(3, 3.45, 'E = {0, 1, 2}' if reverse else 'H = {1, 3, 5}',
                ha='center', fontsize=13)
        ax.text(1.5, -.55, '逆函数：从输出找回唯一输入' if reverse else '正向函数：每个目标元素恰好命中一次',
                ha='center', fontsize=12)
        ax.set_xlim(-.9, 3.9); ax.set_ylim(-.8, 3.8); ax.axis('off')
    fig.suptitle('有限双射与逆函数：两图都列出全部输入和全部箭头', fontsize=16)
    for label in fig.findobj(Text):
        label.set_fontproperties(FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc', size=label.get_fontsize()))
    fig.savefig(out/'b2_inverse_mapping.png', dpi=180, bbox_inches='tight', facecolor='white')
    plt.close(fig)

def draw_elimination_steps(out):
    """Exact row replacement retaining the first equation; no geometric model."""
    fig, ax = plt.subplots(figsize=(12, 4.8))
    blocks = [
        (0, '原方程组', '$2x+3y=7$\n$4x-y=7$', '#edf5fa'),
        (4.4, '保留第一式，替换第二式', '$2x+3y=7$\n$-7y=-7$', '#f7f1e7'),
        (8.8, '先求出一个量，再回代', '$y=1$\n$x=(7-3)/2=2$', '#edf6ec'),
    ]
    for x, title, equations, color in blocks:
        ax.add_patch(Rectangle((x, .8), 3.4, 2.2, facecolor=color,
                               edgecolor='#526575', linewidth=1.2))
        ax.text(x+1.7, 3.35, title, ha='center', fontsize=12)
        ax.text(x+1.7, 1.9, equations, ha='center', va='center',
                fontsize=20, linespacing=2)
    for left, right in [(3.5, 4.3), (7.9, 8.7)]:
        ax.annotate('', xy=(right, 1.9), xytext=(left, 1.9),
                    arrowprops={'arrowstyle': '->', 'color': '#286c94', 'linewidth': 1.5})
    ax.text(6.1, 4.05, '可逆消元：第二式减去两倍第一式，第一式仍保留',
            ha='center', fontsize=16)
    ax.text(6.1, .2, '代回原来的两式：2 × 2 + 3 × 1 = 7，4 × 2 − 1 = 7。',
            ha='center', fontsize=14)
    ax.set_xlim(-.2, 12.4); ax.set_ylim(-.1, 4.45); ax.axis('off')
    for label in fig.findobj(Text):
        label.set_fontproperties(FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc', size=label.get_fontsize()))
    fig.savefig(out/'b2_elimination_steps.png', dpi=180, bbox_inches='tight', facecolor='white')
    plt.close(fig)

def draw_absolute_bounds(out):
    """Schematic rational membership, not a construction of the real line."""
    fig, ax = plt.subplots(figsize=(12, 5.8))
    rows = [(3.6, r'$|x-1|\leq 2$', 'inside', True),
            (2.1, r'$|x-1|<2$', 'inside', False),
            (.6, r'$|x-1|\geq 2$', 'outside', True)]
    for y, label, region, closed in rows:
        ax.text(-4.6, y, label, ha='right', va='center', fontsize=18)
        ax.plot([-3, 5], [y, y], color='#b8c2cb', linewidth=1.2)
        if region == 'inside':
            ax.plot([-1, 3], [y, y], color='#286c94', linewidth=3)
        else:
            for start, end in [(-1, -3), (3, 5)]:
                ax.annotate('', xy=(end,y), xytext=(start,y),
                            arrowprops={'arrowstyle':'->', 'color':'#286c94', 'linewidth':3})
        for x in [-1, 1, 3]:
            ax.plot([x,x], [y-.09,y+.09], color='#526575', linewidth=1)
            ax.text(x, y-.29, str(x), ha='center', va='top', fontsize=15)
        ax.scatter([-1,3], [y,y], s=105, edgecolors='#286c94',
                   facecolors='#286c94' if closed else 'white', linewidths=2, zorder=4)
    ax.text(-.5, 4.5, '同一中心与阈值：端点是否包含，范围在内侧还是两侧',
            ha='center', fontsize=16)
    ax.text(-.5, -.42, '实心点含端点，空心点不含端点；线条与箭头只示意有理数成员范围。',
            ha='center', fontsize=13)
    ax.set_xlim(-7,6); ax.set_ylim(-.7,4.9); ax.axis('off')
    for label in fig.findobj(Text):
        label.set_fontproperties(FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc', size=label.get_fontsize()))
    fig.savefig(out/'b2_absolute_bounds.png', dpi=180, bbox_inches='tight', facecolor='white')
    plt.close(fig)


def draw_affine_coordinates(out):
    """Only five exact rational samples per graph; no complete curve is drawn."""
    from fractions import Fraction
    from rational_affine import affine_value
    xs = [Fraction(-1), Fraction(0), Fraction(1, 2), Fraction(1), Fraction(2)]
    fig, ax = plt.subplots(figsize=(10, 6.2))
    ax.axhline(0, color='#9aa6b2', linewidth=1)
    ax.axvline(0, color='#9aa6b2', linewidth=1)
    for a, b, marker, color, label in [(2, -1, 'o', '#286c94', r'$f(x)=2x-1$'),
                                      (-1, 2, 'x', '#b65c21', r'$g(x)=-x+2$')]:
        ys = [affine_value(a, b, x) for x in xs]
        ax.scatter([float(x) for x in xs], [float(y) for y in ys],
                   s=100, marker=marker, color=color, linewidths=2,
                   facecolors='none' if marker == 'o' else color, label=label, zorder=3)
    for x, y, label, dx, dy in [(0,-1,r'$(0,-1)$',.12,-.35),
                               (.5,0,r'$(1/2,0)$',.12,-.35),
                               (0,2,r'$(0,2)$',.12,.20),
                               (2,0,r'$(2,0)$',.12,.18),
                               (1,1,r'$(1,1)$',.12,.20)]:
        ax.text(x+dx, y+dy, label, fontsize=14)
    ax.text(2.43, -.33, '$x$', fontsize=16)
    ax.text(.08, 3.30, '$y$', fontsize=16)
    ax.set_xlim(-1.5,2.55); ax.set_ylim(-3.5,3.65)
    ax.set_xticks([-1,0,.5,1,2], ['−1','0','1/2','1','2'])
    ax.set_yticks([-3,-2,-1,0,1,2,3])
    ax.grid(alpha=.15); ax.tick_params(labelsize=12)
    ax.set_title('相同输入，两种规则：圈与叉只标五个样本', fontsize=17, pad=16)
    ax.legend(loc='lower right', fontsize=15, framealpha=.95)
    fig.text(.5,.02,'公共点须代入两式证明；有限标记不等于完整函数图。',ha='center',fontsize=14)
    fig.subplots_adjust(bottom=.13)
    for label in fig.findobj(Text):
        label.set_fontproperties(FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc', size=label.get_fontsize()))
    fig.savefig(out/'b2_affine_coordinates.png', dpi=180, bbox_inches='tight', facecolor='white')
    plt.close(fig)


def draw_finite_sum(out):
    """Finite exact input table and accumulated values; no infinite summation."""
    from fractions import Fraction
    from rational_powers_sums import partial_sums, segment_sum
    values = [Fraction(1,2), Fraction(-1), Fraction(3,2), Fraction(2)]
    prefixes = partial_sums(values)
    left, right = segment_sum(values,0,2), segment_sum(values,2,2)
    def label(q):
        if q.denominator == 1:
            return str(q.numerator)
        sign = '-' if q < 0 else ''
        return sign+r'\frac{'+str(abs(q.numerator))+'}{'+str(q.denominator)+'}'
    fig, ax = plt.subplots(figsize=(12, 5.5))
    for i, value in enumerate(values):
        color = '#e2eef5' if i < 2 else '#f8ead8'
        ax.add_patch(Rectangle((i-.36,2.6),.72,.65,facecolor=color,edgecolor='#64748b'))
        ax.text(i,2.925,'$'+label(value)+'$',ha='center',va='center',fontsize=22)
        ax.text(i,3.48,'$a_{'+str(i)+'}$',ha='center',fontsize=16)
    ax.text(-1.14,2.93,'四个项',ha='center',fontsize=14)
    for i, value in enumerate(prefixes):
        x = i-1
        ax.text(x,1.73,'$S_{'+str(i)+'}$',ha='center',fontsize=16)
        ax.text(x,1.22,'$'+label(value)+'$',ha='center',fontsize=22)
        if i < 4:
            ax.annotate('',xy=(x+.66,1.34),xytext=(x+.30,1.34),
                        arrowprops={'arrowstyle':'->','color':'#64748b','linewidth':1.5})
    ax.text(-1,.73,'空前缀',ha='center',fontsize=13)
    ax.text(1.2,.13,'$S_4=('+label(left)+')+('+label(right)+')=3$',ha='center',fontsize=21)
    ax.text(1.0,4.17,'从空和开始，每步只加入一项',ha='center',fontsize=18)
    ax.text(1.0,-.52,'把四项分成前两项与后两项，不漏项，也不重复项。',ha='center',fontsize=14)
    ax.set_xlim(-1.7,3.7); ax.set_ylim(-.8,4.6); ax.axis('off')
    for text_item in fig.findobj(Text):
        text_item.set_fontproperties(FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc', size=text_item.get_fontsize()))
    fig.savefig(out/'b2_finite_sum.png',dpi=180,bbox_inches='tight',facecolor='white')
    plt.close(fig)


def draw_polynomial_records(out):
    """Fixed exact coefficient positions; box positions are only layout."""
    from rational_polynomial_basic import normalize, coefficient, evaluate
    original = (1,0,2,0,0)
    canonical = normalize(original)
    different = (1,2)
    rows = [(original, '原记录', 2.5),
            (canonical, '规范记录', 1.35),
            (different, '另一多项式', .2)]
    fig, ax = plt.subplots(figsize=(11,5.5))
    for i in range(5):
        ax.text(i,3.4,'$i='+str(i)+'$',ha='center',fontsize=16)
    for values,name,y in rows:
        ax.text(-1.2,y+.25,name,ha='center',va='center',fontsize=15)
        for i in range(5):
            present = i < len(values)
            color = '#e2eef5' if present else '#f1f3f5'
            if name == '原记录' and i >= len(canonical):color='#f8ead8'
            if name == '另一多项式' and i==1:color='#f6d9d7'
            ax.add_patch(Rectangle((i-.36,y),.72,.55,facecolor=color,edgecolor='#64748b',linestyle='-' if present else ':'))
            value = coefficient(values,i)
            ax.text(i,y+.275,str(value),ha='center',va='center',fontsize=19,color='#24364b' if present else '#767e88')
    assert evaluate(original,2)==9 and evaluate(different,2)==5
    ax.text(1.5,4.02,'尾零可以省去，中间零保留原位置',ha='center',fontsize=19)
    ax.text(1.5,-.55,'虚线框是补零系数，不计入记录长度。',ha='center',fontsize=14)
    ax.text(1.5,-1.05,'前两行表示同一多项式；第三行的一次位系数不同。',ha='center',fontsize=14)
    ax.set_xlim(-2.1,4.6);ax.set_ylim(-1.3,4.4);ax.axis('off')
    for item in fig.findobj(Text):
        item.set_fontproperties(FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',size=item.get_fontsize()))
    fig.savefig(out/'b2_polynomial_records.png',dpi=180,bbox_inches='tight',facecolor='white')
    plt.close(fig)


def draw_polynomial_product(out):
    from rational_polynomial_product import multiply
    a,b=(1,-1,2),(0,3)
    result=multiply(a,b)
    assert result==(0,3,-3,6)
    colors=['#e2eef5','#f8ead8','#e4f0df','#eadff1']
    fig,ax=plt.subplots(figsize=(10,6))
    for j,v in enumerate(b):
        ax.text(1.4*j,3.8,f'j = {j}，系数 {v}',ha='center',fontsize=15)
    for i,v in enumerate(a):
        y=2.8-i
        ax.text(-1.3,y+.3,f'i = {i}，系数 {v}',ha='right',va='center',fontsize=15)
        for j,w in enumerate(b):
            ax.add_patch(Rectangle((1.4*j-.6,y),1.2,.65,facecolor=colors[i+j],edgecolor='#64748b'))
            ax.text(1.4*j,y+.325,str(v*w),ha='center',va='center',fontsize=20)
            ax.text(1.4*j,y-.25,f'i+j = {i+j}',ha='center',fontsize=11)
    ax.text(.7,4.5,'乘积系数：把指标和相同的项相加',ha='center',fontsize=19)
    ax.text(.7,4.12,'P = (1, −1, 2)，Q = (0, 3)',ha='center',fontsize=16)
    for k in range(4):
        pos=-1.6+1.55*k
        ax.add_patch(Rectangle((pos-.64,-.45),1.28,.65,facecolor=colors[k],edgecolor='#64748b'))
        ax.text(pos,-.1,f'k={k}：{result[k]}',ha='center',va='center',fontsize=15)
    ax.text(.7,-1.0,'候选第五项为零；规范乘积为 (0, 3, −3, 6)。',ha='center',fontsize=14)
    ax.text(.7,-1.45,'同色格属于同一系数；图示不代替一般索引证明。',ha='center',fontsize=14)
    ax.set_xlim(-3,4.3);ax.set_ylim(-1.8,4.9);ax.axis('off')
    for item in fig.findobj(Text):
        item.set_fontproperties(FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',size=item.get_fontsize()))
    fig.savefig(out/'b2_polynomial_product.png',dpi=180,bbox_inches='tight',facecolor='white')
    plt.close(fig)


def draw_quadratic_bound(out):
    """Eight exact rational samples; no interpolation of the Q-valued graph."""
    from fractions import Fraction as F
    with plt.rc_context({'axes.unicode_minus': True}):
        xs=[F(-2),F(-3,2),F(-1),F(-3,4),F(-1,2),F(0),F(1,2),F(1)]
        ys=[2*x*x+3*x-2 for x in xs]
        h,k=F(-3,4),F(-25,8)
        assert all(y-k==2*(x-h)*(x-h) for x,y in zip(xs,ys))
        assert all(y>=k for y in ys)
        fig,ax=plt.subplots(figsize=(9.4,4.8))
        ax.axhline(0,color='#a6afba',lw=1);ax.axvline(0,color='#a6afba',lw=1)
        ax.axhline(float(k),color='#ad7023',ls='--',lw=1.3)
        ax.scatter([float(x) for x in xs],[float(y) for y in ys],s=50,color='#256a8a',zorder=3)
        ax.scatter([float(h)],[float(k)],s=88,color='#b65c21',zorder=4)
        ax.annotate(r'$h=-3/4,\quad F(h)=-25/8$',xy=(float(h),float(k)),xytext=(-1.95,-4.22),
                    arrowprops=dict(arrowstyle='->',color='#b65c21'),fontsize=14,color='#8d4b1b')
        ax.text(1.20,float(k)+.16,r'$\kappa=-25/8$',ha='right',fontsize=13,color='#8d4b1b')
        ax.set_xticks([float(x) for x in xs]);ax.set_xticklabels(['−2','−3/2','−1','−3/4','−1/2','0','1/2','1'])
        ax.tick_params(axis='x',labelsize=12);ax.tick_params(axis='y',labelsize=12)
        ax.set_xlim(-2.3,1.3);ax.set_ylim(-4.7,3.8)
        ax.set_xlabel('有理输入 t（图中仅取八个）',fontsize=13)
        ax.set_ylabel('F(t)',fontsize=13)
        ax.set_title(r'$F(t)=2t^2+3t-2=2(t+3/4)^2-25/8$',fontsize=17,pad=15)
        ax.spines[['top','right']].set_visible(False)
        for label in fig.findobj(Text):
            label.set_fontproperties(FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',size=label.get_fontsize()))
        fig.tight_layout();fig.savefig(out/'b2_quadratic_bound.png',dpi=180,bbox_inches='tight',facecolor='white');plt.close(fig)


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
    fig,ax=plt.subplots(figsize=(10,4.5))
    ax.set_xlim(0,10)
    ax.set_ylim(0,4.5)
    ax.axis('off')
    ax.text(5,4.12,r'$f(q)=(2q+2)/(q+2),\quad q\geq 0$',ha='center',fontsize=18)
    for k,(row,color,y,title) in enumerate(zip(
            chains, ['#256a8a','#a85d25'], [2.65,.85],
            ['S 中更大的成员','更小的有理上界'])):
        ax.text(.2,y+.6,title,color=color,fontsize=14)
        for j,x in enumerate(row):
            pos=1.25+3.5*j;square=x*x
            ax.text(
                pos, y, str(x), ha='center', va='center', fontsize=21,
                color=color,
                bbox=dict(boxstyle='round,pad=.35', fc='#f7f9fa', ec=color))
            sign='<' if k==0 else '>'
            ax.text(pos,y-.56,f'平方为 {square} {sign} 2',
                    ha='center',fontsize=12,color=color)
            if j<2:
                ax.annotate(
                    '', xy=(pos+2.88,y), xytext=(pos+.65,y),
                    arrowprops=dict(arrowstyle='->', lw=1.6, color=color))
                ax.text(pos+1.75,y+.18,'应用 f',ha='center',fontsize=12,color=color)
    for label in fig.findobj(Text):
        label.set_fontproperties(FontProperties(
            fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
            size=label.get_fontsize()))
    fig.tight_layout()
    fig.savefig(out/'b2_rational_gap.png', dpi=180,
                bbox_inches='tight', facecolor='white')
    plt.close(fig)


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
    fig,ax=plt.subplots(figsize=(10.6,3.8))
    ax.set_xlim(-.9,5.5)
    ax.set_ylim(-1.55,2.2)
    ax.axis('off')
    ax.text(
        2.25,1.9,
        r'$A=i(3/2),\quad\varepsilon=1/2,\quad\delta=\varepsilon/2=1/4$',
        ha='center',fontsize=17,
    )
    ax.text(-.78,.72,'指标 n',ha='center',fontsize=12)
    ax.text(-.78,.15,'有理点',ha='center',fontsize=12)
    for n,(q,member) in enumerate(zip(points,inside)):
        color='#256a8a' if member else '#a85d25'
        ax.text(n,.72,str(n),ha='center',fontsize=14)
        ax.text(
            n,.15,str(q),ha='center',va='center',fontsize=18,color=color,
            bbox=dict(boxstyle='round,pad=.25',ec=color,fc='#f7f9fa'),
        )
        ax.text(
            n,-.35,'在 A 内' if member else '不在 A 内',
            ha='center',fontsize=11,color=color,
        )
    ax.text(1,-.82,r'$u=5/4$',ha='center',fontsize=13,color='#256a8a')
    ax.text(2,-.82,r'$v=3/2$',ha='center',fontsize=13,color='#a85d25')
    ax.text(4,-.82,r'$b_0=2$',ha='center',fontsize=13,color='#a85d25')
    ax.text(5,-.82,r'$M=5$',ha='center',fontsize=13,color='#a85d25')
    ax.text(1.5,-1.28,r'$m=2,\quad v-u=1/4<\varepsilon$',ha='center',fontsize=15)
    for label in fig.findobj(Text):
        label.set_fontproperties(FontProperties(
            fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
            size=label.get_fontsize(),
        ))
    fig.tight_layout()
    fig.savefig(
        out/'b2_dedekind_grid.png',dpi=180,
        bbox_inches='tight',facecolor='white',
    )
    plt.close(fig)


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
             '上式证明整个尾段；有限点图只展示样例。'
             '此图只处理一个 ε，不代替任意 ε 的收敛证明。',
             ha='center', fontsize=10.5)
    fig.text(.5, .035,
             '因 n=3 仍等于边界，任何 N≤3 都不合要求；'
             '故本例最早严格阈值为 N=4。',
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


def main():
    plt.rcParams['axes.unicode_minus']=False
    fig,ax=plt.subplots(figsize=(9,3.8))
    colors=['#31688e','#35b779','#e89a36']
    for i,(title,unit,count) in enumerate([('百位','每片表示100',2),('十位','每片表示10',0),('个位','每片表示1',3)]):
        ax.add_patch(Rectangle((i*3+.1,.5),2.8,2.4,facecolor='#f5f7fa',edgecolor='#6b7785',lw=1.2))
        ax.text(i*3+1.5,3.2,title,ha='center',fontsize=16)
        ax.text(i*3+1.5,2.6,unit,ha='center',fontsize=12)
        for j in range(count):
            ax.add_patch(Circle((i*3+.75+j*.75,1.75),.21,color=colors[i]))
        if count==0:ax.text(i*3+1.5,1.75,'0片',ha='center',va='center',fontsize=13)
        ax.text(i*3+1.5,.9,f'数字 {count}',ha='center',fontsize=14)
    ax.text(4.5,.05,'2 × 100 + 0 × 10 + 3 × 1 = 203',ha='center',fontsize=15)
    ax.set_xlim(0,9);ax.set_ylim(-.15,3.65);ax.axis('off')
    out=ROOT/'dist/figures';out.mkdir(parents=True,exist_ok=True)
    for label in fig.findobj(Text):
        label.set_fontproperties(FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc', size=label.get_fontsize()))
    fig.savefig(out/'b1_place_value.png',dpi=180,bbox_inches='tight',facecolor='white')
    plt.close(fig)
    draw_rational_distance(out)
    draw_ratio_allocation(out)
    draw_function_mapping(out)
    draw_inverse_mapping(out)
    draw_elimination_steps(out)
    draw_absolute_bounds(out)
    draw_affine_coordinates(out)
    draw_finite_sum(out)
    draw_polynomial_records(out)
    draw_polynomial_product(out)
    draw_quadratic_bound(out)
    draw_rational_gap(out)
    draw_dedekind_grid(out)
    draw_real_plane(out)
    draw_real_projection(out)
    draw_real_sequence_epsilon(out)

if __name__=='__main__':main()
