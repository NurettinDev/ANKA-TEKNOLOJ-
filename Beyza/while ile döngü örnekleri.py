'''
#isim girene kadar sonsuz döngü
while(True):
    name=input("Enter your name:")
    if(name==""):#boş bırakırsa başa döner contunuue ile
        continue
    else:
        break
print(f"your name is {name}")
'''
#faktöriyel hesaplama
result=1
i=1
number=int(input("Enter an integer:"))
while(i<=number):
       result*=i
       i+=1
print(f"{number}!={result}")
      
