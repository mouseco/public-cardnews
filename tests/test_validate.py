import importlib.util
from pathlib import Path
import tempfile
import unittest

class ValidationTests(unittest.TestCase):
    def test_missing_skill_is_reported(self):
        path = Path(__file__).resolve().parents[1] / 'scripts' / 'validate.py'
        self.assertTrue(path.exists(), 'validator must exist')
        spec = importlib.util.spec_from_file_location('validator', path)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as tmp:
            errors = module.validate(Path(tmp))
        self.assertTrue(any('SKILL.md' in e for e in errors), errors)

    def test_invalid_package_is_rejected(self):
        path = Path(__file__).resolve().parents[1] / 'scripts/validate.py'
        spec = importlib.util.spec_from_file_location('validator', path)
        assert spec is not None and spec.loader is not None
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = root / 'skills/public-cardnews'
            folder.mkdir(parents=True)
            (folder / 'SKILL.md').write_text('bad frontmatter\n[missing](gone.md)\n' + '/home/' + 'alice/private', encoding='utf-8')
            errors = m.validate(root)
            for word in ('frontmatter', 'link', 'private', 'catalog'):
                self.assertTrue(any(word in e for e in errors), (word, errors))

    def test_catalog_assets_and_png_corruption(self):
        import json
        from PIL import Image
        path = Path(__file__).resolve().parents[1] / 'scripts/validate.py'
        spec = importlib.util.spec_from_file_location('validator', path)
        assert spec is not None and spec.loader is not None
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = root / 'skills/public-cardnews/assets/cover-styles'
            for sub in ['images', 'prompts', 'edit-prompts']:
                (folder / sub).mkdir(parents=True)
            (folder.parents[1] / 'SKILL.md').write_text('---\nname: test\ndescription: test\n---\nBody', encoding='utf-8')
            Image.new('RGB', (2, 2)).save(folder / 'images/01.png')
            for sub in ['prompts', 'edit-prompts']:
                (folder / sub / '01.md').write_text('prompt', encoding='utf-8')
            row = {'id': 'S01', 'kind': 'generated'}
            for key, sub, ext in [('image', 'images', 'png'), ('prompt', 'prompts', 'md'), ('edit_prompt', 'edit-prompts', 'md')]:
                row[key] = str((folder / sub / ('01.' + ext)).relative_to(root))
            (folder.parent / 'catalog.json').write_text(json.dumps({'items': [row]}), encoding='utf-8')
            self.assertEqual(m.validate(root), [])
            (folder / 'images/01.png').write_bytes(b'broken')
            self.assertTrue(any('invalid PNG' in e for e in m.validate(root)))
            (folder / 'prompts/01.md').unlink()
            self.assertTrue(any('missing catalog asset' in e for e in m.validate(root)))

if __name__ == '__main__':
    unittest.main()
