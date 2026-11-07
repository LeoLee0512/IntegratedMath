> **历史记录（de08a8a及之前）**：下文描述当时稿件与验收方案，不是本轮最终状态。当前修订、来源缺口及验收结论以 `part1_revision_disposition.md` 和 `part1_acceptance.json` 为准；原样记录已归档 `history/de08a8a/`。

# 第一部分验收器与台账接入检查记录

检查者：`/root/part1_audit`。时间：2026-11-05T08:21:46.966806+00:00

## 范围和限制

这是验收工具的行为检查，不是第一部分数学、教学或视觉通过报告。没有运行全量台账生成器，没有写任何生产JSON，没有编造实际截图审阅或作者批准。本记录可供另一位工具审阅者复核，不能作为正文作者独立数学审读的替代。

## 实际执行

1. `python -m py_compile tools/validate_part1_acceptance.py tools/part1_ledger.py tools/build_production_ledger.py`：退出0。
2. `python /tmp/test_part1_acceptance.py`：退出0。脚本在独立临时根目录创建明确标识为SYNTHETIC的33节计划、两份审读、单页空白PDF、页面PNG、HTML、Markdown及源ZIP，不向真实仓库写入测试验收。正向合成场景accepted；下列12种缺陷分别保持pending：漏一个节、漏目标、数学与教学相同审阅者、作者自行审阅、截图未标实际查看、PDF页数不符、视觉页记录为空、缺少构建检查、计划hash错误、证据路径越出根目录、源稿修改导致过期、视觉报告文件缺失。
3. 真实仓库当前JSON加载为内存副本，对其调用`refresh_part1`及`finish_part1_record`，未调用生成器：33节深度目标成功登记；当前缺证结果pending，部分完成false；所有非00-XX章节/节对象及所有其他部分逐字段等于调用前的深拷贝。

## 当前真实缺证

```json
[
  {
    "stage": "math",
    "reason": "Missing or out-of-repository file: research/production/part1_math_review.json"
  },
  {
    "stage": "build",
    "reason": "Missing or out-of-repository file: research/production/part1_build_review.json"
  },
  {
    "stage": "visual",
    "reason": "Valid build record required before visual acceptance"
  }
]
```

检查输出不代表未来构建已通过。构建、数学/教学以及实际视觉证据齐全后，验收器会重新核查源稿、计划、文件和产物hash；不读取历史accepted作为捷径。

## 检查对应快照

| 文件 | SHA-256 |
|---|---|
| `tools/validate_part1_acceptance.py` | `6b34a1eced42dc4e1f78a2f1663d565626f7f34f67848ae062eec25fc96d0264` |
| `tools/part1_ledger.py` | `6a553c5d69ff02798095a0b83cdf0be0d6abdeb3ca73512fa54edbccd4df5cb9` |
| `tools/build_production_ledger.py` | `c0cdfb01de05ab225af0ab12638b00e76466657ffe21ce3b53ebf32372c541e4` |
| `research/production/part1_acceptance_interface.md` | `52702456e6f6afd7dfe3a3ab983ec8c8bd02665490326d6e05c8c0f6c9908067` |
| `research/production/part1_scope_plan.json` | `3c353bd3ee16589a76a2a12489b0a10396f4769cffc71292be20acdeb0926861` |

## 实现核查点

- 规范仓库相对路径；文件与报告逐字节SHA-256绑定。
- 原分类2章/33节归属核对；声明目标、先修锚点及先修无环核对。
- math/ped独立身份和全33节全部目标显式通过；正文作者不得自审。
- 真实PDF页数、图像可读性及全部PDF页实际查看记录；ZIP内所有计划源文件与审读版本逐字节一致。
- 缺失、陈旧、格式异常、解析器不可用或任一检查失败均pending；作者审阅独立pending，push_succeeded恒false。
- 输出不得覆盖已登记输入、报告、源稿、截图、产物、构建输入或校验器自身。
- helper只注册与提升00-XX；不更改第31批注册代码；生成器只有尾部接入和草稿正文计数口径最小变更。
