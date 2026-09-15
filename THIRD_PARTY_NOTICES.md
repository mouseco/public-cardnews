# Third-party notices

## baoyu-codex-imagegen
- Author: Jim Liu
- Source: https://github.com/JimLiu/baoyu-skills
- Revision: `1567581c26ec29f4216c6e6835415bf30343b0e3`
- Imported subtree: `packages/baoyu-codex-imagegen`
- License: MIT, Copyright (c) 2026 Jim Liu. Full text: [vendor license](vendor/baoyu-codex-imagegen/LICENSE).
- Changes in `src/spawn.ts`: use workspace-write sandbox; allow CODEX_BIN override for Windows executables. Other source files preserved. README backend-document link changed to an absolute upstream URL for this vendored location.
- This is a third-party wrapper, not an OpenAI product. Upstream README links are relative to the upstream repository, not this checkout.

## OpenAI Codex CLI
Installed separately by the user; not bundled. https://github.com/openai/codex — Apache-2.0. CLI code licensing does not license the hosted image model or replace OpenAI service terms. An eligible account and current service access are required; unlimited usage is not promised.

## Development dependencies
Pillow: HPND-family license; PyYAML: MIT. Installed separately via requirements-dev.txt, not vendored.
