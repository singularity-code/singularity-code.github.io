---
title: "[React.js] Component Iteration"
date: 2021-09-29 10:34:00 -0400
categories: python
---

The key must be unique, it could be an index or unique value from the list item.

```js
import React from "react";

function IterationSample() {
  const names = ["snow", "ice", "fire", "wind"];
  const nameList = names.map((name, index) => <li key={index}>{name}</li>);
  return (
    <div>
      <ul>{nameList}</ul>
      
    </div>
  );
}

export default IterationSample;

```
