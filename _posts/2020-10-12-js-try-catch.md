---
title: "자바스크립트 예외처리 (Try Catch Finally)"
date: 2020-10-12 11:34:00 -0400
categories: js object loop
---
try 문은 하나 이상의 문을 포함하는 try- 블록으로 구성됩니다. 단일 문에도 {}를 항상 사용해야합니다. 최소한 하나의 catch-block 또는 finally-block이 있어야합니다. 이것은 try 문에 대한 세 가지 형식을 제공합니다.

try-block에서 예외가 발생하지 않으면 catch-block을 건너 뜁니다.

하나 이상의 try 문을 중첩 할 수 있습니다. 내부 try 문에 catch-block이 없으면 포함하는 try 문의 catch- 블록이 대신 사용됩니다.

```js
try {
  // 이곳의 코드를 실행
} catch(err) {
  // 에러가 발생하면, 여기부터 실행됨
  // err는 에러 객체
} finally {
  // 에러 발생 여부와 상관없이 try/catch 이후에 실행됨
}
```

간단한 구문으로 테스트해보겠습니다.

```js
const a = 500;

try {
  a = 1000;
} catch (e) {
  console.log(e); // TypeError: Assignment to constant variable.
}
```

특정 발생에러를 핸들링 할수 있습니다.

```js
try {
  a = 1000;
} catch (e) {
  if (e instanceof TypeError) {
    console.log('Type error can handle here');
  } else {
    throw e; // Throw other errors
  }
}
```

finally 는 언제든 실행됩니다.

```js
try {
  a = 1000;
} catch (e) {
  if (e instanceof TypeError) {
    console.log('Type error can handle here');
  }
} finally {
  console.log('I got this anyway');
}
```

중첩해서 사용할 수 있습니다.

```js
const a = 100;
try {
  a.toString();
  try {
    a = 200;
  } catch (e) {
    if (e instanceof TypeError) {
      console.log('Error on second try');
    }
  }
} catch (e) {
  console.log(e);
} finally {
  console.log('No error on first try');
}
```


#### 스펙정의

```js
try {
  try_statements
}
[catch (exception_var) {
  catch_statements
}]
[finally {
  finally_statements
}]
```

`try_statements`  
실행할 구문입니다.

`catch_statements`
try-block에서 예외가 발생하면 실행되는 구문입니다.

`exception_var`
연관된 catch-block에 대한 예외 개체를 보유하는 식별자입니다.

`finally_statements`
try 문이 완료된 후 실행되는 구문입니다. 예외가 발생했는지 포착되었는지에 **관계없이** 실행됩니다.

[참고 MDN try...catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
