import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit


class MyWidget(QWidget):
    def init(self):
        super().init()
        self.setWindowTitle('hello world')
        self.create_widget()

    def create_widget(self):
        self.layout = QGridLayout()
        self.button = QPushButton('     ')
        self.button.clicked.connect(self.click_button)
        self.layout.addWidget(self.button)
        self.str = QLineEdit
        self.click = 1
        self.buttons = [QPushButton(str(i)) for i in range(1, 10)]
        for button in self.buttons:
            button.clicked.connect(self.click_button)
            self.layout.addWidget(button)
        self.setLayout(self.layout)

    def click_button(self):
        for h in range(len(self.buttons)):
            if self.button:
                pass
                # self.button = QLineEdit


app = QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())
