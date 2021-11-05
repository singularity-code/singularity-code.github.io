---
title: "[JS] Assign an Object with Object as a key"
date: 2021-11-05 08:00:00 -0400
categories: js object key
---

What will be happen if you use an object as a key in an object?
Run below code and see how it goes.

```js
let obj = { name: "MYNAME" };

let testObj = {};
testObj[obj] = 123;

console.log(testObj); // { '[object Object]': 123 }
console.log(testObj.obj); // undefined
console.log(testObj[obj]); // 123

let obj2 = { name: "YOURNAME" };
testObj[obj2] = 456;
console.log(testObj); // { '[object Object]': 456 }
console.log(testObj[obj2]); // 456
```

As you see an object key can be an object but you can not assign another object as another key because an object does not allow duplicated key pair.

Same code on map, map allows duplicated key values.

```js
let testMap = new Map();
testMap.set(obj, 123);
console.log(testMap);
console.log(testMap.get(obj));
testMap.set(obj2, 456);
console.log(testMap);
console.log(testMap.get(obj2));
```