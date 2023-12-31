# SELENIUM

# pip install selenium
# pip install webdriver_manager

# ** Selenium을 사용하는 이유?
#   - Requests는 현재 URL의 정적 페이지 소스코드만 수집 가능
#   -> "더보기" 버튼 클릭과 같이 동적인 동작 불가!
#   -Selenium 전용 브라우저를 사용해서 동작
#   -> 따라서 chrome 드라이버와 같은 브라우저 설정 반드시 필요!
#  ※ Selenium은 처음에 웹 브라우저 테스트 용으로 개발

# ** Selenium 사용 방법 2가지
#   1. 직접 다운로드
#   - URL: https://sites.google.com/chromium.org/driver/
#   2. 실시간(코드) 다운로드
from datetime import datetime, timedelta


import math
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 1. Selenium 전용 웹 브라우저 구동
options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

# 2. URL 접속
url = "https://movie.daum.net/moviedb/grade?movieId=169137"
driver.get(url)
time.sleep(2)

# 3. 페이지 전체 코드 가져오기
doc_html = driver.page_source

#   4.Selenim -> BeautifulSoup
doc = BeautifulSoup(doc_html,"html.parser")

# 5. 영화 제목 수집

movie_title = doc. select("span.txt_tit")[0].get_text()
print("="*100)
print(f"= 영화 제목: {movie_title}")
print("="*100)

# 6. 전체 리뷰 출력("평점 더보기" 클릭)
#   - 다음 영화 최초 페이지 -> 10개
#   - "평점 더보기" 클릭 -> 30개
#   ? "평점 더보기" 몇 번 클릭? -> 전체 리뷰 출력

#   ex) 전체 리뷰: 187

#수식: 올림 ((187-10)/30) = 6

# 6-1. 전체 리뷰
total_review_cnt = doc.select("span.txt_netizen")[0].get_text()

#   6-2. 전체 리뷰에서 숫자만 추출
#   - 문자열 슬라이싱
#   예) (187명)
#print(total_review_cnt[1:-2]) #문자열 슬라이싱 기말고사에 나옴..
# - 정규식 -> 숫자만 추출

num_review = int(re.sub(r"[^~0-9]","", total_review_cnt))

#6-3."평점 더보기" 클릭 횟수 계산(모든 리뷰 출력)
click_cnt = math.ceil((num_review-10)/30)

# 7. Selenium을 통해서 "평점 더보기" 클릭
for i in range(click_cnt):
    # "평점 더보기" 클릭
    driver.find_element(By.CLASS_NAME, "link_fold").click()
    time.sleep(1)

# 8. 전체 소스코드 가져오기
doc_html = driver.page_source
doc = BeautifulSoup(doc_html,"html.parser")
review_list = doc.select("ul.list_comment > li")

print(len(review_list))

for item in review_list:
    print("=" * 100)
    review_score = item.select("div.ratings")[0].get_text()
    print(f"  - 평점 {review_score}")
    review_content = item.select("p.desc_txt")[0].get_text().strip() #좌우 여백 제거
    # \n : 한줄 개행
    # 수집한 리뷰 개행 -> 문자열 안에 \n 포함
    # \n > 공백으로 변경
    review_content =re.sub("\n", "",review_content)
    print(f"  - 리뷰: {review_content}")
    review_writer = item.select("a.link_nick > span")[1].get_text() # [댓글작성자,작성자,댓글 모아보기
    print(f"  - 작성자: {review_writer}")
    # 24시간이내에 작성된 글은 날짜 -> 예: 21시간전, 17시간전
    # 실제 날짜 표기법 -> 2023. 11. 17. 12:15
    # 표기법: 21시간전 -> 2023. 11. 17. 12:15

    # 21시간전 잘못 뜨는 경우를 어떤 조건을 주면 찾을 수 있을까?
    # = review_date -> 17시간전 or 2023. 11.17 12:17


    review_date = item.select("span.txt_date")[0].get_text()
    if len(review_date) < 7:
        # 현재 시간 - 17시간
        # 예:) 17시간전 -> 숫자만 추출: 17
        reg_hour = int(re.sub(r"[^~0-9]","", review_date))
        # 예) 현재시간(2023.11.17 12:29) - 18 = 2023-11-16 18:29:23.232500
        review_date = datetime.now()-timedelta(hours=reg_hour)
        # 예) 2023-11-16 18:29:23.232500 -> 2023. 11.16. 18:29
        review_date = review_date.strftime("%Y. %m. %d. %H:%M")
    print(f"  - 날짜: {review_date}")