"""Exercise release-note rendering and the actual upload command without networking."""
from pathlib import Path
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from check_release_notes import check_notes, render_notes


class ReleaseNotesTest(unittest.TestCase):
    def test_known_stale_phrases_and_review_status(self):
        for text in ['', '尚未上传新发布资产', '待发布产物', 'TODO', '待填写']:
            with self.subTest(text=text), self.assertRaises(ValueError):
                check_notes(text)
        check_notes('本版产物包括审阅稿，待作者审阅。')

    def test_documented_denylist_boundary(self):
        # Passing these does not establish publication readiness.
        for text in ['待发布', '待发布\n资产', '待发布' + '甲' * 13 + '资产']:
            check_notes(text)

    def test_template_pins_all_source_links(self):
        source = (ROOT / '发布说明.md').read_text()
        for tag in ['review-ch01-2026-10-22', 'review-ch01-2026-10-23']:
            rendered = render_notes(source, tag)
            links = re.findall(r'https://github.com/LeoLee0512/IntegratedMath/blob/[^)]+', rendered)
            self.assertEqual(len(links), 3)
            self.assertTrue(all('/blob/' + tag + '/' in url for url in links))
            self.assertNotIn('{{RELEASE_TAG}}', rendered)
            self.assertNotIn('/blob/draft/', rendered)
        self.assertIn('{{RELEASE_TAG}}', source)
        self.assertEqual(render_notes('blob/{{RELEASE_TAG}}/稿.md#sec-00A15', 'review-ch01/v2'),
                         'blob/review-ch01%2Fv2/稿.md#sec-00A15')

    def test_invalid_refs(self):
        for tag in ['main', 'review-a..b', 'review-a b', 'review-a@{b', 'review-a.lock']:
            with self.subTest(tag=tag), self.assertRaises(ValueError):
                render_notes('本版产物', tag)

    def test_cli_preserves_template(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'notes.md'
            path.write_text('blob/{{RELEASE_TAG}}/source.md')
            proc = subprocess.run([sys.executable, str(ROOT / 'tools/check_release_notes.py'),
                                   str(path), '--release-tag', 'review-test', '--output', str(path)],
                                  capture_output=True)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn('{{RELEASE_TAG}}', path.read_text())

    def test_publisher_passes_rendered_notes_and_cleans_temp(self):
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            (work / 'tools').mkdir()
            (work / 'bin').mkdir()
            (work / 'dist').mkdir()
            for name in ['publish_ch01_release.sh', 'check_release_notes.py']:
                shutil.copy2(ROOT / 'tools' / name, work / 'tools' / name)
            source = (ROOT / '发布说明.md').read_text()
            (work / '发布说明.md').write_text(source)
            (work / 'tools/package_ch01_review.py').write_text('')
            for stem in ['综合数学', '综合数学_第一章审阅版', '综合数学_完整数学目录']:
                for ext in ['.pdf', '.md', '.html']:
                    (work / 'dist' / (stem + ext)).write_text('fixture')
            (work / 'dist/综合数学_第一章_伴生文件.zip').write_text('fixture')
            git = work / 'bin/git'
            git.write_text('#!/bin/sh\ncase "$1" in\nrev-parse) echo fixture-commit;;\nls-remote) exit 2;;\n*) exit 0;;\nesac\n')
            gh = work / 'bin/gh'
            gh.write_text('#!' + sys.executable + '\n' + '''import json, pathlib, sys
args = sys.argv[1:]
if args[0] == 'api':
    print('fixture-commit')
elif args[:2] == ['release', 'create']:
    path = pathlib.Path(args[args.index('--notes-file') + 1])
    pathlib.Path('upload.json').write_text(json.dumps({'args': args, 'path': str(path), 'text': path.read_text()}))
''')
            git.chmod(0o755)
            gh.chmod(0o755)
            env = dict(os.environ, PATH=str(work / 'bin') + os.pathsep + os.environ['PATH'])
            subprocess.run(['bash', 'tools/publish_ch01_release.sh', 'review-ch01-test'],
                           cwd=work, env=env, check=True, capture_output=True)
            import json
            upload = json.loads((work / 'upload.json').read_text())
            self.assertIn('/blob/review-ch01-test/', upload['text'])
            self.assertNotIn('{{RELEASE_TAG}}', upload['text'])
            self.assertIn('--draft', upload['args'])
            self.assertEqual(upload['args'][upload['args'].index('--target') + 1], 'fixture-commit')
            self.assertFalse(Path(upload['path']).exists())
            self.assertEqual((work / '发布说明.md').read_text(), source)


if __name__ == '__main__':
    unittest.main()
