# 소수&팰린드롬

| 시간 제한 | 메모리 제한 | 제출  | 정답 | 맞힌 사람 | 정답 비율 |
| :-------- | :---------- | :---- | :--- | :-------- | :-------- |
| 2 초      | 256 MB      | 17643 | 5600 | 4154      | 30.397%   |

## 문제

어떤 수와 그 수의 숫자 순서를 뒤집은 수가 일치하는 수를 팰린드롬이라 부른다. 예를 들어 79,197과 324,423 등이 팰린드롬 수이다.

어떤 수 N (1 ≤ N ≤ 1,000,000)이 주어졌을 때, N보다 크거나 같고, 소수이면서 팰린드롬인 수 중에서, 가장 작은 수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N이 주어진다.

## 출력

첫째 줄에 조건을 만족하는 수를 출력한다.

## 예제 입력 1 

```
31
```

## 예제 출력 1 

```
101
```

# 회고

팰린드롬인지의 여부와 소수인지의 여부를 판단하는 함수를 각각 만들어서 풀이하였다.

소수인지의 여부를 판단할 때 숫자 1의 예외처리는 꼭 해주자.

자연수가 소수인지를 판별할 때는 자연수의 제곱근 이하의 값까지만 검사를 하면 나머지는 검사를 할 필요가 없다.

팰린드롬인지의 여부를 판단할 때는 [::-1] 문자열 슬라이싱을 이용하였다.