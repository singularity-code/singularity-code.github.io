---
title: "[jQuery] How to add custom values on form submit"
date: 2021-11-23 16:00:00 -0400
categories: js jQuery HTML form submit
---

Assume that the `<form id="loginForm"></form>` exist and other input values included

```js
const password = "";
$("#loginForm").attr("action", "/auth/login");
$("#loginForm").attr("method", "POST");

//add custom value with hidden field
const param_password = $("<input type='hidden' value=" + password + " name='loginPass' readonly>");
$("#loginForm").append(param_password);
$("#loginForm").submit();
```
