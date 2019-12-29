import numpy as np
import matplotlib.pyplot as plt

def average(lst): 
    return sum(lst) / len(lst)


def weightedavg(lst):
    total = 0
    weightsum = 0
    for i in range(len(lst)):
        total += lst[i]*(i+1)
        weightsum += i+1
    return total/weightsum


def normcoef(avg):
    return (avg - 1)/4


def findss(lst):
    # finds the sum of squares
    ss = 0
    mean = average(lst)
    for elem in lst:
        ss += (elem - mean) ** 2
    return ss


def findsp(lst1, lst2):
    # finds the sum of products
    sp = 0
    mean1 = average(lst1)
    mean2 = average(lst2)
    for i in range(len(lst1)):
        sp += (lst1[i] - mean1) * (lst2[i] - mean2)
    return sp


def findscore(lst, size):
    global xax
    slicex = xax[:size]
    slicey = lst[:size]
    meanx = average(slicex)
    meany = average(slicey)
    ss = findss(slicex)
    sp = findsp(slicex, slicey)
    b = sp / ss
    a = meany - b * meanx
    return b * (size + 1) + a

xax = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

y1 = np.array([1, 5, 1, 5, 1, 5, 1, 5, 1, 5])
y2 = np.array([1, 5, 5, 1, 1, 1, 1, 5, 5, 5])

#y1 = np.array([5, 5, 4, 4, 3, 3, 2, 2, 1, 1])
#y2 = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])

y3 = []
y4 = []

for i in range(len(y1)):
    #coefstart = i - 2
    #if coefstart < 0:
    #    coefstart = 0
    #coef = normcoef(average(y1[coefstart:i+1]))
    if i == 0:
        y3.append(y1[0])
    else:
        value = max(1, min(findscore(y1, i + 1), 5))
        y3.append(value)

for i in range(len(y2)):
    #coefstart = i - 2
    #if coefstart < 0:
    #    coefstart = 0
    #coef = normcoef(average(y2[coefstart:i+1]))
    if i == 0:
        y4.append(y2[0])
    else:
        value = max(1, min(findscore(y2, i + 1), 5))
        y4.append(value)

for idex in range(1, 20):
    if idex > 11:
        idx = 11
    else:
        idx = idex
    fig = plt.figure(figsize=(18,4))
    ax = fig.add_subplot(121)
    ax.text(5, 6.5, 'JOE', fontweight='bold', color='white', bbox={'facecolor': 'blue', 'alpha': 0.5, 'pad': 10})
    ax.set_xticklabels([])
    plt.yticks((1, 2, 3, 4, 5))
    ax.set(xlim=(0.5, 10.5), ylim=(0.000001, 7.99999))
    ax.bar(xax[:idx], y1[:idx], 0.5, color="green", alpha=0.5)
    ax.plot(xax[:idx], y3[:idx], color='black', marker='o')
    ax.plot(xax[:idx], y3[:idx], color='red')

    ax2 = fig.add_subplot(122)
    ax2.text(5, 6.5, 'SUSAN', fontweight='bold', color='white', bbox={'facecolor': 'blue', 'alpha': 0.5, 'pad': 10})
    ax2.set_xticklabels([])
    plt.yticks((1, 2, 3, 4, 5))
    ax2.set(xlim=(0.5, 10.5), ylim=(0.000001, 7.99999))
    ax2.bar(xax[:idx], y2[:idx], 0.5, color="green", alpha=0.5)
    ax2.plot(xax[:idx], y4[:idx], color='black', marker='o')
    ax2.plot(xax[:idx], y4[:idx], color='red')
    plt.savefig("images/img"+"{:02d}".format(int(idex))+".png")
