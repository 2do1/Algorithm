## 정수 내림차순으로 배치하기

##### 문제 설명

함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

##### 제한 조건

- `n`은 1이상 8000000000 이하인 자연수입니다.

##### 입출력 예

| n      | return |
| ------ | :----: |
| 118372 | 873211 |

## 회고

문자열을 리스트로 변환하면 문자열의 문자들이 분리되어 리스트에 추가된다는 것을 기억하자. Ex) list("python") -> ['p', 'y', 't', 'h', 'o', 'n']

sort()와 sorted() 차이를 정확히 기억하자. 리스트 정렬과 join() 함수를 이용하여 풀 수 있는 문제였다.

