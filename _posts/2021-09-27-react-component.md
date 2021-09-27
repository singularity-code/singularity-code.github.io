---
title: "React Function and Class Component Template"
date: 2021-09-27 12:34:00 -0400
categories: react
---
There are two way to create a React Component.
Different things are a `Class component` can use "State" and "Life Cycle Methods".
But recent version of `Function Component` also use "State" features using Hook and `Function Component` is simpler than `Class Component`.

React recommand to use functional component for the future.

More information: <a href="https://reactjs.org/docs/components-and-props.html" target="_blank">React.js Component and props</a>

Default React Class Component

```js
import React, { Component } from 'react';

class classComponent extends Component {
  render() {
    return (
      <div>
        
      </div>
    );
  }
}

export default classComponent;
```

Default React Functional Component

```js
import React from 'react'

const functionComponent = () => {
  return (
    <div>
      
    </div>
  )
}

export default functionComponent;
```