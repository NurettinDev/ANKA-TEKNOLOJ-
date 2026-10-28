#%%
# HDR farklı pozlamalarda aynı anda birkaç fotoğraf çekerek bu fotoğrafları birleştirir.
# Tek çekimlerde odaklamadan kaynaklı oluşan fazla parlak bölgeler bu farklı fotoğraflar uygun bir şekilde birleştirlierek yöntemiyle yok edilir.
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def readImagesandTimes():
    filenames = ["hdr1.jpg", "hdr2.jpg"]
    times = np.array([1/2, 1/6], dtype=np.float32) # Pozlama değerleri tutuluyor

    images = []
    for filename in filenames:
        im = cv.imread("Pictures\\" + filename)
        im = cv.cvtColor(im, cv.COLOR_BGR2RGB)
        images.append(im)

    return images, times

images, times = readImagesandTimes()  

# HDR da resimler birbirinin üzerine bineceği için resimler createalignMTB ile align edilir
# farklı pozlamalı fotoğrafları birbirine hizalayan OpenCV sınıfıdır. 
# MTB Median Threshold Bitmap (medyan eşikli bit haritası) anlamına gelir.

# Neden gerekli? HDR birleştirme için çekilen fotoğraflar elde ya da hafif oynayan tripodla çekildiyse birkaç piksel kayar. Hizalama yapmadan birleştirirsen sonuçta hayalet/bulanık kenarlar oluşur.

# Her resmi gri yapar.
# Resmin medyan parlaklığını bulur ve eşikleme yapar: medyandan parlak pikseller 1, koyu olanlar 0.
# Medyan eşik kullanıldığı için pozlama ne kadar farklı olursa olsun iki resimde aynı bit haritası (yaklaşık) çıkar. Bu yüzden farklı pozlamalarda bile karşılaştırılabilir.
# Küçültülmüş sürümlerden başlayıp büyüterek (piramit) bit haritaları üst üste oturtur ve en iyi kaymayı (x, y öteleme) bulur.
# Yalnızca öteleme (kayma) düzeltir. Dönme ve ölçek değişimini düzeltmez.

alignMTB = cv.createAlignMTB()
alignMTB.process(images,images)

# Camera Response Function (CRF): Sahnedeki gerçek ışık miktarı ile kameranın ürettiği piksel değeri arasındaki dönüşüm eğrisidir.
# Neden var? Kamera ışığı doğrusal kaydetmez. 
# Sensörden gelen sinyal; gama, kontrast ve renk işleme adımlarından geçer, sonra JPEG’e yazılır. 
# Yani piksel değeri 200 olan bir nokta, 100 olan noktadan “iki kat” ışık almış demek değildir.

# HDR’da neden gerekli? Farklı pozlamalı fotoğrafları gerçek ışık değerleri üzerinden birleştirmek için önce piksel değerlerini tekrar doğrusal radyansa çevirmen gerekir. 
# Bunun için CRF’nin tersi kullanılır. 
# CRF bilinmezse parlaklıklar yanlış ağırlıklanır ve HDR sonucu bozuk görünür.

calibrateDebevec = cv.createCalibrateDebevec() # Debevec bir yöntemdir Aynı sahnenin farklı pozlama sürelerindeki fotoğraflarına bakar. Her piksel değerinin, pozlama süresi değiştikçe nasıl değiştiğini kullanarak kameranın ışığı piksel değerine nasıl çevirdiğini kestirir.
responseDebevec = calibrateDebevec.process(images, times)

mergeDebevec = cv.createMergeDebevec()
hdrDebevec = mergeDebevec.process(images, times, responseDebevec)

# Tone mapping 
# HDR resmin geniş parlaklık aralığını ekranın gösterebildiği dar aralığa (0-255) sıkıştırma işlemidir.
# HDR birleştirme sonucu gerçek ışık değerlerini float32 olarak tutar ve bu değerler 0-1 ile sınırlı değildir. 
# Güneşin olduğu bölge 1000, gölge 0.01 olabilir. 
# Ekran ve JPEG/PNG ise yalnızca 0-255 gösterebilir. 
# HDR’ı doğrudan gösterirsen ya parlak bölgeler patlar ya da resim aşırı koyu görünür. 
# Tone mapping bu aralığı detayı koruyarak sıkıştırır.

# Parlaklık değerlerini doğrusal olmayan bir eğriyle bastırır. 
# Çok parlak bölgeler güçlü sıkıştırılır, orta ve koyu bölgeler daha az. 
# Böylece hem gökyüzündeki hem gölgedeki detay aynı resimde görünür.

tonemapDrago = cv.createTonemapDrago(1.0, 0.7)
ldrDrago = tonemapDrago.process(hdrDebevec)

plt.figure(figsize=[20,10]); plt.imshow(np.clip(ldrDrago,0,1)); plt.axis("off")

# %%
