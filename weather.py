import requests
import csv
from bs4 import BeautifulSoup
city = input("enter the city you want to search: ")
url = "https://www.google.com/search?q="+"weather"+city
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
data = str.split('\n')
time = data[0]
sky = data[1]
city1 = "City: " + city
temp1 = "Temperature is" + temp
time1 = "Time: " + time
sky1 = "Sky Description: " + sky
file = open("weather.txt", "w")
file.write(city1+"\n")
file.write(temp1+"\n")
file.write(time1+"\n")
file.write(sky1+"\n")
file.close()