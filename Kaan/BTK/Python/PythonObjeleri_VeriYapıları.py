#%%
import math

# işlem önceliği oto yapılır
# işlemde int ve float varsa sonuç float döner
var_int = 2
var_float = 2.5
print(f"Tip için type() : {type(var_float)}")

print(f"10//3 : {10//3}") # sadece tam tarfı için
print(f"10**3 : {10**3}") # üs alma
#%%
#-------------------------- Vergi Alma -------------------------- 
vergi_oran = 27
maas = int(input("Maaşınızı giriniz : "))
print(f"Maaşınız : {maas} \nVergi Oranı : {vergi_oran}")
print(f"Vergiler sonrası kalan : {maas - (maas * (vergi_oran/100))}")

#%%
x, y, name, isStudent = (1, 2, "Kaan", True)

yukari = math.ceil(var_float)
asagi = math.floor(var_float)
print(yukari,asagi)

#%%
#-------------------------- Daire Alan + Çevre ------------------ 
pi = math.pi
r = float(input("Yarıçap Giriniz : "))
alan = pi*(r**2)
cevre = 2*pi*r
print(f"Daire Alanı : {alan:.2f}")
print(f"Daire Çevresi : {cevre:4.2}") # soldan 4 boşluk bırakır virgülden sonra 2 karakter yazar

#%%
dene_str = " Anka technology: KaanPULAT"
print(dene_str[2:8])      # 2. indeksten 7. dahil
print(dene_str[2:8:2])    # 2 4 6. indeksler
print(dene_str[::3])      # baştan sona 3 er atlayarak
print(dene_str[::-1])     # ters çevirir
print(dene_str[8:2:-1])   # geriye doğru 8 den 3 e

print("{s} {n} {a}".format(n = "Kaan", s = "Pulat", a = 22))

#%%
#-------------------------- Soru / Cevap ------------------ 
website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1 
print(len(course))
# 2
print(website[7:10])
# 3
print(website[len(website)-3:len(website)])
# 4
print(f"{course[:15]} {course[len(course)-15:]}")
# 5
print(course[::-1])
# 7
var_str = "Hello world"
var_str = var_str.replace(var_str[6], "W")
print(var_str)
# 8
var_str2 = "abc"
print(var_str2*3)

# %%
print(dene_str.upper())
print(dene_str.lower())
print(dene_str.title())
print(dene_str.capitalize())
print(dene_str.strip()) # baş ve sondaki boşlukalr silinir
print(dene_str.split()) # boşluklara göre ayrır
print(dene_str.strip(":")) # : lara göre ayırır 

# string = "*".join(ayrık_mesaj) dizide halde bulunan ayrık mesajı birleştirir ve her birleştirme arasına * koyar

print(dene_str.find("Kaan"))
print(dene_str.startswith("A")) # A ile başlar mı diye sorar
print(dene_str.endswith("T")) # T ile mi biter diye sorar
print(dene_str.center(60, "*"))
# %%
