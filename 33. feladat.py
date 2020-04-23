domainveg=[".com",".hu"]
tiltott_karakterek=[" ","_",",","?","!","*",":",";"]


def helyes():
    while True:
        try:
            cim=str(input("Adjon meg egy e-mail címet (stop beírása esetén kilép a programból): "))
            if cim=="stop":
                break
            if "@" not in cim:
                print("A megadott email cím nem tartalmaz '@'-ot!")
                continue
            if cim[cim.find("@"):].find(".")==-1:
                print("A megadott e-mail cím vége nem megfelelő (pl.: '.hu', '.com')!")
                continue
            if cim[cim.rfind("."):] not in domainveg:
                print("A megadott domain vége nem engedélyezett!")
                continue
            if cim.rfind("@")==0:
                print("Az e-mail cím nem tartalmaz azonosítót!")
                continue
            if cim[cim.find("@")+1]==cim[cim.find("@")+1].capitalize():
                print("A domain első betűje nem lehet nagybetű!")
                continue
            for i in cim:
                if i in tiltott_karakterek:
                    print("Az email cím tiltott karaktert tartalmaz!")
                    continue
            print("A megadott e-mail cím helyes!")
        except:
            print("Helyes e-mail címet adjon meg!")


helyes()
