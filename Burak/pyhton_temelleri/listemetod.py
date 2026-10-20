

names=["Ali","Yağmur","Hakan","Deniz"]
years=[1990,1995,2000,2005]

names=names+["Cenk"]
print(names)
names=["Sena"]+names
print(names)
find=names.index("Deniz")
print(find)
result="Ali" in names
print(result)

names.reverse()
print(names)
names.sort()
print(names)
years.sort()
print(years)
str="Chevrolet,Dacia"
str=str.split(",")
print(str)
result=min(years)
print(result)
result=max(years)
print(result)
del years[:]
print(years)