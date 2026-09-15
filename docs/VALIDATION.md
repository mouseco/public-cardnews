# v0.5.0-beta.1 검증 기록

- 새 Python venv에 requirements-dev.txt만 설치: 성공.
- 자체 unittest 4개: 통과. 문법/링크/민감 경로 탐지, 목록 자산 누락, 손상 PNG, 실행기 sandbox·binary 설정 확인.
- Windows Bun 1.3.10에서 원본 실행기 테스트: 17개 통과.
- 저장소 validate.py: ok=true, errors=[] (당시 저장소 전체).
- git diff --check: 통과.
- 별도 새 소스·출력 폴더에서 예제 두 장 생성: 각 status=ok, cached=false. 57초·59초 반환.
- 예제 PNG 두 장 decode 및 육안 문구 확인, ZIP CRC 검사 완료.
- 실제 새 PC, 빈 사용자 홈, macOS/Linux 네이티브 생성은 미검증.
- GitHub Actions는 push 후 별도 실행된다. 로컬 통과를 원격 CI 통과로 간주하지 않는다.

생성 예제의 파일별 해시는 [manifest](../examples/first-run/result/manifest.json)에 기록했다. 런타임 개인 경로와 원본 로그는 공개하지 않았다.
