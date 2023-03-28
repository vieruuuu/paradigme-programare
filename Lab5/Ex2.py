from PyQt5.QtWidgets import *
from pathlib import Path
import re
import random


def scrie_jurnal():
    a = 2


def load_action():
    print("load")


def save_action():
    print("save")


dirname = str(Path(__file__).parent.absolute())

f = open(dirname + "/citate.txt", "r")

citate = f.read().splitlines()

f.close()

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

jurnal_box = QLineEdit()

jurnal_box.setText("helo")

layout.addWidget(QLabel(random.choice(citate)))
layout.addWidget(jurnal_box)

load_btn = QPushButton("Load")
save_btn = QPushButton("Save")

load_btn.clicked.connect(load_action)
save_btn.clicked.connect(save_action)

layout.addWidget(load_btn)
layout.addWidget(save_btn)


window.setLayout(layout)
window.show()
app.exec()
