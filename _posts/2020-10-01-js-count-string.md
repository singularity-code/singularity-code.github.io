---
title: "자바스크립트 문자열에서 단어세기 (JS count letter in a string)"
date: 2020-09-23 10:48:00 -0400
categories: js string count
---

String.match() 와 정규표현식을 사용해서 특정문자가 string 문자열에 몇번 포함하는지 세는방법입니다.


```js
const a = 'ablaijclwiejc'
const reg = /j/g;
let result = a.match(reg);
console.log(result)
console.log(result.length)

// regexp 없이사용
console.log(a.match())
```

스펙정의

**`str.match(regexp)`**

`regexp`
정규식 객체입니다. regexp가 비정규식 객체일경우 new RegExp(regexp)를 사용하여 RegExp로 변환합니다.
매개변수 없이 match()를 사용하면 빈 문자열 [""]이 포함된 배열을 반환합니다.
