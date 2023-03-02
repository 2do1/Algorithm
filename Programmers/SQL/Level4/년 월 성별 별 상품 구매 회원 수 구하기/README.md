## 년, 월, 성별 별 상품 구매 회원 수 구하기

##### 문제 설명

다음은 어느 의류 쇼핑몰에 가입한 회원 정보를 담은 `USER_INFO` 테이블과 온라인 상품 판매 정보를 담은 `ONLINE_SALE` 테이블 입니다.`USER_INFO` 테이블은 아래와 같은 구조로 되어있으며 `USER_ID`, `GENDER`, `AGE`, `JOINED`는 각각 회원 ID, 성별, 나이, 가입일을 나타냅니다.

| Column name | Type       | Nullable |
| ----------- | ---------- | -------- |
| USER_ID     | INTEGER    | FALSE    |
| GENDER      | TINYINT(1) | TRUE     |
| AGE         | INTEGER    | TRUE     |
| JOINED      | DATE       | FALSE    |

`GENDER` 컬럼은 비어있거나 0 또는 1의 값을 가지며 0인 경우 남자를, 1인 경우는 여자를 나타냅니다.

`ONLINE_SALE` 테이블은 아래와 같은 구조로 되어있으며, `ONLINE_SALE_ID`, `USER_ID`, `PRODUCT_ID`, `SALES_AMOUNT`, `SALES_DATE`는 각각 온라인 상품 판매 ID, 회원 ID, 상품 ID, 판매량, 판매일을 나타냅니다.

| Column name    | Type    | Nullable |
| -------------- | ------- | -------- |
| ONLINE_SALE_ID | INTEGER | FALSE    |
| USER_ID        | INTEGER | FALSE    |
| PRODUCT_ID     | INTEGER | FALSE    |
| SALES_AMOUNT   | INTEGER | FALSE    |
| SALES_DATE     | DATE    | FALSE    |

동일한 날짜, 회원 ID, 상품 ID 조합에 대해서는 하나의 판매 데이터만 존재합니다.

------

##### 문제

`USER_INFO` 테이블과 `ONLINE_SALE` 테이블에서 년, 월, 성별 별로 상품을 구매한 회원수를 집계하는 SQL문을 작성해주세요. 결과는 년, 월, 성별을 기준으로 오름차순 정렬해주세요. 이때, 성별 정보가 없는 경우 결과에서 제외해주세요.

------

##### 예시

예를 들어 `USER_INFO` 테이블이 다음과 같고

| USER_ID | GENDER | AGE  | JOINED     |
| ------- | ------ | ---- | ---------- |
| 1       | 1      | 26   | 2021-06-01 |
| 2       | NULL   | NULL | 2021-06-25 |
| 3       | 0      | NULL | 2021-06-30 |
| 4       | 0      | 31   | 2021-07-03 |
| 5       | 1      | 25   | 2021-07-09 |
| 6       | 1      | 33   | 2021-07-14 |

`ONLINE_SALE` 테이블이 다음과 같다면

| ONLINE_SALE_ID | USER_ID | PRODUCT_ID | SALES_AMOUNT | SALES_DATE |
| -------------- | ------- | ---------- | ------------ | ---------- |
| 1              | 1       | 54         | 1            | 2022-01-01 |
| 2              | 1       | 3          | 2            | 2022-01-25 |
| 3              | 4       | 34         | 1            | 2022-01-30 |
| 4              | 6       | 253        | 3            | 2022-02-03 |
| 5              | 2       | 31         | 2            | 2022-02-09 |
| 6              | 5       | 35         | 1            | 2022-02-14 |
| 7              | 5       | 57         | 1            | 2022-02-18 |

2022년 1월에 상품을 구매한 회원은 `USER_ID` 가 1(`GENDER`=1), 4(`GENDER`=0)인 회원들이고,
2022년 2월에 상품을 구매한 회원은 `USER_ID` 가 2(`GENDER`=NULL), 5(`GENDER`=1), 6(`GENDER`=1)인 회원들 이므로,

년, 월, 성별 별로 상품을 구매한 회원수를 집계하고, 년, 월, 성별을 기준으로 오름차순 정렬하면 다음과 같은 결과가 나와야 합니다.

| YEAR | MONTH | GENDER | USERS |
| ---- | ----- | ------ | ----- |
| 2022 | 1     | 0      | 1     |
| 2022 | 1     | 1      | 1     |
| 2022 | 2     | 1      | 2     |

## 회고

'동일한 날짜, 회원 ID, 상품 ID 조합에 대해서는 하나의 판매 데이터만 존재합니다' 라는 조건 때문에 중복제거를 해줘야 했다.

DISTINCT를 이용하여 중복 제거를 하였다.

MySQL 함수들을 통해 날짜 데이터에서 일부만을 추출할 수 있다.

- YEAR() : 연도 추출
- MONTH() : 월 추출
- DAY() : 일 추출
- HOUR() : 시 추출
- MINUTE() : 분 추출
- SECOND() : 초 추출

