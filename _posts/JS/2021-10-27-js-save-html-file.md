---
title: "[JS] Save HTML as a file"
date: 2021-10-27 08:00:00 -0400
categories: js HTML save
---

This is a sample code to save the HTML document as a file programmtically which
you can use "save" function to be used somewhere such as a special event.

```js
const save = function () {
	var htmlContent = new Array(document.documentElement.innerHTML);
	var bl = new Blob(htmlContent, { type: 'text/html' });
	var a = document.createElement('a');
	a.href = URL.createObjectURL(bl);
	a.download = 'test-transcripts';
	a.hidden = true;
	document.body.appendChild(a);
	a.click();
};
```