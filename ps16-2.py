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


# import sys
# from PyQt5.QtWidgets import *
#
# def clicked_slot():
#     print('clicked')
#
# app = QApplication(sys.argv)
#
# btn = QPushButton("Hello, PyQt")
# btn.clicked.connect(clicked_slot)
# btn.show()
#
# app.exec_()



import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Review")

        btn1 = QPushButton("Click me", self)
        btn1.move(20, 20)
        btn1.clicked.connect(self.btn1_clicked)

    def btn1_clicked(self):
        QMessageBox.about(self, "message", "clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()