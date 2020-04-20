'''

单选按钮控件 (QRadioButton)


'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from PyQt5.QtCore import *

class RadioButtonDemo(QWidget):
    def __init__(self):
        super(RadioButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QRadioButton')
        print("ok")

        layout = QHBoxLayout()
        self.button1 = QRadioButton('单选按钮1')
        self.button1.setChecked(True)           #默认是False，True的话是选择

        self.button1.toggled.connect(self.buttonState)
        layout.addWidget(self.button1)

        self.button2 = QRadioButton('单选按钮2')
        self.button2.toggled.connect(self.buttonState)
        layout.addWidget(self.button2)
        self.setLayout(layout)


    def buttonState(self):
        radioButton = self.sender()
        if radioButton.text() == '单选按钮1':
            if radioButton.isChecked() == True:
                print('<' + radioButton.text() + '> 被选中')
            else:
                print('<' + radioButton.text() + '> 被取消选中状态')


        if radioButton.text() == '单选按钮2':
            if radioButton.isChecked() == True:
                print('<' + radioButton.text() + '> 被选中')
            else:
                print('<' + radioButton.text() + '> 被取消选中状态')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = RadioButtonDemo()
    main.show()
    sys.exit(app.exec_())
