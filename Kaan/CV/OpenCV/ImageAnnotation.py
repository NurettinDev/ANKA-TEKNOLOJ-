#%%
import cv2 as cv
import matplotlib.pyplot as plt
#%%
st_bgr = cv.imread(r"Pictures\soloturk.jpg", cv.IMREAD_COLOR)
st = cv.cvtColor(st_bgr, cv.COLOR_BGR2RGB)
plt.imshow(st)

#%%
# Resim üzerine çizgi çizme

# img: Çizgi çizilecek resim. Çizim orijinal dizinin üzerine yapılır ve aynı dizi geri döner.
# pt1: Başlangıç noktası, (x, y) sırasıyla. Tuple olmalı, tam sayı içermeli.
# pt2: Bitiş noktası, (x, y).
# color: Renk, BGR sırasıyla. Gri tonlamalı resimde tek değer verilir.
# thickness: Kalınlık (piksel). Varsayılan 1.
# lineType: Çizgi tipi.
# cv.LINE_8: Varsayılan, pürüzlü kenarlı.
# cv.LINE_AA: Kenarları yumuşatır, daha düzgün görünür, biraz yavaş.

# Noktalar (x, y) yani (sütun, satır) sırasındadır. NumPy’daki [satır, sütun] sırasının tersidir.
st_cizgi = st.copy()
cv.line(st_cizgi, (100,300), (450,300), color = (255,0,0), thickness=3, lineType=cv.LINE_AA)
plt.imshow(st_cizgi)
# %%
# Resim üzerine daire çizme

# img: Çizilecek resim. Çizim orijinal dizinin üzerine yapılır.
# center: Merkez noktası, (x, y) sırasıyla. Tam sayı tuple.
# radius: Yarıçap (piksel), tam sayı.
# color: BGR sırasıyla renk.
# thickness: Çizgi kalınlığı. -1 verirsen daire içi dolu çizilir.
# lineType: cv.LINE_8 (varsayılan) ya da kenarları yumuşatan cv.LINE_AA.

st_daire = st.copy()
cv.circle(st_daire, (260,170), 190, color = (0,0,255), thickness= 2, lineType=cv.LINE_8 )
cv.circle(st_daire, (260,170), 10, color = (255,0,0), thickness= -1, lineType=cv.LINE_8 )
plt.imshow(st_daire)
# %%
# Resim üzerine dikdörtgen çizme

# img: Çizilecek resim. Çizim orijinal dizinin üzerine yapılır.
# pt1: Sol üst köşe, (x, y) sırasıyla.
# pt2: Sağ alt köşe, (x, y). 
st_ddgn = st.copy()
cv.rectangle(st_ddgn, (200,150), (300,250), color = (0,255,0), thickness= 2)
plt.imshow(st_ddgn)

# %%
# Resim üzerine yazı yazma
 
# img: Yazının yazılacağı resim. Orijinal dizinin üzerine yazılır.
# text: Yazılacak metin (string).
# org: Metnin sol alt köşesi, (x, y) sırasıyla.
# fontFace: Yazı tipi, örneğin cv.FONT_HERSHEY_SIMPLEX, cv.FONT_HERSHEY_COMPLEX, cv.FONT_HERSHEY_SCRIPT_SIMPLEX.
# fontScale: Yazı boyutu çarpanı (float olabilir, ör. 1.5).
# color: BGR sırasıyla renk.
# thickness: Çizgi kalınlığı.
# lineType: cv.LINE_8 (varsayılan) ya da cv.LINE_AA (yumuşak kenar).
# bottomLeftOrigin: True olursa metin dikey olarak ters çizilir. Genelde dokunulmaz. 

st_text = st.copy()
cv.putText(st_text, 
           "SOLOTÜRK", 
           (100,350), 
           fontFace= cv.FONT_HERSHEY_COMPLEX,
           fontScale= 1.5,
           color=(255,0,0),
           thickness=2,
           lineType= cv.LINE_AA,)

plt.imshow(st_text)
# %%
