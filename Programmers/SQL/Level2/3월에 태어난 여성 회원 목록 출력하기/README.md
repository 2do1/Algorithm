## 3월에 태어난 여성 회원 목록 출력하기

##### 문제 설명

다음은 식당 리뷰 사이트의 회원 정보를 담은 `MEMBER_PROFILE` 테이블입니다. `MEMBER_PROFILE` 테이블은 다음과 같으며 `MEMBER_ID`, `MEMBER_NAME`, `TLNO`, `GENDER`, `DATE_OF_BIRTH`는 회원 ID, 회원 이름, 회원 연락처, 성별, 생년월일을 의미합니다.

| Column name   | Type         | Nullable |
| ------------- | ------------ | -------- |
| MEMBER_ID     | VARCHAR(100) | FALSE    |
| MEMBER_NAME   | VARCHAR(50)  | FALSE    |
| TLNO          | VARCHAR(50)  | TRUE     |
| GENDER        | VARCHAR(1)   | TRUE     |
| DATE_OF_BIRTH | DATE         | TRUE     |

---

##### 문제

`MEMBER_PROFILE` 테이블에서 생일이 3월인 여성 회원의 ID, 이름, 성별, 생년월일을 조회하는 SQL문을 작성해주세요. 이때 전화번호가 NULL인 경우는 출력대상에서 제외시켜 주시고, 결과는 회원ID를 기준으로 오름차순 정렬해주세요.

---

##### 예시

`MEMBER_PROFILE` 테이블이 다음과 같을 때

| MEMBER_ID              | MEMBER_NAME | TLNO        | GENDER | DATE_OF_BIRTH |
| ---------------------- | ----------- | ----------- | ------ | ------------- |
| `jiho92@naver.com`     | 이지호      | 01076432111 | W      | 1992-02-12    |
| `jiyoon22@hotmail.com` | 김지윤      | 01032324117 | W      | 1992-02-22    |
| `jihoon93@hanmail.net` | 김지훈      | 01023258688 | M      | 1993-02-23    |
| `seoyeons@naver.com`   | 박서연      | 01076482209 | W      | 1993-03-16    |
| `yoonsy94@gmail.com`   | 윤서연      | NULL        | W      | 1994-03-19    |

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| MEMBER_ID            | MEMBER_NAME | GENDER | DATE_OF_BIRTH |
| -------------------- | ----------- | ------ | ------------- |
| `seoyeons@naver.com` | 박서연      | W      | 1993-03-16    |

---

##### 주의사항

`DATE_OF_BIRTH`의 데이트 포맷이 예시와 동일해야 정답처리 됩니다.

## 회고

MySQL 함수들을 통해 날짜 데이터에서 일부만을 추출할 수 있다.

- YEAR() : 연도 추출
- MONTH() : 월 추출
- DAY() : 일 추출
- HOUR() : 시 추출
- MINUTE() : 분 추출
- SECOND() : 초 추출

DATE_FORMAT 함수는 DATETIME의 TYPE을 가진 칼럼의 형식을 수정, 지정해주는 함수이다.

형식: DATE FORMAT(날짜, 출력 형식)

- %Y: 년도 표현 4자리로
- %y: 년도 표현 2자리로
- %M: 월 이름을 Full Name으로 Ex) January ~ December
- %m: 월 이름을 00 ~ 12 숫자로
- %D: 일 이름을 1st, 2nd ... 으로
- %d: 일 이름을 01 ~ 31 숫자로
