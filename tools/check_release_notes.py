"""Check known stale phrases and render source links for one release tag.

This is a denylist, not a release-state validator: standalone 待发布 and
wordings outside STALE_STATUS still require human review.
"""
import argparse
from pathlib import Path
import re
import subprocess
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
STALE_STATUS = re.compile(r'(?:尚未|仍未|还未|未|等待|待)\s*(?:上传|发布).{0,12}(?:资产|产物)|\bTODO\b|待填写', re.I)
TAG_PLACEHOLDER = '{{RELEASE_TAG}}'


def check_notes(text):
    if not text.strip():
        raise ValueError('发布说明为空；发布前请先刷新发布说明。')
    match = STALE_STATUS.search(text)
    if match:
        raise ValueError('发布说明含上传前状态或占位文字：' + match.group() + '；请按 RELEASING.md 刷新后再发布。')


def render_notes(text, release_tag):
    check_notes(text)
    if not release_tag.startswith('review-') or subprocess.run(
        ['git', 'check-ref-format', 'refs/tags/' + release_tag],
        capture_output=True,
    ).returncode:
        raise ValueError('发布标签必须是有效的新 review-* 标签。')
    # Encode the ref as one URL component; paths and anchors stay unchanged.
    return text.replace(TAG_PLACEHOLDER, quote(release_tag, safe=''))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', nargs='?', type=Path, default=ROOT / '发布说明.md')
    parser.add_argument('--release-tag', help='用本次发布标签替换源码链接中的 {{RELEASE_TAG}}')
    parser.add_argument('--output', type=Path, help='生成的说明路径；不覆盖源模板')
    args = parser.parse_args()
    if bool(args.release_tag) != bool(args.output):
        parser.error('--release-tag 和 --output 必须同时指定')
    if args.output and args.output.resolve() == args.path.resolve():
        parser.error('输出路径不能覆盖发布说明源模板')
    try:
        text = args.path.read_text(encoding='utf-8')
        check_notes(text)
        if args.output:
            rendered = render_notes(text, args.release_tag)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(rendered, encoding='utf-8')
    except ValueError as exc:
        raise SystemExit(str(exc))
    print('发布说明检查通过；仍须人工核对版本内容、链接和审阅状态。')
