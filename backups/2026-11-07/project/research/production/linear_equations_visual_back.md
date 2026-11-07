# 第十三批后半部实际视觉检查

结果：在下述声明的视觉检查范围内通过，未发现阻断性版面问题。检查者astra_build。证据绑定最终QA时间2026-10-29T16:48:22.961848+00:00及当前416页审阅PDF；精确PDF与图片SHA-256列于后文。

## 实际查看范围与方法

最终QA完成后，用图片工具实际打开22张联系表，从batch-contact-157到batch-contact-409，连续覆盖审阅PDF物理157—416页，共260页。又以原图精度实际打开batch-page-243.png和batch-page-414.png两张单页，查看新增消元图与附录十六的逐分量公式。没有把生成截图、读取文本或哈希匹配代替实际查看。

查看前保存当前PDF、联系表和两张单页哈希；查看后重新核对所有文件未变，且逐项匹配最终batch_validation.json的产物和截图哈希。页码指PDF物理页；页内印刷页码比物理页码小2。综合稿哈希仅标识同批产物，本检查者没有据此声称实际查看综合稿。审阅1—156页及其他三PDF不在本次分工。

## 实际观察

- 157—231页：有理数、比例、量与单位以及函数正文排版连续；已有插图、公式及表格完整显示，未见图片占位符、明显重叠或越界。
- 232—246页：第528章标题与方程单元出现在函数教学之后，先修链接及分类编号说明可见。一元方程的解集/定义域/参数分支表和二元方程组分类公式均在正文区域内。247页开始集中答案，未把课后答案混入前面的教学正文。
- 243页单页：消元图三个方框和两连接箭头完整，左框为2x+3y=7、4x−y=7，中框保留第一式并把第二式改为−7y=−7，右框为y=1、x=(7−3)/2=2；图下代回两原式均得7。图是方程操作示意，没有坐标轴、向量或交点论证。文字与公式可辨识，没有裁切或重叠。
- 247—378页：答案排版连续，蓝色回题链接可见。368页开始B2.5答案，373页接入B2.6答案，378页结束；参数式、分母与括号未见明显越界。此处为视觉检查，没有逐字符重新审读全部数学证明。
- 379—385页：十图来源表及参考资料排版正常；新增一次方程与方程组来源跨384—385页，长路径在正文范围内。没有把研究请求流水放入书稿。
- 386—416页：代码语法着色和附录说明正常显示。394页上一模块仅末行后留较大空白，416页新增代码收尾后也有留白，均为非阻断分页现象，未见代码裁切或重叠。
- 414页单页：附录十六的第一参数式实际显示为(x,y)=(c/a−(b/a)t,t)，一般记录显示为{(p₁+tu₁,p₂+tu₂):t∈Q}，两式均明确逐分量，不依赖未教的有序对加法或数乘。`line`被明示为程序标签，正文说明只定义有理数对的参数集合，不据此建立坐标直线或交点理论。所有分数、括号和参数条件均正常渲染；下一页续接版本说明与完整代码，未见缺失。

## 当前绑定证据

以下全部22张联系表和2张单页均已在最终QA后实际打开；路径相对于仓库根目录。start/end为物理页覆盖范围，单页记录page为实际放大查看页。PDF及图片在本次查看前后哈希相同。

```json
{
  "captured_at": "2026-10-29T16:49:34.620126+00:00",
  "qa_validated_at": "2026-10-29T16:48:22.961848+00:00",
  "pdf_sha256": {
    "dist/综合数学_基础续写审阅版.pdf": "edcb3c82a79b87134182fcc7a896ae0f1204e219cadd37bd9d8db45a1a2e1881",
    "dist/综合数学.pdf": "0d7c606f566c00039994bca55d04eaecef047da57fd53c3d0a69f95ba262b315"
  },
  "contacts": [
    {
      "start": 157,
      "end": 168,
      "path": "build/learning_batch/screenshots/batch-contact-157.png",
      "sha256": "9440859cfad58539305a51bab71d7490bfe635143d702c25c15286d839d87ba3"
    },
    {
      "start": 169,
      "end": 180,
      "path": "build/learning_batch/screenshots/batch-contact-169.png",
      "sha256": "306e9aa870497943b50f4e1e16d6a82b52f93010ab0554a06c4179d523379811"
    },
    {
      "start": 181,
      "end": 192,
      "path": "build/learning_batch/screenshots/batch-contact-181.png",
      "sha256": "176cfa1a9a1f531c66fa77056d819763300e650d733733379ddc5feb60936444"
    },
    {
      "start": 193,
      "end": 204,
      "path": "build/learning_batch/screenshots/batch-contact-193.png",
      "sha256": "b358a92414846d769df311a74c57e0f2bdca59b8227ae881ab7d8ad99259a537"
    },
    {
      "start": 205,
      "end": 216,
      "path": "build/learning_batch/screenshots/batch-contact-205.png",
      "sha256": "1695eff62ed23758acfdb32606ea18aab6106becce20ec034bc338920f689663"
    },
    {
      "start": 217,
      "end": 228,
      "path": "build/learning_batch/screenshots/batch-contact-217.png",
      "sha256": "ccbbbf435cadae42401d75c5bebff3f6a32fbb681d5b151c624a07e3038be64a"
    },
    {
      "start": 229,
      "end": 240,
      "path": "build/learning_batch/screenshots/batch-contact-229.png",
      "sha256": "618ec6e7f6d0dd0fd2f4433e3ca22b8aae7df217844013d31cb8eee3ac9b9e70"
    },
    {
      "start": 241,
      "end": 252,
      "path": "build/learning_batch/screenshots/batch-contact-241.png",
      "sha256": "583ad65f31e1f7512fd3a99a902ba6639b1aff82a752f55af4fdce6fca7e94bc"
    },
    {
      "start": 253,
      "end": 264,
      "path": "build/learning_batch/screenshots/batch-contact-253.png",
      "sha256": "c43ad30465c31ba632a7739ef744da73dfcd21628267f64bb6f3c0d4ffba6718"
    },
    {
      "start": 265,
      "end": 276,
      "path": "build/learning_batch/screenshots/batch-contact-265.png",
      "sha256": "e15d2a2812dcc1e5ea1ed7391b67821c8e0b38bbedbd060aba51b6ed458cf48e"
    },
    {
      "start": 277,
      "end": 288,
      "path": "build/learning_batch/screenshots/batch-contact-277.png",
      "sha256": "5668149697cc2b362aaf283bbd936a4a053a4d161c590fdf4d1d4e9d6c4d177c"
    },
    {
      "start": 289,
      "end": 300,
      "path": "build/learning_batch/screenshots/batch-contact-289.png",
      "sha256": "4aee36ecc7c6b4cf8c589bc2eec4e30e721b0c5f2450b16993f7ddd33799ec6c"
    },
    {
      "start": 301,
      "end": 312,
      "path": "build/learning_batch/screenshots/batch-contact-301.png",
      "sha256": "3027f5bf14b54b1ecf76de53686d7b80feb8b2f31677ac8156bdb5febafbb2be"
    },
    {
      "start": 313,
      "end": 324,
      "path": "build/learning_batch/screenshots/batch-contact-313.png",
      "sha256": "25596db710f51c4be5813b82214156925c96ea5db9bc4efb61c986c480279e0a"
    },
    {
      "start": 325,
      "end": 336,
      "path": "build/learning_batch/screenshots/batch-contact-325.png",
      "sha256": "0691ab553473107af7c381f1f883eb0fee3d0d5e7b2de4eb805c4a932e3dfdaa"
    },
    {
      "start": 337,
      "end": 348,
      "path": "build/learning_batch/screenshots/batch-contact-337.png",
      "sha256": "343d44be72c5e75cc3ea69d7a8410f1a75ae9125acc7e61ae464c2b9f4378271"
    },
    {
      "start": 349,
      "end": 360,
      "path": "build/learning_batch/screenshots/batch-contact-349.png",
      "sha256": "19c566739d11ecc4967284ce0b1fb4d763a3fc491483144c93def91f4eecba0c"
    },
    {
      "start": 361,
      "end": 372,
      "path": "build/learning_batch/screenshots/batch-contact-361.png",
      "sha256": "61d7ff5730fd96514da1a3707357ad8a272b2c5815b5f1362376b0fb7a1d83ed"
    },
    {
      "start": 373,
      "end": 384,
      "path": "build/learning_batch/screenshots/batch-contact-373.png",
      "sha256": "b89abc20b67b86b4013f2612c60b4d3468a5dc63581ecd8d154e334aab6bc23e"
    },
    {
      "start": 385,
      "end": 396,
      "path": "build/learning_batch/screenshots/batch-contact-385.png",
      "sha256": "63b2f4152342a41f67ac95858c2d1f6296668e889c4019d5f540ab9a4de83877"
    },
    {
      "start": 397,
      "end": 408,
      "path": "build/learning_batch/screenshots/batch-contact-397.png",
      "sha256": "8a4bcfd9d3cacff036954fd52e54bbf03b0cce1e2dc02cf9a1c062c3405c7d0c"
    },
    {
      "start": 409,
      "end": 416,
      "path": "build/learning_batch/screenshots/batch-contact-409.png",
      "sha256": "d7be191668f258665809c12a9001526e50d6ca6d7f45ea94fe9888b157ad5ff9"
    }
  ],
  "single_pages": [
    {
      "page": 243,
      "path": "build/learning_batch/screenshots/batch-page-243.png",
      "sha256": "2f4de17930265bf7d00f1cc057998cf5d7cf92e2d76f3627e71d9025779425ca"
    },
    {
      "page": 414,
      "path": "build/learning_batch/screenshots/batch-page-414.png",
      "sha256": "a91c81592ed966d43fa74ad705dfaf847a9cb3f807a6fadf761a699104b64fee"
    }
  ],
  "status": "passed_within_declared_visual_scope",
  "reviewer": "astra_build",
  "reviewed_at": "2026-10-29T16:52:15.231759+00:00",
  "physical_pages_covered": [
    157,
    416
  ],
  "page_count": 260,
  "contact_count": 22,
  "single_page_count": 2,
  "all_listed_images_actually_opened": true
}
```

## 检查尺度与限制

联系表每页为缩略图，适合识别整页越界、坏图、重叠与分页异常；只有243、414两页在此分工中以单页原图查看。不能由此证明全部细小字形、上下标、代码字符或全部数学推导正确；不声称逐页原分辨率放大或逐字符全审。此记录不是形式化证明、用户验收、整章或整部分完成证明。产物改变后不自动继承该结论。
