---
title: "Python 문자열에서 특정문자 카운트하는법"
date: 2020-09-28 10:23:00 -0400
categories: python string count
---

문자열(String)에서 해당문자가 몇번 존재하는지 카운트하는 방법입니다.

```python
w = 'You can count me how many times, more and more'
w.count('o')
```

![pic1](https://dongyeopblog.files.wordpress.com/2016/07/1238.png)

해당문자열에 o 가 몇번 반복되었는지 count 메서드 사용결과 5번 반복됨을 알수있습니다.

```python
w.count('z')
```

![pic2](https://dongyeopblog.files.wordpress.com/2016/07/1239.png)

하지만 z 의 경우 한번도 해당되지 않으므로 0이 반환됩니다.

```python
w.count('more')
```

![pic3](https://dongyeopblog.files.wordpress.com/2016/07/12310.png)

문자만이 아니라 단어 'more' 를 카운트해보면 2 (2번 반복되었음)를 반환합니다.
