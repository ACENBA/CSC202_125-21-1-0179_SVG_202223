import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "http://www.alphvantage.co/query"
NEWS_ENDPOINT = "http://newsapi.org/v2/everything"

STOCK_API_KEY = "G4FI7TY9IRF3I7AU"
NEWS_API_KEY = "90572cf1e9af4d449c49e3aa83de72a6"



stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

requests.get(STOCK_ENDPOINT, params= stock_parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4.close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

diff_percent = (difference / float(yesterday_closing_price)) * 100

if diff_percent > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(NEWS_ENDPOINT, params = news_params)
    articles = news_response.json()["articles"]
    print(articles)

    three_articles = articles[:3]
    print(three_articles)

    
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]