---
title: "[JS] Compare two arrays"
date: 2021-10-06 08:00:00 -0400
categories: js array filter
---

Sample shows compare two arrays and return new array with common element and not common element

```js
const arr1 = [1,2,3,4,5,6];
const arr2 = [4,5,6,7,8,9];

const r = arr1.filter(function(x) {
  return arr2.includes(x);
});

console.log('Same', r);

const r2 = arr1.filter(function(x) {
  return !arr2.includes(x);
});

console.log('Not same', r2);
```
