from PyQt5.Qt import *
from modle import Ui_Dialog
from PyQt5 import QtCore,QtGui

def initmodle(model,ID,name,location):
    # 设置表头
    model.setTable('mylog')

    # model.setFilter(QObject::tr(“ID = ‘ % 1′”).arg(name)); // 根据姓名进行筛选


    # 设置编辑策略（当表变化时）
    model.setEditStrategy(QSqlTableModel.OnFieldChange)
    # ID = 'TY2016000618'
    # name ='电力自动化和继电保护及供配电技术实训装置'
    # location = '西实-101'
    # if name != '0':
    #     model.setFilter(("资产名称 = '%s'") % (name) )
    # if ID != '0':
    #     model.setFilter(("资产编号 = '%s'") % (ID) )
    # if location != '0':
    #     model.setFilter(("存放地点 = '%s'") % (location) )

    if ID == None:
        if  name != None and location !=None:
            model.setFilter(("存放地点 = '%s' and 资产名称 = '%s'") % (location,name))
        if name ==None and location !=None:
            model.setFilter(("存放地点 = '%s'") % (location))
        if name !=None and location ==None:
            model.setFilter(("资产名称 = '%s'") % (name))
        else:
            pass
    if ID !=None:
        model.setFilter(("资产编号 = '%s'") % (ID))




    # model.setFilter(("存放地点 = '%s' and 资产编号 = '%s' and 资产名称 = '%s'") % (location,ID,name) )
    # model.setFilter(("存放地点 = '%s' and 资产编号 = '%s' and 资产名称 = '%s'") % (location,ID,name) )

    # model.setFilter(("SHORTDESC = '%s' and CATEGORY = '%d'" % (date_id, room_id)))


# 装在数据
    model.select()
    # 设置字段头
    model.setHeaderData(0, Qt.Horizontal, 'ID')
    model.setHeaderData(1, Qt.Horizontal, '资产编号')
    model.setHeaderData(2, Qt.Horizontal, '资产名称')
    model.setHeaderData(3, Qt.Horizontal, '计量单位')
    model.setHeaderData(4, Qt.Horizontal, '品  牌')
    model.setHeaderData(5, Qt.Horizontal, '规格型号')
    model.setHeaderData(6, Qt.Horizontal, '价  值')
    model.setHeaderData(7, Qt.Horizontal, '取得日期')
    model.setHeaderData(8, Qt.Horizontal, '存放地点')
    model.setHeaderData(9, Qt.Horizontal, '使用部门')
    model.setHeaderData(10, Qt.Horizontal, '使用人')
    model.setHeaderData(11, Qt.Horizontal, '使用状况')
    model.setHeaderData(12, Qt.Horizontal, '合同编号')
    model.setHeaderData(13, Qt.Horizontal, '最近编辑')
    model.setHeaderData(14, Qt.Horizontal, '备注信息')
    model.setHeaderData(15, Qt.Horizontal, '备注信息')
    # model.setHeaderData(0,Qt.Horizontal,'id')
    # model.setHeaderData(1,Qt.Horizontal,'name')
    # model.setHeaderData(2,Qt.Horizontal,'address')



######继承modle显示界面控件类型
class showmodle(QDialog,Ui_Dialog):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowTitle("123")
        self.setupUi(self)
        query = QSqlQuery()
        query.exec_("select * from mylog")
        if query.next():
            print("query.value(1).toString()")

    '''
    各种槽函数，在不同功能调用时，使能不同的控件按钮
    '''

    def check_clean(self):
        print("clean")

    def check_addline(self):
        pass

    def check_delline(self):
        pass

    def check_borrow(self):
        pass

    def check_move(self):
        pass

    def check_scrapped(self):
        pass

    def check_repair(self):
        pass

    def check_maintain(self):
        pass

    def cheack_upload(self):
        pass

#打开指定数据库
def open_resentDB(Recent_dbname):
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(Recent_dbname)
    if not db.open():
        print('无法建立连接')
#可视化操作
def findrow(i):
    delrow = i.row()


    print('del row=%s' % str(delrow))

#让modle显示界面的tableview加载数据
def createView(title,model):
    view = window.mytableview
    view.setStyleSheet("background-color: rgb(255, 170, 255);")
    view.setModel(model)
    print("model")
    view.setWindowTitle(title)
    return view
#搜索总表中所有数据，可指定搜索ID，姓名，存放地点
def getdate(ID,name,location):
    open_resentDB(Recent_dbname)
    modle = QSqlTableModel()
    initmodle(modle,ID,name,location)
    view = createView("展示数据", modle)
    view.clicked.connect(findrow)
    window.mytableview.setModel(modle)
    # print(viem.__bass__)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    Recent_dbname = 'yang.db'  #加载指定数据库


    window = showmodle()   #在界面中显示
    getdate(None,None,None)
    # window.mytableview.setStyleSheet("background-color: rgb(0, 170, 0);")
    # window.mytableview.setModel(model)
    window.move_bt.setEnabled(True)
    window.show()
    # window.showdate()
    sys.exit(app.exec_())