import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QStackedWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
)

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 300)

box01 = QWidget()
box01.setStyleSheet("background-color : red;")

box02 = QWidget()
box02.setStyleSheet("background-color : blue;")


layout = QHBoxLayout()
layout.addWidget(box01)
layout.addWidget(box02)

window.setLayout(layout)


layout01 = QVBoxLayout()

button01 = QPushButton("home")
button02 = QPushButton("Dashboard")

layout01.addWidget(button01)
layout01.addWidget(button02)

box01.setLayout(layout01)

stack = QStackedWidget()


# page 01

home = QWidget()
label = QLabel("home", home)

# page02

dashboard = QWidget()
label = QLabel("dashboard", dashboard)

stack.addWidget(home)
stack.addWidget(dashboard)


layout02 = QVBoxLayout()
layout02.addWidget(stack)
box02.setLayout(layout02)


def fun01():
    stack.setCurrentIndex(1)


button02.clicked.connect(fun01)
button01.clicked.connect(lambda: stack.setCurrentIndex(0))


window.show()
app.exec()
