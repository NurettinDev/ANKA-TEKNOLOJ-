#%%
def changename (n):
    n = "user"

def changecity(n):
    n[0] = "İstanbul"

# parametre sayısı belirtmeden bu şekilde tanımlama yapılabilir. 
# tek yıldız tuple listesi olarak kaydeder.
def topla(*params):
    print(type(params))
    return sum(params)

# iki yıldız sözlük şeklinde tutar
def displayUser(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key} {value}")

def tumu(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

name = "Kaan"
changename(name)
print(name)

sehirler = ["İzmir", "Balıkesir"]
changecity(sehirler)
print(sehirler) # referans tipinde değişiklik olurken value tipinde değişiklik olmaz.

print(topla(10,20,30,40))
print(topla(10,20,30))

displayUser(isim = "Çınar", yas = 4)
displayUser(isim = "Ali", yas = 34, sehir = "İstanbul")

tumu(10, 20, 30, 40, 50, 60, k1 = "value 1", k2 = "value 2")
# %%
def listeyecevir(*args):
    return list(args)

print(listeyecevir(10,20,30,40,"abc", "def"))

# %%
def kareal(sayi): return sayi**2
sayilar = [1,3,5,4,9]
sonuc = list(map(kareal, sayilar))
print(sonuc)

# %%
sonuc2 = list(map(lambda num: num**2, sayilar))
print(sonuc2)
# %%
# map(): Her elemana bir fonksiyon uygular ve dönüştürülmüş değerleri verir. 
# Eleman sayısı değişmez.

# filter(): Her elemana koşul fonksiyonu uygular ve yalnızca koşulu sağlayanları 
# (fonksiyon True döndürenleri) bırakır. Elemanlar değişmez sayı azalabilir.
sayilar = [1, 2, 3, 4, 5, 6]

list(map(lambda x: x * 2, sayilar))          # [2, 4, 6, 8, 10, 12]
list(filter(lambda x: x % 2 == 0, sayilar))  # [2, 4, 6]