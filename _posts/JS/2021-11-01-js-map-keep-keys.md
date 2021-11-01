---
title: "[JS] Map keeping keys"
date: 2021-11-01 17:00:00 -0400
categories: js map keep keys
---

Simple example shows that JS Map keeps the keys compare to an object does not keep the different data type of keys.

```js
var obj = {
  1: "1",
  1: "1",
};
// { '1': '1' }
console.log(obj);

var map = new Map();
map.set("1", "str1");
map.set(1, 1);
map.set(true, "bool1");
// Map(3) { '1' => 'str1', 1 => 1, true => 'bool1' }
console.log(map);

map.set(1, 1);
// Map(3) { '1' => 'str1', 1 => 1, true => 'bool1' }
console.log(map);

```