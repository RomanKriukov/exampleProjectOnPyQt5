import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(700, 700)
        self.setWindowTitle("Main Window")

        self.lbl = QLabel("Label text", self)
        self.lbl.setStyleSheet('color:red')
        self.lbl.move(50, 20)

        self.btg_color = QButtonGroup()

        self.rbt_red = QRadioButton('Red', self)
        self.rbt_red.move(50, 70)
        self.rbt_red.setStyleSheet('color:red')
        self.rbt_red.setChecked(True)
        self.rbt_red.clicked.connect(self.evt_rbt_clicked)
        self.btg_color.addButton(self.rbt_red, 10)

        self.rbt_green = QRadioButton('Green', self)
        self.rbt_green.move(50, 90)
        self.rbt_green.setStyleSheet('color:green')
        self.rbt_green.clicked.connect(self.evt_rbt_clicked)
        self.btg_color.addButton(self.rbt_green, 15)

        self.rbt_blue = QRadioButton('Blue', self)
        self.rbt_blue.move(50, 110)
        self.rbt_blue.setStyleSheet('color:blue')
        self.rbt_blue.clicked.connect(self.evt_rbt_clicked)
        self.btg_color.addButton(self.rbt_blue, 20)

    def evt_rbt_clicked(self):
        # rbt = self.sender()
        rbt = self.btg_color.checkedButton()
        rbt_id = self.btg_color.checkedId()
        str_color = 'color:' + rbt.text()
        self.lbl.setStyleSheet(str_color)
        print(rbt_id)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
