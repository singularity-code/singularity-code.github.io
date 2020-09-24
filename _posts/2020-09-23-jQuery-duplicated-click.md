---
title: "jQuery – Duplicated onClick Event"
date: 2020-09-23 10:34:00 -0400
categories: javascript jQuery
---
`jQuery` 라이브러리를 이용해서 한번 `click event` 를 사용했는데 실행은 두번되는 경우가 있습니다.
해결방법은 이미 바인딩된 `click`을 한번 언바인딩하고 다시 `click event`를 바인딩 해주면 됩니다.

```js
$("#btnPrint").unbind('click').bind('click', function(e) {
  e.preventDefault();
  // do somthing
});
```
