#%%
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

#%%
kaan_gbr = cv.imread(r"D:\ANKA\CV\OpenCV\Pictures\kaan.jpg", cv.IMREAD_COLOR)
kaan_bw = cv.imread(r"D:\ANKA\CV\OpenCV\Pictures\kaan.jpg", cv.IMREAD_GRAYSCALE)
kaan = cv.cvtColor(kaan_gbr, cv.COLOR_BGR2RGB)
#%%
#Parlaklık Ayarlama
matrix = np.ones(kaan.shape, dtype="uint8") * 50

kaan_parlak = cv.add(kaan, matrix)
kaan_karanlık = cv.subtract(kaan,matrix)

plt.figure(figsize=[20,10])
plt.subplot(131); plt.imshow(kaan); plt.title("Orijinal")
plt.subplot(132); plt.imshow(kaan_parlak); plt.title("Parlak")
plt.subplot(133); plt.imshow(kaan_karanlık); plt.title("Karanlık")
# %%
# Kontrast ayarlama
# Kontrast resimdeki en koyu ile en açık bölgeler arasındaki parlaklık farkıdır
# Yüksek kontrast: Koyular çok koyu, açıklar çok açık. Resim keskin ve canlı görünür ama gölge ve parlak bölgelerdeki detaylar kaybolabilir.
# Düşük kontrast: Parlaklık değerleri birbirine yakın. Resim soluk “sisli” görünür.

# Bu yöntemde oluşturacağımız matrix ile çarpım yaparak kontrast azaltıp arttıracağız
# Bu yöntemle kontrast artırma yaparken bazı piksel değerleri 255 üzerine çıkıp görüntüyü bozabilir

matrix1 = np.ones(kaan.shape) * 0.8
matrix2 = np.ones(kaan.shape) * 1.2 

# float değerlerler çarptığımız için ilk önce float sonra yeniden uint8 e dönüşüm yapcaz
kaan_ykont_bozuk = np.uint8(cv.multiply(np.float64(kaan), matrix2))
kaan_dkont = np.uint8(cv.multiply(np.float64(kaan), matrix1))

plt.figure(figsize=[20,10])
plt.subplot(131); plt.imshow(kaan); plt.title("Orijinal")
plt.subplot(132); plt.imshow(kaan_ykont_bozuk); plt.title("Yüksek Kontrast") # 255 i aşan pikseller görüntüyü bozdu
plt.subplot(133); plt.imshow(kaan_dkont); plt.title("Düşük Kontrast")

# Bozulmanın önüne geçebilmek için çarpım yaparken 0-255 arasına hapsedicez
kaan_ykont_duzgun = np.uint8(np.clip(cv.multiply(np.float64(kaan), matrix2),0,255)) # np.clip dizideki değerleri limitler
plt.figure(figsize=[20,10])
plt.subplot(131); plt.imshow(kaan); plt.title("Orijinal")
plt.subplot(132); plt.imshow(kaan_ykont_duzgun); plt.title("Yüksek Kontrast") 
plt.subplot(133); plt.imshow(kaan_dkont); plt.title("Düşük Kontrast")


# %%
# Eşikleme

# cv.threshold: tek eşik, tüm resim için

# ret, sonuc = cv.threshold(img, thresh, maxval, type)

# img: Gri tonlamalı resim.
# thresh: Eşik değeri (0-255).
# maxval: Koşulu sağlayan piksellere verilecek değer (genelde 255).
# type: Eşikleme türü.
# Dönüş: ret kullanılan eşik değeri, sonuc ikili resim.
# Türler:
# THRESH_BINARY	Eşikten büyükse maxval, değilse 0
# THRESH_BINARY_INV	Tersi: büyükse 0, değilse maxval
# THRESH_TRUNC	Eşikten büyükler eşiğe sabitlenir
# THRESH_TOZERO	Eşikten küçükler 0 olur, büyükler korunur
# THRESH_TOZERO_INV	Tersi

# Otsu yöntemi: Eşiği kendisi hesaplar (thresh yok sayılır):
# ret, sonuc = cv.threshold(kaan_bw, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
# print(ret)    # bulunan eşik

# cv.adaptiveThreshold: her bölge için ayrı eşik

# sonuc = cv.adaptiveThreshold(img, maxValue, adaptiveMethod, thresholdType, blockSize, C)
# maxValue: Koşulu sağlayan piksellere verilen değer (255).
# adaptiveMethod: Eşiğin komşuluktan nasıl hesaplanacağı.
# cv.ADAPTIVE_THRESH_MEAN_C: Komşuluğun ortalaması.
# cv.ADAPTIVE_THRESH_GAUSSIAN_C: Ağırlıklı (Gauss) ortalama, genelde daha iyi.
# thresholdType: Yalnızca THRESH_BINARY ya da THRESH_BINARY_INV.
# blockSize: Her piksel için bakılacak komşuluk penceresi. Tek sayı olmalı (11, 21...).
# C: Hesaplanan ortalamadan çıkarılan sabit. Eşiği ince ayar için kaydırır. (eşik = (komşuluk ortalaması) - C)
# Dönüş: Yalnızca sonuç resmi (ret yok).

# Düz ve homojen bölgelerde (gökyüzü, boş duvar) pikseller komşuluk ortalamasına çok yakındır. 
# C = 0 olursa bu bölgelerde piksel bazen ortalamanın azıcık üstünde bazen altında kalır ve sonuç benek benek gürültü olur. 
# Pozitif bir C “ortalamadan belirgin şekilde koyu değilse arka plan say” demektir ve bu gürültüyü bastırır.
 

retval, kaan_bw_tresh = cv.threshold(kaan_bw, thresh=100, 
                                     maxval=255, 
                                     type = cv.THRESH_BINARY)
kaan_bw_adaptresh = cv.adaptiveThreshold(kaan_bw, 
                                         maxValue=255,
                                         adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                         thresholdType= cv.THRESH_BINARY,
                                         blockSize= 11,
                                         C = 3)

plt.figure(figsize=[20,10])
plt.subplot(131); plt.imshow(kaan_bw, cmap="gray"); plt.title("Orijinal")
plt.subplot(132); plt.imshow(kaan_bw_tresh, cmap="gray"); plt.title("Eşikli") 
plt.subplot(133); plt.imshow(kaan_bw_adaptresh, cmap="gray"); plt.title("Adaptif Eşikli") 

# %%
# Bitwise işlemler de yapılabilir.
# cv.bitwise_or, cv.bitwise_and, cv.bitwise_xor 
# bu metodlar 2 resim ile çalışır
# üst üste gelen 2 resmin piksellerinden biri siyah biri beyazsa and de o piksel siyah olarak verilir
# or ise piksel beyaz olarak verilir
# xor bitler birbirinden farklıysa 255 aynıysa 0 üretir