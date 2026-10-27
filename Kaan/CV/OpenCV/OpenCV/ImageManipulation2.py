#%%
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#%%
img = cv.imread(r"Pictures\chessboard.png", cv.IMREAD_GRAYSCALE)
img_original = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img_original)
# %%
# resmin pikselleriyle diziler ile oynayabiliriz
img_copy = img_original.copy()
img_copy[600,200] = 0
img_copy[599,199] = 0
img_copy[598,198] = 0
img_copy[597,197] = 0
img_copy[596,196] = 0

plt.imshow(img_copy)
# %%
# resim kırpma
kizilelma_bgr = cv.imread(r"Pictures\kizilelma.jpg", cv.IMREAD_COLOR)
kizilelma = cv.cvtColor(kizilelma_bgr, cv.COLOR_BGR2RGB)
plt.imshow(kizilelma)
print(kizilelma.shape)

cy, cx = kizilelma.shape[:2]
cropped_region = kizilelma[175:275, 300:450]
cropped_region2 = kizilelma[int((cy/2)-100) : int((cy/2)+100), int((cx/2)-100) : int((cx/2)+100)]

pencere = ["Yontem 1", "Yontem 2"]
resimler = [cropped_region, cropped_region2]

for ad, resim in zip(pencere, resimler):
    cv.imshow(ad, resim)
    cv.waitKey(3000)
    cv.destroyWindow(ad)

# %%
# yeniden boyutlandırma
# src: Boyutlandırılacak resim (NumPy dizisi).
# dsize: Hedef boyut, (GENİŞLİK, YÜKSEKLİK) şeklinde ters verilir. 
# fx, fy: Genişlik ve yükseklik için ölçek çarpanı. Bunları kullanacaksan dsize None verilir.

cropped_region_resize_fxfy = cv.resize(cropped_region, dsize=(500,500)) # 500x500 yapar görüntüyü
cropped_region_resize_dsize = cv.resize(cropped_region, dsize=None,fx=2, fy=2) # boyutu 2 katına çıkarır

pencere = ["Yontem 1", "Yontem 2"]
resimler_resize = [cropped_region_resize_fxfy, cropped_region_resize_dsize]

print(f"Dsize : {cropped_region_resize_dsize.shape}")
print(f"Fx ve Fy : {cropped_region_resize_fxfy.shape}")

for ad, resim in zip(pencere,resimler_resize):
    cv.imshow(ad,resim)
    cv.waitKey(3000)
    cv.destroyWindow(ad)
# interpolation: Bir resmi büyütürken ya da küçültürken, orijinalde karşılığı olmayan yeni piksellerin değerini çevredeki mevcut piksellerden tahmin etme işlemidir.
# Örneğin resmi 2 katına büyütürsen aradaki boşluklara gelecek piksellerin renkleri komşu piksellere bakılarak hesaplanır
# cv.INTER_NEAREST	       En hızlı, kaba. Piksel sanatı ve maske gibi değerlerin karışmaması gereken yerler
# cv.INTER_LINEAR	       Varsayılan. Genel kullanım büyütme
# cv.INTER_CUBIC	       Büyütmede daha kaliteli daha yavaş
# cv.INTER_AREA	           Küçültmede en iyi sonuç
# cv.INTER_LANCZOS4	       En yüksek kalite, en yavaş


# %%
# Döndürme
kizilelma_flipped_horz = cv.flip(kizilelma, 1)
kizilelma_flipped_vert = cv.flip(kizilelma, 0)
kizilelma_flipped_both = cv.flip(kizilelma, -1)

plt.figure(figsize=[20,10])
plt.subplot(141); plt.imshow(kizilelma); plt.title("Orijinal")
plt.subplot(142); plt.imshow(kizilelma_flipped_horz); plt.title("Yatay Eksende")
plt.subplot(143); plt.imshow(kizilelma_flipped_vert); plt.title("Dikey Eksende")
plt.subplot(144); plt.imshow(kizilelma_flipped_both); plt.title("Her İki Eksende")
# %%
# Döndürme işleminde kendimiz de açı verebiliriz
# getrotationmatrix ile rotasyonu alınmış matrix elde edilir sonrasında warpAffine ile resim çevrilir.

# yukseklik, genislik = img.shape[:2]

# merkez = (genislik // 2, yukseklik // 2)
# M = cv.getRotationMatrix2D(merkez, 45, 1.0)    # (merkez, açı, ölçek)
# dondurulmus = cv.warpAffine(img, M, (genislik, yukseklik))