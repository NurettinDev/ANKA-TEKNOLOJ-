#%%
print("\n-----------------------------------------------------------------------------------\n")
#Sınıf içerisindeki fonksiyonlara metod denir "__xx__" şeklinde tanımlanır
#__init__() sınıftan bir obje oluşturulurken her zaman çağırılır.
# parametre olarak __init__(self) verilmelidir. Eğer boş kalmaması grekn bilgiler varsa
# def __init__(self, nameInput, ageInput, genderInput) şeklinde tanımlanmalıdır

class Person():
    name=""
    age=0          # bu 3 değer tanımlanmasa da init içerisinde bulunan self.name gibi değişkenler varsa python bunları varmış gibi varsayar
    gender=""

    #initializer metod
    def __init__(self, nameInput, ageInput, genderInput):
        self.name = nameInput
        self.age = ageInput
        self.gender = genderInput
    
    #metod
    def test(self):
        print("Metod")

yeni_kisi = Person("Kaan", 22, "Male")
print("İsim : " + yeni_kisi.name + " Yaş : " + str(yeni_kisi.age) + " Cinsiyet : " + yeni_kisi.gender)


class Dog():
    year = 7
    def __init__(self,age=5):  #default değer
        self.age = age
        self.doghumanage= age * self.year

    def human_age(self): #iki farklı yöntem
        return self.age * self.year
        

kopek = Dog(3)
print(kopek.human_age())
print(kopek.doghumanage)

print("\n-----------------------------------------------------------------------------------\n")
#Inheritance

class Musician():
    def __init__(self, name):
        self.name = name

    def test1(self):
        print("test1")

    def test2(self):
        print("test2")

class MusicianPlus(Musician): #kalıtım alındı
    def __init__(self,name):
        Musician.__init__(self,name)
        print("Plus")

    def test1(self): #override (üstüne yazma)
        print("testtesttesttest")

eloka = Musician("Elif")   
kaan = MusicianPlus("Kaan")
print("\nİsim 2 :", kaan.name)
kaan.test1()
kaan.test2()

print("\nİsim 1:", eloka.name)
eloka.test1()
eloka.test2()

print("\n-----------------------------------------------------------------------------------\n")
#Polymorphism

class Banana():
    def __init__(self, name):
        self.name = name
    
    def info(self):
        return f"100 kalori {self.name}"

class Apple():
    def __init__(self, name):
        self.name = name
    
    def info(self):
        return f"150 kalori {self.name}"

apple = Apple("apple")
banana = Banana("banana")
meyve_listesi = [banana,apple]
for meyve in meyve_listesi:
    print(meyve.info())

print("\n-----------------------------------------------------------------------------------\n")
#Encapsulation (Hapsetmek, İstenmeyen değişiklikleri önleme, Erişilmemesi gereken yere ksıtlama)
#değişken önüne iki alt çizgi ile yapılır

class Phone():
    def __init__(self,name, price):
        self.name = name
        self.__price = price

    def info(self):
        print(f"{self.name}'s price is : {self.__price}")

    def __str__(self): # normalde print("iphone") çalıştığında kaydedilen bellek adresi dönerken __str__ ile istenilen mesaj yazdırılabilir
        return f"{self.name} fiyatı : {self.__price}"

iphone = Phone("Iphone 15", 500)
iphone.__price = 200
print(iphone.info()) # 200 yapsak bile 500 kalır
print(iphone)

print("\n-----------------------------------------------------------------------------------\n")
#Abstraction (Soyutlama)
#içerisinde işlem yapılmayacak sınıflar için kullanılır.
#Sınıfı bir işlem için değil içerisindeki yapısı için kullanılır
#Soyut sınıftan obje oluşturulamaz

from abc import ABC, abstractmethod

class ArabaOzellik(ABC):
    
    @abstractmethod
    def maxSpeed(self):
        pass

class Tesla(ArabaOzellik):
    def maxSpeed(self):
        print("200 km/h")

class Mercedes(ArabaOzellik): #Soyuttan türetilen bir sınıfta abstract sınıfta bulunan her metod türetilen metodda bulunmalıdır
    def maxSpeed(self):
        print("250 km/h")

tesla = Tesla()
merc = Mercedes()
# %%
