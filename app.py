# collect user preferences
# - lenght
# - should countain uppercase
# - should countain special
# - should countain digits

#get all available characzers 
# randomly pick characzers up to the length
# ensure we have at lest one of each character type
# ensure length is valid

import random
import string

def generate_password():
    lenght = int(input("Enter the desired password lenght: ").strip())
    include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower()
    include_special = input("Include special letters? (y/n): ").strip().lower()
    include_digits = input("Include digits letters? (y/n): ").strip().lower()

    if lenght < 6:
        print("Password lenght must be at least 6 characters!")
        return
    
    lower = string.ascii_lowercase
    print(lower)

generate_password()