---
title: "[자바스크립트] Boolean Logic"
date: 2020-10-07 16:34:00 -0400
categories: js boolean logic
---

**&&** 모든것이 `true`이면 `true`를 반환.
**||** 언제든 첫번째로 만나는 조건에 `true`이면 `true`를 반환.
**!** (NOT) `true` `false` 값을 반전시킴.

**&&** 예시

```js
var firstName = "John";
var age = 20;

if(age < 13) {
  console.log(firstName + ' is a boy');
} else if (age >= 13 && age < 20) {
  console.log(firstName + ' is a teenager');
} else if (age >= 20 && age < 30) {
  console.log(firstName + ' is a young man');
} else {
  console.log(firstName + ' is a man');
}
```

**||** 예시

```js
if(age < 13) {
  console.log(firstName + ' is a boy');
} else if (age >= 13 || age < 20) {
  console.log(firstName + ' is a teenager');
} else if (age >= 20 || age < 30) {
  console.log(firstName + ' is a young man');
} else {
  console.log(firstName + ' is a man');
}
```

**!** 예시

```js
if(!age < 13) {
  console.log(firstName + ' is not a boy');
} else {
  console.log(firstName + ' is a boy');
}
```
