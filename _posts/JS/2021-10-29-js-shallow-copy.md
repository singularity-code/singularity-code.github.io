---
title: "[JS] Shallow copy an array"
date: 2021-10-29 08:00:00 -0400
categories: js shallow copy array
---

When copying an array with spread operator (...) is a shallow copy.
Which means if the array containing an object will be still pointing same object not copying.

```js
// Shallow copy
const origin1 = [
  { id: 1, checked: true },
  { id: 2, checked: true },
];

const copy1 = [...origin1];

console.log(origin1);
console.log(copy1);
// Copied to new array
console.log(origin1 == copy1);
origin1[0].checked = false;
// This is true because the contents of the array is pointing same object.
console.log(origin1[0] == copy1[0]);
```
