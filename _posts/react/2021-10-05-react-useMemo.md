---
title: "[React.js] UseMemo Hook"
date: 2020-10-05 08:00:00 -0400
categories: js react
---

This sample shows usage of useMemo Hook. the getAvg function will called everytime when
onChange triggers on the input. useMemo will only recompute the memorized value has changed.

```js
import React, { useState, useMemo } from "react";

const getAvg = (numbers) => {
  console.log("Init getAvg");
  if (numbers.length === 0) return 0;
  const sum = numbers.reduce((a, b) => a + b);
  return sum / numbers.length;
};

const AverageMemo = () => {
  const [list, setList] = useState([]);
  const [number, setNumber] = useState("");

  const onChange = (e) => {
    setNumber(e.target.value);
  };

  const onInsert = (e) => {
    const nextList = list.concat(parseInt(number));
    setList(nextList);
    setNumber("");
  };

  const avg = useMemo(() => getAvg(list), [list]);

  return (
    <div>
      <input value={number} onChange={onChange}></input>
      <button onClick={onInsert}>Insert</button>
      <ul>
        {list.map((value, index) => (
          <li key={index}>{value}</li>
        ))}
      </ul>
      <div>
        <b>Average: </b> {avg}
      </div>
    </div>
  );
};

export default AverageMemo;
```

Official Document
![Hooks API Reference](https://reactjs.org/docs/hooks-reference.html)
