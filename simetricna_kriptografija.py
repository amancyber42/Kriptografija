# Simetrična kriptografija
from cryptography.fernet import Fernet
from colorama import Fore, init

# Inicijalizacija colorama
init()
# Generiranje ključa
key = Fernet.generate_key()
# Stvaranje Fernet šifre poomoću generiranog ključa
cipher_suite = Fernet(key)
# Šifriranje poruke (b poruku koju treba šifrirati)
plaintext = b"Pozdrav iz Zagreba"
print(f"{Fore.BLUE}Plain Text: {plaintext}")
ciphertext = cipher_suite.encrypt(plaintext)

# Prikaži rezultate ispisa koristeći boju magenta i crvenu za bolje vizualne prikaze
print(f"{Fore.MAGENTA}Generated key: {key}")
print(f"{Fore.RED}Encrypted Message: {ciphertext}\n")

# Korištenje istog kljuća za stvaranje Fernet šifre (za dešifriranje)
decipher_suite = Fernet(key)
# Dešifriranje poruke
decrypted_message = decipher_suite.decrypt(ciphertext)
# Ispis dešifrirane poruke
print(f"{Fore.GREEN}Decrypted message: {decrypted_message.decode()}")