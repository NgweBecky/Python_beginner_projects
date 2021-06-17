import random

guess_count = 0
guess_limit = 3
computer = random.randint(0,20)

while guess_count < guess_limit:
    user = int(input("Enter your guess: "))

    if user == computer:
        print("Correct guess")
    
    elif user < computer and user >= 0:
        print("Guess is low")
    
    elif user > computer and user <= 21:
        print("Guess is high")
    
    else:
        print("Guess is out of range")
    guess_count += 1

print(computer)
print(user)