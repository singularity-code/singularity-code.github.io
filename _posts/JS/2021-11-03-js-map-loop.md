---
title: "[JS] Map loop"
date: 2021-11-03 16:00:00 -0400
categories: js map loop
---

```js
let recipeMap = new Map([
  ['cucumber', 500],
  ['tomatoes', 350],
  ['onion',    50]
]);

// Loop through keys (vegetable)
for (let vegetable of recipeMap.keys()) {
  console.log(vegetable); // cucumber, tomatoes, onion
}

// Loop through values (amount)
for (let amount of recipeMap.values()) {
  console.log(amount); // 500, 350, 50
}

// Loop through [key, value]
for (let entry of recipeMap) { // Same as recipeMap.entries()
  console.log(entry); // cucumber,500 ...
}

// Map has forEach built in function
recipeMap.forEach( (value, key, map) => {
  console.log(`${key}: ${value}`);
});
```

Result
```js
cucumber
tomatoes
onion
500
350
50
[ 'cucumber', 500 ]
[ 'tomatoes', 350 ]
[ 'onion', 50 ]
cucumber: 500
tomatoes: 350
onion: 50
```