print('\n')

website = 'http://www.example.com'
course = 'Python Programming: Baştan sona python programlama rehberi (40 saat)'

lengthCourse = len(course)
print('Course length:', lengthCourse)
print(course[-15:])
print(course[:15])
print(course[::-1])

lengthWebsite = len(website)
print('Website length:', lengthWebsite)
print(website[7:10])
print(website[-3:])

name = 'Mahmut'
surname = 'Haydar'
fullName = name + ' ' + surname
age = 22
job = 'Computer Engineer'
print('My full name is ' + fullName + ' and I am ' + str(age) + ' years old. I work as a ' + job + '.')
print('My full name is {} {} and I am {} years old. I work as a {}.'.format(name, surname, age, job))
print(f'My full name is {name} {surname} and I am {age} years old. I work as a {job}.')

hello = 'Hello, world!'
hello = hello[0:7] + 'W' + hello[-5:]
print(hello)

abc = 'abc'
print(abc * 3)

print('\n')
