---
title: "[JS] Random Soring Array"
date: 2021-09-30 10:34:00 -0400
categories: js
---

This is to sort elements in an array random orders.

```js
const points = [40, 100, 1, 5, 25, 10];
const result = points.sort(function(a, b){return 0.5 - Math.random()});

console.log(result);
```