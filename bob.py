#!/usr/bin/env python3
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import subprocess
import os

class Window(QWidget):

    def __init__(self, parent = None):
    
        QWidget.__init__(self, parent)
        
        self.backend = "-"
        
        button = QPushButton(self.tr("Login"))
        create = QPushButton(self.tr("Create Account"))
        self.resultLabel = QLabel(self.tr(":D"))
        self.resultLabel2 = QLabel(self.tr(":P"))
        self.t = QLabel(self.tr("Time..."))
        
        # Dropdown
        self.choice = QLabel("Select Backend...", self)
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Select Backend...")
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
        #self.connect(self, SIGNAL("sendValue(PyQt_PyObject)"), self.handleValue)
        
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
        layout.addWidget(self.t, 3, 0, 1, 2)
    
    def closeEvent(self, event):
        subprocess.Popen(["killall", "-9", "continuous"])
        event.accept()
    
    def choose(self, text):
        self.choice.setText(text)
        if self.choice.text() != "Select Backend...":
            if self.choice.text() == "Red-Black Tree":
                self.backend = "rbtree"
            elif self.choice.text() == "Linked List":
                self.backend = "linkedlist"
            elif self.choice.text() == "Separate Chaining":
                self.backend = "sepchain"
            else:
                self.backend = "rbtree"
        QApplication.setStyle(QStyleFactory.create(text))
        self.p = subprocess.Popen("./continuous", stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=25)
        print >> self.p.stdin, self.backend
        with open("./database.txt", "r") as f:
            for line in f:
                line = line.rstrip()
                line = line.split(" ")
                print line
                for i in line:
                    print >> self.p.stdin, i
                self.p.stdin.flush()
                self.p.stdout.readline()
                self.p.stdout.readline()
    
    def handleClick(self):
        if self.backend == "-":
            self.choice.setText("Choose backend!")
            return
        
        # Old style: emits the signal using the SIGNAL function.
        user = self.username.text()
        passwd = self.password.text()
        
        # hash password immediately
        p1 = subprocess.Popen(["echo", "{}".format(passwd)], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["tr", "-d", "\n"], stdin=p1.stdout, stdout=subprocess.PIPE)
        p3 = subprocess.Popen("./hash", stdin=p2.stdout, stdout=subprocess.PIPE)
        passwd = p3.communicate()[0]
        
        print user, passwd
        
        # find user in data structure
        print >> self.p.stdin, "find"
        print >> self.p.stdin, user
        print >> self.p.stdin, passwd
        self.p.stdin.flush()
        
        # Receive signal
        result = self.p.stdout.readline()
        print result
        
        if result == "nouser" or result == "nouser\n":
            self.resultLabel.setText("Invalid username")
        elif result == "success" or result == "success\n":
            self.resultLabel.setText("Logged in! :)")
        elif result == "incorrect" or result == "incorrect\n":
            self.resultLabel.setText("Incorrect password")
        else:
            self.resultLabel.setText("You messed up")
        
        # receive time
        time = self.p.stdout.readline()
        if time != "-":
            time = time.rstrip()
            self.t.setText("Login Time: {} microseconds".format(time))
        
        #self.emit(SIGNAL("sendValue(PyQt_PyObject)"), [user, passwd])
    
    def handleCreate(self):
        if self.backend == "-":
            self.choice.setText("Choose backend!")
            return
        
        # Old style: emits the signal using the SIGNAL function.
        user = self.username2.text()
        passwd = self.password2.text()
        
        # hash password immediately
        p1 = subprocess.Popen(["echo", "{}".format(passwd)], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["tr", "-d", "\n"], stdin=p1.stdout, stdout=subprocess.PIPE)
        p3 = subprocess.Popen("./hash", stdin=p2.stdout, stdout=subprocess.PIPE)
        passwd = p3.communicate()[0]
        
        print user, passwd
        
        # insert into data structure
        print >> self.p.stdin, "insert"
        print >> self.p.stdin, user
        print >> self.p.stdin, passwd
        self.p.stdin.flush()
        
        # receive signal
        result = self.p.stdout.readline()
        if result[0] == "0":
            if result[-2] == "d":
                result = "inserted\n"
            elif result[-2] == "s":
                result = "exists\n"
        print result
        
        if result == "inserted" or result == "inserted\n":
            self.resultLabel2.setText("Account created! :)")
            with open("./database.txt", "a") as f:
                f.write("insert {} {}".format(user, passwd))
        elif result == "exists" or result == "exists\n":
            self.resultLabel2.setText("Username taken, try again")
        else:
            self.resultLabel2.setText("You messed up")
        
        # receive time
        time = self.p.stdout.readline()
        if time != "-":
            time = time.rstrip()
            self.t.setText("Create Account Time: {} microseconds".format(time))
        
        #self.emit(SIGNAL("sendValue(PyQt_PyObject)"), [user, passwd])
        
    #def handleValue(self, value):
        #cmd = "{}".format(self.password.text())
        #print(cmd)
        #self.resultLabel.setText("Submitting request...")
        #self.resultLabel2.setText("Submitting request...")
        #cmd = "./driver {} {} {}".format(self.backend, self.username.text(), self.password.text())
        #cmd = "./continuous"
        #child = os.system(cmd)
        #ps = subprocess.Popen(("echo", cmd), stdout=subprocess.PIPE)
        #output = subprocess.check_output(("./hash"), stdin=ps.stdout)
        #ps.wait()
        #print(output)
        #print("complete")
        

if __name__ == "__main__":
    os.system("./load")
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    window.resize(600, 10)
    sys.exit(app.exec_())
