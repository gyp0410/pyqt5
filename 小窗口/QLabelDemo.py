import sys
from PyQt5.QtWidgets import QVBoxLayout,QMainWindow,QApplication,QLabel,QWidget
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.resize(350,200)

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)

        label1.setText("<font color=black>这是一个百度标签.</font>")
        label1.setAutoFillBackground(True)      #填满整个背景
        palette = QPalette()                    #创建一个调色板的实例
        palette.setColor(QPalette.Window,Qt.green)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")


        #如果设为True，用浏览器打开网页，如果设为False，调用槽函数
        label3.setOpenExternalLinks(True)
        label3.setText("<a href='http://www.baidu.com'>百度一下你就知道")

        label3.setAlignment(Qt.AlignCenter)

        label3.setToolTip('这是一个超链接')

        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)

        label2.linkHovered.connect(self.linkHovered)
        # 将信号绑定到槽上
        
        label3.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')


    def linkHovered(self):
        print('当鼠标滑过label2标签时，触发事件')

    def linkClicked(self):
        print('当鼠标单击label3标签时，触发事件')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())