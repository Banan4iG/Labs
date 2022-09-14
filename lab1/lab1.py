from enum import Enum
import os


class States(Enum):
    firstLitera = 'firstLitera'
    nextLitera  = 'nextLitera'
    stop    = 'stop'
    error   = 'error'


class Lexer:
    
    def __init__(self):
        self.states = States
        self.token = []
        self.current_state = self.states.firstLitera
        
    def main(self, symbol):
        if self.current_state == self.states.firstLitera:
            if (symbol >= 'a' and symbol <= 'z') or (symbol >= 'A' and symbol <= 'Z'):
                self.current_state = self.states.nextLitera
                self.token.append(symbol)
                return
            else:
                self.current_state = self.states.error
                return

        if self.current_state == self.states.nextLitera:
            if symbol == ' ' or symbol == '\n':
                self.current_state = self.states.firstLitera
                print("".join(self.token))
                self.token = []
                return
            elif (symbol >= 'a' and symbol <= 'z') or (symbol >= 'A' and symbol <= 'Z') or (symbol >= '0' and symbol <= '9'):
                self.token.append(symbol)
                return
            else:
                self.current_state = self.states.error
                return

        if self.current_state == self.states.error:
            if symbol == ' ' and symbol != '\n':
                self.token = []
                print("Error")
                self.current_state = self.states.firstLitera
                return
            else:
                return
       
lex = Lexer()
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'text.txt')) as file:
    for symbol in file.read():
        lex.main(symbol)
    lex.current_state = lex.states.stop

if lex.current_state == lex.states.stop:
    print("Stop")