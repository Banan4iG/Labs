from enum import Enum
from lib2to3.pgen2 import token


class States(Enum):
    firstlitera = 'firstlitera'
    nextlitera  = 'nextlitera'
    stop    = 'stop'
    error   = 'error'


class Lexer:
    
    def __init__(self, symbols):
        self.token = []
        self.current_state = States.firstlitera
        self.symbols = symbols
        
    def main(self):
        if not symbols:
            self.current_state = States.stop
        
        else:
            if self.current_state == States.stop:
                print("Stop")
                exit
            
            for symbol in symbols:
                if self.current_state == States.firstlitera:
                    if symbol >= '0' and symbol <= '9':
                        self.current_state = States.error
                        continue
                    elif symbol == ' ' or symbol == '\n':
                        continue
                    elif (symbol >= 'a' and symbol <= 'z') or (symbol >= 'A' and symbol <= 'Z'):
                        self.current_state = States.nextlitera
                        self.token.append(symbol)
                        continue

                if self.current_state == States.nextlitera:
                    if symbol == ' ' or symbol == '\n':
                        self.current_state = States.firstlitera
                        print("".join(self.token))
                        self.token = []
                        continue
                    else:
                        self.token.append(symbol)
                        continue

                if self.current_state == States.error:
                    if symbol == ' ' and symbol != '\n':
                        self.token = []
                        print("Error")
                        self.current_state = States.firstlitera
                        continue
                    else:
                        continue
                        
            
symbols = []
with open("text.txt") as file:
    for symbol in file.read():
        symbols.append(symbol)

lex = Lexer(symbols) 
lex.main()