# B2.7—B2.8 后半卷实际视觉复核

复核时间：2026-10-29T17:11:44.624862+00:00。复核者：`/root/astra_build`。
绑定自动QA时间：`2026-10-29T17:07:44.056562+00:00`，状态 `automated_checks_passed`；review 445页、full 660页。QA文件检查时SHA-256：`d545f635f60fb2d9726e882c59b2a64213bef23f264e824ea23c20b8486cd76c`。

## 实际打开范围与结论

本轮通过图像查看工具实际打开了下表25张当前联系表，连续覆盖审阅版PDF物理页157—445，共289页；最后一张仅含445页。没有沿用上一批截图或只根据文本/自动QA作视觉判断。另以原始截图尺度实际打开258页新图及443页附录十七。所有列出的图像与PDF哈希在检查结束后再次核对，均与本轮QA相符。

本范围视觉结果：通过，未发现阻断性裁切、文字重叠、缺图、明显缺字方框、公式越界或答案混入教学正文。此结论只授权所列范围的视觉复核，不独自构成全部PDF的总验收。

## 具体观察

- 157—245页的有理数、比例、函数及方程正文排版连续；图像、显示公式和链接未见明显重叠或边缘截断。184页部分标题、200页单元收尾留白属于分页效果。
- B2.7始于246页，B2.8始于255页；两者均接续第528章。251—252页符号分支表、256与259页绝对值分支表在联系表尺度未见压出栏外；262页开始统一答案附录，教学正文与题答分开。
- 258页原尺度查看：中心1、界值2，对应端点−1与3；第一行≤内侧实心端点，第二行<内侧空心端点，第三行≥两外侧带箭头及实心端点，均与各行条件相符。图中文字、刻度、图注清晰；说明明确仅示意有理数成员范围，不声称有理数填满连续实线。下方D限制与仿射系数分支段落未受图像挤压。
- 新答案从393页B2.7、398页B2.8依次展开至404页；405页图源表包含新图，411页新来源说明位置清晰。此处检查了页面布局与可见公式完整性，没有把缩略图检查冒充逐题数学重证。
- 443页原尺度查看：标题、接口与返回记录、t=(c−b)/a、正负系数方向、r<0/r=0/r>0分支均可读。零阈值表用{x∈Q:x≠h}表达去掉中心，未出现未介绍的集合差记号；无向量加法或数乘记号。输入检查责任限定为两求解器与contains待检验值，并单列内部compare；radius参数允许负比较值的说明存在。外侧并集开闭端点显示完整。
- 444—445页完整代码布局未见裁切，末页代码结束后有留白；420页和423页旧代码收尾也有较大留白，均非内容遮挡。

## 尺度和职责限制

联系表为1200像素宽、每张最多12页，适合判断版心、分页、图表存在、明显重叠和边界溢出，不能充分辨认每个微小上下标或证明步骤。258与443页单页截图为765×990像素，以原尺度打开，进一步检查图中端点与附录公式；仍不是印刷级逐字校样。未实际打开本轮1—156页，也未打开其他三种PDF；以下其他PDF哈希只记录同一次构建身份，不表示其页面已由本复核者查看。数学正确性、来源许可与程序正确性分别依赖对应专门审阅及有限计算证据，视觉检查不替代它们。

## 当前PDF绑定

| 路径 | SHA-256 |
| --- | --- |
| `dist/综合数学.pdf` | `060e5ab7f13847512b5a56cde9cb1d75e4a61e165ebbe93477ba158adc39f6f2` |
| `dist/综合数学_基础续写审阅版.pdf` | `139b251dff8fef515c8da317201672f3f2efedcecd701202357a7afd138883ae` |
| `dist/综合数学_完整数学目录.pdf` | `6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55` |
| `dist/综合数学_第一章审阅版.pdf` | `53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd` |

## 已实际打开的联系表

| 截图路径 | PDF物理页 | 像素 | SHA-256 |
| --- | --- | --- | --- |
| `build/learning_batch/screenshots/batch-contact-157.png` | 157—168 | 1200×1760 | `9440859cfad58539305a51bab71d7490bfe635143d702c25c15286d839d87ba3` |
| `build/learning_batch/screenshots/batch-contact-169.png` | 169—180 | 1200×1760 | `306e9aa870497943b50f4e1e16d6a82b52f93010ab0554a06c4179d523379811` |
| `build/learning_batch/screenshots/batch-contact-181.png` | 181—192 | 1200×1760 | `176cfa1a9a1f531c66fa77056d819763300e650d733733379ddc5feb60936444` |
| `build/learning_batch/screenshots/batch-contact-193.png` | 193—204 | 1200×1760 | `b358a92414846d769df311a74c57e0f2bdca59b8227ae881ab7d8ad99259a537` |
| `build/learning_batch/screenshots/batch-contact-205.png` | 205—216 | 1200×1760 | `1695eff62ed23758acfdb32606ea18aab6106becce20ec034bc338920f689663` |
| `build/learning_batch/screenshots/batch-contact-217.png` | 217—228 | 1200×1760 | `ccbbbf435cadae42401d75c5bebff3f6a32fbb681d5b151c624a07e3038be64a` |
| `build/learning_batch/screenshots/batch-contact-229.png` | 229—240 | 1200×1760 | `5773160393ab4305fafbab96ca918f5bbf40da15f9c4b024b75b0b6b7f2920cc` |
| `build/learning_batch/screenshots/batch-contact-241.png` | 241—252 | 1200×1760 | `fe627997c5c56c051803be510a0b8efe38f9e11a4eee7864881aa3cf1c48b4eb` |
| `build/learning_batch/screenshots/batch-contact-253.png` | 253—264 | 1200×1760 | `e6cf0c5719e0c44e46bd46b04d2cbdfebf5484ffeb8fdbaa0256860823d5d207` |
| `build/learning_batch/screenshots/batch-contact-265.png` | 265—276 | 1200×1760 | `53fa31b7eb4f68bf079b3a7faac829410df57c9fd471817bbb4cc45597239209` |
| `build/learning_batch/screenshots/batch-contact-277.png` | 277—288 | 1200×1760 | `3860c2ba793f037e98dbcaa55d2111e3b391bf48706b908d04cd3ce0bac41536` |
| `build/learning_batch/screenshots/batch-contact-289.png` | 289—300 | 1200×1760 | `b4bada1a4f3df4d5c00adc2da9141c52af742bf2f702df1b0150922bfb5c01f0` |
| `build/learning_batch/screenshots/batch-contact-301.png` | 301—312 | 1200×1760 | `4c42606bbb46c1645066e35a1fb0f74d087c6834715746d55ee6a971e2457d70` |
| `build/learning_batch/screenshots/batch-contact-313.png` | 313—324 | 1200×1760 | `0276b92c4a00b855613a710dc989f11164b21116049a03b63607df5879e191d3` |
| `build/learning_batch/screenshots/batch-contact-325.png` | 325—336 | 1200×1760 | `1479f6e0f29962ef69e75b35e784694a8e64ba4ac6b67e49b978250b144a65c6` |
| `build/learning_batch/screenshots/batch-contact-337.png` | 337—348 | 1200×1760 | `a63eb5d50e75577bf250574e34bba5e76f7514406e78e75b901b610ccd6a3d3d` |
| `build/learning_batch/screenshots/batch-contact-349.png` | 349—360 | 1200×1760 | `6db0bd29df40d8beeb7c45d97b086302aacff21acba1851cb4142ad8f14e9b40` |
| `build/learning_batch/screenshots/batch-contact-361.png` | 361—372 | 1200×1760 | `c11ebf32ccd636c9cfc3b4e0f0c58ce7600738c7aada52d0c34cb3153faf1c44` |
| `build/learning_batch/screenshots/batch-contact-373.png` | 373—384 | 1200×1760 | `c696d258dfd70ca0c66c32f5dc069c00a8ab17043d627b8ffa0a09c63019cee8` |
| `build/learning_batch/screenshots/batch-contact-385.png` | 385—396 | 1200×1760 | `a81ff27118e4a9a196a1c57589a101db68f7a10dcb750477659399627aa7c55a` |
| `build/learning_batch/screenshots/batch-contact-397.png` | 397—408 | 1200×1760 | `a970d48bca06265486621a55127c81c83e43fef4536531dc872d406ec817591c` |
| `build/learning_batch/screenshots/batch-contact-409.png` | 409—420 | 1200×1760 | `856d06f46b8aa5748f42484110beb47baf7de61f7570716693c994fad3252050` |
| `build/learning_batch/screenshots/batch-contact-421.png` | 421—432 | 1200×1760 | `24c881d0dfebcc32b338e66b2b90b6dca52d555a540f5f5e633d753b365068a6` |
| `build/learning_batch/screenshots/batch-contact-433.png` | 433—444 | 1200×1760 | `b1dc2ee24371c3544495e50cc92d3c4afb3c7a4ae24b5cdfa14d04dead02bb04` |
| `build/learning_batch/screenshots/batch-contact-445.png` | 445—445 | 1200×440 | `a96afbc986d2a416b997213c7660a5d9ac00a53ae847bc7509a777b2eb48f79e` |

## 已实际打开的单页

| 截图路径 | PDF物理页 | 像素 | SHA-256 |
| --- | --- | --- | --- |
| `build/learning_batch/screenshots/batch-page-258.png` | 258 | 765×990 | `bd2f7bf28a402cb5db4052f5a7b5f292ebf6a9d9b980fedf55b6f9a69cca5a4a` |
| `build/learning_batch/screenshots/batch-page-443.png` | 443 | 765×990 | `67d8582b39a7414f4799da0c4d417bf754e835660e982318857a93f1d28e28bf` |
