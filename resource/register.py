# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        Form.setStyleSheet("QWidget#Form{\n"
"    \n"
"    border-image: url(:/1/images/2.jpg);\n"
"}\n"
"")
        self.menu_Button = QtWidgets.QPushButton(Form)
        self.menu_Button.setGeometry(QtCore.QRect(30, 40, 71, 71))
        self.menu_Button.setStyleSheet("\n"
"QPushButton    {\n"
"    border-radius:35px;\n"
"    \n"
"    background-color: rgb(80, 80, 80);\n"
"    \n"
"    border:2px solid rgb(0, 255, 255);\n"
"    \n"
"    color: rgb(170, 255, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover    {\n"
"\n"
"    \n"
"    border:4px solid rgb(255, 0, 0)\n"
"    \n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:checked    {\n"
"\n"
"    \n"
"    background-color: rgb(38, 89, 103)\n"
"    \n"
"}\n"
"\n"
"\n"
"")
        self.menu_Button.setCheckable(True)
        self.menu_Button.setObjectName("menu_Button")
        self.about_Button_2 = QtWidgets.QPushButton(Form)
        self.about_Button_2.setGeometry(QtCore.QRect(130, 140, 71, 71))
        self.about_Button_2.setStyleSheet("\n"
"QPushButton    {\n"
"    border-radius:35px;\n"
"    \n"
"    background-color: rgb(80, 80, 80);\n"
"    \n"
"    border:2px solid rgb(0, 255, 255);\n"
"    \n"
"    color: rgb(170, 255, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover    {\n"
"\n"
"    \n"
"    border:4px solid rgb(255, 0, 0)\n"
"    \n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:checked    {\n"
"\n"
"    \n"
"    background-color: rgb(38, 89, 103)\n"
"    \n"
"}\n"
"\n"
"\n"
"")
        self.about_Button_2.setCheckable(False)
        self.about_Button_2.setObjectName("about_Button_2")
        self.reset_Button_3 = QtWidgets.QPushButton(Form)
        self.reset_Button_3.setGeometry(QtCore.QRect(150, 30, 71, 71))
        self.reset_Button_3.setStyleSheet("\n"
"QPushButton    {\n"
"    border-radius:35px;\n"
"    \n"
"    background-color: rgb(80, 80, 80);\n"
"    \n"
"    border:2px solid rgb(0, 255, 255);\n"
"    \n"
"    color: rgb(170, 255, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover    {\n"
"\n"
"    \n"
"    border:4px solid rgb(255, 0, 0)\n"
"    \n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:checked    {\n"
"\n"
"    \n"
"    background-color: rgb(38, 89, 103)\n"
"    \n"
"}\n"
"\n"
"\n"
"")
        self.reset_Button_3.setCheckable(False)
        self.reset_Button_3.setObjectName("reset_Button_3")
        self.exit_Button_4 = QtWidgets.QPushButton(Form)
        self.exit_Button_4.setGeometry(QtCore.QRect(10, 160, 71, 71))
        self.exit_Button_4.setStyleSheet("\n"
"QPushButton    {\n"
"    border-radius:35px;\n"
"    \n"
"    background-color: rgb(80, 80, 80);\n"
"    \n"
"    border:2px solid rgb(0, 255, 255);\n"
"    \n"
"    color: rgb(170, 255, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover    {\n"
"\n"
"    \n"
"    border:4px solid rgb(255, 0, 0)\n"
"    \n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:checked    {\n"
"\n"
"    \n"
"    background-color: rgb(38, 89, 103)\n"
"    \n"
"}\n"
"\n"
"\n"
"")
        self.exit_Button_4.setCheckable(False)
        self.exit_Button_4.setObjectName("exit_Button_4")
        self.register_Button_5 = QtWidgets.QPushButton(Form)
        self.register_Button_5.setEnabled(False)
        self.register_Button_5.setGeometry(QtCore.QRect(270, 470, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(16)
        self.register_Button_5.setFont(font)
        self.register_Button_5.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 0, 127);\n"
"border-radius:20\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(255, 170, 255);\n"
"}\n"
"QPushButton:pressed    {\n"
"    \n"
"    background-color: rgb(255, 85, 0);\n"
"}\n"
"QPushButton:disabled    {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 180, 248);\n"
"}")
        self.register_Button_5.setObjectName("register_Button_5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 220, 131, 60))
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(246, 255, 162);")
        self.label.setLineWidth(2)
        self.label.setMidLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.id_line = QtWidgets.QLineEdit(Form)
        self.id_line.setGeometry(QtCore.QRect(320, 220, 301, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.id_line.setFont(font)
        self.id_line.setStyleSheet("background-color:transparent;\n"
"font: 16pt \"黑体\";\n"
"color: rgb(252, 255, 35);\n"
"border:none;\n"
"border-bottom:2px solid lightgray;")
        self.id_line.setClearButtonEnabled(True)
        self.id_line.setObjectName("id_line")
        self.passwd_line = QtWidgets.QLineEdit(Form)
        self.passwd_line.setGeometry(QtCore.QRect(320, 300, 301, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.passwd_line.setFont(font)
        self.passwd_line.setStyleSheet("background-color:transparent;\n"
"font: 16pt \"黑体\";\n"
"color: rgb(252, 255, 35);\n"
"border:none;\n"
"border-bottom:2px solid lightgray;")
        self.passwd_line.setClearButtonEnabled(True)
        self.passwd_line.setObjectName("passwd_line")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 300, 100, 60))
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(246, 255, 162);")
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(200, 380, 131, 60))
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(246, 255, 162);")
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setObjectName("label_3")
        self.confirm_line_6 = QtWidgets.QLineEdit(Form)
        self.confirm_line_6.setGeometry(QtCore.QRect(320, 370, 301, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.confirm_line_6.setFont(font)
        self.confirm_line_6.setStyleSheet("background-color:transparent;\n"
"font: 16pt \"黑体\";\n"
"color: rgb(252, 255, 35);\n"
"border:none;\n"
"border-bottom:2px solid lightgray;")
        self.confirm_line_6.setClearButtonEnabled(True)
        self.confirm_line_6.setObjectName("confirm_line_6")
        self.about_Button_2.raise_()
        self.reset_Button_3.raise_()
        self.exit_Button_4.raise_()
        self.register_Button_5.raise_()
        self.label.raise_()
        self.id_line.raise_()
        self.passwd_line.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.menu_Button.raise_()
        self.confirm_line_6.raise_()

        self.retranslateUi(Form)
        self.menu_Button.clicked.connect(Form.show_hide_menu)
        self.reset_Button_3.clicked.connect(Form.reset)
        self.exit_Button_4.clicked.connect(Form.exit_pane)
        self.about_Button_2.clicked.connect(Form.about)
        self.register_Button_5.clicked.connect(Form.register)
        self.menu_Button.clicked['bool'].connect(self.menu_Button.showMenu)
        self.id_line.textChanged['QString'].connect(Form.enable_text_button)
        self.passwd_line.textChanged['QString'].connect(Form.enable_text_button)
        self.confirm_line_6.textChanged['QString'].connect(Form.enable_text_button)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.menu_Button.setText(_translate("Form", "菜单"))
        self.about_Button_2.setText(_translate("Form", "关于"))
        self.reset_Button_3.setText(_translate("Form", "重置"))
        self.exit_Button_4.setText(_translate("Form", "退出"))
        self.register_Button_5.setText(_translate("Form", "注   册"))
        self.label.setText(_translate("Form", "账              号:"))
        self.label_2.setText(_translate("Form", "密           码:"))
        self.label_3.setText(_translate("Form", "确认密码:"))
import login_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
