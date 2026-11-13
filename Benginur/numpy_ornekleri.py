import numpy as np

# 1. Dizi Oluşturma ve Temel Özellikler
print("--- 1. Dizi Oluşturma ---")
a = np.array([1, 2, 3, 4, 5])
b = np.zeros((3, 3), dtype=int)  # 3x3 sıfır matrisi
c = np.arange(10, 50, 5)        # 10'dan 50'ye kadar 5'er artan dizi

print("Tek boyutlu dizi (a):", a)
print("Dizinin boyutu (ndim):", a.ndim)
print("Dizinin şekli (shape):", c.shape)
print("Veri tipi (dtype):", a.dtype)


# 2. İndeksleme ve Dilimleme
print("\n--- 2. İndeksleme ve Dilimleme ---")
matris = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])

print("2. satır, 1. sütun elemanı:", matris[1, 0])
print("Tüm satırlar, 2. sütun:", matris[:, 1])
print("Alt matris (ilk 2 satır, son 2 sütun):\n", matris[:2, 1:])

# Koşullu filtreleme 
kosul = matris > 5
print("5'ten büyük elemanlar:", matris[kosul])
# Tek satırda da yazılabilir: matris[matris > 5]


# 3. Matematiksel İşlemler ve Broadcasting
print("\n--- 3. Matematiksel İşlemler ---")
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print("Element-wise toplama (x + y):", x + y)
print("Skaler ile çarpım (x * 3):", x * 3)
print("Matris Çarpımı (Dot Product):", np.dot(x, y)) # veya x @ y


# 4. İstatistiksel Fonksiyonlar
print("\n--- 4. İstatistiksel Fonksiyonlar ---")
veri = np.array([[10, 20, 30], 
                 [40, 50, 60]])

print("Tüm elemanların toplamı:", np.sum(veri))
print("Genel ortalama:", np.mean(veri))
print("Sütun bazında ortalama (axis=0):", np.mean(veri, axis=0))
print("Satır bazında maksimum değerler (axis=1):", np.max(veri, axis=1))


# 5. Şekil Değiştirme (Reshape) ve Transpoz
print("\n--- 5. Reshape ve Transpoz ---")
duz_dizi = np.arange(12)
boyutlu = duz_dizi.reshape((3, 4))
print("3x4 Matris hali:\n", boyutlu)

print("Matrisin transpozu (.T):\n", boyutlu.T)
