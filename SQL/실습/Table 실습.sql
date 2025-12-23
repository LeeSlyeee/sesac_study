-- <실습 1> --

-- 1. 데이터베이스 초기화
-- 기존에 동일한 이름의 데이터베이스가 있다면 삭제하여 실습 환경을 깨끗하게 만듭니다.
DROP DATABASE IF EXISTS ShopDB;
DROP DATABASE IF EXISTS ModelDB;
DROP DATABASE IF EXISTS sqldb;
DROP DATABASE IF EXISTS tabledb;

-- 2. 데이터베이스 생성
-- 'tabledb'라는 이름의 새로운 데이터베이스를 생성합니다.
CREATE DATABASE tabledb;

-- 3. 테이블 생성 (buytbl)
-- `tabledb` 데이터베이스 안에 `buytbl` 테이블을 생성합니다.
-- [주의] 외래 키(Foreign Key)는 참조하는 테이블(usertbl)이 먼저 존재해야 생성할 수 있습니다.
-- 만약 usertbl이 없는 상태에서 아래 코드를 실행하면 에러가 발생합니다.
CREATE TABLE `tabledb`.`buytbl` (
  `num` INT NOT NULL AUTO_INCREMENT, -- 순번: 정수형, 필수(Not Null), 자동 증가(Auto Increment) -> 1, 2, 3...
  `userid` CHAR(8) NOT NULL,         -- 아이디: 고정길이 문자열(8자), 필수
  `prodName` CHAR(6) NOT NULL,       -- 상품명: 고정길이 문자열(6자), 필수
  `groupName` CHAR(4) NULL,          -- 분류: 고정길이 문자열(4자), NULL 허용
  `price` INT NOT NULL,              -- 단가: 정수형, 필수
  `amount` SMALLINT NOT NULL,        -- 수량: 작은 정수형, 필수
  PRIMARY KEY (`num`),               -- `num` 컬럼을 기본키(PK)로 설정
  FOREIGN KEY (userid) REFERENCES usertbl(userID)  
  -- [에러 가능성] usertbl이 아직 생성되지 않았다면 "Table 'tabledb.usertbl' doesn't exist" 에러 발생
);

-- </실습 1> --

-- 간단한 테스트용 테이블 생성 명령
CREATE TABLE test (num INT);

-- <실습 2> --

-- 1. 초기화 및 재설정
-- tabledb를 다시 삭제하고 재생성합니다.
DROP DATABASE tabledb;
CREATE DATABASE tabledb;

USE tabledb; -- 'tabledb'를 현재 사용할 데이터베이스로 지정합니다.

-- 기존 테이블이 있다면 삭제합니다.
DROP TABLE IF EXISTS buytbl, usertbl;

-- 2. 기본 테이블 생성 연습
CREATE TABLE usertbl -- 회원 테이블
( userID  CHAR(8), -- 사용자 아이디
  name    VARCHAR(10), -- 이름 (가변길이 문자열)
  birthYear   INT,  -- 출생년도
  addr	  CHAR(2), -- 지역 (경기,서울,경남 등 2글자)
  mobile1  CHAR(3), -- 휴대폰 국번 (011, 010 등)
  mobile2  CHAR(8), -- 휴대폰 나머지 번호
  height    SMALLINT,  -- 키
  mDate    DATE  -- 회원 가입일 (날짜형)
);

CREATE TABLE buytbl -- 구매 테이블
(  num INT, -- 순번
   userid  CHAR(8),-- 아이디 (FK가 될 예정)
   prodName CHAR(6), -- 물품명
   groupName CHAR(4) , -- 분류
   price     INT , -- 단가
   amount SMALLINT -- 수량
);

-- 3. NULL/NOT NULL 제약조건 실습
USE tabledb;
DROP TABLE IF EXISTS buytbl, usertbl;

CREATE TABLE usertbl 
( userID  CHAR(8) NOT NULL , -- NOT NULL: 반드시 값이 있어야 함. NULL 입력 시 에러 발생.
  name    VARCHAR(10) NOT NULL, 
  birthYear   INT NOT NULL,  
  addr	  CHAR(2) NOT NULL,
  mobile1	CHAR(3) NULL, -- NULL: 값이 없어도 됨 (선택사항)
  mobile2   CHAR(8) NULL, 
  height    SMALLINT NULL, 
  mDate    DATE NULL 
);
CREATE TABLE buytbl 
(  num INT NOT NULL , 
   userid  CHAR(8) NOT NULL ,
   prodName CHAR(6) NOT NULL,
   groupName CHAR(4) NULL , 
   price     INT  NOT NULL,
   amount    SMALLINT  NOT NULL 
);

-- 4. PRIMARY KEY(기본키) 설정 실습
USE tabledb;
DROP TABLE IF EXISTS buytbl, usertbl;

-- 회원 테이블 생성 (기본키 설정 포함)
CREATE TABLE usertbl 
( userID  CHAR(8) NOT NULL PRIMARY KEY, -- userID를 기본키로 설정. 중복된 ID 입력 불가.
  name    VARCHAR(10) NOT NULL, 
  birthYear   INT NOT NULL,  
  addr	  CHAR(2) NOT NULL,
  mobile1	CHAR(3) NULL, 
  mobile2   CHAR(8) NULL, 
  height    SMALLINT NULL, 
  mDate    DATE NULL 
);

-- 구매 테이블 생성 (기본키 설정 포함)
CREATE TABLE buytbl 
(  num INT NOT NULL PRIMARY KEY, -- num을 기본키로 설정
   userid  CHAR(8) NOT NULL ,
   prodName CHAR(6) NOT NULL,
   groupName CHAR(4) NULL , 
   price     INT  NOT NULL,
   amount    SMALLINT  NOT NULL 
);


-- 5. AUTO_INCREMENT(자동 증가) 실습
DROP TABLE IF EXISTS buytbl;
CREATE TABLE buytbl 
(  num INT AUTO_INCREMENT NOT NULL PRIMARY KEY, -- 데이터 입력 시 숫자를 지정하지 않으면(NULL) 자동으로 증가
   userid  CHAR(8) NOT NULL ,
   prodName CHAR(6) NOT NULL,
   groupName CHAR(4) NULL , 
   price     INT  NOT NULL,
   amount    SMALLINT  NOT NULL 
);


-- 6. FOREIGN KEY(외래키) 설정 실습
DROP TABLE IF EXISTS buytbl;
CREATE TABLE buytbl 
(  num INT AUTO_INCREMENT NOT NULL PRIMARY KEY, 
   userid  CHAR(8) NOT NULL ,
   prodName CHAR(6) NOT NULL,
   groupName CHAR(4) NULL , 
   price     INT  NOT NULL,
   amount    SMALLINT  NOT NULL 
   -- buytbl의 userid가 usertbl의 userID를 참조하도록 설정
   -- [제약조건] buytbl에 입력되는 userid는 반드시 usertbl에 존재하는 ID여야 함.
   , FOREIGN KEY(userid) REFERENCES usertbl(userID)
);

-- 7. 데이터 입력 (INSERT)
INSERT INTO usertbl VALUES('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');
INSERT INTO usertbl VALUES('KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4');
INSERT INTO usertbl VALUES('KKH', '김경호', 1971, '전남', '019', '3333333', 177, '2007-7-7');

-- 구매 테이블 데이터 입력 (num은 NULL로 넣으면 자동 증가값 적용)
INSERT INTO buytbl VALUES(NULL, 'KBS', '운동화', NULL, 30, 2);
INSERT INTO buytbl VALUES(NULL, 'KBS', '노트북', '전자', 1000, 1);
-- [오류 발생 가능성] JYP는 아직 usertbl에 등록되지 않은 사용자입니다.
-- 외래키 제약조건 위배로 에러가 발생할 수 있습니다. (Cannot add or update a child row...)
INSERT INTO buytbl VALUES(NULL, 'JYP', '모니터', '전자', 200, 1); 

-- 추가 사용자 입력 (이제 JYP 등 등록)
INSERT INTO usertbl VALUES('JYP', '조용필', 1950, '경기', '011', '4444444', 166, '2009-4-4');
INSERT INTO usertbl VALUES('SSK', '성시경', 1979, '서울', NULL  , NULL      , 186, '2013-12-12');
INSERT INTO usertbl VALUES('LJB', '임재범', 1963, '서울', '016', '6666666', 182, '2009-9-9');
INSERT INTO usertbl VALUES('YJS', '윤종신', 1969, '경남', NULL  , NULL      , 170, '2005-5-5');
INSERT INTO usertbl VALUES('EJW', '은지원', 1972, '경북', '011', '8888888', 174, '2014-3-3');
INSERT INTO usertbl VALUES('JKW', '조관우', 1965, '경기', '018', '9999999', 172, '2010-10-10');
INSERT INTO usertbl VALUES('BBK', '바비킴', 1973, '서울', '010', '0000000', 176, '2013-5-5');

-- 추가 구매 데이터 입력 (이제 사용자 정보가 다 있으므로 성공)
INSERT INTO buytbl VALUES(NULL, 'JYP', '모니터', '전자', 200,  1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '모니터', '전자', 200,  5);
INSERT INTO buytbl VALUES(NULL, 'KBS', '청바지', '의류', 50,   3);
INSERT INTO buytbl VALUES(NULL, 'BBK', '메모리', '전자', 80,  10);
INSERT INTO buytbl VALUES(NULL, 'SSK', '책'    , '서적', 15,   5);
INSERT INTO buytbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   2);
INSERT INTO buytbl VALUES(NULL, 'EJW', '청바지', '의류', 50,   1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);
INSERT INTO buytbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);


-- </실습 2> --

-- 8. 제약조건(Constraint) 상세 실습
USE tabledb;
DROP TABLE IF EXISTS buytbl, usertbl;

-- 기본 키를 정의하는 방법 1 : 컬럼 정의 옆에 바로 기술
CREATE TABLE usertbl 
( userID  CHAR(8) NOT NULL PRIMARY KEY, 
  name    VARCHAR(10) NOT NULL, 
  birthYear   INT NOT NULL
);

DESCRIBE usertbl; -- 테이블 구조 확인 명령

-- 기본 키를 정의하는 방법 2 : CONSTRAINT 키워드로 이름 지정
DROP TABLE IF EXISTS usertbl;
CREATE TABLE usertbl 
( userID  CHAR(8) NOT NULL, 
  name    VARCHAR(10) NOT NULL, 
  birthYear   INT NOT NULL,  
  CONSTRAINT PRIMARY KEY PK_usertbl_userID (userID) -- PK 이름을 'PK_usertbl_userID'로 지정
);

-- 기본 키를 정의하는 방법 3 : 테이블 생성 후 ALTER TABLE 사용
DROP TABLE IF EXISTS usertbl;
CREATE TABLE usertbl 
(   userID  CHAR(8) NOT NULL, 
    name    VARCHAR(10) NOT NULL, 
    birthYear   INT NOT NULL
);
ALTER TABLE usertbl
     ADD CONSTRAINT PK_usertbl_userID 
     PRIMARY KEY (userID);


-- [복합키(Composite Primary Key) 실습]
-- 두 개 이상의 컬럼을 합쳐서 하나의 기본키로 설정하는 경우
DROP TABLE IF EXISTS prodTbl;
CREATE TABLE prodTbl
( prodCode CHAR(3) NOT NULL,
  prodID   CHAR(4)  NOT NULL,
  prodDate DATETIME  NOT NULL,
  prodCur  CHAR(10) NULL
);
-- prodCode + prodID 조합이 유일해야 함
ALTER TABLE prodTbl
	ADD CONSTRAINT PK_prodTbl_proCode_prodID 
	PRIMARY KEY (prodCode, prodID) ;

-- 테이블 생성 시 복합키 지정
DROP TABLE IF EXISTS prodTbl;
CREATE TABLE prodTbl
( prodCode CHAR(3) NOT NULL,
  prodID   CHAR(4)  NOT NULL,
  prodDate DATETIME  NOT NULL,
  prodCur  CHAR(10) NULL,
  CONSTRAINT PK_prodTbl_proCode_prodID 
	PRIMARY KEY (prodCode, prodID) 
);

SHOW INDEX FROM prodTbl; -- 인덱스 정보를 보면 두 컬럼이 PK로 잡힌 것을 확인 가능

-- [외래키(Foreign Key) 제약조건 옵션 실습]
DROP TABLE IF EXISTS buytbl, usertbl;
CREATE TABLE usertbl 
( userID  CHAR(8) NOT NULL PRIMARY KEY, 
  name    VARCHAR(10) NOT NULL, 
  birthYear   INT NOT NULL 
);
CREATE TABLE buytbl 
(  num INT AUTO_INCREMENT NOT NULL PRIMARY KEY , 
   userID  CHAR(8) NOT NULL, 
   prodName CHAR(6) NOT NULL,
   FOREIGN KEY(userID) REFERENCES usertbl(userID)
);


-- 외래키에 이름을 명시적으로 지정하여 생성
DROP TABLE IF EXISTS buytbl;
CREATE TABLE buytbl 
(  num INT AUTO_INCREMENT NOT NULL PRIMARY KEY , 
   userID  CHAR(8) NOT NULL, 
   prodName CHAR(6) NOT NULL,
   CONSTRAINT FK_usertbl_buytbl FOREIGN KEY(userID) REFERENCES usertbl(userID)
);


-- ALTER TABLE로 외래키 나중에 추가
DROP TABLE IF EXISTS buytbl;
CREATE TABLE buytbl 
(  num INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
   userID  CHAR(8) NOT NULL, 
   prodName CHAR(6) NOT NULL 
);
ALTER TABLE buytbl
    ADD CONSTRAINT FK_usertbl_buytbl 
    FOREIGN KEY (userID) 
    REFERENCES usertbl(userID);

SHOW INDEX FROM buytbl ;

-- 외래키 삭제 후 옵션(ON UPDATE CASCADE) 추가
ALTER TABLE buytbl
	DROP FOREIGN KEY FK_usertbl_buytbl; -- 이름을 알아야 삭제 가능
ALTER TABLE buytbl
	ADD CONSTRAINT FK_usertbl_buytbl
	FOREIGN KEY (userID)
	REFERENCES usertbl (userID)
	ON UPDATE CASCADE; -- 부모 테이블(usertbl)에서 ID가 변경되면 자식 테이블(buytbl)도 자동 변경됨

-- 9. UNIQUE 제약조건 실습
-- 중복된 값은 입력할 수 없지만, NULL은 허용할 수 있음 (단, PK는 NULL 불가)
USE tabledb;
DROP TABLE IF EXISTS buytbl, usertbl;
CREATE TABLE usertbl 
( userID  CHAR(8) NOT NULL PRIMARY KEY, 
  name    VARCHAR(10) NOT NULL, 
  birthYear   INT NOT NULL,  
  email   CHAR(30) NULL  UNIQUE -- 이메일은 유일해야 함. 중복 입력 시 에러.
);

-- UNIQUE 제약조건 이름 지정
DROP TABLE IF EXISTS usertbl;
CREATE TABLE usertbl 
( userID  CHAR(8) NOT NULL PRIMARY KEY,
  name    VARCHAR(10) NOT NULL, 
  birthYear   INT NOT NULL,  
  email   CHAR(30) NULL ,  
  CONSTRAINT AK_email  UNIQUE (email) -- 대체키(Alternate Key)로 사용
);

-- 10. CHECK 제약조건 실습 (데이터 유효성 검사)
-- 입력되는 데이터가 특정 조건을 만족하는지 검사
DROP TABLE IF EXISTS usertbl;
CREATE TABLE usertbl 
( userID  CHAR(8) PRIMARY KEY,
  name    VARCHAR(10) , 
  birthYear  INT CHECK  (birthYear >= 1900 AND birthYear <= 2023), -- 1900~2023 사이 값만 허용
  mobile1	char(3) NULL, 
  CONSTRAINT CK_name CHECK ( name IS NOT NULL)  -- 이름은 NULL일 수 없음 (NOT NULL과 유사 효과)
);

-- 휴대폰 국번에 대한 체크 제약조건 추가
ALTER TABLE usertbl
	ADD CONSTRAINT CK_mobile1
	CHECK  (mobile1 IN ('010','011','016','017','018','019')) ; -- 지정된 목록 중 하나여야 함

-- 11. DEFAULT 정의 실습 (기본값)
DROP TABLE IF EXISTS usertbl;
CREATE TABLE usertbl 
( userID  	CHAR(8) NOT NULL PRIMARY KEY,  
  name    	VARCHAR(10) NOT NULL, 
  birthYear	INT NOT NULL DEFAULT -1,      -- 값이 없으면 -1 자동 입력
  addr	  	CHAR(2) NOT NULL DEFAULT '서울', -- 값이 없으면 '서울' 자동 입력
  mobile1	CHAR(3) NULL, 
  mobile2	CHAR(8) NULL, 
  height	SMALLINT NULL DEFAULT 170,    -- 값이 없으면 170 자동 입력
  mDate    	DATE NULL
);


-- ALTER TABLE로 DEFAULT 값 설정
DROP TABLE IF EXISTS usertbl;
CREATE TABLE usertbl 
( userID  	CHAR(8) NOT NULL PRIMARY KEY,  
  name    	VARCHAR(10) NOT NULL, 
  birthYear	INT NOT NULL,
  addr	  	CHAR(2) NOT NULL,
  mobile1	CHAR(3) NULL, 
  mobile2	CHAR(8) NULL, 
  height	SMALLINT NULL, 
  mDate    	DATE NULL
);
ALTER TABLE usertbl
	ALTER COLUMN birthYear SET DEFAULT -1;
ALTER TABLE usertbl
	ALTER COLUMN addr SET DEFAULT '서울';
ALTER TABLE usertbl
	ALTER COLUMN height SET DEFAULT 170;

-- DEFAULT 값 적용 테스트
-- default 키워드 명시
INSERT INTO usertbl VALUES ('LHL', '이혜리', default, default, '011', '1234567', default, '2023.12.12');
-- 컬럼명 생략 시 자동으로 default 값 적용
INSERT INTO usertbl(userID, name) VALUES('KAY', '김아영');
-- 값을 직접 입력하면 default 무시
INSERT INTO usertbl VALUES ('WB', '원빈', 1982, '대전', '019', '9876543', 176, '2020.5.5');
SELECT * FROM usertbl;


-- <실습 3> --

-- 1. 테이블 압축(Compression) 실습
CREATE DATABASE IF NOT EXISTS compressDB;
USE compressDB;

-- 일반 테이블
CREATE TABLE normalTBL( emp_no int , first_name varchar(14));

-- 압축 테이블 (ROW_FORMAT=COMPRESSED)
CREATE TABLE compressTBL( emp_no int , first_name varchar(14))
	ROW_FORMAT=COMPRESSED ;

-- 대량 데이터 입력 테스트 (employees DB가 존재해야 함)
INSERT INTO normalTbl 
     SELECT emp_no, first_name FROM employees.employees;   
INSERT INTO compressTBL 
     SELECT emp_no, first_name FROM employees.employees;

-- 상태 확인 (Data_length 비교)
SHOW TABLE STATUS FROM compressDB;

DROP DATABASE IF EXISTS compressDB;

-- </실습 3> --



-- <실습 4> --


-- Workbench 1
-- 임시 테이블(Temporary Table) 실습
-- 세션(연결)이 유지되는 동안만 존재하고, 연결이 끊기면 자동 삭제됩니다.

USE employees;
CREATE TEMPORARY TABLE  IF NOT EXISTS  temptbl (id INT, name CHAR(5));
-- 기존 employees 테이블과 이름이 같으면 임시 테이블이 우선됩니다.
CREATE TEMPORARY TABLE  IF NOT EXISTS employees (id INT, name CHAR(5));

DESCRIBE temptbl;
DESCRIBE employees; -- 여기서 employees는 임시 테이블입니다.

INSERT INTO temptbl VALUES (1, 'This');
INSERT INTO employees VALUES (2, 'MySQL');

SELECT * FROM temptbl;
SELECT * FROM employees; 

-- Workbench 2 (가상 시나리오: 새 세션 접속)
-- 새 창이나 다른 세션에서는 위에서 만든 임시 테이블이 보이지 않습니다.
USE employees;
SELECT * FROM temptbl; -- [오류 발생] Table 'employees.temptbl' doesn't exist
SELECT * FROM employees; -- 원래의 employees 테이블(정식 테이블)이 조회됩니다.

-- Workbench 1 (다시 돌아옴)
DROP TABLE temptbl; 

USE employees;
SELECT * FROM employees; -- 임시 테이블 employees가 아직 남아있으므로 그것이 조회됩니다.

-- </실습 4> --


-- 테이블 구조 변경 (ALTER TABLE) 실습
USE tabledb;
-- 열 추가
ALTER TABLE usertbl
	ADD homepage VARCHAR(30)  
		DEFAULT 'http://www.hanbit.co.kr'
		NULL; 

-- 열 삭제 (데이터가 있으면 데이터도 함께 삭제됨)
ALTER TABLE usertbl
	DROP COLUMN mobile1;

-- 열 이름/타입 변경
ALTER TABLE usertbl
	CHANGE COLUMN name uName VARCHAR(20) NULL ;

-- PK 삭제
-- [오류 주의] 다른 테이블에서 이 PK를 참조(FK)하고 있다면 삭제가 불가능합니다.
ALTER TABLE usertbl
	DROP PRIMARY KEY; 

-- FK 삭제
ALTER TABLE buytbl
	DROP FOREIGN KEY buytbl_ibfk_1; 


-- <실습 5> --

-- 1. 데이터 무결성과 제약조건 동작 확인 실습 (심화)
USE tabledb;
DROP TABLE IF EXISTS buytbl, usertbl;

CREATE TABLE usertbl 
( userID  CHAR(8), 
  name    VARCHAR(10),
  birthYear   INT,  
  addr	  CHAR(2), 
  mobile1	CHAR(3), 
  mobile2   CHAR(8), 
  height    SMALLINT, 
  mDate    DATE 
);
CREATE TABLE buytbl 
(  num int AUTO_INCREMENT PRIMARY KEY,
   userid  CHAR(8),
   prodName CHAR(6),
   groupName CHAR(4),
   price     INT ,
   amount   SMALLINT
);

-- 초기 데이터 입력 (제약조건이 없는 상태)
INSERT INTO usertbl VALUES('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');
INSERT INTO usertbl VALUES('KBS', '김범수', NULL, '경남', '011', '2222222', 173, '2012-4-4');
INSERT INTO usertbl VALUES('KKH', '김경호', 1871, '전남', '019', '3333333', 177, '2007-7-7');
INSERT INTO usertbl VALUES('JYP', '조용필', 1950, '경기', '011', '4444444', 166, '2009-4-4');

INSERT INTO buytbl VALUES(NULL, 'KBS', '운동화', NULL   , 30,   2);
INSERT INTO buytbl VALUES(NULL,'KBS', '노트북', '전자', 1000, 1);
INSERT INTO buytbl VALUES(NULL,'JYP', '모니터', '전자', 200,  1);
INSERT INTO buytbl VALUES(NULL,'BBK', '모니터', '전자', 200,  5); 
-- [상황] BBK는 usertbl에 없는 ID입니다. 하지만 현재 FK 제약조건이 없어서 입력이 허용됩니다.
-- 이것이 '무결성 위배' 상태입니다.


-- 2. 제약조건 추가 시도 및 오류 경험
-- PK 추가
ALTER TABLE usertbl
	ADD CONSTRAINT PK_usertbl_userID
	PRIMARY KEY (userID);

DESC usertbl;

-- FK 추가
-- [오류 발생] "Cannot add or update a child row: a foreign key constraint fails..."
-- 이유: buytbl에 'BBK'라는 데이터가 있는데, 부모 테이블 usertbl에는 'BBK'가 없습니다.
-- 기존 데이터가 이미 제약조건을 위반하고 있으므로 제약조건 추가가 실패합니다.
ALTER TABLE buytbl
	ADD CONSTRAINT FK_usertbl_buytbl
	FOREIGN KEY (userID)
	REFERENCES usertbl (userID);

-- 오류 해결: 문제가 되는 자식 데이터(BBK) 삭제
DELETE FROM buytbl WHERE userid = 'BBK';

-- 다시 FK 추가 시도 -> 성공
ALTER TABLE buytbl
	ADD CONSTRAINT FK_usertbl_buytbl
	FOREIGN KEY (userID)
	REFERENCES usertbl (userID);

-- 3. 데이터 입력과 제약조건 체크
-- FK가 걸려있으므로 없는 ID 입력 시 에러 발생
-- [오류 발생] usertbl에 없는 'BBK' 사용 시도 -> 에러
INSERT INTO buytbl VALUES(NULL,'BBK', '모니터', '전자', 200,  5); 

-- 4. 외래키 체크 일시 비활성화 (위험하지만 강력한 기능)
SET foreign_key_checks = 0; -- 체크 기능을 끔
-- [입력 성공] 체크가 꺼져 있어서 BBK 입력이 가능해짐 (무결성은 깨진 상태)
INSERT INTO buytbl VALUES(NULL, 'BBK', '모니터', '전자', 200,  5);
INSERT INTO buytbl VALUES(NULL, 'KBS', '청바지', '의류', 50,   3);
INSERT INTO buytbl VALUES(NULL, 'BBK', '메모리', '전자', 80,  10);
INSERT INTO buytbl VALUES(NULL, 'SSK', '책'    , '서적', 15,   5);
INSERT INTO buytbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   2);
INSERT INTO buytbl VALUES(NULL, 'EJW', '청바지', '의류', 50,   1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);
INSERT INTO buytbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);
SET foreign_key_checks = 1; -- 다시 활성화 (이제부터는 다시 검사함)

-- 5. CHECK 제약조건 추가 및 위배 데이터 충돌
-- 조건: birthYear는 1900~2023, NULL 불가
-- [오류 발생 예상] 이미 입력된 데이터 중 NULL이나 1871년생이 있어서 제약조건 추가 실패
ALTER TABLE userTBL
	ADD CONSTRAINT CK_birthYear
	CHECK ( (birthYear >= 1900 AND birthYear <= 2023) AND (birthYear IS NOT NULL) );

-- 문제 데이터 수정
UPDATE usertbl SET birthYear=1979 WHERE userID='KBS'; -- NULL -> 1979
UPDATE usertbl SET birthYear=1971 WHERE userID='KKH'; -- 1871 -> 1971

-- 다시 CHECK 제약조건 추가 -> 성공
ALTER TABLE userTBL
	ADD CONSTRAINT CK_birthYear
	CHECK ( (birthYear >= 1900 AND birthYear <= 2023) AND (birthYear IS NOT NULL) );
    
-- 위배 데이터 입력 테스트
-- [오류 발생] 2999년은 범위 밖이므로 에러 (Check constraint 'CK_birthYear' is violated)
INSERT INTO usertbl VALUES('TKV', '태권뷔', 2999, '우주', NULL  , NULL , 186, '2023-12-12');

-- 정상 데이터 추가 입력 (누락된 회원들 마저 입력)
-- BBK(바비킴) 데이터가 여기서 드디어 들어옴 -> buytbl의 BBK 데이터와 연결됨
INSERT INTO usertbl VALUES('SSK', '성시경', 1979, '서울', NULL  , NULL , 186, '2013-12-12');
INSERT INTO usertbl VALUES('LJB', '임재범', 1963, '서울', '016', '6666666', 182, '2009-9-9');
INSERT INTO usertbl VALUES('YJS', '윤종신', 1969, '경남', NULL  , NULL , 170, '2005-5-5');
INSERT INTO usertbl VALUES('EJW', '은지원', 1972, '경북', '011', '8888888', 174, '2014-3-3');
INSERT INTO usertbl VALUES('JKW', '조관우', 1965, '경기', '018', '9999999', 172, '2010-10-10');
INSERT INTO usertbl VALUES('BBK', '바비킴', 1973, '서울', '010', '0000000', 176, '2013-5-5');

-- 6. ON UPDATE CASCADE 실습
-- BBK 아이디를 VVK로 변경 시도
-- [오류 발생] buytbl이 BBK를 참조하고 있는데, CASCADE 옵션이 없어서 변경 금지됨
UPDATE usertbl SET userID = 'VVK' WHERE userID='BBK'; 

-- (테스트를 위해) 외래키 체크 끄고 강제 변경
SET foreign_key_checks = 0;
UPDATE usertbl SET userID = 'VVK' WHERE userID='BBK';
SET foreign_key_checks = 1;

-- 결과 확인: usertbl엔 VVK, buytbl엔 BBK가 있어서 조인이 안 됨 (데이터 불일치)
SELECT B.userid, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2)  AS '연락처'
   FROM buytbl B
     INNER JOIN usertbl U
        ON B.userid = U.userid ; -- VVK 구매 내역은 조회되지 않음

-- 불일치 상황 확인
SELECT * FROM buytbl WHERE userid='BBK'; -- 구매 내역 있음

-- 원상 복구
SET foreign_key_checks = 0;
UPDATE usertbl SET userID = 'BBK' WHERE userID='VVK';
SET foreign_key_checks = 1;

-- ON UPDATE CASCADE 적용
ALTER TABLE buytbl
	DROP FOREIGN KEY FK_usertbl_buytbl;
ALTER TABLE buytbl 
	ADD CONSTRAINT FK_usertbl_buytbl
		FOREIGN KEY (userID)
		REFERENCES usertbl (userID)
		ON UPDATE CASCADE; -- 회원 ID 바뀌면 구매내역 ID도 같이 바뀜

-- 다시 변경 시도 -> 성공
UPDATE usertbl SET userID = 'VVK' WHERE userID='BBK';

-- 확인: 구매내역도 자동으로 VVK로 바뀌어서 조인 성공
SELECT B.userid, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2) AS '연락처'
   FROM buytbl B
     INNER JOIN usertbl U
        ON B.userid = U.userid
  ORDER BY B.userid;


-- 7. ON DELETE CASCADE 실습
-- 회원 삭제 시도
-- [오류 발생] VVK가 구매한 내역이 있어서 삭제 안 됨 (ON DELETE RESTRICT가 기본 동작)
DELETE FROM usertbl WHERE userID = 'VVK';

-- ON DELETE CASCADE 추가
ALTER TABLE buytbl
	DROP FOREIGN KEY FK_usertbl_buytbl;
ALTER TABLE buytbl 
	ADD CONSTRAINT FK_usertbl_buytbl
		FOREIGN KEY (userID)
		REFERENCES usertbl (userID)
		ON UPDATE CASCADE
		ON DELETE CASCADE; -- 회원 삭제 시 구매내역도 같이 삭제

-- 다시 삭제 시도 -> 성공
-- usertbl에서 VVK 삭제됨 + buytbl에서 VVK 구매내역도 자동 삭제됨
DELETE FROM usertbl WHERE userID = 'VVK';

-- 결과 확인 (VVK 구매데이터가 사라짐)
SELECT * FROM buytbl ;

-- 마무리
ALTER TABLE usertbl
	DROP COLUMN birthYear ;

-- </실습 5> --
