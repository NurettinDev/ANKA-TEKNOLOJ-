#girilen sayının karakökünün tam sayı olup olmadığı
import math#bunun içindeki sqrt komutunu hiç kullanmadan sayıyı **0.5 ile üssünü alsaydıkta karakök almış olacaktık
myNumber=int(input("Enter a number:"))
square_root=math.sqrt(myNumber)

if(square_root==int(square_root)):
    print(f"The square root of {myNumber} is an integer: {int(square_root)}")
else:
    print(f"The square root of {myNumber} is not an integer: {square_root:.2f}")
