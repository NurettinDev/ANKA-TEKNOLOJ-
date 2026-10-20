

markalar=["BMW","Mercedes","Opel","Mazda"]
sayi=len(markalar)
print(markalar)
print(sayi)
ilkEleman=markalar[0]
print(ilkEleman)
sonEleman=markalar[-1]
print(sonEleman)
markalar[-1]="toyota"
print(markalar)
find=markalar.index("Mercedes")
print(find)
print(markalar[-2])
print(markalar[0:3])
markalar[-1]="Renault"
markalar[-2]="toyota"
print(markalar)
markalar=markalar+["Audi","Nissan"]
print(markalar)
del markalar[-1]
print(markalar)
markalar.reverse()
print(markalar)


student1=["Yiğit","Bilgi",2010,[70,60,70]]
student2=["Sena","Turan",1999,[80,80,70]]
student3=["Ahmet","Turan",1998,[80,70,90]]
öğrenciler=[student1 
            ,student2,
            student3]
print(öğrenciler)