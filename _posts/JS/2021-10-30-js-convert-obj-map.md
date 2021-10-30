---
title: "[JS] Convert an object to an map"
date: 2021-10-30 08:00:00 -0400
categories: js map object convert
---

```js
let obj = {
  name: "John",
  age: 30,
};

let map = new Map(Object.entries(obj));
console.log(obj);
console.log(map);
console.log(map.get("name"));
```