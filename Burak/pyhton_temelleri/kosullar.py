

from datetime import datetime 

# isim=input("İsminizi Giriniz ")
# age=int(input("Lütfen Yaşınızı Giriniz "))
# school=input("Okul Durumuzunu Giriniz ")

# school_result= ((school=="Üniversite")or(school=="üniversite"))or((school=="Lise")or(school=="lise"))

# if(age>18 and school_result):
#     print("Ehliyet Alabilirsiniz ")
# elif(school_result==0):
#     print("Okul Durumunuz Uygun Değil")
# elif(age<18):
#     print("Yaşınız Uygun Değil")
# else:
#     print("Ehliyet Almaya Uygun Değilsiniz")         
    

# vize1=int(input("İlk Vize Notunuzu Giriniz : "))
# vize2=int(input("İkinci Vize Notunuzu Giriniz : "))
# final=int(input("Final Notunuzu Giriniz : "))

# ortalama=((vize1+vize2)/2)*0.4+final*0.6

# if(ortalama>=0  and ortalama<25):
#     print("Ortalama Notunuz : 0")
# elif(ortalama>=25 and ortalama<45):
#     print("Ortalama Notunuz : 1")
# elif(ortalama>=45 and ortalama<55):
#     print("Ortalama Notunuz : 2")
# elif(ortalama>=55 and ortalama<70):    
#     print("Ortalama Notunuz : 3")
# elif(ortalama>=70 and ortalama<85):
#     print("Ortalama Notunuz : 4")
# elif(ortalama>=85 and ortalama<101):
#     print("Ortalama Notunuz : 5")
# else:
#     print("Notunuz Geçerli Aralıklarda Değil.")


car_time=str(input("Lütfen Aracınızın Trafiğe Çıkış Gününü Giriniz.(Yıl/Ay/Gün) : "))

year=car_time.split("/")

today=(datetime.now())

result_year=((today.year)-int(year[0]))*365
result_month = (2(today.month)-int(year[1]))*30
result_day=(today.day)-int(year[-1])

fark=result_year+result_day+result_month
print(f"Aracı Almanızın Üstünden {fark} gün geçti ")
