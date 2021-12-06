---
title: "[JS] Cut string into limited length"
date: 2021-12-06 08:00:00 -0400
categories: js string cut limit
---

Sample function to cut string into desired limit value.

```js
const limitTitle = (title, limit = 17) => {
  const newTitle = [];
  if(title.length > limit) {
    title.split(' ').reduce((acc, cur) => {
      if (acc + cur.length <= limit) {
        newTitle.push(cur);
      }
      return acc + cur.length
    }, 0);
    return `${newTitle.join(' ')} ...`;
  }
  return title;
}

console.log(limitTitle("This is an example title"));
```
