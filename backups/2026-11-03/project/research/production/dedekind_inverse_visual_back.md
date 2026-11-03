# 第25批后半联系表实际视觉复核

审阅者：recover_build21（代理任务 /root/recover_build21）。实际查看完成及记录UTC：2026-10-30T03:11:14.153883+00:00。
最终完整自动QA时间：2026-10-30T03:04:40.471787+00:00；该次QA文件SHA-256：5a52b3fc53377bcb1a5ee42428f2255f0b93906b8706d4687b1a34fd0e986993。

本次逐张调用view_image并实际查看36张联系表，覆盖审阅PDF物理337–765页，共429页；前35张每张12页，最后一张9页。页号指PDF物理页，区别于书内页脚。529、541、553、565在一次工具输出因上下文截断后均重新打开并实际查看，未把截断输出计为已审阅。

## 范围及结论

检查是联系表尺度的排版浏览，关注版心、分页、公式/表格/图片整体、截断与重叠。所覆盖429页未见明显越出纸张、大片缺页、内容覆盖或异常渲染。联系表不能充分识别每个小字号字符、代码行或数学细节；本记录不替代数学审阅、逐页放大审阅，也不独立授予aggregate visual acceptance。

- 337–360：多项式、平方与二次方程到有理数空隙正文；图和表均完整。物理357页短段收尾留白属于章尾排版，后续章正常起页。
- 361–408：空隙、切割、加法、非负乘法、有号乘法及环律；图表与多行公式整体位置正常。
- 409–432：有序环、倒数、除法到答案附录开头。物理424页答案附录正常起页；IR/DQ新正文的公式块和性质表位置完整。
- 433–528：前序自然数、整数、有理数等答案段落、公式和表格无明显版面问题。
- 529–576：函数与反函数、方程、不等式、绝对值和坐标答案；多支分类表及长式版心稳定。
- 577–624：幂、有限和、多项式记录、卷积、除法与根的答案；求和上下标和多行公式块未见整体裁切，表格未覆盖相邻文字。
- 625–672：平方、二次式、空隙、切割及加乘答案；集合定义和长推导整体位于版心内。
- 673–696：有号乘法/有序环到本批倒数与除法答案；八行符号表、多行Inv链、三支解集和最后上确界说明未见联系表尺度的截断或重叠。
- 697–720：插图来源目录、参考资料和代码附录开始；资料段落与彩色链接完整。物理720页仅有代码尾行后留白，下一附录正常起页，不记为渲染缺页。
- 721–756：算法及有限计算代码附录；公式、代码缩进与跨页延续在联系表尺度正常。稀疏尾页保留后自然进入下一附录。
- 757–765：一次式除法、平方根/二次方程、空隙图和切割有限见证绘图代码；最后765页代码收尾完整可见，底部留白，无明显截断。此处代码逐字符可读性由主代理的末页放大审阅补充。

另有本代理先前逐张实际打开20张1.7倍重点页的独立记录：/tmp/recover25_formula_visual_review.md；本报告不重复扩大该记录的覆盖范围。自动QA全页边界结果已单独记录，不拿文字层检测代替本次实际看图。

## PDF绑定

- dist/综合数学_基础续写审阅版.pdf：765页；SHA-256 `dc7d0bf566d7542d8d9b81547afb862b68dde6cb080a2d2c03bba96cd0c008a9`。
- dist/综合数学.pdf：979页；SHA-256 `3f720d5fffa96fa1298785c284f492845b5fc51bd2335339b0a3c60e60a939c3`。

## 36张实际查看的联系表及SHA-256

文件目录：build/learning_batch/screenshots/。下列每一行均已实际打开查看。

| 文件 | 物理页 | SHA-256 |
|---|---:|---|
| batch-contact-337.png | 337–348 | `ff7499e108cf6eb8e56684195fd5a69acfec7e784b2238def515985e4b429a77` |
| batch-contact-349.png | 349–360 | `3a92091518b3c7f1dd2065b12bfafd2f224d7f15319bc473fcf6b907486ad6d9` |
| batch-contact-361.png | 361–372 | `aaf208c54084e87ee9ddabe66ae355d70d55d7057ff5450f2a7c440e8ad143b1` |
| batch-contact-373.png | 373–384 | `72aa9f40d98ee3a2064163bf05e1b0468e8b1f5d040774a04cd7d99d08ae762d` |
| batch-contact-385.png | 385–396 | `ea59703ef2aa21b1f7f368ec6a11f650fd14d5ef8f87ff3a8adddd65ddce9f73` |
| batch-contact-397.png | 397–408 | `be65a23b4e715445720656e4fcefeca580f3ba124378a5c833d855720e3cc1c0` |
| batch-contact-409.png | 409–420 | `c3c5b215adff6f910ad8822d5d4d30f73be77598fa4adcfe6e1d684da35b94d3` |
| batch-contact-421.png | 421–432 | `9ca70abf33d6a84d70452f739e41c8010195c279d6dede46477fa29490b3ebe3` |
| batch-contact-433.png | 433–444 | `44bf1bace59c33ab6f70d31927ac394dbac8137547bb1276126729a51e00dfe5` |
| batch-contact-445.png | 445–456 | `cdbc83364d563a134249dd37c4d814b50812c92c666582d09422f06b41d2e72d` |
| batch-contact-457.png | 457–468 | `ecfc4eea5e1af47d570a279b331333fdc7ed1fc78c5db54dc8d24b867446a43b` |
| batch-contact-469.png | 469–480 | `69cd19c05ffa2ab7e6301291a31121de1341c6ff68609e1f422a12fa7e59baf4` |
| batch-contact-481.png | 481–492 | `2b4fc9e288b3d54bde85167909e6e813a5cd92a8fdfec6aeb6a5a9bb18ea551c` |
| batch-contact-493.png | 493–504 | `46538cf6c44b7bebdc2e3ef641a9022ec5047515a29a2fc588b3a5197f5b9bad` |
| batch-contact-505.png | 505–516 | `b6597d2d502251a41e1d2e3a86f0bf9e96081c2d55d9f101c2c40e334064dd9e` |
| batch-contact-517.png | 517–528 | `5e1f60d969c639832c71540e91c718f3832a35a3373bc6205bb5e0d8aa5f0065` |
| batch-contact-529.png | 529–540 | `be52e4ea39d8813dceb8afb78b8d85979ff4cb32ee3868df12dace5aa86e72fc` |
| batch-contact-541.png | 541–552 | `e15e7929e348f5c37ddb25098991719489f6d249d5058c376355f7e78eb08f23` |
| batch-contact-553.png | 553–564 | `4e5bdc1300b3a5ed95bbf17d76a6c6efdbafb35a92432b713703cb1332e61b96` |
| batch-contact-565.png | 565–576 | `1ce79b2ebd8dbe89651232c848ee4f3f1d35dc2dbcf160ea2d31cca3ac6d2705` |
| batch-contact-577.png | 577–588 | `5a7f6547d86ed05360450d61dd9b6cc08467f857b397b81425159cda0c97292a` |
| batch-contact-589.png | 589–600 | `1326204c2198fce06d55c895793e884772313b291cfb0c7561a1caed145df5b7` |
| batch-contact-601.png | 601–612 | `8397ebcb48dfb6468d72c05b3f4d122db1838c5942c794c3b574cc801cbedfe0` |
| batch-contact-613.png | 613–624 | `763df1cea17f6cae63921f85fd03453da03b00e020c31669464c69dfc846fb90` |
| batch-contact-625.png | 625–636 | `a8a6f84e0824d540b040e6e9b02b3300e88479c87eae5c39c6618e250d61b28c` |
| batch-contact-637.png | 637–648 | `e70a1f243a26ffb69a20c01c152941960f16dedbc4d09b17d2c9c5629709a88c` |
| batch-contact-649.png | 649–660 | `85dbd1cc0dfe24df86b0a720a73b4215ce12f6c891761d5c0e464e8cedb29151` |
| batch-contact-661.png | 661–672 | `513c0a31fe3d1c698416b2dfd409ce8e4cd3b8622c4814ea0df8b3aad92171e1` |
| batch-contact-673.png | 673–684 | `c93a263013661fe9cf0aa1d94f3b2d5516afcd2951acf0f37ee2e236a1e4f79e` |
| batch-contact-685.png | 685–696 | `8774a767104ba391d9153a961bd3abb2450e8e506c4c8e80949c51f0087a7f5d` |
| batch-contact-697.png | 697–708 | `ee4d8ea9e321b89c86ef112a85e890f529c4316e6fdc26362a142230cbb27153` |
| batch-contact-709.png | 709–720 | `de4adb7b65ff71ba73247d54cf392d5ca491c1602c4ec6560febf76172ee7f81` |
| batch-contact-721.png | 721–732 | `d9f360435e7fc8a3ad9ce2ab48aec57028ce79176e6d4d98d9ae835e40e749f2` |
| batch-contact-733.png | 733–744 | `6548412c0bcffa0465953f79283bbf6c8e0fbaaffd6e9ca533be264f4bb0273a` |
| batch-contact-745.png | 745–756 | `ccecfa15eecb31dd348f902e76f87f471d40a8516794deb4ac9ad2dd5d05ffb6` |
| batch-contact-757.png | 757–765 | `081c7ab06caa7584d02f9ebfdd3e882b2f2e2089fad75069a75a88da2404abaa` |

36张图哈希均与上述最终自动QA的screenshot_sha256条目吻合。本次仅写/tmp报告；未修改正式稿、正式审阅台账、aggregate接受记录或Git提交；未触碰第24批快照。

最终自动验收时间：2026-10-30T03:04:40.471787+00:00。原报告SHA-256 `5c7d9f3808b378ec1ff7ad665098145b5a0c212d448ce39ff6c3657296a4cbea`。
