#!/usr/bin/env python3
"""Verify the backup, or reconstruct every exact original file into a NEW directory."""
from pathlib import Path
import argparse, hashlib, json

base=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path,help='New destination directory; must not already exist')
args=parser.parse_args()
manifest=json.loads((base/'manifest.json').read_text())
out=args.output.resolve() if args.output else None
if out:out.mkdir(parents=True,exist_ok=False)
total=0
for record in manifest['entries']:
    relative=Path(record['path'])
    if relative.is_absolute() or '..' in relative.parts:raise ValueError('Unsafe manifest path')
    paths=[]
    if record['storage']=='file':
        paths=[(base/record['backup_path'],None)]
    else:
        for chunk in record['chunks']:
            h=chunk['sha256']
            if len(h)!=64 or any(c not in '0123456789abcdef' for c in h):raise ValueError('Invalid object digest')
            paths.append((base/'objects'/h[:2]/h,chunk))
    digest=hashlib.sha256();size=0
    target=out/relative if out else None
    if target:target.parent.mkdir(parents=True,exist_ok=True)
    handle=target.open('xb') if target else None
    try:
        for path,chunk in paths:
            if not path.resolve().is_relative_to(base):raise ValueError('Escaping backup path')
            payload=path.read_bytes()
            if chunk and (len(payload)!=chunk['bytes'] or hashlib.sha256(payload).hexdigest()!=chunk['sha256']):raise ValueError('Damaged object: '+str(path))
            digest.update(payload);size+=len(payload)
            if handle:handle.write(payload)
    finally:
        if handle:handle.close()
    if size!=record['bytes'] or digest.hexdigest()!=record['sha256']:raise ValueError('File hash mismatch: '+str(relative))
    total+=size
print(json.dumps({'status':'verified','files':len(manifest['entries']),'bytes':total,'restored_to':str(out) if out else None},ensure_ascii=False))
