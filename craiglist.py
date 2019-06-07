from bs4 import BeautifulSoup
import requests

url = "https://mumbai.craigslist.org/"
response = requests.get(url)

data = response.text
soup = BeautifulSoup(data, 'html.parser')                    #html.parser is used since we are scrapping using html related 
titles = soup.find_all("div", {"class":"housing"})           #div is the tagname and classname is written in curly brackets

for title in titles:
	print(title.text)
