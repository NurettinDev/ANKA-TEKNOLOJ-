#Object oriented programming dunder/magic method
class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def __str__(self):
        return f"Name:{self.name}\nAge:{self.age}"
p1=Person("Beyza Yaman",20)
print(p1)
# def __repr__(self):#daha detaylı göstermek için kullanılır(türünüde gösterir)
#     return f"Name:{self.name!r}\nAge:{self.age!r}"
