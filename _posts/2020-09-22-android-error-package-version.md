---
title: "Android 패키지 파일을 분할하는 중에 문제가 발생하였습니다."
date: 2020-09-22 10:51:28 -0400
categories: android
---
Android 앱 개발중 Release 버젼으로 .apk 파일을 생성해 모바일에 직접 설치하고싶을때

“패키지 파일을 분할하는 중에 문제가 발생하였습니다” 라는 에러가 나면서 설치되지 않는다면

APK 파일의 minSdkVersion (개발중인 안드로이버젼)이
설치되는 폰의 Android Version보다 높기때문입니다.

반대로 얘기하면, 실행하려는 폰이 개발된 앱보다 버젼이 낮기 때문입니다.

Manifest.xml 을 열어보면 최소/목표사양의 Android Version을 지정할 수 있습니다.

다음과 같은 방법을 시도해 볼 수 있습니다.

`개발중인 Minimum Android Version 을 더 낮춘다.`
`Compile, Target Android Version 을 설치할 폰과 맞춘다.`
`테스트할 폰의 Android OS를 빌드 버젼 또는 더 높게 업그레이드를 한다.`

보통의 경우 설치할폰에 설정에 들어가서 Android버젼을 먼저 확인한후
개발툴로 돌아와 개발 버젼을 폰에 맞게 맞춰주시면 대부분 해결이 가능합니다.

Android Studio에서는 AndroidManifest.xml의 <users-sdk> 항목이 해당됩니다

```xml
<users-sdk android:minSdkVersion="integer"
           android:targetSdkVersion="integer"
           android:maxSdkVersion="integer"/> 
```
안드로이드 스튜디오에서는 버젼을 번호로 입력해야합니다. 아래 표를 참고해주세요.

예를 들면 안드로이드 롤리팝 버젼(21)으로 개발했는데 폰이 허니콤(11)이면 패키지파일을 제대로 설치할수없다는 것입니다.

아래표에서 API 레벨 숫자를 써주시면 됩니다.

[Google: Codenames, Tags, and Build Numbers](https://source.android.com/setup/start/build-numbers)

`Xamarin Studio에서는 AndroidManifesto 를 UI 를 이용해 수정할 수 있습니다.`
