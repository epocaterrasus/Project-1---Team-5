#Imports the necessary libraries
import yfinance as yf
import pandas as pd
import json

#for information about the API and it's different call functions please visit, visit https://pypi.org/project/yfinance/

#Creates a class to hold all the definitions that will call our API for the different types of data
class TickerData():
    #Function that transforms the ticker into a YahooFinance(API) readable format
    def __init__(self,ticker):
        self.ticker =  yf.Ticker(ticker)
    
#General Information

#Function that gets general stock information from the ticker.info call
    def getInfo(self):
        ticker_info = self.ticker.info
        #turns the information into a DataFrame for better organization and access to information
        ticker_info_df = pd.DataFrame.from_dict(ticker_info, orient="index")
        return (ticker_info_df)

#Historical Pricing

    #Function that gets price history for a one week period
    def history1Week(self):
        ticker_hist_1wk_df = self.ticker.history(period="1wk")
        #Resets the index of the DataFrame so that the Date can be properly selected
        ticker_hist_1wk_df = ticker_hist_1wk_df.reset_index()
        return(ticker_hist_1wk_df)
    #Function that gets price history for a one month period
    def history1Month(self):
        ticker_hist_1mo_df = self.ticker.history(period="1mo")
        #Resets the index of the DataFrame so that the Date can be properly selected
        ticker_hist_1mo_df = ticker_hist_1mo_df.reset_index()
        return(ticker_hist_1mo_df)
    #Function that gets price history for a three months period
    def history3Month(self):
        ticker_hist_3mo_df = self.ticker.history(period="3mo")
        #Resets the index of the DataFrame so that the Date can be properly selected
        ticker_hist_3mo_df = ticker_hist_3mo_df.reset_index()
        return(ticker_hist_3mo_df)  
    #Function that gets price history for a 1 Year period     
    def history1Year(self):
        ticker_hist_1yr_df = self.ticker.history(period="1yr")
        #Resets the index of the DataFrame so that the Date can be properly selected
        ticker_hist_1yr_df = ticker_hist_1yr_df.reset_index()
        return(ticker_hist_1yr_df)
        #Function that gets price history for a 3 Year period     
    def history3Year(self):
        ticker_hist_3yr_df = self.ticker.history(period="3yr")
        #Resets the index of the DataFrame so that the Date can be properly selected
        ticker_hist_3yr_df = ticker_hist_3yr_df.reset_index()
        return(ticker_hist_3yr_df)    

#Financials

    #Function that gets financials in a yearly form (last four years)
    def getYearlyFinancials(self):
        ticker_yr_financials = self.ticker.financials
        return(ticker_yr_financials)
    #Function that gets financials in a quarterly form (last four quarters)
    def getQuarterlyFinancials(self):
        ticker_qt_financials = self.ticker.quarterly_financials
        return(ticker_qt_financials)

#Holding Information

    #Function that gets the percentage shareholding between Insiders and Institutional Owners
    def getHoldingPerc(self):
        ticker_pct_holders = self.ticker.major_holders
        return(ticker_pct_holders)
    #Function that gets the top 10 institutional holders
    def getInstitutionals(self):
        ticker_institutional = self.ticker.institutional_holders
        return(ticker_institutional)
        



if __name__=="__main__":
    ticker_data = TickerData("FB")
    print (ticker_data.getInfo())