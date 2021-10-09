---
title: "[Python] Basic Class"
date: 2021-10-09 08:00:00 -0400
categories: python
---

This is a simple example of python class object

```python
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

p = Point(3,5)
print(p.x)
print(p.y)
```

Official Document

<a href="https://docs.python.org/3/tutorial/classes.html" target="_blank">Python Classes</a>