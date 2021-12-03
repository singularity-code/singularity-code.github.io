---
title: "[JS] Formatting console output"
date: 2021-12-03 08:00:00 -0400
categories: web js console CSS
---

You can pass arguments to the console.log like a C printf();

With `%c` and second parameter, you can inject CSS style to the text.

---

`%s`	Formats the value as a string

`%i` or `%d`	Formats the value as an integer

`%f`	Formats the value as a floating point value

`%o`	Formats the value as an expandable DOM element

`%O`	Formats the value as an expandable JavaScript object

`%c`	Applies CSS style rules to the output string as specified by the second parameter

```js
console.log("%s is %i", "Pie", 3.1415926535);
// Pie is 3
console.log("%s is %f", "Pie", 3.1415926535);
// Pie is 3.1415926535

console.log("%c CSS text", "color: blue; font-size: 13px");
// Check out in the browser console
```