# 第26批构建与重点公式实际页图复核

执行者：recover_build21（/root/recover_build21）。28张1.7倍页图逐张实际打开完成于2026-10-30T03:25:02.524518+00:00前；本记录时间：2026-10-30T03:25:59.570009+00:00。

收到明确READY26及ledger已退出0后才启动。第25批3041499六文件快照保持原状。未修改正式稿、工具、来源、审阅台账或提交；未注册aggregate visual acceptance。

## 已实际完成的构建与边界检查

`python tools/build_learning_batch.py --incremental`成功退出0（/tmp/recover26-build.log）。紧接运行/tmp/recover26_pdf_precheck.py，成功退出0；四份PDF逐页逐词按与validator相同的8pt纸张边界条件检查，均零越界。详情/tmp/recover26_pdf_precheck.json。

- 综合数学_基础续写审阅版.pdf：794页；SHA-256 `41e2a2b7d9d26561c145accd816e4c2feab681109da6424cea88e0c4acaa592b`。
- 综合数学.pdf：1008页；SHA-256 `a4ba277fa593402fc386fab901f5c50de4fe143d35e139cf575515184ff5b251`。
- 综合数学_第一章审阅版.pdf：31页；SHA-256 `53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd`。
- 综合数学_完整数学目录.pdf：218页；SHA-256 `6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55`。

## 实际放大查看的范围与观察

根据最终实际PDF定位，多个公式和答案跨页。为覆盖这些收尾，将约20页目标扩展为两版各14页，共28张。PyMuPDF按1.7倍渲染，每张均单独通过view_image打开并实际查看；不是仅生成截图或读取文字层。以下编号均为物理PDF页。

- 审阅423、424 / 合订637、638：自然嵌入四个映射的域与目标、ν复合定义、0/1相容、加法相容及双向保序链清晰完整。四映射行在正文底部完整，ν定义次页承接正常。
- 审阅428、429 / 合订642、643：E=ε⊘2、E⊕E=ε三行链、长夹逼链、取反后两次加法比较和归并ε的长等式均完整。页末宽度正性跨页衔接正常，两侧误差各自严格界完整。
- 审阅433、434 / 合订647、648：min两支与条件对应清楚，δ/(2s+2)分式、上调四行估计、s=0说明和下调δ/(2s)可读。下一页s²/(2s)=s/2、t>0、t²=A+h²>A多行展开、对全体候选X的共同上界说明与A=0边界均完整，无裁切。
- 审阅436 / 合订650：平方方程的A<0、A=0、A>0三支集合及条件对应清楚，根号横线与集合括号完整；有理像集合定义和1<s<2比较行清晰。
- 审阅710 / 合订924：自然嵌入答案中的两行映射、i(r)严格下段集合、ν定义及0/1相容长式完整。此页仅覆盖该答案开头的映射与零一相容，不声称覆盖该题全部后续推导。
- 审阅716、717 / 合订930、931：宽度答案的取反展开、两次严格不等式、加法归并和差的有理相容三行链完整，次页总宽度与两侧误差收尾齐全；嵌套括号和ℝ下标未裁切。
- 审阅720、721 / 合订934、935：上调答案的min两支、正分母验证、h的定义和四行估计在前页完整，后页展开与s=0解释完整接续。下调答案的δ界、h=δ/(2s)、乘回消去、0<h≤s/2及t²展开完整。
- 审阅722 / 合订936：下调答案对全体族成员的共同上界论证、最小上界矛盾和A=0边界完整；根函数定义域/目标、根号以及有理相容示例清晰。
- 审阅724 / 合订938：平方方程全参数三支集合、平移解X=1±s的两候选及代回长式完整，根号、括号、严格号无明显缺字或覆盖；页尾自然留白。

上述28张未见排版裁切、公式重叠、页脚碰撞或不可辨认的所列重点符号。此处为限定页的排版视觉审阅，不代替独立数学审阅，也不构成全书人工视觉接受。预边界脚本生成的末三页截图没有计入本报告实际打开范围。

## 28张实际打开截图的绑定

| 截图 | PDF物理页 | SHA-256 |
|---|---:|---|
| /tmp/recover26_formula_pages/review-423.png | 423 | `f60fd050ba7844e055d2d0121c8d1e9da8f2bbb963358d422c744c87126ff22f` |
| /tmp/recover26_formula_pages/review-424.png | 424 | `ab311e8c86df1cbd6a2273351d7ddd61c094995a28f99b6fdddefd6a02b5fef5` |
| /tmp/recover26_formula_pages/review-428.png | 428 | `b45deb542258c65c88e602a971b1f0c561c3b50a8d2ea6686f534debcad12f74` |
| /tmp/recover26_formula_pages/review-429.png | 429 | `5677d292dcc8759766ca79311417da3a342fca383c2c6cccedb9071fe1624d54` |
| /tmp/recover26_formula_pages/review-433.png | 433 | `f13cef07ef6331e9918834a18ab689c0f3c824a7a6d80b7a0ad09605575f35fd` |
| /tmp/recover26_formula_pages/review-434.png | 434 | `156c613b89a96669a1e14364216cf781dd7957847c4c2a22974b6ea38662adc7` |
| /tmp/recover26_formula_pages/review-436.png | 436 | `d935518cce96e160995ea39780b45d1307dd89e8b828d6a860c4185db3c83a85` |
| /tmp/recover26_formula_pages/review-710.png | 710 | `d43f6c1f5b320ac5ecffd4842b81d7315ffb93d57911154d4fc34367711dfdc3` |
| /tmp/recover26_formula_pages/review-716.png | 716 | `d8438c7cf0de18b56d012f86a2f4bd0a1b8e009508529e22d5ac2386453eabdd` |
| /tmp/recover26_formula_pages/review-717.png | 717 | `3c2c4ee57fe69075d33f43be1c7f8a6d6ae054e64a1aa5139e65dc2207546a69` |
| /tmp/recover26_formula_pages/review-720.png | 720 | `2ce745ef750bb62c2a8204730a851be3ac66a8c03892011914c65bebe0998a18` |
| /tmp/recover26_formula_pages/review-721.png | 721 | `0764ba04a2fa65a7827919804df73f70ba6e3a74f60b27aa9b80e2a5f9458f72` |
| /tmp/recover26_formula_pages/review-722.png | 722 | `a2bc4c8b6e44e2c60eb30bcfc1ecb07181d9e94f3dc0a676030754a76ce920a9` |
| /tmp/recover26_formula_pages/review-724.png | 724 | `4313a481de9f4677ab2f1b2f27690b58a1b78a4914c097bbff1d5421bab7995c` |
| /tmp/recover26_formula_pages/full-637.png | 637 | `bbede87abab672d313fcdbdd48a6b3dca915fd293b572ec0d7f7d8e08e0f0057` |
| /tmp/recover26_formula_pages/full-638.png | 638 | `2769032c9ea1cd1303f677782a46028b8fd8cf8952620a68fe873b0fd4aa7699` |
| /tmp/recover26_formula_pages/full-642.png | 642 | `269a9f9d96734df56748992e4885d5142a0111d681d1c79bfaf84f346795cd8b` |
| /tmp/recover26_formula_pages/full-643.png | 643 | `5427ff5152bfcc9d5c579cd214aec24d1aa4e2e7ae69dabb4075894c882c9cef` |
| /tmp/recover26_formula_pages/full-647.png | 647 | `d183c1eab7f66eec6faaa9a1480bf0aec31ed720b29dfaf076597f9bb20787ae` |
| /tmp/recover26_formula_pages/full-648.png | 648 | `127c38b031e19b8e3901ec1811010c968c51d198826d1ee345fb87d76d0574ff` |
| /tmp/recover26_formula_pages/full-650.png | 650 | `06a59bf1146d6963e5f36d4926c1e830d0c43ffd6714d1ca8bf87187481a171b` |
| /tmp/recover26_formula_pages/full-924.png | 924 | `08f34b1a908523b8a4cfcb9e61b558da89526c9c5d13e36828fe0cbee62e5599` |
| /tmp/recover26_formula_pages/full-930.png | 930 | `be0a06f4b005eb877536cfab446eb772c26d9632b719b4de0c19cde7c889cc89` |
| /tmp/recover26_formula_pages/full-931.png | 931 | `434e18ad1d0994289dbd030e07f8806865de563fbfd5d84aee978b484b51f037` |
| /tmp/recover26_formula_pages/full-934.png | 934 | `1a1efeaeb44506f00f7733aa93c6381e04a56e1be5ec1dbf413ed217e7db021a` |
| /tmp/recover26_formula_pages/full-935.png | 935 | `295d126438c59d653af036ea4d907517180402e5aab66a7ff8bb44a46e368282` |
| /tmp/recover26_formula_pages/full-936.png | 936 | `687b01c4cdb81288a0ae4514c22a882ada569a969d1430a7af01f930fb59c9d4` |
| /tmp/recover26_formula_pages/full-938.png | 938 | `46bb3dc5c52b2819bbee8b86b8146709224b6bc6f757519743b734a7946ca455` |

## 完整validator

完整命令 `python tools/validate_learning_batch.py` 实际成功退出0，整个构建→四PDF预边界→完整validator流水线退出0。最终状态 `automated_checks_passed`，最终QA时间 `2026-10-30T03:27:34.484916+00:00`，QA文件SHA-256 `5d2e35d9362554ca7cf3247a324e513a63ae3d39608c9747e9052d06eb8d2501`。日志/tmp/recover26-qa.log。缺字警告与TeX overflow警告均为空；完整QA登记954张截图。aggregate visual保持待人工接受，本代理未注册。
