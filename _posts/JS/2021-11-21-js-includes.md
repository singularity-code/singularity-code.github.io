---
title: "[JS] Find a included string"
date: 2021-11-21 08:00:00 -0400
categories: js string include endwith startwith
---

`String.includes(substr, pos)` returns true or false when the String includes the word.

```js
console.log("Widget with id".includes("Widget")); // true
console.log("Hello".includes("Bye")); // false
console.log("Widget".includes("id")); // true
console.log("Widget".includes("id", 3)); // false, no "id" after index 3 position
```

Also, you can use `String.startwith()` or `String.endwith()` to find a word includes in the text.

```js
console.log("Widget".startsWith("Wid")); // true
console.log("Widget".endsWith("get")); // true
```