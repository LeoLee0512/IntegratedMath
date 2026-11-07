# 第二十二批前半卷与其他 PDF 选页实际视觉复核

自动 QA 时间（validated_at）：2026-10-30T02:12:54.672078+00:00。本次实际视觉记录：2026-10-30T02:16:54.074993+00:00。

绑定 `data/production/batch_validation.json` 自动通过版本，SHA-256：`b84ad0893d860d45deec39baf7f6394e39bbb1e7f3c62b630e375d626f253db5`。四份 PDF 页数依次为：基础续写审阅版 687、完整版 901、第一章审阅版 31、完整数学目录 218；QA 绑定 189 份源文件、48 份产物与 824 张截图。

收到本批 READY 后，先保存当前四份 PDF、全部截图与 QA 的哈希快照，再通过图像工具实际打开以下 40 张当前图像：审阅版 28 张联系表覆盖 PDF 页 1–336，目录单页 3–6，其他三份 PDF 的全部 8 张生成选页联系表。完整版为 63 个选页，第一章及完整目录各为 4 个选页。没有用第二十一批图像或其旧观察代替本次查看，也没有用文本抽取或自动 QA 推测视觉结果。

## 本次实际观察

- 审阅版 PDF 页 1–336：封面、献词、章节入口、课后题、数学推导、表格及图示在联系表尺度排布完整，未见阻断性的裁切、重叠、缺图或明显乱码。第一页有书名、“学习 实践 成长”及 Leo Lee；第二页献词居中。第 25 页为第一章末题、第 26 页为数论部分入口，第 184 页末题后接第 185 页数学教育入口；这些留白与章节内容相接，没有将其误判为渲染失败。
- 当前目录 PDF 第 3–6 页按原图逐页查看：标题层级、缩进、点线、页码均可辨认。第 4 页在第526章续写下列 B2.23“分割的有理逼近、加法与相反数”印刷页码 369、B2.24“分割加法的群律与次序平移”印刷页码 375；第 5 页对应课后题完整解答列页码 607、613，参考资料中新增“分割加法、相反数与次序平移参考资料”页码 630。第 6 页附录二十五“分割网格的有限见证绘图”列页码 684，末项完整可见。目录末页留白较多，条目未裁切。
- 完整版 63 个选页：封面、献词、总目录、MSC 分类条目、已有教学和答案入口、图源表及计算附录均可见。PDF 第 585 页含 B2.23 入口，第 591 页含 B2.24 入口；第 823、829 页分别可见新单元答案入口。第 835 页图源表包含新网格图条目；第 900–901 页显示新网格附录的说明、公式和连续代码，未见联系表尺度的明显越界或缺失。未把未选中的其他 PDF 页列作已看。
- 第一章四选页（1、2、16、31）显示封面、献词、分数节奏图及模拟代码；完整数学目录四选页（1、2、110、218）显示标题、目录说明及分类列表，未见明显裁切、重叠或空白渲染异常。
- 本轮前半卷没有新教学单元正文；本报告的原尺寸查看限于目录 3–6 页。新单元正文、答案及新插图的放大验看由主编另行记录，不能将本报告的联系表观察表述为这些页的逐字或细部验收。

## 尺度与范围限制

审阅版每张 12 页联系表为 1200 × 1760 像素，每页缩略图约 313 × 405。完整版前五张联系表同尺寸，最后一张 3 页联系表为 1200 × 440；第一章及目录 4 页联系表为 1200 × 880。四张目录单页为 765 × 990，按 original 方式实际打开。联系表检查覆盖整体版式和明显异常，不能代替全部单页放大后的细小字形、上下标、证明内容、代码字符或链接目标检查。审阅版 PDF 页 337–687 不属于本报告实际已看范围；本报告也不核验未列出的完整版、第一章或目录页。

## 绑定的四份 PDF

- `dist/综合数学_基础续写审阅版.pdf`：`12dababaeb06e930c29674c8d5d66e9732aa522050cd3a2dd727d23151082fb6`。
- `dist/综合数学.pdf`：`8e03e3ec412c47a93b61bf257856c70e59cfbff815b3afc7dba591222491ab69`。
- `dist/综合数学_第一章审阅版.pdf`：`53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd`。
- `dist/综合数学_完整数学目录.pdf`：`6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55`。

## 实际打开的联系表与覆盖页

- `build/learning_batch/screenshots/batch-contact-001.png`；PDF 页 1–12；SHA-256 `ea17ff1cdd6100d1839447f5cd6ec000a0c7f29836d880d32d6de5f6ce4e63f2`。
- `build/learning_batch/screenshots/batch-contact-013.png`；PDF 页 13–24；SHA-256 `ab224cab814badefac492fefbcfb90e0029c764f78b718424dcb3bc37d6f1cf9`。
- `build/learning_batch/screenshots/batch-contact-025.png`；PDF 页 25–36；SHA-256 `b775357e7fa2b94641545aeb2426c91dc0b65e140aea1476ff40f53e6acccc59`。
- `build/learning_batch/screenshots/batch-contact-037.png`；PDF 页 37–48；SHA-256 `7720a529b3cb54166792513c823977bece5f95b0af2344dce86324b0ddd9527a`。
- `build/learning_batch/screenshots/batch-contact-049.png`；PDF 页 49–60；SHA-256 `9ce6945222de2f0805e968fab470ef10cf3fc4f78ffb6be3179ac78f2faa59c6`。
- `build/learning_batch/screenshots/batch-contact-061.png`；PDF 页 61–72；SHA-256 `63b2fe0c9f11ca38ba4c063aa2a9778230b30486abdf2751541a454bfbec642c`。
- `build/learning_batch/screenshots/batch-contact-073.png`；PDF 页 73–84；SHA-256 `5b338ebf3279b492a9c20bae8c0c65fc669254714b73e2d5a215d679aad37eef`。
- `build/learning_batch/screenshots/batch-contact-085.png`；PDF 页 85–96；SHA-256 `21ea2c1059ae4a1f56c08a9c5bfed5d60bdf923140532ecdd17505e3026c8772`。
- `build/learning_batch/screenshots/batch-contact-097.png`；PDF 页 97–108；SHA-256 `1fb674142c503b84e0457385602011d6f40aa077cddcc46dedd1aec5db579015`。
- `build/learning_batch/screenshots/batch-contact-109.png`；PDF 页 109–120；SHA-256 `310e0d4721d007a44a90d6d9adb6baac22888ad83ebf481652c0ecd4649cba6a`。
- `build/learning_batch/screenshots/batch-contact-121.png`；PDF 页 121–132；SHA-256 `83c82021d61fcc32d5fd86ad6144a066c03503a7535c5b92d45575d04fa64e73`。
- `build/learning_batch/screenshots/batch-contact-133.png`；PDF 页 133–144；SHA-256 `e07abfdb8ece075ce3273e49dba94c71785cd8a0456e201d4c2882d4d7f0cfb8`。
- `build/learning_batch/screenshots/batch-contact-145.png`；PDF 页 145–156；SHA-256 `25ed63a2881987ac9e519f5de919ae9852908a014a357d56b0bbf5283361199b`。
- `build/learning_batch/screenshots/batch-contact-157.png`；PDF 页 157–168；SHA-256 `31c80b7c66a7607aa20cbf3ca79e5f513b9e75f6ccccd7146a32206b8a0de2d2`。
- `build/learning_batch/screenshots/batch-contact-169.png`；PDF 页 169–180；SHA-256 `6ca231b5c48b860a967a707295f69e09142200c3978eb5ec1d5560412578ccf2`。
- `build/learning_batch/screenshots/batch-contact-181.png`；PDF 页 181–192；SHA-256 `aa72320a5e1b63fdadf0f0b100f572598db5e95b8406953364defc974ff36842`。
- `build/learning_batch/screenshots/batch-contact-193.png`；PDF 页 193–204；SHA-256 `d2dda57e2d2acb4c885129ae201ddb3621164f83ac46d0db563e5127099d0155`。
- `build/learning_batch/screenshots/batch-contact-205.png`；PDF 页 205–216；SHA-256 `8db17d1990ff9cf40f5f75bf1ab34b7251edf310e402824e2820c02bc74386f7`。
- `build/learning_batch/screenshots/batch-contact-217.png`；PDF 页 217–228；SHA-256 `a5a40a4a44ef0160a231b574ec743840cfb5a8f66ad77eec15d4048240cc7434`。
- `build/learning_batch/screenshots/batch-contact-229.png`；PDF 页 229–240；SHA-256 `aff57657fe09236ca28416fda8241da57ba2fc1a02eee90f72c7b8abe912946c`。
- `build/learning_batch/screenshots/batch-contact-241.png`；PDF 页 241–252；SHA-256 `5a81534b4389a12ff9578ceccb36cf9ab6da1b572403ae45271b66ae23e44419`。
- `build/learning_batch/screenshots/batch-contact-253.png`；PDF 页 253–264；SHA-256 `552fbc1a3a09faea80c8bcec2380b4922fabfc64c01b79f51d06bee007861916`。
- `build/learning_batch/screenshots/batch-contact-265.png`；PDF 页 265–276；SHA-256 `6b006aca9a0f164c6d872e97550c35adf545bcf981ea285bc5d055eb8abce3a1`。
- `build/learning_batch/screenshots/batch-contact-277.png`；PDF 页 277–288；SHA-256 `3f16fb56441f363b8f98db3eeb857b9a1ef74f9230df2c0db37cc08aec80ccf9`。
- `build/learning_batch/screenshots/batch-contact-289.png`；PDF 页 289–300；SHA-256 `625eefe27ec25d15d96562e692b29eb1702d50a876ac836cf915fea6ba380a1b`。
- `build/learning_batch/screenshots/batch-contact-301.png`；PDF 页 301–312；SHA-256 `13acdcac0696159a2920ef712a5a6d93d21ce86120359369cf5e1f9874f27d10`。
- `build/learning_batch/screenshots/batch-contact-313.png`；PDF 页 313–324；SHA-256 `cffa8881ec8713497587ba07963552aee1d9cf1cda9d4c99125141f42be3c03d`。
- `build/learning_batch/screenshots/batch-contact-325.png`；PDF 页 325–336；SHA-256 `cc637116bdc83b91573c505044409bb85869abce061ef45e6140a98f7bc5e70d`。
- `build/learning_batch/screenshots/full-contact-001.png`；PDF 页 1、2、3、18、217、218、241、250、400、408、416、426；SHA-256 `5e972de5ab0e3df52792fb8b036d42e401d690c806a47861020289f2cbb5ba69`。
- `build/learning_batch/screenshots/full-contact-013.png`；PDF 页 432、439、447、451、455、461、470、477、485、494、501、511；SHA-256 `68ab62278e3cd2867313f06c76ecd55bb95282c974a7a8a298683e29684f356b`。
- `build/learning_batch/screenshots/full-contact-025.png`；PDF 页 520、528、536、544、551、558、564、572、578、585、591、599；SHA-256 `c6192b5d2b2369f4efbf5c1066a53cdbba725bf603f1695922a616562c5dd4ae`。
- `build/learning_batch/screenshots/full-contact-037.png`；PDF 页 689、698、753、764、777、783、791、796、802、807、813、818；SHA-256 `b45b9efddba78671dd647077143f3207e6c6a735124562a95e48e942f154afa0`。
- `build/learning_batch/screenshots/full-contact-049.png`；PDF 页 823、829、835、874、876、879、882、885、888、891、893、895；SHA-256 `b09c5ea9af823dae834fc8c517557a3f848507d2ead3ce98fe5ec222b2cd3520`。
- `build/learning_batch/screenshots/full-contact-061.png`；PDF 页 898、900、901；SHA-256 `e76cc1034d019656d01e688266f58edf1d1f1c302e2179c7e5e5534cbd3793a3`。
- `build/learning_batch/screenshots/ch01-contact-001.png`；PDF 页 1、2、16、31；SHA-256 `7951d2f2fe656285214fcad14c8939f8a79424d08b4a34f5963722a57603547d`。
- `build/learning_batch/screenshots/catalog-contact-001.png`；PDF 页 1、2、110、218；SHA-256 `1855dd0fa8213f41a22c7d4963a6eb12d30a6ba5f3c662a14752d1a23697b833`。

## 实际打开的原尺寸目录页

- `build/learning_batch/screenshots/batch-page-003.png`：`da556c12589dc379f1a121838473dd5cb59cce8eb7cf31ff1d39d7355559c15a`。
- `build/learning_batch/screenshots/batch-page-004.png`：`6c9a6009e6b5aa5f574ca4b9272a5c3f11ee301d213d6529c2237ec6d1004f48`。
- `build/learning_batch/screenshots/batch-page-005.png`：`2a0140062154547f659b0427507f8c7651306493f40c8cc4b9e31b6b2bc5108f`。
- `build/learning_batch/screenshots/batch-page-006.png`：`cf8a96b4f8d1900860b0746daef673e8d8225d190ea3f1190f08fc01a01325a7`。

落盘前重算四份 PDF、40 张已看截图及自动 QA 的 SHA-256，均与看图前快照逐项一致；全部已看截图和 PDF 的哈希亦与绑定的同一自动 QA 完全一致。未修改正式源码、PDF、截图、自动 QA 或 accepted/总验收状态；本文件仅为本轮实际已看范围的独立补充观察，不是整章完成、数学证明或发布批准。
