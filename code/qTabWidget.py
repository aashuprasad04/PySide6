import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTabWidget

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 300)

tab = QTabWidget()


home = QWidget()
production = QWidget()


tab.addTab(home, "home")
tab.addTab(production, "production")

layout = QVBoxLayout()
layout.addWidget(tab)
window.setLayout(layout)


label =QLabel("home page", home)
label =QLabel("production page", production)


window.show()


app.exec()
