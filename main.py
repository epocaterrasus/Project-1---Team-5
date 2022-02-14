from matplotlib import ticker
import yfinance as yf
import pandas as pd

ticker = "MSFT"

stock = yf.Ticker(ticker)

stock_info = stock.info

stock_df = pd.DataFrame.from_dict(stock_info, orient="index")

stock_financials = stock.financials

print(stock_financials)

stock_mh = stock.major_holders

print (stock_mh)

institutional = stock.institutional_holders

print(institutional)

#Qualitative Information

#defines a variable containing the stock's name
stock_name = stock_df[0]["shortName"]

#defines a variable containing the stock's business summary
stock_summary = stock_df[0]["longBusinessSummary"]

#defines a variable containing the stock's country of incorporation/business
stock_location = stock_df[0]["country"]

#defines a variable containing the stock's industry
stock_industry = stock_df[0]["country"]