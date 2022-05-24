from bs4 import BeautifulSoup
import requests

url = 'https://habr.com/ru/all/'
def get_news(url):
    response = requests.get(url)
#print(response.text)


    soup = BeautifulSoup(response.text, 'html.parser')
    news = soup.find_all('a', class_="tm-article-snippet__title-link")
    for el in news:
        print(el.find('span').text)
#print(news)

get_news(url)
for i in range(2,11):
    get_news('https://habr.com/ru/all/page' + str(i))


