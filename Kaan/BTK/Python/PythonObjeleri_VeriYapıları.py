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
#-------------------------- String Metodlar ------------------ 
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
#-------------------------- String Metodlar Sorular ------------------
# 1
print(" Hello World ".strip())
# 2
print("www.sadikturan.com".strip("wmoc."))
# 3
print(course.lower())
# 4
print(website.count("a")) # website.count("a",0,10) 0 ve 10 indeksleri içerisindekileri sayar
# 5
result = website.endswith("com") and website.startswith("www")
print(result)
# 6 
print(website.find(".com"))
# 7
print(course.isalpha())
# 8
print("Contents".center(50,"*"))
print("Contents".ljust(50,"*"))
# 9
print(course.replace(" ", "-"))
# 11
print(course.split(" "))

# %%
#-------------------------- Listeler ------------------
arabalar = ["BMW","Mercedes","Opel","Mazda"]
nums = [1,2,3,4,5,6,7,8,9]

nums.insert(1, 33)
nums.remove(3)
print(nums)
print(nums.index(33))

nums.sort()
print(nums)

nums.reverse()
print(nums)
# sort() ve reverse() metodlarının liste döndürmediği için direkt print içerisinde yazıldığında none döner 
# print(sorted(nums))
# print(list(reversed(nums)))

print("Mercedes" in arabalar)
del arabalar[-1]
print(arabalar)

# %%
#-------------------------- Tuples ------------------
# List değiştirilebilir Tuple değiştirilemez yalnızca count ve index metodları kullanılabilir
# Tek elemanlı tuple’da virgül şarttır
# Tuple içinde tanımlanan liste değiştirilebilir
t = ([1, 2], 3)
t[0].append(99)    
# t[0] = [5] type error verir        

# tuple a eleman eklemek için farklı bir tuple tanımlanıp birbirine eklenir
t = (1, 2, 3)
t = t + (4,)
print(t)

x,y = (10,20)
print(x)

#tuple listeye liste tuple a dönüştürülebilir list(tup) ve tuple(liste)
# %%
#-------------------------- Dictionary ------------------
users = {
    "Kaan Pulat" : {
        "age" : 23,
        "roles" : ["admin", "user"],
        "email" : "kaan@gmail.com"
    }
}

print(users["Kaan Pulat"]["age"])
print(users["Kaan Pulat"]["roles"][0])

name_surname = input("isim soyisim : ")
age = int(input("yaş : "))
email = input("mail: ")

users.update({
    name_surname: {
        "age" : age,
        "roles"  : ["user"],
        "email" : email
    }
})

print(users[name_surname])
# %%
#-------------------------- Sets ------------------
# Sırasız tekrar etmeyen elemanlardan oluşan değiştirilebilir koleksiyon
s = {1, 2, 3, 3, 2}
print(s)            # tekrarlar silinir

#{} boş sözlük oluşturur boş set için set()
a = {}        # dict
b = set()     # boş set

# Sırasızdır indeksle erişilmez s[0] hata verir
# Elemanları hashable olmalıdır sayı string tuple olabilir list ve başka set olamaz
# Eleman var mı kontrolü çok hızlıdır (x in s)

s = {1, 2, 3}
s.add(4)       # ekler
s.remove(2)    # siler yoksa KeyError
s.discard(99)  # siler yoksa hata vermez
s.pop()        # rastgele bir eleman çıkarır
s.clear()      # hepsini siler

a = {1, 2, 3, 4}
b = {3, 4, 5}

print(a | b)  # birleşim {1, 2, 3, 4, 5}
print(a & b)  # kesişim {3, 4}
print(a - b)  # fark {1, 2}
print(a ^ b)  # simetrik fark {1, 2, 5}

# union() intersection() difference() metodları da aynı işi yapar

print({1, 2} <= {1, 2, 3})    # sol sağdakinin alt kümesi mi sorusunu sorar

# Daha çok listeden tekrarları silmektir
liste = [1, 2, 2, 3, 3, 3]
ayiklanmis = list(set(liste))    # [1, 2, 3]

# sette {1,2,3} ile {3,2,1} aynı şeydir
# List sıralı ve tekrara izin verir tuple sıralı ve değişmez set sırasız ve benzersiz
# %%
