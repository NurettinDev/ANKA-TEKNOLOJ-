import cv2 as cv
import sys 

# s = 0 cihazdaki default olan kameraya erişir eğer harici kamera varsa indeksi artırarak ona erişebiliriz
s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

source = cv.VideoCapture(s)
print(source.isOpened())

win_name = "Kamera"
cv.namedWindow(win_name, cv.WINDOW_NORMAL)

# ESC ye basana kadar devam eder, 1 milisaniye bekle basılan tuşun kodunu ver, basılmadıysa -1 döner
# ord("q") q tuşunu ascii kodunu verir bu şekilde denklik kontrolü yaparak farklı tuşlara farklı görevler atanabilir.
while cv.waitKey(1) != 27: 
    has_frame, frame = source.read()
    if not has_frame:
        break
    cv.imshow(win_name, frame)

source.release()
cv.destroyWindow(win_name)
