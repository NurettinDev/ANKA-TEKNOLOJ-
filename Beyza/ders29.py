#boolean fonksiyonu
print("bool('python'):",bool("python"))#içerde herhangi bir şey yazıyrsa True
print("bool(''):",bool(""))#boş bırekırsan ya da 0 değerini girersen False
# is operatörü nesnelerin aynı olup olmamasına bakar, = ise nesnelerin içeriklerine bakar

fruit=["strawberry","grape","pineapple","banana"]
print("apple" in fruit)#fruitin içinde apple varmı diyor (False) not in olsaydı yokmu diye sorar(True)
fruit.append("cherry")#listenin sonuna ekleme yapar
fruit.insert(1,"melon")#listede istediği indexin yerine istediğin şeyi sıkıştırıyor
print(fruit[4])#listedeki 4. indexli elemanı gösterir
new_fruit=fruit.copy()#bir kopyasını oluşturmak için kullanılır sonradan değiştirilen şeylerde kopya etkilenmez
new_fruit=list(fruit)#copy nin aynısı
new_fruit=fruit[:]#bu yöntemde bir kopya oluşturur
fruit2=["lemon","lime"]
fruit.extend(fruit2)#listeyi genişletti (sonuna ekleme yaptı)
print(fruit)#listeyi gösterir
print(new_fruit)
print(len(fruit))#listenin kaç elemandan oluştuğunu söyler
# ~ işareti bitsel değil olarak kullanılır girilen ondalığın 1 fazlasının - işaretlisi olur