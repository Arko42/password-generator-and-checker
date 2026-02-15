import secrets
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    character_pool = ""

    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    # fallback if user deselects all
    if not character_pool:
        character_pool = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(secrets.choice(character_pool) for _ in range(length))
    return password
