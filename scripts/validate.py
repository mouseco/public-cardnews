"""Offline consistency checks; not a legal, OCR, or security certification."""
from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote
import yaml
from PIL import Image

CATALOG = 'skills/public-cardnews/assets/catalog.json'


def validate(root):
    root = Path(root).resolve()
    errors = []
    skill = root / 'skills/public-cardnews/SKILL.md'
    if not skill.exists():
        return ['missing SKILL.md']
    text = skill.read_text(encoding='utf-8')
    try:
        assert text.startswith('---\n')
        parts = text.split('---', 2)
        meta = yaml.safe_load(parts[1])
        assert isinstance(meta, dict) and meta.get('name') and meta.get('description') and parts[2].strip()
    except (AssertionError, IndexError, yaml.YAMLError):
        errors.append('invalid frontmatter: SKILL.md')
    private = re.compile(r'(?:/home/[A-Za-z0-9_-]+/|/mnt/[a-z]/Users/|[A-Z]:\\Users\\|sk-(?:proj-)?[A-Za-z0-9_-]{20,}|-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----)')
    hidden_address = 'ai.' + 'kosaf.go.kr'
    for p in root.rglob('*'):
        if any(x in p.relative_to(root).parts for x in ('.git', '.venv', '.runtime', 'runs', 'node_modules', '__pycache__')):
            continue
        if p.is_file() and p.suffix in ('.md', '.json', '.yml', '.yaml', '.toml', '.txt', '.py', '.ts'):
            s = p.read_text(encoding='utf-8')
            if private.search(s) or hidden_address in s:
                errors.append(f'private path/address/token pattern: {p.relative_to(root)}')
            if '\ufffd' in s:
                errors.append(f'UTF-8 replacement character: {p.relative_to(root)}')
            if p.suffix == '.md':
                targets = re.findall(r'\]\(([^\s)]+)(?:\s+[^)]*)?\)', s) + re.findall(r'(?:src|href)="([^"]+)"', s)
                for target in targets:
                    if target.startswith(('http:', 'https:', '#', 'mailto:')):
                        continue
                    target = unquote(target.split('#')[0])
                    if target and not (p.parent / target).exists():
                        errors.append(f'broken link: {p.relative_to(root)} -> {target}')
    catalog = root / CATALOG
    if not catalog.exists():
        errors.append('missing catalog')
    else:
        try:
            rows = json.loads(catalog.read_text(encoding='utf-8'))['items']
            ids = [r['id'] for r in rows]
            if len(ids) != len(set(ids)):
                errors.append('duplicate catalog id')
            indexed = set()
            for row in rows:
                if row['kind'] != 'generated':
                    continue
                for key in ('image', 'prompt', 'edit_prompt'):
                    f = root / row[key]
                    indexed.add(f.resolve())
                    if not f.is_file():
                        errors.append(f'missing catalog asset: {row["id"]} {key}')
            asset_root = root / 'skills/public-cardnews/assets/cover-styles'
            for folder, suffix in [('images', '*.png'), ('prompts', '*.md'), ('edit-prompts', '*.md')]:
                for p in (asset_root / folder).glob(suffix):
                    if p.resolve() not in indexed:
                        errors.append(f'unindexed asset: {p.relative_to(root)}')
        except (KeyError, TypeError, ValueError) as exc:
            errors.append(f'invalid catalog: {exc}')
    for p in root.rglob('*.png'):
        if any(x in p.relative_to(root).parts for x in ('.git', '.venv', '.runtime', 'runs', 'node_modules')):
            continue
        try:
            with Image.open(p) as im:
                assert im.format == 'PNG'
                im.verify()
            with Image.open(p) as im:
                im.load()
                assert min(im.size) > 0
        except Exception:
            errors.append(f'invalid PNG: {p.relative_to(root)}')
    return errors


if __name__ == '__main__':
    errors = validate(Path(__file__).resolve().parents[1])
    print(json.dumps({'ok': not errors, 'errors': errors}, ensure_ascii=False, indent=2))
    sys.exit(bool(errors))
