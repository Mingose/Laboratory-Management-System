from PyQt5.Qt import *
from resource.itemadd import Ui_Form  # 从UI文件夹下的register文件中导入UI_Form对象
from PyQt5.QtCore import QDate
# from showlmodle_pane import *


# def check_entry_itemmassage(added_number_sb,added_step_sb,itemID,itemname,item_unit_cb,item_brand_cb,item_model_cb,item_value_cb,item_changedata_cb,item_loca,item_department,item_user_cb,item_condition_cb,item_contractNO_cb,tipEdit_te):
#
#     # #参数接收
#     # added_number = added_number_sb
#     # added_step = added_step_sb
#     # ItemID = itemID
#     # Itemname = itemname
#     # Item_unit = item_unit_cb
#     # Item_brand = item_brand_cb
#     # Item_model = item_model_cb
#     # Item_value = item_value_cb
#     # Item_changedata = item_changedata_cb
#     # Item_loca = item_loca
#     # Item_department = item_department
#     # Item_user = item_user_cb
#     # Item_condition_cb = item_condition_cb
#     # Item_contractNO_cb = item_contractNO_cb
#     # IipEdit_te = tipEdit_te
#     # #转换数据类型itemID
#     # #idstr = str(filter(lambda x: x.isalpha(), itemID))
#     # #idnum = int(filter(str.isdigit,itemID))
#
#     # print("资产编号分割",idnum)
#
#     print("点击录入按钮")
#
#     # 这几句必须要加，否则无法正常插入数据
#
#     db = QSqlDatabase.addDatabase('QSQLITE')
#     db.setDatabaseName(Recent_dbname)
#     if not db.open():
#         print('无法连接数据库')
#         return False
#     query = QSqlQuery()     #不能放在前面，程序会崩溃
#
#
#     SSQL = "SELECT count(*) FROM mylog"
#     conn = sqlite3.connect(Recent_dbname)
#     cmd = conn.cursor()
#     cmd.execute(SSQL)
#     #将元祖中的数据取出
#     rowcount = cmd.fetchone()
#
#     row = rowcount[0]
#     # 判断内容是否为空
#     # 判断是否批量导入
#     # 检索步长
#     # 循环i次导入到rowID行,资产编号=itemID+步长*(i-1)
#     #print("总行数:%s" % cmd.fetchone())
#     # print("row=",row)
#     # print("rowcountTYPE:",type(rowcount))
#     # print("rowTYPE:",type(row))
#     # addrownum = row +1
#     # print("type:",type(itemname))
#     # print(added_number_sb,added_step_sb,itemID,itemname,item_unit_cb,item_brand_cb,item_model_cb,item_value_cb,item_changedata_cb,item_loca,item_department,item_user_cb,item_condition_cb,item_contractNO_cb,tipEdit_te)
#     # print(addrownum,itemID,itemname,item_unit_cb,item_brand_cb,item_model_cb,item_value_cb,item_changedata_cb,item_loca,item_department,item_user_cb,item_condition_cb,item_contractNO_cb,Recent_dbname,tipEdit_te)
#
#
#     # query.exec('insert into mylog values(%d,\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',)'% (addrownum,ItemID,Itemname,Item_unit,Item_brand,Item_model,Item_value,Item_changedata,Item_loca,Item_department,Item_user,Item_condition_cb,Item_contractNO_cb,Recent_dbname,IipEdit_te))
#     #query.exec('insert into mylog values(addrownum,ItemID,Itemname,Item_unit,Item_brand,Item_model,Item_value,Item_changedata,Item_loca,Item_department,Item_user,Item_condition_cb,Item_contractNO_cb,Recent_dbname,IipEdit_te)')
#     #query.exec('insert into mylog values(addrownum,itemID,itemname,item_unit_cb,item_brand_cb,item_model_cb,item_value_cb,item_changedata_cb,item_loca,item_department,item_user_cb,item_condition_cb,item_contractNO_cb,Recent_dbname,tipEdit_te)')
#     #BUG数据类型与空值错误
#     # i = 1
#     # if i < added_number_sb:
#     #     i=i+1
#     #     added_number_sb = added_number_sb - 1
#     #     row = row + 1
#     #     itemID_PL = itemID + added_step_sb * (i - 1)
#     #
#     #     print("added_number_SB = %s,itemID_PL= ", added_number_sb)
#     #     # 传入15个输出15个，|1|added_number_sb--,|2|added_step_sb--,|3|itemID=itemID_PL|4|,rowcount+,|5|RecentChange+
#     # query.exec('insert into mylog values(row,itemID_PL,itemname,item_unit_cb,item_brand_cb,item_model_cb,item_value_cb,item_changedata_cb,item_loca,item_department,item_user_cb,item_condition_cb,item_contractNO_cb,RecentChange,tipEdit_te)')
#     #query.exec('insert into mylog values(3,123,itemname,item_unit_cb,item_brand_cb,item_model_cb,item_value_cb,item_changedata_cb,item_loca,item_department,item_user_cb,item_condition_cb,item_contractNO_cb,RecentChange,tipEdit_te)')
#     #mylist = (addrownum,ItemID,Itemname,Item_unit,Item_brand,Item_model,Item_value,Item_changedata,Item_loca,Item_department,Item_user,Item_condition_cb,Item_contractNO_cb,Recent_dbname,IipEdit_te)
#     #cmd.executemany('INSERT INTO mylog values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,)',mylist)
#     #conn.commit()
#     #query.exec('insert into mylog [(ID,取得日期)] values(9,2019)')
#     # haha = item_model_cb
#     print('itemIDTYPE:%s'%type(itemID))
#     itemID_PL = int(itemID)
#     print('itemIDTYPE_PL:%s' % type(itemID_PL))
#     added_number_sb = int(added_number_sb)
#     print('addnum数据类型：%s' % type(added_number_sb))
#     print("added_step_sbTYPE:%s"% type(added_step_sb))
#     added_step_sb_PL = int(added_step_sb)
#     print("added_step_sbTYPE:%s" % type(added_step_sb_PL))
#
#     for i in range(0,added_number_sb):
#         row = row + 1
#         if i >= 1:
#             itemID_PL = itemID_PL +added_step_sb_PL
#
#         query.exec('insert into mylog values(%d,\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')'% (row,itemID_PL,itemname,item_unit_cb,item_brand_cb,item_model_cb,item_value_cb,item_changedata_cb,item_loca,item_department,item_user_cb,item_condition_cb,item_contractNO_cb,Recent_log,tipEdit_te))
#
#
#
#    #不关闭无法正常退出
#     db.close()
#     return True



class AddItemPane(QWidget, Ui_Form):



    show_check_addeditem_signal = pyqtSignal(str,str,str,str,str,str,str,str,str,str,str,str,str,str,str)

    show_back_mainfunction_sig = pyqtSignal()

    show_check_recently_added_sig = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowTitle("123")
        self.setupUi(self)
#按钮信号槽
    def added_btn_enable(self):
        itemname = self.itemname_cb.currentText()
        itemID = self.itemID_cb.currentText()
        item_loca = self.item_loca_cb.currentText()
        #and added_number_sb > 0
        added_number_sb = self.added_number_sb.value()
        #print(added_number_sb)
        if len(itemname) > 0 and len(itemID) > 0 and len(item_loca) >0 :
            self.daoru_btn.setEnabled(True)
        else:
            self.daoru_btn.setEnabled(False)
#QTextEdit.toPlainText()
#    QSpinBox.valueChanged()
    def added_check(self):
        print("点击录入")
        itemname = self.itemname_cb.currentText()
        itemID = self.itemID_cb.currentText()
        item_loca = self.item_loca_cb.currentText()
        item_brand_cb = self.item_brand_cb.currentText()
        item_model_cb = self.item_model_cb.currentText()
        item_value_cb = self.item_value_cb.currentText()
        item_changedata_cb = self.item_changedata_cb.currentText()
        item_department = self.item_department.currentText()
        item_user_cb = self.item_user_cb.currentText()
        item_condition_cb = self.item_condition_cb.currentText()
        item_contractNO_cb = self.item_contractNO_cb.currentText()
        item_unit_cb = self.item_unit_cb.currentText()
        tipEdit_te = self.tipEdit_te.toPlainText()

        added_number_sb = str(self.added_number_sb.value())
        added_step_sb = str(self.added_step_sb.value())
        # QSpinBox.textFromValue()
        # QComboBox.text
        # self.show_check_addeditem_signal.emit(itemname, itemID,item_loca,item_brand_cb,item_model_cb,item_value_cb,
        #                                       item_changedata_cb,item_department,item_user_cb,item_condition_cb,
        #                                       item_contractNO_cb,item_unit_cb,tipEdit_te)
        self.show_check_addeditem_signal.emit(added_number_sb,added_step_sb,itemID,itemname,item_unit_cb,item_brand_cb,item_model_cb,item_value_cb,item_changedata_cb,item_loca,item_department,item_user_cb,item_condition_cb,item_contractNO_cb,tipEdit_te)

        # 编辑日志

    def back_mainfunction(self):
        print("返回主菜单")
        self.show_back_mainfunction_sig.emit()

    def recently_added(self):
        print("显示最近导入")
        # itemID = self.itemID_cb.currentText()
        # itemname = self.itemname_cb.currentText()
        self.show_check_recently_added_sig.emit()
        #显示最近导入界面（showmodlw_pane）,并且传入乱码不显示已经有的，不再新建数据库




if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    Recent_dbname = 'yang.db'  # 加载指定数据库
    window = AddItemPane()
    window.show()
    window.show_check_addeditem_signal.connect(lambda q,w,e,r,t,y,u,i,o,p,a,s,d,f,g :print(q,w,e,r,t,y,u,i,o,p,a,s,d,f,g))

    # window.show_check_addeditem_signal.connect(check_entry_itemmassage)
    # window.show_back_mainfunction_sig.connect(check_backtomain)
    # window.show_check_recently_added_sig.connect(check_recently_added)


    # # Recent_dbname = 'yang.db'  # 加载指定数据库
    # # window_showmodle = showmodlepane()  # 在界面中显示
    # getdate(None, None, None)
    # window_showmodle.move_bt.setEnabled(True)
    # window_showmodle.show()

    sys.exit(app.exec_())