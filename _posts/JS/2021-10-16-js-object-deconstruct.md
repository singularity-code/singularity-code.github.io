---
title: "[JS] Deconstruct an object"
date: 2021-10-16 08:00:00 -0400
categories: js object deconstruct
---

Example shows that how to deconstruct an object to assign to another object.

```js
let options = {
  size: {
    width: 100,
    height: 200
  },
  items: ["Cake", "Donut"],
  extra: true
};

let {
  size: { // size = 0,
    width,
    height
  },
  items: [item1, item2], // assign items
  title = "Menu" // title will be "Memo"
} = options;

console.log(title);  // Menu
console.log(width);  // 100
console.log(height); // 200
console.log(item1);  // Cake
console.log(item2);  // Donut
```
