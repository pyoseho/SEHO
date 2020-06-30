import datetime

days_range = []

start = datetime.datetime.strptime("2020-01-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-06-30", "%Y-%m-%d") # 범위 + 1
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    days_range.append(date.strftime("%Y-%m-%d"))

print(days_range)
['2020-01-01', '2020-01-02', ... , '2020-06-30']

pip install bs4

import requests
from bs4 import BeautifulSoup
webpage = requests.get("https://news.naver.com)
