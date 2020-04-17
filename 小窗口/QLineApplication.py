

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt
import sys

class QLineApplication(QWidget):
    def __init__(self):
        super(QLineApplication, self).__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)

        label1.setText("<font color=black>下面是一个超链接.</font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window,Qt.yellow)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()

        vbox.addWidget(label1)

        self.setLayout(vbox)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineApplication()
    main.show()
    sys.exit(app.exec_())

