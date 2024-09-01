import yfinance as yf
import pandas as pd
from datetime import datetime

import requests_cache
session = requests_cache.CachedSession('yfinance.cache')
session.headers['User-agent'] = 'my-program/1.0'

ticker = 'VOO'

stock = yf.Ticker(ticker)
data = stock.history(period="max")  # 'max' period fetches the maximum available historical data
earliest_date = data.index.min()
print(earliest_date)
exit()

data: pd.DataFrame = yf.download(ticker)
filename: str = f'{ticker}_{datetime.now().strftime("%Y-%m-%d")}.csv'
data.to_csv(filename)
