#stinglerde format kullanımı
'''
text="The price is only {price:.2f} turkish lira!"
print(text.format(price=70))
text1="My name is {fname}, I'm {age} years old ".format(fname="Fehmi",age=34)
text2="My name is {0}, I'm {1} years old ".format("Fehmi",34)
text3="My name is {}, I'm {} years old ".format("Fehmi",34)
print(text1)
print(text2)
print(text3)
'''
text="we do not have {:<10} children"#yazacağın ifadeyi sola hizala ve 10 karakter boşlık bırak
print(text.format(7))# '>' olsaydı sağa hizalardı ,'^' olsaydı tam ortalardı
#'=' olsaydı ifadedeki - kısmı sola hizalardı
#'+' olsaydı ifadenin - yada + olduğunu belirtirdi
#'-' olsaydı pozitif ifadelerin başına + yazmayacaktı (- varsa yazar ama)
#' '(boşluk) olsaydı - li ifalerin - sini gösterir pozitiflerin başına boşluk bırakır
# ',' olsaydı büyük ifadelerde binlik ayırıcı olurdu (virgülle)
# '_' olsaydı büyük ifadelerde binlik ayırıcı olurdu( _ ile)
# 'b' olsaydı ifadeyi binary formunda yazardı
# 'c'olsaydı ifadenin unicod karşılığını yazardı
# 'd'olsaydı ifadeyi decimal formunda yazardı
# 'o'olsaydı ifadeyi octal formunda yazardı
# '.2f' olsaydı sayıyı ondalık sayı kısmında 2 basamak kalacak şekilde verir
# 'f' olsaydı virgülden sonra 6 basamak verirdi
# '.%' olsaydı % lik şekilde yazardı
#  bir şeyin başında 0b yazarsa binary 0x yazarsa hexadecimal olur




