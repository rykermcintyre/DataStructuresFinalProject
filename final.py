import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Window(QWidget):

    def __init__(self, parent = None):
    
        QWidget.__init__(self, parent)
        
        login_button = QPushButton(self.tr("Log in"))
        self.resultLabel = QLabel(self.tr("..."))
        
        # New style: uses the connect method of a pyqtSignal object.
        self.connect(login_button, SIGNAL("clicked()"), self.handleLoginClick)
        
        # Old style: uses the SIGNAL function to describe the signal.
        self.connect(self, SIGNAL("sendValue(PyQt_PyObject)"), self.handleValue)
        
        layout = QVBoxLayout(self)
        layout.addWidget(login_button)
        layout.addWidget(self.resultLabel)
    
    def handleLoginClick(self):
    
        # Old style: emits the signal using the SIGNAL function.
        self.emit(SIGNAL("sendValue(PyQt_PyObject)"), "Logged In")
    
    def handleValue(self, value):
    
        self.resultLabel.setText(repr(value))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    window.resize(2000, 2000)
    sys.exit(app.exec_())
