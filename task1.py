import random
import matplotlib.pyplot as plt
import numpy as np


def walkendgraph(startingposition=0,rightweight=1,leftweight = 1,nomovement = 1):

    probablities = [1] * rightweight + [0] * nomovement + [-1] *leftweight

    x=startingposition
    res= {}
    for i in range(-10,11,1):
        res[i]=0
    for i in range(1000):
        for j in range (20):
            x+= random.choice(probablities)
        if (-11<x<11):
            res[x]=res[x]+1
        #plt.plot[res.keys(),res.values()]
        x=startingposition

    plt.bar(list(res.keys()), list(res.values()))
    plt.suptitle('times how many times walk ended at a certain distance\nwith starting position 5', fontsize=10)
    plt.xlabel('distances')
    plt.ylabel('no of times a walk ended')

    #plt.plot(list(res.keys()), list(res.values()))

    plt.show()

def path():
    x=0
    steps=11
    res= []

    for i in range(steps):
        res.append(x)
        x+=random.randint(-1,1)
    plt.figure(figsize=[10,10])
    plt.suptitle('one of the random walks', fontsize=16)

    plt.xticks([s for s in range(len(res))])
    plt.plot([s for s in range(len(res))], res)
    plt.scatter([s for s in range(len(res))], res)
    plt.xlabel('steps')
    plt.ylabel('position')
    plt.axis([0, len(res), -10, 10])
    plt.grid(True)
    plt.show()

