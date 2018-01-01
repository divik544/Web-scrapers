#Script that fetches bitcoin prices, requests module is used to create a http request and data is fetched in the form of JSON.
import requests

res = requests.get('https://www.zebapi.com/api/v1/market/ticker/btc/inr')

data = res.json()
print("Prices in INR:" )
print("Buy at:", data['buy'])
print("Sell at :", data['sell'])

res = requests.get('https://www.zebapi.com/api/v1/market/ticker/btc/usd')
data = res.json()
print("Prices in USD")
print("Buy at: ", data['buy'])
print("Sell at :", data['sell'])
