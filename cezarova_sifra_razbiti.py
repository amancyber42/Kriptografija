from colorama import Fore, init

init()

# Definiranje funkcije za enkripciju Caesar šifre
def implement_caesar_cipher(text, key, decrypt=False):
    # Inicijalizirati prazan niz za pohranu rezultata
    result = ""
    # Iterirati kroz svaki znak u ulaznom tekstu
    for char in text:
        if char.isalpha():
            shift = key if not decrypt else -key
            # Provjeriti jeli znak malo slovo
            if char.islower():
                result += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                # Primjeniti formulu za šifriranje Caesarove šifre za velika slova
                result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            # Ako znak nije abecedni ostaviti ga kakav jest, npr. brojevi, interpunkcija
            result += char
    # Vrati rezultat, a to je šifrirani ili dešifrirani tekst
    return result

# Definiranje funkcije za razbijanje Caesar šifre
def crack_caesar_cipher(ciphertext):
    # Iterirati kroz sve moguće tipke (0 do 25) jer postoji 26 slova
    for key in range(26):
        # Pozvati funkciju implement_caesar_cipher s trenutnim ključem za dešifriranje
        decrypted_text = implement_caesar_cipher(ciphertext, key, decrypt=True)
        # Ispiši rezultat prikazajući i dešifrirani tekst za svaki ključ
        print(f"{Fore.RED}Key {key}: {decrypted_text}")

# Pokrenite kontinuiranu petlju kako bi program nastavio raditi
while True:
    # Prihvatiti korisnički unos
    encrypted_text = input(f"{Fore.GREEN}[?] Unesi tekst/poruku za dešifriranje: ")
    # Provjeri ako korisnik ništa ne navodi
    if not encrypted_text:
        print(f"{Fore.RED}[-] Navedite tekst za dešifriranje.")
    else:
        crack_caesar_cipher(encrypted_text)
