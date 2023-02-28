import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

con = sqlite3.connect("coffee.sqlite")
cur = con.cursor()
result = cur.execute("""SELECT * FROM coffee""").fetchall()
data = []
d = {}
for el in result:
    data.append(list(el))
    d[list(el)[1]] = list(el)[2:]

class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.btn_calc.clicked.connect(self.calculate)
        self.names = []
        for i in data:
            self.names.append(i[1])
            self.spisok.addItem(i[1])


    def calculate(self):
        r = d[self.spisok.currentText()]
        self.label_7.setText(str(r[0]))
        if r[1] == 1:
            self.label_8.setText('Молотый')
        else:
            self.label_8.setText('В зёрнах')
        self.label_9.setText(str(r[2]))
        self.label_10.setText(str(r[3]))
        self.label_11.setText(str(r[4]))

    '''self.result_label.setText(format(float(self.area_inp.text()) * float(self.width_inp.text())
                                     * self.data[self.spisok.currentText()], '.3f'))'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
