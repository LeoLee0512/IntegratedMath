# 《综合数学》云端成果备份 · 2026-11-03

本目录按用户“确认上传到这个仓库，全部上传；上传后暂停”的授权建立。它是恢复备份，不是全书完稿或新 Release。原分支正文与历史不覆盖、不合并；本次明确允许备份生成文件，作为原 source-only 分发约定的一次例外。

## 阅读入口与验收状态

- [已验收的919页审阅PDF](project/local-inputs/snapshots/a9363f6/dist/综合数学_基础续写审阅版.pdf)：提交 `a9363f607a818f69d77e8723ac3d3e5666ca4026`，61个学习单元、502题及独立完整答案。[对应Markdown](project/local-inputs/snapshots/a9363f6/dist/综合数学_基础续写审阅版.md)。
- [939页未验收审阅PDF](project/dist/综合数学_基础续写审阅版.pdf)：新增数列比较与子列内容，自动校验已通过，整体实际页面验收未完成。[对应Markdown](project/dist/综合数学_基础续写审阅版.md)。不得把它标作已验收版。
- [完整分类目录PDF](project/dist/综合数学_完整数学目录.pdf)、[中文目录Markdown](project/dist/综合数学_完整数学目录.md)。63部分、534章、6006末级条目是分类结构，不代表全部正文完成。
- [当前源稿与独立答案](project/manuscript/foundations)、[研究和审校记录](project/research)、[覆盖台账](project/data/production)、[构建脚本](project/tools)、[历史快照](project/local-inputs/snapshots)。
- [第32批待验收稿](project/local-inputs/pending-batch32)、[第33批待验收稿](project/local-inputs/pending-batch33)、[第34批已恢复的计划记录](project/local-inputs/pending-batch34)。完整顶层部分仍为0。

当前 `project/dist` 中的伴生包仍是已验收第30批包，不能因为它与939页PDF同处一个目录，就视为第31批验收包。所有原始状态记录按原字节保留。

## 大文件的无损保存与恢复

伴生ZIP及历史Git bundle按原始字节分块存入 `objects/`。重复块只保存一份，每块至多8 MiB；没有使用Git LFS、付费存储或Release。ZIP不是重新压缩，恢复后的SHA-256必须与原文件完全一致。原文件位置、大小、散列、块顺序均在 [manifest.json](manifest.json)，没有把超大包静默省略。

下载或克隆本分支后，在本目录运行：

```sh
python3 restore.py
python3 restore.py --output /path/to/new/IntegratedMath-restored
```

第一行只核验所有文件；第二行恢复全部纳入清单的文件，目标目录必须尚不存在。恢复出的 `_history/repository.bundle` 包含云端已有提交历史，可用 `git bundle verify` 验证；它不包含Git凭据或配置。当前未提交修改另由 `project/` 精确保留。

## 排除与恢复限制

清单 `excluded` 逐项列出按用户要求排除的外部教材缓存、执行缓存及Git管理文件。没有上传凭据、令牌或工作区外的私人文件。保留来源链接、许可证说明及审计记录；不把缓存全文混入备份。

环境恢复后原 `/tmp` 内容已消失。此前仅存于该临时目录、未复制到持久工作区的第34批极值/一致连续四份正文与答案、其部分审稿和来源自查、第35批导数候选计划及当时部分放大页面记录，本次未能恢复。它们没有被冒充为已备份内容；具体已知缺失项见 [unavailable.json](unavailable.json)。第34批持久化的计划与概念审仍在。

上传与核验结果单独登记；本说明不预先宣称远端推送成功。此后按用户要求暂停写作。
