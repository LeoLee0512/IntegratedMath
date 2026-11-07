#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

release_tag="${1:?Usage: bash tools/publish_ch01_release.sh review-ch01-YYYY-MM-DD}"
[[ "$release_tag" == review-* ]] || { echo 'Use a new review-* tag.' >&2; exit 1; }
git check-ref-format "refs/tags/$release_tag"
git diff --quiet && git diff --cached --quiet || { echo 'Commit source changes before releasing.' >&2; exit 1; }
python tools/check_release_notes.py
gh auth status
release_commit="$(git rev-parse HEAD)"
remote_commit="$(gh api "repos/LeoLee0512/IntegratedMath/commits/$release_commit" --jq .sha)"
[[ "$remote_commit" == "$release_commit" ]] || { echo 'Push the source commit before releasing.' >&2; exit 1; }
if git ls-remote --exit-code --tags https://github.com/LeoLee0512/IntegratedMath.git "refs/tags/$release_tag"; then
  echo 'This tag already exists; use a new review version.' >&2
  exit 1
else
  tag_status=$?
  [[ "$tag_status" == 2 ]] || exit "$tag_status"
fi
python tools/package_ch01_review.py
python - <<'PY'
from pathlib import Path
import hashlib
paths = [Path('dist') / (stem + ext) for stem in
         ['综合数学', '综合数学_第一章审阅版', '综合数学_完整数学目录'] for ext in ['.pdf', '.md']]
paths += [Path('dist') / (stem + '.html') for stem in ['综合数学', '综合数学_第一章审阅版']]
paths += [Path('dist/综合数学_第一章_伴生文件.zip')]
Path('dist/SHA256SUMS.txt').write_text(''.join(
    hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + p.name + '\n' for p in paths))
PY
gh release create "$release_tag" \
  --repo LeoLee0512/IntegratedMath --target "$release_commit" \
  --draft --title "综合数学 第一章审阅稿 $release_tag" --notes-file 发布说明.md \
  dist/综合数学.pdf dist/综合数学.md dist/综合数学.html \
  dist/综合数学_第一章审阅版.pdf dist/综合数学_第一章审阅版.md dist/综合数学_第一章审阅版.html \
  dist/综合数学_完整数学目录.pdf dist/综合数学_完整数学目录.md \
  dist/综合数学_第一章_伴生文件.zip dist/SHA256SUMS.txt
