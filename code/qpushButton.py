import sys

from PySide6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QLineEdit

app = QApplication(sys.argv)

window = QWidget()
window.resize(500, 300)

label01 = QLabel("aashu", window)

button = QPushButton("click me", window)
button.move(0, 20)

# label02 = QLabel("", window)
# label02.move(0,50)
# label02.setStyleSheet("background-color: red;")
# label02.resize(200,30)

input01 = QLineEdit(window)
input01.move(0, 100)

label02 = QLabel("hello", window)
label02.move(0, 50)


def Hello():
    name = input01.text()
    label02.setText(name)


button.clicked.connect(Hello)

window.show()

app.exec()
