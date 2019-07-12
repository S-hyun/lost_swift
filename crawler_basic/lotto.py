# 다음 로또 당첨 페이지에서 이번주 당첨번호 찾아서 입력하기

import requests
from bs4 import BeautifulSoup
# 엑셀에 저장하기 위한 모듕
from openpyxl import  Workbook

# pip install openpyxl
# 1. 로또 당첨번호 페이지 url 만들기
# 2. 해당 페이지 접속 with requests
# 3. 점속이 제대로 됐는지 확인하기
# 4. 데이터를 html로 변환하기 with BeautifulSoup
# 5. html 에서 요소 찾아 출력하기

url = "https://search.daum.net/search?w=tot&DA=UMZ&t__nil_searchbox=suggest&sug=topex&sugo=16&sq=%E3%84%B9%E3%85%97%EB%98%90+&o=1&q=%EB%A1%9C%EB%98%90+%EB%8B%B9%EC%B2%A8+%EB%B2%88%ED%98%B8"

data = requests.get(url)

if data.status_code != requests.codes.ok:
    print("접속 실패")
    exit()


html = BeautifulSoup(data.text, "html.parser")

nums = html.select("span.img_lotto")
wb = Workbook()
ws = wb.active



for index, num in enumerate(nums, start=1):
    print(num.text)
    ws.cell(1, index, num.text)

wb.save("lotto.xlsx")

# data save in excel file
# html.select_one("selector")

