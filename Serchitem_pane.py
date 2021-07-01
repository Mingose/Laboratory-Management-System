from PyQt5.Qt import *
from resource.Serchitem import Ui_Form  # 从UI文件夹下的register文件中导入UI_Form对象
from PyQt5.QtCore import QDate



class SerchitemPane(QWidget, Ui_Form):
    show_check_addeditem_signal = pyqtSignal(str,str,str)
    show_back_mainfunction_sig = pyqtSignal()
    # show_check_recently_added_sig = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowTitle("123")
        self.setupUi(self)
#按钮信号槽
    def serch_btn_enable(self):
        itemname = self.itemname_cb.currentText()
        itemID = self.itemID_cb.currentText()
        item_loca = self.item_loca_cb.currentText()
        if len(itemname) > 0 or len(itemID) > 0 or len(item_loca) >0 :
            self.serch_bt.setEnabled(True)
        else:
            self.serch_bt.setEnabled(False)

    def serch_check(self):
        print("点击查找")
        itemname = self.itemname_cb.currentText()
        itemID = self.itemID_cb.currentText()
        item_loca = self.item_loca_cb.currentText()
        if len(itemname) ==0:
            itemname=None
        if len(itemID) == 0:
            itemID=None
        if len(item_loca) == 0:
            item_loca=None
        print("id", itemID)
        print("itemname", itemname)
        print("item_loca", item_loca)
        self.show_check_addeditem_signal.emit(itemID,itemname,item_loca)


        # 编辑日志

    def back_mainfunction(self):
        print("返回主菜单")
        self.show_back_mainfunction_sig.emit()

    def recently_serched(self):
        print("显示查询结果")
        self.serch_check()
        # self.show_check_recently_added_sig.emit()

    def mohu_sherch(self):
        print("选中模糊查找")

    def saoyisao(self):
        print("点击扫一扫")
        self.show_check_saoyisao_sig.emit()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = SerchitemPane()
    window.show()
    window.show_check_addeditem_signal.connect(lambda q,w,e:print(q,w,e))
    sys.exit(app.exec_())