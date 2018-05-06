import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import subprocess
import os

class Window(QWidget):

    def __init__(self, parent = None):
    
        QWidget.__init__(self, parent)
        
        button = QPushButton(self.tr("Login"))
        create = QPushButton(self.tr("Create Account"))
        self.resultLabel = QLabel(self.tr(":D"))
        self.resultLabel2 = QLabel(self.tr(":P"))
        
        # Dropdown
        self.choice = QLabel("Backend", self)
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Red-Black Tree")
        self.comboBox.addItem("Linked List")
        self.comboBox.addItem("Separate Chaining")
        
        # Create Textbox
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.usernameLabel = QLabel(self.tr("username: "))
        self.passwordLabel = QLabel(self.tr("password: "))
        self.username2 = QLineEdit()
        self.password2 = QLineEdit()
        self.usernameLabel2 = QLabel(self.tr("Create username: "))
        self.passwordLabel2 = QLabel(self.tr("Create password: "))
        
        # New style: uses the connect method of a pyqtSignal object.
        self.connect(button, SIGNAL("clicked()"), self.handleClick)
        self.connect(create, SIGNAL("clicked()"), self.handleCreate)
        self.comboBox.activated[str].connect(self.choose)
        
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
        layout.addWidget(self.choice, 3, 2)
        layout.addWidget(self.comboBox, 3, 3)
    
    def choose(self, text):
        self.choice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))
    
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
        #cmd = "{}".format(self.password.text())
        #print(cmd)
        self.resultLabel.setText("Submitting request...")
        self.resultLabel2.setText("Submitting request...")
        cmd = "./driver rbtree {} {}".format(self.username.text(), self.password.text())
        os.system(cmd)
        #ps = subprocess.Popen(("echo", cmd), stdout=subprocess.PIPE)
        #output = subprocess.check_output(("./hash"), stdin=ps.stdout)
        #ps.wait()
        #print(output)
        print("complete")
        

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    window.resize(600, 10)
    sys.exit(app.exec_())
