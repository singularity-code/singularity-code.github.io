---
title: "[Python] Basic Class"
date: 2021-10-09 08:00:00 -0400
categories: python
---

This is a simple example of python class object

```python
class Point:
  name = "First Name"
  arr = [1,2,3]

  def __init__(self, x, y):
    self.x = x
    self.y = y

p = Point(3,5)
print(p.name)
p.name = "Another Name"
print(p.name)

print(p.arr)
p.arr.append(4)
print(p.arr)

print(p.x, p.y)
p.x = 10
print(p.x, p.y)
```

Official Document

<a href="https://docs.python.org/3/tutorial/classes.html" target="_blank">Python Classes</a>