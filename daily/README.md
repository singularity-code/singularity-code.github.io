# 데일리 바이트

매일 아침 만드는 IT·AI 브리핑. `singularity-code.github.io` 저장소의 `daily/` 폴더에 있고, GitHub Pages로 서비스한다(저장소 루트는 기존 Jekyll 블로그).

- 최신호와 지난 호: https://singularity-code.github.io/daily/
- 발행 절차: [CLAUDE.md](CLAUDE.md)

## 구조

- `issues/YYYY-MM-DD.html` 하루 한 호
- `assets/style.css` 모든 호가 같이 쓰는 디자인
- `template/issue.html` 새 호의 뼈대
- `build_index.py` `index.html`(아카이브)을 다시 만든다. `index.html`은 직접 고치지 않는다.

`CLAUDE.md`, `README.md`, `template/`, `build_index.py`는 루트 `_config.yml`의 `exclude`에 등록되어 사이트에 게시되지 않는다. (`CLAUDE.md`의 `{{...}}` 표기가 Jekyll Liquid 빌드를 깨뜨리지 않게 하려는 목적도 있다.)

## Claude Cowork 예약 작업 등록

Claude Desktop의 Cowork 탭에서 사이드바의 **Scheduled**를 열고 **New task**를 눌러 만든다. 또는 Cowork 작업 안에서 `/schedule`을 입력해 대화로 만들 수도 있다.

- 이름: 데일리 바이트 발행
- 빈도: 매일, 한국 시간 오전 7시(원하는 시각)
- 작업 폴더: 로컬 저장소의 **`daily/` 폴더**
- 프롬프트:
  ```
  이 폴더의 CLAUDE.md 절차에 따라 오늘자 데일리 바이트를 발행해 줘.
  ```

예약을 켜기 전에 같은 프롬프트를 Cowork 작업으로 한 번 직접 실행해 보고, 결과(`issues/` 새 파일, 푸시, 사이트 반영)를 확인하는 것을 권한다.

## 알아둘 점

- 예약 작업은 **컴퓨터가 켜져 있고 Claude Desktop 앱이 열려 있을 때** 실행된다.
- 터미널에서 `git push`가 비밀번호 입력 없이 되어야 한다(예약 작업은 사람이 입력할 수 없다).
- 디자인을 바꾸려면 `assets/style.css`와 `template/issue.html`을 고친다. 지난 호도 같은 CSS를 쓰므로 함께 바뀐다.
