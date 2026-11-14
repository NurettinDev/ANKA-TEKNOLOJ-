#Inheritance (Kalıtım/Miras alma)
class Person: #parent class/ base class (ebeveyn-temel sınıf)
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def myPrint(self):
        print(self.firstname,self.lastname)

class Student(Person):# child class /derived class (çocuk-türetilmiş sınıf)
    #"pass" koyarsak olduğu gibi miras alabiliriz ama extra ekleme yapmak istiyorsak alttakini kullanmalıyız
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)  
        self.graduationyear=year
    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}")
p1=Student("Beyza","Yaman",2024)
p1.myPrint()
p1.welcome()
print(p1.graduationyear)
