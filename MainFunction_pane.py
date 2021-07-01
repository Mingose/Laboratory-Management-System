from PyQt5.Qt import *
from resource.MainFunction import Ui_Form  # 从UI文件夹下的register文件中导入UI_Form对象


class MainFunctionPane(QWidget, Ui_Form):

    back_login_sig = pyqtSignal()
    show_datalog_sig = pyqtSignal()
    remove_item_sig = pyqtSignal()
    move_item_sig = pyqtSignal()
    borrow_item_sig = pyqtSignal()
    add_item_sig = pyqtSignal()
    output_excel_sig = pyqtSignal()
    check_serch_sig = pyqtSignal()



    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowTitle("88")
        self.setupUi(self)


    def show_datalog(self):
        print("日志")
        self.show_datalog_sig.emit()


    def show_login(self):
        print("退出到登录界面")
        self.back_login_sig.emit()

    def remove_item(self):
        print("按下报废按钮")
        self.remove_item_sig.emit()


    def move_item(self):
        print("移动资产")
        self.move_item_sig.emit()

    def borrow_item(self):
        print("资产外借")
        self.borrow_item_sig.emit()

    def add_item(self):
        print("资产入库")
        self.add_item_sig.emit()

    def output_excel(self):
        print("输出表格")
        self.output_excel_sig.emit()

    def check_serch(self):
        print("点击搜索")
        self.check_serch_sig.emit()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MainFunctionPane()
    #window.show_data_signal.connect(lambda: print("退出"))
    #window.show_join_qq_group_signal.connect(lambda :print("11"))
    window.show()
    sys.exit(app.exec_())