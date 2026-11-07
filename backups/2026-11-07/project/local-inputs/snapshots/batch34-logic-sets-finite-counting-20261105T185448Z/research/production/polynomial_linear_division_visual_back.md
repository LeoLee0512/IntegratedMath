# 第十九批一次除式与根数界：审阅版后段实际视觉复核

## 结论与实际范围

主代理明确发送最终QA READY后，本代理实际打开38张接触表，覆盖《综合数学_基础续写审阅版》PDF物理页157–604，共448页；另实际打开物理页557、603、604的单页图，共41张图片。所见范围没有阻断性的图文遮挡、公式重叠、明显越界或内容裁切。页557修订后的来源引用已在本轮单页图中实际检查，长标识与后续文字在页边距内。

本报告不修改全局QA状态，不代表整书验收。所有页码均为PDF物理页；页脚另有印刷页码。页1–156、主代理另看的24张单页以及前段代理查看的其他PDF图片不计入本代理范围。其余三份PDF在本报告仅核字节哈希和页数，未声称逐页查看。

## QA快照与当前文件绑定

以下绑定来自最终READY后的QA快照；没有把第十八批图片或此前发生裁切的构建图片当作本轮证据。38张接触表及3张单页图均在READY后实际打开，再逐张重新计算SHA-256与该快照比对，全部一致。四份PDF也重新计算SHA-256并核页数。

- QA路径：`data/production/batch_validation.json`
- `validated_at`：`2026-10-29T19:20:53.442564+00:00`
- 状态：`automated_checks_passed`
- 本次读取快照SHA-256：`2630831372ae3acc90e46268a1f45a67c4a7fa60fb5ea17c52de2a87c6d83a6a`
- 快照记录规模：168个源文件、44个构建产物、717张截图。

QA快照哈希绑定本次读取的版本；若后续加入人工审阅记录，不以更新后的文件哈希替换此历史值。

| PDF | 页数 | SHA-256 |
|---|---:|---|
| `dist/综合数学.pdf` | 818 | `44a42aeb215bf904d9a440217046afe5889f97ce7f1ddf9be651f0be9467a787` |
| `dist/综合数学_基础续写审阅版.pdf` | 604 | `00e6637eb2ee4bb360a5a21e7b0848e7cc17d30959c8fcf5ea23603f0d4e051a` |
| `dist/综合数学_完整数学目录.pdf` | 218 | `6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55` |
| `dist/综合数学_第一章审阅版.pdf` | 31 | `53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd` |

## 实际所见

- 页157–329：接触表尺度的正文、公式、表格及既有插图没有可辨识的遮挡、越界或页脚冲突。页184、185、201等章节结束或转换页有较多留白，内容及页码仍在，未将留白误判为缺页。既有乘法证明有短小跨页延续行，所见只是连续分页，无明显裁切。
- 页330–344：新增一次除式、综合除法、不同根数界及恒等识别的正文与练习均可定位。状态公式、示例表格及证明块与正文分隔正常；页344是短小来源结束段，下面留白，随后页345进入答案区。
- 页345–548：答案区整体未见接触表尺度的阻断。新增PD答案从页537开始，RT答案从页542开始，末尾到548；两批新增题答的公式块、步骤表和段落没有明显互压或向右溢出。
- 页549–557：插图索引与参考来源在接触表中可辨识；密集文本仍保有正常边界。页557另行放大核对修复结果，详见下一项。
- 单页557（页脚555）：新增一次除式来源中的OpenStax作者/书名、独立“固定提交”行、完整commit标识、蓝色来源链接及后续范围说明均完整显示，右边界有余量。mathlib来源段和底部审计路径分行显示，没有被页边截断；底部附录入口和页脚不相互覆盖。本代理没有打开此前有裁切的旧图作并排比较，所判定的是本轮最终图片可见内容已经完整。
- 页558–604：程序附录说明、公式与代码在接触表尺度未见明显越界。页566、569、572、588、600、602、604等代码尾部留白程度不同，没有据此宣称内容丢失。最后接触表只有601–604四页，其他格位为背景，而不是额外空白PDF页。
- 单页603（页脚601）：附录二十二标题、输入输出说明、D_a及商余等式、两条状态更新式、后缀不变式均可读。末段检查程序和JSON路径分行显示，文件名、段落及页脚之间保有间距；正文没有向右或下边界截断。这里的视觉可读性不等于API输入校验已由本代理执行。
- 单页604（页脚602）：文档字符串、四项导入、`divide_linear`函数、初始化、倒序循环、旧余数参与新商更新以及最终`return quotient, remainder`均显示完整。缩进和行末清楚，源文件结束后的大块留白不是代码被截断。

## 实际打开图片清单

接触表起页为157、169，之后每次加12，直至601。前37张每张12页、1200×1760；最后一张4页、1200×880，合计448页。三张单页图均为765×990。本表每张均实际调用图像查看工具打开；哈希匹配和文字提取没有替代图像查看。

| 图片路径 | 尺寸 | SHA-256 |
|---|---|---|
| `build/learning_batch/screenshots/batch-contact-157.png` | 1200×1760 | `31c80b7c66a7607aa20cbf3ca79e5f513b9e75f6ccccd7146a32206b8a0de2d2` |
| `build/learning_batch/screenshots/batch-contact-169.png` | 1200×1760 | `6ca231b5c48b860a967a707295f69e09142200c3978eb5ec1d5560412578ccf2` |
| `build/learning_batch/screenshots/batch-contact-181.png` | 1200×1760 | `aa72320a5e1b63fdadf0f0b100f572598db5e95b8406953364defc974ff36842` |
| `build/learning_batch/screenshots/batch-contact-193.png` | 1200×1760 | `d2dda57e2d2acb4c885129ae201ddb3621164f83ac46d0db563e5127099d0155` |
| `build/learning_batch/screenshots/batch-contact-205.png` | 1200×1760 | `8db17d1990ff9cf40f5f75bf1ab34b7251edf310e402824e2820c02bc74386f7` |
| `build/learning_batch/screenshots/batch-contact-217.png` | 1200×1760 | `a5a40a4a44ef0160a231b574ec743840cfb5a8f66ad77eec15d4048240cc7434` |
| `build/learning_batch/screenshots/batch-contact-229.png` | 1200×1760 | `aff57657fe09236ca28416fda8241da57ba2fc1a02eee90f72c7b8abe912946c` |
| `build/learning_batch/screenshots/batch-contact-241.png` | 1200×1760 | `5a81534b4389a12ff9578ceccb36cf9ab6da1b572403ae45271b66ae23e44419` |
| `build/learning_batch/screenshots/batch-contact-253.png` | 1200×1760 | `552fbc1a3a09faea80c8bcec2380b4922fabfc64c01b79f51d06bee007861916` |
| `build/learning_batch/screenshots/batch-contact-265.png` | 1200×1760 | `6b006aca9a0f164c6d872e97550c35adf545bcf981ea285bc5d055eb8abce3a1` |
| `build/learning_batch/screenshots/batch-contact-277.png` | 1200×1760 | `943f244fe9bbf4922a2552393dc4f1dc92c003d1343db4089fd82241053968ca` |
| `build/learning_batch/screenshots/batch-contact-289.png` | 1200×1760 | `625eefe27ec25d15d96562e692b29eb1702d50a876ac836cf915fea6ba380a1b` |
| `build/learning_batch/screenshots/batch-contact-301.png` | 1200×1760 | `13acdcac0696159a2920ef712a5a6d93d21ce86120359369cf5e1f9874f27d10` |
| `build/learning_batch/screenshots/batch-contact-313.png` | 1200×1760 | `cffa8881ec8713497587ba07963552aee1d9cf1cda9d4c99125141f42be3c03d` |
| `build/learning_batch/screenshots/batch-contact-325.png` | 1200×1760 | `cc637116bdc83b91573c505044409bb85869abce061ef45e6140a98f7bc5e70d` |
| `build/learning_batch/screenshots/batch-contact-337.png` | 1200×1760 | `6055d007a29b8b0810495ab2569d3529f3e92074dc6ea43978a76d42725f98e8` |
| `build/learning_batch/screenshots/batch-contact-349.png` | 1200×1760 | `db545618b319be69e92b47291364568549987aeeae06e92ad84a30b3ffe6ccc5` |
| `build/learning_batch/screenshots/batch-contact-361.png` | 1200×1760 | `c1b2c21e200f84b9d35973e23e33d59806c2bc5e2494bda62b878256e003ff1c` |
| `build/learning_batch/screenshots/batch-contact-373.png` | 1200×1760 | `54eb1233c8aa8aa43cc36c97d988c447dc13a68011589c2749c0466ceb3ce32b` |
| `build/learning_batch/screenshots/batch-contact-385.png` | 1200×1760 | `ebd3be29f4debfe6a1dd07f814c6b3f01bba44fa976b0d380dc89c7d1fccbac9` |
| `build/learning_batch/screenshots/batch-contact-397.png` | 1200×1760 | `b55fc9c6a2ddacef7ae46dca7a6cd374f877a2e41e2264a9724a5f70c9c05d34` |
| `build/learning_batch/screenshots/batch-contact-409.png` | 1200×1760 | `a99fe4dd1ae72dd3076173c787a0772d65363ce9e79da439a814b39ab12898fc` |
| `build/learning_batch/screenshots/batch-contact-421.png` | 1200×1760 | `bd409da3f60e969e2ef4d021e32f6a50fde48b301bcc0c55068b2394028016ad` |
| `build/learning_batch/screenshots/batch-contact-433.png` | 1200×1760 | `2092da49b698ddf17f6fa996bca5d48e3fb362f5e5c97743a7e2bb746433965d` |
| `build/learning_batch/screenshots/batch-contact-445.png` | 1200×1760 | `a2261299a48a3ac54e061e4c3c0794f2b1dfc58ecfe49d8438aa483ba91eecc2` |
| `build/learning_batch/screenshots/batch-contact-457.png` | 1200×1760 | `a7fe33c42571b4dc803663af918fc2641bed06e1c58c04f307db672e8a88771d` |
| `build/learning_batch/screenshots/batch-contact-469.png` | 1200×1760 | `502d63add7357a93a2a7d7091aac2f166ac8fc4c3ef9a4bf535ef3eb03536510` |
| `build/learning_batch/screenshots/batch-contact-481.png` | 1200×1760 | `c51f6d1b7f250f7333a54775d77424c4be3faf009c20c06a5bba4fc03353f574` |
| `build/learning_batch/screenshots/batch-contact-493.png` | 1200×1760 | `d9c8a2eb5ea0a2ef4326f84b0eeb0c08e0d710e6da3edd830c9f20adae3c9513` |
| `build/learning_batch/screenshots/batch-contact-505.png` | 1200×1760 | `8ec9e4af7d1a684cee404fb3c1ee8ddc6942e76c93c58227590268c14443eaf1` |
| `build/learning_batch/screenshots/batch-contact-517.png` | 1200×1760 | `ab650c17bbaf891771632950304adc1bff868dc5fbf8c4fa0ae819e115b59cba` |
| `build/learning_batch/screenshots/batch-contact-529.png` | 1200×1760 | `7ba4849efdd7f419a0794544a1b6812c05eaa885b040877467c437e0d2e90cb0` |
| `build/learning_batch/screenshots/batch-contact-541.png` | 1200×1760 | `0a993f83030de3721e703c395a2f5c28b009dcf1994c9a2cea44b5c0c1a6ea9a` |
| `build/learning_batch/screenshots/batch-contact-553.png` | 1200×1760 | `b7c8fb14eb724c3a5c121230f8fe31399d246d6f42f6daea356d45b868e44297` |
| `build/learning_batch/screenshots/batch-contact-565.png` | 1200×1760 | `8a5f87fbad303bbe8752fc08768cc5b480047bdfeb457436d198bd6f4f069c2e` |
| `build/learning_batch/screenshots/batch-contact-577.png` | 1200×1760 | `eaec803645c2d2f6567fa90d6170d241823594bbefc3508e954930a5baa40229` |
| `build/learning_batch/screenshots/batch-contact-589.png` | 1200×1760 | `6d7567efce82be7d806d7b5fab35ff3a453fd5783ac9ab76d41a81b986be3ced` |
| `build/learning_batch/screenshots/batch-contact-601.png` | 1200×880 | `20ddea118ade8afc31b12ab07b3be8de391f4b5051668e45272f310ccc6a3f18` |
| `build/learning_batch/screenshots/batch-page-557.png` | 765×990 | `774d025627ccc2607d03a5e84078fd753e3fe2f29fc8463ffaaf5f39c25aed5b` |
| `build/learning_batch/screenshots/batch-page-603.png` | 765×990 | `49249a40e7227f015cdab01f4d1c53ce0fd60f66b4d01ac764975ddfda8251e8` |
| `build/learning_batch/screenshots/batch-page-604.png` | 765×990 | `d95d3cd82e6229ca014ec09860e1c902c71d2f5416aea6054d43fb2a919da724` |

## 检查边界

接触表支持整体版式、明显裁切及图文位置检查，不支持“全部448页的每个字和符号都按原显示尺寸逐字复读”的结论。本轮只有557、603、604三页另作单页检查。数学与完整16道题答的全文教学审查另见 `research/production/polynomial_linear_division_pedagogy_review.md`，不能由缩略图代替。

本次没有执行附录API、SymPy或Lean，没有点击PDF超链接或重新抓取外部来源，也没有实际读者试用。主代理/前段代理的视觉工作不合并冒充本代理的打开范围。最终验收与生产台账由主代理另行处理；本报告只给出上述实际所见、精确绑定及其限制，未修改任何正式源稿。
