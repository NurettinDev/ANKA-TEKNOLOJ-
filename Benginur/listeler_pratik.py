# 1.Temel liste oluşturma ve eleman ekleme/çıkarma
notlar = [70, 85, 90, 45, 60]
notlar.append(100)      # sona eleman ekler
notlar.insert(1, 75)    # belirtilen indexe ekler (1. index)
notlar.remove(45)       # ilk eşleşen 45 değerini siler
silinen = notlar.pop()  # sondaki elemanı çıkarır ve değişkene atar

print("Güncel notlar:", notlar)
print("Çıkarılan not:", silinen)

# 2.Sıralama ve ters çevirme
sayilar = [12, 5, 23, 1, 89, 42]
sayilar.sort()          # küçükten büyüğe kalıcı sıralama
print("Sıralı hali:", sayilar)

sayilar.reverse()       # listeyi ters çevirir
print("Ters çevrilmiş:", sayilar)

#3.Dilimleme örneği
harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("İlk 3 eleman:", harfler[:3])
print("Ortadaki elemanlar:", harfler[2:5])
print("2şer atlayarak:", harfler[::2])

#4.Hızlı liste oluşturma
# 1'den 10'a kadar olan çift sayıların karesi
cift_kareler = [x**2 for x in range(1, 11) if x % 2 == 0]
print("Çift sayıların kareleri:", cift_kareler)

#5. İç içe liste (Nested list) örneği / Matris mantığı
matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 2. satır 3. elemana ulaşmak için (indexler 0'dan başlıyor)
print("Matrisin [1][2] elemanı:", matris[1][2])
