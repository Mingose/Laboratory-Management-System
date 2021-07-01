from PyQt5.Qt import *
from resource.login import Ui_Form  # 从UI文件夹下的register文件中导入UI_Form对象


class loginPane(QWidget, Ui_Form):
    show_register_pane_signal = pyqtSignal()
    show_check_login_signal = pyqtSignal(str,str)
    #show_join_qq_group_signal = pyqtSignal

    def __init__(self,parent=None, *args , **kwargs):
        super().__init__(parent, *args , **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowTitle("注册界面")
        self.setupUi(self)

        #QLabel.setMovie()
        movie = QMovie(":/1/images/top_2.gif")
        movie.setScaledSize(QSize(580,300))
        self.login_top_bg_.setMovie(movie)
        movie.start()

    def account_error_animation(self):
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.widget_2)
        animation.setPropertyName(b"pos")
        animation.setKeyValueAt(0, self.widget_2.pos())
        animation.setKeyValueAt(0.3, self.widget_2.pos() + QPoint(-10, 0))
        animation.setKeyValueAt(0.5, self.widget_2.pos())
        animation.setKeyValueAt(0.7, self.widget_2.pos() + QPoint(10, 0))
        animation.setKeyValueAt(1, self.widget_2.pos())
        animation.setDuration(120)
        animation.setLoopCount(3)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def show_register(self):
        print("show register")
        self.show_register_pane_signal.emit()

    def enable_login_btn(self):
        QComboBox
        account = self.account_Box.currentText()
        passwd = self.passwd_line.text()
        #print(account, passwd)
        if len(account) > 0 and len(passwd) > 0:
            self.login_button.setEnabled(True)
        else:
            self.login_button.setEnabled(False)

    def check_login(self):
        print("check login")
        account = self.account_Box.currentText()
        passwd = self.passwd_line.text()
        self.show_check_login_signal.emit(account,passwd)

    def auto_login(self,checked):
        print("auto",checked)
        if checked:
            self.hold_passwd.setChecked(True)

    def rememble_passwd(self,checked):
        print("rememble_passwd",checked)
       # QCheckBox.setChecked()
        if not checked:
            self.auto_log.setChecked(False)

    def join_qq_group(self):
        print("2weima")
        #self.show_join_qq_group_signal.emit()
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = loginPane()
    window.show()
    sys.exit(app.exec_())