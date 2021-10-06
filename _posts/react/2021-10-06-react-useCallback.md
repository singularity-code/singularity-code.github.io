---
title: "[React.js] UseMemo Hook"
date: 2020-10-06 08:00:00 -0400
categories: js react
---

This sample shows that normal onChange function and using useCallback hook.
useCallback will returns a memorized callback to prevent unnecessary renders.

```js
// assume that you have setNumber function

const onChange = (e) => {
    setNumber(e.target.value);
};

// with callback
const onChange = useCallback((e) => {
    setNumber(e.target.value);
}, []); // [] will create function only on firsttime

```

Official Document
![Hooks API Reference](https://reactjs.org/docs/hooks-reference.html)