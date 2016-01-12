__author__ = 'lanx'

# Select r items in n
def permutation(n, r):
    answer = []
    select(n, r, answer)
    for idx, a in enumerate(answer):
        print idx+1, a

def select(n, r, answer, picked=[]):
    if len(picked) >= r:
        answer.append(list(picked))
        #print picked
        return False

    for i in range(n):
        if i in picked:
            continue
        picked.append(i)
        flag = select(n, r, answer, picked)
        picked.pop()



def combination(n, r):
    answer = []

permutation(4,3)
combination(3,2)
