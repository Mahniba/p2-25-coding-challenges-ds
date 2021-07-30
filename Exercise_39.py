# Ceasar Cipher
import string
alphabet_uppercase = string.ascii_uppercase
alphabet_lowercase = string.ascii_lowercase

def ceasar_cipher(text, key):
    result = ""
    ceasar_alphabet_upper = alphabet_uppercase[26-key: 26] + alphabet_uppercase[0: 26-key]
    ceasar_alphabet_lower = alphabet_lowercase[26-key: 26] + alphabet_lowercase[0: 26-key]

    for char in text:
        if not char.isalpha():
            result += char
        elif char.isupper():
            result += ceasar_alphabet_upper[alphabet_uppercase.find(char)]
        elif char.islower():
            result += ceasar_alphabet_lower[alphabet_lowercase.find(char)]
    return result


print(ceasar_cipher("Ceasar Cipher!", 8))