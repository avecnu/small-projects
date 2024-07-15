import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import qrcode 

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QR Code Generator")
        button = QtWidgets.QPushButton("Create")

        self.imlabel = QtWidgets.QLabel(self)
        self.imlabel.setScaledContents(True)

        self.label = QtWidgets.QLabel()
        self.input = QtWidgets.QLineEdit()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(button)
        layout.addWidget(self.label)

        button.clicked.connect(self.button_on)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)

        layout_hor = QtWidgets.QHBoxLayout()
        layout_hor.addWidget(widget)
        layout_hor.addWidget(self.imlabel)

        widget_2 = QtWidgets.QWidget()
        widget_2.setLayout(layout_hor)

        self.setCentralWidget(widget_2)
    
    def set_image(self):
        self.pixmap = QtGui.QPixmap("qrcode.png")
        self.imlabel.setPixmap(self.pixmap)
        self.resize(self.pixmap.width(), self.pixmap.height())

    def button_on(self):
        text = self.input.text()
        qr = qrcode.QRCode(version=3, box_size=3, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)
        data = (text)
        qr.add_data(data)
        qr.make(fit=True)
        self.img = qr.make_image(fill_color="black", back_color="white")
        self.img.save("qrcode.png")
        self.label.setText("Done!")
        self.set_image()

app = QtWidgets.QApplication([]) # instance 
window = MainWindow()
window.show()
app.exec() # method to open the window

