# Stock Analyzer Tool

The Stonks Analyzer (v.1.0) is a GUI stock monitoring tool that aims to balance retail investors' playing field by providing a platform for fundamental and technical analysis of US and international equities. The monitor will pull up real-time information using the Yahoo Finance API. The functionality is simple first input the ticker of the desired stock. The first version offers the following information:

* Company Information: Ticker, Name, Sector, and Industry
* Business Summary
* Latest News
* Ratios: Trailing PE, Forward PE, Trailing EPS, ROE, TEV/Sales, TEV/EBITDA, Total Debt/Equity, Total Debt/EBITDA, Total Debt/TEV, and Price to Book
* Forecasts
* Price Movement
* Historical Prices
* Pricing Graphs

### Coming Soon Stonks Analyzer V.2

For a future release (v.2.0), we aim to have the following upgrades:

* UI/UX Improvements
* Function optimization to make loading speeds faster
* Improved graphing: We aim to have more graphing functionality, starting with fixing the labeling and identification as well as adding multifunctional graphs that display overlayed pricing and volume as well as other functionalities such as the abilities to add moving averages, exponential moving averages, etc.
* Additional information: We will add more details to give the user/investor more tools to make an informed investment decision
* Adding a ranking system using metrics inspired by William O'Neill's CANSLIM system.


---

## Technologies

The following technologies were used to build and deploy this application:

* Python - Version 3.9.7
* Anaconda (Which includes Jupyter Lab and Pandas)
* Path (from pathlib)
* PyQt
* PyQtGraph
* Yahoo Finance API

---

## Installation and Usage Guide

### 1. Install Python 3.9.7

For installing Python 3.9.7 you can find the Installation Files for both Windows/Mac OS in the following link
 * [Anaconda Installation Files](https://www.anaconda.com/products/individual "Anaconda Installation Files")

If you require assistance installing it, you can follow the following videos for guidance
* [Youtube Video Python Installation Guide - Windows](https://www.youtube.com/watch?v=uSVl7gRXP80 "Python Installation Video - Windows") 
* [Youtube Video Python Installation Guide - Mac](https://www.youtube.com/watch?v=r6bBaj797t8 "Python Installation Video - Mac") 
 
### 2. Install Anaconda

For installing Python 3.9.7 you can find the Installation Files for both Windows/Mac OS in the following link
 * [Python Installation Guide](https://www.python.org/downloads/release/python-397/ "Python Installation Guide")

If you require assistance installing it, you can follow the following videos for guidance
* [Youtube Video Anaconda Installation Guide - Windows](https://www.youtube.com/watch?v=g6ln1dAt-RI "Anaconda Installation Video - Windows") 
* [Youtube Video Anaconda Installation Guide - Mac](https://www.youtube.com/watch?v=oWVTO_69U4c "Anaconda Installation Video - Mac")

### 3. Installing Required Librabries

For installing the Yahoo Finance API please follow the following link
 * [Yahoo Finance API Installation](https://pypi.org/project/yfinance/ "Yahoo Finance API Installation")

 For installing the PyQT and PYQt Graph libraries please follow the following link
 * [PyQT5 Installation Guide](https://doc.bccnsoft.com/docs/PyQt5/installation.html "PyQT 5 Installation Guide")


### 3. Downloading the Stock Monitor Repository

Navigate to your desired location where you would like to save the documents for this application. You can do this by using the ```cd``` command followed by a space and the file path inside quotations ```" file path "```. In my example I have gone to Desktop.

![image](https://user-images.githubusercontent.com/94983278/149385012-181d1769-0af6-487e-8e04-823a28f2c3ed.png)

Clone this project's repository from GitHub using the following command 

```https://github.com/epocaterrasus/StockMonitor.git```

### 4. Opening the Stock Monitor

Being in the folder created when you downloaded the repository type ```python main_app.pyw```, this will open the window, the next step would be to input your desired ticker in the top right corner and start exploring!

---


## Images

![image](https://user-images.githubusercontent.com/94983278/154855624-eeed02e5-6d84-4c1e-9012-517c506bf2dd.png)

---

## Contributors

Edgar Pocaterra - epocaterra@protonmail.ch / +1 806 283 5455

Nico Cortese - nicolasacortese@gmail.com / +1 315 868 8027

Donika Berisha

Jerry Ross

---

## License

MIT License

Copyright (c) 2022 epocaterrasus

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
