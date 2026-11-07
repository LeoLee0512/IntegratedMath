# 第35批75单元候选独立集成审计

2026-11-05；审阅者 `/root/part1_audit`。结论：**候选集成审核通过，无应用阻断；不是构建或产物验收。** 本次只读正式仓库与两组候选，检查脚本、报告及隔离重跑输出仅写/tmp。未执行正式生成器、compose_body、builder、validator主函数、PDF编译或截图；未修改正式稿、审签、台账或产物。

## 精确候选与基线

| 候选文件 | SHA-256 |
| --- | --- |
| /tmp/frc-rfs-flc75-registration/build_production_ledger.py | dcae973168a9b5884a112b4d665ded3f1bb13ad9c6dece30874b022f58c53e1c |
| /tmp/frc-rfs-flc75-registration/accepted_reviews.json | 7b0d3f55bd9ac7e6efe724ac82bb562bfeb99599aa766090bc5011831f7e783a |
| /tmp/batch35-builder-candidate/build_learning_batch.py | da78349c3fcb72a4c232ac452e7ee9ce8d45ca0d9c938ac6a45d002c44d8bf17 |
| /tmp/batch35-builder-candidate/validate_learning_batch.py | be68563984a52cd7474d954f3ae4a76947aa55abea5fe7afd6688c09bbefde58 |

实际重算两个candidate_hashes.json列出的各文件hash，均匹配。registration.json列出的40项正式基线也逐项重算，全部匹配。正式工具基线为ledger `5f7e554207ba99ed089941c5ef46e74dae52e3e6b8e3c8daeff15befd2a7114f`、builder `efa3639ac6753e7b6fa45a5f3778121ce67b07962bc70f82329c7adbdb80efb1`、validator `14a36b325d52d9d1d8f3e3e597734aea399fa5f2969dd84cb8be85b14756ebaf`；accepted基线 `f65c40b79f14f718dfebed26f6e927dcd3bd8c67ce932a78509aa3e364a8969d`。应用前仍须由执行者重核，不能把此时比较视为后续并发变化的豁免。

## 实际差异检查

实际逐段读完整累计ledger差异、builder和validator差异，读取六条新增accepted登记及三份教学报告；本代理先前已分别全文审过三单元并写数学报告，本次核这些签署身份和实际字节，不声称再次重读所有教学正文。

- AST提取实际对象后核旧72个UNIT_SPECS、旧144个BRIDGE路径、旧144条accepted记录逐项相等；新75项各编号及顺序与builder.UNITS一一对应。旧三个分类映射、旧72正文顺序保留。
- 新单元均8题、8答案，24对锚和定义/证明锚唯一且存在。新六条审签仅math/ped两阶段，各单元math=/root/part1_audit、ped=/root，身份不同；实际六稿和六报告SHA均与accepted绑定相符，每份报告含其两稿最终hash。作者“未审/未注册”历史措辞未被用作通过证据。
- 75×8+27=627题答；150条文字审签。没有候选构建签，没有把旧34批收据升格为75项产物通过。FSP等后续稿未列入UNIT_SPECS/UNITS/accepted。
- builder.source_hashes新增的15个plan/source/report路径均实际存在，并与各spec.source_records逐项吻合。三单元六稿随UNITS纳入原有输入绑定流程；新来源锚frc-sources/rfs-sources/flc-sources纳入唯一性检查。缓存原文不作为出版依赖加入，不在这里执行新网络访问。
- 函数AST检查：ledger仅prerequisite_data/build有变；builder仅source_hashes/compose_body/main与改名扩充的启动guard有变；validator仅main/render_contacts有变。其他既有函数AST保留。所有旧验证项仍在，数量、章序、部分序和披露文本按75项准确更新，另增加部分→章→单元包含条件。没有改成恒真或删除检查。

## 学习顺序、分类与精确先修

| 序号/学习号 | 单元 | 实际主分类 | 部分/章 | 先修锚数 |
| --- | --- | --- | --- | --- |
| 73 / B4.L1 | FRC | 15A03 | 11 / 84 | 24 |
| 74 / B2.39 | RFS | 97H20 | 63 / 528 | 29 |
| 75 / B4.L2 | FLC | 15A03 | 11 / 84 | 18 |

已以实际msc_taxonomy及当前chapters/parts核父子链和编号，不仅信候选字符串。71个先修引用逐一查到唯一锚且位于更早登记的单元。FRC取实数运算/函数/有限计数，旧有理求和仅登记结构对照，不依赖尚未定义的实数和；RFS取固定状态递归、自然索引/差、实数加乘及旧有理和的嵌入接口，不反向依赖FRC或二次方程；FLC明确依赖FRC五接口与RFS五接口，再定义加权实数表。不存在新登记引入的单元先修环。

MODULES只扩充real-algebra-equations显示标题与本轮写作覆盖，既有ID/stage/tags/概略边不改。线性代数模块的精确接口另明确B4.L2→B4.L1及B2.39，故没有把概略模块图冒称全量证明依赖；也没有将整个方程模块加为FRC先修。模块/第84章/第528章都仍partial，旧单元not_covered只表示该单元自身范围，不能误读为全书不存在后续已写内容。

实际读取新增三段导读，确认按84→528续→84续和11→63续→11续生成独立唯一锚。学习号不替代MSC编号，返回528没有被留在线性代数部分标题下。validator同时查章序、部分序、章区间，以及新部分锚在所属章与单元之前且在下一部分之前。三单元导读与source文本的隔离装配检查通过。

## 外部Markdown引用与隔离负例

当前正式validator已有的is_local_markdown_fragment与候选函数AST完全相同。实际执行9个输入：有效HTTP/HTTPS源文件`.md#`引用允许；相对稿件路径、`../`、绝对本地路径、file URL、协议相对路径、无主机的畸形HTTPS路径均识别为本地/不允许泄露；普通内部锚不误报。原audit_book仍要求内部锚存在，且仅允许#、https://、http://、mailto:前缀，因此该修复没有把任意相对链接放行。此处是链接分类检查，不等于远端可访问或内容已核验。

实际复跑候选提供的隔离检查脚本，仅将其输出重定向到本报告目录；执行范围是提取原样启动guard和两段位置检查，不调用完整构建/验证主程序。真实75项及8 verified/10 pending/15原创账通过；正式72项、FRC/RFS次序互换、RFS误归15-XX、把第63部分返回标题移至RFS之后均被拒绝。24题答与三个来源锚检查通过。复跑详细证据见isolated_replay.json，独立对象/基线/签署核对见checks.json；前者不冒称是本代理重新发明的测试。

## 非阻断备注与后续边界

候选ledger的RFS追加块前仍有74阶段遗留代码注释“finite coordinate linear combinations remain unregistered”。实际下一块明确登记最终FLC，执行对象/签署/报告均为75项，因此不影响结果；建议以后改注释避免读源码时误会。无需改冻结正文或重签数学。

第一部分仍为8个G已核、10个G来源pending、15个原创T/S独立审阅；00B05应用门槛及八稿绑定保留。作者审阅与整部分完成不由本报告升级。75单元应用后必须实际重新生成台账并重建，旧构建证据若输入hash失配须如实pending；随后重新完成627对题答、链接/字体/溢出/图形自动验证及绑定新PDF的实际视觉。本报告只支持这四份精确候选安全进入正式应用步骤。
