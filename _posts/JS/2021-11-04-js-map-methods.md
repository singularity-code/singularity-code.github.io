---
title: " "
date: 2021-11-04 13:00:00 -0400
categories: js map method
---

new Map() – create a new map.
map.set(key, value) – set key and value pair.
map.get(key) – `return key's value`. If no key exist then `return undefined`.
map.has(key) – If key is exist then `true`, if not then `false`.
map.delete(key) – Delete the key.
map.clear() – Clear the map.
map.size – Return the size of the map (How many keys in the map).

```js
var map = new Map();
map.set("1", "str1");
map.set(1, "num1");
map.set(true, "bool1");
map.set("test", "Some Value");
console.log(map);
console.log(map.has("test"));
console.log(map.get("test"));
console.log("Size: ", map.size);
map.delete("1");
console.log("Size: ", map.size);
console.log(map.get("1"));
console.dir(map);
map.clear();
console.dir(map);
```