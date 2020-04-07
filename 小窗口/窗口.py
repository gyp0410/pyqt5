import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


import 小窗口

class my_Ui(小窗口.Ui_MainWindow):
    def __init__(self, MainWindow):
        super().setupUi(MainWindow)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = my_Ui(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
