import numpy as np


def init_boggle(static=0):
    if static == 0:
        board = [['U','R','L','P','M'],
                 ['X','P','R','E','T'],
                 ['G','I','A','E','T'],
                 ['X','T','N','Z','Y'],
                 ['X','O','Q','R','S']]
        return board
    else:
        board = np.ndarray((5,5))
        return board
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
level = 0
answer = []
answer_xy = []

def print_board(board):
    for line in board:
        print line


def print_answer(answer, answer_xy):
    init_char = '*'
    pboard = []
    str = []
    for i in range(5):
        for j in range(5):
            str.append(init_char)
        pboard.append(str)
        str = []

    for idx, point in enumerate(answer_xy):
        #print idx, point[0], point[1]
        x = point[0]; y = point[1]
        pboard[x][y] = answer[idx]
    print_board(pboard)

def hasword(x, y, word, level=0, all=False):
    global answer
    result = False
    #print b[x][y]
    answer.append(b[x][y])
    answer_xy.append((x,y))

    if(x > 5 or y > 5):
        return False

    if(b[x][y] != word[level]):
        return False

    if "".join(answer) == word:
        print 'Found answer: %s' % answer
        #print 'Co', answer_xy
        print_answer(answer, answer_xy)
        return True

    for i in xrange(8):
        #print answer
        result = hasword(x+dx[i], y+dy[i], word, level+1)
        answer.pop()
        answer_xy.pop()
        if all == True and result == True:
            break


    return result

b = init_boggle()
print_board(b)

print hasword(0,1, 'RRET')
