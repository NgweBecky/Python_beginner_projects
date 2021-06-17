#a rock paper scissor game where the computer randomly generates
#an answer while the user inputs an answer and both are compared
#I made the game a simple one as in either your input is wrong or correct

import string
from random import *
#please any further modification of the game is welcomed  

player = input("Enter a code not above 5 words:")
string_list = string.ascii_letters + string.digits + string.punctuation
computer = "".join(choice(string_list) for i in range(randint(1, 6)))
while len(player) <= 5:
    if player == computer:
        print("correct answer")
    else:
        raise ValueError
print(computer)
