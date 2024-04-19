from PyQt5.Qt import *

from welcome import MainWindow
from signup  import Dialog           
import sqlite3


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(496, 265)
        #Dialog.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.u_name_label = QLabel(Dialog)
        self.u_name_label.setGeometry(QRect(150, 110, 71, 20))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        '''
        .setGeometry(QtCore.QRect(70, 120, 191, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(31, 32, 41);\n"
                                    "border-color: rgb(31, 32, 41);\n"
                                    "color: rgb(211, 211, 211);")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        '''
        #self.u_name_label.setGeometry(QRect(70,120,190,30))
        self.u_name_label.setFont(font)
        self.u_name_label.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                    "border-color: rgb(31, 32, 41);\n"
                                    "color: rgb(211, 211, 211);")
        self.u_name_label.setAlignment(Qt.AlignCenter)
        self.u_name_label.setObjectName("u_name_label")
        self.pass_label = QLabel(Dialog)
        self.pass_label.setGeometry(QRect(150, 150, 71, 21))
        font = QFont()
        font.setPointSize(10)
        self.pass_label.setFont(font)
        self.pass_label.setAlignment(Qt.AlignCenter)
        self.pass_label.setObjectName("pass_label")
        self.uname_lineEdit = QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QRect(230, 110, 113, 20))
        self.uname_lineEdit.setObjectName("uname_lineEdit")
        self.pass_lineEdit = QLineEdit(Dialog)
        self.pass_lineEdit.setGeometry(QRect(230, 150, 113, 20))
        self.pass_lineEdit.setEchoMode(QLineEdit.Password)  # Маскируем вводимые символы
        self.pass_lineEdit.setStyleSheet("border: 1px solid #6384ff;\n"
                                        "border-radius: 8px;\n"
                                        "padding: 0 5px;\n"
                                        "background: #ADBEFF;\n"
                                        "selection-background-color: darkgray;\n")
        self.pass_lineEdit.setObjectName("pass_lineEdit")
        self.login_btn = QPushButton(Dialog)
        self.login_btn.setGeometry(QRect(130, 200, 100, 30))
        self.login_btn.setObjectName("login_btn")
        self.login_btn.setFlat(True)
        style = '''
QPushButton {
	background-color: #6384ff;
	color: #fff;
	border: none;
	min-width: 30px;
	border-radius: 5px;
}

QPushButton::flat {
	background-color: transparent;
	border: none;
	color: #000;
	border-radius: 5px;
}

QPushButton::disabled {
	background-color: #606060;
	color: #959595;
	border: none;
	border-radius: 5px;
}

QPushButton::hover {
	background-color: #718fff;
	border: 2px solid #718fff;
	border-radius: 5px;
}

QPushButton::pressed {
	background-color: #446cff;
	border: 1px solid #446cff;
	border-radius: 5px;
}

QPushButton::checked {
	background-color: #3761ff;
	border: 1px solid #3761ff;
	border-radius: 5px;
}
'''
        self.login_btn.setStyleSheet(style)

        #self.login_btn.setStyleSheet("background-color: rgb(0, 0, 255);\n"
        #                            "border-color: rgb(31, 32, 41);\n"
        #                            "border-radius: 5px;\n"
        #                            "color: rgb(211, 211, 211);")

        self.signup_btn = QPushButton(Dialog)
        self.signup_btn.setGeometry(QRect(240, 200, 100, 30))
        self.signup_btn.setObjectName("signup_btn")
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(190, 10, 211, 51))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login Form"))
        self.u_name_label.setText(_translate("Dialog", "USERNAME "))
        self.pass_label.setText(_translate("Dialog", "PASSWORD"))
        self.login_btn.setText(_translate("Dialog", "Login"))
        self.signup_btn.setText(_translate("Dialog", "Sign Up"))
        self.label.setText(_translate("Dialog", "Login Form"))


class LoginDatabase():
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def is_table(self, table_name):
        query = "SELECT name from sqlite_master WHERE type='table' AND name='{}';".format(table_name)
        cursor = self.conn.execute(query)
        result = cursor.fetchone()
        if result == None:
            return False
        else:
            return True


class MainDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.loginDatabase = LoginDatabase('sources/login.db')
        if self.loginDatabase.is_table('USERS'):
            pass
        else:
            self.loginDatabase.conn.execute("CREATE TABLE IF NOT EXIST USERS(USERNAME TEXT NOT NULL, EMAIL TEXT, PASSWORD TEXT)")
            self.loginDatabase.conn.execute("INSERT INTO USERS VALUES(?, ?, ?)", 
                                           ('admin', 'admin@gmail.com', 'admin') 
            )
            self.loginDatabase.conn.commit()

        self.login_btn.clicked.connect(self.loginCheck)
        self.signup_btn.clicked.connect(self.signUpCheck)        

    def showMessageBox(self, title, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def welcomeWindowShow(self, username):
        self.welcomeWindow = MainWindow(username)
        self.welcomeWindow.show()

    def signUpShow(self):
        self.signUpWindow = Dialog(self)
        self.signUpWindow.show()

    def loginCheck(self):
        username = self.uname_lineEdit.text()
        password = self.pass_lineEdit.text()
        if (not username) or (not password):
            msg = QMessageBox.information(self, 'Внимание!', 'Вы не заполнили все поля.')
            return

        result = self.loginDatabase.conn.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",
                                                 (username, password))
        if len(result.fetchall()):     
            self.welcomeWindowShow(username)
            self.hide()
            self.loginDatabase.conn.close()
        else:
            self.showMessageBox('Внимание!', 'Неправильное имя пользователя или пароль.')

    def signUpCheck(self):
        self.signUpShow()


if __name__ == "__main__":
    import sys
    app    = QApplication(sys.argv)
    w = MainDialog()
    w.show()
    sys.exit(app.exec_())