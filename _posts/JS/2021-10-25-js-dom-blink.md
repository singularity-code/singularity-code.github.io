---
title: " "
date: 2021-10-25 08:00:00 -0400
categories: js dom blink
---

Simple blinking DOM Element

```html
<div id="element">BLINK!!!</div>

<script>
  setInterval(() => element.hidden = !element.hidden, 1000);
</script>
```