import requests


def get_weather_by_city(city_name):
    url = "https://goweather.herokuapp.com/weather/" + city_name
    weather = requests.get(url).json()
    return weather


print (get_weather_by_city("Kazan"))
print (get_weather_by_city("Praha"))

def print_fun_facts():
    url = "https://cat-fact.herokuapp.com/facts"
    for i in range(1):
        print(requests.get(url).json()[i]["text"])

print_fun_facts()

def print_dog_facts():
    url = " http://dog-api.kinduff.com//api/facts"
    for i in range(1):
        print(requests.get(url).json()["facts"][0])

print_dog_facts()

import webbrowser

url = "https://random-d.uk/api/random"
pic_url = requests.get(url).json()['url']
for i in range (1,100):
    webbrowser.open(pic_url)


print("Hello, word саня миняет мир , в мире")

print("Третье изменение")
