#Using Tkinter
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QLineEdit

# Cal_for_GUI
class Cal_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # label num1
        lblnum1 = QLabel('Input 1', self)
        lblnum1.move(15, 10)
        # label num2
        lblnum2 = QLabel('Input 2', self)
        lblnum2.move(15, 50)
        # label result
        lblres = QLabel('Result', self)
        lblres.move(15, 200)
        # TextEdit for input1
        self.input1 = QLineEdit(self)
        self.input1.setFixedWidth(150)
        self.input1.move(100, 10)
        # TextEdit for input2
        self.input2 = QLineEdit(self)
        self.input2.setFixedWidth(150)
        self.input2.move(100, 50)
        # TextEdit for Result
        self.res = QLineEdit(self)
        self.res.setFixedWidth(150)
        self.res.move(100, 200)
        # Button for +
        bplus = QPushButton("+", self)
        bplus.move(30, 100)
        # Button for -
        bminus = QPushButton("-", self)
        bminus.move(150, 100)
        # Button for *
        bmul = QPushButton("*", self)
        bmul.move(30, 150)
        # Button for /
        bdiv = QPushButton("/", self)
        bdiv.move(150, 150)
        # button handler
        bplus.clicked.connect(self.add)
        bminus.clicked.connect(self.minus)
        bmul.clicked.connect(self.mul)
        bdiv.clicked.connect(self.div)
        # statusBar
        self.statusBar().showMessage('Written by Siri')
        self.setGeometry(500, 500, 270, 270)
        self.setWindowTitle('GUI for Calculator')
        self.show()

    # func for add
    def add(self):
        sender = self.sender()
        try:
            val1 = float(self.input1.text())
            val2 = float(self.input2.text())
            tot = val1 + val2
            self.statusBar().showMessage('Written by Udin: button ' + sender.text() + ' was pressed')
            self.res.setText(str(self.makeAsItIs(tot)))
        except ValueError:
            self.res.setText('Invalid Input')

    def square(self):
        sender = self.sender()
        try:
            val1 = float(self.input1.text())
            val2 = float(self.input2.text())
            tot = val1 ** 2 + val2 ** 2
            self.statusBar().showMessage('Written by Udin: button ' + sender.text() + ' was pressed')
            self.res.setText(str(self.makeAsItIs(tot)))
        except ValueError:
            self.res.setText('Invalid Input')

    # function for minus
    def minus(self):
        sender = self.sender()
        try:
            val1 = float(self.input1.text())
            val2 = float(self.input2.text())
            tot = val1 - val2
            self.statusBar().showMessage('Written by Udin: button ' + sender.text() + ' was pressed')
            self.res.setText(str(self.makeAsItIs(tot)))
        except ValueError:
            self.res.setText('Invalid Input')

    # function for multiply
    def mul(self):
        sender = self.sender()
        try:
            val1 = float(self.input1.text())
            val2 = float(self.input2.text())
            tot = val1 * val2
            self.statusBar().showMessage('Written by Udin: button ' + sender.text() + ' was pressed')
            self.res.setText(str(self.makeAsItIs(tot)))
        except ValueError:
            self.res.setText('Invalid Input')

    # function for division
    def div(self):
        sender = self.sender()
        try:
            val1 = float(self.input1.text())
            val2 = float(self.input2.text())
            if (val2 == 0):
                self.res.setText('divide by 0')
            else:
                tot = val1 / val2
                self.statusBar().showMessage('Written by Siri: button ' + sender.text() + ' was pressed')
                self.res.setText(str(self.makeAsItIs(tot)))
        except ValueError:
            self.res.setText('Invalid Input')

    # function make the result as it is
    def makeAsItIs(self, value):
        if (value == int(value)):
            value = int(value)
        return value

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Cal_GUI()
    sys.exit(app.exec_())