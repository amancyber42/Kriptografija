import string
from colorama import Fore, init

init()

# Funkcija za ivođenje  enkripcije
def affine_encription(plaintext, a, b):
    alphabet = string.ascii_uppercase
    m = len(alphabet)
    ciphertext = ''

    for char in plaintext:
        if char in alphabet:
            p = alphabet.index(char)
            c = (a * p + b) % m
            ciphertext += alphabet[c]

        else:
            ciphertext += char

    return ciphertext

# Definirati otvoreni text i ključne komponente
plaintext = input(f"{Fore.GREEN}[?] Unesite tekst za šifriranje: ")
a = 3
b = 10
encrypted_text = affine_encription(plaintext, a, b)
print(f"{Fore.MAGENTA}[+] Plaintext: {plaintext}")
print(f"{Fore.GREEN}[+] Šifrirani tekst: {encrypted_text}")
    
