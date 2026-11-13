# Uçuş Görev Sıralama Sistemi

# Algoritma Açıklaması
Geliştirilen sistemde öncelikle tüm görevler veri bütünlüğü, pozitif süre, 1-5 arası öncelik ve uçuşa uygunluk açısından denetlenir; kural dışı kayıtlar doğrudan 'reddedilir'. Geçerli kayıtlar, önceliği yüksek olandan düşük olana doğru, önceliklerin eşit olduğu durumlarda ise sisteme ilk eklenen önce işlenecek şekilde yani (FIFO)ile sıralanır. Ardından kalan uçuş süresi kapasitesi kontrol edilerek sıradaki görevin sığması durumunda uçuşa dahil edilir, sığmayan uygun görevler ise daha sonraki küçük görevlerin değerlendirilebilmesi için döngü bozulmadan 'bekliyor' durumuna alınır.

# Test Durumları ve Sonuçları (4 Senaryo)

# TEST 1: Hepsi Uygun ve Sığar
- *Girdi:Kapasite=15 | G1(Öncelik:3, Süre:4), G2(Öncelik:5, Süre:5), G3(Öncelik:4, Süre:3)
- *Sonuç:Uçuşa Alınanlar: G2, G3, G1 (Önceliğe göre sıralandı ve kapasiteye sığdı).

# TEST 2: Eşit Öncelik ve Sıralama Korunumu (FIFO)
- *Girdi:Kapasite=6 | A1(Öncelik:4, Süre:4), A2(Öncelik:4, Süre:4)
- *Sonuç:Uçuşa Alınanlar: A1 | Bekleyenler: A2 (Öncelikler eşit olduğu için önce gelen FIFO kuralıyla alındı, ikincisi kapasite yetmediği için bekledi).

# TEST 3: Uzun Görev Beklerken Kısa Görevin Alınması
- *Girdi:Kapasite=5 | B1(Öncelik:5, Süre:8), B2(Öncelik:3, Süre:3)
- *Sonuç:Uçuşa Alınanlar: B2 | Bekleyenler: B1 (B1 önceliği yüksek olmasına rağmen kapasiteye sığmadığı için beklemeye alındı, sıradaki uygun kısa görev B2 uçuşa dahil edildi).

# TEST 4: Hatalı ve Uygun Olmayan Kayıtlar
- *Girdi:Kapasite=10 | C1(Süre:0 - Hatalı), C2(Öncelik:6 - Hatalı), C3(Uygunluk:False)
- *Sonuç:Tüm hatalı ve uygun olmayan kayıtlar kurallar gereği başarıyla reddedildi ve nedenleri raporlandı.
