import sys
from colorama import Fore, init

init()

def implement_caesar_cipher(message, key, decrypt=False):
    result = ""
    # Iterirati kroz svaki znak u korisničkom unosu
    for character in message:
        if character.isalpha():
            shift = key if not decrypt else -key
            if character.islower():
                result += chr(((ord(character) - ord('a') + shift) % 26) + ord('a'))
            else:
                result += chr(((ord(character) - ord('A') + shift) % 26) + ord('A'))
        else:
            result += character  # Ako nije slovo, ostavi znak nepromijenjen
    return result

# Glavni dio koda
if __name__ == "__main__":
    # Traži se od korisnika da unese tekst za šifriranje
    text_to_encrypt = input(f"{Fore.GREEN}[?] Molimo unesite svoj tekst/poruku: ")
    key = int(input(f"{Fore.GREEN}[?] Navedite duljinu smjene (0-25): "))

    # Provjeriti je li navedeni ključ u važećem rasponu (0 do 25)
    if key > 25 or key < 0:
        print(f"{Fore.RED}[!] Dužina vaše smjene trebala bi biti između 0 i 25.")
        sys.exit()

    # Šifriranje korisničkog unosa pomoću navedenog ključa
    encrypted_text = implement_caesar_cipher(text_to_encrypt, key)

    # Prikaži šifrirani tekst
    print(f"{Fore.GREEN}[+] '{text_to_encrypt}' {Fore.MAGENTA}je šifriran kao {Fore.RED}{encrypted_text}")