it's better to check their website as there're more positions there.

Tell us about one of the most interesting technical challenges you’ve had to solve. How did you go about it and what was the outcome?

What is the latest technology that you learned, what inspired you to learn it, and how was it useful?

https://github.com/JaeYeopHan/Interview_Question_for_Beginner

immediately-invoked function expression

```js
// IIFE를 사용하면
// i is not defined가 뜬다.
(function() {
  // var 변수는 여기까지 hoisting이 된다.
  for(var i=0; i<10; i++) {
    console.log('i', i)
  }
})()
console.log('after loop i is', i) // ReferenceError: i is not defined

// var i 전역변수화 됨 IIFE
(function() {
  for(i=0; i<10; i++) {
    console.log('i', i)
  }
})()
console.log('after loop i is', i) // after loop i is 10

// 'use strict' i is not defined라는 에러가 발생한다.
(function() {
  'use strict'
  for(i=0; i<10; i++) {
    console.log('i', i)
  }
})()
console.log('after loop i is', i) // ReferenceError: i is not defined
```

Temporal Dead Zone(TDZ)
const와 let은 범위가 지정된 변수를 갖는다.
이 둘의 호이스팅이 실행 되기전 까지 액세스 할수 없는 것을 TDZ라 한다.
즉, let/const선언 변수는 호이스팅되지 않는 것이 아니다. 스코프에 진입할 때 변수가 만들어지고 TDZ(Temporal Dead Zone)가 생성되지만, 코드 실행이 변수가 실제 있는 위치에 도달할 때까지 액세스할 수 없는 것이다. let/const변수가 선언된 시점에서 제어흐름은 TDZ를 떠난 상태가 되며, 변수를 사용할 수 있게 된다.

NodeJS란
크롬 V8 JavaScript 엔진으로 빌드된 JS Runtime
Node.js 라이브러리 내의 API는 모두 비동기
단일 쓰레드 모델을 사용하고, 이벤트 메커니즘을 통해 서버가 멈추지 않고 반응할 수 있어 확장성을 키워줍니다.
그리고 Chrome의 V8 JavaScript 엔진을 사용하여 빠른 코드 실행을 제공하며, 버퍼링이 없습니다.
데이터를 실시간으로 다루는 애플리케이션이나 싱글페이지 애플리케이션(SPA), 입출력이 잦은 애플리케이션을 개발할 때 뛰어난 효율성을 발휘합니다.
싱글 쓰레드 모델이기 때문에 하나의 작업 자체가 시간이 많이 걸리면 전체 시스템의 성능이 아주 급격하게 나빠지므로 CPU 사용률이 높은 애플리케이션에선 Node.js 사용을 권장하지 않습니다.

foreach()와 map()함수의 차이점
.foreach()
값을 반환 하지 않는다.
각 요소에 대해 콜백을 실행합니다.(현재 배열을 변경해서 반환)

.map()
값을 반환 한다.
각 요소에서 함수를 호출하여 결과로 새 배열을 작성하여 각 요소를 새 요소에 매핑합니다.

Speed = $.each < map < filter < forEach < reduce < for loop

Closure
`A closure is the combination of a function and the lexical environment within which that function was declared.`
클로저는 함수와 그 함수가 선언됐을 때의 렉시컬 환경(Lexical environment)과의 조합이다. -MDN-
위 정의에서 말하는 “함수” 란 반환된 내부함수를 의미하고 “그 함수가 선언될 때의 렉시컬 환경(Lexical environment)”란 내부 함수가 선언됐을 때의 스코프를 의미한다.
즉, 클로저는 반환된 내부함수가 자신이 선언됐을 때의 환경(Lexical environment)인 스코프를 기억하여 자신이 선언됐을 때의 환경(스코프) 밖에서 호출되어도 그 환경(스코프)에 접근할 수 있는 함수를 말한다.

1. Virtual DOM은 무엇인가요?
Virtual DOM is replication of HTML DOM Elements in the memory.
When Component is re rendered, 
Virtual DOM은 애플리케이션의 UI를 구성하는 HTML 엘리먼트를 메모리 내에서 구현한 것입니다. 컴포넌트가 다시 렌더링될 때, virtual DOM은 업데이트할 요소의 목록을 만들기 위해 기존의 DOM 모델에서 변경되는 사항을 비교합니다. DOM 전체를 다시 렌더링할 필요 없이 실제 DOM에 필요한 최소한만 변경하여 효율성이 높다는 것이 큰 장점입니다.

2. JSX는 무엇인가요?
JSX는 HTML처럼 보이는 코드를 작성할 수 있게 해주는 자바스크립트 문법의 확장입니다. JSX는 자바스크립트 함수 호출 방식으로 컴파일되어 컴포넌트에 대한 마크업을 만들 수 있는 더 좋은 방법을 제공합니다.

3. 클래스 컴포넌트와 함수형 컴포넌트의 차이는 무엇인가요?
React 16.8(hooks 도입) 이전에는 내부 state를 유지하는 데 필요한 컴포넌트를 생성하거나 생명주기 메소드(lifecycle methods)(즉, componentDidMount 및 shouldComponentUpdate)를 활용하기 위해 클래스 기반 컴포넌트를 사용했습니다. 클래스 기반 컴포넌트는 리액트의 Component 클래스를 확장하는 ES6 클래스입니다. 또한 최소한 render() 메서드를 포함해야 합니다.

4. key는 어떻게 사용되나요?
리액트에서 collection을 렌더링할 때 엘리먼트와 데이터 사이의 관계를 추적하기 쉽도록 반복되는 각 엘리먼트에 key를 추가하는 것이 중요합니다. 키는 고유한 ID(이상적으로는 UUID 또는 기타 고유 문자열)를 사용해야 하지만, 마지막 수단으로 Array index가 될 수 있습니다.

5. state와 props의 차이는 무엇인가요?
props는 부모 컴포넌트에서 자식 컴포넌트로 전달되는 데이터입니다. props는 수정될 수 없으며 표시되거나 다른 값을 계산하는데만 사용됩니다. state는 컴포넌트의 생명 주기 동안 수정될 수 있는 내부 데이터로, 다시 렌더링해도 유지됩니다.

6. 왜 state를 직접 변경하지 않고 setState를 이용하나요?
만약 컴포넌트의 state를 직접 변경하려고 시도한다면, 리액트는 컴포넌트를 다시 렌더링해야 하는지 알 수 있는 방법이 없습니다. setState() 메소드를 사용하면 리액트는 컴포넌트의 UI를 업데이트할 수 있습니다.

9. React context는 무엇인가요?
리액트는 하나의 앱 안에서 복수의 컴포넌트들이 state를 공유할 때 발생하는 문제들을 해결하기 위해 context API를 제공합니다. context가 도입되기 전에는 Redex와 같은 별도의 상태 관리 라이브러리를 가져오는 것이 유일한 방법이었습니다. 그러나 많은 개발자들은 (특히 작은 앱에서) Redux가 불필요한 복잡성을 유발한다고 느꼈습니다.

10. Redux는 무엇인가요?
Redux는 React를 위한 써드파티 state 관리 라이브러리로, context API가 개발되기 전부터 존재했습니다. Redux는 store라고 불리는 state 컨테이너의 개념을 기반으로 하는데, store 컴포넌트는 데이터를 props로 받을 수 있습니다. store를 업데이트하는 유일한 방법은 reducer를 통해 전달되는 store에 action을 보내는 것입니다. reducer는 action과 현재의 state를 받고, 새로운 state를 반환(return)하고, 구독된(subscribed) 컴포넌트를 다시 렌더링하게 만듭니다.

11. React 애플리케이션을 스타일링(styling)하는 보편적인 방식은 무엇인가요?
인라인 스타일링(Inline styling) : 프로토타입을 만들 때 훌륭하지만 한계가 많습니다 (예로, pseudo-classes를 사용할 수 없습니다)
클래스 기반 CSS 스타일 : 인라인 스타일링보다 유용하고 React에 익수하지 않은 개발자들도 쉽게 사용할 수 있습니다.
CSS in JS 스타일링 : 컴포넌트 안에서 스타일을 자바스크립트로 선언하여 스타일링할 수 있게 해주는 많은 라이브러리가 있습니다.

12. 제어 컴포넌트와 비제어 컴포넌트의 차이는 무엇인가요?
HTML 문서에서 많은 form 엘리먼트들(<select>, <textarea>, <input> 등)은 고유한 state를 유지합니다. 비제어 컴포넌트는 DOM을 이러한 input들의 state에 대한 진짜 근원(source of truth for the state of these inputs)으로 취급합니다. 제어 컴포넌트에서 내부 state는 엘리먼트의 값(value)를 추적하기 위해 사용됩니다. input의 값이 변경되면 리액트는 input을 다시 렌더링합니다. 비제어 컴포넌트는 non-React 코드와 합칠 때(예를 들어 jQuery 플러그인의 일부를 지원해야 할 때) 유용하게 사용될 수 있습니다.

13. 생명주기(lifecycle) 메소드는 무엇인가요?
클래스 기반 컴포넌트는 그들이 mount(DOM에 렌더링)되었을 때, unmount될 때 등과 같이 그들의 생명주기 중 특정한 시점에 호출되는 특별한 메소드를 선언할 수 있습니다. 이는 예를 들면 컴포넌트가 필요로 하는 것을 셋팅 및 해제하거나, 타이머를 설정하거나 브라우저 이벤트에 바인딩하는 데 유용합니다.

아래의 생명주기 메소드들은 컴포넌트를 불러오기 위해 사용할 수 있습니다.

14. React hooks는 무엇인가요?
Hooks는 클래스 기반 컴포넌트의 장점(예를 들면 내부 state와 생명주기 메소드)을 함수형 컴포넌트로 가져오려는 리액트의 시도입니다.

15. React hooks의 장점은 무엇인가요?
클래스 기반 컴포넌트, lifecycle hooks, this의 필요성이 사라집니다
공통 기능을 커스텀 hook로 만들어서 로직을 재사용하기 쉬워집니다.
컴포넌트 자체에서 로직을 분리할 수 있어서 읽기 쉽고 테스트하기 쉬운 코드를 작성할 수 있습니다.
