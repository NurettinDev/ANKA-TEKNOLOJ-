#While Loop
i=1
while(i<=7):
    print(i,end=" ")#yanyana yazdırmak için end ekledik
    if(i==4):
        break#koşul sağlandığında döngüyü kırıp sonlandırıyor
    i+=1
print("\n done")


i=0
while(i<=7):
    i+=1
    if(i==4):
         continue#koşul sağlanınca döngünün içindeki kendinden sonraki komutu atlar
    print(i,end=" ")#yanyana yazdırmak için end ekledik
    
print("\n done")


i=1
while(i<=7):
    print(i,end=" ")
    i+=1
else:
    print(f"\n i({i}) veriable is no longer than 7")#i=8 olunca bitti
print("\n while loop is over")
#NOT: döngünün içinde ne olmasını istiyorsak aynı satır hizasına yazmamız gerekli çünkü c deki gibi {} yok

myNumber=[70,14,25,65,3]

i=0
while(i<len(myNumber)):
    print(myNumber[i],end=",")
    i+=1
