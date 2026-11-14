'''
#Kullanıcıdan 7 sayı alıp küçükten büyüğe doğru sıralı yazdırmak 
myNumbers=[]
i=0
while(i<7):
    input_number=int(input("Enter an integer:"))#kullanıcıdan 7 tane sayı almak için
    myNumbers.append(input_number)#içine aktarsın diye append
    i+=1
myNumbers.sort()#küçükten büyüğe sıralasın diye sort
x=0
while(x<7):
    print(myNumbers[x],end=" ")#yanyana yazması için end 
    x+=1
'''
#ÇİFT sayıları yazdırma
number=int(input("Enter the start number:"))
end_number=int(input("Enter the ending number:"))
while(number<end_number):
    if(number%2==0):#2 ye bölümünden kalan 0 ise çift 1 ise tek
        print(number,end=" ")
    number+=1
