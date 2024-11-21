import yfinance as yf
import pandas as pd
from bs4 import BeautifulSoup
import requests

def fetch_stock_data(ticker_list, start_date, end_date):
    """
    Fetches historical stock data using Yahoo Finance API
    """
    stock_data = {}
    for ticker in ticker_list:
        try:
            stock = yf.Ticker(ticker)
            stock_data[ticker] = stock.history(start=start_date, end=end_date)
            print(f"Successfully fetched data for {ticker}")
        except Exception as e:
            print(f"Error fetching data for {ticker}: {str(e)}")
    return stock_data

def scrape_market_news(ticker):
    """
    Scrapes latest news articles related to the stock from Yahoo Finance
    """
    url = f"https://finance.yahoo.com/quote/{ticker}/news"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = []
        
        articles = soup.find_all('h3', class_='Mb(5px)')
        for article in articles[:5]:
            news_items.append(article.text.strip())
            
        return news_items
    except Exception as e:
        print(f"Error scraping news for {ticker}: {str(e)}")
        return []
