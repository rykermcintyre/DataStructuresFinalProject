import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import subprocess


class Window(QWidget):

    def __init__(self, parent = None):
    
        QWidget.__init__(self, parent)
        
        button = QPushButton(self.tr("Click me"))
        self.resultLabel = QLabel(self.tr("..."))

        # Create Textbox
        self.username = QLineEdit()
        self.password = QLineEdit()
        #self.usernameLabel = QLabel(self.tr("username: "))
        #self.passwordLabel = QLabel(self.tr("password: "))
        #textbox.move(50, 50)
        #textbox.resize(280, 40)
        # New style: uses the connect method of a pyqtSignal object.
        self.connect(button, SIGNAL("clicked()"), self.handleClick)
        
        # Old style: uses the SIGNAL function to describe the signal.
        self.connect(self, SIGNAL("sendValue(PyQt_PyObject)"), self.handleValue)
        
        layout = QGridLayout(self)
        layout.addWidget(button, 0, 0)
        layout.addWidget(self.resultLabel, 0, 1)
        layout.addWidget(self.username, 1, 0)
        layout.addWidget(self.password, 1, 1)
        #layout.addWidget(self.usernameLabel, 1, 0)
        #layout.addWidget(self.passwordLabel, 1, 1)
    def handleClick(self):
        # Old style: emits the signal using the SIGNAL function.
        user = self.username.text()
        passwd = self.password.text()
        self.emit(SIGNAL("sendValue(PyQt_PyObject)"), {user: passwd})
        
    def handleValue(self, value):
        cmd = "{}".format(self.password.text())
        self.resultLabel.setText("Submitting request...")
        ps = subprocess.Popen(("echo", cmd), stdout=subprocess.PIPE)
        output = subprocess.check_output(("./hash"), stdin=ps.stdout)
        ps.wait()
        print(output)
        print("complete")
        #print(output)
        #os.system("echo {} {}".format(self.username.text(), self.password.text()))

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    window.resize(600, 600)
    sys.exit(app.exec_())
