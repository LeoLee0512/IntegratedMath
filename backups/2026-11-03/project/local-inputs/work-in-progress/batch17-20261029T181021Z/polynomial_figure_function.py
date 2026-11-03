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
