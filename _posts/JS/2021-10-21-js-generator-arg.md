---
title: "[JS] Generator Args"
date: 2021-10-21 08:00:00 -0400
categories: js generator args
---

With generator, you can call the yield like a tokken.
Here is an example.

The returned yield object has `value` and `done`
when the last yield then `done` will be `true`

```js
function* gen() {
  yield "First Statement";
  yield "Second Statement";
  yield "Third Statement";
}

let generator = gen();

console.log(generator.next().value); // First
console.log(generator.next().value); // Second
console.log(generator.next().value); // Third
console.log(generator.next().value); // undefined
console.log(generator.next());
console.log(generator.next().done == true) // true
```

Another example
```js
const generator2 = numGen(2);

console.log(generator2.next().value); // 0
console.log(generator2.next().value); // 1
console.log(generator2.next().value); // 2
console.log(generator2.next().value); // undefined
console.log(generator2.next().done); // true
```