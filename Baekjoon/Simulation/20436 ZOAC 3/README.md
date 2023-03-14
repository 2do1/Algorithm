# ZOAC 3

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| :-------- | :---------- | :--- | :--- | :-------- | :-------- |
| 1 초      | 1024 MB     | 1535 | 727  | 604       | 46.569%   |

## 문제

2020년 12월, 세 번째로 개최된 ZOAC의 오프닝을 맡은 성우는 누구보다 빠르게 ZOAC를 알리려 한다.

하지만 안타깝게도 성우는 독수리타법이다!

- 독수리 타법이란 양 손의 검지손가락만을 이용해 타자를 치는 타법이다.

- 성우는 한글 자음 쪽 자판은 왼손 검지손가락으로 입력하고, 한글 모음 쪽 자판은 오른손 검지손가락으로 입력한다.

- *a*의 좌표가 (x1, y1)이고, *b*의 좌표가 (x2, y2)일 때, *a*에 위치한 성우의 손가락이 *b*로 이동하는 데에는 *a*와 *b*의 택시 거리 |x1-x2|+|y1-y2| 만큼의 시간이 걸린다.

- 각 키를 누르는 데에는 1의 시간이 걸린다.

- 성우는 두 손을 동시에 움직일 수 없다.

- 성우가 사용하는 키보드는 쿼티식 키보드이며, 아래 그림처럼 생겼다.

  ![img](https://upload.acmicpc.net/408ea292-3a7e-4b25-b5ec-d6a85f82a6ce/-/preview/)

바쁜 성우를 위하여 해당 문자열을 출력하는 데 걸리는 시간의 최솟값을 구해보자.

## 입력

첫 번째 줄에는 두 알파벳 소문자 *sL*, *sR*이 주어진다. *sL*, *sR*은 각각 왼손 검지손가락, 오른손 검지손가락의 처음 위치이다.

그 다음 줄에는 알파벳 소문자로 구성된 문자열이 주어진다. 문자열의 길이는 최대 100자이다. 빈 문자열은 주어지지 않는다.

## 출력

입력으로 주어진 문자열을 출력하는 데에 걸리는 시간의 최솟값을 출력한다.

## 예제 입력 1 

```
z o
zoac
```

## 예제 출력 1 

```
8
```

## 힌트

성우가 두 손을 동시에 움직이지 못하는 이유는 다음과 같다.

- 사람은 두 가지 이상의 일을 동시에 할 수 없다.
- 대학원생은 사람이다.
- 성우는 대학원생이다.

# 회고

''성우는 한글 자음 쪽 자판은 왼손 검지손가락으로 입력하고, 한글 모음 쪽 자판은 오른손 검지손가락으로 입력한다." 라는 조건을 처음에 확인하지 못해서 틀렸었다..

이 조건을 보고 한글 자음과 한글 모음을 어떻게 구별하지?? 고민을 많이 했었는데

그냥 단순하게 한글 자음쪽 자판들인 알파벳 소문자들을 모아 변수에 저장해준 뒤, 거리를 재기 전에 in 함수를 이용하여 한글 자음 쪽 자판인지, 모음 쪽 자판인지의 여부를 체크해주면 됐다.

알고리즘 문제를 풀 때 너무 어렵게 생각하는 경우가 많은 것 같다. 천천히 생각해보면 쉽게 풀 수 있는 문제인데.. 더욱 더 문제를 많이 풀어봐야겠다