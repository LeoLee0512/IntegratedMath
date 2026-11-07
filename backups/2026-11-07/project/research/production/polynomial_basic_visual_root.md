# 第十七批主编实际放大页面检查

最终自动QA时间：2026-10-29T18:34:29.983841+00:00。本报告对应本次543页审阅版，不以此前510页图像替代。

主编实际使用view_image打开21张不同单页图。先从已完成构建的PDF渲染至/tmp/poly-root-view，最终QA结束后逐字节核对：20张与最终截图相同；第300页图像区域的渲染像素不同，因此又实际打开最终batch-page-300.png重查。未把不同截图宣称字节相同。页码为PDF页码，不是页脚印刷页码。全部21页确实放大查看，没有只按文字提取或文件存在批准。

检查所见：记录/补零分段公式、规范化、全指标相等、求值、零和次数条件清楚；第300页新图三行系数及虚框说明完整且图注同页；第312/490页负分数通分步骤编译正常；题答蓝色链接可辨，自动跳转检查另见QA。第541页目录与长文件名分行正常，第542至543页add函数连续跨页，未丢代码；第492/543页留白为短末段的自然分页，非阻断。未见损坏图片、公式残码、重叠、裁切或页界溢出。

此报告仅覆盖下列21张放大页；全部缩略页与其他PDF选页由另外两份视觉报告说明，不据此宣称每页均全尺寸校对或数学无误。

## 最终PDF绑定

- `dist/综合数学.pdf`：`ce03c5b1932c972bb570398feedcb12d1ab5f162d0d876de66903fa6b09c5553`
- `dist/综合数学_基础续写审阅版.pdf`：`e82caf15a299323ad26a68a8907fbc52193faac87b3e2004612d06ed449c1f6c`
- `dist/综合数学_完整数学目录.pdf`：`6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55`
- `dist/综合数学_第一章审阅版.pdf`：`53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd`

## 实际打开且核对最终截图的页面

- PDF第297页：`build/learning_batch/screenshots/batch-page-297.png`，`b9957f6a3e562ef4ef54765100a10f06bf81d116f8dc58c353453fec6aa1dee0`
- PDF第300页：`build/learning_batch/screenshots/batch-page-300.png`，`399c5ea69986a0dfb48f9a42b37a1da78d245221628f01b1258ec0a90e21310a`
- PDF第302页：`build/learning_batch/screenshots/batch-page-302.png`，`9f72da8279ab32962811f5c0068af53e4912c86221b54ae512444dc9d1575bd7`
- PDF第303页：`build/learning_batch/screenshots/batch-page-303.png`，`810bad18304e7e84fb7ca7ad4b28edd8919840f05717a062b477caf73f66c3ca`
- PDF第305页：`build/learning_batch/screenshots/batch-page-305.png`，`438b97c343e1b0a09811d7cc538b1ee4216bddd1ad1ea4aa62a51e63cd377679`
- PDF第306页：`build/learning_batch/screenshots/batch-page-306.png`，`e4f2034db33b3daa9561e55fe89f6e0bf1321b1ee52dab4a4d8477905cd76063`
- PDF第308页：`build/learning_batch/screenshots/batch-page-308.png`，`8618119e64fe0d5573b72654aa222d0078068188ab1acc268beec227a8c25286`
- PDF第310页：`build/learning_batch/screenshots/batch-page-310.png`，`896800a3e11d224528afcd32642c296e1e20134c935aa99e5330820e928abdf0`
- PDF第311页：`build/learning_batch/screenshots/batch-page-311.png`，`84ebdc5d8d4a1883edd4c104d70600d92f49c7dcffeeaed963827aaf392e30f7`
- PDF第312页：`build/learning_batch/screenshots/batch-page-312.png`，`14b3f0cec9a4d077fe443ac3729160153b14aa91c985f23b3b21786767f114f2`
- PDF第480页：`build/learning_batch/screenshots/batch-page-480.png`，`a55eb7727e5aeaa79de637c06bdf3d3c708f52a811c884286ed5920faf47c003`
- PDF第483页：`build/learning_batch/screenshots/batch-page-483.png`，`9a02cda8973bb356a252b6a9cd0e2a0c3c448a249ce3f318c38af21c50ae8d21`
- PDF第485页：`build/learning_batch/screenshots/batch-page-485.png`，`137c5172690d795e69558943354085e06b72f9067b5f93b94e747e54a8b9a905`
- PDF第486页：`build/learning_batch/screenshots/batch-page-486.png`，`390fa4c997c143f45010bc0fa75d2761564c29f10e3d4253bdc80bce0e55fa40`
- PDF第489页：`build/learning_batch/screenshots/batch-page-489.png`，`28c32208a1c0f7666e0a924bc332a1802e8e7a02882330adf8218ef50e9b6a4f`
- PDF第490页：`build/learning_batch/screenshots/batch-page-490.png`，`b928974647e3754a30924b9e4e6da2e44878cdb85bce1591e9d80ec10321fcab`
- PDF第491页：`build/learning_batch/screenshots/batch-page-491.png`，`d8dff87abce53f90fb4ac6f167303916b56d30859ebd42d9ef7933c11a1befd7`
- PDF第492页：`build/learning_batch/screenshots/batch-page-492.png`，`398dde547c3c5b9f8cce693bc63096dce07515b3b058c5dc8c2de805a1bcac75`
- PDF第541页：`build/learning_batch/screenshots/batch-page-541.png`，`3bdb30daaf0eb44e160e5d27df11acbc0b1b10973ffb16852b07f8cd77ff04ff`
- PDF第542页：`build/learning_batch/screenshots/batch-page-542.png`，`46c230418f01f011d4384aec0ce6f6271d5be178a0a9b1c684b7ffd5085aadde`
- PDF第543页：`build/learning_batch/screenshots/batch-page-543.png`，`c4ecdcd9cf6f1e8386804862d9134d0a7f0a61afa529ba325cd63eed60e464cc`
