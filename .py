print("Döviz İşlem")
print("USD/TL:1\nEUR/TL:2\nSTR/TL:3")

kur=int(input("KUR GİRİN:"))
miktar=int(input("MİKTAR GİRİN:"))


if kur == 1:
    print(miktar*27,"TL")