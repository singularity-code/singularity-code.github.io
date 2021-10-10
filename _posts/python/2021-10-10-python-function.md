---
title: "[Python] Function"
date: 2021-10-10 08:00:00 -0400
categories: python
---

Simple example shows python function

```python
def square(x):
  return x * x

def main():
  for i in range(10):
    print("{} squared is {}".format(i, square(i)))

if __name__ == "__main__":
  main()
```
