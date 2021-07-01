
import sys
# import traceback
from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from PyQt5 import QtCore, QtGui, QtWidgets
# import sqlite3
#import createDB


def createDB(Recent_dbname):

    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(Recent_dbname)
    if not db.open():
        print('无法连接数据库')
        return False
    query = QSqlQuery()
    query.exec('create table people(id int primary key ,name varchar(10),address varchar (50))')
    query.exec('insert into people values(0,"lining","shengzheng")')
    query.exec('insert into people values(1,"wang","shengzheng")')
    query.exec('insert into people values(2,"wang","shengzheng")')
    query.exec('insert into people values(3,"wang","shengzheng")')
    query.exec('insert into people values(4,"wang","shengzheng")')
    db.close()
    return  True


#2、定义初始化函数
def initialzeModel(model):
    #设置表头
    model.setTable('mylog')
    #设置编辑策略（当表变化时）
    model.setEditStrategy(QSqlTableModel.OnFieldChange)
    #装在数据
    model.select()
    #设置字段头
    model.setHeaderData(0,Qt.Horizontal,'ID')
    model.setHeaderData(1,Qt.Horizontal,'资产编号')
    model.setHeaderData(2,Qt.Horizontal,'资产名称')
    model.setHeaderData(3, Qt.Horizontal, '计量单位')
    model.setHeaderData(4,Qt.Horizontal,'品  牌')
    model.setHeaderData(5,Qt.Horizontal,'规格型号')
    model.setHeaderData(6,Qt.Horizontal,'价  值')
    model.setHeaderData(7,Qt.Horizontal,'取得日期')
    model.setHeaderData(8,Qt.Horizontal,'存放地点')
    model.setHeaderData(9,Qt.Horizontal,'使用部门')
    model.setHeaderData(10,Qt.Horizontal,'使用人')
    model.setHeaderData(11,Qt.Horizontal,'使用状况')
    model.setHeaderData(12,Qt.Horizontal,'合同编号')
    model.setHeaderData(13, Qt.Horizontal, '最近编辑')
    model.setHeaderData(14,Qt.Horizontal,'备注信息')
    model.setHeaderData(15, Qt.Horizontal, '备注信息')
    # model.setHeaderData(0,Qt.Horizontal,'id')
    # model.setHeaderData(1,Qt.Horizontal,'name')
    # model.setHeaderData(2,Qt.Horizontal,'address')




    #创建视图
def createView(title,model):
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view

def findrow(i):
    delrow = i.row()


    print('del row=%s' % str(delrow))



    # row4= view.currentIndex().row()
    # print(row)
def addrow():
    ret = model.insertRows(model.rowCount(),-1)
    print('insertRow=%s' % str(ret))

def delrow():
    ret = model.removeRow(model.rowCount(),1)
    print('insertRow=%s' % str(ret))

def open_resentDB(Recent_dbname):
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(Recent_dbname)
    if not db.open():
        print('无法建立连接')

def show_table():
    # 1、创建一个变量存放表格
    model = QSqlTableModel()
    delrow = -1
    # 初始化modle
    initialzeModel(model)

    view = createView("展示数据", model)

    # view.setMinimumSize(500,300)
    view.clicked.connect(findrow)
    # 3、显示一个对话框，将表显示到对话框中
    dlg = QDialog()
    layout = QVBoxLayout()
    layout.addWidget(view)
    # 增加两个按钮
    addbtn = QPushButton('添加一行')
    addbtn.setMinimumSize(QtCore.QSize(20, 50))
    addbtn.setStyleSheet("QPushButton {\n"
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
    addbtn.clicked.connect(lambda: model.insertRow(view.currentIndex().row()+1))
    #addbtn.clicked.connect(addrow)
    delbtn = QPushButton('删除一行')
    delbtn.setMinimumSize(QtCore.QSize(20, 50))
    delbtn.setStyleSheet("QPushButton {\n"
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

    delbtn.clicked.connect(lambda: model.removeRow(view.currentIndex().row()))

    cleanbtn = QPushButton('清除条目')
    cleanbtn.setMinimumSize(QtCore.QSize(20, 50))
    cleanbtn.setStyleSheet("QPushButton {\n"
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
    cleanbtn.clicked.connect(lambda: print("点击清空"))

    functionbt = QPushButton('更多操作')
    functionbt.setMinimumSize(QtCore.QSize(20, 50))
    functionbt.setStyleSheet("QPushButton {\n"
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
    functionbt.clicked.connect(lambda: print("选择更多"))



    layout.addWidget(view)
    layout.addWidget(addbtn)
    layout.addWidget(delbtn)
    layout.addWidget(cleanbtn)
    layout.addWidget(functionbt)
    dlg.setLayout(layout)
    # 4、设置窗口大小并显示
    dlg.setWindowTitle("最近编辑条目")
    dlg.resize(800, 400)
    dlg.exec()#不可用open（），不可用show（）天坑
    # sys.exit(app.exec())入坑

def show_recentTABLE(Recent_dbname):
    # model = QSqlTableModel()
    open_resentDB(Recent_dbname)
    show_table()
    # print(model[0,3])

if __name__ == '__main__':
    Recent_dbname = 'yang.db'
    #createDB('2020')
    app = QApplication(sys.argv)
    show_recentTABLE(Recent_dbname)

    #查询总行数
    # SQL = "SELECT id,name,address FROM people"
    # SQL = "SELECT count(*) FROM people"
    # filename = "myDB/2020"
    # conn = sqlite3.connect(filename)
    # cmd = conn.cursor()
    # cmd.execute(SQL)
    # num = 0
    # for user_row in cmd.fetchall():
    #     num=num+1
    #     id = user_row[0]
    #     name = user_row[1]
    #     address = user_row[2]
    #     print(id)
    # print("总行数=",num)
    # print("总行数:%s" % cmd.fetchone())







    # # 1、创建一个变量存放表格
    # model = QSqlTableModel()
    #
    # delrow = -1
    # # 初始化modle
    # initialzeModel(model)
    #
    # view = createView("展示数据", model)
    # view.clicked.connect(findrow)
    #
    # # 3、显示一个对话框，将表显示到对话框中
    # dlg = QDialog()
    # layout = QVBoxLayout()
    # layout.addWidget(view)
    #
    # # 增加两个按钮
    # addbtn = QPushButton('添加一行')
    # addbtn.clicked.connect(addrow)
    #
    # delbtn = QPushButton('删除一行')
    # delbtn.clicked.connect(lambda: model.removeRow(view.currentIndex().row()))
    # layout.addWidget(view)
    # layout.addWidget(addbtn)
    # layout.addWidget(delbtn)
    # dlg.setLayout(layout)
    #
    # # 4、设置窗口大小并显示
    # dlg.setWindowTitle("date Demo")
    # dlg.resize(500, 500)
    # dlg.show()

    sys.exit(app.exec())
