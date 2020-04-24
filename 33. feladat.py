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
            domain=cim[cim.find("@")+1:]
            if domain.find(".")==-1:
                print("A megadott e-mail cím vége nem megfelelő (pl.: '.hu', '.com')!")
                continue
            if domain[domain.rfind("."):] not in domainveg:
                print("A megadott domain vége nem engedélyezett!")
                continue
            if cim[cim.find("@")+1]!=cim[cim.find("@")+1].lower():
                print("A domain első betűje nem lehet nagybetű!")
                continue
            if cim.find("@")==0:
                print("Az e-mail cím nem tartalmaz azonosítót!")
                continue

            flag1=None
            flag2=None
            for i in cim[:cim.find("@")]:
                if i in tiltott_karakterek:
                    flag1=True
            for i in domain:
                if i in tiltott_karakterek:
                    flag2=True
            if flag1 is True and flag2 is None:
                print("Az azonosító tiltott karaktert tartalmaz!")
                continue
            if flag1 is None and flag2 is True:
                print("A domain tiltott karaktert tartalmaz!")
                continue
            if flag1 is True and flag2 is True:
                print("Az azonosító és a domain is tiltott karaktert tartalmaz!")
                continue
            print("A megadott e-mail cím helyes!")
        except:
            print("Helyes e-mail címet adjon meg!")


helyes()
