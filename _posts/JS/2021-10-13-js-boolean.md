---
title: " "
date: 2021-10-13 08:00:00 -0400
categories: js
---

Baisc boolean logic sample.

```js
// && => true if all are true
// || => true if one is ture
// ! (NOT) => inverts true /false value

var firstName = "John";
var age = 20;

if (age < 13) {
	console.log(firstName + ' is a boy');
} else if (age >= 13 && age < 20) {
	console.log(firstName + ' is a teenager');
} else if (age >= 20 && age < 30) {
	console.log(firstName + ' is a young man');
} else {
	console.log(firstName + ' is a man');
}

if (age < 13) {
	console.log(firstName + ' is a boy');
} else if (age >= 13 || age < 20) {
	console.log(firstName + ' is a teenager');
} else if (age >= 20 || age < 30) {
	console.log(firstName + ' is a young man');
} else {
	console.log(firstName + ' is a man');
}

if (!age < 13) {
	console.log(firstName + ' is not a boy');
} else {
	console.log(firstName + ' is a boy');
}
```