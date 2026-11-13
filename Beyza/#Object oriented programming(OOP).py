#Object oriented programming(OOP)
# class MyClass:
#     x=7 #veriable->propert

# obj=MyClass()
# print(obj.x)
'''
class Vehicle:
    brand="Skoda"
    model="Superb"
    color="White"

car_obj=Vehicle()
print("Brand=",car_obj.brand)
print("Model=",car_obj.model)
print("Color=",car_obj.color)
'''
#init=başlat
def __init__(self):#constructor method(function)
    pass
class Vehicle:
    def __init__(self,brand,model,color):
        self.brand=brand#instance veriables
        self.model=model
        self.color=color

car1_obj=Vehicle("skoda","superb","white")
car2_obj=Vehicle("honda","civic","green")

print(car1_obj.brand,"-",car1_obj.model,"-",car1_obj.color)
print(car2_obj.brand,"-",car2_obj.model,"-",car2_obj.color)