import random
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def twopersonwalk(start1=2,start2=5, draw=False):
    x1 = start1
    x2 = start2
    res1 = []
    res2=[]

    for i in range(100):
        res1.append(x1)
        res2.append(x2)
        if (x1==x2):

            x1 += random.choice([-1, 1])
            x2 += random.choice([-1, 1])
            res1.append(x1)
            res2.append(x2)
            break
        x1 += random.randint(-1, 1)
        x2 += random.randint(-1, 1)

    #plt.figure(figsize=[10, 10])
    if draw==True:
        plt.suptitle('one of the random walks of two people', fontsize=16)
        plt.plot([s for s in range(len(res1))], res1, 'g')
        plt.plot([s for s in range(len(res2))], res2)
        plt.xlabel('steps')
        plt.ylabel('position')
        plt.grid(True)
        plt.show()

    if (i < 99):
        return i
    return 0

def twopersongraph():
    res={}
    for i in range(100):
        res[i]=0
    for i in range(100):
        a = twopersonwalk()
        if a in res.keys():
            res[a]=res[a]+1
    res.pop(0)

    fig, ax = plt.subplots()

    ax.bar(list(res.keys()), list(res.values()))
    plt.suptitle('frequency of how much time it took for\ntwo people to cross paths', fontsize=16)

    plt.ylabel('frequency')
    plt.xlabel('time/steps')
    plt.show()

twopersongraph()
#twopersonwalk(draw=True)
