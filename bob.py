import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os

class Window(QWidget):

    def __init__(self, parent = None):
    
        QWidget.__init__(self, parent)
        
        button = QPushButton(self.tr("Click me"))
        self.resultLabel = QLabel(self.tr("..."))

        # Create Textbox
        self.username = QLineEdit()
        self.password = QLineEdit()
        #textbox.move(50, 50)
        #textbox.resize(280, 40)
        # New style: uses the connect method of a pyqtSignal object.
        self.connect(button, SIGNAL("clicked()"), self.handleClick)
        
        # Old style: uses the SIGNAL function to describe the signal.
        self.connect(self, SIGNAL("sendValue(PyQt_PyObject)"), self.handleValue)
        
        layout = QVBoxLayout(self)
        layout.addWidget(button)
        layout.addWidget(self.resultLabel)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
    def handleClick(self):
        # Old style: emits the signal using the SIGNAL function.
        user = self.username.text()
        passwd = self.password.text()
        self.emit(SIGNAL("sendValue(PyQt_PyObject)"), {user: passwd})
        
    def handleValue(self, value):
        self.resultLabel.setText("Submitting request...")
        print("./hash | echo {} {}".format(self.username.text(), self.password.text()))

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    window.resize(600, 600)
    sys.exit(app.exec_())
