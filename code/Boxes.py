import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 300)


box01 = QWidget()
box01.resize(50, 30)
box01.setStyleSheet("background-color:red;")


box02 = QWidget()
box02.resize(50, 30)
box02.setStyleSheet("background-color:blue;")


layout01 = QVBoxLayout()
layout01.addWidget(box01)
layout01.addWidget(box02)

window.setLayout(layout01)


label = QLabel("hello", box01)
label = QLabel("World", box02)


window.show()
app.exec()
