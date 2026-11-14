text= "Welcome to my world. My world is python"
result1=text.count("world")#text te world kelimesinin ne kadar geçtiğini gösterir
result2=text.startswith("Wel")#başlangıç değerim bununlamı başlıyor diyor(T/F)
result3=text.endswith("thon")#sonunda ne var bununlamı bitiyor(T/F)
result=text.find("wor")#ilk kez bununla karşılaştığı yerin indexini verir-yoksada -1 verir
result5=text.index("python")#find gibi ama bulamazsa hata veriyor
text2="Pyton"
result11=text2.isalnum()#alfanumeric  yani sayı yada harften başka birşey içerirse False
result4=text2.isalpha()#a-z ye sadece harh içerirse True
result6=text2.isascii()#ascii değerlerinden farklı bir şey varsa False
result4=text2.isdecimal()#sadece rakamlardan oluşursa True
print(result6)

#tabsların uzunluğunu belirler
''''
text2="P\ty\tt\th\to\tn"
print(text2.expandtabs())#boş bırakırsak "8" kabul eder
print(text2.expandtabs(2))
print(text2.expandtabs(10))
'''
