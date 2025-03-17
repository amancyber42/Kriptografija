import base64
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import secrets
import os

def load_salt():
    """Učitaj sol iz datoteke salt.salt"""
    return open("salt.salt", "rb").read()  # Učitaj sol iz datoteke

def derive_key(salt, password):
    """Izvedite ključ iz lozinke koristeći sol"""
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return kdf.derive(password.encode())

def generate_key(password, salt, salt_size=32):
    """Generiraj ključ iz lozinke i spremljene soli"""
    derived_key = derive_key(salt, password)
    return base64.urlsafe_b64encode(derived_key).decode('utf-8')  # Vratiti Base64 kodirani ključ

def brute_force_decrypt(filename, salt, possible_passwords):
    """Brute-force dešifriranje datoteke pokušavajući sve moguće lozinke"""
    for password in possible_passwords:
        print(f"Pokušavam lozinku: {password}")
        key = generate_key(password, salt)
        try:
            decrypted_data = decrypt_file(filename, key)
            print("Dešifriranje uspješno!")
            return decrypted_data
        except Exception as e:
            print(f"Neuspješno dešifriranje s lozinkom: {password}")
    print("Brute-force dešifriranje nije uspjelo.")
    return None

def decrypt_file(filename, key):
    """Pokušaj dešifriranja datoteke s danim ključem"""
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    try:
        decrypted_data = f.decrypt(encrypted_data)
        return decrypted_data
    except cryptography.fernet.InvalidToken:
        raise ValueError("Pogrešan ključ za dešifriranje.")
