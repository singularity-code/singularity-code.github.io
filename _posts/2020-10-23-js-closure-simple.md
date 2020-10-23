---
title: "자바스크립트 간단한 클로저 예시"
date: 2020-10-23 16:34:00 -0400
categories: js simple closure sample
---

클로저(Closure)를 응용한 간단한 예제입니다.

```js
function interviewquestion(job) {
  let jobQuestion = "";
  if(job === 'designer') {
    jobQuestion = ', UX에 대해 설명할 수 있나요?';
  } else if(job === 'teacher') {
    jobQuestion = ', 무슨 과목을 가르치 시나요?';
  } else {
    jobQuestion = ', 무슨 일을 하십니까??';
  }
  return function(name) {
    console.log(name + jobQuestion);
  }
}
```

실행 코드

```js
var designerQuestion = interviewquestion('designer');
designerQuestion('길동');

// 길동, UX에 대해 설명할 수 있나요?

interviewquestion('teacher')('아무');
// 아무, 무슨 과목을 가르치 시나요?
```

함수 `interviewquestion(job)` 은 `function(name)`를 반환합니다.
이때 jobQuestion 값에 대해서는 밖에서 접근이 불가능합니다. 이것이 `Closure`를 이용한것인데
오직 내부함수 `function(name)`에서만 접근이 가능합니다.

두번째로 실행한 `interviewquestion` 에서는 `interviewquestion('teacher')`로 함수가 실행되고 다시 `('아무')`값을 받아 반환된 함수가 실행되었습니다.

만약 함수를 반환하지 않았다면 에러가 납니다.

```js
function interviewquestion2(job) {
  let jobQuestion = '';
  if (job === 'designer') {
  jobQuestion = ', UX에 대해 설명할 수 있나요?';
  } else if (job === 'teacher') {
  jobQuestion = ', 무슨 과목을 가르치 시나요?';
  } else {
    jobQuestion = ', 무슨 일을 하십니까??';
  }
  return;
  console.log(name + jobQuestion);
}

interviewquestion2('teacher')('아무');

// TypeError: interviewquestion2(...) is not a function
```

간단한 예제로 클로저(Closure)가 캡슐화(Encapsulation)를 한다는 것을 살펴보았습니다.
