# 고무오리 디버깅 

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| :-------- | :---------- | :--- | :--- | :-------- | :-------- |
| 1 초      | 512 MB      | 2115 | 1258 | 1130      | 63.058%   |

## 문제

백준 문제 풀이에 힘들어하는 수진이를 위해 민우는 문제해결에 도움이 되는 고무오리를 준비했다. 민우가 준비한 고무오리는 신비한 능력이 존재하는데, 최근에 풀던 백준 문제를 해결해주는 능력이다. 신비한 고무오리와 함께 수진이의 백준 풀이를 도와주자!

고무오리의 사용법은 다음과 같다.

- "고무오리 디버깅 시작" 이라고 외친다
- 문제들을 풀기 시작한다
- 고무오리를 받으면 최근 풀던 문제를 해결한다
- "고무오리 디버깅 끝" 이라고 외치면 문제풀이를 종료한다.

하지만 고무오리에는 치명적인 문제가 있는데, 풀 문제가 없는데 사용한다면 고무오리는 벌칙으 로 두 문제를 추가한다는 점이다.

## 입력

첫 번째 줄에 "고무오리 디버깅 시작"이라고 주어진다. 두 번째 줄부터 "고무오리" 또는 "문제"가 주어진다. 이는 "고무오리 디버깅 끝"이 주어질 때까지 반복한다. 최대 102줄이 입력으로 주어진다.

## 출력

고무오리 디버깅이 끝날 때, 주어진 문제를 수진이가 해결하였는지 여부에 따라 남은 문제 없이 모든 문제를 해결하였으면 "고무오리야 사랑해"을 출력하고 하나라도 문제가 남았다면 "힝구"를 출력하라.

## 예제 입력 1 

```
고무오리 디버깅 시작
문제
고무오리
문제
문제
고무오리
고무오리
고무오리 디버깅 끝
```

## 예제 출력 1 

```
고무오리야 사랑해
```

## 예제 입력 2 

```
고무오리 디버깅 시작
고무오리
고무오리
고무오리
고무오리 디버깅 끝
```

## 예제 출력 2 

```
고무오리야 사랑해
```

## 예제 입력 3 

```
고무오리 디버깅 시작
문제
문제
고무오리
고무오리
고무오리
문제
고무오리
문제
고무오리
고무오리
고무오리
고무오리 디버깅 끝
```

## 예제 출력 3 

```
고무오리야 사랑해
```

## 예제 입력 4 

```
고무오리 디버깅 시작
고무오리
고무오리 디버깅 끝
```

## 예제 출력 4 

```
힝구
```

# 회고

스택을 이용해 풀이하면 됐다.