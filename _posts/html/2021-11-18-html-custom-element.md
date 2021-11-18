---
title: "[HTML5] Create an custom element"
date: 2021-11-18 10:00:00 -0400
categories: html web js element custom
---

This sample shows that how to define a custom HTML docuemnt using `window.customElements`.

```html
customElements.define('show-hello', class extends HTMLElement {
  connectedCallback() {
    const shadow = this.attachShadow({mode: 'open'});
    shadow.innerHTML = `<p>
      Hello, ${this.getAttribute('name')}
    </p>`;
  }
});
```

To use, include shadow element to a HTML DOM.

```html
<show-hello name="John"></show-hello>
```

Check out the documents for more details and Browser compatibility.
<a href="[https://](https://developer.mozilla.org/en-US/docs/Web/API/Window/customElements)" target="_blank">Window.customElements</a>
