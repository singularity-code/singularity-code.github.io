---
title: "[JS] Find an object in an array"
date: 2021-10-08 08:00:00 -0400
categories: js array search
---

This sample shows how to find an object with key, value in an array.
find() method will stop loop when the condition is true.
If the condition is not true then return `undefined`.

```js
let users = [
  {id: 1, name: "John"},
  {id: 2, name: "Pete"},
  {id: 3, name: "Mary"}
];

let user = users.find(item => item.id == 1);
console.log(user);
```

MDN Web Docs

<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find" target="_blank">Array.prototype.find()</a>