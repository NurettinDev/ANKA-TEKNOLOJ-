import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import sys
# Akış
# Sabitler: PREVIEW, BLUR, FEATURES, CANNY filtreleri sayıyla temsil eder. 
# img_filter hangi filtrenin aktif olduğunu tutar.

# Kamera açılır: cv.VideoCapture(s), s = 0 varsayılan kameradır.
# Döngü (while alive):
# source.read() bir kare okur okunamazsa döngü biter.
# cv.flip(frame, 1) kareyi yatay çevirir (ayna görüntüsü).
# img_filter değerine göre kareye filtre uygulanır ve result’a yazılır.
# cv.imshow sonucu gösterir.
# cv.waitKey(1) tuşu okur: q/ESC çıkış, c Canny, b Blur, f Features, p Preview.

# Fonksiyonlar
# cv.blur(frame, (13, 13))
# Ortalama filtresidir. 
# Her pikseli, çevresindeki 13x13 bölgenin ortalamasıyla değiştirir. 
# Kernel büyüdükçe bulanıklık artar. 
# Kernel boyutu tek sayı olmak zorunda değildir ama merkezlenmesi için genelde tek seçilir.

# cv.Canny(frame, 100, 200)
# Kenar bulur. Çıktı siyah zeminde beyaz kenarlardan oluşan tek kanallı resimdir.
# threshold1 (alt eşik): Gradyanı bunun altında kalan pikseller kenar sayılmaz.
# threshold2 (üst eşik): Bunun üstündeki pikseller kesin kenardır.
# İkisinin arasındakiler yalnızca kesin bir kenara bağlıysa kenar kabul edilir (hysteresis).
# Oran genelde 1:2 ya da 1:3 seçilir. 
# Renkli kareyi doğrudan vermek yerine gri yapıp vermek daha güvenlidir: cv.Canny(cv.cvtColor(frame, cv.COLOR_BGR2GRAY), 100, 200).

# cv.goodFeaturesToTrack ve feature_params
# Shi-Tomasi Yöntemi
# Her piksel için çevresindeki bölgenin parlaklık değişimine (gradyan) bakar.
# Değişimin iki yönde de güçlü olduğu pikselleri “köşe” olarak puanlar.
# qualityLevel ile zayıf puanlıları eler.
# Puana göre sıralar, minDistance içinde birbirine yakın olanlardan yalnızca en iyisini bırakır.
# En fazla maxCorners kadarını döndürür.
# maxCorners: En fazla kaç köşe döndürüleceği (500).
# qualityLevel: En iyi köşenin kalitesinin bu oranından düşük olanlar elenir ve kenar olarak işaretlenmez. 
# 0.2 ise en iyinin %20'sinin altı atılır. Artırırsan köşe sayısı azalır.
# minDistance: İki köşe arasındaki en az piksel mesafesi (15). Köşelerin üst üste yığılmasını önler.
# blockSize: Köşe hesabında her piksel için bakılan komşuluk boyutu (9).

PREVIEW = 0     # Preview mode
BLUR = 1        # Blurring Filter
FEATURES = 2    # Corner Feature Detector
CANNY = 3       # Canny Edge Detector

feature_params = dict(maxCorners = 500,
                      qualityLevel = 0.2,
                      minDistance = 15,
                      blockSize = 9)

s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

img_filter = PREVIEW
alive = True

win_name = "Camera Filters"
cv.namedWindow(win_name, cv.WINDOW_NORMAL)
result = None

source = cv.VideoCapture(s)

while alive:
    ret, frame = source.read()
    if not ret:
        break

    frame = cv.flip(frame, 1)

    if img_filter == PREVIEW:
        result = frame
    elif img_filter == BLUR:
        result = cv.blur(frame, (13,13))
    elif img_filter == CANNY:
        result = cv.Canny(frame, 100,200)
    elif img_filter == FEATURES:
        result = frame
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        corners = cv.goodFeaturesToTrack(frame_gray, **feature_params)
        if corners is not None:
            for x,y in np.float32(corners).reshape(-1,2):
                cv.circle(result, (int(x),int(y)), 3, (0,255,0), -1)

    cv.imshow(win_name, result)

    key = cv.waitKey(1)
    if key == ord("q") or key == 27:
        alive=False
    elif key == ord("c"):
        img_filter = CANNY
    elif key == ord("b"):
        img_filter = BLUR
    elif key == ord("f"):
        img_filter = FEATURES
    elif key == ord("p"):
        img_filter = PREVIEW

source.release()
cv.destroyAllWindows()