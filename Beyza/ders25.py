text="706737"
result=text.isdigit()#hepsi sayıdan oluşuyorsa TRue
print(result)
y="\u0032"
print(int(y,16))# 16 lık sistemdeki karşılığını verir
a="_Beyza2"
print(a.isidentifier())#içinde harf,rakam ve _ olabilir ama rakamla başlayamaz ve boşluk falan içerirse False olur
#islower harfleri küçültür,isupper harfleri büyültür
# isnumeric sadece rakam varsa True döndürür
#isprintable ekrana yazdrılamayan ifadeler varsa yani (\n gibi şeyler varsa olmaz) False
# isspace tamamı boşluktan oluşuyorsa True
#istitle her kelimenin baş harfi büyükse True
Number=("a","b","c","d")
result3=":".join(Number)#join ayırma işlemi yapar(: ile ayır diyor yani)
print(result3)
#ljust ve rjust ifadeyi sola ve sağa yanaştırır(istediğin kadar)
result4=a.rjust(10,".")#10 tab boşluğun solda kalcak şekilde . koy geri kalanına text i yazdır
print(result4,"favorite number")
#strip başta ve sondaki boşlukları silip atar(neyi kaldırmak istersen onu kaldırır)
text1="hello, python"
result1=str.maketrans("p","t")#p yi t ye çevirir(3. bir veri girersem girdiğim şeyleri textten çıkartır )
print(text1.translate(result1))
#partition() içine yazılan veriye göre texti 3 e ayırıyor
#replace("a","b",3) a nın yerine b yi koyar (ilk gördüğü 3 a da)
#split(" ") her boşlukta kelimeleri ayrıp liste oluşturur
#zfill(10) kapladığı yer 10 olana kadar başını 0 ile doldur
