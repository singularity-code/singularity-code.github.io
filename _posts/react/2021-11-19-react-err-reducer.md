---
title: "[Redux] Expected the reducer to be a function"
date: 2021-11-19 14:00:00 -0400
categories: redux reducer error
---

If you see `Error: Expected the reducer to be a function.`

message when you call `createStore` to create store.

Check out the second argument of `createStore`. It must be a function.

```js
// Error
const store = createStore(rootReducer, composeWithDevTools);

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>,
  document.getElementById('root'),
```

```js
// Correct
const store = createStore(rootReducer, composeWithDevTools());

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>,
  document.getElementById('root'),
```
