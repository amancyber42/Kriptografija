# Provjerava preuzete datoteke
import argparse, hashlib, sys
from colorama import init, Fore

init()
# Definirati funkciju za izračunavanje sha256 hash datoteke
def calculate_hash(file_path):
    # napraviti sha256 objekt
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file: # Otvorite datoteku u binarnom načinu za čitanje (rb)
        while True:
            data = file.read(65536)  # čitati datoteku u dijelovima od 64KB
            if not data:
                break
            sha256_hash.update(data)
    return sha256_hash.hexdigest()

# Definirajte funkciju za provjeru izračunatog hash-a u odnosu na očekivani hash
def verify_hash(download_file, expected_hash):
    calculated_hash = calculate_hash(download_file)
    return calculated_hash == expected_hash

# Napravite parser za rukovanje argumentima naredbenog retka
parser = argparse.ArgumentParser(description="Provjerite hash preuzete softverske datoteke.")
# Definirajte dva argumenta naredbenog retka: 
# -f ili --file: Put do preuzete softverske datoteke (obavezno). 
# --hash: Očekivana vrijednost raspršivanja (obavezno).
parser.add_argument("-f", "--file", dest="downloaded_file", required=True, help="Put do preuzete softverske datoteke")
parser.add_argument("--hash", dest="expected_hash", required=True, help="Očekivani hash vrijednosti")
args = parser.parse_args()
if not args.downloaded_file or not args.expected_hash:
    print(f"{Fore.RED}[-] Navedite datoteku za provjeru valjanosti i njezin hash.")
    sys.exit()

# Provjerite je li hash datoteke točan pozivom verify_hash funkcije
if verify_hash(args.downloaded_file, args.expected_hash):
    print(f"{Fore.GREEN}[+] Hash provjera uspješna. Softver je autentičan.")
else:
    print(f"{Fore.RED}[-] Provjera raspršivanja nije uspjela. Softver nije autentičan.")