import numpy as np 

a = np.array([[1, 2, 3], [4, 5, 6]])
np.array([1, 2.5])      # [1. 2.5], hepsi float
np.array([1, "a"])      # hepsi string olur
a.astype(float)         # tip değiştirme

print(a.shape)    # (2, 3)
print(a.ndim)     # 2
print(a.size)     # 6
print(a.dtype)    # int64

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a + 10)                   # her elemana eklenir
print(a + np.array([1, 0, 1]))   # her satıra eklenir

np.zeros((2, 3))
np.full((2, 2), 7)          # 7 lerden oluşan 2x2 matris
np.eye(3)                   # birim matris
np.linspace(0, 1, 5)        # 0-1 arası 5 eşit aralıklı sayı

# Eleman bazlı ve matris çarpımı farklıdır
# a * b          eleman eleman çarpım
# a @ b          matris çarpımı (np.dot ile aynı)

# List her tipten elemanı tutan genel bir yapıdır. 
# NumPy dizisi aynı tipteki sayısal verileri tutan matematiksel işlemler için oluşturulmuş yapıdır. 
my_list1 = [10,20,30,40]
my_list2 = [50,60,70,80]
my_numpy_array1 = np.array(my_list1) #listeyi numpy dizisi yapar
my_numpy_array2 = np.array(my_list2) #listeyi numpy dizisi yapar
print( f"Dizi toplam : {my_numpy_array1 + my_numpy_array2}")
print( f"Dizi bölme  : {my_numpy_array1 / my_numpy_array2}")
print(np.arange(0,10)) # 0-9 arası dizi oluşturma

# Random
print(np.random.randn(4,4))
new_array = np.random.randint(1,300,5) #1-299 arası 5 sayı
print(np.ones((4,3)))
print(new_array[new_array>23]) # diziddeki 23 ten büyükleri yazdırır

# transpoze and reshape
matrix_array = np.array([[10,20], [30, 40], [50,60]])
print(f"Transpoze :\n{matrix_array.transpose()}") # satır sütun tersler
print(f"Reshape   :\n{matrix_array.reshape(1,6)}") # tek sıraya düşürdük

datas = np.array([10,20,30,40,50,60])
print (f"Mean : {datas.mean()} \nStandart Sapma = {datas.std()}")