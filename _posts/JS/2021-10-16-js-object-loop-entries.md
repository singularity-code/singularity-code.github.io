---
title: "[JS] Loop an Object with entries"
date: 2021-10-16 08:00:00 -0400
categories: js object deconstruct
---

Example shows that how to loop through an object with entries (key, value)

```js
let user = {
  name : "User",
  addr : "Address"
};

for (const [key, value] of Object.entries(user)) {
	console.log(`${key} : ${value}`);
}
```
