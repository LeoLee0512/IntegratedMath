"""Render repository-relative source links against the requested release tag."""
import argparse
from pathlib import Path
import re
import subprocess
from urllib.parse import quote, urlsplit
from check_release_notes import check_notes

ROOT = Path(__file__).resolve().parents[1]
REPO = 'https://github.com/LeoLee0512/IntegratedMath'
LINK = re.compile(r'(?<!!)\[([^\]\n]+)\]\(([^\s)]+)\)')


def render_notes(text, tag, root=ROOT):
    check_notes(text)
    if not tag.startswith('review-'):
        raise ValueError('Use a review-* release tag')
    subprocess.run(['git', 'check-ref-format', 'refs/tags/' + tag], check=True, capture_output=True)

    def pin(match):
        label, target = match.groups()
        # Require local source links, not arbitrary branch names that cannot be
        # separated safely from file paths (both can contain slashes).
        if target.startswith((REPO + '/blob/', REPO + '/tree/')):
            raise ValueError('Use a repository-relative source link in 发布说明.md: ' + target)
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or target.startswith('#'):
            return match.group()
        if not parsed.path or parsed.query:
            raise ValueError('Unsupported local release-note link: ' + target)
        path = (root / parsed.path).resolve()
        if not path.is_relative_to(root.resolve()) or not path.is_file():
            raise ValueError('Release-note source link is missing or outside the repository: ' + target)
        relative = path.relative_to(root.resolve()).as_posix()
        fragment = '#' + quote(parsed.fragment, safe='-._~') if parsed.fragment else ''
        return f'[{label}]({REPO}/blob/{quote(tag, safe="")}/{quote(relative, safe="/")}{fragment})'

    return LINK.sub(pin, text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tag', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    rendered = render_notes((ROOT / '发布说明.md').read_text(encoding='utf-8'), args.tag)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding='utf-8')
    print('Release notes pinned to tag ' + args.tag + ': ' + str(args.output))


if __name__ == '__main__':
    main()
