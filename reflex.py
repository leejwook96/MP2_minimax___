from evaluation import *


def horizontal_4check(board, player, attack_four, defense_four):
    for i in range(0, 7):
        for j in range(0, 3):  # check columns from 0 to 2
            # when current position is player.
            if board[i][j] == player or board[i][j] == ' ':
                count_player = 0
                count_space = 0
                attack_col = 0
                # count the number of opponent player within consecutive 4 locations.
                for k in range(0, 5):
                    if board[i][j + k] == player and board[i][j + k] != ' ':
                        count_player += 1
                    elif board[i][j + k] == ' ':
                        count_space += 1
                        attack_col = j + k
                # if count is 4, which means consecutive 4 locations are all opponents, we have to block it.
                if count_player == 4 and count_space == 1:
                    coord = (i, attack_col)
                    attack_four.add(coord)
                    # Left first based on tie breaker
                    # if j != 0 and board[i][j-1] == ' ':
                    # coord = (i,j-1)
                    # attack_four.add(coord)
                    # Right
                    # elif j != 3 and board[i][j+4] == ' ':
                    # coord = (i,j+4)
                    # attack_four.add(coord)

                    # when current position is opponent player.
    for i in range(0, 7):
        for j in range(0, 4):
            if board[i][j] != player:
                count = 0
                # count the number of opponent player within consecutive 4 locations.
                for k in range(0, 4):
                    if board[i][j + k] != player and board[i][j + k] != ' ':
                        count += 1
                # if count is 4, which means consecutive 4 locations are all opponents, we have to block it.
                if count == 4:
                    # Left first based on tie breaker
                    if j != 0 and board[i][j - 1] == ' ':
                        coord = (i, j - 1)
                        defense_four.add(coord)
                        # possible_four.add([i][j-1])
                    # Right
                    elif j != 3 and board[i][j + 4] == ' ':
                        coord = (i, j + 4)
                        defense_four.add(coord)
                        # possible_four.add([i,j+4])


# three in a row
def horizontal_3check(board, player, defense_three):
    for i in range(0, 7):
        for j in range(1, 4):  # check columns from 0 to 4
            # when current position is opponent player
            if board[i][j] != player:
                count = 0
                # count the number of opponent player within consecutive 3 locations
                for k in range(0, 3):
                    if board[i][j + k] != player and board[i][j + k] != ' ':
                        count += 1
                # if count is 3, which means consecutive 3 locations are all opponents, we have to block it.
                if count == 3:
                    if board[i][j - 1] == ' ' and board[i][j + 3] == ' ':
                        coord = (i, j - 1)
                        defense_three.add(coord)


def vertical_4check(board, player, attack_four, defense_four):
    for i in range(0, 3):  # check rows from 0 to 3
        for j in range(0, 7):
            # when current position is player.
            if board[i][j] == player or board[i][j] == ' ':
                count_player = 0
                count_space = 0
                attack_row = 0
                # count the number of opponent player within consecutive 4 locations.
                for k in range(0, 5):
                    if board[i + k][j] == player and board[i + k][j] != ' ':
                        count_player += 1
                    elif board[i + k][j] == ' ':
                        count_space += 1
                        attack_row = i + k
                # if count is 4, which means consecutive 4 locations are all opponents, we have to block it.
                if count_player == 4 and count_space == 1:
                    coord = (attack_row, j)
                    attack_four.add(coord)
                    # Down first based on tie breaker
                    # if i != 3 and board[i+4][j] == ' ':
                    # coord = (i+4, j)
                    # attack_four.add(coord)
                    # Up
                    # elif i != 0 and board[i-1][j] == ' ':
                    # attack_four.add(coord)
    for i in range(0, 4):  # check rows from 0 to 3
        for j in range(0, 7):
            # when current position is oppnent player.
            if board[i][j] != player:
                count = 0
                # count the number of opponent player within consecutive 4 locations.
                for k in range(0, 4):
                    if board[i + k][j] != player and board[i + k][j] != ' ':
                        count += 1
                # if count is 4, which means consecutive 4 locations are all opponents, we have to block it.
                if count == 4:
                    # Down first based on tie breaker
                    if i != 3 and board[i + 4][j] == ' ':
                        coord = (i + 4, j)
                        defense_four.add(coord)
                    # Up
                    elif i != 0 and board[i - 1][j] == ' ':
                        coord = (i - 1, j)
                        defense_four.add(coord)


def vertical_3check(board, player, defense_three):
    for i in range(1, 4):  # check rows from 0 to 4
        for j in range(0, 7):
            # when current position is opponent player.
            if board[i][j] != player:
                count = 0
                # count the number of opponent player within consecutive 3 locations
                for k in range(0, 3):
                    if board[i + k][j] != player and board[i + k][j] != ' ':
                        count += 1
                # if count is 3, which means consecutive 3 locations are all opponents, we have to block it.
                if count == 3:
                    if board[i - 1][j] == ' ' and board[i + 3][j] == ' ':
                        coord = (i + 3, j)
                        defense_three.add(coord)


def RightDiagon_4check(board, player, attack_four, defense_four):
    for i in range(0, 3):  # check rows from 0 to 3
        for j in range(0, 3):  # check columns from 0 to 3
            # when current position is player.
            if board[i][j] == player or board[i][j] == ' ':
                count_player = 0
                count_space = 0
                attack_row = 0
                attack_col = 0
                # count the number of opponent player within consecutive 4 locations.
                for k in range(0, 5):
                    if board[i + k][j + k] == player and board[i + k][j + k] != ' ':
                        count_player += 1
                    elif board[i + k][j + k] == ' ':
                        count_space += 1
                        attack_row = i + k
                        attack_col = j + k
                # if count is 4, which means consecutive 4 locations are all opponents, we have to block it.
                if count_player == 4 and count_space == 1:
                    coord = (attack_row, attack_col)
                    attack_four.add(coord)
                    # Left and Upper positioin first based on tie breaker
                    # if (i != 0) and (j != 0) and board[i-1][j-1] == ' ':
                    # coord = (i-1, j-1)
                    # attack_four.add(coord)
                    # Right and Down
                    # elif i != 3 and j != 3 and board[i+4][j+4] == ' ':
                    # coord = (i+4, j+4)
                    # attack_four.add(coord)
    for i in range(0, 4):  # check rows from 0 to 3
        for j in range(0, 4):  # check columns from 0 to 3
            # when current position is opponent player.
            if board[i][j] != player:
                count = 0
                # count the number of opponent player within consecutive 4 locations.
                for k in range(0, 4):
                    if board[i + k][j + k] != player and board[i + k][j + k] != ' ':
                        count += 1
                # if count is 4, which means consecutive 4 locations are all opponents, we have to block it.
                if count == 4:
                    # Left and Upper positioin first based on tie breaker
                    if (i != 0) and (j != 0) and board[i - 1][j - 1] == ' ':
                        coord = (i - 1, j - 1)
                        defense_four.add(coord)
                    # Right and Down
                    elif i != 3 and j != 3 and board[i + 4][j + 4] == ' ':
                        coord = (i + 4, j + 4)
                        defense_four.add(coord)


def RightDiagon_3check(board, player, defense_three):
    for i in range(1, 4):  # check rows from 0 to 4
        for j in range(1, 4):  # check columns from 0 to 4
            # when current position is opponent player.
            if board[i][j] != player:
                count = 0
                # count the number of opponent player within consecutive 3 locations.
                for k in range(0, 3):
                    if board[i + k][j + k] != player and board[i + k][j + k] != ' ':
                        count += 1
                # if count is 3, which means consecutive 3 locations are all opponents, we have to block it.
                if count == 3:
                    if board[i - 1][j - 1] == ' ' and board[i + 3][j + 3] == ' ':
                        coord = (i - 1, j - 1)
                        defense_three.add(coord)


def LeftDiagon_4check(board, player, attack_four, defense_four):
    for i in range(0, 3):  # check rows from 0 to 3
        for j in range(4, 7):  # check columns from 3 to 6
            # when current position is player.
            if board[i][j] == player or board[i][j] == ' ':
                count_player = 0
                count_space = 0
                attack_row = 0
                attack_col = 0
                # count the number of opponent player within consecutive 4 locations.
                for k in range(0, 5):
                    if board[i + k][j - k] == player and board[i + k][j - k] != ' ':
                        count_player += 1
                    elif board[i + k][j - k] == ' ':
                        count_space += 1
                        attack_row = i + k
                        attack_col = j - k
                # if count is 3, which means consecutive 4 locations are all opponents, we have to block it.
                if count_player == 4 and count_space == 1:
                    coord = (attack_row, attack_col)
                    attack_four.add(coord)
                    # if j != 3 and i != 3 and board[i+4][j-4] == ' ':
                    # coord = (i+4, j-4)
                    # attack_four.add(coord)
                    # elif i != 0 and j != 6 and board[i-1][j+1] == ' ':
                    # coord = (i-1, j+1)
                    # attack_four.add(coord)
                    # when current position is opponent player.
    for i in range(0, 4):  # check rows from 0 to 3
        for j in range(3, 7):  # check columns from 3 to 6
            if board[i][j] != player:
                count = 0
                # count the number of opponent player within consecutive 4 locations.
                for k in range(0, 4):
                    if board[i + k][j - k] != player and board[i + k][j - k] != ' ':
                        count += 1
                # if count is 3, which means consecutive 4 locations are all opponents, we have to block it.
                if count == 4:
                    if j != 3 and i != 3 and board[i + 4][j - 4] == ' ':
                        coord = (i + 4, j - 4)
                        defense_four.add(coord)
                    elif i != 0 and j != 6 and board[i - 1][j + 1] == ' ':
                        coord = (i - 1, j + 1)
                        defense_four.add(coord)


def LeftDiagon_3check(board, player, defense_three):
    for i in range(1, 4):  # check rows from 0 to 4
        for j in range(3, 6):  # check columns from 2 to 6
            # when current position is opponent player.
            if board[i][j] != player:
                count = 0
                # count the number of opponent player within consecutive 3 locations.
                for k in range(0, 3):
                    if board[i + k][j - k] != player and board[i + k][j - k] != ' ':
                        count += 1
                # if count is 3, which means consecutive 3 locations are all opponents, we have to block it.
                if count == 3:
                    if board[i - 1][j + 1] == ' ' and board[i + 3][j - 3] == ' ':
                        coord = (i + 3, j - 3)
                        defense_three.add(coord)


def winning_block(board, player, winning_blk):
    for i in range(0, 7):
        for j in range(0, 3):
            count_H = 0
            count_V = 0
            flag_H = True
            flag_V = True
            for k in range(0, 5):
                if board[i][j + k] != player and board[i][j + k] != ' ':
                    flag_H = False
                    break
                elif board[i][j + k] == player:
                    count_H += 1
                else:
                    continue

            for k in range(0, 5):
                if board[j + k][i] != player and board[j + k][i] != ' ':
                    flag_V = False
                    break
                elif board[j + k][i] == player:
                    count_V += 1
                else:
                    continue

            if (flag_H):
                coord = (count_H, i, j, 'H')
                winning_blk.add(coord)
            if (flag_V):
                coord = (count_V, j, i, 'V')
                winning_blk.add(coord)
    ## checking Right diagonal
    for i in range(0, 3):
        for j in range(0, 3):
            count_R = 0
            flag_R = True
            for k in range(0, 5):
                if board[i + k][j + k] != player and board[i + k][j + k] != ' ':
                    flag_R = False
                    break
                elif board[i + k][j + k] == player:
                    count_R += 1
                else:
                    continue
            if (flag_R):
                coord = (count_R, i, j, 'R')
                winning_blk.add(coord)
    ## checking Left diagonal
    for i in range(0, 3):
        for j in range(4, 7):
            count_L = 0
            flag_L = True
            for k in range(0, 5):
                if board[i + k][j - k] != player and board[i + k][j - k] != ' ':
                    flag_L = False
                    break
                elif board[i + k][j - k] == player:
                    count_L += 1
                else:
                    continue
            if (flag_L):
                coord = (count_L, i, j, 'L')
                winning_blk.add(coord)


def winning_position(board, winning_blk, player):
    max_list = []
    bottom_list = []
    possible_position = set()
    max_num = winning_blk[0][0]
    for item in winning_blk:
        # if winning_blk[][0] == max_num:
        if item[0] == max_num:
            max_list.append(item)
    for item in max_list:
        if item[3] == 'V':
            count = 0
            for k in range(0, 5):
                if board[item[1] + k][item[2]] == ' ':
                    count += 1
                if k == 0 and board[item[1] + k][item[2]] == ' ' and board[item[1] + k + 1][item[2]] == player:
                    coord = (item[1] + k, item[2])
                    possible_position.add(coord)
                elif k == 4 and board[item[1] + k][item[2]] == ' ' and board[item[1] + k - 1][item[2]] == player:
                    coord = (item[1] + k, item[2])
                    possible_position.add(coord)
                elif 0 < k < 4 and board[item[1] + k][item[2]] == ' ' and (
                        board[item[1] + k + 1][item[2]] == player or board[item[1] + k - 1][item[2]] == player):
                    coord = (item[1] + k, item[2])
                    possible_position.add(coord)
                if count == 5:
                    coord = (item[1] + 4, item[2])
                    possible_position.add(coord)

        elif item[3] == 'H':
            count = 0
            for k in range(0, 5):
                if board[item[1]][item[2] + k] == ' ':
                    count += 1
                if k == 0 and board[item[1]][item[2] + k] == ' ' and board[item[1]][item[2] + k + 1] == player:
                    coord = (item[1], item[2] + k)
                    possible_position.add(coord)
                elif k == 4 and board[item[1]][item[2] + k] == ' ' and board[item[1]][item[2] + k - 1] == player:
                    coord = (item[1], item[2] + k)
                    possible_position.add(coord)
                elif 0 < k < 4 and board[item[1]][item[2] + k] == ' ' and (
                        board[item[1]][item[2] + k + 1] == player or board[item[1]][item[2] + k - 1] == player):
                    coord = (item[1], item[2] + k)
                    possible_position.add(coord)
                if count == 5:
                    coord = (item[1], item[2])
                    possible_position.add(coord)

        elif item[3] == 'R':
            count = 0
            for k in range(0, 5):
                if board[item[1] + k][item[2] + k] == ' ':
                    count += 1
                if k == 0 and board[item[1] + k][item[2] + k] == ' ' and board[item[1] + k + 1][
                                    item[2] + k + 1] == player:
                    coord = (item[1] + k, item[2] + k)
                    possible_position.add(coord)
                elif k == 4 and board[item[1] + k][item[2] + k] == ' ' and board[item[1] + k - 1][
                                    item[2] + k - 1] == player:
                    coord = (item[1] + k, item[2] + k)
                    possible_position.add(coord)
                elif 0 < k < 4 and board[item[1] + k][item[2] + k] == ' ' and (
                        board[item[1] + k + 1][item[2] + k + 1] == player or board[item[1] + k - 1][
                            item[2] + k - 1] == player):
                    coord = (item[1] + k, item[2] + k)
                    possible_position.add(coord)
                if count == 5:
                    coord = (item[1], item[2])
                    possible_position.add(coord)

        elif item[3] == 'L':
            count = 0
            for k in range(0, 5):
                if board[item[1] + k][item[2] - k] == ' ':
                    count += 1
                if k == 0 and board[item[1] + k][item[2] - k] == ' ' and board[item[1] + k + 1][
                                    item[2] - k - 1] == player:
                    coord = (item[1] + k, item[2] - k)
                    possible_position.add(coord)
                elif k == 4 and board[item[1] + k][item[2] - k] == ' ' and board[item[1] + k - 1][
                                    item[2] - k + 1] == player:
                    coord = (item[1] + k, item[2] - k)
                    possible_position.add(coord)
                elif 0 < k < 4 and board[item[1] + k][item[2] - k] == ' ' and (
                        board[item[1] + k - 1][item[2] - k + 1] == player or board[item[1] + k + 1][
                            item[2] - k - 1] == player):
                    coord = (item[1] + k, item[2] - k)
                    possible_position.add(coord)
                if count == 5:
                    coord = (item[1] + 4, item[2] - 4)
                    possible_position.add(coord)
    sorting_position = sorted(possible_position, key=lambda tup: tup[1])
    for item in sorting_position:
        leftmost = sorting_position[0][1]
        if (item[1] == leftmost):
            bottom_list.append(item)
    sorting_position = sorted(bottom_list, reverse=True)
    return sorting_position[0]


def reflex_agent(player, board_H):
    # if player == 'O':
    #     player = 'X'
    # else:
    #     player = 'O'
    globals()
    if player == 'O':
        maker = player1.pop(0)
    print("player is " + player)
    attack_four = set()
    defense_four = set()
    defense_three = set()
    winning_blk = set()
    flag = True
    no_winning_blk = False

    horizontal_4check(board_H, player, attack_four, defense_four)
    vertical_4check(board_H, player, attack_four, defense_four)
    RightDiagon_4check(board_H, player, attack_four, defense_four)
    LeftDiagon_4check(board_H, player, attack_four, defense_four)
    attack_4 = sorted(attack_four)
    defense_4 = sorted(defense_four)

    if (len(attack_4) != 0):
        board_H[attack_4[0][0]][attack_4[0][1]] = player
        flag = False

    if (len(defense_4) != 0 and flag):
        board_H[defense_4[0][0]][defense_4[0][1]] = player
        flag = False

        '''
        print "attack_four list as below"
        print sorted(attack_four)
        print"================="
        print "defense_four list as below"
        print sorted(defense_four)
        print"================="
        '''
    horizontal_3check(board_H, player, defense_three)
    vertical_3check(board_H, player, defense_three)
    RightDiagon_3check(board_H, player, defense_three)
    LeftDiagon_3check(board_H, player, defense_three)
    defense_3 = (sorted(defense_three))
    if (len(defense_3) != 0 and flag):
        board_H[defense_3[0][0]][defense_3[0][1]] = player
        flag = False

        '''
        print "defense_three list as below"
        print sorted(defense_three)
        print"================="
        print "winning_block is as below"
        '''

    if (flag):
        winning_block(board_H, player, winning_blk)
        winning_blk = sorted(winning_blk, reverse=True)

        '''
        print winning_blk
        print"================="
        print "winning position is as below"
        '''
        if len(winning_blk) == 0:
            for j in range(0, 7):
                for i in range(6, -1, -1):
                    if board_H[i][j] == ' ':
                        board_H[i][j] = player
                        no_winning_blk = True
                        break
                if (no_winning_blk):
                    break

        else:
            gomoku = winning_position(board_H, winning_blk, player)
            board_H[gomoku[0]][gomoku[1]] = player
    for i in range(0, 7):
        print()
        print('----------------------')
        for j in range(0, 7):
            print('|' + board_H[i][j], end = " ")
    print()
    print('----------------------')
    end_flag = winning_check(board_H, player)
    print(end_flag)
    return end_flag