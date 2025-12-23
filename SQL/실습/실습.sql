<실습 >

USE employees;

USE mysql;
SELECT * FROM employees;

-- [오류 발생 가능성]
-- 현재 선택된 데이터베이스는 'mysql'입니다.
-- 'mysql' 데이터베이스에는 'titles'라는 테이블이 없으므로 에러가 발생할 수 있습니다.
-- 해결: SELECT * FROM employees.titles; 와 같이 데이터베이스를 명시하거나 USE employees; 레를 먼저 실행해야 합니다.
SELECT * FROM titles ;

-- 'employees' 데이터베이스의 'titles' 테이블을 명시적으로 조회하므로 정상 실행됩니다.
SELECT * FROM employees.titles;

SELECT * FROM employees.titles;
SELECT * FROM titles; -- 여전히 현재 DB가 mysql이라면 에러 발생

SELECT first_name FROM employees;

SELECT first_name, last_name, gender FROM employees;

-- 한줄 주석 연습
SELECT first_name, last_name, gender -- 이름과 성별 열을 가져옴
FROM employees;

/* 블록 주석 연습
SELECT first_name, last_name, gender
FROM employees;
*/



-- <실습 1> --

-- 현재 서버에 있는 데이터베이스 정보 조회
SHOW DATABASES;

-- 사용할 데이터베이스 지정
USE employees;

-- 현재 선택된 데이터베이스의 테이블 정보 조회
SHOW TABLE STATUS;

-- 테이블 이름만 간단히 조회
SHOW TABLES; 

-- employees 테이블의 구조(컬럼 정보) 조회
DESCRIBE employees; -- 또는 DESC employees;

SELECT first_name, gender FROM employees;

-- </실습 1> --

-- AS(Alias): 컬럼명에 별칭 부여. 공백이 포함된 별칭은 작은따옴표('')로 감싸야 함
SELECT first_name AS 이름 , gender 성별, hire_date '회사 입사일'
FROM employees;

-- <실습 2> --

DROP DATABASE IF EXISTS sqldb; -- 만약 sqldb가 존재하면 우선 삭제한다.
CREATE DATABASE sqldb;

USE sqldb;
CREATE TABLE usertbl -- 회원 테이블
( userID  	CHAR(8) NOT NULL PRIMARY KEY, -- 사용자 아이디(PK)
  name    	VARCHAR(10) NOT NULL, -- 이름
  birthYear   INT NOT NULL,  -- 출생년도
  addr	  	CHAR(2) NOT NULL, -- 지역(경기,서울,경남 식으로 2글자만입력)
  mobile1	CHAR(3), -- 휴대폰의 국번(011, 016, 017, 018, 019, 010 등)
  mobile2	CHAR(8), -- 휴대폰의 나머지 전화번호(하이픈제외)
  height    	SMALLINT,  -- 키
  mDate    	DATE  -- 회원 가입일
);
CREATE TABLE buytbl -- 회원 구매 테이블(Buy Table의 약자)
(  num 		INT AUTO_INCREMENT NOT NULL PRIMARY KEY, -- 순번(PK)
   userID  	CHAR(8) NOT NULL, -- 아이디(FK)
   prodName 	CHAR(6) NOT NULL, --  물품명
   groupName 	CHAR(4)  , -- 분류
   price     	INT  NOT NULL, -- 단가
   amount    	SMALLINT  NOT NULL, -- 수량
   FOREIGN KEY (userID) REFERENCES usertbl(userID)
);

INSERT INTO usertbl VALUES('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');
INSERT INTO usertbl VALUES('KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4');
INSERT INTO usertbl VALUES('KKH', '김경호', 1971, '전남', '019', '3333333', 177, '2007-7-7');
INSERT INTO usertbl VALUES('JYP', '조용필', 1950, '경기', '011', '4444444', 166, '2009-4-4');
INSERT INTO usertbl VALUES('SSK', '성시경', 1979, '서울', NULL  , NULL      , 186, '2013-12-12');
INSERT INTO usertbl VALUES('LJB', '임재범', 1963, '서울', '016', '6666666', 182, '2009-9-9');
INSERT INTO usertbl VALUES('YJS', '윤종신', 1969, '경남', NULL  , NULL      , 170, '2005-5-5');
INSERT INTO usertbl VALUES('EJW', '은지원', 1972, '경북', '011', '8888888', 174, '2014-3-3');
INSERT INTO usertbl VALUES('JKW', '조관우', 1965, '경기', '018', '9999999', 172, '2010-10-10');
INSERT INTO usertbl VALUES('BBK', '바비킴', 1973, '서울', '010', '0000000', 176, '2013-5-5');
INSERT INTO buytbl VALUES(NULL, 'KBS', '운동화', NULL   , 30,   2);
INSERT INTO buytbl VALUES(NULL, 'KBS', '노트북', '전자', 1000, 1);
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

SELECT * FROM usertbl;
SELECT * FROM buytbl;


/*
source C:\SQL\sqldb.sql
exit
*/

-- </실습 2> --


USE  sqldb;
SELECT * FROM usertbl;

-- 기본 WHERE 절: 이름이 '김경호'인 행 조회
SELECT * FROM usertbl WHERE name = '김경호';

-- AND 연산자: 1970년 이후 출생이고 키가 182 이상인 사람
SELECT userID, Name FROM usertbl WHERE birthYear >= 1970 AND height >= 182;

-- OR 연산자: 1970년 이후 출생이거나 키가 182 이상인 사람
SELECT userID, Name FROM usertbl WHERE birthYear >= 1970 OR height >= 182;

-- 범위 조회 (AND 사용)
SELECT name, height FROM usertbl WHERE height >= 180 AND height <= 183;

-- BETWEEN ... AND ... : 연속된 범위 조회에 사용
SELECT name, height FROM usertbl WHERE height BETWEEN 180 AND 183;

-- OR 연산자로 여러 지역 조회
SELECT name, addr FROM usertbl WHERE addr='경남' OR  addr='전남' OR addr='경북';

-- IN() : 이산적인 값들 중 하나에 해당하는지 조회
SELECT name, addr FROM usertbl WHERE addr IN ('경남','전남','경북');

-- LIKE : 문자열 패턴 매칭 ('김%' : 김으로 시작하는 모든 문자열)
SELECT name, height FROM usertbl WHERE name LIKE '김%';

-- LIKE : ('_종신' : 앞 한 글자는 무엇이든 상관없고 뒤가 '종신'인 문자열)
SELECT name, height FROM usertbl WHERE name LIKE '_종신';

-- 서브쿼리(SubQuery) 학습
SELECT name, height FROM usertbl WHERE height  > 177;

-- '김경호'의 키보다 큰 사람 조회. 서브쿼리가 먼저 실행되어 김경호의 키(177)를 반환함
SELECT name, height FROM usertbl 
   WHERE height > (SELECT height FROM usertbl WHERE Name = '김경호');

-- [오류 발생 가능성]
-- 서브쿼리 결과가 2개 이상(경남인 사람이 여러 명)이면 비교 연산자(>=)만으로는 에러 발생
-- 해결: ANY, ALL 등의 키워드 필요
SELECT name, height FROM usertbl 
   WHERE height >= (SELECT height FROM usertbl WHERE addr = '경남');

-- ANY: 서브쿼리 결과 중 하나라도 만족하면 참 (즉, 최소값보다 크거나 같으면 됨 -> 170 이상)
SELECT name, height FROM usertbl 
   WHERE height >= ANY (SELECT height FROM usertbl WHERE addr = '경남');

-- ALL: 서브쿼리 결과 모두를 만족해야 참 (즉, 최대값보다 크거나 같아야 함 -> 173 이상)
SELECT name, height FROM usertbl 
   WHERE height >= ALL (SELECT height FROM usertbl WHERE addr = '경남');

-- = ANY : IN() 과 동일한 효과
SELECT name, height FROM usertbl 
   WHERE height = ANY (SELECT height FROM usertbl WHERE addr = '경남');
   
-- IN() : 서브쿼리 결과에 포함되는 값 찾기
SELECT name, height FROM usertbl 
  WHERE height IN (SELECT height FROM usertbl WHERE addr = '경남');

SELECT name, mDate FROM usertbl ORDER BY mDate;

SELECT name, mDate FROM usertbl ORDER BY mDate DESC;

SELECT name, height FROM usertbl ORDER BY height DESC, name ASC;

SELECT addr FROM usertbl;

SELECT addr FROM usertbl ORDER BY addr;

SELECT DISTINCT addr FROM usertbl;

USE employees;
SELECT emp_no, hire_date FROM employees 
   ORDER BY hire_date ASC;

USE employees;
SELECT emp_no, hire_date FROM employees 
   ORDER BY hire_date ASC
   LIMIT 5;

SELECT emp_no, hire_date FROM employees 
   ORDER BY hire_date ASC
   LIMIT 0, 5;  -- LIMIT 5 OFFSET 0 과 동일

USE sqldb;
CREATE TABLE buytbl2 (SELECT * FROM buytbl);
SELECT * FROM buytbl2;

CREATE TABLE buytbl3 (SELECT userID, prodName FROM buytbl);
SELECT * FROM buytbl3;

SELECT userID, amount FROM buytbl ORDER BY userID;

SELECT userID, SUM(amount) FROM buytbl GROUP BY userID;

SELECT userID AS '사용자 아이디', SUM(amount) AS '총 구매 개수'  
   FROM buytbl GROUP BY userID;

SELECT userID AS '사용자 아이디', SUM(price*amount) AS '총 구매액'  
   FROM buytbl GROUP BY userID;

USE sqldb;
SELECT AVG(amount) AS '평균 구매 개수' FROM buytbl ;

SELECT userID, AVG(amount) AS '평균 구매 개수' FROM buytbl  GROUP BY userID;

SELECT name, MAX(height), MIN(height) FROM usertbl;

SELECT name, MAX(height), MIN(height) FROM usertbl GROUP BY Name;

SELECT name, height
   FROM usertbl 
   WHERE height = (SELECT MAX(height)FROM usertbl) 
       OR height = (SELECT MIN(height)FROM usertbl) ;

SELECT COUNT(*) FROM usertbl;

SELECT COUNT(mobile1) AS '휴대폰이 있는 사용자' FROM usertbl;

USE sqldb;
-- 기본적인 GROUP BY: 사용자별 총 구매액
SELECT userID AS '사용자', SUM(price*amount) AS '총구매액'  
   FROM buytbl 
   GROUP BY userID ;

-- [오류 발생] WHERE 절에 집계 함수 사용 불가
-- 오류 내용: Invalid use of group function
-- 이유: WHERE 절은 그룹화하기 '전'에 필터링을 수행하므로, 그룹화가 필요한 SUM() 함수를 사용할 수 없습니다.
-- 해결: GROUP BY 다음에 오는 HAVING 절을 사용해야 합니다.
SELECT userID AS '사용자', SUM(price*amount) AS '총구매액'  
   FROM buytbl 
   WHERE SUM(price*amount) > 1000 
   GROUP BY userID ;

-- 정상 쿼리: HAVING 절 사용
SELECT userID AS '사용자', SUM(price*amount) AS '총구매액'  
   FROM buytbl 
   GROUP BY userID
   HAVING SUM(price*amount) > 1000 ;

-- ORDER BY는 맨 마지막에 위치해야 함
SELECT userID AS '사용자', SUM(price*amount) AS '총구매액'  
   FROM buytbl 
   GROUP BY userID
   HAVING SUM(price*amount) > 1000 
   ORDER BY SUM(price*amount) ;

-- WITH ROLLUP: 그룹별 중간 합계와 총 합계를 구해줌
SELECT num, groupName, SUM(price * amount) AS '비용' 
   FROM buytbl
   GROUP BY  groupName, num
   WITH ROLLUP;

SELECT groupName, SUM(price * amount) AS '비용' 
   FROM buytbl
   GROUP BY  groupName
   WITH ROLLUP;

USE sqldb;
CREATE TABLE testTbl1 (id  int, userName char(3), age int);
INSERT INTO testTbl1 VALUES (1, '홍길동', 25);

INSERT INTO testTbl1(id, userName) VALUES (2, '설현');

INSERT INTO testTbl1(userName, age, id) VALUES ('하니', 26,  3);

USE  sqldb;
CREATE TABLE testTbl2 
  (id  int AUTO_INCREMENT PRIMARY KEY, 
   userName char(3), 
   age int );
INSERT INTO testTbl2 VALUES (NULL, '지민', 25);
INSERT INTO testTbl2 VALUES (NULL, '유나', 22);
INSERT INTO testTbl2 VALUES (NULL, '유경', 21);
SELECT * FROM testTbl2;

SELECT LAST_INSERT_ID(); 

ALTER TABLE testTbl2 AUTO_INCREMENT=100;
INSERT INTO testTbl2 VALUES (NULL, '찬미', 23);
SELECT * FROM testTbl2;

USE  sqldb;
CREATE TABLE testTbl3 
  (id  int AUTO_INCREMENT PRIMARY KEY, 
   userName char(3), 
   age int );
ALTER TABLE testTbl3 AUTO_INCREMENT=1000;
SET @@auto_increment_increment=3;
INSERT INTO testTbl3 VALUES (NULL, '나연', 20);
INSERT INTO testTbl3 VALUES (NULL, '정연', 18);
INSERT INTO testTbl3 VALUES (NULL, '모모', 19);
SELECT * FROM testTbl3;

USE sqldb;
CREATE TABLE testTbl4 (id int, Fname varchar(50), Lname varchar(50));
INSERT INTO testTbl4 
  SELECT emp_no, first_name, last_name
    FROM employees.employees ;

USE sqldb;
CREATE TABLE testTbl5 
   (SELECT emp_no, first_name, last_name  FROM employees.employees) ;

-- 데이터 수정 (UPDATE)
UPDATE testTbl4
    SET Lname = '없음'
    WHERE Fname = 'Kyoichi';

USE sqldb;
-- [주의/오류 가능성] WHERE 절 없는 UPDATE
-- MySQL의 'Safe Update' 모드가 켜져 있다면, Key 컬럼을 이용한 WHERE 절 없이 전체 테이블을 업데이트하려 할 때 에러를 발생시킬 수 있습니다.
-- 에러 메시지: You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column
UPDATE buytbl SET price = price * 1.5 ;

USE sqldb;
-- [오류 가능성] Safe Update 모드에 걸릴 수 있음
DELETE FROM testTbl4 WHERE Fname = 'Aamer';

-- LIMIT을 사용하면 일부 Safe Update 제한을 우회할 수도 있지만 시스템 설정에 따름
DELETE FROM testTbl4 WHERE Fname = 'Aamer'  LIMIT 5;


-- <실습 3> : 대용량 테이블 삭제 비교 --

USE sqldb;
CREATE TABLE bigTbl1 (SELECT * FROM employees.employees);
CREATE TABLE bigTbl2 (SELECT * FROM employees.employees);
CREATE TABLE bigTbl3 (SELECT * FROM employees.employees);

-- 1. DELETE: DML 명령. 데이터를 하나씩 삭제하며 트랜잭션 로그를 남김. 가장 느림.
DELETE FROM bigTbl1;

-- 2. DROP: DDL 명령. 테이블 자체를 삭제함 (구조도 사라짐). 빠름.
DROP TABLE bigTbl2;

-- 3. TRUNCATE: DDL 명령. 테이블 구조는 남기고 데이터만 싹 비움. 로그를 적게 남겨 DELETE보다 훨씬 빠름.
TRUNCATE TABLE bigTbl3;

-- </실습 3> --



-- <실습 4> : 제약조건, 데이터 중복 처리 --

USE sqldb;
CREATE TABLE memberTBL (SELECT userID, name, addr FROM usertbl LIMIT 3); -- 3건만 가져옴
ALTER TABLE memberTBL 
	ADD CONSTRAINT pk_memberTBL PRIMARY KEY (userID); -- PK를 지정함
SELECT * FROM memberTBL;

INSERT INTO memberTBL VALUES('BBK' , '비비코', '미국');
INSERT INTO memberTBL VALUES('SJH' , '서장훈', '서울');
INSERT INTO memberTBL VALUES('HJY' , '현주엽', '경기');
SELECT * FROM memberTBL;

-- [INSERT IGNORE]
-- PRIMARY KEY 중복 등으로 인한 에러 발생 시, 에러를 내고 멈추는 대신 경고만 발생시키고 무시(넘어감)한다.
INSERT IGNORE INTO memberTBL VALUES('BBK' , '비비코', '미국');
INSERT IGNORE INTO memberTBL VALUES('SJH' , '서장훈', '서울');
INSERT IGNORE INTO memberTBL VALUES('HJY' , '현주엽', '경기');
SELECT * FROM memberTBL;

-- [ON DUPLICATE KEY UPDATE]
-- PK 중복 발생 시, INSERT 대신 UPDATE를 수행한다.
INSERT INTO memberTBL VALUES('BBK' , '비비코', '미국')
	ON DUPLICATE KEY UPDATE name='비비코', addr='미국';
INSERT INTO memberTBL VALUES('DJM' , '동짜몽', '일본')
	ON DUPLICATE KEY UPDATE name='동짜몽', addr='일본';
SELECT * FROM memberTBL;

-- </실습 4> --

USE sqldb;
SELECT userid AS '사용자', SUM(price*amount) AS '총구매액'  
  FROM buyTBL GROUP BY userid;

WITH abc(userid, total)
AS
(SELECT userid, SUM(price*amount)  
  FROM buyTBL GROUP BY userid )
SELECT * FROM abc ORDER BY total DESC ;

WITH cte_usertbl(addr, maxHeight)
AS
  ( SELECT addr, MAX(height) FROM usertbl GROUP BY addr)
SELECT AVG(maxHeight*1.0) AS '각 지역별 최고키의 평균' FROM cte_usertbl;
