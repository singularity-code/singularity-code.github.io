---
title: "자바스크립트 2차원 배열 만들기 (Create 2D Array)"
date: 2020-10-19 10:34:00 -0400
categories: js object loop
---

많은 방법이 있겠지만 간단하게 JS에서 2차원 배열을 만드는 예시입니다.

```js
const x = 10;
const y = 10;

let area = new Array(x);
for (let i = 0; i < area.length; i++) {
  area[i] = new Array(y);
}
```

또는

```js
const x = 10;
const y = 10;

let area = new Array(x);
for (const i of area) {
  area[i.index] = new Array(y);
}
console.log(area);
```

```js
// 결과
//
// [
//   [ <10 empty items> ],
//   [ <10 empty items> ],
//   [ <10 empty items> ],
//   [ <10 empty items> ],
//   [ <10 empty items> ],
//   [ <10 empty items> ],
//   [ <10 empty items> ],
//   [ <10 empty items> ],
//   [ <10 empty items> ],
//   [ <10 empty items> ]
// ]
```
