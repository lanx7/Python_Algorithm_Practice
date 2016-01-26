__author__ = 'lanx'
import numpy as np

def move(clocks, no, count):
    for i in range(count):
        for s in switch[no]:
            #print s, clocks[s]
            if clocks[s] == 12:
                clocks[s] = 3
            else:
                clocks[s] = clocks[s] + 3
    return

def done(clocks):
    for c in clocks:
        if c != 12:
            return False
    return True


def select(picked, clocks, answer):
    if len(picked) == len(switch):
        #print picked
        c = clocks.copy()
        for i in xrange(len(picked)):
            move(c, i, picked[i])
        if done(c) == True:
            #print picked
            answer.append(list(picked))
            return True
        return False

    for i in xrange(4):
        picked.append(i)
        flag = select(picked, clocks,answer)
        picked.pop()

    return False

depth = 10
switch = [(0,1,2), (3,7,9,11), (4,10,14,15), (0,4,5,6,7), (6,7,8,10,12),
        (0,2,14,15), (3,14,15), (4,5,7,14,15), (1,2,3,4,5), (3,4,5,9,13)]
count = [0] * 16

with open('clocksync_input.dat','r') as f:
    line = f.readline()
    num = int(line)

    for i in xrange(1, num+1):
        print "\nCase %d" % i
        line = f.readline().strip()
        tokens = line.split(" ")

        clocks = np.array(map(lambda x: int(x), tokens))
        print clocks
        #clocks = np.reshape(A, (4, 4))
        #print clocks
        answer = []
        select([], clocks, answer)
        print answer
        min = 0
        for a in answer:
            if sum(a) > min:
                min = sum(a)

        print "Minimum Move is %d" % min
