import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow


import 小窗口

class my_Ui(小窗口.Ui_MainWindow):
    def __init__(self, MainWindow):
        super().setupUi(MainWindow)
        self.initUI()


    def initUI(self):
        self.random_Button.clicked.connect(self.random_number)
        self.sort_Button.clicked.connect(self.sort_number)



    def random_number(self):
        self.number = range(0, 100)                      #数值范围0-100
        self.numbers = random.sample(self.number,10)
        self.textBrowser.setText(str(self.numbers))
        print("ok")
        print(self.number)


    def sort_number(self):
        for i in range(len(self.number) - 1):
            for j in range(len(self.numbers) - i - 1):
                if self.numbers[j] > self.numbers[j + 1]:
                    self.numbers[j], self.numbers[j + 1] = self.numbers[j + 1], self.numbers[j]
        self.textBrowser_2.setText(str(self.numbers))
        print('OK')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = my_Ui(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
