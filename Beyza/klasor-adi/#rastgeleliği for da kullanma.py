#rastgeleliği for da kullanma
'''
for item in range(1,19,3):# 1 den 19 a kadar 3 er arttırma 19 dahil değil
    print(item,end=" ")
    if(item==4):
        break
else:
    print("\n for loop finished")#break kullanılırsa bu kısımda kırıldığı için sonuçta görünmez
    '''
'''
number=int(input("Enter an integer:"))
for item in range(number):#girilen sayıya kadar sayılar atanır
    if(item%2==1):#tek sayıları es geçerek yazdırır
        continue
    print(item,end=" ")
else:
    print("\n For loop finished")
     '''
for item in range(8):
 if(item==4):#4 ü pas geçti
  pass#yerine ... (üç nokta)kullanılabilir
 #NOT: sonradan ekleme ve kodlama yapmak istiyorsak üç nokta yada pass kullanılabilir bu sayaede o kısım görmezden gelinir
 else:
  print(item,end=" ")
else:
 print("\n for loop finished")
