from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
import functools

class calculator(QMainWindow):
    def __init__(self, parent=None):
        '''
        sets up calculator object
        '''
        super().__init__(parent)
        self.setGeometry(100, 100, 500, 1000)
        central = QWidget()
        self.lastUsedEquals = False
        self.expression = ''
        self.display = ''
        self.buttons = {}
        self.screen = QLabel()
        self.setCentralWidget(central)
        self.grid = QGridLayout()
        self.grid.setAlignment(Qt.AlignCenter)
        self.setupScreen()
        self.setupButtons()
        central.setLayout(self.grid)
    
    def setupScreen(self):
        '''
        sets structure of calculator 
        '''
        self.screen.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.grid.addWidget(self.screen,0,1,1,3)
        self.screen.setText('')
        self.screen.setAlignment(Qt.AlignRight)
        self.screen.setStyleSheet("background-color: #99ff4b; border: 1px solid black;border-radius: 10px;font-size: 36px;") 
    def setupButtons(self):
        '''
        sets up all buttons and links them to methods
        '''
        for number in range(10) : 
            self.buttons[number] = QPushButton(str(number))
            self.buttons[number].clicked.connect(functools.partial(self.numberPressed,str(number)))
            self.buttons[number].setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding))
            self.buttons[number].setStyleSheet("background-color: #ffffff;font-size: 36px;")

        for button in ['/','C','*','(',')','-','.','+','=']:   
            self.buttons[button] = QPushButton(button)
            self.buttons[button].clicked.connect(functools.partial(self.buttonPressed,button))
            self.buttons[button].setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding))
            self.buttons[button].setStyleSheet("background-color: #acaaa7;font-size: 36px;")

        self.buttons['='].setStyleSheet("background-color: #ffb235;font-size: 36px;")
        self.buttons['C'].setStyleSheet("background-color: #6f6f6f;font-size: 36px;")

        self.grid.addWidget(self.buttons[9],1,0 )
        self.grid.addWidget(self.buttons[8],1,1)
        self.grid.addWidget(self.buttons[7],1,2)
        self.grid.addWidget(self.buttons['/'],1,3)
        self.grid.addWidget(self.buttons['C'],1,4)

        self.grid.addWidget(self.buttons[6],2,0)
        self.grid.addWidget(self.buttons[5],2,1)
        self.grid.addWidget(self.buttons[4],2,2)
        self.grid.addWidget(self.buttons['*'],2,3)
        self.grid.addWidget(self.buttons['('],2,4)

        self.grid.addWidget(self.buttons[3],3,0)
        self.grid.addWidget(self.buttons[2],3,1)
        self.grid.addWidget(self.buttons[1],3,2)
        self.grid.addWidget(self.buttons['-'],3,3)
        self.grid.addWidget(self.buttons[')'],3,4)

        self.grid.addWidget(self.buttons[0],4,0)
        self.grid.addWidget(self.buttons['.'],4,1)
        self.grid.addWidget(self.buttons['+'],4,2)
        self.grid.addWidget(self.buttons['='],4,3,1,2)

        self.displayText()


    def numberPressed(self,btn):
        '''
        adds numbers as pressed
        '''
        if self.lastUsedEquals:
            self.display = ''
        self.display += btn
        self.expression += btn
        self.displayText()


    def buttonPressed(self,btn):
        '''
        deals with calculator opporations
        '''
        self.lastUsedEquals = False
        if btn in ['(',')','.']:
            self.display += btn
            self.expression += btn
        elif btn == 'C':
            self.display = ''
            self.expression = ''
        elif btn == '=':
            if self.expression and self.expression != 'ERROR':
                try:
                    self.display = str(eval(self.expression))
                    self.expression = ''
                    
                except Exception as error:
                    self.display = 'ERROR'
                    print(error)
                self.lastUsedEquals = True
            else:
                self.display = ''
        else:
            if '(' in self.display and not ')' in self.display:
                self.display += btn
            else:
                self.display = ''
            self.expression += btn
        self.displayText()
        if self.lastUsedEquals:
            self.expression = self.display 

    def displayText(self):
        '''
        displays formated calculator text in 
        '''
        self.screen.setText(f'<h2>{self.display}</h2> <br> {self.expression}')

def main():
    app = QApplication(sys.argv)
    window = calculator()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()