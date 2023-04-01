# 염색체

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| :-------- | :---------- | :--- | :--- | :-------- | :-------- |
| 2 초      | 64 MB       | 1634 | 1099 | 833       | 69.533%   |

## 문제

상근이는 생명과학 연구소에서 염색체가 특정한 패턴인지를 확인하는 일을 하고 있다. 염색체는 알파벳 대문자 (A, B, C, ..., Z)로만 이루어진 문자열이다. 상근이는 각 염색체가 다음과 같은 규칙을 만족하는지 검사해야 한다.

- 문자열은 {A, B, C, D, E, F} 중 0개 또는 1개로 시작해야 한다.
- 그 다음에는 A가 하나 또는 그 이상 있어야 한다.
- 그 다음에는 F가 하나 또는 그 이상 있어야 한다.
- 그 다음에는 C가 하나 또는 그 이상 있어야 한다.
- 그 다음에는 {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다.

문자열이 주어졌을 때, 위의 규칙을 만족하는지 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 테스트 케이스의 개수 T ≤ 20 이 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 최대 200개의 알파벳 대문자로 이루어진 문자열이 주어진다.

## 출력

각 테스트 케이스에 대해서, 문제의 규칙을 지키는 문자열인 경우에는  "Infected!"를, 아닌 경우에는 "Good"을 출력한다.

## 예제 입력 1 

```
15
AFC
AAFC
AAAFFCC
AAFCC
BAFC
QWEDFGHJMNB
DFAFCB
ABCDEFC
DADC
SDFGHJKLQWERTYU
AAAAAAAAAAAAABBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCDDDDDDDDDDDEEEEEEEEEEEEEEEFFFFFFFFC
AAAFFFFFBBBBCCCAAAFFFF
ABCDEFAAAFFFCCCABCDEF
AFCP
AAFFCPP
```

## 예제 출력 1 

```
Infected!
Infected!
Infected!
Infected!
Infected!
Good
Good
Good
Good
Good
Good
Good
Good
Good
Good
```

# 회고

파이썬에서는 re 모듈을 통해 정규 표현식을 사용한다.

re.compile()을 사용하여 정규 표현식을 컴파일 한다.

match() 함수를 이용해 문자열의 처음부터 정규식과 매치되는지 조사한다.

- `^` : 해당 패턴으로 시작
- `?` : 해당 패턴을 0번또는 1번
- `$` : 해당 패턴으로 끝
- `+` : 해당 패턴이 하나 이상