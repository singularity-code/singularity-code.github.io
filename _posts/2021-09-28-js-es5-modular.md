---
title: "[JS] ES5 Common Modular Pattern"
date: 2021-09-28 09:00:00 -0400
categories: js
---

ES5 Basic Module Pattern.

Place public functions in the return statement.

```js
const moduleName = (function () {
  const _private = "something";
  const _privateFunction = function () {
    return;
  };
  const publicFunction = function () {
    return;
  };
  return {
    publicFunction: publicFunction, // This function will expose
  };
})();

// Example
moduleName._privateFunction(); // Invalid
moduleName.publicFunction(); // Valid
```
