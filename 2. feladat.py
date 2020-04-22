import numpy as np

def eredmeny(b,c):
    c=np.asarray(c)
    ermek_sorrendben=np.sort(c)[::-1]
    vegeredmeny=""
    flag=0
    for i in ermek_sorrendben:
        if b//i>=1 and flag==1:
            vegeredmeny+=f";{b//i}db {i}Ft"
            b=b-(b//i)*i
        if b//i>=1 and flag==0:
            vegeredmeny+=f"{b//i}db {i}Ft"
            b=b-(b//i)*i
            flag+=1
    return vegeredmeny

def kiiras(a):
    for i in range(a):
        while True:
            try:
                szam=int(input(f"Adja meg a(z) {i}. pénzösszeget: "))
                if szam<1 or szam>100000:
                    raise
                print(eredmeny(szam,ermek))
                break
            except:
                print("Adjon meg egy 1 és 100000 közötti számot.")


while True:
    try:
        dbszam=int(input("A pénzösszegek darabszáma: "))
        if dbszam<1 or dbszam>1000:
            raise
        break
    except:
        print("Egy 1 és 1000 közötti számot adjon meg!")

ermek=[1,2,5,10,50,100]
kiiras(dbszam)
