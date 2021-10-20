---
title: "[JS] Deconstruct Assignemnt Example"
date: 2021-10-20 08:00:00 -0400
categories: js object deconstruct example
---

This example shows that how to use deconstucting assignment with some function parameters.

The old way you must provide the parameters in orders.
```js
// Static assignment
function ajax(title, url, params, onSuccess, onFail, onCallback) {
  console.log(title, url, params, onSuccess, onFail, onCallback);
}

ajax("selectSome", "/data/selectSome", "", "", function () {});
```

With deconstructing assignment, you do not need to worry about the ordering of parameters.
If the name is matched then will assign to the value.

```js
// New with destrucuring
function ajax2({ title, url, params, onSuccess, onFail, onCallback }) {
  console.log(title, url, params, onSuccess, onFail, onCallback);
  onSuccess();
  onCallback();
}

// Use it
let request = {
  url: "/data/update",
  title: "update",
  onCallback: () => {
    console.log("Callback Function");
  },  
  onSuccess: () => {
    console.log("Successful!");
  },
};

// Run
ajax2(request);
```
