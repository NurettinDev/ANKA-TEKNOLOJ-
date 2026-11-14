#sayı tahmini oyunu
import random
random_number=random.randint(1,100) #1 le 100 arasında rastgele bir tam sayı
remaining_attempts=5 #5 deneme hakkı atndı
score=100 #başlangıç puanı
attempt_count=0 #deneme sayısı
print("Guess a number between 1 and 100")
print(f"Your starting score:{score}")

while(remaining_attempts>0):
    guess=int(input("Your guess:"))
    if(guess<1 or guess>100):
        print("Please! Enter a number between 1 and 100")
        continue
    attempt_count+=1
    if(guess==random_number):
        print(f"congratulations! You guessed the number correctly on your {attempt_count}.attempt")
        print(f"Your total score:{score}")
        break
    elif(guess<random_number):
        print("Try a larger number")
    else:
        print("Try a smaller number")
    remaining_attempts-=1
    score-=20
    if(remaining_attempts>0):
        print(f"Remaing attempts:{remaining_attempts}")
        print(f"Current score:{score}")
    else:
        print("Unfortunately! You ran out of attempts!")
        print(f"Your total score:{score},\n answer:{random_number}")
