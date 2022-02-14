import yfinance as yf
import json
class TikerData():
    def __init__(self,tikr):
        self.tikr =  yf.Ticker(tikr)
    def getHistoricalData(self):
        #llamamos a yf con self.tikr como tikr
        ticker_info = self.tikr.info


        #print(ticker_info['longName'])
        return (ticker_info)
    def test(self):
        #test
        print(self)

if __name__=="__main__":
    tikr_data = TikerData("MSFT")
    print (tikr_data.getHistoricalData())