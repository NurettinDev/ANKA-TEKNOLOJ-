#obeb okek bulma
number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))
smaller=min(number1,number2)

for i in range(smaller,0,-1):
    if(number1%i ==0 and number2%i ==0):
        obeb=i
        break
okek=(number2*number1)//obeb
print(f"The obeb of {number1} and {number2} is {obeb}")
print(f"The okek of {number1} and {number2} is {okek}")
