# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modle.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(789, 716)
        Dialog.setSizeGripEnabled(False)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 771, 711))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mytableview = QtWidgets.QTableView(self.layoutWidget)
        self.mytableview.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.mytableview.setObjectName("mytableview")
        self.horizontalLayout.addWidget(self.mytableview)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.clean_bt = QtWidgets.QPushButton(self.layoutWidget)
        self.clean_bt.setEnabled(False)
        self.clean_bt.setMinimumSize(QtCore.QSize(20, 50))
        self.clean_bt.setStyleSheet("QPushButton {\n"
"    background-color: rgb(33, 174, 250);\n"
"    border-radius: 15px;\n"
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
        self.clean_bt.setIcon(icon)
        self.clean_bt.setObjectName("clean_bt")
        self.verticalLayout.addWidget(self.clean_bt)
        self.addline_bt = QtWidgets.QPushButton(self.layoutWidget)
        self.addline_bt.setEnabled(False)
        self.addline_bt.setMinimumSize(QtCore.QSize(20, 50))
        self.addline_bt.setStyleSheet("QPushButton {\n"
"    background-color: rgb(33, 174, 250);\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(72, 203, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 255);\n"
"}")
        self.addline_bt.setIcon(icon)
        self.addline_bt.setObjectName("addline_bt")
        self.verticalLayout.addWidget(self.addline_bt)
        self.delline_bt = QtWidgets.QPushButton(self.layoutWidget)
        self.delline_bt.setEnabled(False)
        self.delline_bt.setMinimumSize(QtCore.QSize(20, 50))
        self.delline_bt.setStyleSheet("QPushButton {\n"
"    background-color: rgb(33, 174, 250);\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(72, 203, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 255);\n"
"}")
        self.delline_bt.setIcon(icon)
        self.delline_bt.setObjectName("delline_bt")
        self.verticalLayout.addWidget(self.delline_bt)
        self.borrow_bt = QtWidgets.QPushButton(self.layoutWidget)
        self.borrow_bt.setEnabled(False)
        self.borrow_bt.setMinimumSize(QtCore.QSize(20, 50))
        self.borrow_bt.setStyleSheet("QPushButton {\n"
"    background-color: rgb(33, 174, 250);\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(72, 203, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 255);\n"
"}")
        self.borrow_bt.setIcon(icon)
        self.borrow_bt.setObjectName("borrow_bt")
        self.verticalLayout.addWidget(self.borrow_bt)
        self.move_bt = QtWidgets.QPushButton(self.layoutWidget)
        self.move_bt.setEnabled(False)
        self.move_bt.setMinimumSize(QtCore.QSize(20, 50))
        self.move_bt.setStyleSheet("QPushButton {\n"
"    background-color: rgb(33, 174, 250);\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(72, 203, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 255);\n"
"}")
        self.move_bt.setIcon(icon)
        self.move_bt.setObjectName("move_bt")
        self.verticalLayout.addWidget(self.move_bt)
        self.scrapped_bt = QtWidgets.QPushButton(self.layoutWidget)
        self.scrapped_bt.setEnabled(False)
        self.scrapped_bt.setMinimumSize(QtCore.QSize(20, 50))
        self.scrapped_bt.setStyleSheet("QPushButton {\n"
"    background-color: rgb(33, 174, 250);\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(72, 203, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 255);\n"
"}")
        self.scrapped_bt.setIcon(icon)
        self.scrapped_bt.setObjectName("scrapped_bt")
        self.verticalLayout.addWidget(self.scrapped_bt)
        self.repair_bt = QtWidgets.QPushButton(self.layoutWidget)
        self.repair_bt.setEnabled(False)
        self.repair_bt.setMinimumSize(QtCore.QSize(20, 50))
        self.repair_bt.setStyleSheet("QPushButton {\n"
"    background-color: rgb(33, 174, 250);\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(72, 203, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 255);\n"
"}")
        self.repair_bt.setIcon(icon)
        self.repair_bt.setObjectName("repair_bt")
        self.verticalLayout.addWidget(self.repair_bt)
        self.maintain_bt = QtWidgets.QPushButton(self.layoutWidget)
        self.maintain_bt.setEnabled(False)
        self.maintain_bt.setMinimumSize(QtCore.QSize(20, 50))
        self.maintain_bt.setStyleSheet("QPushButton {\n"
"    background-color: rgb(33, 174, 250);\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(72, 203, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 255);\n"
"}")
        self.maintain_bt.setIcon(icon)
        self.maintain_bt.setObjectName("maintain_bt")
        self.verticalLayout.addWidget(self.maintain_bt)
        self.output_bt = QtWidgets.QPushButton(self.layoutWidget)
        self.output_bt.setEnabled(False)
        self.output_bt.setMinimumSize(QtCore.QSize(20, 50))
        self.output_bt.setStyleSheet("QPushButton {\n"
"    background-color: rgb(33, 174, 250);\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(72, 203, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 255);\n"
"}")
        self.output_bt.setIcon(icon)
        self.output_bt.setObjectName("output_bt")
        self.verticalLayout.addWidget(self.output_bt)
        self.upload_bt = QtWidgets.QPushButton(self.layoutWidget)
        self.upload_bt.setMinimumSize(QtCore.QSize(20, 50))
        self.upload_bt.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(189, 63, 0);\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(255, 85, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 255);\n"
"}")
        self.upload_bt.setIcon(icon)
        self.upload_bt.setObjectName("upload_bt")
        self.verticalLayout.addWidget(self.upload_bt)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)
        self.verticalLayout.setStretch(9, 2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 6)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Dialog)
        self.clean_bt.clicked.connect(Dialog.check_clean)
        self.addline_bt.clicked.connect(Dialog.check_delline)
        self.delline_bt.clicked.connect(Dialog.check_delline)
        self.borrow_bt.clicked.connect(Dialog.check_borrow)
        self.move_bt.clicked.connect(Dialog.check_move)
        self.scrapped_bt.clicked.connect(Dialog.check_scrapped)
        self.repair_bt.clicked.connect(Dialog.check_repair)
        self.maintain_bt.clicked.connect(Dialog.check_maintain)
        self.upload_bt.clicked.connect(Dialog.cheack_upload)
        self.output_bt.clicked.connect(Dialog.check_output)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.clean_bt.setText(_translate("Dialog", "清空列表"))
        self.addline_bt.setText(_translate("Dialog", "增加一行"))
        self.delline_bt.setText(_translate("Dialog", "删除一行"))
        self.borrow_bt.setText(_translate("Dialog", "借出"))
        self.move_bt.setText(_translate("Dialog", "转移"))
        self.scrapped_bt.setText(_translate("Dialog", "待报废"))
        self.repair_bt.setText(_translate("Dialog", "待维修"))
        self.maintain_bt.setText(_translate("Dialog", "维护保养"))
        self.output_bt.setText(_translate("Dialog", "输出excel"))
        self.upload_bt.setText(_translate("Dialog", "同步修改"))
import login_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
