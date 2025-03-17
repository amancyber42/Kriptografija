import os
import json
import getpass
from cryptography.fernet import Fernet

# ----------------- Šifriranje i dešifriranje ----------------- #
# Provjera i učitavanje ključa
def load_key():
    if not os.path.exists('key.key'):
        key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(key)
    else:
        with open('key.key', 'rb') as key_file:
            key = key_file.read()
    return key

# Generiranje objekta za šifriranje
key = load_key()
cipher = Fernet(key)

def encrypt_password(password):
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    try:
        return cipher.decrypt(encrypted_password.encode()).decode()
    except Exception as e:
        print("[-] Pogreška pri dešifriranju:", str(e))
        return None

# ----------------- Rad s korisnicima ----------------- #
def register_user():
    username = input("Unesite korisničko ime: ")
    password = getpass.getpass("Unesite lozinku: ")
    encrypted_password = encrypt_password(password)

    user_data = {"username": username, "password": encrypted_password}
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)
    print("[+] Registracija uspješna.")

def login_user():
    if not os.path.exists('user_data.json'):
        print("[-] Korisnik nije registriran. Registrirajte se prvo.")
        return False

    with open('user_data.json', 'r') as file:
        user_data = json.load(file)

    username = input("Unesite korisničko ime: ")
    password = getpass.getpass("Unesite lozinku: ")

    if username == user_data['username']:
        decrypted_password = decrypt_password(user_data['password'])
        if decrypted_password == password:
            print("[+] Prijava uspješna.")
            return True
    print("[-] Neuspješna prijava.")
    return False

# ----------------- Upravljanje lozinkama ----------------- #
def add_password(website, password):
    if not os.path.exists('passwords.json'):
        passwords = {}
    else:
        with open('passwords.json', 'r') as file:
            passwords = json.load(file)

    encrypted_password = encrypt_password(password)
    passwords[website] = encrypted_password

    with open('passwords.json', 'w') as file:
        json.dump(passwords, file)
    print(f"[+] Lozinka za {website} spremljena.")

def get_password(website):
    if not os.path.exists('passwords.json'):
        print("[-] Nema spremljenih lozinki.")
        return None

    with open('passwords.json', 'r') as file:
        passwords = json.load(file)

    if website in passwords:
        encrypted_password = passwords[website]
        decrypted_password = decrypt_password(encrypted_password)
        return decrypted_password
    else:
        print(f"[-] Nema lozinke za {website}.")
        return None

def view_websites():
    if not os.path.exists('passwords.json'):
        print("[-] Nema spremljenih lozinki.")
        return

    with open('passwords.json', 'r') as file:
        passwords = json.load(file)

    print("\n[+] Spremljene web stranice:")
    for website in passwords:
        print(f"- {website}")

# ----------------- Glavni program ----------------- #
def main():
    while True:
        print("\n1. Registracija")
        print("2. Prijava")
        print("3. Izlaz")
        choice = input("Unesite svoj izbor: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            if login_user():
                # Opcije za upravljanje lozinkama nakon prijave
                while True:
                    print("\n1. Dodaj web stranicu")
                    print("2. Dohvati lozinku")
                    print("3. Pogledaj spremljene web stranice")
                    print("4. Odjava")
                    password_choice = input("Unesite svoj izbor: ")

                    if password_choice == '1':
                        website = input("Unesite naziv web stranice: ")
                        password = getpass.getpass("Unesite lozinku: ")
                        add_password(website, password)
                    elif password_choice == '2':
                        website = input("Unesite naziv web stranice: ")
                        password = get_password(website)
                        if password:
                            print(f"[+] Lozinka za {website}: {password}")
                    elif password_choice == '3':
                        view_websites()
                    elif password_choice == '4':
                        print("[+] Odjavljeni ste.")
                        break
                    else:
                        print("[-] Pogrešan unos. Pokušajte ponovno.")
        elif choice == '3':
            print("Izlaz iz programa...")
            break
        else:
            print("[-] Nevažeći izbor. Pokušajte ponovno.")

if __name__ == "__main__":
    main()
