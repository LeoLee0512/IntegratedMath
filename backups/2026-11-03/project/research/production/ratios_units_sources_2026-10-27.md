# 比例、量与单位：公开来源核验

B1.20 比与比例；B1.21 有理数值的量、单位与精确换算。仅原创事实摘要，不转载题目、图或连续正文。

核验日期：2026-10-27 UTC。33次真实请求，32次HTTP200；其余状态见下。

## 访问与独立性边界

本轮重新读取cloud-environment-runtime及networking指南，读取本机网络策略并查询运行状态。正常继承代理、保留TLS验证，只读公开GitHub网页和raw文件；无登录、无代理绕过、不取私有链接。先看仓库目录定位，再逐模块读取；错位检索结果明确列为未采用。

未请求官网不是已取得HTTP403；不冒称下载过官方原版或已核最新SI修订。

采用两套不同作者团队、不同课程的公开授权教材系列，但两者同属OpenStax出版体系；不是两个完全独立出版机构。单位算式另按有理数代数独立核对。BIPM草案不计入两套可用教材，也不代替官方规范。

## [RU-PREALGEBRA] Prealgebra 2e

作者：Lynn Marecek、MaryAnne Anthony-Smith、Andrea Honeycutt Mathis。固定提交 ad40c7e3c9a909cde81a24c526f52fe26a51fb14；书名含2e。

https://github.com/openstax/osbooks-prealgebra-bundle

许可：CC BY-NC-SA 4.0。许可含非商业和相同方式共享限制，不是公共领域或无限制商业转载许可。本书不移植教材表达和题文，仅原创陈述标准事实并引用。

- **比与率的区别**（modules/m81303/index.cnxml：fs-id2423119、fs-id1405171、fs-id2778087）：该节题名Ratios and Rate。比比较数或同单位的量；同类量原先单位不同时先换同单位；率比较不同类型测量。本书以有理商定义比时独立补足后项非零与负值/模型范围，不把日常例子当通用公理。
- **比例及交叉相乘条件**（modules/m81311/index.cnxml：fs-id1166492018126、fs-id1166498443767、note fs-id1166489098476）：比例a/b=c/d明确b≠0,d≠0；正文表述与交叉乘积相等当且仅当。该说明用于核对条件；本书两向证明须从已经证明的有理运算推导，不能仅照教材算法省略非零条件。
- **精确长度与时间换算**（modules/m81330/index.cnxml：table fs-id1627796、para fs-id1561154、table fs-id1448508）：实际读到1min=60s、1h=60min、1km=1000m、1cm=1/100m；故本书采用这些精确约定后可独立算出1h=3600s。只取这几项，不采用同表中以365天概括一年的说法，也不把其近似英美制换算数据提升为精确常数。

## [RU-PHYSICS] University Physics Volume 1

作者：Samuel J. Ling、Jeff Sanny、William Moebs。固定提交 2300d5b8ca2571dacc6ec25ebef56ba8d49000a2；不推断出版页码或最新SI修订年份。

https://github.com/openstax/osbooks-university-physics-bundle

许可：CC BY-NC-SA 4.0。只作来源交叉检查，不转载正文、表格、题目或图。

- **基本单位、导出单位与前缀**（modules/m58270/index.cnxml：table fs-id1168326798535、para fs-id1168329125088、table fs-id1168326843228）：基单位表列长度m与时间s；速率单位m/s作为长度/时间导出；前缀表列kilo为10^3、centi为10^-2。本批不使用旧教材精密基单位实现说明来声称最新SI规范。
- **换算因子方向**（modules/m58271/index.cnxml：para fs-id1168328205340、fs-id1168328184191）：明确每千米1000米，按目标单位选择换算因子并消去旧单位；时间例中明列每分钟60秒。书中部分英美制数值为近似，本书只用已明确采用的精确米/厘米/千米/秒/时约定。
- **量纲只是检查条件**（modules/m58272/index.cnxml：para fs-id1168328194195及其后列表）：可相加各项与等式两边须同量纲，标准数学函数的输入受相应量纲条件限制。这里是必要的物理一致性检查，不能推出同量纲一定同量种，也不能凭量纲相符证明物理模型正确。本批用显式量类别标签限制模型运算，不引入未证实数理论。

## [RU-BIPM-DRAFT-AUX] SI Brochure edition 9, semantic encoded version (DRAFT)

作者：内容署名BIPM；转码仓库维护者Metanorma/Ribose。固定提交8de8bf0890e0bd80f6201be3e9a6da8886384817；root声明9e v3.01，2024-08-28。

https://github.com/metanorma/bipm-si-brochure

许可：README称官方BIPM文档按CC BY 3.0 IGO发布。不据此分发第三方文件；不将此草案用作书稿官方规范证据。

- **草案边界**（README开头、LICENSE段；sources/si-brochure/3.01/si-brochure-en.adoc头部）：README明确开发中和不得作官方用途。root虽含status:in-force，仍不能抵消整个转码项目的DRAFT警告；不将其当官方原文已核。
- **辅助交叉检查而非正文规范引用**（sections-en/02-system-of-units.adoc：行418–436、507–512；03-multiples.adoc前缀表；04-non-si-units.adoc非SI单位表）：读到扭矩与能量同量纲但不同性质、Hz与Bq用途区分、小时3600秒及前缀关系。只作辅助一致性线索，未获得官方原文前不把这些例子标为官方核验通过，也不要求本批小学单位入口展开这些物理概念。

## 独立数学核对

- **比例交叉相乘**。条件：a,b,c,d∈Q，b≠0,d≠0。a/b=c/d两侧乘bd得到ad=bc；反向两侧乘(bd)的倒数或依次除非零b,d恢复比例。若容许零分母，交叉等式可以成立而原比例未定义，因此条件不可删。
- **共同倍率与分配模型**。条件：相同比a/b=c/d且b,d非零；物理分配另要求T>0,m≥0,n>0。倍率k=d/b非零且由b*k=d唯一确定；交叉等式推出a*k=c。分配模型令x=Tm/(m+n),y=Tn/(m+n)，m+n>0使分母合法，x≥0,y>0。这里只是本书指定有理数量模型，不是自然界普遍比例定律。
- **单位换算不变量**。条件：同类精确模型量，单位u,v相对同一参照量的尺度su,sv为正有理数。xu=yv等价于x*su=y*sv，故y=x*su/sv。正尺度保证唯一及正负保持；复合时中间尺度消去。若s_cm=1/100,s_km=1000,s_h=3600，则km/h到m/s倍率1000/3600=5/18，反向18/5。量与其数值须区别。
- **类别标签与量纲边界**。条件：本批只在明确定义的有理数模型类别内计算。同类量相加/比较；同类量的比须先统一单位；不同类量的率保留量类别与单位。量纲相同不是类别相同的充分条件，量纲检查也不证明模型或数值正确。未使用实数完备性。

## MSC定位

第63部分97-XX数学教育，第526章97Fxx算术与数论教育。B1.20定位97F80；B1.21定位97F70。均只登记教学桥接的部分目标，不称整章或整叶完成。

## 实际请求与哈希

- `bipm_candidates`：HTTP 200，字节数 201393；SHA-256 `4b0f5946edd9a766b8a0f6a0bf7d2a5b6e161b0872b9c7698eb8bd6d9102fd3c`。
  https://github.com/search?q=BIPM+SI+brochure&type=repositories
- `bipm_draft_non_si`：HTTP 200，字节数 6651；SHA-256 `5e690df1806a71b87a8076c2e63dd20d0e95f48fdd276e927be1807acc12545a`。
  https://raw.githubusercontent.com/metanorma/bipm-si-brochure/8de8bf0890e0bd80f6201be3e9a6da8886384817/sources/si-brochure/3.01/sections-en/04-non-si-units.adoc
- `bipm_draft_prefix`：HTTP 200，字节数 4793；SHA-256 `1a8db218a7e0e834b785d3c76b049c75895e5ff4f425b4f8b2312a14adc75774`。
  https://raw.githubusercontent.com/metanorma/bipm-si-brochure/8de8bf0890e0bd80f6201be3e9a6da8886384817/sources/si-brochure/3.01/sections-en/03-multiples.adoc
- `bipm_draft_units`：HTTP 200，字节数 56528；SHA-256 `b6a5dc12caacb8ee61a8011233182b028f72a2ea0c946130285f85db915d2dc5`。
  https://raw.githubusercontent.com/metanorma/bipm-si-brochure/8de8bf0890e0bd80f6201be3e9a6da8886384817/sources/si-brochure/3.01/sections-en/02-system-of-units.adoc
- `bipm_readme`：HTTP 200，字节数 8451；SHA-256 `83831283f9e78984d69f2f34ca54281d211e79729fa61c9dbf53061986b0da76`。
  https://raw.githubusercontent.com/metanorma/bipm-si-brochure/main/README.adoc
- `bipm_reference_tree`：HTTP 200，字节数 269169；SHA-256 `fd6f25f0ed833f3b73d39543efe37f3adf677fe9b7c02a1cb5ef4c848a2aaec3`。
  https://github.com/metanorma/bipm-si-brochure/tree/8de8bf0890e0bd80f6201be3e9a6da8886384817/reference-docs
- `bipm_repo`：HTTP 200，字节数 346318；SHA-256 `105e5e5294c24ccc14cf7676a12ee92cf7bc9d0597d1bad0eaa6445129c710a1`。
  https://github.com/metanorma/bipm-si-brochure
- `bipm_repositories`：HTTP 404，字节数 None；SHA-256 `None`。
  https://github.com/orgs/BIPM/repositories
- `bipm_source_root`：HTTP 200，字节数 1508；SHA-256 `c4fe39f523e859e32e026e5f07a6e95ede224a9c4e84d71bf703a910527fec2f`。
  https://raw.githubusercontent.com/metanorma/bipm-si-brochure/8de8bf0890e0bd80f6201be3e9a6da8886384817/sources/si-brochure/3.01/si-brochure-en.adoc
- `nist_repositories`：HTTP 200，字节数 202379；SHA-256 `9b9b140279c9aefd177fa975561f262cf7947862e6a7d5cc14e4a59b2a452387`。
  https://github.com/orgs/usnistgov/repositories?q=units
- `nist_si_repositories`：HTTP 200，字节数 412204；SHA-256 `3c90a1e72f12aa761db8f20589738cfa92bf19e315c613a73cd230dd342c3598`。
  https://github.com/orgs/usnistgov/repositories?q=SI
- `openstax_collection`：HTTP 200，字节数 5043；SHA-256 `309fa072672372d1e46d52031167c21d9a120d1cdfdf3001548e1ca2975077a2`。
  https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/main/collections/prealgebra-2e.collection.xml
- `openstax_license`：HTTP 200，字节数 21442；SHA-256 `ab1a44bbba58252630134574d7b2534813339240eb645825ffcc2487dbe8114a`。
  https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/LICENSE
- `openstax_measure`：HTTP 200，字节数 161549；SHA-256 `ae49551fc94b1d09699bbd716e7b6f3a3352315b793fccf70aeeac9c63d8b2df`。
  https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81329/index.cnxml
- `openstax_measure_system_final`：HTTP 200，字节数 172178；SHA-256 `fb86a56f6cbe7cceee3657f6b8d12deb06695c80638e644d710ad8bc88e45ee2`。
  https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81330/index.cnxml
- `openstax_measurement`：HTTP 200，字节数 116178；SHA-256 `92589b2290e7ecae69e44e09d213e71404d2c01183a4a7fae0c4c0a759d73b71`。
  https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81326/index.cnxml
- `openstax_measurement_systems`：HTTP 200，字节数 94347；SHA-256 `cb3d6989619d946b6466f316357391d780701e22eb6fd5549d95b27610018738`。
  https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81318/index.cnxml
- `openstax_metric`：HTTP 200，字节数 115973；SHA-256 `296b89db4f2b8090bc667d3a35bfddd736d7b9e4f710c4527edd4c08b8872629`。
  https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81328/index.cnxml
- `openstax_percent_proportion`：HTTP 200，字节数 58591；SHA-256 `04b96b8548d2f02b7fcd2fac31992e76c6450599276f229fcb9f0ba40cf663d2`。
  https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81308/index.cnxml
- `openstax_preface`：HTTP 200，字节数 26760；SHA-256 `1c7cf6eda8be5021f1f33dc22069f5a3db50d1412a024bb57c7268b25db7f9df`。
  https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81241/index.cnxml
- `openstax_proportions`：HTTP 200，字节数 147021；SHA-256 `be5387c846439a946cff737d3522a07d1bf4cf1ecc322074c0aa01ed0e1bf5c8`。
  https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81304/index.cnxml
- `openstax_ratio`：HTTP 200，字节数 82440；SHA-256 `62c2e97599f0cc79fc9d835caf4d2e3fb238a83ef2eb3fc21c28d68d3b3a09d4`。
  https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81302/index.cnxml
- `openstax_solve_proportions`：HTTP 200，字节数 166142；SHA-256 `f7ec28ad31af989be3482e8a59b8e3fc2a47190b30573d90062658acc170528f`。
  https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81311/index.cnxml
- `openstax_systems_measure`：HTTP 200，字节数 64823；SHA-256 `b8d988ce0fa05acf3491fb754d33f36204363dcb8df7e45acfcb832f01e6f7b2`。
  https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81327/index.cnxml
- `openstax_tree`：HTTP 200，字节数 267514；SHA-256 `0585c0ed75cb4ab70cbcd5f7e0ee48223e4fc50cda64ada1a758783c144c096e`。
  https://github.com/openstax/osbooks-prealgebra-bundle/tree/main
- `openstax_units`：HTTP 200，字节数 88953；SHA-256 `94f83224b28b2f328df6af9824d52d7b987a9b4e74d4056ad9ccb04e3b477a00`。
  https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81303/index.cnxml
- `physics_collection`：HTTP 200，字节数 8981；SHA-256 `c55d0b6baf5b379e5a21afbecd07e4b35ee3170a8234bdc8cfedc22fcb8a0f04`。
  https://raw.githubusercontent.com/openstax/osbooks-university-physics-bundle/main/collections/university-physics-volume-1.collection.xml
- `physics_conversion`：HTTP 200，字节数 26564；SHA-256 `d29f5478b77cada00bdb769b4b87dd7f0e51ed39dffdba07a1d1a1dd1c283184`。
  https://raw.githubusercontent.com/openstax/osbooks-university-physics-bundle/2300d5b8ca2571dacc6ec25ebef56ba8d49000a2/modules/m58271/index.cnxml
- `physics_dimensions`：HTTP 200，字节数 37131；SHA-256 `ea6c3b0bc1942a32691d8ae39c9ded766900429ce8a567d504963e8c7ec66028`。
  https://raw.githubusercontent.com/openstax/osbooks-university-physics-bundle/2300d5b8ca2571dacc6ec25ebef56ba8d49000a2/modules/m58272/index.cnxml
- `physics_license`：HTTP 200，字节数 21013；SHA-256 `8e63d319b3d085a7571278ea3033d713131ac0d330b87cf9ac854e05ee44229d`。
  https://raw.githubusercontent.com/openstax/osbooks-university-physics-bundle/2300d5b8ca2571dacc6ec25ebef56ba8d49000a2/LICENSE
- `physics_preface`：HTTP 200，字节数 22378；SHA-256 `d44a54f98e7759519a64cf938f7d2c15137a1afcf341ac0d4a209ab011226344`。
  https://raw.githubusercontent.com/openstax/osbooks-university-physics-bundle/2300d5b8ca2571dacc6ec25ebef56ba8d49000a2/modules/m62204/index.cnxml
- `physics_tree`：HTTP 200，字节数 266313；SHA-256 `f4cb231cfc1d143b9eace2a469cae9b6ad01b1f0949ac10c6072c9c00e00f596`。
  https://github.com/openstax/osbooks-university-physics-bundle
- `physics_units`：HTTP 200，字节数 42940；SHA-256 `4116491d82fc9c69d374b14aefa1caa822e3258a18ef214ee4d0cc3724cb0f9c`。
  https://raw.githubusercontent.com/openstax/osbooks-university-physics-bundle/2300d5b8ca2571dacc6ec25ebef56ba8d49000a2/modules/m58270/index.cnxml

未采用的错位定位结果：openstax_ratio, openstax_proportions, openstax_measure, openstax_percent_proportion, openstax_measurement, openstax_systems_measure, openstax_metric, openstax_measurement_systems。
这些定位请求返回的标题分别是平均数/概率、平方根、公式、利息、几何或恒等元等；没有将成功下载当作相关知识已核。GitHub组织/搜索/目录请求仅用于定位，不算数学来源。BIPM组织请求404已保留。

## 未核事项

- 没有直达BIPM/NIST官方全文或核对最新SI修订。
- 没有将版权教材题干、解答、表格或图写入书稿。
- 没有宣称两套同出版方教材完全独立。
- 没有运行机器形式证明。
- 没有把真实测量误差、偏移温标换算、无理长度或一般量纲理论视为本批已讲完。

第三方完整响应只存/tmp/integratedmath-ratios-units-audit；仓库仅存此原创说明及URL、状态、字节数、哈希和必要许可短摘。
