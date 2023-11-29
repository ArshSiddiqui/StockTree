import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}
url = "https://finance.yahoo.com/quote/LRCX/history?p=LRCX"
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

data_table = soup.findAll("table")[0]
data_table_rows = data_table.find_all("tr")
data_table_data = []
for r in data_table_rows:
    col = r.find_all("td")
    col = [t.text.strip() for t in col]
    if len(col) > 2:
        data_table_data.append([e for e in col if e])

if len(data_table_data) > 10:
    print(data_table_data[0:10])
else:
    print(data_table_data)
