# 동일한 단어 그룹화하기

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| :-------- | :---------- | :--- | :--- | :-------- | :-------- |
| 2 초      | 512 MB      | 976  | 662  | 589       | 68.250%   |

## 문제

소문자로 이루어진 단어 N개가 주어졌을 때, 단어가 총 최소 몇 개의 그룹으로 이루어져 있는지 구하는 프로그램을 작성하시오.

그룹에 속한 단어는 모두 같은 알파벳으로 이루어져 있어야 하고, 개수도 같아야 한다. 즉, 단어를 구성하는 알파벳의 순서만 달라야 한다.

## 입력

첫째 줄에 단어의 개수 N이 주어진다. (2 ≤ N ≤ 100) 둘째 줄부터 N개의 줄에 단어가 한 줄에 하나씩 주어진다. 단어는 알파벳 소문자로만 이루어져 있고, 길이는 10을 넘지 않는다.

## 출력

첫째 줄에 그룹의 최소 개수를 출력한다.

## 예제 입력 1 

```
4
cat
dog
god
tca
```

## 예제 출력 1 

```
2
```

## 예제 입력 2 

```
2
a
a
```

## 예제 출력 2 

```
1
```

# 회고

알파벳 개수를 세줄 필요 없이 그냥 입력받은 단어를 정렬하고 문자열로 합쳐준 뒤 리스트에 저장한다.

그 후 set 자료구조를 이용하여 중복 제거를 해 최소 몇 개의 그룹으로 이루어져 있는지 구하면 됐다.