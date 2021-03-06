# 이진수 덧셈 

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| :-------- | :---------- | :--- | :--- | :-------- | :-------- |
| 1 초      | 128 MB      | 2888 | 1025 | 911       | 40.870%   |

## 문제

이진수 덧셈은 매우 간단하고, 십진수 덧셈과 비슷하게 하면 된다. 십진수 덧셈을 할 때는, 오른쪽부터 왼쪽으로 차례대로 숫자 하나씩 더하면 된다. 이진수 덧셈도 이와 비슷하게 하면 된다. 십진수 덧셈은 외워야 할 덧셈이 많지만, 이진수 덧셈은 아래와 같이 5가지만 기억하면 된다.

- 0 + 0 = 0
- 1 + 0 = 1
- 0 + 1 = 1
- 1 + 1 = 10
- 1 + 1 + 1 = 11

두 이진수가 주어졌을 때, 그 합을 이진수로 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 테스트 케이스의 수 T(1<=T<=1,000)가 주어진다. 각 테스트 케이스는 숫자 2개로 이루어져있다. 이 숫자는 0과 1로만 이루어진 이진수이며, 길이는 최대 80자리이다. (덧셈 결과는 81자리가 될 수도 있다) 이진수는 0으로 시작할 수도 있다.

## 출력

각 테스트 케이스에 대해 입력으로 주어진 두 이진수의 합을 구해 이진수로 출력한다. 숫자의 앞에 불필요한 0이 붙으면 안 된다.

## 예제 입력 1 

```
3
1001101 10010
1001001 11001
1000111 1010110
```

## 예제 출력 1 복사

```
1011111
1100010
10011101
```

# 회고

int() 함수와 bin() 함수를 이용해서 푸는 문제이다.

다른 진수의 문자열을 10진수로 변환하려고 하면 int() 함수에 진수의 base값(2~36) 값을 int(value, base) 형태로 입력하면 된다.

파이썬에는 10진수에서 2, 8, 16진수로 변환해주는 bin(), oct(), hex() 함수가 있다는 것을 기억하자.

앞의 진법 표시를 지우기 위해서는 [2:] 슬라이싱을 통해 지울 수 있다.