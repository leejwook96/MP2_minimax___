from reflex import *
from evaluation import *
from minimax import *

end = True
board_H = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', 'O', ' ', ' ', ' '],
           [' ', ' ', ' ', 'X', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
#player = 'O'

while(end):
    end = reflex_agent('O', board_H)
    if not end:
        break
    end =  minimax_agent(board_H, 'X')
