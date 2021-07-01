# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_top_bg_ = QtWidgets.QLabel(self.widget)
        self.login_top_bg_.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.login_top_bg_.setText("")
        self.login_top_bg_.setObjectName("login_top_bg_")
        self.horizontalLayout.addWidget(self.login_top_bg_)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setStyleSheet("color: rgb(138, 138, 138)")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 30, -1, 10)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.passwd_line = QtWidgets.QLineEdit(self.widget_2)
        self.passwd_line.setMinimumSize(QtCore.QSize(0, 45))
        self.passwd_line.setStyleSheet("QLineEdit {\n"
"    font-size: 20px;\n"
"    border: none;\n"
"    border-bottom: 1px solid lightgray;\n"
"    background-color: transparent;\n"
"}\n"
"QLineEdit:hover {\n"
"    border-bottom: 1px solid gray;\n"
"}\n"
"QLineEdit:focus {\n"
"    border-bottom: 1px solid rgb(18, 183, 245);\n"
"}\n"
"")
        self.passwd_line.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.passwd_line.setClearButtonEnabled(True)
        self.passwd_line.setObjectName("passwd_line")
        self.gridLayout.addWidget(self.passwd_line, 1, 0, 1, 2)
        self.auto_log = QtWidgets.QCheckBox(self.widget_2)
        self.auto_log.setStyleSheet("color: rgb(149, 149, 149);")
        self.auto_log.setObjectName("auto_log")
        self.gridLayout.addWidget(self.auto_log, 2, 0, 1, 1)
        self.account_Box = QtWidgets.QComboBox(self.widget_2)
        self.account_Box.setMinimumSize(QtCore.QSize(0, 45))
        self.account_Box.setStyleSheet("QComboBox {\n"
"    font-size: 20px;\n"
"    border: none;\n"
"    border-bottom: 1px solid lightgray;\n"
"    background-color: transparent;\n"
"}\n"
"QComboBox:hover {\n"
"    border-bottom: 1px solid gray;\n"
"}\n"
"QComboBox:focus {\n"
"    border-bottom: 1px solid rgb(18, 183, 245);\n"
"}\n"
"QComboBox::drop-down {\n"
"    background-color: transparent;    \n"
"    width: 60px;\n"
"    height: 40px;               \n"
"}\n"
"QComboBox::down-arrow {\n"
"    \n"
"    image: url(:/1/images/down_arrow.png);\n"
"    width: 60px;\n"
"    height: 20px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    min-height: 60px;\n"
"}\n"
"QComboBox QAbstractItemView:item {\n"
"    color: lightblue;\n"
"}")
        self.account_Box.setEditable(True)
        self.account_Box.setObjectName("account_Box")
        self.account_Box.addItem("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/1/images/th_untangle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_Box.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/1/images/管它.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_Box.addItem(icon1, "")
        self.gridLayout.addWidget(self.account_Box, 0, 0, 1, 2)
        self.hold_passwd = QtWidgets.QCheckBox(self.widget_2)
        self.hold_passwd.setStyleSheet("color: rgb(149, 149, 149);")
        self.hold_passwd.setObjectName("hold_passwd")
        self.gridLayout.addWidget(self.hold_passwd, 2, 1, 1, 1)
        self.login_button = QtWidgets.QPushButton(self.widget_2)
        self.login_button.setEnabled(False)
        self.login_button.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(10)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(33, 174, 250);\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(72, 203, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 255);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/1/images/dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_button.setIcon(icon2)
        self.login_button.setIconSize(QtCore.QSize(30, 50))
        self.login_button.setObjectName("login_button")
        self.gridLayout.addWidget(self.login_button, 3, 0, 1, 2)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_3.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_3.setStyleSheet("border-image: url(:/1/images/gui_qq_group.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 5)

        self.retranslateUi(Form)
        self.account_Box.editTextChanged['QString'].connect(Form.enable_login_btn)
        self.passwd_line.textChanged['QString'].connect(Form.enable_login_btn)
        self.pushButton_3.clicked.connect(Form.join_qq_group)
        self.pushButton_2.clicked.connect(Form.show_register)
        self.login_button.clicked.connect(Form.check_login)
        self.auto_log.clicked['bool'].connect(Form.auto_login)
        self.hold_passwd.clicked['bool'].connect(Form.rememble_passwd)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.account_Box, self.passwd_line)
        Form.setTabOrder(self.passwd_line, self.auto_log)
        Form.setTabOrder(self.auto_log, self.hold_passwd)
        Form.setTabOrder(self.hold_passwd, self.login_button)
        Form.setTabOrder(self.login_button, self.pushButton_2)
        Form.setTabOrder(self.pushButton_2, self.pushButton_3)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录"))
        self.pushButton_2.setText(_translate("Form", "注册账号"))
        self.auto_log.setText(_translate("Form", "自动登录"))
        self.account_Box.setItemText(0, _translate("Form", "yang"))
        self.account_Box.setItemText(1, _translate("Form", "wudianshiyanshi"))
        self.account_Box.setItemText(2, _translate("Form", "931363918"))
        self.hold_passwd.setText(_translate("Form", "记住密码"))
        self.login_button.setText(_translate("Form", "安全登录"))
        self.login_button.setShortcut(_translate("Form", "Return"))
import login_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
