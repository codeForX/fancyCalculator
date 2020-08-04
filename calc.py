from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
import functools

class calculator(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(100, 100, 500, 1000)
        central = QWidget()
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
        self.screen.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.grid.addWidget(self.screen,0,1,1,3)
        self.screen.setText('')
        self.screen.setAlignment(Qt.AlignRight)
        self.screen.setStyleSheet("background-color: #99ff4b; border: 1px solid black;border-radius: 10px;font-size: 36px;") 
    def setupButtons(self):
        for number in range(10) : 
            self.buttons[number] = QPushButton(str(number))
            self.buttons[number].clicked.connect(functools.partial(self.numberPressed,str(number)))
            self.buttons[number].setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding))
        for button in ['/','C','*','(',')','-','.','+','=']:   
            self.buttons[button] = QPushButton(button)
            self.buttons[button].clicked.connect(functools.partial(self.buttonPressed,button))
            self.buttons[button].setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding))
        
        

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
        self.display += btn
        self.displayText()
    def buttonPressed(self,btn):
        if btn in ['(',')','.']:
            self.display += btn
        elif btn == 'C':
            self.display = ''
            self.expression = ''
        elif btn == '=':
            if self.expression and self.expression != 'ERROR':
                self.expression += self.display
                try:
                    self.display = str(eval(self.expression))
                    self.expression = ''
                    
                except Exception as error:
                    self.display = 'ERROR'
                    print(error)
                    self.screen.setText(self.display)
            else:
                self.display = ''
                self.screen.clear()
        else:
            if '(' in self.display and not ')' in self.display:
                self.display += btn
            else:
                self.expression = (self.expression + self.display + btn)
                self.display = ''
        self.displayText()
            

    def displayText(self):
        self.screen.setText(f'<h2>{self.display}</h2> <br> {self.expression}')

def main():
    app = QApplication(sys.argv)
    window = calculator()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()