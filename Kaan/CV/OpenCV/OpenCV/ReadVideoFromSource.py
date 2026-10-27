import cv2 as cv
import sys
import matplotlib.pyplot as plt
from IPython.display import HTML

source = "Videos//Megamind.avi" # source = 0 ile kameraya erişilebilir

cap = cv.VideoCapture(source)

if(cap.isOpened()):
    print("Opened")
else:
    print("Error")

# sadece 1 frame okuyup görüntülemek için
ret, frame = cap.read()
plt.imshow(frame[..., ::-1]) # dizinin son eksenini (renk kanalları) ters çevirir
plt.show()

# Videoyu oynatmak için
# HTML("""
# <video width=1024 controls>
# <source src= "Videos//başkavideo.mp4" type="video/mp4">
# </video>
# """)

# OpenCV ile Video Yazma
# filename: Kaydedilecek dosyanın yolu ve adı ("cikti.mp4"). Uzantı, fourcc ile uyumlu olmalı.
# fourcc: Video codec’inin 4 harfli kodu. cv.VideoWriter_fourcc(*"mp4v") ile oluşturulur.
# fps: Çıktı videosunun saniyedeki kare sayısı (ör. 30). Kaynak videoyla aynı hızda kaydetmek için cap.get(cv.CAP_PROP_FPS) kullanılır.
# frameSize: Kare boyutu, (genişlik, yükseklik) sırasıyla. Yazdığın karelerle birebir aynı olmalı.
# isColor: True renkli (3 kanallı), False gri tonlamalı kare bekler. Varsayılan True.

frame_width = int(cap.get(3)) # karenin gneişliğini alır
frame_height = int(cap.get(4)) # akrenin yüksekliğini alır

out_mp4 = cv.VideoWriter("Videos/cikti.mp4", cv.VideoWriter.fourcc(*"mp4v"),120 ,(frame_width, frame_height)) # saniyede 120 frame oynadığı için video hızlanır

while(cap.isOpened()): # video bitene kadar devam et
    ret, frame = cap.read()

    if ret:
        out_mp4.write(frame)
    else:
        print("Kayedildi")
        break

cap.release()
out_mp4.release()