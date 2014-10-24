def MtoJ():
    syote=float(input("Anna muutettava metri määrä: "))
    vastaus = syote * 3.28
    print("Metrit jalkoina: ",round(vastaus,2))

def JtoM():
    syote=float(input("Anna muutettava jalka määrä: "))
    vastaus = syote / 3.28
    print("Jalat metreinä: ",round(vastaus,2))

def EtoD():
    syote=float(input("Anna muutettava euro määrä: "))
    vastaus = syote * 1.2669
    print("Eurot dollareina: ",round(vastaus,2))

def CtoF():
    syote=float(input("Anna muutettava Celcius-määrä: ")) #lisätty
    vastaus = (syote*1.8 + 32)
    print("Celciukset Fahrenheitteina: ",round(vastaus,2)) 

def FtoC():
    syote=float(input("Anna muutettava Fahrenfeit määrä: "))
    vastaus = syote / 1.8 + 32 #tässä on muuten virhe
    print("Fahrenheitit celciuksina: ",round(vastaus,2))


while(True):
    print(" ")
    print("Yksikkömuunnin:\n1) Metrit Jaloiksi\n2) Jalat metreiksi")
    print("3) Eurot Dollareiksi\n4) Dollarit Euroiksi")
    print("5) Celciukset Fahrenheiteiksi\n6) Fahrenheitit Celciuksiksi")
    print("0) Lopeta")
    valinta=int(input("Mitä haluat tehdä?: "))
    if(valinta==0):
        break
    elif(valinta==1):
        MtoJ()
    elif(valinta==2):
        JtoM()
    elif(valinta==3):
        EtoD()
    elif(valinta==4):
        DtoE()
    elif(valinta==5):
        CtoF()
    elif(valinta==6):
        FtoC()
    else:
        print("Syöte ei kelpaa.")
