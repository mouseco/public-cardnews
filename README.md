# Public Cardnews

**정책 카드뉴스를 기획하고, 디자인을 고른 뒤 프롬프트와 이미지까지 만드는 스킬.**

**v0.5.0-beta.1** — Windows 중심 베타. 번들 실행기와 가상 기관 예제를 제공합니다. 새 PC 검증은 아직 남아 있습니다. OpenAI 또는 정부기관의 공식 도구가 아닙니다.

[설치부터 첫 이미지까지](docs/QUICKSTART.md) · [제작 샘플](skills/public-cardnews/references/generated-samples.md) · [사용 조건](docs/RIGHTS.md)

## 빠른 시작

Git·Node.js·Bun·본인 Codex 계정이 필요합니다. 검사에는 Python도 사용합니다.

```text
git clone https://github.com/mouseco/public-cardnews.git
cd public-cardnews
git checkout v0.5.0-beta.1
npm install -g @openai/codex@0.154.0
codex login
codex login status
```

**Windows에서는 먼저 [CODEX_BIN 설정과 작업 폴더 생성](docs/QUICKSTART.md)을 수행하세요.** 그다음 저장소 루트에서:

```text
bun vendor/baoyu-codex-imagegen/src/main.ts --image runs/demo/01.png --prompt-file examples/first-run/prompts/01.md --aspect 4:5 --timeout 300000 --retries 0
```

개인 image-prompt/codex-image 스킬은 별도 설치할 필요 없습니다. 공개 스킬과 번들 실행기만 사용합니다. 계정의 이미지 기능 지원·한도는 OpenAI 서비스 정책에 따릅니다.

## 제작 샘플

**S01–S07은 직접 생성한 샘플입니다.** 번호·경로·상태·출처의 정본은 [통합 목록](skills/public-cardnews/assets/catalog.json) 한 곳입니다.

<p>
<img src="skills/public-cardnews/assets/cover-styles/images/01.png" alt="S01 파란 입체형" width="32%" />
<img src="skills/public-cardnews/assets/cover-styles/images/02.png" alt="S02 메모지형" width="32%" />
<img src="skills/public-cardnews/assets/cover-styles/images/03.png" alt="S03 폴더형" width="32%" />
</p>

S01 파란 입체형 · S02 메모지형 · S03 폴더형

<p>
<img src="skills/public-cardnews/assets/cover-styles/images/04.png" alt="S04 기술 도해형" width="32%" />
<img src="skills/public-cardnews/assets/cover-styles/images/05.png" alt="S05 평면 정책형" width="32%" />
<img src="skills/public-cardnews/assets/cover-styles/images/06.png" alt="S06 사진형" width="32%" />
</p>

S04 기술 도해형 · S05 평면 정책형 · S06 사진형 **(실험안)**

[각 이미지의 생성·편집 프롬프트](skills/public-cardnews/references/generated-samples.md)를 함께 제공합니다. S06은 가상 인물 사진형이며 배경 원고 외 문구가 남아 있어 실험안으로 분리했습니다. 다른 샘플도 실제 게시 전 원고·기관명·날짜를 교체하고 확인하세요.

## S07 · 텍스트 중심 손글씨 메모형

크림색 종이에 펜으로 핵심을 적어 건네는 느낌의 디자인입니다. 입체 그림·인포그래픽 대신 **읽기 쉬운 손글씨, 문단 여백, 녹색 밑줄과 연노랑 형광펜**을 사용합니다. 기존 S02 메모지형과 별도의 선택지입니다.

<p><img src="skills/public-cardnews/assets/handwritten-memo/images/01.png" alt="S07 손글씨 메모 표지" width="45%" /><img src="skills/public-cardnews/assets/handwritten-memo/images/02.png" alt="S07 손글씨 메모 본문" width="45%" /></p>

- AI·뉴스 브리핑과 업무 요약에 적합합니다.
- 내용을 줄여도 **무슨 소식인지 → 주요 내용 → 업무에서 확인할 점**을 보존합니다.
- 같은 위계의 글자 크기와 충분한 줄간격을 유지하고, 첫 장을 참조해 후속 장을 생성합니다.
- 공개 승인된 6장 디자인 시안입니다. 뉴스 사실 확인용 자료가 아니며, 재사용할 때 최신 원고·날짜·출처로 교체하세요.

[전체 6장과 프롬프트](skills/public-cardnews/references/generated-samples.md#s07--텍스트-중심-손글씨-메모형) · [디자인 기준](skills/public-cardnews/references/handwritten-memo.md)

> S07은 `main`에 추가되었습니다. 위 고정 베타 태그에는 포함되지 않으므로 이 디자인을 사용하려면 `git switch main` 후 `git pull --ff-only`로 업데이트하세요.

## 실제 배포 예제

가상 기관 **새봄연구소**의 S02 메모지형 2장입니다.

<p><img src="examples/first-run/result/01.png" alt="예제 표지" width="45%" /><img src="examples/first-run/result/02.png" alt="예제 본문" width="45%" /></p>

[원고 프롬프트](examples/first-run/prompts/01.md) · [검수 기록](examples/first-run/result/review.md) · [PNG·프롬프트·검수 ZIP](examples/first-run/demo.zip)

기존 Windows PC의 새 소스·출력 폴더에서 생성했습니다. 기존 계정 로그인을 사용했으며 새 PC·빈 사용자 홈 검증으로 간주하지 않습니다. Codex 0.154.0, Bun 1.3.10에서 실행했습니다. 실제 이미지 모델 버전은 미확인입니다.

## 작업 흐름

기획안이 있으면 문구·수치·장수를 보존합니다. 없으면 목적·독자·근거·참여 경로를 확인하고 기획부터 제안합니다.

**기획 승인 → 디자인 선택 → 장별 프롬프트 → 첫 장 생성·확인 → 후속 장 → 원고 대조·PNG 검사 → 전달**

같은 위계 글자 크기, 의미 단위 줄바꿈, 숫자·단위 묶음은 프롬프트와 육안검수 기준입니다. 픽셀 단위 타이포 통일이나 한글·그래프 무오류를 자동 보장하지 않습니다. 오류는 해당 장을 재생성해 해결합니다.

## 에이전트에 스킬 설치하기

**이미 사용 중인 Hermes·Claude Code·Codex에 `public-cardnews` 스킬을 추가하는 안내입니다.** 세 프로그램을 모두 설치할 필요는 없습니다. 아래에서 사용하는 에이전트 하나를 고르세요.

### 먼저 준비하기 — 공통

1. 위 [빠른 시작](#빠른-시작)에 따라 저장소를 내려받고 준비물을 설치합니다. 이미 내려받았다면 다시 clone하지 않아도 됩니다.
2. 터미널에서 `cd public-cardnews`로 **저장소 폴더 안에 들어온 상태**에서 아래 복사 명령을 실행합니다. `skills/public-cardnews/SKILL.md`가 보이는 위치입니다.
3. `SKILL.md` 하나만 복사하지 말고 **`skills/public-cardnews` 폴더 전체**를 복사합니다. `references`와 `assets`도 필요합니다.

> **이미지 생성에는 세 에이전트 모두 Bun과 OpenAI Codex CLI, 이미지 생성 기능을 사용할 수 있는 본인 Codex 계정이 필요합니다.** Claude Code나 Hermes로 기획하더라도 이미지는 저장소의 Codex 실행기로 생성합니다. 스킬 복사만으로 도구 설치·로그인이 끝나지는 않습니다. [도구 준비·로그인·첫 이미지 생성](docs/QUICKSTART.md)을 함께 진행하세요.
>
> 복사 후에도 **원본 저장소를 이동하거나 삭제하지 마세요.** 스킬 폴더 밖의 `vendor/` 실행기와 `docs/` 문서를 계속 사용합니다. Windows와 WSL은 홈 폴더·인증·실행 경로가 다르므로, **에이전트가 실행되는 환경에서 설치**하세요.

아래 명령은 같은 이름의 스킬이 있으면 덮어쓰지 않고 멈춥니다. 기존 스킬을 직접 수정했다면 먼저 백업하고 차이를 확인하세요.

### 1. Hermes에 설치

기본 설치 위치는 `~/.hermes/skills/public-cardnews`입니다. 별도 프로필을 사용한다면 **해당 프로필의 `HERMES_HOME` 아래**에 설치합니다. 아래 명령은 현재 터미널의 `HERMES_HOME` 값을 우선 사용하므로, 다른 프로필을 사용 중이라면 실행 전에 대상 경로를 확인하세요.

**macOS·Linux·WSL — Bash**

```bash
skills_dir="${HERMES_HOME:-$HOME/.hermes}/skills"
if [ -e "$skills_dir/public-cardnews" ]; then
  printf '이미 설치되어 있습니다. 기존 스킬을 백업·비교하세요.\n'
else
  mkdir -p "$skills_dir" && cp -R skills/public-cardnews "$skills_dir/public-cardnews"
fi
```

**Windows 네이티브 — PowerShell**

```powershell
$hermesHome = if ($env:HERMES_HOME) { $env:HERMES_HOME } else { Join-Path $HOME '.hermes' }
$skillsDir = Join-Path $hermesHome 'skills'
$target = Join-Path $skillsDir 'public-cardnews'
if (Test-Path $target) { throw '이미 설치되어 있습니다. 기존 스킬을 백업·비교하세요.' }
New-Item -ItemType Directory -Force $skillsDir | Out-Null
Copy-Item -Path 'skills/public-cardnews' -Destination $target -Recurse
```

**사용하기:** 같은 저장소 폴더에서 `hermes`를 실행해 새 대화를 열고 다음처럼 요청합니다. 별도 프로필을 쓴다면 그 프로필로 실행하세요.

```text
public-cardnews 스킬을 불러와 줘.
현재 작업 폴더가 public-cardnews 저장소야. 먼저 실제 절대 경로를 확인하고,
그 안의 docs와 vendor 실행기를 사용해 줘.
직원 대상 AI 활용 안내 카드뉴스 2장을 만들고 싶어.
설치 상태와 생성 준비물을 확인한 뒤 기획안과 디자인 후보부터 보여줘.
이미지 생성은 내가 기획과 디자인을 승인한 뒤 진행해 줘.
```

공식 안내: [Hermes 스킬 시스템](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)

### 2. Claude Code에 설치

개인 스킬 폴더인 `~/.claude/skills/public-cardnews`에 설치하면 여러 프로젝트에서 사용할 수 있습니다. 아래는 **로컬 Claude Code 기준**이며, claude.ai 웹의 파일 업로드 안내가 아닙니다.

**macOS·Linux·WSL — Bash**

```bash
skills_dir="$HOME/.claude/skills"
if [ -e "$skills_dir/public-cardnews" ]; then
  printf '이미 설치되어 있습니다. 기존 스킬을 백업·비교하세요.\n'
else
  mkdir -p "$skills_dir" && cp -R skills/public-cardnews "$skills_dir/public-cardnews"
fi
```

**Windows — PowerShell**

```powershell
$skillsDir = Join-Path $HOME '.claude/skills'
$target = Join-Path $skillsDir 'public-cardnews'
if (Test-Path $target) { throw '이미 설치되어 있습니다. 기존 스킬을 백업·비교하세요.' }
New-Item -ItemType Directory -Force $skillsDir | Out-Null
Copy-Item -Path 'skills/public-cardnews' -Destination $target -Recurse
```

**사용하기:** 같은 저장소 폴더에서 `claude`를 실행하고, 대화창에 아래 내용을 입력합니다. `/public-cardnews`는 터미널 명령이 아니라 Claude Code 안에서 사용하는 스킬 호출입니다.

```text
/public-cardnews 현재 작업 폴더가 public-cardnews 저장소야. 실제 절대 경로를 확인하고 이곳의 docs와 vendor 실행기를 사용해 줘. 직원 대상 AI 활용 안내 카드뉴스 2장을 만들려고 해. 생성 준비물을 확인하고 기획안과 디자인 후보부터 보여줘. 이미지 생성은 승인 후 진행해 줘.
```

이 프로젝트에서만 쓰려면 개인 폴더 대신 **사용할 프로젝트의 `.claude/skills/public-cardnews`**에 같은 폴더 전체를 복사해도 됩니다. 개인·프로젝트 위치에 중복 설치할 필요는 없습니다.

공식 안내: [Claude Code 스킬 설치 위치와 호출 방법](https://code.claude.com/docs/en/skills)

### 3. Codex에 설치

공식 문서의 사용자 스킬 위치인 `~/.agents/skills/public-cardnews`에 설치합니다. 아래는 **로컬 Codex CLI 기준**입니다.

**macOS·Linux·WSL — Bash**

```bash
skills_dir="$HOME/.agents/skills"
if [ -e "$skills_dir/public-cardnews" ]; then
  printf '이미 설치되어 있습니다. 기존 스킬을 백업·비교하세요.\n'
else
  mkdir -p "$skills_dir" && cp -R skills/public-cardnews "$skills_dir/public-cardnews"
fi
```

**Windows — PowerShell**

```powershell
$skillsDir = Join-Path $HOME '.agents/skills'
$target = Join-Path $skillsDir 'public-cardnews'
if (Test-Path $target) { throw '이미 설치되어 있습니다. 기존 스킬을 백업·비교하세요.' }
New-Item -ItemType Directory -Force $skillsDir | Out-Null
Copy-Item -Path 'skills/public-cardnews' -Destination $target -Recurse
```

**사용하기:** 같은 저장소 폴더에서 `codex`를 실행합니다. 대화창에서 `/skills`로 `public-cardnews`가 보이는지 확인한 뒤 다음처럼 요청합니다. `$public-cardnews`는 셸 명령이 아니라 **Codex 대화창에 입력하는 스킬 이름**입니다.

```text
$public-cardnews 현재 작업 폴더가 public-cardnews 저장소야. 실제 절대 경로를 확인하고 이곳의 docs와 vendor 실행기를 사용해 줘. 직원 대상 AI 활용 안내 카드뉴스 2장을 만들려고 해. 생성 준비물을 확인하고 기획안과 디자인 후보부터 보여줘. 이미지 생성은 승인 후 진행해 줘.
```

이 프로젝트에서만 쓰려면 개인 폴더 대신 **사용할 프로젝트의 `.agents/skills/public-cardnews`**에 복사하고 그 프로젝트에서 Codex를 실행하세요.

공식 안내: [Codex 스킬 설치 위치와 호출 방법](https://developers.openai.com/codex/skills)

### 설치 확인과 문제 해결

- **스킬이 보이지 않으면:** 에이전트를 종료하고 다시 실행합니다. 설치 폴더 바로 아래에 `SKILL.md`, `references/`, `assets/`가 있는지 확인하세요. `public-cardnews/public-cardnews/SKILL.md`처럼 폴더가 이중으로 들어가면 안 됩니다.
- **스킬은 읽지만 실행기를 못 찾으면:** 내려받은 저장소의 절대 경로를 알려주세요. 새 대화를 다른 폴더에서 시작했다면 특히 필요합니다. 설치된 스킬 폴더와 원본 저장소 폴더는 서로 다릅니다.
- **Windows에서 이미지 생성이 실패하면:** [CODEX_BIN 설정](docs/QUICKSTART.md#windows-실제-codexexe-지정)을 확인하고 같은 환경에서 `codex login status`를 실행하세요.
- **설치 완료와 생성 성공은 별도입니다:** 스킬을 읽은 것을 확인한 뒤 [첫 이미지 생성](docs/QUICKSTART.md#2-첫-표지-생성)까지 성공해야 제작 준비가 끝납니다.

설치 위치와 호출 방법은 각 에이전트의 공식 문서를 기준으로 안내합니다. **세 에이전트·모든 OS에서의 신규 설치 및 이미지 생성 전체 과정을 검증한 것은 아닙니다.** 현재 실기 검증 범위는 [설치 안내의 지원 범위](docs/QUICKSTART.md#지원-범위와-준비물)를 확인하세요.

## 오프라인 검사

```text
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
python scripts/validate.py
bun test ./vendor/baoyu-codex-imagegen/src
```

검사는 스킬 문법·상대 파일 링크·목록과 자산 누락·PNG decode·흔한 민감 경로/토큰 패턴을 확인합니다. 외부 URL 생존, OCR, 법적 검토, 모든 비밀 탐지를 보장하지 않습니다. runs/와 개인 로그는 공개 검사·커밋에서 제외합니다.

## 라이선스와 출처

- 자체 코드·문서·프롬프트: [MIT](LICENSE)
- 공개 승인 생성 PNG: [사용 조건](docs/RIGHTS.md), 권리 보유 범위 내 MIT 허용
- 번들 실행기: Jim Liu의 baoyu-codex-imagegen, MIT, 고정 revision 및 변경 내역은 [고지문](THIRD_PARTY_NOTICES.md)
- OpenAI Codex CLI: 사용자가 별도 설치하는 Apache-2.0 도구. 호스팅 이미지 모델은 이 저장소의 오픈소스 대상이 아닙니다.

[개발 상태와 남은 검증](docs/ROADMAP.md) · [기획 기준](docs/PRD.md) · [분류 기준](docs/TAXONOMY.md)
