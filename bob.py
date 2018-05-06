import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import subprocess

class Window(QWidget):

    def __init__(self, parent = None):
    
        QWidget.__init__(self, parent)
        
        button = QPushButton(self.tr("Login"))
        create = QPushButton(self.tr("Create Account"))
        self.resultLabel = QLabel(self.tr("..."))
        self.resultLabel2 = QLabel(self.tr("..."))

        # Create Textbox
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.usernameLabel = QLabel(self.tr("username: "))
        self.passwordLabel = QLabel(self.tr("password: "))
        self.username2 = QLineEdit()
        self.password2 = QLineEdit()
        self.usernameLabel2 = QLabel(self.tr("Create username: "))
        self.passwordLabel2 = QLabel(self.tr("Create password: "))
        #textbox.move(50, 50)
        #textbox.resize(280, 40)
        # New style: uses the connect method of a pyqtSignal object.
        self.connect(button, SIGNAL("clicked()"), self.handleClick)
        self.connect(create, SIGNAL("clicked()"), self.handleCreate)
        
        # Old style: uses the SIGNAL function to describe the signal.
        self.connect(self, SIGNAL("sendValue(PyQt_PyObject)"), self.handleValue)
        
        layout = QGridLayout(self)
        layout.addWidget(button, 2, 0)
        layout.addWidget(create, 2, 2)
        layout.addWidget(self.resultLabel, 2, 1)
        layout.addWidget(self.resultLabel2, 2, 3)
        layout.addWidget(self.username, 1, 0)
        layout.addWidget(self.password, 1, 1)
        layout.addWidget(self.usernameLabel, 0, 0)
        layout.addWidget(self.passwordLabel, 0, 1)
        layout.addWidget(self.username2, 1, 2)
        layout.addWidget(self.password2, 1, 3)
        layout.addWidget(self.usernameLabel2, 0, 2)
        layout.addWidget(self.passwordLabel2, 0, 3)
    def handleClick(self):
        # Old style: emits the signal using the SIGNAL function.
        user = self.username.text()
        passwd = self.password.text()
        self.emit(SIGNAL("sendValue(PyQt_PyObject)"), [user, passwd])
    
    def handleCreate(self):
        # Old style: emits the signal using the SIGNAL function.
        user = self.username.text()
        passwd = self.password.text()
        self.emit(SIGNAL("sendValue(PyQt_PyObject)"), [user, passwd])
        
    def handleValue(self, value):
        cmd = "{}".format(self.password.text())
        print(cmd)
        self.resultLabel.setText("Submitting request...")
        self.resultLabel2.setText("Submitting request...")
        ps = subprocess.Popen(("echo", cmd), stdout=subprocess.PIPE)
        output = subprocess.check_output(("./hash"), stdin=ps.stdout)
        ps.wait()
        print(output)
        print("complete")
        

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    window.resize(600, 10)
    sys.exit(app.exec_())
