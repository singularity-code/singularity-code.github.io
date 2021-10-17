---
title: "[JS] Array - Deconstructing assignment"
date: 2021-10-17 08:00:00 -0400
categories: js array deconstruct assignment
---

Sample shows that automatically assign array elements to new variables.
They assigned value type is not an array.

```js
// Deconstructing an array and assign to variables.
let arr = ["Firstname", "Address"];
let [name, address] = arr;
console.log(typeof(firstname), firstname)

// split returns an array
let [firstName, lastName] = "Firstname Lastname".split(' ');
console.log(typeof(lastName), lastName)

// Skip assigning
let [title1, , , title2] = ["Sameple1", "Sample2", "Sample3", "Sample4", "Sample5"];
console.log(typeof(title2), title2);
