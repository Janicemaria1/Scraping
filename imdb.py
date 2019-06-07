import requests
from bs4 import BeautifulSoup

url='https://www.imdb.com/search/title?genres=drama&groups=top_250&sort=user_rating,desc'
resp=requests.get(url)

soup = BeautifulSoup(resp.text, 'html.parser')

llist = soup.find_all('h3', {'class':'list-item-header'})

for x in llist:
	for y in x.find_all('a'):
		print(y.text)
