---
title: "자바스크립트 랜덤 문자열 생성 (Generate Random String)"
date: 2020-09-23 10:34:00 -0400
categories: python
---

Math.random()을 사용해서 임의의 문자열을 만들어내는 방법입니다.
bit는 8, 16, 32 로 넣어주시면 됩니다.

Code

```js
function generateString(bit) {
	const random_str = Math.random().toString(bit).substring(2, 15) + Math.random().toString(bit).substring(2, 15);
	return random_str;
}

// 2 Bit
console.log(generateString(2));

// 32 Bit
console.log(generateString(32));
```

Run

![picture](https://github-io-dblog.s3-ap-southeast-2.amazonaws.com/js-string-random.png)