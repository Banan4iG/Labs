from enum import Enum
import os


class States(Enum):
    firstLitera = 'firstLitera'
    nextLitera  = 'nextLitera'
    stop    = 'stop'
    error   = 'error'


class Lexer:
    
    def __init__(self, symbols):
        self.token = []
        self.current_state = States.firstLitera
        self.symbols = symbols
        
    def main(self):
        if not symbols:
            self.current_state = States.stop
                  
        else: 
            for symbol in symbols:
                if self.current_state == States.firstLitera:
                    if (symbol >= 'a' and symbol <= 'z') or (symbol >= 'A' and symbol <= 'Z'):
                        self.current_state = States.nextLitera
                        self.token.append(symbol)
                        continue
                    else:
                        self.current_state = States.error
                        continue

                if self.current_state == States.nextLitera:
                    if symbol == ' ' or symbol == '\n':
                        self.current_state = States.firstLitera
                        print("".join(self.token))
                        self.token = []
                        continue
                    elif (symbol >= 'a' and symbol <= 'z') or (symbol >= 'A' and symbol <= 'Z') or (symbol >= '0' and symbol <= '9'):
                        self.token.append(symbol)
                        continue
                    else:
                        self.current_state = States.error
                        continue

                if self.current_state == States.error:
                    if symbol == ' ' and symbol != '\n':
                        self.token = []
                        print("Error")
                        self.current_state = States.firstLitera
                        continue
                    else:
                        continue

            lex.current_state = States.stop
        
        if self.current_state == States.stop:
            print("Stop")           
            
symbols = []
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'text.txt')) as file:
    for symbol in file.read():
        symbols.append(symbol)
lex = Lexer(symbols) 
lex.main()
