import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select(".titleline a")

print("Топ 10 новостей Hacker News:\n")
for i, title in enumerate(titles[:10], 1):
    print(i, title.text)


    