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
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower()
    include_special = input("Include special letters? (yes/no): ").strip().lower()
    include_digits = input("Include digits letters? (yes/no): ").strip().lower()

    if lenght < 4:
        print("Password lenght must be at least 4 characters!")
        return
    
    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""
    all_characters = lower + uppercase + special + digits

    required_character = []
    if include_uppercase =="yes":
        required_character.append(random.choice(uppercase))
    if include_digits == "yes":
        required_character.append(random.choice(digits))
    if include_special == "yes":
        required_character.append(random.choice(special))

    remaining_lenght = lenght - len(required_character)
    password = required_character

    for _ in range(remaining_lenght):
        character = random.choice(all_characters)
        password.append(character)

    random.shuffle(password)

    str_password = "".join(password)
    return str_password


password =  generate_password()
print(password)