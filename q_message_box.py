import sys
from PyQt5.QtWidgets import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton("Show Message", self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        res = QMessageBox.question(self, "Disk Full", "Your disk drive is almost full!")
        print(res)
        if res == QMessageBox.Yes:
            QMessageBox.information(self, '', "You've clicked 'Yes' button")
        elif res == QMessageBox.No:
            QMessageBox.information(self, '', "You've clicked 'No' button")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())