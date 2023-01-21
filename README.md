# Custom Scheme

윈도우용 커스텀 URI 스킴 테스트용 저장소

## 파일

- build.cmd : 테스트 파이썬 스크립트 빌드 및 특정 풀더로 파일 이동

- client.py : 테스트 파이썬 스크립트로 커스텀 URI 스킴으로 실행되는 프로그램입니다.
- game.py   : 테스트 클라이언트가 실행하는 프로그램입니다.

- Install.reg   : 커스텀 URI 스킴 레지스트리 등록 편집기
- Uninstall.reg : 커스텀 URI 스킴 레지스트리 삭제 편집기

## 메모

1. 파이썬 스크립트를 빌드하려면 pyinstaller가 필요합니다.

2. `C:\` 드라이브에 `p-launcher` 풀더에 결과물을 저장하고 실행합니다. (레지스트리에서 확인 가능)

## 형식

URI는 다음과 같습니다.

```
p-launcher://game/{GAME_ID}

GAME_ID: 숫자로만 구성됩니다.
```
