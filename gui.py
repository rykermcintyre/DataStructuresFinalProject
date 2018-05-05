#!/usr/bin/env python3

import sys
from PyQt4.QtGui import *

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Hello World")
window.show()

nameLabel = QLabel("Name:")
nameEdit = QLineEdit()
addressLabel = QLabel("Address:")
addressEdit = QTextEdit()

layout = QGridLayout(window)
layout.addWidget(nameLabel, 0, 0)
layout.addWidget(nameEdit, 0, 1)
layout.addWidget(addressLabel, 1, 0)
layout.addWidget(addressEdit, 1, 1)
layout.setRowStretch(2, 1)

window.resize(480, 160)

window.resize(320, 180)

sys.exit(app.exec_())
