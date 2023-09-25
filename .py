print("Döviz İşlem")
print("EUR/USD:1\nUSD/TL:2\nEUR/TL:3\nSTR/TL:4\nSTR/EUR:5")

kur=int(input("KUR GİRİN:"))
miktar=int(input("MİKTAR GİRİN:"))

if kur == 1:
    print(miktar*1.07,"USD")

if kur == 2:
    print(miktar*27,"TL")

if kur == 3:
    print(miktar*29,"TL")

if kur == 4:
    print(miktar*33,"TL")

if kur == 5:
    print(miktar*3.902,"EUR")

