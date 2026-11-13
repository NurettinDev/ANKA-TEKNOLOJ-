#asal sayı kontrolü
input_number=int(input("Bir sayı girin:"))
isPrime=True
if(input_number<0):
    print("Negatif bir sayı girdiniz.Pozitif bir sayı girin")
elif(input_number>0 and input_number<2):
    print("En küçük asal sayı 2 dir")
else:
    for i in range(2,int(input_number**0.5)+1):#sayının karaköküne kadar olan sayılara bölümünü kontrol eder
        if(input_number%i==0):
            isPrime=False
            break
    if(isPrime):
            print(f"{input_number} bir asal sayıdır")
    else:
            print(f"{input_number} bir asal sayı değildir")