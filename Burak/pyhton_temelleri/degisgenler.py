
customer1_Name, customer1_Surname, = ('John', 'Doe')
customer1_FullName = customer1_Name + customer1_Surname
customer1_sex = False #male
customer1_Tc = "12345678901"
customer1_birthDate = "01/01/1990" 
customer1_adress = "123 Main St, Anytown, USA"
customer1_age = 2026 - int(customer1_birthDate.split("/")[-1])  # Calculate age based on birth year

if customer1_sex:
    print(f"Customer 1: {customer1_FullName}, Sex: Male, TC: {customer1_Tc}, Birth Date: {customer1_birthDate}, Address: {customer1_adress}, Age: {customer1_age}")
else:{
    print(f"Customer 1: {customer1_FullName}, Sex: Female, TC: {customer1_Tc}, Birth Date: {customer1_birthDate}, Address: {customer1_adress}, Age: {customer1_age}") 
}
order1='110 TL'
oreder2='1100.5 TL'
order3='356.95 TL'
toplam=int(order1.split()[0]) + float(oreder2.split()[0]) + float(order3.split()[0])
print(f"Toplam: {toplam} TL")