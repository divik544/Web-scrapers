#scripts to fetch quotes from quotes.toscrape.com

import requests
from bs4 import BeautifulSoup

def print_quote(urltext):
	res = requests.get(urltext)	#create a HTTP Request

	soup = BeautifulSoup(res.text,'lxml')
	
	for quote in soup.find_all('div', {'class':"quote"}):
		print(quote.span.text)	#quote
		print("by", quote.small.text)	#author's name

if __name__ == '__main__':
	iniurl='http://quotes.toscrape.com/'
	print_quote(iniurl)
	ct=2
	while input("Want More?(Y/N)") == 'Y':
		print_quote(iniurl+'page/'+str(ct)+'/')
		ct += 1
