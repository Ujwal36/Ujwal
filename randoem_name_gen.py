# Provide me Random Capitalized Name Generator

import random

def generate_random_name(length=10):
    name = ""
    for _ in range(length):
        
        number = random.randint(ord('a'), ord('z'))
        name += chr(number)

    return name.capitalize()

# Generate a random name of length 10
random_name = generate_random_name(10)
print(random_name)
