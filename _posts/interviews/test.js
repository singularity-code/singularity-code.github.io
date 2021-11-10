(function test() {
  // var 변수는 여기까지 hoisting이 된다.
  for (var i = 0; i < 10; i++) {
    console.log("i", i);
  }
})();
// ReferenceError: i is not defined
console.log("after loop i is", i);

(function test() {
  for (i = 0; i < 10; i++) {
    console.log("i", i);
  }
})();
// after loop i is 10
console.log("after loop i is", i);

// 'use strict' i is not defined라는 에러가 발생한다.
(function test() {
  "use strict";
  for (i = 0; i < 10; i++) {
    console.log("i", i);
  }
})();
console.log("after loop i is", i);
