import sys
from PyQt5.QtWidgets import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton("Open file", self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        res = QFileDialog.getOpenFileName(self, 'Open file', '/Users', 'JPG File (*jpg);;PNG File (*.png)')
        print(res)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())