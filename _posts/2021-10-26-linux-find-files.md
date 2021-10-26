---
title: "[Linux] Find files with name/type"
date: 2021-10-26 08:00:00 -0400
categories: linux shell find
---

Sample shows how to find files with name and extension name in Linux system.

```sh
# with name
find $directory -type f -name "*somename.*"

# with extension / type
find $directory -type f -name "*.pdf"
```