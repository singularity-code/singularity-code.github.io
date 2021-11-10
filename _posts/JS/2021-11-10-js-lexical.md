---
title: "[JS] Lexical Scope with IIFE"
date: 2021-11-10 10:00:00 -0400
categories: js scopre IIFE lexical
---

Case 1. Even with `var` the variable is hoisting inside the IIFE.

```js
(function() {
  // var is hoisting inside scope.
  for(var i=0; i<10; i++) {
    console.log('i', i)
  }
})()
console.log('after loop i is', i) // ReferenceError: i is not defined
```

Case 2. without `var` the variable is hoisting outside the IIFE.

```js
// var i is accessed outside of scope
(function() {
  for(i=0; i<10; i++) {
    console.log('i', i)
  }
})()
console.log('after loop i is', i) // after loop i is 10
```

Case 3. With `use strict` the variable `i` is not hoisting outside of scope.

```js
(function() {
  'use strict'
  for(i=0; i<10; i++) {
    console.log('i', i)
  }
})()
console.log('after loop i is', i) // ReferenceError: i is not defined
```
