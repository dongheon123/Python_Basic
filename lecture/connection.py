# 파일시스템: 폴더 또는 디렉토리로 데이터를 저장하는 방법
# 데이터베이스: 데이터를 효율적으로 저장하고 관리해주는 시스템(이론)

# 데이터베이스 관리 시스템: DBMS. DB제품

# ** DBMS 종류
# 1. 관계형 데이터베이스(RDB) : 전통적인(스키마:명세서)
#     - ORACLE ..유료
#     - MySQL ..무료
#     - MariaDB
#
# 2. NoSQL : New(빅데이터)
#     - MongoDB
#     - Redis

# ** DBMS 프로세스
#     - DB에 ID, PW 저장
# Pycharm(Python) ----------------DB(MongoDB)
#     1. Pycharm과 DB Connection 맺기
#     - IP : 컴퓨터를 접속 할 수 있는 주소
#     - PORT : 컴퓨터 내에 프로그램의 위치
#     - ID and PW

# 2. SQL을 사용해서 작업(CRUD) 진행
#     - SQL(구조질의어): RDB를 사용하기 위해서는 반드시 사용!
#     CREATE -> INSERT
#     READ -> SELECT
#     UPDATE -> UPDATE
#     DELETE -> DELETE

# ** MongoDB 설정 방법
# 1. 직접 설치(Local)
# 2. MongoDB에서 제공하는 랩 클라우드 사용 (설치X)
#   - MongoDB 회원가입 필수!
#   - IP와 PORT -> URL 제공!


from pymongo import MongoClient

# MongoDB Connection

def conn_mongodb():
    # IP, PORT, ID, PW
    DB_ID = ""   # 상수(전체 대문자로 변수명을 사용)
    DB_PW = ""

    # ex) 은행권 -> 금리(상수)
