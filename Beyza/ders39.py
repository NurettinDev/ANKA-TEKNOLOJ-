''''
import copy
list1=[[1,2],[3,4]]
new_list=copy.deepcopy(list1)#iç içe liste varsa copy kütüpün. den deepcopy çağrılır kopyalamak için

new_list[0][0]=70
new_list[0][1]=19
new_list[1][1]=34
print(list1)
print(new_list)
'''
fruit=["strawberry","grape","melon","pineapple","banana","melon"]
#fruit.remove("strawberry")#istediğin veriyi listeden kaldırır
#fruit.pop()#son ögesini kaldırır
#del fruit#böyle listeyi siler ama sonuna [3] koyarsak mesela 3. indextekini siler
#fruit.clear()#listenin içini boşaltır
# result=fruit.index("grape")#grape in index numarasını söyler
# result2=fruit.count("melon")# kaç kez melon varsa onu söyler

# print(result2)
#fruit.sort(key=str.lower)#küçükten büyüğe sıralama 
# fruit.sort(reverse=True)#küçükten büyüğe sıralamayı tersine çevirdi

'''
def mySort(x):
    return abs(x-20)#abs mutlak değere almaya yarar
fruit=["strawberry","grape","melon","pineapple","banana","melon"]
myNumbers=[70,19,29,39,48,7,12]
fruit.sort()
myNumbers.sort(key=mySort)#20 sayısına yakın olanlara göre sıraladı
print(myNumbers)
'''
fruit.reverse()#sırayı tersine çevirir
print(fruit)