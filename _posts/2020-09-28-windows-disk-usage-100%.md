---
title: "윈도우 10 디스크 100 문제 (Windows 10 Disk Usage 100%)"
date: 2020-09-28 10:14:00 -0400
categories: windows disk100% disk usage superfetch 윈도우즈 디스크100
---
***DB블로그 같은내용이며 이전중입니다***

2년전 처음 이 글을 작성할때는 디스크100 문제가 해결되어서 향후에는
이 글이 “필요없게” 되었으면 좋겠다는 생각이었는데요.
안타깝게도 아직은 아니지만 언젠가 그런날이 오길 기대해 봅니다.

> Windows 10 초기화 후 진행된 작업으로, 개인마다 컴퓨터의 상황과 설치된 프로그램이 다름에 따라서 다음방법을 이용해도 효과는 다를 수 있음을 미리 알려드립니다.

Windows 10 의 고질적인 문제로 작업관리자(Task Manager)에 들어가보면
디스크 사용이 항상 100%인 것인데요.

상식적으로 생각해봐도 이것은 컴퓨터에 좋을것이 하나도 없습니다.
프로그램을 돌려야하는데 디스크는 항상 100% 읽는 중이다?
더욱이 디스크가 SSD라면 이것은 디스크수명을 갉아먹는 치명적인 현상일것입니다.

온라인상에 많은 글과 동영상이 있지만 제가 살펴본결과,
상황은 사용자마다 다르기 때문에 할 수 있는건 다 적용해 보는것이 좋습니다.

중요한것은, 원인을 모르고 접근하면 3~6개월 후 디스크 100문제는 다시 찾아온다는 것이죠.

첫번째로 윈도우10이 태블릿과 데스크탑의 통합을 지향하기 때문에 쓸데없는 테블릿 옵션을 꺼주는것에 중점을… (결과적으로 이 방법은 윈도우 OS 효율을 약간 높여줍니다)

두번째로 윈도우10의 문제를 일으키는 3가지 서비스를 강제종료시키고 다시 자동으로 실행되지 않게하는 방법을 추천하고 있습니다. (결과적으로 이 방법은 디스크문제를 해결합니다)

저는 여기서 두가지 방법을 함께 적용해서 윈도우10 디스크 문제를 해결하고 추가대안을 제시해 보겠습니다.

> 2017년 10월기준작성된 글로, 현재는 다음과 같은 방법을 시도해볼 수 있습니다.
(Windows 10 Pro version 1609 환경에서 작성되었습니다)

#### 기본적인 방법 (Software 관점에서 해결)

각 스텝마다 적용한후 작업관리자를 보면서 디스크사용률이 떨어지는지 확인해보면서 작업하면 됩니다.
(효과가 없는데 찜찜하시면 되돌리면 되겠죠?)

    1. Desktop에 필요없는 옵션 전부끄기
    2. 디스크활성화 100%를 발생시키는 3가지 서비스 강제종료
    3. 상주하는 프로그램들의 삭제
    4. 하드디스크 포맷 후 OS 재설치 (이후 2번 역시 검토해 주는편이 좋습니다)

#### 최후의 방법 (Hardware 관점에서 해결)

    1. HDD -> SSD 업그레이드

첫번째 방법부터 알아보겟습니다.

#### 1.Desktop에 필요없는 옵션 전부끄기

윈도우즈10은 태블릿과 통합환경을 지향하는 덕분에 일반PC 에서는 사용하지 않을 쓸데없는(?) 모드들이 들어있습니다. 문제는 이것들이 기본적으로 켜져있다는것.
일반,카메라,알림 등 항목들에서 태블릿PC에 필요한 옵션들이 있습니다.
코타나음성서비스를 포함해서요.

아주 쉽게 할수있는 조치로 태블릿모드에 필요한 설정을 모조리 꺼줍니다. (필요하면 다시 활성화하면 됩니다)

    1.윈도우즈 시작 -> 설정

![disk1](https://dongyeopblog.files.wordpress.com/2016/12/disk1_1.png)

    2. 설정 -> 개인정보 탭에서 켜짐으로된 항목들중 불필요한것들을 모두 비활성화합니다.

![disk2](https://dongyeopblog.files.wordpress.com/2016/12/s1.png)
![disk3](https://dongyeopblog.files.wordpress.com/2016/12/disk1_21.png)

> 모든 항목을 보여드리기엔 글이 너무 길어지는 관계로 생략하겠습니다. 카메라,마이크,알림,통화기록(?) 살펴보시면 데스크탑에 거의 쓸데없는 옵션들입니다.
>2019 Update: 현재 배포되고 있는 Windows 10 Redstone5 에서는 이 항목들이 많이 늘어서 스크린샷과 다를수 있습니다. 쓸데없는 항목은 비활성화해주시는게 좋겠습니다)

#### 2.디스크활성화 100%를 발생시키는 서비스 3가지 설정변경

두번째 방법은 다음 3가지 서비스설정을 바꿔줌으로써 큰 효과를 볼수있습니다.

    1. 윈도우즈키 + R (Windows Key + R)로 실행창을 연다.

    2. 서비스 매니저 실행

![disk4](https://dongyeopblog.files.wordpress.com/2016/12/disk2_1.png)

#### 3.다음 3가지 서비스 항목을 사용안함 상태로 바꾸어 줍니다

초보에게는 “잘못되면 망하는거 아니야?” 라고 생각이 드실수도 있지만 모든항목이 무슨기능을 하는지는 해당메뉴 **왼쪽에 자세한 설명** 이 포함되니 참고하시면 됩니다.

***Background Intelligent Transfer Service***: 백그라운드에서 파일을 전송한다는 내용입니다. 이것을 끄게되면 프로그램및 기타정보를 자동으로 “다운로드”할수없다는데… 윈도우즈 업데이트등이 해당됩니다. 수동으로 받는편을 택하는 것입니다.

***Sysmain(Superfetch)*** 가장 문제되는 부분이라고들 합니다. 윈도우즈 성능을 향상시키기위해서 사용자패턴을 인식해서 프로그램을 미리 로드하는 기능인데 오히려 체감속도는 저하된다는게 일반적인 의견입니다.

> 2019 Update : Lodi 님이 댓글에 알려주신 내용으로 2018 년 10월 윈도우즈 업데이트에서 Superfetch는 Sysmain으로 변경되었습니다. Sysmain 과 Superfetch는 이름만 변경되었을뿐, 정확히 같습니다.

***Windows Search***: 윈도우즈 검색결과를 제공합니다.

***Connected User Experiences and Telemetry***:  윈도우 시스템 이력정보를 수집해서 전송합니다. 이것을 Disable 함으로써 시스템에 불필요한 프로세스를 줄이는 효과가 있는것으로 생각됩니다. 프라이버시 이슈와도 관련이 있습니다. 관련내용과 중지하는방법은 다음분이 잘 정리해놓으셨기때문에 참고하시면 좋을듯 하네요.

[홍차의꿈 – MS가 수집한다는 ‘윈도10 텔레메트리(Telemetry)’,뭘까?](http://jsb000.tistory.com/493)

![disk5](https://dongyeopblog.files.wordpress.com/2016/12/disk2_2.png)
![disk6](https://dongyeopblog.files.wordpress.com/2016/12/disk2_3.png)
![disk7](https://dongyeopblog.files.wordpress.com/2016/12/disk2_4.png)

> Lodi 님이 알려주신 내용으로 Windows 2018 Oct Update 이후 버전은 Superfetch가 Sysmain라는 이름으로 존재합니다.

![disk8](https://dongyeopblog.files.wordpress.com/2016/12/1-3.jpg)

    위의 3가지 항목에 대해서 개별적으로 마우스 우클릭 -> 속성

![disk9](https://dongyeopblog.files.wordpress.com/2016/12/d_5.png)

    시작유형에서 “사용 안함” 으로 바꾸어준후 확인.

![disk10](https://dongyeopblog.files.wordpress.com/2016/12/disk2_6.png)

    위의 3가지 항목을 사용안함으로 바꾼후 창을 닫으면 시스템을 재시작할건지 묻는데
    그전에 다음과 같이 레지스트리 에디터를 열어 자동으로 다시 실행할수없게 확실히 바꾸어줍니다.

    1) 윈도우키 + R -> regedit
![disk11](https://dongyeopblog.files.wordpress.com/2016/12/disk3_1.png)

    아래경로로 따라가시거나,
    Regedit 편집기에 다음 텍스트를 복사/붙이기 하시면 해당 경로로 이동합니다.
    Windows 빌드 1904 에서는 ControlSet001 항목으로 변경되어 있습니다

```bash
Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters
```

또는

```bash
Computer\HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Session Manager\Memory Management\PrefetchParameters
```

![disk12](https://dongyeopblog.files.wordpress.com/2016/12/disk3_2.png)

        항목에 도착하시면 EnablePrefetcher와 EnableSuperfetch가 보입니다.

![disk13](https://dongyeopblog.files.wordpress.com/2016/12/disk3_3.png)

> 2019 Update 최근 업데이트 후에는 다음과 같이 Superfetch는 없이 보일 수 있습니다.
Sysmain(Superfetch)는 UI에서 비활성화 시켜주시고 EnablePrefetcher 만 진행하시면 됩니다.
Prefetcher값을 2로 바꾸어 줍니다.

![disk14](https://dongyeopblog.files.wordpress.com/2016/12/1-1.jpg)

    두항목 각각 우클릭 -> 수정

![disk15](https://dongyeopblog.files.wordpress.com/2016/12/disk3_4.png)

> 2017.04.10 Update
레지스트리관련해서 문의를 해주셔서 관련항목을 추가로 알려드립니다.

비활성화는 0을 입력해야 되는거 아닌가 하는것인데요. 관련 옵션은 다음과 같습니다.

***Sysmain (Superfetch)*** 는 1을 입력합니다.

    0 – Disable (비활성화)
    1 – Enable SuperFetch for boot files only (부트시 적용)
    2 – Enable SuperFetch for applications only (앱에만 적용)
    3 – Enable SuperFetch for both boot files and applications (앱과 부트 모두적용)

***Prefetcher*** 는 1과 2의 속성이 반대로 입니다. Prefetcher는 “2”를 입력하셔야 합니다.

    0 – Disable Prefetcher
    1 – Application launch Prefetching enabled (앱에만 적용)
    2 – Boot Prefetching enabled (부트시 적용)
    3 – Application launch and Boot Prefetching enabled (앱과 부트 모두적용)

어플리케이션에는 적용하지않지만 부트할때는 효과를 보기때문에 부팅시에만 활성화 되게합니다. 0으로 하는 경우 완전 비활성화이니 주의하세요.

다른항목이 저와 다를수있으나 해당 두 값에 대해서만 바꾸어 줍니다.

![disk16](https://dongyeopblog.files.wordpress.com/2016/12/disk3_6.png)

> 2019.01.05 Update
2019년 01월 이후 업데이트된 윈도우에서는 Superfetch 레지스트리를 여기에 포함하지 않고 있습니다.

![disk17](https://dongyeopblog.files.wordpress.com/2016/12/nosuperfetch.jpg)

자.. 그럼 골치덩이 서비스들을 꺼주엇으니 효과가 있겟죠?

시스템을 재부팅 해줍니다.

![disk18](https://dongyeopblog.files.wordpress.com/2016/12/disk10031.png)

재부팅후 작업관리자를 열어서 프로세스를 확인해보면

99%는 아니지만 어느정도 하드디스크 효율이 좋아졌을수도 아닐수도 있습니다.

프로그램이 많이 설치되지않은 나쁘지 않은 상태라면 다음과같이 50% 미만으로 줄어들었을테고

![disk19](https://dongyeopblog.files.wordpress.com/2016/12/disk1005.png)

아니라면 처음에는 40~50%시작해서 좋아지는듯 보이다가
다시 90% 육박또는 다시 100% 되는상태일수 있습니다.

![disk20](https://dongyeopblog.files.wordpress.com/2016/12/disk1006.png)

왜?! CPU나 메모리는 만족할만 수준인데 디스크는 왜 다시 사용량이 올라갈까요?

문제는, 아직도 항상구동되고있는 “백그라운드 프로세스” 수많은 서비스 또는 프로그램들 때문입니다.
(안티바이러스 프로그램이 수시로 디스크를 스캔하고 있는것도 대다수의 원인입니다)

PC를 오래 사용해였을경우, 수많은 인증프로그램과 툴바, 자동업데이트 등을 설치했을경우 내가 모르는 일들이 많이 벌어지고 있는경우죠. 이것이 세번째 방법인데 개인적으로 설치된 프로그램이 다르니 직접 하나씩 강제 종료를 하면서 작업해주어야 합니다.

일반적으로 시작프로그램은 꼭 필요한것이 아니면 깨끗히 없애 주시는것이 좋으며, Java Auto Update, Adobe Acrobat Update 등 자동 업데이트들을 강제종료한후 디스크 사용률이 줄어드는지 확인해 보시는게 좋습니다.

> 자동 업데이트등을 정지시킨다는것은 다음부터는 수동으로 업데이트 하셔야 합니다.

컴퓨터와 친하지 않은분도 계실지 모르니,
디스크 100%이 발생하는 이유에 대해 다르게 표현한다면…

빌게이츠가 사장님이고 윈도우란 직원이 있고 하드디스크를 창고라고 할때
창고안에 Java, MS오피스, 인터넷브라우저들, Adobe 소프트웨어들이 보관되어 있고
사장님이 “윈도우군, 창고에가서 이것들 상태가 어떤지 항상 체크/자동 업데이트 하도록!” 이라고 했다면,

이런경우 윈도우군의 창고 이용률은 올라가겟지요? (당연히 정상입니다)
이때 창고 = 디스크,  사용률은 100% 라고 할 수 있겠습니다.
그럼 이제 어떤 소프트웨어들이 문제일지 감이 잡히지요?

***적용한지 한달후***

최적화작업후 한달동안 모니터링한결과 저는 위와같은 방법으로 효과를 보았고 이제는 아무것도 안하면 하드디스크는 쓸데없이 동작하지 않게 되었습니다. 많은 분들이 효과를 보셔서 시스템이 무리한 작업을 하지않게 되엇으면 하는 바램이며, 낮다고 좋은것만은 아닙니다. 컴퓨터는 저희가 신경써도 되지않는 많은 일을 처리해야 하니까요.

성공적으로 하셧을 경우 대략 50% 이하의 디스크 사용률을 달성하셧다면 만족할만 수준이라고 할수있겟습니다. (일부 소프트웨어나 서비스는 필요한 분들도 있을테니..)

다음은 마지막으로 프로세스가 없을때
마우스가 움직이지 않으면 0% 로 떨어지는 디스크사용률 화면입니다.

제가 확인한건 일부 메신저, 공인인증, 보안프로그램등은 상주한다고해도 디스크 사용률에 크게 영향을 미치지 않는것으로 보이며, 최적화가 되셧다면 이후에도 설치되는 프로그램들을 잘 모니터링 하시며 의도치않은 작업을 하는것 (브라우저 툴바, 다운로더 등등)은 정기적으로 정리해주시거나 복원시점을 만들어서 사용하시면 좋을것 같네요.
> 아래 화면은 공인인증서 보안 모듈등이 설치된 상태에서도 영향이 없다는것을 보여줍니다.

![disk21](https://dongyeopblog.files.wordpress.com/2016/12/ecb59ceca081ed9994.png)

> 2017 8월 추가내용

4번째 해결방법 – 하드웨어적인 방법
디스크를 100% 사용한다는것은 어떤의미 일까요?
다른의미로는 시스템 속도를 디스크가 못따라 간다는것과 같습니다.

제가 관찰한 바로는, 새로운PC의 대부분은 디스크 100% 현상은 거의 없었습니다. (완전히 없는건 아닙니다)
하지만 우리가 PC를 사용하다보면 OS가 할일은 많아지고 설치된 프로그램들도 많아지죠.

소프트웨어적으로 해결이 안되신 분은 일반 HDD의 SSD교체도 고려해보시기 바랍니다.
(하드웨어적 해결방법 입니다)
비용은 물론 싸지는 않습니다. (2019년: 이제 저렴해졌습니다!) 하지만, 해당 문제로 PC가 느리다면 CPU, Memory 업그레이드 보다 큰 메리트가 있습니다. 현재 우리가 사용하는 PC에서
“물리적인 디스크(Hard Disk)” 라는것이 전체시스템에서 가장느린 I/O 라는것은 고려해볼 문제입니다.

또한 시스템에서 보자면 “디스크 사용률 100%”이라는 것은 “최선을 다하고 있다” 라고 생각해 볼수 있습니다.

SSD는 I/O속도가 빠르기 때문에 OS가 아무리 작업을 해도 일반하드보다는 빠릅니다.
하지만 그렇다고 디스크가 아무것도 안하는것은 아닙니다. 다음을 보시면 0% 임에도 불구하고 읽고 쓰고, 디스크는 무엇인가 계속 하고 있습니다. (저희가 체감 못할만큼 0.4~ 0.9ms)에서 끝날 뿐이죠.
정말 운이 안좋다면 SSD에서도 디스크 100% 또는 80%정도 일시 올라가는 현상이 나타날수 있지만,
거의 본적 없네요.

그렇게 되면 시스템이상, 디스크의 불량, 어떠한 앱이 프로세스를 잡고 있는지 고려해볼 문제이지요.
그럼에도 SSD는 큰 속도향상을 기대할수 있기때문에 비용이 부담되지 않는분들은 고려해보시기 바랍니다.

![disk22](https://dongyeopblog.files.wordpress.com/2016/12/ssd4.png)

> 2020 7월

5번째 추가적인 방법으로 소개해드렸던 램디스크 (RamDisk) 관련 방법은 SSD 의 보급률이 증가하고 가격이 많이 저렴해진것을 감안하여 배제해였습니다.

글이 조금 길었지만 효과가 있기를 바라면서… 행복하세요.
