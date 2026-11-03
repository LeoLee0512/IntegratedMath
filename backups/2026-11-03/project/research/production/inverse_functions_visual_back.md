# 第十二批后半部实际视觉检查

结果：在声明的联系表检查范围内通过，未发现阻断性版面问题。检查者astra_build；本次时间及精确产物、图片SHA-256见下方证据。

## 范围与方法

图名修正且最终QA完成后，实际重新通过图片工具打开下列全部20张审阅版联系表，覆盖PDF物理157—387页，共231页。没有依赖旧轮图片哈希或把图片生成当作实际查看。查看前先保存当前PDF和截图哈希，查看后再逐项核对均未改变，并与最终batch_validation.json对应记录一致。

审阅版387页，综合稿602页。物理页码以联系表PDF page标签为准；页内印刷页码小2。综合稿哈希仅标识同批产物，本检查者没有查看综合稿。审阅1—156页与其他三PDF不在本次范围。根代理另做的单页放大不冒记为本人查看。

## 实际观察

- 157—216页：有理数、比例、量与单位以及既有函数正文连续，公式分行和表格均在正文区域。181页距离图、189页比例图、206页函数箭头图完整显示，无丢图占位符或明显裁切。
- 217—231页：新增单射满射双射与逆函数正文、公式及表格布局正常。229页反向箭头图已显示E/H集合名称，左右图三条箭头均完整，图题与后续原像正文不重叠。232页才开始集中答案。
- 232—353页：答案连续，返回题目链接呈蓝色，未见公式或表格越界。342页开始B2.3答案，347页接入B2.4答案，353页结束。此处是视觉布局检查，不是逐字符重审每个数学推导。
- 354—359页：九幅插图来源表及参考资料正常排布；359页含新增逆函数来源，长链接和伴生文件路径均在正文区域内。
- 360—387页：源码语法着色可见，说明、公式与代码块未见明显裁切或正文裸TeX。附录十四在383—385页，附录十五在386—387页；新增三性质、逆图及原像公式排版正常，完整模块跨两页继续。368页只保留上一代码块末行后有较大留白，属于非阻断附录分页现象，没有重叠或内容被截断。

## 当前绑定证据

以下20张图片均已在本次最终QA之后实际打开。图片路径相对于仓库根目录；每个start/end都是审阅PDF物理页。PDF及联系表在本次查看前后哈希一致。

```json
{
  "captured_at": "2026-10-29T16:27:13.899421+00:00",
  "pdf_sha256": {
    "dist/综合数学_基础续写审阅版.pdf": "af6f45ed99a8788018fb414b1833fb79843be0c6db8787b0e55ecb8f18a6daaf",
    "dist/综合数学.pdf": "20ab2a250b99d8af53c9aa132cccdbbaa3e262136746e97438e01e0c29c26da0"
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
      "sha256": "dede9730ea6e30725ca35d211a032e771593230323b6e83e4954c77562819dd4"
    },
    {
      "start": 241,
      "end": 252,
      "path": "build/learning_batch/screenshots/batch-contact-241.png",
      "sha256": "334612511919cc7dba7e7c974abfda586f1842b826244973a90778b3bd76da56"
    },
    {
      "start": 253,
      "end": 264,
      "path": "build/learning_batch/screenshots/batch-contact-253.png",
      "sha256": "af09ddbebc256ba7387f24409261c12132547ff74dee94fe76ffbccb52f2b9f4"
    },
    {
      "start": 265,
      "end": 276,
      "path": "build/learning_batch/screenshots/batch-contact-265.png",
      "sha256": "3635d7d565c0823931c0ca5734db85f53dce3456085e89aba6d5156251225384"
    },
    {
      "start": 277,
      "end": 288,
      "path": "build/learning_batch/screenshots/batch-contact-277.png",
      "sha256": "ea59e70d3e3d7192ee99db498f940b1e993d4fab67e674d0644a5496720ba20a"
    },
    {
      "start": 289,
      "end": 300,
      "path": "build/learning_batch/screenshots/batch-contact-289.png",
      "sha256": "de7740035d8e567e0fb1d03989150e379221ded5a5d56a4415624693d7e2dc31"
    },
    {
      "start": 301,
      "end": 312,
      "path": "build/learning_batch/screenshots/batch-contact-301.png",
      "sha256": "b058eaf3b9c37b6bea599533187f0c80db5503a5f732c42009251546061cb987"
    },
    {
      "start": 313,
      "end": 324,
      "path": "build/learning_batch/screenshots/batch-contact-313.png",
      "sha256": "bc9d685dfdc7bdac82919a69a15d524726ec79a23e4408a34ff33fa0ccef52f1"
    },
    {
      "start": 325,
      "end": 336,
      "path": "build/learning_batch/screenshots/batch-contact-325.png",
      "sha256": "472ce2d6147ee2943b6d70fbd0daac539d4e094357da9a5537c43c017b05aa8e"
    },
    {
      "start": 337,
      "end": 348,
      "path": "build/learning_batch/screenshots/batch-contact-337.png",
      "sha256": "853baaf4c4d21fe8aef4ae826491fb9289c73012595539d2793eede72f72f279"
    },
    {
      "start": 349,
      "end": 360,
      "path": "build/learning_batch/screenshots/batch-contact-349.png",
      "sha256": "b16259d001abea185cf881f7f032b39caf2e5e92d2c008b074fbcc31b7558702"
    },
    {
      "start": 361,
      "end": 372,
      "path": "build/learning_batch/screenshots/batch-contact-361.png",
      "sha256": "ad11d21a54285f964e6cc54cd288a1bd525970ba88d90555892d28129e2f2a51"
    },
    {
      "start": 373,
      "end": 384,
      "path": "build/learning_batch/screenshots/batch-contact-373.png",
      "sha256": "bcda0b8df6ea0faf1235140d73d16a94b90dc0e1d280b486128290a4a3b2653b"
    },
    {
      "start": 385,
      "end": 387,
      "path": "build/learning_batch/screenshots/batch-contact-385.png",
      "sha256": "2a12bf639976613dd4596f6058fbdd1bbb47fc712f415046bc5bf533546dc006"
    }
  ],
  "status": "passed_within_declared_visual_scope",
  "reviewer": "astra_build",
  "reviewed_at": "2026-10-29T16:28:44.873376+00:00",
  "physical_pages_covered": [
    157,
    387
  ],
  "page_count": 231,
  "contact_count": 20,
  "all_listed_contacts_actually_opened": true
}
```

## 限制

联系表为每页缩略图，适合发现整页越界、坏图、重叠与分页异常，不能证明每个细小字形、上下标和代码字符正确；没有宣称逐页原分辨率放大或逐字符全审。此记录不等于数学形式证明、用户验收或第529章及全书完成。产物变化后本结论不自动继承，需重新核验。
