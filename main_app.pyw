#This sheet of code creates our "engine" which pulls in the data from the interface.py to create and run our GUI/Program

#Imports the required libraries and sheets
import sys
from interface import*
from PyQt5.QtWidgets import QApplication,QWidget

#Creates a class to create the interface based on the Widgets created on interface.py
class AppRun(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
       

#Creates the main function to run the program along with the exit functionality       
if __name__=="__main__":
    aplicacion = QtWidgets.QApplication(sys.argv)
    interface = AppRun()
    interface.show()

    sys.exit(aplicacion.exec_())
