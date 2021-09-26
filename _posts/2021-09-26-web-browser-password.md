---
title: "Prevent the browser saving password"
date: 2021-09-26 17:34:00 -0400
categories: web
---

Browser saving password popup is triggered by input type "password". It should not be triggered when autocomplete attribute is not "on" but some browser ignore when it "off" because the browser suggest that it is better security practice for storing the password.

However if you want to prevent he saving password popup for another security concern, these method might be useful while some browser ignore whatever you set the autocomplete attribute.

But this solution may not supported all browsers and you will need to careful to use this code because this might show what password entering in the input.

```html
<input type="text" id="input_password" class="password" autocomplete="off"/>
```

```css
#password {
  text-security: disc;
  -webkit-text-security: disc;
  -moz-text-security: disc;
}
```

```js
// With jQuery
if($("#input_password").css("webkitTextSecurity") !== "disc") {
  $("#loginPass").attr("type", "password");
}

// No jQuery
if (window.getComputedStyle(input_password).webkitTextSecurity !== "disc") {
 $("#input_password").attr("type", "password");
}
```

If you do not prefer above way and want to keep the input type as "password" then try below.

```html
<input type="password" name="Password" autocomplete="off" readonly onfocus="this.removeAttribute('readonly');" >
```