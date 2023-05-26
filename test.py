"""
Following this tutorial: https://www.youtube.com/watch?v=6W6iY7uUu34


git add test.py
git commit -m "initial commit"
git push origin main

"""

import yfinance as yf

ticker = yf.Ticker("VOO")
print(ticker.info)
