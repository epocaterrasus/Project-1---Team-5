# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ejemplo.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#This file has no comments as it is automatically designed when using the PyQt Designer Software.

from PyQt5 import QtCore, QtGui, QtWidgets
from functions import *
from PyQt5.QtCore import QAbstractTableModel, Qt
from tickerdata import *
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
class QtTable(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None
class DataFrameModel(QtCore.QAbstractTableModel):
    DtypeRole = QtCore.Qt.UserRole + 1000
    ValueRole = QtCore.Qt.UserRole + 1001

    def __init__(self, df=pd.DataFrame(), parent=None):
        super(DataFrameModel, self).__init__(parent)
        self._dataframe = df

    def setDataFrame(self, dataframe):
        self.beginResetModel()
        self._dataframe = dataframe.copy()
        self.endResetModel()

    def dataFrame(self):
        return self._dataframe

    dataFrame = QtCore.pyqtProperty(pd.DataFrame, fget=dataFrame, fset=setDataFrame)

    @QtCore.pyqtSlot(int, QtCore.Qt.Orientation, result=str)
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self._dataframe.columns[section]
            else:
                return str(self._dataframe.index[section])
        return QtCore.QVariant()

    def rowCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return len(self._dataframe.index)

    def columnCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return self._dataframe.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < self.rowCount() \
            and 0 <= index.column() < self.columnCount()):
            return QtCore.QVariant()
        row = self._dataframe.index[index.row()]
        col = self._dataframe.columns[index.column()]
        dt = self._dataframe[col].dtype

        val = self._dataframe.iloc[row][col]
        if role == QtCore.Qt.DisplayRole:
            return str(val)
        elif role == DataFrameModel.ValueRole:
            return val
        if role == DataFrameModel.DtypeRole:
            return dt
        return QtCore.QVariant()

    def roleNames(self):
        roles = {
            QtCore.Qt.DisplayRole: b'display',
            DataFrameModel.DtypeRole: b'dtype',
            DataFrameModel.ValueRole: b'value'
        }
        return roles


class Ui_Form(object):
    def onClickButton(self):
        #print(self.lineEdit.text())
        ticker_data = TickerData(self.lineEdit.text())
        #Stock Info
        modelPyQt = QtTable(stockInfo(ticker_data))
        self.stockInfo.setModel(modelPyQt)
        self.stockInfo.setWindowTitle('Company data')
        self.stockInfo.resizeColumnsToContents()
        # stock Summary
        self.stockSummary.setText(stockSummary(ticker_data))
        # Pricing Info
        modelPricingInfo = QtTable(pricingInfo(ticker_data))
        self.pricingInfo.setModel(modelPricingInfo)
        self.pricingInfo.setWindowTitle('Company pricing info')
        self.pricingInfo.resizeColumnsToContents()
        #  analyst Summary
        modelAnalystSummary = QtTable(analystSummary(ticker_data))
        self.analystSummary.setModel(modelAnalystSummary)
        self.analystSummary.setWindowTitle('Company Analyst summary')
        self.analystSummary.resizeColumnsToContents()
        # Stock price evolution
        modelStockPriceEvolution = QtTable(stockpriceEvolution(ticker_data))
        self.stockpriceEvolution.setModel(modelStockPriceEvolution)
        self.stockpriceEvolution.setWindowTitle('Company Stock Price evolution')
        self.stockpriceEvolution.resizeColumnsToContents()
        # Common ratios
        modelCommonRatios = QtTable(getCommonRatios(ticker_data))
        self.getCommonRatios.setModel(modelCommonRatios)
        self.getCommonRatios.setWindowTitle('Company Stock Price evolution')
        self.getCommonRatios.resizeColumnsToContents()
        # News
        modelNews = QtTable( ticker_data.getNews())
        self.news.setModel(modelNews)
        self.news.setWindowTitle('Company news')
        self.news.resizeColumnsToContents()
        #Graph for one week
        dataOneWeek = ticker_data.history1Week()
        self.Graph1WeekClose.plot(dataOneWeek.Close.tolist())
        #Graph for one month
        dataOneMonth = ticker_data.history1Month()
        self.Graph1MonthClose.plot(dataOneMonth.Close.tolist())
        #Graph for three month
        dataThreeMonth = ticker_data.history3Month()
        self.Graph3MonthClose.plot(dataThreeMonth.Close.tolist())
        #Graph for One year
        dateOneYear = ticker_data.history1Year()
        self.Graph1YearClose.plot(dateOneYear.Close.tolist())
        #Graph for three year
        dateThreeYear = ticker_data.history3Year()
        self.Graph3YearClose.plot(dateThreeYear.Close.tolist())
        #axis = dataTest.Date.tolist()
        #xdict = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f'}
        #self.graphicsView.plot.setAxisItems({'bottom':axis})
        #self.labelCompanyName.setText(self.lineEdit.text())
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1330, 900)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(970, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 211, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("stonks.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(7, 130, 1321, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(970, 82, 111, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(1100, 30, 201, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(420, 30, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(470, 70, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(1100, 80, 201, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(1150, 0, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 140, 1301, 751))
        self.tabWidget.setObjectName("tabWidget")
        self.tabStockInfo = QtWidgets.QWidget()
        self.tabStockInfo.setObjectName("tabStockInfo")
        self.stockpriceEvolution = QtWidgets.QTableView(self.tabStockInfo)
        self.stockpriceEvolution.setGeometry(QtCore.QRect(0, 610, 500, 110))
        self.stockpriceEvolution.setObjectName("stockpriceEvolution")
        self.stockInfo = QtWidgets.QTableView(self.tabStockInfo)
        self.stockInfo.setGeometry(QtCore.QRect(0, 40, 500, 80))
        self.stockInfo.setObjectName("stockInfo")
        self.stockInfo.horizontalHeader().setStretchLastSection(True)
        self.stockInfo.verticalHeader().setDefaultSectionSize(50)
        self.analystSummary = QtWidgets.QTableView(self.tabStockInfo)
        self.analystSummary.setGeometry(QtCore.QRect(0, 440, 931, 71))
        self.analystSummary.setObjectName("analystSummary")
        self.pricingInfo = QtWidgets.QTableView(self.tabStockInfo)
        self.pricingInfo.setGeometry(QtCore.QRect(0, 530, 725, 60))
        self.pricingInfo.setObjectName("pricingInfo")
        self.getCommonRatios = QtWidgets.QTableView(self.tabStockInfo)
        self.getCommonRatios.setGeometry(QtCore.QRect(0, 350, 930, 60))
        self.getCommonRatios.setObjectName("getCommonRatios")
        self.stockSummary = QtWidgets.QTextBrowser(self.tabStockInfo)
        self.stockSummary.setGeometry(QtCore.QRect(510, 40, 771, 81))
        self.stockSummary.setObjectName("stockSummary")
        self.news = QtWidgets.QTableView(self.tabStockInfo)
        self.news.setGeometry(QtCore.QRect(0, 160, 1281, 161))
        self.news.setObjectName("news")
        self.CompanyInfo = QtWidgets.QLabel(self.tabStockInfo)
        self.CompanyInfo.setGeometry(QtCore.QRect(160, 10, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CompanyInfo.setFont(font)
        self.CompanyInfo.setObjectName("CompanyInfo")
        self.CompanySummary = QtWidgets.QLabel(self.tabStockInfo)
        self.CompanySummary.setGeometry(QtCore.QRect(670, 10, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CompanySummary.setFont(font)
        self.CompanySummary.setObjectName("CompanySummary")
        self.CompanyNews = QtWidgets.QLabel(self.tabStockInfo)
        self.CompanyNews.setGeometry(QtCore.QRect(470, 130, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CompanyNews.setFont(font)
        self.CompanyNews.setObjectName("CompanyNews")
        self.CompanyRatios = QtWidgets.QLabel(self.tabStockInfo)
        self.CompanyRatios.setGeometry(QtCore.QRect(430, 320, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CompanyRatios.setFont(font)
        self.CompanyRatios.setObjectName("CompanyRatios")
        self.CompanyForecasts = QtWidgets.QLabel(self.tabStockInfo)
        self.CompanyForecasts.setGeometry(QtCore.QRect(420, 410, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CompanyForecasts.setFont(font)
        self.CompanyForecasts.setObjectName("CompanyForecasts")
        self.CompanyPriceMovement = QtWidgets.QLabel(self.tabStockInfo)
        self.CompanyPriceMovement.setGeometry(QtCore.QRect(270, 510, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CompanyPriceMovement.setFont(font)
        self.CompanyPriceMovement.setObjectName("CompanyPriceMovement")
        self.CompanyPriceHistoricals = QtWidgets.QLabel(self.tabStockInfo)
        self.CompanyPriceHistoricals.setGeometry(QtCore.QRect(150, 590, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CompanyPriceHistoricals.setFont(font)
        self.CompanyPriceHistoricals.setObjectName("CompanyPriceHistoricals")
        self.tabWidget.addTab(self.tabStockInfo, "")
        self.tabGraphs = QtWidgets.QWidget()
        self.tabGraphs.setObjectName("tabGraphs")
        self.Graph1WeekClose =pg.PlotWidget(self.tabGraphs)
        self.Graph1WeekClose.setGeometry(QtCore.QRect(10, 40, 401, 271))
        self.Graph1WeekClose.setObjectName("Graph1WeekClose")
        self.Graph1MonthClose = pg.PlotWidget(self.tabGraphs)
        self.Graph1MonthClose.setGeometry(QtCore.QRect(430, 40, 401, 271))
        self.Graph1MonthClose.setObjectName("Graph1MonthClose")
        self.Graph3MonthClose =pg.PlotWidget(self.tabGraphs)
        self.Graph3MonthClose.setGeometry(QtCore.QRect(850, 40, 401, 271))
        self.Graph3MonthClose.setObjectName("Graph3MonthClose")
        self.Graph1YearClose = pg.PlotWidget(self.tabGraphs)
        self.Graph1YearClose.setGeometry(QtCore.QRect(190, 360, 401, 271))
        self.Graph1YearClose.setObjectName("Graph1YearClose")
        self.Graph3YearClose = pg.PlotWidget(self.tabGraphs)
        self.Graph3YearClose.setGeometry(QtCore.QRect(610, 360, 401, 271))
        self.Graph3YearClose.setObjectName("Graph3YearClose")
        self.Graph1Week = QtWidgets.QLabel(self.tabGraphs)
        self.Graph1Week.setGeometry(QtCore.QRect(110, 10, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Graph1Week.setFont(font)
        self.Graph1Week.setObjectName("Graph1Week")
        self.Graph1Month = QtWidgets.QLabel(self.tabGraphs)
        self.Graph1Month.setGeometry(QtCore.QRect(540, 10, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Graph1Month.setFont(font)
        self.Graph1Month.setObjectName("Graph1Month")
        self.Graph3Month = QtWidgets.QLabel(self.tabGraphs)
        self.Graph3Month.setGeometry(QtCore.QRect(960, 10, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Graph3Month.setFont(font)
        self.Graph3Month.setObjectName("Graph3Month")
        self.Graph1Year = QtWidgets.QLabel(self.tabGraphs)
        self.Graph1Year.setGeometry(QtCore.QRect(310, 330, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Graph1Year.setFont(font)
        self.Graph1Year.setObjectName("Graph1Year")
        self.Graph3Year = QtWidgets.QLabel(self.tabGraphs)
        self.Graph3Year.setGeometry(QtCore.QRect(720, 330, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Graph3Year.setFont(font)
        self.Graph3Year.setObjectName("Graph3Year")
        self.tabWidget.addTab(self.tabGraphs, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(self.onClickButton) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "RUN"))
        self.label_3.setText(_translate("Form", "1. Please enter your desired stock Ticker in the Box                                                     "))
        self.label.setText(_translate("Form", "STONKS ANALYZER V.1"))
        self.label_4.setText(_translate("Form", "a Blumberg Inc. Production"))
        self.label_5.setText(_translate("Form", "2. Hit Run"))
        self.label_6.setText(_translate("Form", "Instructions"))
        self.CompanyInfo.setText(_translate("Form", "Company Information"))
        self.CompanySummary.setText(_translate("Form", "Company Summary"))
        self.CompanyNews.setText(_translate("Form", "Company News"))
        self.CompanyRatios.setText(_translate("Form", "Company Ratios"))
        self.CompanyForecasts.setText(_translate("Form", "Company Forecasts"))
        self.CompanyPriceMovement.setText(_translate("Form", "Company Price Movement"))
        self.CompanyPriceHistoricals.setText(_translate("Form", "Company Price Historicals"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStockInfo), _translate("Form", "Stock Information"))
        self.Graph1Week.setText(_translate("Form", "Closing Prices 1 Week"))
        self.Graph1Month.setText(_translate("Form", "Closing Prices 1 Months"))
        self.Graph3Month.setText(_translate("Form", "Closing Prices 3 Months"))
        self.Graph1Year.setText(_translate("Form", "Closing Prices 1 Year"))
        self.Graph3Year.setText(_translate("Form", "Closing Prices 3 Year"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGraphs), _translate("Form", "Graphs"))
