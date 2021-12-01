---
title: "[React] Routing"
date: 2021-12-01 17:00:00 -0400
categories: react routing dom
---

Example of React DOM Router usage.

Here assume that you already have `Menu` and `Page` Component to render.

Configure index.js to wrap `<App/>` in the `<BrowserRouter/>`

index.js
```js
import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import { BrowserRouter } from "react-router-dom";

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById("root")
);
```

Then place each path `<Route/>` in the `<Routes/>` and declare the `path` and the `element`.

App.js
```js
import { Routes, Route } from "react-router-dom";
import Menu from "./components/Menu";
import Page1 from "./pages/Page1";
import Page2 from "./pages/Page2";

function App() {
  return (
    <div>
      <Menu />
      <hr />
      <Routes>
        <Route path="/page1" element={<Page1/>} />
        <Route path="/page2" element={<Page2/>} />
      </Routes>
    </div>
  );
}

export default App;
```
