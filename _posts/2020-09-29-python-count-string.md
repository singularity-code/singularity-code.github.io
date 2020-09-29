---
title: "Python 문자열에서 특정문자 카운트하는법 (Python count string)"
date: 2020-09-28 10:23:00 -0400
categories: python string count built-in
---

문자열(String)에서 해당문자가 몇번 존재하는지 카운트하는 방법입니다.

스펙 정의는 다음과 같습니다.

#### `string.count(s, sub[, start[, end]])`

***Return the number of (non-overlapping) occurrences of substring sub in string s[start:end].***
***Defaults for start and end and interpretation of negative values are the same as for slices.***

s[시작:끝] string에서 substring sub(겹치지 않는) 발생 횟수를 반환합니다.
시작 및 끝의 기본값과 음수값의 해석은 slice와 동일 합니다.

기본값은 0 index 이며 sub는 검색할 문자열입니다.

---

```python
w = 'You can count me how many times, more and more'
w.count('o')
```

![pic1](https://dongyeopblog.files.wordpress.com/2016/07/1238.png)

해당문자열에 o 가 몇번 반복되었는지 count 메서드 사용결과 5번 반복됨을 알수있습니다.

---

```python
w.count('z')
```

![pic2](https://dongyeopblog.files.wordpress.com/2016/07/1239.png)

하지만 z 의 경우 한번도 해당되지 않으므로 0이 반환됩니다.

---

```python
w.count('more')
```

![pic3](https://dongyeopblog.files.wordpress.com/2016/07/12310.png)

문자만이 아니라 단어 'more' 를 카운트해보면 2 (2번 반복되었음)를 반환합니다.
