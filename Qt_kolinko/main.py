from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow

from random import randint, choice

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.generate.clicked.connect(self.test)
        self.ui.generate.clicked.connect(self.generate)
        
    def test(self):
        print(1)

    def generate(self):
        signs = ''
        if self.ui.check_letters.isChecked():
            signs += "asdfghjkertyuictwqvbmnxz"
        if self.ui.check_number.isChecked():
            signs += "0123456789"
        
        results = ''
        number = randint(5, 10)
        for i in range(number):
            results += choice(signs)

        self.ui.result.setText(results)
        
style = '''
QWidget {
    background : rgb(169, 203, 235);
}
QLabel {
color : rgb(47, 123, 194);
}
QPushButton {
    background-color: rgb(47, 123, 194);
    color: rgb(169, 203, 235);
    border-radius: 10px;
    font-weight: bold;
    height: 25px;
}
'''

app = QApplication([])
app.setStyleSheet(style)
window = Widget()
window.show()
app.exec_()