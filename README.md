# CSIS_scraper

미국 국무부(United States Department of State)의 분석들을 받아오기 위한 크롤러입니다.

## User guide

크롤러의 파이썬 파일은 util.py, scraper.py 그리고 parser.py 총 세가지로 구성되어 있습니다. 
util.py는 크롤링 한 파이썬의 beautifulsoup 패키지를 받아서 url내의 html정보를 정리합니다.
scraper는 util.py내의 사이트내의 url 링크들을 get_soup함수를 통해 모아줍니다.
parser는 이렇게 만들어진 url리스트를 통해서 각 분석들의 제목/일자/내용을 모아줍니다.

## 유의사항

이 코드는 작동하지만, 폴더내의 모듈들을 원활하게 불러오는데 문제를 가지고 있습니다. init부분의 문제를 수정하고 있습니다.
