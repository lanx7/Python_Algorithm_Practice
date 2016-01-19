
def check_friends(picked, friends):
    idx = 0
    size_pairs = len(picked)/2
    for i in range(size_pairs):
        num1 = picked[i*2]
        num2 = picked[i*2+1]
        #print set([num1,num2])
        if set([num1,num2]) not in friends:
            return False

    return True


def pick(picked, total, friends, num_answer):
    if len(picked) >= total:
        if check_friends(picked, friends) == True:
            print "Found Answer: ", picked
            num_answer[0] = num_answer[0] + 1
        return False

    for i in range(total):
        if i in picked:
            continue
        picked.append(i)
        pick(picked, total,friends,num_answer)
        picked.pop()


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
        answer = []
        num_answer = [0]
        pick(answer, tot, friends, num_answer)
        print num_answer[0]


