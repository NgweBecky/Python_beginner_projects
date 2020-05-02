import string
from random import *

character = string.ascii_letters + string.digits + string.punctuation
password = "".join(choice(character) for x in range(randint(8, 16)))

print(password)