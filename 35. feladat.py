import numpy as np
import matplotlib.pyplot as plt


def mutat(ls):
    if ls==['']:
        return "Az ön listája üres."
    elemek=[]
    elofordulas=[]
    ls=np.sort(np.asarray(ls))
    for i in ls:
        if i not in elemek:
            elemek.append(i)
            elofordulas.append(np.sum(ls==i))
    plt.bar(elemek,elofordulas,color="g")
    plt.title("Elemek előfordulása a listában")
    plt.xlabel("Elemek")
    plt.ylabel("Előfordulás száma")
    plt.show()
    if max(elofordulas)>len(ls)/2:
        for i in range(len(elofordulas)):
            if elofordulas[i]==max(elofordulas):
                return f"{elemek[i]} ({max(elofordulas)}x szerepel egy {len(ls)} hosszú listában)\n"
    return ""


while True:
    a=input("Adja meg egy lista elemeit vesszővel elválasztva (stop beírása esetén kilép a programból): ").split(",")
    if a==['stop']:
        break
    print(mutat(a))
