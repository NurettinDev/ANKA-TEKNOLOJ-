#%%
d = {"k1":1, "k2":2, "k3":3}

for item in d:
    print(item) # sadece keyler gelir

for item in d.items():
    print(item) # tüm key value lar gelir

for item in d.values():
    print(item) # sadece value gelir

for item in d.keys():
    print(item) # sadece keyler gelir

for key, value in d:
    print(key, value) # sadece keyler gelir
# %%
urun_sayi = int(input("Ürün sayısını giriniz : "))
urunler = {}
i = 0
while i < urun_sayi:
    urun_ad = input("Ürün adını giriniz : ")
    urun_fiyat = int(input("Ürün fiyatını giriniz : "))
    urunler[urun_ad] = urun_fiyat
    i+=1

for ad, fiyat in urunler.items():
    print(f"{ad} fiyatı {fiyat} TL olacak şekilde listeye eklendi")

# %%
# enumerate
greeting = "Hello There"

for index, letter in enumerate(greeting):
    print(f"index : {index} letter : {letter}")

for item in enumerate(greeting):
    print(f"item: {item}")

# listeleri birleştirmek için zip kullanılır. Liste içerisinde tuple olarak tutar
# %%
numbers = [x for x in range(3) for y in range(3)]
print(numbers)