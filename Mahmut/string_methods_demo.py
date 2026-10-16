from numpy import rint


print('\n')

website = 'http://www.example.com'
course = 'Python Programming: Baştan sona python programlama rehberi (40 saat)'
greeting = " Hello, World! "

print(greeting)
print('\n')

result_1 = greeting.strip() #sağdan ve soldan için ise srip başına r ve l harfleri kullanılır.
print(result_1) 
print('\n')

result_2 = website.strip('htp:/w.com')
print(result_2)
print('\n')

course = course.lower()
print(course)
print('\n')

course = course.upper()
print(course)   
print('\n')

website_1 = website.count('e')
print(website_1)
print('\n')

website_2 = website.count('www')
print(website_2)
print('\n')

website_3 = website.count('www', 0, 10)
print(website_3)
print('\n')

website_4 = website.startswith('www')
print(website_4)
print('\n')

website_5 = website.endswith('com')
print(website_5)
print('\n')

website_6 = website.find('www')
print(website_6)
print('\n')

website_7 = website.find('com', 0, 10)
print(website_7)
print('\n')

course_1 = course.isalpha()
print(course_1)
print('\n')

course_2 = course.isdigit()
print(course_2)
print('\n')

greeting_centered = greeting.center(50, '*')
print(greeting_centered)
print('\n')

greeting_ljust = greeting.ljust(50, '*')
print(greeting_ljust)
print('\n')

greeting_rjust = greeting.rjust(50, '*')
print(greeting_rjust)       
print('\n')

course_3 = course.replace('python', 'C++')
print(course_3)
print('\n')

course_4 = course.replace(' ', '-')
print(course_4)
print('\n')

course_5 = course.replace(' ', '-', 5)
print(course_5)
print('\n')

greering_replaced = greeting.replace('Hello', 'Hi')
print(greering_replaced)
print('\n')

course_6 = course.split(' ')
print(course_6)
print('\n') 

print(course_6[5])
print('\n')