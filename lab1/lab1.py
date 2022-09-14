from enum import Enum
import os
import codecs

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

    def firstLitera_action(self, symbol):
        if symbol.isalpha():
            self.current_state = self.states.nextLitera
            self.token.append(symbol)
        else:
            self.current_state = self.states.error

    def nextLitera_action(self, symbol):
        if symbol == ' ' or symbol == '\n':
            self.current_state = self.states.firstLitera
            print("".join(self.token))
            self.token = []
        elif symbol.isalpha() or symbol.isdecimal():
            self.token.append(symbol)
        else:
            self.current_state = self.states.error

    def error_action(self, symbol):
        if symbol == ' ' or symbol == '\n':
            self.token = []
            print("Error")
            self.current_state = self.states.firstLitera

    def main(self, symbol):
        match self.current_state:
            case self.states.firstLitera:
                self.firstLitera_action(symbol)

            case self.states.nextLitera:
                self.nextLitera_action(symbol)
            
            case self.states.error:
                self.error_action(symbol)

symbols = []
lex = Lexer()
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'text.txt'), encoding = "utf-8") as file:
    for symbol in file.read():
        lex.main(symbol)

lex.current_state = lex.states.stop
if lex.current_state == lex.states.stop:
    print("Stop")