---
title: "[JS] Simple way to measure execution time"
date: 2021-10-15 08:00:00 -0400
categories: js console time
---

This sample shows count execution time for a function.

```js
const test = () => {
  let a = 0;
  for (i = 0; i <= 100000; i++) {
    a++;
  }
}

console.time();
test();
console.timeEnd();
```

<a href="https://developer.mozilla.org/en-US/docs/Web/API/console/time" target="_blank">MDN console.time()</a>