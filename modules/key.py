"""
##### Key Module v0.0.1
"""

def generate(characters, mode):
    import string
    import random
    import secrets
    
    if characters < 12:
        raise ValueError("Password length should be at least 12 characters.")
    
    if mode == "strong":
        letters = string.ascii_letters
        digits = string.digits
        symbols = "!@#$%^&*()_+[]{}|;:,.<>?/=-"
        character_sets = [letters, digits, symbols]
    elif mode == "mid":
        letters = string.ascii_letters
        digits = string.digits
        character_sets = [letters, digits]
    elif mode == "weak":
        letters = string.ascii_lowercase
        character_sets = [letters]
    else:
        raise ValueError("Invalid mode. Use 'strong', 'mid', or 'weak'.")

    password = ""

    for char_set in character_sets:
        password += secrets.choice(char_set)

    for _ in range(characters - len(character_sets)):
        char_set = random.choice(character_sets)
        password += secrets.choice(char_set)

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password