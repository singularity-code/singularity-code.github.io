---
title: "[자바스크립트] Array 마지막 자르기 (Javascript Cut last element of an Array)"
date: 2020-10-05 21:00:00 -0400
categories: js array cut
---

자바스크립트 Array 에서 마지막 Element 를 자르는 방법입니다.

##### pop()

배열에서 마지막 요소를 제거하고 해당 요소를 반환합니다. 이 방법은 배열의 길이를 변경합니다.

```js
var array = [];
array.slice(-1).pop();
```

---

##### splice()

기존 요소를 제거하거나 교체하거나 새로운 요소를 해당자리에 추가하여 배열의 내용을 변경합니다.

```js
arr.splice(index[, deleteCount, elem1, …, elemN]);
```

```js
var array = [1,2,3,4,5]
array.splice(array.indexOf(2), 1); // from index 2 remove 1 element
```

---

### 스펙정의

pop()

**`arrName.pop()`**

반환값(return)

배열에서 제거 된 요소입니다. 배열이 비어 있으면 정의되지 않습니다

---

splice()

**`let arrDeletedItems = array.splice(start[, deleteCount[, item1[, item2[, ...]]]])`**

매개 변수(parameters)

`start`

배열 변경을 시작할 인덱스입니다.
배열의 길이보다 크면 start는 배열의 길이로 설정됩니다. 이 경우 요소는 삭제되지 않지만 메서드는 제공된 item[n *]만큼 요소를 추가하는 추가 기능으로 동작합니다.
음수이면 배열 끝에서 많은 요소를 시작합니다. (이 경우 원점 -1, 즉 -n은 마지막 n 번째 요소의 인덱스이므로 array.length-n의 인덱스와 동일합니다.) array.length + start가 0보다 작으면 인덱스 0에서 시작합니다.

`deleteCount (Optional)`

처음부터 제거 할 배열의 요소 수를 나타내는 정수입니다.
deleteCount가 생략되거나 해당 값이 array.length보다 크거나 같은 경우-start (즉, 시작에서 시작하여 배열에 남아있는 요소의 수보다 크거나 같은 경우), 모든 요소 어레이의 시작부터 끝까지 삭제됩니다.

**IE8에서는 deleteCount가 생략 되어도 모두 삭제되지 않습니다.**

deleteCount가 0이거나 음수이면 요소가 제거되지 않습니다. 이 경우 하나 이상의 새 요소를 지정해야합니다.

`item1, item2, ... Optional`

처음부터 배열에 추가 할 요소입니다. 요소를 지정하지 않으면 splice()는 배열에서 요소 만 제거합니다.

반환값(return)

삭제 된 요소를 포함하는 배열을 반환합니다.
하나의 요소 만 제거되면 한 요소의 배열이 반환됩니다.
제거 된 요소가 없으면 빈 배열이 반환됩니다.
