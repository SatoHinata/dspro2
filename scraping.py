from bs4 import BeautifulSoup
import requests

url = "https://www.mhlw.go.jp/www1/topics/kenko21_11/b2.html"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")
text = soup.get_text()

start = text.find("日本人の歩数の現状では、1日平均で、男性") + len("日本人の歩数の現状では、1日平均で、男性")
end = text.find("％である(平成9年度国民栄養調査)。") + len("％である(平成9年度国民栄養調査)。")
steps = text[start:end]

print(steps)