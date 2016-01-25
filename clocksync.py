__author__ = 'lanx'
import numpy as np

with open('clocksync_input.dat','r') as f:
    line = f.readline()
    num = int(line)

    for i in xrange(1, num+1):
        print "\nCase %d" % i
        line = f.readline().strip()
        tokens = line.split(" ")

        A = np.array(map(lambda x: int(x), tokens))
        print A
        clocks = np.reshape(A, (4, 4))
        print clocks

