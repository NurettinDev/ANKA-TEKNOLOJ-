#for döngüsü
'''
fruits=["grape","orange","strawberry","cherry"]
for item in fruits:#dizideki ifadeleri item karakterine boşalttı
    print(item)
'''
fruits=["grape","orange","strawberry","cherry"]
i=0
for item in fruits:#dizideki ifadeleri item karakterine boşalttı
    if(item=="orange"):
        continue
    print(i,".index=",item)
    i+=1
