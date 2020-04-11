import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow


import 小窗口

class my_Ui(小窗口.Ui_MainWindow):
    def __init__(self, MainWindow):
        super().setupUi(MainWindow)
        self.random_number()
        #self.sort_nunmber()


    def random_number(self):
        number = range(0, 100)
        numbers = random.sample(number,10)
        self.textBrowser.setText(str(numbers))
        print("ok")

    # def sort_number(self):
    #     for i in range(len(numbers) - 1):
    #         for j in range(len(nums) - i - 1):
    #             if nums[j] > nums[j + 1]:
    #                 nums[j], nums[j + 1] = nums[j + 1], nums[j]

    #random_Button


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = my_Ui(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
