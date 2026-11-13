#iç içe döngüler
'''
adjectives=["red","big","tasty"]
fruits=["grape","strawberry","cherry"]
for outher in adjectives:
    for inner in fruits:
        print(outher,inner)
     '''
'''
myNumbers=[
    [29,21],
    [12,23],
    [90,91]
]
for item in myNumbers:
    print(f"{item}")
    '''
fruits=["grape","orange","melon","cherry"]
for index,item in enumerate(fruits):
    print(f"{index}-{item}")
names=["fehmi","beyza"]
ages=[34,20]
for name,age in zip(names,ages):#listeleri birleştiriyor
    print(f"{name} is {age} years old")