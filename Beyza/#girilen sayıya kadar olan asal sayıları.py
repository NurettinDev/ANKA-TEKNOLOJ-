#girilen sayıya kadar olan asal sayıları bulma
input_number=int(input("Bir sayı girin:"))
prime_numbers=[]
if(input_number<0):
    print("Negatif bir sayı girdiniz.Pozitif bir sayı girin")
elif(input_number>0 and input_number<2):
    print("En küçük asal sayı 2 dir")
else:
    prime_numbers.append(2)
    for i in range(3,input_number+1,2):#3 ten itibaren 2 şer artışla sayıya kadar olan sayıları i ye atıyor
        for j in range(3,int(i**0.5)+1):#3 ten sayının karaköküe kadar olan sayıları j ye atar
            if(i %j ==0):#i nin j ye bölümüden kalanı kontrol eder i j ye bölünüyorsa bırakır
               break
        else:#bölünmezse sayıyı diziye ekler
            prime_numbers.append(i)
    print(f"{prime_numbers}")