#!/usr/bin/env python3
"""Package an inspected LOCAL teaching batch; performs no network operation."""
from pathlib import Path
import hashlib
import json
import zipfile
from build_learning_batch import source_hashes,artifact_hashes

ROOT=Path(__file__).resolve().parents[1]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    report=json.loads((ROOT/'data/production/batch_validation.json').read_text())
    if report.get('status')!='automated_checks_passed':
        raise ValueError('Run the batch validator before packaging')
    if report.get('source_sha256')!=source_hashes() or report.get('artifact_sha256')!=artifact_hashes():
        raise ValueError('Source or output changed; rebuild and validate before packaging')
    visual=report.get('visual_review',{})
    if visual.get('status')!='accepted' or visual.get('result')!='passed':
        raise ValueError('Actual visual inspection is required')
    if not visual.get('reviewer') or not visual.get('reviewed_at'):
        raise ValueError('Missing visual inspection identity/time')
    for name,value in report['artifact_sha256'].items():
        if not name.endswith('.pdf'):continue
        if visual.get('artifact_sha256',{}).get(name)!=value:
            raise ValueError('Visual review is not bound to this PDF: '+name)
        pages=visual.get('pages',{}).get(name,[])
        if not pages:raise ValueError('No inspected pages: '+name)
        for page in pages:
            p=ROOT/page['path']
            if digest(p)!=page['sha256']:raise ValueError('Screenshot changed: '+str(p))
    files=[]
    for folder,patterns in {
        'manuscript':['**/*.md'],'tools':['*.py','*.tex','*.css'],
        'templates':['*.md'],'research':['ch01_*.md','ch01_*.json','user_derivation_style.md',
                                        'production/*.md','production/*.json',
                                        'catalog_zh_chunks/*.json','catalog_zh_chunks/*.tsv','catalog_zh_chunks/*.md'],
        'data':['msc_taxonomy.json','catalog_titles.json','catalog_titles_zh.json','editorial_plan.json',
                'catalog_validation.json','catalog_chinese_validation.json',
                'ch01_simulation.json','production/*.json'],
        'dist':['*.md','*.pdf','*.html','style.css','figures/ch01_*.png','figures/b1_*.png','figures/b2_*.png'],
        'build/learning_batch':['*.json','*.log','screenshots/*.png','contact-*.png'],
        'build/review_ch01':['*.log','build_inputs.json']
    }.items():
        for pattern in patterns:files.extend((ROOT/folder).glob(pattern))
    files += [ROOT/p for p in ['README.md','EDITORIAL_POLICY.md','LEARNING_PATH.md','PRODUCTION_PLAN.md',
                               'BATCH_CHECKPOINT.md','RELEASING.md','requirements-build.txt']]
    files=sorted(p for p in set(files) if p.name != "package_validation.json")
    assert all(p.is_file() for p in files)
    assert not any(p.suffix=='.docx' or p.name=='MSC_2020.pdf' for p in files)
    manifest={str(p.relative_to(ROOT)):digest(p) for p in files}
    # Every validated source and artifact must survive packaging, including all
    # solver modules, dependency reports, teaching units and generated figures.
    for inventory in ['source_sha256','artifact_sha256']:
        for name,value in report[inventory].items():
            if manifest.get(name)!=value:
                raise ValueError('Validated file missing or changed in package: '+name)
    target=ROOT/'dist/综合数学_基础续写_伴生文件.zip'
    with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
        for p in files:z.write(p,Path('IntegratedMath')/p.relative_to(ROOT))
        z.writestr('IntegratedMath/SHA256SUMS.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    with zipfile.ZipFile(target) as z:
        assert z.testzip() is None
        for p,h in manifest.items():assert hashlib.sha256(z.read('IntegratedMath/'+p)).hexdigest()==h,p
    summary={'status':'local_package_verified','path':str(target.relative_to(ROOT)),
             'file_count':len(files)+1,'bytes':target.stat().st_size,'sha256':digest(target),
             'network_operations':0}
    (ROOT/'data/production/package_validation.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
