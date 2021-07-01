# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'itemadd.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from time import strftime, localtime

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 650)
        Form.setMinimumSize(QtCore.QSize(850, 650))
        Form.setMaximumSize(QtCore.QSize(850, 650))
        Form.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.itemname_cb = QtWidgets.QComboBox(Form)
        self.itemname_cb.setGeometry(QtCore.QRect(150, 80, 171, 51))
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
        self.itemname_cb.addItem("")
        self.itemID_cb = QtWidgets.QComboBox(Form)
        self.itemID_cb.setGeometry(QtCore.QRect(150, 140, 171, 51))
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
        self.itemID_cb.addItem("")
        self.item_loca_cb = QtWidgets.QComboBox(Form)
        self.item_loca_cb.setGeometry(QtCore.QRect(150, 200, 171, 51))
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
        self.item_loca_cb.addItem("")
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
        self.item_brand_cb = QtWidgets.QComboBox(Form)
        self.item_brand_cb.setGeometry(QtCore.QRect(150, 260, 171, 51))
        self.item_brand_cb.setStyleSheet("QComboBox {\n"
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
        self.item_brand_cb.setEditable(True)
        self.item_brand_cb.setObjectName("item_brand_cb")
        self.item_brand_cb.addItem("")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 260, 121, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.item_model_cb = QtWidgets.QComboBox(Form)
        self.item_model_cb.setGeometry(QtCore.QRect(150, 320, 171, 51))
        self.item_model_cb.setStyleSheet("QComboBox {\n"
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
        self.item_model_cb.setEditable(True)
        self.item_model_cb.setObjectName("item_model_cb")
        self.item_model_cb.addItem("")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 320, 121, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.item_value_cb = QtWidgets.QComboBox(Form)
        self.item_value_cb.setGeometry(QtCore.QRect(150, 380, 171, 51))
        self.item_value_cb.setStyleSheet("QComboBox {\n"
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
        self.item_value_cb.setEditable(True)
        self.item_value_cb.setObjectName("item_value_cb")
        self.item_value_cb.addItem("")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 380, 121, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(20, 440, 121, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.item_department = QtWidgets.QComboBox(Form)
        self.item_department.setGeometry(QtCore.QRect(150, 500, 171, 51))
        self.item_department.setStyleSheet("QComboBox {\n"
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
        self.item_department.setEditable(True)
        self.item_department.setObjectName("item_department")
        self.item_department.addItem("")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(20, 500, 121, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(370, 140, 121, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.item_user_cb = QtWidgets.QComboBox(Form)
        self.item_user_cb.setGeometry(QtCore.QRect(500, 80, 171, 51))
        self.item_user_cb.setStyleSheet("QComboBox {\n"
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
        self.item_user_cb.setEditable(True)
        self.item_user_cb.setObjectName("item_user_cb")
        self.item_user_cb.addItem("")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(370, 320, 121, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.item_contractNO_cb = QtWidgets.QComboBox(Form)
        self.item_contractNO_cb.setGeometry(QtCore.QRect(500, 200, 171, 51))
        self.item_contractNO_cb.setStyleSheet("QComboBox {\n"
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
        self.item_contractNO_cb.setEditable(True)
        self.item_contractNO_cb.setObjectName("item_contractNO_cb")
        self.item_contractNO_cb.addItem("")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(370, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(370, 200, 121, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.item_unit_cb = QtWidgets.QComboBox(Form)
        self.item_unit_cb.setGeometry(QtCore.QRect(500, 260, 171, 51))
        self.item_unit_cb.setStyleSheet("QComboBox {\n"
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
        self.item_unit_cb.setEditable(True)
        self.item_unit_cb.setObjectName("item_unit_cb")
        self.item_unit_cb.addItem("")
        self.item_condition_cb = QtWidgets.QComboBox(Form)
        self.item_condition_cb.setGeometry(QtCore.QRect(500, 140, 171, 51))
        self.item_condition_cb.setStyleSheet("QComboBox {\n"
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
        self.item_condition_cb.setEditable(True)
        self.item_condition_cb.setObjectName("item_condition_cb")
        self.item_condition_cb.addItem("")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(370, 260, 121, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(690, 80, 121, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.added_number_sb = QtWidgets.QSpinBox(Form)
        self.added_number_sb.setGeometry(QtCore.QRect(690, 130, 121, 41))
        self.added_number_sb.setMinimum(1)
        self.added_number_sb.setMaximum(999999)
        self.added_number_sb.setObjectName("added_number_sb")
        self.daoru_btn = QtWidgets.QPushButton(Form)
        self.daoru_btn.setEnabled(False)
        self.daoru_btn.setGeometry(QtCore.QRect(700, 190, 111, 41))
        self.daoru_btn.setStyleSheet("QPushButton {\n"
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
        self.daoru_btn.setIcon(icon)
        self.daoru_btn.setObjectName("daoru_btn")
        self.tipEdit_te = QtWidgets.QTextEdit(Form)
        self.tipEdit_te.setGeometry(QtCore.QRect(370, 370, 301, 181))
        self.tipEdit_te.setObjectName("tipEdit_te")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 560, 261, 51))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
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
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(380, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 10, 75, 31))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.item_changedata_cb = QtWidgets.QComboBox(Form)
        self.item_changedata_cb.setGeometry(QtCore.QRect(150, 440, 171, 51))
        self.item_changedata_cb.setStyleSheet("QComboBox {\n"
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
        self.item_changedata_cb.setEditable(True)
        self.item_changedata_cb.setObjectName("item_changedata_cb")
        self.item_changedata_cb.addItem("")
        self.item_changedata_cb.setItemText(0, strftime("%Y/%m/%d-/%H/%M/%S/", localtime()))
        self.added_step_sb = QtWidgets.QSpinBox(Form)
        self.added_step_sb.setGeometry(QtCore.QRect(690, 290, 121, 41))
        self.added_step_sb.setMinimum(1)
        self.added_step_sb.setMaximum(999999)
        self.added_step_sb.setObjectName("added_step_sb")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(690, 240, 121, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")

        self.retranslateUi(Form)
        self.pushButton_3.clicked.connect(Form.back_mainfunction)
        self.itemname_cb.currentTextChanged['QString'].connect(Form.added_btn_enable)
        self.itemID_cb.editTextChanged['QString'].connect(Form.added_btn_enable)
        self.item_loca_cb.editTextChanged['QString'].connect(Form.added_btn_enable)
        self.added_number_sb.valueChanged['int'].connect(Form.added_btn_enable)
        self.daoru_btn.clicked.connect(Form.added_check)
        self.pushButton_2.clicked.connect(Form.recently_added)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.itemname_cb.setItemText(0, _translate("Form", "电脑"))
        self.itemID_cb.setItemText(0, _translate("Form", "20150011"))
        self.item_loca_cb.setItemText(0, _translate("Form", "1-101"))
        self.label.setText(_translate("Form", "资产名称："))
        self.label_2.setText(_translate("Form", "资产编号："))
        self.label_4.setText(_translate("Form", "存放地点："))
        self.item_brand_cb.setItemText(0, _translate("Form", "戴尔"))
        self.label_5.setText(_translate("Form", "品  牌："))
        self.item_model_cb.setItemText(0, _translate("Form", "EXP-9980"))
        self.label_6.setText(_translate("Form", "规格型号："))
        self.item_value_cb.setItemText(0, _translate("Form", "20000.00元"))
        self.label_7.setText(_translate("Form", "价  值："))
        self.label_8.setText(_translate("Form", "取得日期："))
        self.item_department.setItemText(0, _translate("Form", "物电学院"))
        self.label_9.setText(_translate("Form", "使用部门："))
        self.label_3.setText(_translate("Form", "使用状况："))
        self.item_user_cb.setItemText(0, _translate("Form", "杨程钧"))
        self.label_10.setText(_translate("Form", "备注信息："))
        self.item_contractNO_cb.setItemText(0, _translate("Form", "A998989"))
        self.label_13.setText(_translate("Form", "使用人："))
        self.label_14.setText(_translate("Form", "合同编号："))
        self.item_unit_cb.setItemText(0, _translate("Form", "台"))
        self.item_condition_cb.setItemText(0, _translate("Form", "在用"))
        self.label_16.setText(_translate("Form", "计量单位："))
        self.label_11.setText(_translate("Form", "批量导入："))
        self.daoru_btn.setText(_translate("Form", "导入"))
        self.pushButton_2.setText(_translate("Form", "显示近期导入"))
        self.label_12.setText(_translate("Form", "资产入库"))
        self.pushButton_3.setText(_translate("Form", "返回主界面"))
        self.label_15.setText(_translate("Form", "编号步长："))
import login_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
