"""
Following this tutorial: https://www.youtube.com/watch?v=6W6iY7uUu34

How to update repo
git add test.py
git commit -m "initial commit"
git push origin main


How to make requirements.txt
pip list
pip freeze > requirements.txt

"""

import yfinance as yf

ticker = yf.Ticker("VOO")
print(ticker.info)
