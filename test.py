# import sys
# from PyQt5.QtWidgets import *
#
# app = QApplication(sys.argv)
# dlgMain = QDialog()
# dlgMain.setWindowTitle("First GUI")
# dlgMain.show()
#
# app.exec_()


import sys
from PyQt5.QtWidgets import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second GUI")
        self.resize(300, 200)

        self.ledText = QLineEdit("Default text", self)
        self.ledText.move(90, 50)

        self.btnUpdate = QPushButton("Update Window Title", self)
        self.btnUpdate.move(70, 80)
        self.btnUpdate.clicked.connect(self.evt_btn_update_clicked)

    def evt_btn_update_clicked(self):
        self.setWindowTitle(self.ledText.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
