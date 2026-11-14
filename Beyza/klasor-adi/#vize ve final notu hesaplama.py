#vize ve final notu hesaplama
midterm=float(input("Enter the midterm grade:"))
final=float(input("Enter the final exam grade:"))
average=(midterm*0.4)+(final*0.6)

if(average>=90):
    letter_grade="AA"
elif(average>=85):
    letter_grade="BA"
elif(average>=80):
    letter_grade="BB"
elif(average>=75):
    letter_grade="CB"
elif(average>=70):
    letter_grade="CC"
elif(average>=65):
    letter_grade="DC"
elif(average>=60):
    letter_grade="DD"
elif(average>=50):
    letter_grade="FD"
else:
    letter_grade="FF"

print(f"Your avarege:{average:.1f}")
print(f"Your letter grade:{letter_grade}")
