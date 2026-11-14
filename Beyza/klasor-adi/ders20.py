print(ord("F"))#ASCII tablo değerini gösteriri
print(ord("!"))
print(ord("Ü"))#genişletilmiş ascıı tablosu karşılığı
print(bin(70))#binary değeri 
print((255).bit_length())#bit uzunluğunu gösteririr

'''
text="Ç"
result=text.encode("ascii")#çıktı alamayız çünkü ascii de "ç" yok
print(result)
'''

'''
test="\x50\x79\x74\x6F\x6E"#"python" ın hex.d karşılığı
result=test.encode("ascii")
result2=result.decode()
print(result)
print(result2)
print(type(result))
print(type(result2))
'''

#ascii de bulunmayan değerler için atama
text="Şükrü"
result6=text.encode(encoding="utf-8")#utf-8 deki karşılığını atar
result=text.encode(encoding="ascii", errors="backslashreplace")# backslash=\ atar
result2=text.encode(encoding="ascii", errors="ignore")#görmezden gelinmesini istersen
result3=text.encode(encoding="ascii", errors="namereplace")#açıklama yapmak için
result4=text.encode(encoding="ascii", errors="replace")#soru işareti atar
result5=text.encode(encoding="ascii", errors="xmlcharrefreplace")#xml karşılığını atar
print(result6)
print(result2)
print(result5)
print(result4)
