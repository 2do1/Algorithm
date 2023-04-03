## 조건에 맞는 사용자 정보 조회하기

##### 문제 설명

다음은 중고 거래 게시판 정보를 담은 `USED_GOODS_BOARD` 테이블과 중고 거래 게시판 첨부파일 정보를 담은 `USED_GOODS_FILE` 테이블입니다. `USED_GOODS_BOARD` 테이블은 다음과 같으며 `BOARD_ID`, `WRITER_ID`, `TITLE`, `CONTENTS`, `PRICE`, `CREATED_DATE`, `STATUS`, `VIEWS`는 게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수를 의미합니다.

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

`USED_GOODS_USER` 테이블은 다음과 같으며 `USER_ID`, `NICKNAME`, `CITY`, `STREET_ADDRESS1`, `STREET_ADDRESS2`, `TLNO`는 각각 회원 ID, 닉네임, 시, 도로명 주소, 상세 주소, 전화번호를 의미합니다.

| Column name     | Type         | Nullable |
| --------------- | ------------ | -------- |
| USER_ID         | VARCHAR(50)  | FALSE    |
| NICKANME        | VARCHAR(100) | FALSE    |
| CITY            | VARCHAR(100) | FALSE    |
| STREET_ADDRESS1 | VARCHAR(100) | FALSE    |
| STREET_ADDRESS2 | VARCHAR(100) | TRUE     |
| TLNO            | VARCHAR(20)  | FALSE    |

------

##### 문제

`USED_GOODS_BOARD`와 `USED_GOODS_USER` 테이블에서 중고 거래 게시물을 3건 이상 등록한 사용자의 사용자 ID, 닉네임, 전체주소, 전화번호를 조회하는 SQL문을 작성해주세요. 이때, 전체 주소는 시, 도로명 주소, 상세 주소가 함께 출력되도록 해주시고, 전화번호의 경우 xxx-xxxx-xxxx 같은 형태로 하이픈 문자열(`-`)을 삽입하여 출력해주세요. 결과는 회원 ID를 기준으로 내림차순 정렬해주세요.

------

##### 예시

`USED_GOODS_BOARD` 테이블이 다음과 같고

| BOARD_ID | WRITER_ID | TITLE                  | CONTENTS                                          | PRICE  | CREATED_DATE | STATUS | VIEWS |
| -------- | --------- | ---------------------- | ------------------------------------------------- | ------ | ------------ | ------ | ----- |
| B0001    | dhfkzmf09 | 칼라거펠트 코트        | 양모 70%이상 코트입니다.                          | 120000 | 2022-10-14   | DONE   | 104   |
| B0002    | lee871201 | 국내산 볶음참깨        | 직접 농사지은 참깨입니다.                         | 3000   | 2022-10-02   | DONE   | 121   |
| B0003    | dhfkzmf09 | 나이키 숏패팅          | 사이즈는 M입니다.                                 | 40000  | 2022-10-17   | DONE   | 98    |
| B0004    | kwag98    | 반려견 배변패드 팝니다 | 정말 저렴히 판매합니다. 전부 미개봉 새상품입니다. | 12000  | 2022-10-01   | DONE   | 250   |
| B0005    | dhfkzmf09 | PS4                    | PS5 구매로인해 팝니다.                            | 250000 | 2022-11-03   | DONE   | 111   |

`USED_GOODS_USER` 테이블이 다음과 같을 때

| USER_ID   | NICKNAME   | CITY   | STREET_ADDRESS1   | STREET_ADDRESS2 | TLNO        |
| --------- | ---------- | ------ | ----------------- | --------------- | ----------- |
| dhfkzmf09 | 찐찐       | 성남시 | 분당구 수내로 13  | A동 1107호      | 01053422914 |
| dlPcks90  | 썹썹       | 성남시 | 분당구 수내로 74  | 401호           | 01034573944 |
| cjfwls91  | 점심만금식 | 성남시 | 분당구 내정로 185 | 501호           | 01036344964 |
| dlfghks94 | 희망       | 성남시 | 분당구 내정로 101 | 203동 102호     | 01032634154 |
| rkdhs95   | 용기       | 성남시 | 분당구 수내로 23  | 501호           | 01074564564 |

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| USER_ID   | NICKNAME | 전체주소                           | 전화번호      |
| --------- | -------- | ---------------------------------- | ------------- |
| dhfkzmf09 | 찐찐     | 성남시 분당구 수내로 13 A동 1107호 | 010-5342-2914 |

## 회고

문자열 자르기 함수에는 LEFT(), RIGHT(), MID() 함수가 있다.

- LEFT(): 왼쪽에서부터 지정한 문자열 개수만큼 가져온다. LEFT('문자열','왼쪽부터 가져올 갯수')
- RIGHT(): 오른쪽에서부터 지정한 문자열 개수만큼 가져온다. RIGHT('문자열','오른쪽부터 가져올 갯수')
- MID(): 지정한 시작 인덱스부터 지정한 문자열 개수만큼 가져온다. SUBSTR(), SUBSTRING()과 같다. MID('문자열', '시작 위치', '가져올 갯수')

CONCAT() 함수는 둘 이상의 문자열을 입력한 순서대로 합쳐서 반환해주는 함수이다.

문자열의 시작위치는 모든 DB 공통으로 1에서 시작한다. (0에서 시작하는 인덱스와는 다르다.)