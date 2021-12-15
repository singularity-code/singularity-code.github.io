---
title: "[JS] Promise Basics"
date: 2021-12-15 10:00:00 -0400
categories: js promise es6
---

### 1. Resolve case

```js
//resolve
var promise = new Promise(function (resolve, reject) {
  setTimeout(() => resolve('done!'), 1000);
});

promise.then(
  (result) => console.log('CASE 1', result),
  (error) => console.log('CASE 1',error.message)
);
```

### 2. Reject case

```js
//reject
var promise = new Promise(function (resolve, reject) {
  setTimeout(() => reject(new Error('failed!')), 2000);
});

promise.then(
  (result) => console.log('CASE 2',result),
  (error) => console.log('CASE 2',error.message)
);
```

### 3. Handling only error with passing null in resolve

```js
// handle only error
var promise = new Promise(function (resolve, reject) {
  setTimeout(() => reject(new Error('handle failed!')), 2000);
});

promise.then(null, (e) => console.log('CASE 3',e.message));

// or you can use catch
promise.catch((e) => console.log('CASE 3', e.message));
```

### 4. Finally - Execute always without result of resolve or reject

```js
//finally (good for cleanup)
new Promise(function (resolve, reject) {
  setTimeout(() => resolve('Resolved'), 1000);
})
  .finally(() => console.log('CASE 4 Finally! I always run!'))
  .then(
    (result) => console.log('CASE 4', result),
    (error) => console.log('CASE 4', error.message)
  );
```