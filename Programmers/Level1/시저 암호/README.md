## 시저 암호

##### 문제 설명

어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

##### 제한 조건

- 공백은 아무리 밀어도 공백입니다.
- s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
- s의 길이는 8000이하입니다.
- n은 1 이상, 25이하인 자연수입니다.

##### 입출력 예

| s       | n    | result  |
| ------- | ---- | ------- |
| "AB"    | 1    | "BC"    |
| "z"     | 1    | "a"     |
| "a B z" | 4    | "e F d" |

## 회고

아스키 코드로 변환해서 푸는 문제. chr() 함수와 ord() 함수를 이용했다.

chr() 함수는 아스키 코드 값을 입력받아 그 코드에 해당하는 문자를 리턴해주고,

ord() 함수는 문자의 아스키 코드 값을 리턴해준다.

다른 사람의 코드가 공백을 무시하고 문자만 생각해도 되는 점과, 시간복잡도 면에서도 더 나은것 같다.