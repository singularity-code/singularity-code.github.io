---
title: "자바스크립트 String 카멜 케이스 바꾸기 (JS String to Camelcase)"
date: 2020-09-30 10:00:00 -0400
categories: js javascript string camelcase
---

Reguar Expression을 이용해서 string을 카멜 케이스로 바꾸는 메서드입니다.

```js
let str = "THIS_IS_DOM_ID";

function toCamelCase(str) {
  return str.toLowerCase().replace(/[^a-zA-Z0-9]+(.)/g, (m, chr) => chr.toUpperCase());
}
console.log(toCamelCase(str))
```
