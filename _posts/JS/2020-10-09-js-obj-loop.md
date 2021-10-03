---
title: "자바스크립트 객체 반복문 (Loop through an Object)"
date: 2020-10-09 09:34:00 -0400
categories: js object loop
---

Object.entries()를 사용해서 Object의 `key` `value`을 반복문으로 적용하는 방법입니다.

```js
let user = {
  name : "Name",
  addr : "Address"
};

for (const [key, value] of Object.entries(user)) {
  console.log(`${key} : ${value}`);
}
```

##### 스펙정의

**`Object.entries(obj)`**

Object.entries () 메서드는 for ... in 루프에서 제공하는 것과 동일한 순서로 지정된 객체의 고유 한 열거 가능한 문자열 키 속성 [키, 값] 쌍의 배열을 반환합니다. (유일한 중요한 차이점은 for ... in 루프가 프로토 타입 체인의 속성도 열거한다는 것입니다).

Object.entries ()가 반환하는 배열의 순서는 객체가 정의 된 방식에 의존하지 않습니다. 특정 순서가 필요한 경우 Object.entries (obj) .sort ((a, b) => b [0] .localeCompare (a [0]));처럼 배열을 먼저 정렬해야합니다.

##### 매개변수

`obj` - 열거 가능한 문자열 키 속성 [키, 값] 쌍이 반환되는 개체입니다.

##### 반환값

주어진 객체의 고유 열거 가능한 문자열 키 속성 [키, 값] 쌍의 배열입니다.
