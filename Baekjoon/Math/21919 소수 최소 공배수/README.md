# 소수 최소 공배수

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| :-------- | :---------- | :--- | :--- | :-------- | :-------- |
| 1 초      | 512 MB      | 1826 | 509  | 384       | 25.651%   |

## 문제

행복이는 길이가 N인 수열 A에서 소수들을 골라 최소공배수를 구해보려고 한다.

행복이를 도와 이를 계산해주자.

## 입력

첫째 줄에 수열 A의 길이 N이 주어진다. (1≤N≤10,000)

그 다음줄에는 수열 A의 원소 Ai가 공백으로 구분되어 주어진다. (2≤Ai≤1,000,000)

답이 2^63 미만인 입력만 주어진다.

## 출력

첫째 줄에 소수들의 최소공배수를 출력한다.

만약 소수가 없는 경우는 -1을 출력한다.

## 예제 입력 1 

```
5
2 3 5 6 8
```

## 예제 출력 1 

```
30
```

수열 중에 소수는 2, 3, 5가 있다.

## 예제 입력 2 

```
4
4 16 64 256
```

## 예제 출력 2

```
-1
```

소수가 없으므로 -1 이다.

# 회고

자연수가 소수인지를 판별할 때는 자연수의 제곱근 이하의 값까지만 검사를 하면 나머지는 검사를 할 필요가 없다.

출력 초과가 나와서 틀렸던 문제인데, 수열에 중복된 소수가 있는 경우를 예외처리 해주지 않아 틀렸었다...