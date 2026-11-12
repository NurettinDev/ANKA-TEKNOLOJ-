Bu uygulamanın amacı belirli bakım işlerini belirlenen zamanda yapabilme, ekipman eksikleri varsa bakım işini yapmama, 
reddetmedir. 

İlk başta bakım işi ve bakım planlayıcısı olarak iki sınıftan oluşuyor. “Bakim_isi” sınıfı yapılacak işin kimliğini,
süresini, önceliğini, ekipmanın hazır olup olmadığını barındırıyor. Ayrıca “str” metoduyla kullanıcının nesnedeki değerleri okuyabilmesini 
amaçladım. “Bakim_planlayicisi” sınıfında ise kapasite değeri, kalan süre, reddedilen bakım işleri, kabul edilen bakım işleri ve bekleyen 
bakım işleri bulunuyor. 

Kalan süre kapasiteye eşitleniyor çünkü kalan süre en başta kapasiteye eşit, bakım işini yaptıkça azalıyor. “Plan_yap” 
fonksiyonu, öncelikle "süre pozitif tam sayı mı?" diye bakar sonrasında işin ekipmanları hazır değilse reddeder, işi reddedilenler listesine ekler. Ekipmanlar hazırsa süre karşılaştırması yapılır, kalan süre
bakım işinin süresinden büyükse o iş yapılır. Daha sonra kalan süreden bakım işinin süresi çıkartılarak yeni kalan zamanımız elde edilir. Ekipmanları
hazır olduğu için iş, kabul edilenler listesine eklenir. Eğer hiçbir koşul sağlanmıyorsa bekleyenler listesine eklenir. 

Karşılaştırılacak bakım işlerini diğer yerlerde kullanabilmek için “Bakim_isin_obj” nesnesine eklenir. İşler öncelik sırasında sıralamak için
bir listenin içine koyulur. Sonra “sort” yardımcısıyla “Isler” listesindekileri öncelik sırasına göre sıralanır, “reverse=true” koduyla büyük sayıdan 
küçük sayıya sıralanır. “key=oncelik_al” koduyla da “sort” yardımcısının neyi sıralayacağı belirtilir. Daha sonrasında Bakım planlayıcısı 
çağırılır ve kapasite değeri belirlenir. 

“Planlayici_obj.Plan_yap(Isler)”  koduyla “Isler” listesini “Plan_yap” metodunda sırayla inceleyip karar vermesi sağlanıyor. Son olarak da bulduğumuz değerler 
çıktı alınıyor.

### Öncelik değerlerinin aynı olduğu sürelerin farklı olduğu bir örnek ve öncelik değerleinin aynı olduğu birinin ekipmanının hazır olmadığı bir örnek:

İşler ve özellikleri:
```
Bakim_isi1_obj = Bakim_isi("M1", 3 , 2 , True  )
Bakim_isi2_obj = Bakim_isi("M2", 4 , 3 , True  )
Bakim_isi3_obj = Bakim_isi("M3", 3 , 2 , False )
Bakim_isi4_obj = Bakim_isi("M4", 4 , 9 , True  )
```
Çıktısı:
```
Kimlik: M2, Öncelik: 4, Süre: 3, Ekipman: True
Kimlik: M4, Öncelik: 4, Süre: 9, Ekipman: True
Kimlik: M1, Öncelik: 3, Süre: 2, Ekipman: True
Kimlik: M3, Öncelik: 3, Süre: 2, Ekipman: False
Kapasite= 10
Kalan Süre= 5
Kabul edilenler=
Kimlik: M2, Öncelik: 4, Süre: 3, Ekipman: True
Kimlik: M1, Öncelik: 3, Süre: 2, Ekipman: True
Reddedilenler=
M3 reddedildi:  Ekipman hazır değil.
Bekleyenler=
M4 bekliyor:  Süre kalan kapasiteye sığmadı. 
```

### Negatif olan ve tam sayı olmayan süreli bir örnek:

İşler ve özellikleri:
```
Bakim_isi1_obj = Bakim_isi("M1", 3 , 2 ,  True  )
Bakim_isi2_obj = Bakim_isi("M2", 2 , 3.5 , True )
Bakim_isi3_obj = Bakim_isi("M3", 5 , 2 ,  True  )
Bakim_isi4_obj = Bakim_isi("M4", 1 ,-5 ,  True  )
```

Çıktısı:
```
Kimlik: M3, Öncelik: 5, Süre: 2, Ekipman: True
Kimlik: M1, Öncelik: 3, Süre: 2, Ekipman: True
Kimlik: M2, Öncelik: 2, Süre: 3.5, Ekipman: True
Kimlik: M4, Öncelik: 1, Süre: -5, Ekipman: True
Kapasite= 13
Kalan Süre= 9
Kabul edilenler=
Kimlik: M3, Öncelik: 5, Süre: 2, Ekipman: True
Kimlik: M1, Öncelik: 3, Süre: 2, Ekipman: True
Reddedilenler=
M2 reddedildi:  Süre pozitif tam sayı değil.
M4 reddedildi:  Süre pozitif tam sayı değil.
Bekleyenler=
```

### Öncelik değerleri farklı ama öncelik değeri düşük olup süresi kısa olanın yapıldığı bir örnek:

İşler ve özellikleri:
```
Bakim_isi1_obj = Bakim_isi("M1", 4 , 5 , True  )
Bakim_isi2_obj = Bakim_isi("M2", 3 , 3 , False )
Bakim_isi3_obj = Bakim_isi("M3", 3 , 2 , True  )
Bakim_isi4_obj = Bakim_isi("M4", 5 , 5 , True  )
```

Çıktısı:
```
Kimlik: M4, Öncelik: 5, Süre: 5, Ekipman: True
Kimlik: M1, Öncelik: 4, Süre: 5, Ekipman: True
Kimlik: M2, Öncelik: 3, Süre: 3, Ekipman: False
Kimlik: M3, Öncelik: 3, Süre: 2, Ekipman: True
Kapasite= 7
Kalan Süre= 0
Kabul edilenler=
Kimlik: M4, Öncelik: 5, Süre: 5, Ekipman: True
Kimlik: M3, Öncelik: 3, Süre: 2, Ekipman: True
Reddedilenler=
M2 reddedildi:  Ekipman hazır değil.
Bekleyenler=
M1 bekliyor:  Süre kalan kapasiteye sığmadı.
```

### Hepsinin yapıldığı bir örnek:

İşler ve özellikleri:
```
Bakim_isi1_obj = Bakim_isi("M1", 4 , 2 , True  )
Bakim_isi2_obj = Bakim_isi("M2", 5 , 3 , True  )
Bakim_isi3_obj = Bakim_isi("M3", 2 , 2 , True  )
Bakim_isi4_obj = Bakim_isi("M4", 1 , 4 , True  )
```

Çıktılar:
```
Kimlik: M2, Öncelik: 5, Süre: 3, Ekipman: True
Kimlik: M1, Öncelik: 4, Süre: 2, Ekipman: True
Kimlik: M3, Öncelik: 2, Süre: 2, Ekipman: True
Kimlik: M4, Öncelik: 1, Süre: 4, Ekipman: True
Kapasite= 13
Kalan Süre= 2
Kabul edilenler=
Kimlik: M2, Öncelik: 5, Süre: 3, Ekipman: True
Kimlik: M1, Öncelik: 4, Süre: 2, Ekipman: True
Kimlik: M3, Öncelik: 2, Süre: 2, Ekipman: True
Kimlik: M4, Öncelik: 1, Süre: 4, Ekipman: True
Reddedilenler=
Bekleyenler=
```
