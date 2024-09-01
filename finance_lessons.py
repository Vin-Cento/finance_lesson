import yfinance as yf
from datetime import datetime
import requests_cache
session = requests_cache.CachedSession('yfinance.cache')

def sumCompany(ticker:str):
    stock = yf.Ticker(ticker, session=session)

    stockShares = stock.get_shares_full(start=datetime.now().strftime("%Y-%m-%d")).values[0]
    stockPrice = stock.history(period='1d')['Close'].iloc[0]
    stockMarketCap = stockPrice * stockShares

    print("Market Cap: ${:,.2f}".format(stockMarketCap))
    print("Price Per Share: ${:,.2f}".format(stockPrice))
    print("Total Share Outstanding: {:,}".format(stockShares))

sumCompany('LUV')
