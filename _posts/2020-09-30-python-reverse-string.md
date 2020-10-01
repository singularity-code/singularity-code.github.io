---
title: "Python 문자열 뒤집기(Reverse String)"
date: 2020-09-30 09:34:00 -0400
categories: python string reverse
---

파이썬에서 문자열을 거꾸로 만드는 방법입니다.

##### 문자열을 하나씩, 반대로 잘라서 다시 입력시킨후 출력하는방법

```python
s = 'Reverse this strings'
s = [::-1]
print s
```

실행화면
![pic1](https://dongyeopblog.files.wordpress.com/2016/11/screen-shot-2016-11-25-at-2-01-52-am.png)

---

##### Reverse()를 이용하는 방법

```python
s = 'Reverse this strings'
print ''.join(reversed(s))
```

실행화면
![pic1](https://dongyeopblog.files.wordpress.com/2016/11/screen-shot-2016-11-25-at-2-04-30-am.png)

---

##### 파이썬적인 코드

```python
print 'Reverse this strings'[::-1]
```

실행화면
![pic2](https://dongyeopblog.files.wordpress.com/2016/11/screen-shot-2016-11-25-at-2-07-33-am.png)
