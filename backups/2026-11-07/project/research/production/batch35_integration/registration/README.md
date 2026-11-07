# FRC/RFS/FLC 第73—75单元候选（未应用）

基于保全的74项候选，仅追加最终已独立数学与教学审读的FLC。当前正式登记仍72；本目录不改正式正文/工具/accepted/产物，不运行构建。完整保留旧74spec、148稿源路径与148文字审签，新候选75单元、600基础题答+27第一部分=627对、150文字审签。

顺序固定FRC/B4.L1(73)→RFS/B2.39(74)→FLC/B4.L2(75)，旧编号不改。FLC主归第11部分15-XX、第84章15Axx、15A03局部，锚flc-unit、题答flc-q01—08/flc-a01—08、来源flc-sources。主分类不因阅读顺序变化。冻结稿标题不改，builder以后另做学习号映射。

## 精确依赖与模块图判断

现有模块记录明确标为`module_plan_not_complete_chapter_dependency_specification`。root确认保持概略MODULES全部边；不是把该图冒充全量证明先修。FLC spec登记18个实际正文先修锚，必含FRC模型/运算/加法/标量/重编号及RFS的definition、prefix-table、linearity、concatenation、padding。linear-algebra的scope_boundary另明确B4.L2→B4.L1和B2.39及其逐锚接口，B2.39来自real-algebra-equations。没有让B4.L1依赖整个实数方程模块，也没有说FLC可跳过实数和。

相对74候选，MODULES连显示标题也完全不变；相对正式72只继承此前已批准的real-algebra-equations显示标题扩充，ID/stage/tags/edges均未变。模块实际覆盖增加FLC，未写内容仍含张成、基、线性相关、维数、秩、lineability、抽象空间、一般线性映射、矩阵、行列式及任意项重排/换序。RFS模块文字注明具体组合由B4.L2另模块提供；各旧单元spec未覆盖范围仍保留，不能把单元局部边界误说成全书当前状态。

FLC1以两层函数类型和RFS实数表和构造组合，分别核m0/n0及一项两项；FLC2—6为系数相加、共同缩放、向量项相加、同步拼接和坐标重编号。不引一般向量和递归、向量项任意重排、双重和、张成、基或维数。

## 审签、来源与基线

新增math=/root/part1_audit、ped=/root两真实全文八解报告。正式两稿与实际/tmp审稿hash一致。报告日期只有2026-11-05，登记不虚构时分。源/计划/作者自检原“未审/暂存”状态是历史，不覆写旧取得时间；它们不是独立通过证据。

本次只核source记录和审读报告及缓存hash，没有新网络请求或假称重新全文读源书。原sourceJSON保留实际/tmp读位置，保全映射为`local-inputs/pending-batch35/finite-linear-combinations-cache-preservation.json`；逐一确认固定section-LC.xml、目录快照、requests.json及旧COPYING/bookinfo哈希。保全JSON仅是本地核验baseline，不加进书稿来源依赖列表，不复制外部原文进候选或分发。

原74候选baseline中的validator已有root正式修复：10e0078b…→14a36b32…，只把`.md#`检测改为区分公开HTTP(S)引用与本地稿件路径。已实际读精确diff，新registration明确记录baseline_refresh，旧候选历史不改。其余基线hash全部相同。

`flc_delta.diff`是相对74的新增差异，`build_production_ledger.diff`是相对正式72累计差异；accepted_reviews_flc_delta.diff只新增两签。frc-rfs74-base保留原候选。checks核AST语法、旧对象/审签、先修锚、8对题答及内存unit_records；不调用build/main、不写正式台账、不签PDF/视觉。

正式应用仍需先封存本批，按baseline复核，再配套更新builder/validator。必须显示84→528续→84续及真实第11/63部分返回，不能将RFS错误放进线性代数分类下。未完成披露、题答/源hash和新产物视觉均须重新核验。
