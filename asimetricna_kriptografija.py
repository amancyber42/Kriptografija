from cryptography.hazmat.primitives.asymmetric import rsa # Uvoz funkcionalnosti generiranja RSA ključa
from cryptography.hazmat.primitives.asymmetric import padding # Uvoz padding za enkripciju i dešifriranje
from cryptography.hazmat.primitives import hashes # Uvoz algoritma hashiranja za enkripciju
from colorama import init, Fore # Uvoz formatiranja boja za terminal izlaz

init() # Inicijalizacija colorama za izlaz terminala u boji
# Generiranje par ključeva
private_key  = rsa.generate_private_key(
    public_exponent=65537, # Često korišten javni ekponent
    key_size=2048 # Veličina ključa u bitovima 
)

public_key = private_key.public_key() # Dobivanje odgovarajučeg javnog ključa
# Poruka kuju treba šifrirati
text_to_encrypt = b"Kriptografija je kull" # Poruka za šifriranje
# Šifriranje poruke
cipher_text = public_key.encrypt(
    text_to_encrypt, # Poruka za šifriranje
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()), # Generiranje maske funkcija sa SHA256 hash algoritmom
        algorithm=hashes.SHA256(), # Hash algoritam za enkripciju
        label=None # Izborna oznaka za prilagodbu (postavljanje na None)
    )
)

# Dešifriranje poruke
decrypted_message = private_key.decrypt(
    cipher_text, # Šifrirana poruka
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()), # Generiranje maske koja se koristi tijekom encripcije
        algorithm=hashes.SHA256(), # Hash algoritam koji se koristi tjekom enkripcije
        label=None # Izborna oznaka za prilagodbu (postavljanje na None)
    )
)

# Prikaz informacija u boji
print(f"{Fore.MAGENTA}Orginal Message: {text_to_encrypt}") # Ispis orginal poruke u boji
print(f"{Fore.RED}Encrypted Message: {cipher_text} ", cipher_text) # Ispis šifriranu poruku
print(f"{Fore.GREEN}Decrypted Message: {decrypted_message.decode()}") # Ispis dešifrirane poruke