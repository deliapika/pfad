import pyhttpx
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from datetime import datetime



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
}
session = pyhttpx.HttpSession()
page = session.get(url='https://tianqi.2345.com/wea_history/72038.htm',headers=headers)
# print(page.text)

soup = BeautifulSoup(page.text, 'html.parser')
weather = soup.find('table')  # 找到页面中的 table 标签
data = []
for row in weather.find_all('tr'):  # 遍历 table 中的所有 tr 标签
    line = []
    for td in row.find_all('td'):  # 遍历 tr 标签中的所有 td 标签
        line.append(td.text)  # 将 td 标签的文本添加到数据数组中
    if len(line) > 0:
        data.append(line)

filename = "assignment/data.txt"
with open(filename, 'w', encoding='UTF8') as f:
    f.write(str(data))




date_list = []
highest_list = []
lowest_list = []
for line in data:
    date_list.append(datetime.strptime(line[0].split(" ")[0], '%Y-%m-%d').date())
    highest_list.append(int(line[1][:-1]))
    lowest_list.append(int(line[2][:-1]))


plt.title("Temperature of BaoAn in Sep")
plt.xlabel("date")
plt.ylabel("temperature")

plt.plot(date_list, highest_list)
plt.plot(date_list, lowest_list)
plt.legend(['highest', 'lowest'])  # 设置折线名称
plt.grid()
plt.show()