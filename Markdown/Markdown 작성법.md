ㅇMarkdown 작성법 (간략화)
============

> 상세 가이드는 다음 링크를 참조.
>> Markdown Guide(https://www.markdownguide.org), (https://teck10.tistory.com/256)

## 1. 큰분류,제목
- ' # '(h1, h2 같은 기능)을 써서 표현, 샵1개면 h1, 2개면 h2
- ' = ' h1에 밑줄넣어 구분함, 문서제목이나 완전큰분류로 쓰면 좋음

## 2. 작은분류, 리스트/메뉴
- ' - '(하이픈/대쉬), ' * '(아스타리스크), ' + '(플러스) 로 일반적 사용
- 문자를 번갈아가며 사용하면 여백을 주며 사용가능
* ' > '(꺽쇠), 인용문, 한줄씩 강조할때 사용하면 좋음
* 인용문 중첩 으로 안에서 리스트 사용 가능
+ ' 1. ', ' 2. ' 숫자 점으로 표현 가능
+ 순서를 넣어 리스트를 작성할때 사용

## 3. 스크립트 표현
- ' ``` ' 백틱을 써서 표현
- ' tab ' 을 써서 표현 
```
지금처럼 박스를 만들어 태그적용없는 순수 문자를 표현하는데 사용
줄바꿈, 특수문자 적용안되어 원본 소스 표시할때 좋음.
```
    tab을 써서 표현도 가능하나, 간단히 단일로 쓸 때만 추천한다.
    타 옵션과 충돌이 잘 나서 깨지지 않는지 확인하며 써야함.

## 4. 계층표현
> 계층 표현은 아래처럼 탭으로 구분해서 작성하면 된다. 
> - 숫자로 게층 표현할 땐 2단까지만 쓰는게 좋다.
> - h1, h2같은 태그와 탭으로 직접 구현도 가능하다.
  1. 가나다
     1. 밝은빛
  2. 라마나 
  3. 그림자
     1. 멋짐
     2. 균형

- 가나다
  - 밝은빛
- 라마나
- 그림자
  - 멋짐
  - 균형
    - 수호자
    - 지속

## 5. 줄바꿈과 밑줄
줄바꿈은
마크다운에서 엔터로
구분이 잘 안되며 <br> <strong>&#60;br&#62;</strong>태그를
사용하여 구분하면 된다.
*****
-----
- ' ----- ' 하이픈 여러개 또는 ' ***** '아스타리스크 여러개로 밑줄 표현

## 6. 스타일
- <em>&#60;em&#62;태그, 기울기, 이텔릭, 강조(Emphasis) </em>
- _&#95;밑줄 하나로 둘러싸면 기울기&#95;_
- <strong>&#60;strong&#62;태그, 진하게, 강하게</strong>
- __&#95;&#95;밑줄 두개로 둘러싸도 진하게2, 강하게2&#95;&#95;__
- &#60;del&#62;태그, <del>취소, 이제</del>
- &#126;&#126;물결표시 2개로 둘러싸도&#126;&#126; ~~태그, 취소~~

* 글자색, 배경색은 html의 sapn태그로 작성 가능
```
<span style="color: red">red</span>
<span style="color: #0000FF">파랑</span>
<span style="color: #008000">초록</span>
<span style="color: #2D3748; background-color:#fff5b1;"> Strong</span>
<span style="color: #808080">그레이</span>
<span style="color: #ffd33d">노랑</span>
<span style='background-color: #fff5b1'>노란형광펜</span>
<span style='background-color: #f6f8fa'>회색형광펜</span>
<span style='background-color: #f1f8ff'>파랑형광펜</span>
<span style='background-color: #ffdce0'>빨강형광펜</span>
<span style='background-color: #dcffe4'>초록형광펜</span>
<span style='background-color: #f5f0ff'>보라형광펜</span>
<span style='background-color: #F7DDBE'>주황형광펜</span>
```

<span style="color: red">red</span>
<span style="color: #0000FF">파랑</span>
<span style="color: #008000">초록</span>
<span style="color: #2D3748; background-color:#fff5b1;"> Strong</span>
<span style="color: #808080">그레이</span>
<span style="color: #ffd33d">노랑</span>
<span style='background-color: #fff5b1'>노란형광펜</span>
<span style='background-color: #f6f8fa'>회색형광펜</span>
<span style='background-color: #f1f8ff'>파랑형광펜</span>
<span style='background-color: #ffdce0'>빨강형광펜</span>
<span style='background-color: #dcffe4'>초록형광펜</span>
<span style='background-color: #f5f0ff'>보라형광펜</span>
<span style='background-color: #F7DDBE'>주황형광펜</span>

## 7. 링크, 이미지
```
[GOOGLE](https://google.com)
[NAVER](https://naver.com "링크 설명(title)을 작성하세요.")
[상대적 참조](../users/login)
[GitHub][1] 문서 안에서 [참조 링크]를 그대로 사용할 수도 있습니다.

다음과 같이 문서 내 일반 URL이나 꺾쇠 괄호(`< >`, Angle Brackets)안의 URL은 자동으로 링크를 사용합니다.
구글 홈페이지: https://google.com
네이버 홈페이지: <https://naver.com>

이미지는 다음양식을 사용하면 됩니다.
![](image주소 url)
![대체택스트](image주소 url)
```
[GOOGLE](https://google.com)<br>
[NAVER](https://naver.com "링크 설명(title)을 작성하세요.")<br>
[상대적 참조](../users/login)<br>
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbfCAYe%2FbtrVOxCOtni%2FBpOdKKvmsNhN3ttVtUek91%2Fimg.jpg)
![고마워요](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FXaZ6F%2FbtrVUysF599%2FnhTFnkrkkJX85XJ6swvHfk%2Fimg.jpg)

## 8. 표 작성
&#60;table&#62; 태그로도 사용가능하나 작성법을 알아두자..
- 헤더 셀을 구분할 때 3개 이상의 -(hyphen/dash) 기호가 필요하다.
- 헤더 셀을 구분하면서 :(Colons) 기호로 셀(열/칸) 안에 내용을 정렬할 수 있다.
- 가장 좌측과 가장 우측에 있는 |(vertical bar) 기호는 생략 가능하다.
- 아직 행이나 열 병합 기능은 지원하지 않는 것으로 보인다.

3열 테이블
| 값 | 의미 | 기본값 |
|---|:---:|---:|
| `static` | 유형(기준) 없음 / 배치 불가능 | `static` |
| `relative` | 요소 자신을 기준으로 배치 |  |
| `absolute` | 위치 상 부모(조상)요소를 기준으로 배치 |  |
| `fixed` | 브라우저 창을 기준으로 배치 |  |

4열 테이블
값 | 의미 | 기본값 | 비고
---|:---:|---:|---:
`static` | 유형(기준) 없음 / 배치 불가능 | `static`
`relative` | 요소 **자신**을 기준으로 배치 | | 비교
`absolute` | 위치 상 **_부모_(조상)요소**를 기준으로 배치 |
`fixed` | **브라우저 창**을 기준으로 배치 | | 고정
