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

**发布前先刷新发布说明。** 编辑 `发布说明.md`，核对本版内容、T/S/G 数量、实际验证结果与作者审阅状态；删除“尚未上传新发布资产”等上传前状态和待填占位文字，改用“本版产物包括……”等发布前后均成立的描述。上传状态保留在 README 或工作记录，不能提前改成“已发布”。仓库内的源码链接采用 `https://github.com/LeoLee0512/IntegratedMath/blob/{{RELEASE_TAG}}/文件路径`；`{{RELEASE_TAG}}` 是发布脚本替换的标签变量，不是待填内容。脚本按传入标签生成临时说明，将其作为 `--notes-file` 交给 GitHub，不改写已提交的模板。Release 中的链接因此固定到本次标签，不随工作分支移动；创建草稿后再改仓库文件不会自动更新已有 Release 说明。

运行 `python tools/check_release_notes.py` 检查已知过期表述与占位文字，再提交本轮源码和已刷新的发布说明，推送当前工作分支，确保该提交已在远端。使用有本仓库写入权限的 `gh` 登录，在源码无未提交修改时运行：

```sh
bash tools/publish_ch01_release.sh review-ch01-2026-10-22
```

标签名必须是新版本号。脚本在联网前检查并渲染发布说明，然后检查包和当前快照，创建指向当前提交的 **draft Release**，上传三个PDF、两个离线HTML、三个Markdown、伴生zip及 `SHA256SUMS.txt`；既有同名 Release 不覆盖。发布前在 GitHub 检查已上传的资产和草稿说明，核对三个源码链接均为 `blob/<本次标签>/...`，写清仍待作者审阅的状态，再将草稿发布。发布成功后再将 README 的迁移状态更新为真实版本链接；发布说明保持描述本版内容的稳定文字。不能把尚未存在的 Release 写成可下载版本。

若需修订已有草稿的说明，先更新并提交源模板，再用**该草稿原有标签**渲染并显式更新；不要将未渲染的模板直接上传，也不要为改说明移动标签：

```sh
python tools/check_release_notes.py --release-tag review-ch01-2026-10-22 --output build/release-notes.md
gh release edit review-ch01-2026-10-22 --repo LeoLee0512/IntegratedMath --notes-file build/release-notes.md
```

复查页面，确保文字描述仍与该标签及资产相符；源稿或资产变化应另发新版本。上面的渲染命令也可单独用于发布前预览，不需要联网。

**检查器的覆盖边界。** `check_release_notes.py` 是“已知过期表述”清单，不是完整状态机。中文模式要求“待/未”等状态词后接“上传/发布”，并在其后最多12个非换行字符内出现“资产/产物”；单独的“待发布”、跨行或间隔更远的新写法可能漏检。遇到新过期写法时补充明确规则及回归用例；不宜笼统禁止“待”字，因为“待作者审阅”仍是必须保留的真实状态。检查通过不能证明已上传、链接可访问或版本描述正确，仍需人工核对。

本轮云环境 `gh` 认证不可用，连接器不提供 Release 上传接口；工具与产物已准备，不据此声称上传成功。该限制不影响源码编辑与构建。

CI 在工作分支及 PR 上重建并执行自动检查，通过 Actions 保存短期构建资产供检查；这不是正式版本，不自动将视觉检查记为通过，也不替代 Releases。

## 历史策略

- `history/35-chapter-draft` 固定指向旧35章稿提交 `818bc3c77023b76dac56fb3b4a3ca3b6eee0ce39`。
- `history/ch01-before-editorial-policy` 固定指向迁移前提交 `d5a181d81e73c2b7702ad1a49820d840a44a5af5`。
- 后续章节在工作分支保留有意义的提交，优先 merge 或 fast-forward；正式审阅包加 `review-*` 标签，不移动已发布标签。
- 人工审校记录中的旧散列保持原值，修订意见追加记录。需要长期保存的节点同时保留分支或标签，不仅在文字里引用裸散列。
- 本轮不清除既有二进制历史；若未来确需缩减历史仓库体积，须另行制定备份、旧链接迁移和协作者同步方案。
