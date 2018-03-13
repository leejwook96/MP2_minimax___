from copy import deepcopy as dp
from evaluation import *


class Node:
    def __init__(self):
        self.parent = None
        self.child = list()
        self.avail_pos = []
        self.value = 0
        self.board = None
        self.pos = None
        self.total_value = 0

    def __lt__(self, other):
        return self.total_value < other.total_value

    def __gt__(self, other):
        return self.total_value > other.total_value

    def __eq__(self, other):
        return self.total_value == other.total_value

    def __ne__(self, other):
        return not self.__eq__(other)


LEN = 7
AVAIL = ' '
P1 = 'O'
P2 = 'X'
board = []

for i in range(0, LEN):
    board += [[AVAIL] * LEN]


def get_avail_pos(b):
    avail_pos = []
    for i in range(0, LEN):
        for j in range(0, LEN):
            if b[i][j] is AVAIL:
                avail_pos += [(i, j)]

    return avail_pos


class Minimax:
    def __init__(self, board, player, opponent):
        self.root = Node()
        self.root.board = board
        self.root.avail_pos = get_avail_pos(board)
        self.player = player
        self.opponent = opponent

    def evaluation(self, board, player, depth):
        h = horizontal_attack(board, player, depth) + horizontal_defense(board, player)
        v = vertical_attack(board, player, depth) + vertical_defense(board, player)
        r = RightDiagon_attack(board, player, depth) + RightDiagon_defense(board, player)
        l = LeftDiagon_attack(board, player, depth) + LeftDiagon_defense(board, player)
        score = h + v + r + l
        return score

    def expand_to_depth3(self, player, opponent):
        num_node_expand = 0
        # ------------------------ DEPTH 1 --------------------------------
        for i in range(0, len(self.root.avail_pos)):
            child = Node()
            child.parent = self.root
            child.avail_pos = dp(self.root.avail_pos)
            child.pos = child.avail_pos.pop(i)
            child.board = dp(self.root.board)
            child.board[child.pos[0]][child.pos[1]] = player
            self.root.child += [child]
            num_node_expand += 1
            child.value = self.evaluation(child.board, player, 1) - self.evaluation(child.parent.board, player, 0)
            child.total_value = child.value

        # ------------------------ DEPTH 2 --------------------------------
        for c in self.root.child:
            for i in range(0, len(c.avail_pos)):
                child = Node()
                child.parent = c
                child.avail_pos = dp(c.avail_pos)
                child.pos = child.avail_pos.pop(i)
                child.board = dp(c.board)
                child.board[child.pos[0]][child.pos[1]] = opponent
                c.child += [child]
                num_node_expand += 1
                child.value = self.evaluation(child.board, player, 2) - child.parent.value
                child.total_value = child.value + c.value

        # ------------------------ DEPTH 3 --------------------------------
        for c in self.root.child:
            for c1 in c.child:
                for i in range(0, len(c1.avail_pos)):
                    child = Node()
                    child.parent = c1
                    child.avail_pos = dp(c1.avail_pos)
                    child.pos = child.avail_pos.pop(i)
                    child.board = dp(c1.board)
                    child.board[child.pos[0]][child.pos[1]] = player
                    c1.child += [child]
                    num_node_expand += 1

                    child.value = self.evaluation(child.board, player, 3) - child.parent.value
                    child.total_value = child.value + c1.value

                max_val = max(c1.child)
                c1.total_value = max_val.total_value
                if c1.value < max_val.value:
                    c1.pos = max_val.pos

        for c in self.root.child:
            min_val = min(c.child)
            c.total_value = min_val.total_value
            if c.value < min_val.value:
                c.pos = min_val.pos

        return max(self.root.child)


# -----------------------------------------------------------------------------------------------------------------


board_H = [[' ', 'O', 'O', 'O', ' ', ' ', ' '],
           [' ', ' ', 'O', 'X', ' ', ' ', ' '],
           [' ', ' ', 'O', 'O', 'O', ' ', ' '],
           [' ', ' ', 'X', 'X', ' ', 'X ', ' '],
           [' ', 'X', 'X', 'X', ' ', ' ', ' '],
           [' ', 'O', 'O', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ']]


def minimax_agent(board, player):
    print("Minimax turn")
    # if player == 'X':
    #     player = 'O'
    #     opponent = 'X'
    # else:
    #     player = 'X'
    #     opponent = 'O'
    if player is 'X':
        opponent = 'O'
    else:
        opponent = 'X'
    minimax = Minimax(board, player, opponent)
    pos = minimax.expand_to_depth3(player, opponent)
    board[pos.pos[0]][pos.pos[1]] = player

    print("player {} made a move at {} , score {}".format(player, pos.pos, pos.value))

    for i in range(0, 7):
        print()
        print('----------------------')
        for j in range(0, 7):
            print('|' + board[i][j], end = " ")
    print()
    print('----------------------')
    end_flag = winning_check(board, player)
    print("END MINIMAX")
    print(end_flag)
    return end_flag
