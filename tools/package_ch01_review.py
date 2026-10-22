"""Package only the current review, its sources and evidence; exclude user attachments."""
from pathlib import Path
import hashlib
import json
import zipfile
from review_artifacts import require_review

require_review()

ROOT=Path(__file__).resolve().parents[1]
names=[
    'README.md','EDITORIAL_POLICY.md','LEARNING_PATH.md','RELEASING.md','发布说明.md','requirements-build.txt',
    '.gitignore','.github/workflows/build-review.yml','data/editorial_plan.json','tools/style.css','tools/review_artifacts.py',
    'tools/publish_ch01_release.sh','build/review_ch01/build_inputs.json',
    'tools/build_ch01_review.py','tools/draw_ch01_figures.py','tools/ch01_simulation.py',
    'tools/validate_ch01_review.py','tools/package_ch01_review.py',
    'tools/build_full_catalog.py','tools/pdf_header.tex',
    'tools/merge_catalog_chinese.py','tools/validate_catalog_chinese.py',
    'data/msc_taxonomy.json','data/catalog_titles.json','data/catalog_validation.json',
    'data/catalog_titles_zh.json','data/catalog_chinese_validation.json',
    'data/ch01_validation.json','data/ch01_simulation.json',
    'research/user_derivation_style.md','research/ch01_math_review.md','research/editorial_revision_review.md',
    'research/ch01_source_checks.json','research/ch01_source_checks.md',
    'dist/综合数学.md','dist/综合数学.pdf','dist/综合数学.html','dist/style.css',
    'dist/综合数学_第一章审阅版.md','dist/综合数学_第一章审阅版.pdf',
    'dist/综合数学_第一章审阅版.html',
    'dist/综合数学_完整数学目录.md','dist/综合数学_完整数学目录.pdf',
]
files=[ROOT/n for n in names]
for folder,pattern in [('manuscript/review_ch01','*.md'),('figures','ch01_*.png'),
                       ('dist/figures','ch01_*.png'),('build/review_ch01','contact-*.png'),
                       ('build/review_ch01/screenshots','*.png'),('build/review_ch01','*.log'),
                       ('build/review_ch01/catalog-screenshots','*.png')]:
    files.extend((ROOT/folder).glob(pattern))
files.extend(p for p in (ROOT/'research/catalog_zh_chunks').iterdir()
             if p.suffix in ['.json','.tsv','.md'])
files=sorted(set(files))
assert all(p.is_file() for p in files)
assert all(p.suffix not in ['.docx'] and p.name!='MSC_2020.pdf' for p in files)
manifest={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
manifest_path=ROOT/'data/ch01_release_hashes.json'
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
files.append(manifest_path)
target=ROOT/'dist/综合数学_第一章_伴生文件.zip'
with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
    for p in files:z.write(p,Path('IntegratedMath')/p.relative_to(ROOT))
with zipfile.ZipFile(target) as z:
    assert z.testzip() is None
    for path,digest in manifest.items():
        assert hashlib.sha256(z.read('IntegratedMath/'+path)).hexdigest()==digest
print(json.dumps({'files':len(files),'bytes':target.stat().st_size,'path':str(target)},ensure_ascii=False))
