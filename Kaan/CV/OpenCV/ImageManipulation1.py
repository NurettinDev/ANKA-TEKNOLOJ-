#%%
import sys
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(threshold=sys.maxsize) # çıktılar tam haliyle verilir
#%%
# resmi grayscale olarak okur
cb_img = cv.imread(r"Pictures\chessboard.png", 0)
print(cb_img) # 2 boyutlu diziyi verir. 8bit renk aralığında olduğu için değerler 0-255 arasında gelir

#%%
# resim boyutu
print(f"Image size : {cb_img.shape}")

# resim data type
print(f"Image size : {cb_img.dtype}")

#%%
# yüklü resmi gösterme
plt.imshow(cb_img)

# imshow() resim grayscale olsa bile matplotlib farklı bir colormap kullandığı için mor sarı çıkıyor
# bunun önüne geçmek için cmap parametresini ayarlamak lazım
plt.imshow(cb_img, cmap="gray")

# %%
# 1 vererek renkli resim olarak okuttuk
baykar_renkli = cv.imread(r"Pictures\Baykar.png", 1)
print(f"Image size : {baykar_renkli.shape}") # (480, 416, 3) 3 kanal
print(f"Image data type : {baykar_renkli.dtype}")
plt.imshow(baykar_renkli)

#%%
# opencv rgb leri bgr olarak okuduğu için maviler kırmızı olarak gözüküyor
# o yüzden kanalları ters çevirmemiz lazım 
# : (birinci): tüm satırlar (yükseklik)
# : (ikinci): tüm sütunlar (genişlik)
# ::-1 (üçüncü): kanalları sondan başa doğru al
baykar_renkli_reversed = baykar_renkli[:,:, ::-1]
plt.imshow(baykar_renkli_reversed)
# %%
# renkli resim olarak okuyoruz ve split ile kanallarına ayrıştırıyoruz
resim_split = cv.imread(r"Pictures\RB22 Reveal.jpeg", cv.IMREAD_COLOR)
b,g,r = cv.split(resim_split)

# ayrılmış kanalları gösterelim
plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(r); plt.title("Kırmızı Kanal")
plt.subplot(142);plt.imshow(g); plt.title("Yeşil Kanal")
plt.subplot(143);plt.imshow(b); plt.title("Mavi Kanal")

# ayrık resmi birleştirelim
resim_merge = cv.merge((b,g,r))
plt.subplot(144);plt.imshow(resim_merge[:, :, ::-1]);plt.title("Birleşik Resim")
# %%
# renk kanallarını değiştirmek için sürekli dizi işlemleri yapmamıza gerek yok
# cvtcolor() metodu ile istediğimiz resmi ilk parametre istediğimiz kanalı ikinci parametre olarak verip istediğmiz şekilde alabiliriz
resim_KanalDegisim = cv.cvtColor(resim_split, cv.COLOR_BGR2RGB)
plt.imshow(resim_KanalDegisim) # normalde bozuk gelmesi gereken resim düzgün geliyor
# %%
resim_hsv = cv.cvtColor(resim_split, cv.COLOR_BGR2HSV)
h,s,v = cv.split(resim_hsv)

# ayrılmış kanalları gösterelim
plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(h); plt.title("Hue (Renk Tonu) Kanalı")
plt.subplot(142);plt.imshow(s); plt.title("Saturation (Doygunluk) Kanalı")
plt.subplot(143);plt.imshow(v); plt.title("Value (Parlaklık) Kanalı")
plt.subplot(144);plt.imshow(resim_hsv);plt.title("HSV")

# %%
h_yeni = h + 15
resim_modifiedh = cv.merge((h_yeni, s, v))
resim_modifiedh_rgb = cv.cvtColor(resim_modifiedh, cv.COLOR_HSV2RGB)

plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(h_yeni); plt.title("Yeni Hue (Renk Tonu) Kanalı")
plt.subplot(142);plt.imshow(s); plt.title("Saturation (Doygunluk) Kanalı")
plt.subplot(143);plt.imshow(v); plt.title("Value (Parlaklık) Kanalı")
plt.subplot(144);plt.imshow(resim_modifiedh_rgb);plt.title("Modifiye Edilmiş HSV Resminin RGB Kanallısı")

# %%
# resimleri kaydetmke için cv.imwrite() metodu kullanılır
cv.imwrite(r"Pictures\modified_rb22.jpeg", resim_modifiedh_rgb)
# %%
# matplotlib in imshow u ile cv nin imshow metodu farklı kullanılır
# cv için bir window oluşturulması gerekir.
# İsimler için ya direkt string ay da değişkenler ile verilmelidir
# window1 = cv.namedWindow("Window") X YANLIŞ
pencere = "Kaan"
cv.namedWindow(pencere)
cv.imshow(pencere, baykar_renkli)
cv.waitKey(3000) # 3sn göserir, 0 olursa bir tuşa basılana kadar açık aklır
cv.destroyWindow(pencere)
# %%
