# 《综合数学》当前成果备份 · 2026-11-07

按用户“先上传一波，再继续写”保存本轮可恢复成果。本目录是增量恢复备份，不是全书完成声明；原分支根目录及旧备份保留。生成文件沿用用户明确授权的备份例外，不创建Release。

## 阅读入口

- [当前1086页审阅PDF](project/dist/综合数学_基础续写审阅版.pdf) / [Markdown](project/dist/综合数学_基础续写审阅版.md)：75个学习单元、627题及独立答案。自动检查通过，但第35批中段页面复核、最终汇总和验收尚未完成。
- [当前含分类目录的1299页PDF](project/dist/综合数学.pdf) / [Markdown](project/dist/综合数学.md)：63部分、534章、6006节为分类框架，不代表正文全覆盖。
- [最后完整验收第34批1049页PDF](project/local-inputs/snapshots/batch34-logic-sets-finite-counting-20261105T185448Z/dist/综合数学_基础续写审阅版.pdf)：72单元、603题；原检查点ac530aa。对应源稿与审查记录保留在该快照中。
- [当前原稿与独立答案](project/manuscript/foundations)、[研究及审查记录](project/research/production)、[覆盖台账](project/data/production)、[构建脚本](project/tools)。
- [已恢复的后续草稿](project/local-inputs/pending-batch36)：FSP子空间稿、FLI线性无关稿、图与图源、00B15来源提案等。FLI独立数学报告未恢复，需要重新审查；提案尚未应用。

完整顶层部分仍为0；第一部分8项专题来源已核、10项待核。当前dist的基础伴生ZIP仍是第34批包，不是第35批包。dist/part1是保留的旧产物，不用它证明当前第一部分验收；当前状态以恢复审计和来源台账为准。

## 精确核验与大文件恢复

[manifest.json](manifest.json)记录全部纳入文件的路径、大小、SHA256、存储方式及排除范围。大文件以8MiB块存入objects，恢复的是原始字节，不使用付费存储或Git LFS。运行：

```sh
python3 restore.py
python3 restore.py --output /path/to/new/IntegratedMath-restored
```

第一条只核验；第二条还恢复到必须不存在的新目录。历史增量bundle依赖a9363f6提交，可结合2026-11-03备份中的旧bundle恢复历史；正文和脚本可直接从本次project目录恢复，不依赖bundle。

## 边界与未恢复项

本次是当前成果增量备份，并非重新上传所有历史快照。除第34批外的历史快照继续保留在云工作区；2026-11-03旧备份保持原样。可重新生成的页面截图和编译中间文件未重复上传，审查/构建哈希收据保留；外部教材缓存、凭据和无关私人文件排除。未保全的/tmp内容（包括FEX计划、FLI独立数学报告）已不可恢复，不冒充已上传。

本说明与清单在上传前生成。是否已成功上传，以后续远端核验记录与实际提交为准。此次上传结束后按用户要求继续写作。
