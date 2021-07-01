from PyQt5.Qt import *
from resource.register import Ui_Form    #从UI文件夹下的register文件中导入UI_Form对象

class RegisterPane(QWidget,Ui_Form):

    exit_singal = pyqtSignal()
    register_accout_passwd_singal = pyqtSignal(str,str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setWindowTitle("注册界面")
        self.setupUi(self)

        self.animation_targetes = [self.exit_Button_4,self.about_Button_2,self.reset_Button_3]
        #self.animation_targetes_pos = [self.exit_Button_4,self.reset_Button_3,self.about_Button_2]
        self.animation_targetes_pos = [target.pos() for target in self.animation_targetes]


    def show_hide_menu(self,checked):
        print("show_hide_menu",checked)
            # 创建序列动画组
        animation_group = QSequentialAnimationGroup(self)
        for idx, target in enumerate(self.animation_targetes):
            # 创建三个属性动画
            animation = QPropertyAnimation()
            animation.setTargetObject(target)
            animation.setPropertyName(b"pos")
            if not checked:
                animation.setStartValue(self.menu_Button.pos())
                animation.setEndValue(self.animation_targetes_pos[idx])
            else:
                animation.setEndValue(self.menu_Button.pos())
                animation.setStartValue(self.animation_targetes_pos[idx])
            animation.setDuration(200)
            animation.setEasingCurve(QEasingCurve.OutBounce)
            #animation_group.setEasingCurve(QEasingCurve.InOutBounce)
            animation_group.addAnimation(animation)
        animation_group.start(QAbstractAnimation.DeleteWhenStopped)




    def reset(self):
        print("reset")
        self.id_line.clear()
        self.passwd_line.clear()
        self.confirm_line_6.clear()

    def exit_pane(self):
        #print("exit_pane")
        self.exit_singal.emit()

    def about(self):
        print("about")
        QMessageBox.about(self,"关于","版权所有，盗版必究")

    def register(self):
        #print("register")
        ID_Text = self.id_line.text()
        passwd_Text = self.passwd_line.text()
        self.register_accout_passwd_singal.emit(ID_Text,passwd_Text)

    def enable_text_button(self):
        print("判定")
        ID_Text = self.id_line.text()
        passwd_Text = self.passwd_line.text()
        confitm_Text = self.confirm_line_6.text()
        if len(ID_Text) > 0 and len(passwd_Text) > 0 and len(confitm_Text) > 0 and passwd_Text == confitm_Text:
            self.register_Button_5.setEnabled(True)
        else:
            self.register_Button_5.setEnabled(False)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = RegisterPane()

    window.exit_singal.connect(lambda :print("退出"))
    window.register_accout_passwd_singal.connect(lambda a,b:print(a,b))

    window.show()
    sys.exit(app.exec_())