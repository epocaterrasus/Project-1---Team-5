import pandas as pd
import yfinance as yf
import datetime

#sets the ticker for the desired stock to monitor/analyze
ticker_input = "MSFT"

#transforms te ticker into a format readable by the API
ticker = yf.Ticker(ticker_input)

#This section will pull all available data from the Info Section of our API and organize it

#retrieves stock info from the API
ticker_info = ticker.info

#sets the viewable rows of the dataframe to the maximum, this configuration will last for all the DataFrames from now on unless altered
pd.set_option('display.max_rows', None)

#converts the information into a DataFrame
ticker_info_df = pd.DataFrame.from_dict(ticker_info, orient="index")