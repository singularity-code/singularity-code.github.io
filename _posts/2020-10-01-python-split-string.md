---
title: "Python 문자열 나누기,분할,자르기 String split"
date: 2020-10-01 10:34:00 -0400
categories: python string split
---

문자열 해당문자를 기준으로 자르는(나누는) 방법입니다.

---

1. split()

```python
w = 'tommorowtommorowtommorowtommorw'
w.split('o')
```

![pic1](https://dongyeopblog.files.wordpress.com/2016/07/12317.png)

---

2. partition()

```python
w = 'tommorowtommorowtommorowtommorw'
w.partition('o')
```

![pic2](https://dongyeopblog.files.wordpress.com/2016/07/12318.png)

첫번째 경우는 ‘o’를 기준으로 앞과 뒤로 나눈것이고
두번째 경우는 ‘ro’를 기준으로 나눈 경우입니다.

split과 partition의 다른점은 split은 문자열 전부 해당 기준으로 잘라서 배열(array)를 반환하고
partition은 첫번째 조건이 발견되었을시 그것을 기준으로 나눈뒤 값들을 튜플(tuple)을 반환합니다.

---

스펙정의

##### `string.split(s[, sep[, maxsplit]])`

문자열 s의 단어 목록을 반환합니다. 선택적 두 번째 인수 sep가 없거나 None이면 단어는 공백 문자 (공백, 탭, 줄 바꿈, 리턴, 폼 피드)의 임의 문자열로 구분됩니다. 두 번째 인수 sep가 있고 None이 아닌 경우 단어 구분 기호로 사용할 문자열을 지정합니다. 반환 된 목록은 문자열에서 겹치지 않는 구분 기호 발생 수보다 하나 더 많은 항목을 갖습니다. maxsplit이 주어지면 최대 maxsplit 수의 분할이 발생하고 나머지 문자열은 목록의 마지막 요소로 반환됩니다 (따라서 목록에는 최대 maxsplit + 1 요소가 있음). maxsplit이 지정되지 않았거나 -1이면 분할 수에 제한이 없습니다 (가능한 모든 분할이 수행됨).

빈 문자열에 대한 분할 동작은 sep의 값에 따라 다릅니다. sep를 지정하지 않거나 None으로 지정하면 결과는 빈 목록이됩니다. sep가 임의의 문자열로 지정되면 결과는 빈 문자열 인 하나의 요소를 포함하는 목록이됩니다.

##### `str.partition(sep)`

sep의 첫번째 문자열을 분할하고 구분 기호 앞 부분, 구분 기호 자체, 구분 기호 뒤 부분을 포함하는 3-튜플을 반환합니다. 구분 기호를 찾을 수없는 경우 문자열 자체를 포함하는 3-튜플을 반환 한 다음 두 개의 빈 문자열을 반환합니다.
