## DATETIME에서 DATE로 형 변환

##### 문제 설명

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

| NAME             | TYPE       | NULLABLE |
| ---------------- | ---------- | -------- |
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| INTAKE_CONDITION | VARCHAR(N) | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_INTAKE  | VARCHAR(N) | FALSE    |

`ANIMAL_INS` 테이블에 등록된 모든 레코드에 대해, 각 동물의 아이디와 이름, 들어온 날짜[1](https://school.programmers.co.kr/learn/courses/30/lessons/59414#fn1)를 조회하는 SQL문을 작성해주세요. 이때 결과는 아이디 순으로 조회해야 합니다.

##### 예시

예를 들어, `ANIMAL_INS` 테이블이 다음과 같다면

```
ANIMAL_INS
```

| ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME   | SEX_UPON_INTAKE |
| --------- | ----------- | ------------------- | ---------------- | ------ | --------------- |
| A349996   | Cat         | 2018-01-22 14:32:00 | Normal           | Sugar  | Neutered Male   |
| A350276   | Cat         | 2017-08-13 13:50:00 | Normal           | Jewel  | Spayed Female   |
| A350375   | Cat         | 2017-03-06 15:01:00 | Normal           | Meo    | Neutered Male   |
| A352555   | Dog         | 2014-08-08 04:20:00 | Normal           | Harley | Spayed Female   |
| A352713   | Cat         | 2017-04-13 16:29:00 | Normal           | Gia    | Spayed Female   |

SQL문을 실행하면 다음과 같이 나와야 합니다.

| ANIMAL_ID | NAME   | 날짜       |
| --------- | ------ | ---------- |
| A349996   | Sugar  | 2018-01-22 |
| A350276   | Jewel  | 2017-08-13 |
| A350375   | Meo    | 2017-03-06 |
| A352555   | Harley | 2014-08-08 |
| A352713   | Gia    | 2017-04-13 |

------

본 문제는 [Kaggle의 "Austin Animal Center Shelter Intakes and Outcomes"](https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes)에서 제공하는 데이터를 사용하였으며 [ODbL](https://opendatacommons.org/licenses/odbl/1.0/)의 적용을 받습니다.

------

1. 시각(시-분-초)을 제외한 날짜(년-월-일)만 보여주세요. [↩](https://school.programmers.co.kr/learn/courses/30/lessons/59414#fnref1)

## 회고

DATE_FORMAT 함수는 DATETIME의 TYPE을 가진 칼럼의 형식을 수정, 지정해주는 함수이다.

형식: DATE FORMAT(날짜, 출력 형식)

- %Y: 년도 표현 4자리로
- %y: 년도 표현 2자리로
- %M: 월 이름을 Full Name으로 Ex) January ~ December
- %m: 월 이름을 00 ~ 12 숫자로
- %D: 일 이름을 1st, 2nd ... 으로
- %d: 일 이름을 01 ~ 31 숫자로