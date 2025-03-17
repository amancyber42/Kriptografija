import sys 
from cryptography.fernet import Fernet 
from colorama import Fore, init

init()
# Funkcija za generiranje novog ključa za šitriranje i dešifriranje
def generate_key():
    return Fernet.generate_key()

# Funkcija za spremanje ključa u datoteku
def save_key(key, filename="secret_key.key"):
    with open(filename, "wb") as key_file:
        key_file.write(key)

# Funkcija za učitavanje ključa iz datoteke
def load_key(filename="secret_key.key"):
    return open(filename, "rb").read()

# Funkcija za šifriranje datoteke
def encrypt_file(key, input_file):
    cipher = Fernet(key) # šifra s priloženim ključem
    # čitanje otvorenog teksta iz ulazne datoteke
    with open(input_file, "rb") as file:
        plaintext = file.read()

    # šifrirati otvoreni tekst
    encrypted_data = cipher.encrypt(plaintext)
    # prebrisati ulaznu datoteku šifriranim podacima
    with open(input_file, "wb") as file:
        file.write(encrypted_data)

# Funkcija za dešifriranje datoteke
def decrypt_file(key, input_file):
    # stvoriti Fernet šifru s danim ključem
    cipher = Fernet(key)
    # pročitaj šifrirane podatke iz ulazne datoteke
    with open(input_file, "rb") as file:
        encrypted_data = file.read()
    # dekriptira podatke
    deccrypted_data = cipher.decrypt(encrypted_data)
    # prebrisati ulaznu datoteku s dekriptiranim podacima
    with open(input_file, "wb") as file:
        file.write(deccrypted_data)

# Zatražiti korisnički unos za odabir između enkripcije i dešifriranja
user_input = input(
    '[?] ] Želite li šifrirati ili dekriptirati datoteku?\n\nOdaberite opciju 1 za šifriranje i 2 za dešifriranje: ')
if user_input == '1':
    try:
        file_to_encrypt = input("Unesite stazu do ulazne datoteke: ") # uzeti ulaznu datoteku i ključ od korisnika
        key = generate_key() # generiran novi ključ i spremljen u datoteku
        save_key(key)
        encrypt_file(key, file_to_encrypt) # šifrirati ulaznu datoteku pomoću generiranog ključa
    except Exception:
        # Obradite iznimke i ispišite poruku o pogrešci
        print(f'{Fore.GREEN}[+] Provjerite jeste li unjeli valjanu datoteku.')
    else:
        # Ispis poruke o uspjehu ako je enkripcija uspješna
        print(f'{Fore.GREEN}[+] {file_to_encrypt} Šifriranje uspješno.')

# Proces dešifriranja
elif user_input == '2':
    try:
        input_to_decrypt = input("Unesite stazu do ulazne datoteke: ") # Uzmite ulaznu datoteku i ključ od korisnika
        loaded_key = load_key() # Učitaj ključ iz datoteke za dešifriranje
        decrypt_file(loaded_key, input_to_decrypt) # Dešifrirajte ulaznu datoteku koristeći učitani ključ
    except Exception:
        print(f'{Fore.RED}[+] Navedite valjanu datoteku: ')
    else:
        print(f'{Fore.GREEN}[+] Uspješno dešifrirano')
else:
    print(f'{Fore.RED}[-] Nevažeći unos!')
    sys.exit()