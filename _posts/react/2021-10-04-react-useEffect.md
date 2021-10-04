---
title: "[React.js] UseEffect Hook"
date: 2020-10-04 08:00:00 -0400
categories: js react.js
---

Example component shows useEffect Hook. Provice a second argument will give you which value update.

```js
import React, { useState, useEffect } from "react";

const Info = () => {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    console.log("Render Complete");
    console.log({
      firstName,
      lastName,
    });
    return () => {
      console.log("callback");
      console.log(firstName);
    };
  }, []);

  const onChangeName = (e) => {
    setFirstName(e.target.value);
  };

  const onChangeLastName = (e) => {
    setLastName(e.target.value);
  };
  return (
    <div>
      <div>
        <input value={firstName} onChange={onChangeName}></input>
        <input value={lastName} onChange={onChangeLastName}></input>
      </div>
      <div>
        <b>First Name: </b> {firstName}
      </div>
      <div>
        <b>Last Name: </b> {lastName}
      </div>
    </div>
  );
};

export default Info;
```

Official Document
![Using the Effect Hook](https://reactjs.org/docs/hooks-effect.html)
