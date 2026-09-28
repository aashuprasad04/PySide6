import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QLabel,
    QMenuBar,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
)

app = QApplication(sys.argv)
window = QMainWindow()
window.resize(500, 300)


# menuBar
menu = QMenuBar()

hMenu = menu.addAction("home")
pMenu = menu.addAction("production")
hiMenu = menu.addAction("history")
sMenu = menu.addAction("setting")

window.setMenuBar(menu)


# central
central = QWidget()
# label01 = QLabel("hello", central)

home = QWidget()
label02 = QLabel("home Page", home)

production = QWidget()
label03 = QLabel("Production Page", production)


window.setCentralWidget(central)


stack = QStackedWidget()
stack.addWidget(home)
stack.addWidget(production)

layout = QVBoxLayout()
layout.addWidget(stack)
central.setLayout(layout)

hMenu.triggered.connect(lambda: stack.setCurrentIndex(0))

pMenu.triggered.connect(lambda: stack.setCurrentIndex(1))


window.show()
app.exec()
