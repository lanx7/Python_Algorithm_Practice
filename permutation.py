__author__ = 'lanx'

# Select r items in n
def permutation(n, r, answer, picked=[]):
    if len(picked) >= r:
        answer.append(list(picked)) # Need to deep-copy the list
        #print picked
        return False

    for i in range(n):
        if i in picked:
            continue
        picked.append(i)
        flag = permutation(n, r, answer, picked)
        picked.pop()

def combination(n, r, answer, picked=set()):
    if len(picked) >= r:
        if picked not in answer:
            answer.append(set(picked)) # Need to deep-copy the list
            #print picked
            return False
        else:
            return False

    for i in range(n):
        if i in picked:
            continue
        picked.add(i)
        flag = combination(n, r, answer, picked)
        picked.pop()

answer = []
permutation(5,3, answer)
for idx, a in enumerate(answer):
    print idx+1, a

answer_c = []
combination(5,3, answer_c)
for idx, a in enumerate(answer_c):
    print idx+1, a

