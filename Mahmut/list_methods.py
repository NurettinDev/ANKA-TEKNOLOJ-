print('\n')

names = ["Mahmut", "Ahmet", "Mehmet", "Ayşe", "Fatma", "Ali", "Veli", "Zeynep", "Elif", "Hasan"]
year_of_birth = [2004, 2009, 1992, 1995, 1988, 1991, 1987, 1993, 1994, 1989]

names.append("Cenk")
year_of_birth.append(2000)  

names.insert(0, "Merve")
year_of_birth.insert(0, 1990)

names.insert(len(names), "Cem")
year_of_birth.insert(len(year_of_birth), 1998)

names.remove("Ali")
year_of_birth.remove(1991)

names.pop(3)
year_of_birth.pop(3)

print(names)
print(year_of_birth)
print('\n')

print(names.index("Zeynep"))
print(year_of_birth.index(1994))
print('\n')

print("Zeynep" in names)
print(1974 in year_of_birth)
print('\n')

print(list(reversed(names)))
print(list(reversed(year_of_birth)))
print('\n')

print(sorted(names))
print(sorted(year_of_birth))
print('\n')

str = 'merhaba dünya'
result = str.split()
print(result)
print('\n')

print(min(year_of_birth))
print(max(year_of_birth))
print('\n')

year_of_birth.clear()
print(year_of_birth)
print('\n')

markalar = []
marka = input("Marka giriniz: ")
markalar.append(marka)
print(markalar)
print('\n')