---
title: "자바스크립트 Set (Javascript Set)"
date: 2020-10-06 09:34:00 -0400
categories: js set
---

Set 객체를 사용하면 원시 값이든 객체 참조 든 모든 유형의 고유 한 값을 저장할 수 있습니다.

`.add()` 요소 추가
`.delete()` 요소 제거
`.has()` 값이 존재하는지 확인

Set의 각 값은 고유해야하므로 값이 같은지 확인합니다. 이전 버전의 ECMAScript 사양에서는 === 연산자에 사용 된 것과 동일한 알고리즘을 기반으로하지 않았습니다. 특히 Set의 경우 +0 (완전히 -0과 동일)과 -0은 서로 다른 값이었습니다. 그러나 이것은 ECMAScript 2015 사양에서 변경되었습니다. 자세한 내용은 브라우저 호환성 표에서 "-0 및 0의 키 같음"을 참조하십시오.

NaN 및 undefined도 Set에 저장할 수 있습니다. 모든 NaN 값은 동일합니다 (즉, NaN !== NaN이지만 NaN은 NaN과 동일한 것으로 간주 됨).

```js
let set = new Set();

set.add(1);
set.add(2);
set.add(2);
console.log(set); // 2 중복이 추가되지 않았음

set.add('this is text');
console.log(set);

let obj = {
  a: 1,
  b: 2,
};
set.add(obj);
console.log(set);

set.add({
  a: 1,
  b: 2,
});
console.log(set); // obj 로 추가한것과  {a: 1, b: 2} 는 다른 오브젝트임

console.log(set.has(1)); // true
console.log(set.has(2)); // true
console.log(set.has(3)); // false
console.log(set.has(Math.sqrt(4))); // true 2라는값이 존재하기 때문에
console.log(set.has(obj)); // true

console.log(set.size); // 5

set.delete(2);
console.log(set.has(2)); // false 2값은 지워졌음

console.log(set.size); // 4
```

---

Object 테스트

```js
let set = new Set();

let Kim = { name: "Kim" };
let Lee = { name: "Lee" };
let Thom = { name: "Thom" };

// 어떤 고객(Kim, Thom)은 여러 번 방문할 수 있습니다.
set.add(Kim);
set.add(Lee);
set.add(Thom);
set.add(Kim);
set.add(Thom);

// Set 에는 유일한 값만 저장됩니다.
console.log( set.size ); // 3

set.add({
  name: 'Lee',
});

// Lee Object 는 { name: 'Lee' } 와는 다른값을 레퍼런스하기 때문에 다르다는것에 주의해야합니다.
console.log( set.size ); // 4

for (let user of set) {
  console.log(user.name); // // Kim, Lee, Thom 순으로 출력됩니다.
}
```

참고 [ECMAScript® 2021 Language Specification](https://tc39.es/ecma262/#sec-set-objects)
