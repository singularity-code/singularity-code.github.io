---
title: "[JS] Sort objects in an array"
date: 2020-10-02 08:00:00 -0400
categories: js
---

This is how to sort an array containing objects.
If you want to performance check, remove comments on console.times.

```js
const cars = [
	{ type: 'Company1', year: 2016 },
	{ type: 'Company2', year: 2001 },
	{ type: 'Company3', year: 2010 },
];
let result;

//console.time();
result = cars.sort(function (a, b) {
	return a.year - b.year;
});
//console.timeEnd();

console.log(result);

//console.time();
reult = cars.sort(function (a, b) {
	let x = a.type.toLowerCase();
	let y = b.type.toLowerCase();
	if (x < y) {
		return -1;
	}
	if (x > y) {
		return 1;
	}
	return 0;
});
//console.timeEnd();

console.log(result);
```