from tickerdata import *
#Imports the necessary libraries
#from typing_extensions import Self
import yfinance as yf
import pandas as pd
import json
import datetime
from IPython.display import display
from bokeh.models.formatters import DatetimeTickFormatter
from xlwings import view
from datetime import timedelta
from PyQt5 import QtCore, QtGui, QtWidgets

#print(ticker_data.getInfo())

#Function that creates a table with summary information about the stock/ticker





def stockInfo(ticker_data):
    
    #Pulls in the symbol using the getInfo function
    stock_ticker = ticker_data.getInfo()[0]["symbol"]
    #Pulls in the short name for the company using the getInfo function
    stock_name = ticker_data.getInfo()[0]["shortName"]
    #Pulls in the sector using the getInfo function
    stock_sector = ticker_data.getInfo()[0]["sector"]
    #Pulls in the stock industry using the getInfo function
    stock_industry = ticker_data.getInfo()[0]["industry"]
    #Creates a dictionary containing our aforementioned variables
    stock_information_dic = {"Ticker" : stock_ticker, "Name" : stock_name, "Sector" : stock_sector, "Industry" : stock_industry}
    #Creates a DataFrame from the previously mentioned dictionary with no index (for aestethics)
    stock_information_df = pd.DataFrame(data=stock_information_dic, index=[""])
    stock_information_df.style.set_properties(subset=[""], **{'width': '300px'})
    return(stock_information_df)

#Function that pulls the business summary for the stock/ticker
def stockSummary(ticker_data):
    #Pulls in the Long Business Summary using the getInfo function
    stock_description = ticker_data.getInfo()[0]["longBusinessSummary"]
    return stock_description

#Function that creates a table with price and % change information
def pricingInfo(ticker_data):
    #Pulls in the Current Stock Price rounds it
    stock_curr_price = round((ticker_data.getInfo()[0]["regularMarketPrice"]),2)
    #Pulls in the Yesterday's Stock Price and rounds it
    stock_ystdy_price = round((ticker_data.getInfo()[0]["regularMarketPreviousClose"]),2)
    #Pulls in the 50 Day Average Stock Price and rounds it
    stock_50dyavg_price = round((ticker_data.getInfo()[0]["fiftyDayAverage"]),2)
    #Calculates the value difference since todays and yesterdays price and rounds it
    change_since_ystdy = round(((stock_curr_price - stock_ystdy_price) / stock_curr_price),2)
    #Calculates the % difference since todays and yesterdays price and rounds it
    pct_change_since_ystdy = round(((change_since_ystdy / stock_ystdy_price) * 100),2)
    #creates a Dictionary containing all the information we generated or calculated in our previous steps
    stock_price_dic = {"Current Price ($)" : stock_curr_price, "Yesteday Closing Price ($)" : stock_ystdy_price, "Fifty Day Average Price ($)" : stock_50dyavg_price, "Change since Yesterday ($)" : change_since_ystdy, "Change since Yesterday (%)": pct_change_since_ystdy}
    #creates a DataFrame using our dictionary and desired columns and no index (for aesthethics)
    stock_price_df = pd.DataFrame(data=stock_price_dic, index=[""])
    return(stock_price_df)

#Function that creates a table that summarizes analysts pricing opinions for the stock
def analystSummary(ticker_data):
    stock_current_price = ticker_data.getInfo()[0]["regularMarketPrice"]
    #pulls in the Number of Analysts Ratings/Opinions 
    number_of_analysts = ticker_data.getInfo()[0]["numberOfAnalystOpinions"]
    #pulls in the Target Median Price 
    target_median_price = round(ticker_data.getInfo()[0]["targetMedianPrice"],2)
    #pulls in the Target Mean Price 
    target_mean_price = round(ticker_data.getInfo()[0]["targetMeanPrice"],2)
    #Calculates the %difference between the target median price and the current price and rounds it
    pct_diff_target_median = round((((target_median_price - stock_current_price) / stock_current_price) * 100), 2)
    #Calculates the %difference between the target mean price and the current price and rounds it
    pct_diff_target_mean = round((((target_mean_price - stock_current_price) / stock_current_price) * 100), 2) 
    #creates a Dictionary containing all the information we generated or calculated in our previous steps
    stock_analysts_dic = {"# of Analyst Forecasts" : number_of_analysts, "Median Target Price" : target_median_price, "% Difference Current Price to Median Target": pct_diff_target_median, "Mean Target Price" : target_mean_price, "% Difference Current Price to Mean Target": pct_diff_target_mean,}
    #creates a DataFrame using our dictionary and desired columns and no index (for aesthethics)
    stock_analysts_df = pd.DataFrame(data=stock_analysts_dic, index=[""])
    #rotates the Axis of our DataFrame
    stock_analysts_df = stock_analysts_df
    return stock_analysts_df

#Function that creates a table with the stocks price evolution
def stockpriceEvolution(ticker_data):
    stock_current_price = ticker_data.getInfo()[0]["regularMarketPrice"]
    stock_ystdy_price = round((ticker_data.getInfo()[0]["regularMarketPreviousClose"]),2)
    change_since_ystdy = round(((stock_current_price - stock_ystdy_price) / stock_current_price),2)
    #1 Week Numbers and calculations
    #Pulls the 1Wk Closing Stock Price
    stock_1wk_price = round(ticker_data.history1Week()["Close"][0],2)
    #calculates the % difference between current price and 1Wk Closing Price and rounds it
    stock_1wk_change = round((((stock_current_price - stock_1wk_price) / stock_current_price) * 100), 2)
    #1mo Numbers and calculations
    #Pulls the 1month Closing Stock Price 
    stock_1mo_price = round(ticker_data.history1Month()["Close"][0],2)
    #calculates the % difference between current price and 1mo Closing Price and rounds it
    stock_1mo_change = round((((stock_current_price - stock_1mo_price) / stock_current_price) * 100), 2)
    #3mo Numbers and calculations
    #Pulls the 3month Closing Stock Price 
    stock_3mo_price = round(ticker_data.history3Month()["Close"][0],2)
    #calculates the % difference between current price and 1mo Closing Price and rounds it
    stock_3mo_change = round((((stock_current_price - stock_3mo_price) / stock_current_price) * 100), 2)
    #1 Year Numbers and calculations
    #Pulls the 1Yr Closing Stock Price from ticker_hist_1yr_df and rounds it
    stock_1yr_price = round(ticker_data.history1Year()["Close"][0],2)
    #calculates the % difference between current price and 1Yr Closing Price and rounds it
    stock_1yr_change = round((((stock_current_price - stock_1yr_price) / stock_current_price) * 100), 2)
    #3 Year Numbers and Calculations
    #Pulls the 3Yr Closing Stock Price
    stock_3yr_price = round(ticker_data.history3Year()["Close"][0],2)
    #calculates the % difference between current price and 3Yr Closing Price and rounds it
    stock_3yr_change = round((((stock_current_price - stock_3yr_price) / stock_current_price) * 100), 2)
    #Finds our calculates the dates for each timeperiod which will then be used as labels when creating our DataFrame
    stock_today_date = pd.Timestamp.today().date()
    stock_yesterday_date = (stock_today_date  - timedelta(days = 1))
    stock_1wk_date = ticker_data.history1Week()["Date"][0].date()
    stock_1mo_date = ticker_data.history1Month()["Date"][0].date()
    stock_3mo_date = ticker_data.history3Month()["Date"][0].date()
    stock_1yr_date = ticker_data.history1Year()["Date"][0].date()
    stock_3yr_date = ticker_data.history3Year()["Date"][0].date()
    #creates a Dictionary containing all the information we generated or calculated in our previous steps
    stock_evolution_dic = {"Date" : [stock_today_date, stock_yesterday_date, stock_1wk_date, stock_1mo_date, stock_3mo_date, stock_1yr_date, stock_3yr_date], "Price" : [stock_current_price, stock_ystdy_price, stock_1wk_price, stock_1mo_price, stock_3mo_price, stock_1yr_price, stock_3yr_price], "% Change" : ["-", change_since_ystdy, stock_1wk_change, stock_1mo_change, stock_3mo_change, stock_1yr_change, stock_3yr_change]}
    #stores our desired column names
    columns = ["Actual", "Last Close", "1 Week Close", "1 M Close","3 M Close", "1 Year Close", "3 Year Close"]
    #creates a DataFrame using our dictionary and desired columns
    stock_evolution_df = pd.DataFrame.from_dict(stock_evolution_dic, orient='index', dtype=None, columns = columns)
    print(stock_evolution_df)
    return stock_evolution_df

#Function that creates a table with Common Ratios
def getCommonRatios(ticker_data):
    ratios ={
   "Trailing PE": round(ticker_data.getInfo()[0]["trailingPE"],2),
    "Forward PE": round(ticker_data.getInfo()[0]["forwardPE"],2),
    "Trailing EPS": round(ticker_data.getInfo()[0]["trailingEps"],2), 
    "Forward EPS": round(ticker_data.getInfo()[0]["forwardEps"],2),
    "Return On Equity": round(ticker_data.getInfo()[0]["returnOnEquity"],2),
    "TEV/Sales": round(ticker_data.getInfo()[0]["enterpriseValue"]/ticker_data.getInfo()[0]["totalRevenue"],2),
    "TEV/EBITDA": round(ticker_data.getInfo()[0]["enterpriseValue"]/ticker_data.getInfo()[0]["ebitda"],2),
    "Total Debt/Equity": round(ticker_data.getInfo()[0]["debtToEquity"],2),
    "Total Debt/EBITDA": round(ticker_data.getInfo()[0]["totalDebt"]/ticker_data.getInfo()[0]["ebitda"],2),
    "Total Debt/TEV": round(ticker_data.getInfo()[0]["totalDebt"]/ticker_data.getInfo()[0]["enterpriseValue"],2),
    "Price to Book": round(ticker_data.getInfo()[0]["priceToBook"],2) 
    }
    #Creates a DataFrame using our dictionary and desired columns and no index (for aesthethics)  
    common_ratios_df = pd.DataFrame(data=ratios, index=[""])
    #Rotates the Axis of our DataFrame
    common_ratios_df = common_ratios_df
    return(common_ratios_df)

#def plot


