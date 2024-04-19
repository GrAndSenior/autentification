from PyQt5.Qt import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(466, 283)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(120, 30, 231, 51))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QRect(140, 120, 211, 51))
        font = QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Добро пожаловать!"))
        self.label_2.setText(_translate("MainWindow", "Хорошего вам дня!"))


class MainWindow(QMainWindow, Ui_MainWindow):          
    def __init__(self, name='admin'):
        super().__init__()
        self.setupUi(self)

        self.label.setText('{} {}'.format(self.label.text(), name))
        gridLayout = QGridLayout(self.centralwidget)
        gridLayout.addWidget(self.label)
        gridLayout.addWidget(self.label_2)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())