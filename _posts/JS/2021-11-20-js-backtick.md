---
title: "[JS] Backtick String"
date: 2021-11-20 22:00:00 -0400
categories: js string backtick
---

Below multiple liens of strings with "" are not correct syntax in JS.

Use of backtick `` will allow you to combine strings

```js
let originList = "Guests:
* John
* Pete
* Mary
";
```

But you can use it with backticks

```js
let guestList = `Guests:
 * John
 * Pete
 * Mary
`;
console.log(guestList);
```

This is usuful when you declare HTML syntax as a string.

```js
// provide better human readable
const html = `
  <div>
    <p>Example</p>
  </div>
`;
console.log(html);
```

Using `${}` will allow to use single line JS syntax and excute.

```js
function sum(a, b) {
  return a + b;
}

console.log(`1 + 2 = ${sum(1, 2)}`);

// Result
// 1 + 2 = 3
```
