# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainFunction.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(607, 475)
        Form.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 591, 421))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.borrow_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.borrow_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.borrow_btn.setMaximumSize(QtCore.QSize(99999, 99999))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.borrow_btn.setFont(font)
        self.borrow_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(33, 174, 250);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(72, 203, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 255);\n"
"}")
        self.borrow_btn.setObjectName("borrow_btn")
        self.horizontalLayout.addWidget(self.borrow_btn)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_12.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_12.setMaximumSize(QtCore.QSize(99999, 99999))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(85, 85, 0);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"        \n"
"    background-color: rgb(185, 185, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 255);\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout.addWidget(self.pushButton_12)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.moveitem_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.moveitem_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.moveitem_btn.setMaximumSize(QtCore.QSize(99999, 99999))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.moveitem_btn.setFont(font)
        self.moveitem_btn.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(108, 217, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 255);\n"
"}")
        self.moveitem_btn.setObjectName("moveitem_btn")
        self.horizontalLayout_2.addWidget(self.moveitem_btn)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_10.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_10.setMaximumSize(QtCore.QSize(99999, 99999))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(206, 137, 0);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 255);\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_2.addWidget(self.pushButton_10)
        self.remove_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.remove_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.remove_btn.setMaximumSize(QtCore.QSize(99999, 99999))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.remove_btn.setFont(font)
        self.remove_btn.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(184, 61, 184);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(255, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 255);\n"
"}")
        self.remove_btn.setObjectName("remove_btn")
        self.horizontalLayout_2.addWidget(self.remove_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.datelog_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.datelog_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.datelog_btn.setMaximumSize(QtCore.QSize(99999, 99999))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.datelog_btn.setFont(font)
        self.datelog_btn.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(127, 127, 190);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 255);\n"
"}")
        self.datelog_btn.setObjectName("datelog_btn")
        self.horizontalLayout_3.addWidget(self.datelog_btn)
        self.datelog_btn_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.datelog_btn_3.setMinimumSize(QtCore.QSize(0, 0))
        self.datelog_btn_3.setMaximumSize(QtCore.QSize(99999, 99999))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.datelog_btn_3.setFont(font)
        self.datelog_btn_3.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(206, 137, 0);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 255);\n"
"}")
        self.datelog_btn_3.setObjectName("datelog_btn_3")
        self.horizontalLayout_3.addWidget(self.datelog_btn_3)
        self.exit_buttuon = QtWidgets.QPushButton(self.layoutWidget)
        self.exit_buttuon.setMinimumSize(QtCore.QSize(0, 0))
        self.exit_buttuon.setMaximumSize(QtCore.QSize(99999, 99999))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.exit_buttuon.setFont(font)
        self.exit_buttuon.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(204, 0, 0);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 255);\n"
"}")
        self.exit_buttuon.setObjectName("exit_buttuon")
        self.horizontalLayout_3.addWidget(self.exit_buttuon)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        self.exit_buttuon.clicked.connect(Form.show_login)
        self.datelog_btn.clicked.connect(Form.show_datalog)
        self.remove_btn.clicked.connect(Form.remove_item)
        self.moveitem_btn.clicked.connect(Form.move_item)
        self.pushButton_10.clicked.connect(Form.borrow_item)
        self.borrow_btn.clicked.connect(Form.add_item)
        self.datelog_btn_3.clicked.connect(Form.output_excel)
        self.pushButton_12.clicked.connect(Form.check_serch)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "实验室资产管理系统"))
        self.borrow_btn.setText(_translate("Form", "资产入库"))
        self.pushButton_12.setText(_translate("Form", "资产查询"))
        self.moveitem_btn.setText(_translate("Form", "资产移动"))
        self.pushButton_10.setText(_translate("Form", "资产借出"))
        self.remove_btn.setText(_translate("Form", "资产报废"))
        self.datelog_btn.setText(_translate("Form", "日志查询"))
        self.datelog_btn_3.setText(_translate("Form", "输出excel"))
        self.exit_buttuon.setText(_translate("Form", "退出系统"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
