# import sys
# from PyQt5.QtWidgets import *
#
# app = QApplication(sys.argv)
# label = QLabel("Hello, PyQt")
# label.show()
#
# print("Before event loop")
# app.exec_()
# print("After event loop")


import sys
from PyQt5.QtWidgets import *

def clicked_slot():
    print('clicked')

app = QApplication(sys.argv)

btn = QPushButton("Hello, PyQt")
btn.clicked.connect(clicked_slot)
btn.show()

app.exec_()