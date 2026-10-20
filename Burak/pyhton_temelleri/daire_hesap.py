import math
r=(input("Yarıçapı giriniz: "))
istenilen=(input("Alanı veya çevreyi hesaplamak istiyor musunuz? (alan/çevre/hepsi): "))
if istenilen=="alan":
    alan=math.pi*float(r)**2
    print(f"Alan: {alan:.2f}")
elif istenilen=="çevre":
    cevre=2*math.pi*float(r)
    print(f"Çevre: {cevre:.2f}")
elif istenilen=="hepsi":
    alan=math.pi*float(r)**2
    cevre=2*math.pi*float(r)
    print(f"Alan: {alan:.2f}")
    print(f"Çevre: {cevre:.2f}") 



