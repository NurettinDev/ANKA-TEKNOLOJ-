print('\n')

arabalar = ['BMW', 'Mercedes', 'Opel', 'Mazda']

print(len(arabalar)) 
print('\n')

print(arabalar[0])
print(arabalar[3])
print('\n')

arabalar[-1] = 'Toyota'
print(arabalar)
print('\n')

result_1 = 'Mercedes' in arabalar
print(result_1)
print('\n')

print(arabalar[-2])
print('\n')

print(arabalar[0:3])
print('\n')

print(arabalar[:3])    
print('\n')

print(arabalar[2:])
print('\n')

print(arabalar[-2:])
print('\n')

arabalar[-2:] = ['Toyota', 'Renault']
print(arabalar)
print('\n')

arabalar += ['Audi', 'Nissan']
print(arabalar)
print('\n')

print(arabalar)
print('\n')

del arabalar[-1]
print(arabalar)
print('\n')

print(arabalar[::-1])
print('\n')

student1 = ['Ahmet', 'Yılmaz', 2001, [80, 90, 70]]
student2 = ['Mehmet', 'Demir', 2002, [90, 80, 70]]
student3 = ['Ayşe', 'Kara', 2000, [70, 80, 90]]

print(student1[0], student1[1], student1[2], student1[3])
print(student2[0], student2[1], student2[2], student2[3])
print(student3[0], student3[1], student3[2], student3[3])   
print(student1[3][0])
print('\n')

result_1 = f'{student1[0]} {student1[1]} {2026 - student1[2]} yaşında ve not ortalaması {student1[3][0] + student1[3][1] + student1[3][2] / 3}'
print(result_1)
print('\n')