player1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
player2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def horizontal_attack(board, player, depth):
    score = 0
    for i in range(0, 7):
        for j in range(0, 3):  # check columns from 0 to 3
            # when current position is player.
            count_player = 0
            count_space = 0
            for k in range(0, 5):
                if board[i][j + k] == player and board[i][j + k] != ' ':
                    count_player += 1
                elif board[i][j + k] == ' ':
                    count_space += 1
            # if count is 4, which means consecutive 4 locations are all opponents, we have to block it.
            if count_player == 5 and depth == 1:  # find winning position at depth 1
                return 9000000000
            elif count_player == 5 and depth == 2:
                return 900000000
            elif count_player == 5 and depth == 3:  # find winning position at depth 3
                return 90000000
            elif count_player == 4 and count_space == 1:
                score += 10000
            elif count_player == 3 and count_space == 2:
                score += 100
            elif count_player == 2 and count_space == 3:
                score += 10
            elif count_player == 1 and count_space == 4:
                score += 1

    for i in range(0, 7):
        for j in range(0, 4):  # check columns from 0 to 3
            count_player = 0
            count_space = 0
            for k in range(0, 4):
                if board[i][j + k] == player and board[i][j + k] != ' ':
                    count_player += 1
                elif board[i][j + k] == ' ':
                    count_space += 1
            # if count is 4, which means consecutive 4 locations are all opponents, we have to block it.
            if count_player == 4 and depth == 1:  # find winning position at depth 1
                score += 100000
            elif count_player == 4 and depth == 2:
                score += 10000
            elif count_player == 4 and depth == 3:  # find winning position at depth 3
                score += 10000
            elif count_player == 3 and count_space == 1:
                score += 1000
    return score


def vertical_attack(board, player, depth):
    score = 0
    for i in range(0, 3):
        for j in range(0, 7):
            count_player = 0
            count_space = 0
            for k in range(0, 5):
                if board[i + k][j] == player and board[i + k][j] != ' ':
                    count_player += 1
                elif board[i + k][j] == ' ':
                    count_space += 1
            if count_player == 5 and depth == 1:  # find winning position at depth 1
                return 9000000000
            elif count_player == 5 and depth == 2:
                return 900000000
            elif count_player == 5 and depth == 3:  # find winning position at depth 3
                return 90000000
            elif count_player == 4 and count_space == 1:
                score += 10000
            elif count_player == 3 and count_space == 2:
                score += 100
            elif count_player == 2 and count_space == 3:
                score += 10
            elif count_player == 1 and count_space == 4:
                score += 1

    for i in range(0, 4):
        for j in range(0, 7):
            count_player = 0
            count_space = 0
            for k in range(0, 4):
                if board[i + k][j] == player and board[i + k][j] != ' ':
                    count_player += 1
                elif board[i + k][j] == ' ':
                    count_space += 1
            # if count is 4, which means consecutive 4 locations are all opponents, we have to block it.
            if count_player == 4 and depth == 1:  # find winning position at depth 1
                score += 100000
            elif count_player == 4 and depth == 2:
                score += 10000
            elif count_player == 4 and depth == 3:  # find winning position at depth 3
                score += 10000
            elif count_player == 3 and count_space == 1:
                score += 1000
    return score


def RightDiagon_attack(board, player, depth):
    score = 0
    for i in range(0, 3):  # check rows from 0 to 3
        for j in range(0, 3):  # check columns from 0 to 3
            # when current position is player.
            count_player = 0
            count_space = 0
            # count the number of opponent player within consecutive 4 locations.
            for k in range(0, 5):
                if board[i + k][j + k] == player and board[i + k][j + k] != ' ':
                    count_player += 1
                elif board[i + k][j + k] == ' ':
                    count_space += 1
            if count_player == 5 and depth == 1:  # find winning position at depth 1
                return 9000000000
            elif count_player == 5 and depth == 2:
                return 900000000
            elif count_player == 5 and depth == 3:  # find winning position at depth 3
                return 90000000
            elif count_player == 4 and count_space == 1:
                score += 10000
            elif count_player == 3 and count_space == 2:
                score += 100
            elif count_player == 2 and count_space == 3:
                score += 10
            elif count_player == 1 and count_space == 4:
                score += 1

                # count the number of opponent player within consecutive 4 locations.
    for i in range(0, 4):  # check rows from 0 to 3
        for j in range(0, 4):  # check columns from 0 to 3
            count_player = 0
            count_space = 0
            for k in range(0, 4):
                if board[i + k][j + k] == player and board[i + k][j + k] != ' ':
                    count_player += 1
                elif board[i + k][j + k] == ' ':
                    count_space += 1
            if count_player == 4 and depth == 1:  # find winning position at depth 1
                score += 100000
            elif count_player == 4 and depth == 2:
                score += 10000
            elif count_player == 4 and depth == 3:  # find winning position at depth 3
                score += 10000
            elif count_player == 3 and count_space == 1:
                score += 1000
    return score


def LeftDiagon_attack(board, player, depth):
    score = 0
    for i in range(0, 3):  # check rows from 0 to 3
        for j in range(4, 7):  # check columns from 3 to 6
            # when current position is player.
            count_player = 0
            count_space = 0
            for k in range(0, 5):
                if board[i + k][j - k] == player and board[i + k][j - k] != ' ':
                    count_player += 1
                elif board[i + k][j - k] == ' ':
                    count_space += 1
            # if count is 3, which means consecutive 4 locations are all opponents, we have to block it.
            if count_player == 5 and depth == 1:  # find winning position at depth 1
                return 9000000000
            elif count_player == 5 and depth == 2:
                return 900000000
            elif count_player == 5 and depth == 3:  # find winning position at depth 3
                return 90000000
            elif count_player == 4 and count_space == 1:
                score += 10000
            elif count_player == 3 and count_space == 2:
                score += 100
            elif count_player == 2 and count_space == 3:
                score += 10
            elif count_player == 1 and count_space == 4:
                score += 1

    for i in range(0, 4):  # check rows from 0 to 3
        for j in range(3, 7):  # check columns from 3 to 6
            count_player = 0
            count_space = 0
            for k in range(0, 4):
                if board[i + k][j - k] == player and board[i + k][j - k] != ' ':
                    count_player += 1
                elif board[i + k][j - k] == ' ':
                    count_space += 1
            if count_player == 4 and depth == 1:  # find winning position at depth 1
                score += 100000
            elif count_player == 4 and depth == 2:
                score += 10000
            elif count_player == 4 and depth == 3:  # find winning position at depth 3
                score += 10000
            elif count_player == 3 and count_space == 1:
                score += 1000
    return score


def horizontal_defense(board, player):
    score = 0
    for i in range(0, 7):
        for j in range(0, 3):  # check columns from 0 to 3
            # when current position is player.
            count_player = 0
            count_opponent = 0
            count_space = 0
            for k in range(0, 5):
                if board[i][j + k] != player and board[i][j + k] != ' ':
                    count_player += 1
                elif board[i][j + k] != ' ':
                    count_opponent += 1
                elif board[i][j + k] == ' ':
                    count_space += 1
            # if count is 4, which means consecutive 4 locations are all opponents, we have to block it.
            if count_player == 4 and count_opponent == 1:
                return 9000000
            elif count_player == 3 and count_space == 1 and count_opponent == 1:
                score += 5000
            elif count_player == 2 and count_space == 2 and count_opponent == 1:
                score += 100
                # elif count_player == 2 and count_space == 3:
                # score += 5
    for i in range(0, 7):
        for j in range(0, 4):  # check columns from 0 to 3
            count_player = 0
            count_opponent = 0
            count_space = 0
            for k in range(0, 4):
                if board[i][j + k] != player and board[i][j + k] != ' ':
                    count_player += 1
                elif board[i][j + k] != ' ':
                    count_opponent += 1
                elif board[i][j + k] == ' ':
                    count_space += 1
            if count_player == 3 and count_opponent == 1:
                score += 10000
            elif count_player == 2 and count_space == 1 and count_opponent == 1:
                score += 100
    return score


def vertical_defense(board, player):
    score = 0
    for i in range(0, 3):
        for j in range(0, 7):
            count_player = 0
            count_space = 0
            count_opponent = 0
            for k in range(0, 5):
                if board[i + k][j] != player and board[i + k][j] != ' ':
                    count_player += 1
                elif board[i + k][j] != ' ':
                    count_opponent += 1
                elif board[i + k][j] == ' ':
                    count_space += 1
            if count_player == 4 and count_opponent == 1:
                return 9000000
            elif count_player == 3 and count_space == 1 and count_opponent == 1:
                score += 5000
            elif count_player == 2 and count_space == 2 and count_opponent == 1:
                score += 100
    for i in range(0, 3):
        for j in range(0, 7):
            count_player = 0
            count_space = 0
            count_opponent = 0
            for k in range(0, 4):
                if board[i + k][j] != player and board[i + k][j] != ' ':
                    count_player += 1
                elif board[i + k][j] != ' ':
                    count_opponent += 1
                elif board[i + k][j] == ' ':
                    count_space += 1
            if count_player == 3 and count_opponent == 1:
                score += 10000
            elif count_player == 2 and count_space == 1 and count_opponent == 1:
                score += 100


    return score


def RightDiagon_defense(board, player):
    score = 0
    for i in range(0, 3):  # check rows from 0 to 3
        for j in range(0, 3):  # check columns from 0 to 3
            # when current position is player.
            count_player = 0
            count_space = 0
            count_opponent = 0
            # count the number of opponent player within consecutive 4 locations.
            for k in range(0, 5):
                if board[i + k][j + k] != player and board[i + k][j + k] != ' ':
                    count_player += 1
                elif board[i + k][j + k] != ' ':
                    count_opponent += 1
                elif board[i + k][j + k] == ' ':
                    count_space += 1
            if count_player == 4 and count_opponent == 1:
                return 9000000
            elif count_player == 3 and count_space == 1 and count_opponent == 1:
                score += 5000
            elif count_player == 2 and count_space == 2 and count_opponent == 1:
                score += 100
    for i in range(0, 4):  # check rows from 0 to 3
        for j in range(0, 4):  # check columns from 0 to 3
            # when current position is player.
            count_player = 0
            count_space = 0
            count_opponent = 0
            # count the number of opponent player within consecutive 4 locations.
            for k in range(0, 4):
                if board[i + k][j + k] != player and board[i + k][j + k] != ' ':
                    count_player += 1
                elif board[i + k][j + k] != ' ':
                    count_opponent += 1
                elif board[i + k][j + k] == ' ':
                    count_space += 1
            if count_player == 3 and count_opponent == 1:
                score += 10000
            elif count_player == 2 and count_space == 1 and count_opponent == 1:
                score += 100
    return score


def LeftDiagon_defense(board, player):
    score = 0
    for i in range(0, 3):  # check rows from 0 to 3
        for j in range(4, 7):  # check columns from 3 to 6
            # when current position is player.
            count_player = 0
            count_opponent = 0
            count_space = 0
            for k in range(0, 5):
                if board[i + k][j - k] != player and board[i + k][j - k] != ' ':
                    count_player += 1
                elif board[i + k][j - k] != ' ':
                    count_opponent += 1
                elif board[i + k][j - k] == ' ':
                    count_space += 1
            if count_player == 4 and count_opponent == 1:
                return 9000000
            elif count_player == 3 and count_space == 1 and count_opponent == 1:
                score += 5000
            elif count_player == 2 and count_space == 2 and count_opponent == 1:
                score += 100
    for i in range(0, 4):  # check rows from 0 to 3
        for j in range(3, 7):  # check columns from 3 to 6
            # when current position is player.
            count_player = 0
            count_opponent = 0
            count_space = 0
            for k in range(0, 4):
                if board[i + k][j - k] != player and board[i + k][j - k] != ' ':
                    count_player += 1
                elif board[i + k][j - k] != ' ':
                    count_opponent += 1
                elif board[i + k][j - k] == ' ':
                    count_space += 1
            if count_player == 3 and count_opponent == 1:
                score += 10000
            elif count_player == 2 and count_space == 1 and count_opponent == 1:
                score += 100

    return score


def winning_check(board, player):
    end_flag = True
    for i in range(0, 7):
        for j in range(0, 3):
            count_H = 0
            count_V = 0
            for k in range(0, 5):
                if board[i][j + k] != player and board[i][j + k] != ' ':
                    break
                elif board[i][j + k] == player:
                    count_H += 1
                else:
                    continue

            if count_H == 5:
                end_flag = False
                print("@@@@@@@@@@@@@@@@@@@@@@@")
                print("@@  Player " + player + " is win. @@")
                print("@@@@@@@@@@@@@@@@@@@@@@@")
                return end_flag

            for k in range(0, 5):
                if board[j + k][i] != player and board[j + k][i] != ' ':
                    break
                elif board[j + k][i] == player:
                    count_V += 1
                else:
                    continue
            if count_V == 5:
                end_flag = False
                print("@@@@@@@@@@@@@@@@@@@@@@@")
                print("@@  Player " + player + " is win. @@")
                print("@@@@@@@@@@@@@@@@@@@@@@@")
                return end_flag

    for i in range(0, 3):
        for j in range(0, 3):
            count_R = 0
            for k in range(0, 5):
                if board[i + k][j + k] != player and board[i + k][j + k] != ' ':
                    break
                elif board[i + k][j + k] == player:
                    count_R += 1
                else:
                    continue
            if count_R == 5:
                end_flag = False
                print("@@@@@@@@@@@@@@@@@@@@@@@")
                print("@@  Player " + player + " is win. @@")
                print("@@@@@@@@@@@@@@@@@@@@@@@")
                return end_flag

    ## checking Left diagonal
    for i in range(0, 3):
        for j in range(4, 7):
            count_L = 0
            for k in range(0, 5):
                if board[i + k][j - k] != player and board[i + k][j - k] != ' ':
                    break
                elif board[i + k][j - k] == player:
                    count_L += 1
                else:
                    continue
            if count_L == 5:
                end_flag = False
                print("@@@@@@@@@@@@@@@@@@@@@@@")
                print("@@  Player " + player + " is win. @@")
                print("@@@@@@@@@@@@@@@@@@@@@@@")
                return end_flag
    for i in range(0, 7):
        for j in range(0, 7):
            if board[i][j] == ' ':
                return end_flag

    end_flag = False
    return end_flag