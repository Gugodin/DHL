from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 420)
        MainWindow.setMinimumSize(QSize(750, 420))
        MainWindow.setMaximumSize(QSize(750, 420))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.x1 = QLineEdit(self.centralwidget)
        self.x1.setObjectName(u"x1")
        self.x1.setGeometry(QRect(230, 160, 41, 31))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(330, 340, 91, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 50, 311, 41))
        font = QFont()
        font.setFamily(u"MS Gothic")
        font.setPointSize(20)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(QFont.Bold)
        self.label.setFont(font)
        self.label.setCursor(QCursor(Qt.ArrowCursor))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 160, 121, 31))
        font1 = QFont()
        font1.setFamily(u"PMingLiU-ExtB")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(QFont.Bold)
        self.label_2.setFont(font1)
        self.label_2.setCursor(QCursor(Qt.ArrowCursor))
        self.x2 = QLineEdit(self.centralwidget)
        self.x2.setObjectName(u"x2")
        self.x2.setGeometry(QRect(300, 160, 41, 31))
        self.y2 = QLineEdit(self.centralwidget)
        self.y2.setObjectName(u"y2")
        self.y2.setGeometry(QRect(650, 160, 41, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(440, 160, 121, 31))
        self.label_3.setFont(font1)
        self.label_3.setCursor(QCursor(Qt.ArrowCursor))
        self.y1 = QLineEdit(self.centralwidget)
        self.y1.setObjectName(u"y1")
        self.y1.setGeometry(QRect(580, 160, 41, 31))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 250, 171, 31))
        self.label_4.setFont(font1)
        self.label_4.setCursor(QCursor(Qt.ArrowCursor))
        self.nuCiudades = QLineEdit(self.centralwidget)
        self.nuCiudades.setObjectName(u"nuCiudades")
        self.nuCiudades.setGeometry(QRect(400, 260, 51, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Generar mapa", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ruta de DHL imaginario", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Intervalo de X", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Intervalo de Y", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Numero de ciudades", None))
    


