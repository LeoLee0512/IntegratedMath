# FSP第76项登记候选：仅提案，尚未安装或应用

2026-11-05，/root/part1_audit。基于第35批已应用的75单元、150条文字审签；不修改当前327项构建输入，不运行生成器/build/validator，不预注册FLI。候选数量为76单元、608基础题答＋27第一部分＝635对、152条文字审签。

本目录有两份候选文件build_production_ledger.py、accepted_reviews.json，以及相对当前正式75项的完整.diff、语义检查checks.json和registration.json。base/保全精确旧文件，prepare.py是生成候选脚本副本；candidate_hashes.json绑定本目录文件。正式来源仍在/tmp/finite-coordinate-subspaces-draft，未复制进正式稿、未改临时原文或历史报告。

## 单元及先修

FSP为第76项、学习号B4.L3，主第11部分15-XX／第84章15Axx／15A03，模块linear-algebra；标题保持已审“线性子空间与有限表的生成集合”。学习号映射由后续builder加，不改冻结正文标题。原75个spec、150稿路径、150审签完整保留；MODULES连显示标题和全部依赖边都不变。

登记FSP1—6、8题与8解、23个精确先修锚。22个来自正文开篇实际链接，另补rfs-definition定位单项和值的递归依据；这些锚均存在且来自更早登记的单元。FSP依次以单项和引理、闭合与含项建立最小性，再得同值集表不变，不调用未证任意重排。模块精确接口另补B4.L3→FRC/RFS/FLC，而非增添概略MODULES边。

模块和第84章的written内容仅新增具体V_n子空间和有限表生成；不再把这段有限生成全称为未写。任意向量族生成、子空间交/和、商空间、抽象空间、线性相关与无关、基、维数、秩、lineability、一般线性映射、矩阵、消元、行列式及任意重排仍未覆盖。保持completed=false和chapter_pending，不把当前已审FSP扩大成完整15A03或整章。

## 临时源到正式路径映射

registration.json.actual_to_intended逐项列出7份文件的实际/tmp路径、目标路径与SHA：两稿到manuscript/foundations，plan/source/author_check/math_review/pedagogy_review到research/production。当前目标均实际不存在。只有未来按映射字节复制并复核哈希，候选accepted才能匹配其正式路径；现在不能称正式单元已登记或构建通过。

正文SHA d61775e91c706c45cf03b216ed16e0b03de8799926f51302815c51ffdf09fd97；答案SHA93847c7812c470fb727c277edd5853ea64f0071b63ec4776c65ec9d8330f29dc。math审者/root/part1_audit、报告e3b73d9a00a4ec19ef2fb1866960a6069949d901373458eb1a3280d8ab2ac11d；ped审者/root、报告ccac39e48c0a6c04dec335d80079ded55c474f599a1d7f88093e880d43250491。两份均真实全文八解审签，原报告日精度保留，不代签或伪造更精确时刻。

原sourceJSON实际读取位置和事件保持原字节，包括/tmp新S/SS原生缓存；COPYING/bookinfo仍指既有本地缓存。本轮只重新核四条缓存hash，内容阅读证据承接已有数学/教学报告，不声称新联网或又读原书全文。sourceJSON/报告中的“暂未安装/待审”等原作者/历史措辞不改写，作者检查不充当独立通过证据。未来移动缓存需另存保全映射，不能篡改原读取路径或时间。外部源全文没有复制入本候选。

## 已完成检查及尚未执行

两候选语法可解析，旧对象/签署逐项相等；仅prerequisite_data和build函数AST变化，其他既有函数不变。8对题答与6证明锚存在，23先修皆在旧75之内；实际分类数据核15A03→15Axx→15-XX和第84章。来源和两审签绑定实际/tmp字节，正式基线及稿件先修hash记录在registration.json.baseline_sha256。完整差异已实际逐段检查。

未运行任何台账生成或新构建，不签构建/视觉，不改变第一部分来源10pending及作者审阅状态。当前builder/validator只支持第35批75项，未来采用第76项或再纳入已写且已审FLI成为第77项时，必须另准备匹配的builder/validator更新；不能把本候选单独覆盖正在构建的正式文件。未来应用前还须重核baseline，当前35产物的新收据应独立封存；旧收据输入失配时如实pending。
