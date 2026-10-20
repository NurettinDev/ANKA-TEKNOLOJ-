

# number =[1,2,3,4,5]
# x=0
# for a in number:
#     print(x)
#     x=x+1

# isimler = ["Mert","İsmail","Kartal"]

# for name in isimler:
#     print(f"My name is {name}")

# name ="İsmail Kartlal"
# for harf in name:
#     print(harf)

# toplam=0
# sayilar =[1,3,4,5,6,7,19,26,42,55]

# # for sayi in sayilar:
# #     toplam+=+sayi
# #     print(toplam)
# sonuç=0
# for sayi in sayilar:
#     if(sayi % 2 == 1):
#        sonuç=sayi**2
#        print(f"Tek olan {sayi} nın karesi {sonuç}") 

# sehirler=["Kocaeli","İstanbul","Ankara","izmir","Rize"]

# for sehir in sehirler:
#     if(len(sehir)<=5):
#         print(F"En fazla 5 Harfe Sayip Şehirler {sehir}")
toplam_fiyat=0
urunler=[{"name":"samsung s6","price":"3000"},
         {"name":"samsung s7","price":"4000"},
         {"name":"samsung s8","price":"5000"},
         {"name":"samsung s9","price":"6000"},
         {"name":"samsung s10","price":"7000"}
         ]
for urun in urunler:
    if(int(urun["price"])<=5000):
        print(urun["name"])
        





