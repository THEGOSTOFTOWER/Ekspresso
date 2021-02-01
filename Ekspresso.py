import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Экспрессо')
        self.con = sqlite3.connect('coffee.sqlite')
        cur = self.con.cursor()
        self.result = cur.execute("""SELECT * FROM coffee""").fetchall()
        self.table.setRowCount(len(self.result))
        self.table.setColumnCount(len(self.result[0]))
        for i, elem in enumerate(self.result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
