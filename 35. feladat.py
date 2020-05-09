import numpy as np
import matplotlib.pyplot as plt


def mutat(ls):
    elemek=[]
    elofordulas=[]
    ls=np.asarray(ls)
    np.sort(ls)
    for i in ls:
        if i not in elemek:
            elemek.append(i)
            elofordulas.append(np.sum(ls==i))
    plt.bar(elemek,elofordulas)
    plt.title("Elemek előfordulása a listában")
    plt.xlabel("Elemek")
    plt.ylabel("Előfordulás száma")
    plt.show()