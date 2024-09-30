import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(700, 700)

        self.btn = QPushButton("Change label", self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

        self.lbl = QLabel("Label text", self)
        self.lbl.move(60, 100)
        self.lbl.resize(500, 500)
        font = QFont("Times New Roman", 24, 74, True)
        self.lbl.setFont(font)

    def evt_btn_clicked(self):
        str_text = """
        <h1>Fruits</h>
        <ul>
            <li>Apple</li>
            <li>Orange</li>
        </ul>
        """
        self.lbl.setText(str_text)
        pxm = QPixmap("pictures/Ambersweet_oranges.jpg")
        width = pxm.size().width()
        height= pxm.size().height()
        self.resize(width + 100, height + 100)
        self.lbl.resize(width, height)
        self.lbl.setPixmap(pxm)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
    