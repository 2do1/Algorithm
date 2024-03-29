# 달나라 토끼를 위한 구매대금 지불 도우미

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| :-------- | :---------- | :--- | :--- | :-------- | :-------- |
| 1 초      | 256 MB      | 2103 | 1003 | 833       | 49.554%   |

## 문제

달나라 토끼들이 사용하는 화폐는 동전뿐이다. 동전의 종류는 1원, 2원, 5원, 7원 이렇게 4종류가 있다. 물건을 사고 동전으로 계산을 하는데 동전의 개수가 최소가 되도록 지불하지 않는 것은 불법이다. 예를 들어, 17원을 지불할 때 7원짜리 동전 1개와 5원짜리 동전 2개로 지불해야 합법이고, 7원짜리 동전 2개와 2원짜리 동전 1개, 1원짜리 동전 1개로 지불해도 17원이 되지만, 총 동전의 개수가 4개가 되어 최소 개수가 아니므로 불법이다.

지불 금액을 입력받아 합법이 되는 동전 개수를 출력으로 내어주는 프로그램을 작성해보자.

## 입력

첫 번째 줄에 달나라 토끼가 지불해야하는 금액 N(0 ≤ N ≤ 100,000)이 주어진다.

## 출력

첫 번째 줄에 달나라 토끼가 합법적으로 낼 수 있는 동전의 개수를 출력한다.

## 예제 입력 1

```
12
```

## 예제 출력 1

```
2
```

## 예제 입력 2

```
21
```

## 예제 출력 2

```
3
```

## 힌트

| 지불 금액 | 합법 지불             | 불법 지불(예)                     |
| --------- | --------------------- | --------------------------------- |
| 12원      | 7원 x 1개 + 5원 x 1개 | 5원 x 2개 + 2원 x 1개             |
| 17원      | 7원 x 1개 + 5원 x 2개 | 7원 x 2개 + 2원 x 1개 + 1원 x 1개 |
| 21원      | 7원 x 3개             | 7원 x 2개 + 5원 x 1개 + 2원 x 1개 |

# 회고

금액이 7원 이상, 5원 이상, 2원 이상, 1원 이상일 경우 총 4가지로 나누어서 dp 테이블을 채워주면 됐다.
