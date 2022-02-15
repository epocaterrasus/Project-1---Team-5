import sys
from ejemplo import*
from PyQt5.QtWidgets import QApplication,QWidget

class MiFormulario(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
       

       
if __name__=="__main__":
    aplicacion = QtWidgets.QApplication(sys.argv)
    mi_app = MiFormulario()
    mi_app.show()

    sys.exit(aplicacion.exec_())
