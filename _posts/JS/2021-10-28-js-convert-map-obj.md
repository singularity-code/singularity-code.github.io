---
title: "[JS] Convert Map to Object"
date: 2021-10-28 08:00:00 -0400
categories: js map object convert
---

Simple example of convert a map to an object

```js
let map = new Map();
map.set('banana', 1);
map.set('orange', 2);
map.set('meat', 4);

let obj = Object.fromEntries(map.entries()); // Converting
console.log(obj);
console.log(obj.orange); // 2
```