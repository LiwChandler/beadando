domainveg=[".com",".hu"]
tiltott_karakterek=[" ","_",",","?","!","*",":",";"]


def helyes(a):
    if "@" not in a:
        return "A megadott email cím nem tartalmaz '@'-ot!"
    domain=a[a.find("@")+1:]
    if domain.find(".")==-1:
        return "A megadott e-mail cím vége nem megfelelő (pl.: '.hu', '.com')!"
    if domain[domain.rfind("."):] not in domainveg:
        return "A megadott domain vége nem engedélyezett!"
    if a[a.find("@")+1]!=a[a.find("@")+1].lower():
        return "A domain első betűje nem lehet nagybetű!"
    if a.find("@")==0:
        return "Az e-mail cím nem tartalmaz azonosítót!"

    flag1=None
    flag2=None
    for i in a[:a.find("@")]:
        if i in tiltott_karakterek:
            flag1=True
    for i in domain:
        if i in tiltott_karakterek:
            flag2=True
    if flag1 is True and flag2 is None:
        return "Az azonosító tiltott karaktert tartalmaz!"
    if flag1 is None and flag2 is True:
        return "A domain tiltott karaktert tartalmaz!"
    if flag1 is True and flag2 is True:
        return "Az azonosító és a domain is tiltott karaktert tartalmaz!"
    return "A megadott e-mail cím helyes!"


while True:
    cim=str(input("Adjon meg egy e-mail címet (stop beírása esetén kilép a programból): "))
    if cim=="stop":
        break
    print(helyes(cim))
    print()
