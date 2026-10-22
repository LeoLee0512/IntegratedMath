# 构建、发布与历史保留

Git 保存可编辑源稿和人工审校记录。`dist/`、`build/`、生成的章节图片与构建报告被忽略；它们在本地仍可使用，并随 Release 资产分发。`tools/style.css` 是样式源，构建时复制到 `dist/style.css`。旧提交中的产物保留，不执行历史清洗或强制推送。

## 从源码得到审阅包

按 README 安装依赖，依次运行：

```sh
python tools/build_ch01_review.py
python tools/validate_catalog_chinese.py
python tools/validate_ch01_review.py
```

检查 `build/review_ch01/contact-*.png` 的全部章稿页面，再放大查看章首、公式、插图、题答链接附近和新增段落；另查独立目录与全稿的代表页面。验证脚本会把视觉状态重置为待检查，避免沿用旧结果。

只有实际看过后，才能把 `data/ch01_validation.json` 的 `visual_review` 改为以下形状；页码、时间、结论填写实际检查值，`artifact_sha256` 复制报告根部的同名字段，将记录绑定到本轮全部产物：

```json
{
  "status": "inspected",
  "reviewed_at": "实际检查时间（含时区）",
  "pages": {"综合数学_第一章审阅版": [1, 2], "综合数学": [1], "综合数学_完整数学目录": [1]},
  "result": "实际检查范围与结论；示例页码须替换",
  "artifact_sha256": {"dist/文件名": "从本轮报告复制的完整散列映射"}
}
```

然后执行 `python tools/package_ch01_review.py`。打包器检查自动验证状态、构建输入快照、所有输出散列及视觉记录，拒绝过期检查。伴生包包含源稿、构建代码、样式源、数据台账、审校记录、PDF/HTML/Markdown、图与本次截图；不含原始DOCX、MSC PDF或外部教材全文。重建会使旧报告失效，必须重新检查。

## 上传 GitHub Releases

**发布前先刷新发布说明。** 编辑 `发布说明.md`，核对本版内容、T/S/G 数量、实际验证结果与作者审阅状态；删除“尚未上传新发布资产”等上传前状态和待填占位文字，改用“本版产物包括……”等发布前后均成立的描述。上传状态保留在 README 或工作记录，不能提前改成“已发布”。源码链接保留仓库相对路径，不能写会漂移的分支URL。脚本用本次标签生成 `build/release-notes.md`，将相对源码链接固定为 `https://github.com/LeoLee0512/IntegratedMath/blob/<标签>/<文件>`，并保留锚点；外部网址保持原样。实际传给 `--notes-file` 的是生成文件，源模板不会被改写。

运行 `python tools/check_release_notes.py` 检查已知过期表述与占位文字，再提交本轮源码和已刷新的发布说明，推送当前工作分支，确保该提交已在远端。使用有本仓库写入权限的 `gh` 登录，在源码无未提交修改时运行：

```sh
bash tools/publish_ch01_release.sh review-ch01-2026-10-22
```

标签名必须是新版本号。脚本在联网前检查并渲染说明，然后检查包和当前快照，创建指向当前提交的 **draft Release**，上传三个PDF、两个离线HTML、三个Markdown、伴生zip及 `SHA256SUMS.txt`；既有同名 Release 不覆盖。渲染预览不会创建标签；实际创建 Release 时才由 GitHub 将新标签关联到已核验的提交。发布前在 GitHub 检查资产与生成说明，并逐个打开标签链接确认文件和版本，再将草稿发布。

若需修订已有草稿说明，保持原标签不动，更新说明模板后运行 `python tools/render_release_notes.py --tag <原标签> --output build/release-notes.md`，再执行 `gh release edit <原标签> --repo LeoLee0512/IntegratedMath --notes-file build/release-notes.md`。核对所链接文件在该标签下确实存在；不能通过移动标签让它追上新稿。发布成功后再将 README 的迁移状态更新为真实版本链接，不能把尚未存在的 Release 写成可下载版本。

`check_release_notes.py` 是已知表述检查，覆盖“待发布”“尚未上传”等以及少数占位词；它不理解全部同义改写、否定或引用语境，更不是发布状态机。通过检查不表示已经上传、文案正确或所有链接有效；可能误报的引文需人工改写或判断。本轮用两个不同标签渲染同一模板，核对链接随标签变化且模板不变，并检查独立“待发布”也会被拒绝。

本轮云环境 `gh` 认证不可用，连接器不提供 Release 上传接口；工具与产物已准备，不据此声称上传成功。该限制不影响源码编辑与构建。

CI 在工作分支及 PR 上重建并执行自动检查，通过 Actions 保存短期构建资产供检查；这不是正式版本，不自动将视觉检查记为通过，也不替代 Releases。

## 历史策略

- `history/35-chapter-draft` 固定指向旧35章稿提交 `818bc3c77023b76dac56fb3b4a3ca3b6eee0ce39`。
- `history/ch01-before-editorial-policy` 固定指向迁移前提交 `d5a181d81e73c2b7702ad1a49820d840a44a5af5`。
- 后续章节在工作分支保留有意义的提交，优先 merge 或 fast-forward；正式审阅包加 `review-*` 标签，不移动已发布标签。
- 人工审校记录中的旧散列保持原值，修订意见追加记录。需要长期保存的节点同时保留分支或标签，不仅在文字里引用裸散列。
- 本轮不清除既有二进制历史；若未来确需缩减历史仓库体积，须另行制定备份、旧链接迁移和协作者同步方案。
