import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(700, 700)
        self.setWindowTitle("Main Window")

        self.led_title = QLineEdit(self.windowTitle(), self)
        self.led_title.move(50, 50)
        self.btn_update = QPushButton('Update Title', self)
        self.btn_update.move(150, 100)
        self.btn_update.clicked.connect(self.evt_btn_update_clicked)

    def evt_btn_update_clicked(self):
        self.setWindowTitle(self.led_title.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
