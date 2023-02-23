## 가격이 제일 비싼 식품의 정보 출력하기

##### 문제 설명

다음은 식품의 정보를 담은 `FOOD_PRODUCT` 테이블입니다. `FOOD_PRODUCT` 테이블은 다음과 같으며 `PRODUCT_ID`, `PRODUCT_NAME`, `PRODUCT_CD`, `CATEGORY`, `PRICE`는 식품 ID, 식품 이름, 식품 코드, 식품분류, 식품 가격을 의미합니다.

| Column name  | Type        | Nullable |
| ------------ | ----------- | -------- |
| PRODUCT_ID   | VARCHAR(10) | FALSE    |
| PRODUCT_NAME | VARCHAR(50) | FALSE    |
| PRODUCT_CD   | VARCHAR(10) | TRUE     |
| CATEGORY     | VARCHAR(10) | TRUE     |
| PRICE        | NUMBER      | TRUE     |

------

##### 문제

`FOOD_PRODUCT` 테이블에서 가격이 제일 비싼 식품의 식품 ID, 식품 이름, 식품 코드, 식품분류, 식품 가격을 조회하는 SQL문을 작성해주세요.

------

##### 예시

`FOOD_PRODUCT` 테이블이 다음과 같을 때

| PRODUCT_ID | PRODUCT_NAME   | PRODUCT_CD | CATEGORY | PRICE |
| ---------- | -------------- | ---------- | -------- | ----- |
| P0018      | 맛있는고추기름 | CD_OL00008 | 식용유   | 6100  |
| P0019      | 맛있는카놀라유 | CD_OL00009 | 식용유   | 5100  |
| P0020      | 맛있는산초유   | CD_OL00010 | 식용유   | 6500  |
| P0021      | 맛있는케첩     | CD_OL00001 | 소스     | 4500  |
| P0022      | 맛있는마요네즈 | CD_OL00002 | 소스     | 4700  |

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| PRODUCT_ID | PRODUCT_NAME | PRODUCT_CD | CATEGORY | PRICE |
| ---------- | ------------ | ---------- | -------- | ----- |
| P0020      | 맛있는산초유 | CD_OL00010 | 식용유   | 6500  |

## 회고

처음 쿼리를 작성할 때 다음과 같이 작성하였는데

SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, MAX(PRICE)

이렇게 작성하면 가격이 최대인 상품의 가격만 보여주고, 나머지 값은 테이블의 처음 상품의 속성을 보여준다.

서브쿼리를 이용하여 풀이하였다. 이 문제 같은 경우는 단일행 서브쿼리이다.

서브쿼리란 하나의 쿼리 문장 내에 포함된 또 하나의 쿼리 문장이다.

- 서브쿼리는 괄호()로 감싸져서 표현 된다.
- 서브쿼리는 단일 행 또는 복수 행 비교 연산자와 함께 사용 가능하다.
- 서브쿼리에서는 ORDER BY를 사용하지 못한다.

WHERE 문에 나타는 서브쿼리를 중첩 서브쿼리(Nested Subquery)라고 한다.