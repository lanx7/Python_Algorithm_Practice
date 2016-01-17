

num = 0

with open('picnic_input.dat','r') as f:
    line = f.readline()
    num = int(line)

    for i in xrange(1, num+1):
        print "Case %d" % i
        line = f.readline().strip()
        tokens = line.split(" ")
        tot = int(tokens[0])
        print "Total: %d" % tot
        numFriends = int(tokens[1])
        print "# of Friends Pair: %d" % numFriends

        line = f.readline().strip()
        tokens2 = line.split(" ")
        friends = []

        for j in xrange(numFriends):
            #print tokens2[j*2], tokens2[j*2+1]
            friends.append(set([int(tokens2[j*2]),int(tokens2[j*2+1])]))

        print friends

def pick(picked):
    if len(picked) > 4: 
        return False
