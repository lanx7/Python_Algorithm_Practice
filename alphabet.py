__author__ = 'lanx'
# GOOD + BAD = SOSO, G, O, D, B, A, S,

alphabet = ['G','O','D','B','A','S']
picked = []
answer = []

def pick(picked, num=1, all=False):
    if(len(picked) == 6):
        G = picked[0]
        O = picked[1]
        D = picked[2]
        B = picked[3]
        A = picked[4]
        S = picked[5]

        if G*1000+O*110+2*D+B*100+A*10-S*1010-O*101 == 0 and G != 0 and B != 0 and S != 0:
            global answer
            answer.append(list(picked))
            #print picked
            return True
        return False

    for i in range(10):
        picked.append(i)
        flag = pick(picked,num+1,all)
        if flag == True and all == True:
            return flag
        picked.pop()

    return False


pick(picked, 1, True)
for idx, a in enumerate(answer):
    print idx+1, a
