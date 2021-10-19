---
title: "[JS] Object Deconstructing Assignment"
date: 2021-10-19 08:00:00 -0400
categories: js deconstructing assignment object
---

```js
let options = {
  title: "SOMETHING",
  width: 200,
  height: 300
};

// Not assigned because key name does not exist
let {test1, test2, test3} = options;
console.log("First Value ", test1);
console.log("Second Value ", test2);
console.log("Third Value ", test3);

// Assigned value with matching keys
let {title, width, height} = options;
console.log("Assigned Title ", title);
console.log("Assigned Height ", height);

// Assign matched key's value to the new variable name
let {
  title: t,
  width: w,
  height: h
} = options;
console.log(t, w, h);


// Assign remaning value as origin's key
let {title: t3, ...rest} = options;
console.log("Value of t3 ", t3);
console.log(rest);

let {...args} = options;
console.log(args)
console.log(args.title)
```