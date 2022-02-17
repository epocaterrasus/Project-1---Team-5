#This sheet of code contains all the different DataCalls from the Yahoo Finance API which are then used by our other functions which create the DataFrames and visualizations for the information we chose to display

#Imports the necessary libraries
import yfinance as yf
import pandas as pd
import datetime
from bokeh.models.formatters import DatetimeTickFormatter
from xlwings import view

#%matplotlib inline

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
        ticker_hist_1yr_df = self.ticker.history(period="1y")
        #Resets the index of the DataFrame so that the Date can be properly selected
        ticker_hist_1yr_df = ticker_hist_1yr_df.reset_index()
        return(ticker_hist_1yr_df)
        #Function that gets price history for a 3 Year period     
    def history3Year(self):
        ticker_hist_3yr_df = self.ticker.history(period="3y")
        #Resets the index of the DataFrame so that the Date can be properly selected
        ticker_hist_3yr_df = ticker_hist_3yr_df.reset_index()
        return(ticker_hist_3yr_df)    

#Financials

    #Income Statements

    #Function that gets the income statement in a yearly form (last four years)
    def getYearlyIncome(self):
        ticker_yr_income = self.ticker.financials
        return(ticker_yr_income)
    #Function that gets the income statement in a quarterly form (last four quarters)
    def getQuarterlyIncome(self):
        ticker_qt_income = self.ticker.quarterly_financials
        return(ticker_qt_income)
    
    #Balance Sheet

    #Function that gets the balance sheet for the last four years
    def getBalanceSheet(self):
        ticker_balance_sheet = self.ticker.balance_sheet
        #Formats to remove commas from strings
        ticker_balance_sheet.replace(",","",regex=True, inplace=True)
        #Converts strings into floats
        ticker_balance_sheet = ticker_balance_sheet.astype(float)
        #Formats the style of the output to display desired amount of decimals
        ticker_balance_sheet = ticker_balance_sheet.style.format("{:,.0f}")
        return(ticker_balance_sheet)
    #Function that gets the quarterly balance sheet for the last four quarters
    def getQBalanceSheet(self):
        ticker_q_balance_sheet = self.ticker.quarterly_balance_sheet
        #Formats to remove commas from strings
        ticker_q_balance_sheet.replace(",","",regex=True, inplace=True)
        #Converts strings into floats
        ticker_q_balance_sheet = ticker_q_balance_sheet.astype(float)
        #Formats the style of the output to display desired amount of decimals
        ticker_q_balance_sheet = ticker_q_balance_sheet.style.format("{:,.0f}")
        return(ticker_q_balance_sheet)

#Holding Information

    #Function that gets the percentage shareholding between Insiders and Institutional Owners
    def getHoldingPerc(self):
        ticker_pct_holders = self.ticker.major_holders
        return(ticker_pct_holders)
    #Function that gets the top 10 institutional holders
    def getInstitutionals(self):
        ticker_institutional = self.ticker.institutional_holders
        return(ticker_institutional)

#Earnings

    #Function that gets the earnings for the last four years (revenue and earnings)
    def getEarnings(self):
        ticker_earnings = self.ticker.earnings
        return(ticker_earnings)
    #Function that gets the earnings for the last four quarters (revenue and earnings)
    def getEarnings(self):
        ticker_q_earnings = self.ticker.quarterly_earnings
        return(ticker_q_earnings)

#Recommendations

    # Functions that get the recommendations
    def getRecommendations(self):
        ticker_recommendations = self.ticker.recommendations
        #resets the index
        ticker_recommendations = ticker_recommendations.reset_index()
        #sets the "Date" as the index
        ticker_recommendations.set_index("Date", inplace=True)
        # Slices recommendations to only show past 6 months
        #sets end date for the slice
        end = pd.to_datetime('now')
        #sets start date for the slice
        start = pd.to_datetime('now')-pd.DateOffset(months=6)
        #slices the information using our start and end date
        ticker_recommendations = ticker_recommendations[start:end]
        return(ticker_recommendations)

#Calendar

    #Function to get the calendar
    def getCalendar(self):
        ticker_calendar = self.ticker.calendar
        return(ticker_calendar)

#News

    #Function to get news
    def getNews(self):
        #Imports the news into a DataFrame
        ticker_news = pd.DataFrame.from_dict(self.ticker.news)
        #Changes the publish time from Unix seconds into a date
        ticker_news["providerPublishTime"] = pd.to_datetime(ticker_news["providerPublishTime"], unit = "s")
        #Sets the publish time as the index
        ticker_news.set_index("providerPublishTime", inplace=True)
        #Drops the uuid and type column
        ticker_news.drop(columns = ["uuid","type"], inplace=True)
        #Resets the index
        ticker_news = ticker_news.reset_index()
        #Sets Column Names
        ticker_news.set_axis(["Publish Time", "Article Title", "Publisher", "Link"], axis = 1, inplace = True)
        #Sets index
        ticker_news = ticker_news.set_index("Publish Time")
        #Styles the width of the table
        #ticker_news = ticker_news.style.set_properties(subset=['Article Title'], **{'width': '300px'})
        return(ticker_news)



#Main function that runs the code by pulling in a ticker, in this example FB, but with our interface this ticker becomes changeable to any ticker desired by the user
if __name__=="__main__":
    ticker_data = TickerData("FB")
