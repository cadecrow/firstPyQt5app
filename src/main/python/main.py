from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *

import sys

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    mainWindow = QMainWindow()
    mainWindow.resize(250, 150)
    label = QLabel('Hey,  you\'re a badass!')
    button = QPushButton('Hell Yeah I am!!!')
    def on_button_clicked():
        alert = QMessageBox()
        alert.setText('SIIIIIKE!!! \n \n \n \n \n \n                                          jk:)')
        alert.exec()
    button.clicked.connect(on_button_clicked)
    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(button)
    window = QWidget()
    window.setLayout(layout)
    mainWindow.setCentralWidget(window)
    mainWindow.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
