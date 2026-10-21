# 第一部分第一章：公开来源核验

核查时间（UTC）：2026-10-21T16:16:47.298842+00:00。

本轮仅核对等式规则、除零限制、反例、有限完整枚举，以及 Clay 黎曼猜想官方页的访问状态。全部请求使用公开 HTTPS、无需登录，未绕过访问控制。伴生 JSON 保留实际成功请求的 URL、HTTP 状态、内容哈希和字节数；不保存教材题干、答案、插图或连续正文。

## CH01-ALG：OpenStax《Elementary Algebra 2e》

公开入口：<https://github.com/openstax/osbooks-prealgebra-bundle>。

许可依据均已实际取得，HTTP 200：

- [仓库 README](https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/main/README.md) 明确列出该书。
- [LICENSE](https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/main/LICENSE) 声明 **CC BY-NC-SA 4.0**。
- [该书集合元数据](https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/main/collections/elementary-algebra-2e.collection.xml) 同样标明 `by-nc-sa/4.0`。

不能沿用旧印象把当前资料标成 CC BY，或说成允许无条件商业再利用。本稿仅核对数学规则，不复制或翻译原书题干、解答及正文。

| 核验点 | 实际来源 | 结果与范围 |
|---|---|---|
| 等式两边同加、同减 | [m82463：Subtraction and Addition Properties of Equality](https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/main/modules/m82463/index.cnxml) | HTTP 200；分别陈述同减、同加保持等式。书稿的双向等价性须自行补全逆操作说明。 |
| 除法须除数非零 | [m82464：Division and Multiplication Properties of Equality](https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/main/modules/m82464/index.cnxml) | HTTP 200；除法性质明确要求除数非零。乘零保持原等式为真，不代表能从乘零后的等式逆向恢复原式。 |

最初检查的 m82462 是章导言，不将其充作上述性质的证据。

## CH01-LOGIC：Oscar Levin《Discrete Mathematics: An Open Introduction》

公开入口：<https://github.com/oscarlevin/discrete-book>。

[LICENSE](https://raw.githubusercontent.com/oscarlevin/discrete-book/master/LICENSE) 与[活动前言](https://raw.githubusercontent.com/oscarlevin/discrete-book/master/source/frontmatter.ptx) 均取得 HTTP 200。当前核对的是第四版材料，声明 **CC BY-NC-SA 4.0**。许可证另说明已发布第三版及更早版本为 CC BY-SA 4.0；本轮没有把旧版许可套到当前材料上。README 中出现不同分支与版次的混合描述，故许可判断同时使用实际前言。

- [Rules of Logic](https://raw.githubusercontent.com/oscarlevin/discrete-book/master/source/sec_logic-rules.ptx)，HTTP 200：量词与否定部分支持“一个反例足以否定全称命题”；真值表部分要求覆盖所有可能的真假组合，提供有限完整枚举的具体依据。
- [Proofs](https://raw.githubusercontent.com/oscarlevin/discrete-book/master/source/sec_logic-proofs.ptx)，HTTP 200：直接证明中的活动正文明确汇总全部可能情况之后才得出结论。只记录论证方法，不复制案例。

**核验边界：**先删除 XML 注释再判断活动正文。`Proofs` 文件中存在被注释掉的“Proof by (counter) Example”与“Proof by Cases”旧段落，不把它们当作本次活动出版内容。反例依据实际来自 `Rules of Logic`。有限完整枚举不等于有限抽样；核对有限集合所有元素不能自动证明关于全部自然数的命题。

## CH01-CLAY-RH：Clay 官方黎曼猜想页面

官方 URL：<https://www.claymath.org/millennium/riemann-hypothesis/>。

实际结果：`Tunnel connection failed: 403 Forbidden`，发生于环境代理的 CONNECT 阶段。未取得 Clay 页面正文；这不是已观察到的 Clay 源站 HTTP 响应。许可未检查，**官方最新研究状态未由本次请求核实**。

可以把 URL 留作官方待核查入口，但不能写“本次已阅读 Clay 页面并确认截至今日的状态”。访问失败也不能被解释为官方问题已解决、页面不公开或所有公众都无法访问。

## 未采用的候选入口

Richard Hammack 的 [Book of Proof](https://richardhammack.github.io/BookOfProof/) 同样发生代理 CONNECT 403。未取得内容，未依据记忆填写许可；不用于支持本章论证。

## 使用决定

本章可以引用 CH01-ALG 与 CH01-LOGIC 来核对基本规则与逻辑方法，且仍应独立给出定义、条件、证明和原创例题。开放许可包含条件，不等于免除署名或允许一切用途。本轮没有取得、分发或改编任何外部习题；没有核实黎曼猜想官方页面的最新正文。
