#!/usr/bin/env python3
from PyQt5 import QtWidgets, uic
import sys

class Window2(QtWidgets.QMainWindow):                          
    def __init__(self):
        super().__init__()
        uic.loadUi('resultat.ui', self)
        self.setFixedSize(400,200)
        
class Window3(QtWidgets.QDialog):                          
    def __init__(self):
        super().__init__()
        uic.loadUi('dialogAbout.ui', self)
        self.setFixedSize(400,200)
        
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('main.ui', self)
        
        # Sæt pointers
        self.button = self.findChild(QtWidgets.QPushButton, 'buttonBeregn')
        self.buttonQuit = self.findChild(QtWidgets.QAction, 'actionAfslut')
        self.buttonAbout = self.findChild(QtWidgets.QAction, 'actionOm_Normperiode')
        
        # Forbind
        self.button.clicked.connect(self.buttonBeregnPressed)
        self.buttonQuit.triggered.connect(self.buttonQuitPressed)
        self.buttonAbout.triggered.connect(self.buttonAboutPressed)
        
        # Åbn hovedvindue
        self.setFixedSize(500,250)
        self.show()

    def buttonBeregnPressed(self):
        self.w = Window2()
        
        # Sæt pointers
        self.labelFaktiskNormperiode = self.w.findChild(QtWidgets.QLabel, 'labelFaktiskNormperiode')
        self.labelNattevagter = self.w.findChild(QtWidgets.QLabel, 'labelNattevagter')
        self.labelWeekender = self.w.findChild(QtWidgets.QLabel, 'labelWeekender')
        self.labelFridoegn = self.w.findChild(QtWidgets.QLabel, 'labelFridoegn')
        self.labelNormtimer = self.w.findChild(QtWidgets.QLabel, 'labelNormtimer')
        self.inputNormperiode = self.findChild(QtWidgets.QLineEdit, 'inputNormperiode')
        self.inputFeriedage = self.findChild(QtWidgets.QLineEdit, 'inputFeriedage')
        
        # Beregn
        faktiskNormperiode = int(self.inputNormperiode.text()) - int(self.inputFeriedage.text()) / 5
        antal_AN = faktiskNormperiode * 7 // 6
        antal_weekend = faktiskNormperiode // 2
        antal_fridage = faktiskNormperiode * 2
        antal_timer = faktiskNormperiode * 37
        
        # Skriv resultat
        self.labelFaktiskNormperiode.setText(str(faktiskNormperiode))
        self.labelNattevagter.setText(str(antal_AN))
        self.labelWeekender.setText(str(antal_weekend))
        self.labelFridoegn.setText(str(antal_fridage))
        self.labelNormtimer.setText(str(antal_timer))
        
        # Åbn vindue
        self.w.show()

    def buttonQuitPressed(self):
        sys.exit()

    def buttonAboutPressed(self):
        self.w2 = Window3()
        self.w2.show()

app = QtWidgets.QApplication(sys.argv)
window = Window()
app.exec_()

