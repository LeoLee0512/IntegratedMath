# 第20批后段实际视觉复核

结论：在下列实际打开的最终截图范围内，未发现阻断交付的版面缺陷。本记录仅为后段视觉复核，不设定全局 QA 接受状态。

## 最终版本绑定

收到 root 的 READY 后才打开本批最终截图。自动验证报告 `data/production/batch_validation.json` 的状态为 `automated_checks_passed`；validated_at 为 `2026-10-29T20:01:09.623579+00:00`。报告 SHA256：`1166d4b59cd5c777a09fc42e8d3ab44300dff99afcdb8f2c0e6420962465f8c4`。读入时与复核结束时报告字节一致；保留快照 `/tmp/ped20_visual_qa_snapshot.json`。报告列出 177 个来源、46 个产物和 753 个截图哈希；这些总数是报告记录，不代表本审阅者逐个打开了全部产物。

实际重新计算并匹配以下四份 PDF 的报告哈希：

| PDF | SHA256 |
| --- | --- |
| `dist/综合数学.pdf` | `c632cd1d05d72d9bff486934c08f429703df89b51a6197ce10cb9316961ffc5c` |
| `dist/综合数学_基础续写审阅版.pdf` | `48631f7b35c352772ace00e6951d1ff1f23c1807d5c41efce11b1a4268f84694` |
| `dist/综合数学_完整数学目录.pdf` | `6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55` |
| `dist/综合数学_第一章审阅版.pdf` | `53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd` |

审阅版 632 页、全书 846 页为本次构建范围；本报告没有实际逐页查看全书 PDF。正式二次式图 `dist/figures/b2_quadratic_bound.png` SHA256：`7f3e4b0b9a23b47b3b0ec6aa8968d1c01f5a1977e81aadd49f9d19555850d000`，与前次教学审阅打开的 κ 版图相同；本次实际打开其 PDF 排版截图第355页。

## 实际打开范围与观察

以 `tools.view_image` 实际打开 40 张后段联系表：157, 169, 181, 193, 205, 217, 229, 241, 253, 265, 277, 289, 301, 313, 325, 337, 349, 361, 373, 385, 397, 409, 421, 433, 445, 457, 469, 481, 493, 505, 517, 529, 541, 553, 565, 577, 589, 601, 613, 625（数字为 PDF 起页），连续覆盖审阅版 PDF 第157–632页，共476页。末张只有625–632八页，其余十二页。另实际打开16张单页放大截图：344, 347, 350, 353, 355, 356, 562, 564, 568, 570, 571, 572, 582, 630, 631, 632。共56张实际图像，全部重新计算 SHA256 并与上述最终报告逐项匹配。页码均指 PDF 页序，非书页脚印刷页码。

联系表检查正文与答案的页边界、公式和表格是否明显溢出、图文重叠、遗漏整页、异常裁切以及附录代码排版。所有后段联系表均实际看过；并非只依据自动报告或旧图作判断。

放大页分别覆盖 SQ 入口与规范代表判据（344、347）、QC 定义与分类表（350、353）、κ 图及课后题（355、356）、SQ/QC 答案的公式与分支（562、564、568、570、571）、16图来源表（572）、本批来源说明（582）、整数平方根及二次方程计算附录（630–632）。图355的 h、κ、输入标签、最小值标记、图注和有限采样边界均可辨识；点和标记未遮挡关键文字，图与说明保持有理输入的限定。分类表353的四支和有理平方存在条件完整落在页面内。来源582的提交号、文献和审计路径有换行但未截断到页面外。附录630–632的证明、公式和代码没有可见越界；631到632的代码续页保留了缩进上下文。

未发现需要修改源文件的阻断问题。少量跨页公式或说明续行、章节结束留白属于现有排版，未见导致内容丢失的迹象。

## 限制

联系表只能支持整体版面检查，不能代替476页逐字放大校对。除列出的16页外，未声称逐页精读单页截图；未覆盖本代理分工之外的1–156页，也未实际打开其他三份 PDF 的页面。本次未执行数学/API/Lean 检验，未重新进行四稿教学审查，未以有限示例替代证明；自动检查通过仅引用所绑定报告。未修改正文、来源、构建代码、全局 QA 或台账。

## 实际截图 SHA256

| 截图 | SHA256 |
| --- | --- |
| `build/learning_batch/screenshots/batch-contact-157.png` | `31c80b7c66a7607aa20cbf3ca79e5f513b9e75f6ccccd7146a32206b8a0de2d2` |
| `build/learning_batch/screenshots/batch-contact-169.png` | `6ca231b5c48b860a967a707295f69e09142200c3978eb5ec1d5560412578ccf2` |
| `build/learning_batch/screenshots/batch-contact-181.png` | `aa72320a5e1b63fdadf0f0b100f572598db5e95b8406953364defc974ff36842` |
| `build/learning_batch/screenshots/batch-contact-193.png` | `d2dda57e2d2acb4c885129ae201ddb3621164f83ac46d0db563e5127099d0155` |
| `build/learning_batch/screenshots/batch-contact-205.png` | `8db17d1990ff9cf40f5f75bf1ab34b7251edf310e402824e2820c02bc74386f7` |
| `build/learning_batch/screenshots/batch-contact-217.png` | `a5a40a4a44ef0160a231b574ec743840cfb5a8f66ad77eec15d4048240cc7434` |
| `build/learning_batch/screenshots/batch-contact-229.png` | `aff57657fe09236ca28416fda8241da57ba2fc1a02eee90f72c7b8abe912946c` |
| `build/learning_batch/screenshots/batch-contact-241.png` | `5a81534b4389a12ff9578ceccb36cf9ab6da1b572403ae45271b66ae23e44419` |
| `build/learning_batch/screenshots/batch-contact-253.png` | `552fbc1a3a09faea80c8bcec2380b4922fabfc64c01b79f51d06bee007861916` |
| `build/learning_batch/screenshots/batch-contact-265.png` | `6b006aca9a0f164c6d872e97550c35adf545bcf981ea285bc5d055eb8abce3a1` |
| `build/learning_batch/screenshots/batch-contact-277.png` | `3f16fb56441f363b8f98db3eeb857b9a1ef74f9230df2c0db37cc08aec80ccf9` |
| `build/learning_batch/screenshots/batch-contact-289.png` | `625eefe27ec25d15d96562e692b29eb1702d50a876ac836cf915fea6ba380a1b` |
| `build/learning_batch/screenshots/batch-contact-301.png` | `13acdcac0696159a2920ef712a5a6d93d21ce86120359369cf5e1f9874f27d10` |
| `build/learning_batch/screenshots/batch-contact-313.png` | `cffa8881ec8713497587ba07963552aee1d9cf1cda9d4c99125141f42be3c03d` |
| `build/learning_batch/screenshots/batch-contact-325.png` | `cc637116bdc83b91573c505044409bb85869abce061ef45e6140a98f7bc5e70d` |
| `build/learning_batch/screenshots/batch-contact-337.png` | `ff7499e108cf6eb8e56684195fd5a69acfec7e784b2238def515985e4b429a77` |
| `build/learning_batch/screenshots/batch-contact-349.png` | `a57b44bafdef4665f2471771e269c402eaeeb2ab14b3a0b4bc54e61648cbfb96` |
| `build/learning_batch/screenshots/batch-contact-361.png` | `a10df8b4fc0739062562853a5f1de99f8810a329b12331bf5e1e68d8bb88f70e` |
| `build/learning_batch/screenshots/batch-contact-373.png` | `cc20915b92b1f71fcb1e1e87c466467083dae11042507859384b8ee0d0232e4c` |
| `build/learning_batch/screenshots/batch-contact-385.png` | `82a7a93e5221237aa9a43c4073a8c436cb3bdfbe2fd72761e0caa6e5f9d15a4d` |
| `build/learning_batch/screenshots/batch-contact-397.png` | `fe57fc891fbd03b009354f9b79364f37981dcb381ed3ac664d8c46ae2f6d068f` |
| `build/learning_batch/screenshots/batch-contact-409.png` | `2f05e373ac12727780c80c84da4a1f2fda2b9567fe4ee4d724100d49bb0f3fa5` |
| `build/learning_batch/screenshots/batch-contact-421.png` | `a16fbb9a2869ce4fec721e79bb96db1e62ed023aac8d3ea98ed0b22f4306d214` |
| `build/learning_batch/screenshots/batch-contact-433.png` | `c994ecf89b19254d5e58aca84486e238c2835c9bee8620bdfeea7cfb9b648e7b` |
| `build/learning_batch/screenshots/batch-contact-445.png` | `e2f87df555b900c50855a3cf30cabbae7a54ad291980039af862b7e6469480ff` |
| `build/learning_batch/screenshots/batch-contact-457.png` | `9475198bedbc6fdd35cfaadf97766378b09ae2e6429863c61f5823822492447a` |
| `build/learning_batch/screenshots/batch-contact-469.png` | `a2285a8be5839bc0fba5f1375db75510f462f5d6181502dc034c2bb9dfa81a47` |
| `build/learning_batch/screenshots/batch-contact-481.png` | `fd305af6c0147257ba0a30554af7b42d3d4768dce12f0535fa9ef79f98f892ba` |
| `build/learning_batch/screenshots/batch-contact-493.png` | `335a18b8e1f1ddddb35ed1336c1e7e5361a6e91f22cb47ab575e25c56695d6b3` |
| `build/learning_batch/screenshots/batch-contact-505.png` | `529014e649f17265ca16dfad1efd5a96fdcf19dd02031a58e704b86e6776d8f5` |
| `build/learning_batch/screenshots/batch-contact-517.png` | `51a05ba51483e3edabcf8cc9bfd5219774f97accbd915d9cfd42968709e7ec00` |
| `build/learning_batch/screenshots/batch-contact-529.png` | `3120f8f87b8ae44e73027eeb4e173565946521b40a559c78e0c4db8406d6fda6` |
| `build/learning_batch/screenshots/batch-contact-541.png` | `9559ae2b136802c56de54c836164ea453126307a6c80673322267f0b210d641c` |
| `build/learning_batch/screenshots/batch-contact-553.png` | `249a9d551a031715c7a43b515f80f98a5ab16da179ae87d1d057c37a42a4db4f` |
| `build/learning_batch/screenshots/batch-contact-565.png` | `4888d42ed5768520def86dced61f71fa33c2a4e2912c7602722d19a67afe3c22` |
| `build/learning_batch/screenshots/batch-contact-577.png` | `d5532252d1a74608c9a805ff6c333270f5d1f36eee3db93f924ecd7039e5cfd5` |
| `build/learning_batch/screenshots/batch-contact-589.png` | `2df6e344cef5783aeb1579f8bb1c6d71119a227a6dc42f1fb3949ffcff9e9a4e` |
| `build/learning_batch/screenshots/batch-contact-601.png` | `63dc069dd890fdbafc714ddd0b49bc8c3f128476d046df9d0e14a008765a6eb4` |
| `build/learning_batch/screenshots/batch-contact-613.png` | `df3f024da32100c8be3160bd30f8701cd9434b056a4b549abe524894ba34b496` |
| `build/learning_batch/screenshots/batch-contact-625.png` | `d62e68b60313f89606f4a574428198749d040b4520875be467a9972972f5df44` |
| `build/learning_batch/screenshots/batch-page-344.png` | `819f33041a5eb7673dd6871638609073d5c5035c0496d9aaa41107cccf13d298` |
| `build/learning_batch/screenshots/batch-page-347.png` | `d0e26b666f0ed11ed95aa7938aa297273cd8178c8b9f9eab46006a3ab5d04076` |
| `build/learning_batch/screenshots/batch-page-350.png` | `5f74cdcc851321588513331aaf5bb265b16da3eee47470df3ac66acf29e79ed8` |
| `build/learning_batch/screenshots/batch-page-353.png` | `36b375bf2224aace3ae901652d1f4e22ed40c31dd151cb8cbd468648df5a21b3` |
| `build/learning_batch/screenshots/batch-page-355.png` | `4dae9a6afd6fc650730ea19a83b408ce551cf822d70809846ead86f0d438629d` |
| `build/learning_batch/screenshots/batch-page-356.png` | `9c6519f0cdb55a90233f00892316dd5be551ef78b8ba282486117a0f6cdaea85` |
| `build/learning_batch/screenshots/batch-page-562.png` | `b3b0fffa2e9d090b285cb07e0c1ef91abec9ba4e5f2d050c83392c8c1635e698` |
| `build/learning_batch/screenshots/batch-page-564.png` | `3d238356c01d9e982bd709af1832615ed969bc3bc8805f03fe5649084c4d559b` |
| `build/learning_batch/screenshots/batch-page-568.png` | `5340cdea91814b788f0c5da1e992ff5d131f2d982b7ebc02378325d6eef7bb13` |
| `build/learning_batch/screenshots/batch-page-570.png` | `45f882d33de4b99c521ccfbc0a61f8572231b5f589075058784ab52010541e62` |
| `build/learning_batch/screenshots/batch-page-571.png` | `36bbefc9100ea998b49901ef03985db0229725aefbfbd267cbe19a30a0e3b578` |
| `build/learning_batch/screenshots/batch-page-572.png` | `6823664368fa7b4eceef8c30a8089e2ed0dcef06eea0b96b8e02a1100961d426` |
| `build/learning_batch/screenshots/batch-page-582.png` | `f99db114aa4022d6a6f1a391cd96c9ae931c1eb7e3c745431a0fabd52a4a86ed` |
| `build/learning_batch/screenshots/batch-page-630.png` | `0754a5232af1cc649356722a09c5b48654948cdda22d06087baaf63d4a2719be` |
| `build/learning_batch/screenshots/batch-page-631.png` | `9f48a83401068375bd7180e01aa4810116bce3663d0bc03f1fed4e9a22d73150` |
| `build/learning_batch/screenshots/batch-page-632.png` | `da42c2f4b8e17bbb192d020800c20e923c8478ff6e72101eb2e06666894c3526` |
