import pathlib
import secrets
import base64
import getpass
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import os

def generate_salt(size=16):
    """Generiraj sol koja se koristi za derivaciju ključa, 'size' je 
    duljina soli za generiranje"""
    return secrets.token_bytes(size)

def derive_key(salt, password):
    """Izvedite ključ iz 'lozinke' koristeći prosljeđeni 'salt'"""
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return kdf.derive(password.encode())

def load_salt():
    # učitaj sol iz datoteke salt.salt
    return open("salt.salt", "rb").read()

def generate_key(password, salt_size=32, load_existing_salt=False, save_salt=True):
    """Generiraj ključ iz 'lozinke' i soli.
    Ako je 'load_existing_salt'True, učitat če se sol iz datoteke u trenutnom direktoriju
    pod nazivom 'salt.salt'.
    Ako je 'save_salt'True, tada če se generirati nova sol
    i spremiti ga u 'salt.salt'."""
    if load_existing_salt:
        # učitaj postoječu sol
        salt = load_salt()
    elif save_salt:
        # generirajte novu sol i spremite ju 
        salt = generate_salt(salt_size)
        with open("salt.salt", "wb") as salt_file:
            salt_file.write(salt)
    # generirajte ključ iz soli i lozinke
    derived_key = derive_key(salt, password)
    # kodirajte ga koristeći Base64 i vratite
    return base64.urlsafe_b64encode(derived_key)

# Enkripcija datoteke
def encrypt(filename, key):
    """S obzirom na naziv datoteke (str) i ključ (bajtovi), šifrira datoteku i napiši"""
    f = Fernet(key)
    with open(filename, "rb") as file:
        # čitanje svih podataka datoteke
        file_data = file.read()
        # Šifrirani podaci
        encrypted_data = f.encrypt(file_data)
        # zapišite šifriranu datoteku
        with open(filename, "wb") as file:
            file.write(encrypted_data)

# Dešifriranje datoteke
def decrypt(filename, key):
    """S obzirom na naziv datoteke (str) i ključ (bajtovi), dekriptiraj datoteku i napiši"""
    f = Fernet(key)
    with open(filename, "rb") as file:
        # čitanje šifriranih podataka
        encrypted_data = file.read()
        # dešifriranje podataka
        try:
            decrypted_data = f.decrypt(encrypted_data)
        except cryptography.fernet.InvalidToken:
            print("[!] Nevažeći token, najvjerotnije je lozinka netočna")
            return
        # zapišite orginalnu datoteku
        with open(filename, "wb") as file:
            file.write(decrypted_data)

# Šifriranje i dešifriranje mapa
def encrypt_folder(foldername, key):
    # ako je to mapa šifrirajte cijelu mapu
    for child in pathlib.Path(foldername).glob("*"):
        if child.is_file():
            print(f"[*] Šifriranje {child}")
            # šifrirati datoteku
            encrypt(child, key)
        elif child.is_dir():
            # ako je to mapa šifriraj cijelu mapu
            encrypt_folder(child, key)

# Dešifriranje mapa
def decrypt_folder(foldername, key):
    # ako je to mapa dešifrirajte cijelu mapu
    for child in pathlib.Path(foldername).glob("*"):
        if child.is_file():
            print(f"[*] Dešifriranje {child}")
            # dešifrirati datoteku
            decrypt(child, key)
        elif child.is_dir():
            # ako je to mapa dešifriraj mapu
            decrypt_folder(child, key)

if __name__ == "__main__":
    import argparse
    
    # Kreiranje parsera za argumente
    parser = argparse.ArgumentParser(description="Skripta za šifriranje i dešifriranje datoteka/mapa s lozinkom")
    parser.add_argument("path", help="Put do datoteke ili mape za šifriranje/dešifriranje")
    parser.add_argument("-s", "--salt-size", help="Veličina soli (default: 32 bajta)", type=int, default=32)
    parser.add_argument("-e", "--encrypt", action="store_true", help="Šifriranje datoteke/mape")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Dešifriranje datoteke/mape")

    # Parsiranje argumenata
    args = parser.parse_args()

    # Provjera da li je šifriranje ili dešifriranje odabrano (ne oba)
    if args.encrypt and args.decrypt:
        raise ValueError("Ne možete istovremeno koristiti opcije -e (šifriranje) i -d (dešifriranje).")
    if not args.encrypt and not args.decrypt:
        raise ValueError("Morate odabrati jednu od opcija: -e (šifriranje) ili -d (dešifriranje).")

    # Traženje lozinke
    password = getpass.getpass("Unesite lozinku: ")

    # Generiranje ključa
    if args.encrypt:
        key = generate_key(password, salt_size=args.salt_size, save_salt=True)
    else:  # args.decrypt
        key = generate_key(password, load_existing_salt=True)

    # Provjera je li put datoteka ili mapa, te izvođenje akcije
    if args.encrypt:
        if os.path.isfile(args.path):
            encrypt(args.path, key)
            print(f"Datoteka '{args.path}' uspješno šifrirana.")
        elif os.path.isdir(args.path):
            encrypt_folder(args.path, key)
            print(f"Mapa '{args.path}' uspješno šifrirana.")
        else:
            raise FileNotFoundError(f"Put '{args.path}' nije pronađen.")

    elif args.decrypt:
        if os.path.isfile(args.path):
            decrypt(args.path, key)
            print(f"Datoteka '{args.path}' uspješno dešifrirana.")
        elif os.path.isdir(args.path):
            decrypt_folder(args.path, key)
            print(f"Mapa '{args.path}' uspješno dešifrirana.")
        else:
            raise FileNotFoundError(f"Put '{args.path}' nije pronađen.")