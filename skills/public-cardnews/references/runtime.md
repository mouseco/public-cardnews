# 공개 배포 실행 경로

별도 개인 image-prompt/codex-image 스킬은 필수가 아니다. 이 스킬의 타이포·제작 기준으로 프롬프트를 작성하고 public-cardnews 저장소의 vendor/baoyu-codex-imagegen/src/main.ts를 Bun으로 실행한다. 저장소 위치는 사용자에게 받은 실제 경로를 사용한다. 인증은 본인 Codex 계정으로 수행한다.

[설치와 실행 안내](https://github.com/mouseco/public-cardnews/blob/main/docs/QUICKSTART.md)

표지 생성: `bun vendor/baoyu-codex-imagegen/src/main.ts --image runs/demo/01.png --prompt-file examples/first-run/prompts/01.md --aspect 4:5 --timeout 300000 --retries 0`

후속 장은 첫 결과를 --ref로 전달한다. 같은 스타일의 시리즈만 참조하고 독립 디자인 비교는 각각 생성한다. 공식 외부 이미지의 모델 입력 권한은 별도 확인한다. 샘플 PNG와 현재 원고를 혼동하지 않는다.

타이포 통일은 생성 지시 및 육안검수 기준이며 픽셀 자동 보장 기능이 아니다. 이미지 모델 버전은 실행 결과가 입증하지 않으면 미확인으로 표시한다.
