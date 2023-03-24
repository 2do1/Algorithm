## 조건에 부합하는 중고거래 상태 조회하기

##### 문제 설명

다음은 중고거래 게시판 정보를 담은 `USED_GOODS_BOARD` 테이블입니다. `USED_GOODS_BOARD` 테이블은 다음과 같으며 `BOARD_ID`, `WRITER_ID`, `TITLE`, `CONTENTS`, `PRICE`, `CREATED_DATE`, `STATUS`, `VIEWS`은 게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수를 의미합니다.

| Column name  | Type          | Nullable |
| ------------ | ------------- | -------- |
| BOARD_ID     | VARCHAR(5)    | FALSE    |
| WRITER_ID    | VARCHAR(50)   | FALSE    |
| TITLE        | VARCHAR(100)  | FALSE    |
| CONTENTS     | VARCHAR(1000) | FALSE    |
| PRICE        | NUMBER        | FALSE    |
| CREATED_DATE | DATE          | FALSE    |
| STATUS       | VARCHAR(10)   | FALSE    |
| VIEWS        | NUMBER        | FALSE    |

---

##### 문제

`USED_GOODS_BOARD` 테이블에서 2022년 10월 5일에 등록된 중고거래 게시물의 게시글 ID, 작성자 ID, 게시글 제목, 가격, 거래상태를 조회하는 SQL문을 작성해주세요. 거래상태가 SALE 이면 판매중, RESERVED이면 예약중, DONE이면 거래완료 분류하여 출력해주시고, 결과는 게시글 ID를 기준으로 내림차순 정렬해주세요.

---

##### 예시

`USED_GOODS_BOARD` 테이블이 다음과 같을 때

| BOARD_ID | WRITER_ID | TITLE             | CONTENTS                                       | PRICE | CREATED_DATE | STATUS | VIEWS |
| -------- | --------- | ----------------- | ---------------------------------------------- | ----- | ------------ | ------ | ----- |
| B0007    | s2s2123   | 커피글라인더      | 새상품처럼 깨끗합니다.                         | 7000  | 2022-10-04   | DONE   | 210   |
| B0008    | hong02    | 자전거 판매합니다 | 출퇴근용으로 구매했다가 사용하지 않아서 내놔요 | 40000 | 2022-10-04   | SALE   | 301   |
| B0009    | yawoong67 | 선반 팝니다       | 6단 선반. 환불 반품 안됩니다.                  | 12000 | 2022-10-05   | DONE   | 202   |
| B0010    | keel1990  | 철제선반5단       | 철제선반 5단 조립식 팜                         | 10000 | 2022-10-05   | SALE   | 194   |

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| BOARD_ID | WRITER_ID | TITLE       | PRICE | STATUS   |
| -------- | --------- | ----------- | ----- | -------- |
| B0010    | keel1990  | 철제선반5단 | 10000 | 판매중   |
| B0009    | yawoong67 | 선반 팝니다 | 12000 | 거래완료 |

## 회고

DATE_FORMAT 함수는 DATETIME의 TYPE을 가진 칼럼의 형식을 수정, 지정해주는 함수이다.

형식: DATE FORMAT(날짜, 출력 형식)

- %Y: 년도 표현 4자리로
- %y: 년도 표현 2자리로
- %M: 월 이름을 Full Name으로 Ex) January ~ December
- %m: 월 이름을 00 ~ 12 숫자로
- %D: 일 이름을 1st, 2nd ... 으로
- %d: 일 이름을 01 ~ 31 숫자로



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
