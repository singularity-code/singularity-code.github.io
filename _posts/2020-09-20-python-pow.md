---
title: "python 제곱과 루트 구하기"
date: 2020-09-20 01:54:28 -0400
categories: python
---

제곱과 루트 표현법을 두개의 좌표를 통해 라인의 거리와 경사를 구하는 프로그램으로 알아보겟습니다.

파이썬에서 루트,제곱을 구하는 방법은 여러가지가 있지만 크게 두가지가 있습니다.
`제곱`

```python
a ** n
math.pow(a, n)
```

`루트`

```python
x ** 0.5
math.sqrt(x)
```

math모듈을 통해서 pow(a, n) sqrt(x) 로도 사용가능합니다.

이것을 응용한 점두개를 이용해 선을 만든뒤 거리와 경사를 구하는 클래스입니다.

제곱은 (x + y ) ** 2 또는 math.pow(( x + y), 제곱횟수)

루트는 (x + y ) ** 0.5 또는 math.sqrt(x + y) 를 이용합니다.

```python
import math

class Line(object):
  def __init__(self, coor1, coor2):
    self.coor1 = coor1 # 1번점 (x1, y1)
    self.coor2  = coor2  #2번점 (x2, y2)
  
  def distance(self): # 두점간의 거리를 구하는 function
    x1, y1 = self.coor1 # x1, y1 값을 정의
    x2, y2 = self.coor2 # x2, y2 값을 정의
  
  return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2, y1),2))
  
  def slope(self): # 두점의 경사를 구하는 function
    x1, y1 = self.coor1
    x2, y2 = self.coor2
    return float (y2 - y1) / (x2 - x1)
```

결과를 출력해보겠습니다.

1.Tuple 2 개 (두개의 점)를 생성합니다.

```python
coor1 = (3, 2)
coor2 = (8, 10)
```

2.클래스를 바탕으로 Line 오브젝트를 생성합니다.

```python
line = Line(coor1, coor2)
```

3.두점간의 경사를 계산합니다.

```python
line.slope()
```

결과 >> 1.6

4.두점간의 거리 계산하기

```python
line.distance()
```

결과 >> 9.433981132056603
