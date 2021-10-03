---
title: "자바스크립트 고정 소수점 표기법 (JS fixed float number)"
date: 2020-10-07 16:34:00 -0400
categories: js number tofixed
---

숫자를 표현할때 0.39234 같은경우 0.39 두번째 자리까지 끊고 싶을때가 있죠.
이럴때 `.toFixed(digits)`로 표현할 수 있습니다.

```js
var num = 5.56789293847;

var test1 = Number.parseFloat(num).toFixed(2);
console.log(test1); // 5.57

var test2 = Number.parseFloat(num).toFixed(4);
console.log(test2); // 5.5679

var test3 = Number.parseFloat(num).toFixed();
console.log(test3); // 6 소수점 첫째자리에서 반올림되었습니다.

var test4 = (1000000000000000128).toString(); // toString은 인접한 숫자 값과 숫자를 구별하기에 충분한 유효 자릿수 만 반환합니다.
console.log(test4); // 1000000000000000100

var test5 = (1000000000000000128).toFixed(0); // toFixed의 출력은 일부 값에 대해 toString보다 더 정확합니다.
console.log(test5); // 1000000000000000128

var test6 = num.toFixed(100);
console.log(test6); // 5.5678929384699999971530814946163445711135864257812500000000000000000000000000000000000000000000000000

var test7 = num.toFixed(101);
console.log(test7); // RangeError: toFixed() digits argument must be between 0 and 100

```

##### 스펙정의

**`numObj.toFixed([digits])`**

toFixed()는 지수 표기법을 사용하지 않고 소수점 이하 자릿수를 가진 numObj의 문자열 표현을 반환합니다. 숫자는 필요한 경우 반올림되고 필요한 경우 분수 부분은 지정된 길이를 갖도록 0으로 채워집니다. numObj의 절대 값이 1e + 21보다 크거나 같으면이 메서드는 단순히 Number.prototype.toString()을 호출하고 지수 표기법으로 문자열을 반환합니다.

##### 매개변수

`digits` (선택사항)

소수점 뒤에 표시 할 자릿수입니다. 이것은 0과 20 사이의 값일 수 있으며, 구현은 선택적으로 더 큰 범위의 값을 지원할 수 있습니다. 필수가 아니기 때문에 이 인수를 생략하면 0으로 처리됩니다.

##### 반환값

고정 소수점 표기법을 사용하여 주어진 숫자를 나타내는 문자열.

##### 예외처리

`RangeError`

숫자가 너무 작거나 큰 경우. 0에서 100 사이의 값은 RangeError를 일으키지 않습니다. 구현체는 더 크고 작은 값을 지원할 수 있습니다.

`TypeError`

이 메서드가 숫자가 아닌 개체에서 호출되는 경우.

참고 [ECMAScript® 2021 Language Specification - 20.1.3.3 Number.prototype.toFixed ( fractionDigits )](https://tc39.es/ecma262/#sec-properties-of-the-number-constructor)
