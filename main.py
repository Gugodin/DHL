import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


from view.PrimeraVentana import Ui_MainWindow


class ventana(QMainWindow):

    listaPermisos = []

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.generateMap)
        

    def generateMap(self):
        print('Hola')
        # self.x2 =


         

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = ventana()
#     window.show()
#     sys.exit(app.exec())
