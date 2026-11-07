# 新三来源版独立目录视觉继承证明

结论：**218页单独目录的视觉结果通过，方式为精确图像一致后承接旧实际审阅。** 本次实际调用 view_image 次数为0，不声称重新逐张看图。旧审阅者 `/root/part1_pedagogy` 于 `2026-11-05T10:04:05.150940+00:00` 实际看完19张contact（1—218页）并放大2、18、114、178、218页；本次核对并承接的是那份真实已做的检查。

本次核验者 `/root/part1_audit`；时间 `2026-11-05T17:11:13.000552+00:00`。当前 PDF `dist/part1/综合数学_完整数学目录.pdf` 的 SHA-256 为 `2ead115d44e99663d56999ce723c25735a143c7c8c8c2236cf9b8d24f6a5a463`；旧 PDF 为 `cc4e45a20c3ca1e23d4991ab4cc5b4ec3966ea0abd9d7853025ea73f2c485c67`，**两份PDF字节不同**。没有以文件名相同或源目录未改来推断视觉相同，也没有认定差异只来自时间元数据。

## 精确核验链

1. 旧 JSON 与旧实际看图 MD 的字节均匹配已封存提交647d6bc；旧 JSON 记录的MD证据hash正确，明确19张全部 inspected。旧完整目录实际PDF仍保存在publish工作区，hash与旧签和旧validation都一致。
2. 当前 validation 为 automated_checks_passed，当前目录PDF有218页、全页渲染，PDF hash 与实际文件相符；input_sha256全部与当前文件相符。本次绑定 validation SHA-256 `c65aa6df0cc6e02afa06bae58b36c952896ee7ab860f477dd9c9d61fac96afb1`。
3. 当前19条contact逐条与旧记录核页码、路径和实际PNG SHA-256，全部相等；展开页码恰为1—218，无缺页、重复或越界。旧5张实际放大图也全部与当前PNG hash一致。
4. 当前与旧validation记录的全部218张单页PNG hash逐一相等，并核实际当前PNG文件。
5. **独立从新、旧两份实际PDF重新渲染全部218页**，使用既有审查相同的PyMuPDF 1.25倍尺度；每页新PDF所得PNG字节、旧PDF所得PNG字节、现有截图实际字节哈希以及新旧validation哈希五者一致。渲染在内存中比较，没有写入或改动产物。不能仅凭旧截图留在目录中得到此结果。
6. 签署前重核当前validation hash及全部输入hash，未发生版本漂移。每页证明和每张contact及放大图hash见同名JSON。

继承的视觉结论限于已检查尺度上的排版：中文和混排符号可见、长条目换行、章标题与条目分隔、页脚边界、末页6006/97U99收尾。旧实际检查未发现阻断；精确图像相同故未产生新的可见差异。19张contact全页检查和5页放大不等于6006条专业译名逐字审校，不认证PDF链接点击或其他非像素性质。

## 每张已核相同的contact

| 页码 | 路径 | SHA-256 |
|---|---|---|
| 1—12 | `build/part1/contacts/综合数学_完整数学目录/contact-001.png` | `3cb7a619f6a1a9825fea0ecd6978dbdd95be55997dd66c91709206bd5f15a8b2` |
| 13—24 | `build/part1/contacts/综合数学_完整数学目录/contact-013.png` | `22ac332f1c3be61cbb38123452c58285e8f345943aa43efbbc1dcc152541f47e` |
| 25—36 | `build/part1/contacts/综合数学_完整数学目录/contact-025.png` | `d40595bd425533a80da56300c909b75b352f0a2e17b07f0c30e809267a8ae0fe` |
| 37—48 | `build/part1/contacts/综合数学_完整数学目录/contact-037.png` | `b31a3d4baff21ad5c4a2cf507efd4f683c25d22ed931719e82f369a10121825a` |
| 49—60 | `build/part1/contacts/综合数学_完整数学目录/contact-049.png` | `3f181682befe0900d240d0ae3b1cd347882c7a4e0cb383ded78b098471e070ef` |
| 61—72 | `build/part1/contacts/综合数学_完整数学目录/contact-061.png` | `d282f5d005c60d144c73a0be987d28a414f7bc17c535cfad9706f133aeb1df8e` |
| 73—84 | `build/part1/contacts/综合数学_完整数学目录/contact-073.png` | `a6648189c0a66cf396408ea1f0c1725841bb3257677f038f5689063eb9993448` |
| 85—96 | `build/part1/contacts/综合数学_完整数学目录/contact-085.png` | `44295b69bb24e58a485ca078fc98ddd146bc7e58fc32535a7c270768d6907054` |
| 97—108 | `build/part1/contacts/综合数学_完整数学目录/contact-097.png` | `6da3e3de3951472007516fe279c12c8e36ceff23b839c0d9ee8cf89d58a5a7ad` |
| 109—120 | `build/part1/contacts/综合数学_完整数学目录/contact-109.png` | `a18daad3f30e74007ed0ce4f47d53e0196de793121089c7e566ff2e1484ba49b` |
| 121—132 | `build/part1/contacts/综合数学_完整数学目录/contact-121.png` | `6a834d2e80a11662b5f1eaa27c25030b1b5d03093dc82badae27fd0b965754da` |
| 133—144 | `build/part1/contacts/综合数学_完整数学目录/contact-133.png` | `ab01e9b8723f686ac06bce6f8c3238c2755ed60fe74ce937e344625337cad9f9` |
| 145—156 | `build/part1/contacts/综合数学_完整数学目录/contact-145.png` | `e7248ea54675fad593e8f5fe91caa9e79c0e96bb9db3691d0eeaa061acbec912` |
| 157—168 | `build/part1/contacts/综合数学_完整数学目录/contact-157.png` | `13080c7452f5521a831a3426c83b381d16cd194b921a523fb05d6f7fd8915988` |
| 169—180 | `build/part1/contacts/综合数学_完整数学目录/contact-169.png` | `f031129d1807fef9e7901a92303b528b9560b1120ecad6ae95bab7307b7d5eba` |
| 181—192 | `build/part1/contacts/综合数学_完整数学目录/contact-181.png` | `2c6f895e33a29e67c1d8d4ffab283c4069a49395a09638ff7730272722bf575e` |
| 193—204 | `build/part1/contacts/综合数学_完整数学目录/contact-193.png` | `5d00433d27603c2aec26f36a0637297c2aad4560287b6e86a58201c5be2542b2` |
| 205—216 | `build/part1/contacts/综合数学_完整数学目录/contact-205.png` | `ec57aebd9ea93f670cc7c503e85b2ce58cd308eb5a2fbec5717f30b9156de542` |
| 217—218 | `build/part1/contacts/综合数学_完整数学目录/contact-217.png` | `661b4920e14207e285a5027b275c52be8860aa771048d482571f8b4c5d44084e` |

本次没有改变旧审阅文件、PDF、截图、源稿或台账，只新增本MD和同名JSON。原实际审阅MD SHA-256 `7d6ee8c3c147cbfd63a578f645fc4af2a8c8a6d93cc9555793a07f58ae6823f3`，JSON SHA-256 `6e3f359b754b0e040a0daf9cca062160368109d56526fa78b7db43a1083d3620`。当前新JSON SHA-256 `b1dd305fdcfabc2bcc16288d87177f840df69aaef11b45989de7a4bffe62cef0`。

第一部分的11个G专题来源仍pending；本报告不表示完整部分accepted，不签其他两份PDF、构建总门槛或作者验收。
