# generate a random password
import random
import string

def generate_password(length=10):
    # define the characters to use in the password
    characters = string.ascii_letters
    digits = string.digits 
    # generate a random password with both letters and digits
    password = ''.join(random.choice(characters + digits) for _ in range(length))

password =generate_password()

print(f"Generated password: {password}")


