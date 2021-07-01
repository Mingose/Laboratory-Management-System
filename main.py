#导入界面

from Login_Pane import loginPane
from register_pane import RegisterPane
from MainFunction_pane import MainFunctionPane
from AddItem_pane import AddItemPane
# from showlmodle_pane import showmodlepane
import ShowRencentmodle_pane
from Serchitem_pane import SerchitemPane
import showlmodle_pane
from PyQt5.QtSql import *
from PyQt5.Qt import *
import sqlite3
import time


#######实在没办法的BUG############################################
# import Recent_table窗口无缝切换
#######实在没办法的BUG#############################################





#创建数据库函数
def createDB(Recent_dbname):
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(Recent_dbname)
    if not db.open():
        print('无法连接数据库')
        return False
    query = QSqlQuery()
    query.exec('create table mylog('
               'ID int primary key ,'
               '资产编号 ,'
               '资产名称 ,'
               '计量单位,'
               '资产品牌 ,'
               '规格型号 ,'
               '价值  ,'
               '取得日期 ,'
               '存放地点,'
               '使用部门 ,'
               '使用人 ,'
               '使用状况 ,'
               '合同编号,'
               '最近编辑 ,'
               '备注信息 )')

    db.close()
    return True

# 注册界面展示函数
def show_register_pane():
    print("展示注册界面")

    # 动画效果
    animation = QPropertyAnimation(register_pane)  # 继承register_pane
    animation.setTargetObject(register_pane)  # 设定操作对象
    animation.setPropertyName(b"pos")  # 设置属性
    animation.setEndValue(register_pane.pos())  # 设置开始与结束值
    animation.setStartValue(QPoint(0, 0))
    animation.setDirection(1000)  # 设置动画完成时间
    animation.setEasingCurve(QEasingCurve.InBounce)  # 弹簧特效
    animation.start(QAbstractAnimation.DeleteWhenStopped)  # 结束时删除动画

#登录界面与注册界面操作
def exit_register_pane():
    print("展示登录界面")
    animation = QPropertyAnimation(register_pane)  # 继承register_pane
    animation.setTargetObject(register_pane)  # 设定操作对象
    animation.setPropertyName(b"pos")  # 设置属性
    animation.setEndValue(register_pane.pos())  # 设置开始与结束值
    animation.setStartValue(QPoint(0, login_pane.width()))
    animation.setDirection(1000)  # 设置动画完成时间
    animation.setEasingCurve(QEasingCurve.OutBounce)  # 弹簧特效
    animation.start(QAbstractAnimation.DeleteWhenStopped)  # 结束时删除动画

#登录验证成功创建数据库（acconunt+Now）
def check_login(account,passwd):
    if (account == "tang" and passwd =="ttttt") or \
            (account == "yang" and passwd =="q") or \
            (account == "wei" and passwd =="wwwww") or \
            (account == "zhou" and passwd =="zzzzz"):
        print("ok")

        mainfunction_pane.show()
        login_pane.hide()
        # 检测连接数据库
        Now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        # 局部变量转全局
        global change_dbname
        global Recent_log
        Recent_log =account + Now
        change_dbname = "./myDB/db/" + account + Now + ".db"
        print("change_dbname=",change_dbname)
        # createDB(Recent_dbname)
        return change_dbname
        # show_recentTABLE(Recent_dbname)

    else:
        login_pane.account_error_animation()



#主界面操作
def check_exit_mainfunction():
    print("按下返回登录")
    #print(A.add(Recent_dbname))
    mainfunction_pane.hide()
    login_pane.show()

def check_add_item():
    print("main add item")
    mainfunction_pane.hide()
    additempane.show()
def check_serch_item():
    print("main serch item")
    mainfunction_pane.hide()
    SerchitemPane.show()
#入库界面操作
#插入行
def check_entry_itemmassage(added_number_sb,added_step_sb,itemID,itemname,item_unit_cb,item_brand_cb,item_model_cb,item_value_cb,item_changedata_cb,item_loca,item_department,item_user_cb,item_condition_cb,item_contractNO_cb,tipEdit_te):



    print("点击录入按钮")

    # 这几句必须要加，否则无法正常插入数据

    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(Recent_dbname)
    if not db.open():
        print('无法连接数据库')
        return False
    query = QSqlQuery()     #不能放在前面，程序会崩溃


    SSQL = "SELECT count(*) FROM mylog"
    conn = sqlite3.connect(Recent_dbname)
    cmd = conn.cursor()
    cmd.execute(SSQL)
    #将元祖中的数据取出
    rowcount = cmd.fetchone()

    row = rowcount[0]

    print('itemIDTYPE:%s'%type(itemID))
    itemID_PL = int(itemID)
    print('itemIDTYPE_PL:%s' % type(itemID_PL))
    added_number_sb = int(added_number_sb)
    print('addnum数据类型：%s' % type(added_number_sb))
    print("added_step_sbTYPE:%s"% type(added_step_sb))
    added_step_sb_PL = int(added_step_sb)
    print("added_step_sbTYPE:%s" % type(added_step_sb_PL))

    for i in range(0,added_number_sb):
        row = row + 1
        if i >= 1:
            itemID_PL = itemID_PL +added_step_sb_PL

        query.exec('insert into mylog values(%d,\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')'% (row,itemID_PL,itemname,item_unit_cb,item_brand_cb,item_model_cb,item_value_cb,item_changedata_cb,item_loca,item_department,item_user_cb,item_condition_cb,item_contractNO_cb,Recent_log,tipEdit_te))



   #不关闭无法正常退出
    db.close()
    return True


#点击返回
def check_backtomain():
    print("返回主界面")
    mainfunction_pane.show()
    additempane.hide()

def serchcheck_backtomain():
    print("返回主界面")
    mainfunction_pane.show()
    SerchitemPane.hide()

def check_recently_added():
    print("显示最近导入")
    time = Recent_log
    ShowRencentmodle_pane.Modleshow(Recent_dbname,Recent_log)

def check_serchitem(ID,name,location):
    print("显示搜索结果")
    print("id", ID)
    print("itemname", name)
    print("item_loca", location)
    if len(ID) == 0:
        ID = None
    if len(name) == 0:
        name = None
    if len(location) == 0:
        location = None
    showlmodle_pane.Modleshow(ID,name,location)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Recent_dbname = ".\myDB\db\yang.db"
#界面定义
    login_pane = loginPane()
    register_pane =RegisterPane()
    mainfunction_pane = MainFunctionPane()
    additempane = AddItemPane()
    # dlg = showmodlepane()  # 显示最近导入面板
    SerchitemPane = SerchitemPane()


    # showresent= show_recentTABLE(Recent_dbname)
# 展示登录界面
    login_pane.show()

    register_pane = RegisterPane(login_pane)  # 注册界面继承父控件登录界面
    register_pane.move(0, register_pane.height())  # 从登录界面的底部开始移动
    register_pane.show()
    # showlmodle_pane.Modleshow(Recent_dbname, None, None, None)


#接收按钮信号
    #注册界面信号
    register_pane.exit_singal.connect(exit_register_pane)
    register_pane.register_accout_passwd_singal.connect(lambda a,b:print(a,b))
    #登录界面信号
    login_pane.show_register_pane_signal.connect(show_register_pane)
    login_pane.show_check_login_signal.connect(check_login)
    #功能主界面信号
    mainfunction_pane.back_login_sig.connect(check_exit_mainfunction)
    mainfunction_pane.add_item_sig.connect(check_add_item)
    mainfunction_pane.check_serch_sig.connect(check_serch_item)
    #录入界面信号
    additempane.show_check_addeditem_signal.connect(check_entry_itemmassage)
    additempane.show_back_mainfunction_sig.connect(check_backtomain)
    additempane.show_check_recently_added_sig.connect(check_recently_added)
    #搜索界面信号
    SerchitemPane.show_check_addeditem_signal.connect(check_serchitem)
    SerchitemPane.show_back_mainfunction_sig.connect(serchcheck_backtomain)
    # SerchitemPane.show_check_recently_added_sig.connect ()


    sys.exit(app.exec_())