
'''This line imports the requests library, which is a Python module used for making HTTP requests to web servers'''
import requests

'''This line defines a variable called API_KEY and assigns it the value actual CoinMarketCap API key'''
API_KEY = '416c373f-f531-4dda-b122-c7ef92d902d5'

'''This line defines a variable called URL and assigns it the value 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest', 
which is the URL for the CoinMarketCap API endpoint that we will be using to fetch cryptocurrency data.'''
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

'''This line defines a dictionary called params which contains the parameters to be sent with the API request. In this case, 
we are requesting data for the Bitcoin cryptocurrency ('symbol': 'BTC') and we want the price data to be returned in Nigeria Naira ('convert': 'NGN')'''
params = {'symbol': 'BTC,ETH', 'convert': 'NGN'}

'''his line defines a dictionary called headers which contains the API key to be sent as a header with the API request. 
The CoinMarketCap API requires this key to authenticate the request and ensure that only authorized users can access the data.'''
headers = {'X-CMC_PRO_API_KEY': API_KEY}

'''This line sends a GET request to the specified URL with the params and headers included in the request. 
The requests.get() method returns a Response object, which contains the server's response to the request.'''
response = requests.get(URL, params=params, headers=headers)

'''This line converts the response data to a Python object using the json() method of the Response object. 
The json() method returns a dictionary that contains the parsed JSON data returned by the server.'''
data = response.json()

'''This line extracts the price data for Bitcoin from the parsed JSON data. The structure of the JSON data is hierarchical, 
and the price data is nested under several keys. This line accesses the price value using a series of dictionary key lookups'''
price_btc = data['data']['BTC']['quote']['NGN']['price']
price_eth = data['data']['ETH']['quote']['NGN']['price']

'''This line prints out the current Bitcoin price in NGN, using Python's formatted string literals to insert the price value into the string. 
The :.2f specifier formats the price value as a floating point number with 2 decimal places.'''
print(f"The current Bitcoin price is N{price_btc:.2f}")
print(f"The current Ethereum price is ${price_eth:.2f}")

