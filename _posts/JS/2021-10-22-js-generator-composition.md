---
title: " "
date: 2021-10-22 08:00:00 -0400
categories: js generator composition
---

This example shows that how to compose two or more generator functions.

```js

// First generator to return start num to end num
function* generateSequence(start, end) {
  for(let i = start; i <= end; i++) yield i;
}

// Second generator to call first generator and return sequence of strings
function* generatePasswordCodes() {
  yield* generateSequence(48, 57); // 0123456789
  yield* generateSequence(65, 90); // ABCDEFGHIJKLMNOPQRSTUVWXYZ
  yield* generateSequence(97, 122); // abcdefghijklmnopqrstuvwxyz
}

// Use of two generator composition
let str = '';

for (let code of generatePasswordCodes()) {
  str += String.fromCharCode(code);
}

console.log(str);
```