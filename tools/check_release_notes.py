"""Reject known pre-upload status text and placeholders in public release notes."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
STALE_STATUS = re.compile(r'(?:尚未|仍未|还未|未|等待|待)\s*(?:上传|发布).{0,12}(?:资产|产物)|\bTODO\b|待填写', re.I)


def check_notes(text):
    if not text.strip():
        raise ValueError('发布说明为空；发布前请先刷新发布说明。')
    match = STALE_STATUS.search(text)
    if match:
        raise ValueError('发布说明含上传前状态或占位文字：' + match.group() + '；请按 RELEASING.md 刷新后再发布。')


if __name__ == '__main__':
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / '发布说明.md'
    try:
        check_notes(path.read_text(encoding='utf-8'))
    except ValueError as exc:
        raise SystemExit(str(exc))
    print('发布说明检查通过；仍须人工核对版本内容、链接和审阅状态。')
