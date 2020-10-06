---
title: "[자바스크립트] Set 탐색하기/반복문 (Javascript Set Iteration)"
date: 2020-10-06 10:34:00 -0400
categories: js set iteration
---

임의의 Set Object 를 생성해서 데이터를 넣겠습니다.

```js
let set = new Set();

set.add(10);
set.add(1);
set.add(9);
set.add(6);
set.add('test text');
set.add({
  a: 1,
  b: 2,
});
let car = {
  a: 1,
  b: 2,
};
set.add(car);
set.add({
  a: 3,
  b: 4,
});
```

기본적인 반복문

```js
// 기본 반복문
for (let item of set) {
  console.log('TEST 1', item);
}

// forEach()를 사용한 반복문
set.forEach(function (value) {
  if (value === 9) {
    console.log('TEST 2 forEach does not stop');
    return false; // 반환해도 해당 element 의 function이 반복되었기 때문에 중단되지 않습니다
  }
  console.log('TEST 2', value);
});
```

Set 의 메서드를 사용한 반복문

```js
// Set 에서 keys()는 values()와 같습니다.
for (let item of set.keys()) {
  if (item === 9) {
    console.log('TEST 3: ', item);
  }
}

// Set 에서 values()는 keys()와 같습니다.
for (let item of set.values()) {
  if (item === car) {
    console.log('TEST 4: ', item);
  }
}

// Set 에 추가한 순서대로 반환됩니다.
for (let [key, value] of set.entries()) {
  if (key === value) {
    console.log('TEST 5', key);
  }
}
```

참고 [ECMAScript® 2021 Language Specification](https://tc39.es/ecma262/#sec-set-objects)
