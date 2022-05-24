from bs4 import BeautifulSoup
import requests

url = 'https://dtf.ru/games'
def get_game(url):
    response = requests.get(url)
#print(response.text)


    soup = BeautifulSoup(response.text, 'html.parser')
    game = soup.find_all('div', class_="content-title content-title--short l-island-a")
    for el in game:
        print(el.text.replase('\n' + " " * )

get_game(url)
#print(news)

#get_news(url)
#for i in range(2,11):
 #   get_news('https://habr.com/ru/all/page' + str(i))

