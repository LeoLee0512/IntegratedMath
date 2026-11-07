# 第二十批主编实际页面检查

自动检查时间：2026-10-29T20:01:09.623579+00:00。主编实际打开26个不同审阅版页面：344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 562, 563, 564, 565, 566, 567, 568, 569, 570, 582, 630, 631, 632。这些图片在最终自动检查前由当前PDF以1.25倍渲染，全部实际打开；重建后25张与最终QA截图逐字节相同，355页图像区域像素改变，主编实际重开最终355页复核并绑定新哈希。报告绑定当前最终PDF，不把旧PDF哈希当作最终文件。不以截图生成代替实际查看。

审阅版632页，含完整目录版846页。本报告只声称上述26页放大检查；其余缩略页及其他PDF由前后段报告分别记录。未发现所看页面有未编译公式、缺字、图像损坏、文字遮挡或纸边裁切。

## 实际观察

344—349页覆盖SQ1平方符号及非负比较、SQ2存在和唯一性分离、部分平方根定义、SQ3四分支表、SQ4规范记录判据及二非有理平方。表格中长解集单元自然折行，四行条件与答案对应清楚；347页规范记录证明跨页继续，分子分母和互素条件均可读。

350—356页覆盖配方逐行展开、2a与4a非零条件、判别式双向变换、退化和非退化解集分类、全Q输入下的界以及课后题。353页解集表中的零、单根、双根和正非平方分支清楚。355页图16显示离散八个样本，h与κ标签清晰且与正文一致，图下明示没有把样本连接成完整函数图。未见每张图下额外“原创”标签。

562—570页查看平方与二次方程独立答案，含规范化、零输入、分数系数、无有理根及退化分支。题答跳转文字可见，严格代数依据及先前结论链接保留。部分答案自然续至下一页，不表示内容缺失；本报告未声称逐字放大全部答案页。

582页来源40位固定commit独立成段，没有上一批长行越界问题；来源路径换行可读。630—632页附录二十三给整数二分平方界的不变式、严格差下降、零输入和唯一性证明，接有理平方及全参数方程API。代码自然跨页，632页以solve_quadratic结尾，尾部大段留白正常。数学表达与程序代码的用途已区分。

## 最终文件绑定

- `dist/综合数学.pdf`：`c632cd1d05d72d9bff486934c08f429703df89b51a6197ce10cb9316961ffc5c`
- `dist/综合数学_基础续写审阅版.pdf`：`48631f7b35c352772ace00e6951d1ff1f23c1807d5c41efce11b1a4268f84694`
- `dist/综合数学_完整数学目录.pdf`：`6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55`
- `dist/综合数学_第一章审阅版.pdf`：`53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd`

| 实际检查的最终截图 | SHA-256 |
|---|---|
| `build/learning_batch/screenshots/batch-page-344.png` | `819f33041a5eb7673dd6871638609073d5c5035c0496d9aaa41107cccf13d298` |
| `build/learning_batch/screenshots/batch-page-345.png` | `f81ef675e32789d18637875b09c55eebdaca31737bde8dcb4375aec2387f36e8` |
| `build/learning_batch/screenshots/batch-page-346.png` | `438fab2bdfed31b46fd1bd90e95c294077e59ce6d075251cd4766e5e495b6df8` |
| `build/learning_batch/screenshots/batch-page-347.png` | `d0e26b666f0ed11ed95aa7938aa297273cd8178c8b9f9eab46006a3ab5d04076` |
| `build/learning_batch/screenshots/batch-page-348.png` | `0fd489d0fbbca9279b363a5bebc7cc2f7239ff4ad0a19312aac54e6b82ca3913` |
| `build/learning_batch/screenshots/batch-page-349.png` | `6c2709bf19b6f6f3bf89ffbfd858f538d2e0bdcf03e2ad6d44b98e39ad8fc322` |
| `build/learning_batch/screenshots/batch-page-350.png` | `5f74cdcc851321588513331aaf5bb265b16da3eee47470df3ac66acf29e79ed8` |
| `build/learning_batch/screenshots/batch-page-351.png` | `641f07088af72ed6f0e11b70ba2d74b38068c501995162798cd884192cc77701` |
| `build/learning_batch/screenshots/batch-page-352.png` | `2ed6ae2804b85a5d6ddacccba2ca999b67b0858314b3f9da9bd8c7e521d62374` |
| `build/learning_batch/screenshots/batch-page-353.png` | `36b375bf2224aace3ae901652d1f4e22ed40c31dd151cb8cbd468648df5a21b3` |
| `build/learning_batch/screenshots/batch-page-354.png` | `2754bf3d2e556127a4e48a0d2f8b83a0a22c00235ec18c3917dddb841238cc2a` |
| `build/learning_batch/screenshots/batch-page-355.png` | `4dae9a6afd6fc650730ea19a83b408ce551cf822d70809846ead86f0d438629d` |
| `build/learning_batch/screenshots/batch-page-356.png` | `9c6519f0cdb55a90233f00892316dd5be551ef78b8ba282486117a0f6cdaea85` |
| `build/learning_batch/screenshots/batch-page-562.png` | `b3b0fffa2e9d090b285cb07e0c1ef91abec9ba4e5f2d050c83392c8c1635e698` |
| `build/learning_batch/screenshots/batch-page-563.png` | `0fbce368719e54f9e15bc4da9a0ac75907c7e6e91a2b20a4a029ae33316505a2` |
| `build/learning_batch/screenshots/batch-page-564.png` | `3d238356c01d9e982bd709af1832615ed969bc3bc8805f03fe5649084c4d559b` |
| `build/learning_batch/screenshots/batch-page-565.png` | `fb2af63dc7b25cb0783675e8138292f1f8b3faae375d2b2b51b86a8a9af343b5` |
| `build/learning_batch/screenshots/batch-page-566.png` | `c864e7252cfcc3a53a9647a6b257c9ebd5647eade9256b27377de520d84e29dd` |
| `build/learning_batch/screenshots/batch-page-567.png` | `669134d11b0cdf9ea784c37bf8a3e197856a42621176de1c31eaef2506e7fc83` |
| `build/learning_batch/screenshots/batch-page-568.png` | `5340cdea91814b788f0c5da1e992ff5d131f2d982b7ebc02378325d6eef7bb13` |
| `build/learning_batch/screenshots/batch-page-569.png` | `d1ab8fdf32a95038ded97715ed0c64bc7e29d2829fcde26a039efc4112a433d4` |
| `build/learning_batch/screenshots/batch-page-570.png` | `45f882d33de4b99c521ccfbc0a61f8572231b5f589075058784ab52010541e62` |
| `build/learning_batch/screenshots/batch-page-582.png` | `f99db114aa4022d6a6f1a391cd96c9ae931c1eb7e3c745431a0fabd52a4a86ed` |
| `build/learning_batch/screenshots/batch-page-630.png` | `0754a5232af1cc649356722a09c5b48654948cdda22d06087baaf63d4a2719be` |
| `build/learning_batch/screenshots/batch-page-631.png` | `9f48a83401068375bd7180e01aa4810116bce3663d0bc03f1fed4e9a22d73150` |
| `build/learning_batch/screenshots/batch-page-632.png` | `da42c2f4b8e17bbb192d020800c20e923c8478ff6e72101eb2e06666894c3526` |

限制：没有把有限数值检查或页面观察叫作形式化证明；不是每一页逐字放大校对。16图中的新图是有限有理样本的示意，其一般性质依正文证明。
