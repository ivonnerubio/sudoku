


def print_board():
    print ('-----------------------\n'
           '|0 2 3 | 1 0 3 | 1 2 0|\n'
           '|4 0 6 | 4 5 0 | 4 0 6|\n'
           '|7 8 9 | 7 0 9 | 0 8 9|\n'
           '-----------------------'
           )


boardar = [
            [0,2,3,1,0,3,1,2,0],
            [4,0,6,4,5,0,4,0,6],
            [7,8,9,7,0,9,0,8,9]
            ]


board = (
        '-----------------------\n'
        '| 0 2 3 | 1 0 3 | 1 2 0|\n'
        '| 4 0 6 | 4 5 0 | 4 0 6|\n'
        '| 7 8 9 | 7 0 9 | 0 8 9|\n'
        '-----------------------'
      )

print (board)


board1 = board[26:31] + board[50:57] + board[59:60]
print(board1)