---
title: "[JS] Slice Strings"
date: 2021-12-07 15:00:00 -0400
categories: js string slice
---

Example codes of `String.slice()`

```js
let str = "stringify";
console.log(str.slice(0, 5) ); // 'strin', from 0 to 5
console.log(str.slice(0, 1) ); // 's', from 0 to 1

str = "stringify";
console.log(str.slice(2) ); // ringify, from 2 to end

str = 'stringify';

// from last 4 to last 1
console.log(str.slice(-4, -1) ); // gif
str = 'stringify';
```

Please aware that `String.substring()` and `String.slice` result is not same


```js
// same value will be returned
console.log(str.substring(2, 6) ); // "ring"
console.log(str.substring(6, 2) ); // "ring"

// slice result is not same as substring
console.log(str.slice(2, 6) ); // "ring"
console.log(str.slice(6, 2) ); // ""
```