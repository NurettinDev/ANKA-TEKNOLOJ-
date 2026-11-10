max_capacity = 9
#Paket kimliği(index 0), öncelik (1-5)(index 1), boyut (pozitif tam sayı, KB)(index 2), bütünlük durumu (doğrulandı 1/doğrulanmadı 0) (index 3)
#Küçük indeks ilk gönderilen büyük indeks daha sonra gönderilen şeklinde belirlendi.
packages = [["P1", 5, 6, 1], ["P2", 4, 5, 1], ["P3", 3, 3, 1], ["P4", 2, 2, 0]]

unverified_ones = []
too_big_ones = []

#İlk filtre
for row in packages:
	if row[3] == 0:
		packages.remove(row)
		unverified_ones.append(row[0])
	if row[2] > max_capacity:
		try:
			packages.remove(row[0])
		except ValueError:
			pass
		too_big_ones.append(row[0])

item_amount = len(packages)
temp_size1 = 0
temp_priority1 = 0 

matrix = [[0 for col in range(max_capacity)] for row in range(item_amount)]

def isUpperHigher(r, c, S, matrix):
	if r == 1:
		return -1
	if matrix[r-2][c-1] >= S:
		return 1
	else:
		return 0

for r in range(1, item_amount+1):
	for c in range(1, max_capacity+1):
		temp_size1 = packages[r-1][2]
		temp_priority1 = packages[r-1][1]
		size_dif = c - temp_size1
		if (size_dif) == 0:
			if isUpperHigher(r, c, temp_priority1, matrix) == 1:
				matrix[r-1][c-1] = matrix[r-2][c-1]
			elif isUpperHigher(r, c, temp_priority1, matrix) == 0:
				matrix[r-1][c-1] = temp_priority1
			else:
				matrix[r-1][c-1] = temp_priority1
			continue
		elif (size_dif) > 0:
			S=0
			if r!=1:
				S = temp_priority1 + matrix[r-2][ size_dif-1]
			else:
				matrix[r-1][c-1] = temp_priority1

			if isUpperHigher(r, c, S, matrix) == 1:
				matrix[r-1][c-1] = matrix[r-2][c-1]
			elif isUpperHigher(r, c, S, matrix) == 0:
				matrix[r-1][c-1] = S
			continue    
		else:
			if r == 1:
				matrix[r-1][c-1] = 0
			else:
				matrix[r-1][c-1] = matrix[r-2][c-1]
			continue

for rs in matrix:
	print(rs)

selected_items = []
unselected_items = []
#Backtracking(geri izleme ve paketleri ortaya çıkarma)
c = max_capacity
for r in range(item_amount, 0, -1):
	if r==1:
		selected_items.append(packages[r-1][0])
		continue
	if matrix[r-1][c-1] == matrix[r-2][c-1]:
		unselected_items.append(packages[r-1][0])
		continue
	else:
		selected_items.append(packages[r-1][0])
		c = max_capacity-packages[r-1][2]

print("Kabul Edilenler: ", selected_items)
print("Bekleyenler: ", unselected_items)
print("Reddedilenler---")
print("	Doğrulanmayanlar: ", unverified_ones)
print("	Kapasiteyi tek başına aşanlar: ", too_big_ones)
