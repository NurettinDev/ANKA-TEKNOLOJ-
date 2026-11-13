#list comprehension kullanımı
fruits=["grape","orange","melon","watermelon"]

#normalde böyle kullanırız
#for item in fruits:
 #   print(item)
[print(item) for item in fruits] #kısa yol(list comprehension)
#new_list=[]
# for item in fruits:
#     if("g" in item):
#         new_list.append(item)
# print(new_list)
new_list=[item for item in fruits if("g" in item)]#kısa yol
print(new_list)