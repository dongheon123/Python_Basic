#   파일시스템: 폴더 또는 디렉토리로 데이터를 저장하는 방법
#   데이터베이스: 데이터를 효율적으로 저장하고 관리해주는 시스템(이론)

#   데이터베이스 관리 시스템(DBMS): 데이터베이스 제품!
#   ** DBMS 종류
#   1. 관계형 데이터베이스(RDB) : 전통적인(스키마: 명세서)
#   - ORACLE
#   - MySQL
#   - MariaDB

#   2. NoSQL: New(빅데이터)
#   - MongoDB
#   - Redis

# ** DBMS 프로세스
#   -DB에 ID와 PW 저장
# Pycharm(Python)  -------------- DB(MongoDB)
#   1. Pycharm과 DB Connection 맺기
#   - IP: 컴퓨터를 접속 할 수 있는 주소
#   - PORT: 컴퓨터 내에 프로그램의 위치
#   - ID and PW:
#   2. SQL을 사용해서 작업 진행
#   -SQL(구조질의어): RDB를 사용하기 위해서는 반드시 사용!
#   -RDB(SQL)을 사용, NoSQL(SQL X)
#   CREATE  -> INSERT
#   READ    -> SELECT
#   UPDATE  -> UPDATE
#   DELETE  -> DELETE

# ** MongoDB 사용방법 2가지
#   1. 직접 설치(Local)
#    - IP,PORT,ID,PW
#   -장점:  설치과정 복잡, 설정 직접, 컴퓨터 자원 부족
#   -단점:  사용편함, 관리편함,커스터마이징 가능
#   2. MongoDB에서 제공하는 Web Cloud 사용
#   - URL,ID,PW
#   - 장점: 사용편함, 설치X, 설정X, 컴퓨터 자원 X
#   - 단점: 관리 X, 커스터마이징 X

#   ** MongoDB 구조
#  설치: MongoDB(DBMS)
#       ㄴ DB(카카오톡):DB는 폴더 개념
#           ㄴ Collection( 회원 ): Collection은 표개념
#            ㄴ Collection(톡)
#              ㄴ Collection(친구)
#               ㄴ ...
#       ㄴ DB(카카오뱅크):
#           ㄴ Collection(회원)
#           ㄴ Collection(계좌)
#           ㄴ Collection(대출)
#            ㄴ...
#       ㄴ DB(카카오페이)
#          ㄴ....
# pymongo: Python - MongoDB 연결해서 사용
from pymongo import MongoClient

#MongoDM Connection
def conn_mongodb():
    #IP,PORT,ID,PW
    DB_ID="root"  #상수(전체 대문자로 변수명을 사용)
    DB_PW="1234"    # 예시) 은행에서 금리(상수)
    client = MongoClient(f"mongodb+srv://{DB_ID}:{DB_PW}@daumcluster.pwey6ij.mongodb.net/")   #URL
    db = client["daum"]
    collection = db.get_collection("news")
    return collection
