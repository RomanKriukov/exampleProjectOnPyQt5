import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(700, 700)

        self.icon_pxm_on = QIcon(QPixmap("pictures/switch_on.png"))
        self.icon_pxm_off = QIcon(QPixmap("pictures/switch_off.png"))

        self.btn = QPushButton("Label is enabled", self)
        self.btn.move(35, 50)
        self.btn.setIcon(self.icon_pxm_on)
        self.btn.setFlat(True)
        self.btn.clicked.connect(self.evt_btn_clicked)

        self.lbl = QLabel("Label text", self)
        self.lbl.move(60, 100)
        self.lbl.resize(500, 500)
        font = QFont("Times New Roman", 24, 74, True)
        self.lbl.setFont(font)

    def evt_btn_clicked(self):
        if self.lbl.isEnabled():
            self.lbl.setDisabled(True)
            self.lbl.setText("Enable label")
            self.btn.setText("Label is disabled")
            self.btn.setIcon(self.icon_pxm_off)
        else:
            self.lbl.setEnabled(True)
            self.lbl.setText("Disable label")
            self.btn.setText("Label is enabled")
            self.btn.setIcon(self.icon_pxm_on)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
    