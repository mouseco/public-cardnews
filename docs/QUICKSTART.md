# 설치부터 첫 이미지까지

## 지원 범위와 준비물

- Git, Node.js 22 LTS, Bun 1.2 이상, Python 3.10 이상(검사·ZIP 포장용).
- OpenAI Codex CLI와 이미지 생성 기능을 사용할 수 있는 본인 계정. 로그인 표시만으로 실제 생성 지원을 보장하지 않는다.
- 실기 검증: Windows의 Bun 1.3.10 / Codex CLI 0.154.0, WSL에서 Windows 실행. Python 검사는 Ubuntu에서 수행.
- macOS·Linux 네이티브 및 신규 Windows PC는 안내만 제공하며 별도 실기 검증 전이다.
- Codex는 자신의 계정으로 로그인한다. 인증 파일을 공유하거나 복사하지 않는다. 구독 한도·서비스 약관이 적용되며 무제한 사용을 보장하지 않는다.

Bun과 Node.js는 각각 https://bun.sh/docs/installation 과 https://nodejs.org/ 에서 설치한다. 이 안내는 별도 PS1 실행 파일을 내려받아 실행하지 않는다.

## 1. 다운로드와 도구 확인

터미널에서:

```text
git clone https://github.com/mouseco/public-cardnews.git
cd public-cardnews
git checkout v0.5.0-beta.1
npm install -g @openai/codex@0.154.0
bun --version
codex --version
codex login
codex login status
bun vendor/baoyu-codex-imagegen/src/main.ts --help
```

실행기는 `vendor/baoyu-codex-imagegen`에 고정 버전으로 포함되어 있다. 별도 image-prompt/codex-image 개인 스킬 설치는 필요 없다. 직접 실행은 아래 명령만 사용한다. Bun 자체 내장 API를 사용하므로 실행기에 추가 npm install은 필요 없다.

### Windows: 실제 codex.exe 지정

npm의 codex.ps1/codex.cmd 대신 실행 파일을 지정한다. PowerShell에서:

```powershell
$npmRoot = (npm root -g).Trim()
$c = @(Get-ChildItem (Join-Path $npmRoot '@openai\codex') -Recurse -Filter codex.exe | Where-Object { $_.FullName -notmatch '\.codex-' })
if ($c.Count -ne 1) { throw 'codex.exe 후보가 하나가 아닙니다. 정상 설치 경로를 확인해 CODEX_BIN에 지정하세요.' }
$env:CODEX_BIN = $c[0].FullName
New-Item -ItemType Directory -Force runs/demo | Out-Null
```

macOS/Linux는 `command -v codex`로 확인하고 `mkdir -p runs/demo`를 실행한다. 필요하면 `export CODEX_BIN="$(command -v codex)"`로 지정한다. Windows와 WSL의 로그인·실행 경로를 섞지 않는다.

## 2. 첫 표지 생성

저장소 루트에서 한 줄로 실행한다. 기존 결과가 있다면 runs/demo 대신 새 폴더명을 쓴다.

```text
bun vendor/baoyu-codex-imagegen/src/main.ts --image runs/demo/01.png --prompt-file examples/first-run/prompts/01.md --aspect 4:5 --timeout 300000 --retries 0 --log-file runs/demo/01.jsonl
```

성공 JSON에 status=ok와 실제 PNG 경로가 나온다. `runs/demo/01.png`를 직접 열어 새봄연구소·AI 활용 안내·부제 문구를 확인한다. 이 단계가 성공하기 전에 다음 장으로 넘어가지 않는다. 실패했는데 파일만 남았다면 그 파일을 완료로 간주하지 않는다.

## 3. 첫 장을 참조해 두 번째 장 생성

```text
bun vendor/baoyu-codex-imagegen/src/main.ts --image runs/demo/02.png --prompt-file examples/first-run/prompts/02.md --ref runs/demo/01.png --aspect 4:5 --timeout 300000 --retries 0 --log-file runs/demo/02.jsonl
```

문구·잘림·줄바꿈·수치·색상 일관성을 직접 확인한다. 오류는 해당 장 프롬프트를 고쳐 새 출력명으로 재생성한다. 글자 크기는 프롬프트와 육안검수로 관리하며 픽셀 단위 동일성을 자동 보장하지 않는다.

## 4. 검사와 ZIP 전달

Python 가상환경을 만들고 도구를 설치한다. Windows는 `py`, macOS/Linux는 `python3`를 사용한다.

```text
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.venv\Scripts\python.exe -m unittest discover -s tests -v
.venv\Scripts\python.exe scripts/validate.py
Copy-Item examples/first-run/prompts runs/demo/prompts -Recurse
'이미지 두 장의 문구와 줄바꿈을 직접 확인했습니다.' | Set-Content runs/demo/review.txt -Encoding utf8
Compress-Archive -Path runs/demo/01.png,runs/demo/02.png,runs/demo/prompts,runs/demo/review.txt -DestinationPath runs/demo.zip
```

macOS/Linux:

```bash
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate.py
cp -R examples/first-run/prompts runs/demo/prompts
```

이미지를 본 뒤 검수 기록을 작성하고 PNG·프롬프트·검수 기록만 ZIP으로 묶는다. `validate.py`는 저장소 정합성을 검사하며 runs/는 검사에서 제외한다. 새 결과의 문구와 PNG 확인은 별도로 수행해야 한다. 로그에는 개인 경로·대화 내용이 있을 수 있으므로 ZIP이나 GitHub에 자동 포함하지 않는다.

## 5. Hermes 스킬로 사용하기 — 선택

Hermes의 활성 프로필 skills 폴더에 `skills/public-cardnews` 폴더 전체를 복사한다. 기본 프로필은 홈 디렉터리의 `.hermes/skills/public-cardnews`다. `HERMES_HOME`을 설정했다면 그 아래 `skills/public-cardnews`를 사용한다. 이미 같은 이름의 스킬이 있다면 먼저 백업하고 변경 내용을 비교한다. references와 assets도 포함한다. 새 대화에서 public-cardnews 스킬을 불러오도록 요청하고, 이 저장소의 실제 위치를 알려준다. 공개 스킬의 references/runtime.md가 직접 실행 방법을 안내한다. 실행기를 포함한 저장소는 이동·삭제하지 않는다.

다른 에이전트는 SKILL.md를 작업 지침으로 읽고 위 CLI를 호출할 수 있다. 모든 에이전트의 자동 설치·검색을 검증한 것은 아니다.

## 실패 대응

- **codex not found / spawn failed:** PATH와 CODEX_BIN, Windows 실행 파일 존재 확인. 위 버전 명령부터 실행한다.
- **invalid_refresh_token / token_expired / 로그인 오류:** 같은 OS 환경에서 codex login을 실행한다. 토큰을 다른 PC에서 복사하지 않는다.
- **timeout:** runs/demo의 해당 로그와 실행 중인 Bun/Codex 프로세스부터 확인한다. 이미 완료된 장은 유지하고 실패한 장만 새 이름으로 실행한다. 계속 같은 요청을 재시도하지 않는다.
- **lock_busy:** 다른 생성 작업이 진행 중인지 확인한다. 실행 중이면 기다린다. 프로세스 종료를 확인하지 않고 잠금 파일을 삭제하지 않는다.
- **ok지만 문구 오류:** 생성 성공과 게시 가능 상태는 다르다. 원고를 줄이거나 배치 지시를 수정해 재생성한다.
- **이미지 기능 사용 불가:** 계정·CLI 버전·현재 서비스 지원을 확인한다. 별도 API 과금으로 자동 전환하지 않는다.

원격 생성은 비결정적이며 샘플과 픽셀이 같아지지는 않는다. 샘플 선택·로그인·생성·검수를 각각 확인한다.
