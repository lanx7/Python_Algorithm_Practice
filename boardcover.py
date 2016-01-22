import numpy as np
# -*- coding: utf-8 -*-

num = 0
block_dx = [(1,0), (1,1), (0,-1), (0,1)]
block_dy = [(0,1), (0,1), (1,1), (1,1)]

height = 0
width = 0
count = 0

def is_complete(board):
    for line in board:
        for k in line:
            #print k
            if k == True:
               return False
    return True

def check(board):
    for (x,y), value in np.ndenumerate(board):
#        print x,y, value
        if value == True:
            return x,y
    return x,y

def put_block(board):
    #print board
    global height, width, count
    h,w = check(board)
    #print h, w

    #
    #print "XX", height, width, count, x, y
    if is_complete(board) == True:
        count = count + 1
    #    print count
        return False

    if w == width-1 and h == height-1:
        return False

    # Try 4 types of blocks
    for i in xrange(len(block_dx)):
        dx1 = block_dx[i][0]; dy1 = block_dy[i][0] # block coordinate1
        dx2 = block_dx[i][1]; dy2 = block_dy[i][1] # block coordinate2
        if w + dx1 > width-1 or w + dx2 > width-1: # out of board
            continue
        if h + dy1 > height-1 or h + dy2 > height-1:
            continue

        ## 꼽고 이동
        if board[h,w] == True and board[h+dy1,w+dx1] == True and board[h+dy2,w+dx2] == True:
            board[h,w] = False; board[h+dy1,w+dx1] = False; board[h+dy2,w+dx2] = False
            put_block(board)
            board[h,w] = True; board[h+dy1,w+dx1] = True; board[h+dy2,w+dx2] = True


with open('boardcover_input.dat','r') as f:
    line = f.readline()
    num = int(line)

    for i in xrange(1, num+1):
        print "\nCase %d" % i
        line = f.readline().strip()
        tokens = line.split(" ")
        height = int(tokens[0])
        width = int(tokens[1])
        print "Height = %d, Width = %d" % (height, width)

        board = np.zeros(shape=(height,width),dtype=bool)
        for j in xrange(height):
            line = f.readline().strip()
            for k in xrange(len(line)):
                if line[k] == '#':
                    board[j,k] = False
                else:
                    board[j,k] = True

        print board
        print type(board)
        print is_complete(board)

        #check(board)
        put_block(board)
        print count


"""
    더이상 블럭을 꼽을 수 없음  True이고 dx dy도 True
    if (블럭이 꽉 참 ) --> 정답
    else 그냥 답이 아님


    picked + new bock #하나의 블럭을 꼽음
    put_block(picked)
"""