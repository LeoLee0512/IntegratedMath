"""Bind chapter review records to the build inputs and distributable outputs."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]


def hashes(paths):
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(paths)}


def source_hashes():
    names = ['requirements-build.txt', 'tools/build_ch01_review.py',
             'tools/manuscript_format.py', 'tools/build_full_catalog.py', 'tools/draw_ch01_figures.py',
             'tools/ch01_simulation.py', 'tools/pdf_header.tex', 'tools/style.css',
             'data/msc_taxonomy.json', 'data/catalog_titles.json',
             'data/catalog_titles_zh.json']
    return hashes([ROOT / n for n in names] + list((ROOT / 'manuscript/review_ch01').glob('*.md')))


def artifact_hashes():
    stems = ['综合数学', '综合数学_第一章审阅版', '综合数学_完整数学目录']
    paths = [ROOT / 'dist' / (s + ext) for s in stems for ext in ['.md', '.pdf']]
    paths += [ROOT / 'dist' / (s + '.html') for s in stems[:2]]
    paths += [ROOT / 'dist/style.css']
    paths += list((ROOT / 'dist/figures').glob('ch01_*.png'))
    return hashes(paths)


def check_build_inputs():
    recorded = json.loads((ROOT / 'build/review_ch01/build_inputs.json').read_text())
    if recorded != source_hashes():
        raise ValueError('Build inputs changed; rebuild and validate the chapter first')


def require_review():
    check_build_inputs()
    report = json.loads((ROOT / 'data/ch01_validation.json').read_text())
    current = artifact_hashes()
    visual = report.get('visual_review')
    if report.get('status') != 'automated_checks_passed' or report.get('artifact_sha256') != current:
        raise ValueError('Artifacts changed or automated validation is missing; validate again')
    if not isinstance(visual, dict) or visual.get('status') != 'inspected':
        raise ValueError('Actual visual inspection is required before packaging; see RELEASING.md')
    if visual.get('artifact_sha256') != current or not visual.get('result') or not visual.get('reviewed_at'):
        raise ValueError('Visual inspection must identify these exact artifacts and its actual result')
    for name, artifact in report['artifacts'].items():
        pages = visual.get('pages', {}).get(name, [])
        if not pages or any(type(p) is not int or not 1 <= p <= artifact['pages'] for p in pages):
            raise ValueError('Record inspected page numbers for each PDF: ' + name)
