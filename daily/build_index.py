#!/usr/bin/env python3
"""issues/*.html 을 훑어 index.html(날짜별 아카이브)을 다시 만든다. 표준 라이브러리만 사용."""
import html
import re
from pathlib import Path

ROOT = Path(__file__).parent
ISSUES = sorted(ROOT.glob("issues/????-??-??.html"))  # 오름차순: 호수 = 위치 + 1


def headline(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    m = re.search(r'<h2 id="headline">(.*?)</h2>', text, re.S)
    if not m:
        m = re.search(r"<title>(.*?)</title>", text, re.S)
    return html.escape(re.sub(r"<[^>]+>", "", m.group(1)).strip()) if m else path.stem


def main() -> None:
    if not ISSUES:
        raise SystemExit("issues/ 에 발행된 호가 없습니다.")
    items = []
    for no, p in enumerate(ISSUES, start=1):
        items.append((no, p.stem, headline(p)))
    items.reverse()  # 최신호가 위
    latest_no, latest_date, latest_head = items[0]

    rows = "\n".join(
        f'      <li><time datetime="{d}">{d}<small>제{no}호</small></time>'
        f'<a href="issues/{d}.html" target="_self">{h}</a></li>'
        for no, d, h in items
    )
    page = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>데일리 바이트</title>
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;600;700&amp;display=swap">
</head>
<body>
<div class="wrap">
  <header>
    <div class="top">
      <div class="brand"><a href="index.html" target="_self">데일리 바이트</a><span>AI·개발·신제품 브리핑</span></div>
    </div>
  </header>
  <section class="archive-hero">
    <a class="latest" href="issues/{latest_date}.html" target="_self">
      <span class="latest-meta"><b>최신호</b>제{latest_no}호 · {latest_date}</span>
      <span class="latest-title">{latest_head}</span>
      <span class="latest-go">읽으러 가기 <i aria-hidden="true">→</i></span>
    </a>
  </section>
  <section style="padding:40px 0">
    <ul class="issue-list">
{rows}
    </ul>
  </section>
</div>
</body>
</html>
"""
    (ROOT / "index.html").write_text(page, encoding="utf-8")
    print(f"index.html 갱신: 총 {len(items)}호, 최신 {latest_date}")


if __name__ == "__main__":
    main()
