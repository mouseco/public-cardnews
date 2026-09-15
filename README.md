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

**S01–S06는 직접 생성한 샘플입니다.** 번호·경로·상태·출처의 정본은 [통합 목록](skills/public-cardnews/assets/catalog.json) 한 곳입니다.

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

## 실제 배포 예제

가상 기관 **새봄연구소**의 S02 메모지형 2장입니다.

<p><img src="examples/first-run/result/01.png" alt="예제 표지" width="45%" /><img src="examples/first-run/result/02.png" alt="예제 본문" width="45%" /></p>

[원고 프롬프트](examples/first-run/prompts/01.md) · [검수 기록](examples/first-run/result/review.md) · [PNG·프롬프트·검수 ZIP](examples/first-run/demo.zip)

기존 Windows PC의 새 소스·출력 폴더에서 생성했습니다. 기존 계정 로그인을 사용했으며 새 PC·빈 사용자 홈 검증으로 간주하지 않습니다. Codex 0.154.0, Bun 1.3.10에서 실행했습니다. 실제 이미지 모델 버전은 미확인입니다.

## 작업 흐름

기획안이 있으면 문구·수치·장수를 보존합니다. 없으면 목적·독자·근거·참여 경로를 확인하고 기획부터 제안합니다.

**기획 승인 → 디자인 선택 → 장별 프롬프트 → 첫 장 생성·확인 → 후속 장 → 원고 대조·PNG 검사 → 전달**

같은 위계 글자 크기, 의미 단위 줄바꿈, 숫자·단위 묶음은 프롬프트와 육안검수 기준입니다. 픽셀 단위 타이포 통일이나 한글·그래프 무오류를 자동 보장하지 않습니다. 오류는 해당 장을 재생성해 해결합니다.

## 설치형 스킬

[SKILL.md](skills/public-cardnews/SKILL.md)와 references·assets 폴더를 함께 Hermes 활성 프로필에 복사합니다. [상세 설치 안내](docs/QUICKSTART.md)를 따르고 실행기 저장소의 실제 위치를 에이전트에게 알려주세요. 다른 에이전트에서는 지침으로 읽고 CLI를 직접 호출할 수 있습니다.

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
