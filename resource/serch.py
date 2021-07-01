import sqlite3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
def serch():

    conn = sqlite3.connect(Recent_dbname)
    c = conn.cursor()
    print ("Opened database successfully")
    cursor = c.execute("SELECT *  from mylog")
    for row in cursor:
        if row[1] == "20150013":
            text.append(row[0])
            print("所有搜索到的行",text)
            print(row[0])
            for lie in  row:
                print(lie)

    print ("Operation done successfully")
    conn.close()



def update_change(conn,mylog):



    sql =''' UPDATE mylog
              SET 资产名称 = 'hehe',
               存放地点 = ?
                                        
              WHERE id = ?'''

    c = conn.cursor()
    c.execute(sql,mylog)

    conn.commit()
    print("Total number of rows updated :", conn.total_changes)
    conn.close()
    # cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")




def showserch():
    print("hehe")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Recent_dbname = 'yang.db'
    conn = sqlite3.connect(Recent_dbname)

    text = []
    serch()
    update_change(conn,('109',1))
    # enter()
    #显示到当dialog中
    #修改（地址、备注、最近编辑）
    #插入所在行数

    sys.exit(app.exec)