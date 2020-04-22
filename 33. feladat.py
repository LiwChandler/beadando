domainveg=[".com",".hu"]
domain_tiltott_karakterek=[" ","_",",","?","!","*",":",";"]

while True:
    try:
        cim=str(input("Adjon meg egy e-mail címet (stop beírása esetén a program leáll): "))
        if "@" not in cim:
            print("Az email cím nem tartalmaz '@'-ot")

        for i in cim[0:cim.find("@")+1]:
            if i in domain_tiltott_karakterek:
                raise
        if cim[cim.rfind("."):] not in domainveg:
