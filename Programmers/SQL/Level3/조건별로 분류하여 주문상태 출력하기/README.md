## 조건별로 분류하여 주문상태 출력하기

##### 문제 설명

다음은 식품공장의 주문정보를 담은 `FOOD_ORDER` 테이블입니다. `FOOD_ORDER` 테이블은 다음과 같으며 `ORDER_ID`, `PRODUCT_ID`, `AMOUNT`, `PRODUCE_DATE`, `IN_DATE`,`OUT_DATE`,`FACTORY_ID`, `WAREHOUSE_ID`는 각각 주문 ID, 제품 ID, 주문양, 생산일자, 입고일자, 출고일자, 공장 ID, 창고 ID를 의미합니다.

| Column name  | Type        | Nullable |
| ------------ | ----------- | -------- |
| ORDER_ID     | VARCHAR(10) | FALSE    |
| PRODUCT_ID   | VARCHAR(5)  | FALSE    |
| AMOUNT       | NUMBER      | FALSE    |
| PRODUCE_DATE | DATE        | TRUE     |
| IN_DATE      | DATE        | TRUE     |
| OUT_DATE     | DATE        | TRUE     |
| FACTORY_ID   | VARCHAR(10) | FALSE    |
| WAREHOUSE_ID | VARCHAR(10) | FALSE    |

------

##### 문제

`FOOD_ORDER` 테이블에서 5월 1일을 기준으로 주문 ID, 제품 ID, 출고일자, 출고여부를 조회하는 SQL문을 작성해주세요. 출고여부는 5월 1일까지 출고완료로 이 후 날짜는 출고 대기로 미정이면 출고미정으로 출력해주시고, 결과는 주문 ID를 기준으로 오름차순 정렬해주세요.

------

##### 예시

`FOOD_ORDER` 테이블이 다음과 같을 때

| ORDER_ID   | PRODUCT_ID | AMOUNT | PRODUCE_DATE | IN_DATE    | OUT_DATE   | FACTORY_ID | WAREHOUSE_ID |
| ---------- | ---------- | ------ | ------------ | ---------- | ---------- | ---------- | ------------ |
| OD00000051 | P0002      | 4000   | 2022-04-01   | 2022-04-21 | 2022-04-21 | FT19970003 | WH0005       |
| OD00000052 | P0003      | 2500   | 2022-04-10   | 2022-04-27 | 2022-04-27 | FT19970003 | WH0006       |
| OD00000053 | P0005      | 6200   | 2022-04-15   | 2022-04-30 | 2022-05-01 | FT19940003 | WH0003       |
| OD00000054 | P0006      | 1000   | 2022-04-21   | 2022-04-30 | NULL       | FT19940003 | WH0009       |
| OD00000055 | P0008      | 1500   | 2022-04-25   | 2022-05-11 | 2022-05-11 | FT19980003 | WH0009       |

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| ORDER_ID   | PRODUCT_ID | OUT_DATE   | 출고여부 |
| ---------- | ---------- | ---------- | -------- |
| OD00000051 | P0002      | 2022-04-21 | 출고완료 |
| OD00000052 | P0003      | 2022-04-27 | 출고완료 |
| OD00000053 | P0005      | 2022-05-01 | 출고완료 |
| OD00000054 | P0006      |            | 출고미정 |
| OD00000055 | P0008      | 2022-05-11 | 출고대기 |

## 회고

IF문 또는 CASE문을 이용하여 풀이할 수 있었던 문제였다.

부등호를 이용하여 5월 1일 이전 날짜인지 5월 1일 이후 날짜인지를 확인하였다.

CASE문

- WHEN - THEN은 항상 같이 사용되어야 한다.
- WHEN - THEN은 여러개 사용 가능하다.
- ELSE가 존재할 때, 모든 조건에 해당하지 않는 경우 ELSE 결과값을 반환한다.
- ELSE가 존재하지 않을 때, 모든 조건에 해당하지 않는 경우 NULL을 반환한다.

```mysql
# CASE문 사용 방법

CASE
    WHEN 조건1 THEN 결과값1
    WHEN 조건2 THEN 결과값2
    WHEN 조건N THEN 결과값N
    ELSE 결과값
END
```