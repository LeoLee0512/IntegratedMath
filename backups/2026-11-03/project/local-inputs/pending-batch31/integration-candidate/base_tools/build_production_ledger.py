#!/usr/bin/env python3
"""Rebuild truthful manuscript production ledgers; requires only Python's standard library.

The classification index is scope, never evidence of written or reviewed teaching.
Registration below is explicit: no arbitrary Markdown glob can count as a chapter.
Review reports are candidates until tied to the exact manuscript snapshot and scope.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {'major': 63, 'intermediate': 534, 'general_leaf': 503, 'subject_leaf': 5503}
STAGES = ['unwritten', 'draft', 'math-reviewed', 'pedagogy-reviewed', 'build-verified']
CH01 = ['manuscript/review_ch01/chapter.md', 'manuscript/review_ch01/answers.md',
        'manuscript/review_ch01/appendices.md']
BRIDGE = ['manuscript/foundations/natural_numbers.md',
          'manuscript/foundations/natural_numbers_answers.md',
          'manuscript/foundations/place_value.md',
          'manuscript/foundations/place_value_answers.md',
          'manuscript/foundations/natural_order.md',
          'manuscript/foundations/natural_order_answers.md',
          'manuscript/foundations/division_remainder.md',
          'manuscript/foundations/division_remainder_answers.md',
          'manuscript/foundations/positional_representation.md',
          'manuscript/foundations/positional_representation_answers.md',
          'manuscript/foundations/natural_subtraction.md',
          'manuscript/foundations/natural_subtraction_answers.md',
          'manuscript/foundations/integers_addition_order.md',
          'manuscript/foundations/integers_addition_order_answers.md',
          'manuscript/foundations/integers_multiplication.md',
          'manuscript/foundations/integers_multiplication_answers.md',
          'manuscript/foundations/integer_division.md',
          'manuscript/foundations/integer_division_answers.md',
          'manuscript/foundations/divisibility.md',
          'manuscript/foundations/divisibility_answers.md',
          'manuscript/foundations/gcd_euclidean.md',
          'manuscript/foundations/gcd_euclidean_answers.md',
          'manuscript/foundations/bezout.md',
          'manuscript/foundations/bezout_answers.md',
          'manuscript/foundations/coprimality.md',
          'manuscript/foundations/coprimality_answers.md',
          'manuscript/foundations/rationals_construction.md',
          'manuscript/foundations/rationals_construction_answers.md',
          'manuscript/foundations/rationals_addition.md',
          'manuscript/foundations/rationals_addition_answers.md',
          'manuscript/foundations/rationals_multiplication.md',
          'manuscript/foundations/rationals_multiplication_answers.md',
          'manuscript/foundations/rationals_division.md',
          'manuscript/foundations/rationals_division_answers.md',
          'manuscript/foundations/rationals_order.md',
          'manuscript/foundations/rationals_order_answers.md',
          'manuscript/foundations/rationals_absolute.md',
          'manuscript/foundations/rationals_absolute_answers.md',
          'manuscript/foundations/ratios_proportions.md',
          'manuscript/foundations/ratios_proportions_answers.md',
          'manuscript/foundations/quantities_units.md',
          'manuscript/foundations/quantities_units_answers.md',
          'manuscript/foundations/functions_definition.md',
          'manuscript/foundations/functions_definition_answers.md',
          'manuscript/foundations/functions_composition.md',
          'manuscript/foundations/functions_composition_answers.md',
          'manuscript/foundations/functions_bijections.md',
          'manuscript/foundations/functions_bijections_answers.md',
          'manuscript/foundations/functions_inverse.md',
          'manuscript/foundations/functions_inverse_answers.md',
          'manuscript/foundations/linear_equations.md',
          'manuscript/foundations/linear_equations_answers.md',
          'manuscript/foundations/linear_systems.md',
          'manuscript/foundations/linear_systems_answers.md',
          'manuscript/foundations/linear_inequalities.md',
          'manuscript/foundations/linear_inequalities_answers.md',
          'manuscript/foundations/absolute_inequalities.md',
          'manuscript/foundations/absolute_inequalities_answers.md',
          'manuscript/foundations/rational_coordinates.md',
          'manuscript/foundations/rational_coordinates_answers.md',
          'manuscript/foundations/affine_graphs.md',
          'manuscript/foundations/affine_graphs_answers.md',
          'manuscript/foundations/rational_powers.md',
          'manuscript/foundations/rational_powers_answers.md',
          'manuscript/foundations/finite_sums.md',
          'manuscript/foundations/finite_sums_answers.md',
          'manuscript/foundations/polynomial_records.md',
          'manuscript/foundations/polynomial_records_answers.md',
          'manuscript/foundations/polynomial_linear_operations.md',
          'manuscript/foundations/polynomial_linear_operations_answers.md',
          'manuscript/foundations/polynomial_multiplication.md',
          'manuscript/foundations/polynomial_multiplication_answers.md',
          'manuscript/foundations/polynomial_product_structure.md',
          'manuscript/foundations/polynomial_product_structure_answers.md',
          'manuscript/foundations/polynomial_linear_division.md',
          'manuscript/foundations/polynomial_linear_division_answers.md',
          'manuscript/foundations/polynomial_roots_identity.md',
          'manuscript/foundations/polynomial_roots_identity_answers.md',
          'manuscript/foundations/rational_square_equations.md',
          'manuscript/foundations/rational_square_equations_answers.md',
          'manuscript/foundations/rational_quadratic_equations.md',
          'manuscript/foundations/rational_quadratic_equations_answers.md',
          'manuscript/foundations/rational_gaps_bounds.md',
          'manuscript/foundations/rational_gaps_bounds_answers.md',
          'manuscript/foundations/dedekind_cuts_order.md',
          'manuscript/foundations/dedekind_cuts_order_answers.md',
          'manuscript/foundations/dedekind_addition.md',
          'manuscript/foundations/dedekind_addition_answers.md',
          'manuscript/foundations/dedekind_additive_order.md',
          'manuscript/foundations/dedekind_additive_order_answers.md',
          'manuscript/foundations/dedekind_nonnegative_product.md',
          'manuscript/foundations/dedekind_nonnegative_product_answers.md',
          'manuscript/foundations/dedekind_nonnegative_laws.md',
          'manuscript/foundations/dedekind_nonnegative_laws_answers.md',
          'manuscript/foundations/dedekind_signed_product.md',
          'manuscript/foundations/dedekind_signed_product_answers.md',
          'manuscript/foundations/dedekind_ring_order.md',
          'manuscript/foundations/dedekind_ring_order_answers.md',
          'manuscript/foundations/dedekind_inverse.md',
          'manuscript/foundations/dedekind_inverse_answers.md',
          'manuscript/foundations/dedekind_division_field.md',
          'manuscript/foundations/dedekind_division_field_answers.md',
          'manuscript/foundations/real_archimedean_density.md',
          'manuscript/foundations/real_archimedean_density_answers.md',
          'manuscript/foundations/real_square_roots.md',
          'manuscript/foundations/real_square_roots_answers.md',
          'manuscript/foundations/real_absolute_distance.md',
          'manuscript/foundations/real_absolute_distance_answers.md',
          'manuscript/foundations/real_quadratic_equations.md',
          'manuscript/foundations/real_quadratic_equations_answers.md',
          'manuscript/foundations/real_plane_affine.md',
          'manuscript/foundations/real_plane_affine_answers.md',
          'manuscript/foundations/real_plane_distance.md',
          'manuscript/foundations/real_plane_distance_answers.md',
          'manuscript/foundations/real_plane_lines.md',
          'manuscript/foundations/real_plane_lines_answers.md',
          'manuscript/foundations/real_plane_projection.md',
          'manuscript/foundations/real_plane_projection_answers.md',
          'manuscript/foundations/real_sequences_limits.md',
          'manuscript/foundations/real_sequences_limits_answers.md',
          'manuscript/foundations/real_sequences_algebra.md',
          'manuscript/foundations/real_sequences_algebra_answers.md']
# Each tuple: module id, stage, title, prerequisite module ids, MSC locating tags.
MODULES = [
 ('reading','B0','阅读数学与核查论证',[],['00']),
 ('natural','B1','计数与自然数运算',['reading'],['03','11']),
 ('place-value','B1','十进位值与书面运算',['natural'],['11']),
 ('natural-order','B1','自然数序与强归纳',['natural','place-value'],['03','11']),
 ('division','B1','自然数带余除法',['natural-order'],['11']),
 ('positional','B1','规范位值表示与终止性',['division'],['11','68']),
 ('written-arithmetic','B1','自然数减法与逐位加减',['positional'],['11','68']),
 ('integer-addition-order','B1','整数的表示、加法与次序',['written-arithmetic'],['03','11']),
 ('integer-multiplication','B1','整数乘法与符号规则',['integer-addition-order'],['11']),
 ('integer-division','B1','整数带余除法',['integer-multiplication','division'],['11']),
 ('divisibility','B1','整数整除关系',['integer-division'],['11']),
 ('gcd-euclidean','B1','公因数与欧几里得算法',['divisibility','natural-order'],['11','68']),
 ('bezout','B1','贝祖等式与扩展欧几里得算法',['gcd-euclidean'],['11','68']),
 ('coprimality','B1','互素、整除消去与整数对的规范记录',['bezout'],['11']),
 ('rational-construction','B1','有理数的构造与规范表示',['coprimality'],['03','11']),
 ('rational-arithmetic','B1','有理数运算与良定义',['rational-construction'],['11']),
 ('rational-order','B1','有理数次序、绝对值与有理距离',['rational-arithmetic'],['11','26']),
 ('number-systems','B1','分数与实数的概念桥接',['rational-order','functions'],['03','11','26','97']),
 ('prime-factorization','B1','素数与唯一分解',['coprimality','natural-order'],['11']),
 ('relations-units','B1','等式、不等式、比例与单位',['rational-order'],['11','26','97']),
 ('functions','B2','变量、函数、坐标与图像',['relations-units'],['03','26','97']),
 ('real-algebra-equations','B2','实数方程与配方界',['functions','number-systems'],['97']),
 ('real-plane-geometry','B2','实数坐标、位移与欧氏距离',['functions','number-systems'],['97','51','54']),
 ('elementary-geometry','B2','图形、长度与面积',['relations-units'],['51']),
 ('logic-sets','B3','集合、量词、映射与证明规则',['relations-units','functions'],['03']),
 ('induction-counting','B3','归纳法与有限计数',['logic-sets'],['03','05','11']),
 ('number-construction-revisit','B3','回访数系构造及其公理基础',['logic-sets','induction-counting'],['03','11']),
 ('linear-algebra','B4','向量空间与线性映射',['logic-sets','functions'],['15']),
 ('single-analysis','B4','极限、连续、微分与积分',['functions','induction-counting','number-systems'],['26','40']),
 ('groups','B5','群与同态',['logic-sets','induction-counting'],['20']),
 ('rings-fields','B5','环、域与代数扩张',['groups','linear-algebra'],['12','13']),
 ('real-measure','B5','实分析、可测性与积分',['single-analysis','logic-sets'],['26','28']),
 ('multivariable','B5','多变量微积分',['single-analysis','linear-algebra'],['26']),
 ('complex-analysis','B5','复分析',['single-analysis','multivariable'],['30']),
 ('ode','B5','常微分方程',['single-analysis','linear-algebra'],['34']),
 ('topology','B5','点集拓扑',['logic-sets','functions'],['54']),
 ('probability','B5','概率基础',['induction-counting','single-analysis'],['60']),
 ('functional-analysis','B6','赋范空间与泛函分析',['real-measure','linear-algebra','topology'],['46']),
 ('manifolds','B6','光滑流形与微分几何',['topology','multivariable','linear-algebra'],['53','57']),
 ('quotient-fundamental-group','B6','商空间与基本群',['topology','groups'],['55']),
 ('homology','B6','链复形与同调',['quotient-fundamental-group','linear-algebra'],['18','55']),
 ('distributions-sobolev','B6','分布与索伯列夫空间',['functional-analysis','multivariable'],['35','46']),
 ('hilbert-spectrum','B6','希尔伯特空间与谱理论',['functional-analysis'],['46','47']),
 ('elliptic-foundations','B6','椭圆方程与弱解基础',['distributions-sobolev','ode'],['35']),
 ('spectral-geometry','B6','拉普拉斯谱与几何',['manifolds','hilbert-spectrum','elliptic-foundations'],['53','58']),
]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def existing(root, paths):
    return [p for p in paths if (root/p).is_file() and (root/p).stat().st_size > 0]


def evidence(root, paths):
    return [{'path': p, 'sha256': digest(root/p)} for p in existing(root, paths)]


def record(root, row, number, part_code, files, body_files, scope):
    sources = existing(root, files)
    bodies = existing(root, body_files)
    drafted = bool(bodies)
    return {
        'code': row['code'], 'number': number, 'title': row['title_zh'],
        'parent_code': row['parent_code'], 'part_code': part_code, 'level': row['level'],
        'source_files': sources, 'source_snapshot': evidence(root, sources),
        'body_source_files': bodies,
        'stage': 'draft' if drafted else 'unwritten',
        'stages': {
            'unwritten': {'status': 'false' if drafted else 'true', 'evidence': []},
            'draft': {'status': scope if drafted else 'not_started',
                      'evidence': evidence(root, bodies)},
            'math-reviewed': {'status': 'pending', 'evidence': []},
            'pedagogy-reviewed': {'status': 'pending', 'evidence': []},
            'build-verified': {'status': 'pending', 'evidence': []},
        },
        'coverage': {'scope': scope if drafted else 'none', 'completed': False,
                     'unwritten_topics': '需逐目标登记；存在草稿或章节标题不构成整章／节完成'},
        'learning_entry': {'status': 'pending', 'module_ids': [], 'diagnostic_exercises': [],
                           'prerequisite_definition_anchors': [], 'adopted_assumptions': []},
        'learning_objectives': {'status': 'needs_planning', 'items': []},
        'depth_plan': {'status': 'needs_planning', 'per_objective_depth': [],
                       'policy': '按学习目标确定完整教学或专题导读；不把全部未写章统一降为导读'},
        'source_verification': {'status': 'pending', 'records': [],
                                'requirements_ref': 'source_requirements'},
        'cross_references': {'status': 'pending', 'proved': [], 'adopted': [],
                             'external': [], 'open_problems': []},
        'exercise_answer_separation': {
            'status': 'files_present_unreviewed' if any('answers' in p for p in sources) and drafted else 'pending',
            'exercise_files': bodies, 'answer_files': [p for p in sources if 'answers' in p],
            'paired_ids_verified': False},
        'review_evidence': {'math': [], 'pedagogy': [], 'build': [],
                            'candidate_reports': [], 'promotion_requires_current_hash_and_scope': True},
    }


def prerequisite_data(root, chapters):
    ids = {m[0] for m in MODULES}
    edges = [{'from': dep, 'to': mid, 'kind': 'learning_prerequisite'}
             for mid, _, _, deps, _ in MODULES for dep in deps]
    assert all(e['from'] in ids and e['to'] in ids for e in edges)
    visited, active = set(), set()
    def visit(mid):
        if mid in active:
            raise ValueError('Circular module prerequisite: '+mid)
        if mid in visited:
            return
        active.add(mid)
        for edge in edges:
            if edge['to'] == mid:
                visit(edge['from'])
        active.remove(mid)
        visited.add(mid)
    for mid in ids:
        visit(mid)
    modules = []
    for mid, stage, title, deps, tags in MODULES:
        planned = {'reading':CH01[:1], 'natural':BRIDGE[:1], 'place-value':BRIDGE[2:3],
                   'natural-order':BRIDGE[4:5], 'division':BRIDGE[6:7], 'positional':BRIDGE[8:9],
                   'written-arithmetic':BRIDGE[10:11], 'integer-addition-order':BRIDGE[12:13],
                   'integer-multiplication':BRIDGE[14:15], 'integer-division':BRIDGE[16:17],
                   'divisibility':BRIDGE[18:19], 'gcd-euclidean':BRIDGE[20:21],
                   'bezout':BRIDGE[22:23], 'coprimality':BRIDGE[24:25],
                   'rational-construction':BRIDGE[26:27],
                   'rational-arithmetic':BRIDGE[28:34:2],
                   'rational-order':BRIDGE[34:38:2],
                   'relations-units':BRIDGE[38:42:2],
                   'functions':BRIDGE[42:82:2],
                   'number-systems':BRIDGE[82:108:2],
                   'real-algebra-equations':BRIDGE[108:110:2],
                   'real-plane-geometry':BRIDGE[110:118:2],
                   'single-analysis':BRIDGE[118:122:2]}.get(mid,[])
        modules.append({'id': mid, 'stage': stage, 'title': title, 'prerequisites': deps,
                        'msc_tags': tags, 'source_files': existing(root, planned),
                        'implementation_status': 'partial_draft' if existing(root, planned) else 'unwritten',
                        'precision': 'module_plan_not_complete_chapter_dependency_specification',
                        'entry_diagnostic_status': 'needs_planning',
                        'definition_and_theorem_anchors': []})
        if mid == 'rational-arithmetic':
            arithmetic_parts = [
                (BRIDGE[28], ['加法与代表无关性', '相反数、加法消去与减法',
                              '整数加法兼容与加法方程']),
                (BRIDGE[30], ['乘法与代表无关性', '交换、结合、分配及整数乘法兼容',
                              '零乘积与非零因子消去']),
                (BRIDGE[32], ['非零倒数的构造、代表无关性与唯一性',
                              '除法及乘法方程的全部解分类', '分数记号兼容与带条件约分'])]
            modules[-1]['coverage'] = {
                'scope': 'registered_arithmetic_units_draft' if existing(root, planned) else 'none',
                'written_topics': [topic for path, topics in arithmetic_parts
                                   if existing(root, [path]) for topic in topics],
                'unwritten_topics': [topic for path, topics in arithmetic_parts
                                     if not existing(root, [path]) for topic in topics],
                'excluded_topics': ['有理数次序、绝对值与大小比较（独立rational-order模块）'],
                'completed': False,
                'note': '按B1.15至B1.17实际正文登记运算草稿；不自动授予完整模块完成或审阅状态，不包含有理数序。'}
        if mid == 'rational-order':
            order_parts = [
                (BRIDGE[34], ['正分母交叉比较及代表无关性', '全序、整数嵌入保序与符号判据',
                              '平移、取反及符号敏感的乘除比较']),
                (BRIDGE[36], ['有理数绝对值、区间界与乘商公式',
                              '三角与反三角不等式', '有理数值距离的四条性质'])]
            modules[-1]['coverage'] = {
                'scope': 'registered_order_units_draft' if existing(root, planned) else 'none',
                'written_topics': [topic for path, topics in order_parts
                                   if existing(root, [path]) for topic in topics],
                'unwritten_topics': [topic for path, topics in order_parts
                                     if not existing(root, [path]) for topic in topics],
                'excluded_topics': ['实数构造与完备性', '实数值度量的嵌入解释', '极限与连续性'],
                'completed': False,
                'note': 'B1.18—B1.19只登记有理数范围内的草稿，不授予完整模块或第26章完成状态。'}
        if mid == 'relations-units':
            relations_parts = [
                (BRIDGE[38], ['有条件的比、比例与交叉乘积判据', '共同非零倍率与按比分配',
                              '部分对部分及部分对整体的区分']),
                (BRIDGE[40], ['有理数值的量类别与单位模型', '正有理倍率的唯一换算、往返与复合',
                              '同类量的比与平均速率的单位转换'])]
            modules[-1]['coverage'] = {
                'scope': 'registered_relations_units_draft' if existing(root, planned) else 'none',
                'written_topics': [topic for path, topics in relations_parts
                                   if existing(root, [path]) for topic in topics],
                'unwritten_topics': ['百分数系统教学', '更广义等式与不等式专题',
                                     '实数值的量及测量不确定度理论'],
                'completed': False,
                'note': 'B1.20—B1.21定位97Fxx的两个教育叶节点；只有有理数范围的入门草稿。'}
            modules[-1]['scope_boundary'] = {
                'entry_domain': 'Q',
                'planned_entry_topics': ['后项非零的比', '逐项核查非零分母的比例变形',
                                         '精确有理倍率的单位换算'],
                'excluded_topics': ['实数构造', '完备性', '真实测量误差的一般理论'],
                'note': '此处先修只支持有理数范围的入门；更广义目标开写时补精确先修。'}
        if mid == 'functions':
            function_parts = [
                (BRIDGE[42], ['集合、笛卡尔积与函数三数据的入口',
                              '每输入恰有唯一输出、空集边界与像']),
                (BRIDGE[44], ['同定义域和目标集合的函数相等', '保目标集合的定义域限制',
                              '严格类型复合、恒等、结合与限制相容']),
                (BRIDGE[46], ['单射、满射、双射的量词、空集与目标边界',
                              '复合的单满射保持及反向推论的条件']),
                (BRIDGE[48], ['逆关系成为函数的双射判据与双侧逆唯一',
                              '逆复合反序、原像与有理数可逆规则']),
                (BRIDGE[50], ['有理数范围中的解集与等价变形',
                              '一元一次方程的全部参数分支及分母禁值']),
                (BRIDGE[52], ['二元一次方程组的可逆消元',
                              '零主元、全零系数与唯一无解参数解分类']),
                (BRIDGE[54], ['一次不等式的正负零系数分类与有理区间',
                              '严格非严格端点、交并及允许范围筛选']),
                (BRIDGE[56], ['绝对值内外条件的严格非严格比较',
                              '负零正半径、有理距离范围与全部解集']),
                (BRIDGE[58], ['有理有序对坐标、轴与函数图的完整判据',
                              '图的投影、目标集合边界及竖直例外']),
                (BRIDGE[60], ['仿射图像的斜率、截点及单调分类',
                              '两点拟合与相交、不交、重合的完整分支']),
                (BRIDGE[62], ['有理数非负整数幂的递归与零指数约定',
                              '加指数、乘积幂及幂的幂的归纳证明']),
                (BRIDGE[64], ['状态对递归构造前缀有限和',
                              '逐项一致、线性、拼接偏移与尾零稳定']),
                (BRIDGE[66], ['非空有限系数记录、尾零规范化与正式相等',
                              '非零次数与代表无关的有理求值']),
                (BRIDGE[68], ['逐系数加法、数乘、减法及良定义',
                              '求值线性兼容与最高项抵消的次数分支']),
                (BRIDGE[70], ['单步移位、一维倒序与有限卷积乘法的良定义',
                              '单位、交换、分配、数乘及移位相容']),
                (BRIDGE[72], ['按记录长度证明乘法结合与求值保乘',
                              '非零积次数、零积消去及平方差入口']),
                (BRIDGE[74], ['首一线性除式的唯一商余与求值余数',
                              '综合除法状态递归、后缀不变式与非零商次数']),
                (BRIDGE[76], ['有理因式定理及不同有理根数界',
                              '有界有限点判等与标准有理求值函数识别']),
                (BRIDGE[78], ['有理平方符号、部分平方根与最简表示判据', '平方方程全部解及正有理数无根边界']),
                (BRIDGE[80], ['配方与判别式的双向等价', '退化参数与全体有理解、有理输入界及唯一等号'])]
            modules[-1]['coverage'] = {
                'scope': 'registered_function_units_draft' if existing(root, planned) else 'none',
                'written_topics': [topic for path, topics in function_parts
                                   if existing(root, [path]) for topic in topics],
                'unwritten_topics': [topic for path, topics in function_parts
                                     if not existing(root, [path]) for topic in topics]
                                    + ['一般多项式除法、根的重数、其他数系的根存在性及一般系数环', '一般有限求和重排与无限级数',
                                       '超出有理仿射范围的坐标与函数图像', '一般函数方程与函数空间',
                                       '连续性、极限与实函数理论'],
                'completed': False,
                'note': 'B2.1—B2.20沿函数、方程、不等式、有理坐标及初等代数学习链登记实际目标；97I20、97H30与97H20分别归属，不是整个模块或分类叶的完整教学。'}
            modules[-1]['scope_boundary'] = {
                'entry_domain': '明确集合背景；数值例子限已建立的有理数',
                'note': '采用定义域、目标集合和图的三数据约定，不从图恢复目标；方程桥接限有理数及两个未知数，不把B4线性代数模块计为已写。这些早期有理桥接不依赖后来已写的实数构造；当前实数二次方程由独立real-algebra-equations模块接number-systems，连续图像与极限仍需另列精确先修。'}
        if mid == 'single-analysis':
            modules[-1]['coverage'] = {
                'scope': 'registered_sequence_entry_units_draft' if existing(root, planned) else 'none',
                'written_topics': ['实数数列与收敛量词、唯一性、基本例及尾移', '固定递归前缀界与收敛有界', '线性、绝对值、乘积及合法倒数商的极限'] if existing(root, planned) else [],
                'unwritten_topics': ['单调收敛、子列与完备性定理', '无穷级数', '函数极限、连续、微分与积分'],
                'completed': False,
                'note': 'B4.1—B4.2仅为入口；广义先修induction-counting仍未写，自然归纳与固定递归按前文公开采用。'}
            modules[-1]['definition_and_theorem_anchors'] = [
                anchor_ref(root, path, a) for path, names in [
                    (BRIDGE[118], ['seq-definition','seq-uniqueness','seq-basic-limits','seq-tails']),
                    (BRIDGE[120], ['seqlaw-bounded','seqlaw-linear-absolute','seqlaw-product','seqlaw-reciprocal-quotient'])]
                for a in names]
            modules[-1]['scope_boundary'] = {
                'entry_domain': '从已写函数、自然规则、实数域、绝对值与阿基米德性质直接进入；不依赖二维几何',
                'b3_formal_foundations_completed': False}
        if mid == 'real-plane-geometry':
            modules[-1]['coverage'] = {
                'scope': 'registered_real_plane_geometry_units_draft' if existing(root, planned) else 'none',
                'written_topics': ['实数点与位移的坐标模型', '参数直线、线段与等位移中点', '二维平方和、范数与欧氏距离', '一次方程与参数直线交会分类', '代数正交、投影、勾股与唯一最近点'] if existing(root, planned) else [],
                'unwritten_topics': ['角度测量、面积', '完整欧氏公理模型', '一般向量空间、内积空间及度量化'],
                'completed': False,
                'note': 'B2.35—B2.38仅主登记97G70的四个有限教学目标。'}
            modules[-1]['definition_and_theorem_anchors'] = [
                anchor_ref(root, path, a) for path, names in [
                    (BRIDGE[110], ['realplane-model','realplane-operations','realplane-lines','realplane-segments']),
                    (BRIDGE[112], ['planedist-cauchy','planedist-norm-laws','planedist-metric','planedist-segment-distances']),
                    (BRIDGE[114], ['planeline-determinant','planeline-equation','planeline-uniqueness','planeline-intersections']),
                    (BRIDGE[116], ['planeproj-inner-orthogonal','planeproj-foot','planeproj-nearest','planeproj-line-distance'])]
                for a in names]
            modules[-1]['scope_boundary'] = {
                'entry_domain': '已构造实数、非负根及绝对值上的二维坐标模型',
                'note': '向functions及number-systems单向取先修；36取35及33的精确接口；37不依赖36距离或38，38取35—37及实数平方绝对值；均不需31或34。保留广义elementary-geometry未来模块。'}
        if mid == 'real-algebra-equations':
            modules[-1]['coverage'] = {
                'scope': 'registered_real_quadratic_unit_draft' if existing(root, planned) else 'none',
                'written_topics': ['实数配方及判别式恒等式', '双向仿射换元与全部参数解集', '配方全局界与唯一达到输入'] if existing(root, planned) else [],
                'unwritten_topics': ['一般实形式多项式系统', '高次实方程和一般不等式系统', '微分与一般极值理论'],
                'completed': False,
                'note': '仅B2.34实际教学目标；这是学习模块，不新增分类章或叶。'}
            modules[-1]['definition_and_theorem_anchors'] = [
                anchor_ref(root, BRIDGE[108], a) for a in [
                    'realquad-completion', 'realquad-discriminant', 'realquad-solutions', 'realquad-bounds']]
            modules[-1]['scope_boundary'] = {
                'entry_domain': '已构造的实数有序域及非负平方根；全部实数候选域',
                'note': '单向依赖functions的集合函数语言和number-systems的实数运算/平方根；不反向改变旧functions模块依赖。精确先修按单元锚定位，B2.34不依赖B2.31或B2.33；旧有理配方仅为结构对照。'}
        if mid == 'number-systems':
            number_parts = [
                (BRIDGE[82], ['有理中点稠密与显式自然数界', '上界与上确界、平方缺口和无有理上确界']),
                (BRIDGE[84], ['单侧分割的集合背景、包含全序和有理嵌入', '非主分割与非空有上界族的并集上确界']),
                (BRIDGE[86], ['任意小的有理跨界见证', '和与负分割的四条件闭合及有理相容']),
                (BRIDGE[88], ['分割加法群律与逆元', '平移保序反射、取反、减法及加法方程']),
                (BRIDGE[90], ['非负乘积的成员定义及四条件闭合', '零与正性、交换单位、弱单调及有理相容']),
                (BRIDGE[92], ['非负乘积的结合与两侧分配', '正因子严格比较、反射及消去']),
                (BRIDGE[94], ['全部分割上的乘法及符号规律', '全符号结合、有理相容及零积条件']),
                (BRIDGE[96], ['全符号两侧分配及有序交换环', '各符号因子比较反射及非零消去']),
                (BRIDGE[98], ['正倒数候选四条件及逆元双包含', '非零倒数与唯一性、零无逆及有理相容']),
                (BRIDGE[100], ['非零分母除法、方程全参数分类与双射', '商比较及同一包含序下具上确界性质的有序域']),
                (BRIDGE[102], ['实数自然数严格界、阿基米德倍率及小倒数', '有理像稠密与给定宽度夹逼']),
                (BRIDGE[104], ['实数平方规律及非负平方根存在唯一', '平方方程全部解与二的非有理根']),
                (BRIDGE[106], ['实数绝对值、乘商与三角/反三角', '实数线距四性质、平移倍率与误差条件'])]
            modules[-1]['coverage'] = {
                'scope': 'registered_number_systems_real_absolute_distance_units_draft' if existing(root, planned) else 'none',
                'written_topics': [topic for path, topics in number_parts if existing(root, [path]) for topic in topics],
                'unwritten_topics': [topic for path, topics in number_parts if not existing(root, [path]) for topic in topics]
                    + ['一般实数幂与n次根、完备性等价及唯一同构', '无理长度的几何模型', '复数构造', '连续性与极限'],
                'completed': False,
                'note': '数系概念桥接的模块定位保留；实际已写入口为B2.21—B2.33，依赖B2集合函数、有理平方及已证自然最小元。登记分割集合、次序、有序交换加法群、非负分割乘积规律、全符号乘法的有序交换环及非零倒数与除法，汇总同一序下具上确界性质的完备有序域，再给实数阿基米德性、有理像稠密及非负平方根，再给实数绝对值、线距与误差界；不表示数系模块完成。'}
            modules[-1]['definition_and_theorem_anchors'] = [
                anchor_ref(root, path, anchor) for path, anchor in [
                    (BRIDGE[42], 'fun-sets'), (BRIDGE[42], 'fun-definition'), (BRIDGE[42], 'fun-image'),
                    (BRIDGE[34], 'rord-definition'), (BRIDGE[34], 'rord-laws'),
                    (BRIDGE[34], 'rord-integers'), (BRIDGE[34], 'rord-multiplication'),
                    (BRIDGE[78], 'sqrat-order'), (BRIDGE[78], 'sqrat-two-not-square')]]
            modules[-1]['scope_boundary'] = {
                'entry_domain': '已建立的有理数；新增对象为Q的非空真下闭无最大元子集',
                'adopted_set_background': anchor_ref(root, BRIDGE[84], 'cut-set-background'),
                'note': 'functions依赖只在已写集合/函数与SQ接口处使用；不反向令functions依赖number-systems。幂集存在公开采用；并集从Q按存在条件取子集。已证非空有上界族最小上界性质、有序交换加法群及全符号乘法的有序交换环、各符号因子比较与非零消去；已构造非零倒数和非零分母除法；完备有序域仅指同一包含序上旧DC4的非空有界族上确界性质，不称完整格，不推柯西完备或唯一同构；实数界与有理像稠密由分割见证得到，非负平方根由有序域和上确界独立证明，不依赖前一单元RA；有理网格引理不提供任意分割的成员判定或通用实数API。'}
    return {
        'schema_version': 1, 'basis': 'LEARNING_PATH.md',
        'basis_sha256': digest(root/'LEARNING_PATH.md'),
        'scope': '基础干线和三条示例支线的模块规划；不是534章或6006节的完整精确先修图',
        'stages': {f'B{i}': name for i, name in enumerate([
            '阅读数学','数与运算','函数与几何','证明与离散基础','大学共同基础','专业共同基础','深造入口'])},
        'modules': modules, 'edges': edges,
        'adopted_foundations': [{
            'module': 'natural', 'status': 'explicitly_adopted_not_proved_from_B3',
            'items': ['自然数含零与后继运算', '后继单射且零非后继', '自然数归纳原则',
                      '自然数递归原则及相应递归定义的存在唯一性'],
            'note': '实际单元必须逐条说明采用范围；不将尚未写出的B3构造视作已证先修。'},
            {'module': 'number-systems', 'status': 'explicitly_adopted_not_proved_from_B3',
             'items': ['有理数幂集P(Q)存在', '从P(Q)和Q按明确条件选取子集'],
             'source': anchor_ref(root, BRIDGE[84], 'cut-set-background'),
             'note': '只取给定存在见证，不构造同时选择全族成员的选择函数；不假设实数完备性或实数算术。'}],
        'revisit_links': [{'from': 'number-construction-revisit', 'to': 'number-systems',
                           'kind': 'later_revisit_not_prerequisite',
                           'note': '后续研究形式构造与已采用规则的关系，不反向用同一构造结论证明自身。'}],
        'chapter_dependencies': [{
            'code': r['code'], 'number': r['number'],
            'status': 'defined_entry_only' if r['code']=='00Axx' else 'pending',
            'module_candidates': [m['id'] for m in modules if r['code'][:2] in m['msc_tags']],
            'required_chapter_codes': [], 'required_section_anchors': [],
            'scope_note': ('无前文章节先修；运算规则明示采用' if r['code']=='00Axx' else
                           '模块候选仅供定位，开写前必须逐目标确定先修，不能按分类标签自动加依赖边'),
        } for r in chapters],
        'unplanned_boundaries': ['其余专业支线和应用模块待逐章规划',
             '概率模块的测度论先修取决于具体教学目标，未默认有限概率依赖完整测度论',
             '深造模块内部的精确节与命题先修尚待正文规划',
             '01数学史、97数学教育和通用文献条目可穿插，不是所有数学主题的强制前置'],
        'checks': {'module_dag_acyclic': True, 'unknown_module_ids': [],
                   'b1_has_no_b3_prerequisite': True, 'chapter_records': len(chapters)},
    }



# Registered source anchors are factual navigation, not independent proof approval.
UNIT_SPECS = [
    {'code': 'B1.1', 'number': 1, 'title': '自然数、后继与加法',
     'body': BRIDGE[0], 'answers': BRIDGE[1], 'anchor': 'b1-natural-numbers',
     'module_ids': ['natural'],
     'goals': ['说明零与后继的采用规则', '区分归纳法与有限次检查',
               '从递归定义计算简单自然数和', '逐步说明自然数加法交换律与结合律的证明'],
     'prerequisites': [(CH01[0], 'sec-00A05'), (CH01[0], 'sec-00A06')],
     'adopted': [('b1-peano-rules', '佩亚诺规则P1—P5与相等关系的通常规则'),
                 ('b1-recursion-principle', '自然数递归定义原则及其存在唯一性')],
     'definitions': ['b1-addition-definition'],
     'proved': [('N1','b1-add-one','加一就是取后继'),
                ('N2','b1-zero-left','零在左侧不改变自然数'),
                ('N3','b1-successor-left','左加数的后继公式'),
                ('N4','b1-addition-commutative','自然数加法交换律'),
                ('N5','b1-addition-associative','自然数加法结合律')],
     'questions': 'b1-q', 'answer_prefix': 'b1-a',
     'not_covered': ['自然数的集合论构造与递归原则的基础证明',
                     '自然数序与带余除法的系统教学', '初等数论各原分类节的完整教学']},
    {'code': 'B1.2', 'number': 2, 'title': '乘法与十进制位值',
     'body': BRIDGE[2], 'answers': BRIDGE[3], 'anchor': 'b1-place-value',
     'module_ids': ['place-value'],
     'goals': ['区分数字符号、自然数与数的写法', '按递归规则逐步计算乘积',
               '用已证运算律解释一组十与十个一的交换', '说明进位加法中每次改写的依据'],
     'prerequisites': [(BRIDGE[0], a) for a in ['b1-peano-rules','b1-induction',
          'b1-recursion-principle','b1-addition-definition','b1-addition-commutative',
          'b1-addition-associative','b1-add-one']],
     'adopted_external': [(BRIDGE[0],'b1-peano-rules','自然数规则、归纳与相等规则'),
                          (BRIDGE[0],'b1-recursion-principle','乘法与幂定义所采用的递归原则')],
     'definitions': ['b1-multiplication-definition','b1-place-definition'],
     'proved': [('B1.2.1','b1-multiplication-units','乘法中零与一的作用'),
                ('B1.2.2','b1-right-distributivity','乘法对左侧和的分配律'),
                ('B1.2.3','b1-multiplication-commutative','自然数乘法交换律'),
                ('B1.2.4','b1-multiplication-commutative','乘法对右侧和的分配律'),
                ('B1.2.5','b1-multiplication-associative','自然数乘法结合律'),
                ('B1.2.6','b1-place-examples','一次进位归并保持值')],
     'questions': 'b1-pv-q', 'answer_prefix': 'b1-pv-a',
     'not_covered': ['自然数序、消去律与带余除法的系统教学',
                    '标准十进制表示的普遍存在性和唯一性', '重复归并及书面算法的终止证明']},
]



UNIT_SPECS += [
    {'code':'B1.3','number':3,'title':'自然数的序与归纳工具',
     'body':BRIDGE[4], 'answers':BRIDGE[5], 'anchor':'ord-natural-order',
     'module_ids':['natural-order'],
     'goals':['从加法定义大小关系并证明三歧性','核查加乘保序的条件',
              '从普通归纳证明强归纳','证明严格递降过程的步数界'],
     'prerequisites':[(BRIDGE[0],a) for a in ['b1-peano-rules','b1-induction','b1-recursion-principle',
                        'b1-addition-definition','b1-addition-commutative','b1-addition-associative']]
                     +[(BRIDGE[2],a) for a in ['b1-multiplication-definition','b1-right-distributivity']],
     'adopted_external':[(BRIDGE[0],'b1-peano-rules','自然数与相等规则'),
                         (BRIDGE[0],'b1-recursion-principle','自然数递归原则')],
     'definitions':['ord-definition'],
     'proved':[(a,b,c) for a,b,c in [
         ('O1','ord-predecessor','零或唯一后继'),('O2','ord-zero-sum','零和的条件'),
         ('O3','ord-cancellation','加法消去律'),('O4','ord-partial-order','非严格序性质'),
         ('O5','ord-strict-equivalence','严格序与非严格序'),('O6','ord-successor-comparison','后继比较'),
         ('O7','ord-trichotomy','三歧性'),('O8','ord-addition-order','加法保序与反映'),
         ('O9','ord-multiplication-order','乘法保序与正因子条件'),
         ('O10','ord-strong-induction','强归纳'),('O11','ord-descent','严格下降的步数界')]],
     'questions':'ord-q','answer_prefix':'ord-a',
     'not_covered':['整数序、实数序和序数理论','一般无限结构的良基关系']},
    {'code':'B1.4','number':4,'title':'带余除法',
     'body':BRIDGE[6], 'answers':BRIDGE[7], 'anchor':'div-unit',
     'module_ids':['division'],
     'goals':['明确正除数及余数范围','逐步证明商余存在与唯一',
              '执行后继更新算法并验证不变式和终止','辨别带余除法与分数除法'],
     'prerequisites':[(BRIDGE[4],a) for a in ['ord-definition','ord-cancellation','ord-trichotomy',
          'ord-successor-comparison','ord-addition-order','ord-multiplication-order']]
          +[(BRIDGE[2],'b1-right-distributivity')],
     'adopted_external':[(BRIDGE[0],'b1-peano-rules','自然数与归纳规则')],
     'definitions':['div-quotient-remainder'],
     'proved':[('D-exists','div-existence','正除数商余存在性'),
               ('D-unique','div-uniqueness','商余唯一性'),
               ('D-update','div-successor-update','后继状态更新'),
               ('D-algorithm','div-algorithm','循环不变式与有限步执行')],
     'questions':'div-q','answer_prefix':'div-a',
     'not_covered':['负整数带余除法','欧几里得算法与最大公因数','分数的完整构造']},
    {'code':'B1.5','number':5,'title':'位值表示为何存在、为何唯一',
     'body':BRIDGE[8], 'answers':BRIDGE[9], 'anchor':'pos-unit',
     'module_ids':['positional'],
     'goals':['定义合法数字与无前导零的规范表','证明任意底数至少为二时表示存在唯一',
              '证明反复取商算法终止且正确','用系数和下降证明任意合法进位终止'],
     'prerequisites':[(BRIDGE[4],a) for a in ['ord-definition','ord-addition-order',
          'ord-multiplication-order','ord-strong-induction','ord-descent']]
          +[(BRIDGE[6],a) for a in ['div-theorem','div-uniqueness','div-algorithm']]
          +[(BRIDGE[2],'b1-multiplication-associative')],
     'adopted_external':[(BRIDGE[0],'b1-recursion-principle','有限递归定义原则')],
     'definitions':['pos-base-digits'],
     'proved':[('P1','pos-value-lemmas','位值有限和展开'),('P2','pos-value-lemmas','非零最高位给出正值'),
               ('P3','pos-quotient-descent','底数至少为二时正输入的商严格变小'),
               ('P4','pos-existence','规范表示存在性'),('P5','pos-uniqueness','规范表示唯一性'),
               ('P-extract','pos-extraction-algorithm','反复取商的正确性与终止'),
               ('P6','pos-carry-termination','任意合法进位的值保持与终止')],
     'questions':'pos-q','answer_prefix':'pos-a',
     'not_covered':['负数及分数位值表示','高效长除法与复杂性分析','无限小数展开理论']},
]


UNIT_SPECS += [
    {'code':'B1.6','number':6,'title':'自然数减法与逐位加减',
     'body':BRIDGE[10], 'answers':BRIDGE[11], 'anchor':'sub-unit',
     'module_ids':['written-arithmetic'],
     'goals':['以存在唯一的加法解定义有条件的差','核对差的恒等式与适用条件',
              '证明有限低位界及逐位加法不变式','证明逐位借位正确、有限并能检测范围'],
     'prerequisites':[(BRIDGE[0],a) for a in ['b1-addition-definition','b1-addition-associative']]
          +[(BRIDGE[2], 'b1-multiplication-definition')]
          +[(BRIDGE[4],a) for a in ['ord-definition','ord-cancellation','ord-strict-equivalence',
                       'ord-successor-comparison','ord-addition-order','ord-multiplication-order','ord-descent']]
          +[(BRIDGE[6],a) for a in ['div-theorem','div-algorithm']]
          +[(BRIDGE[8],a) for a in ['pos-value-lemmas','pos-uniqueness','pos-carry-termination']],
     'adopted_external':[(BRIDGE[0],'b1-peano-rules','自然数与归纳规则'),
                         (BRIDGE[0],'b1-recursion-principle','固定状态更新的递归原则')],
     'definitions':['sub-definition','sub-place-bound'],
     'proved':[('S1','sub-definition','差的存在唯一与定义条件'),
               ('S2','sub-identities','带条件的差的恒等式'),
               ('S3','sub-place-bound','有限低位和的严格界'),
               ('S-add','sub-addition-algorithm','逐位加法正确性与有限性'),
               ('S-borrow','sub-borrow-algorithm','逐位借位正确性、范围检测与有限性')],
     'questions':'sub-q','answer_prefix':'sub-a',
     'not_covered':['整数与负数的构造','长乘法与长除法','高效运算的复杂性界','浮点误差理论']},
]


UNIT_SPECS += [
    {'code':'B1.7','number':7,'title':'整数的表示、加法与次序',
     'body':BRIDGE[12], 'answers':BRIDGE[13], 'anchor':'int-unit',
     'module_ids':['integer-addition-order'],
     'goals':['从自然数对定义并证明等价关系及类相等判定',
              '证明自然嵌入、取负和加法不依赖代表及加法律',
              '证明唯一规范正负形式与全序、平移保序',
              '定义整数差并核对自然数差的兼容条件'],
     'prerequisites':[(BRIDGE[0],a) for a in ['b1-addition-definition','b1-addition-commutative','b1-addition-associative']]
          +[(BRIDGE[4],a) for a in ['ord-cancellation','ord-definition','ord-trichotomy','ord-addition-order']]
          +[(BRIDGE[10],a) for a in ['sub-definition','sub-identities']],
     'adopted':[('int-pairs','朴素集合形成：自然数对集合、子集合与类的集合；未从公理集合论重建')],
     'adopted_external':[(BRIDGE[0],'b1-peano-rules','前置自然数与相等规则')],
     'definitions':['int-pairs','int-classes','int-embedding','int-opposite','int-addition','int-order','int-subtraction'],
     'proved':[('I1','int-equivalence','自然数对等价关系'),
               ('I2','int-classes','类相等与代表等价的对应'),
               ('I3','int-embedding','自然数嵌入单射及零代表'),
               ('I4','int-opposite','相反数代表无关与双重取负'),
               ('I5','int-addition','加法代表无关'),
               ('I6','int-addition-laws','加法律、逆元唯一性与消去'),
               ('I7','int-normal-form','唯一正负规范形式'),
               ('I8','int-order','序代表无关及自然数见证'),
               ('I9','int-order-laws','全序、平移与取负反序'),
               ('I10','int-subtraction','整数差与自然差兼容')],
     'questions':'int-q','answer_prefix':'int-a',
     'not_covered':['公理集合论内的整数构造','整数乘法（接续单元B1.8）','整数除法与有理数构造']},
    {'code':'B1.8','number':8,'title':'整数乘法与符号规则',
     'body':BRIDGE[14], 'answers':BRIDGE[15], 'anchor':'imul-unit',
     'module_ids':['integer-multiplication'],
     'goals':['仅用自然数规则证明乘法代表无关',
              '逐步证明整数乘法交换、结合、分配及零一性质',
              '由运算律证明符号规则、零积与非零因子消去',
              '核对正乘保序、负乘反序及零因子的边界'],
     'prerequisites':[(BRIDGE[2],a) for a in ['b1-multiplication-units','b1-right-distributivity',
                    'b1-multiplication-commutative','b1-multiplication-associative']]
          +[(BRIDGE[4],'ord-multiplication-order')]
          +[(BRIDGE[12],a) for a in ['int-pairs','int-equivalence','int-classes','int-embedding',
                       'int-opposite','int-addition','int-addition-laws','int-normal-form','int-order','int-order-laws','int-subtraction']],
     'adopted_external':[(BRIDGE[12],'int-pairs','朴素集合形成背景'),
                         (BRIDGE[0],'b1-peano-rules','前置自然数与相等规则')],
     'definitions':['imul-notation','imul-well-defined'],
     'proved':[('M1','imul-well-defined','乘法不依赖代表选择'),
               ('M2','imul-basic-laws','零一、自然嵌入与交换律'),
               ('M3','imul-associative','乘法结合律'),
               ('M4','imul-distributive','分配律'),
               ('M5','imul-sign-rules','负号与乘法恒等式'),
               ('M6','imul-sign-classification','乘积符号分类'),
               ('M7','imul-zero-product','零积条件'),
               ('M8','imul-cancellation','非零因子消去'),
               ('M9','imul-order','乘法与次序')],
     'questions':'imul-q','answer_prefix':'imul-a',
     'not_covered':['整数幂与除法','有理数构造','浮点误差与复杂性理论']},
]


UNIT_SPECS += [
    {'code':'B1.9','number':9,'title':'整数带余除法',
     'body':BRIDGE[16], 'answers':BRIDGE[17], 'anchor':'idiv-unit',
     'module_ids':['integer-division'],
     'goals':['定义唯一非负幅值并核对零和取反','分零余数与正余数构造负被除数的商余',
              '对任意整数商证明正除数唯一性','证明负除数扩展并区分余数约定'],
     'prerequisites':[(BRIDGE[6],a) for a in ['div-theorem','div-algorithm']]
          +[(BRIDGE[10],'sub-definition')]
          +[(BRIDGE[12],a) for a in ['int-embedding','int-normal-form','int-addition-laws','int-order','int-order-laws','int-subtraction']]
          +[(BRIDGE[14],a) for a in ['imul-basic-laws','imul-distributive','imul-sign-rules','imul-order']],
     'adopted_external':[(BRIDGE[0],'b1-peano-rules','前置自然数规则'),(BRIDGE[12],'int-pairs','朴素集合背景')],
     'definitions':['idiv-absolute','idiv-conventions'],
     'proved':[('D1','idiv-absolute','绝对值存在唯一与基本性质'),('D2','idiv-existence','正除数整数商余存在'),
               ('D3a','idiv-uniqueness','整数严格比较的一个单位界'),('D3','idiv-uniqueness','正除数商余唯一'),
               ('D4','idiv-negative-divisor','非零整数除数的统一带余分解'),('D-alg','idiv-algorithm','分支算法正确性与有限性')],
     'questions':'idiv-q','answer_prefix':'idiv-a',
     'not_covered':['分数除法与有理数构造','高效长除法与复杂度界','整除及最大公因数（后续单元）']},
    {'code':'B1.10','number':10,'title':'整除：用整数倍数建立一种关系',
     'body':BRIDGE[18], 'answers':BRIDGE[19], 'anchor':'dvs-unit',
     'module_ids':['divisibility'],
     'goals':['用存在整数见证定义整除并区别除法','证明传递、线性组合及符号规律',
              '处理零与单位、绝对值界、互相整除','将正除数的整除判据与零余数连接并核对符号变化'],
     'prerequisites':[(BRIDGE[12],a) for a in ['int-embedding','int-addition-laws','int-normal-form','int-order','int-order-laws','int-subtraction']]
          +[(BRIDGE[14],a) for a in ['imul-basic-laws','imul-associative','imul-distributive','imul-sign-rules','imul-sign-classification','imul-zero-product','imul-cancellation','imul-order']]
          +[(BRIDGE[16],a) for a in ['idiv-absolute','idiv-existence','idiv-uniqueness']]
          +[(BRIDGE[4],'ord-successor-comparison')],
     'adopted_external':[(BRIDGE[12],'int-pairs','前置整数构造的朴素集合背景')],
     'definitions':['dvs-definition','dvs-units'],
     'proved':[('V1','dvs-definition','整除见证的非零唯一性与零例外'),('V2','dvs-laws','整除与线性组合规律'),
               ('V3','dvs-zero','零的整除判据'),('V4','dvs-magnitude','正整数至少为一及幅值乘法'),
               ('V5','dvs-units','整数单位恰为正负一'),('V6','dvs-bound','非零被整除数的因子幅值界'),
               ('V7','dvs-associates','互相整除与相伴、非负唯一性'),('V8','dvs-remainder','正除数整除当且仅当余数零')],
     'questions':'dvs-q','answer_prefix':'dvs-a',
     'not_covered':['素数与唯一分解','一般环的整除理论','最大公因数（接续单元）']},
    {'code':'B1.11','number':11,'title':'公因数、最大公因数与欧几里得算法',
     'body':BRIDGE[20], 'answers':BRIDGE[21], 'anchor':'gcd-unit',
     'module_ids':['gcd-euclidean'],
     'goals':['以非负规范及公因数整除性质统一定义gcd','准确解释双零与通常数值最大的区别',
              '证明公因数保持、严格下降与每轮有限','证明任意整数对gcd存在唯一并完整执行算法'],
     'prerequisites':[(BRIDGE[12],'int-subtraction'),(BRIDGE[14],'imul-distributive')]
          +[(BRIDGE[16],a) for a in ['idiv-absolute','idiv-existence']]
          +[(BRIDGE[18],a) for a in ['dvs-definition','dvs-laws','dvs-zero','dvs-bound','dvs-associates','dvs-units']]
          +[(BRIDGE[4],'ord-descent'),(BRIDGE[6],'div-algorithm')],
     'adopted_external':[(BRIDGE[0],'b1-peano-rules','前置自然数与归纳规则')],
     'definitions':['gcd-definition','gcd-properties'],
     'proved':[('G1','gcd-uniqueness','非负规范候选唯一'),('G2','gcd-terminal','零输入与终点候选'),
               ('G3','gcd-invariant','一次替换保持全部公因数'),('G4','gcd-algorithm','算法有限停止'),
               ('G5','gcd-algorithm','算法输出满足定义与存在性'),('G6','gcd-properties','全部公因数与数值最大'),
               ('G7','gcd-properties','交换、变号与同数输入')],
     'questions':'gcd-q','answer_prefix':'gcd-a',
     'not_covered':['贝祖等式与扩展欧几里得算法','素数与唯一分解','同余与分数约分','高效算法的复杂度界']},
]


UNIT_SPECS += [
    {'code':'B1.12','number':12,'title':'贝祖等式与扩展欧几里得算法',
     'body':BRIDGE[22], 'answers':BRIDGE[23], 'anchor':'bez-unit',
     'module_ids':['bezout'],
     'goals':['定义整数线性组合并用有符号原输入初始化系数',
              '证明同时更新的系数不变式、有限停止及全整数贝祖等式',
              '区分最大公因数唯一性与系数不唯一性',
              '证明全部线性组合的整除刻画与整数方程可解判据，包含双零'],
     'prerequisites':[(BRIDGE[12],a) for a in ['int-addition-laws','int-subtraction']]
          +[(BRIDGE[14],a) for a in ['imul-basic-laws','imul-associative','imul-distributive','imul-sign-rules']]
          +[(BRIDGE[16],'idiv-absolute')]
          +[(BRIDGE[18],a) for a in ['dvs-definition','dvs-laws','dvs-zero','dvs-remainder']]
          +[(BRIDGE[20],a) for a in ['gcd-definition','gcd-uniqueness','gcd-algorithm']],
     'adopted_external':[(BRIDGE[0],'b1-peano-rules','前置自然数与归纳规则'),
                         (BRIDGE[12],'int-pairs','前置整数构造的朴素集合背景')],
     'definitions':['bez-linear-combinations','bez-initialization'],
     'proved':[('BZ1','bez-invariant','余数系数的同时更新保持线性组合不变式'),
               ('BZ2','bez-theorem','任意整数输入的贝祖等式与算法终止'),
               ('BZ3','bez-coefficients','保持线性组合值的一族系数变换'),
               ('BZ4','bez-all-combinations','全部整数线性组合恰为最大公因数的整数倍'),
               ('BZ5','bez-equations','整数线性方程可解判据及一组解的构造')],
     'questions':'bez-q','answer_prefix':'bez-a',
     'not_covered':['整数线性方程全部解的参数理论','非负或有界整数解的额外条件',
                    '素数理论、同余与有理数构造','扩展算法的复杂度界']},
    {'code':'B1.13','number':13,'title':'互素、整除消去与整数对的规范记录',
     'body':BRIDGE[24], 'answers':BRIDGE[25], 'anchor':'cop-unit',
     'module_ids':['coprimality'],
     'goals':['说明互素定义C1及零、负号的边界',
              '证明互素的贝祖判据、整除消去及乘积判据',
              '提取正最大公因数并证明剩余整数对唯一、互素且第二分量正',
              '由交叉乘积证明互素正第二分量记录唯一，核对零与规范条件'],
     'prerequisites':[(BRIDGE[12],a) for a in ['int-addition-laws','int-order-laws']]
          +[(BRIDGE[14],a) for a in ['imul-basic-laws','imul-associative','imul-distributive',
                       'imul-sign-classification','imul-zero-product','imul-cancellation','imul-order']]
          +[(BRIDGE[16],'idiv-absolute')]
          +[(BRIDGE[18],a) for a in ['dvs-definition','dvs-laws','dvs-zero','dvs-units','dvs-bound','dvs-associates']]
          +[(BRIDGE[20],a) for a in ['gcd-definition','gcd-algorithm','gcd-terminal','gcd-properties']]
          +[(BRIDGE[22],'bez-theorem')],
     'adopted_external':[(BRIDGE[0],'b1-peano-rules','前置自然数与归纳规则'),
                         (BRIDGE[12],'int-pairs','前置整数构造的朴素集合背景')],
     # C1 is a definition in the manuscript, not a proved proposition.
     'definitions':['cop-definition','cop-record-uniqueness'],
     'proved':[('C2','cop-bezout','互素当且仅当存在等于一的整数线性组合'),
               ('C3','cop-cancellation','互素条件下的整除消去'),
               ('C4','cop-product','与乘积互素的逐因子判据'),
               ('C5','cop-reduction','提取正最大公因数后的唯一互素整数对'),
               ('C6','cop-record-uniqueness','交叉乘积相等的规范记录唯一性')],
     'questions':'cop-q','answer_prefix':'cop-a',
     'not_covered':['有理数等价类构造及其运算良定义','有理数序与分数四则运算',
                    '素数、素因数分解及唯一分解','有理数与实数的完整桥接']},
]


UNIT_SPECS += [
    {'code':'B1.14','number':14,'title':'有理数：从整数记录到唯一规范代表',
     'body':BRIDGE[26], 'answers':BRIDGE[27], 'anchor':'rat-unit',
     'module_ids':['rational-construction'],
     'goals':['在正分母整数对上证明交叉乘积关系为等价关系',
              '定义有理数等价类及分数记号并证明类相等判据',
              '证明整数嵌入单射、零判据及唯一正分母互素代表',
              '明确负分母扩展记号与零分母排除，不预先使用有理数运算'],
     'prerequisites':[(BRIDGE[12],a) for a in ['int-pairs','int-classes','int-addition-laws','int-order-laws']]
          +[(BRIDGE[14],a) for a in ['imul-basic-laws','imul-associative','imul-sign-rules','imul-cancellation']]
          +[(BRIDGE[24],a) for a in ['cop-reduction','cop-record-uniqueness']],
     'adopted':[('rat-unit','朴素集合形成与外延性：指定的整数对、子集合及等价类的集合；未从集合论公理重建')],
     'adopted_external':[(BRIDGE[12],'int-pairs','前置整数构造的朴素集合背景')],
     'definitions':['rat-pairs','rat-equivalence','rat-classes','rat-notation','rat-integers',
                    'rat-normal-form','rat-signed-record'],
     'proved':[('R1','rat-equivalence','交叉乘积关系的自反、对称与传递'),
               ('R2','rat-classes','类相等当且仅当代表等价'),
               ('R3','rat-integers','整数嵌入单射'),
               ('R4','rat-zero','零类与分子为零的等价判据'),
               ('R5','rat-normal-form','每类唯一的正分母互素规范代表')],
     'questions':'rat-q','answer_prefix':'rat-a',
     'not_covered':['公理集合论层面的有理数存在性重建',
                    '有理数加法与相反数（接续单元）','有理数乘法、次序、倒数与除法']},
    {'code':'B1.15','number':15,'title':'有理数加法、相反数与减法',
     'body':BRIDGE[28], 'answers':BRIDGE[29], 'anchor':'radd-unit',
     'module_ids':['rational-arithmetic'],
     'goals':['证明加法输出合法且同时更换两个代表不改变结果类',
              '从整数分量逐步证明加零、交换、结合及相反数规律',
              '证明整数嵌入保持加法与相反数，以及逆元唯一和加法消去',
              '定义减法并证明加法方程存在唯一解，核对括号与零边界'],
     'prerequisites':[(BRIDGE[26],a) for a in ['rat-pairs','rat-equivalence','rat-classes','rat-notation',
                       'rat-integers','rat-zero','rat-normal-form']]
          +[(BRIDGE[12],'int-addition-laws')]
          +[(BRIDGE[14],a) for a in ['imul-basic-laws','imul-associative','imul-distributive',
                       'imul-sign-rules','imul-sign-classification']],
     'adopted_external':[(BRIDGE[26],'rat-unit','前置有理数等价类构造的朴素集合背景；不另加有理数运算公理')],
     'definitions':['radd-definition','radd-opposite','radd-subtraction'],
     'proved':[('RA1','radd-definition','加法输出的整数分量与正分母合法性'),
               ('RA2','radd-well-defined','加法同时更换两个代表后的结果无关性'),
               ('RA3','radd-laws','有理数加法零元、交换律与结合律'),
               ('RA4','radd-opposite','相反数代表无关及加法逆元性质'),
               ('RA5','radd-integers','整数嵌入保持加法与相反数'),
               ('RA6','radd-cancellation','相反数唯一、加法消去及和的相反数'),
               ('RA7','radd-subtraction','减法代表公式与加法方程唯一解')],
     'questions':'radd-q','answer_prefix':'radd-a',
     'not_covered':['有理数乘法及其代表无关性','乘法逆元与有理数除法',
                    '有理数次序与大小比较','实数构造与无限小数']},
]


UNIT_SPECS += [
    {'code':'B1.16','number':16,'title':'有理数乘法与非零因子的消去',
     'body':BRIDGE[30], 'answers':BRIDGE[31], 'anchor':'rmul-unit',
     'module_ids':['rational-arithmetic'],
     'goals':['证明乘法输出合法且同时更换两输入代表不改变结果类',
              '从整数运算证明乘法零一、交换、结合与分配并核对整数嵌入兼容',
              '从加法相反数证明乘积负号规则',
              '从整数零积证明有理数零积与非零消去，不借倒数、除法或有理数序'],
     'prerequisites':[(BRIDGE[26],a) for a in ['rat-pairs','rat-classes','rat-integers','rat-zero','rat-normal-form']]
          +[(BRIDGE[28],a) for a in ['radd-definition','radd-laws','radd-opposite','radd-cancellation','radd-subtraction']]
          +[(BRIDGE[14],a) for a in ['imul-basic-laws','imul-associative','imul-distributive',
                       'imul-sign-rules','imul-sign-classification','imul-zero-product']],
     'adopted_external':[(BRIDGE[26],'rat-unit','前置有理数等价类的朴素集合背景；不另加有理数运算公理')],
     'definitions':['rmul-definition'],
     'proved':[('RM1','rmul-definition','乘法输出的整数分量与正分母合法性'),
               ('RM2','rmul-well-defined','同时更换两输入代表的乘积无关性'),
               ('RM3','rmul-laws','乘法零一、交换律与结合律'),
               ('RM4','rmul-distributive','乘法对加法的两侧分配律'),
               ('RM5','rmul-integers','整数嵌入保持乘法'),
               ('RM6','rmul-signs','乘积与相反数的符号规律'),
               ('RM7','rmul-zero-product','零乘积当且仅当至少一因子为零'),
               ('RM8','rmul-cancellation','非零共同因子的乘法消去')],
     'questions':'rmul-q','answer_prefix':'rmul-a',
     'not_covered':['非零有理数倒数与除法（接续单元）','有理数次序、绝对值与保序',
                    '运算复杂度与数值近似']},
    {'code':'B1.17','number':17,'title':'非零有理数的倒数与除法',
     'body':BRIDGE[32], 'answers':BRIDGE[33], 'anchor':'rdiv-unit',
     'module_ids':['rational-arithmetic'],
     'goals':['证明零没有乘法逆元，非零有理数恰有一个代表无关的倒数',
              '以整数分子符号构造合法倒数代表，不借有理数序',
              '定义非零除数的除法并完整分类乘法方程的全部解',
              '证明旧分数记号与除法一致，核对零、负号、同除数求和及约分条件'],
     'prerequisites':[(BRIDGE[26],a) for a in ['rat-pairs','rat-classes','rat-notation','rat-integers',
                       'rat-zero','rat-normal-form','rat-signed-record']]
          +[(BRIDGE[28],a) for a in ['radd-opposite','radd-integers']]
          +[(BRIDGE[30],a) for a in ['rmul-definition','rmul-laws','rmul-distributive',
                       'rmul-integers','rmul-signs','rmul-zero-product']]
          +[(BRIDGE[12],a) for a in ['int-order-laws','int-addition-laws']]
          +[(BRIDGE[14],a) for a in ['imul-basic-laws','imul-sign-rules','imul-sign-classification']],
     'adopted_external':[(BRIDGE[26],'rat-unit','前置有理数等价类的朴素集合背景；不采用有理数次序')],
     'definitions':['rdiv-nonzero','rdiv-reciprocal','rdiv-division'],
     'proved':[('RD1','rdiv-nonzero','非零类与非零分子判据及零无乘法逆元'),
               ('RD2','rdiv-inverse-unique','一旦存在则乘法逆元唯一'),
               ('RD3','rdiv-reciprocal','非零倒数构造、代表无关性与基本性质'),
               ('RD4','rdiv-division','非零除法与乘法方程全部解分类'),
               ('RD5','rdiv-notation','整数分数记号与新有理数除法一致'),
               ('RD6','rdiv-signs','非零除数条件下的零、负号及同除数求和'),
               ('RD7','rdiv-cancellation','约去共同非零因子的条件')],
     'questions':'rdiv-q','answer_prefix':'rdiv-a',
     'not_covered':['有理数次序、绝对值与大小比较','一般整数指数运算',
                    '实数构造与连续数量理论']},
]


UNIT_SPECS += [
    {'code':'B1.18','number':18,'title':'有理数的次序与乘除比较',
     'body':BRIDGE[34], 'answers':BRIDGE[35], 'anchor':'rord-unit',
     'module_ids':['rational-order'],
     'goals':['在整数层证明正分母交叉比较同时换代表不变',
              '证明全序、三歧性、整数嵌入保序与分子符号判据',
              '证明平移保持并反映比较及取反反序',
              '逐个区分正、负、零因子的乘法比较以及非零除数的除法比较'],
     'prerequisites':[(BRIDGE[12],'int-order-laws')]
          +[(BRIDGE[14],a) for a in ['imul-basic-laws','imul-associative','imul-distributive','imul-order']]
          +[(BRIDGE[26],a) for a in ['rat-pairs','rat-classes','rat-integers','rat-zero']]
          +[(BRIDGE[28],a) for a in ['radd-definition','radd-opposite']]
          +[(BRIDGE[30],a) for a in ['rmul-definition','rmul-laws','rmul-signs']]
          +[(BRIDGE[32],a) for a in ['rdiv-reciprocal','rdiv-division']],
     'adopted_external':[(BRIDGE[26],'rat-unit','前置有理数等价类的朴素集合背景；不采用实数或其完备性')],
     'definitions':['rord-definition','rord-sign'],
     'proved':[('RO0','rord-integer-reflection','正整数因子保持并反映整数比较'),
               ('RO1','rord-well-defined','两种交叉比较同时换代表无关'),
               ('RO2','rord-laws','全序、三歧性及严格与非严格比较的联系'),
               ('RO3','rord-integers','整数嵌入保持并反映次序'),
               ('RO4','rord-translation','同加一个有理数保持并反映比较'),
               ('RO5','rord-negation','取相反数反转次序'),
               ('RO6','rord-multiplication','按正负零因子分类的乘法比较'),
               ('RO7','rord-reciprocal','非零倒数与原数同号'),
               ('RO8','rord-division','按非零除数符号分类的除法比较')],
     'questions':'rord-q','answer_prefix':'rord-a',
     'not_covered':['绝对值与距离（接续单元）','实数构造与完备性','极限及连续性']},
    {'code':'B1.19','number':19,'title':'有理数绝对值与距离',
     'body':BRIDGE[36], 'answers':BRIDGE[37], 'anchor':'rabs-unit',
     'module_ids':['rational-order'],
     'goals':['按有理数次序定义绝对值并证明非负、零判据及相反数不变',
              '核对整数绝对值兼容、正分母代表公式及双向界刻画',
              '证明乘积与非零商公式、三角与反三角不等式',
              '在有理数范围定义距离并逐条证明非负、零判据、对称和三角性质'],
     'prerequisites':[(BRIDGE[16],'idiv-absolute')]
          +[(BRIDGE[26],a) for a in ['rat-classes','rat-integers']]
          +[(BRIDGE[28],a) for a in ['radd-laws','radd-opposite','radd-cancellation','radd-subtraction','radd-integers']]
          +[(BRIDGE[30],a) for a in ['rmul-laws','rmul-distributive','rmul-signs']]
          +[(BRIDGE[32],a) for a in ['rdiv-reciprocal','rdiv-division']]
          +[(BRIDGE[34],a) for a in ['rord-definition','rord-laws','rord-integers','rord-sign',
                       'rord-translation','rord-negation','rord-multiplication']],
     'adopted_external':[(BRIDGE[26],'rat-unit','前置有理数等价类的朴素集合背景；不采用实数完备性或尚未构造的实数嵌入')],
     'definitions':['rabs-definition','rabs-distance'],
     'proved':[('RAB1','rabs-properties','绝对值的基本性质与唯一非负大小'),
               ('RAB2','rabs-integers','整数绝对值兼容与代表公式'),
               ('RAB3','rabs-bounds','绝对值的双向界与区间刻画'),
               ('RAB4','rabs-products','乘积与非零商的绝对值'),
               ('RAB5','rabs-triangle','三角不等式'),
               ('RAB6','rabs-reverse-triangle','反三角不等式'),
               ('RAB7','rabs-distance','有理数值距离的四条性质')],
     'questions':'rabs-q','answer_prefix':'rabs-a',
     'not_covered':['实数构造与完备性','一般度量空间理论','极限、连续性与近似误差理论']},
]


UNIT_SPECS += [
    {'code':'B1.20','number':20,'title':'比、比例与按比分配',
     'body':BRIDGE[38], 'answers':BRIDGE[39], 'anchor':'ratio-unit',
     'parent_code':'97Fxx','parent_chapter_number':526,'part_code':'97-XX',
     'msc_leaf_codes':['97F80'],'module_ids':['relations-units'],
     'goals':['以非零后项的有理商定义比并证明比例的交叉乘积双向判据',
              '证明同时非零倍率与相同比中的唯一共同倍率',
              '在正总量及合法非负比例条件下证明按比分配的存在唯一性',
              '区分两部分之比、部分占整体的比及多组记录共同倍率的模型要求'],
     'prerequisites':[(BRIDGE[26],a) for a in ['rat-integers','rat-normal-form']]
          +[(BRIDGE[28],a) for a in ['radd-laws','radd-subtraction']]
          +[(BRIDGE[30],a) for a in ['rmul-laws','rmul-distributive','rmul-zero-product','rmul-cancellation']]
          +[(BRIDGE[32],a) for a in ['rdiv-division','rdiv-notation','rdiv-cancellation']]
          +[(BRIDGE[34],a) for a in ['rord-laws','rord-translation','rord-multiplication','rord-division']],
     'adopted_external':[(BRIDGE[26],'rat-unit','前置有理数等价类背景；具体分配条件为模型假设，不是普遍自然定律')],
     'definitions':['ratio-definition','ratio-proportion','ratio-models'],
     'proved':[('RP1','ratio-proportion','两分母非零条件下比例与交叉乘积等价'),
               ('RP2','ratio-scaling','共同非零倍率及相同比的唯一倍率'),
               ('RP3','ratio-allocation','正总量与合法非负比例的分配存在唯一'),
               ('RP4','ratio-part-whole','部分对部分与部分对整体的关系')],
     'questions':'ratio-q','answer_prefix':'ratio-a',
     'not_covered':['百分数系统理论','函数与正反比例函数','实数模型及一般比例教学研究']},
    {'code':'B1.21','number':21,'title':'量、单位与换算',
     'body':BRIDGE[40], 'answers':BRIDGE[41], 'anchor':'qty-unit',
     'parent_code':'97Fxx','parent_chapter_number':526,'part_code':'97-XX',
     'msc_leaf_codes':['97F70'],'module_ids':['relations-units'],
     'goals':['明确量类别、参考单位、数值与带单位记录的有理数模型约定',
              '证明正单位倍率下换算唯一并保持往返、复合及相加一致',
              '证明同类量比不随共同单位改变而改变',
              '按长度与时间两种倍率证明平均速率单位换算并区分模型量与实际测量'],
     'prerequisites':[(BRIDGE[26],a) for a in ['rat-notation','rat-normal-form']]
          +[(BRIDGE[28],'radd-laws')]
          +[(BRIDGE[30],a) for a in ['rmul-laws','rmul-distributive','rmul-cancellation']]
          +[(BRIDGE[32],a) for a in ['rdiv-reciprocal','rdiv-division','rdiv-cancellation']]
          +[(BRIDGE[34],a) for a in ['rord-laws','rord-multiplication','rord-reciprocal']],
     'adopted':[('qty-model','同类别有理量记录、正单位倍率及同类量加法的模型约定'),
                ('qty-si','本批采用的精确长度与时间单位关系；不是纯代数推出的物理标准')],
     'definitions':['qty-model','qty-ratio','qty-rate'],
     'proved':[('QU1','qty-conversion','正倍率单位换算数值的存在唯一性'),
               ('QU2','qty-consistency','往返、复合与相加的一致性'),
               ('QU3','qty-ratio','同类量比的单位无关性'),
               ('QU4','qty-rate','长度与时间单位变化时平均速率数值的倍率')],
     'questions':'qty-q','answer_prefix':'qty-a',
     'not_covered':['偏移温标换算','测量误差与不确定度理论','最新SI精密定义与完整计量学',
                    '实数值量、连续运动及一般量纲理论']},
]


UNIT_SPECS += [
    {'code':'B2.1','number':22,'title':'集合、对应与函数',
     'body':BRIDGE[42], 'answers':BRIDGE[43], 'anchor':'fun-unit',
     'parent_code':'97Ixx','parent_chapter_number':529,'part_code':'97-XX',
     'msc_leaf_codes':['97I20'],'msc_cross_reference_codes':['03E20','97E60'],
     'module_ids':['functions'],
     'goals':['说明集合元素、子集、空集、有序对及笛卡尔积的入口语言与采用边界',
              '逐项检验每个输入有且只有一个输出，并明确函数的定义域、目标与图三数据',
              '区分固定目标下空函数唯一与非空定义域到空目标不存在',
              '定义像并区别实际输出集合与目标集合，核查公式与有限值表的表达范围'],
     'prerequisites':[(BRIDGE[12],'int-pairs')]
          +[(BRIDGE[26],a) for a in ['rat-classes','rat-integers']]
          +[(BRIDGE[28],a) for a in ['radd-laws','radd-subtraction']]
          +[(BRIDGE[30],'rmul-laws')]
          +[(BRIDGE[32],'rdiv-division')],
     'adopted':[('fun-unit','公开采用的朴素集合、有限集合与已建数集、有序对集合、条件子集及三项记录背景'),
                ('fun-definition','定义域、目标集合与图共同组成函数数据的约定')],
     'definitions':['fun-sets','fun-pairs','fun-correspondence','fun-definition','fun-image'],
     'proved':[('F1','fun-correspondence','每输入恰一输出的存在条件与唯一条件'),
               ('F2','fun-empty','固定目标的空函数唯一及非空域到空目标不存在'),
               ('F3','fun-image','像包含于目标集合、成员判据及空像与空定义域等价')],
     'questions':'fun-q','answer_prefix':'fun-a',
     'not_covered':['函数相等、限制与复合（接续单元）','单射、满射、双射及反函数',
                    '实数、连续曲线与极限','公理集合论中有序对和集合形成的完整构造']},
    {'code':'B2.2','number':23,'title':'函数相等、限制与复合',
     'body':BRIDGE[44], 'answers':BRIDGE[45], 'anchor':'funcomp-unit',
     'parent_code':'97Ixx','parent_chapter_number':529,'part_code':'97-XX',
     'msc_leaf_codes':['97I20'],'msc_cross_reference_codes':['03E20','97E60'],
     'module_ids':['functions'],
     'goals':['在相同定义域与目标集合下证明函数相等的逐点判据',
              '定义保留目标集合的定义域限制并证明嵌套相容',
              '以严格匹配中间集合的图定义复合并证明每输入唯一输出',
              '证明恒等、双单位律、结合律与限制复合相容，核查空集及目标不同的边界'],
     'prerequisites':[(BRIDGE[42],a) for a in ['fun-sets','fun-pairs','fun-definition','fun-empty','fun-image']]
          +[(BRIDGE[28],'radd-laws')]
          +[(BRIDGE[30],a) for a in ['rmul-laws','rmul-distributive']]
          +[(BRIDGE[32],'rdiv-division')]
          +[(BRIDGE[40],a) for a in ['qty-conversion','qty-consistency']],
     'adopted_external':[(BRIDGE[42],'fun-unit','前置朴素集合形成背景'),
                         (BRIDGE[42],'fun-definition','前置函数三数据约定；目标集合不由图恢复')],
     'definitions':['fc-equality','fc-restriction','fc-composition','fc-identity'],
     'proved':[('FC1','fc-equality','函数三数据相等及同域同目标下的逐点判据'),
               ('FC2','fc-restriction','保目标限制的合法性与嵌套相容'),
               ('FC3','fc-composition','严格类型复合图的存在唯一性'),
               ('FC4','fc-identity','恒等函数与左右单位律及限制恒等的类型边界'),
               ('FC5','fc-associativity','严格类型复合的结合律'),
               ('FC6','fc-restriction-composition','限制与复合的相容性')],
     'questions':'funcomp-q','answer_prefix':'funcomp-a',
     'not_covered':['任意改变目标集合与宽松复合的扩展约定','单射、满射、双射及反函数',
                    '实函数、连续性与极限','函数空间或范畴论的完整体系']},
]


UNIT_SPECS += [
    {'code':'B2.3','number':24,'title':'单射、满射与双射',
     'body':BRIDGE[46], 'answers':BRIDGE[47], 'anchor':'bij-unit',
     'parent_code':'97Ixx','parent_chapter_number':529,'part_code':'97-XX',
     'msc_leaf_codes':['97I20'],'msc_cross_reference_codes':['03E20','97E60'],
     'module_ids':['functions'],
     'goals':['以完整量词定义单射、满射、双射，并给出否定性质的具体见证',
              '证明满射的像判据、双射的唯一原像判据与空集恒等边界',
              '证明改目标为像的合法性及其单满射性质，核查三数据相等条件',
              '证明复合保性与正确的因子推论，以反例说明不可交换或逆推的方向'],
     'prerequisites':[(BRIDGE[42],a) for a in ['fun-sets','fun-definition','fun-empty','fun-image']]
          +[(BRIDGE[44],a) for a in ['fc-equality','fc-restriction','fc-composition','fc-identity']]
          +[(BRIDGE[28],a) for a in ['radd-cancellation','radd-subtraction']]
          +[(BRIDGE[30],'rmul-cancellation')]+[(BRIDGE[32],'rdiv-division')],
     'adopted_external':[(BRIDGE[42],'fun-unit','前置朴素集合与按条件形成子集的背景'),
                         (BRIDGE[42],'fun-definition','函数的定义域、目标与图三数据约定')],
     'definitions':['bij-injective','bij-surjective','bij-bijective'],
     'proved':[('BJ1','bij-surjective','满射当且仅当像等于目标集合'),
               ('BJ2','bij-bijective','双射当且仅当每个目标恰有一个原像'),
               ('BJ3','bij-empty','空函数单满射分类与恒等函数双射'),
               ('BJ4','bij-retarget','改目标为像的合法性、单满射性质及函数相等边界'),
               ('BJ5','bij-composition','严格类型复合保持单射满射及双射'),
               ('BJ6','bij-factors','复合单射推出前因子单射，复合满射推出后因子满射')],
     'questions':'bij-q','answer_prefix':'bij-a',
     'not_covered':['逆函数构造（接续单元）','基数与抽屉原理的系统教学',
                    '任意满射选择右逆的普遍原则','实数、连续图像与全部映射教育理论']},
    {'code':'B2.4','number':25,'title':'逆函数与原像',
     'body':BRIDGE[48], 'answers':BRIDGE[49], 'anchor':'inv-unit',
     'parent_code':'97Ixx','parent_chapter_number':529,'part_code':'97-XX',
     'msc_leaf_codes':['97I20'],'msc_cross_reference_codes':['03E20','97E60'],
     'module_ids':['functions'],
     'goals':['构造逆向图并证明它给出函数当且仅当原函数双射',
              '证明双侧逆的存在判据与唯一性，并检查单侧逆和空集边界',
              '核对类型并证明逆的逆、恒等的逆及复合逆的反序规律',
              '定义无需可逆性的集合原像，证明基本性质并与逆函数值和有理倒数区别'],
     'prerequisites':[(BRIDGE[42],a) for a in ['fun-sets','fun-pairs','fun-definition','fun-empty']]
          +[(BRIDGE[44],a) for a in ['fc-equality','fc-restriction','fc-composition','fc-identity','fc-associativity']]
          +[(BRIDGE[46],a) for a in ['bij-injective','bij-surjective','bij-bijective','bij-retarget']]
          +[(BRIDGE[28],'radd-laws')]
          +[(BRIDGE[30],a) for a in ['rmul-laws','rmul-distributive']]
          +[(BRIDGE[32],'rdiv-division')],
     'adopted_external':[(BRIDGE[42],'fun-unit','前置朴素集合与条件子集背景'),
                         (BRIDGE[42],'fun-definition','函数三数据约定'),
                         (BRIDGE[44],'fc-composition','复合要求中间目标与定义域完全一致')],
     'definitions':['inv-reverse-graph','inv-two-sided','inv-preimage'],
     'proved':[('INV1','inv-reverse-graph','逆向图为函数当且仅当原函数双射及求值等价式'),
               ('INV2','inv-two-sided','双射与存在双侧逆等价且双侧逆唯一'),
               ('INV3','inv-identities','逆函数双射、逆的逆与恒等逆及空集边界'),
               ('INV4','inv-composition','严格复合的逆函数按反序复合'),
               ('INV5','inv-preimage','原像的空集、全目标、单调与复合反序性质')],
     'questions':'inv-q','answer_prefix':'inv-a',
     'not_covered':['任意满射选择右逆的普遍原则与选择公理',
                    '实数上的连续反函数','完整函数空间理论与全部映射教育研究']},
]


UNIT_SPECS += [
    {'code':'B2.5','number':26,'title':'一元一次方程与等价变形',
     'body':BRIDGE[50], 'answers':BRIDGE[51], 'anchor':'lin-unit',
     'parent_code':'97Hxx','parent_chapter_number':528,'part_code':'97-XX',
     'msc_leaf_codes':['97H30'],'msc_cross_reference_codes':['97H20'],
     'module_ids':['functions'],
     'goals':['在共同允许范围内定义解集与等价方程，区别单向推论与双向等价',
              '证明同加及非零倍乘的可逆条件，分析乘零与除未知数的失效边界',
              '对一元一次方程及两边含未知数的形式穷尽参数零值和候选范围分支',
              '在原分母非零的范围内证明清分母等价并完整代回核验候选'],
     'prerequisites':[(BRIDGE[42],a) for a in ['fun-sets','fun-definition']]
          +[(BRIDGE[48],a) for a in ['inv-two-sided','inv-affine']]
          +[(BRIDGE[28],a) for a in ['radd-laws','radd-cancellation','radd-subtraction']]
          +[(BRIDGE[30],a) for a in ['rmul-laws','rmul-distributive','rmul-zero-product',
                                   'rmul-cancellation','rmul-signs']]
          +[(BRIDGE[32],'rdiv-division')],
     'adopted_external':[(BRIDGE[42],'fun-sets','沿用集合及条件子集背景'),
                         (BRIDGE[42],'fun-definition','两边在共同允许范围内取唯一有理值的函数约定')],
     'definitions':['lin-entry','lin-solutions','lin-equivalence','lin-affine'],
     'proved':[('LIN1','lin-addition','同加处处有定义的表达式保持解集'),
               ('LIN2','lin-multiplication','同乘处处非零的表达式保持解集'),
               ('LIN3','lin-affine','基本一次形式的全部参数及范围分支'),
               ('LIN4','lin-two-sides','两边含未知数时的可逆合并及全部分支'),
               ('LIN5','lin-denominators','原分母处处非零条件下的清分母等价')],
     'questions':'lin-q','answer_prefix':'lin-a',
     'not_covered':['二元一次方程组（接续单元）','一般多项式与高次方程理论',
                    '不等式系统、实数与坐标图像','完整代数教育研究']},
    {'code':'B2.6','number':27,'title':'二元一次方程组与可逆消元',
     'body':BRIDGE[52], 'answers':BRIDGE[53], 'anchor':'sys-unit',
     'parent_code':'97Hxx','parent_chapter_number':528,'part_code':'97-XX',
     'msc_leaf_codes':['97H30'],'msc_cross_reference_codes':['97H20','15A06'],
     'module_ids':['functions'],
     'goals':['把同时满足两式的解表示为有理有序对，并用双向包含判断系统等价',
              '证明交换、非零倍乘与保留另一式的倍加替换保持全部解集',
              '证明代入与消元的可逆性，区分消去未知数和丢弃约束',
              '对任意有理系数及全零行分支给出唯一解、无解或全部参数解并证明穷尽'],
     'prerequisites':[(BRIDGE[42],a) for a in ['fun-sets','fun-pairs']]
          +[(BRIDGE[26],'rat-integers')]+[(BRIDGE[28],'radd-laws')]
          +[(BRIDGE[30],a) for a in ['rmul-laws','rmul-distributive']]
          +[(BRIDGE[32],'rdiv-division')]
          +[(BRIDGE[50],a) for a in ['lin-solutions','lin-equivalence','lin-addition',
                                   'lin-multiplication','lin-affine']],
     'adopted_external':[(BRIDGE[42],'fun-sets','沿用集合及条件子集背景'),
                         (BRIDGE[42],'fun-pairs','沿用有序对判等和笛卡尔积，Q²不预设连续平面')],
     'definitions':['sys-solution','sys-classification'],
     'proved':[('SYS1','sys-row-operations','三类可逆方程操作保持全部解集'),
               ('SYS2','sys-substitution','非零首系数下代入参数形式与原解集双向对应'),
               ('SYS3','sys-classification','任意有理系数二元两式的完整分支与全部解分类')],
     'questions':'sys-q','answer_prefix':'sys-a',
     'not_covered':['一般矩阵、秩、行最简形与行列式理论','实数坐标图像与直线交点证明',
                    '一般多元线性代数的系统教学','完整代数教育研究']},
]


UNIT_SPECS += [
    {'code':'B2.7','number':28,'title':'一元一次不等式与有理区间',
     'body':BRIDGE[54], 'answers':BRIDGE[55], 'anchor':'ineq-unit',
     'parent_code':'97Hxx','parent_chapter_number':528,'part_code':'97-XX',
     'msc_leaf_codes':['97H30'],'msc_cross_reference_codes':['97H20'],
     'module_ids':['functions'],
     'goals':['在共同有理允许范围内定义不等式解集、等价、交并及区间端点',
              '由已证序律证明平移和正负乘除的双向条件，区别乘零与除零',
              '完整分类基本及双边一次不等式的正负零系数和严格非严格分支',
              '以交并表达同时满足或至少满足一个条件，并保留允许范围和分母符号'],
     'prerequisites':[(BRIDGE[42],a) for a in ['fun-sets','fun-definition']]
          +[(BRIDGE[50],a) for a in ['lin-entry','lin-solutions']]
          +[(BRIDGE[34],a) for a in ['rord-laws','rord-translation','rord-multiplication','rord-division']]
          +[(BRIDGE[28],a) for a in ['radd-laws','radd-subtraction']]
          +[(BRIDGE[30],a) for a in ['rmul-distributive','rmul-signs']]
          +[(BRIDGE[32],'rdiv-division')],
     'adopted_external':[(BRIDGE[42],'fun-sets','沿用从给定集合按条件取子集的背景'),
                         (BRIDGE[42],'fun-definition','比较前两边必须在同一允许范围内有唯一有理值')],
     'definitions':['ineq-solutions','ineq-set-operations','ineq-intervals','ineq-affine'],
     'proved':[('LIQ1','ineq-transform','平移及处处定号乘除的双向不等式变形'),
               ('LIQ2','ineq-affine','基本一次不等式的正负零系数与严格非严格完整分类'),
               ('LIQ3','ineq-two-sides','两边含未知数时合并系数的等价及全部分支'),
               ('LIQ4','ineq-compound','同时满足取交集，至少满足一个取并集')],
     'questions':'ineq-q','answer_prefix':'ineq-a',
     'not_covered':['绝对值范围（接续单元）','一般高次不等式与优化理论',
                    '实数连续数轴、完备性与拓扑','完整方程不等式教育研究']},
    {'code':'B2.8','number':29,'title':'绝对值条件与有理距离范围',
     'body':BRIDGE[56], 'answers':BRIDGE[57], 'anchor':'absineq-unit',
     'parent_code':'97Hxx','parent_chapter_number':528,'part_code':'97-XX',
     'msc_leaf_codes':['97H30'],'msc_cross_reference_codes':['97H20'],
     'module_ids':['functions'],
     'goals':['双向改写绝对值四种严格非严格比较，区别内侧且与外侧或',
              '穷尽有理距离条件的负零正比较值、端点与全部有理解集',
              '在受限候选范围中用交集筛选解并核查空范围',
              '分类仿射绝对值的零与非零系数，用正因子缩放还原距离条件'],
     'prerequisites':[(BRIDGE[36],a) for a in ['rabs-definition','rabs-properties','rabs-bounds',
                                           'rabs-products','rabs-distance']]
          +[(BRIDGE[28],'radd-laws')]+[(BRIDGE[30],'rmul-distributive')]
          +[(BRIDGE[32],'rdiv-division')]
          +[(BRIDGE[34],a) for a in ['rord-laws','rord-translation','rord-negation','rord-division']]
          +[(BRIDGE[50],'lin-affine')]
          +[(BRIDGE[54],a) for a in ['ineq-solutions','ineq-set-operations','ineq-intervals',
                                   'ineq-transform','ineq-compound']],
     'adopted_external':[(BRIDGE[42],'fun-sets','沿用朴素集合与条件子集背景'),
                         (BRIDGE[54],'ineq-intervals','区间元素限定为有理数，无穷符号不是数值端点')],
     'definitions':['absineq-distance','absineq-domain','absineq-affine'],
     'proved':[('ABI1','absineq-comparison','任意比较值下绝对值内侧合取及外侧析取的四种等价'),
               ('ABI2','absineq-distance','有理距离条件的负零正比较值和全部端点分类'),
               ('ABI3','absineq-affine','仿射绝对值零系数分类及非零系数向距离条件的可逆缩放')],
     'questions':'absineq-q','answer_prefix':'absineq-a',
     'not_covered':['实数距离空间、拓扑球与完备性','一般高次不等式及优化理论',
                    '完整方程不等式教育研究']},
]


UNIT_SPECS += [
    {'code':'B2.9','number':30,'title':'有理坐标与函数图',
     'body':BRIDGE[58], 'answers':BRIDGE[59], 'anchor':'coord-unit',
     'parent_code':'97Ixx','parent_chapter_number':529,'part_code':'97-XX',
     'msc_leaf_codes':['97I20'],'msc_cross_reference_codes':['97H30','97G70'],
     'module_ids':['functions'],
     'goals':['以有理有序对定义坐标点、两轴与象限，并穷尽九类符号位置',
              '证明函数图的坐标成员条件与第一第二坐标集合分别为域和像',
              '在给定定义域和目标内用存在且唯一检验函数图，处理空域及越界',
              '区分有限完整图和无限域取样，用成员条件求轴交点与图的公共点'],
     'prerequisites':[(BRIDGE[42],a) for a in ['fun-sets','fun-pairs','fun-definition',
                                            'fun-empty','fun-image','fun-representations']]
          +[(BRIDGE[44],a) for a in ['fc-equality','fc-restriction']]
          +[(BRIDGE[34],a) for a in ['rord-laws','rord-sign']]
          +[(BRIDGE[28],a) for a in ['radd-laws','radd-subtraction']]
          +[(BRIDGE[30],'rmul-laws')]+[(BRIDGE[32],'rdiv-division')]
          +[(BRIDGE[50],'lin-affine')]+[(BRIDGE[54],'ineq-set-operations')],
     'adopted_external':[(BRIDGE[42],'fun-sets','从给定集合按条件取子集的背景'),
                         (BRIDGE[42],'fun-pairs','有序对判等与笛卡尔积，不预设欧氏平面'),
                         (BRIDGE[42],'fun-definition','沿用含声明定义域、目标和图的函数三数据')],
     'definitions':['coord-model','coord-axes','coord-quadrants','coord-point-sets',
                    'coord-graph','coord-function-test'],
     'proved':[('CO1','coord-quadrants','有理坐标点九类符号位置的完整互斥分类'),
               ('CO2','coord-graph','函数图的点成员判据及域与像的坐标读取'),
               ('CO3','coord-function-test','声明范围内逐横坐标存在且唯一的函数图判据'),
               ('CO4','coord-intersections','函数图与轴及另一函数图的共同点成员公式')],
     'questions':'coord-q','answer_prefix':'coord-a',
     'not_covered':['实坐标平面及一般几何点的坐标表示','欧氏距离、角度、面积与连续曲线',
                    '完整解析几何或函数教育研究']},
    {'code':'B2.10','number':31,'title':'仿射图像与方程交点',
     'body':BRIDGE[60], 'answers':BRIDGE[61], 'anchor':'affgraph-unit',
     'parent_code':'97Ixx','parent_chapter_number':529,'part_code':'97-XX',
     'msc_leaf_codes':['97I20'],'msc_cross_reference_codes':['97H30','97G70'],
     'module_ids':['functions'],
     'goals':['用图的成员条件求仿射图与坐标轴的全部交集并区分点与截距',
              '证明不同输入的恒定差商，明确斜率的非零分母条件',
              '在全有理定义域上证明严格递增递减及常值的系数充要条件',
              '证明不同横坐标两点在仿射函数族中的存在唯一与退化边界',
              '完整分类两仿射图交集、竖直集合及一般一次关系的有理点集'],
     'prerequisites':[(BRIDGE[58],a) for a in ['coord-model','coord-axes','coord-point-sets',
                                            'coord-graph','coord-function-test','coord-intersections']]
          +[(BRIDGE[44],'fc-equality')]
          +[(BRIDGE[28],a) for a in ['radd-laws','radd-cancellation']]
          +[(BRIDGE[30],a) for a in ['rmul-laws','rmul-distributive']]
          +[(BRIDGE[32],'rdiv-division')]
          +[(BRIDGE[34],a) for a in ['rord-laws','rord-translation','rord-multiplication']]
          +[(BRIDGE[50],a) for a in ['lin-affine','lin-two-sides']]
          +[(BRIDGE[52],'sys-solution')]+[(BRIDGE[26],'rat-integers')],
     'adopted_external':[(BRIDGE[58],'coord-model','点限定为Q²的有理有序对'),
                         (BRIDGE[58],'coord-point-sets','图相交指同一有序对满足两个成员条件')],
     'definitions':['affgraph-definition','affgraph-intercepts','affgraph-slope',
                    'affgraph-monotonicity','affgraph-vertical','affgraph-linear-relation'],
     'proved':[('AG1','affgraph-intercepts','仿射图的纵轴唯一交点及横轴全部参数分支'),
               ('AG2','affgraph-slope','仿射输出差式与非零输入差下的恒定差商'),
               ('AG3','affgraph-monotonicity','全Q上严格单调或常值与系数符号的充要条件'),
               ('AG4','affgraph-two-points','不同横坐标两点确定唯一仿射函数'),
               ('AG5','affgraph-intersection','两仿射图唯一交点、不交或重合的完整分类')],
     'questions':'affgraph-q','answer_prefix':'affgraph-a',
     'not_covered':['非严格单调的系统教学','欧氏平行垂直、距离角度及实数连续图像',
                    '一般线性空间与解析几何的系统教学','完整函数教育研究']},
]


UNIT_SPECS += [
    {'code':'B2.11','number':32,'title':'有理数的非负整数幂',
     'body':BRIDGE[62], 'answers':BRIDGE[63], 'anchor':'pow-unit',
     'parent_code':'97Hxx','parent_chapter_number':528,'part_code':'97-XX',
     'msc_leaf_codes':['97H20'],'msc_cross_reference_codes':[],
     'module_ids':['functions'],
     'goals':['用固定更新递归定义有理底数的自然数指数幂并明确零次幂约定',
              '证明基本值、非零底数幂非零及正次零幂的完整判据',
              '分别归纳证明指数加法、乘积的幂及幂的幂',
              '构造自然数到有理数的复合嵌入并证明新旧位值幂相容',
              '区分负底数括号、负号位置和未定义的指数范围'],
     'prerequisites':[(BRIDGE[0],a) for a in ['b1-peano-rules','b1-induction',
                                           'b1-recursion-principle','b1-add-one',
                                           'b1-addition-associative']]
          +[(BRIDGE[2],'b1-right-distributivity')]+[(BRIDGE[4],'ord-predecessor')]
          +[(BRIDGE[30],a) for a in ['rmul-laws','rmul-distributive','rmul-signs',
                                   'rmul-zero-product','rmul-integers']]
          +[(BRIDGE[32],'rdiv-division')]
          +[(BRIDGE[12],a) for a in ['int-embedding','int-addition-laws']]
          +[(BRIDGE[14],'imul-basic-laws')]+[(BRIDGE[26],'rat-integers')]
          +[(BRIDGE[28],'radd-integers')]+[(BRIDGE[8],'pos-value-lemmas')]
          +[(BRIDGE[42],'fun-definition')]
          +[(BRIDGE[44],a) for a in ['fc-equality','fc-composition']],
     'adopted_external':[(BRIDGE[0],'b1-recursion-principle','沿用任意对象范围X及固定更新T的递归原则'),
                         (BRIDGE[0],'b1-induction','沿用含零自然数上的归纳规则')],
     'definitions':['pow-definition','pow-zero','pow-compatibility'],
     'proved':[('POW1','pow-zero','零次、一次、单位底数和幂为零的完整判据'),
               ('POW2','pow-addition','同底数乘法的指数加法规律'),
               ('POW3','pow-product','可交换有理乘法下乘积的幂'),
               ('POW4','pow-iteration','幂的幂与自然指数乘法'),
               ('POW5','pow-compatibility','自然数嵌入有理数后新旧位值幂相容')],
     'questions':'pow-q','answer_prefix':'pow-a',
     'not_covered':['负整数指数、有理指数与实指数','极限或除法语境中的零次幂问题',
                    '形式多项式、二项式定理与一般指数理论']},
]


UNIT_SPECS += [
    {'code':'B2.12','number':33,'title':'有限和与求和规则',
     'body':BRIDGE[64], 'answers':BRIDGE[65], 'anchor':'sum-unit',
     'parent_code':'97Hxx','parent_chapter_number':528,'part_code':'97-XX',
     'msc_leaf_codes':['97H20'],'msc_cross_reference_codes':[],
     'module_ids':['functions'],
     'goals':['区分自然项数、索引和有理数值，定义空范围与有限表',
              '以自然数和有理数的状态对固定更新构造唯一前缀和',
              '证明前缀一致性、有限表延拓独立及逐项加法和缩放',
              '借明确的自然数到有理数嵌入证明常量和公式',
              '证明移位拼接与尾补零规则，核对空段和条件减法的索引边界'],
     'prerequisites':[(BRIDGE[0],a) for a in ['b1-induction','b1-recursion-principle',
                                           'b1-add-one','b1-addition-definition',
                                           'b1-addition-associative']]
          +[(BRIDGE[4],a) for a in ['ord-cancellation','ord-partial-order',
                                   'ord-strict-equivalence','ord-successor-comparison',
                                   'ord-trichotomy','ord-addition-order']]
          +[(BRIDGE[10],'sub-definition')]
          +[(BRIDGE[28],a) for a in ['radd-laws','radd-subtraction']]
          +[(BRIDGE[30],a) for a in ['rmul-laws','rmul-distributive','rmul-signs']]
          +[(BRIDGE[42],a) for a in ['fun-definition','fun-pairs']]
          +[(BRIDGE[44],'fc-equality')]
          +[(BRIDGE[62],a) for a in ['pow-compatibility','pow-definition','pow-zero']],
     'adopted_external':[(BRIDGE[0],'b1-recursion-principle','固定更新作用在N×Q状态对上，不另采用依赖索引的递归公理'),
                         (BRIDGE[0],'b1-induction','前缀长度与索引性质使用自然数归纳'),
                         (BRIDGE[62],'pow-compatibility','项数进入有理计算时使用η:N→Q，指数和索引仍为自然数')],
     'definitions':['sum-indices','sum-definition','sum-extensionality','sum-linearity',
                    'sum-concatenation'],
     'proved':[('SUM1','sum-extensionality','前n项一致决定前缀和及有限表延拓独立'),
               ('SUM2','sum-linearity','逐项相加与有理常数缩放的有限和规则'),
               ('SUM3','sum-constant','常量有限和等于嵌入项数乘常量'),
               ('SUM4','sum-concatenation','移位序列及连续有限表拼接的和值公式'),
               ('SUM5','sum-padding','尾补任意有限个零保持和值')],
     'questions':'sum-q','answer_prefix':'sum-a',
     'not_covered':['任意有限排列或双三索引求和重排','无限级数及收敛理论',
                    '形式多项式与卷积乘法','完整初等代数教学研究']},
]


UNIT_SPECS += [{'code': 'B2.13',
  'number': 34,
  'title': '有限系数记录与多项式',
  'anchor': 'polyrec-unit',
  'goals': ['以正长度有限系数记录及补零函数区分原记录与尾零等价',
            '归纳证明最大非零指标并构造唯一规范代表',
            '以规范记录定义正式多项式、零与非零次数',
            '用既有有限和证明求值的表示无关性及零一输入公式',
            '区分系数对象、标准求值函数与有限样本'],
  'definitions': ['polyrec-records',
                  'polyrec-equivalence',
                  'polyrec-definition',
                  'polyrec-degree',
                  'polyrec-evaluation'],
  'proved': [('PR1', 'polyrec-equivalence', '尾零等价关系与共同有限长度判据'),
             ('PR2', 'polyrec-last-index', '非零记录最大非零指标的存在唯一'),
             ('PR3', 'polyrec-normalization', '规范代表存在唯一且保持全部补零系数'),
             ('PR4', 'polyrec-equality', '正式多项式相等的逐系数判据'),
             ('PR5', 'polyrec-evaluation', '求值与尾零表示无关及标准求值函数'),
             ('PR6', 'polyrec-special-values', '零与一输入以及常量多项式求值')],
  'questions': 'polyrec-q',
  'answer_prefix': 'polyrec-a',
  'adopted': [('polyrec-unit', '明确采用所有非空有限有理记录可收成集合的对象背景；不采用商集合构造')],
  'not_covered': ['多项式加法与数乘（后继单元另教）', '多项式乘法、环或模公理', '根数上界、因式定理与全有理输入求值的反向识别', '零多项式的次数定义'],
  'body': 'manuscript/foundations/polynomial_records.md',
  'answers': 'manuscript/foundations/polynomial_records_answers.md',
  'parent_code': '97Hxx',
  'parent_chapter_number': 528,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97H20'],
  'msc_cross_reference_codes': ['12E05'],
  'module_ids': ['functions'],
  'prerequisites': [('manuscript/foundations/functions_definition.md', 'fun-pairs'),
                    ('manuscript/foundations/functions_definition.md', 'fun-definition'),
                    ('manuscript/foundations/functions_composition.md', 'fc-equality'),
                    ('manuscript/foundations/finite_sums.md', 'sum-indices'),
                    ('manuscript/foundations/natural_numbers.md', 'b1-induction'),
                    ('manuscript/foundations/natural_order.md', 'ord-predecessor'),
                    ('manuscript/foundations/natural_order.md', 'ord-partial-order'),
                    ('manuscript/foundations/natural_order.md', 'ord-successor-comparison'),
                    ('manuscript/foundations/natural_order.md', 'ord-trichotomy'),
                    ('manuscript/foundations/natural_order.md', 'ord-addition-order'),
                    ('manuscript/foundations/natural_subtraction.md', 'sub-definition'),
                    ('manuscript/foundations/rational_powers.md', 'pow-definition'),
                    ('manuscript/foundations/rational_powers.md', 'pow-zero'),
                    ('manuscript/foundations/finite_sums.md', 'sum-definition'),
                    ('manuscript/foundations/finite_sums.md', 'sum-extensionality'),
                    ('manuscript/foundations/finite_sums.md', 'sum-constant'),
                    ('manuscript/foundations/finite_sums.md', 'sum-concatenation'),
                    ('manuscript/foundations/finite_sums.md', 'sum-padding'),
                    ('manuscript/foundations/functions_definition.md', 'fun-sets'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-laws'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-laws'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-zero-product')]},
 {'code': 'B2.14',
  'number': 35,
  'title': '多项式加法、数乘与求值兼容',
  'anchor': 'polyops-unit',
  'goals': ['在共同正长度上构造加法和数乘并逐索引证明良定义',
            '以系数相等证明加法律、唯一相反数与减法恢复',
            '独立证明有理标量规律及两条分配律',
            '以有限和线性律证明求值保加、数乘及差',
            '区分零和最高项抵消并证明有定义范围内的次数结论'],
  'definitions': ['polyops-definition', 'polyops-addition', 'polyops-subtraction', 'polyops-scalars'],
  'proved': [('PO1', 'polyops-definition', '加法数乘系数公式及共同正长度与表示无关'),
             ('PO2', 'polyops-addition', '加法交换结合零元与唯一相反数'),
             ('PO3', 'polyops-scalars', '有理数乘的单位零元复合及分配规律'),
             ('PO4', 'polyops-evaluation', '求值与加法数乘及差兼容'),
             ('PO5', 'polyops-degree', '排除零边界后的和次数及非零标量保次数')],
  'questions': 'polyops-q',
  'answer_prefix': 'polyops-a',
  'adopted_external': [('manuscript/foundations/polynomial_records.md',
                        'polyrec-unit',
                        '沿用非空有限有理记录集合及唯一规范代表模型，零次数未定义')],
  'not_covered': ['两个多项式的乘法与卷积', '多项式环、一般模或向量空间公理', '非零多项式根数上界、因式定理及插值', '一般双三索引有限重排'],
  'body': 'manuscript/foundations/polynomial_linear_operations.md',
  'answers': 'manuscript/foundations/polynomial_linear_operations_answers.md',
  'parent_code': '97Hxx',
  'parent_chapter_number': 528,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97H20'],
  'msc_cross_reference_codes': ['12E05'],
  'module_ids': ['functions'],
  'prerequisites': [('manuscript/foundations/polynomial_records.md', 'polyrec-records'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-equivalence'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-normalization'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-definition'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-equality'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-degree'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-evaluation'),
                    ('manuscript/foundations/finite_sums.md', 'sum-extensionality'),
                    ('manuscript/foundations/finite_sums.md', 'sum-linearity'),
                    ('manuscript/foundations/finite_sums.md', 'sum-padding'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-laws'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-opposite'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-cancellation'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-laws'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-distributive'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-signs'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-zero-product'),
                    ('manuscript/foundations/rational_powers.md', 'pow-definition'),
                    ('manuscript/foundations/rational_powers.md', 'pow-zero')]}]


UNIT_SPECS += [{'parent_code': '97Hxx',
  'parent_chapter_number': 528,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97H20'],
  'msc_cross_reference_codes': ['12E05'],
  'module_ids': ['functions'],
  'code': 'B2.15',
  'number': 36,
  'title': '移位、有限倒序与多项式乘法',
  'anchor': 'polymul-unit',
  'body': 'manuscript/foundations/polynomial_multiplication.md',
  'answers': 'manuscript/foundations/polynomial_multiplication_answers.md',
  'goals': ['逐系数构造单步移位并证明常数项分解',
            '以自然差唯一性和前缀拼接证明一维倒序',
            '定义有限卷积并证明正长度候选的存在与表示无关',
            '证明常量、零、单位、分配、数乘及乘法交换',
            '独立证明左右移位与乘法相容而不预用结合律'],
  'definitions': ['polymul-shift', 'polymul-definition', 'polymul-laws'],
  'proved': [('PM1', 'polymul-shift', '移位系数、线性及常数项分解'),
             ('PM2', 'polymul-reversal', '一维有限倒序与自然差指标恒等式'),
             ('PM3', 'polymul-definition', '有限卷积乘法存在、全指标公式及表示无关'),
             ('PM4', 'polymul-laws', '常量、零、单位、分配、数乘与交换'),
             ('PM5', 'polymul-product-shift', '左右移位与乘法相容')],
  'questions': 'polymul-q',
  'answer_prefix': 'polymul-a',
  'adopted_external': [('manuscript/foundations/polynomial_records.md',
                        'polyrec-unit',
                        '沿用非空有限有理记录集合及唯一规范代表模型；不借多项式环实例')],
  'not_covered': ['乘法结合、乘积求值及非零积次数（后继单元另证）',
                  '一般双重或三重有限求和换序',
                  '多项式除法、因式定理、根数上界及一般因式分解',
                  '一般多项式幂与任意系数环构造'],
  'prerequisites': [('manuscript/foundations/polynomial_records.md', 'polyrec-normalization'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-equality'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-definition'),
                    ('manuscript/foundations/polynomial_linear_operations.md', 'polyops-definition'),
                    ('manuscript/foundations/polynomial_linear_operations.md', 'polyops-addition'),
                    ('manuscript/foundations/polynomial_linear_operations.md', 'polyops-scalars'),
                    ('manuscript/foundations/finite_sums.md', 'sum-definition'),
                    ('manuscript/foundations/finite_sums.md', 'sum-extensionality'),
                    ('manuscript/foundations/finite_sums.md', 'sum-linearity'),
                    ('manuscript/foundations/finite_sums.md', 'sum-constant'),
                    ('manuscript/foundations/finite_sums.md', 'sum-concatenation'),
                    ('manuscript/foundations/finite_sums.md', 'sum-padding'),
                    ('manuscript/foundations/natural_numbers.md', 'b1-induction'),
                    ('manuscript/foundations/natural_order.md', 'ord-predecessor'),
                    ('manuscript/foundations/natural_order.md', 'ord-trichotomy'),
                    ('manuscript/foundations/natural_order.md', 'ord-addition-order'),
                    ('manuscript/foundations/natural_subtraction.md', 'sub-definition'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-evaluation'),
                    ('manuscript/foundations/rational_powers.md', 'pow-addition'),
                    ('manuscript/foundations/natural_numbers.md', 'b1-addition-associative'),
                    ('manuscript/foundations/finite_sums.md', 'sum-indices'),
                    ('manuscript/foundations/natural_order.md', 'ord-partial-order'),
                    ('manuscript/foundations/natural_order.md', 'ord-successor-comparison'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-laws'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-laws'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-distributive')]},
 {'parent_code': '97Hxx',
  'parent_chapter_number': 528,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97H20'],
  'msc_cross_reference_codes': ['12E05'],
  'module_ids': ['functions'],
  'code': 'B2.16',
  'number': 37,
  'title': '多项式乘法的结合、求值与次数',
  'anchor': 'polyprod-unit',
  'body': 'manuscript/foundations/polynomial_product_structure.md',
  'answers': 'manuscript/foundations/polynomial_product_structure_answers.md',
  'goals': ['按可表示的正记录长度证明乘法结合而覆盖零尾部',
            '以幂递推和一维有限和证明移位及乘积求值',
            '逐卷积位置证明非零最高系数、次数和零积判据',
            '证明非零因子的乘法消去并明确条件',
            '引入形式X和平方记号，证明常量相容并连接平方差与有理方程'],
  'definitions': ['polyprod-factorization-entry'],
  'proved': [('PL1', 'polyprod-associativity', '按原记录可表示长度证明乘法结合'),
             ('PL2', 'polyprod-evaluation', '移位求值及求值保持乘积'),
             ('PL3', 'polyprod-degree', '最高系数、非零积次数及零积消去推论'),
             ('PL4', 'polyprod-factorization-entry', '形式符号与常量的运算相容及平方差')],
  'questions': 'polyprod-q',
  'answer_prefix': 'polyprod-a',
  'adopted_external': [('manuscript/foundations/polynomial_records.md',
                        'polyrec-unit',
                        '沿用规范有限系数记录模型与零次数未定义约定')],
  'not_covered': ['一般双重或三重有限求和换序',
                  '多项式除法、因式定理、根数上界及一般因式分解',
                  '任意自然指数的多项式幂、二项式定理',
                  '一般系数环、抽象环论与全有理求值反向识别'],
  'prerequisites': [('manuscript/foundations/natural_numbers.md', 'b1-induction'),
                    ('manuscript/foundations/natural_order.md', 'ord-predecessor'),
                    ('manuscript/foundations/natural_order.md', 'ord-partial-order'),
                    ('manuscript/foundations/natural_order.md', 'ord-successor-comparison'),
                    ('manuscript/foundations/natural_order.md', 'ord-trichotomy'),
                    ('manuscript/foundations/natural_order.md', 'ord-addition-order'),
                    ('manuscript/foundations/natural_subtraction.md', 'sub-definition'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-normalization'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-equality'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-degree'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-evaluation'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-special-values'),
                    ('manuscript/foundations/polynomial_linear_operations.md', 'polyops-addition'),
                    ('manuscript/foundations/polynomial_linear_operations.md', 'polyops-subtraction'),
                    ('manuscript/foundations/polynomial_linear_operations.md', 'polyops-scalars'),
                    ('manuscript/foundations/polynomial_linear_operations.md', 'polyops-evaluation'),
                    ('manuscript/foundations/polynomial_multiplication.md', 'polymul-shift'),
                    ('manuscript/foundations/polynomial_multiplication.md', 'polymul-definition'),
                    ('manuscript/foundations/polynomial_multiplication.md', 'polymul-laws'),
                    ('manuscript/foundations/polynomial_multiplication.md', 'polymul-product-shift'),
                    ('manuscript/foundations/finite_sums.md', 'sum-extensionality'),
                    ('manuscript/foundations/finite_sums.md', 'sum-linearity'),
                    ('manuscript/foundations/finite_sums.md', 'sum-constant'),
                    ('manuscript/foundations/finite_sums.md', 'sum-concatenation'),
                    ('manuscript/foundations/finite_sums.md', 'sum-padding'),
                    ('manuscript/foundations/rational_powers.md', 'pow-definition'),
                    ('manuscript/foundations/rational_powers.md', 'pow-zero'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-distributive'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-zero-product'),
                    ('manuscript/foundations/polynomial_linear_operations.md', 'polyops-definition'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-laws'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-opposite'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-cancellation'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-laws'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-signs')]}]


UNIT_SPECS += [{'parent_code': '97Hxx',
  'parent_chapter_number': 528,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97H20'],
  'msc_cross_reference_codes': ['12E05'],
  'module_ids': ['functions'],
  'code': 'B2.17',
  'number': 38,
  'title': '一次除式的商余与综合除法',
  'anchor': 'polydiv-unit',
  'body': 'manuscript/foundations/polynomial_linear_division.md',
  'answers': 'manuscript/foundations/polynomial_linear_division_answers.md',
  'goals': ['明确有理参数对应的一次首一除式及数值余数与多项式商',
            '按非空原记录可表示长度独立构造商余',
            '以求值和非零因子消去证明余数公式及商余唯一',
            '用固定状态更新与后缀不变式证明综合除法正确和表示无关',
            '区分常量零输入并证明非常量输入的商次数'],
  'definitions': ['polydiv-linear-divisor', 'polydiv-quotient-remainder', 'polydiv-synthetic'],
  'proved': [('PD1', 'polydiv-linear-divisor', '一次除式的非零性、次数与求值'),
             ('PD2', 'polydiv-existence', '按原记录长度证明商余存在'),
             ('PD3', 'polydiv-uniqueness', '余数求值公式与商余唯一性'),
             ('PD4', 'polydiv-invariant', '综合除法后缀不变式及输出表示无关')],
  'questions': 'polydiv-q',
  'answer_prefix': 'polydiv-a',
  'adopted_external': [('manuscript/foundations/polynomial_records.md',
                        'polyrec-unit',
                        '沿用规范有限有理记录集合与零次数未定义约定'),
                       ('manuscript/foundations/natural_numbers.md',
                        'b1-recursion-principle',
                        '采用固定更新递归原则构造综合除法状态序列'),
                       ('manuscript/foundations/functions_definition.md',
                        'fun-pairs',
                        '沿用有序对与笛卡尔积形成状态集合')],
  'not_covered': ['任意多项式除数或非首一除数的一般除法', '因式定理、根数界与求值反向识别（后继单元另证）', '实数或复数参数、根的重数及根存在定理', '一般多项式欧几里得算法'],
  'prerequisites': [('manuscript/foundations/polynomial_records.md', 'polyrec-normalization'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-equality'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-degree'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-evaluation'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-special-values'),
                    ('manuscript/foundations/polynomial_linear_operations.md', 'polyops-addition'),
                    ('manuscript/foundations/polynomial_linear_operations.md', 'polyops-subtraction'),
                    ('manuscript/foundations/polynomial_linear_operations.md', 'polyops-scalars'),
                    ('manuscript/foundations/polynomial_linear_operations.md', 'polyops-evaluation'),
                    ('manuscript/foundations/polynomial_multiplication.md', 'polymul-shift'),
                    ('manuscript/foundations/polynomial_multiplication.md', 'polymul-laws'),
                    ('manuscript/foundations/polynomial_product_structure.md', 'polyprod-associativity'),
                    ('manuscript/foundations/polynomial_product_structure.md', 'polyprod-evaluation'),
                    ('manuscript/foundations/polynomial_product_structure.md', 'polyprod-degree'),
                    ('manuscript/foundations/polynomial_product_structure.md',
                     'polyprod-zero-cancellation'),
                    ('manuscript/foundations/polynomial_product_structure.md',
                     'polyprod-factorization-entry'),
                    ('manuscript/foundations/natural_numbers.md', 'b1-induction'),
                    ('manuscript/foundations/natural_numbers.md', 'b1-recursion-principle'),
                    ('manuscript/foundations/natural_order.md', 'ord-predecessor'),
                    ('manuscript/foundations/natural_order.md', 'ord-successor-comparison'),
                    ('manuscript/foundations/natural_order.md', 'ord-cancellation'),
                    ('manuscript/foundations/natural_subtraction.md', 'sub-definition'),
                    ('manuscript/foundations/functions_definition.md', 'fun-pairs'),
                    ('manuscript/foundations/natural_order.md', 'ord-trichotomy'),
                    ('manuscript/foundations/natural_order.md', 'ord-addition-order'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-laws'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-cancellation'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-laws'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-distributive')]},
 {'parent_code': '97Hxx',
  'parent_chapter_number': 528,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97H20'],
  'msc_cross_reference_codes': ['12E05'],
  'module_ids': ['functions'],
  'code': 'B2.18',
  'number': 39,
  'title': '因式定理、不同根数界与恒等识别',
  'anchor': 'polyroot-unit',
  'body': 'manuscript/foundations/polynomial_roots_identity.md',
  'answers': 'manuscript/foundations/polynomial_roots_identity_answers.md',
  'goals': ['定义有理根与一次因式并证明含零边界的因式定理',
            '以不同根向商转移和次数归纳证明不同有理根数界',
            '用共同系数上界证明足量互异样本能够判等且兼容零对象',
            '由自然数嵌入的有限互异初段证明标准有理求值函数识别系数',
            '区分限制输入、重复样本、重数与有理根不存在的边界'],
  'definitions': ['polyroot-entry', 'polyroot-factor', 'polyroot-bound', 'polyroot-finite-identity'],
  'proved': [('RT1', 'polyroot-factor', '有理根与一次因式等价'),
             ('RT2', 'polyroot-bound', '非零多项式的不同有理根次数界'),
             ('RT3', 'polyroot-finite-identity', '共同系数上界下的有限点判等'),
             ('RT4', 'polyroot-standard-identity', '标准Q到Q求值函数与形式系数的恒等识别')],
  'questions': 'polyroot-q',
  'answer_prefix': 'polyroot-a',
  'adopted_external': [('manuscript/foundations/polynomial_records.md',
                        'polyrec-unit',
                        '沿用规范系数对象，零次数不定义'),
                       ('manuscript/foundations/functions_definition.md',
                        'fun-definition',
                        '标准求值函数仍采用定义域、目标和图三数据约定')],
  'not_covered': ['根的重数、一般多项式除法与一般因式分解算法', '实根复根存在、代数基本定理及其他系数域推广', '任意多项式在有理数上完全分裂', '插值构造与一般无限集合基数理论'],
  'prerequisites': [('manuscript/foundations/polynomial_records.md', 'polyrec-definition'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-equality'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-degree'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-evaluation'),
                    ('manuscript/foundations/polynomial_records.md', 'polyrec-special-values'),
                    ('manuscript/foundations/polynomial_linear_operations.md', 'polyops-subtraction'),
                    ('manuscript/foundations/polynomial_linear_operations.md', 'polyops-evaluation'),
                    ('manuscript/foundations/polynomial_multiplication.md', 'polymul-laws'),
                    ('manuscript/foundations/polynomial_product_structure.md', 'polyprod-evaluation'),
                    ('manuscript/foundations/polynomial_product_structure.md', 'polyprod-degree'),
                    ('manuscript/foundations/polynomial_product_structure.md',
                     'polyprod-factorization-entry'),
                    ('manuscript/foundations/polynomial_linear_division.md', 'polydiv-linear-divisor'),
                    ('manuscript/foundations/polynomial_linear_division.md', 'polydiv-existence'),
                    ('manuscript/foundations/polynomial_linear_division.md', 'polydiv-uniqueness'),
                    ('manuscript/foundations/natural_numbers.md', 'b1-induction'),
                    ('manuscript/foundations/natural_order.md', 'ord-cancellation'),
                    ('manuscript/foundations/natural_order.md', 'ord-successor-comparison'),
                    ('manuscript/foundations/natural_order.md', 'ord-trichotomy'),
                    ('manuscript/foundations/finite_sums.md', 'sum-indices'),
                    ('manuscript/foundations/rational_powers.md', 'pow-compatibility'),
                    ('manuscript/foundations/functions_composition.md', 'fc-equality'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-cancellation'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-zero-product'),
                    ('manuscript/foundations/rationals_order.md', 'rord-laws'),
                    ('manuscript/foundations/rationals_order.md', 'rord-integers'),
                    ('manuscript/foundations/rationals_order.md', 'rord-translation'),
                    ('manuscript/foundations/rationals_order.md', 'rord-negation'),
                    ('manuscript/foundations/rationals_order.md', 'rord-multiplication'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-laws'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-laws'),
                    ('manuscript/foundations/polynomial_linear_operations.md', 'polyops-definition')]}]


UNIT_SPECS += [{'parent_code': '97Hxx',
  'parent_chapter_number': 528,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97H30'],
  'msc_cross_reference_codes': ['97H20'],
  'module_ids': ['functions'],
  'code': 'B2.19',
  'number': 40,
  'title': '有理平方与平方方程',
  'anchor': 'sqrat-unit',
  'body': 'manuscript/foundations/rational_square_equations.md',
  'answers': 'manuscript/foundations/rational_square_equations_answers.md',
  'goals': ['证明平方符号及非负范围中的严格比较',
            '区分存在与唯一并定义有理平方上的部分根函数',
            '按右端条件完整分类平方方程',
            '用互素乘积和规范代表唯一性证明有理平方判据',
            '用整数平方间隙排除二的有理平方根'],
  'definitions': ['sqrat-root-uniqueness'],
  'proved': [('SQ1', 'sqrat-order', '平方符号与非负平方比较'),
             ('SQ2', 'sqrat-root-uniqueness', '同平方两支及非负根唯一性'),
             ('SQ3', 'sqrat-solutions', '有理平方方程完整分类'),
             ('SQ4', 'sqrat-normal-form-test', '规范代表的有理平方判据')],
  'questions': 'sqrat-q',
  'answer_prefix': 'sqrat-a',
  'adopted_external': [('manuscript/foundations/functions_definition.md',
                        'fun-definition',
                        '沿用已声明集合背景和定义域、目标及图的函数约定；不采用实数理论')],
  'not_covered': ['实数构造与每个非负实数的平方根存在', '一般n次根与素数唯一分解', '浮点近似开方'],
  'prerequisites': [('manuscript/foundations/coprimality.md', 'cop-bezout'),
                    ('manuscript/foundations/coprimality.md', 'cop-product'),
                    ('manuscript/foundations/functions_definition.md', 'fun-definition'),
                    ('manuscript/foundations/gcd_euclidean.md', 'gcd-properties'),
                    ('manuscript/foundations/integer_division.md', 'idiv-absolute'),
                    ('manuscript/foundations/integers_multiplication.md', 'imul-sign-rules'),
                    ('manuscript/foundations/integers_addition_order.md', 'int-order-laws'),
                    ('manuscript/foundations/natural_order.md', 'ord-multiplication-order'),
                    ('manuscript/foundations/natural_order.md', 'ord-successor-comparison'),
                    ('manuscript/foundations/rational_powers.md', 'pow-compatibility'),
                    ('manuscript/foundations/rational_powers.md', 'pow-definition'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-laws'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-subtraction'),
                    ('manuscript/foundations/rationals_construction.md', 'rat-classes'),
                    ('manuscript/foundations/rationals_construction.md', 'rat-normal-form'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-definition'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-distributive'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-laws'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-signs'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-zero-product'),
                    ('manuscript/foundations/rationals_order.md', 'rord-integers'),
                    ('manuscript/foundations/rationals_order.md', 'rord-laws'),
                    ('manuscript/foundations/rationals_order.md', 'rord-multiplication'),
                    ('manuscript/foundations/rationals_order.md', 'rord-negation'),
                    ('manuscript/foundations/rationals_order.md', 'rord-sign'),
                    ('manuscript/foundations/rationals_order.md', 'rord-translation')]},
 {'parent_code': '97Hxx',
  'parent_chapter_number': 528,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97H30'],
  'msc_cross_reference_codes': ['97H20'],
  'module_ids': ['functions'],
  'code': 'B2.20',
  'number': 41,
  'title': '配方与有理二次方程',
  'anchor': 'quad-unit',
  'body': 'manuscript/foundations/rational_quadratic_equations.md',
  'answers': 'manuscript/foundations/rational_quadratic_equations_answers.md',
  'goals': ['逐项证明配方恒等式和合法分母条件',
            '证明判别式平方方程与原方程的双向等价',
            '完整处理退化参数和有理平方存在条件',
            '证明正负二次系数下有理输入上的界及唯一等号',
            '区分有限有理样本与全域结论'],
  'definitions': ['quad-entry', 'quad-discriminant', 'quad-bound'],
  'proved': [('QC1', 'quad-completion', '配方恒等式'),
             ('QC2', 'quad-discriminant', '可逆判别式平方方程'),
             ('QC3', 'quad-rational-solutions', '全部有理解与退化分支'),
             ('QC4', 'quad-bound', '有理输入上的界与唯一等号')],
  'questions': 'quad-q',
  'answer_prefix': 'quad-a',
  'adopted_external': [('manuscript/foundations/functions_definition.md',
                        'fun-definition',
                        '沿用已声明集合背景和定义域、目标及图的函数约定；不采用实数理论')],
  'not_covered': ['实数或复数根的存在及连续抛物线', '根的重数、一般多项式分解', '微积分极值理论'],
  'prerequisites': [('manuscript/foundations/rational_coordinates.md', 'coord-model'),
                    ('manuscript/foundations/rational_coordinates.md', 'coord-samples'),
                    ('manuscript/foundations/linear_equations.md', 'lin-addition'),
                    ('manuscript/foundations/linear_equations.md', 'lin-affine'),
                    ('manuscript/foundations/linear_equations.md', 'lin-division'),
                    ('manuscript/foundations/linear_equations.md', 'lin-equivalence'),
                    ('manuscript/foundations/linear_equations.md', 'lin-multiplication'),
                    ('manuscript/foundations/linear_equations.md', 'lin-solutions'),
                    ('manuscript/foundations/rational_powers.md', 'pow-compatibility'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-cancellation'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-laws'),
                    ('manuscript/foundations/rationals_division.md', 'rdiv-cancellation'),
                    ('manuscript/foundations/rationals_division.md', 'rdiv-division'),
                    ('manuscript/foundations/rationals_division.md', 'rdiv-signs'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-cancellation'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-distributive'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-laws'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-signs'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-zero-product'),
                    ('manuscript/foundations/rationals_order.md', 'rord-integers'),
                    ('manuscript/foundations/rationals_order.md', 'rord-laws'),
                    ('manuscript/foundations/rationals_order.md', 'rord-multiplication'),
                    ('manuscript/foundations/rationals_order.md', 'rord-translation'),
                    ('manuscript/foundations/rational_square_equations.md', 'sqrat-normal-form-test'),
                    ('manuscript/foundations/rational_square_equations.md', 'sqrat-order'),
                    ('manuscript/foundations/rational_square_equations.md', 'sqrat-root-uniqueness'),
                    ('manuscript/foundations/rational_square_equations.md', 'sqrat-solutions')]}]


UNIT_SPECS += [{'parent_code': '97Fxx',
  'parent_chapter_number': 526,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97F50'],
  'msc_cross_reference_codes': ['06A05', '03E20'],
  'module_ids': ['number-systems'],
  'code': 'B2.21',
  'number': 42,
  'title': '有理数的稠密、界与平方缺口',
  'anchor': 'qgap-unit',
  'body': 'manuscript/foundations/rational_gaps_bounds.md',
  'answers': 'manuscript/foundations/rational_gaps_bounds_answers.md',
  'goals': ['证明有理中点稠密与从合法记录取得的正自然数界', '区分上界、最大元与相对于有理数的上确界', '逐项推导平方缺口改进式并核正分母', '完整证明非空有上界集合无有理上确界'],
  'definitions': ['qgap-supremum-definition', 'qgap-perturbation'],
  'proved': [('QG1', 'qgap-density-archimedean', '中点稠密与显式阿基米德界'),
             ('QG2', 'qgap-supremum-definition', '上界、最大元与上确界的定义和性质'),
             ('QG3', 'qgap-perturbation', '平方缺口的显式改进公式'),
             ('QG4', 'qgap-no-rational-supremum', '非空有上界却无有理上确界')],
  'questions': 'qgap-q',
  'answer_prefix': 'qgap-a',
  'not_covered': ['实数算术与实数平方根存在性', '迭代极限、连续性与拓扑', '一般集合的上确界存在性'],
  'prerequisites': [('manuscript/foundations/functions_definition.md', 'fun-definition'),
                    ('manuscript/foundations/functions_definition.md', 'fun-sets'),
                    ('manuscript/foundations/integer_division.md', 'idiv-absolute'),
                    ('manuscript/foundations/integers_multiplication.md', 'imul-order'),
                    ('manuscript/foundations/integers_addition_order.md', 'int-embedding'),
                    ('manuscript/foundations/integers_addition_order.md', 'int-order-laws'),
                    ('manuscript/foundations/natural_order.md', 'ord-predecessor'),
                    ('manuscript/foundations/natural_order.md', 'ord-successor-comparison'),
                    ('manuscript/foundations/rational_powers.md', 'pow-compatibility'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-laws'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-subtraction'),
                    ('manuscript/foundations/rationals_construction.md', 'rat-classes'),
                    ('manuscript/foundations/rationals_construction.md', 'rat-integers'),
                    ('manuscript/foundations/rationals_division.md', 'rdiv-cancellation'),
                    ('manuscript/foundations/rationals_division.md', 'rdiv-division'),
                    ('manuscript/foundations/rationals_division.md', 'rdiv-signs'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-distributive'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-laws'),
                    ('manuscript/foundations/rationals_order.md', 'rord-definition'),
                    ('manuscript/foundations/rationals_order.md', 'rord-division'),
                    ('manuscript/foundations/rationals_order.md', 'rord-integers'),
                    ('manuscript/foundations/rationals_order.md', 'rord-laws'),
                    ('manuscript/foundations/rationals_order.md', 'rord-multiplication'),
                    ('manuscript/foundations/rationals_order.md', 'rord-negation'),
                    ('manuscript/foundations/rationals_order.md', 'rord-reciprocal'),
                    ('manuscript/foundations/rationals_order.md', 'rord-translation'),
                    ('manuscript/foundations/rational_square_equations.md', 'sqrat-order'),
                    ('manuscript/foundations/rational_square_equations.md', 'sqrat-two-not-square')],
  'adopted_external': [('manuscript/foundations/functions_definition.md',
                        'fun-sets',
                        '沿用已明确采用的集合外延、已有集合及条件子集背景；不假定实数完备性')]},
 {'parent_code': '97Fxx',
  'parent_chapter_number': 526,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97F50'],
  'msc_cross_reference_codes': ['06A05', '03E20'],
  'module_ids': ['number-systems'],
  'code': 'B2.22',
  'number': 43,
  'title': '戴德金分割、次序与上确界',
  'anchor': 'cut-unit',
  'body': 'manuscript/foundations/dedekind_cuts_order.md',
  'answers': 'manuscript/foundations/dedekind_cuts_order_answers.md',
  'goals': ['公开幂集采用背景并逐项核四条件分割', '证明包含全序与有理下段的保序、次序反映和单射', '证明平方缺口给出非主分割', '证明非空有上界分割族以并集给出上确界并核失败边界'],
  'definitions': ['cut-set-background', 'cut-definition', 'cut-order-embedding', 'cut-supremum'],
  'proved': [('DC1', 'cut-definition', '单侧分割与有理下段'),
             ('DC2', 'cut-order-embedding', '包含全序与有理数的保序嵌入'),
             ('DC3', 'cut-gap', '平方缺口的非主分割'),
             ('DC4', 'cut-supremum', '非空有上界分割族的并集上确界')],
  'questions': 'cut-q',
  'answer_prefix': 'cut-a',
  'not_covered': ['分割加法、乘法、负数、倒数与有序域结构', '实数平方根及无理长度理论', '完整格、无界族或空族的上确界', '所有分割的通用判等或成员判定程序'],
  'prerequisites': [('manuscript/foundations/functions_definition.md', 'fun-definition'),
                    ('manuscript/foundations/functions_definition.md', 'fun-image'),
                    ('manuscript/foundations/functions_definition.md', 'fun-sets'),
                    ('manuscript/foundations/rational_gaps_bounds.md', 'qgap-density-archimedean'),
                    ('manuscript/foundations/rational_gaps_bounds.md', 'qgap-no-rational-supremum'),
                    ('manuscript/foundations/rational_gaps_bounds.md', 'qgap-perturbation'),
                    ('manuscript/foundations/rational_gaps_bounds.md', 'qgap-supremum-definition'),
                    ('manuscript/foundations/rationals_order.md', 'rord-laws'),
                    ('manuscript/foundations/rationals_order.md', 'rord-translation'),
                    ('manuscript/foundations/rational_square_equations.md', 'sqrat-order')],
  'adopted_external': [('manuscript/foundations/functions_definition.md',
                        'fun-sets',
                        '沿用已明确采用的集合外延、已有集合及条件子集背景；不假定实数完备性')],
  'adopted': [('cut-set-background', '显式采用有理数幂集 P(Q) 存在与条件子集；未从集合论公理证明，不假定选择函数或实数运算')]}]


UNIT_SPECS += [{'parent_code': '97Fxx',
  'parent_chapter_number': 526,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97F50'],
  'msc_cross_reference_codes': ['06A05', '06F20'],
  'module_ids': ['number-systems'],
  'code': 'B2.23',
  'number': 44,
  'title': '分割的有理逼近、加法与相反数',
  'anchor': 'cutadd-unit',
  'body': 'manuscript/foundations/dedekind_addition.md',
  'answers': 'manuscript/foundations/dedekind_addition_answers.md',
  'goals': ['从有理网格及已证最小元得到严格跨界间隔', '逐四条件构造和与负分割', '区分严格反射与直接补集反射', '证明新运算在有理下段上的相容'],
  'definitions': ['cutadd-separation', 'cutadd-definition', 'cutadd-negation', 'cutadd-rational'],
  'proved': [('DA1', 'cutadd-grid', '任意小的有理跨界间隔'),
             ('DA2', 'cutadd-definition', '和分割闭合及精确与严格见证等价'),
             ('DA3', 'cutadd-negation', '严格负分割的四条件闭合'),
             ('DA4', 'cutadd-rational', '有理嵌入的加法及取反相容')],
  'questions': 'cutadd-q',
  'answer_prefix': 'cutadd-a',
  'not_covered': ['分割乘法、倒数与有序域结构', '实数平方根、无理长度、极限及连续性', '任意分割的通用成员判定、判等或网格搜索算法'],
  'prerequisites': [('manuscript/foundations/dedekind_cuts_order.md', 'cut-definition'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-gap'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-order-embedding'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-set-background'),
                    ('manuscript/foundations/natural_order.md', 'ord-predecessor'),
                    ('manuscript/foundations/natural_order.md', 'ord-strong-induction'),
                    ('manuscript/foundations/natural_order.md', 'ord-successor-comparison'),
                    ('manuscript/foundations/natural_order_answers.md', 'ord-a07'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-laws'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-opposite'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-subtraction'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-distributive'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-laws'),
                    ('manuscript/foundations/rationals_division.md', 'rdiv-division'),
                    ('manuscript/foundations/rational_gaps_bounds.md', 'qgap-density-archimedean'),
                    ('manuscript/foundations/rational_powers.md', 'pow-compatibility'),
                    ('manuscript/foundations/rationals_order.md', 'rord-division'),
                    ('manuscript/foundations/rationals_order.md', 'rord-laws'),
                    ('manuscript/foundations/rationals_order.md', 'rord-negation'),
                    ('manuscript/foundations/rationals_order.md', 'rord-translation')],
  'adopted_external': [('manuscript/foundations/dedekind_cuts_order.md',
                        'cut-set-background',
                        '沿用有理数幂集及条件子集背景；不新增选择公理或实数域假设')]},
 {'parent_code': '97Fxx',
  'parent_chapter_number': 526,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97F50'],
  'msc_cross_reference_codes': ['06A05', '06F20'],
  'module_ids': ['number-systems'],
  'code': 'B2.24',
  'number': 45,
  'title': '分割加法的群律与次序平移',
  'anchor': 'cutgroup-unit',
  'body': 'manuscript/foundations/dedekind_additive_order.md',
  'answers': 'manuscript/foundations/dedekind_additive_order_answers.md',
  'goals': ['从成员见证证明加法群律', '由严格网格见证证明逆元并核唯一性', '证明平移次序保持反射和双射', '建立取反减法、唯一加法解及差的符号'],
  'definitions': ['cutgroup-translation', 'cutgroup-negation-subtraction'],
  'proved': [('DG1', 'cutgroup-laws', '加法交换结合与零单位'),
             ('DG2', 'cutgroup-inverses', '负分割为逆元及逆元唯一'),
             ('DG3', 'cutgroup-translation', '平移保序反射、严格比较及双侧逆'),
             ('DG4', 'cutgroup-negation-subtraction', '取反反序、减法、唯一加法解及差的符号')],
  'questions': 'cutgroup-q',
  'answer_prefix': 'cutgroup-a',
  'not_covered': ['分割乘法、倒数与有序域结构', '实数平方根、无理长度、极限及连续性', '任意分割的通用成员判定、判等或网格搜索算法'],
  'prerequisites': [('manuscript/foundations/dedekind_addition.md', 'cutadd-definition'),
                    ('manuscript/foundations/dedekind_addition.md', 'cutadd-grid'),
                    ('manuscript/foundations/dedekind_addition.md', 'cutadd-negation'),
                    ('manuscript/foundations/dedekind_addition.md', 'cutadd-rational'),
                    ('manuscript/foundations/dedekind_addition.md', 'cutadd-separation'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-definition'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-gap'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-order-embedding'),
                    ('manuscript/foundations/functions_definition.md', 'fun-definition'),
                    ('manuscript/foundations/functions_inverse.md', 'inv-two-sided'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-laws'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-opposite'),
                    ('manuscript/foundations/rationals_addition.md', 'radd-subtraction'),
                    ('manuscript/foundations/rationals_order.md', 'rord-negation'),
                    ('manuscript/foundations/rationals_order.md', 'rord-translation')],
  'adopted_external': [('manuscript/foundations/dedekind_cuts_order.md',
                        'cut-set-background',
                        '沿用有理数幂集及条件子集背景；不新增选择公理或实数域假设')]}]


UNIT_SPECS += [{'parent_code': '97Fxx',
  'parent_chapter_number': 526,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97F50'],
  'msc_cross_reference_codes': ['06A05'],
  'module_ids': ['number-systems'],
  'code': 'B2.25',
  'number': 46,
  'title': '非负分割的乘积与有理相容',
  'anchor': 'cutprod-unit',
  'body': 'manuscript/foundations/dedekind_nonnegative_product.md',
  'answers': 'manuscript/foundations/dedekind_nonnegative_product_answers.md',
  'goals': ['区分非负分割与有理成员的符号', '从正见证与独立负支逐四条件构造非负乘积', '证明零积正性、交换单位及弱单调', '以有理中点证明非负有理嵌入相容'],
  'definitions': ['cutprod-unit', 'cutprod-definition', 'cutprod-basic-laws'],
  'proved': [('NP1', 'cutprod-positive-witnesses', '正分割的识别与正有理内外见证'),
             ('NP2', 'cutprod-definition', '非负乘积闭合、零与正性及零积条件'),
             ('NP3', 'cutprod-basic-laws', '交换、单位及弱单调'),
             ('NP4', 'cutprod-rational', '非负有理下段的乘积相容')],
  'questions': 'cutprod-q',
  'answer_prefix': 'cutprod-a',
  'not_covered': ['负输入乘法及完整有符号环结构', '非零分割倒数、除法、乘法映射满射及域结构', '实数平方根、无理长度、极限与连续性', '任意分割的通用成员判定或数值计算程序'],
  'prerequisites': [('manuscript/foundations/dedekind_addition.md', 'cutadd-separation'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-laws'),
                    ('manuscript/foundations/dedekind_additive_order.md',
                     'cutgroup-negation-subtraction'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-definition'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-gap'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-order-embedding'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-set-background'),
                    ('manuscript/foundations/rational_gaps_bounds.md', 'qgap-density-archimedean'),
                    ('manuscript/foundations/rationals_division.md', 'rdiv-cancellation'),
                    ('manuscript/foundations/rationals_division.md', 'rdiv-division'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-distributive'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-laws'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-signs'),
                    ('manuscript/foundations/rationals_order.md', 'rord-division'),
                    ('manuscript/foundations/rationals_order.md', 'rord-laws'),
                    ('manuscript/foundations/rationals_order.md', 'rord-multiplication'),
                    ('manuscript/foundations/rationals_order.md', 'rord-translation')],
  'adopted_external': [('manuscript/foundations/dedekind_cuts_order.md',
                        'cut-set-background',
                        '沿用已有分割集合及条件子集背景；非负分割从已有集合取子集，不新增实数域或选择公理')]},
 {'parent_code': '97Fxx',
  'parent_chapter_number': 526,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97F50'],
  'msc_cross_reference_codes': ['06A05'],
  'module_ids': ['number-systems'],
  'code': 'B2.26',
  'number': 47,
  'title': '非负乘积的结合、分配与严格比较',
  'anchor': 'cutprod-laws-unit',
  'body': 'manuscript/foundations/dedekind_nonnegative_laws.md',
  'answers': 'manuscript/foundations/dedekind_nonnegative_laws_answers.md',
  'goals': ['把原成员上调为可用的正见证并处理零边界', '展开嵌套成员证明非负结合律', '处理负成员及共同因子证明两侧分配', '由正差和已证分配得到正因子比较反射及消去'],
  'definitions': ['cutprod-cofinal-witnesses', 'cutprod-strict-order'],
  'proved': [('NL1', 'cutprod-cofinal-witnesses', '非负和正性及正输入中的更大正见证'),
             ('NL2', 'cutprod-associative', '非负乘积结合律'),
             ('NL3', 'cutprod-distributive', '非负乘积两侧分配律'),
             ('NL4', 'cutprod-strict-order', '正因子严格比较、反射及消去')],
  'questions': 'cutprodlaw-q',
  'answer_prefix': 'cutprodlaw-a',
  'not_covered': ['负输入乘法及完整有符号环结构', '非零分割倒数、除法、乘法映射满射及域结构', '实数平方根、无理长度、极限与连续性', '任意分割的通用成员判定或数值计算程序'],
  'prerequisites': [('manuscript/foundations/dedekind_addition.md', 'cutadd-definition'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-inverses'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-laws'),
                    ('manuscript/foundations/dedekind_additive_order.md',
                     'cutgroup-negation-subtraction'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-translation'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-definition'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-order-embedding'),
                    ('manuscript/foundations/dedekind_nonnegative_product.md', 'cutprod-basic-laws'),
                    ('manuscript/foundations/dedekind_nonnegative_product.md', 'cutprod-definition'),
                    ('manuscript/foundations/dedekind_nonnegative_product.md',
                     'cutprod-positive-witnesses'),
                    ('manuscript/foundations/dedekind_nonnegative_product.md', 'cutprod-rational'),
                    ('manuscript/foundations/functions_bijections.md', 'bij-injective'),
                    ('manuscript/foundations/functions_bijections.md', 'bij-surjective'),
                    ('manuscript/foundations/functions_definition.md', 'fun-definition'),
                    ('manuscript/foundations/rational_gaps_bounds.md', 'qgap-density-archimedean'),
                    ('manuscript/foundations/rationals_division.md', 'rdiv-division'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-distributive'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-laws'),
                    ('manuscript/foundations/rationals_order.md', 'rord-division'),
                    ('manuscript/foundations/rationals_order.md', 'rord-multiplication'),
                    ('manuscript/foundations/rationals_order.md', 'rord-translation')],
  'adopted_external': [('manuscript/foundations/dedekind_cuts_order.md',
                        'cut-set-background',
                        '沿用已有分割集合及条件子集背景；非负分割从已有集合取子集，不新增实数域或选择公理')]}]


UNIT_SPECS += [{'parent_code': '97Fxx',
  'parent_chapter_number': 526,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97F50'],
  'msc_cross_reference_codes': ['06A05'],
  'module_ids': ['number-systems'],
  'code': 'B2.27',
  'number': 48,
  'title': '全部分割的乘法、符号与结合',
  'anchor': 'cutsigned-unit',
  'body': 'manuscript/foundations/dedekind_signed_product.md',
  'answers': 'manuscript/foundations/dedekind_signed_product_answers.md',
  'goals': ['以互斥穷尽符号分支定义全乘法', '从定义证明符号而不提前调用分配律', '以任意正幅度和穷尽标签表证明结合', '证明各符号有理相容并区分零积与倒数存在'],
  'definitions': ['cutsigned-definition', 'cutsigned-signs'],
  'proved': [('SP1', 'cutsigned-definition', '四个符号区域上的全乘法及闭合'),
             ('SP2', 'cutsigned-signs', '交换零单位、单次取反与双负乘积'),
             ('SP3', 'cutsigned-associative', '全符号乘法结合律'),
             ('SP4', 'cutsigned-rational-zero', '全有理相容及零积条件')],
  'questions': 'cutsigned-q',
  'answer_prefix': 'cutsigned-a',
  'not_covered': ['全符号分配及有序交换环（后续B2.28建立）',
                  '非零分割倒数、除法、乘法映射满射及域结构',
                  '实数平方根、无理长度、极限与连续性',
                  '任意分割的通用成员判定或数值计算程序'],
  'prerequisites': [('manuscript/foundations/dedekind_addition.md', 'cutadd-negation'),
                    ('manuscript/foundations/dedekind_addition.md', 'cutadd-rational'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-inverses'),
                    ('manuscript/foundations/dedekind_additive_order.md',
                     'cutgroup-negation-subtraction'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-order-embedding'),
                    ('manuscript/foundations/dedekind_nonnegative_laws.md', 'cutprod-associative'),
                    ('manuscript/foundations/dedekind_nonnegative_product.md', 'cutprod-basic-laws'),
                    ('manuscript/foundations/dedekind_nonnegative_product.md', 'cutprod-definition'),
                    ('manuscript/foundations/dedekind_nonnegative_product.md',
                     'cutprod-positive-witnesses'),
                    ('manuscript/foundations/dedekind_nonnegative_product.md', 'cutprod-rational'),
                    ('manuscript/foundations/functions_definition.md', 'fun-definition'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-laws'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-signs')],
  'adopted_external': [('manuscript/foundations/dedekind_cuts_order.md',
                        'cut-set-background',
                        '沿用已有分割集合及条件子集背景；符号分支只在已有集合定义运算，不新增实数域或选择公理')]},
 {'parent_code': '97Fxx',
  'parent_chapter_number': 526,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97F50'],
  'msc_cross_reference_codes': ['06A05', '06F25'],
  'module_ids': ['number-systems'],
  'code': 'B2.28',
  'number': 49,
  'title': '全分配律、乘法比较与消去',
  'anchor': 'cutring-unit',
  'body': 'manuscript/foundations/dedekind_ring_order.md',
  'answers': 'manuscript/foundations/dedekind_ring_order_answers.md',
  'goals': ['用非负差和加法移项处理异号分配', '全分配之后才用乘法差式并命名交换环', '分别处理正负零因子的次序方向及反射', '证明非零消去并区别单射与满射及倒数存在'],
  'definitions': ['cutring-distributive', 'cutring-multiplication-order', 'cutring-cancellation'],
  'proved': [('SR1', 'cutring-distributive-nonnegative-factor', '非负因子的全符号分配'),
             ('SR2', 'cutring-distributive', '全因子两侧分配、差式与交换环'),
             ('SR3', 'cutring-multiplication-order', '正负零因子的比较及反射'),
             ('SR4', 'cutring-cancellation', '非零因子消去与乘法映射单射')],
  'questions': 'cutring-q',
  'answer_prefix': 'cutring-a',
  'not_covered': ['非零分割倒数、除法、乘法映射满射及域结构', '实数平方根、无理长度、极限与连续性', '任意分割的通用成员判定或数值计算程序'],
  'prerequisites': [('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-inverses'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-laws'),
                    ('manuscript/foundations/dedekind_additive_order.md',
                     'cutgroup-negation-subtraction'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-translation'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-order-embedding'),
                    ('manuscript/foundations/dedekind_nonnegative_laws.md', 'cutprod-cofinal-witnesses'),
                    ('manuscript/foundations/dedekind_nonnegative_laws.md', 'cutprod-distributive'),
                    ('manuscript/foundations/dedekind_nonnegative_product.md', 'cutprod-definition'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-associative'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-definition'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-rational-zero'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-signs'),
                    ('manuscript/foundations/functions_bijections.md', 'bij-injective'),
                    ('manuscript/foundations/functions_bijections.md', 'bij-surjective'),
                    ('manuscript/foundations/functions_definition.md', 'fun-definition')],
  'adopted_external': [('manuscript/foundations/dedekind_cuts_order.md',
                        'cut-set-background',
                        '沿用已有分割集合及条件子集背景；符号分支只在已有集合定义运算，不新增实数域或选择公理')]}]


UNIT_SPECS += [{'parent_code': '97Fxx',
  'parent_chapter_number': 526,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97F50'],
  'msc_cross_reference_codes': ['06A05', '06F25'],
  'module_ids': ['number-systems'],
  'code': 'B2.29',
  'number': 50,
  'title': '分割的非零倒数与唯一性',
  'anchor': 'cutinv-unit',
  'body': 'manuscript/foundations/dedekind_inverse.md',
  'answers': 'manuscript/foundations/dedekind_inverse_answers.md',
  'goals': ['从正有理外点构造合法正倒数分割', '以严格跨界见证证明乘积为一并覆盖零成员', '定义非零域上的同号逆元并证明唯一性', '核有理相容及每次逆函数调用的非零条件'],
  'definitions': ['cutinv-positive-definition', 'cutinv-signed-unique'],
  'proved': [('IR1', 'cutinv-positive-definition', '正外点倒数候选的四条件与正性'),
             ('IR2', 'cutinv-positive-inverse', '正逆元的逐成员双包含'),
             ('IR3', 'cutinv-signed-unique', '全部非零分割逆元存在唯一及零无逆'),
             ('IR4', 'cutinv-rational-identities', '有理倒数相容、双逆及取反逆')],
  'questions': 'cutinv-q',
  'answer_prefix': 'cutinv-a',
  'not_covered': ['分割除法、方程全参数分类及完备有序域汇总（后续B2.30建立）',
                  '实数阿基米德性、实数稠密性、平方根及无理长度',
                  '柯西完备等价、完备有序域唯一同构、极限及连续性',
                  '一般分式运算体系、非线性方程及任意分割成员判定算法'],
  'prerequisites': [('manuscript/foundations/dedekind_addition.md', 'cutadd-grid'),
                    ('manuscript/foundations/dedekind_addition.md', 'cutadd-rational'),
                    ('manuscript/foundations/dedekind_addition.md', 'cutadd-separation'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-inverses'),
                    ('manuscript/foundations/dedekind_additive_order.md',
                     'cutgroup-negation-subtraction'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-definition'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-order-embedding'),
                    ('manuscript/foundations/dedekind_nonnegative_product.md', 'cutprod-basic-laws'),
                    ('manuscript/foundations/dedekind_nonnegative_product.md', 'cutprod-definition'),
                    ('manuscript/foundations/dedekind_nonnegative_product.md',
                     'cutprod-positive-witnesses'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-associative'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-definition'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-rational-zero'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-signs'),
                    ('manuscript/foundations/functions_definition.md', 'fun-definition'),
                    ('manuscript/foundations/functions_definition.md', 'fun-sets'),
                    ('manuscript/foundations/rational_gaps_bounds.md', 'qgap-density-archimedean'),
                    ('manuscript/foundations/rationals_division.md', 'rdiv-division'),
                    ('manuscript/foundations/rationals_multiplication.md', 'rmul-laws'),
                    ('manuscript/foundations/rationals_order.md', 'rord-division'),
                    ('manuscript/foundations/rationals_order.md', 'rord-multiplication'),
                    ('manuscript/foundations/rationals_order.md', 'rord-negation'),
                    ('manuscript/foundations/rationals_order.md', 'rord-reciprocal'),
                    ('manuscript/foundations/rationals_order.md', 'rord-translation')],
  'adopted_external': [('manuscript/foundations/dedekind_cuts_order.md',
                        'cut-set-background',
                        '沿用既有分割集合及条件子集背景；不以未证有序域、选择公理或实数阿基米德性为倒数构造先修')]},
 {'parent_code': '97Fxx',
  'parent_chapter_number': 526,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97F50'],
  'msc_cross_reference_codes': ['06A05', '06F25', '12J15'],
  'module_ids': ['number-systems'],
  'code': 'B2.30',
  'number': 51,
  'title': '分割除法、乘法方程与有序域',
  'anchor': 'cutdiv-unit',
  'body': 'manuscript/foundations/dedekind_division_field.md',
  'answers': 'manuscript/foundations/dedekind_division_field_answers.md',
  'goals': ['保留商的部分定义域并证明乘回', '在分割候选域重证方程三支及实际满射', '给正负分母双向比较并限制正倒数反序条件', '逐项汇总有序域与已有上确界性质并限定完备含义'],
  'definitions': ['cutdiv-definition', 'cutdiv-equations', 'cutdiv-complete-field'],
  'proved': [('DQ1', 'cutdiv-definition', '非零分母商、乘回及有理相容'),
             ('DQ2', 'cutdiv-equations', '分割方程全参数解集及非零乘法双射'),
             ('DQ3', 'cutdiv-order', '商的正负比较及正倒数反序'),
             ('DQ4', 'cutdiv-complete-field', '有序域与同一包含序上的上确界完备性')],
  'questions': 'cutdiv-q',
  'answer_prefix': 'cutdiv-a',
  'not_covered': ['实数阿基米德性、实数稠密性、平方根及无理长度', '柯西完备等价、完备有序域唯一同构、极限及连续性', '一般分式运算体系、非线性方程及任意分割成员判定算法'],
  'prerequisites': [('manuscript/foundations/dedekind_addition.md', 'cutadd-definition'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-inverses'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-laws'),
                    ('manuscript/foundations/dedekind_additive_order.md',
                     'cutgroup-negation-subtraction'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-translation'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-definition'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-order-embedding'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-supremum'),
                    ('manuscript/foundations/dedekind_inverse.md', 'cutinv-rational-identities'),
                    ('manuscript/foundations/dedekind_inverse.md', 'cutinv-signed-unique'),
                    ('manuscript/foundations/dedekind_nonnegative_product.md', 'cutprod-definition'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-cancellation'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-distributive'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-multiplication-order'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-associative'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-rational-zero'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-signs'),
                    ('manuscript/foundations/functions_bijections.md', 'bij-injective'),
                    ('manuscript/foundations/functions_bijections.md', 'bij-surjective'),
                    ('manuscript/foundations/functions_composition.md', 'fc-composition'),
                    ('manuscript/foundations/functions_composition.md', 'fc-equality'),
                    ('manuscript/foundations/functions_composition.md', 'fc-identity'),
                    ('manuscript/foundations/functions_definition.md', 'fun-definition'),
                    ('manuscript/foundations/functions_inverse.md', 'inv-two-sided'),
                    ('manuscript/foundations/linear_equations.md', 'lin-equivalence'),
                    ('manuscript/foundations/linear_equations.md', 'lin-solutions'),
                    ('manuscript/foundations/rational_gaps_bounds.md', 'qgap-density-archimedean'),
                    ('manuscript/foundations/rationals_division.md', 'rdiv-division')],
  'adopted_external': [('manuscript/foundations/dedekind_cuts_order.md',
                        'cut-set-background',
                        '沿用既有分割集合及条件子集背景；不以未证有序域、选择公理或实数阿基米德性为倒数构造先修')]}]


UNIT_SPECS += [{'parent_code': '97Fxx',
  'parent_chapter_number': 526,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97F50'],
  'msc_cross_reference_codes': ['06A05', '12J15'],
  'module_ids': ['number-systems'],
  'code': 'B2.31',
  'number': 52,
  'title': '实数的自然数界、阿基米德性质与有理稠密',
  'anchor': 'realarch-unit',
  'body': 'manuscript/foundations/real_archimedean_density.md',
  'answers': 'manuscript/foundations/real_archimedean_density_answers.md',
  'goals': ['区分三层嵌入并由外点给严格自然数界', '以合法实数除法证明正单位倍率与小倒数', '用两次取点分别见证稠密的严格两侧', '证明给定宽度夹逼及两侧误差而不宣称算法'],
  'definitions': ['realarch-embedding', 'realarch-scaled-reciprocal', 'realarch-rational-density'],
  'proved': [('RA1', 'realarch-natural-bound', '分割的严格自然数界及无上界性'),
             ('RA2', 'realarch-scaled-reciprocal', '正单位倍率和任意小正倒数'),
             ('RA3', 'realarch-rational-density', '有理像在分割间的严格稠密'),
             ('RA4', 'realarch-rational-brackets', '任意给定正宽度的有理夹逼')],
  'questions': 'realarch-q',
  'answer_prefix': 'realarch-a',
  'not_covered': ['非负平方根（后续B2.32独立从有序域与DC4证明）',
                  '一般实数幂、n次根、极限及连续性',
                  '柯西完备等价、完备有序域唯一同构',
                  '一般实数二次公式、实数绝对值距离与几何长度模型',
                  '任意分割成员判定、浮点开方或数值误差算法'],
  'prerequisites': [('manuscript/foundations/dedekind_addition.md', 'cutadd-rational'),
                    ('manuscript/foundations/dedekind_addition.md', 'cutadd-separation'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-laws'),
                    ('manuscript/foundations/dedekind_additive_order.md',
                     'cutgroup-negation-subtraction'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-translation'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-definition'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-gap'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-order-embedding'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-definition'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-order'),
                    ('manuscript/foundations/dedekind_inverse.md', 'cutinv-rational-identities'),
                    ('manuscript/foundations/dedekind_inverse.md', 'cutinv-signed-unique'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-distributive'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-multiplication-order'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-rational-zero'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-signs'),
                    ('manuscript/foundations/functions_composition.md', 'fc-composition'),
                    ('manuscript/foundations/functions_definition.md', 'fun-definition'),
                    ('manuscript/foundations/natural_order.md', 'ord-addition-order'),
                    ('manuscript/foundations/natural_order.md', 'ord-predecessor'),
                    ('manuscript/foundations/rational_gaps_bounds.md', 'qgap-density-archimedean'),
                    ('manuscript/foundations/rational_powers.md', 'pow-compatibility'),
                    ('manuscript/foundations/rationals_order_answers.md', 'rord-a08')],
  'adopted_external': [('manuscript/foundations/dedekind_cuts_order.md',
                        'cut-set-background',
                        '沿用已有分割集合及条件子集背景；不借外部已假设实数或阿基米德实例代替书内证明')]},
 {'parent_code': '97Fxx',
  'parent_chapter_number': 526,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97F50'],
  'msc_cross_reference_codes': ['06A05', '12J15'],
  'module_ids': ['number-systems'],
  'code': 'B2.32',
  'number': 53,
  'title': '非负实数平方根的存在唯一',
  'anchor': 'realsqrt-unit',
  'body': 'manuscript/foundations/real_square_roots.md',
  'answers': 'manuscript/foundations/real_square_roots_answers.md',
  'goals': ['由实数分配重建平方公式并限制比较域', '区分上界与最小性并完整证明两侧扰动', '存在唯一后才定义非负平方根函数', '证明平方方程解集穷尽及有理像之外的根'],
  'definitions': ['realsqrt-square-order',
                  'realsqrt-existence',
                  'realsqrt-function',
                  'realsqrt-equations-irrational'],
  'proved': [('RS1', 'realsqrt-square-order', '实数平方代数与非负比较反射'),
             ('RS2', 'realsqrt-existence', '上确界及双侧扰动给非负根存在'),
             ('RS3', 'realsqrt-function', '唯一非负根函数与有理部分根相容'),
             ('RS4', 'realsqrt-equations-irrational', '平方方程全解与二的非有理根')],
  'questions': 'realsqrt-q',
  'answer_prefix': 'realsqrt-a',
  'not_covered': ['一般实数幂、n次根、极限及连续性',
                  '柯西完备等价、完备有序域唯一同构',
                  '一般实数二次公式、实数绝对值距离与几何长度模型',
                  '任意分割成员判定、浮点开方或数值误差算法'],
  'prerequisites': [('manuscript/foundations/dedekind_addition.md', 'cutadd-definition'),
                    ('manuscript/foundations/dedekind_addition.md', 'cutadd-rational'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-inverses'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-laws'),
                    ('manuscript/foundations/dedekind_additive_order.md',
                     'cutgroup-negation-subtraction'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-translation'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-order-embedding'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-supremum'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-complete-field'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-definition'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-equations'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-order'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-cancellation'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-distributive'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-multiplication-order'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-associative'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-rational-zero'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-signs'),
                    ('manuscript/foundations/functions_definition.md', 'fun-definition'),
                    ('manuscript/foundations/functions_definition.md', 'fun-sets'),
                    ('manuscript/foundations/rational_square_equations.md', 'sqrat-root-uniqueness'),
                    ('manuscript/foundations/rational_square_equations.md', 'sqrat-two-not-square')],
  'adopted_external': [('manuscript/foundations/dedekind_cuts_order.md',
                        'cut-set-background',
                        '沿用已有分割集合及条件子集背景；不借外部已假设实数或阿基米德实例代替书内证明')]}]


UNIT_SPECS += [{'parent_code': '97Fxx',
  'parent_chapter_number': 526,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97F50'],
  'msc_cross_reference_codes': ['54E35'],
  'module_ids': ['number-systems'],
  'code': 'B2.33',
  'number': 54,
  'title': '实数绝对值与线上的距离',
  'anchor': 'realabs-unit',
  'body': 'manuscript/foundations/real_absolute_distance.md',
  'answers': 'manuscript/foundations/real_absolute_distance_answers.md',
  'goals': ['从实数全序定义非负幅度并证明唯一', '逐步证明三角反三角及零与异号边界', '在实数有序对上定义距离并核四性质', '分类全部半径条件并以根唯一性连接绝对值'],
  'definitions': ['realabs-definition-bounds',
                  'realabs-products-triangle',
                  'realabs-distance',
                  'realabs-error-root'],
  'proved': [('RAV1', 'realabs-definition-bounds', '实数绝对值与全参数双侧界'),
             ('RAV2', 'realabs-products-triangle', '乘商、三角反三角及完整等号条件'),
             ('RAV3', 'realabs-distance', '线距四性质及平移倍率'),
             ('RAV4', 'realabs-error-root', '距离条件全部分支及平方根连接')],
  'questions': 'realabs-q',
  'answer_prefix': 'realabs-a',
  'not_covered': ['实坐标平面、欧氏距离与几何长度模型', '一般度量空间与度量化理论', '一般实形式多项式、高次方程、极限与微分', '任意分割成员判定或数值近似算法'],
  'prerequisites': [('manuscript/foundations/dedekind_addition.md', 'cutadd-rational'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-inverses'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-laws'),
                    ('manuscript/foundations/dedekind_additive_order.md',
                     'cutgroup-negation-subtraction'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-translation'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-order-embedding'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-definition'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-equations'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-distributive'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-multiplication-order'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-associative'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-rational-zero'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-signs'),
                    ('manuscript/foundations/functions_definition.md', 'fun-definition'),
                    ('manuscript/foundations/functions_definition.md', 'fun-pairs'),
                    ('manuscript/foundations/functions_definition.md', 'fun-sets'),
                    ('manuscript/foundations/rationals_absolute.md', 'rabs-definition'),
                    ('manuscript/foundations/real_square_roots.md', 'realsqrt-equations-irrational'),
                    ('manuscript/foundations/real_square_roots.md', 'realsqrt-function'),
                    ('manuscript/foundations/real_square_roots.md', 'realsqrt-square-order')],
  'adopted_external': [('manuscript/foundations/functions_definition.md', 'fun-sets', '沿用给定集合按条件取子集的背景'),
                       ('manuscript/foundations/functions_definition.md',
                        'fun-definition',
                        '沿用函数域、目标与唯一输出约定')]},
 {'parent_code': '97Hxx',
  'parent_chapter_number': 528,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97H30'],
  'msc_cross_reference_codes': ['97H20'],
  'module_ids': ['real-algebra-equations'],
  'code': 'B2.34',
  'number': 55,
  'title': '实数二次方程与配方界',
  'anchor': 'realquad-unit',
  'body': 'manuscript/foundations/real_quadratic_equations.md',
  'answers': 'manuscript/foundations/real_quadratic_equations_answers.md',
  'goals': ['用真实实数运算重证配方并核每个分母', '证明判别式等价及两个复合恢复输入', '穷尽零系数和判别式三分支并核存在', '区分全局界输出与唯一达到输入'],
  'definitions': ['realquad-completion',
                  'realquad-discriminant',
                  'realquad-solutions',
                  'realquad-bounds'],
  'proved': [('RQ1', 'realquad-completion', '合法分母与实数配方'),
             ('RQ2', 'realquad-discriminant', '判别式恒等式及可逆仿射换元'),
             ('RQ3', 'realquad-solutions', '全部参数实数解集与两根次序'),
             ('RQ4', 'realquad-bounds', '配方全局界及唯一达到输入')],
  'questions': 'realquad-q',
  'answer_prefix': 'realquad-a',
  'not_covered': ['实坐标平面、欧氏距离与几何长度模型', '一般度量空间与度量化理论', '一般实形式多项式、高次方程、极限与微分', '任意分割成员判定或数值近似算法'],
  'prerequisites': [('manuscript/foundations/dedekind_addition.md', 'cutadd-definition'),
                    ('manuscript/foundations/dedekind_addition.md', 'cutadd-rational'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-inverses'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-laws'),
                    ('manuscript/foundations/dedekind_additive_order.md',
                     'cutgroup-negation-subtraction'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-translation'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-order-embedding'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-definition'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-equations'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-order'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-cancellation'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-distributive'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-multiplication-order'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-associative'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-rational-zero'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-signs'),
                    ('manuscript/foundations/functions_composition.md', 'fc-composition'),
                    ('manuscript/foundations/functions_composition.md', 'fc-equality'),
                    ('manuscript/foundations/functions_definition.md', 'fun-definition'),
                    ('manuscript/foundations/functions_definition.md', 'fun-sets'),
                    ('manuscript/foundations/real_square_roots.md', 'realsqrt-equations-irrational'),
                    ('manuscript/foundations/real_square_roots.md', 'realsqrt-existence'),
                    ('manuscript/foundations/real_square_roots.md', 'realsqrt-function'),
                    ('manuscript/foundations/real_square_roots.md', 'realsqrt-square-order')],
  'adopted_external': [('manuscript/foundations/functions_definition.md', 'fun-sets', '沿用给定集合按条件取子集的背景'),
                       ('manuscript/foundations/functions_definition.md',
                        'fun-definition',
                        '沿用函数域、目标与唯一输出约定')],
  'structural_comparisons': [('manuscript/foundations/rational_quadratic_equations.md',
                              'quad-completion',
                              '旧有理配方仅作结构对照，不作为实数定理先修')]}]


UNIT_SPECS += [{'parent_code': '97Gxx',
  'parent_chapter_number': 527,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97G70'],
  'msc_cross_reference_codes': ['51N10'],
  'module_ids': ['real-plane-geometry'],
  'code': 'B2.35',
  'number': 56,
  'title': '实数坐标、位移与仿射参数',
  'anchor': 'realplane-unit',
  'body': 'manuscript/foundations/real_plane_affine.md',
  'answers': 'manuscript/foundations/real_plane_affine_answers.md',
  'goals': ['区分点、位移与分量的类型', '逐分量证明所需运算和平移双逆', '使用至少一个非零方向分量恢复参数', '证明线段端点退化换向及等位移中点唯一'],
  'definitions': ['realplane-model', 'realplane-operations', 'realplane-lines', 'realplane-segments'],
  'proved': [('RP1', 'realplane-model', '实坐标点、投影、轴及有理坐标嵌入'),
             ('RP2', 'realplane-operations', '分量运算与点平移'),
             ('RP3', 'realplane-lines', '非零方向参数单射与直线成员'),
             ('RP4', 'realplane-segments', '线段换向与等位移中点唯一性')],
  'questions': 'realplane-q',
  'answer_prefix': 'realplane-a',
  'not_covered': ['角度、垂直、面积及完整欧氏公理模型', '一般向量空间、内积空间与度量化', '三角取等号的完整分类与线段距离逆命题', '任意分割成员判定或数值计算算法'],
  'prerequisites': [('manuscript/foundations/dedekind_addition.md', 'cutadd-definition'),
                    ('manuscript/foundations/dedekind_addition.md', 'cutadd-rational'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-inverses'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-laws'),
                    ('manuscript/foundations/dedekind_additive_order.md',
                     'cutgroup-negation-subtraction'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-translation'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-order-embedding'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-definition'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-equations'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-order'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-cancellation'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-distributive'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-associative'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-definition'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-rational-zero'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-signs'),
                    ('manuscript/foundations/functions_bijections.md', 'bij-injective'),
                    ('manuscript/foundations/functions_bijections.md', 'bij-surjective'),
                    ('manuscript/foundations/functions_composition.md', 'fc-composition'),
                    ('manuscript/foundations/functions_composition.md', 'fc-equality'),
                    ('manuscript/foundations/functions_composition.md', 'fc-identity'),
                    ('manuscript/foundations/functions_definition.md', 'fun-definition'),
                    ('manuscript/foundations/functions_definition.md', 'fun-image'),
                    ('manuscript/foundations/functions_definition.md', 'fun-pairs'),
                    ('manuscript/foundations/functions_definition.md', 'fun-sets'),
                    ('manuscript/foundations/functions_inverse.md', 'inv-two-sided'),
                    ('manuscript/foundations/real_square_roots.md', 'realsqrt-equations-irrational')],
  'adopted_external': [('manuscript/foundations/functions_definition.md', 'fun-sets', '沿用给定集合按条件取子集的背景'),
                       ('manuscript/foundations/functions_definition.md',
                        'fun-pairs',
                        '沿用有序对逐位置相等与集合积')]},
 {'parent_code': '97Gxx',
  'parent_chapter_number': 527,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97G70'],
  'msc_cross_reference_codes': ['54E35'],
  'module_ids': ['real-plane-geometry'],
  'code': 'B2.36',
  'number': 57,
  'title': '平面距离、平方和与三角不等式',
  'anchor': 'planedist-unit',
  'body': 'manuscript/foundations/real_plane_distance.md',
  'answers': 'manuscript/foundations/real_plane_distance_answers.md',
  'goals': ['先核根域与非负条件再用平方比较', '含零标量证明范数倍率与三角', '逐坐标推出点距四性质和平移倍率', '核参数线段退化端点及中点距离并限定正向结论'],
  'definitions': ['planedist-cauchy',
                  'planedist-norm-laws',
                  'planedist-metric',
                  'planedist-segment-distances'],
  'proved': [('PD1', 'planedist-cauchy', '二维平方恒等式与乘积界'),
             ('PD2', 'planedist-norm-laws', '范数零倍率三角及反三角'),
             ('PD3', 'planedist-metric', '欧氏点距四性质及变换'),
             ('PD4', 'planedist-segment-distances', '精确距离与线段参数距离')],
  'questions': 'planedist-q',
  'answer_prefix': 'planedist-a',
  'not_covered': ['角度、垂直、面积及完整欧氏公理模型', '一般向量空间、内积空间与度量化', '三角取等号的完整分类与线段距离逆命题', '任意分割成员判定或数值计算算法'],
  'prerequisites': [('manuscript/foundations/dedekind_addition.md', 'cutadd-rational'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-laws'),
                    ('manuscript/foundations/dedekind_additive_order.md',
                     'cutgroup-negation-subtraction'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-translation'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-order-embedding'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-definition'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-equations'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-distributive'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-multiplication-order'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-associative'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-rational-zero'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-signs'),
                    ('manuscript/foundations/functions_bijections.md', 'bij-bijective'),
                    ('manuscript/foundations/functions_bijections.md', 'bij-injective'),
                    ('manuscript/foundations/functions_definition.md', 'fun-definition'),
                    ('manuscript/foundations/functions_definition.md', 'fun-pairs'),
                    ('manuscript/foundations/real_absolute_distance.md', 'realabs-definition-bounds'),
                    ('manuscript/foundations/real_absolute_distance.md', 'realabs-distance'),
                    ('manuscript/foundations/real_absolute_distance.md', 'realabs-error-root'),
                    ('manuscript/foundations/real_absolute_distance.md', 'realabs-products-triangle'),
                    ('manuscript/foundations/real_plane_affine.md', 'realplane-model'),
                    ('manuscript/foundations/real_plane_affine.md', 'realplane-operations'),
                    ('manuscript/foundations/real_plane_affine.md', 'realplane-segments'),
                    ('manuscript/foundations/real_square_roots.md', 'realsqrt-equations-irrational'),
                    ('manuscript/foundations/real_square_roots.md', 'realsqrt-function'),
                    ('manuscript/foundations/real_square_roots.md', 'realsqrt-square-order')],
  'adopted_external': [('manuscript/foundations/functions_definition.md', 'fun-sets', '沿用给定集合按条件取子集的背景'),
                       ('manuscript/foundations/functions_definition.md',
                        'fun-pairs',
                        '沿用有序对逐位置相等与集合积')]}]


UNIT_SPECS += [{'parent_code': '97Gxx',
  'parent_chapter_number': 527,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97G70'],
  'msc_cross_reference_codes': ['51N10'],
  'module_ids': ['real-plane-geometry'],
  'code': 'B2.37',
  'number': 58,
  'title': '参数直线、一次方程与交点',
  'anchor': 'planeline-unit',
  'body': 'manuscript/foundations/real_plane_lines.md',
  'answers': 'manuscript/foundations/real_plane_lines_answers.md',
  'goals': ['区分表达式全域与非零方向比例判据', '构造一般一次方程的基点与方向并处理退化', '用两个包含证明线集合唯一而非参数唯一', '先必要消元再充分乘回并穷尽交会分类'],
  'definitions': ['planeline-determinant',
                  'planeline-equation',
                  'planeline-uniqueness',
                  'planeline-intersections'],
  'proved': [('PL1', 'planeline-determinant', '二维表达式与固定非零方向比例判据'),
             ('PL2', 'planeline-equation', '参数直线与一次方程全部系数分支'),
             ('PL3', 'planeline-uniqueness', '两点唯一线集合及表示变化'),
             ('PL4', 'planeline-intersections', '相交重合不交及方向平行表示无关')],
  'questions': 'planeline-q',
  'answer_prefix': 'planeline-a',
  'not_covered': ['角度测量、面积与完整欧氏公理模型', '一般矩阵、行列式及内积空间理论', '一般优化或下确界投影构造', '任意分割成员判定或数值计算算法'],
  'prerequisites': [('manuscript/foundations/dedekind_addition.md', 'cutadd-rational'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-laws'),
                    ('manuscript/foundations/dedekind_additive_order.md',
                     'cutgroup-negation-subtraction'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-order-embedding'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-definition'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-equations'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-cancellation'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-distributive'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-associative'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-rational-zero'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-signs'),
                    ('manuscript/foundations/functions_definition.md', 'fun-definition'),
                    ('manuscript/foundations/functions_definition.md', 'fun-pairs'),
                    ('manuscript/foundations/functions_definition.md', 'fun-sets'),
                    ('manuscript/foundations/real_plane_affine.md', 'realplane-lines'),
                    ('manuscript/foundations/real_plane_affine.md', 'realplane-model'),
                    ('manuscript/foundations/real_plane_affine.md', 'realplane-operations')],
  'adopted_external': [('manuscript/foundations/functions_definition.md', 'fun-sets', '沿用条件子集与外延相等背景'),
                       ('manuscript/foundations/functions_definition.md',
                        'fun-pairs',
                        '沿用有序对逐位置相等与集合积')]},
 {'parent_code': '97Gxx',
  'parent_chapter_number': 527,
  'part_code': '97-XX',
  'msc_leaf_codes': ['97G70'],
  'msc_cross_reference_codes': ['51N20'],
  'module_ids': ['real-plane-geometry'],
  'code': 'B2.38',
  'number': 59,
  'title': '正交、投影与最近点',
  'anchor': 'planeproj-unit',
  'body': 'manuscript/foundations/real_plane_projection.md',
  'answers': 'manuscript/foundations/real_plane_projection_answers.md',
  'goals': ['逐两分量证明内积律并保留零正交', '先验分母正再构造并核唯一垂足', '从任意线上点平方差证明最近点及等号唯一', '定义独立点到线函数并以乘回核距离公式'],
  'definitions': ['planeproj-inner-orthogonal',
                  'planeproj-foot',
                  'planeproj-nearest',
                  'planeproj-line-distance'],
  'proved': [('PP1', 'planeproj-inner-orthogonal', '二维内积规律与全部正交方向'),
             ('PP2', 'planeproj-foot', '正分母垂足存在唯一及线上退化'),
             ('PP3', 'planeproj-nearest', '勾股双向与最近点平方差和唯一'),
             ('PP4', 'planeproj-line-distance', '点到线函数及一般公式和系数缩放')],
  'questions': 'planeproj-q',
  'answer_prefix': 'planeproj-a',
  'not_covered': ['角度测量、面积与完整欧氏公理模型', '一般矩阵、行列式及内积空间理论', '一般优化或下确界投影构造', '任意分割成员判定或数值计算算法'],
  'prerequisites': [('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-laws'),
                    ('manuscript/foundations/dedekind_additive_order.md',
                     'cutgroup-negation-subtraction'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-translation'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-definition'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-equations'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-cancellation'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-distributive'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-multiplication-order'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-associative'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-rational-zero'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-signs'),
                    ('manuscript/foundations/functions_definition.md', 'fun-definition'),
                    ('manuscript/foundations/functions_definition.md', 'fun-pairs'),
                    ('manuscript/foundations/real_absolute_distance.md', 'realabs-definition-bounds'),
                    ('manuscript/foundations/real_absolute_distance.md', 'realabs-products-triangle'),
                    ('manuscript/foundations/real_plane_affine.md', 'realplane-lines'),
                    ('manuscript/foundations/real_plane_affine.md', 'realplane-model'),
                    ('manuscript/foundations/real_plane_affine.md', 'realplane-operations'),
                    ('manuscript/foundations/real_plane_distance.md', 'planedist-cauchy'),
                    ('manuscript/foundations/real_plane_distance.md', 'planedist-metric'),
                    ('manuscript/foundations/real_plane_distance.md', 'planedist-norm-laws'),
                    ('manuscript/foundations/real_plane_lines.md', 'planeline-determinant'),
                    ('manuscript/foundations/real_plane_lines.md', 'planeline-equation'),
                    ('manuscript/foundations/real_square_roots.md', 'realsqrt-function'),
                    ('manuscript/foundations/real_square_roots.md', 'realsqrt-square-order')],
  'adopted_external': [('manuscript/foundations/functions_definition.md', 'fun-sets', '沿用条件子集与外延相等背景'),
                       ('manuscript/foundations/functions_definition.md',
                        'fun-pairs',
                        '沿用有序对逐位置相等与集合积')]}]


UNIT_SPECS += [{'parent_code': '40Axx',
  'parent_chapter_number': 242,
  'part_code': '40-XX',
  'msc_leaf_codes': ['40A05'],
  'msc_cross_reference_codes': ['26A03', '97I30'],
  'module_ids': ['single-analysis'],
  'code': 'B4.1',
  'number': 60,
  'title': '实数数列、收敛定义与基本例',
  'anchor': 'seq-unit',
  'body': 'manuscript/foundations/real_sequences_limits.md',
  'answers': 'manuscript/foundations/real_sequences_limits_answers.md',
  'goals': ['区分全函数、像集合与有限样本', '正确排列误差阈值和全尾量词及其否定', '从定义证明基本例与最早严格阈值', '核自然差合法性并证明尾移双向及交替反例'],
  'definitions': ['seq-definition', 'seq-uniqueness', 'seq-basic-limits', 'seq-tails'],
  'proved': [('SL1', 'seq-definition', '全函数与收敛量词'),
             ('SL2', 'seq-uniqueness', '双阈值与极限唯一'),
             ('SL3', 'seq-basic-limits', '常数倒数与严格阈值'),
             ('SL4', 'seq-tails', '最终相同、尾移与余数交替例')],
  'questions': 'seq-q',
  'answer_prefix': 'seq-a',
  'not_covered': ['B3自然数形式构造与递归原则证明', '单调收敛、子列及级数', '函数极限、连续、微分与积分', '任意实数的数值实现或无限测试'],
  'prerequisites': [('manuscript/foundations/dedekind_addition.md', 'cutadd-rational'),
                    ('manuscript/foundations/dedekind_additive_order.md',
                     'cutgroup-negation-subtraction'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-translation'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-definition'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-equations'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-order'),
                    ('manuscript/foundations/dedekind_inverse.md', 'cutinv-rational-identities'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-multiplication-order'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-rational-zero'),
                    ('manuscript/foundations/division_remainder.md', 'div-quotient-remainder'),
                    ('manuscript/foundations/division_remainder.md', 'div-theorem'),
                    ('manuscript/foundations/functions_composition.md', 'fc-composition'),
                    ('manuscript/foundations/functions_definition.md', 'fun-definition'),
                    ('manuscript/foundations/functions_definition.md', 'fun-pairs'),
                    ('manuscript/foundations/functions_definition.md', 'fun-sets'),
                    ('manuscript/foundations/natural_numbers.md', 'b1-addition-associative'),
                    ('manuscript/foundations/natural_numbers.md', 'b1-addition-commutative'),
                    ('manuscript/foundations/natural_numbers.md', 'b1-addition-definition'),
                    ('manuscript/foundations/natural_numbers.md', 'b1-induction'),
                    ('manuscript/foundations/natural_order.md', 'ord-addition-order'),
                    ('manuscript/foundations/natural_order.md', 'ord-definition'),
                    ('manuscript/foundations/natural_order.md', 'ord-successor-comparison'),
                    ('manuscript/foundations/natural_order.md', 'ord-trichotomy'),
                    ('manuscript/foundations/natural_subtraction.md', 'sub-definition'),
                    ('manuscript/foundations/place_value.md', 'b1-multiplication-commutative'),
                    ('manuscript/foundations/place_value.md', 'b1-multiplication-units'),
                    ('manuscript/foundations/real_absolute_distance.md', 'realabs-definition-bounds'),
                    ('manuscript/foundations/real_absolute_distance.md', 'realabs-products-triangle'),
                    ('manuscript/foundations/real_archimedean_density.md', 'realarch-embedding'),
                    ('manuscript/foundations/real_archimedean_density.md', 'realarch-natural-bound')],
  'adopted_external': [('manuscript/foundations/natural_numbers.md',
                        'b1-induction',
                        '公开采用自然归纳规则，未宣称B3课程完成'),
                       ('manuscript/foundations/natural_numbers.md',
                        'b1-recursion-principle',
                        '公开采用固定更新递归原则'),
                       ('manuscript/foundations/functions_definition.md', 'fun-sets', '沿用条件子集与外延相等背景')]},
 {'parent_code': '40Axx',
  'parent_chapter_number': 242,
  'part_code': '40-XX',
  'msc_leaf_codes': ['40A05'],
  'msc_cross_reference_codes': ['26A03', '97I30'],
  'module_ids': ['single-analysis'],
  'code': 'B4.2',
  'number': 61,
  'title': '收敛数列的界与四则运算',
  'anchor': 'seqlaw-unit',
  'body': 'manuscript/foundations/real_sequences_algebra.md',
  'answers': 'manuscript/foundations/real_sequences_algebra_answers.md',
  'goals': ['用固定状态递归证明空前缀在内的统一界', '分别处理常数零和非零并使用反三角', '先取全列界再选正误差系数证明乘积', '区分最终非零与全项非零并完整构造倒数商全列'],
  'definitions': ['seqlaw-bounded',
                  'seqlaw-linear-absolute',
                  'seqlaw-product',
                  'seqlaw-reciprocal-quotient'],
  'proved': [('SA1', 'seqlaw-bounded', '固定递归前缀界与收敛有界'),
             ('SA2', 'seqlaw-linear-absolute', '和差常数倍及绝对值极限'),
             ('SA3', 'seqlaw-product', '正统一系数的乘积估计'),
             ('SA4', 'seqlaw-reciprocal-quotient', '最终非零、早期填值及合法商')],
  'questions': 'seqlaw-q',
  'answer_prefix': 'seqlaw-a',
  'not_covered': ['B3自然数形式构造与递归原则证明', '单调收敛、子列及级数', '函数极限、连续、微分与积分', '任意实数的数值实现或无限测试'],
  'prerequisites': [('manuscript/foundations/dedekind_addition.md', 'cutadd-rational'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-laws'),
                    ('manuscript/foundations/dedekind_additive_order.md',
                     'cutgroup-negation-subtraction'),
                    ('manuscript/foundations/dedekind_additive_order.md', 'cutgroup-translation'),
                    ('manuscript/foundations/dedekind_cuts_order.md', 'cut-order-embedding'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-definition'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-equations'),
                    ('manuscript/foundations/dedekind_division_field.md', 'cutdiv-order'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-distributive'),
                    ('manuscript/foundations/dedekind_ring_order.md', 'cutring-multiplication-order'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-associative'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-rational-zero'),
                    ('manuscript/foundations/dedekind_signed_product.md', 'cutsigned-signs'),
                    ('manuscript/foundations/functions_definition.md', 'fun-definition'),
                    ('manuscript/foundations/functions_definition.md', 'fun-pairs'),
                    ('manuscript/foundations/functions_definition.md', 'fun-sets'),
                    ('manuscript/foundations/natural_numbers.md', 'b1-add-one'),
                    ('manuscript/foundations/natural_numbers.md', 'b1-induction'),
                    ('manuscript/foundations/natural_numbers.md', 'b1-recursion-principle'),
                    ('manuscript/foundations/natural_order.md', 'ord-successor-comparison'),
                    ('manuscript/foundations/natural_order.md', 'ord-trichotomy'),
                    ('manuscript/foundations/real_absolute_distance.md', 'realabs-definition-bounds'),
                    ('manuscript/foundations/real_absolute_distance.md', 'realabs-products-triangle'),
                    ('manuscript/foundations/real_archimedean_density.md', 'realarch-embedding'),
                    ('manuscript/foundations/real_archimedean_density.md', 'realarch-natural-bound'),
                    ('manuscript/foundations/real_sequences_limits.md', 'seq-basic-limits'),
                    ('manuscript/foundations/real_sequences_limits.md', 'seq-definition'),
                    ('manuscript/foundations/real_sequences_limits.md', 'seq-tails'),
                    ('manuscript/foundations/real_sequences_limits.md', 'seq-uniqueness')],
  'adopted_external': [('manuscript/foundations/natural_numbers.md',
                        'b1-induction',
                        '公开采用自然归纳规则，未宣称B3课程完成'),
                       ('manuscript/foundations/natural_numbers.md',
                        'b1-recursion-principle',
                        '公开采用固定更新递归原则'),
                       ('manuscript/foundations/functions_definition.md', 'fun-sets', '沿用条件子集与外延相等背景')]}]


def anchor_ref(root, path, anchor):
    text = (root/path).read_text() if (root/path).is_file() else ''
    found = '{#'+anchor+'}' in text or 'id="'+anchor+'"' in text
    return {'path': path, 'anchor': anchor, 'reference': path+'#'+anchor,
            'status': 'present' if found else 'missing',
            'source_sha256': digest(root/path) if (root/path).is_file() else None}


def unit_records(root):
    units = []
    for spec in UNIT_SPECS:
        row = {'code':spec['code'],'title_zh':spec['title'],
               'parent_code':spec.get('parent_code','11Axx'),'level':'foundation_bridge_unit'}
        unit = record(root,row,spec['number'],spec.get('part_code','11-XX'),[spec['body'],spec['answers']],
                      [spec['body']],'registered_unit_draft')
        unit['unit_id'] = spec['anchor']
        unit['parent_chapter_number'] = spec.get('parent_chapter_number',26)
        unit['msc_leaf_codes'] = spec.get('msc_leaf_codes',[])
        unit['msc_cross_reference_codes'] = spec.get('msc_cross_reference_codes',[])
        unit['cross_classification_scope'] = '交叉定位不重复登记正文，也不授予交叉章或叶的完成状态'
        unit['classification_note'] = ('基础教学桥接单元，定位'+','.join(unit['msc_leaf_codes'])+'；不新增MSC章／节，不表示其所属章或叶完整覆盖'
                                       if unit['msc_leaf_codes'] else
                                       '基础桥接单元，不新增MSC章／节；不表示11A05或11A63完整覆盖')
        unit['planned_source_files'] = [spec['body'],spec['answers']]
        unit['unit_anchor'] = anchor_ref(root,spec['body'],spec['anchor'])
        unit['learning_objectives'] = {'status':'defined_for_unit','items':spec['goals']}
        unit['learning_entry'].update(status='registered_precise_prerequisites',
            module_ids=spec['module_ids'],prerequisite_definition_anchors=[
                anchor_ref(root,path,anchor) for path,anchor in spec['prerequisites']])
        unit['learning_entry']['adopted_assumptions'] = [
            {**anchor_ref(root,spec['body'],anchor),'title':title}
            for anchor,title in spec.get('adopted',[])] + [
            {**anchor_ref(root,path,anchor),'title':title}
            for path,anchor,title in spec.get('adopted_external',[])]
        unit['cross_references']['adopted'] = unit['learning_entry']['adopted_assumptions']
        unit['cross_references']['proved'] = [
            {**anchor_ref(root,spec['body'],anchor),'proposition':pid,'title':title,
             'claim_status':'proof_in_draft_not_automatic_review_approval'}
            for pid,anchor,title in spec['proved']]
        if spec.get('structural_comparisons'):
            unit['cross_references']['structural_comparisons_not_prerequisites'] = [
                {**anchor_ref(root,path,anchor),'role':role}
                for path,anchor,role in spec['structural_comparisons']]
        unit['definition_anchors'] = [anchor_ref(root,spec['body'],a) for a in spec['definitions']]
        unit['depth_plan'] = {'status':'defined_for_unit',
            'per_objective_depth':[{'objective':goal,'depth':'T_complete_teaching'} for goal in spec['goals']],
            'boundary':'完整教学的目标范围仅限本单元；独立审阅状态另外记录'}
        unit['coverage']['unwritten_topics'] = spec['not_covered']
        pairs = [{'question':anchor_ref(root,spec['body'],spec['questions']+f'{i:02}'),
                  'answer':anchor_ref(root,spec['answers'],spec['answer_prefix']+f'{i:02}')}
                 for i in range(1,9)]
        unit['exercise_answer_separation'].update(
            paired_ids_verified=all(x[k]['status']=='present' for x in pairs for k in ['question','answer']),
            pairs=pairs)
        if unit['exercise_answer_separation']['paired_ids_verified']:
            unit['exercise_answer_separation']['status']='anchors_paired_content_review_separate'
        unit['source_verification']['candidate_records'] = evidence(root,[
            'research/production/foundations_sources_2026-10-27.json',
            'research/production/foundations_sources_2026-10-27.md'] + ([
            'research/production/integers_sources_2026-10-27.md',
            'research/production/integers_sources_2026-10-27.json'] if spec['number'] >= 7 else []) + ([
            'research/production/divisibility_sources_2026-10-27.md',
            'research/production/divisibility_sources_2026-10-27.json'] if spec['number'] >= 9 else []) + ([
            'research/production/bezout_sources_2026-10-27.md',
            'research/production/bezout_sources_2026-10-27.json'] if spec['number'] >= 12 else []) + ([
            'research/production/rationals_sources_2026-10-27.md',
            'research/production/rationals_sources_2026-10-27.json'] if spec['number'] >= 14 else []) + ([
            'research/production/rationals_multiplication_sources_2026-10-27.md',
            'research/production/rationals_multiplication_sources_2026-10-27.json'] if spec['number'] >= 16 else []) + ([
            'research/production/rationals_order_sources_2026-10-27.md',
            'research/production/rationals_order_sources_2026-10-27.json'] if spec['number'] >= 18 else []) + ([
            'research/production/ratios_units_sources_2026-10-27.md',
            'research/production/ratios_units_sources_2026-10-27.json'] if spec['number'] >= 20 else []) + ([
            'research/production/functions_sources_2026-10-29.md',
            'research/production/functions_sources_2026-10-29.json'] if spec['number'] >= 22 else []) + ([
            'research/production/inverse_functions_sources_2026-10-29.md',
            'research/production/inverse_functions_sources_2026-10-29.json'] if spec['number'] >= 24 else []) + ([
            'research/production/linear_equations_sources_2026-10-29.md',
            'research/production/linear_equations_sources_2026-10-29.json'] if spec['number'] >= 26 else []) + ([
            'research/production/linear_inequalities_sources_2026-10-29.md',
            'research/production/linear_inequalities_sources_2026-10-29.json'] if spec['number'] >= 28 else []) + ([
            'research/production/coordinates_affine_sources_2026-10-29.md',
            'research/production/coordinates_affine_sources_2026-10-29.json'] if spec['number'] >= 30 else []) + ([
            'research/production/powers_sums_sources_2026-10-29.md',
            'research/production/powers_sums_sources_2026-10-29.json'] if spec['number'] >= 32 else []) + ([
            'research/production/polynomial_basic_sources_2026-10-29.md',
            'research/production/polynomial_basic_sources_2026-10-29.json'] if spec['number'] >= 34 else []) + ([
            'research/production/polynomial_product_sources_2026-10-29.md',
            'research/production/polynomial_product_sources_2026-10-29.json'] if spec['number'] >= 36 else []) + ([
            'research/production/polynomial_linear_division_sources_2026-10-29.md',
            'research/production/polynomial_linear_division_sources_2026-10-29.json'] if spec['number'] >= 38 else []) + ([
            'research/production/rational_quadratic_sources_2026-10-29.md',
            'research/production/rational_quadratic_sources_2026-10-29.json'] if spec['number'] >= 40 else []) + ([
            'research/production/rational_gaps_cuts_sources_2026-10-29.md',
            'research/production/rational_gaps_cuts_sources_2026-10-29.json'] if spec['number'] >= 42 else []) + ([
            'research/production/dedekind_addition_sources_2026-10-29.md',
            'research/production/dedekind_addition_sources_2026-10-29.json'] if spec['number'] >= 44 else []) + ([
            'research/production/dedekind_multiplication_sources_2026-10-30.md',
            'research/production/dedekind_multiplication_sources_2026-10-30.json'] if spec['number'] >= 46 else []) + ([
            'research/production/dedekind_signed_sources_2026-10-30.md',
            'research/production/dedekind_signed_sources_2026-10-30.json'] if spec['number'] >= 48 else []) + ([
            'research/production/dedekind_inverse_sources_2026-10-30.md',
            'research/production/dedekind_inverse_sources_2026-10-30.json'] if spec['number'] >= 50 else []) + ([
            'research/production/real_arch_sqrt_sources_2026-10-30.md',
            'research/production/real_arch_sqrt_sources_2026-10-30.json'] if spec['number'] >= 52 else []) + ([
            'research/production/real_distance_quadratic_sources_2026-10-30.md',
            'research/production/real_distance_quadratic_sources_2026-10-30.json'] if spec['number'] >= 54 else []) + ([
            'research/production/real_plane_metric_sources_2026-10-30.md',
            'research/production/real_plane_metric_sources_2026-10-30.json'] if spec['number'] >= 56 else []) + ([
            'research/production/real_lines_projection_sources_2026-10-30.md',
            'research/production/real_lines_projection_sources_2026-10-30.json'] if spec['number'] >= 58 else []) + ([
            'research/production/real_sequences_sources_2026-10-30.md',
            'research/production/real_sequences_sources_2026-10-30.json'] if spec['number'] >= 60 else []))
        units.append(unit)
    return units



def aggregate_build_reviews(root, doc, path, targets):
    """Adapt the batch builder's aggregate report only after an actual visual signoff."""
    visual=doc.get('visual_review',{})
    if doc.get('status') not in ['automated_checks_passed','passed','accepted']:
        raise ValueError('Batch automated checks are not passed')
    if visual.get('status')!='accepted' or visual.get('result')!='passed':
        raise ValueError('Actual visual inspection has not been explicitly accepted')
    if not all(isinstance(visual.get(k),str) and visual[k].strip() for k in ['reviewer','reviewed_at']):
        raise ValueError('Named and dated visual reviewer required')
    outputs=doc.get('artifact_sha256',{})
    if not isinstance(outputs,dict) or not outputs:
        raise ValueError('Batch artifact hashes required')
    pdfs=[p for p in outputs if p.lower().endswith('.pdf')]
    if not pdfs:
        raise ValueError('No built PDF artifact registered')
    shots=[]
    for pdf in pdfs:
        if visual.get('artifact_sha256',{}).get(pdf)!=outputs[pdf]:
            raise ValueError('Visual approval does not identify the current PDF: '+pdf)
        pages=visual.get('pages',{}).get(pdf)
        if not isinstance(pages,list) or not pages:
            raise ValueError('Actual screenshot records required for '+pdf)
        for shot in pages:
            if not isinstance(shot,dict) or not isinstance(shot.get('page'),int) or shot['page']<1:
                raise ValueError('Screenshot must identify its positive PDF page number')
            sp=(root/shot['path']).resolve()
            if not sp.is_relative_to(root) or not sp.is_file() or shot.get('sha256')!=digest(sp):
                raise ValueError('Screenshot missing or its hash is stale')
            shots.append({'path':shot['path'],'sha256':shot['sha256']})
    source=doc.get('source_sha256',{})
    if not isinstance(source,dict) or not source:
        raise ValueError('Batch source hash mapping required')
    # A manuscript can stay unchanged while its renderer, algorithm or test
    # changes. Such a report does not certify the current build inputs.
    for source_path, expected_hash in source.items():
        sp=(root/source_path).resolve()
        if not sp.is_relative_to(root) or not sp.is_file() or digest(sp)!=expected_hash:
            raise ValueError('Batch build input missing or stale: '+source_path)
    checks=doc.get('checks',{})
    if not isinstance(checks,dict):
        raise ValueError('Batch checks must be an object')
    reports=[{'path':path,'sha256':digest(root/path)}]+shots
    records=[]
    for (kind,identifier),target in targets.items():
        files=target['source_files']
        if not files or not all(p in source for p in files):
            continue
        records.append({'target_type':kind,'target_id':identifier,'stage':'build-verified',
             'scope':'unit' if kind=='unit' else 'registered_chapter_draft',
             'status':'accepted','reviewer':visual['reviewer'],'reviewed_at':visual['reviewed_at'],
             'blocking_issues':[], 'source_sha256':{p:source[p] for p in files},
             'evidence':reports,'command':doc.get('command'),
             'artifacts':[{'path':p,'sha256':h} for p,h in outputs.items()],
             'checks':{**checks,'screenshot_inspection':True},
             'adapted_from':'aggregate_batch_and_hash_bound_visual_review'})
    return {'schema_version':1,'validations':records}


def apply_reviews(root, chapters, units):
    """Accept only explicit, scope-bound, current-source, current-report attestations.

    A matching digest does not assess mathematics; the named reviewer owns the attestation.
    Missing or stale evidence is reported, never promoted. Unit review does not silently
    become whole-chapter review. This loader itself cannot complete textbook coverage.
    """
    targets = {('unit',r['unit_id']):r for r in units}
    targets.update({('chapter',r['code']):r for r in chapters})
    audit = []
    inputs = [('research/production/accepted_reviews.json','reviews',False),
              ('data/production/batch_validation.json','validations',True)]
    for path,key,is_build in inputs:
        if not (root/path).is_file():
            audit.append({'input':path,'status':'not_present'})
            continue
        try:
            doc=json.loads((root/path).read_text())
            if is_build and isinstance(doc,dict) and 'validations' not in doc:
                doc=aggregate_build_reviews(root,doc,path,targets)
            if doc.get('schema_version')!=1 or not isinstance(doc.get(key),list):
                raise ValueError('schema_version=1 and a record list are required')
        except (ValueError,TypeError,KeyError,OSError) as exc:
            audit.append({'input':path,'status':'pending_schema_adapter' if is_build else 'rejected','reason':str(exc)})
            continue
        for index,review in enumerate(doc[key]):
            item={'input':path,'index':index,'status':'rejected'}
            try:
                if not isinstance(review,dict):
                    raise ValueError('Record must be an object')
                kind,identifier=review.get('target_type'),review.get('target_id')
                item.update(target_type=kind,target_id=identifier)
                target=targets.get((kind,identifier))
                stage=review.get('stage')
                if not target or stage not in (['build-verified'] if is_build else ['math-reviewed','pedagogy-reviewed']):
                    raise ValueError('Unknown target or unauthorized stage for input')
                if review.get('status')!='accepted' or review.get('blocking_issues')!=[]:
                    raise ValueError('Explicit accepted status and empty blocking_issues required')
                if not all(isinstance(review.get(k),str) and review[k].strip() for k in ['reviewer','reviewed_at']):
                    raise ValueError('Reviewer and review date required')
                if not re.fullmatch(r'\d{4}-\d{2}-\d{2}(?:T.*)?',review['reviewed_at']):
                    raise ValueError('Review date must begin with ISO date')
                expected_scope='unit' if kind=='unit' else 'registered_chapter_draft'
                if review.get('scope')!=expected_scope:
                    raise ValueError('Scope must be '+expected_scope)
                if target['stage']=='unwritten' or not target['source_files']:
                    raise ValueError('No registered manuscript body')
                if kind=='unit' and set(target['source_files'])!=set(target['planned_source_files']):
                    raise ValueError('Both registered unit manuscript and answers required')
                current={p:digest(root/p) for p in target['source_files']}
                snapshot={r['path']:r['sha256'] for r in target['source_snapshot']}
                if current!=snapshot or review.get('source_sha256')!=current:
                    raise ValueError('Exact current source snapshot mismatch')
                reports=review.get('evidence')
                if not isinstance(reports,list) or not reports:
                    raise ValueError('At least one hash-bound report required')
                for report in reports:
                    if not isinstance(report,dict) or not isinstance(report.get('path'),str):
                        raise ValueError('Invalid report record')
                    report_path=(root/report['path']).resolve()
                    if not report_path.is_relative_to(root) or not report_path.is_file():
                        raise ValueError('Report must be an existing repository file')
                    if report.get('sha256')!=digest(report_path):
                        raise ValueError('Report digest mismatch')
                if is_build:
                    if not isinstance(review.get('command'),str) or not review['command'].strip():
                        raise ValueError('Build command required')
                    artifacts=review.get('artifacts')
                    if not isinstance(artifacts,list) or not artifacts:
                        raise ValueError('Build artifact list required')
                    for artifact in artifacts:
                        ap=(root/artifact['path']).resolve()
                        if not ap.is_relative_to(root) or not ap.is_file() or artifact.get('sha256')!=digest(ap):
                            raise ValueError('Build artifact missing or stale')
                    required={'formula_rendering','images','cross_references','exercise_answer_pairs','screenshot_inspection'}
                    checks=review.get('checks',{})
                    if not isinstance(checks,dict) or any(checks.get(k) is not True for k in required):
                        raise ValueError('All explicit build inspection checks must pass')
                accepted={**review,'attestation_file':path,'attestation_file_sha256':digest(root/path)}
                target['stages'][stage]={'status':'passed' if kind=='unit' else 'partial',
                                         'evidence':target['stages'][stage]['evidence']+[accepted]}
                category={'math-reviewed':'math','pedagogy-reviewed':'pedagogy','build-verified':'build'}[stage]
                target['review_evidence'][category].append(accepted)
                item.update(status='accepted',stage=stage)
            except (ValueError,TypeError,KeyError,OSError) as exc:
                item['reason']=str(exc)
            audit.append(item)
    for chapter in chapters:
        child_units=[u for u in units if u['parent_code']==chapter['code']]
        if not child_units:
            continue
        chapter['units']=[{'code':u['code'],'title':u['title'],'stage':u['stage'],
                           'msc_leaf_codes':u['msc_leaf_codes'],
                           'review_stages':{k:u['stages'][k]['status'] for k in STAGES[2:]}}
                          for u in child_units]
        for stage in STAGES[2:]:
            passed=[u['code'] for u in child_units if u['stages'][stage]['status']=='passed']
            if passed:
                chapter['stages'][stage]['status']='partial'
                chapter['stages'][stage]['covered_units']=passed
                chapter['stages'][stage]['scope_note']=f"仅列明单元通过，不代表第{chapter['number']}章全部分类主题通过"
    return audit


def part_records(root, parts, chapters, sections):
    """Record whole-part scope and the user's completion-before-push gate.

    Unit/chapter-draft attestations cannot establish whole-part acceptance. A
    historical push is retained only with a local commit and a hash-bound receipt;
    this is evidence validation, not a fresh query of the remote repository.
    """
    previous = {}
    prior_path = root/'data/production/parts.json'
    if prior_path.is_file():
        try:
            prior = json.loads(prior_path.read_text())
            if isinstance(prior, dict) and prior.get('schema_version') == 1 and isinstance(prior.get('entries'), list):
                previous = {r['code']: r for r in prior['entries'] if isinstance(r, dict)
                            and isinstance(r.get('code'), str)}
        except (ValueError, OSError):
            pass
    entries = []
    for part in parts:
        code = part['code']
        child_chapters = [r for r in chapters if r['part_code'] == code]
        direct = [r for r in sections if r['parent_code'] == code]
        subject = [r for r in sections if r['part_code'] == code and r['parent_code'] != code]
        if any(r['parent_code'] != code for r in child_chapters):
            raise ValueError('Part chapter attribution mismatch: '+code)
        if any(r['level'] != 'general_leaf' for r in direct):
            raise ValueError('Part direct-section attribution mismatch: '+code)
        if any(r['parent_code'] not in {c['code'] for c in child_chapters} for r in subject):
            raise ValueError('Part subject-section attribution mismatch: '+code)
        has_draft = any(r['stage'] != 'unwritten' for r in child_chapters+direct)
        push = {'status': 'not_due', 'verified_commit': None, 'verified_at': None,
                'evidence': [], 'reason': '尚无完整顶层部分的验收；单元、章草稿或批次完成不触发push',
                'remote_checked_this_build': False}
        old_push = previous.get(code, {}).get('push', {})
        if isinstance(old_push, dict) and old_push.get('status') == 'verified':
            try:
                commit = old_push.get('verified_commit')
                if not isinstance(commit, str) or not re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', commit):
                    raise ValueError('A full hexadecimal commit digest is required')
                verified_at = old_push.get('verified_at')
                if not isinstance(verified_at, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}T.+', verified_at):
                    raise ValueError('A dated push receipt is required')
                result = subprocess.run(['git','-C',str(root),'cat-file','-t',commit],
                                        capture_output=True, text=True, timeout=10, check=False)
                if result.returncode != 0 or result.stdout.strip() != 'commit':
                    raise ValueError('Recorded commit is not available in local Git history')
                reports = old_push.get('evidence')
                if not isinstance(reports, list) or not reports:
                    raise ValueError('A hash-bound complete-part push receipt is required')
                receipts = []
                for report in reports:
                    if not isinstance(report, dict) or not isinstance(report.get('path'), str):
                        raise ValueError('Invalid push evidence record')
                    rp = (root/report['path']).resolve()
                    if not rp.is_relative_to(root) or not rp.is_file() or report.get('sha256') != digest(rp):
                        raise ValueError('Push evidence is missing or has changed')
                    receipts.append(json.loads(rp.read_text()))
                if not any(isinstance(r, dict) and r.get('schema_version') == 1
                           and r.get('target_type') == 'part' and r.get('target_id') == code
                           and r.get('scope') == 'complete_part' and r.get('status') == 'verified'
                           and r.get('verified_commit') == commit and r.get('verified_at') == verified_at
                           and r.get('full_scope_accepted') is True and r.get('push_succeeded') is True
                           for r in receipts):
                    raise ValueError('No receipt matches the complete part, commit, date and successful push')
                push = {**old_push, 'remote_checked_this_build': False,
                        'preservation_validation': 'local_commit_and_hash_bound_historical_receipt',
                        'historical_only': True,
                        'reason': '保留已验证的历史push证据；不据此授予当前稿完整验收'}
            except (ValueError, TypeError, KeyError, OSError, subprocess.TimeoutExpired) as exc:
                push['previous_record_validation'] = {'status': 'rejected', 'reason': str(exc)}
        entries.append({
            **part, 'level': 'major', 'stage': 'partial_draft' if has_draft else 'unwritten',
            'scope': {
                'chapter_codes': [r['code'] for r in child_chapters],
                'direct_general_section_codes': [r['code'] for r in direct],
                'subject_section_codes': [r['code'] for r in subject],
                'chapter_count': len(child_chapters), 'direct_general_section_count': len(direct),
                'subject_section_count': len(subject),
                'attribution': '保持原MSC父子关系；直属通用节不虚构中类归属'},
            'coverage': {'completed': False, 'scope': 'whole_classification_part',
                'chapters_with_draft': sum(r['stage'] != 'unwritten' for r in child_chapters),
                'completed_chapters': sum(r['coverage']['completed'] for r in child_chapters),
                'direct_sections_with_draft': sum(r['stage'] != 'unwritten' for r in direct),
                'completed_direct_sections': sum(r['coverage']['completed'] for r in direct),
                'note': '有限桥接单元及其审阅不构成顶层部分完成；尚无完整部分验收导入'},
            'acceptance_criteria': [
                '原分类范围内所有需写子章及直属节均按逐项声明的教学深度真正完成，不能以目录或导读替代完整教学',
                '范围内所有节的先修、定义、命题、例题和题答完整，并由当前源稿哈希绑定的数学审阅覆盖',
                '完整部分教学审阅覆盖全部声明目标、先修可读性及题答，而非仅抽取单元',
                '完整部分实际构建及公式、图片、链接、题答检查通过，且有当前产物哈希绑定的实际视觉验收',
                '完整范围验收通过后才到达该部分push节点；每单元、每章或每批结束均不单独触发'],
            'completion_checks': {
                'all_chapters_completed': all(r['coverage']['completed'] for r in child_chapters),
                'all_direct_sections_completed': all(r['coverage']['completed'] for r in direct),
                'full_scope_math_accepted': False, 'full_scope_pedagogy_accepted': False,
                'full_scope_build_and_visual_accepted': False},
            'full_scope_acceptance': {'status': 'pending', 'evidence': [],
                'unit_reviews_do_not_promote_part': True},
            'push': push})
    return {'schema_version': 1, 'generated_by': 'tools/build_production_ledger.py',
        'policy': '持续本地写作；每完成一个完整顶层部分才到达GitHub push节点，生成台账不执行push',
        'receipt_policy': '既有verified记录必须绑定本地commit及仓库内哈希匹配的JSON回执，回执须明确complete_part/full_scope_accepted/push_succeeded；仅保留历史事实，不等于当前完成或重新查询远程',
        'entries': entries,
        'checks': {'parts': len(entries), 'chapters': sum(r['scope']['chapter_count'] for r in entries),
            'direct_general_sections': sum(r['scope']['direct_general_section_count'] for r in entries),
            'subject_sections': sum(r['scope']['subject_section_count'] for r in entries),
            'completed_parts': 0, 'remote_actions_performed': False}}


def build(root):
    taxonomy = json.loads((root/'data/msc_taxonomy.json').read_text())
    translated = json.loads((root/'data/catalog_titles_zh.json').read_text())
    rows = taxonomy['entries']
    titles = {r['code']: r for r in translated['entries']}
    if Counter(r['level'] for r in rows) != Counter(EXPECTED):
        raise ValueError('Unexpected MSC counts')
    if len({r['code'] for r in rows}) != len(rows) or set(titles) != {r['code'] for r in rows}:
        raise ValueError('Classification code sets are inconsistent')
    children = defaultdict(list)
    for row in rows:
        children[row['parent_code']].append(titles[row['code']])
    chapters, sections, parts = [], [], []
    chapter_bridge_files = defaultdict(list)
    leaf_bridge_specs = defaultdict(list)
    for spec in UNIT_SPECS:
        parent = spec.get('parent_code','11Axx')
        chapter_bridge_files[parent].extend([spec['body'],spec['answers']])
        for leaf_code in spec.get('msc_leaf_codes',[]):
            if leaf_code not in titles or titles[leaf_code]['parent_code'] != parent:
                raise ValueError('Registered unit leaf disagrees with taxonomy: '+leaf_code)
            leaf_bridge_specs[leaf_code].append(spec)
        for cross_code in spec.get('msc_cross_reference_codes',[]):
            if cross_code not in titles or titles[cross_code]['level'] != 'subject_leaf':
                raise ValueError('Unknown cross-reference subject leaf: '+cross_code)
            if cross_code in spec.get('msc_leaf_codes',[]):
                raise ValueError('Cross-reference leaf duplicates the primary leaf: '+cross_code)
    part_opening = 'manuscript/review_ch01/part_opening.md'
    ch01_text = (root/CH01[0]).read_text() if (root/CH01[0]).is_file() else ''
    opening_text = (root/part_opening).read_text() if (root/part_opening).is_file() else ''
    for part in children[None]:
        parts.append({'code': part['code'], 'number': len(parts)+1, 'title': part['title_zh']})
        for row in children[part['code']]:
            if row['level'] == 'general_leaf':
                has_anchor = '{#sec-'+row['code']+'}' in opening_text
                files = [part_opening] if has_anchor else []
                sections.append(record(root,row,len(sections)+1,part['code'],files,files,'draft_scope_unreviewed'))
            elif row['level'] == 'intermediate':
                code = row['code']
                files = CH01 if code=='00Axx' else chapter_bridge_files.get(code,[])
                bodies = [p for p in files if 'answers' not in p and 'appendices' not in p]
                chapter = record(root,row,len(chapters)+1,part['code'],files,bodies,
                                 'partial_bridge_only' if code in chapter_bridge_files else 'draft_scope_unreviewed')
                if code=='00Axx':
                    chapter['title'] = '绪论：一般与综合专题'
                    chapter['learning_entry'].update(status='explicit_entry',module_ids=['reading'])
                    chapter['review_evidence']['candidate_reports'] = evidence(root,[
                        'research/ch01_math_review.md','research/ch01_source_checks.md',
                        'research/production/ch01_review_2026-10-27.md'])
                if code=='11Axx':
                    chapter['learning_entry'].update(status='bridge_entry_defined_chapter_pending',
                       module_ids=['natural','place-value','natural-order','division','positional','written-arithmetic','integer-addition-order','integer-multiplication','integer-division','divisibility','gcd-euclidean','bezout','coprimality','rational-construction','rational-arithmetic','rational-order'],adopted_assumptions=[
                       '自然数公理与归纳原则、递归原则；详见prerequisites.json的adopted_foundations'])
                    chapter['coverage']['unwritten_topics'] = '已有自然数与整数运算、带余除法、整除、最大公因数、贝祖等式、互素整数对，以及有理数构造、加减乘法、非零倒数与除法基础；有理数次序、绝对值与大小比较已有草稿；同余、素数、唯一分解、连分数等主题仍待写'
                if code=='97Fxx':
                    chapter['learning_entry'].update(status='bridge_entry_defined_chapter_pending',
                        module_ids=['relations-units','number-systems'])
                    chapter['coverage']['unwritten_topics'] = '仅登记比与比例、精确有理单位模型、有理数的稠密界与平方缺口、戴德金分割次序与非空有界族并集上确界、分割有理逼近及加法相反数、有序交换加法群、非负分割乘积与有理相容、非负结合分配和严格比较、全符号乘法与结合、全分配比较与非零消去、非零倒数与唯一性、除法方程及完备有序域接口、实数界与有理像稠密、非负平方根及实数绝对值距离十五个教学桥接；一般实数幂与n次根、完备性等价与唯一同构、复数、百分数、其余算术数论教育主题及系统教育研究仍待写'
                if code=='97Ixx':
                    chapter['learning_entry'].update(status='bridge_entry_defined_chapter_pending',
                        module_ids=['functions'])
                    chapter['coverage']['unwritten_topics'] = '仅登记函数定义、相等限制复合、单满双射、逆函数、有理坐标与仿射图像六个教学桥接；超出有理仿射范围的图像、函数方程、极限连续及分析学教育研究仍待写'
                if code=='97Hxx':
                    chapter['learning_entry'].update(status='bridge_entry_defined_chapter_pending',
                        module_ids=['functions','real-algebra-equations'])
                    chapter['coverage']['unwritten_topics'] = '仅登记有理数一元一次方程、二元一次方程组、一次不等式、绝对值条件、非负整数幂、有限和、多项式规范记录、加法数乘、有限卷积乘法、乘积求值次数、首一线性商余、有理根与恒等识别、有理平方判据及有理配方二次方程、实数二次方程与配方界十五个教学桥接；一般多项式除法、根的重数及更高次根存在性、更一般不等式系统、高次方程、一般代数结构及代数教育研究仍待写'
                if code=='97Gxx':
                    chapter['learning_entry'].update(status='bridge_entry_defined_chapter_pending',
                        module_ids=['real-plane-geometry'])
                    chapter['coverage']['unwritten_topics'] = '仅登记实数坐标、位移、参数直线与线段、二维范数与欧氏距离、直线方程交点及正交投影最近点四个教学桥接；角度测量、面积、欧氏公理整体模型、其他几何教育主题及系统教育研究仍待写'
                if code=='40Axx':
                    chapter['learning_entry'].update(status='sequence_entry_defined_chapter_pending',
                        module_ids=['single-analysis'])
                    chapter['coverage']['unwritten_topics'] = '仅登记B4.1—B4.2实数数列收敛定义、唯一性、基本例、尾移、有界及四则极限；单调收敛、子列、级数及其余无穷极限主题待写，整章未完成'
                chapters.append(chapter)
                for leaf in children[code]:
                    has_anchor = code=='00Axx' and '{#sec-'+leaf['code']+'}' in ch01_text
                    leaf_specs = leaf_bridge_specs.get(leaf['code'],[])
                    section_files = ([CH01[0],CH01[1]] if has_anchor else
                                     [path for spec in leaf_specs for path in [spec['body'],spec['answers']]])
                    section_bodies = [CH01[0]] if has_anchor else [spec['body'] for spec in leaf_specs]
                    section = record(root,leaf,len(sections)+1,part['code'],section_files,section_bodies,
                                     'partial_bridge_only' if leaf_specs else 'draft_scope_unreviewed')
                    if leaf_specs:
                        section['registered_unit_codes'] = [spec['code'] for spec in leaf_specs]
                        section['coverage']['unwritten_topics'] = '只登记所列桥接单元的有限教学目标，不表示该MSC叶的全部主题与研究范围完成'
                    sections.append(section)
    if len(chapters)!=534 or len(sections)!=6006 or len(parts)!=63:
        raise ValueError('Ledger totals disagree with classification')
    if next(r for r in chapters if r['code']=='11Axx')['number'] != 26:
        raise ValueError('Unexpected 11Axx chapter number')
    for spec in UNIT_SPECS:
        parent = next(r for r in chapters if r['code']==spec.get('parent_code','11Axx'))
        if parent['number'] != spec.get('parent_chapter_number',26) or parent['part_code'] != spec.get('part_code','11-XX'):
            raise ValueError('Registered unit parent numbering disagrees with taxonomy: '+spec['code'])
    all_index = {r['code']:r for r in rows}
    for group in [chapters,sections]:
        assert [r['number'] for r in group] == list(range(1,len(group)+1))
        for r in group:
            assert r['parent_code'] == all_index[r['code']]['parent_code']
            assert all((root/p).is_file() for p in r['source_files'])
    meta = {
        'schema_version':1, 'generated_by':'tools/build_production_ledger.py',
        'source_sha256': {p:digest(root/p) for p in ['data/msc_taxonomy.json','data/catalog_titles_zh.json','LEARNING_PATH.md']},
        'stage_names':STAGES,
        'status_policy':'正文文件及锚点只能支持draft；审稿与构建各自需要绑定当前文件哈希和覆盖范围的证据。目录、文件存在、旧PDF均不授予完成状态。',
        'source_requirements': [
            '每条来源记录作者、标题、版本、页码或定理位置、公开URL、访问日期和使用方式',
            '可公开阅读不等于可转载；逐项核验许可、署名和改编条件',
            '定理至少核对条件与证明链；关键争议点需独立来源或独立推导交叉核验',
            '预印本明确未同行评议；开放问题注明目前学界尚在研究和核验日期',
            '数值计算附公式、假设、误差或稳定性说明、代码和可复现输入输出'],
        'review_gate_requirements': {
            'math-reviewed':'审阅人、日期、当前正文哈希、覆盖命题、已解决问题及未解决问题',
            'pedagogy-reviewed':'符号首次定义、先修可读性、层次入口、例反例与练习梯度的审阅证据',
            'build-verified':'构建命令、输入与输出哈希、公式图像与链接检查、实际截图检查证据'},
        'checks': {'parts':63,'chapters':534,'sections':6006,'direct_general_sections':503,
                   'subject_sections':5503,'classification_parents_preserved':True,
                   'source_files_exist':True,'numbering_contiguous':True},
    }
    units = unit_records(root)
    review_audit = apply_reviews(root,chapters,units)
    meta['review_import_audit'] = review_audit
    meta['snapshot_note'] = '文件哈希仅标识生成时快照；源稿继续修改后必须重新生成并重新核对审阅证据'
    out = root/'data/production'
    out.mkdir(parents=True,exist_ok=True)
    for name,data in [('chapters',{**meta,'parts':parts,'entries':chapters}),
                      ('sections',{**meta,'entries':sections}),
                      ('units',{**meta,'entries':units}),
                      ('prerequisites',prerequisite_data(root,chapters)),
                      ('parts',part_records(root,parts,chapters,sections))]:
        (out/(name+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'chapters':len(chapters),'sections':len(sections),
       'chapters_with_draft_body':sum(r['stage']=='draft' for r in chapters),
       'sections_with_draft_body':sum(r['stage']=='draft' for r in sections),
       'completed_chapters':sum(r['coverage']['completed'] for r in chapters),
       'source_file_checks':'passed','module_graph':'acyclic',
       'unit_reviews_imported':sum(r.get('status')=='accepted' and r.get('target_type')=='unit' for r in review_audit)},ensure_ascii=False,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=ROOT)
    build(parser.parse_args().root.resolve())
