# !밀비 급일

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| :-------- | :---------- | :--- | :--- | :-------- | :-------- |
| 1 초      | 256 MB      | 8857 | 5510 | 4984      | 63.971%   |

## 문제

당신은 길을 가다가 이상한 쪽지를 발견했다. 그 쪽지에는 암호가 적혀 있었는데, 똑똑한 당신은 암호가 뒤집으면 해독된다는 것을 발견했다.

이 암호를 해독하는 프로그램을 작성하시오.

## 입력

한 줄에 하나의 암호가 주어진다. 암호의 길이는 500을 넘지 않는다.

마지막 줄에는 "END"가 주어진다. (END는 해독하지 않는다.)

## 출력

각 암호가 해독된 것을 한 줄에 하나씩 출력한다.

## 예제 입력 1 복사

```
!edoc doog a tahW
noitacitsufbo
erafraw enirambus detcirtsernu yraurbeF fo tsrif eht no nigeb ot dnetni eW
lla sees rodroM fo drol eht ,ssertrof sih nihtiw delaecnoC
END
```

## 예제 출력 1 복사

```
What a good code!
obfustication
We intend to begin on the first of February unrestricted submarine warfare
Concealed within his fortress, the lord of Mordor sees all
```

# 회고

문자열 slicing을 통해 푸는 문제. [::-1]을 통해 문자열을 뒤집었다.