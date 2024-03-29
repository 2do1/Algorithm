# GCD 합  

| 시간 제한 | 메모리 제한 | 제출  | 정답  | 맞힌 사람 | 정답 비율 |
| :-------- | :---------- | :---- | :---- | :-------- | :-------- |
| 1 초      | 128 MB      | 28023 | 10991 | 8953      | 40.108%   |

## 문제

양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 테스트 케이스의 개수 t (1 ≤ t ≤ 100)이 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있다. 각 테스트 케이스는 수의 개수 n (1 < n ≤ 100)가 주어지고, 다음에는 n개의 수가 주어진다. 입력으로 주어지는 수는 1,000,000을 넘지 않는다.

## 출력

각 테스트 케이스마다 가능한 모든 쌍의 GCD의 합을 출력한다.

## 예제 입력 1 복사

```
3
4 10 20 30 40
3 7 5 12
3 125 15 25
```

## 예제 출력 1 복사

```
70
3
35
```

# 회고

유클리드 알고리즘과 itertools 라이브러리의 combinations() 함수를 이용했다.

유클레드 호제법이란 두 정수의 최대공약수를 구하는 알고리즘으로, 두 정수 a, b (a > b)의 최대공약수가 b와 r(a를 b로 나눈 나머지)의 최대공약수와 같다는 원리를 이용한 알고리즘이다.

유클리드 호제법은 반복문과 재귀 함수를 통해 구현할 수 있다.

math 라이브러리에서 gcd() 함수와 lcm() 함수를 제공한다.

다른 사람의 풀이를 보니 combinations() 함수를 이용하지 않고, 이중 for문을 이용하여 두 수를 선택해 최대공약수를 구했다.