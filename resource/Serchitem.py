# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Serchitem.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 650)
        Form.setMinimumSize(QtCore.QSize(850, 650))
        Form.setMaximumSize(QtCore.QSize(850, 650))
        Form.setStyleSheet("background-color: rgb(203, 203, 0);")
        self.itemname_cb = QtWidgets.QComboBox(Form)
        self.itemname_cb.setGeometry(QtCore.QRect(150, 80, 441, 51))
        self.itemname_cb.setStyleSheet("QComboBox {\n"
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
        self.itemname_cb.setEditable(True)
        self.itemname_cb.setObjectName("itemname_cb")
        self.itemID_cb = QtWidgets.QComboBox(Form)
        self.itemID_cb.setGeometry(QtCore.QRect(150, 140, 441, 51))
        self.itemID_cb.setStyleSheet("QComboBox {\n"
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
        self.itemID_cb.setEditable(True)
        self.itemID_cb.setObjectName("itemID_cb")
        self.item_loca_cb = QtWidgets.QComboBox(Form)
        self.item_loca_cb.setGeometry(QtCore.QRect(150, 200, 441, 51))
        self.item_loca_cb.setStyleSheet("QComboBox {\n"
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
        self.item_loca_cb.setEditable(True)
        self.item_loca_cb.setObjectName("item_loca_cb")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 121, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 121, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.serch_bt = QtWidgets.QPushButton(Form)
        self.serch_bt.setEnabled(False)
        self.serch_bt.setGeometry(QtCore.QRect(340, 390, 111, 41))
        self.serch_bt.setStyleSheet("QPushButton {\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/1/images/dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.serch_bt.setIcon(icon)
        self.serch_bt.setObjectName("serch_bt")
        self.showmain_bt = QtWidgets.QPushButton(Form)
        self.showmain_bt.setGeometry(QtCore.QRect(280, 560, 261, 51))
        self.showmain_bt.setStyleSheet("QPushButton {\n"
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
        self.showmain_bt.setFlat(False)
        self.showmain_bt.setObjectName("showmain_bt")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(360, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.back = QtWidgets.QPushButton(Form)
        self.back.setGeometry(QtCore.QRect(10, 10, 75, 31))
        self.back.setStyleSheet("QPushButton {\n"
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
        self.back.setObjectName("back")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(480, 400, 71, 31))
        self.checkBox.setObjectName("checkBox")
        self.QR = QtWidgets.QPushButton(Form)
        self.QR.setGeometry(QtCore.QRect(700, 30, 111, 101))
        self.QR.setStyleSheet("QPushButton {\n"
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
        self.QR.setFlat(False)
        self.QR.setObjectName("QR")

        self.retranslateUi(Form)
        self.back.clicked.connect(Form.back_mainfunction)
        self.checkBox.clicked['bool'].connect(Form.mohu_sherch)
        self.QR.clicked.connect(Form.saoyisao)
        self.itemname_cb.editTextChanged['QString'].connect(Form.serch_btn_enable)
        self.itemID_cb.editTextChanged['QString'].connect(Form.serch_btn_enable)
        self.item_loca_cb.editTextChanged['QString'].connect(Form.serch_btn_enable)
        self.serch_bt.clicked.connect(Form.serch_check)
        self.showmain_bt.clicked.connect(Form.recently_serched)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "资产名称："))
        self.label_2.setText(_translate("Form", "资产编号："))
        self.label_4.setText(_translate("Form", "存放地点："))
        self.serch_bt.setText(_translate("Form", "查询"))
        self.serch_bt.setShortcut(_translate("Form", "Return"))
        self.showmain_bt.setText(_translate("Form", "显示查询结果"))
        self.label_12.setText(_translate("Form", "资产查询"))
        self.back.setText(_translate("Form", "返回主界面"))
        self.checkBox.setText(_translate("Form", "模糊搜索"))
        self.QR.setText(_translate("Form", "扫一扫"))
import login_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
